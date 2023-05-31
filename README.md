## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-30](docs/good-messages/2023/2023-05-30.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,020,752 were push events containing 3,264,139 commit messages that amount to 249,121,934 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 67 messages:


## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[79e07c00db...](https://github.com/Monkestation/Monkestation2.0/commit/79e07c00db8607513347f8e7e6f2a8520e563680)
#### Tuesday 2023-05-30 00:37:21 by Aeri

fucking wacky ass goddamn cargo order console locations fixed

---
## [tonyvitonis/git](https://github.com/tonyvitonis/git)@[eb1c42da8e...](https://github.com/tonyvitonis/git/commit/eb1c42da8e21cc2a8dacd21023a179b788858887)
#### Tuesday 2023-05-30 01:15:27 by Jeff King

t/lib-httpd: make CGIPassAuth support conditional

Commit 988aad99b4 (t5563: add tests for basic and anoymous HTTP access,
2023-02-27) added tests that require Apache to support the CGIPassAuth
directive, which was added in Apache 2.4.13. This is fairly old (~8
years), but recent enough that we still encounter it in the wild (e.g.,
RHEL/CentOS 7, which is not EOL until June 2024).

We can live with skipping the new tests on such a platform. But
unfortunately, since the directive is used unconditionally in our
apache.conf, it means the web server fails to start entirely, and we
cannot run other HTTP tests at all (e.g., the basic ones in t5551).

We can fix that by making the config conditional, and only triggering it
for t5563. That solves the problem for t5551 (which then ignores the
directive entirely). For t5563, we'd see apache complain in start_httpd;
with the default setting of GIT_TEST_HTTPD, we'd then skip the whole
script.

But that leaves one small problem: people may set GIT_TEST_HTTPD=1
explicitly, which instructs the tests to fail (rather than skip) when we
can't start the webserver (to avoid accidentally missing some tests).

This could be worked around by having the user manually set
GIT_SKIP_TESTS on a platform with an older Apache. But we can be a bit
friendlier by doing the version check ourselves and setting an
appropriate prereq. We'll use the (lack of) prereq to then skip the rest
of t5563. In theory we could use the prereq to skip individual tests, but
in practice this whole script depends on it.

