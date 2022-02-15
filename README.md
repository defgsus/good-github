## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-14](docs/good-messages/2022/2022-02-14.md)


1,678,831 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,678,831 were push events containing 2,639,006 commit messages that amount to 218,242,448 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[efdc3e2fa3...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/efdc3e2fa384a29feb255cdd4491c864211ca1c5)
#### Monday 2022-02-14 00:07:51 by AmCath

Revert "Revert "alt Tammany portrait should they say fuck you democracy""

This reverts commit 92e384499310046f8df9a8840d8c69cc7b887b81.

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[fc97f45e5b...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/fc97f45e5b79e588518992f61f8f7bd73456b0b1)
#### Monday 2022-02-14 00:14:47 by Dan Barnes

Revert "Revert "Revert "alt Tammany portrait should they say fuck you democracy"""

This reverts commit efdc3e2fa384a29feb255cdd4491c864211ca1c5.

---
## [Sad-EyedLadyoftheLowlands/rabbit-chat](https://github.com/Sad-EyedLadyoftheLowlands/rabbit-chat)@[118eda2ba2...](https://github.com/Sad-EyedLadyoftheLowlands/rabbit-chat/commit/118eda2ba259ac525add30ac24d319942de0bc6a)
#### Monday 2022-02-14 00:22:14 by Dylan Baird

MAJOR CHANGES - Accept friend request implemented with no error handling. MAJOR PROBLEM - discovered that friends are not working at all as you can only have one relationship at a time - completely idiotic.

---
## [GForceTF/tgstation](https://github.com/GForceTF/tgstation)@[906fb0682b...](https://github.com/GForceTF/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Monday 2022-02-14 00:31:23 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [JenqaDev/tgstation](https://github.com/JenqaDev/tgstation)@[a2fa7799f3...](https://github.com/JenqaDev/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Monday 2022-02-14 00:46:32 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[83ae4d8c0e...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/83ae4d8c0e1bddc1ec38e96d9fd77c1f15a3f8a9)
#### Monday 2022-02-14 00:57:36 by Todd Howard

You tell me do this, He tells me do that. You're all bastards, Go fuck your mother.

---
## [team8/drive-practice-2022](https://github.com/team8/drive-practice-2022)@[9b9d6e1665...](https://github.com/team8/drive-practice-2022/commit/9b9d6e166564556556b3fb2bc34ae6f4dbba390d)
#### Monday 2022-02-14 01:38:51 by Charger1256A

Have you ever tried using an existing timer library in react native Well if not, dont they all absolutely suck. If you want a timer in react native you defentily should create your own, and if you are kinda please publish it so people all acrross the world can usie it. We dont want people wasting their time like me spending hours sifting through the junk filled internet to find a timer, and then when they realize there are no good timer libraries they are like :wear:. React native must create a timer component because they is their duty, it is the only ethical thing to to do, and it will make creating apps with timers signficantly easier. \n First of all react native must create a timer component because their sole purpose is not make life easy for their consumers. People are getting paid to make the consumers life easy, tell them to do thier damn job. I am very disapointed they have not done it. Like Albert Einstein once said, Your mom is fat, but DO YOUR WORK . Everyone know you can't argue with Mr. Albert because he is literally a genius. I would finish this fantastic essay, but I have to do my physics homework :cri:. If you would like to here more about this concerning topic, contact me at yourmom.com/yourmomyisbady.

---
## [nalind/openshift-api](https://github.com/nalind/openshift-api)@[5b82635ef1...](https://github.com/nalind/openshift-api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Monday 2022-02-14 02:18:36 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [R2NorthstarCN/NorthstarLauncher](https://github.com/R2NorthstarCN/NorthstarLauncher)@[db0af63704...](https://github.com/R2NorthstarCN/NorthstarLauncher/commit/db0af63704a6fbc57e80a9db01bbc01b79339d9f)
#### Monday 2022-02-14 02:36:52 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [HomebrewNLP/HomebrewNLP-Jax](https://github.com/HomebrewNLP/HomebrewNLP-Jax)@[1c23de3ac0...](https://github.com/HomebrewNLP/HomebrewNLP-Jax/commit/1c23de3ac07911519325262460ef56987672356a)
#### Monday 2022-02-14 03:29:03 by ClashLuke

fix(model): move idx to manual passing

seriously, fuck you jax

---
## [JAngeloD/convolutional-neural-networks-simplified](https://github.com/JAngeloD/convolutional-neural-networks-simplified)@[d409280e66...](https://github.com/JAngeloD/convolutional-neural-networks-simplified/commit/d409280e66b992ab47c35bb9988742b940c19876)
#### Monday 2022-02-14 04:43:47 by Entalize

Merge branch 'main' of https://github.com/JAngeloD/convolutional-neural-networks-simplified
Go fuck your self

---
## [rywndr/Programming-EBook](https://github.com/rywndr/Programming-EBook)@[97016edd67...](https://github.com/rywndr/Programming-EBook/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Monday 2022-02-14 04:43:49 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [hoopandango/BC_Extractor](https://github.com/hoopandango/BC_Extractor)@[9fa071c327...](https://github.com/hoopandango/BC_Extractor/commit/9fa071c327aaf5df4f1226ef57b6666597e8d50d)
#### Monday 2022-02-14 04:47:35 by Pan Dango

adding six talents is so funny lmao its so funny i swear its the funniest shit ever ponos is a god of humour hahaaha kms

updated data because next eventdata is due.

---
## [toxin06/Server](https://github.com/toxin06/Server)@[1928ce8173...](https://github.com/toxin06/Server/commit/1928ce8173662a477ba13696a88fb23041016ae9)
#### Monday 2022-02-14 05:29:58 by toxin06

Enable Bot Epics

This adds rules and commands to allow bots to use their epics.

^useepic <name> triggers the chosen bot to use their epic if it is equipped, this requires custom items and spells to work properly.
(See bottom for inserts)
Bots, MageEpicPet --- 0 disabled, 1 enabled requiring epic, 2 enabled no epic requirement.
Bots, MageEpicPetMinLvl --- Min level to allow Mages to use their epic pet if above rule criteria is met.
Bots, BotsUseEpicMinLvl --- Minimum level for bots to be able to use their clicky epic via command.

