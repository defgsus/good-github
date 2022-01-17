## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-16](docs/good-messages/2022/2022-01-16.md)


1,414,884 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,414,884 were push events containing 2,001,458 commit messages that amount to 123,394,856 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [ursinnDev/google_guava](https://github.com/ursinnDev/google_guava)@[e015172847...](https://github.com/ursinnDev/google_guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Sunday 2022-01-16 00:27:32 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [openparty/openparty](https://github.com/openparty/openparty)@[38513e9df8...](https://github.com/openparty/openparty/commit/38513e9df88bce138aa05938ebfdfee811b0aaca)
#### Sunday 2022-01-16 00:45:38 by Tin

hack: upgrade fabric; make the site run again with gunicorn;

Sorry, it's ugly. fabric2's API seems silly, or maybe I'm silly.

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[6f8e20e550...](https://github.com/morgoth1145/advent-of-code/commit/6f8e20e550b1ad2f6689ecd0c3f326d23913f7c4)
#### Sunday 2022-01-16 02:46:42 by Patrick Hogg

2016 Day 2 Part 1

Oof, that's a harder Day 2 too! Still not too bad, but moving around in a fixed grid while bounding the coordinates was interesting.

Honestly though, I wasted a ton of time in mapping the end coordinates to the keypad. Doing it manually is dumb, but my brain wasn't immediately processing how to do it smart. (Which is silly, because isn't it just 3*y + x + 1?)

Time: 0:03:12.710717

---
## [Byte-Masons/defi-ui-template](https://github.com/Byte-Masons/defi-ui-template)@[c63023cd91...](https://github.com/Byte-Masons/defi-ui-template/commit/c63023cd914d4bc7ed341387ce5dcce4b11da4fe)
#### Sunday 2022-01-16 03:25:12 by Morgan Hall

Ask myself what would I want if I didn't know what I know

Get started on work to make the repo a reusable template for shady super-coders and noobs alike.

I've tried to approach this with the following principals:
- we shouldn't use anything so clever, it would create an obstacle to use for someone with less experience
- where we use anything that might be more complicated than paint-by-numbers we should demonstrate its use
- we should offer graduated customization paths so a non-tech person can personallize it with little fuss without preventing a power user from doing whatever they want

With that in mind, I have:
- Set the font to Montserrat.  Its safe, common, and harmless in case the consumer doesn't want to change it
- Added Storybook, and stories for each component we have, so anyone can see what components they have to play with
- Added react-navigation and set our app up as a 4-page demo so we can demonstrate its use
- Created some simple abstractions (components) for common layout css so a noob can find and use what they need without knowledge of CSS
- Used CSS modules and CSS variables so a user can choose to just change color scheme, configure dimensions and a more elaborate color config, or go into the CSS and change it there.
- updated the readme with some notes on use

Some notes:
- Ive chopped and changed between interface/type for defining props.  Theres nothing in this - my IDE quick templates write `interface`, I manually write `type`
- we have some components that are nothing more than a div with styles, and so could be achieved just by using a style.  We do this to make it easy for a novice to pick and choose components they require by name rather than having to understand CSS.  If the consumer does not use these components, tree shaking will omit them from the bundle anyway
- we typically pass bot `className` and `style` through to root tags on each component, to give the consumer max flexibility in styling
- we define props for almost every component, even when these are repetitive.  This is so less experienced devs can change for a single component with confidence. Types are removed in conversion to JS anyway

---
## [Jd-Gamer65/ChatAPI](https://github.com/Jd-Gamer65/ChatAPI)@[9bb6a5f25a...](https://github.com/Jd-Gamer65/ChatAPI/commit/9bb6a5f25aa813130674a883f386ccc9d77aa966)
#### Sunday 2022-01-16 03:30:28 by Jd-Gamer65

oops i fucked up again, my includes suck ass, got lost in the code, ooh baby baby

---
## [casualdegenerate/SynX-WebSocket-Testing](https://github.com/casualdegenerate/SynX-WebSocket-Testing)@[a504d8b331...](https://github.com/casualdegenerate/SynX-WebSocket-Testing/commit/a504d8b3311be427e86657a717e1cd892fd64ed4)
#### Sunday 2022-01-16 04:08:40 by casual_degenerate

Upload

Previous upload made a mistake and it just created an annoying folder where I had all this at and it looked stupid. This will make it look more friendly.

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[4610f700eb...](https://github.com/Zonespace27/tgstation/commit/4610f700eb74a3a41555e69c4904ad897caf2d99)
#### Sunday 2022-01-16 04:26:55 by LemonInTheDark

Fixes up multiz atmos connection, cleans some things up in general (#63270)

About The Pull Request

ALLLRIGHT so
Multiz atmos was letting gas flow down into things that should be well, not flowable into
Like say doors, or windows.

This is weird.

Let's get into some context on why yeah?

First, how do things work currently?

atoms have a can_atmos_pass var defined on them. This points to a define that describes how they interact with
flow.
ATMOS_PASS_NO means well, if we're asked, block any attempts at flow. This is what walls use.
ATMOS_PASS_YES means the inverse
ATMOS_PASS_DENSITY means check our current density
ATMOS_PASS_PROC means call can_atmos_pass, we need some more details about this attempt

These are effectively optimizations.

That var, can_atmos_pass is accessed by CANATMOSPASS() the macro
It's used for 3 things.

1: Can this turf share at all?
2: Can this turf share with another turf
3: Does this atom block a share to another turf

All of this logic is bundled together to weed out the weak.

Anyway, so when we added multiz atmos, we effectively made a second version of this system, but for vertical
checks.

Issue here, we don't actually need to.
The only time we care if a check is vertical or not is if we're talking to another turf, it's not like you'll
have an object that only wants to block vertical atmos.
And even if you did, that's what ATMOS_PASS_PROC is for.

As it stands we need to either ignore any object behavior, or just duplicate can_atmos_pass but again.
Silly.

So I've merged the two, and added an arg to mark if this is a verical attempt.
This'll fix things that really should block up/down but don't, like windows and doors and such.

Past that, I've cleaned can_atmos_pass up a bit so it's easier for people to understand in future.
Oh and I removed the second CANATMOSPASS from immediate_calculate_adjacent_turfs.
It isn't a huge optimization, and it's just not functional.

It ties into zAirOut and zAirIn, both of which expect to be called with a valid direction.
So if say, you open a door that's currently blocking space from leaking in from above, you end up with the door
just not asking the space above if it wants to share, since the door can't zAirOut with itself.

Let's just wipe it out.

This makes the other code much cleaner too, heals the soul.

Anyway yadeyada old as ass bug, peace is restored to the kingdom, none noticed this somehow you'd think people
would notice window plasma, etc etc.
Why It's Good For The Game

MUH SIMULATION
Also fuck window gas
Changelog

cl
fix: Fixed gas flowing into windows from above, I am.... so tired
fix: Fixes gas sometimes not moving up from below after a structure change, see above
/cl

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[a2fa7799f3...](https://github.com/LemonInTheDark/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Sunday 2022-01-16 04:46:12 by Jeremiah

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
## [samboy/nexuiz-tiny](https://github.com/samboy/nexuiz-tiny)@[1a29527f32...](https://github.com/samboy/nexuiz-tiny/commit/1a29527f32fc1e622f7a30bdde2a1e2c47328fac)
#### Sunday 2022-01-16 04:54:59 by Sam Trenholme

Blood Prison now uses same skybox as Soylent

Now, we have only three skyboxes:

Day: Downer, Final Rage
Sunset: Graphite, Toxic
Night: Soylent, Aerowalk, Blood Prison

---
## [boy2mantwicethefam/vgstation13](https://github.com/boy2mantwicethefam/vgstation13)@[622f3fac2b...](https://github.com/boy2mantwicethefam/vgstation13/commit/622f3fac2b24476f23d8c9ebfae2dba5e371a3cc)
#### Sunday 2022-01-16 05:08:50 by ShiftyRail

The Thing Before Christmas (#31715)

I thought this was a good way to spice up the winter season.
While I know Ling was removed for a reason, I want you to consider that it got removed years ago. It is fair to say that the playerbase and the game changed so much since then than a "tabula rasa" might be justified.

Besides, ling had deathsting removed and its obnoxious chemical stings axxed too. (#23014)
From a QoL standpoint, the stings have been converted to spells and should be as easy to use as the vampire ones.

As a final note, it's painstaingly true that ling is the least worked over of all our antags and is in dire need of some love and new content. However, this content can only come if people experience ling first-hand and get motivated to fix it.

Worse come to worse, we remove it again lole

Merry Christmas everyone.

:cl:
- rscadd: Santa Claus is coming to town. More specifically, he's coming to Antartica. Wait, he was already here all this time? And why does he look so familiar... OH GOD HELP

---
## [davidbuzz/ardu-configurator](https://github.com/davidbuzz/ardu-configurator)@[7e0a444f79...](https://github.com/davidbuzz/ardu-configurator/commit/7e0a444f79fa612bf2150be5c27bfb7f6666bc06)
#### Sunday 2022-01-16 05:39:13 by Buzz

wip smartlinks test - can we get server-side node from mavagent to work?


more wip - 

tmp copied mav_v2.js direct from mavagent, as its known to work with smartlinks.js , also from mavagent.  todo delete the mav_v2 and use the one in js/mavsp/ foldrr
notes abut using -sdk version for developers


make new backend folder for Node-loaded local code.


allow jspack and 'long' module to both be used by the backend, if we want. 

yes, this is a differernet to the one in js/mavsp/local_modules/ which are currently tweaked for frontend use. sorry about the dupe, we should fix that at some point.
add mavlink parser as a proper local-node-module to the backend

.. with just tiny tweaks.
describe NW flavour on console at startup.

its easy to get the wrong one.
more dev notes


lightly hacked mavagent.js and its modules bing used as a pre-startup.js for ArduConfigurator.

// TERRIBLE HACK using mavagent.js almost in its entirety as a pre-startup.js for arduconfigurator.  
// surprisingly, it seems to kinda mostly work apart from the CLI interface.    we won't leave this here, but its interesting.
 - having this loaded its connecting to a SITL instance on tcp:localhost:5760 if u have one, and forwarding the packets to udp:localhost:14550, such as missionplanner etc.   its not yet routing any of this mavlink stream into the GUI, but its not crashing. 
remove most of  mavagent from pre-startup.js leaving mostly just smartlinks.js  AND get backend UDP routing through to frontend

frontend GUI is a bit borked when UDP right now, but its getting the data.
hex_parser changes are untested so hext parsing might be broken.?

prevents *really* early udp/tcp throwing error before window is opend.

---
## [i5ik/KevinBatdorf](https://github.com/i5ik/KevinBatdorf)@[dee899f176...](https://github.com/i5ik/KevinBatdorf/commit/dee899f176af61821d03f40b29571a33aa115316)
#### Sunday 2022-01-16 05:52:58 by Cris

Quick typo fix: th ebig -> the big ;)

Hey Kevin, thanks for your star at weird-json, just reading your profile and really appreciate what you're doing. Sorry for this annoying PR 😅 
I know how typo fixes, especially on a personal profile repo, can seem like annoying criticisms or put downs. I'm not doin that, man! 
Just bothered to make this for you to see a fellow dev present at his best! My small contribution anyway 😄

---
## [Draconomial/CombatExtended](https://github.com/Draconomial/CombatExtended)@[e9c4ac2915...](https://github.com/Draconomial/CombatExtended/commit/e9c4ac29158608d0b4d0349dd2984784d954fba2)
#### Sunday 2022-01-16 06:43:41 by AL9000

mortar

"You know what, fuck you!"
*replaces mortar def*

---
## [ncrecc/jumper4real](https://github.com/ncrecc/jumper4real)@[1e69b57f9e...](https://github.com/ncrecc/jumper4real/commit/1e69b57f9e2a4c42c64691c12cacaf68196dbf39)
#### Sunday 2022-01-16 07:14:50 by wibi

more level symbols for you
ok, last commit was a lot longer ago than i realized. after this are some big changes in tiles, audio, and hopefully levels

- levelsymbols are now two characters each, which will allow for a hell lot more tiles and objects. the first character of each levelsymbol depends on its "category"; see legend.txt for a description of those. (these are only for some minimal amount of neatness and in practice an actual category field for each levelsymbol will be used instead) old levels don't work anymore, obviously, so they've been removed. ogmo touches grass will likely be reintroduced eventually
- controls can now be rebound at %appdata%\LOVE\jumper4real\controls.txt
- added double-jump arrows
- fixed an issue with mask-based overlap check that caused overlaps to rarely be accurately detected
- objects can now call scripts upon being collided with. for now no objects actually have any of these scripts, and the only object that can trigger them is ogmo
- ogmo can now skidjump
- ogmo now uses S to jump and up to look upwards (using two previously unused sprites)
- rubber now works. damn well, even
- added support for rotating things in the editor; currently just applies to slabs
- you can now pause in-game. right now this isn't useful for much except seeing the quirky random facts
- save/load textbox in the editor is now empty by default instead of containing "awesomelevelset/level1"
- polished ashley's sprite a bit
- added mo (ultra-retro 4x4 ogmo) and upside as ogmo skins
- renamed slope tiles to fit a better naming scheme (denotes non-empty part)
- added ogmos.lua, currently just listing the ogmo skins and containing descriptions for them
- more stuff, probably

---
## [Bawhoppen/-tg-station](https://github.com/Bawhoppen/-tg-station)@[7bead07444...](https://github.com/Bawhoppen/-tg-station/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Sunday 2022-01-16 07:51:49 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [devout-coder/conquer-rn-app](https://github.com/devout-coder/conquer-rn-app)@[2c124e7960...](https://github.com/devout-coder/conquer-rn-app/commit/2c124e79603d29271d55d020f722e4710490cfa5)
#### Sunday 2022-01-16 08:00:07 by awesssome-pro

unfucked browser listener..had pasted some weird shit over there from my clipboard

---
## [waebbl/sci](https://github.com/waebbl/sci)@[d016c223d9...](https://github.com/waebbl/sci/commit/d016c223d9e994ce2b650a48dd78b9e4089e2725)
#### Sunday 2022-01-16 08:13:28 by Andrew Ammerlaan

sci-mathematics/scilab-bin: add version 6.1.1

I officially give up on making a non-bin ebuild. There are several problems:

1. The java dependencies are extremely difficult because of packaging systems
that portage does not support (gralde, maven etc). We can hack around this
as we did in dev-java/lucene::sci, but that is *a lot* of work, for a lot of
dependencies that has to be redone on each version bump.
We can solve this problem by getting the pre-compiled java dependencies from
https://github.com/scilab/scilab-prerequirements. However....

2. Scilab requires versions of libraries that we do not package any more in
::gentoo (e.g. hdf5). And adding and maintaining ebuilds for those old libraries
is too much work.

3. If we take *only* the java stuff from scilab/scilab-prerequirements, build
fails (likely incompatibility with certain versions of some non-java libraries,
see 2.)

4. If we take *all* of scilab/scilab-prerequirements build still fails (with
a different error this time).

5. The amount of scilab dependencies that are being last-rited and I therefore
have to move to ::science to keep the dependencies resolving is increasing.
Scilab is the number 1 cause of ::science breaking at the moment.

Long story short, please enjoy this pre-compiled binary ebuild that actually
works and will save us all a lot of headache.

Closes: https://bugs.gentoo.org/237572
Closes: https://bugs.gentoo.org/691272
Closes: https://github.com/gentoo/sci/issues/879
Closes: https://github.com/gentoo/sci/issues/774
Package-Manager: Portage-3.0.30, Repoman-3.0.3
Signed-off-by: Andrew Ammerlaan <andrewammerlaan@gentoo.org>

---
## [snylonue/mpv](https://github.com/snylonue/mpv)@[5309497727...](https://github.com/snylonue/mpv/commit/5309497727debfe1b268f915c5a41bdbe93ad9de)
#### Sunday 2022-01-16 08:16:51 by wm4

subprocess: replace posix_spawnp() with fork()

This code runs posix_spawnp() within a fork() in some cases, in order to
"disown" processes which are meant as being started detached. But
posix_spawnp() is not marked as async-signal-safe, so what we do is not
allowed. It could for example cause deadlocks, depending on
implementation and luck at runtime. Turns out posix_spawnp() is useless
crap.

Replace it with "classic" fork() to ensure correctness.

We could probably use another mechanism to start a process "disowned"
than doing a double-fork(). The only problem with "disowning" a process
is calling setsid() (which posix_spawnp() didn't support, but maybe will
in newer revisions), and removing as as parent from the child process
(the double-fork() will make PID 1 the parent). But there is no good way
to either remove us as parent, or to "reap" the PID in a way that is
safe and less of a mess than the current code. This is because
POSIX/UNIX is a miserable heap of shit. (Less shit than "alternatives"
like win32, no doubt.)

Because POSIX/UNIX is a miserable heap of shit, execvp() is also not
specified as async-signal-safe. It's funny how you can run a full
fledged HTTP server in an async-signal-safe context, but not start a
shitty damn process. Unix is really, really, really extremely bad at
this process management stuff. So we reimplement execvp() in an
async-signal-safe way.

The new code assumes that CLOEXEC is a thing. Since POSIX/UNIX is such a
heap of shit, O_CLOEXEC and FD_CLOEXEC were (probably) added at
different times, but both must be present. io.h defines them to 0 if
they don't exist, and in this case the code will error out at runtime.
Surely we could do without CLOEXEC via fallback, but I'll do that only
if at least 1 bug is reported wrt. this issue.

The idea how to report exec() failure or success is from musl. The way
as_execvpe() is also inspired by musl (for example, the list of error
codes that should make it fail is the same as in musl's code).

---
## [snylonue/mpv](https://github.com/snylonue/mpv)@[b36484063f...](https://github.com/snylonue/mpv/commit/b36484063f1dcf7928f848e78572d1e5d1d5a62b)
#### Sunday 2022-01-16 08:16:51 by wm4

vo_direct3d: rip out texture video rendering path

This isn't useful anymore. We have a much better d3d11 renderer in
vo_gpu. D3D11 is available in all supported Windows versions. The
StretchRect path might still be useful for someone (???), and leaving it
at least evades conflict about users who want to keep using this VO for
inexplicable reasons. (Low power usage might be a justified reason, but
still, no.)

Also fuck the win32 platform, it's a heap of stinky shit. Microsoft is
some sort of psycho clown software company. Granted, maybe still better
than much of the rest of Silly Con Valley.

---
## [snylonue/mpv](https://github.com/snylonue/mpv)@[c6369933f1...](https://github.com/snylonue/mpv/commit/c6369933f1d9cd204b09be95ef7d4ed1351610e2)
#### Sunday 2022-01-16 08:16:51 by wm4

command: add property to return text subtitles in ASS

See manpage additions. This was requested, sort of. Although what has
been requested might be something completely different. So this is
speculative.

This also changes sub_get_text() to return an allocated copy, because
the buffer shit was too damn messy.

---
## [T1DMS/MineSweeper](https://github.com/T1DMS/MineSweeper)@[b0e13f564d...](https://github.com/T1DMS/MineSweeper/commit/b0e13f564d82c0b32724cd274f8a78b3abf52d81)
#### Sunday 2022-01-16 10:20:13 by T1DMS

MineSweeper

Heres the code:

import random
import re

# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function!
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set 
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer,
        # but since we have a 2-D board, list of lists is most natural)

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]
        # we can see how this represents a board!

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell us what row to look at
            col = loc % self.dim_size  # we want the remainder to tell us what index in that row to look at

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*' # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. we can precompute these and it'll save us some
        # effort checking what's around the board later on :)
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure to not go out of bounds!

        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors!

        self.dug.add((row, col)) # keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r, c)

        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    #          next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    safe = True 

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # 0,0 or 0, 0 or 0,    0
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb ahhhhhhh
            break # (game over rip)

    # 2 ways to end loop, lets check which one
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        # let's reveal the whole board!
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': # good practice :)
    play()

---
## [lordofwizard/codechef](https://github.com/lordofwizard/codechef)@[c31d0e3b63...](https://github.com/lordofwizard/codechef/commit/c31d0e3b6370d6d10e436fb19ee6ebc1949dffd9)
#### Sunday 2022-01-16 10:41:15 by lordofwizard

after fucking my brain for 2 hours and with help of sudhanshu marudgan i FINALLY SOLVED THIS SHIT

---
## [izMystic/qb-hud](https://github.com/izMystic/qb-hud)@[af18f6d04a...](https://github.com/izMystic/qb-hud/commit/af18f6d04a62320bc9f0c15fb09f2268392384ee)
#### Sunday 2022-01-16 11:22:40 by izMystic

update: why use function when command already has permission checking built in

What you know about rollin’ down in the deep?
When your brain goes numb, you can call that mental freeze
When these people talk too much, put that shit in slow motion, yeah
I feel like an astronaut in the ocean, ayy
What you know about rollin’ down in the deep?
When your brain goes numb, you can call that mental freeze
When these people talk too much, put that shit in slow motion, yeah
I feel like an astronaut in the ocean

She say that I’m cool (Damn straight)
I’m like “Yeah, that’s true” (That’s true)
I believe in G-O-D (Ayy)
Don’t believe in T-H-O-T
She keep playing me dumb (Play me)
I’ma play her for fun (Uh-huh)
Y’all don’t really know my mental
Let me give you the picture like stencil
Fallin’ out in a drought
No flow, rain wasn’t pourin’ down (Pourin’ down)
See, that pain was all around
See, my mode was kinda lounged
Didn’t know which, which way to turn
Flow was cool but I still felt burnt
Energy up, you can feel my surge
I’ma kill everything like this purge (Ayy)

Let’s just get this straight for a second, I’ma work (Yuh)
Even if I don’t get paid for progression, I’ma get it (Uh, get it)
Everything that I do is electric (Ayy)
I’ma keep it in a motion, keep it movin’ like kinetic, ayy (Yeah, yeah, yeah, yeah, yeah)

Put this shit in a frame, better know I don’t blame
Everything that I say, man, I seen you deflate
Let me elevate, this ain’t a prank
Have you walkin’ on a plank, la-la-la-la, like
Both hands together, God, let me pray (Now let me pray), uh
I’ve been goin’ right, right around, call that relay (Masked Wolf)
Pass the baton, back and I’m on
Swimmin’ in the pool—Kendrick Lamar, uh (Ayy)
Want a piece of this, a piece of mine, my peace a sign
Can you please read between the lines?
My rhyme’s inclined to break your spine (Spine)
They say that I’m so fine (Fine)
You could never match my grind (True)
Please do not, not waste my time (Wolf)

What you know about rollin’ down in the deep?
When your brain goes numb, you can call that mental freeze
When these people talk too much, put that shit in slow motion, yeah
I feel like an astronaut in the ocean, ayy
What you know about rollin’ down in the deep?
When your brain goes numb, you can call that mental freeze
When these people talk too much, put that shit in slow motion, yeah
I feel like an astronaut in the ocean

---
## [Waselon/TerraGov-Marine-Corps](https://github.com/Waselon/TerraGov-Marine-Corps)@[4529479889...](https://github.com/Waselon/TerraGov-Marine-Corps/commit/4529479889ccc617b1aee8519755e6ab5aa49b08)
#### Sunday 2022-01-16 11:24:59 by hyper2snyper

Lasgun fixes (#9183)

* FUCK YOU SO MUCH EGUNS

* Update guns_codex.dm

---
## [ThomasLandauer/symfony-docs](https://github.com/ThomasLandauer/symfony-docs)@[af131ba7cb...](https://github.com/ThomasLandauer/symfony-docs/commit/af131ba7cb31dc2f65c9fb56332ce6d138b36b22)
#### Sunday 2022-01-16 12:02:54 by Javier Eguiluz

minor #16084 Move myself alongside the inactive Core team members. (sroze)

This PR was submitted for the 5.4 branch but it was merged into the 4.4 branch instead.

Discussion
----------

Move myself alongside the inactive Core team members.

**What a fun ride!** This community is the best I've been working with, full of talented and caring people. I've learnt so much by fixing `@nicolas`-grekas' broken tests or convincing `@fabpot` to ship this Messenger component. I also hope that this modest contribution to the ever-growing list of components inspires others to do the same, give back to an open-source project that enabled me as an engineer to be always more productive and enables us all to focus on solving worlds' problems rather than re-inventing the wheel again.

**I won't have much time for Symfony in the coming 12 months, at least.** For a fair chunk of time already, I have not been able to devote enough time to maintaining and evolving Symfony, and it will remain the same for a little while: I want to focus my energy on building mission-driven startups and it requires my full attention to make them successful. It means I'm not really a Core Team member anymore, so let's make it official so the list can be expanded with great people that have the time I don't.

`@symfony`/mergers thank you so much for your continuous work and care for this amazing project, I know it can only continue to shine. See you in the real world at some conferences, I'm sure ❤️

Commits
-------

2ffdccb54 Move myself alongside the inactive Core team members.

---
## [Evolution-X-Vayu/device_xiaomi_vayu](https://github.com/Evolution-X-Vayu/device_xiaomi_vayu)@[e92c37ce23...](https://github.com/Evolution-X-Vayu/device_xiaomi_vayu/commit/e92c37ce23b17282a6dcb6d96fd35ce5d1f948a9)
#### Sunday 2022-01-16 12:41:46 by klozz

vayu: Disable Android Rescue Party trigger

* Sometimes is fucked and the ROM wants clean shit

Signed-off-by: klozz <klozz@TheXPerienceProject.org>
Change-Id: I2bd06a176a262b9dadf30846dcaf76378b63ea9f

---
## [Eclipse-Station/NEV-Northern-Light](https://github.com/Eclipse-Station/NEV-Northern-Light)@[9d1fa5b852...](https://github.com/Eclipse-Station/NEV-Northern-Light/commit/9d1fa5b8524a9eaf7b46ad212511d508c738d56e)
#### Sunday 2022-01-16 13:05:32 by drexample

Courtesy of @EvilJackCarver - fixes Malf AI spawning when it really shouldn't

Fuck you *unmalfs you ai*

---
## [haxscramper/nimskull](https://github.com/haxscramper/nimskull)@[02bbe58611...](https://github.com/haxscramper/nimskull/commit/02bbe58611662a6d52a86b6e58e465c197711772)
#### Sunday 2022-01-16 14:40:24 by haxscramper

Make compiler report structured

Full rework of the compiler message handling pipeline. Remove old-style message generation that was
based purely on strings that were formatted in-place, and instead implement structured logging where
main compiler code only instantiates objects with required information.

Explanation of changes for this commit will be split into several sections, matching number of edit
iterations I had to make in order for this to work properly.

* File reorganization

In addition to the architectural changes this PR requires some type definition movements.

- PNode, PSym and PType definitions (and all associated types and enums) were moved to the
  ast_types.nim file which is then reexported in the ast.nim
- Enum defininitions for the nilability checking were moved to nilcheck_enums.nim and then
  reexported
- Enum definitions for the VM were moved to to vm_enums.nim

* New files

- Main definition of the report types is provided in the reports.nim file, together with minor
  helper procedures and definition of the ReportList type. This file is imported by options, msgs
  and other parts of the compiler.
- Implementation of the default error reporting is provided in the cli_reporter.nim - all
  disguisting hardcoded string hacks were moved to this single file. Now you can really witness the
  "error messages are good enough for me" thinking that prevailed in the compiler UX since it's
  inception.

* Changed files

Most of the changes follow very simple pattern - old-style hardcoded hacks are replaced with
structural report that is constructed in-place and then converted to string /when necessary/. I'm
pretty sure this change already puts me close to getting CS PHD - it was *unimaginably hard* to
figure out that hardcoding text formatting in place is not the best architecture. Damn, I can
probably apply to the nobel prize right now after I figure that out.

** Changes in message reporting pipeline

Old error messages where reportined via random combinations of the following:

- Direct calls to `msgs.liMessage` proc - it was mostly used in the helper templates like
  `lintReport`
- `message`
- `rawMessage`
- `fatal`
- `globalError` - template for reporting global errors. Misused to the point where name completely
  lost it's meaning and documentation does not make any sense whatsoever. [fn:global-err]
- `localError` - template for reporting necessary error location, wrapper around `liMessage`
- `warningDeprecated` - used two times in the whole compiler in order to print out error message
  about deprecated command switches.

Full pipeline of the error processing was:

- Message was generated in-place, without any colored formatting (was added in `liMessage`)
  - There were several ways message could be generated - all of them were used interchangeably,
    without any clear system.
    1. Some file had a collection of constant strings, such as `errCannotInferStaticParam = "cannot
       infer the value of the static param '$1'"` that were used in the `localReport` message
       formatting immediately. Some constants were used pretty often, some were used only once.
    2. Warning and hint messages were categorized to some extent, so and the enum was used to
       provide message formatting via `array[TMsgKind, string]` where `string` was a `std/strutils`
       formatting string.
    3. In a lot of cases error message was generated using hardcoded (and repeatedly copy-pasted)
       string
- It was passed down to the `liMessage` (removed now) procedure, that dispatched based on the global
  configuration state (whether `ignoreMsgBecauseOfIdeTools` holds for example)
- Then message, together with necessary bits of formatting (such as `Hint` prefix with coloring) was
  passed down to the `styledMsgWriteln(args: varargs[typed])` template, whcih did the final dispatch
  into
- One of the two different /macros/ for writing text out - `callStyledWriteLineStderr` and
  `callIgnoringStyle`.
  - Dispatch could happen into stdout/stderr or message writer hook if it was non-nil
- When message was written out it went into `writeLnHook` callback (misused for
  `{.explain.}` [fn:writeln-explain]) (hacked for `compiles()` [fn:writeln-compiles]) and was
  written out to the stdout/stderr.

It is now replaced with:

- `Report` object is instantiated at some point of a compilation process (it might be an immediate
  report via `localError` or delayed via `nkError` and written out later)
- `structuredReportHook` converts it to string internally. All decitions for formatting, coloring
  etc. happen inside of the structured report hook. Where to write message, which format and so on.
- `writeLnHook` /can/ be used by the `structuredReportHook` if needed - right now it is turned into
  simple convenience callback. In future this could even be replaced with simple helper proc, for
  now I left it as it is now because I'm not 100% sure that I can safely remove this.

** Changes in the warning and hint filtering

Report filtering is done in the particular *implementation* of the error hook -
`options.isEnabled()` provides a default predicate to check whether specific report can be written
out, but it must still be called manually. This allows to still see all the reports if needed. For
example, `cli_reporter.reportHook()` uses additional checks to force write some reports (such as
debug trace in `compiles()` context).

Most of the hint and warning were already categorized, altough some reports had to be split into
several (such as `--hint=Performance` that actually controlled reports for `CopiesToSink` and
`CannotMakeSink`, `--hint=Name` that controlled three reports).

None of the errors were categorized (reports from the `nkError` progress was incorporated, but in
I'm mostly describing changes wrt. to old reporting system) and all were generated in-place

** Minor related changes

- List of allowed reports is now stored in the `noteSets: array[ConfNoteSet, ReportKinds]` field of
  the `ConfigRef`, instead of *seven* separate feilds. Access is now done via getter/setter procs,
  which allows to track changes in the current configuration state.
- Renamed list of local options to `localOptions` - added accessors to track changes in the state.
- Move all default report filter configuration to `lineinfos.computeNotesVerbosity()` - previously
  it was scattered in two different places: `NotesVerbosity` for `--verbosity:N` was calculated in
  `lineinfos`, foreignPackageNotesDefault was constructed in `options`
- Changed formatting of the `internalAssert` and `internalError` messages
- Removed lots of string formatting procs from the various `sem*` modules - ideally they should
  *all* be moved to the `cli_reporter` and related.

-------

Additional notes

[fn:global-err] As I said earlier, `globalError` was misused - it is still not possible to fully get
rid of this sickening hack, since it is used for /control flow/ (you read this correct - it is an
error reporting template, and it is used for control flow. Wonderful design right?).

So, in short - `globalError` can raise `ERecoverableError` that can be caught in some other layer
(for example `sem.tryConstExpr` abuses that in order to bail out (pretty sure it was done as an
'optimization' of some sort, just like 'compiles') when expression fails to evaluate at
compile-time [fn:except])

[fn:except] https://github.com/nim-works/nimskull/pull/94#issuecomment-1006927599

[fn:writeln-explain] Of course you can't have a proper error reporting in the nim compiler, so this
hook was also misused to the point of complete nonsense. Most notable clusterfuck where you could
spot this little shit is implementation of `{.explain.}` pragma for concepts. It was implemented via
really 'smart' (aka welcome to hell) solution in

https://github.com/nim-works/nimskull/commit/74a80988d9289e8147a791c4b0939d4287baaff3 (sigmatch
~704) and then further "improved" in
https://github.com/nim-lang/Nim/commit/fe48dd1cbec500298f7edeb75f1d6fef8490346c by slicing out parts
of the error message with `let msg = s.replace("Error:", errorPrefix)`

For now I had to reuse similar hack - I *do* override error reporting hook in order to collect all
the missing report information. In the future it would be unnecessary - when concept is matched it's
body will be evaluated to `nkError` with reports that are written out later.

[fn:writeln-compiles] when `compiles()` check is executed, all error output is temporarily disabled
(both stderr and stdout) via setting allowed output flags to `{}` (by default it is set to

---
## [SmoSmoSmoSmok/fulpstation](https://github.com/SmoSmoSmoSmok/fulpstation)@[c797bf79ea...](https://github.com/SmoSmoSmoSmok/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Sunday 2022-01-16 14:41:21 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [SmoSmoSmoSmok/fulpstation](https://github.com/SmoSmoSmoSmok/fulpstation)@[b59f03e592...](https://github.com/SmoSmoSmoSmok/fulpstation/commit/b59f03e592ce72f069760eba0f9eb30eeacd16c1)
#### Sunday 2022-01-16 14:41:21 by John Willard

Deputy update (#428)

* deputy berets cant be knocked off, deputies get tablets, service deputy beret buff.

* fuck you

---
## [plinkiac/Movie-Talk](https://github.com/plinkiac/Movie-Talk)@[5716c8ee2e...](https://github.com/plinkiac/Movie-Talk/commit/5716c8ee2e3a3876669f856f8e4cefc11c5c70f8)
#### Sunday 2022-01-16 15:51:36 by Harry S. Plinkett

Rename 2015-01-10 - Fuck You, It's January.txt to 2015-01-10 - Fuck You, It's January (2015).txt

---
## [safwan6363/my-files](https://github.com/safwan6363/my-files)@[75c6e0c86c...](https://github.com/safwan6363/my-files/commit/75c6e0c86c40d9ba445b320a54025c5af3b35b4b)
#### Sunday 2022-01-16 16:25:46 by safwan6363

Bro oh my god fuck yes this was exactly

what i was looking for holy shit now the hard links also work perfectly
fine this is ultra hagu amazing oh my fuckking god ok

---
## [Runsit52/docs](https://github.com/Runsit52/docs)@[5c70349440...](https://github.com/Runsit52/docs/commit/5c703494409263c256b46d71d883d58c54c6ba26)
#### Sunday 2022-01-16 17:13:24 by Runsit52

Update index.md

Are you a law enforcement officer conducting an investigation that may involve user content hosted on GitHub? Or maybe you're a privacy-conscious person who would like to know what information we share with law enforcement and under what circumstances. Either way, you're on the right page.

In these guidelines, we provide a little background about what GitHub is, the types of data we have, and the conditions under which we will disclose private user information. Before we get into the details, however, here are a few important details you may want to know:

We will notify affected users about any requests for their account information, unless prohibited from doing so by law or court order.
We will not disclose location-tracking data, such as IP address logs, without a valid court order or search warrant.
We will not disclose any private user content, including the contents of private repositories, without a valid search warrant.
About these guidelines
Our users trust us with their software projects and code—often some of their most valuable business or personal assets. Maintaining that trust is essential to us, which means keeping user data safe, secure, and private.

While the overwhelming majority of our users use GitHub's services to create new businesses, build new technologies, and for the general betterment of humankind, we recognize that with millions of users spread all over the world, there are bound to be a few bad apples in the bunch. In those cases, we want to help law enforcement serve their legitimate interest in protecting the public.

By providing guidelines for law enforcement personnel, we hope to strike a balance between the often competing interests of user privacy and justice. We hope these guidelines will help to set expectations on both sides, as well as to add transparency to GitHub's internal processes. Our users should know that we value their private information and that we do what we can to protect it. At a minimum, this means only releasing data to third-parties when the appropriate legal requirements have been satisfied. By the same token, we also hope to educate law enforcement professionals about GitHub's systems so that they can more efficiently tailor their data requests and target just that information needed to conduct their investigation.

GitHub terminology
Before asking us to disclose data, it may be useful to understand how our system is implemented. GitHub hosts millions of data repositories using the Git version control system. Repositories on GitHub—which may be public or private—are most commonly used for software development projects, but are also often used to work on content of all kinds.

Users — Users are represented in our system as personal GitHub accounts. Each user has a personal profile, and can own multiple repositories. Users can create or be invited to join organizations or to collaborate on another user's repository.

Collaborators — A collaborator is a user with read and write access to a repository who has been invited to contribute by the repository owner.

Organizations — Organizations are a group of two or more users that typically mirror real-world organizations, such as businesses or projects. They are administered by users and can contain both repositories and teams of users.

Repositories — A repository is one of the most basic GitHub elements. They may be easiest to imagine as a project's folder. A repository contains all of the project files (including documentation), and stores each file's revision history. Repositories can have multiple collaborators and, at its administrators' discretion, may be publicly viewable or not.

Pages — GitHub Pages are public webpages freely hosted by GitHub that users can easily publish through code stored in their repositories. If a user or organization has a GitHub Page, it can usually be found at a URL such as https://username.github.io or they may have the webpage mapped to their own custom domain name.

Gists — Gists are snippets of source code or other text that users can use to store ideas or share with friends. Like regular GitHub repositories, Gists are created with Git, so they are automatically versioned, forkable and downloadable. Gists can either be public or secret (accessible only through a known URL). Public Gists cannot be converted into secret Gists.

User data on GitHub.com
Here is a non-exhaustive list of the kinds of data we maintain about users and projects on GitHub.

Public account data — There is a variety of information publicly available on GitHub about users and their repositories. User profiles can be found at a URL such as https://github.com/username. User profiles display information about when the user created their account as well their public activity on GitHub.com and social interactions. Public user profiles can also include additional information that a user may have chosen to share publicly. All user public profiles display:

Username

The repositories that the user has starred

The other GitHub users the user follows

The users that follow them

Optionally, a user may also choose to share the following information publicly:

Their real name

An avatar

An affiliated company

Their location

A public email address

Their personal web page

Organizations to which the user is a member (depending on either the organizations' or the users' preferences)

Private account data — GitHub also collects and maintains certain private information about users as outlined in our Privacy Policy. This may include:

Private email addresses

Payment details

Security access logs

Data about interactions with private repositories

To get a sense of the type of private account information that GitHub collects, you can visit your personal dashboard and browse through the sections in the left-hand menubar.

Organization account data — Information about organizations, their administrative users and repositories is publicly available on GitHub. Organization profiles can be found at a URL such as https://github.com/organization. Public organization profiles can also include additional information that the owners have chosen to share publicly. All organization public profiles display:

The organization name

The repositories that the owners have starred

All GitHub users that are owners of the organization

Optionally, administrative users may also choose to share the following information publicly:

An avatar

An affiliated company

Their location

Direct Members and Teams

Collaborators

Public repository data — GitHub is home to millions of public, open-source software projects. You can browse almost any public repository (for example, the Atom Project) to get a sense for the information that GitHub collects and maintains about repositories. This can include:

The code itself
Previous versions of the code
Stable release versions of the project
Information about collaborators, contributors and repository members
Logs of Git operations such as commits, branching, pushing, pulling, forking and cloning
Conversations related to Git operations such as comments on pull requests or commits
Project documentation such as Issues and Wiki pages
Statistics and graphs showing contributions to the project and the network of contributors
Private repository data — GitHub collects and maintains the same type of data for private repositories that can be seen for public repositories, except only specifically invited users may access private repository data.

Other data — Additionally, GitHub collects analytics data such as page visits and information occasionally volunteered by our users (such as communications with our support team, survey information and/or site registrations).

We will notify any affected account owners
It is our policy to notify users about any pending requests regarding their accounts or repositories, unless we are prohibited by law or court order from doing so. Before disclosing user information, we will make a reasonable effort to notify any affected account owner(s) by sending a message to their verified email address providing them with a copy of the subpoena, court order, or warrant so that they can have an opportunity to challenge the legal process if they wish. In (rare) exigent circumstances, we may delay notification if we determine delay is necessary to prevent death or serious harm or due to an ongoing investigation.

Disclosure of non-public information
It is our policy to disclose non-public user information in connection with a civil or criminal investigation only with user consent or upon receipt of a valid subpoena, civil investigative demand, court order, search warrant, or other similar valid legal process. In certain exigent circumstances (see below), we also may share limited information but only corresponding to the nature of the circumstances, and would require legal process for anything beyond that. GitHub reserves the right to object to any requests for non-public information. Where GitHub agrees to produce non-public information in response to a lawful request, we will conduct a reasonable search for the requested information. Here are the kinds of information we will agree to produce, depending on the kind of legal process we are served with:

With user consent — GitHub will provide private account information, if requested, directly to the user (or an owner, in the case of an organization account), or to a designated third party with the user's written consent once GitHub is satisfied that the user has verified his or her identity.

With a subpoena — If served with a valid subpoena, civil investigative demand, or similar legal process issued in connection with an official criminal or civil investigation, we can provide certain non-public account information, which may include:

Name(s) associated with the account
Email address(es) associated with the account
Billing information
Registration date and termination date
IP address, date, and time at the time of account registration
IP address(es) used to access the account at a specified time or event relevant to the investigation
In the case of organization accounts, we can provide the name(s) and email address(es) of the account owner(s) as well as the date and IP address at the time of creation of the organization account. We will not produce information about other members or contributors, if any, to the organization account or any additional information regarding the identified account owner(s) without a follow-up request for those specific users.

Please note that the information available will vary from case to case. Some of the information is optional for users to provide. In other cases, we may not have collected or retained the information.

With a court order or a search warrant — We will not disclose account access logs unless compelled to do so by either (i) a court order issued under 18 U.S.C. Section 2703(d), upon a showing of specific and articulable facts showing that there are reasonable grounds to believe that the information sought is relevant and material to an ongoing criminal investigation; or (ii) a search warrant issued under the procedures described in the Federal Rules of Criminal Procedure or equivalent state warrant procedures, upon a showing of probable cause. In addition to the non-public user account information listed above, we can provide account access logs in response to a court order or search warrant, which may include:

Any logs which would reveal a user's movements over a period of time
Account or private repository settings (for example, which users have certain permissions, etc.)
User- or IP-specific analytic data such as browsing history
Security access logs other than account creation or for a specific time and date
Only with a search warrant — We will not disclose the private contents of any user account unless compelled to do so under a search warrant issued under the procedures described in the Federal Rules of Criminal Procedure or equivalent state warrant procedures upon a showing of probable cause. In addition to the non-public user account information and account access logs mentioned above, we will also provide private user account contents in response to a search warrant, which may include:

Contents of secret Gists
Source code or other content in private repositories
Contribution and collaboration records for private repositories
Communications or documentation (such as Issues or Wikis) in private repositories
Any security keys used for authentication or encryption
Under exigent circumstances — If we receive a request for information under certain exigent circumstances (where we believe the disclosure is necessary to prevent an emergency involving danger of death or serious physical injury to a person), we may disclose limited information that we determine necessary to enable law enforcement to address the emergency. For any information beyond that, we would require a subpoena, search warrant, or court order, as described above. For example, we will not disclose contents of private repositories without a search warrant. Before disclosing information, we confirm that the request came from a law enforcement agency, an authority sent an official notice summarizing the emergency, and how the information requested will assist in addressing the emergency.

Cost reimbursement
Under state and federal law, GitHub can seek reimbursement for costs associated with compliance with a valid legal demand, such as a subpoena, court order or search warrant. We only charge to recover some costs, and these reimbursements cover only a portion of the costs we actually incur to comply with legal orders.

While we do not charge in emergency situations or in other exigent circumstances, we seek reimbursement for all other legal requests in accordance with the following schedule, unless otherwise required by law:

Initial search of up to 25 identifiers: Free
Production of subscriber information/data for up to 5 accounts: Free
Production of subscriber information/data for more than 5 accounts: $20 per account
Secondary searches: $10 per search
Data preservation
We will take steps to preserve account records for up to 90 days upon formal request from U.S. law enforcement in connection with official criminal investigations, and pending the issuance of a court order or other process.

Submitting requests
Please serve requests to:

GitHub, Inc.
c/o Corporation Service Company
2710 Gateway Oaks Drive, Suite 150N
Sacramento, CA 95833-3505
Courtesy copies may be emailed to legal@support.github.com.

Please make your requests as specific and narrow as possible, including the following information:

Full information about authority issuing the request for information
The name and badge/ID of the responsible agent
An official email address and contact phone number
The user, organization, repository name(s) of interest
The URLs of any pages, gists or files of interest
The description of the types of records you need
Please allow at least two weeks for us to be able to look into your request.

Requests from foreign law enforcement
As a United States company based in California, GitHub is not required to provide data to foreign governments in response to legal process issued by foreign authorities. Foreign law enforcement officials wishing to request information from GitHub should contact the United States Department of Justice Criminal Division's Office of International Affairs. GitHub will promptly respond to requests that are issued via U.S. court by way of a mutual legal assistance treaty (“MLAT”) or letter rogatory.

Questions
Do you have other questions, comments or suggestions? Please contact GitHub Support.

Did this doc help you?
Privacy policy
Help us make these docs great!
All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.

Or, learn how to contribute.

Still need help?
Ask the GitHub community
Contact support
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
Developer API
Training
Blog

---
## [Blaster4385/IllusionX_sm8250](https://github.com/Blaster4385/IllusionX_sm8250)@[ff9a972ebb...](https://github.com/Blaster4385/IllusionX_sm8250/commit/ff9a972ebbf611005988c3cfe45f1fe9386d77d0)
#### Sunday 2022-01-16 17:53:49 by alk3pInjection

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
## [alkogenius21/GAME](https://github.com/alkogenius21/GAME)@[9cc8960ac6...](https://github.com/alkogenius21/GAME/commit/9cc8960ac68d039e9f46ea55011cecda434e53b6)
#### Sunday 2022-01-16 18:59:05 by alkogenius21

Revert "Fuck you bitch"

This reverts commit 98fcbe0767022caf2cd3aba9cc862b2024f552e6.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9036d618d1...](https://github.com/mrakgr/The-Spiral-Language/commit/9036d618d1c2f191969282bc97075e818df33509)
#### Sunday 2022-01-16 19:35:40 by Marko Grdinić

"11:15am. I am up. I did in fact manage to go to bed earlier yesterday. And it seems I did fall asleep and get up earlier. In fact, I woke up really early, but luckily managed to fall into deep slumber and got some additional necessary high quality rest. Let me chill a bit and I will start.

11:50am. Done with chilling. Let me finish reading the article and then I will start.

12pm. Let me play a bit with Blender. I want to try drawing the petal again. The way I connected the geometry I could have done more efficiently. I have some ideas and want to test them.

First let me try the grid fill.

12:20pm. Oh, the grid fill is great, but the vertex extrusion fill tool from F2 is crap.

Rather than doing it like this though, what if I started with a subdivided plane and pushed thing into place with the grab brush?

12:30pm. I tried making a heart shape with the grab brush and the results are quite impressive. Since I am smoothing it out with the smooth brush, the resulting 2d plane has extremely good topology. This is more than what I expected. If I knew things would be like this, maybe I would have done the flower petals using this method. It is much faster than the modeling method.

12:40pm. I am reflecting on this experience. So far I haven't seen it being done this way, but during retopo instead of using the modeling tools to put the quads in the right places, imagine instead duplicating the mesh and then using the remesher to create the initial surface of quads. And after that going in with the grab tool to push them into place. That could be good.

So far the only retopo that I've seen is by Flycat, and he painstakingly puts every quad into place. I am not sure what to think about that.

Even without a remesher I'd favor using broader strokes.

I should watch the longer video by FlipperNormals on how they do it from start to finish.

12:45pm. I also want to know more about the addons. I think there was an addon for doing things like cutting holes, it caught my eye in a /3/ infographic. But I forgot what its name was.

I'll want to watch a video on the loop tools.

12:50pm. Let me stop reflecting here, and I will start the day for real. First come chores, after that breakfast. After that I'll watch vids for a bit, and get to work on distributing the flowers.

1:50pm. Done with breakfast and chores. Let me start.

First how about the loop tools?

https://youtu.be/W2MjvKy1yCo
Loop Tools Addon | Important Mesh Editing Tool | Blender 2.8

https://youtu.be/su9qqpdVjsU
TOP 20 Add-Ons Built In to Blender 3.0! (ALL FREE!)

Let me watch these two. It should be a good way to start the day.

https://youtu.be/W2MjvKy1yCo?t=90

Ohhh...

That could be a use for the circle tool, yes.

https://youtu.be/W2MjvKy1yCo?t=134

Ohhh, I've been trying to do this with grid fill and regular fill and it did not work. So this how it could be done.

https://youtu.be/W2MjvKy1yCo?t=203

This is really impressive.

https://youtu.be/W2MjvKy1yCo?t=275

This tool is wondorous. I really like this.

https://youtu.be/W2MjvKy1yCo?t=334
> It is quite a clever tool and this used to be an old style of modeling.

2pm. I'll definitely keep the tool in mind. Let me watch the second video.

https://youtu.be/su9qqpdVjsU?t=294

Didn't expect this one.

https://youtu.be/su9qqpdVjsU?t=438

I tried Stored Views in the last two days, but am getting errors with it.

https://youtu.be/su9qqpdVjsU?t=518

MeasureIt is something I should be using.

https://youtu.be/su9qqpdVjsU?t=570

Hmmm, interesting. I suppose there are alternative to geometry nodes in Blender.

https://youtu.be/su9qqpdVjsU?t=833

Terrain generation.

https://youtu.be/su9qqpdVjsU?t=892

Tree generation. It has a lot of different kinds of trees.

https://youtu.be/su9qqpdVjsU?t=1098

Node wrangler has the change math operation keys. I should make use of those in the future.

2:35pm. Am just chilling. What I need to do next is figure out how to use vertex weigths to distribute objects.

But before that I should try out seeing if the hair system works with geo nodes.

2:55pm. Had to take a break. Let me resume properly.

Right now I am trying out the hair stuff.

https://blenderartists.org/t/hairs-geometry-nodes/1336677/10

https://youtu.be/CL5gWQ0Wxaw?t=6

This is really impressive.

What strikes me is how fast this is. He is using just a single curve to do it.

I need to think about this more.

https://youtu.be/GOOHn83BYCI
Why Sculptors SUCK at Drawing! | Sculpting Zero Two in 3D [Darling in the Franxx]

I got baited by the title. Let me watch it since it is only 8m.

https://youtu.be/db7Xfg_oSYE
Every way for creating hair in blender 2.9+ (Curves, Particle, Hair Cards, Modeling, Sculpting )

https://youtu.be/yifhqPF4vu0
Sculpting Fur in Blender (with Alphas)

https://youtu.be/bFV0y2-g1Kk
How To Create A Realistic Shaggy Carpet In Blender

Then I will watch these three.

Let me do some studying today. Then I'll distribute the flowers. Most likely I'll just turn the hair particles into a mesh and then use geo nodes on them, but this is a great time to study this subject especially since I will be making hair for Luna.

3:20pm. It was fun, let me watch the other 3.

https://youtu.be/db7Xfg_oSYE?t=29

Ohhh, how did he do the thing with the planes? I must know that. It looks very realistic.

https://youtu.be/db7Xfg_oSYE?t=211

Ahhh, it is actually possible to change the radius by scaling an individual point. I see.

3:30pm. Let me pause. I want to try out carver. I'll also add the curve tools tutorial to the mix.

https://youtu.be/gQSes0hztnY
Amazing CURVE TOOLS in Blender with the Extra Curves Add-On - FREE Add-On!

Huh, how do I use carver? Ah, I press Ctrl + Shift + X. The tool is complex and I'd need a tutorial in order to be able to use it first.

Now, what the hell, let me get the curve tools tutorial out of the way.

Nevermind this, it just has a bunch of different curves.

Let me get back to hair.

https://youtu.be/db7Xfg_oSYE?t=1197

I hate this kind of fiddling around.

4:10pm. Done with the video.

I am not sure what to think. Using curves seems to be the best bet so far. Let me watch the rest of the vids.

https://youtu.be/yifhqPF4vu0
Sculpting Fur in Blender (with Alphas)

Let me watch this.

https://youtu.be/yifhqPF4vu0?t=195

What is this fast navigate option?

4:35pm. https://youtu.be/yifhqPF4vu0?t=935

I've been thinking of something like this for hair. No doubt there is a hair texture somethere that I can use for sculpting. Either that or displacement maps. I am not happy with any of the tutorials that I've seen so far.

https://youtu.be/yifhqPF4vu0?t=997

if he went wrong anytwhere, that would be not duplicating the textures as he went along. By that I mean, remember when I did the tire tracks? You create one, duplicate it, duplicate that, duplicate it again and get 8 tire tracks. This is a lot better than trying to hack it by hand. What is what this guy is missing.

4:40pm. FInally, let me go for the last tutorial which is on carpets. I hope it won't be another particle system tutorial.

4:45pm. No it is just more particle system stuff.

https://youtu.be/-AuhTsKW68Q
Trying out Blender? make sure you enable edit mesh tools

Let me watch this.

https://youtu.be/-AuhTsKW68Q?t=441

Meh. Most of these are already in Blender as it is or could be done in two steps using other tools.

https://www.youtube.com/results?search_query=blender+hair+geometry+nodes

Let me check this out for a bit more.

https://youtu.be/b4SksL2wc1E?t=110

How did he do that?

5:05pm. This video is from the time the geo nodes were in beta. I am looking at the distribute points on faces node and wondering how I could attach the vertex group data. It has selection and it has density, but I do not know how to make use of that.

https://docs.blender.org/manual/en/3.0/modeling/geometry_nodes/point/distribute_points_on_faces.html

The docs don't give any advice.

5:10pm. Huh, I don't know. Google is not helping me here.

Let me finish watching the video and then I'll think about it. Maybe I'll ask on SO. Maybe I'll watch the donut tutorial.

https://youtu.be/4WAxMI1QJMQ
Blender 3.0 Beginner Geometry Nodes Tutorial (Donut part 9)

I have no idea. Let me give this a shot.

5:20pm. Oh, I see that 20m in he is doing some weight painting. Let me skip to that.

https://youtu.be/4WAxMI1QJMQ?t=1163
> Double pi is tau.

I had no idea. Lol. Ok, I'll watch your video all the way through.

https://youtu.be/4WAxMI1QJMQ?t=241

Agh, I did not even notice the pin icon.

Actually, I am a bit interested in how he did the icing. I'd use a shrinkwrap, but that would end up squashing the other side. Maybe shrinkwrap + solidify in that exact order? But if had to use pure scuplting, I am not sure how I would do it.

https://youtu.be/4WAxMI1QJMQ?t=1359

Now he will explain how to use weight groups. This is what I'll need to distribute the flowers.

https://youtu.be/4WAxMI1QJMQ?t=1383

Ahhhh, I see.

https://youtu.be/4WAxMI1QJMQ?t=1515

Oh, it is possible to fix the clipping. That is interesting. I didn't expect this would be possible. Though I really should have anticipated it given that I've read the manual page for the node.

https://youtu.be/4WAxMI1QJMQ?t=1809

I expected him to do an exponential node.

https://www.poliigon.com/search?credit=0&page=2

It doesn't have much free.

https://youtu.be/7wKnPclzYY8
Blender 3.0 Beginner Modifiers Tutorial (Donut part 3)

Let me just check out how he does the icing.

https://youtu.be/R1isb0x4zYw?t=6

I'd really want to be able to sculpt rocks like these. I'll have to learn that at some point.

https://youtu.be/R1isb0x4zYw
Blender 3.0 Beginner Modelling Tutorial (Donut part 4)

Ah, let me watch this as well. I am in this kind of mood.

6:15pm. Time for lunch. I overdid it with the tutorials today.

6:25pm. Done with lunch. Let me resume. I am done with the tutorials. I really needed to figure out how to bring in the density attributes, but I think I'll just use the hair system to generate some curves and turn it into a mesh.

6:35pm. I am looking at textures and brushes for hair. BlenderKit has some stuff for fur as well as hair brushes.

Enough of this. Forget it for now. I really hate anything having to do with hair in Blender.

Let me do a little review.

Today I did learn quite a bit about various addons as well as some basics like how to make use of density in geo nodes.

But as for watching these basic tutorial by Blender Guru (he is quite good at them) I am mostly getting the confirmation that I understand Blender well enough now. I try to anticipate what he will do and for the most part I am right.

This is pretty good.

6:45pm. In that creature tutorial, I wonder how it was possible to light up specific fur parts of the fur? Would that be possible without going over the vertex groups by hand? I'll leave finding that out for later.

When it comes to doing thing like hair, I'll look into making my own brushes if what I find online is not appropriate. It won't be hard.

6:50pm. Before I proceed forward, just how is it possible to turn a curve into a mesh? The problem with geometry nodes is that they give me an error when I try to apply them. It is extremely annoying.

I guess it wants me to convert it to a mesh first. But, then how do I keep the curve profile?

No, I do not think it is possible. This is probably a limitation that will be lifted in the future.

7pm. Focus me. At this point it is 7pm, and I'd rather just stop for the day here. When watching tutorials there is always the risk of spending the entire day doing it, and that is what usually happens when I do it. I could take off here and chill. But let me at least finish the flower. I set up everything yesterday, what I need to do is make it all procedural.

7:10pm. Huh, how do I get the rotation of the last point. This is what I need for the bulb.

7:20pm. The answer is to capture the attribute. Once you turn the curve into points the endpoint selector ceases to work.

7:25pm. I've got it. Now it looks similarly to a rose with no thorns. On to the next step. I'll link to this geo node in the other file.

8pm. Sigh, going from hair particles to geometry nodes sucks more than I ever would have imagined. Initially I did 1k flowers and that pushed the vertex count to from 1m to 7m, enough to slow down my rig noticeably.

I am not benefiting from the particle edit mode as much as I thought I would and it is really getting in the way of making quick edits.

Ok...I am going to avoid particle systems entirely. I'll focus with what I can do with just geo nodes. That will simplify things. I think I'll also get rid of the subdiv modifiers on the leaves and the bulbs. They are clearly impacting the scene badly. I need to resample the curve to a lesser degree as well.

Rather than it being straight up, I'll really want to adjust the curvature a bit. Maybe I should randomize the position of the final endpoint. That could do the trick. As well as make the flowers 2-3x bigger.

8:15pm. Let me stop here for the day. Today I did various things and learned a bit.

8:25pm. Tomorrow, I am going to put my plans into action. I am going to ditch the tree and go with vines around a wireframe plan. It is more thematically fitting for the kind of flowers that I have here. Originally when I envisioned the scene, I though of Luna looking upwards through the tree branches. Maybe I would have gone with that had I known about the tree generator, but I'll go with the giant flower vines for this scene.

I know if I can do this right, than the follow up scenes will be much easier as I will have the necessary experience to do it more smoothly. For now I just need to keep on trucking. Once I break the ice completely I will be fully on the path to mastering 3d art. If you look at even just the donut tutorial by Blender Guru, there is a lot of complexity to all of this. It is one thing to just follow him, but I doubt many people would be able to do it right off the bat. I am just at that level where I could.

I need to do it. I need to master this. If I could master this, any kind of art will be within my ability.

In 2023 whether it be games, VNs, or anything else, I will be able to do them without an issue."

---
## [JohnFulpWillard/KirieStation](https://github.com/JohnFulpWillard/KirieStation)@[a728992ffd...](https://github.com/JohnFulpWillard/KirieStation/commit/a728992ffdcbe203b8305eee5481fc00c3890c18)
#### Sunday 2022-01-16 19:44:50 by DaddyIssues98

Make special area for the bathroom ruin. (#439)

* im going to curse this server for the rest of his life.

I just killed a man like I'm the impostor from Among Us
Yeah, Yeah
Now my hands are red, I guess Im sus from Among Us
I just got my driver's license and I crashed a school bus
I just saw a man vent, now its time for us to discuss
Red Sus!
So she tryna suck my dick
But I'm a minor, diamond pick
I beat that bitch off with a stick
I melee that bitch with a kick
I laugh my ass off pickle rick
I eat my rice with a chopstick
The doctor called me lunatic
I light that bitch up, candle wick
I pull up with an M9
Yeah, its mine
Play Among Us, Among Drip
With my slimes
Keep a watch all on my wrist
At all times
Eat froot loops with a lime
Among Drip, you know Dior
Your mom's a whore
Call a meeting, Civil War
Drop these losers to the floor
Eat humans, not Vore (what the fuck)
Reactor melting to the floor
(The code is 2214)
The code is 5 digits, not 4
Kinda sus
(What the fuck did I just record, holy shit)

* kay

* duck

---
## [zytops-dev/test-site](https://github.com/zytops-dev/test-site)@[fea3e60fec...](https://github.com/zytops-dev/test-site/commit/fea3e60fec9b2f802e0b8923265f760ac0115b5d)
#### Sunday 2022-01-16 20:16:37 by zytops-dev

I SWEAR TO FUCKING GOD

THIS SHIT BETTER FUCKING WORK

---
## [polygoblyn/MonkeStation](https://github.com/polygoblyn/MonkeStation)@[040b7ff839...](https://github.com/polygoblyn/MonkeStation/commit/040b7ff839d51d4db2ce1747f92312e0925bccd2)
#### Sunday 2022-01-16 20:49:47 by Zonespace

Adds Flavor Text (#48)

* lgtm

* aaaAAAA

* might be better idk

* flavor-examine

* info

* haaa fuck you github

---
## [UConn-AI-Club/uconn-ai-club.github.io](https://github.com/UConn-AI-Club/uconn-ai-club.github.io)@[5302e011c2...](https://github.com/UConn-AI-Club/uconn-ai-club.github.io/commit/5302e011c2a8436d69e2cce7e0e53df42701139f)
#### Sunday 2022-01-16 22:05:05 by m4nik1

Added Components, CSS, Pages for organization and created page files also wired the website to go straight to Homepage also (Fuck you Ronak)

---
## [UConn-AI-Club/uconn-ai-club.github.io](https://github.com/UConn-AI-Club/uconn-ai-club.github.io)@[e162785162...](https://github.com/UConn-AI-Club/uconn-ai-club.github.io/commit/e1627851626c0951931b607aee0026732b900169)
#### Sunday 2022-01-16 22:18:03 by m4nik1

Added CSS, pages, component folders and added navigationbar file also Fuck you Ronak

---