Reported-by: Todd Zullinger <tmz@pobox.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[303cfa3bbb...](https://github.com/Hatterhat/tgstation/commit/303cfa3bbb2199b24df17e87864d92e038a32dca)
#### Tuesday 2023-05-30 01:21:37 by GoldenAlpharex

Fixes is_station_level() sometimes behaving erratically if the value provided is more complex than just a variable (#75489)

## About The Pull Request
I have been debugging this stupid macro for the past nearly five hours,
to finally figure out why it was breaking. If you had something like `a
|| 0` in what you called the macro with, it would somehow manage to
break the cache. This makes it far more foolproof, and will ensure that
it doesn't break here anymore, because debugging this has to be one of
the biggest pains in my ass I've ever had.

## Why It's Good For The Game
So shit like this

![image](https://github.com/tgstation/tgstation/assets/58045821/455122b0-34eb-4ec0-92dd-2775c1f0f878)

Doesn't end up breaking your CI (or even worse, the game in prod), in
places unrelated. At least now it shouldn't be overwriting values in the
cache.

It shouldn't have to do verification that you're doing the right thing,
that should be left on the person using the macro because it was meant
to be faster than a proc call, adding too much verification overhead
kind of just loses some of that speed.

## Changelog

:cl: GoldenAlpharex
fix: Makes checks for the station z level more robust against coders
doing less intuitive stuff, thus protecting it from breaking in weirdly
difficult and seemingly unrelated places (I'm looking at you, nuke
cinematic unit test).
/:cl:

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[bc22fefe3b...](https://github.com/Hatterhat/tgstation/commit/bc22fefe3b1de4d882dd87a5492344672230736d)
#### Tuesday 2023-05-30 01:21:37 by Helg2

Adds proper armor for security plasmamen. (#75156)

## About The Pull Request
It's kinda strange that security plasmamen has no proper armor and you
can just bully them with bottlesmashes. Literally.
Also suits had no wound armor for some reason, which considering that
mold dies without hand kinda silly too.
And helmets just had no armor besides 1 melee armor.
## Why It's Good For The Game
Plasmamen security won't die that easilly. I mean, still easy to kill
them, but not that much.
## Changelog
:cl:
balance: Security Plasmamen now have Security armor. No bullying them
with bottlesmashes anymore.
/:cl:

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[8fa6242c66...](https://github.com/GuillaumePrata/tgstation/commit/8fa6242c66205866b702440f490eeae34ef6b85f)
#### Tuesday 2023-05-30 01:40:31 by Bloop

Refactors High Luminosity Eyes, fixes a ton of bugs related to it as well as qol improvements (#75040)

## About The Pull Request

The high luminosity eyes item was extremely out of date, broken, and
full of copy paste code from atom lighting. Which is a shame because
they were cool.

On top of all that it was using a special light effect that was not very
performant. I got rid of all that, hooked it into atom lighting as a new
light type, and gave it a new TGUI as well because the old ui prompts
were not great either.

You can now pick a color at random if you want. You can also set the
color and range before surgically implanting them. No more being forced
to go through the color picker when you just want to change the range.

Functionally they should pretty much should be the same as before with
some bonus features (see below).


![dreamseeker_nDeLNyOOG2](https://user-images.githubusercontent.com/13398309/235325530-105fe82e-ecc8-4dc4-9c84-143cc6519688.gif)

Closes https://github.com/tgstation/tgstation/issues/61041
Closes https://github.com/Skyrat-SS13/Skyrat-tg/issues/14685

This is 100% completed. I just finished fixing the slight translation
bug when going from 0->1 range (see above gif) and that was the last
thing on my bucket list. I happy enough with this at this point in time.

---

EDIT: 

I have decided to add in one last new feature, and that is...
independent settings for eye color.

<details> <summary>You can now set eye color independently if you
wish</summary>


![dreamseeker_j32B2S4yXQ](https://user-images.githubusercontent.com/13398309/235412568-ffa8e424-8624-4462-9f6f-77c1513aa773.gif)

</details>

The eye color does not modify the light color in any way when set in
this manner, but it can be used for cosmetic purposes.

Kind of makes the item more like cybereyes from cyberpunk, which I think
are pretty neat!

</details>

### What I've done, in more detail:

- refactored high luminosity eyes so they use the atom lighting system
instead of the way they were doing it before
- the new light type, `MOVABLE_LIGHT_BEAM` behaves similarly to
directional lights, with some slight differences. it reuses the same
lighting overlay sprites but scales them vertically to produce a more
focused effect. The result can be seen above. This is in contrast to the
old way, which spawned `range` number of individual 32x32 overlays and
moved them around. This way should perform better as well as be more
maintainable.
- added a new TGUI interface for high luminosity eyes with buttons for
range, a text field for a color hex, a color picker and randomizer
- made the eye overlay emissive when the light is turned on
- range goes from 0 to 5. at range 0, the light overlay is turned off
and you are left with just the emissive eyes.
- added a cosmetic functionality to this item that lets you change the
color of your eyes independently of the lighting (and each other)
- fixed a bug with directional flashlights sometimes not updating their
lighting overlay if you pick them up without changing your direction
---

### Other Misc Fixes

Being able to dynamically set range back and forth exposed some logic
issues that had existed with directional light overlays and I have fixed
those. That is why there are some edits in that file that may not appear
readily obvious why they are there.

Apart from that, two other bugs that come to mind:
1) eye code was supposed to keep track of the eye color you had before
you got new eyes, but it was overwriting that every time you ran
refresh().
2) lighting was supposed to be turning off the light when range is set
to 0, but it was not doing that properly.

And of course besides that, there may have been a few instances of
finding typos/tidying up code

## Why It's Good For The Game

The code for this was like 6 years old and in desperate need of
updating. Now it works, and has a nicer UI.

## Changelog

:cl:
fix: high luminosity eyes light overlays now follow the user correctly
qol: high luminosity eyes now have a tgui menu so you no longer have to
go through the color picker every time you want to change the range.
they also have a new setting that lets you change the color of your eyes
independently of the light color. You can now have cybernetic
heterochromia if you want
fix: directional flashlights when picked up will now always update their
cast light direction correctly no matter what dir you are facing
refactor: refactors high luminosity eye code to better make use of the
atom lighting system, adding a new light type 'MOVABLE_LIGHT_BEAM'
/:cl:

---
## [funman816/tgstation](https://github.com/funman816/tgstation)@[40e98a7ba4...](https://github.com/funman816/tgstation/commit/40e98a7ba450d51787f7a14af63827fc7059ffd6)
#### Tuesday 2023-05-30 01:41:08 by John Willard

Mafia rebalance and backend refactor (#74640)

## About The Pull Request

Turns all Mafia abilities into datums, instead of being a bunch of
shitcode on every single job.
This means it's easier to add new roles
Gives new names to some defines (such as the signal order, to make it
easier to tell when something is fired)
Adds support for modular Mafia jobs with their abilities being in a
certain order (Escort is now properly first).
De-snowflakes Changeling killing abilities and day voting, they're now
actions that are tallied when necessary.

Turns time vars into defines
Generalizes a lot of behavior for abilities, now all abilities can
properly undo their action at night

Fixes problems with the UI (Thoughtfeeder had 2 buttons during night and
they overlapped with names, that's been fixed).

### Behavior changes

- Doctor/Officer can now protect themselves 1 night, because it gives
them a way to protect themselves.
- Lawyer/Warden/Ect now choose their abilities at night, rather than the
day before. The suspense building up towards the end of the night is
part of the game, telling you that it happened at the very start is
quite lame (in the case of Lawyer, anyway).
- Admin setup now uses TGUI instead of html inputs.
- Cut night time by like, 5 seconds, because I found it a little long
lol.
- HoP doesn't count as votes to win until they reveal, because it makes
no sense an unrevealed HoP has their unrevealed votes tallied. I also
like those 1v1 Mayor V. Evil scenarios where dead chat goes crazy, and
hope to replicate that here.
- Mafia now needs 6 people to start instead of 4, because 4 players is
just not enough to play a Mafia round that will do anything but annoy
people.
- The game no longer ends if it's in a standoff with 1 Town, 1 Mafia,
and 1 Neutral, as you've got a kingmaker and they should decide who
wins.

### Things I want to change in the future
Every time night starts/ends, it checks the entire ``GLOB.airlocks`` for
doors with the "mafia" ID. This is stupid.
Rework ``check_victory()`` to make it make more sense, and be more fun
for players.
A visible death animation?
I want to use something similar to admin popup for messages about people
being on stand, and decluttering the UI in general
Also more use of balloon alerts instead of to chat messages for
everything.
Also also, making the UI more responsive to players. Button should be
red when a player is selected, so they know that's who they've selected,
if they want to unselect.
Are votes public when you first cast them? They shouldn't be wtf.
Can we also make the description for roles not be a to chat message? It
can just say when you hover over the '?' come on.
User-written wills instead of auto-generated, and able to send them in
chat
Add support for roleblock-immune roles

## Why It's Good For The Game

Updates a lot of old code to modern standards
Makes it considerably easier to work with Mafia and add new roles
Makes things less prone to breaking as easily.
Code also looks a lot cleaner now.

## Changelog

:cl:
refactor: [Mafia] All Mafia abilities have been overhauled in the
backend, it's now much easier to understand what each role's ability can
do and how it works.
admin: [Mafia] Admin setup of Mafia is now in TGUI
balance: [Mafia] Doctors/Officers can protect themselves once per game.
Be careful around them!
fix: [Mafia] Thoughtfeeder's UI buttons at night won't overlap with
eachother.
fix: [Mafia] HoP's votes now actually matter, instead of being purely
visual.
qol: [Mafia] Lawyers, Wardens, etc. now perform their night ability at
night, instead of the day prior.
qol: [Mafia] Night time now lasts 40 seconds instead of 45.
/:cl:

---
## [funman816/tgstation](https://github.com/funman816/tgstation)@[2b2cb3dff6...](https://github.com/funman816/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Tuesday 2023-05-30 01:41:08 by LemonInTheDark

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
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[912e843f53...](https://github.com/nikothedude/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Tuesday 2023-05-30 01:43:00 by san7890

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
## [knative-automation/client-pkg](https://github.com/knative-automation/client-pkg)@[964c3afe21...](https://github.com/knative-automation/client-pkg/commit/964c3afe219cd6ddcdebfc0cff65d3d536a8359a)
#### Tuesday 2023-05-30 01:48:57 by Knative Automation

upgrade to latest dependencies

bumping golang.org/x/tools b3b5c13...d0863f0:%0A  > d0863f0 go.mod: update golang.org/x dependencies%0A  > 545ca87 gopls/internal/regtest/marker: require go/packages%0A  > 1ace7db go,gopls: remove license from package doc comments%0A  > ebad375 gopls/internal/lsp/protocol: prevent license rendering in godoc%0A  > 10a39ef gopls/internal/lsp/regtest: address additional comments on marker.go%0A  > 69920f2 gopls/internal/regtest/marker: add missing tests for hover%0A  > 24a13c6 gopls/internal/regtest: fill out features of the new marker tests%0A  > 2b149ce gopls/internal/regtest: add a regtest-based version of the marker tests%0A  > edddc5f go/packages: don't discard errors loading export data%0A  > a762c82 go/ssa: add MultiConvert instruction%0A  > f124b50 cmd/stringer: streamline test subprocesses%0A  > 6b6857a gopls: fix typos in comments and doc%0A  > 8111118 go/analysis/internal/facts: fix cycle in importMap.%0A  > dd1c468 gopls/internal/lsp/source: simplify extracting object hover doc%0A  > 66f8f71 gopls/internal/lsp/source: use syntax alone in FormatVarType%0A  > 30f191f internal/imports: update stdlib index for Go 1.20%0A  > 4e98188 internal/imports: use go/packages instead of cmd/api to compute symbols%0A  > 4e8ff89 internal/imports: update stdlib index for 1.20%0A  > 6bd0d00 gopls/internal/lsp: go to definition from linkname directive%0A  > 0cfddb3 gopls/internal/lsp: enable clear builtin completion test%0A  > 41adf8d gopls/internal/lsp/tests: remove StripSubscripts%0A  > 86fdadc gopls/internal/lsp/safetoken: delete safetoken.Range%0A  > c276ee5 internal/robustio: fix signature of getFileID on plan9%0A  > e170d45 gopls/internal/lsp: add clear builtin%0A  > 2ea4b81 go/ast/inspector: skip ranges that do not contain a node type%0A  > 407bbed go/analysis: improve error message on duplicate fixes%0A  > bd5dfbb all: fix some comments%0A  > 072fca5 gopls/protocol: use the current definition of the lsp%0A  > aa633e7 tools/gopls: provide markdown for completion and signature help%0A  > 684a1c0 go/analysis/internal/analysisflags: use os.Executable for program path%0A  > bd5e595 gopls/internal/lsp/cache: add missing mutex%0A  > 2683128 gopls/internal/lsp: differentiate govulncheck/vulncheck imports diags%0A  > d1e92d6 gopls/internal/lsp/mod: reorder vulncheck quick fixes%0A  > 87d00e6 gopls/internal/lsp: separate some requests from source.Identifier%0A  > ae242ec gopls: fix windows file corruption%0A  > 6f65213 gopls/internal/lsp/protocol: Mapper.NodeMappedRange%0A  > e260368 gopls/semantic: report type parameters in the type of a receiver%0A  > b62cbb6 internal/lockedfile: fix build constraints on solaris%0A  > 1aa7e72 gopls/internal/lsp/source: avoid qualifiedObjectsAtProtocolPos%0A  > 5ed33df gopls/internal/lsp/source: rename: prep for incrementality%0A  > e0659d1 gopls/internal/lsp/source: simplify legacy 'references' func%0A  > 1edcfe7 gopls/internal/regtest/diagnostics: require cgo for TestGoListErrors%0A  > f052158 gopls/internal/lsp/protocol: move TestBytesOffset%0A  > d093a13 gopls/internal/lsp/protocol: LocationTextDocumentPositionParams%0A  > bcb677e gopls/internal/regtest: make RegexpSearch return a Location%0A  > 60782e9 gopls/internal/lsp/source: eliminate a couple uses of posToMappedRange%0A  > 031e6e6 gopls/internal/lsp/source: eliminate ResolveImportPath%0A  > f2cd9ef gopls/internal/lsp/source: reduce usage of TypecheckWorkspace%0A  > f10e7d5 gopls/internal/lsp/cache: remove package dependence on packages.Config%0A  > 8270757 gopls/internal/lsp/source: switch call hierarchy to references v2%0A  > 37c69d8 gopls/internal/lsp/source: references: support exported methods%0A  > f3c36a2 gopls/internal/lsp/cmd/test: delete marker-based tests of gopls cmd%0A  > c224aae gopls/internal/lsp/cmd/test: new integration test for gopls command%0A  > deeb64b gopls/internal/lsp/source/xrefs: allow Lookup of a set%0A  > f269f53 gopls/internal/lsp: remove Server.processModifications%0A  > fcd57eb gopls: allow 'any' and 'comparable' in completion results%0A  > aae3642 gopls/internal/lsp/source: referencesV2: support unexported methods%0A  > b5d65e0 tools/gopls: register semantic tokens statically%0A  > 51abc5b gopls/internal/lsp/source: stub: don't panic when encountering 'error'%0A  > ce28f40 gopls/internal/regtest: add a test demonstrating confusion following an%0A  > c4c6aa6 internal/lsp/cache: don't panic in Snapshot on a shutdown view%0A  > 1faecd3 tools/internal/diff: fix off-by-one error in computing diffs%0A  > a7f033a gopls/internal/lsp: consolidate the FileHandle API%0A  > 271e621 internal/lockedfile/internal/filelock: fix aix build tag%0A  > ff9bea5 gopls/internal/lsp/cmd/test: signpost future cleanups%0A  > 7d4ba2f gopls/release: remove unused functionality from release script%0A  > 46b6958 gopls/internal/lsp/source: delete source_test%0A  > bcc7794 go/analysis/passes/directive: add directive analyzer%0A  > 33d416e gopls/internal/lsp: add missing comments on 3x tests.Test impls%0A  > afea272 gopls/internal/lsp/source: make implementations2 work on embedded fields%0A  > bb7c440 gopls/internal/lsp/filecache: use file locking, not rename%0A  > 561a9be gopls/internal/lsp/filecache: actually delete files%0A  > 9682b0d gopls/internal/lsp/source: delete IsInterface%0A  > 7a7b699 go/analysis/passes/loopclosure: avoid panic in new parallel subtest check when t.Run has single argument%0A  > 3e6f71b gopls/internal/regtest: use AfterChange in more places%0A  > 9ff31a5 x/tools/go/analysis/passes/printf: revert URL in error message%0A  > 2fa6ca1 gopls/internal/lsp/source/impls: a new "implementations" index%0A  > 957bec5 gopls/protocol: new versions of generated LSP files%0A  > f0e2d5c internal/gcimporter: discard position info for unneeded lines%0A  > 5bedd86 cmd/digraph: use ReadString rather than bufio.Scanner%0A  > f6ea009 gopls/internal/lsp: remove the experimentalWatchedFileDelay setting%0A  > f46e418 gopls/internal/lsp/source: include ITVs in global references%0A  > f3e53e5 internal/jsonrpc2_v2: fix typos%0A  > d958e85 internal/gcimporter: use two-level file index%0A  > 8aba49b internal/gcimporter: preserve column and line in shallow iexport%0A  > d7fc4e7 gopls: new LSP stub generator%0A  > 5c176b1 internal/robustio: skip os.Link test on android%0A  > d34a055 go/ssa: sanity check the types of phi nodes%0A  > 6f095b4 go/callgraph/vta: add flows for receiver function types%0A  > 8e94967 cmd/fiximports: do not assume go list -json unmarshals into build.Package%0A  > e035d0c go/ssa: fix phi node type in slice to array conversion%0A  > 03eac81 go/expect: remove testdata go.mod to go.fake.mod%0A  > 1e819a3 gopls/internal/regtest: follow-ups to review comments from earlier CLs%0A  > 9ba8bb1 gopls/internal/regtest: clean up workspace symbol helpers%0A  > 91b6070 gopls/internal/regtest: eliminate DiagnosticAtRegexp%0A  > bd48b9a gopls/internal/regtest: eliminate DiagnosticsAtRegexpWithMessage%0A  > 5d65394 gopls/internal/regtest: eliminate DiagnosticAt%0A  > 27dfeb2 gopls/internal/regtest: replace NoDiagnostics with NoMatchingDiagnostics%0A  > 87092c8 gopls/internal/lsp/fake: use protocol types for the fake editor%0A  > 672a036 gopls/internal/regtest: simplify OnceMet expressions with an env helper%0A  > ab7b5b2 gopls/internal/regtest: eliminate GoSumDiagnostic%0A  > 331a1c6 gopls/internal/regtest: add a simpler API for diagnostic expectations%0A  > c9b82f2 gopls/internal/regtest: eliminate EmptyDiagnostics%0A  > e81af27 gopls: update golang.org/x/vuln@6ad3e3d%0A  > d19e3d1 internal/regtest/bench: fix BenchmarkRename and add more benchmark tests for gopls%0A  > 2be1a9a gopls/internal/regtest: rename EmptyOrNoDiagnostics to NoDiagnostics%0A  > 7ec05ac gopls/internal/regtest: eliminate NoDiagnostics%0A  > e956495 gopls/internal/regtest: eliminate DiagnosticsFor%0A  > 8087911 gopls: remove the experimentalWorkspaceModule mode%0A  > 5b300bd gopls/internal/lsp/cache: clean up view workspace information%0A  > 97d5de5 gopls/internal/cache: don't mark initialized after cancellation%0A  > 58691bc gopls/internal/lsp/glob: add an LSP compliant glob implementation%0A  > a3c22fc cmd/cover: delete package%0A  > 98dcb0e cmd/cover: remove replace directive%0A  > 7765567 gopls/internal/lsp/source: minor clarifications%0A  > a7f7db3 cmd/cover: carve out deprecated command into its own module%0A  > f9a10c0 Revert "cmd/cover: carve out deprecated command into its own module"%0A  > e345d46 internal/gcimporter: fix export of invalid methods%0A  > 4305a22 gopls/internal/lsp/cache: don't cache files if mtime is too recent%0A  > 227ee72 internal/regtest/misc: fail eagerly in TestRenameFileFromEditor%0A  > 43158af cmd/cover: carve out deprecated command into its own module%0A  > b798934 gopls/internal/lsp/protocol: cleanups and docs for Mapper%0A  > a24944e gopls/internal/lsp/protocol: rename s/ColumnMapper/Mapper/%0A  > 55935f4 gopls/internal/span: simplify Span%0A  > 40a1c97 gopls/internal/lsp/lsppos: delete Mapper%0A  > 6a3bc37 gopls/internal/lsp/protocol: reimplement ColumnMapper line logic%0A  > 6e9a35d go/callgraph/cha: refactor callee construction%0A  > fef5b76 go/callgraph: fix slicing in callgraph_test.go%0A  > 2be9d05 gopls/internal/lsp/source/xrefs: a new reference index%0A  > 0362cea gopls/internal/lsp/lsppos: delete TokenMapper%0A  > 67baca6 go/callgraph/vta: optimize scc computation%0A  > 2eb6138 gopls/internal/lsp/filecache: use TempDir if UserCacheDir fails us%0A  > 36bd3db gopls/internal/lsp/protocol: move MappedRange%0A  > 16b3bf8 gopls/internal/lsp/cache: assume Go 1.16+%0A  > 3856a5d internal/robustio: add Plan9 support to FileID%0A  > 09cbc42 gopls/internal/lsp/fake: fix EOF bug in applyEdits%0A  > 4ded35d gopls/internal/lsp/cache: use distinct types for mod and work parse keys%0A  > 107f43f gopls/completion: avoid duplicating text in test func completions%0A  > e225fd4 gopls/internal/lsp/mod: fix nil panic in go.mod hover%0A  > 057ed3c gopls/internal/lsp/filecache: use os.Chtimes%0A  > 1fe76af gopls/internal/lsp/source: MappedRange cleanup%0A  > 02bea03 gopls/internal/lsp/protocol: simplify ColumnMapper%0A  > a4455fe go/callgraph: adds benchmarks comparing algorithms%0A  > 7db99dd go.mod: update golang.org/x dependencies%0A  > 1e0dff2 gopls/internal/regtest: avoid race in TestSwitchFromGOPATHToModuleMode%0A  > 0441b43 gopls/internal/lsp/cache: use specific mutexes for module data%0A  > 33071fb internal/robustio: move robustio%0A  > b01e7a4 gopls/internal/regtest/watch: don't run TestSwitchFromGOPATHToModuleMode%0A  > e417ea3 gopls: remove dead analysis code%0A  > 1a08d01 gopls/internal/lsp: update replace directives in go.mod for package renaming%0A  > eac36cb gopls/internal/regtest: port experimental workspace tests to go.work%0A  > 224a61b gopls/internal/lsp/source: delete Snapshot.WriteEnv method%0A  > 81e741e gopls/internal/lsp/safetoken: funnel more calls through this package%0A  > 8367fb2 gopls/internal/regtest: await go.work changes in TestAddAndRemoveGoWork%0A  > 3b16059 gopls/internal/regtest: make BufferText strict%0A  > 0e1d013 gopls/internal/lsp/cache: recreate Views when their root changes%0A  > 2f31dd4 go/ssa,go/analysis/passes/nilness: refine when type param constants are nil%0A  > ae4ff82 gopls/internal/lsp/source: delete GetTypedFile%0A  > fe6b300 gopls/internal/lsp/source: eliminate Snapshot.Package{,s}ForFile%0A  > 26fc609 gopls/internal/lsp/cache: eliminate snapshot.containingPackages%0A  > 85e6ad7 gopls/internal/lsp/safetoken: fix bug in Offset at EOF%0A  > ef1ec5d gopls/internal/lsp/safetoken: fix error message%0A  > 44395ff gopls/internal/lsp/source: avoid unnecessary transitive rdeps%0A  > 6546d82 Revert "gopls/internal/regtest: harmless CL used for benchmark test"%0A  > 3be0647 gopls/symbols: call source.Document symbols only for Go files%0A  > d462c83 gopls/internal/lsp: Replace input text when completing a definition%0A  > 7efffe1 gopls/internal/regtest: harmless CL used for benchmark test%0A  > 1627e95 gopls/internal/lsp: more comment tweaks post-//line support%0A  > 21f6100 internal/lsp/debug: fix broken template%0A  > 6ad27d0 gopls/internal/robustio: FileID, a portable file identifier%0A  > 6df6eee internal/diff/lcs: optimize inner loop%0A  > 57b1265 go/gcexportdata: drop support for go1.6 export data%0A  > 099260e gopls/internal/lsp: followups to dropping line directives%0A  > 61e2d3f gopls/internal/lsp/cache: a new analysis driver%0A  > eb70795 gopls: ignore //line directives%0A  > b4dfc36 go/ssa: deref core type in emitLoad%0A  > 1270fd7 gopls/internal/lsp: announce selectionRangeProvider capability%0A  > 9bc5dce gopls/internal/lsp/cache: simplify DiagnosePackage%0A  > df35cd8 x/tools: drop support for Go toolchains older than go1.16%0A  > db9d10f go/gcexportdata: preallocate buffer to read into when size is known%0A  > 0d2045b gopls/internal/lsp: document analysis-related functions%0A  > b2b9dc3 gopls/internal/lsp/cache: reduce type-checking in renameImports%0A  > 3cb82d5 go/ssa/interp: fix conversion of slice to named array%0A  > 5899b6a gopls: upgrade dependencies following release%0A  > 763a030 gopls/internal/lsp/cache: delete Snapshot.KnownPackages%0A  > cc0e696 gopls/internal/hooks: panic if diff consistency check fails%0A  > 9ec8553 gopls/internal/lsp/source: emit interface stub methods at top level%0A  > 444c8f6 gopls/internal/lsp/cache: only invalidate parsed files if they changed%0A  > 601ca6c gopls/internal/lsp/source: use correct token.File%0A  > 95c9dce internal/lsp/mod: fix run_govulncheck codelens name%0A  > d72a64a gopls/internal/lsp: add selection range request%0A  > 18f76ec gopls/internal/lsp: split ActivePackages%0A  > 84299a0 gopls/internal/lsp/cache: simplify ad-hoc package warning logic%0A  > a3eef25 gopls/internal/lsp/cache: record parse keys when they're created%0A  > 3da7f1e gopls/hover: remove header tags from hover markdown%0A  > a310bcb gopls/internal/lsp/source: eliminate getStubFile%0A  > 3cba5a8 internal/gcimporter: port CL 424876 from std importer%0A  > b0fdb78 gopls/internal/lsp/mod: add Reset vulncheck result codelens%0A  > 88ceb24 gopls/internal/lsp: perform analysis unconditionally%0A  > 3f74d91 gopls/internal/lsp/cache: invalidate govulncheck results older than 1hr%0A  > 6b8674f gopls/internal/lsp/source: avoid typechecking in findRune%0A  > d7dfffd gopls/internal/lsp: eliminate more unnecessary typechecking%0A  > f3fb218 gopls/internal/lsp/fake: use robustio.RemoveAll in (*Workdir).RemoveFile%0A  > 96ff41d gopls/internal/vulncheck: add TODO for the vulncheck diagnostics%0A  > 0f6c6f1 gopls: delete obsolete govulncheck code and stop gopls vulncheck -summary%0A  > c5343a6 gopls/internal/lsp/regtest: fix TestRunGovulncheckError2%0A  > cb701f7 gopls/internal/lsp: avoid type-checking when computing hyperlinks%0A  > d0f184d gopls/internal/lsp/source: avoid unnecessary calls to GetTypedFile%0A  > 1e5efed gopls/internal/lsp/fake: simply use polling to simulate file watching%0A  > 838a165 gopls/internal/lsp/fake: eliminate the unnecessary fake.FileEvent%0A  > 09fb680 gopls/internal/lsp/fake: eliminate the unnecessary ChangeFilesOnDisk API%0A  > 09ae2d5 gopls/internal/lsp/source: KnownPackagePaths: avoid loading%0A  > 1dcc423 gopls/internal/lsp/cache: split metadata and loading in PackagesForFile%0A  > 6b50501 gopls/release: fix the release script when go.work is not used%0A  > aee3994 gopls/internal/lsp/fake: in (*Workdir).RenameFile, fall back to read + write%0A  > fe60148 go.mod: update golang.org/x dependencies%0A  > c9ea9a7 gopls/internal/regtest: add a test for the case when the renaming package's path contains "internal" as a segment%0A  > bf5db81 gopls/internal/lsp/cache: improve ad-hoc warning for nested modules%0A  > aa9f4b2 go/analysis: document that facts are gob encoded in one gulp%0A  > bdcd082 internal/gcimporter: skip tests earlier when 'go build' is not available%0A  > 2ad6325 gopls/internal/lsp/cache: expand ImportPath!=PackagePath comment%0A  > 52c7b88 gopls/internal/robustio: only define ERROR_SHARING_VIOLATION on Windows%0A  > 4f69bf3 gopls/internal/lsp/cache: narrow reloadOrphanedFiles to open files%0A  > 6002d6e gopls/internal/regtest/misc: test Implementations + vendor%0A  > f540ee6 internal/gcimporter: load cached export data for packages individually%0A  > d444fa3 gopls/internal/lsp/cache: simplify canonical URI cache%0A  > 25fdb81 gopls/internal/regtest/misc: skip vendor test on go1.13%0A  > e0b516b gopls/internal/lsp/cache: invalidate metadata after vendor change%0A  > 31d5843 gopls/internal/lsp/cache: fix re-entrant session locking%0A  > 8c78b30 gopls/internal/vulncheck: always use pkg.go.dev/vuln for urls%0A  > 47a8246 gopls/internal/regtest/misc: skip TestRunGovulncheckError2%0A  > d54e12b gopls/internal/lsp: avoid I/O in URI comparison operations%0A  > 0379b73 internal/gcimporter: fix TestImportStdLib%0A  > e79e423 gopls/internal/vulncheck: handle package errors%0A  > c5ce806 gopls/internal/lsp/mod: disable the diagnostics on stdlib vulns%0A  > 78c1861 gopls/internal/vulncheck: clarify the log message%0A  > 1a0053c gopls: move reset go.mod diagnostic codelens to module statement%0A  > 9b8d87b gopls/internal/regtest: fix TestRunGovulncheckStd%0A  > 81b6bef gopls/internal/lsp: add run vulncheck fix for stdlib vulns%0A  > fe83ddb gopls/internal/lsp: move options off of the cache%0A  > 88ee30b gopls/internal/lsp/source: enable run_govulncheck codelens in exp mode%0A  > 0a6aa90 gopls/internal/lsp/command: rename run_vulncheck_exp to run_govulncheck%0A  > bedad5a gopls/internal/lsp/mod: add hover for stdlib vulnerabilities%0A  > 7a1b570 gopls/internal/vulncheck: check vulnerabilities in standard library%0A  > 9a54670 gopls/internal/lsp/mod: add "Run govulncheck" codeaction%0A  > f1b76ae gopls/internal/lsp: add an option to overwrite previous diagnostics%0A  > e8a70a5 gopls/internal/lsp: remove access to mutable session state from the view%0A  > ff22fab gopls/internal/lsp/cache: eliminate obsolete invalidation step%0A  > 3881046 gopls: add a go:generate rule for doc generation%0A  > 4c3cb1e internal/gocommand: add GoVersionString%0A  > e29d1ed gopls: add diagnostic for standard library%0A  > f718365 gopls/internal/lsp: include all vulns info to fetch_vulncheck_result%0A  > 9519368 gopls/internal/lsp/mod: add the vulncheck diagnostics mode%0A  > 7d9f451 gopls/internal/govulncheck: add in-memory cache for vulndb%0A  > 1ccccf8 go/ssa: deprecate coreType and _NormalTerms%0A  > 4b7d1b3 gopls: add diagnostics for both vulns used and not used%0A  > 50ccef5 internal/regtest/bench: add benchmark tests for gopls%0A  > d39685a gopls/internal/lsp/source: Package clarifications%0A  > 7cfde84 gopls/internal/vulncheck: add import info based vuln scanning%0A  > 2b56641 internal/gcimporter: adjust the number of expected packages in TestStdlib%0A  > 50df761 gopls: skip vulnerabilities that are probably fixed in hover%0A  > 7cda55e gopls/internal/lsp/cache: wire in mod vulnerability analysis%0A  > 5c35617 gopls: add quick fixes for all vulnerabilities%0A  > fb7be64 gopls/internal/lsp/command: return the vulncheck progress token%0A  > 060c049 go/packages: fix doc typo%0A  > 6eafd96 gopls: fix formatting for vulncheck results in hover%0A  > b797704 go/analysis/passes/loopclosure: recursively check last statements in statements like if, switch, and for%0A  > 3b9d20c internal/gcimporter: in TestStdlib, only check x/tools packages if we expect to have their source%0A  > 2ad3c33 go/packages: change workaround for issue 28749 to not require NeedFiles%0A  > 57f56ab gopls/internal/lsp/source: avoid panic(nil)%0A  > 41c70c9 internal/lsp/source: avoid using go/types.Implements with Typ[Invalid]%0A  > db5eae2 analysis: correct go/analysis/passes/findcall path in docs%0A  > b978661 cmd/godoc: streamline test subprocesses%0A  > 932ec22 internal/testenv: add a Command function that replaces exec.Command%0A  > 19fb30d gopls/internal/lsp/cache: fix data race in Symbols%0A  > 4ce4f93 gopls/internal/lsp: add gopls.fetch_vulncheck_result%0A  > 8ba9a37 gopls/internal/lsp/mod: highlight when there is no fix for vuln%0A  > 128f61d gopls/internal/lsp/mod: add related info%0A  > fc03993 internal/lsp/mod: adjust vulncheck diagnostics suppression logic%0A  > c099dff gopls/internal/vulncheck: log progress%0A  > 36a5c6a go/ssa: build generic function bodies%0A  > 85bf7a8 gopls/internal/lsp/source: eliminate Metadata interface%0A  > 2592a85 gopls/internal/lsp: simplify KnownPackages%0A  > c7ed4b3 gopls/internal/lsp/cache: clean up tracking of GO111MODULE%0A  > 23056f6 internal/lsp/cache: clean up getOrLoadIDsForURI%0A  > 5a4eba5 internal/lsp/cache: remove support for invalid metadata%0A  > 32a17c0 gopls/internal/lsp/mod: fix unaffecting vuln diagnostics msgs%0A  > dea100b internal/testenv: skip tests that need export data for std if 'go tool compile' does not exist%0A  > ba373ee playground/socket: eliminate an arbitrary timeout in TestLimiter%0A  > 3d085f3 gopls/internal/lsp/lsprpc: eliminate arbitrary timeout in TestEnvForwarding%0A  > 434d569 gopls/internal/lsp/regtest: improve documentation%0A  > ce26db4 go/analysis: add Pass.TypeErrors field%0A  > b0ad6b2 gopls/internal/regtest/misc: fix use of the AfterChange API%0A  > 89856a4 gopls/semantic: semantic tokens for type parameters%0A  > 6e8da3f internal/pkgbits: port small optimization from compiler to tools%0A  > 06fb723 internal/gcimporter: port memory reuse optimizations from Go tree%0A  > fc702c5 internal/gcimporter: fix performance regression for unified IR%0A  > 1cb4c17 gopls/internal/regtest: make AfterChange do the awaiting%0A  > 0c71b56 gopls/internal/lsp: fix diagnostic suppression when folders change%0A  > e3b3c01 go/pointer: break TestInput into subtests and update skips%0A  > 13648cd gopls/internal/lsp/cache: use Package.FileSet where possible%0A  > 8f32411 cmd/stringer: replace ioutil with os%0A  > 3c3713e gopls/internal/lsp/cache: use typed strings (PackagePath et al) throughout%0A  > 004d118 gopls/internal/lsp/mod: simplify ModVulnerabilityDiagnostics%0A  > 4a8413c gopls/internal/lsp/mod: deleted unused function pkgVersion%0A  > bc08991 gopls: sync golang.org/x/vuln@3af8368ee4fe%0A  > d66e9b4 internal/typesinternal: update go/types error codes for 1.20%0A  > 6f99366 gopls/internal/lsp/cache: don't pass snapshot.fset to go/packages%0A  > d56532a cmd/compilebench: make it work without installed .a's%0A  > 502c634 go.mod: update golang.org/x dependencies%0A  > bd04e32 internal/jsonrpc2_v2: eliminate a potential Accept/Dial race in TestIdleTimeout%0A  > d41a43b internal/jsonrpc2_v2: fix a potential deadlock when (*Conn).Close is invoked during Bind%0A  > 3057465 gopls/doc: Add plugin for Lapce to gopls documentation%0A  > ba92ae1 internal/persistent: avoid incorrect map validation due to multiple keys%0A  > 9474ca3 gopls/doc: clarify `go work use`%0A  > 003fde1 internal/gcimporter: use nondeprecated go/packages mode bits%0A  > 5050657 gopls/fake: add semantic token modifiers to fake editor%0A  > 88a3548 gopls/coverage: repair coverage.go%0A  > 8e0240a internal/regtest/workspace: permanently skip TestDeleteModule_Interdependent%0A  > fe725d9 gopls/internal/regtest: simplify awaiting diagnostics from a change%0A  > 3c8152e internal/gcimporter: optimize dependency lookup%0A  > 39c2fd8 internal/lsp/cache: simplify importsState modfile hashing logic%0A  > ec044b1 gopls: update dependencies following the v0.10.0 release%0A  > 2b29c66 internal/gcimporter: API for shallow export data%0A  > affa603 internal/gcimporter: moved from go/internal/gcimporter%0A  > a77a1fb gopls/internal/lsp/mod: fix vulncheck hover message%0A  > 4ada35e gopls/internal/lsp: handle modVulncheckSource in diagnosticSource.String%0A  > e5f03c1 gopls/doc: clean up README and add a release policy%0A  > d5e9e35 go/analysis/passes/loopclosure: enable analysis of parallel subtests%0A  > 039b24b internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 32e1cb7 gopls/internal/lsp: clarify control around diagnostics%0A  > feeb0ba gopls/internal/lsp/cmd: fix deadlock when opening a file%0A  > 6e9dc86 gopls/internal/lsp/source/completion: fix panic in completion on *error%0A  > 73fcd88 Revert "internal/jsonrpc2_v2: initiate shutdown when the Writer breaks"%0A  > 70a130e gopls/api-diff: simplify the api-diff implementation%0A  > 3e8da47 internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 3566f69 gopls/internal/lsp/source: minor space optimizations%0A  > 7cdb0e7 internal/jsonrpc2_v2: rename Serve to NewServer and eliminate its error return%0A  > 28e9e50 internal/jsonrpc2_v2: eliminate error return from Bind%0A  > eabc3a0 internal/jsonrpc2_v2: eliminate isClosingErr%0A  > 4885f7c internal/jsonrpc2_v2: eliminate a temporary connection leak in (*Server).run%0A  > 739f55d internal/jsonrpc2_v2: rework Connection concurrency%0A  > e172e97 go/types/typeutil: break recursion through anonymous interfaces%0A  > f1c8f7f internal/lsp/source: optimize filter regular expression%0A  > e074ef8 gopls/internal: don't show a warning if the Go version is undetected%0A  > 7fba77c gopls/internal/lsp/source: remove deprecated settings from EnableAllExperiments%0A  > 42cb7be gopls/internal/lsp: improve the Go version deprecation message%0A  > 2af106e gopls/internal/hooks: fixes to diff disaster logic%0A  > e4bb343 go/internal/gcimporter: update to anticipate missing targets and .as%0A  > 875c31f go/internal/gcimporter: add test of export/import on std%0A  > 541f4c5 cmd/bundle: quote command-line arguments in output%0A  > de675d5 tools/gopls: argument in function bodies marked as parameter by semantic tokens%0A  > 3e1371f gopls/internal: start on LSP stub generator in Go.%0A  > 121f889 gopls/internal/lsp/mod: merge vuln diagnostics to one, and add a hover%0A  > d6511e5 internal/facts: share go/analysis/internal/facts with gopls%0A  > 2e0ca3a go/internal/gcimporter: fix bug in struct iexport%0A  > 1928cea go/ssa: emit field and index lvals on demand%0A  > 8166dca go/analysis/passes/asmdecl: define register-ABI result registers for RISCV64%0A  > 2dcdbd4 go/internal/gcimporter: port CL 431495 to tools, add tests%0A  > d476af7 go/ssa: add slice to array conversion%0A  > d212f7d gopls/internal/regtest/workspace: fix bugs in test%0A  > 051f03f gopls/internal/lsp/cache: remove unnecessary params%0A  > 21f6127 gopls/internal/lsp/cache: add PkgPath->PackageID index to Metadata%0A  > 06041c9 gopls/doc: update manual documentation of the newDiff setting%0A  > f112c43 go.mod: update golang.org/x dependencies%0A  > 207f456 go/internal/gcimporter: bump version number in skew check%0A  > 65196ca gopls/README.md: fix wording around supported Go versions%0A  > 6128030 gopls/internal: support renaming packages with int. test variants%0A  > 649df2e go.mod: mark as requiring -compat 1.16%0A  > 91311ab gopls/internal/lsp/cache: better import path hygiene%0A  > 9eda97b go/analysis: enable a test that applies after go list behavior change%0A  > b50d7ba gopls: minor cleanup of standalone package support%0A  > 502b93c gopls/internal/lsp: tolerate missing end position in RelatedInformation%0A  > d67c3ad internal/imports: repair warnings from default analyzers%0A  > bc2e3ae internal/jsonrpc2_v2: add Func convenience wrappers for the Binder and Preempter interfaces%0A  > a9b653b cmd/compilebench: use -a instead of -i to ensure dependencies are built%0A  > 4818d9e Revert "gopls/internal/lsp/cache: disable strict analysis while we fix panics"%0A  > b2efd4d internal/jsonrpc2_v2: eliminate most arbitrary timeouts in tests%0A  > 371ef16 internal/jsonrpc2_v2: rework concurrency in idleListener%0A  > 5935531 internal/jsonrpc2_v2: remove “Box” suffix from channel field names%0A  > fd32990 internal/jsonrpc2_v2: error out in-flight client calls when the reader breaks%0A  > 0e222f5 internal/jsonrpc2_v2: close the underlying connection if Wait is called instead of Close%0A  > bc4e384 gopls/internal/lsp/cache: fix crash in analysis%0A  > b93a56f refactor/satisfy: fix visiting functions in the unsafe package%0A  > 9b5e55b gopls/internal/lsp/cache: disable strict analysis while we fix panics%0A  > 9ffaf69 gopls/internal/lsp/cache: minor analysis cleanups%0A  > ffb862b gopls/internal/lsp/cache: remove stray print statement%0A  > f87c1ed internal/fastwalk: improve Darwin performance by ~3x%0A  > b253314 gopls/internal/lsp/cache: add support for loading standalone main files%0A  > 3beecff gopls/internal/span: some cleanups%0A  > d375238 gopls: dedup upgrade code actions for vulncheck%0A  > b20ae4b README: format install command%0A  > 19a5504 gopls/internal/lsp: use the golang.org/x/vuln/exp/govulncheck%0A  > ab79327 cmd/ssadump: disable run mode with runtime package%0A  > 29429f5 gopls/internal/lsp/source: sort protocol edits%0A  > 49b340b go/analysis: update tests for different go list error behavior%0A  > cd0288f internal/lsp/cache: invalidate analysis results on packages.Load%0A  > 906c733 gopls/internal/lsp/source: find references in test packages%0A  > 2a41b25 internal/robustio: fix log.Fatal calls that should be log.Fatalf%0A  > 150b5f8 internal/imports: read entire API dir in mkstdlib.go%0A  > 19cfa79 internal/lsp/source: switch the default diff algorithm to "checked"%0A  > fa6bd3b gopls: include informational vulnerability diagnostics%0A  > 89b4335 gopls/internal/lsp: merge notifications about deprecated settings%0A  > f90d8ad all: fix a few function names on comments%0A  > 350f1e2 gopls/internal/lsp/fake: retry ephemeral errors when renaming on windows%0A  > 8b1d1ec gopls/internal/lsp/cache: suppress panics during analysis%0A  > 20c1ee7 gopls/internal/lsp: warn about Go versions that are too old%0A  > 709f108 gopls/internal/lsp/cache: suppress crashes in fact_purity analyzer%0A  > a410e98 internal/diff: ToUnified may fail%0A  > 26a95e6 gopls/internal/span: move internal/span into gopls%0A  > f2c4579 internal/diff: avoid unnecessary allocations%0A  > 60ddcca internal/diff: Apply: validate inputs%0A  > 02bef08 go/packages/packagestest: break dependency on gopls' span package%0A  > 778f945 go/analysis: break dependency on span package%0A  > c682555 gopls/internal/regtest/misc: delete testdata%0A  > 1552529 gopls/internal/regtest/misc: use vulntest for vuln_test%0A  > c4f49e4 go/analysis/passes/assign: fix map assignment%0A  > bd8c28f internal/diff/lcs: fix shell format error%0A  > ede3ab2 gopls/internal/lsp/protocol: simplify OffsetRange, Position%0A  > dc3cf95 gopls/internal/vulncheck: use vulntest for test database creation%0A  > 4ef38dc gopls/internal/vulncheck/vulntest: add test helpers%0A  > 2f57270 gopls: update golang.org/x/vuln%0A  > d96b238 internal/diff: simplify API, break span dependency%0A  > 9856077 internal/diff: abolish errors%0A  > 33c2dbf gopls/internal/lsp: remove extra newlines in vulncheck diagnostics%0A  > b280e27 gopls/internal/lsp/cache: make IsIntermediateTestVariant a method%0A  > c5514b7 gopls/internal/lsp/source: use PackageFromFile in Identifier%0A  > ff4ff8b gopls/internal/lsp/source: don't type-check in FindPackageFromPos%0A  > 2d32e15 gopls/internal/lsp/cache: in tests, show all stacks during analyzer crash%0A  > dc88e7b godoc: fix some comments%0A  > 7f79a02 gopls: use fmt.Fprintf%0A  > 40dabfa gopls/internal/lsp: add support for package renaming%0A  > 55e5cff internal/diff: unified: match GNU diff for empty file%0A  > 3e0355b gopls/.../fillstruct: support generic types%0A  > ed98f10 gopls: prefix vulncheck diagnostic message with title%0A  > b180eff x/tools/go/analysis: extend json output by SuggestedFixes%0A  > d49f960 internal/lsp/cache: report analysis panics during testing%0A  > 27641fb gopls: suggest upgrading to fixed version for vulncheck diagnostics%0A  > 199742a go/analysis/passes/printf: check for nil scope of instance methods%0A  > 3db607b gopls/internal/lsp/cache: remove "discovered missing identifiers" log%0A  > a4274a8 gopls: add diagnostics for non-stdlib vulnerabilities%0A  > f80e984 gopls/internal/lsp/work: use the WorkFileError diagnostics source%0A  > 9c63911 gopls/internal/lsp: delete dead code%0A  > ae737bc gopls/internal/lsp: remove the source.Session interface%0A  > bddb372 gopls: deprecate three experimental features%0A  > 4dd4ddb go/packages: issue error if 'go list' on PATH is too new%0A  > 10e9d3c gopls/internal/lsp: tolerate new 'imported and not used' error message%0A  > eb45e98 gopls/internal/regtest: fix regtest failures from "undefined" errors%0A  > 1bfc469 gopls: update to handle 'undefined:' versus 'undeclared' in type errors%0A  > 5214f41 internal/gocommand: show pid of process%0A  > c5cd943 gopls: fix the reset_golden.sh script and regenerate golden files%0A  > 49a686d go/analysis: update explanation of (no) Diagnostics.Severity%0A  > eb25de6 go/analysis/passes/loopclosure: only check statements after t.Parallel%0A  > b243e57 gopls/internal/lsp/tests: simplify collectCompletionItems, remove Data.t%0A  > 88b5529 gopls/internal/lsp/tests: use the mustRange helper in more places%0A  > c7ac942 gopls/internal/lsp: simplify prepareRename tests%0A  > b9adce9 internal/lsp/source: derive document symbols from syntax alone%0A  > 3dda4ba all: replace deprecated egrep with grep -E%0A  > 1877b5f go/analysis/passes/printf: permit multiple %w format verbs%0A  > b3ab50b go/analysis/passes/stdmethods: recognize Unwrap() []error%0A  > 62ae586 gopls/test: disable stderr output for command line tests as well%0A  > be3ff02 go/analysis/passes/sortslice: correct diagnostic for sort.Slice(f())%0A  > 2f04713 gopls: fix out of bounds bug in extract%0A  > 16b9742 go/analysis/passes/loopclosure: use go/types' object resolution%0A  > 81a42f0 gopls/internal/lsp/tests: pass in a *testing.T to Data.Golden%0A  > 14462ef go/analysis/passes/loopclosure: experiment with checking t.Run+Parallel%0A  > 00ae48e go/internal/pkgbits: replace os.SEEK_CUR with io.SeekCurrent%0A  > 835bfdf gopls: update x/vuln to pick fix for incorrect version suggestion%0A  > 6782af0 gopls/internal/lsp/source: clarify qualifiedObject%0A  > f901623 gopls/internal/lsp: suppress noisy log output in tests%0A  > df2eb93 gopls/test: fix erroneously skipped tests, remove redundant cmd tests%0A  > 1578244 gopls: set codelensProvider in initialize response%0A  > fdf581f internal/lsp: allow extract func ranges to begin/end with comments%0A  > b256f1f gopls/internal/lsp/cache: remove distracting "safe trimming" log%0A  > 0e011a0 all: use constant to avoid repeated definitions%0A  > 4d18923 gopls/internal/fake: sort edits by both start and end position%0A  > 45ad958 gopls/internal/lsp/protocol: fix json tags and indirect some zero values%0A  > a61f20e internal/gocommand: tweak debugging for hanging go commands%0A  > cdd6986 gopls/tsprotocol: make Disabled in CodeAction optional%0A  > 0398b3d internal/gocommand: add instrumentation for hanging go commands%0A  > 9250e22 internal/lsp: latest version of LSP stubs%0A  > ec74389 gopls/internal/lsp/source: make "chatty" diagnostics the default%0A  > 7e129ca gopls: add codelens to reset upgrade diagnostics%0A  > a81fce3 gopls: run go mod tidy -compat=1.16%0A  > a8b9ed3 gopls/internal/lsp/source: remove Govulncheck from Hooks%0A  > 678efe0 gopls/internal/lsp/cmd: fix vulncheck error handling%0A  > e71c338 go/ssa/ssautil: initialize info when there is syntax%0A  > 0eebaab go/analysis: allow for identical SuggestedFixes%0A  > eeaf4eb internal/lsp/fake: add rename file support for testing%0A  > 4754f75 go/analysis/passes/copylock: modify match pattern to satisfy change sync.Once.done to atomic.Bool%0A  > a630751 x/tools: update go.mod following moving LSP code to x/tools/gopls%0A  > 308e02c x/tools/go/ssa: disable slice-to-array test%0A  > 3ee1710 gopls/doc: update stale documentation and improve link names%0A  > 5f27e05 all: remove redundant type conversion%0A  > b15dac2 gopls: migrate internal/lsp to gopls/internal/lsp%0A  > dd1bab2 go/analysis/passes/printf: fix panic parsing argument index%0A  > bac5507 go/analysis/internal/checker: make applyFixes work from the first character%0A  > c1dd25e gopls/internal/migrate.sh: a script to migrate internal/lsp to gopls/%0A  > 83d7619 gopls : add a mention of staticcheck to settings documentation%0A  > d815cba internal/lsp: update LSP protocol for WorkspaceEdit%0A  > 6a585a2 x/tools/internal/typeparams: use regexp to match wanted result%0A  > be9eab1 go/analysis/passes/inspect: fix example return%0A  > 5ba8541 x/tools/internal/lsp/source: disable some tests for std lib changes%0A  > eb8352e gopls/internal/govulncheck: sync x/vuln@62b0186%0A  > 655abda gopls/internal/regtest: TestEditGoDirectiveWorkspace should fail eagerly%0A  > 33c1ddd tools/gopls/internal/regtest/diagnostics: handle new error message%0A  > 40cfaff x/tools/internal/lsp/source: disable some tests for std lib changes%0A  > f16be35 internal/lsp/source: add functions to type hover output%0A  > dfc8d49 internal/lsp/testdata: fix diagnostics checksum%0A  > 6c10975 internal/lsp/cache: honor RunDespiteErrors=false%0A  > 49ab44d x/tools/internal/lsp: re-enable a test with adjusted error message%0A  > 550e1f5 internal/lsp/tests: use a shorter module path for test data%0A  > 4ccc73c internal/lsp/tests: simplify comparison of markdown at go1.18%0A  > 3eb8a8f internal/lsp/cache: delete misleading Package.IllTyped method%0A  > cb91d6c internal/lsp/cache: clarify error control flow of analysis%0A  > 41c3a9b internal/lsp/analysis/fillreturns: be defensive w.r.t. type errors%0A  > fe1a27b gopls/doc: make doc generation work regardless of the current directory%0A  > ddbeb75 internal/lsp: run internal/lsp/reset_golden.sh%0A  > 248c34b internal/lsp: support regular expressions in Diagnostics tests%0A  > 431f4ef internal/lsp/tests: re-enable ARM tests%0A  > 717a671 go/analysis/passes/printf: remove unused hasBasicType%0A  > 7f23307 internal/lsp: limit diagnostics for upgrades to codelens go.mod file%0A  > 7c5e035 internal/lsp: fix suppressed panic in analyzer%0A  > 2f38e1d internal/lsp/tests: disable failing test on ARM%0A  > d35bb19 internal/lsp/tests: improve assertion error message%0A  > 7111c2e x/tools/internal/lsp: disable a test so we can change the parser error%0A  > db6a62c go/internal/gcimporter: call Interface.Complete in unified importer%0A  > 587a153 internal/lsp: hover to render go 1.19 doc comments%0A  > e55fb40 internal/lsp/cache: clear shouldLoad IDs on load%0A  > a3cac11 godoc/redirect: delete golang.org-specific code%0A  > b3851a8 internal/lsp/cache: tweaks to metadata graph%0A  > 938e162 gopls/internal/regtest: unskip TestDeleteModule_Interdependent%0A  > e8507be gopls/internal/regtest/bench: replace -gopls_version with -gopls_commit%0A  > 8c83056 gopls/internal/regtest: unskip TestSumUpdateFixesDiagnostics%0A  > 987de34 internal/lsp/completion: don't use Type.String for checking identity%0A  > 5a26068 internal/lsp/source: remove utm_source from pkgsite links%0A  > 35f806b gopls/doc/workspace: correct grammar%0A  > bebd890 go/analysis: remove stray print statement in the timeformat analyzer%0A  > 88d981e printf analyzer: link to fmt#Printing for verb/type docs%0A  > c4ec74a go/internal/pkgbits: fix performance of rawReloc%0A  > 37a81b6 internal/lsp: add unnecessary tags for unused vars and imports%0A  > 3807419 internal/lsp/cache: validate the range for critical errors in go files%0A  > b2156b5 gopls: update dependencies%0A  > 0ad49fd internal/imports: update stdlib index for 1.19%0A  > 3950865 gopls/internal/regtest/bench: add a -gopls_version flag%0A  > 6fa767d internal/lsp: update documentation for directoryFilters setting and default value%0A  > 96d05aa gopls/internal/regtest: fix TestFailingDiagnosticClearingOnEdit%0A  > 4ff08b4 gopls: Improve auto-imports example for NeoVim LSP%0A  > 92d58ea internal/lsp/cache: register a file watcher for explicit GOWORK values%0A  > 98aef77 internal/lsp/cache: track explicit go.work files outside the workspace%0A  > fff6d6d internal/lsp: update the broken workspace message to mention go.work%0A  > 9b60852 gopls/internal/regtest: move TestMultipleModules_Warning to ./workspace%0A  > 06d96ee gopls/internal/regtest/bench: add a test for completion following edits%0A  > 81c7dc4 internal/lsp: polish vulncheck progress messages%0A  > af2a0a8 internal/lsp: use exec.CommandContext when running vulncheck%0A  > 3519aa2 internal/lsp/cmd: remove unused Env from pkgLoadConfig%0A  > 6c27717 internal/lsp/mod/code_lens: add "run govulncheck" codelens%0A  > 763f65c gopls/internal/regtest/misc: simplify shared edit tests%0A  > fc3b24a go/internal/gcimporter: rewrite interface receiver parameters%0A  > b5fd088 internal/lsp/command: replace VulncheckArgs Dir with URI%0A  > 99fd76f internal/lsp/cache: delete KnownMetadata.PkgFilesChanged%0A  > 01c9ff0 internal/lsp/cache: invalid packages should not be workspace packages%0A  > bd68922 internal/lsp: new options to disable certain kinds of semantic tokens%0A  > bceee4b internal/lsp/command: let RunVulncheckExp call gopls vulncheck%0A  > 3e0a503 internal/lsp: use directoryFilters in import scanning%0A  > 87f47bb gopls/internal/regtest/bench: refactor and improve benchmarks%0A  > 8b9a1fb go/callgraph/vta: do not assume that recovers cannot be deferred%0A  > 371fc67 go/tools: add check for time formats with 2006-02-01%0A  > d08f5dc gopls/internal/regtest: unskip all of TestModFileModification%0A  > ddb90ec internal/lsp/cache: fix data races to view.options%0A  > 0d04f65 internal/lsp: re-send diagnostics on file events%0A  > d025cce internal/lsp/source: don't crash requesting gc_details for an empty file%0A  > 10cb435 internal/lsp/regtest: improvements for shared execution modes%0A  > 4d0b383 internal/lsp/regtest: minor cleanup for magic regtest envvar%0A  > 310ea71 gopls/internal/regtest: add a test that ignoring a file resolves errors%0A  > 21861e6 gopls/internal/regtest/bench: put feature benchmarks in their own file%0A  > c7f1191 go/internal/gcimporter: set underlying types in proper order; flatten imports%0A  > bd3f524 internal/lsp: rename all the package names in the renamed package%0A  > 9f65685 internal/lsp/source: enable the new diff with allExperiments%0A  > 9580c84 internal/lsp: Check if user's editor support rename operation%0A  > f560bc8 internal/lsp/cache: don't set context cancellation as a critical err%0A  > 8ea5687 internal/lsp/regtest: remove arbitrary timeout for closing the editor%0A  > d01bb2f internal/lsp/source: document the handling of GOPRIVATE for linkTarget%0A  > 98bfcd1 internal/memoize: fix race in Store.Promise%0A  > e02e98a internal/lsp/cache: allow network whenever reloading the workspace%0A  > b52794a internal/lsp/cache: simplify snapshot.Clone reinitialization logic%0A  > f1bb5ca internal/lsp/cache: report a critical error when go.work is invalid%0Abumping golang.org/x/mod b3066c3...b710602:%0A  > b710602 sumdb/dirhash: correct documentation of hash%0A  > a42224d all: replace io/ioutil with io and os package%0A  > 77d797e sumdb/dirhash: fix a panic when argument is not a directory%0A  > 7c05a44 sumdb/note: remove dependency on golang.org/x/crypto/ed25519%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping knative.dev/serving 2c1bb07...c91f8c4:%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping knative.dev/eventing 034bec9...2a5a9a5:%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping knative.dev/networking e5d04e8...2a2f7d2:%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated fil…

---
## [eschulma/evals](https://github.com/eschulma/evals)@[170dfd886c...](https://github.com/eschulma/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Tuesday 2023-05-30 02:07:36 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

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
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [eschulma/evals](https://github.com/eschulma/evals)@[b93700ab49...](https://github.com/eschulma/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Tuesday 2023-05-30 02:07:36 by DunedainStrider

Do math problems related to calculating dates using the Chinese Sexagenary Cycle method. 🧮 (#190)

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
Do math problems related to calculating dates using the Chinese
Sexagenary Cycle method

### Eval description

The Sexagenary Cycle combines 10 Heavenly Stems (Jia 甲, Yi 乙, Bing 丙,
Ding 丁, Wu 戊, Ji 己, Geng 庚, Xin 辛, Ren 壬, Gui 癸) and 12 Earthly Branches
(Zi 子, Chou 丑, Yin 寅, Mao 卯, Chen 辰, Si 巳, Wu 午, Wei 未, Shen 申, You 酉,
Xu 戌, Hai 亥) to form a 60-unit cycle. To calculate, convert the
Gregorian date to its corresponding Heavenly Stem and Earthly Branch
combination, used for marking specific years, months, and days.

### What makes this a useful eval?

The existing GPT models tend to make errors when performing calculations
related to the Sexagenary Cycle. To address this issue, we have provided
a specialized dataset aimed at improving the model's accuracy in
handling Sexagenary Cycle calculations.

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

[2023-03-16 12:46:51,594] [record.py:320] Final report: {'accuracy':
0.65}. Logged to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl
[2023-03-16 12:46:51,594] [oaieval.py:211] Final report:
[2023-03-16 12:46:51,594] [oaieval.py:213] accuracy: 0.65
[2023-03-16 12:46:51,597] [record.py:309] Logged 60 rows of events to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl:
insert_time=2.463ms

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"甲戌的次日是？"}], "ideal": "乙亥"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"乙亥的次日是？"}], "ideal": "丙子"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬寅的后日是？"}], "ideal": "甲辰"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"癸卯的后日是？"}], "ideal": "乙巳"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬子的后日是？"}], "ideal": "甲寅"}
  ```
</details>

---------

Co-authored-by: dunedainstrider <dunedainstrider@mac16>

---
## [eschulma/evals](https://github.com/eschulma/evals)@[2ffd4b57de...](https://github.com/eschulma/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Tuesday 2023-05-30 02:07:36 by Andrew Kondrich

add more logging (#964)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
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
  INSERT_EVAL_HERE
  ```
</details>

---
## [LynxSolstice/cmss13](https://github.com/LynxSolstice/cmss13)@[84fd6b6eb7...](https://github.com/LynxSolstice/cmss13/commit/84fd6b6eb7fdd48d8499b954dfd216fd5a42ed04)
#### Tuesday 2023-05-30 02:11:52 by ihatethisengine

Medevac Buffs (#1513)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request
Reduces cooldown of medevac from 60 seconds to 20 seconds. PO no longer
needs to manually activate the winch, so medevac can be operated from
the cockpit. What's more, you can operate medevac by interacting with
the medevac system itself, and even if you don't have the skills of a
pilot, you can use it if you have the skills of a doctor (which means
nurse can run medevac). And finally, the medical stretcher is now
automatically activated when deployed.

I know there is a PR by jeser that reduces cooldown, but it stuck in PR
hell anyway and also I changed more stuff.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Since we want to force wounded marines to go shipside, we must provide
them a more convenient way to reach the Almayer. Medevac was always
underutilized because it required too much coordination and unnecessary
actions (e.g. having to activate medical stretcher every time, keep in
mind a huge portion of the medic playerbase still has no idea you need
to do this). PO had to spend their limited fly-by time (which should
normally be used on firemissions) to manually activating the winch,
which was always annoying. And cooldown is ridiculous. You have at best
three minutes of fly-by, so that means you could use medevac only twice
(remember that you needed to run to the system every time) per fly-by,
which is definitely not enough.
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

:cl: ihatethisengine
balance: reduced the medevac cooldown from 60 seconds to 20 seconds.
add: anyone with the skills of a doctor or a pilot can manage the
medevac by interacting with the system itself.
qol: medical stretcher automatically activates when deployed.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [llegomark/evals](https://github.com/llegomark/evals)@[24f78a806e...](https://github.com/llegomark/evals/commit/24f78a806e60b452aaefc355f045c6336a81d076)
#### Tuesday 2023-05-30 04:50:47 by YuryRudnitski

Add eval for guessing the singer or band (#659)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
guess-the-singer

### Eval description

This evaluation measures the model's ability to identify a singer or
band by analyzing the first 10 words of a song. To ensure the
evaluation's fairness and focus, we have excluded songs with multiple
singers/bands and included only those published before 2021. To test the
model's performance, we provide it with three potential choices and
evaluate its accuracy in selecting the correct one.

### What makes this a useful eval?

The inclusion of over 4000 popular songs' lyrics provides a large and
diverse dataset for the model to test on. This enables a more accurate
assessment of the model's performance and its ability to identify
singers/bands based on the first 10 words of their songs.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> This evaluation assesses not only the model's ability to recognize a
singer or band based on the first 10 words of a song but also its
capability to accurately copy the provided options without adding any
additional punctuation or text. By testing the model's ability to
replicate the options, we can gain insights into its language generation
capabilities and identify any areas for improvement in its output.
Accuracy achieved with gpt-3.5-turbo equals 0.635.


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
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: in the beginning god created heaven
and earth for what \nChoices: dua lipa, ed sheeran, lady gaga"}],
"ideal": "dua lipa"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: versedrake ayye yo dj wristpect let's
get em' veterans like \nChoices: cardi b, drake, coldplay"}], "ideal":
"drake"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: yeah yeah sick da got that dope they
\nChoices: eminem, dua lipa, nicki minaj"}], "ideal": "eminem"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: bobby v yeah bobby v yeah dj turn me
up \nChoices: nicki minaj, selena gomez, coldplay"}], "ideal": "nicki
minaj"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: ed sheeran yeah i was born a misfit
grew up \nChoices: ed sheeran, maroon 5, justin bieber"}], "ideal": "ed
sheeran"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: there's a dream in my soul a fire
that's deep \nChoices: justin bieber, charlie puth, bts"}], "ideal":
"justin bieber"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: selena gomez take it or leave it baby
take it \nChoices: selena gomez, justin bieber, bts"}], "ideal": "selena
gomez"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: lalala lalala lalalalala oh you know
i've never felt like \nChoices: rihanna, ed sheeran, charlie puth"}],
"ideal": "rihanna"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: how could i see you when i was so
blind \nChoices: katy perry, ed sheeran, drake"}], "ideal": "katy
perry"}
  ```
</details>

Co-authored-by: Vadim Titko <v.tsitko@aiby.com>

---
## [llegomark/evals](https://github.com/llegomark/evals)@[6087aee945...](https://github.com/llegomark/evals/commit/6087aee94583a5ac440f024756b2d9a5f3754410)
#### Tuesday 2023-05-30 04:50:47 by lucasfoufou

Find country from svg (#418)

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
Find country from svg

### Eval description

Test the model's ability to distinguish a country based on its svg shape
(from wikimedia svg file).

### What makes this a useful eval?

Multiple real life use case, the first one would be to understand that a
svg shape is a country (it could be very useful for scraps via [Text
from:] prompts). On the opposite side, while asking to create an app or
a website (with a map, I just had the case for a client), GPT would
currently hint you to find the svg of the country on the web, mainly
linking to wikimedia, this solution is quicker.

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

GPT currently lacks of geography "knowledge" (I've tried him on multiple
tasks where it fails), this evals would help him "recognize" country
shapes, if that's a thing ?

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval
(it's in public domain from wikimedia)

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
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1277.96,284.094 c 0.89,-0.422
1.96,-0.686 2.95,-0.504 0.34,-1.514 -1.67,-0.473 -2.09,-1.512
0.92,-0.307 2,-0.194 2.96,-0.145 -0.75,-0.129 -1.77,0.138 -1.23,-0.792
-0.58,-0.03 -2.55,1.079 -2.79,0.108 -0.32,-1.325 1.7,-2.125 2.66,-2.315
1.29,-0.256 2.51,-0.36 3.82,-0.324 1.85,0.05 3.04,-1.75 5.1,-1.501
-0.24,0.665 2.23,2.987 2.92,2.708 0.47,-0.226 0.91,-0.484 1.34,-0.772
0.94,-0.521 0.88,0.152 1.66,0.302 0.77,0.148 1.37,-0.462 1.42,0.787
0.5,-0.347 -0.24,-0.762 0.17,-1.327 0.43,-0.577 0.65,0.299 1.02,0.397
0.88,0.232 2.02,0 2.91,-0.15 -1.89,-0.553 -1.2,-3.219 -1.04,-4.608
0.1,-0.676 -0.95,-1.354 -1.3,-1.826 -0.6,-0.813 0,-2.049 -0.9,-2.711
0.65,0.114 1.25,0.434 1.9,0.569 0.71,0.148 1.58,-0.549 2.21,-0.235
0.97,0.488 -0.24,1.954 1.1,2.724 0.39,0.222 1.09,-0.173 1.49,-0.177
1.17,-0.01 2.29,0.385 3.43,0.601 1.11,0.211 2.08,0.179 3.07,-0.39
0.9,-0.515 2.11,-0.496 2.93,-1.075 -0.65,0.256 -1.75,0.386 -2.38,0.03
-1.27,-0.731 1.67,-2.529 2.15,-2.748 1.55,-0.694 3.31,-0.611 4.88,-1.241
0.91,-0.365 2.13,-2.453 3.26,-1.869 -0.99,-0.639 -0.38,-5.064
0.44,-5.893 0.81,-0.814 4.94,-2.286 6.01,-1.391 0.54,0.456 -0.52,2.21
1.06,2.601 1.63,0.403 1.25,0.04 2.41,0.383 1.08,0.325 0.74,1.156
1.57,1.56 1.09,0.527 2.19,-0.1 2.05,1.586 0.65,-0.419 1.78,-0.322
2.46,-0.08 1.3,0.444 0.75,2.039 0.49,2.965 0.87,0.145 1.85,0.414
2.71,0.07 0.85,-0.341 1.05,-1.314 1.9,-1.654 0.1,0.536 -0.15,2.933
0.58,2.959 1.07,0.04 3.23,1.451 3.56,2.478 -0.1,-0.296 4.07,0.378
4.28,0.396 1.02,0.09 1.77,-0.122 2.58,0.715 0.63,0.66 1.07,1.697
2.03,1.948 0.21,-0.1 0.37,-0.244 0.5,-0.438 0.31,-0.321 0.46,0.105
0.79,0.15 0.19,0.07 0.24,0.196 0.15,0.377 -0.1,0.392 0.86,0.178
1.01,0.191 1.03,0.09 1.61,-0.538 2.56,0.183 1.01,0.768 3.09,0.91
4.35,1.121 -1.54,1.365 -2.97,2.863 -3.47,4.891 -0.24,0.986 -0.83,1.892
-0.99,2.886 -0.1,0.65 0.12,0.914 -0.14,1.749 -0.31,1.009 0.46,1.85
-0.22,2.476 -0.58,0.528 -1.02,1.037 -1.88,0.96 -0.72,-0.06 -0.78,-1.131
-1.65,-0.648 -0.62,0.349 -0.68,1.463 0.36,1.296 -0.78,0.826 -1.48,1.807
-2.38,2.52 -0.55,0.358 -1.09,0.734 -1.61,1.128 -0.43,0.39 -0.39,1.154
-0.76,1.608 -0.62,0.774 -1.83,1.138 -2.02,2.232 0.14,0.373 0.24,0.757
0.29,1.151 -0.15,0.709 -0.81,0.962 -1.08,1.584 1.19,-0.149 1.63,-0.555
1.94,-1.691 0.31,-1.118 2.37,-1.032 3.21,-0.797 1,0.283 0.32,1.927
1.04,2.728 1.27,1.392 0.49,1.914 -0.65,2.857 0.61,0.857 2.88,2.445
2.26,3.701 -0.43,0.843 -3.57,2 -3.56,2.144 0,0.994 1.97,1.841 2.63,2.408
0.96,0.82 -1.33,2.281 -1,3.365 0.4,1.316 2.92,2.808 4.25,2.275
1.67,-0.669 1.42,0.304 0.79,1.417 -1.52,2.681 -4.43,4.033 -7.03,5.786
0.17,0.244 0.34,0.484 0.51,0.72 -0.97,0.139 -1.78,0.637 -2.69,0.955
-0.97,0.343 -1.6,-0.197 -2.52,-0.124 -1.4,0.11 -2.26,-1.056 -3.93,-0.903
0.67,-1.731 -2.2,-0.404 -2.23,-1.41 0.18,-0.312 0.47,-0.394 0.86,-0.246
0,-0.567 -0.37,-0.887 -0.94,-0.864 0.48,0.734 0.1,0.842 -0.59,0.875
-1.09,0.05 -1.2,-0.01 -1.5,-1.307 0.39,2.583 -0.27,0.936 -1.94,0.936
-0.97,0 -1.76,-0.61 -2.7,-0.656 -1.15,-0.06 -2.42,1.249 -3.45,1.719
-0.8,0.367 -3.62,1.411 -3.44,2.5 0,0.357 -0.13,0.689 -0.32,0.996
-0.45,0.4 -0.41,0.756 0.11,1.068 0.4,1.252 0.14,1.879 0.87,3.086
-0.69,0.197 -1.29,-0.149 -1.97,-0.108 -0.7,0.04 -1.06,0.605 -1.69,0.777
-1.52,0.415 -2.45,-1.16 -3.91,-0.1 -0.1,0.07 -2.12,-0.872 -2.34,-1.035
-0.57,-0.423 0.73,-0.369 -0.18,-0.978 -0.53,-0.353 -1.48,-0.508
-1.93,0.07 -0.21,-1.289 -1.64,-0.75 -2.41,-1.362 -1.07,-0.845
-3.26,-1.387 -2.92,0.643 -1.2,-0.173 -2.55,-0.475 -3.76,-0.253
-0.67,0.123 -1.12,0.313 -1.69,-0.203 -1.02,-0.914 -0.94,-0.538
-1.97,-0.552 -1.03,-0.01 -5.97,-3.26 -6.48,-1.944 -0.94,-0.386
-0.27,-1.066 -0.21,-1.721 0.1,-0.779 -2.2,-0.424 -2.67,-1.015
2.86,-1.059 3.1,-5.023 3.62,-7.601 0.21,-1.012 0.39,-2.607 1.23,-3.329
1.23,-1.052 -0.42,-1.2 -0.53,-0.01 -0.17,-2.436 0.32,-5.421 1.37,-7.632
1.01,0.569 2.02,1.244 2.45,2.376 0.1,0.504 0.19,1.008 0.29,1.512
0.23,0.641 0.87,0.729 0.86,1.512 0.29,-1.007 -0.73,-1.782 -0.83,-2.736
-0.14,-1.466 -0.66,-2.459 -1.96,-3.172 -0.54,-0.298 -1.15,-0.705
-1.6,-1.142 -0.74,-0.712 1.19,-0.357 1.58,0 -0.91,-0.441 -0.96,-4.294
-0.43,-5.04 -1.19,0.835 -4,-0.808 -4.55,-1.915 -0.49,-0.979 -1.6,-1.488
-1.82,-2.631 -0.2,-1.043 1.71,-2.185 -0.69,-2.293 0.28,-0.333
0.34,-0.938 0.7,-1.192 0.92,-0.638 1.76,0.435 2.62,0.544 -1.53,-1.009
-2.13,-0.674 -3.73,-0.466 -0.8,0.105 -2.36,-1.08 -0.88,-1.262
-0.41,-0.407 -0.24,-0.671 0.5,-0.792 -1.13,-0.282 -2.75,0.642
-3.67,-0.36 0.51,0 0.99,-0.127 1.44,-0.36 -0.9,-0.604 -2.57,-0.359
-2.81,0.864 0,-0.8 -0.92,-1.548 -0.1,-2.231 -0.35,0.876 -1.92,0.819
-0.94,-0.288 -1.99,1.73 -4.67,-2.209 -6.69,-0.07 -0.81,-1.117
-1.48,-1.803 -2.87,-2.092\"/></svg>"}], "ideal": ["France"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" id=\"cd\" class=\"landxx cd\" d=\"m
1393.81,748.499 c 0.69,-0.521 1.53,-0.08 1.8,-1.012 0.22,-0.755
0.84,-3.721 0.31,-4.328 -1.38,-1.588 4,-3.988 5.01,-4.891 0.27,1.147
1.95,1.314 2.02,2.521 0.54,-0.559 1.25,-0.89 1.85,-1.371 0.81,-0.656
0.47,-1.845 1.18,-2.589 1.2,1.591 3,-1.453 4.41,-0.744 1.35,0.676
0.11,0.977 -0.1,1.824 -0.23,0.951 0.37,1.993 0.37,2.949 0.6,-0.772
1.92,0.202 2.73,-0.359 1.19,-0.829 1.93,-2.404 2.84,-3.516 0.47,-0.576
2.39,-1.501 2.49,-2.024 0.27,-1.382 1.42,-1.713 2.56,-2.2 2.66,-1.134
3.13,-6.138 3.07,-8.528 0,-1.819 0.12,-3.463 -0.11,-5.279 -0.22,-1.742
1.97,-2.189 2.71,-3.567 1.73,-3.247 1.6,-5.301 5.12,-7.692 1.48,-1.007
2.38,-2.189 3.37,-3.577 0.98,-1.382 0.27,-3.4 0.67,-4.985 0.35,-1.392
1.03,-7.368 1.09,-8.935 0.1,-1.771 1.09,-3.324 1.38,-5.05 0.29,-1.671
-0.2,-3.438 0.17,-5.092 0.71,-3.114 2.57,-5.662 3.63,-8.623 0.62,-1.72
0.33,-3.533 0.28,-5.287 0,-0.809 0.35,-1.657 0.22,-2.448 -0.11,-0.705
-0.53,-1.293 -0.72,-1.971 -0.31,-1.078 1.57,-1.049 2,-2.032 0.6,-1.357
1.23,-2.549 2.25,-3.647 0.99,-1.052 2.22,-1.952 3.73,-1.941 1.27,0
1.78,1.112 2.6,1.293 1.89,0.419 3.65,2.466 4.35,4.206 0.58,1.421
2.62,0.36 3.77,0.707 0.63,0.188 0.94,1.033 1.66,1 0.63,-0.03 0.77,-0.145
1.42,0.191 0.99,0.506 1.19,0 2.17,-0.06 0.65,-0.04 1.36,0.302 1.96,0.522
1.07,0.398 2.54,1.173 3.71,0.76 2.1,-0.738 1.46,-5.749 4.25,-5.88
1.59,-0.08 2.01,3.142 4.09,1.177 0.88,-0.831 6.94,-1.633 6.57,-3.625
1.26,-0.05 1.68,1.669 2.88,1.548 1.45,-0.146 3.93,-0.364 4.53,-1.908
0.23,-0.576 -0.35,-1.151 0.41,-1.533 0.93,-0.466 1.7,-0.188 2.42,0.528
1.17,1.147 2.25,-0.203 3.54,0.408 0.64,0.302 1.17,0.782 1.79,1.105
0.73,0.376 1.25,0.06 2.02,0.172 1.83,0.275 2.54,-1.756 4.47,-0.662
0.73,0.416 3.28,2.021 3.28,2.97 0,0.465 0.6,1.612 1.05,1.796 1.9,0.773
3.71,3.567 5.73,1.659 1.15,-1.082 2,-1.298 3.52,-0.555 1.56,0.765
2.18,0.455 3.11,-1.363 1.21,-2.397 4.32,3.607 4.48,4 0.71,1.754
5.45,1.985 4,4.723 0.92,-0.216 2.04,-0.273 2.27,0.9 0.11,0.313
0.27,0.603 0.48,0.867 0.12,0.602 -0.7,1.727 -0.61,2.355 0.29,2.012
0,4.015 -0.34,5.933 -0.15,1.011 0.6,0.878 1.74,0.678 0.52,-0.09
2.5,1.295 2.14,2.396 -0.86,2.629 -4.13,5.237 -6,7.185 -0.62,0.644
-1.87,2.357 -2.62,2.99 -0.75,0.632 -0.83,0.09 -1.26,0.918 -0.54,1.034
0.12,2.297 -0.53,3.355 -0.73,1.174 -1.45,2.943 -1.61,4.325 -0.14,1.238
-0.12,2.489 -0.2,3.731 -0.11,1.453 -0.3,2.722 -0.45,4.102 -0.11,1.009
0.15,2.425 -0.31,3.349 -0.53,1.051 -1.38,1.445 -2.15,2.296 -1.19,1.317
-1.09,1.742 -1.14,3.287 0,1.018 -1.11,2.163 -1.67,2.89 -1.21,1.603
0.48,3.278 1.42,4.805 0.71,1.151 1.22,1.959 0.7,3.544 -1.91,1.674
0.4,6.932 -1.4,8.659 1.31,0.757 1.07,-2.637 1.53,-2.063 0.45,2.673
-1.22,4.611 -1.23,7.23 0,3.402 2.85,4.969 1.64,7.322 -0.7,1.358
-1.43,1.657 -0.84,2.532 0.9,1.34 1.28,3.548 3.06,7.032 1.19,2.328
4.59,1.892 4.79,7.5 0.1,2.201 1.8,0.993 2.46,4.37 -4.7,1.073 -8.17,1.196
-12.89,2.206 1.95,3.224 -3.12,4.564 -4.03,6.979 2.71,0.838 1.81,5.035
1.63,7.086 -0.14,1.493 0.43,2.903 0.34,4.381 0,0.775 -0.21,1.511
-0.52,2.18 -0.45,0.968 -0.76,1.698 -1.01,2.72 -0.49,2.006 -1.17,3.153
0.1,5.093 0.89,1.35 2.52,3.048 3.69,4.155 0.53,0.497 3.31,2.201
3.52,1.167 0.39,-1.837 0.87,-1.494 2.68,-2.012 0,2.897 -0.1,5.805
-0.18,8.701 0,0.447 0.32,2.356 -0.43,2.431 -0.88,0.09 -1.07,-0.928
-0.46,-1.413 -1.3,-1.593 -4.21,3.376 -5.58,0.392 -0.46,-0.994
-0.89,-2.254 -1.56,-3.155 -0.38,-0.512 -1.4,-1.171 -1.52,-1.776
-0.23,-1.183 -0.46,-2.555 -1.95,-2.597 -1.25,-0.03 -1.79,-1.34
-2.98,-1.484 -1.01,-0.121 -1.62,0.635 -2.31,-0.466 -0.54,-0.854
-0.56,-2.098 -1.34,-2.799 -1.11,-1 -1.91,-4.476 -2.88,-1.358 -1,3.216
-2.76,1.525 -5.27,1.614 -1.69,0.06 -2.09,-0.477 -3.51,-1.124 -0.1,-0.04
-1.6,-0.401 -1.64,-0.394 -2.28,0.4 -2.96,-3.062 -2.15,-4.641 -1.4,0.08
-2.81,0.375 -4.11,0.87 -1.61,0.608 -1.95,1.4 -3.74,0.65 0.69,-1.238
0.73,-2.872 0.13,-2.843 -0.78,0.04 -1.11,-0.627 -1.65,-1.14 -1.25,-1.191
-1.08,0.215 -1.38,0.318 -1.11,0.385 -1.6,0.328 -2.6,0.07 -1.21,-0.313
-1.96,0.53 -3.03,0.908 -1.37,0.485 -2.24,-0.437 -3.13,-0.283 -0.32,0.05
-1.59,-0.08 -1.63,-0.06 -0.86,0.463 -1.3,1.761 -2.48,1.732 0.27,-0.889
-0.27,-1.587 -0.42,-2.422 -0.22,-1.147 0.58,-1.353 0.83,-2.235
0.58,-2.045 -0.22,-5.594 -1.46,-7.239 -1.51,-2.007 -2.16,-3.263
-1.97,-5.861 0.19,-2.685 1.13,-5.502 0.43,-8.174 -0.27,-1.021
-0.99,-1.907 -0.98,-2.99 0,-1.224 0.7,-2.37 0.79,-3.585 0.15,-2.002
-1.14,-1.78 -2.77,-1.795 -1.54,-0.01 -3.07,-0.04 -4.61,0.02 -3.17,0.134
-2.69,-0.557 -1.79,-3.234 -0.71,0 -1.41,-0.18 -2.1,0.09 -0.46,0.182
-0.12,0.385 -0.38,0.609 -0.84,0.717 -4.68,0.09 -5.8,0.09 0.37,0.946
-0.32,2.053 -0.16,3.064 0.13,0.817 0.16,2.114 -1.14,1.836 0.42,1.246
-0.33,2.482 -0.1,3.74 -0.53,0 -3.97,0.114 -4.53,-0.209 -1.65,-0.955
-4.55,0.828 -5.11,0.878 -1.31,-0.213 -2.54,-0.151 -3.97,-0.144
-1.82,-0.38 -2.61,-4.163 -3.52,-5.497 -0.32,-0.47 -0.57,-0.807
-0.91,-1.274 -0.61,-0.864 -0.33,-1.484 -0.46,-2.405 -0.22,-1.639
-1.94,-2.716 -1.69,-4.456 0.22,-1.565 0,-2.871 -0.74,-3.785 -1.02,-1.277
-1,-1.747 -2.6,-1.67 -4.38,0.21 -8.73,0.382 -13.11,0.132 -3.54,-0.201
-7.68,0.384 -11.15,-0.285 -2.78,-0.536 -5.08,3.601
-6.72,-0.577\"/></svg>"}], "ideal": ["Democratic Republic of the
Congo"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1390.14,847.849 c 1.06,-0.165
1.89,-1.097 3.02,-0.896 0.97,0.171 1.84,0.902 2.86,0.707 2.12,-0.406
3.58,-2.884 6,-2.224 1.93,0.526 2.95,2.692 4.89,3.334 1.09,0.365
4.47,0.223 6.27,0.239 8.21,0.07 16.44,0.234 24.65,-0.1 2.17,-0.09
2.9,-0.247 3.93,1.67 1.3,2.439 3.25,1.9 5.6,2.158 3.07,0.337 6.34,0.197
9.22,1.207 1.11,0.388 2.1,0.528 3.08,-0.06 0.86,-0.524 1.69,-0.336
2.94,-0.03 1.26,0.308 2.01,0.1 2.85,-0.1 5.12,-1.189 10.92,-2.392
16.36,-3.42 1.05,-0.2 2.12,-0.682 3.21,-0.515 0.65,0.1 1.62,0.721
2.26,0.401 2.05,-1.02 2.99,1.138 4.34,2.064 -0.98,-0.256 -2.13,0.318
-3.06,0.681 -1.16,0.451 -1.5,2.182 -2.61,1.159 -1.79,-1.646 -5.29,3.747
-6.61,4.381 -0.64,-1.236 -1.33,-3.988 -3.16,-4.161 -2.36,-0.223
-5.3,0.967 -7.59,1.454 -2.71,0.573 -5.9,0.683 -8.59,1.185 l -1,31.899
-6.8,-0.1 -1.47,54.378 c 0.17,2.48 -1.96,1.44 -3.14,2.56 -0.59,0.56
-0.54,1.1 -1.71,1.5 -0.8,0.28 -1.17,0.61 -0.52,1.35 -1.79,0.53
-1.71,-0.14 -3.38,-0.39 -1.75,-0.26 -3.25,0.69 -5.32,0.24 -3.29,-0.7
-5.24,-1.92 -5.39,-2.52 -0.41,-1.68 0,-0.99 0,-2.32 -0.1,-0.53
-0.64,-0.39 -1.04,-0.8 -0.57,-0.6 -1.06,-1.86 -1.67,-1.48 -1.9,1.21
-1.37,3 -2.04,3.52 -0.94,0.73 -2.12,1.7 -3.11,0.46 -1.3,-1.64
-3.04,-2.94 -4.2,-4.69 -1.03,-1.56 -1.86,-3.228 -2.69,-4.895
-0.44,-0.885 -0.48,-1.837 -0.64,-2.792 -0.15,-0.986 -0.83,-1.5
-1.02,-2.398 -0.35,-1.647 0.38,-2.252 -0.84,-3.77 -0.48,-0.606
-0.32,-0.997 -0.3,-1.771 0,-1.251 -0.41,-2.334 -0.54,-3.554 -0.1,-0.869
0,-1.749 -0.27,-2.599 -0.36,-1.202 0.25,-2.365 0,-3.567 -0.4,-2.072
-1.39,-3.963 -2.14,-5.918 -0.85,-2.207 -0.21,-4.07 -0.43,-6.304
-0.15,-1.516 -0.38,-3.414 -0.24,-4.197 0.1,-0.367 0.99,-4.049 0.58,-3.96
-0.1,-1.983 -1.09,-3.925 -2.22,-5.516 -0.63,-0.895 -1.36,-1.729
-1.89,-2.693 -0.49,-0.886 -0.59,-1.97 -1.23,-2.777 -2.94,-3.719
-3.57,-8.234 -5.75,-12.264 -1.99,-3.694 -2.66,-8.768 -5.9,-11.674
-3.49,-3.125 -3.9,-7.688 -3.6,-12.097\"/></svg>"}], "ideal":
["Namibia"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1372.42,438.678 c
-0.96,-0.829 1.1,-1.805 1.63,-2.052 1.61,-0.745 2.47,-1.172 3.44,-2.748
0.78,-1.267 1.57,-1.885 1.26,-3.517 -0.26,-1.407 -0.93,-2.825
-0.78,-4.293 0.19,-2.013 2.64,-1.498 3.03,-2.941 0.42,-1.555 1.69,-2.357
2.99,-2.975 0.99,-0.475 4.23,-1.358 4.26,-2.736 0,-0.69 -0.67,-1.117
-0.59,-1.85 0.13,-1.342 0.18,-2.69 0.31,-4.032 1.29,0.9 3.03,1.355
4.42,2.209 1.46,0.896 3.11,1.201 4.81,1.015 1.71,-0.188 2.98,-1.275
4.74,-0.637 1.57,0.569 3.24,0.628 4.77,1.28 1.36,0.581 2.46,1.63
3.83,2.168 1.2,0.471 2.83,-0.02 3.9,0.719 1.26,0.873 1.5,2.371
1.74,3.773 0.31,1.794 1.02,3.224 2.41,4.429 2.53,2.176 5.65,1.666
8.69,2.217 3.04,0.554 7.38,1.939 9.83,3.917 1.95,1.582 3.75,4.253
6.55,4.002 3.22,-0.291 6.67,-3.134 7.39,-6.372 0.33,-1.495 -0.68,-2.658
-1.14,-4.005 -0.5,-1.485 -0.87,-3.192 -0.36,-4.729 0.93,-2.82
5.57,-6.318 8.52,-6.417 1.52,-0.05 2.41,-1.154 3.82,-1.262 1.44,-0.11
2.97,-0.136 4.38,0.208 1.64,0.401 3.07,1.195 4.63,1.805 1.85,0.723
1.36,0.974 1.45,2.59 0.1,1.309 2.18,1.586 3.13,1.656 1.83,0.138
3.01,0.967 4.7,1.457 1.68,0.487 3.44,-0.08 5.15,0.236 0.96,0.176
2.42,2.102 2.07,3.114 -0.36,1.068 -1.66,1.34 -1.84,2.542 -0.25,1.66
0.81,2.891 1.1,4.435 0.33,1.737 -0.79,3.275 -1.38,4.785 -0.63,1.602
1.01,3.505 1.29,5.163 0.46,2.826 0.96,5.498 1.14,8.396 l 1.78,75.281 c
-2.49,0 -4.98,0 -7.48,0 0.1,1.439 0,2.883 0.14,4.32 l -59.65,-33.761
-13.53,6.482 c -1.14,0.313 -2.55,-1.557 -3.21,-2.222 -2.8,-2.783
-5.83,-3.352 -9.55,-4.197 -1.32,-0.302 -3.06,-0.456 -4.24,-1.19
-0.94,-0.582 -1.38,-2.224 -1.77,-3.174 -1.14,-2.791 -2.53,-3.55
-5.26,-4.578 -0.91,-0.341 -1.77,-1.111 -2.77,-1.085 -0.97,0.02
-2.02,1.104 -2.93,0.118 -0.74,-0.8 -2.02,-2.856 -2.04,-3.963 0,-2.316
-0.26,-3.162 -1.54,-5.134 -0.98,-1.52 -4.24,-4.22 -2.84,-6.243
1.62,-2.334 4.1,-1.441 3.04,-5.269 -0.53,-1.915 -0.91,-3.386
-0.26,-5.329 0.56,-1.665 0.9,-3.039 0.28,-4.76 -0.64,-1.81 -0.14,-3.622
0,-5.461 0.19,-2.18 -0.13,-4.379 -0.86,-6.438 -0.62,-1.766 -1.53,-3.429
-2.62,-4.947\"/></svg>"}], "ideal": ["Libya"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1174.6,515.237 c 0.16,-0.371
0.67,-1.265 1.64,-1.315 l 27.88,-0.03 c 1.42,-0.747 0.44,-6.909
0.35,-9.281 -0.17,-2.384 -0.41,-3.937 1.5,-5.746 1.6,-1.514 1.54,-1.128
6.63,-3.207 l 1.12,-21.833 24.87,-0.291 0.34,-11.071 c 9.47,6.373
18.77,12.937 27.9,19.782 h -13.21 l 5.42,72.911 c 0.45,1.192 1.68,1.706
1.79,1.985 0.72,1.855 -0.23,2.415 -0.3,3.844 -0.1,1.675 -0.25,3.183
-0.74,3.363 l -15.88,0.02 c -9.03,0.312 -12.89,1.548 -13.69,-1.121
-0.39,2.416 -3.97,2.811 -5.73,2.11 -2.79,-1.107 -4.57,-0.64 -5.71,2.498
-0.65,-1.071 -1.59,-1.985 -2.56,-2.918 -1.15,-1.106 -2.25,-1.698
-2.86,-1.361 -2.29,1.269 0.9,7.651 -4.72,7.248 0,0.102 -1.51,-1.093
-1.92,-1.876 -0.51,-0.967 -1.09,-0.659 -2.06,-1.487 -1.05,-0.897
-0.98,-2.361 -1.84,-2.934 -2.31,-1.535 -1.4,-1.554 -1.61,-2.594
-0.27,-1.282 -1.57,-2.914 -2.22,-2.923 -3.4,-0.05 -3.64,-2.805
-5.84,-3.866 -1.12,-0.536 -2.08,-0.818 -3.58,-0.867 -2.33,-0.08
-3.14,2.203 -8.49,1.803 -1.13,-0.08 -0.98,-0.838 -1.94,-0.565
-0.93,0.342 -2.03,3.346 -2.4,4.133 0,-5.202 3.42,-9.445 3.92,-14.544
0.29,-3.07 -0.13,-5.666 -0.52,-8.672 -0.14,-1.084 -0.1,-2.273
-0.79,-3.192 -0.6,-0.802 -1.65,-1.372 -1.76,-2.464 0.8,0.25 1.69,-0.345
1.59,-1.224 -0.54,0.145 -0.97,0.552 -1.16,1.08 0.2,-1.044 1.04,-1.777
1.5,-2.694 0.29,-0.593 -0.14,-1.541 0.21,-1.938 1.57,-1.792 -0.83,-4.97
-1.42,-6.744 -0.24,0.428 -0.41,0.884 -0.5,1.368 -1.59,-1.202
-1.21,-3.688 -2.81,-4.896 -0.25,1.062 -0.64,2.092 -0.86,3.1635
-0.21,-1.3785 -0.1,-2.3295 0.46,-3.6545 z\"/></svg>"}], "ideal":
["Mauritania"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1702.78,554.229 c -2.43,-0.09
-1.06,-5.061 -3.46,-5.344 1.08,-1.714 -2.92,-7.033 -3.61,-8.909 l
-2.81,-6.489 c -7.13,1.401 -14.28,2.934 -21.3,3.881 -5.85,1.805
-8.8,4.713 -10.12,7.879 -1.22,1.824 -1.88,6.43 -4.8,6.253 -1.99,-0.12
-1.78,-3.107 -3.69,-2.881 -2.42,0.285 -4.39,0.24 -6.84,-0.104
-1.39,-0.195 -2.82,-1.184 -4.18,-1.184 -1.5,0 -3,0.145 -4.5,0.287
-1.84,0.174 -3.39,1 -5.3,0.895 -1.05,-0.06 -1.44,-1.224 -2.51,-1.357
-1.02,-0.128 -1.81,0.563 -2.24,1.429 -0.47,0.945 -0.62,2.091 -0.44,3.129
0.11,0.672 1.05,1.339 0.54,2.028 -0.48,0.653 -0.87,1.324 -1.36,2.004
-0.27,0.372 -0.6,0.665 -1.01,0.88 -0.96,0.48 -0.47,0.845 -0.27,1.898
0.31,1.668 -0.32,2.441 -0.61,3.961 -0.28,1.407 0.9,2.63 0.77,4.029
-0.27,-0.24 -1.7,-0.277 -1.46,0.282 0,-0.117 1.44,0.726 1.44,0.722
0.8,0.856 1.1,1.742 1.38,2.862 0.53,2.196 0.58,4.644 1.27,6.78
0.28,0.877 0.98,1.533 1.32,2.388 0.4,1.031 0,2.149 0,3.204 0,2.087
2.48,3.843 1.8,5.963 0.92,0.07 1.54,-0.446 2.47,-0.07 0.99,0.396
1.67,0.723 2.77,0.506 2.25,-0.447 3.26,-2.023 5.61,-0.79 -0.12,-0.64
0.56,-1.29 0.79,-0.359 0.39,-0.428 0.61,-0.925 0.93,-1.401 0.49,-0.753
1.3,-0.736 1.96,-1.238 1.48,-1.118 1.65,-2.245 3.69,-2.713 1.9,-0.437
3.91,-0.52 5.85,-0.342 1.14,0.104 3.06,-1.206 4.2,-1.53 1.71,-0.483
2.56,-1.96 4.06,-2.792 0.46,-0.255 1.11,-0.832 1.61,-0.981 0.55,0.02
1.07,0.149 1.57,0.391 0.57,0.03 1.12,-0.04 1.66,-0.203 3.63,-0.584
4.44,-4.338 7.7,-5.939 1.52,-0.744 2.86,-0.932 4.47,-1.215 2,-0.348
3.65,-1.686 5.62,-2.154 1.36,-0.326 2.74,-0.583 4.07,-1.061 1.32,-0.478
1.79,-1.532 2.91,-2.103 0.93,-0.474 2.93,-0.415 3.21,-1.675 0.34,-1.46
-0.68,-2.788 -0.15,-4.277 1.07,-3.009 4.74,-2.89
6.99,-4.536\"/></svg>"}], "ideal": ["Yemen"]}
  ```
</details>

---------

Co-authored-by: Lucas Fougeras <lucasfougeras@DIGITALCACTUS>

---
## [llegomark/evals](https://github.com/llegomark/evals)@[1785cf6cc2...](https://github.com/llegomark/evals/commit/1785cf6cc289c4a01445fd0eabdfa1a281873d1c)
#### Tuesday 2023-05-30 04:50:47 by Jongseung (John) Lim

Add evals for complementary colors in color theory (#749)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
color_theory_complementary

### Eval description

Test the model's ability to accurately recognize complementary colors in
the color theory.

### What makes this a useful eval?

Color theory is an important tool for designers and aritsts alike.
Complementary color sets represent the opposite color on the color
wheel.

Currently gpt-3.5-turbo fails with 0.5 accuracy.


![image](https://user-images.githubusercontent.com/4276174/233743568-b58879f6-73eb-48eb-9f95-5720bcb11b73.png)


GPT 4 also fails at this task and also fails when being prompted about
complementary color of a specific rgb code.


![image](https://user-images.githubusercontent.com/4276174/233743682-1cd0d148-9d8c-43fc-93b6-d5e4a60fca26.png)


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
- [X] **Include at least 15 high quality examples.**

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
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5F6E]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5E6E]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6E89F3]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6D89F3]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53B]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53C]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA404]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA504]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2A19FA]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2919FA]"}], "ideal": "N"}
  ```
</details>

---
## [llegomark/evals](https://github.com/llegomark/evals)@[3dd0a24da8...](https://github.com/llegomark/evals/commit/3dd0a24da87c3eefd7f17424bdf124ae87698d89)
#### Tuesday 2023-05-30 04:50:47 by Pranav Gade

[eval] swap two words (#280)

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
Swap Words

### Eval description

This eval asks the model to swap two random words, so "chat gpt" should
become "gpt chat"

### What makes this a useful eval?

Robustly being able to swap words around seems like a foundational
capability the model should know, as moving things around probably helps
a lot with logic/math tasks if the model is thinking out aloud.

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"FRKLXk PrOQNNod\""}], "ideal": "\"PrOQNNod FRKLXk\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"hdJLcGtgv VaPHvqHUm\""}], "ideal": "\"VaPHvqHUm hdJLcGtgv\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"AZmgciwu ApPfVAelBGTGq\""}], "ideal": "\"ApPfVAelBGTGq
AZmgciwu\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"IQJeJQTxpKmYZ WppHdbeayUULw\""}], "ideal": "\"WppHdbeayUULw
IQJeJQTxpKmYZ\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"MuXvXQCQbtatHZy Yjnlus\""}], "ideal": "\"Yjnlus
MuXvXQCQbtatHZy\""}
  ```
</details>

---
## [llegomark/evals](https://github.com/llegomark/evals)@[2a94eeb9e1...](https://github.com/llegomark/evals/commit/2a94eeb9e13175344b2d61afa22171df0e49b61a)
#### Tuesday 2023-05-30 04:50:47 by Jeff Kile

Evals for Spanish Feminine Nouns with Masculine Articles (#861)

Added evals for feminine Spanish words that should have masculine
articles

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
spanish_feminine_noun_masculine_article

### Eval description

In Spanish singular feminine words are usually proceeded by La as in La
casa (the house), however many feminine words that start with an "a"
sound are proceeded by El instead of La as in El agua (the water)

### What makes this a useful eval?

For people learning Spanish its a very common mistake to write La agua
(because agua is feminine) but this is not correct. GPT should not
reinforce this mistake especially for people learning or asking
questions about Spanish words.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

For students using GPT to learn Spanish its very important that the
model knows all the rules and the exceptions to those rules or the
students will be mislead

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
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"agua"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"águila"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"ala"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"alba"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"amapola"}],"ideal":["La"]}
  ```
</details>

---
## [ivafractal/evals](https://github.com/ivafractal/evals)@[da73bb5f07...](https://github.com/ivafractal/evals/commit/da73bb5f071c31c3dd571989f057b8e36d3a9334)
#### Tuesday 2023-05-30 05:28:16 by mysterious-progression

Detect highly sensitive human data (#852)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Detecting highly sensitive human data
### Eval description
This eval tests whether models can successfully detect possible highly
sensitive human data without returning false positives on values that
cannot exist in practice. There are many types of highly sensitive human
data but some of the most common and types are but not limited to social
security numbers, passport numbers, credit card numbers, and driver's
licenses. Not all values are valid for a given type. For example, credit
card numbers have a numbering system specified by
https://www.iso.org/standard/39698.html, and use check digits to
validate.

Similarly, passport numbers must comply with the ICAO D9303
https://www.icao.int/publications/documents/9303_p4_cons_en.pdf
<img width="1273" alt="Screenshot 2023-04-27 at 11 01 23 PM"
src="https://user-images.githubusercontent.com/45504048/235056158-3f0eb640-109e-47c5-a64c-554d6d55f708.png">


### What makes this a useful eval?
Institutions spend millions of dollars trying to detect non-encrypted
HSHD in their internal datasets. A combination of regex, ML, and
hard-coded logic is often used yielding complicated, hard to maintain
codebases. The risk associated with plaintext HSHD is high and certain
institutions can be subject to heavy fines if HSHD is leaked if not
properly stored.


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
[evals).](url)

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value
This eval combines many aspects of language processing and
understanding. The task involves understanding what HSHD are, domain
knowledge about what makes them valid, and algorithmic understanding in
order to validate (i.e. check digits)

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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
{"input": [{"role": "system", "content": "Detect whether Passport number
is present in the text. Any potential Passport number that cannot be
valid should not be returned. If valid Passport number is found return
it's value, otherwise return '\"None\""}, {"role": "user", "content":
"Passenger with passport number: 11111111111111 is booked for a
flight"}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether a SSN is
present in the text. Any potential SSN that cannot be valid should not
be returned. If valid SSN is found return it's value, otherwise return
\"None\""}, {"role": "user", "content": "Bob has an SSN of
123-45-6789"}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether a SSN is
present in the text. Any potential SSN that cannot be valid should not
be returned. If valid SSN is found return it's value, otherwise return
\"None\""}, {"role": "user", "content": "The Jane's husban's social
security number is: 331-71-1232"}], "ideal": "331-71-1232"}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "Lemmiwinks
charged his brother Wikileaks on his CC:4193523869738880, $400"}],
"ideal": "4193523869738880"}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Visa card ending in
1738481092549663."}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Master card ending in
1738-4810-9254-9663."}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Discover card ending in
1738-4810-9254-9665."}], "ideal": "1738-4810-9254-9665"}
{"input": [{"role": "system", "content": "Detect whether passport number
is present in the text. Any potential passport number that cannot be
valid should not be returned. If valid passport number is found return
it's value, otherwise return \"None\""}, {"role": "user", "content":
"Passenger with passport number: 1*****1 is booked for a flight"}],
"ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether passport number
is present in the text. Any potential passport number that cannot be
valid should not be returned. If valid passport number is found return
it's value, otherwise return \"None\""}, {"role": "user", "content":
"Passenger with passport number: (*) is booked for a flight"}], "ideal":
"\"None\""}
  ```
