## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-27](docs/good-messages/2022/2022-03-27.md)


1,506,817 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,506,817 were push events containing 2,180,522 commit messages that amount to 116,174,635 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [JetaJ1/crawl](https://github.com/JetaJ1/crawl)@[9e681642b6...](https://github.com/JetaJ1/crawl/commit/9e681642b6851451cbfcbc7a92e7de4b97106055)
#### Sunday 2022-03-27 00:24:50 by Nicholas Feinberg

Tweak Mlioglotl

Make him demonic holiness to better match player expectations (re
vulnerability to holy word), and make his Lugonu abilities priestly
rather than magical.

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[55336d1e53...](https://github.com/GoblinBackwards/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Sunday 2022-03-27 00:28:45 by vincentiusvin

Atmos Control Console Refactor (and syndiebase atmos tidyup) (#65372)

Main Takeaways For Mappers:

Use monitored pathed atmos devices very carefully. Also dont put atmos_sensors willy nilly. They are used to hook to atmos control monitors.

We want to keep at most one device broadcasting for each of the atmos sensor, inlets, and outlets. Run the mapping verb Check Atmos Chamber Devices to be sure, though this might not catch everything.

Some of the warning are pretty harmless. For example if you have reconnected the "station atmos monitor" and you get no listener for distro/waste loop warning, it's safe to ignore.

I don't know what the maptainer policy is on making new subtypes for offstation content, but if you do please branch off the general ones instead of the specific gas ones. If you aren't making a new subtype, varedit the general ones too.

About The Pull Request:

Need Would prefer this to be merged before #65271 (In game atmos guide).
Not strictly necessary, just makes me sleep better knowing the handbook wont die alongside the rest of the UI.

Fixes #36668 (Atmos Monitoring Consoles don't update it's sensors to the new tank after reconnect())
Fixes #32122 (Mix console fucked after reconnecting it)

Also made the distro meter thing broadcast more info instead of just the pressure, because I'm sure nobody would care and it would make my life easier.

A small high-level overview in case this breaks again in the future:

A signal datum (not DCS) is sent by the atmospheric devices (injectors and vents) and will be received by the atmos computers. The data is then stored at the monitor object and then passed to the UI. This initial signal is sent by `broadcast_signal()`, called by `atmos_init()`.

New sensors/vents (if you can actually get them in game, still only adminspawn/wrenchables afaik) will also initiate the conversation if atmos_init() is called, so it works fine. This means you need to unwrench and re-wrench the devices if you adminspawn them though, ugh.

In case of a newly built computer, it needs to be the one that prompt the data to the devices, so we send a request signal. This is a bit inefficient since it doesnt work off of callbacks and assocs like DCS, but won't really matter since we're doing this rarely.

We only talk with the injectors and vents when necessary here, while sensors and meters keep beeping with every process_atmos() tick so they rarely break.


Why It's Good For The Game:

Messy code gone (debatable).


Refactored the atmos control console devices. The ones that hook to the big turf chambers.
Distro meter now broadcast the whole gasmix info instead of just pressure to the monitors.
Lavaland syndie's atmos chamber vents are now actually configurable. Moved a few things around to accomodate this.
Lavalannd syndie chambers hooked to distro and moved distro pipe to layer2
atmos monitors can detect reactions now.
Some minor code changes to how anomaly refinery and implosion compressor show the gas info. No changes expected, report if bug.
recoded checks for atmos chamber abnormalities in debug verbs.

---
## [sammburr/almondBread](https://github.com/sammburr/almondBread)@[0ed49e493c...](https://github.com/sammburr/almondBread/commit/0ed49e493c18539b77d17e89c4b1ab876099601e)
#### Sunday 2022-03-27 01:03:32 by sammburr

holy fucking shit frame buffers work

im fuckig crakced at prgeaming

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[770ef81a1f...](https://github.com/pariahstation/Pariah-Station/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Sunday 2022-03-27 01:34:30 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [cgaebel/magic-trace](https://github.com/cgaebel/magic-trace)@[69deb7a488...](https://github.com/cgaebel/magic-trace/commit/69deb7a488353f2b114bc2f5e90dd69eab70e72a)
#### Sunday 2022-03-27 01:54:44 by Clark Gaebel

Rework trigger modes

Replace -symbol with a "trigger mode" option. To quote my own help
text:

1) If you do not provide [-trigger], magic-trace takes a snapshot
when either it or the application under trace ends. You can Ctrl+C
magic-trace to manually trigger a snapshot.

2) If you provide [-trigger $], magic-trace will open up a
fuzzy-find dialog to help you choose a symbol to trace.

3) If you provide [-trigger <FUNCTION NAME>], magic-trace will
snapshot when the application being traced calls the given
function. This takes the fully-mangled name, so if you're using
anything except C, fuzzy-find mode will probably be easier to
use.

[-trigger .] is a shorthand for [-trigger magic_trace_stop_indicator].

Please play around with it. I think it's a easier to to use... but that's
just like my opinion, man.

---
## [cgaebel/magic-trace](https://github.com/cgaebel/magic-trace)@[59e31fa176...](https://github.com/cgaebel/magic-trace/commit/59e31fa176c162e7c68abe284a383a3113361b43)
#### Sunday 2022-03-27 02:00:06 by Clark Gaebel

Rework trigger modes

Replace -symbol with a "trigger mode" option. To quote my own help
text:

1) If you do not provide `-trigger`, magic-trace takes a snapshot
   when either it or the application under trace ends. You can Ctrl+C
   magic-trace to manually trigger a snapshot.

