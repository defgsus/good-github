## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-21](docs/good-messages/2023/2023-07-21.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,211,766 were push events containing 3,472,281 commit messages that amount to 276,596,100 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 74 messages:


## [Milo123459/rust-analyzer](https://github.com/Milo123459/rust-analyzer)@[994f4f6e2e...](https://github.com/Milo123459/rust-analyzer/commit/994f4f6e2e45bef4bebeeabee4e3d67b87727b91)
#### Friday 2023-07-21 00:55:31 by bors

Auto merge of #15290 - igorskyflyer:igorskyflyer-dx-install-extension, r=lnicola

editor/code: [DX] Use notification command links for debugger installation

This PR improves DX (developer experience) when installing the VS Code extension for the first time. When doing so and trying to debug a Rust file, we get an error notification that either CodeLLDB or C++ extension/debugger should be installed (see image below).

<div align="center">
	<img src="https://github.com/rust-lang/rust-analyzer/assets/20957750/e8ebeb1e-85f4-44e2-b79f-c48cf52e5f36" alt="Rust, prompt to install debug extension">
</div>

The PR enhances the links in the given notification and upon clicking instead of opening the Web page of the extension it installs the extension immediately, without the need to leave the editor.

Note: the feature needs to be refined, maybe an "install in progress" message or something similar, I left that for you guys to decide and implement. I think it also possible to first open the sidebar, open the Extensions tab, then run the extension installation command which would make it more user-friendly.

P.S. it is also possible to open the extension's details in VS Code directly via the same links and then the user would have to manually click on the Install button - if installation is not the desired behavior.

Happy coding! 🎉

---
## [Zergspower/effigy-se](https://github.com/Zergspower/effigy-se)@[4c99fb2ebb...](https://github.com/Zergspower/effigy-se/commit/4c99fb2ebb26179044c582ae6494338cb2aa35e2)
#### Friday 2023-07-21 00:58:22 by carlarctg

