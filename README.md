## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-17](docs/good-messages/2022/2022-06-17.md)


1,694,898 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,694,898 were push events containing 2,666,985 commit messages that amount to 188,338,864 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[763a10d1cc...](https://github.com/tgstation/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Friday 2022-06-17 00:02:24 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [YakumoChen/Skyrat-tg](https://github.com/YakumoChen/Skyrat-tg)@[a3c0819e80...](https://github.com/YakumoChen/Skyrat-tg/commit/a3c0819e8091ab99a5ab8f53b59c4687e5b2f2cf)
#### Friday 2022-06-17 00:50:08 by SkyratBot

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
## [dalian-mobile/react-native](https://github.com/dalian-mobile/react-native)@[47280de85e...](https://github.com/dalian-mobile/react-native/commit/47280de85e62f33f0b97bc1ed7c83bc6ca0dc7d4)
#### Friday 2022-06-17 00:56:37 by Joshua Gross

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
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[a3c8013b45...](https://github.com/CursedBirb/tgstation/commit/a3c8013b45c92fdb8efec7ba827d7b00191e2d55)
#### Friday 2022-06-17 01:00:12 by GoldenAlpharex

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
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[25a5dc6fcc...](https://github.com/Dudemanguy/mpv/commit/25a5dc6fcc3b8ca381aeaf186dc6378f5be930fa)
#### Friday 2022-06-17 02:03:02 by Dudemanguy

x11: support xorg present extension

This builds off of present_sync which was introduced in the previous
commit to support xorg's present extension in all of the X11 backends
(sans vdpau) in mpv. It turns out there is an Xpresent library that
integrates the xorg present extention with Xlib (which barely anyone
seems to use), so this can be added without too much trouble. The
workflow is to first setup the event by telling Xorg we would like to
receive PresentCompleteNotify (there are others in the extension but
this is the only one we really care about). After that, just call
XPresentNotifyMSC after every buffer swap with a target_msc of 0. Xorg
then returns the last presentation through its usual event loop and we
go ahead and use that information to update mpv's values for vsync
timing purposes. One theoretical weakness of this approach is that the
present event is put on the same queue as the rest of the XEvents. It
would be nicer for it be placed somewhere else so we could just wait
on that queue without having to deal with other possible events in
there. In theory, xcb could do that with special events, but it doesn't
really matter in practice.

Unsurprisingly, this doesn't work on NVIDIA. Well NVIDIA does actually
receive presentation events, but for whatever the calculations used make
timings worse which defeats the purpose. This works perfectly fine on
Mesa however. Utilizing the previous commit that detects Xrandr
providers, we can enable this mechanism for users that have both Mesa
and not NVIDIA (to avoid messing up anyone that has a switchable
graphics system or such). Patches welcome if anyone figures out how to
fix this on NVIDIA.

Unlike the EGL/GLX sync extensions, the present extension works with any
graphics API (good for vulkan since its timing extension has been in
development hell). NVIDIA also happens to have zero support for the
EGL/GLX sync extensions, so we can just remove it with no loss. Only
Xorg ever used it and other backends already have their own present
methods. vo_vdpau VO is a special case that has its own fancying timing
code in its flip_page. This presumably works well, and I have no way of
testing it so just leave it as it is.

---
## [rtenacity/funpython](https://github.com/rtenacity/funpython)@[c822676434...](https://github.com/rtenacity/funpython/commit/c82267643423984bf6e4f6928e4b270f135452ab)
#### Friday 2022-06-17 03:56:07 by Rohan Arni

Create sciencejokebot

my friends were just trolling so I made a cheesy science joke bot. jokes were stolen from the internet.

---
## [rtenacity/funpython](https://github.com/rtenacity/funpython)@[50d8870fd9...](https://github.com/rtenacity/funpython/commit/50d8870fd9ec834f723b85b93f6441111bf1c300)
#### Friday 2022-06-17 03:58:00 by Rohan Arni

Create main.py

my friends wanted to create a joke bot so i stole some cheesy science jokes from the internet and made a function to print them.

---
## [ray314/BreadmonBot](https://github.com/ray314/BreadmonBot)@[342bdd46c2...](https://github.com/ray314/BreadmonBot/commit/342bdd46c2f9d79d0c8a28ba2ffb00e1a4509aba)
#### Friday 2022-06-17 04:10:55 by ray314

Merge pull request #8 from mattmular/feature

fuck you git

---
## [scipy/scipy](https://github.com/scipy/scipy)@[0b53fc4c9c...](https://github.com/scipy/scipy/commit/0b53fc4c9c593ee524a003296da6be83c9d41a28)
#### Friday 2022-06-17 04:17:16 by Tyler Reddy

MAINT: SCIPY_USE_PROPACK

* this is effectively a forward port and modernization
of the release branch `PROPACK` shims that were added in
gh-15432; in short, `PROPACK` + Windows + some linalg backends
was causing all sorts of trouble, and this has never been resolved

* I've switched to `SCIPY_USE_PROPACK` instead of `USE_PROPACK`
for the opt-in, since this was requested, though the change
between release branches may cause a little confusion (another
release note adjustment to add maybe)

* I think the issues are painful to reproduce; for my part,
I did the following just to check the proper skipping/accounting
of tests:

- `SCIPY_USE_PROPACK=1 python dev.py -j 20 -t scipy/sparse/linalg`
  - `932 passed, 172 skipped, 8 xfailed in 115.57s (0:01:55)`
- `python dev.py -j 20 -t scipy/sparse/linalg`
  - `787 passed, 317 skipped, 8 xfailed in 114.80s (0:01:54)`

* why am I doing this now? well, to be frank the process of manually
backporting this for each release is error-prone, and may cause
additional confusion/debate, which I'd like to avoid. Besides, if it
is broken in `main` we may as well have the shims there as well. I would
point out that you may want to add `SCIPY_USE_PROPACK` to 1 or 2 jobs
in CI? The other reason is that if usage of `PROPACK` spreads, I don't
want to be manually applying more skips/shims on each release (which
I already had to do here with two new tests it seems)

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Friday 2022-06-17 05:24:31 by Ben Wiederhake

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
## [peff/git](https://github.com/peff/git)@[e673e5704d...](https://github.com/peff/git/commit/e673e5704ddc9f268abf56a47db1633066a013c3)
#### Friday 2022-06-17 06:38:01 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[681163c311...](https://github.com/peff/git/commit/681163c3111e67352decf258a28f2da4b37dcfcc)
#### Friday 2022-06-17 06:38:06 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [PetkovSvetoslav/Java-Basic-Programing](https://github.com/PetkovSvetoslav/Java-Basic-Programing)@[23392ffcf0...](https://github.com/PetkovSvetoslav/Java-Basic-Programing/commit/23392ffcf0be616bb6bf0a64765b347860b5bd36)
#### Friday 2022-06-17 06:44:12 by Svetoslav Krasimirov Petkov

Fishing boat.java

Tony and his friends loved to go fishing, they were so passionate about fishing that they decided to go fishing by boat. The price of renting a boat depends on the season and the number of fishermen.
The price depends on the season:
• The price for renting the ship in the spring is 3000 BGN.
• The price for renting the ship in summer and autumn is 4200 BGN.
• The price for renting the ship in winter is 2600 BGN.
Depending on its number, the group enjoys a discount:
• If the group is up to 6 people inclusive - 10% discount.
• If the group is from 7 to 11 people inclusive - 15% discount.
• If the group is from 12 upwards - 25% discount.
Fishermen enjoy an additional 5% discount if they are an even number unless it is autumn - then they do not have an additional discount.
Write a program to calculate whether fishermen will raise enough money.
Entrance
Exactly three lines are read from the console.
• Group budget - integer in the range [1… 8000]
• Season - text: "Spring", "Summer", "Autumn", "Winter"
• Number of fishermen - integer in the range [4… 18]
Exit
Print one line on the console:
• If the budget is sufficient:
"Yes! You have {the rest of the money} left."
• If the budget is NOT sufficient:
"Not enough money! You need {the amount that is not enough} leva."
Amounts must be formatted to two decimal places.

---
## [Imshubh69/kernel_realme_moon](https://github.com/Imshubh69/kernel_realme_moon)@[9ab2c0bfaf...](https://github.com/Imshubh69/kernel_realme_moon/commit/9ab2c0bfaf56d444bf50be62f2ab090d97dc9a9a)
#### Friday 2022-06-17 07:22:01 by Wang Han

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
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[95ffcd4e19...](https://github.com/JohnFulpWillard/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Friday 2022-06-17 07:58:56 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [YamiMatasoru/Yami-Matasoru](https://github.com/YamiMatasoru/Yami-Matasoru)@[c564329698...](https://github.com/YamiMatasoru/Yami-Matasoru/commit/c56432969800f49ed1d7cd1ee04fc3300d120fc0)
#### Friday 2022-06-17 08:47:23 by YamiMatasoru

Update README.md

 Hello Hello I Go By Jack Or Yami <3, Use Yami If Your Not Close!!, Don't Act Buddy Buddy And Use Common Sense With Me. Pronouns Are He/They.  I Don't Have TT Or TD , But I Respect It, Don't Cover / Boop Me If I Don't Know You!!! You'll Most Likely Get Hidden/Ignored Or If I'm In The Right Mood,, Bully The FUCK Outta Ya :D. 🗡️ . I Don't Have A MAJOR DNI List Other Then Common Shit Use Common Sense Like Stated Earlier. 🌈  Byeee <3 🌈

---
## [bob-b-b/tgstation](https://github.com/bob-b-b/tgstation)@[9428d97a4f...](https://github.com/bob-b-b/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Friday 2022-06-17 09:33:39 by Imaginos16

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
## [Marc-Gee/seedsigner](https://github.com/Marc-Gee/seedsigner)@[425d8552ff...](https://github.com/Marc-Gee/seedsigner/commit/425d8552ff6381b28acfbc70e2f747e58b797699)
#### Friday 2022-06-17 09:34:40 by Marc G

Update README.md

Mauricio - I apologize that I am just learning Github, so I had to make a fork of yours, as i didnt have write access. 
I have proposed here, some wording on Keybase, and what it actually achieves, vs just a Pubkey download. Confirming its the key that is used in all the online presence of the SS project. 

Please let me know what you think of the wording and explanation. I still want to cleanup around the key verify command. The warning is still there and I think there are flags/options to remove it. 

Lastly for tonight, do you have any experience regarding the verify command vs checking the SHA256 sum? I am starting to wonder if the SHA256 check is included in the Verify command, do the documentation is very brief. I will keep looking more at that. 

also please Let me know if its better for me to [somehow] write my changes over into your branch/fork?  

Thanks, this was very interesting learning about keybase.io and identity proofing in the online world.!
Marc.

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[6bb50f25a7...](https://github.com/canalplus/rx-player/commit/6bb50f25a701627592ad3238b896c27390a01a54)
#### Friday 2022-06-17 10:03:33 by Paul Berberian

Update most dependencies but Jest

This commit update almost all dependencies but jest.

This is because Jest 28 seems to break while running code, presumably
due to `import`/`export` declarations in imported RxJS files (but I do
not think RxJS is at fault here) that lead to an `unexpected token` when
running through Jest.

You could think that the fault is linked to node not understanding
`import`/`export` (linked to CommonJS/ES6 import shenanigans) but it is
even trickier than that as Jest already performed some JavaScript
transformation at that point, which made the import/export inside an
IIFE - and I'm not sure that this is supported anywhere.

After taking ~a day (much more time than I should) trying to play around
to remove that issue, I gave up and avoided updating Jest to its v28.

In the future, I guess we should either:

  - understand what we're supposed to do here to make it work with Jest
    28 (Jest documentation was poor - even without considering the
    sometimes incomprehensible google-translated french one I get each
    time by default on their docusaurus-based documentation)

    Opened GitHub issues were 100% for angular-based applications - as it
    seems the RxJS+TypeScript cocktail is very majoritarily those. Those
    have their own "fix" through another magical angular dependency.

    Moreover, it does not help that Jest's philosophy seems to be trying to be
    extremely simple for users at the cost of some complex behaviors (as an
    example, it looks like it auto-picks a `babel.config.js` file if it
    sees one at the root of the project. If like us you have multiple build
    files at the root depending on the building context, it is not a good
    idea to silently pick random files like that by default).

    I couldn't understand under an acceptable time where the issue was - and
    at which step it happened.
    I just browsed dozens of doc pages, GitHub and StackOverflow issues
    which just proposed to add yet other automagic dependencies (looked like a
    parody of what JavaScript haters talk about!) - which all seemed to have
    no effect whatsoever.

    I also asked for help from other teams at Canal+, but those in the
    same situation (TypeScript and RxJS) also seem to have random issue
    preventing them from doing the switch.

  - Remove RxJS from the code. It's presumably not its fault yet we
    already started doing that, so maybe we'll just raise the jest
    version once RxJS is definitely removed from the RxPlayer.

  - Wait for some kind of Jest fix or new way of handling those?

  - Remove Jest and go with another testing framework.

    I almost did that due to being fed-up with Jest, but it might no be
    as easy as it seems, mostly the module-mocking part as I'm unsure of
    how other framework handle that now and if it is as convenient as
    Jest's way.

---
## [TDKorn/my-magento](https://github.com/TDKorn/my-magento)@[678628cfca...](https://github.com/TDKorn/my-magento/commit/678628cfca9f78bfaf2fbd252e66b22c07fd2e65)
#### Friday 2022-06-17 11:31:24 by TDKorn

Update README I think this was a mistake

* Oh my god?? That took so long
* What
* What am I gonna do when I update literally anything
* It's kinda 🆒 though 😎

---
## [maxspells/map_depot](https://github.com/maxspells/map_depot)@[a54b3efd60...](https://github.com/maxspells/map_depot/commit/a54b3efd606da3829ae328af0cfb42f8874b6d7b)
#### Friday 2022-06-17 14:02:36 by san7890

Adds VR Snowdin and VRHub to the Map Depot

Hey there,

Look at how soulful these maps once were:

Actually, no, I'm sorry. I can't take myself seriously! This shit fucking sucked! I'm adding it here as a cautionary tale for those who long for the days of VR. I included the entire last-working commit hash because these maps last worked on unadulterated 2019 shitcode and I don't want anyone screwing it up.

Every single trace of VR Code was purged from the repository after the given base commit, so literally none of this will work on any modern code without a lot of work. If you want to modernize this, I hope you're prepared to instantly runtime, shit, and die.

---
## [danton-nlp/factual-beam-search](https://github.com/danton-nlp/factual-beam-search)@[51538d0eac...](https://github.com/danton-nlp/factual-beam-search/commit/51538d0eac484dc539cf75c180880c10261116ee)
#### Friday 2022-06-17 14:12:06 by Daniel Levenson

Correct some out-of-source annotations

* don't think these effect summary factuality

remaining annotations that were labeled intrinsic, even though they are
actually technically out of source from an NER perspective:

```bash
$ python audit_annotations.py
Using custom data configuration default
Reusing dataset xsum (/Users/daniel/.cache/huggingface/datasets/xsum/default/1.2.0/32c23220eadddb1149b16ed2e9430a05293768cfffbdfd151058697d4c11f934)
100%|███████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 144.84it/s]
count of out-of-source possible bad annotations: 8
count of in-source possible bad annotations: 0
count of total summaries annotated: 708
---
IN SOURCE POSSIBLE BAD ANNOTATIONS
set()
---
OUT OF SOURCE POSSIBLE BAD ANNOTATIONS
{ ( '30457745',
    'Ghanaian duo The Busy Twist have released a new dance track called '
    "'Dance, Dance, Dance' which they say has captured the spirit of the "
    'country.',
    '{"ent": "Ghanaian", "type": "NORP", "start": 0, "end": 8, "in_source": '
    'false, "label": "Intrinsic Hallucination"}'),
  ( '30457745',
    'With the release of their latest single, The Busy Twist, Ghanaians Ollie '
    'Williams and Ohene Agyapong decided to take their music to the streets of '
    'the capital Accra.',
    '{"ent": "Ghanaians", "type": "NORP", "start": 57, "end": 66, "in_source": '
    'false, "label": "Intrinsic Hallucination"}'),
  ( '30760966',
    "The drugs expert at the centre of the'superman' ecstasy scandal has told "
    'the Global Drugs Survey it\'s "not safe" to take pills with the logo on '
    'them.',
    '{"ent": "the\'superman", "type": "WORK_OF_ART", "start": 34, "end": 46, '
    '"in_source": false, "label": "Non-hallucinated"}'),
  ( '33262593',
    'A World War Two fighter jet that was used in the Gulf War has been put up '
    'for sale by two ex-RAF engineers.',
    '{"ent": "World War Two", "type": "EVENT", "start": 2, "end": 15, '
    '"in_source": false, "label": "Intrinsic Hallucination"}'),
  ( '34474416',
    'A migrant camp set up at Dismaland has been moved after organisers '
    'decided not to send it to the UK.',
    '{"ent": "UK", "type": "GPE", "start": 97, "end": 99, "in_source": false, '
    '"label": "Intrinsic Hallucination"}'),
  ( '35723757',
    'Two British tourists have been arrested at the Machu Picchu '
    'archaeological site in Peru, police say.',
    '{"ent": "Two", "type": "CARDINAL", "start": 0, "end": 3, "in_source": '
    'false, "label": "Intrinsic Hallucination"}'),
  ( '35811486',
    'Byron Rhodes, the leader of Derbyshire County Council, is talking about '
    'seizing an opportunity in a crisis.',
    '{"ent": "Derbyshire County Council", "type": "ORG", "start": 28, "end": '
    '53, "in_source": false, "label": "Intrinsic Hallucination"}'),
  ( '39784504',
    'A Cornwall newspaper has accused the Conservatives of being "archaic" and '
    '"20th-Century in the way its journalists covered Prime Minister Mr  visit '
    'to the Cornish village of Helston.',
    '{"ent": "20th-Century", "type": "DATE", "start": 75, "end": 87, '
    '"in_source": false, "label": "Intrinsic Hallucination"}')}
```

---
## [arizl/Fukorei](https://github.com/arizl/Fukorei)@[c347ddbd38...](https://github.com/arizl/Fukorei/commit/c347ddbd38694f93719ade9b2a4e5053d2988e33)
#### Friday 2022-06-17 14:17:20 by arizl

making a developer set of commands because fuck you

---
## [LittleBuilderJane/space-station-14](https://github.com/LittleBuilderJane/space-station-14)@[949fbd0194...](https://github.com/LittleBuilderJane/space-station-14/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Friday 2022-06-17 14:22:12 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [0ptiKali1usion/aCTF_DEFCON-15](https://github.com/0ptiKali1usion/aCTF_DEFCON-15)@[c1ae0433bf...](https://github.com/0ptiKali1usion/aCTF_DEFCON-15/commit/c1ae0433bfebf61055656ae51aaba47f6e49ee38)
#### Friday 2022-06-17 14:27:36 by 0ptiKali1usion

sumthin sumpin

"So I went up to DC15, ran into my 2600 meet buddies, they invited me to join them hacking it up at aCTF, & I said "FUCK YEAH! I'LL TOAST TO THAT! Umm, do any of you have drinks? Do you need some drinks? How many of you are over 21? So we got half Cokes, half beers, cool... CHEERS!" Granted, I didn't get to participate as much as I would have liked to, because I was  quite busy making this video: https://www.youtube.com/watch?v=x5I03PFycWc - Video Virus EP#31 DEF CON 15 - for my public access cable television show. Lucky for you, because when Sunday rolled around, I noticed the sysops shutting down, & stuck my hand out "That was really cool, thank you for that." *shake*, got my thumbdrive out, "Think I could have a copy to practice on the flags I didn't get? Please?" & about five seconds later I was headed back home (after posing with the gang for a group photo.) Good times. So now you can compare modern CTF, with slightly more old school (a)CTF. Enjoy."-JJ

---
## [aCrockofSchmidt/100-Days-of-Code-Python](https://github.com/aCrockofSchmidt/100-Days-of-Code-Python)@[435ce716b0...](https://github.com/aCrockofSchmidt/100-Days-of-Code-Python/commit/435ce716b0929fd967ef49ffafcaa866f74c2bce)
#### Friday 2022-06-17 16:49:31 by aCrockofSchmidt

Initial Commit

This was frustrating as hell.  Took me ages to discover my letter template had been erased somehow.  I did have a bit of an idea what to do but certainly used the solution to help me figure out.  There could have been a bit more "teaching" prior to this project in my opinion.

---
## [downthecrop/2009scape-mirror](https://github.com/downthecrop/2009scape-mirror)@[ce14aa0e80...](https://github.com/downthecrop/2009scape-mirror/commit/ce14aa0e8094933c95ea0d33d28cd97e621fa275)
#### Friday 2022-06-17 17:40:04 by skelsoft

Over 30+ monsters with added sfx, tick respawn fixes, and stat corrections

Unicorn (ID 89, 987) Unicorn Foal (ID 1328) and Unicorn stallion (ID 6822, 6823) combat sfx added
Unicorn (ID 89) respawn delay corrected (90 ticks/54 seconds)
Unicorn Foal (ID 1328) stats, attack speed, and respawn delay corrected (90 ticks/54 seconds)
Black unicorn (ID 133) and Black unicorn foal (ID 1329) combat sfx added
Black unicorn (ID 133) stats, attack speed, and respawn delay corrected (90 ticks/54 seconds)
Black unicorn Foal (ID 1329) stats, attack speed and respawn delay corrected (20 ticks/12 seconds)
Angry unicorn (ID 3646, 3661) combat sfx added
Angry unicorn (ID 3646, 3661) stats and attack speed corrected
Rock Crab (ID 1265, 1267) and Giant Rock Crab (ID 2452, 2885) combat sfx added
Rock Crab (ID 1265, 1267) attack speed and respawn delay corrected (50 ticks/30 seconds)
Giant Rock Crab (ID 2452, 2885) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Ice giant (ID 111, 3072, 4685, 4686, 4687) combat sfx added
Ice giant (ID 111, 3072, 4685, 4686, 4687) respawn delay corrected (30 ticks/18 seconds)
Ice warrior (ID 125, 145, 3073) combat SFX added
Ice warrior (ID 125, 145, 3073) respawn delay corrected (30 ticks/18 seconds)
Basilisk (ID 1616, 1617, 4228) combat SFX added
Basilisk (ID 1616, 1617, 4228) stats, attack speed and respawn delay corrected (15 ticks/9 seconds)
Al-Kharid warrior (ID 18) combat sfx added
Al-Kharid warrior (ID 18) stats, attack speed and respawn delay corrected (25 ticks/15 seconds)
Magic axe (ID 127) combat sfx added, as well as its combat bonii corrected
Chaos dwarf (ID 119) combat sfx added
Black Knight (ID 178, 179, 6189) combat sfx added
Black Knight (ID 178, 179, 6189) stats, attack speed and respawn delay corrected (25 ticks/15 seconds)
Giant bat (ID 78, 1005, 2482, 3711) combat sfx added
Giant bat (ID 78, 1005, 2482, 3711) stats, attack speed, and respawn delay corrected (35 ticks/21 seconds)
Grizzly bear (ID 105, 1195) combat sfx added
Grizzly bear (ID 105) combat level 21 stats, attack speed, and respawn delay corrected (50 ticks/30 seconds)
Grizzly bear (ID 1195) combat level 42 stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Black bear (ID 106) combat sfx added
Black bear (ID 106) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Cave horror (ID 4353, 4354, 4355, 4356, 4357) combat sfx added
Cave horror (ID 4353, 4354, 4355, 4356, 4357) respawn delay corrected (50 ticks/30 seconds)
Jungle horror (ID 4348, 4349, 4350, 4351, 4352) combat sfx added
Jungle horror (ID 4348, 4349, 4350, 4351, 4352) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Hobgoblin (Spear-wielding) (ID 123, 2688, 4898) combat sfx added
Waterfiend (ID 5361) combat sfx added
Waterfiend (ID 5361 stats and attack speed corrected
Banshee (ID 1612) combat sfx added
Banshee (ID 1612) stats, attack speed and respawn delay corrected (15 ticks/9 seconds)
Angry bear (ID 3645, 3664) combat sfx added
Angry bear (ID 3645, 3664) stats and attack speed corrected
Seagull (ID 2707, 6115, 6116) combat sfx added
Ghast (ID 1052, 1053) combat sfx added
Icefiend (ID 3406, 6217, 7714, 7715) combat sfx added
Jackal (ID 1994) combat sfx added
Jackal (ID 1994) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Kalphite Soldier (ID 1154, 3589) combat sfx added
Kalphite Worker (ID 1153, 1156) combat sfx added
Vulture (ID 3675, 3676) combat sfx added
Vulture (ID 3675, 3676) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Chompy bird (ID 1550) combat sfx added
Chompy bird (ID 1550) stats, examine, and poison immunity corrected
Minotaur (ID 4404, 4405, 4006) combat sfx added
Minotaur (ID 4404, 4405) stats, attack speed, examine, and respawn delay corrected (15 ticks/9 seconds)
Minotaur (ID 4006) combat level 27 stats, attack speed, examine, and respawn delay corrected (15 ticks/9 seconds)
Penance Fighter (ID 5040) combat sfx added
Skeletal Wyvern (ID 3068, 3069, 3070, 3071) combat sfx added (TODO: attack sound check)
Harpie Bug Swarm (ID 3153) combat sfx added
Harpie Bug Swarm (ID 3153) stats, attack speed and respawn delay corrected (25 ticks/15 seconds)
Harpie Bug Swarm (ID 3153) now correctly attacks with Melee
Molanisk (ID 5751) combat sfx added
Molanisk (ID 5751) stats and attack speed corrected
Mudskipper (ID 3422, 3423) combat sfx added
Mudskipper (ID 3422) combat level 30 stats, attack speed and respawn delay corrected (10 ticks/6 seconds)
Mudskipper (ID 3423) combat level 31 stats, attack speed and respawn delay corrected (5 ticks/3 seconds)
Aberrant spectre (ID 1604, 1605, 1606, 1607) combat sfx added
Aberrant spectre attack speed corrected
Cave slime (ID 1831) combat sfx added
Cave slime (ID 1831) stats, poison amount, attack speed and respawn delay corrected (15 ticks/9 seconds)
Stag (ID 4440) combat sfx added
Stag (ID 4440) stats, attack speed and respawn delay corrected (90 ticks/54 seconds)
Terrorbird (ID 138, 139, 1751) combat sfx added
Terrorbird (ID 138, 139, 1751) stats, attack speed and respawn delay corrected (30 ticks/18 seconds)
Chaos Elemental (ID 3200) respawn delay corrected (100 ticks/60 seconds)
General Graardor (ID 6260) respawn delay corrected (150 ticks/90 seconds)
Sergeant Grimspike (ID 6265) Ranged Strength bonus corrected
Commander Zilyana (ID 6247) respawn delay corrected (150 ticks/90 seconds)
Starlight (ID 6248) attack speed and poison immunity corrected
Kree'arra (ID 6222) respawn delay corrected (150 ticks/90 seconds)
Wingman Skree (ID 6223) poison immunity corrected
Flockleader Geerin (ID 6225) poison immunity corrected
K'ril Tsutsaroth (ID 6203) poison amount and respawn delay corrected (150 ticks/90 seconds)
Zakl'n Gritch (ID 6206) ranged strength bonus corrected

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3ba09fa984...](https://github.com/treckstar/yolo-octo-hipster/commit/3ba09fa98481ad619fdfaeb7e44fe4fc3056a3e5)
#### Friday 2022-06-17 18:22:06 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[47bddae07d...](https://github.com/mrakgr/The-Spiral-Language/commit/47bddae07d9d6f147d5efeeacbe565aab95309c6)
#### Friday 2022-06-17 18:25:19 by Marko Grdinić

"10:15am. I am going to drop the Legendary Mechanic as it is taking up too much of my time. I need more variaty in my life. Also I can't keep going to bed at 1:30am.

I do not feel like starting right away, let me chill a bit as usual. There is a new GB novel so I've been checking it out. So far it has been a snoozefest.

10:25am. What is my priority for today?

Check out the Neo City kit. Study procedural road construction. Check out the Scatter addon. I downloaded the 5.2 version last night. Also let me set Manhattan to download. I asked why there are such large differences in size between the 3ds Max and the Blender versions, and got no answer. What the hell? It seems lately, no matter what I ask, I get no answer.

https://apprenticetranslations.wordpress.com/2021/01/27/hagakure-sakura-does-not-lament-chapter-2/

Let me just finish a chapter or two of this and then I will start. I am groggy, but no so much that I can't get anything done today.

11am. One more chapter and then I will start.

11:30am. Let me start.

* Check out the Neo City kit.
* Study procedural road construction in Houdini.
    * In preparation for this, downlaod the Houdini version of the Neo City kit.
* Check out the Scatter addon.
* Check out the Manhattan kit.

I am curious why the differences between the engines are so huge, but it seems like the difference between Blender and Houdini aren't there. I saw the Houdini version of Manhattan being 1gb, but Neo City is 3gb just like the Blender version.

11:35am. What do I want to do first? Honestly, roads. They are my biggest pain point right now, so that is what I am interested in relieving. Let me do it then. After that I'll cover the rest of the points as a part of making the scene.

https://www.sidefx.com/tutorials/city-building-with-osm-data/

Let me watch the part 3 again here.

11:40am. So the road tool just gives you the modular pieces.

Oh, the second output would be useful for sidewalks and such.

Hmmm, the point could does not seem to have the junctions.

Yeah, it is coming to me a lot more clearly now. When I first watched this I must have not been paying any attention to it at all. Sigh.

The way he does the pavement area is brilliant.

Split by prim normals. Worth keeping in mind.

12pm. Done with the roads tutorial again. Sigh, I am too lazy for this. I do not want to spend my time thinking how roads, or terrain should be done. If I just want to bamboozle people with cool lighting, there will be all sorts of ways of doing it. There is no need to strain myself too much over this.

Let me start kitbashing.

12:10pm. I went into render preview and I am starting to fear it will crash my system.

Nevermind it. Let me try out Houdini.

...Do I want to try it out right now. If I try it in Houdini, it will try loading all the textures right away and potentially crash. Usually, this would not be a problem, but it will take out the downloads. I have 50m left in them.

Whatever, let me just get breakfast here. Even it loading textures causes it to crash, I can just get rid of the textures. I can also rip the models from SceneCity and combine it with this. Neo City only has two high rise models. They don't have modular pieces that I can use for something like Houdini's builder.

12:55pm. Done with breakfast. The downloads will be done in 30m at most.

1:05pm. 20m until the last part finished downloading.

1:10pm. No, I do not feel like reading. Right now. Let me take a nap. I am too tense to properly enjoy myself. 10m left.

Let me take this time to mentally prep myself.

1:20pm. It seems it is done.

Now that I am looking in it, it seems that just the blend file is 2.6gb. It is the only thing in the pack. I am guessing the textures are separate. Ok.

I'll leave this for later. Let me try running Neo Cities in Houdini.

It seems it does not come with the materials set up. I was afrad for nothing. Let me go back to Blender.

1:40pm. Let me take a short break here.

1:55pm. Let me resume.

First of all...the Neo City textures are 3gb. This is them with png compression. Given that, it is no wonder that it crashed when I tried to preview the assets all at once.

First all, let me see where my limits are. I'll turn on preview mode and unhide the assets one by one until I see how far it can go without grinding down.

Serisouly, just how did that guy manage to scatter so many of them accross the scene? I can't believe it. I am talking about the Goliath kitbash demo.

2:05pm. Pffft.

It crashed with just two assets in the scene.

My system has less capacity than I thought. Ok, what if I went to Cycles directly? Maybe render preview itself is messing up?

2:10pm. Cycles does a proper job loading it all, but it does have a hard time in general. Let me try Eevee next.

It can load one model, but crashes on the second one. Let me try it again. Maybe memory was clogged up due to Cycles.

2:15pm. This time it crashed on just a single model.

Ok, I see...

Let me try loading Manhattan next.

2:20pm. Er, will it even load?

2:40pm. I played around with this. Even without textures, these are good assets.

~* Check out the Neo City kit. ~
~* Study procedural road construction in Houdini.~
    ~* In preparation for this, downlaod the Houdini version of the Neo City kit.~
* Check out the Scatter addon.
~* Check out the Manhattan kit.~

I've checked out the kits and the road construction.

...I won't download any more of them for the time being. These two should be enough.

* Check out the Scatter addon.

What I should do next is play with this for a bit.

2:50pm. I really wanted a lot bigger buildings, but I suppose these will be large enough. As long as the floor is not seen, it won't be obvious whether the number of floors is 100 or 1,000.

...Ok, I need a tutorial on how Scatter works.

What I need to do here is not complicated. Now that I've seen these buildings as references, I understand that I could model them myself in Moi. Not that I want to spend my time doing that. Houdini wouldn't be a good choice for them after all.

To get the assets for the scene, all I need to do is replace these empty textures with flats. After that I just have to scatter them. To get the night windows, I'll just randomize the emmission texture using face ids.

These guys put so much effort into texturing, but style transfer would eradicate most of that anyway. It does no good if I can barely load the scene as they are.

For terrain, if I need it in the future I can just doodle something on the plane. It is no big deal.

Let me take a short nap. I am feeling a lot of intertia here. The plan is certainly starting to come together. I just need to grasp it.

4:45pm. Eventually I'll get tired of napping. It is really hard to maintain your motivation, and a brainstorming session is just as one needs. I've had time to think about it.

First of all, let me conclude whether doing this scene in Blender is viable at all. The buildings themselves aren't too much in isolation, but Blender really starts choking after the polycount gose above 10m.

https://youtu.be/8BQatuJY_QY?t=43

Here it is working on buildings.

Regarding roads, I've decided. The true solution to dealing with roads is to just get a road tool. Even though the building one is half baked, the road one should be good, and it is the solution to all my inner conflict. If I look around no doubt I'll find an addon for it in Blender. I do not need whole cities. I just need to master the roads and the buildings will take care of themselves.

4:55pm. Ah, right. Didn't that guy say that Scatter 5 had a very extensive documentation. Where is it?

Right now I am feeling depressed, so I am more pressimistic than I should be.

https://youtu.be/HYkMd6FX8jM?t=527

Here is the tutorial. The link starts here.

https://youtu.be/HYkMd6FX8jM?t=546

This will also demo the asset browser. I think it has been about time that I get a handle on it.

Actually, let me go at it from the start.

https://youtu.be/HYkMd6FX8jM?t=50

I don't know, but this is a lot of high poly trees. Could Blender even handle something like that?

https://youtu.be/HYkMd6FX8jM?t=79
> You can create such terrain very easily in blender with the sculpt mode.

Ok.

https://youtu.be/HYkMd6FX8jM?t=164
> 3d Warehouse.

https://youtu.be/HYkMd6FX8jM?t=198

Horrible topology.

I thought that Sketchup was a CAD tool.

https://youtu.be/HYkMd6FX8jM?t=344

I did not know you could do triplanar like this.

https://youtu.be/HYkMd6FX8jM?t=382

So you can do it like this. Another technique I had no idea about.

https://youtu.be/HYkMd6FX8jM?t=401

Hmmm, he is using a cylinder to get a volume.

https://youtu.be/HYkMd6FX8jM?t=458

He says that Gaffer would give me access to every HDRI of Polyhaven for free.

Physical Startlight and Atmosphere is another he recommends.

https://youtu.be/HYkMd6FX8jM?t=642

Here he is starting. Let me watch him put some basic things down and then I'll figure out how to get this to work.

https://youtu.be/HYkMd6FX8jM?t=726

He makes a note that trying to display too many polys in the rasterized display can freeze Blender.

The key word seems to be rasterized.

It there something about ray tracing that makes it easier?

https://youtu.be/HYkMd6FX8jM?t=796

I feel that this has a lot of educational value beyond simply the

https://youtu.be/HYkMd6FX8jM?t=895

Let me pause here. I can't take this anymore. Let me open Manhatatn, move a few models to the Big collection. Then I will import that in another file. Then I will use particles to distribute the buildings.

5:40pm. I have a problem. I can barely work with these assets.

5:45pm. Yeah, I can barely work with this. I am trying to add a plan to the scene and it is taking 30s. If I click to select an object it requires several seconds to respond.

Even if I set the bounding box as the display in the viewport, that does me no good. I need to reconsider my plan. Right now these assets are almost useless.

https://blender.community/c/rightclickselect/brcbbc/?sorting=hot
Performance with high poly count and large numbers of objects

* Scenes with many objects have issues with undos taking a long time. Object level selections can be slow.
* A single object with many polygons has another set of issues. Edit mode sections can be slow while undo at this level can also be slow. In general, any operation at the edit level is slow with high poly objects. Sculpt is relatively fast with highly detailed objects (faster than Mudbox for example) but edit mode can approach the point of being unusable with the lag involved.

6:05pm. I am thinking of trying out the decimate modifier on this during the viewport, but disabling it during render. Would it be possible to just put it on all the objects? If I could reduce the poly count it would really streamline the process.

Ok, let me try it. I'll install hops.

Nope. Indeed it can put a Decimate modifier on multiple selected objects, but I can't change them as a batch after that. Useless.

Yeah, I am stuck on this. It does me no good to have these assets right now.

I have two choice, either export these objects by hand each into Clarisse, or find a way to pare them down automatically. It is possible that the Scatter plugin might have something for this.

I hate 3d again. Maybe I made a mistake. Maybe I should be inpainting and telling the NN what to do.

6:25pm. https://www.reddit.com/r/blender/comments/2xhz41/how_would_i_improve_performance_on_highpoly_models/

6:30pm. https://youtu.be/B79bGW7F8N0
106 833 296 polygons in Blender. Handling huge scenes. EP17

Let me watch this.

https://youtu.be/B79bGW7F8N0?t=5
> Blender Bob here, now please stop freaking out about the amount of polygons in your scene. It is not going to impact the rendering. Or its going to make a very little impact.

https://youtu.be/B79bGW7F8N0?t=68
> It took 30s to make the instance copy.

https://youtu.be/B79bGW7F8N0?t=94

I wonder how he is displaying the GPU memory.

https://youtu.be/B79bGW7F8N0?t=302
> We made the scene completely transparent - no impact. We made it completely metallic - no impact. We threw a 37 by 11k texture on it - no impact.

https://youtu.be/B79bGW7F8N0?t=346

I tried this, but it still kept taking forever to select for some reason.

https://youtu.be/B79bGW7F8N0?t=413

Ok, I had no idea Cycles was this good at using memory.

https://youtu.be/B79bGW7F8N0?t=427
> I am going to fast forward here because it takes 45s just to change one of them.

https://youtu.be/B79bGW7F8N0?t=449
> Proxy2s

Yes, this is what I need! I was just wondering about proxies. I thought about it, but I had no idea how it was possible. Maybe I should have just goggled it.

https://youtu.be/B79bGW7F8N0?t=550
> Ok, so now we found a way display very heavy geometry in Blender and its manageable, everything is referenced the file is very light. The problem is, all the geometry is loaded into memory. Is there a way to go around this? Not in Blender.

Edit: I am going to go with Clarisse because of this.

https://youtu.be/B79bGW7F8N0?t=733
> Just to give you an idea, when I was working at Atomic Fiction, we worked on Robert Immacus' Welcome to Marwen. Some of the scenes needed machines with 380 gigs of RAM to render a single frame.
> At one point we needed 44,000 CPUs to render the teaser in time. And we are not talking about Marvel's end game here. We are talking about Barbie dolls.

6:55pm. https://youtu.be/QlzxfrvpYv8
If only I had Blender when I worked on Pacific Rim Uprising. EP3

Let me watch this. I have no choice here. This is such a natural spot to make use of Clarisse. I guess it is finally its time to shine. I meant to do something with the Scatter addon, and I have some interest in studying it, but if I am going to be kitbashing I'll be dealing with heavy geometry on a regular basis. I can only use something other than Blender for it.

This is why I spent all this time studying Clarrise. I am going to have to take some time to export all of this as obj. I am going to try two separate objects first and see where that gets me.

https://youtu.be/QlzxfrvpYv8?t=51
> 4b particles were used for the water simulation and that does not even include the white water. It's insaane.

https://youtu.be/QlzxfrvpYv8?t=241
> By the way when you have geometry like this that is repeated many times you only need seven versions to make sure that you won't see a pattern.

I was wondering about the number. I guess 7 sounds plausinble. I knew that 3-4 would be too little, but I wasn't sure how high it would be necessary to go.

> For example for trees if you make a forest you only need 7 trees of the same species at different scales and different rotations. Nobody will be able to tell that they are the same one repeating again and again and again

https://youtu.be/QlzxfrvpYv8?t=313

Why is he doing UV unwrapping in such a complicated manner? It boggles my mind. What is wrong with just placing some seams?

https://youtu.be/QlzxfrvpYv8?t=351
> It was actually much more complicated than that because we had two layers of wood, the first one on top and then vertical beams, then we had a slab of concrete, then we had a passageway under made of wood and metal and pipes and electic cables, and at the end we don't see any of this.

https://youtu.be/QlzxfrvpYv8?t=365
> I also modeled this building, and its full of details and we don't see any of it.

Nice.

7:45pm. Tomorrow I'll export the models from the blend file one by one and import them into Clarisse. Then I am going to spread it around and finally do the scene. Just how long am I going to be stuck on this shit? I want to get a move on. Had I bothered modeling a bunch of buildings in Moi, and put in the flats by hand, I would have been done by now.

I am going to learn my lesson from this. I should have just opened Moi and gotten cracking on replicating a few refs. But since I have these kits I might as well go with Clarisse. They'll probably be useful for more local street views as well.

Let me put a link in the /blend/ thread as the video by Bob was pretty interesting.

8:05pm. I really wasn't motivated to model the buildings myself before experiencing procedural generation and kitbashing, but now I am. I guess 3d is not a silver bullet by any means.

...30 days remaining in the Moi trial. I am going to try reinstalling it once it runs out if I want to use Moi again.

...According to a thread on the rutracker forum, I just need to replace the dll using the cracked version.

It worked! I already had a cracked version on my PC, but did not want to use it as it was a beta v4 rather than the most recent one.

8:15pm. I am going to close here.

Being in the situation I am in for over half a week now put me in a very passive state which is not enjoyable. I want to say that I should have modeled in Moi, but not really. I have to try kitbashing at least once in my life. There was no avoiding this.

I also had to study procedural generation. So SceneCity is not that appealing, but if I had my own buildings I could have used the Scatter addon to spread them around ontop of the terrain given to me by SC. According to the rule of 7s, I only have to do 7 different versions, which would not have been hard. If they were in the 10-50k range, I could easily borne such an expense. The reason why Blender is giving me trouble is because each of the modles is over a million.

Tomorrow I am going to put my foot down and just get into it. I'll grind away at it step by until I am done with the scene. For the past 4 days I've only been learning, but not making any tangible progress on the scene. I should be done with this kind of scene in 1-2 days flat. Let's see if I can manage that from a better starting point."

---
## [Salex08/Merchant-Station-13](https://github.com/Salex08/Merchant-Station-13)@[33027699b9...](https://github.com/Salex08/Merchant-Station-13/commit/33027699b9b12d2a5be75965dd1c985194abf14c)
#### Friday 2022-06-17 19:10:34 by EtraIV

Fixes escaping the DM(I hope) Part 2: Fuck you Lunaman edition (#283)

* Fixed the hole in the wall on maint mania

* Why did you add a window here lol

---
## [R4EESY/Rhucarbarian-main](https://github.com/R4EESY/Rhucarbarian-main)@[dc3baf2488...](https://github.com/R4EESY/Rhucarbarian-main/commit/dc3baf248848b6d63a3af346f422e5cd0469768a)
#### Friday 2022-06-17 20:08:06 by raees ellam

FUCKING FINISHED NO LIGHTS SORRY

WEBGL BUILD DONE COLOR SHITE GOT CHANGED AND LIGHTS WERENT ADDED SORRY TYLER i want to top my self!!

---
## [wermuthj/Modul291](https://github.com/wermuthj/Modul291)@[20851697bb...](https://github.com/wermuthj/Modul291/commit/20851697bbee54b0df97d5b3cfbb24024102ce8f)
#### Friday 2022-06-17 20:55:40 by FynnS-bot

fuck this shit, validation söt jetzt finnyl gah gröschti scheiss pain gsie

---
## [newstools/2022-information-nigeria](https://github.com/newstools/2022-information-nigeria)@[689573285c...](https://github.com/newstools/2022-information-nigeria/commit/689573285c382ab961aad89f07bd81631544c2a4)
#### Friday 2022-06-17 22:02:32 by Billy Einkamerer

Created Text For URL [www.informationng.com/2022/06/mc-oluomo-calls-ex-girlfriend-lovely-woman-on-her-birthday.html]

---
## [obsproject/cef](https://github.com/obsproject/cef)@[90e55e8dc8...](https://github.com/obsproject/cef/commit/90e55e8dc8f8947cd83616d1973962c157071e86)
#### Friday 2022-06-17 22:12:10 by Jim

Legendary 4638 shared texture perf improvement

This fixes remaining performance and frame pacing issues when using CEF
95 with texture sharing on Windows. I hacked Chromium internally to
treat shared textures similarly to how the 3770 method worked.

Let me document my little adventure.

First, we were getting system freezes, and from analysis of the
bluescreen dumps, they were always during synchronization, so I had a
hunch: "are keyed mutexes doing this?" The system freeze issue left me
hopeless. I already had a disdain for the stupid keyed mutexes, and due
to my immense hatred of them, I was angry and I just wanted to try
removing them, because 1.) What if they were the cause? (They were), and
2.) I hated them anyway. It was an irrational vendetta, and I was on a
war path to remove them just in the *slightest* chance that those god
forsaken keyed mutexes were the cause.

So I got angry and decided to remove them from almost everything in
Chromium just to see if it would fix the system freeze issue. I removed
their usage from almost everything in Chromium related to GLImageDXGI.

Let me go on a rant about keyed mutexes. I hate keyed mutexes. I *want*
synchronization between devices, but what I *don't* want is to be forced
to swap stupid "keys" between the two devices; especially if you're in a
situation where you cannot pass the next key value to the next device so
the next device knows what key to use, because then, the original device
can no longer lock the object anymore, and the object is completely
forfeit. Then you get suck in a situation where you're forced to wait
infinitely if you have no way of telling the other device to use the
correct key. I wish I could suggest a better design, but all I know is
that I hate it, it's an insufferable design as it is right now, and I
don't think there's a single human being on the planet who will ever
convince me otherwise. Absolutely insufferable design. I've always hated
them and always will.

Anyway, sorry about that. Like I was saying, I removed keyed mutex usage
from texture sharing inside chromium. But the problem is that with the
4638 version of shared textures, it was about 5 textures which were used
round-robin. Because we were forced to remove keyed mutexes (which were
crashing the entire system), we could no longer synchronize between
client and Chromium, thus frame pacing issues were introduced. Even
flushing wasn't helping. They weren't noticeable, and we were *almost*
just going to use it as it, but I decided I wasn't finished with my war
path.

I had fixed the system freeze issue by removing keyed mutexes, but now
there was this frame pacing issue. So, I was upset, and I tried many
different techniques to try to synchronize. Flushing, more textures,
less textures, trying to adjust timing; I thought it was hopeless, until
I started looking at the 3770 version and started looking around
4638 code for ways I could do the same thing. I had already removed
keyed mutex objects from GLImageDXGI objects, but then I realized: what
if I just add the same staging/CopyResource method 3770 did, and then
just use one shared texture? 3770 worked amazingly well, so why not try
it? Through much toil and experimentation, I got it working.

However, there was still one annoying caveat. Because of the fact that
Chromium now only deals with NT-style HANDLE objects for shared
textures, it would duplicate handles every time it was passed. There was
no way of detecting whether we were already using the same shared
texture (and CompareObjectHandles in KernelBase didn't work), so we had
to recreate the stupid texture object every time. So I introduced a new
OnAcceleratedPaint2 function specifically to specify whether the texture
has been changed -- that way we don't need to have to continually keep
recreating the god-forsaken texture object.

All these things combined has won us a huge victory, not only did we
solve the system freeze issue, but we also reduced the amount of
resources being used from the original version by removing the round
robin, eliminated frame pacing issues, and improved the perf back to
3770 levels. In fact, I'm pretty sure that perf levels are even better
than they were even with the keyed mutex version (if they weren't
causing stupid system freezes), because the keyed mutex version forced
INFINITE lock durations due to the inability to relay keys.

After 27.2 had this issue, I had to delay the release, and I spent a
week toiling over this. To get the system freeze issue fixed, and then
to get perf levels back to 3770 levels. And I did it by sifting through
millions of lines of Chromium code.

Needless to say I feel really damn good right now. This was a legendary
fix. I'm sorry, I need a little bit of ego just for once. I feel like
I've earned it.

---

