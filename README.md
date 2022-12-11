## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-10](docs/good-messages/2022/2022-12-10.md)


1,674,976 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,674,976 were push events containing 2,282,783 commit messages that amount to 146,543,376 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 57 messages:


## [casswedson/Cataclysm-DDA](https://github.com/casswedson/Cataclysm-DDA)@[b1a13b739a...](https://github.com/casswedson/Cataclysm-DDA/commit/b1a13b739acab08acff85b888ac5264f1471ec8d)
#### Saturday 2022-12-10 01:39:41 by casswedson

fix: edge case ci error exit

so a step of the reviewer workflow always runs, good it is the actual
magical step doing the hard work, but if the workflow gets canceled, the
step exits with an error code, I actually knew this but me from like a
day ago was like:
"nah man this won't bother me in the future."

guess what; after a couple hours I was felling the pain my perfectionist
subconscious was putting me through, plus odd error code exits aren't
very professional or clean or pleasing I'd say, also someone may think
it's weird, look into it, waste time looking at my code

title: do not draw much attention

---
## [nevimer/Skyrat-tg](https://github.com/nevimer/Skyrat-tg)@[3dfeccbf27...](https://github.com/nevimer/Skyrat-tg/commit/3dfeccbf27b8dc53c97c2e9db0f1bdc4fd000ebe)
#### Saturday 2022-12-10 01:57:42 by SkyratBot