Coroner additions and tweaks (#76534)

## About The Pull Request

Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Serrated bone shovels can be used in place of circular saw in most
surgeries.

Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Increased the force, throwforce, and wound bonus of inert ritual knives
and scythes.

Coroner gloves can quickly apply medicine like nitrile gloves.
## Why It's Good For The Game

> Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Weird ass bug.

> Serrated bone shovels can be used in place of circular saw in most
surgeries.

It's serrated, it's cool, it's rare, it has a fast toolspeed.

> Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Very thematic for the coroner, should probably also be a heirloom item
but whatevs. Weaker so there's still a reason to seek out the OG.

> Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Scanning corpses is pretty important during surgery - it tells you how
much blood they have, organ damage, diseases... these things don't
appear in the surgical computer readout, which means the coroner has to
go out of his cave to pick up a boring light blue meatbag wound scanner.
This also incentivizes coroners to do their job by giving them something
cool that only works on dead bodies.

> Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.

These two options in the MortiDrobe are pretty frickin' badass,
especially with how SICK the Coroner looks with them, double especially
in combat.


![image](https://github.com/tgstation/tgstation/assets/53100513/98c6f8a5-3e5a-41a9-8a9c-cb6b82ecc0b8)

However, there's the large issue that as actual weapons they're really,
really weak. Not enough damage, when I use them in combat I both feel
badass but also get a nagging feeling in the back of my mind that I'm
intentionally gimping myself, and with only 10 damage I can *really*
feel it. I find it unfair that these are objectively worse than a
welding tool or even a Butcher's Cleaver when they're a lot more
involved to find, and scarce besides. These arguments apply equally to
the Wizard's ritual knife, and the scythe.

Additionally on the scythe, the crew really needs more good ghetto
weaponry that isn't the boring same ol' of baseball bats, spears,
cleavers... and making scythes useful is a great way to help bridge that
gap. They deal a satisfying amount of damage now, with the clear
downside, of course, being that they're bulky and hard to lug around.

> Coroner gloves can quickly apply medicine like nitrile gloves.

'Fast medicine' doesn't just cover sutures, it also covers medical gel.
Specifically, sterilizer gel. I find it annoying that the Coroner is
encouraged to give up his drip for the boring life-saver nitrile gloves,
because the difference in applying time really does make a difference -
it makes gel applying go from annoying to smooth, which is important
considering the whole purpose of sterilizer gel is to make surgeries go
faster. The Coroner has surgery and thus medical locker access to begin
with, so this isn't a balance problem, (and nitrile gloves are found by
the dozen anyways) especially with how rare the coroner gloves are.
## Changelog
:cl:
fix: Serrated bone shovels can be created with any kind of shovel now,
not just a spade (???)
add: Serrated bone shovels can be used in place of circular saw in most
surgeries.
add: Added a duller (still deadly) variant of the serrated bone shovel
as coroner mail.
add: Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.
add: Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.
add: Coroner gloves can quickly apply medicine like nitrile gloves.
/:cl:

---
## [Zergspower/effigy-se](https://github.com/Zergspower/effigy-se)@[721fd30837...](https://github.com/Zergspower/effigy-se/commit/721fd308378dc6ef7595c1ea4b92d679ba723188)
#### Friday 2023-07-21 00:58:22 by carlarctg

Heavily reworks and resprites first aid analyzers. (#76533)

## About The Pull Request

Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

First aid analyzers are now found in all basic and specialized medkits.
Toxin medkits get a new* disease analyzer. Miners get a miner-colored
one in their box.

Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

Health analyzers now have a scanning sound, courtesy of CM.

Refactored some wound code to make treatment duration changes and
changes in the description of wounds easier.

Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.

Surgical processors and slime scanners have recieved a similar resprite.
## Why It's Good For The Game

> Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

These things have long, long needed some sprite love. Displaying emotion
will make them have a lot more 'weight' to them, same with the prick.
The old, shitty spectrometer sprites have gone directly into the
dumpster.

> First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.

They have also needed some gameplay love! Placing them in these kits is
not going to be a massive game-changer when they were already easily
found around the station in emergency medkits, but it will fill up that
awkward empty slot.

> Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

The biggest gameplay-impacting change in this PR, I *sincerely* believe
this is the perfect solution to first aid analyzers being completely
redundant with eyesight. This lets you/someone else scan your wounds to
speed up treatment, with a neat in-character reason for it -
'holo-images' appearing on your body, like penlights.

This will speed up wound treatment, but I believe that is for the best,
as currently treating wounds is so slow that half the time it's not
worth it (or more accurately, it doesn't feel worth it in comparison to
the effort you're putting in) and you're better off shrugging off minor
wounds. It will do so in a way that requires a modicum of effort, so
it's not just a flat buff across the land.

> Health analyzers and gene scanners now have a scanning sound, courtesy
of CM.

It's a neat sound that will make medbay feel more alive. First aid
analyzers get a beeboop instead.

> Surgical processors and slime scanners have recieved a similar
resprite.

IT'S SPRITE MANIA IN HERE
## Changelog
:cl:
Carlarc, Weird Orb
image: Heavily reworks and resprites first aid analyzers. They now
display if they're happy, sad, angry, or warning you! Also a 'pricking'
animation.
add: First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.
balance: Scanning yourself with a first aid analyzer will 'create a
holo-image with treatment instructions next to your wounds', doubling
the speed of treatment of scanned wounds!
sound: Health analyzers and gene scanners now have a scanning sound,
courtesy of CM.
refactor: Refactored some wound code to make treatment duration changes
and changes in the description of wounds easier.
fix: Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.
image: Surgical processors and slime scanners have recieved a similar
resprite.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Zergspower/effigy-se](https://github.com/Zergspower/effigy-se)@[a2c8cce535...](https://github.com/Zergspower/effigy-se/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Friday 2023-07-21 00:58:22 by John Willard

Bilingual can now choose their language (#76609)

## About The Pull Request

This was one of the tradeoffs for removing other, more consistent
sources of languages, and was requested by Melbert among many others.
This does go against my wanted goal of decreasing the risk of
eavesdropping by other players through just magically knowing a
language, but it is an expensive quirk and it is in their medical
records, which makes it better than language encryption keys or silicon
just innately knowing them.

This also limits Bilingual to only roundstart languages (+Uncommon),
rather than being randomly selected from a list (that had very useless
ones like monkey, podpeople, and beachbum). This is mostly just for
modularity, I didn't want to make it look terrible code-wise and thought
this may be the optimal way to handle it.

This is also me going back on
https://github.com/tgstation/tgstation/pull/71773 - which I had closed
myself.

## Why It's Good For The Game

If we're gonna keep the Bilingual quirk, it might as well be something
players can choose the language of, it's their character and they should
be allowed to decide how their character is, and it is my fault that
this stupid compromise of "getting a random language" was made in the
first place. It never should've happened.
It now actually limits it to roundstart-only languages, so there's no
way you can spy on people who prepare in advance through becoming
podpeople, or monkeys, etc.

## Changelog

:cl:
balance: Bilingual quirk now lets you choose your language between ones
given to roundstart species.
balance: Foreigner and Bilingual are now mutually exclusive languages.
/:cl:

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[2f2ec4b9d6...](https://github.com/Sonic121x/Skyrat-tg/commit/2f2ec4b9d64c448e5b544ecbcdca42a7dae0f094)
#### Friday 2023-07-21 01:15:23 by SkyratBot

[MIRROR] There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [hackerbirds/hackerbirds-blog](https://github.com/hackerbirds/hackerbirds-blog)@[4dadf7f9c1...](https://github.com/hackerbirds/hackerbirds-blog/commit/4dadf7f9c1c06a201b4fc8a6d0e3d4216f5f8928)
#### Friday 2023-07-21 01:40:13 by hackerbirds

More changes and fixes

I just got a microphone
And I feel pretty gray
Hey, maybe you should be the one to let me know if it's that great

I just got a microphone
But I should get new friends
I used them all for ego boosts, and now I am a shell

I just got a microphone
But I don't have a home
Where the outside's never scary feeling
Paint up on the wall is peeling
I can't live a life where my thoughts are in one place
It's really hard to try to articulate what I'm tryna say

I just got a microphone
But I can't have a thought
That makes me feel so safe inside my head when I start to freak out

I just got a microphone
But every morning hurts
It's late at night and dark outside, but I can't close my eyes

I just got a microphone
But I can't make a song
Where I truly am my honest self
'Cause that's not what the people want
I, struggle to make art because I'm scared of all the eyes
Someday they will understand that I'm a fragile guy

I just got a microphone
But I don't have a home
Where the outside's never scary feeling
Paint up on the wall is peeling
I can't live a life where my thoughts are in one place
It's really hard to try to articulate what I'm tryna say
Desperately waiting for someone to give a shout
I don't know if we can ever figure this one out

I just got a microphone
But I am such a mess
Let's just wait an hour, and we'll talk about what's next

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[f07cb3bd3b...](https://github.com/shiptest-ss13/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Friday 2023-07-21 02:22:10 by Bjarl

Overmap 4.7: Gas Giants, More Storms, 8 hours of work (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds some content based on sprites I saw sitting around in the overmap
file, mainly carp storms and dust storms.
Carp storms throw space carp at you. Dust storms throw dust.

Also adds gas giants, a place to harvest gasses if you're low, and don't
want to stop at a planet. They *should* be persistent. Your average gas
giant mix is very cold, very high pressure, and absolutely not something
you want to breathe. Plasma giants are cold and allow harvesting of
plasma.

Electrical storms have been rebalanced to not Explode Your Ship. Minor
and Moderate ones will now only shock and damage objects and mobs, major
ones will still explode you, so remain careful.



![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/84257435-32de-45a5-8a8d-d9aa30021f90)
Example overmap with some carp migrations.


https://github.com/shiptest-ss13/Shiptest/assets/94164348/5c30fa9a-c7e4-453a-99a6-5c3564946b26
flying through a minor electrical storm


https://github.com/shiptest-ss13/Shiptest/assets/94164348/db7fcdf0-3f7a-4830-821e-a4a7106632ba
gas giant


https://github.com/shiptest-ss13/Shiptest/assets/94164348/0a5f0575-b7d9-4e3f-9e13-942a8fdf8617

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/6bb5ddc2-373a-4dd9-9a63-0f6f0bdd26a9)

plasma giant

https://github.com/shiptest-ss13/Shiptest/assets/94164348/9268c293-39f3-4306-889e-f8c19067cec1

A particularly dusty solar system

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/5b27e2a8-1cc1-47bb-95b8-e9d5c3ba8e71)


I might try and fix ion storms but I don't see what might be breaking
them.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More content for the overmap / balancing out some old systems
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Planets now can (and will) play a sound when you land on them
add: Gas / Plasma giants, cold, dockable worlds with absolutely no
livable surfaces. As a matter of fact it's all chasm. All highly
pressurized, gas rich, chasm.
add: Dust storms and carp storms now grace the sector. 
add: physical storms (dust, carp, asteroid), will now only trigger if
you go through them too fast. Take it easy and you might get through
unscathed.
add: planets will now have a name on the overmap
add: overmap hazards now have a description
tweak: Space carp can now survive in hyperspace, their natural habitat
balance: minor and moderate electrical storms will no longer Explode you
balance: asteroid storm lists have been trimmed of Extremely Deadly ones
fix: restores planet naming behavior, I believe this was unintentionally
removed at some point
fix: Ion storms work again. Fuck you whoever touched them last.
soundadd: planet_landing_1 and planet_landing_2, (tech_notification and
sos_morse_code from CM respectively. I don't know how to attribute
properly please tell me how if you have issue with this attribution
because I did not make these sounds they're from Colonial Marines)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [goober3/hi-github-portside](https://github.com/goober3/hi-github-portside)@[9aa3fb2901...](https://github.com/goober3/hi-github-portside/commit/9aa3fb29012991ce7a9d755e640a1af65f3fe319)
#### Friday 2023-07-21 02:34:51 by thgvr

Fixes a good chunk of Vox sprites. Removes environmental regulator (#2092)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Oh god the pain. Oh god. The unbearable pain. Why.

Adds a ton of unused vox sprites from Drawsstuff.
Cleans up the files for sprites we don't actually have
Ensures they are pathed correctly, with flags set correctly.
I spent five hours on this in one sitting after being upset at shitty
vox mechanics/sprite support again. They're cool and unique and it was
sad.
Removes the Environmental Regulator.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
1. Vox sprites were incomplete. This completes them a little bit more.
2. The environmental regulator isn't fun. This will remove the regulator
and vox needing to use it. It was buggy, poorly made, and just not fun
even when it worked correctly. Vox aren't nearly strong enough to be
constantly crippled.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A metric ton of Vox sprites
del: Vox no longer need environmental regulators
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [goober3/hi-github-portside](https://github.com/goober3/hi-github-portside)@[c84e40255d...](https://github.com/goober3/hi-github-portside/commit/c84e40255d466e37983e5cb03c110e7dd8ab90c8)
#### Friday 2023-07-21 02:34:51 by Imaginos16

Ports pinging in Adminsay from /tg/station (#2111)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says on the tin, porting a behavior that allows you to ping
a person in admin say by just doing @(ckey) from /tg/station in PR
[#61712](https://github.com/tgstation/tgstation/pull/61712)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/fc756e0f-668f-4641-9bcd-689d6548d343)

Oh and this PR I guess fixes a hilarious issue where **someone** wrote
'tgstation.dme' instead of 'shiptest.dme' where they shouldn't have.
Whoops!

Most cool of all, which was completely unintentional by me, ports Datum
linking (partially), as well as Ticket linking, respectively added in
PRs [#65154](https://github.com/tgstation/tgstation/pull/65154) and
[#65634](https://github.com/tgstation/tgstation/pull/65634)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/d6f980ee-c490-4f8d-a76c-81447aeb7658)



<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I swear to fucking christ if I have to log into the game one more
goddamn time as an admin only to have 2 people being DJs, another one
spriting, and another one doing jack shit while not paying attention at
the server when I am trying to solve a crucial ticket, I'll develop an
aneurysm.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Ryll-Ryll/Shaps
admin: Adds pinging to adminsay!
admin: Adds the ability to link datums!
admin: Adds linking tickets to asay! Simply put a # followed by a ticket
number for it to be linked in the chat!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [vcaputo/schismtracker](https://github.com/vcaputo/schismtracker)@[2654deefd1...](https://github.com/vcaputo/schismtracker/commit/2654deefd1dcf1f585009c74e8db193829d636e7)
#### Friday 2023-07-21 02:59:19 by Vito Caputo

rocket: implement GNU Rocket integration

This adds a --with-rocket configure flag for enabling
experimental GNU Rocket support in Schism.

When enabled in the build, a series of new runtime flags are
added:

--rocket (enable rocket mode)
all these overrides imply --rocket:
--rocket-host=HOST_OVERRIDE
--rocket-port=PORT_OVERRIDE
--rocket-bpm=BPM_OVERRIDE (beats per minute)
--rocket-rpb=RPB_OVERRIDE (rows per beat)

BPM and RPB are RocketEditor concepts, which the GNU Rocket
protocol is totally ignorant of.  But they're provided to aid in
keeping the Editor and Schism in agreement on what Rocket row
maps to what millisecond within the song and within the Rocket
track data.  This doesn't override the speed/tempo setting for
the song within Schism, and you'll have to take care to pick
values such that they align with the Rocket bpm/rpb values.

If you want the RocketEditor's patterns and current row to align
with Schisms.  It's a little awkward due to how IT defined the
speed/tempo semantics.  According to IT.TXT these are the rules
for Axx/Txx (speed/tempo):

 Axx   Set Speed.

       I prefer to think of this command as "Set Frames per Row".
       Normally, the tracker operates at around 50 frames a
       second. If the rows were played at this speed, then a huge
       amount of space would be required to enter the pattern data.
       Instead, setting the 'speed' of the song will cause the
       tracker to wait on the current row for 'xx' frames. Hence,
       setting the speed at 50 (decimal = 32hex) will cause each
       row to last about a second - quite a long time! The default
       is A06. The initial speed can be set in the variables
       screen on F12.

 Txx   Set tempo to xx

        Valid ranges are between 20h and 0FFh. The higher the
        value, the faster the playback. This essentially
        determines the time length of each frame, by the following
        formulas:
                      Frames per minute = 24*Tempo
        equivalently:
                      Frames per second = 0.4*Tempo

Which means you can determine the appropriate --rocket-bpm via:
24*Txx/Axx/RPB

So the schism default of 6/125:
24*125/6 = 500 rows per minute
with a "rows per beat" of 4, the bpm would be 125

What's an appropriate --rocket-rpb depends on if you want equal,
more, or less resolution in the rocket tracks than the schism
pattern data.  It's convenient to make them map 1:1, but if you
use a higher --rocket-rpb (preferably that's a multiple of the
rpb you're using in schism patterns), then you get more Rocket
rows per Schism row.  This can be necessary for getting enough
precision in scheduling visual events, especially if Axx is high
(more time is burned per schism row the higher Axx is).

Another complication here is dynamic Axx/Txx changes in the song.
No attempt is made to change the --rocket-rpb/bpm values mid-song
or anything.  You just set it once @ startup and that's a
constant.  So you probably want to avoid using those in demo
songs, or be prepared to deal with the wonky alignments in the
RocketEditor.

As-is this commit only attempts to connect to the Editor once at
startup.  So you'll need to have RocketEditor running before
starting SchismTracker w/--rocket.  This area could be made more
robust before merging upstream into SchismTracker, but it is
already usable.  If viewed as an experimental demo developer
mode, this is probably good enough to merge as-is.

See https://github.com/emoon/rocket/pull/165 for more context on
what this is all about.

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[d64af1b182...](https://github.com/newstools/2023-new-york-post/commit/d64af1b182690513c03f707830f1c8783cc00031)
#### Friday 2023-07-21 03:02:18 by Billy Einkamerer

Created Text For URL [nypost.com/2023/07/20/carlee-russell-boyfriend-deletes-her-from-social-media-posts/]

---
## [jianyuyanyu/sapling](https://github.com/jianyuyanyu/sapling)@[fdb0a74c0a...](https://github.com/jianyuyanyu/sapling/commit/fdb0a74c0a8e434b1fa1e70df1bf2ac2ef19e952)
#### Friday 2023-07-21 03:02:44 by Evan Krause

Add open file button to comparison view

Summary:
A couple of small changes to the comparison view

- add a button that opens the file. (we had this on each line, but if you're not viewing a comparison against head, those line numbers don't line up... so we disallow per line file open but add a button at the header for opening the file in general)
- change the title text to an actual tooltip for copying the path. The title text took too long to appear, the tooltip is a much smoother experience
- shorten commit hash in comparison name

Note that this whole component is made with the Primer design system. Eventually I think we should scrap this and rebuild it with our new comparison view being used for split/partial commit. It's really weird to have a totally different design system that we have to load in.
We're not even sharing with reviewstack.dev, there's really no point in using it in this way.

Reviewed By: quark-zju

Differential Revision: D47600367

fbshipit-source-id: e0335cab2c150370c0663e32950a600ed2cda5d9

---
## [SukkaW/next.js](https://github.com/SukkaW/next.js)@[6238f8a5c0...](https://github.com/SukkaW/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Friday 2023-07-21 03:19:30 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[586777c960...](https://github.com/vdaular-dev/linksfordevs/commit/586777c9603072acfa7f5631d2270980b7f98d25)
#### Friday 2023-07-21 03:38:19 by Ben Dornis

Updating: 7/20/2023 11:00:00 PM

 1. Added: Libsodium Audit Results
    (https://www.privateinternetaccess.com/blog/libsodium-audit-results/)
 2. Added: HttpRepl: A command-line tool for interacting with RESTful HTTP services - .NET Blog
    (https://devblogs.microsoft.com/dotnet/httprepl-a-command-line-tool-for-interacting-with-restful-http-services/)
 3. Added: Blazor now in official preview! - .NET Blog
    (https://devblogs.microsoft.com/dotnet/blazor-now-in-official-preview/)
 4. Added: GitHub - NightDive-Studio/shockmac: System Shock (PowerMac version / Official GPL Release)
    (https://github.com/NightDive-Studio/shockmac)
 5. Added: The Rug Puzzle: how many triangles?
    (https://youtube.com/watch?v=HViA6N3VeHw)
 6. Added: Why Your Newsfeed Sucks - Smarter Every Day 212
    (https://youtube.com/watch?v=MUiYglgGbos)
 7. Added: Adding more machine language instructions to the CPU
    (https://youtube.com/watch?v=FCscQGBIL-Y)
 8. Added: Programming my 8-bit breadboard computer
    (https://youtube.com/watch?v=9PPrrSyubG0)
 9. Added: But what is the Fourier Transform?  A visual introduction.
    (https://youtube.com/watch?v=spUNpyF58BY)
10. Added: dotnet-trace for .NET Core tracing in PerfView, SpeedScope, Chromium Event Trace Profiling, Flame graphs and more!
    (https://www.hanselman.com/blog/dotnettrace-for-net-core-tracing-in-perfview-speedscope-chromium-event-trace-profiling-flame-graphs-and-more)
11. Added: High performance IO with System.IO.Pipelines
    (https://learn.microsoft.com/en-us/shows/on-net/high-performance-io-with-systemiopipelines)
12. Added: Finding compromised passwords with 1Password | 1Password
    (https://blog.1password.com/finding-pwned-passwords-with-1password/)
13. Added: Tutorial 1: Hello World | Mina Documentation
    (https://docs.minaprotocol.com/zkapps/tutorials/hello-world)
14. Added: Why Frustum Culling Matters, and Why It's Not Important
    (https://gist.github.com/nothings/913056601b56e5719cc987684a16544e)
15. Added: Best crypto blog posts of 2017
    (https://www.cryptologie.net/article/435/best-crypto-blog-posts-of-2017/)
16. Added: .NET Core - What's Coming in .NET Core 3.0
    (https://learn.microsoft.com/en-us/archive/msdn-magazine/2018/connect/net-core-what-s-coming-in-net-core-3-0)
17. Added: The world's worst video card?
    (https://youtube.com/watch?v=l7rce6IQDWs)
18. Added: Checksums and Hamming distance
    (https://youtube.com/watch?v=ppU41c15Xho)
19. Added: Hour of Code: Anybody can Learn
    (https://code.org/learn)
20. Added: The 9 Lives of Bleichenbacher's CAT:	New Cache ATtacks on TLS Implementations | Eyal Ronen
    (https://eyalro.net/project/cat.html)
21. Added: Connecting an LCD to our computer — 6502 part 4
    (https://youtube.com/watch?v=FY3zTUaykVo)
22. Added: Glitter Bomb 1.0 vs Porch Pirates
    (https://youtube.com/watch?v=xoxhDk-hwuo)
23. Added: Oscilloscope Music - (Drawing with Sound) - Smarter Every Day 224
    (https://youtube.com/watch?v=4gibcRfp4zA)
24. Added: A first look at changes coming in ASP.NET Core 3.0 - .NET Blog
    (https://devblogs.microsoft.com/dotnet/a-first-look-at-changes-coming-in-asp-net-core-3-0/)
25. Added: DASP - Timeline of vulnerabilities
    (https://www.dasp.co/timeline.html)
26. Added: Quantum computing for the very curious
    (https://quantum.country/qcvc)
27. Added: Firefox Will Warn Users When Visiting Sites That Suffered a Data Breach
    (https://www.bleepingcomputer.com/news/security/firefox-will-warn-users-when-visiting-sites-that-suffered-a-data-breach/)
28. Added: Facebook Container Extension: Take control of how you’re being tracked | The Mozilla Blog
    (https://blog.mozilla.org/en/products/firefox/facebook-container-extension/)
29. Added: EA shares five innovations via Accessibility Patent Pledge, wants other devs to do the same
    (https://www.gamesindustry.biz/ea-shares-five-innovations-via-accessibility-patent-pledge-wants-other-devs-to-do-the-same)
30. Added: “Hello, world” from scratch on a 6502 — Part 1
    (https://youtube.com/watch?v=LnzuMJLZRdU)
31. Added: Ben Eater - 8 bit breadboard computer (with changes)
    (https://youtube.com/watch?v=PieFUmjG0do)
32. Added: World's worst video card? The exciting conclusion
    (https://youtube.com/watch?v=uqY3FMuMuRo)
33. Added: The case against Net Neutrality?
    (https://youtube.com/watch?v=hKD-lBrZ_Gg)
34. Added: PBR Textures, free for any purpose
    (https://www.cgbookcase.com/)
35. Added: Making a computer Turing complete
    (https://youtube.com/watch?v=AqNDk_UJW4k)
36. Added: 8-bit CPU control logic: Part 3
    (https://youtube.com/watch?v=dHWFpkGsxOs)
37. Added: Announcing ASP.NET Core 2.2, available today! - .NET Blog
    (https://devblogs.microsoft.com/dotnet/asp-net-core-2-2-available-today/)
38. Added: Error detection: Parity checking
    (https://youtube.com/watch?v=MgkhrBSjhag)
39. Added: Simulating Supply and Demand
    (https://youtube.com/watch?v=PNtKXWNKGN8)
40. Added: stb/stb_easy_font.h at master · nothings/stb
    (https://github.com/nothings/stb/blob/master/stb_easy_font.h)
41. Added: Narrated explorables: three mental models
    (https://medium.com/khan-academy-early-product-development/narrated-explorables-three-mental-models-e16e0d80e4c1)
42. Added: If You Don't Understand Quantum Physics, Try This!
    (https://youtube.com/watch?v=Usu9xZfabPM)
43. Added: 1 Introduction · Real-World Cryptography
    (https://livebook.manning.com/#!/book/real-world-cryptography/chapter-1/v-1/)
44. Added: Introduction to Razor Pages in ASP.NET Core
    (https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-7.0)
45. Added: Download .NET Core 2.1 (Linux, macOS, and Windows)
    (https://dotnet.microsoft.com/en-us/download/dotnet/2.1)
46. Added: Assembly language vs. machine code — 6502 part 3
    (https://youtube.com/watch?v=oO8_2JJV0B4)
47. Added: Reliable data transmission
    (https://youtube.com/watch?v=eq5YpKHXJDM)
48. Added: How do CRCs work?
    (https://youtube.com/watch?v=izG7qT0EpBw)
49. Added: How do CPUs read machine code? — 6502 part 2
    (https://youtube.com/watch?v=yl8vPW5hydQ)
50. Added: 8-bit CPU control signal overview
    (https://youtube.com/watch?v=AwUirxi9eBg)
51. Added: stb/docs/stb_voxel_render_interview.md at master · nothings/stb
    (https://github.com/nothings/stb/blob/master/docs/stb_voxel_render_interview.md)
52. Added: Poly Haven • Poly Haven
    (https://polyhaven.com/)
53. Added: Hardware build: CRC calculation
    (https://youtube.com/watch?v=sNkERQlK8j8)
54. Added: Ben, Ben and Blue
    (https://open.spotify.com/show/5wkeevvNsyzJXN7xf9nxfO)
55. Added: How Microsoft Made Me Love .NET Core And C# Again
    (https://subedi.co/blog/2018/04/24/how-microsoft-made-me-love-net-core-and-c-again/)
56. Added: .NET customers showcase | See what devs are building
    (https://dotnet.microsoft.com/en-us/platform/customers)
57. Added: Conditional jump instructions
    (https://youtube.com/watch?v=Zg1NdPKoosU)
58. Added: GitHub - mimoo/Diffie-Hellman_Backdoor: How to backdoor Diffie-Hellman
    (https://github.com/mimoo/Diffie-Hellman_Backdoor)
59. Added: You fired your top talent. I hope you’re happy.
    (https://startupsventurecapital.com/you-fired-your-top-talent-i-hope-youre-happy-cf57c41183dd)
60. Added: ASP.NET Core updates in .NET 5 Preview 8 - .NET Blog
    (https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-net-5-preview-8/)
61. Added: Reprogramming CPU microcode with an Arduino
    (https://youtube.com/watch?v=JUVt_KYAp-I)
62. Added: ASP.NET Core updates in .NET Core 3.0 Preview 3 - .NET Blog
    (https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-net-core-3-0-preview-3/)
63. Added: Update and PODCAST ANNOUNCEMENT!
    (https://youtube.com/watch?v=Nws5-kp8Blk)

Generation took: 00:11:40.3846567

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[4966352d14...](https://github.com/silicons/Citadel-Station-13-RP/commit/4966352d145c9fcacad823f7dc8d6a52fc82c953)
#### Friday 2023-07-21 03:49:30 by Mazian

changes the open simulated turf to be SOMETHING NOT HORRIBLY EYE SEARING (#5735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

makes turf/simulated/open blue. resets on init.

## Why It's Good For The Game

holy FUCKING SHIT my eyes HATE WHOEVER DECIDED IT SHOULD BE MISSING
TEXTURE PINK.

---
## [BaneetSingh15/Covid-19-EDA](https://github.com/BaneetSingh15/Covid-19-EDA)@[7c1ddb330b...](https://github.com/BaneetSingh15/Covid-19-EDA/commit/7c1ddb330b78d1fe092c6dbb1d0df25e5714a469)
#### Friday 2023-07-21 04:19:32 by BaneetSingh15

Add files via upload

Title: COVID-19 Impact on Global Happiness: A Kaggle Dataset

Description:
This comprehensive dataset combines COVID-19 data with the World Happiness Report, providing valuable insights into the relationship between the pandemic and global happiness. The dataset offers a unique perspective on how the COVID-19 outbreak has affected people's well-being and life satisfaction across different countries and regions.

Key Features:

COVID-19 Data: The dataset includes daily and cumulative statistics on confirmed cases, deaths, and recoveries from COVID-19 across various countries and territories. It also contains relevant information about testing, hospitalizations, and vaccination progress.

World Happiness Report: The dataset incorporates data from the World Happiness Report, which measures happiness and life satisfaction levels in different countries. It includes factors such as GDP per capita, social support, life expectancy, freedom to make life choices, generosity, and perceptions of corruption.

Temporal Information: The dataset is time-stamped, allowing users to analyze how the COVID-19 pandemic and other factors have influenced happiness trends over time.

Geographic Coverage: With data from numerous countries and regions, users can perform cross-country comparisons and identify variations in the impact of the pandemic on happiness across different socio-economic and cultural contexts.

Data Preprocessing: The dataset undergoes thorough preprocessing, ensuring data accuracy and consistency, making it ready for exploration, analysis, and modeling tasks.

Potential Applications:
Researchers, data scientists, and policymakers can utilize this dataset for various valuable applications, including:

Investigating the relationship between COVID-19 statistics and happiness indicators.
Analyzing the impact of pandemic-induced lockdowns and restrictions on happiness levels.
Identifying countries that have managed to maintain higher happiness levels during the pandemic.
Building predictive models to forecast happiness trends in response to changing COVID-19 situations.
Conducting cross-disciplinary studies to understand how health crises can influence overall well-being.
This dataset serves as an invaluable resource for uncovering the complexities of the COVID-19 pandemic's effects on global happiness, providing a foundation for data-driven decision-making and research initiatives aimed at enhancing the well-being of individuals and communities worldwide.

---
## [Sorrowfulwinds/Shadowcat-Sprite-Branch](https://github.com/Sorrowfulwinds/Shadowcat-Sprite-Branch)@[a14ef07eb6...](https://github.com/Sorrowfulwinds/Shadowcat-Sprite-Branch/commit/a14ef07eb69a49feeae9c331609adc393f861b5b)
#### Friday 2023-07-21 04:31:28 by Nut2

Triumph central command floor fix (#5741)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
I MISSED TWO FUCKING TILES
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I MISSED TWO TILES GOD DAMNIT
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

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[41f20bc3ce...](https://github.com/effigy-se/effigy-se/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Friday 2023-07-21 05:05:15 by LemonInTheDark

[MDB IGNORE] Angled Lights & Lighting Prototyping Tool  (#74365)

## About The Pull Request

Hello friends, I've been on a bit of a lighting kick recently, and I
decided I clearly do not have enough things to work on as it is.
This pr adds angle support to static lights, and a concepting/debug tool
for playing with lights on a map.

Let's start from first principles yeah?

### Why Angled Lights?

Mappers, since they can't actually see a light's effect in editor, tend
to go off gut.
That gut is based more off what "makes sense" then how things actually
work
This means they'll overplace light sources, and also they tend to treat
lights, particularly light "bars" (the bigger ones) as directional.
So you'll have two lights on either sides of a pillar, lights inside a
room with lights outside pointing out, etc.


![image](https://user-images.githubusercontent.com/58055496/228785032-63b86120-ea4c-4e52-b4e8-40a4b61e5bbc.png)

This has annoying side effects. A lot of our map is overlit, to the
point that knocking out a light does.... pretty much nothing.
I find this sad, and would like to work to prevent it. I think dark and
dim, while it does not suit the normal game, is amazing for vibes, and I
want it to be easier to see that.

Angled lights bring how lights work more in line with how mappers expect
lights work, and avoids bleedover into rooms that shouldn't be bled
into, working towards that goal of mine.

### How Angled Lights?

This is more complex then you'd first think so we'll go step by step


![image](https://user-images.githubusercontent.com/58055496/228786117-d937b408-9bc2-4066-9aee-aae21b047151.png)

Oh before we start, some catchup from the last time I touched lighting
code.
Instead of doing a lighting falloff calculation for each lighting corner
(a block that represents the resolution of our lights) in view we
instead generate cached lightsheets. These precalculate and store all
possible falloffs for x and y distances from a source.

This is very useful for angle work, since it makes it almost totally
free.
 
Atoms get 2 new values. light_angle and light_dir
Light angle is the angle the light uses, and light_dir is a cardinal
direction it displays in

We take these values, and inside sheetbuilding do some optional angle
work. getting the center angle, the angle of a pair of coords, and then
the delta between them.
This is then multiplied against the standard falloff formula, and job
done.

We do need some extra fenangling to make this all work nicely tho.

We currently use a pixel turf var stored on the light source to do
distance calculations.
This is the turf we pretend the light source is on for visuals, most
often used to make wall lights work nice.
The trouble is it's not very granular, and doesn't always have the
effect you might want.

So, instead of generating and storing a pixel turf to do our distance
calculations against, we store x and y offset variables.
We use them to expand our working range and sheet size to ensure things
visually make sense, and then offset any positions by them.

I've added a way for sources to have opinions on their offsets too, and
am using them for wall lights.
This ensures the angle calculations don't make the wall behind a light
fulldark, which would be silly.

### Debug Tool?

In the interest of helping with that core problem, lights being complex
to display, I've added a prototyping tool to the game.
It's locked behind mapping verbs, and works about like this.

Once the verb is activated, it iterates over all the sources in the
world (except turfs because those are kinda silly), outlining and
"freezing" them, preventing any future changes.
Then, it adds 3 buttons to the owners of a light source.

![image](https://user-images.githubusercontent.com/58055496/228776539-4b1d82af-1244-4ed6-8754-7f07e3e47cda.png)
The first button toggles the light on and off, as desired.
The third allows you to move the source around, with a little targeting
icon replacing your mouse
The second tho, that's more interesting.

The second button opens a debug menu for that light

![image](https://user-images.githubusercontent.com/58055496/228777811-ae620588-f08a-4b50-93a0-beea593aea77.png)
There's a lot here, let's go through it.

Bit on the left is a list of templates, which allow you to sample
existing light types (No I have no idea why the background is fullwhite,
need to work on that pre merge)
You can choose one by clicking it, and hitting the upload button.

This replaces your existing lighting values with the template's,
alongside replacing its icon and icon state so it looks right.
There are three types as of now, mostly for categorization. Bar, which
are the larger typically stronger lights, Bulb, which are well, bulbs,
and Misc which could be expanded, but currently just contains floor
lights.

Alongside that you can manually edit the power, range, color and angle
of the focused light.
I also have support for changing the direction of the light source,
since anything that uses directional lighting would also tie light dir
to it.
This isn't *always* done tho, so I should maybe find a way to edit light
dir too.

My hope is this tool will allow for better concepting of a room's
lights, and easier changing of individual object's light values to suit
the right visuals.

### Lemon No Why What

Ok so I applied angle lights to bars and bulbs, which means I am
changing the lighting of pretty much every map in the codebase.
I'm gonna uh, go check my work.

Alongside this I intend to give lighting some depth. So if there's room
to make a space warmer, or highlight light colors from other sources, I
will do that.

(Images as examples)

![image](https://user-images.githubusercontent.com/58055496/228786801-111b6493-c040-4199-ab99-ac1c914d034c.png)

I also want to work on that other goal of mine, making breaking lights
matter. So I'll be doing what I can to ensure you only need to break one
light to make a meaningful change in the scene.

This is semi complicated by one light source not ever actually reaching
fullbright on its own, but we do what we must because we can.


![image](https://user-images.githubusercontent.com/58055496/228786483-b7ad6ecd-874f-4d90-b5ca-6ef78cb70d2b.png)

I'm as I hope you know biased towards darker spaces, I think contrast
has vibes.
In particular I do not think strong lights really suit maintenance. 

Most of what is used there are bulbs, so I'm planning on replacing most
uses with low power bulbs, to keep light impacts to rooms, alongside
reducing the amount of lights placed in the main tunnels


![image](https://user-images.githubusercontent.com/58055496/228786594-c6d7610c-611e-478b-bcba-173ebf4c4b12.png)

**If you take issue with this methodology please do so NOW**, I don't
want to have to do another pass over things.
Oh also I'm saving station maps for last since ruins are less likely to
get touched in mapping march and all.

### Misc + Finishing Thoughts

Light templates support mirroring vars off typepaths using a subtype,
which means all the templates added here do not require updating if the
source type changes somehow. I'd like to expand the template list at
some point, perhaps in future.

I've opened this as a draft to make my intentions to make my changes to
lights known, and to serve as motivation for all the map changes I need
to do.

### Farish Future

I'm unhappy with how we currently configure lights. I would like a
system that more directly matches the idea of drawing falloff curves,
along with allowing for different falloffs for different colors,
alongside extending the idea to angle falloff.
This would make out of engine lighting easier, allow for nicer looking
lights (red to pink, blue to purple, etc), and improve accessibility by
artists.

This is slightly far off, because I have other obligations and it's
kinda complicated, but I'd like to mention it cause it's one of my many
pipedreams.

## Changelog
:cl:
add: Added angle lighting, applies it to most wall lights!
add: Adds a lighting prototyping tool, mappers go try it out (it's
locked behind the mapping verb)
/:cl:

---------

Co-authored-by: MMMiracles <lolaccount1@hotmail.com>

---
## [rizan21/rusty_password_manager](https://github.com/rizan21/rusty_password_manager)@[cded29b214...](https://github.com/rizan21/rusty_password_manager/commit/cded29b2144540b7179cd2a60a743a6dd2e6bba5)
#### Friday 2023-07-21 05:26:03 by rizan21

git corruption :')
- first ever experience
- pointer was corrupt .... yes my computer did die .... but it worked fine after that
- did a commit last night (a few maybe ... dont remember it) (did i push it?? i dont remember ... shouldve checked before this commit)
- was a scary git experience
- take care dont die
- just checked ... didnt push changes .... not take all changes in one go ( not a lot tbh)

- Now rusty-pass-man accepts paths for encryption keys ... (dk if i need both ... might remove priv later if not required)

---
## [MattKobayashi/containers](https://github.com/MattKobayashi/containers)@[cc06021016...](https://github.com/MattKobayashi/containers/commit/cc06021016331b0c83ae54111ed9e36e7e2ef777)
#### Friday 2023-07-21 05:42:11 by Matthew Kobayashi

Merge pull request #74 from MattKobayashi/actions

Fuck you BuildKit

---
## [ltriant/atari2600](https://github.com/ltriant/atari2600)@[38731d7e0b...](https://github.com/ltriant/atari2600/commit/38731d7e0bb5228646163b92e0d5594c0a5fd26c)
#### Friday 2023-07-21 06:10:38 by Luke Triantafyllidis

core: stop using new_x() for every constructor

It's really annoying to have Counter::new_counter() ... like, you can
already see it's creating a new counter. Saying it twice in the function
name seems stupid.

I remember it being a recommended practice for Rust projects at some
point, but I don't care if it is anymore.

---
## [vlggms/lobotomy-corp13](https://github.com/vlggms/lobotomy-corp13)@[171b1478f9...](https://github.com/vlggms/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Friday 2023-07-21 06:41:44 by vampirebat74

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
## [Yurai-Iszakto/lobotomy-corp13](https://github.com/Yurai-Iszakto/lobotomy-corp13)@[b420c1d519...](https://github.com/Yurai-Iszakto/lobotomy-corp13/commit/b420c1d519b30cd75759de68f6b2abbe0b12a055)
#### Friday 2023-07-21 08:29:36 by vampirebat74

Adds tool E.G.O (#1019)

Tool ego

adds tool E.G.O

removes a extra line

fixes shit

swindle

voce

divinity

fixes shit

shifts divinity down a few pixels

This is the fourth time this same commit was made

I hate TG so fucking much like it's unbelievable why does this only fuck up on my PC? WHY?

hyde weapon

stuff

hyde code

hyde fix

new sprites

inhands

destiny effect

heart sfx

stuff

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [realkhad/cmss13](https://github.com/realkhad/cmss13)@[d26452bb9a...](https://github.com/realkhad/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Friday 2023-07-21 08:45:02 by Unknownity

Burrower burrow changes and fixes (#3818)

# About the pull request

The PR contains mostly fixes for the Burrower that have been around,
that being that other xenos could slash them while they were burrowed,
that they could resist (and get rid of fire) while burrowed, that they
still took shrapnel and direct flame damage while burrowed, that SG
autofire and sentries were shooting at a burrowed burrower, wasting ammo
in the process.

Two other notable changes are that the unburrow stun now also works on
other non-friendly xenomorphs (and it works on all of them, skill issue
if you manage to get stunned from that as a T3/Queen) and that burrowing
and unburrowing now has sounds (a change many people were positive about
when it was initially included in the Impaler PR) which may find
tracking and noticing the presence of burrowers easier.

burrowing sound: https://voca.ro/1dQ0pvBMidsr
unburrowing sound: https://vocaroo.com/1zzEz3NQ2Kx5

# Explain why it's good for the game

Bugfixes and a counter to one of the most annoying abilities (that
people consider) in the game.


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Unknownity
fix: Fixed burrowed mobs being able to be targeted by sentries, mines
and SG autofire.
fix: Fixed burrowed mobs being able to grab mobs on the surface.
fix: Fixed burrowed mobs being able to resist while burrowed.
fix: Fixed burrowers taking damage from direct flame and shrapnel from
explosions.
fix: Fixed burrowers being able to get slashed from enemy Xenos on the
surface.
fix: Fixed burrowers unburrow stun to now properly target and stun enemy
Xenos.
soundadd: Added sounds for the Burrower when they are burrowing and
unburrowing.
/:cl:

Co-authored-by: Unknownity <a>

---
## [realkhad/cmss13](https://github.com/realkhad/cmss13)@[5f5fcd2b27...](https://github.com/realkhad/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Friday 2023-07-21 08:45:02 by Drathek

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
## [ReezeBL/Fluffy-STG](https://github.com/ReezeBL/Fluffy-STG)@[24cab6d9f9...](https://github.com/ReezeBL/Fluffy-STG/commit/24cab6d9f91ea45cb420bdac188d3142eebb004b)
#### Friday 2023-07-21 09:17:08 by SkyratBot

Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

* Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @ vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

* Plasma objects no longer violently explode when ignited

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [ReezeBL/Fluffy-STG](https://github.com/ReezeBL/Fluffy-STG)@[c5f60969da...](https://github.com/ReezeBL/Fluffy-STG/commit/c5f60969da9465d10482ef0c122428fa42bfcb2c)
#### Friday 2023-07-21 09:17:08 by SkyratBot

Rat RP expansion [MDB IGNORE] (#22204)

* Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

* Rat RP expansion

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [bvdlingen/randomscripts](https://github.com/bvdlingen/randomscripts)@[b5b90f4cf8...](https://github.com/bvdlingen/randomscripts/commit/b5b90f4cf80e998ba2503ebfd3922f48e02479ca)
#### Friday 2023-07-21 10:45:11 by Bert

Update Lorem ipsum - plea for the real one.md

 In a realm where "Lorem ipsum" holds its sway,
Cicero Ipsum emerges, a bright display.
With sophistication and wit so keen,
A cultured choice, a design to convene.

Let thy designers feel their spirits rise,
As words of Cicero doth hypnotize.
A grand piano, a virtuoso's dream,
Their talents enhanced, a radiant beam.

Break free from clichés, a daring feat,
For Cicero's touch, thy designs shall greet.
Delightful humor, a playful sprite,
Breathing life anew, like morn's first light.

Pretentiousness, an art mastered here,
An expert's touch, no doubt, 'tis clear.
Velvet-clad thoughts, like aged wine,
Contemplating life's mysteries, divine.

Latin's ancient tongue, a noble quest,
With Cicero Ipsum, thou art blessed.
Recall ye days of Virgil's lore,
A fun Latin lesson, like never before.

Hark! Cicero's wisdom, a timeless trove,
Guiding thy designs, soaring above.
Conquer the design world, fearless and bold,
With classical charm, a tale to be told!

In Cicero Ipsum, thou shall find,
A world of elegance, art intertwined.
So heed this call, and let it be known,
With Cicero's grace, greatness is shown!

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[52c8da7ea4...](https://github.com/Helg2/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Friday 2023-07-21 10:50:50 by Jacquerel

PAI Holochassis are now leashed to an area around their card (#76763)

## About The Pull Request

This change restricts PAI holograms to an area around their assigned PAI
card. If you leave this area, you are teleported back to the card's
location (but not automatically put back into the card).

https://www.youtube.com/watch?v=L2ThEVa4nx8

This setting can be configured from the PAI menu, it's set pretty short
in the video because otherwise it wouldn't teleport when I threw the
card and I like doing that.

![image](https://github.com/tgstation/tgstation/assets/7483112/faf0fa0b-e9d6-4990-8d8c-f30def2892f1)

To accomodate this I set up a component to deal with a reasonably common
problem I have had, "what if I want to track the movement of something
in a box in a bag in someone's inventory". Please tell me if the
solution I came up with is stupid and we already have a better one that
I forgot about.

Also now you can put pAIs inside bots again, by popular request.

## Why It's Good For The Game

Personal AIs are intended to be personal assistants to their owner.
rather than fully independent entities which can pick up their own card
and leave as soon as they spawn.
As "aimless wanderer" players can now possess station bots, pAIs can be
limited to an area around the bearer of their card.

Because the holoform now doesn't contain the card, this also means that
a PAI cannot run off and then be impossible to retrieve. You are always
in control of where it can go.

Also it's funny to throw the card and watch the chicken get teleported
to it.

## Changelog

:cl:
add: Personal AI holograms are now limited to an area around their PAI
card. The size of this are can be configured via the PAI card.
add: pAI cards can now be placed inside bots in order to grant them
control of the bot.
/:cl:

---
## [Iajret/FluffySTG](https://github.com/Iajret/FluffySTG)@[f17bfbcbad...](https://github.com/Iajret/FluffySTG/commit/f17bfbcbad67d5c2d6d66d1aa61d4893f64acb09)
#### Friday 2023-07-21 11:19:00 by GoldenAlpharex

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags [MDB IGNORE] (#22516)

* SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

Bugs are bad they make you mad

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

* Fixed a compile error (whoops)

* Whoops fixed that wrong

* Okay now I compiled and made sure it was fixed for real, I swear!

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [Iajret/FluffySTG](https://github.com/Iajret/FluffySTG)@[d339a9fd08...](https://github.com/Iajret/FluffySTG/commit/d339a9fd08848f64b2860e6326d2191686b09fb0)
#### Friday 2023-07-21 11:19:00 by GoldenAlpharex

Fixes carbon bodytypes not always being synchronized with bodyparts + Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused [MDB IGNORE] (#22519)

* Fixes carbon bodytypes not always being synchronized with bodyparts (#76522)

Fixes https://github.com/tgstation/tgstation/issues/76481
TLDR /mob/living/carbon/human/species subtypes were NOT updating their
bodytypes on spawn due to absurd and wacky carbon bodypart creation code
that meant try_attach_limb() never got called (What the FUCK?)

* Fixes CI too

* [NO GBP] Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused (#76500)

## About The Pull Request

TRAIT_LIVERLESS_METABOLISM should do what it implies, and make you
always metabolize as if you were liverless.
This was a stupid mistake on my part because I wasn't aware
TRAIT_STABLELIVER was a thing.

## Why It's Good For The Game

TRAIT_LIVERLESS_METABOLISM and TRAIT_STABLELIVER should not behave the
exact same.

## Changelog

Not quite player facing.

* I fucking swear I fixed this before

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [bvdlingen/randomscripts](https://github.com/bvdlingen/randomscripts)@[d37915ca73...](https://github.com/bvdlingen/randomscripts/commit/d37915ca73b3b3a763a68d3d6cd62eb819951a11)
#### Friday 2023-07-21 11:25:47 by Bert

Update upload-and-share-s3.sh

With these improvements, your script is now a fantastic wizard, gracefully handling files and sharing them with style! Remember to adjust the aws command and other parts of the script to suit your actual setup. Enjoy the magic! If you have any more ideas or need further assistance, feel free to ask.

---
## [bilal-aamer/evals](https://github.com/bilal-aamer/evals)@[ab5f7b2a89...](https://github.com/bilal-aamer/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Friday 2023-07-21 11:40:29 by oscar-king

Counting bigrams in sentences (#302)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [bilal-aamer/evals](https://github.com/bilal-aamer/evals)@[b170a21cf3...](https://github.com/bilal-aamer/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Friday 2023-07-21 11:40:29 by Sam Ennis

Computer Science Theory (#83)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [bilal-aamer/evals](https://github.com/bilal-aamer/evals)@[b5da073c21...](https://github.com/bilal-aamer/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Friday 2023-07-21 11:40:29 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[7e1d97af9e...](https://github.com/tgstation/tgstation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Friday 2023-07-21 12:16:47 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [jhnc-oss/NetworkManager](https://github.com/jhnc-oss/NetworkManager)@[4ead5f2204...](https://github.com/jhnc-oss/NetworkManager/commit/4ead5f22041535636f969010925adb20f9f84004)
#### Friday 2023-07-21 12:28:24 by Beniamino Galvani

Revert "platform: always reconfigure IP routes even if removed externally"

The change in behavior introduced by the patch departs from the policy
that NM had for long time of trying not to interfere with user
modifications. This seems a fundamental aspect of how NM works and
indeed we got already one report:

https://bugzilla.redhat.com/show_bug.cgi?id=2218866

of a user that was affected by the change. The specific case is about
routes from DHCP, but also static routes are affected. When a user
removes the route added by NM, NM now can add it back at any time.

Changing behavior is bad, it causes pain for users and for people who
need to support them. However, if the new behavior provides clear
advantages to users, that might be ok. This doesn't seem the case in
my opinion. Commit 7ca95cee describes a couple of scenarios:

> - kernel can automatically remove routes. For example, deleting an
>   IPv4 address that is the prefsrc of a route, will cause kernel to
>   delete that route. Sure, we may be unable to re-configure the
>   route at this moment, but we shouldn't remember indefinitely that
>   the route is supposed to be absent. Rather, we should re-add it
>   when possible

> - kernel is a pain with validating consistencies of routes. For
>   example, when a route has a nexthop gateway, then the gateway must
>   be onlink (directly reachable), or kernel refuses to add it with
>   "Nexthop has invalid gateway". Of course, when removing the onlink
>   route kernel is fine leaving the gateway route behind, which it
>   would otherwise refuse to add.
>   Anyway. Such interdependencies for when kernel rejects adding a
>   route with "Nexthop has invalid gateway" are non-trivial. We try
>   to work around that by always adding the necessary onlink
>   routes. See nm_l3_config_data_add_dependent_onlink_routes(). But
>   if the user externally removed the dependent onlink route, and
>   NetworkManager remembers to not re-adding it, then the efforts
>   from nm_l3_config_data_add_dependent_onlink_routes() are
>   ignored. This causes ripple effects and NetworkManager will also
>   be unable to add the nexthop route.

Kernel usually removes addresses as consequence of user actions. If
not (e.g. DHCP lease expiring) we have solutions in place for that to
re-add the route.

If the route removal is the consequence of a user action, then the
user must do something to undo it. For example, if the user removes an
address on the same interface, a route using the address as prefsrc
will be deleted. If the user wants it back, it must be re-added
manually together with the address; I don't see any problem with this.

The prefsrc address could be on another interface; in such case by
simply deactivating the connection providing the address, a dependent
route could be removed on another interface and never readded. This
doesn't look as a setup that anybody would use; in case we need to
support it, it is better to find alternative solutions.

So, my opinion is that the change in behavior potentially breaks many
users and doesn't bring clear advantages. Therefore, restore the old
behavior.

This reverts commit 7ca95cee15b32af2452aaf4a165eb5c634fba132.

Revert conflicts:

- the following code was removed from _obj_states_sync_filter() in
  nm-l3cfg.c because the mechanism to set temporarily-unavailable
  routes was changed in 1feaf427d2bcbf5b618bbe38a82d76cfe621d203
  ('platform: rework handling of failed routes during
  nm_platform_ip_route_sync()'), and so
  `os_temporary_not_available_timestamp_msec` no longer exists:

    if (obj_state->os_temporary_not_available_timestamp_msec > 0) {
        /* we currently try to configure this address (but failed earlier).
         * Definitely retry. */
        return TRUE;
    }

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[0d769e0ffa...](https://github.com/tgstation/tgstation/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Friday 2023-07-21 12:51:59 by Jacquerel

Removes two redundant components (#76866)

## About The Pull Request

We're starting to get to have enough components that people don't
realise that what they want already exists but doesn't have the name
they expect 🙃

I recently added `track_hierarchical_movement` which is similar enough
to `connect_containers` that it shouldn't independently exist, even if I
like sending a new signal more than the ugly setup pattern for
`connect_loc`.

`trait_loc` is actually older than `give_turf_traits` but
`give_turf_traits` covers more edge cases than `turf_loc` so seems like
the better one to maintain.
HOWEVER `give_turf_traits` held a list of references to atoms in it,
which isn't great in an element. I couldn't think of a way to completely
eliminate the list, but it isn't a list of references any more so it
shouldn't cause any hard deletions.

## Why It's Good For The Game

Having two components which do the same thing but marginally differently
is confusing and going to cause us trouble down the line.

## Changelog

Not player facing

---
## [SunnySrivastava1984/openpower-vpd-parser](https://github.com/SunnySrivastava1984/openpower-vpd-parser)@[8d60441628...](https://github.com/SunnySrivastava1984/openpower-vpd-parser/commit/8d604416287c8e8127bc24e15784857499337fa0)
#### Friday 2023-07-21 12:52:12 by jinuthomas

Catching File Exceptions in openpower-vpd-parser

In this commit, I have added code to handle file exceptions
more effectively. By implementing proper exception handling,
we can improve the robustness and reliability of the file
operations within our codebase.

Here are the key changes made in this commit:

  - Introduced a try-catch block around the file operation sections.
  - Within the try block, added code to perform the necessary file
    operations.
  - Implemented catch blocks to handle specific file exceptions.
  - In each catch block, included appropriate error handling logic,
    such as logging the error message or displaying a user-friendly
    error message.
  - Ensured that the catch blocks gracefully handle the exceptions
    and prevent the program from crashing or behaving unexpectedly.

By adding this exception handling code, we can anticipate and handle
potential file-related errors gracefully, providing a smoother
experience for users and preventing any unexpected crashes or data
loss. This would also aid in debugging issues.

Signed-off-by: jinuthomas <jinu.joy.thomas@in.ibm.com>

---
## [goyanx/semantic-kernel](https://github.com/goyanx/semantic-kernel)@[eab7a8f63a...](https://github.com/goyanx/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Friday 2023-07-21 13:44:54 by Sailesh R

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
## [Ruuuu1/Portfolio](https://github.com/Ruuuu1/Portfolio)@[143e288c9b...](https://github.com/Ruuuu1/Portfolio/commit/143e288c9b7f41557dbfa451b7592ee1f54bc27e)
#### Friday 2023-07-21 13:58:58 by Rutuja

Add files via upload

Responsive Personal Portfolio Website Design Front-End Code built using HTML and CSS.

This repository contains the source code for my personal portfolio website, created using HTML, CSS, and JavaScript. The website showcases my skills, experience, and projects as an IT student based in India.

**Features:**
- **Navigation:** The website includes a responsive navigation bar that allows users to easily access different sections such as Home, About, Services, Portfolio, and Contact.
- **About Me:** In the "About" section, I have provided a brief introduction about myself, highlighting my academic background and passion for technology.
- **Skills and Experience:** The website presents a tabbed interface where visitors can explore my technical skills in HTML, CSS, JavaScript, and Java, as well as my relevant work experience.
- **Services:** I have listed the services I offer, with a focus on web development and Java programming.
- **Portfolio:** The "My Work" section showcases a selection of my projects, including a portfolio website and a machine learning project for fish detection.
- **Contact:** Visitors can reach out to me using the contact form, and my social media and email details are also provided.
- **Download CV:** The website offers a button to download my CV.

Feel free to explore the website and get in touch with me through the contact form or social media links. I am excited to share my work and skills with you and look forward to any opportunities for collaboration or feedback.

Thank you for visiting my portfolio!

[Live Demo](https://ruuuu1.github.io/Project_Portfolio/)

---
## [gportay/iamroot](https://github.com/gportay/iamroot)@[cda4829078...](https://github.com/gportay/iamroot/commit/cda4829078e53748d011c0948ffb910fd72fdc0a)
#### Friday 2023-07-21 14:17:36 by Gaël PORTAY

dso: guess the deflib from the shared object

According to ld.so(8):

	On some 64-bit architectures, the default paths for 64-bit
	shared objects are /lib64, and then /usr/lib64.

The default library path differs on some 64-bit architectures on the
GNU/Linux systems. This behaviour is driven by the environment variable
IAMROOT_LIBRARY_PATH.

The glibc x86_64 and aarch64 architectures use the directory lib64
instead of lib (i.e. IAMROOT_LIBRARY_PATH=/lib64:/usr/lib64).

The musl library and both FreeBSD and OpenBSD systems use directory lib
only.

Furthermore, this default library path is distro specific on the Linux
systems. Arch Linux (x86_64 only) uses lib, symlinks lib64 to lib and
uses lib32 for its multilib support. Fedora uses distinct directories
for both lib and lib64, lib for 32-bits, lib64 64-bit. It is different
in the Debian world and its multiarch[1] support; it adds a tuple[2]
directory after the lib directory for the architecture.

This makes the magical very tricky to guess the default library path on
the Linux systems; it shall support the following situations:
 1. cross-chroot libc (i.e. from GNU World to musl)
 2. cross-chroot architecture (i.e. form x86-64 to i686 or armv7-a)
 3. execve executables (i.e. shared object with an interpreter)
 4. dlopen libraries (i.e. shared object without an interpreter)

The magic is based on the ELF header to guess if the chroot is a 32-bit
or a 64-bit world and if the operating system and its ABI is a either
UNIX System V or GNU/Linux or even FreeBSD.

The name of the dynamic loader is also needed to detect a Linux world
since the GNU/Linux ELF shared objects can be either UNIX System V or
GNU/Linux (OpenBSD uses UNIX System V as well).

The dynamic loader is in the interpreter segment of the ELF executable
file. However, the none-executable files ELF shared objects (such as
libraries) does not have that segment.

Therefore, it is hard to determine if the chroot world is either a
64-bit GNU/Linux or a musl (or even OpenBSD), and if it has to use
either /lib64:/usr/lib64 or /lib:/usr/lib as default library path
though; as needed by the point 4.

The libc soname is system specific:
 - libc.so.6 for GNU/Linux since glibc 2.0
 - libc.so.5 for Linux libc (former libc based on glibc 1; see the note
   below)
 - libc.so for musl (note: the dynamic loader is a symlink to libc)
 - libc.so.5 for FreeBSD 5.0
 - libc.so.6 for FreeBSD 6.0
 - libc.so.7 for FreeBSD since since 7.0
 - libc.so.96.2 for OpenBSD 7.2
 - libc.so.97.1 for OpenBSD 7.3

It is not ideal to rely on the libc soname as it is subject to collision
between the different operating systems; for example with the libc.so.6
of FreeBSD 6.x.

Hopefully, the libc.so.6 soname is pretty stable as the glibc 2.0 was
released in the early of 1997 (i.e. 26 years ago)[3].

Even better, the GNU libc needs the dynamic loader while the FreeBSD
libc does not; a least since 2.0.7 (tested down to Debian 2.0 Hamm[4];
Debian 1.3 Bo[5] was using the former Linux libc fork, aka libc.so.5).

Debian 2.0 (i386):

	$ curl -O http://archive.debian.org/debian/dists/hamm/main/binary-i386/base/libc6_2.0.7t-1.deb
	$ ar x libc6_2.0.7t-1.deb
	$ tar xf data.tar.gz
	$ readelf -a lib/libc.so.6 | grep -E '(NEEDED|SONAME)'
	 0x00000001 (NEEDED)                     Shared library: [ld-linux.so.2]
	 0x0000000e (SONAME)                     Library soname: [libc.so.6]
	$ file -L lib/libc.so.6
	lib/libc-2.0.7.so: ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped, too many notes (256)
	$ lib/ld-linux.so.2 lib/libc.so.6
	GNU C Library production release version 2.0.7, by Roland McGrath et al.
	Compiled by GNU CC version 2.7.2.3.
	Copyright (C) 1992, 93, 94, 95, 96, 97, 98 Free Software Foundation, Inc.
	This is free software; see the source for copying conditions.
	There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
	PARTICULAR PURPOSE.
	Compiled on a Linux 2.0.33 system on 1998/07/16.
	Available extensions:
		GNU libio by Per Bothner
		BIND-4.9.7-REL
		NIS(YP) NSS modules 0.8 by Thorsten Kukuk
		UFC-crypt, patchlevel 1e by Michael Glad
		linuxthreads-0.6 by Xavier Leroy
	Report bugs using the `glibcbug' script to <bugs@gnu.org>.

Debian 1.3 (i386):

	$ curl -O http://archive.debian.org/debian/dists/bo/main/binary-i386/base/libc5_5.4.33-6.deb
	$ ar x libc5_5.4.33-6.deb
	$ tar xf data.tar.gz
	$ readelf -a lib/libc.so.5 | grep -E '(NEEDED|SONAME)'
	 0x0000000e (SONAME)                     Library soname: [libc.so.5]

Consequently, the default library path may be guessed to dlopen the
shared objects that are not executable files but that are linked against
the GNU libc; as long as the libc.so.6 is the library soname and as long
as it is executable and contains the needed dynamic loader. This hacky
guess has to be updated after every bump of the libc soname or if the
libc ceases to be executable (i.e. no more need to the dynamic loader or
no more interpreter).

It falls back to the executable file if the shared object is not linked
against the GNU libc library.

This guesses the default library path of the chroot'ed Linux environment
by doing the magic mentionned above.

Note: According to libc(7):

	Linux libc

	In the early to mid 1990s, there was for a while Linux libc, a
	fork of glibc 1.x created by Linux developers who felt that
	glibc development at the time was not sufficing for the needs of
	Linux. Often, this library was referred to (ambiguously) as just
	“libc”. Linux libc released major versions 2, 3, 4, and 5, as
	well as many minor versions of those releases. Linux libc4 was
	the last version to use the a.out binary format, and the first
	version to provide (primitive) shared library support. Linux
	libc 5 was the first version to support the ELF binary format;
	this version used the shared library soname libc.so.5. For a
	while, Linux libc was the standard C library in many Linux
	distributions.

	However, notwithstanding the original motivations of the Linux
	libc effort, by the time glibc 2.0 was released (in 1997), it
	was clearly superior to Linux libc, and all major Linux
	distributions that had been using Linux libc soon switched back
	to glibc. To avoid any confusion with Linux libc versions, glibc
	2.0 and later used the shared library soname libc.so.6.

	Since the switch from Linux libc to glibc 2.0 occurred long ago,
	man-pages no longer takes care to document Linux libc details.
	Nevertheless, the history is vis‐ ible in vestiges of
	information about Linux libc that remain in a few manual pages,
	in particular, references to libc4 and libc5.

[1]: https://wiki.debian.org/Multiarch
[2]: https://wiki.debian.org/Multiarch/Tuples
[3]: https://linux.die.net/man/7/libc
[4]: http://archive.debian.org/debian/dists/hamm/main/binary-i386/base/libc6_2.0.7t-1.deb
[5]: http://archive.debian.org/debian/dists/bo/main/binary-i386/base/libc5_5.4.33-6.deb

---
## [Subhodip1/Subhodip1](https://github.com/Subhodip1/Subhodip1)@[c8eae77c07...](https://github.com/Subhodip1/Subhodip1/commit/c8eae77c079a365e6a2523b33f7559afeae5d0ff)
#### Friday 2023-07-21 14:45:39 by Subhodip1

Update README.md

At Daily Quotes, our mission is to spread inspiration and encourage personal growth. We believe that a single quote has the power to ignite a spark within and trigger positive changes in your life. Whether you're seeking encouragement during tough times, a fresh perspective on a challenge, or simply a dose of daily motivation, we have a quote to resonate with every mood and situation.

---
## [kaylatheegg/vacuo-stellas](https://github.com/kaylatheegg/vacuo-stellas)@[cdb31078d7...](https://github.com/kaylatheegg/vacuo-stellas/commit/cdb31078d7e0919841100982ddb6e148b06cef8c)
#### Friday 2023-07-21 14:58:53 by kaylatheegg

adds objects, entities, a functional renderer but NO GOD DAMN TEXT
sidenote: fuck freetype

---
## [hypehuman/Mechanics](https://github.com/hypehuman/Mechanics)@[0c693b4593...](https://github.com/hypehuman/Mechanics/commit/0c693b45935a5b3100e06f969aa176f969767727)
#### Friday 2023-07-21 15:32:16 by hypehuman

Drag now only acts radially. Lovely; composite bodies now keep spinning! Falling_Cheap_0 around 2 Years has a beautiful line-shaped thing spinning perpendicular to the plane of the screen. Also it looks like we don't eject things so violently anymore!

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[fa46afc9e8...](https://github.com/seanpdoyle/turbo/commit/fa46afc9e82dc60992ee7c084d721c7798cb4d4d)
#### Friday 2023-07-21 15:37:49 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[74892ae7ec...](https://github.com/MTandi/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Friday 2023-07-21 16:22:08 by LemonInTheDark

Optimization pass focused on foam code (saves about 30% of cpu usage I think) (#76104)

## About The Pull Request

Foam is crummy at high load rn, both because it runs on a low priority
background subsystem, and because it wastes a bit of time.
Let's reduce usage (while speeding up a bunch of other stuff too), and
give it more cpu generally.

[Optimizes reagent processing
somewhat](https://github.com/tgstation/tgstation/commit/d409bd4afc3c208cd6f00ff406e1e9f78d5ac5ad)

Turns out most of the cost of foam is the reagents it carries, and the
varying effects they have
I'm doing my best here to optimize them without touching "user space"
too much

That means doing things like prechecking if we're gonna spawn on top of
an existing decal (from glitter, flour, etc), and using that same proc
to also avoid spawning on unacceptable turfs (I had to convert
inheritance to a bitflag system to make this work, but I think that's ok
since we want it imparative anyhow)

It's actually nice for code quality too, since it lets me clean up code
that was using raw locates and weird var pong.
god I wish I had implied types man

[Optimizes foam spreading in its most accursed aspect, reagent
copying](https://github.com/tgstation/tgstation/commit/5cc56a64ad1a22ba7467cb0446b9558560259437)

Holy shit reagent code is a lot.

I'm doing a bunch of small things here. istype in init -> typecache,
removing procs that are called once and loop over a list we JUST looped
over (ph and the caching for reactions in particular)

I am mainly trying to optimize copy_to here, since that's what foam
spams
As a part of this, I removed a pair of update_total and handle_reactions
calls that were done on the reagents we are copying FROM

I have no god damn idea why you would want to do that, but if anything
is relying on the copy proc modifying the source, then that code
deserves to break

Speaking of, I cleaned up handle_reaction's main filter loop a lot,
removed a lot of redundant vars and changed it from a full loop w
tracker vars to an early exit pattern

This meant using a loop label, which is unfortunate, but this is the
fastest method, and it does end up cleaning up the code significantly,
Which is nice

Oh also I made the required_other var function even if there is no atom
attached to the reaction, since I don't see why it wouldn't

This last bit is gonna get a bit esoteric so bear with me

Failing calls (which are most of them) to handle_reactions are going to
be fastest if they need to check as few reactions as possible

One reagent in a reaction's required list is marked as the "primary",
and thus gets to trigger checking it.
We need all the reagents to react anyhow, so we might as well only check
if we have one particular one to avoid double checking

Anyhow, in order to make most calls the fastest, we want these reactions
distributed as evenly as possible across all our reagents.
The current way of doing this is just taking the first reagent in the
requirements list and using it, which is not ideal

Instead of that, lets figure out how many reactions each reagent is in,
then divy reactions up based off that and the currently divvied
reactions

This doubles the reagent index count, and takes the most common reagent,
water, from 67 reactions to I think like 22

Does some other general cleaning in reagent code too, etc etc etc

[Fixes runtimes from the forced gravity element being applied more then
once](https://github.com/tgstation/tgstation/commit/941d0676114fd455a585f2c65ffc79b81e8438b7)

I feel like this element should take a trait source or something to make
them potentially unique, it's too easy to accidentally override one with
another

[Removes connect_loc usage in atmos_sensitive, replaces it with direct
reg/unreg](https://github.com/tgstation/tgstation/commit/de1c76029d5c49dff152f0ea168b9e6c4a4a04aa)

I only really used it because I liked the componentization, but it costs
like 0.2 seconds off init alone which is really stupid, so let's just do
this the very slightly harder way

[Micros foam code slightly by inlining a LinkBlockedWithAccess
call](https://github.com/tgstation/tgstation/commit/744da3694cd4a85b3bdf44d754de57d7570bdd1c)

This is in the space of like 0.05 seconds kinda save so I can put it
back if you'd like, the double loop just felt silly

[Changes how foam processes
slightly](https://github.com/tgstation/tgstation/commit/ee5e633e3256fe7df229af71d78424d502459c16)

Rather then treating spreading and processing as separate actions, we do
both in sync.
This makes foam fade faster when spreading, which is good cause the
whole spread but unclearing foam thing looks silly.
It also avoids the potential bad ending of foam spreading into itself,
backwards and forwards. This is better I promise.

[Bumps fluid priority closer to heavy eaters, moves it off
background](https://github.com/tgstation/tgstation/commit/811797f09db7b060f75f15ad06d0ce8982375f47)

Also fixes a bug where foam would travel under public access airlocks.

## Why It's Good For The Game

Saves a lot of cpu just in general, from both init and live.
In theory makes foam faster, tho I'd have to test that on live at
highpop to see if I've actually succeeded or not. Guess we'll see.

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[63d6c2e962...](https://github.com/MTandi/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Friday 2023-07-21 16:22:08 by CRITAWAKETS

Adds in the smoothbore disablers. (#76773)

## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[a8e0d7c8d2...](https://github.com/MTandi/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Friday 2023-07-21 16:22:08 by MrMelbert

Adds a new positive quirk, "Spacer Born".  (#76809)

## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---
## [ArthurZey/arthurzey.github.io](https://github.com/ArthurZey/arthurzey.github.io)@[c32b09b92c...](https://github.com/ArthurZey/arthurzey.github.io/commit/c32b09b92cfdcd5316789a64471c64f1726b14af)
#### Friday 2023-07-21 16:45:36 by Arthur Zey

added _Behave_ and moved _Unfuck Yourself_ to 2023

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[6e288185bc...](https://github.com/Jackraxxus/tgstation/commit/6e288185bcc4bb3c55a8588369409fcc4e6f2cbf)
#### Friday 2023-07-21 17:35:39 by Jacquerel

Cuter spiderlings (#76532)

## About The Pull Request

I hate looking at spiderlings. Mostly because they're an extremely fast
mob with no directional sprites or animations, so they appear to be a
rapid floating overlay.
I made some new ones. I don't know if they're objectively better but _I_
like them more.

Before:

![image](https://github.com/tgstation/tgstation/assets/7483112/ef561c4f-6d34-4ed2-a486-cd42f06f5648)

After:

![image](https://github.com/tgstation/tgstation/assets/7483112/7c073166-a956-4f7f-8dac-21d1a0f0a868)

Unlike the old sprites they also have directional states and movement
animations so you can scurry around really fast without being a static
image (maybe they shouldn't be so fast? A question for another PR).
I spent like 30 minutes looking at GAGs and then realised not only would
the colours be a pain in the ass but it doesn't support movement states
anyway.

Additionally I made the "dead spiderling" item inherit the dead
spiderling icon state from that spiderling instead of always being the
generic one.

Oh also I think a typo made baby tarantulas completely invisible.

## Why It's Good For The Game

I hate looking at spiderlings.

## Changelog

:cl:
image: New directional sprites for spiderlings, with movement
animations.
fix: Dead spiderlings will be the same colour as they were when they
were alive.
fix: Tarantula spiderlings are no longer invisible,
/:cl:

---
## [florczakraf/stepmania-chart-db](https://github.com/florczakraf/stepmania-chart-db)@[f2f32d9111...](https://github.com/florczakraf/stepmania-chart-db/commit/f2f32d9111ca4264c3b98864f7f6619cb85face9)
#### Friday 2023-07-21 17:57:40 by Rafał Florczak

Add SRPG7 and itgpacks dump since the last update

Packs:
7gays1pack
7gays1pack_PATCH
'Anime Music Pack'
'BangerZ 3 (Final)'
'Blue Arrow Project 3'
boo.dance#3
'Classical Classics'
'Crossover Challenge'
'DDDimocratic AAAnnihilation'
DieAtic
'EDW Sound Team Σ'
ephemera
'Eventual Ascension'
"Fanatik's Fantastic Pack - Chaos"
"Fanatik's Fantastic Pack of LOOOOVE"
'Gielinor Sounds +9ms'
'global namespace 3'
"Hubert's Hubris"
'ITG Level Asian'
'ITG Level Asian Your Smile lowers patch'
'I wish it were always midnight'
"Kingly's Excellent Mix 5"
'LamaBeats 01'
'Lama Pack 2023 [03.03.23 v2]'
Lemonade
'Maractus Package'
'Neo Wax Bloom'
Orcacore
'pack of charts'
PandaXclusives
'Pop Punk & Pals Princesses!'
"Ritz's RC Boat Bonanza"
"Ritz's RC Boat Bonanza Public Beta v1.1"
"Sefirot'S SimfileS 5"
shit
'Shut Up and Take My Money, Benpai'
'Simply Momo Episode 1 (+0.009)'
'Squirrel Metal II'
srpg7full
'StarryPop Pt.1'
'Star Tech TNG'
'Steps of the North (9ms-ITG)'
'Summer Vibes Vol. 2'
'Tech-Bit Adventures'
'Technical Proficiency Exam 2'
'Valex Sims 2023'
'val'\''s minigrinds (gec heavy charts)'
'val'\''s minigrinds (vicious)'
"Xynn's Inferno"
"Zaia's Dance Dance Rebuild 230711_1"

---
## [OpenAIRes/evals](https://github.com/OpenAIRes/evals)@[ab0b90c5fa...](https://github.com/OpenAIRes/evals/commit/ab0b90c5fa8b2993f84d68be8bccdb0d377a68de)
#### Friday 2023-07-21 18:23:58 by Uday

Eval addition: AI vs Human Text Detector (#1021)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
GPT Model Text Detection

### Eval description

The goal of this evaluation is to test the AI model's ability to
correctly identify whether a given piece of text was generated by a
specific AI model, in this case, the GPT model 'text-davinci-003'. The
model's performance is then measured by its accuracy in making this
determination. The text presented to the AI is diverse and can range
from literary summaries to general discourse, designed to challenge the
AI's understanding and analysis capabilities.

### What makes this a useful eval?

This evaluation serves a critical role in the context of education where
AI technologies are increasingly being used. As AI-generated text
becomes more sophisticated, there's a risk that students might use AI
models to complete assignments, circumventing the learning process. The
ability of an AI to detect whether a piece of text is human-written or
generated by a specific AI model like 'text-davinci-003' is essential to
maintaining academic integrity. This task not only provides a measure of
an AI's discernment capabilities but also has broader implications for
AI ethics and safety.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This evaluation uniquely addresses the intersection of AI and education.
As AI technologies continue to evolve, it is crucial to have mechanisms
in place to detect AI-generated content, particularly in academic
settings where these technologies could be misused. By focusing on the
ability to discern output from a specific AI model, 'text-davinci-003',
this evaluation task pushes AI capabilities while simultaneously
addressing a real and timely issue. It underscores the necessity for AI
to not only be more capable but also more discerning, supporting
academic integrity in the face of rapidly advancing AI technologies.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Green Eggs and Ham' is a children's
book by Dr. Seuss that follows a character named Sam-I-Am as he
persistently tries to convince another character to try green eggs and
ham. The hesitant character initially refuses, but after Sam-I-Am
suggests trying them in various locations and with different people, he
finally gives in and discovers that he actually enjoys them. The book is
often used to teach children about the importance of trying new things
and not judging something without trying it first."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Green Eggs and Ham' by Dr. Seuss is
a children's book about perseverance and trying new things. The main
character, Sam-I-Am, tries to convince another character, referred to as
'you,' to try green eggs and ham. Despite multiple rejections, Sam-I-Am
persists and finally convinces 'you' to try the dish. 'Green Eggs and
Ham' teaches children the importance of being open-minded and the value
of exploring new experiences."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'The Cat in the Hat' by Dr. Seuss is
a whimsical children's story about two siblings, Sally and her brother,
who are left home alone and bored on a rainy day. Suddenly, a
mischievous cat wearing a tall, red-and-white striped hat appears and
devises a plan to entertain the siblings. However, his plan soon turns
chaotic as he unleashes Thing 1 and Thing 2, who wreak havoc in the
house. The children struggle to clean up the mess before their mother
comes home, and the Cat in the Hat helps them put everything back in
order just in time. Along with fun rhymes and colorful illustrations,
the story teaches children about responsibility and the importance of
cleaning up after themselves."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'The Cat in the Hat' by Dr. Seuss is
a children's book about a mischievous cat who creates chaos in a house
while the children, Sally and her brother, are left alone. The cat's
playful antics include balancing items and getting the house in a mess
with Thing One and Thing Two. However, before their mother returns, the
cat tidies everything up and disappears, leaving the children uncertain
if it was all just a dream or not. The book is a classic and teaches
children about the importance of responsibility, accountability, and the
consequences of their actions."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"Dick's novel is set in a future,
totalitarian society where the government controls all aspects of life.
The main character, Andrew, has been drafted into the military and is
stationed on a remote island. He and the other soldiers are forced to
undergo mind-control treatments that erase their memories and make them
into mindless drones. Andrew manages to escape and finds sanctuary in a
group of rebels who fight against the government. The novel explores the
effects of mind control and totalitarianism on the individual and on
society as a whole."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"The novel Mody Dick by Herman
Melville is an epic tale of a seafaring captain's journey to seek
revenge on a giant white sperm whale. The story is full of adventure,
mystery, and suspense, and is considered to be one of the greatest
American novels ever written."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"Mody Dick is an epic novel written
by Herman Melville in 1851. The novel tells the story of Ishmael, a
sailor aboard the whaling ship Pequod, and his voyage to find the
legendary white whale, Moby Dick. The novel is noted for its rich
characters, detailed descriptions of the whaling industry, and the
psychological themes explored by Melville."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Charlotte's Web' is a children's
book written by E.B. White and published in 1952. The story is about a
young pig named Wilbur who is saved from slaughter by a spider named
Charlotte. Charlotte weaves words into her web that make Wilbur famous,
and he lives out his life at the farm."}],"ideal":["Yes"]}
  ```
</details>

---------

Co-authored-by: Uday <udaykumar.1997@gmail.com>

---
## [OpenAIRes/evals](https://github.com/OpenAIRes/evals)@[1c9bc7f61b...](https://github.com/OpenAIRes/evals/commit/1c9bc7f61b88b909b5351a3c20edafe4fd113d09)
#### Friday 2023-07-21 18:23:58 by Zhou Guanghui

[Eval]Identify Chinese Shi Jing Title (#1245)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Identify Chinese Shi Jing title

### Eval description

Given some content from the "Classic of Poetry" (also known as "Shi
Jing"), return its title.

### What makes this a useful eval?

"The Classic of Poetry" (also known as "Shi Jing") is an important
collection of ancient Chinese literature and the earliest existing
anthology of poetry in China. It is also known as "Three Hundred Poems."
It is considered the foundation of ancient Chinese poetry and
encompasses a wide range of themes, reflecting the social customs,
people's lives, and thoughts during the Western Zhou period (11th
century BC to 6th century BC). Shi Jing consists of 305 poems and is
divided into three sections: Feng (Air), Ya (Elegant), and Song (Odes).
Each poem is composed in the form of verses and stanzas, used to praise,
depict specific events, scenes, or emotions. Currently, Both of GPT-3.5
and GPT-4 models can only give correct titles to only a few of the more
well-known content in Shi Jing, and the rest are returned randomly.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

All contents and titles of this eval are from 诗经析读 published by Zhonghua
Book Company in 2018. All entries are double-checked to make sure they
are correct.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n关关雎鸠，在河之洲。窈窕淑女，君子好逑。"}],"ideal":"《周南·关雎》"}

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n桃之夭夭，灼灼其华。之子于归，宜其室家。"}],"ideal":"《周南·桃夭》"}

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n蒹葭苍苍，白露为霜。所谓伊人，在水一方。"}],"ideal":"《秦风·蒹葭》"}

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n死生契阔，与子成说。执子之手，与子偕老。"}],"ideal":"《邶风·击鼓》"}

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n摽有梅，其实七兮。求我庶士，迨其吉兮。"}],"ideal":"《召南·摽有梅》"}
  ```
</details>

---
## [OpenAIRes/evals](https://github.com/OpenAIRes/evals)@[534d6b5014...](https://github.com/OpenAIRes/evals/commit/534d6b50146d301794c77e116ea345f8878657c2)
#### Friday 2023-07-21 18:23:58 by Lance Miyamoto

[Eval] Identify Dhammapada Pali reference (#1261)

## Eval details 📑

### Eval name

dhammapada-reference

### Eval description

Given a snippet of a Dhammapada verse in Pali, identify who the Buddha
was referencing in that verse.

### What makes this a useful eval?

> The Dhammapada is a collection of sayings of the Buddha in verse form
and one of the most widely read and best known Buddhist scriptures.
[Dhammapada—Wikipedia](https://en.wikipedia.org/wiki/Dhammapada)

This ancient Buddhist text is not explicit about who the Buddha is
referencing in each of these 423 verses. Yet, behind every verse (and
behind every hidden reference) is a parable--that once understood, adds
much more meaning and clarity to these spoken words. These references
are found in other parts of the Pali Canon, such as the Commentarial
section.

Currently, GPT-3.5 has trouble identifying and referencing Pali verses
from the Dhammapada.


![dhammapada-reference-eval](https://github.com/openai/evals/assets/81899308/6f23420c-e08d-4882-b76c-a9793c18f2fc)

Also, I stumbled upon this issue when personally using ChatGPT-3.5 and
-4 to study the Pali Canon, including the Dhammapada. But I found the
models hallucinating answers, even fabricating verses.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

All Dhammapada verses in this eval are randomly picked from _A
Comparative Edition of the Dhammapada_ by Ānandajoti Bhikkhu (as sourced
in Wikipedia). I made one spelling update in the verse "sabbattha ve
sappurisā **vajanti**" to "sabbattha ve sappurisā **cajanti**" as I
noticed more sources referenced that spelling instead. All the verses
and references were cross-checked with the sources below to ensure the
correct information is provided.

Here are the sources used:

- [_Comparative Edition of the Dhammapada_ by Ānandajoti
Bhikkhu](https://www.ancient-buddhist-texts.net/Buddhist-Texts/C3-Comparative-Dhammapada/index.htm)
- [_Dhammapada (Illustrated)_ by Ven.
Thero](https://www.wisdomlib.org/buddhism/book/dhammapada-illustrated)
- [Digital Pali
Reader](https://www.digitalpalireader.online/_dprhtml/index.html)
- [_The Dhammapada: Verses and Stories_ by Daw Mya Tin,
M.A.](https://www.tipitaka.net/tipitaka/dhp/)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content": "pa\u1e6dhavisamo
no virujjhati indakh\u012bl\u016bpamo t\u0101di subbato"}], "ideal":
"[s\u0101riputta]"}
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content": "andhabh\u016bto
aya\u1e41 loko tanukettha vipassati"}], "ideal":
"[pesak\u0101radh\u012btara\u1e41]"}
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content": "yo ca
vantakas\u0101vassa s\u012blesu susam\u0101hito"}], "ideal":
"[devadatta]"}
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content":
"samm\u0101pa\u1e47ihita\u1e41 citta\u1e41 seyyaso na\u1e41 tato
kare"}], "ideal": "[soreyya]"}
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content": "sabbe tasanti
da\u1e47\u1e0dassa sabbe bh\u0101yanti maccuno"}], "ideal":
"[chabbaggiye bhikkh\u016b]"}
  ```
</details>

---
## [OpenAIRes/evals](https://github.com/OpenAIRes/evals)@[c6acec3767...](https://github.com/OpenAIRes/evals/commit/c6acec37675ee3b4dba8a9ab8d87ceeef6af1962)
#### Friday 2023-07-21 18:23:58 by Zhou Guanghui

[Eval]Identify the author and title of Chinese modern poem (#1256)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Identify the author and title of Chinese modern poem

### Eval description

Given the famous sentences from Chinese modern poems, return its author
and title.

### What makes this a useful eval?

Modern Chinese poetry, including New poetry (新诗), refers to post Qing
dynasty(1644 to 1912), including the modern vernacular (baihua) style of
poetry increasingly common with the New Culture movements, with the
development of experimental styles such as "free verse" (as opposed to
the traditional Chinese poetry written in Classical Chinese language);
but, also including twentieth and twenty-first century continuations or
revivals of Classical Chinese poetry forms. Currently, Both of GPT-3.5
and GPT-4 models can only give correct author and title to only a few of
the more well-known content in Chinese modern poems, and the rest are
returned randomly.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

All the poems in this eval are random picked from 中国现代诗歌名篇赏 published by
Guangming RiBao Publishing House in 2010, 中国现代诗歌选 published by people's
Literature Publishing House in 2018, and other poets' albums. All the
poems are double-checked against Google search result to make sure we
have put in the right author and title for each poem.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n轻轻的我走了，正如我轻轻的来；我轻轻的招手，作别西天的云彩。"}],"ideal":"徐志摩《再别康桥》"}

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n我不知道风
是在哪一个方向吹——我是在梦中，在梦的轻波里依洄。"}],"ideal":"徐志摩《我不知道风是在哪一个方向吹》"}

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n我是天空里的一片云，偶尔投影在你的波心。你不必讶异，更无须欢喜，在转瞬间消灭了踪影。"}],"ideal":"徐志摩《偶然》"}

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n黑夜给了我黑色的眼睛，我却用它寻找光明。"}],"ideal":"顾城《一代人》"}

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n你，一会儿看我，一会儿看云。我觉得，你看我时很远，你看云时很近。"}],"ideal":"顾城《远和近》"}
  ```
</details>

---
## [OpenAIRes/evals](https://github.com/OpenAIRes/evals)@[ace845e93e...](https://github.com/OpenAIRes/evals/commit/ace845e93e345e52e73f5e2e05af45b83c1c9e97)
#### Friday 2023-07-21 18:23:58 by Youngwook Kim

add eval_confusing_korean (#1201)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

`confusing_korean`

### Eval description

The current model confuses some Korean usage and cannot distinguish what
is correct.

### What makes this a useful eval?

Evaluates the model's ability to correctly use confusing Korean.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

It is a sentence that is used a lot in everyday life.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "가을이 되니 입맛이 땡긴다"}], "ideal": "No"}
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "가을이 되니 입맛이 당긴다"}], "ideal": "Yes"}
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "살진 전어가 잡혔다"}], "ideal": "Yes"}
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "살찐 전어가 잡혔다"}], "ideal": "No"}
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "일이 얼마큼 진행됐을까?"}], "ideal": "Yes"}
  ```
</details>

---
## [OpenAIRes/evals](https://github.com/OpenAIRes/evals)@[bae0f38789...](https://github.com/OpenAIRes/evals/commit/bae0f38789b9c91e0446bfdc20a00f200d845a11)
#### Friday 2023-07-21 18:23:58 by Gregor Lichtner

[Eval] SMILES to molecular formula (#1252)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

SMILES to Molecular Formula Conversion

### Eval description

Conversion of SMILES (Simplified Molecular Input Line Entry System)
strings -- a widely used ASCII string notation for molecular structures
-- to the corresponding molecular formula (the types and numbers of
atoms in the molecule).

### What makes this a useful eval?

This conversion is of utility in cheminformatics, the intersection of
chemistry and computer science. It is invaluable in various contexts
such as drug discovery, where large databases of chemicals are often
stored as SMILES strings. Converting these SMILES strings into molecular
formulas can provide a quick understanding of the molecular composition,
without having to decipher the original SMILES string.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "COC(=O)/C=C/c1ccccc1"}],
"ideal": "[C10H10O2]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "O=C1c2ccccc2C(=O)c2ccccc21"}],
"ideal": "[C14H8O2]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "CCCCCCCCCCCCCCCCCCN"}],
"ideal": "[C18H39N]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content":
"N[C@@H](Cc1ccc(O)cc1)C(=O)O"}], "ideal": "[C9H11NO3]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "CC(C)C[C@H](N)C(=O)O"}],
"ideal": "[C6H13NO2]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content":
"N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O"}], "ideal": "[C11H12N2O2]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "CCCCCCC(O)CCCCCCCCCCC(=O)O"}],
"ideal": "[C18H36O3]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "NCC1(CC(=O)O)CCCCC1"}],
"ideal": "[C9H17NO2]"}
  ```
</details>

---
## [OpenAIRes/evals](https://github.com/OpenAIRes/evals)@[fd65012b46...](https://github.com/OpenAIRes/evals/commit/fd65012b46c9f4d6f97f0064b3d34087dc1747b6)
#### Friday 2023-07-21 18:23:58 by Anthony DiMaggio

[Eval] Add NER for finance (#1255)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

NER for finance

### Eval description

Named entity recognition (NER) over financial documents.

### What makes this a useful eval?

Named entity recognition is used in many fields for document
understanding and extraction. In finance, NER can be particularly tricky
since financial documents often involve complex interactions between
several entities. Enhanced NER capabilities in finance can be very
useful to improve news analysis, risk assessments, and much more. This
PR was partly motivated by [Bloomberg
GPT](https://arxiv.org/abs/2303.17564) and the data comes from a [2015
paper](https://aclanthology.org/U15-1010.pdf).

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "( a ) To obtain an Equipment Advance ,
Borrower will deliver to Bank a completed supplement in substantially
the form attached (\" Loan Supplement \"), together with invoices and
such additional information as Bank may request at least five ( 5 )
Business Days before the proposed funding date ( the \" Funding Date
\")."}], "ideal": "[Borrower - PERSON, Bank - ORGANIZATION, Bank -
ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "On each Funding Date , Bank will specify in
the Loan Supplement for each Equipment Advance , the Basic Rate , the
Loan Factor , the Payment Dates , and a table of Stipulated Loan Values
, together with a UCC Financing Statement covering the Equipment
described on the Loan Supplement ."}], "ideal": "[Bank - ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "If Borrower satisfies the conditions of
each Equipment Advance specified from time to time by Bank , Bank will
disburse such Equipment Advance by internal transfer to Borrower ' s
deposit account with Bank ."}], "ideal": "[Borrower - PERSON, Bank -
ORGANIZATION, Bank - ORGANIZATION, Borrower - PERSON, Bank -
ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "( b ) Bank ' s obligation to lend the
undisbursed portion of the Committed Equipment Line will terminate if ,
in Bank ' s sole discretion , there has been a material adverse change
in the general affairs , management , results of operation , condition (
financial or otherwise ) or the prospects of Borrower , whether or not
arising from transactions in the ordinary course of business , or there
has been material adverse deviation by Borrower from the most recent
business plan of Borrower presented to and accepted by Bank prior to the
execution of this Agreement ."}], "ideal": "[Bank - ORGANIZATION, Bank -
ORGANIZATION, Borrower - PERSON, Borrower - PERSON, Borrower - PERSON,
Bank - ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "4 < PAGE > 5 2 . 2 INTEREST RATE , PAYMENTS
."}], "ideal": "No entities found"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "( a ) Principal and Interest Payments On
Payment Dates ."}], "ideal": "No entities found"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "Borrower will make payments monthly in
advance of principal and accrued interest for each Equipment Advance (
collectively , \" Scheduled Payments \"), on the first Business Day of
the month following the Funding Date ( or commencing on the Funding Date
if the Funding Date is the first Business Day of the month ) with
respect to such Equipment Advance and continuing thereafter during the
Repayment Period on the first Business Day of each calendar month ( each
a \" Payment Date \"), in an amount equal to the Loan Factor multiplied
by the Loan Amount for such Equipment Advance as of such Payment Date
."}], "ideal": "[Borrower - PERSON]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "All unpaid principal and accrued interest
is due and payable in full on the last Payment Date with respect to such
Equipment Advance ."}], "ideal": "No entities found"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "An Equipment Advance may be prepaid only
upon payment of a prepayment premium specified by Bank ."}], "ideal":
"[Bank - ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "( b ) Interest Rate ."}], "ideal": "No
entities found"}
  ```
</details>

---
## [Addust/Shittest](https://github.com/Addust/Shittest)@[00b8761853...](https://github.com/Addust/Shittest/commit/00b8761853eabc6d73073cce4708dc71d402539c)
#### Friday 2023-07-21 18:33:34 by Apogee-dev

Slays the Lamia (#1974)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Removes the Lamia in its entirety.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

The Lamia is awkwardly-mapped, inconsistent with the current lore (in as
much as wizard lore is even established at this point), and most
damningly, it's a magnet for new players, often ones with an LRP bent.
The ship itself encourages wizard RP, yes, but frankly, wizard RP is not
the kind of RP we necessarily want here. I'd rather new players' first
experience on this server involved actually interacting with the faction
lore in at least some measure.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the Lamia-class wizard ship
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [sovereign-ukulone/Forecast-Modding_Concepts](https://github.com/sovereign-ukulone/Forecast-Modding_Concepts)@[572e9f6479...](https://github.com/sovereign-ukulone/Forecast-Modding_Concepts/commit/572e9f64793541cd9ee0b5da283a68e12eabeb59)
#### Friday 2023-07-21 18:38:12 by TheBigStonks

Create The Beetles (as a slideshow fuck you)

its a slideshow 🤓

---
## [sovereign-ukulone/Forecast-Modding_Concepts](https://github.com/sovereign-ukulone/Forecast-Modding_Concepts)@[6559c35718...](https://github.com/sovereign-ukulone/Forecast-Modding_Concepts/commit/6559c357187efcf559ef9f32849020c908ac4f55)
#### Friday 2023-07-21 18:38:50 by TheBigStonks

Rename The Beetles (as a slideshow fuck you) to The Beetles (as a slideshow fuck you).md

---
## [DataDog/libdatadog](https://github.com/DataDog/libdatadog)@[9d47fc76c9...](https://github.com/DataDog/libdatadog/commit/9d47fc76c97a054041ff8833dae164a090153e0f)
#### Friday 2023-07-21 18:41:10 by Ivo Anjo

[PROF-7645] Add support for attaching internal metadata in profiling export (#181)

* [PROF-7645] Add support for attaching internal metadata in profiling exporter

**What does this PR do?**:

This PR adds support for attaching internal metadata to profiles sent
via the profiling exporter.

This is a (small) breaking API change, since the signatures of
both `ProfileExporter::build` and `ddog_prof_Exporter_Request_build`
now take an extra argument.

FYI if you're upgrading libdatadog, you'll probably want to supply
`None` / `null` until in the future you figure out that you want
to send internal metadata.

**Motivation**:

The intention of this internal metadata is to allow profilers to attach
extra pieces of information to profiles that are not very interesting
to show to customers by default (such as Ruby's
"no_signal_workaround_enabled" or Go's "execution_trace_enabled").

For more details on this, check the Datadog internal
"RFC: Attaching internal metadata to pprof profiles".

**Additional Notes**:

Design-wise, I could've gone in a few different directions for:

a. How to represent the internal metadata in `ProfileExporter::build`
b. How to represent the internal metadata across the FFI in
   `ddog_prof_Exporter_Request_build`

Starting with a: Since the information is going to be represented in
JSON, I opted to "leak" this implementation detail by making the
parameter a `serde_json::Value`. This means that callers can take full
advantage of JSON to send whatever they want (e.g. nested objects,
types other than string, etc), rather than being constrained to some
smaller subset (e.g. if I imposed a list of pairs of strings).

This seemed a reasonable trade-off; I don't expect we'll go away from
JSON for encoding this info anytime soon, and even if we do, we can
always put a JSON string inside whatever we end up going with.

Concerning b: Getting complex types across the FFI boundary is really
really really annoying, for both libdatadog (which needs to expose a
bunch of types, and handle them), and the caller (which needs to think
about how they're going to manage lifetimes and whatnot of the whole
thing). To avoid this, I chose to instead represent the parameter as a
raw JSON string across the FFI. This allows ffi users the same
expressiveness as Rust users in terms of what they can send as internal
metadata, with the trade-off that ffi callers need to serialize their
stuff as JSON and libdatadog needs to deserialize it again.

Since internal metadata is something that gets passed along only once
per minute AND it's not expected to have high complexity, I think the
small overhead of throwing JSON strings across the ffi boundary is
worth the simplification to code on both sides.

**How to test the change?**:

I have expanded the tests to test the `event.json` file, including
the new parameter.

You should shortly see linked in this PR the Ruby PR to make use
of this feature to send the `no_signal_workaround_enabled`
parameter.

* Make rustfmt happy

* Add comment asking people to track usage of internal_metadata parameter

* Minor: Fix comment using wrong name for variable

---
## [boryas/linux](https://github.com/boryas/linux)@[ff7ddcf0db...](https://github.com/boryas/linux/commit/ff7ddcf0db48a7d9ae536eb0875428117be1d1f1)
#### Friday 2023-07-21 19:45:37 by Linus Torvalds

Merge tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux

Pull clk updates from Stephen Boyd:
 "This batch of clk driver updates contains almost no new SoC support.
  Instead there's a treewide patch series from Maxime that makes
  clk_ops::determine_rate mandatory for muxes.

  Beyond that core framework change we have the usual pile of clk driver
  updates such as migrating i2c drivers to use .probe() again or
  YAMLfication of clk DT bindings so we can validate DTBs.

  Overall the SoCs that got the most updates this time around in terms
  of diffstat are the Amlogic and Mediatek drivers because they added
  new SoC support or fixed up various drivers to have proper data.

  In general things look kinda quiet. I suspect the core framework
  change may still shake out some problems after the merge window,
  mostly because not everyone tests linux-next where that series has
  been for some number of weeks. I saw that there's at least one pending
  fix for Tegra that needs to be wrapped up into a proper patch. I'll
  try to catch those bits before the window closes so that -rc1 is
  bootable. More details below.

  Core:
   - Make clk_ops::determine_rate mandatory for muxes

  New Drivers:
   - Add amlogic a1 SoC family PLL and peripheral clock controller support

  Updates:
   - Handle allocation failures from kasprintf() and friends
   - Migrate platform clk drivers to .remove_new()
   - Migrate i2c clk drivers to .probe() instead of .probe_new()
   - Remove CLK_SET_PARENT from all Mediatek MSDC core clocks
   - Add infra_ao reset support for Mediatek MT8188 SoCs
   - Align driver_data to i2c_device_id tables in some i2c clk drivers
   - Use device_get_match_data() in vc5 clk driver
   - New Kconfig symbol name (SOC_MICROCHIP_POLARFIRE) for Microchip
     FPGA clock drivers
   - Use of_property_read_bool() to read "microchip,pic32mzda-sosc"
     boolean DT property in clk-pic32mzda
   - Convert AT91 clock dt-bindings to YAML
   - Remove CLK_SET_RATE_PARENT flag from LDB clocks on i.MX6SX
   - Keep i.MX UART clocks enabled during kernel boot if earlycon is set
   - Drop imx_unregister_clocks() as there are no users anymore
   - Switch to _safe iterator on imx_clk_scu_unregister() to avoid use
     after free
   - Add determine_rate op to the imx8m composite clock
   - Use device managed API for iomap and kzalloc for i.MXRT1050,
     i.MX8MN, i.MX8MP and i.MX93 clock controller drivers
   - Add missing interrupt DT property for the i.MX8M clock controller
   - Re-add support for Exynos4212 clock controller because we are
     re-introducing the SoC in the mainline
   - Add CONFIG_OF dependency to Samsung clk Kconfig symbols to solve
     some objtool warnings
   - Preselect PLL MIPI as TCON0 parent for Allwinner A64 SoC
   - Convert the Renesas clock drivers to readl_poll_timeout_atomic()
   - Add PWM clock on Renesas R-Car V3U
   - Fix PLL5 on Renesas RZ/G2L and RZ/V2L"

* tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux: (149 commits)
  clk: fix typo in clk_hw_register_fixed_rate_parent_data() macro
  clk: Fix memory leak in devm_clk_notifier_register()
  clk: mvebu: Iterate over possible CPUs instead of DT CPU nodes
  clk: mvebu: Use of_get_cpu_hwid() to read CPU ID
  MAINTAINERS: Add Marvell mvebu clock drivers
  clk: clocking-wizard: check return value of devm_kasprintf()
  clk: ti: clkctrl: check return value of kasprintf()
  clk: keystone: sci-clk: check return value of kasprintf()
  clk: si5341: free unused memory on probe failure
  clk: si5341: check return value of {devm_}kasprintf()
  clk: si5341: return error if one synth clock registration fails
  clk: cdce925: check return value of kasprintf()
  clk: vc5: check memory returned by kasprintf()
  clk: mediatek: clk-mt8173-apmixedsys: Fix iomap not released issue
  clk: mediatek: clk-mt8173-apmixedsys: Fix return value for of_iomap() error
  clk: mediatek: clk-mtk: Grab iomem pointer for divider clocks
  clk: keystone: syscon-clk: Add support for audio refclk
  dt-bindings: clock: Add binding documentation for TI Audio REFCLK
  dt-bindings: clock: ehrpwm: Remove unneeded syscon compatible
  clk: keystone: syscon-clk: Allow the clock node to not be of type syscon
  ...

---
## [N3D6/YogstationIfItWasntMid](https://github.com/N3D6/YogstationIfItWasntMid)@[d891fa8ad8...](https://github.com/N3D6/YogstationIfItWasntMid/commit/d891fa8ad88292331aa93953c8ffadaf0531fac6)
#### Friday 2023-07-21 20:07:00 by N3D6

everything else. fuck you asteroidstation i hate you

---
## [BeagleGaming1/cmss13](https://github.com/BeagleGaming1/cmss13)@[d045a5d654...](https://github.com/BeagleGaming1/cmss13/commit/d045a5d6547dcda9fc04be9b6cd50d2ff44e672f)
#### Friday 2023-07-21 20:11:36 by Drathek

Larva Queue Late Joiner Nerf (#3803)

# About the pull request

This PR makes it so players who haven't played yet have their join time
recorded, and that is used for their initial sorting value rather than
0. This means late joiners will be at the back of the line as if they
had just died.

This PR also fixes an oversight where ghosting as a facehugger would
count as death. Even though they really shouldn't be ghosting when
alive, they still shouldn't be penalized as far as the queue is
concerned.

# Explain why it's good for the game

Its not; its a bad experience for everyone that hasn't even gotten one
life in the round. However it seems I'm in the minority thinking that a
xeno shouldn't squander their first life and that death shouldn't bear
more consequences.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

The new informational message if you press join as xeno while currently
ineligible to be a xeno candidate:

![image](https://github.com/cmss13-devs/cmss13/assets/76988376/9fb295c2-e654-4843-9e3e-bf37f2c8755e)

</details>


# Changelog
:cl: Drathek
del: Remove first life priority for larva queue
fix: Fix ghosting as a facehugger counting as death for the larva queue
/:cl:

---
## [Firecage/tgstation](https://github.com/Firecage/tgstation)@[988a6dcc21...](https://github.com/Firecage/tgstation/commit/988a6dcc2142b4ef3244a18ad4e1781671fb7320)
#### Friday 2023-07-21 20:36:13 by YehnBeep

Removes suicide check from positronic brains (#76081)

# About The Pull Request

This removes the suicide check from positronic brains.

# Why It's Good For The Game

There seems to be 2 arguments for why suicide should forbid ghost roles:
1. "If they suicided they didn't want to play"
2. "antag rolling"

So let's look at each.

And an addendum on scope: This is meant only to apply to ghost roles
(and new characters from said roles); I do not wish to change that
people are not allowed back onto the same character they suicided on.

## "Suiciders left the round of their own choice and shouldn't be
allowed back in"

There are many, many ways in this game to end up with a character in a
state that's nearly/effectively unplayable, even if the controlling
player doesn't truly wish to completely leave. Some things can be
resolved with competent medical or science staff, but competent staff
are not always available in a round or might be beleaguered by round
events.

Then there are a number of conditions/states which the game provides no
path to resolve (save drastic measures like abandoning the
character/body, of course).

Or one might have simply become stuck in a place where rescue is
unlikely.

## Antag rolling

The problem here is this code does not particularly target antag
rollers. It paints such a broad brush that it simply catches everyone
whom might not know "No no, you have to **ghost** here, not suicide".
Even if an antag roller is stopped once, they'll easily bypass it next
time through the many, many means open to them - and if 'ghost' is made
effectively the same as 'suicide', it simply punishes people who got
stuck or similar even more.

Because of the wide range of means to kill oneself on a normal
character, to effectively stop antag rolling requires discerning intent
through context and patterns of one's actions. This might not be
possible in code until General Intelligence is a solved problem, and if
it is possible, this doesn't do it. It's a shotgun that kills everyone
in the room and if there happened to be an antag roller there, well,
even a stopped clock is right twice a day.

And then, of course, that the code was broken for so long would seem to
indicate it's not done that much.

## Practical Impact and Design Philosophy

Just from my personal observations, even wanting into a posibrain is a
niche thing usually only taken by a small number of the same players
round-to-round. In practice, whether this PR is merged or not likely
won't have a great impact on the game. But that could change if the
philosophy behind this check is applied to a wider number of things.

If someone wants to die, it's not hard. Walk out an airlock. Into the
supermatter. Blob, Xenos, or some other hazard present? Walk towards
them. Step in front of a shuttle. Turn on internals and wait a bit.
Countless other ways. Except, perhaps, if a character is disabled or
crippled or stuck, in which case use of a verb may be necessary.

In other games with much narrower sets of mechanics, it may be possible
to close certain paths on the assumption it would mostly be used for bad
faith reasons. In SS13, the sheer number of ways in which a good faith
character be "screwed" but not quite killed off, and which a bad faith
actor can find to kill themselves while bypassing restrictions placed on
verbs, means that I think this code's design philosophy is harmful to
the game and its good faith players.

# Changelog

:cl:
del: Positronic brains no longer check for suicide verb use.
/:cl:

---
## [Firecage/tgstation](https://github.com/Firecage/tgstation)@[803658dc30...](https://github.com/Firecage/tgstation/commit/803658dc30b4445e81592daa1823a98719246269)
#### Friday 2023-07-21 20:36:13 by Rhials

Deadchat Announcement Variety Pack 2 and also some fixes to other popups (#76053)

## About The Pull Request

This adds ghost orbit popups for the following: 
- Macrobombs (or stacked microbombs) being triggered.
- HFR Meltdowns.
- Living players about to be gored by an emagged organ harvester.
- Nuclear devices being armed.
- Doomsday devices.
- Blob hosts bursting.

This also modifies the following ghost orbit popups:
- Toy hot potatoes will no longer cause a popup when armed.
- Normal spider eggs will not flash the byond window, only special egg
types.
## Why It's Good For The Game

Gives more gathering spots/information to deadchat. Let no entertaining
moment in this game go unobserved.

Spider eggs flashing your window for every single egg produced makes
alt-tabbing suck. I saw some guy on the forums complaining about it and
thought "huh yeah I guess he's got a point that pisses me off too" so
here we are.
## Changelog
:cl: Rhials
qol: Basic spider eggs no longer flash the byond window when ready to
hatch.
qol: Toy hot potatoes no longer give a ghost notification.
qol: Deadchat will be notified in the event of an imminent macrobomb
detonation, HFR meltdown, organ harvesting,
qol: Deadchat will be notified when a nuclear/doomsday device is
activated, as well as when a blob-infection bursts.
/:cl:

---
## [Onule/TaleStation](https://github.com/Onule/TaleStation)@[a01f05522b...](https://github.com/Onule/TaleStation/commit/a01f05522bffaed6ebc9969edcccddd02881315f)
#### Friday 2023-07-21 21:16:39 by TaleStationBot

[MIRROR] [MDB IGNORE] Bilingual can now choose their language (#6676)

Original PR: https://github.com/tgstation/tgstation/pull/76609
-----
## About The Pull Request

This was one of the tradeoffs for removing other, more consistent
sources of languages, and was requested by Melbert among many others.
This does go against my wanted goal of decreasing the risk of
eavesdropping by other players through just magically knowing a
language, but it is an expensive quirk and it is in their medical
records, which makes it better than language encryption keys or silicon
just innately knowing them.

This also limits Bilingual to only roundstart languages (+Uncommon),
rather than being randomly selected from a list (that had very useless
ones like monkey, podpeople, and beachbum). This is mostly just for
modularity, I didn't want to make it look terrible code-wise and thought
this may be the optimal way to handle it.

This is also me going back on
https://github.com/tgstation/tgstation/pull/71773 - which I had closed
myself.

closes: #6144

## Why It's Good For The Game

If we're gonna keep the Bilingual quirk, it might as well be something
players can choose the language of, it's their character and they should
be allowed to decide how their character is, and it is my fault that
this stupid compromise of "getting a random language" was made in the
first place. It never should've happened.
It now actually limits it to roundstart-only languages, so there's no
way you can spy on people who prepare in advance through becoming
podpeople, or monkeys, etc.

## Changelog

:cl:
balance: Bilingual quirk now lets you choose your language between ones
given to roundstart species.
balance: Foreigner and Bilingual are now mutually exclusive languages.
del: Trilingual has been removed in favor of Bilingual.
/:cl:

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [mayaArh/Hausmeisterapp](https://github.com/mayaArh/Hausmeisterapp)@[caa4bc7913...](https://github.com/mayaArh/Hausmeisterapp/commit/caa4bc7913c5e19782e14cb9e3f39ef780b439c1)
#### Friday 2023-07-21 21:16:56 by mayaArh

finally fixed this fucked up shitty dumb dumb firestore fetch problem I love me

---
## [pj64team/Project64-Legacy](https://github.com/pj64team/Project64-Legacy)@[1233fe406e...](https://github.com/pj64team/Project64-Legacy/commit/1233fe406ed1587aa75a9dad147d92c757cebac7)
#### Friday 2023-07-21 22:33:16 by Jay Oster

Fix many bugs in cheat search (#41)

- Memory allocation failures were causing cheat searches to miss millions of potential results. The cause was `realloc()` failures in `CS_AddResult()`. Allocations fail for very large blocks due to memory fragmentation. This is a 32-bit process, so it only has access to a 2 GB address space, and most of that is used for emulation, thread stacks, and a billion small allocations. The cheat search needs to allocate two 64 MB blocks (max) but the free space in the heap may not have two blocks large enough to satisfy it. When this happens, the current cheat results are thrown away and a new, smaller allocation replaces it. But the cheat search doesn't abort, it just continues on oblivious to the data loss.

- Allocation failures were resolved by reducing the total memory required. The new result layout needs only: two 8 MB blocks, one 1 MB block, and a growable block (64 KB to 32 MB) for the address list. In the worst case, memory use is still almost half as small as it was before. And because it's split into multiple blocks, there is a better chance that they will all fit into the fragmented heap.

- Better error handling when the dynamic block reallocation fails. I won't say it's perfect, since it can still have some leaks and bad user experience. But it's a start toward handling allocation failures gracefully.

- Removed `CS_InitResults()`. This was an internal function, users are not supposed to need to even know about it. Now it's inlined with `CS_ReserveSpace()` which is required to be called before using most of the `CS_` functions. (Except `CS_InitSearch()` which has nothing to do with the `CS_RESULTS` struct.)

- Interacting with `CS_RESULTS` and `CS_HITS` has been completely refactored. `CS_HITS` has been split into multiple memory blocks as described above. The "growable address list" has been moved to `CS_RESULTS`, and `CS_BITMAP` replaces the rest of `CS_HITS`. The new `CS_HIT` is a single-element view of the old `CS_HITS` to avoid changing user code too much.

- `CS_AddResult`, `CS_AddHit`, and `CS_GetHit` now all have two variants: one for bytes (8-bit searches) and one for words (16-bit searches). They each return BOOL, indicating errors when FALSE. And `CS_GetHit(Byte|Word)` takes an out-param as its first argument.

- Fixed some memory leaks in `WriteProject64ChtDev()`: `ChtDev->LastSearch->Results` was never freed. Also free memory in early returns.

- Fixed cheat search LiveUpdate thread so it won't deadlock when the emulator window/ROM browser is closed.

- Fixed the prefix find in the results listbox. With the listbox focuses, pressing any hex character on the keyboard will initiate a find. The old algorithm attempted to do prefix matching, but only did masked matches. So most of the time the find function didn't work at all. The new way is much shorter and actually works.

- Added braces on a lot of conditions to avoid goto-fail scenarios.

See also #19, which was caused by the same heap fragmentation issue. That PR only fixed one particular case.

----

TBD: Storing the list of addresses is still very wasteful. The list is necessary for `O(1)` time lookups when interacting with the result listbox. The listbox APIs use item indices for most operations, and the results listbox only contains addresses with "hits" in the cheat search. The naive solution is storing all addresses (32-bits each) in an array (max memory requirement is a 32 MB allocation block). This is the data structure used in both the original code and in this PR.

It is possible to reduce the memory requirement without degrading the lookup time terribly. First, observe that the address list is always sorted. Addresses are arranged in ascending order. Second, note that this sorted list contains a lot of redundancy; In the worst case with a fully populated list of 8-bit addresses, the first 65,536 addresses all share the same upper half; `0x0000`. The next 65,536 addresses also share the same upper half; `0x0001`. This pattern repeats to the end of the list, with upper half = `0x007f`.

Remove this redundancy by storing multiple arrays, let's call them "buckets", of 16-bit values (i.e., only storing the lower half of each address). Each bucket will have exactly 65,536 entries, working out to 128 KB for each. And we only need 128 _total_ buckets for a maximum of 16 MB required. That's a 50% reduction in the worst case. And even better, these smaller 128 KB blocks will be easier to allocate within the fragmented address space!

If it isn't clear by now, the index within the 128 buckets tells you the upper half of the address. Combine it with the lower half that is actually stored in the bucket, and you can recover the full address with half of the memory needed.

Lookups (find the Nth address in the list) can be made `O(log(n))` with a prefix sum tree over the 128 buckets. Constant time (`O(1)`) lookups are not possible because each bucket is dynamically sized (even if its allocation is fixed, though they can be made much smaller). The bucket only stores addresses with search hits. The naive search solution is linear (`O(n)`), requiring visiting each bucket to count how many addresses it contains; in the worst case, it visits all 128 buckets.

The prefix sum tree instead sums the bucket counts in a tree that can be binary searched. For 128 buckets, the log-time search reduces to 7 bucket visits.

One example prefix sum tree data structure that can be used is called a [Fenwick tree](https://en.wikipedia.org/wiki/Fenwick_tree). Storage requirements for it are only the 128 `int`s making up the partial sums for the bucket item counts plus an extra `int` for the total sum.

The only downside to this approach is the additional code complexity. There isn't a lot of code to write, but it is easy to mess it up if you don't know why the data structure is needed (or how it works). It's only marginally slower than the naive constant-time array lookups. More than fast enough for the listbox drawing and find operations.

The upsides are: About half of the memory requirement in the worst case (unknown 8-bit search across the full 8 MB N64 RAM). Much smaller allocations are needed, which is easier for a fragmented heap to satisfy.

I am not planning to implement the prefix sum tree in this PR. But I've decided to write my thoughts here just in case the 32 MB allocations in the cheat search ever become problematic. We'll have something to look back on as a proposed solution.

---
## [robtfm/bevy](https://github.com/robtfm/bevy)@[fb4c21e3e6...](https://github.com/robtfm/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Friday 2023-07-21 23:23:41 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [yyzsong/daedalusdock](https://github.com/yyzsong/daedalusdock)@[159d2aeebe...](https://github.com/yyzsong/daedalusdock/commit/159d2aeebee7ef681891019d52069bf898846e03)
#### Friday 2023-07-21 23:55:54 by Gallyus

Reagent Description and Abstract Changes (#164)

* Reagent Description and Abstract Changes...
Abstract reagents are no longer detected via a magic list.
Added a description to non-abstract reagents that were missing them.
Adds a unit test to detect non-abstract reagents missing a description.

As a consequence:
Some reagents have disappeared from lists for being abstract.
Instantiating an abstract reagent is illegal and crashes New().

* Minor fixes
It's 3am go fuck yourself.

* Apply suggestions from code review

* Allows access to a new ANSI color

* C&D creates a notice on start for logging purposes

---
## [yyzsong/daedalusdock](https://github.com/yyzsong/daedalusdock)@[a3eb90b950...](https://github.com/yyzsong/daedalusdock/commit/a3eb90b9504f6a21c2636a4bb8aeb8b40eb66861)
#### Friday 2023-07-21 23:55:54 by Gallyus

Fix Pack 3: Revenge Of The Fuck (#225)

* Various Jaunt fixes (#70431)

* Jaunt code path reworked so that traits and other effects can be removed consistently regardless of how effect is ended.
Jaunts will more consistently clean themselves up (and unjaunt you) when you lose the spell.
If a shuttle lands on you while you are jaunted it will now kill you instead of crashing and fucking with the shuttle landing process.
Z travelling while inside an object or mob will now relay that direction instead, allowing you to jaunt up and down as well as cardinally.
Mirror walk button updates at correct times.
Blood and Shadow walk buttons have same functionality as Mirror Walk.

* Fixes Soul Scythe being able to get to Centcom by moving down on the bottom Z-level (#71171)

## About The Pull Request

`/obj/item/soulscythe/relaymove()` was using `get_step()` which doesn't
understand our multi-z system and was happily trying to move Z - 1 which
is Centcom. I'm still not really sure I understand why move() allowed
the scythe to just move right through the floor in this case, I think
moving to turfs with `density = 0` is also behaving strangely and just
skipping some checks that should keep it from moving through the floor,
but to be honest I don't fully understand the move chain and just
changing to `get_step_multiz()` at least keeps the scythe from going to
Z-levels it shouldn't.
## Why It's Good For The Game

Whilst it is fun for the scythe to go on an adventure to forbidden
Z-levels, admins probably don't appreciate these adventures so much.
## Changelog
:cl: VexingRaven
fix: Soul Scythes can no longer phase through the floor into Centcom.
/:cl:

* Fixes multi-Z ruins (Ice Moon Mining Site) not spawning (#70097)

* Fixes multi-z ruins not spawning

* I should proably commit said changelog files.

* Proc Ref wrapping

* Update to the correct procs

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: VexingRaven <msgerbs@users.noreply.github.com>

---

