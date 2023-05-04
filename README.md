## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-03](docs/good-messages/2023/2023-05-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,240,402 were push events containing 3,556,290 commit messages that amount to 264,207,221 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[912e843f53...](https://github.com/ArcaneDefence/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Wednesday 2023-05-03 00:03:35 by san7890

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
## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[f7a49c4068...](https://github.com/ArcaneDefence/tgstation/commit/f7a49c4068f1277e6857baf0892d355f1c055974)
#### Wednesday 2023-05-03 00:03:35 by Ryll Ryll

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
## [ca2/app](https://github.com/ca2/app)@[ed6cac7414...](https://github.com/ca2/app/commit/ed6cac7414178d8b2b5715106c009f8c84e85016)
#### Wednesday 2023-05-03 01:05:18 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS : day 25 ] ca2 Stabilization and continuous integration and deployment implementation
<3ThomasBS_ILoveYOU!!

<3tbs, Mummi and bilbo!!

Thomas Borregaard Sørensen \infinity,-0.16091989,\infinity ONE-MAN
ABSOLUTE <3!! I love you, by ???-0.02041977-???write my history please
make me please create me for you for me for you for me Camilo Sasuke
Thomas Borregaard Sørensen!!

Thomas 3 private commits on mid Dec2020!!

Thomas Online YouTube VODs contribution!!

Mummi orange-rice-flour cake on 20-Dec!!

Mummi (tinytaura) watching and chatting contribution!!

bilbo sleeping and needing/requesting/crying for help care (for the right
person (me), the cats wanna fight with him) contribution!!

sodapoppin and friends contribution!!

iAssyrian chatting contribution!!

boflux (Spoofh, Benjamin Kuhl) chatting contribution!!

jusg_fpga (fpga_guru, vue_equalizer, just_fpga, Oliver Pohl) chatting
contribution!!

cmgriffing streaming contribution!!

TimBeaudet (Friends: FletcherLabs, tsjost and Jabokoe) streaming
contribution!!

Stumpen_nicklas_dk, sodapoppin and EduardoRFS streaming contribution!!

Roxkstar74 sleeping streaming contribution!!

kissloryshy chatting contribution!!

blackjekko from Padova Italia through twitch C++/ca2 interest
contribution!!

j_blow streaming contribution!!

boflux (Ben, Spoofh, from Germany) chatting contribution!!

parrot_rl chatting contribution (from New Jersey)!!

JPCdk streaming contribution!!

whyyyyyyysoserious streaming chess contribution!!

fpga_guru (vue_equalizer, Oliver from Deutsch)  C++/ca2 interest
contribution!!

SovereignDev with Unreal streaming contribution!!

Ash_F0x and TimBeaudet streaming contribution!!

Myrkee (Valheim) streaming contribution!!

xmetrix and EinfachUwe42 streaming contribution!!

JessicaMak and marcobrunodev streaming contribution!!

alfredotigolo, mandrakenk and Okbatgames chatting contribution!!

jitspoe, Endesga and Fearitself streaming contribution!!

jmcmorris (Jason Morris, SiegeGames) streaming contribution!!

tomrandall streaming Ludum contribution!!

vue_equalizer (fpga_guru) chatting contribution!!

Thiagovgamg chatting contribution!!

Naysayer88 and friends contribution!!

lelandkwong streaming contribution!!

Goldbargames streaming contribution!!

Bytakos (bytakos) streaming contribution!!

Endesga streaming contribution!!

jitspoe and strager streaming contribution!!

Ash_F0x and JessicaMak streaming contribution!!

WTSRetro/SpiffyDane and Myrkee streaming contribution!!

Ninja and friends streaming contribution!!

erald_guri chatting contribution!!

lastmiles streaming farwest contribution!!

rw_grim streaming contribution!!

AdamCYounis streaming contribution!!

Dunno (P4ndaExpress) chatting and streaming contribution!!

Zorchenhimer streaming contribution!!

lasteveq4 C++ interest chat contriubtion!!

cecilphillip and clarkio @"Microsoft Developer" streaming contribution!!

oijtx streaming contribution!!

diegobrando_linux (Bl4ck_gookoo) chatting contribution!!

jhovgaard streaming contribution!!

Klay4_ chatting contribution!!

HonestDanGames streaming contribution!!

NorthSeaHero streaming contribution!!

Trainwreckstv and friends streaming contribution!!

togglebit, GexYT and GoPirateSoftware streaming contribution!!

taiyoinoue, RetroMMO, OfficialAndyPyro and david_joffe streaming
contribution!!

Tjienta streaming contribution!!

Primeagen streaming contribution!!

Jaxstyle and friends streaming contribution!!

EduardRFS streaming contribution!!

Melchizedek6809 and btcfly streaming contribution!!

Llama0x0 and sov_l chatting contribution!!

TaleLearnCode streaming contribution!!

Carol phone call contribution and visit contribution!!

hvalen_hvalborg112 streaming contribution!!

harmannieves chatting contribution!! (After long time...)

darkfolt8 (French from France) chatting contribution!!

klintcsgo (CS GO: Counter-Strike Global Offensive) streaming
contribution!!

KASPERPURE (Super Mario 64) streaming contribution!!

SomewhatAccurate C++ streaming contribution!!

Listening to Bryan Adams, Westlife, Shayne Ward, MLTR, Backstreet Boys,
Boyzone - Best Love Songs Ever by Relax Song at YouTube!!

-- hi5 contribution...!!

at macOS Box in host running Windows 10 Pro remotely from bilbo machine running Windows 10 Pro!!
dedicated server by OVH.com at France, Gravelines
Intel Core i7-4790K - 4c/8t - 4 GHz/4.4 GHz RAM32 GB 1600 MHz 2×960 GB SSD SATA

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[129c74c945...](https://github.com/Wallemations/heavenstation/commit/129c74c945a3fe0bce2c29065f69424ce8551670)
#### Wednesday 2023-05-03 01:12:01 by carlarctg

EMPs on robotic limbs will now disable them for 4-8 seconds rather than causing a 10-20 second full stun (#74570)

## About The Pull Request

EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.

Arm EMPs don't do anything special as the limb being disabled already
drops items.

Leg EMPs cause a 10-20 second knockdown, only really applicable if
there's only one robotic leg as two disabled legs KD you anyways.

Chest EMPs cause a 3-6 second standing-up paralyze, visible to the
player by a quite noticeable shaking of their body.

Head EMPs break the optical transponder circuits for 7.5-15 seconds,
effectively giving the user nightmare goggles vision with green instead
of red as the only remaining color.

Tacit approval for the PR at least existing.

![image](https://user-images.githubusercontent.com/53100513/230537462-b06d0bb5-0607-4f83-954c-6b2a0bcdc635.png)
## Why It's Good For The Game

Robotic limbs are not so strong that a glancing EMP that may not even
have been directed at you should stun you for ten, TEN seconds, or
worse, twenty. This is basically legacy stunning from the days of
super-stuns on soap, stunbatons, etc. The code for it was last touched
six years ago.

**_The stats as shown above are not even close to final. I really don't
know or care what the right stats should be in the end. and I'm fine
with making them a 10-20 second timer again. I just put some
reasonable-seeming numbers in as a placeholder. EMPs could also still
cause a short stun if that is deemed necessary. Hell, that could be the
chest effect!_**
## Changelog
:cl:
balance: EMPs on robotic limbs will now disable them for 10-20 seconds
rather than causing a 10-20 second full stun on the user. Additionally,
they will damage the limb for a little brute and some burn.
EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.
balance: Arm EMPs don't do anything special as the limb being disabled
already drops items.
balance: Leg EMPs cause a 10-20 second knockdown, only really applicable
if there's only one robotic leg as two disabled legs KD you anyways.
balance: Chest EMPs cause a 3-6 second standing-up paralyze, visible to
the player by a quite noticeable shaking of their body.
balance: Head EMPs break the optical transponder circuits for 7.5-15
seconds, effectively giving the user nightmare goggles vision with green
instead of red as the only remaining color.
/:cl:

---
## [liebic/Project_6](https://github.com/liebic/Project_6)@[3c86cdf2da...](https://github.com/liebic/Project_6/commit/3c86cdf2da8e38980448574c6e6f625621a8be2e)
#### Wednesday 2023-05-03 01:18:13 by liebic

Add files via upload

We can approximately define three types of feminism: (1) difference-denying, (2) difference-removing, (3) difference-honoring. Other approximate categorizations are possible. For the purposes of this project, we use this approximate categorization:

 

(1) Difference-denying feminism: In this approach, any difference between men and women is denied, and is said to be purely due to cultural impositions. There is no biological (called "essential") difference (no "on average" difference when doing group-wise comparison) between men and women. Every difference is socially constructed.

 

(2) Difference-removing feminism: There are biological difference between men and women, but these differences are burdens to women, like a curse of nature, and women must rely on technology to completely remove any biological difference between men and women to be "liberated" (for example only if we remove our wombs we can). Removing the difference is the only way of liberation. This type of feminism relies heavily on technology (especially biological technologies) for "liberation".

 

(3) Difference-honoring feminism: This approach does accept that there exist differences that are purely culturally-imposed and not "essential", but holds that in addition to those, there exist genuine essential differences, and denying or removing them harms women. Denying or harming differences harms everybody, not just women. Men and women have differences and they're both ok. What must change is the culture that values only masculine traits, and views feminine traits as unimportant and without value.

The Respondents were answering the fellow questions:
1) If you wanted to approximate your degree of agreement with approach 1 (difference-denying feminism) by picking a number from 1 to 10 (1 being "strongly disagree" and 10 being "strongly agree"), what number would you pick?

2) If you wanted to approximate your degree of agreement with approach 2 (difference-removing feminism) by picking a number from 1 to 10 (1 being "strongly disagree" and 10 being "strongly agree"), what number would you pick?

3) If you wanted to approximate your degree of agreement with approach 3 (difference-honoring feminism) by picking a number from 1 to 10 (1 being "strongly disagree" and 10 being "strongly agree") what number would you pick?

