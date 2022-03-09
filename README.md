## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-08](docs/good-messages/2022/2022-03-08.md)


1,788,788 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,788,788 were push events containing 2,854,376 commit messages that amount to 213,802,775 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [nangtani/blender](https://github.com/nangtani/blender)@[2e146df515...](https://github.com/nangtani/blender/commit/2e146df51589281ac2cacef117f5f94fcbb4c7b7)
#### Tuesday 2022-03-08 00:00:28 by Joseph Eagar

temp-vertex-paint: Vertex paint branch

I have successully ported vertex paint's
draw brush to C++ thanks to the magic
of templates.  It's amazing how easy
this is.

---
## [radar651/S.P.L.U.R.T-Station-13](https://github.com/radar651/S.P.L.U.R.T-Station-13)@[2f9272dc4b...](https://github.com/radar651/S.P.L.U.R.T-Station-13/commit/2f9272dc4b26209129e47a226276deb360818203)
#### Tuesday 2022-03-08 00:08:49 by Ludox

FUCK YOU

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[42f74fd65e...](https://github.com/san7890/bruhstation/commit/42f74fd65e32b04e247352c853e133dfe3b30ab5)
#### Tuesday 2022-03-08 00:18:17 by san7890

Mapper's Delight: Directional Poster Spawners [MDB IGNORE]

A lot of my PRs have been focused on having a fire lit under the seat of my pants. However, this PR is based off one conversation I had with someone.

"Haha, mapper. All you do is var_edits."

It was a bit more verbose than that, but it really did get me thinking about how fucking massive our files our thanks to these var_edits. This PR adds directional helpers to both A) Help mappers map the correct things with as little var edits as possible and B) Lessen the amount of space each fucking map file is thanks to however many extra bytes are taken up with pixel_x = 32. we have a lot of posters.

Bluntly put, this PR adds directional helpers to all generic /random poster spawners. i would add them to every single poster in the game, but that's a lot of work for unique posters, and someone can probably come up with a better idea. Good luck with that, this is just a good first step.

---
## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[d1a7cf0dca...](https://github.com/kleinesfilmroellchen/serenity/commit/d1a7cf0dca5a540a63ecf661e8bf45de1b92fddc)
#### Tuesday 2022-03-08 00:18:35 by kleines Filmröllchen

LibAudio+Userland: Use new audio queue in client-server communication

Previously, we were sending Buffers to the server whenever we had new
audio data for it. This meant that for every audio enqueue action, we
needed to create a new shared memory anonymous buffer, send that
buffer's file descriptor over IPC (+recfd on the other side) and then
map the buffer into the audio server's memory to be able to play it.
This was fine for sending large chunks of audio data, like when playing
existing audio files. However, in the future we want to move to
real-time audio in some applications like Piano. This means that the
size of buffers that are sent need to be very small, as just the size of
a buffer itself is part of the audio latency. If we were to try
real-time audio with the existing system, we would run into problems
really quickly. Dealing with a continuous stream of new anonymous files
like the current audio system is rather expensive, as we need Kernel
help in multiple places. Additionally, every enqueue incurs an IPC call,
which are not optimized for >1000 calls/second (which would be needed
for real-time audio with buffer sizes of ~40 samples). So a fundamental
change in how we handle audio sending in userspace is necessary.

This commit moves the audio sending system onto a shared single producer
circular queue (SSPCQ) (introduced with one of the previous commits).
This queue is intended to live in shared memory and be accessed by
multiple processes at the same time. It was specifically written to
support the audio sending case, so e.g. it only supports a single
producer (the audio client). Now, audio sending follows these general
steps:
- The audio client connects to the audio server.
- The audio client creates a SSPCQ in shared memory.
- The audio client sends the SSPCQ's file descriptor to the audio server
  with the set_buffer() IPC call.
- The audio server receives the SSPCQ and maps it.
- The audio client signals start of playback with start_playback().
- At the same time:
  - The audio client writes its audio data into the shared-memory queue.
  - The audio server reads audio data from the shared-memory queue(s).
  Both sides have additional before-queue/after-queue buffers, depending
  on the exact application.
- Pausing playback is just an IPC call, nothing happens to the buffer
  except that the server stops reading from it until playback is
  resumed.
- Muting has nothing to do with whether audio data is read or not.
- When the connection closes, the queues are unmapped on both sides.

This should already improve audio playback performance in a bunch of
places.

Implementation & commit notes:
- Audio loaders don't create LegacyBuffers anymore. LegacyBuffer is kept
  for WavLoader, see previous commit message.
- Most intra-process audio data passing is done with FixedArray<Sample>
  or Vector<Sample>.
- Improvements to most audio-enqueuing applications. (If necessary I can
  try to extract some of the aplay improvements.)
- New APIs on LibAudio/ClientConnection which allows non-realtime
  applications to enqueue audio in big chunks like before.
- Removal of status APIs from the audio server connection for
  information that can be directly obtained from the shared queue.
