## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-30](docs/good-messages/2022/2022-12-30.md)


1,839,701 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,839,701 were push events containing 2,485,639 commit messages that amount to 158,187,980 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 47 messages:


## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[cba002fa91...](https://github.com/Striders13/tgstation/commit/cba002fa912f07112fbbedcab330a35e2bffeab7)
#### Friday 2022-12-30 00:02:11 by Sol N

converts contraband file into poster file, makes holiday posters work (kind of) (#72131)

## About The Pull Request

The first part of this is just something that bothered me when I was
messing around with something that I will PR in the new year,
contraband.dm and dmi is ONLY posters. There's nothing else in there and
there are plenty of official posters, and if with #71717 we will also
add holiday posters to the mix then I think that its time to retire
contraband and make it poster.

Some small things I did while messing with it was change some variables
that were single letters into actual variable names, but overall this
part of the pr is not a player facing change.

That said, speaking of #71717 I think that it didn't work? Or didn't
work the way that it was supposed to? All of the spawned posters aren't
instances of festive posters, they are instances of normal posters, so
the code on initialize was not doing anything and the only reason the
holiday_none poster was showing up was because of the proc in randomize
spawning the posters in as those other posters. Because it didn't
actually _become_ poster/official/festive it never could do the proc
that turns it into a poster for the holiday that is actually occurring.

But then when I made it work and it turned into the generic posters I
decided that it would be better if instead of 30% of all posters being a
half finished mess, that if there wasn't a holiday poster it just
wouldn't replace them at all. I have poster Ideas and Dreams so I will
try to help with adding to more holiday posters but not in this PR.

What IS in this PR though, is a new traitor poster that appears during
the holidays.

![dreamseeker_MxxBzXIxiy](https://user-images.githubusercontent.com/116288367/208793262-9d4a45dc-f7bb-4208-b3c3-78cb68cf9af5.png)

This is a generic evil holiday poster that will replace normal evil
posters in the evil poster objective, because I agree with #72003 that
it should be a feature.

## Why It's Good For The Game

Contraband file is just posters already, this is easier for people to
find the posters.
I like holiday posters and think that we should have them and add more,
it is a fun easy thing to add to a lot of the microholidays to make them
more visible in addition to the name generation, but I don't want to see
the unfinished holiday poster so I do think that it's better to only
have them spawn if the holiday actually has a poster. Looking forward to
febuary!

## Changelog

:cl:
add: during holidays the spread syndicate propaganda through posters
objective has a chance of spawning evil holiday poster
fix: framework for holiday posters is more functional and modular
code: contraband.dm file and contraband.dmi file are both now poster.dm
and poster.dmi
/:cl:

---
## [i3roly/CMI8788](https://github.com/i3roly/CMI8788)@[0adef3c507...](https://github.com/i3roly/CMI8788/commit/0adef3c507c0227c91e1554ec81931d87aacec9f)
#### Friday 2022-12-30 00:40:13 by gagan sidhu

small change, HAUGE difference, same result: tim cook went full <YOU KNOW WHAT>

- so ofc APPUL, being APPUL, saying the word with such enthusiasm you'd think their cheeks are going to explode, decided they were "too good" for {in,out}{b,w,l}
	-instead, you have to use IOMapped{Read,Write}

i figured this out when i was looking at the code figuring out why getCurrentSampleFrame was crashing so badly. turned out the address being written to the register was (likely) being translated to the true physical value.
	-ofc APPUL, again, being APPUL, decided not to tell anyone this.
	-i don't even know how in/out does this. but it will take a value you write, and return something else via read.
			-conclusion: Clemens is one HARD MFer.

the end result was subtracting the (true?) physical address returned by in{w} from the virtual (always virtual with APPUL no matter what, unless we use in/out) returned by ->getPhysicalAddress().
	-of course this is wrong.

-so i had to figure out why exactly this was happening, and i learned that NOTHING was being written to the pci bus!! NOTHING!!
	-the detection of the H6 card (correct) was a fluke, because its value is zero!!

phil, the mac god, aka @pmj, was educating me about this situation a few years ago:
	- https://stackoverflow.com/questions/61143416/os-x-kernel-panic-when-attempting-to-access-pci-memory-mapped-register

NOW, i have verified that these IOMappedFunctions actually allow the address the kernel specifies, and i assume down the line in/out are called. (https://github.com/apple/darwin-xnu/blob/main/iokit/Kernel/IOMapper.cpp#L370)
	-the important thing is the registers for each stream are now holding the right address in memory, so whenever we call getCurrentSampleFrame, we get something that jives with our allocation's getPhysicalAddress()

pretty sure i'm the PCI god of OS X now.
	-well, i mean, phil obviously knows way more than me, but this is my own solution to a real problem that no one has figured out, because they haven't written a real PCI driver for OSX.
		-even the adapter cards that are out there today (like those cool sonnet cards) are plug and play because they find a way to make the right asic to leverage the existing apple drivers.
			-i am writing a new driver where no existing apple kext can help me.

this is awesome. now i know for sure the port mapped IO is working. what a fucking nuisance.

of course people you know this by now, but block-head, full-sleeve button-up, chest-high pantaloons, water-aided combover dweeb TIMMAY went FULL <YOU KNOW WHAT>
https://www.youtube.com/watch?v=X6WHBO_Qc-Q
	-if only today's climate would allow ben to make more of these.

good day
for winfrey
popped two-plus percent
stopped the blood
heaven-sent

cue the gorge
tonight she eatin' good
and she wantin more
like she always would

fat bitch gotta add her twist
got TIMMAY round her wrist
cue up the next APPUL tv special
your next propaganda vessel

macPCIgod - (aka tallest midget because no one does anything for APPUL when idiots like TIMMAY and his fat bitch stakeholder ruin things for money - "The Bloomberg Way").

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[80e6cd6a75...](https://github.com/TaleStation/TaleStation/commit/80e6cd6a75a00217c0767c717869adba53761693)
#### Friday 2022-12-30 00:44:50 by TaleStationBot

[MIRROR] [MDB IGNORE] Unfuckies pod blood (#3879)

* Unfuckies pod blood (#72323)

I broke it in #72220
Thanks to @Fikou for catching this
list(variable = 0.1) doesnt work on byond, so I last-minute improvised
and changed it to
list("[variable]" = 0.1), using a string instead of a typepath. I
already tested it thoroughly so decided it was probably good without
thinking of it anymore

:cl:
fix: fixes pod blood I swear
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

* Unfuckies pod blood

Co-authored-by: Time-Green <timkoster1@hotmail.com>
Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[eb6c0eb37c...](https://github.com/jlsnow301/tgstation/commit/eb6c0eb37c095c188074c7cec98bf5bf36a2cf04)
#### Friday 2022-12-30 01:06:16 by Jacquerel

Dogs use the Pet Command system (#72045)


About The Pull Request

Chiefly this refactors dogs to use the newer component/datum system for "pet which follows instructions". It also refactors it a little bit because I had better ideas while working on this than I had last week. Specifically, instead of passing around keys we just stick a weakref to our currently active behaviour in the blackboard. Basically the same but skipping an unecessary step.

Additionally it adds a component for the previous "befriending a mob by clicking it repeatedly" behaviour which hopefully we won't use too much because it's not very exciting (I am planning on replacing it for dogs some time after Christmas).
The biggest effort in here was making the Fetch command more generic, which includes multiple behaviours (which might be used on their own?) and another component (for holding an item without hands).

Additionally I noticed that dogs would keep following my instructions after they died.
This seems unideal, and would be unideal for virtually any AI controller, so I added it as an AI_flag just in case there's some circumstance where you do want to process AI on a dead mob.

Finally this should replicate all behaviour Ian already had plus "follow" (from rats) and a new bonus easter egg reaction, however I noticed that the fetch command is supposed to have Ian eat any food that you try to get him to fetch.
This has been broken for some time and I will be away from my desk for a couple weeks pretty soon, so I wrote the behaviour for this but left it unused. I will come back to this in the future, once I figure out a way to implement it which does not require adding the "you can hit this" flag to every edible item.

Also I had to refit the recent addition of dogs barking at felinids to fit into this, with a side effect that now dogs won't get mad at a Felinid they are friends with. This... feels like intended behaviour anyway?
Why It's Good For The Game

It's good for these to work the same way instead of reimplementing the same behaviour in multiple files.
Being able to have Ian (or other dogs) follow you around the station is both fun and cute, and also makes him significantly more vulnerable to being murdered.
Changelog

cl
add: Ian has learned some new tricks, tell him what a good boy he is!
add: Ian will come on a walk with you, if you are his friend.
refactor: Ian's tricks work the same way as some other mobs' tricks and should be extendable to future mobs.
fix: Dogs no longer run at the maximum possible speed for a mob at all times.
add: When Ian gets old, he also slows down. Poor little guy.
add: Dogs will no longer dislike the presence of Felinids who have taken the time to befriend them.
/cl

---
## [nbitzz/monofile](https://github.com/nbitzz/monofile)@[3ef9eeaf4c...](https://github.com/nbitzz/monofile/commit/3ef9eeaf4c9868155216dc86c515c6192961023b)
#### Friday 2022-12-30 01:12:53 by stringsplit

this code actually sucks ass
god bless anyone who reads this
1.2.1 i'll need to clean this shit up lmao

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b96f7d31b0...](https://github.com/treckstar/yolo-octo-hipster/commit/b96f7d31b07f46afb22418e7317f866da7656a78)
#### Friday 2022-12-30 01:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [nicholasgalante1997/couch-gag](https://github.com/nicholasgalante1997/couch-gag)@[099404ed2c...](https://github.com/nicholasgalante1997/couch-gag/commit/099404ed2cceca9cb37a75b3768f8f3c87564d98)
#### Friday 2022-12-30 02:11:32 by Nick Galante __asus

i swear to god asus makes absolute trash computers. never buy one. fuck you asus!

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[4d88f6e437...](https://github.com/Hatterhat/Skyrat-tg/commit/4d88f6e437ee794624e5d3b268a4bf37359832c7)
#### Friday 2022-12-30 02:33:49 by SkyratBot

[MIRROR] Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. [MDB IGNORE] (#17893)

* Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

* Corrects error in stamina HUD element display calculation. Increases stamina HUD readability.

Co-authored-by: itseasytosee <55666666+itseasytosee@users.noreply.github.com>

---
## [avar/git](https://github.com/avar/git)@[3e9c4df61f...](https://github.com/avar/git/commit/3e9c4df61fe966591038ff78cf161d9aab0b6a3c)
#### Friday 2022-12-30 03:12:55 by Ævar Arnfjörð Bjarmason

rebase & sequencer API: fix get_replay_opts() leak in "rebase"

Make the recently added replay_opts_release() function non-static and
use it for freeing the "struct replay_opts" constructed by the
get_replay_opts() function in "builtin/rebase.c". See [1] for the
initial addition of get_replay_opts().

To safely call our new replay_opts_release() we'll need to change all
the free() to a FREE_AND_NULL(), and set "xopts_nr" to "0" after we
loop over it and free() it (the free() in the loop doesn't need to be
a FREE_AND_NULL()).

This is because in e.g. do_interactive_rebase() we construct a "struct
replay_opts" with "get_replay_opts()", and then call
"complete_action()". If we get far enough in that function without
encountering errors we'll call "pick_commits()" which (indirectly)
calls sequencer_remove_state() at the end.

But if we encounter errors anywhere along the way we'd punt out early,
and not free() the memory we allocated. Remembering whether we
previously called sequencer_remove_state() would be a hassle, so let's
make it safe to re-invoke replay_opts_release() instead.

I experimented with a change to be more paranoid instead, i.e. to
exhaustively check our state via an enum. We could make sure that we:

- Only allow calling "replay_opts_release()" after
  "sequencer_remove_state()", but not the other way around.

- Forbid invoking either function twice in a row.

But such paranoia isn't warranted here, let's instead take the easy
way out and FREE_AND_NULL() this.

See [2] for the initial implementation of "sequencer_remove_state()",
which assumed that it should be removing the full (including on-disk)
rebase state as a one-off.

1. 73fdc535d26 (rebase -i: use struct rebase_options to parse args,
   2019-04-17)
2. 26ae337be11 (revert: Introduce --reset to remove sequencer state,
   2011-08-04)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[58b61a17a7...](https://github.com/Donglesplonge/tgstation/commit/58b61a17a78e90ea9da91351572abee9a4f93ccb)
#### Friday 2022-12-30 03:17:15 by Jacquerel

Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[2327e445d2...](https://github.com/Gofawful5/Skyrat-tg/commit/2327e445d26e20ab410a5f97109d2088c00681ce)
#### Friday 2022-12-30 03:17:41 by SkyratBot

[MIRROR] Gatfruit will no longer drop from ice portals. [MDB IGNORE] (#18202)

* Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.

![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.

![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

* Gatfruit will no longer drop from ice portals.

Co-authored-by: carshalash <carshalash@gmail.com>

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[cd13fcdf46...](https://github.com/Sonic121x/Skyrat-tg/commit/cd13fcdf467b1a9fe5d8fc5256552b0601284dca)
#### Friday 2022-12-30 03:48:28 by Jolly

[MODULAR] contraband.dmi is no longer a hard override on posters (#18106)

* hhngh

* dunks this fucking dmi

* fuck you

---
## [Unknownity/cmss13](https://github.com/Unknownity/cmss13)@[15af7f1ee5...](https://github.com/Unknownity/cmss13/commit/15af7f1ee5e7dbd568ea01b53c993e127b4bdb12)
#### Friday 2022-12-30 04:14:57 by ThePiachu

Cargo ammo and ammo box mapping (re-up) (#1759)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Previous version of this PR ( #1650 ) claimed to have changed 384 files,
which would be impossible to review. So re-uploading this PR with
hopefully a sane amount of files changed...

---

When I was playing cargo I spent a good half an hour in a round just
mindlessly packing ammo magazines into boxes in squad prep. It didn't
put a dent in the squad prep supply, and I barely got a handful of
boxes. So I thought to myself that this is pretty much a waste of time
for cargo and decided to code a better solution:

https://www.youtube.com/watch?v=cnXcEYAV8P4

So now select vendors (opt-in via `VEND_LOAD_AMMO_BOXES`) support ammo
consolidation. They count the number of ammo magazines you have and from
that they derive the number of magazine boxes you can vend. If you vend
a magazine, it updates the number of boxes available, and if you vend a
box, it updates the number of magazines available (as well as all
derived boxes - see the 3 pack of grenades and 25 pack box).

The `item_to_box_mapping` tracks ammo boxes (minus loose ammo), grenade
boxes, grenade packets and mine boxes.

Most notable affected vendors - Requisition ammo vendor, Requisition
vendor that features grenades, Squad vendors that have ammo in them.

So now Requisition will be able to easily raid Squad Vendors to stock up
their ammo drops and save countless hours of mind-numbing cargo work.

This code ALSO correctly works when you're re-stocking a vendor with
either individual magazines or magazine boxes. Correct amounts are
updated everywhere. So you *could* take a magazine box, put it in a
vendor and thus let people vend 16 magazines out of it seemlessly.
Really useful just incase you need to restock Requisitions with
individual ammo or something...

Other notes:
- Boxes of magazines are put directly under the corresponding ammo so
you can vend them in larger amounts easier. Useful for 3-packs of
grenades
- We should add a Shotgun Shell Box Box so we can also handle those
easily...
- Nailgun ammo box had to be converted from being /smg/ since that
created an invalid ammo box that nobody used.
- Nulled out a magazine type for an intermediary box that later gets
used for MREs and all that

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Gameplay around loading magazines into ammo boxes is not interesting, so
cutting it down to minimum is for the best.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
add: Added an automated ammo box management system to various vendors
stocking bulk ammo and grenades. It will automatically combine ammo
magazine into boxes, and divide boxes into individual magazines (or
grenades, MRE packets, etc.). The boxes will appear at the bottom of the
vendor (yes, this also includes the regular grenade boxes that used to
be higher).
qol: Cargo will no longer need to pack individual vended ammo magazines
into boxes thanks to the ammo box management system. Your chains have
been broken!
qol: Requisitions vendor now stocks 3-packs of grenades as well as
individual HEDP grenades.
qol: Requisitions ammo vendor now can vend a lot more individual
magazines (actual number of magazines remains unchanged, just the ammo
boxes have been consolidated into magazines).
qol: Requisition vendors now vend to floor when they are not vending to
the front desks. This will make filling crates of ammo boxes or rappels
easier.
code: Minor changes to code around some ammo boxes to remove one phantom
box and prevent intermediate box types from being indexed when they
shouldn't be.
code: Refactored the code that checks whether items are in mint enough
condition to re-stock.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [Fabinistere/fight_arena](https://github.com/Fabinistere/fight_arena)@[2e6c3aeb8b...](https://github.com/Fabinistere/fight_arena/commit/2e6c3aeb8b0a6a919c2197947e2a2c62eec0d555)
#### Friday 2022-12-30 04:15:22 by Wabtey

add Durability and CleanUp and add FEAR resistance

Restructure of Event (related with combat placed in Combat, etc)

- dialog_box
  - update_dialog_panel
    - refactor how to detect dialog change;
    by looking at directly the DialogPanel,
    instead of the Entity Interlocutor which their dialog is being change only after the update_dialog_tree.
    Fix the bug: Reset the text even if there is no change
    - Activate Event (by adding them in their plugin)
    Fix the bug:  Need to skip twice (or more) to exit a node
  - end_node_dialog
    - extraction of update_dialog_panel
- dialog_player
  - dialog_dive
    - extraction for a NeverNester Behavior
    - Only modify UIPanel or Scroll
    (for exception like monologue)
  - hide_empty_button:
  Disable empty button
    - prevent crash by selecting a non accepted button
- dialog_system
  - fix print_file (issue with list of text/choice)
  - rm debug print
  - add print_file unit test
- npc
  - aggression
    - doc
  - movement
    - import
    - format
- combat
  - add the event to be processed
- debug
  - TODO in Debug

- vscode
  - add TODOs in logs

## FIXME

Still some issue to exit dialog

## Note

I have been VAPORIZED.
If God could existed, i dismembered them under my bed.
Dedication to gabriel, Apostate of Hate.

[cathartic laughter]

---
## [avatar2t/streamingmovie2023](https://github.com/avatar2t/streamingmovie2023)@[54caf95870...](https://github.com/avatar2t/streamingmovie2023/commit/54caf95870b6a4088b985d0ce3fdf2dcba2d95e4)
#### Friday 2022-12-30 04:16:20 by avatar2t

 Avatar 2  la voie de 2022 Français Gratuit et VF Complet

[FILMS VOIR] Avatar 2 : la voie de l'eau (2022) Français Gratuit et VF Complet
<a href="https://flixtv.bigmovies10.site/fr/movie/76600/avatar-the-way-of-water" style="font-size: 28px;" target="_blank">[VOIR]~ Avatar 2 Streaming VF | Gratuit en Francais VOSTFR</a>
➤ Avatar: la voie de l'eau Film Complet en streaming gratuit

Regarder le film Avatar : La voie de l'eau (2022) en streaming VF (VOSTFR) gratuit en Filmdailyplus | Avatar : La voie de l'eau (2022) film complet en français, streaming gratuitement sans limite de temps.

Les meilleurs sites pour regarder Avatar : La voie de l'eau un film en streaming gratuit en VF ou VOSTFR, en illimité et sans inscription.

<a href="https://flixtv.bigmovies10.site/fr/movie/76600/avatar-the-way-of-water" style="font-size: 28px;" target="_blank">➤ Avatar : La voie de l'eau (2022) film complet en français</a>
➤ https://flixtv.bigmovies10.site/fr/movie/76600/avatar-the-way-of-water

<a href="https://flixtv.bigmovies10.site/ro/movie/76600/avatar-the-way-of-water" target="_self"><img src="https://upload-os-bbs.hoyolab.com/upload/2022/12/28/297607217/ea86a1343ffbbc4f688a23ac26272fab_662051349000317745.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg" border="0" /></a>


Un autre site de Avatar : La voie de l'eau streaming de films en ligne gratuit pouvez également essayer est Dans cet article. Ce site propose de nombreux films classés en plusieurs catégories comme drame, action, comédie, science-fiction et bien d'autres.

Le site Web où Vous pouVez regarder des Films de Avatar : La voie de l'eau en streaming gratuit

14 décembre 2022 en salle / 3h 12min / Science fiction, Aventure, Fantastique, Action
De James Cameron
Par Amanda Silver, James Cameron
Avec Sam Worthington, Zoe Saldana, Sigourney Weaver
Titre original Avatar: The Way of Water

SYNOPSIS
Avertissement : des scènes, des propos ou des images peuvent heurter la sensibilité des spectateurs
Se déroulant plus d’une décennie après les événements relatés dans le premier film, AVATAR : LA VOIE DE L’EAU raconte l'histoire des membres de la famille Sully (Jake, Neytiri et leurs enfants), les épreuves auxquelles ils sont confrontés, les chemins qu’ils doivent emprunter pour se protéger les uns les autres, les batailles qu’ils doivent mener pour rester en vie et les tragédies qu'ils endurent.

D'après Avatar : La voie de l'eau de Paolo Cognetti.

En chemin, Benimaru et Limule font la rencontre de Hiiro, un ogre qui tient Benimaru en grand respect, et qui pourrait bien avoir de véritables liens avec ce dernier…

Qui est vraiment Hiiro et que se passe-t-il réellement au pays de Raja ? Le slime le plus fort du monde s’engage dans une nouvelle grande aventure !


Avatar : La voie de l'eau is a 2022 American superhero film based on the Marvel Comics character Black Panther. Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures, it is the sequel to Black Panther (2018) and the 30th film in the Marvel Cinematic Universe (MCU). Directed by Ryan Coogler, who co-wrote the screenplay with Joe Robert Cole, the film stars Letitia Wright, Lupita Nyong'o, Danai Gurira, Winston Duke, Florence Kasumba, Dominique Thorne, Michaela Coel, Tenoch Huerta, Martin Freeman, and Angela Bassett. In the film, the leaders of Wakanda fight to protect their nation in the wake of King T'Challa's death.

Ideas for a sequel began after the release of Black Panther in February 2018. Coogler negotiated to return as director in the following months, and Marvel Studios officially confirmed the sequel's development in mid-2019. Plans for the film changed in August 2020 when Black Panther star Chadwick Boseman died from colon cancer, with Marvel choosing not to recast his role of T'Challa. Other main cast members from the first film were confirmed to return by that November, and the title was announced in May 2021. Production initially took place from late June to early November 2021, in Atlanta and Brunswick, Georgia, as well as around Massachusetts, before a hiatus to allow Wright to recover from an injury sustained during filming. Production resumed by mid-January 2022 and wrapped in late March in Puerto Rico.

Avatar : La voie de l'eau premiered at the El Capitan Theatre and the Dolby Theatre in Hollywood on October 26, 2022, and was released in the United States on November 11, 2022, as the final film in Phase Four of the MCU. The film received positive reviews from critics, who praised the cast's performances (particularly Wright's, Huerta's, and Bassett's), emotional weight, Coogler's direction, action sequences, musical score, and tribute to Boseman.

Sortie du film Avatar : La voie de l'eau : Date de sortie?


L’intrigue du film Avatar : La voie de l'eau

Queen Ramonda, Shuri, M’Baku, Okoye and the Dora Milaje fight to protect their nation from intervening world powers in the wake of King T’Challa’s death. As the Wakandans strive to embrace their next chapter, the heroes must band together with the help of War Dog Nakia and Everett Ross and forge a new path for the kingdom of Wakanda.

Pour regarder Avatar : La voie de l'eau des films gratuitement sur Internet, sans avoir à se soucier des sanctions pénales encourues, rien de mieux que le streaming ! Il existe aujourd’hui plusieurs sites streaming de séries gratuits et performants mais le meilleur actuellement est sûrement cineinc qui vous proposent de visionner vos Avatar : La voie de l'eau en streaming en Français. Profitez du meilleur streaming gratuit de 2021 ! Quoi de mieux que les longues soirées d’automne pour se regarder des films Avatar : La voie de l'eau en streaming entre amis ou en amoureux ou bien même en solo.

On adore vous savoir calé devant un bon film Avatar : La voie de l'eau sur internet, alors le s’est donné pour mission de vous aider en vous donnant cette sites internet fabuleuse qui va sauver bon nombre de vos soirées au coin du feu (ou du radiateur quoi).

Vous allez pouvoir binger sévère ! L’occasion pour vous de voir Avatar : La voie de l'eau films que vous aimez ou que vous attendiez de découvrir.

Pouvoir regarder un film Avatar : La voie de l'eau gratuitement sur internet chez soi sans prendre le risque du téléchargement illégal c’est quand même bien sympa. Mais trouver un site de streaming gratuit et fiable pour avoir accès à des séries et des films ce n’est pas toujours simple. Oh ça non. On en sait tous quelque chose pas vrai ?

On peut errer sur le net pendant des heures avant de trouver son bonheur. Surtout si vous cherchez à regarder en streaming Avatar : La voie de l'eau films en VF ou VOSTFR. Le choix est encore plus restreint. Alors on a fait pour vous une petite des meilleurs sites de streaming gratuits pour Avatar : La voie de l'eau film. Ou les deux.

Ne nous remerciez pas. Enfin si, vous pouvez mais ça nous fait vraiment plaisir de vous aider. On vous a trouvé le Avatar : La voie de l'eau streaming gratuits. La crème de la crème. Si vous êtes équipés d’une bonne connexion internet (sans avoir un truc monstrueux non plus hein), vous trouverez forcément votre Avatar : La voie de l'eau . Ou alors c’est que vous êtes bien difficiles…

Retournez voir une seconde fois et faites attention. RegarderIp Man 4 : Le dernier combat Movie WEB-DL Il s’agit d’un fichier extrait sans erreur d’un serveur telLe Voyage du Pèlerin,tel que Netflix, ALe Voyage du Pèlerinzon Video, Hulu, Crunchyroll, DiscoveryGO, BBC iPlayer, etc. Il s’agit également d’un film ou d’une é Avatar : La voie de l'eau ion télévisée téléchargé via un site web comme on lineistribution, iTunes. La qualité est assez bonne car ils ne sont pas ré-encodés.

Les flux vidéo (H.264 ou H.265) et audio sont généralement extraits de iTunes ou d’ALe Voyage du Pèlerinzon Video,

puis redistribués dans un conteneur MKV sans sacrifier la qualité. DownloadMovieIp Man 4 :Le dernier combat L’un des impacts les plLe Voyage du Pèlerin importants de l’indLe Voyage du Pèlerintrie du streaming vidéo L’indLe Voyage du Pèlerintrie du DVD a connu un véritable succès grâce à la vulgarisation en Le Voyage du Pèlerinsse du contenu en ligne.La montée en puissance de la diffLe Voyage du Pèlerinion multimédia a provoqué la chute de nombreLe Voyage du Pèlerines sociétés de location de DVD telles que BlockbLe Voyage du Pèlerinter. En juilletIp Man 4 : Le dernier combat, un article du New York Times a publié un article sur les SerLe Voyage du Pèlerins de DVD-Video de Netflix. Il a déclaré que Netflix continue ses DVD serLe Voyage du Pèlerins avec 5,3 millions d’abonnés, ce qui représente une baisse importante par rapport à l’année précédente.

Quelle est la différence entre le téléchargement et streaming ?

La diffusion après téléchargement requis la récupération de l’ensemble des données d’un film ou d’un extrait vidéo, cela prend du temps et de l’espace sur votre disque dur. L’avantage du streaming vous n’avez rien à télécharger, il permet la lecture d’un flux audio ou vidéo que vous pouvez lire directement depuis un lecteur proposé le plus souvent par des plateformes qui proposent plusieurs films, séries ou morceaux musicaux.

étiquette :

Avatar : La voie de l'eau film complet

Avatar : La voie de l'eau 2022 film complet

Avatar : La voie de l'eau film complet en français

Avatar : La voie de l'eau streaming vostfr

Avatar : La voie de l'eau film streaming

Avatar : La voie de l'eau streaming vf

---
## [rj-cc/cinnamoncoffeelandingpagedraft](https://github.com/rj-cc/cinnamoncoffeelandingpagedraft)@[d401b96bc1...](https://github.com/rj-cc/cinnamoncoffeelandingpagedraft/commit/d401b96bc18dd62fab9fe4db189341601d21738a)
#### Friday 2022-12-30 04:20:43 by Raul Jesus C. Cabarong Jr

Update README.md

Coffee Shop Landing Page Draft
As I wanted also to have a coffee shop business and my girlfriend bakes delicious cinnamon rolls, I made this project which can be utilized later on for our dream business. 
https://rj-cc.github.io/cinnamoncoffeelandingpagedraft/

---
## [himanshutamboli/Practice-Datasets](https://github.com/himanshutamboli/Practice-Datasets)@[f6d5910a8b...](https://github.com/himanshutamboli/Practice-Datasets/commit/f6d5910a8b7c2b8b4efb349b4fe037d2ef0e02b2)
#### Friday 2022-12-30 05:04:47 by Himanshu Tamboli

Add files via upload

Practice Project - 2: Medical Cost - Personal Insurance Dataset (type_1)

Problem Statement:
Insurance Forecast by using Regression Algorithms (tried every algorithm)

Health insurance is a type of insurance that covers medical expenses that arise due to an illness. These expenses could be related to hospitalisation costs, cost of medicines or doctor consultation fees. The main purpose of medical insurance is to receive the best medical care without any strain on your finances. Health insurance plans offer protection against high medical costs. It covers hospitalization expenses, day care procedures, domiciliary expenses, and ambulance charges, besides many others. Based on certain input features such as age, bmi, no of dependents, smoker, region -- medical insurance is calculated.

Columns details:

· age: Age of primary beneficiary

· sex: Insurance contractor gender, female, male

· bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9

· children: Number of children covered by health insurance / Number of dependents

· smoker: Smoking

· region: The beneficiary's residential area in the US, northeast, southeast, southwest, northwest

· charges: Individual medical costs billed by health insurance

Predicting charges: Can you accurately predict insurance costs?

Downlaod Files:
https://github.com/dsrscientist/dataset4
https://github.com/dsrscientist/dataset4/blob/main/medical_cost_insurance.csv

P.S. - We are using Linear Regression algorithm for this medical insurance cost prediction model to predict the medical insurance charges of a person based on the given data.

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[50929f054b...](https://github.com/Holoo-1/tgstation/commit/50929f054b89cab80a1e501b7a01bc74c79163d7)
#### Friday 2022-12-30 08:37:41 by GuillaumePrata

Goliath dna infusion (#71657)

## About The Pull Request
This is a baseline version of the organs and I intend on polishing them
more in the future (Hopefully after other faunas get added to the
infuser.)

Now, this PR adds goliaths to the DNA infuser at genetics. It gives 4
organs and a final bonus effect.

1- Goliath eyes: Simple mostly filler organ that gives night vision.
2- Goliath lungs: Allow miners to breath either lavaland or the default
air mix. As a side effect they can't breath pure O2 anymore so internals
can't be used. Stay away from N2O or use your gas mask properly.
3- Goliath heart: Give miner ash storm protection
4- Goliath brain: Turns one of the miner's arm into a tendril goliath
hammer that can be used to mine. Like the mounted chainsaw it cannot be
dropped, it has slower atk speed, deals 20 damage by default and a bonus
80 to lavaland fauna, it also acts as a baseball bat against fauna so
you can dodge being hit back with good timing.
As a side effect, you can't equip gloves as your hand is a big ass
hammer...

The extra effect for having all 4 organs is lava immunity for now, I
really want to turn it into something more interesting later.

GAGS organs and bonus coderspriter arm:
![goliath
sprites](https://user-images.githubusercontent.com/55374212/205477889-22cfa586-dd43-405d-80cf-3981b31304e1.png)
If I have time I might animate the arm later.
## Why It's Good For The Game
This add some useful tools for miners if they opt into asking genetics
for help and bother to drag a goliath corpses to it.
The organs can be useful on the station, but they will only really shine
at lavaland.

We were brainstorming more things that miners can get from the station
on their downtime waiting the cargo shuttle to bring their bought gear,
this would be a simple and easy power up for miners that can have some
small (ignoring the hammer arm) bonus to miners, but small power ups
pile up.

I also wrote a hackMD around these organs, their goals, non goals,
future possibilities for fauna organs (goliath and others) etc.
https://hackmd.io/@GuillaumePrata/goliath_infusion_organs

## Changelog
:cl: Guillaume Prata
add: Geneticists figured out how to infuse goliath DNA into humanoids!
(Many monkeys were harmed in the process!)
add: Goliath eyes for nightvision, lungs to breath at lavaland safely,
heart to protect you from ash storms and the brain which turns one of
your arms into a tendril hammer.
add: Tendril hammer: Your arm becomes a giant mass of plate and tendril
but it won't fit on gloves anymore. While slow to swing around, you can
obliterate fauna/megafauna with it, 20 base dmg + 80 bonus damage to
fauna/megafauna with a bonus knockback.
/:cl:

---
## [BeatAroundTheBuscher/ROSIGMA](https://github.com/BeatAroundTheBuscher/ROSIGMA)@[a72f0768a2...](https://github.com/BeatAroundTheBuscher/ROSIGMA/commit/a72f0768a298af75659378e6c1408ca168bdcedd)
#### Friday 2022-12-30 09:17:04 by Surrealaser

1. Completed and added the Dekker Twincore Plasma rifle to the game complete with working plasma heat mechanics.

2. Inquisition Stormtroopers:
-Now have access to three additional weapons, the Longlas, Twincore Plasma Rifle and the Multimelta. The Plasma Rifle and Multimelta require requisite research to unlock and use (Dekker Plasma Rifle and the Multimelta). 
-The Longlas armor grants the Analyze ability as well as superior Anti-Camo, Thermal and Night Vision; ideal for a scout or sniper.
-Special Psi Defense bonus has been reduced by 50 to account for their Psi Strength no longer being bugged.
-Inquisitor Stormtroopers are now immune to zombification due to their warded armor.

3. Drain Scripts: Scripts that leech HP, TU, Morale, etc on hit and kill, these have been refined with added functionality, including fatal wound removal. Currently only in use by the Daemonette Claws, Khorne Berserker Axe, Bloodletter Sword and Valkyrie Spear, but I intend to expand this functionality to other weapons.

4. Gauss Weapons: Standardization and canon accuracy improved.

5. Whitespace removal.

6. Khorne Berserkers get a special Khorne blessed chainaxe exclusive to them, and are generally a little more scary.

---
## [NSU-FIT-Operating-Systems/20201-POSIX-Threads](https://github.com/NSU-FIT-Operating-Systems/20201-POSIX-Threads)@[4c2d00ecee...](https://github.com/NSU-FIT-Operating-Systems/20201-POSIX-Threads/commit/4c2d00ecee6c814524f02de59d24f60a08217b63)
#### Friday 2022-12-30 09:43:02 by Alexander Yanin

a.yanin/common: Create a new common module `loop`

After prolonged deliberation, I've decided to create a simple event loop
that would support async TCP socket operations.

The event loop design is directly inspired by libuv,
with a few minor differences.

- the extensive use of the `error` and `log` modules because I don't
  care about other people's use-cases

- fearless memory allocations (since I've kept avoiding them for some
  reason while having a machine with 16 GiB of RAM)

- `poll` instead of the clearly superior `epoll` because POSIX...
  at least it's not `select`, duh.

- the extensible handler interface
  - they'll be responsible for juggling callbacks

- a decoupled executor interface (now that I think of it, it looks
  really similar to Java's executors... that's scary.)

I'm still thinking where to put the I/O operations in this picture
so that they wouldn't be a royal pain.

The goal is to have an overwhelmingly large part of the codebase shared
among the 31st and 33rd labs; the only difference there being
a different choice of the executor (single-threaded vs thread pool).

And since I anticipate (and actively hope) that this will be my last
grand effort writing code in C, I'm going extravagant with my designs.
To the detriment of the poor people who'll have to review this.
To them I say this: I'm not sorry at all.

---
## [Perl/perl5](https://github.com/Perl/perl5)@[0bd7fce725...](https://github.com/Perl/perl5/commit/0bd7fce7251f538cff3f3188eec4566188889826)
#### Friday 2022-12-30 09:50:49 by Yves Orton

regcomp.c etc - rework branch reset so it works properly

Branch reset was hacked in without much thought about how it might interact
with other features. Over time we added named capture and recursive patterns
with GOSUB, but I guess because branch reset is somewhat esoteric we didnt
notice the accumulating issues related to it.

The main problem was my original hack used a fairly simple device to give
multiple OPEN/CLOSE opcodes the same target buffer id. When it was introduced
this was fine. When GOSUB was added later however, we overlooked at that this
broke a key part of the book-keeping for GOSUB.

A GOSUB regop needs to know where to jump to, and which close paren to stop
at. However the structure of the regexp program can change from the time the
regop is created. This means we keep track of every OPEN/CLOSE regop we
encounter during parsing, and when something is inserted into the middle of
the program we make sure to move the offsets we store for the OPEN/CLOSE data.
This is essentially keyed and scaled to the number of parens we have seen.
When branch reset is used however the number of OPEN/CLOSE regops is more than
the number of logical buffers we have seen, and we only move one of the
OPEN/CLOSE buffers that is in the branch reset. Which of course breaks things.

Another issues with branch reset is that it creates weird artifacts like this:
/(?|(?<a>a)|(?<b>b))(?&a)(?&b)/ where the (?&b) actually maps to the (?<a>a)
capture buffer because they both have the same id. Another case is that you
cannot check if $+{b} matched and $+{a} did not, because conceptually they
were the same buffer under the hood.

These bugs are now fixed. The "aliasing" of capture buffers to each other is
now done virtually, and under the hood each capture buffer is distinct. We
introduce the concept of a "logical parno" which is the user visible capture
buffer id, and keep it distinct from the true capture buffer id. Most of the
internal logic uses the "true parno" for its business, so a bunch of problems
go away, and we keep maps from logical to physical parnos, and vice versa,
along with a map that gives use the "next physical parno with the same
logical parno". Thus we can quickly skip through the physical capture buffers
to find the one that matched. This means we also have to introduce a
logical_total_parens as well, to complement the already existing total_parens.
The latter refers to the true number of capture buffers. The former represents
the logical number visible to the user.

It is helpful to consider the following table:

  Logical:    $1      $2     $3       $2     $3     $4     $2     $5
  Physical:    1       2      3        4      5      6      7      8
  Next:        0       4      5        7      0      0      0      0
  Pattern:   /(pre)(?|(?<a>a)(?<b>b)|(?<c>c)(?<d>d)(?<e>e)|(?<f>))(post)/

The names are mapped to physical buffers. So $+{b} will show what is in
physical buffer 3. But $3 will show whichever of buffer 3 or 5 matched.
Similarly @{^CAPTURE} will contain 5 elements, not 8. But %+ will contain all
6 named buffers.

Since the need to map these values is rare, we only store these maps when they
are needed and branch reset has been used, when they are NULL it is assumed
that physical and logical buffers are identical.

Currently the way this change is implemented will likely break plug in regexp
engines because they will be missing the new logical_total_parens field at
the very least. Given that the perl internals code is somewhat poorly
abstracted from the regexp engine, with parts of the abstraction leaking out,
I think this is acceptable. If we want to make plug in regexp engines work
properly IMO we need to add some more hooks that they need to implement than
we currently do. For instance mg.c does more work than it should. Given there
are only a few plug in regexp engines and that it is specialized work, I
think this is acceptable. We can work with the authors to refine the API
properly later.

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[ae02bd97ff...](https://github.com/AnywayFarus/Skyrat-tg/commit/ae02bd97ff71d2f4714b4ea7c8076acf21ed06c6)
#### Friday 2022-12-30 10:03:59 by OrionTheFox

Gunset case resprite (#18119)

* Noice Icons

* smol

* ccode 4 icon

* Fuck it. We Webedit.

* Oh this should go too

* i hate commas anyways

Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [mattdway/CreateWithVR](https://github.com/mattdway/CreateWithVR)@[c50dc76c3d...](https://github.com/mattdway/CreateWithVR/commit/c50dc76c3d6cfef69c505a35cafe3a7b2ab699d9)
#### Friday 2022-12-30 10:18:04 by mattdway

12-30-22 Commit v2.8.1

12-30-22 v2.8.1
12-30-22 Commit

Dev Log For 12/29/22 and 12/30/22 (into the evening):

I added an isGrabbed bool, per the suggestion of Nemu in the comment section of Valem Tutorials video on physics hands.  Grabbing an item still disables all colliders on both hands and dropping an item re-enables all colliders on both hands after a .5 second delay.  The real change to adding the bool is that when dropping an item and grabbing an item again quickly before that .5 second countdown concludes, the collider does not re-enable.

Before when dropping and picking up an item within short succession (for example when switching an item from the left hand to the right hand or vice versa or when dropping and picking up an item again, such as to reload the darts or the staples, the collider would re-enable while still holding the item.

This caused two distinct and noticeable bugs.  First, your opposite hand could suddenly interact with the item you are holding which, for larger items, caused all sorts of physics issues -- especially if accidently bumping the item in your hand around while carrying it.  This was most noticeable when carrying larger items such as a piece of art off the walls or the watering can (which can be somewhat annoying when tipped).  Secondly, when holding an item and having the collider enabled on the same hand, when letting go of the item a collision could (and often) did occur causing the item you dropped to be unintentionally flung across the room in a violent fashion instead of dropping to the ground where you stood.

I tested this with both switching an item between the right and left hand and in dropping and immediately picking the object up again and the colliders stay off for both hands in both scenarios now, which is much more stable and works a lot better from a mechanic stand-point.

Another idea I had for my room.  The water bottle already spins uncontrollably whenever you are both holding it and you put on the lid.  The collisions cause it to spin in a circle in your hand and when you let it go sometimes the water bottle lands right side up and sometimes not.  Rather than fix this (as this is an interesting and amusing bug) I think I'm going to keep it as a fun little easter egg interaction for the room.  Tonight I created a note out of a white plane and a text mesh pro component that says "Can you complete the water bottle flip challenge?" and I placed that under the bottle and the lid.  I also created an empty  game object to house all three and I moved these closer to the table's edge to make it easier to reach without having to use distance grabbing.  I made this note a XR Grab Interactable with a collider and rigidbody.

What I'd also like to do is add a quick script so that if the water bottle is in the air and then drops right side up (collider on the bottom of the bottle on the Y axis) then a cheering sound plays.  And if it lands on either side axis (I'd put colliders there too) a booing sound plays.  It would be a fun way to add a silly little interaction.  Maybe later I'd even come back and add a scoring system to it to count how many times it lands right side up vs. not.

I didn't specify that you put the lid on to spin it but if I hope the subtle hint of having the lid and bottle on top of the bottle would be a clue that you can get some real spin by putting it on and I don't want to spell it all out but for there to be a little self discovery there.

I also added the colliders necessary to determine if the bottle has hit right side up or on any other plane and I also added a script component to this bottle (but I haven't yet written the script that will go with this).

I fixed the north wall collider, which was back too far and allowed objects to partially clip when pressed against the wall (this is because the collider was behind the mesh render rather than in front of it).

I fixed the decretive record_blue so that you can now pick this up by recreating this item and setting it as an XR Interactable with a collider and a rigid body and configuring.

I fixed all of the locomotion settings on the Settings menu: Continuous_Movement_Settings_Toggle, Teleportation_Anywhere_Settings_Toggle and Teleportation_Limited_Settings_Toggle.  In the On Value Change (Boolean) section of each of these UI toggles I hadn't updated and added in the all of the new teleportation mats (with the mesh render turned off) I'd added to my room since.  There are 12 of these teleportation mats and 1 rug in my room now.  Thus, when selecting Continuous Motion not all of these teleportation anchors were being disabled and when selecting this toggle and when selecting Teleportation (Limited) and Teleportation (Anywhere) those teleportation anchors were not being re-enabled.

For neatness and tracking sake I went ahead and relinked all the teleportation mats and the teleportation rug in the exact same alphabetical order listed in the hierarchy, within the On Value Change (Boolean) for each of these three toggle menus I mentioned.  This makes it easier to see if I am missing any linked game objects in the future.  I also added TeleportAnchorWithFade.enabled (TeleportationAnchorWithFade > bool enabled) and I made sure that the currect checkbox was checked for each toggle.

I re-adjusted the collider on the back of the two dinning room chairs.  It was too far forward and I was able to move my hand through those chairs at will.  Readjusting the rotation and the X position helped.

Of note, I find that with the chairs and the dinning room table that if I move my hand fast enough I can still phase my hand through those objects.  This is not true on the outside walls/windows nor the couch arm.  No matter how fast I move my controller my hand hits those solidly.  I started to investigate and troubleshoot why (colliders and rigidbody settings are all the same and I experimented with does the collider's thickness make a difference so I increased the Y size of the collider but found that this did not solve the issue).  I've tabled this investigation for another day but I would like to figure it out.

I added a secret message to the back of the clock (Job Sim inspired) and I gave the clock a box collider, a rigidbody, and a XR Grab Interactable component so that this can be picked up.

I also added a socket hook (a duplicate of the art hook and socket) and I adjusted the settings on both the socket and on the clock so that this should work for socketing the clock to the wall.  I also adjusted the size of the sphere collider to be smaller and more akin to the size of the clock.

I also moved the clock from under the -- INTERACTIVE STATIC -- menu to the -- DYNAMIC -- menu, now that this clock is fully

A few things need fixing with the clock.

1.) That socket isn't working correctly and the clock falls down when starting the game.  This needs to be troubleshot and fixed.

2.) The clock does not respond to distance grabbing and the raycast, currently and this needs to also be fixed.

3.) The shadow for the clock is currently baked and I need to set this back to dynamic so that that shadow is no longer baked now that the clock is an interactable.  This also needs to be fixed.

4.) When picking up the clock for the first time rotating the clock is difficult.  I'm not sure why this is but when I drop the clock and re-pick up everything is fine again.  I also notice the first time I pick this up (albeit it is half-way clipped through the wall after falling) the attach is not being used.  Maybe once the other pieces have been fixed this will resolve itself.  If not I need to investigate, troubleshoot and fix this too.

The art socket on the north wall was way too large.  I resized it to be an appropriate radius and more akin to the other art sockets.

The north wall art can be picked up via distance grabbing while the art on the east and south walls cannot.  I don't recall if I disabled those on purpose due to collisions while being pulled towards you or not.  I need to test that and to at least make all the art work the same.  This is something I need to fix.

I fixed the cabinet door's rigidbody settings to be Continuous Speculative so that these would properly collide with the shelf colliders inside the cabinets.  I choose Continuous Speculative as I notice that my pseudo body collider (and more specifically the Character Controller that tilts forward when I lean forward) also has the ability to push in on these doors hard enough it skips through the collider (where as pushing with the physics hands does not) and I wanted to see ifi Continuous Speculative had the ability to better stop this from happening.  This had little to no effect on the cabinets when pushing against them with my pseudo collider so I may change this back to Continuous Dynamic later.

I don't have a great solution for the character controller pushing on the doors.  I could make these not interact but then any door (including the front door, at least when opened -- as I have a wall collider in front of the closed front door, currently to prevent this behavior) you'd be able to walk through.  Including when the front door is open, and that isn't a behavior I necessarily want unless this is really problematic.  I may need to come up with a different solution for this.

I ran into one weird bug in which when play testing I am facing the wall (punch lists) and all of the Continuous Motion controls are reversed (right is left, left is right, forwards is backwards and backwards is forwards.  I thought this was either a bug introduced at random or something I inadvertently changed in the project.  I closed and reopened the project and the same behavior persisted.  I then closed Unity, Unity Hub, Oculus and I turned off my Oculus Quest 2 headset.  I then turned my Oculus Quest 2 back on and I reopened Unity Hub, Unity (and my project), connected via Airlink and play tested again and the problem went away and everything was normal again.  I think taking my headset off and letting it go to sleep while making changes in Unity caused the issue.  Maybe something to do with my standing play space in the headset.  I've seen this once before and it also reverted itself.  I'll watch out for this in the future.

I also updated the version number and the commit date on the Welcome Menu screen.

Up next to fix:

The four clock pieces listed above.

1.) That socket isn't working correctly and the clock falls down when starting the game.  This needs to be troubleshot and fixed.

2.) The clock does not respond to distance grabbing and the raycast, currently and this needs to also be fixed.

3.) The shadow for the clock is currently baked and I need to set this back to dynamic so that that shadow is no longer baked now that the clock is an interactable.  This also needs to be fixed.

4.) When picking up the clock for the first time rotating the clock is difficult.  I'm not sure why this is but when I drop the clock and re-pick up everything is fine again.  I also notice the first time I pick this up (albeit it is half-way clipped through the wall after falling) the attach is not being used.  Maybe once the other pieces have been fixed this will resolve itself.  If not I need to investigate, troubleshoot and fix this too.

Some of the art being able to be grabbed via distance grabbing while others can not.  While I the idea of distance grabbing the art for the ease of use, I'm not sure how much destruction that may cause if distance grabbing from half way around the room and having it collide with everything in-between the player and the art.  So it may be better to just turn this off for all art instead of turning it on.  I can play test both to see which is better.

Determine if there is a good solution for the character controller colliding with the cabinet doors when leaning forward.

Determine why my physics hands can clip through the dinning room table and chairs when at a fast enough speed.  Try and make this work more like the couch or outside colliders.  Test with other furniture to see if anything else in the room allows this to happen.  Compare and contrast to troubleshoot.

Thin items like photos from the polaroid camera and my punch list sheets are still sometimes getting stuck under the floor and I need to troubleshoot that more to try and fix.

Updating the Interactive board and/or punch lists.  I'm running out of room on my punch lists and I have no more room to add additional punch lists, so I'll have to decide how I wish to use these moving forward.  I still love the idea of having bugs and/or future features viewable in VR and I have a lot of future ideas (both from ideas I've come up with and that my students have come up with that could be added).

If I get that working I feel like I have a lot of the bug pieces in my room fixed.  I'll have to go back to my bug list to check to be sure, but off the top of my head there aren't any others that are coming to mind that I need to fix.  At this point I may choose a new feature to add to this room, just to continue my (and my student's) learning.
@mattdway
mattdway committed on Dec 30

---
## [ikalnytskyi/vm.kalnytskyi.com](https://github.com/ikalnytskyi/vm.kalnytskyi.com)@[e88c0940a0...](https://github.com/ikalnytskyi/vm.kalnytskyi.com/commit/e88c0940a0f9b057314e4f0e9b20589aa9a96b56)
#### Friday 2022-12-30 10:34:46 by Ihor Kalnytskyi

Run Vaultwarden natively

Containers are pain in the ass if all you're looking for is to self host
a bunch of tiny services. The reality, however, bites since there lots
of software without proper packages for Linux distributions.

This patch moves Vaultwarden from running in Podman to be run natively
via old plain systemd unit. For that to happen we first need to unpack
Vaultwarden from the docker image to disk, and then run it in isolated
environment.

Part of the reason why I want this is to play a bit with systemd
sandboxing functionality to understand better its pros and cons.

---
## [oureveryday/Grasscutter](https://github.com/oureveryday/Grasscutter)@[88bc5c4c54...](https://github.com/oureveryday/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Friday 2022-12-30 10:36:29 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[08e6480f8a...](https://github.com/LumberKing/Tianxia/commit/08e6480f8a96caf9790c9f883a172a396a70a046)
#### Friday 2022-12-30 11:03:27 by Silversweeper

Balance/optimization/polishing (part 24 of ???) + Kiyohara improvements

General:
- Bugfixes.
- Took care of some assorted TODOs.

Artefacts:
- Added a new artefact.

Bloodlines:
- Added (intentionally very weak) bloodlines to track the agnates of the four Fujiwara branches (Nanke, Hokke, Shikike, and Kyoke).

CBs:
- Fixed unexpected bracket.
- Fixed Shi Jingtang's usurpation of some important counties.
- Changed Go Yeongchang's war against Liao to be an attempt to take over Liao rather than an independence war; it makes more sense that way.
- Merged Liao/(Jurchen) Jin historical CBs into the SoH CB files.
- Restored the Song-(Jurchen) Jin Sixteen Prefectures negotiation event triggering.

Laws:
- Fixed broken interest group laws.
- Hopefully fixed the interest groups laws sometimes ending up with more than one law active in the same category.
- Fixed broken regency power laws.

Objectives:
- The AI will no longer back the Takeover faction against a CI/ConBu/EI liege if it's eligible for one of those governments and has a claim, seeing at should want to be the new ruler.
- Considering a certain job requirement, becoming a Council Eunuch no longer counts for the "Become Councillor" ambition (players can't be Council Eunuchs anyway; landed characters are ineligible).
- Fixed issues with ambition selection for women under equal laws or doctrines.

Scripted triggers and effects:
- The Mandate calculation is now a bit more forgiving if there is no Chinese Imperial China.
- The Sixteen Prefectures are now properly ceded to Liao, rather than turning into tributaries of Liao.
- New Crusade-related changes to block some potential exploits.

Decisions:
- Dragon hunts can now be attempted further away from Fredak's lair.
- Added a new artefact decision.
- Improved on Chinese culture conversion conditions; they were a bit overly harsh.
- It is now possible to refound the Luojuzi.

Events:
- Updated IDs for Fredak's recovery.
- Ambushes targeting rival dragonslayer parties now compares intrigue a bit better.
- The AI will no longer attempt to duel rival dragonslayers that are much better at PCS.
- The AI will now potentially avoid engaging a rival dragonslayer based on traits.
- Adjusted likelihood of various dragonslaying quest travel events.
- Mandate revolts will now only happen if there is a Chinese Imperial China.
- Potential dragonslayer tumblees should now be of an appropriate gender and orientation.
- Would-be dragonslayers should now consider gender more sensibly when potentially inviting a tumblee along on the journey.
- Joining bandit attacks might now be more profitable, though it's not exactly a Kind act, is it...?
- Disagreements with fellow would-be dragonslayers now check for traits when determining the resolution if you're not diplomatic enough to instantly pass the check.
- Added weights to the fey bargain that potentially will be offered to a would-be dragonslayer.
- Improved the logic at a certain tower.
- Improved the logic in the strange ruins.
- Patient characters no longer are more likely to fail to spot patterns, but Wroth characters are.
- A number of PCS checks during the dragonslayer questline are now harder to pass. If you don't have high PCS, why are you even on the quest?
- Added some new events to the dragonslayer questline, including some ways to pick up lifestyles that potentially might help.
- Attempting to murder or assassinate a would-be dragonslayer now impacts your traits.
- If you and your party decide to join a bandit attack your party dies if you die.
- Your party members now get injured and/or maimed if you get injured and/or maimed in a situation where they should get injured and/or maimed.
- Fixed a bug where a dragonslaying-related breakup was rather more fatal than intended.
- A certain curse and a certain boon now work as intended if you should abandon your quest to slay Fredak, the Emperor of Embers.
- Attempted to fix a new crusade exploit for Chinese-/Japanese-style lieges.
- Strategists, Hunters, Duelists, and obviously Gamers now have a bit of an advantage when fighting dragons (not to be confused with having Advantage).
- It is no longer possible to get non-joke artefacts if you loot Fredak's lair ahead of the fight.
- The Eastern Zodiac no longer matters when fighting Fredak at the lair.
- Made it a bit easier to wound Fredak at the lair, but also made it a bit harder to kill him in general (though wounds help; maybe let someone else do the heavy lifting first?).
- Martial now matters when fighting dragons.
- Dragonslayer artefacts are now a bit better at their job.
- Fredak now potentially takes wounds when fighting even if the outcome isn't "Gets wounded".
- There's now possibly a... bird... in Fredak's hoard.
- High Intrigue characters sneaking into Fredak's lair are no longer penalized for their high Intrigue.
- Certain events at Fredak's lair now affects traits.
- Changed Chinese culture split conditions; they were a bit too harsh.
- Powerful Council Eunuchs can now "helpfully" offer to replace a commander... at the small, small cost of being impossible to fire for several years.
- Restored the child cap override for CI/JI/DI rulers, with some minor adjustments.

History:
- Duan Siping should now have more of an opportunity to take over Da Yining.
- Xu Zhigao should now start leading the Takeover faction.
- Various Sessho/Kampaku/Shikken should now start their Regency Loyalist factions on game start.
- Adjusted Liao-Goryeo border back to where it should be.
- Liao now uses Primogeniture.
- Improved the Kiyohara clan.
- Japanese title adjustments due to the above.
- Added Fujiwara bloodlines.

Localization:
- Assorted improvements.
- Fixed some more instances of the game being "literally uplayable".

---
## [BlissRoms/platform_frameworks_base](https://github.com/BlissRoms/platform_frameworks_base)@[52763102e7...](https://github.com/BlissRoms/platform_frameworks_base/commit/52763102e741ca0ae6dcaf96d0ce92b013f6d790)
#### Friday 2022-12-30 13:03:44 by Kuba Wojciechowski

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
## [Unknownity/cmss13](https://github.com/Unknownity/cmss13)@[229a2e6ed2...](https://github.com/Unknownity/cmss13/commit/229a2e6ed24998b2b97421ae421cfe25b77ae1b1)
#### Friday 2022-12-30 13:39:44 by Stan_Albatross

Teleporter tgui and minor refactor (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

converts teleporters to tgui and removes some shitcode

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui


![image](https://user-images.githubusercontent.com/66756236/208460209-8f260838-1da1-49af-8d6c-44efcc974efb.png)


![image](https://user-images.githubusercontent.com/66756236/208458960-7bd162fd-e2fe-4c23-a3f6-257cb73516f5.png)


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
ui: swapped teleporters to use tgui.
fix: teleporter consoles now have actual sprites!
code: "improved" some teleporter code.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [Unknownity/cmss13](https://github.com/Unknownity/cmss13)@[0dd70b12e5...](https://github.com/Unknownity/cmss13/commit/0dd70b12e5142b3b0f14bf237765c1e643fe8a3f)
#### Friday 2022-12-30 13:39:44 by Stan_Albatross

removes unused nanoui templates (#2012)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

none of these templates are used anywhere

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
del: Removed ten unused nanoui templates. Don't worry, they'll all be
going away soon.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [lavaeater/lava-music](https://github.com/lavaeater/lava-music)@[808adda45a...](https://github.com/lavaeater/lava-music/commit/808adda45a3c5f67529f9acc6ca9a80e4650b6b5)
#### Friday 2022-12-30 14:04:09 by Tommie Nygren

I fucking hate scene2d ui. It is complete and utter shit.

---
## [jughu/tgstation](https://github.com/jughu/tgstation)@[63561ca455...](https://github.com/jughu/tgstation/commit/63561ca455933a38f3390f7fcfa6266fda3c53b3)
#### Friday 2022-12-30 14:18:40 by san7890

Guards against uplink failsafe code being the same as unlock code (#72113)

## About The Pull Request

There's probably a better way to do this to be honest, but I think it's
silly for both to potentially be the same and this should work alright.
## Why It's Good For The Game

Fixes #71446.

I don't think the Syndicate is that stupid.
## Changelog
:cl:
fix: After a recent mishap with a high-ranking Syndicate operative, the
uplink's unlock code and failsafe code (the one that makes it blow up if
you say it) should never turn out to be the same.
/:cl:

---
## [HELLINFIX/kernel_realme_mt6781](https://github.com/HELLINFIX/kernel_realme_mt6781)@[0ffdb92029...](https://github.com/HELLINFIX/kernel_realme_mt6781/commit/0ffdb9202910eb834ef2934327ffaa6d814731df)
#### Friday 2022-12-30 16:03:59 by Peter Zijlstra

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

---
## [GloriousFerguson/DeltaEight](https://github.com/GloriousFerguson/DeltaEight)@[a742c64df9...](https://github.com/GloriousFerguson/DeltaEight/commit/a742c64df98ec4f23eaa64162a2518a91c642ead)
#### Friday 2022-12-30 16:38:44 by carlarctg

Fix entering a ghosted xeno not removing ghostize sleep. (#2076)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Fix entering a ghosted xeno not removing ghostize sleep.

# Explain why it's good for the game

This sucks ass! Let me wake up!!!!! can KILL you if you enter a xeno in
a difficult situation!!!!!!

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
fix: Fix entering a ghosted xeno not removing ghostize sleep.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [saint-lascivious/saint-lascivious.github.io](https://github.com/saint-lascivious/saint-lascivious.github.io)@[69b88afa46...](https://github.com/saint-lascivious/saint-lascivious.github.io/commit/69b88afa46313543a949614a8c5bea8f1f23c6fe)
#### Friday 2022-12-30 16:53:10 by Hayden Pearce

saint-lascivious.github.io: some downright hacky bullshit

   lets see what lighthouse thinks of these shenanigans

 - an asynchronous css test (ab)using the print media type
   i found this used extensiely in the wild
   it appears to be industry standard, which is kinda hilarious

Changes to be committed:
 - modified:   index.html

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[519c6311b5...](https://github.com/Danielkaas94/DTAP/commit/519c6311b553039316a55543fe4e6d9390b5622f)
#### Friday 2022-12-30 17:42:12 by Danielkaas94

✨ Fluorescent Adolescent ✨
Oh, the boy's a slag, the best you ever had
The best you ever had is just a memory
And those dreams weren't as daft as they seem
Aren't as daft as they seem, my love
When you dream them up

---
## [etienne-lelouet/dwm-custom](https://github.com/etienne-lelouet/dwm-custom)@[67d76bdc68...](https://github.com/etienne-lelouet/dwm-custom/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2022-12-30 18:09:43 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [Barbacoa08/fighter-advice](https://github.com/Barbacoa08/fighter-advice)@[fb155033fd...](https://github.com/Barbacoa08/fighter-advice/commit/fb155033fd3b1162b079725b4fee90e88b7ecc8b)
#### Friday 2022-12-30 18:28:34 by barbajoe

centralize a util method and update testing+config to use TS (#33)

* remove dead code

* add `genId` util method

* add test for new util method

* update vite config to be TS and handle globals for test files

* ugh, just make it work

annoyed that I'm having so much trouble with getting test files to globally inherit `vitest`

* AH-HA! just had to FTGM :facepalm:

https://vitest.dev/config/#globals

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[401ccf01c8...](https://github.com/Danielkaas94/DTAP/commit/401ccf01c8663e9b485ff1a02eeaaafd27626dc2)
#### Friday 2022-12-30 18:41:09 by Danielkaas94

💙🔵🔷🔵💙 Blue Blood Blues 💙🔵🔷🔵💙
Yeah, I love you so much.
I don't need to resist.
I don't need to exist.
Dripping blue blood from the wrist.
I don't need to resist.
And all the neighbors get pissed when I come home.
I make em nervous. Yeah, I make em nervous.

Crack a window, crack a broken bone.
Crack your knuckles when you're at home.
Lick an ice cream cone. Crack a bone.

All you had to do was ask.
Who is it that wears the mask?
When you give me the task.
Leave me broke and shirtless.
Check your lips at the door woman.
Shake your hips like battleships.

Yeah, all the white girls trip when I sing at Sunday service.

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[3f9bcab972...](https://github.com/GeoB99/reactos/commit/3f9bcab972e5177fb4252800f324b075c4a660bc)
#### Friday 2022-12-30 19:02:28 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

Another important note is that the added code grew up the binary size of x64 FreeLdr and that makes a PE image check fail because the bootloader is too large. Currently such code is disabled for AMD64, until
a real fix comes into place.

---
## [RealJohnGalt/GaltsGulch-sm8150](https://github.com/RealJohnGalt/GaltsGulch-sm8150)@[7112098b69...](https://github.com/RealJohnGalt/GaltsGulch-sm8150/commit/7112098b69d5922b7d34c1f6088dad4b0507214e)
#### Friday 2022-12-30 20:02:09 by Jason A. Donenfeld

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
## [simonw/disaster-data](https://github.com/simonw/disaster-data)@[e2f10b2c5d...](https://github.com/simonw/disaster-data/commit/e2f10b2c5d6b4809e1a05dbd2c9343ced13450e2)
#### Friday 2022-12-30 20:08:51 by disaster-scrapers

fema/shelters: 7 shelters removed, 3 shelters changed

7 shelters removed:
  Mt. Enon Baptist Church in Dayton, OH (OPEN)
    https://www.google.com/maps/search/39.7551139,-84.2208322
    population = 0

  St. Bernadette Catholic Parish in Lakewood, CO (OPEN)
    https://www.google.com/maps/search/None,None
    population = 0

  Arapahoe County Fairgrounds in Aurora, CO (OPEN)
    https://www.google.com/maps/search/None,None
    population = 2

  Ann & Chuck Dever Center in Englewood, FL (OPEN)
    https://www.google.com/maps/search/26.924404,-82.314119
    population = 37

  Del Tura Shelter in North Fort Myers, FL (OPEN)
    https://www.google.com/maps/search/26.738655,-81.912434
    population = 151

  God's Grace Community Church in Houston, TX (OPEN)
    https://www.google.com/maps/search/None,None
    population = 0

  Moore County Parks and Recreation in Carthage, NC (OPEN)
    https://www.google.com/maps/search/35.303695,-79.416233
    population = 16

---
## [aakropotkin/floco](https://github.com/aakropotkin/floco)@[c2db48c70b...](https://github.com/aakropotkin/floco/commit/c2db48c70ba68d3d11f4f94f602c73869fe8165f)
#### Friday 2022-12-30 20:29:21 by Alex Ameen

honestly starting to hate this module system bullshit

---
## [hexdump0815/rack-dockerbuild-v2](https://github.com/hexdump0815/rack-dockerbuild-v2)@[e09dc0d135...](https://github.com/hexdump0815/rack-dockerbuild-v2/commit/e09dc0d1354ad04d8eb9054a85a4cae4ca50c305)
#### Friday 2022-12-30 20:44:22 by hexdump

ok - lets do the libcsound64 stuff different for dbRackCsound

looks like we have to build our own libcsound64 library anyway as the
default debian one seems to not be compiled with the required
INIT_STATIC_MODULES compile flag ... and while we are at it we can then
also build a static library (which is not part of the debian libcsound64
package) and this way avoid all the shared lib hacks

all this is quite ugly and can be done much nicer, but my main goal is
to get it somehow working with only minimal effort right now :)

---
## [etra0/litcher](https://github.com/etra0/litcher)@[b76e5f4f86...](https://github.com/etra0/litcher/commit/b76e5f4f86e78e92a0092e874d9350cf52d9daf9)
#### Friday 2022-12-30 20:50:28 by Sebastián Aedo

Changed InputFloat for Drag for Position

As requested for our lord and savior, Jim2Point0, The Legendary
Fortographer, it would be more convenient for more the position to be
draggables.

Despite the current despair of our society, screenshots should be a top
priority of every peasant in this world, and so this commit had to be
made.

This is god's law.

(cherry picked from commit 95e678da5cd326b6bb3fcc4f0645f2b4c9b82d6a)

---
## [Pseudo-Corp/SynergismOfficial](https://github.com/Pseudo-Corp/SynergismOfficial)@[a0515406da...](https://github.com/Pseudo-Corp/SynergismOfficial/commit/a0515406da6037eee69582bdfd63b66fafde290a)
#### Friday 2022-12-30 21:55:08 by Mixelz

Perk List Overhaul

Contained within this commit is an encompassing overhaul onto several different parts of the Perk List, including the merging of several perks, adding additional levels to denote previously hidden effects and implementing updating effect % counters to applicable perks.
To clarify, no changes to the functionality of the perks were made, only to the presentation of said perks.
The full list of changes are as follows, in the order they appear in the code:

Merging in Midas' Windfall and Industrial Daily Codes into 2 levels of XYZ.
Minor formatting change for Unlimited Growth.
Improved readability of Not so challenging description and uppercased its name.
Merged A Particular Improvement into Automation Upgrades, also added an extra level to denote the previously hidden effect of keeping w2x10.
Revamped the descriptions for Automation Upgrades to improve readability and internal consistency with labeled effects.
Combined Blessed by the Spirits, Advanced Runes Autobuyer, and Autobuy Talisman Resources into a new perk: Automagical Runes.
Combined Better Cube Opening and Automation Cubes into a new perk: Cool QoL Cubes.
Combined Real Time Auto Ascend and Auto Ascension Challenge Sweep into a new perk: Eternal Ascensions.
Updated descriptions for "Ant God's Cornucopia" for readability/spelling.
Swapped the descriptions of Golden Revolution 1 and 2 (Keeping it in line with the effect ordering of GQ 1/2/3 themselves.)
Golden Revolution 1/2/3, PL-AT Σ, and skrauQ now all update to display their current % effect.
Combined Metacogenesis and Metatrigenesis into a new perk: Octeract Metagenesis.
Immaculate Alchemy now updates its description per level instead of having 1 description for all 3 levels.

---
## [packrat386/boreas](https://github.com/packrat386/boreas)@[0ed436c031...](https://github.com/packrat386/boreas/commit/0ed436c0313fb12197b7f38db16051d0f48beab7)
#### Friday 2022-12-30 22:42:14 by Aidan Coyle

Add CSS so it looks somewhat presentable

Incidentally drop the images. They are a pain in the ass to display
and they don't look good anyway (sorry NWS)

---
## [TastyPie2/FizzBuzzEnterpriseEdition_CSharp](https://github.com/TastyPie2/FizzBuzzEnterpriseEdition_CSharp)@[cf2d2de8a8...](https://github.com/TastyPie2/FizzBuzzEnterpriseEdition_CSharp/commit/cf2d2de8a8b5a45e8d741e7439173aa2570b91f8)
#### Friday 2022-12-30 23:51:58 by Mathias Hansen

We lost Joe.

It is with great concern that I must inform you that Joe, a valued member of our development team, has experienced a mental health crisis while working on a critical project. As a result, he has been admitted to the nearest psychiatric ward for treatment and will be unable to return to work for an indefinite period of time.

This situation is deeply unfortunate and we extend our sincerest condolences to Joe and his family. We prioritize the well-being of our employees above all else, and are committed to providing the necessary support and resources to ensure that our team members are able to maintain their mental health and well-being.

In the meantime, we have implemented contingency measures to ensure that the project remains on track and that our clients continue to receive the high level of service that they have come to expect from us. We are confident that these measures will allow us to continue to meet our commitments and deliver results for our clients.

We appreciate your understanding and patience during this difficult time. Please do not hesitate to reach out to me with any questions or concerns.

---

