## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-22](docs/good-messages/2022/2022-02-22.md)


1,846,586 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,846,586 were push events containing 2,948,119 commit messages that amount to 209,413,834 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 26 messages:


## [vzaliva/cerberus](https://github.com/vzaliva/cerberus)@[2a8f7721b3...](https://github.com/vzaliva/cerberus/commit/2a8f7721b34cc13fd6db9fd6a6e775520d2f45de)
#### Tuesday 2022-02-22 00:22:02 by Thomas Sewell

Tweak nested time log to ~JSON

Maybe it would make sense if the log parsed as a native
JSON object and/or python value? Some progress in that
direction, but it isn't exactly working out great.

(It's annoying that JSON doesn't seem to permit a trailing
comma, e.g. [ 1, 2, 3, ], so that the printer needs either
state or silly hacks to avoid printing too many commas.)

---
## [WordPress/gutenberg](https://github.com/WordPress/gutenberg)@[f30420f02b...](https://github.com/WordPress/gutenberg/commit/f30420f02bec757f1b4c3fff03ce05d0229ec7ed)
#### Tuesday 2022-02-22 00:35:12 by Dennis Snell

Blocks: Remember raw source block for invalid blocks.

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `source` attribute on a block which
only exists for invalid blocks at the time of this patch. That `source`
carries the original un-processed data for a block node and can be used
to reconstruct the original markup without using garbage data and without
inadvertently changing it through the series of autofixes, deprecations,
and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `source` property to provide
a more consistent and trusting experience for working with unrecognized
content.

---
## [SarmentiCampbell/Skyrat-tg](https://github.com/SarmentiCampbell/Skyrat-tg)@[1f70226654...](https://github.com/SarmentiCampbell/Skyrat-tg/commit/1f70226654438f75811a2d59ad9c52bf88c048fc)
#### Tuesday 2022-02-22 00:36:18 by SkyratBot

