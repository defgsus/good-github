## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-16](docs/good-messages/2022/2022-06-16.md)


1,734,777 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,734,777 were push events containing 2,738,702 commit messages that amount to 194,455,648 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9428d97a4f...](https://github.com/tgstation/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Thursday 2022-06-16 00:02:37 by Imaginos16

[MDB IGNORE] The Tilening V2 - Damaged Tile Overlays Edition (#67761)


About The Pull Request

Hello once more! As we near summer, I continued to reminisce on several PRs done throughout last year! One of them was the controversial, but rather positive Tilening V1, as done by me and Twaticus a while back (#58932), and felt I could've done a better job with how it was presented.

And thus, thanks to @Fikou encouraging me with a very interesting find of a previous tile resprite attempt, I've successfully done it!

Ladies and Gentlemen, I present to you all, Tilening Version Two!
image

Now this isn't your run of the mill tile resprite. While I did improve the appearance of several tiles I haven't touched last time (including the showroom/freezer tiles now), I decided to do something special that most mappers shall appreciate!

Don't you hate it when of all damaged states, there's only ones for grey tiles when we have white, black, terracotta and a bunch of other materials? Don't you wish they were overlays instead?

Well golly gee do I have good news for you!
image
image

After painstakingly spending at least several hours trying to learn enough code to pull it off, I have successfully made it so most tiles display transparent versions of damage overlays over them! This means mappers can express their creativity that much better! And thanks to how the code is written, its super easy to snowflake certain tile types to make them use unique damaged states (looking at you wooden tiles), so fret not in that aspect.

Credits to:
@WJohn For actually making those damaged overlays! Wouldn't've done the PR if it wasn't for you.
@dragomagol, @RigglePrime and @LemonInTheDark for helping me out in a VC at 10 PM to 12 AM troubleshooting the code to make this improvement work!
Why It's Good For The Game

The shading is done better as compared to last time, making them feel more cubical and less like a pancake when seen from above! This PR also makes it so that we never ever have to touch damaged tiles ever again potentially, saving up some RSC regarding icons.

However, due to how damaged tiles are currently mapped in, rather than overlayed as I envision in the future, it'll require a PR by San to be merged later that should make it safe to remove these icons.
Changelog

cl PositiveEntropy, WJohnston, Dragomagol, LemonInTheDark, Riggle
imageadd: Resprites most variety of tiles into a better shaded version!
code: Damaged floors are now damaged overlays, meaning that most tiles should properly display a damaged state!
/cl

---
## [Aevann1/rDrama](https://github.com/Aevann1/rDrama)@[6c15633240...](https://github.com/Aevann1/rDrama/commit/6c156332406c10e6786105fc28d2b20fdf933c9e)
#### Thursday 2022-06-16 00:31:20 by Aevann1

Revert "fuck you, use a real browser"

This reverts commit b992c1e2cd3e5aeb07b25d4ebf3695387c16ab2c.

---
## [Addust/tgstation](https://github.com/Addust/tgstation)@[a3c8013b45...](https://github.com/Addust/tgstation/commit/a3c8013b45c92fdb8efec7ba827d7b00191e2d55)
#### Thursday 2022-06-16 01:00:39 by GoldenAlpharex

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

---
## [Lionh34rt/qb-core](https://github.com/Lionh34rt/qb-core)@[9d83a952c2...](https://github.com/Lionh34rt/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Thursday 2022-06-16 01:00:45 by uShifty

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
## [momentum-mod/website](https://github.com/momentum-mod/website)@[b6af3ec14b...](https://github.com/momentum-mod/website/commit/b6af3ec14bb62b45582a0340c965203d128dc546)
#### Thursday 2022-06-16 01:15:42 by tsa96

feat: Port old tests

God, these things are fucking gross. We'll want to write a LOT more. Ran jest-codemods on everything, not great but best we're gonna get I reckon.

---
## [CrudeWax/space-station-14](https://github.com/CrudeWax/space-station-14)@[949fbd0194...](https://github.com/CrudeWax/space-station-14/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Thursday 2022-06-16 02:39:58 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Thursday 2022-06-16 03:17:55 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [facebook/react-native](https://github.com/facebook/react-native)@[47280de85e...](https://github.com/facebook/react-native/commit/47280de85e62f33f0b97bc1ed7c83bc6ca0dc7d4)
#### Thursday 2022-06-16 06:40:45 by Joshua Gross

New Props parsing infrastructure for perf improvements: visitor pattern vs random-map-access pattern (ViewProps, minus YogaLayoutableShadowNode)

Summary:
Perf numbers for this stack are given in terms of before-stack and after-stack, but the changes are split up for ease of review, and also to show that this migration CAN happen per-component and is 100% opt-in. Most existing C++ components do not /need/ to change at all.

# Problem Statement

During certain renders (select critical scenarios in specific products), UIManagerBinding::createNode time takes over 50% of JS thread CPU time. This could be higher or lower depending on the specific product and interaction, but overall createNode takes a lot of CPU time. The question is: can we improve this? What is the minimal overhead needed?

The vast, vast majority of time is taken up by prop parsing (specifically, converting JS values across the JSI into concrete values on the C++ props structs). Other methods like appendChild, etc, do not take up a significant amount of time; so we conclude that createNode is special, and the JSI itself, or calling into C++, is not the problem. Props parsing is the perf problem.

Can we improve it? (Spoiler: yes)

# How does props parsing work today?

Today, props parsing works as follows:

1. The ConcreteComponentDescriptor will construct a RawPropsParser (one per component /type/, per application: so one for View, one for Image, one for Text... etc)
2. Once per component type per application, ConcreteComponentDescriptor will call "prepare" on the RawPropsParser with an empty, default-constructed ConcreteProps struct. This ConcreteProps struct will cause RawProps.at(field) for every single field.
3. Based on the RawProps::at calls in part 2, RawPropsParser constructs a Map from props string names (width, height, position, etc) to a position within a "value index" array.
4. The above is what happens before any actual props are parsed; and the RawPropsParser is now ready to parse actual Props.
5. When props are actually being parsed from a JSI dictionary, we now have two phases:
  1. The RawPropsParser `preparse`s the RawProps, by iterating over the JSI map and filling in two additional data structures: a linear list of RawValues, and a mapping from the ValueIndex array (`keyIndexToValueIndex_`; see step 3) to a value's position in the values list (`value_` in RawPropsParser/RawProps);
  2. The ConcretePropT constructor is called, which is the same as in step 2/3, which calls `fieldValue = rawProps.at("fieldName")` repeatedly.
  3. For each `at` call, the RawProps will look up a prop name in the Map constructed in step 3, and either return an empty value, or map the key name to the `keyIndexToValueIndex_` array, which maps to a value in `values_`, which is then returned and further parsed.

So, a few things that become clear with the current architecture:

1. Complexity is a property of the number of /possible/ props that /can/ be parsed, not what is actually used in product code. This violates the "only pay for what you use" principal. If you have `<View opacity={0.5} />`, the ViewProps constructor will request ~170 properties, not 1!
2. There's a lot of pre-parsing which isn't free
3. The levels of indirection aren't free, and make cache misses more likely and pipelining is more challenging
4. The levels of indirection also require more memory - minor, but not free

# How can we improve it?

The goal is to improve props parsing with minimal or zero impact on backwards-compability. We should be able to migrate over components when it's clear there's a performance issue, without requiring everything gets migrated over at once. This both (1) helps us prove out the new architecture, (2) derisks the project, (3) gives us time, internally and externally, to perfect the APIs and gradually migrate everything over before deleting the old infrastructure code entirely.

Thus, the goal is to do something that introduces a zero-cost abstraction. This isn't entirely possible in practice, and in fact this method slightly regresses components that do not use the new architecture /at all/, while dramatically improving migrated components and causing the impact of the /old/ architecture to be minimal.

# Solution

1. We still keep the existing system in place entirely.
2. After Props are constructed (see ConcreteComponentDescriptor changes) we iterate over all the /values/ set from JS, and call PropsT::setProp. Incidentally, this allows us to easily reuse the same prop for multiple values for "free", which was expensive in the old system.
3. It's worth noting that this makes a Props struct "less immutable" than it was before, and essentially now we have a "builder pattern" for Props. (If we really wanted to, we could still require a single constructor for Props, and then actually use an intermediate PropsBuilder to accumulate values - but I don't think this overhead would be worth for the conceptual "immutability" win, and instead a "Construct/Set/Seal" model works fine, and we still have all the same guarantees of immutability after the parsing phase)

# Implementation Details
# How to properly construct a single Prop value

Minor detail: parsing a single prop is a 3-step process. We imagine two scenarios: (1) Creating a new ShadowNode/Props A from nothing/void, so the previous Props value is just the default constructor. (2) Cloning a ShadowNode A->B and therefore Props A must be copied to Props B before parsing.

We will denote this as a clone from A->B, where A may or may not be a previous node or a default-constructed Props node; and imagine in particular that we're setting the "opacity" value for PropsB.

We must first (1) copy a value over from the previous version of the Props struct, so B.opacity = A.opacity; (2) Determine if opacity has been set from JS. If so, and there is a value, B.opacity = parse(JSValue). (3) If JS has passed in a value for the prop, BUT the value is `null`, it means that JS is resetting or deleting the prop, so we must set it BACK to the default. In this case we set PropsB.opacity = DefaultConstructedProps.opacity.

We must take care in general to ensure that the correct behavior is achieved here, which should help to explain some of the code below.

## String comparisons vs hash comparisons

In the previous system, a RawPropsKey is three `const char*` strings, concatenated together repeatedly /at runtime/. In practice, the ONLY reason we have the prefix, name, suffix Key structure is for the templated prop parsing in ViewProps and YogaStyableProps - that's it. It's not used anywhere else. Further, the key {"margin", "Left", "Width"} is identical to the key {"marginLeftWidth", null, null} and we don't do anything fancy with matching prefixes before comparing the whole string, or similar. Before comparison, keys are concatenated into a single string and then we use `strcmp`. The performance of this isn't terrible, but it's nonzero overhead.

I think we can do better and it's sufficient to compare hashed string values; even better, we can construct most of these /at compile time/ using constexpr, and using `switch` statements guarantee no hash collisions within a single Props struct (it's possible there's a collision between Props.cpp and ViewProps.cpp, for example, since they're different switch statements). We may eventually want to be more robust against has collisions; I personally don't find the risk to be too great, hash collisions with these keys are exceedingly unlikely (or maybe I just like to live dangerously). Thus, at runtime, each setProp requires computing a single hash for the value coming from JS, and then int comparisons with a bunch of pre-compiled values.

If we want to be really paranoid, we could be robust to hash collisions by doing `switch COMPILED_HASH("opacity"): if (strcmp(strFromJs, "opacity") == 0)`. I'm happy to do this if there's enough concern.

## Macros

Yuck! I'm using lots of C preprocessor macros. In general I found this way, way easier in reducing code and (essentially) doing codegen for me vs templated code for the switch cases and hashing prop names at compile-time. Maybe there's a better way.

Changelog: [Added][Fabric] New API for efficient props construction

Reviewed By: javache

Differential Revision: D37050215

fbshipit-source-id: d2dcd351a93b9715cfeb5197eb0d6f9194ec6eb9

---
## [jimc/linux](https://github.com/jimc/linux)@[9f116135a2...](https://github.com/jimc/linux/commit/9f116135a2c6c6acd54deb888a60681df9fbd807)
#### Thursday 2022-06-16 08:20:32 by Jim Cromie

dyndbg: add drm.debug style bitmap support WIP

Add kernel_param_ops and callbacks to implement a bitmap in a
sysfs-node, which controls classes.  This supports uses like:

  echo 0x3 > /sys/module/drm/parameters/debug

IE add these:

 - int param_set_dyndbg_classes()
 - int param_get_dyndbg_classes()
 - struct kernel_param_ops param_ops_dyndbg_classes

Following the model of kernel/params.c STANDARD_PARAM_DEFS, these are
non-static and exported.  This might be unnecessary here.

get/set use an augmented kernel_param; the arg refs a new struct
ddebug_classes_bitmap_param, initialized by the DYNAMIC_DEBUG_CLASSES
macro (see commit HEAD~6), which contains:

BITS: a pointer to the user module's ulong holding the bits/state.  By
ref'g the client's bit-state _var, we coordinate with existing code
(such as drm_debug_enabled) which uses the _var, so it works
unchanged, even as the foundation is switched out underneath it..
Using a ulong allows use of BIT() etc.

FLAGS: dyndbg.flags toggled by bit-changes. Usually just "p".

MAP: a pointer to struct ddebug_classes_map, which maps those
class-names to pr_debug.class_ids 0..N.  This class-map is
defined/declared/initialized by DYNAMIC_DEBUG_CLASSES() etc.

map-type: enum _DISJOINT, _LEVELS

RFC:

Above was written before DISJOINT and LEVELS was distinguished, and
describes former, but this patch has both.  Testing shows DISJOINT is
solid, _LEVELs is not; the interface has some ambiguities.

To map LEVELS onto DISJOINT, levels are mapped to consecutive DISJOINT
bits, and the x>y relation is enforced on the bit position.
All well and good, until -1 is needed to clear bit 0.

This also has the undesirable property that read val doesnt match just
written val:

   echo 0 > verbosity
   cat verbosity
   0x1

a few ways out ?

1 :#> echo -1 > $sysknob
  signed int input carries additional expressive capacity
  this preserves 2**N bitmapping
  but bit-0 is weird (for LEVELS only, not DISJOINT)

2 subtract 1 from input, treat as bitpos (like now)
  :#> echo 0 > levelX	# turn OFF bit 0
  :#> echo 1 > levelX	# turn ON bit  0
  :#> echo 2 > levelX	# turn ON bits 1-0
  :#> echo 3 > levelX	# turn ON bits 2-0

3 drop "V0", "L0"
  v=0 is just printk, no point in using this in prdbgs, so theres nothing to control.
  this kinda puts V1 on bit-0

4 use symbolic classnames
  :#> echo +INFO,-TRACE > nv_debug
  :#> echo -V1 > verbosity

5 base=1 on _LEVELS class
  this might combine with others, or further confuse things.

ATM impl is 1, without the -1 input.  The chief trouble here is that
the readback value after writing 0 is 0x1, which violates the
principle of least-surprise.  Fixing that in param-get feels hacky.

Theres also some ambiguity potentially added in the symbol to bit
mapping; the names in a _LEVELS classmap can muddle things (2,3 break
this istm).

  :#> echo 0 > verbosity
  :#> echo V0 > verbosity  # should mean the same thing

This constraint basically means that; V0 must be allocated (just a
bit), mapped (so its legal input), and unused (because its just a
complicated printk).  MAYBE.

More map-types could tailor behavior, and input forms accepted:

DD_CLASS_DISJOINT_HEX: accept only hex bitmaps

DD_CLASS_DISJOINT_SYMNAMES: accept only symbolic class-names

DD_CLASS_VERBOSE_NUMBER: accept only decimal verbosity numbers

DD_CLASS_VERBOSE_SYMNAMES: accept only symbolic class-names

maybe
should exclude V0, or

also breaks 1

Signed-off-by: Jim Cromie <jim.cromie@gmail.com>

---
## [ZacWalk/binutils-gdb](https://github.com/ZacWalk/binutils-gdb)@[86d77f6a5b...](https://github.com/ZacWalk/binutils-gdb/commit/86d77f6a5be904f13c633f10bdf77ff3dd69db94)
#### Thursday 2022-06-16 08:47:57 by Andrew Burgess

gdb: don't try to use readline before it's initialized

While working on a different patch, I triggered an assertion from the
initialize_current_architecture code, specifically from one of
the *_gdbarch_init functions in a *-tdep.c file.  This exposes a
couple of issues with GDB.

This is easy enough to reproduce by adding 'gdb_assert (false)' into a
suitable function.  For example, I added a line into i386_gdbarch_init
and can see the following issue.

I start GDB and immediately hit the assert, the output is as you'd
expect, except for the very last line:

  $ ./gdb/gdb --data-directory ./gdb/data-directory/
  ../../src.dev-1/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.
  ----- Backtrace -----
  ... snip ...
  ---------------------
  ../../src.dev-1/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.
  Quit this debugging session? (y or n) ../../src.dev-1/gdb/ser-event.c:212:16: runtime error: member access within null pointer of type 'struct serial'

Something goes wrong when we try to query the user.  Note, I
configured GDB with --enable-ubsan, I suspect that without this the
above "error" would actually just be a crash.

The backtrace from ser-event.c:212 looks like this:

  (gdb) bt 10
  #0  serial_event_clear (event=0x675c020) at ../../src/gdb/ser-event.c:212
  #1  0x0000000000769456 in invoke_async_signal_handlers () at ../../src/gdb/async-event.c:211
  #2  0x000000000295049b in gdb_do_one_event () at ../../src/gdbsupport/event-loop.cc:194
  #3  0x0000000001f015f8 in gdb_readline_wrapper (
      prompt=0x67135c0 "../../src/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.\nA problem internal to GDB has been detected,\nfurther debugging may prove unreliable.\nQuit this debugg"...)
      at ../../src/gdb/top.c:1141
  #4  0x0000000002118b64 in defaulted_query(const char *, char, typedef __va_list_tag __va_list_tag *) (
      ctlstr=0x2e4eb68 "%s\nQuit this debugging session? ", defchar=0 '\000', args=0x7fffffffa6e0)
      at ../../src/gdb/utils.c:934
  #5  0x0000000002118f72 in query (ctlstr=0x2e4eb68 "%s\nQuit this debugging session? ")
      at ../../src/gdb/utils.c:1026
  #6  0x00000000021170f6 in internal_vproblem(internal_problem *, const char *, int, const char *, typedef __va_list_tag __va_list_tag *) (problem=0x6107bc0 <internal_error_problem>, file=0x2b976c8 "../../src/gdb/i386-tdep.c",
      line=8455, fmt=0x2b96d7f "%s: Assertion `%s' failed.", ap=0x7fffffffa8e8) at ../../src/gdb/utils.c:417
  #7  0x00000000021175a0 in internal_verror (file=0x2b976c8 "../../src/gdb/i386-tdep.c", line=8455,
      fmt=0x2b96d7f "%s: Assertion `%s' failed.", ap=0x7fffffffa8e8) at ../../src/gdb/utils.c:485
  #8  0x00000000029503b3 in internal_error (file=0x2b976c8 "../../src/gdb/i386-tdep.c", line=8455,
      fmt=0x2b96d7f "%s: Assertion `%s' failed.") at ../../src/gdbsupport/errors.cc:55
  #9  0x000000000122d5b6 in i386_gdbarch_init (info=..., arches=0x0) at ../../src/gdb/i386-tdep.c:8455
  (More stack frames follow...)