[MIRROR] Clowns will now always like bananas. [MDB IGNORE] (#17300)

* Clowns will now always like bananas. (#70919)

## About The Pull Request
Clown's liver makes them like bananas, ignoring their racial food
preferences.

## Why It's Good For The Game
I don't think clown moths should vomit from eating bananas. They are
clowns, after all.
Also clowns are healed from eating them, so it's a bit silly that they
vomit from their funny medicine.

## Changelog

:cl:
balance: Non-human clowns enjoy eating bananas now.
/:cl:

* Clowns will now always like bananas.

Co-authored-by: Striders13 <53361823+Striders13@users.noreply.github.com>

---
## [RatFromTheJungle/Skyrat-tg](https://github.com/RatFromTheJungle/Skyrat-tg)@[84b1612201...](https://github.com/RatFromTheJungle/Skyrat-tg/commit/84b161220115e3243272299b3f8f3cb29d484709)
#### Saturday 2022-12-10 02:18:53 by SkyratBot

[MIRROR] Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. [MDB IGNORE] (#18019)

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. (#71674)

## About The Pull Request

- The chaplain choice beacon now uses a radial to select the armor set,
instead of a list, giving the user a preview of what each looks like.

![image](https://user-images.githubusercontent.com/51863163/205417930-f5ceab11-6974-48a9-a871-abcb8228bcf2.png)

- Lots of additional cleanup to choice beacon code in general. Less copy
pasted code.
- All beacons now speak from the beacon with their message, instead of
some going by "headset message". Soul removed

## Why It's Good For The Game

I always forgot when selecting my armor which looks like what, and
choosing an ugly one is a pain since you only get one choice. This
should help chaplains get the armor they actually want without needing
to check the wiki.

## Changelog

:cl: Melbert
qol: The chaplain's armament beacon now displays a radial instead of a
text list, showing previews of what all the armor sets look like
qol: (Almost) all choice beacons now use a pod to send their item,
instead of just magicking it under your feet
code: Cleaned up some choice beacon code.
/:cl:

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup.

* update modular

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[df5a689a58...](https://github.com/TaleStation/TaleStation/commit/df5a689a580c6763075a4853ada899d01743e435)
#### Saturday 2022-12-10 03:08:16 by TaleStationBot

[MIRROR] [MDB IGNORE] Basic Mob Carp: Retaliate Element (#3605)

* Basic Mob Carp: Retaliate Element (#71593)

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

* Basic Mob Carp: Retaliate Element

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Spectralized/clovermon-showdown](https://github.com/Spectralized/clovermon-showdown)@[6d337bdac2...](https://github.com/Spectralized/clovermon-showdown/commit/6d337bdac26661f4209c26f0d1db7497984806d2)
#### Saturday 2022-12-10 03:28:57 by Mr. Sableye

Fixes Boltbeam (except probably some weird edge cases but fuck you)

---
## [P404-lavender/android_hardware_qcom_display](https://github.com/P404-lavender/android_hardware_qcom_display)@[836130d282...](https://github.com/P404-lavender/android_hardware_qcom_display/commit/836130d282e73bf36bb0cdc2fd834fff8806d5d9)
#### Saturday 2022-12-10 04:13:17 by xenxynon

fix mismerge
I'm very lazy
also fuck you
also kys

Signed-off-by: xenxynon <flynryder427@gmail.com>

---
## [meow56/advent-of-code-2022](https://github.com/meow56/advent-of-code-2022)@[d1c07653be...](https://github.com/meow56/advent-of-code-2022/commit/d1c07653be78f2cfea84f878bf5ad1781ba52edd)
#### Saturday 2022-12-10 05:28:03 by meow56

Day 10-2

Mmm. The only bug this time was incrementing cycle before doing stuff.

Oh also, did you like my horrible regX joke? That's what I call funny.

---
## [Sylviacord/sylviacraft](https://github.com/Sylviacord/sylviacraft)@[5749387583...](https://github.com/Sylviacord/sylviacraft/commit/5749387583afceb7af345ed6a3636b4b248e623c)
#### Saturday 2022-12-10 05:51:07 by TehcJS

fix issue idiot stupid fuck i fuck you hate badwhy

---
## [xyamikitsune/app-dev](https://github.com/xyamikitsune/app-dev)@[9ba3f4720b...](https://github.com/xyamikitsune/app-dev/commit/9ba3f4720ba3196ca3f531d58d2df8be1e0d3b93)
#### Saturday 2022-12-10 06:04:35 by xyamikitsune

Update README.md

Avengers - A movie about superheroes or more like uncontrollable individuals that possess such power, and a god as well are included in the team.
Thor - One of the original of the avengers. He as well got his own movie and was a god. Son of Odin, and half-brother of Loki.
Doctor Strange - A well-known doctor/surgeon that has such talent not only in medical field but in magic as well.
Jurassic World - There's a tour in an island theme park populated by dinosaurs created from prehistoric DNA. Era wherein dinosaur still exist by getting their fossils and creating them again. 
Transformer - A huge humanoid-robots that came from another planet called "Cybertron". A technological world/planet that is full of shining metals and robots which called transformers sooner called "Autobots" and "Decepticon".

---
## [xyamikitsune/app-dev](https://github.com/xyamikitsune/app-dev)@[bf21915bed...](https://github.com/xyamikitsune/app-dev/commit/bf21915bed0f822124f44fdc71ac1827d9475f00)
#### Saturday 2022-12-10 06:13:35 by xyamikitsune

Update README.md

Avengers - A movie about superheroes or more like uncontrollable individuals that possess such power, and a god as well are included in the team.

Thor - One of the original of the **avengers** He as well got his own movie and was a god. Son of Odin, and half-brother of **Loki**.

Doctor Strange - A well-known doctor/surgeon that has such talent not only in medical field but in magic as well.

Jurassic World - There's a tour in an island theme park populated by dinosaurs created from prehistoric DNA. Era wherein dinosaur still exist by getting their fossils and creating them again. 

Transformer - A huge humanoid-robots that came from another planet called "**Cybertron**". A technological world/planet that is full of shining metals and robots which called transformers sooner called "**Autobots" and "Decepticon**".

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8cfc50e764...](https://github.com/treckstar/yolo-octo-hipster/commit/8cfc50e7646b0b640f162a581c0168c04540ab63)
#### Saturday 2022-12-10 06:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [xyamikitsune/app-dev](https://github.com/xyamikitsune/app-dev)@[ef094731d8...](https://github.com/xyamikitsune/app-dev/commit/ef094731d84a9f601814f0720d0961ea6157fe5d)
#### Saturday 2022-12-10 06:30:29 by xyamikitsune

Create README.md

Avengers - A group of individuals that has different kind of powers, they grouped themselves together even though they don't want to do it but in order to save the planet Earth, they should do it. The group consists of billionaire, an archer, spy, enraged green beast, a lightning god and an old human that wears America outfit.

Thor - One of the original member of the group called "Avenger" of planet Earth. A god that can control a lightning, and son of Odin ( The father of all ), a brother of Loki ( God of Mischief ).

Doctor Strange - A well-known doctor/surgeon. Best of the best skilled surgeon in the world. But due to some accident, he lost his ability to save someone life. He lost his ability as a surgeon but a new power/skill came and that's what makes who he is right now.

Jurassic World - An island theme park populated by dinosaurs created from prehistoric DNA. Dinosaurs came back from fossil and many things happened.

Transformer - A huge humanoid-robots that came from another planet called "Cybertron". The robots can transform into different kind of cars that exists in the modern era of the world.

---
## [MylesAndMore/tumble](https://github.com/MylesAndMore/tumble)@[a56513d851...](https://github.com/MylesAndMore/tumble/commit/a56513d85180c699b566783d7e1ce1f12d641aa4)
#### Saturday 2022-12-10 07:23:47 by Myles

1AM COMMIT LETS GOOOO

- fixed about 20 bugs, glitches, exploits, you name it--Jacob can break anything (not even joking, did my first *real* playtest; it was...valuable...we'll leave it at that)
- added some sort of block balancing (want to improve on it later maybe?)
- change the prefix back to lowercase because we're emo or something (COMMONALITY SHUT UP)
- game env is now more controlled (thanks Jacob)
- can I go to bed now

---
## [Megharoyal/java](https://github.com/Megharoyal/java)@[acfe6cb4bf...](https://github.com/Megharoyal/java/commit/acfe6cb4bf1405c433184998b6b06b51aa7e4237)
#### Saturday 2022-12-10 08:17:30 by Thota Meghana

Create The Chronicles of Narnia

Four kids Peter,Susan,Edmond and Lucy travel through a wardrobe to the land of Narnia. Narnia is a fantasy world of magic with mythical beasts and talking animals.While exploring the land of narnia Lucy found Mr.Tumnus the two legged stag ,and she followed it, down a narrow path .She and Mr.Tumnus became friends and he offered a cup of coffee to Lucy in his small hut.It was time for Lucy to return to her family and so she bid good bye to Mr.Tumnus and while leaving Mr.Tumnus told that it is quite difficult to find the route back as it was already dark.He told her to see the trees while returning back and said that the first tree with two digits number will help her find the way and the way to go back to her home is the sum of digits of the tree and that numbered way will lead her to the tree next to the wardrobe where she can find the others.Lucy was already confused, so pls help her in finding the route to her home.... 

Input Format:
Input consists of an integer corresponding to the 2-digit number.
Output Format:
Output consists of an integer corresponding to the sum of its digits.

Sample Input
23

Sample Output
5

---
## [etherware-novice/tgbagilsstation](https://github.com/etherware-novice/tgbagilsstation)@[661eaa985e...](https://github.com/etherware-novice/tgbagilsstation/commit/661eaa985e32056cc25f32bd81d9106861a4f9f8)
#### Saturday 2022-12-10 09:05:42 by MrMelbert

Important heretic spell rebalancing (#71620)

## About The Pull Request

Nerfs
- Furious steel cooldown: 30s -> 60 seconds (when ascended: 10s -> 30s)
- Furious steel: Now affected by antimagic
- Cleave cooldown: 40s -> 45s
- Cleave range: 9 tiles -> 4 tiles
- Cleave wound: Now has natural clotting, changing the amount of blood
loss from inf -> ~40%
- Blood siphon range: 9 tiles -> 6 tiles
- Void Pull: Now affected by antimagic
- Void Phase: Now affected by antimagic

Buffs
- Void Blast cooldown: 60s -> 30s

Other
- Rust Formation now has a "distinct" icon
- Void Blast now has a "distinct" icon

## Why It's Good For The Game

A lot of these spells were extremely oppressive, and made it pretty much
a joke to get away with anything.
They were no-brainer choices, and as a result no one really pathed into
anything else but these.

- Furious Steel: 
- Now that blade heretics have "realignment" in their repertoire, which
offers them another counter for being hit by disablers or batons, this
spell doesn't need to have such an insanely high uptime. The spell
should be used for initiating and obtaining the lead in a combat,
instead of having nigh-invulnerability for most periods.
- Additionally, antimagic protection was kind of missing, which was
partially an oversight of it not being a `/magic` projectile.
 
- Cleave:
- Cleave was by far the most absurd ability available bar none. This
spell was guaranteed death in 30 seconds if the target had no way to
stop the bloodflow immediately. AND it could be casted from across the
screen. This brings cleave's range into midrange between you and the
target, giving a lot more opportunity to be aware for the victim.
- Critical bleed wounds had a negative clotting rate, meaning that prior
you would bleed to 0% from cleave if you didn't stop it. Not very fun,
so with the default clotting rate it now stops at 60% blood flow -
enough to be lethal if untreated, but doesn't completely tap you out
   - **Alternatives**: 
      - Keep the no clotting, make it a pure melee / touch spell. 
      - Reduce the cooldown, make it a projectile
- Change it to be like a cool scythe attack that comes out of the caster
and does a sweep

- Blood Siphon: 
- This was primarily done to slot in better with Cleave's range
decrease, encouraging more close range combat between the two. Getting
point clicked from across the screen isn't fun.

- Void Pull and Phase:
- Largely done for consistency. These are spells which cause damage, so
anti-magic should stop the damage from the spells.

- Void Blast
- I have no idea why I made the cooldown so high on this, 1 minute made
it almost worthless.

TLDR: Instakill click spells from across the screen bad, invulnerability
bad

## Changelog

:cl: Melbert
balance: Heretic: Furious Steel's cooldown has been doubled (30s ->
60s), and abides by antimagic
balance: Heretic: Cleave's cooldown has increased by 5s, range has been
decreased to 4 tiles, and wound applied now has natural clotting
balance: Heretic: Blood Siphon's range has been decreased to 6 tiles
balance: Heretic: Void Pull and Phase abide by antimagic
balance: Heretic: Halved Void Blast's cooldown to 30s
qol: Heretic: Void Blast and Rust Formation now have distinct icons 
/:cl:

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[4fd404aa8f...](https://github.com/TheBoondock/tgstation/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Saturday 2022-12-10 09:25:03 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms


![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)
  
</details>



## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[5da871e271...](https://github.com/TheBoondock/tgstation/commit/5da871e2719fb7aac04fb1ec4c85ea7a09a83b36)
#### Saturday 2022-12-10 09:25:03 by RikuTheKiller

Made geysers easier to find (#71608)

## About The Pull Request

This PR raises the geyser spawn rate from 0.1 to 0.15 and increases the
weight of wittel geysers to 10 which is the same as every other special
geyser. (previously 6)

Wittel shouldn't be any less difficult to find than other geysers as all
of the special geysers are equally powerful. Hyper-plasmium oxide can be
used to make extremely powerful explosives that can go beyond maxcaps
and hollow water + protozine can create an infinite amount of strange
reagent.

I've subjected myself to going out of my way to visit lavaland/icemoon
several times to get wittel and each time finding a single geyser takes
about 5 minutes of my time. This, coupled with the fact you really don't
have a lot of time to be wasting on looking for the geysers results in
an unfun experience.

I understand geysers are sort of a necessary evil, however, they
shouldn't be THIS difficult to find. Out of the 10 or so geysers I've
found, only 1 has had wittel in it and it was next to a whelp portal
which ended both me and my miner escort.

I've also hunted the entirety of lavaland with no luck. (Horrendous
experience.)

I've dedicated entire rounds to this, by the way.
## Why It's Good For The Game

If you go out of your way to waste ages hunting for geysers, there
should at least be a reward. That is, in the same round, not after 3 or
more rounds as even megafauna gear isn't gatekept THAT hard.

You shouldn't have to waste this much of a miner's time (who is also
going for megafauna gear) to get something that is arguably less
powerful than what they get for less effort. Megafauna gear is also
available every round and is attained via predictable methods.

This PR will also likely make geyser scanning a more comparable method
of point gain to just mining.

Oh and not to mention that penthrite is available almost roundstart via
luxpens. (It's a wittel chem.)
## Changelog
:cl:
balance: Geysers now spawn more often, especially wittel geysers.
/:cl:

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[2425531eb2...](https://github.com/TheBoondock/tgstation/commit/2425531eb2dab84fb27ed864e4c52470bfff6918)
#### Saturday 2022-12-10 09:25:03 by John Willard

Removes tablets (not PDAs) entirely. (#71507)

## About The Pull Request

**Comes with an UpdatePaths!**

Removes the tablet subtype, PDAs now replaces them entirely.

Nukie and Silicon tablets are now subtypes of the PDA instead, while
contractor ones were removed entirely as they didn't do anything and
were unused (though it wouldn't be hard to re-add).

Nukie PDAs are now the only type of PDA that uses modular_tablets.dmi,
which is just larger icons of modular_pda. Each application requires an
icon state in both of these, for 2 different sizes, which makes it
annoying to make new applications, especially if it can also run on
computers/laptops.

### Icons

Because Silicon tablets are now a subtype of PDA, they use PDA icons
instead of tablet ones. Luckily for us, they already exist in code.

![image](https://user-images.githubusercontent.com/53777086/203876575-56eb1593-774c-47c6-8e7d-491a7805f28c.png)

AI's don't use a tablet icon though, so they aren't affected.

## Why It's Good For The Game

There's very little difference between tablets and PDAs, PDAs overshadow
them in every single way, so at this point I don't see why we should
have both of these, and if you compare the two in usefulness and actual
in-game use by players, it's a no-brainer than the item all players get
roundstart and comes with a messenger should be the one we go with.

Also as said in the about section, when making an app you would need to
make icon states for the program running for all hardware it can run on,
which is Computer, Laptop, PDA, and Tablet.

Laptop is just a smaller computer icon
PDA is just a smaller tablet icon

However, you can't simply shrink the size of the icon, instead you have
to completely resprite the same app icon FOUR TIMES for it to not
bluescreen on all these different devices.

<details>
<summary>
Here's examples of it
</summary>
Computer (NOTE: *They share the same icon file as regular computers*)
<img
src="https://user-images.githubusercontent.com/53777086/203876801-486a8054-489a-4983-bdad-a2599b4dc379.png"/>
Laptop
<img
src="https://user-images.githubusercontent.com/53777086/203876333-58e5d135-f4c6-4a02-8948-1df771e294a4.png"/>
Tablet
<img
src="https://user-images.githubusercontent.com/53777086/203876352-816c7fb1-c681-40b9-99e0-052f49632c7f.png"/>
PDA
<img
src="https://user-images.githubusercontent.com/53777086/203876358-1cf7253d-3c6a-456a-8133-ebf7f0351637.png"/>
</details>

If we wish to help in simplifying this, we should remove tablet icons
entirely, which means 1 less icon to worry about. To do this, we'd need
to resprite nukie PDAs, however I am very much not a spriter and never
tried GAGS, so I'll leave it to someone else to do.

## Changelog

:cl:
del: Tablets are now removed, PDAs are now the base 'tablet'. Silicon
and nukie tablets are now PDAs.
/:cl:

---
## [lichess-org/chess-openings](https://github.com/lichess-org/chess-openings)@[9f7632e84e...](https://github.com/lichess-org/chess-openings/commit/9f7632e84ebf35b79b8d3c08af9b95943cc54e59)
#### Saturday 2022-12-10 09:50:51 by Alexandru Duca

Scandinavian Defense: Portuguese Gambit

- Removed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. f3 Bf5` named `Scandinavian Defense: Portuguese Variation, Portuguese Gambit`.
- Renamed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` from `Scandinavian Defense: Portuguese Variation` to `Scandinavian Defense: Portuguese Gambit`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` named `Scandinavian Defense: Portuguese Gambit, Banker Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` named `Scandinavian Defense: Portuguese Gambit, Classical Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` named `Scandinavian Defense: Portuguese Gambit, Correspondence Refutation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` named `Scandinavian Defense: Portuguese Gambit, Elbow Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` named `Scandinavian Defense: Portuguese Gambit, Jadoul Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` named `Scandinavian Defense: Portuguese Gambit, Lusophobe Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` named `Scandinavian Defense: Portuguese Gambit, Melbourne Shuffle Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` named `Scandinavian Defense: Portuguese Gambit, Wuss Variation`.

This line `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` in the Scandinavian Defense has many different names across chess literature. Selby Anderson released the book [Center Counter Defense: The Portuguese Variation](https://www.amazon.com/Center-Counter-Defense-Portuguese-Variation/dp/1886846103) in the year 1997 and, apparently, named it `Portuguese Variation`. In his book [Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943), [David Smerdon](https://en.wikipedia.org/wiki/David_Smerdon) called this line `Portuguese Complex`, but he noted that it was also called `Portuguese Opening` as well as `Jadoul Variation` [Section 1]. It's called `Portuguese Gambit` in Wikipedia's [list of chess gambits](https://en.wikipedia.org/wiki/List_of_chess_gambits#Scandinavian_Defense) and `Portuguese Variation` as well as `Jadoul Variation` in Wikipedia's article on the [Scandinavian Defense](https://en.wikipedia.org/wiki/Scandinavian_Defense#2...Nf6). (Unfortunately, I was unable to check the sources Wikipedia provides because I couldn't find the referenced books.)

Since Selby Anderson's book predates all other sources, there is an argument to name this line `Portuguese Variation`. However, Black delays taking back the pawn on d5 twice (first time with `2... Nf6` and second time with `3... Bg4`). This gives White the opportunity to secure the extra pawn with e.g. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4 Bg6 6. c4`. Additionally, Selby Anderson may not have been aware of the dubious nature of this variation ([Stockfish gives White +0.8](https://lichess.org/7CAhQOCs)). Furthermore, David Smerdon repeatedly refers to this line as a gambit despite calling it `Portuguese Complex`. Because of this, I argue that this line should be called the `Portuguese Gambit`.

[Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943) is currently the most extensive book on the `Portuguese Gambit`. It categorizes all major responses from White after `1. e4 d5 2. exd5 Nf6 3. d4 Bg4`. Smerdon also offers creative names for all variations covered by his theory. Here are the variations sorted by chapter:
1. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` is called `The Banker`. (White "banks" the extra pawn with the immediate `5. c4`.)
2. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` is called `The Jadoul`. (Named after [Michel Jadoul](https://de.wikipedia.org/wiki/Michel_Jadoul) who is one of the earliest exponents of the Portuguese Gambit [Introduction, Inspirational Game #1].)
3. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` is called `The Melbourne Shuffle`. (Played by many australian IMs from Melbourne [Chapter 3]. It is named after a [rave dance](https://en.wikipedia.org/wiki/Melbourne_shuffle) which originated in Melbourne.)
4. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` is called `The Correspondence Refutation`. (A line against the `Portuguese Gambit` successfully employed the correspondence community [Chapter 4].)
5. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` is called `The Wuss`. (Apparently, `4. Be2` is a wimpy move and only a [wuss](https://www.merriam-webster.com/dictionary/wuss) would play it.)
6. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` is called `The Lusophobe`. (According to Wikipedia, [Lusophobia](https://en.wikipedia.org/wiki/Lusophobia) is irrational hostility, racism or hatred towards Portugal, the Portuguese people or the Portuguese language and culture. David Smerdon is making a joke by referring to the line `4. Bb5+ Nbd7 5. Be2` as "Anti-Portuguese" or "effective against the Portuguese Gambit".)
7. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` is called `The Elbow`. (Given the effectivness of the line `4. Bb5+ Nbd7 5. Be2`, occasionally playing `4... c6` may discourage players from studying it while preparing against you. Playing `4... c6` is a metaphor for hitting your well prepared opponent with your elbow [Chapter 7].)
8. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` is called `The Classical`. (Refers to the fact that the move `4. Nf3` is principled [Chapter 8].)

---
## [PhantomNiqht/ColdWarModHOI4](https://github.com/PhantomNiqht/ColdWarModHOI4)@[94e0eaf10c...](https://github.com/PhantomNiqht/ColdWarModHOI4/commit/94e0eaf10cdaff0189431142743a34b2ed6f30bf)
#### Saturday 2022-12-10 10:11:24 by BenisMomentum

Added Mersin as a playable Country

big dick mersin, cucks all of turkey, fuck you syria you're next

---
## [ThomasLotsander/AdventOfCode](https://github.com/ThomasLotsander/AdventOfCode)@[d728513b04...](https://github.com/ThomasLotsander/AdventOfCode/commit/d728513b04beb13825d4f05088b5ff4df467d46e)
#### Saturday 2022-12-10 11:04:42 by Thomas Lotsander

Day 7... Fucking hell this is ugly. Maybe refacotr next year.

---
## [Simplehorror/Yogstation](https://github.com/Simplehorror/Yogstation)@[0e64e06e9e...](https://github.com/Simplehorror/Yogstation/commit/0e64e06e9e738cc7c170a008b264b6dbecc98df6)
#### Saturday 2022-12-10 11:33:12 by Sniblet

Update objective.dm (#17000)

My name is not important. What is important is what I'm going to do. I just fucking hate this world, and the human worms feasting on its carcass. My whole life is just cold, bitter HATRED. And I always wanted to die violently. This is the time of vengeance, and no life is worth saving. And I will put into the grave as many as I can. It's time for me to kill. And it's time for me to die.

---
## [LensPlaysGames/LITE](https://github.com/LensPlaysGames/LITE)@[efbefb2caa...](https://github.com/LensPlaysGames/LITE/commit/efbefb2caaa3124981a50629124d3d444c1a700d)
#### Saturday 2022-12-10 11:50:16 by Lens

`realpath()` is *not* like `_fullpath()`, sadly

Missing semicolon, haha.

It's not the 80s anymore: no more `get_current_dir_name()`

Error printout for `realpath()`

These stupid bikeshedding commits are needed so I can test it on my
linux VM by pulling from git; it will be fixed shortly (or not).

Just going to add: the fact that `realpath` *requires* a file to exist
at path just to give you an absolute path is bonkers and annoying.

If `realpath()` fails with ENOENT, create file and try again.

Typos

I forget C is case-sensitive, sometimes...

The millionth commit that solves nothing: More `realpath()`

This commit has been rebased and is a combination of 7 commits.

---
## [faaaay/coyote-bayou](https://github.com/faaaay/coyote-bayou)@[288f673652...](https://github.com/faaaay/coyote-bayou/commit/288f6736526554c75abbcb09c92acb457be1c9b0)
#### Saturday 2022-12-10 12:02:12 by Superlagg

Merge remote-tracking branch 'upstream/master' into that-stupid-fuckin-dumb-shitass-fuckin--fuck-fuckass-shitfuck-gun-thing-that-isnt-alll-that-bad-honestly

---
## [MatandoYT/pokecrystal-mobile-en](https://github.com/MatandoYT/pokecrystal-mobile-en)@[ef79cf2c97...](https://github.com/MatandoYT/pokecrystal-mobile-en/commit/ef79cf2c970c92b091aa0132d42912e48c69f4a5)
#### Saturday 2022-12-10 12:31:26 by Damien Doury

Zipcode input constraints added (#11)

* Zipcode inputs accept letters and blank.

* Added the ability to compile pokecrystal-eu.gbc ROM with "make crystal-eu"

* Input constraints done.

Notes:
- As the zipcode is saved as a list of indexes from the char pools, and as the char pools differ from one region to another, the zipcodes will be broken from one region to another. This could be fixed server-side, or by encoding/decoding the indexes into VRAM indexes (the alphabet is constant between most regions, except asian ones) when opening/leaving the Profile menu.
- The macros I created are old and ugly (rgbds 0.3.8), and should be udpated when updating RGBDS.
- My code is kinda quick and dirty, as several lists are duplicated when they could be used once. I'm thinking about the "Zipcode_CharPoolForStringIndex" arrays, which could save several dozen bytes if optimized.
- A special case case for the alignment of the AUS region codes has been made, because the string length is not constant. This doubles the "Prefectures" array, which adds 173 bytes to the rom bank.
- With that being said, we are far from running out of space in the ROM $12.

* The zipcode is now right aligned/shifted when it ends with blank characters.

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[c13a816f04...](https://github.com/re621/dnpcache/commit/c13a816f048b3dbd1cc2ff528836296c47c61c6d)
#### Saturday 2022-12-10 12:46:57 by bitWolfy

Remove 991 artists from the DNP list.

Removed: byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, peshky, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, malachimoet, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, infinitedelusion, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, 100101, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, jdlaclede, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, trunchbull, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, whippytail, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[e9cff525dc...](https://github.com/Time-Green/tgstation/commit/e9cff525dc5b57153af3b4bb9039de08d6823805)
#### Saturday 2022-12-10 13:24:32 by tralezab

Refactors Pirates into Pirate Gangs, Adds the Psyker-gang as new pirates (#71650)

## About The Pull Request

### Refactor
Pirate gangs are now datumized for extendability, custom dialogue, etc.

### Psyker Gang 🧠 
Psyker-gang Members are pirates who are... yes, Psykers. They're on a
gore-binge and need some money for more hits of gore!

- Gore autoinjectors, filled with dirty kronkaine. Don't overdose,
you'll go splat.
- Psykerboost armor, reactive armor that refreshes psychic abilities.
Given to the leader.

- [x] @Fikou is making the map :D

## Why It's Good For The Game

God I fucking love variety also now we can add as many different pirates
as we so desire

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/205342701-9cba63ef-a22c-4f07-9b48-8793c4a2b5af.png)
  
</details>

## Changelog
:cl: Tralezab code, Fikou's map, PigeonVerde and Halcyon for sprites!
add: Psyker-gangers are new pirates
refactor: refactored pirate code so we can add more in the future
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[00d3780c38...](https://github.com/sleepynecrons/cmss13/commit/00d3780c382c704f24e5c6f24aa36d88d509b7ea)
#### Saturday 2022-12-10 13:24:40 by carlarctg

PDT/L Buff (#1757)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

PDT/L kits now fold into cardboard.

Added many spare PDT/L kits and batteries to req. (Marines dropped them
off at req once they realized they were shitty milsurp knockoffs)

Made minibatteries tiny.

Added boldwarning span macro.

Improved locator tube sprites: Now has a pop-out battery slot at the top
that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.

Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Fixed a bug in which a string referenced a null var.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

When I saw the PDT/L kit, I was very interested. It seemed like a great
way to encourage teamwork and buddying up with some fun lore flavor on
the side. However, trying it out, it really feels bare-bones. I get it's
supposed to be 'crappy' because Boots magazine subscriber items suck and
so do the lives of every private on the corps, but the way that's
implemented really ruins the extremely cool concept that is being able
to locate your fellow buddies across the battlefield, so you don't need
to continually say HEY WHERE ARE YOU over comms in the many times you'll
get split up.

Thus I've heavily buffed them around the board, which you may think is
going way too far, and to an extent, you're _right._ It's intentional.
This is a really cool item that actively encourages teamwork and that's
why I would rather swing the buff hammer too hard than give it a paltry
buff and some qol that ultimately nobody cares about. It's the same as
the spotter kit. It's nuts, but needs teamwork to actually be useful.
And this should be encouraged.

If it is still deemed too strong, there are things we can do to
laterally nerf it without closing the PR outright. Making the tube not
work if the bracelet holder's dead, having it needs comms to work come
to mind, but there are surely others.

> Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

The intention here is to let marines actually resupply their kits once
they run dry, and if they're proactive, maybe grab some and bring them
to FOB with them. Despite the description, the cells cannot easily be
recharged as power cell chargers are different from rechargers, they are
effectively Bay12 legacy that is VERY hard to come across.

'What if someone carries like 5 of them in their bag? That'd completely
nullify the power drain part.'

The stinger here is 'in the bag'. There are not enough reasons to carry
bags and satchels in this game right now as the sheer amount of storage
for goods marines have make them a one-man-army with two primaries. If a
marine forgoes a shotgun that might save them from a 1-pounce capping
runner for 5 spare LT batteries, a default medkit, and two flare boxes,
they are well within their rights to do so.

> Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)

This lets req drop them off at FOB if they eventually figure out they
can drop unvended surplus there. If this somehow happens, marines who
never even glanced at the kit in loadout or prep will notice it exists
and maybe, just maybe, use them!

> Made minibatteries tiny.

You may think this contradicts my earlier point about sacrificing
storage value, but _actually_ think about it. All webbing types, armor
slots, pouches, belts, even the helmet, all share the common attribute
of not caring about item size. If it's small or medum it still takes 1
out of the 3 slots in medium armor. Any storage item that isn't a
satchel, effectively. Every spare battery taken directly in the average
marine's inventory is one slot less for 5 shotgun shells, one magazine,
one unga juice flask, binoculars. What this means in the end is simply
that marines may carry one to two spare batteries in their helmet (I
think) at the cost of Drip which few marines will trade for, and satchel
marines don't have to sacrifice a lot of space for the spare battery.
Plus, it makes sense, why wouldn't a small AA rechargeable battery be
tiny.

> Improved locator tube sprites: Now has a pop-out battery slot at the
top that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

This looks so sick!

> Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Adding sounds to items should be standarized, I think. There are so many
cool sounds in the sound/machines folder that go unused. Personally i
felt like these small stupid sounds added a LOT to the atmosphere of
this tiny locator tube and bracelet. Alien Isolation is known for its
sounds, we should strive to emulate that.

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
add: Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.
qol: PDT/L kits now fold into cardboard.
add: Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)
balance: Made minibatteries tiny.
refactor: Added boldwarning span macro.
imageadd: Improved locator tube sprites: Now has a pop-out battery slot
at the top that shows up if emptied. The main green stripe is now a
battery indicator with appropiately-faded-out yellow warning and
blinking red danger sprites. The small notch at the bottom is now a
bracelet indicator that turns off without a battery and blinks red if
the bracelet was somehow destroyed.
qol: The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.
soundadd: Added a ton of sounds to interactions with the PDT/L kit.
Beeps on scanning, buzzes on errors, clicks on handling.
fix: Fixed a bug in which a string referenced a null var.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [404undefined/Grasscutter](https://github.com/404undefined/Grasscutter)@[88bc5c4c54...](https://github.com/404undefined/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Saturday 2022-12-10 13:27:02 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [smaitch/Grail](https://github.com/smaitch/Grail)@[4df80ca4cf...](https://github.com/smaitch/Grail/commit/4df80ca4cf84636fb32cd7c838cedd681f9985af)
#### Saturday 2022-12-10 13:33:03 by Yoshimo

The Waking Shores:
- Picture Perfect (65486) requires Pictures with Purpose (69870)
- Black Wagon Flight (65793) requires Claimant to the Throne (66780)
- The Courage of One's Convictions (65939) requires Talon Strike (65956)
- Obsidian Oathstone (66049) doesn't require The Courage of One's Convictions (65939)
- Forging a New Future (66056) requires The Courage of One's Convictions (65939)

Ohn'aran Plaines:
- Toward the City (65803) requires Making Introductions (65801)
- By Broken Road (65940) requires For Food and Rivalry (65804)
- Covering Their Tails (66024) requires The Khanam Matra (66022)
- The Nokhud Threat (66025) requires Trucebreakers (66023)
- Catching Wind (66236) requires Toting Totems (66225)
- Oh No, Ohn'ahra! (66258) requires Eagle-itarian (66256)
- Stormbreaker (66337) requires Deconstruct Additional Pylons (66335)
- Clans of the Plains (66969) requires Honoring Our Ancestors (66019)
- The Hunting Hound (67921) requires The Trouble with Taivan (67772)
- Try Again, Taivan! (68083) requires Part of a Pack (70989
- The Gentle Giant (68084) requires Try Again, Taivan! (68083)
- Shaping a Shepherd (68085) requires The Gentle Giant (68084)
- Danger in Daruukhan (68087) requires Reign of the Ram (71022)
- Saving Centaur (69094) requires Danger in Daruukhan (68087)
- Homeward Hound (69095) requires Saving Centaur (69094)
- Taivan's Purpose (69096) requires Homeward Hound (69095)
- Part of a Pack (70989) requires The Hunting Hound (67921)
- Reign of the Ram (71022) requires Shaping a Shepherd (68085)

The Azure Span:
- Tome-ward Bound (65848) requires Cut Out the Rot (65844)
- Straight to the Top (65852) requires Driven Mad (65702)
- Reclaiming the Oathstone (65854) requires Platform Adjustments (65751)
- Supplies! (65870) requires Snap the Traps (65866)
- Gnoll Way Out (65871) requires Snap the Traps (65866)
- Ill Gnolls with Ill Intent (65872) requires Snap the Traps (65866)
- Leader of the Shadepaw Pack (65873) requires Snap the Traps (65866)
- Kirin Tor Recovery (65977) requires Lava Burst (65944)
- Free Air (66007) requires Primal Power (65958)
- Can We Keep It? (66223) seems to require Scampering Scamps (66218)
- Spreading Decay (66239) requires Gnoll Way Out (65871)
- Setting the Defense (66489) seems to require WANTED: Frigellus (66488)
- Ways of Seeing (66500) requires Suspiciously Quiet (69904)
- For The Love of Others (66503) seems to require Ways of Seeing (66500)
- Assemble the Defenses (67033) requires The Azure Wizard (70747) for Dracthyr
- Preservation of Knowledge (67035) requires The Azure Wizard (70747) for Dracthyr
- How To Stop An Exploding Toy Boat (67175) requires Arcane Detection (67174)
- Needles to Say (68642) requires Mossing the Mark (68641) , might require Prowling Polar Predators (68639)
- Vitamins and Minerals (68643) requires Mossing the Mark (68641) , might require Prowling Polar Predators (68639)
- Sugar, Spice, and Everything Nice (68644) requires Vitamins and Minerals (68643) , might require Needles to Say (68642)
- Save a Slyvern (69862) requires Sugar, Spice, and Everything Nice (68644)
- Toejam the Terrible (70129) requires Rowie (66558)
- Sad Little Accidents (70168) seems to require The Joy of Painting (70166)
- They Took the Kits (70338) requires Save a Slyvern (69862)
- The Azure Wizard (70747) requires Shades of Blue (70746)
- For Blue Eyes Only (70748) requires Wayward Archivists (71182)
- A Claw in Need (71095) requires Help Is Our Way! (71094)
- Is A Claw Indeed (71096) requires A Claw in Need (71095)
- A Helping Claw (71097) requires Is A Claw Indeed (71096)
- Setting Your Very Own Net (72584) seems to require <NONAME> (70793) and Iskaaran Fishing Net (70871)

Thaldraszus:
- The Once and Future Team (65938) requires Quelling Causalities (66646)
- Return to the Present (66032) requires Resistance Isn't Futile (66030)
- To the... Past? (66033) doesn't require Temporal Two-ning (72519)
- Back to Reality (66037) seems to require Deathwingurlugull! (70371) for the Horde
- Feels Like the First Time (66083) requires Time is Running Out (66081)
- Closing Time (66087) requires Times Like These (66084)
- Southern Exposure (66167) requires Nowhere to Hide (66163)
- Remember the Fallen (66245) requires Vengeance, Served Hot (66169)
- Slightly Used Weapons (66247) requires Vengeance, Served Hot (66169)
- Tying Things Together (66248) requires Vengeance, Served Hot (66169)
- Clear the Sky (66249) requires Slightly Used Weapons (66247)
- Rebels With a Cause (70838) requires Follow the Clues (70837)
- Detonation Locations (70842) requires Follow the Clues (70837)
- Maldra's in Hot Water (70850) requires Ruin the Runestones (70843) , may require Rebels With a Cause (70838) & Detonation Locations (70842)
- Chasing Waterfalls (70873) requires Maldra's in Hot Water (70850)
- To Breach a Fire Wall (70874) requires Chasing Waterfalls (70873)
- Worst of the Worst (70875) requires To Breach a Fire Wall (70874)
- Fracture the Foci (70876) requires To Breach a Fire Wall (70874)
- Ring of Fire (70878) requires To Breach a Fire Wall (70874)
- Report on the Rebels (70879)  requires Ring of Fire (70878) , may require Worst of the Worst (70875) & Fracture the Foci (70876)

Azmerloth:
- Deathwingurlugull! (70371) requires Murloc Motes (66035) , seems to require Mugurlglrlgl! (66704)

Professions:
- The Wonders of the World (67298) requires That's My Specialty (67295)
- The Master of Their Craft (69946) requires That's My Specialty (67295)

---
## [Conga0/Mo_Creeps](https://github.com/Conga0/Mo_Creeps)@[70a83af006...](https://github.com/Conga0/Mo_Creeps/commit/70a83af0068af04711eeff105e563411c8e9be8e)
#### Saturday 2022-12-10 13:44:03 by Conga Lyne

New Creep, Various Fixes, Heat Asthete work

Adjusted Toxic Worm Nest's ceiling to look more cave-like and natural
Fixed Abandoned Orchestra blowing himself up in rage
Fixed Trophy Room Statues not spawning if you mod restarted before going near them
Fixed Revenge Reflection not showing it's full description
Slightly Reduced the health of Glu Slugs, they should die faster now, especially if you start with bouncing burst
Added a visual timer for Creature Shifting's cooldown if you have the fungal timer mod
Added a ui icon for killing the Aesthete of Heat (still not currently spawnable, will be done when boss is finished)
Slightly reduced speed of Aesthete of Heat's revenge fire bolts
Lava Immunity Buff now lasts 50% longer from eating Infernal Meat
Divine Being & Aesthete of Heat are now immune to slice damage (homing omega sawblade & forget builds for easy kills felt underwhelmin)
Divine Being no longer gains immunity frames upon taking damage
Sharply reduced Aesthete of Heat's revenge firebolt damage, 200 damage per bolt was.. a lot. Yeah.
New Creep: Leaky Slime, leaks hazardous liquids ontop of you

---
## [zhenli1347/terminal](https://github.com/zhenli1347/terminal)@[f2ebb21bd1...](https://github.com/zhenli1347/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Saturday 2022-12-10 13:44:16 by Mike Griese

Add snap-layouts support to the Terminal (#11680)

Adds snap layout support to the Terminal's maximize button. This PR is
full of BODGY, so brace yourselves.

Big thanks to Chris Swan in #11134 for building the prototype.
I don't believe this solves #8795, because XAML islands can't get
nchittest messages

- The window procedure for the drag bar forwards clicks on its client
  area to its parent as non-client clicks.
- BODGY: It also _manually_ handles the caption buttons. They exist in
  the titlebar, and work reasonably well with just XAML, if the drag bar
  isn't covering them.
- However, to get snap layout support, we need to actually return
  `HTMAXBUTTON` where the maximize button is. If the drag bar doesn't
  cover the caption buttons, then the core input site (which takes up
  the entirety of the XAML island) will steal the `WM_NCHITTEST` before
  we get a chance to handle it.
- So, the drag bar covers the caption buttons, and manually handles
  hovering and pressing them when needed. This gives the impression that
  they're getting input as they normally would, even if they're not
  _really_ getting input via XAML.
- We also need to manually display the button tooltips now, because XAML
  doesn't know when they've been hovered for long enough. Hence, the
  `_displayToolTip` `ThrottledFuncTrailing`

## Validation
Minimized, maximized, restored down, hovered the buttons slowly, moved
the mouse over them quickly, they feel the same as before. But now with
snap layouts appearing.

## TODO!
* [x] I'm working on getting the ToolTips on the caption buttons back. Alas, I needed a demo of this _today_, so I'll fix that tomorrow morning.
* [x] mild concern: I should probably test Win 10 to make sure there wasn't weird changes to the message loop in win11 that means this is broken on win10.
* [x] I think I used the wrong issue number for tons of my comments throughout this PR. Double check that. Should be #9443, not #9447. 

Closes #9443
I thought this took care of #8587 ~as a bonus, because I was here, and the fix is _now_ trivial~, but looking at the latest commit that regressed.

Co-authored-by: Chris Swan <chswan@microsoft.com>

---
## [zhenli1347/terminal](https://github.com/zhenli1347/terminal)@[442432ea15...](https://github.com/zhenli1347/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Saturday 2022-12-10 13:44:16 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [lllgts/android_kernel_xiaomi_polaris](https://github.com/lllgts/android_kernel_xiaomi_polaris)@[c5d842f62d...](https://github.com/lllgts/android_kernel_xiaomi_polaris/commit/c5d842f62db0a03743c8c16c199d157822f2e39c)
#### Saturday 2022-12-10 13:46:53 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>

---
## [crawl/crawl](https://github.com/crawl/crawl)@[1352289c90...](https://github.com/crawl/crawl/commit/1352289c90d15a53f9c472dac9343ad61d9104a7)
#### Saturday 2022-12-10 15:13:40 by Nicholas Feinberg

New species: Meteoran

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species!
Meteorae have an exciting variety of bonuses - great attributes
and aptitudes across the board, passive mapping, and exploration
healing, regaining HP and MP when viewing new territory. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Meteorae are humanoid beings. (In the night sky, they look
  like dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Meteorae's LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- Meteorae glow in the dark. Permanent backlit status (not halo!):
  +enemy to hit, -stealth, disables invis. Suppressed in forms.
  Seems funny.

Credit to hellmonk for the initial version of this species and
pushing to make 'em happen. :)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0883d36c9d...](https://github.com/treckstar/yolo-octo-hipster/commit/0883d36c9dd91b63ecb95f77b301d38d23b1b443)
#### Saturday 2022-12-10 15:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ghostwriter/laminas-continuous-integration-action](https://github.com/ghostwriter/laminas-continuous-integration-action)@[a0e1b235fa...](https://github.com/ghostwriter/laminas-continuous-integration-action/commit/a0e1b235faf25781121413bd82ceba29e3c38e78)
#### Saturday 2022-12-10 16:27:57 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [a-person-you-dont-know123/garrysmod-chatsounds](https://github.com/a-person-you-dont-know123/garrysmod-chatsounds)@[35dee955a9...](https://github.com/a-person-you-dont-know123/garrysmod-chatsounds/commit/35dee955a9ae01494db3c127d7e83b653d479e32)
#### Saturday 2022-12-10 16:30:30 by Mike

10 years in the joint made you a fuckin pussy

fuck you

---
## [a-person-you-dont-know123/garrysmod-chatsounds](https://github.com/a-person-you-dont-know123/garrysmod-chatsounds)@[088f7ca630...](https://github.com/a-person-you-dont-know123/garrysmod-chatsounds/commit/088f7ca6306dd083b7a32f59683f1e3d49187f9c)
#### Saturday 2022-12-10 16:30:30 by Sensuka

more tf2 chatsounds in tf2_extras folder (#420)

* More Killing Floor Chatsounds

the title speaks for itself, it adds more killing floor chatsounds, hurray.

* more killing floor sounds, again

same thing but different sounds

* Delete and she never listened.ogg

* Delete ha ha ha haaa.ogg

* Delete heheheheheheh.ogg

* Delete i always told her.ogg

* Delete id make something of myself.ogg

* killing floor patriarch

adds more patriarch

* killing floor chatsounds

the title again speaks, it adds a few sounds from killing floor

* more tf2 chatsounds in tf2_extra folder

for shits & giggles

---
## [yogan/advent-of-code](https://github.com/yogan/advent-of-code)@[c0325b9366...](https://github.com/yogan/advent-of-code/commit/c0325b93669587e0b68b34c42e4b17d958557dab)
#### Saturday 2022-12-10 16:52:17 by Frank Blendinger

Add day 09 part 2 (Nim)

Holy fuck, this was painful. Visualizing the rope DOES help. I learned
the hard way.

---
## [LeDrascol/S.P.L.U.R.T-Station-13](https://github.com/LeDrascol/S.P.L.U.R.T-Station-13)@[8eec99b320...](https://github.com/LeDrascol/S.P.L.U.R.T-Station-13/commit/8eec99b3206e917bd711987a80422168de53f83d)
#### Saturday 2022-12-10 17:00:04 by LemonInTheDark

Caches GetJobName. Fuck you (#274)

* Caches GetJobName. Fuck you

This code made me deeply upset, WHY IS IT RECURSIVE WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY

* Centcom handling, properly this time

* Empties out real_job_name

* Sets real_job_name up in the right place

* Moves real_job_name to SSjob, uses modularTM

* Yeet

* Removes old code, swaps over to the SSjob list

* dme changes

* indents... comments

Co-authored-by: SandPoot <enric_gabirel@hotmail.com>

---
## [VoltageOS/frameworks_base](https://github.com/VoltageOS/frameworks_base)@[8a970a40e9...](https://github.com/VoltageOS/frameworks_base/commit/8a970a40e98fa57d5c2c2bf953e4ba00ebd5cab8)
#### Saturday 2022-12-10 17:47:29 by Joey Huab

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

Signed-off-by: Dmitrii <bankersenator@gmail.com>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[3efa9b5382...](https://github.com/Bjarl/Shiptest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Saturday 2022-12-10 18:07:43 by Zevotech

undoes a fuckup on a ruin (#1578)

* undoes a fuckup on a ruin
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
sets light range to 2 on the ruin areas of beach_colony.dmm
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the brackets) if you have tested your changes and this is ready for review. Leave unticked if you have yet to test your changes and this is not ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that any issues found during tested have been addressed.

## Why It's Good For The Game
the ruin is no longer pitch fucking dark in the middle of a daylit planet (hopefully)
<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
fix: changes light range to 2 on the areas of beach_colony
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

* im stupid

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[9499a1542b...](https://github.com/ss220-space/tgstation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Saturday 2022-12-10 18:31:26 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

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

---
## [MonkeMango/sidealleysqueaks-source](https://github.com/MonkeMango/sidealleysqueaks-source)@[15d48e8ec5...](https://github.com/MonkeMango/sidealleysqueaks-source/commit/15d48e8ec5a404c366b3a4a38e1894e69410cb88)
#### Saturday 2022-12-10 19:02:17 by MonkeMango

"Pulling is not possible" SHUT THE FUCK UP GIT YOU STUPID BITCH

🥵🥵

---
## [abesto/rust-monaco](https://github.com/abesto/rust-monaco)@[d8e4efbeb4...](https://github.com/abesto/rust-monaco/commit/d8e4efbeb4d05d964ecb47598311d81d931906b7)
#### Saturday 2022-12-10 19:09:31 by Zoltan Nagy

Fix (?) `CodeEditorLink`

When attempting to use `CodeEditorLink::with_editor`, in my use-case the
callback would never be invoked, and `with_editor` would always return
`None`. When printing the value of the link, I saw it *did* have a
`Some(...)` in there, so I suspect something was up with the way `Rc` /
borrows were used? I tried to understand exactly what's
happening, but got lost in the `Scope` / `Rc` / `RefCell` soup. Another
guess is that the `Scope` that got stored in the `Rc<RefCell>>` on
`CodeEditorLink` wasn't actually linked (heh) to the *real* scope, since
that was a copy of the `Scope`.

I'm kinda experimenting my way through a fairly big design space, and I
have *some* experience messing with `Rc` and friends, but I'm completely
new to Yew, so I'll document my thought process so you can more easily
tell me if / how I'm wrong.

* We only ever store `CodeEditorModel` inside an
  `Rc<RefCell<Option<CodeEditorModel>>>`. This smart pointer gets cloned
  to each new `CodeEditorLink` (instead of storing some reference to a
  `Scope`). This makes it easy to reason about
  what's going on - exactly the data we need is passed around, and it
  has a single place of storage.
* I dropped the feature of allowing a `CodeEditorLink` to be passed in,
  for two reasons:
  * `CodeEditorLink` didn't expose a public constructor, and the `.0`
    field is private, so there is in fact no way (AFAICT) to create a
    `CodeEditorLink`. This means the feature ... never worked? I think?
  * `ctx.prop()` gives us an &-reference, so to update the data in the
    `CodeEditorLink` passed in via props, we need internal mutability,
    which complicates things further. Dropping this allows the
    implementation to be simple, and user code can still store the
    `CodeEditorLink` instance received in the `on_editor_created`
    callback.

This however has a drawback: if user code wants to store the
`CodeEditorLink`, then (at least in functional components) we kinda
enforce double-rendering at startup: there's no clean way of saying
"re-render if the link changes, except the first time when I store some
special `None` value in the state". So:

* Added a public constructor
* Re-added the `link` property
* Wrapped the data in `CodeEditorModel` into a `RefCell` to enable
  internal mutability (no need for another wrapping `Rc`)

This is close, but there's *still* double-rendering, since we still
don't have anything in `CodeEditorLink` for a stable comparison across
rendering passes, *only* the reference to the model. Since that changes
once the editor is finished, we trigger a re-render.

The core of the problem is: `CodeEditorLink` gets cloned all over the
place, and we need some identifier that tells us if it's "the same"
`CodeEditorLink`. Since it can't be the data it's carrying (see above),
it has to be something else, and probably something synthetic.

And so: I added a simple synthetic ID to `CodeEditorLink` when it's
created using an atomic counter, and implemented `PartialEq` in terms of
that field.

At this point this is working for me as I expect it to, so submitting
in a PR seems like a good idea.

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[ce39f048bf...](https://github.com/morrowwolf/cmss13/commit/ce39f048bf5eb25e2a93d7355327ccacc0504b01)
#### Saturday 2022-12-10 20:09:07 by carlarctg

Buffed, resprited, enhanced Oppressor. (#1732)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

**Resprited Oppressor! Pics here:**


![image](https://user-images.githubusercontent.com/53100513/204121775-9f4acd11-d818-46e8-81d3-c38bdfdabf5c.png)

Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Oppressor can hook over the M2C and M56D again.

Oppressor can hook over ledges. (UNIMPLEMENTED)

Tail stab's main ability usage is moved to a different proc for future
custom tail stabs.

Redesigned Tail Stab for Oppressor. Tail seize now utilizes a projectile
and beams to fire a 3-tile reaching tail hook, that pulls in AND DOES
NOT STUN marines. (It slows them for 0.5 seconds)

![Screenshot_20221127-032533~2](https://user-images.githubusercontent.com/53100513/204122365-e1ee57f7-1b9d-443e-a45c-dceec07a88d3.png)

Oppressor's abduct has had its effect strings changed to imply coiling
and uncoiling of the tail. Captured targets will now have a beam of the
Oppressor's tail attached to them (Purely visual) until they reach the
Praetorian, alongside an overlay of the vice grip on their legs.

Added a proc, .ammo/on_bullet_generation(), for the ammo datum to apply
effects to the generated bullet/projectile.

Added the bound_beam variable to projectiles. Could be used in the
future for things like harpoon guns, lasers, etc.

Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

Videos tomorrow.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Animated telegraphs looked really cool, but (I presume) were removed
because BYOND sometimes freezes or starts animations midway through when
short lived animated objects show up, for some reason. I effectively
made it so these are irrelevant by slapping on the border - The animated
effects are just a bonus and will not impact visibility, and in fact
enhance it.

> Oppressor can hook over the M2C and M56D again.

Everyone I've talked to agrees that there really is no reason for these
weapons to protect from abduction. The player can just.. move out of the
way, or even rest if they're in a crowded spot. It's also very
frustrating to see it get in the way of *other* abducts that bonk into
it. The player is going immobile in range of a xenomorph that punishes
immobility.

> Oppressor can hook over ledges. (UNIMPLEMENTED)

Couldn't replicate this issue for some reason... So uh. I dunno.

> Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)

Geeves approved.

This looks so fucking awesome. The slow is barely a thing, so I wouldn't
fret about slow creep. The reaching hook does no damage, only pulls
targets closer. This isn't necessarily super strong, but it's mega cool
and fits with Oppressor's theme of dislocation. I also changed the
windup from 1s to 0.5s so it can be utilized during combat, but this
could be reverted if it's too strong somehow.

> Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

This looked stinky on the tail seize.

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

:cl: Carlarc, Mikola Wei

imageadd: Resprited Oppressor, sprites made by Mikola Wei.
imageadd: Re-added animated telegraphs for Abduction. They've been
tweaked to always have the default border - that way, the weird way
byond handles short-lived animated objects doesn't make the telegraph
absurdly small. It can always be easily seen.
balance: Oppressor can hook over the M2C and M56D again.
refactor: Tail stab's main ability usage is moved to a different proc
for future custom tail stabs.
add: Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)
imageadd: Oppressor's abduct has had its effect strings changed to imply
coiling and uncoiling of the tail. Captured targets will now have a beam
of the Oppressor's tail attached to them (Purely visual) until they
reach the Praetorian, alongside an overlay of the vice grip on their
legs.
refactor: Added a proc, .ammo/on_bullet_generation(), for the ammo datum
to apply effects to the generated bullet/projectile.
refactor: Added the bound_beam variable to projectiles. Could be used in
the future for things like harpoon guns, lasers, etc.
fix: Fixed non-damaging projectiles causing a blood spurt. (It was
checking flags && FLAG instead of flag & flag, remember to use
CHECK_BITFIELD folks!)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

Co-authored-by: harryob <me@harryob.live>

---
## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[0b9264ce5f...](https://github.com/Tastyfish/Skyrat-tg/commit/0b9264ce5f14565e42d5e3dc67660a95f5d48f65)
#### Saturday 2022-12-10 20:38:05 by SkyratBot

[MIRROR] Fixes mineral turfs having weird lighting [MDB IGNORE] (#17618)

* Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

* Fixes mineral turfs having weird lighting

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [hinto-janaiyo/gupax](https://github.com/hinto-janaiyo/gupax)@[4da775667b...](https://github.com/hinto-janaiyo/gupax/commit/4da775667b46e9fb9f2fb1a83a3b23d4d4bee1dc)
#### Saturday 2022-12-10 20:44:56 by hinto-janaiyo

windows/pty: include static [VCRUNTIME140.dll], change PTY size

Bare metal windows was complaining about this DLL, so it is now
included statically using [https://docs.rs/static_vcruntime/].
I tried statically linking everything for Windows but:
	1. It's not necessary, pretty much all DLLs needed
	   (except this one) are included in Windows 7+ by default
	2. It's a pain in the ass to build everything
	   statically, especially since Gupax needs OpenSSL.
	   (building OpenSSL on Windows == hell)

Windows/macOS were having console artifacts, escape codes and
random newlines would show up in P2Pool/XMRig output. After
thinking about it for a while, I realized I left the PTY
size to the default [24 rows/80 columns], hence the PTYs
prematurely inserting newlines and weird escape codes.

It works fine after setting it to [100/1000]. Interestingly,
Linux worked completely fine on 24/80, probably resizes internally.

---
## [abesto/rust-monaco](https://github.com/abesto/rust-monaco)@[e317a37415...](https://github.com/abesto/rust-monaco/commit/e317a37415efdeb03bdaed39a7f34bdfd24e9d94)
#### Saturday 2022-12-10 21:01:54 by Zoltan Nagy

Fix (?) `CodeEditorLink`

When attempting to use `CodeEditorLink::with_editor`, in my use-case the
callback would never be invoked, and `with_editor` would always return
`None`. When printing the value of the link, I saw it *did* have a
`Some(...)` in there, so I suspect something was up with the way `Rc` /
borrows were used? I tried to understand exactly what's
happening, but got lost in the `Scope` / `Rc` / `RefCell` soup. Another
guess is that the `Scope` that got stored in the `Rc<RefCell>>` on
`CodeEditorLink` wasn't actually linked (heh) to the *real* scope, since
that was a copy of the `Scope`.

I'm kinda experimenting my way through a fairly big design space, and I
have *some* experience messing with `Rc` and friends, but I'm completely
new to Yew, so I'll document my thought process so you can more easily
tell me if / how I'm wrong.

## Attempt 1

* We only ever store `CodeEditorModel` inside an
  `Rc<RefCell<Option<CodeEditorModel>>>`. This smart pointer gets cloned
  to each new `CodeEditorLink` (instead of storing some reference to a
  `Scope`). This makes it easy to reason about
  what's going on - exactly the data we need is passed around, and it
  has a single place of storage.
* I dropped the feature of allowing a `CodeEditorLink` to be passed in,
  for two reasons:
  * `CodeEditorLink` didn't expose a public constructor, and the `.0`
    field is private, so there is in fact no way (AFAICT) to create a
    `CodeEditorLink`. This means the feature ... never worked? I think?
  * `ctx.prop()` gives us an &-reference, so to update the data in the
    `CodeEditorLink` passed in via props, we need internal mutability,
    which complicates things further. Dropping this allows the
    implementation to be simple, and user code can still store the
    `CodeEditorLink` instance received in the `on_editor_created`
    callback.

This however has a drawback: if user code wants to store the
`CodeEditorLink`, then (at least in functional components) we kinda
enforce double-rendering at startup: there's no clean way of saying
"re-render if the link changes, except the first time when I store some
special `None` value in the state". So:

## Attempt 2

* Added a public constructor
* Re-added the `link` property
* Wrapped the data in `CodeEditorModel` into a `RefCell` to enable
  internal mutability (no need for another wrapping `Rc`)

This is close, but there's *still* double-rendering in some
circumstances. The core problem is: we don't have anything in
`CodeEditorLink` for a stable comparison across rendering passes,
*only* the reference to the model. Since that changes once the editor
is created, the `CodeEditorLink` is also considered to have changed.

I messed around with a synthetic id, but didn't manage to get the
behavior I wanted; ended up using `TextModel` instead to get the text
out of the editor.

Again, this is not perfect; in particular, if `on_editor_created`
depends on the `CodeEditorLink`, then we get double-rendering. But I
figure it's an improvement still, so submitting the PR.

---
## [Xsard/Portafolio](https://github.com/Xsard/Portafolio)@[76471577f7...](https://github.com/Xsard/Portafolio/commit/76471577f7074c13bf0eac8ff9be3bc7a83c6406)
#### Saturday 2022-12-10 21:48:52 by Ignacio Korenhof

THE ONE ALWAYS FOR U

Lay beside me
Tell me what they've done
Speak the words I wanna hear
To make my demons run

The door is locked now
But it's opened if you're true
If you can understand the me
Then I can understand the you

Lay beside me, under wicked sky
Through black of day, dark of night
We share this, paralysed
The door cracks open
But there's no sun shining through
Black heart scarring darker still

But there's no sun shining through
No, there's no sun shining through
No, there's no sun shining

What I've felt, what I've known
Turn the pages, turn the stone
Behind the door, should I open it for you?
Yeah, what I've felt, what I've known
Sick and tired, I stand alone
Could you be there?
'Cause I'm the one who waits for you
Or are you unforgiven too?

Come lay beside me
This won't hurt, I swear
She loves me not, she loves me still
But she'll never love again
She laid beside me but she'll be there when I'm gone
Black heart scarring darker still

Yes, she'll be there when I'm gone
Yes, she'll be there when I'm gone
Dead sure she'll be there

What I've felt, what I've known
Turn the pages, turn the stone
Behind the door, should I open it for you?
Yeah, what I've felt, what I've known
Sick and tired, I stand alone
Could you be there?
'Cause I'm the one who waits for you
Or are you unforgiven too?

Lay beside me
Tell me what I've done
The door is closed, so are your eyes
But now I see the sun
Now I see the sun
Yes, now I see it

What I've felt, what I've known
Turn the pages, turn the stone
Behind the door, should I open it for you?
Yeah, what I've felt, what I've known
So sick and tired of staying alone
Could you be there?
'Cause I'm the one who waits
The one who waits for you

What I've felt, what I've known
Turn the pages, turn the stone
Behind the door, should I open it for you?
(So I dub thee unforgiven)

Oh, what I've felt
Oh, what I've known
I take this key (never free)
And I bury it (never me) in you
Because you're unforgiven, too
(Never free, never me)
'Cause you're unforgiven, too

---
## [Eneocho/vgstation13](https://github.com/Eneocho/vgstation13)@[496d3bb777...](https://github.com/Eneocho/vgstation13/commit/496d3bb777d9538dd05b57d9a042acffd6496741)
#### Saturday 2022-12-10 21:51:34 by ValkyrieSkies

Med/Sci mapping changes on Metaclub, also Bridge lightswitch (#33197)

* Metaclub Science Improvements

* Feature creep

* Fixes the god awful bridge wallpipes

---
## [copperwater/xNetHack](https://github.com/copperwater/xNetHack)@[dc35c12e7f...](https://github.com/copperwater/xNetHack/commit/dc35c12e7f8fc43ffbecf145820200ce920d68c2)
#### Saturday 2022-12-10 22:32:37 by copperwater

Implement boss-blocking of magic mapping

One main motivation of this is for the Quest, preventing the hero from
peeking ahead on certain levels (such as the Archeologist locate, lower
filler, and goal levels) to see how the terrain got generated and where
the hidden secrets are. But at the same time, it doesn't really make
sense to mark the levels as strictly unmappable, because the nemesis may
be the force preventing you from mapping them. And it may not work just
to clear the nommap flag, since you could kill the enemy off-level.

The solution here is to expand the nommap flag to 2 bits to allow a
third value, "boss blocked", which if magic mapping is attempted checks
whether the local boss has been defeated and if not will not allow you
to map. It works somewhat similarly to demon lord teleport blocking but
not quite the same: demon lords take their teleport blocking to any
level they are on, whereas here it only applies in the lair but still
applies if the enemy is alive but off-level. (Otherwise it could be
pretty easy just to quaff cursed invisibility, let the enemy warp to
you, take them upstairs and return without them, and then map the level
in their absence.)

Note that it's up to the level designer to apply this new flag; if left
unspecified the level will still be mappable even if there is a boss
present, and if specified as "nommap" it will still be never mappable
even after the boss has been killed.

I have applied this change to the four demon lord lairs and certain
Quest levels I have redesigned. Quest levels I have not touched remain
the same as in vanilla. This could be extended for other boss lairs like
the Wizard's Tower, Medusa, and Vlad's Tower, but none of those felt
particularly important to prevent mapping on.

---
## [gurfan/vgstation13](https://github.com/gurfan/vgstation13)@[e6156a8d91...](https://github.com/gurfan/vgstation13/commit/e6156a8d91d8a24ebe6437f07198713f76946fc1)
#### Saturday 2022-12-10 22:39:08 by samo priimek

pulse demon tweaks (#33690)

* remove the stupid maxcharge tweak

* sneed

* comment unused stuff

* revert everything

* prevent you from killing yourself stupidly

* suck SMES faster, gain maxcharge when sucking APC's

* remove the capacity upgrade

* tweak the ability costs and upgrades

---
## [PolGubau/stickies](https://github.com/PolGubau/stickies)@[57d546ab1b...](https://github.com/PolGubau/stickies/commit/57d546ab1ba2419c88710748a225f43eaf912f2f)
#### Saturday 2022-12-10 22:39:24 by Pol Gubau

Pol; Master; Last Christmas I gave you my heart
But the very next day you gave it away
This year, to save me from tears
I'll give it to someone special
Last Christmas I gave you my heart
But the very next day you gave it away
This year, to save me from tears
I'll give it to someone special
Once bitten and twice shy
I keep my distance, but you still catch my eye
Tell me baby, do you recognize me?
Well, it's been a year, it doesn't surprise me
Happy Christmas, I wrapped it up and sent it
With a note saying "I love you", I meant it
Now I know what a fool I've been
But if you kissed me now, I know you'd fool me again
Last Christmas I gave you my heart
But the very next day you gave it away
This year, to save me from tears
I'll give it to someone special
Last Christmas I gave you my heart
But the very next day you gave it away
This year, to save me from tears
I'll give it to someone special
Ooh
Oh, oh, baby
A crowded room, friends with tired eyes
I'm hiding from you and your soul of ice
My God, I thought you were someone to rely on
Me? I guess I was a shoulder to cry on
A face on a lover with a fire in his heart
A man under cover, but you tore me apart
Oh, oh now I've found a real love
You'll never fool me again
Last Christmas I gave you my heart
But the very next day you gave it away
This year, to save me from tears
I'll give it to someone special, special
Last Christmas I gave you my heart
But the very next day you gave it away
This year, to save me from tears
I'll give it to someone special
Special
A face on a lover with a fire in his heart (I gave you mine)
A man under cover but you tore him apart
Maybe next year I'll give it to someone
I'll give it to someone special

---
## [argonui/SCED](https://github.com/argonui/SCED)@[b5fbe4d0db...](https://github.com/argonui/SCED/commit/b5fbe4d0db1ba5b7ecb2547c5f46497b246e7293)
#### Saturday 2022-12-10 23:04:30 by bootleggerFinn

Initial 2.4.0

Rearranged table for new campaign
Previously featured community content converted to downloader versions
Updated/Added Following content: The Scarlet Keys, Celtic Rising, Jumanji, Machining a Mystery, Dr. Jekyll and Mr. Hyde, CYOA Campaign Guides, Dead Space Investigators, Aespa Investigators, Magical Girl Project, Streets of New Capenna, The Bad Batch, Arkham Fantasy  Pixel Art Mini-Cards
Updated snap points
Updated spawn position of standalone scenarios/challenge scenarios memory bags

---
## [vncsreis/HeroicGamesLauncher](https://github.com/vncsreis/HeroicGamesLauncher)@[3f6541c8a7...](https://github.com/vncsreis/HeroicGamesLauncher/commit/3f6541c8a700511cea9f0c9b572a5d2138ee76e3)
#### Saturday 2022-12-10 23:44:33 by Mathis Dröge

Improve README and developer experience (#1807)

* Update VSCode configuration

* Lots of README changes

- Update our bages; might've overdone it a little, but they're fun to add :^)
- Add badges for Web Technologies used
- Rewrite & bump up system requirements a bit
- Wrap the Language list, Development in a container, and Screenshots in
  <details>; this makes the page load faster and makes it seem less
  daunting
- Add a Flathub badge to the Flatpak section
- Unify Linux install instructions (as much as possible)
- Remove 3rd-party APT repository
  In my opinion, we have enough distribution formats already, and the
  install instructions are a little dodgy
- Add Beta AUR package to the list
- Clarify Windows install instructions by splitting up WinGet and manual
  install
- Make "Development environment" its own section
- Remove Beta and Alpha notes on Windows and macOS build instructions
- Explain what exactly is happening when you run `yarn dev` and in which
  scenarios you might want to use it
- Move the "Back to top" badge to the actual bottom of the page

* Add a Content Security Policy

This doesn't really do much in our situation:
- Just in case someone ever manages to load a website in Heroic's main
  window, no JS can run inside it
- Gets rid of the warning in the console when testing with `yarn dev`

I've tested the Webviews (unaffected) and links to ProtonDB and such
(also unaffected, not sure why though). Please test if this breaks
anything

---