2) If you provide `-trigger $`, magic-trace will open up a
   fuzzy-find dialog to help you choose a symbol to trace.

3) If you provide `-trigger <FUNCTION NAME>`, magic-trace will
   snapshot when the application being traced calls the given
   function. This takes the fully-mangled name, so if you're using
   anything except C, fuzzy-find mode will probably be easier to
   use.

`-trigger .` is a shorthand for `-trigger magic_trace_stop_indicator`.

This also removes three command-line arguments that are a mix of
unnecessary and probably a bad idea to expose:

- `-delay-thresh` can be replicated by an applicationg doing this
  measurement itself. It's a very cheap operation for an application
  to add, I don't think that magic-trace is adding very much here.

- `-duration-thresh` is in the same boat as `-delay-thresh`.

- `-immediate-stop` causes issues on some kernels. Let's just remove
  it for now and revisit it in a couple years. If people actually
  want their trace to end exactly when the trigger fires, we can
  postprocess the trace output.

Please play around with this! I think it's a easier to to use... but
that's just like my opinion, man.

---
## [cgaebel/magic-trace](https://github.com/cgaebel/magic-trace)@[44df16955a...](https://github.com/cgaebel/magic-trace/commit/44df16955a0bba6fe40a9d9ee674ae292f213772)
#### Sunday 2022-03-27 02:01:26 by Clark Gaebel

Rework trigger modes

Replace `-symbol` with a "trigger mode" option. To quote my own help
text:

1) If you do not provide `-trigger`, magic-trace takes a snapshot
   when either it or the application under trace ends. You can Ctrl+C
   magic-trace to manually trigger a snapshot.

2) If you provide `-trigger $`, magic-trace will open up a
   fuzzy-find dialog to help you choose a symbol to trace.

3) If you provide `-trigger <FUNCTION NAME>`, magic-trace will
   snapshot when the application being traced calls the given
   function. This takes the fully-mangled name, so if you're using
   anything except C, fuzzy-find mode will probably be easier to
   use.

`-trigger .` is a shorthand for `-trigger magic_trace_stop_indicator`.

This also removes three command-line arguments that are, in my opinion,
a mix of unnecessary and probably a bad idea to expose:

- `-delay-thresh` can be replicated by an applicationg doing this
  measurement itself. It's a very cheap operation for an application
  to add, I don't think that magic-trace is adding very much here.

- `-duration-thresh` is in the same boat as `-delay-thresh`.

- `-immediate-stop` causes issues on some kernels. Let's just remove
  it for now and revisit it in a couple years. If people actually
  want their trace to end exactly when the trigger fires, we can
  postprocess the trace output.

Please play around with this! I think it's a easier to to use... but
that's just like my opinion, man.

---
## [acramernc/babot](https://github.com/acramernc/babot)@[183d89af66...](https://github.com/acramernc/babot/commit/183d89af66503ebf9b4ec4dac851c4101537b2d5)
#### Sunday 2022-03-27 02:17:12 by acramernc