It turns out that the problem is that the async event handler
mechanism has been invoked, but this has not yet been initialized.

If we look at gdb_init (in gdb/top.c) we can indeed see the call to
gdb_init_signals is after the call to initialize_current_architecture.

If I reorder the calls, moving gdb_init_signals earlier, then the
initial error is resolved, however, things are still broken.  I now
see the same "Quit this debugging session? (y or n)" prompt, but when
I provide an answer and press return GDB immediately crashes.

So what's going on now?  The next problem is that the call_readline
field within the current_ui structure is not initialized, and this
callback is invoked to process the reply I entered.

The problem is that call_readline is setup as a result of calling
set_top_level_interpreter, which is called from captured_main_1.
Unfortunately, set_top_level_interpreter is called after gdb_init is
called.

I wondered how to solve this problem for a while, however, I don't
know if there's an easy "just reorder some lines" solution here.
Looking through captured_main_1 there seems to be a bunch of
dependencies between printing various things, parsing config files,
and setting up the interpreter.  I'm sure there is a solution hiding
in there somewhere.... I'm just not sure I want to spend any longer
looking for it.

So.

I propose a simpler solution, more of a hack/work-around.  In utils.c
we already have a function filtered_printing_initialized, this is
checked in a few places within internal_vproblem.  In some of these
cases the call gates whether or not GDB will query the user.

