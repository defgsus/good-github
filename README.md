## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-24](docs/good-messages/2022/2022-04-24.md)


1,520,435 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,520,435 were push events containing 2,232,873 commit messages that amount to 121,982,828 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a137c15a79...](https://github.com/tgstation/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Sunday 2022-04-24 00:02:47 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Son-of-Space/tgstation](https://github.com/Son-of-Space/tgstation)@[cd1b891d79...](https://github.com/Son-of-Space/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Sunday 2022-04-24 00:05:28 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[242ef904f0...](https://github.com/Zergspower/Skyrat-tg/commit/242ef904f0a2ea2cc5de87863e93def5131ea0be)
#### Sunday 2022-04-24 01:04:34 by SkyratBot

[MIRROR] Fixes bartender drink throwing, makes smashing always spill [MDB IGNORE] (#12326)

* Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

* Fixes bartender drink throwing, makes smashing always spill

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[d411393e72...](https://github.com/SmoSmoSmoSmok/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Sunday 2022-04-24 01:12:36 by Zytolg

NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[4652d4bb63...](https://github.com/SmoSmoSmoSmok/tgstation/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Sunday 2022-04-24 01:12:36 by Jolly

Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[b86cf89125...](https://github.com/SmoSmoSmoSmok/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Sunday 2022-04-24 01:12:36 by Aleksej Komarov

tgui: API improvements + docs (#65943)


About The Pull Request

This pull request improves tgui API in many ways.

Using TGUI for custom HTML popups

This standardizes and simplifies the process of HTML popup creation and DM <-> JS communication.

Makes tgui window API a perfect alternative for old-style browser panels. It will be super useful for @Iamgoofball since he wanted to make a lightweight browser element that plays background music, and this will make his life a lot easier.

It is now possible to create tgui windows with fully inlined JS and CSS, which can be used to make unkillable tgui-based UIs (can't white/blue screen due to network errors). You can split files into JS and CSS, and still serve a single HTML file using this.

Moved sendMessage function to the Byond API object, where it rightfully belongs, and now supports a shorthand form: Byond.sendMessage(type, payload). This shortens and simplifies a lot of code.

Refactored window.update to no longer be public. Now to subscribe to incoming messages, you should use new public APIs: Byond.subscribe(fn) and Byond.subscribeTo(type, fn), and TGUI internally uses these functions as well, which reduces boilerplate in index.js.

Renamed window.__windowId__ to Byond.windowId (old variable is still available for backwards compatibility).

Byond API now supports null id, e.g. Byond.winget(null, 'url'), which makes things like this possible:

// Fetch URL of a currently connected server
Byond.winget(null, 'url').then((serverUrl) => {
  // Connect to this server (opens a new dreamseeker instance)
  Byond.call(serverUrl);
  // Close this client because new instance is connecting
  Byond.command('.quit');
});

Certain polyfills are now statically compiled (commited into git) and are baked into tgui.html. The downside is that HTML went 16 kB -> 50 kB. The upside is that you can now use a relatively modern level API with full support for IE8 when writing plain old html UIs using /datum/tgui_window directly. They are committed into git, because polyfills will never need to be updated (unless of course we randomly decide to get rid of ie8.js and html5shiv.js).
Breaking Changes

No breaking changes. This should be tested for regressions. Upgrading is simple if you're on a relatively up-to-date branch - copy paste all affected tgui files and you're good.

---
## [NganuCoeg/kernel_realme_trinket](https://github.com/NganuCoeg/kernel_realme_trinket)@[07ddaa6d7b...](https://github.com/NganuCoeg/kernel_realme_trinket/commit/07ddaa6d7b48fd36fb834a62bd03c83996e516af)
#### Sunday 2022-04-24 01:36:44 by Wang Han

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
Signed-off-by: NganuCoeg <starterpackmeh@gmail.com>

---
## [tgstation/map_depot](https://github.com/tgstation/map_depot)@[a54b3efd60...](https://github.com/tgstation/map_depot/commit/a54b3efd606da3829ae328af0cfb42f8874b6d7b)
#### Sunday 2022-04-24 01:56:47 by san7890

Adds VR Snowdin and VRHub to the Map Depot

Hey there,

Look at how soulful these maps once were:

Actually, no, I'm sorry. I can't take myself seriously! This shit fucking sucked! I'm adding it here as a cautionary tale for those who long for the days of VR. I included the entire last-working commit hash because these maps last worked on unadulterated 2019 shitcode and I don't want anyone screwing it up.

Every single trace of VR Code was purged from the repository after the given base commit, so literally none of this will work on any modern code without a lot of work. If you want to modernize this, I hope you're prepared to instantly runtime, shit, and die.

---
## [helqfvl/og-names](https://github.com/helqfvl/og-names)@[05d1c1c1d2...](https://github.com/helqfvl/og-names/commit/05d1c1c1d23e8eeb417e99c5c65be2784032793e)
#### Sunday 2022-04-24 02:22:57 by fez

Create abbreviations.txt (#58)

* Create abbreviations.txt

> 4AO - For adults only
> AFK - Away from keyboard
> AKA - Also known as
> ASAP - As soon as possible
> BAE - Before anyone else
> BFF - Best friend forever
> BRB - Be right back
> BTW - By the way
> BUMP - Bring up my post
> CTR - Click-through rate
> DIY - Do it yourself
> ETC - Et cetera
> FAQ - Frequently asked questions
> FYI - For your information
> G2G - Got to go
> HMU - Hit me up
> IDC - I don't care
> IDK - I don't know
> ILY - I love you
> IMO - In my opinion
> J4F - Just for fun
> KISS - Keep it simple stupid
> LMAO - Laughing my ass off
> LMFAO - Laughing my f***ing ass off
> LMK - Let me know
> MSG - Message
> NSFW - Not safe for work
> NVM - Nevermind
> OMW - On my way
> PPL - People
> POV - Point of view
> QNA - Questions and answeres
> ROFL - Rolling on floor laughing
> RUOK - Are you okay
> SOS - Save our ship
> SMS - Short message service
> STFU - Shut the f**k up
> TBH - To be honest
> TTYL - Talk to you later
> UUID - Universally unique identifier
> VIP - Very important person
> WTF - What the f**k
> XMAS - Christmas
> Y2K - The year 2000
> ZZZ - Sleeping noise

* Added "idfc"

Added:
› IDFC - I don't f\*\*\*ing care

* Fix: GTG

Fixed:
› GTG - Got to go | Changed from "G2G".

---
## [Invader07/assets](https://github.com/Invader07/assets)@[f8c6a59b86...](https://github.com/Invader07/assets/commit/f8c6a59b8620e450998ac11cc1e3cf2873551801)
#### Sunday 2022-04-24 03:26:06 by Casini Loogi

Merge pull request #11 from Invader07/master

new world shit because redirectors a bitch (and so it can be put in the Fucking game)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0ac895b5a0...](https://github.com/treckstar/yolo-octo-hipster/commit/0ac895b5a0be550fe7e59a297b3f65de5fbdcf65)
#### Sunday 2022-04-24 04:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [fangshun2004/rathena](https://github.com/fangshun2004/rathena)@[d617d9f083...](https://github.com/fangshun2004/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Sunday 2022-04-24 04:48:43 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [knowler/knowlerkno.ws](https://github.com/knowler/knowlerkno.ws)@[5e8fd6174f...](https://github.com/knowler/knowlerkno.ws/commit/5e8fd6174fd9acc1f49ee9abf851fdd5fa7c79a8)
#### Sunday 2022-04-24 06:07:27 by Nathan Knowler

Improve invalid form submission response + UI

We populate the form with the invalid data so that the user doesn’t need
to fill it out again. If the honeypot was triggered, we leave the form
empty as a “fuck you.”

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[d8ffda8ff9...](https://github.com/UnderMybrella/usa/commit/d8ffda8ff9335ec0fc902cde4c3d4d490f1d6c61)
#### Sunday 2022-04-24 06:13:26 by MarkiSpider

Update 90 files @ Sun, 24 Apr 2022 06:13:23 GMT
This site update changes karen-archive.html, case-directory.html, thealienalliance.html, thebutterflysoldiers.html, schedule.html, youreinthewrongpartoftown.html, aretheyalium.html, logs.html, images.html, theoracle.html, michaeljackson.html, logs.html, c-8-dickpicks.html, user.html, 914222-1952425161182025.html, thebannerborn.html, zeusandfriends.html, reviews.html, dashboard.html, MatPat.html, idkbro.html, thecaptain.html, thedude.html, oopsalbangers.html, inhumanresources.html, 914222-195242514914101.html, ijustmadeyoulookunderthere.html, the-d_.html, user8118151241161251919.html, iinhumanresources.html, terfwar.html, departments.html, captainwhyareyoudoingthistome.html, moriarty.html, 914222-3421144920.html, USA-Logo-RecruitingPage.gif, auth.html, cases.html, usa-home.html, dont-push.html, LixianTV.html, employeeaccountabilitytimesignature-portal.html, USA-Logo-RecruitingPage.gif, cart.html, Jupiterandfriends.html, agentloginportal.html, the-asshats.html, illinois.html, corn-dm.html, thejackson5.html, gettingjiggywithit.html, logout.html, legal.html, girlofthe21stcentury.html, MichaelJackson.html, capitalism.html, fuckem.html, NerdFiction.html, terrorblycute.html, shatteredbysomeone.html, everyone.html, messenger.html, evidence.html, evidence.html, woahhh.html, ohyouwouldlikethatwouldntyou.html, redacted.html, agencydirectory.html, karen6803.html, karen6804.html, 914222-5241612154525.html, lolgotyou.html, thefounders.html, sexygoldarms.html, the-baboonies.html, 2702-invincible2syndicate.html, case-directory.html, Imsorrymissjackson.html, 914222-1916151820192112124214513114.html, nebuchadnezzar.html, karen6816.html, cachow.html, karen6815.html, helpcenter.html, kriskringle.html, byebyebye.html, thekilleidoscope.html, para.docs-portal, karen6809.html, Rad_R.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[1b15dab2c2...](https://github.com/UnderMybrella/usa/commit/1b15dab2c247291baaa1bb4474d08deb4aa7d722)
#### Sunday 2022-04-24 06:32:45 by MarkiSpider

Update 98 files @ Sun, 24 Apr 2022 06:32:42 GMT
This site update changes karen-archive.html, case-directory.html, thealienalliance.html, thebutterflysoldiers.html, schedule.html, youreinthewrongpartoftown.html, aretheyalium.html, logs.html, images.html, theoracle.html, michaeljackson.html, logs.html, dontpush.html, c-8-dickpicks.html, user.html, 914222-1952425161182025.html, thebannerborn.html, zeusandfriends.html, overview.html, reviews.html, dashboard.html, MatPat.html, idkbro.html, thecaptain.html, thedude.html, oopsalbangers.html, 914222-20513165181205.html, inhumanresources.html, 914222-195242514914101.html, ijustmadeyoulookunderthere.html, the-d_.html, user8118151241161251919.html, iinhumanresources.html, terfwar.html, departments.html, captainwhyareyoudoingthistome.html, moriarty.html, 914222-3116201914.html, 914222-3421144920.html, USA-Logo-RecruitingPage.gif, auth.html, cases.html, usa-home.html, .html, dont-push.html, LixianTV.html, employeeaccountabilitytimesignature-portal.html, USA-Logo-RecruitingPage.gif, cart.html, Jupiterandfriends.html, agentloginportal.html, the-asshats.html, illinois.html, corn-dm.html, thejackson5.html, gettingjiggywithit.html, logout.html, legal.html, girlofthe21stcentury.html, capitalism.html, MichaelJackson.html, fuckem.html, NerdFiction.html, shatteredbysomeone.html, terrorblycute.html, everyone.html, messenger.html, 914222-29151493191121139.html, evidence.html, evidence.html, woahhh.html, ohyouwouldlikethatwouldntyou.html, redacted.html, agencydirectory.html, karen6803.html, karen6804.html, 914222-5241612154525.html, lolgotyou.html, thefounders.html, sexygoldarms.html, the-baboonies.html, 2702-invincible2syndicate.html, case-directory.html, Imsorrymissjackson.html, 914222-1916151820192112124214513114.html, nebuchadnezzar.html, karen6816.html, .izntyizzyor, cachow.html, karen6815.html, helpcenter.html, kriskringle.html, byebyebye.html, thekilleidoscope.html, para.docs-portal, suspect-hierarchy.html, karen6809.html, Rad_R.html

---
## [saint-lascivious/munin-pihole-plugins](https://github.com/saint-lascivious/munin-pihole-plugins)@[02cb03fa2e...](https://github.com/saint-lascivious/munin-pihole-plugins/commit/02cb03fa2e684c04f421af0e9affdbfd9d8d72f1)
#### Sunday 2022-04-24 06:35:18 by Hayden Pearce

munin-pihole-plugins: more output and formatting changes

somewhat of an extension of 43d9294

Changes to be committed:
 - modified:   script/munin-pihole-plugins
   bump version to 05.12.00
   more colour in output
   (highlight commands that were not found in red)
   offset reverberate output
   (add a two character offset from the terminal edge)
   find a use for reverberate's fallthrough case
   (this ended up working out nicely with additional output)
   (more work that ideally shouldn't ever be seen)
   (this lets us format both code and its resulting output better)
   fix formatting in warning when script dir isn't in $PATH
   (the suggested output didn't need bracing)
   (seems we found a flaw with shellcheck's parsing)
   (said flaw was accidentally fixed splitting a multi-line echo)
   (as always, fuck you, shellcheck)

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[9d9a57c754...](https://github.com/UnderMybrella/usa/commit/9d9a57c754b5772e0a9a51d13fed8a96b069745e)
#### Sunday 2022-04-24 06:46:39 by MarkiSpider

Update 96 files @ Sun, 24 Apr 2022 06:46:34 GMT
This site update changes karen-archive.html, case-directory.html, thealienalliance.html, thebutterflysoldiers.html, schedule.html, youreinthewrongpartoftown.html, aretheyalium.html, logs.html, images.html, theoracle.html, michaeljackson.html, logs.html, dontpush.html, c-8-dickpicks.html, user.html, 914222-1952425161182025.html, zeusandfriends.html, thebannerborn.html, overview.html, reviews.html, dashboard.html, MatPat.html, idkbro.html, thecaptain.html, thedude.html, oopsalbangers.html, 914222-20513165181205.html, inhumanresources.html, 914222-195242514914101.html, ijustmadeyoulookunderthere.html, the-d_.html, user8118151241161251919.html, iinhumanresources.html, terfwar.html, departments.html, captainwhyareyoudoingthistome.html, moriarty.html, 914222-3116201914.html, 914222-3421144920.html, USA-Logo-RecruitingPage.gif, auth.html, cases.html, usa-home.html, .html, dont-push.html, LixianTV.html, employeeaccountabilitytimesignature-portal.html, cart.html, Jupiterandfriends.html, agentloginportal.html, the-asshats.html, illinois.html, corn-dm.html, thejackson5.html, gettingjiggywithit.html, logout.html, legal.html, girlofthe21stcentury.html, MichaelJackson.html, capitalism.html, fuckem.html, NerdFiction.html, terrorblycute.html, shatteredbysomeone.html, everyone.html, messenger.html, 914222-29151493191121139.html, evidence.html, evidence.html, woahhh.html, ohyouwouldlikethatwouldntyou.html, redacted.html, agencydirectory.html, karen6803.html, karen6804.html, 914222-5241612154525.html, lolgotyou.html, thefounders.html, sexygoldarms.html, the-baboonies.html, 2702-invincible2syndicate.html, case-directory.html, Imsorrymissjackson.html, 914222-1916151820192112124214513114.html, nebuchadnezzar.html, karen6816.html, cachow.html, karen6815.html, helpcenter.html, kriskringle.html, byebyebye.html, thekilleidoscope.html, para.docs-portal, suspect-hierarchy.html, karen6809.html, Rad_R.html

---
## [MineClone2/MineClone2](https://github.com/MineClone2/MineClone2)@[5f126c4686...](https://github.com/MineClone2/MineClone2/commit/5f126c468650577ea0baefb5d79b81835fe33579)
#### Sunday 2022-04-24 07:00:33 by cora

add hypercopyrighted end crystal beam texture

This texture has the following poem written by me, cora, encoded in its
pixeldata. I the author hereby release both the texture file and the
poem as cc0.

Additionally I explicitly consent with its inclusion into MineClone2,
MineClone5 and Mineclonia as well as any other minetest game for this
day and all the days to come.

Shall though betray me with a texture, mate
I'll smile at though just like a summer's day
The raindrop particles - no laggy state
But spring is coming, really, soon it's may

As If the seasons meant a damn to us
They do not exist in mineclone at all
unreal water flow, iron never rusts
but copper does in summer and in fall

But what this literally is about
because this damn thing is really silly
you see somehow they had to say it loud

I would bring that quote with painting lilys
but plagerism everywhere you see
so this will just be good enough for me

---
## [ThePainkiller/sojourn-station](https://github.com/ThePainkiller/sojourn-station)@[941b0c2515...](https://github.com/ThePainkiller/sojourn-station/commit/941b0c25153baaf6757bc6f5842fa2e8400653ab)
#### Sunday 2022-04-24 07:21:54 by ThePainkiller

Drip megapack 100% real not fake 1 commit church buff speedmerge

- Adds Justice, Pandemonica, Malina, Zdrada and Modeus alt styles for charming outfit
- Adds a black suit jacket with adjustable styles for the charming outfit
- Adds charming waistcoat for Malina/Cerberus drip
- Ports the Tojo Pants and Tojo Jacket from the mad dog of Shimano himself
- Ports black and red overcoat styles (Joker, Morningstar)
- New sprites for Prospector/Foreman lockers, Salvager lockers changed in appearance to rusty old ones for fluff
- Adds New Testament Knight Hardsuit RIG module for the church's New Testament Armaments Disk, a Divisor/Numerical joint effort in producing a combat-ready hardsuit. A pre-loaded version with flash, shield, jetpack and storage modules spawns on the Prime's office's altar. Same stats as the Combat Hardsuit.

---
## [EtraIV/Merchant-Station-13](https://github.com/EtraIV/Merchant-Station-13)@[763ae2f259...](https://github.com/EtraIV/Merchant-Station-13/commit/763ae2f259b46d116f0b4bef65ad1dc66f948f79)
#### Sunday 2022-04-24 07:33:50 by Etra

Used null forgiving operator for borgpanel keyslot access (who the fuck wrote this shit jfc)

---
## [dnelson-1901/freebsd-ports](https://github.com/dnelson-1901/freebsd-ports)@[e250aeb4a1...](https://github.com/dnelson-1901/freebsd-ports/commit/e250aeb4a1399664907d0df0605a3577ba671609)
#### Sunday 2022-04-24 09:04:04 by Tobias C. Berner

KDE: Update KDE Gear to 22.04

Thursday, 21 April 2022

Welcome to KDE Gear ⚙️ 22.04!

Skip to What’s New

KDE Gear ⚙️ 22.04 brings you all the updates added to a long list of KDE
apps over the last four months. KDE programs allow you to work, create
and play without having to submit yourself to extortionate licenses and
intrusive advertising, or surrender your privacy to unscrupulous
corporations.

Below you will discover a selection of the changes added in the last
four months to software designed to make your life better. But remember,
there is much, much more: games, social media apps, utilities for
communicating, developing and creating stuff… All these things have been
worked on to give you more stability and boost your productivity.

If you want to see a full list of everything we have done, check out the
complete changelog.

WARNING: There’s a lot!

All the details can be found here:
	https://kde.org/announcements/gear/22.04.0/

---
## [Kaz205/renoir](https://github.com/Kaz205/renoir)@[a70fc62899...](https://github.com/Kaz205/renoir/commit/a70fc628996538ef476153c7ff9070834021e91f)
#### Sunday 2022-04-24 10:35:14 by Peter Zijlstra

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
## [Abstaina44/Abstaina44](https://github.com/Abstaina44/Abstaina44)@[b275d04e97...](https://github.com/Abstaina44/Abstaina44/commit/b275d04e97dd0b5e53bdb0cdb45a7dc609dd744b)
#### Sunday 2022-04-24 10:42:45 by Ephraim Abstaina

Update README.md

A results oriented young man who puts excellence at the forefront of every task assigned and is taken to detail and accuracy. 
With a very high level of efficiency and reliability there is a profound sense or desire to deliver and help others develop themselves in a manner so as to be able to achieve something without having to rely on others. 
In terms of relations, is very open to new experiences and coordinates all aspects of a challenge well enough to create a changing environment for others to work in. 
While living outside work, there is a need to share with family and friends and value is placed on everything and everyone who is likely to have a relationship with or shares common desire with in order to achieve a set goal or objective. There is also an element of purpose to give back to society while sustaining present resources for future generations to discover and develop. 

A resident of the United Arab Emirates, founder of Crypto Hub Network . I am pro- trader in crypto currencies, a junior blockchain dev with 4yrs experience in Java, C++ and Solidity, an early adopter of Non Fungible Tokens.(NFT's)
        My 4yrs experience in crypto currency trading and blockchain development has made me the most exceptional and demanding one among all the experts.
I am tremendously good at NFT’s, blockchain Technology and Cryptocurrency trading( Futures and Spot)
  Last year, Binance the largest cryptocurrency exchange by volume of which  Changpeng Zhao is the founder organised a three day online trading and I came out successfully with a certificate.
Since the introduction of NFT’s on the Ethereum blockchain, I have minted over 20 from different NFT marketplaces( Opensea) and also sold alot of them.

I can visually represent  what my client wants in my works.I am honest and confident.I possess all the qualities you need for this job.
Again I am a learner and I love to learn new things, testing on them and love having feedbacks.
Everyday I determine to be a more improved one.
I am an Innovative AI Engineer / Entrepreneur with 5 years of professional experience in application design, architectural road map, development, testing and production level deployment on smart contracts  and TPUs. I am highly experience in writing efficient and reproducible codes and algorithms, as well as building and re-using complex neural networks via various programming languages. I do have a comprehensive/ practical understanding of applied ML in sports, health, fin-tech, agriculture and music.

---
## [tromey/gdb](https://github.com/tromey/gdb)@[bbea680797...](https://github.com/tromey/gdb/commit/bbea68079781ac4c2fc941867ee9888585cafb77)
#### Sunday 2022-04-24 11:15:34 by Andrew Burgess

gdb/python: improve the auto help text for gdb.Parameter

This commit attempts to improve the help text that is generated for
gdb.Parameter objects when the user fails to provide their own
documentation.

Documentation for a gdb.Parameter is currently pulled from two
sources: the class documentation string, and the set_doc/show_doc
class attributes.  Thus, a fully documented parameter might look like
this:

  class Param_All (gdb.Parameter):
     """This is the class documentation string."""

     show_doc = "Show the state of this parameter"
     set_doc = "Set the state of this parameter"

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_All, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_All ('param-all')

Then in GDB we see this:

  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

Which is fine.  But, if the user skips both of the documentation parts
like this:

  class Param_None (gdb.Parameter):

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_None, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_None ('param-none')

Now in GDB we see this:

  (gdb) help set param-none
  This command is not documented.
  This command is not documented.

That's not great, the duplicated text looks a bit weird.  If we drop
different parts we get different results.  Here's what we get if the
user drops the set_doc and show_doc attributes:

  (gdb) help set param-doc
  This command is not documented.
  This is the class documentation string.

That kind of sucks, we say it's undocumented, then proceed to print
the documentation.  Finally, if we drop the class documentation but
keep the set_doc and show_doc:

  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

That seems OK.

So, I think there's room for improvement.

With this patch, for the four cases above we now see this:

  # All values provided by the user, no change in this case:
  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

  # Nothing provided by the user, the first string is now different:
  (gdb) help set param-none
  Set the current value of 'param-none'.
  This command is not documented.

  # Only the class documentation is provided, the first string is
  # changed as in the previous case:
  (gdb) help set param-doc
  Set the current value of 'param-doc'.
  This is the class documentation string.

  # Only the set_doc and show_doc are provided, this case is unchanged
  # from before the patch:
  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

The one place where this change might be considered a negative is when
dealing with prefix commands.  If we create a prefix command but don't
supply the set_doc / show_doc strings, then this is what we saw before
my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- This command is not documented.
  ... snip ...

And after my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- Set the current value of 'print param-none'.
  ... snip ...

This seems slightly less helpful than before, but I don't think its
terrible.

Additionally, I've changed what we print when the get_show_string
method is not provided in Python.

Back when gdb.Parameter was first added to GDB, we didn't provide a
show function when registering the internal command object within
GDB.  As a result, GDB would make use of its "magic" mangling of the
show_doc string to create a sentence that would display the current
value (see deprecated_show_value_hack in cli/cli-setshow.c).

However, when we added support for the get_show_string method to
gdb.Parameter, there was an attempt to maintain backward compatibility
by displaying the show_doc string with the current value appended, see
get_show_value in py-param.c.  Unfortunately, this isn't anywhere
close to what deprecated_show_value_hack does, and the results are
pretty poor, for example, this is GDB before my patch:

  (gdb) show param-none
  This command is not documented. off

I think we can all agree that this is pretty bad.

After my patch, we how show this:

  (gdb) show param-none
  The current value of 'param-none' is "off".

Which at least is a real sentence, even if it's not very informative.

This patch does change the way that the Python API behaves slightly,
but only in the cases when the user has missed providing GDB with some
information.  In most cases I think the new behaviour is a lot better,
there's the one case (noted above) which is a bit iffy, but I think is
still OK.

I've updated the existing gdb.python/py-parameter.exp test to cover
the modified behaviour.

Finally, I've updated the documentation to (I hope) make it clearer
how the various bits of help text come together.

---
## [tromey/gdb](https://github.com/tromey/gdb)@[299953ca95...](https://github.com/tromey/gdb/commit/299953ca95cc5ac47e52236e2eeb44afc5369134)
#### Sunday 2022-04-24 11:15:34 by Andrew Burgess

gdb/python: handle non utf-8 characters when source highlighting

This commit adds support for source files that contain non utf-8
characters when performing source styling using the Python pygments
package.  This does not change the behaviour of GDB when the GNU
Source Highlight library is used.

For the following problem description, assume that either GDB is built
without GNU Source Highlight support, of that this has been disabled
using 'maintenance set gnu-source-highlight enabled off'.

The initial problem reported was that a source file containing non
utf-8 characters would cause GDB to print a Python exception, and then
display the source without styling, e.g.:

  Python Exception <class 'UnicodeDecodeError'>: 'utf-8' codec can't decode byte 0xc0 in position 142: invalid start byte
  /* Source code here, without styling...  */

Further, as the user steps through different source files, each time
the problematic source file was evicted from the source cache, and
then later reloaded, the exception would be printed again.

Finally, this problem is only present when using Python 3, this issue
is not present for Python 2.

What makes this especially frustrating is that GDB can clearly print
the source file contents, they're right there...  If we disable
styling completely, or make use of the GNU Source Highlight library,
then everything is fine.  So why is there an error when we try to
apply styling using Python?

The problem is the use of PyString_FromString (which is an alias for
PyUnicode_FromString in Python 3), this function converts a C string
into a either a Unicode object (Py3) or a str object (Py2).  For
Python 2 there is no unicode encoding performed during this function
call, but for Python 3 the input is assumed to be a uft-8 encoding
string for the purpose of the conversion.  And here of course, is the
problem, if the source file contains non utf-8 characters, then it
should not be treated as utf-8, but that's what we do, and that's why
we get an error.

My first thought when looking at this was to spot when the
PyString_FromString call failed with a UnicodeDecodeError and silently
ignore the error.  This would mean that GDB would print the source
without styling, but would also avoid the annoying exception message.

However, I also make use of `pygmentize`, a command line wrapper
around the Python pygments module, which I use to apply syntax
highlighting in the output of `less`.  And this command line wrapper
is quite happy to syntax highlight my source file that contains non
utf-8 characters, so it feels like the problem should be solvable.

It turns out that inside the pygments module there is already support
for guessing the encoding of the incoming file content, if the
incoming content is not already a Unicode string.  This is what
happens for Python 2 where the incoming content is of `str` type.

We could try and make GDB smarter when it comes to converting C
strings into Python Unicode objects; this would probably require us to
just try a couple of different encoding schemes rather than just
giving up after utf-8.

However, I figure, why bother?  The pygments module already does this
for us, and the colorize API is not part of the documented external
API of GDB.  So, why not just change the colorize API, instead of the
content being a Unicode string (for Python 3), lets just make the
content be a bytes object.  The pygments module can then take
responsibility for guessing the encoding.

So, currently, the colorize API receives a unicode object, and returns
a unicode object.  I propose that the colorize API receive a bytes
object, and return a bytes object.

---
## [HashmatHamid/Hashmat-Python-assessment](https://github.com/HashmatHamid/Hashmat-Python-assessment)@[0fc70e1835...](https://github.com/HashmatHamid/Hashmat-Python-assessment/commit/0fc70e183589578b33850a3b47837725dd3bf8a4)
#### Sunday 2022-04-24 11:15:38 by Hashmat Hamid

def intro():
    print("""Hello and welcome to my general mathematics quiz.
In this quiz you will be asked from 10-50 mathematics questions based on
your choice.
Also depending on your choice, you can choose to  do either a hard or easy
quiz.
The hard quiz will feature algebra and number, you will also be only
allowed to answer with word answers.
With the easy questions you will be asked number questions and the answers
wil be in a multi-choice form. """)
    print("I hope you enjoy :)")

def name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha():
              break
        except ValueError:
            print("Not a valid name")

    print("Hello {} I hope you have fun playing my game".format(name))

def age():
    while True:
        try:
            age = input("Please enter your age: ")
            age = int(age)
            break
        except ValueError:
            print("Not a valid age! Please try again ...")

    print("Wow, you are {}".format(age))

def questions():
    global score
    score=0
    qq = { 'Q.1) What is 2*2 \n a: 4\n b: 5\n c: 3\n' : '4' , 'Q.2) What is 3*2\n a: 2\n b: 6\n c: 7 \n' : '6' ,
                 'Q.3) What is the unit for factorial in maths \n a: ^\n b: %\n c: ! \n' : '!' , 'Q.4) What is the equation for a question using the pythagoras theorem \n a: a^2+b^2=c^2\n b: b^2+c^2=a^2\n c: c^2+a^2=b^2 \n' : 'a^2+b^2=c^2' , 'Q.5) What is the value of pi \n a: 2.5\n b: 3.14\n c: 0.1 \n' : '3.14' , 'Q.6) What is 2 squared \n a: 4\n b: 2\n c: 1\n' : '4' , 'Q.7) What is the square root of 81 \n a: 9\n b: 13\n c: 10 \n' : '9' , 'Q.8) What is the value of Gst \n a: 15%\n b: 1.5%\n c: 0.15% \n' : '15%' , 'Q.9) Where did the person who invented Algorthm die \n a: Baghdad\n b: London\n c: Beijing\n' : 'Baghdad' , 'Q.10) What year did Stephen Hawking die \n a: 2018\n b: 2019\n c: 2017 \n' : '2018'
         }

    for key in qq.keys():
        user_answer=input(key).lower().strip()
        if qq.get(key)==user_answer:
            print("Correct!")
            score+=1
        else:
            print("You're Wrong!")

intro()
name()
age()
questions()
print("You got "+str(score)+" right!")

---
## [nickol998/Absinthe](https://github.com/nickol998/Absinthe)@[f07f0029ea...](https://github.com/nickol998/Absinthe/commit/f07f0029eaefa597b6256507f94143337c4c44d1)
#### Sunday 2022-04-24 12:04:22 by gys619

删除：[ 2000jinli_log.js, CK_WxPusherUid.json, JDJRSignValidator.js, JDJRValidator_Aaron.js, JDJRValidator_Pure.js, JD_DailyBonus.js, JD_extra_cookie.js, JS_USER_AGENTS.js, LICENSE, Loon/lxk0301_LoonTask.conf, QuantumultX/cookies.conf, QuantumultX/gallery.json, QuantumultX/lxk0301_cookies.conf, QuantumultX/lxk0301_gallery.json, Surge/Task.sgmodule, Surge/lxk0301_Task.sgmodule.sgmodule, TS_USER_AGENTS.ts, USER_AGENTS.js, ZooFaker_Necklace.js, activity/JD_extra_cookie.js, activity/jd_0yuankanjia.js, activity/jd_15_5.js, activity/jd_29_8.js, activity/jd_5g.js, activity/jd_818.js, activity/jd_UnknownTask4.js, activity/jd_angryBean.js, activity/jd_apple_live.js, activity/jd_appliances.js, activity/jd_bean_sign.js, activity/jd_beauty_ex.js, activity/jd_big_winner.js, activity/jd_bridge.js, activity/jd_btnyx.py, activity/jd_bzlshdgt.js, activity/jd_car.js, activity/jd_carnivalcity.js, activity/jd_cash.js, activity/jd_cfd_fresh.js, activity/jd_cfd_fresh_exchange.js, activity/jd_cfd_hb.js, activity/jd_cfd_loop.js, activity/jd_cfd_mooncake.js, activity/jd_cfd_mooncake_help.js, activity/jd_cfd_pearl.js, activity/jd_cfd_pearl_ex.js, activity/jd_cfdtx.js, activity/jd_city_exchange.js, activity/jd_city_lottery.js, activity/jd_citytx.js, activity/jd_coupon.js, activity/jd_crazy_joy.js, activity/jd_crazy_joy_bonus.js, activity/jd_crazy_joy_coin.js, activity/jd_daily_egg.js, activity/jd_daily_lottery.js, activity/jd_ddwj.js, activity/jd_decompression.js, activity/jd_delCoupon.js, activity/jd_desire.js, activity/jd_digital_floor.js, activity/jd_djyyj.js, activity/jd_dlpj.js, activity/jd_dpqd.js, activity/jd_ds.js, activity/jd_dyj_help.js, activity/jd_family.js, activity/jd_fcdyj_help_wx.js, activity/jd_fcwb.js, activity/jd_film_museum.js, activity/jd_firecrackers.js, activity/jd_firecrackers2.js, activity/jd_fission.js, activity/jd_focus.js, activity/jd_foodRunning.js, activity/jd_freshgoods.js, activity/jd_ftzy_help.js, activity/jd_global.js, activity/jd_global_mh.js, activity/jd_golden_machine.js, activity/jd_gouwuche.js, activity/jd_gyp.js, activity/jd_haier.js, activity/jd_half_redrain.js, activity/jd_hb.js, activity/jd_health.js, activity/jd_health_plant.py, activity/jd_honour.js, activity/jd_hotNeight.js, activity/jd_hotnight.js, activity/jd_hyj.js, activity/jd_hyj_help.py, activity/jd_immortal.js, activity/jd_immortal_answer.js, activity/jd_industrial_task.js, activity/jd_industryLottery.js, activity/jd_jchsign.js, activity/jd_jdh.js, activity/jd_jika.js, activity/jd_jingsubang.js, activity/jd_joy.js, activity/jd_joy_feedPets.js, activity/jd_joy_park_newtask.js, activity/jd_joy_run.js, activity/jd_joy_steal.js, activity/jd_jump.js, activity/jd_jxd.js, activity/jd_jxdzz.js, activity/jd_jxg.js, activity/jd_jxhlk.js, activity/jd_jxhlk.py, activity/jd_jxnc.js, activity/jd_jxnn.js, activity/jd_jxstory.js, activity/jd_koi_Help.js, activity/jd_kxcdz.js, activity/jd_ldhwj.js, activity/jd_live.js, activity/jd_live_redrain.js, activity/jd_live_redrain2.js, activity/jd_ljd.js, activity/jd_lol.js, activity/jd_lotteryMachine.js, activity/jd_lottery_drew.js, activity/jd_lsj.js, activity/jd_lxLottery.js, activity/jd_market_lottery.js, activity/jd_mcxhd.js, activity/jd_medal_exchange.py, activity/jd_mh.js, activity/jd_mhyyl.js, activity/jd_mhyyl_prize.js, activity/jd_mofang.js, activity/jd_mofang_ex.js, activity/jd_mohe.js, activity/jd_mohe_help.js, activity/jd_moneyTree_help.js, activity/jd_ms.js, activity/jd_ms_redrain.js, activity/jd_mx_shop.js, activity/jd_neight1.js, activity/jd_neight2.js, activity/jd_newTreasure.py, activity/jd_newYearMoney.js, activity/jd_newYearMoney_lottery.js, activity/jd_nian.js, activity/jd_nian_ar.js, activity/jd_nian_sign.js, activity/jd_nian_wechat.js, activity/jd_nsjcj.js, activity/jd_party_night.js, activity/jd_petTreasureBox.js, activity/jd_pubg.js, activity/jd_qcshj.js, activity/jd_qycl.js, activity/jd_redPacket_help.js, activity/jd_ryhxj.js, activity/jd_selectionOffice.js, activity/jd_sendBeans.js, activity/jd_sevenDay.js, activity/jd_shop.js, activity/jd_sign_graphics.js, activity/jd_sjjc.js, activity/jd_sjnhj.js, activity/jd_speed.js, activity/jd_spnvjd.js, activity/jd_summer_movement.js, activity/jd_superMarket.js, activity/jd_super_box.js, activity/jd_super_mh.js, activity/jd_superbox.js, activity/jd_sxLottery.js, activity/jd_tcl.js, activity/jd_teamFLP.js, activity/jd_tewu.js, activity/jd_tiger_help.js, activity/jd_travel.js, activity/jd_travel_help.js, activity/jd_travel_shop.js, activity/jd_unbind.js, activity/jd_unknownTask1.js, activity/jd_unsubscribe.js, activity/jd_watch.js, activity/jd_wxCollectionActivity.js, activity/jd_wxShopFollowActivity.js, activity/jd_xg.js, activity/jd_xgyl.js, activity/jd_xiaolongfan.js, activity/jd_xiaomi.js, activity/jd_xinruimz.js, activity/jd_xinxiangyin.js, activity/jd_xqscjd.js, activity/jd_xtg.js, activity/jd_xtg_help.js, activity/jd_xyhy.js, activity/jd_year.js, activity/jd_yijia.js, activity/jd_yijiajiu.js, activity/jd_ylyn.js, activity/jd_ys.js, activity/jd_zbjmh.js, activity/jd_zoo.js, activity/jd_zooCollect.js, activity/jd_zooElecsport.js, activity/jd_zzt.js, activity/jx_mc_coin.js, activity/jx_sign_xd.js, backUp/AlipayManor.js, backUp/GetJdCookie.md, backUp/GetJdCookie2.md, backUp/GetJdCookie3.md, backUp/JDJRValidator_Smiek.js, backUp/JD_extra_cookie.js, backUp/Jd_jrValidator.js, backUp/MovementFaker.js, backUp/README.md, backUp/TG_PUSH.md, backUp/ZooFaker_Necklace.js, backUp/aclog.png, backUp/elecV2P.md, backUp/getJDCookie.js, backUp/gitSync.md, backUp/githubAction.md, backUp/iCloud.md, backUp/iOS_Weather_AQI_Standard.js, backUp/index.js, backUp/jdFruitShareCodes.js, backUp/jdJxncShareCodes.js, backUp/jdJxncTokens.js, backUp/jdUA.py, backUp/jd_11RedEnvelope.js, backUp/jd_1212red.js, backUp/jd_15_5.js, backUp/jd_19_6.js, backUp/jd_29_8.js, backUp/jd_5_2.js, backUp/jd_DrawEntrance.js, backUp/jd_MMdou.js, backUp/jd_Supershophf.js, backUp/jd_all_bean_change.js, backUp/jd_angryKoi_all.js, backUp/jd_appliances.js, backUp/jd_bean_change.js, backUp/jd_bean_day_change.js, backUp/jd_bean_month_change.js, backUp/jd_beauty_ex.js, backUp/jd_beauty_plant.py, backUp/jd_big_winner.js, backUp/jd_bzlshdgt.js, backUp/jd_car.js, backUp/jd_carnivalcity.js, backUp/jd_cash_exchange.js, backUp/jd_cfd.js, backUp/jd_cfd_SlotMachine.js, backUp/jd_cfd_fresh.js, backUp/jd_cfd_fresh_exchange.js, backUp/jd_cfd_loop.js, backUp/jd_cfd_mooncake.js, backUp/jd_cfd_mooncake_help.js, backUp/jd_cfd_pearl.js, backUp/jd_cfd_pearl_ex.js, backUp/jd_cfdtx.js, backUp/jd_chinaJoy.js, backUp/jd_city_exchange.js, backUp/jd_citytx.js, backUp/jd_cjzdgf.js, backUp/jd_cleancart.js, backUp/jd_collectcardhelp.js, backUp/jd_crazy_joy.js, backUp/jd_crazy_joy_bonus.js, backUp/jd_crazy_joy_coin.js, backUp/jd_daily_egg.js, backUp/jd_daily_lottery.js, backUp/jd_ddPlayer.js, backUp/jd_ddgame.js, backUp/jd_ddo_pk.js, backUp/jd_ddwj.js, backUp/jd_ddwj_help.js, backUp/jd_decompression.js, backUp/jd_delCoupon.js, backUp/jd_djjl.js, backUp/jd_dreamFactory.js, backUp/jd_dt.js, backUp/jd_dtld.js, backUp/jd_earn30.js, backUp/jd_enen.js.bak, backUp/jd_europeancup.js, backUp/jd_exchangejxbeans.js, backUp/jd_family.js, backUp/jd_fan.js, backUp/jd_fc.js, backUp/jd_fcwb.js, backUp/jd_finance.js, backUp/jd_fission.js, backUp/jd_freshgoods.js, backUp/jd_fruit.js, backUp/jd_getFollowGift.py, backUp/jd_goldPhone.js, backUp/jd_goodMorning.js, backUp/jd_gyp.js, backUp/jd_half_redrain.js, backUp/jd_hb_a.js, backUp/jd_health.js, backUp/jd_health_exchange.py, backUp/jd_health_plant.py, backUp/jd_hwsx.js, backUp/jd_hyj.js, backUp/jd_industrial_task.js, backUp/jd_industryLottery.js, backUp/jd_jchsign.js, backUp/jd_jika.js, backUp/jd_jingsubang.js, backUp/jd_jmofang.js, backUp/jd_joy.js, backUp/jd_joy_feedPets.js, backUp/jd_joy_help.js, backUp/jd_joy_park_newtask.js, backUp/jd_joy_run.js, backUp/jd_joy_sendcard_all.py, backUp/jd_joy_steal.js, backUp/jd_joy_tx.js, backUp/jd_joyjd_open.js, backUp/jd_joyjd_open_list.js, backUp/jd_jump.js, backUp/jd_jxcfd_cash100.py, backUp/jd_jxd.js, backUp/jd_jxdzz.js, backUp/jd_jxg.js, backUp/jd_jxlhb.js, backUp/jd_jxmc_mkmb.js, backUp/jd_jxnc.js, backUp/jd_jxnnfls.py, backUp/jd_jxzpk.js, backUp/jd_kanjia.js, backUp/jd_kanjia3.js, backUp/jd_king.js, backUp/jd_kj.js, backUp/jd_kws.js, backUp/jd_kxcdz.js, backUp/jd_kyd.js, backUp/jd_ldhwj.js, backUp/jd_live_redrain.js, backUp/jd_lotteryMachine.js, backUp/jd_lottery_drew.js, backUp/jd_lsj.js, backUp/jd_lxLottery.js, backUp/jd_mall_active.js, backUp/jd_market_lottery.js, backUp/jd_mb.js, backUp/jd_mf_exchange.js, backUp/jd_mfexchange.js, backUp/jd_mhtask.js, backUp/jd_mhyyl.js, backUp/jd_mofang_ex.js, backUp/jd_mohe.js, backUp/jd_mpdzcar.js, backUp/jd_mpdzcar_game.js, backUp/jd_mpdzcar_help.js, backUp/jd_ms.js, backUp/jd_necklace_new.js, backUp/jd_newTreasure.py, backUp/jd_ns_open.js, backUp/jd_nsjdlot.js, backUp/jd_nyx_help.js, backUp/jd_nzmh.js, backUp/jd_olympicgames.js, backUp/jd_pet.js, backUp/jd_phone.js, backUp/jd_plantBean.js, backUp/jd_ppdz.js, backUp/jd_ppkhr.js, backUp/jd_price.js, backUp/jd_qcshj.js, backUp/jd_qixi.js, backUp/jd_qjd.js, backUp/jd_qmwxj.js, backUp/jd_redrain.js, backUp/jd_redrain_half.js, backUp/jd_sendBeans.js, backUp/jd_sevenDay.js, backUp/jd_shop.js, backUp/jd_sign_graphics1.js, backUp/jd_sjnhj.js, backUp/jd_speed.js, backUp/jd_spider_requests.py, backUp/jd_spnvjd.js, backUp/jd_sq.js, backUp/jd_summer_exchange.js, backUp/jd_summer_movement.js, backUp/jd_summer_movement_help.js, backUp/jd_superBrand2.js, backUp/jd_superMarket.js, backUp/jd_superbox.js, backUp/jd_sxLottery.js, backUp/jd_task.json, backUp/jd_tcl.js, backUp/jd_team60.js, backUp/jd_teamAnJia.js, backUp/jd_teamFLP.js, backUp/jd_travel.js, backUp/jd_travel_shop.js, backUp/jd_twlove.js, backUp/jd_twmsdtt.js, backUp/jd_twoly.js, backUp/jd_twzStar.js, backUp/jd_tyt.js, backUp/jd_unbind.js, backUp/jd_unsubscriLive.js, backUp/jd_unsubscribe.js, backUp/jd_userAwardExpandinfo.py, backUp/jd_utils.js, backUp/jd_wish.js, backUp/jd_wjcj.js, backUp/jd_wxCollectionActivity.js, backUp/jd_wxShopFollowActivity.js, backUp/jd_wxj.js, backUp/jd_xiaolongfan.js, backUp/jd_xlong.js, backUp/jd_xmGame.js, backUp/jd_xqscjd.js, backUp/jd_xsqjd.js, backUp/jd_xtc.js, backUp/jd_xtg.js, backUp/jd_xxy.js, backUp/jd_xyhy.js, backUp/jd_year.js, backUp/jd_yijia.js, backUp/jd_ys.js, backUp/jd_zd.js, backUp/jd_zdjr.js, backUp/jd_zjb.js, backUp/jd_zzt.js, backUp/jddj_bean.js, backUp/jinli_log.js, backUp/jx_cfd_pearl_exchange.js, backUp/jx_mczn_exchange.js, backUp/jx_sign_xd.js, backUp/killck.js, backUp/mengniu.js, backUp/mySelf.boxjs.json, backUp/redrian_user.py, backUp/reposync.md, backUp/rush_anjia.js, backUp/sendNotify.js, backUp/tencentscf.md, backUp/webhook.js, backUp/xmSports.js, bot_jd_bean_change.js, boxjs.json, cleancart_activity.js, config.json, docker/Dockerfile, docker/README.md, docker/Readme.md, docker/auto_help.sh, docker/bot/jd.png, docker/bot/jd_bot, docker/bot/requirements.txt, docker/bot/setup.py, docker/default_task.sh, docker/docker-compose.yml, docker/docker_entrypoint.sh, docker/example/custom-append.yml, docker/example/custom-overwrite.yml, docker/example/default.yml, docker/example/docker\345\244\232\350\264\246\346\210\267\344\275\277\347\224\250\347\213\254\347\253\213\345\256\271\345\231\250\344\275\277\347\224\250\350\257\264\346\230\216.md, docker/example/jd_scripts.custom-append.syno.json, docker/example/jd_scripts.custom-overwrite.syno.json, docker/example/jd_scripts.syno.json, docker/example/multi.yml, docker/extra.sh, docker/notify_docker_user.js, docker/proc_file.sh, docker/task_before.sh, function/JDJRValidator_Pure_smiek.js, function/TS_USER_AGENTS.ts, function/common.js, function/config.js, function/eval.js, function/jdValidate.js, function/jdcookie.js, function/jinli_log.ts, function/jxAlgo.js, function/magic.js, function/ql.js, function/sendNotify.js, function/sign_graphics_validate.js, getJDCookie.js, githubAction.md, gua_MMdou.js, gua_cleancart_ddo.js, gua_opencard115.js, gua_opencard117.js, gua_opencard118.js, gua_opencard127.js, gua_opencard128.js, gua_opencard129.js, gua_opencard130.js, gua_opencard131.js, gua_opencard132.js, gua_wealth_island.js, gua_wealth_island_help.js, index.js, jdEnv.py, jd_10-4.js, jd_15_8.js, jd_19-5.js, jd_19_5.js, jd_5_2.js, jd_CheckCK.js, jd_CkSeq.js, jd_DailyBonus_Mod.js, jd_OpenCard.py, jd_OpenCard_Force.js, jd_UpdateUIDtoRemark.js, jd_angryBean.js, jd_bean_change.js, jd_bean_change1.js, jd_bean_home.js, jd_bean_info.js, jd_bean_sign.js, jd_beans_7days.py, jd_beauty.js, jd_beauty_ex.js, jd_beauty_plant.py, jd_captian_anjia.js, jd_car.js, jd_carnivalcity.js, jd_cash_Mod_Panda.js, jd_cash_exchange.js, jd_cash_wx.js, jd_cfd.js, jd_cfd_fresh.js, jd_cfd_hb.js, jd_cfd_loop.js, jd_cfd_mooncake.js, jd_cfd_pearl.js, jd_cfd_pearl_ex.js, jd_cjzdgf.js, jd_cleancart.js, jd_club_lottery.js, jd_daily_egg.js, jd_daily_lottery.js, jd_ddnc_farmpark.js, jd_delCoupon.js, jd_delete_coupon.js, jd_dpqd.js, jd_dpsign.js, jd_dreamFactory.js, jd_dreamFactory_help.js, jd_dreamFactory_tuan.js, jd_duobao.js, jd_dwapp.js, jd_exchangejxbeans.js, jd_family.js, jd_fan.js, jd_farautomation.js, jd_fcwb.js, jd_fcwb.py, jd_follow_shop.js, jd_fruit.js, jd_fruit_Mod.js, jd_fruit_friend.js, jd_fruit_plant.ts, jd_fruit_task.js, jd_getFollowGift.py, jd_gjlh.js, jd_gold_creator.js, jd_goodMorning.js, jd_gua_cleancart_Panda.js, jd_half_redrain.js, jd_hbCount.py, jd_health.js, jd_health_collect.js, jd_health_exchange.py, jd_health_help.js, jd_health_plant.py, jd_jdfactory.js, jd_jdfactory_help.js, jd_jdzz.js, jd_jfcz.js, jd_jieMo.js, jd_jin_tie.js, jd_jinli_hongbao.ts, jd_joy_feedPets.js, jd_joy_park.js, jd_joy_park_Mod.js, jd_joy_park_task.js, jd_joy_reward_Mod.js, jd_joy_run.js, jd_joy_steal.js, jd_joy_tx.js, jd_joyjd_open.js, jd_joypark_open.js, jd_js_sign.js, jd_jump.js, jd_jx_sign.js, jd_jxg.js, jd_jxgckc.js, jd_jxhlk.py, jd_jxlhb.js, jd_jxmc.js, jd_jxmc_hb.js, jd_jxnc.js, jd_jxnn.js, jd_kanjia.js, jd_kd.js, jd_live.js, jd_live_redrain.js, jd_lotteryMachine.js, jd_lzdz1_customized1.js, jd_lzdz1_customized10.js, jd_lzdz1_customized11.js, jd_lzdz1_customized12.js, jd_lzdz1_customized13.js, jd_lzdz1_customized14.js, jd_lzdz1_customized15.js, jd_lzdz1_customized16.js, jd_lzdz1_customized2.js, jd_lzdz1_customized3.js, jd_lzdz1_customized5.js, jd_lzdz1_customized9.js, jd_lzdz1_jx.json, jd_lzkjdz.js, jd_m_sign.js, jd_market_lottery.js, jd_mhtask.js, jd_mncryyj.js, jd_mofang.js, jd_mofang_ex.js, jd_mohe.js, jd_moneyTree.js, jd_moneyTree_help.js, jd_morningSc.js, jd_mpdzcar.js, jd_mpdzcar_game.js, jd_mpdzcar_help.js, jd_ms.js, jd_nzmh.js, jd_pay_contract.js, jd_pet.js, jd_pet_automation.js, jd_petrw.js, jd_pigPet.js, jd_plantBean.js, jd_plantBean_help.js, jd_plusReward.js, jd_price.js, jd_priceProtect_Mod.js, jd_productZ4Brand.js, jd_redrain.js, jd_redrain_half.js, jd_refreshInvokeKey.js, jd_sendBeans.js, jd_sevenDay.js, jd_sgmh.js, jd_share.js, jd_shop.js, jd_shop_sign_duck.js, jd_sign.js, jd_signFree.js, jd_sign_graphics.js, jd_sign_graphics1.js, jd_speed.js, jd_speed_redpocke.js, jd_speed_sign.js, jd_speed_signred.js, jd_superBrandStar.js, jd_superMarket.js, jd_sxLottery.js, jd_test.js, jd_try.js, jd_try_notify.py, jd_tyt.js, jd_unbind.js, jd_unsubscriLive.js, jd_unsubscribe.js, jd_upgrade.js, jd_wdz.js, jd_week.js, jd_wish.js, jd_wq_wxsign.js, jd_wsdlb.js, jd_wxCollectionActivity.js, jd_wxgame.js, jd_wyw.js, jd_xinruimz.js, jd_xs_zzl.js, jd_yfcoupon.js, jd_ylyn.js, jd_zdjr.js, jd_zjb.js, jd_zjb_help.js, jddjCookie.js, jddj_bean.js, jddj_fruit.js, jddj_fruit_collectWater.js, jddj_getPoints.js, jddj_getck.js, jddj_plantBeans.js, joy_run_token.json, jx_cfd_card.js, jx_factory_automation.js, jx_sign.js, jx_sign_xd.js, lxk0301.boxjs.json, magic.json, magic.py, mount.sh, notify.md, package.json, sendNotify.js, sendNotify.py, serverless.yml, shell_script_mod.sh, sign_graphics_validate.js, test.js, tools/a.py, tools/empty.json, tools/jd_dreamFactory_product.js, utils/JDCookie.py, utils/JDJRValidator.js, utils/JDJRValidator_Pure.js, utils/JDJRValidator_Pure1.js, utils/JDSignValidator.js, utils/JD_DailyBonus.js, utils/MoveMentFaker.js, utils/MovementFaker.js, utils/TS_USER_AGENTS.ts, utils/USER_AGENTS.js, utils/ZooFaker_Necklace.js, utils/common.js, utils/config.js, utils/eval.js, utils/jdCookie.js, utils/jdShareCodes.js, utils/jdValidate.js, utils/jd_jxmcToken.js, utils/jd_sign_validate.js, utils/jdcookie.js, utils/jinli_log.ts, utils/jxAlgo.js, utils/magic.js, utils/ql.js, utils/sendNotify.js, utils/sign_graphics_validate.js, utils/sign_graphics_validate1.js]

---
## [magit/magit](https://github.com/magit/magit)@[ab801de538...](https://github.com/magit/magit/commit/ab801de53827a232b7806362fb08ca804f27c6d0)
#### Sunday 2022-04-24 14:28:35 by Jonas Bernoulli

magit-section-context-menu: Support non-section branches

We use section keymaps to implement context-sensitive menus but
branches are not always represented using sections.  To support
such "painted branches" anyway use fake sections, which closely
mirror the commit section in which the click occurred.

This admittedly is ugly and somewhat risky, but seems to work well.
`magit-section-update-highlight' would break due to this hack, so
we avoid calling it.  If it turns out that things also break due
to this kludge, then we might have to revert.

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[e58fb506ef...](https://github.com/vincentiusvin/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Sunday 2022-04-24 15:02:29 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [ROM-EXTRAS/android_frameworks_base](https://github.com/ROM-EXTRAS/android_frameworks_base)@[b9e42b1661...](https://github.com/ROM-EXTRAS/android_frameworks_base/commit/b9e42b166199c918e0eaca7e0aea47e320f013fe)
#### Sunday 2022-04-24 16:33:09 by ezio84

Hidden gestural bar: fix visual glitches when switching states

hacky way but it works (TODO: find a proper fix in the new year,
i don't have motivation to dig into navbar/keyguard code fuckery now lol)

setting the height to 1px keeps the navbar almost invisible
but fixes the annoying visual glitches when going from screen
off to ambient pulsing or lockscreen (more noticeable on some devices
like bonito)
to replicate the issue without this commit:
- screen ON, then screen off, then double tap to go to ambient,
then double tap to go to lockscreen, then double tap to switch screen off,
then switch screen on again
- or just switch screen off/on a few times with the power button

Also sync the hide pill code with Pulse hide pill feature

Change-Id: Ib1cc83492f8a091be5cac4563d844010cef69dbc

---
## [TakeFiveGames/qb-core](https://github.com/TakeFiveGames/qb-core)@[9d83a952c2...](https://github.com/TakeFiveGames/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Sunday 2022-04-24 17:07:24 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [kas-catholic/confessit-web](https://github.com/kas-catholic/confessit-web)@[e1f4dc5804...](https://github.com/kas-catholic/confessit-web/commit/e1f4dc5804740d506df16e16d0795411203c4eba)
#### Sunday 2022-04-24 17:52:28 by Mike

Update Examination

A deacon reached out to me via email to note that suicidal thoughts are
not in themself sinful (though could be a sign of depression, anxiety,
or other mental illness and might still require help). As such, we
should update the text to read simply,

> Did I attempt suicide?

CCC 2281-2283

---
## [crdroidandroid/android_kernel_oneplus_sm7250](https://github.com/crdroidandroid/android_kernel_oneplus_sm7250)@[e445f775b0...](https://github.com/crdroidandroid/android_kernel_oneplus_sm7250/commit/e445f775b0124a68287982fe38bdc66765eef0d7)
#### Sunday 2022-04-24 19:29:39 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [Kuuuuuuuu/julia](https://github.com/Kuuuuuuuu/julia)@[62e0729dbc...](https://github.com/Kuuuuuuuu/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Sunday 2022-04-24 21:16:25 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[446f280757...](https://github.com/microsoft/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Sunday 2022-04-24 22:04:58 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[9792a6e7e6...](https://github.com/UnderMybrella/usa/commit/9792a6e7e6b549bfc534a02d4694f646f6c70746)
#### Sunday 2022-04-24 22:33:01 by MarkiSpider

Update 56 files @ Sun, 24 Apr 2022 22:32:58 GMT
This site update changes auth.html, cases.html, usa-home.html, .html, dont-push.html, LixianTV.html, employeeaccountabilitytimesignature-portal.html, cart.html, Jupiterandfriends.html, agentloginportal.html, the-asshats.html, illinois.html, corn-dm.html, thejackson5.html, gettingjiggywithit.html, legal.html, logout.html, girlofthe21stcentury.html, MichaelJackson.html, capitalism.html, fuckem.html, NerdFiction.html, terrorblycute.html, shatteredbysomeone.html, everyone.html, messenger.html, 914222-29151493191121139.html, evidence.html, evidence.html, woahhh.html, ohyouwouldlikethatwouldntyou.html, redacted.html, agencydirectory.html, karen6803.html, karen6804.html, 914222-5241612154525.html, lolgotyou.html, thefounders.html, sexygoldarms.html, the-baboonies.html, 2702-invincible2syndicate.html, case-directory.html, 914222-1916151820192112124214513114.html, Imsorrymissjackson.html, nebuchadnezzar.html, karen6816.html, cachow.html, karen6815.html, helpcenter.html, kriskringle.html, byebyebye.html, thekilleidoscope.html, para.docs-portal, suspect-hierarchy.html, karen6809.html, Rad_R.html

---
## [ahamlinman/xt](https://github.com/ahamlinman/xt)@[c5125a7658...](https://github.com/ahamlinman/xt/commit/c5125a76586eed8304025160f77bf4744698a8ee)
#### Sunday 2022-04-24 22:41:16 by Alex Hamlin

Switch back to exclusive range

I'm actually going to go ahead and disagree with clippy on this one.
Inclusive ranges are so rare in my experience compared to exclusive
ranges that I do a bit of a double take when I see one, and have to
think a lot more carefully about whether it actually does what I want.
Frankly, I think this form makes it a lot more obvious at a glance that
we're looking for a slice N bytes long offset by 1 from the start.

---
## [kulinseth/pytorch](https://github.com/kulinseth/pytorch)@[65329f4fac...](https://github.com/kulinseth/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Sunday 2022-04-24 23:24:02 by Edward Z. Yang

Disable meta device tests.

After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Pull Request resolved: https://github.com/pytorch/pytorch/pull/74468

Approved by: https://github.com/mruberry

---

