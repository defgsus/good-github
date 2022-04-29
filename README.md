## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-28](docs/good-messages/2022/2022-04-28.md)


1,751,343 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,751,343 were push events containing 2,836,745 commit messages that amount to 218,702,979 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [jupyterkat/Pariah-Station](https://github.com/jupyterkat/Pariah-Station)@[fb13b0e4ff...](https://github.com/jupyterkat/Pariah-Station/commit/fb13b0e4ff4a8957f2837adf7ba06ae2eb388bf8)
#### Thursday 2022-04-28 00:01:56 by PariahBot

[MIRROR] Vim mecha changes (#541)

* Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

* Vim mecha changes

Co-authored-by: B4CKU <50628162+B4CKU@users.noreply.github.com>
Co-authored-by: Debian <debian@packer-output-01d6f1be-59bf-4994-80ec-c61b12fe30e1>

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[4d54e290db...](https://github.com/silicons/Citadel-Station-13-RP/commit/4d54e290db51697d12fc54a6bbb0a376f43b7280)
#### Thursday 2022-04-28 00:04:45 by Zandario

Security TGUI (#3886)

* e

* Fuck it, I'm pushing it.

* Fuck you

* Refactored Brigdoors, updated their UI, does annoucements

Also updated logging a little bit and documented some things.

* Multitool sync

---
## [goldelico/letux-kernel](https://github.com/goldelico/letux-kernel)@[9709c8b5cd...](https://github.com/goldelico/letux-kernel/commit/9709c8b5cdc88b1adb77acdbfd6e8a3f942d9af5)
#### Thursday 2022-04-28 00:22:28 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [twilightwanderer/tgstation](https://github.com/twilightwanderer/tgstation)@[54403a1ca0...](https://github.com/twilightwanderer/tgstation/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Thursday 2022-04-28 01:15:48 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [castawaynont/tgstation](https://github.com/castawaynont/tgstation)@[e58fb506ef...](https://github.com/castawaynont/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Thursday 2022-04-28 01:26:59 by LemonInTheDark

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
## [magatsuchi/tgstation](https://github.com/magatsuchi/tgstation)@[cd1b891d79...](https://github.com/magatsuchi/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Thursday 2022-04-28 03:19:06 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [SimplexShotz/firebase-real-time-collaborative-text-editor](https://github.com/SimplexShotz/firebase-real-time-collaborative-text-editor)@[f6768c89b4...](https://github.com/SimplexShotz/firebase-real-time-collaborative-text-editor/commit/f6768c89b42e1c56f51f2145fa71f553eee84640)
#### Thursday 2022-04-28 04:09:17 by SimplexShotz

The Penultimate Update

You read that right! This 2-month long project is finally coming to a close, and I couldn't be more proud of the end result. Let's take a look at what this update includes.

Added Support For:
 - Realtime Cursor Tracking
 - "Style Memory" (for example, hitting "Ctrl + B" while nothing is selected will cause the next character typed to be bold, unless the cursor is moved)
 - Ctrl + Backspace/Delete support
 - Client will now auto-disconnect if unable to sync after 10+ attempts
 - Complete overhaul of the FitScore system; it's now much more readable, condensed, and accurate
 - Links now have a preview button

Bug Fixes:
 - Disconnected users will no longer leave behind extra unneeded data in Firebase
 - FitScores are now correct (they were off in a few cases before)
 - The "after" surrounding text is now calculated properly for all changes
 - The undo/redo stack is now much more consistent and accurate
 - Fixed syncing and content updating to be MUCH more accurate; the editor now rarely ever has to sync, which greatly improves the editing experience
 - Styles are now handled properly
 - Classes are now handled properly within the "setText" function
 - The "mousemove" event is now handled and updates the cursor properly
 - Moving the cursor now updates the client's status properly
 - Style buttons no longer throw errors when the cursor is not inside the editor
 - Link hrefs are now trimmed properly to prevent unnecessary padding by spaces/line breaks
 - Links are now stored in a condensed object rather than an array to save storage space in Firebase
 - All changes now have "start" and "end" keys for their indexes
 - Fixed the order of undo/redo events (the pending undo/redo is pushed as a change BEFORE the change is applied; before, this was the other way around, which was causing issues when determining the surrounding text)
 - The "getSelectionPosition" function now returns a proper location when the cursor is in the editor, but no text is selected
 - Cursor colors now have a limit on how bright the colors can be, making them much more visible in a lot of cases

Yeah... there were just a *few* bug fixes... Anywho, onto what's left:

Coming Soon:
 - Lots of testing :D
 - (potentially?) Support for Chromebooks' grammar auto-correct (I still have to find out if this fires an "input" event; if it doesn't, then I don't think this will be possible to handle, unfortunately)
 - (hopefully not) More bug fixes!! WHOOOOO (although pretty much everything is working AMAZINGLY right now; this project has gone so much better than I ever could have expected it to, haha! not to jinx myself, of course...)

I'm claiming the "Magnum Opus" title just for this GitHub project~

---
## [YakumoChen/tgstation](https://github.com/YakumoChen/tgstation)@[ce0aff7526...](https://github.com/YakumoChen/tgstation/commit/ce0aff7526158133acd1b53bd5d2d9d6ac9578f3)
#### Thursday 2022-04-28 05:03:51 by GoldenAlpharex

Fixed Icebox's lower two z-levels not being included in the Map Compile action (#66503)

Did you know that you could currently put a bunch of random shit in the lower levels of icebox and the map compile would be none the wiser?

I sure did.

I hate that it's done manually this way, but honestly it's not worth refactoring the whole action to make it work differently.

Ensuring that the lower levels work properly is, in fact, a good thing.

---
## [Jayhawk4080/spicetify-cli](https://github.com/Jayhawk4080/spicetify-cli)@[0a89573c1c...](https://github.com/Jayhawk4080/spicetify-cli/commit/0a89573c1ce2f4ed3f4cdaac7651bc34dffb3a0a)
#### Thursday 2022-04-28 05:05:53 by Łukasz Ordon

fix: `New Releases` custom app for Spotify 1.1.81+ (#1563)

* Fix `New Releases` custom app for Spotify 1.1.81+

- Based on proposed fix for `Shuffle+` (#1559)
- Fixes #1539 #1530 

Notes:
- Can probably be written nicer - this is my scuffed attempt to fix it
- May or may not actually show all new releases for all followed artists - have over 665 of them but I don't think I'm getting all of them (see below)
- May or may not return `error 500` (added `.catch()` block keeps it from breaking whole custom app)

* Minimize `internal server error: 500`...

...for big libraries of followed artists.

Changes:
- Change `URL` to query only discographies
- Limit amount of queried albums to 5

Notes:
- This does **NOT** fixes erroring fully - it only maxes out amount of data you can query before getting rate limited
- The more options you select (ex. albums + EPs + podcasts), the less data you may receive
- To max number of albums received, I recommend to select only `Albums` (since `Singles and EPs` will probably get displayed anyway...)

* Add notifications when error occurred

Notifications added:
- Error code (`500`, `429` etc.)
- Amount of followed artists to fetch releases from
- Amount of followed artists failed to fetch releases from

I guess we have to get along with getting `500-ed` - one time it fetches everything instantly, second time it drops 60 artists...

* "Prettify" file to pass `Prettier` test

* Fix filtering, counter...

- Fixing filtering as no matter was what set in config, it always displayed everything as "Album"
- Fixing "Missing releases from..." counter - should properly reset now

What broke again:
- "Appears on" releases cannot be retrieved with that API endpoint - this filter is just there and doesn't do anything - this prevents from showing everything as "Appears on" etc.

Notes:
- There seem to be an API endpoint for retrieving "Related content" stuff - problem is that would query everything TWICE... which breaks everything even more (and we don't wanna do that)
- If someone knows how to query everything using separate endpoint without doing it 4 times, let me know...

* Forgor `( )`... Oops... :skull:

I forgor 💀

* Include requested changes

Changes:
- Properly encode URI including variables
- Make `limit` variable customizable via settings (set default to 5)
- Make error messages as "dev console only"

Notes:
- Errors displayed in console may be a little spammy - if we get error early, there may be lots of lines displaying it + counter...
   * I'm not too sure how to tackle this - just remove them altogether? Or is there a function that could "suppress" them?
   * Switching from normal `log` to `debug` may help a little as they will be only visible if user has set their console log level to include `Verbose`
- Making `limit` customizable may lead to even more errors but fuck it I guess - it's better to have a choice than not, right?
   * It can be manually input via custom app settings (same place where other options are) - there is no list etc. - it's just normal input field
- Set `offset` value as const `0` and not making it customizable (cause why would you want to start searching from ex. 3rd album instead of beginning, right?)
- Leaving `Fetching releases from...` notification cause it looks cool - it's fun to know how many followed artists you have 😆

---
## [Sergei-Udris/Cara-Dune](https://github.com/Sergei-Udris/Cara-Dune)@[3a00982bef...](https://github.com/Sergei-Udris/Cara-Dune/commit/3a00982bef14c49c7f248a8cc73386c37867833f)
#### Thursday 2022-04-28 07:13:34 by Cara-Dune

i move on the map, i turned swing compoenents into whole processes, i use all namespaces, all refs are in main
:McEnroe sorry, i was just practicing my serve
:Andy-Samberg how did McEnroe get in here?!
:Jonah fuck you, McEnroe!

---
## [Khalvat-M/kernel_samsung_msm8974](https://github.com/Khalvat-M/kernel_samsung_msm8974)@[033b82ffa1...](https://github.com/Khalvat-M/kernel_samsung_msm8974/commit/033b82ffa1628cb63c15463011b080ecac3d302f)
#### Thursday 2022-04-28 08:01:08 by Linus Torvalds

mm: get rid of 'vmalloc_info' from /proc/meminfo

It turns out that at least some versions of glibc end up reading
/proc/meminfo at every single startup, because glibc wants to know the
amount of memory the machine has.  And while that's arguably insane,
it's just how things are.

And it turns out that it's not all that expensive most of the time, but
the vmalloc information statistics (amount of virtual memory used in the
vmalloc space, and the biggest remaining chunk) can be rather expensive
to compute.

The 'get_vmalloc_info()' function actually showed up on my profiles as
4% of the CPU usage of "make test" in the git source repository, because
the git tests are lots of very short-lived shell-scripts etc.

It turns out that apparently this same silly vmalloc info gathering
shows up on the facebook servers too, according to Dave Jones.  So it's
not just "make test" for git.

We had two patches to just cache the information (one by me, one by
Ingo) to mitigate this issue, but the whole vmalloc information of of
rather dubious value to begin with, and people who *actually* want to
know what the situation is wrt the vmalloc area should just look at the
much more complete /proc/vmallocinfo instead.

In fact, according to my testing - and perhaps more importantly,
according to that big search engine in the sky: Google - there is
nothing out there that actually cares about those two expensive fields:
VmallocUsed and VmallocChunk.

So let's try to just remove them entirely.  Actually, this just removes
the computation and reports the numbers as zero for now, just to try to
be minimally intrusive.

If this breaks anything, we'll obviously have to re-introduce the code
to compute this all and add the caching patches on top.  But if given
the option, I'd really prefer to just remove this bad idea entirely
rather than add even more code to work around our historical mistake
that likely nobody really cares about.

Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Change-Id: Ia17de8b8f49d801efa5aaff3c61ba4c1082dc1e3

---
## [paulgessinger/acts](https://github.com/paulgessinger/acts)@[6e1fd31474...](https://github.com/paulgessinger/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Thursday 2022-04-28 08:25:49 by Stephen Nicholas Swatman

feat: Implement a new orthogonal range search seed finder (#904)

As I said in #901, I have been playing around with seed finding a little bit lately. Last weekend, I mentioned an idea for a new (?) kind of seed finding algorithm based on range search datastructures, and this is the very, very first semi-working implementation of it, just before the weekend.

The idea behind this algorithm is relatively simple. In traditional seedfinding, we check a whole lot of candidate spacepoints to see whether they meet some condition. If you look at this differently, each spacepoint defines a volume in the z-r-φ space, which contains any spacepoints it can form a doublet with. What if we reversed this logic? What if we defined this volume first, and then just extract the spacepoints inside of that space? That way, we can vastly reduce the number of spacepoints we need to look at.

How do we do this quickly? With [_k_-d trees](https://en.wikipedia.org/wiki/K-d_tree). These data structures are cheap to build, and they give us very fast orthogonal range searches. In other words, we can very quickly look up which of our spacepoints lie within an axis-aligned orthognal n-dimensional hyperrectangle. In this case, which spacepoints lie within a z-r-φ box.

So, the core idea of this seedfinder is to define as many of our seedfinding constraints in orthogonal fashion. That way, we can make our candidate hyperrectangle smaller and smaller. The tighter the constraints we can place, the better. Then, we look up the relevant spacepoints, and we can avoid looking at any others. That also means this solution requires no binning whatsoever.

## Constraint conversion

Currently there are quite a few constraints in the code. Here is my status update on how well it is going to convert each of them. In some cases, we can define a weaker version of the constraints in orthogonal fashion. This is still very powerful, and it doesn't actually lose us any efficiency (because we can always check the tighter constraint in a non-orthogonal way later, not a problem)!

### Unary constraints

Currently, I am not aware of any unary constraints in the Acts seed finding code. That is to say, logic to determine whether a point is allowed to be a lower spacepoint. However, I have the following thoughts about introducing some:

* I believe the binning code does some kind of magic to determine whether a spacepoint can be a lower spacepoint. Since my solution doesn't use any binning, I don't have access to this just yet. However, if we can incorporate this logic it could be very powerful.
* Maximum single-point η: we currently have some checks in place to see if the pseudorapidity of particles is not too high. We could realistically use this maximum pseudorapidity, combined with the collision region range to constrain the bottom spacepoints.

### Binary constraints

These are the existing binary constraints on spacepoint duplets:

Constraint | Description | Orthogonalization
-|-|-
Minimum ∆r | Ensure that the second spacepoint is within a certain difference in radius | Full
Maximum cot θ | Ensure that the pseudorapidity of the duplet is not too high | Unsuccessful
z-origin range | Ensure that the duplet would have originated from the collision point | Weakened 
Maximum ∆φ<sup>1</sup> | Ensure that the duplet does not bend too much in the x-y plane | Full

<sup>1</sup> This check does not exist explicitly in the existing seed finder, but is implicit in the binning process.

### Ternary constraints

There are a lot of ternary constraints (to check whether a triplet is valid):

Constraint | Description | Orthogonalization
-|-|-
Scattering angle | ??? | Unsuccessful
Helix diameter | Ensure the helix diameter is within some range | In progress
Impact parameters | Ensure the impact parameters are close to the collision point | In progress
Monotonic z<sup>1</sup> | Ensure that z increases or decreases monotonically between points | Full

<sup>1</sup> This check does not exist in the existing seed finder, check #901.

There are also constraints defined in the experiment-specific cuts, and the seed filter, and in other places. If we could convert some of those to orthogonal constraints the implementation would become much more powerful. However, I don't really understand what is happening in those files just yet. Need more reading.

## Current performance

The current performance of this seedfinder is... Complicated. On my machine, it runs a 4000 π<sup>+</sup> event in about 5 seconds, three times slower than the existing seedfinder. Its efficiency is much higher though, and the fake rate is much lower. So that's something. However, that is in part because I am creating far more seed candidates, so take this with a big grain of salt.

## Potential gain

There are two ways that I can think of to use this kind of algorithm. The first is an inside-to-outside algorithm, where we pick a lower spacepoint first, check the space it defines for a middle spacepoint, and then check the space the two of them define for a third spacepoint. This algorithm has time complexity 𝒪(_n_<sup>3</sup>), and it has space complexity 𝒪(_n_). Due to the constants, I still believe this implementation can outperform the 𝒪(_n_<sup>2</sup>) existing algorithm, however.

The second way would be to construct a set of duplets using this logic, and then to fit those together like we do with traditional seedfinding. This has 𝒪(_n_<sup>2</sup>) time complexity like the existing code, but also space complexity 𝒪(_n_<sup>2</sup>).

## Things that are completed

* The implementation of the _k_-d tree seems to work very well, and it is quite fast.
* Basic seedfinding using this strategy is functional.

## Things that don't work yet

* My maximum ∆φ constraint does not cross the 2π boundary yet.
* I used the existing seedfinding algorithm as a stepping stone, which I have completely destroyed in the process. Obviously I do not intend on keeping it that way, and the existing algorithm will be restored to its full glory.
* Lots more.

## Things that can be improved

* Add more constraints, and tighten existing ones.
* Lots of things, pretty much everything. But I really want to go home for the weekend, so I will write this part next week.

---
## [defgsus/kindergarten-times](https://github.com/defgsus/kindergarten-times)@[0f31ab070c...](https://github.com/defgsus/kindergarten-times/commit/0f31ab070cdf977ea6499bdf041565789f07e578)
#### Thursday 2022-04-28 08:29:00 by bergi

simply laziness.

and my morning coffee took longer because of thoughts about yesterday evening.
We live in a relatively small town here. There's a lot of students, though,
and very valuable nodes and networks of sub-cultural people. Yesterday,
a documentary about this sub-culture and the conflicting real estate politics
was premiered on the market place.

It was great to see a lot of these old faces again. Again,
for me, means: after turning into a family man and especially after 24 months
of pandemic *don't-do-anything-with-anybody* mindset which, fortunately,
has started to fade out a bit. Not that everybody was sitting at home but
i certainly had no big part in joint activities.

Now, one of the people interviewed in the film has always been controversial.
He'd some good statements, as usual, but a lot of people in town simply call
him an asshole, sexist, drug addict, a show-off, a creep. I found it fun
to meet him again after some time, amongst hundreds of sub-cultural
friends and supporters, watching this film, that was created to a good part
because of the mobilization of this controversial person and which explains,
based on a particular story ('Die Insel' in Jena) how governments
(state or local) can simple override the desires of people regardless
of the people's years-long efforts to articulate their basic need, in the city
council, in the press, on demonstrations, in official meetings.

Well, at least we can screen a documentary about these misfortunes on the
market place, right? Privately payed and organized, of course.

But all that did not lead to my prolonged morning coffee. After the screenig,
another old-school sub-culture activist approached and asked how i could
still hang about with *this person*, the controversial one. Let's call
the old-schooler **O** and the controversial person **C**. After some
discussion we parted, leaving me with the decission to not ever talk
again with **C** or **O** will never talk with me again.

Background: **C** is organizing small regular demonstrations against
"covid government measures", like obligatory vaccinations, which are not
currently applied and probably not needed anyway, but are discussed often
enough. Now this whole covid/government topic is a sad one anyway and
people, even friends or former friends are fighting about it. Needless
to say that in this little scenario i'm describing, **O** is more on the
*there-is-good-reason-to-be-afraid-by-covid*-side and not so much on the
*but-that-can-not-give-the-government-full-control-over-our-lifes*-side.

Well, it must all be seen in context. And there are different contexts.
Always. I'm not out to fight with people but i like to hear different
and controversial oppinions and a like a bunch of different people that
might not like each other.

But now i'm forced to choose a side or what? **O**, the good guys, or
**C**, the scum and nazi-collaborators. Oh, nazi you say? Well, he did
say *fascists* in particular but we did not clearly define the boundary
between fascist and non-fascist. Sure, why be picky? We don't like
*fascist* nor *nazis*. And i'm simply to despise **C** for letting *fascists*
talk on his demonstrations. Oh, we don't have a *fascist* party in germany
any more. **O** is talking about the AFD youth, the "alternative", which
is, of course, a right-wing political movement, but you could also call it
conservative neo-liberalism that paints itself in the color of resistance
and really picks any topic that the other parties are not willing to
discuss. You can also call them tinfoil heads, which i find a bit sad
because whatever interesting *tinfoil-topic* you have will eventually
be perceived as spread by the right-wings. Sure, that's what they do!
The AFD is increasing it's base through *propaganda*. That's what all the
political parties do, the kind of *propaganda* is a bit different, though.

It's simply tiring. We could dispute so much just about the way one perceives
things. I don't want to dispute. Not in earnest at least. I like to learn
why people think about things the way they do. Why they think a mask
protects us from covid or why they think that this is the most stupid lie
by the government. You know, there are *scientifc facts* in between but
most of the time people follow their guts. Now why should managers and
politicians be excempt from that? They also largly do what they *feel* is
right. And that *right* is a clear *wrong* for someone else.

If i don't officially distance myself from **C**, then **O** will officially
distance himself from me. I just wonder how far this goes. Will i loose all
my friends? I don't think so. But there's another separation, another
parallel world in our little town.

We never ever talk to fascists! It's forbidden by the law, ähh.. i mean
by the agreement of our *scene*.

How is *fascist* defined then? Someone who collaborates with
someone who collaborates with the AFD is clearly a *fascist*.

You know what? If we just had a lever this big to discriminate people
that browse smartphone 8 hours a day?

---
## [Urgau/cargo](https://github.com/Urgau/cargo)@[6a4d98d232...](https://github.com/Urgau/cargo/commit/6a4d98d2327124ca52bb9f67d6ad0097eb6b2e65)
#### Thursday 2022-04-28 08:43:14 by bors

Auto merge of #10472 - epage:add, r=ehuss

feat: Import cargo-add into cargo

### Motivation

The reasons I'm aware of are:
- Large interest, see #5586
- Make it easier to add a dependency when you don't care about the version (instead of having to find it or just using the major version if thats all you remember)
- Provide a guided experience, including
  - Catch or prevent errors earlier in the process
  - Bring the Manifest format documentation into the terminal via `cargo add --help`
  - Using `version` and `path` for `dependencies` but `path` only for `dev-dependencies` (see crate-ci/cargo-release#288 which led to killercup/cargo-edit#480)

### Drawbacks

1. This is another area of consideration for new RFCs, like rust-lang/rfcs#3143 (this PR supports it) or rust-lang/rfcs#2906 (implementing it will require updating `cargo-add`)

2. This is a high UX feature that will draw a lot of attention (ie Issue influx)

e.g.
- killercup/cargo-edit#521
- killercup/cargo-edit#126
- killercup/cargo-edit#217

We've tried to reduce the UX influx by focusing the scope to preserving semantic information (custom sort order, comments, etc) but being opinionated on syntax (style of strings, etc)

### Behavior

Help output
<details>

```console
$ cargo run -- add --help
cargo-add                                                                                                                                  [4/4594]
Add dependencies to a Cargo.toml manifest file

USAGE:
    cargo add [OPTIONS] <DEP>[`@<VERSION>]` ...
    cargo add [OPTIONS] --path <PATH> ...
    cargo add [OPTIONS] --git <URL> ...

ARGS:
    <DEP_ID>...    Reference to a package to add as a dependency

OPTIONS:
        --no-default-features     Disable the default features
        --default-features        Re-enable the default features
    -F, --features <FEATURES>     Space-separated list of features to add
        --optional                Mark the dependency as optional
    -v, --verbose                 Use verbose output (-vv very verbose/build.rs output)
        --no-optional             Mark the dependency as required
        --color <WHEN>            Coloring: auto, always, never
        --rename <NAME>           Rename the dependency
        --frozen                  Require Cargo.lock and cache are up to date
        --manifest-path <PATH>    Path to Cargo.toml
        --locked                  Require Cargo.lock is up to date
    -p, --package <SPEC>          Package to modify
        --offline                 Run without accessing the network
        --config <KEY=VALUE>      Override a configuration value (unstable)
    -q, --quiet                   Do not print cargo log messages
        --dry-run                 Don't actually write the manifest
    -Z <FLAG>                     Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for
                                  details
    -h, --help                    Print help information

SOURCE:
        --path <PATH>        Filesystem path to local crate to add
        --git <URI>          Git repository location
        --branch <BRANCH>    Git branch to download the crate from
        --tag <TAG>          Git tag to download the crate from
        --rev <REV>          Git reference to download the crate from
        --registry <NAME>    Package registry for this dependency

SECTION:
        --dev                Add as development dependency
        --build              Add as build dependency
        --target <TARGET>    Add as dependency to the given target platform

EXAMPLES:
  $ cargo add regex --build
  $ cargo add trycmd --dev
  $ cargo add --path ./crate/parser/
  $ cargo add serde serde_json -F serde/derive
```

</details>

Example commands
```rust
cargo add regex
cargo add regex serde
cargo add regex@1
cargo add regex@~1.0
cargo add --path ../dependency
```
For an exhaustive set of examples, see [tests](https://github.com/killercup/cargo-edit/blob/merge-add/crates/cargo-add/tests/testsuite/cargo_add.rs) and associated snapshots

Particular points
- Effectively there are two modes
  - Fill in any relevant field for one package
  - Add multiple packages, erroring for fields that are package-specific (`--rename`)
  - Note that `--git` and `--path` only accept multiple packages from that one source
- We infer if the `dependencies` table is sorted and preserve that sorting when adding a new dependency
- Adding a workspace dependency
  - dev-dependencies always use path
  - all other dependencies use version + path
- Behavior is idempotent, allowing you to run `cargo add serde serde_json -F serde/derive` safely if you already had a dependency on `serde` but without `serde_json`
- When a registry dependency's version req is unspecified, we'll first reuse the version req from another dependency section in the manifest.  If that doesn't exist, we'll use the latest version in the registry as the version req

### Additional decisions

Accepting the proposed `cargo-add` as-is assumes the acceptance of the following:
- Add the `-F` short-hand for `--features` to all relevant cargo commands
- Support ``@`` in pkgids in other commands where we accept `:`
- Add support for `<name>`@<version>`` in more commands, like `cargo yank` and `cargo install`

### Alternatives

- Use `:` instead of ``@`` for versions
- Flags like `--features`, `--optional`, `--no-default-features` would be position-sensitive, ie they would only apply to the crate immediate preceding them
  - This removes the dual-mode nature of the command and remove the need for the `+feature` syntax (`cargo add serde -F derive serde_json`)
  - There was concern over the rarity of position-sensitive flags in CLIs for adopting it here
- Support a `--sort` flag to sort the dependencies (existed previously)
  - To keep the scope small, we didn't want general manifest editing capabilities
- `--upgrade <POLICY>` flag to choose constraint (existed previously)
  - The flag was confusing as-is and we feel we should instead encourage people towards `^`
- `--allow-prerelease` so a `cargo add clap` can choose among pre-releases as well
  - We felt the pre-release story is too weak in cargo-generally atm for making it first class in `cargo-add`
- Offer `cargo add serde +derive serde_json` as a shorthand
- Infer path from a positional argument

### Prior Art

- *(Python)* [poetry add](https://python-poetry.org/docs/cli/#add)
  - `git+` is needed for inferring git dependencies, no separate  `--git` flags
  - git branch is specified via a URL fragment, instead of a `--branch`
- *(Javascript)* [yarn add](https://yarnpkg.com/cli/add)
  - `name@data` where data can be version, git (with fragment for branch), etc
  - `-E` / `--exact`, `-T` / `--tilde`, `-C` / `--caret` to control version requirement operator instead of `--upgrade <policy>` (also controlled through `defaultSemverRangePrefix` in config)
  - `--cached` for using the lock file (killercup/cargo-edit#41)
  - In addition to `--dev`, it has `--prefer-dev` which will only add the dependency if it doesn't already exist in `dependencies` as well as `dev-dependencies`
  - `--mode update-lockfile` will ensure the lock file gets updated as well
- *(Javascript)* [pnpm-add](https://pnpm.io/cli/add)
- *(Javascript)* npm doesn't have a native solution
  - Specify version with ``@<version>``
  - Also overloads `<name>[`@<version>]`` with path and repo
    - Supports a git host-specific protocol for shorthand, like `github:user/repo`
    - Uses fragment for git ref, seems to have some kind of special semver syntax for tags?
  - Only supports `--save-exact` / `-E` for operators outside of the default
- *(Go)* [go get](https://go.dev/ref/mod#go-get)
  - Specify version with ``@<version>``
  - Remove dependency with ``@none``
- *(Haskell)* stack doesn't seem to have a native solution
- *(Julia)* [pkg Add](https://docs.julialang.org/en/v1/stdlib/Pkg/)
- *(Ruby)* [bundle add](https://bundler.io/v2.2/man/bundle-add.1.html)
  - Uses `--version` / `-v` instead of `--vers` (we use `--vers` because of `--version` / `-V`)
  - `--source` instead of `path` (`path` correlates to manifest field)
  - Uses `--git` / `--branch` like `cargo-add`
- *(Dart)* [pub add](https://dart.dev/tools/pub/cmd/pub-add)
  - Uses `--git-url` instead of `--git`
  - Uses `--git-ref` instead of `--branch`, `--tag`, `--rev`

### Future Possibilities

- Update lock file accordingly
- Exploring the idea of a [`--local` flag](https://github.com/killercup/cargo-edit/issues/590)
- Take the MSRV into account when automatically creating version req (https://github.com/killercup/cargo-edit/issues/587)
- Integrate rustsec to report advisories on new dependencies (https://github.com/killercup/cargo-edit/issues/512)
- Integrate with licensing to report license, block add, etc (e.g. https://github.com/killercup/cargo-edit/issues/386)
- Pull version from lock file (https://github.com/killercup/cargo-edit/issues/41)
- Exploring if any vendoring integration would be beneficial (currently errors)
- Upstream `cargo-rm` (#10520), `cargo-upgrade` (#10498), and `cargo-set-version` (in that order of priority)
- Update crates.io with `cargo add` snippets in addition to or replacing the manifest snippets

For more, see https://github.com/killercup/cargo-edit/issues?q=is%3Aissue+is%3Aopen+label%3Acargo-add

### How should we test and review this PR?

This is intentionally broken up into several commits to help reviewing
1. Import of production code from cargo-edit's `merge-add` branch, with only changes made to let it compile (e.g. fixing up of `use` statements).
2. Import of test code / snapshots.  The only changes outside of the import were to add the `snapbox` dev-dependency and to `mod cargo_add` into the testsuite
3. This extends the work in #10425 so I could add back in the color highlighting I had to remove as part of switching `cargo-add` from direct termcolor calls to calling into `Shell`

Structure-wise, this is similar to other commands
- `bin` only defines a CLI and adapts it to an `AddOptions`
- `ops` contains a focused API with everything buried under it

The "op" contains a directory, instead of just a file, because of the amount of content.  Currently, all editing code is contained in there.  Most of this will be broken out and reused when other `cargo-edit` commands are added but holding off on that for now to separate out the editing API discussions from just getting the command in.

Within the github UI, I'd recommend looking at individual commits (and the `merge-add` branch if interested), skipping commit 2.  Commit 2 would be easier to browse locally.

`cargo-add` is mostly covered by end-to-end tests written using `snapbox`, including error cases.

There is additional cleanup that would ideally happen that was excluded intentionally from this PR to keep it better scoped, including
- Consolidating environment variables for end-to-end tests of `cargo`
- Pulling out the editing API, as previously mentioned
  - Where the editing API should live (`cargo::edit`?)
  - Any more specific naming of types to reduce clashes (e.g. `Dependency` or `Manifest` being fairly generic).
- Possibly sharing `SourceId` creation between `cargo install` and `cargo edit`
- Explore using `snapbox` in more of cargo's tests

Implementation justifications:
- `dunce` and `pathdiff` dependencies: needed for taking paths relative to the user and make them relative to the manifest being edited
- `indexmap` dependency (already a transitive dependency): Useful for preserving uniqueness while preserving order, like with feature values
- `snapbox` dev-dependency: Originally it was used to make it easy to update tests as the UX changed in prep for merging but it had the added benefit of making some UX bugs easier to notice so they got fixed.  Overall, I'd like to see it become the cargo-agnostic version of `cargo-test-support` so there is a larger impact when improvements are made
- `parse_feature` function: `CliFeatures` forces items through a `BTreeSet`, losing the users specified order which we wanted to preserve.

### Additional Information

See also [the internals thread](https://internals.rust-lang.org/t/feedback-on-cargo-add-before-its-merged/16024).

Fixes #5586

---
## [MineClone2/MineClone2](https://github.com/MineClone2/MineClone2)@[5f126c4686...](https://github.com/MineClone2/MineClone2/commit/5f126c468650577ea0baefb5d79b81835fe33579)
#### Thursday 2022-04-28 08:53:51 by cora

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[9073628905...](https://github.com/treckstar/yolo-octo-hipster/commit/90736289050439eb7ea74baea3a441d488bb8cf1)
#### Thursday 2022-04-28 09:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [stipid-code/dotfiles](https://github.com/stipid-code/dotfiles)@[99eaa14cf7...](https://github.com/stipid-code/dotfiles/commit/99eaa14cf7e83182a9c6a97886bda339fa25bc92)
#### Thursday 2022-04-28 09:59:52 by methlab inc

For thee fucking windows pleb

remember to change the executables' path to wherever bill's boys shoved your only decent fucking terminal

---
## [Toshiro90/rathena](https://github.com/Toshiro90/rathena)@[d617d9f083...](https://github.com/Toshiro90/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Thursday 2022-04-28 11:03:33 by Aleos

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
## [BatElite/goonstation](https://github.com/BatElite/goonstation)@[bdad398f9e...](https://github.com/BatElite/goonstation/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Thursday 2022-04-28 11:10:22 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [rohittembhurne2194/ICTSBMALL_ULB](https://github.com/rohittembhurne2194/ICTSBMALL_ULB)@[71bdab48c5...](https://github.com/rohittembhurne2194/ICTSBMALL_ULB/commit/71bdab48c570a29a33294851db3edd4ebb07dfe4)
#### Thursday 2022-04-28 11:17:49 by umeshl@appynitty.com

Changes done By The Future milionaire or Billionaire persone and its me God is Great god always with i will be Millionaire in my 30s and is possible through my trading careear also in 2 years i open my youtube channel and guide people for their better future i wll be next healer ameen god blessed me thanku so much for support the gretest enery i love you...

---
## [sgrif/hollow_rando_im_stuck](https://github.com/sgrif/hollow_rando_im_stuck)@[e1d907a3ca...](https://github.com/sgrif/hollow_rando_im_stuck/commit/e1d907a3cafca12bfd560aa2410e47294b1e3f00)
#### Thursday 2022-04-28 13:38:55 by Sage Griffin

Use `TrackerLog.txt` instead of `TrackerDataWithoutSequenceBreaksPM.txt`

I was really surprised that this was able to work without knowing which
items the user had picked up, and finally we found the reason it can't
actually be that simple. Some items, such as the cloak, would unlock
more than one location if you could pick it up multiple times.

So this puts us in the not so great situation of needing the user to
give us that information. The only place where it's easily accessible in
a machine readable format is in the actual save file. But that's in a
different directory from the spoiler log, which for the web UI would be
painful to work with. I might consider it if we could take *only* that
file and not need the spoiler log, but the save doesn't include
information like the logic for each check, and the item placements also
would be difficult to reconstruct.

So that leaves us with the files in the randomizer's log files. Nothing
here has the information I need in a machine readable format, but
TrackerLog.txt has it in a form that at least is relatively easy to
crunch through without actually parsing it, so I've gone with that.

Since we know the actual locations that have been cleared, this means
we no longer need the TrackerData file that we were using before. That
file was nice to use since it had every reachable transition already
marked. Now that we're not using that file, I have to re-implement that
logic.

Additionally, the spoiler log doesn't include the actual transition data
when transition rando isn't turned on. So we need to include the vanilla
transitions in the binary. We will need additional logic to handle
transition rando, which I have not included in this commit.

At this point our logic really is starting to look like a shitty
implementation of prolog or datalog. It'll probably be worthwhile to
investigate using a library with an actual implementation of that type
of logic.

---
## [bellegarde-c/android_kernel_gnumdk_sm8150](https://github.com/bellegarde-c/android_kernel_gnumdk_sm8150)@[55be0c6357...](https://github.com/bellegarde-c/android_kernel_gnumdk_sm8150/commit/55be0c6357f112038cede0b1d2510260f2173325)
#### Thursday 2022-04-28 14:59:24 by Peter Zijlstra

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
## [LawrenceZ1A/MultipurposeProject](https://github.com/LawrenceZ1A/MultipurposeProject)@[6d844053d3...](https://github.com/LawrenceZ1A/MultipurposeProject/commit/6d844053d392ec1303e7b047113c4debbb8bb981)
#### Thursday 2022-04-28 15:05:13 by CuboidRaptor

TF LAWRENCE!

WHAT THE HELL?
STOP DELETING MY CODE.
IF IT BREAKS FOR YOU, THEN JUST DON'T USE IT.
IT'S NOT THAT DAMN HARD.

---
## [idan054/my_tests](https://github.com/idan054/my_tests)@[b309c64b68...](https://github.com/idan054/my_tests/commit/b309c64b68dec794033d6291962ef5657d8e34bd)
#### Thursday 2022-04-28 15:30:47 by Idan054

Scrape EASY.co.il

V6
+ Cookies user changed detection
+ bug fix because get_pen_msgs() sucks

V5 Requests.Stips Project: (Just better)
It's a mini projects, sorry for no details cuz I don't give a fuck

V2.1 Requests.Stips Project:
+ login_stips.py >> ReNamed >> A1_LoginStips.py
+ A23_OnlineNotification.py: get_notifications() & check_online_user()

V1 Requests.Stips Project:
 + main_stips.py
 + login_stips.py

---
## [jsgit21/Chikbot](https://github.com/jsgit21/Chikbot)@[ab8626473f...](https://github.com/jsgit21/Chikbot/commit/ab8626473fdce8bc41794c0b99413737ae5f07f0)
#### Thursday 2022-04-28 17:30:04 by Joe

Create README.md

# Chikbot
Chikbot was born as a passion project around the time Wordle became popular. For a while I knew I wanted to build a Discord bot and experiment with what potential it could bring to my Discord server. The initial inspiration was being able to track individual's Wordle scores from day to day as a bit of friendly competition. After getting comfortable with the Node.js module known as Discord.js (https://discord.js.org/#/) I began to implement other functionality as well as work to have it fully hosted on Heroku utilizing a PostgreSQL database for storing my data.

### User Stories

- [x] Implement basic commands/functionality for the bot to be utilized by users in the discord
- [x] Per user Wordle score tracking https://www.nytimes.com/games/wordle/index.html

#### Additional User Stories
- [x] Quordle support (Alteration of Wordle, web browser game; https://www.quordle.com/#/ )
- [x] Dad Joke API Implementation https://icanhazdadjoke.com/api
- [x] Magic The Gathering API Implementation https://docs.magicthegathering.io/
  - [x] Search for Magic The Gathering playing cards and display them to the user
- [ ] Create functionality for users to create Tasks/Goals list
- [ ] Implement self-assign user roles through Chikbot

---
## [bluca/systemd-stable](https://github.com/bluca/systemd-stable)@[0863a55ae9...](https://github.com/bluca/systemd-stable/commit/0863a55ae95fe6bf7312b7a864d07a9e3fbee563)
#### Thursday 2022-04-28 18:18:20 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>
(cherry picked from commit de90700f36f2126528f7ce92df0b5b5d5e277558)
(cherry picked from commit 367041af816d48d4852140f98fd0ba78ed83f9e4)

---
## [iawong/curriculum](https://github.com/iawong/curriculum)@[9c740aacfa...](https://github.com/iawong/curriculum/commit/9c740aacfa82b3abb39345c2f6fe042c271ca711)
#### Thursday 2022-04-28 18:34:55 by BMT-z

Add section for warnings about branch diversions

From personal experience and what I've seen in the git-help channel it seems like a few people are struggling with the issue of branch diversion, I'm still doing the html foundations and didn't realize making changes to my readme file via GitHub would cause the branch diversion issue, I think in git basics it should state that making any changes to your files via GitHub can cause issues and if you want to change even the readme file it's best to do it via a commit and push, I'm aware this is covered later on but i still believe making this a note in the git basics section would help a lot of users from running into this issue.

---
## [dfinity/motoko](https://github.com/dfinity/motoko)@[62752bb2f6...](https://github.com/dfinity/motoko/commit/62752bb2f6693d3af67f550e36a810967cbba5f7)
#### Thursday 2022-04-28 19:37:32 by Gabor Greif

feat: transform `for`-loops on arrays into `while`-loops (#2831)

## How it works

- we transform AST `ForE` loops by `Construct.whileE` _while_ lowering to IR
- the transformation kicks in when a `DotE` expression is applied to a value with an array type, by projecting out the `vals` accessor
- we get hold of the expression in the `DotE` node and use that (i.e. its constituents) as the starting point to obtain the array's size, and then index into it (for `keys` accessor the indexing is trivial)
- we build a classic `while` loop with an index running from zero below the size
- we don't distinguish between immutable/mutable arrays and also cater for potentially effectful loop bodies, as well as array expressions (and unit expressions passed to the call)
- we always CBV-bind the array expression to a variable (even if it is already a `VarE`, otherwise we end up in name capture hell)

## Pain points

We lose a bunch of source locations in the process of conversion to IR. This is not really a problem now, but will make the debugging experience less enjoyable some day.
 
## TODOs:
- [x] `FileCheck` on final IR
- [x] `async` (talk to @crusso)
- [x] `S.`-only transformation?
- [x] Are parens interfering? — No
- [x] test all combinations
- [ ] check why we have a perf regression

## Further optimisation opportunities
- eliminate unknown call following `call $@(im)mut_array_size`
- use `u32` arithmetic and indexing (currently _bignum_ calls)
- [x] we could optimise `DotE(..., "keys")` similarly — DONE

---
## [KingSaturn/TDemo-5-Timber](https://github.com/KingSaturn/TDemo-5-Timber)@[9a19e9b383...](https://github.com/KingSaturn/TDemo-5-Timber/commit/9a19e9b3831bd0bdb42061ddf6b50c7720df2622)
#### Thursday 2022-04-28 20:52:50 by Ethan Munday

Fixed the bullshit hidden Inventory bug

I had to manually load in the icon, material and model onto the items in the players inventory since they didn't load normally, this completely sucks and I hate this

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[855e1360c0...](https://github.com/microsoft/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Thursday 2022-04-28 21:17:17 by Mike Griese

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

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[a137c15a79...](https://github.com/BlueMemesauce/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Thursday 2022-04-28 21:44:45 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[903b74d4da...](https://github.com/mbs-octoml/mbs-tvm/commit/903b74d4dac721a7c5d09430973517888562f4fd)
#### Thursday 2022-04-28 22:11:15 by Mark Shields

** Collage v2 sketch ***

- Try again on python target changes, this time leave check_and_update_host_consist unchanged
- Revert python target changes to try again less agressively
- Few other cleanups
- Switch to 'external codegen targets' style
- Woops, run just_tvm after collage to pick up tuning logs
- Finish tuning for rtx3070
- Run them all!
- Update tuning logs
- Share global vars in the candidate function cache
- Finished tuning mobilenet, started on resnet50.
- Include model name in logs to make sure we don't get anything mixed up
- Drop -arch=sm_80
- Fix MaxCoalesce
- Attach external_symbol to lifted functions
- Add missing node registration, but leave VisitAttrs empty for now
- Make MaxCoalesce as aggressive as possible, since simple impl did not handle sharing.
- Finish tuning resnext50
- Improve coelescing
- Account for coelesced functions when outlining final module
- Fix caching, for real this time.
- More nn.conv2d autotvm tuning records, but still not done with resnext50_32_4d.
- OutlineExternalFunction both when preparing to estimate cost and after optimal
  partitioning applied.
- Use fp16 in TensorRT only if model's 'main_dtype' is float16.
- Fix CostEstimator caching issue
- More Target cleanup (while waiting for tuning runs)
- Better logging of candidates
- Support export to ONNX
- Fix merge
- Part-way through tuning for mobilenet.
- Add resnext50_32x4d
- Lift all "Compiler" functions before estimating to ensure no Relay passes are run on them
- Still trying
- Trying to track down weird failure in conv2d compute.
- Switch tensorrt to be fully pattern & composite function based
- Combiner rule for tuple projection
- Allow build to fail in estimate_seconds
- Add mobilenetv2 and resnet50v2 to menagerie
- Update CompilationConfig to handle target refinement
- Nuke remaining uses of TargetMap in favor of CompilationConfig
  (still needs to be pushed into python side)
- Save/Load dso libraries (needed for Cutlass with separated run)
- Move models into separate file
- gpt2_extract_16 and autotvm tuning log
- Handle missing tuning log files
- fp16 support in scalars and the tensorrt runtime.
- Wrap runner in nsys nvprof if requested
- Enforce strict compile/run time separation in preparation for profiling
- Better logging of final optimal partitioning and state of all candidates
- Fix handling of tuples and InlineComposites fixup pass.
- Fix TensorRT pattern bugs
- Pass max_max_depth via PassContext
- Better logging so can quickly compare specs
- BUG: Benchmark the partitioned rather than original model!!!
- Use median instead of mean
- Back to GPT2
- Make sure all function vars have a type
- Don't extract tasks if estimating BYOC-only
  (Was double-tuning every cutlass kernel).
- Make sure cudnn pattern table is registered
- Enable cudnn, get rid of support for op-predicate based BYOC integrations
- Enable cublas
- And yet another go at pruning unnecessary candidates.
- Another go at pruning unnecessary candidates
- Fix CompositePartitionRule use
- Fix a few bugs with new TensorRT pattern-based integration
- Rework RemoveSubCandidatesCombinerRule for soundness
- Better logging
- Bug fixes
- Implement critical nodes idea for avoiding obviously unnecessary candidates
- Promote DataflowGraph from alias to class so can cache downstream index set
- Quick check to avoid unioning candidates which would create a cycle
- Host out CandidatePartitionIndex and add rules to avoid small candidates subsumed by containing candidates
- GetFunction can legitimately return nullptr
- rename tuning log
- Support for int64 literals
- Switch GPT2 to plain model
- Fix library cloberring issue for cutlass
- actually checkin 'built in' tuning log (covers mnist & gpt2 only)
- trying to debug gpt2
- Update TargetKind attribute name
- working through gpt2 issues
- checkin tuning records for MNIST (with hack to not retry failed winograd)
- Autotvm tuning disabled if log file empty (default)
- Autotvm tuning during search working
- tune during search
  (but does not load tuned records after search!)
- About to add tuning to estimate_seconds
- Split out the combiner rules & make them FFI friendly
- Rework comments
- Estimate IRModule instead of Function (closer to meta_schedule iface)
- Add 'host' as first-class partitioning spec
  (Avoids special casing for the 'leave behind for the VM' case)
- Move CollagePartitioner to very start of VM compiler flow (not changing legacy)
- Fix bugs etc with new SubGraph::Rewrite approach
  Ready for updating RFC to focus on partitioning instead of fusion.
- Working again after partition<->fusion split.
- Add PrimitivePartitionRule
- Refactor SubGraph Extract/Rewrite
- Rename kernel->partition, fusion->partition
- Next: make nesting in "Primitive" an explicit transform
- respect existing target constraints from device planner
- make 'compiler' and 'fusion_rule' attributes avail on all target kinds
- moved design to tvm-rfcs, https://github.com/apache/tvm-rfcs/pull/62
- incorporate comments
- avoid repeated fusion
- fix trt type checking
- better logs
- pretty print primitive rules
- fix tensorrt
- multiple targets per spec
- don't extract candidate function until need cost
  Need to bring CombineByPrimitives back under control since lost depth limit.
- cleaned up fusion rule names
- added 'fuse anything touching' for BYOC
- Finish dd example
- Add notion of 'MustLower', even if a candidate fires may still need to consider
  leaving node behind for VM (especially for constants).
- starting example
- finished all the dd sections
- documentation checkpoint
- docs checkpoint
- more design
- starting on dd
- runs MNIST with TVM+CUTLASS+TRT
- cutlass function-at-a-time build
- need to account for build_cutlass_kernels_vm
- move cutlass tuning into relay.ext.cutlass path to avoid special case
- add utils
- don't fuse non-scalar constants for tvm target.
- stuck on cuda mem failure on conv2d, suspect bug in main
- where do the cutlass attrs come from?
- running, roughtly
- pretty printing, signs of life
- wire things up again
- Switch SubGraph and CandidateKernel to TVM objects
- naive CombineByKindFusionRule, just to see what we're up agaist
  Will switch to Object/ObjectRef for SubGraph and CandidateKernel to avoid excess copying.
- preparing to mimic FuseOps
- rework SubGraph to use IndexSet
- rough cut at MaximalFusion
- split SubGraph and IndexSet in preparation for caching input/output/entry/exit sets in SubGraph.
- top-down iterative handling of sub-sub-graphs
- about to give up on one-pass extraction with 'sub-sub-graphs'
- Add notion of 'labels' to sub-graphs
- Rework FusionRules to be more compositional
- partway through reworking fusion rules, broken
- SubGraph::IsValid, but still need to add no_taps check
- dataflow rework, preparing for SubGraph::IsValid
- explode into subdir
- mnist with one fusion rule (which fires twice) working
- switch to CandidateKernelIndex
- Confirm can measure 'pre-annotated' primitive functions
- checkpoint
- stuff
- more sketching
- dominator logging

---
## [dub-stack/chakra-radix-colors](https://github.com/dub-stack/chakra-radix-colors)@[733ee8c55a...](https://github.com/dub-stack/chakra-radix-colors/commit/733ee8c55ad5b4b6765a775ecfb13f025c6fc81a)
#### Thursday 2022-04-28 23:07:34 by Spencer Duball

test(checkbox): Holy shit that was painful. Looks like cypress caches  inbetween tests and doesn't refresh these until a new  with a different query happens???

---
## [JuliaLang/julia](https://github.com/JuliaLang/julia)@[62e0729dbc...](https://github.com/JuliaLang/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Thursday 2022-04-28 23:47:42 by Mirek Kratochvil

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

