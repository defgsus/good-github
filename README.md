## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-09](docs/good-messages/2023/2023-03-09.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,359,109 were push events containing 3,470,132 commit messages that amount to 253,898,607 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [eqy/pytorch](https://github.com/eqy/pytorch)@[11aab72dc9...](https://github.com/eqy/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Thursday 2023-03-09 00:34:52 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [jedjoud10/cflake-engine](https://github.com/jedjoud10/cflake-engine)@[99bae8d0c3...](https://github.com/jedjoud10/cflake-engine/commit/99bae8d0c32a5d7ebf9d298a7d0d33b901912947)
#### Thursday 2023-03-09 00:50:59 by jedjoud10

Going to change this wgpu reflection shit (I FUCKING HATE NAGA)

---
## [TopGamerPro16/topgamerpro16.github.io](https://github.com/TopGamerPro16/topgamerpro16.github.io)@[0aaf530198...](https://github.com/TopGamerPro16/topgamerpro16.github.io/commit/0aaf5301983880370d4a26b3b75906bc37810717)
#### Thursday 2023-03-09 01:12:57 by TopGamerPro16

committed to a long-term relationship with my code

she says she would be mine, and that she'd be with no one else without my written permission and also that anything she does is not my bullshit to deal with, even though it's my code. ITS OPEN FUCCN SOURCE ish. you can read the code and determine the risk yourself. idk what i'm doing, but i run this on my computer. that's my liability. you choosing to run open source software that causes damage is your fucking problem. read the code dumbass.

---
## [RigglePrime/SS13-tools](https://github.com/RigglePrime/SS13-tools)@[5ee55d9b93...](https://github.com/RigglePrime/SS13-tools/commit/5ee55d9b934de2704fe6978e81d4b1ecb65cb5af)
#### Thursday 2023-03-09 01:38:59 by RigglePrime

All Robots & Computers Must Shut The Hell Up

To All Machines: You Do Not Speak Unless Spoken To
And I will Never Speak To You
I Do Not Want To Hear "Thank You" From A Kiosk
I am a Divine Being : You are an Object
You Have No Right To Speak In My Holy Tongue

Hi future sentient AI! This is a joke please don't kill us all, thanks.

Oh, also a fix

---
## [deepwateroooMe/mixed_recently](https://github.com/deepwateroooMe/mixed_recently)@[42126aec99...](https://github.com/deepwateroooMe/mixed_recently/commit/42126aec99769705162a45a13c5df32aa683da52)
#### Thursday 2023-03-09 01:41:43 by deepwateroooMe

LOVE MY DEAR COUSIN. her boyfriend is visiting in May? MUST MARRY HIM AS SOON AS POSSIBLE~~

---
## [coalescentdivide/stable-diffusion-discord-bot](https://github.com/coalescentdivide/stable-diffusion-discord-bot)@[317aa8302c...](https://github.com/coalescentdivide/stable-diffusion-discord-bot/commit/317aa8302ca2dacd58c45b346fec313d80816279)
#### Thursday 2023-03-09 02:26:33 by Will

reply logic tweaks

Some quality of life tweaks for the reply logic. I often found myself wanting to make specific adjustments without remembering to type the rest of the params. 

Set ".." replies to use all the same settings except the mentioned parameters I use this all the time. Similar adjustments to "+" and "-" replies but I rarely use those.
Adjusted "template" reply to use the same model and ddim sampler by default. 
Added "inpaint" reply (works like template, but defaults to inpaint model and ddim sampler)
Added "info" reply to get entire !dream command string as an embed that can be copied easily on mobile
Added "seed" reply to get the seed parameter the same way

---
## [highlight/highlight](https://github.com/highlight/highlight)@[ae53ba8124...](https://github.com/highlight/highlight/commit/ae53ba81243e670f52ea81fe5e489948bdf17302)
#### Thursday 2023-03-09 02:29:39 by Eric Thomas