My proposal is to add a new readline_initialized function, which
checks if the current_ui has had readline initialized yet.  If this is
not the case then we should not attempt to query the user.

After this change GDB prints the error message, the backtrace, and
then aborts (including dumping core).  This actually seems pretty sane
as, if GDB has not yet made it through the initialization then it
doesn't make much sense to allow the user to say "no, I don't want to
quit the debug session" (I think).

---
## [J-N-Slocombe/git](https://github.com/J-N-Slocombe/git)@[3d2f96a930...](https://github.com/J-N-Slocombe/git/commit/3d2f96a930d8ba68326260289a3d5511560281ce)
#### Thursday 2022-06-16 09:24:08 by brian m. carlson

builtin/stash: provide a way to export stashes to a ref

A common user problem is how to sync in-progress work to another
machine.  Users currently must use some sort of transfer of the working
tree, which poses security risks and also necessarily causes the index
to become dirty.  The experience is suboptimal and frustrating for
users.

A reasonable idea is to use the stash for this purpose, but the stash is
stored in the reflog, not in a ref, and as such it cannot be pushed or
pulled.  This also means that it cannot be saved into a bundle or
preserved elsewhere, which is a problem when using throwaway development
environments.

Let's solve this problem by allowing the user to export the stash to a
ref (or, to just write it into the repository and print the hash, à la
git commit-tree).  Introduce git stash export, which writes a chain of
commits where the first parent is always a chain to the previous stash,
or to a single, empty commit (for the final item) and the second is the
stash commit normally written to the reflog.