***Mage pet epic item***
INSERT INTO `items` (`id`, `minstatus`, `Name`, `aagi`, `ac`, `accuracy`, `acha`, `adex`, `aint`, `artifactflag`, `asta`, `astr`, `attack`, `augrestrict`, `augslot1type`, `augslot1visible`, `augslot2type`, `augslot2visible`, `augslot3type`, `augslot3visible`, `augslot4type`, `augslot4visible`, `augslot5type`, `augslot5visible`, `augslot6type`, `augslot6visible`, `augtype`, `avoidance`, `awis`, `bagsize`, `bagslots`, `bagtype`, `bagwr`, `banedmgamt`, `banedmgraceamt`, `banedmgbody`, `banedmgrace`, `bardtype`, `bardvalue`, `book`, `casttime`, `casttime_`, `charmfile`, `charmfileid`, `classes`, `color`, `combateffects`, `extradmgskill`, `extradmgamt`, `price`, `cr`, `damage`, `damageshield`, `deity`, `delay`, `augdistiller`, `dotshielding`, `dr`, `clicktype`, `clicklevel2`, `elemdmgtype`, `elemdmgamt`, `endur`, `factionamt1`, `factionamt2`, `factionamt3`, `factionamt4`, `factionmod1`, `factionmod2`, `factionmod3`, `factionmod4`, `filename`, `focuseffect`, `fr`, `fvnodrop`, `haste`, `clicklevel`, `hp`, `regen`, `icon`, `idfile`, `itemclass`, `itemtype`, `ldonprice`, `ldontheme`, `ldonsold`, `light`, `lore`, `loregroup`, `magic`, `mana`, `manaregen`, `enduranceregen`, `material`, `herosforgemodel`, `maxcharges`, `mr`, `nodrop`, `norent`, `pendingloreflag`, `pr`, `procrate`, `races`, `range`, `reclevel`, `recskill`, `reqlevel`, `sellrate`, `shielding`, `size`, `skillmodtype`, `skillmodvalue`, `slots`, `clickeffect`, `spellshield`, `strikethrough`, `stunresist`, `summonedflag`, `tradeskills`, `favor`, `weight`, `UNK012`, `UNK013`, `benefitflag`, `UNK054`, `UNK059`, `booktype`, `recastdelay`, `recasttype`, `guildfavor`, `UNK123`, `UNK124`, `attuneable`, `nopet`, `updated`, `comment`, `UNK127`, `pointtype`, `potionbelt`, `potionbeltslots`, `stacksize`, `notransfer`, `stackable`, `UNK134`, `UNK137`, `proceffect`, `proctype`, `proclevel2`, `proclevel`, `UNK142`, `worneffect`, `worntype`, `wornlevel2`, `wornlevel`, `UNK147`, `focustype`, `focuslevel2`, `focuslevel`, `UNK152`, `scrolleffect`, `scrolltype`, `scrolllevel2`, `scrolllevel`, `UNK157`, `serialized`, `verified`, `serialization`, `source`, `UNK033`, `lorefile`, `UNK014`, `svcorruption`, `skillmodmax`, `UNK060`, `augslot1unk2`, `augslot2unk2`, `augslot3unk2`, `augslot4unk2`, `augslot5unk2`, `augslot6unk2`, `UNK120`, `UNK121`, `questitemflag`, `UNK132`, `clickunk5`, `clickunk6`, `clickunk7`, `procunk1`, `procunk2`, `procunk3`, `procunk4`, `procunk6`, `procunk7`, `wornunk1`, `wornunk2`, `wornunk3`, `wornunk4`, `wornunk5`, `wornunk6`, `wornunk7`, `focusunk1`, `focusunk2`, `focusunk3`, `focusunk4`, `focusunk5`, `focusunk6`, `focusunk7`, `scrollunk1`, `scrollunk2`, `scrollunk3`, `scrollunk4`, `scrollunk5`, `scrollunk6`, `scrollunk7`, `UNK193`, `purity`, `evoitem`, `evoid`, `evolvinglevel`, `evomax`, `clickname`, `procname`, `wornname`, `focusname`, `scrollname`, `dsmitigation`, `heroic_str`, `heroic_int`, `heroic_wis`, `heroic_agi`, `heroic_dex`, `heroic_sta`, `heroic_cha`, `heroic_pr`, `heroic_dr`, `heroic_fr`, `heroic_cr`, `heroic_mr`, `heroic_svcorrup`, `healamt`, `spelldmg`, `clairvoyance`, `backstabdmg`, `created`, `elitematerial`, `ldonsellbackrate`, `scriptfileid`, `expendablearrow`, `powersourcecapacity`, `bardeffect`, `bardeffecttype`, `bardlevel2`, `bardlevel`, `bardunk1`, `bardunk2`, `bardunk3`, `bardunk4`, `bardunk5`, `bardname`, `bardunk7`, `UNK214`, `subtype`, `UNK220`, `UNK221`, `heirloom`, `UNK223`, `UNK224`, `UNK225`, `UNK226`, `UNK227`, `UNK228`, `UNK229`, `UNK230`, `UNK231`, `UNK232`, `UNK233`, `UNK234`, `placeable`, `UNK236`, `UNK237`, `UNK238`, `UNK239`, `UNK240`, `UNK241`, `epicitem`) VALUES (550005, 0, 'Orb of Mastery (Bot)', 0, 0, 0, 0, 5, 20, 0, 10, 15, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20000, 20000, '', '0', 4096, 4278190080, '0', 0, 0, 0, 20, 20, 0, 0, 30, 0, 0, 0, 4, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, 20, 1, 0, 0, 0, 0, 2868, 'IT151', 0, 3, 0, 0, 0, 15, 'Orb of Mastery', 0, 1, 100, 0, 0, 0, 0, 1, 10, 1, 1, 0, 0, 0, 34869, 0, 0, 0, 46, 1, 0, 0, -1, 0, 8192, 1936, 0, 0, 0, 0, 0, 0, 10, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '2012-12-27 10:34:55', '', 0, 0, 0, 0, 1, 0, 0, '', 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, NULL, '2011-12-11 01:53:39', NULL, '13THFLOOR', 0, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, '00000000000000000000', 0, '', 0, 0, 0, 0, 0, '', -1, 0, 0, 0, 0, 0, '', -1, 0, 0, 0, 0, 0, '', -1, 0, 0, 0, 0, 0, '', -1, 0, 0, 0, 0, 0, 0, '', '', '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '2004-02-03 13:29:35', 0, 70, 16543, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, 0, 0, 0, 0, 0, 0, 142, 0, 1, 0, 1036831949, 1075838976, 0, -1, 0, -256, 255, 0, 0, -2147483648, 63, 0, 0, 0, 1);

***Spells for useepic command***
INSERT INTO `spells_new` (`id`, `name`, `player_1`, `teleport_zone`, `you_cast`, `other_casts`, `cast_on_you`, `cast_on_other`, `spell_fades`, `range`, `aoerange`, `pushback`, `pushup`, `cast_time`, `recovery_time`, `recast_time`, `buffdurationformula`, `buffduration`, `AEDuration`, `mana`, `effect_base_value1`, `effect_base_value2`, `effect_base_value3`, `effect_base_value4`, `effect_base_value5`, `effect_base_value6`, `effect_base_value7`, `effect_base_value8`, `effect_base_value9`, `effect_base_value10`, `effect_base_value11`, `effect_base_value12`, `effect_limit_value1`, `effect_limit_value2`, `effect_limit_value3`, `effect_limit_value4`, `effect_limit_value5`, `effect_limit_value6`, `effect_limit_value7`, `effect_limit_value8`, `effect_limit_value9`, `effect_limit_value10`, `effect_limit_value11`, `effect_limit_value12`, `max1`, `max2`, `max3`, `max4`, `max5`, `max6`, `max7`, `max8`, `max9`, `max10`, `max11`, `max12`, `icon`, `memicon`, `components1`, `components2`, `components3`, `components4`, `component_counts1`, `component_counts2`, `component_counts3`, `component_counts4`, `NoexpendReagent1`, `NoexpendReagent2`, `NoexpendReagent3`, `NoexpendReagent4`, `formula1`, `formula2`, `formula3`, `formula4`, `formula5`, `formula6`, `formula7`, `formula8`, `formula9`, `formula10`, `formula11`, `formula12`, `LightType`, `goodEffect`, `Activated`, `resisttype`, `effectid1`, `effectid2`, `effectid3`, `effectid4`, `effectid5`, `effectid6`, `effectid7`, `effectid8`, `effectid9`, `effectid10`, `effectid11`, `effectid12`, `targettype`, `basediff`, `skill`, `zonetype`, `EnvironmentType`, `TimeOfDay`, `classes1`, `classes2`, `classes3`, `classes4`, `classes5`, `classes6`, `classes7`, `classes8`, `classes9`, `classes10`, `classes11`, `classes12`, `classes13`, `classes14`, `classes15`, `classes16`, `CastingAnim`, `TargetAnim`, `TravelType`, `SpellAffectIndex`, `disallow_sit`, `deities0`, `deities1`, `deities2`, `deities3`, `deities4`, `deities5`, `deities6`, `deities7`, `deities8`, `deities9`, `deities10`, `deities11`, `deities12`, `deities13`, `deities14`, `deities15`, `deities16`, `field142`, `field143`, `new_icon`, `spellanim`, `uninterruptable`, `ResistDiff`, `dot_stacking_exempt`, `deleteable`, `RecourseLink`, `no_partial_resist`, `field152`, `field153`, `short_buff_box`, `descnum`, `typedescnum`, `effectdescnum`, `effectdescnum2`, `npc_no_los`, `field160`, `reflectable`, `bonushate`, `field163`, `field164`, `ldon_trap`, `EndurCost`, `EndurTimerIndex`, `IsDiscipline`, `field169`, `field170`, `field171`, `field172`, `HateAdded`, `EndurUpkeep`, `numhitstype`, `numhits`, `pvpresistbase`, `pvpresistcalc`, `pvpresistcap`, `spell_category`, `pvp_duration`, `pvp_duration_cap`, `pcnpc_only_flag`, `cast_not_standing`, `can_mgb`, `nodispell`, `npc_category`, `npc_usefulness`, `MinResist`, `MaxResist`, `viral_targets`, `viral_timer`, `nimbuseffect`, `ConeStartAngle`, `ConeStopAngle`, `sneaking`, `not_extendable`, `field198`, `field199`, `suspendable`, `viral_range`, `songcap`, `field203`, `field204`, `no_block`, `field206`, `spellgroup`, `rank`, `field209`, `field210`, `CastRestriction`, `allowrest`, `InCombat`, `OutofCombat`, `field215`, `field216`, `field217`, `aemaxtargets`, `maxtargets`, `field220`, `field221`, `field222`, `field223`, `persistdeath`, `field225`, `field226`, `min_dist`, `min_dist_mod`, `max_dist`, `max_dist_mod`, `min_range`, `field232`, `field233`, `field234`, `field235`, `field236`) VALUES (25107, 'Torment of Shadows', 'PLAYER_1', '', '', '', 'Your mind is filled by fear and terror from the shadows.', ' is gripped by shadows of fear and terror.', 'The shadows release your mind.', 200, 0, 0, 0, 9000, 0, 0, 1, 16, 0, 0, -75, -10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2503, 2119, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 100, 102, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 1, 0, 3, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 5, 0, 14, -1, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 44, 13, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 161, 94, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1938, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, -99, 1, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0);
INSERT INTO `spells_new` (`id`, `name`, `player_1`, `teleport_zone`, `you_cast`, `other_casts`, `cast_on_you`, `cast_on_other`, `spell_fades`, `range`, `aoerange`, `pushback`, `pushup`, `cast_time`, `recovery_time`, `recast_time`, `buffdurationformula`, `buffduration`, `AEDuration`, `mana`, `effect_base_value1`, `effect_base_value2`, `effect_base_value3`, `effect_base_value4`, `effect_base_value5`, `effect_base_value6`, `effect_base_value7`, `effect_base_value8`, `effect_base_value9`, `effect_base_value10`, `effect_base_value11`, `effect_base_value12`, `effect_limit_value1`, `effect_limit_value2`, `effect_limit_value3`, `effect_limit_value4`, `effect_limit_value5`, `effect_limit_value6`, `effect_limit_value7`, `effect_limit_value8`, `effect_limit_value9`, `effect_limit_value10`, `effect_limit_value11`, `effect_limit_value12`, `max1`, `max2`, `max3`, `max4`, `max5`, `max6`, `max7`, `max8`, `max9`, `max10`, `max11`, `max12`, `icon`, `memicon`, `components1`, `components2`, `components3`, `components4`, `component_counts1`, `component_counts2`, `component_counts3`, `component_counts4`, `NoexpendReagent1`, `NoexpendReagent2`, `NoexpendReagent3`, `NoexpendReagent4`, `formula1`, `formula2`, `formula3`, `formula4`, `formula5`, `formula6`, `formula7`, `formula8`, `formula9`, `formula10`, `formula11`, `formula12`, `LightType`, `goodEffect`, `Activated`, `resisttype`, `effectid1`, `effectid2`, `effectid3`, `effectid4`, `effectid5`, `effectid6`, `effectid7`, `effectid8`, `effectid9`, `effectid10`, `effectid11`, `effectid12`, `targettype`, `basediff`, `skill`, `zonetype`, `EnvironmentType`, `TimeOfDay`, `classes1`, `classes2`, `classes3`, `classes4`, `classes5`, `classes6`, `classes7`, `classes8`, `classes9`, `classes10`, `classes11`, `classes12`, `classes13`, `classes14`, `classes15`, `classes16`, `CastingAnim`, `TargetAnim`, `TravelType`, `SpellAffectIndex`, `disallow_sit`, `deities0`, `deities1`, `deities2`, `deities3`, `deities4`, `deities5`, `deities6`, `deities7`, `deities8`, `deities9`, `deities10`, `deities11`, `deities12`, `deities13`, `deities14`, `deities15`, `deities16`, `field142`, `field143`, `new_icon`, `spellanim`, `uninterruptable`, `ResistDiff`, `dot_stacking_exempt`, `deleteable`, `RecourseLink`, `no_partial_resist`, `field152`, `field153`, `short_buff_box`, `descnum`, `typedescnum`, `effectdescnum`, `effectdescnum2`, `npc_no_los`, `field160`, `reflectable`, `bonushate`, `field163`, `field164`, `ldon_trap`, `EndurCost`, `EndurTimerIndex`, `IsDiscipline`, `field169`, `field170`, `field171`, `field172`, `HateAdded`, `EndurUpkeep`, `numhitstype`, `numhits`, `pvpresistbase`, `pvpresistcalc`, `pvpresistcap`, `spell_category`, `pvp_duration`, `pvp_duration_cap`, `pcnpc_only_flag`, `cast_not_standing`, `can_mgb`, `nodispell`, `npc_category`, `npc_usefulness`, `MinResist`, `MaxResist`, `viral_targets`, `viral_timer`, `nimbuseffect`, `ConeStartAngle`, `ConeStopAngle`, `sneaking`, `not_extendable`, `field198`, `field199`, `suspendable`, `viral_range`, `songcap`, `field203`, `field204`, `no_block`, `field206`, `spellgroup`, `rank`, `field209`, `field210`, `CastRestriction`, `allowrest`, `InCombat`, `OutofCombat`, `field215`, `field216`, `field217`, `aemaxtargets`, `maxtargets`, `field220`, `field221`, `field222`, `field223`, `persistdeath`, `field225`, `field226`, `min_dist`, `min_dist_mod`, `max_dist`, `max_dist_mod`, `min_range`, `field232`, `field233`, `field234`, `field235`, `field236`) VALUES (25106, 'Curse of the Spirits', 'PLAYER_1', '', '', '', 'Your body is consumed by the raging spirits of the land.', ' is consumed by the raging spirits of the land.', 'The spirits have subsided.', 100, 0, 0, 0, 9000, 0, 0, 1, 14, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2512, 2106, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 100, 100, 100, 100, 100, 122, 100, 100, 100, 100, 100, 100, 0, 0, 0, 1, 10, 10, 10, 10, 10, 0, 254, 254, 254, 254, 254, 254, 5, 0, 5, -1, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 12, 15, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 139, 107, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1932, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, -99, 1, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0);
INSERT INTO `spells_new` (`id`, `name`, `player_1`, `teleport_zone`, `you_cast`, `other_casts`, `cast_on_you`, `cast_on_other`, `spell_fades`, `range`, `aoerange`, `pushback`, `pushup`, `cast_time`, `recovery_time`, `recast_time`, `buffdurationformula`, `buffduration`, `AEDuration`, `mana`, `effect_base_value1`, `effect_base_value2`, `effect_base_value3`, `effect_base_value4`, `effect_base_value5`, `effect_base_value6`, `effect_base_value7`, `effect_base_value8`, `effect_base_value9`, `effect_base_value10`, `effect_base_value11`, `effect_base_value12`, `effect_limit_value1`, `effect_limit_value2`, `effect_limit_value3`, `effect_limit_value4`, `effect_limit_value5`, `effect_limit_value6`, `effect_limit_value7`, `effect_limit_value8`, `effect_limit_value9`, `effect_limit_value10`, `effect_limit_value11`, `effect_limit_value12`, `max1`, `max2`, `max3`, `max4`, `max5`, `max6`, `max7`, `max8`, `max9`, `max10`, `max11`, `max12`, `icon`, `memicon`, `components1`, `components2`, `components3`, `components4`, `component_counts1`, `component_counts2`, `component_counts3`, `component_counts4`, `NoexpendReagent1`, `NoexpendReagent2`, `NoexpendReagent3`, `NoexpendReagent4`, `formula1`, `formula2`, `formula3`, `formula4`, `formula5`, `formula6`, `formula7`, `formula8`, `formula9`, `formula10`, `formula11`, `formula12`, `LightType`, `goodEffect`, `Activated`, `resisttype`, `effectid1`, `effectid2`, `effectid3`, `effectid4`, `effectid5`, `effectid6`, `effectid7`, `effectid8`, `effectid9`, `effectid10`, `effectid11`, `effectid12`, `targettype`, `basediff`, `skill`, `zonetype`, `EnvironmentType`, `TimeOfDay`, `classes1`, `classes2`, `classes3`, `classes4`, `classes5`, `classes6`, `classes7`, `classes8`, `classes9`, `classes10`, `classes11`, `classes12`, `classes13`, `classes14`, `classes15`, `classes16`, `CastingAnim`, `TargetAnim`, `TravelType`, `SpellAffectIndex`, `disallow_sit`, `deities0`, `deities1`, `deities2`, `deities3`, `deities4`, `deities5`, `deities6`, `deities7`, `deities8`, `deities9`, `deities10`, `deities11`, `deities12`, `deities13`, `deities14`, `deities15`, `deities16`, `field142`, `field143`, `new_icon`, `spellanim`, `uninterruptable`, `ResistDiff`, `dot_stacking_exempt`, `deleteable`, `RecourseLink`, `no_partial_resist`, `field152`, `field153`, `short_buff_box`, `descnum`, `typedescnum`, `effectdescnum`, `effectdescnum2`, `npc_no_los`, `field160`, `reflectable`, `bonushate`, `field163`, `field164`, `ldon_trap`, `EndurCost`, `EndurTimerIndex`, `IsDiscipline`, `field169`, `field170`, `field171`, `field172`, `HateAdded`, `EndurUpkeep`, `numhitstype`, `numhits`, `pvpresistbase`, `pvpresistcalc`, `pvpresistcap`, `spell_category`, `pvp_duration`, `pvp_duration_cap`, `pcnpc_only_flag`, `cast_not_standing`, `can_mgb`, `nodispell`, `npc_category`, `npc_usefulness`, `MinResist`, `MaxResist`, `viral_targets`, `viral_timer`, `nimbuseffect`, `ConeStartAngle`, `ConeStopAngle`, `sneaking`, `not_extendable`, `field198`, `field199`, `suspendable`, `viral_range`, `songcap`, `field203`, `field204`, `no_block`, `field206`, `spellgroup`, `rank`, `field209`, `field210`, `CastRestriction`, `allowrest`, `InCombat`, `OutofCombat`, `field215`, `field216`, `field217`, `aemaxtargets`, `maxtargets`, `field220`, `field221`, `field222`, `field223`, `persistdeath`, `field225`, `field226`, `min_dist`, `min_dist_mod`, `max_dist`, `max_dist_mod`, `min_range`, `field232`, `field233`, `field234`, `field235`, `field236`) VALUES (25104, 'Wrath of Nature', 'PLAYER_1', '', '', '', 'You are gripped by nature\'s wrath.', ' has been gripped by nature\'s wrath.', 'The wrath of nature recedes.', 200, 0, 0, 0, 9000, 0, 0, 1, 30, 0, 0, -55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2503, 2119, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 1, 0, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 5, 0, 52, -1, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 44, 13, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 161, 109, 0, -100, 0, 0, 0, 0, 0, 0, 0, 1926, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -100, 100, -100, -99, 1, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0);
INSERT INTO `spells_new` (`id`, `name`, `player_1`, `teleport_zone`, `you_cast`, `other_casts`, `cast_on_you`, `cast_on_other`, `spell_fades`, `range`, `aoerange`, `pushback`, `pushup`, `cast_time`, `recovery_time`, `recast_time`, `buffdurationformula`, `buffduration`, `AEDuration`, `mana`, `effect_base_value1`, `effect_base_value2`, `effect_base_value3`, `effect_base_value4`, `effect_base_value5`, `effect_base_value6`, `effect_base_value7`, `effect_base_value8`, `effect_base_value9`, `effect_base_value10`, `effect_base_value11`, `effect_base_value12`, `effect_limit_value1`, `effect_limit_value2`, `effect_limit_value3`, `effect_limit_value4`, `effect_limit_value5`, `effect_limit_value6`, `effect_limit_value7`, `effect_limit_value8`, `effect_limit_value9`, `effect_limit_value10`, `effect_limit_value11`, `effect_limit_value12`, `max1`, `max2`, `max3`, `max4`, `max5`, `max6`, `max7`, `max8`, `max9`, `max10`, `max11`, `max12`, `icon`, `memicon`, `components1`, `components2`, `components3`, `components4`, `component_counts1`, `component_counts2`, `component_counts3`, `component_counts4`, `NoexpendReagent1`, `NoexpendReagent2`, `NoexpendReagent3`, `NoexpendReagent4`, `formula1`, `formula2`, `formula3`, `formula4`, `formula5`, `formula6`, `formula7`, `formula8`, `formula9`, `formula10`, `formula11`, `formula12`, `LightType`, `goodEffect`, `Activated`, `resisttype`, `effectid1`, `effectid2`, `effectid3`, `effectid4`, `effectid5`, `effectid6`, `effectid7`, `effectid8`, `effectid9`, `effectid10`, `effectid11`, `effectid12`, `targettype`, `basediff`, `skill`, `zonetype`, `EnvironmentType`, `TimeOfDay`, `classes1`, `classes2`, `classes3`, `classes4`, `classes5`, `classes6`, `classes7`, `classes8`, `classes9`, `classes10`, `classes11`, `classes12`, `classes13`, `classes14`, `classes15`, `classes16`, `CastingAnim`, `TargetAnim`, `TravelType`, `SpellAffectIndex`, `disallow_sit`, `deities0`, `deities1`, `deities2`, `deities3`, `deities4`, `deities5`, `deities6`, `deities7`, `deities8`, `deities9`, `deities10`, `deities11`, `deities12`, `deities13`, `deities14`, `deities15`, `deities16`, `field142`, `field143`, `new_icon`, `spellanim`, `uninterruptable`, `ResistDiff`, `dot_stacking_exempt`, `deleteable`, `RecourseLink`, `no_partial_resist`, `field152`, `field153`, `short_buff_box`, `descnum`, `typedescnum`, `effectdescnum`, `effectdescnum2`, `npc_no_los`, `field160`, `reflectable`, `bonushate`, `field163`, `field164`, `ldon_trap`, `EndurCost`, `EndurTimerIndex`, `IsDiscipline`, `field169`, `field170`, `field171`, `field172`, `HateAdded`, `EndurUpkeep`, `numhitstype`, `numhits`, `pvpresistbase`, `pvpresistcalc`, `pvpresistcap`, `spell_category`, `pvp_duration`, `pvp_duration_cap`, `pcnpc_only_flag`, `cast_not_standing`, `can_mgb`, `nodispell`, `npc_category`, `npc_usefulness`, `MinResist`, `MaxResist`, `viral_targets`, `viral_timer`, `nimbuseffect`, `ConeStartAngle`, `ConeStopAngle`, `sneaking`, `not_extendable`, `field198`, `field199`, `suspendable`, `viral_range`, `songcap`, `field203`, `field204`, `no_block`, `field206`, `spellgroup`, `rank`, `field209`, `field210`, `CastRestriction`, `allowrest`, `InCombat`, `OutofCombat`, `field215`, `field216`, `field217`, `aemaxtargets`, `maxtargets`, `field220`, `field221`, `field222`, `field223`, `persistdeath`, `field225`, `field226`, `min_dist`, `min_dist_mod`, `max_dist`, `max_dist_mod`, `min_range`, `field232`, `field233`, `field234`, `field235`, `field236`) VALUES (25103, 'Speed of the Shissar', 'PLAYER_1', '', '', '', 'Your body pulses with the spirit of the Shissar.', 's body pulses with the spirit of the Shissar.', 'Your body slows.', 100, 0, 0, 0, 6000, 0, 0, 3, 300, 0, 0, 166, 40, 0, 0, -3, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 166, 40, 0, 0, -3, 40, 0, 0, 0, 0, 0, 0, 2518, 2124, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 1, 0, 0, 11, 6, 10, 24, 24, 1, 254, 254, 254, 254, 254, 254, 5, 0, 5, -1, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 43, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 134, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1939, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, -99, 3, 300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0);
INSERT INTO `spells_new` (`id`, `name`, `player_1`, `teleport_zone`, `you_cast`, `other_casts`, `cast_on_you`, `cast_on_other`, `spell_fades`, `range`, `aoerange`, `pushback`, `pushup`, `cast_time`, `recovery_time`, `recast_time`, `buffdurationformula`, `buffduration`, `AEDuration`, `mana`, `effect_base_value1`, `effect_base_value2`, `effect_base_value3`, `effect_base_value4`, `effect_base_value5`, `effect_base_value6`, `effect_base_value7`, `effect_base_value8`, `effect_base_value9`, `effect_base_value10`, `effect_base_value11`, `effect_base_value12`, `effect_limit_value1`, `effect_limit_value2`, `effect_limit_value3`, `effect_limit_value4`, `effect_limit_value5`, `effect_limit_value6`, `effect_limit_value7`, `effect_limit_value8`, `effect_limit_value9`, `effect_limit_value10`, `effect_limit_value11`, `effect_limit_value12`, `max1`, `max2`, `max3`, `max4`, `max5`, `max6`, `max7`, `max8`, `max9`, `max10`, `max11`, `max12`, `icon`, `memicon`, `components1`, `components2`, `components3`, `components4`, `component_counts1`, `component_counts2`, `component_counts3`, `component_counts4`, `NoexpendReagent1`, `NoexpendReagent2`, `NoexpendReagent3`, `NoexpendReagent4`, `formula1`, `formula2`, `formula3`, `formula4`, `formula5`, `formula6`, `formula7`, `formula8`, `formula9`, `formula10`, `formula11`, `formula12`, `LightType`, `goodEffect`, `Activated`, `resisttype`, `effectid1`, `effectid2`, `effectid3`, `effectid4`, `effectid5`, `effectid6`, `effectid7`, `effectid8`, `effectid9`, `effectid10`, `effectid11`, `effectid12`, `targettype`, `basediff`, `skill`, `zonetype`, `EnvironmentType`, `TimeOfDay`, `classes1`, `classes2`, `classes3`, `classes4`, `classes5`, `classes6`, `classes7`, `classes8`, `classes9`, `classes10`, `classes11`, `classes12`, `classes13`, `classes14`, `classes15`, `classes16`, `CastingAnim`, `TargetAnim`, `TravelType`, `SpellAffectIndex`, `disallow_sit`, `deities0`, `deities1`, `deities2`, `deities3`, `deities4`, `deities5`, `deities6`, `deities7`, `deities8`, `deities9`, `deities10`, `deities11`, `deities12`, `deities13`, `deities14`, `deities15`, `deities16`, `field142`, `field143`, `new_icon`, `spellanim`, `uninterruptable`, `ResistDiff`, `dot_stacking_exempt`, `deleteable`, `RecourseLink`, `no_partial_resist`, `field152`, `field153`, `short_buff_box`, `descnum`, `typedescnum`, `effectdescnum`, `effectdescnum2`, `npc_no_los`, `field160`, `reflectable`, `bonushate`, `field163`, `field164`, `ldon_trap`, `EndurCost`, `EndurTimerIndex`, `IsDiscipline`, `field169`, `field170`, `field171`, `field172`, `HateAdded`, `EndurUpkeep`, `numhitstype`, `numhits`, `pvpresistbase`, `pvpresistcalc`, `pvpresistcap`, `spell_category`, `pvp_duration`, `pvp_duration_cap`, `pcnpc_only_flag`, `cast_not_standing`, `can_mgb`, `nodispell`, `npc_category`, `npc_usefulness`, `MinResist`, `MaxResist`, `viral_targets`, `viral_timer`, `nimbuseffect`, `ConeStartAngle`, `ConeStopAngle`, `sneaking`, `not_extendable`, `field198`, `field199`, `suspendable`, `viral_range`, `songcap`, `field203`, `field204`, `no_block`, `field206`, `spellgroup`, `rank`, `field209`, `field210`, `CastRestriction`, `allowrest`, `InCombat`, `OutofCombat`, `field215`, `field216`, `field217`, `aemaxtargets`, `maxtargets`, `field220`, `field221`, `field222`, `field223`, `persistdeath`, `field225`, `field226`, `min_dist`, `min_dist_mod`, `max_dist`, `max_dist_mod`, `min_range`, `field232`, `field233`, `field234`, `field235`, `field236`) VALUES (25102, 'Reviviscence', 'PLAYER_1', '', '', '', '', '', '', 200, 0, 0, 0, 10000, 2250, 15000, 0, 0, 0, 600, 96, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2510, 2051, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 1, 0, 0, 81, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 15, 0, 5, -1, 0, 0, 255, 56, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 43, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 101, 73, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1524, 42, 82, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -62, 135, -78, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO `spells_new` (`id`, `name`, `player_1`, `teleport_zone`, `you_cast`, `other_casts`, `cast_on_you`, `cast_on_other`, `spell_fades`, `range`, `aoerange`, `pushback`, `pushup`, `cast_time`, `recovery_time`, `recast_time`, `buffdurationformula`, `buffduration`, `AEDuration`, `mana`, `effect_base_value1`, `effect_base_value2`, `effect_base_value3`, `effect_base_value4`, `effect_base_value5`, `effect_base_value6`, `effect_base_value7`, `effect_base_value8`, `effect_base_value9`, `effect_base_value10`, `effect_base_value11`, `effect_base_value12`, `effect_limit_value1`, `effect_limit_value2`, `effect_limit_value3`, `effect_limit_value4`, `effect_limit_value5`, `effect_limit_value6`, `effect_limit_value7`, `effect_limit_value8`, `effect_limit_value9`, `effect_limit_value10`, `effect_limit_value11`, `effect_limit_value12`, `max1`, `max2`, `max3`, `max4`, `max5`, `max6`, `max7`, `max8`, `max9`, `max10`, `max11`, `max12`, `icon`, `memicon`, `components1`, `components2`, `components3`, `components4`, `component_counts1`, `component_counts2`, `component_counts3`, `component_counts4`, `NoexpendReagent1`, `NoexpendReagent2`, `NoexpendReagent3`, `NoexpendReagent4`, `formula1`, `formula2`, `formula3`, `formula4`, `formula5`, `formula6`, `formula7`, `formula8`, `formula9`, `formula10`, `formula11`, `formula12`, `LightType`, `goodEffect`, `Activated`, `resisttype`, `effectid1`, `effectid2`, `effectid3`, `effectid4`, `effectid5`, `effectid6`, `effectid7`, `effectid8`, `effectid9`, `effectid10`, `effectid11`, `effectid12`, `targettype`, `basediff`, `skill`, `zonetype`, `EnvironmentType`, `TimeOfDay`, `classes1`, `classes2`, `classes3`, `classes4`, `classes5`, `classes6`, `classes7`, `classes8`, `classes9`, `classes10`, `classes11`, `classes12`, `classes13`, `classes14`, `classes15`, `classes16`, `CastingAnim`, `TargetAnim`, `TravelType`, `SpellAffectIndex`, `disallow_sit`, `deities0`, `deities1`, `deities2`, `deities3`, `deities4`, `deities5`, `deities6`, `deities7`, `deities8`, `deities9`, `deities10`, `deities11`, `deities12`, `deities13`, `deities14`, `deities15`, `deities16`, `field142`, `field143`, `new_icon`, `spellanim`, `uninterruptable`, `ResistDiff`, `dot_stacking_exempt`, `deleteable`, `RecourseLink`, `no_partial_resist`, `field152`, `field153`, `short_buff_box`, `descnum`, `typedescnum`, `effectdescnum`, `effectdescnum2`, `npc_no_los`, `field160`, `reflectable`, `bonushate`, `field163`, `field164`, `ldon_trap`, `EndurCost`, `EndurTimerIndex`, `IsDiscipline`, `field169`, `field170`, `field171`, `field172`, `HateAdded`, `EndurUpkeep`, `numhitstype`, `numhits`, `pvpresistbase`, `pvpresistcalc`, `pvpresistcap`, `spell_category`, `pvp_duration`, `pvp_duration_cap`, `pcnpc_only_flag`, `cast_not_standing`, `can_mgb`, `nodispell`, `npc_category`, `npc_usefulness`, `MinResist`, `MaxResist`, `viral_targets`, `viral_timer`, `nimbuseffect`, `ConeStartAngle`, `ConeStopAngle`, `sneaking`, `not_extendable`, `field198`, `field199`, `suspendable`, `viral_range`, `songcap`, `field203`, `field204`, `no_block`, `field206`, `spellgroup`, `rank`, `field209`, `field210`, `CastRestriction`, `allowrest`, `InCombat`, `OutofCombat`, `field215`, `field216`, `field217`, `aemaxtargets`, `maxtargets`, `field220`, `field221`, `field222`, `field223`, `persistdeath`, `field225`, `field226`, `min_dist`, `min_dist_mod`, `max_dist`, `max_dist_mod`, `min_range`, `field232`, `field233`, `field234`, `field235`, `field236`) VALUES (25101, 'Barrier of Force', 'PLAYER_1', '', '', '', 'You are surrounded by a swirling maelstrom of magical force.', ' is surrounded by a swirling maelstrom of magical force.', 'The maelstrom dissipates.', 0, 0, 0, 0, 15000, 0, 0, 3, 1000, 0, 0, 1, 15, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 800, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2511, 2045, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 15, 205, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 1, 0, 0, 55, 148, 10, 10, 15, 254, 254, 254, 254, 254, 254, 254, 6, 0, 4, -1, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 42, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 78, 86, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1931, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, -99, 3, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);

---
## [Lianvee/Shiptest](https://github.com/Lianvee/Shiptest)@[5e29827ceb...](https://github.com/Lianvee/Shiptest/commit/5e29827cebbb7cd08d4bf5b210675526f324bf6d)
#### Monday 2022-02-14 05:56:18 by Zephyr

Spacemandmm fixes (#799)

* do it

Signed-off-by: Matthew <matthew@tfaluc.com>

* little more detail here

Signed-off-by: Matthew <matthew@tfaluc.com>

* put it in the wrong dmi

Signed-off-by: Matthew <matthew@tfaluc.com>

* Update code/game/objects/items/tools/chisel.dm

Copy paste gp BRRR

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

* resolve some issues that spacemandmm is complaining about because got fucking damn is it annoying when I am trying to code something and I get nonstop errors about stupid issues. also did you know that people though rand was exclusive on the high end? its actually not, both params are inclusive, which is stupid since this is different to almost every other god damn language

Signed-off-by: Matthew <matthew@tfaluc.com>

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

---
## [spookybear0/geode-sdk](https://github.com/spookybear0/geode-sdk)@[cb4a6b351a...](https://github.com/spookybear0/geode-sdk/commit/cb4a6b351aacf4de793319a6d7b51225cc148249)
#### Monday 2022-02-14 06:32:32 by HJfod

fix the stupid fucking piece of shit invalid hex fucking cock
motherfucker perkeleen paskasaatana pirunhelvetin shitass piece of cum
garbage

---
## [dforziat/UnityJam](https://github.com/dforziat/UnityJam)@[bd4c143faa...](https://github.com/dforziat/UnityJam/commit/bd4c143faa0261337132caf0bb84854d20667355)
#### Monday 2022-02-14 10:32:38 by dforziat

Small Tweaks to boss animation. Unity fucking sucks and I hate it

---
## [vemonet/rdflib-endpoint](https://github.com/vemonet/rdflib-endpoint)@[d5fbd23440...](https://github.com/vemonet/rdflib-endpoint/commit/d5fbd23440a4795fdda2d990f7b03543388f1401)
#### Monday 2022-02-14 10:52:07 by Vincent Emonet

add aiofiles to dependencies. All of sudden this shit is required to have starlette FileResponse working, what a fucking joke, those slow-thinkinf devs really cant figure out how to properly resolve dependencies

---
## [osamuaoki/qmk_firmware](https://github.com/osamuaoki/qmk_firmware)@[0d4e85f4a1...](https://github.com/osamuaoki/qmk_firmware/commit/0d4e85f4a13da9dad17c334917f59d17139d94b1)
#### Monday 2022-02-14 14:06:17 by Osamu Aoki

Format update and note

Note: Although these 2 lines should move to // Magic section, doinso may
cause trouble.  (My development time vague memory:  Back slash and back
space became swapped.  Since others had MAGIC_TOGGLE_CONTROL_CAPSLOCK
here, I assume this is the least invasive (but ugly patch.)

Signed-off-by: Osamu Aoki <osamu@debian.org>

---
## [trembyle/scummvm](https://github.com/trembyle/scummvm)@[dc4cfa05fe...](https://github.com/trembyle/scummvm/commit/dc4cfa05fe77224adf8c806309145e881d4ea8b9)
#### Monday 2022-02-14 14:41:22 by Torbjörn Andersson

SCUMM: Display Loom Overture Timing value as time, not a magic number

It makes it less obvious what the default was, but I think this is a lot
more user friendly. For some reason, it looks awful in RTL languages,
but I have no idea how to fix that.

---
## [kristian/neonbee](https://github.com/kristian/neonbee)@[e9be1819bc...](https://github.com/kristian/neonbee/commit/e9be1819bc87e939fe75d022e6ac0b6b1eb91171)
#### Monday 2022-02-14 14:52:57 by Kristian Kraljic

feat: improve `Launcher`, `Deployable`, `EntityModelManager` and more

This change is huge... I am sorry, but here is a video of me explaining why the change got so huge [1]. Sorry? Good news tough: All changes have been made interface and thus downwards compatible to the old NeonBee version, thus no adaptions to existing functionality should become necessary. Let me go into detail what changed and which quality of life / boy scout rule improvements have been made:

- Many NeonBee methods had been introduced in a pre-Vert.x 4-era. Meaning they did not take advantage of the futurization process Vert.x went through. This change rewrites many methods and simplifies them by switching the futurized methods, instead of methods using handlers.

- Improved the NeonBee bootstrap by making it more asynchronous, by changing the structure of method calls throughout the boot process and wrapping blocking code in `AsyncHelper.executeBlocking` calls.

- Simplified implementation of the `Launcher` class. Instead of manually defining and parsing all options in the launcher to get to a `NeonBeeOption` instance, instead switching to Vert.x's annotation-based `CLIConfigurator` implementation. Annotations are now defined directly in the `NeonBeeOptions` and injected into the `NeonBeeOptions` instance by the `CLIConfigurator`. This makes it much simpler and less error prone to define options and makes it also clear: everything that is in `NeonBeeOptions` can be defined through the command-line or environment. For the latter a `EnvironmentAwareCommandLine` was introduced, that also considers the environment variables if no options are set as arguments, deprecating all "helper methods" that have been there for only this reason.

- Added a new `development_conventions.md` document, that elaborates many "hidden rules" that we came up over the years, when it comes to coding conventions, such as: naming conventions for NeonBee variables, whether to use an instance to `NeonBee` or to `Vertx`, where to place `Context` variables in method signatures and how to properly correlate log messages. Then, in this change, a couple of old methods have been cleaned up to fit this new guiding document.

- The old naming choice for the "/verticles" subfolder does no longer make sense, because not only verticles are deployed by the `DeployerVerticle`, but full "modules". Thus, introduced a new `getModulesDirectory` method to `NeonBeeOptions` and deprecated the old `getVerticlesDirectory`. Two `DeployerVerticle` will now take care to deploy the old and the new directory if necessary (present).

- Introduced a new --module-jar-paths option to NeonBee options, that allows to define paths to module JARs, that will get deployed during the bootstrap phase of NeonBee into own self-first class-loaders. Previously the only option to deploy modules was through NeonBees `DeployerVerticle`, that was watching the `verticles` sub-directory for changes. The new option grants to also deploy modules that are not physically in that folder.

- Split up `EntityModelManager` into its (previously embedded) sub-classes by introducing a package private `EntityModelLoader` class. Futurized many of its methods and improved the concept for registering "external models": Previously modules did register / unregister models to the `EntityModelManager` by using their module identifier as a unique key. The `EntityModelManager` kept a private map of these IDs (`BUFFERED_MODULE_MODELS`) mapping to a set of compiled `EntityModel` objects. Now the concept was changed by introducing a new `EntityModelDefinition` object, that can be used to influence compilation of models of the `EntityModelManager`. Whenever a `EntityModelDefinition` is added / removed from the `EntityModelManager` it will attempt to compile a new "global" set of models. This allows for inter-dependent models and sets up the `EntityModelManager` for an upcoming change to be completely remodeled in order to support versioned models going forward (see the roadmap). It also makes managing the "external models" more easy, because no longer we need to hold a map of identifiers, but only a `Set<EntityModelDefinition>` to be maintained by the `EntityModelManager`. This makes it useful not only to modules, but any object that needs to deal with model generation can now supply a `EntityModelDefinition`.

- Removed `NeonBeeModule` in favor of a new `DeployableModule`. The `Deployable` interface was thought to become a generic object. Everything that can be deployed to NeonBee should inherit `Deployable`. `NeonBeeModule` violated this pattern and implemented much the same logic. Now the whole `io.neonbee.internal.deploy` package is consistent again, by introducing a `DeployableModels` (that can deploy `EntityModelDefinition` object), `DeployableModule` (that parses JAR files and splits them up into `DeployableModels` and `DeployableVerticles`) and a generic `Deployables` class, that handles deployments of multiple `Deployable` objects. This makes the whole deployment much cleaner, as for NeonBee everything is now a `Deployable` and the logic, whether it is a module, or a verticle, or a model that is being deployed, is now completely hidden away inside of the respective `Deployable` implementation. After deployment, everything results in the same `Deployment` instance, that can be undeployed again in the same fashion.

- Quality of life improvements to `AsyncHelper` by introducing runnables, cosumers and suppliers that can throw an exception. This allowed to replace existing calls like `AsyncHelper.executeBlocking(vertx, () -> { try { ... } catch (e) { return failedFuture(e); } })` with `AsyncHelper.executeBlocking(vertx, () -> ...)`.

- Simplified `ClassPathScanner` and introduced a new `CloseableClassPathScanner` that closes the underlying `URLClassLoader` to stop leaking resources.

- Introduced a new `ThreadHelper` class, that can be used to retrieve the calling or own class, as well as the class-loader of the current thread.

- Made `NeonBeeProfile` behave the same as for `moduleJarPaths` when getting parsed, meaning that you can define multiple profiles separated by comma.

- Renamed CollectionsHelper to CollectionHelper, because it was the only helper with a plural name.

- Improve many tests (esp. Deployable ones) mainly by mocking more and spying less.

- Made `setEnvironment` and `withEnvironment` work on Windows, to be able to remove `@DisableOnOS` annotation for tests changing environment variables.

[1] https://www.youtube.com/watch?v=AbSehcT19u0

---
## [SonicSoapyBoi/restoration-mod](https://github.com/SonicSoapyBoi/restoration-mod)@[49bb20bbcd...](https://github.com/SonicSoapyBoi/restoration-mod/commit/49bb20bbcdd563dc83518a19482985676a270cf2)
#### Monday 2022-02-14 15:42:52 by SonicSoapyBoi

HOLY SHIT WHY YOU HAVE SWEDISH COLORS?!

Fixed Zombie Zeal Cloakers having swedish textures
-Added Summers and his Co. back to Boiling Point
-Added Winters to First World Bank (i did some tests here and he works good here)

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[ed43d0fffc...](https://github.com/odoo-dev/odoo/commit/ed43d0fffc13a0c3fe83ca4b22ba060613f91812)
#### Monday 2022-02-14 15:45:59 by Julien Castiaux

[REF] core: HTTPocalypse (9) ORM initialization

This commit is the 9th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

When the "new" ORM API was implemented back in 2013, the HTTP was not
entirely ported to the new API. The authors of the new ORM API confessed
that they just "made it works" without much care for the HTTP API. A
decade later it is clear that the "lazy" approach prooved difficult
to reason about where and when the various ORM objects (cursor registry,
environment, context, user id) are set and modified.

Thanks to the HTTPocalypse, creation and modifications of those ORM
objects are now greedy, when one attempts to change the context, the
environment is greedely re-created using the modified context. The
previous approach was to wait until we re-use the environment to
re-create it.

The various ORM object properties setter have been removed and replaced
by `request.update_env` and `request.update_context`. The various ORM
object properties getter have not been modified and still act as alias
to the request environment.

The `check` function of `odoo.service.model` was kinda old, kinda
bloated with a kinda bad signature. The function have been renamed and
refactored. Because the function was a decorator, the visual clue
"this function is serialization-error safe" was at the function
definition. Actually it is the caller that needs the visual clue "I want
to protect this function call". The `check` function is no more a
decorator, it is a `asyncio.call_soon`-like function, passing arguments
is possible via `functools.partial`.

PR: odoo#78857
Task: 2571224

---
## [GNUWeeb/linux](https://github.com/GNUWeeb/linux)@[e206f51916...](https://github.com/GNUWeeb/linux/commit/e206f519162f8ffa0c325a1b5326b7301c88f046)
#### Monday 2022-02-14 16:06:53 by Jason A. Donenfeld

random: use linear max-period irq entropy accumulator

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As a permutation of only two
rounds, there are some easily searchable differential trails in it, and
as a means of preventing malicious irqs, it completely fails, since it
xors new data into the entire state every time. It can't really be
analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in this
context, in case a malicious irq compromises a per-cpu fast pool within
the 64 interrupts / 1 second window, and then inside of that same window
somehow can control its return address and cycle counter, even if that's
a bit far fetched. However with a very CPU-limited budget, actually
doing that remains an active research project (and perhaps there'll be
something useful for Linux to come out of it). And while the abundance
of caution would be nice, this isn't *currently* the security model, and
we don't yet have a fast enough solution to make it our security model.
Plus there's not exactly a pressing need to do that. (And for the
avoidance of doubt, the actual cluster of 64 accumulated irqs still gets
dumped into our cryptographically secure input pool.)

So, for now we are going to stick with the existing irq security model,
which assumes that each cluster of 64 irq cycle counter samples are
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector.  However, when considering this for our four-word
accumulation, versus NT's one-word, we run into potential problems
because the words don't contribute to each other, and some may well be
fixed, which means we'd need something to schedule on top. In addition,
this works for 2-monotone distributions, which the cycle counter is, but
not the registers and return addresses that we're also capturing.
(Whether capturing anything beyond the cycle counter in the interrupt
handler is even adding much is a question for a different time.)

However, a simple LFSR actually serves the same purpose and beyond, but
easily extends to larger state sizes and more complex distributions.
Importantly, it has the advantage that it only has the trivial invariant
subspace (0 -> 0), rather than quite a few invariant subspaces like
rotate-xor, which means we benefit from the analysis of
<https://eprint.iacr.org/2021/1002>, which gives proofs that these types
of linear structures with only trivial invariant subspaces make very
good entropy accumulators.

So this commit chooses a very fast and high diffusion max-period LFSR,
implemented in a Feistel-like fashion, which pipelines quite well. On an
i7-11850H, this takes 35 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://xn--4db.cc/V1nFTMYE/magma>,
or the equivalent Sage script, <https://xn--4db.cc/LpZhTYIh/sage>,
proves that this construction does indeed yield a max-period LFSR with a
primitive polynomial for our 4 pool words.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose an LFSR with pretty high diffusion, perhaps even higher than the
original fast_mix(), which we can quantify by computing that the minimum
weight of the linear code is 10, versus around 8 if we treat the
original fast_mix() as linear as well. In other words, we probably don't
regress at all from a perspective of diffusion, even if it's not really
a design goal anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now fixes that model much more rigorously. Plus the
performance is better, which perhaps matters in irq context.

As a final note, the previous fast_mix() was contributed by an anonymous
author, which, I've been told, has made some legally-minded people a bit
uncomfortable and is also against the kernel project's "real name"
policy.

Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [gdelanoy/shells](https://github.com/gdelanoy/shells)@[ffe5870bfd...](https://github.com/gdelanoy/shells/commit/ffe5870bfda6d3954fc4ddf39df9d75763430eda)
#### Monday 2022-02-14 17:27:15 by Guillaume Delanoy

Yeah, yo mama dresses you funny and you need a mouse to delete files.

---
## [bytewax/bytewax](https://github.com/bytewax/bytewax)@[8a6f0c0886...](https://github.com/bytewax/bytewax/commit/8a6f0c08867939b52421e10998546ba2850090b9)
#### Monday 2022-02-14 17:54:17 by David Selassie

Introducing: exhash

Missed out on [this crucial little note for Python's
`__hash__`](https://docs.python.org/3.9/reference/datamodel.html#object.__hash__):

> By default, the `__hash__()` values of str and bytes objects are
> "salted" with an unpredictable random value. Although they remain
> constant within an individual Python process, they are not
> predictable between repeated invocations of Python.

This means that having Timely route using Python's `hash` is fine
within one process, but breaks between multiple processes. Running the
wordcount demo with multiple procs, I occasionally get duplicate
counts because as it's doing `reduce_epoch` it thinks two instances of
`("the", 1)` are not the same key.

The "easier" way to fix this is to set the env var
[`PYTHONHASHSEED`](https://docs.python.org/3.9/using/cmdline.html#envvar-PYTHONHASHSEED). But
I don't think that's the best idea for a few reasons:

1. It's another gotcha for running multiple procs.

2. It's another source of coordination between cluster processes.

3. It feels weird to explain in one of our first tutorials that you
   need to use this obscure Python interpreter env var to make things
   work, and if you forget, there aren't errors, just wrong answers.

So my thought was to create an analagous `exhash` which explicitly is
meant to capture a consistent hash.

I did this using `functools.singledispatch` so you can write a version
for each type, and it'll call the right version. This will let users
add their own custom types later if they want. It returns a
[`hashlib`](https://docs.python.org/3/library/hashlib.html) algorithm
object (which doesn't actually have a formal type...). Which bytewax
will ask for the digest from and pass onto the Rust hashing machinery.

You can optionally pass in an algorithm object to support easy hashing
of nested types as you'll see in the `tuple` and `frozenset`
implementations.

Worries:

- This is also a little bit magic and another bit of conceptual
  overhead, although I'm hoping that if you stick to pretty common
  Python types you won't even need to touch this.

- Should we allow implementations for mutable objects like `list` and
  `set`? I haven't thought through what situations might cause a
  mutable list to "change" while sitting in a Rust `HashMap` and mean
  that all hell could break loose. I think this could happen if you
  use things like `stateful_map` and store and mutate values while
  also passing them on. I define some exception raising
  implementations for mutable types, but people could still override
  this if they want.

---
## [natto1784/singh3](https://github.com/natto1784/singh3)@[a7a15dc3b1...](https://github.com/natto1784/singh3/commit/a7a15dc3b140b5993b2581bd2c28d8d30df143f6)
#### Monday 2022-02-14 18:30:17 by natto1784

just made a huge fucking mess

added SelectMenu for embeds
removed interactions (for now)
stupid macros
need to organize this shit asap

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[aa41bd5ef2...](https://github.com/mrakgr/The-Spiral-Language/commit/aa41bd5ef2ccf9f8bcae158caff51f1e36948d7c)
#### Monday 2022-02-14 18:41:01 by Marko Grdinić

"10:45am. Am I getting enough sleep? I think I am, but it is close. Let me chill for a while and then I will figure out how Carve works.

Hmmm, I am not getting answers to my recent Houdini questions. I guess I'll abandon that thread.

11:15am. Let me finish ch 8 of Hinaki's doujin and then I will start. It is really difficult to find good Houdini learning resources. I do not have the money for the Hipflash courses. Well, let me just deal with the current scene, and then I'll consider going back to Blender.

11:20am. Ok, let me start. I need to study the Carve SOP examples.

11:40am. I am going over the examples and I really fucking hate how they use random colors for boxes. Black box over a black font. This is unreadable! I have to click it to see what it ways. Just what are these people thinking?

https://forums.odforce.net/topic/39009-carve-a-curve-by-specific-length-and-not-a-percentage/

Let me download the file from here. I am going to have to register for an account here, but it will be worth it if it allows me to figure out how to do this.

Hmmm, an alternative to this would be resamle with something like 0.1. Once you have that, you know that blasting 3 from the start will give you 0.3 of distance. But that is not a principled way of doing it anymore than using boolean curve.

https://forums.odforce.net/

Ohhh, this place is a Houdini focused forum. I should be asking here instead of on /3/.

I should revisit my old questions and post them here. If I could get answers, that would really increase the value of me using Houdini, maybe enough to stick with it.

11:40am. Ehhh, that is right. I do not know why I did not focus on this solution, but doing a foreach over the primitives is a viable solution.

https://forums.odforce.net/topic/50358-stop-sweep-from-interseting-itself/

This was the question I asked on /3/ yesterday. Let me check out the examples.

///

int pts[];
pts = primpoints(0, @primnum);
int n = len(pts);
int I[];
vector N[];
vector C[];
float U[];
//float A[];
for (int i = 0; i < n; i++)
{
    int im1 = max(i - 1, 0);
    int ip1 = min(i + 1, n-1);
    vector Nm1 = point(0, 'N', pts[im1]);
    vector Np1 = point(0, 'N', pts[ip1]);
    vector Qm1 = point(0, 'P', pts[im1]);
    vector Qp1 = point(0, 'P', pts[ip1]);
    vector Q = point(0, 'P', pts[i]);
    Nm1 = normalize(Q - Qm1);
    Np1 = normalize(Qp1 - Q);
    float u = point(0, 'curveu', pts[i]);
    float angle = acos(dot(Nm1, Np1));
    float t = chf('part') * $PI;
    if (angle > t)
    {
        push(I, i);
        push(N, normalize(lerp(Nm1, Np1, 0.5)));
        push(C, Q);
        push(U, u);
    }
    //push(A, angle);
}

int @I[];
@I = I;
vector @Nor[];
@Nor = N;
vector @C[];
@C = C;
float @U[];
@U = U;
i@count = len(U);
//float @A[];
//@A = A;

///

I found this piece of code for seeking out sharp corners in one of the examples. It would really be a pain in the ass to have to figure this out and do this by myself.

12:10pm. The use of clip I feel works particularly well. But the approach is incredibly complex.

12:30pm. No forget it. I should either do what I did or just stick to whole surfaces. The PolyDoctor node works for fixing the artefacts even if does not deal with self intersections properly.

Actually, it would not be too bad if I could PolyFill them, but that does not work.

12:35pm. No forget it. I can't get it to work. These automated tools are shit.

Moving on.

What should I do next?

I have everything except pool water and towels on the rack. I should Google Houdini towels.

The pool waster won't be too hard. I just have to extrude the bottom upwards after splitting it.

12:40pm. Ok, so I have a plan. I just have to figure out how to hang the towels onto the post and then I am done with the modeling part. Those towels are the only challenging part.

12:45pm. After I do this come the texturing phase. I should get to it.

12:50pm. https://www.youtube.com/c/Entagma/search?query=vellum

Enough, let me stop here for the morning. I did a little bit and figured out how to use Carve to trim curves by length.

What I need to do next is move on. Forget sharp turns. The blast solution is passable.

1pm. Forget the hook. Let me do the usual at this time of the day. Chores and breakfast. Then I'll get the towels and the pool out of the way. I should absolutely finish the modeling of the pool scene today, apart from Luna.

2:25pm. Let me start the afternoon session. I'll start things off by watching some tutorials. I need to figure out how clothing works in Houdini. I obviously can't scupt it using a brush, so I'll have to go the simulation route.

https://www.youtube.com/watch?v=9-R2L5VCd58
Houdini Tutorial: Cloth Sculpt

2:50pm. https://www.iamag.co/free-tutorial-creating-art-in-houdini/

While looking for cloth tuts this caught my attention. Let me take a look. It is good to look at how other people work every once in a while.

Right now, I just about know how to do clothing, but I am not sure if I know enough to try a towel.

...Oh, this is a pretty good scene. Yeah, I should watch this. Definitely.

2:55pm. Why is he making a box in such a complex manner? Well, whatever.

2:55pm. 6m in. So far so good. I can follow this. I hadn't know that you could tranform the front face. So I did learn something already.

I think this series has everything. So far, I only know about modeling, but after I watch this I'll have a reference for all the steps.

3:05pm. He used Shift + R to swap the inputs of a copy node!

I wish I knew that. It would have made dealing with it less annoying.

3:05pm. 12:40pm. > Just give it like a face normal.

Shit, it took me a while to figure that out yesterday. Unless you use face normals, you get weird shading artefacts after a boolean. He knows his stuff. Yeah, I think after this course I'll learn all that I need.

3:25pm. 3:14m into lesson1c. This way of using divide is not something I knew about. Yeah, it is impressive.

3:35pm. https://vimeo.com/rohandalvi?embedded=true&source=owner_name&owner=2587336

Vimeo has such shitty layout.

3:40pm. Forget it, let me move to 2a. So far I could follow all of it. System L has something to do with flowers, but I haven't looked into it. I guess this will be my intro.

3:55pm. 11:06m in. This is not like what I thought it would be, but it not hard to understand.

Ah whatever, let me just focus on this course for the rest of the day.

4pm. I've been browsing the iamag site, but I can't find these Houdini courses in the catalogue. Nevermind that for now. Let me get back into it.

https://www.youtube.com/playlist?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH
Houdini For The New Artist

I'll check this course out later.

4:25pm. 26m in. This does not look bad. I admit, I tuned out when he started messing with VOP nodes.

4:45pm. Let me take a break here.

5:10pm. Let me resume. Time for that terrain tutorial.

5:15pm. 4:25m in. What is that create in context? That is interesting.

Instead blasting, he should he used clip.

5:30pm. I need to figure out how the orient attribute works. I do not understand what he did with it.

5:35pm. This is a great tutorial. I'll be going back to it in the future for reference.

Looking the clothes line gives me an idea. I should be able to hook one of the points to the tip of the rack to prevent it from sliding off. Duh. I completely forgot about that.

5:55pm. That clothesline video told me everything I need to make the towel. It is perfect.

I really should have watched this video right from the start, but Houdini vids are all on Vimeo and it has been hard to find them.

Let me watch the chair vid.

1:45m in. What is the join node?

I'll have to look at the example for it later. Also I see in the docs that Stitch can be used to do cushions. I'll keep that in mind.

So far, the way he does procedural modeling is a dream. He does in 10m what would require me an entire day. I need to close that gap.

6:05pm. Holy shit, he'll use bevel to create gaps! That is high IQ thinking. I wish I could thought of that myself. I really have a while until I get there.

Watching him work is inspiring. I think I am going to persevere with Houdini. I want to go back to Blender, but I am liking the node based workflow too much. I know deep down that the more skilled I get, the smoother my work will be. If I could get my efficiency to go up, I could actually make the case for using Houdini to do art.

6:40pm. Had to leave for lunch. Let me resume.

6:45pm. I really need to remember `chramp` for the future. That is really useful. I am really in awe of Houdini's curve modeling capabilities.

7pm. It is really cool how you can control the fog density in Houdini.

https://www.iamag.co/free-tutorial-creating-art-in-houdini/

I'll leave the last two tutorial for tomorrow. I need focus for this.

https://www.sidefx.com/learn/collections/modeling-tools/

Hmmm, what is this point beveling thing here?

https://www.sidefx.com/schools/category/online-course/

https://learn.houdini.school/courses/procedural-geometry/info

115$. This shit is expensive. Forget this.

https://www.rohandalvi.net/home

Trying to learn Houdini could easily bankrupt a guy.

7:15pm. Ok, let me stop here properly. Now that I have the knowledge of how to create a towel, I'll finish the last two courses, do that and then move on to texturing. I'll have to watch tutorials on how to do that as well. I only touched upon that briefly in the Blender courses, and it will be time to seriously tackle it.

7:25pm. I need to buckle up and just do it. The hardest part is always the first scene. Once I break through the ceiling, I'll release an influx of capability. With another month of practice, I think I could master Houdini's fundamentals and establish my true workflow. I'll move from being ineffective like now to being effective and moving towards being even more so. I need to keep pushing forward. The time when I ma ready to being Heaven's key in terms of visuals is at most a few months away.

I still have to master audio as well. It is a pity that instead of starting work on Heaven's Key I have that bit of homework waiting for me as well. Like with visuals, it will take me a few months. So far I am 4.5 months into my art journey. If I am lucky, maybe I'll be able to get somewhere with audio in 2. I certainly can't imagine there being as much to learn there as in 3d art, so my workload should be comparatively lighter there.

7:35pm. Sigh, I just so adore some Houdini's workflow, even though I hate the program itself at times. I can't help it. I will have to become my mainstay. I want to become good at it and I am willing to pay the price of that.

7:40pm. Let me spend some time wandering the wastes. It is time for that rest."

---
## [gt2345/gtang-determined](https://github.com/gt2345/gtang-determined)@[08888717a6...](https://github.com/gt2345/gtang-determined/commit/08888717a6db21304115cd119ebb5d926d51c88e)
#### Monday 2022-02-14 18:46:26 by Bradley Laney

feat: unify task logs [DET-6062, DET-6063, DET-6064, DET-6065, DET-6066] (#3070)

This change adds persistent logs for all task types (well, all except poor old checkpoint GC). This means that logs are written to the logging back-end as configured in the master (PostgreSQL through master or Elastic) by Fluentbit and accessible through APIs in the master that translate reads to the back-end's language. To allow for this change, many other changes were required. A (probably) non-exhaustive list follows:
* Trial logs used to go to a `trial_logs` table or index. I tried to not tear the codebase asunder forever with trials and the others using different tables/queries/structs/etc everywhere. Existing tasks were marked has having `log_version == 0` and the old `trial_logs` table now serves logs those tasks (only trials). From now on, all tasks are written with `log_version == 1` and queries for their logs are routed to the `task_logs` table. The old trial logs table (now the `log_version == 0` table) is mothballed - it (mostly) shouldn't be touched again and the old logs should load from there fine forever while new features can be built on the new table. There were alternatives besides leaving trials and task logs separate forever that I shied away from; e.g., I considered a migration to update the trial logs table to schema of the task logs table, but since we access task logs by task_id, this would require rewriting the index on trial_id or adding one on task_id which is too expensive for a migration. This solution balances complexity, maintainability and migration cost.
* Because task logs went through the master, we were free to built features like readiness checks on top of them. Now that they don't, before logs leave the container a small helper script skims them, checks for the readiness logs and posts readiness to a new API. I considered alternatives here, too, like reading the logs back in on the master side, but that incurs a lot more overhead I felt this was more flexible anyway.
* The old events endpoint used to return logs, now it doesn't. This was because it (the eventManager that backed the endpoint) used to _store_ the logs, and now it doesn’t. In my opinion, the work to read the log stream and the old event stream and merge them is low value and annoying. Users should just prefer the new `/api/v1/tasks/:id/logs` endpoint for logs and rely on events to get the few task events that were relied on. Events will likely be supplanted by a task state watcher of some time so webui/cli can just watch for the readiness bit to flip.

---
## [freedesktop/NetworkManager](https://github.com/freedesktop/NetworkManager)@[2f2f526bd6...](https://github.com/freedesktop/NetworkManager/commit/2f2f526bd65c25fb3d841c4cb9515c149d2bfe20)
#### Monday 2022-02-14 19:18:48 by Thomas Haller

platform: support IPv6 mulitpath routes and fix cache inconsistency

Add support for IPv6 multipath routes, by treating them as single-hop
routes. Otherwise, we can easily end up with an inconsistent platform
cache.

Background:
-----------

Routes are hard. We have NMPlatform which is a cache of netlink objects.
That means, we have a hash table and we cache objects based on some
identity (nmp_object_id_equal()). So those objects must have some immutable,
indistinguishable properties that determine whether an object is the
same or a different one.

For routes and routing rules, this identifying property is basically a subset
of the attributes (but not all!). That makes it very hard, because tomorrow
kernel could add an attribute that becomes part of the identity, and NetworkManager
wouldn't recognize it, resulting in cache inconsistency by wrongly
thinking two different routes are one and the same. Anyway.

The other point is that we rely on netlink events to maintain the cache.
So when we receive a RTM_NEWROUTE we add the object to the cache, and
delete it upon RTM_DELROUTE. When you do `ip route replace`, kernel
might replace a (different!) route, but only send one RTM_NEWROUTE message.
We handle that by somehow finding the route that was replaced/deleted. It's
ugly. Did I say, that routes are hard?

Also, for IPv4 routes, multipath attributes are just a part of the
routes identity. That is, you add two different routes that only differ
by their multipath list, and then kernel does as you would expect.
NetworkManager does not support IPv4 multihop routes and just ignores
them.
Also, a multipath route can have next hops on different interfaces,
which goes against our current assumption, that an NMPlatformIP4Route
has an interface (or no interface, in case of blackhole routes). That
makes it hard to meaningfully support IPv4 routes. But we probably don't
have to, because we can just pretend that such routes don't exist and
our cache stays consistent (at least, until somebody calls `ip route
replace` *sigh*).

Not so for IPv6. When you add (`ip route append`) an IPv6 route that is
identical to an existing route -- except their multipath attribute -- then it
behaves as if the existing route was modified and the result is the
merged route with more next-hops. Note that in this case kernel will
only send a RTM_NEWROUTE message with the full multipath list. If we
would treat the multipath list as part of the route's identity, this
would be as if kernel deleted one routes and created a different one (the
merged one), but only sending one notification. That's a bit similar to
what happens during `ip route replace`, but it would be nightmare to
find out which route was thereby replaced.
Likewise, when you delete a route, then kernel will "subtract" the
next-hop and sent a RTM_DELROUTE notification only about the next-hop that
was deleted. To handle that, you would have to find the full multihop
route, and replace it with the remainder after the subtraction.

NetworkManager so far ignored IPv6 routes with more than one next-hop, this
means you can start with one single-hop route (that NetworkManger sees
and has in the platform cache). Then you create a similar route (only
differing by the next-hop). Kernel will merge the routes, but not notify
NetworkManager that the single-hop route is not longer a single-hop
route. This can easily cause a cache inconsistency and subtle bugs. For
IPv6 we MUST handle multihop routes.

Kernels behavior makes little sense, if you expect that routes have an
immutable identity and want to get notifications about addition/removal.
We can however make sense by it by pretending that all IPv6 routes are
single-hop! With only the twist that a single RTM_NEWROUTE notification
might notify about multiple routes at the same time. This is what the
patch does.

The Patch
---------

Now one RTM_NEWROUTE message can contain multiple IPv6 routes
(NMPObject). That would mean that nmp_object_new_from_nl() needs to
return a list of objects. But it's not implemented that way. Instead,
we still call nmp_object_new_from_nl(), and the parsing code can
indicate that there is something more, indicating the caller to call
nmp_object_new_from_nl() again in a loop to fetch more objects.

In practice, I think all RTM_DELROUTE messages for IPv6 routes are
single-hop. Still, we implement it to handle also multi-hop messages the
same way.

Note that we just parse the netlink message again from scratch. The alternative
would be to parse the first object once, and then clone the object and
only update the next-hop. That would be more efficient, but probably
harder to understand/implement.

https://bugzilla.redhat.com/show_bug.cgi?id=1837254#c20

---
## [wraith-54321/fulpstation](https://github.com/wraith-54321/fulpstation)@[b59f03e592...](https://github.com/wraith-54321/fulpstation/commit/b59f03e592ce72f069760eba0f9eb30eeacd16c1)
#### Monday 2022-02-14 20:34:57 by John Willard

Deputy update (#428)

* deputy berets cant be knocked off, deputies get tablets, service deputy beret buff.

* fuck you

---
## [Perkedel/IvanC-MIDI-Play-Plugin](https://github.com/Perkedel/IvanC-MIDI-Play-Plugin)@[b869fecf13...](https://github.com/Perkedel/IvanC-MIDI-Play-Plugin/commit/b869fecf13925e9f7cb6a29ac578d9903cb03f64)
#### Monday 2022-02-14 20:40:51 by Joel Robert Justiawan

sobeg

pls publish this thing to JUCE forum, linking back to IvanC's original source code forum link up there!

attempt playhead failed miserably. I need help. that's why I want to talk to forum. With good standing of proof that this means something, I hope, people see and join in to help us.

reimprove UI arrangement. damn, I still don't understand how UI resize arrangement works at all! It's way other than CSS. Oh yeah, there's a component. Now just the matter of how to put component into main PluginEditor here.

Full the README.md so other can understand + more info about JUCE, as beginner friendly as possible.

Attempt to fix drum for some MIDI files not drumming failed. OH IDEA, how about push entire track by couple a bit. and then this vacant space are reserved to patch out!

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[1b56fe1b06...](https://github.com/i3roly/glibc_ddwrt/commit/1b56fe1b06d5d076a32656f4906c63e124c89e15)
#### Monday 2022-02-14 20:54:59 by gagan sidhu

48359/4.14.266, small update. "autotune ensure you're the winner, not the loser, in life" - randy marsh

- update dnsmasq
- wireguard/eop updates
- mc update for big builds/lootbag
- kernel update
- apply the hw_nat fix by @hanwckf
    -personally i didn't notice any issues with having
     wlan_optimize on, but maybe there's something to it.
     dunno. maybe i'll flip it back on in another build.

hate updating a build so quickly but what can you do?
    -welllll i know what you can do, so i shall again
     spare you the expletive(s).

TESTED AND WORKING

* Shelly's room, evening. Randy knocks on her door *

Randy
        Shelly, that's enough time on your phone.

Shelly
        Leave me alone, Dad! Stop nagging me all the time!

Randy
        You know we're all cutting down on phone time.

Shelly
        [sits up]

        Don't limit me! You don't even understand me!

Randy
        [sees a poster of himself as <'famous' "musician">,
        his secret identity]

        Yeah. I don't understand you at all. A lot you know.

        [walks away saddened]

        *   The Marsh garage    *

*  Randy is adding more stacks of cash to those already  *
*    hidden behind the poster. A door opens and Randy    *
*            quickly seals it up.                        *

* He gets to his workbench just as Stan closes the door. *

Stan
        Uh hey Dad. I need to talk to you.

Randy
        Oh really? A-About... about what?

Stan
        Dad, is it possible for someone to be one way on
        the outside but totally different on the inside?

        [Randy sighs deeply and stands up to walk]

        I mean, can someone identify as one sex but be
        something else but still have it be nothing about sex?

Randy
        Yes. Yes, Stan. I am <'famous' "musician">.

Stan
        ...What?

Randy
        It started off so simple. There's a guy at work. Hanson.
        He would use the bathroom and just blow the thing up, you know?
        Not only that, but he was in there all the time! I finally got
        fed up and pretended to be a woman.
        I called myself <'famous' "musician">. Have you ever been in a
        woman's bathroom, Stan? It's all clean and there's enough stalls
        for everyone. It was so freeing. I started singing while I was
        in there, and then I- started writing things down.

Stan
        Well you said you knew a guy at work who was
        <'famous' "musician">'s uncle.

Randy
        Yah, that's my cover.

Stan
        The chick that wrote the theme song to the new
        <shitty recession stimulus-funded book and movie series>, is you?

Randy
        Yeah.

        [turns around and faces Stan]

        The record company messed it all up. It was supposed to go:

            "<shitty recession stimulus-funded book and movie series>,
            yah yah yah, yah yah yah! <shitty recession stimulus-funded
            book and movie series>."

        But they just- do what they want with my songs.

Stan
        Wha-wait, <'famous' "musician"> sounds like a girl.

Randy
        Autotune. Wanna see how I do it?

        [moments later, a music program pops up.
        Twelve tracks are shown at lower left]

        I come up with all my best stuff in the bathroom at work.

        I use this program to import the recordings I make on my phone.

        [plays the highlighted track]

            "Yeah yeah, feeling good on a Wednesday. Sparklinnnnn'
            thoughts. Givin' me the hope to go ohhhn"

            [farts and poop noises]

            "Oh! Whoa. What I need now is a little bit of shelter."

Stan
        Dad, <'famous' "musician">'s music is actually really good.

Randy
        Thanks.

        But it gets even better when I add the drum loops.

        [replays the same track with drum loops added]

        Then with the computer I can actually quantize everything.

        [brings up the quantizer and chooses his settings]

        Backup instruments.

        [scale, beats, bass, tambourine, guitars, strings]

        And then finally I use the Autotune.

        ["Auto-Tuner v10." He chooses his settings there, and
        the song is transformed. The same track is now enhanced
        with <no name shitty "musician">'s voice and no trace of Randy]

            "Sparklin' thoughts, feelin' good on a Wednesday.
            Givine me the hope, givin' givin' me the hope to go ohhhn.
            What I need is a little bit of shelter."

        [this is all too much for Stan to take in, and he passes out.]

        [Randy notices]

        Stan?

---
## [lillanes/dwm](https://github.com/lillanes/dwm)@[67d76bdc68...](https://github.com/lillanes/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2022-02-14 21:10:48 by Chris Down

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
## [Capsandi/tgstation](https://github.com/Capsandi/tgstation)@[b48cda6afa...](https://github.com/Capsandi/tgstation/commit/b48cda6afa047be95390dc1360e8d899ec6394b0)
#### Monday 2022-02-14 21:15:52 by LemonInTheDark

Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

* Please stop typecasting target, noooooooooooooooooo

* Fixes harddels in pinned module code

The logic for pinned modules was intentionally hanging references to the
mob that pinned the action button. I have depression.

The pinned_to list also was never fully cleared, but that would have
just exasperated the issue. I've converted its use of mobs to refs, and
its use of the module var into something better managed

(Friendly reminder that actions will persist in your nightmares forever
unless they are manually qdel'd, this code wasn't doing that.

Also cleaned up how the pinned_to list is managed, hopefully it's a bit
more action centered now

---
## [subiabre/reck](https://github.com/subiabre/reck)@[f6d30ee01b...](https://github.com/subiabre/reck/commit/f6d30ee01bf8b48f86040dc06bd0f49d32ffce90)
#### Monday 2022-02-14 23:40:00 by Daniel

FUCK DOCKER WHY THE FUCK DOES THIS NOT WORK IN AN ARM64 CHIP WTF IS "CONTAINERIZATION" GO FUCK YOURSELF IM GOING CRAZY

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[8f32cbe38d...](https://github.com/timothymtorres/tgstation/commit/8f32cbe38d956e06c919be36386da76befb0555b)
#### Monday 2022-02-14 23:55:45 by LemonInTheDark

Reworks janitor cyborg cleaning, focus on the slipping (#64131)

Alt of #64105 and #64126 (I'm sorry Novva, I should have said something earlier)
I main janitor. As a janitor main, my greatest joy in life is slipping people who ignore my signs

I've seen some people complain about janitor borgs, so I decided to look into em

Unfortunately, not only is the janitor borg just a straight upgrade to janitors, it has absolutely no reason to use most of its kit
We give it standard cleaning supplies, and hell even bespoke tools to deal with leaving slippery tiles everywhere, but we also just let them clean anything they can walk over

This seems a bit too much to me, even for borgs. Also it's like, really boring

So what if we made their movement based cleaning cost something? How about we make it suck water from their bucket. Use the same pattern as mop code, make it twice as expensive though. Give it a slowdown, some sound cues, and an action button to trigger it all

---