[MIRROR] Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit [MDB IGNORE] (#11027)

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit

Co-authored-by: Iamgoofball <iamgoofball@gmail.com>

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[906fb0682b...](https://github.com/Sealed101/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Tuesday 2022-02-22 00:39:22 by necromanceranne

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
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[2209c36036...](https://github.com/DesmontTiney/tgstation/commit/2209c36036c5c0c303443fd4a6304da9384e5107)
#### Tuesday 2022-02-22 00:43:52 by san7890

Fixes Weird Area Definition on DeltaStation (#64986)

So, there I was. Pondering the blobbosity of Auxiliary Base Construction. Deciphering and unclothing the issue in my mind in order to better comphrehend it. I was there for a few moments, until this ugly beast of a fucking area definition caught my eye:

Hideous. Repugnant. I was relishing the thought of dissecting Auxiliary Base Construction into fifteen million more areas (it _will_ lessen obtusities) when that scraggletooth of an utterly mortifying error forced me into a visceral rage: the likes of which have never been experienced on this planet Earth.

---
## [bellomia/MOTTlab](https://github.com/bellomia/MOTTlab)@[7efab486a7...](https://github.com/bellomia/MOTTlab/commit/7efab486a739f5d8156131da87a5e2a346ee180f)
#### Tuesday 2022-02-22 01:32:53 by Gabriele Bellomia

First try at square lattice

Works, but it poses loads of problems:

- The Symbolic Math Toolbox function ellipticK() is soooooo muuuuuuch sloooooooooooooooow, its computing time dominates everything. I guess I should have forseen this: a symbolic implementation to process very dense numerical samples of complex numbers it's such a bad idea. Overall a bethe lattice loop takes ~300ms, while a square lattice loop around 24s, that is a x80 slowdown. Damn it.

- Anyway I'd prefer to avoid forcing yet another toolbox dependency.

HENCE

Could we try the good old fft-powered numerical way?

1. Generate the DOS by whatever, numerical, method (even elliptic integrals, but numerical, probably the standard ellipke() MATLAB function). If things go really bad fuck it, let's generate it one time and store a binary file in the repository.

2. Go by definition of self-consistency: Gloc(z) = H[DOS](z-Sloc(z)), an Hilbert transform to which we feed the DOS (generated or tabulated, whatever). But how the hell we evaluate a transform at given z-Sigma(z)? THIS COULD BE AN INEVITABLE PROBLEM.

NB1) Frustration apart, we'd try to avoid tabulating the DOSes, we want flexibility with the energy sampling and interpolating / downsampling could be cumbersome.

NB2) If we succeed generating the DOS we should consider avoiding regenerating at each loop. Instead of passing around a string identifying the lattice we should then consider passing directly the generated DOS.

NB3) This has to perform better than the symbolic method in gftools, BUT it could still be significantly slower / less accurate than the current implementation, for the Bethe lattice. Maybe let's make the DOS argument optional and fall back to the bethe lattice by default. This way the blazing-fast, reliable, infinite-dimensions implementation would be preserved.

---
## [JohnKnee3/zookeepr](https://github.com/JohnKnee3/zookeepr)@[f530421036...](https://github.com/JohnKnee3/zookeepr/commit/f530421036858cfd1a0af4154957a30125dacb4e)
#### Tuesday 2022-02-22 02:20:14 by john.a.clark3

11.1.5

We first used a simple
app.get('/api/animals', (req, res) => {
  res.send('Hello!');
});
That sent Hello if our .get was talking to animals.json animals object.

Then we updated it
app.get('/api/animals', (req, res) => {
  res.json(animals);
});
To grab the entire animals array using .get instead of .send.

Then we used this

app.get('/api/animals', (req, res) => {
  let results = animals;
  console.log(req.query)
  res.json(results);
});
+
 http://localhost:3001/api/animals?name=Erica
To console log the name Erica.

Finally we updated the .get into it's final form
app.get('/api/animals', (req, res) => {
  let results = animals;
  if (req.query) {
    results = filterByQuery(req.query, results);
  }
  res.json(results);
});
to set it up to receive .querys that talk to the function filterbyQuery.

function filterByQuery(query, animalsArray) {
  let filteredResults = animalsArray;
  if (query.diet) {
    filteredResults = filteredResults.filter(animal => animal.diet === query.diet);
  }
  if (query.species) {
    filteredResults = filteredResults.filter(animal => animal.species === query.species);
  }
  if (query.name) {
    filteredResults = filteredResults.filter(animal => animal.name === query.name);
  }
  return filteredResults;
}
Which will look at what you type for example
http://localhost:3001/api/animals?name=Erica
grabs Erica's object
{
      "id": "2",
      "name": "Erica",
      "species": "gorilla",
      "diet": "omnivore",
      "personalityTraits": ["quirky", "rash"]
    },
and
http://localhost:3001/api/animals?species=gorilla
would grab
{
"id": "1",
"name": "Terry",
"species": "gorilla",
"diet": "omnivore",
"personalityTraits": [
"anxious",
"goofy"
]
},
{
"id": "2",
"name": "Erica",
"species": "gorilla",
"diet": "omnivore",
"personalityTraits": [
"quirky",
"rash"
]
}
We finally set up the personalityTraits query which is a bit more involved because it is an array.

function filterByQuery(query, animalsArray) {
  let personalityTraitsArray = [];
  // Note that we save the animalsArray as filteredResults here:
  let filteredResults = animalsArray;
  if (query.personalityTraits) {
    // Save personalityTraits as a dedicated array.
    // If personalityTraits is a string, place it into a new array and save.
    if (typeof query.personalityTraits === "string") {
      personalityTraitsArray = [query.personalityTraits];
    } else {
      personalityTraitsArray = query.personalityTraits;
    }
    // Loop through each trait in the personalityTraits array:
    personalityTraitsArray.forEach((trait) => {
      // Check the trait against each animal in the filteredResults array.
      // Remember, it is initially a copy of the animalsArray,
      // but here we're updating it for each trait in the .forEach() loop.
      // For each trait being targeted by the filter, the filteredResults
      // array will then contain only the entries that contain the trait,
      // so at the end we'll have an array of animals that have every one
      // of the traits when the .forEach() loop is finished.
      filteredResults = filteredResults.filter(
        (animal) => animal.personalityTraits.indexOf(trait) !== -1
      );
    });
  }
was added to the top and used the initial if statement to check if you one trait else you checked for multiple.  Then it assings it to the personality traits array let.  Then using for each it finds each query and grabs what is needed.

Very dense and may need to read again.

---
## [mwmichalek/MyQ](https://github.com/mwmichalek/MyQ)@[59752e5886...](https://github.com/mwmichalek/MyQ/commit/59752e58865037baf99ad7f8d1a323d42df0e631)
#### Tuesday 2022-02-22 02:54:09 by mwmichalek

For some reason requests to the server aren't going out.  Fuck you!

---
## [afkvido-development/MessageEngine](https://github.com/afkvido-development/MessageEngine)@[6cdd8def88...](https://github.com/afkvido-development/MessageEngine/commit/6cdd8def88a9e7c28cc2aecee61f0d25548d8d12)
#### Tuesday 2022-02-22 03:16:24 by gemsvido

MessageEngine

I'VE FIXED MESSAGEENGINE

THANK GOD

OK I AM NEVER USING MAVEN AGAIN

FUCK YOU, MAVEN

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[defe30ea4a...](https://github.com/Koi-3088/ForkBot.NET/commit/defe30ea4aada2a29b94d97eefac5a1c1e0618cf)
#### Tuesday 2022-02-22 04:12:15 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [flick-23/SEM-5](https://github.com/flick-23/SEM-5)@[f328e8fc5f...](https://github.com/flick-23/SEM-5/commit/f328e8fc5fc12fa009ab5c740f478a29ec0d3e59)
#### Tuesday 2022-02-22 05:00:43 by Venkatesh D

If you're using this, and just in case you're someone i don't like, then fuck you :) Other good peeps feel free to use

---
## [JoelSpeed/api](https://github.com/JoelSpeed/api)@[5b82635ef1...](https://github.com/JoelSpeed/api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Tuesday 2022-02-22 10:05:33 by W. Trevor King

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
## [neha-p6/chef](https://github.com/neha-p6/chef)@[9c615241b5...](https://github.com/neha-p6/chef/commit/9c615241b52a3947549bc17ab85e256dc47be7ab)
#### Tuesday 2022-02-22 11:12:00 by Lamont Granquist

Disable knife gem install in kitchen tests

This causes horrible issues.

We are installing knife in a TK virt and can't really build it and
install it as a test (hacking up appbundler to do this would largely
invalidate the test since we wouldn't be testing customer behavior)
and as such it needs to be installed from rubygems.  That means
installing knife-17, which pulls down chef-17 which currently has
a dep on diff-lcs 1.3.x which conflicts with 1.5.x which throws
the errors around the binstubs conflicting (which may or may not be
a rubygems bug, I investigated that a bit and couldn't determine
why that is happening since the 3rd line has the magic rubygems
comment).  We can't just use "--force" as an option since that'll
ignore deps and stuff as well which is precisely the kinds of things
that we're trying to catch.  So for now this test is more pain
that it is worth.

Signed-off-by: Lamont Granquist <lamont@scriptkiddie.org>

---
## [cjhead/dwm](https://github.com/cjhead/dwm)@[67d76bdc68...](https://github.com/cjhead/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Tuesday 2022-02-22 13:03:31 by Chris Down

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
## [cosanta/cosanta-core](https://github.com/cosanta/cosanta-core)@[1f35c2b23b...](https://github.com/cosanta/cosanta-core/commit/1f35c2b23b6eb7e4f48a34ca8ed9e1ab9bde9300)
#### Tuesday 2022-02-22 13:45:05 by Wladimir J. van der Laan

Merge #10271: Use std::thread::hardware_concurrency, instead of Boost, to determine available cores

937bf4335 Use std::thread::hardware_concurrency, instead of Boost, to determine available cores (fanquake)

Pull request description:

  Following discussion on IRC about replacing Boost usage for detecting available system cores, I've opened this to collect some benchmarks + further discussion.

  The current method for detecting available cores was introduced in #6361.

  Recap of the IRC chat:
  ```
  21:14:08 fanquake: Since we seem to be giving Boost removal a good shot for 0.15, does anyone have suggestions for replacing GetNumCores?
  21:14:26 fanquake: There is std::thread::hardware_concurrency(), but that seems to count virtual cores, which I don't think we want.
  21:14:51 BlueMatt: fanquake: I doubt we'll do boost removal for 0.15
  21:14:58 BlueMatt: shit like BOOST_FOREACH, sure
  21:15:07 BlueMatt: but all of boost? doubtful, there are still things we need
  21:16:36 fanquake: Yea sorry, not the whole lot, but we can remove a decent chunk. Just looking into what else needs to be done to replace some of the less involved Boost usage.
  21:16:43 BlueMatt: fair
  21:17:14 wumpus: yes, it makes sense to plan ahead a bit, without immediately doing it
  21:18:12 wumpus: right, don't count virtual cores, that used to be the case but it makes no sense for our usage
  21:19:15 wumpus: it'd create a swarm of threads overwhelming any machine with hyperthreading (+accompanying thread stack overhead), for script validation, and there was no gain at all for that
  21:20:03 sipa: BlueMatt: don't worry, there is no hurry
  21:59:10 morcos: wumpus: i don't think that is correct
  21:59:24 morcos: suppose you have 4 cores (8 virtual cores)
  21:59:24 wumpus: fanquake: indeed seems that std has no equivalent to physical_concurrency, on any standard. That's annoying as it is non-trivial to implement
  21:59:35 morcos: i think running par=8 (if it let you) would be notably faster
  21:59:59 morcos: jeremyrubin and i discussed this at length a while back... i think i commented about it on irc at the time
  22:00:21 wumpus: morcos: I think the conclusion at the time was that it made no difference, but sure would make sense to benchmark
  22:00:39 morcos: perhaps historical testing on the virtual vs actual cores was polluted by concurrency issues that have now improved
  22:00:47 wumpus: I think there are not more ALUs, so there is not really a point in having more threads
  22:01:40 wumpus: hyperthreads are basically just a stored register state right?
  22:02:23 sipa: wumpus: yes but it helps the scheduler
  22:02:27 wumpus: in which case the only speedup using "number of cores" threads would give you is, possibly, excluding other software from running on the cores on the same time
  22:02:37 morcos: well this is where i get out of my depth
  22:02:50 sipa: if one of the threads is waiting on a read from ram, the other can use the arithmetic unit for example
  22:02:54 morcos: wumpus: i'm pretty sure though that the speed up is considerably more than what you might expect from that
  22:02:59 wumpus: sipa: ok, I back down, I didn't want to argue this at all
  22:03:35 morcos: the reason i haven't tested it myself, is the machine i usually use has 16 cores... so not easy due to remaining concurrency issues to get much more speedup
  22:03:36 wumpus: I'm fine with restoring it to number of virtual threads if that's faster
  22:03:54 morcos: we should have somene with 4 cores (and ￼ actually test it though, i agree
  22:03:58 sipa: i would expect (but we should benchmark...) that if 8 scriot validation threads instead of 4 on a quadcore hyperthreading is not faster, it's due to lock contention
  22:04:20 morcos: sipa: yeah thats my point, i think lock contention isn't that bad with 8 now
  22:04:22 wumpus: on 64-bit systems the additional thread overhead wouldn't be important at least
  22:04:23 gmaxwell: I previously benchmarked, a long time ago, it was faster.
  22:04:33 gmaxwell: (to use the HT core count)
  22:04:44 wumpus: why was this changed at all then?
  22:04:47 wumpus: I'm confused
  22:05:04 sipa: good question!
  22:05:06 gmaxwell: I had no idea we changed it.
  22:05:25 wumpus: sigh ￼
  22:05:54 gmaxwell: What PR changed it?
  22:06:51 gmaxwell: In any case, on 32-bit it's probably a good tradeoff... the extra ram overhead is worth avoiding.
  22:07:22 wumpus: https://github.com/bitcoin/bitcoin/pull/6361
  22:07:28 gmaxwell: PR 6461 btw.
  22:07:37 gmaxwell: er lol at least you got it right.
  22:07:45 wumpus: the complaint was that systems became unsuably slow when using that many thread
  22:07:51 wumpus: so at least I got one thing right, woohoo
  22:07:55 sipa: seems i even acked it!
  22:07:57 BlueMatt: wumpus: there are more alus
  22:08:38 BlueMatt: but we need to improve lock contention first
  22:08:40 morcos: anywya, i think in the past the lock contention made 8 threads regardless of cores a bit dicey.. now that is much better (although more still to be done)
  22:09:01 BlueMatt: or we can just merge #10192, thats fee
  22:09:04 gribble: https://github.com/bitcoin/bitcoin/issues/10192 | Cache full script execution results in addition to signatures by TheBlueMatt · Pull Request #10192 · bitcoin/bitcoin · GitHub
  22:09:11 BlueMatt: s/fee/free/
  22:09:21 morcos: no, we do not need to improve lock contention first.   but we should probably do that before we increase the max beyond 16
  22:09:26 BlueMatt: then we can toss concurrency issues out the window and get more speedup anyway
  22:09:35 gmaxwell: wumpus: yea, well in QT I thought we also diminished the count by 1 or something?  but yes, if the motivation was to reduce how heavily the machine was used, thats fair.
  22:09:56 sipa: the benefit of using HT cores is certainly not a factor 2
  22:09:58 wumpus: gmaxwell: for the default I think this makes a lot of sense, yes
  22:10:10 gmaxwell: morcos: right now on my 24/28 physical core hosts going beyond 16 still reduces performance.
  22:10:11 wumpus: gmaxwell: do we also restrict the maximum par using this? that'd make less sense
  22:10:51 wumpus: if someone *wants* to use the virtual cores they should be able to by setting -par=
  22:10:51 sipa: *flies to US*
  22:10:52 BlueMatt: sipa: sure, but the shared cache helps us get more out of it than some others, as morcos points out
  22:11:30 BlueMatt: (because it means our thread contention issues are less)
  22:12:05 morcos: gmaxwell: yeah i've been bogged down in fee estimation as well (and the rest of life) for a while now.. otherwise i would have put more effort into jeremy's checkqueue
  22:12:36 BlueMatt: morcos: heh, well now you can do other stuff while the rest of us get bogged down in understanding fee estimation enough to review it ￼
  22:12:37 wumpus: [to answer my own question: no, the limit for par is MAX_SCRIPTCHECK_THREADS, or 16]
  22:12:54 morcos: but to me optimizing for more than 16 cores is pretty valuable as miners could use beefy machines and be less concerned by block validation time
  22:14:38 BlueMatt: morcos: i think you may be surprised by the number of mining pools that are on VPSes that do not have 16 cores ￼
  22:15:34 gmaxwell: I assume right now most of the time block validation is bogged in the parts that are not as concurrent. simple because caching makes the concurrent parts so fast. (and soon to hopefully increase with bluematt's patch)
  22:17:55 gmaxwell: improving sha2 speed, or transaction malloc overhead are probably bigger wins now for connection at the tip than parallelism beyond 16 (though I'd like that too).
  22:18:21 BlueMatt: sha2 speed is big
  22:18:27 morcos: yeah lots of things to do actually...
  22:18:57 gmaxwell: BlueMatt: might be a tiny bit less big if we didn't hash the block header 8 times for every block. ￼
  22:21:27 BlueMatt: ehh, probably, but I'm less rushed there
  22:21:43 BlueMatt: my new cache thing is about to add a bunch of hashing
  22:21:50 BlueMatt: 1 sha round per tx
  22:22:25 BlueMatt: and sigcache is obviously a ton
  ```

Tree-SHA512: a594430e2a77d8cc741ea8c664a2867b1e1693e5050a4bbc8511e8d66a2bffe241a9965f6dff1e7fbb99f21dd1fdeb95b826365da8bd8f9fab2d0ffd80d5059c

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[00cb8cc0af...](https://github.com/canalplus/rx-player/commit/00cb8cc0af5c0f5caec6b183e2f8dce13096ae1c)
#### Tuesday 2022-02-22 14:01:13 by Paul Berberian

Switch from a `Manifest` class to a `IManifest` interface

The `Manifest` object was a class describing a content regardless of the
streaming protocol (e.g. DASH, Smooth etc.) used:
  - Its URL (at which it can be refreshed)
  - Its minimum and maximum seekable position
  - The description of the available audio/video/text tracks and
    qualities
  - How to request initialization and media segments
  - decryption initialization data
  - and many other things

It is thus a central part of the RxPlayer.

However, the fact that it is defined as a class made us encounter
several issues over time:
  1. No asynchronous operation can happen at object construction. This
     mainly have been problematic recently, as I wanted to use an
     asynchronous Web API (MediaCapabilities's decodingInfo object) to
     detect support to define a property of a `Representation` (which is
     another class inside the `Manifest`'s instance).

     At the end, I may not decide to go in this road (defining the
     property as instanciation) for various other reasons, but the
     possible need to define asynchronous properties still could stand in
     the future.

  2. At instanciation, no other value (excepted the constructed
     `Manifest` object) can be returned.
     This was already problematic as various minor issues can occur
     while instanciating a `Manifest` (e.g. a track has no supported
     codec).

     Due to this, the idea was previously to define a new property of
     the `Manifest`, called `contentWarnings`, which contained all those
     issues. This was kind of a hack.

  3. I remember wanting in the past to have multiple potential
     constructors, with different arguments given, to unlock advanced
     features while staying readable.

     This is not really possible with `classes`, at least not easily
     and readably.

Those are the reason why this commit is a proposal to define an
`IManifest` interface instead and having regular functions constructing
it.
However doing this has also several disadvantages:

  - Property names and method signatures are duplicated: once at type
    definition and the other time in the function that creates it.

    As they are in two separate places, we might also more easily forget
    to update e.g. the documentation when doing changes.

  - tsserver's "go to definition" feature presents in most editors is
    going to favour the interface over the code. This can be good as
    that's where the documentation is, but also bad as that's not where
    the real logic is.

  - it's not possible to call `instanceof` anymore on it, and the most
    probable replacement is doing good ol' and ugly duck typing.

    However this was done at only one place in the code (checking if the
    `initialManifest` `loadVideo` option is a `Manifest` instance).

---
## [kvoli/cockroach](https://github.com/kvoli/cockroach)@[255c1fb027...](https://github.com/kvoli/cockroach/commit/255c1fb02708f99fef62b0af719af5e0984d9de3)
#### Tuesday 2022-02-22 15:16:52 by craig[bot]

Merge #71542 #73319 #74077 #76401 #76748

71542: backupccl: Support RESTORE SYSTEM USERS from a backup r=gh-casper a=gh-casper

Support a new variant of RESTORE that recreates system users that don't exist in current cluster from a backup that contains system.users and also grant roles for these users. Example invocation: RESTORE SYSTEM USERS FROM 'nodelocal://foo/1';

Similar with full cluster restore, we firstly restore a temp system database which contains system.users and system.role_members into the restoring cluster and insert users and roles into the current system table from the temp system table.

Fixes: #45358

Release note (sql change): A special flavor of RESTORE, RESTORE SYSTEM USERS FROM ..., is added to support restoring system users from a backup. When executed, the statement recreates those users which are in a backup of system.users but do not currently exist (ignoring those who do) and re-grant roles for users if the backup contains system.role_members.

73319: jobs: Execute scheduled jobs on a single node in the cluster. r=miretskiy a=miretskiy

Execute scheduled jobs daemon on a single node -- namely, the lease
holder for meta1 range lease holder.

Prior to this change, scheduling daemon was running on each node,
polling scheduled jobs table periodically with a `FOR UPDATE` clause.
Unfortunately, job planning phase (namely, the backup planning phase) could
take significant amount of time.  In such situation, the entirety
of the scheduled jobs table would be locked, resulting in inability
to introspect the state of schedules (or jobs) via `SHOW SCHEDULES` or similar
statements.

Furthermore, dropping `FOR UPDATE` clause by itself is not ideal because
that would lead to expensive backup planning being executed on almost every
node, with all but 1 node making progress.

The single node mode is disabled by default, but can be enabled
via a `jobs.scheduler.single_node_scheduler.enabled` setting.

Release Notes: scheduled jobs scheduler now runs on a single node by default
in order to reduce contention on scheduled jobs table.

74077: kvserver: lease transfer in JOINT configuration r=shralex a=shralex

Previously:
1. Removing a leaseholder was not allowed.
2. A VOTER_INCOMING node wasn't able to accept the lease.

Because of (1), users needed to transfer the lease before removing
the leaseholder. Because of (2), when relocating a range from the
leaseholder A to a new node B, there was no possibility to transfer
the lease to B before it was fully added as VOTER. Adding it as a
voter, however, could degrade fault tolerance. For example, if A
and B are in region R1, C in region R2 and D in R3, and we had
(A, C, D), and now adding B to the cluster to replace A results in
the intermediate configuration (A, B, C, D) the failure of R1 would
make the cluster unavailable since no quorum can be established.
Since B can't be added before A is removed, the system would
transfer the lease out to C, remove A and add B, and then transfer
the lease again to B. This resulted a temporary migration of leases
out of their preferred region, imbalance of lease count and degraded
performance.

The PR fixes this, by (1) allowing removing the leaseholder, and
transferring the lease right before we exit the JOINT config. And (2),
allowing a VOTER_INCOMING to accept the lease.

Release note (performance improvement): Fixes a limitation which meant 
that, upon adding a new node to the cluster, lease counts among existing
nodes could diverge until the new node was fully upreplicated.

Here are a few experiments that demonstrate the benefit of the feature.
1. 
> roachprod create local -n 4 // if not already created and staged
> roachprod put local cockroach
> roachprod start local:1-3 --racks=3 // add 3 servers in 3 different racks
> cockroach workload init kv --splits=10000
> roachprod start local:4 --racks=3 // add a 4th server in one of the racks

Without the change (master):
<img width="978" alt="Screen Shot 2022-02-09 at 8 35 35 AM" src="https://user-images.githubusercontent.com/6037719/153458966-609dbb7e-ca3d-4db6-9cfb-adc228f2bdf2.png">

With the change:
<img width="986" alt="Screen Shot 2022-02-08 at 8 46 41 PM" src="https://user-images.githubusercontent.com/6037719/153459366-2d4e2def-37cf-405b-b601-8be57419ae02.png">

We can see that without the patch the number of leases on server 0 (black line) goes all the way to 0 before it goes back up and that the number of leases in other racks goes up, both undesirable. With the patch both things are no longer happening.

2. Same as 1, but with a leaseholder preference of rack 0:

ALTER RANGE default CONFIGURE ZONE USING lease_preferences='[[+rack=0]]';

Without the change (master):
<img width="966" alt="Screen Shot 2022-02-09 at 10 45 27 PM" src="https://user-images.githubusercontent.com/6037719/153460753-bce048f0-f6da-4e21-afdc-317620c035b2.png">

With the change:
<img width="983" alt="leaseholder preferences - with change" src="https://user-images.githubusercontent.com/6037719/153460780-55795866-cf47-404d-b77a-45d9e011f972.png">

We can see that without the change the number of leaseholders in racks 1 and 2 together (not in preferred region) grows from 300 to 1000, then goes back to 40. With the fix it doesn’t grow at all.






76401: pgwire: add server.max_connections public cluster setting r=rafiss a=ecwall

This setting specifies a maximum number of connections that a server can have open at any given time.
<0 - Connections are unlimited (existing behavior)
=0 - Connections are disabled
>0 - Connections are limited
If a new non-superuser connection would exceed this limit, the same error message is
returned as postgres: "sorry, too many connections" with the 53300 error code
that corresponds to "too many connections".

Release note (ops change): An off-by-default server.max_connections cluster
setting has been added to limit the maximum number of connections to a server.

76748: sql: add missing specs to plan diagrams r=rharding6373 a=rharding6373

This change allows missing specs (e.g., RestoreDataSpec and
SplitAndScatterSpec) to be shown in plan diagrams. Before this change a
plan involving these types would result in an error generating the
diagrams. Also added a test to make sure future specs implement the
`diagramCellType` interface, which is required to generate diagrams.

Release note: None


Co-authored-by: Casper <casper@cockroachlabs.com>
Co-authored-by: Yevgeniy Miretskiy <yevgeniy@cockroachlabs.com>
Co-authored-by: shralex <shralex@gmail.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: rharding6373 <rharding6373@users.noreply.github.com>

---
## [elan-ev/tobira](https://github.com/elan-ev/tobira)@[d961e0d934...](https://github.com/elan-ev/tobira/commit/d961e0d9345b0785171c7f6018596d45f12668eb)
#### Tuesday 2022-02-22 15:47:36 by Lukas Kalbertodt

Improve design of user info in header for logged-in users

On mobile, the icon changed to have a user with a green checkmark next
to it, better indicating that the user is logged in. On desktop, that
icon is also shown with the text "logged in as: <name>" left of it. The
text and the icon both make the user menu appear.

This is better than the previous version in my opinion. For one, I think
it looks fresher. But more importantly, the user name being in this
button box was weird, and the user menu touching that button then is
also weird. Since the user box was limited in size, but the size of the
menu was independent, it would often be a size mismatch which looked
really ugly. I don't think the original design was fixable, really.
That's why I implemented this now.

---
## [AppStateESS/triptrack](https://github.com/AppStateESS/triptrack)@[511c49c8b5...](https://github.com/AppStateESS/triptrack/commit/511c49c8b58f433e1f9262901856f3ab29f67730)
#### Tuesday 2022-02-22 18:42:03 by Matt McNaney

please travis-ci devil gods. see my offering of blood to your deployment demon and may it satisfy their hunger

---
## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[dfeff2051a...](https://github.com/kleinesfilmroellchen/serenity/commit/dfeff2051ae0e1a06c42f1757ea874b895d47473)
#### Tuesday 2022-02-22 19:24:34 by kleines Filmröllchen

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

Known issues/exposed bugs:
- Two processes running audio enqueues at the same time will pin the CPU
  at 100% due to both of them yield()ing all the time. See #12679.
- AudioServer hangs in driver after changing sample rate. (Probably
  already an issue before these changes.)
- SoundPlayer's BarsVisualization doesn't draw anything until you switch
  to another visualization and back again.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [johnkim-det/determined](https://github.com/johnkim-det/determined)@[08888717a6...](https://github.com/johnkim-det/determined/commit/08888717a6db21304115cd119ebb5d926d51c88e)
#### Tuesday 2022-02-22 20:00:03 by Bradley Laney

feat: unify task logs [DET-6062, DET-6063, DET-6064, DET-6065, DET-6066] (#3070)

This change adds persistent logs for all task types (well, all except poor old checkpoint GC). This means that logs are written to the logging back-end as configured in the master (PostgreSQL through master or Elastic) by Fluentbit and accessible through APIs in the master that translate reads to the back-end's language. To allow for this change, many other changes were required. A (probably) non-exhaustive list follows:
* Trial logs used to go to a `trial_logs` table or index. I tried to not tear the codebase asunder forever with trials and the others using different tables/queries/structs/etc everywhere. Existing tasks were marked has having `log_version == 0` and the old `trial_logs` table now serves logs those tasks (only trials). From now on, all tasks are written with `log_version == 1` and queries for their logs are routed to the `task_logs` table. The old trial logs table (now the `log_version == 0` table) is mothballed - it (mostly) shouldn't be touched again and the old logs should load from there fine forever while new features can be built on the new table. There were alternatives besides leaving trials and task logs separate forever that I shied away from; e.g., I considered a migration to update the trial logs table to schema of the task logs table, but since we access task logs by task_id, this would require rewriting the index on trial_id or adding one on task_id which is too expensive for a migration. This solution balances complexity, maintainability and migration cost.
* Because task logs went through the master, we were free to built features like readiness checks on top of them. Now that they don't, before logs leave the container a small helper script skims them, checks for the readiness logs and posts readiness to a new API. I considered alternatives here, too, like reading the logs back in on the master side, but that incurs a lot more overhead I felt this was more flexible anyway.
* The old events endpoint used to return logs, now it doesn't. This was because it (the eventManager that backed the endpoint) used to _store_ the logs, and now it doesn’t. In my opinion, the work to read the log stream and the old event stream and merge them is low value and annoying. Users should just prefer the new `/api/v1/tasks/:id/logs` endpoint for logs and rely on events to get the few task events that were relied on. Events will likely be supplanted by a task state watcher of some time so webui/cli can just watch for the readiness bit to flip.

---
## [15peaces/15-3athena](https://github.com/15peaces/15-3athena)@[bdff59e6ee...](https://github.com/15peaces/15-3athena/commit/bdff59e6eeb3bfe3f641f8882a179ab5f41b9e20)
#### Tuesday 2022-02-22 20:54:47 by 15peaces

== Some 3ceam merges ==
=General:
*Merged missing changes from 3ceam rev. 794 - 795

*Added the "skillfailmsg" command.
-Its a debug command for testing skill fail messages.

*Added support for homunculus spirit spheres.
-This is needed for future updates for Eleanor's skills.
-Note: Officially the spirit sphere's are supposed to last for 600 seconds (10 minutes) for each one, but due to techanical issues I gave up and decided to not have any timers on them for now.
-This makes them last forever until the homunculus dies, is vaporized, player logs out, or the spheres are used by skills.
-Honestly, I don't think anyone will care.

*Added 2 new state checks.
-ST_FIGHTER is used to check if a homunculus is in fighter mode.
-ST_GRAPPLER is used to check if a homunculus is in grappler mode.
-These state checks are used for Eleanor's skills.

*clif_hom_spiritball_single
*clif_hom_spiritball
*merc_hom_addspiritball
*merc_hom_delspiritball
-Added these functions.

*clif_hom_skillupdateinfo
-Added this function as needed to make it possible to combo the skill Sonic Claw after Midnight Frenzy.

*Its now possible for homunculus skills to have cooldowns.
-Cooldown's for homunculus skills are not saved on logout since its not really needed.

*Cleaned up some code.

*Eleanor
-Can now generate spirit sphere's when the Style Change skill is learned. A max of 10 sphere's can be gained and each one adds +3 ATK to the homunculus damage.
-All of Eleanor's offensive skills now check if she's in fighter or grappler mode.

=Skills:
*SR_DRAGONCOMBO
-Made it easier to start a combo.
-Basicly, using this skill will no longer stop your character's normal attacking which allows you to combo after use. But you have to be in the middle of normal attacking when used for it to work. Its not 100% official but its the best I can do.

*MH_STYLE_CHANGE
-Added full support.

*MH_SONIC_CRAW
-Updated damage formula.
-Removed variable cast.
-Added cooldown.
-The number of hits it deals is now affected by the number of sphere's the homunculus has when casted.
-Can now be comboed after Midnight Frenzy.
-Note: The aftercast change is unofficial but when looking at the ones for the grapple skills and the amount of time you get to combo Silvervein Rush after Sonic Claw's aftercast, its clearly stupid to have a 1 second aftercast. A cooldown clearly
-does the job better for a combo skill.

*MH_CBC
-Corrected timer settings to prepare for future support.

*MH_STAHL_HORN
-Fixed a issue where the skill didn't apply a duration for stun.

*MH_SILVERVEIN_RUSH
*MH_MIDNIGHT_FRENZY
-Added support for these skills.

---
## [mbabigian/Stockfish](https://github.com/mbabigian/Stockfish)@[cb9c2594fc...](https://github.com/mbabigian/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Tuesday 2022-02-22 22:16:38 by Tomasz Sobczyk

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
## [projects-nexus/android_kernel_xiaomi_sm8250](https://github.com/projects-nexus/android_kernel_xiaomi_sm8250)@[b57c865f88...](https://github.com/projects-nexus/android_kernel_xiaomi_sm8250/commit/b57c865f88859073081c3dfe3e2c10d762ba8cb0)
#### Tuesday 2022-02-22 22:32:37 by George Spelvin

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
## [MarcelRaschke/react](https://github.com/MarcelRaschke/react)@[c7b4497988...](https://github.com/MarcelRaschke/react/commit/c7b4497988e81606f1c7686434f55a49342c9efc)
#### Tuesday 2022-02-22 23:53:23 by Andrew Clark

[Experiment] Lazily propagate context changes (#20890)

* Move context comparison to consumer

In the lazy context implementation, not all context changes are
propagated from the provider, so we can't rely on the propagation alone
to mark the consumer as dirty. The consumer needs to compare to the
previous value, like we do for state and context.

I added a `memoizedValue` field to the context dependency type. Then in
the consumer, we iterate over the current dependencies to see if
something changed. We only do this iteration after props and state has
already bailed out, so it's a relatively uncommon path, except at the
root of a changed subtree. Alternatively, we could move these
comparisons into `readContext`, but that's a much hotter path, so I
think this is an appropriate trade off.

* [Experiment] Lazily propagate context changes

When a context provider changes, we scan the tree for matching consumers
and mark them as dirty so that we know they have pending work. This
prevents us from bailing out if, say, an intermediate wrapper is
memoized.

Currently, we propagate these changes eagerly, at the provider.

However, in many cases, we would have ended up visiting the consumer
nodes anyway, as part of the normal render traversal, because there's no
memoized node in between that bails out.

We can save CPU cycles by propagating changes only when we hit a
memoized component — so, instead of propagating eagerly at the provider,
we propagate lazily if or when something bails out.

Most of our bailout logic is centralized in
`bailoutOnAlreadyFinishedWork`, so this ended up being not that
difficult to implement correctly.

There are some exceptions: Suspense and Offscreen. Those are special
because they sometimes defer the rendering of their children to a
completely separate render cycle. In those cases, we must take extra
care to propagate *all* the context changes, not just the first one.

I'm pleasantly surprised at how little I needed to change in this
initial implementation. I was worried I'd have to use the reconciler
fork, but I ended up being able to wrap all my changes in a regular
feature flag. So, we could run an experiment in parallel to our other
ones.

I do consider this a risky rollout overall because of the potential for
subtle semantic deviations. However, the model is simple enough that I
don't expect us to have trouble fixing regressions if or when they arise
during internal dogfooding.

---

This is largely based on [RFC#118](https://github.com/reactjs/rfcs/pull/118),
by @gnoff. I did deviate in some of the implementation details, though.

The main one is how I chose to track context changes. Instead of storing
a dirty flag on the stack, I added a `memoizedValue` field to the
context dependency object. Then, to check if something has changed, the
consumer compares the new context value to the old (memoized) one.

This is necessary because of Suspense and Offscreen — those components
defer work from one render into a later one. When the subtree continues
rendering, the stack from the previous render is no longer available.
But the memoized values on the dependencies list are. This requires a
bit more work when a consumer bails out, but nothing considerable, and
there are ways we could optimize it even further. Conceptually, this
model is really appealing, since it matches how our other features
"reactively" detect changes — `useMemo`, `useEffect`,
`getDerivedStateFromProps`, the built-in cache, and so on.

I also intentionally dropped support for
`unstable_calculateChangedBits`. We're planning to remove this API
anyway before the next major release, in favor of context selectors.
It's an unstable feature that we never advertised; I don't think it's
seen much adoption.

Co-Authored-By: Josh Story <jcs.gnoff@gmail.com>

* Propagate all contexts in single pass

Instead of propagating the tree once per changed context, we can check
all the contexts in a single propagation. This inverts the two loops so
that the faster loop (O(numberOfContexts)) is inside the more expensive
loop (O(numberOfFibers * avgContextDepsPerFiber)).

This adds a bit of overhead to the case where only a single context
changes because you have to unwrap the context from the array. I'm also
unsure if this will hurt cache locality.

Co-Authored-By: Josh Story <jcs.gnoff@gmail.com>

* Stop propagating at nearest dependency match

Because we now propagate all context providers in a single traversal, we
can defer context propagation to a subtree without losing information
about which context providers we're deferring — it's all of them.

Theoretically, this is a big optimization because it means we'll never
propagate to any tree that has work scheduled on it, nor will we ever
propagate the same tree twice.

There's an awkward case related to bailing out of the siblings of a
context consumer. Because those siblings don't bail out until after
they've already entered the begin phase, we have to do extra work to
make sure they don't unecessarily propagate context again. We could
avoid this by adding an earlier bailout for sibling nodes, something
we've discussed in the past. We should consider this during the next
refactor of the fiber tree structure.

Co-Authored-By: Josh Story <jcs.gnoff@gmail.com>

* Mark trees that need propagation in readContext

Instead of storing matched context consumers in a Set, we can mark
when a consumer receives an update inside `readContext`.

I hesistated to put anything in this function because it's such a hot
path, but so are bail outs. Fortunately, we only need to set this flag
once, the first time a context is read. So I think it's a reasonable
trade off.

In exchange, propagation is faster because we no longer need to
accumulate a Set of matched consumers, and fiber bailouts are faster
because we don't need to consult that Set. And the code is simpler.

Co-authored-by: Josh Story <jcs.gnoff@gmail.com>

---
## [Noah6544/Pygame_Spaceship_Game](https://github.com/Noah6544/Pygame_Spaceship_Game)@[f82e7bc24f...](https://github.com/Noah6544/Pygame_Spaceship_Game/commit/f82e7bc24f57617442bf9477051b9c78838716a0)
#### Tuesday 2022-02-22 23:56:16 by Noah Buchanan

Created Hitboxes/Collisions system and more!

Been putting off updating this for some time because I was having trouble with the pygame.rect object and the pygame.Rect.colliderect functions. I thought that it was above what I was able to do but it was extremely easy and pretty fast. Lesson learned: Always try  before giving up, and before you give up, make sure you know why. Don't just "ah I can't do this" instead, make sure its something more like, "I can't get this done because I don't know how to work with parent and child inheritance classes and I don't have time right now. Don't give up when you're frustrated, chances are, you're about to hit gold.

--
integrated the new inheritance class was a ton easier than i thought it was going to be. super function is a life-saver, just the other day i was looking at it thinking I wasn't going to use it until im wayy more experiences, but wow. 
---
integrated new collisions with rectangle objects and have them reset positions on collisions, will continue to buildup the bare bones of the program then polish this minigame. I will then make a UI menu to select minigames

---

