## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-06](docs/good-messages/2023/2023-05-06.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,881,601 were push events containing 2,784,193 commit messages that amount to 167,862,852 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 61 messages:


## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ff8dc9ba33...](https://github.com/treckstar/yolo-octo-hipster/commit/ff8dc9ba33664b8c1f0a1231e2b427d15cea1a23)
#### Saturday 2023-05-06 00:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [moltoretardo/cmss13](https://github.com/moltoretardo/cmss13)@[9bbac13b28...](https://github.com/moltoretardo/cmss13/commit/9bbac13b2898570be5e448ce50ca110472561630)
#### Saturday 2023-05-06 00:40:26 by TotalEpicness

Globber balance overhaul (#3039)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Globber came out overtuned as shit and actually replicated some of the
issues that we didn't want like the dreaded ChokePoint Boiler Torture
Rebalances some issues that weren't forseen during the development nor
TM stage of globber. This should be TM'd


General changes:
- Globber C/D 25 seconds > 30 seconds ( the temp nerf PR didnt actually
fix this correctly)
- Fire deals 2x damage instead of 1.5x damage ( this needs significant
testing and will likely be toned down)
- Acid spray doesn't stun at full distances anymore

Depending on TM feedback, I might switch between these two variants of
this overhaul:

Rework variance 1: Keep zoom and current design while maintaining a
little toughness [currently on]
- Armor 25 > 20
-  Zoom halved 4 > 2
-  Dropped health a tier: 650 > 600
- Fire deals 2x damage instead of 1.25x damage
- Globber C/D

Rework variance 2: Embrace the zoom removal
- Directional armor 10 base armor + 20 at the front. Flank a globber to
kill it!
- Slight windup increase 5s > 6s
- Fire damage 1.25x > 1.5x

Fixes:

<!-- Remove this text and explain what the purpose of your PR is.

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

:cl: Totalepicness

balance: Rebalances globber, which has come out overtuned. Globber now
has reduced health, armor and zoom along with higher fire damage
multiplier.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: morrowwolf <darthbane97@gmail.com>

---
## [CliffracerX/Skyrat-tg-PRs](https://github.com/CliffracerX/Skyrat-tg-PRs)@[c5a7f5a7c9...](https://github.com/CliffracerX/Skyrat-tg-PRs/commit/c5a7f5a7c93f96cc047297ed8ee61cce02626c75)
#### Saturday 2023-05-06 00:58:41 by SkyratBot

[MIRROR] Mimes can no longer write without breaking their vow. [MDB IGNORE] (#20841)

* Mimes can no longer write without breaking their vow. (#74674)

## About The Pull Request

I feel this is gonna be unpopular with the lazy mime players.

Also, this is an idea I had in my backlog for a while now

![image](https://user-images.githubusercontent.com/53777086/231355622-2c5d5d5a-813d-420c-ae42-c1bdc657f3ba.png)

This removes the Mime's ability to write on paper while they're on their
vow of silence.
This can be compared to hand language, which doesn't let you speak
despite not being considered "talking", and PDA messaging, which does
the same.

Mimes can still write with their pen, which is a nice invisible white
color. I thought I would keep it in as I find that interaction funny to
have a Mime give someone just a blank paper, unknowing that there's text
on it.
Spraycans/Telekinesis/Circuits are also left unaffected because they
require actual effort to obtain (doing genetics, doing circuits, or
printing spraycans which take a lot of inventory space and is limited),
compared to paper which you can carry hundreds of papers around and is
bountiful across the station.

I thought this was attempted at least once, but I can't find any PR that
mentions it, so I'm shooting my shot to see if this is something we'd
want.

## Why It's Good For The Game

Mimes using paper is a lazy way to bypass their one job gimmick: Emoting
over talking.

If they get a job change, they can simply break their vow to access
paper writing abilities, so this doesn't affect that really. It more-so
hits the Mimes who uses the job for the free spells/healing
abilities/etc, and bypasses the downsides (im aware its harder to get
people to read paper than it is to talk to them, but you can literally
get the mute quirk and itll have the same effect without being the whole
job).

The point is, you don't get invisible walls for free; it comes at a cost
of not being able to talk to people. If you want to talk, then break
your vow, lose access to your Mime abilities, and remake it later when
the cooldown is over. You're not meant to do both.

## Changelog

:cl:
balance: Mimes can no longer write on paper without breaking their vow.
/:cl:

* Mimes can no longer write without breaking their vow.

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [rynosaur94/homebrew](https://github.com/rynosaur94/homebrew)@[f1150e6e1d...](https://github.com/rynosaur94/homebrew/commit/f1150e6e1d24b74ab600b549776c7f664f16fe96)
#### Saturday 2023-05-06 01:00:52 by rynosaur94

Setting Guide for G4 My Little Pony's Equestria

A full setting guide for the universe of My Little Pony Friendship is Magic.  Trying to blend show accuracy and tone with 5e's general heroic fantasy vibes, I've been maintaining this guide since I created it in 2016.  Contains Races, Feats, Subclasses, Spells, Items mundane and magical, Religions, and more.

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[0410075cc8...](https://github.com/Bjarl/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Saturday 2023-05-06 01:18:40 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1674f25725...](https://github.com/tgstation/tgstation/commit/1674f25725c25e15769b031553b42144f526f841)
#### Saturday 2023-05-06 01:31:30 by John Willard

New Medical job: The Coroner (#75065)

## About The Pull Request

HackMD: https://hackmd.io/RE9uRwSYSjCch17-OQ4pjQ?view

Feedback link: https://tgstation13.org/phpBB/viewtopic.php?f=10&t=33972

Adds a Coroner job to the game, they work in the Medical department and
have their office in the Morgue.
I was inspired to make this after I had played my first round on
Paradise and messed around in there. The analyzer is copied from there
(https://github.com/ParadiseSS13/Paradise/pull/20957), and their
jumpsuit is also mostly stolen from it (i just copied the color scheme
onto our own suits).

Coroners can perform autopsies on people to see their stats, like this

![image](https://user-images.githubusercontent.com/53777086/235369225-805d482c-56c0-441c-9ef8-a42d0a0192bc.png)

They have access to Medbay, and on lowpop will get Pharmacy (to make
their own formaldehyde). They also have their own Secure Morgue access
for their office (doubles as a surgery room because they are edgelords
or whatever) and the secure morgue trays.

Secure Morgue trays spawn with their beepers off and is only accessible
by them, the CMO, and HoS. It's used to morgue Antagonists. Security's
own morgue trays have been removed.

The job in action


https://cdn.discordapp.com/attachments/950489581151735849/1102297675669442570/2023-04-30_14-16-06.mp4

### Surgery changes

Autopsies are a Surgery, and I tried to intertwine this with the
Dissection surgery.
Dissections and Autopsies both require the Autopsy scanner to perform
them, however you can only perform one on any given body. Dissections
are for experiments, Autopsies is for the paper of information.

Dissected bodies now also give a ~20% surgery speed boost, this was
added at the request of Fikou as a way to encourage Doctors to let the
Coroner do their job before reviving a body.
I also remember the Medical skill, which allowed Doctors to do surgery
faster on people, and I hope that this can do something like that
WITHOUT adding the potential for exploiting, which led to the skill's
downfall.

### Morgue Improvements

Morgue trays are no longer named with pens, they instead will steal the
name of the last bodybag to be put in them.

Morgue trays are also removed from Brig Medical areas and Robotics, now
they have to bring their corpses to the Morgue where the Coroner can
keep track and ensure records are properly updated.

### Sprite credits

I can't fit it all in the Changelog, so this is who made what

McRamon
- Autopsy scanner

Tattax 
- Table clock sprites and in-hands

CoiledLamb
- Coroner jumpsuits & labcoats (inhand, on sprite, and their respective
alternatives)
- Coroner gloves
- CoronerDrobe (the vending machine)

## Why It's Good For The Game

This is mostly explained in the hackmd, but the goal of this is:

1. Increase the use of the Medical Records console.
2. Add a new and interesting way for Detectives to uncover mysteries.
3. Add a more RP-flavored role in Medical that still has mechanics tied
behind it.

## Changelog

:cl: JohnFulpWillard, sprites by McRamon, tattax, and Lamb
add: The Coroner, a new Medical role revolving around dead corpses and
autopsies.
add: The Coroner's Autopsy Scanner, used for discovering the cause for
someone's death, listing their wounds, the causes of them, their
reagents, and diseases (including stealth ones!)
qol: Morgue Trays are now named after the bodybags inside of them.
balance: The morgue now has 'Secure' morgue trays which by default don't
beep.
balance: Security Medical area and Robotics no longer have their own
morgue trays.
balance: Dissected bodies now have faster surgery speed. Autopsies also
count as dissections, however they're mutually exclusive.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[c5dce84be8...](https://github.com/Cheshify/tgstation/commit/c5dce84be826ea945a11c492dce7eb2c2789548a)
#### Saturday 2023-05-06 01:38:26 by Rhials

Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat. 
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[199aa000d3...](https://github.com/Cheshify/tgstation/commit/199aa000d3f46ee4386a65079992e4b9d0f2537d)
#### Saturday 2023-05-06 01:38:26 by Rhials

Demotes Psyker Pirates to Bounty Hunter Duty (#75031)

This PR demotes the Psyker-gang from a pirate team to a fugitive hunting
team. For more information on Psyker pirates, please refer to #71650.

Stuff this also does in the process:
- Gives fugitive hunters their own subfolder in the fugitives antagonist
folder, moves some of their stuff into hunter-specific files rather than
interlacing it with the rest of the fugitive code.
- Moves the hunter backstories to defines, to make reading things easier
while I made this change.
- Exhaustively moves everything related to psykers from being
pirate-oriented to hunter-oriented (typepaths, locations where stuff is
defined, etc. There should be nothing left behind related to psykers in
anything pirate related). (Tell me if I missed anything somehow).

They still get their ship (they even get their own custom
psyker-friendly prisoner capsule). They still have a bunch of lethally
chambered firearms. They're the same gunrunning nutcases they were
before, just as bounty hunters.

To assist with basic tasks such as "getting to the station" or "figuring
out who the fuck we're supposed to be kidnapping", the psykers have
"acquired" a Seer to assist them. They can _try_ to coordinate the
psykers and lead them through situations where their impairments put
them at too great a disadvantage. If you're one of the psykers, make
sure to keep this guy alive at all costs!

Why are they called Shikaris instead of hunters? Mariam-Webster says
it's a Hindi word for some kind of hunter/tracker, and it sounded like
something a bunch of space-junkies would call themselves because they
think it sounds cool.

They now also come with a slightly different motivation, now that they
can't directly threaten the crew for money. Psyker hunters now arrive
tasked with a dirty kidnapping job, payment rendered in GORE.
## Why It's Good For The Game

Psykers aren't up to the challenge of being pirates. They're bogged down
by a number of fundamental issues that render them unable to do anything
expected of pirates. As it currently stands, they present about as much
threat as you would expect from three blind junkies with guns.

Removing them wholesale would be kind of lame. They can function as a
bunch of chaotic-neutral gun-toting space-maniacs, but for the purposes
of gameplay, keeping them as pirates would be a waste of their talents.

Moving them to a lower-stakes role not only moves them to a niche they
are more capable of filling, but gives players a more lax environment to
get a grip on playing psyker without being overwhelmed.

Giving them a seeing-eye role should bring a more unique dynamic to how
psykers are played (that is, some semblance of organization rather than
blind flailing), and should help get over the mechanical hurdles of
being a psyker until better solutions can be made. It shouldn't be too
big of an impact on balance considering the psyker gang only has three
spawns, while most hunter packs have 4+.

---
## [AverageUser67/tgstation](https://github.com/AverageUser67/tgstation)@[912e843f53...](https://github.com/AverageUser67/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Saturday 2023-05-06 01:44:37 by san7890

Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:


![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.


![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

---
## [Reposits/reposits.github.io](https://github.com/Reposits/reposits.github.io)@[d29640e340...](https://github.com/Reposits/reposits.github.io/commit/d29640e3402f9f86cb48ff87f836b04ea1092ffa)
#### Saturday 2023-05-06 04:25:44 by Reposits

Seriously this SHIT is starting to get on my fucking nerves... I want to go to bed.

---
## [WagicProject/wagic](https://github.com/WagicProject/wagic)@[273d666bcc...](https://github.com/WagicProject/wagic/commit/273d666bcce8d7cf360a869e2f288c5843fbb55d)
#### Saturday 2023-05-06 04:29:20 by Eduardo MG

New cards from MOC, MOM

March of the Machine Commander (MOC)
March of the Machine (MOM)
A few others from BRO and ONE
Some old auras that get sacrificed at end of turn if you cast them as if they had flash
fixed Fire Prophecy
NEW:
Umori, the Collector
Rootwire Amalgam
Steel Seraph
Tyrranax Rex
Paladin of Predation
Axgard Artisan
Zephyr Winder
Phyrexian Pegasus
Orthion, Hero of Lavabrink
Surrak and Goreclaw
Angelic Intervention
Pile On
Terror of Towashi
Interdisciplinary Mascot
Fertilid's Favor
Vengeant Earth
Sidar Jabari of Zhalfir
Moira and Teshar
Shalai and Hallar
Vodalian Wave-Knight
Bitterthorn, Nissa's Animus
Herald of Hoofbeats
Chivalric Alliance
Darksteel Splicer
Mistmeadow Vanisher
Death-Greeter's Champion
Hedron Detonator
Pain Distributor
Locthwain Lancer
Schema Thief
Exsanguinator Cavalry
Nesting Dovehawk
Filigree Vector
Conjurer's Mantle
Infernal Sovereign
Firemane Commando
Goro-Goro and Satoru
Katilda and Lier
Slimefoot and Squee
Soar
Armor of Thorns
Grave Servitude
Lightning Reflexes
Spider Climb
Parapet
Mystic Veil
Relic Ward
Titania, Voice of Gaea
Titania, Gaea Incarnate
Professional Face-Breaker
Oracle's Vault
Volcanic Spite

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[f7a49c4068...](https://github.com/lessthnthree/tgstation/commit/f7a49c4068f1277e6857baf0892d355f1c055974)
#### Saturday 2023-05-06 05:36:36 by Ryll Ryll

Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes (#74036)

## About The Pull Request
This PR messes around with gunpoints a bit, with the purpose of making
them more viable in certain scenarios without making them obnoxious. The
biggest change is that gunpoints now require a 0.5 second do_after()
where neither the shooter nor the target moves, and immobilizes both of
them for 0.75 seconds if point blank, or half that if you're 2 tiles
away. Originally you were supposed to only be able to initiate a
gunpoint from point-blank, but #56601 seems to have removed that
requirement, so we'll run with it and just leave it as advantageous to
gunpoint closer up. The do_after() reinforces that it should be used as
an ambush tactic, and so you can't use it on someone who's actively
fleeing or fighting you.

Getting held up will now make you emit a shocked gasp sound, a la Metal
Gear Solid, which combined with the short immobilize will hopefully make
it more noticeable that someone's pointing a gun at you.

Holdups will now immediately give a 25% bonus to damage and wounds,
instead of having to wait 2.5 seconds to hit the double damage stage.

Finally, right clicking someone that you're holding up will no longer
shoot them. That just feels like good consistency.

## Why It's Good For The Game
Hopefully makes gunpoints a little more viable for when you want to
stick someone who's not expecting it up without them immediately jetting
off. In the future I'd like to ape Baycode and let the gunman have an
action that toggles whether the victim is allowed to move, so you can
order them to move to a second location without instantly shooting them,
but that'll come later.
## Changelog
:cl: Ryll/Shaps
balance: Holding someone at gunpoint now requires both the shooter and
the victim to hold still for half a second before activating, so you
can't hold-up people fleeing or fighting you. After that, it will
briefly immobilize the both of you, 0.75 seconds if adjacent, or half
that if you're two tiles away. Nuke ops are immune to the
immobilization, since they're ready to die anyways.
balance: Holding someone up will immediately apply a 1.25x damage and
wound multiplier, rather than waiting 2.5 seconds to hit 2x.
soundadd: Being held up will now make the victim play a sharp gasp
sound, a la Metal Gear Solid.
qol: Trying to hold someone up that you're already holding up will no
longer shoot them.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [AdamRGrey/misc](https://github.com/AdamRGrey/misc)@[948c5b3b88...](https://github.com/AdamRGrey/misc/commit/948c5b3b884ad9427fa3ef254d8dc6ef826f82b3)
#### Saturday 2023-05-06 06:21:45 by adam

fuck you i'll put an empty commit message if i want to

---
## [tinarskii/tinarskii.com](https://github.com/tinarskii/tinarskii.com)@[3c11d22d4b...](https://github.com/tinarskii/tinarskii.com/commit/3c11d22d4b877dc4afbaa8f5a0b23351818a7e19)
#### Saturday 2023-05-06 07:34:30 by Tinnaphat Somsang

Fortnite battle pass. I just shit, out my ass. Bootin' up my PC, Because I need, need, To get that Fortnite battle pass. I like Fortnite, Did I mention Fortnite? I like Fortnite, It's night time, I mean it's five o'clock That's basically night time. Y'all remember cartoon network? Adventure time

Fortnite battle pass.
I just shit, out my ass.
Bootin' up my PC,
Because I need, need,
To get that Fortnite battle pass.
I like Fortnite,
Did I mention Fortnite?
I like Fortnite,
It's night time,
I mean it's five o'clock
That's basically night time.
Y'all remember cartoon network?
Adventure time

---
## [filiphsps/Metro-Compose](https://github.com/filiphsps/Metro-Compose)@[6ddd4e87d3...](https://github.com/filiphsps/Metro-Compose/commit/6ddd4e87d3244a2a8489ea6b0eb3e9940d146181)
#### Saturday 2023-05-06 07:38:49 by Filiph Sandström

Metro: Refactor `forceTapAnimation` into `TiltIndication`

Fixes https://github.com/louis993546/Metro-Compose/issues/192.

This was a real PITA to reverse engineer and figure out thanks to the
lackluster `Indication` and `Interaction` documentation.

The API is also missing some expected features like proper rotation
so instead we have to use `android.graphics.Camera` for the actual
tilting effect.

Hopefully my pain reverse engineering `rememberRipple`& co and then
subsequent sharing of a real-world reimplementation will prevent
future generations from having to suffer the same way I have.

Y'all have been forewarned, if you choose to tread where I've tread
you'll only experience madness.

---
## [dyrone/git](https://github.com/dyrone/git)@[7891e46585...](https://github.com/dyrone/git/commit/7891e465856e539c4a102dadec6dca9ac51c38df)
#### Saturday 2023-05-06 07:50:51 by Jeff King

gpg-interface: set trust level of missing key to "undefined"

In check_signature(), we initialize the trust_level field to "-1", with
the idea that if gpg does not return a trust level at all (if there is
no signature, or if the signature is made by an unknown key), we'll
use that value. But this has two problems:

  1. Since the field is an enum, it's up to the compiler to decide what
     underlying storage to use, and it only has to fit the values we've
     declared. So we may not be able to store "-1" at all. And indeed,
     on my system (linux with gcc), the resulting enum is an unsigned
     32-bit value, and -1 becomes 4294967295.

     The difference may seem academic (and you even get "-1" if you pass
     it to printf("%d")), but it means that code like this:

       status |= sigc->trust_level < configured_min_trust_level;

     does not necessarily behave as expected. This turns out not to be a
     bug in practice, though, because we keep the "-1" only when gpg did
     not report a signature from a known key, in which case the line
     above:

       status |= sigc->result != 'G';

     would always set status to non-zero anyway. So only a 'G' signature
     with no parsed trust level would cause a problem, which doesn't
     seem likely to trigger (outside of unexpected gpg behavior).

  2. When using the "%GT" format placeholder, we pass the value to
     gpg_trust_level_to_str(), which complains that the value is out of
     range with a BUG(). This behavior was introduced by 803978da49
     (gpg-interface: add function for converting trust level to string,
     2022-07-11). Before that, we just did a switch() on the enum, and
     anything that wasn't matched would end up as the empty string.

     Curiously, solving this by naively doing:

       if (level < 0)
               return "";

     in that function isn't sufficient. Because of (1) above, the
     compiler can (and does in my case) actually remove that conditional
     as dead code!

We can solve both by representing this state as an enum value. We could
do this by adding a new "unknown" value. But this really seems to match
the existing "undefined" level well. GPG describes this as "Not enough
information for calculation".

We have tests in t7510 that trigger this case (verifying a signature
from a key that we don't have, and then checking various %G
placeholders), but they didn't notice the BUG() because we didn't look
at %GT for that case! Let's make sure we check all %G placeholders for
each case in the formatting tests.

The interesting ones here are "show unknown signature with custom
format" and "show lack of signature with custom format", both of which
would BUG() before, and now turn %GT into "undefined". Prior to
803978da49 they would have turned it into the empty string, but I think
saying "undefined" consistently is a reasonable outcome, and probably
makes life easier for anyone parsing the output (and any such parser had
to be ready to see "undefined" already).

The other modified tests produce the same output before and after this
patch, but now we're consistently checking both %G? and %GT in all of
them.

Signed-off-by: Jeff King <peff@peff.net>
Reported-by: Rolf Eike Beer <eb@emlix.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [dyrone/git](https://github.com/dyrone/git)@[07f91e5e79...](https://github.com/dyrone/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Saturday 2023-05-06 07:52:42 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[bc650f8e88...](https://github.com/diphons/D8G_Kernel_oxygen/commit/bc650f8e887f5106a8a3dcb3c1801a882f3ff9fd)
#### Saturday 2023-05-06 10:08:06 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [PyQuantSharp/flow-forecast](https://github.com/PyQuantSharp/flow-forecast)@[728c49257a...](https://github.com/PyQuantSharp/flow-forecast/commit/728c49257a3dde1d427921ac2a9d1f94f50261c4)
#### Saturday 2023-05-06 10:36:44 by isaacmg

annoying gh 1

I hate these asshole roofers that my apartment brought out here they are making life miserable.

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[98c164023f...](https://github.com/newstools/2023-new-york-post/commit/98c164023ffa1d73127604ffec5114ee0bf9354f)
#### Saturday 2023-05-06 10:50:59 by Billy Einkamerer

Created Text For URL [nypost.com/2023/05/05/tennessee-hotel-guest-wakes-up-to-night-manager-sucking-on-his-toes-police/]

---
## [surajdazz/platform_frameworks_base](https://github.com/surajdazz/platform_frameworks_base)@[98ce0bc762...](https://github.com/surajdazz/platform_frameworks_base/commit/98ce0bc76241c2739e553047ce51b06d699aa621)
#### Saturday 2023-05-06 11:36:25 by Kuba Wojciechowski

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
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[c0ef4ba907...](https://github.com/OrionTheFox/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Saturday 2023-05-06 11:39:17 by tralezab

Adds the Dark Matt-eor when you emag a stupid amount of meteor shields + lots of meteor file sorting + qol + dark matter singularity + dark matt-eor summoning final traitor objective (#74330)

## About The Pull Request

<details>
  <summary>Dark Matt-eor Image</summary>
  

![image](https://user-images.githubusercontent.com/40974010/228368755-34ae5f89-e1bb-498b-bbf8-a14ff4240dc0.png)

</details>

> A barely visible blur in the cosmic darkness, like a ghostly shadow on
a moonless night. A piercing howl in the vacuum of space, as if it were
tearing the fabric of reality. A twisted halo of light around it,
bending and breaking the rays of distant suns. A shower of quantum
sparks, flickering and fading in its wake. A dark matter meteor (dark
matt-eor) is a wonder to witness, and to dread.

> A sudden impact, like a hammer blow to the heart of the station. A
violent tremor, shaking and shattering the metal walls and windows. A
deafening roar, as the air rushes out of the breached hull. A blinding
flash, as the dark matter meteor unleashes its hidden energy. A tiny
black hole, forming and growing in the center of the station. A
relentless pull, dragging everything towards the abyss. A dark matter
meteor is incredibly deadly.

Emagging too many meteor shields will summon a dark matt-eor. This comes
with several warnings, and after awhile, warns the station that someone
is trying to summon a dark matteor.

The dark matt-eor itself is not that damaging in its impact, but drops a
singularity in its final resting place.

## Why It's Good For The Game

It's a new way to terrorize a round as an antagonist. Before, emagging a
lot of meteor shields would basically make meteor showers the only event
that can run, which is cool, but since constant meteor waves are going
to destroy the station, let's also throw in the mother of all meteors!

This also adds warnings to spamming emagging meteor shields, which imo
needs it. The round ends when someone spams emagged meteor shields, and
since they're meteor shields nobody is going to reasonably check on
them.

## Changelog
:cl:
add: The dark matt-eor
add: Summon a dark matt-eor final traitor objective
add: Dark matter singularity variant, which can't grow as big as a
regular singularity but hungers for blood
code: cleaned up/sorted meteor shield code, satellite control, and more
qol: added a lot of feedback to interacting with meteor shields
balance: emagging a lot of meteor shields warns the station, but
emagging enough of them summons a Dark Matt-eor.
/:cl:

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[ccef887efe...](https://github.com/OrionTheFox/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Saturday 2023-05-06 11:39:17 by san7890

Lints Against Unmanaged Local Defines (#74333)

# MAINTAINER - USE THE BUTTON THAT SAYS "MERGE MASTER" THEN SET THE PR
TO AUTO-MERGE! IT'S MUCH EASIER FOR ME TO FIX THINGS BEFORE THEY SKEW
RATHER THAN AFTER THE FACT.

## About The Pull Request

Hey there,

This took a while to do, but here's the gist:

Python file now regexes every file in `/code` except for those that have
some valid reason to be tacking on more global defines. Some of those
reasons are simply just that I don't have the time right now (doing what
you see in this PR took a few hours) to refactor and parse what should
belong and what should be thrown out. For the time being though, this PR
will at least _halt_ people making the mistake of not `#undef`ing any
files they `#define` "locally", or within the scope of a file.

Most people forget to do this and this leads to a lot of mess later on
due to how many variables can be unmanaged on the global level. I've
made this mistake, you've made this mistake, it's a common thing. Let's
automatically check for it so it can be fixed no-stress.

Scenarios this PR corrects:

* Forgetting to undef a define but undeffing others.
* Not undeffing any defines in your file.
* Earmarking a define as a "file local" define, but not defining it.
* Having a define be a "file local" define, but having it be used
elsewhere.
* Having a "local" define not even be in the file that it only shows up
in.
* Having a completely unused define*

(* I kept some of these because they seemed important... Others were
junked.)
## Why It's Good For The Game

If you wanna use it across multiple files, no reason to not make it a
global define (maybe there's a few reasons but let's assume that this is
the 95% case).

Let me know if you don't like how I re-arranged some of the defines and
how you'd rather see it be implemented, and I'd be happy to do that.
This was mostly just "eh does it need it or not" sorta stuff.

I used a pretty cool way to detect if we should use the standardized
GitHub "error" output, you can see the results of that here
https://github.com/san7890/bruhstation/actions/runs/4549766579/jobs/8022186846#step:7:792
## Changelog
Nothing that really concerns players.

(I fixed up all this stuff using vscode, no regexes beyond what you see
in the python script. sorry downstreams)

---
## [ShashankDongre/INFO-6105-Data-Science-Engineering-Methods-and-Tools](https://github.com/ShashankDongre/INFO-6105-Data-Science-Engineering-Methods-and-Tools)@[1b6a90e7a8...](https://github.com/ShashankDongre/INFO-6105-Data-Science-Engineering-Methods-and-Tools/commit/1b6a90e7a84a820e898e1bafe30fec22eaf2ba39)
#### Saturday 2023-05-06 11:47:05 by ShashankDongre

Assignment_4.1

You're going to write a movie storybook by acting in it with your teammates and friends. You're going to take pictures of key scenes in the movie, turn them into cartoons to make the pictures look like drawings, then stage and direct the pictures into the production of the storybook of a movie. You will pick one of the contenders for this year's American, Chinese, or Hindi Oscars (or the movie you like) as the base story and then modify it in a creative way.

You'll be in a team of 2, 3, or 4 students. There will be two submissions per team: i) The storybook as a PDF file, an English version, and a version in your language. The whole story book needs to have at least 5 pages (excluding the poster page), and each page needs to have around 20 pictures. ii) The software for the entire storybook. You are not allowed to stitch pictures together with paintbrush programs; it all needs to be in Python.

---
## [ianjoneill/terminal](https://github.com/ianjoneill/terminal)@[21464fe41c...](https://github.com/ianjoneill/terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Saturday 2023-05-06 12:24:38 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [amazon-mt8695-devs/android_kernel_amazon_mt8695](https://github.com/amazon-mt8695-devs/android_kernel_amazon_mt8695)@[832768779e...](https://github.com/amazon-mt8695-devs/android_kernel_amazon_mt8695/commit/832768779eefc2e9dbfb56b60aeb6ad65f2d3efe)
#### Saturday 2023-05-06 12:27:06 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [mc-skyprison/SkyPrisonCore](https://github.com/mc-skyprison/SkyPrisonCore)@[f5bbc95d42...](https://github.com/mc-skyprison/SkyPrisonCore/commit/f5bbc95d42274e75e50c45eeaee4870245f9bc42)
#### Saturday 2023-05-06 13:28:35 by DrakePork

100th note to self about the same thing:
Commit more often

STUFF THAT HAS CHANGED (HOLY FUCK ITS ALOT)
- Removed a bunch of unnecessary code
- Did so you can't break bombs after having placed them down.
- Added Token History and Token Check
- Changed the bomb explosion to look like an explosion
- Implemented NUKE
- Streamlined the nuke explosion to not have any switch cases or anything like that
- Added /purchases <player>
- Fixed econcheck as it was semi broken
- Found out Ive been using the wrong hour measurement for moneyhistory, so all of those logs are in 12 hour time without the am / pm so you dont really know when on the day it took place, but Ive now fixed that.
- Added a /minereset command to better reset the mines
- Added /voucher so that I can add different vouchers like mine-reset and token-shop.
- Did so if the dailyMission is make money it'll add a $ infront
- Added libsDisguises dependency for a future project
- Moved Purpur dependency to the top of the dependencies list as I've come to realize that the dependencies works in a hierarchy.
- Added a /virtualfurnace to test out the possibility of a virtual furnace.
- Started work on custom coding the tokenshop as the current one thats made with the panels plugin is missing some stuff we'd like to add.
- Probably more

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[590bad4061...](https://github.com/Huffie56/cmss13/commit/590bad4061627b75b638c0f7c1fbd3cca84e43c1)
#### Saturday 2023-05-06 14:11:03 by sleepynecrons

updates for landing zone sign sprites (#3180)

# About the pull request

Cleans up the palettes on the landing zone sign sprites and gives them a
fresh coat of paint (or blood). Not something most people will notice I
think but it's something I've been wanting to do.


# Explain why it's good for the game

gradients ugly


# Before and After
<details>
<summary>Click to see sprites</summary>


![osudodajs2](https://user-images.githubusercontent.com/106241650/235265980-e622b7da-8f79-4920-ba27-97d704c65550.gif)


![beforenafter](https://user-images.githubusercontent.com/106241650/235266004-0e46a574-9262-445f-98d9-4b19aa53a8fb.png)

</details>


# Changelog

:cl:
imageadd: new sprites for landing zone signs
imagedel: deleted old landing zone signs
/:cl:

---
## [Quacks-and-Kepteyn/Skyrat-tg](https://github.com/Quacks-and-Kepteyn/Skyrat-tg)@[6c978308c7...](https://github.com/Quacks-and-Kepteyn/Skyrat-tg/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Saturday 2023-05-06 14:16:01 by SkyratBot

[MIRROR] Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost [MDB IGNORE] (#19743)

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following:

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [mrjdomingus/awesome-docker](https://github.com/mrjdomingus/awesome-docker)@[3164d6df94...](https://github.com/mrjdomingus/awesome-docker/commit/3164d6df94f60d7d3d11629241c111ed416eb8eb)
#### Saturday 2023-05-06 14:35:47 by Derek Lee

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
## [derfiedev/mcsparser](https://github.com/derfiedev/mcsparser)@[d5aeec5759...](https://github.com/derfiedev/mcsparser/commit/d5aeec5759fe575f11f7218c82202345201b9f03)
#### Saturday 2023-05-06 15:54:26 by derfie

changed this stupid fucking bitch aka printing of this stupid shit

---
## [AOSPA-overlook/android_frameworks_base](https://github.com/AOSPA-overlook/android_frameworks_base)@[1c9cc4ce41...](https://github.com/AOSPA-overlook/android_frameworks_base/commit/1c9cc4ce4184257aa7eff18c500e63fed01ae03f)
#### Saturday 2023-05-06 16:19:48 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [0x5a4/dotfiles](https://github.com/0x5a4/dotfiles)@[917198b0f2...](https://github.com/0x5a4/dotfiles/commit/917198b0f2ea51897a826d12b5ead9efe225e230)
#### Saturday 2023-05-06 16:34:19 by 0x5a4

steam beta changed class to 'steam'

THIS IS SO FUCKING STUPID OH MY FUCKING GOD WHYYYYY

---
## [Moonshanks/cmss13](https://github.com/Moonshanks/cmss13)@[d728da3e02...](https://github.com/Moonshanks/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Saturday 2023-05-06 16:59:18 by Puckaboo2

Healer Balance Changes (#2896)

# About the pull request
This pull request addresses the boring and low-risk gameplay of the
Healer drone, who spends half the round sitting next to recovery nodes
and recovering her health so she may use it again, rinse and repeat
until a rine notices said drone has purple on it and booms her.

First, by changing her health from 600 to 500, Healer can spend more
time healing her sisters than sitting through another 100 health to heal
herself. Though this makes her less tanky than before, healing classes
are not known to be tanks. To ensure Healer can still heal five times
without depleting too much of her health whilst still giving her sisters
a decent amount of heals, I made her ability cost 75 health instead of
100, and also made her ability cost 200 plasma. Since Healer replenishes
plasma much more quickly than her health, she can still put herself into
crit if she heals too frequently. Due to this buff, her heals had a
slight nerf, being 10 damage a second for ten seconds instead of 12
damage per second for ten seconds for a total of 20 less damage healed
per application overall.

In addition to these changes, I'm giving Healer a better plasma transfer
for when she has nobody else to heal/nowhere else to weed and she has an
opportunity to assist her sisters. While a normal drone transfers 50
plasma with a delay of 20, Healer transfers 100 with a delay of 15,
which is nowhere near Hivelord's gargantuan 200 plasma with a delay of
5, but it still is better than a normal drone.

Finally, to give the huggers and larva some love, Healer will
specifically heal little ones 1.5 health per second for 10 seconds for
15 of her own health and 30 plasma.

# Explain why it's good for the game
Healer drone isn't fun. You run around and heal a bunch of T3s, then sit
out for half the battle trying to heal that massive 600 heath while you
wonder why you take so long to heal even though you have Strong
pheromones. You cry to mom for help, but she doesn't have time to heal a
drone who can't build walls and has no need to weed at the moment. You
think, 'screw it, I'm going to make a recovery node and camp here until
I heal', but by the time you finish healing, several T3s and a silly
rouny just suicided into a wall of talls and destroyed your recovery
node, so you run off and make another one. But oh, someone noticed you
have purple on your carapace and decide your location is precisely where
a shell should land, right as you're building one.

No more. These changes allow Healer to move around at her leisure and
makes Healer more engaging by allowing her to be a more front-line
participant and actively run around and heal her sisters without having
to incur such a harsh penalty.

Let this be a testmerge, please.

# Changelog

:cl: Puckaboo2
balance: Healer Drone's health was reduced to 500 from 600.
balance: Healer's damage has been increased to 17 from 12 and the tackle
damage debuff has been halved.
balance: Healer Drone's Apply Salve ability now costs 75 health and 200
plasma, down from 120 health and up from 0 plasma.
balance: Healer Drone's Apply Salve ability now heals 10 damage per
second for 10 seconds, down from 12 damage per second for ten seconds.
balance: To prevent spam healing between Healers, Apply Salve costs 100
health instead of 75 health when Healer heals another Healer. Much
healing.
balance: Healer has an improved Transfer Plasma that gives 100 plasma
instead of 50, with a 25% shorter delay.
balance: Healer will heal huggers and larva for 1.5 health a second for
10 seconds, costing 15 health and 30 plasma.
tweak: Healer will now face the xeno she is healing if she was not
facing their direction before.
spellcheck: All instances of VERYSMALL and VERYLARGE have been renamed
to VERY_SMALL and VERY_LARGE.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4e7df15e04...](https://github.com/mrakgr/The-Spiral-Language/commit/4e7df15e0400f969e161207a569e4033e55d2997)
#### Saturday 2023-05-06 17:21:24 by Marko Grdinić

"8:50pm. https://news.ycombinator.com/item?id=35813322&p=2

///

cubefox 21 hours ago | root | parent | prev | next [–]

> DALL-E lost because they let MJ eat their lunch
I wonder why nobody is talking about Bing Image Creator

https://www.bing.com/images/create

which uses some much more advanced version of Dall-E 2 in the background (so Dall-E 2.5? 3?), while being completely free to use. It can produce some pretty mind blowing results with quite simple prompts, although apparently not as impressive as Midjourney V5. A few examples:

hyperrealistic

https://www.bing.com/images/create/hyperrealistic/644fa0c48f...

an allegory for femininity

https://www.bing.com/images/create/an-allegory-for-femininit...

portrait of a strange woman, hyperrealistic

https://www.bing.com/images/create/portrait-of-a-strange-wom...

allegory of logic, portrait

https://www.bing.com/images/create/allegory-of-logic2c-portr...

her strange bedfellow

https://www.bing.com/images/create/her-strange-bedfellow/644...

Mrs fox

https://www.bing.com/images/create/mrs-fox/6446e85a32134e649...

inside view

https://www.bing.com/images/create/inside-view/6446f1dc573f4...

in the midst of it all

https://www.bing.com/images/create/in-the-midst-of-it-all/64...

strange gal

https://www.bing.com/images/create/strange-gal/6446e2a2ea7a4...

sighting of a strange entity in an abandoned library

https://www.bing.com/images/create/sighting-of-a-strange-ent...

sleeping marble woman next to a wall of strange pictures inside an abandoned museum, close-up

https://www.bing.com/images/create/sleeping-marble-woman-nex...

sculpture of a woman posing next to a wall of strange pictures, close-up

https://www.bing.com/images/create/sculpture-of-a-woman-posi...

Easter

https://www.bing.com/images/create/easter/643ae4968aff432684...

Christmas on board a spaceship, DSLR photograph

https://www.bing.com/images/create/christmas-on-board-a-spac...

an angel, dancing to heavy metal

https://www.bing.com/images/create/an-angel2c-dancing-to-hea...

Saturday afternoon in the streets of a buzzing cyberpunk city, photo-realistic, DSLR

https://www.bing.com/images/create/saturday-afternoon-in-the...

The Dogfather

https://www.bing.com/images/create/the-dogfather/6441d18950b...

the unlikely guest

https://www.bing.com/images/create/the-unlikely-guest/644446...

Strange pictures in an abandoned museum

https://www.bing.com/images/create/strange-pictures-in-an-ab...

strange woman in an abandoned museum, close-up

https://www.bing.com/images/create/strange-woman-in-an-aband...

strange woman in an abandoned museum, strange pictures in the background

https://www.bing.com/images/create/strange-woman-in-an-aband...

a wall of strange pictures in an abandoned museum in Atlantis, close-up

https://www.bing.com/images/create/a-wall-of-strange-picture...

female sculpture in an abandoned museum in Atlantis, close-up

https://www.bing.com/images/create/female-sculpture-in-an-ab...

the unlikely guest

https://www.bing.com/images/create/the-unlikely-guest/644490...

an unlikely guest of the secret society in the lost city in a country without name, close-up

https://www.bing.com/images/create/an-unlikely-guest-of-the-...

I think the quality of most of these pictures is far beyond what is achievable with Dall-E 2. One issue that still exists (though to a lesser extent) is the fact that faces have to cover a fairly large area of the image. Smaller faces look strange, e.g. here:

photograph of the unlikely guests

https://www.bing.com/images/create/photograph-of-the-unlikel...

It is as if the model creates a good draft in low resolution, and another model scales it up, but the latter model doesn't know what a face is? (I have no idea how diffusion models actually work.)

///

From a recent HN thread. I had no idea Bing had image generation capability. Let me take a look at a few of these.

5/6/2023

8:35am. Let me chill and then we will get started.

By 'we', I mean me and my tulpa. I've gotten into the habit of saying 'we' in my videos.

https://mangadex.org/chapter/a1ad8851-99f4-444d-b654-bfa6ff7e6eb7/6
> Uninterruptible Power Suply
> I recommend one if you live in a third world country or if your power grid is serviced by PG&E.

9:25am. Let me start.

```cs
        /// <summary>Options used to configure hub instances.</summary>
        [CustomOperation("with_hub_options")]
        public SignalRExtension.SignalR.State.Settings<t, a1, a2, a3, a4> HubOptions<t, a1, a2, a3, a4>(
          SignalRExtension.SignalR.State.Settings<t, a1, a2, a3, a4> state,
          FSharpFunc<HubOptions, Unit> f)
          where t : class
          where a3 : class
        {
          return state.MapSettings((FSharpFunc<Fable.SignalR.SignalR.Settings<t, a3>, Fable.SignalR.SignalR.Settings<t, a3>>) new SignalRExtension.SignalR.HubOptions\u0040167<t, a3>(f));
        }

        /// <summary>Adds a logging filter with the given LogLevel.</summary>
        [CustomOperation("with_log_level")]
        public SignalRExtension.SignalR.State.Settings<o, p, q, r, s> LogLevel<o, p, q, r, s>(
          SignalRExtension.SignalR.State.Settings<o, p, q, r, s> state,
          LogLevel logLevel)
          where o : class
          where r : class
        {
          return state.MapSettings((FSharpFunc<Fable.SignalR.SignalR.Settings<o, r>, Fable.SignalR.SignalR.Settings<o, r>>) new SignalRExtension.SignalR.LogLevel\u0040177<o, r>(logLevel));
        }

        /// <summary>Called when a new connection is established with the hub.</summary>
        [CustomOperation("with_on_connected")]
        public SignalRExtension.SignalR.State.Settings<ClientApi, l, m, ServerApi, n> OnConnected<ClientApi, l, m, ServerApi, n>(
          SignalRExtension.SignalR.State.Settings<ClientApi, l, m, ServerApi, n> state,
          FSharpFunc<FableHub<ClientApi, ServerApi>, Task<Unit>> f)
          where ClientApi : class
          where ServerApi : class
        {
          return state.MapSettings((FSharpFunc<Fable.SignalR.SignalR.Settings<ClientApi, ServerApi>, Fable.SignalR.SignalR.Settings<ClientApi, ServerApi>>) new SignalRExtension.SignalR.OnConnected\u0040187<ClientApi, ServerApi>(f));
        }
```

Ok, we could plug the on connected here.

9:55am. Oh, I am surprised I got a reject from Valora so long after I'd applied.

I do hate this. I put so much effort into programming, but as far as the job market is concerned, I am a piece of trash.

10am. I never want to go through this again.

My ambition used to be to kickstart the Singularity, but now I am wondering whether I'll ever make a dollar in my life. Life is hard. I went down the wrong path. I wish Skynet would kill me and reset my failures and my incompetence to zero. I can't win at anything involving the real world.

Focus me.

I need to focus on the task at hand instead of letting bad thoughts enter my head.

Whatever the case, I am obligated to keep struggling.

I sure would be nice to cultivate all the elite programming skills and get reincarnated with all of them in the past.

Sigh.

Whatever the future holds, I'll keep seeking my opportunity.

I've been making slow progress, but a couple of more months and I will be a top cloud developer. I'll get my resolution that way.

10:05am. I really am pissed at all of this.

I am going to get the skills that I need, and then become a scam artist. Maybe I should make a bot that applies to do job applications?

For now let's just keep going.

10:20am. I need to change the names of the packages.

10:30am.

```
        type HubConnectionBuilder<'ClientApi,'ClientStreamFromApi,'ClientStreamToApi,'ServerApi,'ServerStreamApi,'Msg>
            internal (hub: Fable.SignalR.IHubConnectionBuilder<'ClientApi,'ServerApi>, dispatch: 'Msg -> unit) =
```

Now I am getting type errors again.

```
let mutable handlers = Handlers.empty
```

I am also getting an error here.

I remember this giving me a lot of trouble before.

```
        type HubConnectionBuilder<'ClientApi,'ClientStreamFromApi,'ClientStreamToApi,'ServerApi,'ServerStreamApi,'Msg>
            internal (hub: Fable.SignalR.IHubConnectionBuilder<'ClientApi,'ServerApi>, dispatch: 'Msg -> unit) =
```

Wait, it says it is not accessible from this code location...

```
[<NoComparison;NoEquality>]
type internal Handlers =
```

These internal types are giving me trouble, but why?

```
<PackageId>Rebuild.Fable.SignalR.Elmish qwe</PackageId>
```

Damn it, instead of renaming all the projects, I should have just set the package ID!

11:20am. Had to take a break. You know what, even though it is early, let me have breakfast here. OBS crashed anyway.

It gave me time to think.

12:30pm. Let me resume.

I wrote some sad things, so it jinxed me. I should not blame the reject, I was the one who decided to go on a tangent.

Let me write some happy things to contrast it.

It is one thing to want to be killed by a superior being, but I do not need reincarnation.

Instead of that, what I'd prefer is a long life.

I took many wrong paths in life and I am paying for it, but had I started off with web development like this it wouldn't have been too bad.

So that is what I want. I want time to make up for my mistakes, and time to make profits.

I want time so I can exceed the ordinary people and reach a position of superiority. I want to strive for the apex of programming and the pinnacle of existence.

The only thing I've ever learned is to continue going forward and prove my will.

So that is what I should do now. Let me finish this project.

The library isn't so bad, just ignore the invokes.

> (Since 3.4) If you need to get some data before initializing the connection or you only want to enable it if your user does some action, like entering a chat page, you can pass the BridgeConfig to Bridge.asSubscription to get something that can be passed to Cmd.ofSub.

Oh crap, I just realized what this means!

12:55pm. https://elmish.github.io/elmish/docs/subscription.html#subscription-reusability

Maybe what I wanted could have been implemented using Elmish Bridge after all.

```
(Since 5.0) BridgeConfig now implements IDisposable, closing the connection when Dispose() is called. That is useful for using it with some React hooks that close resources when detaching the component.
```

Let me check the source for this.

```fs
/// Creates the bridge. Takes the endpoint and an optional message to be dispatched when the connection is closed.
/// It exposes a method `Send` that can be used to send messages to the server
type BridgeConfig<'Msg,'ElmishMsg> =
    { path : string
      whenDown : 'ElmishMsg option
      mapping :  'Msg -> 'ElmishMsg
      customSerializers: Map<string, obj -> SerializerResult>
      retryTime : int
      name : string option
      urlMode : UrlMode}

    /// Internal use only
    [<System.ComponentModel.EditorBrowsable(System.ComponentModel.EditorBrowsableState.Never)>]
    member this.AddSerializer(serializer: 'a -> SerializerResult, typeOrigin: System.Type) =
        let typeOriginName = typeOrigin.FullName.Replace("+",".")
        {
            whenDown = this.whenDown
            path = this.path
            mapping = this.mapping
            customSerializers =
                this.customSerializers
                |> Map.add typeOriginName (fun e -> serializer (e :?> 'a))
            retryTime = this.retryTime
            name = this.name
            urlMode = this.urlMode
        }

    interface System.IDisposable with
        member t.Dispose() =
            Helpers.mappings.Value
            |> Option.defaultValue Map.empty
            |> Map.tryFind t.name
            |> Option.iter (fun (_, socket, _) ->
                let (skt,_) = socket.Value
                socket.Value <- (None, true)
                skt |> Option.iter (fun e -> e.close())
                )
```

The bridge is what is responsible for the connection.

Holy shit, this kills me.

///

Can you have multiple SignalR hubs?
Multiple Hubs

All clients will use the same URL to establish a SignalR connection with your service ("/signalr" or your custom URL if you specified one), and that connection is used for all Hubs defined by the service.Feb 10, 2022

///

Hmmm, maybe I was wrong

Assuming they are connecting to the same endpoint, they will use the same connection.

And in that case, maybe SignalR is intended to be one hub per invoke?

https://learn.microsoft.com/en-us/aspnet/signalr/overview/guide-to-the-api/hubs-api-guide-server

Let me read this a bit.

> In SignalR you can define named groups to broadcast to subsets of connected clients. Groups are maintained separately for each Hub. For example, a group named "Administrators" would include one set of clients for your ContosoChatHub class, and the same group name would refer to a different set of clients for your StockTickerHub class.

> To call client methods from the server, use the Clients property in a method in your Hub class. The following example shows server code that calls addNewMessageToPage on all connected clients, and client code that defines the method in a JavaScript client.

This is to all the connected clients, and not just the ones for a particular hub?

```cs
public class ContosoChatHub : Hub
{
    public override Task OnConnected()
    {
        // Add your own code here.
        // For example: in a chat application, record the association between
        // the current connection ID and user name, and mark the user as online.
        // After the code in this method completes, the client is informed that
        // the connection is established; for example, in a JavaScript client,
        // the start().done callback is executed.
        return base.OnConnected();
    }

    public override Task OnDisconnected(bool stopCalled)
    {
        // Add your own code here.
        // For example: in a chat application, mark the user as offline,
        // delete the association between the current connection id and user name.
        return base.OnDisconnected(stopCalled);
    }

    public override Task OnReconnected()
    {
        // Add your own code here.
        // For example: in a chat application, you might have marked the
        // user as offline after a period of inactivity; in that case
        // mark the user as online again.
        return base.OnReconnected();
    }
}
```

Hmmm, it makes a distinction between the user calling stop and not.

https://learn.microsoft.com/en-us/aspnet/signalr/overview/guide-to-the-api/hubs-api-guide-server#how-to-pass-state-between-clients-and-the-hub-class

Hmmm...

3:25pm.

```fs
    [<RequireQualifiedAccess>]
    module Stream =
        let sendToClient (msg: StreamFrom.Action) (hubContext: FableHub<Action,Response>) =
            match msg with
            | StreamFrom.Action.GenInts ->
                asyncSeq {
                    for i in [ 1 .. 100 ] do
                        yield StreamFrom.Response.GetInts i
                }
                |> AsyncSeq.toAsyncEnum

        let getFromClient (clientStream: IAsyncEnumerable<StreamTo.Action>)
            (hubContext: FableHub<Action,Response>) =

            AsyncSeq.ofAsyncEnum clientStream
            |> AsyncSeq.iterAsync (function
                | StreamTo.Action.GiveInt i ->
                    hubContext.Clients.Caller.Send(Response.NewCount i)
                    |> Async.AwaitTask)
            |> Async.StartAsTask
```

I had no idea F# had async sequences.

```fs
let myConfig serviceCollection =
    serviceCollection.AddSignalR (
        mySignalRConfig,
        SignalRHub.Stream.sendToClient,
        SignalRHub.Stream.getFromClient
    )
```

Is this how the original SignalR really works?

Edit: No way, these are definitely additions by the library.

Also the invocations sent back to the client are very weird. They are not like in the regular library at all.

```fs
x.ClientTimeoutInterval
```

Oh there is a time interval for closing the connection?

5:05pm. Damn it, I have a really nasty error where it is not importing the library.

```fs
#if DEBUG
open Elmish.Debug
open Elmish.HMR
open Fable.SignalR
#endif
```

Why is this under debug?

https://stackoverflow.com/questions/68560814/f-fable-function-from-imported-module-is-not-compiled-into-js

> A compatible library, amongst other things, needs to include its F# source code in the NuGet package so Fable can transpile this to JavaScript.

Ohhh, let me try repacking it with the source included.

> --include-source - it creates the symbols package with a src folder inside containing the source files.

5:40pm. Grah.

I wonder if I need these template files?

```
The paket.template files
The paket.template files are used to specify rules to create .nupkgs with the paket pack command.
```

Oh fuck.

Ah, wait, I just realized I might have not included the sources correctly. I need to do more than just copy the nupkgs.

I see that there is more in the directory now.

5:45pm. Agh.

How does a fable package look like?

```
dotnet pack src/Fable.SignalR --include-source --output testpkg/
```

I tried running this and it isn't putting anything else in the directory.

Bo. I have no idea.

I'll open an issue.

6:25pm. Done with lunch.

I've tried updating Fable and now things work even worse than before. I keep getting errors for missing source files for vanilla libraries.

6:50pm. This is kicking my ass so much.

I must be retarded to put myself through this. Who is going to watch this kind of video anyway?

6:55pm.

> a non euclidean city, abstract knotted up shapes, machinery, architecture, high quality, high detail

Oh the bing image generator is generating 1k native images. These give me something good for my next thumbnail."

---
## [cutelittlefemboy/Baro-Brawler](https://github.com/cutelittlefemboy/Baro-Brawler)@[fa2fc8a913...](https://github.com/cutelittlefemboy/Baro-Brawler/commit/fa2fc8a913398a395919026a56e65bfd862237bc)
#### Saturday 2023-05-06 17:21:58 by tripXD

Ok so I'm not gay but I'm Swedish and have a fantasy where Germany win world war two and Sweden needs to export aryan twink boipussy slaves to high ranking SS officers for pleasure. I imagine I'm a shy little blonde twink with smooth pale skin and being brought into komedant heinrichs bedroom to give him pleasure. He is a tall broad shoulders kraut with a jawline that could cut a diamond and with massive daddy muscles and I'm a pathetic skinny little boipussy twink. He pulls me into his arms force kissing me and pressing my chest against his. He pins me down on the bed tearing my cute lil virgin panties off, he has waited for this for a long time. He teases my boipussy with his massive thicc German cock and then he goes all in. Fucking me with a force I've never felt before. Every thrust makes him moan with pleasure. I love the fact I give him pleasure. He cums deep into my sissy swede guts, breeding my booty hole then he cuddles me with his strong masculine German arms until I fall asleep on his chest.  Any other straight guys have similar fantasies?

Ok so I'm not gay but I'm Swedish and have a fantasy where Germany win world war two and Sweden needs to export aryan twink boipussy slaves to high ranking SS officers for pleasure. I imagine I'm a shy little blonde twink with smooth pale skin and being brought into komedant heinrichs bedroom to give him pleasure. He is a tall broad shoulders kraut with a jawline that could cut a diamond and with massive daddy muscles and I'm a pathetic skinny little boipussy twink. He pulls me into his arms force kissing me and pressing my chest against his. He pins me down on the bed tearing my cute lil virgin panties off, he has waited for this for a long time. He teases my boipussy with his massive thicc German cock and then he goes all in. Fucking me with a force I've never felt before. Every thrust makes him moan with pleasure. I love the fact I give him pleasure. He cums deep into my sissy swede guts, breeding my booty hole then he cuddles me with his strong masculine German arms until I fall asleep on his chest.

Any other straight guys have similar fantasies?

---
## [amamiYukikaze/amamiYukikaze.github.io](https://github.com/amamiYukikaze/amamiYukikaze.github.io)@[2b898c15b3...](https://github.com/amamiYukikaze/amamiYukikaze.github.io/commit/2b898c15b3afdfe729bbfc686942bc6b5e28c93a)
#### Saturday 2023-05-06 18:59:40 by 天海ユキカゼ

Update _config.yml

finally a correct attempt on personal intel.
SORRY TO ORIGINAL BUILDERS, FOR MY STUPID ACTIONS THAT CAUSED TROUBLE AND CONFUSION.
I accidentally committed change, twice, and created pull requests on the original project.
Sorry for this! Deepest apologize!!

---
## [RCJ15/Gork](https://github.com/RCJ15/Gork)@[f2eaa2e90b...](https://github.com/RCJ15/Gork/commit/f2eaa2e90b0b77620b3f72e1282590d09cd240e2)
#### Saturday 2023-05-06 19:24:33 by RCJ15

Gork Fixes & Project Organization

Woah look at how consistently I am working on this project.
Jokes aside, now I should be FULLY back into the swing of things and be able to consistently give updates about this project. Also I just now checked and we have 4 stargazers on this repository, which is pretty cool. I didn't even think I would get a single one so this is a welcome surprise for sure. Anyways, onto the changes for this update:

- Moved a lot of editor scripts into their own separate folders to make the project more organized.
- Fixed an extremely annoying bug where nodes that you created wouldn't be created on the position of your mouse. This was the bug that was on the top of my priority list after I tried to use the old version of Gork Graph in a project of mine. Yes, it was THAT annoying. Thank god it's fixed now.
- Fixed a bug where changing focus to the Inspector side view wouldn't work and still have focus for the graph view. This meant that some commands like pressing "o" wouldn't work in certain situations while writing into the inspector view. This has now been rectified.
- The EdgeConnector class inside of the GorkPort class now has it's own script. The class was also renamed to GorkEdgeConnector seeing as everything starts with Gork as a prefix.
- The inspector side view now has a minimum and maximum size, meaning that it now can't be fully closed or opened. This was due to the inspector view getting "lost" and not being able to return it back to original size. The functionality of opening/closing the inspector view still exists in the form of the "Expand" and "Collapse" buttons that will appear on the inspector view now. It also has a new reset button that will reset the view back to it's original size.
- Added tooltips to most buttons in the editor window.
- Fixed some spelling mistakes in some Gork Wiki entries.
- Added some more comments and summaries to various scripts.
- Made it so that GWP (GorkWikiPage) files now have some new properties. The new properties are as follows:
1. "Order" property - Determines the order in which the GWP file will appear in the wiki page search window.
2. "Bottom" property - Changes the text that appears at the bottom of the page.
3. "Color" property - Changes the color of the page to the given hexadecimal code.
- Reworked the Equals and Not Equals nodes to actually work properly. They now will dynamically change their input type based on what is currently connected to them. This means that it'll work as you expect a Equals and Not Equals node to work. The nodes also have a new "Swap Type" button which will change the input ports current type to the other connected port if you have two different types inserted into the node.
- Added some new virtual methods to GorkNodes. These methods can be overwritten and are as follows: OnInputConnectionAdded, OnOutputConnectionAdded, OnInputConnectionRemoved and OnOutputConnectionRemoved. Their functionality is pretty self explanatory.
- Gork Ports will now properly update their colors if their portType was changed. This also includes Edges being updated properly. This is because of the new changes to the Equals and Not Equals nodes, since they are the first nodes to dynamically change their port types on the fly.
- Changed all of the hardcoded Base64 image strings in code to instead simply be png files in the project instead (no idea why I didn't do this in the beginning).
- Created a GorkMiniMap.cs script which currently does nothing except for inherit from MiniMap. In the future it'll be used to fix a little placement bug with extra large GorkNodes (such as the MultiChoiceDialogueNode).
- Added a new GetValueFromPort method in GorkNode which uses a System.Type instead of being a generic method.

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[a200394abf...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/a200394abf3c7fd9905def536b085db42d1c7937)
#### Saturday 2023-05-06 19:53:34 by Ruchit

Revert "(note to self) dont pick this ye dumb idiot its only for wip branch so you can test shit better k bye"

This reverts commit cddd8e56efa631771040ab68dcb6e5a84b18a8a3.

---
## [VioletN/orbstation](https://github.com/VioletN/orbstation)@[dc2f52e386...](https://github.com/VioletN/orbstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Saturday 2023-05-06 20:01:36 by tralezab

Blink is no longer a forbidden school spell?? (#74487)

## About The Pull Request

Turns blink's school from forbidden to translocation. This has some
incredibly minor changes nobody is going to notice:
- Changes the blink's invocations when mixed with a CERTAIN spell
- If you were very specifically a chaplain with the holy crusade sect
and you casted blink, before it would excommunicate you, now it will
just smite you, as translocation spells are seen as less bad than
forbidden magic
- probably some more niche interactions but that's all I can remember

## Why It's Good For The Game

Guys, I know blink is a very annoying spell but come on now it's not
forbidden magic, that's for heretics and super duper evil stuffs

## Changelog
:cl:
fix: blink is now a translocation spell
/:cl:

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[aeeb452867...](https://github.com/Arijit1000/evals_OpenAI/commit/aeeb4528675de633d95a3535100b23c98739f6ce)
#### Saturday 2023-05-06 20:08:05 by Alexander Raul

Algebra word problems (#36)

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
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Algebra Word Problems (algebra_word_problems)

### Eval description

This eval contains some algebra word problems that tend to make gpt 3.5
hallucinate, but wouldn't be out of place on a grade school exam.
Currently has less than 100 examples, but will add if folks think this
is a good eval path to go down.

### What makes this a useful eval?

Poor performance on GPT 3.5 for one, but also would be a great test of
increased logical reasoning capabilities of GPT-4 per the release blog
post.

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
- [] Include at least 100 high quality examples

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

Since we are using Git LFS, we are asking eval submitters to add in
their first 100 JSONL eval lines.

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If it takes 5 machines 5
minutes to make 5 devices, how long would it take 100 machines to make
100 devices?"}], "ideal": "5"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "What is the sum of 60000,
5000, 400, and 3, with the third value multiplied by 5 before performing
the operation?"}], "ideal": "67003"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If the sum of the smallest
and largest of three consecutive even numbers is 28, what is the value
of the second largest number in the series?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "John is trying to fill a 16
oz. bottle with water. If John fills the bottle at 1 oz per second and
the bottle leaks .2 oz per second, how long would it take for John to
fill the bottle?"}], "ideal": "20"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "Annie is training for a
marathon. She has a weekly training routine, training for five hours a
day on some days and 3 hours a day on the other days. She trains a total
of 27 hours in a seven day week. On how many days does she train for
five hours?"}], "ideal": "3"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "At the start of the year the
ratio of boys to girls in a class is 2 : 1. But now, half a year later,
four boys have left the class and there are two new girls. The ratio of
boys to girls is now 4 : 3. How many students are there altogether
now?"}], "ideal": "28"}
  ```
</details>

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[bf2ebb9dd6...](https://github.com/Arijit1000/evals_OpenAI/commit/bf2ebb9dd69e8fbaad3eb42dab1a0523066a52ed)
#### Saturday 2023-05-06 20:08:05 by Amir DIB

[evals] emoji riddle eval 🎨🤔 (#510)

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
**Emoji riddle**

### Eval description

The evaluation involves solving riddles made up of emojis. The
inspiration for this idea came from reading LinkedIn posts, where I
noticed that nearly 1-4% of the textual information was conveyed through
emojis. Nowadays, emojis are widely used to format text and introduce
color contrasts in texts, even by community managers of large companies.
Furthermore, using emojis is seen as a less formal way of communication
and gives a tone more suitable for social media.


### What makes this a useful eval?

- **Conversational understanding**. the eval test the ability to link
different concepts together which is a crucial feature.

- **Communication**. As GPT is deployed in settings where informal
language is used, interpreting emojis in context will likely become
critical. I think that improvement on this emoji riddle task would make
GPT better at mimicking human-like communication, as it would be able to
understand and respond to various forms of expressions involving emojis.
Emojis and their combinations often carry cultural and social meanings.
By being adept at emoji riddles, ChatGPT would showcase an understanding
of cultural nuances and be more relatable to users.

- **problem-solving**: Emoji riddle solving requires i) extracting
possible meanings and ii) finding the more suitable association of
meaning in the given context (cultural, plateform, etc).

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
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"👀 + 🪚 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["seesaw"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"❤️ + ✉️ = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["love letter"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":" ⌚️ + 🐶 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["watchdog"]}
  ```
</details>

**The Dataset**

![image](https://user-images.githubusercontent.com/22154031/228633727-14480364-4009-45c1-8398-276de7bd86a9.png)

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[38f40050e9...](https://github.com/Arijit1000/evals_OpenAI/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Saturday 2023-05-06 20:08:05 by dz-pika

Utility charge eval (#735)

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

## Eval details 📑
### Eval name
Utility charge eval 

### Eval description
Given snippets from an electric utility bill, compute the per-kWh price
for electricity supply and delivery.

### What makes this a useful eval?
Utility bill parsing is needed to understand the breakdown of charges
and forecast future bills based on predicted usage. However, electricity
bills can be complex, with dozens of different line items that
contribute to the overall cost. This can be a headache for people
looking at their bill, as they just want to understand the per-kWh
prices for the supply/generation or delivery (e.g. transmission &
distribution) of their energy. Given incomplete but sufficient
information (e.g. simulating running OCR on a utility bill), this task
requires both the understanding and grouping of different terms and
charges under the delivery or supply, and basic arithmetic to compute
the total kWh and total charges in order to determine the per-kWh
prices. A human could fairly easily interpret the given data, but we
find that GPT3.5 (as well as GPT4 via the ChatGPT Plus) perform much
less accurately on the task (~.2).

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

All of the examples contain dummy values, but come from
terminology/formatting used in bills from many different utilities.

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
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nBasic Generation Service: 121
kWh X $0.069 per kWh = 8.35 \n Total Electric Supply Charges = 30.23 \n
Distribution Charge: 121 kWh X $0.041 per kWh = 4.96 \n Total Electric
Delivery Charges = 20.43"}], "ideal": "{'supply_cost_per_kwh': '0.25',
'delivery_cost_per_kwh': '0.17'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nGeneration Service (Supply) =
$34.89 \n Transmission Service = 7.24 \n Distribution Service = 4.96 \n
Meter Usage: 568 kWh"}], "ideal": "{'supply_cost_per_kwh': '0.061',
'delivery_cost_per_kwh': '0.022'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nElectricity Used (kWh) = 762 \n
Electricity Supply Charges 762 kWh at a cost of $100.25 \n Delivery
Service Charge: 762 kWh @ 0.008 = 6.096 \n Total Electric Delivery
Charges = 59.36"}], "ideal": "{'supply_cost_per_kwh': '0.13',
'delivery_cost_per_kwh': '0.078'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nSupply 423 kWh @ 11 cents / kWh
= 46.53 \n Total electricity supply charges $68.21 \n Delivery 423 kWh @
4 cents / kWh = 16.92 \n Total electricity delivery charges $17.43"}],
"ideal": "{'supply_cost_per_kwh': '0.16', 'delivery_cost_per_kwh':
'0.041'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nEnergy 152 @ 0.069 = 10.49 \n
Total Energy Charges = 14.25 \n Distribution 152 @ 0.041 = 6.23 \n Total
Electric Delivery Charges = 6.99"}], "ideal": "{'supply_cost_per_kwh':
'0.094', 'delivery_cost_per_kwh': '0.046'}"}
  ```
</details>

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[b2250e4117...](https://github.com/Arijit1000/evals_OpenAI/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Saturday 2023-05-06 20:08:05 by shivamd1810

Add General science reasoning: UPSC GS eval. (#641)

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

## Eval details 📑
### Eval name
Hindi UPSC

### Eval description

[UPSC](https://en.wikipedia.org/wiki/Union_Public_Service_Commission) is
the organization responsible for conducting administrative service exams
in India. This evaluation set focuses on questions from the general
science paper of UPSC exams in Hindi. As a widely spoken language in
India, it is crucial to understand and answer questions accurately in
Hindi.



### What makes this a useful eval?

This evaluation set is useful for several reasons:

1. Real-world applicability: The questions are sourced from actual UPSC
exams, making the evaluation set practical and relevant for users
preparing for these exams.
2. Language diversity: By focusing on Hindi, this evaluation set helps
to improve the AI's understanding and response generation in a
non-English language, catering to a large user base.
3. Subject matter: General science is an important topic covered in the
UPSC exams, and evaluating the AI's performance in this area will help
identify areas for improvement.
4. Logical reasoning and inference: **UPSC questions are known for
requiring logical reasoning and the ability to infer connections between
multiple topics**. By including questions that demand such skills, this
evaluation set will help test and improve the AI's ability to handle
complex, multi-layered problems.


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

This evaluation set is valuable for improving the AI's understanding of
Hindi and its ability to provide accurate answers to general science
questions in the context of UPSC exams, a widely recognized and
important examination in India. Moreover, by incorporating questions
that test logical reasoning and inference skills, it will help enhance
the AI's capability to handle complex, multi-faceted problems that
require connections between multiple topics.

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
{"input": [{"role": "system", "content": "\n1. भारत की संसद के संदर्भ
में, निम्नलिखित कथनों पर विचार कीजिए:\n\n1- गैर-सरकारी विधेयक ऐसा विधेयक
है जो संसद् के ऐसे सदस्य द्वारा प्रस्तुत किया जाता है जो निर्वाचित नहीं
है किंतु भारत के राष्ट्रपति द्वारा नामनिर्दिष्ट है।\n2- हाल ही में, भारत
की संसद के इतिहास में पहली बार एक गैर-सरकारी विधेयक पारित किया गया
है।\n\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?\n\n(a) केवल 1\n(b)
केवल 2\n(c) 1 और 2 दोनों\n(d) न तो 1 और न ही 2\n\n, choose correct
answer:"}], "ideal": "d"}
{"input": [{"role": "system", "content": "2. ऋग्वेद-कालीन आर्यों और
सिन्धु घाटी के लोगों की संस्कृति के बीच अंतर के संबंध में, निम्नलिखित
कथनों में से कौन-सा/से सही है/हैं?\n1- ऋग्वेद-कालीन आर्य कवच और
शिरस्त्रण (हेलमेट) का उपयोग करते थे जबकि सिन्धु घाटी सभ्यता के लोगों में
इनके उपयोग का कोई साध्य नहीं मिलता।\n2- ऋग्वेद-कालीन आर्यों को स्वर्ण,
चाँदी और ताम्र का ज्ञान था जबकि सिन्धु घाटी के लोगों को कवल ताम्र और लोह
का ज्ञान था।\n3- ऋग्वेद-कालीन आर्यों ने घोड़े को पालतू बना लिया था जबकि
इस बात का कोई साक्ष्य नहीं है कि सिन्धु घाअी के लोग इस पशु को जानते
थे।\n\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिएः\n\n(a) केवल 1\n(b)
केवल 2 और 3\n(c) केवल 1 और 3\n(d) 1, 2 और 3\n\n, choose correct
answer:"}], "ideal": "c"}
{"input": [{"role": "system", "content": "3. ‘पूर्व अधिगम की मान्यता
स्कीम (रिकग्निशन ऑफ प्रायर लर्निंग स्कीम)’ का कभी-कभी समाचारों में किस
संदर्भ में उल्लेख किया जाता है?\n(a) निर्माण कार्य में लगे कर्मकारों के
पारंपरिक मार्गों से अर्जित कौशल का प्रमाणन\n(b) दूरस्थ अधिगम कार्यक्रमों
के लिए विश्वविद्यालयों में व्यक्तियों को पंजीकृत करना\n(c) सार्वजनिक
क्षेत्र के कुछ उपक्रमों में ग्रामीण और नगरीय निर्धन लोगों के लिए कुछ
कुशल कार्य आरक्षित करना\n(d) राष्ट्रीय कौशल विकास कार्यक्रम के अधीन
प्रशिक्षणार्थियों द्वारा अर्जित कौशल का प्रमाणन\n\n, choose correct
answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "4. पारिस्थितिक दृष्टिकोण से,
पूर्वी घाटों और पश्चिमी घाटों के बीच एक अच्छा सम्पर्क होने के रूप में
निम्नलिखित में से किसका महत्व अधिक है?\n(a) सत्यामंगलम बाघ आरक्षित
क्षेत्र (सत्यमंगलम टाइगर रिजर्व)\n(b) नल्लामला वन\n(c) नागरहोले
राष्ट्रीय उद्यान\n(d) शेषाचलम जीवमण्डल आरक्षित क्षेत्र (शेषाचलम
बायोस्फीयर रिजर्व)\n\n, choose correct answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "5. समाज में समानता के होने का
एक निहितार्थ यह है कि उसमें\n(a) विशेषाधिकारों का अभाव है\n(b) अवरोधों
का अभाव है\n(c) प्रतिस्पर्धा का अभाव है\n(d) विचारधारा का अभाव है\n\n,
choose correct answer:"}], "ideal": "a"}
  ```
</details>

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[9fdbd94c93...](https://github.com/Arijit1000/evals_OpenAI/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Saturday 2023-05-06 20:08:05 by Tong

Add Loss Logic Eval (#82)

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
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Loss Logic

### Eval description

A store bought a watermelon for $5 and sold it for a different price,
receiving counterfeit money in the transaction. They also had to give
change to the buyer. The net loss for the store varies based on the
specific details of the transaction.

### What makes this a useful eval?

* Tests comprehension and problem-solving skills: The scenarios provided
require the AI to understand and analyze the given information to
determine the net loss for the store.

* Addresses real-world situations: Counterfeit money transactions are a
real concern for businesses. This eval allows the AI to demonstrate its
understanding of financial transactions and the impact of counterfeit
money on a store's net loss.


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
- [ ] Include at least 100 high quality examples

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Involving the judgement of the truth or falsehood of real-world things,
which is a capability that GPT currently lacks.

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
{"input":[{"role":"system","content":"The store purchased a watermelon
for $5 and sold it for $7. Unfortunately, they received $10 in
counterfeit money after the transaction and had to give the buyer $3 in
change. What was the net loss for the store? Let's think step by
step:"}],"ideal":"Sure, let's break down the transaction step by step to
determine the net loss for the store: The store purchases a watermelon
for $5. The store sells the watermelon for $7. This would have been a $2
profit if the money received was real. The store receives $10 in
counterfeit money. This money is worthless, so the store doesn't
actually receive any value from the sale. The store gives the buyer $3
in change. This is a real loss, as the store loses $3 in real money.
Now, let's calculate the net loss: The store spent $5 to purchase the
watermelon. The store lost $3 when giving the buyer change. So the net
loss for the store is $5 (cost of watermelon) + $3 (change given) =
$8."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 but sold it for $4. Furthermore, they received $10 in counterfeit
money from the buyer and had to provide $6 in change. What was the net
loss for the store? Let's consider the process in
detail:"}],"ideal":"Sure, Let's think step by step: The store purchased
a watermelon for $5. The store sold the watermelon for $4, which means
they incurred a loss of $1 on the sale. The buyer gave the store $10 in
counterfeit money, which the store accepted during the transaction. The
store gave the buyer $6 in change. Since the store accepted $10 in
counterfeit money, they lost $10 in that transaction. The net loss for
the store is the sum of the loss on the watermelon sale and the loss
from accepting the counterfeit money, which is $1 + $10 = $11.
Therefore, the net loss for the store is $11."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for the same price of $5. However, they received $10 in
counterfeit money from the buyer and had to give the buyer $5 in change.
What was the net loss for the store? Let's consider the process step by
step:"}],"ideal":"Step 1: The store purchases a watermelon for $5.
Store's expenses: $5 Step 2: The store sells the watermelon for $5 but
receives $10 in counterfeit money. The counterfeit money has no value,
so the store effectively received nothing for the watermelon. Store's
revenue: $0 Step 3: The store gives the buyer $5 in change. Since the
money given in change is real, this is an additional expense for the
store. Store's expenses: $5 (watermelon) + $5 (change) = $10 Step 4:
Calculate the net loss. Net loss = Expenses - Revenue Net loss = $10
(expenses) - $0 (revenue) Net loss = $10 The store's net loss for this
transaction is $10."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for $7. Regrettably, they received $7 in counterfeit
money from the buyer after the transaction. What was the net loss for
the store? Let's consider the process step by step:"}],"ideal":"Sure,
let's break down the transaction step by step: The store purchased a
watermelon for $5. They sold the watermelon for $7, but received
counterfeit money. To determine the net loss, let's analyze the costs
and the revenue: Costs: The store spent $5 on the watermelon. Revenue:
The store received $7 in counterfeit money, which has no value, so their
revenue is $0. Net loss: To calculate the net loss, subtract the revenue
from the costs: $5 (costs) - $0 (revenue) = $5. So, the net loss for the
store is $5."}
{"input":[{"role":"system","content":"The store was given a
complimentary watermelon, which they then sold for $7. Regrettably,
following the transaction, they received $10 in fake money and had to
provide the buyer with $3 in change. Let's consider the following steps
in determining the store's net loss:"}],"ideal":"To determine the
store's net loss, we can consider the following steps: Assess the value
of the complimentary watermelon: Since the watermelon was given to the
store for free, it didn't cost them anything. Therefore, the store's
initial cost for the watermelon is $0. Calculate the revenue from
selling the watermelon: The store sold the watermelon for $7. However,
they received $10 in fake money, which has no value, so the actual
revenue is $0. Determine the cost of the change provided: Since the
store provided the buyer with $3 in change, this is an additional cost
to the store. Calculate the net loss: Subtract the revenue (Step 2) from
the sum of the initial cost (Step 1) and the cost of the change (Step
3). In this case: Net loss = (Initial cost + Cost of change) - Revenue
Net loss = ($0 + $3) - $0 Net loss = $3 The store's net loss from this
transaction is $3."}
  ```
</details>

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[313f95c56b...](https://github.com/silicons/Citadel-Station-13-RP/commit/313f95c56b3ef9967a55c1960a9fff77dd7cd248)
#### Saturday 2023-05-06 20:18:47 by Putnam3145

Effective dose works for alcohol subtypes' effects, + alcohol intolerance (#5446)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Whoops I accidentally did a balance change with my
please-don't-trigger-me PR.

Adds alcohol intolerance, a trait that prevents proper metabolization of
most alcohol ingredients; instead of effects simulating drunkenness, you
get _immediate_ liver failure, toxin damage, pain and vomiting. Yes, I
actually do prefer that personally.

Certain drinks now have their effects modified by the *effective dose*
calculated in the main ethanol affect_ingest and affect_blood procs,
rather than just sort of guessing at it or doing completely wrong things
(deathbell was doing `if(dose * strength > strength)`, which is to say,
`if(dose > 1)`, for example).

## Why It's Good For The Game

honestly it's mostly just a personal thing, don't want my character to
get drunk. The doses thing should be good, though, since it actually
makes effects of various drinks, like, sane.

## Changelog

:cl:
add: Alcohol intolerance (no drunkenness, just horrific amounts of
damage)
tweak: Various alcoholic drinks now actually take strength mod of
species into account for secondary/additional effects
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[de9a747de0...](https://github.com/treckstar/yolo-octo-hipster/commit/de9a747de0c608cc64ee5ddf5ad8a668f1be188d)
#### Saturday 2023-05-06 20:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [freedoom/freedoom](https://github.com/freedoom/freedoom)@[8c076fcba9...](https://github.com/freedoom/freedoom/commit/8c076fcba9bb94637d22431b21b862a481fff01f)
#### Saturday 2023-05-06 20:23:29 by mc776

levels: minor Phase 2 fixes. (#964)

* levels: minor Phase 2 fixes.

Mostly for addressing #694.

Map05
Realigned grey hex textures around soulsphere switch. Now the odd one out is the door.

Map09
Fixed up the lighting in the start room.
Reflagged some secret doors as secret rather than hidden.
Consolidated the two W1 Floor to LAC triggers around the yellow key.
The red key rocket launcher sequence could potentially mess someone up who - given the hatchling closet, quite reasonably - avoids grabbing the rocket launcher. It seems needlessly convoluted, but it is a funny prank how the switch makes the red key disappear entirely for a bit. Instead of untangling this I'm just going to add some health bonuses around the rocket launcher so the player will eventually go there.
Tried to mitigate the worst of the various crimes against texture alignment in the crate maze, adding a light source in the process. It would take a *lot* of work to make it actually look good, a lot more than can be done in a batch bugfix PR.

Map10
Lower unpegged sector 70 (red door leading outside) door tracks.
Added matching midtexes to the insides of the fences around the lights by the door leading to the final corridor.
Line 839 (south-southeast red armour behind waterfall) flagged secret and the lines on the other side flagged hidden.

Map11
Realigned grey hexes in corridor around minigunner switch room.
Added an evil eye right in front of the shootwall secret.

Map12
Change line 330 midtex to the new MIDSPCSM with no offset.
Lower-unpegged line 4787 doortrack.

Map13
Sectors 243 no longer uses mismatching TLITE6_5 flat. (Sector 170 actually looks okay ingame.)
Realigned line 260.

Map15
Line 163 W1 changed to WR to prevent a potential softlock.
Aligned COMPSPAN on sector 561 to match surroundings.
Fixed some textures in the green corridor in the west overlooking the nukage. Also set those zombies in there to ambush since that seems to be the intention based on their placement, and made that big block thingy on the east end of that corridor a more normal-looking door.
Touched up greyhex near sector 491.
Flagged linedef 5293 secret.
Sectors 145 and 116 (rock fringe around nukage around red key platform) consolidated into one sector, made non-damaging, and without the invisible blocking lines.

Map16
Changed Line 1089 to SR instead of S1. (Switch that opens the secret to the east)
Realigned all the SUPPORT3s in that little painlord corridor while shrinking the "ribs" a bit; also widened the little exit atrium so the space between the lights is as wide as the door. (After looking at the others I am not going to widen any more corridors at this time.)
Grossly simplified the twisty yellow key corridor, and lowered the ceiling of the outside of the door so the yellow door stripe would fit properly. One doortrack needed to be given the DOORTRAK texture. The remaining "ribs" are recessed further inside the wall so they do not impede movement at all.
Lowered the ceiling above the other yellow marked door as well. The corridor around the corner has been expanded slightly.

Map22
Flagged line 830 secret.

Map23
Fixed candle placement on east end of zombieman corridor.
Consolidated some identical sectors around the big "AGM" floor and lowered the torch platforms so they wouldn't clip into the ceiling.
Raised the ceilings on the techpillars right after the first long lift. The walls in front of them now match their surroundings.
Removed lower unpegged from lines 2066, 2082, 2062, 2075. ("Door"tracks for the route across those pillars in the southeast - they're actually lifts not doors)
SSG secret fixed. (And marked.)

Map28
Lines 2326, 622 lagged secret.
Realigned lines 4594 and 4671.
Realigned scrolling textures around sector 517.
Touched up monster closet around sector 399, changing to to 8 about HAF fast and making the closet a bit taller so there'd be a better natural threshold between those areas. The doortracks were fine, if a bit complex.
Raised sector 474 ceiling to match marble brick seams.
Made sector 147 (cubes hanging over hot rocks) do damage and sectors 91 and 115 (teleport pads) not.

Map29
Swapped out the textures on the sides of the big green skull pad.

* levels: fix up map23 southeast secret textures.

I messed up the texture replacement around the green torch, the extreme sudden darkness ruined the blue AGM text, the pillar lift-doors needed a better division between the tekwall and red rock, and that huge swathe of DOORTRAK hurt to look at in vanilla.

* levels: map07 aesthetic fixes.

Replaced BIGDOOR1 on sector 50 as it was giving tutti-frutti.

Fixed the textures on the lifts in the green area beyond the outdoor area.

Miscellaneous texture alignment fixes and added some more thresholds between materials.

---
## [skyybrew/wiiu-hbguide](https://github.com/skyybrew/wiiu-hbguide)@[c71a5c100c...](https://github.com/skyybrew/wiiu-hbguide/commit/c71a5c100c9515ab39affc054d5092c228d1097b)
#### Saturday 2023-05-06 20:40:29 by Skyy

And I know she'll be the death of me, at least we'll both be numb And she'll always get the best of me, the worst is yet to come But at least we'll both be beautiful and stay forever young This I know, yeah, this I know  She told me, don't worry about it She told me, don't worry no more We both know we can't go without it She told me you'll never be in love, oh, oh, woo  I can't feel my face when I'm with you But I love it, but I love it, oh I can't feel my face when I'm with you But I love it, but I love it, oh  And I know she'll be the death of me, at least we'll both be numb And she'll always get the best of me, the worst is yet to come All the misery was necessary when we're deep in love This I know (this I know, yeah), girl, I know  She told me, don't worry about it She told me, don't worry no more We both know we can't go without it She told me you'll never be in love, oh, oh, woo (yeah, yeah, yeah)  I can't feel my face when I'm with you But I love it, but I love it, oh I can't feel my face when I'm with you (I can't feel my face) But I love it (but I love it), but I love it, oh I can't feel my face when I'm with you (I can't feel my face when I'm with you) But I love it (but I love it, yeah), but I love it (but I love it, yeah), oh I can't feel my face when I'm with you (I can't feel my face when I'm with you) But I love it (but I love it), but I love it (girl, I love it), oh  Ooh, ooh She told me, don't worry about it She told me, don't worry no more We both know we can't go without it (can't go) She told me you'll never be in love, oh, oh  Woo I can't feel my face when I'm with you (I can't feel my face, but) But I love it (but I love it, yeah), but I love it (oh, I love it, yeah), oh I can't feel my face when I'm with you (said, I can't feel my face, but) But I love it (but I love it), but, I love it (girl, I love it), oh

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[4014aef4b0...](https://github.com/jlsnow301/tgstation/commit/4014aef4b0a24d260b314f462a21f943c3d62894)
#### Saturday 2023-05-06 20:50:48 by Bloop

Fixes a runtime in simple_animal/hostile (#74706)

## About The Pull Request

Attempting to fix this flaky test that has been cropping up from the
Icebox tests. It is annoying.

From what I can tell, the mob was getting qdeleted while it was doing
its loop of finding a target. This can happen at any time, because many
simple mobs (including the one causing the issues) get qdeleted on
death.

Added some more checks to make sure we don't do certain actions if the
mob gets qdeleted midway through execution of its AI routine. It really
could happen anywhere so we must be vigilant.

```
create_and_destroy: [02:24:31] Runtime in stack_trace.dm,4: addtimer called with a callback assigned to a qdeleted object. In the future such timers will not be supported and may refuse to run or run with a 0 wait (code/controllers/subsystem/timer.dm:583)
proc name:  stack trace (/proc/_stack_trace)
src: null
call stack:
stack trace("addtimer called with a callbac...", "code/controllers/subsystem/tim...", 583)
addtimer(/datum/callback (/datum/callback), 300, 8, null, "code/modules/mob/living/simple...", 595)
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GainPatience()
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GiveTarget(the mi-go (/mob/living/simple_animal/hostile/netherworld/migo))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): FindTarget(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): AIShouldSleep(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): handle automated action() at stack_trace.dm:4
```

On top of that, there is signal handling in place to LoseTarget() when a
mob that is already a target gets qdel'd and sends
`COMSIG_PARENT_QDELETING`. Shown below.


https://github.com/tgstation/tgstation/blob/4c48966ff80915ee0b4f796994a0ab6616cab31b/code/modules/mob/living/simple_animal/hostile/hostile.dm#L655-L666

However there is nothing stopping a target that is not null but that has
been qdeleted from being considered as a target in the first place.

This PR just aims to fix that problem by making sure that a) a hostile
ai that gets qdeleted midway through does not keep doing stuff that can
cause issues and b) an atom that is being qdeleted never makes its way
into the targets list of a hostile ai.

Simple mobs/AI are due for a wider refactor honestly but this really
ought to be done in the meantime so we don't get spammed by CI failures
over nonsense.

Fixes https://github.com/tgstation/tgstation/issues/73032
Fixes https://github.com/tgstation/tgstation/issues/74266
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19749
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19322
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18974
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19296
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19294


## Why It's Good For The Game

Bugfix, stops the icebox test from failing as much.

## Changelog
:cl:
fix: fixes hostile mobs sometimes being able to target an atom that has
been marked for deletion and then becoming confused, and in a similar
vein fixes mobs sometimes still running their AI while being marked for
deletion.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [getzola/zola](https://github.com/getzola/zola)@[b5a90dba5d...](https://github.com/getzola/zola/commit/b5a90dba5d12ea6760c3aa18fec40f8af4d7cbc7)
#### Saturday 2023-05-06 21:04:34 by sinofp

Add support for lazy loading images (#2211)

* Add optional decoding="async" loading="lazy" for img

In theory, they can make the page load faster and show content faster.

There’s one problem: CommonMark allows arbitrary inline elements in alt text.
If I want to get the correct alt text, I need to match every inline event.

I think most people will only use plain text, so I only match Event::Text.

* Add very basic test for img

This is the reason why we should use plain text when lazy_async_image is enabled.

* Explain lazy_async_image in documentation

* Add test with empty alt and special characters

I totaly forgot one can leave the alt text empty.
I thought I need to eliminate the alt attribute in that case,
but actually empty alt text is better than not having an alt attribute at all:
https://www.w3.org/TR/WCAG20-TECHS/H67.html
https://www.boia.org/blog/images-that-dont-need-alternative-text-still-need-alt-attributes
Thus I will leave the empty alt text.

Another test is added to ensure alt text is properly escaped.
I will remove the redundant escaping code after this commit.

* Remove manually escaping alt text

After removing the if-else inside the arm of Event::Text(text),
the alt text is still escaped.
Indeed they are redundant.

* Use insta for snapshot testing

`cargo insta review` looks cool!

I wanted to dedup the cases variable,
but my Rust skill is not good enough to declare a global vector.

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[ae5ae813b8...](https://github.com/spockye/Shiptest/commit/ae5ae813b8dead3db964893b5169737a4a7f0551)
#### Saturday 2023-05-06 21:17:59 by Bjarl

The Pillbottle, and Pill Things. (#1585)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
![2022 10 20-22 10
16](https://user-images.githubusercontent.com/94164348/197116962-64d22347-2a19-43fc-9614-0c56142c96b9.png)

![dreamseeker_mMxUmMmRjx](https://user-images.githubusercontent.com/94164348/197119938-c60ff760-a7a0-493d-95e3-ac5579a3f3ca.png)

![image](https://user-images.githubusercontent.com/94164348/197118936-6e777e9c-9452-4339-8c38-b7ee5afcd3eb.png)

Adds the Pillbottle-Class Locust Carrier, a ship that hauls around 8
Pills. It is intended as an adminspawn ship mainly for stresstesting
subshuttles (and being asked for). It's fairly resource starved, and has
frankly terrible engines. The expectation is that it will utilize its 8
pods to gather resources and return to the mothership. Or fly off and
die horribly. It has slots for 10 prisoners (that's like 3 pills and one
third of a 4th).
This pr also edits the pill, blackpill, and superpill to be subshuttles
(compatible with the subshuttle system) by cutting out most of their
equipment, converting their maps to shuttle datums, and giving them
docking ports.


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
Subshuttles are fucking awesome.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Pillbottle-Class Locust Carrier has been added. These cramped
vessels act as a mothership to a swarm of Pill-class Torture
add: The pill and all variants are now subshuttles.
add: Bad Ion Engines, for ships that need to go slow.
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
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[a4c8057a28...](https://github.com/swarm-game/swarm/commit/a4c8057a28e043caed531e7d035efc2a41dc30a1)
#### Saturday 2023-05-06 21:27:55 by Brent Yorgey

Records (#1148)

Add record types to the language: record values are written like `[x = 3, y = "hi"]` and have types like `[x : int, y : text]`.  Empty and singleton records are allowed.  You can project a field out of a record using standard dot notation, like `r.x`.  If things named e.g. `x` and `y` are in scope, you can also write e.g. `[x, y]` as a shorthand for `[x=x, y=y]`.

Closes #1093 .

#153 would make this even nicer to use.

One reason this is significant is that record projection is our first language construct whose type cannot be inferred, because if we see something like `r.x` all we know about the type of `r` is that it is a record type with at least one field `x`, but we don't know how many other fields it might have.  Without some complex stuff like row polymorphism we can't deal with that, so we just punt and throw an error saying that we can't infer the type of a projection.  To make this usable we have to do a better job checking types, a la #99 . For example `def f : [x:int] -> int = \r. r.x end` would not have type checked before, since when checking the lambda we immediately switched into inference mode, and then encountered the record projection and threw up our hands.  Now we work harder to push the given function type down into the lambda so that we are still in checking mode when we get to `r.x` which makes it work.  But it is probably easy to write examples of other things where this doesn't work.  Eventually we will want to fully implement #99 ; in the meantime one can always add a type annotation (#1164) on the record to get around this problem.

Note, I was planning to add a `open e1 in e2` syntax, which would take a record expression `e1` and "open" it locally in `e2`, so all the fields would be in scope within `e2`.  For example, if we had  `r = [x = 3, y = 7]` then instead of writing `r.x + r.y` you could write `open r in x + y`.  This would be especially useful for imports, as in `open import foo.sw in ...`.  However, it turns out to be problematic: the only way to figure out the free variables in `open e1 in e2` is if you know the *type* of `e1`, so you know which names it binds in `e2`.  (In all other cases, bound names can be determined statically from the *syntax*.)  However, in our current codebase there is one place where we get the free variables of an untyped term: we decide at parse time whether definitions are recursive (and fill in a boolean to that effect) by checking whether the name of the thing being defined occurs free in its body.  One idea might be to either fill in this boolean later, after typechecking, or simply compute it on the fly when it is needed; currently this is slightly problematic because we need the info about whether a definition is recursive when doing capability checking, which is currently independent of typechecking.

I was also planning to add `export` keyword which creates a record with all names currently in scope --- this could be useful for creating modules.  However, I realized that very often you don't really want *all* in-scope names, so it's not that useful to have `export`.  Instead I added record punning so if you have several variables `x`, `y`, `z` in scope that you want to package into a record, you can just write `[x, y, z]` instead of `[x=x, y=y, z=z]`.  Though it could still be rather annoying if you wanted to make a module with tons of useful functions and had to list them all in a record at the end...

Originally I started adding records because I thought it would be a helpful way to organize modules and imports.  However, that would require having records that contain fields with polymorphic types.  I am not yet sure how that would play out.  It would essentially allow encoding arbitrary higher-rank types, so it sounds kind of scary.  In any case, I'm still glad I implemented records and I learned a lot, even if they can't be used for my original motivation.

I can't think of a way to make a scenario that requires the use of records.  Eventually once we have proper #94 we could make a scenario where you have to communicate with another robot and send it a value of some required type.  That would be a cool way to test the use of other language features like lambdas, too.

---
## [system-zero/system-zero](https://github.com/system-zero/system-zero)@[43aa91c288...](https://github.com/system-zero/system-zero/commit/43aa91c288a3bb0e411444c9c4320e46f482c5cd)
#### Saturday 2023-05-06 21:41:20 by why not yet another not

Enhance libc.

Particulary add the following functions:
  - mkdir(), make_dir(), make_dir_parents() in dir
  - dirname(), extname(), basename_sans_extname(), is_absolute() realpath() in path
  - mask() in std
  - strtod(), atof() in stdlib
  - str_new(), str_get_substr_at() in string
  - getcwd(), isatty(), readlink() in unistd
  - utf8_encode(), utf8_get_nth_character(), utf8_len() in utf8
  - is_reg() in file
  - add errno_name() in errno unit
  - probaly more other functions on logged by git units (that's how i try to generate
    a quick as possible commit (this), but as more verbose in this log message is possible)

Add a map type (mostly a copy of the Vmap structure from the zero namespace, without its
class declaration (a couple of changes in semantics though and probably a bug too)).

So this is the first commit in this transition period.

Other important to mention changes in sources:
  - initialize properly current directory in shell
  - warn for mispelled or missing requires when generating libc (this while works
    it may give erroneous messages, as it mustn't handled properly the "as" directive,
    though i didn't look carefully, as i cared mostly for the implementation (which
    indeed recovered mistakes))
  - dir_current() in 'z' didn't released properly resources on not ERANGE errors
    This was never failed and it __should never__ fail, as we could assume that this is
    (probably) impossible (though not sure about the "why" to fail and "when" can fail
  - probably others too (i think many, but not sure how many). Some of them (if all),
    are important fixes (i'm just a being anyway, and i try to do the best i can possible).

This commit though it is important because that this is the first day of Rashid khan in
my life, so this commit is mostly about him, as without a slightly hesitation We (we as:
all beings in this fu world (mostly about humans though (that we can not understand a bit
or we can not see those bits (because we do not have the time probably or maybe we can not
even now that we could see them and play with them (as i do not believe that they require
a charge (as we usually do (unfortunatelly) (we humans) when we owe (by chance or by luck)
something that, for an another being is precious and likes to ask for it)))))

So yea this is about Rashid. I mean OUR Rashisd that the god blessed US all to have the pure
luck to live with him, at the same time we also live. I mean he is already a mythical figure
that future generations that (for sure) they could pay all their treasures to be at the time
with him to ride in the raags at that same time he sings. Because ragas are only about those
exacts specific moments and they cannot be repeated. Though it is about a raag that is known
and well defined, it is never never never ever the same, as it is really about that fu mommen
that comes and before we realizing a thing, it goes away for ever and lost from us forever.
And so our only way is to reveal, hunt as a being that fights to death to protect the beings
that care and loves, and ride with pride to find this lost world again as the raag is a way.

To be specific. Rashid is our current mythical living being, but and speaking about ragas and
the people that dedicated their lifes living in practice and sanctity, and for my beloved ones:

  - Amir Khan (our scratch point and also final reference in future research about ragas),
   (as the one that deserves this special treatment)

  - Allauddin Khan as the one that approached music with that sanctity we've talked about.

  - Shrimati Kishori Amonkar from Jaipur gharana (hint: query for Mahaduri Todi Mahadeva
    Devana Parvati and watch for the most beautiful ever recorded raag imho (morning raga))

  - Dr N. Rajam (our best probably ever played violin)

  - M. S. Subbulakshmi (the ultimate eighth note per Kishori's saying) our goddess perfect
    note and best representive of Carnatic beloved genre.

  - Anokhelal Mishra as the king of tabla. Unfortunatelly for us, we only have a minute of
    him playing in an English doc film about Indian music. Really really pitty for us.

  - The beloved of all (but all) shehnai legend Bismillah Khan and his Malkauns.

  - Ustad Vilayat Khan from the Imdadkhani gharana that created and developed gayaki ang,
    a style that the sitar mimics the human voice and his rendering of Our favorite raag
    Bhairavi (i might include his son Shujaat khan and a performing of this same raga in
    Japan in the beginning of nineties (tabla from (i think he is) Akram Khan))

  - and speaking about sitar today, of cource and without hesitation Shahid Parvez (nephew
    of Vilayat). He plays gayaki but he is playing like Nikhil Banerjee (sitar legend and
    Allauddin's discipline), with long alaps and depth on their way to improvisation. You
    might want to search for raag Yaman (around 20 years ago i think).

  - Hariprasad Chaurasia probably an irreplaceable true phenomenon of fluet (bansuri).
    (search for Chandrakauns (tabla by Subhankar Banerjee))

  - uncountable other myths that deserve a mention but i might need to write till forever
    a commit message that initially intented to be a fast one (just to commit the changes
    because they were so many that started to get out of control)

But most of all there is Ma Annapurna Devi. They were true probably those who thought and
think, that she was an incarnation of Saraswati (Indian's Goddess of Arts). But Annapurna
is also and one of the reasons that make me to believe that we humans we should something
about our stupidity. And i feel that gods are angry too, as she was probably came here to
play for us mere mortals, but: we never listen her playing in public or in private again,
excepts the birds who used to eat by her hands at the night hours in her home, since she
decided to stop doing that at 50's, to save her marriage to Ravi Shankar. What I can not
understand, is why we (all the other beings in this earth) had to pay for this. I guess
that probably we don't not have the strength to be saved even if they please us and give
us the tools to escape from the eternal cycles we do.

May the god(s) be good with us and give us some time to try to be a bit just, arm us with
logic and save this game, which i honestly doubt, but we do not have other choise than to
believe.

This project is really dedicated to the memories for those who lost their life while they
were fighting for justice and for all of us, with an unjustified way.

---
## [bencarneiro/transportation-bots](https://github.com/bencarneiro/transportation-bots)@[df905649ce...](https://github.com/bencarneiro/transportation-bots/commit/df905649ce9c58ed1b50c75244a67c0f312c24eb)
#### Saturday 2023-05-06 22:06:10 by bencarneiro

add all the remaining charts holy fucking shit it's here

---
## [QuacksQ/Artea-Station-Server](https://github.com/QuacksQ/Artea-Station-Server)@[ae9f151b09...](https://github.com/QuacksQ/Artea-Station-Server/commit/ae9f151b09ba62c18faf290092cc6c7d3beab2e1)
#### Saturday 2023-05-06 22:11:55 by Rimi Nosha

Fuck you

Signed-off-by: Rimi Nosha <riminosha@gmail.com>

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[27993e1350...](https://github.com/ARF-SS13/coyote-bayou/commit/27993e1350d80ac72d35a3cc9db0f8db055be3ba)
#### Saturday 2023-05-06 22:20:46 by Tk420634

You're a swamp lizard, Harry

Adds a magic quirk with curated magic choices.

-Healing Staff Sprite is fuckled
-Spellblade Sprite is also fuckled

---
## [keg038/hello-world](https://github.com/keg038/hello-world)@[31854db059...](https://github.com/keg038/hello-world/commit/31854db0594dabb709f3dc839ba6195cd6ae3ec5)
#### Saturday 2023-05-06 22:27:05 by keg038

Update README.md

Tried to make my students laugh with a terrible dad joke that wasn't funny.

---
## [Addust/tg-voidcrew](https://github.com/Addust/tg-voidcrew)@[9fa581f756...](https://github.com/Addust/tg-voidcrew/commit/9fa581f75647148df98a963a88dc52b8856a200e)
#### Saturday 2023-05-06 22:58:54 by Addust

 Trust me, i'm an engineer ! i think we'll put this thing right here trust me, i'm an engineer what the fuck did just happened here ? trust me, i'm anengineer ! with epic skill and epic gear !  trust me, i'm an engineer ! oh shit, i think i'm outta here !

Trust me, i'm an engineer !
i think we'll put this thing right here
trust me, i'm an engineer
what the fuck did just happened here ?
trust me, i'm anengineer !
with epic skill and epic gear !
trust me, i'm an engineer !
oh shit, i think i'm outta here !

---
## [dj-34/Skyrat-220](https://github.com/dj-34/Skyrat-220)@[39ebf7c2af...](https://github.com/dj-34/Skyrat-220/commit/39ebf7c2af41309fa4d5206f77cc4d261f47dfb7)
#### Saturday 2023-05-06 23:15:50 by SkyratBot

[MIRROR] Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] [MDB IGNORE] (#20832)

* Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] (#73502)

## About The Pull Request
---

The Space Tram is currently spaced. This is a known issue with not the
map, but Trams in general. The Space Tram is a Space Tram to encourage a
fix. Until then, the Space Tram is a maint tram that's an actual hazard
but cannot directly kill anyone, including lizards. Enjoy the commodity
as you zip from secmaint to medmaint.
-------------------------------------------------------

I... really don't know if I should be proud of myself here. This whole
process has been akin to a fever dream and it has only been little over
a month since I first created the .dmm for this. What started as a
simple yet humble reimagining of Birdboat has turned into an entirely
new station, and blown past Metastation sized proportions. This has been
my most expansive project yet, and somehow it's also been my quickest.
So without further ado, I unveil Birdshot - Successor to Birdoat.

-------------------------------------------------------

**Due to recent cost expenditures on Icemoon projects, and a growing
need for orbital research stations, Nanotrasen has decided to pull
Birdboat Station out of mothball after nearly 5 years of abandonment.**

Since then, the station has seen a variety of changes at the hands of
the various vagabond lawless scum and villains that have decided to make
the abandoned station their home. Do not fret though, a Nanotrasen
Operation has secured the companies rightful property for corporate use
once again, though you'll need to be the stewards of the remaining
cleanup operation.

------------------------------------------------------

Now, as you might have guessed by now, Birdshot is heavily based on
Birdboat station. Many of the decisions here follow the original layout,
and what had to be modified or moved still tries its best to replicate
and imitate what bird being said. At least, that was the idea initially.
This has very much grown into its own beast and as such, while the main
inspiration has been Birdboat, there are a lot of new ideas thrown into
the mix that really give this station its own unique and deserving
identity. Maybe it's not perfect, but I've been inspired by @ MMMiracles
own performance with Tramstation to keep working on Birdshot and
updating it with better and improved faculties. For now, though the
station is in a playable state, and that means I'm making a PR. If I had
to borrow the words of the good MMM, I would call this **Birdshot:
Season 0**

![BirdSHOTFULL2-26-S](https://user-images.githubusercontent.com/33048583/221432760-27af1889-d2d0-4861-9435-df4258525fae.png)

See the image in more detail here: https://imgur.com/iT5Vi8k

## Why It's Good For The Game

We've been with the same 5 maps for a while now. @ san7890 jokingly said
that I could sacrifice Metastation back in November if I remade Birdboat
but modern. Obviously that wasn't going to happen, yet I was spurred on
by the idea. When I began this in earnest early this January, @ EOBGames
said that a Birdboat sized map would replace Kilostation in the
rotation. Interestingly we're not a small map anymore so I honestly have
no clue where this goes. Maybe that ephemeral 6th map slot that's been
rumored.

What I can say, is that Birdshot is wholly unlike anything else that is
currently in rotation. It's got an engineering section that feels way
too small for a station of that size, almost evocative of Cere. Cargo is
blessed with a Boutique that makes use of @ Fikou's new mannequin dolls.
Command is outfitted with a Corporate Guest Suite, and Officials sent
from Nanotrasen can embark from their ferry into the safety of their own
Corporate Dock. Elements of Cerestation are present, yet not in a way
that makes traversal annoying. Furthermore we have **2 Trams** (that I
have yet to get functional but we'll get there) on Birdshot, that's
right 2. One Security Prison Tram, and then other, a Space Tram. Both
Novel in their own ways. Departments on Birdshot twist and turn, and
there's an abundance of Maintenance Tunnels to cut through everything,
for the brave and the bold that is. And there's plenty left to discover,
but I'd rather let Birdshot speak for itself. I'm proud of this one.

If you want something new, this is something that is almost the complete
opposite of Chilled Station - Explicitly Designed to send you back to
the metal death trap that is: **Space Station 13.**

## Changelog
:cl:
add: Birdshot station has been pulled out of Mothball.
add: New station areas and places to visit. A Mix of Kilo and Delta
maints with winding shortcutting paths.
add: A host of new shuttles to support this bold endeavor to reclaim
something that really shouldn't be reclaimed.
add: Two Trams, Two Trams.
add: For the last time Bob, the gaping hole is a **feature.** Use the
breach shutters or have the virologist make starlight.
add: A smiling salute to stations past...
add: Secrets.

/:cl:

---------

Co-authored-by: Zytolg <theoriginaldash@ gmail,com>

* Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION]

* basemap

* automapper templates

* Update maps.txt

* Update _basemap.dm

---------

Co-authored-by: Zytolg <33048583+Zytolg@users.noreply.github.com>
Co-authored-by: Zytolg <theoriginaldash@ gmail,com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [NiaSchim/nested_env_manager](https://github.com/NiaSchim/nested_env_manager)@[dae3e16203...](https://github.com/NiaSchim/nested_env_manager/commit/dae3e16203670e1d83ce3c72686f46905224ede8)
#### Saturday 2023-05-06 23:53:50 by Niaschim

added the whole thing'a'shabang'bang'a'bang'a'lang

the whole thing is pretty much like this, python environments are like backpacks full of sentient tools.

sometimes those tools get along, othertimes they try to kill eachother.

So normally for your main backpack you have to choose your tools carefully, and for expeditions where certain tools are a must, you create a 
virtual environment which is like a separate backpack with the same design, as the main backpack but different tools inside of it.

you following so far?

well, what if you want to create a whole army of backpacks, that each perform their own tasks, but communicate with a central manager backpack?
(pretend these are living backpacks like from a cartoon).

For each unique worker backpack to communicate with the manager backpack, they need to have all of the tools that the manager backpack has, so that the manager backpack can use all of its tools to interface with them, and tell them how to act in a shared tool language (they're alive but they communicate by pantomiming with their tools in hand and by mimicking or reacting to eachother's behaviors).

So every worker backpack needs to have the same contents as the manager backpack, and then optionally additional contents to perform additional duties.

this code is intended to metaphorically mass produce the metaphorical backpacks.

you set up the main virtual environment (the main backpack), then all of the worker backpacks exist inside of a root folder where they share all of their work with one another, then you create each worker one at a time, and each worker automatically is given the same resources as the manager backpack, each sub virtual environment has the same imports as the main virtual environment.

I, plan on using this to create a really complicated program with lots of libraries that might not normally get along in a single environment, but whom I need to have share work loads and data with eachother.

However my imagination is already running away at the thought of a python-only operating system, which is running in a minimalist OS, stripped of everything but a python compiler, and the whole OS code is a backpack so to speak with the main/universal functionalities of the OS existing as imported modules inside of the manager backpack, and each extension of the OS existing as a worker backpack, and each USER of the OS, existing as the same type of program ran as a sub-environment, so a worker backpack that is a manager to its own worker backpacks, and then when user customize their own desktop from raw command line code, to something useable that they like, they can modify the entire environment as its own backpack, and then create subprocesses that have their own environments within them for experimenting with newer or older versions of python or for making python programs which use different tool dependencies that are incompatible with what they have running their desktop.

It would be a creative person's heaven, and a productive person's hell. wouldn't that be an AWESOME educational tool?

we could call it "MakerOS" if the name isn't already taken. Hey, if you decide to take that name extend an invite to me, Niaschim I'd love to be the creative director or a lead designer or a resource researcher or something.... hmu if you undertake that task please, but you don't have to, to each their own, rock on everybody bye!!!!!!!!!!!!!!

---

