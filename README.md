## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-07](docs/good-messages/2023/2023-08-07.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,274,107 were push events containing 3,386,506 commit messages that amount to 262,091,942 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 50 messages:


## [kernelci/linux](https://github.com/kernelci/linux)@[0a2c2baafa...](https://github.com/kernelci/linux/commit/0a2c2baafa312ac4cec4f0bababedab3f971f224)
#### Monday 2023-08-07 00:02:47 by Linus Torvalds

proc: fix missing conversion to 'iterate_shared'

I'm looking at the directory handling due to the discussion about f_pos
locking (see commit 797964253d35: "file: reinstate f_pos locking
optimization for regular files"), and wanting to clean that up.

And one source of ugliness is how we were supposed to move filesystems
over to the '->iterate_shared()' function that only takes the inode lock
for reading many many years ago, but several filesystems still use the
bad old '->iterate()' that takes the inode lock for exclusive access.

See commit 6192269444eb ("introduce a parallel variant of ->iterate()")
that also added some documentation stating

      Old method is only used if the new one is absent; eventually it will
      be removed.  Switch while you still can; the old one won't stay.

and that was back in April 2016.  Here we are, many years later, and the
old version is still clearly sadly alive and well.

Now, some of those old style iterators are probably just because the
filesystem may end up having per-inode mutable data that it uses for
iterating a directory, but at least one case is just a mistake.

Al switched over most filesystems to use '->iterate_shared()' back when
it was introduced.  In particular, the /proc filesystem was converted as
one of the first ones in commit f50752eaa0b0 ("switch all procfs
directories ->iterate_shared()").

But then later one new user of '->iterate()' was then re-introduced by
commit 6d9c939dbe4d ("procfs: add smack subdir to attrs").

And that's clearly not what we wanted, since that new case just uses the
same 'proc_pident_readdir()' and 'proc_pident_lookup()' helper functions
that other /proc pident directories use, and they are most definitely
safe to use with the inode lock held shared.

So just fix it.

This still leaves a fair number of oddball filesystems using the
old-style directory iterator (ceph, coda, exfat, jfs, ntfs, ocfs2,
overlayfs, and vboxsf), but at least we don't have any remaining in the
core filesystems.

I'm going to add a wrapper function that just drops the read-lock and
takes it as a write lock, so that we can clean up the core vfs layer and
make all the ugly 'this filesystem needs exclusive inode locking' be
just filesystem-internal warts.

I just didn't want to make that conversion when we still had a core user
left.

Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Christian Brauner <brauner@kernel.org>

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[8f1ceefd2b...](https://github.com/Offroaders123/NBTify/commit/8f1ceefd2b88505c86c52b5f03d7349806da214f)
#### Monday 2023-08-07 01:25:53 by Offroaders123

No Never

Wow. Wow wow wow! Went down the rabbit hole with discussions in the MM discord, it was great! Thanks @HoldYourWaffle!

I was gonna include more of our conversations, but there were so many I don't know if it would make sense here haha. Super productive, really fun.

I tried asserting the return type to reflect whether the input generic is valid/unset or not, but it's not reliable to work with, because it widens the types too much.

Essentially:
```ts
type SafeNever<T> = [T] extends [never] ? unknown : T;

export declare function parse<T extends RootTag = never>(data: string): SafeNever<T>;
```

But this doesn't work well/breaks when working with `NBTData`, which doesn't allow `unknown` as an input generic type (which is correct).

```ts
// @ts-expect-error
export declare function read<T extends RootTag = never>(data: Uint8Array): Promise<NBTData<<SafeNever>>>;
```

So, the next step was to try the other option available, move the generic type check out of the generic and into the return type. But this isn't realistic/reliable, and also hard to work with like this first one.

```ts
export declare function parse<T>(data: string): T extends RootTag ? T : unknown;
```

This worked semi-nicely with incorrect values, because if they weren't `RootTag`-compatible, the return value would always be `unknown`. Perfect! But a great point that HoldYourWaffle pointed out was that it doesn't correctly represent the control flow of the function path, because `unknown` is not the same as `never` (not talking types, but actions.)

```ts
const gg: unknown = parse<5>("5");
```

While the type is 'correct' because it isn't a shape, it's not really correct because it should show an error here, mirroring what it would do in run time. Because '5' isn't a valid SNBT string, it would 'never' complete, meaning that `unknown` isn't correct because that means it did run as expected, you just don't know the value.

So that's not ideal, and not accurate. It also didn't help that the same `NBTData`-and-the-like parameter type issues were happening here, because the return type has a possible `unknown` in it, which isn't accepted by the other parameters for the API (again, which is correct).

So then we came back to the setup to how this commit looks right now, where the generics don't have default values. This means that if unsupplied, the return types for the functions are `RootTag`, which didn't *seem* too bad. But `CompoundTag` is build with an index-signature, and it's paired with `ListTag`, which is built from the `Array<Tag>` type. Sounds good and dandy, but turns out that an index-signature can validate alongside that one in a union type, meaning that a plain `RootTag` declaration allows you to (type-wise) access methods and values on the value which might not exist! What the heck!

```ts
// hallucinate.ts

export type RootTag = CompoundTag | ListTag<Tag>;

export type Tag = string | number | boolean | ListTag<Tag> | CompoundTag;

export interface ListTag<T extends Tag> extends Array<T> {}

export interface CompoundTag {
  // Try commenting out this index signature line
  [name: string]: Tag;
}

declare const gg: RootTag;

gg.concat;
gg.length;

// @ts-expect-error
gg.concat();
```

So you can see the methods aren't callable, but it does let you access properties that don't exist. This is the case even with `noPropertyAccessFromIndexSignature` and `noUncheckedIndexAccess` (I think that one has more to do with arrays, but yeah).

So the realisticness I decided out of the different options are that there are a few different ways to take this decision:
(I think I mentioned it in #32, but yeah)

If the generic was optional, the catch for the implicit nature of the generic is when you use it, it will be `unknown`
But making the generic non-optional means you have to decide ahead of time whether it's strongly-typed, or turtle-brained as `any`
So it moves the first step to the beginning, when the variable is defined, not when it's accessed
So it removes `unknown` from it altogether
Optional Generic state: either `unknown`, `interface ThisIsMyShape`, or `any`
Non-Optional Generic state: `ERROR: ts(missing generic parameter)`, `interface ThisIsMyShape`, or `any`

Now that we know that `unknown` and `never` aren't possible/not feasable/realistic, the three options are either: `interface ThisIsMyShape`, or defaulting back to `any`. If function generics could be made mantatory, then I could essentially enable the 'unknown' state, where it would show as a missing generic when used without a supplied generic, like `NBTData` does, because classes *can* have required generics.

```ts
// @ts-i-want-this-to-error - If you could make this generic mandatory, the return type could be `unknown` if you didn't supply a generic value, rather than being `RootTag`, which is an option we've narrowed out.
export declare function parse<T extends RootTag>(data: string): T;
```

So, if:
- `never` can't be returned, nor used reliably
- `unknown` can't be returned, nor used reliably
- The return type can't be narrowed, nor used reliably
- `RootTag` can't be checked outside of the generic/used reliably

That leaves it back to either defaulting the generic to `RootTag`, or `any`. And for me, I think making it consistent is the most important part. `RootTag` can make up values altogether, which could be misleading. But if you plain just see an `any` there, you know for a fact that anything goes, so you *know* it will hallucinate values, because that's what it does. It doesn't mislead you to values that are/might not be there.

So while `any` is unsafe because it allows you to traverse it as anything, I think that's better than traversing it as what you *think* it is. That's not the purpose of typing it out; If you want to type it out just for the sake of making it not `any`, that seems more dangerous to me, because that's saying that you know that `RootTag` is. But `any` just plain says, "hey, all rules are gone here, beware".

`unknown` would be the best scenario here for the return type, because it would warn you if you are trying to use the return type as if it were `any` implicitly. It would be the best to have the user specify that they intend to use `any` on purpose.

Wow, learned a lot from this! Thanks again to @HoldYourWaffle for helping discern all of this in the last day or so. Can't believe how much our group of 'turtle-brains' over at Minecraft Manipulator are good at getting stuff done. We might be slow, and or quiet sometimes at things, but when we get movin', oh man!

https://stackoverflow.com/questions/71193522/typescript-inferred-never-is-not-never
https://github.com/microsoft/TypeScript/issues/23182#issuecomment-379091887
https://www.typescriptlang.org/play#example/unknown-and-never
https://stackoverflow.com/questions/55610260/how-to-make-generics-mandatory
https://stackoverflow.com/questions/69763621/check-if-object-is-empty-using-typescript-generic

https://www.youtube.com/watch?v=J1f5b4vcxCQ

The next thing we started talking about after this commit-and-related-to-it, was whether NBT data should be represented using primitives, or wrapper objects with methods and such. I think it boiled down to that I like primitives for declaring new data structures, but primitive wrappers are probably the better choice for working with the data itself. Think of things like `Array.prototype.push()`. You wouldn't call it as a standalone function, or as a static method, it doesn't really make sense to do it that way.

```ts
const thingo: number[] = [];
thingo.push(5);

Array.push(thingo,5);

pushArray(thingo,5);
```

HoldYourWaffle:
> Yes, composing NBT from scratch is much nicer with the primitive variant, no argument there.
> The thing is: you're not doing that regularly, at least not as much as manipulating the data, especially for a project called Minecraft *Manipulator* :)
>
> Secondly: the manipulation part of any program is much more intricate, bug-prone and maintenance-heavy than composing some static-ish data. When debugging shenanigans or implementing new features I need to be able to read, interpret, understand and write manipulation code quickly
> Finally: while the "primitive composing" is certainly nicer, the alternative is not that bad. The "convenience method manipulation" variant has a lot of advantages compared to the "functional" alternative though.

Me:
> That's a great argument, and I think I have to convince myself now that it makes more sense

HoldYourWaffle:
> 🔥

I think it's a great argument, I think my holdup is to whether NBT is something that needs an 'abstract' representation. I have felt like that using methods around the primitives allows for more composability, and you can build things together better using plain functions to manipulate the structures, rather than instance methods on the data abstractions themselves.

Me:
> I was gonna say, I want to look into classes for these again, if we do it right
> Cause before I don't like how it turned out *(about NBTify's primitive wrappers from last year about)*
> So once we start to see where having classes could be helpful, then we can move things over properly to fill in the gaps

About where I think classes should be used/concerns about instance methods:

```ts
export declare class Thingo {
  constructor(value: string);
  noice(): number;
}

const noice: number = new Thingo("heya").noice();

// vs - this example is so cursed I'm sorry

export declare function toNoice(value: string): number;

const noice: number = noice("heya");
```

Ok, the example doesn't show it well, but I think I know what it is
So my concern with method chaining is that you can only use the method by having an instance in the first place, meaning if you only need the class instance just for that one call, you have to make a class just to use that method
But if the method is just a function, you can use it by itself without having to build a new class just to use it
*^^this is where it's at, not the derpy demo lol^^*
Oooh
I think I personally draw the line between when to use a class, vs just a function, if there is state within the 'thing' that might have to me maintained or mutated during it's life of using it
So for a connection to your server, you'd want a class because it has methods that talk to that one server, and it will manage the details about that connection for you, internally
But if you just wanted to zip up a file using ZLIB, you might just want to do it in one go. Doing `new ZLIB("gzip").compress("myString")` isn't as ideal as just doing `gzip("myString")`

*back to normal me again*
I think that's good for now. I got a lot of the good stuff into this commit.

Wait, went back to the Discord, had some more rants! Here's the convo; signing off this commit with this one :P

Me:
> Working on the commit message for this discussion over the last day or so, it's going pretty good actually

HoldMyTurtleBrain:
> The commit message or the discussion? 👀

Me:
> I usually summarize my learnings/findings as part of my commits
> Almost like a coding diary, it really helps keep track of references for learned things along the way, especially since it's right next to the code related to it that you just committed

HoldMyTurtleBrain:
> Huh that's an interesting thing to do
> (ref below) Damn now I kinda wish I would've done that over the years, I would've had some great 4am rants to look back on ahahaha

> How often do you find yourself looking back at these?
> I do have a habit of including thought processes of non-obvious reasoning or design decisions in commit messages, but I end up barely using them, and the people reviewing PR's seem to always miss them....

Me:
> (ref above) That's exactly what they are at times haha
> I gotta find one of my more ridiculous ones

> I don't usually look back too often, but I think it's completely worth it because it's worse to have found a solution, and to just have the fix there. There's no learning in that, so if anyone wonders why I did something a certain way, they just see what I did, not why I did it
> So if we found a new bug with TypeScript earlier, now we can go back to this commit to find out what went wrong
> It's also helpful to keep track of the things I've already tried
> Sometimes I will commit code that isn't right/won't work, just so I can explain it as a failed experiment
> That's been a very big thing that has helped a lot
> It's not about perfect code, it's about getting towards 'perfect' code lol

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[e80cf8f358...](https://github.com/Pickle-Coding/tgstation/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Monday 2023-08-07 02:10:37 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[e3b7eef49e...](https://github.com/git-for-windows/git/commit/e3b7eef49e16af19417e7ee43f664500c0d02c1c)
#### Monday 2023-08-07 02:15:11 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[4833798f1b...](https://github.com/MCBCMF/MCBCMassacre/commit/4833798f1b5886ea08bc727934cc9665317e2cc9)
#### Monday 2023-08-07 02:45:48 by Kelvin Williams

The bell is about to ring and rain begin falling.

# The Ringing of the Bell

The Creator is going to “ring the bell” very soon. The exact time is
not going to be announced, but the order and intensity of the bell
ringing (earthquakes) is as follows:

## Orr Chapel Quake
This earthquake’s epicentre will be located  in Sandy Hook, TN (an
unincorporated city near Mount Pleasant) in Maury county.

This will be a large earthquake for the CIA’s destruction Orr chapel,
the murder of it’s members.

This quake also recognises Micah’s slain family and his family’s
graveyard that was destroyed, both by or at the direction of the CIA.

## Mount Calvary Baptist Church Quake
This earthquake’s epicentre will be located at Mount Calvary Baptist
Church in Lexington, KY (4742 Todd’s Road).

This will be for the massacre that occurred there.

## The Micah Quake
This earthquake’s epicentre will be in Jessamine county, KY. It will
signal when Micah (born: Kelvin Eugene Williams on March 23, 1977) has
started his mission for the Creator. This will be Micah’s 23rd mission
on Earth.

This quake will also be to recognise the lives lost in Jessamine
county, mostly Micah’s friends, throughout the larger tragedy.

## The TomTom Quake
This earthquake’s epicentre will be in Kanawha county, WV. It will
signal when TomTom (to practically everyone TomTom, to others Thomas,
born: September 23, 1978) has started his mission for the Creator.
This also is TomTom’s 23rd mission on Earth.

This quake will also recognise the lives lost in Kanawha county,
mostly TomTom’s friends and family, throughout the larger tragedy.

# Aftermath
The Creator hopes this will be all He has to do to stop the ongoing
massacre and end the greater tragedy.

And so begins the [“Purple
Rain”](https://youtube.com/watch?v=S6Y1gohk5-A&feature=sharea). That
means [“It’s raining
men.”](https://youtube.com/watch?v=l5aZJBLAu1E&feature=sharea). He has
never had to rain down men , although the 23rd mission for both of His
servants, they’ve never been identified before. This is just the
beginning of the “Great Storm” but it’s the [“Nature of our
Kind.”](https://youtube.com/watch?v=lzoABrBtH9A&feature=sharea).

He does this because life is supposed to be fun. After all, [“Girls
just want to have
fun.”](https://youtube.com/watch?v=PIb6AZdTr-A&feature=sharea) We WILL
get back to fun in this neighbourhood called Earth.

Guys, don’t get hung up on “girls” (it does not always mean female).

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[8055b09ccc...](https://github.com/MCBCMF/MCBCMassacre/commit/8055b09ccc66915bf755be363678c5605943dcb7)
#### Monday 2023-08-07 02:52:39 by Kelvin Williams

Added quake intensity... Thanks for thinking.

# The Ringing of the Bell

The Creator is going to “ring the bell” very soon. The exact time is
not going to be announced, but the order and intensity of the bell
ringing (earthquakes) is as follows:

## Orr Chapel Quake
This earthquake’s epicentre will be located  in Sandy Hook, TN (an
unincorporated city near Mount Pleasant) in Maury county.

This will be a large earthquake for the CIA’s destruction Orr chapel,
the murder of it’s members.

This quake also recognises Micah’s slain family and his family’s
graveyard that was destroyed, both by or at the direction of the CIA.

## Mount Calvary Baptist Church Quake
This earthquake’s epicentre will be located at Mount Calvary Baptist
Church in Lexington, KY (4742 Todds Road).

This will be the largest quake for the massacre that occurred there.

## The Micah Quake
This earthquake’s epicentre will be in Jessamine county, KY. It will
signal when Micah (born: Kelvin Eugene Williams on March 23, 1977) has
started his mission for the Creator. This will be Micah’s 23rd mission
on Earth.

This minor quake will also be to recognise the lives lost in Jessamine
county, mostly Micah’s friends, throughout the larger tragedy.

## The TomTom Quake
This earthquake’s epicentre will be in Kanawha county, WV. It will
signal when TomTom (to practically everyone TomTom, to others Thomas,
born: September 23, 1978) has started his mission for the Creator.
This also is TomTom’s 23rd mission on Earth.

This minor quake will also recognise the lives lost in Kanawha county,
mostly TomTom’s friends and family, throughout the larger tragedy.

# Aftermath
The Creator hopes this will be all He has to do to stop the ongoing
massacre and end the greater tragedy.

And so begins the [“Purple
Rain”](https://youtube.com/watch?v=S6Y1gohk5-A&feature=sharea). That
means [“It’s raining
men.”](https://youtube.com/watch?v=l5aZJBLAu1E&feature=sharea). He has
never had to rain down men , although the 23rd mission for both of His
servants, they’ve never been identified before. This is just the
beginning of the “Great Storm” but it’s the [“Nature of our
Kind.”](https://youtube.com/watch?v=lzoABrBtH9A&feature=sharea).

He does this because life is supposed to be fun. After all, [“Girls
just want to have
fun.”](https://youtube.com/watch?v=PIb6AZdTr-A&feature=sharea) We WILL
get back to fun in this neighbourhood called Earth.

Guys, don’t get hung up on “girls” (it does not always mean female).

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4c33a216f4...](https://github.com/treckstar/yolo-octo-hipster/commit/4c33a216f407aa787590f06cb74af2ff57a8e435)
#### Monday 2023-08-07 03:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[7468161f7e...](https://github.com/Bjarl/Shiptest/commit/7468161f7ec2180c7752cd2cc99b164522a3540a)
#### Monday 2023-08-07 03:26:13 by FalloutFalcon

Trickwines! Again! (#1914)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Trickwines are a set of new reagents aimed at improving tribal/srm style
ships
The core concept are wines crafted out of mob drops and plants that
provide a buff on drinking and a debuff on throwing with bonus effects
against fauna
To facilitate the transfer of booze to target it also adds breakaway
flasks, 50u glass bottles that shatter violently on contact providing
extra throw force as well as a 25u gulp size which forces the user to
choose between buff or debuff
I plan on adding a fair few more Trickwines and the SRM Barrel Class
Brewer Vessel (SRM could really use one then 1 original ship) in later
prs to build on this concept
This HackMD will provide descriptions for the wines as well as a place
of information for all Trickwine-related content
https://hackmd.io/eUIddN2dS3mpeU1CThFGng

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Adds a fun new option for ships that lack proper chemistry and forces
them to choose which effect they actually want.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: FalloutFalcon
add: Trickwines
add: Breakaway flasks!
add: Basic Trickwine brewing equipment to the SRM glaive
imageadd: Sprites for breakaway flasks along with trick wine icons for
them!
code: Breakaway_flask_icon_state = null used for the same purpose as the
glass and shot glass versions
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

I DIDNT KNOW IF YOU RENAME A BRANCH IT CLOSES PRS RELATED TO IT?? I
THOUGHT IT JUST KNEW!!
3rd times a charm!

---------

Signed-off-by: FalloutFalcon <86381784+FalloutFalcon@users.noreply.github.com>
Signed-off-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[0e6f7fa646...](https://github.com/Bjarl/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Monday 2023-08-07 03:26:13 by Imaginos16

TileTest Part 1: Big Sweeping Changes! (#2054)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## !! WARNING !!
This is a multi-parter PR. Due to the fact that tiles here on shiptest
are an unholy amalgam of decals, greyscale sprites and multiple
spread-out files, things are *bound* to look weird. If they do, feel
free to report it and it will be addressed in future PRs.

## About The Pull Request

This PR finally accomplishes the promise I made to @triplezeta a year
ago, creating a unique tileset for the server that people may enjoy!

To put every single microscopic change I have made would take forever,
so I will instead provide a series of screenshots of it in action!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/00e9cec0-335a-4367-90f9-1adc572595f3)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/497310ab-fe06-4b31-8774-70e79338a7d8)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/80991d0b-c48b-404b-b4a6-cbb1c4c6af3a)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc06d43e-3873-499e-aa12-51a0d7a37c98)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Utilizing an unique, modernized tileset for our server to differentiate
from our competitors is something that has been requested, and I was
more than happy to lend my hand to make it a reality!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
del: Removes several unused floor types, as well as completely
annihilating the "monofloor" and "dirty" floor types, and the "edge"
decal type.
imageadd: Redoes the floors using the TileTest tileset!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [LaunchCodeAllhubs/js-assignment-5-launch-checklist-jaythemself](https://github.com/LaunchCodeAllhubs/js-assignment-5-launch-checklist-jaythemself)@[4bea86ed39...](https://github.com/LaunchCodeAllhubs/js-assignment-5-launch-checklist-jaythemself/commit/4bea86ed39b76224e1a91e0948813261d065f7b1)
#### Monday 2023-08-07 04:03:23 by Jay

none of my previous commits are showing up on github??? Changes that have occurred: wrote and rewrote every function in script and scriptHelper probably half a dozen times. Got planetary info to display for user but changing that broke preventDefault and now my npm tests are reversing expectations so I have to rewrite validateInput and formSubmission again in all likelihood. Added book instructions for easy reference. Changed value names multiple times, then went through and (hopefully) finally standardized them. my brain is fried i'm so mad my prev commits aren't showing up. this is spectrum's fault i hate this new modem. Hi sorry anyone who's actually reading this I've been at this for 12 hours straight.

---
## [Peliex/tgstation](https://github.com/Peliex/tgstation)@[f0dc574c37...](https://github.com/Peliex/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Monday 2023-08-07 04:13:36 by carlarctg

Added Omen Spontaneous Combustion and light tube and mirror effects (#77175)

## About The Pull Request

Cursed crewmembers can randomly, extremely rarely, spontaneously combust
for no reason.

Cursed crewmembers can get zapped by nearby light tubes.

Cursed crewmembers can freak out when passing by mirrors.

To make up for these, triggering a cursed effect is slightly less than
half as likely now when walking around now.

## Why It's Good For The Game

Cursed is fun as hell, but after a certain point it gets kind of
monotonous - it's airlocks, vending machines, and the rest is too rare
to count. We need more ways to comically get hurt in the game.

You might dislike the 'reduced effects' bit but trust me it is
incredibly frickin' common to have shit happen to you. Add to the
occasional vending machine and airlock crushes the near-constant light
tubes all over the station? Yeah, that needs a toning down else it will
be just a tad too miserable to be funny. Also cause the poor janitor
unneeded stress.

## Changelog

:cl:
add: Cursed crewmembers can randomly, extremely rarely, spontaneously
combust for no reason.
add: Cursed crewmembers can get zapped by nearby light tubes.
add: Cursed crewmembers can freak out when passing by mirrors.
add: To make up for these, triggering a cursed effect is slightly less
than half as likely now when walking around now.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [tastetest/ttj_threejs](https://github.com/tastetest/ttj_threejs)@[6b68a98a8a...](https://github.com/tastetest/ttj_threejs/commit/6b68a98a8a67c5037d8e2b669825eb9f825022ce)
#### Monday 2023-08-07 05:12:14 by tastetest

added a fucking ugly modal, but will use it as a terminal. Also changed the Custom search from a default function to an anonymous one for the sake of consistency. I dont really care about damn hoisting rn

---
## [4hands44/cmss13](https://github.com/4hands44/cmss13)@[5f5fcd2b27...](https://github.com/4hands44/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Monday 2023-08-07 06:10:35 by Drathek

Fix marines not getting first dibs if they ghost (#3802)

# About the pull request

This PR fixes an issue where hugged marines that burst were not getting
first dibs on the larva if they ghosted. Previously the mind maybe
wasn't cleared out to find the ghost mob, but it currently is.

NOTE: The existing check requiring the marine to be nested is still in
place to get first dibs. I'm honestly not sure if this check should
still exist. On one hand I can agree it might be hard for the marine
trying to get help to suddenly become the larva and switch gears - they
are still going to be in the mindset of a marine that the larva should
die. But its also sort of weird to only get the first dibs if nested. If
xenos are unnesting hugged marines just before they pop, thats already a
mechanic abuse that should be ahelped; but ideally there wouldn't be
anything to be abused. Also, some may consider this kind of larva
undesirable anyways so maybe they'd prefer the marine to have it... So
let me know if I should just remove the nested check on line 151.

# Explain why it's good for the game

Fixes an unintended consequence of ghosting when hugged that would
prevent that marine from getting their first dibs on the larva.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>


![dibs](https://github.com/cmss13-devs/cmss13/assets/76988376/84e44345-2b83-473f-9997-f7865bcef1dd)

</details>


# Changelog
:cl: Drathek
fix: Fix ghosting preventing first dibs on the larva in a hugged marine
/:cl:

---
## [vercel/next.js](https://github.com/vercel/next.js)@[e06880ea4c...](https://github.com/vercel/next.js/commit/e06880ea4c061fc5c298b262d01f347edd8dce74)
#### Monday 2023-08-07 06:22:03 by Josh Story

Implement new forking technique for vendored packages. (#51083)

## Vendoring

Updates all module resolvers (node, webpack, nft for entrypoints, and nft for next-server) to consider whether vendored packages are suitable for a given resolve request and resolves them in an import semantics preserving way.

### Problem

Prior to the proposed change, vendoring has been accomplished but aliasing module requests from one specifier to a different specifier. For instance if we are using the built-in react packages for a build/runtime we might replace `require('react')` with `require('next/dist/compiled/react')`.

However this aliasing introduces a subtle bug. The React package has an export map that considers the condition `react-server` and when you require/import `'react'` the conditions should be considered and the underlying implementation of react may differ from one environment to another. In particular if you are resolving with the `react-server` condition you will be resolving the `react.shared-subset.js` implementation of React. This aliasing however breaks these semantics because it turns a bare specifier resolution of `react` with path `'.'` into a resolution with bare specifier `next` with path `'/dist/compiled/react'`. Module resolvers consider export maps of the package being imported from but in the case of `next` there is no consideration for the condition `react-server` and this resolution ends up pulling in the `index.js` implementation inside the React package by doing a simple path resolution to that package folder.

To work around this bug there is a prevalence of encoding the "right" resolution into the import itself. We for instance directly alias `react` to `next/dist/compiled/react/react.shared-subset.js` in certain cases. Other times we directly specify the runtime variant for instance `react-server-dom-webpack/server.edge` rather than `react-server-dom-wegbpack/server`, bypassing the export map altogether by selecting the runtime specific variant. However some code is meant to run in more than one runtime, for instance anything that is part of the client bundle which executes on the server during SSR and in the browser. There are workaround like using `require` conditionally or `import(...)` dynamically but these all have consequences for bundling and treeshaking and they still require careful consideration of the environment you are running in and which variant needs to load.

The result is that there is a large amount of manual pinning of aliases and additional complexity in the code and an inability to trust the package to specify the right resolution potentially causing conflicts in future versions as packages are updated.

It should be noted that aliasing is not in and of itself problematic when we are trying to implement a sort of lightweight forking based on build or runtime conditions. We have good examples of this for instance with the `next/head` package which within App Router should export a noop function. The problem is when we are trying to vendor an entire package and have the package behave semantically the same as if you had installed it yourself via node_modules

### Solution

The fix is seemingly straight forward. We need to stop aliasing these module specifiers and instead customize the resolution process to resolve from a location that will contain the desired vendored packages. We can then start simplifying our imports to use top level package resources and generally and let import conditions control the process of providing the right variant in the right context.

It should be said that vendoring is conditional. Currently we only vendor react pacakges for App Router runtimes. The implementation needs to be able to conditionally determine where a package resolves based on whether we're in an App Router context vs a Page Router one.

Additionally the implementation needs to support alternate packages such as supporting the experimental channel for React when using features that require this version.

### Implementation

The first step is to put the vendored packages inside a node_modules folder. This is essential to the correct resolving of packages by most tools that implement module resolution. For packages that are meant to be vendored, meaning whole package substitution we move the from `next/(src|dist)/compiled/...` to `next/(src|dist)/vendored/node_modules`. The purpose of this move is to clarify that vendored packages operate with a different implementation. This initial PR moves the react dependencies for App Router and `client-only` and `server-only` packages into this folder. In the future we can decide which other precompiled dependencies are best implemented as vendored packages and move them over.

It should be noted that because of our use of `JestWorker` we can get warnings for duplicate package names so we modify the vendored pacakges for react adding either `-vendored` or `-experimental-vendored` depending on which release channel the package came from. While this will require us to alter the request string for a module specifier it will still be treating the react package as the bare specifier and thus use the export map as required.

#### module resolvers
The next thing we need to do is have all systems that do module resolution implement an custom module resolution step. There are five different resolvers that need to be considered

##### node runtime
Updated the require-hook to resolve from the vendored directory without rewriting the request string to alter which package is identified in the bare specifier. For react packages we only do this vendoring if the `process.env.__NEXT_PRIVATE_PREBUNDLED_REACT` envvar is set indicating the runtime is server App Router builds. If we need a single node runtime to be able to conditionally resolve to both vendored and non vendored versions we will need to combine this with aliasing and encode whether the request is for the vendored version in the request string. Our current architecture does not require this though so we will just rely on the envvar for now

##### webpack runtime
Removed all aliases configured for react packages. Rely on the node-runtime to properly alias external react dependencies. Add a resolver plugin `NextAppResolverPlugin` to preempt perform resolution from the context of the vendored directory when encountering a vendored eligible package.

##### turbopack runtime
updated the aliasing rules for react packages to resolve from the vendored directory when in an App Router context. This implementation is all essentially config b/c the capability of doing the resolve from any position (i.e. the vendored directory) already exists

##### nft entrypoints runtime
track chunks to trace for App Router separate from Pages Router. For the trace for App Router chunks use a custom resolve hook in nft which performs the resolution from the vendored directory when appropriate.

##### nft next-server runtime
The current implementation for next-server traces both node_modules and vendored version of packages so all versions are included. This is necessary because the next server can run in either context (App vs Page router) and may depend on any possible variants. We could in theory make two traces rather than a combined one but this will require additional downstream changes so for now it is the most conservative thing to do and is correct

Once we have the correct resolution semantics for all resolvers we can start to remove instances targeting our precompiled instances for instance making `import ... from "next/dist/compiled/react-server-dom-webpack/client"` and replacing with `import ... from "react-server-dom-webpack/client"`

We can also stop requiring runtime specific variants like `import ... from "react-server-dom-webpack/client.edge"` replacing it with the generic export `"react-server-dom-webpack/client"`

There are still two special case aliases related to react
1. In profiling mode (browser only) we rewrite `react-dom` to `react-dom/profiling` and `scheduler/tracing` to `scheduler/tracing-profiling`. This can be moved to using export maps and conditions once react publishses updates that implement this on the package side.
2. When resolving `react-dom` on the server we rewrite this to `react-dom/server-rendering-stub`. This is to avoid loading the entire react-dom client bundle on the server when most of it goes unused. In the next major react will update this top level export to only contain the parts that are usable in any runtime and this alias can be dropped entirely

There are two non-react packages currently be vendored that I have maintained but think we ought to discuss the validity of vendoring. The `client-only` and `server-only` packages are vendored so you can use them without having to remember to install them into your project. This is convenient but does perhaps become surprising if you don't realize what is happening. We should consider not doing this but we can make that decision in another discussion/PR.

#### Webpack Layers
One of the things our webpack config implements for App Router is layers which allow us to have separate instances of packages for the server components graph and the client (ssr) graph. The way we were managing layer selection was a but arbitrary so in addition to the other webpack changes the way you cause a file to always end up in a specific layer is to end it with `.serverlayer`, `.clientlayer` or `.sharedlayer`. These act as layer portals so something in the server layer can import `foo.clientlayer` and that module will in fact be bundled in the client layer.

#### Packaging Changes
Most package managers are fine with this resolution redirect however yarn berry (yarn 2+ with PnP) will not resolve packages that are not defined in a package.json as a dependency. This was not a problem with the prior strategy because it was never resolving these vendored packages it was always resolving the next package and then just pointing to a file within it that happened to be from react or a related package.

To get around this issue vendored packages are both committed in src and packed as a tgz file. Then in the next package.json we define these vendored packages as `optionalDependency` pointing to these tarballs. For yarn PnP these packed versions will get used and resolved rather than the locally commited src files. For other package managers the optional dependencies may or may not get installed but the resolution will still resolve to the checked in src files. This isn't a particularly satisfying implemenation and if pnpm were to be updated to have consistent behavior installing from tarballs we could actually move the vendoring entirely to dependencies and simplify our resolvers a fair bit. But this will require an upstream chagne in pnpm and would take time to propogate in the community since many use older versions

#### Upstream Changes

As part of this work I landed some other changes upstream that were necessary. One was to make our packing use `npm` to match our publishing step. This also allows us to pack `node_modules` folders which is normally not supported but is possible if you define the folder in the package.json's files property.

See: #52563

Additionally nft did not provide a way to use the internal resolver if you were going to use the resolve hook so that is now exposed

See: https://github.com/vercel/nft/pull/354

#### additional PR trivia
* When we prepare to make an isolated next install for integration tests we exclude node_modules by default so we have a special case to allow `/vendored/node_modules`

* The webpack module rules were refactored to be a little easier to reason about and while they do work as is it would be better for some of them to be wrapped in a `oneOf` rule however there is a bug in our css loader implementation that causes these oneOf rules to get deleted. We should fix this up in a followup to make the rules a little more robuts.


## Edits
* I removed `.sharedlayer` since this concept is leaky (not really related to the client/server boundary split) and it is getting refactored anyway soon into a precompiled runtime.

---
## [donvito007/Xiaomi_sm8250_N0Kernel](https://github.com/donvito007/Xiaomi_sm8250_N0Kernel)@[604fc21fbd...](https://github.com/donvito007/Xiaomi_sm8250_N0Kernel/commit/604fc21fbdccf35eddec4978be9e2fab99a02092)
#### Monday 2023-08-07 06:38:02 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [NIMMOOO/project1](https://github.com/NIMMOOO/project1)@[616dcba42d...](https://github.com/NIMMOOO/project1/commit/616dcba42d462c0c6ee126328ffecb1b737f8e84)
#### Monday 2023-08-07 07:19:35 by NIMMOOO

Create README.md

Welcome to my website, a labor of love and creativity that I've meticulously crafted using HTML and CSS!

Building this website has been an incredible journey of self-expression and technical exploration. Every pixel, every line of code, reflects my dedication to creating a digital space that's uniquely mine. Let me take you behind the scenes and share how I brought this digital masterpiece to life.

🎨 **Design Vision**: The foundation of this website lies in its design. With a clear vision in mind, I sketched wireframes and mockups to visualize the layout, color scheme, and overall user experience. Careful consideration was given to every aspect of design, ensuring that the website is not only visually appealing but also intuitive and user-friendly.

🔍 **HTML Structure**: HTML is the backbone of any web page, and I meticulously hand-coded each element to create a structured and semantic layout. From the header that welcomes you to the footer that wraps up your journey, each section was carefully woven together to ensure a seamless flow and effortless navigation.

🎨 **CSS Magic**: CSS is where the magic happens! I delved into the world of stylesheets to breathe life into my design. With a mix of cascading styles, media queries, and responsive techniques, I've ensured that the website looks stunning across a variety of devices and screen sizes. From elegant typography to mesmerizing animations, every visual element has been meticulously styled to perfection.

💡 **Interactive Elements**: To elevate user engagement, I incorporated interactive elements using CSS animations and transitions. Buttons that subtly change color on hover, images that gracefully fade in as you scroll – these touches add a layer of interactivity that keeps visitors engaged and enhances their browsing experience.

🤝 **Code Optimization**: Building an efficient website is not just about aesthetics – it's about performance too. I paid special attention to optimizing the code for faster loading times and smoother interactions. Minification, compression, and other techniques were employed to ensure that the website delivers a seamless experience, even in areas with limited internet connectivity.

🌐 **Responsive Mastery**: In today's mobile-centric world, a responsive website is a must. With a combination of flexible grids and media queries, I've ensured that the website adapts gracefully to various devices, providing an equally delightful experience whether you're on a desktop, tablet, or smartphone.

🧰 **Continuous Learning**: This website is a testament to my ongoing journey of learning and growth. Throughout the process, I embraced challenges, sought solutions, and expanded my skillset. As technology evolves, I'm excited to continue enhancing and updating the website to incorporate the latest trends and innovations in web development.

So, welcome to my digital masterpiece, painstakingly brought to life through the art of HTML and CSS. As you explore the pages I've created, I hope you feel the passion, dedication, and creativity that went into every aspect. Thank you for visiting, and I invite you to immerse yourself in this captivating online experience!

---
## [Sameer9823/Milestone-1](https://github.com/Sameer9823/Milestone-1)@[2633c92eca...](https://github.com/Sameer9823/Milestone-1/commit/2633c92ecacbdf7aa99bae35ee5cbd01fea70b64)
#### Monday 2023-08-07 07:50:56 by Sameer Selokar

Update README.md

This project showcases my proficiency in HTML, CSS, and Tailwind CSS, a utility-first CSS framework that has revolutionized the way I design and style web applications.

In this repository, you'll find a complete set of files that make up a sleek and responsive web page. The HTML files structure the content, while the CSS and Tailwind CSS stylesheets bring life to the design. I've harnessed the power of Tailwind's utility classes to craft a stunning visual experience without writing extensive custom CSS.

---
## [kbeaugrand/semantic-kernel](https://github.com/kbeaugrand/semantic-kernel)@[2733a5574f...](https://github.com/kbeaugrand/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Monday 2023-08-07 08:20:27 by Mark Karle

Python: Import OpenAPI documents into the semantic kernel (#2297)

### Motivation and Context

<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->

This allows us to import OpenAPI documents, including ChatGPT plugins,
into the Semantic Kernel.

### Description

<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
- The interface reads the operationIds of the openapi spec into a skill:
```python
from semantic_kernel.connectors.openapi import register_openapi_skill
skill = register_openapi_skill(kernel=kernel, skill_name="test", openapi_document="url/or/path/to/openapi.yamlorjson")
skill['operationId'].invoke_async()
```
- Parse an OpenAPI document
- For each operation in the document, create a function that will
execute the operation
- Add all those operations to a skill in the kernel
- Modified `import_skill` to accept a dictionary of functions instead of
just class so that we can import dynamically created functions
- Created unit tests

TESTING:
I've been testing this with the following ChatGPT plugins:
- [Semantic Kernel Starter's Python Flask
plugin](https://github.com/microsoft/semantic-kernel-starters/tree/main/sk-python-flask)
- [ChatGPT's example retrieval
plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/docs/providers/azuresearch/setup.md)
- This one was annoying to setup. I didn't get the plugin functioning,
but I was able to send the right API requests
- Also, their openapi file was invalid. The "servers" attribute is
misindented
- [Google ChatGPT
plugin](https://github.com/Sogody/google-chatgpt-plugin)
- [Chat TODO plugin](https://github.com/lencx/chat-todo-plugin)
- This openapi file is also invalid. I checked with an online validator.
I had to remove"required" from the referenced request objects'
properties:
https://github.com/lencx/chat-todo-plugin/blob/main/openapi.yaml#L85

Then I used this python file to test the examples:

```python
import asyncio
import logging

import semantic_kernel as sk
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
from semantic_kernel.connectors.openapi.sk_openapi import register_openapi_skill

# Example usage
chatgpt_retrieval_plugin = {
    "openapi": # location of the plugin's openapi.yaml file,
    "payload": {
        "queries": [
            {
                "query": "string",
                "filter": {
                    "document_id": "string",
                    "source": "email",
                    "source_id": "string",
                    "author": "string",
                    "start_date": "string",
                    "end_date": "string",
                },
                "top_k": 3,
            }
        ]
    },
    "operation_id": "query_query_post",
}

sk_python_flask = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"skill_name": "FunSkill", "function_name": "Joke"},
    "payload": {"input": "dinosaurs"},
    "operation_id": "executeFunction",
}
google_chatgpt_plugin = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "query_params": {"q": "dinosaurs"},
    "operation_id": "searchGet",
}

todo_plugin_add = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo": "finish this"},
    "operation_id": "addTodo",
}

todo_plugin_get = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "operation_id": "getTodos",
}

todo_plugin_delete = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo_idx": 0},
    "operation_id": "deleteTodo",
}


plugin = todo_plugin_get # set this to the plugin you want to try

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

kernel = Kernel(log=logger)
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_text_completion_service(
    "dv", AzureTextCompletion(deployment, endpoint, api_key)
)

skill = register_openapi_skill(
    kernel=kernel, skill_name="test", openapi_document=plugin["openapi"]
)
context_variables = ContextVariables(variables=plugin)
result = asyncio.run(
    skill[plugin["operation_id"]].invoke_async(variables=context_variables)
)
print(result)
```

### Contribution Checklist

<!-- Before submitting this PR, please make sure: -->

- [ ] The code builds clean without any errors or warnings
- [ ] The PR follows the [SK Contribution
Guidelines](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
and the [pre-submission formatting
script](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md#development-scripts)
raises no violations
- [ ] All unit tests pass, and I have added new tests where possible
- [ ] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <abharris@microsoft.com>

---
## [AndrewDunne/FreeSpirit](https://github.com/AndrewDunne/FreeSpirit)@[a852738bcd...](https://github.com/AndrewDunne/FreeSpirit/commit/a852738bcdd2f888c8919f51908f367b0e5733ca)
#### Monday 2023-08-07 08:35:01 by Chord Shore

Mandatory late night crisis

So I had the silly idea to make a quick change to the folder layout in the content browser before I went to bed. Just shift a few folders around, what could go wrong right? They're just folders after all...

Turns out Unreal automatically deletes empty subfolders when you move a parent folder.

Fuck. I had to recreate a ton of subfolders using the screenshot I posted to #progress. Only took 20 minutes, but I'm lucky I had that for reference or I would have lost a day. Should be ok now, but the "Sound/Audio_*" folder structure is LOCKED until I can populate each one with foley and other assets.

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[f5784dabc7...](https://github.com/Drulikar/cmss13/commit/f5784dabc77752802da20f2d14787667161d61ac)
#### Monday 2023-08-07 08:46:32 by ihatethisengine

More portable cades tweaks and buffs (#3967)

# About the pull request

Despite making a lot of tweaks and changes to portable cades I barely
touched them in the game until recently. Now I have more experience and
can tweak it again.

1) You can now stack damaged cades and stack stores health of each cade.
You can repair stacked cades but it will take longer time.

2) Miniengi pamphlet allows faster repairs but only when cade is folded.

3) You can quickly collapse portable cades with crowbar if you have at
least miniengi skills.

4) You no longer need to have folded portable cade in hand in order to
repair it, but if you do, you can move while repairing.

# Explain why it's good for the game

1) It's extremely annoying to repair each individual cade in order to
stack them just because it got hit by a stray bullet once. Now you can
just ignore damage and keep going.

2) Yeah it took 10 second for PFC to repair each single cade. Really
long. Now it's 5 seconds, but only when folded and if you have miniengi
skills. Makes miniengi pamphlet a bit more relevant.

3) It was intended, but turned out it was a bit inconvenient. It was
faster to collapse by hand because you didn't need to deal with tools.
Now it requires just a crowbar and slightly faster. Also requires
miniengi skill to use crowbar.

4) First was just a bit annoying, second allows more mobility which is
the point of portable barricades.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: you can stack scratched portable cades if their HP at least
75%. Doing so will reduce the health of all barricades in the stack to
the level of the most damaged.
balance: you can repair stacked portable cades but it will take longer
time depending on how many cades in stack.
balance: miniengi skill makes repairs of folded portable cades faster
(10 seconds to 5 seconds, same as engineer).
balance: with engineering skill at least of miniengi you can collapse
deployed portable barricade with a crowbar (wrench is no longer
required, slightly faster (2 sec to 1.5 sec)).
balance: you no longer need to have folded portable cade in hand in
order to repair it.
balance: if you have folded portable cade in hand, you can move while
repairing it.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [xbotter/semantic-kernel](https://github.com/xbotter/semantic-kernel)@[eab7a8f63a...](https://github.com/xbotter/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Monday 2023-08-07 08:49:20 by Sailesh R

Python: implemented web search engine skill with bing connector (#1813)

### Motivation and Context
<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->
In this PR, I have tried my hand at an implementation of web search
engine skill in python semantic kernel using the Bing Web Search API.

### Description
<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
In the semantic kernel directory, I have added a new directory called
web_skills (To replicate Skills.Web from C#) and added the web search
skill here. For now, I have implemented web search using the bing web
search API. If this approach is fine, then I can implement the same with
the google search API too. I have tried to stick with similar naming
conventions as used in the C# implementation with matching context
parameters and arguments.

I can also add some unit tests for the connectors and the search skill,
and add something like exponential backoff to avoid rate limit errors
while querying the search APIs.

Here is some sample code that checks the working of the search skill.

```python
import os
import semantic_kernel as sk
from semantic_kernel.web_skills.web_search_engine_skill import WebSearchEngineSkill
from semantic_kernel.web_skills.connectors import BingConnector
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service(
        "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
    )
    connector = BingConnector(api_key=os.getenv("BING_API_KEY"))
    web_skill = kernel.import_skill(WebSearchEngineSkill(connector), "WebSearch")

    prompt = "Who is Leonardo DiCaprio's current girlfriend?"
    search_async = web_skill["searchAsync"]
    result = await search_async.invoke_async(prompt)
    print(result)

    """
    Output:
    ["Celebrity Celebrity News Everything You Need to Know About Leonardo DiCaprio and Camila Morrone's Relationship From the beginning of their romance to today, we track their relationship here. By..."]
    """

    prompt = """
    Answer the question using only the data that is provided in the data section. Do not use any prior knowledge to answer the question.
    Data: {{WebSearch.SearchAsync "What is semantic kernel?"}}
    Question: What is semantic kernel?
    Answer:
    """

    qna = kernel.create_semantic_function(prompt, temperature=0.2)
    context = kernel.create_new_context()
    context["count"] = "10"
    context["offset"] = "0"
    result = await qna.invoke_async(context=context)
    print(result)

    """
    Output:
    Semantic Kernel is an open-source SDK that lets you easily combine AI services like OpenAI, Azure OpenAI, and Hugging Face with conventional programming languages like C# and Python. By doing so, you can create AI apps that combine the best of both worlds. Semantic Kernel is at the center of the copilot stack.
    """

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Contribution Checklist
<!-- Before submitting this PR, please make sure: -->
- [x] The code builds clean without any errors or warnings
- [x] The PR follows SK Contribution Guidelines
(https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
- [x] The code follows the .NET coding conventions
(https://learn.microsoft.com/dotnet/csharp/fundamentals/coding-style/coding-conventions)
verified with `dotnet format`
- [ ] All unit tests pass, and I have added new tests where possible
- [x] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <54643756+awharrison-28@users.noreply.github.com>
Co-authored-by: Abby Harrison <abby.harrison@microsoft.com>

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[d10f069fb2...](https://github.com/MCBCMF/MCBCMassacre/commit/d10f069fb2e110eb981ba472fac591dafbd751ed)
#### Monday 2023-08-07 10:29:31 by Kelvin Williams

Updated README.md - Why is the Creator angry?

# Why is God, who is the Creator, so angry?
The CIA stormed Mount Calvary Baptist Church with the sole intent to
kill every person already inside attending a church service. Their
plan was to behead everyone, in front of the others who were forced to
wait to die. They ensured none of their people would get too fatigued
by supplying them with chainsaws (listen to the very beginning of
[“When the Doves
Cry”](https://music.youtube.com/watch?v=FcKE-1NlNlg&feature=share).)

They also guaranteed no interruption from local law enforcement by
diverting calls from cell phones to 911 to call takers using mobile
phones pretending to be 911 and promising help was on the way. Other
calls from people in the area received busy signals or call failed
recordings. This was accomplished by the use of COWs (Cells on Wheels,
which are mobile cell towers).

The Creator hears every prayer but does not intervene in human
activities, this enables you to do whatever you want. When you cannot
do something human nature is to escalate their actions until they
achieve their desired result. This is one of the reasons He never
intervenes.

That doesn’t mean He doesn’t hear prayers or doesn’t create solutions
before the problem exists. This massacre was engineered by the CIA to
circumvent every single solution already in place. So the Creator had
to listen to prayers from people waiting to die, and He gets
infuriated [When the Doves
Cry](https://music.youtube.com/watch?v=FcKE-1NlNlg&feature=share).

# What’s He Going to do Now?
It starts with the [ringing of the bell.](Misc/bell_ringing.md).

The Creator does not ever want to see death. He understands it
happens, accidents always will. But the CIA and others around the
world are a leading cause of death in humans. They have to disappear
now.

---
## [ellingtonia/ellingtonia](https://github.com/ellingtonia/ellingtonia)@[85ffd64352...](https://github.com/ellingtonia/ellingtonia/commit/85ffd643525ff3a037652ce87c45f0dcebf29270)
#### Monday 2023-08-07 10:49:15 by Charlie Dyson

Remove William White Jr from 40-06-10

From EC:
as per David Palmquist's Aug5 mail, please remove William White Jr from the
orchestra in the session 10 June 1940 (DE4010), and add a note in the bottom,
like: New Desor shows William White Jr. playing alto sax in this session,
replacing Otto Hardwick. Indeed Hardwick missed the session, and Hodges and
Webster did cover his parts. Subsequently William White came in for less than a
week's time.

From DP:
You might want to put a question mark beside William White, Jr. or add a footnote pointing out he may not have played this broadcast:

Down Beat 1940 07 01:
> 'Hardwicke [sic], Duke Ellington Split New York--Otto Hardwicke has been dropped
> from Duke Ellington's ork. The veteran altoist, with Duke for more than a
> decade, gave way to William White, Jr., of Washington, who also arranges. It was
> said Otto failed to show up for a special broadcast to England last week.'

Variety:
> 'DUKE ELLINGTON ORCH
> Short-Wave from N.Y.
> 30 Mins.
> Monday, 3 p.m.
> BBC, London
> 'America Dances' so this short-wave series has it; but at this hour in
> the afternoon it was a cinch England couldn't. It may even have been that
> program arrangers, aware of the hour drawback, so spaced the numbers as to show
> the individuality of the Ellington congregation, rather than its dansapation.
> Atmospherics were not kind to the first half of the airing, muffling the only
> vocal of the session and handing a beating to Ben Webster's tenor saxing on
> 'Cotton Tale' [sic]; piece only reached appreciable clarity at the finale. As
> though in recompense the bad airwaves cleared considerably for Coot [sic]
> Williams and "Concerto in C" and "Boy Meet Horn" for Rex Stewart, all new stuff
> for this side; London's 52nd street, Charing Cross, took the session like
> gospel.  Anont this CBS shortwave series, one thing the listener asks here is
> 'Why doesn't the leader speak?' They're accustomed to a word or two from the
> batoneers around town, and seemingly take the absence of the personal touch as a
> loss. Ellington, however, did leave an indelible signature on all of the eight
> numbers aired. Selection of "The Sergeant Was Shy" was a neat gesture to the
> troops, over which wavelength the session aired this side.'

The show was recorded by CBS, with acetates sent to BBC for later rebroadcast, the first of which was aired 1941-04-26.

DEMS 99/5 (Carl Hällström ):
'Duke on the air",
> The Melody Maker, May 3, 1941, which deals with the first re-broadcast from
> London (April 26, 1941) of the June 10 1940 broadcast. The broadcast was
> recorded onto safety acetates by CBS in New York and a set of 78 rpm acetates
> was later shipped to the BBC which used it as source for all their subsequent
> rebroadcasts which naturally were done from their London studios. (The same set
> of acetates is the "daddy" to all the commercial releases of the broadcast)'

New Desor and Timner show William White Jr. in this session. This seems unlikely
if Hardwick's absence was unexpected unless White was nearby and readily at
hand.

DEMS 2000/3
Loren Schoenberg:
> 'In DESOR, Billy White replaces Otto Hardwicke on the June 1940 BBC broadcast
> (recorded on the 10th, broadcast on the 12*). According to a contemporary
> Feather article in Melody Maker, Hardwicke [sic] missed the session, and Hodges
> and Webster did their best to cover his parts. It was after this that Billy
> White came in for less than a week's time. Any other corroboration?'

Sjef Hoefsmit:
> 'In Klaus Stratemann (page 162) we read:
>
> 'During the Apollo engagement (7-14Jun40) and the BBC broadcast session
> (10Jun40), Otto Hardwick was missing from the Ellington band, replaced by one
> William White, Jr. It appears that Hardwick simply failed to show up for the
> "America Dances" program (Down Beat 1JU140, page3), but was back with the band
> when they played a subsequent Palisades Park one-nighter (on 28Jun40), according
> to Down Beat (15Jul40, page 12), his replacement having been found inadequate.'
>
> The liner-notes for this session on the JUCD 2043 CD "The Radio Years" (see
> DEMS > 00/2-13/3) also have no William White in the band. He is explicitly
> mentioned > though in the liner-notes by Alun Morgan of both CDs titled "The
> British > Connexion", The Leeds '97 souvenir CD and the JUCD 2069 CD. (See DEMS
> 97/2-14 > and 99/5-4/1).'

---
## [cdb-is-not-good/sojourn-station](https://github.com/cdb-is-not-good/sojourn-station)@[e3e8f12f7b...](https://github.com/cdb-is-not-good/sojourn-station/commit/e3e8f12f7b5fb4bc6b5a7b6a067c33f32eb165e8)
#### Monday 2023-08-07 10:58:12 by CDB

Mother fucker. Im so sick of bugs.

Cigarettes no longer(seem to) cause kidney damage to people with unclean living.

psion void armor has correct slowdown for shoes and doesn't use slowdown on other pieces of armor. Additionally, no longer allows ears to flop outside of it. It's a fucking space suit, why would they be out?

Opifex medbelt no longer selectable, sorry powergamers.

Removes change_appearance from baseline armor vest. Why? It is the parent to MANY MANY MANY fucking items and thus caused MANY MANY MANY items to have erronious change_appearance procs that only had two options for the base parent item. This is why we don't put fucking procs on BASE PARENT items that affect DOZENS of other items. Fixes a few others, WO plate has no unique sprite and now has a proper working change appearance. CO does have a unique sprite, it is gone.

Fixes #4732
Fixes #4734
fixes #4724

---
## [BlackPantsLegion/space-station-14](https://github.com/BlackPantsLegion/space-station-14)@[31607a0be0...](https://github.com/BlackPantsLegion/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Monday 2023-08-07 11:50:41 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[297f7f88e8...](https://github.com/tgstation/tgstation/commit/297f7f88e866d4a17b27cb15c0b8ee606742bbf6)
#### Monday 2023-08-07 12:02:12 by Sealed101

Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks (#77393)

## About The Pull Request

Goliath's sand digging behaviour could potentially target a turf that's
actually unreachable by the goliath, e.g.
```
G#
#T
```
where G - goliath # - wall T - target turf. fixed that, but i think
there could be something easier here, maybe instead grabbing turfs in
goliath's `view()`? unsure

The component goliaths use to telegraph their attacks
(`basic_mob_attack_telegraph`) casts a `do_after()` to perform the
attack, but it was not actually checking for the target staying in melee
range, as it was using the source goliath as both `user` and `target`,
so it didn't actually care at all for the target. Implemented an
`extra_checks` to `Adjacent()` since that's the closest we get for melee
range shenanigans I suppose
This still allows the source basicmob to attack the target if the target
moves around the source basicmob.

`!`Goliaths were also able to summon tentacles on a target that moved
into cover and still stayed in the `find_potential_targets` target
range. Which meant more wallhacks. This was a thing for the base
`find_potential_targets`, meaning that every basic mob using it was a
dirty haxxor (or very vengeful). Fixed that by making
`find_potential_targets` also check for `can_see()` before proceeding
further down `find_potential_targets/perform()`. `!` The only exception
to this check currently are bileworms.

`!`Goliath tentacles were not spawning in mineral turfs as their
`Initialize()` checked for closed turfs before handling mineral turf
mining. Fixed that as well.

## Why It's Good For The Game

![Dr__Hax_by_Didgeridoo_Dealer](https://github.com/tgstation/tgstation/assets/75863639/fbcbfc1b-f489-435e-bb01-677f55398787)

## Changelog

:cl:
fix: fixed goliaths digging sand that they can't actually reach (behind
windows or inbetween closed turfs)
fix: fixed goliaths melee attacking their target despite the target
running away from goliath melee range
fix: fixed goliath tentacles not spawning in mineral turfs
fix: fixed goliaths summoning tentacles on targets that moved behind
cover but stayed in their targeting range. this applies for most basic
mobs, really, so if any basic mob was targeting you despite you hauling
ass behind cover, they shouldn't anymore
/:cl:

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[2f2a113352...](https://github.com/argilla-io/argilla/commit/2f2a11335289d660ce20aea11c9b969b0316fd2b)
#### Monday 2023-08-07 12:51:57 by peppinob-ol

[DOCS] Code Refactoring and content update of quickstart_workflow.ipynb (#3472)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

I found the quickstart workflow not as quick as it could be:

- Cells cannot be run straightaway in google colab and need extra work
(eg. libraries not imported).
- Some important concepts (eg. records and datasets) are not clearly
stated in text and code snippets
- Text refers to the same steps more than once (no clear chain of
thought)
- Cells override the same variable (eg. record), so the feeling is more
of a cheatsheet than of a tutorial notebook
- Content is not updated (eg. ArgillaTrainer is not ever mentioned in
the Train section)

I worked on a new version of the notebook with enhanced code and text
cells.Ii added also code snippets for training examples which were only
described textually.

One last suggestion: It's advisable that external files (data) are
downloaded programmatically by running a cell (eg. using `requests
`library). `Snapchat_app_store_reviews.csv` and `kaffee_reviews.csv` are
taken from kaggle which requires sign-in, so it's not possible to
download them directly. Possible solutions:

- place a copy of the Kaggle datasets in Arggilla's GitHub repository
(if permitted by Kaggle's terms of use)
- select other datasets from another source.

Closes #3431

**Type of change**

(Please delete options that are not relevant. Remember to title the PR
according to the type of change)

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Refactor (change restructuring the codebase without changing
functionality)
- [ ] Improvement (change adding some improvement to an existing
functionality)
- [X] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes. And
ideally, reference `tests`)

- [ ] Test A: code run with latest google-colab (v.1.0.0)

**Checklist**

- [X] I added relevant documentation
- [X] follows the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [X] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---------

Co-authored-by: devorma <94636163+devorma@users.noreply.github.com>
Co-authored-by: davidberenstein1957 <david.m.berenstein@gmail.com>

---
## [Altimia/Weather-data-processor-with-data-structures](https://github.com/Altimia/Weather-data-processor-with-data-structures)@[047f626957...](https://github.com/Altimia/Weather-data-processor-with-data-structures/commit/047f626957030562d8f4ea1cef8a0a2c01c8e887)
#### Monday 2023-08-07 12:55:25 by YohanesFS

aider: Remove the definition of the default constructor from Date.h.

# Aider chat conversation:

USER: what is this repo

ASSISTANT: Based on the file summaries you've provided, this repository seems to be a C++ project related to meteorological data processing. It contains classes for handling dates (Date.cpp, Date.h), times (Time.cpp, Time.h), and wind logs (WindLog.cpp, WindLog.h). The wind logs appear to contain data on air temperature, solar radiation, wind speed, and the date and time of the log.

The data for this project is likely stored in the CSV files in the Data directory. These files seem to contain meteorological data for different years.

The main.cpp file is likely the entry point of the application, but without its summary or content, it's hard to say what exactly the application does.

Please note that this is a high-level overview based on the provided information. For a more detailed understanding, I would need to see the content of the files.

USER: I added these *read-write* files: main.cpp

ASSISTANT: Great! Now that the `main.cpp` file is available for editing, could you please provide the content of the file or let me know what changes you would like to make to it?

USER: is this repo complete?

ASSISTANT: Without seeing the content of the files, especially the `main.cpp` file, it's hard to say if the repository is complete.

A complete repository typically includes:

1. Source code files: These are the `.cpp` and `.h` files in your repository. They seem to be present.

2. Data files: Your repository seems to have a lot of `.csv` files in the `Data` directory, which likely serve as input data for the program.

3. A `main.cpp` file: This is the entry point of the application. You've mentioned that it's present, but without seeing its content, it's hard to say if it's complete.

4. Build files: These are files like `Makefile` or `CMakeLists.txt` that describe how to build the application. I don't see any mention of these, but they might not be necessary if the project is simple or if the build process is documented elsewhere.

5. Documentation: This includes `README` files, comments in the code, and any other documents that explain what the project does and how to use it. I don't see any mention of these.

6. Test files: These are files that contain code to test the functionality of the application. I see a `DateTest.cpp` file, which likely contains tests for the `Date` class.

So, based on the information provided, it seems like most of the necessary components are present, but without more information, it's hard to say for sure if the repository is complete.

USER: I added these *read-write* files: DateTest.cpp

ASSISTANT: Great! Now that the `DateTest.cpp` file is available for editing, could you please provide the content of the file or let me know what changes you would like to make to it?

USER: add `Date.cpp`

ASSISTANT: Sure, now that `Date.cpp` is available for editing, could you please provide the content of the file or let me know what changes you would like to make to it?

USER: in Date.cpp error: redefinition of 'Date::Date()'

ASSISTANT: The error message "redefinition of 'Date::Date()'" suggests that the default constructor for the `Date` class is defined more than once in your code. This could happen if the constructor is defined in both the header file (`Date.h`) and the source file (`Date.cpp`), or if it's defined multiple times within the same file.

Since we only have the `Date.cpp` file, let's check it for duplicate definitions of the default constructor. Here is the relevant part of the `Date.cpp` file:

```cpp
// default constructor
Date::Date()
    : day(1), month(1), year(2000)
{
}
```

This is the only definition of the default constructor in this file. If the constructor is also defined in the `Date.h` file, you should remove it from there. However, since the `Date.h` file is read-only, you'll need to do this yourself.

If the constructor is not defined in the `Date.h` file, then there must be another definition of the default constructor in the `Date.cpp` file. In that case, you should remove the duplicate definition.

If you're still having trouble, please provide the content of the `Date.h` file or any other files that might contain a definition of the `Date::Date()` constructor.

USER: I added these *read-write* files: Date.h

ASSISTANT: Great! Now that the `Date.h` file is available for editing, we can address the issue of the redefinition of the `Date::Date()` constructor.

Looking at the `Date.h` file, we can see that the default constructor is indeed defined in the header file:

```cpp
// default constructor
Date() : day(1), month(1), year(2000) {}
```

And it is also defined in the `Date.cpp` file:

```cpp
// default constructor
Date::Date()
    : day(1), month(1), year(2000)
{
}
```

This is causing the redefinition error. To fix this, we should remove the definition of the default constructor from the `Date.h` file and keep it only in the `Date.cpp` file. Here is the proposed change:

```cpp
Date.h
<<<<<<< ORIGINAL
// default constructor
Date() : day(1), month(1), year(2000) {}
=======
// default constructor
Date();
>>>>>>> UPDATED
```

This change declares the default constructor in the `Date.h` file but does not define it. The definition remains in the `Date.cpp` file. This should resolve the redefinition error.

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[1ecd03fc58...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/1ecd03fc587180931e35a5485f987eb16966020b)
#### Monday 2023-08-07 13:00:51 by SkyratBot

[MIRROR] Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes [MDB IGNORE] (#22787)

* Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

* Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes

---------

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [snakemake/snakemake](https://github.com/snakemake/snakemake)@[c9eaa4e12e...](https://github.com/snakemake/snakemake/commit/c9eaa4e12e4a348f93e5ea5793faaec1fd547fac)
#### Monday 2023-08-07 13:00:53 by Vanessasaurus

feat: support for external executor plugins (#2305)

Hi @johanneskoester! :wave: As we chat about in a thread somewhere, I
think it would be really powerful to allow for installing (and
discovering) external plugins to Snakemake. Specifically for the Flux
Operator, I have easily three designs I'm testing, and it's not really
appropriate to add them proper to snakemake - but I believe the
developer user should be empowered to flexibly add/remove and test them
out.

This pull request is first try demo of how snakemake could allow
external executor plugins. I say "first try" because it's the first time
I've experimented with plugins, and I tried to choose a design that
optimizes simplicity and flexibility without requiring external
packages, or specific features of setuptools or similar (that are likely
to change). The basic design here uses pkgutil to discover
snakemake_executor_* plugins, and then provides them to the client (to
add arguments) and scheduler to select using one with `--executor`.

I've written up an entire tutorial and the basic design in this early
prototype, which is basically the current Flux integration as a plugin!
https://github.com/snakemake/snakemake-executor-flux. The user would
basically do:

```bash
# Assuming this was released on pypi (it's not yet)
$ pip install snakemake-executor-flux

# Run the workflow using the flux custom executor
$ snakemake --jobs 1 --executor flux
```
I've designed it so that plugins are validated only when chosen, and
each plugin can add or otherwise customize the parser, and then (after
parsing) further tweak the args if chosen. Then in scheduler.py, we
simply look if the user selected a plugin, and call the main executor
(and local_executor) classes if this is the case.

The one hard piece is having a flexible way to pass forward all those
custom arguments. The current snakemake design has basically a custom
boolean for every executor hard coded (e.g., `--flux` or `--slurm`) and
while we don't want to blow that up, I'm worried moving forward passing
all these custom namespaced arguments through the init, workflow,
scheduler/dag, is going to get very messy. So the approach here is a
suggested way to handle the expanding space of additional executors by
way of passing forward full args, and then allowing the plugins to
customize the parser before or after. If we were to, for example, turn
current executors into plugins (something I expect we might want to do
for the Google Life Sciences API that is going to be deprecated in favor
of batch) we could write out a more hardened spec - some configuration
class that is passed from the argument parser through the executor and
through execution (instead of all the one off arguments).

Anyway - this is just a first shot and I'm hoping to start some
discussion! This is a totally separate thing from TBA work with Google
Batch - this is something that I've wanted to try for a while as I've
wanted to add more executors and have seen the executor space exploding.
:laughing: I haven't written tests or updated any docs yet pending our
discussion!

### QC

* [ ] The PR contains a test case for the changes or the changes are
already covered by an existing test case.
* [ ] The documentation (`docs/`) is updated to reflect the changes or
this is not necessary (e.g. if the change does neither modify the
language nor the behavior or functionalities of Snakemake).

---------

Signed-off-by: vsoch <vsoch@users.noreply.github.com>
Co-authored-by: vsoch <vsoch@users.noreply.github.com>
Co-authored-by: Johannes Köster <johannes.koester@tu-dortmund.de>
Co-authored-by: Johannes Köster <johannes.koester@uni-due.de>

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[62ab5e77f4...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/62ab5e77f44af5f0c118038233e138b85fe4906b)
#### Monday 2023-08-07 13:32:50 by SkyratBot

[MIRROR] Refactors Slaughter/Laughter Demons into Basic Mobs [MDB IGNORE] (#22801)

* Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

## About The Pull Request

On the tin, the former "imp" is now refactored into basic mob code. Very
simple since these are only meant to be controlled by players, and all
of their stuff was on Signal Handlers and Cooldown Actions anyways. Just
lessens the amount of stupidity.

Did you know that we were trying to make demons spawn in a `pop`'d cat
named "Laughter"? Embedded in the list? I've literally never seen this
cat, so I'm under heavy suspicion that the code we were using was broken
for the longest time (or may have never worked), and we now instead just
do it a much more sane way of having a cat spawn on our demise.

## Why It's Good For The Game

Cleaner code! Less simple mob jank to deal with. Trims down the list of
simple animals to refactor. No more duplicated code that we were already
doing on parent! It's so good man literally everything was seamless with
a bit of retooling and tinkering. The typepath is also no longer `imp`,
it's actually `demon`, which I'm happy with because there's no other
demons to have it be confused with anymore.

We were also doing copypasta on both the demon spawner bottle and the
demon spawning event so I also just unified that into the mob. I also
reorganized the sprites to be a bit clearer and match their new
nomenclature

## Changelog
:cl:
refactor: Slaughter and Laughter Demons have been refactored, please
place an issue report for any unexpected things/hitches.
fix: Laughter Demons should now actually drop a kitten.
/:cl:

* Refactors Slaughter/Laughter Demons into Basic Mobs

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [xenomacabre/VilesMods](https://github.com/xenomacabre/VilesMods)@[3e4c88f501...](https://github.com/xenomacabre/VilesMods/commit/3e4c88f501d84c7edd7e78e45ddd5812cc1e0a75)
#### Monday 2023-08-07 16:12:54 by Vile

Vile's Mods Update: Aug 7, 2023

OPEN THE WINDOWS
-Window walls no longer cover floor, so you can build floors under them now

AMUSE BOUCHE
-Increase glow radii of hearths
!!!MAKE SURE TO CHECK YOUR WORK TAB TO UPDATE THE FOLLOWING!!!
-Workgiver added: Work at hearth. This is so you can specify non-food jobs at a hearth such as candlemaking.
-Kitchen table is now removed from "butchering", so you can differentiate jobs between butchering and other kithen table bills if you want.

HARDCORE RENOVATION
-Increased cost of service counter and bar
-New Barricade texture

HELL BENT FOR LEATHER TANNING
-Renamed some leathers and added grades to the end of the names. For example D- is a poor leather and B is a decent leather. This is experimental and subject to change after some testing and your feedback.
-Dying vat rotates correctly
-Fixed cured/uncured tags nesting
Leather thingDef changes:
    -Upholstery leather (brown) is now called Upholstery leather, oxblood
    -added Embossed leather, oxblood
    -Embossed leather (black) is now called simply Patent Leather (still has same stats as other embossed leathers)
    -top-grain leather is now called "unplolished leather"
-Shortened some recipe names to make them easier to read
-Genuine and bonded leather use fewer ingredients/more efficient
-full-grain leather recipes are now half as efficient
-Big birds drop fewer hides
-Bark is now removed at chopping spot/block
-Added thingCategories for leathers so you can more easily customize stockpiles and recipes
-Some adjustment to leather colors - fixed soft leather color bug
-Added custom textures for leather defs

MATERIALS SCIENCE
-Chlorine/lye now more efficient to make
-Teflon uses crushed stone instead of flux for now (considering adding fluorospar, but not ready to go there just yet)
-Coin minting/melting unlocked early game
-Galena can be smelted early game
-Magnetite smelting now more efficient
-Can smelt titanomagnetite at blast furnace now which gets you lots of iron, but you don't get the titanium.
-fixed aluminium dooropen speed
-Adjusted ore commonality:
    -Sphalerite much more common on surface and deep drilling
    -Silver no longer found deep minable (get it from galena or melt coins)
    -Titanomagnetite can be found deep mining, but very rare
    -deep cassiterite less common
    -deep glow/coldstone less common
    -galena more common
    -Scheelite more common
-Adjusted some fabric colors
-Vinyl faux leather severely nerfed
-Granite and Marble have beauty offset for walls etc

VILE's TWEAKS
-Added some offset perks to some ideology clothing
-Removed pointless gendering of some apparel
-Rockhound background gives stonecutting bonus
-Shoes have better movespeed, caligae boots worse
-More fucking around with pawn badges

WOOD YOU PLEASE
-Increased efficiency of higher-tier candles and lanterns
-renamed firewoods to be easier to read in small menus
-Door open speed is now related to how dense the wood is. REMINDER: Plank recipes are listed from lightest (cecropia/pine) to heaviest (as long as you have alphabetical sorting turned off)
-Added note to sawmill description about smithing workspeed
-Patched heating log stove to be less powerful but much more fuel efficient

WORK TAB FOR BIG FONTS
-Prep meal is now called "kitchen table"

---
## [daplcor/KU](https://github.com/daplcor/KU)@[77a09e5ffb...](https://github.com/daplcor/KU/commit/77a09e5ffbf6d1ea7f7df6d8a0e251bb830a712f)
#### Monday 2023-08-07 16:18:15 by AmirDapl

headache

Might have made my repl too stupid, but I can't for the life of me mint with collection-policy.  Collections work fine, but here we are.  need to figure out why ledger isn't finding tokens but token-policy sees it.

---
## [ma44/mojave-sun-13](https://github.com/ma44/mojave-sun-13)@[b2f0f35f3a...](https://github.com/ma44/mojave-sun-13/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Monday 2023-08-07 16:39:48 by EdwardNashton

Speed, Money and Faith: Updating an areas of Town. (#2286)

* Update TGS DMAPI

* Speed, Money and Faith: Updating an areas of Town.

Added a Church with a graveyard area (that currently empty because we have no tombs).

Remade one quarter into 4 different shops: Liquor, Pharmacy, Gun Shop, General Store.

Remade old shitty Library into Biker's Club.

Remade a Dime's Radio Station (by his permission)

Fixed a small area issue on a top z-level of Car Jankyard.

* Fixes up a bunch of stuff :)

* additional minority fixes

---------

Co-authored-by: tgstation-server <tgstation-server@users.noreply.github.com>
Co-authored-by: Edward Nashton <eddienigma48@gmail.com>
Co-authored-by: Professor Popoff <omniderpectional@gmail.com>

---
## [mamedev/mame](https://github.com/mamedev/mame)@[e97630981c...](https://github.com/mamedev/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Monday 2023-08-07 17:43:14 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [nifranizam/New-Repo](https://github.com/nifranizam/New-Repo)@[7213ed1f04...](https://github.com/nifranizam/New-Repo/commit/7213ed1f04d28cee28628f309c743448255d8b17)
#### Monday 2023-08-07 19:05:41 by Fathima Nifra

Add files via upload

Hi!!
Portfolio Webpage - Favorite Place Sri lanka
Description
Welcome to my portfolio webpage, "Beauty Of Srilanka"! This single-page website showcases my love and appreciation for the beauty of nature through photography and achievements related to different wonders of srilanka. The webpage aims to create a visually appealing and interactive experience for visitors, providing insights into my passion for the nature.
The theme of this portfolio webpage revolves around the beauty of srilanka. As an avid nature enthusiast and photographer, I have curated a collection of stunning photographs capturing various landscapes, wildlife, and natural phenomena. Additionally, I have included a section highlighting my achievements and experiences in nature-related activities and projects. The overall theme aims to immerse visitors in the breathtaking landscapes and the importance of conservation and appreciation for nature's diversity.
I hope you enjoy exploring the beauty of srilanka through my photography and achievements showcased on this portfolio webpage. As you scroll through the different sections and interact with the elements, I invite you to immerse yourself in the beauty and diversity of the natural world. Feel free to contact me through the provided contact form if you have any inquiries or would like to discuss any nature-related projects or collaborations.

---
## [YellowSegment/Game](https://github.com/YellowSegment/Game)@[e6cafba75c...](https://github.com/YellowSegment/Game/commit/e6cafba75cc4ebd3b29227cc35166f0684aec444)
#### Monday 2023-08-07 19:29:14 by freight3092

I FREAKING CAMED

YO YO MAMA PEED HER LITTLE SLIT DUDE HAHA GET FUCKING SHIT ON YOU FUCKING NERD

---
## [Kreeldor/awesome-docker](https://github.com/Kreeldor/awesome-docker)@[3164d6df94...](https://github.com/Kreeldor/awesome-docker/commit/3164d6df94f60d7d3d11629241c111ed416eb8eb)
#### Monday 2023-08-07 19:58:47 by Derek Lee

Add Kurtosis to list of testing tools (#1063)

* Add Kurtosis to list of testing tools

Hey team! We'd like to add Kurtosis to the list of testing tools. 

*What is Kurtosis?* Kurtosis is a built system for multi-(docker)container test environments. 
*What is Kurtosis for?* Kurtosis is for engineers who dev against large distributed systems/applications and who experience pain when trying to configure multi (Docker) container environments for their testing workflows. 

Kurtosis can be used locally without the need to sign up and is free-forever under a source-available license (BSL). 

We have:
- Linked out to our Github: https://github.com/kurtosis-tech/kurtosis
- [A README on our GIthub](https://github.com/kurtosis-tech/kurtosis#readme)
- Content about how to setup/install the project (in our [Github README](https://github.com/kurtosis-tech/kurtosis#to-start-using-kurtosis) and on our [docs](https://docs.kurtosis.com/install)),
- Lots of great examples on: [Github](https://github.com/kurtosis-tech/awesome-kurtosis#awesome-kurtosis-) and in our [docs](https://docs.kurtosis.com/). 

I followed the [Quality Standards](https://github.com/veggiemonk/awesome-docker/blob/master/.github/CONTRIBUTING.md#quality-standards) you guys wrote, but please let me know if you've got any questions about Kurtosis or if we missed something!

Thanks

* add "composable" to description

---
## [SPT-Mod-Dev/SPT-Mod-Dev](https://github.com/SPT-Mod-Dev/SPT-Mod-Dev)@[5731420c13...](https://github.com/SPT-Mod-Dev/SPT-Mod-Dev/commit/5731420c136c2d4ca8ca7e5f21bb6f8a972f53d2)
#### Monday 2023-08-07 20:12:09 by Jonah Kaplan

Merge pull request #45 from SPT-Mod-Dev/Romania-Focus-Tree

Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead

Well, the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb

So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go (GO!)
You'll never shine if you don't glow

Hey, now, you're an all-star, get your game on, go play
Hey, now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold

It's a cool place and they say it gets colder
You're bundled up now wait 'til you get older
But the meteor man beg to differ
Judging by the hole in the satellite picture

The ice we skate is getting pretty thin
The water's getting warm so you might as well swim
My world's on fire. How about yours?
That's the way I like it and I'll never get bored

Hey, now, you're an all-star, get your game on, go play
Hey, now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold

Go for the moon
Go for the moon
Go for the moon
Go for the moon

Hey, now, you're an all-star, get your game on, go play
Hey, now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars

Somebody once asked could I spare some change for gas
I need to get myself away from this place
I said yep, what a concept
I could use a little fuel myself
And we could all use a little change

Well, the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb

So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go
You'll never shine if you don't glow

Hey, now, you're an all-star, get your game on, go play
Hey, now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold

And all that glitters is gold
Only shooting stars break the mold

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3dc75f84f2...](https://github.com/tgstation/tgstation/commit/3dc75f84f2eebc388c7f698284d77df4d8cf8fdf)
#### Monday 2023-08-07 20:30:16 by YakumoChen

Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!) (#77174)

## About The Pull Request

Authored with help and love from @Thalpy 

I scream for ice cream!!


![image](https://github.com/tgstation/tgstation/assets/10399117/db1e559b-7dab-499b-a076-8f12748ba2e8)

Introduces many new flavours of ice cream:
-Caramel
-Banana
-Lemon Sorbet
-Orange Creamsicle
-Peach (Limited Edition!)
-Cherry chip
-Korta Vanilla (made with lizard-friendly ingredients!)


![image](https://github.com/tgstation/tgstation/assets/10399117/99a87615-f55c-49be-8caf-2b1ac4c7f03f)

Korta Cones! Now too can Nanotrasen's sanitation staff enjoy the wonders
of ice cream!
You can also substitute custom ice cream flavours with korta milk!
Finally, the meaty ice cream lactose-intolerants asked for is in reach!

## Why It's Good For The Game

I always thought the ice cream vat could use more flavours. The custom
flavour besides, it isn't as intuitive to rename the cone and the added
variety is good. The lack of a banana flavour already was questionable.
All the ice cream flavours used a selection of five sprites, now it's
just one sprite and better supporting more additions.
Some of the flavours don't use milk! You can't do this with the custom
flavour, making it slightly more interesting.

## Changelog
:cl: YakumoChen, Thalpy
add: Chen And Garry's Ice Cream is proud to debut a wide selection of
cool new frozen treat flavours on a space station near you!
add: Chen And Garry's Ice Cream revolutionary Korta Cones allow our ice
cream vendors to profit off the lizard demographic like never before!
code: Ice cream flavours now are all greyscaled similarly to GAGs
/:cl:

---
## [taparkins/localdev_setup](https://github.com/taparkins/localdev_setup)@[2818f32712...](https://github.com/taparkins/localdev_setup/commit/2818f3271222c7454df7fb0e9de02be8c90af16e)
#### Monday 2023-08-07 20:37:30 by Talia Parkinson

Checkout vimrc from specified commit, rather than most recent

 - This guy added a BUNCH of shit in the last year or so, and the
   plugins have gotten borderline unusable as a consequence. PLUS it
   installed CoPilot without my realizing it, which is shady as fuck
   tbph. This is doing a shallow clone from a specified hash until I get
   around to forking the repo to avoid this happening in the future.

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[171b1478f9...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Monday 2023-08-07 20:53:59 by vampirebat74

Limbus Company E.G.O dump (#1062)

* Adds roseate desire

roseate sfx

datums

weapons

add aedd

sprite adjustments

unfucks suits

new sfx

name fix

aaaa

adds capote

adds sloshing

farmwatch

farmwatch suit

stuff

farmwatch stuff

capote inhands

red sheet finished

sloshing gift

linters

Stuff

stuff

fixes shit

stuff

weapon code cleanup

spicebush finished

removes the heal

code fix

stuff

removes reference

farmwatch hat

new vfx

requested changes

* block duration

---------

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[37d9d899d0...](https://github.com/newstools/2023-new-york-post/commit/37d9d899d016d6dd49d862213ca4a36801f68f6e)
#### Monday 2023-08-07 21:10:12 by Billy Einkamerer

Created Text For URL [nypost.com/2023/08/07/i-used-ai-to-catch-my-boyfriend-cheating-heres-how-you-can-too/]

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[2b80714afa...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/2b80714afa150d6f9e335f8ae68ef84444d52506)
#### Monday 2023-08-07 21:14:56 by SkyratBot

[MIRROR] Base Female sprite tweaks [MDB IGNORE] (#22924)

* Base Female sprite tweaks (#77407)

## About The Pull Request

ASS STUFF HAS BEEN REMOVED BUT I STILL HATE IT

This PR tones down the proportions of the female base sprites, as
currently they have about SIX extra pixels on the ass and a random pixel
missing from the neck, which breaks some hairstyles & makes the neck
look quite stupid.
It also adds a couple pixels to the male one because theirs was so
stupidly SMALL it looked like they had no tailbone (still does, kind
of).

Here is the current sprite

![image](https://github.com/tgstation/tgstation/assets/81964183/1bf22dd7-2b06-4632-8617-b89b3b1c8d2c)
& new sprite (only neck pixel removed)

![image](https://github.com/tgstation/tgstation/assets/81964183/b1228e01-23e0-4508-86a6-bc8e73b0fcd0)

## Why It's Good For The Game

Fixes some hairs

![image](https://github.com/tgstation/tgstation/assets/81964183/3b293cf9-2661-4358-a327-2882acb93067)

## Changelog

:cl:
image: fixes weird inconsistency on the neck and butt of the female base
sprite
/:cl:

* Base Female sprite tweaks

---------

Co-authored-by: Sheits <81964183+Sheits@users.noreply.github.com>

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[86b58866bc...](https://github.com/AnywayFarus/Skyrat-tg/commit/86b58866bc0e3e8a1ee2e511328b6a76687b6e77)
#### Monday 2023-08-07 21:33:16 by SkyratBot

[MIRROR] Science Resprite! (With Sovl!) [MDB IGNORE] (#22861)

* Science Resprite! (With Sovl!) (#77314)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
What a crusty department. These outfits are...
Something.

![image](https://github.com/tgstation/tgstation/assets/76465278/63fe13cf-bcbf-42c2-a22c-c868ae49a72c)

How old are these now? I'm pretty sure they're unchanged since when I
started playing years ago on other servers.... besides the RD Turtleneck
and Roboticist suit of course. But they still did have some touch-ups to
be made...

Regardless, I think this department deserves a little love!
I've tried to stay true as I could to their current designs; this isn't
a re-**_design_**, just a re-sprite. I used the base jumpsuit design
from Medbay for most of these since it's the most modern suit that fit
with the colored-spots style.

![image](https://github.com/tgstation/tgstation/assets/76465278/ef7ff5b0-f0e3-481a-9ed4-ba830e3ee0c3)

All of them have been touched up, and the RD's "alt" is now a subtype of
the buttondown so it can easily inherit any sprite updates in the
future.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
These deserved some touch-ups and modernization, and while I'm not keen
on entirely reworking them I figured I could at the least give them the
update the Science Team deserves.

(The buttondown has an outdated obj sprite in this image! It's since
been made smaller and more folded)
Also labcoats for comparison

![dreamseeker_Ds8gZLKoGE](https://github.com/tgstation/tgstation/assets/76465278/4da60512-b813-4260-b3fe-5c71b60cec81)

![dreamseeker_C9DpFWWOS7](https://github.com/tgstation/tgstation/assets/76465278/1de55f4c-2eaa-480b-811f-aaa5832eeceb)

![dreamseeker_02d3d7b6aj](https://github.com/tgstation/tgstation/assets/76465278/b1f40d03-c9b8-4f6b-bc54-516b11a7bfb3)

![dreamseeker_DwJGDwbUf1](https://github.com/tgstation/tgstation/assets/76465278/20f97a5e-42ab-4fe0-8eae-4ac6ed24ead4)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
image: resprited the entirety of RnD! Genetics, Robotics, the RD, and
the Science Team themselves will enjoy the fresh new looks but same
great taste! No, wait, great STYLE! Don't eat these, they're covered in
chemicals.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* Science Resprite! (With Sovl!)

* Update vending.dm

---------

Co-authored-by: OrionTheFox <76465278+OrionTheFox@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [ruhee/show-archive](https://github.com/ruhee/show-archive)@[f009c366bc...](https://github.com/ruhee/show-archive/commit/f009c366bce83f6f792a5e0fc8c1062fe71ab368)
#### Monday 2023-08-07 21:34:54 by Ruhee Dewji

A ridiculously lovely day

Almost cried when Hiroki read that poem. Rae made everyone laugh constantly. Saw L, A&J&baby, went with C, had a wonderful time.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[08f720517b...](https://github.com/Buildstarted/linksfordevs/commit/08f720517b645afcc5cc8bbd422084474926b9c6)
#### Monday 2023-08-07 22:10:20 by Ben Dornis

Updating: 8/7/2023 10:00:00 PM

 1. Added: Notes on exit interviews
    (https://rednafi.com/zephyr/notes_on_exit_interviews/)
 2. Added: Removing Randomness with LLDB
    (https://bryce.co/lldb-remove-randomness/)
 3. Added: My (Painful) Experience With Ubiquiti As A DevOps Engineer | tyzbit.blog
    (https://tyzbit.blog/my-painful-experience-with-ubiquiti-as-a-devops-engineer)
 4. Added: How does a CTO know when they need a coach?
    (https://blog.mocoso.co.uk/2023/06/26/how-does-a-cto-know-when-they-need-a-coach/)
 5. Added: Writing a recursive descent parser in Bash · m10k
    (https://m10k.eu/2023/07/29/pkgex-parser.html)
 6. Added: Being a Disciplined Person In an Undisciplined World
    (https://durmonski.com/self-improvement/disciplined-person/)
 7. Added: Tradeoffs in Testing
    (https://dillonshook.com/tradeoffs-in-testing/)
 8. Added: The Central Binomial Coefficient and Laplace's Method
    (https://cgad.ski/blog/the-central-binomial-coefficient-and-laplaces-method.html)
 9. Added: The universe is (probably) not a simulation
    (https://blog.georgovassilis.com/2023/08/07/the-universe-is-probably-not-a-simulation/)
10. Added: "Make something idiot-proof, the world will show you a better idiot"
    (https://www.izoukhai.com/blog/make-something-idiot-proof-the-world-will-show-you-a-better-idiot)
11. Added: Humble Tech Book Bundle: Math for Programmers 2023 by Manning
    (https://www.humblebundle.com/books/math-for-programmers-2023-manning-books)
12. Added: Hacking is child's play - SQL injection with Havij by 3 year old
    (https://youtube.com/watch?v=Fp47G4MQFvA)
13. Added: 06 We Speak: IBM MQ
    (https://youtu.be/fv-ag8h5lYA)
14. Added: MassTransit Bus Stop - Request Response via Messaging (RPC)
    (https://youtube.com/watch?v=TWWVHWlBGIs)
15. Added: Disinterest.
    (https://www.baldurbjarnason.com/2023/disinterest/)
16. Added: Bike: Row Types
    (https://www.hogbaysoftware.com/posts/bike-row-types/)
17. Added: Growth Experiment: How Much Traffic Unsplash Drives to Your Website - Fresh van Root
    (https://freshvanroot.com/blog/how-much-traffic-unsplash-drives-website/)
18. Added: Layoffs and its impact
    (https://aravind.dev/layoff/)
19. Added: The Concretude of the Cloud
    (https://notes.ghed.in/cloud-computing-water-consumption-90e7e46f5d54)

Generation took: 00:10:08.3053764

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[d875610098...](https://github.com/lizardqueenlexi/orbstation/commit/d875610098a1259a5112d4a0e5afc0b7bd32ff6d)
#### Monday 2023-08-07 22:17:52 by Rhials

[NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**


https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

---
## [meedan/check-api](https://github.com/meedan/check-api)@[dc890de6e2...](https://github.com/meedan/check-api/commit/dc890de6e23208a4db9e99f8e28e665b8ffc8a7e)
#### Monday 2023-08-07 22:36:14 by Christa Hartsock

Update GraphQL to use class-based SDK 🫠

This commit upgrades us to GraphQL 1.11.10, from 1.9.21, and begins using the new class-based SDK from the previous .define syntax.Though this change isn't supposed to be required until GraphQL 2.0, I found in practice that we couldn't upgrade to the minimum version needed for Ruby 3.0 (1.11.7) without doing it. 

**What I did**

With the new GraphQL DSL, we are able to use Ruby class composition, which includes inheritance from base classes and including modules to get specific functionality.

I tried to create some useful abstract base classes that borrowed heavily from our previous GraphQL CRUD generator. We had a lot of carveouts in the generator for specific classes (specifically in .define_parent_returns or the generator functions for what wanted to be classes), and I tried to eliminate these and move them to explicit declarations in classes now that we have the ability to do that (yay library enabling composition!)

As much as possible, I tried to move us toward declaring things explicitly to reduce my and hopefully future us's confusion rather than using metaprogramming or extracting abstract functions. Going forward, I think we should only extract methods or classes where there is shared functionality for a type or mutation, and rely on explicit declaration or modules for attributes that differ based on the underlying class we're modifying.

There is some kind of tricky metaprogramming and code in the mutation base classes, because of problems I ran into with inheritance and other things. I also hope that now that the pattern is set up we won't have to touch them too much, and can instead rely on configuring their child classes.

**Some gotchas I ran into / things of note**

Our API uses a mix of camel-case and snake-case. The new GraphQL library wants to convert everything to camelcase, which will break our API. I've tried where possible to default attributes to snakecase (changing this in the base Type), but it's not possible for everything - specifically when we set fields and arguments on mutation classes. To override the default behavior of camelcaseing, we have to manually set camelize: false on any field or argument that has an underscore in mutation classes.

* GraphQL Ruby now has a new base mutation class that we could opt into if we want, but it changes the way the API would look - of note is removing the input: key from request bodies, not allowing direct setting of inputs and fields on the input type in the mutation class (I think), and not automatically injecting the global ID in the response. To maintain our old behavior, we have to descend from GraphQL::Schema::RelayClassicMutation rather than GraphQL::Schema::Mutation, which I've done in Mutations::BaseMutation (and all descendent classes we expect to use for our mutations: Mutations::CreateMutation, Mutations::UpdateMutation, Mutations::DestroyMutation, Mutations::BulkUpdateMutation, Mutations::BulkDestroyMutation)
* GraphQL schema now gets generated at runtime. When our tests run they only start the application a maximum of once per file. This means that the previous approach we used to create and delete annotation types, which the GraphQL schema relies on to be generated correctly, and reloading the schema as necessary does not work - as a result we're now calling  TestDynamicAnnotationTables.load! before GraphQL controller tests, which loads the existing annotation tables generated in development into test fresh each time.
* Our QueryType returns an always null ID field. This is because the frontend was requesting it even though we don't use it. I don't know why, but this fixed it. So, I added it and moved on.

Resources:

Here's the migration guide I leaned on heavily: https://imaharu.github.io/graphql-ruby-doc-ja/schema/class_based_api.html#compatibility--migration-overview. It's still missing a lot, but may help if you want to understand changes in the API.

Also, the new API is described in the GraphQL ruby docs: https://graphql-ruby.org/guides

**Some additional things that appear in this commit, that may be of note in future**

* Manually specify resolve functions for missing methods

We sometimes automatically generate getters for attributes stored
as a hash (eg get_slack_webhook, get_languages) but since we rely
on method_missing to do so, GraphQL doesn't detect those methods as
being valid because it checks for their validity using
Model.respond_to(:method_name), which returns false even though
Model.method_name returns a legitimate value. To get around this,
we can manually create resolve methods with the attribute name
that just call into the model.

* Allow batch nesting

This is now allowed in GraphQL batch, and the error we were previously
catching no longer exists.

https://github.com/Shopify/graphql-batch/issues/70

* Properly implement nodes and interfaces, and support OpenStructs

OpenStructs break the class hierarchy, so we need more explicit
handling to support our current use case. Our id_from_object now
calls down into the OpenStruct :type method, like we were doing before

* Fix edge setting in most mutation classes

I think there was a naming conflict (name -> obj_name) causing things
to go totally wonky.

* Fix tests that depend on a specific schema

Certain tests require annotation types to be in the database before loading
the schema. We can't reload the schema easily in test environment. Given that this
data is actually static in practice (and hardcoded into the GraphQL schema we
generate), we might want to consider preloading it into the database rather than
creating it in individual tests. For now, we just create the dynamic annotations in
the test setup for the controller test file the test is run within.

Try to avoid altering the other tests for now, even though we'll need
to eventually. Begins loading in DynamicAnnotation stuff from a dump
of our local (and QA) database after a fresh build so that we can have
a consistent GraphQL schema. The new GraphQL interpreter only creates the
schema at runtime, which means we build it once per test run. As a result,
we need to have all of our DynamicAnnotation annotation types and fields
in place before we start the app to run tests.

This sidesteps fixing the dynamic annotation stuff for the rest of the
app, since that's a big one.

* Change flaking tests to use createDynamic instead of db-gen mutation

Also adds :action to Dynamic mutations to support using createDynamic
for createDynamicReportDesign, which requires the action attribute
in certain circumstances. Kind of a hack for tests to pass, since we're
having problems loading the schema from database consistently

CV2-3094

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[1db23d1753...](https://github.com/Offroaders123/NBTify/commit/1db23d17535ef867f1d1007650dc9754e898179f)
#### Monday 2023-08-07 23:22:21 by Offroaders123

Optional CompoundTag Keys

Brought over from the test 'Primitive Wrapper Objects: Take Two' branch, now `undefined` is an acceptable entry on `CompoundTag` key/value pairs!

This change also makes the default `RootTag` return type for various function calls more usable, but I'm also going to roll back that test in this commit. Having `RootTag` as the default return type makes sense in terms of what it is at the type level, but it isn't as user-friendly when doing things with it specifically. So the default return type will once again be `any`, which feels more synonymous with how you would work with `JSON.parse()` or `Response.prototype.json()`, which NBTify is semi-trying to mirror in some aspects. #32

I think I need to rework the unsafe/safe `ListTag` and `CompoundTag` handling again, as now with having `undefined` being an ok value at the type level, there needs to be a better line of distinction of where it is present in the `CompoundTag` type when it is passing through the library. It gets removed when passed through `fromCompoundUnsafe()`, but the return type `CompoundTag` still lists it as a possible value for keys of `CompoundTag`. So for `undefined` at least, I need to at minimum move the handling for that into places where `CompoundTag`s are traversed directly, and put `undefined` handling there, since it is allowed on the type now, unlike before.

*Stringify and Write modules use '!' to counteract this inconsistency at the moment*

Oh yeah, and `NBTData` still requires a first parameter generic, I'm not going to revert that one, as it does help a lot with having the user be more explicit about their types when possible. They have to choose whether or not to provide their own type, or just use `any` if they don't know their types yet. If functions could require generics too, then I wouldn't default the return types to `any`, as requiring a generic would be the best use case for the UX of the return types. But I understand why that doesn't make as much sense, so it's ok :)

Got lots of music the last few days! They have all been OUTSTANDING!!

Haken - Affinity 🕹️
Devin Townsend - Lightwork 🐙
Cleft - Whale Bone 🐋
Mike Keneally - Inkling (More from the Scambot 2 Sessions) 🦂🦂
Devin Townsend - Silent Night ❄️

---

