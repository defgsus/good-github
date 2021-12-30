## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-29](docs/good-messages/2021/2021-12-29.md)


1,609,390 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,609,390 were push events containing 2,231,422 commit messages that amount to 155,299,256 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [tdauth/wowr](https://github.com/tdauth/wowr)@[1df66e0e43...](https://github.com/tdauth/wowr/commit/1df66e0e434acdc660111b68e0b4ca3f8e7cbbef)
#### Wednesday 2021-12-29 00:32:25 by barade

1.9.3

- Increase number of respawn groups to fix missing respawns of creep bosses.
- Add The Burning Legion and Bosses to the player stats multiboard.
- Show level of Evolution in player stats.
- Show player stats multiboard from start but minimized.
- Rename AI players to AI.
- Increase gold of housings to 100 000.
- Add lost units and technologies to player stats.
- Fix tooltip of Improved Lumber Harvesting for Furbolgs.
- Hide Blood Elf Cage model on death.
- Increase number of farms and workers for Naga and Furbolg AI.
- Add quest log entries Hidden Bases and Hero Journey.
- Add Mountain Giant to tavern.
- Kil'Jaeden, Tichondrius, Eredar Warlock and Keeper of Frostmourne cost food now.
- Rename Ogrimmar to Orgrimmar for several heroes.
- Furbolg Tribal Center, Green Dragon Roost, Pig Farm and Dragon Roost require ground-pathable to be built now.
- Dragon Roost for Orcs costs 200 gold now.
- Fel Peon cost as much gold as regular Peons now.
- Keep Tier 2 XP bonus on repick and for second hero.
- Add many missing heroes to hero equivalents in the gameplay constants.
- Only show VIP welcome message if VIPs are enabled.
- Remove votes for leaving players from the votings in the beginning of the game.
- Add Goblin Laboratory and Black Market to many more start locations to make the game more fair.
- Add entry by the Ocean to Sunstrider Isle.
- Add black borders on the Ocean to Outland.
- Add quest log entry for the stats multiboard.
- Reduce quest log entries to Special Race Building.
- Reduce costs of Improved Power Generator.
- Add ability Drop all Items to Backpack.
- Add research Improved Mount which increases the movement speed of your mount.
- Add research levels to the tooltips of different researches with 100 levels.
- Fix icon of Unique - Legion´s Hate.
- Rename quest log entry "New Features" to "Reforged Version" and move it down.
- Fix icon of Engineering - Adept.
- Reduce collision size of Souls.
- Give Archimonde bonus hero Bash of Eredar Warlock.
- Add Neutral Shop which can built by Neutral Citizens and sells Orbs.
- Add names of VIPs to the VIP room.
- Reduce stock initial delay for Neutral Citizens to 0.
- Fix Orgrimmar name in floating text.
- Translate tooltip of Illidan´s Blade back into English.
- Add "-suicide" chat command description to quest log entry Hero Death.
- Allow Pickpocketing on The Burning Legion and Bosses.
- Fix values of RaceUndead and RaceNightElf.
- Increase number of levels of War Stomp from Tauren Chieftain from 3 to 12.
- Reset Naga building HP to the original values.
- Fix completing Lich King Quest 4.
- Add some missing tooltips for bosses.
- Add Nether Dragon boss to tavern in Outland.
- Fix icon position of Rain of Chaos of Book of Summoning Pedestal.
- Make Book of Summoning Pedestal a building, add pathing and requires ground-pathable.
- Drop legendary and quest items on Boss and The Burning Legion hero deaths, too.
- Ping only visible allied heroes with "-pingh".
- Add chat command "-pingl" to ping legendary artifacts on the ground.
- Remove Forgotten One from Paladin bosses.
- Give Paladin bosses orbs, so they can fight air units.
- Give Dreadlord and single Paladin bosses orbs, so they can fight air units.
- Add missing food costs and tooltips to Boss heroes.
- Boss heroes as second heroes require level 60 now.
- Add missing icon and tooltip texts to Life Steal from Nether Dragon.
- Respawn creep groups also when a creep changes the owner (not only death).
- Increase array sizes of respawn groups, rects etc. for creep respawns which will avoid bugs.
- Count exact number of respawn groups for certain groups to reduce the number of loop calls.
- Try to fix respawning heroes of creep groups by adding them with the exact member index.
- Add hero level 50 requirements to all heroes for Taverns.
- Add Wizard to Tavern heroes.
- Classify Fortified Hideout as Town Hall.
- Clear hero equivalents list to make all heroes equal.
- Add cheat "-share" for better testing.
- Spend unused skill points of bosses on their hero abilities.
- Change colors of Keeper of Frostmourne to boss colors.
- Fix tooltip values of item Unique - Mask of Death.
- Change order IDs of Freelancer Summon Mercanaries to avoid conflicts with abilities.
- Fix Freelancer AI hero start locations.

---
## [Stevanus-Christian/terminal](https://github.com/Stevanus-Christian/terminal)@[f2ebb21bd1...](https://github.com/Stevanus-Christian/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Wednesday 2021-12-29 02:03:20 by Mike Griese

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
## [tensorflow/probability](https://github.com/tensorflow/probability)@[9b67e5abdd...](https://github.com/tensorflow/probability/commit/9b67e5abdd31840b33d17f106a275fca017827ef)
#### Wednesday 2021-12-29 02:46:25 by Dave Moore

Port `make_trainable` to use new state utilities, and add a stateless version w/ JAX support.

The change to make_trainable itself is minimal. A couple of issues that came up:

1. Stateful trainable distributions are now DeferredModules, which 'quack like' distributions, but break a few `isinstance` checks that I had to update. (thus illustrating the perils of `isinstance` checks).

2. How should we distinguish stateful/stateless functions in the API? Some options:
a) Keep both functions in the same module, with a `_stateless` suffix for the stateless version. (what I've done here, and what we did with tfp.math.minimize_stateless)
b) Put stateless versions in their own submodule, e.g., `tfp.experimental.vi.stateless.make_trainable`.
c) Put both stateful and stateless versions in their own submodules, with a top-level wrapper that points to the stateless versions under JAX and the stateful versions under TF. (this is too magicky IMHO).

Various other things are possible too. I don't think the choice now is *too* critical since it's still experimental, but lmk if you have strong feelings.