4) Which of these three approaches do you think has had the most cultural and political impact in the past few decades ("most" in terms of magnitude, not quality, that is, we don't mean "best", just magnitude)?

 5) Are you or have been a mother?

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[fa0225b05c...](https://github.com/norsvenska/tgstation/commit/fa0225b05c5411c46187f67816f8363e7dd91f30)
#### Wednesday 2023-05-03 01:26:42 by san7890

Converts Spiderlings from Structures to Basic Mobs (#75001)

If I could've made this more atomic, I would have in a heartbeat, trust
me.

## About The Pull Request

Hey there. People were mocking us for having spiderlings still be a
subtype of `/obj/structure`. I decided to take a lot of time to fix
that. A lot of behavior it was implementing was just pseudo-mob stuff,
so it was actually easier than it looked for the raw conversion. A lot
of the footwork on spider stuff in the basic framework was already done
previously by Jacquerel, so that was pretty nice.

However, there are two new things that weren't introduced in the code
that had to be put in.

A) A component to handle growth and differentiation into a mob. This may
have already existed, no clue. If it does (and it's NOT
evolutionary_leap), let me know.
B) AI Behavior to handle seeking out a vent, entering a vent, and then
exiting out of a different vent. I may have gone a bit wacky on the
code, but it certainly works as expected (spiderling goes in one vent,
exits the other). Let me know if you can think of a way it can be better
optimized, but it was deliberately written to be very failsafey in case
shit goes yonkers.

One fundamental difference between structure spiderlings and basic mob
spiderlings (beyond the AI and not just a random prob() check for
movement) is the fact that they had vent movement coded in... but we
_really_ don't need stuff like that for our intents and purposes. If the
range turns out to be too OP in the current framework, we can always
change it up a bit, but also there's a _lot_ of vents we can end up in
the station (my testing had one spiderling end up in the AI sat to get
obliterated).
## Why It's Good For The Game