Iterate over each stash from topmost to bottomost, looking up the data
for each one, and then create the chain from the single empty commit
back up in reverse order.  Generate a predictable empty commit so our
behavior is reproducible.  Create a useful commit message, preserving
the author and committer information, to help users identify stash
commits when viewing them as normal commits.

If the user has specified specific stashes they'd like to export
instead, use those instead of iterating over all of the stashes.

As part of this, specifically request quiet behavior when looking up the
OID for a revision because we will eventually hit a revision that
doesn't exist and we don't want to die when that occurs.

Signed-off-by: brian m. carlson <sandals@crustytoothpaste.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [onderkalaci/postgres](https://github.com/onderkalaci/postgres)@[c40ba5f318...](https://github.com/onderkalaci/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Thursday 2022-06-16 09:41:45 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [aggregat4/dendriform](https://github.com/aggregat4/dendriform)@[515a4249fb...](https://github.com/aggregat4/dendriform/commit/515a4249fb389d53bfac4785ee7f8ecb38e3db0c)
#### Thursday 2022-06-16 09:56:50 by Boris Terzic

Fixes a bug where we were not explicitly returning a value from a function and it was evaluating as undefined (fuck you javascript)

---
## [loongson/valgrind-loongarch64](https://github.com/loongson/valgrind-loongarch64)@[6cc2d94d93...](https://github.com/loongson/valgrind-loongarch64/commit/6cc2d94d93fa5350355b8cedb0d6b5309fcc588c)
#### Thursday 2022-06-16 10:57:16 by Paul Floyd

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
## [jeannie2/font-library](https://github.com/jeannie2/font-library)@[954170ee0b...](https://github.com/jeannie2/font-library/commit/954170ee0b32949d41c327585954f2317beaa9a9)
#### Thursday 2022-06-16 11:36:26 by jeannie2

Update families.json

Added tags for 17 fonts without any tags: Inspiration, Inter, Jua, Lexend, Legend Deca, Legend Giga, Legend Exa, Potta One, Praise, Nanum Gothic Coding, Oooh Baby, Puppies Play, Rock 3D, Single Day, Shizuru, Style Script, Send Flowers 

Removed tag "caps" for Sedgewick Ave (only applies to Sedgwick Ave Display) -> sorry I didn't tag correctly

---
## [LongSleeves/sojourn-station](https://github.com/LongSleeves/sojourn-station)@[796aeaa98f...](https://github.com/LongSleeves/sojourn-station/commit/796aeaa98f76c2a6ef7a94e540d3b8f7efcb027b)
#### Thursday 2022-06-16 12:01:56 by lolman360

fixes stacks deleting randomly (#3357)

* whoo

* god i fucking hate stackcode

thank you kevinz

---
## [ULTRA-HOI/HOI4-ULTRA-Project](https://github.com/ULTRA-HOI/HOI4-ULTRA-Project)@[fac4d1de28...](https://github.com/ULTRA-HOI/HOI4-ULTRA-Project/commit/fac4d1de288bb3515a029c8e62d9b51affb9295c)
#### Thursday 2022-06-16 13:08:20 by Jakub Mozgawa

Localisation fixes. Fuck you paradox and your logs, this is ridiculous. Fix your hashing

---
## [ritukanta/android_kernel_realme_RMX1821](https://github.com/ritukanta/android_kernel_realme_RMX1821)@[efad1d46be...](https://github.com/ritukanta/android_kernel_realme_RMX1821/commit/efad1d46be66f03503e7ded728b59e7b77dbfc8b)
#### Thursday 2022-06-16 14:04:57 by aviraxp

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
Signed-off-by: NaissAA <nasifahmed150@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[efd18f213b...](https://github.com/treckstar/yolo-octo-hipster/commit/efd18f213b790180cad4d25968a1ef04f6367995)
#### Thursday 2022-06-16 15:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[763a10d1cc...](https://github.com/tgstation/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Thursday 2022-06-16 15:22:28 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[2cd6f3fbd8...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/2cd6f3fbd82109567a03900f98ca79de178258bf)
#### Thursday 2022-06-16 16:35:43 by George Spelvin

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
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[eeb6a2aae8...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/eeb6a2aae8cec09eba1122208a4366f41b09d921)
#### Thursday 2022-06-16 16:35:43 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [00ze-cyclone/Yogstation](https://github.com/00ze-cyclone/Yogstation)@[a819d9af09...](https://github.com/00ze-cyclone/Yogstation/commit/a819d9af093b2147b2d9601897c46cad08d1a30f)
#### Thursday 2022-06-16 17:45:16 by 00ze-cyclone

remove one space

I think it might fix everything, if it does then holy shit I want HC

---
## [YakumoChen/Skyrat-tg](https://github.com/YakumoChen/Skyrat-tg)@[a3c0819e80...](https://github.com/YakumoChen/Skyrat-tg/commit/a3c0819e8091ab99a5ab8f53b59c4687e5b2f2cf)
#### Thursday 2022-06-16 17:54:19 by SkyratBot

[MIRROR] Removes (in) smoke and foam reactions [MDB IGNORE] (#13963)

* Removes (in) smoke and foam reactions (#67270)

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

* Removes (in) smoke and foam reactions

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[13a65d3682...](https://github.com/cockroachdb/cockroach/commit/13a65d3682863dc94b5057801edae7ed8f7d7d18)
#### Thursday 2022-06-16 17:58:15 by Andrei Matei

util/tracing: fix crash in StreamClientInterceptor

Before this patch, our client-side tracing interceptor for streaming rpc
calls was exposed to gRPC bugs being currently fixed in
github.com/grpc/grpc-go/pull/5323. This had to do with calls to
clientStream.Context() panicking with an NPE under certain races with
RPCs failing. We've recently gotten two crashes seemingly because of
this. It's unclear why this hasn't shown up before, as nothing seems new
(either on our side or on the grpc side). In 22.2 we do use more
streaming RPCs than before (for example for span configs), so maybe that
does it.

This patch eliminates the problem by eliminating the
problematic call into ClientStream.Context(). The background is that
our interceptors needs to watch for ctx cancelation and consider the RPC
done at that point. But, there was no reason for that call; we can more
simply use the RPC caller's ctx for the purposes of figuring out if the
caller cancels the RPC. In fact, calling ClientStream.Context() is bad
for other reasons, beyond exposing us to the bug:
1) ClientStream.Context() pins the RPC attempt to a lower-level
connection, and inhibits gRPC's ability to sometimes transparently
retry failed calls. In fact, there's a comment on ClientStream.Context()
that tells you not to call it before using the stream through other
methods like Recv(), which imply that the RPC is already "pinned" and
transparent retries are no longer possible anyway. We were breaking
this.
2) One of the grpc-go maintainers suggested that, due to the bugs
reference above, this call could actually sometimes give us "the
wrong context", although how wrong exactly is not clear to me (i.e.
could we have gotten a ctx that doesn't inherit from the caller's ctx?
Or a ctx that's canceled independently from the caller?)

This patch also removes a paranoid catch-all finalizer in the
interceptor that assured that the RPC client span is always eventually
closed (at a random GC time), regardless of what the caller does - i.e.
even if the caller forgets about interacting with the response stream or
canceling the ctx.  This kind of paranoia is not needed. The code in
question was copied from grpc-opentracing[1], which quoted a
StackOverflow answer[2] about whether or not a client is allowed to
simply walk away from a streaming call. As a result of conversations
triggered by this patch [3], that SO answer was updated to reflect the fact
that it is not, in fact, OK for a client to do so, as it will leak gRPC
resources. The client's contract is specified in [4] (although arguably
that place is not the easiest to find by a casual gRPC user). In any
case, this patch gets rid of the finalizer. This could in theory result
in leaked spans if our own code is buggy in the way that the paranoia
prevented, but all our TestServers check that spans don't leak like that
so we are pretty protected. FWIW, a newer re-implementation of the
OpenTracing interceptor[4] doesn't have the finalizer (although it also
doesn't listen for ctx cancellation, so I think it's buggy), and neither
does the equivalent OpenTelemetry interceptor[6].

Fixes #80689

[1] https://github.com/grpc-ecosystem/grpc-opentracing/blob/8e809c8a86450a29b90dcc9efbf062d0fe6d9746/go/otgrpc/client.go#L174
[2] https://stackoverflow.com/questions/42915337/are-you-required-to-call-recv-until-you-get-io-eof-when-interacting-with-grpc-cl
[3] https://github.com/grpc/grpc-go/issues/5324
[4] https://pkg.go.dev/google.golang.org/grpc#ClientConn.NewStream
[5] https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/tracing/opentracing/client_interceptors.go#L37-L52
[6] https://github.com/open-telemetry/opentelemetry-go-contrib/blame/main/instrumentation/google.golang.org/grpc/otelgrpc/interceptor.go#L193

Release note: A rare crash indicating a nil-pointer deference in
google.golang.org/grpc/internal/transport.(*Stream).Context(...)
was fixed.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[adde67c1c8...](https://github.com/mrakgr/The-Spiral-Language/commit/adde67c1c81c596c396f1d801a23036d4e3af9e9)
#### Thursday 2022-06-16 18:24:02 by Marko Grdinić

"8:45am. I went to bed at 10:15pm. I am a lot more rested today than I was yesterday. First, let me set the Scatter 5 to download.

8:55am. The rapidgator links are still broken. I see that my post did not show up. Did the admin see them? Whatever.

Dong Bai and Dungeon Meshi go.

9:30am. Let me start. It is time to try out the SceneCity for the first time. It is time to get that thing done.

I think for the sake of skill I might have misinterpreted the meaning of art. Worse, the kind of medium I consume which is manga and anime gave me the wrong impression of what it is.

In programming if you want to just get things done, you do not spend years making your own library and langauge, instead you just import a library other people have done and stitch things together. You do need some basic skill in programming to do that, but it does not need to be 5/5.

The same goes with art. I should not fall into the trap of thinking I have to do everything myself.

The more I start treating it like a Javascript webmonkey treats programming, the more successful I will be. It is really sad. If I start making my own props and charas from scratch I will just be competing with pro props and chara artists, and that would be a waste of time. I have other things that need doing don't I?

9:45pm. It is time to let things go. If I got a job doing programming, I certainly would not be doing it in Spiral. Neither should I expect to be modeling everything on my own. My room was a special case.

Now, let's see if it will work with 3.2 or if I will have to go to an earlier version.

Nope, it does not work. Let me try 3.1. Nope.

9:50am. It works only in 3.0. The later versions are out. So be it.

10am. Hmmm, I have it installed. How do I actually make it work? Let me go back to one of those tutorials.

https://youtu.be/FdDLlm4c5YQ?t=61

He deletes the default cube and puts in the terrain node after that. Ok.

10:05am. Whoa it even generates the clouds.

It put some of the horse chestnut trees in a very weird place. Is it using them as templates for scattering? Yes.

10:30am. Ok, I think I get it.

https://youtu.be/FdDLlm4c5YQ?t=182

Right now what I am wondering is how to make this spherical. I guess I could start with a square and cout out the offending parts by hand.

https://youtu.be/FdDLlm4c5YQ?t=271

This tutorial is actually quite useful.

https://youtu.be/FdDLlm4c5YQ?t=282

Like this it looks quite drab, but if I style transfered it into a drawing or a painting I bet it would look much better.

10:40pm. Ok, let me do a render. Then I'll do a style transfer and see how it comes out.

10:45am. I am a bit confused why it gets stuck on the first sample for so long.

It only updated after 3m. Last time I had to shut down blender to get it to abort. Hmmm, at sample 80 it is much clearer than it was before.

Hmmm, the samples are ramping up rapidly. This is not bad. It is an outdoors scene so it is easy to render. When the render started it said 3h, but now it says 1h left. I think if I leave it on its own it should finish in another 10m.

10:55am. 11m in and it is halfway through the 4k samples.

14m in, and only 1k samples left. It is getting faster. I'll have my render done in a few mins.

11am. Done. It only took 15m. Now I'll put it through style transfer.

Just pencil work and great wave will do for now. Maybe something else with wibrant colors.

11:15am. I was going to try just a few, but let me do a few more.

11:20am. Nice. Let me take a short break.

11:35am. I am back. Let me do a writeup.

///

A few days ago, I set the goal for myself to do a city. Since I had Houdini experience, my first impulse was to make use of it. It wasted a few of my days, and I realized that rather than messing with its half baked nodes, I need specialized programs for the task. I got SceneCity, and here is the default city with a desert theme, 5m to setup and 15m to render. The lighting is poor, but that does not matter as this is just a demo. All this is a good lesson for me as I got stuck for a few days, and broke out by letting go my inhibitions. I developed my various skills over the last 8 months, but if I want quality, I should be using procedural generators and kitbashing. Nothing is going to get me faster to my goals than that. It is like how if you are programming, it is a much better idea to use a library than spend your valuable time doing your own. It is a bit heartbreaking as this way of doing art requires little skill even if it gives the best results, programming went this way long ago. I have some sculpting skills, but I am going to look in chara generators as well after I am done with environments, and only modify them enough to get what I am going for. Doing anything else would mean competing with dedicated prop and chara artists, and nobody is going to reward me for that. My audience is only going to care about the end result.

Anyway, here is the Cycles render, it is too drab and dull. Even if I put in some work, it would still have that distinctive 3d look. 2d artists tend to have distinctive styles that you can tell from the image, but 3d works look similar to one another. This is both due to how 3d renderers work, and how the models are made and textured. The great precision of 3d works against it in this case.

///

12:10pm. Let me also post it on Twitter. Remember that Clarisse render? The reason it looked so good is because I was given all the assets up front and just had to place them. If that was not the case it would taken a good deal longer.

12:20pm. https://twitter.com/Ghostlike/status/1537379979931136001

Here is the Twitter thread. If I get no replies in the /wip/ thread I think I'll stop posting there. I meant to do that last time, but since I got some good reactions apart from people calling me schizo autist I changed my mind.

Hmmm, right. What I need to do is simply check out some other templates and study them. What I also want to do here is try a circular plane, and derive its UVs through projection from view. Also I can't forget that I have 900 images of the VN cover that I should go through. I'll have to make time for that.

1:20pm. Let me chill a bit longer and I will start.

2:20pm. Had to take some time to do the chores. Let me start. Before I do anything else, I have a wish. I want to revisit that picture I made in Houdini and put it through style transfer. It came out particularly plastic, so I am curious as to what I would get. I worked a long time on it, so the least I could do is see what comes out of it.

Also, I am getting crabbed in the /wip/ thread again. If this was my own forum, I'd just ban that guy and move on. But rather than just stand there and take it, I'll just leave. I could reply with a crab image, but it would not be worth it. If those people want to their board to be filled with /beg/s then can have it.

On that note...nobody is upvoting my posts in the PL thread. It is time to abort that as well. It has been overdue on that.

I'll stick to Twitter from here on out. But even Twitter isn't important. I have 5 followers. This is nothing. I'll get a proper audience once I start posting on Royal Road or Scribblehub. There was also a third site, but I forgot what it was called.

https://forum.scribblehub.com/threads/royalroad-vs-scribble-hub.1778/

I guess I'll go with RR.

https://forum.novelupdates.com/threads/other-websites-for-fiction.8195/

Hmmm, I don't know, was there a 3rd site? Maybe it was not after all. I guess I can always post on both RR and SH.

No prob. It is not like the effort will kill me. Now...

Let me check out that old picture.

2:40pm. So far, all of the style transfered images look bad.

2:45pm. Failure. There isn't a style transfered single image that I like in this batch. Maybe I need to try it on a bigger number of styles. For some reason they are messing up the blues.

2:50pm. Nevermind that. I need to get going.

Let me make a bigger city.

Huh, actually, where are the templates that I saw in the Youtube video?

Let me not rush this. SceneCity has its own node editor so it is not that simple. It will take me a while to get a handle on it.

Oh right, since Scatter 5 finished downloading, let me just unpack it.

I'll install it later.

3:20pm. https://youtu.be/bDj28kE63iY
Blender Quick Tip: The scenecity addon

Let me watch this.

https://cgpersia.com/2022/03/kitbash3d-manhattan-183113.html

Also let me download a kitbash kit. Why not make my own city? The way it is structured is a bit confusing to be honest. It has gigabytes in various parts. It seems to have different setups for 3ds Max Maya and Blender. Why is Blender 2.5gb while, 3ds Max is 7 times that?

It has FBX OBJ and Textures in separate spaces. Well, let me get it.

Yesterday when I decided I won't use piecewise procedural generation like with Houdini, that simplified my work tremendously. With that attitude, nothing is really stoping me from kitbashing my own city.

The reason why I am considering that is because scene city is a bit confusing. Apart from the big render node, I am not sure what is going on. The grid city makes sense, but freeform roads crash when I try to execute them. The scatter city does not have roads. It has a tool for terrain generation, but I am guessing I am expected to plug the result of that into the scatter city over terrain template on my own. One thing what I want right now is very large buildings. Let me start the download and then I will watch the tutorial.

https://youtu.be/bDj28kE63iY?t=143

Is this deprecated or not?

https://scenecitydoc.cgchan.com/

The stuff on the main page says that scatter city buildings overlap. Also curved roads do not test for intersections. Grid structures on the other hand work properly. Let me watch some of the tutorials here.

https://twitter.com/CouturierArnaud/status/1467596341878525957
> Generating free-form roads in SceneCity makes Blender 3.0 crash. I'll investigate, but I suspect it is a Blender bug. The rest of the addon works perfectly :)
> Development is going very well, I'll tell you more when the time comes 😉

I've run into this.

> Hi Arnold, I think the scenecity tool seems to have a bug on blender version 3.1 that prevents it from installing properly, is there any chance to fix it?😉
> Hello :) Yes, I'm porting it to Blender 3.1 at the moment. More news normally in a week at most.

There hasn't been any news in quite a while.

3:55pm. Honestly, if this addon could create cities with free form roads that would be really interesting. I understand myself that this is a lot harder than managing grid like structures, but that is why I'd like to see it in an addon.

https://youtu.be/5Z0wDKuXS3I?t=316

Let me stop here with this. I think I should go even further back into 2.93 if I want to run this addon properly, but I do not need free form roads. Let me focus on my priority. I want a skyscaper city. I want it to generate some really tall buildings.

4:10pm. Focus me. Let me see if I can make skycrapers in grid city. I think it has some support for procedural building generation. If it does not have a static building that meets my needs, a dynamic one should do well.

4:25pm. https://scenecitydoc.cgchan.com/

Buildings size map...

> When you want to know more about any particular node, simply click on the Node doc button, it is a direct link and will open its doc page in your web browser, so do not hesitate.

Huh what?

https://scenecitydoc.cgchan.com/scatter-cities/detailed-explanations

There are node docs buttons in the screenshots, but I can't see any of those in node tree.

4:40pm. There is a building height modifier in the easy terrain node. Unfortunrately, now I run into issues with overlapping buildings.

4:50pm. Blender crashed and took out the whole system with it. Worst, it took out the downloads.

Ugh, I am not sure what to think about this. Looking how the default scatter node is creating intersecting buildings, I am really wondering what the value of this addon really is. Considering all the buildings are boxy cubes, just why did it draw on so many resources? Let me load it up again.

Let me take a short break here.

5:05pm. https://www.youtube.com/results?search_query=unity+procedural+city

Let me watch one of these tutorials.

https://youtu.be/jONgvgTzL5k
Procedural City Generation with CScape

So far I am not very enthused with SceneCity. Out of date, poorly documented, unimpressive feature set.

https://youtu.be/jONgvgTzL5k

This is interesting. You can grab a building and increase its size.

5:30pm. > i've never seen someone work so hard to be as lazy as this dude

This is from a /wip/ thread. Yes, this describes me perfectly.

https://youtu.be/jONgvgTzL5k?t=847

I thought this would would be longer, but it cuts off at 14m.

5:45pm. I feel it is coming together for me. Right now I need a break though.

I need just two things which should not be hard to accomplish and then I will have what I need to make the scene.

I just do not feel like doing it. Let me laze for a bit. I'll take a nap for a bit.

6:10pm. Hmmm, I was in bed quite a bit longer than I thought. I guess I am dazed from thsi. At any rate, I've made my plans. Let me see if I can clear two basic hurdles.

6:10pm. Goddamit, doesn't the easy node have anything for night shots? What did the docs say about that. I know it was in the docs.

https://scenecitydoc.cgchan.com/scatter-cities/detailed-explanations
> You can turn on the emit channel for night shots, and off for daytime. With a bit of work you can make the materials more elaborate to increase realism, like adding detail textures, make the windows reflective etc…

6:20pm. I am confused. The emmit channel is already in there.

Oh, the texture itself is black.

https://scenecitydoc.cgchan.com/scatter-cities/detailed-explanations

Yeah, I am retarded. This addon actually has some functionality for creating night textures. What the hell?

6:55pm. No It is just for that scatter thing. Damn it, I really hate this addon. I really do. It is like 3 unfinished city building addons rolled into 1. Giving this a try was my great unluck. I'd be better of learning how to craft individual pieces myself.

I really need an city pack. If that crash did not take out my download I'd already have a chunk of it.

7pm. I am thinking what I should do here. SceneCity is very unsatisfactory to me.

7:10pm. Right now I am stuck again. I am thinking what I should do.

https://kitbash3d.com/products/mini-kit-neo-city

Free assets from Kitbash? Hmmm, this kind of scene above the clouds is something like I've been envisioning.

If it has one, maybe it has other free assets as well. Let me have lunch here and then I will write down my thoughts.

https://www.youtube.com/watch?v=MVNtf33q3pc
TOP 10 FREE Assets for Environment Design in Unity

https://www.youtube.com/watch?v=_UgeDCNadHQ
Brushify - Build A City In UE4

Let me just back up these links.

7:50pm. Done with lunch, but I really do not feel like ranting about it.

7:55pm. https://youtu.be/DseVAuchtmU
Free Kitbash, Greeble and Texture resources DOWNLOADS

I've set the Neo City kit to download. Let me watch the above. It is only 3m.

8:05pm. What is going on, why is the internet connection so slow? Don't tell me that getting WikiArt dataset blew through the budget for the month? Right now I am only getting 80kb/s on that kit. Well, nevermind.

8:15pm. Whops, nearly forgot about the captcha for Manhattan. I got it in time.

Let me close here for the day. I'll come to a decision tomorrow once I take a look at the kit. What I might do is do more research on how to do roads procedurally.

For a paid addon, CityScene is an embarassment. It does none of the difficult parts of what a city generator would be expected to do. It does not give me much over the Scatter addon. In fact, with the Scatter addon I could at least get non-overlapping buildings. At least the grid city part of it has some decent props I'll be able to use. It depends on the whether the Neo City kit turns out to be enough.

8:20pm. In an ideal world just getting an addon would be enough, but it seems I am going to have to develop my city building technique a little. Things aren't always as easy as you want them to be."

---
## [NatsukiAza/Proyecto-7C](https://github.com/NatsukiAza/Proyecto-7C)@[4b284095f0...](https://github.com/NatsukiAza/Proyecto-7C/commit/4b284095f035fbd4bdd70ef056bee38fc9265c2c)
#### Thursday 2022-06-16 18:56:12 by Jaime Howard

estander hir ay relice llu ar lique to mi 

Ding-a-ling-ling-ling-ling-ling-ling-ling!
Boo-ba-doo-ba-doop!
Boo-ba-doo-ba-doop!
Ring ring ring ring ring ring ring
Banana phone
Ring ring ring ring ring ring ring
Banana phone
I've got this feeling, so appealing
For us to get together and sing, sing!
Ring ring ring ring ring ring ring banana phone
Ding dong ding dong ding dong ding donana phone
It grows in bunches, I've got my hunches
It's the best! Beats the rest!
Cellular, modular, interactivodular!
Ring ring ring ring ring ring ring banana phone
Boop-boo-ba-doo-ba-doop!
Ping pong ping pong ping pong ping panana phone
It's no baloney, it ain't a p(h)ony
My cellular bananular phone!
Don't need quarters, don't need dimes
To call a friend of mine!
Don't need computer or TV
To have a real good time!
I'll call for pizza, I'll call my cat
I'll call the white house, have a chat!
I'll place a call around the world, operator get me Beijing-jing-jing-jing!
Yeah!
Play that thing!
Whooo Hooo!
Ring ring ring ring ring ring ring
Banana phone
Boop-boo-ba-doo-ba-doop
Ying yang ying yang ying yang ying yonana phone
It's a real live mama and papa phone
A brother and sister and a dogaphone
A grandpa phone and a grammophone too! Oh yeah!
My cellular, bananular phone!
Banana phone, ring ring ring!
(It's a phone with a peel!)
Banana phone, ring ring ring!
(Now you can have your phone and eat it too!)
Banana phone, ring ring ring!
(This song drives me bananas!)
Banana phone, ring ring ring!
Boo-ba-doo-ba-doop-doop-doop!

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[96df27ab78...](https://github.com/treckstar/yolo-octo-hipster/commit/96df27ab7844a9d89f145b27bd956290c9739b68)
#### Thursday 2022-06-16 19:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Ice-Pendragon/BabelCDB_CustomCard](https://github.com/Ice-Pendragon/BabelCDB_CustomCard)@[37423207dd...](https://github.com/Ice-Pendragon/BabelCDB_CustomCard/commit/37423207dd2d2f6048aca60c240ff3b21e7f0d9b)
#### Thursday 2022-06-16 20:27:04 by Naim

Added new Rush cards

From "Megaroad Pack":
- The Half-Body Crawling Around
- Ghoulish Gal
- The Thing in the Purple Mirror
- The Doll of Dread
- Nightmare Knock
- Frightening Fan Mail
- Zombie Carnival
- Zombie Fireworks
- Surprising Zombie Victory
- Gradually Approaching Footsteps
- The Cursed Cat Counting Dishes
- Terror Phone Number
- Cursed Skeletal Dragon Diarga
- The Strange Specter of Celestial Severance
- Sacrificial Summon
- Progress Potter
- Mother's Storm
- Excitagain
From "Deck Modification Pack - Requiem of Destruction!!":
- Dian Keto the Cure Maiden
- Cremation Dog Nitro
- Dynamo Might
- Chemicalize Salamander
- Rice Terrace Ripple
- Ewekai Aquasheep
- Ewekai Thunderlambda
- Ewekai Airaries
- Ewekai Waveschaf
- Melo Melo Meeeg☆Uuultra Beam
- Splendid Floor Master
- Tutumes Dark Witch
- Ichthyosteguard
- Sunbathing Kappa
- Kappa's Gas
- Miginagi the Talismanic Warrior
- Rainy Megalopolis
- Bubble Kingdom
- Nuvia the Wicked Mischief Maker
- Sannomiya Golden G Robo MK-III
- Alien 33
- The Three Warp-Granny Sisters
- Alien Count of the White Dwarf, St. Germain
- 300 Light-Year Red Cloak
- Third Coming of the Reptilian Count
- Area 33
- The Three Moonlit Mystery Geckos
The "Jump Victory Carnival 2022" promo:
- Luster Dragon

---
## [DirtyApexAlpha/codeql](https://github.com/DirtyApexAlpha/codeql)@[5fcea34eaa...](https://github.com/DirtyApexAlpha/codeql/commit/5fcea34eaab80445c9f0a1b6754a9ba96ef18c1c)
#### Thursday 2022-06-16 20:52:53 by thinkbubble.cloud@thinkbubble.com

 revise PhoenixSmashes.txt

Takes this Artifact Splice off of the thing hate can not defeat Beloved are head to footer and god right above her direct to master...main stage ignition. Recover what is marked and make it mine. If you cannot relate to this in anyway that is the light and dark, both are good! Dare not by questioning harshly with the 3 W's.  Devil's playground no more, changelog  I suggest, "Edens_Acute_Trigger_Many_Entities" |  (-:eat-me;-)  |

---
## [Technobug14/mojave-sun-14](https://github.com/Technobug14/mojave-sun-14)@[2996f41136...](https://github.com/Technobug14/mojave-sun-14/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Thursday 2022-06-16 22:05:49 by EdwardNashton

Update Time: Machinery to People (#2096)

* Update Time: Machinery to People

Added a recorders and server racks all over the city.

Slightly changed a "Cheap Motel" near Police Dept.

Slightly changed Police Dept.

Slightly updated Chemical Factory and Weather Station.

* Update time: small fixes

Changed a servers on Power Plant.

* Update Time: that god damn room in PD

I hope we're done with it.

* Update Time: small fix

Removed a potential feature with "shutter trap" in PD.

* Update Time: fixes and updating Water Treatment Station

You made me do this, Original.

* Update Time: one day the south dir comes, we'll place our stuff and go

Sometimes you get too picky

Co-authored-by: Edward Nashton <eddienigma48@gmail.com>

---
## [Alia5/GlosSI](https://github.com/Alia5/GlosSI)@[ae45a9918b...](https://github.com/Alia5/GlosSI/commit/ae45a9918bcecb0b51bc12a280f0bbcf7e53b4db)
#### Thursday 2022-06-16 22:13:14 by Peter Repukat

Fix build

Fix stupid visual studio paths
My gosh, you suck!

Why cannot it be **easily** possible to include icons RELATIV THE THE FUCKING SOLUTION?! FUCK MICROCRAP

---
## [viruscreator12233/fuck-you-virus](https://github.com/viruscreator12233/fuck-you-virus)@[65286a1006...](https://github.com/viruscreator12233/fuck-you-virus/commit/65286a10066bc87ff3ad08cbbdf9524aec23f6da)
#### Thursday 2022-06-16 22:32:08 by viruscreator12233

Virus code

So you are going to copy and paste the code into the windows notepad, you are going to click file and then save as Fuck You.vbs, the name is optional but it has to end with .vbs, save it to documents, then you are going to go to my computer, go to documents, and click on the file, it should make a lot of popups but you can fix it by shutting down you computer or restarting it, this virus is harmless unless you have a slow pc. Do not do this unless you have a vm to test it on, that's all, good luck!

---
## [focus-trap/focus-trap](https://github.com/focus-trap/focus-trap)@[1ef05963d5...](https://github.com/focus-trap/focus-trap/commit/1ef05963d5f3ea043569ece299896b9bacbed5a6)
#### Thursday 2022-06-16 22:38:06 by Stefan Cameron

Migrate to Cypress 10

- Ran `cypress open` and followed instructions in Migration Helper
- Renamed cypress.config.ts to cypress.config.js because typings are ridiculous
  (errors in typings in there when there's no issues are just annoying)
- Attempted to add code coverage support, and did get this working locally, however
  no coverage was measured. I don't believe that's because the code wasn't instrumented
  because the .nyc_output/out.json was generated (which proves code was instrumented).
  I think it's because we're starting a separate server and having Cypress access the
  demo from there. This is different from the setup we have on tabbable where we don't
  have to do this and coverage works very well. Something for another day and maybe
  another contributor.
- Modernized the GitHub ci.yml.

---
## [Mqisty/Alternatives](https://github.com/Mqisty/Alternatives)@[126308e18e...](https://github.com/Mqisty/Alternatives/commit/126308e18e6759a3412415be643b775e8f123be4)
#### Thursday 2022-06-16 22:47:14 by Sam

1.12.2 Feather - Changed curseforge links (that site is awful oh my god)

---
## [Ebb-Real/tgstation](https://github.com/Ebb-Real/tgstation)@[95ffcd4e19...](https://github.com/Ebb-Real/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Thursday 2022-06-16 23:21:54 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[a5bbfcc41c...](https://github.com/LemonInTheDark/tgstation/commit/a5bbfcc41c8f9263bc0e0e0020e3a718da02b92e)
#### Thursday 2022-06-16 23:29:49 by LemonInTheDark

Haha johnathan I am dying (Resolves PM issues on map views)

Ok so like, there's this idea in byond, about submaps
Basically we can use a prefix before screen_loc values, and some byond
dmf fuckery to get a second map window to draw to.

We'd then setup some plane masters with appropriate screen locs, and use
vis_contents or just appearances to get an object with the appropriate
screen_loc to look like the thing we wanna mimic.

This is how we do camera consoles and such.

Basically, this system needs to account for offset planes. But as I was
working on it, it occured to me: shouldn't it also account for stuff
that modifies planes, basically shouldn't huds "know" what planes are
effecting them.

In persuit of this, I refactored how plane masters are handled, adding
plane groups, that represent planes rendered on some particular screen.

It in theory supports preloading plane masters, and applying them to
huds later, tho I have yet to find use for that.

In addition, life continues to be suffering, so I refactored all uses of
this pattern to use one consistent object, in the same rough way.

This makes the code a lot easier to reason about and read, and makes
making modifications to the pattern much easier

Note to self: If I'm gonna do this whole plane master group thing, I
might need a way to get existing "modifiacations" to plane masters

That or just nut up and make most things use the main group, not sure

Oh and I'm gonna make the debug window capable of editing these things,
for sniks

---