3. It's a pain to specify docstrings for both the stateful and stateless versions. I ended up writing a 'base' docstring for the generator, and then using replacement magic (some substitutions here, plus the stuff in trainable utils that converts 'Yields' to 'Returns' and adds the 'seed' kwarg to the stateful builder docstring) to generate the stateful and stateless versions. I don't love this, but at least it kind of works.

PiperOrigin-RevId: 418707747

---
## [ncrecc/jumper4real](https://github.com/ncrecc/jumper4real)@[0c3bd199ab...](https://github.com/ncrecc/jumper4real/commit/0c3bd199ab02ada62e29003e797b87c32764049b)
#### Wednesday 2021-12-29 03:19:16 by wibi

help i'm stuck in a newline debate
FUCK

editor and whatnot checks for LF instead of CR LF now because when people download the files from github the CR LF becomes LF even though git bash internally forces LF to CR LF???

aaaaa fuck you comp sci just use one fucking type of newline

---
## [auchtopus/CPSC_434_Final_Project](https://github.com/auchtopus/CPSC_434_Final_Project)@[2b6d99d5a6...](https://github.com/auchtopus/CPSC_434_Final_Project/commit/2b6d99d5a64fbbbf7275ab37562ac0848ea9748b)
#### Wednesday 2021-12-29 04:10:28 by Anthony Jiang

It's all just so fucked

1. accept should be blocking; need to think of a way to implement that or develop a means of rationalizing making it not blocking.
- the issue is that a) if the syn comes in before the acceopt, this approach is okay
- if the syn comes in after the accept, we are in trouble because we need to set a state variable

However, the bigger problem is the semantics.

accept is supposed to
1. be blocking
2. return the newly created socket for listening on the 4-tuple.

our accept is a) nonblocking (will return immediately regardless of whether the underlying thread has actually accepted) and b) returns the original socket. This is because we create new TCPSocks in threads (because we did not think far enough to use selector/multiplexer) so we are stuck with TCP connections in individual threads. To implement this feature requires the implementation of a blocking accept; without a blocking accept, you will not necessarily be able to return the copleted socket. \

The "slack" -- delay for receiving a message is picked up by the server code, where we use an infinite loop and the write function that can safely return 0 if no bytes can be read.
We will effectively return 0 until the connection is fully accepted on the listensock//now mp connection 1

---
## [L0KH1/NumpyNeuralNet](https://github.com/L0KH1/NumpyNeuralNet)@[5b2b187894...](https://github.com/L0KH1/NumpyNeuralNet/commit/5b2b187894d70ad63a3bb35518ac143ee616bf13)
#### Wednesday 2021-12-29 04:43:13 by Loki

About to kiss the homies goodnight and then remembered that all my homies hate DS_Store. No more nightmares - gang gang.

---
## [Honkers-the-clown/tgstation](https://github.com/Honkers-the-clown/tgstation)@[bfa1542009...](https://github.com/Honkers-the-clown/tgstation/commit/bfa1542009aa7fecbe0e50aef9561b49a4874448)
#### Wednesday 2021-12-29 04:53:30 by Cimika/Lessie/KathyRyals

Felinids don't like getting sprayed with water. (#59506)

This PR is an ode to @Ryll-Ryll, who inspired me to try and find fun, silly things to PR to try and make people smile.
About The Pull Request

Felinids now get a SMALL and SHORT mood debuff when getting sprayed with water. The intent of this PR is not to provide content to grief felinid (flashback to the "Felinids hate water" pr), but rather to provide a funny interaction.

Bonus point (Suggested by Ninja) : Getting sprayed with water interrupts do_after. Felinid climbing on your table ? Pssshttt. Straight in the face.

PR with permission from @ninjanomnom
Why It's Good For The Game

Light-hearted fun and a bit of flavour to felinids.
Changelog

cl
add: Felinids don't like getting sprayed with water.
code: Adds a new status effect, incapacitated, which causes your do_afters to stop.
/cl

---
## [Rbon/emacs.d](https://github.com/Rbon/emacs.d)@[23ecb23c82...](https://github.com/Rbon/emacs.d/commit/23ecb23c82746f6c41b68d53b644939cecb6bfc0)
#### Wednesday 2021-12-29 05:07:32 by Robin Bisho

Refactoring

I can't believe it was this easy all along. I just needed to LITERALLY
write (keymap). All this time, I thought the documentation for which-key was
using (keymap) as a placeholder for a map that I myself am supposed to
provide. NOPE. Just a magical sequence of characters. I should be angry that the
solution was right there in front of me, but honestly I'm just happy I finally
figured out what I was doing wrong after all these hours.

---
## [beartype/beartype](https://github.com/beartype/beartype)@[c18b896233...](https://github.com/beartype/beartype/commit/c18b896233d4573468f239c560a1cb1b81612950)
#### Wednesday 2021-12-29 07:23:13 by leycec

PEP 570 -- Python Positional-Only Parameters.

