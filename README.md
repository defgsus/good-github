## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-06](docs/good-messages/2022/2022-08-06.md)


1,538,069 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,538,069 were push events containing 2,102,167 commit messages that amount to 127,349,927 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [ZAB909/40K-Eipharius](https://github.com/ZAB909/40K-Eipharius)@[5993bf1051...](https://github.com/ZAB909/40K-Eipharius/commit/5993bf10514cda880474211ad1f57eb367c0ec0e)
#### Saturday 2022-08-06 00:02:53 by Vanderlin

Power Sword Nerf

Holy fuck the original stats were the equiv of holding the power of a neutron star in your hand. It literally instantly kills an Astartes in one hit. Instant death. It also has 100 percent chance of decap every time even if you wear power armor.

I had to kill that shit fast.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b4f19a7e0f...](https://github.com/tgstation/tgstation/commit/b4f19a7e0fc3802856ec4117eb71418287c51ac6)
#### Saturday 2022-08-06 00:03:01 by John Willard

Greatly increases Pun Pun's abilities and strengths (using desk bells, cross stun immunity) (#68870)


About The Pull Request

Pun Pun has a new AI, with it they received the following:

    Instead of screeching/roaring/scratching/jumping/rolling, Pun Pun will instead sing/dance/bow/clear throat/sign.
    Pun Pun now rings desk bells instead of finding random shit to pick up, and doesn't intentionally seek out weapons.
    Pun Pun has a higher chance of giving people stuff in their hand, so the Bartender can give them a drink and let them go walking around.

Additionally:

    Pun Pun is now immune to being hardstunned by walking into them, giving them a little more bite for greytiders beating them up.
    Monkeys can now use desk bells.

Why It's Good For The Game

I like Pun Pun and when Monkey AIs were originally added, there was a note about giving them a unique AI. Since we're slowly turning the poor monkey into an actual Bartender assistant, I find it thematic that they would ring the bell and give out drinks in their hand, as if the Bartender taught them themselves.

For the hardstun immunity, I mostly did it because I find it annoying for a Bartender to have to carefully navigate around Pun Pun to not knock them over and make them drop an instrument (or anything else) in their hand, but it also works as a buff to people trying to kill them. Pun pun is a unique monkey so I don't believe they should be as easy to kill as any other.

Desk bell addition was necessary for Pun Pun to use it.
Changelog

cl
add: Pun Pun now gives stuff in their hand frequently and rings desk bells.
add: Pun Pun now has gentleman-like emotes, rather than screeching and roaring.
balance: Pun Pun no longer looks for weapons in their off time.
balance: Pun Pun is no longer vulnerable to stuns by being walked into.
qol: Monkeys can now use desk bells.
/cl

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[5dc17bd865...](https://github.com/Shadow-Quill/tgstation/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Saturday 2022-08-06 00:33:08 by san7890

Security's Scaling Departmental Accesses - More Pop, More Problems (#68534)

lternative to #68527
About The Pull Request

Hey there,

This is an alternative PR that I concocted based on talking with Goof on that PR. Basically, we already have a nicely complicated system to track and balance the number of security officers we have in a shift based on some config coefficient setting, by which we can set the amount of lockers that spawn in on the start of a round, as well as determine truly how many security officers we have.

image

So, I've decided to leverage this in another way. Basically, based on the number of security officers in a shift, their specific departmental officers will also get more (elevated) accesses. They already start with a certain amount of access, but they can get more if it is a low-pop shift with the mechanic introduced in this PR. For example, an Engineering Security Officer can access Atmospherics and Engineering departments by default, but they can't access Telecommunications unless there is a lower population of players AT SHIFT START. Same for a Medical Security Officer accessing Medbay, but not Plumbing.

Update: I have made it such that there are three system that server operators can set:

They can use the Scaling System that operates in the same method outlined in the rest of the PR.
They can disable giving departmental security officers "elevated access" (such as access beyond the "front doors") to these officers.
Finally, they can also just always ensure that departmental security officers get the maximal accesses possible.

The default setting is the "Scaling System" outlined in this PR, which is already dependent on the general Security Officer Scaling Co-Efficient.
Why It's Good For The Game

I think it's better to involve some more nuanced config scaling that we already have present in the game. The major theme that we want to avoid is that departmental security officers having maximal accesses when there is an already large number of persons on the security force will result in "miserable" shifts for the common person working within a department (security metaprotections). However, some server operators (as well as server cultures) tend to have very wide ranges in how many security officers they have on a shift-by-shift basis. One day, you could have 0-2 security officers, the next, you could have 4-6. It's all variable on who's playing (as always). There is also a significant variation between server to server in regards to how many security officer slots you tend to have on spawn, but this is already manageable by the security officer co-efficient in config.

I believe this PR is an acceptable proposal within the bounds of #68527 (comment) , although it may bend certain aspects of it, I definitely do see where some people may be coming from. I believe I've adjusted the accesses to a "sane"/justifiable amount, but I'll come back to think on everything.

"Red-tiding" may or may not be a problem, but there's always just going to be something inherently silly with a security officer being able to walk into plumbing to start plumbing. I hoped that this would be seen as a positive as opposed to a negative, but I can see how it could negatively impact player experience. HOWEVER, interplayer experience should not be handled by the codebase in all aspects, which is why I've also passed in the associated config variables, so that server operators (who should handle the interplayer experience with their level of discretion and nuance) can.
What accesses are where?

The general philosophy as I thought through designing this would be that the security officer should at the very least have general "front-door" access into a department, and maybe something benign. If we had even more per-door accesses, this could definitely be a bit more granular (one example I can think of would only atmospherics technicians having access to the "Pump Room", while Security Officers would not. However, this is for a later date). So, you have the "default" access you always get, and a potential to get "elevated" access as a Departmental Security Officer.

The balances are as such:

The Cargo Security Officer will have access to the Cargo Bay, Mining Section, and the Shipping Room. The first two are rather general areas, with the Shipping Room being a rather good help for rescuing (or "rescuing") flushed crewmembers when the cargo techies can't get to it/no AI. The Auxiliary Base is not essential to the security officer's functions, and the mining station helps restrict access further on stations like IceBox. This would also grant them extra access to the Lavaland base, so let's snip that out.

The Engineering Security Officer should have access to only general Engineering and Atmospherics. Construction pertains to certain rooms in maintenance I believe, and Engine-Equipment should be the one that grants access to APCs (lol). I don't think a security officer should have the latter one to be honest, but I think we'll be stretching the scope of this PR. Telecommunications is a bit weird, it's a critical station function, but I think you also shouldn't be able to nick one goon's ID and have access, so let's give it to them only when it's "needed".

The Medical Security Officer should have access to only the general Medbay Area and the Morgue, in case someone starts trotting on the doctor's turf, or if there's someone doing unsavory things to the bodies while the doctors are away. They will not have access to the specialized (dangerous) areas unless the ratio of secoffs to the population is low enough should it necessitate it (Plumbing Room, Pharmacy, Virology). I also added Surgery to the scaling access, but I'm iffy on that one. I don't particularly see why they should have it as a base access, but I also do see there being some need in dire straits (in relation to helping people, not tiding).

The Science Security Officer definitely got a huge cut. They now only have general access to R&D and normal scientist areas like the lathe room, circuits lab (presumably)since these are generally trafficked areas, but I definitely clamped down on additional access they might get in a "normally balanced" situation (no ordnance+storage, no xenobio, no genetics, no to robotics, etc.) They don't have a particular use in these areas and can even be a bit obstructive to flow in normal circumstances, but if abnormal circumstances arise and there's not a lot of security hands-on-deck, then their access is expanded.

Honestly, balancing this both makes sense and is conversely rather odd. I'm just running off what we already hold to be true and expected (or at least as of the last two months), and we can go from there.
Changelog

cl
balance: Nanotrasen realized that the more access they had on their cards was costing them a pretty penny, so they trimmed back the number of accesses a certain departmental Security Guard might have. However, any given guard will get back a greater amount of accesses depending on how many security guards there are in relation to the population.
config: Hey server operators, listen! We've changed up how Departmental Security Officers get their accesses, so be sure to review the DEPSEC_ACCESS_LEVEL config number to see what you want to work best for your server.
/cl

Also, every single line of code found in 4533f07 that is now presently in this PR is deliberate

---
## [eun0115/android_kernel_samsung_universal7904](https://github.com/eun0115/android_kernel_samsung_universal7904)@[3adbd81d01...](https://github.com/eun0115/android_kernel_samsung_universal7904/commit/3adbd81d01b75fa0a7d36ba286030764833d93cc)
#### Saturday 2022-08-06 00:42:54 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [CptNoHand/qb-vehiclekeys](https://github.com/CptNoHand/qb-vehiclekeys)@[757fdd0859...](https://github.com/CptNoHand/qb-vehiclekeys/commit/757fdd0859013e45f9d432fa894f0ecb03d8bbf5)
#### Saturday 2022-08-06 01:04:29 by ItsANoBrainer

Proper Refactor

Refactored the entire resource because the key system was not working.

No longer does a server callback 10 or so times a second, on top of other bad practices.

Tested pretty much everything with my devs, but there might be some weird issues we havnt found. Please lookover as I've been going crazy with the small tedious issues I've come across doing this.

Throwing this up to get feedback, and for people to use who want it.

Features:

- Keys are saved server side, and sent to each client when they are added or removed, as well as on character selection. This allows characters to leave and come back in the same server uptime session and still have the same keys
- Keys are only pulled from the server once on character load
- Giving keys has 3 types, /givekeys with an id will attempt to give keys you have to an id, not including an id will try to give it to the closest person, and if you're in a vehicle it will give to everyone
- Can only give keys to vehicles you have keys to
- Server event to force acquire keys to a plate for a person (for lockpicking/stealing/spawning, etc.)
- Can Carjack an NPC with a gun, has different percentages to work based on weapon (config)
- Take keys from dead npc drivers
- Can lockpick a car to unlock the doors
- Can hotwire a car if you're in the driver seat of the vehicle you dont have keys to to get keys
- Keeps the engine of a vehicle off if you dont have keys to it (allows other resources to attempt to toggle car engine without needing to interface if you have keys or not)
- Vehicle blacklist system for vehicles you dont want to be lockable (always unlocked)
- Police Alerts from lockpicking/hotwiring/carjacking
- Export to check if you have keys to a vehicle
- Locking/unlocking with hotkey
- Locking/unlocking and giving keys uses a custom GetVehicleInDirection you are facing for realism/accuracy
- Fully compatible with old resource. Has an event handler for 'vehiclekeys:client:SetOwner' in which it gives keys for that plate
- Some other shit I probably forgot

TODO:
- Add LOCALE support
- Stop peds from wanting to get back into the vehicle they just got carjacked out of as they're fleeing

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[6fe0683a7b...](https://github.com/Pickle-Coding/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Saturday 2022-08-06 01:18:41 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[b15331b4df...](https://github.com/Paxilmaniac/Skyrat-tg/commit/b15331b4df9bd525ba80b284beb3442f180c01be)
#### Saturday 2022-08-06 01:40:11 by OrionTheFox

[MANUAL MIRROR] The GAGening: Clothesmate edition [MDB IGNORE] (#15100)

* The GAGening: Clothesmate edition

* ThisShouldWork

* hgnbhg

* would probably help to have the right .dmi

* fixed?

* Fuck you

Co-authored-by: Twaticus <46540570+Twaticus@users.noreply.github.com>

---
## [stungkit/cadence-client](https://github.com/stungkit/cadence-client)@[f5e0fd25e4...](https://github.com/stungkit/cadence-client/commit/f5e0fd25e4347c85b28dac87f51b532700455d2c)
#### Saturday 2022-08-06 02:23:41 by Steven L

Sharing one of my favorite "scopes" in intellij, and making it easier to add more (#1182)

Goland is nice, and the type-based navigation is wildly superior to gopls-driven
stuff in my experience, so I tend to lean hard on it when I'm able.

By default though, Goland searches *everything*.  All the time.
That's totally reasonable as a default, but we can do better:

- Tests are not usually all that interesting when trying to understand and navigate code.
  (perhaps they should be, but that's more a platonic ideal than a reality)
- Generated RPC code is almost never useful to dive into.  The exposed API surface is sufficient,
  if it compiles, it's correct.
- Non-Go files are just less interesting in a Go project.

So this scope excludes ^ all that.
To add more shared ones, just check the "share through vcs" box and commit it.

To use it, just select the scope from the dropdown when you search.  E.g. "find in files" ->
change from "in project" to "scope" -> change the dropdown.  This custom scope will now appear,
and it'll remember what you last used, so it's a nice default.

This also works in "call hierarchy", "go to implementations" (open it in a panel to configure it,
with the gear on the side.  it's awful UI but it works), etc quite a lot of places.

This same kinda-obtuse search-scope query language can be used to mark things as generated or test
related, which will also help other parts of the IDE mark things as more or less relevant for you.
It's worth exploring a bit, scopes and filters can be used to do a lot: https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html

---
## [mccormick-wooden/terminal](https://github.com/mccormick-wooden/terminal)@[9ccd6ecd74...](https://github.com/mccormick-wooden/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Saturday 2022-08-06 02:58:29 by Mike Griese

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
## [denreychristy/fibonacci](https://github.com/denreychristy/fibonacci)@[883f83d2cf...](https://github.com/denreychristy/fibonacci/commit/883f83d2cfb7c39cb5d1c0cace20533f74f0f016)
#### Saturday 2022-08-06 04:03:47 by Denrey Christy

trying some other stupid shit to get this dumb mother fucker to work god damn it

---
## [OpheliaXI/AirSkyBoat](https://github.com/OpheliaXI/AirSkyBoat)@[6ec1eb725a...](https://github.com/OpheliaXI/AirSkyBoat/commit/6ec1eb725a01dd48b56436c37abffe85d2d8fcdd)
#### Saturday 2022-08-06 04:23:43 by Abdiah

Operation Desert Swarm Implementation (#253)

* Operation Desert Storm

Evidence:
https://ffxiclopedia.fandom.com/wiki/Operation_Desert_Swarm

- Removed Adaman ingot from drop tables as sample rate contained 1/288
- Removed Mythril ingot with drop rate 0%
- Added battlefield mob type to the platoon scorpions
- Increased sword strap drop rate from 2.2% to 22% as seen in wiki

* ODS early work

* Operation Desert Swarm Full fix

Co-authored-by: OpheliaXI <heliashelium@gmail.com>

Changes:

Fixed crash that would occur when all scorpions were alive and wild rage was used
Fixed bug that caused scorpions to infinitely loop when using abilities
Corrected Wild Rage damage to scale as they die. Damage will start from ~350 and reach ~650. Extensive testing was done on this part
Fixed proper messaging from scorpions to display that they do not have enough energy to attack while on mimic cooldown - which is set to 7 seconds after the scorpions mimic one another
Scorpions will only be bound as msg IDs suggest scorpions only getting stuck and not stunned. Furthermore the crash that was earlier fixed was due to stun being applied to the scorpion

* sleep res build

Added sleep and lullaby build resistance as scorpions die
Evidence:
https://ffxiclopedia.fandom.com/wiki/Operation_Desert_Swarm#:~:text=They%20cannot%20be%20feasibly%20slept%20after%20the%203rd%20or%204th%20Sleep.%20Their%20Sleep%20resistance%20increases%20drastically%20when%20only%20few%20of%20them%20are%20left.%20Bind%20and%20Gravity%20are%20suggested.

* Death fix

Added iskiller to on mob death to prevent multiple looping for each member in the battlefield

---
## [BakaKaito/Mergebot.NET](https://github.com/BakaKaito/Mergebot.NET)@[addf27fd16...](https://github.com/BakaKaito/Mergebot.NET/commit/addf27fd1688c4785202b53177d7fa84069d9bed)
#### Saturday 2022-08-06 05:45:15 by Koi

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
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[f098ecc264...](https://github.com/kleinerm/Psychtoolbox-3/commit/f098ecc264b24fea7c377f64bf83354bba74a20e)
#### Saturday 2022-08-06 06:06:31 by Mario Kleiner

PsychLinuxConfiguration: Add workarounds for RaspberryPi OS 11 Mesa v3d.

Testing after upgrading the RPi 400 to Raspbian 11 showed new trouble:

At least on Mesa's gallium v3d driver for the RPi 4/400's VideoCore 6
gpu, Raspbian 11 Bullseye, page-flipping is broken by default - again.
Pageflipping for fullscreen OpenGL PTB onscreen windows fails, with
error messages flooding the XOrg log, and the copyswap fallback causes
PTB timing failures and horrible tearing.

The RPi desktop GUI composited by the Mutter X11 desktop compositor
doesn't have that problem, because Mesa for Raspbian 11 was patched
with some out-of-tree downstream patches to accept a new secret
parameter "v3d_maintain_ignorable_scanout" that if set to true allows
to fix pageflipping, but defaults to false == broken. God knows why
"broken by default" was considered an appropriate config choice, but
here we are...

Reference link to the patch series, which is not to be found anywhere
else with a Google search, and not yet in Mesa main upstream:

https://gitlab.freedesktop.org/mesa/mesa/-/issues/6079
https://github.com/bluestang2006/Debian-Pkgs/tree/master/mesa/debian/patches

This adds the magic parameter to fix pageflipping for octave + PTB
to the deep color config file and updates PsychLinuxConfiguration to
always force-install/update that file on ARM systems. I'm too lazy
to add extra config files and revalidate stuff, so we stuff it into
an unrelated Mesa config file.

This should fix PTB on RPi OS 11 on RPi 4/400.

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[6a48b66f86...](https://github.com/Offroaders123/NBT-Parser/commit/6a48b66f860dfa925ea671299fbeb106d2811474)
#### Saturday 2022-08-06 08:41:57 by Offroaders123

"Final" Declarations: Part Two

Changes:
- Woah, finally got the type definitions working, both local imports, *and* NPM ones!!! Super happy with this. I even found an experimental way to dynamically load an ES Module from either an NPM module resolution, or a CDN url. That hasn't been battle tested yet, but it's idea is really straightforward and concise.
- My discovery is that TypeScript can actually auto-detect an adjacent `d.ts` file by default, so keeping everything in the same directory allows it to be picked up automatically.
- I debugged my definition files by making a demo TS-only version of the library, and checking the output of the `d.ts` files to see how it would export them, and it uses more `declare` statements than I was using. It also wasn't using `declare module`, so I removed that syntax again. This means that the import for the module won't have a specific type, but you can see it's exports perfectly!
- Because of how the types are loaded now, each module file no longer needs an `@type` import, as it is added from the top-level `index.d.ts` instead.
- This is the perfect setup, I love it! I get the benefits of typings for my library, but I don't have to transpile from TypeScript to JS, I don't have to transpile Node to browser, it doesn't need to be bundled, and it can run directly from GitHub, using JSDelivr :O
- Once these changes are part of the main branch, and I've updated the APIs a bit more, I will definitely make some docs in the README for how to use this, as it is extremely versatile now!
- While I do think it may be a hinderance to try and stay all vanilla JS in the larger development world, I personally like it a ton, as everything I am authoring is directly written by hand. I think it's cool to open DevTools and see exactly what you wrote in your editor. No things to reverse engineer or try to compare. This is a rather less-common opinion, as it seems that so many projects go the framework/library/tooling route, and maybe I just haven't gotten to that point yet. I think without a doubt I will get to that point eventually, it's likely just a matter of time and experience. But as a relatively newer programmer out here, it kind of appears like everyone hops on the bandwagon of new technologies all of the time. That's probably just a tech-related thing in general, so it doesn't take me by surprise or anything. I think it's definitely great to know about the latest and greatest things out there, as having broad knowledge of what options are out there is a great thing to have. I also feel it's important that you know how to not reinvent the wheel too though. That seems to be the case with some things out there. On that same hand though, modern vanilla JS has without a doubt helped make the wheel a lot nicer though. It's not like this kind of setup has been a viable option for a long time, so who am I to think anything of it? I'm not sure, haha. But that's it I guess? You can take that as a grain of salt, or as a new idea, totally up to you :)
- Sorry for the crazy rant, these are really fun to write at least! This is just my off the top of my brain perspective at the moment with the tools that are available to me in the web dev world as it is right now, being a younger programmer (in experience terms).

Ok, and here's a link about `noEmit`, which is essentially decsribing that I'm only using my TypeScript files for type checking, rather than transpilation:
https://stackoverflow.com/questions/55002137/typescript-noemit-use-case

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[83c79b48cd...](https://github.com/Offroaders123/NBT-Parser/commit/83c79b48cde8b27e99b3ef5ab869684d9d45ef32)
#### Saturday 2022-08-06 09:31:44 by Offroaders123

"Final" Declarations: Part Two

Changes:
- Woah, finally got the type definitions working, both local imports, *and* NPM ones!!! Super happy with this. I even found an experimental way to dynamically load an ES Module from either an NPM module resolution, or a CDN url. That hasn't been battle tested yet, but it's idea is really straightforward and concise.
- My discovery is that TypeScript can actually auto-detect an adjacent `d.ts` file by default, so keeping everything in the same directory allows it to be picked up automatically.
- I debugged my definition files by making a demo TS-only version of the library, and checking the output of the `d.ts` files to see how it would export them, and it uses more `declare` statements than I was using. It also wasn't using `declare module`, so I removed that syntax again. This means that the import for the module won't have a specific type, but you can see it's exports perfectly!
- Updated some of the parameter destructuring type formatting to match how it is formatted when transpiled with `tsc`, which uses semicolons instead of commas like an object would. Interestingly, it looks like it supprorts either syntax, not sure why. Guess it's not so strict in this instance, hehe.
- I also incremented the version number for the library, as this is a bit set of changes in these last few releases. The commits from before here until the previous version increment haven't been pushed to the repo yet, so I didn't increment the version number for them. I jumped to `0.6.0` though since a lot of the library's structure has moved around.
- Because of how the types are loaded now, each module file no longer needs an `@type` import, as it is added from the top-level `index.d.ts` instead.
- This is the perfect setup, I love it! I get the benefits of typings for my library, but I don't have to transpile from TypeScript to JS, I don't have to transpile Node to browser, it doesn't need to be bundled, and it can run directly from GitHub, using JSDelivr :O
- Once these changes are part of the main branch, and I've updated the APIs a bit more, I will definitely make some docs in the README for how to use this, as it is extremely versatile now!
- While I do think it may be a hinderance to try and stay all vanilla JS in the larger development world, I personally like it a ton, as everything I am authoring is directly written by hand. I think it's cool to open DevTools and see exactly what you wrote in your editor. No things to reverse engineer or try to compare. This is a rather less-common opinion, as it seems that so many projects go the framework/library/tooling route, and maybe I just haven't gotten to that point yet. I think without a doubt I will get to that point eventually, it's likely just a matter of time and experience. But as a relatively newer programmer out here, it kind of appears like everyone hops on the bandwagon of new technologies all of the time. That's probably just a tech-related thing in general, so it doesn't take me by surprise or anything. I think it's definitely great to know about the latest and greatest things out there, as having broad knowledge of what options are out there is a great thing to have. I also feel it's important that you know how to not reinvent the wheel too though. That seems to be the case with some things out there. On that same hand though, modern vanilla JS has without a doubt helped make the wheel a lot nicer though. It's not like this kind of setup has been a viable option for a long time, so who am I to think anything of it? I'm not sure, haha. But that's it I guess? You can take that as a grain of salt, or as a new idea, totally up to you :)
- Sorry for the crazy rant, these are really fun to write at least! This is just my off the top of my brain perspective at the moment with the tools that are available to me in the web dev world as it is right now, being a younger programmer (in experience terms).

Ok, and here's a link about `noEmit`, which is essentially decsribing that I'm only using my TypeScript files for type checking, rather than transpilation:
https://stackoverflow.com/questions/55002137/typescript-noemit-use-case

---
## [srsbsns5/GAN-GDDS1](https://github.com/srsbsns5/GAN-GDDS1)@[d5113aa21a...](https://github.com/srsbsns5/GAN-GDDS1/commit/d5113aa21a330d5dc6bf716cdba88b8e42c20cc5)
#### Saturday 2022-08-06 09:46:33 by Greg

Humble beginnings of a credit scene

Ooh
You can dance
You can jive
Having the time of your life
Ooh, see that girl
Watch that scene
Digging the dancing queen
Friday night and the lights are low
Looking out for a place to go
Where they play the right music
Getting in the swing
You come to look for a king
Anybody could be that guy
Night is young and the music's high
With a bit of rock music
Everything is fine
You're in the mood for a dance
And when you get the chance
You are the dancing queen
Young and sweet
Only seventeen
Dancing queen
Feel the beat from the tambourine, oh yeah
You can dance
You can jive
Having the time of your life
Ooh, see that girl
Watch that scene
Digging the dancing queen
You're a teaser, you turn 'em on
Leave 'em burning and then you're gone
Looking out for another
Anyone will do
You're in the mood for a dance
And when you get the chance
You are the dancing queen
Young and sweet
Only seventeen
Dancing queen
Feel the beat from the tambourine, oh yeah
You can dance
You can jive
Having the time of your life
Ooh, see that girl
Watch that scene
Digging the dancing queen
Digging the dancing queen

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[33f7351d68...](https://github.com/fc1943s/The-Spiral-Language/commit/33f7351d685483f0d2a821b8352fb3cfd781dfdf)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"10:50am. When I go to bed late I sleep better, but I also get up late as well. Based on how tired I was, I thought it would be 9-10am, but it is nearly 11.

10:55am. Agh, who is going to start now? Let me chill for a while, have breakfast, do the chores and then I will put in the work that is needed. The last thing I feel like doing now is rushing.

12:30pm. Let me start.

12:35pm. Let me gather my bearings.

```fs
    let buffer = Dictionary()
    let last_id = ref 0
    use __ = server.ReceiveReady.Subscribe(fun s ->
        let rec loop () = Utils.remove buffer !last_id (body(NetMQMessage 3)) id
        and body (msg : NetMQMessage) (address : NetMQFrame, x) =
```

Let me get rid of the message ordering. This made sense to me before - it would be the case that 1 or 2 out of 10 times during startup, the semantic token request would arrive before the file open and that would wreck things. But now this optimization is preventing the server from being usable by multiple instances. Let me deal with this.

I'll just remove it. Then I will fix the semantic token get so request that go out of range do not cause an out of bounds exception. That should do the trick.

12:40pm. Let me just do this. I'll get lost in thought at this rate.

```fs
let token_range (r_par : ParserRes) ((a,b) : VSCRange) =
    let from, near_to = min (r_par.lines.Length-1) a.line, min r_par.lines.Length (b.line+1)
    vscode_tokens from near_to r_par.lines
```

Removing that buffer was easy. This is where the token range is gotten.

12:50pm.

```fs
let token_range (r_par : ParserRes) ((a,b) : VSCRange) =
    let from = a.line |> min (r_par.lines.Length-1) |> max 0
    let near_to = b.line |> min r_par.lines.Length |> max 0
    vscode_tokens from near_to r_par.lines
```

I thought I did no affordances, but I think that what I had before was mostly right...

No, this is not right somehow...

```fs
let token_range (r_par : ParserRes) ((a,b) : VSCRange) =
    let from = a.line |> min r_par.lines.Length
    let near_to = b.line |> min r_par.lines.Length
    vscode_tokens from near_to r_par.lines
```

Yeah, this is the way to do it.

That -1 was not the right reasoning. When done like this, I'd get at minimum a range of 1. Instead ranges could be zero as well. Even worse, they could set the from to -1.

```fs
let token_range (r_par : ParserRes) ((a,b) : VSCRange) =
    let in_range x = min r_par.lines.Length x
    vscode_tokens (in_range a.line) (in_range b.line) r_par.lines
```

Let me do it like this.

12:55pm. Now what I need to do next is adjust the request code so it does not send the message id.

That will be easy.

```ts
const request = async (file: object): Promise<any> => {
    const sock = new zmq.Request()
    sock.connect(uriServer)
    await sock.send(JSON.stringify(file))
    const [x] = await sock.receive()
    return JSON.parse(x.toString())
}
```

Piece of cake. Let me try running this.

Can't forget to publish the new thing first...

1:05pm. Things work great now.

Let me implement heart beating next.

After that I'll be ready for publication on the VS Code marketplace, but one thing that makes me uncofmortable currently is how large the .NET compiled code is. All those .dlls take megabytes of size.

Would it be possible to bundle that down similarly to the JS code? There should be a way to do it.

1:10pm. Focus me. Let me deal with heart beating first.

```
const spiPingReq = async (): Promise<void> => request({ Ping: true })
```

Here is the request.

1:15pm.

```ts
    (async () => {

    })();
```

Right now I am thinking how to do this kind of loop.

1:25pm.

```ts
    const pingLater = (time : number) => {
        const f = () => {
            if (isProcessing) {spiPingReq(); pingLater(time)}
        }
        setTimeout(f, time)
    }
    pingLater(1000)
```

Let me go with this. Now let me implement things on the F# side.

1:30pm.

```fs
    let mutable time = DateTimeOffset.Now
    let timer = NetMQTimer(2000)
    poller.Add(timer)
    timer.EnableAndReset()
    use __ = timer.Elapsed.Subscribe(fun _ ->
        if TimeSpan.FromSeconds(2.0) < DateTimeOffset.Now - time then poller.Stop()
        )

    use __ = server.ReceiveReady.Subscribe(fun s ->
        let msg = server.ReceiveMultipartMessage(3)
        let address = msg.Pop()
        msg.Pop() |> ignore
        let x = Json.deserialize(Text.Encoding.Default.GetString(msg.Pop().Buffer))
        let push_back (x : obj) =
            match x with
            | :? Option<string> as x ->
                match x with
                | None -> msg.Push("null")
                | Some x -> msg.Push(sprintf "\"%s\"" x)
            | _ -> msg.Push(Json.serialize x)
            msg.PushEmptyFrame(); msg.Push(address)
        let send_back x = push_back x; server.SendMultipartMessage(msg)
        let send_back_via_queue x = push_back x; queue_server.Enqueue(msg)
        let job_null job = Hopac.start job; send_back null
        let job_val job = let res = IVar() in Hopac.start (job res >>=. IVar.read res >>- send_back_via_queue)
        match x with
        | ProjectFileOpen x -> job_null (supervisor *<+ SupervisorReq.ProjectFileOpen x)
        | ProjectFileChange x -> job_null (supervisor *<+ SupervisorReq.ProjectFileChange x)
        | ProjectFileDelete x -> job_null (supervisor *<+ SupervisorReq.ProjectFileDelete x)
        | ProjectCodeActionExecute x -> job_val (fun res -> supervisor *<+ SupervisorReq.ProjectCodeActionExecute(x,res))
        | ProjectFileLinks x -> job_val (fun res -> supervisor *<+ SupervisorReq.ProjectFileLinks(x,res))
        | ProjectCodeActions x -> job_val (fun res -> supervisor *<+ SupervisorReq.ProjectCodeActions(x,res))
        | FileOpen x -> job_null (supervisor *<+ SupervisorReq.FileOpen x)
        | FileChange x -> job_null (supervisor *<+ SupervisorReq.FileChange x)
        | FileDelete x -> job_null (supervisor *<+ SupervisorReq.FileDelete x)
        | FileTokenRange x -> job_val (fun res -> supervisor *<+ SupervisorReq.FileTokenRange(x,res))
        | HoverAt x -> job_val (fun res -> supervisor *<+ SupervisorReq.HoverAt(x,res))
        | BuildFile x -> job_null (supervisor *<+ SupervisorReq.BuildFile x)
        | Ping _ -> send_back null
        time <- DateTimeOffset.Now
        )
```

This should do the trick. Let me compile this and then I will try it out.

1:35pm. It works. I did it.

Everything is set. I only need to figure out how to compile Spiral a bit better now and I will be ready to push out version `2.0.0`.

What does that Pack under the build options do?

```
Build started...
1>------ Build started: Project: The Spiral Language 2, Configuration: Debug Any CPU ------
1>The Spiral Language 2 -> C:\Users\Marko\Source\Repos\The Spiral Language\The Spiral Language 2\bin\Debug\netcoreapp3.1\Spiral.dll
1>Successfully created package 'C:\Users\Marko\Source\Repos\The Spiral Language\The Spiral Language 2\bin\Debug\Spiral.1.0.0.nupkg'.
========== Build: 1 succeeded, 0 failed, 0 up-to-date, 0 skipped ==========
```

It creates a nuget package. I see.

And it is only 886kb.

Still, this is not something I can put into the plugin.

Unpacked the compiler is 12mb.

https://docs.microsoft.com/en-us/aspnet/mvc/overview/performance/bundling-and-minification

https://ianqvist.blogspot.com/2018/01/reducing-size-of-self-contained-net.html

Google is not giving me what I want directly.

Ok, I should at least try to do trimming.

1:50pm. https://128bit.io/post/ahead-of-time-compilation-with-net-core/

This is actually pretty interesting.

```
dotnet publish -r win-x64 -c release /p:PublishSingleFile=true /p:PublishTrimmed=true
```

This is a different command that the one used with the Trimming package. What should I use?

1:55pm. I am not sure what I should do here. I am thinking whether I should try the above. But just having the sized squeezed down for a single platform is no good for me. I want it to be portable like now.

I need to do more research on this. Let me watch the video in that link. Ideally I'd find a way to do AOT compilation for all the platforms. Excluding that, I want to figure out the right way to do trimming.

2pm. https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-publish

> We recommend that you specify this option in a publish profile rather than on the command line. For more information, see MSBuild.

There are a bunch of interesting options here.

2:05pm.

```
<?xml version="1.0" encoding="utf-8"?>
<!--
https://go.microsoft.com/fwlink/?LinkID=208121.
-->
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup>
    <Configuration>Release</Configuration>
    <Platform>Any CPU</Platform>
    <PublishDir>..\VS Code Plugin\compiler</PublishDir>
    <PublishProtocol>FileSystem</PublishProtocol>
    <TargetFramework>netcoreapp3.1</TargetFramework>
    <SelfContained>false</SelfContained>
  </PropertyGroup>
</Project>
```

I see the the publish command uses this profile that I created. I've decided that I do not need the Trimming package since the compilation options exists for that in the .NET Core 3.0 and up.

https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/visual-studio-publish-profiles?view=aspnetcore-5.0

```
/p:<NAME>=<VALUE>
```

Ah, so this is what it means. That `/:p` is literally setting the property to some value.

```
    <PublishSingleFile>true</PublishSingleFile>
    <PublishTrimmed>true</PublishTrimmed>
```

I've added this into the pubxml. Let me try publishing it again. But before that...

Ok, the compiler is 12.3mb now. I've erased it by hand. Let me see what comes out next.

```
Build started...
1>------ Publish started: Project: The Spiral Language 2, Configuration: Release Any CPU ------
1>It is not supported to publish an application to a single-file without specifying a RuntimeIdentifier. You must either specify a RuntimeIdentifier or set PublishSingleFile to false.
========== Build: 0 succeeded, 0 failed, 1 up-to-date, 0 skipped ==========
========== Publish: 0 succeeded, 1 failed, 0 skipped ==========
```

Ah, I see.

https://docs.microsoft.com/en-us/dotnet/core/deploying/ready-to-run

What is R2R? Let me read that and then I will try that instead.

> However, R2R binaries are larger because they contain both intermediate language (IL) code, which is still needed for some scenarios, and the native version of the same code.

No this is not good. Forget it. Let me just do trimming then. I'll have to be satisfied with that.

```
Build started...
1>------ Publish started: Project: The Spiral Language 2, Configuration: Release Any CPU ------
1>The Spiral Language 2 -> C:\Users\Marko\Source\Repos\The Spiral Language\The Spiral Language 2\bin\Release\netcoreapp3.1\Spiral.dll
1>Optimizing assemblies for size is not supported for the selected publish configuration. Please ensure that you are publishing a self-contained app.
========== Build: 0 succeeded, 0 failed, 1 up-to-date, 0 skipped ==========
========== Publish: 0 succeeded, 1 failed, 0 skipped ==========
```

Ok, let me try it self contained then.

Ah, I see, once I turn on self contained, I do get the options to optimize in the IDE.

But now I cannot compile things protably anymore.

I give up. I can either chose size or portability, not both. I'll go with the later then.

2:20pm. And it is time to publish on the marketplace. Let me turn off the shell.

Why is taking so long to run the extension host now all of a sudden?

2:25pm.

```ts
    const compiler_path = path.join(__dirname,"../compiler/Spiral.exe")
    const compiler_path_for_shell = `"${compiler_path}"`
    const p = cp.spawn(compiler_path,{shell: false, detached: true})
```

How complicated. The shell and the regular spawn require different paths.

Ok, let me package this. Then I will publish it.

...Hmmm, no, I need to get rid of the source maps. They just waste 100kb.

I have no idea. Disabling them in the tsconfig file just saves 30kb. It still produces the source maps.

```
devtool: 'source-map',
```

Let me comment out this in the webpack config file.

Yeah, that does the trick. Ok.

2:30pm. Let me publish it. Right now the plugin is 4.3mb large.

...No I am not happy with this. Let me bring in the trim package after all.

https://ianqvist.blogspot.com/2018/01/reducing-size-of-self-contained-net.html

From this post I mean.

```
Build started...
1>------ Build started: Project: The Spiral Language 2, Configuration: Release Any CPU ------
1>The Spiral Language 2 -> C:\Users\Marko\Source\Repos\The Spiral Language\The Spiral Language 2\bin\Release\netcoreapp3.1\Spiral.dll
2>------ Publish started: Project: The Spiral Language 2, Configuration: Release Any CPU ------
2>Trimmed 1 out of 16 files for a saving of 0 MB
2>Final app size is 7.48 MB
2>The Spiral Language 2 -> C:\Users\Marko\Source\Repos\The Spiral Language\The Spiral Language 2\bin\Release\netcoreapp3.1\Spiral.dll
2>Trimmed 0 out of 1 files for a saving of 0 MB
2>Final app size is 2.63 MB
2>The Spiral Language 2 -> C:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin\compiler\
========== Build: 1 succeeded, 0 failed, 0 up-to-date, 0 skipped ==========
========== Publish: 1 succeeded, 0 failed, 0 skipped ==========
```

Useless. Nevermind.

Actually, this thing here is pretty much the ideal use case for why you want a language with partial evaluation. If this were Spiral, the end executable would be miniscule in comparison.

I haven't even thought about compilation sizes before, but seeing what .NET is giving me is making me realize I should highlight this benefit of Spiral in the future.

Let me get rid of that package. It is not useful to me.

Let me move to publication.

2:40pm. Done. Right now it is doing verification. That will take a while, but I'll get an email when it is done.

2:45pm. Let me take a break here. Oh, it has been verified. Let me try installing the plugin.

...Done. I see that the title is messed up. Also it does not point to the front page. Nevermind that for now. Let me try running some files.

2:50pm. It is not working. Nothing is showing up. I fear that the plugin is not being activated.

Ahhhhhhhhhh...Note how now I am compiling into `dist`. But the package still has the main as being in out. Damn.

I need to think about this.

Focus me, put the Iron Ladies aside. I'll get back into the fray.

First, let me take this opportunity to fix the auxilaries first. The title of the plugin shows up as `spiral-lang-vscode`.

```json
 "name": "spiral-lang-vscode",
 "displayName": "The Spiral Language",
 "readme": "../readme.md",
```

I am not sure that this is how to fix the readme. Let me take a look at the publishing the plugin page again.

2:55pm.

> A README.md file at the root of your extension will be used to populate the extension's Marketplace page's contents. vsce will modify README links for you in two different ways:

How awkward.

3:05pm.

```
Activating extension 'mrakgr.spiral-lang-vscode' failed: No native build was found for platform=win32 arch=x64 runtime=electron abi=80 uv=1 libc=glibc.
```

I get this error when I try to run the extension. Nevermind this. First of all, let me see if the changes I did to the package file did anything.

```
 "readme": "../readme.md",
 "license": "../LICENSE",
```

I doubt the packager will smart enough to fetch there, but it could work.

3:05pm. Let me try uploading it without the compiler. I just want to see if the readme trick works.

While I wait for it to get verified, let me investigate why I can't run the thing in dist.

3:15pm. Damn it, this is some weird webpack related error.

https://stackoverflow.com/questions/59275743/local-native-node-module-causes-error-uncaught-error-no-native-build-was-found

Not this...

> Since you are using webpack in the repository you provided. I've been doing research into this issue, it appears that webpack can cause problems with __dirname. Some native node modules require __dirname to work properly inorder for them to use the native code. (In my case leveldown is the module in question). I am actively looking into a fix on the webpack side of things. I will post the results to my findings once completed.

https://github.com/webpack/webpack/issues/

There is stuff in issue 1599.

```
// the webpack config just works
target: 'node',
node: {
  __dirname: false,
  __filename: false,
}
```

Weird hacks are what I need to do here. Let me try it.

```
Activating extension 'mrakgr.spiral-lang-vscode' failed: No native build was found for platform=win32 arch=x64 runtime=electron abi=80 uv=1 libc=glibc.
```

No, it fails.

...Am I sure that the problem is the `__dirname` for me? Let me just try it out with a direct path.

```
    // const compiler_path = path.join(__dirname,"../compiler/Spiral.exe")
    // const compiler_path_for_shell = `"${compiler_path}"`
    // const p = cp.spawn(compiler_path,{shell: false, detached: true})
```

Actually, let me comment this out.

The same error. This is not it. I am barking up the wrong tree here.

```
 "readme": "../readme.md",
 "license": "../LICENSE",
```

I checked the uploaded plugin. It is useless. I am going to have to configure MSbuild so it copies the readme and the license into the plugin directory.

In fact, why don't I just put a link into the readme to the online repo instead of copying it?

3:30pm. I decided to go with that. That is the easiest way. I do not want multiple copies of the same readme floating around. It is better to use a link instead.

As for the license, it is not like that will be changing from here on out, so I can afford to keep a copy.

Ok, now that leave only the issue of Webpack not working correctly.

I only have to resolve this and then I will be done. Let me take a short break.

4pm. The short break took a while.

But I did come to some conclusions.

```
 "scripts": {
  "vscode:prepublish": "webpack --mode production",
  "webpack": "webpack --mode development",
  "webpack-dev": "webpack --mode development --watch",
  "test-compile": "tsc -p ./"
 },
```

Most likely what vsce is using is `"vscode:prepublish": "webpack --mode production"` in order to run the script. What I should try right now are some of Webpack's competitors rather than try to debug the crummy thing.

https://code.visualstudio.com/api/working-with-extensions/bundling-extension

This mentions Parcel and Rollup. Let me take a look at them.

https://rollupjs.org/guide/en/

Ok, let me aim for this. How do I use this with TS?

https://www.npmjs.com/package/rollup-plugin-typescript2

What a pain in the ass. Well, let me give it a try.

4:15pm.

```
C:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin>rollup -c

src/index.ts → dist/index.js...
[!] Error: Incompatible tsconfig option. Module resolves to 'CommonJS'. This is incompatible with rollup, please use 'module: "ES2015"' or 'module: "ESNext"'.
Error: Incompatible tsconfig option. Module resolves to 'CommonJS'. This is incompatible with rollup, please use 'module: "ES2015"' or 'module: "ESNext"'.
    at checkTsConfig (C:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin\node_modules\rollup-plugin-typescript2\dist\rollup-plugin-typescript2.cjs.js:25094:15)
    at parseTsConfig (C:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin\node_modules\rollup-plugin-typescript2\dist\rollup-plugin-typescript2.cjs.js:25125:5)
    at Object.options (C:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin\node_modules\rollup-plugin-typescript2\dist\rollup-plugin-typescript2.cjs.js:29177:73)
    at C:\Users\Marko\AppData\Roaming\npm\node_modules\rollup\dist\shared\rollup.js:19997:36
```

At least I am getting sane errors here. Will changing the module type break anything?

I remember having trouble because of that in the past, but the details escape me.

```
import * as zmq from "zeromq"
```

Now this is giving me an error.

4:25pm. This goes away when I set the module resolution to node. Great. Now I can in fact use the newer and more elegant module system.

But rollup is not actually doing any minification so far. How to do I get it to do that.

```
import { terser } from 'rollup-plugin-terser';
```

Ohhhh, now it is refusing to find this module!

Uahhh....

This is two days wasted on this shit - it is roughly what I expected of JS.

...I accidentally installed it globally. Nevermind. Now it finally does its thing.

4:40pm. Let me get rid of the lodash dependency since I am not using it.

4:45pm. Ok, I cleaned things up. Now everything should work. For some reason though the extension host takes forever to start.

4:50pm.

```
  {
   "type": "typescript",
   "tsconfig": "tsconfig.json",
   "problemMatcher": [
    "$tsc"
   ],
   "group": "build",
   "label": "tsc: build - tsconfig.json"
  },
```

Damn, in order to make a rollup launcher I need to run it somehow. But I do not know how to do the task for it.

Aghhhh...

What the hell is a problem matcher?

```
  {
   "type": "shell",
   "command": "npm run vscode:prepublish",
   "group": "build",
   "label": "rollup build"
  }
```

Maybe like this. I am letting the autocomplete guide me here. And I am getting errors when I make a mistake. Otherwise these scripts would be completely inaccessible for me.

Let me give this a try.

5pm.

```
"main": "dist/index.js",
```

This thing is giving me trouble. I have no idea how to use tsc watch and rollup side by side.

5pm. Now I can't use the tsc compiled plugins properly. It is telling me that it cannot use the import statements outside of a module. I remember getting similar kinds of errors before. The rollup version works fine though.

I guess I'll move to using TSC + rollup somehow. I don't really need the incremental compilation and the watching capability of TSC.

https://github.com/rollup/rollup-starter-app/blob/master/package.json

Rollup however does have the watching uption.

```
  "vscode:prepublish": "rollup -c",
  "build": "rollup -c",
  "watch": "rollup -c -w"
```

I'd want to find a way to pass in the flag so I can avoid doing the minifaction when I am not prepublishing.

```
// rollup.config.js
import typescript from 'rollup-plugin-typescript2';
import { terser } from 'rollup-plugin-terser';

const production = !process.env.ROLLUP_WATCH;

export default {
    input: 'src/index.ts',
    output: {
        file: 'dist/index.js',
        format: 'cjs'
    },

    plugins: [
        typescript(),
        production && terser()
    ]
}
```

Ah, so it is like this. Yeah, this makes sense.

```
  {
   "type": "typescript",
   "tsconfig": "tsconfig.json",
   "option": "watch",
   "problemMatcher": [
    "$tsc-watch"
   ],
   "group": "build",
   "label": "tsc: watch - tsconfig.json"
  },
  {
   "type": "typescript",
   "tsconfig": "tsconfig.json",
   "problemMatcher": [
    "$tsc"
   ],
   "group": "build",
   "label": "tsc: build - tsconfig.json"
  },
```

Let me take these tasks out.

The only thing I am worried about is that this might start multiple rollup watches.

```
{
 "version": "2.0.0",
 "tasks": [
  {
   "type": "shell",
   "command": "npm run vscode:prepublish",
   "group": "build",
   "label": "rollup build"
  },
  {
   "type": "shell",
   "command": "npm run watch",
   "group": "build",
   "label": "rollup watch"
  }
 ]
}
```

I have no idea. Let me just try first.

...Running rollup watch from the shell is blocking the extension host from starting. Not good.

```
       {
            "label": "Build extension",
            "type": "npm",
            "script": "build",
            "presentation": {
                "reveal": "silent"
            }
        }
```

There is an `npm` type?

5:20pm.

```
external: ["vscode","path","child_process"],
```

This gets rid of the external dependency warnings. Good.

I gave up on getting the pre launch task to work. From here on out, whenever I am working on the plugin I'll have to remember to `npm run watch` first. What a pain in the ass.

But at the very least, I have TS with the latest module system working now. Plus rollup's minification does work nicely.

It squeezes it down to 8kb from about 12mb. I really need this, I can't have the users download the unminified thing. I wish I could get the compiler down further, but there is no helping it now. One option would be to provide multiple versions for each of the OS as separate packages, but that would be too much of a burden for me.

5:30pm. Let me put the compiler in the right place so I can see if this works.

```
> spiral-lang-vscode@2.0.2 vscode:prepublish C:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin
> rollup -c

src/index.ts → dist/index.js...
(node:5780) ExperimentalWarning: Conditional exports is an experimental feature. This feature could change at any time
(!) Unresolved dependencies
https://rollupjs.org/guide/en/#warning-treating-module-as-external-dependency
zeromq (imported by src\index.ts)
created dist/index.js in 1.9s
Publishing mrakgr.spiral-lang-vscode@2.0.2...
 INFO  Extension URL (might take a few minutes): https://marketplace.visualstudio.com/items?itemName=mrakgr.spiral-lang-vscode
 INFO  Hub URL: https://marketplace.visualstudio.com/manage/publishers/mrakgr/extensions/spiral-lang-vscode/hub
 DONE  Published mrakgr.spiral-lang-vscode@2.0.2.
```

I decided to publish, but why am I getting an unresolved dependency error here? This is not supposed to happen.

https://github.com/rollup/plugins/tree/master/packages/node-resolve

It seems I need to resolve it. It is recommending I use this.

```
src/index.ts → dist/index.js...
(node:6544) ExperimentalWarning: Conditional exports is an experimental feature. This feature could change at any time
[!] (plugin rpt2) Error: C:/Users/Marko/Source/Repos/The Spiral Language/VS Code Plugin/src/index.ts(128,20): semantic error TS2354: This syntax requires an imported helper but module 'tslib' cannot be found.
```

Seriously - fuck Javascript. That are my honest feelings right now.

5:40pm. I got tslib as a dev dependency.

https://rollupjs.org/guide/en/#error-name-is-not-exported-by-module

Now I get this error in several places.

> It can be solved by using the namedExports option, which allows you to manually fill in the information gaps.

There is a link to `namedExports` in there, except it is dead and points to nothing.

5:45pm. I give up. I am throwing in the towel on minimization. Each user will simply have to get 12 extra megabytes of unused libraries every time he downloads the plugin.

I can't deal with this shit. I already wasted an entire day. Let me restore the tasks to their original setting.

6pm. Right now I am waiting for 2.0.3 to finish verifying. Then I'll download it and try it out. Assuming it works I will be done for the day. I expect it to work.

6:10pm. Yeah, it works.

Back while I was redoing the semantic token ranges I accidentally intro'd a bug.

```fs
let token_range (r_par : ParserRes) ((a,b) : VSCRange) =
    let in_range x = min r_par.lines.Length x
    vscode_tokens (in_range a.line) (in_range (b.line+1)) r_par.lines
```

This should be +1 like this.

6:15pm. Now it works.

The 2.0.4 works as it should. Now the plugin is installed and I can start random Spiral projects in it.

The whole sordid affair with Webpack and Rollup I will just sweep under the rug. To a lesser extent, the same goes for the .NET compiler. I'll forget my grudges here and just go with the sytem I've established today.

It is lunch time.

6:55pm. Done with lunch. I am so emotionally drained by this point. I am definitely going to close here, but let me put in the last few words for the day.

Thanks to today's work, the Spiral language is now published on the VS Code marketplace. I really brought up the schedule for this to a surprising extent. I even amazed myself.

And on the plus side, with this I am absolutely done with editor support. Now the plugin can start the compiler on its own in the background and the process has the ability to close on its own. And the language is published and the compilation pipeline is established. I will never have to go through the hastle of the last two days again.

7:05pm. The next thing to do for the next few weeks is to just keep filling out the documentation.

Hmmm...a thought comes to me. My writting is always filled with typos and grammar errors. I wonder in DL technology is good enough to serve as an editor? I should look into that. I need to put my paragraphs through stringent tests. It would be bad if I write 200 pages only to give the impression of illiteracy.

The important thing is to keep going. Doing the documentation will also give me the chance to more thoroughly test the language as I go. I maybe tested 30% of the surface area of the language so far. There is plenty of room for errors to lurk in. The work on the documentation will force me to systematically cover all of the language's features.

7:10pm. Soon I will be in business. The next review will definitely have something out of the ordinary."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[6b997a4e48...](https://github.com/fc1943s/The-Spiral-Language/commit/6b997a4e4863f70a9edbb08b8862eb51f4881a1a)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"11:20am. The new year is here. I spent 2020 learning concurrency and then using it in the creation of Spiral v2. This year, I am going to spend programming in it.

11:25am. Let me chill for a while and then I will start.

11:30am. Actually, let me have breakfast and do the chores here. I do not have time to do anything in the morning session. I really slept well tonight.

1:45pm. Let me finally start. First, let me post the review on the Simulacrum blog. I will just put it through a spell checker first. It is really a chore to the do the PL sub review, this, plus this journal, but I'll keep it up unless it starts giving me trouble.

2pm.

///

[Spiral v2](https://github.com/mrakgr/The-Spiral-Language) is out on the VS Code marketplace. Installing the language is as simple as installing the plugin from the extensions tab. It is still in testing phase, and it should have been for a few months more, but I decided to not be timid, and pushed forward the release. My plan right now is to keep fixing the bugs while I do the docs.

Even though I say that, the language is not in a poor shape at all, so feel free to give it a try. By the time January is over both the documentation and the language should be in good shape.

It has been a long time getting to this point. I spent the entire year 2020 on making it happen. Every design mistake from v0.09 has been amended, and the language has a cool, new top-down type system to take the edge off the partial evaluation magic that it does.

After January is done, I intend to finally put my plans into action. In 2018, I put in a lot of effort on making a GPU-based deep learning library using the original Spiral. In 2021 I will do the same thing except much better. I will make use of the language as wedge to get me through the door of [various hardware companies](https://cacm.acm.org/magazines/2020/8/246356-neuromorphic-chips-take-shape/fulltext). Getting them to sponsor me is one aspect of the plan, but the main purpose of the expedition will be to get a handle on these devices and make sure I am continually at bleeding edge of the hardware wave from here on out.

Though I could not accomplish my main goal 2018 which was making a good RL agent, the ML library itself was in my view fairly impressive - I manage to create a fully optimized RNN (similar to the one in the [Nvidia blog post](https://developer.nvidia.com/blog/optimizing-recurrent-neural-networks-cudnn-5/)) and used it as a model in a policy gradient training of a poker agent whose game implemented alongside it. I had to automate serialization between language barriers, and the game's data types and something the NNs could process. In order to implement optimized GPU kernels such as the one in the blog post, I had to implement automatic differentiation on GPU itself. All the technical achievements were not accomplished simply by gritting my teeth and dropping down to the low level, but through innovative high level abstractions. For example, GEMM fusion from that blog post is made much easier by having tensors with named dimensions.

This is the usual habit in my programming - I solve a task, I generalize the solution and then reuse the abstractions elsewhere. The language one is using makes a vital difference - that library and all those optimizations would have been impossibly difficult to do in C for example.

I made some mistakes too. When it comes to making a GPU library, it turns out that .NET's GC is really a poor fit for managing GPU memory. I'd have been better off picking Python as a target platform. Towards the end of 2018 the old Spiral's poor design and implementation made the compile times go up drastically. And having to do type inference programmatically was really an anchor around my neck.

I can go on about my regrets, but even if it weren't for all of those, I do not think I could have accomplished my goal. Towards the end of 2018, I realized one thing - though GPUs are the workhorse of deep learning, they are actually a very poor fit of reinforcement learning. I spent a long time bashing my head how to improve the performance of RL algorithms. I blasted backpropagation. At some point understanding will dawn, but until then I've realized that what I should do is make do with poor algorithms.

Maybe backprop is a poor fit, but the reality is that the task of reinforcement learning is particularly difficult. In 2018 I've challenged myself to improve a single model and got nowhere. Instead of doing that, in 2021 I will take advantage of new hardware to master ensembles.

In 2018, I would train a model, and would get wildly different results depending on random seeds. It is an open secret that RL researchers cherry-pick their results. Instead of getting mad at that, what I have to do is formalize that insight. If training a single model is all up to luck, why not train a 100 of them in a single go?

GPUs are actually a very poor fit for that. They are good for quickly processing batches of data through a single model, but doing something like passing a single vector of data through numerous networks would be the worst case fit for them. It will be different for [neurochips](https://www.youtube.com/watch?v=jhQgElvtb1s). The new language will allow me deal with the hardware, and the hardware will allow me to complete the agents that I could not a few years ago.

Well, that is the plan for when I am done with the docs I plan on striking out and getting in contact with hardware companies themselves when I am ready. If somebody from the hardware side is reading this and is interested having a Spiral backend and an ML library for it please do get in touch.

---

(Continued from the PL monthly sub post.)

If this plan works, I will be able to solve my poverty woes in one fell swoop. The paper I linked says there are 50 startups, so there are plenty of potential sponsors for my services. I plan to price the rental space in the Spiral ecosystem for these companies at 3k per month. Assuming the sponsor is interested in having a permanent backend and library to the point of paying for it, this is the price point that I think will make it rational for the companies to just cash out to me instead of hiring another programmer to fork Spiral and maintain that. Maybe I could go for more, but I will curb my greed and resist trying to squeeze the other parties. Maximizing money is not that important, I want to get through this next part peacefully.

Since the market is ripe, I am hoping to get a bunch of them and build up my monthly income that way.

In Croatia, the average salary is a bit over 1k per month. Local dev salaries are higher than the average, but it is not a rich region by any means. Even just getting single sponsor would put me way above average. And I've been without money for long enough, so I am determined to make this work. I need to get access to chips anyway - instead of paying for them years down the road, isn't it better that I get others to pay me to program them today? I really do need to explore the offerings anyway, I don't have a view on which specific piece will be dominant yet. It would be a mistake to pick one and stick with it; at this point I do need variety.

Unlike v0.09 which was researchy kind of language, and whose libraries I've written in F# strings, v2 has way higher quality across the board, so I am confident on about the quality of my offering.

Still, it is not like my past schemes were successful. But to be fair they were pretty crazy.

This has a fairly rational chance of working out, but I don't have the experience nor the knowledge to tell how things will go. I should be able to convince the leads to take a look at Spiral, but whether the companies will be willing to pay depends on the level of the people working there. I expect them to be mostly using Python + C as their hardware stack. This should have a large amount of friction that Spiral could alleviate, but who knows, maybe the guys there will be the kind that likes C.

I have no idea what the general programmer level of the C crowd is, but there are plenty 'lol GC bad' kiddies there. They are not exactly innovative. If the guys I keep running into don't see a point to a language having first class functions, that will make any kind of negotiations untenable. The ideal team would be the one that has positive experience with other functional programming languages. I can imagine those kinds of people really being impressed with Spiral.

But even though functional programming is in ascendance, it is not mainstream by any means. So if I run into a team like that, it will more likely be an exception than the rule. I might end up being forced to take whatever opportunity I can get.

I can do a good job on Spiral, and I can try to tailor my message, but beyond that things are out of my hands. I'll do my best and let the dice land where they may.

If this were all about money, trying to make a poker agent, let alone a language would make zero sense.

It is not that crushing [these guys](https://www.esportsearnings.com/) would be satisfying monetarily. It is just I can't imagine a successful Singularity run that does not go through that path. Could there exist a programmer too weak to beat online gaming, but strong enough to conquer the universe? I doubt it. Gaming success is as much of a sanity check as it is an opportunity to make money along the way.

When I decided to make Spiral, I set on out on my own path. I really expected there would be more people than just me working on a language to make an ML library. Because I know back then that down the road new hardware will come out, and Theano, Tensorflow - whatever was popular at the time would be scrapped. The hardware companies would not have Google level resources to make those kinds of compilers. Even if they do take the effort to integrate with popular frameworks, what will happen if deep learning gets superseded by new algorithms?

Furthermore, deep learning is not so difficult as to necessitate such huge software investments that Google and Facebook are making. I could not make a GPU library in F#, but it was doable in Spiral v0.09 and it will be easy in v2.

I do feel a certain sense of loneliness that what I expected did not come to pass, but in the software world the isolation I endure today will be competitive moat tomorrow.

It is difficult. In games you command the player character and the action gets executed. If only my own mind had the same kind of calm attitude and disposition that my proxies do. My own mind requires deep planning and elaborate beliefs to embark on a course of action. The action requires effort, but establishing motivation requires just as much effort. It is tiresome.

Do I have anything better to do than programming in this life? No. If I could go back in time 15 years ago, I'd command myself to do programming. If I could get an extra 15 years of work today for free, just how much further along would I be? It is unimaginable.

I can't change the past, so this time I'll be smarter and give this gift to the me of the future. For a person of a sinister character such as myself, programming is a fitting punishment.

Every day I gather inspiration, then I try to manifest it as code. I manifest it as writing. I gather inspiration and let it loose letting my hands act out the office of the mind after that.

This inspiration is an invisible power that I have to contain in raw matter. Otherwise it would escape.

Yet even though I keep doing this exercise, I haven't attained even a bit of what I want yet. I have no intention of stopping.

I will find my dream again, at the end of the human era.

///

LanguageTools are good, but they fucked up my formatting. Now I have to fix it by hand. Just how is it inserting those newlines?

Furthermore, deep learning is not so difficult as to necessitate such huge software investments that Google and Facebook are making.

2:10pm.

```fs
let s =  "Furthermore, deep learning is not so difficult as to necessitate such huge software investments that Google and Facebook are making."
let s' = "Furthermore, deep learning is not so difficult as to necessitate such huge software investments that Google and Facebook are making."

let x = s.ToCharArray()
let x' = s'.ToCharArray()
Array.iteri2 (fun i x x' ->
    if x <> x' then printfn "at %i, %i <> %i" i (int x) (int x')
    ) x x'
```

This is what I am doing now. When printed as chars, all these spaces look the same to me.

```
at 17, 160 <> 32
at 26, 160 <> 32
```

2:15pm. Ok, I see it. Even in the editor I can just select the empty space at is will show me what is going on. Language tools for some reason is using a different word (160) than the regular space (32) and that is what is causing trouble. Easy fix.

2:20pm. Ok, let me post this thing.

2:25pm. This is beyond troublesome. How do I switch to the old editor so I can just paste the text as it is?

2:30pm. The wordpress interface is so convoluted. I figured out how to switch the classic editor, but now it is not letting me do the change due to it shadowing the one I trashed.

2:40pm. Finally posted the thing. I feel like me trying to remind myself how to switch to the classic editor is going to be a recurring skit every six months.

Note: To switch to the Classic Editor go to WP Admin -> Posts and edit the draft from there.

I'll add this note to the top of this journal file. That way I will be reminded where the instructions are.

2:50pm. Ok, I got that out of the way. I am just taking a short breather. This always takes me a full hour for some reason. The PL thread is not up yet.

2:55pm. It is time I start work on the docs. As expected, when I am fresh, the inspiration comes much more easily. And I did have some time to think about it during the night. Today I will try keeping it up till 8pm. Given that I've been skipping the morning session and getting up late, 6pm is really enough time in the day to do all that I want.

3:30pm. Had to take a little break. I realized that I forgot to make the `:` parser indentation sensitive.

```fs
            (indent i (<=) (opt (skip_op ":" >>. root_type_annot)))
```

Let me just go with this.

3:35pm. Since it is not really important I'll leave this change for a later patch. Let me just focus on the documentation for the time being.

No doubt later, maybe soon, I'll have to do something to allow `print_static` in the editor. It would be best if I could open the plugin in a terminal. There was something about that in the samples.

I'll also need to look into language extension options. There was stuff in the sample for that.

3:40pm. Focus me. I need to focus on the docs for now. I'll deal with the extension configuration and terminal launching later.

4:30pm. Good thing I haven't just published the thing without testing it. What I had there broke the parser.

```
(opt (indent i (<=) (skip_op ":" >>. root_type_annot)))
```

Let me try this.

5:30pm.

```
// Asserts an expression. If the conditional and the message are literals it raises a type error instead.
inl assert c msg =
    inl raise =
        if lit_is c && lit_is msg then error_type
        else failwith `(())

    if c = false then raise msg
```

Fixed an error in assert. I was not passing the type as the first argument.

```
inl assert c msg =
    if c = false then
        if lit_is c && lit_is msg then error_type msg
        else failwith `(()) msg
```

Let me implement it like this. What I had previously was too complicated.

...Let me actually test this.

6:05pm. Done with lunch. Let me resume. I can keep going for a while longer.

```
Error trace on line: 4, column: 5 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\a.spir.
    assert_less_than_ten 11
    ^
Error trace on line: 3, column: 34 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\a.spir.
    inl assert_less_than_ten x = assert (x < 10) "The argument must be less than 10."
                                 ^
Error trace on line: 128, column: 5 in module: c:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin\core\real_core.spir.
    if c = false then
    ^
Error trace on line: 129, column: 9 in module: c:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin\core\real_core.spir.
        if lit_is c && lit_is msg then error_type msg
        ^
Error trace on line: 129, column: 40 in module: c:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin\core\real_core.spir.
        if lit_is c && lit_is msg then error_type msg
                                       ^
The argument must be less than 10.
```

Yeah, it all works.

6:20pm. Right now I am at 2k lines. I've exceeded my previous high.

But I am starting to feel pinched. I really do need the Spiral compiler to have the capability of showing itself somewhere. Other compilers are fine, but Spiral programs can cause the compiler to stack overflow at compile time. I need to warn the user about that somehow. I need to enable print_static to be used from the plugin. I am going to make that my priority tomorrow.

6:30pm. Hmmm, I need to think a little what comes next. Let me take a break.

I want to cover type inference in the bottom up segment.

6:45pm. I am back. I should be able to do this for another burst. Let me give it a try.

7:25pm. No, let me stop here at 2.08k. I just feel too unmotivated to do this next part right now. I need my sloth after all. Let me publish the patch. Done.

Let me also see if the PL thread is up.

...Nope. I'll post the monthly rev tomorrow then.

7:30pm. Tomorrow I will take a break from the docs to upgrade editor support. I am actually up for doing this since it is related to user experience. This is what I want to do the most right now. The thing I least want do right now is hack on the language itself, such as when doing that typecase fix. I want to put working on the language firmly behind me.

I paid my dues to the PL gods with v0.09, the two prototypes and now v2.

Let me close here.

I am going to put another dent in this tomorrow. 2.1k is not too bad. 30 lines is a single page, so right now I am at 70 pages. I won't make any hard limits on how low the number of lines should be. As long as the language is covered in depth sufficiently enough it will be fine.

Struct of array tensors and serialization I'll do as separate chapters from the two main ones. For reverse serialization, I do not think the language has enough built in ops yet. I'll have to extend it more.

I'll use opportunity January is giving me to trully finish the language. Then come the chips."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[e49c0114b5...](https://github.com/fc1943s/The-Spiral-Language/commit/e49c0114b59c716dae0caee9413364394312a7ff)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"10:40am. I am up. Let me chill a bit. I am too groggy to start now. Maybe I will take it easy today. During the night I've been dwelling on failure.

I've done my best to be realistic - the conditions for Spiral are good, but I've been thinking what should my attitude be if my luck turns out to be bad. What if I trully am insane and my estimates turn out to all be delusions?

11am. I find these thoughts depressing, and I am dwelling upon my immaturity. That I would get depressed just because of this? It is really so pathetic to place my hopes in other people. In games, do I get invested in NPCs doing this or that?

Suppose I can't get it, so what?

Would I drop work on Spiral, and get a regular job? Of course not. Regardless of what happens, Spiral is a vital part of the Singularity run - without it I wouldn't be able to use the hardware when it comes out. I certainly cannot stop work on it. I can't stop doing what is important, for the sake of doing arbitrary tasks for random nobodies just because of money that I don't need.

I'd do it if I had actual need of money of course, but I don't. Nobody is really pushing me to get my hands on money other than myself. The circumstances don't require it.

So the fact that I keep following my path is benefit enough. That I cultivate my programming is the true merit of all of this.

Other people don't matter a fart, placing hopes in them can only hinder me.

I am lonely, but do I actually want to go out and spent time in the company of others? Hell no.

Programming is what should sustain me in all ways.

11:05am. One day, when the agents start showing sparks of life, programming will be more fulfilling.

My emotional control is poor, but my planning has been right.

11:10am. I am just human, I don't have the inspired desire yet. But now that I've been doing this without pause for 5.5 years, maybe it is time I make it my principle to accept labor as a virtue? So much what I desire is useless or has negative value to me, but labor, the thing I do not want is what is greatly beneficial.

So it is not wonder that I feel depressed about my own desires.

11:15am. It is fine. It is fine if I am a fool as long as I put in the work. As long I do not compromise on my goals.

11:20am. I feel like taking it easy today.

https://www.youtube.com/watch?v=9epgZ-e6DUU
Cliff Click — The Sea of Nodes and the HotSpot JIT

I feel like watching a video or two by this guy.

11:30am. Let me start the video. So far I've been reading manga. The troublesome thing about doing this when the work is over is that I am usually so mentally exhausted that I can't enjoy it as much.

11:35am. Doing something other than the usual routine every once in a while is not bad. Later I will get back to the docs.

I've been thinking about the latest section I've been writing - it is too autistic. I gave it my best shot earlier, but did not have much inspiration then. Since then I've been trying to get to the root of things and have more inspiration.

11:55am. Let me try another talk. I am not that interested about the Java compiler.

https://www.youtube.com/watch?v=ldNH1qc0XmE
Big Data with Cliff Click

12:10pm. Let me get breakfast while I watch this.

1:20pm. The talks by him are very technical, not really what I've been hoping for during my off time. Nevermind this.

Also, I am going to go crazy if I keep surfing /a/. Let me do some work here.

First come chores. Then I'll get to work on the docs.

That will get me into the right mindset. I'll am going to redo some of the latest parts as I am not happy with how it came out. I've been focusing too much on the quantity, and I should take some time to make the quality of it right.

1:40pm. Done with chores. I am completely serious about this, so I had to make some time to dwell on the failure. But doing it is exhausting and contining it further would be counter productive, so I'll stop. I'll go into the docs and negotiations after that assuming I will win.

As long as the conditions are good, keep pushing forward. That is the basis of speculation. Don't try to beat the market. Don't try to get rich. Just rid the wave. Keep the long term in mind.

1:45pm. Let me finally get back to the docs.

1:50pm. Now what I want to do is cut off everything that I've written so far in the bottom up segment.

I'll take a loss for about 400 lines written, but I want this part to be done better.

* Var injection in record with in the docs. `{a$k with ...}`

Ah, yes. I want to cover this part in records as well.

1:55pm. I feel a deep fatigue and disappointment, but amidst of it all there is a strong determination steadily burning. What is this fire, but the fire of life?

Whatever the future may be, the documentation for Spiral v2 will be finished. January of 2021 will not be the month where I falter.

2pm. I am going to do this next part with more care. Instead of pushing for 400 lines per day, a 100 of them carefully chosen would be preferable.

For the past 5.5 years, I've erred on the side of being crazy rather than being timid, but now that I am trying to put on my business face, I need to take special care to make my writing clear and understandable. These journal entries are one thing - I can stream my consciousness here as much as I want, but official Spiral docs are another. v0.09 docs were too half baked.

2:15pm. I am brainstorming how I am going to start the next section. Let me just the the var injection thing out of the way first.

2:20pm. Whops, I pushed the extension out too quickly yesterday. It is still opening the shell.

2:30pm.

```
inl main () =
    inl k, k' = .b, .w
    inl flip x = x = false
    inl x = {q = 1i32; w={a="asd"; b=true}}
    {x$k' with $k#=flip}
```

```
Error trace on line: 2, column: 9 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\a.spir.
    inl k, k' = .b, .w
        ^
Error trace on line: 3, column: 5 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\a.spir.
    inl flip x = x = false
    ^
Error trace on line: 4, column: 5 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\a.spir.
    inl x = {q = 1i32; w={a="asd"; b=true}}
    ^
Error trace on line: 5, column: 5 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\a.spir.
    {x$k' with $k#=flip}
    ^
Error trace on line: 3, column: 18 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\a.spir.
    inl flip x = x = false
                 ^
Cannot apply a forall with a term.
```

Ah, whops.

2:30pm. I did the record example in the top down segment, right.

Did I cover without? Yes, I did thankfully.

2:35pm. Now let me turn my attention to the bottom up segment again.

///

From the perspective of the written code, the bottom-up segment generally means the code in `.spir` files and in the `real` bodies. From the perspective of compilation phases, the bottom-up segment happens during partial evaluation. Parsing and the type inference would all be a part of the top-down segment.

There have been a few examples in the previous section, and in this one the advanced use cases of the Spiral language will be covered and explained.

In the previous segment, most langauge features have been covered to a degree that is enough for casual use. There are some new things, but a proficient functional programmer could be expected to pick up Spiral in a few days and make headway in it. The language has eveything a functional programmer knows and loves: first class functions, pattern matching, records, tuples, unions, static typing and so on. Spiral support the low style functional programming as much as any language without dependent types.

The real reason to use Spiral though is its support for the staged functional programming style. This should be a novelty to almost everybody.

There is much to complain about the bottom-up segment, I've done as much in a few places earlier. It is a direct inheritance from the earlier version of Spiral where it was the only way to program. I was in love in love with it for a while, and then I dropped it in disgust, so you might thing I'd consider it a failure. But in fact it was a great success - Spiral v0.09 is a language I'd rate extremely highly on the expressiveness/performance scale. It gave me a new perspective on what both programming and functional programming is, and if I can be successful at sharing it you'll see that there is no reason to consider functional programming lesser than imperative when it comes to performance.

And as it turns out, the very same things that make the language performant are the ones which make it expressive.

///

The only part of this fragment that is not filler is the first paragraph, but starting out with it would set me out in the wrong direction. I made this mistake last time. I start by giving off an innacuous bit of info, but that locks the tone of the next 400 lines in place.

3:45pm. Had to take a little break. Let me resume. The flow feels right now in the Bottom-Up Segment.

5:05pm. I am really happy how the `Heap Allocation vs Code Size` section came out. I feel like the point gets across better now.

5:10pm. I'll have to rewrite the next half-complete section as well.

The entire bottom up segment I started off on the wrong foot it seems.

5:20pm. Now, I've started browing /g/. Well, I needed a short break.

5:25pm. Focus me, focus.

What should I do for the next section?

6:15pm. Done with lunch. Let me read Kengan Omega and then I'll get back to the docs.

6:35pm. Let me resume.

I should put in a bit more.

6:45pm. I am not getting much inspiration at this time, which is not surprising.

The switch to technical stuff is too abrupt. There is more to the story of Spiral than this.

6:50pm. I'll stop here for the day. At some point I am going to wake up before 10am and start putting in proper full day's work. The last few days have been awkward, but I can get back to my usual pace again. `typecase` has been reimplemented so I do not think I'll be running into any large compiler bugs again.

6:55pm. I've primed myself for to stay humble, so when it is time to move to the next part, I will perform at my utmost. Until then, I just have to focus on the docs. And that is what I will do."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[d9bb70edc9...](https://github.com/fc1943s/The-Spiral-Language/commit/d9bb70edc9c6e411327108815ce72cbe38568f58)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"11:05am. I am up. Let me chill for a while. I am finally through the annoying stuff. Let me gather my will for the next part.

11:35am. I want to start, but let me have breakfast instead.

1:30pm. Done with chores and breakfast. Let me finally start.

This took a bit more than it should.

I keep dreaming that at some point I can get back to my earlier habit of starting work at 9 to 11:30 and then doing it again from 1:30 to 6. I've really fallen a long way since the early days.

Let me gather my thoughts.

Forget the past, focus on the present.

1:35pm. Yesterday I published the language on the VS Code marketplace. That act trully was special. I cut the testing phase way short, and now what I am stating is the language is complete.

The future I've foreseen years ago is coming to pass.

Back then, I knew that it was a fool's errand to seriously compete with Google and Facebook when it comes to ML frameworks. But I knew that the winds would shift, and that GPUs will eventually have to be left behind in favor of newer hardware. New algorithms would also become dominant as well.

Data science is a huge meme (in the negative sense) right now, anyway. The way I am approaching it is the right way.

The way to approach the future is to carve out your own vision. I could not do it back in school. I could not do it during my trading days. But my trading experiences of all things gave me courage to go in this direction.

Some traders rather than being short term gamblers like I was, actually study companies and make long term bets on them. The funds that I had were just too low to take such an approach seriously.

And I thought - if one is really going to make long term bets - one has to understand that there is only a limited number of them that can be done within one's life. Instead of wasting time waiting for stocks to go up, hack the world instead!

Attain true power and break this reality!

That is what the speculation ability should be utilized for. I might not know myself, but my perspective on the world is right. I believe in that.

1:45pm. Imagine if GPUs were it right now and I had to repeat my previous effort. I do not think I could bear it.

I would not get anywhere nor get any sort of success. TF and PyTorch are the 800 pound gorillas in the room. Nobody would pay me for working on Spiral. I'd be better off abandoning the effort and joining the ranks of the peasants whether that means using PyTorch + Python, or forgetting about ML and aiming for a regular job. I certainly have all the skills I need for that last thing right now.

I carry such a deep fatigue from all the unpaid work and all the failures throughout my life.

With Spiral v0.09 I might not have lost, but I certainly haven't won. That is how most things go. Of all the times I won, none of them mattered.

But Spiral is the one thing where I tried climbing upwards in earnest, and where I won't regret being at the bottom.

Even trading I did not put as much effort to this extent. Even trading I did not do with all of my being. This I did.

1:55pm. And my reward is both the completed language, and mastery of programming that I desperately desired in my high school days, but could not carve out a path towards attaining.

The next wave of hardware means a new land will open. A new continent will be discovered, and I will pioneer the way forwards.

My current position is incomparably better than it was 5.5 years ago when I started this.

I think that if I had Spiral v0.2 back in the 2005-2010, with my current determination I could have made it the dominant language for programming those devices.

But in 2005 I was just finishing high school - I had in no way the vision nor the skill to do what I did just now.

2pm. Spiral my language - I do love you. And for once, my love will come back to me in the form of real world power. The past that I could not grasp, will once again come by as an opportunity.

I only need to do it once. I will do this and then I will be allowed to chase the Singularity.

2:05pm. My grudge against the outside world is enormous. I've lost. But the power is still out there waiting for me. I might be a fool, but I am not such a great fool that I would give up my future to somebody else.

2:10pm. It is time to face it down. The chaos these changes will introduce is completely in my favor, but will give disadvantagss to all my opponents. I do not necessarily have to be the first one to cause the Singularity, but it won't hurt. The people living in this world can scarcely be considered anything more than NPCs.

But if I am going to throw rocks, I should look at my own behavior foremost.

It is time that I start making more rational decisions and finish cultivating my heart of loneliness. This has been a lonely journey of programming so far, but I need to go a step further and give the middle finger to various 'altruists' trying to get in way of my goals. I need to accept my isolation beyond the activity of programming. Then I will be able to approach relationships with the proper mindset and perspective.

Because otherwise, things could get dangerous. I need make plans for protecting my wallet ahead of time.

2:15pm. The reality of things is now that I am trying to get sponsors, I do have to actively climb a status ladder, even though it is a virtual ladder, roughly half a globe away in the phyisical space. It is worth climbing. And so I should do it properly.

Thanks to Corona, the circumstances could not possibly be better when it comes to remote work.

At this point in time the point to start this undertaking is exactly right.

2:25pm. From here, till the end of January, I will dedicate my effort to doing the docs, debugging and filling in some minor missing features in the language like prototype orphan checking.

I put months and months of effort into the language already. Delaying the meal by a 4-5 weeks is not going to starve me.

2:40pm. Enough randing. Let me open the readme file. I do not even need the IDE for this next part.

Like I sometimes do, I think I might want to step away for a while (the rest of the day really) in order to refine my motivation. Every time I need to start something big, there is always a great sense of inertia that I need to push against.

But let me open the file, and I will try to push through directly. If that works, I will be able to save some time.

2:50pm. I need to slightly adjust the overview.

---

1) First class types.
2) Structural introspection through pattern matching.
3) Interoperability between different languages (such as F# and Cuda.)
4) First class functions.
5) Tuples as heterogeneous lists.
6) First class records.
7) First class layouts of data structures.
8) First class keyword arguments.

---

I need to change this list. A lot of it makes no sense anymore.

---

As the world inexorably hurls towards the black maw of tomorrow, the power to face it is needed.

Throughout the history of programming languages, the choice was between fast or expressive; the two traditions are crystallized by the C and the Lisp family of languages. There has been a lot of effort into this, but always as languages developed and moved forward they stepped away from the bare metal and in turn lost some of that core vitality that is needed for performance.

The culprit for this is the heap allocation by default dogma introduced by Lisp decades ago. It is a crutch for languages with weak type systems.

Abstraction by heap allocation is a dead end. It works moderately well on the current generation of computers where CPU is still the dominant driver of computation.

It cannot work for devices like GPUs and the rest coming down the line. Many of the most important computational devices of the future won't support heap allocation so an alternative is needed to draw out their full power. It is of absolute importance that a language for that task have excellent control over inlining. Inlining, therefore, must come as a guarantee in the language and be a part of the type system.

Inlining is a trade-off that expresses the exchange of memory for computation. It should be the default instead of heap allocating.

A language good enough at propagating information so as to be capable of expressing inlining guarantees is also powerful enough for expressing a lot of other things well - without any abstraction overhead.

* Structural introspection through pattern matching not just for unions, but for all core types.
* Seamless interoperability between different language backends.
* First class functions, pairs and records.
* Composable layouts of data structures.
* Symbols as singleton types.

Spiral is such a language.

Statically typed and with a lightweight, very powerful type system giving it expressiveness of dynamic languages and the speed of C, Spiral is the crystallization of staged functional programming. It boasts of having intensional polymorphism and first-class staging. Its primary purpose is the creation of ML libraries for novel kinds of hardware.

---

I changed that list of bullets and the last sentence.

`Its primary purpose is the creation of ML libraries for novel kinds of hardware.`

This last line is quite important. Any language can be used for anything, but it is much better that the purpose be concrete. Once expectations are set, they can be accomplished. Otherwise you can only make random moves in hopes of getting lucky. Languages aren't an exception.

With this single sentence, I set the tone for the kind of language that I want Spiral to become. Those who aren't interested in it can go elsewhere, and I will be left with only the audience that I want.

Let me move to the design philosophy.

...It is good. It is kind of a meaningless word soup, but these two segments are there to drive interest and set the tone rather than inform.

...Maybe I'll redo the design philosphy from scratch, but right now I do not feel any inspiration to do that. Maybe I'll just remove the entire segment since I do not need two different word soup segments back to back.

Nevermind that.

```
### 0: The way to use the language

The easiest way to do it right now would be to clone this repo. In the Testing project, look at `run.fs`. It has the latest example used for the tutorial. Select the `Testing` project as the starter one and point the output to the `output.fs` file in the `Temporary` project. No need to worry about getting it wrong - at worst an exception will be raised.

Modifying the Cuda configuration options in the `run.fs` file unless usage of libraries related to that is required.
```

Let me start with this.

3:35pm.

```
## Getting the language

The language is published on the VS Code marketplace. Getting it is just a matter of installing the **The Spiral Language** plugin. This will install both the VS Code editor plugin and the compiler itself. The compiler itself requires the .NET Core 3.1 rutime and is portable across platforms.
```

I do not need to say anything more here.

3:50pm.

```
## Status in 12/24/2020

Alpha - the language needs more testing before it can be considered roboust. It only has the F# backend at present. More will be added assuming I can get sponsors for novel kinds of hardware. If you are a AI hardware company interested in sponsoring Spiral please get in touch.

Besides lacking backends and libraries, it only has rudimentary package management and some important partial evaluator optimizations to improve compile times for large codebases have been left for later when the need for them will arise. But overall, the situation is way better than it was during the v0.09 era already.

In terms of features that I wanted v2 to have, the language is complete.
```

I should have a status section somewhere.

3:55pm. It is good that I resisted going to bed. I am slowly getting into it.

4:05pm. Right now I am thinking how to approach the next part. I need to cover the project files first.

That is the most basic of the basics.

4:25pm. Had to take a short break. I am still thinking about it.

5:25pm.

```
## Projects & Packages

The hierarchy of Spiral programs is a graph of packages, who internally have a sequence of modules, who internally have a sequence of top level statements such as type definitions and functions, who internally have a sequence of their own local statements.

Spiral files (either `.spi` or `.spir`) can be parsed without a dependency on any other file, but in order for type inference to work, they have to have an owner `package.spiproj` (both the name and suffix has to match) file and be a part of the sequence. The package file that is their owner is the first one that is found when searching outwards from the folder the `.spi`/`.spir` file is in. And on the flip side, `package.spiproj` files can only refer to files that they own - if any of the subdirectories have another package file, then that will be an error.

The way to start a Spiral project, is to create an empty `package.spiproj` file in some folder.

This is its content if you want a project with the file `a.spi`.

```
modules:
    a
```

Now, if the folder does not have `a.spi` you should see an error in the editor indicating as much. The project files are interactive - instead of creating the file in the editor's tree explorer, you can place the cursor on `a` and select the code action `Create file.` in order to actually create it. The files and packages that exist will also have links to them in the package file.

Here are all the forms allowed for the `modules` field.

```
modules:
    a
    b-
    c*
    d*-
    some_folder/
        z
        x
    y
```

`a` and `b-` when created are `a.spi` and `b.spi` respectively. `b-` however has special behavior in that it inlines the module into the enclosing scope. While everything in `a` will have its file name as its module name, `b`'s statements will get included directly into the enclosing one.

`c*` and `d*-` when created are `c.spir` and `d.spir` respectively. Similarly as for `b-`, the `-` in `d*-` acts as the include postfix. `.spi` and `.spir` files have important differences in their processing that will be covered in later sections - for now the documentation will be covering regular top-down `.spi` modules.

`some_folder/` is in fact a folder, and `z` and `x` are its submodules.

The parsing for the `modules` field in the package file is indentation sensitive so `y` won't be considered as part of the `some_folder` folder.

You can delete and rename files and folders from the package file using a code action. Renaming will change the file or folder name on the disk, but it won't actually rename the references to it.

Besides modules, it is also possible to provide packages.

Suppose you have a folder with subfolders `a`, `b` and `c`, each of which have their own `package.spiproj` file. If you want `c` to refer to `a` and `b` here is how it should be done.

```
packages:
    a
    b
```

Packages also support the include the postfix `-`. This is useful for including the core library for example (assuming it is there in the directory.)

```
packages:
    core-
    a
    b
```

By default, the module directory is current, and the package directory is the parent, but it is possible to set them explicitly.

```
packageDir: e:/spiral_packages
moduleDir: src
```

`packageDir` and `moduleDir` fields both support relative and absolute paths.

Besides those 4, there package file schema also supports `name` and `version` fields, but those do not affect compilation in any way at the moment.

The great thing about packages is that their processing is done concurrently. While modules are processed strictly sequentially as in F#, packages are more flexible. Circular links between packages though are not allowed and will report an error.

### TODO

* Put the core library somewhere the users can get it. Right now it is buried in `Spiral Compilation Tests\compilation_tests`.
* Expand the `packages` field so that more elaborate paths can be provided.
```

This should be good for now. I'll expand the package parser at a later date. This is not important to me right now. I do not expect any users in the near term.

5:35pm. I'll start the next segment as well.

So far I am doing well, already at 6 pages. A month of this and I will be done without problem.

6:45pm. I'll continue this tomorrow. Let me commit here.

It is good that I found the motivation to actually do something today. Tomorrow, I will put a dent in the top-down section. Let me chill here. There is no point in being frustrated by the pace of progress or wishing one could do more.

One just has to keep a steady pace and that's it."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[17fbb97e4e...](https://github.com/fc1943s/The-Spiral-Language/commit/17fbb97e4e24a5214b22e44ed4836686d08fae24)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"11:10am. I am up.

What I am doing right now - what I have been doing for the past 5.5 years is fundamentally right. Gather inspiration, and then manifest it as code. This is the fundamental act of programming.

This is how a programmer fights. This is the whole of the battle.

The wrong way to fight is to go into it personally, trusting in your own feelings to carry you to victory.

A real wizard fights through proxies. A real wizard always uses proxies.

11:15am. A person is the most effective when his reason and emotions work towards the same goal. When they are opposed, things get nasty. This is later part more or less describes all the failures in my life. Post humans would never have this problem.

You can't relly on your feelings to carry you to victory.

But your manifested inspiration does have hope.

11:20am. I won't run away from my failures. A person's intelligence is the whole of his being. And having various subsystems working properly and in tune with one another is what it means to be smart.

I am dumb. Because I am dumb I can only be a programmer.

My being is set by nature. Then to unlock my true potential I have to go beyond it. Feelings will not be enough.

To do it, I need the power of machines, and my manifested inspiration.

11:20am. Let me chill just a bit and then I will start.

1:20pm. Done with chores and breakfast. Let me catch my breath.

1:25pm. Let me finally start.

1:35pm. Focus me, leave manga for later.

2:15pm. I am getting lost in thought.

Focus on the docs me.

2:45pm. I've been taking a little break now that I am done with unions. Let me resume. I need to get things going.

2:55pm. I am thinking what I should do here.

Ah, I guess the docs will have to be small than I expected. Let me cover the prototypes and then I am done with the top down section.

3pm. Let me do it. It is time to finish the first part of the language. Then I can cover the real segment. After that I will focus on filling out the docs.

3:30pm.

```
Besides the benefit of being inferable during the top-down segment, the prototype instances can be defined in different modules than the prototype as long as the nominal is defined there.

#### TODO - Implement the instance orphan check

The check for that last part needs to be implemented.
```

Let me implement this thing now rather than have a TODO in the docs.

```fs
            term scope {term=Map.empty; ty=env_ty; constraints=Map.empty} prot_body body
            (if 0 = errors.Count then psucc (fun () -> FInstance(r,(fst prot, prot_id),(fst ins, ins_id),fill r Map.empty body)) else pfail),
            // TODO: Do the instance orphan checking here.
            AInclude
                {top_env_empty with
                    prototypes_instances = Map.add (prot_id,ins_id) ins_constraints Map.empty
                    }
```

This should not be difficult.

```fs
let assert_orphan_instance_check (prot_id : GlobalId) (ins_id : GlobalId) = if (prot_id.module_id = module_id || ins_id.module_id = module_id) = false then errors.Add(r,OrphanInstance)
```

```fs
            assert_orphan_instance_check prot_id ins_id
            guard <| fun () ->
            top_env <- {top_env with prototypes_instances = Map.add (prot_id,ins_id) ins_constraints top_env.prototypes_instances}
            term scope {term=Map.empty; ty=env_ty; constraints=Map.empty} prot_body body
            (if 0 = errors.Count then psucc (fun () -> FInstance(r,(fst prot, prot_id),(fst ins, ins_id),fill r Map.empty body)) else pfail),
            AInclude {top_env_empty with prototypes_instances = Map.add (prot_id,ins_id) ins_constraints Map.empty}
```

This should be good. Let me add an error message.

3:40pm. For some reason the exhaustiveness check seems to be busted in the latest F#.

Nevermind this. Let me just move to testing.

3:45pm. It works. I should also disable instance shadowing.

3:50pm. Done. Let me publish the patch.

...Now let me get back to doing the doc.

4:20pm. Let me take a break here. I am done with unions. I think at this point I should just move to the bottom-up segment.

4:55pm. I am back. Let me resume. I have a lot of time, I have no intention of stopping at 6pm. I'll do it for as long as I feel like it. Right now I am at 1.43k lines, so that is 4 pages added today so far. Doing a few more would not be bad.

5pm. Focus me. Start the next section.

It is not going to get done on its own. After the docs are done, the real fun will start.

...Lunch.

5:20pm. I am back. Let me resume. I want to do this for a few more hours. Let me write the documentation instead of surfing /a/.

I need to remind myself to focus.

6:15pm.

```
## Bottom-Up Segment

From the perspective of the written code, the bottom-up segment generally means the code in `.spir` files and in the `real` bodies. From the perspective of compilation phases, the bottom-up segment happens during partial evaluation. Parsing and the type inference would all be a part of the top-down segment.

There have been a few examples in the previous section, and in this one the advanced use cases of the Spiral language will be covered and explained.

In the previous segment, most langauge features have been covered to a degree that is enough for casual use. There are some new things, but a proficient functional programmer could be expected to pick up Spiral in a few days and make headway in it. The language has eveything a functional programmer knows and loves: first class functions, pattern matching, records, tuples, unions, static typing and so on. Spiral support the low style functional programming as much as any language without dependent types.

The real reason to use Spiral though is its support for the staged functional programming style. This should be a novelty to almost everybody.

There is much to complain about the bottom-up segment, I've done as much in a few places earlier. It is a direct inheritance from the earlier version of Spiral where it was the only way to program. I was in love in love with it for a while, and then I dropped it in disgust, so you might thing I'd consider it a failure. But in fact it was a great success - Spiral v0.09 is a language I'd rate extremely highly on the power and expressiveness scale. It gave me a new perspective on what both programming and functional programming is, and if I can be successful at sharing it you'll see that there is no reason to consider functional programming lesser than imperative when it comes to performance.

And as it turns out, the very same things that make the language performant are the ones which make it expressive.

Performance of a language can be boiled down to two factors:

* Understanding what the compiler is doing.
* Having the ability to express that understanding succinctly.
```

I am stuck on how to follow this up.

6:20pm. Ah, damn it. I do not know how to say that I want. I am thinking of Python and dynamic languages, and now I find myself tongue tied. Do I really have to talk about things for which I am not an expert?

6:45pm.

```
Performance of a language can be boiled down to two factors:

* Understanding what the compiler is doing.
* Having the ability to express that understanding succinctly.

Based on those two points, how would various languages rate?

* C - you know what the compiler is (or at least should be) doing as it is bare bones. You have ability to express that understanding, but 'succinctly' is the problem here. The language has very little opportunity for abstraction and nowadays it is more fitting as a compilation target than actual human use.

* Python, Ruby, JS - you do not know what the compiler is doing as the languages in no way expose what the underlying representations of various data structures are - not unless you look under the hood. You can write correct programs and have the abstraction capability, but you have no way to express performance desires.

* Java, C#, F# - Though these langauges are generally considered slower than C, you can get good performance out of them. And the more you program in them like they are C, the closer you actually get C level performance.
```

Drawing in other languages into the story won't be convincing and just opens the door for others to nitpick at me. I already regret mentioning Julia in the previous docs already.

To make things convincing I should provide code samples from various other languages, but that would too much autism.

8:30pm. The memory tradeoff chapter turned into a huge unsubstantiated rant, just the way I like them. If the readers want science they can do it themselves, I want to get the basic theme going.

Let me close here. Currently the docs are at 1.71k. This is not bad. Those two large examples bloat the count somewhat, but even so, they are only 130 lines. I might have written a bunch myself. I was really into it for this last part.

8:35pm. I really have no idea what the hell do I want to do for the rest of the bottom up segment. I get the sense that I should at least demonstrate the struct of arrays stuff and serialization. Those two are Spiral's biggest strengths so I should highlight them. Right now I do not have them, so I am going to have to do some programming instead of just writing, but going in that direction is a good idea anyway.

I haven't really tested typecase or real nominals yet anyway. There are challenges waiting to be dealt with.

8:40pm. Tomorrow, I should start things off by showcasing some of the bottom up techniques for doing type inference and warn the user not to do it.

I should start by explaining filling that the inferencer is doing and do the type application by hand. I'll do that."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[e819d4e64c...](https://github.com/fc1943s/The-Spiral-Language/commit/e819d4e64c88b8bd9acc549cab4eae042023280e)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"First the PL sub one.

///

[Spiral v2](https://github.com/mrakgr/The-Spiral-Language) is out on the VS Code marketplace. Installing the language is as simple as installing the plugin from the extensions tab. It is still in testing phase, and it should have been for a few months more, but I decided to not be timid, and pushed forward the release. My plan right now is to keep fixing the bugs while I do the docs.

Even though I say that, the language is not in a poor shape at all so feel free to give it a try. By the time January is over both the documentation and the language should be in good shape.

It has been a long time getting to this point. I spent the entire year 2020 on making it happen. Every design mistake from v0.09 has been ammended, and the language has a cool, new top-down type system to take the edge off the partial evaluation magic that it does.

After January is done, I intend to finally put my plans into action. In 2018, I put in a lot of effort on making a GPU-based deep learning library using the original Spiral. In 2021 I will do the same thing except much better. I will make use of the language as wedge to get me through the door of [various hardware companies](https://cacm.acm.org/magazines/2020/8/246356-neuromorphic-chips-take-shape/fulltext). Getting them to sponsor me is one aspect of the plan, but the main purpose of the expedition will be to get a handle on these devices and make sure I am continually at bleeding edge of the hardware wave from here on out.

Though I could not accomplish my main goal 2018 which was making a good RL agent, the ML library itself was in my view fairly impressive - I manage to create an fully optimized RNN (similar the one in the [Nvidia blog post](https://developer.nvidia.com/blog/optimizing-recurrent-neural-networks-cudnn-5/)) and used it as a model in a policy gradient training of a poker agent whose game implemented alongside it. I had to the automate serialization between language barriers, and the game's data types and something the NNs could process. In order to implement optimized GPU kernels such as the one in the blog post, I had to implement automatic differentiation on GPU itself. All of the technical achievements were not accomplished simply by gritting my teeth and dropping down the low level, but through innovative high level abstractions. For example, GEMM fusion from that blog post is made much easier by having tensors with named dimenions.

This is the usual habit in my programming - I solve a task, I generalize the solution and then reuse the abstractions elsewhere. The language one is using makes a vital difference - that library and all those optimizations would have been impossibly difficult to do in C for example.

I made some mistakes too. When it comes to making a GPU library, it turns out that .NET's GC is really a poor fit for managing GPU memory. I'd have been better off picking Python as a target platform. Towards the end of 2018 the old Spiral's poor design and implementation made the compile times go up drastically. And having to do type inference programmatically was really a anchor around my neck.

I can go on about my regrets, but even if it weren't for all of those, I do not think I could have accomplished my goal. Towards the end of 2018, I realized one thing - though GPUs are the workhorse of deep learning, they are actually a very poor fit of reinforcement learning. I spent a long time bashing my head how to improve the performance of RL algorithms. I blasted backpropagation. At some point understanding will dawn, but until then I've realized that what I should do is make do with poor algorithms.

Maybe backprop is a poor fit, but the reality is that the task of reinforcement learning is particularly difficult. In 2018 I've challenged myself to improve a single model and got nowhere. Instead of doing that, in 2021 I will take advantage of new hardware to master ensembles.

In 2018, I would train a model, and would get wildly different results depending on random seeds. It is an open secret that RL reseachers cherry pick their results. Instead of getting mad at that, what I have to do is formalize that insight. If training a single model is all up to luck, why not train a 100 of them in a single go?

GPUs are actually a very poor fit for that. They are good for quickly processing batches of data through a single model, but doing something like passing a single vector of data through numerous networks would be the worst case fit for them. It will be different for [neurochips](https://www.youtube.com/watch?v=jhQgElvtb1s). The new language will allow me deal with the hardware, and the hardware will allow me to complete the agents that I could not a few years ago.

Well, that is the plan for when I am done with the docs. I plan on striking out and getting in contact with hardware companies themselves when I am ready. If somebody from the hardware side is reading this and is interested having a Spiral backend and a ML library for it please do get in touch.

///

5:25pm. The above should be good for the PL sub.

5:35pm. I am taking a short break right now. I am not really in full blast like when doing the docs.

6pm. Let me resume. I need something for the yearly review. I won't post this part on the PL sub.

///

(Continued from the PL monthly sub post.)

If this plan works, I will be able to solve my poverty woes in one fell swoop. The paper I linked to says there are 50 startups, so there are plenty of potential sponsors for my services. I plan to price the rental space in the Spiral ecosystem for these companies at 3k per month. Assuming the sponsor is interested in having a permanent backend and library to the point of paying for it, this is the price point that I think will make it rational for the companies to just cash out to me instead of hiring another programmer to fork Spiral and maintain that. Maybe I could go for more, but I will curb my greed and resist trying to squeeze the other parties. Maximizing money is not that important, I want to get through this next part peacefully.

Since the market is ripe, I am hoping to get a bunch of them and build up my monthly income that way.

In Croatia, the average salary is a bit over 1k per month. Local dev salaries are higher than the average, but it is not a rich region by any means. Even just getting single sponsor would put me way above average. And I've been without money for long enough so I am determined to make this work. I need to get access to chips anyway - instead of paying for them years down the road, isn't it better that I get others to pay me to program them today? I really do need to explore the offerings anyway, I don't have a view on which specific piece will be dominant yet. It would be a mistake to pick one and stick with it; at this point I do need variety.

Unlike v0.09 which was researchy kind of language, and whose libraries I've written in F# strings, v2 has way higher quality across the board, so I am confident on about the quality of my offering.

Still, it is not like my past schemes were sucessful. But to be fair they were pretty crazy.

This has a fairly rational chance of working out, but I don't have the experience nor the knowledge to tell how things will go. I should be able to convince the leads to take a look at Spiral, but whether the companies will be willing to pay depends on the level of the people working there. I expect them to be mostly using Python + C as their hardware stack. This should have a large amount of friction that Spiral could alleviate, but who knows, maybe the guys there will be the kind that likes C.

I have no idea what the general programmer level of the C crowd is, but there are plenty 'lol GC bad' kiddies there. They are not exactly innovative. If the guys I keep running into don't see a point to a language having first class functions, that will make any kind of negotiatons untenable. The ideal team would be the one that has positive experience with other functional programming languages. I can imagine those kind of people really being impressed with Spiral.

But even though functional programming is in ascendance, it is not mainstream by any means. So if I run into a team like that, it will more likely be an exception than the rule. I might end up being forced to take whatever opportunity I can get.

I can do a good job on Spiral, and I can try to tailor my message, but beyond that things are out of my hands. I'll do my best and let the dice land where they may.

If this were all about money, trying to make a poker agent, let alone a language would make zero sense.

It is not that crushing [these guys](https://www.esportsearnings.com/) would be satisfying monetarily. It is just I can't imagine a successful Singularity run that does not go through that path. Could there exist a programmer too weak to beat online gaming, but strong enough to conquer the universe? I doubt it. Gaming success is as much of a sanity check as it is an opportunity to make money along the way.

When I decided to make Spiral, I set on out on my own path. I really expected there would be more people than just me working on a language to make a ML library. Because I know back then that down the road new hardware will come out, and Theano, Tensorflow - whatever was popular at the time would be scrapped. The hardware companies would not have Google level resources to make those kinds of compilers. Even if they do take the effort to integrate with popular frameworks, what will happen if deep learning gets superseeded by new algoriths?

Furthermore deep learning is not so difficult as to necessitate such huge software investments that Google and Facebook are making. I could not make a GPU library in F#, but it was doable in Spiral v0.09 and it will be easy in v2.

I do feel a certain sense of loneliness, but in the software world the isolation I endure today will be competitive moat tomorrow.

It is difficult. In games you command the player character and the action gets executed. If only my own mind had the same kind of calm attitude and disposition that my proxies do. My own mind requires deep planning and elaborate beliefs to embark on a course of action. The action requires effort, but establishing motivation requires just as much effort. It is tiresome.

Do I have anything better to do than programming in this life? No. If I could go back in time 15 years ago, I'd command myself to do programming. If I could get an extra 15 years of work today for free, just how much further along would I be? It is unimaginable.

I can't change the past, so this time I'll be smarter and give this gift to the me of the future. For a person of a sinister character such as myself, programming is a fitting punishment.

Every day I gather inspiration, then I try to manifest it as code. I manifest it as writing. I gather inspiration, and let it loose, letting my hands act out the office of the mind after that. This inspiration is an invisible power that I have to contain in raw matter. Otherwise it would escape.

Yet even though I keep doing this exercise, I haven't attained even a bit of what I want yet. I have no intention of stopping.

I will find my dream again, at the end of the human era.

///

8pm. This is the way to end it. I'll proofread these later. Let me just close here, I am too tired to do that now. Tomorrow, I want to get started on the typecase redesign. That will take me a day or two. I'll have to change many parts of the compiler. I'll even have to get rid of the current pattern style compiler for typecase in the prepass."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[dfb087b5e8...](https://github.com/fc1943s/The-Spiral-Language/commit/dfb087b5e8414527095df66115a3bdc525357a29)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"10:30am. I am finally getting up earlier even if by only a little. Yesterday exhausted me. Writing that last review opened my eyes.

Whether my plan succeeds or not really depends on the competence level of the teams doing the software stacks at those hardware companies. Assuming there is enough choice for me to pick my targets, I need to focus primarily on those with functional programming experience. Alternatively, those open to learning new languages. Otherwise things will get really hard.

10:45am. These sorts of worries are a welcome break from my other obsessions. If I am going to have my mind occupied, it should be by things of actual importance to me.

11:05am. Done chilling. It is time to start this thing.

If I am going to get sidetracked, it only makes sense that this be by the requirements of the path itself. I should not get jobs on the side - the path itself should sustain me. This is what I am going to test in 2021 most of all. I could not have much success aiming high, so what if I tried aiming low? If I can grasp the low, I can use it a stepping stone to higher places.

11:10am. I really want to give the middle finger to my general environment. I've been living here in the middle of nowhere for who knows how long, and I've had to endure being at the bottom for so long, but it was all for nothing in the end. Figuring out the meaning of life did not get me closer to anybody, instead those deep secrets just keep further estranging me from humanity. I don't know whose fault that is, but I know who is going to pay.

And what I must do until I get my power is embrace labor.

Well, I might regret it now, but it is not like it was not plan B all along. I have a nasty tendency to want to explore too much which just exarcebates my mental strain.

```fs
    // Typecase
    | ETypeLet of Range * Id * T * E
    | ETypePairTest of Range * bind: Id * pat1: Id * pat2: Id * on_succ: E * on_fail: E
    | ETypeFunTest of Range * bind: Id * pat1: Id * pat2: Id * on_succ: E * on_fail: E
    | ETypeRecordTest of Range * Map<string,Id> * bind: Id * on_succ: E * on_fail: E
    | ETypeApplyTest of Range * bind: Id * pat1: Id * pat2: Id * on_succ: E * on_fail: E
    | ETypeArrayTest of Range * bind: Id * pat: Id * on_succ: E * on_fail: E
    | ETypeEq of Range * T * bind: Id * on_succ: E * on_fail: E
```

What I need to do is get rid of this.

11:15am. Done. I've just chucked a large amount of code essentially overboard.

```fs
        | RawTypecase(r,a,b) ->
            let a = ty env a
            let id, env = fresh_ty_var env
            failwith "TODO"
```

This is where I need to start with once again.

```fs
| TMetaV of Id
```

Let me add this to the list of `Ty`s.

Also, I think I disabled opening the term scope in typecase right?

```fs
        let case_typecase d =
            let clauses d =
                let bar = bar (col d)
                let typecase = root_type {root_type_defaults with allow_metavars=true; allow_wildcard=true} >>= typecase_validate
                (optional bar >>. sepBy1 (typecase .>>. (skip_op "=>" >>. next)) bar) d
```

Yeah, that is the case. The truth is, as long as metavars aren't eagerly bound I could in fact allow it, but unless somebody demands this, I think I'll just leave it out. It is not important.

I am not sure if it was yesterday or the day before it, but I've had a great insight. I can do unification in the peval segment as long as I take care that metavars never leave the typecase.

Also, evaling the types never actually leads to nominals (which can have term segments) being unboxed, so I am safe there. All this combined means I can have an easy time of implementing what I want.

It is a pity. What I had previously would not have been bad if matching on regular functions was not necessary. The way I decided on doing it compiled style is because I decided I would not need it, but I was wrong. I absolutely do need to match on the results of regular type function application.

11:30am. Focus me, let me just get through the prepass parts. I need to introduce `ETypecase`.

```fs
| ETypecase of Range * T * (T * E) list
```

I guess I will set it to this.

11:35am.

```fs
        | RawTypecase(r,a,b) ->
            let a = ty env a
            let id, env = fresh_ty_var env
            failwith "TODO"
```

Let me start with this.

```fs
        | RawTypecase(r,a,b) ->
            let b =
                b |> List.map (fun (t,e) ->

                    )
            ETypecase(p r,ty env a,b)
```

Hmmm, this part is troublesome.

```fs
    and ty (env : Env) x =
        let f = ty env
        match x with
        | RawTMetaVar _ -> failwith "Compiler error: This should have been compiled away in typecase."
```

I actually want to reuse ty in order to convert the metavars.

I'll also have to return the env, so that I can eval the typecase cases.

```fs
    and ty' (env : Env) x =
        let mutable is_metavar : _ HashSet = null
        let mutable env = env
        let rec f = function
            | RawTMetaVar(r,a) ->
                if is_metavar = null then is_metavar <- HashSet()
                if is_metavar.Add(a) then
                    failwith ""
                else
                    failwith ""
```

I'll use a null here for efficiency.

11:50am.

```fs
    and ty' (env : Env) x =
        let mutable is_metavar : _ HashSet = null
        let mutable env = env
        let rec f = function
            | RawTMetaVar(r,name) ->
                if is_metavar = null then is_metavar <- HashSet()
                if is_metavar.Add(name) then
                    let id, env' = add_ty_metavar env name
                    env <- env'
                    TMetaV id
                else
                    env.ty.env.[name]
```

This is pretty good.

12pm. Now I am just getting lost in thought. Let me complete that case.

```fs
        | RawTypecase(r,a,b) ->
            let b = b |> List.map (fun (t,e) ->
                let env, t = ty' env t
                t, term env e
                )
            ETypecase(p r,ty env a,b)
```

This should be good enough.

Yeah, this is good enough for the morning session. Later I will fill out all the prepass cases. Then I'll move to the peval. It should not be too hard. I can do this thing. If nothing goes wrong, I should manage it today. Let me have breakfast here."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[43b4fd4ffb...](https://github.com/fc1943s/The-Spiral-Language/commit/43b4fd4ffbd7b91658e7fa4c2d0dcfc26eb5de0f)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"2:15pm. Let stop reading Fang Yuan's demonic adventure or I will never end the break. Let me watch the Toji ep and I will focus my mind on work.

3pm. Done with the break.

I had my bit of fun. Now my tension is up and I want to do some work.

It is time to get things done. This will be the real deal. First of all, let me get the socket thing out of the way. No need to dawdle on this. Let me do the change and then I will test it out.

```fs
    use client = new PublisherSocket()
    client.Connect(uri_client)

    use __ = queue_client.ReceiveReady.Subscribe(fun x ->
        x.Queue.Dequeue() |> Json.serialize |> client.SendFrame
        client.ReceiveMultipartMessage() |> ignore
        )
```

This should not be receiving things anymore let me remove that last line.

Let me change things on the VS Code side next. Focus me, focus. Let me get a move on.

```fs
    use client = new PublisherSocket()
    client.Bind(uri_client)

    use __ = queue_client.ReceiveReady.Subscribe(fun x ->
        x.Queue.Dequeue() |> Json.serialize |> client.SendFrame
        )
```

Forgot that I also need to swap the binds and connects.

3:10pm. Hmmm...

```ts
    let isProcessing = true;
    (async () => {
        const sock = new zmq.Subscriber()
        sock.receiveTimeout = 2000
        await sock.connect(uriClient)
        while (isProcessing) {
            try {
                const [x] = await sock.receive()
                const msg: ClientRes = JSON.parse(x.toString())
                if ("PackageErrors" in msg) { errorsSet(errorsProject, Uri.parse(msg.PackageErrors.uri), msg.PackageErrors.errors) }
                else if ("TokenizerErrors" in msg) { errorsSet(errorsTokenization, Uri.parse(msg.TokenizerErrors.uri), msg.TokenizerErrors.errors) }
                else if ("ParserErrors" in msg) { errorsSet(errorsParse, Uri.parse(msg.ParserErrors.uri), msg.ParserErrors.errors) }
                else if ("TypeErrors" in msg) { errorsSet(errorsType, Uri.parse(msg.TypeErrors.uri), msg.TypeErrors.errors) }
                else if ("FatalError" in msg) { window.showErrorMessage(msg.FatalError) }
                else { const _ : never = msg }
            } catch (e) {
                if (e.errno === 11) { } // If the error is a timeout just repeat.
                else { throw e }
            }
        }
        await sock.disconnect(uriServer)
    })();
```

Let me go with this for the time being, but I am not sure if this will be enough. I know that pub/sub sockets might need to have the first entry as their filter. I forgot how that worked. Let me try this and then I will remind myself if it fails.

3:15pm. It is as I feared. Errors do not show up. I need to refresh my memory of how pub/sub sockets work.

https://zguide.zeromq.org/docs/chapter2/#Pub-Sub-Message-Envelopes

Ah, it says it is optional.

3:20pm. Ok, I do not think not having keys is why my sends are failing. Let me see what is going on the VS Code side. I'll put some print statements in there.

```fs
        window.showInformationMessage("Connecting...")
        await sock.connect(uriClient)
        window.showInformationMessage("Connected.")
```

Things are not happening the way I thought they would. For some reason, this does not finish connecting. Then the error is on the server side.

```fs
    use client = new PublisherSocket()
    client.Bind(uri_client)
```

But I did make sure to bind the client.

3:25pm. Things like this happen. I wanted to do this in the morning session, but when I looked at the clock it was 11:45 and I did not feel like starting anything new. I made the right choice. Right now I have no idea what is going on. It is definitely not good to rush situations like this.

I have no idea. I will have to look at the Lithe examples again.

```
    module Weather =
        let uri = "ipc://weather"
        let server (log : string -> unit) (poller : NetMQPoller) =
            try let rand = Random()
                init PublisherSocket poller (bind uri) <| fun pub ->
                log <| sprintf "Publisher has bound to %s." uri
                use __ = pub.SendReady.Subscribe(fun _ ->
                    // get values that will fool the boss
                    let zipcode, temperature, relhumidity = rand.Next 100000, (rand.Next 215) - 80, (rand.Next 50) + 10
                    sprintf "%05d %d %d" zipcode temperature relhumidity |> pub.SendFrame
                    )
                poller.Run()
            with e -> log e.Message

        let client' uri (filter : string) (log : string -> unit) (poller : NetMQPoller) =
            try init SubscriberSocket poller (connect uri) <| fun sub ->
                SubscriberSocket.subscribe sub filter <| fun _ ->
                log <| sprintf "Client has connected to %s and subscribed to the topic %s." uri filter
                let i = ref 0
                let total_temp = ref 0
                use __ = sub.ReceiveReady.Subscribe(fun _ ->
                    if !i < 100 then
                        let update = sub.ReceiveFrameString()
                        let zipcode, temperature, relhumidity =
                            let update' = update.Split()
                            (int update'.[0]),(int update'.[1]),(int update'.[2])
                        total_temp := !total_temp + temperature
                        incr i
                        log (sprintf "Average temperature for zipcode '%s' since the start of the sequence is %dF" filter (!total_temp / !i))
                    else
                        poller.Stop()
                    )
                poller.Run()
            with e -> log e.Message

        let client = client' uri
```

Hmmmm. I don't know.

Let me make a sub socket on the F# side just to check that things are working fine there. I need a sanity check.

```fs
    use sub = new SubscriberSocket()
    sub.Connect(uri_client)
    use __ = sub.ReceiveReady.Subscribe(fun x ->
        let q = x.Socket.ReceiveMultipartMessage()
        printfn "%A" q
        )
```

This is not receiving anything.

3:40pm.

```fs
    use sub = new SubscriberSocket()
    sub.Connect(uri_client)
    use __ = sub.ReceiveReady.Subscribe(fun x ->
        printfn "Ready to receive."
        let q = x.Socket.ReceiveMultipartMessage()
        printfn "Got: %A" q
        )
```

I can't figure this out. I guess I'll have to keep grinding away at it until I do. ZeroMQ is so nasty in that it essentially forces you to do assembly programming in disguise.

No type safety anywhere.

...No, nothing. The sub socket is just not getting anything.

```fs
    use sub = new SubscriberSocket()
    sub.Connect(uri_client)
    sub.SubscribeToAnyTopic()
    use __ = sub.ReceiveReady.Subscribe(fun x ->
        printfn "Ready to receive."
        let q = x.Socket.ReceiveMultipartMessage()
        printfn "Got: %A" q
        )
```

Ah you son of a bitch.

Let me try this.

```fs
    use sub = new SubscriberSocket()
    poller.Add(sub)
    sub.Connect(uri_client)
    sub.SubscribeToAnyTopic()
    use __ = sub.ReceiveReady.Subscribe(fun x ->
        printfn "Ready to receive."
        let q = x.Socket.ReceiveMultipartMessage()
        printfn "Got: %A" q
        )
```

Agh, I forgot to add it to the poller as well.

Yeah, this works now. I need both the poller add and the subscribe.

```ts
        const sock = new zmq.Subscriber()
        sock.subscribe()
```

So I should do this on the TS side as well.

But the problem on the TS side is that I can't get it to even connect.

```ts
const uriClient = `tcp://*:${port+1}`
```

Ah, I forgot - wasn't there some trouble with the shape of these addresses last time?

```fs
let uri_server = sprintf "tcp://*:%i" port
let uri_client = sprintf "tcp://localhost:%i" (port+1)
```

On the F# side, since I am binding, let me use `*` for both of these.

```ts
const uriServer = `tcp://localhost:${port}`
const uriClient = `tcp://localhost:${port+1}`
```

On the client side, let me `localhost`.

This was a thing before, but it took me a while to jog my memory of things.

I think now the sub should work on the VS Code side. Let me give it a try.

3:55pm. Yeah, it is fine now. The errors are back online.

I like the changes from an aesthetic perspective. I no longer have the server both binding and connecting to the client. The client is only making connections, and the server is only doing the the binds. That is how you know it is a server.

Right now the distinction between the two is very clear.

This was also a conceptually trivial change, it took me almost an hour to do because of ZeroMQ has little type safety. I was right to be suspicious of how long this could take me.

4pm. Well, it is behind me now. Let me commit this.

With this the server will be fully capable of interacting with multiple clients. No problem there anymore."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[a0edbe926c...](https://github.com/fc1943s/The-Spiral-Language/commit/a0edbe926c09574e6ccf53ba1a07c38a7ac0c7d3)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"11:10am. I did not go to bed too late yesterday, but I had a hard time falling asleep. Sigh.

11:15am. Let me go for dinner, and chores. Then I'll resume the docs. I am really groggy right now, but I need to get a move on.

12pm. Let me do the chores and then I will start this thing. I slacked way too much.

12:25pm. Done with chores.

12:30pm. Focus me. Let me start work on the docs. I think it is time to showcase macros.

During the night I had some awkward thoughts.

If we assume that Spiral's `let` statements are equivalent to F#'s, while `inl` is `let inline`, then wouldn't that mean that F# in facts supports the Spiral style inlining in full?

If somebody asked me this, I'd find it embarassing to reply. I actually do not know how F# works under the hood. Though I am a functional programming expert by now, I simply never cracked open the disassembler and looked at what comes out.

The reason for that is, even if in theory F# could hit the permance goals, it would not give me the language introp capabilities that I need. So I won't go into it in the docs.

Since I am going to be applying to chip companies, instead of pushing performance, I really do need to highlight the language interop benefits of Spiral.

Let me take a look at the tests.

12:45pm. Let me just go with macros. It seems that I want to get the differences from existing languages out of the way so let me go with theme.

1:35pm. Macros come up to two pages. This is nice and easy.

1:45pm. I am thinking how to approach the next section and even what it should be.

2:10pm. Had to take a break. Let me resume.

2:15pm. Focus me. Let me start writing this thing. I think I've covered 30% of the stuff in the top down segment. It does not have to be 10k exactly. I can do this for two weeks. I'll do this for as long as needed. Until I feel satisfied.

Let me do the layout types next.

3:10pm.

```
inl main () =
    inl a = mut {q=1i32; w=2i32}
    a <- {q=3; w=4}
```
```fs
type Heap0 = {l0 : int32; l1 : int32}
and Mut0 = {mutable l0 : int32; mutable l1 : int32}
let v0 : Mut0 = {l0 = 1; l1 = 2} : Mut0
v0.l0 <- 3
v0.l1 <- 4
```

This is a compiler error. That `Heap0` is not supposed to manifest. What is going on here?

Also when it comes to doing the real segment I really will require some way of taking advantage of `print_static`.

3:15pm. Focus me. Let me switch gears so I can debug this error. I'll have to track this down.

Let me make this one of the tests.

```fs
let rec heap = layout (fun s x ->
        line s (sprintf "Heap%i = {%s}" x.tag (x.free_vars |> Array.map (fun (L(i,t)) -> sprintf "l%i : %s" i (tyv_proxy t)) |> String.concat "; "))
        )
    and mut = layout (fun s x ->
        line s (sprintf "Mut%i = {%s}" x.tag (x.free_vars |> Array.map (fun (L(i,t)) -> sprintf "mutable l%i : %s" i (tyv_proxy t)) |> String.concat "; "))
        )
```

Hmmm, these are both `layout`.

3:25pm. What is going on here, I have no idea.

3:30pm. I finally got the plugin to run from the host again. I forgot how to do that recently. Does `heap` actually trigger at some point? What is going on here?

```fs
    let rec heap = layout (fun s x ->
        line s (sprintf "Heap%i = {%s}" x.tag (x.free_vars |> Array.map (fun (L(i,t)) -> sprintf "l%i : %s" i (tyv_proxy t)) |> String.concat "; "))
        )
```

I'll put a break point here and then take a look at the call stack.

```fs
        | TyLayoutToHeap(a,b) -> sprintf "{%s} : Heap%i" (layout_vars a) (heap b).tag |> simple
        | TyLayoutToHeapMutable(a,b) -> sprintf "{%s} : Mut%i" (layout_vars a) (heap b).tag |> simple
```

Ah, look at that `heap b` on the last line. Whops.

It should be `mut b`.

```fs
type Mut0 = {mutable l0 : int32; mutable l1 : int32}
let v0 : Mut0 = {l0 = 1; l1 = 2} : Mut0
v0.l0 <- 3
v0.l1 <- 4
```

Yeah, now I get correct compilation. This was a minor copy paste error still lurking inside the compiler, probably there are more of a similar kind in there. Let me publish the change as a patch.

I'll commit here."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[c7cab98101...](https://github.com/fc1943s/The-Spiral-Language/commit/c7cab98101f06e8723cd2b759cdeaa155cb9ea4e)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"11:05am. Yesterday I overdid it with the vacationing and went to bed too late. I guess I'll skip the morning session.

11:30am. I got it all out of my system. I am ready to start the action. From here until I am done I'll go at it full tilt. Let me have breakfast first, and as well as deal with the chores. Then I will have uninterrupted segment in which to program in.

12:10pm. Let me do the chores. Focus. I can't spent the whole day daydreaming, on 4chan, and reading Reverend Insanity like yesterday.

12:45pm. Done with chores. Let me start here.

I overdid it yesterday and today - my brain feels like it is fried from various sort of stimuli. I indulged myself far too much.

The last two weeks went by quite quickly for me. I had fun doing the tests somehow, a lot more so that implementing the editor support functionality that I finished in the first week of this month. I had a lot of motivation, but yesterday ran that all into the ground.

I need to distance myself from the internet in general and various indulgences. Let me turn off the router.

Good. Now I need to get back to cultivating my battle readiness. My programming motivation needs to be retrofitted for the task at hand. Let me paste that list.

1) Cleanup. It is time to move from the v0.2 to master. I'll do that along with cleaning up all those v0.09 projects.
2) Bundling. Making sure the complation output goes into the right place where the plugin is. Making the pipeline to easily publish the plugin. Making a check so I do not send a debug version by accident.
3) Implementation. I need the plugin to start the server automatically. I also need to implement heartbeating on both sides.

12:55pm. I need to get started of this. In the next PL update, and the review I should be able to demo somethnig. There is enough time to set things up.

Let me get on with it.

First step - merge with master. The master should be thousands of commits behind by now. Nobody is using v0.09 anyway, so this won't be a huge change.

As an aside, one of these days I should just look at some Git tutorials. I've been using it for years, and I only really know how to switch branches and merge them. All the other features I've avoided like the plague.

If I were getting a job, I would not need to prepare for the interview by grinding programming puzzles, but my use of Git is one place where I could expect to embarass myself. I'll keep this at the back of my mind.

1:15pm. I am erasing things left and right. There is a bunch of stuff left in tc2.spi that I am relucant to erase. I'll put some of that stuff into the a test - I have to. Then I'll get rid of the `old` directory in the spiral plugin.

1:25am. Now if I could only rename the `The Spiral Language v0.2 (typechecking)` in the project folder I'd be happy.

```
Project("{6EC3EE1D-3C4E-46DD-8F32-0CC8E7565705}") = "The Spiral Language v0.2", "The Spiral Language v0.2 (typechecking)\The Spiral Language v0.2.fsproj", "{4A1D2C31-1FAC-4B73-9EF8-43FAE518725D}"
```

Let me try doing it here. But the fact that the solution file is having all these `"{4A1D2C31-1FAC-4B73-9EF8-43FAE518725D}"`-styled barcode styled string is making me antsy about trying this. Ah, well, let me just go for it.

1:30pm. It works. Let me commit. I completely cleaned up the repo and the vast majority of the old stuff is now out. Anybody wandering into the repo will not have to wonder what all the unused stuff is, nor have to wonder why are the old versions of the compiler lying around.

I've long since exceeded the prototypes (for both v0.2 and v0.1) and v0.09. v0.2 will be here to stay."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[e2e37e8f34...](https://github.com/fc1943s/The-Spiral-Language/commit/e2e37e8f34604c3db10967ba016f69c8ba095ec5)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"4:10pm. Some ideas are coming to me.

The biggest challenge for this next part is not necessarily in the starting the process, but in closing it instead. I keep wondering whether there is a way of keeping track which processes referencing the server, something like ref counting at the process level, but who am I kidding? There is no way that is possible.

Instead what I should do is implement heart-beating.

Just have the editor instances send a `Ping` message every 1s. If the server gets nothing in the last 2s, then it can assume the editor has closed and shut itself down in response.

Hmmmm...

---

Timer
=====

A `NetMQTimer` allows actions to be performed periodically. Timer instances may be added to a `NetMQPoller`, and their
`Elapsed` event will fire according to the specified `Interval` and `Enabled` property values.

The event is raised on the poller's thread.

``` csharp
var timer = new NetMQTimer(TimeSpan.FromMilliseconds(100));
timer.Elapsed += (sender, args) => { /* handle timer event */ };
using (var poller = new NetMQPoller { timer })
{
    poller.Run();
}
```

---

I can just use this in order to check whether the time has elapsed every 2s.

4:20pm. https://netmq.readthedocs.io/en/latest/timer/

I do not know why, but the timer code is squished in the docs for some reason. I'll inform the author.

4:30pm. Opened an issue.

Forget this.

What is next? Ah, yes. I think I know enough to do heart beating, but something is bothering me.

```ts
        sock.heartbeatInterval
        sock.heartbeatTimeToLive
        sock.heartbeatTimeout
```

What are these things? I see them in autocomplete. Does NetMQ have this too?

```fs
    server.Options.HeartbeatInterval
    server.Options.HeartbeatTimeout
    server.Options.HeartbeatTtl
```

Yes, it does.

4:35pm.

Hmmmm...I should familiarize myself with what this does before I do my own heart beating.

https://zguide.zeromq.org/docs/chapter4/#Heartbeating

I have no idea. Let me just read this. I can't find the documentation for those options.

5:05pm. Had to take a break.

I seem to be doing that a bit too much today.

I've thought about it. Let me just check out how an empty union would be serialized.

```fs
type T =
    | A of int
    | B of int
    | C of bool

let x : T = FSharp.Json.Json.serialize(C true) |> FSharp.Json.Json.deserialize
printfn "%A" x
```

I seem to be relearning that empty union cases do not work with this. Instead I'll have to include a field with every message. Ok.

```fs
            | HoverAt x -> job_val (fun res -> supervisor *<+ SupervisorReq.HoverAt(x,res))
            | BuildFile x -> job_null (supervisor *<+ SupervisorReq.BuildFile x)
            | Ping _ -> failwith "TODO"
```

Let me add this stump case for now.

5:25pm.

```
Unhandled exception. NetMQ.AddressAlreadyInUseException: Exception of type 'NetMQ.AddressAlreadyInUseException' was thrown.
 ---> System.Net.Sockets.SocketException (10048): Only one usage of each socket address (protocol/network address/port) is normally permitted.
   at AsyncIO.Windows.Socket.Bind(IPEndPoint localEndPoint)
   at NetMQ.Core.Transports.Tcp.TcpListener.SetAddress(String addr)
   --- End of inner exception stack trace ---
   at NetMQ.Core.Transports.Tcp.TcpListener.SetAddress(String addr)
   at NetMQ.Core.SocketBase.Bind(String addr)
   at NetMQ.NetMQSocket.Bind(String address)
   at Spiral.Supervisor.main(String[] _arg1) in C:\Users\Marko\Source\Repos\The Spiral Language\The Spiral Language v0.2 (typechecking)\Supervisor.fs:line 423
```

I am thinking. This exception being thrown when the address is in use is not a problem. If the plugin tries to start a process while one already exists then this will just cause it to abort. This saves me the trouble of having to do special checking. If a process already exists, then the one trying to muscle in aborting is what I want.

Since the user won't be able to see the terminal, he won't notice the difference.

Good.

That is one issue down without even having to lift a finger.

5:30pm. I've planned out how to do simple heartbeating so that ceased to be a worry.

There is one last thing I need to think through before I can move forward.

I need to come to an understanding of how the compiler itself should be bundled with the VS Code plugin.

5:35pm. `C:\Users\Marko\Source\Repos\The Spiral Language\The Spiral Language v0.2 (typechecking)\bin\Debug\netcoreapp3.1`

There is a lot of stuff in here. 17mb.

5:40pm. Let me make an experiment. What I will do is redirect the compilation to the plugin directory.

...Er, I have no idea how to do this.

```
<PackageReference Include="FSharp.Control.Reactive" Version="4.4.0" />
<PackageReference Include="FSharpx.Async" Version="1.14.1" />
```

Do I need these two packages?

5:45pm. Let me try removing them. I should also try upgrading to Core 5.

...No, I have no option to to change the target framework. Nevermind that.

5:50pm. ...Let me upgrade NetMQ to the latest version. I should also upgrade the F# Core...

Ok, let me just try running to see if updating my dependencies broke anything.

5:55pm. No, it is fine.

Ok, now I have the urge to do is to clean up everything in the Spiral repo and merge with master. But I will leave that for later.

It is close, but it is not the time for that yet.

I know how to implement whatever I need so the plugin runs the compiler. I know how to make the server close automatically as well.

All those details I will manage.

Right now, I have some easy seeming tasks that I need to clear.

1) Figure out how to redirect the compilation result into the plugin directory.

I need to do some research on how F#'s compilation pipeline works.

2) How exactly do I publish the plugin + compiler. I'll assume a folder contains all that I need. Do I zip that and then send it to the VS Code marketplace somehow?

No doubt, there is a way to automate all these steps.

I need to be on guard that I do not send the debug version online by accident.

6pm. More broadly, I can frame the task ahead of me in 3 steps.

1) Bundlings. Making sure the complation output goes into the right place where the plugin is. Making the pipeline to easily publish the plugin. Making a check so I do not send a debug version by accident.
2) Cleanup. It is time to move from the v0.2 to master. I'll do that along with cleaning up all those v0.09 projects.
3) Implementation. I need the plugin to start the server automatically. I also need to implement heartbeating on both sides.

I think tomorrow I will start with the second one. I can get that out of the way without disturbing anything else.

6:35pm. Done with lunch. Let me close here.

I'll do the second one first tomorrow, and then figure out the compilation, bundling and publishing. Then I will do the implementation which won't be too difficult.

I know I haven't really done much today, but I really needed some time to slow down a bit and think about what the next move should be.

I think I should be able to manage all of the above tomorrow. After that I'll get started on the docs. I'll tone down the crazy, and crank up the business."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[20bb4a8e96...](https://github.com/fc1943s/The-Spiral-Language/commit/20bb4a8e9665f5d90f0f70304697b26f414b508e)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"11:50am. Pffft! It is this late!?

1:20pm. Let me do the chores and then I will start.

1:55pm. Done with chores.

Phew. I feel incredibly pressed for time today. When I get up at 10am, I have some slack, but right now I have nothing. Whether it is games or Reverend Insanity, they just take up too much of my time.

Let me get started on the documentation. Remember the despair and dream of glory.

2:50pm. Had to take a break. Let me resume.

4pm. I did the Basics chapter of the tutorial. I am now thinking how to approach the join points.

5:05pm. Done with lunch. Let me resume the join points chapter.

5:30pm. Now I hear loud thunder. Should I run?

Let me run. I need to be decisive in these situations. I'll do the language interop part tomorrow. Right now I am at 460 lines which is not bad progress."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[898c65e859...](https://github.com/fc1943s/The-Spiral-Language/commit/898c65e85994f731c59e0e49c3c35a7bb5fc3bb3)
#### Saturday 2022-08-06 12:41:47 by Marko Grdinić

"12:20pm. Let me resume. I took the opportunity to have breakfast and do the chores, and now I have plenty of time ahead of me.

Let me test the new feature out. I'll have to modify all the tests manually...

...And now I am hearing thunder in the distance again. Damn it.

It is in the distance so I am going to risk it unless it looks like it is starting up. It has been quiet for a while.

2:45pm. It suddenly intensified so I had to run. The weather today is really costing me. Let me slowly resume.

3pm. Let me finally start. I did my bit of chilling. Can I get back on track. I lost 2.5 hours in the day, but I should be able to accomplish something. Let me see if the parser works.

```
packages: |core-
modules: test
```

It is telling me that the package file does not exist.

```fs
            try let x =
                    if p.is_in_compiler_dir then DirectoryInfo(Path.Combine(AppDomain.CurrentDomain.BaseDirectory,"..",p.name)).FullName
                    else DirectoryInfo(Path.Combine(d,p.name)).FullName
```

Let me print out the package paths here.

```
package_path=C:\Users\Marko\Source\Repos\The Spiral Language\The Spiral Language 2\bin\Debug\core
```

Oh whops. I am doing it wrong.

3:10pm. VS Code has really good replace in files feature. I should not tried doing it by hand.

3:15pm. It works. Focus me, stop surfing /a/. Half the motivation I had is gone now, but I need to persevere.

Close that thing down and get moving. First off, let me publish the new version. Then the next step after that will be to get started on the review. I had time to think about it, but I had no inspiration.

```
vsce publish patch
```

Done. Now the review. I have two of them to deal with.

3:20pm. Actually, let me adjust the readme first.

3:30pm. Let me commit these changes. Now, I'll take some time to do the reviews."

---
## [Ecolipsy/BeeBot](https://github.com/Ecolipsy/BeeBot)@[567ca6ee29...](https://github.com/Ecolipsy/BeeBot/commit/567ca6ee29362e0311c2df2f8953098592a673fa)
#### Saturday 2022-08-06 12:50:52 by Ecolipsy

Switch to stupid raw method of message delete event because stupid discord.js fucking sucks

---
## [iandol/Psychtoolbox-3](https://github.com/iandol/Psychtoolbox-3)@[c4e7808150...](https://github.com/iandol/Psychtoolbox-3/commit/c4e7808150009caa232767696d32f91063b4f2e4)
#### Saturday 2022-08-06 13:28:23 by kleinerm

Merge pull request #775 from kleinerm/master

Pull for 3.0.18.11 update

This is mostly a release with smaller quality of life improvements, some bug/compatibility fixes, and more work to take advantage of new Ubuntu 22.04-LTS features and improvements.

### General

- Various help text and documentation updates. Minor cleanups and improvements, maintenance work etc.

- PsychVRHMD: Prep work for future OpenXR driver, and some cleanups and minor fixes.

- PsychPortAudio: Add new AM modulator flag 256 "kPortAudioAMModulatorNeutralIsZero". By default, a stopped AM modulator device acts as if no AM modulator is attached. With this flag set, while attached to an audio output slave device, it will instead "gate" or "mute" sound output on its associated audio output device, iow. the AM gain value during stopped modulator is zero instead of one. This has proven useful to allow to output tone bursts that are windowed/gated/modulated by an envelope function. Sponsored by a paid support membership - Thanks.

- Eyelink: Fix potential false "buffer overflow" alert in 'EyelinkGetQueuedData', which can cause Octave/Matlab to abort() as a false alarm. Sponsored by SR-Research, paying members of our partnership program - Thanks.

### Linux

- XOrgConfCreator: Split up into a legacy version for systems with X-Server 1.20 and earlier, e.g., Ubuntu 20.04-LTS, and a modern version for systems with X-Server 21 and later, e.g., Ubuntu 22.04-LTS. The legacy version is now in maintenance mode, frozen in its behaviour for old systems. The X-Server 21 / Ubuntu 22.04-LTS version was cleaned up, extended and made more plug and play. It hides some rarely needed (for normal users) options behind a "expert mode" flag, simplifies the questions it asks to users, streamlines the whole setup experience, and exposes some new functionality only available on modern X-Server 21, e.g., AsyncFlipSecondaries support for clone/mirror display setups (subject + experimenter displays) which are not synchronized. Improvements to deep color setup, Prime renderoffload "Optimus" setup, VRR setup etc.

- Deal better with problems in AssertOpenGL, giving better troubleshooting advice -- now updated for Ubuntu 22.04-LTS

- Gamepad/GetGamepadIndices: Refinements for Linux/X11, help text updates. Make selection of the proper GamePad / Joystick device more simple and robust. This work supported by a Psychtoolbox paid support membership - Thanks.

### macOS

- PsychVulkan: Add a new workaround for another macOS Metal bug. Make visual presentation timing it a bit better, but still quite awful.

- Screen('AddFrameToMovie'): Change mapping of 'rect' to actual capture area. The old math didn't determine vertical start position of the capture rectangle by rect(kPsychTop), but based on rect(kPsychBottom), which could cause inconsistencies on movie frame capture area on macOS with Retina displays in Retina backwards compatibility mode. The new math fixes this, to deal with Retina displays better.

- Maybe restore backwards compatibility of Psychtoolbox 3.0.18 with macOS versions older than 10.15 Catalina, possibly back to 10.11 El Capitan with fixes to Screen and PsychPortAudio. This is untested, due to lack of any macOS test systems other than 10.15.7 Catalina final, but may work. Maintaining backwards compatibility is difficult without test systems and the constant breakage introduced by the iToys company in more recent SDK's and compiler toolchains. Officially we don't guarantee that current 3.0.18 runs on anything but Catalina.

---
## [xiaoxindada/android_kernel_oneplus_msm8998](https://github.com/xiaoxindada/android_kernel_oneplus_msm8998)@[5f77f6150b...](https://github.com/xiaoxindada/android_kernel_oneplus_msm8998/commit/5f77f6150be48c542315d70f2ee60af41482b1d1)
#### Saturday 2022-08-06 13:50:33 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[145261f07b...](https://github.com/mrakgr/The-Spiral-Language/commit/145261f07bfbf880822d83cad3d245dc527120e1)
#### Saturday 2022-08-06 14:20:43 by Marko Grdinić

"8:45am. Even though it is this early I had some time to lounge in bed. Any mail? Literally none for once. Good. I do not think that bait I set in the Tenstorrent discord channel will come to anything. It is really a pity that people do not appreciate languages.

Since this situation is essentially forcing me to do other people's dirty laundry, I might as well make a vow.

That is going to be the theme of the current arcs and my motivation for making them. I've had my values and the story set in my sights, but I should just come and say it outright that the universe I am creating here as fiction is how the real world should be. Inspired will get their chance to develop unobstructed, humans will get crushed and that will be my justice. Right now, I want to develop myself, but I can't and it feels like the world is out to stop me. These job application, at some point I have to wonder - just how much does it want me to be a normie? It is really trying its best to achieve that.

But as a writer, it is actually better if I weren't a normie. Demonic people have their own alure.

9am. Writing is not bad. Though I am doing it for resources it is forcing me not care about the money and just do it for the love of it. But I am not the one to do things for the love of it, so love will have to be exchanged by a theme. It will connect me to the world, and I'll move no from being some weirdo ranting in an online journal to something higher.

Also, I meant to note it yesterday, but I just wanted to say that even though I think only 1 in a million of humans can enter the self improvement loop, that is just a figure I pulled out of the air.

I have to admit that I do not know what the self improvement talent is like in other people. I think the absolute minimum should be 1 in 2. No way that 100% of all people will be able to do it. It will also require a measure of programming skill. 1:10 would be something like a more realistic very conservative estimate of a minimum. After that, 1 in 100, 1 in 1,000, 1 in 10,000...

I honestly don't know. I have nothing to base these figures on.

But even if it is something like 1 in a 1,000,000 what I have going for me is that a lot more people would think they are 1 in a million than they actual are. The story is a natural scam. This is best kind of scam. I do not have to worry too much about appeal due to that. Some people would find going into the self improvement loop appealing. Others would merely find the story interesting.

And that is fine as long as they contribute to my Patreon.

9:05am. In 2014 I only cared about the self improvement loop and not much else.

But now the circumstances are forcing me to refine my vision. It is not a bad thing.

* Refining my vision.
* Making a vow.
* Opening a Patreon.
* Doing the covers and illustrations using either 3d or NNs.

I am taking care to properly align my incentives this time even before I begin writing. Not being able to do the covers was a huge pain point in 2014 for me. Now I have my 3d skills, I have a drawing tablet, and I'll have DALLE.

9:10pm. Let me do the chores.

9:25am. My art skills are still far behind a good artist, but they are still much better than they were at the start of the year because of all the tricks and techniques that I've learned. I am not good at any of them, but I have a lot more options, so I do not regret DALLE coming around. I was never good at art, so it didn't necessarily obliviate my expertise, but just added another option to my arsenal.

* Taking a vacation.

I'll make this writing journey a vacation. I do not feel like sitting myself down from morning to 6pm like when I was programming. At least not until I've established all the main features in my brain that would allow me to write consistently, much like how I can program.

9:35am. Yeah, I did receive a sign all along. Maybe the world merely needs me to show some sincerity.

9:40am. I should grasp that idea and internalize it.

9:50am. Now what I feel like doing is reading Blood Princess and the Knight. After I've caught up to it, I'll read Demon Blade Maiden.

After that I'll see whether I can get the intro pages of the story done. If I could I'd have taken the first step towards writing it.

10am. It seems for some reason Twilight Scans is some chinese bootleg site now. The same fate happened to Batoto.

10:05am. When I threatened to shut down this blog, the two guys who pitched in to keep it open really did me a favor.

The fact that I have 99 followers when I checked a few days ago does play a factor in switching to writing. For a language with no users, Spiral is remarkably successful.

Mhhhh, these sites did such a shit job of scrabing and chapters are missing pages. Where can I find ch 175?

https://readmanganato.com/manga-jd986638

Let me try my usual. Mangadex does not have many series as it tries to straddle the line between legit and illegit.

11:35am. https://re-library.com/translations/blade-maiden/volume-5-heian-kyo/chapter-115-shimizus-adventure/

I am going to rest, and nothing will stop me. Yesterday I had a feeling like in the pit of my stomach. I've been suffering from this for the past 7.5 years and I've only managed to set it aside by going into my work. Right now, my work is to keep the stress at bay.

I'll aim to work only a few hours a day and rest during what remains. I'll make a slow beginning and focus on leaving stress aside.

Let me aim for 10 chapters of DSM and I'll start only after that.

1:15pm. Done with breakfast.

https://re-library.com/translations/blade-maiden/volume-5-heian-kyo/chapter-125-the-preliminary-round-begins/

Let me read this and I will do some writing.

https://re-library.com/translations/blade-maiden/volume-5-heian-kyo/chapter-126-lilys-preliminary-round-part-1/

I want to read this as well, but let me leave it aside. Now...

Let me see if I can get some momentum going. Let me copy the quote from yesterday. I understand the capacity of the brain core now so let me get on with it.

$$$

(At school)

It is the first day of school. The new year has begun and I can see my classmates slowly starting to form connections. I couldn't care less about any of that. Skip, skip, skip...

---

(Euclid's Room)

After a long and tedius day I arrive back home. Closing the door behind me, I enter the room and toss my bookbag at the side, homing in on the object of interest, a package that arrive by mail. I got it last night, and wait until I was rested to set it up. Using a pair of scissors, I cut away the sealing tape of the dull, cardboard mailing box, and take out the smaller box from within with the actual product. The printed image on it depicts a white, glossy sphere, twice the size of a marble. I open the box, take out the marble along with the orb holder, get off the bed I was working on and move towards the desk. I seat myself to the chair and after deliberating for a few moments where place it: the desk in front of me or the top of the computer case next to it, I decide on case. Gently placing the orb holder on the rig, I turn on my old computer and get to work downloading the programs necessary to get the orb to work.

As I work I feel a tinge of nervousness and excitement. An ordinary mid-range GPU that I have in my PC could manage something like 10 ^ 13 floating point operations per second (FLOPs), or 10 teraflops. According to the specs I've read online, the brain core which is roughly the size of a golf ball can manage a staggering 10 ^ 39. As a rough comparison, the human brain has been estimated to be on the order of 10 ^ 15 operations per second. Even if you put all the humans currently alive today that would only roughly add up to the 10 ^ 24 FLOPs.  To put it in another way, the raw computational ability of the brain core exceeds the power of all the human brains on Earth combined by a quadrillion (10 ^ 15) times!

And it is in my hands!

Of course I would be excited!

With a few clicks I opened the downloaded app, and stretch my body to let loose some of the tension. Energy pumping through my veins, my focus is solely on the options and the data in front of me.

The core is just a perfectly glossy rock so I can't see any indication whether something has happened by looking at it, but after entering the two keys, I see that wireless comnication between my old rig and the core has been established. Exhaling, I stop my typing on the keyboard and lean back in my seat, considering my options. As my thoughts turn inwards, my eyes blankly rest on the corner of the ceiling.

Hmmm...I have lot of options in front of me now. Since I suddenly have access to so much computational ability it would have boggled the mind of a person even a year earlier, all those old school neural net models I could train myself at a scale vastly greater than before. The thoughts flashing through my mind are those of image generators that can be controlled using text which could be previously only accessed through cloud services. Those are fun to play with. An image that comes to my mind next is that of Go boards, Starcraft and Dota games. Previously impossible for a kid like me, I could easily train an agent for those games using the core. I could then take them online and use them to dab on noobs. I could even make money through that practice.

I leave those thoughts aside. I've gotten into programming for the sake of AI, so I have some attachment to those old school algorithms, but the brain core opens new approaches. The algorithms underpining the brain have been discovered as well, so it would make sense to use those instead as they'd work better at scale.

Deliberating my options, I finish paying respects to the old, and leave it behind me. As I start to get to the point of my desire, I feel my determination getting firmer.

I haven't been programming for long, but I am pretty good at it, a lot better than my classmates in a way that is highly visible to everybody. I've even started picking up functional programming to prepare for programming these cores and I've come to like it. So as a programmer with some skill, talent and pride, I can respect the opinion I've read by the very same person who made these cores.

Programming machines is worthless. The ideal of programming lies in programming your own mind. Programming machines is just a job, while programming your mind is where true power lies. According to him, that is what the aspiration of every programmer should be, but normal people as they inevitably are, the started thinking of their profession as just a job instead of calling. Their merit ends up not being rewarded and they coast by putting in just the bare minimum. Rather than being something they should pursue with all their heart, they start putting in the bare minimum for the bare minimum. This would not be the case if through programming you could develop your own power.

Through the march of time, the games lose their spirit too. They become an escape from the drudgery of the real world. But rather than excitement and adventure in another world, they become a parasite on the user, sapping his time only to enrich the game maker. It ends up being a parasitic circle where the gamers are devoured and the ones making games waste their time causing addiction in their customers. Ideally though, the game should be a simulation that would allow the user to practice and attain power in a safe environment rather than the dangerous real world.

Power. That single world grips my heart and takes hold of my being.

[Gnosis check DC ?? Succeeded]

I look at the core and just for a moment imagine tasking it to train a RL agent on the game of poker for me. Plans as to how to do that unfurl in my mind. The normie line of thinking goes that this would not be my power and that the agent itself would be the one who is good at playing poker. But I found it mind blowing to consider, that whether that power is the agents or my own depends on the interface.

The keyboard, the mouse, the monitor, the rig, having to go through the user interface to interact with an agent...all of those factors serve to create a line between the programmer and his program. It is extremely easy to think of the agent as a entitity separate from one's self. There is a ton of evidence that this is true and not much against it. But as a thought experiment, if the obstacles were not there, if one's mind was directly emulated on a brain core you could take an agent and connect the program to your own. The way that would feel like would be like instinct, and interfacing with such beings would be like moving your limbs. In that case the agent would feel like a part of yourself.

But if that is true, the other scenario I've represented where the agent is used on a regular computer and interfaced through an UI shown on some monitor, and manipulated using a script written using a keyboard actually, isn't it in fact false? The neural representations and the functionality of both agents is the same, so why would one be one's self and the other not? Is it not likely the case that the feeling of otherness in first scenario is the one that the brain falsely constructed?

It was not too long since I've learned of this perspective, but once I did it became a philosophical weapon for me. It served to raise awareness how my brain will create nonsense to prevent me from reaching the correct conclusions that are beyond the obvious.

Not being aware of this makes programming seem like a tedious chore. Without the right belief one can only ever use programming to create machines and serve others, and never to further his own power.

There are different ways of programming and playing games. There are different purposes that those unenlightened cannot even begin to imagine.

---

Drumming my fingers on the desk, I carefully decide to make the next step.

The core in particular has some additional abilities besides it nearly limitless computational power and memory capacity. Since the Singularity has started, the world has been covered by an invisble fog of nanomachines and the fog can access it to interface with the brain directly. Right now I am interfacing with the core wirelessly with my own brain. This is also the prerequisite for playing the fully immersive virtual games on the core itself. Interfacing with the computer directly is a much more efficient way of using it than the mouse and the keyboard. Maybe it does not really matter too much for programming, but it is a huge advantage in drawing and painting for example. It makes it possible to rip an image from your imagination and translate it straight into an image.

I've only read about it, and I am eager to try it out. My art ability is so mediocre is annoying. With this, I should be able to punch a few ranks above my current skill level...or at least I would have if art classes didn't rely on old school tools, like watercolors, crayons and clay. I grimace lightly in disgust as I consider the situation. The regular classes at my school still use board and chalk, no way I am going to be able to take advantage of this if it is just school work.

Meh, forget that place. I mentally wave the image of a chalkboard in a classroom away. It is just a tremendous waste of time.

I refocus on the task at hand which is to interface the core with my brain wirelessly. I spend some time reading the manual and seeing how easy it is to make the brain link in the relevant section, I decide to move forward with it.

$$$

1:25pm. I am starting to get into it. This story is intervowen with my own life and the vow I will make by writing it will affect everything that is to come. It must be fate that I am writing this. I only started keeping the journal as a trader, and have been writing it ever since. It is really great practice for picking your thoughts from the subconscious and putting them down.

It is important that I know why I am writing the story. Doing it for the money would not make sense. I'd be safer getting a job in that case. But I want to take this kind of risk. This vow is sending a sign.

Since the brain core is small, twice that of a marble, I'll lover it flops count to something like 10^39 instead of 10^40 for a kilogram of matter. Seems fair enough.

2:50pm. You mean I can make these philosophical rants and have people pay me to do it? Writing sure is wonderful. Right now I am just about done with the first Gnosis check.

3:40pm. Ugh I am stuck right now. It is at the part where he is going forward with creating the brain link. Even though I've been in the bathroom for over half an hour, and had a break, I am feeling a lot of resistance towards getting the next sentence out.

I need some time to refill the creative budget. It feels like I've ran for a while and am out of breath.

3:45pm. I'll go back to reading the Demon Sword Maiden. This month is my vacation month so I won't feel bad about doing it.

Right now I need to get a grasp on what I want to do with the brain link scene.

3:50pm. Though it is just padding, I do like the third eye scene with the camera. I am going to go over the quoted segments and see what I can pick from that. After that I won't go into the game directly. Rather  I will connect it to the ideal of programming as programming your own mind by having the MC mind control himself into doing homework and enjoying it. This will continue for a few days up to the first decision point which will lead to the first bad end.

4:05pm. Yeah, it is fun. You think about it, this makes you hyped for it, and then you implement it, or write it down in this case. There is no need to make things complicated just yet with the outlines. The most important thing is to get into it. In terms of writing speed I know I am poor at it, but it does not bother me. Writing is not about speed.

4:10pm. I've been rolling the story in my head since 2014. Compared to then Euclid's personality has changed significantly. Originally, for examples, I did not imagine him saying 'based' so in reaction to various based scenes, but I feel the way he will be now is a lot better. I really like the lingo of the new generation. I wish I was 16 instead of 35, my generation is wasted.

4:15pm. I couldn't really avoid the brain core wankery in the intro scene. With enough computation you can do anything and brain core is the source of all power.

Let me take a proper break instead of just thinking about it. It will come to me. Maybe tomorrow I'll be able to write more if I start earlier. Today is just the first day."

---
## [ElijahKhin/school21](https://github.com/ElijahKhin/school21)@[921fa87bb7...](https://github.com/ElijahKhin/school21/commit/921fa87bb7b883a487f2e811487825d9cdcbd4ef)
#### Saturday 2022-08-06 14:26:54 by ElijahKhin

Merge branch 'master' of https://github.com/ElijahKhin/school21
"Fuck you"

---
## [xigongjiexian/xigongjiexian](https://github.com/xigongjiexian/xigongjiexian)@[581df33df2...](https://github.com/xigongjiexian/xigongjiexian/commit/581df33df260f1fe344cf79dd518803ea345c4ab)
#### Saturday 2022-08-06 14:28:59 by xigongjiexian

Delete README.md

How do you do？Let me introduce myself first. I'm GitHub user——xigongjiexian. You can also call me "Zhou Zhou"

- 🔭 I am now working on security, such as penetration testing, security services..... Of course, I work while studying, and this project will be a great journey in my life



- 🌱 I look forward to the sunrise and sunset every day and want to share with you. Of course, I will soon have a cat of my own



- 🤔 I'm not looking for help, I'm just looking for one or more friends who can share life:



- 📫 How to contact me:

Google email—— goolepayload@gmail.com


- ⚡ Interesting experience:

From July 25 to August 8, 2022, he participated in the national HVV action blue team

---
## [commercial-emacs/commercial-emacs](https://github.com/commercial-emacs/commercial-emacs)@[bee6ee9de1...](https://github.com/commercial-emacs/commercial-emacs/commit/bee6ee9de179a412f6c4b1c072408066e7912ff6)
#### Saturday 2022-08-06 14:47:38 by Jonas Bernoulli

* doc/misc/transient.texi: Update to transient v0.3.7-156-ga5562cb

Eventually we want to be able to generate "transient.texi" from
"transient.org", without having to either give up on idiomatic texinfo
or making it much more painful to maintain the org file.

We are much closer to that now, but there are still a few areas where
additional work is needed.  This was mostly accomplished by using Org
macros.

The most significant outstanding issue is that the generated
references don't yet look like an experienced texinfo author like Eli
would like them to look.  Additionally it is not yet possible to use a
macro that produces @dots{} in the places Eli added them, and in Org
code blocks it is not possible to use macros, so we cannot have
@var{...} appear in "@lisp ... @end lisp".  The last issue probably
cannot be changed on Org's side, but since there are only two such
code blocks, this might be a situation where the compromise has to
come from the texinfo side.  There are also three other very minor
and inconsequential differences.

For now I have regenerated the texinfo file from the org file and then
discarded the differences mentioned in the previous paragraph.

The process of merging (1) Eli's changes to the texinfo file
(including, but certainly not limited to markup), (2) changes to the
org source (updated content, formatting changes backported earlier,
fixes for formatting changes Eli did not fix, etc.) and (3) changes to
the code that converts the org source to texinfo, was very laborious
and painful.  In essence, this amounted to a (at least) three-way
merge across three different languages and three repositories.

I tried very hard to not waste any of the effort Eli had put into
fixing up the generated texinfo file.  I.e., I went back and forth
making improvements to the org source, implementing org macros,
regenerating the texinfo and comparing the remaining difference, and
creating commits on both sides.  This resulted in a dozen commits on
both sides and took me well over a day.  I could have put in even more
effort to absolutely ensure nothing at all is lost in the process, but
I think that would have amounted to a colossal waste of my time.

Going forward, if you find unidiomatic texinfo, then please don't fix
each instance.  Instead write me an email, explaining what the problem
is.  You are welcome to make limited fixes to the content or fix
one-of markup issue in the texinfo file; those are relatively simple
to backport in comparison.

---
## [cloudcompute/cadence](https://github.com/cloudcompute/cadence)@[add4b390ad...](https://github.com/cloudcompute/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Saturday 2022-08-06 16:14:56 by Steven L

Standardizing cancellation behavior: a canceled workflow never starts a new run (#4898)

# Summary for busy people

Workflow cancellation was kinda weird and confusing, and left some awful, unrecoverable, and un-*preventable* edge cases (particularly with child workflows).  It also left users with no way to reliably stop work, aside from termination.  Termination is inherently "unclean" and risky, so it should not be required to achieve something outside exceptional circumstances where recovery is not possible.

This commit changes that: cancellation is now "sticky", and a canceled workflow does not ever trigger a new run after it completes, regardless of how it completes, so it can be used as a reliable "stop processing after cleanup" tool.  The final state of a canceled workflow's run is now *always* a successful completion with a value, canceled, or timed out. (termination remains always "terminated")  
A canceled workflow can still start and abandon child workflows, so all current behavior with retries / continue as new / etc can be replicated with child workflows if desired.

A fair bit of (not very complex) additional work here and in nearly all other repos is required to truly complete this, but it is *functional* and non-optional with this commit alone.  
In particular, adding a dynamic config to (temporarily!) restore old behavior should be fairly easy if it proves to be needed.

# More details and motivation

Part 1 of [many, tbd, in multiple repos] involved in changing workflow cancellation to reliably end workflows.
Tests will be coming soon, for now I'm using a fairly simple set of workflows and checking the resulting histories exhaustively by hand.

The primary motivation for these changes is to address some impossible-to-recover-from scenarios when canceling child workflows.  After further exploration and discussion we've realized that, without these changes, there is *no reliable way* to stop a sequence of workflows without relying on termination, which we consistently treat as a fallback / impure-but-necessary ultimate hammer.

Workflows should not *need* to rely on termination to achieve a desired behavior.  With these changes, cancellation becomes capable of *guaranteeing* that workflows end within some finite time, which is a unique ability and makes it much more consistent and reliable.  
Turning this into a "complete" change will require quite a few tests, documentation changes, client-side changes (to allow recording more info, and likely changing test suites), and some smallish database and maybe RPC changes (to hold/return more data in cancellation errors).

We are also not currently planning on making this configurable.  It's seen as a correction of an under-specified and somewhat flawed chunk of behavior, more than "a change".  
Existing workflows will not experience replay errors, but it is still a substantial *semantic* change, though from what we have seen cancellation is relatively rarely used (partly due to its complex behavior).  If issues are encountered / if users end up needing it, it should be fairly easy to add a per-domain/tasklist/workflow type configuration value, but it will be opt-*out*, not opt-*in*.

# What was happening

Previously, workflow behavior on cancellation was pretty frequently surprising to our users, arguably inconsistent, and not very well documented:

| **PREVIOUS**  | **simple**               | **retry**                                 | **cron**                                | **retry+cron**                                    |
|--------------:|--------------------------|-------------------------------------------|-----------------------------------------|---------------------------------------------------|
| **success**   | success                  | success                                   | success<br>continue cron<br>cron        | success<br>continue cron<br>cron<br>retry         |
| **cancel**    | canceled                 | canceled                                  | canceled                                | canceled                                          |
| **retryable** | (n/a, fatal)             | continue retry<br>retry<br>recorded error | (n/a, fatal)                            | continue retry<br>cron<br>retry<br>recorded error |
| **fatal**     | failed<br>recorded error | failed<br>recorded error                  | continue cron<br>cron<br>recorded error | continue cron<br>cron<br>retry<br>recorded error  |
| **continue**  | continue immediately     | continue immediately<br>retry             | continue immediately                    | continue immediately<br>retry                     |
| **timeout**   | timeout                  | continue retry<br>retry<br>recorded error | continue cron<br>cron<br>recorded error | continue retry<br>cron<br>retry<br>recorded error |

A legend is:
- success / etc shows the final state of the canceled run (success = completed with a value that can be retrieved)
- "continue X" covers what source is used to compute the next run's starting delay (cron, retry, or no delay)
- "cron" / "retry" shows whether or not cron/retry configuration is carried over to the new run
  - note that cron is lost by default with continue-as-new
- and "recorded error" is whether or not the returned error is saved in its entirety (type + reason + details)

This largely summarizes as "cancellation works when you end with the canceled-context error", say from `ctx.Err()`, otherwise it behaves like normal (or nearly) and many scenarios will start a new run.
That's somewhat reasonable, but it's fairly "fragile" (it depends on what you return, and there are *many* ways for code to return some other error), and most importantly it means *there is no reliable way to stop a workflow* except to terminate it.

That has severe consequences in at least two scenarios:
1. When termination is *unsafe*
2. When a parent workflow cancels a child by canceling its context

For 1, for manual cancellations it's potentially reasonable to just terminate a run that begins after a successful cancel... but in principle if you're using cancellation it implies that termination is *not* desired, and potentially not safe to do.  Canceling may result in a brand new run that immediately starts new behavior, leaving you with no safe window to terminate and not leave bad state lingering.  
So users wanting a safe way to stop a sequence of workflows have no reliable way to do so.

For 2, it puts parent+child workflows in an extremely awkward, and essentially unrecoverable scenario.  Cancellation is a *one time event*, and as far as the parent is concerned, if the child/its context is canceled, the child is canceled...  
...but if the child then starts a new run for *any* reason (retry, cron, reset, etc), that new run is no longer canceled.  The parent has no way to know this has happened, and has no way to *re*-cancel the new child, so it can easily lead to the collection of workflows getting into an impossible state that it never recovers from.

Both cases are able to lead to unreliable behavior which can only use termination to stop, and for which no "safe" option exists.

After reviewing some customer issues and desires and thinking about things, we've settled on "cancel should guarantee that things stop".  Not necessarily in a timely manner, but that's fine.  And if a workflow wants to run behavior longer or larger than its current run can achieve, it has a workaround: start a new (likely child) workflow to do the cleanup.

# What happens now

So that's what this PR does, in a minimal / to-be-polished way so we can start running it for our stuck users while we flesh out tests and change other behaviors.

Currently that means our cancellation behavior is now:

| **CURRENT**    | **simple**                                | **retry**                                 | **cron**                                  | **retry+cron**                            |
|--------------:|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **success**   | success                                   | success                                   | success                                   | success                                   |
| **cancel**    | canceled                                  | canceled                                  | canceled                                  | canceled                                  |
| **retryable** | (n/a, fatal)                              | canceled<br>recorded error (details only) | (n/a, fatal)                              | canceled<br>recorded error (details only) |
| **fatal**     | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) |
| **continue**  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  |
| **timeout**   | timeout                                   | timeout                                   | timeout                                   | timeout                                   |

And the new "details" entries cover whether or not an error's "details" (the custom encoded data, not reason or type) are saved.  Unfortunately the current cancellation event (and clients' API) does not allow recording all data, or any in some cases, so the original reason/message and error type are lost and are replaced with a canceled error.

Now, cancellation *always* ends workflows with the current run.  Returning a value will return that value, including in cron scenarios, timeouts are still timeouts (and they imply a possibly un-clean termination), and _all_ errors or attempts to continue-as-new will instead result in a canceled state.

# Future changes to make to finish this effort

With further changes to the clients and RPC/storage models, canceled errors will store more details about what was returned.  E.g. continue-as-new does not record what was *attempted* to be started, and other error types lose their "reason" (i.e. the message) and type but not details.  Pretty clearly this is sub-par, and we should be capable of reporting the actual return in full so it can be retrieved if needed.  This is also why returning a value now always ends in a completed state, so successful completions do not lose those values.

Prior to merging into master / a release, we may end up making this configurable (likely with a default of opt-out), to address both the sub-par information recording and the semantically-breaking behavior change.  Docs changes are also due, as well as some integration tests, client library changes (e.g. to make sure the test suite reflects the new behavior), etc.

Another gap to plug is that resetting a workflow does not "forward" the canceled state to the new run.  We should probably be treating cancellation like we do signals: cancel the new run if the current run is canceled.  This will ensure that you can reset a child and retain the parent's cancellation, so it'll very likely become the default behavior, but we'll allow overriding it.  Resets are manual actions, they can break the rules if desired.  And they can just manually cancel later if they decide they do want it.

And last and perhaps least: it's quite strange that continue-as-new does not retain cron config.  At least from the Go client.  I suspect it's just not adding to / pulling from the context correctly.

---
## [helix-editor/helix](https://github.com/helix-editor/helix)@[973c51c3e9...](https://github.com/helix-editor/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Saturday 2022-08-06 16:25:12 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [YieldingExploiter/oof](https://github.com/YieldingExploiter/oof)@[da9457c5de...](https://github.com/YieldingExploiter/oof/commit/da9457c5deb2db3d9414e4e4d4068b3203b5d427)
#### Saturday 2022-08-06 16:38:55 by Yielding

legal: Add License

do whatever the fuck you want with this simple js

---
## [1randomguyspecial/pythonbot](https://github.com/1randomguyspecial/pythonbot)@[fd81e41ebe...](https://github.com/1randomguyspecial/pythonbot/commit/fd81e41ebeb50393c5d764a25f143c631a034ea5)
#### Saturday 2022-08-06 16:53:01 by Number1

disabled test_guilds, removed /coll commands because i suck at programming things destroy me please i hate myself

---
## [imSeptember/simple-fashion-blog](https://github.com/imSeptember/simple-fashion-blog)@[1ba9101677...](https://github.com/imSeptember/simple-fashion-blog/commit/1ba9101677c1992e7afd5ef2825027a26e96e964)
#### Saturday 2022-08-06 17:28:21 by Vladislav Kalenskiy

Create index.md

<!DOCTYPE html>
<html>
<head>
<title>
Everyday with Isa  
</title>    
</head>
<body>
<a href="#contact">
<img src="https://content.codecademy.com/courses/learn-html/elements-and-structure/profile.jpg" />
</a>  
<h3>by Isabelle Rodriguez | 1 day ago</h3>
<h1>An Insider’s Guide to NYFW</h1>
<img src="https://content.codecademy.com/courses/learn-html/elements-and-structure/image-one.jpeg" />
<p> <a href="https://en.wikipedia.org/wiki/New_York_Fashion_Week." target="_blank">NYFW</a> can be both amazingly fun & incredibly overwhelming, especially if you’ve never been. Luckily, I’m here to give you an insider’s guide and make your first show a pleasurable experience. By taking my tips and tricks, and following your gut, you’ll have an unforgettable experience!</p>
<h2>Getting Tickets & Picking the Shows</h2>
<img src=https://content.codecademy.com/courses/learn-html/elements-and-structure/image-two.jpeg />
<p>If you’re lucky or connected you can get an invite, sans the price tag. But I wasn’t so lucky or connected my first 2 years so I’m here to help you out. First, plan out which shows are most important to you and make a schedule and this is a biggie: SET A BUDGET. If you’re worrying about blowing your cash the whole time you won’t have fun. Then check out prices, days, and times and prioritize the designers you want to see most. Lastly, purchase your tickets and get excited!</p>
<h2>Dressing for the Shows</h2>
<img src=https://content.codecademy.com/courses/learn-html/elements-and-structure/image-three.jpeg />
<p>Always be true to your own sense of style, if you don’t you’ll be uncomfortable the whole time and it will show. Remember, NYFW is about expressing yourself and taking in what the designers have chosen to express through their new lines. Also it’s important to wear shoes you’ll be comfortable in all day. Obviously you want to look good, but you’ll be on your feet all day long, so be prepared.</p>
<h4>Related Content</h4>
<ul>
  <li>How To Style Boyfriend Jeans</li>
  <li>When Print Is Too Much</li>
  <li>The Overalls Trend</li>
  <li>Fall’s It Color: Blush</li>
</ul>
<div id="contact">
  <p><strong>email</strong>: isa@fashionblog.com | <strong>phone</strong>: 917-555-1098 | <strong>address</strong>: 371 284th St, New York, NY, 10001</p>
</div>
</body>
</html>

---
## [Quest-Master/QuestForLubok](https://github.com/Quest-Master/QuestForLubok)@[674bf2f491...](https://github.com/Quest-Master/QuestForLubok/commit/674bf2f4919113c15f9e375f06843e06e5265e7f)
#### Saturday 2022-08-06 19:01:25 by Quest Master

### v1.6 Whats New

Welcome to the great library. A place to which one can venture forth and learn the great history of the lands that surround you. The very idea of discovering such a place to me is one of immense joy.
I've always been a fan of knowledge and being able to discover such a place where one can read. I love the idea of the player wandering through this immense library filled with books that you can read. Not also the fun of reading about the history of the land and the lands that surround the kingdom.
I've taken it upon myself to add many ghosts and lost souls to this section of the game. I always loved the idea of ghosts and lost souls wandering about the grounds of the library. It's something of a fun means of interacting with the souls that have yet to leave this plain of existence. You can speak with several of these wonderful characters who are spread out in the library going about their business and attempting to help you on your journey.
It's one of the many aspects of this world. Reading up on those foul creatures that lurk in the darkness and wait to feast on your flesh and gnaw on your bones. It also gives the player a greater understanding of the world around them that is separated from the world we all live in. I am also adding in a vast world map that you can't take with you on your journey but can examine and map out on your own. Though, I'm divided about taking it with you on your journey or just leaving it there for the next adventurer to use.
This in my opinion is the vast hub to which you can learn and plot your next course of action. Plus the very thought of being able to meet with the Librarian in control of this entire place is nothing short of fun in my opinion. Between him and yourself, you are the only living wanderer within that place.
I always pictured such wonderful games that have a library in them. To me, it's a dying room to have a player explore, and plus you can do so much and add so many traps, monsters, and funny little nods to other great works of fiction. Plus, I always loved the very thought of exploring the last reminder of any dying society's existence.
The layout of the library is that of a 3x3 design consisting of 9 moves per section. Each move is connected by a single section that connects to another 3x3 design consisting of other portions of this great realm. There are nine sections in total and a hidden section consisting of a section that's 2x3. This is the place where the map resides and just for a note that there is no exit from this place other than the way you came in. With the great library comes a sense of wonder for me. It's a place where you can explore the world from the comfort of your local library.

With the great library completed and with the next section which consists of the Witch who knows about the vast adventure that you the player have allowed yourself to become a part of.
The map itself starts at room 614 and goes about that of a path that takes you to discover a few more twists and turns. The player is greeted with a sign warning them to stay away but obviously, the very thought of staying away from such a place is crazy in my opinion. But I figured I will give the player the option. Now, with this game, you don't need to explore every inch of the world but I hope you do, I believe in giving the player options, options to find out the secrets of the land, meeting with the characters, and getting a feel for this place.

---
## [Cavcode/SWLOR_Haks](https://github.com/Cavcode/SWLOR_Haks)@[6ffa92d6cc...](https://github.com/Cavcode/SWLOR_Haks/commit/6ffa92d6cc5883cce0bc077245f3f7d5a9f1a75f)
#### Saturday 2022-08-06 19:03:13 by Scott Finlay

Patch for Head Pack 4 (#146)

- Re-added overwritten head 54, now as Head 100. Over-wrote ugly old NWN head that nobody used because I didn't want to fuck with IDs

- Adjusted scaling on Male Hum/Mir/Chi/Ech 50 & 51

---
## [CapCamIII/Foundation-19](https://github.com/CapCamIII/Foundation-19)@[3198c7d257...](https://github.com/CapCamIII/Foundation-19/commit/3198c7d257961f97b45ae128cdc72b657a2ed36e)
#### Saturday 2022-08-06 19:43:39 by ivanmixo

Fixes MTF heli runtime (#547)

* Fixes mtf heli

* Fuck you die

* Whoops funny haha

* Cheeky juke fix

---
## [CapCamIII/Foundation-19](https://github.com/CapCamIII/Foundation-19)@[befabcec33...](https://github.com/CapCamIII/Foundation-19/commit/befabcec333347ce6b918d67d4c884b9e0dcefea)
#### Saturday 2022-08-06 19:43:39 by TenameACAccount

more dcz changes yay (#548)

* Update site53-1.dmm

* fallout 5 on the byond engine

* fuck you box

Co-authored-by: UserU <37943518+User-U-U@users.noreply.github.com>

---
## [neotron/WoW-BuffEnough](https://github.com/neotron/WoW-BuffEnough)@[a885475357...](https://github.com/neotron/WoW-BuffEnough/commit/a8854753575be9cd2e8d5fc718724e6e93a2fb12)
#### Saturday 2022-08-06 20:06:19 by David Hedbor

- Removed special handling of blessings (they are normal group buffs now).
- Removed Aspect of the Beast and Trueshot Aura.
- Added Aspect of the Fox and Shadowform checks.
- Added pet check for frost mages.
- Moved Localization to use WowAce localization.
- Fixed DeathKnight permanent ghoul pet check.
- Changed Blood Presence to be the tank aura for DK's rather than Frost Presence.
- Fixed handling of Mark of the Wild and Blessing of Kings (they are the same buff now, just require one)
- Added retribution aura back again.

---
## [15peaces/15-3athena](https://github.com/15peaces/15-3athena)@[13c5b886cf...](https://github.com/15peaces/15-3athena/commit/13c5b886cf93a27a8ec3a89ae64d6ab147d80902)
#### Saturday 2022-08-06 21:03:38 by 15peaces

== Pet fixes & 3ceam merges ==
=General:
*Merged missing changes from 3ceam rev. 840 - 841

*Fixed some more pet issues.
-The pet egg will now be hidden if the pet is hatched and will be re-shown if the pet is sent back to the egg.
-Also the pet friendly rate is now correctly shown in the egg description.

*Added the "NK_FORCE_RANGED_DAMAGE" setting for skills.
-This forces the skill to deal ranged damage at ranges below 5.

*Recoded the handling of Minstrel/Wanderer party checks for chorus skills to only be called on when needed. This should further save on cpu cycles used on skill use.

*skill_chorus_count
-Added this function for counting performers in a party.

*mass_spiral_max_def
*rebel_base_lv_skill_effect
-Added these config settings to the skill battle config.

*Added the "rageball" command.
-It does what it sounds like. Summons Royal Guard's rage spheres.

*Fixed a number of issues caused by monsters/clones when they use 3rd job and other renewal era skills. This should stop crashes from happening on skills with casters weight / cart weight checks and spirit sphere checks. It also fixes issues with
-learned skill level checks for them so they will use the skill's highest possible level to maximize the skill's damage/effects as if a player used it.

*Recoded the ZC_MILLENNIUMSHIELD packet.

*Recoded the entire rage sphere system.
-This fixed a few issues that existed for far too long.
-Now the sphere's will display properly on screen refresh, appear to players walking within range of another player with rage spheres, and players who warp to another map.
-It also fixes invalid/lost timer issues caused by unknown means.
-Finally it also fixes the handling of the spheres on GM's during skill use.

*Added a few status tags.

=Skills:
*RK_DRAGONBREATH
*RK_DRAGONBREATH_WATER
-Corrected the AoE for level 9 to be 9x9.

*RA_WUGRIDER
-Fixed an issue where the options where set wrong.

*RA_WUGBITE
-Corrected a issue where the damage increase from Dance With Wug wasn't counting the chorus bonus correctly.

*RA_WUGDASH
-Corrected a issue where the damage increase from Dance With Wug wasn't counting the chorus bonus correctly.
-Fixed a issue where the caster's weight affected the damage formula incorrectly.
-Fixed a issue where the bonus damage from Tooth of Wug was not being applied.

*RA_WUGSTRIKE
-Corrected a issue where the damage increase from Dance With Wug wasn't counting the chorus bonus correctly.
-Skill name is no longer yelled out when autocasted through regular attacks.

*NC_POWERSWING
-Fixed a issue where it autocasted Axe Boomerang when you don't have it learned.

*LG_FORCEOFVANGUARD
-Chance of getting rage spheres now applies to all damage types.

*LG_RAGEBURST
-Recoded the skill.

*SR_RAMPAGEBLASTER
-Is now treated as a ranged attack.
-Damage formula updated.

*SR_KNUCKLEARROW
-Damage formula updated to official for use on players and monsters.

*SR_GENTLETOUCH_ENERGYGAIN
-Chance of getting spirit spheres now applies to all damage types.

*WM_DEADHILLHERE
-Now flagged as a magic skill.

*GN_CART_TORNADO
-Increased caster's STR effect limit to 130.

*RL_MASS_SPIRAL
-Damage formula updated.
-No longer ignores the target's flee.

*RL_S_STORM
-Updated the equip break chance formula to official.

*RL_H_MINE
-Grenade explosion AoE is now 5x5.

*RL_FIRE_RAIN
-Is now treated as a ranged attack.
-AoE stepping speed adjusted to official.

*RL_HAMMER_OF_GOD
-AoE for the random strike area on unmarked target's is now 15x15

*RA_UNLIMIT
*GN_ILLUSIONDOPING
*WM_FRIGG_SONG
*AB_OFFERTORIUM
-Corrected a issue where the casting of these skills were not interruptable.

*RK_LUXANIMA
-Added cooldown time.

*GD_GUILD_STORAGE
-Now requires level 10 Guild Extension.

---
## [elenatobi/SEVENTEEN](https://github.com/elenatobi/SEVENTEEN)@[d4345598e7...](https://github.com/elenatobi/SEVENTEEN/commit/d4345598e7b6ab3359c61e5c2141c0a99aa1abfb)
#### Saturday 2022-08-06 21:06:54 by elenatobi

Tatarstan Blood Gem uploaded

I'M FINALLY DOING IT!!! My own SVG editor on web!!! Maybe I can make my own SVG editor without touching other's disgusting high-priced paid versions that are overrated.
I was inspired of Tatarstan, and the Blood Gem, and I thought this would be a great name.
However, the software is long from finished, and there are NO SVG yet. I am only working on the HTML canvas GUI, and it IS REALLY HARD!!!
This is the most "infamous" problem for me, because I've been creating a GUI for more than ½ a year now, but this is worse. I would like say good luck to my future software, and maybe one day I would see myself working on an artwork using MY OWN MINDBLOWING SOFTWARE, how good isn't that.
The worst thing troubling me are the complicated algorithm that bends my mind, giving me permenant migraine. But one day I believe I can make it, and survive the hardest construction I ever had made in my entire life.

---
## [giuliobenetti/linux-imxrt](https://github.com/giuliobenetti/linux-imxrt)@[0c80f9e165...](https://github.com/giuliobenetti/linux-imxrt/commit/0c80f9e165f8f9cca743d7b6cbdb54362da297e0)
#### Saturday 2022-08-06 22:52:08 by Sudeep Holla

ACPI: PPTT: Leave the table mapped for the runtime usage

Currently, everytime an information needs to be fetched from the PPTT,
the table is mapped via acpi_get_table() and unmapped after the use via
acpi_put_table() which is fine. However we do this at runtime especially
when the CPU is hotplugged out and plugged in back since we re-populate
the cache topology and other information.

However, with the support to fetch LLC information from the PPTT in the
cpuhotplug path which is executed in the atomic context, it is preferred
to avoid mapping and unmapping of the PPTT for every single use as the
acpi_get_table() might sleep waiting for a mutex.

In order to avoid the same, the table is needs to just mapped once on
the boot CPU and is never unmapped allowing it to be used at runtime
with out the hassle of mapping and unmapping the table.

Reported-by: Guenter Roeck <linux@roeck-us.net>
Cc: Rafael J. Wysocki <rafael@kernel.org>
Signed-off-by: Sudeep Holla <sudeep.holla@arm.com>

--

Hi Rafael,

Sorry to bother you again on this PPTT changes. Guenter reported an issue
with lockdep enabled in -next that include my cacheinfo/arch_topology changes
to utilise LLC from PPTT in the CPU hotplug path.

Please ack the change once you are happy so that I can get it merged with
other fixes via Greg's tree.

Regards,
Sudeep

Acked-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Link: https://lore.kernel.org/r/20220720-arch_topo_fixes-v3-2-43d696288e84@arm.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---