- Split the pause playback API into two APIs with more intuitive names.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [elliottbernstein/crawl](https://github.com/elliottbernstein/crawl)@[e8bc28a0cf...](https://github.com/elliottbernstein/crawl/commit/e8bc28a0cf5eb223156f893c8f47b1284931e78a)
#### Tuesday 2022-03-08 01:04:50 by DreamDust

vaults: float vaults by DreamDust

dreamdust_dug_too_deep

The dwarves dug a little too deep and unearthed... a Balrug! Even a
mighty dwarf hero (with a potentially good weapon to loot!) fell in
battle to the demon. RIP. Maybe this is why we don't see deep dwarves
much anymore. Hmmmm...

The idea behind this vault is to place a single Balrug early enough that
it's a serious (but not unmanageable) threat. I added a downhatch close
by if players need to escape in a hurry. There are also warning signs in
advance (all the dwarf corpses and the suspicious volcanic floor tiles
outside the Balrug room).

[ Committer's note: Added a runed door for the balrug, adjusted
  transparency, traded volcanic floor for blood. ]

dreamdust_wu_jian_sword_trials

A Wu Jian-themed vault. Challenge three increasingly powerful
sword-wielders for their increasingly good swords.

[ Committer's note: Adjusted depth range, added monsters to the earlier
  trial, trimmed arenas, added transperency. ]

dreamdust_merry_men

Inspired by Robin Hood and his band of merry men. Features a forest with
a bunch of archers and a good bow and aides to banditry to loot in the center.

[ Committer's note: Adjusted layout to prevent teleport closets, monster
  counts, loot. ]

dreamdust_tengu_aerie

A large nest of tengus. They keep their shiny loot in the center...
along with their fledglings (wait, are we the baddies??).

[ Committer's note: moved the crystal walls to the middle, put the
  rock wall on the outside (so the reavers can bolt bounce their
  omnibolts), and thinned the monster density. ]

dreamdust_hydra_shepherd

A shepherd is raising a flock (?) of hydras down in the Depths! Some
players might regret abandoning their flaming weapons after finishing
Lair/Swamp, haha.

[ Committer's note: upgraded the cyclops to a stone giant, added a small
  chance for a really high head count. ]

dreamdust_elfheim

The home of Duvessa and Dowan.
The more-practical Duvessa has training dummies in her room, while the
vain Dowan has a large mirror to admire himself with.

[ Committer's note: cut down on custom tiling/colouring a bit. ]

---
## [copperwater/xNetHack](https://github.com/copperwater/xNetHack)@[879897d885...](https://github.com/copperwater/xNetHack/commit/879897d885462664cabcd521ca62fc3fd5a4fcf5)
#### Tuesday 2022-03-08 01:06:51 by copperwater

Add black mold

A new monster? In xNetHack???

This has been planned for quite a while, and only now gotten around to.
The general idea is adding a member to the F class that actually might
pose a threat to the player rather than being firmly in assists-only
status. This is particularly relevant since F monsters grow on moldy
corpses.

The general details of the monster come from SporkHack's gray fungus,
via EvilHack which imported it fairly directly from there. Differences
include:
- It's named "black mold" rather than "gray fungus" because black mold
  is a real-life thing that can grow in living spaces, making the
  inhabitants sick.
- It's modeled after the other molds. It has similar stats, no active
  attacks, etc.
- It doesn't confer poison resistance when eaten. Instead it makes the
  consumer deathly ill when eaten. (Though this is curable by vomiting
  and is therefore labeled as FoodPois -- it's a little weird that the
  sickness from the passive attack is not curable by vomiting and the
  sickness from eating it is, but that's due to the different ways it's
  making you sick, one by having it in your digestive tract and one by
  inhaling spores.)
- It appears quite late for a F monster, with a difficulty of 8.
- The Brewing Patch applies to it, allowing black mold to be fermented
  in fruit juice to later turn to sickness.

Unlike in EvilHack, monster illness is not implemented and so the black
mold's passive attack does nothing when it hits a monster.

---
## [ivanmixo/tgstation](https://github.com/ivanmixo/tgstation)@[ac21ef9078...](https://github.com/ivanmixo/tgstation/commit/ac21ef9078d88f51a4e198e394ed56e3cc731b45)
#### Tuesday 2022-03-08 01:16:28 by Pickle-Coding

No, we don't want radiation getting released in large pipenets fuck you fuckr uyu! (#65212)

* Make it harder to release radiation in large pipenets. Squares the volume / 2,500 thingy, and adds the requirements to the proto-nitrate bz response and proto-nitrate tritium response gas reactions to release radiation. This will make it significantly harder to release radiation in large pipenets, because releasing radiation in large pipenets makes it harder for people to identify the cause on why they are getting irradiated, which is bad and goes against the modern radiation goals.

Squaring is not enough for deranged people that know we don't want radiation released in large pipenets. Cubes the requirement instead. If someone could get enough gases reacting at once after this, then there is a bigger problem with atmos.

Who had fun seeing everything green, then getting irradiated and not even knowing why? I don't know, because I don't know who put the gases in waste and why we must suffer.

---
## [eun0115/4.14_kernel_moon](https://github.com/eun0115/4.14_kernel_moon)@[28596ef125...](https://github.com/eun0115/4.14_kernel_moon/commit/28596ef125263b57bf46a254f3a91d8d89d20373)
#### Tuesday 2022-03-08 02:27:32 by Wang Han

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
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Tuesday 2022-03-08 03:24:15 by Albert Liu

Add PresetService (User Presets Step 3) (#1164)

Final feature demo:

![Kapture 2022-01-13 at 23 36 00](https://user-images.githubusercontent.com/12578068/149469927-b62bfa43-4701-4498-a489-565aea36da2c.gif)

---------------------------

This PR is extracted from #1041 as step 2 of the User Preset feature.

rebase of picked commits pertaining to PresetServiceService onto Albert-UserDictionaryService

PresetService provides the ability to save and "apply" collections of settings (represented by objects) that a user might find convenient to save and apply as a group. These groups are called Presets.

PresetService uses DictionaryService to store presets (it creates kind of a *view* in the database sense, of the user dictionary, that only includes Presets)

Changes from last review (for Yicong)
 - Code comments
 - fixed subscription memory leak by using takeUntil(observable), where said observable completes on NgOndestroy
 - DictionaryService now attempts to init whenever client logs in (sorry, you'll have to re-review my changes to DictionaryService)
 - PresetService now has public ready promise/value member 
   - This indicates that its init isn't complete until DictionaryService's init is complete (which is async, and cant be awaited in the constructor)
 - DeletePreset now built into PresetService (don't know why I ever didn't have that)
 - Revert Changes to Styles.scss to fix Karma test runner interface (I originally changed them as a workaround for an ng-zorro component that's no longer used)

 Note: for this step, I had less time and more complex code to test. I'm not sure I caught all the bugs, but it passes unit tests.
The quality of the code in this pr is lesser, in my opinion, so You'll have to be a little more careful on my behalf.



Co-authored-by: Zuozhi Wang <zuozhiw@gmail.com>
Co-authored-by: Yicong Huang <17627829+Yicong-Huang@users.noreply.github.com>

---
## [ozzono/scripts](https://github.com/ozzono/scripts)@[aba296ffdf...](https://github.com/ozzono/scripts/commit/aba296ffdf903c37f9b82315252b4b5abf1871e7)
#### Tuesday 2022-03-08 03:58:45 by Hugo Virgilio

Fortune Commit: I used to be such a sweet sweet thing, 'til they got a hold of me,
I opened doors for little old ladies, I helped the blind to see,
I got no friends 'cause they read the papers, they can't be seen,
With me, and I'm feelin' real shot down,
And I'm, uh, feelin' mean,
	No more, Mr. Nice Guy,
	No more, Mr. Clean,
	No more, Mr. Nice Guy,
They say "He's sick, he's obscene".

My dog bit me on the leg today, my cat clawed my eyes,
Ma's been thrown out of the social circle, and Dad has to hide,
I went to church, incognito, when everybody rose,
The reverend Smithy, he recognized me,
And punched me in the nose, he said,
(chorus)
He said "You're sick, you're obscene".
		-- Alice Cooper, "No More Mr. Nice Guy"

---
## [timhjersted/tsorcDownload](https://github.com/timhjersted/tsorcDownload)@[4a5f2a3f13...](https://github.com/timhjersted/tsorcDownload/commit/4a5f2a3f130475a4a6850cc6d3d78daa5af491e9)
#### Tuesday 2022-03-08 05:34:22 by timhjersted

0.3.21

MAP 0.3.21
------------------
Added a few new pre-EoC secrets and progression-skips (if you find them, please be cryptic and use ||redacted spoiler text here|| in Discord to discuss them
Fixed 2 progression-blocking puzzle walls in the SHM "dungeon with blue flames" (you will need to turn off adventure mode to mine through the walls if playing on a previous map)
Glass Prison got some more attention and detail
The Hunter, The Rage and the Litch King now spawn from a golden ring, instead of a craftable summon item (needs latest mod update to work)
Larger portion of the jungle is also crimson and is cast in greater darkness
Meteor Temple is slightly more spacious + a particular trap room is less lethal
Crimson zone near jungle underground is larger
Path to the Catacombs adjusted (2 extra "shortcut" gates were also removed since they teased possible progression options that are no longer used)
Path to jungle loot adjusted slightly to account for new progression options
Tweaked The Sorrow's water pumps to avoid overflowing the boss room with water
Fixed two signs that had their text removed in a previous update
Fixed more typos
Fixed a broken bed in The Machine Temple
Removed unintended Soul of Fright exploit
More small tweaks

MUSIC 0.3.21
------------------
Added boss music for Ancient Demon
Tried to fix Sandstorm music not playing sometimes

---
## [Beorseder/Evolve](https://github.com/Beorseder/Evolve)@[2cd5860161...](https://github.com/Beorseder/Evolve/commit/2cd5860161e23a0a160cd9c4be4876fbf98dbd6b)
#### Tuesday 2022-03-08 06:26:15 by Beorseder

Calculator Updates, Minor Bug Fixes, and Info

Perks:
Added Doomed achievement to the perks lists because there's no way to know that it unlocks Hellscape/Eden planets otherwise.
Added Governor CRISPR tree to perks list.
Fixed Evolve Journeyman not showing the full list of values in the wiki perks page if the perk was not yet obtained.

Calculators:
Updated Plasmid/Anti-Plasmid gain calculators with the new caps on gains, the High Population trait, being Synthetic genus for MADs, and being in Truepath, and AI Apocalypse reset.
Updated Phage gain calculator with Truepath and AI Apocalypse reset.
Updated Dark Energy bonus calculator with Lemon Cleaner perk.
Added AI Core gain and bonus calculators.
Added gain calculators to AI Apocalypse reset entry.
Updated Job Stress calculator to be fixed and accommodate for trait rankings and, the Emotionless trait and to fix Titan Colonist string.

Wiki Info:
Added information about Sludge's modification costing 10x more and their inability to remove Ooze to the Failed Experiment entry. Also fixed the data link to MAD reset.
Similarly added to CRISPR Mutation entry that Sludge also have 10x costs.
Added to Raid, Siege, and Terrorist Attack events how they don't happen in Truepath.
Added Pillage event(s) entry to Major Events page.
Updated Llama Minor Event with trait restrictions.
Updated Ascension reset entry with information on the geology buff and Ascended planets.
Added wiki effect to Alien Biotech tech.

Textual:
Fixed Entertainer tooltip showing twice the effect of Musical.
Fixed Gauss Rifles showing the effect for Disruptor Rifles.
Fixed some wiki fuel cost displays.
Fixed Water Freighter tooltip showing half the Helium-3 cost. Fixes #713
Fixed some typos.
Changed instances of "space cost creep" to "non-homeworld cost creep" to indicate that they apply to Hell Dimension as well.
Updated Pig-Latin.

Misc:
Exporting the save now updates accelerated time bank to account for if someone is paused and exports, updating their save's current time and thus losing all that accelerated time.
Fixed CRISPR and Blood Infusions being affected by adjustCosts when checking their affordability, which caused some issues with traits shifting their costs around making the coloring inaccurate sometimes near the cost.
Fixed Ritual Casting not showing up in Industry in Cataclysm.
Fixed bug where, if not Preloading Tab Content, shifting to another tab when in the custom lab and then shifting back to Civilization tab would not show the custom lab anymore. Fixes #671
Detritivores no longer see the Farming ritual as it doesn't do anything for them.
Fixed bug with building the Forward Base not reloading space to show the Troop Lander and Crashed Ship structures.

---
## [TeodorD420/tgstation](https://github.com/TeodorD420/tgstation)@[3bd5a2d8df...](https://github.com/TeodorD420/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Tuesday 2022-03-08 06:51:06 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [stamp-protocol/core](https://github.com/stamp-protocol/core)@[e755b6a7c1...](https://github.com/stamp-protocol/core/commit/e755b6a7c109b354b518f6c2663bddfea9075ecc)
#### Tuesday 2022-03-08 07:59:00 by Andrew Danger Lyon

replacing sodox::sign::* with ed25519-dalek

not super happy about this, because the two are NOT compatible, either
in key generation from seed or even in valid signature results (sigs
from sodox are "invalid" in ed25519-dalek for some godforsaken reason).

basically, this means all existing identities are completely invalid and
need to be regenerated, which sucks because i have to rebuild the Zephy
ID in the stamp doc (lol).

also, had to update a shit ton of tests and fix some serialization junk.
also, implementing rand_chacha20 since i thought it would make the
derive-from-seed signing keys line up. nope. oh well, at least it's more
secure than the StdRnd or w/e the hell it's called.

---
## [josefkarasek/api-1](https://github.com/josefkarasek/api-1)@[5b82635ef1...](https://github.com/josefkarasek/api-1/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Tuesday 2022-03-08 08:49:25 by W. Trevor King

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
## [raysofttr/BRS](https://github.com/raysofttr/BRS)@[1d08c7fb6e...](https://github.com/raysofttr/BRS/commit/1d08c7fb6e0ccee3fea85f68885c4bbbf9b06ecb)
#### Tuesday 2022-03-08 09:30:55 by BROOVS (BRS) PROJECTS

Update README.md

Broovs (BRS) Projects is a software and technology development company established by Turkish Academics at the Technopolis Technology Development Center. Their projects have an ecosystem focused on benefits to people and society. At this point, 12 projects have been produced and their planning has been completed. 
We have noticed that all projects support each other and create a consumption mechanism in each project, plan a fiction on the BRS Token owned by the company, and since the fiction and the structure of the company have been researched and passed the level of sharing with you, this report has been prepared for your information purposes. The company plans to make the BRS TOKEN, which is produced with high ease of use and awareness on the BSC network, an asset that will be used in many projects in the future. The company solves its projects with the support of its in-house technical team and academicians without the need for external procurement, and within the scope of the project,
1.	The dec generation search engine Broovs.com the beta version is active and has a user-oriented algorithm whose entries are made and approved by users. https://broovs.com 
2.	Playsore now active in the messenger app with Swift, now that are not available in any messaging app crypto wallet feature added that it belongs to any contract at the time of the BSc network to send and receive coins, it is possible https://swiftmessengerweb.com   
3.	The company has also identified a shortage in Turkey within the scope of BRS Projects and has been able to successfully list the BSC network https://coinswifter.com CoinSwifter, registered at the address, has activated the crypto trading platform. With this platform, easy and fast transactions can be made without using any brokerage exchange. 
4.	Simultaneously with the installation of the exchange, the secure Cold Wallet Swifter Wallet has been activated with the ability to carry out swap transactions and high-security storage. https://swifterwallet.com
5.	As a result of long-term studies, the Company has activated the XRAY-RAYCHAIN Blockchain, which they describe as the first open source Blockchain in Turkey, and the premining phase is underway. https://raychainscan.com 
6.	Turkey's first and only real Xray blockchain ’s NFT produce to be able to broovsblock broovsbox smart contract to be able to the next company and doing projects with companies, institutions and individuals of data security, data recording and data storage node participating in the network to perform operations that holds and each point will become a supporter of an xray. With the application that will be installed with the algorithm developed by our company based on the XRAY Blockchain, the memory of mobile phones will be increased up to 1 TB, which will prevent people from having to constantly change their mobile phones and ensure that the capital will remain in our country.
7.	The development stage is ongoing Fanmeter.tv with its project, it aims to achieve a first in the world by creating a scoring system for social media phenomena and ensuring that advertisers and families reach the right audience. https://fanmeter.tv 
We also mentioned Broovs.com , Swift Messenger, and Fanmeter.tv their projects are user-oriented projects and are designed as Web 3.0 projects that share their income with users after the developer shares have been separated and do not keep personal records. To get more information https://broovs.io you can visit his address.

---
## [specklesystems/speckle-sketchup](https://github.com/specklesystems/speckle-sketchup)@[9b5c043029...](https://github.com/specklesystems/speckle-sketchup/commit/9b5c043029fc93b3a0bc422c16b30fb0c9196a38)
#### Tuesday 2022-03-08 10:15:23 by izzy lyseggen

feat(ui): saved streams & 1-click send (#37)

* feat(ui): saved streams and wip 1 click

* style(connector): remove some puts statements

* feat(accounts): default acct helper

* feat(ui): more 1 click send

need a way to wait for connector launch...

* fix(ui): waiting quick send!

* feat(ui): view in web from toast notif

note to self: the one in frontend is kinda ugly 😓 
went with outine btn for now bc it was better than that big ol dark gray btn

* fix: turn off dev

i always fkn do this i needa just use an env file gdi

* feat(ui): notify ui of oneclick send

* feat(metrics): remove old and use the new!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[159875d8cd...](https://github.com/mrakgr/The-Spiral-Language/commit/159875d8cdb25e1060b987151664933d965734c7)
#### Tuesday 2022-03-08 12:14:43 by Marko Grdinić

"10:05am. Let me read the Baki translation and then I will start. The weather just keeps getting colder and colder. Yesterday I put in Win 10 on that 15 year old PC and it works fine. Those crappy Win 7 ISOs lead me down the wrong path. There is no point in paring Windows down if it turns out to have missing drivers.

I am a bit concerned how it put the .exe file for one of the cracks in the wrong Windows directory, c: instead of e:. Also, I've been installing Windows on e:, but for some reason it copies the old `Windows.old` to c:. I find this pretty confusing.

Let me read the thing and I will hook it up just for a few mins to check if Win XP that is still there works. It should.

10:20am. Actually let me chill a bit and then I will start. Today I will definitely finish the playlist.

10:40am. It is time to start. Let me just do this final checkup on that old PC and I'll pass it from my hands. After that come the Mantra tutorials.

10:45am. A-OK. I am done with that chore. Where was I with the Mantra Tut?

https://youtu.be/JtDQaYWkSsk?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=2
Surface Imperfections: Dirt mask & Occlusion mask — Procedural Material Creation with Mantra ep. 09

Let me watch this. Let me start Houd.

https://youtu.be/JtDQaYWkSsk?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=865

I really have to get familiar with writing OSL. That tiny bit that I have in nodes I should rewrite using OSL.

Let me first watch the video and then I will get on that.

https://youtu.be/JtDQaYWkSsk?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=906

Just how did he get a pattern like this. It boogles my mind. I thought he would get the dirt texture by loading it from file, but this is how he got it. If I was to do it procedurally, I'd never think of something like this. I'd just mix noise until something good came out.

11:15am. I dislike the tiling effect that the mask has. It was because of it that I was so certain it would be a premade texture.

Oh, yeah. V-Ray has a procedural dirt texture build it. I should take a look at it.

* OSL rewrite.
* Dirt texture.

https://youtu.be/JtDQaYWkSsk?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=1360

This is super boring, let me go wtih the bullet points.

First, let me replace the two float operations with an OSL node.

11:25am.

```vex
shader S(float a, float b, out float r) {
    r = a * (b - 1);
}
```

Let me back this up here.

https://thhube.github.io/tutorials/osl/osl.html

Let me copy that thing again.

Ah, that out should be output. The support for this is so poor that is not even giving me errors.

11:40am. This is way worse than I thought. Given that it has silent error checking, writing OSL directly and observing the results is out of the question. But the main problem with using this for small functions is that this only outputs big shaders - surface, volume and displacement. I can't use this to write `a * b`.

Crap.

11:45am. This is ridiculous. I should check the language spec. It is just too unlikely that `shader` only has bsdf outputs.

https://github.com/AcademySoftwareFoundation/OpenShadingLanguage
> Documentation -- at this point consisting of the OSL language specification (useful for shader writers), but in the future will have detailed documentation about how to integrate the OSL libraries into renderers.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Vector+Operations

I really have no idea why the operations nodes were so slopily designed in V-Ray.

I wish at least that the params weren't grayed out when the is no input. Well, nevermind that for now.

12:05pm. Nevermind this. If I have to do vector operations I'll just have to make do with what I have. It is not impossible just awkward. Let me go back to the video. I'll reserve the dirt texture for later.

https://youtu.be/wXf6PUdGZtI?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S
Types of Lights, Global Illumination, Render Noise and Settings — Rendering with Mantra ep. 10

Let me just move to the next thing. That video is too boring for me to bear. Actually, let me watch the lighthouse video.

https://youtu.be/zsxg3eWkNYM
Introduction to Vray for Houdini Tutorial

Let me resume this lighthouse tutorial. I was at 18m yesterday.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Material+Builder

Could I use regular Houdini nodes with V-Ray if I didn't dive into the builder?

https://youtu.be/zsxg3eWkNYM?t=1869

This part is really confusing me. So the user can set the weight even despite the input being plugged in?

12:50pm. Nope, I can't use the regular nodes with V-Ray ones. It will just fail to render. This is not at all surprising.

1pm. https://youtu.be/wXf6PUdGZtI?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S
Types of Lights, Global Illumination, Render Noise and Settings — Rendering with Mantra ep. 10

My focus is really low and I am not paying much attention. This is a sign that it is time to switch to doing my own things. I am really agitated at how hard regular vector operations are. I can't do things like take power

Ah, it has color operations! And those have power.

Damn you. Still, no nodes like sin and cos. No way to decompose the color and vector nodes to their individual pieces like in Blender. The fact that you can't use OSL to write utility functions is really disappointing.

1:10pm. The V-Ray node design really leaves much to be desired here. V-Ray ranges from really good to really bad when it comes to design.

Let me have breakfast here. I am going to give the rest of the tutorials a shot, but after that I'll move to just doing my own thing. I think I know quite a lot already and it is time to think about finishing the pool scene. It is going to look good."

---
## [matthewgismondi76/hidden-memory-tricks](https://github.com/matthewgismondi76/hidden-memory-tricks)@[841e1930de...](https://github.com/matthewgismondi76/hidden-memory-tricks/commit/841e1930de33a61d8206fa28f78fbd3f24147614)
#### Tuesday 2022-03-08 12:22:05 by Matthew Gismondi

Create recipes.sh

I am not posting this to give anyone ideas. I am posting this because I am being misrepresented, I am being denied a fair chance to be heard, and I am assumed to be a criminal and kept under close watch because of things I am not even doing. And I am tired of hearing other people list off the things they are annoyed that they have to deal with and realizing that those things would have been very much appreciated and needed if they had been sent to me and if they had been see for what they were supposed to be and not what they turned into. And as long as I am still dealing with the same cars that follow me around treating me like an enemy until they get right up to me, which is what used to happen, and as long as I have to listen to my neighbors take showers at very odd times of the night that coincide perfectly with when I would expect someone to have mercy and send relief, and as long as I hear people walk by my window and very loudly remind me of how disgusting I am after answering my call for help at someone else's door, and as long as people keep telling me that I am ok when i am not thinking that eventually I will believe it and get to the point that I am so desperate for it all to stop that I will be able to just will everyone's crimes away into oblivion and we would all be happy, then I will keep being a pain in everyone's ass about everything. Because I was the one who had Thunderstrike. I was the one who smelled violets in the ER bay in Marina del Rey when the nurse was confused about me being a real patient, and I was the one who couldn't get help that entire time I was stranded there because people thought I was the devil himself. Literally, I now am coming to realize. I was also the one in Davis when that girl was so excited to see me and I still have no idea why. And that same day I was the one who the shopkeeper accused of being a thief. I had just walked miles in flip flops and was tired and trying to call for help. I had no idea why everyone was so rude, but that is when the mixups started. I have no idea why because I was alone and I never made it anywhere. I ended up in that rest stop, #46, watching scissortails dance around on that scenic overlook. Now it has become even more difficult for me to be seen as who I am, and then under that who I am again. Several times over I was wrapped in disguises it feels like, and it seems like that's what is going on with this code too. Only the code is malicious. I am not. Or maybe it is not either and is just meant to protect everyone else because they think I am evil. But why would anyone consider me evil when my gifts came from Jehovah? If they didn't then I guarantee you there was some kind of malicious and underhanded swap that happened, but you would think that at some point someone somewhere along the way would have told me what it was that made them hate me so much.

---
## [linuxppc/linux](https://github.com/linuxppc/linux)@[a50e1fcbc9...](https://github.com/linuxppc/linux/commit/a50e1fcbc9b85fd4e95b89a75c0884cb032a3e06)
#### Tuesday 2022-03-08 12:30:57 by Josef Bacik

btrfs: do not WARN_ON() if we have PageError set

Whenever we do any extent buffer operations we call
assert_eb_page_uptodate() to complain loudly if we're operating on an
non-uptodate page.  Our overnight tests caught this warning earlier this
week

  WARNING: CPU: 1 PID: 553508 at fs/btrfs/extent_io.c:6849 assert_eb_page_uptodate+0x3f/0x50
  CPU: 1 PID: 553508 Comm: kworker/u4:13 Tainted: G        W         5.17.0-rc3+ #564
  Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS 1.13.0-2.fc32 04/01/2014
  Workqueue: btrfs-cache btrfs_work_helper
  RIP: 0010:assert_eb_page_uptodate+0x3f/0x50
  RSP: 0018:ffffa961440a7c68 EFLAGS: 00010246
  RAX: 0017ffffc0002112 RBX: ffffe6e74453f9c0 RCX: 0000000000001000
  RDX: ffffe6e74467c887 RSI: ffffe6e74453f9c0 RDI: ffff8d4c5efc2fc0
  RBP: 0000000000000d56 R08: ffff8d4d4a224000 R09: 0000000000000000
  R10: 00015817fa9d1ef0 R11: 000000000000000c R12: 00000000000007b1
  R13: ffff8d4c5efc2fc0 R14: 0000000001500000 R15: 0000000001cb1000
  FS:  0000000000000000(0000) GS:ffff8d4dbbd00000(0000) knlGS:0000000000000000
  CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  CR2: 00007ff31d3448d8 CR3: 0000000118be8004 CR4: 0000000000370ee0
  Call Trace:

   extent_buffer_test_bit+0x3f/0x70
   free_space_test_bit+0xa6/0xc0
   load_free_space_tree+0x1f6/0x470
   caching_thread+0x454/0x630
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? lock_release+0x1f0/0x2d0
   btrfs_work_helper+0xf2/0x3e0
   ? lock_release+0x1f0/0x2d0
   ? finish_task_switch.isra.0+0xf9/0x3a0
   process_one_work+0x26d/0x580
   ? process_one_work+0x580/0x580
   worker_thread+0x55/0x3b0
   ? process_one_work+0x580/0x580
   kthread+0xf0/0x120
   ? kthread_complete_and_exit+0x20/0x20
   ret_from_fork+0x1f/0x30

This was partially fixed by c2e39305299f01 ("btrfs: clear extent buffer
uptodate when we fail to write it"), however all that fix did was keep
us from finding extent buffers after a failed writeout.  It didn't keep
us from continuing to use a buffer that we already had found.

In this case we're searching the commit root to cache the block group,
so we can start committing the transaction and switch the commit root
and then start writing.  After the switch we can look up an extent
buffer that hasn't been written yet and start processing that block
group.  Then we fail to write that block out and clear Uptodate on the
page, and then we start spewing these errors.

Normally we're protected by the tree lock to a certain degree here.  If
we read a block we have that block read locked, and we block the writer
from locking the block before we submit it for the write.  However this
isn't necessarily fool proof because the read could happen before we do
the submit_bio and after we locked and unlocked the extent buffer.

Also in this particular case we have path->skip_locking set, so that
won't save us here.  We'll simply get a block that was valid when we
read it, but became invalid while we were using it.

What we really want is to catch the case where we've "read" a block but
it's not marked Uptodate.  On read we ClearPageError(), so if we're
!Uptodate and !Error we know we didn't do the right thing for reading
the page.

Fix this by checking !Uptodate && !Error, this way we will not complain
if our buffer gets invalidated while we're using it, and we'll maintain
the spirit of the check which is to make sure we have a fully in-cache
block while we're messing with it.

CC: stable@vger.kernel.org # 5.4+
Signed-off-by: Josef Bacik <josef@toxicpanda.com>
Signed-off-by: David Sterba <dsterba@suse.com>

---
## [FauziAkram/Stockfish](https://github.com/FauziAkram/Stockfish)@[cb9c2594fc...](https://github.com/FauziAkram/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Tuesday 2022-03-08 13:33:29 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [nyh/scylla](https://github.com/nyh/scylla)@[674d3a5a84...](https://github.com/nyh/scylla/commit/674d3a5a8465c365cb0e608f4c921e3c12b758c6)
#### Tuesday 2022-03-08 13:38:29 by Nadav Har'El

compound_compat.hh: add missing methods of iterator

While debugging legacy_compound_view, I noticed that it cannot be used
as a C++20 std::ranges::input_range because it is missing some trivial
methods. So let's fix this, and make the life of future developers a
little bit easier.

The two trivial methods we need to implement:

1. A postfix increment operator. We already had a prefix increment
   operator, but the C++20 concept weakly_iterable also needs postfix.

2. By mistake (this will be corrected in https://wg21.link/P2325R3),
   weakly_iterable also required the default_initialized concept, so
   our iterator type also needs a default constructor.
   We'll never actually use this silly constructor, and when this C++20
   standard mistake is corrected, we can remove this constructor.

After this patch, a legacy_compound_view is accepted for the C++20
ranges::input_range concept.

Signed-off-by: Nadav Har'El <nyh@scylladb.com>

---
## [mezzio/mezzio-aurarouter](https://github.com/mezzio/mezzio-aurarouter)@[836ae8d9d1...](https://github.com/mezzio/mezzio-aurarouter/commit/836ae8d9d1791188986eebadf7bd5c7428c54b9e)
#### Tuesday 2022-03-08 14:49:15 by Michał Bundyra

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
## [jkosh44/materialize](https://github.com/jkosh44/materialize)@[3af43e2538...](https://github.com/jkosh44/materialize/commit/3af43e25388609cb43b7ab352ffe03d34f89d552)
#### Tuesday 2022-03-08 14:53:38 by Nikhil Benesch

coord: allow SELECTing from unmaterialized sources

This commit allows `SELECT` queries to depend, directly or indirectly,
on unmaterialized sources. This was previously disallowed because we
didn't track the `since` frontier of unmaterialized sources; now we do.

Users will no longer see errors like

    unable to automatically determine a query timestamp

which is a huge upgrade in the user experience, in my opinion. The
downside is that users are not careful, a one-off query may result in
e.g. re-reading an entire Kafka source from the upstream broker. If it
becomes a problem, we can consider introducing a "safe mode" (maybe via
a session variable) that disallows queries that would re-instantiate a
source.

This new behavior facilitates making tables unmaterialized by default
(#10883). That change goes down more easily if you can `SELECT` from an
unmaterialized table.

---
## [DiosMussolinos/GonePhishing-Unity-2021.1.18f1](https://github.com/DiosMussolinos/GonePhishing-Unity-2021.1.18f1)@[da4bc6855d...](https://github.com/DiosMussolinos/GonePhishing-Unity-2021.1.18f1/commit/da4bc6855db684eeb2ebe21d10c667348669fc17)
#### Tuesday 2022-03-08 15:40:36 by Gabriel Vergari

I hate myself version 33. Tested and more shit fixed... OH GOD, LET ME END THIS

---
## [SingleSimha/YoutubeVideoDownloaderWebsite](https://github.com/SingleSimha/YoutubeVideoDownloaderWebsite)@[9acaf349ce...](https://github.com/SingleSimha/YoutubeVideoDownloaderWebsite/commit/9acaf349ce148cb4836e00f2f43dcdb54320106a)
#### Tuesday 2022-03-08 16:03:52 by SingleSimha

Lol 2160 and 1440p didnt work

Fuck youtube they didnt let me download 2160p videos i hate youtube.... i am just desprate to use yt.. FKKKKKKKKK I HATEEEE YOUTUBEEEEEEEEEEEEEEEEEEEEEEEEEE..... SUZAN YOU SUCKKKKKKKK

---
## [BrendonWatsonLab/Actigraphy](https://github.com/BrendonWatsonLab/Actigraphy)@[920f18628b...](https://github.com/BrendonWatsonLab/Actigraphy/commit/920f18628bad1fe7f78b3b4f918b9d1a0405f4ee)
#### Tuesday 2022-03-08 16:20:09 by David Kim

Bandaid

So I added some functionality that scales the LR and HR plots to look definitely different. The axis is now fixed, so you can choose it. Anyways, the weird ass time shift fucked me up, so I manually shifted it by 5 hours to fix it... The actual actigraphy that leads to the fucked up values is not fixed though... I gotta do some more digging is all...

---
## [SP-FA/generateDataset](https://github.com/SP-FA/generateDataset)@[8157b78d8c...](https://github.com/SP-FA/generateDataset/commit/8157b78d8c82b3e7e0896b626f09f65bfd4e5bc1)
#### Tuesday 2022-03-08 16:27:26 by SP-FA

update readme again

oh god im a fking stupid shit.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Tuesday 2022-03-08 17:57:56 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [pakaplace/commenda-ethdenver](https://github.com/pakaplace/commenda-ethdenver)@[a93eff73fb...](https://github.com/pakaplace/commenda-ethdenver/commit/a93eff73fb8454b9546ab29c45b0c30d1c531371)
#### Tuesday 2022-03-08 17:58:53 by Yaacov

Login with magic links using stytch - but UI is kinda fucked and auth checks are still dependent on the old login flow

---
## [KakarotKernel/kernel_realme_atoll](https://github.com/KakarotKernel/kernel_realme_atoll)@[a6af78a806...](https://github.com/KakarotKernel/kernel_realme_atoll/commit/a6af78a8067f8f9370616305df7ef9c1875037c5)
#### Tuesday 2022-03-08 18:00:55 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: sweetyicecare <gabrielseedev@outlook.com>
Signed-off-by: Jprimero15 <jprimero155@gmail.com>
Signed-off-by: Joel Gómez <nahuelgomez329@gmail.com>

Conflicts:
	mm/swapfile.c
	mm/swap.c

---
## [Binaergewitter/serious-bg](https://github.com/Binaergewitter/serious-bg)@[00ee869a80...](https://github.com/Binaergewitter/serious-bg/commit/00ee869a80b043f36a822d9a442c7bba11603870)
#### Tuesday 2022-03-08 19:13:03 by fliiiix

Remove Deezer from abo list

Because it is broken fuck you deezer

---
## [SuffolkLITLab/ALKiln](https://github.com/SuffolkLITLab/ALKiln)@[fe728649d3...](https://github.com/SuffolkLITLab/ALKiln/commit/fe728649d3b5a7be2d6cbf4eff90857d63a2986b)
#### Tuesday 2022-03-08 19:42:07 by plocket

Update our package's dependencies for v4 (#503)

I'm thinking this is just going to be for v4. Not bothering with this for v3 unless we absolutely have to since none of the vulnerabilities are severe. My current rationale is that the more work we do to maintain 3, the less work we can do getting v4 ready for release. Ready to hear opinions.

- Close #164, update cucumber to v7
- Prepare for v8 of cucumber because I won't remember it later
- Close #394, update puppeteer
- Update our version of node (and that of our action that we'll run for other people's libs). [Addresses #393 so we can use the suffolk npm org package.]
- Use `npm audit` to fix the remaining vulnerabilities (now 0)
- [Remove package.json as discussed in #489 to align our tests' behaviors with those of our users.]

* Update action.yml node to v17

* Update from cucumber v6 to v7. See details.

See https://github.com/cucumber/cucumber-js/blob/main/docs/migration.md#migrating-to-cucumber-js-7xx

Only use cucumber setDefaultTimeout globally and use a shim that replicates the fix in v8 that lets you do custom timeouts more easily so we can still give enough time for steps that may need more time.

Use all caps for statuses.

Test screenshot step.

Btw, the cucumber test output visually looks a bit different now - when a scenario passes, all the steps pass too.

Sorry about the little comment changes, etc. Tried to remove a lot of those incidental unrelated changes.

* Update puppeteer to latest (13). See details below.

- page.waitFor -> page.waitForTimeout and page.waitForSelector (Got deprication notice. See https://github.com/puppeteer/puppeteer/issues/6214.)
- remove removeEventListener (we'd need to change it to removeListener anyway - v4.0.0 and see https://github.com/puppeteer/puppeteer/blob/main/docs/api.md#eventemitterremovelistenerevent-handler). For now we'll count on page close taking care of it, just in case removing it would prevent multiple-file-downloads.

* Update GitHub worflow node version, tweak changelog item order

* Fix npm audit vulnerabilities and update action.yml cucumber

* Pin the colors lib in action.yml

* Remove package-lock.json #489, use kiln v4 for users, CHANGELOG

* Fix custom timeout, remove duplicate report entry, as per review

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ee3bf0cb1e...](https://github.com/mrakgr/The-Spiral-Language/commit/ee3bf0cb1e46211a16045d3a6eb9b990b46ea9d0)
#### Tuesday 2022-03-08 20:45:34 by Marko Grdinić

"2:15pm. https://www.patreon.com/posts/50498890
Heroine Survival Chapter 1

I've been meaning to pick this up for a while as I have a soft spot for killer girls. But I just wanted to note that this is posted on Patreon of all things. I didn't know that this was possibel. I'd of course want to make my own place as soon as possible, but until I get some kind of income will post stuff on places like Twitter and potentially here.

Let me leave this for later. Let me finish the Mantra shading tutorial and then I will get started on my own stuff. I need to master shading, and it won't be too hard.

https://youtu.be/wXf6PUdGZtI?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S
Types of Lights, Global Illumination, Render Noise and Settings — Rendering with Mantra ep. 10

Let me start this.

2:35pm. https://youtu.be/oUWFxqhJDlA?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S
Car Paint Shader, Fresnel, Frosted Glass Effect — Rendering with Mantra ep. 11

Let me start skimming. I do not feel like watching all of this.

https://youtu.be/oUWFxqhJDlA?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=907

He says that the sheen makes normals which look outwards the camera look lighter.

I guess I have an answer what that is.

3:05pm. I am dead, I can't go on anymore with these tutorials.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Material

Right now I am reading the docs for a bit. I was wonering what Coat is, but I think it is literally another layer on top of the first one.

3:35pm. No, that is not true. The coat literally just multiplies the numbers of the diffuse color. I was confused as to how the changes are going, but it is a straightforward multiplication. This can lead to unexpected results unless you use a grayscale value for the coat.

I see why Blender calls it clear coat. I could use this as a mask.

3:40pm. But it not a huge deal. Let me check out sheen.

3:50pm. A little bit of experience goes a long way. Sheen is very similar to frenel. The main difference is that the diffuse color gets interpolated with the sheen color. I did not understand this while I was back at Blender.

4:20pm. Let me take a break. I think I will step away from the screen for just a bit.

I've been going at it tirelessly for over a week, but now it is time to step back just a little bit and review.

I...can do it.

5:20pm. Let me resume. I used to do these motivational brainstorming sessions all the time when I was programming.

Let me just play with mirrors a bit and then I will go forward with my plan.

5:40pm. Hmmm, I see.

When I was messing with Blender I did not really think too deeply about the index of refraction. But now I see that if you crank it up, it is possible to make dielectric surfaces into mirror.

My initial impression was that dielectrics have weaker reflections, but now I understand that the situation is more nuanced. For dielectrics their reflectivity is strongly dependent on the IOR. Back then I did not want to mess with the parameter, but now that I've done so I feel that I've learned a lot. IOR of water is 1.3, right?

https://knowledge.autodesk.com/support/3ds-max/learn-explore/caas/CloudHelp/cloudhelp/2015/ENU/3DSMax/files/GUID-CCD9B76C-9AC6-46E6-8B9C-E367CFC0FDAF-htm.html

Hmmm, I see. Even air itself is 1.0003.

6pm. I needed to do this bit of thinking.

8:10pm. I am still thinking about it. I've been doing a skill check in my head, and have been stuck on figuring out the best way to do a pattern that I once saw. It was a radial block pattern.

8:20pm. This issue I am grinding away at right now is so annoying and it does not matter in the least. I am being dumb by even thinking about it.

At any rate, going over all that I've learned in the last...7 weeks, I can tell it is quite a lot. I know a lot of modeling, and in the last week I learned quite a bit about shading.

8:45pm. Ok, I figured the problem of how to move the centroid out from a poligon. Forget this for now.

To reusme the earlier thread, I've learned an enormous amount of Houdini at this point. What am I still missing?

Well, I go back to the start and watch that spiral tower video. There are also video on the Houdini site.

But that can be put aside for now. I certainly know enough.

Yeah, I am done with the tutorials for the time being.

It is time to put what I know into action. I've learned the equivalent of sketching in Houdini and now it is time to move to painting.

I've gone over all that I can with geometry, and all that I can do with shaders. It might seem fancy, but what it allows me is to be smart with repetition. It might be a definite step up in abstraction compared to Blender, but it is still 3d art at its root. All it does is allow me to add a little programming flair.

9:10pm. It is going to be good when I get going.

Honestly, I've been kind of slow, and I do not know how much that is going to improve. I've never been a speed demon. In that respect, going for a VN first is a not a bad idea. If I went for a manga, I'd probably burn out.

9:15pm. Let me close here 'early' for a change. Tomorrow, I am definitely going to start grinding things out. It really is not that complicated. Put the diffise, put the falloff, put in the translucent, put in self illumination, add some noise on top of that. The vines are not something that should give me too much trouble. I just have to let go of my pretensions.

It is geometry itself that shoudl be the hard part of doing art. By the time you are done with sketching yuo should have the scene fully visualized.

9:15pm. One thing I regret is the way I did the flower. The way I've done it would make some things more difficult. Instead of doing a sweep, I should have made flower and then either bent it or path deformed it. That would have allowed me to have stable uvs, for one. I could use that for some special patterns on the vines.

I think I am going to go for that. There is no reason I can't redo the core parts of the scene. In Blender this would be hard, but in Houdini it is a piece of cake.

But I should not get fancy right at the start. Let me do the basic thing and then I'll consider what to do from here. I would not be surprised if the basic thing turns out to be good enough.

The important thing is to just sit down and just get things out.

Those AI chips are waiting for me and Spiral is sitting there waiting to be used.

I have two choices:

* Get a job and get the resources that I need to chase the Singularity that way.
* Acquire manipulation tree skills and target the world directly.

Either I can sell myself into slavery and join the NPC ranks, or I can take risks. I did get close to getting a job that one time. If the offer was not 2.5k, but something reasonable, I'd have taken it and by now have enough money to afford the chips and a lot of other things besides. But it would be a pity to withhold Heaven's Key from the world. I'll make it a blow it won't recover from. I'll get a good hit, get the money for the chip by the end of it and acquire the power I've been dreaming about.

No matter which path, capitalism will take its bite out of me.

A scholar sells his intellect.
A laborer sells his strength.
An artist his dream.

But rather than be an artist, I should be a prophet. Rather than selling my brain, muscle or heart, I should sell my eyes.

Dreams come and go, but my vision will be neverending. That is what I should aspire to.

Instead of relying on my brain, I should rely on my desire. My will, Heaven's Key will happen."

---
## [mosra/magnum-plugins](https://github.com/mosra/magnum-plugins)@[17a474540a...](https://github.com/mosra/magnum-plugins/commit/17a474540add0ad475aaaaf2c9928873bdc68f1a)
#### Tuesday 2022-03-08 20:55:38 by Vladimír Vondruš

AssimpImporter: port to the new Utility::Path.

The only notable change is that reading of external *empty* files will
succeed, while before it was treated the same as a read failure. Plus
thanks to Utility::Path taking Corrade::StringView we no longer need to
do insane shit like

    "basename" + std::string{".some-suffix"}

and suffering from one allocation for the suffix temporary string and
another for the concatenation result, but can do just the following with
just a single allocation:

    "basename"_s + ".some-suffix"

---
## [mosra/magnum-plugins](https://github.com/mosra/magnum-plugins)@[17c2513653...](https://github.com/mosra/magnum-plugins/commit/17c25136531da9362f396b2f234b01328dab6438)
#### Tuesday 2022-03-08 20:55:38 by Vladimír Vondruš

{Cgltf,TinyGltf}Importer: port to the new Utility::Directory.

Now the importer will properly fail when referenced files (buffers,
images) exist but can't be read -- instead of silently continuing,
failing subsequently due to the zero-size bufer being too small or an
empty image file having unknown format. Plus thanks to Utility::Path
taking Corrade::StringView we no longer need to do insane shit like

    "basename" + std::string{".some-suffix"}

and suffering from one allocation for the suffix temporary string and
another for the concatenation result, but can do just the following with
just a single allocation:

    "basename"_s + ".some-suffix"

Other than that, mostly just busywork.

---
## [TerraLindaHighSchool/memorium-memorium-production-team](https://github.com/TerraLindaHighSchool/memorium-memorium-production-team)@[97ed4ef350...](https://github.com/TerraLindaHighSchool/memorium-memorium-production-team/commit/97ed4ef35003ac75fbc7f016dd93a6b2599de8ec)
#### Tuesday 2022-03-08 21:10:23 by WoofMeister

i hate you stupid github you need to die jk lol not really haha funny also i put angyboi inside unity bc hawt

---
## [4cm4k1/next.js](https://github.com/4cm4k1/next.js)@[91146b23a2...](https://github.com/4cm4k1/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Tuesday 2022-03-08 21:16:06 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [serd2011/terminal](https://github.com/serd2011/terminal)@[f2ebb21bd1...](https://github.com/serd2011/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Tuesday 2022-03-08 21:57:59 by Mike Griese

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
## [serd2011/terminal](https://github.com/serd2011/terminal)@[442432ea15...](https://github.com/serd2011/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Tuesday 2022-03-08 21:57:59 by Mike Griese

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
## [mawrick26/SM8250](https://github.com/mawrick26/SM8250)@[cc2c0a0a43...](https://github.com/mawrick26/SM8250/commit/cc2c0a0a43b741664709ad95899f988f1c19bb2b)
#### Tuesday 2022-03-08 22:21:41 by George Spelvin

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

---
## [mawrick26/SM8250](https://github.com/mawrick26/SM8250)@[171a414606...](https://github.com/mawrick26/SM8250/commit/171a41460639b8c8068ff131523ba26dd0923109)
#### Tuesday 2022-03-08 22:21:41 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[83c7559f7c...](https://github.com/sojourn-13/sojourn-station/commit/83c7559f7c9d151b330239652f0b66ba3463584a)
#### Tuesday 2022-03-08 22:48:05 by WilliamNelson37

Fratellis and Co

Finishes the Fratellis

Removed Low level code that allowed staff to vore people (why the fuck)

Removed Low level code that allowed staff to regurgitate vored people (god's light has diminished)

---