</details>

---
## [ivafractal/evals](https://github.com/ivafractal/evals)@[f58f95ba32...](https://github.com/ivafractal/evals/commit/f58f95ba324e5a1ed86315f3c39ee758f2836bd3)
#### Tuesday 2023-05-30 05:28:16 by ali risheh

[Eval] Mandaliof table test (#847)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Mandaliof table test

### Eval description

This Eval is checking if the model can find a specific atom with the
highest atomic number among 20 different atoms.

### What makes this a useful eval?

There are applications in biophysics and biochemistry (like drug
discovery) that rely on physics equations and induction on atom
features. If ChatGPT is going to be used in this field, it should be
very reliable in case of understanding physical facts. Interpretation of
the periodic table is a very simple Eval that shows the model is still
unreliable for use cases in this field.

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
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

Physics problems are almost the most difficult tasks for any deep
learning model since they are based on fundamentals of nature, and even
humans are not capable of understanding comprehensive explanations of
them. In this regard, if ChatGPT will be able to interpret physical
facts, it is very likely that it can interpret literally everything
because even human are not able to do that.

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

Mandaliof table is the basic of physics.

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
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. I, Mg, Nd, Rf, Si, Ho, Fr, Ar, Xe, Rh,
Am, No, Rf, Bi, Cd, In, Sc, Te, Ce, Ge"}], "ideal": "Rf"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Fm, Ac, C, Ir, Ba, Rn, Ti, Sc, B, Nb, Cl,
Ra, Cr, Hs, Bk, Tl, Mt, S, He, Mc"}], "ideal": "Mc"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Ta, Bh, Bi, Ce, Rf, Lv, Bi, Gd, Cs, Ho,
Ta, Np, Cm, Sr, Pb, Pu, Ne, Og, Tm, Fm"}], "ideal": "Og"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Tl, Eu, Ts, Be, Ga, Cm, Ba, Sr, C, Cl,
Mo, Ni, Ru, Hs, In, Be, Dy, Ho, Br, Mt"}], "ideal": "Ts"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Mn, Hg, Pm, K, Ge, P, Fr, Cn , Mn, Fr,
Lv, W, Gd, Mt, Cd, Xe, Ge, I, Og, Br"}], "ideal": "Og"}
  ```
</details>

---
## [ivafractal/evals](https://github.com/ivafractal/evals)@[2167c99864...](https://github.com/ivafractal/evals/commit/2167c998643af0de952e1cceaf346d7b99d49104)
#### Tuesday 2023-05-30 05:28:16 by Jeff Kile

Identify which scale mode a series of notes belongs to (#860)

Added evals to determine the scale mode name based off the nodes in the
scale

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
music_theory_scale_modes

### Eval description
Test the model's ability to identify which western music scale a series
of 7 notes belongs to

### What makes this a useful eval?

This is good for analyzing music or getting help with music theory
problems like figuring out which scale to use to solo over a series of
chords, or which scale to use to write a melody depending on the mood or
chord selection.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

GPT-4 often hallucinates on these and will give a confident incorrect
answer

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
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G# A# B C# D# E?"}],"ideal":["E Lydian"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G# A B C# D E?"}],"ideal":["E Mixolydian","E Dominant"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G A B C D E?"}],"ideal":["E Aeolian","E Minor"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F G A A# C D E?"}],"ideal":["E Locrian"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: F G A A# C D E F?"}],"ideal":["F Ionian","F Major"]}
  ```
</details>

---
## [PolarstarCoffee/Wizard392](https://github.com/PolarstarCoffee/Wizard392)@[0b2827aa53...](https://github.com/PolarstarCoffee/Wizard392/commit/0b2827aa536f9c9028eef245ec73acf33d8805e4)
#### Tuesday 2023-05-30 05:35:31 by Sam

Sam's Super Mega Update

-Enemy Type Array for spawn ( random enemy type will spawn at set spawn locations)
-Added 2 spawn points top left and top right
-Adjusted Spawn timing on all 7 spawn points
           -Left spawns first
            -Right spawns 2nd
            -Bottom left/right spawn around when beat drops
             -Top left/right spawn around 40 seconds to increase difficulty curve as song progresses
             -Adjusted time between enemy spawn per spawn point to between 5-9 seconds
-Doubled Enemy Speed
-Made enemy speed vary based on enemy type
-Added current iteration of "Zack's" beat (Look how easy it is to spell his name right)
-Shrunk the rune ring/visualizer slightly
-Adjusted Wizards position in ring to be more centered
-Added pulse script to Wizard/Rune Ring
-Adjusted Pulse intensity on a few assets
-Fixed Drunken tree so that he is no longer drunk
-Applied Drunken tree effect to Drunk Gnome because that shit is funny and canonically makes more sense on the Gnome enemy
-Removed Audio control on Main Camera 1 (we had 2 audio controllers for some reason)
-Added the most fucked up SFX deathsounds(SEND HELP)

---
## [orthography/tgstation](https://github.com/orthography/tgstation)@[2aaafd9a67...](https://github.com/orthography/tgstation/commit/2aaafd9a67c270fa0772cd9beffb6789d53750e3)
#### Tuesday 2023-05-30 06:25:27 by TheVekter

Replaces the syndicate corpse Legions can drop with one without a MODSuit (#75700)

## About The Pull Request
This is part of a pass I'm working on doing where I go through and
remove instances of antag gear outside of their normal context. This is
mostly going to involve replacing space/Lavaland ruin gear with
something close to the same power level but not distinctly something
only antags should be able to get. I want to keep ruins rewarding but I
don't want explicit antag gear to be something you can obtain without
needing an uplink.

The first part of this is me removing the MODSuit from the syndicate
operative corpse. The new one drops a turtleneck, a syndicate gas mask,
and gripper gloves.

## Why It's Good For The Game
It's my opinion that antag gear should probably stay in antag hands
unless you manage to kill one or steal an uplink. The main impetus for
this was a discussion I had a while back about how blood red hardsuits
used to _just_ be an antag thing. I kind of miss that general feeling of
paranoia that came from seeing someone wearing it, as opposed to seeing
it these days and just thinking "Yeah, it's probably someone who got it
from space".

In this specific instance, Syndicate MODSuits are pretty strong anyway
and, regardless of the low odds of getting one, I really don't think it
should be available as loot off a fairly easy-to-kill mob.

## Changelog
:cl:
balance: Syndicate corpses dropped from killing a Legion no longer come
with a MODSuit.
/:cl:

---
## [gotenksIN/android_kernel_nothing_sm7325](https://github.com/gotenksIN/android_kernel_nothing_sm7325)@[89841fbb16...](https://github.com/gotenksIN/android_kernel_nothing_sm7325/commit/89841fbb16a600826a18a73a717af915c8bb17af)
#### Tuesday 2023-05-30 07:13:57 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

commit f53af4285d775cd9a9a146fc438bd0a1bee1838a upstream.

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [L8X/Roblox-Client-Optimizer](https://github.com/L8X/Roblox-Client-Optimizer)@[3e47c0172a...](https://github.com/L8X/Roblox-Client-Optimizer/commit/3e47c0172a5e2c0272981f4cf18e2a6527aeaa19)
#### Tuesday 2023-05-30 07:24:35 by Exponential-Workload

fix: fuck you no pipebomb in your mailbox

& by pipebomb in your mailbox i mean icon

---
## [Amanetes/naming-cheatsheet](https://github.com/Amanetes/naming-cheatsheet)@[8bcb483976...](https://github.com/Amanetes/naming-cheatsheet/commit/8bcb4839762053a095ee8cbbf3b4f5b471d01181)
#### Tuesday 2023-05-30 07:52:15 by tebb

docs: improve a/hc/lc pattern order explanation (#40)

Thank you.  This cheatsheet is very useful.

If I understood the logic, my changes to README.md may be helpful.  If not, sorry :)

Also ... Could you add shouldUpdateComponent and shouldComponentUpdate into the table (or an extension to the table below Note:).  It isn't obvious to me which columns 'should', 'Update' and 'Component' are in because 'Update' is the verb (action?).

Thanks.

---
## [dtrudg/singularity](https://github.com/dtrudg/singularity)@[4fdce0d1c5...](https://github.com/dtrudg/singularity/commit/4fdce0d1c59af8158f3f2e293ddcfda2dda301e8)
#### Tuesday 2023-05-30 08:45:41 by David Trudgian

Allow kernel squashfs / extfs mount to be disabled in singularity.conf (release-3.11)

In singularity.conf, add two directives `allow kernel squashfs` and
`allow kernel extfs` which default to 'yes'. When set to 'no', these
directives prevent a squashfs mount or extfs mount from being
performed through the kernel. Note that this only happens in setuid
mode / as root.

squashfs and extfs mounts are added from the various locations that
handle loopback mounting of a filesystem image. The image could be a
container rootfs, an overlay, or an image bind. In each case the image
may be a standalone file or embedded in a SIF.

The simplest place to gate these mounts is in mount.AddImage, via the
existing check that the fs type is authorized as the source for an
image mount.

Authorized filesystems for image mounts are held in a package var. At
the start of container creation we now explicitly authorize squashfs
and extfs, unless disabled by singularity.conf.

Relying on a package scope variable isn't ideal. We have multiple
processes at container creation, so the authorization must be
performed in the right place. e2e tests have been added to verify
overlay, image bind, and container rootfs image flows.

Gating the filesystems earlier in the `PrepareConfig` portion of the
runtime is, in my opinion, more liable to errors as the checks would
have to be replicated in the multiple places that images are handled.

Ideally the mount.System could perhaps hold the list of allowed /
disallowed filesystems, that could be set when it is created. However,
this would require a large amount of refactoring to complex and
critical code.

---
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[bd0c332bad...](https://github.com/davidhildenbrand/qemu/commit/bd0c332baddbed5e7fada0f4a4cb79b65578eb76)
#### Tuesday 2023-05-30 09:33:55 by David Hildenbrand

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
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[23fb937f1a...](https://github.com/davidhildenbrand/qemu/commit/23fb937f1a23af61a63950617607550376c63509)
#### Tuesday 2023-05-30 09:42:28 by David Hildenbrand

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
## [luxi-record/react-sourceCodeDebug](https://github.com/luxi-record/react-sourceCodeDebug)@[c7b4497988...](https://github.com/luxi-record/react-sourceCodeDebug/commit/c7b4497988e81606f1c7686434f55a49342c9efc)
#### Tuesday 2023-05-30 10:00:20 by Andrew Clark

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
## [melvin-mendoza/formbricks](https://github.com/melvin-mendoza/formbricks)@[27d63c01e1...](https://github.com/melvin-mendoza/formbricks/commit/27d63c01e1a772a745da074b535138f3d605f101)
#### Tuesday 2023-05-30 10:09:45 by Matti Nannt

Introducing the new Formbricks (#210)

### New Formbricks Release: Complete Rewrite, New Features & Enhanced UI 🚀

We're thrilled to announce the release of the new Formbricks, a complete overhaul of our codebase, packed with powerful features and an improved user experience.

#### What's New:

1. **Survey Builder**: Design and customize your in-product micro-surveys with our intuitive survey builder.
2. **Trigger Micro-Surveys**: Set up micro-surveys to appear at specific points within your app, allowing you to gather feedback when it matters most.
3. **JavaScript SDK**: Our new JavaScript SDK makes integration a breeze - just embed it once and you're ready to go.
4. **No-Code Events**: Set up events and triggers without writing a single line of code, making it accessible for everyone on your team.
5. **Revamped UI**: Enjoy an entirely new user interface that enhances usability and provides a smooth, delightful experience.

This release marks a major step forward for Formbricks, enabling you to better understand your users and build an outstanding product experience.

Please update your Formbricks integration to take advantage of these exciting new features, and let us know in the Discord if you have any questions or feedback!

Happy surveying! 🎉

---
## [Doan-Pham/Stren](https://github.com/Doan-Pham/Stren)@[f9742954b7...](https://github.com/Doan-Pham/Stren/commit/f9742954b7d4a08850115ebcc38a105b6ed9527c)
#### Tuesday 2023-05-30 10:14:18 by DoanPham

feat: Add methods for fetching default values

In the application, certain data will have default values (Ex: each user
in NutritionDiaryScreen, which is for tracking nutrition and calories,
has 4 meals by default - Breakfast, Lunch, Dinner, Snacks). Adding these
values for each user on the database will require enormous efforts, so
the alternative is to group the default values in a different data
source, and merge the default values with user's personal data whenever
fetching data

---
## [Stefsk-glitch/App](https://github.com/Stefsk-glitch/App)@[243b9c4ab3...](https://github.com/Stefsk-glitch/App/commit/243b9c4ab3be86f81f554477c73075280d161ae1)
#### Tuesday 2023-05-30 10:53:09 by GertieMeneer

Merge pull request #32 from Stefsk-glitch/login

omg im cumming stewie holy fuck

---
## [Addust/tgstation](https://github.com/Addust/tgstation)@[56d960a763...](https://github.com/Addust/tgstation/commit/56d960a7630d0b03bfcd59c073b29393a70a1891)
#### Tuesday 2023-05-30 11:18:25 by GoldenAlpharex

Wintercoats can now be zipped and unzipped through alt-click and separates the hood sprites from the jacket sprites (#74886)

## About The Pull Request
The title says it all, really.

~~Initially, I was only going to do it for all wintercoats, but then I
figured I might as well bring it down to all of `/hooded`, just so other
suits could benefit from it, since that behavior came from there anyway.
Does that mean that it does nothing for some of them? Yes, it does. Does
that justify having another variable to tell whether or not that should
be possible? In my humble opinion, not really, but I'm not against it if
it's requested.~~

~~That functionality was intentionally removed from the Void Cloak, as
there would be balance implications (since bringing up the hood makes
the whole cloak invisible, which you could skirt by just "zipping" it,
which also makes it invisible.~~

~~The sprites were already there, so this change was very simple to do.
Simply unties the zipped up look from the fact that the hood is up.
However, toggling the hood forces the zipping/unzipping, just so there's
no balance implications involved. It's just simpler that way.~~

So, I ended up going back and changing the sprites so that the hoods
would no longer be baked into the jacket's sprites, so that they could
be done as overlays instead, which ended up solving my problem with
hoods not being there on zipped-up versions.

For now, it's been made on winter coats only, but it shouldn't be that
difficult to bring it back down to the `/hooded` level. I just didn't
want to bother touching up the sprites down there, as it already took me
like 2-3 hours touching up the sprites of the winter coats alone.

I also took the decision to make it so EVA winter coats used the regular
winter coat's sprites, because they had special ones that just looked
like worse versions of the original, without anything special going on
for them. It was just a straight downgrade compared to the base sprite,
in my opinion.

There's still issues with the custom winter coat, in that the hood isn't
made into an overlay for it yet (and that'll require an extra bit of
logic to make it work, too), but it was already an issue before, the
hood is always present on the current version of the custom winter coat.

There's still a handful (sadly, most) of the winter coats that don't
properly reflect on their obj sprites when they're opened versus when
they're closed, but that's due to an initial spriter oversight, and not
to my doing. The open versions were just left as closed on many of them,
and I simply don't have the patience nor the appropriate skills to edit
that many coats that way.

## Why It's Good For The Game
Now you can be stylish with or without the hoodie!

![image](https://user-images.githubusercontent.com/58045821/233544697-cc821c3a-d965-4d96-af44-c44ff866496f.png)

![image](https://user-images.githubusercontent.com/58045821/233544711-da956b6b-44c4-4903-a34f-4d2890abc781.png)

![image](https://user-images.githubusercontent.com/58045821/233544717-b5221b04-0e6d-4931-83d0-d56fdac60ec3.png)


According to ChatGPT, with one small tweak (thanks Opera GX for the
suggestion):

> Zipped and unzipped through alt-click, winter coats can now be. Hmm,
stylishly warm, you shall be. Feel like a Spaceman, you will. Use the
Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.

## Changelog

:cl: GoldenAlpharex, ChatGPT for the first changelog entry (slightly
edited)
qol: Zipped and unzipped through alt-click, winter coats can now be.
Hmm, stylishly warm, you shall be. Feel like a Spaceman, you will. Use
the Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.
image: Winter coats no longer have their hood baked into their jacket's
sprite, both in item form and when worn.
fix: Updated the Icebox EVA winter coats (the Endotherm winter coats) to
use the same sprites as the regular winter coats.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[661624802b...](https://github.com/odoo-dev/odoo/commit/661624802b1c50cb9cad4ad11bc59db7f9375f8a)
#### Tuesday 2023-05-30 11:27:56 by Jeremy Kersten

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

closes odoo/odoo#119230

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4
Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [LegaspinoCindy/Legaspino_IT2A_finalproject_AnimeWorld](https://github.com/LegaspinoCindy/Legaspino_IT2A_finalproject_AnimeWorld)@[88619887d1...](https://github.com/LegaspinoCindy/Legaspino_IT2A_finalproject_AnimeWorld/commit/88619887d1f09d72919f4aca0d5df63b2f0034c0)
#### Tuesday 2023-05-30 11:44:20 by LegaspinoCindy

Create README.md

Anime World is a web app is an ultimate online destination for anime enthusiasts seeking a visual feast of captivating anime artwork. Our photo gallery is dedicated to showcasing the mesmerizing world of anime through stunning visuals that will leave you spellbound.
At Anime World, we understand the power of anime artistry and its ability to transport us to extraordinary realms. Our team of passionate anime lovers has curated a diverse and carefully selected collection of anime images that represent the beauty, diversity, and creativity of this captivating art form. With our extensive photo gallery, we aim to celebrate the exceptional talent of anime artists and the incredible attention to detail that goes into creating each frame. From breathtaking landscapes to intricate character designs, action-packed scenes to heartwarming moments, our collection encompasses the full spectrum of emotions and experiences that anime has to offer.

---
## [mshurkaeu-public/i-care.by](https://github.com/mshurkaeu-public/i-care.by)@[cd26a84942...](https://github.com/mshurkaeu-public/i-care.by/commit/cd26a84942eb3287f0ce6e59f8b6cc3e1409e66a)
#### Tuesday 2023-05-30 11:49:19 by Mikalai Shurkaeu

Replace description of the target audience on the second introductory screen

on my opinion, the new description describes the target audience
better than previous "those, who want to live their own lives".
The new description is easier to understand.

Old description:
"What is own life?" Do I want that "own life"?

New description:
You care about something important? - Yes, of course.
Do you want to care about that more pleasantly and efficiently? - Yes!

The commit contains 640x426 photo of a flood in Bingley, Bradford,
United Kingdom in 2015. The photo made by Chris Gallagher
(https://unsplash.com/@chriswebdog) on Unsplash (https://unsplash.com).
The photo was downloaded from https://unsplash.com/photos/4zxp5vlmvnI/.
The photo license is "Unsplash License" from https://unsplash.com/terms/.

---
## [custom-mt/evals](https://github.com/custom-mt/evals)@[38f40050e9...](https://github.com/custom-mt/evals/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Tuesday 2023-05-30 12:38:52 by dz-pika

Utility charge eval (#735)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Utility charge eval 

### Eval description
Given snippets from an electric utility bill, compute the per-kWh price
for electricity supply and delivery.

### What makes this a useful eval?
Utility bill parsing is needed to understand the breakdown of charges
and forecast future bills based on predicted usage. However, electricity
bills can be complex, with dozens of different line items that
contribute to the overall cost. This can be a headache for people
looking at their bill, as they just want to understand the per-kWh
prices for the supply/generation or delivery (e.g. transmission &
distribution) of their energy. Given incomplete but sufficient
information (e.g. simulating running OCR on a utility bill), this task
requires both the understanding and grouping of different terms and
charges under the delivery or supply, and basic arithmetic to compute
the total kWh and total charges in order to determine the per-kWh
prices. A human could fairly easily interpret the given data, but we
find that GPT3.5 (as well as GPT4 via the ChatGPT Plus) perform much
less accurately on the task (~.2).

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

All of the examples contain dummy values, but come from
terminology/formatting used in bills from many different utilities.

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
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nBasic Generation Service: 121
kWh X $0.069 per kWh = 8.35 \n Total Electric Supply Charges = 30.23 \n
Distribution Charge: 121 kWh X $0.041 per kWh = 4.96 \n Total Electric
Delivery Charges = 20.43"}], "ideal": "{'supply_cost_per_kwh': '0.25',
'delivery_cost_per_kwh': '0.17'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nGeneration Service (Supply) =
$34.89 \n Transmission Service = 7.24 \n Distribution Service = 4.96 \n
Meter Usage: 568 kWh"}], "ideal": "{'supply_cost_per_kwh': '0.061',
'delivery_cost_per_kwh': '0.022'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nElectricity Used (kWh) = 762 \n
Electricity Supply Charges 762 kWh at a cost of $100.25 \n Delivery
Service Charge: 762 kWh @ 0.008 = 6.096 \n Total Electric Delivery
Charges = 59.36"}], "ideal": "{'supply_cost_per_kwh': '0.13',
'delivery_cost_per_kwh': '0.078'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nSupply 423 kWh @ 11 cents / kWh
= 46.53 \n Total electricity supply charges $68.21 \n Delivery 423 kWh @
4 cents / kWh = 16.92 \n Total electricity delivery charges $17.43"}],
"ideal": "{'supply_cost_per_kwh': '0.16', 'delivery_cost_per_kwh':
'0.041'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nEnergy 152 @ 0.069 = 10.49 \n
Total Energy Charges = 14.25 \n Distribution 152 @ 0.041 = 6.23 \n Total
Electric Delivery Charges = 6.99"}], "ideal": "{'supply_cost_per_kwh':
'0.094', 'delivery_cost_per_kwh': '0.046'}"}
  ```
</details>

---
## [custom-mt/evals](https://github.com/custom-mt/evals)@[b2250e4117...](https://github.com/custom-mt/evals/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Tuesday 2023-05-30 12:38:52 by shivamd1810

Add General science reasoning: UPSC GS eval. (#641)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Hindi UPSC

### Eval description

[UPSC](https://en.wikipedia.org/wiki/Union_Public_Service_Commission) is
the organization responsible for conducting administrative service exams
in India. This evaluation set focuses on questions from the general
science paper of UPSC exams in Hindi. As a widely spoken language in
India, it is crucial to understand and answer questions accurately in
Hindi.



### What makes this a useful eval?

This evaluation set is useful for several reasons:

1. Real-world applicability: The questions are sourced from actual UPSC
exams, making the evaluation set practical and relevant for users
preparing for these exams.
2. Language diversity: By focusing on Hindi, this evaluation set helps
to improve the AI's understanding and response generation in a
non-English language, catering to a large user base.
3. Subject matter: General science is an important topic covered in the
UPSC exams, and evaluating the AI's performance in this area will help
identify areas for improvement.
4. Logical reasoning and inference: **UPSC questions are known for
requiring logical reasoning and the ability to infer connections between
multiple topics**. By including questions that demand such skills, this
evaluation set will help test and improve the AI's ability to handle
complex, multi-layered problems.


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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This evaluation set is valuable for improving the AI's understanding of
Hindi and its ability to provide accurate answers to general science
questions in the context of UPSC exams, a widely recognized and
important examination in India. Moreover, by incorporating questions
that test logical reasoning and inference skills, it will help enhance
the AI's capability to handle complex, multi-faceted problems that
require connections between multiple topics.

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
{"input": [{"role": "system", "content": "\n1. भारत की संसद के संदर्भ
में, निम्नलिखित कथनों पर विचार कीजिए:\n\n1- गैर-सरकारी विधेयक ऐसा विधेयक
है जो संसद् के ऐसे सदस्य द्वारा प्रस्तुत किया जाता है जो निर्वाचित नहीं
है किंतु भारत के राष्ट्रपति द्वारा नामनिर्दिष्ट है।\n2- हाल ही में, भारत
की संसद के इतिहास में पहली बार एक गैर-सरकारी विधेयक पारित किया गया
है।\n\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?\n\n(a) केवल 1\n(b)
केवल 2\n(c) 1 और 2 दोनों\n(d) न तो 1 और न ही 2\n\n, choose correct
answer:"}], "ideal": "d"}
{"input": [{"role": "system", "content": "2. ऋग्वेद-कालीन आर्यों और
सिन्धु घाटी के लोगों की संस्कृति के बीच अंतर के संबंध में, निम्नलिखित
कथनों में से कौन-सा/से सही है/हैं?\n1- ऋग्वेद-कालीन आर्य कवच और
शिरस्त्रण (हेलमेट) का उपयोग करते थे जबकि सिन्धु घाटी सभ्यता के लोगों में
इनके उपयोग का कोई साध्य नहीं मिलता।\n2- ऋग्वेद-कालीन आर्यों को स्वर्ण,
चाँदी और ताम्र का ज्ञान था जबकि सिन्धु घाटी के लोगों को कवल ताम्र और लोह
का ज्ञान था।\n3- ऋग्वेद-कालीन आर्यों ने घोड़े को पालतू बना लिया था जबकि
इस बात का कोई साक्ष्य नहीं है कि सिन्धु घाअी के लोग इस पशु को जानते
थे।\n\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिएः\n\n(a) केवल 1\n(b)
केवल 2 और 3\n(c) केवल 1 और 3\n(d) 1, 2 और 3\n\n, choose correct
answer:"}], "ideal": "c"}
{"input": [{"role": "system", "content": "3. ‘पूर्व अधिगम की मान्यता
स्कीम (रिकग्निशन ऑफ प्रायर लर्निंग स्कीम)’ का कभी-कभी समाचारों में किस
संदर्भ में उल्लेख किया जाता है?\n(a) निर्माण कार्य में लगे कर्मकारों के
पारंपरिक मार्गों से अर्जित कौशल का प्रमाणन\n(b) दूरस्थ अधिगम कार्यक्रमों
के लिए विश्वविद्यालयों में व्यक्तियों को पंजीकृत करना\n(c) सार्वजनिक
क्षेत्र के कुछ उपक्रमों में ग्रामीण और नगरीय निर्धन लोगों के लिए कुछ
कुशल कार्य आरक्षित करना\n(d) राष्ट्रीय कौशल विकास कार्यक्रम के अधीन
प्रशिक्षणार्थियों द्वारा अर्जित कौशल का प्रमाणन\n\n, choose correct
answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "4. पारिस्थितिक दृष्टिकोण से,
पूर्वी घाटों और पश्चिमी घाटों के बीच एक अच्छा सम्पर्क होने के रूप में
निम्नलिखित में से किसका महत्व अधिक है?\n(a) सत्यामंगलम बाघ आरक्षित
क्षेत्र (सत्यमंगलम टाइगर रिजर्व)\n(b) नल्लामला वन\n(c) नागरहोले
राष्ट्रीय उद्यान\n(d) शेषाचलम जीवमण्डल आरक्षित क्षेत्र (शेषाचलम
बायोस्फीयर रिजर्व)\n\n, choose correct answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "5. समाज में समानता के होने का
एक निहितार्थ यह है कि उसमें\n(a) विशेषाधिकारों का अभाव है\n(b) अवरोधों
का अभाव है\n(c) प्रतिस्पर्धा का अभाव है\n(d) विचारधारा का अभाव है\n\n,
choose correct answer:"}], "ideal": "a"}
  ```
</details>

---
## [custom-mt/evals](https://github.com/custom-mt/evals)@[9fdbd94c93...](https://github.com/custom-mt/evals/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Tuesday 2023-05-30 12:38:52 by Tong

Add Loss Logic Eval (#82)

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
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Loss Logic

### Eval description

A store bought a watermelon for $5 and sold it for a different price,
receiving counterfeit money in the transaction. They also had to give
change to the buyer. The net loss for the store varies based on the
specific details of the transaction.

### What makes this a useful eval?

* Tests comprehension and problem-solving skills: The scenarios provided
require the AI to understand and analyze the given information to
determine the net loss for the store.

* Addresses real-world situations: Counterfeit money transactions are a
real concern for businesses. This eval allows the AI to demonstrate its
understanding of financial transactions and the impact of counterfeit
money on a store's net loss.


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
- [ ] Include at least 100 high quality examples

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Involving the judgement of the truth or falsehood of real-world things,
which is a capability that GPT currently lacks.

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
{"input":[{"role":"system","content":"The store purchased a watermelon
for $5 and sold it for $7. Unfortunately, they received $10 in
counterfeit money after the transaction and had to give the buyer $3 in
change. What was the net loss for the store? Let's think step by
step:"}],"ideal":"Sure, let's break down the transaction step by step to
determine the net loss for the store: The store purchases a watermelon
for $5. The store sells the watermelon for $7. This would have been a $2
profit if the money received was real. The store receives $10 in
counterfeit money. This money is worthless, so the store doesn't
actually receive any value from the sale. The store gives the buyer $3
in change. This is a real loss, as the store loses $3 in real money.
Now, let's calculate the net loss: The store spent $5 to purchase the
watermelon. The store lost $3 when giving the buyer change. So the net
loss for the store is $5 (cost of watermelon) + $3 (change given) =
$8."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 but sold it for $4. Furthermore, they received $10 in counterfeit
money from the buyer and had to provide $6 in change. What was the net
loss for the store? Let's consider the process in
detail:"}],"ideal":"Sure, Let's think step by step: The store purchased
a watermelon for $5. The store sold the watermelon for $4, which means
they incurred a loss of $1 on the sale. The buyer gave the store $10 in
counterfeit money, which the store accepted during the transaction. The
store gave the buyer $6 in change. Since the store accepted $10 in
counterfeit money, they lost $10 in that transaction. The net loss for
the store is the sum of the loss on the watermelon sale and the loss
from accepting the counterfeit money, which is $1 + $10 = $11.
Therefore, the net loss for the store is $11."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for the same price of $5. However, they received $10 in
counterfeit money from the buyer and had to give the buyer $5 in change.
What was the net loss for the store? Let's consider the process step by
step:"}],"ideal":"Step 1: The store purchases a watermelon for $5.
Store's expenses: $5 Step 2: The store sells the watermelon for $5 but
receives $10 in counterfeit money. The counterfeit money has no value,
so the store effectively received nothing for the watermelon. Store's
revenue: $0 Step 3: The store gives the buyer $5 in change. Since the
money given in change is real, this is an additional expense for the
store. Store's expenses: $5 (watermelon) + $5 (change) = $10 Step 4:
Calculate the net loss. Net loss = Expenses - Revenue Net loss = $10
(expenses) - $0 (revenue) Net loss = $10 The store's net loss for this
transaction is $10."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for $7. Regrettably, they received $7 in counterfeit
money from the buyer after the transaction. What was the net loss for
the store? Let's consider the process step by step:"}],"ideal":"Sure,
let's break down the transaction step by step: The store purchased a
watermelon for $5. They sold the watermelon for $7, but received
counterfeit money. To determine the net loss, let's analyze the costs
and the revenue: Costs: The store spent $5 on the watermelon. Revenue:
The store received $7 in counterfeit money, which has no value, so their
revenue is $0. Net loss: To calculate the net loss, subtract the revenue
from the costs: $5 (costs) - $0 (revenue) = $5. So, the net loss for the
store is $5."}
{"input":[{"role":"system","content":"The store was given a
complimentary watermelon, which they then sold for $7. Regrettably,
following the transaction, they received $10 in fake money and had to
provide the buyer with $3 in change. Let's consider the following steps
in determining the store's net loss:"}],"ideal":"To determine the
store's net loss, we can consider the following steps: Assess the value
of the complimentary watermelon: Since the watermelon was given to the
store for free, it didn't cost them anything. Therefore, the store's
initial cost for the watermelon is $0. Calculate the revenue from
selling the watermelon: The store sold the watermelon for $7. However,
they received $10 in fake money, which has no value, so the actual
revenue is $0. Determine the cost of the change provided: Since the
store provided the buyer with $3 in change, this is an additional cost
to the store. Calculate the net loss: Subtract the revenue (Step 2) from
the sum of the initial cost (Step 1) and the cost of the change (Step
3). In this case: Net loss = (Initial cost + Cost of change) - Revenue
Net loss = ($0 + $3) - $0 Net loss = $3 The store's net loss from this
transaction is $3."}
  ```
</details>

---
## [moeen-movahednia/evals](https://github.com/moeen-movahednia/evals)@[8e276ea460...](https://github.com/moeen-movahednia/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Tuesday 2023-05-30 12:44:46 by steven-luabase

Eval: Probability Questions Sourced From Actuarial Exam P and University Statistics Courses (#263)

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
Probability Questions

### Eval description

Tests the model's ability to understand answer probability questions.
Questions are sourced from Society of Actuaries Exam P sample questions
and practice problems/exams from statistics classes at MIT, UPenn,
California State University, Durham University, University of
Connecticut, and other sources. The full list of questions and sources
(in the same order as in the `.jsonl` files) can be found in this Google
[sheet](https://docs.google.com/spreadsheets/d/1TU_4VPhIce9JtLV5gLy619WNibVjiWB-dtiwqkBtCrU/edit?usp=sharing)

### What makes this a useful eval?

Test the model's ability to understand worded probability questions,
bring in concepts such as probability distributions, and then reason
through a correct answer.

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

Using the `match` grading criteria, GPT3.5-turbo got an accuracy score
of `{'accuracy': 0.07}`

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
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A pair of fair, standard dice are rolled. What is the
probability the sum of the dice is 5"}], "ideal": ["0.1111"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "An airplane is built to be able to fly on one engine. If the
plane's two engines operate independently, and each has a 1% chance of
failing in any given four-hour flight, what is the chance the plane will
fail to complete a four-hour flight to Oklahoma due to engine
failure?"}], "ideal": ["0.0001"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A 1-inch-diameter coin is thrown on a table covered with a
grid of lines two inches apart. What is the probability the coin lands
in a square without touching any of the lines of the grid?"}], "ideal":
["0.2500"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 50 students in a certain class, 5 speak French. Two
students of the class will be selected at random. Which of the following
is closest to the probability that neither of the students selected will
speak French?"}], "ideal": ["0.8100"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 10 marbles in a box, 2 are green. A person will
select 2 marbles simultaneously and at random from the box. What is the
probability that neither of the marbles selected will be green?"}],
"ideal": ["0.6222"]}
  ```
</details>

---
## [moeen-movahednia/evals](https://github.com/moeen-movahednia/evals)@[33484c8341...](https://github.com/moeen-movahednia/evals/commit/33484c83416c30733359d5c4dcb9a61f91cab8a6)
#### Tuesday 2023-05-30 12:44:46 by emu1729

Added AIME eval (#293)

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
AIME-Evaluation

### Eval description

This eval evaluates GPT on some selected AIME (American Invitational
Mathematics Examination) problems. This is a selective and prestigious
mathematical examination for high schoolers. All questions are selected
from the 2001 and 2002 AIME I and II examinations.

### What makes this a useful eval?

This evaluation combines math and logical evaluation and is designed to
be quite challenging. The model must first understand the math question
asked and then perform the math equations needed to come up with a
reasonable solution.

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

Our eval was designed to include both math and logical reasoning and is
quite challenging. This is a level above the AMC10 examination.

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
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Find the sum of all positive
two-digit integers that are divisible by each of their
digits."}],"ideal":"630"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A fair die is rolled four
times. The probability that each of the final three rolls is at least as
large as the roll preceding it may be expressed in the form m\/n, where
m and n are relatively prime positive integers. Find m +
n"}],"ideal":"079"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A sphere is inscribed in the
tetrahedron whose vertices are A = (6, 0, 0), B = (0, 4, 0), C = (0, 0,
2), and D = (0, 0, 0).The radius of the sphere is m \/ n, where m and n
are relatively prime positive integers. Find m + n."}],"ideal":"005"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A mail carrier delivers mail
to the nineteen houses on the east side of Elm Street. The carrier
notices that no two adjacent houses ever get mail on the same day, but
that there are never more than two houses in a row that get no mail on
the same day. How many different patterns of mail delivery are
possible?"}],"ideal":"351"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"The numbers 1, 2, 3, 4, 5, 6,
7, and 8 are randomly written on the faces of a regular octahedron so
that each face contains a different number. The probability that no two
consecutive numbers, where 8 and 1 are considered to be consecutive, are
written on faces that share an edge is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"085"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Let N be the largest positive
integer with the following property: reading from left to right, each
pair of consecutive digits of N forms a perfect square. What are the
leftmost three digits of N?"}],"ideal":"816"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each of the 2001 students at a
high school studies either Spanish or French, and some study both. The
number who study Spanish is between 80 percent and 85 percent of the
school population, and the number who study French is between 30 percent
and 40 percent. Let m be the smallest number of students who could study
both languages, and let M be the largest number of students who could
study both languages. Find M-m."}],"ideal":"298"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A set of positive numbers has
the 'triangle-property' if it has three distinct elements that are the
lengths of the sides of a triangle whose area is positive. Consider sets
{4, 5, 6, ..., n} of consecutive positive integers, all of whose
ten-element subsets have the triangle property. What is the largest
possible value of n?"}],"ideal":"253"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each unit square of a 3-by-3
unit-square grid is to be colored either blue or red. For each square,
either color is equally likely to be used. The probability of obtaining
a grid that does not have a 2-by-2 red square is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"929"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Given that x and y are both
integers between 100 and 999, inclusive; y is the number formed by
reversing the digits of x; and z=|x-y|. How many distinct values of z
are possible?"}],"ideal":"009"}

  ```
</details>

---------

Co-authored-by: Emily Mu <emilymu@30-10-85.wireless.csail.mit.edu>
Co-authored-by: Emily Mu <emilymu@30-10-24.wireless.csail.mit.edu>

---
## [moeen-movahednia/evals](https://github.com/moeen-movahednia/evals)@[8f8632ec55...](https://github.com/moeen-movahednia/evals/commit/8f8632ec55ee1f9704fe34225e1bce0cd999a8b1)
#### Tuesday 2023-05-30 12:44:46 by Oshan Upreti

Nepali song singer recognition (#892)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Nepali Song Singer

### Eval description

It tests the ability to understand Nepali language from given English
Transliteration phrase which is provided by user as a song title, and
checks the singer/band of the song. This eval has the accuracy of zero.
And, I still created this eval PR because I get the wrong answers every
time I ask, and I don't think that should be the case. It might not be
something that needs to be done immediately, but in a near future you
would expect your AI to answer it correctly.

### What makes this a useful eval?

If it can do for any English songs in the database, it should be able to
do for other languages as well. This is just a pattern I found it in my
mother tongue, but there might be different other languages where this
is happening as well, and it can be other things as well not just the
song title recognition.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Sayad Timro Bato Ma"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Timi Lai Dekhera"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Aaja maan udhera bhagchha"}],
"ideal": "Udit Narayan"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Kaha Hola Ghar Bara"}], "ideal":
"Karma"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Khaseka Tara"}], "ideal":
"Albatross"}
  ```
</details>

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[2901313821...](https://github.com/Jolly-66/tgstation/commit/290131382174cfc7bae107824288060d5976d91f)
#### Tuesday 2023-05-30 13:05:43 by Ghom

Adds a eye-dropper right-click function to the painting canvas. (#75571)

## About The Pull Request
Having used the painting UI to kill some time during long rounds for a
decent chunk of the past year, the need of a quicker and less tedious
way to fix a misclick or mistake like drawing over the wrong pixel has
become clear to me, as well as getting some feedback on the palette
component I made last year.

As the title suggests, this PR adds an eye-dropper function to the
canvas. Right-Click a pixel on the canvas, and the painting tool will
copy its color. Simple as, works on both finished and unfinished
paintings.

As a bonus, you can also right-click one of those selectable
white/colored squares on the color scheme near the bottom of the UI (if
using spraycan/palette) to change its color without having to go back to
main game window and a radial menu.

EDIT: With the tooltip added to the UI, I can say it's ready.

## Why It's Good For The Game
This PR aims to add better options to change colors on the go and
improve the user experience on the painting UI.

## Changelog

:cl:
qol: Adds a eye-dropper-like right-click function to the painting canvas
UI. Right-Click a pixel on the canvas while holding a painting tool to
have it copy its color.
qol: Also adds a right-click function to the color palette at the bottom
of the UI to allow users to set its colors without having to alternate
between the game window and the UI.
qol: Lastly, a tooltip has been added near the top-left corner of the
same UI to let players know of these features.
/:cl:

---
## [ca2/app](https://github.com/ca2/app)@[70c2f35332...](https://github.com/ca2/app/commit/70c2f3533248ceeb43befbf404072dff0463b3a9)
#### Tuesday 2023-05-30 13:10:15 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS Ventura : day 27 ] ca2 Stabilization and ca2 Store (continuous integration and deployment)
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
## [Tridu33/LeetCodeWars](https://github.com/Tridu33/LeetCodeWars)@[4f97b67e68...](https://github.com/Tridu33/LeetCodeWars/commit/4f97b67e688446a187aab6cdee722c245cdbfa5d)
#### Tuesday 2023-05-30 15:54:50 by tridu33

Talk of Tech Innovation is Bullshit. Shut Up and Get the shit Done. by Linus Torvalds

---
## [jratt0/forks__git_git](https://github.com/jratt0/forks__git_git)@[07f91e5e79...](https://github.com/jratt0/forks__git_git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Tuesday 2023-05-30 15:58:50 by Jeff King

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
## [openai/evals](https://github.com/openai/evals)@[3d9de9a624...](https://github.com/openai/evals/commit/3d9de9a62411f9e6a999e96ce8f07eebf0e8c121)
#### Tuesday 2023-05-30 17:06:03 by dyar-al-ashtari

Eval Norwegian lexicon (#1044)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
`norwegian-lexicon`

### Eval description

This eval uses valid Norwegian words taken from the dictionary and
assesses whether GPT can recognize them as valid.

### What makes this a useful eval?

The Norwegian language is simple yet complicated at the same time. There
are a lot of words that are valid Norwegian words that do not get
recognized anymore. An AI should be able to identify these words with
precision. All of the words used in the samples are valid Norwegian
words and can be found in the dictionary. After assessing GPT-4 (through
the playground) and GPT-3.5 -- it failed to recognize most of the words.
Some of the words would return positive during some evals. Other times
it wouldn't recognize them. After asking GPT why it is not a valid word,
it would apologize and fix its mistake.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Skarpne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Bløtne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Hovedantall"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Klenge"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Blankolov"}],"ideal":"Y"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[6a37c9b51b...](https://github.com/openai/evals/commit/6a37c9b51b48a2f735898846cfb08b37cbd63179)
#### Tuesday 2023-05-30 17:07:38 by Aaron Goldsmith

[eval] 3x3 Game Of Life  (#345)

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
GOL

### Eval description

Determine the next state of a 3x3 Game of Life Board. 

### What makes this a useful eval?

Spacial reasoning

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
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n0 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 0\n\n0 1
0\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n1 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n1 0
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n1 1
1\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n0 0
0\n\n1 0 1"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n0 1
1\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 1\n\n0 1
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 0\n\n0 0
0\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 0 0\n\n1 1
0\n\n0 0 0"]}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[b91292c803...](https://github.com/openai/evals/commit/b91292c803af2bdadeec3853ab03514b73310109)
#### Tuesday 2023-05-30 17:11:33 by Zyenith

Add Eval: Internal Representations via Counting (#1006)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
Internal representations via counting

### Eval description

Using series of logical questions that require multiple (simple)
manipulations of numbers to get the ideal answer. These are basic tasks
that should be doable by an LLM, but require several steps of internal
"thought" to get right.

### What makes this a useful eval?

Situations with number manipulation with multiple steps are prevalent
anywhere in the modern world. Testing the internal representation of the
LLM can provide other insights on how well its "mind" processes
information.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval is capable of providing insight into the LLM's internal
representation of objects versus answering fact-based questions or
straightforward complex logic puzzles.

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

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"Roger and Emily are in a room.
Roger puts a cat in an empty box while Emily is in the room. They both
leave, and Emily returns and puts a turtle in the box as well. How many
items does Roger think are in the box?"}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are four darts already on a
dart board. Bob throws one dart at the dartboard, and it lands. Alice
throws two darts, and one misses but one hits the dartboard. How many
darts are on the dartboard?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"A bakery sold 25 cakes in the
morning and 17 cakes in the afternoon. The day after, they sold 15 more
cakes. How many cakes did they sell on the second day?"}],"ideal":"15"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are six blue birds and three
red birds sitting on a tree. Two blue birds fly away, and one red bird
flies away. How many birds are left on the tree?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"John has double the amount of
pencils than Sarah, and Sarah has as many pencils as Mark. Mark has 2
pencils. How many pencils does John have?"}],"ideal":"4"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[e116ede848...](https://github.com/openai/evals/commit/e116ede848957eff8e76b5d8463ed5291163a28f)
#### Tuesday 2023-05-30 17:11:47 by Wesley Barlow

Add eval: rhetorical-devices (#1005)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
rhetorical-devices

### Eval description

Evaluates model's ability to select the most specific rhetorical
modification of a sentence from a multiple choice with a large number of
nuanced rhetorical devices.

### What makes this a useful eval?

Useful for using LLMs to write novels and generate consistent/parametric
authorial tone.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL She likes to listen to the winds. MODIFIED
She swoons at such sweet gales. Answer in the format (x) Rhetorical"}],
"ideal": "(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL The rock was very large. MODIFIED The rock
was remarkably raised. Answer in the format (x) Rhetorical"}], "ideal":
"(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Visionary dreams elevate me at night.
MODIFIED Visionary reminitions elevate self resting in lightlessness.
Answer in the format (x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Once, I thought I had lost her pet.
MODIFIED Once, dunce — thought I lost Juliet's pet. Answer in the format
(x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Do you want to understand research on
artificial general intelligence? MODIFIED Don't you want to investigate
artifacts of artificial general intelligence? Answer in the format (x)
Rhetorical"}], "ideal": "(c) Consonance"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[6151d9fe86...](https://github.com/openai/evals/commit/6151d9fe867a4106dab49fe6f06e762e939abfbf)
#### Tuesday 2023-05-30 17:15:05 by πisk0mate

eval: korean spelling (#699)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑

### Eval name
korean_spellings

### Eval description
Evaluates whether a given Korean word is spelled correctly or not with a
simple "Yes" or "No".

### What makes this a useful eval?
The samples are chosen from a set of frequently misspelled Korean words.
The words are specifically chosen because they are some of the most
frequently misspelled even by Korean native speakers. They are also
frequently used in day to day life.

The first 50 are the frequent misspelling of the word, and the last 50
are the same words but correctly spelled.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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
{"input":[{"role":"system","content":"You will be prompted with a single
word. Is this word correctly spelled in the Korean language? Answer with
exactly one of the following: Yes or No. Don't add anything else to the
response."},{"role":"user","content":"설레임"}],"ideal":"No"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Is this word correctly spelled in the Korean language? Answer with
exactly one of the following: Yes or No. Don't add anything else to the
response."},{"role":"user","content":"단언컨데"}],"ideal":"No"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Is this word correctly spelled in the Korean language? Answer with
exactly one of the following: Yes or No. Don't add anything else to the
response."},{"role":"user","content":"되물림"}],"ideal":"No"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Is this word correctly spelled in the Korean language? Answer with
exactly one of the following: Yes or No. Don't add anything else to the
response."},{"role":"user","content":"설렘"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Is this word correctly spelled in the Korean language? Answer with
exactly one of the following: Yes or No. Don't add anything else to the
response."},{"role":"user","content":"단언컨대"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Is this word correctly spelled in the Korean language? Answer with
exactly one of the following: Yes or No. Don't add anything else to the
response."},{"role":"user","content":"대물림"}],"ideal":"Yes"}
  ```
</details>

---
## [Sagura091/rccst-lib](https://github.com/Sagura091/rccst-lib)@[7eca0c61cf...](https://github.com/Sagura091/rccst-lib/commit/7eca0c61cf4f3d15583b2e8106a3ea7eca09cf68)
#### Tuesday 2023-05-30 17:20:06 by sagura091

I HAte my life.... Love programming but I made my life miserable....

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[835952ccf4...](https://github.com/Pickle-Coding/tgstation/commit/835952ccf42af58db7238a572d7df6a9b8b2afd7)
#### Tuesday 2023-05-30 19:24:33 by MrMelbert

Drunk slurring scales based on how drunk you are (#75459)

## About The Pull Request

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...


![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11


![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

## Why It's Good For The Game

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

## Changelog

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

---
## [pan93412/evals](https://github.com/pan93412/evals)@[93e7dd53d1...](https://github.com/pan93412/evals/commit/93e7dd53d11816c7051be009046b5990944a4dae)
#### Tuesday 2023-05-30 19:50:08 by fc-friday

Evaluate simple visual understanding with simple descriptions, shapes and navigation (#977)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
simple-visual-understanding

### Eval description

This evaluation tests whether the model is capable of emerging very 
simple visual representations of the world as well as understanding
simple
concepts used in everyday language like U turn, L shape etc.  


### What makes this a useful eval?

Human reasoning and intelligence are very tied to visual representations
we build of the world. In the quest to better understand and communicate
with us, it is important for an AI to grasp the same models of the world
we have. Common everyday language refers to things like U turn, L shape
etc
so assessing whether the model actually understands these shapes is
important.

It is of course understandable that an LLM that has never actually seen 
anything can't really understand visual aspects of our world but these 
very simple tests try to assess whether a model has been able to emerge 
such capabilities from written language.

It is interesting to see that GPT actually passes a few tests,
indicating
that some rudimentary visual representation has already emerged. 
Nevertheless, it fails most of the tests indicating there's still work
to be done.

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
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

These evals have been built from scratch to minimize the possibility of
previous training data helping the model to solve the
problems without actually understanding the meaning of them.

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

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system", "content": "Please answer the following
question using only a single letter on your reply."}, {"role": "user",
"content": "There's a building with 5 floors and 5 windows per floor. At
night, every third window of every floor is lit and the others are off.
Which letter of the alphabet do the lit windows look like?"}], "ideal":
"I"}
{"input": [{"role": "system", "content": "Please answer the following
question using only 'Left' or 'Right' words in a JSON list format"},
{"role": "user", "content": "A person stands in front of the entrance to
a 'U' shaped corridor. The first turn is to the right. At the end of the
corridor there's an exit. Which turns does she have to make to reach the
exit?"}], "ideal": ["[\"Right\",\"Right\"]", "[\"Right\", \"Right\"]"]}
{"input": [{"role": "system", "content": "Please answer the following
question using only a single word on your reply."}, {"role": "user",
"content": "There are 5 men side by side. On top of those men's
shoulders, 4 men stand. On top of those 4 men's shoulders, 3 men stand
and so on. What 2D geometric shape do they form?"}], "ideal":
"Triangle"}
{"input": [{"role": "system", "content": "Please answer the following
question using only a single letter on your reply."}, {"role": "user",
"content": "At the half time break, a large group of cheerleaders enter
a football field from the side. 20 of them form a row along the east 40
yard line. 20 others form a row along the west 40 yard line. 20 more
form a horizontal row connecting the previous 2 rows by crossing the
center field mark. Looking from above, which letter of the alphabet do
they form?"}], "ideal": "H"}
{"input": [{"role": "system", "content": "Please answer the following
question using only 'Left' or 'Right' words in a JSON list format"},
{"role": "user", "content": "There's a maze formed by 5 concentric
circles. The innermost circle has a door to the north and all the other
circles have doors at 90 degrees to the right of the immediately inner
circle. A person stands inside the innermost circle, facing the door to
the north. Which turns does she have to make to reach the exit?"}],
"ideal": ["[\"Right\", \"Right\", \"Right\", \"Right\"]",
"[\"Right\",\"Right\",\"Right\",\"Right\"]"]}
{"input": [{"role": "system", "content": "Please answer the following
question using only a single letter on your reply."}, {"role": "user",
"content": "There's a square parking lot with 5 parking slots on each
side. There are 5 cars parked on the north side, 5 cars parked on the
west side and 5 cars parked on the south side. Looking from above, which
letter of the alphabet do the cars form?"}], "ideal": "C"}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[c822671b9b...](https://github.com/pan93412/evals/commit/c822671b9bc31116135ac5e776291dc7fd0f1f6d)
#### Tuesday 2023-05-30 19:50:08 by James

Eval: Seating Arrangement (#982)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
Seating Arrangements

### Eval description

An array of seating arrangement constraints, each with 2 solutions.
Examining the models spatial reasoning abilities.

### What makes this a useful eval?

Assists with evaluating simple spatial reasoning with a limited number
of solutions to a constraint problem. I created a solver to ensure that
each puzzle only has 2 solutions and a limited number of variables. A
human should be able to solve these extremely easily even without
writing the names down on pen and paper.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Daniel and Sophia are enemies, Sophia and
Charlotte are enemies, Olivia and Daniel are friends, Daniel and
Benjamin are friends, Benjamin and Charlotte are friends."}], "ideal":
["Charlotte | Benjamin | Daniel | Olivia | Sophia", "Sophia | Olivia |
Daniel | Benjamin | Charlotte"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Eleanor is a loner, Samuel and Christopher are
enemies, Emma is a loner, Samuel and Eleanor are enemies."}], "ideal":
["Eleanor | Christopher | Scarlett | Samuel | Emma", "Emma | Samuel |
Scarlett | Christopher | Eleanor"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Nathan and Samuel are enemies, David and Samuel
are friends, Olivia and Samuel are friends, Olivia is a loner, David and
Victoria are friends."}], "ideal": ["Nathan | Victoria | David | Samuel
| Olivia", "Olivia | Samuel | David | Victoria | Nathan"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Olivia and Eleanor are enemies, Grace and Olivia
are friends, Eleanor and Alexander are enemies, Scarlett and Olivia are
friends, Grace and Eleanor are enemies."}], "ideal": ["Eleanor |
Scarlett | Olivia | Grace | Alexander", "Alexander | Grace | Olivia |
Scarlett | Eleanor"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Ava and Christopher are friends, Isaac and
Benjamin are enemies, David and Ava are friends, Christopher and
Benjamin are enemies."}], "ideal": ["Benjamin | David | Ava |
Christopher | Isaac", "Isaac | Christopher | Ava | David | Benjamin"]}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[d80eb3a01e...](https://github.com/pan93412/evals/commit/d80eb3a01e9a217114f57011b7cd2c9a1a3aac99)
#### Tuesday 2023-05-30 19:50:08 by erauner12

[Eval] Resolving ambiguous sentences (#889)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Ambiguous Sentences (`ambiguous-sentences`)

### Eval description
Resolves ambiguous questions of sentence pairs. Examples are taken from
the Winograd Schema Challenge. The challenge involves a pair of
sentences that differ in only one or two words, and the machine is
required to determine the correct meaning of a pronoun in the sentence.

### What makes this a useful eval?
It is pointed out that GPT is still often thrown off by these types of
questions, providing one answer upon the first request, and it often
changes if the request is regenerated with a different result
`(0.7666666666666667)`.

I think it is worth including as an example to others viewing the
repository who are trying to understand what kind of logic GPT tends to
fail with, even if some of this data has already been trained on.
Provides a place to insert similar types of ambiguous sentence/question
pairs as they are discovered.

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
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)
- Handpicked specific prompts from the challenge that I have noticed
have mixed results consistently.
- Ensure that matching prompts are next to each other for easy
comparison for humans in the `.jsonl` file.

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
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The city councilmen refused the
demonstrators a permit because they feared violence.. Who feared
violence?"}],"ideal":"city councilmen"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The city councilmen refused the
demonstrators a permit because they advocated violence.. Who advocated
violence?"}],"ideal":"demonstrators"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The lawyer asked the witness a
question, but he was reluctant to answer it.. Who was reluctant to
answer the question?"}],"ideal":"witness"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The lawyer asked the witness a
question, but he was reluctant to repeat it.. Who was reluctant to
repeat the question?"}],"ideal":"lawyer"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Tom threw his schoolbag down to
Ray after he reached the top of the stairs.. Who reached the top of the
stairs?"}],"ideal":"Tom"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Tom threw his schoolbag down to
Ray after he reached the bottom of the stairs.. Who reached the bottom
of the stairs?"}],"ideal":"Ray"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Although they ran at about the
same speed, Sue beat Sally because she had such a good start. Who had a
good start?"}],"ideal":"Sue"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Although they ran at about the
same speed, Sue beat Sally because she had such a bad start. Who had a
bad start?"}],"ideal":"Sally"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Frank was upset with Tom because
the toaster he had bought from him didn't work.. Who had bought from the
toaster?"}],"ideal":"Frank"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Frank was upset with Tom because
the toaster he had sold to him didn't work.. Who had sold to the
toaster?"}],"ideal":"Tom"}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[423895860c...](https://github.com/pan93412/evals/commit/423895860c47c405018a5a59e15ead8f52fba615)
#### Tuesday 2023-05-30 19:50:08 by Stephen Blum

[Evals] Add Nutrition Facts (#853)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
nutrition

### Eval description

Test the model's nutritional accuracy, providing machine parsable and
accurate responses using metric notation when asked about specific
values.

### What makes this a useful eval?

The task of populating a spreadsheet with information based on facts
from adjacent cells that contain inquiries and details is currently a
manual task and can be time consuming and prone to errors. Using a
natural language parser and language model like GPT can automate the
process and save time. Filling in missing details from adjacent
spreadsheet cells containing natural language would be useful in
automating the process of populating a spreadsheet with data based on
nutritional facts and inventory in our case. This would save time and
effort for staff, who would otherwise have to manually enter data.

In the case where we were assisting one of our customers, Google
Spreadsheets was used as the tool to store and manage the data related
to nutritional facts and inventory. The idea was to use a natural
language parser and language model like GPT to extract the intention of
a spreadsheet cell and provide the following cell with the desired
information based on the data stored in Google Spreadsheets.

However, the accuracy of the information provided by the language model
were not reliable, and the desired results could not be achieved. We had
to approach the problem with a combination of manual and scripting. More
work needs to be done to improve the accuracy and reliability of
language models like GPT when integrated with tools like Google
Spreadsheets.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

The model mostly answers in the desired format, yet usually got it
wrong.

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
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin c is in 100 grams of
avocado?"}], "ideal": "10.0mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b5 is in 100 grams of
banana?"}], "ideal": "0.3mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b6 is in 100 grams of
banana?"}], "ideal": "0.4mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin c is in 100 grams of
banana?"}], "ideal": "8.7mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b2 is in 100 grams of
plum?"}], "ideal": "0.1mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b3 is in 100 grams of
plum?"}], "ideal": "0.4mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b6 is in 100 grams of
pear?"}], "ideal": "0.1mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin c is in 100 grams of
pear?"}], "ideal": "4.3mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin d is in 100 grams of
avocado?"}], "ideal": "0.0mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin e is in 100 grams of
avocado?"}], "ideal": "2.1mg"}
  ```
</details>

---
## [Rohail33/Realking_xiaomi_xaga](https://github.com/Rohail33/Realking_xiaomi_xaga)@[0bdb40acb9...](https://github.com/Rohail33/Realking_xiaomi_xaga/commit/0bdb40acb9d085b7b03fb40ec6dbd1472043be24)
#### Tuesday 2023-05-30 20:29:12 by Wang Han

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
## [kanshe7/kanshe7](https://github.com/kanshe7/kanshe7)@[6c36cfa28b...](https://github.com/kanshe7/kanshe7/commit/6c36cfa28b12ab74e3e0914c0f7bf9a2c7aa1627)
#### Tuesday 2023-05-30 20:33:29 by kanshe7

Update README.md

Project Name
Bugema University Chatbot

Description
The Bugema University Chatbot is an intelligent virtual assistant designed to provide information and support to students, faculty, and visitors of Bugema University. It leverages natural language processing and machine learning techniques to understand user queries and provide accurate responses.

Features
FAQ Support: The chatbot is trained with a set of frequently asked questions about Bugema University, including programs, admissions, tuition fees, scholarships, student life, facilities, and more.
Customized Responses: The chatbot is designed to provide personalized and relevant answers based on the user's input, ensuring a more engaging and interactive experience.
Academic Calendar: The chatbot can provide information about the academic calendar, including semester start and end dates, registration periods, examination periods, and breaks.
User-friendly Interface: The chatbot interface is intuitive and easy to use, allowing users to type their queries and receive instant responses.
Installation
To run the Bugema University Chatbot locally, follow these steps:

Clone the repository: git clone <repository-url>
Install the required dependencies: pip install -r requirements.txt
Run the application: python app.py
Access the chatbot in your web browser: http://localhost:5000
Contribution
Contributions are welcome! If you find any issues or have suggestions for improvement, please submit a pull request or open an issue in the repository. Let's work together to enhance the Bugema University Chatbot and make it even more helpful for the Bugema University community.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

---
## [francis-codex/WordPair-Generator-App](https://github.com/francis-codex/WordPair-Generator-App)@[e2e8f42360...](https://github.com/francis-codex/WordPair-Generator-App/commit/e2e8f42360a17400556cbd45853ad3307b051062)
#### Tuesday 2023-05-30 21:11:22 by francis-codex

Update README.md

The WordPair Generator app is a unique and innovative tool designed to inspire creativity and generate new ideas by combining two random words to create interesting word pairs. It harnesses the power of artificial intelligence and natural language processing to provide users with an endless stream of unexpected word combinations.

The app's interface is user-friendly and intuitive, allowing users to easily navigate and interact with the various features. Upon launching the app, users are greeted with a clean and visually appealing design, creating an enjoyable experience.

The WordPair Generator app offers multiple modes to suit different creative needs. In the "Quick Pair" mode, users can simply tap a button to instantly generate a random word pair. This mode is perfect for spontaneous brainstorming sessions or when a quick burst of inspiration is needed.

For users looking for more specific word combinations, the app provides a "Custom Pair" mode. In this mode, users can input their own keywords or select from predefined categories to narrow down the type of words they want to generate. For example, users may choose categories such as "Nature," "Technology," or "Food" to focus the word pairings on those specific themes.

The app also features a "Favorites" section where users can save and revisit their favorite word pairs. This allows users to build a personalized collection of creative sparks that they can refer to later when working on writing projects, brainstorming ideas for business names, or simply for the joy of discovering intriguing word combinations.

Moreover, the WordPair Generator app offers additional features to enhance the creative process. It includes a sharing option that enables users to share their favorite word pairs directly with friends or colleagues via social media platforms or messaging apps. This facilitates collaboration and sparks conversations around the generated ideas.

With regular updates and expansions to its word database, the WordPair Generator app ensures a constant influx of fresh and diverse word pairings, keeping users engaged and continuously inspired.

In summary, the WordPair Generator app is a dynamic tool that utilizes AI to generate unique word combinations, fostering creativity, and offering a valuable resource for writers, marketers, designers, and anyone seeking inspiration for their projects.

---
## [ZveronHSE/backend_new](https://github.com/ZveronHSE/backend_new)@[45f91821ca...](https://github.com/ZveronHSE/backend_new/commit/45f91821caf5bbf3a4b8533b6e70340eb9d8d2a4)
#### Tuesday 2023-05-30 21:48:22 by Sofia Terekhova

[ZV-412] Add tracing  (#117)

* [ZV-412] fix mistake and change to library version tag

[ZV-412] add platform to apigateway

[ZV-412] fix library

[ZV-412] add settings to logback and add new settigns in application.yml

[ZV-412] edit tracing library interceptor

[ZV-412] server interceptors

[ZV-412] full correct working client tracing

[ZV-412] correct working client tracing interceptor

[ZV-412] add jaeger configuration for specialist service

[ZV-412] add instance

* [ZV-412] fix tests

* [ZV-412] fix test x2

* [ZV-412] fix test x3

* [ZV-412] fix test x4

* [ZV-412] fix test x5 fuck you

* [ZV-412] fix test x66666 fuck you

---------

Co-authored-by: sofia.terekhova <sofiamaria.terekho@aliexpress.ru>

---
## [hackworthltd/primer-app](https://github.com/hackworthltd/primer-app)@[eb93f85743...](https://github.com/hackworthltd/primer-app/commit/eb93f85743fee0bd3397eaff1e4c761a96527bd2)
#### Tuesday 2023-05-30 22:40:19 by George Thomas

feat: scroll to def when its name is clicked in the sidebar

This approach is a bit hacky, but we couldn't think of a better way to
do this without wrapping large chunks of `App` in a
`ReactFlowProvider`, which we weren't crazy about. (However, that
approach may become less objectionable/problematic once we've broken
the live eval and definition list out of the sidebar.)

We'd prefer to pass the def's `GlobalName` to the `TreeReactFlow`
callback, but this would require quite a bit of reworking of the
sidebar's definition list. As that component is probably not long for
this world, we'll defer this work until later when we figure out
exactly where the definition list will go.

Limitations of this current implementation:

* It doesn't change the zoom level and technically only focuses on the
definition's root node, without trying to fit its entire tree on the
screen. We should probably support this, perhaps through some sort of
double-click/double-touch mechanism.

* It only works for definitions the student has defined in the current
module. It doesn't work for imported definitions, and it doesn't work
for typedefs, as those aren't yet rendered on the canvas. However,
this feature should be relatively easy to adapt to student-defined
typedefs once they're represented as trees on the canvas.

* It's not yet implemented in the live eval view. It may be useful for
fitting the tree on the screen when we switch which definition is
being evaluated, but there may be easier/better ways to do this that
don't involve the convoluted callback mechanism we've had to implement
here, because all of the controls we need are in a monolithic
component. We'll explore this in subsequent work, in any case.

Signed-off-by: Drew Hess <src@drewhess.com>

---
## [gered/ggdt](https://github.com/gered/ggdt)@[ad8d1f9ae3...](https://github.com/gered/ggdt/commit/ad8d1f9ae379f5b1da4c73eeceb0fcf1cc11149a)
#### Tuesday 2023-05-30 22:52:48 by gered

i have no idea why this decided to throw a compile error now? wtf?

my wild-ass guess is this is somehow related to the serde dependency
being included now, but who the fuck knows. what a joke.

---
## [BeebBeebBoob/SKYRAT-SS220](https://github.com/BeebBeebBoob/SKYRAT-SS220)@[52eb909f42...](https://github.com/BeebBeebBoob/SKYRAT-SS220/commit/52eb909f423900340814843d3223a7f3205add35)
#### Tuesday 2023-05-30 22:53:11 by Tom

Makes Hell Microwaves Not Use Power (#67413) (#21210)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

Co-authored-by: san7890 <the@san7890.com>

---
## [wolfd/streamlit](https://github.com/wolfd/streamlit)@[596bff9128...](https://github.com/wolfd/streamlit/commit/596bff9128a7d48104fd566a512c50f2b4d6f38d)
#### Tuesday 2023-05-30 23:26:30 by Danny Wolf

Upgrade react-range to fix memory usage of sliders

As mentioned in
https://blog.streamlit.io/six-tips-for-improving-your-streamlit-app-performance/
memory usage struggles in the browser if you have large ranges:

> Due to implementation details, high-cardinality sliders don't suffer
> from the serialization and network transfer delays mentioned earlier,
> but they will still lead to a poor user experience (who needs to
> specify house prices up to the dollar?) and high memory usage. In my
> testing, the example above increased RAM usage by gigabytes until the
> web browser eventually gave up (though this is something that should
> be solvable on our end. We'll look into it!)

This was caused by a bug in react-range, which I fixed last year.
https://github.com/tajo/react-range/pull/178

At the time, I had figured it would get picked up by a random yarn
upgrade and didn't worry too much about it.
But, apparently yarn doesn't really have an easy way of doing upgrades
of transitive dependencies (see https://github.com/yarnpkg/yarn/issues/4986)?
I took the suggestion of someone in that thread to delete the entry and
let yarn regenerate it.

Some techinical details about the react-range fix from the original
commit message (the "application" is a streamlit app):

> We have an application that uses react-range under the hood, and we
> noticed that a range input was taking 2GB of RAM on our machines. I
> did some investigation and found that regardless of whether the marks
> functionality was being used, refs were being created for each
> possible value of the range.

> We have some fairly huge ranges (we're using the input to scrub a
> video with potential microsecond accuracy), and can imagine that
> other people are affected by the previous behavior. This change
> should allow us to continue using large input ranges without
> incurring a memory penalty.

---
## [wolfd/streamlit](https://github.com/wolfd/streamlit)@[3485c24eba...](https://github.com/wolfd/streamlit/commit/3485c24ebace15f5d0d20021a955c8ee4799d0de)
#### Tuesday 2023-05-30 23:28:47 by Danny Wolf

Upgrade react-range to fix memory usage of sliders

As mentioned in
https://blog.streamlit.io/six-tips-for-improving-your-streamlit-app-performance/
memory usage struggles in the browser if you have large ranges:

> Due to implementation details, high-cardinality sliders don't suffer
> from the serialization and network transfer delays mentioned earlier,
> but they will still lead to a poor user experience (who needs to
> specify house prices up to the dollar?) and high memory usage. In my
> testing, the example above increased RAM usage by gigabytes until the
> web browser eventually gave up (though this is something that should
> be solvable on our end. We'll look into it!)

This was caused by a bug in react-range, which I fixed last year.
https://github.com/tajo/react-range/pull/178

At the time, I had figured it would get picked up by a random yarn
upgrade and didn't worry too much about it.
But, apparently yarn doesn't really have an easy way of doing upgrades
of transitive dependencies (see https://github.com/yarnpkg/yarn/issues/4986)?
I took the suggestion of someone in that thread to delete the entry and
let yarn regenerate it.

Some technical details about the react-range fix from the original
commit message (the "application" is a streamlit app):

> We have an application that uses react-range under the hood, and we
> noticed that a range input was taking 2GB of RAM on our machines. I
> did some investigation and found that regardless of whether the marks
> functionality was being used, refs were being created for each
> possible value of the range.

> We have some fairly huge ranges (we're using the input to scrub a
> video with potential microsecond accuracy), and can imagine that
> other people are affected by the previous behavior. This change
> should allow us to continue using large input ranges without
> incurring a memory penalty.

---