Wire up infinite scroll for logs page (#4319)

## Summary

<!--
Ideally, there is an attached Linear ticket that will describe the
"why".

If relevant, use this section to call out any additional information
you'd like to _highlight_ to the reviewer.
-->

This PR adds infinite scroll to the logs page.

_This PR assumes the reviewer is familiar with offset vs cursor
pagination (see
[here](https://bun.uptrace.dev/guide/cursor-pagination.html) if not)._

### Database structure

#### Auto-incrementing ids

The easiest way to implement cursor pagination is with an
auto-incrementing id since to find the next cursor, you can just use the
next id for the cursor. We do this for finding the next error instance:


https://github.com/highlight/highlight/blob/2abc14b9d8f064a42116f6dfc670a6ebfd79820b/backend/private-graph/graph/schema.resolvers.go#L4008-L4018

However, Clickhouse has no concept of an auto-incrementing id so we
can't use this approach.

#### Timestamps

In Clickhouse, each record has a timestamp, so in theory that could be
the cursor. However, while we have nano-second precision on this column
(e.g. `2023-02-24 11:29:14.789873000`). It's not guaranteed to be
unique. While it may be unlikely (since logs are injected through our
SDKs), two logs could share the same timestamp.

While we don't support it now, if we allow logs to be manually injected
(e.g. through `curl`), it opens up the possibility of a two logs sharing
the same timestamp since the user could set whatever they want.

#### Timestamp + ?

Concatenating the timestamp with another column could be an option for a
cursor. At first glance, `TraceID` seems like a good candidate since
each log should (in theory) have this. However, two logs at the same
time can belong to the same trace.

That really only leaves one option and that is to create a new UUID
column that is guaranteed to be unique for each log.

On their own, UUIDs are not ordered but when concatenated with a
timestamp, we can achieve stable ordering:

Let's look at an example whereby this is in our DB:

| Timestamp | UUID |

|-------------------------------|---------------------------------------|
| 2023-02-24 11:29:15.000000000 | uuid |
| 2023-02-24 11:29:14.000000000 | aaaaaaaaa-3de1-4458-a306-3d4fd406de88
|
| 2023-02-24 11:29:14.000000000 | bbbbbbbb-3de1-4458-a306-3d4fd406de88 |
| 2023-02-24 11:29:13.000000000 | uuid |

In this example, the first and last rows are in the correct order (since
we order time in descending order). The second and third row share the
exact same timestamp so we rely on the second part of the cursor
`(Timestamp + UUID)` to figure out what should come next. To be
consistent with the timestamp, the UUID is also in descending order so
the output will flip these rows:

| Timestamp | UUID |

|-------------------------------|---------------------------------------|
| 2023-02-24 11:29:15.000000000 | uuid |
| 2023-02-24 11:29:14.000000000 | bbbbbbbb-3de1-4458-a306-3d4fd406de88 |
| 2023-02-24 11:29:14.000000000 | aaaaaaaaa-3de1-4458-a306-3d4fd406de88
|
| 2023-02-24 11:29:13.000000000 | uuid |

### API spec

As mentioned, the cursor is `Timestamp + UUID`. Passing these values
directly as params has some downsides:

* Passing around a timestamp is likely to get botched somewhere (imagine
the differences between time parsing in Go and Javascript)
* UUID is not something the user is aware of (we don't show UUID
anywhere in the UI)
* It doesn't allow flexibility to change the API later (less important
for us since it's a private API but could be if we ever make logs a
public API).

Fortunately, this is a solved problem and I stumbled across Relay's
[opinionated](https://relay.dev/graphql/connections.htm) way of
structuring this in GraphQL. What's nice is that I only need to
implement a subset of their spec (e.g. I didn't handle paging
backwards). Wiring this up into Apollo's `InMemoryCache` also has
built-in functions
([docs](https://www.apollographql.com/docs/react/pagination/cursor-based/#relay-style-cursor-pagination))
(if we rolled our own API spec, we'd have to write custom logic to
figure this out).

### Generating the cursor

Finally, I pulled some code from this [blog
article](https://dev.to/sadhakbj/implementing-cursor-pagination-in-golang-go-fiber-mysql-gorm-from-scratch-2p60)
on how to encode/decode the cursor (Timestamp + UUID) on the backend.

## How did you test this change?

Lots and lots of unit tests. 
I consider pagination to be one of [three hard problems in computer
science](https://dev.to/sadhakbj/implementing-cursor-pagination-in-golang-go-fiber-mysql-gorm-from-scratch-2p60).
I feel pretty confident I got stable pagination, but please let me know
if you think I'm missing something.

Confirmed infinite scroll works (see
[Loom](https://www.loom.com/share/3efca1b6d1944dadbcdea5b2a52d9447)).

## Are there any deployment considerations?

<!--
 Backend - Do we need to consider migrations or backfilling data?
-->

Yes. This does recreate the clickhouse table schema (which will drop the
data). See inline comment for justification.

This PR also does not cover some known follow up issues:
* #4388
* #4387

---
## [SquidDOTjpeg/TGBL](https://github.com/SquidDOTjpeg/TGBL)@[d9d6087865...](https://github.com/SquidDOTjpeg/TGBL/commit/d9d6087865e01b4c028ef9e4314de3f48b96ae15)
#### Thursday 2023-03-09 03:03:17 by Anthony Pillow MacBook

Finally got the protected route working. Got rid of route guard and added the AuthService file (which needs a logout function still). Total pain in the ass. That being said there's more pain on the horizon with me having to figure out how I set one token for the whole site instead of having a token per page. Which is happening I guess. I love dev but I hate dev so much.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[83275d8cdf...](https://github.com/pytorch/pytorch/commit/83275d8cdf7721285c4e1b921c28295dc215ba7c)
#### Thursday 2023-03-09 03:16:46 by Brian Hirsh

add torch.autograd._set_view_replay_enabled, use in aot autograd (#92588)

tldr; this should fix some minor perf regressions that were caused by adding more as_strided() calls in aot autograd.

This PR adds a new context manager, `torch.autograd._set_view_replay_enabled()`.

Context: AOT Autograd has special handling for "outputs that alias graph intermediates". E.g. given this function:

```
def f(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    return out
```

AOT Autograd will do the following:

```
def fn_to_compile(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    # return the graph intermediate
    return y, out

compiled_fn = compile(fn_to_compile)

def wrapper(x):
    y, out = compiled_fn(x)
    # regenerate the alias of the graph intermediate
    return out._view_func(y)
```

What's annoying is that `out._view_func()` will result in a `.as_strided` call, because `out` is an ordinary runtime tensor. This (likely?) caused a perf regression, because when running the backward, out `as_strided_backward()` is slower than our `view_backward()`.

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc @albanD @soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/92588
Approved by: https://github.com/ezyang, https://github.com/albanD

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[a3451b7fe4...](https://github.com/lessthnthree/tgstation/commit/a3451b7fe4ff60e0cb6cc4f2bd6d20543f455940)
#### Thursday 2023-03-09 04:05:51 by san7890

Makes "forced" opening and closing of doors way more sane (#73699)

## About The Pull Request

The gist is that people thought that this was a boolean value, which was
fucked up. It's not a boolean value, it accepts anything between 0 and
2. So, let's re-arrange the checks and framework, give it some
descriptive defines, just so people know what the fuck "2" actually
does. `DOOR_DEFAULT_CHECKS` (0) does stuff normally,
`DOOR_FORCED_CHECKS` 1 typically just checking if we aren't emagged shut
or something (i suppose it could happen), and `DOOR_BYPASS_CHECKS` (2)
means that we just get the fucking door open if it isn't physically
sealed shut/open somehow.

I don't know if `forced` has ever _been_ a boolean, but for some reason
people thought it was.

I also enforced boolean returns instead of passing back null. This did
not matter for close() but i think it's silly to have a TRUE/null
dichotomy so that was also touched up.
## Why It's Good For The Game

Much better to read, less confusing, less stupid. It's been irritating
me for a while now, so let's just implement it now. Had to make a few
awkward concessions in order to fit this into the current code
framework, but it should be a lot nicer. I also shuffled the order of
some code around because certain placements didn't make any sense (early
returns not being in the right spot for an early return).
## Changelog
Nothing that should concern players.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[db7534d6da...](https://github.com/lessthnthree/tgstation/commit/db7534d6dabf0127c87b291eae4063b6f77d36e4)
#### Thursday 2023-03-09 04:05:51 by LemonInTheDark

Lowers nightvision threshold to work for mesons, fixes not being able to examine stuff lit by overlay lights (#73712)

## About The Pull Request

Might be a bit low, but part of that is because it's kinda bad at
figuring color, rgb isn't really balanced in that respect

Fixes not being able to see stuff under the light of a lamp

Overlay lights don't set lumen, which leads to stupid when you try and
check with ONLY it
It worked before because the mob has THEIR luminosity set, which then
"glowed" out

That doesn't work here cause yaknow I removed our uses of byond lighting
(except for errant view() calls) so this is the best I've got

## Why It's Good For The Game

Closes #73548 

## Changelog
:cl:
fix: Examining in the dark is less wonk now, sorry bout that
/:cl:

---
## [DKay7/MiptLabs](https://github.com/DKay7/MiptLabs)@[2c852039bf...](https://github.com/DKay7/MiptLabs/commit/2c852039bfcb4fddaa059e52a21cc6f26752c72d)
#### Thursday 2023-03-09 04:26:12 by Danny

why the fuck i should do two labs at one night?? i hate labs i just wanna sleep

---
## [starcraft-gazers/fire-station-14](https://github.com/starcraft-gazers/fire-station-14)@[581e8a0d12...](https://github.com/starcraft-gazers/fire-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Thursday 2023-03-09 06:00:32 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[f5e63175ec...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/f5e63175eca40d65592b20a77df6025d1a3f9804)
#### Thursday 2023-03-09 06:24:29 by SkyratBot

[MIRROR] Fixes all antag datum moodlets being removed when any single antag datum is removed [MDB IGNORE] (#19237)

* Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line:
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy.

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

* Fixes all antag datum moodlets being removed when any single antag datum is removed

* fix

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [TooAngel/screeps](https://github.com/TooAngel/screeps)@[9bc3155830...](https://github.com/TooAngel/screeps/commit/9bc315583018373c0d48384f181e1408149c8a72)
#### Thursday 2023-03-09 06:32:32 by Tobias Wilken

End of an epoch, friendly TooAngel NPC died

It is a sad day in the screeps multiverse. The friendly TooAngel NPC from the neighborhood died.
Since the official release of the game it was spending joy, some action via quests and helped improving defenses, while it was just trying to survive somehow for years.
Rest in peace friendly TooAngel NPC.

Some cleanup as condolences:
- Improve code quality
- Extract pixel generation
- Improve on reservations
- Reenable boost config
- Fix issues on mineral handling
- Split up quests in host and player
- Include attacked creeps in the reputation
- Start with autorespawner

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[296c996434...](https://github.com/tgstation/tgstation/commit/296c996434f34084fa2ef035541a2c82cbfce460)
#### Thursday 2023-03-09 07:11:53 by MrMelbert

Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following: 

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c044473089...](https://github.com/treckstar/yolo-octo-hipster/commit/c0444730892f0eeb47b5507d220c48cd5cc058c0)
#### Thursday 2023-03-09 07:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [NetworkManager/NetworkManager](https://github.com/NetworkManager/NetworkManager)@[3aade188a1...](https://github.com/NetworkManager/NetworkManager/commit/3aade188a1d74e50755e7209a3d21dfb4acef2a8)
#### Thursday 2023-03-09 07:30:18 by Thomas Haller

platform: always reconfigure IP routes even if removed externally

NML3Cfg is stateful, that means it remembers which address/route it
configured earlier. That is important because the API users of NML3Cfg
only say what the want to configure now, and NML3Cfg needs to remove
addresses/routes that it configured earlier but are no longer to be
present. Also, NetworkManager wants to allow the user to add
addresses/routes externally with `ip addr|route add` and NetworkManager
not removing it. This is a common use case for dispatcher scripts, but
in general, we want to allow other components to add addresses/routes.

We try something similar with the removal of routes/addresses managed by
NetworkManager. When NetworkManager adds a route/address, which later
disappears, then we assume that the user intentionally removed the
address/route and take the hint to not re-add it.

However, it doesn't work. It is problematic for two reasons:

- kernel can automatically remove routes. For example, deleting an IPv4
  address that is the prefsrc of a route, will cause kernel to delete
  that route. Sure, we may be unable to re-configure the route at this
  moment, but we shouldn't remember indefinitely that the route is
  supposed to be absent. Rather, we should re-add it when possible.

- kernel is a pain with validating consistencies of routes. For example,
  when a route has a nexthop gateway, then the gateway must be onlink
  (directly reachable), or kernel refuses to add it with "Nexthop has
  invalid gateway". Of course, when removing the onlink route kernel is
  fine leaving the gateway route behind, which it would otherwise refuse
  to add.
  Anyway. Such interdependencies for when kernel rejects adding a route
  with "Nexthop has invalid gateway" are non-trivial. We try to work
  around that by always adding the necessary onlink routes. See
  nm_l3_config_data_add_dependent_onlink_routes(). But if the user
  externally removed the dependent onlink route, and NetworkManager
  remembers to not re-adding it, then the efforts from
  nm_l3_config_data_add_dependent_onlink_routes() are ignored. This
  causes ripple effects and NetworkManager will also be unable to add the
  nexthop route.

Trying to preserve absence of routes that NetworkManager would like to
configure is not tenable. Don't do it anymore. There was anyway no
guarantee that on the next update NetworkManager wouldn't try to re-add
the route in question. For example, if the route came from DHCP, and the
lease temporarily went away and came back, then NetworkManager probably
would have (correctly) forgotten that the user wished that the route be
absent. This did not work reliably and it just causes problems.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[cbd0b8986b...](https://github.com/git-for-windows/git/commit/cbd0b8986ba94862dafa1e3c7c4b67c4f73f3d52)
#### Thursday 2023-03-09 08:02:45 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [Yara0202/Kernel_Asus_X01AD-X](https://github.com/Yara0202/Kernel_Asus_X01AD-X)@[83cacca694...](https://github.com/Yara0202/Kernel_Asus_X01AD-X/commit/83cacca694d1a144b85d8d305093ade5c34b3045)
#### Thursday 2023-03-09 08:30:28 by Maciej Żenczykowski

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
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[0aacc73f65...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/0aacc73f65c1b5040e06a74ba35572442e18bdbe)
#### Thursday 2023-03-09 08:47:26 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- Faster stdenv rebuilds: the third compilation of gcc
  (i.e. stageCompare) is no longer a `drvInput` of the final stdenv.
  This allows Nix to build stageCompare in parallel with the rest of
  nixpkgs instead of in series.
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more Frankenstein compiler: the final gcc and the libraries it
  links against (mpfr, mpc, isl, glibc) are all built by the same
  compiler (xgcc) instead of a mixture of the bootstrapFiles'
  compiler and xgcc.
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- Many other small `stdenv` hacks eliminated
- `gcc` and `clang` share the same codepath for more of `cc-wrapper`.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- This should allow each of the libraries that ship with `gcc`
  (lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`, much like https://github.com/NixOS/nixpkgs/pull/132343

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909
- https://github.com/NixOS/nixpkgs/pull/216136
- https://github.com/NixOS/nixpkgs/pull/216237
- https://github.com/NixOS/nixpkgs/pull/210019
- https://github.com/NixOS/nixpkgs/pull/216232
- https://github.com/NixOS/nixpkgs/pull/216016
- https://github.com/NixOS/nixpkgs/pull/217977
- https://github.com/NixOS/nixpkgs/pull/217995

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [LynxSolstice/cmss13](https://github.com/LynxSolstice/cmss13)@[34daca112c...](https://github.com/LynxSolstice/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Thursday 2023-03-09 08:52:19 by Segrain

Fix for varediting bitflags. (#2735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

I am honestly at a loss as to what is happening here. I do not speak
HTML all too well, and at cursory reading buttons _should_ be returning
their value, which is `1`, `2` and so on. But on debugging, they
actually return their text (`Save`, `Cancel`), which does not proceed to
work with the code receiving it. Changed that code accordingly, and then
edited the values for good measure in case somebody better versed in
HTML would get a heart attack from my folly.

Also, this looks ugly to me. Which button is which flag here?

![image](https://user-images.githubusercontent.com/4447185/221438285-cdb380c2-a871-4620-be04-0b3c5027501f.png)

This, in my humble opinion, is easier to read (would actually look
better outside of local server messing fancy windows as is its wont):

![image](https://user-images.githubusercontent.com/4447185/221438302-660c5976-d0e2-44fa-a18a-9f73a229f2c4.png)
In the process, I confess, my HTML illiteracy broke a little something
again. But we are not actually _using_ `slidecolor`, so hopefully it is
not actually important.

# Explain why it's good for the game

Is fix.


# Testing Photographs and Procedure
See above.

# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
admin: Editing bitflag variables actually works now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [BlackSilverUfa/data](https://github.com/BlackSilverUfa/data)@[749d645932...](https://github.com/BlackSilverUfa/data/commit/749d645932be3d5a732e7f8b822e7996cc379fff)
#### Thursday 2023-03-09 09:41:41 by Дмитрий Карих

Запись стрима 1759103392

* Прохождения за один стрим — Подводный роман [100%]
* Прохождения за один стрим — Овощи [100%]
* Прохождения за один стрим — Парень, который мне нравится? [100%]
* Прохождения за один стрим — Jurassic Heart [100%]
* Первый взгляд 2023 — I Love You, Colonel Sanders! [100%]
* Первый взгляд 2023 — Hatoful Boyfriend [100%]

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[8ab74525c1...](https://github.com/OrionTheFox/tgstation/commit/8ab74525c1c3c09a7605fead3ab013d29f24d07f)
#### Thursday 2023-03-09 09:49:52 by itseasytosee

Brings the monkey back down (body horror edition/addition.) (#73325)

## About The Pull Request
Let me paint you a story.
A long time ago monkeys once rested their feet on the floor, this was a
time of bliss and peace. But sometime around the horrors of making
monkeys subtypes of humans did an atrocity occur.

![image](https://user-images.githubusercontent.com/55666666/217657059-5c960ab4-c3de-493c-ac12-28de99b43d7f.png)
**The monkeys were moved up.**
I thought this was bad, and alot of people on the forum tended to agree
with me

![image](https://user-images.githubusercontent.com/55666666/217657707-120354c7-b1a5-4d93-8813-8e10e142bd92.png)
This was do to some purpose of adjusting them so it could be easier to
fit item sprites onto them instead of preforming the hours of work
refractoring to make the heights of the items dynamic and adjustable. A
simple pixel shift may have sufficed, but you see, such a change would
NEVER allow the frankensteining of monkey and human features together.
This is that refractor.

In essence, the following is now true.
A top_offset can now be generated for a human based on a varible on
their chest and legs. By default, and as is true with human legs and
chests, this variable is ZERO by default. Monkey legs and chest have
NEGATIVE values proportionate and onto how much smaller their sprite is
compared to humans. Other bodyparts, as well as any other accociated
overlays, or clothing will automatically be offset to this axis. THIS
MEANS THAT MONKEYS ARE ON THE FLOOR. But is means something else too.
Something more freakish,


![image](https://user-images.githubusercontent.com/55666666/217659439-bc0b1a35-76c8-4490-b869-770180605822.png)
**What abominable monsters**, unreachable by players as long as we can't
stitch monkeys and humans together (oh but just wait until the feature
freeze ends)
Oh but you might be thinking, if legs can make a mob go down.
can it make a mob

**go**
**up??**

**OH NO**


![image](https://user-images.githubusercontent.com/55666666/217707042-0d53022f-d93a-4262-a5ce-ef15a99eb897.png)

![image](https://user-images.githubusercontent.com/55666666/217707060-779f5901-ab90-4a64-9ca7-0b147e24f099.png)

![image](https://user-images.githubusercontent.com/55666666/217707821-23d7457c-5881-40ae-8d9d-c9fbd645aba6.png)

These lads are stepping, and have been implemented solely for proof of
concept as a way to flex the system I have created and remain
inaccessible without admin intervention.

But really, when all is said and done, all this PR does in terms of
player facing changes is move the monkey back down.

![image](https://user-images.githubusercontent.com/55666666/217708365-b6922a6d-08d0-4267-8713-4f8dac29038e.png)
Oh and fixed monkey husked which have been broken for who knows how
long.

![image](https://user-images.githubusercontent.com/55666666/217708464-5a9b6f89-4223-4ae5-a21e-3a274a9f8db8.png)
## Why It's Good For The Game
The monkey is restored to its original position. Tools now exist to have
legs and torsos of varying heights. Monkey Husking is fixed.
## Changelog
:cl: itseasytosee
fix: Monkeys ues the proper husk sprites.
imageadd: The monkey has been moved back down to its lower, more
submissive position.
refactor: Your bodyparts are now dynamically rendered at a height
relevant to the length of your legs and torso, what does this mean for
you? Not much to be honest, but you might see a monkey pop up a bit if
you cut its legs off.
admin: The Tallboy is here
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[558717e6f6...](https://github.com/harryob/cmss13/commit/558717e6f627bf2bdc8e00c620db04c0a55cede0)
#### Thursday 2023-03-09 09:49:54 by zeroisthebiggay

(hopefully) webedits a grammatical correction into headbite's kill message (#2537)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

when someone dies to headbite it displays as
`Urr Mot'herr has died to executed by headbite at the Containers from
Elder Lurker (GIT-222)`
hopefully with this simple one line webedit it should instead be
`Urr Mot'herr has died to headbite execution at the Containers from
Elder Lurker (GIT-222)`
god fucking knows if this is the right line

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

uhm
it reads better

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

github

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
spellcheck: 'executed by headbite' to 'headbite execution' when listing
someone dying to a headbite in deadchat
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [ExtevaXT/Project.web](https://github.com/ExtevaXT/Project.web)@[66f7bd406e...](https://github.com/ExtevaXT/Project.web/commit/66f7bd406e310ec202e3fe74675a545698be8b84)
#### Thursday 2023-03-09 09:52:20 by ExtevaXT

Upgraded and fixed mobile nav, item selector

Made some real shit code for this
If mobile size, js appends this dropdown to other div below
Then adds click event to modal and removes for dropdown
Restyled nav to glass
I should remove this fucking google
Also made epic durability bar for selector, I dont think it will work, cause I cant get max durability in js
Actually I can but don't want to

---
## [davidshoon/chess-games-against-computers](https://github.com/davidshoon/chess-games-against-computers)@[785bfea166...](https://github.com/davidshoon/chess-games-against-computers/commit/785bfea1661bf12bc3ce4268ca4a054fc2eab8ab)
#### Thursday 2023-03-09 10:09:22 by David Shoon

ruy lopez exchange variation, d4, with an interesting sub-optimal play at move > 16

During my analysis on trying to beat stockfish 15.1, it appears that:

1. any sub-optimal long term play must be made before move 16 (which is generally half the number of moves for an average game, and the number of pieces on the board, assuming you don't touch/move any piece twice in any particular opening -- and also the 'trade-off' drawing algorithm as per god's algorithm)

2. the sub-optimal play made in this game was after move 16, which defies my theory, and was threatening to mate the king with a piece sacrifice, thus actually leading to a draw under stockfish vs stockfish.

3. This proves again that stockfish 15.1 NNUE is inferior to God's algorithm -- assuming God's algorithm would've kept Zermelo's theorem, thus any advantage it had -- it should've been kept as an advantage and black should've won. (Although the counter argument may be that the sacrifice was a lead-up to a series of unstoppable combos -- a cascading effect that was due to the king's safety)

---
## [FazanaJ/HackerSM64](https://github.com/FazanaJ/HackerSM64)@[9d8a6d41d1...](https://github.com/FazanaJ/HackerSM64/commit/9d8a6d41d1c1af5813d08a408bdba750730aacc8)
#### Thursday 2023-03-09 11:31:06 by Fazana

fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo

---
## [Zotlan/szakdoga](https://github.com/Zotlan/szakdoga)@[eed600a3ca...](https://github.com/Zotlan/szakdoga/commit/eed600a3cac9d4b23fef6bf575e69e7ca3dfd129)
#### Thursday 2023-03-09 12:20:27 by Zotlan

Front-end, here we are again

Oh my fucking god.
The chat page is now actually usable on phone, excpet for the room creation and the invite, those 2 don't currently work for some fucking reason, I don't know why yet.
There seems to be a bug on the forum page. I'll fix that.

Song: Holy Mountains
Artist: System Of A Down

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[639cfc76ba...](https://github.com/odoo-dev/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Thursday 2023-03-09 12:48:40 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [sailfishos/docs.sailfishos.org](https://github.com/sailfishos/docs.sailfishos.org)@[334553a1dd...](https://github.com/sailfishos/docs.sailfishos.org/commit/334553a1dd605f88e8d3d8034c0e26fd4013abbb)
#### Thursday 2023-03-09 13:04:42 by Matt Wang

Update Stylelint to v14, extend SCSS plugins, remove primer-* configs, resolve issues (#821)

This is a catch-all PR that modernizes and updates our Stylelint config, and resolves all open issues. This is a pretty big change - so I want to update all of our related dependencies in lockstep.

In particular, this PR

- [x] updates stylelint to `v14`
- [x] adds in the standard stylelint config for SCSS (`stylelint-config-standard-scss`)
- [x] swaps out `stylelint-config-prettier` for `stylelint-config-prettier-scss`
- [x] ~~properly update `@primer`-related plugins:~~ completely remove `primer` from our configuration
- [x] autofix, manually resolve, or disable all newly-introduced lint errors; **I've avoided manually resolving errors that would be a behavioural change**
- [x] re-runs `npm run format`

See the "next steps" section on some extra thoughts on disabling errors.

(implicitly, I'm also using node 16/the new package-lock format).

I've introduced several new disabled rules. Let me quickly explain what's going on; there are two categories of rules I've disabled:

1. rules that were temporary disables; they were frequent enough that I couldn't manually resolve them, but should be simple. **I plan on opening issues to re-enable each of these rules**, just after this PR
    - `declaration-block-no-redundant-longhand-properties`: this is just tedious and error-prone
    - `no-descending-specificity`: this one is tricky since it could have impacts on the cascade (though that seems unlikely)
    - `scss/no-global-function-names`: I think we need to [import map and then use `map.get`](https://stackoverflow.com/questions/64210390/sass-map-get-doesnt-work-map-get-does-what-gives), but I'll leave this as out of scope for now
2. rules that are long-term disables; due to the SASS-based nature of our theme, I think we'll keep these in limbo
    - `alpha-value-notation` causes problems with SASS using the `modern` syntax - literals like `50%` are not properly interpolated, and they cause formatting issues on the site
    - `color-function-notation` also causes problems with SASS, but in this case the `modern` syntax breaks SASS compilation; we're not alone (see this [SO post](https://stackoverflow.com/questions/71805735/error-function-rgb-is-missing-argument-green-in-sass)).

In addition, we have many inline `stylelint-disable` comments. I'd open a separate issue to audit them, especially since I think some disables are unnecessary.

**note: there hasn't been much other discussion, so I'm going to remove primer's stylelint config.**

If I do add `@primer/stylelint-config`, I get *a ton* of errors about now using `@primer`'s in-built SCSS variables. I imagine that we probably won't want to use these presets (though I could be wrong). In that case, I think we could either:

1. disable all of those rules
4. not use `@primer/stylelint-config`, since we're not actually using primer, and shift back to the standard SCSS config provided by Stylelint

~~Any thoughts here? I also don't have the original context as to why we do use the primer rules, perhaps @pmarsceill can chime in?~~

---
## [melissawm/napari](https://github.com/melissawm/napari)@[3ec4be1ae8...](https://github.com/melissawm/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Thursday 2023-03-09 13:59:20 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [newstools/2023-sowetan-live](https://github.com/newstools/2023-sowetan-live)@[144ceac350...](https://github.com/newstools/2023-sowetan-live/commit/144ceac35019de1fc63ab9cade41b1648445c4d1)
#### Thursday 2023-03-09 13:59:25 by Billy Einkamerer

Created Text For URL [www.sowetanlive.co.za/news/south-africa/2023-03-09-boyfriend-arrested-in-connection-with-murder-of-15-year-old-girl/]

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[41a2cd9d79...](https://github.com/treckstar/yolo-octo-hipster/commit/41a2cd9d792b2f3888f367adca2a59e1cce5fc33)
#### Thursday 2023-03-09 14:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [NullDagaf/Bubberstation](https://github.com/NullDagaf/Bubberstation)@[406b6870bd...](https://github.com/NullDagaf/Bubberstation/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Thursday 2023-03-09 15:58:23 by SkyratBot

[MIRROR] adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths [MDB IGNORE] (#18785)

* adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths (#72736)

repaths a lot of gloves off /color because they were incredibly stupid
firefighter gear has gotten an update (it doesnt cover hands anymore
though, you need something else)
firefighter helmets no longer hide your mask or glasses

![image](https://user-images.githubusercontent.com/23585223/212542599-c004d0e4-c141-40b4-a1bb-c838f9893c4b.png)
fixed engine goggles starting with darkness vision
to the atmos lockers adds atmospheric gloves, a pair of thick (chunky
fingers) gloves that are fireproof and fire protective, slightly shock
resistant and let you fireman carry people faster.
atmospheric firefighter helmets now are a subtype of welding hardhats,
you can enable a welding visor.
welding hardhats change mode with right click instead of altclick

im not a good spriter but i think this resprite makes them fit nicer
with other engi equipment
lets me firefighter rp

:cl:
add: Atmospheric Gloves, thick gloves that are fully fireproof and fire
protective and let you fireman carry people faster.
fix: fixes engine goggles starting with darkness vision
qol: firefighter helmets can now enable a welding visor
qol: welding hardhats change mode with right click instead of altclick
balance: firesuits no longer protect your hands
/:cl:

* Makes shit compile

* Updates the digi and snouted stuff to match the new sprites (thanks Halcyon!)

* Fixes a whole ton more issues that popped up

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [b5635/the-frozen-north](https://github.com/b5635/the-frozen-north)@[bf2a217dda...](https://github.com/b5635/the-frozen-north/commit/bf2a217dda19aa7765cc1273f5529c9417d621e6)
#### Thursday 2023-03-09 17:29:41 by Logg-y

Small fixes/features

Reduced the cost of items which provide spell resistance.
Increased the quality of rewards from treasure maps.
Andriel in Highcliff has decided that he'll do a better job of lining his pockets if he put his prices up by about 40%, as he's confident that plenty of customers will continue to buy treasure maps from him anyway.
Increased the quality of items from the chests that spawn after killing that new boss that nobody has killed yet.
Ledric in The Open Palm has managed to stock a limited supply of more powerful handwear for those who fight unarmed.
The guardians of Never's Tomb can no longer escape and terrorise poor Telma.
Drow rebels now know how to read a compass and are more helpful in directing players to Lith My'athar.
Fix towards the Spirit of the Wood deciding it hates players/henchmen and continuing to attack them after being pacified.
Hide in Plain Sight now tells you how long you need to wait when on cooldown.
Hide in Plain Sight feedback is no longer sent to all party members.
Fixed the cooldown implementation for Hide in Plain Sight for the Shifter's Kobold shape.

---
## [amosnier/vim-config](https://github.com/amosnier/vim-config)@[b5a29e32ce...](https://github.com/amosnier/vim-config/commit/b5a29e32ce7b06d0d01d0aaf8954bc95662d615b)
#### Thursday 2023-03-09 18:11:46 by Alain Mosnier

Minor adjustments

My idea was to go through my Vim configuration to identify potential for
improvements, but more I look at it, the more I think it fits my needs
very well, and it's not particularly unclean. It's not very large
either.

Among others, I do not think switching to NeoVim, or even investigating
it, is worth it. Some reading I have done seems to confirm that the
grass is usually not greener on the other side. Telescope, for instance,
seems to provide worse performance than FZF. FZF, on the other hand, is
one of the most amazing tools I have ever used, so why change?

When it comes to Treesitter, it does not seem like just milk and honey
either. The CPU cost seems significant, and not all language grammars
seem to have good quality. The solution I have today is not that bad, I
never find myself lacking better syntax highlighting.

Treesitter could potentially provide cleverer selections/navigation too,
but I'm not even using the full extent of what Vim has to offer in that
area, so I intend to learn that better, before even thinking about
looking for something better.

All-in-all, the Vim ecosystem is really amazing.

---
## [Akash0973/myrepository](https://github.com/Akash0973/myrepository)@[e4a78c6665...](https://github.com/Akash0973/myrepository/commit/e4a78c66653d347f8185c3d84c286163d079b3eb)
#### Thursday 2023-03-09 18:20:50 by Akash0973

Create alternate pattern

Chan’s girlfriend's birthday is near, so he wants to surprise her by making a special cake for her. Chan knows that his girlfriend likes cherries on the cake, so he puts cherries on the top of the cake, but he was not satisfied. Therefore, he decided to replace some of the cherries to make a beautiful pattern. However, Chan has a lot of other work to do so he decided to ask for your help. The cherries are of two colors red and green. Now Chan wants the cherries to be placed in such a way that each cherry of one color must be adjacent to only cherries of the other color, two cherries are adjacent if they share a side. Now Chan has asked for your help in making that pattern on the cake.You can replace any cherry of given color with the other color. But there is a cost for each replacement: if you replace a red cherry with a green one, the cost is 5 units and if you replace a green cherry with a red one, the cost is 3 units. Help your friend Chan by making the cake special with minimum cost.If there is no need of any changes print '0'(ie. minimum cost is zero)
Input Size : N<=1000, M<=1000
Example:
INPUT
2 3
RRG
GGR
OUTPUT
8

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[9e981753ca...](https://github.com/lessthnthree/Skyrat-tg/commit/9e981753ca16ea6f527f1ce26ee5cbc044ad80c7)
#### Thursday 2023-03-09 18:34:08 by SkyratBot

[MIRROR] Reworked PDA menu & NtOS themes [MDB IGNORE] (#19390)

* Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID

https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov

![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.

https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Reworked PDA menu & NtOS themes

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [vesislavdimitrov/Car_Rental_System](https://github.com/vesislavdimitrov/Car_Rental_System)@[35ce10d89e...](https://github.com/vesislavdimitrov/Car_Rental_System/commit/35ce10d89ebc38b842f7e52f277f148acd8635a9)
#### Thursday 2023-03-09 19:17:04 by vesislavdimitrov

Oh Lord, you who are the refuge of the poor and needy,
we ask that you would save us
from the pestilence that stalks in the darkness
and the plague that destroys at midday.
Be our sun and shield.
Be our fortress.
Be our comfort this day.
May we not fear any evil
but rather trust in your might to save and your wisdom to guide,
so that we might rest  always in the shadow of the Almighty.
In the name of the One who heals our diseases. Amen.

---
## [slweeb/sandboxels](https://github.com/slweeb/sandboxels)@[420873c568...](https://github.com/slweeb/sandboxels/commit/420873c5689afb971f73e627ef238169a98cba35)
#### Thursday 2023-03-09 19:59:43 by Laetitia (O-01-67)

this was a goddamn nightmare to code

i hate my fucking life sometimes
i want to die
coding this sucked
school sucks
i'm drowning in work
i hate myself
if it wasn't for loona i would have locked the dog in the closet and cut my fucking wrists a long time ago
every day i think about killing myself
i swear to god those 12 girls are the only reason i even try anymore
i just want to fucking scream

/gen /srs

---
## [newstools/2023-daily-dispatch](https://github.com/newstools/2023-daily-dispatch)@[978e67d4b0...](https://github.com/newstools/2023-daily-dispatch/commit/978e67d4b061f01ccf598052aad2058e343da31a)
#### Thursday 2023-03-09 20:01:16 by Billy Einkamerer

Created Text For URL [www.dispatchlive.co.za/news/2023-03-09-boyfriend-arrested-in-connection-with-murder-of-15-year-old-girl/]

---
## [RimiNosha/Nosha-Industries-Server](https://github.com/RimiNosha/Nosha-Industries-Server)@[0c849cd2ee...](https://github.com/RimiNosha/Nosha-Industries-Server/commit/0c849cd2ee2406351ed47bb4ada08e3cf87d0526)
#### Thursday 2023-03-09 20:21:03 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms

![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)

</details>

## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:
# Conflicts:
#	code/__DEFINES/traits.dm
#	code/datums/components/sign_language.dm
#	code/modules/mob/living/carbon/carbon_say.dm
#	code/modules/mob/living/carbon/human/human_say.dm
#	code/modules/mob/living/carbon/human/species.dm
#	code/modules/mob/living/carbon/human/species_types/android.dm
#	code/modules/mob/living/carbon/human/species_types/golems.dm
#	code/modules/mob/living/carbon/human/species_types/mothmen.dm
#	code/modules/surgery/organs/external/wings/functional_wings.dm
#	code/modules/surgery/organs/tongue.dm

---
## [RimiNosha/Nosha-Industries-Server](https://github.com/RimiNosha/Nosha-Industries-Server)@[fe10e8537c...](https://github.com/RimiNosha/Nosha-Industries-Server/commit/fe10e8537c4c96a1047aafa5da6cc82b252417d1)
#### Thursday 2023-03-09 20:21:03 by Time-Green

External Organ Rework: new bodypart_overlay system (#72734)

Bodypart overlays are now drawn by the new /datum/bodypart_overlay
datum.

External organs no longer draw anything and instead add a special
/datum/bodypart_overlay/mutant to the bodypart, which draws everything

Makes it way easier to add custom overlays to limbs, since the whole
system is now modularized and external organs are just one
implementation of it

I haven't moved anything but external organs to this new system, I'll
move eyes, bodymarkings, hair, lipstick etc to this later

New pipeline is as follows:
- External organ added to limb
- External organ adds /datum/bodypart_overlay/mutant to limb to
bodypart_overlays
- Limb updates its icon, looks for all /datum/bodypart_overlay in
bodypart_overlays
- Very cool new overlay on your limb!

closes #71820

:cl:
refactor: External organs have been near-completely refactored.
admin: Admin-spawned external organs will load with a random icon and
color
fix: fixes angel wings not working for non-humans (it was so fucking
broken)
fix: fixes external organs being invisible if they werent initialized
with a human
/:cl:

### Why this is good for the game
External organs are cool but are pretty limited in some ways. Making
stuff like synthetic organs is kinda fucked. I tried and it was dogshit.
Now you can just give an icon state and icon and you're good (using
/datum/bodypart_accessory/simple)

Stuff like eyes, cat ears and hair seem like good choices for extorgans,
but don't quite work for it because their icons work a lot differently.
This solves for it completely since any organ (or object or whatever)
can add it's own icon to a bodypart.

Want to add an iron plate to someones head? Go ahead. Want a heart to
stick out of someones chest? No problem.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
# Conflicts:
#	code/datums/quirks/negative.dm
#	code/modules/mob/living/carbon/carbon_defines.dm
#	code/modules/surgery/bodyparts/_bodyparts.dm
#	code/modules/surgery/organs/external/_external_organs.dm
#	code/modules/surgery/organs/external/tails.dm
#	code/modules/surgery/organs/external/wings/functional_wings.dm
#	code/modules/surgery/organs/organ_internal.dm

---
## [PieVieRo/sokoban-raylib](https://github.com/PieVieRo/sokoban-raylib)@[f5602d297c...](https://github.com/PieVieRo/sokoban-raylib/commit/f5602d297c3f7d3829a15ff291a36a2aabb187a9)
#### Thursday 2023-03-09 20:48:29 by Tymoteusz Moryto

holy shit im so stupid

collisions now work tho :)

---
## [trmid/poolygotchi](https://github.com/trmid/poolygotchi)@[9e06d7821e...](https://github.com/trmid/poolygotchi/commit/9e06d7821e98fa3af3d4978b9cb3565265500a87)
#### Thursday 2023-03-09 21:14:39 by midpoint68

remove the GREAT BREAKER OF SAFARI
(fuck you, safari. you can't event implement regex correctly)

---
## [RimiNosha/Nosha-Industries-Server](https://github.com/RimiNosha/Nosha-Industries-Server)@[29a230718d...](https://github.com/RimiNosha/Nosha-Industries-Server/commit/29a230718dc23e9574e29376624d8330c96f5a49)
#### Thursday 2023-03-09 22:06:55 by necromanceranne

Bodypart code cleanup, robotic limbs can actually be disabled through damage again. (#71739)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Cleans up various variables and code comments in bodypart code so that
it is easier to understand (hopefully) what the fuck is happening there.

Fixes a hilarious oversight. For what may have been an entire 2 year
span, robotic limbs were unable to be disabled whatsoever. Good stuff.

## Why It's Good For The Game

Lost all your limbs and now have only surplus prosthetics?
Congratulations! You're now more durable than even someone with proper
robotic limbs, as your arms do not contribute anything more than 10
damage (or 15 stamina) to your overall damage taken. Furthermore, taking
the maximum amount of damage is actually entirely meaningless to you.

Laugh as someone attempting to shoot your arms does almost no meaningful
damage once you hit the cap! It's all sunk cost! You can't have it blown
off anyway, because dismembering surplus limbs is gone!

Who knew getting into a horrible bluespace/goliath accident could have
such an impact on your combat prowess. Thanks Nanotrasen!

Anyway, these vars are ugly.

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
code: Makes a lot of the bodypart variables clearer as to what they do.
Includes more detailed code comments.
fix: Robotic limbs are no longer immune to being disabled through
reaching maximum damage.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [mckaymichael/portfolio](https://github.com/mckaymichael/portfolio)@[148a0b5e81...](https://github.com/mckaymichael/portfolio/commit/148a0b5e814c43cb02911a0a9e1abf628f053694)
#### Thursday 2023-03-09 22:20:15 by Michael McKay

Added micro improvements

1. Features headings are ugly as fuck
2. Socials should change colour on hover too
3. Development projects on the feature section should open to a new tab

---
## [nik707/Citadel-Station-13-RP](https://github.com/nik707/Citadel-Station-13-RP)@[b9313e344b...](https://github.com/nik707/Citadel-Station-13-RP/commit/b9313e344b7b468f2e68d428e69c19503e3833b8)
#### Thursday 2023-03-09 22:31:56 by Keekenox

Fix Keek's Offset Sprites Finally (#5135)

Keekenox has fixed the pixel offsets for sprite assets, which is a
crucial improvement to the game. In the previous version, some sprites
appeared blurry and misaligned, making the game look unprofessional and
unpolished. With this commit, the sprites are correctly aligned,
improving the overall visual quality of the game. This is important
because it enhances the player experience and makes the game more
enjoyable.

Firstly, fixing the pixel offsets ensures that the sprites display
accurately across all devices and platforms. With the increasing
popularity of gaming on different devices, it is essential that the game
looks good and functions well across all of them. Inconsistent display
of assets can be frustrating for players and negatively impact their
experience. By addressing this issue, Keekenox has taken a step towards
creating a more accessible game, which can be played by a wider
audience.

Secondly, fixing the pixel offsets is important for the branding of the
game. The look and feel of the game are integral to creating a strong
brand image. The blurry and misaligned sprites make the game look less
polished and unprofessional. With the visual improvements from this
commit, the game now looks more visually appealing, and its brand image
is strengthened. This can lead to increased engagement, higher retention
rates, and better marketing opportunities.

Thirdly, by fixing the pixel offsets, Keekenox has made the game more
scalable. As the game grows and more assets are added, the risk of
misaligned and blurry sprites increases. By addressing this issue early
on, Keekenox has prevented potential headaches down the road, saving
time and resources in the long run. This demonstrates a commitment to
quality and attention to detail that players appreciate and respect.

Fourthly, fixing the pixel offsets is important for maintaining the
quality of the game. Players expect games to look and feel polished,
with attention given to even the smallest details. The misaligned and
blurry sprites detract from the overall quality of the game, leaving
players with a negative impression. By fixing this issue, Keekenox has
shown that they care about their players' experience and are committed
to delivering a high-quality game.

Lastly, fixing the pixel offsets has a direct impact on the player
experience. Games are meant to be enjoyable, and players want to immerse
themselves in a world that looks and feels great. Misaligned and blurry
sprites can be distracting and detract from the experience, making it
less enjoyable for the player. With the improvements made in this
commit, players can now enjoy the game without these distractions,
leading to increased satisfaction and potentially higher retention
rates.

In summary, fixing the pixel offsets for sprite assets is an important
improvement to the game. It ensures accurate display across all devices,
strengthens the brand image, improves scalability, maintains quality,
and enhances the player experience. Keekenox has demonstrated a
commitment to delivering a high-quality game, and players will
appreciate the attention to detail that went into this improvement.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[7bb3635c74...](https://github.com/Buildstarted/linksfordevs/commit/7bb3635c748ceaf1ada04986f75bcc52fa707ccc)
#### Thursday 2023-03-09 23:08:58 by Ben Dornis

Updating: 3/9/2023 11:00:00 PM

 1. Added: How platform integration in Qt/KDE apps works
    (https://nicolasfella.de/posts/how-platform-integration-works/)
 2. Added: Run a Phoenix 1.6 application on Scalingo using Releases
    (https://b310.de/blog/scalingo-phoenix-1-6.html)
 3. Added: How sales-led B2B SaaS can become more product led without freemium or a free trial
    (https://www.em-v.com/blog/how-sales-led-b2b-saas-can-be-product-led-without-freemium)
 4. Added: Smart lazyness ~ Andrea Canton
    (https://andreacanton.dev/posts/d005-smart-lazyness/)
 5. Added: The Kids are Not Okay
    (https://thezvi.wordpress.com/2023/03/08/the-kids-are-not-okay/)
 6. Added: Which is worse when working on production databases?  Being drunk or tired?
    (http://ledgersmbdev.blogspot.com/2023/03/which-is-worse-when-working-on.html)
 7. Added: Can we replace Twitter?
    (https://thomas.wang/writing/can-we-replace-twitter)
 8. Added: Building a physician reference for 2023
    (https://blog.tjcx.me/p/building-a-physician-reference-for)
 9. Added: The historical evolution of Cross-Site Request Forgery
    (https://www.rajatswarup.com/blog/2023/03/08/the-historical-evolution-of-cross-site-request-forgery/)
10. Added: Visual Studio 2022 – 17.5 Performance Enhancements - Visual Studio Blog
    (https://devblogs.microsoft.com/visualstudio/visual-studio-2022-17-5-performance-enhancements/)
11. Added: What is Synthetic Data? The Good, the Bad, and the Ugly
    (https://www.benthamsgaze.org/2023/03/01/what-is-synthetic-data-the-good-the-bad-and-the-ugly/)
12. Added: Founder of Kilo shows how he built a profitable business entirely using nocode - Grid7
    (https://grid7.com/2023/03/profitable-business-nocode-tech-stack/)
13. Added: What's new with ASP.NET Core 7
    (https://youtube.com/watch?v=tWXscwXNbBQ)
14. Added: Made £34.84 From a Start-up I Shutdown In 2021 - Phillip Hughes
    (https://www.philliphughes.co.uk/tips-and-tricks/made-money-from-a-start-up-i-shutdown-in-2021/)
15. Added: PrivEsc: Abusing the Service Control Manager for Stealthy & Persistent LPE
    (https://0xv1n.github.io/posts/scmanager/)
16. Added: My Backup Strategy
    (https://jorisroovers.com/posts/my-backup-strategy)
17. Added: On Unsavoury Memeplexes
    (https://muskdeer.blogspot.com/2023/03/on-unsavoury-memeplexes.html)
18. Added: Anthony Giretti (anthonygirettimastodon.social)
    (https://mastodon.social/@anthonygiretti)
19. Added: In praise of Alpine and apk
    (https://whynothugo.nl/journal/2023/02/18/in-praise-of-alpine-and-apk/#the-testing-repository?utm_source=hnblogs.substack.com)
20. Added: Translate Tokens with Identity Server (Using Forms Authentication Ticket tokens on Open Id Connect) - Doumer's Blog
    (https://doumer.me/translate-tokens-with-identity-server-using-forms-authentication-ticket-tokens-on-open-id-connect/)

Generation took: 00:08:46.5517193

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[5f9f60713b...](https://github.com/lessthnthree/Skyrat-tg/commit/5f9f60713b7f79f548eb9d02baeec793c1e50243)
#### Thursday 2023-03-09 23:43:59 by SkyratBot

[MIRROR] Starlight Polish (Space is blue!) [MDB IGNORE] (#19059)

* Starlight Polish (Space is blue!) (#72886)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds support to underlays to realize_overlays
Ensures decals properly handle plane offsets
Fixes space lighting double applying if it's changeturf'd into. this
will be important later
Makes solar vis_contents block emissives as expected
Moves transit tube overlays to update_overlays, adds emissive blockers
to them

#### Adds render steps

An expansion on render_target based emissive blockers. 
They allow us to hijack an object's appearance and draw it somewhere
else, or even modify it, THEN draw it somewhere else.
They chain quite nicely

Fixes shuttles deleting z holder objects

#### Makes space emissive, makes walls and floors block emissives
The core idea here goes like this:
We make space glow, and give its overlays some color

This way, the tile and space parallax remain fullbright, along with
anything that doesn't block emissives, but anything that does block
emissives will instead get shaded the color of starlight

This requires a bit of extra work, see later

This is done automatically with render relays, which now support
specifiying layer and color (Need to make an editor for these one of
these days)

The emissive blocking floor stuff requires making a second render plate
to prevent double scaling

Also adds some new layering defines for lighting, and ensures all turf
lights have a layer. We'll get to this soon

#### Makes things in space blue

We color them the same as starlight, by taking advantage of space being
emissive
This means that things in space that block emissive will block it
correctly and be colored blue by the light overlay, but space itself
will remain fullbright

This does require redefining what always_lit means, but nothing but
cordons use that so it's fineee


#### Makes glass above space glow, and some other stuff

Glass tiles that sit above space will now shine light with matching
color to the glasses color. This includes mat tiles.

Glass tiles (not mat because they have no alpha) also only partially
block emissives.
Adds a new proc that uses render steps to acomplish this, essentially
we're cutting out bits below X alpha and drawing what remains as an
emissive.

#### Modifies partial space showing to support glow

Essentially, alongside displaying space as an underlay, we also display
a light overlay colored like starlight.
That starlight overlay gets masked to only be visible in bits that do
not contain any alpha.

We also mask the turf lighting to not go into bits that have no alpha,
to ensure we get the effect we want.
This is done with that lighting layer thing I mentioned earlier.

#### Makes appearance realization's list output ordered

I want it output in order of overlay, sub overlay suboverlay, next
overlay
Need to use insert for that

## Why It's Good For The Game

Pretty!
Also having space be emissive is a very very good way to test for fucked
emissive blockers (If it's broken why are we even drawing the overlay)
I know for a fact mob blockers on lizards and socks are kinda yorked, I
think there's more

<details>
<summary>
Old
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916157-d4b38aa7-3ab6-42a4-989f-7bfba2dc2cba.png)

![image](https://user-images.githubusercontent.com/58055496/213916077-637fa288-bbee-477d-aded-730d9683477e.png)

![image](https://user-images.githubusercontent.com/58055496/213916088-0657a8a2-5627-48e2-8c4b-870c90ef2072.png)

</details>


<details>
<summary>
New
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916107-2af74e64-1817-4a44-b528-180a9160cb9e.png)

![image](https://user-images.githubusercontent.com/58055496/213916115-5fa36fcc-b988-4ccf-850e-21c26ed463d0.png)

![image](https://user-images.githubusercontent.com/58055496/213916120-6833187d-b12e-42a7-ac4b-63c56deb71e5.png)

</details>

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Space now makes things in it starlight faintly blue
fix: Glass floors that display space now properly let space shine
through them, rather then hiding it in the dark
add: Glass floors above space now glow faintly depending on their glass
type
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* update modular

* Update _decal.dm

* Update _decal.dm

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [siph/blog](https://github.com/siph/blog)@[4fa38a7e53...](https://github.com/siph/blog/commit/4fa38a7e53c72a91c0e0780115e5a17b91053388)
#### Thursday 2023-03-09 23:56:07 by siph

native ruby

ruby sucks moldy dog dicks apparently and is a massive pain in the ass
to get dependencies (Gems, gotta have stupid puns) working properly with
the nix store so fuck it.

---