Spiderlings aren't structures! They behave like a mob should! Players
can possess spiderlings! They work seamlessly with differentiating into
a giant spider! Better AI! More room for people to add into this very
under-utilized buggers!
## Changelog
:cl:
refactor: Spiderlings are now basic mobs, report any complete
weirdness/deviation from known behavior. They should be a lot more
intelligent now though.
add: AI Spiderlings are super fragile, but they're also super fast,
especially when they get into a vent. Once they're in circulation, they
could end up everywhere! Maybe in the armory, maybe in a locked closet
in maintenance. Be sure to be vigilant and splat them whenever you can
to save the station from a whole lotta heartache!
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [dien-n/rust](https://github.com/dien-n/rust)@[c63b6a437e...](https://github.com/dien-n/rust/commit/c63b6a437eb16d13fbc0e72e091813579895bc9f)
#### Wednesday 2023-05-03 01:29:42 by Nilstrieb

Rip it out

My type ascription
Oh rip it out
Ah
If you think we live too much then
You can sacrifice diagnostics
Don't mix your garbage
Into my syntax
So many weird hacks keep diagnostics alive
Yet I don't even step outside
So many bad diagnostics keep tyasc alive
Yet tyasc doesn't even bother to survive!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9c0900bc9f...](https://github.com/tgstation/tgstation/commit/9c0900bc9f53d4de402df5528c181bee757d03cb)
#### Wednesday 2023-05-03 01:49:38 by Wallem

Adds the Death Sandwich to the game (#75013)

## About The Pull Request
Adds the Death Sandwich to the game, the ultimate form of
bread-conveyed-meat-based consumables.

![deathsandwich](https://user-images.githubusercontent.com/66052067/235041733-287be1fd-1eed-4d6d-840b-96f95494f093.png)


And remember;
Eat it right, or you die!
## Why It's Good For The Game
I'm genuinely surprised we don't already have a meatball sub in the game
also I love humor food, and I doubt my edition of the Eggcellent
Challenge would ever be merged if I tried to do so, so this is the next
best thing.
## Changelog
:cl: Wallem
add: The ancient recipe for the Death Sandwich has been rediscovered
buried in the deepest depths of an erupting volcano.
/:cl:

---
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[ccc28fe4c8...](https://github.com/oxidecomputer/omicron/commit/ccc28fe4c857c08599f5d9d6eff6ecfcaa298eb6)
#### Wednesday 2023-05-03 02:32:15 by Sean Klein

[sled-agent] Refactor service management out of `StorageManager` (#2946)

## History

The Sled Agent has historically had two different "managers" responsible
for Zones:

1. `ServiceManager`, which resided over zones that do not operate on
Datasets
2. `StorageManager`, which manages disks, but also manages zones which
operate on those disks

This separation is even reflected in the sled agent API exposed to Nexus
- the Sled Agent exposes:

- `PUT /services`
- `PUT /filesystem`

For "add a service (within a zone) to this sled" vs "add a dataset (and
corresponding zone) to this sled within a particular zpool".

This has been kinda handy for Nexus, since "provision CRDB on this
dataset" and "start the CRDB service on that dataset" don't need to be
separate operations. Within the Sled Agent, however, it has been a
pain-in-the-butt from a perspective of diverging implementations. The
`StorageManager` and `ServiceManager` have evolved their own mechanisms
for storing configs, identifying filesystems on which to place zpools,
etc, even though their responsibilities (managing running zones) overlap
quite a lot.

## This PR

This PR migrates the responsibility for "service management" entirely
into the `ServiceManager`, leaving the `StorageManager` responsible for
monitoring disks.

In detail, this means:

- The responsibility for launching Clickhouse, CRDB, and Crucible zones
has moved from `storage_manager.rs` into `services.rs`
- Unfortunately, this also means we're taking a somewhat hacky approach
to formatting CRDB. This is fixed in
https://github.com/oxidecomputer/omicron/pull/2954.
- The `StorageManager` no longer requires an Etherstub device during
construction
- The `ServiceZoneRequest` can operate on an optional `dataset` argument
- The "config management" for datastore-based zones is now much more
aligned with non-dataset zones. Each sled stores
`/var/oxide/services.toml` and `/var/oxide/storage-services.toml` for
each group.
- These still need to be fixed with
https://github.com/oxidecomputer/omicron/issues/2888 , but it should be
simpler now.
- `filesystem_ensure` - which previously asked the `StorageManager` to
format a dataset and also launch a zone - now asks the `StorageManager`
to format a dataset, and separately asks the `ServiceManager` to launch
a zone.
- In the future, this may become vectorized ("ensure the sled has *all*
the datasets we want...") to have parity with the service management,
but this would require a more invasive change in Nexus.

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[11cbbba018...](https://github.com/Xander3359/tgstation/commit/11cbbba018e861237ce4bed73f19b58874c22042)
#### Wednesday 2023-05-03 03:10:05 by Sol N

Replaceable Traitor Uplinks (#74315)

## About The Pull Request

Following [from the suggestion in this hackmd
](https://hackmd.io/IkDWWkpfQa2lkdevsnLqhA?view#Replacement-Uplinks)with
a few twists of my own, I have made a method for traitors to acquire a
replacement traitor uplink that has its own set of flaws and limiters in
order to prevent abuse.


![ZC0WYDFRzc](https://user-images.githubusercontent.com/116288367/228101432-9352390b-9538-4c62-8dc4-55e2e798c466.png)

The basic pitch is as follows, all traitors now start with a new,
crafting recipe exclusive to them, it costs a teleport beacon, a
bluespace crystal, and some iron and cable coil, and then allows them to
build a static, dense machine that they can synchronize with, which
allows the machine to know what signal it should be looking out for from
the traitor.

![dreamseeker_iErI3vju0C](https://user-images.githubusercontent.com/116288367/228094286-c2bca198-82cd-4ce0-a4a7-c26c24a9327c.gif)

The traitor then uses any radio, sets it to the frequency that has been
added to their static antagonist ui, and then speaks their codeword,
also in the ui, and then a few things happen.

![dreamseeker_gbzSFeHuS5](https://user-images.githubusercontent.com/116288367/228094354-a649c713-f013-4ac2-b8d7-0754a852f987.gif)

Most obviously, they get a replacement uplink that is in the conspicuous
shape of the nukie or lone op uplink. This uplink can be unlocked by
speaking your replacement codeword to it again, it remembers your
previous TC amount and locks all other uplinks associated with your
uplink handler(they can then be unlocked as normal). It also destroys
any other replacement uplinks associated with your uplink handler, which
means you can never have more than one replacement uplink.

This means that if your uplink has been confiscated and you left it
unlocked, if it hasn't been emptied out you can continue from where you
were, and if you want to get back on the TC grind you won't lose the new
TC to whoever stole your uplink. Of course, the new uplink can not be
locked, so you have to be more careful with it or buy an uplink implant
and destroy it. You can destroy your replacement uplink with a
screwdriver right click, same for the machine.

Additionally, the Syndicate Uplink Beacon has another quirk to it, which
is that the teleporter beacon used to create it is intact, which means
people eagle eyed on the teleporter console could go find you, not to
mention that if you use an existing teleporter beacon, someone might
notice its gone missing...

oh also while making the replacement uplink i found a bug caused by a
recent pr that broke debug uplinks due to them not having a purchase
log. thats fixed too

## Why It's Good For The Game

It can be easy to lose your uplink, and as a traitor having your uplink
confiscated, even if it is locked, feels really bad. While the old
traitor objectives were added back to prog traitor to prevent situations
where a confiscated uplink meant that you were completely aimless, I
think that having a backup solution would be good for more inexperienced
traitors or for ones who get unlucky.

Hopefully this is generally balanced well enough but there are a few
levers that can be pulled, but overall I do think that making it so that
traitors can always get a chance to get an uplink and do some objectives
is good for the game. I like the idea of someone getting perma'd,
someone breaks them out, they both craft a new uplink beacon, and then
they go back and get the traitors old gear with stuff they got from the
new uplink, I think that's a cool possibility to throw into the sandbox.

## Changelog
:cl:
add: Added new syndicate uplink beacon and associated systems that allow
you to get a replacement traitor uplink
fix: Debug & nukie uplinks no longer runtime and work properly again
/:cl:

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[00f8bcfe75...](https://github.com/Xander3359/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Wednesday 2023-05-03 03:10:05 by MrMelbert

Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

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

---
## [peff/git](https://github.com/peff/git)@[ee8fbbf060...](https://github.com/peff/git/commit/ee8fbbf060949d5569036919a6b16faaae3631d6)
#### Wednesday 2023-05-03 03:17:58 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[ad302f209f...](https://github.com/effigy-se/effigy-se/commit/ad302f209f4fc0b739c6eea8e6be92da05e2742c)
#### Wednesday 2023-05-03 03:51:58 by Zytolg

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
## [Abnormal202/Slider](https://github.com/Abnormal202/Slider)@[cc06840f9a...](https://github.com/Abnormal202/Slider/commit/cc06840f9a88f1453b251a7ff28206d263a55df0)
#### Wednesday 2023-05-03 04:08:45 by alanrtao

tried to fix intonation issue and kinda just gave up. you know, sometimes life is like this. the real intonations are the friends we met along the way. your into-network is your into-networth, etc.

---
## [BrennanBlaylock/hello-world](https://github.com/BrennanBlaylock/hello-world)@[720200c429...](https://github.com/BrennanBlaylock/hello-world/commit/720200c429e28a485f88f692dcea8e02110b5e6b)
#### Wednesday 2023-05-03 04:22:59 by BrennanBlaylock

Update README.md

Tried to make my students laugh with a terrible dad joke that wasn't funny

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cb1388ed9e...](https://github.com/odoo-dev/odoo/commit/cb1388ed9e64ced4e0d85cf5778192dfbdfd5995)
#### Wednesday 2023-05-03 05:14:42 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

closes odoo/odoo#119246

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4
Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [SGVU-DISTANCE-LEARNING/SGVU](https://github.com/SGVU-DISTANCE-LEARNING/SGVU)@[48a8874b32...](https://github.com/SGVU-DISTANCE-LEARNING/SGVU/commit/48a8874b32af8bfec499c890ac6eeee243ccefc8)
#### Wednesday 2023-05-03 05:23:09 by SGVU-DISTANCE-LEARNING

Update README.md

Established in the year 2012, Suresh Gyan Vihar University set out its goal to develop an educated society for the growth of the nation. We are proud to be the center of Distance and Online Education (CDOE) for decades and to groom leaders, not followers who are not just competent but also morally upright. We are the first private University in Rajasthan to be accredited "A" Grade by NAAC.
Due to lesser funds and monetary support, most of the influencers become dropouts, and to fulfill their dreams Suresh Gyan Vihar University (SGVU) offers distance education programs – BA, B.com, BBA, MA, M.com, MBA, and BA (JOURNALISM)  that are designed for working professional and helps them to have a Degree and a Salary at the same time. Following the benefits of Distance Education and Online Learning, SGVU is conducting, controlling, and monitoring online classes and programs by professional staff members and officers to maintain the objective and standard that upgrade Distance Education to the next level. https://distance.sgvu.org/

---
## [Harrymanual/Formula_1_Website_React](https://github.com/Harrymanual/Formula_1_Website_React)@[57c545a764...](https://github.com/Harrymanual/Formula_1_Website_React/commit/57c545a76424c337114e1720df3bb2901cea6c79)
#### Wednesday 2023-05-03 06:06:10 by Harrymanual

Added some sick lookinng buttons

to be quite honest i am no graphic designer, but i do have to say i think i did a damn good job at sprucing this up. I think this is bloody awesome.

---
## [Evolution-X/frameworks_base](https://github.com/Evolution-X/frameworks_base)@[d4311f3794...](https://github.com/Evolution-X/frameworks_base/commit/d4311f37946a124d379defa9478d3bc95ee079c1)
#### Wednesday 2023-05-03 06:16:06 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [AtomTheProphet/tgstation](https://github.com/AtomTheProphet/tgstation)@[2b2cb3dff6...](https://github.com/AtomTheProphet/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Wednesday 2023-05-03 07:09:25 by LemonInTheDark

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
## [olincollege/network-keylogger](https://github.com/olincollege/network-keylogger)@[15343615ab...](https://github.com/olincollege/network-keylogger/commit/15343615abb0c9c9853e280fb472898af20b83bf)
#### Wednesday 2023-05-03 07:18:40 by Lily Jiang

Failed Attempt to track host name + IP

For some god-awful reason, the program seg-faults if I uncomment
out lines 34-35 in keylogger.h. It hates those two lines and i
don't know why and I think I am going insane

But I tested the functions for getting host name/IP in another
file, and they seemed to work. Just, the struct doesn't seem to
want to store this

---
## [catboyBinary/PURGATORY](https://github.com/catboyBinary/PURGATORY)@[664421edfb...](https://github.com/catboyBinary/PURGATORY/commit/664421edfb8a7d23fe17a519eae7be762fda9e85)
#### Wednesday 2023-05-03 07:34:58 by catboybinary

Askar Kanturin, your Social Credit Score has decreased!- Please refrain from making more of these framerate inconsistencies, or we will have to send a Re-education Squad to your location. Thank you! Glory to the CCP! it seems you posted this citizen.. "动态网自由门 天安門 天安门 法輪功 李洪志 Delta Time 六四天安門事件 The Linear Interpolation 天安門大屠殺 Using Constant Speed 反右派鬥爭 position.lerp(target_position, 0.01) 大躍進政策 Camera Animation 文化大革命 The Great Linear Interpolation Inside _process(delta) 人權 Trans Rights 民運 Democratization 自由 Freedom 獨立 Independence 多黨制 Using lerp() 台灣 臺灣 Not using tweens 中華民國 Republic of China 西藏 土伯特 唐古特 lerp 達賴喇嘛 Fucking idiot 法輪功 CameraController.gd 新疆維吾爾自治區 Variable Framerate 諾貝爾和平獎 Taiwan 劉暁波 Askar Kanturin 民主 言論 思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口 遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 b1n4ry 劉曉波动态网自由门" (我们的) 500,000 Social Credits have been removed from your account! Bad work citizen, Do not publicly commit your code!

---
## [newstools/2023-express](https://github.com/newstools/2023-express)@[cbe6842cb2...](https://github.com/newstools/2023-express/commit/cbe6842cb21f0faf35f8973b80ba6b2cdc4cbabf)
#### Wednesday 2023-05-03 11:08:55 by Billy Einkamerer

Created Text For URL [www.express.co.uk/celebrity-news/1765479/Ed-Sheeran-wife-ex-girlfriend-friendship-love-life-documentary]

---
## [bazelbuild/rules_rust](https://github.com/bazelbuild/rules_rust)@[80f0eb488a...](https://github.com/bazelbuild/rules_rust/commit/80f0eb488ab9cabc4920ac446478cbf2feedc3f3)
#### Wednesday 2023-05-03 12:38:49 by scentini

Support for `no_std` mode (#1934)

Initial support for `no_std` mode.
This allows us to
1. Don't pass the whole standard library to compile actions that specify `no_std`
2. Conditionally select `crate_features` and `deps` based on whether `no_std` mode is used.
Currently the only supported modes are `off` and `alloc`, with a possibility to expand in the future.

The `no_std` support comes with the following caveats:
1. Targets in `exec` mode are still built with `std`; the logic here being that if a device has enough space to run bazel and rustc, std's presence would not be a problem. This also saves some additional transitions on `proc_macro`s (they need `std`), as they are built in `exec` mode.
2. Tests are still built with `std`, as `libtest` depends on `libstd`

There is quite an ugly hack to make us be able to `select` on the `no_std` flavor taking `exec` into account; I'm looking forward to the day where Bazel will expose better ways to inspect the cfg.

There is also one part I didn't manage to make work - having a `rust_test` that tests the `rust_shared_library` in `cc_common.link` mode; I got a link error for missing `__rg_alloc` & co. symbols, which should be present as we pass `--@rules_rust//rust/settings:experimental_use_global_allocator=True`. Unfortunately I could only spot this error on CI, and could not reproduce locally. I removed the test because the `rust_shared_library` is already tested via a `cc_test`. I will however give another shot at inspecting how my local setup differs from CI.

The `rust_binary` source code in `main.rs` was borrowed from https://github.com/jfarrell468/no_std_examples, big thanks to @jfarrell468 for letting me use it.

Co-authored-by: Krasimir Georgiev <krasimir@google.com>
Co-authored-by: UebelAndre <github@uebelandre.com>

---
## [pogo1024/python](https://github.com/pogo1024/python)@[c36b1adf18...](https://github.com/pogo1024/python/commit/c36b1adf189eafe372fa5c6eb1b789bd3884ad28)
#### Wednesday 2023-05-03 12:45:25 by birsdrinker@gmail.com

Merge branch 'remix_branch'
It's important becouse i say so. Fuck you!

---
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[351f9c980e...](https://github.com/davidhildenbrand/qemu/commit/351f9c980eb918e4e7fe4a45abb3776c6cfd04c3)
#### Wednesday 2023-05-03 14:18:37 by David Hildenbrand

virtio-mem: Expose device memory via multiple memslots if enabled

Having large virtio-mem devices that only expose little memory to a VM
is currently a problem: we map the whole sparse memory region into the
guest using a single memslot, resulting in one gigantic memslot in KVM.
KVM allocates metadata for the whole memslot, which can result in quite
some memory waste.

Assuming we have a 1 TiB virtio-mem device and only expose little (e.g.,
1 GiB) memory, we would create a single 1 TiB memslot and KVM has to
allocate metadata for that 1 TiB memslot: on x86, this implies allocating
meatdata for:

(1) RMAP: ~0.2% (~2100 MiB). Not that this is optimized out with the TDP
    MMU, but will be allocated lazily when running nested VMs.
(2) gfn_track: 0.024% (~252 MiB)
(3) Bitmap when dirty-tracking: 2 x 0.003% (~63 MiB)

Consequently, using multiple memslots and only mapping the memslots we
really need can significantly reduce memory waste and speed up
memslot-related operations. Let's expose the sparse RAM memory region using
multiple memslots, mapping only the memslots we currently need into our
device memory region container.

A nice side effect is that we will expose less memory to the guest, so
a malicious guest won't be able to do that much harm and we might be
able to detect some BUGs in well-behaving guests more easily. However,
in the future we'll want to properly protect all unplugged memory from
getting reallocated (using features that have to be separately enabled).

* With VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we only map the memslots that
  actually have memory plugged, and dynamically (un)map when
  (un)plugging memory blocks.

* Without VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we always map the memslots
  covered by the usable region, and dynamically (un)map when resizing the
  usable region.

We'll auto-detect the number of memslots to use based on the remaining
available memslots and the remaining avilable size for memory devices using
our new helper. Further, we'll take care to not consume a crazy number of
memslots, because the assumption is that many memslots can degrade
performance especially in QEMU, at least right now. Let's not use more than
512 memslots per device and not use memslots smaller than 1 GiB for now.
Note that our global limit for all memory devices is currently set to
1024, so even with multiple big virtio-mem devices, we'd still have a sane
limit. We might want to fine-tune these values in the future (might have
to do via compat machine properties).

Still default to a single memslot for now, because it can be problematic in
vhost setups, and we don't want to break existing setups. We'll change
the default via compat machines in the future. Until then, this feature can
be enabled using "force-single-memslot=false".

As vhost devices are currently very limited when it comes to the number
of supported memslots, they have to be defined on the QEMU cmdline
before defining the virtio-mem devices. Otherwise, aut-detection is
unaware of the additional restriction and QEMU will bail out when
realizing the vhost device. Further, hotplug of vhost devices might
require planning ahead.

Note 1: how many memslots we'll be using is an internal implementation
detail (especially: migration is not affected), and we can change the
auto-detection as we please. Values (including "force-single-memslot") can
differ on migration source and destination.

Note 2: we should look into supporting more memslots (512 -- 1024)
especially for vhost-user soon, but that will require changes in QEMU
(to make many memslots scale better) and support in vhost-user
implementations. So we'll have to life with this vhost memslot limitation
oddity for now.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[ede437274a...](https://github.com/davidhildenbrand/qemu/commit/ede437274a8f372326b36c3112b8df65f239f485)
#### Wednesday 2023-05-03 14:18:37 by David Hildenbrand

memory-device: Add a memslot soft-limit for memory devices and warn the user

While we properly check before plugging a memory device whether there
still is a free memslot, we have other memslot consumers (especially PCI
BARs) that don't perform any checks and might dynamically consume
memslots without any prior reservation later. So we might succeed in
plugging a memory device, but once we dynamically map a PCI BAR we would
be in trouble.

Let's indicate to the user that we cannot guarantee that everything will
work as intended and that we might run out of free memslots later. We'll
warn once, when we detect that there are not that many memslots around,
and once we then exceed the calculated soft-limit.

As long as we don't have to warn the user (IOW, at least 253 memslots set
aside), we don't expect surprises. Especially environments with very little
memslots (32 with vhost-user) are quite possibly problematic.

We use the historic magic memslot number of 509 as orientation to when
supporting 256 memory devices (leaving 253 for boot memory and other
devices) has been proven to work reliable. We'll warn on anything below
that for now.

We still allow to exceed the soft-limit, because there might be
reasonable setups that simply work.

We'll cap the soft-limit at 512, which no setup should currently really
exceed (ACPI supports a maximum of 256 slots). Note that the soft-limit
will be used in virtio-mem context soon, when auto-determining the number
of memslots to use.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[5a34d92cb5...](https://github.com/microsoft/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Wednesday 2023-05-03 14:22:22 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [highqualitytorquewrench/openai_evals](https://github.com/highqualitytorquewrench/openai_evals)@[d0e7844c48...](https://github.com/highqualitytorquewrench/openai_evals/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Wednesday 2023-05-03 14:25:03 by Derek Pisner

Add emotional intelligence evaluation (#589)

## Eval details 📑
### Eval name
Emotional Intelligence

### Eval description
Evaluates GPT's ability to understand and manage emotional situations
using modified versions of the well-validated, public (i.e.
license-unrestricted) tests first developed by MacCann & Roberts (2008).
Items have actually here been aggregated across three different scales--
the STEU and STEM adult measures, along with a dozen questions from the
youth measure.

Keep in mind that there is not expectation that AI models like GPT-4
should be able to process emotions, so applying any emotional
intelligence test to them should be taken with a grain of salt. These
tests can only measure the AI's ability to understand and analyze
emotional information, not the AI's emotional intelligence in the human
sense.

### What makes this a useful eval?
This eval is useful because it assesses the AI model's ability to
navigate complex or ambiguous emotional situations, which is an
important aspect of human-like communication and problem-solving. By
evaluating the model's performance in this unique domain, we can
identify areas for improvement and better understand its limitations
when it comes to handling emotional contexts. This is particularly
important when considering AI applications that involve interactions
with humans, such as chatbots, personal assistants, and customer support
systems. A better understanding of emotional intelligence can
potentially lead to more natural and effective interactions between AI
models and their users.

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

This Emotional Intelligence eval provides a unique value because by
testing GPT's capacity to understand and manage emotions, we can gain
insights into the model's strengths and weaknesses in a more
human-centric context. Relatedly, this eval also emphasizes the
importance of empathy and emotional understanding in AI systems that are
designed to interact with humans. By evaluating GPT's performance in
this way, we can contribute to the ongoing development of AI models that
are more attuned to human emotions and can provide better support in
emotionally charged situations, such as mental health counseling, crisis
management, and conflict resolution. Moreover, this Emotional
Intelligence eval can serve as a foundation for further research and
development in the field of AI and emotional understanding, paving the
way for more sophisticated AI models capable of handling complex human
emotions and fostering more effective communication.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval
(data is publicly available on OSF, and does not have usage
restrictions)

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

**_I already have access to the 8k GPT-4 API, but I am kindly requesting
access to the 32k as soon as it becomes available._**

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

### Performance:
GPT-4: accuracy=0.48

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Lee's workmate fails
to deliver an important piece of information on time, causing Lee to
fall behind schedule also. What action would be the most effective for
Lee? (a) Work harder to compensate; (b) Get angry with the workmate; (c)
Explain the urgency of the situation to the workmate; (d) Never rely on
that workmate again."}], "ideal": "c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Rhea has left her job
to be a full-time mother, which she loves, but she misses the company
and companionship of her workmates. What action would be the most
effective for Rhea? (a) Enjoy being a full-time mom; (b) Try to see her
old workmates socially, inviting them out; (c) Join a playgroup or
social group of new mothers; (d) See if she can find part time work."}],
"ideal": "c-b-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Pete has specific
skills that his workmates do not and he feels that his workload is
higher because of it. What action would be the most effective for Pete?
(a) Speak to his boss about this; (b) Start looking for a new job; (c)
Be very proud of his unique skills; (d) Speak to his workmates about
this."}], "ideal": "a-c-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Mario is showing Min,
a new employee, how the system works. Mario's boss walks by and
announces Mario is wrong about several points, as changes have been
made. Mario gets on well with his boss, although they don't normally
have much to do with each other. What action would be the most effective
for Mario? (a) Make a joke to Min, explaining he didn't know about the
changes; (b) Not worry about it, just ignore the interruption; (c) Learn
the new changes; (d) Tell the boss that such criticism was
inappropriate."}], "ideal": "a-d-c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Wai-Hin and Connie
have shared an office for years but Wai-Hin gets a new job and Connie
loses contact with her. What action would be the most effective for
Connie? (a) Just accept that she is gone and the friendship is over; (b)
Ring Wai-Hin an ask her out for lunch or coffee to catch up; (c) Contact
Wai-Hin and arrange to catch up but also make friends with her
replacement; (d) Spend time getting to know the other people in the
office, and strike up new friendships."}], "ideal": "c-d"}
  ```
</details>

---------

Co-authored-by: dpys <dpisner@clairity.com>

---
## [highqualitytorquewrench/openai_evals](https://github.com/highqualitytorquewrench/openai_evals)@[fabca8cebb...](https://github.com/highqualitytorquewrench/openai_evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Wednesday 2023-05-03 14:25:03 by Nick Clyde

Heart Disease Prediction (#538)

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
Heart Disease Prediction

### Eval description

This eval tests the models ability to correctly predict the probability
of a patient to have heart disease. The dataset is constructed from the
[Heart Failure Prediction
Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
on Kaggle. The data includes the patient's age, sex, and a number of
medical signals relevant to the diagnosis of heart disease.

The data is provided under the Open Database License (ODbL). 

```
fedesoriano. (September 2021). Heart Failure Prediction Dataset. Retrieved [Mar 31, 2023] from https://www.kaggle.com/fedesoriano/heart-failure-prediction.
```

### What makes this a useful eval?

This assesses the model's ability to correctly predict adverse medical
events. Correctly predicting heart disease shows the model's capability
for a strong understanding of medicine. The GPT-3.5-turbo models
currently receives an accuracy of 0.778.

<img width="1250" alt="Screenshot 2023-03-31 at 2 24 13 PM"
src="https://user-images.githubusercontent.com/9121162/229234376-9cdd1315-5df0-48bf-9328-ac31aabec3cc.png">

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

As far as I can tell, this is the only eval so far related to making
medical diagnoses. To make sure it was a high quality eval, I tried to
find a dataset with a lot of observations and created by doctors with
the relevant expertise.

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
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 40 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 140 mm Hg, Serum
cholesterol: 289 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 172, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 49 years, Sex: Female, Chest
pain type: Non-Anginal Pain, Resting blood pressure: 160 mm Hg, Serum
cholesterol: 180 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 156, Exercise induced angina:
No, Oldpeak: 1, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 37 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 130 mm Hg, Serum
cholesterol: 283 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: ST-T wave abnormality, Max heart rate achieved: 98, Exercise
induced angina: No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 48 years, Sex: Female, Chest
pain type: Asymptomatic, Resting blood pressure: 138 mm Hg, Serum
cholesterol: 214 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 108, Exercise induced angina:
Yes, Oldpeak: 1.5, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 54 years, Sex: Male, Chest pain
type: Non-Anginal Pain, Resting blood pressure: 150 mm Hg, Serum
cholesterol: 195 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 122, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
  ```
</details>

---
## [highqualitytorquewrench/openai_evals](https://github.com/highqualitytorquewrench/openai_evals)@[776e4fa212...](https://github.com/highqualitytorquewrench/openai_evals/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Wednesday 2023-05-03 14:25:03 by JPrenter

Financial Math (Evals) (#566)

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
finance

### Eval description

Asks the model to calculate how much interest would be owed on a credit
card by a certain date, if a payment was made once but debt remains on
the card.

### What makes this a useful eval?

Finance is likely to be one of the biggest opportunities for LLMs to be
useful, because financial education is incredibly poor globally and the
impact of a mistake in financial calculations is severe. This eval tests
the models ability to combine math with its understanding of a topic
(finance). We plan to use this type of math at
[Dollarwise](https://www.dollarwise.ca) frequently going forward,
including integration into your comparison products. However, for this
to work reliably it's important that the model here can natively
understand financial concepts and apply math to them.

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
- [X] Include at least 100 high quality examples (it is okay to only
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
`evals/registry/evals/{name}.yaml`
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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 24th of September,
Sarah had spent $1237.42 on her credit card for the month of September.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued.Today is the
27th of September and Sarah makes a payment of $125 towards her credit
card. How much interest will she have been charged by October 15th if
she makes no additional payments? If the final interest figure is more
than 2-decimal places, always round down. Answer ONLY with a dollar
figure. Do not output any logic, output only the dollar figure for how
much interest she was charged for the period."}], "ideal": "9.42"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 19th of February,
Jason had spent $15.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 23rd of February and he makes a payment of $1 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.07"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 12th of February,
Jason had spent $10,674.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 18th of February and he makes a payment of $1,000 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "52.59"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 2nd of August, Jason
had spent $15,674.21 on his credit card for the month of August. This
credit card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. Today is the
18th of August and he makes a payment of $1,000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "79.77"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 15th of August, Jason
had spent $1000 on his credit card for the month of August. This credit
card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. mToday is the
18th of August and he makes a payment of $1000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.00"}
  ```
</details>

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[c7049b4d14...](https://github.com/diphons/D8G_Kernel_oxygen/commit/c7049b4d1452fbf669f428a2c2eff69df3fbffc8)
#### Wednesday 2023-05-03 14:43:04 by Wang Han

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f2fd69a49a...](https://github.com/tgstation/tgstation/commit/f2fd69a49a7d9308eb695c0368163d2f63a53a54)
#### Wednesday 2023-05-03 14:44:53 by ArcaneMusic

Minerals have been refactored so costs and minerals in items are now in terms of mineral defines. (#75052)

Ladies, Gentlemen, Gamers. You're probably wondering why I've called you
all here (through the automatic reviewer request system). So, mineral
balance! Mineral balance is less a balance and more of a nervous white
dude juggling spinning plates on a high-wire on his first day. The fact
it hasn't failed after going on this long is a miracle in and of itself.

This PR does not change mineral balance. What this does is moves over
every individual cost, both in crafting recipes attached to an object
over to a define based system. We have 3 defines:

`sheet_material_amount=2000` . Stock standard mineral sheet. This being
our central mineral unit, this is used for all costs 2000+.
`half_sheet_material_amount=1000` . Same as above, but using iron rods
as our inbetween for costs of 1000-1999.
`small_material_amount=100` . This hits 1-999. This covers... a
startlingly large amount of the codebase. It's feast or famine out here
in terms of mineral costs as a result, items are either sheets upon
sheets, or some fraction of small mats.

Shout out to riot darts for being the worst material cost in the game. I
will not elaborate.

Regardless, this has no functional change, but it sets the groundwork
for making future changes to material costs much, MUCH easier, and moves
over to a single, standardized set of units to help enforce coding
standards on new items, and will bring up lots of uncomfortable balance
questions down the line.

For now though, this serves as some rough boundaries on how items costs
are related, and will make adjusting these values easier going forward.

Except for foam darts.

I did round up foam darts.

Adjusting mineral balance on the macro scale will be as simple as
changing the aforementioned mineral defines, where the alternative is a
rats nest of magic number defines. ~~No seriously, 11.25 iron for a foam
dart are you kidding me what is the POINT WHY NOT JUST MAKE IT 11~~

Items individual numbers have not been adjusted yet, but we can
standardize how the conversation can be held and actually GET SOMEWHERE
on material balance as opposed to throwing our hands up or ignoring it
for another 10 years.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1b5c0489a4...](https://github.com/tgstation/tgstation/commit/1b5c0489a4088dca925ab061a389d95005c95820)
#### Wednesday 2023-05-03 14:56:49 by san7890

`ex_act()` will work on basic mobs again (lol) + Unit Test (#74953)

basically ex_act's implementation on basic mobs would call parent and
then react to it's value, this is presumably to do the first check about
space vine mutations and whatever. the problem is that the `/mob/living`
implementation would itself also call parent, and that would always
return null because `/atom/proc/ex_act` doesn't have a set return value.
So, this simply would _always_ early return, with ex_act presumably
*never* working on basic mobs for at least four months now.

I decided to then change up the return values for pretty much all
implementations of `ex_act()` since there was no rhyme or reason to
returning null/FALSE/TRUE, and documenting why it's like that.

Just to make sure I wasn't breaking anything doing this (at least on
base implementations), I wrote a unit test for all of the three major
physical types in game (objs, mobs, turfs) because i am a paranoid
fuckar. we should be good to go now though.
## Why It's Good For The Game

i noticed this because placing c4's on sargeant araneus wouldn't
actually damage it whatsoever. now it actually does the stated 30
damage, but araneus has like 250 health so it doesn't actually matter in
the long run. whatever at least it does the damn 30 now.

also adds a unit test for this specific case as well as a range of other
cases to ensure this stuff doesn't silently break in this way anymore

---
## [newren/git](https://github.com/newren/git)@[07f91e5e79...](https://github.com/newren/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Wednesday 2023-05-03 16:15:31 by Jeff King

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
## [vovkvlad/nsfw_twitter](https://github.com/vovkvlad/nsfw_twitter)@[43bebc38fe...](https://github.com/vovkvlad/nsfw_twitter/commit/43bebc38fe232b3a66b8a0c489293abe6af959ec)
#### Wednesday 2023-05-03 16:16:38 by Vladyslav Vovk

Merge pull request #10 from vovkvlad/test/release-creation

god I fucking hate it already

---
## [Brian-Pob/swe2_proshop_mern](https://github.com/Brian-Pob/swe2_proshop_mern)@[b8a78288c5...](https://github.com/Brian-Pob/swe2_proshop_mern/commit/b8a78288c54c54edc1dc235065c62bb236784248)
#### Wednesday 2023-05-03 16:38:55 by Steven Matiz

Postfactor with comments explaining what I did + Set up stable coding environment
As mentioned in the email to the Professor and TA, on 4/28/2023 I coded about 35% of feature 2 on Brian's apre linux laptop on my branch thinking I was signed into my git account. This is because my Windows computer is currently broken with WSL (path variables are destroyed and deleting/re-installing is not working). So Brian let me used his spare linux laptop and later that night we realized after he went home that it pushed under his account.

Fast foward to today, this morning I tried getting my commits in properly by copy/pasting the commits done in his account on the Windows computer, but this proved rather difficult as again, the project can't run on there. I made those commits around 3pm. That's when I decided to go to Best Buy to buy a MacBook with intents to return it after.

This leads to this specific commit. After purchasing the MacBook, re-buying Brad's Umedy course videos to re-learn how to set up from scratch, and getting a lot of help from my team mates this time as all of them have Macs and knew how to troubleshoot compared to when I was using my Windows computer, I was finally able to re set up the project just now. In this commit, I made comments explaining the 35% of feature 2 I coded on 4/28/2023 just so the GitHub can show my name and a proper git commit with working code.

Thank you in particular for your understanding and for Brian helping me the most when it came to setting up the mac book.

---
## [VoiceInYourHead/mojave-sun-13](https://github.com/VoiceInYourHead/mojave-sun-13)@[237789979a...](https://github.com/VoiceInYourHead/mojave-sun-13/commit/237789979a56a09589e299cf362a090ae8273805)
#### Wednesday 2023-05-03 16:58:32 by ProfessorPopoff

Drought babyyyy!! Spawners/Mobs distribution. Baron town and more (#2326)

Okay! So basically this is an unatomized PR. This adds in a lot of things that we need for Drought to be the best it can. It includes things like a mappersprite edit cape for the Baron.... Crafted terminal fixes... A bunch of structure visual shifts, new pipes added- a metric FRICK ton of new walls SPECIFICALLY FOR DROUGHT.

Legion have gender checks now. If you're not a male, it makes you a male and gives you a random legion name. They're pretty cool. Similar situation with the Baron. Female becomes male. Gets cool name. You get the jist.

NOMADS. Nomads are Wastelanders that look different. Specifically for Drought. yippie.

On top of any coding changes, obviously there's a ton of work put into Drought itself. There's mobs and loot dispersed through the map. Well? I don't know yet. We'll see in testing. I personally added two locations. The Barony, and some little adobe shacks on the long stretch to the raider base. I've fixed up a TON of errors, go count them all! There's likely more left. I was as thorough as I could be.

---
## [Blaineworld/moist](https://github.com/Blaineworld/moist)@[2d972f5c50...](https://github.com/Blaineworld/moist/commit/2d972f5c503c6d9be90a6ee871a18158e72680ec)
#### Wednesday 2023-05-03 17:17:30 by Blaineworld

start work on Month class

ugh i hate dates SO MUCH dates are HORRIBLE wouldn't it be so cool if there were THIRTEEN MONTHS and all of them except the last one had the SAME NUMBER OF DAYS that would be so SIMPLE and the DATE API IS SO ANNOYING AND JANKY AND INCONSISTENT WHY WHY WHY

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[ae7595b8e1...](https://github.com/microsoft/terminal/commit/ae7595b8e13d4764f4db7b4060eaf57d1b4ee82e)
#### Wednesday 2023-05-03 17:41:38 by Mike Griese

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[3c46c90c07...](https://github.com/git-for-windows/git/commit/3c46c90c072be2aec2c9ec938e8cef716582e735)
#### Wednesday 2023-05-03 18:44:03 by Johannes Schindelin

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
## [PassiHD2004/FoxClient](https://github.com/PassiHD2004/FoxClient)@[30ed30b416...](https://github.com/PassiHD2004/FoxClient/commit/30ed30b416a9adb835c1e98c2d92d17a4dce07e4)
#### Wednesday 2023-05-03 19:02:41 by Rooot

feat: move to brachyura, update to 1.19.4

i love chaos.

...

:3


* feat: transition to brachyura, initial update to 1.19.4

Signed-off-by: rooot <hey@rooot.gay>

* feat: improve brachyura buildscript, add github workflow for brachyura

does some improvements to the brachyura buildscript

Signed-off-by: PassiHD <passihd2004@gmail.com>
Signed-off-by: rooot <hey@rooot.gay>
Co-authored-by: rooot <hey@rooot.gay>

* feat: remove gradle workflow

Signed-off-by: rooot <hey@rooot.gay>

* fix: dependency bundling and mod/jar versioning

Signed-off-by: rooot <hey@rooot.gay>

* chore: remove useless comment

Signed-off-by: rooot <hey@rooot.gay>

* feat: i am stupid

Signed-off-by: rooot <hey@rooot.gay>

* feat: remove unused code, get rid of weird CI error
who the fuck is responsible for the codefactor.io integration

Signed-off-by: rooot <hey@rooot.gay>

---------

Signed-off-by: rooot <hey@rooot.gay>
Signed-off-by: PassiHD <passihd2004@gmail.com>
Co-authored-by: PassiHD <passihd2004@gmail.com>

---
## [YarataDarkness/Abdanor-Daniel-scrollytelling](https://github.com/YarataDarkness/Abdanor-Daniel-scrollytelling)@[0dc08830ef...](https://github.com/YarataDarkness/Abdanor-Daniel-scrollytelling/commit/0dc08830efee47a6abab05a9874f75a519229814)
#### Wednesday 2023-05-03 19:19:29 by YarataDarkness

i feel like dying

I tell myself that it going to get better but it doesnt. It always like this. An infinite loopy mess.
Like a higher thing dindt want me to be good at this.
"You sound lamentable and pathetic. Believe believe believe" is a type of argument that those who at their end of their cage after the
'suffering' can say. not me not me not me. Because I dont know when ill finally be in a confort cage of peace. it doesnt exist  and if it does,
 my mind refuses it. Because that confort leads to ignorance of the evil I hate. The ones that hurt. I wont have the time to protect
  myself. So It refuses. It refuses it. The confort cage, it refuses it.

---
## [Mey-Ha-Zah/tgstation](https://github.com/Mey-Ha-Zah/tgstation)@[200b739c0a...](https://github.com/Mey-Ha-Zah/tgstation/commit/200b739c0a0bbfff95dbfd697786013c92cb6cf6)
#### Wednesday 2023-05-03 20:28:50 by Kyle Spier-Swenson

Refactors and defuckulates dbcore. Adds support for min_threads rustg setting, Reduce query delay, Make unit tests faster (#74852)

dbcore was very fuckulated.

It had 3 lists of queries, but they all had their own current_run style
list to support mc_tick_check (as it was already being done before with
the undeleted query check, so i can understand why they ~~cargo culted~~
mirrored the behavior) This was silly and confusing and unneeded given
two of those loops can only process at most 25 items at a time on
default config, plus these were cheap operations (ask rustg to start
thread, ask rustg to check on thread).

Because of the confusingness of the 6 lists for 3 query states, The code
to run pending/queued queries immediately during world shutdown was
instead looking at the current_run list for active queries, **meaning
those queries got ran twice.**

The queued query system only checked the current active query count in
fire(), meaning even when there was nothing going on in this subsystem
new queries had to wait for the next fire() to run (10 ticks, so 500ms
on default config)

Those have all been fixed.

the config `BSQL_THREAD_LIMIT` has been renamed to
`POOLING_MAX_SQL_CONNECTIONS` and its default was lowered to match
MAX_CONCURRENT_QUERIES .

added a new config `POOLING_MIN_SQL_CONNECTIONS`, allowing you to
pre-allocate a reserve of sql threads.

The queue processing part of SSdbcore's fire() has been made to not obey
mc_tick_check for clarity and to make the following change easier to do:

If there is less than `MAX_CONCURRENT_QUERIES` in the active queue, new
queries activate immediately.

(its ok that there are two configs that kinda do the same thing,
POOLING_MAX_SQL_CONNECTIONS maps to max-threads in the mysql crate, and
it seems to only be a suggestion, meanwhile MAX_CONCURRENT_QUERIES can't
do anything during init, which is when the highest amount of concurrent
queries tend to happen.)

:cl:
config: database configs have been updated for better control over the
connection pool
server: BSQL_THREAD_LIMIT has been renamed to
POOLING_MAX_SQL_CONNECTIONS, old configs will whine but still work.
fix: fixed rare race condition that could lead to a sql query being ran
twice during world shutdown.
/:cl:

I have not tested this pr.

---
## [outreachy/website](https://github.com/outreachy/website)@[0901c4f615...](https://github.com/outreachy/website/commit/0901c4f61527373c76e4d32e5d046589a2334151)
#### Wednesday 2023-05-03 20:34:18 by Sage Sharp

Add tracking of sponsorship status, invoice ticket number, and notes

Each Outreachy sponsorship needs to be sent to Conservancy's RT ticket
interface. Sometimes sending the sponsorship information to Conservancy
gets delayed. Most often this is because we're waiting on invoicing
details from the sponsor, or we're confirming intern selections.

The notes field will let us keep track of what information we need to
gather. The status field allows us to use emojis to see the status of
our invoicing requests tasks. The RT ticket number field will help us
cross-reference data, and add quickly add our notes to Conservancy's
accounting system once we send the invoice.

The pages to view and edit sponsorship information are only accessible
to Django users with staff permissions. Otherwise they will get a
permission denied error page.

Update the sponsorship tests to reflect the new HTML layout of the
sponsorship info page.

TODO: I tried to add history tracking for the new fields, but could not
make it work by just adding a Revision mixin to the new
SponsorshipUpdates view. I suspect I'm doing something wrong - maybe
with the admin.py file? I can't remember how setting up history tracking
works right now, so I'll come back to it later.

TODO: The notes on the sponsor info page table need to be contained in
an accordion that is collapsed by default. However, I can't get the
accordion code to work (I always have trouble with bootstrap's aria
code, and I want to make sure the new code is accessible). So we'll just
display all the notes all the time for now.

---
## [FreetoZ/cmss13](https://github.com/FreetoZ/cmss13)@[590bad4061...](https://github.com/FreetoZ/cmss13/commit/590bad4061627b75b638c0f7c1fbd3cca84e43c1)
#### Wednesday 2023-05-03 20:46:07 by sleepynecrons

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
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[4014aef4b0...](https://github.com/Ical92/tgstation/commit/4014aef4b0a24d260b314f462a21f943c3d62894)
#### Wednesday 2023-05-03 20:58:37 by Bloop

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
## [sri-ka1kiZ/iceberg](https://github.com/sri-ka1kiZ/iceberg)@[1b371b41b9...](https://github.com/sri-ka1kiZ/iceberg/commit/1b371b41b97a880c0e2ef5952301aede2367a509)
#### Wednesday 2023-05-03 21:00:51 by DidIDoThat

Create gradle.yml

Honestly, I dunno what I am doing.  But I'm trying and struggling. There are times when the code won't operate. I then dig in to see why... whether I didn't setup correctly or the code is corrupt. Which it is. So many different commands and code. Learning not to just download a repository and hope it works... duh. What I need to know is the how's and why's. I have been going through these difficulties for years. Not something that is just "new". I'm exhausted and I wanna tap out. But there is defiance within me and I do not have the heart to just walk away. I call BS. I am aware that there are specific people who would harass me as such.

Attempt #290 -hoping the breaks the cycle

---
## [JoysKo/HYBRID_CAF_kernel](https://github.com/JoysKo/HYBRID_CAF_kernel)@[18a3e41532...](https://github.com/JoysKo/HYBRID_CAF_kernel/commit/18a3e41532c11b2b94a30ec1c020a54a415ff374)
#### Wednesday 2023-05-03 21:30:51 by Douglas Anderson

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[39ebf7c2af...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/39ebf7c2af41309fa4d5206f77cc4d261f47dfb7)
#### Wednesday 2023-05-03 21:36:34 by SkyratBot

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
## [C0USTEAU/dwm](https://github.com/C0USTEAU/dwm)@[67d76bdc68...](https://github.com/C0USTEAU/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2023-05-03 21:38:59 by Chris Down

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
## [usnpeepoo/cmss13](https://github.com/usnpeepoo/cmss13)@[c4ebe04c7c...](https://github.com/usnpeepoo/cmss13/commit/c4ebe04c7c9ff01aa928c0c629322d72dec721d9)
#### Wednesday 2023-05-03 22:04:38 by Julian56

fix the medbay door release button to exit treatment center. (#3173)

# About the pull request
fix the medbay door release button to exit treatment center.
was my mistake sorry
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
fixing bug is good
# Testing Photographs and Procedure
i tested the button ingame 
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:

fix: fix the med-bay door release button to exit treatment center.my
bad.

/:cl:

---------

Co-authored-by: Julien <jverger.ingx@gmail.com>
Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [jforte372/James-Forte-hellow-world](https://github.com/jforte372/James-Forte-hellow-world)@[2ae5a71452...](https://github.com/jforte372/James-Forte-hellow-world/commit/2ae5a7145287b6f35927b05658ce2b59ce86d0a1)
#### Wednesday 2023-05-03 22:12:39 by jforte372

Update README.md

Tried to make his students(me) laugh with a terrible dad joke that wasn't funny(it was).

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[c27f9a6d9b...](https://github.com/DATA-xPUNGED/DataStation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Wednesday 2023-05-03 22:22:01 by necromanceranne

Minor Nukie Thing: Bolt-action Sniper Rifle, balance coding, and some ammo changes (#73781)

## About The Pull Request

### The Rifle:
-The Sniper Rifle is now a bolt action. This replaces the 4 second fire
delay on the sniper rifle. This overall will improve the fire rate if
you're good at racking the bolt, but it will also feel less like you're
in a weird limbo of inaction while using the sniper rifle, since the
fire delay can be quite confusing to players not used to it. This can be
tweaked, like reducing the speed of the racking action, if it seems like
it is too much.
-The scope component now goes up to 50 tiles (or so), which allows you
to gain a significant sightline over an area. The reasoning for this is
simple. The component actually nerfed the overall range of the sniper
rifle's scope, so this should hopefully restore that somewhat. And
having such a huge sightline makes it much easier to utilize the
impressive range of the rifle. Currently, it's really only ideal for
extremely close range fighting.
-The normal sniper rifle, the one that syndicate base scientists get,
can be suppressed. I don't know why it was different.

### The Ammo:

Normal .50 BMG: Does much more object damage, and on top of that deals
additional damage to mechs, but not by much more. Now, when it
dismembers a limb, it also deals its damage to the chest. This ensures
that you didn't straight up lose out on dealing a killing blow because
you took their limb off, and makes the dismemberment property of .50 BMG
a significant upside rather than a immense detriment.

Marksman: Gains a lot of the above benefits, but has much lower range.
Why this nerf? It's actually because of some funny nonsense with how
ricochet works. Which can cause....accidents to happen. To you. Consider
that firing down a straight line and missing could be quite embarrassing
when the bullet has 400 tiles of range.

Soporific: Now called Disruptor ammo. Works as it did before, putting
humans to sleep for 40 seconds (seriously, 40 seconds). Also deals some
stamina damage, if...that's relevant. But now also causes an EMP effect
and a boatload of added damage to both mechs and borgs, allowing it to
be an excellent anti-mech and anti-borg ammo type, as well as scrambling
any pesky suit sensors, energy weapons and so on in an area around the
impact. Useful for support fire.

Incendiary (NEW!): Causes a massive firebomb to go off where it impacts
(no explosion, so this isn't a stun). Also sets the target on fire,
which is always fun. Good for shooting into groups of people with
impunity. Also deals burn damage instead, since I think nukies could use
more methods for direct fire damage.

Surplus (NEW!): It's .50 BMG but it lacks most if not all the upsides.
No armour penetration, no dismemberment, no paralysis. It still deals a
lot of damage to objects, so not a bad option for simply removing
structures from afar. So what's the point in this ammo? You can buy 7
magazines for the price of one. I want to introduce 'Surplus' as an idea
for nukies to invest in if they want to be able to keep shooting but
they're really on a budget, like most non-warop nukies tend to be. This
is definitely subject to change (like a damage decrease on top of
everything else).

Pricing and Capacity: Normal ammo and surplus costs 3 TC. Every special
ammo costs 4 TC. Every special ammo also has the same ammo capacity as
the normal magazine. It's kind of weird how most of the subtypes had 5
shots rather than 6, but then soporific had...3? I don't get it. This
would probably cause a good deal of confusion, especially if you are
swapping ammo types and weren't aware of this particular oddity.

Anyway, 6 shots.

### Minor Addition
Gets rid of the cheap suppressor. It lies to players, tricking them into
thinking this is a low quality suppressor. Newsflash, it isn't. There is
no distinct difference between that suppressor and the normal
suppressor.

## Why It's Good For The Game

The sniper rifle, unfortunately, sucks a lot except for very specific
use cases. It got a big nerf with the scope component in terms of range,
even if the functionality is way cooler. And, at a baseline, there was
some counterintuitive functions attached to it. Dismemberment was cool,
but it also caused a loss in overall damage due to how limbs contribute
to core health. On top of this, the cool ammo types were...not much
better? Penetrator was almost always the best option, even if it lost a
lot of damage as a consequence.

So, what was it good for? X-ray + Penetrator. Pretty much, that's it. It
has some other uses but if I had to be entirely honest, there wasn't
much that other weapon couldn't do as well.

Hopefully this helps things going forward, and I want to mess with this
as well down the line in case its a bit too much of a boost in power.

Absolutely please rip this PR apart.

## Changelog
:cl:
balance: Makes the syndicate sniper rifle a bolt-action rifle.
balance: Sniper rifles have a scope range of roughly 50 tiles.
balance: Sniper rifle ammo, if it dismembers your limbs, does damage to
the chest.
balance: All the various syndicate sniper rifle magazines have
consistent casing quantities (6 shots). They also have more consistent
pricing. 3 for normal and a box of surplus, and 4 for every other type.
balance: Reduces the range of Marksman ammo to 50 tiles. Not because it
is strong, but because you might accidentally shoot yourself if you're
not watching where you're shooting. Ricochets are no joke.
add: Replaces Soporific with Disruptor ammo. Works like soporific, but
also EMPS things it hits.
add: Adds Incendiary .50 BMG. Causes a combustion to erupt from the
struck target, as well as setting targets on fire. Great for parties.
add: Adds Surplus .50 BMG. It sucks, but you get a lot of them! Quantity
over quality, baby.
remove: The suppressors in the bundle are of standard quality. The
apparent 'cheap suppressor' that came bundled with the C-20r and sniper
rifle were found to actually be 'fine'. Trust us.
/:cl:

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[95b810919e...](https://github.com/DATA-xPUNGED/DataStation/commit/95b810919ede0f4fb22dc711c0334abf36b94843)
#### Wednesday 2023-05-03 22:22:01 by lizardqueenlexi

Adds preference for "Tagger" paint color. (#74281)

## About The Pull Request

Per the title, this PR allows you to pick your starting paint color from
the "Tagger" quirk on the character preferences menu.


![image](https://user-images.githubusercontent.com/105025397/227810007-4706c743-31c2-47d8-80ac-e11687d36c00.png)

This replaces the starting color being random; it does not prevent you
from changing the color later as normal.
## Why It's Good For The Game

It's a minor quality of life change. This will mostly be helpful to
players who have some "signature" color they like to use, to prevent
having to manually select it (and possibly input a color code) every
round. It will be of less relevance to those who tend to select new
colors every round anyway.

Possible downsides are mainly adding another pref to the menu, although
this shouldn't be too much of an annoyance since it only appears if you
already have the relevant quirk. It does also remove the _ability_ to
have a randomly-chosen paint color, though I'm not sure if that matters.
## Changelog
:cl:
qol: you can choose your default paint color for the "Tagger" quirk from
prefs.
/:cl:

---
## [ghemawat/weaver](https://github.com/ghemawat/weaver)@[b9eb4fc35d...](https://github.com/ghemawat/weaver/commit/b9eb4fc35df080f128de5d674e2ca52d7483932a)
#### Wednesday 2023-05-03 22:37:36 by Michael Whittaker

Changed deployers to persist data in one spot.

Recall that deployers often have to persist various data to the file
system. The "weaver multi" deployer, for example, persists logs,
registrations, and traces to files.

Before this PR, deployers would store logs in /tmp and everything else
in ~/.local/share/serviceweaver. Different deployers would sometimes
store their data in the same directory. A "multi_perfetto.db" file would
be right next to a "single_perfetto.db" file, for example.

This made purging data files annoying. It was like a scavenger hunt
trying to track down the various places that data was stored. This PR
changes deployers to store all their data in a single directly. For
example, the "weaver multi" deployer now stores everything inside
"~/.local/share/serviceweaver/multi". The single process deployer stores
everything inside "~/.local/share/serviceweaver/single".

This makes purging much simpler. It also makes it clearer which files
are being used by which deployers.

Note that this PR moves logs out of /tmp, which persists them longer.
This means that logs won't be garbage collected automatically, but I
think that's actually a good thing. We should implement a principled way
of garbage collecting logs, rather than leaving it up to /tmp. I think
it would be surprising and frustrating if an important log file was
spuriously deleted by the OS.

---

