## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-02](docs/good-messages/2023/2023-11-02.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,448,199 were push events containing 3,749,920 commit messages that amount to 293,540,786 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 78 messages:


## [oilshell/oil](https://github.com/oilshell/oil)@[e8a11fd16e...](https://github.com/oilshell/oil/commit/e8a11fd16e1244443c988c6015feb8eddc8d5cf0)
#### Thursday 2023-11-02 00:02:12 by Andy C

[ysh breaking] s->trim(), s->startsWith()

camelCase: startswith() -> startsWith()

See Zulip for rationale on s->trim() over s->strip().

We're not implementing all of Python's API, and there are a number of
cosmetic reasons for trim().

Settled on this API:

   trim()
   trimLeft()
   trimRight()

   trimPrefix()
   trimSuffix()

Though to be honest I wonder if the "speed bump" with Python will be
annoying.  It's not that hard for us to accept 'startswith' as well.

Although I want one way to do it, when methods in Python/JS differ by
CASE ONLY, it could be an argument for having both names.

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[9e18c6575a...](https://github.com/necromanceranne/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Thursday 2023-11-02 00:08:12 by lizardqueenlexi

Basic Pirate NPCs (#79284)

## About The Pull Request

Converts hostile pirate NPCs to basic mobs - specifically, a subtype of
trooper. As their behavior is not meaningfully distinct from other
troopers, this conversion mostly just sticks them on the existing AI
behavior while keeping the rest the same.

Pirates do have one new thing going for them, though, to differentiate
them from other troopers. They use the new **plundering attacks**
component, which means that every time they land a melee attack, they
steal money from the bank account of whoever they hit. This requires the
target to be wearing an ID with a linked bank account, so it's not the
hardest thing in the world to hide your money from them - but it's still
something to be wary of! If killed, any mob with this component will
drop everything they've stolen in a convenient holochip.
## Why It's Good For The Game

Takes down 5 more simplemobs, and (I think) converts the last remaining
trooper-type enemy to be a basic trooper. (It's possible there's more
I've forgotten that could use the same AI, though.)

The money-stealing behavior is mostly good because I think it's funny,
but it also makes the pirates something a little distinct from "yet
another mob that runs at you and punches you until you die". They still
do that, but now there's a little twist! This can be placed on other
mobs too, if we want to make any other sorts of thieves or brigands.
## Changelog
:cl:
refactor: Pirate NPCs now use the basic mob framework. They'll be a
little smarter in combat, and if you're wearing your ID they'll siphon
your bank account with every melee attack! Beware! Please report any
bugs.
/:cl:

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[d1ad9b6658...](https://github.com/lizardqueenlexi/orbstation/commit/d1ad9b665823708c3ae651eb9729023968e7feaf)
#### Thursday 2023-11-02 00:19:44 by necromanceranne

Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone (#79232)

## About The Pull Request

Brings the CQC kit back down to the same price range of 14 TC (it's 1
more than before weapon kits). It feels like currently that CQC is
overpriced, even with the stealth box coming along with it, and by
comparison the energy sword and shield got a huge value increase by
combining the two. They're both melee styles and also equally difficult
play styles. It isn't really necessary to make one more expensive than
the other. Also now comes with syndicate smokes. It's a whatever change,
ops get these for free on the base.

Adds a core gear kit in the weapon category. This kit comes with a
doormag, a freedom implant, stimpack and c-4 charge. All of these are
items almost every nukie buys if they want to succeed, so let's inform
newer players by putting it RIGHT on top of the list. This isn't at any
discount, this is mostly to help inform players what items help make you
successful.

Hat stabilizers are now a part of every syndicate modsuit for FREE. It
comes built in, can't be removed, and has no complexity cost. Now
everyone can wear their wacky hats as they operate.

## Why It's Good For The Game

CQC felt like it got shafted waaay too hard with the weapon case
changes. Definitely don't believe that it is punching at the same weight
as many of the other high cost weapons. So we've dropped it down a
category. 14 TC is still a large upfront cost, even if it comes bundled
with a lot of goods.

Melbert gave me the idea of a core bundle kit to help newer players and
I was really taken with that. So I added it as part of this followup.

I want people to wear their hats goddamnit, and I didn't learn my
mistake with the tool parcels. So now everyone has hat stands on their
suits. WEAR THE SOMBRERO YOU **FUCK**.

### THIS IS NOW A THREAT.

## Changelog
:cl:
balance: Operatives can once again read about the basics of CQC at a
reasonable price of 14 TC.
qol: All Syndicate MODsuits come with the potent ability to wear hats on
their helmets FOR FREE. No longer does any operative need be shamed by
their bald helmet's unhatted state when they spot the captain, in their
MODsuit, wearing a hat on their helmet. The embarrassment has resulted
in more than a few operatives prematurely detonating their implants! BUT
NO LONGER! FASHION IS YOURS!
qol: There is now a Core Gear Box, containing a few essential pieces of
gear for success as an operative. This is right at the top of the
uplink, you can't miss it! Great for those operatives just starting out,
or operatives who need all their baseline equipment NOW.
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e06c2ff40e...](https://github.com/treckstar/yolo-octo-hipster/commit/e06c2ff40eb90fb188d15814be73ecdbd75520db)
#### Thursday 2023-11-02 00:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [bryanwills/readthedocs.org](https://github.com/bryanwills/readthedocs.org)@[ea6503eb6f...](https://github.com/bryanwills/readthedocs.org/commit/ea6503eb6fbfb3eb7c77830407b05012997e3ce0)
#### Thursday 2023-11-02 00:25:02 by Anthony

Add organization view UI filters (#10847)

* Add organization view UI filters

This filters are used for the new dashboard UI, they are not API filters.

These were a challenge to create, as django-filter is really opinionated
about the way it should work, and doesn't quite agree with use cases
that need to use filtered querysets (such as limiting the field choices
to objects the organization is related to).

I went through many permutations of this code, trying to find a pattern
that was not obtuse or awful. Unfortunately, I don't quite like the
patterns here, but because all of the django-filter magic happens at the
class level instead of at instantiation time, every direction required
hacks to obtain something reasonable.

Given the use we have for filters in our UI, I wouldn't mind making
these into a more generalized filter solution.

I think I'd like to replace some of the existing filters that currently
hit the API with frontend code and replace those with proper filters
too. These are mostly the project/version listing elements.

* Add filter for organization dropdown

This replaces an API driven UI element. It's not important that these UI
filters are frontend, it was just easier than figuring out how to make
django-filter work for this use case at that time.

* Fix the team member filter yet again

* Use a custom filter field to execute filter set queryset method

* Add tests organization filter sets

* Update code comments

* A few more improvements

- Make view code nicer, use django_filters.views.FilterMixin, sort of
- Use FilterSet.is_valid() to give empty list on validation errors
- Clean up tests with standard fixtures instead

* Review updates for tests and arguments

* Rename FilterMixin -> FilterContextMixin

* Fix lint

---
## [FluffiestFloof/Delta-v-rebase](https://github.com/FluffiestFloof/Delta-v-rebase)@[19dd012857...](https://github.com/FluffiestFloof/Delta-v-rebase/commit/19dd01285769120f7c0f278cb05b4f95a7712632)
#### Thursday 2023-11-02 00:29:10 by Colin-Tel

Adds Asterisk Station (#374)

* Adds Asterisk Station

The map renderer is a bitch ass motherfucker.

* Update default.yml

added Asterisk to pool, and alphabetized the list.

* Update PostMapInitTest.cs

forgot I had to do this shit

* Update asterisk.yml

I forgot the cool role

* Update asterisk.yml

Added station maps

* Update asterisk.yml

Added JobSpawns for salvage and made some other adjustments

* Update asterisk.yml

Changes made after Velcro's review

---
## [BurgerLUA/tgstation](https://github.com/BurgerLUA/tgstation)@[517d33e6f0...](https://github.com/BurgerLUA/tgstation/commit/517d33e6f06289085d0c6015a01c3a3ce7bc22d0)
#### Thursday 2023-11-02 00:35:21 by Jacquerel

Basic blob mobs (#78520)

## About The Pull Request

I remembered today that blob code is ass, especially blob spores.
There's still a lot to improve but I cleaned up _some_ of it by
converting these mobs.
Now they use a newer framework and more signal handling as compared to
circular references.

I _expect_ the behaviour here to largely be the same as it was or
similar. I haven't added anything fancy or new.

This is a reasonably big PR but at least all of the files are small?
Everything here touched every other thing enough that it didnt make
sense to split up sorry.

Other things I did in code:
- Experimented with replacing the `mob/blob` subtype with a component.
Don't know if this is genius or stupid.
- AI subtree which just walks somewhere. We've used this behaviour a lot
but never given it its own subtree.
- Blob Spores and Zombies are two different mobs now instead of being
one mob which just changes every single one of its properties.
- Made a few living defence procs call super, because the only thing
super does was send a signal and we weren't doing that for no reason.
Also added a couple extra signals for intercepts we did not have.

## Changelog

:cl:
fix: Blob spores will respond to rallies more reliably (it won't runtime
every time they try and pathfind).
fix: Blobbernaut pain animation overlays should align with the direction
the mob is facing instead of always facing South
refactor: Blob spores, zombies, and blobbernauts now all use the basic
mob framework. They should work the same, but please report any issues.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[0d5f9907a2...](https://github.com/Zergspower/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Thursday 2023-11-02 01:05:49 by Jacquerel

Shapechange health transfer tweaks (#79009)

## About The Pull Request

Fixes #78721
This PR does a handful of things behind the scenes to increase the
consistency of shapechange health tracking.

First of all we adjust the order of operations taken when you restore
the original body. The implementation as-was would remove the status
effect midway through and null a bunch of variables we tried to continue
using. This would result in several runtimes and code failing to run,
with the upshot that untransforming upon death would leave the caster
completely alive, with the corpse of its transformed shape at its feet.
Oops.

Additionally while testing this I realised that transferring the damagew
as also kind of fucked.
We wouldn't bother to do it at _all_ if you died, which is a shame, so I
made it simply heal you instead of reviving you so we can always do it.
Then as noted in the linked issue, we were applying all transferred
damage to a single limb, which could exceed the health of the limb and
remove damage. Now we spread it around the body.

Finally, applying damage to a human using the "force" flag would often
actually apply less damage to their _health_ than expected. This is
because arms and legs contribute only 75% of their damage taken to a
mob's overall health.
Now instead of reading `health` we read `total damage` which ignores the
limb damage modifier.

The end result of this is that if you transform into a corgi, take 50%
of your health, and transform back then you will have 50% of your health
as a human.
Previously the result would be that you'd have ~63%, then transforming
into a corgi would leave you with ~63% of a corgi's health, then
transforming back into a human would leave you at about 71%... and so on
and so forth. Now it doesn't do that.

## Changelog

:cl:
fix: Dying when using (most) shapeshift spells will now kill you rather
than having you pop out of the corpse of your previous form.
fix: Damage will now be accurately carried between forms rather than
being slightly reduced upon each transformation.
/:cl:

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[157fafeaa9...](https://github.com/Jolly-66/tgstation/commit/157fafeaa95d4823c272326a37310a7017b206ef)
#### Thursday 2023-11-02 01:08:21 by lizardqueenlexi

[CI Fix] The Demonic Frost-Miner will not attack corpses. (#79294)

## About The Pull Request

Fixes #79147.

Prevents the Demonic Frost-Miner from shooting at corpses by returning
early from `OpenFire()`. Also adds the "gutted" status effect to the
corpses in its arena so it won't try to gut them.
## Why It's Good For The Game

#78826 introduced an unfortunate bug by placing corpses in the Frost
Miner's arena. There were a combination of three factors at play here:
that the Miner attacks corpses, that it happens to use colossus bolts in
its attacks, which dust corpses, and that some unfortunate quirk of life
code causes runtimes if, as far as I can tell, a life tick goes off when
a mob is at the wrong point in the dusting process. The time this
process takes happened to perfectly coincide with the Monkey Business
unit test (being the first test that takes a significant period of
time), causing it to randomly fail.

So, this fixes a flaky test that has been a pain in the ass for the last
five days, is the big thing.

Also, it can't possibly have been intended for the Miner to run around
obliterating the aesthetic corpses in its arena within the first 15
seconds of any given round. Completely ruining the mood!

I'll point out that this particular boss may have been forgotten in
#77731, which set out to make only the colossus still gib/dust you, but
even were that not the case I think it would be a bit silly for the
Miner to be busy shooting lifeless corpses when a player shows up to
challenge it, rather than standing in its scary ritual circle.
## Changelog
:cl:
fix: The Demonic Frost-Miner will no longer run around destroying the
corpses in its arena the moment the round begins.
/:cl:

---
## [cyphar/runc](https://github.com/cyphar/runc)@[96219995c3...](https://github.com/cyphar/runc/commit/96219995c338adbc6a2eddad913efa2a30dbc7b5)
#### Thursday 2023-11-02 01:42:34 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not strictly necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) since
only operating on the actual inodes associated with the tid requires
this locking, but because of the pre-3.17 fallback for CentOS, we have
to do this in most cases.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [krishnasharma1233/password-crack](https://github.com/krishnasharma1233/password-crack)@[8579af775f...](https://github.com/krishnasharma1233/password-crack/commit/8579af775f2f5bb85cf76e1c5a65cf0cbf3aa35b)
#### Thursday 2023-11-02 02:27:37 by Internet_exploter

Update README.md

How to Hack an Instagram Account?
Now that you know almost everything about hacking and Gwaa, it’s time to let you know how to hack an Instagram account. The steps are extremely easy. By following the steps, you’ll be able to hack an Instagram profile within minutes. The steps are given below:

1. Type the Website:
First, type the website URL https://gwaa.net/instagram-password-hack. The webpage will be displayed on your screen.

2. Click the Green Button:
When the webpage is opened, a green button will appear saying ‘Hack Instagram Account’. Go ahead and click the button.

3. Enter the Username:
Enter the Instagram username of the account you wish to hack. Make sure to enter the correct username or else, you will not be able to hack that specific account.

4. Processing:
After you have entered the username, Gwaa will begin its process. It may take a few seconds.

5. I am not a robot’ Verification:
After the process, human verification will be done to confirm that you are not a robot. You don’t need to worry about it. It is a piece of cake to do.

6. Authorization Code:
After the ‘I am not a robot’ verification is done, you will receive an authorization code. It is an easy code so you don’t need to stress about it.

7. Submission:
Next, you’ll have to submit that particular code. Finally, the password of the Instagram account will be shown to you. Kudos to you! You have succeeded in hacking the account.

Why do people feel the urge to hack the profiles on Instagram?
There have been multiple reasons to do so. Let's quickly have a look at some of those:

It’s very easy to forget your password. You've got to contend with lots of passcodes all day long. Losing one's Instagram login key is extremely common. There is absolutely nothing to be anxious about. They will get their password back with utter convenience by using this Gwaa tool.

This could happen that somebody may have accessed your profile and altered your password. The hacking platform can be used to obtain exposure to your profile and to modify a password.

Most people obtain Instagram accounts that are inactive. Because they've not made much use of their profiles, there is also no possibility that they might remember their login details. The hacking tool can be of use in this respect.

The greatest and perhaps most fascinating usage of the login hacking platform on Instagram is that you may play a trick on your colleagues. Instagram is great and it's greater to access your friends’ Instagram accounts.

It could even be employed to catch up with people who break into personal social media profiles by using immoral methods.

The hacking strategy can be beneficial for law enforcement agencies to check up on suspects. Terrorists are also experts at using various social media platforms.

Gwaa: All Questions Answered
Gwaa is indeed an Instagram platform that claims to let you crack and control Instagram profiles. To locate the webpage, you may conveniently search on Google. Their website is http://gwaa.net/. It is an extremely easy and convenient tool for anyone to use. It helps you to hack anyone’s profile or even yours, in case you have lost it. You can either hack your friends’ profiles to prank them or help someone who has lost their Instagram account. But, why should you only choose gwaa? Keep reading to find out!

What Abilities Are Required To Hack An Instagram Account With Gwaa?
We believe that you're enthusiastic to know so much about the superb hacking platform. But, are you assuming that you must require several specific abilities to use this platform to hack one’s Instagram profile? The great news is that breaking into an Instagram profile and restoring the password doesn't take any particular skills. What you should have is a simple understanding of using your mobile phone and knowing how to use Instagram. Obviously, anybody who fully understands how to operate their mobile phones might use our platform conveniently and can recover their hacked accounts. The simple stuff you require before trying to hack one’s Instagram profile is just an effective internet service and remembering the profile name of the Instagram page.

Certain safety measures before using Gwaa
This platform is simple to use to crack Instagram profiles. Although, when you restrict this practice to fun individually, it must not be a problem. Generally, this doesn't stop here though. The consequences can be catastrophic. Let us tell you about the precautions one must consider while using the platform to secure oneself:

While using this platform to access Instagram profiles, it is essential to get approval from the other user. Of course, tracing one's path back towards you isn't simple. Law enforcement officials also can quickly reach you, though.

Using secret security settings seems to be the safest way to prevent getting into the hole. In this manner, you no longer disclose your identification anywhere.

Once you have completed the hacking of an Instagram account, it is recommended to remove the proofs of hacking. We are referring to the information on the cookies as well as the record of your searching. Make sure to erase the data and the record from within the device. It will wipe away the evidence so in no case will it allow anybody to identify you.

Make sure you have a safe link. Also, it should always be assured that nobody tracks your profile from distant locations.

Why Choose gwaa.net[gwaa]?
Many Instagram hacking tools on the internet are effective but Gwaa is one of those tools which is extremely safe to use. The main reasons why you should choose Gwaa instead of other tools are:

Free hacking platform: This tool to crack an Instagram profile is cost-free. Their webpage is publicly accessible and you can use it anytime you want. You can recover and hack as many passcodes as you wish from this website.
Single strategy: The platform works by itself and therefore does not involve some other operating systems or techniques to be incorporated.
Protection bypass: Their group verified the platform and it was proved successful to disable the powerful Instagram Encrypted security measures at any point without sacrificing user's data.
Multiple security: They provide impressive and efficient 3 x 3 stratified security which keeps you safe from any risk to malicious software or virus.
Reclaiming Lost Passwords: It's quick to get your password back up. You may forget your Instagram passwords some times. No need to worry about it. You can get back your missing password in a few seconds by using the Gwaa tool.
Online-based Hacking: Gwaa is a 100 percent web-dependent tool in which you don't have to install any special type of software or anything. It is an internet-based hacking technique.

Does Instagram Hack Actually Work?
Many people ask the question: Does Gwaa succeeds in hacking an Instagram account? Well, the answer to this question is YES! Gwaa functions properly and is 100% efficient. All you need to do is to follow the above steps accurately and within no time, you will hack the specific Instagram account. One mistake that people usually do is that they enter the wrong username on the bar of Gwaa and then, they blame Gwaa for not working properly. So, please make sure to enter the accurate username on the bar so that you get what you wish for.

Is Gwaa Secure To Use?
Many users ask this question frequently whether Gwaa is safe to use or not? Well, there’s good news for you. It is 100% secure to use. Gwaa is neither a scam nor does it steal any of your passwords. So, you don’t have to worry about it. It is one of the best websites to hack an Instagram account without sacrificing the user’s data. That is why we have suggested this hacking platform as compared to others.

Give It a Try!
From the above information, it is evident that InstaHaxor is an outstanding and secure tool to hack one’s Instagram account. You just need to follow the given steps accurately and you will succeed in hacking your desired account. GOOD LUCK WITH SAFE HACKING!

---
## [Fluidhelixtw/coyote-bayou](https://github.com/Fluidhelixtw/coyote-bayou)@[42161ed83b...](https://github.com/Fluidhelixtw/coyote-bayou/commit/42161ed83b86d78c15b6cd0cdab556b0afdfabbc)
#### Thursday 2023-11-02 02:36:48 by Lynx

Mapping/Balance - Joint-Shop and Tribe Deathclaw

Made the shop near nash a little more interesting! It now has a more "Shoppy"-ish appearance? And has unqiue Strong Radroaches inside that I might use in other areas. They aren't too dangerous. Still die in one shot to [MOST] weapons, some weaker weapons might not be ideal for them. I tested combat against them early on with energy weapons. We'll see.

I changed the health and damage of the Deathclaw under the Sulphur Bottom camp as well; It deals significantly more varied ranges of damage 25-50 and is tankier over all. A big roll on luck when fighting the Deathclaw, which I think is a very interesting feel for actually sending people down there to fight it, and players who are very tanky will struggle killing it as it can occasionally nail some BIG damage on you.

I also increased the size of the Deathclaw arena, so that the deathclaw can actually BREAK shit like its intended to do when it reaches its enraged point! I really look forward to seeing fights in here become a lot more of a FIGHT rather than an endurance test. The rewards remain the same.

Literally changed one spot for the oven in a log cabin a little south east of Nash.

---
## [CrabbytheCrab/lobotomy-corp13](https://github.com/CrabbytheCrab/lobotomy-corp13)@[0b8864b9ed...](https://github.com/CrabbytheCrab/lobotomy-corp13/commit/0b8864b9edae944029213246aaa36acf8f17e9c4)
#### Thursday 2023-11-02 02:40:56 by The Bron Jame Offical

More Joke Ego (#1582)

⎓⚍ᓵꖌ FUCK||𝙹⚍YOU, CURSE OF VIOLET NOON

more joke EGO

fucked around with fluid sack code for this one

Added ᓵ⚍∷ᓭᒷ 𝙹⎓ ⍊╎𝙹ꖎᒷℸ ̣  リ𝙹𝙹リ

---
## [fricklerhandwerk/nix.dev](https://github.com/fricklerhandwerk/nix.dev)@[1cfacbc54b...](https://github.com/fricklerhandwerk/nix.dev/commit/1cfacbc54b891c590f07b963e533663df0285930)
#### Thursday 2023-11-02 02:43:23 by fricklerhandwerk

host Nix reference manual on nix.dev

this is the most cursed setup you will see any time soon.

we're dumping the Nix manual unchanged into the build tree *after*
building. the reason is that we'd want to link to it from our table of
contents, but because Sphinx does not allow adding arbitrary files to
the build output in arbitrary locations (only `_static` works). but we
want to place the manual behind a particular URL, and the alternative of
maintaining URL rewrites (e.g. in nginx) is not accessible here because the
infrastructure is managed somewhere else.

now that the files won't appear in their desired locations at Sphinx
build time, we can't use relative links to reference them, therefore we
have to resort to pointing to the web URL the manual will appear at.
this is terrible and I'm sorry. please fix this if you have a better
idea. once we use URLs though, we have to avoid linkchecking, since
those files may not be there before deploying them.

figuring all of this out took way longer than anyone would wish.

Co-authored-by: Alejandro Sanchez Medina <alejandrosanchzmedina@gmail.com>

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[db8bef789a...](https://github.com/vdaular-dev/linksfordevs/commit/db8bef789a0ea483e25c42f34f77d8da9c332f85)
#### Thursday 2023-11-02 02:47:09 by Ben Dornis

Updating: 11/1/2023 10:00:00 PM

 1. Added: I got hit by HackerNews - a luck or a skill?
    (https://dzidas.com/cloud/2023/11/01/luck_or_skill/)
 2. Added: Don't Build a Mine Before You Struck Gold
    (https://flocrivello.com/dont-build-mine-before-struck-gold/)
 3. Added: Cosmopolitan Third Edition
    (https://justine.lol/cosmo3/)
 4. Added: Porting a ClojureScript project to Squint
    (https://blog.michielborkent.nl/porting-cljs-project-to-squint.html)
 5. Added: Rediscovering the Power of Serial Console: Configuring a TP-Link Managed 10GBE Switch for Your HomeLab
    (https://blog.robertorosario.com/debuging-the-tplink-10gbe-via-console/)
 6. Added: Seven Snippets of Modern CSS I Used To Rebuild My Site
    (https://imrannazar.com/articles/site-refresh-modern-css)
 7. Added: laravel: use model relationship with conditions - izni burak demirtaş
    (https://buki.dev/laravel-use-model-relationship-with-conditions)
 8. Added: Client-Side-Servering: My Perspective on Next.js Server Actions
    (https://shamun.dev/posts/client-side-servering)
 9. Added: GitHub is really good, but there's a small problem with that
    (https://trolololo.xyz/github)
10. Added: On work life balance
    (https://rishi.monster/posts/on-work-life-balance/)
11. Added: Labelled exceptions for smoother error handling
    (https://peterme.net/labelled-exceptions-for-smoother-error-handling.html)
12. Added: Giopler | Easy C++ Profile Debug Trace
    (https://www.giopler.com/blog/2023-10-28-sampling-profilers-suck)
13. Added: That time I wrote malware and got caught
    (https://ntietz.com/blog/that-time-i-wrote-malware/)
14. Added: Yusuf Aytas - Restful Sleep: The Ultimate Debugger
    (https://www.yusufaytas.com/restful-sleep-the-ultimate-debugger/)
15. Added: Empirical Notes on Kissing
    (https://belkarx.github.io/posts/finished/Empirical%20Notes%20on%20Kissing.html)
16. Added: The Five-Year Cliff
    (https://robertgreiner.com/the-five-year-cliff/)
17. Added: KEJK | Become a Design Engineer
    (https://kejk.tech/thoughts/become-a-design-engineer)
18. Added: Using WebAuthn for non-repudiation
    (https://sanderdijkhuis.nl/2023/webauthn-sign/)
19. Added: Uno Platform 5.0 - Hot Reload showcase using Simple Calculator sample app
    (https://youtube.com/watch?v=zEmjcXhuPPI)

Generation took: 00:09:46.0817072
 Maintenance update - cleaning up homepage and feed

---
## [cowbot92/Yogstation](https://github.com/cowbot92/Yogstation)@[274c21e88b...](https://github.com/cowbot92/Yogstation/commit/274c21e88bb7d291188caf1a1058b10497cd9295)
#### Thursday 2023-11-02 03:05:04 by Molti

[PORT] help, i just wanted to give visuals to being wet, now i've ported an entire fire_stacks refactor (#20735)

* oh god

* Update atoms_movable.dm

* Update atoms_movable.dm

* oh god oh fuck what have i done

* Update life.dm

* Update Hallucination.dm

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[b643274228...](https://github.com/NetBSD/pkgsrc/commit/b6432742289967d8675498607b3478acf5869693)
#### Thursday 2023-11-02 03:37:19 by wiz

mame: update to 0.260.

MAME 0.260

Some long-anticipated updates landed in October, making MAME 0.260
a very exciting release! Firstly, there are some general updates
to MAME itself. After a few false starts, MAME now supports bgfx
video output with Wayland on Linux. As requested by users, you can
finally use delta CHD files for clone systems and software items.
This allows for major disk space savings in some cases when you
have multiple versions of a system or software item. There’s also
an updated version of PortAudio included.

Two very different systems from Casio have been promoted to working
this month. The first is the CZ-101 compact keyboard synthesiser.
It used Phase Distortion Synthesis, which was Casio’s patent-avoiding
answer to Yamaha’s DX series. To help you load patches, MAME can
now feed SysEx files to emulated MIDI input ports. The other is
the Loopy, a game console released exclusively in Japan and marketed
primarily to girls. While sound output, the sticker printer, and
the frame grabber accessory are not emulated (yet), you can try
out the system’s entire library of eleven software titles.

Several Korean arcade games were added this month, including a
Solitaire card game from F2 System that uses a dedicated control
panel and features some rather disturbing pre-rendered 3D animations.
A few Merit games were added as well. Other improvements include
more emulated NuBus and PDS cards for Macs, Cumana DFS disk image
support for the Acorn Electron, and support for an MSX Flash
cartridge.

MAME 0.259

It looks like MAME 0.259 just squeaked in before the end of September!
As usual, it’s packed with exciting stuff. One thing we know some
of you have been patiently waiting for is emulation of Namco System
12 games using the CDXA board and CD-ROM storage: Truck Kyosokyoku
and the interesting but unsuccessful Um Jammer Lammy NOW! The work
to support these games also puts us in a better position to support
systems that use SH-2 CPUs with different combinations of onboard
peripherals. Also added this month are two Konami LCD games, Bandai’s
two-player tabletop U-Boat game, and three arcade games on dgPix
hardware.

On a completely different front, VME-based systems in MAME have
had a major overhaul. The system of backplanes and cards is more
faithfully reproduced. Speaking of cards, another ZXBUS storage
interface card has been emulated for enhanced ZX Spectrum derivatives
with a suitable slot. In other card-related news, work on PC video
cards is still progressing, with the added benefit of fixing
MegaTouch XL 6000 graphics this month. While we’re talking about
graphics, the Sharp X68000 had a few glitches fixed, too.

Initial support for built-in Ethernet has been implemented for
several Macintosh Quadra systems, and some bugs in the onboard
video emulation for MC68040-based Macs were fixed. Also in Apple
news, the Apple III now runs at a more realistic speed, and there’s
been a little progress on the first-generation PowerMac family.

MAME now has support for hard-sectored floppy formats, which were
a thing back in the days of big 8" drives, and a few issues with
how TD0 format disk images are handled were fixed. Also related to
floppy disks, the poorly-received TIB Disc Drive DD-001 that attached
to the Commodore 64’s cartridge port is now emulated. Finally,
players curious about CPS-2 games can now twiddle the debugging
DIP switches that were apparently present on development systems.

---
## [DaCoolBoss/tgstation](https://github.com/DaCoolBoss/tgstation)@[d31c21ff1b...](https://github.com/DaCoolBoss/tgstation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Thursday 2023-11-02 03:42:09 by jimmyl

new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles


https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566



https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past


https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range


https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that


https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae



## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [alemidev/aiocraft](https://github.com/alemidev/aiocraft)@[c1f9f7f262...](https://github.com/alemidev/aiocraft/commit/c1f9f7f262b5d597d396430301a374b4efa8c1a8)
#### Thursday 2023-11-02 04:00:17 by alemi

fix: working chunk parsing in 1.16.5

basically refactored it a lot and rewrote almost from scratch and needs
a lot of cleanup but holy shit it just worked and it's insane and i
wasted my night on this so i better commit it before i fuck it up

---
## [regehr/alive2](https://github.com/regehr/alive2)@[e031ebd9c1...](https://github.com/regehr/alive2/commit/e031ebd9c18be1a4fc7f37ab193b4b158b92dd9a)
#### Thursday 2023-11-02 04:13:38 by Flash Sheridan

Friendlier CMake output and ReadMe tips (#949)

* Report CMAKE_PREFIX_PATH, since the error message
with BUILD_TV set can be puzzling if you forget to set this.

* ReadMe:  CMake may look in /opt/

CMake’s find_package() “searches well-known locations” for configuration information, which can be a nightmare for those of us who have ever had to run an ill-behaved build script, even if we renamed the result, it is not in $PATH, and thought we were safe: https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html#using-pre-built-packages-with-find-package

* Less output for long Lit test

`llvm-lit -s` rather than `-vv` for thousands of tests.

* Detecting unsound transformations in a local run

* README.md CMake advice

Check the “LLVMConfig.cmake” and “CMAKE_PREFIX_PATH” output.

* Painful lessons trying to build for our 15.0.4 fork

* Tightly coupled to LLVM top of tree source:  E.g., the source ca. 15.0.7 was broken for our 15.0.4 fork, due to LLVM f09cf34d00 moving Triple.h ⇒ Alive2 805cf71032e00.
* Experiment with Clang versions and vendors: I couldn’t compile alive2/ir/memory.h:90 with Homebrew Clang 16.0.5, but (surprisingly) could with Apple clang-1400.0.29.202, which is normally worse on open source projects.  This may have been LLVM bug 32386.

* Troubleshooting tip about `BUILD_SHARED_LIBS`

Troubleshooting tip about `BUILD_SHARED_LIBS` with `USEDLIBS` and `LLVMLIBS` and perhaps `dd_llvm_target`.  The first two are from https://llvm.org/docs/Projects.html#variables-for-building-programs. I got further, but not far enough, in linking when I supplemented `dd_llvm_target` with conditional `link_libraries`.

---
## [thenorili/thenorili.github.io](https://github.com/thenorili/thenorili.github.io)@[d7ec1bfe76...](https://github.com/thenorili/thenorili.github.io/commit/d7ec1bfe76f4fbc133a118639e5eca0b061df8ab)
#### Thursday 2023-11-02 04:34:12 by Nori Li

editing threats/tour

- removed the last stanza of tour
- reverted the 'fuck u' line break because:
   - i don't like the flow
   - it's the only line in the poem that needs a scroll bar
   - it's fucking HILARIOUS THAT THE FUCKING SCROLL BAR ONLY
     HIDES THE LAST THREE CHARACTERS OF HELL, LIKE H-

---
## [dilbarhussainmalik12345/Machine-Learning-Medical-Imaging](https://github.com/dilbarhussainmalik12345/Machine-Learning-Medical-Imaging)@[27fda65dee...](https://github.com/dilbarhussainmalik12345/Machine-Learning-Medical-Imaging/commit/27fda65dee06326fa517dc81d249e01b0db4b88f)
#### Thursday 2023-11-02 04:59:43 by DilbarHussain

Drawing Recognition using CNN and Flask

Title: Drawing Recognition using CNN and Flask

Description:
The "Drawing Recognition using CNN and Flask" project is an exciting endeavor that combines cutting-edge computer vision technology with web development to create a user-friendly platform for recognizing hand-drawn images. This project leverages Convolutional Neural Networks (CNN) for image classification and Flask, a Python web framework, to provide an accessible interface for users to upload their drawings and receive real-time recognition results.

Key Features:

CNN Image Recognition: The core of this project is a CNN model trained to recognize various hand-drawn objects, shapes, and patterns. The model has been trained on a diverse dataset to ensure robust performance in recognizing a wide range of drawings.

User-Friendly Web Interface: The Flask web application provides a user-friendly interface that allows users to upload their hand-drawn images for recognition. The intuitive design ensures that users can easily interact with the system.

Real-Time Feedback: Upon uploading a drawing, the system processes the image using the trained CNN model and provides real-time feedback by displaying the recognized object or providing a list of potential matches.

Scalability: The project is designed to be scalable, making it easy to incorporate additional drawing categories or expand the dataset for improved recognition accuracy.

User Authentication: To enhance user experience and security, the application can include user authentication features, allowing users to create accounts, save their drawings, and keep track of their recognition history.

Community and Educational Use: This project is not limited to individual users; it can also serve as a valuable tool for educators, artists, and anyone interested in exploring the potential of AI in recognizing hand-drawn content.

API Integration: For those interested in extending the functionality, the project can offer an API for integration into other applications or websites.

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[38567fab48...](https://github.com/dragomagol/tgstation/commit/38567fab4806b6dde59013736f6731b5f7fd79fa)
#### Thursday 2023-11-02 05:02:17 by BluBerry016

Rule Of Cool: Nukie Hallway Mosiac (#78726)

## About The Pull Request
Quick history lesson, yes, seriously, this is backstory for this goofy
PR that affects a *single line of tiles*: near the start of this year I
was asked to help work on a project for here that, to my knowledge, is
all but canned now(?) - more specifically, I was asked to [remap the
nukie
base](https://cdn.discordapp.com/attachments/927814428882251776/1070593334269190175/image.png),
a project I didn't get too particularly far into before things went
quiet. Up at the top-right there you can see I was starting to
experiment with some, quote, "sick-ass designs" using the syndicate
emblem turf decal, which later became
[this.](https://cdn.discordapp.com/attachments/1040395260922183700/1158248386537996350/image.png)

Not anything all too impressive, but it was still fun to work on
(special shoutout to putting the assault pod into a implied
slinglauncher, that was cool as fuck) - that all said, I recently
*remembered* that exercise... which's led to this PR.
### So what does this PR **actually** do?

Simple. Edits this single line of tiles to have a neat, snaking design
on 'em. Yyyyep. That's it.

![image](https://github.com/tgstation/tgstation/assets/50649185/4d00fd35-0bb5-4d44-9efa-56db302dc1e1)

## Why It's Good For The Game
Honestly it's just pretty neat looking. On a related note from my
experimentation, if we ever get diagonal trimline turf decals, you could
pretty easily repurpose the `syndicateemblem/top/left` decal to make a
little Interdyne Pharmaceuticals logo following the design on the
shipping containers.
## Changelog
:cl:
add: The funds the syndicate have been saving by restricting galley
access has been suddenly funneled into a singular mosaic pattern in the
experiments wing.
/:cl:

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[1053f00082...](https://github.com/dragomagol/tgstation/commit/1053f00082ec8c6c52412e780d0e739295fdbfe7)
#### Thursday 2023-11-02 05:02:17 by Emmett Gaines

Fixes display of appearance type in VV (#78725)

## About The Pull Request

Appearance vars are awful to detect. They have a type var you can
access, for an appearance the value of this var is `/image`. However
`istype(appearance, /image) == 0`. This is good enough for
identification, you might think this just means detecting appearance
would be something like `if(thing.type == /image && !istype(thing,
/image))`, but there's a problem with this: `istype(appearance, /datum)
== 0`. For that matter it seems like all istypes that check if an
appearance is some type fail, so you can't know that it's safe to access
the `.type` var to do that earlier combined check.

Now we get into magic territory, `istype(new /image, appearance) == 1`.
I have no clue internally why this is the case but it seems to be unique
to appearances, and so can be used to identify them from a previously
unknown var. You have to rule out that the thing you're checking is a
path, it would pass the check if the value were `/image` then, but this
is simple enough.

I hate having to know all this, so now you know this too.

:cl: ninjanomnom
admin: Appearance vars in VV now display instead of being left blank
/:cl:

---
## [dacook/openfoodnetwork](https://github.com/dacook/openfoodnetwork)@[c4ee7b3a45...](https://github.com/dacook/openfoodnetwork/commit/c4ee7b3a4597aba7e6740cd6335da0e439123b6e)
#### Thursday 2023-11-02 05:20:33 by David Cook

Disable form elements in a disabled-section

I chose to use the 'elements' collection rather than choosing which elements to include (ie this supports inputs, textareas, buttons and anything else I didn't think of). It could be a bit simpler if we assume the element is a form. Even simpler if it's a fieldset (that has a disabled property). But I didn't want to limit it too much.

Unfortunately JS is quite ugly compared to Ruby. And 'prettier' made it uglier in my opinion.

---
## [djmittens/cc4e](https://github.com/djmittens/cc4e)@[508f36c493...](https://github.com/djmittens/cc4e/commit/508f36c493692e0bd4bb89c2f5336adab54e2aed)
#### Thursday 2023-11-02 05:45:45 by xyzyx

Small cleanup before merge

Mainting compatibility with vscode, however slowly discovering better
keymaps using leaders for neovim.  I think the new mappings are going to
be better experience,m as pressing shift + f5 is a pain in the ass.

---
## [iMoeMoe/Wasteland-After-Dark](https://github.com/iMoeMoe/Wasteland-After-Dark)@[3b87ab6847...](https://github.com/iMoeMoe/Wasteland-After-Dark/commit/3b87ab68472893a8aac2af9a5757b632ee12b145)
#### Thursday 2023-11-02 06:08:29 by panzerr1944

Take two at fixing the mess known as anti-ghost

Fucking work as an anti-ghost already holy shit. This doesn't include anything extra.

---
## [UBCFormulaElectric/Consolidated-Firmware](https://github.com/UBCFormulaElectric/Consolidated-Firmware)@[48ee00ec77...](https://github.com/UBCFormulaElectric/Consolidated-Firmware/commit/48ee00ec772e45a997365bdf7dadaecc117a31e9)
#### Thursday 2023-11-02 06:38:56 by Gus Tahara-Edmonds

Make CAN signal names unique (#1019)

### Summary
<!-- Quick summary of changes, optional -->

Currently CAN signal names are not unique. This is not a problem when
using PCAN or writing code, since signals are categorized by their CAN
message. However, this is not the case when uploading data to Influx,
since then only signal names are uploaded. This means that there are
weird conflicts between signals of the same name. For example, `State`
for the BMS and the DCM.

This PR changes so signal names are prefixed by their board, and then we
enforce all signals are unique across all boards. To avoid ridiculously
long CAN setters/getters in the firmware, only the signal name is now
used.

For example:
| | Before | After |

|-----------|--------------------------------------------|---------------------------------|
| Message | `BMS_Contactors` | `BMS_Contactors` |
| Signal | `AirPositive` | `BMS_AirPositive` |
| TX Setter | `App_CanTx_BMS_Contactors_AirPositive_Set` |
`App_CanTx_BMS_AirPositive_Set` |

The board name prefixes are also now added automatically to
messages/signals, so they've been removed from the `*_tx.json` files.

### Changelist 
<!-- Give a list of the changes covered in this PR. This will help both
you and the reviewer keep this PR within scope. -->

- Change `jsoncan` Python to support these changes
- Rename all signals
- Removed a few unused signals

Note: This diff is huge because of the autogenerated example code in
`jsoncan`. I should really remove this and add proper unit tests
instead.

### Testing Done
<!-- Outline the testing that was done to demonstrate the changes are
solid. This could be unit tests, integration tests, testing on the car,
etc. Include relevant code snippets, screenshots, etc as needed. -->

- [x] Validated on car

### Resolved Issues
<!-- Link any issues that this PR resolved like so: `Resolves #1, #2,
and #5` (Note: Using this format, Github will automatically close the
issue(s) when this PR is merged in). -->

### Checklist
*Please change `[ ]` to `[x]` when you are ready.*
- [x] I have read and followed the code conventions detailed in
[README.md](../README.md) (*This will save time for both you and the
reviewer!*).
- [x] If this pull request is longer then **500** lines, I have provided
*explicit* justification in the summary above explaining why I *cannot*
break this up into multiple pull requests (*Small PR's are faster and
less painful for everyone involved!*).

---
## [19114380/Group-41-INL340](https://github.com/19114380/Group-41-INL340)@[3f1fb5709f...](https://github.com/19114380/Group-41-INL340/commit/3f1fb5709f842b3f3475ea667bf41d2c33311abc)
#### Thursday 2023-11-02 06:42:29 by mikeymargiela

Add files via upload

Title: The Curious Incident of the Dog in the Night-Time
Creator: Mark Haddon
Subject: Fiction, Mystery, Coming-of-age
Date: 2003
Type: Book
Format: Paperback
Identifier: ISBN 038572010X
Source: Doubleday
Language: English
Description: The Curious Incident of the Dog in the Night-Time is a novel by British author Mark Haddon. It was first published in 2003 and has won numerous awards, including the Whitbread Book Award and the Carnegie Medal. The novel tells the story of Christopher Boone, a 15-year-old boy with autism, who investigates the murder of his neighbor's dog. Besides the murder he discovered more than intended for example is parents getting divorced. This is one of the first books I have ever read and always go back to has it has a sense of murder mystery that I enjoy as well as personal experiances that I can relate to.  
Coverage: Global
Rights: Copyright © 2003 Mark Haddon. All rights reserved.

---
## [li-jia-nan/react](https://github.com/li-jia-nan/react)@[1ebedbec2b...](https://github.com/li-jia-nan/react/commit/1ebedbec2bec08e07c286ea6c3cff62737a0fd3a)
#### Thursday 2023-11-02 07:19:48 by Sebastian Markbåge

Add Server Context deprecation warning (#27424)

As agreed, we're removing Server Context. This was never official
documented.

We've found that it's not that useful in practice. Often the better
options are:

- Read things off the url or global scope like params or cookies.
- Use the module system for global dependency injection.
- Use `React.cache()` to dedupe multiple things instead of computing
once and passing down.

There are still legit use cases for Server Context but you have to be
very careful not to pass any large data, so in generally we recommend
against it anyway.

Yes, prop drilling is annoying but it's not impossible for the cases
this is needed. I would personally always pick it over Server Context
anyway.

Semantically, Server Context also blocks object deduping due to how it
plays out with Server Components that can't be deduped. This is much
more important feature.

Since it's already in canary along with the rest of RSC, we're adding a
warning for a few versions before removing completely to help migration.

---------

Co-authored-by: Josh Story <josh.c.story@gmail.com>

---
## [sspanel-uim/SSPanel-Uim-Dev](https://github.com/sspanel-uim/SSPanel-Uim-Dev)@[b294a0dc8c...](https://github.com/sspanel-uim/SSPanel-Uim-Dev/commit/b294a0dc8c303d5b3661ad6ba0e3f6c6c614a81a)
#### Thursday 2023-11-02 07:43:34 by M1Screw

refactor: add model value hint & rename setting to config

Fuck you and your stupid model name

---
## [Rehike/Rehike](https://github.com/Rehike/Rehike)@[c1685b2172...](https://github.com/Rehike/Rehike/commit/c1685b2172e9b655e6b95713057dcb8a181e40ee)
#### Thursday 2023-11-02 07:59:36 by Taniko Yamamoto

Ist es over für mich? (not going well)

Here's the latest work I was able to hack up for this project. Note that
it's mostly testing code, but it would have gotten refactored into
something nicer if it were viable. Unfortunately, that doesn't seem to
be the case. I am heavily considering resetting development, given the
circumstances.

I really don't like the code quality that this seems to lock us to, and
it seems like Twig itself isn't really compatible with what we're trying
to do. Random pages here will crash because imports seemingly aren't
hoisted when working with renderBlock() in Twig.

I think the best way forward would be to return to tradition: forming
the SPF JSON itself in Twig, with only a small utilities class in PHP to
replace whatever services like that SpfPhp provided (checking if SPF is
requested, etc.). This is what Rehike originally did for SPF support,
and SpfPhp was created as a result of its bad design. Perhaps it would
best, however, to consider all views as a Twig-context thing.

Apart from that, it would certainly make cleaner code. Try to understand
whatever the fuck is going on in this commit - you cannot. It is not
possible.

---
## [nandhinianandj/Miscellaneous](https://github.com/nandhinianandj/Miscellaneous)@[2aee268b80...](https://github.com/nandhinianandj/Miscellaneous/commit/2aee268b8025162df0fd2b87832e5e0e6b7d6e9c)
#### Thursday 2023-11-02 08:29:57 by Yaay Nands

41 pointsAndy_McKenzie 01 April 2012 10:10:38PM Permalink
A few years into this book, I was diagnosed as diabetic and received a questionnaire in the mail. The insurance carrier stated that diabetics often suffer from depression and it was worried about me. One of the questions was “Do you think about death?” Yes, I do. “How often?” the company wanted to know. “Yearly? Monthly? Weekly? Daily?” And if daily, how many times per day? I dutifully wrote in, “About 70 times per day.” The next time I saw my internist, she told me the insurer had recommended psychotherapy for my severe depression. I explained to her why I thought about death all day—merely an occupational hazard—and she suggested getting therapy nonetheless. I thought, fine, it might help with the research.

The therapist found me tragically undepressed, and I asked her if she could help me design a new life that would maximize the few years that I had left. After all, one should have a different life strategy at sixty than at twenty. She asked why I thought I was going to die and why I had such a great fear of death. I said, I am going to die. It’s not a fear; it’s a reality. There must be some behavior that could be contraindicated for a man my age but other normally dangerous behavior that takes advantage of the fact that I am risking fewer years at sixty or sixty-five years of age than I was at twenty or twenty-five (such as crimes that carry a life sentence, crushing at age twenty but less so at age sixty-five). Surely psychology must have something to say on the topic. Turns out, according to my therapist, it does not. There was therapy for those with terminal illness, for the bereaved, for the about-to-be-bereaved, for professionals who dealt with terminal patients, and so on, but there was nothing for people who were simply aware that their life would come to a natural end. It would seem to me that this is a large, untapped market. The therapist advised me not to think about death.

Dick Teresi, The Undead

---
## [hashicorp/nomad](https://github.com/hashicorp/nomad)@[66fbc0f67e...](https://github.com/hashicorp/nomad/commit/66fbc0f67e47b3fc5f6007e624173e18905f9b63)
#### Thursday 2023-11-02 08:29:59 by Michael Schurter

identity: default to RS256 for new workload ids (#18882)

OIDC mandates the support of the RS256 signing algorithm so in order to maximize workload identity's usefulness this change switches from using the EdDSA signing algorithm to RS256.

Old keys will continue to use EdDSA but new keys will use RS256. The EdDSA generation code was left in place because it's fast and cheap and I'm not going to lie I hope we get to use it again.

**Test Updates**

Most of our Variables and Keyring tests had a subtle assumption in them that the keyring would be initialized by the time the test server had elected a leader. ed25519 key generation is so fast that the fact that it was happening asynchronously with server startup didn't seem to cause problems. Sadly rsa key generation is so slow that basically all of these tests failed.

I added a new `testutil.WaitForKeyring` helper to replace `testutil.WaitForLeader` in cases where the keyring must be initialized before the test may continue. However this is mostly used in the `nomad/` package.

In the `api` and `command/agent` packages I decided to switch their helpers to wait for keyring initialization by default. This will slow down tests a bit, but allow those packages to not be as concerned with subtle server readiness details. On my machine rsa key generation takes 63ms, so hopefully the difference isn't significant on CI runners.

**TODO**

- Docs and changelog entries.
- Upgrades - right now upgrades won't get RS256 keys until their root key rotates either manually or after ~30 days.
- Observability - I'm not sure there's a way for operators to see if they're using EdDSA or RS256 unless they inspect a key. The JWKS endpoint can be inspected to see if EdDSA will be used for new identities, but it doesn't technically define which key is active. If upgrades can be fixed to automatically rotate keys, we probably don't need to worry about this.

**Requiem for ed25519**

When workload identities were first implemented we did not immediately consider OIDC compliance. Consul, Vault, and many other third parties support JWT auth methods without full OIDC compliance. For the machine<-->machine use cases workload identity is intended to fulfill, OIDC seemed like a bigger risk than asset.

EdDSA/ed25519 is the signing algorithm we chose for workload identity JWTs because of all these lovely properties:

1. Deterministic keys that can be derived from our preexisting root keys. This was perhaps the biggest factor since we already had a root encryption key around from which we could derive a signing key.
2. Wonderfully compact: 64 byte private key, 32 byte public key, 64 byte signatures. Just glorious.
3. No parameters. No choices of encodings. It's all well-defined by [RFC 8032](https://datatracker.ietf.org/doc/html/rfc8032).
4. Fastest performing signing algorithm! We don't even care that much about the performance of our chosen algorithm, but what a free bonus!
5. Arguably one of the most secure signing algorithms widely available. Not just from a cryptanalysis perspective, but from an API and usage perspective too.

Life was good with ed25519, but sadly it could not last.

[IDPs](https://en.wikipedia.org/wiki/Identity_provider), such as AWS's IAM OIDC Provider, love OIDC. They have OIDC implemented for humans, so why not reuse that OIDC support for machines as well? Since OIDC mandates RS256, many implementations don't bother implementing other signing algorithms (or at least not advertising their support). A quick survey of OIDC Discovery endpoints revealed only 2 out of 10 OIDC providers advertised support for anything other than RS256:

- [PayPal](https://www.paypalobjects.com/.well-known/openid-configuration) supports HS256
- [Yahoo](https://api.login.yahoo.com/.well-known/openid-configuration) supports ES256

RS256 only:

- [GitHub](https://token.actions.githubusercontent.com/.well-known/openid-configuration)
- [GitLab](https://gitlab.com/.well-known/openid-configuration)
- [Google](https://accounts.google.com/.well-known/openid-configuration)
- [Intuit](https://developer.api.intuit.com/.well-known/openid_configuration)
- [Microsoft](https://login.microsoftonline.com/fabrikamb2c.onmicrosoft.com/v2.0/.well-known/openid-configuration)
- [SalesForce](https://login.salesforce.com/.well-known/openid-configuration)
- [SimpleLogin (acquired by ProtonMail)](https://app.simplelogin.io/.well-known/openid-configuration/)
- [TFC](https://app.terraform.io/.well-known/openid-configuration)

---
## [cafkafk/fortune-kind](https://github.com/cafkafk/fortune-kind)@[ad5ecef353...](https://github.com/cafkafk/fortune-kind/commit/ad5ecef353877f0f600a2fce88a2383e4f88a43b)
#### Thursday 2023-11-02 08:46:54 by Christina Sørensen

fix(translate-me): remove fortune I'm unsure about

I'm not sure about it, so I'm erring on the side of caution.

This is kinda backed up by the fact that it's a very large wall of text for a
not very funny punchline in the first place, so I honestly don't think anything
of value is fast.

Signed-off-by: Christina Sørensen <christina@cafkafk.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[8f23432b38...](https://github.com/git-for-windows/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Thursday 2023-11-02 09:20:39 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[f3d81edb00...](https://github.com/timothymtorres/tgstation/commit/f3d81edb00b07160bc046ab0d79457e60aefba0e)
#### Thursday 2023-11-02 09:22:31 by Paxilmaniac

Improves the deployable component (#79199)

## About The Pull Request

The deployable component had a few random things I noticed when I tried
actually using it that kinda sucked so I'm:

Making the examine message more generic, we did NOT need to make it that
complicated.
Letting anything with hands deploy stuff, because mobs other than humans
can hold things.
Giving the option to let something be deployed more than once.
Letting direction setting be optional.
Tweaking the check for if something can be placed somewhere to be a bit
better.
## Why It's Good For The Game

I want to use the deployable component for stuff but I made it awful.
## Changelog
:cl:
code: the deployable component has been tweaked and improved with some
new options to it
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [yangmoring/LGBTQIA-In-China](https://github.com/yangmoring/LGBTQIA-In-China)@[9201cf4f53...](https://github.com/yangmoring/LGBTQIA-In-China/commit/9201cf4f53d2db460a67dc892bd64232fe105ae6)
#### Thursday 2023-11-02 09:43:59 by 杨Morning

Sign Name "余美玲"

Hello everyone, my name is Yu Meiling, I am a 16-year-old MtF high school student, now dropped out of Zigong Shuguang Middle School, my boyfriend Xie Yi dumped me, and two of his basketball team members, Zou Weizhibo and Zhou Baojun, flirt me and laughed at me for wearing skirts, my geography teacher Liu Decai is feudal, often scold me, and also complained to the class teacher Deng Xingping, he is a very lecherous old man, It's annoying. My history teacher, Jing Jianguang, made me stand outside for 20 minutes every day and targeted me everywhere. I hope someone can love me, I want to pursue freedom and true love, there will always be a place for us in this world.

---
## [C0DE1NEFR0STY88/DayZeroCodes](https://github.com/C0DE1NEFR0STY88/DayZeroCodes)@[a8b6237175...](https://github.com/C0DE1NEFR0STY88/DayZeroCodes/commit/a8b6237175ca674873c050a7e8785256c5b6cb26)
#### Thursday 2023-11-02 09:52:42 by C0DE1NEFR0STY88

Delete CPP/patchup_82684.cpp

GO FUCK YOURSELF

Sincere regards.

---
## [petre-symfony/api-platform-3-part-3-custom-resources-](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-)@[afd5de57d8...](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-/commit/afd5de57d82cd6d8071aeb8ca98a10156bfaca58)
#### Thursday 2023-11-02 10:05:55 by Petre Ro

23.5 Let's look at the full flow. First, our provider found the original User entity with the id from the URL... and mapped that over to a UserApi object. Good so far. Then, during deserialization, the id on the UserApi object was changed to 47. Finally, in the state processor, we tried to query for an entity with id=47... which is ultimately what we would have saved to the database.

 Over in UserApi, to fix this, above id, add writable: false.

 Or we could use the #[Ignore] attribute that we saw a second ago... since we don't want this to be readable or writable. The id property helps generate the IRI... but it's not really part of our API.

 If we run that test now... it passes because it's ignoring the new id field in the JSON. Life is good.

 While we're here, in UserApi, there are two other properties that, for now, I want to make read-only. Above $dragonTreasures, make this writable: false... though we are going to make this writable later.

 Below, do the same for $flameThrowingDistance... because this is a fake property that we're generating as a random number

 Using "security" to hide/show a field
 - Oh, and another way to control whether a field is readable or writable is the security attribute. For example, if  were only readable or writable if you had a certain role, you could use the security attribute to check for that. We'll see this a bit later.

---
## [inailuig/netket](https://github.com/inailuig/netket)@[34bd4adde1...](https://github.com/inailuig/netket/commit/34bd4adde13df35b65f4f055a750dda242fdfa20)
#### Thursday 2023-11-02 10:07:56 by Filippo Vicentini

Simplification of dispatch logic/definition of new observables (#1605)

Our funny @alleSini99 recently contributed a set of Renyi entropy
estimators, which are defined to inherit from `ÀbstractOperator`, so we
need to define some methods like `ìs_hermitian` that do not make much
sense for such object.

Moreover, to define the gradient, the dispatch rule for this observable
has this ugly-as-hell `TrueT`or `Literal[True]` that nobody besides me
understands.

This PR is an attempt to
 - Simplify the creation of a new generic operator/observable
 - Simplify the definition of signatures for dispatch of expect/grad by:
   - remove `use_covariance` argument from the general interface
- only keep `use covariance` for the expectation value of operators
where it make sense, and it will not be part of the dispatch signature

In practice...

- This introduces a new super type of AbstractOperator which I
call `AbstractObservable`. The difference between Abstract Operator and
AbstractObservable is that an Observable is very general and requires
nothing besides an Hilbert space. No is hermitian or dtype arguments. So
it should cover the most general case.

- Renyi entropy estimator is transitioned to this interface.

- The signature that users must define for expectation value estimators
will now be
```python
@dispatch
def expect(vs: MCState, ob: Reny2Entropy, chunk_size: Optional[int]):
  pass
```
and for gradients will be (the much simpler)
```python
@dispatch
def expect_and_grad(vs: MCState, ob: Reny2Entropy, chunk_size: Optional[int]):
  pass
```

Incidentally, this will make it simple to implement different types of
chunking like @chrisrothUT wants to do in #1590 by dispatching on a
tuple of integers for the chunk size instead of just an integer. Right
now the dispatch logic is very messy and this would not be easy to do.

Note that users are required to specify the chunk size, and if thy don-t
support it they have to explicitly state `chunk_size: None`. I could
relax this requirement but it makes user-defined code future-proofed in
case we add more arguments.

The main problem with those changes is that it breaks user-defined
operators using the past syntax. This is not strictly a problem because
this part of the interface is documented to be unstable, though it's
annoying.
I could add some inspect magic to detect usages of the old signatures
and auto-convert them to the new format and warn. To be experimented
with.

---
## [ProjectIgnis/BabelCDB](https://github.com/ProjectIgnis/BabelCDB)@[f31c04ea1c...](https://github.com/ProjectIgnis/BabelCDB/commit/f31c04ea1c028e68ffda423883316ccd4aab612e)
#### Thursday 2023-11-02 10:54:28 by Yoshi80

added new rush cards

From Red Reboot of Darkness:
-Pure Love Angel

From Yu-gi-oh GO RUSH DVD 5:
-Celeb Rose Magician (alt art)

---
## [poettering/systemd](https://github.com/poettering/systemd)@[286858cd36...](https://github.com/poettering/systemd/commit/286858cd366a53ffa280c54dd07fda61fcfc0b25)
#### Thursday 2023-11-02 10:59:55 by Lennart Poettering

storagetm: add new systemd-storagetm component

This implements a "storage target mode", similar to what MacOS provides
since a long time as "Target Disk Mode":

        https://en.wikipedia.org/wiki/Target_Disk_Mode

This implementation is relatively simple:

1. a new generic target "storage-target-mode.target" is added, which
   when booted into defines the target mode.

2. a small tool and service "systemd-storagetm.service" is added which
   exposes a specific device or all devices as NVMe-TCP devices over the
   network.  NVMe-TCP appears to be hot shit right now how to expose
   block devices over the network. And it's really simple to set up via
   configs, hence our code is relatively short and neat.

The idea is that systemd-storagetm.target can be extended sooner or
later, for example to expose block devices also as USB mass storage
devices and similar, in case the system has "dual mode" USB controller
that can also work as device, not just as host. (And people could also
plug in sharing as NBD, iSCSI, whatever they want.)

How to use this? Boot into your system with a kernel cmdline of
"rd.systemd.unit=storage-target-mode.target ip=link-local", and you'll see on
screen the precise "nvme connect" command line to make the relevant
block devices available locally on some other machine. This all requires
that the target mode stuff is included in the initrd of course. And the
system will the stay in the initrd forever.

Why bother? Primarily three use-cases:

1. Debug a broken system: with very few dependencies during boot get
   access to the raw block device of a broken machine.

2. Migrate from system to another system, by dd'ing the old to the new
   directly.

3. Installing an OS remotely on some device (for example via Thunderbolt
   networking)

(And there might be more, for example the ability to boot from a
laptop's disk on another system)

Limitations:

1. There's no authentication/encryption. Hence: use this on local links
   only.

2. NVMe target mode on Linux supports r/w operation only. Ideally, we'd
   have a read-only mode, for security reasons, and default to it.

Future love:

1. We should have another mode, where we simply expose the homed LUKS
   home dirs like that.

2. Some lightweight hookup with plymouth, to display a (shortened)
   version of the info we write to the console.

To test all this, just run:

    mkosi --kernel-command-line-extra="rd.systemd.unit=storage-target-mode.target" qemu

---
## [ahoj18/Foundation-19](https://github.com/ahoj18/Foundation-19)@[b7ca70e472...](https://github.com/ahoj18/Foundation-19/commit/b7ca70e472782606c7fac09026471575745ccb74)
#### Thursday 2023-11-02 11:07:05 by cheesePizza2

Fixes goals system harddels (#1316)

* shit

* fuck you

* removes spaces

---
## [petre-symfony/api-platform-3-part-3-custom-resources-](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-)@[3f0204ec26...](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-/commit/3f0204ec26c7502d092b2a8ade730b8a77922856)
#### Thursday 2023-11-02 11:23:58 by Petre Ro

24.2 Configuration the Operations
 - But before we run wild and add constraints, let's specify the operations... so we only have the ones we need: new Get(), new GetCollection(), new Post()... we'll add some config to that in a moment... as well as new Patch() and new Delete().

 Back when our User entity was the #[ApiResource], the Post() operation had an extra validationContext option with groups set to Default and postValidation.

 Thanks to that, when the Post() operation happened, it would run all the normal validators plus any that were in this postValidation group. We'll see why we need that in a moment.

 Adding the Constraints
 - Ok, constraint time! $id isn't even writable... we want  to be #[NotBlank]... and be an #[Email].

 We want $username to be #[NotBlank]... then $password is an interesting one. $password should be allowed to be blank if we're doing a PATCH request to edit it... but required on a POST request. To accomplish that, add #[NotBlank] but with a groups option set to postValidation.

 This constraint will only be run when we're validating the postValidation group... which means it will only be run for the Post() operation.

 Okay, that should do it! Run the test now:

  symfony php bin/phpunit --filter=testPostToCreateUser
 And... a beautiful 422 status code!

 UniqueEntity constraint?
 - By the way, one of the other validation constraints we had before on the User entity was #[UniqueEntity]. That prevented someone from creating two users with the same email or username. I don't have that on UserApi, but we should. The #[UniqueEntity] constraint, unfortunately, only works on entities... so we'd need to create a custom validator to have that on UserApi. We're not going to worry about that right, but I wanted to point it out.

 Anyway, back over on the test, re-add the fields. Validation, check!

---
## [pascua28/android_kernel_samsung_sm8250](https://github.com/pascua28/android_kernel_samsung_sm8250)@[b7f8ff233d...](https://github.com/pascua28/android_kernel_samsung_sm8250/commit/b7f8ff233db0d44c1019fa244f0ee8b54ef4359e)
#### Thursday 2023-11-02 11:27:17 by Peter Zijlstra

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
## [cheddar-me/pbbuilder](https://github.com/cheddar-me/pbbuilder)@[c61bd2e6df...](https://github.com/cheddar-me/pbbuilder/commit/c61bd2e6dfd92ae15effdc968a3a4715bd3402d1)
#### Thursday 2023-11-02 12:49:47 by Stanislav (Stas) Katkov

Integrating collection renderer from ActionView (#43)

# Goal
We should be able to effectively render collection of data and be able to cache it.

## Problem statement
Previously, we have used following code to render collection:
```ruby
pb.cache!(@account.offers_cache_key, expires_in: 12.hours) do
  pb.featured_offers @featured_offers, partial: "offer", as: :offer

  pb.normal_offers @normal_offers, partial: "offer", as: :offer
end
```

But we need to introduce fragment caching to offers, since list cache has high miss rate. This is how implementing fragment caching in pbbuilder should look like:

```ruby
pb.cache!(@account.offers_cache_key, expires_in: 12.hours) do
  pb.featured_offers partial: "offer", as: offer, collection: @featured_offers, cached: true
  pb.normal_offers partial: "offer", as: :offer, collection: @normal_offers, cached: true
end
```

This syntax is heavily inspired by jbuilder. Here is list of examples from that gem that uses cached:  and collection: attributes.
```ruby
json.partial! partial: 'posts/post', collection: @posts, as: :post
```
```ruby
json.partial! 'posts/post', collection: @posts, as: :post
```
```ruby
json.partial! "post", collection: @posts, cached: true, as: :post
```
```ruby
json.array! @posts, partial: "post", as: :post, cached: true
```
```ruby
json.array! @posts, partial: "posts/post", as: :post, cached: true
```
```ruby
json.comments @post.comments, partial: "comments/comment", as: :comment, cached:true
```

## Proposed solution

In this PR, we're implementing more effective  rendering of collection with a help of `ActiveView::CollectionRenderer`. Support for caching of partial is currently not in the scope, but this will help implement caching and caching digest later.

Following syntax should be supported:
```ruby
pb.friends partial: "racers/racer", as: :racer, collection: @racers
```

```ruby
pb.friends "racers/racer", as: :racer, collection: @racers
```

Previous syntax works as it used to before. These will remain unchanged and will not use collection renderer (at least for now)
```ruby
pb.partial! @racer, racer: Racer.new(123, "Chris Harris", friends)
```
```ruby
pb.friends @friends, partial: "racers/racer", as: :racer
```

## TODO
- [x] Add documentation for this change
- [ ] Check performance difference between Collection Renderer and our approach. (without cache for now)
- [x] It's using PartialRenderer with rails 7 now - this seems like a bug, it should use CollectionRenderer.

## Prior work
Some inspiration for this PR could be found here:
* https://github.com/rails/jbuilder/pull/501
* https://github.com/rails/rails/blob/main/actionview/lib/action_view/renderer/partial_renderer/collection_caching.rb#L20
* https://github.com/rails/rails/tree/main/actionview collection_renderer
* https://github.com/rails/rails/blob/main/actionview/lib/action_view/renderer/partial_renderer/collection_caching.rb#L20

---
## [mozilla-mobile/mozilla-vpn-client](https://github.com/mozilla-mobile/mozilla-vpn-client)@[6bf1add73e...](https://github.com/mozilla-mobile/mozilla-vpn-client/commit/6bf1add73eb06b1bbf1c994feb7cdcde00e403e4)
#### Thursday 2023-11-02 12:59:27 by Beatriz Rizental

Enable sign in cancel button click test

Ok, this is just a bit hacky. The test was failing because that button is
below the fold. We'd have to scroll down to actually click on it. However,
I cannot figure out how to scroll down for the life of me. I talked to Matt L.
and he showed me the fun fact that if you click right on the fold without
scrolling turns out you already reach the cancel button.

Now, tests are clicking in the middle of elements. So what I did is I changed
the test to actually click at the top right corner of the element. In practice,
this makes no difference. So instead of embarking in yet another rabbit hole
to fix this, I refrained.

---
## [DETrooper/Begotten-III](https://github.com/DETrooper/Begotten-III)@[2d348ef039...](https://github.com/DETrooper/Begotten-III/commit/2d348ef039f7c151c586d11a7d33b1e7738a32a1)
#### Thursday 2023-11-02 13:13:46 by DETrooper

Sanity Update

	- Added insanity ambience.
	- Added new sanity effects.
	- Ported Begotten VR sanity hallucinations.
	- The roaches will now come for you when you're ragdolled.
	- You will no longer lose sanity in hell if you are of Faith of the Dark, instead of needing to be a member of the Children of Satan.

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[9ff9e4b9a8...](https://github.com/psychonaut-station/PsychonautStation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Thursday 2023-11-02 15:30:06 by necromanceranne

Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

## About The Pull Request

Allows for damage falloff to apply to more than just shotgun pellets.
Now any projectile can have a damage falloff defined.

Scatter Laser shells no longer use the minigun beams to determine their
damage. Instead they use the actually defined scatter laser beams. Those
beams do 7.5 damage per pellet, times by 6 pellets.

Scatter laser beams now have damage falloff, a separately defined
(positive) wounding power from normal beams, and wound falloff.

Scatter laser shells can be printed from security protolathes once you
have weapon tech.

Scatter laser shells _may_ be damaged by EMPs based on severity. The
result is that it fires a practically useless volley of laser fire. They
cause a honk sound when they hit, so you know when you've shot one of
these.

## Why It's Good For The Game

Well, we want shotguns universally to not be defined by their damage
output (especially extreme damage output) but by niche.

What does the scatter laser shell currently occupy as a niche?

The single highest damage output of any projectile weapon in direct
damage. The thing we don't want of shotguns, and it is reigning champion
of all guns.

Okay, that's a bit misleading, because obviously it is competing with
the likes of .50 BMG which does 70 damage outright and dismembers limbs,
potentially doing upwards of 90 damage if it does, and also hard stuns
people. Obviously _that_ is technically a stronger bullet.

But not for raw damage, because the scatter laser does 90 damage out the
gate, barring any potential wounding that might occur which increases
the damage multiplicatively. No gimmicks, no extra procs, nothing. It's
just 15 force lasers (with no damage dropoff) split between 6 beams.

And the reason for this is because this shell has been nerfed once prior
by making it not fire 6 normal laser shots into someone. That was 120
damage at the time, 120 to 90 was...I guess a nerf during the taser era.
Depends on how you viewed it. Buckshot was doing like 80 at the time,
believe me it was a wild period. But anyway, when we did the whole
damage rearrangement over the course of the laser few years, every other
shell got touched except this one for some reason. Even pulse slugs lost
10 damage while this was still sitting on 90 force point blank.

So what is the new niche? Well, it's laser buckshot. That's not a niche
but crew don't get buckshot, so this is their buckshot. It wounds real
good. Real goddamn good. And its is a laser. It fits the aesthetic,
obviously.

Okay, thanks.

## Changelog
:cl:
balance: Scatter laser shells actually utilize the _real_ scatter laser
beam. This comes with damage changes. And wounding power.
feature: EMPs can potentially damage scatter laser shells.
refactor: All projectiles can now have damage falloff defined. Yay.
balance: Scatter laser shells can be printed when weapons technology is
researched.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[071f6063e6...](https://github.com/psychonaut-station/PsychonautStation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Thursday 2023-11-02 15:30:06 by carlarctg

Adds charges to omens and omen smiting. Reduces omen bad luck if nobody's nearby. (#78899)

## About The Pull Request

refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.

qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)

fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.

## Why It's Good For The Game

> refactor: Adds charges to omens and omen smiting rather than only
being permanent or one-use. Mirrors now grant seven bad luckers.

Allows for someone to get between 1-infinity omen accidents. Seriously
why wasnt this a thing before

> qol: Reduces omen bad luck if nobody's nearby.

I LOVE this quirk, but trying to do antything at all except 'Suffer
Miserably' is nigh impossible. To alleviate life a little, making it so
that you have a lesser chance of suffering misfortune if nobody's around
will be the perfect compromise. It makes life easier but doesn't
compromise funny moments.

Any client in viewrange will disable the reduction. This includes
ghosts.

## Changelog

:cl:
refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.
qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)
fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud)@[f2b128f972...](https://github.com/ubicloud/ubicloud/commit/f2b128f972ce81847956e386d626bd9a94c0106e)
#### Thursday 2023-11-02 15:43:07 by Daniel Farina

Introduce Clog

a.k.a. CLover LOGging.  Also there often can be too many logs, which
evokes a the other meaning of the word clog.  Expansion of meaning to
the type of shoes is an exercise for the reader.

You would use it like this:

    # Strand ubid gets included in metadata automatically
    Clog.emit("A message")

And like this, when you have metadata:

    Clog.emit("A message") { { my_metadata_name: { field1: ..., field2: ... } } }

I also add logging in a few places.

There are some general ideas that I'm combining from years past with
Clog, in no particular order:

1. The message component is almost always static

   It's much easier to search source code and perform log system
   queries if the log message is a static string, and dynamic
   information is in metadata.

   Inspiration: exception aggregating systems are more reliable when
   the Exceptions have messages that do not embed dynamic text.

2. Use thread local variables for automatic log enrichment.

   At first, I used real thread local variables, but changed this to
   use `Thread.name`, which can improve thread debug rendering as well
   as being usable to enrich logs.  If we add more metadata to enrich
   logging output, I suggest use of Thread local variables set by the
   Dispatcher or Strand framework code.

   A nice consequence of this is that simple log messages that only
   want to include the UBID of what is being operated upon can obtain
   this by logging a static message only.

   Inspiration: systemd and syslog both perform automatic enrichment
   with at least PID, and in the former case, with unit names and
   other data, without any special considerations by the application
   emitting output.  And it's pretty useful.

3. Use (mostly) a single hash for metadata, with a unique-ish name.

   Instead of doing something like:

        { a_field: "data", b_field: "more data" }

   Do:

        { going_concern: { a_field: "data", b_field: "more data", magnitude: 7 } }

   This is informally a kind of type information, useful in queries,
   such as this one written in Mezmo/LogDNA format:

        going_concern.magnitude:>3

   Which is a lot more selective than:

        magnitude:>3

   Often, this is desirable, unless "magnitude" was a idiom throughout
   the entire application (as `ubid` and `Thread#name` is for us,
   already an exception to this guideline).

   Permissible aberrations can be expected in the case of idiomatic
   representations used in many log records.  Then you might have
   something like:

        { well_known_metadata_or_representation_name: { ... },
          going_concern: { a_field: "data", b_field: "more data" } }

   Inspiration: the defunct logging service "Timber" suggested this
   style, and it seemed like a pretty good idea after using it for a
   while.

4. Use blocks to compute dynamic fields for logs.

   `Clog.emit` takes a block that should yield the metadata included
   with the log line.  There are two reasons I want to experiment with
   using blocks to do this:

   (a) It contains the code that exists for logging when it is not as
       trivial as a single expression in a hash literal.

   (b) In event we do the typical DEBUG/INFO/WARN levels, you can
       avoid calling the block.  However, that is not implemented
       here, because I'm not sure if it's necessary.

   Inspiration: the Crystal programming language does this, and in
   their case, it's even more powerful, since "DEBUG" code can be
   stripped at compile time if a release build is set.

5. Support JSON output

   LogDNA (now known as Mezmo) had some useful heuristics of trying to
   parse anything that looked like JSON as JSON, but also storing
   non-JSON output.  This is useful when, say, Ruby core dumps and
   prints a bunch of output: at least you can see it happened and
   piece things together.  Or if a library emits a `puts`.  But, when
   we have the wherewithal, and we think the output log is going to a
   system that can parse JSON, we should emit JSON.

   Left un-done in this patch is some heuristics to have more
   human-friendly rendering of logs when, for example,
   `$stdout.isatty` is true.  That's for later.

---
## [LadyDefile/Wordsmith-DalamudPlugin](https://github.com/LadyDefile/Wordsmith-DalamudPlugin)@[9c1144d05a...](https://github.com/LadyDefile/Wordsmith-DalamudPlugin/commit/9c1144d05a8a3416824da10aca9d36299f671d6c)
#### Thursday 2023-11-02 15:52:13 by LadyDefile

Merge branch 'Statistics' into Fucking-Stupid-Shit

---
## [LadyDefile/Wordsmith-DalamudPlugin](https://github.com/LadyDefile/Wordsmith-DalamudPlugin)@[0c6ab1470d...](https://github.com/LadyDefile/Wordsmith-DalamudPlugin/commit/0c6ab1470d3841081ef174cb74a22764f8eed308)
#### Thursday 2023-11-02 15:52:42 by LadyDefile

Merge pull request #48 from LadyDefile/Fucking-Stupid-Shit

Update

---
## [piscesmk2013/frameworks_base](https://github.com/piscesmk2013/frameworks_base)@[49ed3b2e7f...](https://github.com/piscesmk2013/frameworks_base/commit/49ed3b2e7f708c1f95528dcf2b723b8d2f797605)
#### Thursday 2023-11-02 15:54:01 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [A-Safe/casa-bosl-soc](https://github.com/A-Safe/casa-bosl-soc)@[3e243ee5a8...](https://github.com/A-Safe/casa-bosl-soc/commit/3e243ee5a80fc0c67408a83ce7dd5d3199734a41)
#### Thursday 2023-11-02 16:38:17 by Filip Grocholski

0.0.3

The past 2 weeks have been shitty for my productivity as I've been not only physically sick but also mentally unwell, sorry.
Anyway...
I've finally managed to unify knexHelper's codebase under one universal repo so there are no multiple versions across all the servers that utilise it.
Summary of changes:
- 2 new types of queries have been added to customQueryBuilder() LIMIT and ORDER.
- filterQueries file has been added which contains functions that emulate loopback's filter system and translate the filter queries to be executed as customQueries.
- test folder has been added, currently contains only tests for convertFilterToCustomQuery().
- DEBUG property has been added to knexHelper.

---
## [FairfirFarlander/Equestria-Divided-Reunification](https://github.com/FairfirFarlander/Equestria-Divided-Reunification)@[c2a5a416b2...](https://github.com/FairfirFarlander/Equestria-Divided-Reunification/commit/c2a5a416b2219cee44f754a5f23b7e0006efb618)
#### Thursday 2023-11-02 16:41:50 by FairfirFarlander

20231102 (11AM CST) - 2.2.1.1 Bump and TFL

### 2.2.1.1 Bump
- Added more PLB cosmetic tags. =_=
- Changed notes for certain provinces.
- Turned Little Dove Fields into a rural province from a town.
- Same as above for Sierrra Caballo along with a reduction of VP by 5.
- Changed Tricorn to rural which is subject to reversion by us.
- Noted change to Bluebell Fields. Fuck you this is the HSW capital.
- The mountain in the dragon lands got nerfed again. We noted it, but left it alone.
- Minor countrytechtreeview tweaks to... subtitles?
### TFL
- Added a bookmark description for the TFL.
- Tweaked the opening screen for TFL.
- Changed the ideology and party names for TFL.
- Removed the test descriptions from TFL.
- Changed the pony general names for TFL.
- Finished the TFL tree.

---
## [Mayaeeee/simplesite-](https://github.com/Mayaeeee/simplesite-)@[adf42c37b2...](https://github.com/Mayaeeee/simplesite-/commit/adf42c37b20cfa2be1597c714a627e3e5886eb3a)
#### Thursday 2023-11-02 17:17:04 by Mayaeeee

Changed I am an Associate Professor of Marketing at the University of Northern Colorado where I research and teach in the areas of consumer psychology and digital marketing. I enjoy spending time with my family, biking, traveling, and learning about new languages and cultures to Maya Eaton is currently a business major with an emphasis in marketing at the University of Northern Colorado. She loves spending quality time with her family and friends. Maya is proud of her Pakistani heritage and culture. In her free time, she enjoys traveling and doting on her pet cat named Kakashi. After graduation, Maya hopes to secure a marketing position that allows her to apply her education and experience while making a positive difference in her community. She is a driven, compassionate and outgoing young woman who is excited for the future and all the opportunities it holds.

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[c0de4cf883...](https://github.com/kleinerm/Psychtoolbox-3/commit/c0de4cf883d7d002884d51f772ef52aef34b0e91)
#### Thursday 2023-11-02 17:25:21 by Mario Kleiner

PsychOpenXR: Add initial eyetracking via HTC SRanipal.

Requires SRAnipalMex to work and on the path, otherwise standard OpenXR eyetracking is
used. The mex file and source code is not yet included in the Psychtoolbox distribution.

This works with and requires the HTC proprietary SRanipal eye tracking api for MS-Windows,
in combination with a supported HTC HMD, e.g., HTC Vive Pro Eye (tested) or HTC Vive Cosmos
or HTC Vive Focus 3 with eye tracker hardware extension, the latter two untested, but assumed
to work in the same way.

It allows binocular eye tracking for left and right eye separately, returning two separate eye
gaze samples. Additionally a 3rd combined "cyclops eye" sample is returned, which is the fusion
or average of the two eye gaze samples, similar (identical?) to what HTC's implementation of
the OpenXR XR_EXT_eye_gaze_interaction extension returns as sole eye pose.

Implementation notes:

While OpenXR eye tracking with the standard OpenXR extension only works with a maximum
sampling rate of 60 Hz, ie. blocking the calling code for approximately 16 msecs for each
query in PsychVRHMD('PrepareRender') or PsychOpenXRCore('GetTrackingState', ..., 4), this
works with up to native sampling rate of the eyetracker, in this case 120 Hz / one sample
every approximately 8.3 msecs. As it turns out, one needs to use the callback api to get max
rate and minimum latency/overhead, where our callback is called from SRanipals own thread.
With the non-callback api's it is always blocking calls with 16 msecs+ duration resulting in poor
performance. The latter seems to be what HTC's implementation of OpenXR eyetracking does.

The HTC proprietary api delivers more detailed info than current official OpenXR extensions,
so both from a performance perspective and richness of information perspective it is clearly
perferrable to use the HTC proprietary api when available on a HTC HMD. The quality of the
api docs is horrifying however, and often faulty, so using it is somewhat a pain in the ass.

The type and units of returned information from SRanipal is different from what OpenXR
returns or uses, so some hacks had to be used to sort-of convert to OpenXR compliant format.

Currently the raw gaze samples are not 7 component vectors with eye position (x,y,z) and
orientation quaternion (rx,ry,rz,rw), but only 6 component vectors with orientation encoded
differently, and some shady matrix math hacks to get a sort of usable / sort of ok'ish gazeMat
matrix for eyegaze out of it. From that we derive other info like global gaze matrix, 3D eye
gaze vectors and 2D (x,y) gaze sample positions the usual way via the code shared with
regular OpenXR gaze tracking.

Some oddities - the reason for these is totally unclear:

- We need to switch some signs in the math - Is it a bug in HTC's runtime? A feature? A quirk?
I don't know.

- Eye center of the left eye seems to be stored in right eye, and vice versa, but the end result
wrt. 2D gaze position is the same, and the 3D gaze vectors originate in puzzling locations but
point to and converge in the correct gaze location. Again, could not find out why.

---
## [Mayaeeee/simplesite-](https://github.com/Mayaeeee/simplesite-)@[9ef550b452...](https://github.com/Mayaeeee/simplesite-/commit/9ef550b4525ca9adc756075b8f495d513b9bc5f3)
#### Thursday 2023-11-02 17:43:13 by Mayaeeee

 changed  Classes I have taught include Consumer Behavior, Marketing Research and Analysis, Web and Digital Ad Analytics, and Digital Advertising. My teaching philosophy is centered around providing students with both theory and hands-on experience in the latest marketing trends and technologies. I strive to provide a positive and supportive learning environment in the classroom. Relevant marketing technologies I teach include Google Analytics, Google Tag Manager, Google Data Studio, Google Search and Display Ads, Tableau, JASP, HTML/CSS, and Qualtrics. to After graduating, I hopes to begin a career in marketing and digital marketing. My specific interest is in applying her skills to the medical field. I am passionate about healthcare and hopes to help hospitals, pharmaceutical companies, or medical device manufacturers market their services and products. Is interested in developing social media campaigns to promote new treatment options and innovations in healthcare technology. I wants to work on digital marketing strategies like SEO, paid search ads, and content marketing for medical companies. My goal is to use my marketing expertise to help improve patient education and access to healthcare resources. Most importantly, I want to make a positive impact in the medical field through effective branding, messaging, and outreach using my skills in marketing and digital marketing.

---
## [pauldevine/mame](https://github.com/pauldevine/mame)@[b17bd90268...](https://github.com/pauldevine/mame/commit/b17bd90268aa6b970b96efcfe4f52040434b000f)
#### Thursday 2023-11-02 17:59:57 by wilbertpol

msx2_cart.xml: Added 31 items, 29 working. (#11642)

* msx2_cart.xml: Added 31 items, 29 working.

New working software list items
-------------------------------
Aleste (Woomb) [file-hunter]
Arkanoid 2 (Korea) [file-hunter]
Ashguine - Fukushuu no Honoo (Japan, alt 2) [file-hunter]
Daisenryaku MSX2 (Japan, alt) [file-hunter]
Gekitotsu Pennant Race 2 (Japan, sample) [file-hunter]
Hydlide 3 - The Space Memories (Woomb) [file-hunter]
Alien 8 Remake [file-hunter]
Los Amores de Brunilda (v1.01) [file-hunter]
Los Amores de Brunilda (v1.0) [file-hunter]
Barbarian the Duel [MSXdev]
Bomb Jack [file-hunter]
Bomb Jack (alt) [file-hunter]
Booming Boy (demo) [MSX Area]
Bubble Dream [MRC Tenliner Challenge]
DIM X (demo) [file-hunter]
Equivocal (v1.5) [Passion MSX2 Contest]
Equivocal (v1.0) [Passion MSX2 Contest]
Gold Fan [N.I]
Highway Fighter (demo) [file-hunter]
Inferno [msxdev Compo]
Jailbreak (v1.02) [Passion MSX2 Contest]
Jailbreak (alt) [Passion MSX2 Contest]
Jailbreak (alt 2) [Passion MSX2 Contest]
Knight Lore Remake [Retroworks]
Lilly's Saga - The Stones of Evergreen (v1.2) [MSXdev]
Lilly's Saga - The Stones of Evergreen (v1.1) [MSXdev]
Lilly's Saga - The Stones of Evergreen (v1.0) [MSXdev]
La Sorpresa (Spanish) [Oniric Factor]
A Surpresa (Portuguese) [Oniric Factor]

New NOT_WORKING software list additions
------------------------------------------
Ehagaki-yō wāpuro (Japan) [file-hunter]
Life on Earth (demo) [file-hunter]

* Fix capitalisations of Wāpuro and AshGuine

---
## [JJ-Rogers/zechub](https://github.com/JJ-Rogers/zechub)@[0d97121c8c...](https://github.com/JJ-Rogers/zechub/commit/0d97121c8ca6106c2c829f5b8f47679d1801a3f1)
#### Thursday 2023-11-02 18:27:20 by TonyAkinsWritesCrypto

ZecWeekly66

# ZecWeekly (Episode 66)


The Zebra book, Zcash enhanced privacy, ZecHub Extras, Zcash 7th Anniversary , Ywallet Upgrade. 


Curated by "TonyAkins"[TonyAkin01](https://twitter.com/TonyAkins01))

---

#### Welcome to ZecWeekly Episode 66


Welcome to the thrilling episode of ZecWeekly, as we explore Zcash's implementation of FROST using Schnorr , Zcash 7th Anniversary celebrated with lots of merches and prizes, release of Zebra updated 1.3.0, and the introduction of UniFFi for Developer's use cases. 

–
### This Week Education's Pieces.

This week's education pieces will educate and refine us with all details about Zcash addresses, both shielded and transparent addresses and other the latest development in the Zcash payment system. 

Click  the link below to access the resource :

https://wiki.zechub.xyz/visualizing-zcash-addresses




### Zcash Updates

Zcash and ECC updates. 

[NowNodes features Zcash for upgraded Privacy ecosystem](https://twitter.com/NOWNodes/status/1716463761777680713)

[Ywallet Zcash Ledger app on Nano S Plus w/ Orchard tx](https://www.youtube.com/watch?v=HRVNpDDoh1Y&t=34s) 

[Zcash Digitals Decentralized](https://twitter.com/ElectricCoinCo/status/1717570088771952811)

[tECC DAYS 2023 celebrated](https://twitter.com/ECCIntegrator/status/1718035043736547504)


[Announcing Zebra 1.3.0](https://twitter.com/ZcashFoundation/status/1716524342853476576)

[Implementation of UniFFi on Zcash Network](https://twitter.com/eiger_co/status/1716801431510851824)

[Zcash SDK fixes now live](https://twitter.com/EdgeWallet/status/1716530980499128578)

#### Zcash Community Grants Updates

[WalletD Community Grant Application](https://forum.zcashcommunity.com/t/walletd-community-grant-application/45876?utm_source=dlvr.it&utm_medium=twitter)

[Security assessment for Zcash FROST published](https://twitter.com/ZecHub/status/1716930299140169764)

[Zcash Community funded @eiger_co to create UniFFi library](https://twitter.com/ZcashCommGrants/status/1717273970922123392)

#### Community Projects

[Zcash 7th Anniversary celebrated in grande style](https://free2z.cash/ZecHub/zpage/zcash-7th-anniversary-challenge)

[Post Comments on Free2Z using Zenith CLI! Go check it out!](https://www.youtube.com/watch?v=HtorP8TJ5vk)

#### News & Media

[Binance founder CZ’s fortune gets slashed $12B, while SBF is still at $0](https://cointelegraph.com/news/binance-ceo-changpeng-zhao-fortune-slashed-billionaires-index)

[Google to invest another $2B in AI firm Anthropic: Report](https://cointelegraph.com/news/google-to-invest-another-two-billion-in-ai-firm-anthropic)

[Kraken to suspend trading for USDT, DAI, WBTC, WETH, and WAXL in Canada](https://cointelegraph.com/news/kraken-suspend-trading-usdt-dai-wbtc-weth-and-waxl-stablecoin-canada)

[AI Girlfriend Amouranth Wants to Use Her 'Vaginal Yeast' to Brew Beer](https://decrypt.co/203517)

[Audits and rug-pulled projects, a $650B token burn, and major DeFi protocol quits UK: Finance Redefined](https://cointelegraph.com/news/audits-and-rug-pulled-projects-a-650b-token-burn-and-major-defi-protocol-quits-uk-finance-redefined)

[Bitcoin's 14% Weekly Gain Signals 'End of an Era' as Big Tech Dumps, Analyst Says](https://www.coindesk.com/markets/2023/10/27/bitcoins-14-weekly-gain-signals-end-of-an-era-as-big-tech-dumps-analyst-says/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[Binance Founder CZ's Wealth Falls About $12B as Trading Revenue Slumps: Bloomberg](https://www.coindesk.com/business/2023/10/27/binance-founder-czs-wealth-falls-about-12b-as-trading-revenue-slumps-bloomberg/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[How major German firms like Mercedes and Lufthansa are using NFTs](https://cointelegraph.com/news/germany-mercedes-lufthansa-nfts)

[ChatGPT creator OpenAI builds new team to check AI risks](https://cointelegraph.com/news/chatgpt-openai-new-team-ai-risks)

[Bitcoin restarting 2023 uptrend after 26% Uptober BTC price gains — research](https://cointelegraph.com/news/bitcoin-2023-uptober-btc-price-research)



## Some Zcash Tweets


[Central bank of Brazil account heard about Zcash today](https://x.com/anarchychains/status/1717288641288921272)

[Happy Birthday Zcash!!!](https://twitter.com/ZforZcash/status/1718085318543376404)

[ZcashFoundation and NCCGroupInfosec conduct a security assessment of the Foundation’s FROST](https://twitter.com/ZcashFoundation/status/1716849796315512935)

[What are Zero-knowledge Proofs](https://twitter.com/NighthawkWallet/status/1717730883933806958)

[Zcash Community Grant minutes](https://twitter.com/ZcashCommGrants/status/1717556482344907090)

[Keep yourself safe from hack with a Zcash wallet](https://twitter.com/NighthawkWallet/status/1717007699592851702)

[Metrics should be updated](https://twitter.com/ZcashForum/status/1716786643171225726)

[Join our UPA friends if you're at EFDevconnect](https://twitter.com/ElectricCoinCo/status/1716886693444530195)


[Social media Data collection, does it matter?](https://twitter.com/ZecHub/status/1716850588942577890)

[Follow NighthawkWallet for crypto privacy education](https://twitter.com/NighthawkWallet/status/1716625185623728248)

[Privacy is normal!](https://twitter.com/ZcashNigeria/status/1716755151497707660)


## Zeme of the Week

[https://twitter.com/ZcashNigeria/status/1718151545324200002](https://twitter.com/ZcashNigeria/status/1718151545324200002)

[https://twitter.com/zcashbrazil/status/1717609507432337754](https://twitter.com/zcashbrazil/status/1717609507432337754)

[https://twitter.com/zcashbrazil/status/1717225798019567621](https://twitter.com/zcashbrazil/status/1717225798019567621)



## Jobs in the Ecosystem

[Zcash needs graphic designers,writers, and privacy advocate in its ecosystem](https://twitter.com/ZecHub/status/1713947885220344234)

[Create Video HOWTO - Setup WSL in windows, and compile lastest zcashd](https://github.com/ZecHub/zechub/issues/567)

---
## [AkihiroSuda/passt-mirror](https://github.com/AkihiroSuda/passt-mirror)@[ee58f37db0...](https://github.com/AkihiroSuda/passt-mirror/commit/ee58f37db060535bee298bc98f61497eac37f152)
#### Thursday 2023-11-02 18:48:24 by Stefano Brivio

test: Add Podman system test with bats for pasta

Ugly as hell, but we keep breaking things otherwise, and I keep
forgetting to run this manually (as long as it's based on my local
Podman setup, that's the only alternative).

We need to clone the Podman repository as distribution packages don't
contain test scripts, typically. While at it, build the latest
version which is what really matters.

As we're planning anyway to revamp the test framework, I'd be
inclined to just add this without too many thoughts, and have it as
a nice-to-have requirement reminder for the new framework.

Link: https://github.com/containers/podman/pull/19699
Suggested-by: Paul Holzinger <pholzing@redhat.com>
Signed-off-by: Stefano Brivio <sbrivio@redhat.com>
Reviewed-by: David Gibson <david@gibson.dropbear.id.au>

---
## [claudio-walser/storganizer](https://github.com/claudio-walser/storganizer)@[78d0a0bbe2...](https://github.com/claudio-walser/storganizer/commit/78d0a0bbe2ed245927f305c5a763feb52e6f022f)
#### Thursday 2023-11-02 19:00:15 by Claudio

Holy shit, remembers me why I dont like this stuff

---
## [needtoday/self-development](https://github.com/needtoday/self-development)@[93fe93d909...](https://github.com/needtoday/self-development/commit/93fe93d9093175436ccb10f045d73ee58c6df2d0)
#### Thursday 2023-11-02 19:09:25 by needtoday

Update README.md

Needtoday Institute is offering courses in CBSE Class 9 – 12 Maths & Science Digital Marketing & Branding and Marketing Platform from Needtoday.com where we create and execute unique Digital Marketing strategies for each customer to create their online presence, build their Digital brand, grow their business online and achieve their marketing goals.
Understanding Holistic Healing: Mind, Body, and Spirit

Holistic healing is founded on the belief that optimal health requires a balance between the mind, body, and spirit. It emphasizes the interconnectedness of these aspects and the influence they have on each other. Depression, often stemming from a combination of psychological, physiological, and emotional factors, can benefit from holistic approaches that address the person as a whole.

Mindful Meditation and Mind-Body Connection

Mindful meditation is a cornerstone of many holistic approaches. By cultivating mindfulness, individuals can become more attuned to their thoughts and feelings, fostering self-awareness and self-acceptance. Meditation not only helps manage stress and anxiety but can also alleviate symptoms of depression. Regular practice has been shown to promote positive changes in brain structure and function, enhancing emotional regulation and reducing the recurrence of depressive episodes.

Nutrition for Mental Well-being

The saying "you are what you eat" holds true in the realm of mental health as well. A balanced and nutrient-rich diet can have a profound impact on mood and cognitive function. Omega-3 fatty acids, found in fatty fish, flaxseeds, and walnuts, have been linked to a reduced risk of depression. Additionally, foods rich in antioxidants, such as fruits and vegetables, can help combat oxidative stress, which has been associated with depression.

Physical Activity as a Mood Enhancer

Regular exercise is not only beneficial for physical health but also plays a significant role in mental well-being. Engaging in physical activity releases endorphins—natural mood lifters—while also reducing stress hormones. Whether it's a brisk walk, a yoga session, or a dance class, finding an enjoyable form of exercise can contribute to a more positive outlook and help alleviate symptoms of depression.

Holistic Therapies: Acupuncture and Herbal Remedies

Holistic therapies like acupuncture and herbal remedies have been used for centuries to restore balance within the body. Acupuncture, an ancient Chinese practice, involves inserting thin needles into specific points on the body to stimulate energy flow. It is believed to release blocked energy and promote emotional healing. Similarly, certain herbal supplements, such as St. John's Wort and saffron extract, have shown promise in managing mild to moderate depression. However, it's important to consult a healthcare professional before incorporating herbal remedies into your routine, as they can interact with medications.

Cultivating a Supportive Lifestyle

Holistic healing extends beyond individual practices to encompass the broader aspects of life. Building a supportive network of friends, family, and mental health professionals can be invaluable in the journey toward healing. Engaging in creative pursuits, spending time in nature, and practicing gratitude can contribute to a positive mindset and help counteract the negative thought patterns associated with depression.

In Conclusion

Overcoming depression is a multi-faceted journey that requires a comprehensive approach. Holistic healing recognizes the intricate connections between the mind, body, and spirit, offering a range of tools to support individuals in their quest for well-being. While holistic approaches can be powerful complements to traditional treatments, it's important to remember that depression varies from person to person. Consulting with mental health professionals is essential to create a personalized and effective healing plan.

ALWAYS BE HAPPY Program 
Online Spiritual Program for Self Development

Always Be Happy Program is a simple spiritual discipline, which combines Gratitude, Prayer, Meditation and Serving the Lord for your self-development and well being, leading to a life filled with Joy
Price: ₹ 99/-
Buy Now: https://bit.ly/43HFBnm
Program Access: 
Download Needtoday.com INSTITUTE APP on Android by clicking  (https://bit.ly/3DuJVf1). For IOS: Download MyInstitute APP by clicking (https://apple.co/3Qc6NHx) and enter MPMYQ as Org code
Remember, healing from within takes time and patience. By embracing holistic approaches, individuals can empower themselves to take an active role in their mental health journey and work toward a brighter and more balanced future.

---
## [facebook/flow](https://github.com/facebook/flow)@[d25d3a87e5...](https://github.com/facebook/flow/commit/d25d3a87e5b7df204f9fc038905e36d81dfd929e)
#### Thursday 2023-11-02 19:11:35 by Sam Zhou

[flow][tools] Use hermes-parser for flow-remove-types

Summary:
This is the last dependency of flow-parser in our yarn workspaces. I want to get rid of dependency on flow-parser so we can yarn install without a build step. We just don't get enough dogfooding value out of it to justify the build pain.

This diff switches to use hermes-parser instead of flow-parser. I still kept the same sketchy string manipulation based "transpilation", but eventually we should just kill the tool and recommend babel register, so I didn't bother to turn it into something better.

I did add one hack for `%checks` by looking ahead one token to remove `:` as well. Previously panagosg7 worked around it by making the location of InferredPredicate include `:` as well. I'm not that interesting in making the change in hermes-parser, since people should just use type guards.

Changelog: [internal]

Reviewed By: panagosg7

Differential Revision: D50915858

fbshipit-source-id: 18742c657602477020173f288337aaad8aad08bb

---
## [MysteryMan21333/TerraGov-Marine-Corps](https://github.com/MysteryMan21333/TerraGov-Marine-Corps)@[fb4899d20e...](https://github.com/MysteryMan21333/TerraGov-Marine-Corps/commit/fb4899d20e990a0a65b8cb5b0ad19b1ef9ab083e)
#### Thursday 2023-11-02 19:50:34 by KM-Catman

Slight redesign of Valhalla Vendors and Chemistry. Adds FC and Synth to Valhalla. (#13612)

* Valhalla Fixes

Start room is now all Hulls, adds a Friend, Materializes the Chaplain's chained demon, and adds more Xeno Huds.

* FC and Synth Added. Slight readjustment.

* Changed the vendor section as per Grayson's request

* Adds three new Warning Stripes.

Adds a FCDR, Synth, and Mech warning stripe. Adds them in front of the prep rooms

* Duct Taped Space

* Removed random bedsheet (Goddamn you hotkeys)

---
## [artimaus/nationgen](https://github.com/artimaus/nationgen)@[0c9dc417c3...](https://github.com/artimaus/nationgen/commit/0c9dc417c3b2eab6f9ec4207290f28efec775722)
#### Thursday 2023-11-02 19:57:21 by geepope

Sacred balance changes, new filters

Slightly increased weighting of filters over stat increases.
Expanded filter selection to be somewhat less picky about trying to get exact power values.
Overly fragile sacreds tend to get bonus defense, gold discounts, and are more likely to be rec-anywhere.
Weak/cheap rec-anywhere sacreds do not receive as much cost penalty as before.
Added a number of new sacred filters.

Filter balance changes:
Decreased power budget of basic stealth.
Increased power budget of blanket stat increase.
Increased levels of fireshield (fireshield 2/4 is just too low to do much.) Increased power budget of higher levels of fireshield to compensate.
Added extra shock resist to stormpower.
Increased power budget of recuperation. It's an incarnate bless and a pretty good one.
Decreased power budget of season-power (these are zero-sum modifiers and are not really a net advantage.) Also decreased probabilities of season-power.
Increased power budget of the higher level of turning year power (this is *not* a zero-sum modifier, so the higher level is strictly more powerful than the lower level.)
Decreased extra gold cost on darkness power, it's a niche effect that requires considerable investment to get use of outside of cave provinces.
Decreased extra gold cost on awe/sun awe. It's only particularly useful against low morale troops and quickly loses relevance, and vanilla sacreds are allowed it without too much cost.
Decreased extra gold cost on glamour, but also weighted it against heavy armor, and against very low defense (where it is too expensive) and very high defense (where it is too good.)
Increased power budget of ethereal.

---
## [mondrake/symfony](https://github.com/mondrake/symfony)@[af44385d9e...](https://github.com/mondrake/symfony/commit/af44385d9e6eba77b4bf4610231ce9569bdcc9b5)
#### Thursday 2023-11-02 20:02:55 by Robin Chalas

feature #50754 [HttpKernel] when configuring the container add services_{env} with php extension  (helyakin)

This PR was merged into the 6.4 branch.

Discussion
----------

[HttpKernel] when configuring the container add services_{env} with php extension

| Q             | A
| ------------- | ---
| Branch?       | 6.4
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | none
| License       | MIT

Hello the community

This is my first PR attempt.

So after reading this [documentation](https://symfony.com/doc/current/service_container.html#remove-services) and unsuccessfully trying to load my `service_test.php`, I've noticed that the `configureContainer(..)` function in the `MicroKernelTrait` file was not configured to automatically load this file.

So either we should fix the documentation, either we should fix the configuration.

Since this the [framework-bundle](https://github.com/symfony/framework-bundle) is backed by [Alximy](https://alximy.io) I figured it would be cool 😎 to try and fix 🐛 the configuration.

Anyway share me your thoughts about what should be done !

And I wanted to say that php service configuration is 🔥 so shoutout to the one who did this (I think it's you `@nicolas`-grekas with this [PR](https://github.com/symfony/symfony/pull/23834) right ? 💪🏻)

Also big thanks to `@jeremyFreeAgent` for debugging this with me and `@HeahDude` for showing me the php service configuration PR.

Commits
-------

4aac1d9fee :bug: (kernel) when configuring the container add services with php ext

---
## [ritchiae/crawl](https://github.com/ritchiae/crawl)@[9db281c723...](https://github.com/ritchiae/crawl/commit/9db281c7239a55fb109428ccad75eac9b04e15ee)
#### Thursday 2023-11-02 21:16:15 by DracoOmega

Change Hexslinger starting spells

The new spell list is:
 -Jinxbite
 -Sigil of Binding
 -Inner Flame
 -Cause Fear
 -Dimensional Bullseye

Hexslinger was always troubled. Its spellbook was split across multiple
schools, making them tricky to cast, and they still didn't do much without
ALSO training ranged weapons heavily. Slow was often a trap and in
general the archetype was clunky, without providing sufficient benefit for
splitting your skills between weapons and spells.

The intent of this change is to provide a smoother curve of castable
spells, and more immediate value to training hexes instead of simply
ignoring them in favor of being a 'worse hunter'.

Jinxbite provides a little immediate power to help deal with earlygame
threats with which current hexslinger often struggles significantly.

Sigil of Binding provides powerful utility and can help set up Inner Flame
triggers in a way that the old spellset could almost never safely do in
practice.

Portal Projectile was always a spell that was far better late than it was
early, and so Dimensional Bullseye is now a capstone that provides
even stronger long-term value, but with other easier to cast spells that
let you bridge the gap to it better.

Cause Fear was always good (if you could manage to survive long enough
to have access to it!) and remains untouched.

(Also give them 1 starting level of Fire Magic, to help just a little bit
with getting Inner Flame off the ground)

---
## [MoonTricks/crawl](https://github.com/MoonTricks/crawl)@[34c7ba284f...](https://github.com/MoonTricks/crawl/commit/34c7ba284f62950488e3860eb4499ce7605a6146)
#### Thursday 2023-11-02 21:16:36 by Nicholas Feinberg

Retheme: hand crossbow -> hand cannon (Sastreii, hellmonk)

Hand crossbows are intended to be a rare, high-tier one-handed range
weapon, similar to eveningstars or double swords. However, the name
and theme hasn't conveyed this well to players. People reasonably ask:
wait, wasn't this a starting weapon? And: how come a hand crossbow
does as much damage as a two-handed arbalest?!

So, retheme them. Hand cannons are alchemical weapons that douse bolts
in magical powders to send them screaming forth. (E.g. by causing the
bolts to fall forward instead of down, bewitching them into a fatal
attraction with their target, etc, etc.) They also belch smoke when
fired, for theme reasons (this might need to be toned down) and are
extra noisy. They're otherwise identical to hand crossbows.

It's a bit silly, but crawl has triple swords and triple crossbows,
so it seems within bounds for tone. Let's try it out!

Tiles by Sastreii, original suggestion from hellmonk.

---
## [kamrunnahar22/Kamrun-Nahar](https://github.com/kamrunnahar22/Kamrun-Nahar)@[f27c72cf14...](https://github.com/kamrunnahar22/Kamrun-Nahar/commit/f27c72cf147db29f4b050b2c36de5b99930ce82f)
#### Thursday 2023-11-02 21:22:03 by kamrunnahar22

Social Media Marketing Manager | Instagram | Facebook | TikTok | YouTube

⭐⭐ Welcome to my profile! ⭐⭐

If you want to gain an edge over your competitors and achieve growth in your business, I can help you do so by increasing your brand awareness. As your Social Media Manager, I will implement a comprehensive brand awareness strategy that puts your business in front of your target audience, fosters a deeper connection and builds trust, setting you apart from your competitors.

With over 4 years of experience managing social media accounts of professionals and public figures across various niches, I have honed my skills and kept abreast of the latest trends in the industry. My dedication to helping businesses and entrepreneurs with brand strategy and social media marketing sets me apart from the rest.

📌Here's what sets me apart as a social media manager:

🚀 Manages multiple social media accounts for different brands simultaneously, ensuring consistent engagement and growth.

🚀 Collaborated with design, content and ad copy teams to optimize campaign results.

🚀 Executed digital-first campaigns, integrating traditional brands with significant print presence

🚀 Successfully executed influencer marketing campaigns across a wide range of niches.

🚀 Combined graphics design and social media management skills for enhanced brand impact.

🚀 Ran targeted campaigns on Facebook and Instagram.

🚀 Instagram, TikTok, Facebook and Twitter, Reddit are organically grown.

🚀 Created viral campaigns that resonated with target audiences and received recognition from industry experts.

📌When you hire me as your social media manager, you can expect:

🎯 Content creation

🎯 Graphics Design

🎯 Instagram management

🎯 Facebook account management

🎯 LinkedIn Account Management

🎯 Twitter account management

🎯 TikTok account management

🎯 Pinterest account management

🎯 Niche hashtag research

🎯 Reddit Promotion

🎯 Organic leaf growth

🎯 Increase engagement and traffic

🎯 Weekly content calendar

🎯 Instagram and Facebook ads

🎯 YouTube Subscribe & View

🎯 SEO and increased visibility

🎯 Social media analysis and reporting

🎯 Community Management.

☑️ I use a range of industry-leading social media management tools including Microsoft Office, Google Suites, Notion, Hootsuite, Buffer, Tailwind, Canva, Slack, Meta Business Suite, and others to streamline my work and increase efficiency.

✅ When you choose to work with me, you can expect personalized attention, open communication, and an unwavering commitment to helping you achieve your goals. I am dedicated to exceeding your expectations and ensuring your social media presence is strong and impactful.

Ready to take your social media game to the next level? Send me a message with all the details about your brand and let's discuss your project further

I am eager to cooperate with you and contribute to your success!

Regards,
Kamrun Naher

---
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[a32fdee38c...](https://github.com/LumberKing/Tianxia/commit/a32fdee38c8f84298bdd77d7cf452999b63e6574)
#### Thursday 2023-11-02 22:23:46 by Silversweeper

Misc improvements, some artefact work, bugfixes

- Norse characters will no longer encounter suspected Odins when hunting if the Allfather is considered an evil god.
- Characters that oppose getting married will no longer take ambitions to get married or have children. Yes, marriage isn't a strict requirement, but it's still odd.
- Rulers should no longer refer to their capitals as land powers where they should refer to their realms as such.
- Characters should no longer refer to themselves as the would-be murderer if a Private Conversation goes wrong because the other party tried to murder them.
- The "I'm getting stressed out about my many lovers" now checks that a sufficient amount of them aren't imprisoned, as opposed to possibly stressing you out over a single non-imprisoned lover and only letting you break things off with them.
- Heretic and religious revolts now spawn leaders based on temple holder gender, seeing as they're led by "a charismatic [GetPriestTitle]".
- Prosperity should no longer cause characters to praise the wrong high god.
- Prosperity can now only result in a centre of worship if you share the province's religion; might be something to open up a bit, but it should certainly not be possible with *any* province religion.
- Minor adjustments to Vietnam's CoA.
- Added CoA for Heilongjiang.
- Looted duplicate artefacts are now destroyed even if duplicates; clearly, they were fake!
- Remove a couple of artefact spawns; relevant artefacts to be moved to "quest" events.
- Removed indestructibility from some artefacts that didn't need it.
- Removed very_rare artefact flag from a bunch of not-so-rare artefacts.
- Set up historical spawning of a few more artefacts.
- Added the Baopuzi and the Danjing yaoyue.
- Added <trait>_opinion and opinion_of_<trait> for Tianxia's pagan Crusader traits.
- Fixed incorrect prestige penalties for the GC's preferences when it comes to Tributes/Boons.
- Added decision to pay money to strengthen your religion, seeing as not everyone has access to holy wars or religious liberation wars.
- Opened up hunts for women under more circumstances; now Enatic Clans reformers, non-Agnatic Clans Minahasan and Minangkabau rulers, WL members, and rank 2+ WotRS members can also hunt.
- Restricted the famous_<body part> artefacts to Christians due to them being pretty odd in some places; might revisit down the line.
- Changed prestige rewards for the above to piety rewards, seeing as the Christian loc is "<Body part> of a Saint".
- Removed infamous_tongue artefact; it's quite odd.
- MNM "Councillor discovers artefact" events now allow for the discovery of many Tianxia artefacts as well as JD's Chinese artefacts if JD is active. Loc TODO.
- Added _EXPLANATION for all <trait>_opinion and opinion_of_<trait> modifiers.
- Ported main loc for JD artefacts; handling of the proper name for the relevant CI title (if any) TODO.
- Magicians can now visit the AI during Indian feasts.
- Added some more sanity checks for impregnation/seduction in a couple of places.
- Satanic orgies are now a bit more sensibly coded. A bit.
- Ancestor worship is now saner when it comes to attraction triggers.
- Celibate wives should no longer cheat on their spouse with the justification "We don't have children because my husband is infertile!".
- Wives should no longer cheat on their husbands over "suspected infertility" if said husband is Celibate (you've not even tried) or a eunuch (you know what the problem is).
- Underage characters are no longer invited to... "parties" during the coronation event chain; serious vanilla oversight!
- Lustful Children of Destiny are now more likely to get plenty of lovers.
- Only adult Hwarang can now seek Spritual Guidance, solving several possible problems.
- Damsels in distress are no longer into marriage (and becoming lovers) if either party is incompatible.
- Fixed Jeanne d'Arc potentially becoming the lover of someone that's incompatible.
- If men aren't allowed to fight they will also not be around to be handsome guards to tumble.
- It is now possible for homosexual characters to make friends (and get lovers) in an MO.
- MOs no longer cause heterosexual characters to change their orientation; they will instead only get the opportunity to become lovers with someone that they aleady are attracted to.
- While Lucifer does not frown on homosexuality, he also recognizes the problematic nature of vanilla event 6225. It has been excised with prejudce.
- Lucifer and off-brand counterparts have likewise recognized that DW orgies were set up in a problematic manner. This problem has also been excised with prejudce.
- DW orgies no longer make explicit references to Hell or succubi, seeing as those might not make sense in a bunch of places.
- Sleeping with a prostitute while on a crusade and making them your lover has the same effect on your traits as sleeping with them but not making them your lover.
- SRS lover events now check attraction from both directions, as opposed to only checking it from one direction.

---
## [MascaChapas27/SegmentationFault](https://github.com/MascaChapas27/SegmentationFault)@[c2126fd442...](https://github.com/MascaChapas27/SegmentationFault/commit/c2126fd442431c40fcf7cd4605fc0e56b40e163c)
#### Thursday 2023-11-02 22:51:26 by Derrameitor

global music player

now the music player is global yeah fuck you professor who told me that global variables were the worst thing

---
## [ChakatStormCloud/tgstation](https://github.com/ChakatStormCloud/tgstation)@[e39a43e2a4...](https://github.com/ChakatStormCloud/tgstation/commit/e39a43e2a418f19fde52e05281bfdae063f4a6c1)
#### Thursday 2023-11-02 23:05:54 by Toastgoats

[No GBP] Fixes the secret bottomless pit in the ethereal pirate shuttle (#78138)

## About The Pull Request

I DIDNT NOTICE THAT ALL THE DIRT IN THE ETHEREAL SHUTTLE HAD CHASM
BASETURFS FUCK FUCK FUCK


![image](https://github.com/tgstation/tgstation/assets/63932673/ba5f7b02-7577-48ad-b2bc-b8b1c0e4192f)

(Also rebalances the ship a bit by adding some more turrets and cleans
up the wonky turf decals and engines)
## Why It's Good For The Game

God's strongest mapper needs to get some sleep asap I'm so fucking tired

A few people also pointed out that only having two turrets was extremely
punishing even for the playstyle I was trying to encourage, so it makes
sense to add a little wiggle room.
## Changelog
:cl:
balance: Gave the bluespace geode pirates 4 more teleporter bolt
turrets.
fix: The bluespace geode pirates no longer have a bluespace portal to
the bottomless pit dimension.
add: Station-safe dirt tiles for all your mapping needs, but surely no
station maps use the chasm baseturf ones, right? Right?
/:cl:

---
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[c034314f1b...](https://github.com/jjpark-kb/Skyrat-tg/commit/c034314f1b41c2f9ad1e66d939b95f49a0d2f36e)
#### Thursday 2023-11-02 23:23:43 by SkyratBot

[MIRROR] Basic skeletons [MDB IGNORE] (#24545)

* Basic skeletons (#79206)

## About The Pull Request

Turns skeletons (the simple animal version) into basic mobs. This was
another incredibly simple conversion, since skeletons don't really do
anything but walk at you and beat you to death.

Because I thought it was funny, though, skeletons will now seek out
cartons of milk and drink them. Real milk will heal them for a
significant amount, but soymilk, being false milk, will deal them
grievous injury instead! Skeletons beware... I didn't add any other
sorts of milk due to limited ability with existing AI behaviors to
identify milk containers (they actually only look for the carton items).

Other than that, I've done some flavor adjustment for skeletons' attacks
- their effects and sounds will now suit the weapon they're actually
holding - for example, skeleton templars now actually use their swords
instead of slashing you with their horrible fingers. Along with this I
gave the basic skeletons a normal slashing sound, instead of the weird,
impactless hallucination sound they used to use for some reason. I never
liked that sound.

Finally, I've reflavored the spear-wielding skeleton mobs to "undead
settlers", following the naming of the corpses dropped by snow legions
as of #76898, rather than being named after an offensive term for Inuit
people. These skeletons do, after all, appear in settlements on alien
worlds.

To enable the flavor of milk drinking, I expanded the `basic_eating`
component to allow drinking rather than eating flavor, with a different
sound and its own set of verbs. This deletes whatever they drink from,
but c'est la vie.
## Why It's Good For The Game

Ticks 6 more entries off the simple animal freeze. While skeletons are
still extremely simple, being largely-identical mobs that only exist to
beat you to death, being basic mobs should make them slightly better at
this job. Also, again, I think it's really funny that you can distract
skeleton mobs with milk, or even hurt them.
## Changelog
:cl:
refactor: Hostile skeleton NPCs now use the basic mob framework. They're
a little smarter, and they also have a slightly improved set of attack
effects and sounds. They love to drink milk, but will be harmed greatly
if any heartless spaceman tricks them into drinking soymilk instead.
Please report any bugs.
/:cl:

* Basic skeletons

* updatepaths

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[0e3b7d842b...](https://github.com/jjpark-kb/Skyrat-tg/commit/0e3b7d842b40525754a931903dded315f5a0270e)
#### Thursday 2023-11-02 23:23:43 by SkyratBot

[MIRROR] Adds a Syndicate Monkey Agent beacon uplink item [MDB IGNORE] (#24550)

* Adds a Syndicate Monkey Agent beacon uplink item (#79012)

## About The Pull Request

Adds a Syndicate Monkey Agent beacon uplink item. It spawns a dapper
monkey that must follow your orders.

Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

Added a more modularlike subtype for antagonist spawners to reduce
future hardcoding.

Gave the syndicate turtleneck a monkey sprite, from SS14!

## Why It's Good For The Game

I want to see the clown driving security insane with 2-3 monkeys and an
incredible amount of pranking. Or an assistant killing everyone with his
monkey friends while wearing a monkey suit. Or a geneticist sending out
mutated monkeys to kill people. Or a scientist equipping his monkeys
with bombs or xenobiology equipment and sending them out to wreak havoc.

6 TC is only enough for two monkeys, but you can get a third if you
finish any kind of objective.

> Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

We can't have the monkey mafia without guns, come on. The guns are weak
and only usable by monkeys. Additionally, they're restricted to
entertainment only.

Credit to SS14 for the monky turtleneck sprite.

## Changelog

:cl:
add: Adds a Syndicate Monkey Agent beacon uplink item. It spawns a
dapper monkey that must follow your orders.
add: Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.
refactor: Added a more modularlike subtype for antagonist spawners to
reduce future hardcoding.
sprite: Gave the syndicate turtleneck a monkey sprite, from SS14!
/:cl:

---------

Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Adds a Syndicate Monkey Agent beacon uplink item

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[e8cfffb7cc...](https://github.com/Offroaders123/Smart-Text-Editor/commit/e8cfffb7cc79a4621c7861f005e9db6dea06babe)
#### Thursday 2023-11-02 23:38:25 by Offroaders123

TS Service Worker!

If I fully commit to Vite's greatly working magic, then it actually works really well to use TS with a Service Worker! I think I just didn't fully get the concept of entry points for Vite's build step/Rollup's use of that config. Now I get how things work together a bit better. I know Vite is composed of multiple different tools, but I didn't know the connection before, or where specific things hooked up together.

Also it's that I found out that Rollup was made by Rich Harris too. Svelte god haha.

Listening to Lightwork 🔥🦑

Oh yeah and to use the Service Worker, you have to build the app with `npm run build`, then run it with `npm run preview`. Previously you could use it with `npm run dev`, but that doesn't work when the Service Worker has to be part of the Rollup build step, rather than just a syntax translation. I think that's a limitation of Vite's hot module loader, I'm not totally sure. I changed my mind on making it a requirement to run the SW in `npm run dev` though, hence why I think I finally found it ok to remove it from that. I usually disable it when running it like that anyways, since having it on for hot reloading makes it a bit more challenging anyways. And also, I've pretty much debugged everything I need the Service Worker for, so I can just use it on it's own in TS now, without needing to debug new features as much. When I do need to try things out again, I will likely instead setup a standalone (Vite) server with a plain JS SW, then debug things there instead. Or, even just change this one to JS, and run it with `npm run dev` here.

I was curious how Vite's `import.meta` values are assigned, and it looks like it just does them as part of the build step, and recognizes when you try to access values from them. So it's like a build-time only monkeypatch or something. Essentially, it only does that when it picks up that you are trying to access the `import.meta` with those values. So it's like tree-shaken `import.meta` extending, really neat! I guess that's no different than optionally bundling/polyfilling features as you use them. I guess I thought that bundlers would do that kind of thing every time, implicitly. But that's not how things work, they are smarter than that, and me apparently :P

Thankfully this makes everything fully TS-checked too, so I don't need `allowJS` anymore :D

I think `isolatedModules` might be making `<reference no-default-lib="true">` work, I'm not totally sure though. Vite/ESBuild is also key to having a TS-based Service Worker, because TS requires the use of `export {}` for plain ESM file emits, which is unfortunate, because I just want ESM for the file's type checking/strictness, not to make it an actual ESM module when you load it with `navigator.serviceWorker.register()`. Not all browsers still support `{ type: "module" }` yet, so I can't rely on using that to account for the additional `export {}` line.

https://vitejs.dev/config/build-options.html
https://stackoverflow.com/questions/71355290/prevent-service-worker-js-from-being-bundled-with-vite-rollup
https://dev.to/whchi/how-to-use-processenv-in-vite-ho9

---