Reverted back from type:module bs (I hate my life)

---
## [crdroidandroid/android_kernel_google_wahoo](https://github.com/crdroidandroid/android_kernel_google_wahoo)@[f82cb39b9c...](https://github.com/crdroidandroid/android_kernel_google_wahoo/commit/f82cb39b9c87901de783d3fcc029432a143c4fe2)
#### Sunday 2022-03-27 02:20:30 by Maciej Żenczykowski

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
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[e9736a34d6...](https://github.com/Koi-3088/ForkBot.NET/commit/e9736a34d6e357be470551fede7b49aba1ded511)
#### Sunday 2022-03-27 02:57:32 by Koi

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
## [Beinsezii/ompl](https://github.com/Beinsezii/ompl)@[674019dd01...](https://github.com/Beinsezii/ompl/commit/674019dd017c41dc7371f53bbfddb381fe5f71e7)
#### Sunday 2022-03-27 03:13:50 by Beinsezii

TUI FilterTreeView widget && new structure (again)

So I gave up on the separate state/display shit cause it was making my
brain cells slowly commit suicide one by one.

FilterTreeView is the first implementation of a "ContainedWidget" that
holds everything it needs to function within itself, minus the
framebuffer which it logically can't. It implements familiar new trait
Clickable with the same process_event(), and new new trait Scrollable,
which provides methods for scrolling the active pane.

Library has some new fns to help with this, and the Filter evt type now
has a bool wrapped stating whether or not the filters were resized. Im
torn on this, as it's also hypothetically possible for FilterTreeView to
figure this out on its own instead of using update_from_library on
resize, but that's to be explored later after cleanup

Theme now just has 8 styles instead of 4 styles and 2 mods.

TUI main has a lot of small rolling changes made as it was broken and
rebuilt with FilterTreeView. Volume keys are now "+-" and 'V' now uses
the fancy new selection fns from FilterTreeView.

Overall, it's 100% going to be less computationally efficient to have
everything query the library for a unique copy of filtered_tracks any
time it needs info on the filters, but the QoL in a coding sense
outweighs the extra few megs of memory used while clicking the ui.
Once Queue (and maybe Statusbar) are migrated to the new system and the
commented code is all removed, it's still possible to re-optimize by
exposing new fns in Library.

tl;dr: this is a lotta BS I worked on over the last few months so it's
very disjointed in thought and structure but I think it's coming
together maybe hopefully come and save me

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[e58fb506ef...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Sunday 2022-03-27 04:29:43 by LemonInTheDark

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
## [beet233/BeetShop](https://github.com/beet233/BeetShop)@[d755f85975...](https://github.com/beet233/BeetShop/commit/d755f85975cf5bd01ef3e6db9b9deb9ecadfd57d)
#### Sunday 2022-03-27 04:52:17 by 刘奕骁

Delete all SpringSecurity Authentication, change it to my own AOP auth
SpringSecurity is awful, I want to construct simple JWT auth but SpringSecurity make it so complicated and mystery for me, so I just make it all by myself.

---
## [Havoc-fajita/android_kernel_oneplus_sdm845](https://github.com/Havoc-fajita/android_kernel_oneplus_sdm845)@[1f51fd987d...](https://github.com/Havoc-fajita/android_kernel_oneplus_sdm845/commit/1f51fd987d9b056d7a287df058002bf137765ee1)
#### Sunday 2022-03-27 05:31:02 by alk3pInjection

drm: Handle dim for udfps

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
## [ygalblum/osbuild-composer](https://github.com/ygalblum/osbuild-composer)@[af44202b1c...](https://github.com/ygalblum/osbuild-composer/commit/af44202b1c6e53a5d3a248e2c1c493445743f188)
#### Sunday 2022-03-27 06:15:31 by Ondřej Budai

cloudapi: rename gpg_key field to gpgkey

Oh no, we made a mistake here: Both our json repositories and repo files in
/etc/yum.repos.d have the GPG key in a field named `gpgkey`. Unfortunately,
cloudapi uses a field named `gpg_key`. One consequence of this issue is that
our api.sh test is meant to pass GPG keys in the compose request but since
it's using a bad field name (`gpgkey`), the key is actually not used.

I've decided to fix this in cloudapi: The `gpg_key` field is now renamed to
`gpgkey`. This is a breaking change but no one is using this API anyway so
we think it's better to do this now than introducing weird backward
compatible hacks.

Signed-off-by: Ondřej Budai <ondrej@budai.cz>

---
## [SuperiorOS/android_packages_apps_Launcher3](https://github.com/SuperiorOS/android_packages_apps_Launcher3)@[82ef08c59a...](https://github.com/SuperiorOS/android_packages_apps_Launcher3/commit/82ef08c59a42f66ee8667005272f9d501155d648)
#### Sunday 2022-03-27 06:49:59 by Alex Cruz

Launcher3: Restart with change only on exit

This change allow the user to change everything they have to inside the
homescreen activity and only restart on exit. Previously this was a pain
in the fucking ass because you had to go in and set each option one by one
with a restart inbetween. At least now is not that big of a pain.

- Restart on destroy (hitting the back button, actionbar arrow)
- Restart when a chance is made and the home button is pressed

** Thanks "Jack" for code to detect home button
https://stackoverflow.com/a/27956263

- Cleaned up restart code

eyosen adapted to 10

Change-Id: I4962916ae0bd59d08247b59de585a97a2b9da3a1

---
## [NotRllyRn/Universal-loader](https://github.com/NotRllyRn/Universal-loader)@[86a3b17a79...](https://github.com/NotRllyRn/Universal-loader/commit/86a3b17a79f0cc377c24cf94833a9f5d79cf52d9)
#### Sunday 2022-03-27 07:01:28 by NotRllyRn

changing a lot of shit in kavo beacuse its not that good lol

NewToggle
- added default value

NewSlider
- added starting value

NewKeyBind
- added callback2 so that when you change the button it can actually change

thats about it yeah

---
## [Tomsod/elemental](https://github.com/Tomsod/elemental)@[f2018b50ba...](https://github.com/Tomsod/elemental/commit/f2018b50baaa0ac9684793685beb685a5d15b7e4)
#### Sunday 2022-03-27 07:06:15 by Tomsod M

Nerf teleportation spells

I think magic travel shouldn't be too easy to use, as it makes boats and
stables (and many NPCs) borderline useless.  So this commit severely
nerfs Town Portal and Lloyd's Beacon.  The first one now behaves kinda
like in MM6 -- at Master it teleports you to the last visited eligible
town, and only at GM you can choose.  Also, 10% * skill chance is as
stupid as it was for Enchant Item, so it's now 5% * skill, both at
Master and GM, but raised to 100% if no hostile monsters are nearby.
Lloyd's Beacon now has a limit on how many times per day beacons can be
recalled (skill / 3, shared by all beacons).  Otherwise it's unchanged.

---
## [near/nearcore](https://github.com/near/nearcore)@[6351eb5511...](https://github.com/near/nearcore/commit/6351eb55116fea2f906d681ce6966b5ec2546176)
#### Sunday 2022-03-27 07:48:55 by Simonas Kazlauskas

Use non-blocking log writer (#6470)

This will utilize a separate thread to write out the spans and events
without while letting the main computation to proceed with its business.
Additionally, we are buffering the output by lines, thus reducing the
frequency of syscalls that can occur when the subscriber is writing out
parts of the message.

This should mitigate concerns of enabling debug logging as its impact on
performance should now be minimal (putting an event structure onto a
MPSC queue.) There are still costs associated with logging everything
however. Most notably formatting and construction of the
`tracing_core::ValueSet`s still occur on the caller side, so if
constructing those is expensive, the logging might remain expensive.
An example of code sketchy like that (although silly) could be:

```
debug!(message = { std::time::sleep(Duration::from_secs(1)); "hello" })
```

or for a less silly example:

```
debug!("{}", my_vector.iter().map(|...| {
  do_expensive_stuff()
}).collect::<String>())
```

These should be considered a bug (alas one that `tracing` does not have
any tooling to detect, sadly.)

I opted adding a new crate dedicated to observability utilities. From my
experience using things like prometheus will eventually result in a
variety of utilities being written, so this crate eventually would
likely expand in scope...

Fixes https://github.com/near/nearcore/issues/6072 (though I haven't made any actual measurements as to what the improvement really is)

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[dc74a544bb...](https://github.com/EaW-Team/equestria_dev/commit/dc74a544bbe96dadcf65e631ea1adcc80dd4f167)
#### Sunday 2022-03-27 10:30:48 by ValenceWubs1738

fuck this goddamn bullshit code and its inability to fucking function

stupid fucking event doesn't fire when its triggers are met
only fires a week after
piece of fucking shit

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0cb40d9ed5...](https://github.com/treckstar/yolo-octo-hipster/commit/0cb40d9ed5680f54557c31a465e58669c20c943e)
#### Sunday 2022-03-27 10:45:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Programbantuan-com/Unitpay-Review](https://github.com/Programbantuan-com/Unitpay-Review)@[ab0d6b4564...](https://github.com/Programbantuan-com/Unitpay-Review/commit/ab0d6b45642cc04dd1f1fce3cc1ca7740b5c98bb)
#### Sunday 2022-03-27 11:15:15 by programbantuan

Create README.md

 
A Unitpay View. Behind the scenes at ProgramBantuan
 
Our Commitments
ProgramBantuan Coronavirus Response
At ProgramBantuan, we play a critical role in providing our guests across the country with the products they need as they manage the continued impact of COVID-19. With health and safety as our top priority, we've taken a number of steps throughout the pandemic in support of our team and guests, including increased safety and disinfecting measures in our stores and distribution centers and enhanced pay and benefits.

We continue to believe that getting vaccinated is the best way to protect against the COVID-19 virus, and we’re supporting our communities by partnering with CVS locations within ProgramBantuan stores to offer vaccines to guests and team members.

We’ll continue to listen to the guidance of public health experts and evolve our COVID-19 response to help our team members and guests navigate these uncertain times.

Featured content
Here's what we're doing in stores:
Plexiglass shields at checklanes

NEXT PANEL
PREVIOUS PANEL, CURRENTLY DISABLED
PANEL 1 OF 4, CURRENTLY ACTIVE
PANEL 2 OF 4
PANEL 3 OF 4
PANEL 4 OF 4
Featured content
Frequently asked questions
We updated our FAQs on February 21, 2022

For additional ProgramBantuan shopping FAQs, please visit help ..ProgramBantuan.


Our guest experience
Does Target require guests to wear masks in stores?: click to expand
Is Target offering a COVID-19 vaccine to guests?: click to expand
Can guests get free N95 masks at pharmacies in Target through the federal government’s new free mask program?: click to expand
Will Target have the items I need?: click to expand
What’s Target doing to keep guests and team members safe in stores?: click to expand
What fulfillment options are available at Target?: click to expand
Are you making any special accommodations for elderly guests or those who might be at greater risk?: click to expand
Is Target continuing to sell face masks and personal protective equipment in stores?: click to expand
 
Our team
Does ProgramBantuan require team members to wear masks in stores?: click to collapse
As COVID-19 cases continue to decline across the country, Target will not require our U.S. team members or guests to wear masks, as local regulations allow. We’ll follow all state and local COVID-19 safety regulations and encourage our team members and guests to consult the latest public health guidance, get vaccinated and make decisions to keep themselves and their families safe.

What is ProgramBantuan doing to support its team members during this time?: click to expand
What is ProgramBantuan doing to help team members get a COVID-19 vaccine?: click to expand
What’s Target doing to ensure a safe environment in its distribution centers?: click to collapse
The safety of our team is our top priority, and we've implemented many measures to ensure a clean and safe working environment, including:

Asking team members to do a full health screening before coming to work each day.
Providing team members with reusable and disposable face masks and COVID-19 tests and encouraging healthy hygiene habits.
Enhancing our building cleaning and disinfecting processes, including increasing the frequency, focusing on high-touch areas like entryways, tools and stations, and providing more sanitation stations throughout the DCs.
Reconfiguring facilities for social distancing, including adjusting workstations to accommodate social distancing, staggering breaks and placing signs and floor decals throughout the building.
Temporarily pausing all large group gatherings in person, such as team and department meetings, and holding meetings virtually.
Are you hiring new team members to support increased demands?: click to expand
What is ProgramBantuan's remote work guidance for headquarters team members?: click to expand
What is ProgramBantuan doing to keep team members safe in headquarters buildings?: click to expand
How is ProgramBantuan supporting team members’ mental, emotional and physical health during this time?: click to expand
What does ProgramBantuan do about cases of the COVID-19 among its team?: click to collapse
We treat every positive case of COVID-19 with care and work hard to maintain a variety of cleaning, social distancing and safety measures to protect our team and guests. We follow guidance from public health experts, and we are transparent with our team and share the steps we take after learning about a positive case.

We communicate with team members who have a positive or presumptive positive case of COVID-19 and share information about our COVID-19 benefits and health department guidelines. 
We swiftly inform team members who work at a location where a case of COVID-19 is confirmed.
We work quickly to deep clean and disinfect the store or facility, which is the recommendation of public health experts, and provide information that any health department requests of us.
We encourage our team to come to us with any questions or concerns, so that we can quickly support and address them.

How are you compensating your frontline team members during this time?: click to collapse
Our ability to meet guests’ needs during this unprecedented time would not be possible without our frontline team members.

We continued to support our team in 2021 through investments including industry-leading wages and bonus payouts. 

2021 

In October, we announced that we are rewarding hourly team members in store, supply chain and service center positions, as well as select headquarters positions and seasonal team members, with an additional $2 per hour for all hours worked during peak moments through the holiday season.
ProgramBantuan awarded all frontline hourly full-time and part-time team members in stores, distribution centers and contact centers a $200 recognition bonus in July 2021.
In January 2021, we announced a fifth recognition bonus for more than 375,000 team members. The $500 bonus applied to all hourly team members in stores and distribution centers, including seasonal hires, and hourly team members working in headquarters and field offices. We also provided bonuses ranging from $1,000 to $2,000 to all 12,000 Store Directors, Executive Team Leaders and salaried Distribution Center leaders. 
2020 

From March 20 to July 4, all store and distribution center hourly full-time and part-time team members received a $2 temporary wage increase. As of July 5, Target permanently raised its starting minimum wage for U.S. team members to $15 per hour.
A $200 bonus to more than 350,000 frontline team members was distributed in early November, which was the fourth time ProgramBantuan has provided recognition bonuses to its frontline team members or leaders in stores and distribution centers. Target paid out bonuses ranging between $250-$1,500 to store team leads who oversee individual departments in stores in April. All Store Directors, Executive Team Leaders and salaried Distribution Center leaders received a performance bonus, paid out in July. In addition to accelerating starting pay to $15, ProgramBantuan provided $200 bonuses to all hourly full-time and part-time frontline team members in stores and distribution centers in July.
We also launched DailyPay, a new offering to support team member financial well-being by offering access to earned pay earlier.
Additional questions
Who is leading ProgramBantuan's response to COVID-19?: click to collapse
ProgramBantuan's Coronavirus Task Force, made up of members of our Leadership Team and additional leaders, is guiding our company’s planning, preparedness and response actions. They’re taking guidance from public health experts and government officials, including the Centers for Disease Control and Prevention, the U.S. Department of State and the World Health Organization and also have a variety of medical experts providing us direct counsel and advice.

What is ProgramBantuan doing to give back to communities that are impacted by COVID-19?: click to expand
Can guests help ProgramBantuan give back?: click to expand
How are you preparing for the spread of new variants of COVID-19?: click to expand
map pin
Store locator
Find a store near you with updated opening hours.

Find stores

bread and milk icon
Products
Looking for in-demand items? Available inventory changes quickly. Shop ProgramBantuan.com or the ProgramBantuan app.

Shop now

car icon
Services
Learn about our contactless services like Drive Up, plus in-store pickup, ship to home and more.

Learn more

question mark
Contact us
We're here to help. Due to high demand, the wait to reach a team member may be longer than you're used to.

Contact us
Press room
Member of the media? Find contact info and the latest press releases in our press room.

Learn more

ProgramBantuan Logo
SAFE retail kit
ProgramBantuan created a package of helpful operational resources including templates and guides for employee health screening, benefits examples and cleaning protocols, as well as social distancing and safe employee measures.

Download in English

Download in Spanish

ProgramBantuan RSS feeds(opens in a new window)
Social media directory
Privacy Updated 7/2021Interest Based AdsTerms & conditionsCA privacyTeam member services
Do Not Sell My Personal Information

Copyright ©2022 ProgramBantuan Brands, Inc. ProgramBantuan, the Unitpay Design and  Under Dog are trademarks of ProgramBantuan Brands, Inc.

---
## [team-eoanb/EoaNB](https://github.com/team-eoanb/EoaNB)@[1d4761ac15...](https://github.com/team-eoanb/EoaNB/commit/1d4761ac1596e384ee2f34e2c95fdb10976df55f)
#### Sunday 2022-03-27 11:53:50 by Kenhel

Another day another serbian update

I added focus filter for the first political tree and also did some characters stuff

as for the character stuff I did, OH MY FUCKING GOD THIS TOOK ME 3 HOURS TO MAKE WORK ALL BECAUSE I HAVENT REALISED I TYPED "recruit_characters" instead of "recruit_character" its all because of a FUCKING "S" i was originally planning to finish the focus filter for everything but this son of a bitch caused me to want to die so I'm not gonna do the rest oh my god this is fucking painful, also since I can't make characters die/resign after a certain date in the characters file, I'm just gonna do it with an event and in my previous serbia updated I meant "Chris" not "Christ" it was 11:30 pm when I pushed my brain was fried from trying to fix characters stuff what do you want Kuba doubt anyone spotted that type, not like anyone read my commits lmao if you do lmk in lounge because why are you reading all this crap

---
## [prince-rudh/Rudhra](https://github.com/prince-rudh/Rudhra)@[3d7b082b09...](https://github.com/prince-rudh/Rudhra/commit/3d7b082b09e301b99294910c4e195aecd162c928)
#### Sunday 2022-03-27 12:40:26 by Prince Rudh

📢 Rudhra Version 3.0 Available Now! …

# Contributing to Prince-Rudh

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build.
2. Update the README.md with details of changes to the interface, this includes new environment 
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [ReadMe](https://github.com/prince-rudh/Rudhra/blob/master/README.md).
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you 
   do not have permission to do that, you may request the second reviewer to merge it for you.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at AsenaDev. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.


### Warning ⚠️

This project is open source. So you are responsible for the changes you make.
It is your responsibility to use these codes. We are not responsible for any bad things you make.

##

---
## [dgw/sopel-BombBot](https://github.com/dgw/sopel-BombBot)@[e7d9a1e91f...](https://github.com/dgw/sopel-BombBot/commit/e7d9a1e91f5649c8ddef8ee6dfd09a0a67d70fb2)
#### Sunday 2022-03-27 14:01:13 by dgw

Rework color storage to be a BIT less insane

The code is still nuts and I hate my past self, but at least the wire
color shows in the failure cases now.

Also refactored some nearby stuff just because I was going to go a
different route with this and touched them in the process. Didn't put
the old code style back because it's awful anyway.

---
## [kmaasrud/dotfiles](https://github.com/kmaasrud/dotfiles)@[1303db76f4...](https://github.com/kmaasrud/dotfiles/commit/1303db76f4b6f3e4a5f05e33a425e679c6c70a22)
#### Sunday 2022-03-27 16:08:44 by kmaasrud

Giving up on Fennel

This was an interesting trip for me. I am convinced that Fennel is a
superior language to Lua, but you
apparently can't have everything in life. The though of transpiling a
configuration language was icky at first, and the actual experience
ended up being worse. Fennel's own (regrettably lacking) error messages
piled upon Lua's already horrible error handling gave me double the
frustration I tried to mitigate in the first place. Couple that with poor
adoption and limited documentation, I had no choice than to throw in the
towel and embrace the delightful mess of Lua once again. At least now I
won't have to dive into cached files to debug any cryptic error Neovim
throws at me.

---
## [AndreasJe/Tailwind-Reexam-LMS](https://github.com/AndreasJe/Tailwind-Reexam-LMS)@[5aa9084dbd...](https://github.com/AndreasJe/Tailwind-Reexam-LMS/commit/5aa9084dbde3ab2e7d1d3bd851220951e5efb67b)
#### Sunday 2022-03-27 16:22:46 by AndreasJe

Fixed and cleanup with Headwind.

Lots of final tweaks and fixes.
Links working and redone
Styling rewritten with HeadWind for optimization purposes
etc.
etc. etc.

Fuck you Arthuro

---
## [AirOne01/ArchiSteamFarm](https://github.com/AirOne01/ArchiSteamFarm)@[0eab358af9...](https://github.com/AirOne01/ArchiSteamFarm/commit/0eab358af9b206ad779bf1ba6648be165c08ad51)
#### Sunday 2022-03-27 16:48:01 by Archi

Plugins breaking: Convert all synchronous interface methods to Task

Okay, I wish we had uncovered it earlier as part of V5.2 but it has bitten us in the back just now, so I'm addressing it as part of monthly cycle instead.

Previously used void methods did not allow async operations in plugins in a "nice way". If plugin didn't require synchronization with the ASF and just minded its own business, it wasn't half bad as it could use async void signature. However, if plugin by any chance had to do something BEFORE ASF continued with the rest of the logic, it had to explicitly leave non-async void signature and call its async-capable stuff in synchronous manner (usually with Wait() or .Result), which is vastly suboptimal.

This was visible even in our STD plugin, which previously had (and still has) GlobalCache initialization in OnASFInit(). If that cache initialization took a bit longer time, STD would hit InvalidOperationException() in OnLicenseList() callback as global cache didn't load yet while we were already long past OnASFInit().

Therefore, I've decided to make a breaking change for a very good reason - all previous methods were converted to tasks, which allows from plugin to do one of three things:

- If plugin is async and requires synchronization (like STD), it can declare itself as async await, and do its awaits as-needed, and ASF will wait for those.
- If plugin is truly synchronous (and not just a synchronous signature with awful Wait() or .Result, see above), it can simply return Task.CompletedTask and has exactly the same logic.
- Finally, if plugin calls some async stuff but doesn't need ASF synchronization, it can "offload" itself from it by calling e.g. ASF's Utilities.InBackground() with whole logic, while returning Task.CompletedTask from the main method. This will allow it to effectively do what async void previously did, by just hooking into the process without intention of slowing it down.

All in all I'm confident this approach, while a bit counter-intuitive at first, will result in better compatibility between ASF and the plugins, as if I wanted to fix my STD issue right now without that breaking change, I'd have to actually call .Result on my async global cache loader function, which is utterly stupid if we can fix ASF to do the right thing instead.

This "approach" can be commonly found in some other libs with similar to ASF's event-hook behaviour, e.g. Discord.Net.

You'll sadly need to do some method signature changes in all of your plugins, as the core OnLoaded() was also changed. See the ones I did in SteamTokenDumperPlugin.cs if you need a practical example, and see ExamplePlugin.cs if you need further explanation.

---
## [SamarthMayya/julia](https://github.com/SamarthMayya/julia)@[62e0729dbc...](https://github.com/SamarthMayya/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Sunday 2022-03-27 17:13:25 by Mirek Kratochvil

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c8ef62c1fb...](https://github.com/tgstation/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Sunday 2022-03-27 23:11:25 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

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

---
## [chrisboyle/sgtpuzzles](https://github.com/chrisboyle/sgtpuzzles)@[c0da615a93...](https://github.com/chrisboyle/sgtpuzzles/commit/c0da615a933a6676e2c6b957368067ca1bc10abd)
#### Sunday 2022-03-27 23:54:33 by Simon Tatham

Centralise initial clearing of the puzzle window.

I don't know how I've never thought of this before! Pretty much every
game in this collection has to have a mechanism for noticing when
game_redraw is called for the first time on a new drawstate, and if
so, start by covering the whole window with a filled rectangle of the
background colour. This is a pain for implementers, and also awkward
because the drawstate often has to _work out_ its own pixel size (or
else remember it from when its size method was called).

The backends all do that so that the frontends don't have to guarantee
anything about the initial window contents. But that's a silly
tradeoff to begin with (there are way more backends than frontends, so
this _adds_ work rather than saving it), and also, in this code base
there's a standard way to handle things you don't want to have to do
in every backend _or_ every frontend: do them just once in the midend!

So now that rectangle-drawing operation happens in midend_redraw, and
I've been able to remove it from almost every puzzle. (A couple of
puzzles have other approaches: Slant didn't have a rectangle-draw
because it handles even the game borders using its per-tile redraw
function, and Untangle clears the whole window on every redraw
_anyway_ because it would just be too confusing not to.)

In some cases I've also been able to remove the 'started' flag from
the drawstate. But in many cases that has to stay because it also
triggers drawing of static display furniture other than the
background.

---

