## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-08](docs/good-messages/2023/2023-05-08.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,097,600 were push events containing 3,375,754 commit messages that amount to 251,277,230 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 60 messages:


## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[1a918a2e14...](https://github.com/MTandi/tgstation/commit/1a918a2e1411f58e5a90f587a92daebebb9ac395)
#### Monday 2023-05-08 00:20:09 by Jacquerel

Golem Rework (#74197)

This PR implements this design document:
https://hackmd.io/@Y6uzGFDGSXKRaWDNicSiEg/BkRr176st
Put briefly, this will remove every existing golem subtype and
consolidate golems into a single species with cool new sprites.
NOT implemented from that PR is the ability to eat Telecrystals, I
couldn't come up with an appropriate visual that can stack with the
existing ones, but that should be a reasonably trivial add for a future
artist & developer.

New Golems have a food-based mechanic where their hunger decays pretty
quickly and can only be replenished by eating minerals. They start
moving slower as they get hungrier, until eventually they become
completely immobilised and need to be rescued.
Eating different kinds of minerals will visually change your sprite and
give you a special effect in a similar way to old golems, but temporary.
While transformed, you can't eat any other kind of mineral which would
transform you (but can still consume glass).
To see the full list of effects, look at the hackmd above.

In service of these sprites working I have refactored the
`species/offset_features` feature by killing it and delegating that
responsibility to limbs instead. Rather than applying an offset to items
due to your species, it is due to your weird head or arms. This makes
overall more sense to me, but it inflates the code changes in this PR
somewhat.
It doesn't make a lot of sense to atomise unfortunately because that
code also seemed to be entirely unused until I tried to use it in this
PR, so you wouldn't be able to tell if my changes broke anything. I
might make a downstream sad by doing this.

All of the actual numbers in this PR are made up and only loosely
tested, it will need some testmerges to gather feedback about whether it
sucks or not.

Other relevant changes:
I reworked how bioscrambling works based off bodypart bodytypes, to
automatically exclude golem limbs in either direction. There's really no
way to have those work on humans or vice versa. Organs still fly though.

---
## [bearrrrrrrr/coyote-bayou](https://github.com/bearrrrrrrr/coyote-bayou)@[27993e1350...](https://github.com/bearrrrrrrr/coyote-bayou/commit/27993e1350d80ac72d35a3cc9db0f8db055be3ba)
#### Monday 2023-05-08 00:27:43 by Tk420634

You're a swamp lizard, Harry

Adds a magic quirk with curated magic choices.

-Healing Staff Sprite is fuckled
-Spellblade Sprite is also fuckled

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[912e843f53...](https://github.com/BlueMemesauce/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Monday 2023-05-08 00:32:43 by san7890

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
## [newstools/2023-express](https://github.com/newstools/2023-express)@[b5a7bc367a...](https://github.com/newstools/2023-express/commit/b5a7bc367a4bdb6fa9a832d81533fe8cd4f6c4c4)
#### Monday 2023-05-08 00:55:19 by Billy Einkamerer

Created Text For URL [www.express.co.uk/celebrity-news/1766703/Nicole-Scherzinger-boyfriend-Lewis-Hamilton-Thom-Evans-love-life]

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[f1fef9b0c3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/f1fef9b0c3f10e6191ed51be93d092050e77c531)
#### Monday 2023-05-08 01:16:10 by SkyratBot

[MIRROR] Demotes Psyker Pirates to Bounty Hunter Duty [MDB IGNORE] (#20951)

* Demotes Psyker Pirates to Bounty Hunter Duty (#75031)

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

* Demotes Psyker Pirates to Bounty Hunter Duty

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [wupeng-engineer/Open-Assistant](https://github.com/wupeng-engineer/Open-Assistant)@[b9c60ed582...](https://github.com/wupeng-engineer/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Monday 2023-05-08 01:33:23 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[c5dce84be8...](https://github.com/DATA-xPUNGED/DataStation/commit/c5dce84be826ea945a11c492dce7eb2c2789548a)
#### Monday 2023-05-08 01:44:59 by Rhials

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
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[1674f25725...](https://github.com/DATA-xPUNGED/DataStation/commit/1674f25725c25e15769b031553b42144f526f841)
#### Monday 2023-05-08 01:44:59 by John Willard

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
## [Elli-Skala/Skyrat-tg](https://github.com/Elli-Skala/Skyrat-tg)@[e7a6f94460...](https://github.com/Elli-Skala/Skyrat-tg/commit/e7a6f94460cc391e7afc69682ddbefc87e036261)
#### Monday 2023-05-08 01:56:14 by SkyratBot

[MIRROR] Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances [MDB IGNORE] (#20358)

* Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

## About The Pull Request

- Signallizes head revolutionary flash conversion code, moving it out of
core flash code.
- Removes "tacticool" flashing from head revs, but they can still
convert from any direction

- Fixes April Fools "You son of a bitch! I'm in" force say never
working.
   - Revs are muted on conversion so they couldn't talk.
       - Fixed by only muting revs on non-holidays
   - Cultists are unconscious on conversion so they couldn't talk
       - Fixed by only unconscious-ing cultists on non-holidays
- Brainwash victims are more often than not unconscious / asleep so they
couldn't talk
       - Just left this one.

- Reduced the chance of them occurring and limits it to April Fools only
- A 1% chance of the force says ocurring means they will happen pretty
much once a week, given multiple rev / cult rounds happen every week and
on average like, 20 people are converted. A little absurd, it's good
that it never worked?

## Why It's Good For The Game

Antag code in core item code is bad

It's funny this meme has existed for like 2, 3 years now? No one's
tested it, it's never worked

## Changelog

:cl: Melbert
refactor: Removes Rev code from core flash code
fix: Getting converted on April Fools now triggers the meme force say as
always intended
del: The meme force say can no longer trigger on any day (it didn't work
before anyways)
/:cl:

* Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [kokizzu/genqlient](https://github.com/kokizzu/genqlient)@[ff790e1c06...](https://github.com/kokizzu/genqlient/commit/ff790e1c0631db0144b0752fbf3890cb622432e9)
#### Monday 2023-05-08 01:59:06 by Ben Kraft

Add an option to handle enums with ugly casing (#270)

There are a bunch of places in genqlient where we just kind of hope you
don't have ridiculous casing conflicts in your schema. Apparently with
enum values there are actual schemas that have this problem! Now we have
an option to disable. I ended up putting it all under `casing` instead
of in `bindings` so we can clearly document the list of algorithms we
support, and so we can have an `all_enums` value if you're working with
a schema with a lot of this; in the future we may want to add similar
behavior for types/fields, add more possible algorithms (e.g. to make
things unexported), etc.

I added tests for the new feature, although the way the tests are set up
it wasn't convenient to do so for a schema where this is actually
required. I also added a check for case conflicts that points you to
this option. (I don't want to do it automatically for reasons described
in the issue; mainly it just seemed a bit too magical.)

Fixes #265.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[21363d07a5...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/21363d07a5eec9fbce5be2f17cd1693319906d61)
#### Monday 2023-05-08 02:02:40 by SkyratBot

[MIRROR] De-holes holy arrows [MDB IGNORE] (#20985)

* De-holes holy arrows (#75184)

## About The Pull Request

Covers the 2-pixel hole in the holy arrow sprite with 1 alpha pixels to
prevent unintentional missed clicks.

## Why It's Good For The Game

It's annoying and a bad experience to think you clicked on a sprite but
actually landed on a tiny transparent hole and clicked nothing or the
object below the one you wanted.

## Changelog
:cl:
image: Holy arrows are now 15% less holy (You can no longer click on the
2-pixel hole in the arrowhead and unintentionally click the object below
the arrow instead.)
/:cl:

* De-holes holy arrows

---------

Co-authored-by: Thunder12345 <Thunder12345@users.noreply.github.com>

---
## [lebedev/tgstation](https://github.com/lebedev/tgstation)@[c3b78761d2...](https://github.com/lebedev/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Monday 2023-05-08 03:05:49 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [lebedev/tgstation](https://github.com/lebedev/tgstation)@[b5ebf5c942...](https://github.com/lebedev/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Monday 2023-05-08 03:05:49 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [IPerhapsCode/School-moment](https://github.com/IPerhapsCode/School-moment)@[37aacbbd89...](https://github.com/IPerhapsCode/School-moment/commit/37aacbbd89612e1554d39c1846b17a8c5e415d41)
#### Monday 2023-05-08 03:08:50 by IPerhapsCode

yo fuck prog holy shit le projet final est trop tof

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3822f00c27...](https://github.com/treckstar/yolo-octo-hipster/commit/3822f00c275e54ab194d120324b05acedb991a41)
#### Monday 2023-05-08 03:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [tabulon-ext/inxi](https://github.com/tabulon-ext/inxi)@[ed7049fcc1...](https://github.com/tabulon-ext/inxi/commit/ed7049fcc14fd5a1bb7e01b9674ad4c64e90cefa)
#### Monday 2023-05-08 03:45:18 by Harald Hope

Completion of the audio fixes and improvements of 3.3.26. Added less common
sound servers like EsounD and aRts, and made state reports more accurate for
ALSA.

Major USB code and data upgrades/refactors. The USB changes prepare inxi for USB
4, and adds lanes and Si/IEC speeds to the report. It is important to determine
what USB mode you are running in with 3.x and 4. These changes conform more
closely to how the USB consortium wants USB speeds refered to.

With more robust USB data, this data now appears in a similar form as pcie: data
for Devices, -A, -E, -G, -N, and for -D drives, as usb: plus rev, speed, lanes,
mode, with the -xx/-a options, like pcie. This has been a long standing
oversight and weakness of inxi USB and Device data, but now the two are fully
integrated, including for drives, which was quite tricky to get working.

Added netpkg and Zenwalk support to packages and repos. Also added repos support
for sbopkg and slpkg, and updated package tools for Slackware.

And more distros added to system base feature, and a few more for main ID.

Improved --recommends report quite a bit, now it's more granular for missing
packages and package manager reports, and also fixed a long standing missing
current shell + version issue. Added the final package manager type, pkgtool
(Slackware), that will be supported, which makes for 4, which is enough. Note
that other package managers can be added following the documentation
instructions for packagers, but this is enough for out of the box pm handling.

Fixed a long standing oddity with how free / /proc/meminfo report MemTotal vs
the actual physical RAM. I believe this issue also showed with GPU assigned RAM,
but now for all but short form, shows Memory/RAM: available: ... used: ...

--------------------------------------------------------------------------------
SPECIAL THANKS:

1. To the Slackware people at linuxquestions.org forums, who helped, again, on
this audio feature, even finding current or not too old systems that use some of
the new / old audio servers (EsoundD) running in the wild, which I never
expected to see. And also for exposing some weak spots in the USB advanced
logic, and helping with the sbopkg and slpkg repo logic and tools reports.

2. To the Manjaro forum users, for providing cases that show where inxi can be
improved. The audio server/api issue, the current USB 3/4 upgrade, were
initiated by threads pointing to things that could be improved in inxi. So I
guess the real thanks are for using inxi enough to trigger cases that show where
it's weak or can be better. Note that this requires that I follow roughly their
forums, however I only look at threads that seem like they might be of general
interest, or which suggest a possible weak spot in inxi, and I don't follow them
consistently. More reliable is to file github issues, since I will always see
those.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. DesktopData: at one point, BunsenLabs Debian OpenBox had XDG_CURRENT_DESKTOP
set to XFCE, which it isn't, but inxi can't work around such hacks, plus I don't
even know if Bunsen is around anymore anyway.

2. DesktopData: CODE 1 reminds us that the time to depend on x tools like xprop
for anything re desktop/wm detections is fast drawing to a close, true Wayland
will not have xprop, unless it's running on xwayland, which is not something
that should be relied on. Maybe recheck Moksha/Enlightenment which depend on
xprop for version detection.

The list of xprop detected wm/desktops in get_env_xprop_misc_data() is almost
all X only wm/desktops, so those should be safe unless one of them decides to
work on a wayland comositor.

3. BSD: ongoing weaknesses in BSD data sources make maintaining feature parity
impossible, but I am trying to get the BSD data as clean and consistent as
possible. I wish this were not the case, but the fact is, /sys is expanding and
creating excellent and reliable data sources with every major Linux kernel
update, and so far nothing comparable has appeared in the BSDs. This is just
reality, it's not a condemnation, but something like the /proc then /sys file
systems are an excellent idea, well worth emulating.

4. For the RAM available/total clarification, there's a slight issue because
free/meminfo show MemAvailable as Free for use RAM, but dmesg shows available
meaning what was available to the system during boot, minus the reserved
percentage. Since we needed one term, available to System offers the closest
in terms of technical precision without being too verbose. Technically available
in this context means: total physical minus 'kernel code' minus 'reserved'.

--------------------------------------------------------------------------------
BUGS:

1. CheckRecommends: See Fix 6b, more or less a bug, but really just a fix.

2. AUDIO: for USB devices, put extra data into row 0, no matter which row the
USB device is. This led to the extra data for USB being assigned to the wrong
row. Sigh.

3. OptionsHandler: When show{'ram'} was set, for bsd, set use{'bsd-raid'}, which
makes both show raid and ram fail for BSD. Oops. User mode RAM data only seen in
OpenBSD so far. This made loading $dboot{'ram'} fail, and any raid as well,
sigh, unless -m was also tripped.

--------------------------------------------------------------------------------
FIXES:

1. DistroData: typo for Arch base: was ctios, was supposed to be ctlos.

2a. DesktopData: found case where xprop -root not present (Void Linux), so xfce
test failed. Split to new function dedicated to xfce detection that doesn't use
xprop data. Also, XFCE is working on their Wayland version, which would in
theory not even have xprop by default.

Also, the base version number test for xfce depended on xprop, but
xprop doesn't even have that xfce version data anymore, so just checking if
xfce(4|5|)-panel exist and assigning primary version based on that test.

2b. DesktopData: Also see See CODE 1a,1b for further xprop and test fixes that
could have led to false positive or negative test conditions for the items that
used xprop tests. These tests are all xprop agnostic now, if it's there, they
will use it, if not, do the best they can.

3. PackageData: fixed legacy dpkg-query, old version did not support -f shortcut
for --showformat. This made dpkg package listing fail.

4a. GRAPHICS: Added legacy XFree86.0.log to X log path detection, that was an
oversight. Also added legacy module syntax _drv.o (not _drv.so). This gets X
driver data now for very old systems.

4b. GRAPHICS: fixed corner case where no x driver data, running as root, was not
supposed to show 'note: X driver n/a' message, that was a holdover from before
driver output was cleaned up and driver: N/A shows when no drivers at all found.
Just forgot to remove it when doing recent updates in the driver section, maybe?

5. REPOS/PackageData: For netpkg Zenwalk Slackware systems, showed only slackpkg
repo data, empty, and showed the Slackware pm, not netpkg for pm. See
Enhancements 5, 6.

6. REPOS: removed slapt_get file /etc/slapt-get/pubring.kbx, that's not a repo
file. Thanks chrisreturn for pointing that out.

7a. CheckRecommends: See also CODE 6. Fixed case where > 1 package manager is
detected on system, now lists them one by one for detected, and shows package
install options as well. Before only picked first detected, which could lead
to wrong results for Missing Package lists.

7b. CheckRecommends: Fixed glitch, forgot to update the current shell/version
when ShellData was refactored, this led to no current shell + version showing
up in recommends core tools report.

8. RAM: fixed speed_mapper string match to allow for older syntaxes. This is as
far as known OpenBSD only, from dboot data. Matches then converts PC2700 to
PC-2700 which then allows for mapping.

9. RAM/PROCESSES/INFO/SHORT: Finally tracked down a long time oddity, where for
example:
 RAM: total: 31.28 GiB
does not match 32 GiB physical installed. This is because that is the total
available after kernel and system reserved RAM is deducted, and in some cases,
GPU allocated RAM. There are also corner cases where the listed amount can be
less due to physical RAM damage, but that's uncommon.

Added explanation of why it's different, and what available is referring to in
man -m/--memory.

Changed -m, -tm to show:

System RAM: available: 31.28 GiB used 26.23 GiB (83.9%)

and -I to show:

Memory: available: 31.28 GiB used 26.23 GiB (83.9%)

You can get the 'reserved' and 'kernel code' data from dmesg, but since Debian
made that root/sudo tool, can't count on being able to parse that out of dmesg,
plus you can never count no dmesg anyway since it can get overwritten by kernel
oops or wonky device etc. inxi doesn't use dmesg data for Linux for this reason.

... [    0.000000] Memory: 32784756K/33435864K available (10252K kernel code,
1243K rwdata, 3324K rodata, 1584K init, 2280K bss, 651108K reserved, 0K
cma-reserved)

Also removed Raspberry Pi video RAM added back in to total now that it's clear
it's what is available. This may also make systems with GPU using system RAM
more correct.

9. SENSORS: sensors /sys tried to create concatenated string with $unit $value
but these are not necessarily defined, that needed to be protected with defined
tests.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1a. AUDIO: JACK: added helper nsmd (new session manager), and its recommended
gui agordejo. That's the drop in replacement for non-session-manager, the dev of
which apparently lost interest in that project. But the ID method will work fine
for for either, since both ran as nsmd.

1b. AUDIO: PULSE: added pulseaudio-alsa plugin support for helpers. This is like
pipewire-alsa plugin, just alsa config file. Only seen in Arch Linux so far, but
if others use similar paths for the glob pattern, they will also work fine.

Also added pulseaudio-esound-compat plugin, which is easier to detect with
/usr/bin/esdcompat.

Also added paman, pulseaudio manager.

1c. AUDIO: ESOUND,ARTS: added legacy esd (EsounD aka: Enlightened Sound Daemon)
and aRts sound server support, with basic help/tools. These are quite old, but
are still occasionally seen in the wild on newer systems, surprisingly enough.

1d. AUDIO: ALSA: added alsactl to alsa tools. Missed that one, it's an /sbin
type utility.

1e. AUDIO: ALSA: First try at ALSA compiled in but inactive report,  previously
depended on active only state of the API. Now uses compiled in SND_ kernel
switch using the /boot/config-[kernel] file, which is a big expensive parse but
only will activate on Linux kernels with no /proc/asound present. This fallback
fails if kernel config file not present: /boot/config-$(uname -r).

1f. AUDIO: OSS: added tool ossctl.

1g. AUDIO: NAS: added helper: audiooss which is an OSS compat layer.

2a. DistroData: added Arch base distros: ArchEX, Bridge Linux, Condres OS,
Feliz, LiriOS, Magpie, Namib, Porteus, RevengeOS, SalientOS, VeltOS.

None of these are verified. Some don't exist anymore.
Source: https://www.slant.co/topics/7603/~arch-linux-based-distributions

2b. DistroData: added ubuntu lunar 23-4 release id.

2c. DistroData: added porteux, added porteux, zenwalk to slackware systembase

3. DesktopData/GRAPHICS: added Smithay Wayland compositor. Not verified.

4a. UsbData/UsbItem: added USB lanes (-Jxx) and mode (-Ja), to add more useful
data about USB revision and mode names the USB group has created. Otherwise it's
too difficult to try to explain it. Note that -Jxx lanes follows other inxi
items that show PCIe lanes as an -xx item to try to keep it consistent.

This also consolidates the bsd and linux data sources, see CODE 5.

Note modes and lanes are Linux only because the revision number, lanes, and
speed used to determine mode are only natively available in Linux as actual
internal data values. If this changes BSD support will be added in the future.

The BSD rev and speed data is synthesized completely by inxi using some string
values, and thus is not reliable, which means that pretending inxi can get this
granular with data that is not coming directly from the system itself is
probably not a good idea.

Following wikipedia mode names: https://en.wikipedia.org/wiki/USB4

These are the known possible combinations:
rev: 1.0 mode: 1.0 lanes: 1 speed: 1.5 Mbps
rev: 1.1 mode: 1.0 lanes: 1 speed: 1.5 Mbps
rev: 1.1 mode: 1.1 lanes: 1 speed: 12 Mbps
rev: 2.0 mode: 1.0 lanes: 1 speed: 1.5 Mbps
rev: 2.0 mode: 1.1 lanes: 1 speed: 12 Mbps
rev: 2.0 mode: 2.0 lanes: 1 speed: 480 Mbps
rev: 2.1 mode: 2.0 lanes: 1 speed: 480 Mbps
rev: 3.0 mode: 3.2 gen-1x1 lanes: 1 speed:  5 Gbps
rev: 3.0 mode: 3.2 gen-1x2 lanes: 2 speed: 10 Gbps
rev: 3.1 mode: 3.2 gen-1x1 lanes: 1 speed:  5 Gbps
rev: 3.1 mode: 3.2 gen-1x2 lanes: 2 speed: 10 Gbps
rev: 3.1 mode: 3.2 gen-2x2 lanes: 2 speed: 20 Gbps [seen this case]
rev: 3.2 mode: 3.2 gen-1x1 lanes: 1 speed:  5 Gbps [wrong rev: seen this case]
rev: 3.2 mode: 3.2 gen-1x2 lanes: 2 speed: 10 Gbps [wrong rev: possible case]
rev: 3.2 mode: 3.2 gen-2x1 lanes: 1 speed: 10 Gbps
rev: 3.2 mode: 3.2 gen-2x2 lanes: 2 speed: 20 Gbps
rev: 3.2 mode: 4-v1 gen-3x2 lanes: 2 speed: 40 Gbps [not seen, but possible]
rev: 4 mode: 4-v1 gen-2x1 lanes; 1 speed: 10 Gbps
rev: 4 mode: 4-v1 gen-2x2 lanes: 2 speed: 20 Gbps
rev: 4 mode: 4-v1 gen-3x1 lanes: 1 speed: 20 Gbps
rev: 4 mode: 4-v2 gen-3x2 lanes: 2 speed: 40 Gbps
rev: 4 mode: 4-v2 gen-4x1 lanes: 1 speed: 40 Gbps
rev: 4 mode: 4-v2 gen-4x2 lanes: 2 speed: 80 Gbps
rev: 4 mode: 4-v2 gen-4x3-asymmetric lanes: 3 up, 1 down speed:120 Gbps

I believe 120Gbps takes the 2 lanes of tx/rx and converts 2 rx lanes to tx so
the entire lane is dedicated to transmit. and the third lane is dedicated to rx.

Includes error message for unknown usb 3/4 rev/speed match combos. These can be
bad hardware self reporting or unknown other issues.

4b. USB: Added Si/IEC speeds (base 2, base 10). -Ja triggers extra IEC, base 2
Bytes (xxx [MG]iB/s). -Jx triggers basic standard Si xxx [MG]b/s base 10 bits.

5a. PackageData: added netpkg as package tool. This stores data in same location
as slackpkg, but assume if exists directory /var/netpkg, then the system is
using netpkg as pm, not slackpkg.

5b. PackageData: added Slackware sbopkg, sboui as tools for pkgtool and netpkg.

6a. REPOS: added netpkg (Zenwalk Slackware based pm) repo report.

6b. REPOS: added sbopkg basic repo report. This handles both value syntax types,
as well as the ability of /root config file to overwrite /etc config repo.

6c. REPOS: added slpkg repo report. This handles their old and newer syntax.

7a. CheckRecommends: For Slackware users, added pkgtool missing package name,
also will use netpkg so hopefully Zenwalk uses same package names.

7b. CheckRecommends: Added radeon to kernel modules checks.

8. AUDIO/BLUETOOTH/DRIVES/GRAPHICS/NETWORK: For USB, -[ADEGN]xx adds rev, speed,
lanes. -[ADEGN]a adds mode.

9. RAM: Updated RAM PC DDR in speed_mapper(), which is as far as I know only
used by OpenBSD, which allows for MT/s speeds as non-root user, which is nice.
That list hadn't been updated in a long time, so filled out DDR 1-5 PCx-yyyy
ids.

--------------------------------------------------------------------------------
CHANGES:

1a. USB: For -Jxy1, speed is now a child of rev: parent. This goes along with
mode: and lanes: being children of rev:. This follows how USB consortium wants
to refer to USB revisions now: by speed, lanes, and modes, the latter being the
technical term, the speed being the marketing term.

1b. USB: If no speed data found, show N/A. This should almost never happen
except for very old Linux and rarely with BSD.

1c. USB: Device type is lower cased except for abbreviations (type-C, HID). This
makes it more consistent as a value.

1d. USB: Show basic Si speed with -Jx, and adds new IEC speed with -Ja.

2. CheckRecommends: See ENHANCEMENT, CODE 6. Now showing row by row package
managers and missing packages, by package manager(s).

3. DRIVES: Changed long standing redundant use of 'type':
type: USB ... type: HDD
to:
type: USB ... tech: HDD
'tech:' means the technology used, HDD, SDD, and if we can ever figure out how
to detect it, Hybrid Hard Drive (HHD),

4. AUDIO/BLUETOOTH/DRIVES/GRAPHIC/NETWORK: moved 'type: USB' pair to after
driver for -A/-E/-G/-N, which allows it to be the parent of the new USB data
block. Negative is it moves it a bit further back in the line.

For Drives, it moves it from after /dev.. maj-min to after block-size, However,
with -D/-Dx, it's last in the line, which is nice. This is the only way I could
find to make it more consistent across all possible USB device/drive type
reports.

5. INFO/RAM/PROCESSES: Changed -I:

Memory: [total] used:
to:
Memory: available: [total] used:

Changed -tm/-m to be consistent:

Memory: RAM: total: .. used..
to:
Memory: System RAM: available: ... used:..

This corrects a long standing inaccuracy where MemTotal is not actually the full
system RAM, but is the RAM minus reserved stuff for system and kernel, and GPU
memory in some cases.

--------------------------------------------------------------------------------
DOCUMENTATION:

1a. DOCS: docs/inxi-audio.txt: ongoing updates, adding more information, more
on helpers, detection methods, etc.

1b. DOCS: New: docs/inxi-usb.txt: USB info, update, added more, a work in
progress.

1c. DOCS: docs/inxi-custom-recommends.txt: name in inxi comment did not match,
and updated to new comment cleaned up syntax in example. Fixed inxi comment file
name.

1d. DOCS: New: docs/inxi-unit-handling.txt: To document how inxi handles
size/speed data internally, and ideally, to help integrate all those methods
into one big tool one day, not spread across many area.

1e. DOCS: New: docs/inxi-repo-package-manager.txt: To start to document arcana
and methods and commands and outputs for package managers. Since this is a late
start, will take time to complete, but better late than never.

2a. MAN/OPTIONS: updated for USB -Jx, -Jxx, -Ja, adding lanes, mode, iec speed
items.

2b. MAN/OPTIONS: fixed error which had USB speed as -Jxxx instead of -Jxx. Also
then changed speed to be -Jx.

2c. MAN/OPTIONS: updated for repos for SBOPKG, SBOUI, SLPKG, and added
SLAPT_GET, I'd forgotten that one.

2d. MAN/OPTIONS: updated for -xx[ADEGN] USB rev, speed, lanes; for -a[ADEGN]
updated for USB mode.

2e. MAN/OPTIONS: updated for memory available/used changed.

3. MAN: fixed some inconsistent use of short/long form display in extra data
options.

--------------------------------------------------------------------------------
CODE:

1a. DesktopData: New function for xfce only detections, turns out xprop is not
necessarily installed, Void Linux for example had failed ID. Old version
required xprop to do the tests, which was not robust and failed in this case.
Function: get_env_xfce_data(). Also made xprop data optional for all the
xxx_xprop_data desktop tests, not just some of them. This will forward proof
the desktops

1b. DesktopData: Fixed bad parens in test cases, was not correctly organized.
if (a || b || (c || d) && e)
was supposed to be:
if (a || b || ((c || d) && e))
Odd how those types of glitches creep in, one fix is also to just make the lines
break more reasonably so the conditions are easier to parse visually.

2a. DEBUGGER: Added /etc/X11/XF86Config-4 xorg conf file to debugger.

2b. DEBUGGER: audio_data(): added audio server versions to cover all known ones.

3. MemoryData: changed all $memory to array references, got rid of split :
separators, which were clearly legacy items leftover from bash/gawk days. Also
changed MemoryData::get('splits') to get('full') to reflect this change.

This change should be transparent though it may introduce corner case undefined
value situation but that should not happen since array values are defined first.

4. UsbData: Refactor of usb speed, rev, added lanes, mode. Refactored most of
the bsd/linux rev/speed logic, merged some of bsd speed/rev into the new
version_data() function, which loads all the data based on what is calling it.
This helps consolidate the logic across usb data sources.

5a. GLOBAL: made functions/methods use same comment syntax for args:
 args: 0:...; 1:...
always starting with 0, to match array index. Same syntax for return array index
values. In some cases simply note a variable is passed by ref:
 args: $value passed by reference.

5b. GLOBAL: made all sub/functions/methods follow the same spacing syntax. This
seems to be a good compromise for space/readability. Note that adding in these
new lines added about 400 lines to the total length, plus the line breaks that
were already there. Yes, inxi has a lot of sub routines! aka functions and
sometimes aka methods.

[empty line]
[comments]
sub [name] {

Packages/classes now also all follow the same spacing rules:

[empty line]
[comments]
{
package [name];
[empty line]
[comments]
sub [name] {
...
}
}

Internally, subs generally do not use any empty lines unless it makes sense to
do so for some specific reason.

5c: GLOBAL: made start of sub comments be upper case, I have a bad habit of
typing comments in lower case, easier to read if it's reads like a normal
sentence.

6. CheckRecommends: refactored entire items logic, set global hash for test
items. Made support > 1 detected package manager.

7. REPOS: cleaned up comments for package manager/repo blocks.

8. SENSORS: sensors_sys failed to reset to undefined $unit and $value, and also
failed to test if they were defined before using them in concatenation.

---
## [ofek/black](https://github.com/ofek/black)@[0019261abc...](https://github.com/ofek/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Monday 2023-05-08 05:03:45 by Richard Si

Update stable branch after publishing to PyPI (#3223)

We've decided to a) convert stable back into a branch and b) to update
it immediately as part of the release process. We may as well automate
it. And about going back to a branch ...

Git tags are not the right tool, at all[^1]. They come with the
expectation that they will never change. Things will not work as
expected if they do change, doubly so if they change regularly. Once
you pull stable from the remote and it's copied in your local
repository, no matter how many times you run git pull you'll never see
it get updated automatically. Your only recourse is to delete the tag
via `git tag -d stable` before pulling.

This gets annoying really quickly since stable is supposed to be the
solution for folks "who want to move along as Black developers deem
the newest version reliable."[^2] See this comment for how this impacts
users using our Vim plugin[^3]. It also affects us developers[^4]. If
you have stable locally, once we cut a new release and update the stable
tag, a simple `git pull` / `git fetch` will not pull down the updated
stable tag. Unless you remember to delete stable before pulling, stable
will become stale and useless.

You can argue this is a good thing ("people should explicitly opt into
updating stable"), but IMO it does not match user expectations nor
developer expectations[^5]. Especially since not all our integrations
that use stable are bound by this security measure, for example our
GitHub Action (since it does a clean fetch of the repository every time
it's used). I believe consistency would be good here.

Finally, ever since we switched to a tag, we've been facing issues with
ReadTheDocs not picking up updates to stable unless we force a rebuild.
The initial rebuild on the stable update just pulls the commit the tag
previously pointed to. I'm not sure if switching back to a branch will
fix this, but I'd wager it will.

[^1]: https://git-scm.com/docs/git-tag#_on_re_tagging

[^2]: https://black.readthedocs.io/en/stable/contributing/release_process.html#moving-the-stable-tag

[^3]: https://github.com/psf/black/issues/2503#issuecomment-1196357379

[^4]: In fairness, most folks working on Black probably don't use the
      `stable` ref anyway, especially us maintainers who'd know what is
      the latest version by heart, but it'd still be nice to make it
      usable for local dev though.

[^5]: Also what benefit does a `stable` ref have over explicit version
      tags like `22.6.0`? If you're going to opt into some odd pin
      mechanism, might as well use explicit version tags for clarity
      and consistency.

---
## [JoysKo/HYBRID_CAF_kernel](https://github.com/JoysKo/HYBRID_CAF_kernel)@[18a3e41532...](https://github.com/JoysKo/HYBRID_CAF_kernel/commit/18a3e41532c11b2b94a30ec1c020a54a415ff374)
#### Monday 2023-05-08 05:26:56 by Douglas Anderson

serial: core: Allow processing sysrq at port unlock time

[ Upstream commit d6e1935819db0c91ce4a5af82466f3ab50d17346 ]

Right now serial drivers process sysrq keys deep in their character
receiving code.  This means that they've already grabbed their
port->lock spinlock.  This can end up getting in the way if we've go
to do serial stuff (especially kgdb) in response to the sysrq.

Serial drivers have various hacks in them to handle this.  Looking at
'8250_port.c' you can see that the console_write() skips locking if
we're in the sysrq handler.  Looking at 'msm_serial.c' you can see
that the port lock is dropped around uart_handle_sysrq_char().

It turns out that these hacks aren't exactly perfect.  If you have
lockdep turned on and use something like the 8250_port hack you'll get
a splat that looks like:

  WARNING: possible circular locking dependency detected
  [...] is trying to acquire lock:
  ... (console_owner){-.-.}, at: console_unlock+0x2e0/0x5e4

  but task is already holding lock:
  ... (&port_lock_key){-.-.}, at: serial8250_handle_irq+0x30/0xe4

  which lock already depends on the new lock.

  the existing dependency chain (in reverse order) is:

  -> #1 (&port_lock_key){-.-.}:
         _raw_spin_lock_irqsave+0x58/0x70
         serial8250_console_write+0xa8/0x250
         univ8250_console_write+0x40/0x4c
         console_unlock+0x528/0x5e4
         register_console+0x2c4/0x3b0
         uart_add_one_port+0x350/0x478
         serial8250_register_8250_port+0x350/0x3a8
         dw8250_probe+0x67c/0x754
         platform_drv_probe+0x58/0xa4
         really_probe+0x150/0x294
         driver_probe_device+0xac/0xe8
         __driver_attach+0x98/0xd0
         bus_for_each_dev+0x84/0xc8
         driver_attach+0x2c/0x34
         bus_add_driver+0xf0/0x1ec
         driver_register+0xb4/0x100
         __platform_driver_register+0x60/0x6c
         dw8250_platform_driver_init+0x20/0x28
	 ...

  -> #0 (console_owner){-.-.}:
         lock_acquire+0x1e8/0x214
         console_unlock+0x35c/0x5e4
         vprintk_emit+0x230/0x274
         vprintk_default+0x7c/0x84
         vprintk_func+0x190/0x1bc
         printk+0x80/0xa0
         __handle_sysrq+0x104/0x21c
         handle_sysrq+0x30/0x3c
         serial8250_read_char+0x15c/0x18c
         serial8250_rx_chars+0x34/0x74
         serial8250_handle_irq+0x9c/0xe4
         dw8250_handle_irq+0x98/0xcc
         serial8250_interrupt+0x50/0xe8
         ...

  other info that might help us debug this:

   Possible unsafe locking scenario:

         CPU0                    CPU1
         ----                    ----
    lock(&port_lock_key);
                                 lock(console_owner);
                                 lock(&port_lock_key);
    lock(console_owner);

   *** DEADLOCK ***

The hack used in 'msm_serial.c' doesn't cause the above splats but it
seems a bit ugly to unlock / lock our spinlock deep in our irq
handler.

It seems like we could defer processing the sysrq until the end of the
interrupt handler right after we've unlocked the port.  With this
scheme if a whole batch of sysrq characters comes in one irq then we
won't handle them all, but that seems like it should be a fine
compromise.

Signed-off-by: Douglas Anderson <dianders@chromium.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [axietheaxolotl/tgstation](https://github.com/axietheaxolotl/tgstation)@[c8c977989a...](https://github.com/axietheaxolotl/tgstation/commit/c8c977989a793cfe1e24eb6aa4350e14335025e5)
#### Monday 2023-05-08 06:01:26 by John Willard

Mimes can no longer write without breaking their vow. (#74674)

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

---
## [Vallat/Skyrat-tg](https://github.com/Vallat/Skyrat-tg)@[39ebf7c2af...](https://github.com/Vallat/Skyrat-tg/commit/39ebf7c2af41309fa4d5206f77cc4d261f47dfb7)
#### Monday 2023-05-08 06:44:25 by SkyratBot

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
## [soon14/evals](https://github.com/soon14/evals)@[ab5f7b2a89...](https://github.com/soon14/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Monday 2023-05-08 06:56:59 by oscar-king

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
## [soon14/evals](https://github.com/soon14/evals)@[b170a21cf3...](https://github.com/soon14/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Monday 2023-05-08 06:56:59 by Sam Ennis

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
## [soon14/evals](https://github.com/soon14/evals)@[b5da073c21...](https://github.com/soon14/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Monday 2023-05-08 06:56:59 by somerandomguyontheweb

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
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[ae7595b8e1...](https://github.com/PKRoma/Terminal/commit/ae7595b8e13d4764f4db7b4060eaf57d1b4ee82e)
#### Monday 2023-05-08 07:45:25 by Mike Griese

Add `til::property` and other winrt helpers (#15029)

## Summary of the Pull Request

This was a fever dream I had last July. What if, instead of `WINRT_PROPERTY` magic macros everywhere, we had actual templated versions you could debug into. 

So instead of 

```c++
WINRT_PROPERTY(bool, Deleted, false);
WINRT_PROPERTY(OriginTag, Origin, OriginTag::None);
WINRT_PROPERTY(guid, Updates);
```

you'd do 

```c++
til::property<bool> Deleted{ false };
til::property<OriginTag> Origin{ OriginTag::None };
til::property<guid> Updates;
```

.... and then I just kinda kept doing that. So I did that for `til::event`.

**AND THEN LAST WEEK**

Raymond Chen was like: ["this is a good idea"](https://devblogs.microsoft.com/oldnewthing/20230317-00/?p=107946)

So here it is. 

## Validation Steps Performed
Added some simple tests.

Co-authored-by: Leonard Hecker <lhecker@microsoft.com>

---
## [LewinReimann/ChampionCardGame](https://github.com/LewinReimann/ChampionCardGame)@[1a2726bf4b...](https://github.com/LewinReimann/ChampionCardGame/commit/1a2726bf4bb3d34f641e5e75acac0dbc1fb6dd63)
#### Monday 2023-05-08 08:39:26 by Lewin Reimann

First Iterations of 3D Dice WORKING!!! YEEEEAAA

Took me quiete some focking  time. But hell yeah here we are. Rolls are working. Need to adjust them a bit so that they are stopped earlier and dont roll around like stupid. Like after 2 seconds increasing their Gravity Mass or Drag.

---
## [jni/napari](https://github.com/jni/napari)@[3ec4be1ae8...](https://github.com/jni/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Monday 2023-05-08 09:43:47 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [Segrain/cmss13](https://github.com/Segrain/cmss13)@[df247be72a...](https://github.com/Segrain/cmss13/commit/df247be72a87e69e8841ad754633329c87a7883d)
#### Monday 2023-05-08 10:17:10 by brian

reduces platform and handrail projectile coverage significantly (#2995)

# About the pull request

Does exactly what the title implies: reduces platform and handrail
projectile coverage significantly.
Platforms 60% -> 0%
Handrails 35% -> 10%

# Explain why it's good for the game

When a platform and handrail are combined, that totals at a 95% chance
of blocking a bullet passing through that tile. Platform corners also
catch bullets. That's some hogwash if you ask me. It makes areas like
Sorokyne's Mining platform entrance nearly un-defendable for marines
since they can't shoot past what is effectively an invisible bullet
wall. When I made Sorokyne, this was not the intent of the area. New
Varadero has similar problems.

You may ask, why not change those areas instead? My answer: Sod off,
they look awesome, and I don't want to code a check on projectiles to
determine if you're shooting 'up' at a ledge which would be the logical
simulationist fix. Also handrails aren't supposed to block bullets
unless they're reinforced (not that anyone uses that mechanic though).
How do I know this? I willed this mechanic into existence for Strata
with shitcode. I was there when it was written.

Both xenos that spit and marines that shoot will benefit from this
change.

Oh yeah and corners won't catch bullets anymore.

# Changelog

:cl: Triiodine
balance: Reduced projectile coverage of platforms from 60% to 0%.
balance: Reduced projectile coverage on handrail types from 35% to 10%.
Sandstone handrails are unaffected and remain at 35% projectile
coverage.
balance: Sandstone handrails can no longer be reinforced.
/:cl:

---------

Co-authored-by: Chadwick B. Dunlop <fake@fake.mail>

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[a59cd4fbe7...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/a59cd4fbe70c772a7124d18bc79effebd80b4d7b)
#### Monday 2023-05-08 10:40:48 by Ruchit

Revert "(note to self) dont pick this ye dumb idiot its only for wip branch so you can test shit better k bye"

This reverts commit cddd8e56efa631771040ab68dcb6e5a84b18a8a3.

---
## [TheRealJake12/Kade-Engine-Community](https://github.com/TheRealJake12/Kade-Engine-Community)@[12429488b6...](https://github.com/TheRealJake12/Kade-Engine-Community/commit/12429488b61cf282ac754dc8ab368b2ad90f88f8)
#### Monday 2023-05-08 11:44:33 by TheRealJake_12

sections

THIS HAS BEEN A PAIN IN THE ASS FOR FUCKS SAKE STEPMANIA SONGS BROKE
SONGS WITH NOTETYPES BROKE
I FUCKING HATE THIS SO DAMN MUCH THE SECTIONS BROKE EVERYTHING CHARTS WERE TOO BROKEN TO PLAY. THE NOTES WERE FUCKY
I love performance :)

---
## [facebookincubator/antlir](https://github.com/facebookincubator/antlir)@[2a04669533...](https://github.com/facebookincubator/antlir/commit/2a046695334a3459d3ff11919b38981274d72a2b)
#### Monday 2023-05-08 12:04:09 by Vinnie Magro

[antlir2][depgraph] separate requirements from ordering

Summary:
Refactor `Requirement` to be separate from ordering. Most of the time, a
`Requirement` does in fact imply ordering, but there are a few exceptions where
it does not, and I expect that list to grow longer as there are more high-level
features added to the antlir2 api (thinking things like more systemd
functionality)

For an example that already exists:
- `user_add` requires that the user's `homedir` exists
- `ensure_dirs_exist` requires that the owner user exists
Boom: ordering cycle

Importantly though, `user_add` logically has a non-ordering dependency on the
existence of the `homedir`. `ensure_dirs_exist(homedir)` has a strict ordering
requirement on the user existing, otherwise we can't `chown`.
The cycle can be broken by saying that `user_add`'s dependency on the `homedir`
is simply a requirement, but does not imply ordering. This will allow the
`user_add` feature to create the user, then the `ensure_dirs_exist` to come
along and create the directory.

But wait, why is this not an issue in antlir1? antlir1 allows you to create a
user without asserting any property about the home directory, it's perfectly
valid as far as antlir1 is concerned to create a user with a non-existent
homedir. We can do better in antlir2 and this occasionally leads to
pain-points when migrating layers to a stricter api.
Funny enough, part of antlir1's lax behavior around homedirs has caused a huge
pain with auditing requirements before ;)

Test Plan:
```
❯ buck2 test fbcode//antlir/antlir2/antlir2_depgraph/tests:
Buck UI: https://www.internalfb.com/buck2/d484b17c-1cec-496f-a1de-de955f6c0d8a
Test UI: https://www.internalfb.com/intern/testinfra/testrun/8444249454798646
RE: reSessionID-6655adce-0df7-447c-8f71-d47a04a2ef70  Up: 3.6 MiB  Down: 0 B
Jobs completed: 44. Time elapsed: 24.9s. Cache hits: 0%. Commands: 19 (cached: 0, remote: 0, local: 19)
Tests finished: Pass 17. Fail 0. Fatal 0. Skip 0. Build failure 0
```

Before the code implementation, the new test failed as expected
`fbcode//antlir/antlir2/antlir2_depgraph/tests:unordered-requirements`
```
cycle in dependency graph:
  Feature { label: Label("fbcode//antlir/antlir2/antlir2_depgraph/tests:unordered-requirements--features"), data: EnsureDirExists(EnsureDirExists { group: GroupName("antlir"), dir: PathInLayer("/home/antlir"), mode: Mode(493), user: UserName("antlir") }) }
  Feature { label: Label("fbcode//antlir/antlir2/antlir2_depgraph/tests:unordered-requirements--features"), data: User(User { name: UserName("antlir"), uid: None, primary_group: GroupName("antlir"), supplementary_groups: [], home_dir: PathInLayer("/home/antlir"), shell: PathInLayer("/usr/sbin/nologin"), comment: None }) }
```

Reviewed By: epilatow

Differential Revision: D45568979

fbshipit-source-id: 52cee5528fd70d8667b899cac8dfa600e5b033b1

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[ad302f209f...](https://github.com/MTandi/tgstation/commit/ad302f209f4fc0b739c6eea8e6be92da05e2742c)
#### Monday 2023-05-08 12:50:34 by Zytolg

Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] (#73502)

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
identity. Maybe it's not perfect, but I've been inspired by @MMMiracles
own performance with Tramstation to keep working on Birdshot and
updating it with better and improved faculties. For now, though the
station is in a playable state, and that means I'm making a PR. If I had
to borrow the words of the good MMM, I would call this **Birdshot:
Season 0**


![BirdSHOTFULL2-26-S](https://user-images.githubusercontent.com/33048583/221432760-27af1889-d2d0-4861-9435-df4258525fae.png)



See the image in more detail here: https://imgur.com/iT5Vi8k



## Why It's Good For The Game

We've been with the same 5 maps for a while now. @san7890 jokingly said
that I could sacrifice Metastation back in November if I remade Birdboat
but modern. Obviously that wasn't going to happen, yet I was spurred on
by the idea. When I began this in earnest early this January, @EOBGames
said that a Birdboat sized map would replace Kilostation in the
rotation. Interestingly we're not a small map anymore so I honestly have
no clue where this goes. Maybe that ephemeral 6th map slot that's been
rumored.

What I can say, is that Birdshot is wholly unlike anything else that is
currently in rotation. It's got an engineering section that feels way
too small for a station of that size, almost evocative of Cere. Cargo is
blessed with a Boutique that makes use of @Fikou's new mannequin dolls.
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

Co-authored-by: Zytolg <theoriginaldash@gmail,com>

---
## [32th-System/deltarune_repainted](https://github.com/32th-System/deltarune_repainted)@[191a80635b...](https://github.com/32th-System/deltarune_repainted/commit/191a80635b30b9032c07bccb62cfd8e87eac5f88)
#### Monday 2023-05-08 14:28:12 by Fatfuck22

gromit mugs

[Gromit pours the tea in the cup, putting the bread in the toaster, pushing it down, then pushing the toaster away, then getting out of a chair, marking an X on the 12 from the calendar, then looking at a watch, then Wallace sleeps, then Gromit grabs the envelopes, shuffling it up, walking to the table with a train passing by, then sitting in a chair, unboxing an envelope, then opening and closing a music card, then opening a music card, hearing music, hearing a buzzer, saying, "Breakfast", pressing a button] Wallace: It's my turn for breakfast this morning, Gromit. I'd like a three-minute egg... [Gromit pulls a lever] Wallace: Whoa! Steady on! [puts his pants on] Gromit! [sits on his chair] [the hands put sleeves on, raising his hands, putting on a shirt, popping his head out] Wallace: Ha-ha! [Gromit presses a button, shooting jam out, then the toaster pops out, putting jam on it, landing on a plate, eating the toast] Wallace: Well, that went as well as could be expected, didn't it? Though I might have to make a small adjustment to the drop. A touch painful on re-entry. [puts toast in his mouth] Cracking toast, Gromit. [Gromit continues looking at a newspaper] Wallace: [swallows his toast] Any post, was there, perchance? [Gromit takes the envelopes to Wallace] Wallace: Oh, dear, a bit steep! Oh, my goodness! Well, I'll be... They're all bills. Oh, dear, oh, dear! We shall have to economise, Gromit. I'll have to let that room out. Oh, dear! [takes a picture frame, dialing the locker, opening a locker, taking a piggybank, closing a locker, putting the picture frame back up, sitting back down, taking the cork out, shaking the coins out] Oh. Just look at that. I'm down to my last few coppers. And those presents weren't cheap, either. Gasp! [Gromit looks at Wallace] Wallace: Well, Gromit, let's see what's on the 9:05, shall we? [hears a train tooting] Here she comes now. I wonder what this can be. Happy birthday, chuck! [takes a present to Gromit] [Gromit opens a present, looking at the leash and spikes] Wallace: I knew you'd like it. Here, let me help you. [puts spikes around his neck] You look like somebody owns you now. And that's only the first part. Come and look in here. [Gromit looks at the Techno Trousers, in a present, walking backwards to Gromit, then looking at the tag with an X, saying, "To Gromit Love Wallace"] Wallace: I think you'll find this present a valuable addition to our modern lifestyle![opens a present] They're Techno Trousers. Ex-NASA. Fantastic for walkies! All you do is attach the lead on here... [puts leash on Gromit] ...then program in. Walkies, 10 minutes, 20 minutes. Oops! [the Techno Trousers walk down]

---
## [Daniel98Kamau/Learning_Computers](https://github.com/Daniel98Kamau/Learning_Computers)@[a1186e24b0...](https://github.com/Daniel98Kamau/Learning_Computers/commit/a1186e24b01aa796fab0ac3179de2a1beb7ce06f)
#### Monday 2023-05-08 14:59:51 by Daniel K. Njoroge

Create README.txt

My journey into the computer world.

By the beginning of the year 2023, I was a computer dimwit per say. My computer literacy skills were most rudimentary and primitive. Having grown up in an African countryside where technological exposure till date is low, a desire to get into tech is tantamount to a wild goose chase. It calls for unmatched resilience and commitment to get a breakthrough.

Early this year, I met with an old friend ( We first met when I joined the high school where he was a student.), who is doing well in the field of tech. He had these mind-blowing idea of a project he wanted to roll-out. He explained in a nutshell what the process would look like. I listened keenly but at first thought I could not be of help, since I had no requisite skills.

My friend told me that it was not a prerequisite to have computer skills. The major requirement was to be committed to the course and be teachable. I took up the challenge to learn new skills and be productive in society. Three months now into this thrilling journey and I cannot find enough words to thank all my mentors. I am also open to collaborate with everyone with a similar mindset to continue scaling the heights.

The bigger picture.
I am striving to measure up to the purpose. It is in the public domain that knowledge is power. I am one very happy person for finally having found a purpose in life. I look forward to a point in time when I will be in a position to mentor other soul(s) to live a purposeful live and be that light at the end of their tunnels.

---
## [sebastiansuarez189/sebastiansuarez](https://github.com/sebastiansuarez189/sebastiansuarez)@[d7abef0784...](https://github.com/sebastiansuarez189/sebastiansuarez/commit/d7abef07848daf304e348b3a86a2b293a6934283)
#### Monday 2023-05-08 15:41:26 by sebastiansuarez189

Heads up! Good defense! Good defense! We're going downtown. Shut the hell up, you stupid mutt! What do you want? HDS, sir. How are you this afternoon? Alrighty. I have a package for you. It sounds broken. Most likely. I'll bet it was something nice. This is an insurance form. If you'll just sign here, here, and here... ...we'll get the rest of the forms to you soon. That's a lovely dog. - Do you mind if I pet him? - I don't give a rat's butt. Oh, brother! That's fine. I can finish the rest. You just have yourself a good day. Take care now. Bye-bye. Excuse me! HDS! HDS! Coming through! Got a package, people! Get away from the door. What's the matter with you? I said, get! Son of a b***h! That was a close one! Unfortunately... ...in every contest there must be a loser. Hungry, fellow? There you go. No problem. It gets flooded. We'll just wait a few seconds. Or we can try it now. Putz! Come on! Get out! Get out! Warning: Psycko are closer than they appear! Give me a push while you're back there. Alrighty, then! It's alive! It's alive! My little baby, come here. You missed Mommy, didn't you? Yes, you did. Did Daddy hurt you? I won't let him. No, I won't. He can keep the big TV, but he's not gonna hurt my baby, no he's not. Thank you, Mr. Ventura. How can I ever repay you? A reward would be good. There is some damage to my car, and I had to fill it with premium. Would you like for me to take your pants off instead? Gee! Let me think. Sure. People are real friendly around here. Ventura! Yes, Satan? I'm sorry, sir. You sounded like someone else. Never mind the wisecracks, Ventura. You owe me rent. Mr. Shickadance, I told you, you're my first priority. I'm on a very big case right now. Check this out. Look at that. That's a true albino pigeon. Some rich guy lost it. He's offering a $25,000 reward. As soon as I find this bird... ...you're paid. I heard animals in there. I heard them again this morning, scratching around. I never bring my work home with me. Oh, yeah? What's all this pet food for? Fiber. Wanna take a look inside? Come on! Come on! Go ahead. Snoop around! Well? Are you satisfied? Just don't let me catch you with an animal in here. That's all. All right. Take care, now. Bye-bye, then. Loser! Come to me, jungle friends. Roger, let me ask you one question. How in hell do you lose a 500-pound fish? What? I'm sorry, I was just going to say... ...that it's not a fish. It's a mammal. Thank you, Miss Jacques Cousteau. She didn't mean anything by that. I don't give a good about that fish! Fillet it and fast-food it if you want to! All I give about is winning the Super Bowl! My athletes have got to have their heads in the right place! Roger! You've been in this business a long time. You know how superstitious these players are. I have a quarterback that's put his socks on backwards since high school. I've got a linebacker that hasn't washed his jockey strap in two years... ...because he thinks flies are lucky. I want that fish on that field Super Bowl Sunday. Find the fish... ...or find new jobs! Why did it happen now, two weeks before the Super Bowl? I'll tell you, it's those animal-rights activists! Always out with their signs: "Animals were born free! Stop torturing Snowflake!" That fish lives better than they do. The police are checking into the animal- rights groups. Have they called back? No, but I wanted to tell you, when I lost my Cuddles... ...I hired a pet detective. A what? A pet detective. Thanks, Martha, but we better leave this to professionals. Well, actually, he was quite good. Pet detection is a very involved, highly scientific process. Like a glove! Mr. Ventura here to see you. Thanks, Martha. Hi, I'm Melissa Robinson. Pleasure to meet you. Any trouble getting in? No, the guy with the rubber glove was surprisingly gentle. Security's tight Super Bowl week. Why don't you have a seat? I'll get right to the point. Our mascot was stolen from his tank last night. Are you familiar with Snowflake? Negative. We got him from Miami. He's a rare bottle-nosed dolphin. This is a new trick he was going to do for the halftime show. Let's go. Blue 42, blue 42! Hut, hut! All right! Come on, let's go! Good boy! Would you like an ashtray? I don't smoke. It's a disgusting habit. The police came today. Apparently, the kidnappers came in through the back with a... Four-wheel-drive van, loaded from the rear. Roger, how you holding up? If I'm walking funny it's because I got two dozen reporters up my butt. They've been asking me about Snowflake all morning. Who's he? Roger Podacter, meet Ace Ventura. He's our pet detective. Nice to meet you. You came very highly recommended by Martha Mertz. Martha Mertz? Oh, yeah! Pekingese, lost in Highland Park area. She was half-dead when I found her. Is that the tank? Excuse me. - Cops drain it? - Yes, this morning. If I'm not back in five minutes... ...just wait longer. Captain's log, stardate 23.9, rounded off to the nearest decimal point. We've traveled back in time to save an ancient species from annihilation. So far... ...no signs of aquatic life, but I am going to find it. If I have to tear another black hole, I'm going to find it! I've got to, mister! Oh, great! I'll try to head them off. Ace, get out of the tank. I just can't do it, captain! I don't have the power! People! I said, get out of the tank now! For God's sake, Jim, I'm a doctor, not a pool man! Where's Snowflake? Snowflake is not available right now. Roger, I've been waiting all day. I got to get a shot of his new trick! What, is he sick? People, people! Lassie must be missing. Make any good collars lately? Or were they leashes? Homicide, Ventura. How are you gonna solve that one? Good question, Aguado! First, I'd establish a motive. The killer saw the size of the bug's dick and became insanely jealous. Then I'd lose 30 pounds porking his wife! Come on! Now, kiss and make up! Excuse me. I'd like to ask you a few questions. This is not the time, Ace. If Einhorn come down here and see me talking to you or your butt, I'm history. I can keep him under control. You have to tell me who's on the Snowflake case. I can't do nothing for you on that. My hands are tied. All right, that's it! Now it's my turn! Five minutes alone, that's all I need! Better look alive. Einhorn's on her way down. Come on, now. Ace, please. What's that matter? Afraid I'll make a stink? Come on! Aguado's working the case, all right? Aguado! Good call! We're just a little busy now... ...with murderers and burglaries and drug dealers. Things like that. A missing dolphin isn't exactly a high priority. Now you've pissed him off. - Would you give me a break? - I can't hold him much longer! My boss is coming! Okay, look. We ran a check with local animal-rights groups. We checked out the taxidermists and we already checked on van rentals. So far, nothing, nathin', nada. All right? Any unusual bets being made? Of course! This is Super Bowl! - What'd you find out about the tank? - Nothing. Tire tracks, an escape route. A guard didn't see anything. - That's it? - I swear. Now will you please get out of here before I get in trouble? Thank you for your cooperation. By the way, do you have a mint? Perhaps some Binaca? Holy testicle Tuesday! What the hell is he doing here? I came to confess. I was the second gunman on the grassy knoll. Spare me the routine. I know you're working the Snowflake case. May I suggest you yield to the experts on this one? We'll find the porpoise. Now I feel better. Of course, that might not do any good. Nobody's missing a porpoise. It's a dolphin that's been taken. The common harbor porpoise has an abrupt snout... ...while the bottle-nosed dolphin, or Tursiops truncatus... ...has an elongated beak, cone-shaped teeth and a serrated dorsal appendage. But I'm sure you already knew that. That's what turns me on about you. Your attention to detail. Listen, pet dick... ...how would you like me to make your life a living hell? Well, I'm not really ready for a relationship, Lois. But thank you for asking. Maybe I'll give you a call sometime. Your number still 911? Alrighty, then! Excuse me. Is Greg here? Thank you! What's the password? New England clam chowder. Is that the red or the white? I can never remember that! White? Hey, Woodstock! Hey, Saint Francis, how's it going? Super, thanks for asking. I hope you're having a lovely day. Do you? Don't I? So what are you up to? Just watching the fishies. You see those blips? That's a Norwegian whaling fleet. I'm sending them new directional coordinates. They'll find Jimmy Hoffa... ...before they find any whales. Gravy! So can you still tap into the aquatic supply stores in the area? Of course I can. Why? I wanna trace the sale of equipment... ...for transporting or housing a dolphin recently. Come on, I thought you had a challenge for me. All right, we got marine winch, sling, feeder fish, 20,000-gallon tank... Wait a minute. Look here. That's a lot of equipment for a civilian. Ronald Camp? The billionaire? Billionaire and rare-fish collector. Really? That is the face of the enemy. Always trying to get his greedy hands on endangered species. Hold on. Camp is connected with the dolphins? That subgenius gave them the land the stadium's built on. And look, he's throwing another "I'm the richest man in the universe" party. Looks like it's time for me to get myself a date. I'm really going out on a limb here. His social events are strictly A-list. The date started good, Chuck, but before we got to the party, she tensed up. If you do anything to embarrass me... What? Like this? Hi, Captain Stubing. How are Gopher and Doc? Permission to come aboard, sir. I'm sorry, ladies. Glad you could make it. Thank you. You look wonderful. And who is he, a friend? No, this is... This is my date. He's a lawyer. Does he have a name, or should I call him "Lawyer"? I'm sorry. This is Ace V... Tom Ace. Pleasure to meet you. Congratulations on all your success. You smell terrific! One of the first lessons we learned... ...back at... ...Stanford was the growth of food- poisoning claims against wealthy-people. One could make quite a lucrative law practice... ...with little else. How is everybody feeling tonight? Very, very well, thank you. Look, honey... ...there's the hors d'oeuvres. Are you insane? There is no way that Camp stole Snowflake. What are you trying to do? Will you keep him occupied while I work my magic, please? Smooshy, isn't it? We got a few cases from my new dealer in Paris. Excuse me, Ron... ...I need to use the bathroom. I think it's the pt. Sure, it's over there. Stuff probably looks better on the way out. He wasn't feeling well earlier today. Gravy! Don't worry, Snowflake. Ace Ventura's here. Yummy! Snowflake! Here, Snowflake. I've got a snack for you. They're wonderful, aren't they? Yes, they certainly are. No matter what's going on in my life... ...I can always watch them swim... ...and be totally at peace. It's not Snowflake! It's not Snowflake! It's not Snowflake! Are you sure your date is all right? It's been an awfully long time. Who, Tom? Well, I'm sure he's fine. Do not go in there! I'm sorry. I'll have the plumbing checked immediately. Do that! If I'd been drinking out of the toilet, I might've been killed. I'm sorry again, Mr. Ace. What're you doing? I'm sorry, Ron. What's he doing? Let's go! Stop it! I don't even wanna know why your pants are missing! You could've cost me my job! So you found a pebble in Snowflake's tank. I'll call CNN. I found it in the filter, thank you. And it's not a pebble, it's a rare, triangular cut orange amber. What're you talking about? Tonight I saw the same stone in Camp's ring. I thought you said Camp didn't do it. No, his ring wasn't missing a stone. But whoever was in that tank had a ring just like his. Ring? What ring? The 1984 Dolphin AFC championship ring. I find the ring with a missing stone, I find Snowflake. How you gonna do that? Simple. Loser! Why don't you learn how to drive, pal? You wanna play? That stone could've come from anywhere. It could've come from... ...a necklace or a pendant, an earring. It came from an '84 AFC championship ring. Einhorn thinks it may have been an animal-rights group. You know FAN? Free Animals Now, started by Chelsea, daughter of industrialist Fisher Gamble? Over half a million members worldwide? No. Who are they? Did you know... ...they sent letters to college teams demanding the release of their mascots? What do you feed your dog? Dog food. Why? He is miserable! What are you talking about? He's very unhappy. I feel sorry for him. Bad diet, isolated environment. It's amazing he's still alive. You're just mad because your stupid pebble theory didn't work out. You can't express anger. Yeah? And you're ugly. I'm not even gonna talk to you. Would you please leave? Why? So you can beat him? Fatty! You're unbelievable! Hiring you was the biggest mistake I ever made. Well, why don't you cry about it, saddlebags? You like her, huh? Yeah, she's all right. Look, Melissa, I... I'm here at the North Beach Towers condo complex in north Miami... ...where Roger Podacter, head of operations for the Miami Dolphins... ...has apparently committed suicide... ...allegedly leaping to his death from his 20th-story balcony... You okay? I told you. I was in my apartment... ...across the hall. I heard a scream... ...so I called the manager. The place was empty, except for the dog. I opened the balcony door and looked out... ...splat, bang, pancake time. Okay, thank you very much. Hi there, fella. Have a bad night? So... ...animals can sense evil. Who let Dr. Doolittle in? Lieutenant, he came with Miss Robinson. This is police business. We'll let you know if the coroner finds a tick. Face it... Forget it. She's right. Besides... ...I wouldn't want someone tracing my steps, pointing out my mistakes. So... ...you don't think this is an obvious suicide, Mr. Pet Detective? I wouldn't say that. There's plenty of evidence here to support your theory. Except, of course, for that spot of blood on the railing. May I tell you what I think happened? Alrighty, then! Roger Podacter went out after work, had a few drinks, then came home. He wasn't alone. Someone else was with him. There was a struggle... ...and he was thrown over that balcony. Roger Podacter didn't commit suicide. He was murdered. That's a very entertaining story... ...but real detectives have to worry about that little thing called... ...evidence. I think I heard a toilet flush. Maybe somebody lost a turtle. Well, I... I guess I'm out of my league here. Good work. There is just one more thing, lieutenant. This woman is Roger Podacter's neighbor. She said she heard a scream. Right? And you had to open the balcony door when you came in? - That's true. - You're sure you had to open this door? I'm certain. What's the point, Ventura? Only this. This is double-paned, soundproof glass. There is no way... ...she could have heard Podacter scream on the way down. The scream she heard came from inside... ...before he was thrown off the balcony. The murderer closed the door upon going. Can you feel that, buddy? I have exorcized the demons! This house is clear. - Losers. - Get him out of here! - Losers! Losers! - Let's go, Ace. Losers. Come on. Back to the zoo. What are you thinking? This whole thing is connected, somehow. I want to find that other ring. Ace, you checked all the rings. Receipts? What about receipts? There's gotta be receipts. That was pretty impressive, what you did at the apartment. You don't have to tell me. I was there. Maybe you should've joined the police force, become a real detective. I don't do humans. You really love animals. If it gets cold enough. No, I have a kinship with them. I understand them. Wanna hear something spooky? Sure. One time when I was about 12, I had a dream that I was being followed by... ...a big dog with rabies. He had these bloodshot eyes... ...and foam came out of his mouth. No matter how fast I ran, he just kept gaining on me and gaining on me. Then just before I got to my front door... ...he jumped and sank his teeth in. That's when I woke up... ...and felt the back of my neck. Check that out. Bastard! I'm sorry, I just couldn't help myself. Want to know why I do this? I'm not sure anymore. You better be sure... ...because once you get inside my head... ...there's no turning back. So... Are these all? There's only a dozen. Maybe it's in another file, in the back. Who the hell is that? What? That. Who the hell is that? That's Ray Finkle, the kicker. Don't you know who he is? Why isn't he in this picture? This was taken earlier in the year. Ray Finkle wasn't added till mid-season. He missed the final field goal in the Super Bowl that year. Cost the Dolphins the game. But he got himself a ring, didn't he? Definitely. "Replacement kicker having a great year." "Ready for Super Bowl, all-star kicker boasts." "Field goal sails wide, Dolphins lose Super Bowl." "The kick heard round the world." That was Finkle. The Dolphins lost by one point. Poor guy. Poor guy with a motive, baby. Where is he now? I heard he went back to his hometown in Collier County. Really? You're gonna drop me off before you go? No way. You shouldn't be left alone right now. It might not be safe at your apartment. What do you suggest? Oh, my God! Oh, my God. Three times? I'm sorry, that's never happened to me before. I must be tired. Okay, I'm ready again. I'm looking for Ray Finkle... ...and a clean pair of shorts. What do you know about Ray Finkle? Soccer-style kicker. Graduated from Collier High, 1976. Stetson University honors graduate, Most points and distance. Nickname, "The Mule." The only pro athlete from here. And one hell of a model American. Are you another one of them Hard Copy guys? No, sir. I'm just a big Finkle fan. This is my Graceland, sir. Will you put that gun down? The boy is a fan of our son. So nice to meet you. I'm Ray's mother... ...and this is Ray's father. It's a real honor! It's an honor to have you here. My Ray is so appreciative of his fans. He'll be so pleased you stopped by. Are you expecting Ray anytime soon? Oh, yes. I expect him home any minute. Would you like some cookies? I just baked them. Yummy! Ray Finkle's house. I can't wait to meet him. Ray ain't coming home. But your wife expects him any minute. She expects him home any minute. See, the engine's running but there's nobody behind the wheel. Eight years ago... ...our son escaped from Shady Acres Mental Hospital. And they're still bugging us to pick up his stuff. It was all that Dan Marino's fault. Everyone knows that. If he'd held the ball laces out, like he's supposed to... ...Ray wouldn't have missed the kick. Dan Marino should die of gonorrhea and rot in hell. Would you like a cookie, son? What do you know? They're little footballs. Laces out. When Ray gets back and starts kicking again... ...he'll never even know he was gone. I've kept his room just the way he left it. Oh, boy! What a sports nut, huh? May I? Oh, yes, by all means. Five seconds to go here in Super Bowl 17. Dolphins trailing the 49ers... ... by one. This will win the game for Miami. There's the snap. Marino holds. The kick... ... and it's high. No, it's... ... no good. Ray Finkle blew a 26-yard field goal! I don't believe it! The Dolphins lose! The Dolphins lose! The Dolphins lose the Super Bowl! - Melissa, it's Ace! - Where are you? I'm in psychoville, and Finkle's the mayor. Where's Marino? Why? He's about to join Snowflake. I've gotta know where he is! He has a commercial shoot at the Bogart Sound Stage. Call the police. Get extra security over there. Now! Ace, what's going on? Thought I left? I'm really gonna go this time. Here we go, folks. Very quiet. Action! I'm Dan Marino, and if anyone knows the value of protection, it's me. So I take care of the hands that take care of me... ...with Isotoner gloves! Cut! Again from the top. I said, cut! Guys, it's a cut! What the hell are they doing? That's a cut! - What is this, a rewrite? - Shut up! - Where'd they go? - Over there! Let's go! Excuse me, gentlemen! Pet detective! Come on! What's wrong? Can't you hit me? Have there been ransom demands? There's no communication with the kidnappers. Will the Super Bowl be postponed? The game is on as scheduled. Why weren't we told about the kidnapping? Secrecy was essential. We couldn't risk any interference. - Are the crimes related? - I'm sorry, I can't comment further. Now, if you'll excuse me... Get me the autopsy on Podacter! Aguado, send out a memo: No one talks to the press! And somebody get me some coffee! Tonight on Miami Vice, Crockett gets the boss a coffee! When I get out of that bathroom, you'd better be gone! Is it number one or number two? I just wanna know how much time I have. By the way, I went ahead and solved that... ...pesky Snowflake-Podacter- Marino thing. You ever heard of a former Dolphin kicker named Ray Finkle? All right, Ventura... ...make it quick. I found a rare stone at the bottom of Snowflake's tank. It belongs to a Dolphin '84 AFC championship ring. It would've been a Super Bowl ring, but Ray missed the kick. Blames the whole thing on Marino. We're talking paranoid, delusional psychosis. I saw the guy's room. Cozy, if you're Hannibal Lecter. So how does Roger Podacter fit in? My guess is, Finkle was snooping around. Podacter recognized him. End of story. As for Snowflake, they gave him Finkle's number, taught him how to kick a goal. Finkle took it personally. So where is Finkle now? Busted out of a mental institute. He's been plotting his revenge for years. Waiting for the perfect time to get back at them. The time when it'd hurt them most: Super Bowl time. Man, I'm tired of being right! Congratulations. You've done some fine detective work... ...Ace. I'm sorry, could you speak into my good ear? I thought I heard you call me Ace. Maybe I was wrong about you. Maybe you are more than just a pet dick. Your gun is digging into my hip. What's wrong? Want me to read you your rights? Maybe later. What is it? That bony little... ...Melissa Robinson? You just don't do anything for me. Down, boy! Everything okay in here? I heard some commotion. Fine, sergeant. You want me to throw him out? Why don't you throw yourself out? Yes, ma'am. Ace, I want you to leave everything to us. I can't do that, lieutenant. I was hired to find Snowflake. When we find Marino... ...we'll deliver Snowflake. When I find Snowflake... ...I'll deliver Marino. Melissa, it's Ace! What are you doing here? It's the middle of the night. You have to commit me. Finkle escaped from Shady Acres. They still have his stuff. They aren't gonna let us look around. I know. It's a good thing I'm a master of disguise. Mrs. Robinson... ...I'm Dr. Handly. Now who is it you want us to look at? My brother... ...Larry. I'm ready to go in. Just give me a chance! I know there's a lot riding on it, but it's all psychological. Just gotta stay positive. I'm gonna execute a buttonhook pattern, super slow-mo. Let's see that... ...in an instant replay. Your brother won't be the first football pro we've treated. - Is that right? - Yes, we're very sensitive... ...to the stress athletes have to endure. I'm open! I'm open! I'm open! We'll do some preliminary evaluations... ...but I think he'll fit in nicely here. Over here! Rover, sit! Hut, hut! He seems to have some difficulty letting go of the game. Has he had a history of mental illness? As long as I've known him. This is one of our therapy rooms. And we do arts and crafts out here in the courtyard. And this is the storage room. Down the hallway we have another... Halftime! He'll be fine there by himself for the next 20 minutes. I'll show you the dormitories, then. Isotoners. Obsess much? Where are you going? - To clean the storage room. - No, clean the cafeteria. I don't tell you how to do your job. The schedule says... ...clean the cafeteria. - I know what I'm doing. You should've done it earlier. Man, come on. Cafeteria, my butt! I'm cleaning in here! You take breaks too long. You smoke... Man, you're a pain in the butt! "Search called off for missing hiker." "A search ended today when rescue workers... ...were unable to find the body of Lois Einhorn." A hiker missing since Friday? Lois Einhorn? Holy moly! What're you doing out here? Get back to work! "Love, Roger"? Ace, it's E. You think the article you found was something? I got a note from Roger to Einhorn... ... thanking her for a wonderful evening. Something ain't stirring the Kool-Aid, man. Wiggles, rewind. What the hell does Lois Einhorn have to do with Ray Finkle? Come on, think! Finkle and Einhorn, in it together. How? Why? All right! Here we go. Answer's right there! Just gotta get blood to the brain! Finkle and Einhorn! Finkle and Einhorn! Finkle and Einhorn! Finkle and Einhorn! Quitter! What do you want? I don't have any food for you. I have to have money to buy food. I have to have a dolphin to get money. Do you see a dolphin here? Let's face it... ...your master is a loser. What the? That's it. That's it! Einhorn is Finkle. Finkle is Einhorn! Einhorn is a man! Oh, my God! Einhorn is a man! "Your gun is digging into my hip." God! And the big story in this Super Bowl game is the abduction... ... of Miami's starting quarterback, Dan Marino. It's gotta be a strain on this Miami team, Bob... What's the matter, Dan? Aren't you having fun? I just love Super Bowl Sunday. Don't you, Dan? A magical afternoon... ...where dreams are made... ...and crushed. Look, if you want tickets, you're going about it the wrong way. Do I look familiar to you? Does it seem as if we've... ...met someplace before? I don't know. I get hit in the head a lot. Now the coin toss. Kickoff time. My favorite thing. Laces out! I made some refreshments, Dan. Would you like some refreshments, Dan? I'll be right back, Dan. I don't know how much psycho-woman's paying you, but I'll double it. Sorry. "Psycho-woman" keeps us out of prison. Snowflake, here you go. Come on. Check it out, Marino. I'm throwing passes to a dolphin. Go get some more fish! I'm gonna kill that dolphin. Lovely party. Pity I wasn't invited. Where the hell's the smelt? Unconscious. Exactly as I planned. What the hell was that? What happened? What's going on? You okay? Guess what? It's naptime! What a hit! Heads up! Who are you? Ace Ventura, Pet Detective. I've been sent with a special play: The quarterback sneak. Penalty! Too many men on the field. I warned you, Ventura. Whatever happened to "Ace"? Good question. Be careful with that phone. In time, you could develop a tumor. Aguado, it's Lieutenant Einhorn. Send some men over to the Hallandale yacht basin. I've got the kidnapper trapped in the warehouse. It's Ace Ventura, Pet Detective. Code 11 in progress, 343 Victorville Road... ... at the Palmdale basin. Officer needs backup. Suspect's name: Ace Ventura... ... should be considered armed and dangerous. It's Ace. We gotta break out of here. Is he in trouble? Don't worry, if there's one thing I know... ...there's nothing Ace can't handle. Don't kill me! Please! I'll never tell anyone, I swear. - He's who you want! Kill him! - Kill him! Kill him! He held the ball, remember? Come on, look at him! - Crybaby! - Jock! - Wimp. - Musclehead. Shut up! I think I'll kill the dolphin first. I wouldn't want you to miss that. And there's the snap. The kick! And it's good! Good to see somebody who doesn't buckle under the pressure! What would you know about pressure? Well, I have kissed a man. Of course, there's never been a more crucial kick in a Super Bowl... ... than the "kick heard around the world." I mean, it's clear to me that it was a good hold. Finkle just booted it. The laces were in! They were in! You like that? You like that? And that! And that! Having a little trouble with the lady? You don't understand... ...she's a... Get him, Lois! Get him! Get him! Shoot him! - Shoot him! - Hold your fire! Don't shoot! Put your guns down, or this cop gets it! I mean it! She's not joking! He kidnapped Snowflake! He killed Roger Podacter and was about to kill Marino and me! Fiction can be fun! But I find the reference section much more enlightening. For instance... ...if you look up... ...professional football's all-time bonehead plays... ...you might read about a Miami Dolphin kicker named Ray Finkle... ...who missed a 26-yard field goal in the closing seconds of Super Bowl 17. You wouldn't read that Finkle was committed to a mental hospital... ...only to escape and join the police... ...in a scheme to get even with Marino... ...whom he blamed for the entire thing! What are you talking about? She's not Lois Einhorn! She's Ray Finkle! She's a man! He's lying! Shoot him! Let's just see who's lying, shall we? Would a real woman have to wear one of these? Boy, that's really on there! But tell me this: Would a real woman... ...be missing these? That kind of surgery can be done over the weekend. But I doubt very much... ...if he could find the time during his busy schedule... ...to get rid of... ...big old... ...Mr. Knish! Oh, boy! Come here. Would you excuse me for just one second? Ladies and gentlemen... ...my esteemed colleague, Mr. Marino... ...brought new evidence to my attention. Now... ...history has certainly shown that even the most intuitive... ...criminal investigator can be wrong. But if I am mistaken... ...if the lieutenant is indeed a woman... ...as she claims to be... ...then, my friend... ...she is suffering from the worst case of hemorrhoids I have ever seen! That's why Roger Podacter is dead! He found Captain Winkie! Good night! You've been a wonderful audience. Be sure to tip your waitress. Die, animal boy! Quick decision. Loser! You have any more gum? That's none of your business. Stay out of my personal affairs. You're a weird guy, Ace. A weird guy. Ladies and gentlemen... ... the Miami Dolphins are proud... ... to welcome back to Joe Robbie Stadium... ... our beloved mascot... ... and the star of our halftime show: Snowflake! And now... ... returning for the second half, the Dolphins' most valuable player... ... Dan Marino! Idiot! Do you know what you've done? You just cost me 25 grand, Polly. Yeah? Blow me! Really? The National Football League... ... would like to offer a special thank- you to the man who rescued Dan Marino... ... and our beloved Snowflake. A great humanitarian... ... and a lover of all animals: Mr. Ace Ventura! Get off me! Get off me!

---
## [nednaZ/Monkestation2.0](https://github.com/nednaZ/Monkestation2.0)@[d43ebd042d...](https://github.com/nednaZ/Monkestation2.0/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Monday 2023-05-08 16:00:24 by san7890

Log Active Turfs To Mapping Log (#74267)

## About The Pull Request

Was reminded of doing this via
https://github.com/tgstation/tgstation/issues/74245#issuecomment-1483943979

They're mapping issues, so let's log them to the mapping log. Quite
shrimple honestly.


![image](https://user-images.githubusercontent.com/34697715/227805458-5e6bcf01-629d-4b81-ab6a-b26e63d41ca3.png)
## Why It's Good For The Game

As the comments expound, the reason why we probably haven't done this in
the past is because any number of things can cause active turfs (like
ruin placement (either in icebox or in space)), or other silly stuff
like that. Thus, finding stuff like this would only really be viable
with stuff like the View Active Turfs verb, where you could visually
jump to and see all of the active turfs in that dynamic configuration
(and this still remains the best way to find active turfs).

This PR just makes it easier to do a "post-mortem" analysis on potential
active turfs, so that if it's very blatant, it can be fixed a lot
easier. It's best to try and find them during an ongoing round, but this
is life. (same as the unit tests concession, not too enthused on that
but we would have spontaneous errors out the ass without _something_)
## Changelog
Nothing that concerns players.

---------

Co-authored-by: tattle <66640614+dragomagol@users.noreply.github.com>

---
## [nednaZ/Monkestation2.0](https://github.com/nednaZ/Monkestation2.0)@[40fc11eb07...](https://github.com/nednaZ/Monkestation2.0/commit/40fc11eb0733ca25eff56e7379cb574a997fb6d3)
#### Monday 2023-05-08 16:00:24 by LemonInTheDark

Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[2c92211dac...](https://github.com/ss220-space/Skyrat-tg/commit/2c92211dac3d2929db283bb0e58d2933f1607b0d)
#### Monday 2023-05-08 16:05:18 by SkyratBot

[MIRROR] Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool [MDB IGNORE] (#20602)

* Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool (#74744)

## About The Pull Request

Replaced the subspace amplifier in the Black Market Uplink's crafting
recipe with a signaller and a microlaser.

Added the Black Market Uplink to the maintenance loot pool.
## Why It's Good For The Game

The BMU is an _extremely_ rare device to find in rounds. It can quite
literally ONLY be found via the crafting recipe, and with how stupidly
bloated the crafting lists are, it isn't something many people know
about. All this means that a very unique and engaging gimmick item is
tragically extremely obscured.

To add to this, the recipe requires a _subspace amplifier_. These items
are UNBELIEVABLY rare - they need you to vend them from a techfab with
bluespace communication technology researched, which is fair to say is
not a common thing. Sometimes maps have them in tech storage, but even
then you have to break and enter which can be quite risky at times and
an annoying blockade the other times.

The black market items are not worth this much hassle. They are all
small cute gimmicky objects that do not heavily impact the round. By
making it not only easier to craft with common items, but also appear in
the maintenance loot pool, this will make assistants find out about it
more often, which can further incentivize them to utilize the **cargo
bounty system** to get enough money to buy their funny gadgets.

Another idea would be to make the uplink appear as a bounty item, which
would be a great way to tell players it exists and encourage them to mix
both systems together. The system for getting items is also
unnecessarily, miserably awful - your item either gets literally thrown
into space from a random direction, or it is teleported silently without
warning in 60 seconds onto a completely random place which can very much
include Security, Command, the Vault, or other high-security areas.
Needing to B&E into these areas to get your durathread vest is, uh. Not
worth it. However these aren't part of this PR, unless they're given the
A-OK. (also maybe make it cargo purchasable?)
## Changelog
:cl:
balance: Makes Black Market Uplinks more easily craftable, adds them to
uncommon maint loot pool
/:cl:

* Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [openbsd/src](https://github.com/openbsd/src)@[7922d92f72...](https://github.com/openbsd/src/commit/7922d92f725a12fafc8177d16fef629aee4265a6)
#### Monday 2023-05-08 16:20:26 by tb

Rename the other_ctx in X509_STORE_CTX into trusted

The other_ctx is a strong contender for the worst name of a struct member
in OpenSSL. It's a void * member whose only purpose ever was to be set to a
STACK_OF(X509) * via X509_STORE_CTX_trusted_stack() (yes, this is obviously
a setter, why do you ask?) and then to be used by the get_issuer() callback
(which of course isn't there to find any old issuer, but only to look for
issuers among the 'trusted' certs).

Anyway, we may want to rename untrusted into intermediates and trusted into
roots later on, but for now let's match the lovely public API. While there
rename get_issuer_sk() into get_trusted_issuer() which is a more accurate
and slightly less silly name.

ok jsing

---
## [HorizonsEndMC/Ion](https://github.com/HorizonsEndMC/Ion)@[def6328a38...](https://github.com/HorizonsEndMC/Ion/commit/def6328a3840de08ec4b1bdd22ce8d482210e205)
#### Monday 2023-05-08 16:23:12 by Astralchroma

Whoever decided to not set a default value for this, fuck you

---
## [Firecharge123/cmss13](https://github.com/Firecharge123/cmss13)@[e4a1892e0a...](https://github.com/Firecharge123/cmss13/commit/e4a1892e0a42115dfb3d90009d960386b76fe955)
#### Monday 2023-05-08 16:27:25 by NewyearnewmeUwu

No more proximity sensor spam. (#3076)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
You can now slash proximity sensors to shut them up as xeno, and death
shuts off any proximity sensors in your belongings.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This is literally just the engi bellpack again. It's being used to OOCly
annoy people and needs a way to circumvent it.
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
fix: Proximity sensors can now be slashed by xenos to deactivate them,
and they turn off after you die if you have an active one on you.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d92fa5516f...](https://github.com/TaleStation/TaleStation/commit/d92fa5516ff15f84fcacdaed2cfec5a5b7b9520d)
#### Monday 2023-05-08 16:54:11 by TaleStationBot

[MIRROR] [MDB IGNORE] Golem Rework (#5675)

Original PR: https://github.com/tgstation/tgstation/pull/74197
-----
## About The Pull Request

Fixes #74375 *
Fixes #73235
Fixes #64420 *

*Technically, by making these things either intentional or nonexistent

This PR implements this design document:
https://hackmd.io/Y6uzGFDGSXKRaWDNicSiEg/BkRr176st
Put briefly, this will remove every existing golem subtype and
consolidate golems into a single species with cool new sprites.
NOT implemented from that PR is the ability to eat Telecrystals, I
couldn't come up with an appropriate visual that can stack with the
existing ones, but that should be a reasonably trivial add for a future
artist & developer.


![image](https://user-images.githubusercontent.com/7483112/235223788-cbfda4bc-1b4e-4613-b352-6179decb757b.png)
The diamond one renders you invisible so uh... hard to get a screenshot
of the sprite.

New Golems have a food-based mechanic where their hunger decays pretty
quickly and can only be replenished by eating minerals. They start
moving slower as they get hungrier, until eventually they become
completely immobilised and need to be rescued.
Eating different kinds of minerals will visually change your sprite and
give you a special effect in a similar way to old golems, but temporary.
While transformed, you can't eat any other kind of mineral which would
transform you (but can still consume glass).
To see the full list of effects, look at the hackmd above.


![image](https://user-images.githubusercontent.com/7483112/235224479-86f57ca2-4363-42de-8532-2a1141df09c9.png)

In service of these sprites working I have refactored the
`species/offset_features` feature by killing it and delegating that
responsibility to limbs instead. Rather than applying an offset to items
due to your species, it is due to your weird head or arms. This makes
overall more sense to me, but it inflates the code changes in this PR
somewhat.
It doesn't make a lot of sense to atomise unfortunately because that
code also seemed to be entirely unused until I tried to use it in this
PR, so you wouldn't be able to tell if my changes broke anything. I
might make a downstream sad by doing this.

All of the actual numbers in this PR are made up and only loosely
tested, it will need some testmerges to gather feedback about whether it
sucks or not.

TODO:

- [x] Actually implement the rest of the transformation effects.
- [x] Add status alerts with tooltips to tell you what's happening to
you.
- [x] Add examine tooltips to edible minerals if you have a golem brain.
- [x] Possibly add examine tooltips to the Golem to let other people
know what their active effect is doing?
- [x] Check if a limb we have is actually a golem one before drawing
rocks growing out of it.
- [x] Make Golems become immobilised if they are starving.
- [x] Test golems wearing clothes.
- [x] Test humans with golem limbs (Test conclusion: it's fucked, don't
allow it)
- [x] Let golems smelt materials if they are stood in lava.
- [x] Figure out what to do with the couple of places which used to
spawn specific golem subtypes.
- [x] Maybe let them mine by punching or tie that to one of the mineral
buffs idk.
- [ ] Add excitement to any effects which don't seem useful or
interesting in practice.
- [ ] Tune values so that you both have to actively care about having
food on hand but also can meaningfully enjoy the game.

Other relevant changes:
I reworked how bioscrambling works based off bodypart bodytypes, to
automatically exclude golem limbs in either direction. There's really no
way to have those work on humans or vice versa. Organs still fly though.

## Why It's Good For The Game

Reduces the pollution of the codebase by tens of subtypes of one gimmick
species.
Refocuses golems to be good at mining, and able to perform secondary
roles based on what they are being supplied with to eat, instead of
being a huge number of visually similar guys who mostly just hung around
being humans anyway.
These sprites look really good (but I need to make sure they work well
when put on other carbons, and with clothes).

## Changelog

:cl: Jacquerel with new icons mostly by INFRARED_BARON 
balance: Golems have been reworked into a hunger-based species who gain
temporary transformations when eating different kinds of mineral.
del: The previous golem subtypes no longer exist.
/:cl:

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [LpSuchtie/CHOMPStation2](https://github.com/LpSuchtie/CHOMPStation2)@[b1f52736ca...](https://github.com/LpSuchtie/CHOMPStation2/commit/b1f52736ca4407110979e2c246ae002b89ed86ae)
#### Monday 2023-05-08 17:24:23 by Fluff

Loots, Loots, and More Loots

-Removed the gas in the phoron canisters, and added some chemdispensers in place of the sleeper
-Made the carbinter gun thing useable
-Hopefully made the pirate vessel worth visisting
-Changed the walls of the vox shuttle, adjusted the foes because the giant voxes just stop exsisting, and mercs should die quikly
-Slightly buffed red shuttle down loot.
-Buffed the loot of the blood church

---
## [V037/fuck-that-shit-arduino-suck](https://github.com/V037/fuck-that-shit-arduino-suck)@[d56f65403a...](https://github.com/V037/fuck-that-shit-arduino-suck/commit/d56f65403a2d4271dc78f420a6b29d4d3b13a5fc)
#### Monday 2023-05-08 17:29:26 by Valentino

Merge branch 'main' of https://github.com/V037/fuck-that-shit-arduino-suck

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2068ea9ab5...](https://github.com/tgstation/tgstation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Monday 2023-05-08 17:42:56 by SyncIt21

Crate, Closet Refactors & Access Secured Stuff  (#74754)

## About The Pull Request
This PR is actually 2 parts, one that fixes runtimes with crates & the
other that allows secured closets to be crafted
along with a secured suit storage unit

**Crate Fixes**

Fixes #74708

The problem starts here

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L31-L34
Not only does this if condition look ugly but it's highly error prone
because one single call to `update_appearance()` can cause this to fail,
and sure enough if you look at the parent `Initialize()` proc it calls
just that

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L81-L88
Since we know the appearance is guaranteed to be changed in some way
before the if condition gets executed let's check what the final state
of the crate would be before this if check

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L54-L56
We see that the final icon state depends on the variable `opened` so if
we want to place/spawn a crate that is opened at round start we have to
ensure that `opened = TRUE` so the `if(icon_state ==
"[initial(icon_state)]open")` succeeds and does its job correctly.
Sadly we did dum shit like this
```
/obj/structure/closet/crate{
	icon_state = "crateopen"
}
```
throughout the entire code base, we thought backwards and were only
concerned in making the closet look open rather than setting its correct
variables to actually say that it is opened. because none of these
crates actually set `opened = TRUE` the final icon state becomes just
"crate" NOT "crateopen" therefore the if condition fails and we add the
component

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L36-L37
with the wrong parameters, so when closing the closet after_close()
removes the component with the wrong arguments

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L81-L84
that is does not unregister the signals and readds the component i.e.
re-registers the signals causing runtime.

The solution just do this
```
/obj/structure/closet/crate/open[mapping helper]
```
To clearly state that you want the closet to be open, that way you don't
have to memorize the icon_state for each different type of crate, it's
consistent across all crates & you don't get runtimes.

And that's exactly what i did everywhere

Another issue that is fixed is "Houdini crates" i.e. crates which are
open & appear empty but when you close & reopen them magical loot
appears, Go ahead walk upto to cargo and find any empty crate that is
open and do this

Fixes #69779


https://user-images.githubusercontent.com/110812394/232234489-0193acde-22c8-4c19-af89-e897f3c23d53.mp4

You will be surprised, This is seriously harmful to players because they
can just walk by a crate that appears to be open & empty only to realize
later that it had some awesome loot. Just mean

The reason this happens is because of the Late Initialization inside
closets

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L85-L86

What late initialization does is suck up all stuff on its turf

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L97-L100

In theory this is supposed to work perfectly, if the closet is closed
move everything on the turf into the closet and so when the player opens
it, they all pop back out.
But what happens if the closet is opened before ` LateInitialize()` is
called? This breaking behaviour is caused by object spawners

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/effects/spawners/random/structure.dm#L94-L100
And maint crates

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L141-L143
These 2 spawners open up the crate based on random probability before `
LateInitialize()` is called on the crate and so what happens is the
crate is first opened and then stuff on the turf is sucked in causing an
open but empty crate to appear.

The solution is simple just check again in ` LateInitialize()` if our
crate is still closed before we proceed.That's fixed now too

**Code Refactors**
1. Introduced 2 new signals COMSIG_CLOSET_PRE/POST CLOSE which are the
counter parts for the open signals. hook into them if you ever need to
do stuff before & after closing the closet while return BLOCK_CLOSE for
COMSIG_CLOSET_PRE_CLOSE if you want to block closing the closet for some
reason
2. 2 new procs `before_open()` & `before_close()` which are the counter
parts for `after_open()` & `after_close()`. If you need to write checks
and do actions before opening the closet or before closing the closet
override these procs & not the `open()` & `close()` procs directly

**Secured Craftables** 
This is just a reopened version of #74115 after i accidently merged
another branch without resolving the conflicts first so i'll just
repaste everything here, since crates & closets are related might as
well do all in one

1. **Access secured closets**
   
   - **What about them?**
          **1. Existing System**
If you wanted to create a access secured closet with the existing system
its an 4 step process
            - First construct a normal closet
            - Weld it shut so you can install the airlock electronics
            - Install the electronics [4 seconds]
            - Unweld
This is a 4 step process which takes time & requires a welding tool
         **2. New system**
Combine the 4 steps into 1 by crafting the secure closet directly
                    
![Screenshot
(184)](https://user-images.githubusercontent.com/110812394/235904926-c2ea231c-eba7-45d0-a5af-e0456fdd40bc.png)

    - **Bonus Features**
              **1. Card reader**
The card reader acts as an interface between the airlock electronics &
the player. Usually if you want to change access on a locker you have to
                  - Weld the closet shut
                  - Screw driver out the electronics
                  - Change the settings
                  - Install it back
                  - Unweld
With a card reader there is no need of a welder & screwdriver. You can
change the access of the locker while its operational

        **How do i install the card reader?**
             1. Weld the closet shut
             3. Insert card reader with hand
4. To remove the card reader use crowbar or just deconstruct the whole
closet with a welding tool
             5. Unweld closet

         **How to change its access?**
This will overwrite the settings on your airlock electronics. To do this
1. make sure the closet is first unlocked. This is important so that no
random person who doesn't have access to the closet can change its
access while its locked. It would be like giving the privilege of
changing your current password without first confirming if you know the
old password
2. attack/swipe the closet with your PDA. Make sure your ID card is
inside the PDA for this to work. You can also just use your ID card
directly without a PDA
         3. You will get 3 options to decide the new access levels
           
![Screenshot
(174)](https://user-images.githubusercontent.com/110812394/233454364-d99a2fb6-9f26-4db3-9fac-a10689955484.png)


        They work as follows
- **Personal**: As the name implies only you can access this locker and
no one else. Make sure to have your ID on you at all times cause if you
loose it then no one can open it
- **Departmental**: This copies the access levels of your ID and will
allow people having those exact same access levels. Say you want to
create a closet accessible to only miners. Then have an miner choose
this option and now only miners can open this closet. If the Hop sets
custom access on your ID then only people with those specific access
levels can open this closet
         - **None**: No access, free for all just like a normal closet

**Security:** After you have set the access level it is important to
lock the access panel with a "multi-tool", so no one else can change it.
Unlock the panel again with the "multi-tool" to set the new access type

       **2. Give your own name & description**
To rename the closet or change its description you must first make the
closet access type as personel i.e. make it yours, then use an pen to
complete the job. You cannot change names of departmental or no access
closets because that's vandelism

       **3. Custom Paint Job**
    Use airlock painter. Not intuitive but does the job. 
   
![Screenshot
(181)](https://user-images.githubusercontent.com/110812394/234202905-00946b88-2513-489d-b0a2-d618a72f3e49.png)

      **4. Personal closets**
Round start personal closets can have their access overridden by a new
ID when in it's unlocked state. This is useful if the last person has no
use for the closet & someone else wants to use it.


    - **Why its good for the game?**      
1. Having your own personal closet with your own name & description
gives you more privacy & security for your belongings so people don't
steal your stuff. Personal access is more secure because it requires you
to have the physical ID card you used to set this access and not an ID
which has the same access levels as your previous ID
2. Make secure closets faster without an welding tool & screw driver
3. Bug fix where electronics could be screwed out from round start
secured closets countless times spawning a new airlock electronic each
time
      
2. **Access secured freezers**

    - **What about them?**
The craftable freezer from #73942 has been modified to support secure
access. These can be deconstructed with welders just as before

![Screenshot
(185)](https://user-images.githubusercontent.com/110812394/235905000-ba165feb-4384-4759-b46b-dba77c9e6ba3.png)


    - **How does it work?**
The access stuff works exactly the same as secure closets described
above. You can rename & change description with pen just like the above
described secure closets. No paint job for this. Install card reader
with the same steps described above.

    - **Why it's good for the game?**
1. Make access secured freezers faster without a welder and screwdriver
2. Your own personally named & locked freezer for storing dead bodies is
always a good thing

4. **Access secured suit storage unit**
   - **What about them?**
Suit storage units now require airlock electronics for construction. The
access levels you set on it will be used to decide
       1. If a player can unlock the unit
       2. If the player can open the unit after unlocking
       3. If the player can disinfect whatever is inside
       
      By default all round start suit storage units have free access

   - **Install card reader**
Provides the same functionality as secured closets described above. To
install it
     1. Open its panel with a screw driver
     2. Add a card reader to it with hand
     3. Close the panel
     
     When you deconstruct the machine the card reader pops back out

   - **Why it's good for the game?**
1. Having your own access protected and named suit storage unit so
random people don't steal your mod suits? Who wouldn't want that.?
Provides security for department storage units.
2. If you have the unit locked then you cannot deconstruct the machine
with a crowbar providing additional security
3. Fixes #70552 , random people can't open/unlock the suit storage unit
without access. You can set personal access to make sure only you can
access the unit

## Changelog
:cl:
add: Access secured closets. Personal closets can have their access
overwritten by an new id in it's unlocked state
add: Access secured freezers.
add: Access secured suit storage units.
fix: Suit storage unit not having access restrictions.
fix: airlock electronics not properly getting removed after screwing
them out from round start lockers
fix: round spawned open crates run timing when closed
fix: open crates hiding stuff in plain sight
fix: open closets/crates sucking up contents during late initialize
causing them appear empty & open
/:cl:

---------

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [Eric-Arellano/rustworkx](https://github.com/Eric-Arellano/rustworkx)@[e025356b04...](https://github.com/Eric-Arellano/rustworkx/commit/e025356b046a807e848a7c0ee2a32490927d46da)
#### Monday 2023-05-08 17:53:44 by Matthew Treinish

Update tox configuration to use tox >= 4.4.0 (#851)

* Update tox configuration to use tox >= 4.4.0

Tox 4.0.0 was released in December 2022 [1] and was a major rewrite of
the internals of the package that included numerous backwards
incompatible changes [2]. Along with that major rewrite was a long
period of instability in the package with a flurry of 47 releases [3]
since 4.0.0 (which has only been 3-4 months). At the time of the 4.0.0
release we pinned the tox version in CI with #761 to avoid this
instability as our tox configuration was not compatible with tox 4.x.y
and tox was actually not compatible with how we had things configured
more generally. The hope was that tox would stabilize more, fix the
issues that plagued the tox 4 release series and we'd be able to relax
that pin without requiring bumping our minimum tox version to ensure
users could use either the old version or the new version locally.
However, since #761 that hope hasn't been realized the divergence
between tox 3 and tox 4 has only widened and at least personally I'm not
convinced of an improvement in stability to the tox 4 release series.
That being said however, this is becoming a developer pain as by default
when setting up a new build environment pip will install the latest
version of tox and we don't have an effective mechanism to pin the tox
version for users as you need to install tox manually as it's the
primary python development entrypoint we use. The only only avenue to
address this would be documentation updates in the CONTRIBUTING.md file,
which we didn't update at the time in #761 because it was meant to be
a version temporary pin that has turned out to not be so temporary.

Since it's been >3 months since we first pinned the tox version and that
pin was meant to be temporary this commit removes that pin and bumps our
minimum supported tox version to be 4.4.0, which despite not being
compatible with tox < 4 as we originally hoped, at least seems to work
fine with install rustworkx after updating the configuration file. This
should hopefully ease the onboarding experience for developers when
working with rustworkx and trying to bootstrap a local development
environment. Longer term I expect we'll look at moving off of tox,
as it no longer seems like a project we can rely on (especially as
a key component for our development and CI infrastructure) for rustworkx
and instead look at something like `nox` which I've heard good things
about and know that PyO3 had moved to it a year or two ago.

Fixes #812

[1] https://pypi.org/project/tox/4.0.0/
[2] https://tox.wiki/en/latest/upgrading.html
[3] https://pypi.org/project/tox/#history

* Stop using tox for retworkx backwards compat jobs

Tox's isolated builder mechanism seems to be incompatible with our
environment variable based package naming mechanism that we use to build
the legacy retworkx package. This is causing CI to fail on the backwards
compat jobs that are installing retworkx (which depends on rustworkx) to
ensure that our backwards compatibility shim works as expected. Instead
of trying to force tox to do the correct thing, it's just easier to stop
using it for that one CI job and instead just manually install and run
the tests.

---
## [AtomicMaya/ftp-server-client](https://github.com/AtomicMaya/ftp-server-client)@[d7662d82cd...](https://github.com/AtomicMaya/ftp-server-client/commit/d7662d82cded7825d6e7f448c17bf547a53b1089)
#### Monday 2023-05-08 18:13:56 by AtomicMaya

add README

START

Modular Makefile, basic TCP SND/RCV, server loop

Added lineReader, utilities server side and client side (constants, etc...)

Need CRC

Add common/ Need CRC

CRC tested, builtins added

Colors ! :smile:

Need to decompile and verify packet info on recv

Added CMD predefs, added message pinging, need acknowledgment, need mkdir, need distant cd, need local cd

Trying stuff

SERVER MESSAGING

Added Reqs, stuff

Get this fucking thing to fucking work, stat

FILE CORRUPTION WTAF

Got stuff done

GOT CRC WORKING AND MSG PING + CONF, need CRC VALIDATION

GOT THE THING TO FUCKING WORK

SMTHG SMTHG NEED TO STRESS TEST

Added File utilities, need to implement IO handshake, etc. Night Night

Fixed weird ' ' issue

new builtin shit, added signal handle for client sigint, kill me now

REWORKED PACKET SYSTEM TO STATIC SIZE

SOMETHING

Added some listing stuff, removed ping

Moved queries to server/builtins, Working list query

Getting to upload

Procedure

Got fucking interrupted

Advances, lock file test

Wonky upload locks

Wonky upload locks

moved stuff tests to be done

Advances

Push under duress

SOMETHING

Test

Need to delocalize file

Got the upload working, delocalized push/pull. Now download

Cleanup on aisle 4 => added QOL macros in utils.h, upload is 100% functional

Started download, Modified debug clause

DOWNLOAD ADVANCES

MIGRATE

BUILTINS

FINISHED THE fucking download, added a delete command, distant and local

Hooray, catching up on documentation, client/builtins.c done

Comments galore

Done, I think

Finished README.md, removed hack for ../, added colors, etc...

Fixed typo in README.md, fucking the finalest now

[final] :rocket: Added a warning to the README, fixed one copy-paste typo on ./client/builtins.c, nothing breaking but can be confusing.

Add LICENSE

Update README.md

Update LICENSE

---
## [highlight/highlight](https://github.com/highlight/highlight)@[18d94ccc74...](https://github.com/highlight/highlight/commit/18d94ccc7425a9441000e1bf4a7f92565898666e)
#### Monday 2023-05-08 18:25:18 by Lewis Liu

Enable Reflame for Highlight web app (#4586)

## Summary

<!--
Ideally, there is an attached Linear ticket that will describe the
"why".

If relevant, use this section to call out any additional information
you'd like to _highlight_ to the reviewer.
-->

This PR finally enables [Reflame](https://reflame.app/)
[previews](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
for the Highlight web app. 🥳

### What does this mean for me?

First you'll need to sign up at https://reflame.app, connect your GitHub
account, and ask @Vadman97 for an invite to the highlight organization.

Then, once this PR is merged, every time you push up a change to the web
app (in /frontend) or any of its dependencies, you'll get a Reflame
preview link on your commit immediately, usually within 3 seconds,
instead of however many minutes it used to take:
![Screenshot 2023-04-13 at 5 40 57
PM](https://user-images.githubusercontent.com/6934200/231912410-5dc2880d-353c-402e-8562-67ce4ee54137.png)

In addition, you'll have access to the Reflame [VSCode
extension](https://marketplace.visualstudio.com/items?itemName=reflame.agent)
for development, which deploys your changes usually within ~500ms of a
file save, and then reflects your changes instantly with a full browser
refresh in production mode, or with state-preserving React fast refresh
in development mode. See development mode in action here:


https://user-images.githubusercontent.com/6934200/231914985-3679e955-ddcf-4ad1-9c7e-1c7451dc3ef5.mp4

It's worth noting that Reflame is actually _deploying your changes to
the internet_ every time, so you can send these links to yourself to
check your changes on another device (even multiple devices
simultaneously), or share them with teammates or customers to give them
a sneak peak of what you're working on, iterate with their feedback, and
have those changes reflected on their browsers in real time (even if
they're on the other side of the world)!

### How do I even review this? There's like 500 files here?!

I'd recommend reviewing either commit by commit and skipping the 2nd
commit, or by viewing all files changed and skipping over everything in
`__generated` folders, since they only contain files generated using the
newly added build scripts. This should leave only about 30 files to
review, and most of the changes are a only a couple of lines long.

These scripts and generated files are a temporary stop-gap to support
features that don't have first-class support in Reflame yet,
specifically:

- Reading version from package.json
- CSS/SCSS modules
- Tailwind
- SVGR
- Git Submodules
- Vanilla Extract

These are roughly ranked in order of how quickly I think they will get
first-class support in Reflame, at which point we'll be able to remove
the associated scripts and generated files. Notably, Vanilla Extract is
as far down the list as it is because it requires executing
user-supplied code as part of its build process, which is going to take
quite a bit of work to enable safely in a multitenant system like
Reflame (but I do plan on tackling this eventually as I get closer to
building features like testing and backend APIs support). Though we may
still be able to get rid of the build script sooner than that by
building it into the VSCode extension if there's enough demand.

Outside of the script and configuration changes, there are a few
additional source changes for compatibility. I left comments on the PR
for every one of these explaining the motivation behind them. I've also
split most of them out into separate PRs so they can be reviewed, tested
and shipped independently:

- https://github.com/highlight/highlight/pull/5086
- https://github.com/highlight/highlight/pull/5087
- https://github.com/highlight/highlight/pull/5088
- https://github.com/highlight/highlight/pull/5089 

## How did you test this change?

<!--
Frontend - Leave a screencast or a screenshot to visually describe the
changes.
-->

A lot of care has gone into making sure your existing local dev workflow
works exactly as you're used to (just with a few more scripts running
than before), and that the production deployment process remains
untouched as well. If you notice any material differences in any of your
day to day workflows while trying out this PR, or in the Render preview
deploys, please let me know and I'll try to address it ASAP.

I've tried following the [docker dev guide
here](https://www.highlight.io/docs/getting-started/self-host/dev-deployment-guide)
and running `yarn dev:frontend` (without the `doppler run --` part), and
both seem to be working identically as on main as far as I can tell,
though for the latter I'm missing a few env vars from doppler so
couldn't verify past the login screen, will need your help to make sure
everything works as expected there.

If you want to try out Reflame before this PR gets merged, just make a
branch off of this PR (previews are not working for this PR because it's
coming from a fork, and the appId in the config is for the
highlight/highlight repo, but it should work if you cherry pick these
commits into another branch within this repo). The VSCode extension
should also just work once you get a VSCode account.
[Here's](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
the preview I'm using to test my changes.

Would love to make Reflame better with your feedback! Just leave a
comment here, [shoot me an email](mailto:lewis@reflame.app), or ask for
an invite to the #highlight-reflame channel in Slack to chat there or
send me a DM.

## Are there any deployment considerations?

<!--
 Backend - Do we need to consider migrations or backfilling data?
-->

Definitely would be helpful to get a Render preview for this to poke
around in.

---
## [l3dlp-sandbox/terminal](https://github.com/l3dlp-sandbox/terminal)@[77215d9d77...](https://github.com/l3dlp-sandbox/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Monday 2023-05-08 18:29:08 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [l3dlp-sandbox/terminal](https://github.com/l3dlp-sandbox/terminal)@[9ccd6ecd74...](https://github.com/l3dlp-sandbox/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Monday 2023-05-08 18:29:08 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [RosieSapphire/RubyMath](https://github.com/RosieSapphire/RubyMath)@[9ceb701465...](https://github.com/RosieSapphire/RubyMath/commit/9ceb70146544bf0d6893e833ccd246b959aff7a0)
#### Monday 2023-05-08 18:31:07 by Rosie Sapphire

Oh my God, I think I finally fixed it holy fuck was it broken

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[66cb695343...](https://github.com/IndieanaJones/tgstation/commit/66cb695343721087437e651d07268e284e25763d)
#### Monday 2023-05-08 19:15:09 by carlarctg

IV drips' default transfer rate is no longer zero. (#74724)

## About The Pull Request

Set default IV transfer rate to maximum (5) instead of 0.
## Why It's Good For The Game

> Set default IV transfer rate to maximum (5) instead of 0.

When you hook someone onto an IV drip, you naturally expect that to be
the end of the process - you hooked someone to a drip, and now you can
go about your day. Them needing to fiddle with buttons is bad for
several reasons:

- It is unintuitive.
IV drips don't look like machines. Their sprite doesn't reflect the fact
that you need to fiddle with the settings before they can work the same
way any other machine or computer might. And to be honest, they
shouldn't.
- It is separate from how every other server currently has it.
Yes, yes, I know that argument is very flawed and full of holes. But
what I'm trying to say with it is, effectively speaking, an extension of
the above point. In other servers, you drag-click someone to an IV drip
and there we go, it's functional. In TG, it just-so-happens to not be
functional due to what is almost definitely a recent oversight, which
very much can, has, and will lead to unnecessary frustration.
- There is no practical reason for it to be set at 0.
Imagine if chem dispensers started at +0 units and needed to be set to
+5 to continue. Or if bottles had a transfer rate of 0u. Or if guns
started with their safeties on. Even if it made sense, it would just be
frustrating and needless, and wouldn't improve the game in any
significant manner enough to offset frustration. We're here for fun, not
perfect balance or realism/verisimilitude after all.
- It's an oversight.
It was changed in #71217. Before that, it was always set to the maximum,
5u. However, presumably due to confusion (Variables that can be adjusted
ingame usually are set to zero/the minimum possible) it ended up being
changed to this.

Apparently an argument can be made that this is fine because fumbling to
get medical aid done is a part of the game. I disagree heavily - blood
bags are already stored in the cold room, something only 2/5 of the
roles in medbay even have access to, with the paramedic, virologist,
chemist all being unable to reach it. This is already enough 'fumbling'
that's necessary. If someone moved the blood bags outside the cold room
next to the IV drips, then all the better - it's a reward for medbay
being prepared.

However I wouldn't mind if someone asked me to make it so the default
transfer rate is, well, something below maximum. It's common practice in
a lot of parts of SS13 to have things set in an unoptimized state so
players can go around improving them, such as air alarms, cryogenics,
etc. Just as long as it's not literally unusable otherwise, as the
'minimum basic setup' should just be slapping on a blood bag!
## Changelog
Dunno what to put here TBH. Can't tell if it's qol, fix, balance, etc.

:cl:
qol: Set default IV transfer rate to maximum (5) instead of 0.
/:cl:

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[205ea3dad7...](https://github.com/IndieanaJones/tgstation/commit/205ea3dad711fa541f93adc7f2053250d3e3c777)
#### Monday 2023-05-08 19:15:09 by Bloop

Fixes spoon overlay not updating every time (#74687)

## About The Pull Request

After bludgeoning myself one too many times with a spoon, here we are.

The spoon overlay wasn't updating to reflect that soup had been
consumed, which led to trying to eat it again and then pain.

Why do spoons hurt so much?

## Why It's Good For The Game

Less spoon related injuries.

## Changelog

:cl:
fix: spoon overlays will now update when you eat from them to reflect
that food = gone. it really is gone, you can stop beating yourself with
the spoon. oh god please stop--
/:cl:

---
## [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)@[0e96f1cd6e...](https://github.com/software-mansion/react-native-reanimated/commit/0e96f1cd6e0f6bae6a57aad6f5bd5208d5ae0d19)
#### Monday 2023-05-08 20:00:38 by Tomasz Żelawski

Remove plugin dev files from npm package (#4433)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Currently development files from `plugin/` are included in npm package.
This PR removes them from it.

b4:
<img width="253" alt="Screenshot 2023-05-08 at 14 39 29"
src="https://user-images.githubusercontent.com/40713406/236829343-1865480f-99d0-4843-adb2-f658db2acce0.png">
after:
<img width="238" alt="Screenshot 2023-05-08 at 14 39 51"
src="https://user-images.githubusercontent.com/40713406/236829379-7c31b6b4-27e1-493c-8be0-6254edbd0c4c.png">

Since [README is always
included](https://docs.npmjs.com/cli/v6/configuring-npm/package-json#files)
I renamed plugin's dev README and removed `README` from being included
in `package.json`.


## Test plan

I recommend using this powerful oneliner: 
`./createNPMPackage.sh && mkdir tarball-new && mv
react-native-reanimated-3.1.0.tgz tarball-new && tarball-new && tar -xf
react-native-reanimated-3.1.0.tgz && ..`
to see the contents of the new package.

Also run _some_ Example App to see if Reanimated plugin from the tarball
is actually working.

---
_Note_: Testing this PR took me longer than it should.

For some reason with current configuration of Example App and running it
on Android (I didn't check iOS) it's surprisingly difficult to use
reanimated from either tarball or unpacked tarball directory. I had to
make a new app and then include Example's source code there.

While it's not that troublesome I think we should have a more
streamlined approach for using custom reanimated package location for
tests with our Examples.

---------

Co-authored-by: Tomek Zawadzki <tomasz.zawadzki@swmansion.com>

---
## [TotoR115/Drizzt-Saga](https://github.com/TotoR115/Drizzt-Saga)@[914de29c90...](https://github.com/TotoR115/Drizzt-Saga/commit/914de29c907181ff2724b75cbbdf2819688633d3)
#### Monday 2023-05-08 20:13:32 by TotoR115

Creature Corrections

-f_lich.cre: has wrong race, skelleton instead of LICH, wrong alignement unknown(20) instead of lawfull_evil (19), wrong gender, should be male and wrong weapon, should be LICH02

-F_Valen.cre (Valen): Race and class should be VAMPIRE

-F_slaysh.cre (slayer shadow): race should be DEMONIC, Class should be SPECTRE, animation should be 0x7F32 (SLAYER). It also seems a bit too stong for an encounter; AC, THAC0, HP and strength are lowered

-F_cyclop.cre (cyclops): has no alignement, should be Chaotic evil (51) as PnP

-F_dipnos.cre (Nibby "Dipnose"): lack is alignement. set to Chaotic Neutral (50)

-F_dragon.cre (baby dragon): Race should be DRAGON. the strength seems a bit too hight (25) for a baby dragon. should be set to 19

-F_dromag.cre and F_drowar.cre (drows): lack alignement, should be neutral evil (35)

-F_gobele.cre and f_goblin.cre (goblins): lack alignement, should be lawful evil (19)

-f_nib.cre (nib jansen): lack alignement, could be Neutral good (33)

-f_spidqu.cre (demonic spider queen): as unknon alignement, and has HUMAN race instead of DEMONIC (121)

-f_wlfspr.cre (were winterwolf spirit): Class should be WOLFWERE (158), Race could be SPECTRE (133) and gender should be NEITHER (4).

-f_bel.cre (Belhifet): Race set to human instead of demonic

- F_drizzt.cre (drizzt): racial enemy is changed for something more usefull : DEMONIC (121)

---
## [Perkedel/perkedel-astro](https://github.com/Perkedel/perkedel-astro)@[541f5f612d...](https://github.com/Perkedel/perkedel-astro/commit/541f5f612d6dc76960ec2670bcf044cbc9316cc3)
#### Monday 2023-05-08 21:08:22 by Joel Robert Justiawan

I could only learn so much

that's it. look at sumarry, like I hear priest summarizing God's Bible, packed in a
khotbah presentation.

oh My God, that's (the Homestuck) not to mention isn't it?

sorry, I ..
asd
fa
sg
arg
aereg
erg
ersh

---
## [Pichoco/Wyvern-of-Marina](https://github.com/Pichoco/Wyvern-of-Marina)@[a7de6e45f7...](https://github.com/Pichoco/Wyvern-of-Marina/commit/a7de6e45f763e34fef04aa0b44b761e5b02a327b)
#### Monday 2023-05-08 21:29:57 by Megalon

removed music functionality but added other things

idk why replit was being a bitch and wouldn't allow me to use their opus support anymore which kinda sucks but hey it is what it is. at least i finished everything in the list we made a while ago, such as snipe, deletecommand, and sending a random username upon keyword "which"

---
## [willardstation/tg-voidcrew](https://github.com/willardstation/tg-voidcrew)@[2b2cb3dff6...](https://github.com/willardstation/tg-voidcrew/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Monday 2023-05-08 21:52:03 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [l3dlp-sandbox/sql](https://github.com/l3dlp-sandbox/sql)@[ebd772dd1d...](https://github.com/l3dlp-sandbox/sql/commit/ebd772dd1d8b4f1f5c08ab32da768b7ee0cb0660)
#### Monday 2023-05-08 22:18:14 by Rasmus Schultz

add support for yield $index => $value in mappers

this feature was missing and has been implemented as described in the README.

this is actually a bugfix, but it's also potentially a breaking change for some poorly implemented mappers - specifically, if your mapper inadvertedly discards the indices of the given array (effectively renumbering the values) this bug would previously help this case by simply renumbering the entire result.

for example, the following mapper function is lossy and discards indices:

function my_mapper(array $rows)
{
  foreach ($rows as $row) {
    yield $row;
  }
}

If you were using batches of, say, 20 records, this mapper would return an array with indices 0..19 for the first batch, and indices 0..19 again for the second batch, and so on. This coud likely cause nasty bugs in a loop that actually uses these keys for something, since the keys of each batch would collide with the keys of the previous batch.

The faulty batch processing behavior would simply renumber these as 0..19, 20..39 and so on, since it was effectively discarding your bad indices and renumbering everything.

With the introduction of this change, Result::createIterator() will assign a running $record_index, which ensures unique indices across batches - these indices will propagate to mappers, but if any mapper discards the indices, well, you get key collissions... meaning, anywhere we use iterator_to_array() or Result::all() etc. you can expect colliding entries to (silently!) disappear.

The good news is, if you're using Result::all() you're probably not using batches - since you're intentionally loading the entire result into a single array. If you did specify a page size, however, and one of your mappers discards indices, then yeah, you'll have problems.

This would seem to be a limitation of the array type in the PHP language, unfortunately. There's no difference between "array being used as a map" and "array proper" in PHP, hence no way to type-hint or even for our code to type-check at run-time.

Well, we could collect all the keys, test for collisions, and throw exceptions - but this would mean memory overhead for all keys in memory, which is potentially a problem for scripts working with very large batches.

We might be able to test for key collisions in Result::all() since here we expect everything to fit in memory anyhow - so adding an exception here might be a meaningful addition?

---
## [TheEmuDev/Fantasy-Game](https://github.com/TheEmuDev/Fantasy-Game)@[c807fcfa5b...](https://github.com/TheEmuDev/Fantasy-Game/commit/c807fcfa5bee18216e18414375383b4c6819eaf2)
#### Monday 2023-05-08 22:52:39 by Zach

Sorry that this is going into spawn enemy dean

fuck you :)

---
## [HeapsOfRam/GAMENet](https://github.com/HeapsOfRam/GAMENet)@[b89226cce7...](https://github.com/HeapsOfRam/GAMENet/commit/b89226cce715d7b3cc9080b3bb67d0d884ac9a4c)
#### Monday 2023-05-08 23:44:18 by HeapsOfRam

ablations (#3)

* ablations

This is the first commit for my work with ablations. The first
ablation I have tried to implement is omitting the history component
of the data preparation task. Strangely, this seems to perform
better than the original GAMENet model... I wonder if there is
something I am missing, if there is a change I need to make to
the GAMENet model in order to get this working properly. However,
for now this is at least a start with the ablations. I also will try
to add other ablations that make sense.

This commit also contains some major code restructuring. I have made
a class that is a wrapper around the data utilities that I have, that
can group tasks and datasets together to perform the necessary
preparation and provide the data needed for training. I don't think
this is necessarily the right approach, especially since I have
created my own `Task` class when pyhealth has its own concepts of
tasks. For now, this works and helps me dynamically switch certain
parameters such as what dataset I am using and which tasks I am
running -- so I may stick with it depending on the time I have. If
I have additional time, I will try to figure out a better way to
structure the code.

I have also added some other files, such as the start to an EDA
python notebook, but that is in its very nascent stages. I have added
a `drug_rec_task.py` that has the tasks I plan to perform for the
ablations, but most of them are experimental at the moment so I
plan to clean that up. I also included results from the runs, which
contain the strange situation of GAMENet results improving when not
considering the history of the patient.

* first refactor; task command line arguments

This commit contains the first refactor effort for this PR. I think
I may add a second refactor where I abstract some of the model logic
into another wrapper class. For now, I have cleaned up a lot of the
messiness of the first commit in the PR by removing old, commented
code and moving functions around.

First, I extracted the data logic into its own file so that it
would be a bit easier to manage. The gamenet.py file was getting
large and unwieldy so I figured this would help make things cleaner.
I also added the ability for the data wrapper to run custom tasks
that get passed to it, and generally made the flow here a little
bit nicer. I still don't know if this was the right abstraction to
have here, but for now it's codified the logic well enough that I
am satisfied (at least for now).

I also added some command line arguments to manage the running of
tasks. By default, only the original drug recommendation preparation
task is run. However, a user can specify any number of optional tasks
with the `-t` argument now, though at the moment the only additional
allowed task is the no history task -- the ablation introduced
earlier in this PR that computes the patient record without considering
their history of medications, procedures, and conditions. I feel
these changes should help make the development of further tasks a
bit easier. There is also the `-a` flag, which will run all of the
possible tasks for that dataset.

* second refactor; model abstractions

Abstracted the model logic out into a wrapper that helps to
encapsulate the functions that are important for training and model
evaluation. This is a small refactor compared to the previous one,
but my plan for the next commits is to add a metric around the
number of drugs being recommended by each method, and to add more
ablations as needed. I have a feeling that while the GAMENet model
without history performs better than the GAMENet model with history
at the moment, that tracking this additional metric will help prove
that the history is important by showing a degraded performance
in the drug count metric. I've tried to also replicate the DDI Rate
metric in a local branch, but so far my efforts have been
unsuccessful. I may try again after thinking through it a bit more,
but since it was relatively tricky to figure out for now I have
paused that effort.

* average drugs per visit

One suggestion from the project draft (progress report) was to include
details about how many drugs each model recommends on average per
visit. This is because one of the strengths of GAMENet is that it
tends to recommend a smaller set of drugs per visit, which helps
reduce the DDI Rate of the results as well. I wanted to include this
metric as another way to compare the models.

This commit has the logic for calculating that metric, and does so
for each experiment. The surprising thing to me is that the RETAIN
model seems to recommend less drugs than GAMENet for both included
tasks. I may want to revisit how exactly I am calculating this, since
it doesn't exactly match up with the experimental results from the
original paper (though admittedly it is close, so it may be correct).
I'm hoping this approach will also help me figure out the right way
to calculate the DDI Rate of each model as well.

I have also included the results of my most recent run in this commit
to keep a record of them. For example, it is worth noting that without
the patient history, the GAMENet model tends to recommend more drugs.

* ddi rate metric

I realized that my attempts at recreating the DDI Rate metric were
actually (somewhat) valid; my mistake was that I misread the DDI Rate
values in the original paper, and thought my results were a magnitude
off. Instead, they are fairly close to what is presented in the paper,
so I have added this calculated back so that I can print out the
DDI rate for each method (as well as the delta compared to the
base DDI rate of 0.0777). Strangely, it seems RETAIN recommends
fewer drugs than GAMENet on average in my implementation, which does
not correspond to what is seen in the paper (or in my original
reproduction done in the first PR of this repo). However, GAMENet
seems to consistently perform better in terms of metrics like
accuracy and DDI Rate.

Additionally, I have moved some functions around from the prior
commit as a bit of cleanup. Now the DDI Rate and the Average Drugs
per Visit metrics are calculated within the model wrapper itself.

Finally, I have added some more results from these DDI Rate runs.
As mentioned, the metrics do seem a bit strange at times so I may
continue investigating as time allows. However, the due date is
fast approaching so I may have to wrap this up soon and cut a release
for the final project submission. We will have to see how far I get
in the next day or so. I plan at least one more cleanup and
documentation related commit for this PR. Depending on time there
may be a few more commits -- such as one additional ablation if I
can get it working.

* procedure ablation

One of my planned ablations was to omit the procedure information
for patients to see how the various models would perform. This commit
includes both the task that prepares the drug task data without any
procedure codes, as well as an "alternative" GAMENet model that is
trained (and evaluated) on the data prepared without procedure codes.
This new model variant is called GAMENetNoProc for now, but I will
try to come up with a better name for it. This may also be where I
try to make a PR against pyhealth to provide some options to the
GAMENet model as far as whether to include procedure information
or not...but we will see.

The results here are fairly interesting. The number of drugs per
visit that were recommended in GAMENet was actually smaller on
average, but the DDI Rate was higher compared to the original
GAMENet implementation. I may try to run this again to see if that
is consistent. For now, I have included the results of my most recent
run, as well as the alt_gamenets.py file with the GAMENet variant
I described. The new drug recommendation task has also been included
in the drug_rec_task.py file, and the task has been added to the
list of allowed tasks for command line arguments.

Additionally, I made some minor updates to the README, including
documenting the flags that have been added to the script since the
last README update.

* gamenet with no hist

I realized that the ablation I tried to add for no history still
maintained a dynamic memory component within the GAMENet model, so
it likely was not working the way I expected it to. I have now added
another GAMENet variant, GAMENetNoHist, which removes the Dynamic
Memory component from the GAMENetLayer. The new layer here is called
GAMENetLayerNoDM. Previous drugs are not computed and are not sent
to the forward operation of this layer, so hypothetically now both
the data preparation and the GAMENet model should not account for
the history of the patient.

I have also made a few other edits. I tried to add a flattening task
to the drug_rec_tasks to make another ablation I had planned, but
I could not get this to work as expected. I think I will have to
skip this ablation for the sake of the project at least, as it is
a bit tricky to figure out for now.

Additionally, I have moved most of my constant values into a
constants.py file, which makes it easier when I want to make changes
that affect the entire logic -- such as adding a new task. Now, I
can just change values in the constants file (such as which task
corresponds to which model) in order to add or update certain
characteristics. I have also added timing metrics to each training,
so I can see how long it takes to train each model. Some results from
some of my runs have been added here as well.

* eda notebook

I've revised the EDA notebook. Now it is working again. This notebook
demonstrates the process of loading in the MIMIC data, performing
tasks on that data, and then training and evaluating the models on
that data. The final step is that it outputs the table of model
performance characteristics, which will be used in the final report
(with some minor revisions). The notebook still needs to be cleaned
up a bit, and some documentation and a 200 word summary still need
to be added. However, I am comitting it in this state as it is generally
where I want it to be. I may try to figure out if there are other
visualizations I can add in this notebook as well.

Additionally, I cleaned up some of the code from the previous commit.
For example, I have mode the training timing logic into the model
wrapper class itself, so that now it is automatically done on
training and can easily be stored and access later on when needed.
I also removed some comments and extraneous code.

* dev eda notebook and fix podman

I have finalized the EDA notebook to account for the requirements
for the Notebook bonus for the final project. Now, the notebook should
fulfill those requirements, such as containing a summary of the results
and of the entire reproduction study. For some reason, I could no
longer run the notebook with the full dataset. For now, I have just
run in dev mode to get sufficient outputs. There is still the previous
commit which contains the exact outputs with actual data which is
being used in my final report.

I also update the Dockerfile and the docker run script to enable the
changes I have made in this PR to also run in the containerization
framework I introduced previously. Now, the default behavior is for
the container to run all tasks when invoked. I will probably not
make this more fancy. The python script accepts command line arguments,
and the build_and_run script can be used to see the proper way to
pass command line arguments in to the python script. If it is easy,
I may try to add some command line arguments to the bash script.
But it seems unnecessary as I can just copy the commands and run
them manually with the proper flags if needed.

Finally, I removed some references to unused code lines, especially
with regards to the flat ablation which I was unable to get to work
successfully.

* fix strict models and final documentation

Previously, I only allowed very strict model classes to be passed
in as arguments to the ModelWrapper. I have made that more flexible,
and now I allow any object that is a subclass of GAMENet or RETAIN
to be passed in as the model type for the wrapper. This allows the
EDA notebook to work a bit better as well. The notebook has been
updated to reflect those changes.

Additionally, I added some final comments in the code to document
some of the aspects to make it easier to follow. I also updated the
README with a link to my video for the assignment.

---

