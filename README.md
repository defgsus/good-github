## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-06](docs/good-messages/2022/2022-06-06.md)


1,774,738 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,774,738 were push events containing 2,749,974 commit messages that amount to 215,204,767 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [K-Kumar-01/vitess](https://github.com/K-Kumar-01/vitess)@[dbfb9a49f7...](https://github.com/K-Kumar-01/vitess/commit/dbfb9a49f7c3b067221d0aae0d3c0285e6baf098)
#### Monday 2022-06-06 00:41:04 by Andrew Mason

[vtadmin] Add infrastructure for generating authz tests for vtadmin (#10397)

* Add infrastructure for generating authz tests for vtadmin

The lack of verifying authz checks are where they should be is one of the
most glaring issues in vtadmin (in my opinion; it's also my "fault" things
are this way). At the same time, writing all the code by hand to verify
every single endpoint would be a giant pain (which is the main reason
things are this way). So, let's codegen all the bits we don't care about!
The bonus here is that the config.json now can serve as authoritative on
what permissions are required for what endpoints.

The goal here is to have the config primarily specify the rules needed for
each endpoint, with as minimal "overhead" (currently specifying test cases
and mock data) as possible.

I want to separate the introduction of this setup from its complete
adoption, so I will submit a follow-up change that adds the rest of the
endpoint tests.

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* add missing license headers

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* Add make target and CI check

Signed-off-by: Andrew Mason <andrew@planetscale.com>

---
## [SgtHunk/tgstation-1](https://github.com/SgtHunk/tgstation-1)@[d411393e72...](https://github.com/SgtHunk/tgstation-1/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Monday 2022-06-06 01:01:01 by Zytolg

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
## [SgtHunk/tgstation-1](https://github.com/SgtHunk/tgstation-1)@[4652d4bb63...](https://github.com/SgtHunk/tgstation-1/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Monday 2022-06-06 01:01:01 by Jolly

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
## [SgtHunk/tgstation-1](https://github.com/SgtHunk/tgstation-1)@[b86cf89125...](https://github.com/SgtHunk/tgstation-1/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Monday 2022-06-06 01:01:01 by Aleksej Komarov

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
## [13spacemen/tgstation](https://github.com/13spacemen/tgstation)@[cd294e9040...](https://github.com/13spacemen/tgstation/commit/cd294e9040505e73e46384d6166015afa43217f3)
#### Monday 2022-06-06 01:13:22 by vincentiusvin

Scipaper rebalancing: Nitrium and halon shell removal. Nitrous added. Emphasis on BZ. (#66738)

Similar in spirit to #65707, with some more changes.

Restructured the gaseous experiments to:

    Nitrous (practice experiment)
    BZ (mainstay experiment)
    Hyper-Nob (lategame/once-in-a-while experiment)

Added a mining partner.

Moved adv weaponry lock to normal weaponry under reactionless. Toned down t3 reactionless.

BZ locks adv engi. Medbay unbridled by toxin gasses now.

Removed Xenobio's BZ Can.
Why It's Good For The Game

My original intent with papers was expanding the difficulty range of toxins. Both to things harder than tritium (nob, nitrium, etc) and also to things easier than tritium (bz, reactionless, etc).

In that process, I feel that i strayed a bit to the harder side, this PR is an attempt to tone down the overall difficulty of some of the gaseous experiments a notch.

Nitrous now takes place of the old BZ, BZ takes place of old nitrium/halon, and noblium stays because it's difficulty is in a pretty good spot for a relatively unimportant but nice to have tech.

While we're at it, I also added more emphasis to BZ production to toxins instead of tritium. This will hopefully incentivize people to try the department out. There is a risk of this being a bit of a chore, but I believe that the relevant atmos gameplay loop is strong enough to have it be fun. You need to check on the chamber, turn on pipes, adjust the input rate, and many more that makes it significantly more fun to do.

We do this by:

    Locking advanced engineering with BZ (organs and implants lock lifted). Depending on feedback i wont mind changing this around if you want to suggest another node as long as it's of similar or very slightly less importance.

    Getting rid of xeno's BZ can. Some xeno players need it for making slimes sleep, with their roundstart supply removed there should be a significant demand for the BZ production in toxins to go online asap.

If you have been paying attention to our PRs, i have been working to make BZ production as seamless and quick as possible in toxins. My five map prs #66454 #66198 #66064 #66010 #65857 have been building up to this. You can make BZ relatively quickly with the new freezer chamber in place. Probably even faster than ordering it in cargo, which is a fine ballpark to use if you want to make changes to it.

If you want to know how to operate it, here is a wiki guide in place https://tgstation13.org/wiki/User:Vincentius_vin/Sandbox#BZ_Synthesis. We will move it to the main toxins page once the rest of the page is finished, pictures are added, 

Made adv engi tech node require bz shells as an experiment, organs no longer need it.
Adv mining no longer requires adv engi.
Removed nitrium and halon shell, implant experiment lock lifted because of the former.
Relocked sec 1 tech node to need pressure bombs, sec 2 no longer needs tritium bomb.
Made advanced pressure bombs easier to do without funny fusion gases.
Added a new mining partner that accepts smaller (even non-atmos/non-ordnance related) bombs
Added more options to purchase nodes in the paper partners. Your point gain stays the same though.
Removed roundstart BZ can from xenobio.

---
## [13spacemen/tgstation](https://github.com/13spacemen/tgstation)@[245ec35dae...](https://github.com/13spacemen/tgstation/commit/245ec35dae59d0edc92663ccb8012b27d5e1a198)
#### Monday 2022-06-06 01:13:22 by LemonInTheDark

Removes (in) smoke and foam reactions (#67270)

* Removes smoke and foam reactions

Turns out when you let reagents react in foam/smoke, people put bombs in
them.

This behavior was initially added to just smoke, accidentially in
(56f7ac0c0a29e8f898c4aab35947d027952b43f7) accidentialy (thalpy tried to
make both foam and smoke instant react, but instead made smoke's temporary
holder reagent instant instead. hhhhhhh)

Assuming this was intentional it was then extended to foam in
(1879e2d338c9bf5f191cef6c39944b26a41e6092)

Basically, we're idiots. Anyway lets just walk this all back to instant
reaction on smoke/foam formation. Hate you people

* Removes another source of gunpowder smoke

Temporal told me about this. Gunpowder uses an ex_act signal as a
starter, and that also counts for smoke objects.

Really don't want instant detonation smoke bombs, so let's just... not
shall we?

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[92fda5014d...](https://github.com/timothymtorres/tgstation/commit/92fda5014dbc8ba64c19848e693c179af35da2ac)
#### Monday 2022-06-06 01:26:46 by san7890

Makes Hell Microwaves Not Use Power (#67413)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[27946f516d...](https://github.com/Zytolg/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Monday 2022-06-06 01:27:34 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [wbprime/dwm](https://github.com/wbprime/dwm)@[67d76bdc68...](https://github.com/wbprime/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2022-06-06 02:23:22 by Chris Down

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
## [Fiscal2/JSwebsite](https://github.com/Fiscal2/JSwebsite)@[c2857f55b8...](https://github.com/Fiscal2/JSwebsite/commit/c2857f55b82ec3e51e17db38b5f569d6b4840170)
#### Monday 2022-06-06 03:44:54 by Fiscal2

the stupid fucking button...I cant do shit push...

---
## [weebcyberpunk/petit](https://github.com/weebcyberpunk/petit)@[d6b4b9bfe3...](https://github.com/weebcyberpunk/petit/commit/d6b4b9bfe389b47c35bfed00efaa69171b4eac09)
#### Monday 2022-06-06 04:00:41 by GG

Hell yeah I wrote this shit from scratch in about 4 hours

---
## [TheNeoGamer42/Echo13](https://github.com/TheNeoGamer42/Echo13)@[91795aa57f...](https://github.com/TheNeoGamer42/Echo13/commit/91795aa57f5ecc4aeee81e91a50e08de0d960be5)
#### Monday 2022-06-06 04:02:00 by TheNeoGamer42

Arrowhead-Class Long Range Scoutship (#111)

* woo

* i kinda fucking forgot i moved an entire room and that there was a wall there now

* god fucking damnet the other wall too

* wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwires

* you know this really throws a wrench in my plans, you know? I hate wrenches in my plans.

* slightly less sane piping to infuriate both myself and others. also a waste hookup for that portable scrubber I threw in.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[b9364eed92...](https://github.com/ammarfaizi2/linux-fork/commit/b9364eed9232f3d2a846f68c2307eb25c93cc2d0)
#### Monday 2022-06-06 04:26:36 by Douglas Anderson

drm/msm/dpu: Move min BW request and full BW disable back to mdss

In commit a670ff578f1f ("drm/msm/dpu: always use mdp device to scale
bandwidth") we fully moved interconnect stuff to the DPU driver. This
had no change for sc7180 but _did_ have an impact for other SoCs. It
made them match the sc7180 scheme.

Unfortunately, the sc7180 scheme seems like it was a bit broken.
Specifically the interconnect needs to be on for more than just the
DPU driver's AXI bus. In the very least it also needs to be on for the
DSI driver's AXI bus. This can be seen fairly easily by doing this on
a ChromeOS sc7180-trogdor class device:

  set_power_policy --ac_screen_dim_delay=5 --ac_screen_off_delay=10
  sleep 10
  cd /sys/bus/platform/devices/ae94000.dsi/power
  echo on > control

When you do that, you'll get a warning splat in the logs about
"gcc_disp_hf_axi_clk status stuck at 'off'".

One could argue that perhaps what I have done above is "illegal" and
that it can't happen naturally in the system because in normal system
usage the DPU is pretty much always on when DSI is on. That being
said:
* In official ChromeOS builds (admittedly a 5.4 kernel with backports)
  we have seen that splat at bootup.
* Even though we don't use "autosuspend" for these components, we
  don't use the "put_sync" variants. Thus plausibly the DSI could stay
  "runtime enabled" past when the DPU is enabled. Techncially we
  shouldn't do that if the DPU's suspend ends up yanking our clock.

Let's change things such that the "bare minimum" request for the
interconnect happens in the mdss driver again. That means that all of
the children can assume that the interconnect is on at the minimum
bandwidth. We'll then let the DPU request the higher amount that it
wants.

It should be noted that this isn't as hacky of a solution as it might
initially appear. Specifically:
* Since MDSS and DPU individually get their own references to the
  interconnect then the framework will actually handle aggregating
  them. The two drivers are _not_ clobbering each other.
* When the Qualcomm interconnect driver aggregates it takes the max of
  all the peaks. Thus having MDSS request a peak, as we're doing here,
  won't actually change the total interconnect bandwidth (it won't be
  added to the request for the DPU). This perhaps explains why the
  "average" requested in MDSS was historically 0 since that one
  _would_ be added in.

NOTE also that in the downstream ChromeOS 5.4 and 5.15 kernels, we're
also seeing some RPMH hangs that are addressed by this fix. These
hangs are showing up in the field and on _some_ devices with enough
stress testing of suspend/resume. Specifically right at suspend time
with a stack crawl that looks like this (from chromeos-5.15 tree):
  rpmh_write_batch+0x19c/0x240
  qcom_icc_bcm_voter_commit+0x210/0x420
  qcom_icc_set+0x28/0x38
  apply_constraints+0x70/0xa4
  icc_set_bw+0x150/0x24c
  dpu_runtime_resume+0x50/0x1c4
  pm_generic_runtime_resume+0x30/0x44
  __genpd_runtime_resume+0x68/0x7c
  genpd_runtime_resume+0x12c/0x20c
  __rpm_callback+0x98/0x138
  rpm_callback+0x30/0x88
  rpm_resume+0x370/0x4a0
  __pm_runtime_resume+0x80/0xb0
  dpu_kms_enable_commit+0x24/0x30
  msm_atomic_commit_tail+0x12c/0x630
  commit_tail+0xac/0x150
  drm_atomic_helper_commit+0x114/0x11c
  drm_atomic_commit+0x68/0x78
  drm_atomic_helper_disable_all+0x158/0x1c8
  drm_atomic_helper_suspend+0xc0/0x1c0
  drm_mode_config_helper_suspend+0x2c/0x60
  msm_pm_prepare+0x2c/0x40
  pm_generic_prepare+0x30/0x44
  genpd_prepare+0x80/0xd0
  device_prepare+0x78/0x17c
  dpm_prepare+0xb0/0x384
  dpm_suspend_start+0x34/0xc0

We don't completely understand all the mechanisms in play, but the
hang seemed to come and go with random factors. It's not terribly
surprising that the hang is gone after this patch since the line of
code that was failing is no longer present in the kernel.

Fixes: a670ff578f1f ("drm/msm/dpu: always use mdp device to scale bandwidth")
Fixes: c33b7c0389e1 ("drm/msm/dpu: add support for clk and bw scaling for display")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Abhinav Kumar <quic_abhinavk@quicinc.com>
Tested-by: Jessica Zhang <quic_jesszhan@quicinc.com> # RB3 (sdm845) and
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@linaro.org>
Patchwork: https://patchwork.freedesktop.org/patch/487884/
Link: https://lore.kernel.org/r/20220531160059.v2.1.Ie7f6d4bf8cce28131da31a43354727e417cae98d@changeid
Signed-off-by: Abhinav Kumar <quic_abhinavk@quicinc.com>

---
## [Sector-Echo-13-Team/Echo13](https://github.com/Sector-Echo-13-Team/Echo13)@[dd3c97ece9...](https://github.com/Sector-Echo-13-Team/Echo13/commit/dd3c97ece998ea7e92a8bf1d6e93c736f1ca0203)
#### Monday 2022-06-06 04:35:04 by TheNeoGamer42

arrowhead fixes (#116)

* literally just adds two goddamn wires holy shit

* s ink

* wagoogus

---
## [EtraIV/MerchantStation13](https://github.com/EtraIV/MerchantStation13)@[144b5838c0...](https://github.com/EtraIV/MerchantStation13/commit/144b5838c01985628a46954e276f5f643596634c)
#### Monday 2022-06-06 05:09:03 by karmaisblackandbluepilled

Adds surplus crate-only items. (#256)

* Funny stuff right here

* is this piece of shit ACTUALLY complaining about indentation in a fucking comment fuck you

---
## [EtraIV/MerchantStation13](https://github.com/EtraIV/MerchantStation13)@[8c35a11b61...](https://github.com/EtraIV/MerchantStation13/commit/8c35a11b61efc2bb38c7d33bd7cb577b536d49f5)
#### Monday 2022-06-06 05:09:03 by EtraIV

Fix point vendors (#259)

* Fix point vendors bluescreening if accessed with an ID with no registered account

* You can't (brokenly) take apart point vendors anymore

* Moves the point vendors to the FUCKIGN VENDING DIRECTORY HOLY SHIT TCEO WHY DID YOU PUT THEM IN ECONOMY YOU IDIOT

---
## [EdwardGuerra25/EdwardGuerra25](https://github.com/EdwardGuerra25/EdwardGuerra25)@[3680f9864c...](https://github.com/EdwardGuerra25/EdwardGuerra25/commit/3680f9864cff1a6f4c4e46b0bb048cfad6c6bff4)
#### Monday 2022-06-06 05:25:35 by Edward Guerra 52

ABOUT ME

✊🏽 Hi I am @EdwardGuerra25 but in social networks @dont_atteishom18. 
🏀 I'm interested in life, sports and mental health of others, because in programming I'm curious but that I'm interested in not a lot but it's about.
⚰️ I am currently learning Biomedical Engineering but to be honest we are giving it as the old men say reluctantly. 
📈 I am looking to collaborate in different projects as this is a new world for me and its possibilities attract me to new ventures.
💣 How to reach me you can contact me by mail by the one that appears in my profile and if I don't answer you can send me some I have to see!

---
## [NavinShrinivas/SimpleGrep](https://github.com/NavinShrinivas/SimpleGrep)@[2bbfd342d3...](https://github.com/NavinShrinivas/SimpleGrep/commit/2bbfd342d3932d412c6ac6b4de8b57ea378c92cf)
#### Monday 2022-06-06 06:23:54 by NavinShrinivas

WTHHTHTHTHT

Signed-off-by: NavinShrinivas <karupal2002@gmail.com>

I did implement horspool algorithm, but its insanely faster than my
stupid algorithm, why? AHHHHHHH
I hate myself :(

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[28e586bb55...](https://github.com/treckstar/yolo-octo-hipster/commit/28e586bb55e7873711354bc71315c08eb55b6e1f)
#### Monday 2022-06-06 07:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [xMeerkat/xMeerkat](https://github.com/xMeerkat/xMeerkat)@[162cb87648...](https://github.com/xMeerkat/xMeerkat/commit/162cb876487ad3dcf0514e8a6ea9dde1dd518f41)
#### Monday 2022-06-06 08:41:16 by gemsvido

I'll fix this later but damn, JavaScript FUCKING SUCKS - http://xMeerkat.com

---
## [ActuallyHappening/The-WildStar-Project](https://github.com/ActuallyHappening/The-WildStar-Project)@[123e00fb78...](https://github.com/ActuallyHappening/The-WildStar-Project/commit/123e00fb786945cf420ac7401e2457683afe80ed)
#### Monday 2022-06-06 09:26:42 by Smartguy88 - Smg88

oh my gosh I am so stupid sometimes just don't
even look at my mistake!

---
## [bendavies/laminas-code](https://github.com/bendavies/laminas-code)@[061f1fddec...](https://github.com/bendavies/laminas-code/commit/061f1fddecf14eaf9d8635687efc6c46ebad4a50)
#### Monday 2022-06-06 11:19:30 by Michał Bundyra

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
## [transcom/mymove](https://github.com/transcom/mymove)@[8af1f5a031...](https://github.com/transcom/mymove/commit/8af1f5a03143dce4ab3c6aa01b8772cd2f41adb9)
#### Monday 2022-06-06 12:34:44 by Marty Boren

Very rough skeleton of move code search

after many moons of struggle, I've finally got something that
kinda works.
There's an endpoint for searching for moves.
and an office page with a search box that hits that endpoint
and drops the results in a table.

i was really struggling to get the react part of this to work without
setting off an infinite loop, so now that I've finally gotten there
i want to commit even though this is still full of debug cruft.

lots of exciting things left to do, such as:
- the moves that are returned by the endpoint are missing most of the
  stuff they should have.
- We also can't search for DoD ID
- interface for passing search info between things is inconsistent

---
## [rurban/valgrind](https://github.com/rurban/valgrind)@[6cc2d94d93...](https://github.com/rurban/valgrind/commit/6cc2d94d93fa5350355b8cedb0d6b5309fcc588c)
#### Monday 2022-06-06 14:10:14 by Paul Floyd

Use a different way to tell where the syscall handler was interrupted on FreeBSD and macOS

I was using a global variable. This would be set to '1' just before
calling the function to save cflags and cleared just after, then
using the variable to fill in the 'outside_rnage_ condition
in VG_(fixup_guest_state_after_syscall_interrupted)

Even though I haven't experienced any isseus with that, the comments just before
do_syscall_for_client made me want to try an alternative.

This code is very ugly and won't please the language lawyers.
Functions aren't guaranteed to have an address and there is no
guarantee that the binary layout will reflect the source layout.
Sadly C doesn't have something like "sizeof(*function)" to give
the size of a function in bytes. The next best that I could
manage was to use dummy 'marker' functions just after the
ones I want the end address of and then use the address of
'marker - 1'

I did think of one other way to do this. That would be to
generate a C file containing the function sizes. This would
require

1. "put_flag_size.c" would depend on the VEX guest_(x86|amd64)_helpers
   object files
2. Extract the sizes, for instance

echo -n "const size_t x86_put_eflag_c_size = 0x" > put_flag_size.c
nm -F sysv libvex_x86_freebsd_a-guest_x86_helpers.o | awk -F\| '/LibVEX_GuestX86_put_eflag_c/{print $5}' >> put_flag_size.c
echo ";" >> put_flag_size.c

That seems fairly difficult to do in automake and I'm not sure if
it would be robust.

---
## [brucerennie/NetHack](https://github.com/brucerennie/NetHack)@[e764026a1f...](https://github.com/brucerennie/NetHack/commit/e764026a1f2a005742118db24be71ae4ec270e38)
#### Monday 2022-06-06 15:17:44 by PatR

more wish logging - show the result

Extend the log event for a wish to include what was produced.  It
would be better to show the item as fully ID'd but then #chronicle
gives away information.

The backslash+newline pairs were inserted for this log message.  In
the game and in dumplog those two lines are each one wide line.  The
turn numbers shown are actually arbitrary since ^W takes no time.

|Logged events:
| Turn
|    1: wizard the chaotic male orcish Wizard entered the dungeon
|    2: made his first wish - "protection", got "a tattered cape"
|    3: made his first artifact wish - "blessed +2 rustproof magicbane",\
 got "an athame named Magicbane"
|    4: wished for "master key of thievery", got "a key named The Master\
 Key of Thievery"

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[694d059288...](https://github.com/mrakgr/The-Spiral-Language/commit/694d059288f7cac0f032282d19b427b60c8b140f)
#### Monday 2022-06-06 16:44:19 by Marko Grdinić

"2:15pm. I am tired. Honestly, if every day gave me fortuitous encounters like this, I'd long have achieved transcendence.

Yesterday I gave up on the Blender plugin plan, but now it occurs to me that it is alive again. Which is just as well, since my plan was to study the code, but now I have an actual reason for doing that.

2:25pm. When it is time to resume, I think what I will do is first post this batch on my Twitter.

3:10pm. Enough Legendary Mechanic. It is time to start getting ready for the next session. Let chill a bit more and I will start.

3:55pm. I've done a few more images. Right now I am forming an opinion on CAST. It is pretty good. Compared to other methods it is less stylized and preserves the salient features of the original better. But whether it is better depends on what you are going for. Still, I will go for it as it is so easy to use compared to NNST.

I've been trying to make ML work for me for so long, and look at this. It came to me in literally a snap. Without a doubt, this path is the true path. Being able to do style transfer like this eliminates the primary weakness of 3d.

5pm. Done with the tweeting spree.

5:20pm. Somehow I really like that image of the crab I posed in the wip thread. It is not noisy in the way that my own image is. In fact it is clean in the way I'd prefer the anime style to be. If I want a cleaner look I'll really have to learn how to denoise my Luxcore products. I think I turned on the option, so why didn't it do the job?

No, actually I did not turn on the option. The reason for that is because it is not using Nvidia's denoiser, but the slow CPU ones. I didn't want to bother testing if it does it during rendering or just at the end. If I ever use Luxcore again I should make it a priority to try it out.

5:25pm. Looking at the crab image it occured to me that the nature of the blur operation changes with CAST. Rather than the image really being blurry like in the photo, it is instead drawn with large strokes. Contrasted with the high detail, tiny strokes used to draw the drab, it looks really great. It has a ton of watermarks over it, which I did not post on Twitter.

5:30pm. I am just engrossed in my own imagination. I need to get on with it.

Even though I've been doing nothing, but making posts all day today, it took a lot out of me. I've been mentally active for 9h already.

5:40pm. https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/qa.md

Right now I am reading this. It seems the CAST authors are either related to the CycleGAN authors or they've adapted their code in a big way.

5:45pm. I am thinking what I want to do right now. I do not have the mental energy for an in depth code dive. Let me read the paper again. What did they say about future improvements?

> In the future, we plan to improve the contrastive style learning process by considering artist and category information

Ah, I see.

5:50pm. Right now, I do not really understand how CAST works. Vanilla style transfer sure, but CAST is doing something else.

6:20pm. > To maintain the content information of the content image in the process of style transfer between the two domains, we also add a cycle consistency loss:

What is this for? How does this make sense. I think the repo does not have the training code yet.

> The results of using other backbones are shown in the supplementary materials.

Supplementary materials?

6:30pm. I've read the paper again. I think I understand it better now, but I do not really understand the paired inputs in the generator. I'll want to check out Cycle GAN and some of the references they are borrowing their tricks from.

6:35pm. Hmmmm, no let's leave it at this. My brain needs time to unwind.

Come to think of it, NN denoising is a thing. Since it is too late to do it the regular way, maybe I should try that?

Nevermind it for now. My goal for tomorrow should be simple - I'll walk myself through the code and see if I can go even higher than 1.4k. I can't imagine not having neough memory for 2k images. It is one thing to hold a large number of intermediaries through 30 layers of training, but passing it feedforward through the net should not be a problem even for my GTX 970.

6:40pm. In order to achieve that goal, I will need more insight into the code, hence I have a motivation to actually study it besides pure curiosity.

Let me have lunch. I am done for the day."

---
## [aslenofarid/kernel_asus_sdm660](https://github.com/aslenofarid/kernel_asus_sdm660)@[a84746c9d6...](https://github.com/aslenofarid/kernel_asus_sdm660/commit/a84746c9d61dc9bb450d3e678c7a634b08717cd4)
#### Monday 2022-06-06 16:50:39 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db

---
## [OoLunar/DSharpPlus](https://github.com/OoLunar/DSharpPlus)@[8380b5b2de...](https://github.com/OoLunar/DSharpPlus/commit/8380b5b2deb9f2243c87e3277a34902ec08bb716)
#### Monday 2022-06-06 17:06:54 by InFTord

[ci-skip] Fix docs typos in DiscordRestClient (#1317)

* Update DiscordRestClient.cs

* insanity

edited all of this with github site editor
madness
editing 2k lines of code is kinda pain with github site editor

* im idiot

* fixing...

* uh oh

* i love fixing docs

* fixing inconsistent ID stuff..

---
## [nvanbenschoten/cockroach](https://github.com/nvanbenschoten/cockroach)@[f782e45fd0...](https://github.com/nvanbenschoten/cockroach/commit/f782e45fd0da015396bc758e855535a951f2e21a)
#### Monday 2022-06-06 19:11:42 by Andrei Matei

util/timeutil: don't strip mono time in timeutil.Now

Our timeutil.Now() insists on returning UTC timestamps, for better or
worse. It was doing this by calling time.Now.UTC(). The rub is that the
UTC() call strips the monotonic clock reading from the timestamp.
Despite repeatedly trying ([1]), I've failed to find any reasonable
reason for that behavior. To work around it, this patch does unsafe
trickery to get a UTC timestamp without stripping the monos.

Stripping the monos has the following downsides:
1. We lose the benefits of the monotonic clock reading.
2. On OSX, only the monotonic clock seems to have nanosecond resolution. If
we strip it, we only get microsecond resolution. Besides generally sucking,
microsecond resolution is not enough to guarantee that consecutive
timeutil.Now() calls don't return the same instant. This trips up some of
our tests, which assume that they can measure any duration of time.
3. time.Since(t) does one less system calls when t has a monotonic reading,
making it twice as fast as otherwise:
https://cs.opensource.google/go/go/+/refs/tags/go1.17.2:src/time/time.go;l=878;drc=refs%2Ftags%2Fgo1.17.2

An alternative considered was setting the process' timezone to UTC in an
init(): time.Local = time.UTC. That has downsides: it makes cockroach
more unpleasant to link as a library, and setting the process timezone
makes the timestamps not roundtrip through marshalling/unmarshalling
(see [1]).

[1] https://groups.google.com/g/golang-nuts/c/dyPTdi6oem8

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[b1caf70d10...](https://github.com/willior/Action_RPG_1/commit/b1caf70d101ed9f8faaee278619c1d299e9ed9f7)
#### Monday 2022-06-06 19:12:00 by willior

Update TileMapTest.tscn

created a TileMap with stairs though it's not implemented properly. the individual staircase tiles have to be AutoTile regions, but when placing them on the World, AutoTile needs to be disabled otherwise it messes with the Ridge AutoTile bitmask. i've tried setting bitmasks on the stairs' AutoTile regions but that doesn't seem to work. so the only way to create maps this way would be to lay out all AutoTile tiles FIRST, before any stairs, then disable autotile and place stairs and hope you don't fuck up.
this is an extremely stupid way of doing things, and i hope to god there is a workaround. every time i try to make tilesets i'm appalled by how horribly designed this system is, and how horribly lacking the documentation is. so it becomes literally impossible to learn how to do anything using this system. it makes getting anything but the bare basics done absolutely impossible. zero documentation, zero intuitively designed tools.
maybe Atlas tiles are the solution, or maybe making one single AutoTile region - but i don't know how the system accounts for identical bitmasks. so either one of two things can occur from here: 1. i waste a colossal amount of time trying to learn this system, and don't; 2. i waste a colossal amount of time trying to learn this system, and realize how useless it is because it seems like manually placing tiles is faster than trying to deal with this garbage nonsense.

---
## [dfinity/motoko](https://github.com/dfinity/motoko)@[e883348f8a...](https://github.com/dfinity/motoko/commit/e883348f8a35c0925d7363cc6b9488fdac261a29)
#### Monday 2022-06-06 19:17:07 by Gabor Greif

feat: introduce array-slice processing for compacting GC (#3231)

This PR introduces a modified marking (and visiting) technique for array fields, where `Array`s are GC-ed by considering their suffixes as slices, pushing these on the mark stack as bulk collections, and treating the fields in the prefix as individual objects being pushed onto the mark stack.

Following key changes are made:
- when visiting an `Array` in the dynamic heap we consult a new callback that can opt-out of the individual processing of some suffix of the array (by returning an index smaller than the array length)
- fields before this index will be processed as before by the first callback
- for the suffix the new callback is in charge to perform the bulk action
- in case of array marking, the new callback checks if the current slice is longer than some cutoff, and if so, it will push the array and the start of the suffix to the mark stack. (We abuse the tag entries as the start index for the suffix slice, so the cutoff must be numerically bigger than the biggest heap tag; this invariant is enforced)
- when pulling entries `(obj, tag)` from the mark stack a `tag >= TAG_ARRAY_SLICE_LOW_LIMIT` indicates that we have to deal with a suffix slice of an `Array`. The visitor will then again check the slice's length and do the subdivision again, as necessary.

This way of treating suffix-slices as pseudo-heapobjects originates from the suggestion of @ulan in a SGM (2022-05-30). It sidesteps the issue with layering violations, and restricts the handling of pseudo-tags to a very restricted portion of the collector source code, viz. the pushing of the range, and the visitor's case analysis on the tag, which now needs to  know about the suffix slices. Fortunately the visitor already accepts the heap tag as an argument (and doesn't extract it from the object; which would be unreliable due to threading), so the appearance of pseudo-tags is not a big deal.

The cutoff is currently chosen as 127, so for any `Array` at most 128 new entries are being placed on the mark stack.

The charm of this solution is that the same code is doing the marking pushing/popping and visiting as before, only that now it happens in an interleaved manner. The mark is already present on the array, so no reëntrancy can't occur, and eventually all its fields get processed.

-----

Below is an account of how field-by-field marking, pushing and visiting was done formerly (still in use for prefix portion of arrays), and an aborted attempt to a scheme as suggested by @osa1. I leave it for reference.

----------
See #2903. This reduces the marking stack traffic for GC-ed arrays substantially. Not applicable to copying GC!

## Status quo

Here is what happens to an array object's (single) field while `mark_fields`:
 - considered only when it is a skewed pointer and points into the dynamic heap (otherwise it is a _static object_ or a _magic_, no need to GC)
 - visitor callback is invoked:
   - `mark_object` will place a bit and push to the mark stack when not marked yet
     (when being pushed onto the mark stack the (unskewed) pointer and the heap tag are remembered)
   - the field address gets `thread()`-ed when the contained object is physically located at a less or equal address than the array itself
     (threading will put the field address into the object tag saving the tag into the word where the field address points to; the old object pointer is overwritten, but may live on in the mark stack)

## How bulk marking could work (ABANDONED)

When discovering a sequence of value fields that are laid out successively in memory and a count field in front, we can do a bunch of nice shortcuts. Below items sketch the how this could work. Invariant: there must be a tag field immediately before the length field.

- the bulk visitor callback gets called with a pointer to the length field
- it decides that it is worth doing a ranged marking and divides the bulk into a (small) prefix and a non-empty suffix `(pointer_to_length, start_index)`
- set all marks corresponding to (dynamic heap) objects in the suffix to avoid re-visiting (see [open issue](#Revisit-avoidance-is-more-complicated))
- push `(pointer_to_length, start_index)` onto the mark stack, using low bits in the pointer to differentiate from `(obj, tag)` pairs
- bulk visitor callback returns the prefix length, the fields in this area will be visited individually

When it comes to popping the mark stack and there is a field range on its top we want to be as transparent as possible, but also have to perform steps that had to be skipped (relative to the proceeding on individual fields)

 - identify that the ToS is a range `(pointer_to_length, start_index)`
 - obtain a pointer to the field indexed by `start_index`
 - increment `start_index` (still remains on the stack)
 - if  `start_index` is equal to the length, pop the entry
 - check that the field is a GC-able pointer
 - if so, extract the object and the heap tag corresponding to the field
 - otherwise pop again and return that
 - apply the threading to the field address (use the invariant to get the home object and apply the threading criterion)
 - return the object and the heap tag

## Open issues

There are some ugly wrinkles in this design, that need to be addressed somehow.

### Revisit avoidance is more complicated

An object is either unmarked, in the mark stack or is being (has been) visited. When pushing entire ranges, we cannot process individual objects and as such marking and threading may happen in unexpected ways.

#### Saving the marked bit

When eagerly marking the whole range of fields, we must not drop the info whether the individual mark is already set. This is because a mark means that either an object is in the mark stack or being/have-been visited. We have two possibilities:
- mark range eagerly on push, but remember previous marks (e.g. in the unused bit of the `Value` in the fields), or
- instead mark lazily on popping an object from the range, performing the threading anyway, but never returning already marked objects.

The latter option is in conflict with what #2903 suggests, and could potentially invalidate the idea of pushing ranges at all.

#### Intervening `thread()` call after range marking

After a range has been pushed and all dynamic objects marked, an individual field with an object also referenced by the range might become threaded. In this case the tag field of that object gets overwritten, but can be distinguished from regular tags. Such objects got individually pushed and already popped from the stack, and thus have been visited. So the field in the range must be threaded, but the pointed object must be skipped (not visited again).

### Layering violation

The fact that the `pop_mark_stack` needs to know about object layout and then how to do the threading is disgusting.
Maybe there should be a callback parameter that is invoked then a non-pointer (i.e. range) entry is encountered in ToS position.

### `pointer_to_dynamic_heap` needs the heap base

If `pop_mark_stack` is to check pointers for pointing into the dynamic heap, it needs to receive the heap base, but it currently doesn't. It is open if the caller has this piece of information. (It has, what a relief!)

### Special format of `usize` passed to `push_mark_stack` and `push_range_mark_stack`

Distinguishing by the lowest bit is hacky.

## Further improvement opportunities

I spotted below optimisation tricks while reading the code.

 - `pointer_to_dynamic_heap` unskews a lot, why not compare with a `heap_base` that is 1 less?
 - `mark_object` doesn't need to get the previous mark (`bool`), but compare the (64-bit) word the mark is in whether it changed
 - `mark_object` unskews. Would it be possible to do `set_bit` using the `raw_ptr`?
 - `field_value.get_ptr() <= obj` could be `field_value.raw_ptr() + 1 <= obj` and further `field_value.raw_ptr() < obj` saving us an addition
 - can the double storing of the heap tag (by `thread` and `push_mark_stack`) be consolidated?
   (we have 2 cases for whether `thread` happens and 2 cases whether the `push_mark_stack` happens)
 - can the dynamic heap pointer check be reduced to a shift and a comparison with `BITMAP_FORBIDDEN_PTR` (at least while marking, as it is not available in copying GC)?

---
## [git/git](https://github.com/git/git)@[c472db5059...](https://github.com/git/git/commit/c472db50594861829b2ee8ba38e98cbe60432022)
#### Monday 2022-06-06 19:56:04 by Ævar Arnfjörð Bjarmason

object-file.c: do fsync() and close() before post-write die()

Change write_loose_object() to do an fsync() and close() before the
oideq() sanity check at the end. This change re-joins code that was
split up by the die() sanity check added in 748af44c63e (sha1_file: be
paranoid when creating loose objects, 2010-02-21).

I don't think that this change matters in itself, if we called die()
it was possible that our data wouldn't fully make it to disk, but in
any case we were writing data that we'd consider corrupted. It's
possible that a subsequent "git fsck" will be less confused now.

The real reason to make this change is that in a subsequent commit
we'll split this code in write_loose_object() into a utility function,
all its callers will want the preceding sanity checks, but not the
"oideq" check. By moving the close_loose_object() earlier it'll be
easier to reason about the introduction of the utility function.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [iMineLink/pcsx2](https://github.com/iMineLink/pcsx2)@[89f10e1605...](https://github.com/iMineLink/pcsx2/commit/89f10e160572063b4871bfb8d0c6ffff54f9543a)
#### Monday 2022-06-06 22:27:28 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [Kapu1178/Pariah-Station](https://github.com/Kapu1178/Pariah-Station)@[70a87f9510...](https://github.com/Kapu1178/Pariah-Station/commit/70a87f95100c290699ce5b92bb099d2f56bbb336)
#### Monday 2022-06-06 22:58:43 by Gallyus

HOLY SHIT SHUT UP (#742)

* HOLY SHIT SHUT UP

* Apply suggestions from code review

* seeba sauce

---
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[edfa15e207...](https://github.com/RigglePrime/tgstation/commit/edfa15e207b1940b698426bc8a355d5c039a0ab2)
#### Monday 2022-06-06 23:23:09 by LemonInTheDark

fixes helllag from change turf being used on a turf of the same type (#53000)

Prevents horrible lag and runtime spam, makes the ash drake fight doable again, and adds a safeguard in case of other odd turf shit.
Changelog

cl
fix: The ash drake fight is winnable again, and the game will no longer die when he goes into the lava arena attack.
/cl

---