This commit adds full-blown support for [PEP 570 -- Python
Positional-Only Parameters](https://www.python.org/dev/peps/pep-0570).
Given the triviality, the rear view mirror of regret suggests we kinda
should've implemented this sooner. Better late than never, best
@beartype friends for life (BBFFL). (*Periodic periodontist trysts!*)

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[b2ba847c22...](https://github.com/carshalash/tgstation/commit/b2ba847c223dcbdc49c85a46156d5dbc28dbe5bd)
#### Wednesday 2021-12-29 08:14:48 by LemonInTheDark

Reduces the move delay buffer to 1 tick (#63332)

We've got this delay buffer behavior
Idea is basically, if we're just holding down the key, just keep adding to the old delay
This way, fractional move delays make sense

Was added in this commit 491bdac

When it was added, movement was triggered by verbs sent by the client
So we needed a big grace window to account for networking delay

Don't need that anymore cause we use keyLoop, so let's just cut it all the way down

Why?
Because right now if you somehow manage to input a move afer move_delay is up
but before the window runs out, you will be elidgable for a new move before you visually reach the tile

Got a dm from mothblocks about this last night, something about flash stepping? IDK I don't play here
Seems silly though, let's sweep this up

Oh and mothblocks owes me a pizza, please add this to the commit history so it can be certified as a part of the blockchain

---
## [AlecGoncharow/zeus-rs](https://github.com/AlecGoncharow/zeus-rs)@[e74e5c4c96...](https://github.com/AlecGoncharow/zeus-rs/commit/e74e5c4c96bc465fa6c1fa6d87d35d8d8979a789)
#### Wednesday 2021-12-29 08:15:15 by Alec Goncharow

Rewrite rendering flow and consolidate driver code

This is huge commit.

The main focus of these changes has to do with completely overhauling
the rendering process. Previously we were naively creating buffers every
frame for every draw call, as well as recreating bind groups every
`render()` call.

Ironically that is not what inspired me to rewrite the renderer, my main
inspiration was to untangle the resources and specifics of each render pass
from the render code itself so that it could be as agnostic as
reasonably possible to the details of each render pass.

The example I had run up on and I knew was due for a refactor is adding
a pass that draws water well, the problem is I would have to create all
these shaders and resources in the renderer proper, and at this point it
had already become and unwieldy 1k LoC mess, I could power through and
hope I wouldn't need any more passes, but it was clear I would be
artificially limiting my self if I hadn't done a major overhaul.

In order to accomplish this, I have iterated on the API several times
over the past day and a half, churning through the semantics of using
something that I call a `RenderWrangler`. This gist is that the Wrangler
will keep all the allocated resources that may need to be shared across
render passes, as well as the context needed to perform wgpu
RenderPass's via a new `Pass` struct. The new rendering process is much
more demanding of users of the `pantheon` API but offers as much
flexibility as possible in terms of twiddling with settings in `wgpu`.

The current code is nearly on par with the previous renderer's default
scene, it has everything except the lackluster shadow pass and the
texture pass that would just draw arbitrary textures. That being said,
comparing the performance across the 2 implementations of a scene with
the terrain and rotating cube provides some pretty awesome results.

Old Renderer debug
```
FPS: 392.70822, sample_sum 83.441086, MAX_SAMPLES 32768, average_tick 0.0025464199
```

Old Renderer --release
```
FPS: 1275.6854, sample_sum 25.686583, MAX_SAMPLES 32768, average_tick 0.0007838923
Iterate turnaround time: ns 2630
FPS: 1308.4719, sample_sum 25.042952, MAX_SAMPLES 32768, average_tick 0.00076425023
Iterate turnaround time: ns 2580
FPS: 1309.6519, sample_sum 25.02039, MAX_SAMPLES 32768, average_tick 0.0007635617
```

New Renderer debug
```
FPS: 1213.5828, sample_sum 27.001043, MAX_SAMPLES 32768, average_tick 0.00082400645
ignoring window event CursorEntered { device_id: DeviceId(X(DeviceId(2))) }
Iterate turnaround time: ns 10010
FPS: 1517.1993, sample_sum 21.597689, MAX_SAMPLES 32768, average_tick 0.00065910915
Iterate turnaround time: ns 9280
FPS: 1496.2098, sample_sum 21.900671, MAX_SAMPLES 32768, average_tick 0.00066835544
```

New Renderer --release
```
FPS: 4357.009, sample_sum 7.5207562, MAX_SAMPLES 32768, average_tick 0.00022951527
ignoring window event CursorEntered { device_id: DeviceId(X(DeviceId(2))) }
Iterate turnaround time: ns 2440
FPS: 4234.6157, sample_sum 7.738128, MAX_SAMPLES 32768, average_tick 0.00023614893
Iterate turnaround time: ns 2390
FPS: 4336.935, sample_sum 7.555566, MAX_SAMPLES 32768, average_tick 0.00023057757
```

These are some figures I captured after ripping out the passes not found
in the current implementation out of the old renderer, and it is quite
an impressive speed up. Beyond that the new implementation will scale
much better as new things are drawn, where as the old one would add
additional overhead of creating a buffer every frame, barring some very
careful buffer reuse.

So in effect we now have a more capable renderer, a more configurable
renderer, a better performing renderer, with the only trade off being
the user has to write the code they were already going to write but
outside of the engine rather than baked into it.

A side effect of this rewrite was that I would need my `core` crate to
be much closer intertwined with the rendering details but since the
server would need to know how to make these as well I figured it made
sense to join these into the `game` crate, renaming the `game` source to
be a `mod client` and since `core` is already a module in rust, it got
renamed to `mod base`.

The major additions to the `game` crate outside of pulling in the
`base` and `server` modules is the `mod rendering` in `client` this
module will be where the unwieldy mess of initalizing render pass
resources and any helper functions with interfacing with the `wrangler`
will live. I had considered putting the helper functions in `pantheon`
but couldn't think of a way of doing so without possibly running into
more of driver logic with library logic.

As it stands, the current model is for drawable entities to `register`
themselves with the `RenderWrangler` via the `rendering` module and by
doing so tells the `RenderWrangler` how to draw it in perpetutiy. The
entities have access to uniforms and push constants to modify how
they are drawn but the ability to overwrite the vertex data does not
exist at the moment, will revisit this when it makes sense.

I am still energized to keep working on this and get to adding new
render passes but I know that those changes don't fit the spirit of
this branch so I am setting my flag down and saying "close enough to a
render graph for my purposes" and hitting the save button before I get
to the fun parts.

---
## [lngchensh/826](https://github.com/lngchensh/826)@[6ae425555a...](https://github.com/lngchensh/826/commit/6ae425555ac8877d0fce2ee605b84689787e2743)
#### Wednesday 2021-12-29 08:18:11 by lngchensh

Create README.md

The Justice Department sued Mr. Bannon in connection with his friend Guo Wengui. 'Xi Guo' is at the cusp of evil deeds; there comes the catastrophe with horror.


Bannon, 67, was indicted by a federal grand jury on two counts of contempt of Congress related to his refusal to testify and his refusal to provide documents for failing to comply with a subpoena before a House select committee on January 6, the Justice Department said on Friday. Bannon's indictment which spread like wildfire, is bound to hit his gay friend Guo Wengui. Recently, Bloomberg mentioned the connection between Guo Wengui, Air Coin, and Bannon. You can't be lucky to be around Guo, and you will get hurt for connecting with Shit Bannon. Now is the time for investors whom Cheater Guo has cheated to report his violations.

After Trump removed Bannon, letting Bannon without a place to rest, Bannon happened to meet Guo Wengui, who had no political asylum ，handed over the 'pillow.' Then, the two allied. They have lovely time since then. But Bannon, a white supremacist who has remained loyal to Trump from the White House, did his best to keep him in office, inciting the January 6 storming of Congress, and so far, the evidence is clear. To support Bannon and give Trump, who Guo Wengui thinks will surely win the re-election, a good impression, in addition to increasing the chance to get political asylum, Guo put his all eggs in one basket. He ordered Luther and Bannon, a group of 'Ants' gangs, such as Xia Chunfeng and more than ten others, to attack the Capitol building, among which "Sister Liu" was wounded in the leg by a rubber bullet from the riot police. Cameras capture all these. In short, Once Bannon's assault on the Congress case is found guilty, Guo Wengui is destined to be punished by the law.

With a good friend, Guo Wengui naturally overjoyed, since the beginning also ushered in the highlight of Guo's scam moment. Therefore, in terms of importance, Bannon to Guo Wengui is delicious to eat and a pity to discard. To be sure, Bannon is not xisi Xiao Ge, Gong Xiaoxia, Guo Baosheng, Zeng Hong, and other minions. His name is a life-saving straw, and he is a great helper in self-promotion and in promoting recognition of Guo's deception. As everyone knows, Bannon did his best for Guo Wengui in establishing the New Chinese Federation, the fraudulent donation of the legal foundation and the legal society, the fraud of G-series, and the publicity of Xi coins. Bannon worked so hard. How could Guo not reciprocate? So he gave Bannon a luxury yacht for enjoying and served Him with good wine and food. Bannon was pleased about this, and Bannon's nephew also became a designer of Gfashion. Reputedly, Guo Wengui recently announced that Bannon's eldest daughter would train the national Defense Force. There is always another side to the story. With Bannon's mess on the surface, the dirty scams like G-series, Coin, Newgettr, The Legal Foundation, etc., will no longer be covered by them. And with Bannon's indictment, 'Xi Guo' built by Guo Wengui will be in jeopardy.

Mr. Guo was involved in two counts of contempt of Congress against Mr. Bannon. Guo Wengui, Giuliani, Bannon, and others are deeply engaged in discrediting President-elect Joe Biden. That is the malicious arrangement of Henry Biden's 'Hard Disk gate.' This initiator is Giuliani, promoted by Bannon, Guo Wengui, and 'Big Ant' Lude. The FBI raided Mr. Giuliani's home in April, and there were signs of that before then. Although Guo Wengui ordered to take down all the videos on Gnews, the evidence was already there. Moreover, many Former Trump associates, including Bannon, Giuliani, and others, are still nominally on Guo Wengui's payroll. Therefore, once the Biden family cares about the 'Hard Disk Gate,' Guo Wengui will surely suffer revenge. What's more, it's not just a smear on private reputations. Like the assault on Capitol Hill, 'Hard Disk Gate' is hard evidence that foreigners meddle in American elections, a federal crime. So, as Bannon falls into the law, his ally, Guo Wengui, will naturally be punished.

In addition, after Trump's demise, Guo Wengui still grudgingly invited the former president to join The New Gett. Whether the intention is to promote New Gett, defraud, gain political patronage in the future, or enhance one's status, it is a significant fault and courting death. Now, the Biden administration is bound to overthrow Bannon. The reason is that Biden does have the purpose of crushing Trump and preventing the latter from making a comeback. Deliberately acts as a warning to the opponent. Beat the enemy through another man. Trump will face a punch, so will Guo Wengui, related to Trump, have a good life?! In short, Guo Wengui, who has already been Mired in the vortex of the Democratic and Republican parties in the United States, has no way to extricate himself, and the opportunity to get out has been completely lost. He will await his doom.

In short, because of Bannon, Guo Wengui was into the 18 layers of hell, ultimately could not turn over. Bashing Guo, by contrast, will get bad luck, but at least there is the hope of redemption. You victim who cheated by Guo，Guo Wengui fraud factual evidence is in the rule of law foundation, G-series, Xi Coin, New Gett. Only We determined and report, prosecute Guo Wengui now is the right way. Why don't we all take action now?！

---
## [ZeqaNetwork/PocketMine-MP](https://github.com/ZeqaNetwork/PocketMine-MP)@[d9c70cb176...](https://github.com/ZeqaNetwork/PocketMine-MP/commit/d9c70cb176c25bd67f7cab384428d6a9165f4539)
#### Wednesday 2021-12-29 10:49:44 by Dylan K. Taylor

start.cmd: prevent idiotic behaviour when paths contain characters such as brackets
god I hate this shit so much

---
## [angolon/aoc2021](https://github.com/angolon/aoc2021)@[3f31ec5daa...](https://github.com/angolon/aoc2021/commit/3f31ec5daacf963abc5e79f80c942ccf2cdff129)
#### Wednesday 2021-12-29 11:34:28 by Angus Gerry

Giving up on my shit and writing some god damned tests.

---
## [Inesteem/LoggerParser](https://github.com/Inesteem/LoggerParser)@[d3a513438d...](https://github.com/Inesteem/LoggerParser/commit/d3a513438dd7f5cb7dcb6ae12454668676fb785b)
#### Wednesday 2021-12-29 11:38:21 by Judith Hemp

holy fuck, just implement this fucking shit in python - fuck you, java

---
## [EgorDinamit/KirieStation](https://github.com/EgorDinamit/KirieStation)@[0b5947a20f...](https://github.com/EgorDinamit/KirieStation/commit/0b5947a20f2f218ad0e3f972add1e6ea5a90a9b5)
#### Wednesday 2021-12-29 11:55:34 by Kirie Saito

6 MONTHS. SIX FUCKING MONTHS OF THIS CRAP I FINALLY FIXED IT (#376)

FUCK YOU

---
## [metabase/metabase](https://github.com/metabase/metabase)@[2a6d813340...](https://github.com/metabase/metabase/commit/2a6d813340971fffcab8e6978d807f7daaf11edc)
#### Wednesday 2021-12-29 12:56:04 by dpsutton

Relativize links when emitting html from md in pulse/subscriptions (#18428)

* Relativize links when emitting html from md in pulse/subscriptions

Helpful links:
- https://awesomeopensource.com/project/vsch/flexmark-java
- https://github.com/vsch/flexmark-java/blob/master/flexmark-java-samples/src/com/vladsch/flexmark/java/samples/PegdownCustomLinkResolverOptions.java
- https://github.com/vsch/flexmark-java/blob/8a881b73109a287b5f202e2e1fc9f9c497d5eecf/flexmark/src/main/java/com/vladsch/flexmark/html/HtmlRenderer.java#L433
- https://github.com/vsch/flexmark-java/blob/8a881b73109a287b5f202e2e1fc9f9c497d5eecf/flexmark/src/main/java/com/vladsch/flexmark/html/renderer/ResolvedLink.java#L10

This was a pain in the ass. I had been looking for a way to just easily
traverse the ast, but this might cause problems since there are spans
and text positions everywhere. So i looked at how to change the
parser. Everything is so difficult to change. Luckily there was a
built-in way to do this with link resolvers, found in a github issue
https://github.com/vsch/flexmark-java/issues/308 . And ideally this
would be done in the parser but it seems to be done in the html
emitter.

https://github.com/vsch/flexmark-java/blob/master/flexmark-java-samples/src/com/vladsch/flexmark/java/samples/CustomLinkResolverSample.java

And then I got turned around on what is relative or not. What happens if
you do something seemingly sane like:

```markdown
[a link to google](www.google.com)
```

This is apparently a relative link since it lacks a protocol. And our
`resolve-uri` code treats it as such:

```clojure
markdown=> (resolve-uri "www.google.com")
"http://localhost:3000www.google.com"
markdown=>
```

This seems strange to me but is also the behavior on gist.github.com:
https://gist.github.com/dpsutton/412502ffa89186487e41885855dfa781 has a
link to https://gist.github.com/dpsutton/www.google.com

In all, trying to figure out this object oriented factory mess i had 24
tabs open to the source of NodeVisitor, NodeVisitorBase,
AstActionHandler, VisitHandler, ParserExtension,
NodePostProcessorFactory, etc. It was truly unpleasant.

* Remove errant require of mb.util.urls

* Ensure the site setting always has a slash when resolving relative

The URI class will do some wonky things. Sometimes it feels structural,
but it can also just feel like it is combining strings willy nilly.

```clojure
(.. (URI. "http://example.com") (resolve "www.google.com") toString)
"http://example.comwww.google.com"
```

So ensure that there is a final trailing slash

---
## [FintanH/radicle-link](https://github.com/FintanH/radicle-link)@[7cc5811a3f...](https://github.com/FintanH/radicle-link/commit/7cc5811a3f9470cf3c2253aac7b5a5e79bb456c9)
#### Wednesday 2021-12-29 13:06:16 by Kim Altintop

Stable Rust

Make all crates compile under stable rust.

A number of `std` features we've been using were either stabilised, or
are unlikely to ever be stabilised. Also GATs don't seem to ever arrive
in a shape or form comprehensible to mere mortals. So let's stop chasing
and reformulate all code to compile under stable.

Note that:

- there does not seem to be a workaround for the `backtrace` feature

  This was used in one place in the `daemon` crate to manually add
  backtrace information to an error message, which may or may not be
  that useful. Executable crates using `anyhow` at the top level should
  still get backtrace information, although this may require to enable
  `anyhow`'s `backtrace` feature.

- a `Try` trait is provided via `radicle-std-ext`

  This will probably not work with `?` desugaring, but we're not using
  that at the moment. The "real" Try trait can be enabled using the
  feature `nightly` when a nightly toolchain is used. Note that
  `nightly` was chosen over `unstable`, as we may want to use the latter
  for our own unstable features at some point.

- the never type (`!`) is provided as `Void` from `radicle-std-ext`

  Regrettably, the never type is one of those features which are
  unlikely to be stabilised anytime soon. We alias `Void` to
  `Infallible` however, so in case it _does_ get stabilised we'll get
  the actual thing and not an incompatible type.

- our `rustfmt` rules require nightly

  Build scripts have been adjusted to accomodate for that, but note that
  editor hooks and such may need to be adjusted by contributors.

- stable clippy has very different opinions

  Sorry for the noise.

- specifically, box patterns is marked "perma-unstable"

  I have thus opted to ignore all lints about large enum variants for
  error types and use unboxed values. Pattern matching on boxes is
  rather painful, so it might be good to review errors for whether they
  are actually meant to be scrutinized, and convert variants which
  aren't to trait objects.

Fixes #476
Signed-off-by: Kim Altintop <kim@eagain.st>

---
## [regretware/sn-core](https://github.com/regretware/sn-core)@[9902a35004...](https://github.com/regretware/sn-core/commit/9902a35004356c0c3975f302549ac7a008f93991)
#### Wednesday 2021-12-29 14:15:46 by Andrey Karabanov

nope fuck you andrey you will touch navigation again and again until the fucking end of time you will

---
## [teslabs/zephyr](https://github.com/teslabs/zephyr)@[6809593739...](https://github.com/teslabs/zephyr/commit/680959373982584eb4fca09cdea464dfe59d262d)
#### Wednesday 2021-12-29 14:53:20 by Andy Ross

soc/intel_adsp: Linkage rework

Lots of changes to the linkage, none major:

+ Remove all the manually-defined ELF program headers.  This was a big
  pain to maintain, and I finally figured out why we were doing this:
  it turns out to have been a workaround for the flags issue below.

+ Suppress the "empty loadable section" warnings at module generation.
  This turns out to be an objcopy issue, when you drop all the
  sections from an ELF program header.

+ Set section flags for NOLOAD sections manually.  Rimage is very
  strict about flags (even to the point of trying to suck in its own
  metadata section as program text).  This turns out to be really
  fragile, as the linker automatically sets flags on the output
  section based on the symbols placed in it.  Rather than needing to
  have one program header per section, or playing games in the
  assembly for section definition to make this all match, just set the
  flags expressly on the sections we know about on the objcopy command
  line.

+ Similarly drop the special memory regions with explicit faked
  "physical" addresses that were being used for non-loadable sections
  (e.g. .fw_metadata, .static_log_entries).  Just link them all after
  the rest of the image like other platforms do.

+ Clean up multiple levels of macro indirection for the manifest base
  address, which is ultimately coming from kconfig.  Now the magic
  numbers don't seem so magic.

+ Remove legacy symbol exports for "cacheattr" that we don't use
  anymore.

Signed-off-by: Andy Ross <andrew.j.ross@intel.com>

---
## [LDR-Siren/EmilyC-SamanthaPrater-EruzaArto](https://github.com/LDR-Siren/EmilyC-SamanthaPrater-EruzaArto)@[054c16b151...](https://github.com/LDR-Siren/EmilyC-SamanthaPrater-EruzaArto/commit/054c16b151dae9a7c2ff0f8da3da0fa015d5d0d4)
#### Wednesday 2021-12-29 15:15:52 by LDR

0 12 28 2021 reddit spewage

She spewed all over Reddit 
I got accused of supporting Child Abuse and Domestic Violence(I am a victim of both but that is that big brain IQ working for her) 
She has gone after James military account and we have a lot of those screen shots
And she has brought in other people to fight her battle because there are those of us that support her mom for the person she has become, not the person she was. But by saying that I supposedly support Child Abuse and DV.  Emily obviously screams that we do not read her words and her whole argument against me proves she does not comprehend the words being spoken to her. It is one thing to read words its another to comprehend them. And she went back and attacked my daughter and I saying she felt sorry for my child(Who mind you gets everything she wants, is fed, clothed, loved, adored, encouraged to continue her art, and lives in a clean home. Oh and has never had LICE!) One of her friends even went as far to divulge that information that her mom, a neighbor had to rid Emily of Lice multiple times. Which begs to be asked "Did grandma not take care of her? Was grandma neglectful and not the saint that Emily makes her out to be?" I am guessing that grandma simply worked too much to give two shits about her let her do whatever and didn't care quite as much as Emily said she did. 

Either way she is still an Art Thief and our own handsome Captain Caveman has made a list of all her transgressions! Its a doozy!

---
## [cossacklabs/themis](https://github.com/cossacklabs/themis)@[9a6b4ed019...](https://github.com/cossacklabs/themis/commit/9a6b4ed019464e5f2e6258482bcb7bcf42a9fa09)
#### Wednesday 2021-12-29 15:24:13 by Alexei Lozovsky

Update GoThemis and WasmThemis examples to 0.14.0 (#893)

* go: Update examples to GoThemis 0.14.0

* go: Update tools to GoThemis 0.14.0

* wasm: Update examples to WasmThemis 0.14.0

* wasm: Upgrade "webpack-dev-server" 3 => 4

dev-only dependency of the example. Bumping the version to get rid
of "npm audit" warnings. Of course there are breaking changes...

* wasm: Throw away more polyfills

Newer versions of webpack-dev-server start showing all the warnings from
webpack right in your face. Let's fix them then...

WasmThemis includes code paths for Node.js support. They are not used
since browsers are not Node.js, but try explaining that to webpack.
So we do that but telling it to shut up and ignore all those built-in
Node.js modules.

* wasm: Suppress more warnings about "ws" dependency

WebSockets? Why?..

Anyway. I've found this workaround that gets webpack to shut up.

* wasm: Disable subresource integrity in dev builds

webpack-subresource-integrity used by the SRIPlugin *really* does not
like being used from a development web server. It prints warnings and
webpack-dev-server throws a giant full-screen overlay right in your
face when doing "npm run start". Okay, FINE, I'll disable you...

* wasm: Check package-lock.json into the repo

WasmThemis and JsThemis already do this, let the example have it
in the repo too. GitHub will scan it for vulnerabilities for us.

* go: Update pkg.go.dev badge

Uh... I don't remember why this is done manually. I guess because
the proper badges [1] don't show neither package name, nor version?

[1]: https://pkg.go.dev/badge/?path=https%3A%2F%2Fpkg.go.dev%2Fgithub.com%2Fcossacklabs%2Fthemis%2Fgothemis

---
## [aws/aws-cdk](https://github.com/aws/aws-cdk)@[c071367def...](https://github.com/aws/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Wednesday 2021-12-29 17:22:18 by Kaizen Conroy

feat(glue): support partition index on tables (#17998)

This PR adds support for creating partition indexes on tables via custom resources.
It offers two different ways to create indexes:

```ts
// via table definition
const table = new glue.Table(this, 'Table', {
  database,
  bucket,
  tableName: 'table',
  columns,
  partitionKeys,
  partitionIndexes: [{
    indexName: 'my-index',
    keyNames: ['month'],
  }],
  dataFormat: glue.DataFormat.CSV,
});
```

```ts
// or as a function
table.AddPartitionIndex([{
  indexName: 'my-other-index',
  keyNames: ['month', 'year'],
});
```

I also refactored the format of some tests, which is what accounts for the large diff in `test.table.ts`. 

Motivation: 
Creating partition indexes on a table is something you can do via the console, but is not an exposed property in cloudformation. In this case, I think it makes sense to support this feature via custom resources as it will significantly reduce the customer pain of either provisioning a custom resource with correct permissions or manually going into the console after resource creation. Supporting this feature allows for synth-time checks and dependency chaining for multiple indexes (reason detailed in the FAQ) which removes a rather sharp edge for users provisioning custom resource indexes themselves.

FAQ:

Why do we need to chain dependencies between different Partition Index Custom Resources? 
  - Because Glue only allows 1 index to be created or deleted simultaneously per table. Without dependencies the resources will try to create partition indexes simultaneously and the second sdk call with be dropped.

Why is it called `partitionIndexes`? Is that really how you pluralize index?
  - [Yesish](https://www.nasdaq.com/articles/indexes-or-indices-whats-the-deal-2016-05-12). If you hate it it can be `partitionIndices`.

Why is `keyNames` of type `string[]` and not `Column[]`? `PartitionKey` is of type `Column[]` and partition indexes must be a subset of partition keys...
  - This could be a debate. But my argument is that the pattern I see for defining a Table is to define partition keys inline and not declare them each as variables. It would be pretty clunky from a UX perspective:
    ```ts
    const key1 = { name: 'mykey', type: glue.Schema.STRING };
    const key2 = { name: 'mykey2', type: glue.Schema.STRING };
    const key3 = { name: 'mykey3', type: glue.Schema.STRING };
    new glue.Table(this, 'table', {
      database,
      bucket,
      tableName: 'table',
      columns,
      partitionKeys: [key1, key2, key3],
      partitionIndexes: [key1, key2],
      dataFormat: glue.DataFormat.CSV,
    });
    ```

Why are there 2 different checks for having > 3 partition indexes?
  - It's possible someone decides to define 3 indexes in the definition and then try to add another with `table.addPartitionIndex()`. This would be a nasty deploy time error, its better if it is synth time. It's also possible someone decides to define 4 indexes in the definition. It's better to fast-fail here before we create 3 custom resources.

What if I deploy a table, manually add 3 partition indexes, and then try to call `table.addPartitionIndex()` and update the stack? Will that still be a synth time failure?
  - Sorry, no. 

Why do we need to generate names?
  - We don't. I just thought it would be helpful.

Why is `grantToUnderlyingResources` public?
  - I thought it would be helpful. Some permissions need to be added to the table, the database, and the catalog.

Closes #17589.

----

*By submitting this pull request, I confirm that my contribution is made under the terms of the Apache-2.0 license*

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[2ff57104b7...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/2ff57104b7507daeb836729fde99da5b0c619154)
#### Wednesday 2021-12-29 17:25:26 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: Anush02198 <Anush.4376@gmail.com>
Signed-off-by: Divyanshu-Modi <divyan.m05@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[df70d33608...](https://github.com/mrakgr/The-Spiral-Language/commit/df70d3360867369028409d05a272dd20b6e0fc3c)
#### Wednesday 2021-12-29 18:33:43 by Marko Grdinić

"11:50am. How did I stay in bed for so long?

11:55am. Well, let me chill, have breakfast and then I will start. During the night it occurred to me that instead of the monofil marker, I should be using a variable length pen. I want to give that a try.

1:25pm. Done with breakfast and chores. Let me start. When I am done with this picture I'll consider moving from CSP to a free program like Krita or Sai. Since I am using a pirated version at the moment, I do not have access to most of CSP anyway.

Ok, first let me try the variable length pen instead of the monofil marker.

1:05pm. I'll just go with the G pen. I have no idea what the difference between some of these is, they all seem the same to me.

1:35pm. I have a while to go before I master pressure sensitivity. Now let me get started. It is time to put my plan into action.

1:55pm. Done with cushion 4. Now comes the last one. This image so far has a lot of soul.

2:25pm. Things are going faster this time around. Unlike what I thought, I do not need to stack layers, but I am making better use of the soft brush thanks to the mask

Now let me deal with the rest of the cushion. I need to make it darker and add some detail.

3:05pm. Done with the 5th cushion. That's all of them. I did an expert job. What I have to do now is take the layer masks of all the cushions and invert them. That will give me the couch area.

3:10pm. Focus me, stop reading the Baki thread.

3:15pm. Ok, let me do the sofa. After I do that I'll be done with 50% of the picture.

3:25pm. I feel that I am getting better. I think I've been taking the advice that I should use broad strokes a bit too much to heart.

3:30pm. Ah, fuck. I thought I was doing a good job, but I've just realized that I had erase on for most of the sofa. And I see it being used on the cushions as well. Shit. What I thought was my own color was actually the picture underneath bleeding through. Is there a setting to convert opacity to brightness?

3:40pm. It seems not. I have convert it to brightness by hand. Fuck.

3:45pm. Ok, I managed to salvage the situtation by changing the color of the paper underneath.

I need to be careful that this does not happen again.

4:20pm. Hrmmmm, I am not getting much use out of the G pen. If anything, I am less precise compared to before.

4:30pm. Yeah, forget variable width pens. They are doing me no good. Less is more in this case.

4:35pm. I forgot to switch from erase mode again. That thing is the devil. I should avoid it while painting with gradient maps. I'll just use the hard eraser instead.

5:05pm. I botched the bottom part and I know why. I should have textured it using many strokes that go across. Instead what I have now is a bunch of strokes that swirl around. It does not look good at all. I completely failed at capturing the feel and it looks like a kid went wild with a marker. I am going to have to redo it.

As a kid I would frequently use strokes that go in all sorts of directions.

5:25pm. Had to take a break. And it is good that I did, as taking a step back allowed me to think about the overall process. I did really stupid today. Let me go back to the g pen.

5:30pm. What I should have done from the start is put a flat raster layer and filled it with black. That would have eliminated all the hassle with using the eraser by accident. Instead I relied on the paper, fixed things by hand and who knows what I would have done in parallel timelines.

In fact, it occured to me during the break that using a flat layer would have significantly expanded my arsenal and allowed me to actually erase in higher layers. With a flat layer if I erased by accident it would have just gone towards black instead towards transparent.

I've been such a fool.

6:10pm. Let me leave for lunch.

6:40pm. Done with lunch.

I do not want to stop the art here for the day, let me just have some mandarins first. What I will do now is the sky and the stars. That will be easy. I'll leave the reflextions for tomorrow though.

6:55pm. Let me try getting into it again.

7:10pm. No, the fatigue is hitting me. It is so tedious to do these stars. I masked out about a quarter of them so far and I'll do the rest tomorrow. The fog itself was super easy to do as expected. I did a few lines with the g pen and then blurred them out. The stars take effort to mask out, but thankfully I rolled back on the decision to stock the sky with them otherwise it would take me a few hours just to deal with them. At the way things are going I'll be able to finish my first painting tomorrow. I guess it could serve as a wallpaper.

I'll post it in the /beg/ thread after I am done.

Damn this sure is taking me a while. I think today was the third day since I started working on it. Even if I get faster from here on out, it would still take me 2 days to deal with it.

I'll have to think how I can change my process to get properly faster. Maybe I could combine 3d backgrounds with 2d characters and find a way to make such a style mesh.

7:30pm. I am just sitting here in a daze. Let me close. Tomorrow I finish. After that I'll get started on the yearly review. Maybe I'll skip the PL sub review this year."

---
## [bulengerkacper/CRV_token_helper](https://github.com/bulengerkacper/CRV_token_helper)@[2d0ec8ea10...](https://github.com/bulengerkacper/CRV_token_helper/commit/2d0ec8ea1058e3e72237ac78d0f61f0f9a6556df)
#### Wednesday 2021-12-29 19:05:34 by bulengerkacper

Performed first jquery in my life, kinda funny that i am coding more than 6 yrs currently

---
## [connectuum/redbook](https://github.com/connectuum/redbook)@[85efe04501...](https://github.com/connectuum/redbook/commit/85efe04501fc8200242bbaaebcdb9cea59bbcd27)
#### Wednesday 2021-12-29 19:36:04 by connectuum

highlighted "Soul and God" chapter

another beautiful chapter, now that i have finally read it carefully. searching for _something_, first finding an image of in others, until realizing that it is my own soul that is missing. the soul that goes along with me, helping me to see the whole in each part. the recursive is the spring of life, the repeating resonance of well-being.

this is not taught, but discovered: by living and thinking to the fullest, by listening for that internal language you do not understand, by accepting the legitimacy of the knowledge of the heart.

our soul, our God, is our opposite, and believe it this serves our perfection through balance and completion. we must build and create and _live fully_ to develop into something more, to give birth to what is to come.

mockery may come from within and without. you must rise above this, in the example of Christ, to accept that you and he are the same, to become a Christ yourself.

> weight of words and wars we carry
> i'm like you
> just like you
> eyes of secret storm and story
> show and tell: we'll make it through
> by the _telling_
> will they _become_?
> will they all be
> feathers?

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[66a6e3d75b...](https://github.com/sojourn-13/sojourn-station/commit/66a6e3d75b1fd8cd72b3b22441443186c71832da)
#### Wednesday 2021-12-29 20:10:11 by Bones

More Genes then JC Pennies!

bottomless belly given to doggos. Increases max capacity for nutrition to 4 times the amount. good for long journeys if you can fill up. -10%
cat eyes on panthers and cats. Gives increased dark vision. Flashes will wreck your ass. -20%
cold resistance renamed into Thick Fur. Thick fur given to bears and corgis of all kind (protect Ian)  Now gives 10% brute resist along with cold resistance. Gives 10% burn weakness and takes up skin mutation slot - 20% instability.
honk given to geese. Literally just makes you honk like a dork
Echolocation given to bats.  allows you to see without eyes. -40% (If people abuse this with organ insertions I will make it turn your vision fucking black)
screaming given to possoms. Like moo and honk but for those who must scream!
toxin resistance given to snakes and bats. Gives a 10% reduction in toxin damage taken. 20% instability
Balances cowhide to cause 20% instability (Agreed amount with Hex)
Creates MUT_TYPE_EYES to keep from gaining all the eye genes.
Barotrauma gene added to space sharks/great whites. costs 20% instability. Gives pressure resistance.

---
## [DrBibop/EnforcerMod](https://github.com/DrBibop/EnforcerMod)@[c8bc6835dd...](https://github.com/DrBibop/EnforcerMod/commit/c8bc6835dd8bf1cf2a665fa81ce87202e0f8e947)
#### Wednesday 2021-12-29 20:17:35 by TimeSweeper

more dumb shit i'm sure

silly limb masking but also legit limb masking
more reorganizing it looks like
vr maybe
god damn so much shit I don't even know

---
## [GamingInfinite/VoidEngineMods](https://github.com/GamingInfinite/VoidEngineMods)@[3240032766...](https://github.com/GamingInfinite/VoidEngineMods/commit/32400327667fe861b91e2a811748dba8d7b08c5d)
#### Wednesday 2021-12-29 20:22:10 by GamingInfinite

Fixing characters for the new updated sprites

yeah yeah IK with all the stuff about Amor that came out I should probably drop this mod entirely, but despite the person that he is, which at this point I fucking hate, I still can't discount the work that came together out of BnB.  So I'm gonna continue using it as a model.

---
## [ederekun/fourteen_kernel_oneplus_msm8998](https://github.com/ederekun/fourteen_kernel_oneplus_msm8998)@[e1a53ab670...](https://github.com/ederekun/fourteen_kernel_oneplus_msm8998/commit/e1a53ab6702f4c910083a27ebbf8c279b3c02bc2)
#### Wednesday 2021-12-29 20:45:24 by Peter Zijlstra

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
## [GPUCode/ps2_emu](https://github.com/GPUCode/ps2_emu)@[fc244e8aad...](https://github.com/GPUCode/ps2_emu/commit/fc244e8aaddc3b0ca7da95173a5348a898c7f227)
#### Wednesday 2021-12-29 20:54:41 by emufan

Add initial implementation of EE timers

* Yeah, timers again, my favourite topic... To be frank the EE timers
are a bit simpler than the IOP timers as they have less complexity
in their configuration. However, since the BIOS starts to use them
at this point, we can't get away with a extermelly partial implementation
like the IOP.

* The Emotion Engine has four hardware timers, each of them having
three registers (four on Timer 0 and 1). They are practically the same
with the IOP in that regard, having a count a compare/target and a mode
register. Timer 0 and 1 have an additional register Tn_HOLD which
keeps track of the count value when a peripheral on the
SBUS generates an interrupt.

* All the timers increment based on the bus clock which is exactly
half of the EE clock. The timers can also be configured to count
based on external sources, namely hblank and vblank. These are less
accurate but can be used to keep track when the screen refreshes.
I had hoped that we could have ignored hblank for now, but the BIOS
configures Timer 3 (used for BIOS alarms) to use it so implementing it
is necessary. The timings were taken from the timer header [1]
of the ps2sdk.

* An interesting fact as well is the interrupts as edge triggered
which means that an interrupt is sent to the EE when the raised flags in
Tn_MODE switch from 0 to 1 [2]. This is easy to implement and so did I,
to avoid any headaches in the future.

* Since the EE ticks the timers directly, we can't increment the counters
each time the function get called. To properly emulate the timer frequency,
an internal counter is used, that when its value is equal to the ratio
between the EE frequency and the timer clock, the real counter is incremented.

* This can be expensive since the timer function gets called every EE cycle
so we will probably change it to cycle adding in the future, especially when
the JIT will be implemented.

[1] https://github.com/ps2dev/ps2sdk/blob/master/ee/kernel/include/timer.h#L53
[2] https://psi-rockin.github.io/ps2tek/#eetimers

---
## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[fab444ffe2...](https://github.com/Tastyfish/Skyrat-tg/commit/fab444ffe2887cb2838f974a41c392ed48d2ae6e)
#### Wednesday 2021-12-29 21:29:55 by Seris02

[modular] big borg code improvements and fixes (#9701)

* big borg code improvements and fixes

* I missed a modular comment

* fuck you linters

* yis

* converts skyrat versions to better

* annnnnd that should fix it

---

