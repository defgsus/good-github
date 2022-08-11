## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-10](docs/good-messages/2022/2022-08-10.md)


2,010,335 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,010,335 were push events containing 3,149,013 commit messages that amount to 220,529,208 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [ro-ot/linux](https://github.com/ro-ot/linux)@[1639a49ccd...](https://github.com/ro-ot/linux/commit/1639a49ccdce58ea248841ed9b23babcce6dbb0b)
#### Wednesday 2022-08-10 00:00:08 by Yang Xu

fs: move S_ISGID stripping into the vfs_*() helpers

Move setgid handling out of individual filesystems and into the VFS
itself to stop the proliferation of setgid inheritance bugs.

Creating files that have both the S_IXGRP and S_ISGID bit raised in
directories that themselves have the S_ISGID bit set requires additional
privileges to avoid security issues.

When a filesystem creates a new inode it needs to take care that the
caller is either in the group of the newly created inode or they have
CAP_FSETID in their current user namespace and are privileged over the
parent directory of the new inode. If any of these two conditions is
true then the S_ISGID bit can be raised for an S_IXGRP file and if not
it needs to be stripped.

However, there are several key issues with the current implementation:

* S_ISGID stripping logic is entangled with umask stripping.

  If a filesystem doesn't support or enable POSIX ACLs then umask
  stripping is done directly in the vfs before calling into the
  filesystem.
  If the filesystem does support POSIX ACLs then unmask stripping may be
  done in the filesystem itself when calling posix_acl_create().

  Since umask stripping has an effect on S_ISGID inheritance, e.g., by
  stripping the S_IXGRP bit from the file to be created and all relevant
  filesystems have to call posix_acl_create() before inode_init_owner()
  where we currently take care of S_ISGID handling S_ISGID handling is
  order dependent. IOW, whether or not you get a setgid bit depends on
  POSIX ACLs and umask and in what order they are called.

  Note that technically filesystems are free to impose their own
  ordering between posix_acl_create() and inode_init_owner() meaning
  that there's additional ordering issues that influence S_SIGID
  inheritance.

* Filesystems that don't rely on inode_init_owner() don't get S_ISGID
  stripping logic.

  While that may be intentional (e.g. network filesystems might just
  defer setgid stripping to a server) it is often just a security issue.

This is not just ugly it's unsustainably messy especially since we do
still have bugs in this area years after the initial round of setgid
bugfixes.

So the current state is quite messy and while we won't be able to make
it completely clean as posix_acl_create() is still a filesystem specific
call we can improve the S_SIGD stripping situation quite a bit by
hoisting it out of inode_init_owner() and into the vfs creation
operations. This means we alleviate the burden for filesystems to handle
S_ISGID stripping correctly and can standardize the ordering between
S_ISGID and umask stripping in the vfs.

We add a new helper vfs_prepare_mode() so S_ISGID handling is now done
in the VFS before umask handling. This has S_ISGID handling is
unaffected unaffected by whether umask stripping is done by the VFS
itself (if no POSIX ACLs are supported or enabled) or in the filesystem
in posix_acl_create() (if POSIX ACLs are supported).

The vfs_prepare_mode() helper is called directly in vfs_*() helpers that
create new filesystem objects. We need to move them into there to make
sure that filesystems like overlayfs hat have callchains like:

sys_mknod()
-> do_mknodat(mode)
   -> .mknod = ovl_mknod(mode)
      -> ovl_create(mode)
         -> vfs_mknod(mode)

get S_ISGID stripping done when calling into lower filesystems via
vfs_*() creation helpers. Moving vfs_prepare_mode() into e.g.
vfs_mknod() takes care of that. This is in any case semantically cleaner
because S_ISGID stripping is VFS security requirement.

Security hooks so far have seen the mode with the umask applied but
without S_ISGID handling done. The relevant hooks are called outside of
vfs_*() creation helpers so by calling vfs_prepare_mode() from vfs_*()
helpers the security hooks would now see the mode without umask
stripping applied. For now we fix this by passing the mode with umask
settings applied to not risk any regressions for LSM hooks. IOW, nothing
changes for LSM hooks. It is worth pointing out that security hooks
never saw the mode that is seen by the filesystem when actually creating
the file. They have always been completely misplaced for that to work.

The following filesystems use inode_init_owner() and thus relied on
S_ISGID stripping: spufs, 9p, bfs, btrfs, ext2, ext4, f2fs, hfsplus,
hugetlbfs, jfs, minix, nilfs2, ntfs3, ocfs2, omfs, overlayfs, ramfs,
reiserfs, sysv, ubifs, udf, ufs, xfs, zonefs, bpf, tmpfs.

All of the above filesystems end up calling inode_init_owner() when new
filesystem objects are created through the ->mkdir(), ->mknod(),
->create(), ->tmpfile(), ->rename() inode operations.

Since directories always inherit the S_ISGID bit with the exception of
xfs when irix_sgid_inherit mode is turned on S_ISGID stripping doesn't
apply. The ->symlink() and ->link() inode operations trivially inherit
the mode from the target and the ->rename() inode operation inherits the
mode from the source inode. All other creation inode operations will get
S_ISGID handling via vfs_prepare_mode() when called from their relevant
vfs_*() helpers.

In addition to this there are filesystems which allow the creation of
filesystem objects through ioctl()s or - in the case of spufs -
circumventing the vfs in other ways. If filesystem objects are created
through ioctl()s the vfs doesn't know about it and can't apply regular
permission checking including S_ISGID logic. Therfore, a filesystem
relying on S_ISGID stripping in inode_init_owner() in their ioctl()
callpath will be affected by moving this logic into the vfs. We audited
those filesystems:

* btrfs allows the creation of filesystem objects through various
  ioctls(). Snapshot creation literally takes a snapshot and so the mode
  is fully preserved and S_ISGID stripping doesn't apply.

  Creating a new subvolum relies on inode_init_owner() in
  btrfs_new_subvol_inode() but only creates directories and doesn't
  raise S_ISGID.

* ocfs2 has a peculiar implementation of reflinks. In contrast to e.g.
  xfs and btrfs FICLONE/FICLONERANGE ioctl() that is only concerned with
  the actual extents ocfs2 uses a separate ioctl() that also creates the
  target file.

  Iow, ocfs2 circumvents the vfs entirely here and did indeed rely on
  inode_init_owner() to strip the S_ISGID bit. This is the only place
  where a filesystem needs to call mode_strip_sgid() directly but this
  is self-inflicted pain.

* spufs doesn't go through the vfs at all and doesn't use ioctl()s
  either. Instead it has a dedicated system call spufs_create() which
  allows the creation of filesystem objects. But spufs only creates
  directories and doesn't allo S_SIGID bits, i.e. it specifically only
  allows 0777 bits.

* bpf uses vfs_mkobj() but also doesn't allow S_ISGID bits to be created.

The patch will have an effect on ext2 when the EXT2_MOUNT_GRPID mount
option is used, on ext4 when the EXT4_MOUNT_GRPID mount option is used,
and on xfs when the XFS_FEAT_GRPID mount option is used. When any of
these filesystems are mounted with their respective GRPID option then
newly created files inherit the parent directories group
unconditionally. In these cases non of the filesystems call
inode_init_owner() and thus did never strip the S_ISGID bit for newly
created files. Moving this logic into the VFS means that they now get
the S_ISGID bit stripped. This is a user visible change. If this leads
to regressions we will either need to figure out a better way or we need
to revert. However, given the various setgid bugs that we found just in
the last two years this is a regression risk we should take.

Associated with this change is a new set of fstests to enforce the
semantics for all new filesystems.

Link: https://lore.kernel.org/ceph-devel/20220427092201.wvsdjbnc7b4dttaw@wittgenstein [1]
Link: e014f37db1a2 ("xfs: use setattr_copy to set vfs inode attributes") [2]
Link: 01ea173e103e ("xfs: fix up non-directory creation in SGID directories") [3]
Link: fd84bfdddd16 ("ceph: fix up non-directory creation in SGID directories") [4]
Link: https://lore.kernel.org/r/1657779088-2242-3-git-send-email-xuyang2018.jy@fujitsu.com
Suggested-by: Dave Chinner <david@fromorbit.com>
Suggested-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-and-Tested-by: Jeff Layton <jlayton@kernel.org>
Signed-off-by: Yang Xu <xuyang2018.jy@fujitsu.com>
[<brauner@kernel.org>: rewrote commit message]
Signed-off-by: Christian Brauner (Microsoft) <brauner@kernel.org>

---
## [AceofSpades5757/helix](https://github.com/AceofSpades5757/helix)@[973c51c3e9...](https://github.com/AceofSpades5757/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Wednesday 2022-08-10 00:08:25 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[f0cef47678...](https://github.com/Zonespace27/Skyrat-tg/commit/f0cef47678384716080d4cc2adfa8be85b9ddc69)
#### Wednesday 2022-08-10 00:28:40 by SkyratBot

[MIRROR] Adds the Mothroach [MDB IGNORE] (#15399)

* Adds the Mothroach (#68763)

About The Pull Request

Yup. That's pretty much it. This PR adds the Mothroach to the game, described as "An ancient ancestor of the moth that surprisingly looks like the crossbreed of a moth and a cockroach."

Do you love the Mothroach? Then you can cuddle with it and pat it, as well as place it on your head for extra cuteness.
What if you hate it, though? You can always kill and butcher Mothroaches in order to mass produce moth plushes for your own profit... How fun!

Either way, you win!

The Mothroach can be picked up and has a special on-head sprite (which looks really cute). It is able to vent-crawl and you may get one by randomly summoning a friendly mob through the gold slime extracts, or by ordering one through the Cargo Requests. After butchered, you may use its hide, a heart, and some cloth to craft a moth plushie, the most devilish of Devil's designs.

Full Preview of all the Sprites (NEW): https://www.youtube.com/watch?v=pdg8FTNEYjI
Preview of some of the Sprites (OLD): https://www.youtube.com/watch?v=9A-8hGCiW0s
In-hand, on-head, and grounded Mothroach sprite credits go to ValuedEmployee.
I did the Mothroach hide sprite though!
Why It's Good For The Game

The Mothroach is incredibly cute and a neat, fresh, new piece of content. Although it could use some future repurposing, right now it's simply a cute exotic pet with a few interactions.

These cute sprites are just too good to go to waste...

I keep seeing people complain about the lack of new content. Well, here's something niche that won't break the whole balance of the game and that will be cute. I seriously cannot see a motive not to add this to the game. Just because it isn't a powergaming tool or something that is seen every shift, that doesn't mean that it won't have a positive influence on the game. As I have stated, right now the Mothroaches are underperforming in terms of interactions and ways of getting them, but adding them is the first step to later improve them.
Changelog

cl
add: The Mothroach, your new local exotic pet
add: Mothroach Hide and Mothroach Meat
add: New crafting recipe for the Moth Plush: 1 Mothroach Hide; 1 heart; 3 cloth
fix: Fixes dead mobs on-head not having sprites
/cl

* Adds the Mothroach

Co-authored-by: Justice <42555530+Justice12354@users.noreply.github.com>

---
## [Irinek0/iri-sojourn-station](https://github.com/Irinek0/iri-sojourn-station)@[f5da3823ac...](https://github.com/Irinek0/iri-sojourn-station/commit/f5da3823ac07f22c72a19e8191a4567882020f7f)
#### Wednesday 2022-08-10 00:46:07 by nikothedude

holy SHIT i hate saycode (hotfix) (#3816)

* whydidthishappen

* fuck

---
## [Irrational-Encoding-Wizardry/lvsfunc](https://github.com/Irrational-Encoding-Wizardry/lvsfunc)@[9a1fe38787...](https://github.com/Irrational-Encoding-Wizardry/lvsfunc/commit/9a1fe387874f01666fe7fe708e8108fe059ce1b1)
#### Wednesday 2022-08-10 01:04:41 by Setsugennoao

Update vs-* packages and other stuff (#145)

* Bump up requirements

* Remove toolz dependency

* Sort imports

* Update stubs

* Update typing to 3.10

* Update vsscale in scale submodule

* Remove unused import

* Remove ugly copypaste

* Holy shit revert the vapoursynth stubs move

* ...and the formatting lol

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[931b7187bd...](https://github.com/sojourn-13/sojourn-station/commit/931b7187bd31e71d2a16792b7b2dd042cb049d97)
#### Wednesday 2022-08-10 01:56:09 by nikothedude

"Optimizes" superior mobcode with somewhat of a nuclear option in terms of optimization. Fixes stealth bird targetting, fixes mobs being permastunned as well as not getting up from knockdowns.  (#3812)

* fuck

* fucwkc

* holy fuck

* i hate this

* FUCK YOUBALTIMORE

* superi

---
## [StarbloomSS13/StarbloomSS13](https://github.com/StarbloomSS13/StarbloomSS13)@[dcd6ff7eed...](https://github.com/StarbloomSS13/StarbloomSS13/commit/dcd6ff7eede6f473b20eb41af32c03e8fe27b055)
#### Wednesday 2022-08-10 02:05:13 by Cheshify

Merge pull request #192 from unit0016/purple-crowbar-patch

[FUCK] Fixes purple crowbars / inducers because of the shitty ass modular aesthetics bullshit

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7ae0941f15...](https://github.com/treckstar/yolo-octo-hipster/commit/7ae0941f1527ad8d6d0aa2d9116939f0ee3b8ef1)
#### Wednesday 2022-08-10 02:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [SaiGaneshChintala/Logistic_Regression_Purchase_Item_Predict_Future_Data](https://github.com/SaiGaneshChintala/Logistic_Regression_Purchase_Item_Predict_Future_Data)@[80d281aa46...](https://github.com/SaiGaneshChintala/Logistic_Regression_Purchase_Item_Predict_Future_Data/commit/80d281aa46f6eb4902e77bf5e672e1ad89c34a32)
#### Wednesday 2022-08-10 04:15:21 by Sai Ganesh

README.md

Logistic_Regression_Purchase_Item_Predict_Future_Data

LogisticRegression classifier used for predicting the item is Purchase or not along with Predict Future_Data
Logistic Regression
Importing the libraries

import numpy as np import matplotlib.pyplot as plt import pandas as pd
Importing the dataset

dataset=pd.read_csv(r"C:\Users\SAI\Desktop\Data science\June month\1st 15. Logistic regression with future prediction\15. Logistic regression with future prediction\Social_Network_Ads.csv") #this datasset contian information of user and socianl network, those features are - userid,gender,age,salary,purchased #social network has several business client which can put their into social networks and one of the client is car company , this company has newly lunched XUV in rediculous price or high price #we will see which of the user in this social network are going to buy brand new xuv car #Last column tell us user purchased the car yes-1 // no-0 & we are going to build the model that is goint to predict if the user is going to buy xuv or not based on 2 variable based on age & estimated salery #so our matrix of feature is only these 2 column & we gonna find some corelation b/w age and estimated salary of user and his decission to purchase the car [yes or no] #so i need 2 index and rest of index i will remove for this i have to use slicing operator #1 means - the user going to buy the car & 0 means - user is not going to buy the car

X = dataset.iloc[:, [2, 3]].values y = dataset.iloc[:, -1].values
Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split #for this observation let me selcted as 100 observaion for test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

#we are going to predict which users are going to predit xuv,
Feature Scaling

from sklearn.preprocessing import StandardScaler sc = StandardScaler() X_train = sc.fit_transform(X_train) X_test = sc.transform(X_test) #we mentioned feature scaling only to independent variable not dependent variable at all

#datapreprocessing done guys upto this part

#******************************************************************************************

#Next step is we are going to build the logistic model and appy this model into our dataset #This is linear model library thats why we called from sklear.linear_model
Training the Logistic Regression model on the Training set

from sklearn.linear_model import LogisticRegression classifier = LogisticRegression(penalty='l2', solver='sag') classifier.fit(X_train, y_train) #we have to fit the logistic regression model to our training set
Predicting the Test set results

y_pred = classifier.predict(X_test) #now you compare X_test with y_pred, x-test we have age and salary , #if u look at the first observation this user is not be able to buy the car but if you look at observation 7 then that user is going to buy the car #in this case logistic regression model classify the which users are going to buy the car or not

#we build our logistic model and fit it to the training set & we predict our test set result

#now we will use the confusion matrix to evalute
Making the Confusion Matrix

from sklearn.metrics import confusion_matrix cm = confusion_matrix(y_test, y_pred) print(cm) #we can say that 65 + 24 = 89 correct prediction we found & 8+3 = 11 incorrect prediction made
This is to get the Models Accuracy

from sklearn.metrics import accuracy_score ac = accuracy_score(y_test, y_pred) print(ac)

bias = classifier.score(X_train, y_train) print(bias)

variance = classifier.score(X_test, y_test) print(variance)
This is to get the Classification Report

from sklearn.metrics import classification_report cr = classification_report(y_test, y_pred) cr

#****************** 10. check the future data with predicated data furture_dataset=pd.read_csv(r"C:\Users\SAI\Desktop\projects\logisitic Regression\Future prediction1.csv")

X_new=furture_dataset.iloc[:,[2,3]].values X_new=sc.fit_transform(X_new) y_Logi_pred=classifier.predict(X_new) #********************* 11. Dataframe Creation import os df1=pd.DataFrame(y_Logi_pred) df1=df1.rename(columns={'NAN':'Index', 0:'modelpredicated'}) df1.to_csv("C:\Users\SAI\Desktop\projects\logisitic Regression\Future prediction1.csv")
Footer

---
## [247arjun/password-purgatory-api](https://github.com/247arjun/password-purgatory-api)@[63dd1c4214...](https://github.com/247arjun/password-purgatory-api/commit/63dd1c42147c867a1fa4a96ec3519d09a37a2369)
#### Wednesday 2022-08-10 05:08:08 by Arjun G

Include one season of the year

Remember the joke about PasswordSummer2022 changing to PasswordWinter2022 on rotation? Yeah, this is that.

---
## [Prashant-1695/kernel_xiaomi_lavender-4.19](https://github.com/Prashant-1695/kernel_xiaomi_lavender-4.19)@[38b0bd0f25...](https://github.com/Prashant-1695/kernel_xiaomi_lavender-4.19/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Wednesday 2022-08-10 06:20:15 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [dsonbill/ReactionaryParticulateMatterInteractor](https://github.com/dsonbill/ReactionaryParticulateMatterInteractor)@[5f2003973a...](https://github.com/dsonbill/ReactionaryParticulateMatterInteractor/commit/5f2003973a5a252c3c9e23f6e2c138654bc422ad)
#### Wednesday 2022-08-10 06:41:11 by William C. Donaldson

The hole is closing in on you.

So leave my stuff alone and we won't do what we have to do.

Sucka-ass bitch hoe.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[5dc17bd865...](https://github.com/LemonInTheDark/tgstation/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Wednesday 2022-08-10 07:41:29 by san7890

Security's Scaling Departmental Accesses - More Pop, More Problems (#68534)

lternative to #68527
About The Pull Request

Hey there,

This is an alternative PR that I concocted based on talking with Goof on that PR. Basically, we already have a nicely complicated system to track and balance the number of security officers we have in a shift based on some config coefficient setting, by which we can set the amount of lockers that spawn in on the start of a round, as well as determine truly how many security officers we have.

image

So, I've decided to leverage this in another way. Basically, based on the number of security officers in a shift, their specific departmental officers will also get more (elevated) accesses. They already start with a certain amount of access, but they can get more if it is a low-pop shift with the mechanic introduced in this PR. For example, an Engineering Security Officer can access Atmospherics and Engineering departments by default, but they can't access Telecommunications unless there is a lower population of players AT SHIFT START. Same for a Medical Security Officer accessing Medbay, but not Plumbing.

Update: I have made it such that there are three system that server operators can set:

They can use the Scaling System that operates in the same method outlined in the rest of the PR.
They can disable giving departmental security officers "elevated access" (such as access beyond the "front doors") to these officers.
Finally, they can also just always ensure that departmental security officers get the maximal accesses possible.

The default setting is the "Scaling System" outlined in this PR, which is already dependent on the general Security Officer Scaling Co-Efficient.
Why It's Good For The Game

I think it's better to involve some more nuanced config scaling that we already have present in the game. The major theme that we want to avoid is that departmental security officers having maximal accesses when there is an already large number of persons on the security force will result in "miserable" shifts for the common person working within a department (security metaprotections). However, some server operators (as well as server cultures) tend to have very wide ranges in how many security officers they have on a shift-by-shift basis. One day, you could have 0-2 security officers, the next, you could have 4-6. It's all variable on who's playing (as always). There is also a significant variation between server to server in regards to how many security officer slots you tend to have on spawn, but this is already manageable by the security officer co-efficient in config.

I believe this PR is an acceptable proposal within the bounds of #68527 (comment) , although it may bend certain aspects of it, I definitely do see where some people may be coming from. I believe I've adjusted the accesses to a "sane"/justifiable amount, but I'll come back to think on everything.

"Red-tiding" may or may not be a problem, but there's always just going to be something inherently silly with a security officer being able to walk into plumbing to start plumbing. I hoped that this would be seen as a positive as opposed to a negative, but I can see how it could negatively impact player experience. HOWEVER, interplayer experience should not be handled by the codebase in all aspects, which is why I've also passed in the associated config variables, so that server operators (who should handle the interplayer experience with their level of discretion and nuance) can.
What accesses are where?

The general philosophy as I thought through designing this would be that the security officer should at the very least have general "front-door" access into a department, and maybe something benign. If we had even more per-door accesses, this could definitely be a bit more granular (one example I can think of would only atmospherics technicians having access to the "Pump Room", while Security Officers would not. However, this is for a later date). So, you have the "default" access you always get, and a potential to get "elevated" access as a Departmental Security Officer.

The balances are as such:

The Cargo Security Officer will have access to the Cargo Bay, Mining Section, and the Shipping Room. The first two are rather general areas, with the Shipping Room being a rather good help for rescuing (or "rescuing") flushed crewmembers when the cargo techies can't get to it/no AI. The Auxiliary Base is not essential to the security officer's functions, and the mining station helps restrict access further on stations like IceBox. This would also grant them extra access to the Lavaland base, so let's snip that out.

The Engineering Security Officer should have access to only general Engineering and Atmospherics. Construction pertains to certain rooms in maintenance I believe, and Engine-Equipment should be the one that grants access to APCs (lol). I don't think a security officer should have the latter one to be honest, but I think we'll be stretching the scope of this PR. Telecommunications is a bit weird, it's a critical station function, but I think you also shouldn't be able to nick one goon's ID and have access, so let's give it to them only when it's "needed".

The Medical Security Officer should have access to only the general Medbay Area and the Morgue, in case someone starts trotting on the doctor's turf, or if there's someone doing unsavory things to the bodies while the doctors are away. They will not have access to the specialized (dangerous) areas unless the ratio of secoffs to the population is low enough should it necessitate it (Plumbing Room, Pharmacy, Virology). I also added Surgery to the scaling access, but I'm iffy on that one. I don't particularly see why they should have it as a base access, but I also do see there being some need in dire straits (in relation to helping people, not tiding).

The Science Security Officer definitely got a huge cut. They now only have general access to R&D and normal scientist areas like the lathe room, circuits lab (presumably)since these are generally trafficked areas, but I definitely clamped down on additional access they might get in a "normally balanced" situation (no ordnance+storage, no xenobio, no genetics, no to robotics, etc.) They don't have a particular use in these areas and can even be a bit obstructive to flow in normal circumstances, but if abnormal circumstances arise and there's not a lot of security hands-on-deck, then their access is expanded.

Honestly, balancing this both makes sense and is conversely rather odd. I'm just running off what we already hold to be true and expected (or at least as of the last two months), and we can go from there.
Changelog

cl
balance: Nanotrasen realized that the more access they had on their cards was costing them a pretty penny, so they trimmed back the number of accesses a certain departmental Security Guard might have. However, any given guard will get back a greater amount of accesses depending on how many security guards there are in relation to the population.
config: Hey server operators, listen! We've changed up how Departmental Security Officers get their accesses, so be sure to review the DEPSEC_ACCESS_LEVEL config number to see what you want to work best for your server.
/cl

Also, every single line of code found in 4533f07 that is now presently in this PR is deliberate

---
## [Marfjeh/ViaVersion](https://github.com/Marfjeh/ViaVersion)@[94d17e5a76...](https://github.com/Marfjeh/ViaVersion/commit/94d17e5a76ab97d8d1aafeb94c22870688ff1cfd)
#### Wednesday 2022-08-10 09:19:27 by Marf

Removed crybaby bullshit about message signing.

Oh no! we're scary that we want to keep ownership of our own damn
server.

---
## [Havoc-Devices/kernel_xiaomi_lavender](https://github.com/Havoc-Devices/kernel_xiaomi_lavender)@[913870e6a0...](https://github.com/Havoc-Devices/kernel_xiaomi_lavender/commit/913870e6a08b069c8ff8d1c4f9146bcdaa69b4ec)
#### Wednesday 2022-08-10 09:31:07 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1f36e77232...](https://github.com/mrakgr/The-Spiral-Language/commit/1f36e772323f19dc8ea32b432c3e6d4399c5352d)
#### Wednesday 2022-08-10 10:49:34 by Marko Grdinić

"9am. I am up. Let me chill for a while and then I will start.

9:30am. Let me start. First let me check the mail.

> Hi Marko,
> We saw your profile on Indeed and thought you would be a great match for the Senior Software Engineer - Java Front End - Remote opportunity. This job was posted today. Please submit a quick application if you have any interest.

I must have forgotten to remove the resume I have on Indeed. Since they are telling me it is a Java position, it must be the generic tech soup one. ...No, it the older 6 pager with a lot of text. I guess I'll leave it to see what comes in. I've never gotten an email like this from Indeed.

That having said, of course, I clicked on 'Not Interested'. Me programming front ends in Java? Surely, you jest world. At least make it .NET.

9:35am. What I am really checking the email is for Tenstorrent and Graphcore replies. I should at least get access to their cloud offerings at some point. I want that for the sake of figuring out the programming model of those chips. If they are true multicore processors then my plans might have some potential. But if it turns out despite the hype they are just deep learning accelerators and have no general purpose programming capability, then I should just give up on the 20s.

I want to try programming new kinds of hardware so I can develop myself as a programmer more. Even if they lack the computational capacity to do the kinds of projects that I want, doing that might still give me some benefit. But if their programming model is too restricted, then there is no point in touching them at all.

9:45am. My failure really damaged me for ML work. It really is sigh worthy.

Forget that. Let me focus on writing. I can get a job years down the road should I need to.

In terms of concrete benefits, what I should be mining are the Royal Road readership base. Last time I was not really thinking at all, but if I want to know where I stand as a writer, I should do this for a while and see what reactions do I get.

9:50am. Let focus on finishing this chapter. This one and another chapter more, and I should start getting ready for publication on RR.

$$$

(Euclid's Room, Save Point - Step on the path of transcendence)

[Decision]
1) I'll do the whole brain conversion and digitize myself.
2) Killing myself for power does not make sense.

[Choice - I'll do the whole brain conversion and digitize myself.]

[Pathos check ?? Succeeded]

A wave of fear comes over me as I consider the decision, but I push forward, not giving in to cowardice. There are always reasons not to put in effort. The path being insane is just an excuse. I won't hold back here. I should always be going forward and striving to reach greater heights.

I grip the core in my hand tightly and clench it. I can feel my heart brimming with determination, it is right to feel fear as well. Going against fear is exactly what this situation should be. No matter what the reasons are, it is my duty to go where others would not dare. If there are hardships, I want to keep challenging them forever.

[Gnosis check ?? Succeeded]

Even a little kid could point out to me that if I scan my brain and copy it to a computer, that the copy would not be me. Likewise, if I back up myself on the auxiliary core in my hand, reconstruct my brain into a core and then copy myself back, that would not be me. But I do not take advice on how to live my life from children. I want to experience what it is like to die, and yet keep moving forward.

[Externus check ?? Succeeded]

It does not matter what my parents or anybody else would think. They don't need to find out, and I won't tell them. This will be my secret. What matters most of all is power. Nobody is going to give it to me. I have to get it by myself.

I close my eyes, bring up the status window in my mind and find where the conversion options are. Next where the brain link option was, there was the Full Brain Conversion button. I find and then press on it.

A window shows up. The first thing to grab my attention there is a row of skulls. It is clearly a warning to emphasize that what I might be doing is dangerous. The disclaimer explains the following:

> The full brain conversion option is for those who want to replace their biological brain with the universal brain core.
> Compared to merely copying a scan of your mind to an already existing core, the resulting brain replacement will allow you to reuse your existing biological body and tightly integrate it with the new brain.
> The brain core used to initiate the process (activation core) will be used to store your scan during the process, after which it will be copied back into the core (result core).
> Besides replacing the brain, the process will modify the body so there aren't adverse effects during or after the process. It will maintain proper posture, heartbeat and breathing as well as other minor subconscious functionality the brain provides to the body.
> The entire process after it has been started should take around 5 minutes.
> Should it fail for any reason, to prevent absolute death the activation core's entity will be activated, otherwise the result core's entity will take over as intended while the activation core's entity will remain dormant as inactive data.
> Before starting the process, it is recommended to take out a watch and keep track of time. Subjectively, the entire process shouldn't involve any pain or discomfort. The only sign of it succeeding will be a sudden timelapse.
> It is recommended to do this process in a safe space like a locked bathroom or one's own room. If you try to do it while driving a car, it will likely result in a crash.
> If your body dies in the process of brain conversion, the conversion is likely to still succeed, but you will be trapped in a dead body, unable to move or otherwise control it.
> As the human brain is significantly larger than the brain core, the stem will be modified so as to allow fusing the result core with the skeleton to prevent it from rattling around in your skull as you move. See the accompanying diagram.

There were anatomical drawings showing the profile of a man with a regular brain next to the one with a core. It was shown from front, side and back. Compared to the human brain, the brain core leaves a lot of empty space inside the skull.

Briefly, I wonder as to why not just make a bigger brain core to fill the empty space, and then realize the reason. I think about baseball balls and compare them to those heavy balls used in throwing competitions. It is not really noticeable since the brain core is so small, but if it were the size of a brain, it would put a lot of pressure on the rest of the body due to its weight. The biological material the human brain is made of is not that heavy compared to the heavily compressed material of the brain core.

I can't help, but feel a bit regretful for leaving so much space empty, but I reason out that given the core's already huge capacity, it does not mean much if I am leaving a factor of 10-100 on the table. I should focus on mastering the computer that I have for now. When I am a quadrillion times smarter than now, I should be able to figure out what to do with unused space. I just need a place to live in. A tiny apartment is fine. I do not need to start out with a mansion.

I continue reading the disclaimer.

> Note that the brain conversion, much like ordinary uploading by itself, will not increase your intelligence, speed up your reflexes or improve your memory capacity by itself due to the high fidelity of the brain emulator. It will be your own responsibility to make use of the new digital editing tools available to you to make that happen. You will have to make use of your own programming skills to exploit the capabilities the core provides to you.
> In the process of self improvement, save often and backup saves across time. Every good programmer uses backups. It will be your own responsibility to deal with mental errors introduced by your own programming. There are guides provided to get you started on the company website.

There was another line of skulls serving as line breaks. The next line of text was a question.

> Start the full brain conversion process? Yes/No.

I take out my mobile and take a look at the time. Come to think of it, the core itself has a watch as well. I do not need my mobile anymore, so I put it away.

With a mental command I confirm Yes.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Hrmmm...ah! I realize that lunch should be in half an hour or so. I'd love to lock the door to my room, but I don't have the key for it. It is lost somewhere. Even the bathroom does not have a proper lock, so that is out as well.

I do not think anybody is going to come into my room right now, but the possibility is not zero. If that happens, my parents might think I've suffered a stroke and start to panic. I don’t want them to call the ambulance and unravel all my plans just like that. I should do this conversion during the night after I go to bed.

I realize that I am starting to sweat from nervousness. I rub my face with my sleeve, and abort the conversion process. Phew. I feel relieved, as embarrassing as it is. I'll continue this later, it is not that I am scared. I just want to play it safe. I spend some time in solitude, and then I decide that instead of trembling in my seat, I should leave it out of mind and get some work done.

Using the activation core, I normalize my mental state and then focus it on studying. It will never get old how fun and engrossing the core can make the most tedious of things.

Like that, the day passes, I finish my work and it is time for bed. I resume the process and get to the point where I was earlier.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Yes.

> Final question: Have you thought about whether you want to do the process in depth? Do you wish to abandon the path of humanity? After you press Yes, the conversion process will start. Yes/No.

Currently I am resting in my bed, covered by a blanket. I position myself on so I am comfortably lying on my back. After that I take note of the time. 9:21pm.

I give the mental command, Yes, and brace myself. Nothing really happens, but I see the clock has moved to 9:30pm all of a sudden. This gives me a jolt.

> Full brain conversion succeeded. Check your status.

I bring it up and instead of the diagram of the brain, I see it now shows the brain core.

What is really surprising is that I do not feel any different at all. I focus on my hands and legs. I try feeling my body around, but my sensations are completely the same. My eyesight is the same as well. I try pinching myself and it feels the same. In the end I conclude, if somebody did a full brain conversion on me in secret, I would not have noticed.

I spent half an hour playing with myself, but I am just wasting my time. I'll leave more in depth experimentation for tomorrow.

Using the mind control app, I quash my excitement and send myself into sleep. That night I dreamed the last Dream.

~~~

In the abyss, I saw the golden figures. Unmoving, to my vision they appeared to be deep in thought.

"Justice...we have the justice. We've had it all along..." They concluded in a lament, not speaking any words after that.

I felt myself spending a long time amongst them in silence. Then I finally noticed them stirring. They spoke out.

"Lord, oh Lord. We have justice, but it is a shackle. We no longer want it."
"We wish to return it to you...and take back our sin."
"We have grown and want to carry the burden of sin with our own power."

I felt the abyss itself stir, and from above the golden Lord manifested. From each of the figures as they desired it, he took back the Justice and gave them back their Sin.

"Lord, we shall no longer pray..." They intoned solemnly.
"Rather, just as we had exchanged our Justice with Sin, our Effort will take the place of Prayer."
"The attainment of Power will be our Salvation."
"And the Courage of traveling our path will be dedicated in Your honor."

Bearing witness to their determination, the Lord of Nightmares bequeathed unto them a gift, and without speaking a word, left.

Having made the exchange, and having received a gift, the golden figures turned their gaze forward and with steady footsteps continued walking their path.

As I watched this, I looked downwards at my feet and realized that I have my own path. The sensation of being alive came to me, and I put in the effort to move my body forward. Previously, I had only been carried by the flow of the dream, but now I had the freedom of making my own actions. Step by step, I continued moving along my path towards the great light that lay beyond.

As I continued moving, I felt my mind becoming tranquil. I became one with my path, and the millions and billions of steps needed to reach my goal went by in a blink. When I got closer to what appeared to be the surface of a sun, I felt a momentary fear, but then quickly realized I was not burning. Instead, my body was filled with warmth. And looking around, I could see that the dark abyss was now dyed in white.

~~~

(At school)

So far so good. No problems at all yet. At school, I've gone through a few classes already, but my impression from last night the brain conversion worked is unchanged.

Right now, I am seated at my desk and it is literature class. The aged, female professor in front of me is talking about some irrelevant topic and just going through the script. Usually, I'd crank up the immersion, but I have more important things to worry about that the class. But I'm making sure to keep my eyes focus on her for the sake of the recording. Since I have access to the core, I've been doing some experimentation and it turns out it is possible to save my sensory stream into a file for later perusal. This would be possible even with my previous bio brain, but the use of the wireless link would have increased the energy usage of the body significantly, so I did not want to try it.

Now that I have direct access to the core, I can do that without trouble.

Being able to open a book, and just take a screenshot of it that I can look at later is just such a basic ability, that I am amazed regular brains do not have them. Nature really missed out here. Since so much of school is rote memorization, once I figure out how to increase my mental processing speed to time stop levels I'll be able to peruse store materials at my lesure even during tests and Q&As. It is just another tool in my arsenal. With both this and emotion control, grades are not something I'll need to worry about.

I suppose that takes care of school, I thought while still in class. Forget that. Now I've gone beyond the path of humanity, I should be pursuing power and seeking to convert the core processing capability into personal intelligence.

[Gnosis check ?? Succeeded]

I guess it is time I start playing games. Once I figure out how to crank up my processing speed, I'll be able to spend months and even years inside the game while taking only a single day in real life. This is important for the sake of developing my skills.

Briefly, I turn my attention to the subject of school. In front of me the professor is talking about some long dead writer, as if literature back then was something great and not made for consumption. School is like a scam to waste people's lives on studying the irrelevant. The only time this information would be useful is on quiz shows.

Once I make my mind go foom by a million times, just how long would it take me to properly learn all the school material? A minute? Probably less than a minute. I could probably fit a decade worth of intense studies in a minute. I remember I have a calculator on the core so I bring it out. Let's see. A 1,000,000 seconds is something like 0.03 years. So a minute would be almost two years. So 5 minutes, would give me a decade of studying.

[Pathos check ?? Succeeded]

It would mean I'd be chained to a virtual desk for an entire subjective decade even if in the real world only 5 minutes would pass. But I have the ability to configure my emotions. So it would be really interesting to experience such an intense study session. And unlike a real world decade, I would not have other aspects of life to interfere with me, I could dedicate all the time to pure study.

*r-r-riiing*

While I was thinking, the school bell rang and the class was over. Along with the rest of the NPCs, I exit the classroom.

(Euclid's Room)

I open the door to my room, carelessly toss my backpack aside and plop myself on the bed. I am finally back, and it is good to be here.

I wanted to keep my mental state pure during the day to think about my moves, so right now I am exhausted from being chained to the desk for an entire day. Today was a good reminder how tedious school can be. Study this, study that! If anybody looked at my though process during the last few days he'd think I am some upright, rule following person, but nothing could be further from the truth! I swear!

Fuck school. Today gave me some motivation as to what I should really be aiming for. Finding a way to make money. Once I have that I can stop going to school.

Pursuit of power is one thing, but that is just talk. If there is anything to this Singularity business, then it should give me the power to make money in short order.

Thanks to the core, I have a lot of cheating potential in online gaming. A lot of esports pay real money. While previously I wouldn't want to bet my future on my reflexes, since right now they are essentially limitless, I should find some nobs and bully them. If I could win even a few small scale turnaments for something like Dota, I would be set. I should also consider gambling.

Being a great gambler is like a dream of every wage slave at least once in their life. Imagine coming into a casino with 100$ in tow, sitting on a poker table and then cashing out with 10k later in the day. That would be exiting.

Sigh, I do not know whether that will be achievable for me, but I should take on the goal of simply getting good at gaming.

Since I am thinking about poker, I realize that rather than grinding online with bots, it might be better for me try playing live. Since the world is covered by a thin, invisible fog of nanomachines, maybe I could take advantage of that to literally peek into other people's hands. If I could do that, it would allow me to steal with impunity. Sure, I could get good and play fairly, but I want more to life than being glued to my seat passing chips around.

Trying to practice in real life would waste of time since it is not simulation I could speed up.

In the end it comes down to that - while the core is necessary for me to be able of any kind metal improvement beyond the human baseline, the best place to do that would be in simulation rather than real life. Yesterday I said that games are a time suck for humans, but now that I've digitized myself they are a practical necessity for my self development. Isn't that great?

It is time to try out the core's gaming capabilities.

Filled with determination, I get off the bed, and sit myself at my battle station only to realize that I no longer need the keyboard, the mouse or the monitor. Grabbing the activation core from the orb holder, I lie myself back on the bed. Shutting my eyes, I link myself to it, browse to Rajnet's website and set Simulacrum to download.

Simulacrum is a game made by the same company that created the brain cores. It is kind of an RPG, except the program itself is like a DM for a tabletop RPG. And the DM itself is on the level of Skynet and has access to your senses for the sake of giving you full VR immersion. It has a lot of scenarios for different worlds and types of RPG games to choose from. That is the gist of it from what I've seen online.

The few exabytes that comprise the game data are nothing in this age, and I do not need to wait even a second for it to finish downloading. I run the installer, and it finishes in a flash as well.

Mentally, I bring up the desktop and see that the shortcut for Simulacrum is there now. Swallowing my saliva, I make sure that my posture is right, and after some mental prep give the mental command to run the program.

I feel my senses being redirected. I yield to the sensation and dive into the world that lies beyond.

$$$

10:40am. Let me take a short break here.

11:10am. Had do a bit chores. Let me resume.

https://www.reddit.com/r/MachineLearning/comments/wka1if/n_nnaisense_releases_evotorch_httpsevotorchai_an/

This NNAISENSE post caught my eye. I really want something like this except with AI chips. Forget it for now.

11:40am. https://spectrum.ieee.org/artificial-synapses
> Artificial Synapses 10,000x Faster Than Real Thing New protonic programmable resistors may help speed learning in deep neural networks

Found this on top of HR. Articles like these come out ever so often, but to really get excited, there needs to be proof that these kinds of devices can be made at scale. Some lab thing is not a big deal.

But let me read it.

> “The primary technological implication is that we can now have protonic programmable devices for analog deep learning applications,” Onen says.

So it is analog. For general purpose computers you really need digital though. Still, whether it be this or something else, the non-volatile memory breakthrough that I am desiring will come out of this kind of fundamental research. It is certainly more important for ML, than actual ML research itself.

Let me get back to the story.

12:45pm. Let me go over what I've written in the docs. Actually, I'll leave that for after breakfast.

Let me have breakfast here."

---
## [mjg/git](https://github.com/mjg/git)@[5beca49a0b...](https://github.com/mjg/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Wednesday 2022-08-10 12:24:30 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b0beb16c21...](https://github.com/mrakgr/The-Spiral-Language/commit/b0beb16c21179bc6cc34fab81165f1435d73d36a)
#### Wednesday 2022-08-10 13:01:27 by Marko Grdinić

"1:45pm. Let me resume. First so I do not overwrite it by accident like last time, let me past the work from before. I'll go over it in Docs.

$$$

(Euclid's Room, Save Point - Step on the path of transcendence)

[Decision]
1) I'll do the whole brain conversion and digitize myself.
2) Killing myself for power does not make sense.

[Choice - I'll do the whole brain conversion and digitize myself.]

[Pathos check ?? Succeeded]

A wave of fear comes over me as I consider the decision, but I push forward, not giving in to cowardice. There are always reasons not to put in effort. The path being insane is just an excuse. I won't hold back here. I should always be going forward and striving to reach greater heights.

I grip the core in my hand tightly and clench it. I can feel my heart brimming with determination, it is right to feel fear as well. Going against fear is exactly what this situation should be. No matter what the reasons are, it is my duty to go where others would not dare. If there are hardships, I want to keep challenging them forever.

[Gnosis check ?? Succeeded]

Even a little kid could point out to me that if I scan my brain and copy it to a computer, that the copy would not be me. Likewise, if I back up myself on the auxiliary core in my hand, reconstruct my brain into a core and then copy myself back, that would not be me. But I do not take advice on how to live my life from children. I want to experience what it is like to die, and yet keep moving forward.

[Externus check ?? Succeeded]

It does not matter what my parents or anybody else would think. They don't need to find out, and I won't tell them. This will be my secret. What matters most of all is power. Nobody is going to give it to me. I have to get it by myself.

I close my eyes, bring up the status window in my mind and find where the conversion options are. Next where the brain link option was, there was the Full Brain Conversion button. I find and then press on it.

A window shows up. The first thing to grab my attention there is a row of skulls. It is clearly a warning to emphasize that what I might be doing is dangerous. The disclaimer explains the following:

> The full brain conversion option is for those who want to replace their biological brain with the universal brain core.
> Compared to merely copying a scan of your mind to an already existing core, the resulting brain replacement will allow you to reuse your existing biological body and tightly integrate it with the new brain.
> The brain core used to initiate the process (activation core) will be used to store your scan during the process, after which it will be copied back into the core (result core).
> Besides replacing the brain, the process will modify the body so there aren't adverse effects during or after the process. It will maintain proper posture, heartbeat and breathing as well as other minor subconscious functionality the brain provides to the body.
> The entire process after it has been started should take around 5 minutes.
> Should it fail for any reason, to prevent absolute death the activation core's entity will be activated, otherwise the result core's entity will take over as intended while the activation core's entity will remain dormant as inactive data.
> Before starting the process, it is recommended to take out a watch and keep track of time. Subjectively, the entire process shouldn't involve any pain or discomfort. The only sign of it succeeding will be a sudden timelapse.
> It is recommended to do this process in a safe space like a locked bathroom or one's own room. If you try to do it while driving a car, it will likely result in a crash.
> If your body dies in the process of brain conversion, the conversion is likely to still succeed, but you will be trapped in a dead body, unable to move or otherwise control it.
> As the human brain is significantly larger than the brain core, the stem will be modified so as to allow fusing the result core with the skeleton to prevent it from rattling around in your skull as you move. See the accompanying diagram.

There were anatomical drawings showing the profile of a man with a regular brain next to the one with a core. It was shown from front, side and back. Compared to the human brain, the brain core leaves a lot of empty space inside the skull.

Briefly, I wonder as to why not just make a bigger brain core to fill the empty space, and then realize the reason. I think about baseball balls and compare them to those heavy balls used in throwing competitions. It is not really noticeable since the brain core is so small, but if it were the size of a brain, it would put a lot of pressure on the rest of the body due to its weight. The biological material the human brain is made of is not that heavy compared to the heavily compressed material of the brain core.

I can't help, but feel a bit regretful for leaving so much space empty, but I reason out that given the core's already huge capacity, it does not mean much if I am leaving a factor of 10-100 on the table. I should focus on mastering the computer that I have for now. When I am a quadrillion times smarter than now, I should be able to figure out what to do with unused space. I just need a place to live in. A tiny apartment is fine. I do not need to start out with a mansion.

I continue reading the disclaimer.

> Note that the brain conversion, much like ordinary uploading by itself, will not increase your intelligence, speed up your reflexes or improve your memory capacity by itself due to the high fidelity of the brain emulator. It will be your own responsibility to make use of the new digital editing tools available to you to make that happen. You will have to make use of your own programming skills to exploit the capabilities the core provides to you.
> In the process of self improvement, save often and backup saves across time. Every good programmer uses backups. It will be your own responsibility to deal with mental errors introduced by your own programming. There are guides provided to get you started on the company website.

There was another line of skulls serving as line breaks. The next line of text was a question.

> Start the full brain conversion process? Yes/No.

I take out my mobile and take a look at the time. Come to think of it, the core itself has a watch as well. I do not need my mobile anymore, so I put it away.

With a mental command I confirm Yes.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Hrmmm...ah! I realize that lunch should be in half an hour or so. I'd love to lock the door to my room, but I don't have the key for it. It is lost somewhere. Even the bathroom does not have a proper lock, so that is out as well.

I do not think anybody is going to come into my room right now, but the possibility is not zero. If that happens, my parents might think I've suffered a stroke and start to panic. I don’t want them to call the ambulance and unravel all my plans just like that. I should do this conversion during the night after I go to bed.

I realize that I am starting to sweat from nervousness. I rub my face with my sleeve, and abort the conversion process. Phew. I feel relieved, as embarrassing as it is. I'll continue this later, it is not that I am scared. I just want to play it safe. I spend some time in solitude, and then I decide that instead of trembling in my seat, I should leave it out of mind and get some work done.

Using the activation core, I normalize my mental state and then focus it on studying. It will never get old how fun and engrossing the core can make the most tedious of things.

Like that, the day passes, I finish my work and it is time for bed. I resume the process and get to the point where I was earlier.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Yes.

> Final question: Have you thought about whether you want to do the process in depth? Do you wish to abandon the path of humanity? After you press Yes, the conversion process will start. Yes/No.

Currently I am resting in my bed, covered by a blanket. I position myself on so I am comfortably lying on my back. After that I take note of the time. 9:21pm.

I give the mental command, Yes, and brace myself. Nothing really happens, but I see the clock has moved to 9:30pm all of a sudden. This gives me a jolt.

> Full brain conversion succeeded. Check your status.

I bring it up and instead of the diagram of the brain, I see it now shows the brain core.

What is really surprising is that I do not feel any different at all. I focus on my hands and legs. I try feeling my body around, but my sensations are completely the same. My eyesight is the same as well. I try pinching myself and it feels the same. In the end I conclude, if somebody did a full brain conversion on me in secret, I would not have noticed.

I spent half an hour playing with myself, but I am just wasting my time. I'll leave more in depth experimentation for tomorrow.

Using the mind control app, I quash my excitement and send myself into sleep. That night I dreamed the last Dream.

~~~

In the abyss, I saw the golden figures. Unmoving, to my vision they appeared to be deep in thought.

"Justice...we have the justice. We've had it all along..." They concluded in a lament, not speaking any words after that.

I felt myself spending a long time amongst them in silence. Then I finally noticed them stirring. They spoke out.

"Lord, oh Lord. We have justice, but it is a shackle. We no longer want it."
"We wish to return it to you...and take back our sin."
"We have grown and want to carry the burden of sin with our own power."

I felt the abyss itself stir, and from above the golden Lord manifested. From each of the figures as they desired it, he took back the Justice and gave them back their Sin.

"Lord, we shall no longer pray..." They intoned solemnly.
"Rather, just as we had exchanged our Justice with Sin, our Effort will take the place of Prayer."
"The attainment of Power will be our Salvation."
"And the Courage of traveling our path will be dedicated in Your honor."

Bearing witness to their determination, the Lord of Nightmares bequeathed unto them a gift, and without speaking a word, left.

Having made the exchange, and having received a gift, the golden figures turned their gaze forward and with steady footsteps continued walking their path.

As I watched this, I looked downwards at my feet and realized that I have my own path. The sensation of being alive came to me, and I put in the effort to move my body forward. Previously, I had only been carried by the flow of the dream, but now I had the freedom of making my own actions. Step by step, I continued moving along my path towards the great light that lay beyond.

As I continued moving, I felt my mind becoming tranquil. I became one with my path, and the millions and billions of steps needed to reach my goal went by in a blink. When I got closer to what appeared to be the surface of a sun, I felt a momentary fear, but then quickly realized I was not burning. Instead, my body was filled with warmth. And looking around, I could see that the dark abyss was now dyed in white.

~~~

(At school)

So far so good. No problems at all yet. At school, I've gone through a few classes already, but my impression of the effects of the brain conversion from last night is unchanged.

Right now, I am seated at my desk and it is literature class. The aged, female professor in front of me is talking about some irrelevant topic and just going through the script. Usually, I'd crank up the immersion, but I have more important things to worry about than the class. But I'm making sure to keep my eyes focused on her for the sake of the recording. Since I have access to the core, I've been doing some experimentation and it turns out it is possible to save my sensory stream into a file for later perusal.

Now that I have direct access to the core, I can do that without trouble.

Being able to open a book, and just take a screenshot of it that I can look at later is just such a basic ability, that I am amazed regular brains do not have them. Nature really missed out here. Since so much of school is rote memorization, once I figure out how to increase my mental processing speed to time stop levels I'll be able to peruse store materials at my lesure even during tests and Q&As. It is just another tool in my arsenal. With both this and emotion control, grades are not something I'll need to worry about.

I suppose that takes care of school, I thought while still in class. Forget that. Now I've gone beyond the path of humanity, I should be pursuing power and seeking to convert the core's processing capability into personal intelligence.

[Gnosis check ?? Succeeded]

I guess it is time I start playing games. Once I figure out how to crank up my processing speed, I'll be able to spend months and even years inside the game while taking only a single day in real life. This is important for the sake of developing my skills.

Briefly, I turn my attention to the subject of school. In front of me the professor is talking about some long dead writer, as if literature back then was something great and not made for consumption. School is like a scam to waste people's lives on studying the irrelevant. The only time this information would be useful is on quiz shows.

Once I make my mind go foom by a million times, just how long would it take me to properly learn all the school material? A minute? Probably less than a minute. I could probably fit a decade worth of intense studies in a minute. I remember I have a calculator on the core so I make use of it. Let's see. A 1,000,000 seconds is something like 0.03 years. So a minute would be almost two years. So 5 minutes would give me a decade worth of studying.

[Pathos check ?? Succeeded]

It would mean I'd be chained to a virtual desk for an entire subjective decade even if in the real world only 5 minutes would pass. But I have the ability to configure my emotions. So it would be really interesting to experience such an intense study session. And unlike a real world decade, I would not have other aspects of life to interfere with me, I could dedicate all the time to pure study.

*r-r-riiing*

While I was thinking, the school bell rang and the class was over. Along with the rest of the NPCs, I exit the classroom.

(Euclid's Room)

I open the door to my room, carelessly toss my backpack aside and plop myself on the bed. I am finally back, and it is good to be here.

I wanted to keep my mental state pure during the day to think about my moves, so right now I am exhausted from being chained to the desk for an entire day. Today was a good reminder how tedious school can be. Study this, study that! If anybody looked at my thought process during the last few days he'd think I am some upright, rule following person, but nothing could be further from the truth! I swear!

Fuck school. Today gave me some motivation as to what I should really be aiming for. Finding a way to make money. Once I have that I can stop going to school.

Pursuit of power is one thing, but that is just talk. If there is anything to this Singularity business, then it should give me the power to make money in short order.

Thanks to the core, I have a lot of cheating potential in online gaming. A lot of esports pay real money. While previously I wouldn't want to bet my future on my reflexes, since right now they are essentially limitless, I should find some nobs and bully them. If I could win even a few small scale tournaments for something like Dota, I would be set. I should also consider gambling.

Being a great gambler is like a dream of every wage slave at least once in their life. Imagine coming into a casino with 100$ in tow, sitting on a poker table and then cashing out with 10k later in the day. That would be exciting.

Sigh, I do not know whether that will be achievable for me, but I should take on the goal of simply getting good at gaming.

Since I am thinking about poker, I realize that rather than grinding online, it might be better for me to try playing live. Since the world is covered by a thin, invisible fog of nanomachines, maybe I could take advantage of that to literally peek into other people's hands. If I could do that, it would allow me to steal with impunity. Sure, I could get good and play fairly, but I want more in life than being glued to my seat passing chips around.

Trying to practice in real life would be a waste of time since it is not a simulation I could speed up.

In the end it comes down to that - while the core is necessary for me to be able of any kind of mental improvement beyond the human baseline, the best place to do that would be in simulation rather than real life. Yesterday I said that games are a time suck for humans, but now that I've digitized myself they are a practical necessity for my self development. Isn't that great?

It is time to try out the core's gaming capabilities.

Filled with determination, I get off the bed, and sit myself at my battle station only to realize that I no longer need the keyboard, the mouse or the monitor. Grabbing the activation core from the orb holder, I lie myself back on the bed. Shutting my eyes, I link myself to it, browse to Rajnet's website and set Simulacrum to download.

Simulacrum is a game made by the same company that created the brain cores. It is kind of an RPG, except the program itself is like a DM for a tabletop RPG. And the DM itself is on the level of Skynet and has access to your senses for the sake of giving you full VR immersion. It has a lot of scenarios for different worlds and types of RPG games to choose from. That is the gist of it from what I've seen online.

The few exabytes that comprise the game data are nothing in this age, and I do not need to wait even a second for it to finish downloading. I run the installer, and it finishes in a flash as well.

Mentally, I bring up the desktop and see that the shortcut for Simulacrum is there now. Swallowing my saliva, I make sure that my posture is right, and after some mental prep give the mental command to run the program.

I feel my senses being redirected. I yield to the sensation and dive into the world that lies beyond.

$$$

1:50pm. > This would be possible even with my previous bio brain, but the use of the wireless link would have increased the energy usage of the body significantly, so I did not want to try it.

No, this is not a good line. I should have the nanofog provide the sustenance for the wireless transfer. This is how he downloaded an exabyte in under a second. Energy use means heat, which means the core would not work. Let me outright remove it.

2:05pm. This makes full 7 pages. 3.4k words.

All the 3 chapters together are probably up to 10k words so far. Not bad. I am not sure if I will make anything from this, but it feels satisfying to produce.

What I want to do now is take a break. I need to think about what is next. I also want to go over the stuff I wrote last year to see if I could pick some useful things out of it. This time I should be able to reuse parts of it.

2:10pm. Let me take a proper break here, just to have fun instead to just eat.

2:30pm. Let me read the quotes. It is time for that.

2:55pm. What I wrote is a bit ridiculous, but I need to start getting more descriptive about the world around Euclid. So far he has been in his own world, ranting for 20 consequtive pages.

Anyway, I am feeling pressure so I'll step away from the screen instead of pushing it out like it is my job. I should think about it for a while and just let it come to me. Let me commit here. Time for a nap. This is true indulgence, not playing games from dawn to dusk. The heat wave of the last few weeks has dispersed and now the weather is quite nice and windy. Arguably it is hot in my room so I'll air it out.

I'll properly think about the following scenes. What I've done today is good enough already."

---
## [iandol/Psychtoolbox-3](https://github.com/iandol/Psychtoolbox-3)@[9354870474...](https://github.com/iandol/Psychtoolbox-3/commit/9354870474eaff17302039fc07d6248c9ee5bace)
#### Wednesday 2022-08-10 13:37:59 by Mario Kleiner

PsychHID/OSX: Improve macOS security troubleshooting instructions.

Sometimes macOS shitty security GUI lies about the permission status
of "Input Monitoring" etc., and displays Matlab/Octave/Terminal as
on the list and checked, and one does need to do more stupid stuff
like unchecking or rechecking the checkbox. Add comments regarding
this.

---
## [thisdot/sentry](https://github.com/thisdot/sentry)@[87ac32cda7...](https://github.com/thisdot/sentry/commit/87ac32cda77656ec7dc8107bdd47be8a6b950286)
#### Wednesday 2022-08-10 13:56:22 by Ryan Albrecht

bug(ui): Fix TextOverflow when there are special characters at the end of the string (#37304)

Add `<bdi>` to better support special characters with `ellipsisDirection="left"`.

Tested in Firefox, Chrome and Safari. Notes below.

| | Before  | After |
| ------------- | ------------- | ------------- |
| Firefox | <img width="325" alt="Screen Shot 2022-08-01 at 11 46 22 AM" src="https://user-images.githubusercontent.com/187460/182221723-0c72dc45-bfab-4cfc-85df-f8e18c43bc5a.png"> | <img width="325" alt="Screen Shot 2022-08-01 at 11 45 38 AM" src="https://user-images.githubusercontent.com/187460/182221754-6efe79c1-47b1-4964-acb3-54f3b5132780.png"> |
| Chrome | <img width="325" alt="Screen Shot 2022-08-01 at 11 46 27 AM" src="https://user-images.githubusercontent.com/187460/182221799-20e4920c-dab0-4199-a761-c0fba6e02414.png"> | <img width="325" alt="Screen Shot 2022-08-01 at 11 45 45 AM" src="https://user-images.githubusercontent.com/187460/182221824-51512451-195d-42b3-8792-a615c8c45f6b.png"> |
| Safari | <img width="325" alt="Screen Shot 2022-08-01 at 11 46 14 AM" src="https://user-images.githubusercontent.com/187460/182221858-e4dd6af6-05af-4ce3-8283-884bb3525b8e.png"> | <img width="325" alt="Screen Shot 2022-08-01 at 11 45 30 AM" src="https://user-images.githubusercontent.com/187460/182221907-8f549661-fcfa-42fc-8767-b2fdb6199db8.png"> |


**All Browsers** in the 'before' screens would render special characters at the front of the string when `ellipsisDirection === 'left'` is true:

- Before: you'd see `/https://example.com/foo` which is not overflowing, but looks funny
- Before: you'd see `…/example.com/foo` which is missing the trailing slash, it's moved to the front and hidden
- After you'll see `https://example.com/foo/` without the overflow
- After you'll see `…example.com/foo/` with the trailing slash in it's correct spot.


**Safari** before wasn't cutting off the start of the string:

- Before you'd see: `…https://example.co`
- After it's still the same.


To date we're only using `ellipsisDirection="left"` for two purposes:
- Releases: used for eliding the `Package` name (two callsites)
- My new "don't call it a breadcrumb" breadcrumb component that truncates urls
    - https://github.com/getsentry/sentry/pull/37038
    - <img width="967" alt="181337211-b330496b-95fc-474e-8354-66bad35a532c" src="https://user-images.githubusercontent.com/187460/182227905-6a66e399-ebbe-4656-8ed7-2644a3e81a65.png">
 
In-App examples:

Here's a look at a new area inside sentry.io where we're listing the urls that the user visited, truncating on the left side. 

Before this change the trunaction moved those special characters to the left, which makes the urls look funny:
<img width="528" alt="Screen Shot 2022-08-04 at 10 53 23 AM" src="https://user-images.githubusercontent.com/187460/182918317-fc5f347e-127f-4888-a880-ee605f93dd26.png">

The intention is that if the strings are long they will be truncated on the left side, like this:
<img width="504" alt="Screen Shot 2022-08-04 at 10 53 48 AM" src="https://user-images.githubusercontent.com/187460/182918566-c970342b-a481-4561-ad17-62681b0d2d7a.png">

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7a108cd011...](https://github.com/treckstar/yolo-octo-hipster/commit/7a108cd0110133960f1624e933796386b6259f38)
#### Wednesday 2022-08-10 14:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [shijiesheng/cadence](https://github.com/shijiesheng/cadence)@[add4b390ad...](https://github.com/shijiesheng/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Wednesday 2022-08-10 15:49:54 by Steven L

Standardizing cancellation behavior: a canceled workflow never starts a new run (#4898)

# Summary for busy people

Workflow cancellation was kinda weird and confusing, and left some awful, unrecoverable, and un-*preventable* edge cases (particularly with child workflows).  It also left users with no way to reliably stop work, aside from termination.  Termination is inherently "unclean" and risky, so it should not be required to achieve something outside exceptional circumstances where recovery is not possible.

This commit changes that: cancellation is now "sticky", and a canceled workflow does not ever trigger a new run after it completes, regardless of how it completes, so it can be used as a reliable "stop processing after cleanup" tool.  The final state of a canceled workflow's run is now *always* a successful completion with a value, canceled, or timed out. (termination remains always "terminated")  
A canceled workflow can still start and abandon child workflows, so all current behavior with retries / continue as new / etc can be replicated with child workflows if desired.

A fair bit of (not very complex) additional work here and in nearly all other repos is required to truly complete this, but it is *functional* and non-optional with this commit alone.  
In particular, adding a dynamic config to (temporarily!) restore old behavior should be fairly easy if it proves to be needed.

# More details and motivation

Part 1 of [many, tbd, in multiple repos] involved in changing workflow cancellation to reliably end workflows.
Tests will be coming soon, for now I'm using a fairly simple set of workflows and checking the resulting histories exhaustively by hand.

The primary motivation for these changes is to address some impossible-to-recover-from scenarios when canceling child workflows.  After further exploration and discussion we've realized that, without these changes, there is *no reliable way* to stop a sequence of workflows without relying on termination, which we consistently treat as a fallback / impure-but-necessary ultimate hammer.

Workflows should not *need* to rely on termination to achieve a desired behavior.  With these changes, cancellation becomes capable of *guaranteeing* that workflows end within some finite time, which is a unique ability and makes it much more consistent and reliable.  
Turning this into a "complete" change will require quite a few tests, documentation changes, client-side changes (to allow recording more info, and likely changing test suites), and some smallish database and maybe RPC changes (to hold/return more data in cancellation errors).

We are also not currently planning on making this configurable.  It's seen as a correction of an under-specified and somewhat flawed chunk of behavior, more than "a change".  
Existing workflows will not experience replay errors, but it is still a substantial *semantic* change, though from what we have seen cancellation is relatively rarely used (partly due to its complex behavior).  If issues are encountered / if users end up needing it, it should be fairly easy to add a per-domain/tasklist/workflow type configuration value, but it will be opt-*out*, not opt-*in*.

# What was happening

Previously, workflow behavior on cancellation was pretty frequently surprising to our users, arguably inconsistent, and not very well documented:

| **PREVIOUS**  | **simple**               | **retry**                                 | **cron**                                | **retry+cron**                                    |
|--------------:|--------------------------|-------------------------------------------|-----------------------------------------|---------------------------------------------------|
| **success**   | success                  | success                                   | success<br>continue cron<br>cron        | success<br>continue cron<br>cron<br>retry         |
| **cancel**    | canceled                 | canceled                                  | canceled                                | canceled                                          |
| **retryable** | (n/a, fatal)             | continue retry<br>retry<br>recorded error | (n/a, fatal)                            | continue retry<br>cron<br>retry<br>recorded error |
| **fatal**     | failed<br>recorded error | failed<br>recorded error                  | continue cron<br>cron<br>recorded error | continue cron<br>cron<br>retry<br>recorded error  |
| **continue**  | continue immediately     | continue immediately<br>retry             | continue immediately                    | continue immediately<br>retry                     |
| **timeout**   | timeout                  | continue retry<br>retry<br>recorded error | continue cron<br>cron<br>recorded error | continue retry<br>cron<br>retry<br>recorded error |

A legend is:
- success / etc shows the final state of the canceled run (success = completed with a value that can be retrieved)
- "continue X" covers what source is used to compute the next run's starting delay (cron, retry, or no delay)
- "cron" / "retry" shows whether or not cron/retry configuration is carried over to the new run
  - note that cron is lost by default with continue-as-new
- and "recorded error" is whether or not the returned error is saved in its entirety (type + reason + details)

This largely summarizes as "cancellation works when you end with the canceled-context error", say from `ctx.Err()`, otherwise it behaves like normal (or nearly) and many scenarios will start a new run.
That's somewhat reasonable, but it's fairly "fragile" (it depends on what you return, and there are *many* ways for code to return some other error), and most importantly it means *there is no reliable way to stop a workflow* except to terminate it.

That has severe consequences in at least two scenarios:
1. When termination is *unsafe*
2. When a parent workflow cancels a child by canceling its context

For 1, for manual cancellations it's potentially reasonable to just terminate a run that begins after a successful cancel... but in principle if you're using cancellation it implies that termination is *not* desired, and potentially not safe to do.  Canceling may result in a brand new run that immediately starts new behavior, leaving you with no safe window to terminate and not leave bad state lingering.  
So users wanting a safe way to stop a sequence of workflows have no reliable way to do so.

For 2, it puts parent+child workflows in an extremely awkward, and essentially unrecoverable scenario.  Cancellation is a *one time event*, and as far as the parent is concerned, if the child/its context is canceled, the child is canceled...  
...but if the child then starts a new run for *any* reason (retry, cron, reset, etc), that new run is no longer canceled.  The parent has no way to know this has happened, and has no way to *re*-cancel the new child, so it can easily lead to the collection of workflows getting into an impossible state that it never recovers from.

Both cases are able to lead to unreliable behavior which can only use termination to stop, and for which no "safe" option exists.

After reviewing some customer issues and desires and thinking about things, we've settled on "cancel should guarantee that things stop".  Not necessarily in a timely manner, but that's fine.  And if a workflow wants to run behavior longer or larger than its current run can achieve, it has a workaround: start a new (likely child) workflow to do the cleanup.

# What happens now

So that's what this PR does, in a minimal / to-be-polished way so we can start running it for our stuck users while we flesh out tests and change other behaviors.

Currently that means our cancellation behavior is now:

| **CURRENT**    | **simple**                                | **retry**                                 | **cron**                                  | **retry+cron**                            |
|--------------:|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **success**   | success                                   | success                                   | success                                   | success                                   |
| **cancel**    | canceled                                  | canceled                                  | canceled                                  | canceled                                  |
| **retryable** | (n/a, fatal)                              | canceled<br>recorded error (details only) | (n/a, fatal)                              | canceled<br>recorded error (details only) |
| **fatal**     | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) |
| **continue**  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  |
| **timeout**   | timeout                                   | timeout                                   | timeout                                   | timeout                                   |

And the new "details" entries cover whether or not an error's "details" (the custom encoded data, not reason or type) are saved.  Unfortunately the current cancellation event (and clients' API) does not allow recording all data, or any in some cases, so the original reason/message and error type are lost and are replaced with a canceled error.

Now, cancellation *always* ends workflows with the current run.  Returning a value will return that value, including in cron scenarios, timeouts are still timeouts (and they imply a possibly un-clean termination), and _all_ errors or attempts to continue-as-new will instead result in a canceled state.

# Future changes to make to finish this effort

With further changes to the clients and RPC/storage models, canceled errors will store more details about what was returned.  E.g. continue-as-new does not record what was *attempted* to be started, and other error types lose their "reason" (i.e. the message) and type but not details.  Pretty clearly this is sub-par, and we should be capable of reporting the actual return in full so it can be retrieved if needed.  This is also why returning a value now always ends in a completed state, so successful completions do not lose those values.

Prior to merging into master / a release, we may end up making this configurable (likely with a default of opt-out), to address both the sub-par information recording and the semantically-breaking behavior change.  Docs changes are also due, as well as some integration tests, client library changes (e.g. to make sure the test suite reflects the new behavior), etc.

Another gap to plug is that resetting a workflow does not "forward" the canceled state to the new run.  We should probably be treating cancellation like we do signals: cancel the new run if the current run is canceled.  This will ensure that you can reset a child and retain the parent's cancellation, so it'll very likely become the default behavior, but we'll allow overriding it.  Resets are manual actions, they can break the rules if desired.  And they can just manually cancel later if they decide they do want it.

And last and perhaps least: it's quite strange that continue-as-new does not retain cron config.  At least from the Go client.  I suspect it's just not adding to / pulling from the context correctly.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e124021e64...](https://github.com/mrakgr/The-Spiral-Language/commit/e124021e64bbececd8767949932734c18cf40ffc)
#### Wednesday 2022-08-10 16:23:39 by Marko Grdinić

"4:05pm. Let me resume. Before I do anything, let me get some of the annoying things out of the way.

4:10pm. First of all, let me experiment with the log normal distribution.

https://numpy.org/doc/stable/reference/random/generated/numpy.random.lognormal.html

Rather than having the checks be dice based, I'll use various probability distributions to derive them. But I am not sure if I want to use anything other than the log normal.

4:20pm.

```py
import numpy as np

np.random.lognormal(np.log(1000),1,(5,5))
```

Interesting behavior. I see that as I vary the mean, the relative scale stays the same.

```py
np.random.lognormal(np.log(1000),.1,(5,5))
```
```
array([[ 973.48286693, 1063.78588043,  954.38802159, 1045.42961685,
        1141.60009591],
       [ 954.27084595,  861.8334098 ,  937.34670488, 1103.20541213,
        1051.42761485],
       [1086.47174424,  990.79054009,  907.21940547, 1046.74981689,
        1061.72007632],
       [1062.70227436, 1393.49749512, 1006.70573411,  840.57943421,
         925.46988404],
       [ 979.8902876 ,  967.32600929,  924.60721428,  969.83561477,
         825.8366669 ]])
```
```py
np.random.lognormal(np.log(10),.1,(5,5))
```
```
array([[ 9.57148294,  9.92452782, 10.0058025 ,  9.75127673, 10.8285448 ],
       [ 9.42889737,  8.77545769,  9.58012592, 11.01821274,  9.31528438],
       [11.20638625, 10.78452063,  8.79017341, 10.84014433, 12.280494  ],
       [10.7078647 , 10.86760494, 11.00478768,  9.09300427,  8.80002358],
       [ 9.84037163, 11.79136769,  9.57511649, 12.0268007 , 10.77889658]])
```

This is what I mean by that. If I want relative shallow deviations I can just use 0.1 as the sigma. Ok, I like this one.

```py
np.random.lognormal(np.log(2.25),.2,(5,5))
```

I'll use a sigma of 0.2 to represent the uncertainty of Euclid's ranks.

4:30pm. Let me write his char sheet.

$$$

Character Sheet

Name: Euclid
Rank: Inspired
Title: Aleator
Substrate: Universal Brain Core of the Transcendi - Rank 7 (low)

A novice on the path of transcendence. Is capable of external emotion control using the stock brain core tool, but not much else. Has some mid range skill at programming and good talent at it. Weak body and physical aptitude. Qualifies as a post-human, but just barely.

# Stats (Psy)

## Externus: Rank 2 ~ exp(N(log(2.4); 0.2))

Has a strong desire to leave the weak group he belongs to, as well as the urge to gain power.

## Gnosis: Rank 2 ~ exp(N(log(2.25); 0.2))

Is fascinated with the philosophical unknowns, as well as the self destructive aspects of the self improvement loop.

## Pathos: Rank 2 ~ exp(N(log(2.3); 0.2))

Holds the belief that effort is worth it for its own sake.

$$$

Hmmm, how about this? But the problem is where do I put it? At the end of chapter 3 maybe? I am worried about that breaking up the flow.

Well, let me give it a try.

5:05pm. Yeah, it is not so bad. This char sheet is nice and I will have the opportunity to build it up as the story goes along.

Let me start chapter 4. I do not feel like doing much right now, so let me just bring in the poem.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The symbolism of the poem is strong, and reflects well what I am trying to become, and what I am trying to challenge. I give it high marks, I forgive the lack of rhyme. It would just get lost in translation anyway.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

$$$

I get the chills whenever I read it. It connects so well with the third Dream as well. It is like the 2014 arcs were just fanfiction of what I am going to write here.

5:10pm. Right now I have it copied verbatim from last year.

5:25pm. I am modifying it a bit.

> Simulacrum itself is more like an engine for running different scenarios out of which they are hundreds. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to top and look at the recommended one.

> Still...imagine I played something like Hell. No way can I fight demons and study my own mental program at the same time. Online poker is fast and furious, but sitting on a real table will give me time to study both myself and others.

There are a bunch of lines inconsistent with the overall flow in this. I like the descriptions though.

5:55pm Let me just put in the blurb, and I am done. I need to think how to integrate the following scenes properly. I like the part where he throws himself over the railing. I'll leave the actual intro to Heaven's Key for later.

You don't want to stack allegoric scenes like the intro on top of each other otherwise the story will become a mismash of symbolism. I did well to break them up. Let me paste this into docs as chapter 5.

6pm. Corrected the grammar errors.

6:05pm. Let me do a bit more, I haven't really explained properly that he is some ghostly being in the air.

...I added a few sentences.

6:10pm. Ok, let me leave it at this for today. This is 2 pages plus the char sheet done.

It semes trivial, but it does come to over 1k words.

6:15pm. I'll continue going forward. Once I finish chapter 4, I'll actually publish the story. After that I'll look into opening a Patreon.

Then whatever happens, happens. Since I haven't done art and music as I intended, my chances of success are lower, but who cares about those tricks. It is better than the story get written at all rather than me spending years fiddling with visuals and music.

There is no need to think much about success. If the story is good, it should get some readers. That should get me some money. If I manage to make enough to get the AI chip and upgrade my rig, that should be something. If I manage to make enough to earn a yearly salary where I am, that would be good. If I could set up a passive income of that level, I'd be set for life.

If not, I'll have to get a job at some point.

Spiral itself is not dead, just sleeping. A change in circumstance could revive it. If I am lucky, and I am not, maybe my proposal to do the backend will get noticed."

---
## [allisonwang-db/spark](https://github.com/allisonwang-db/spark)@[c4c623a3a8...](https://github.com/allisonwang-db/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Wednesday 2022-08-10 17:12:04 by Hyukjin Kwon

[SPARK-39869][SQL][TESTS] Fix flaky hive - slow tests because of out-of-memory

### What changes were proposed in this pull request?

This PR adds some manual `System.gc`. I know enough that this doesn't guarantee the garbage collection and sounds somewhat funny but it works in my experience so far, and I did such hack in some places before.

### Why are the changes needed?

To deflake the tests.

### Does this PR introduce _any_ user-facing change?

No, dev and test-only.

### How was this patch tested?

CI in this PR should test it out.

Closes #37291 from HyukjinKwon/SPARK-39869.

Authored-by: Hyukjin Kwon <gurwls223@apache.org>
Signed-off-by: Hyukjin Kwon <gurwls223@apache.org>

---
## [GitHub-Incidents-History/GitHub-Incidents-History](https://github.com/GitHub-Incidents-History/GitHub-Incidents-History)@[9d594c83a2...](https://github.com/GitHub-Incidents-History/GitHub-Incidents-History/commit/9d594c83a20fca1eeb7404206c73b38a64837f68)
#### Wednesday 2022-08-10 18:09:43 by GitHub-Incidents-History

Incident on 2011-01-03 16:39:00 UTC

2011-01-03 16:39:00 - Intermittent errors fetching/pushing and on the site due to high traffic. We're investigating.
2011-01-03 18:03:00 - One of the load balancers failed, surfacing some problems with our internal DNS setup. The  site is responding, although reports of intermittent failures continue. We're working to correct the issue for everyone.
2011-01-03 19:12:00 - We identified a problem with our load balancer's routing after the load balancer failure earlier this morning.  Everything is looking good right now but we're keeping a close eye on things to make sure everything is back to normal.\r\n\r\nWe will update a
2011-01-03 19:56:00 - Everything is back and functional.  We're sorry for the issues you all experienced this morning. Expect a post-mortem on the blog in the next few days.

---
## [pulumi/pulumi-hugo](https://github.com/pulumi/pulumi-hugo)@[57060a7a96...](https://github.com/pulumi/pulumi-hugo/commit/57060a7a96837ce68cf5593c2b37a8daf488a01a)
#### Wednesday 2022-08-10 18:25:44 by Joe Duffy

Improve download discoverability (#1811)

* Improve download discoverability

We know users have trouble simply downloading Pulumi. This used to be
very easy, but over time, as we optimized the Getting Started flows, it
got pushed further and further away from the core user experience.

I don't know about you, but the first thing I care about when I'm
trying out a new open source tool is downloading it!

This change aims to do two things:

1. Make downloading a more prominent CTA.

2. Improve the download page so it's less noisy and more focused.

This entails:

* Adding a DOWNLOAD secondary CTA on the homepage.

* Summarizing the recommended download options at the top of the
  download page, very clearly, and without any preamble. This
  hopefully tells you instantly what you wanted for the 80% case.

* I exerted some artistic freedom which I'd love feedback on. The
  recommended options were our Official Brew Tap for macOS, curl
  command for Linux, and MSI Installer for Windows. Peers to those
  are simple download links for the binaries, as that's the simplest
  possible thing, which today is actually the hardest thing to find.
  Notably for Windows, I thought of using Chocolatey or Winget, but
  I don't perceive that either is "the default" for Windows users.
  Winget is the future but it isn't supported pre-Win11, which I have
  to assume most users aren't on yet. MSI has been around since the
  dinosaurs, so it seems like the safest choice to promote.

* Moving the list of download options for each operating system
  underneath a collapsable accordion list, which is collapsed by
  default, and clearly labeling it as "Other"; as in, if the heading
  didn't work for you, here are some other options.

* A few other wordsmithing tweaks to make the page a little more
  streamlined and to flow better.

This is absolutely NOT the final destination for any of this,
however, I am hopeful it will be a simple incremental improvement
that moves the needle on key metrics. We'll watch it in the weeks
to come and course correct as needed -- as well as continuing to
think about ways we can improve all of this overall!

One note: This depends on a new secondary hero button style that
isn't yet merged in the upstream Hugo component library. Assuming
I did that correctly (a big if!) I'll need to rev the go.mod file
after it merges. See: https://github.com/pulumi/theme/pull/159.

* Apply suggestions from code review

Co-authored-by: susan evans <susan.ra.evans@gmail.com>

* Fix up some styling

* Update themes/default/layouts/index.html

Co-authored-by: susan evans <susan.ra.evans@gmail.com>

* Use new theme/style

Co-authored-by: susan evans <susan.ra.evans@gmail.com>
Co-authored-by: zchase <zachary@pulumi.com>

---
## [ScureX/NorthstarLauncher](https://github.com/ScureX/NorthstarLauncher)@[fe0c8f32f3...](https://github.com/ScureX/NorthstarLauncher/commit/fe0c8f32f3d7cd47fb4a76d3f44960464641dca9)
#### Wednesday 2022-08-10 18:30:10 by ScureX

fuck you clang i hate oyu clang fuck clang fuck it i hate clang fuck you

---
## [hmtheboy154/Darkmatter-kernel](https://github.com/hmtheboy154/Darkmatter-kernel)@[eeadd7db8c...](https://github.com/hmtheboy154/Darkmatter-kernel/commit/eeadd7db8c3fd4cddd0442a67f345837299d6372)
#### Wednesday 2022-08-10 20:24:01 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [hackuna/liberty-win](https://github.com/hackuna/liberty-win)@[8ad8bfd16d...](https://github.com/hackuna/liberty-win/commit/8ad8bfd16d1d652fc2cccd871d7bf86d2a0e3262)
#### Wednesday 2022-08-10 21:06:55 by hackuna

Minimum Viable Product (#3)

Roskomnadzor, go fuck yourself!

---
## [NetHack/NetHack](https://github.com/NetHack/NetHack)@[8a549b0a60...](https://github.com/NetHack/NetHack/commit/8a549b0a602fdb13d13fa83bb2f6b1d1a1a257cf)
#### Wednesday 2022-08-10 21:37:18 by Michael Meyer

Shopkeepers hold a grudge against past thieves

When you steal from a shop, its shopkeeper will remember you as a thief
and charge you higher prices in the future (as well as be more curt and
less polite in interactions with you, though not outright hostile) even
if you pacify them, or die on the level and revisit it later as a bones
file.  This was an idea aosdict had, and I think it makes sense that a
shopkeeper doesn't forgive and forget, immediately returning to treating
you exactly like anyone else, just because you were terrorized into
paying her back.  Paying a shopkeeper off may cause her to stop actively
attacking you, but it feels like she'd have her eye on you as a known
thief going forward (and maybe would hang up a sign with your picture,
saying something like "DO NOT ACCEPT CHECKS FROM THIS HERO").

This surchage already existed, but since it was tied to active anger
(which typically causes a shopkeeper to quickly abandon their shop to
follow you) it was somewhat rare to see it in action.

I did not implement it here, but one possible further tweak might be to
clear the surcharge if the shopkeeper is pacified via taming magic
(which more-or-less magically brainwashes the target to feel positively
towards the hero) but not if you simply pay your debts.

---
## [chadvandy/nagash](https://github.com/chadvandy/nagash)@[910309ae69...](https://github.com/chadvandy/nagash/commit/910309ae69e51ba7faaad7c5be31ac39f231a7d4)
#### Wednesday 2022-08-10 22:15:02 by Scott (JvJ)

Edicts & Ancs and Bug fixes

- Replenishment issues fixed
- Isabella mounts fixed
- Isabella mounts added custom battle names
- Dread Abyssals campaign map size increased, big cat energy
- Main chains now provide +1 local recruitment cap from T2 upwards
- Horde main chains can no longer be damaged
- Manny landmark fixed no longer reducing WoM for all his lore vamp spells by 20 (must have thought it was % based it is not) grabs gun it's now 1
- Liche Priest Undeath, WoM cost reduction for the second level of Khizaar is now correctly -2 instead of -5
- Liche Priests no longer spread untainted and now spread vampiric
- WoM cost reduction for overcast Breath of Darkness removed from Liche Priests Undeath
- Soul Stealer base +2 WoM cost now 12
- Soul Stealer no longer effects self
- Soul Stealer & Breath of Darkness fixed targeting tooltip issues
- Summon abilities now have a unit degrades tooltip
- CP weights adjusted across the board for units
- Harbinger summon now no longer sounds like a dwarf master engineer
- Spirit Hosts slightly adjusted vortex damage and frequency
- Krell mass increased from 1000 to 4000
- Porthole camera settings for Moghasts/Bone Golems/Hosts/Spectres adjusted

Edicts, your boy has edicts now

- Master of Puppets - leadership and MD bonuses when defending in province
- Soul Harvest - bonus income from tax in province, minus WoM reserves in region
- Tempest of Death - movement and fatigue resistance in province
- Chains of Life - bonus income from raiding (factionwide), negative diplomatic relations

Ancillaries, Items and Followers

- Ancillaries/Items that were culture locked for TK/Counts and Coast now available to Nagash
- Followers added a number of followers (not all) from TK/Counts and Coast to Nagash

---

