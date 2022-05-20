## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-19](docs/good-messages/2022/2022-05-19.md)


1,707,591 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,707,591 were push events containing 2,756,346 commit messages that amount to 195,887,972 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [mengzhisuoliu/terminal](https://github.com/mengzhisuoliu/terminal)@[77215d9d77...](https://github.com/mengzhisuoliu/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Thursday 2022-05-19 00:23:30 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[46200d89ae...](https://github.com/cyberitsolutions/bootstrap2020/commit/46200d89aee3f4cdd5e761ca80e9bb2b50f9a3ba)
#### Thursday 2022-05-19 00:35:46 by Trent W. Buck

dvdrip: remove needless timestamp

16:13 <twb> self.dvd_title = f'{self.dvd_title or "Unknown"} {datetime.datetime.today()}'
16:13 <twb> That should be date.today(), but I want to remove it completely
16:13 <twb> the tvserver adds another timestamp, so I don't think it's needed
16:14 <twb> REDACTED: any opinion?
16:14 <REDACTED> Hmmm, I think the timestamp should be added as soon as possible to avoid 2 rip jobs trampling on each other
16:14 <twb> REDACTED: it's already using temp dirs.
16:15 <twb> It just means that if two staff have the *same* disc, and try to rip *both* discs on the same day, the second one will go "oh, it already exists in the .ripped queue" and (now) cleanup after itself
16:16 <REDACTED> If we're reliably handling errors, then yeah fine, it can go, I think. Because realistically they'll be the same regardless of date ripped. But make sure you're not overwriting things without checking
16:16 <twb> Whereas what happens at AMC is they end up re-rippign the same dvd 11 fuckign times
16:16 <REDACTED> Ok, cleanup itself is the important part
16:16 <twb> Yeah
16:16 <twb> Anyway the desktop side of this I'll check today incidentally as part of this

---
## [Sirryan2002/Paradise](https://github.com/Sirryan2002/Paradise)@[6082c95eb3...](https://github.com/Sirryan2002/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Thursday 2022-05-19 01:08:50 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [yuzefovich/cockroach](https://github.com/yuzefovich/cockroach)@[88b245aa46...](https://github.com/yuzefovich/cockroach/commit/88b245aa469ee6302a25d3ac4cbe58b23927831d)
#### Thursday 2022-05-19 01:49:52 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here]
(https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox]
(https://ant.design/docs/react/getting-started) (render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox]
(https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here]
(https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

---
## [angie1148/luci-go](https://github.com/angie1148/luci-go)@[7271a1c01b...](https://github.com/angie1148/luci-go/commit/7271a1c01baa3a9448fdd24d8964c134933dbd6f)
#### Thursday 2022-05-19 03:36:43 by Vadim Shtayura

[gae] Make go.chromium.org/luci/gae work on go116 GAE.

It is a horrible hack. "google.golang.org/appengine" appears to be
mostly working on go116 GAE, except logging is broken. But luci/gae
wraps logging and we can implement it using GAE v2 method (structured
logging to stdout).

The only wrinkle in this plan is that the appengine library still
calls logservice.Flush RPC, even if there's no logs to flush (and
this fails and emits noise in stderr).

But there's an unreleased (!) 1.5y old commit in
github.com/golang/appengine that provides an undocumented way to
disable logging done by the library. We rely on it now by fetching
appengine module via git hash instead of a released version number.

To use this hack, the service should have the following in app.yaml:

  runtime: go116
  app_engine_apis: true

Q: Why not switch to google.golang.org/appengine/v2 (which
essentially does the same thing as this commit, just a layer
lower)?

A: To ease the migration. Due to how Go modules work, v2 is
a completely separate package. Unless we switch all code base (and
all dependencies) to v2 in a single commit, there'll be a possibility
of both v1 and v2 libraries linked into a single binary. Since both
of them register the same protobuf messages, it causes panics during
startup due to name conflicts in the proto registry:
https://github.com/golang/appengine/issues/281 All services will have
to be switch to go116 at once, otherwise they'll likely panic during
startup. With this hack, the exact same codebase works on both go111
and go116 and there are no panics. Individual services can switch to
go116 at their own pace after core libraries have switched.

Q: So once all go111 apps switch to go116 using this hack, we are
done with GAE migrations and can live happily ever after?

A: No, this is a fragile hack and a dead end. Code that relies on it
will not be getting any real support (i.e. new features) and very
likely will break at some point. LUCI services should still migrate
to Google Cloud APIs and go.chromium.org/luci/server framework.

Q: If it is such a horrible hack, and there's a better approach, why
are we doing it?

A: It is becoming extremely difficult to maintain buildability of
shared luci-go code on go111 for GAE. Many fundamental libraries
(like gRPC) deprecated go111 support loooong time ago, and we have
to resort to pinning dependencies to prehistoric versions. With more
and more libraries removing go111 compatibility, it is getting harder
and harder to maintain pinned dependencies. At this point it is less
frustrating to maintain an abominable "appengine v1 library on top
of go116 runtime with hacks" than try to keep go111 compatibility.

R=iannucci@chromium.org

Change-Id: Id2a8daf85d30efc4b82f4d177b1639b5a1d1894a
Reviewed-on: https://chromium-review.googlesource.com/c/infra/luci/luci-go/+/3651087
Reviewed-by: Robbie Iannucci <iannucci@chromium.org>
Commit-Queue: Vadim Shtayura <vadimsh@chromium.org>

---
## [CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA)@[02ff2c953f...](https://github.com/CleverRaven/Cataclysm-DDA/commit/02ff2c953f5dacab37f1a374271d352c01ebcfea)
#### Thursday 2022-05-19 03:39:19 by casswedson

fix: default issue template labels (#57792)

Well then, let me elaborate on why this didn't work on the first try, and
why it was so hard to spot the problem, then again like 3 people looked
at this: a case typo, that's it

just like a lot of things in life the label to issue template feature is
picky and won't tell you all of its secrets, you gotta lean by bashing
your head against it until you learn or die

Starting with why I was confident this worked in the initial pr:

in a test repo I have I use "(S1 - Need Confirmation)" as a label, the
config in that repo looks for a label with that casing so it works
no problem, cdda differs by one letter however
`labels: ["(S1 - Need Confirmation)"]` for the config in both repos specifically
here try it yourself, try the bug report template in this repo
https://github.com/casswedson/issue-labeling/issues/new/choose

The mistake:

in *this* repo the casing of "confirmation" in the S1 label is just lowercase
all the way down the word, makes all the difference I tell ya

in any case #57534 had a typo in it that made it not work 100% this fixes it by
doing the following:
change
`labels: ["(S1 - Need Confirmation)"]`
to
`labels: ["(S1 - Need confirmation)"]`

This reverts commit 7894b1e4a4dba375e4ac9260b9569eca8657aa24.
plus a little edit

sorry for the big wall of text explaining a typo fix, I want to make
sure I and everyone else understands how stupid of me was missing that
simple thing
good thing not a lot of people noticed and it's no big deal, right?

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[f6ce903dea...](https://github.com/OrionTheFox/Skyrat-tg/commit/f6ce903deade160357e23b927d376851f0dbdd2c)
#### Thursday 2022-05-19 04:11:06 by SkyratBot

[MIRROR] Makes glass floors override platings. Fixes glass floor openspace bug. [MDB IGNORE] (#13226)

* Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)

About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

* Makes glass floors override platings. Fixes glass floor openspace bug.

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [sthagen/facebook-pyre-check](https://github.com/sthagen/facebook-pyre-check)@[fbd33d0b85...](https://github.com/sthagen/facebook-pyre-check/commit/fbd33d0b8570c69957213b943255bba2c3c74285)
#### Thursday 2022-05-19 04:26:21 by Shannon Zhu

Split find references for local and global names

Summary:
We probably can't support find all references with a table lookup, because we need to be able to handle requests on any name - not just function calls, and not just at the point of definition.

For example,

```
1: def foo() -> None:
2:    x = 1
3:    y = x
4:
5: def bar() -> None:
6:    foo()
7:
8: def baz() -> None:
9:    foo()
```

In this case, we'd need to be able to ask for "find all references" on `foo` on line 9, and return the `foo`s on lines 1 and 6. We need to be able to ask for "find all references" on `x` in line 2 and return the `x` on line 3.

Essentially, if we represented this as a mapping from reference -> list of references, every single reference in the list would also need its own entry to refer back to the rest of the group; so this isn't just a reverse callgraph lookup.

Given that we also need to support this for essentially every valid name: functions, attributes, globals, local values, class names, module names, etc., I think the only way to implement this is to take Hack's approach of tweaking the name of the reference in question, and then re-asking the type checker to calculate undefined name errors and converting those errors into reference locations.

In cases where we're asking for references of a name that is in the global scope, this starts to look a lot like unsaved changes overlays with a few exceptions (cc stroxler):

- Unsaved changes can be filtered down to only a module in question to prevent fan-out and keep things performant, also limit the memory footprint of writing overlay keys to all of the dependency tables. For find-all-references, we /need/ the fan-out and don't mind the perf hit, but this means we will need to make adjustments to make sure we aren't blowing up memory if we do many find-all-references checks in a row on the same server.
- To clean up the memory footprint, we'll either need to pay a heavy performance cost of remembering the last overlaid change and reverting it when applying the new overlaid change (I don't think this makes sense, since perf costs are highly variable depending on the name we pass in), or implementing a clean-up/sweep functionality that goes through shared memory tables and uses the dependency graph to delete keys written by the overlay check when we are done.
- We'll want to block writes to the dependency graph and just rely on the "logical" key to propagate our changes and propagate the cleanup.
- We'll need a transform visitor to figure out the right place to make the AST renaming change to kick off the incremental check.

In cases where we're asking for references of a name that is only in a local scope, we don't have to care about the environment at all - just take the relevant define body, make an adjustment to make sure the line defining the reference doesn't register or is modified, and then run an uninitialized local analysis on that one define and convert the errors to reference locations.

I'll tackle the local portion first before diving into the overlay/environment dependency changes needed to support this globally.

Note that: performance is likely not a concern here at all. find-all-references in Hack will load for minutes if you invoke it on some standard library function or basic class that is used all over the repository, as it should. Find all references should behave, performance wise, identically to a type check when the thing is changed. Also fun fact that pylance's find all references is also very slow and anecdotally seems quite flaky/often incorrect. I could not get a find all references request working at all in the current jedi setup.

Reviewed By: stroxler

Differential Revision: D35629810

fbshipit-source-id: 4761013b68a1389287731f9b9ac36fc749defcf3

---
## [SamriddhiKaul/EndTerm](https://github.com/SamriddhiKaul/EndTerm)@[13b471046d...](https://github.com/SamriddhiKaul/EndTerm/commit/13b471046d6dcda35deb4aaf1a0b417314bfca32)
#### Thursday 2022-05-19 04:48:50 by samriddhi/18

[200~<! DOCTYPE html >
<html>
<head>
<title>Assignment
</title>
</head >
<body>
<table border="1">
<caption><h1>Practice Table</h1></caption>
<tr>
<td>
<table border="1">
<tr>
<td><img
src="https://www.gardendesign.com/pictures/images/675x529Max/site_3/helianthus-yellow-flower-pixabay_11863.jpg"
height="100%"
width="100%"</td>
<td><img
src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/close-up-of-tulips-blooming-in-field-royalty-free-image-1584131603.jpg"
height="40%"
width="30%"</td>
</tr>
<tr>
<td><img
src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7DSG6qgN7-BNccysyV5QZxMXsMJngt_8gqOyj4yCo1YEy068ilZm5xVFO1w6TYzJ3cUI&usqp=CAU"
height="100%"
width="100%"</td>
<td><img src="https://imgcdn.floweraura.com/FA-12-CCC.jpg"
height="40%"
width="30%"
</td>
</tr>
</table>
</td>
<td>
<table border="1">
<tr>
<td>
<div style="background-color:yellow">
<a
href="https://www.goodhousekeeping.com/holidays/mothers-day/g5187/mothers-day-flowers/">Cakes</a>
</div>
</td>
<td>
<div style="background-color:green;">
<a
href="https://www.bigbasket.com/pc/snacks-branded-foods/chocolates-candies/">Chocolates</a>
</div>
</td>
</tr>
<tr>
<td>
<div style="background-color:pink">
<a
href="https://kcroasters.com/?gclid=Cj0KCQiAtJeNBhCVARIsANJUJ2FeqyPNlnfX7Uko3x1aOD-EBQKAZVTUXEQOhp2SZwNcC-LmSUV1rIcaAgXUEALw_wcB">Coffee</a>
</div>
</td>
<td>
<div style="background-color:orange;">
<a
href="https://www.hungryhowies.com/?gclid=Cj0KCQiAtJeNBhCVARIsANJUJ2HtETR7XD84Tb-_vS78w-le6TWGrlqJMS_tEB3XCRAUDaQrsLc3suIaAu0GEALw_wcB&gclsrc=aw.ds">Pizza</a>
</div>
</td>
</tr>
</table></td>
</tr>
<tr>
<td>
<table border="1">
<p><div style="background-color:black;color:white;">
Sunset, also known as sundown, is the daily disappearance of the Sun
below the horizon due to Earth's rotation. As viewed from everywhere on
Earth (except the North and South poles), the equinox Sun sets due west
at the moment of both the Spring and Autumn equinox. As viewed from the
Northern Hemisphere, the sun sets to the northwest (or not at all) in
the Northern hemisphere's spring and summer, and to the southwest in the
autumn and winter; these seasons are reversed for the Southern
Hemisphere.

The time of sunset is defined in astronomy as the moment when the upper
limb of the Sun disappears below the horizon.[1] Near the horizon,
atmospheric refraction causes sunlight rays to be distorted to such an
extent that geometrically the solar disk is already about one diameter
below the horizon when a sunset is observed.

Sunset is distinct from twilight, which is divided into three stages.
The first one is civil twilight, which begins once the Sun has
disappeared below the horizon, and continues until it descends to 6
degrees below the horizon. The second phase is nautical twilight,
between 6 and 12 degrees below the horizon. As for the third one, it is
astronomical twilight, which is the period when the Sun is between 12
and 18 degrees below the horizon.[2] Dusk is at the very end of
astronomical twilight, and is the darkest moment of twilight just before
night.[3] Finally, night occurs when the Sun reaches 18 degrees below
the horizon and no longer illuminates the sky.
</div>
</P>
</table>
</td>
<td>
<table border="1">
<p>
<div
style="background-image:url('https://royalpepper.in/blog/wp-content/uploads/2021/08/f1c1c93f3f0266e714d071a5f9ba273802ba7c64.jpg');"
height="50%"
width="50%">
India, officially the Republic of India (Hindi: Bhārat Gaṇarājya),[23]
is a country in South Asia.
It is the seventh-largest country by area, the second-most populous
country, and the most populous democracy in the world.
Bounded by the Indian Ocean on the south, the Arabian Sea on the
southwest, and the Bay of Bengal on the southeast, it shares land
borders with Pakistan to
 the west;[f] China, Nepal, and Bhutan to the north; and Bangladesh and
 Myanmar to the east.
 In the Indian Ocean, India is in the vicinity of Sri Lanka and the
 Maldives; its Andaman and Nicobar Islands share a maritime border with
 Thailand, Myanmar and Indonesia.
 Modern humans arrived on the Indian subcontinent from Africa no later
 than 55,000 years ago.[24] Their long occupation, initially in varying
 forms of isolation as hunter-gatherers, has made the region highly
 diverse, second only to Africa in human genetic diversity.[25] Settled
 life emerged on the subcontinent in the western margins of the Indus
 river basin 9,000 years ago, evolving gradually into the Indus Valley
 Civilisation of the third millennium BCE.[26] By 1200 BCE, an archaic
 form of Sanskrit, an Indo-European language, had diffused into India
 from the northwest,[27] unfolding as the language of the Rigveda, and
 recording the dawning of Hinduism in India.[28] The Dravidian languages
 of India were supplanted in the northern and western regions.[29] By
 400 BCE, stratification and exclusion by caste had emerged within
     Hinduism,[30] and Buddhism and Jainism had arisen, proclaiming
     social orders unlinked to heredity.[31] Early political
     consolidations gave rise to the loose-knit Maurya and Gupta Empires
     based in the Ganges Basin.[32] Their collective era was suffused
     with wide-ranging creativity,[33] but also marked by the declining
     status of women,[34] and the incorporation of untouchability into
     an organised system of belief.[g][35] In South India, the Middle
     kingdoms exported Dravidian-languages scripts and religious
     cultures to the kingdoms of Southeast Asia.
     </div>
     </p>
     </table>
     </td>
     </table>

     </body>
     </html>

---
## [DarkKnight2019/crawl](https://github.com/DarkKnight2019/crawl)@[c08b2e8bf8...](https://github.com/DarkKnight2019/crawl/commit/c08b2e8bf8864494d43077b7622612e4c5b192df)
#### Thursday 2022-05-19 05:45:30 by nicolae-carpathia

Add the most nicolae demonic rune vault possible (#2260)

* Add the most nicolae demonic rune vault possible

I have reached my apotheosis: I have put a rune in a shop.

Since the demonic rune repeats if you don't pick it up, I figured it
would be the best option for a rune shop. (The abyssal rune also
reappears if you don't pick it up, but the theme is easier to fit into
Pandemonium.) If you already have the rune, the shop instead places
another kind of rarity: a figurine of a ziggurat. (The only other
really rare item I could think of was a quad damage, and I've been
explicitly told multiple times that I'm not allowed to use those
outside of Sprint. Tyranny!)

Out of 25 generated shops, the stats on the price of a demonic rune:
Minimum: 3804
Maximum: 8647
Average: 6640.76
St Dev:  1412.1
I didn't check the price stats on the zigfig because the rune is the
real draw here.

The vault also places fat stacks of cash, three other shops, and
demon-summoning monsters from other branches as visitors. Enjoy!

* Make adjustments to the pan bazaar rune vault

Make some changes based on feedback from the other devs:
1) If you already have the demonic rune, instead of selling a
   zigfig, the central shop now just sells randarts. (I had
   underestimated the importance of zigfigs.)
2) The difficulty has been turned up a bit. The area outside
   the central area places more monsters now.
3) A few of the nonruniferous shops have been tweaked.

---
## [NaokoAF/kiwi](https://github.com/NaokoAF/kiwi)@[54ed4f4d14...](https://github.com/NaokoAF/kiwi/commit/54ed4f4d1487122dc739a5a3ce6165205911818d)
#### Thursday 2022-05-19 06:14:03 by NaokoAF

Update a lot of things

im sorry i just cant bother to do this git thing properly ok

this shit is incredibly annoying to work with sometimes so fuck it

---
## [Sunflair0/cash-grab](https://github.com/Sunflair0/cash-grab)@[caccf2c96f...](https://github.com/Sunflair0/cash-grab/commit/caccf2c96fe9dbbe74ead5f1cd9fb4ea9fb0919f)
#### Thursday 2022-05-19 08:22:25 by Sunflair0

Create README.md

This is my take on a group assignment while attending Midlands Code Camp. We were instructed to create a whack-a-mole game. But, smacking all those moles made me sad, so I made my own verson where you are penalized for hitting those adorable buggers.
I added levels (I am very proud of the buttons), 4 lives, changed the graphics, added the cash and mole pop up options, the preview and action bar on the bottom, the scoreboard at the end; really, I changed everything except the mole pop ups.
I worked on this a long time because by the time I finished one module, I learned how to do another better and I re-did that. I got very familiar with Greensock and animations, used 3D Paint and Canva (for SVG conversion). In the end, I figured since I am a junior developer, it's ok to have the program a bit messy, because I am still learning. It also proves I wrote it myself!
I am aware that Lighthouse testing rates my speed low, and I am sorry. If you have suggestions for me, I am WIDE OPEN to constructive critism! Help me be a better coder.
I do hope you enjoy playing the game. Try it on all hardness levels, use up all the hearts and restart the game. My only regret is that I don't have a cute animation at the end when you pass the game. 
But, I may have one in the future! Stay tuned.

---
## [SweetBlueSylveon/Shiptest](https://github.com/SweetBlueSylveon/Shiptest)@[a012575b50...](https://github.com/SweetBlueSylveon/Shiptest/commit/a012575b5049c55cd75aef1f403ed2357534c85b)
#### Thursday 2022-05-19 08:26:17 by SweetBlueSylveon

I hate underdoor tiles

By god's light I smite you.
Fuck you underdoor walls.

---
## [veryyourmom/Wow-im-funny](https://github.com/veryyourmom/Wow-im-funny)@[26009fb0c9...](https://github.com/veryyourmom/Wow-im-funny/commit/26009fb0c955890ff490b08bcf29c0b9ecb38f8b)
#### Thursday 2022-05-19 08:33:24 by onetruegaming

Update .env

fuck you github im gonnag kill you someday

---
## [avar/git](https://github.com/avar/git)@[e793cfb65e...](https://github.com/avar/git/commit/e793cfb65ea00a88170d95b032d01806e8728f50)
#### Thursday 2022-05-19 08:40:31 by Ævar Arnfjörð Bjarmason

usage API: use C99 macros for {usage,usagef,die,error,warning,die}*()

Change the "usage" family of functions to be defined in terms of C99
variadic macros, as we've optionally done with the BUG() macro and
BUG_fl() function since d8193743e08 (usage.c: add BUG() function,
2017-05-12), and unconditionally since 765dc168882 (git-compat-util:
always enable variadic macros, 2021-01-28).

This would have been possible before having a hard dependency on C99,
but as the dual implementations of C99 and pre-C99 macros and
functions adjusted in preceding commits show, doing so would have been
rather painful.

By having these be macros we'll now log meaningful "file" and "line"
entries in trace2 events. Before this we'd log "usage.c" in all of
them, and the line would be the relevant locations in that file.

To do this we need to not only introduce X_fl() functions for
{die,error,warning,die}{,_errno}(), but also change all the callers of
the set_*() and get_() functions in usage.h to take "file" and "line"
arguments.

Neither the built-in {die,error,warning,die}{,_errno}() nor anyone
else does anything useful with these "file" and "line" arguments for
now, but it means we can define all our macros and functions
consistently.

It also opens the door for a follow-up change where these functions
could optionally emit the file name and line number, e.g. for
DEVELOPER=1 builds, or depending on configuration.

It might be a good change to remove the "fmt" key from the "error"
events as a follow-up change. As these few examples from running the
test suite show it's sometimes redundant (same as the "msg"), rather
useless (just a "%s"), or something we could now mostly aggregate by
file/line instead of the normalized printf format:

      1 file":"builtin/gc.c","line":1391,"msg":"'bogus' is not a valid task","fmt":"'%s' is not a valid task"}
      1 file":"builtin/for-each-ref.c","line":89,"msg":"format: %(then) atom used more than once","fmt":"%s"}
      1 file":"builtin/fast-import.c","line":411,"msg":"Garbage after mark: N :202 :302x","fmt":"Garbage after mark: %s"}

"Mostly" here assumes that it would be OK if the aggregation changed
between git versions, which may be what all users of trace2 want. The
change that introduced the "fmt" code was ee4512ed481 (trace2: create
new combined trace facility, 2019-02-22), and the documentation change
was e544221d97a (trace2: Documentation/technical/api-trace2.txt,
2019-02-22).

Both are rather vague on what problem "fmt" solved exactly, aside from
the obvious one of it being impossible to do meaningful aggregations
due to the "file" and "line" being the same everywhere, which isn't
the case now.

In any case, let's leave "fmt" be for now, the above summary was given
in case it's interesting to remove it in the future, e.g. to save
space in trace2 payloads.

The change here in git_die_config() is the bare minimum needed to get
it working, but better would be a change[1] to correctly report the
caller file and line numbers. Let's leave that for later, it can be
done later.

1. https://lore.kernel.org/git/patch-4.4-e0e6427cbd3-20211206T165221Z-avarab@gmail.com/#t

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[af451061da...](https://github.com/avar/git/commit/af451061da786c83cc66456bcf296fab78ac4687)
#### Thursday 2022-05-19 08:40:39 by Ævar Arnfjörð Bjarmason

usage API: make the "{usage,fatal,error,warning,BUG}: " translatable

In preceding commits the vreportf() function was made static, so we
know it's only being called with a limited set of fixed prefixes. Pass
an enum indicating the kind of usage message we're emitting instead,
which means that we can fold the BUG_vfl_common() functionality
directly into it.

Since we've now got one place were we're emitting these usage messages
we can make them translatable.

We need to be careful with this function to not malloc() anything, as
a failure in say a use of strbuf_vaddf() would call xmalloc(), which
would in turn call die(), but here we're using static strings, either
from libintl or not.

I was on the fence about making the "BUG: " message translatable, but
let's do it for consistency. Someone who doesn't speak a word of
English may not know what "BUG" means, but if it's translated they
might have an easier time knowing that they have to report a bug
upstream. Since we'll always emit the line number it's unlikely that
we're going to be confused by such a report.

As we've moved the BUG_vfl_common() code into vsnprintf() we can do
away with one of the two checks for buffer sizes added in
116d1fa6c69 (vreportf(): avoid relying on stdio buffering, 2019-10-30)
and ac4896f007a (fmt_with_err: add a comment that truncation is OK,
2018-05-18).

I.e. we're being overly paranoid if we define the fixed-size "prefix"
and "msg" buffers, are OK with the former being truncated, and then
effectively check if our 256-byte buffer is larger than our 4096-byte
buffer. I wondered about adding a:

    assert(sizeof(prefix) < sizeof(msg)); /* overly paranoid much? */

But I think that would be overdoing it. Anyone modifying this function
will keep these two buffer sizes in mind, so let's just remove one of
the checks instead.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[cbb6ace359...](https://github.com/avar/git/commit/cbb6ace359518ea3b14c2aea45d4ed2eca8d378d)
#### Thursday 2022-05-19 08:41:44 by Ævar Arnfjörð Bjarmason

usage API: add "core.usageAddSource" config to add <file>:<line>

Optionally extend the support that BUG() has had for emitting line
numbers to the {usage,fatal,error,warning}{,_errno}() functions.

Before we'd unconditionally get error messages like:

    $ git -c core.x=y config --get --bool core.x
    fatal: bad boolean config value 'y' for 'core.x'

Which can be changed with core.usageAddSource=true to include the file
and line numbers:

    $ git -c core.usageAddSource=true -c core.x=y config --get --bool core.x
    fatal: config.c:1241: bad boolean config value 'y' for 'core.x'

As the added documentation notes this is primarily intended to be
useful to developers of git itself, but is being exposed as a user
setting to e.g. help file better bug reports.

This also adds a "GIT_TEST_USAGE_ADD_SOURCE" setting intended to run
the test suite in this mode.

Currently it has a lot of failures. Most of those are rather trivial,
and can be "fixed" by pointing GIT_TEST_CMP to a "diff -u" that does a
s/^(usage|fatal|error|warning): [^:]+:[0-9]+/$1/g on its input files,
and likewise for a "grep" wrapper that does the same.

Even if we can't run the tests in this mode yet I'd like to have this
for ad-hoc debugging, and to make it easier to work towards running
the tests in this mode. If we can turn this on permanently it'll be
much easier to read test output, as we won't need to worry about the
indirection of looking up where an error might have been emitted,
which can be especially painful when the message being emitted isn't
unique within git.git.

This new code needs to be guarded by the "dying" variable for the
reasons explained in 2d3c02f5db6 (die(): stop hiding errors due to
overzealous recursion guard, 2017-06-21), and for those same reasons
it's racy under multi-threading.

Here the worst case is that incrementing the variable will run away
from us, and we won't get our desired <file>:<line> number. That's OK
in this case, those cases should be isolated to the config code (if we
can't parse the config), memory allocation etc, but we'll get it right
in the common cases.

Using GIT_TEST_USAGE_ADD_SOURCE should be immune from any racyness, as
it only needs a getenv() and git_parse_maybe_bool(), which won't die.

Add a repo_cfg_bool_env() wrapper to repo-settings.c for
GIT_TEST_USAGE_ADD_SOURCE, in 3050b6dfc75 (repo-settings.c: simplify
the setup, 2021-09-21) I indicated that the GIT_TEST_MULTI_PACK_INDEX
env variable/config pair in that file has odd semantics, but users of
repo_cfg_bool_env() have straightforward and expected semantics. If
the environment variable is set (true or false) we'll use it,
otherwise we'll use the config, and finally fall back on the
default (of "false", in this case).

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4a22b304e6...](https://github.com/mrakgr/The-Spiral-Language/commit/4a22b304e6f66563d254c80889b15255f754c307)
#### Thursday 2022-05-19 09:07:34 by Marko Grdinić

"9:10am. I've been thinking what my problem is when it comes to painting that bed. I've realized what my problems are. During the night, I've approached it as a drawing problem instead. What if I simply tried to do line art for this? Then I realized the truth. The creases are essentially noise patterns, so it is no wonder that I can't store them in memory and comprehend them. I knew that fundamentally the way I am approaching them is broken, just putting down some strokes and then bluring them out.

It simply doesn't make sense to me. And because the goals are so ambiguous I find it impossible to draw. The end result is as if I were just tossing mud at the screen. Yesterday when I finished I was happy for 10m until I reviewed and came to my senses.

Forget painting, and trying to shade the bed directly. I already know that is very hard. Instead what would be something that I could draw? As weak as my 2d skills are, I should be able to draw primitive shapes.

Since the bed is a 3d box, imagine if I scattered a bunch of cylinders over it and tried drawing that. Imagine trying to draw curved surfaces like the ones I've made in Moi.

Could I draw this curved surface, could I draw that curved surface? What is the problem, and what is my limit?

9:20am. If I focus on composing primitives while 2d drawing, I should be able to make progress. But instead I started off with shading, did not at all feel out the 3d shape of what I was painting and got completely lost.

9:25am. Somewhat ironically, this kind of approach of focusing on primitives would make 2d and 3d art quite similar, but that is good. That is how I would know I am on the right path when it comes to 2d. 2d should not be completely different from 3d.

9:30am. The painterly approach of trying to optimize the shades would work if I had a really good reference, but changing brightness so they match is fundamentally different from stroking out the iso-curves of various surfaces. I can't use the former approach to feel out the 3d space. Unless I have it to begin with I am going to get lost.

I lost the moment I flat shaded the planes of the bed. That is the part where I went wrong.

9:35pm. While programming I often write code and then think about how it fits in. There is only so much you can do by trying to think everything through from the beginning. The hand takes the office of the mind.

I absolutely have to make it so that this applies to 2d art as well. It certainly applies to 3d art where I am constantly moving things around.

9:35am. If I could learn how to manipulate primitives directly in 2d space, and learn how to draw curved surfaces, then I could move from the bottom of 2/5 to somewhere decent. The first step towards acquiring skill is to set sensible goals. There is absolutely no reason to be distressed over having bad memory and such.

If I can learn how to draw curved surfaces, then I can learn to compose them in a scene to get a good looking image. At point I can do the coloring and the shading. If I had the creases in the reference, I would not have failed at painting them.

9:40am. This all goes back to what I studied last year. Remember those Drawing Database vids where he spent all his time drawing primitives? I want to say I forgot the fundamentals, but I never really learned them to begin with. I sort of didn't see the point since I had 3d. Why practice drawing boxes directly when I could just import them?

And indeed, that is a good question - what was I even trying to do in the past couple of days?

Apparently, not use my brain, go somewhere I should not be, and get my ass kicked. I should learn from this experience. Forget trying to immitate those experienced painters who can do what they want from imagination directly. The loose approach is faster for them, but it won't be for me.

Tracing out that couch which I am still using as the wallpaper for my desktop only served to retard my progress.

9:55am. It is not that something like this has never happened in programming. I start writing code and then I find that I can't keep track of what I am doing in my head. The plan turns out to be convoluted and I become lost as to what it is I am doing.

10am. Right now I am thinking about my wins and losses.

I am thinking about the documentary of Inio Asano. I hadn't really thought about taking an image and leveling it out before putting in my own drawings.

Suppose I wanted to take such an approach.

If I just took a 3d photo as it is, then I'd have to match the level of detail on my own model. but if I grayscaled it and leveled it out, I would have to do a lot less work to make the model integrate with the background.

I mean, if I was doing it grayscale, I would not need to color or texture my model. I could just take the same approach as Pablo or use the Mangaka plugin to integrate it into the scene.

10:05am. His approach of using photographs would be viable whether I am using 2d or 3d.

So in fact, given that it saves me from directly modeling a lot of things, it would be a huge gain. I can always go into a grayscale image and paint it myself so it matches the simplified texturing of the model.

10:10am. I know deep down that if I want to get good results, it is not realistic of me to model literally everything from scratch.

I am going to have to learn to draw if only so I can retouch leveled-out photos and some painting so I can color those images back in.

10:20am. This brings me to the present situation. What is my plan?

I do not need to start grinding 2d. Doing more 3d modeling should be more than good enough. I mean, Moi and Zbrush will make me better at 2d drawing, than 2d ever will.

So I should really level up my modeling skills as much as possible.

For painting, I will check out the NPR stuff in Blender. No doubt I will be using a combination of that and hand painting in CSP. It won't be fancy at all.

10:40am. That huge and intricate spaceship Inio did? Since it is grayscale, he could have just painted that intricate machinery using black lines. Since the depth is leveled out, I'd naturally imagine it would be some huge and intricate 3d modeling job, but it could not be further from the truth.

This is real magic. It is natural to imagine great artists being very skilled, but no amount of skills will give those kinds of results.

10:50pm. Let me set the course to download.

10:55am. Yeah, the plan is simple. In order to be able to take a few steps forward, I am going to have to take a step back first. I spent time learning texturing, but that was going in the wrong direction. Somewhat ironically, the Designer stuff was in the right direction as it directly relates to compositing.

I am going to have to go to grayscale and then back to color. That is what I should aim for. It will make my art much easier to integrate with photo references.

For painting my models I am going to have to look into NPR. Maybe I won't need that and will opt to do my paint over directly in CSP. But it does not matter. Either way it is not a big deal.

11am. I can leave investigating NPR for later.

My current approach will place modeling front and center. This is just the way I like it. I did not want to do the rest all that much. I found texturing interesting, but only to a degree. I knew that I couldn't spare the time for it.

I won't get obsessed about NPR at this point. I'll just have faith that I'll deal with it when the time comes.

For now what I should focus is on finishing the room. I should imagine my intention is to draw it and then paint it as if I were doing 2d. Forget NPR, and forget everything else.

11:05am. Let me have breakfast here first. The night was a bit strained for me as I was obsessed about the painting failure. Right now I still feel groggy."

---
## [Urumasi/tgstation](https://github.com/Urumasi/tgstation)@[0504c0a2b4...](https://github.com/Urumasi/tgstation/commit/0504c0a2b466d617efd4dcc77b092fcdbdad24be)
#### Thursday 2022-05-19 09:08:10 by LemonInTheDark

Improper forced qdel cleanup,  some expanded del all verbs (#66595)

* Removes all supurfolus uses of QDEL_HINT_LETMELIVE

This define exists to allow abstract, sturucturally important things to
opt out of being qdeleted.
It does not exist to be a "Immune to everything" get out of jail free
card.
We have systems for this, and it's not appropriate here.

This change is inherently breaking, because things might be improperly
qdeling these things. Those issues will need to be resolved in future,
as they pop up

* Changes all needless uses of COMSIG_PARENT_PREQDELETED

It exists for things that want to block the qdel. If that's not you,
don't use it

* Adds force and hard del verbs, for chip and break glass cases
respectively

The harddel verb comes with two options before it's run, to let you
tailor it to your level of fucked

* Damn you nova

Adds proper parent returns instead of . = ..()

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Ensures immortality talismans cannot delete their human if something goes fuckey. Thanks ath/oro for pointing this out

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [TristanM04/MajorProject2022](https://github.com/TristanM04/MajorProject2022)@[88c51b1915...](https://github.com/TristanM04/MajorProject2022/commit/88c51b19151c8730e4ed0ebc893b07176d85e5a9)
#### Thursday 2022-05-19 12:17:05 by TristanM04

Writing to and reading from the DB

Since the last Git push, I fixed the last exception that was thrown when trying to write to the database. The issue was that the ID table had "Not null" ticked in the Database, meaning it doesn't allow nulls. I was ecstatic when I successfully wrote to the database, however this happiness was short lived as when I try to check if a user already exists my application, I enter an eternal loop, I looked around for answers on logic but couldn't find any that works if (C# WPF DB Browser for SQLite). This is when I remembered that my good friend Ethan worked with C# interfaces last year, so I asked him about it and I ended up not needing the loop. However, now my application freezes when I try write to the DB and no exception is thrown which means I don't even know where to start when it comes to troubleshooting.

A side note: I initially decided to do a push each week, however I have started to do one whenever I reach a milestone or roadblock. I also believe that from now on, my Git pushes will have similar length explanations to this one.

---
## [littleskyyy/Campus-recruitment](https://github.com/littleskyyy/Campus-recruitment)@[c1259f35b2...](https://github.com/littleskyyy/Campus-recruitment/commit/c1259f35b25e23c64b4317f9ca3275a2f64ac223)
#### Thursday 2022-05-19 12:37:42 by littleskyyy

Add files via upload

Abstract and Figures:
Each student dreams of having a work offer in their hands before leaving college.
 A selection probability indicator lets students get an sense of where they're standing and what to do to ensure a decent selection.
 A placement project that can forecast the probability or form of business that a student in the pre-final year has chances of placing. 
While a forecasting project could help in the academic preparation of an institution for future years.
 With the emergence of data mining and machine learning, through analyzing the data set of the previous student year, numerous predictive models were applied. 
Steps involved in data cleaning & Preprocessing:
 Step 1: Importing Necessary libraries
Step 2: Importing dataset from local directory
Step 3: Using unique to show what are the unique value present in each column
Step 4: To check any null values are present in our dataset
Step5: Drop unnecessary columns (these column does not affect out target, if we delete these column) in permanently.
Step 6: To check any outliers are present in our dataset by using BoxPlot. If any outliers are present we have to replace or remove outlier using IQR method.
Step 7: Using countplot we have to know how many students are getting placed and how many male and female students are placed or not.
Step 8: Using heat map and pairplot, To check  how to correlate with each column in our dataset.
Step 9: we need to convert our categorical value into numerical value so we use LabelEncoder and Get_dummies to covert our dataset.

Building a machine learning model:
We have to split our input(Independent) and target variable (Dependent).
Using ExtraTreesRegressor, we find which feature is closest or important in our target output.
We use standardscaler to the values are modified and lies between 0 to 1.because the variation of values is high.
Now, we have to import necessary libraries for building a machine learning model.
We use traintestsplit and it is used to estimate the performance of machine learning algorithm.
Now we use LogisticRegression, Decisiontree  for predicting our dataset. We find Classification report for getting Precision, Recall and Confusion matrix(TP,TN,FP,FN) and Accuracy Score(It show how much of percentage your prediction is correct) of our dataset.
Now we have to check our test input using model testing and check whether the news are real/fake.

Conclusion:
After Analysis of data I can conclude that whether the students are getting placed depends upon their individual knowledge, Degree percentage and work Experience..

---
## [Finch2002/Pass-Your-C_TSCM42_67-Exam-Easy-Certsleads](https://github.com/Finch2002/Pass-Your-C_TSCM42_67-Exam-Easy-Certsleads)@[05c03ca5d3...](https://github.com/Finch2002/Pass-Your-C_TSCM42_67-Exam-Easy-Certsleads/commit/05c03ca5d30aadf66821818b83fbc490645c81f4)
#### Thursday 2022-05-19 13:08:10 by Tim

SAP C_TSCM42_67 Dumps Pdf

Latest C_S4FTR_1809 Dumps with Verified SAP C_S4FTR_1809 Exam Questions 2022

C_S4FTR_1809 is one of the most important IT certification exams. The SAP C_S4FTR_1809 exam candidates try hard to pass their SAP 365 Fundamentals exam at their first attempt with good marks, but it is not easy. The SAP 365 C_S4FTR_1809 exam checks the skills of the candidates, and that makes the C_S4FTR_1809 exam difficult to pass for the candidates who do not have enough knowledge about the SAP 365 Fundamentals. To pass the SAP C_S4FTR_1809 exam successfully in one go, you have to use a C_S4FTR_1809 exam dumps learning material that contains all the information about the SAP 365 Fundamentals such as Realdumpspro exam dumps. Realdumpspro has prepared the C_S4FTR_1809 dumps preparation material according to the syllabus of the SAP 365 C_S4FTR_1809 test. You will enjoy the best learning experience with the Realdumpspro C_S4FTR_1809 dumps learning material.

What To Consider For SAP C_S4FTR_1809 Exam Questions Preparation?

Realdumpspro offers the C_S4FTR_1809 dumps preparation material in the easy-to-understand pdf file. You can easily download the C_S4FTR_1809 exam dumps on all the devices that include your PC, laptop, Mac, tablet, and smartphone. With the help of C_S4FTR_1809 dumps pdf, you will not have to go to preparation classes. The C_S4FTR_1809 exam dumps will help you in preparing for your exam at your home or office.

100% Real Exam Dumps of C_S4FTR_1809 Exam

Realdumpspro offers the 100% verified C_S4FTR_1809 dumps pdf. You will get the questions and answers in the C_S4FTR_1809 pdf dumps that belong to the actual format of the SAP 365 C_S4FTR_1809 exam. You will get the relevant questions and answers from all the topics of the SAP 365 Fundamentals exam that are 100% valid to use for the C_S4FTR_1809 exam preparation. The pdf questions and answers learning dumps are designed and verified by the subject matter experts. So, there is no doubt in the validity of the C_S4FTR_1809 exam dumps.

Get Free Updates for Three Months on C_S4FTR_1809 Dumps

If you are using the Realdumpspro SAP exam dumps learning material for your SAP 365 Fundamentals preparation, then you do not have to worry about the updates. Realdumpspro provides you the learning material according to the most recent version of the C_S4FTR_1809 exam. The syllabus might get change after your purchase of the SAP C_S4FTR_1809 dumps, so Realdumpspro will also provide you the after-purchase updates without any delay. You will get the updates as soon as the company introduces them. These updates will be free within the three months after your purchase.

Check Free C_S4FTR_1809 PDF Demo Before Payment

Realdumpspro offers a demo for your satisfaction with the C_S4FTR_1809 exam dumps learning material. The demo is free and shows the efforts of the experts who prepared this amazing C_S4FTR_1809 dumps learning material for the preparation of the SAP 365 Fundamentals exam. You will get an idea about the quality and features of the C_S4FTR_1809 exam dumps which will make your decision easy about the purchase. If you find the C_S4FTR_1809 exam dumps useful, then don't waste your time in delaying your purchase. Order for the C_S4FTR_1809 dumps to get your desired marks in your SAP 365 Fundamentals exam.

100% Refund Guarantee on C_S4FTR_1809 Dumps

There is no chance of failure in your SAP 365 C_S4FTR_1809 exam if you are preparing with Realdumpspro. Use the C_S4FTR_1809 dumps pdf for at least two weeks to prepare well for your C_S4FTR_1809 SAP 365 Fundamentals exam, and then take your C_S4FTR_1809 exam confidently. You will surely get maximum marks in the C_S4FTR_1809 exam. If you could not pass your SAP 365 Fundamentals exam at your first attempt with good marks, then you can ask for the payment refund. Realdumpspro will take the responsibility of your failure in the SAP C_S4FTR_1809 exam, and send your payment back according to the refund policy.

Get Special Discount Offer on C_S4FTR_1809 Dumps PDF

Realdumpspro has recently announced a huge discount offer. Now you can get your SAP C_S4FTR_1809 Exam Dumps pdf questions and answers product at the discounted price of 20%. Order now and start your preparation to pass the C_S4FTR_1809 exam with excellent marks.

Visit Here: https://www.realdumpspro.com/C_S4FTR_1809-dumps-pdf

---
## [DAVTOURS/-Best-Safari-Experiences-in-Uganda](https://github.com/DAVTOURS/-Best-Safari-Experiences-in-Uganda)@[72d06d7d68...](https://github.com/DAVTOURS/-Best-Safari-Experiences-in-Uganda/commit/72d06d7d68e0d0e7a942bc8aa0ecb212007df80e)
#### Thursday 2022-05-19 14:26:23 by Dav Safaris

 Best Safari Experiences in Uganda

 Best Safari Experiences in Uganda
A wide selection of safari experiences easily included on a single journey’s itinerary makes Uganda a favorable safari destination. From immersive city cultures to remote hidden tribes, expansive big game savannah plains, to rainforests populated with primates and birds, you will have something for every day you travel in Uganda.
Let’s take a look at the seven best safari experiences in Uganda that any tourist can choose to have on their itinerary.

1. Mountain Gorilla Trekking
Gorilla trekking in the mountain rainforests of southwestern Uganda is undoubtedly on the top of the best safari experiences in Uganda. Seven of every Uganda safari trip include a gorilla trekking experience in Bwindi Impenetrable National Park.
Trekking deep in the mystical jungles searching for a family of mountain gorillas and spending sixty minutes sitting quietly in their presence beats most wild adventures in Africa. Uganda has one of the most active primate conservation programs and collaborating with Rwanda and the DR Congo government has saved the endangered primates from extinction.

Today, Uganda protects more than half of the last mountain gorillas. It provides incredible opportunities for visitors to spend uninterrupted moments with habituated gorilla groups in protected parks. Gorilla tourism has incredibly increased the survival chances for mountain gorillas in their range. 
Over 1000 mountain gorillas survive between two populations. One of the populations is entirely within the Ugandan border, with about 500 individuals protected in Bwindi Impenetrable National Park. The other population roams the slopes of the Virunga Mountains between three national parks, including Volcanoes National Park in Rwanda, Virunga NP in DRC, and Mgahinga NP in Uganda.
About twenty (20) gorilla groups in Uganda have been habituated to human visits and are available for gorilla tourism, and a few others are reserved for research. What makes Uganda a favored destination for gorilla experiences is the gorilla habituation experience, which allows visitors to spend about 4 hours with gorillas and the typical gorilla trekking experience of 1 hour. 
On a gorilla trekking safari experience in Uganda, you’ll fly into the country and spend a night in or near the capital. The next day, you travel about 500 km southwest to the country’s extreme corner. You’ll also spend a night in a lodge outside the park. The experience of staying right outside the jungle is something to look up to, especially for nature lovers.
Gorilla trekking excursions start early at 7:30 am from five trailheads in the park’s boundaries. You will have spent a night close to any of the five trailheads at the starting point on time. You’ll join other trekkers at the trailhead and spend almost half the day in the forest, including paying for the allowed time with the gorillas.
You can book your entire journey with a local operator. However, make sure you organize your trip with a licensed and trusted operator to process your trekking permit, book your accommodation, and transport you to the park. Such is Dav Safaris Ltd at info@davsafaris.com .

2. Chimpanzee Trekking
Right under the gorilla experience, chimpanzee trekking is one of the top two not to miss safari experiences in Uganda. Tracking chimpanzees is an assured way to connect to our primate history and bond you with human’s closest relatives. Looking straight in the eyes of a wild chimpanzee that lives in its natural forest and seeing the similarity it shares with us is an unforgettable experience. 
Chimpanzee trekking experiences in Uganda occur daily in Kibale National Park and Budongo Forest. These early morning treks bring visitors a few feet close to the wild primates, allowing the visitors to stay with the chimps for an hour guided by expert local guides. It is a must-do experience for adventure lovers and forest walking enthusiasts.
However, chimpanzee trekking demands moderate physical fitness. Chimps are active primates and, within their natural range, can move from 2 km to 10 km in a day. So keeping up with their movements during your visit is an active experience that may drain your limbs of energy. Therefore, do some simple exercises before booking your chimpanzee trekking experience in Uganda.
The chimpanzee trekking experience costs $200 for a permit in Kibale Forest or less in other forests like Budongo and Kyambura Gorge. There is a wide selection of safari accommodation within trekking center distance for budget and high-cost choices. You could spend about $100 to $900 per night on a room with decent amenities and meals.
Please email us at info@davsafaris.com to help you plan your chimpanzee tracking experience in Uganda with trusted local expertise.

3. Wildlife Watching Game Drives
Uganda offers incredible wildlife watching game drive experiences with good privacy in less crowded safari parks. Big animals are present, including lions, elephants, giraffes, hippos, buffalo, zebra, and many antelope species.
Although the animals are not as concentrated as in Kenya and Tanzania, wildlife watching is one of the best safari experiences in Uganda because of the fewer tourists within the national parks.
Uganda has four big-name national parks that offer safari game drives as good as anywhere else in Africa. All of them are family-friendly, with a good selection of lodges and camps for kids. Fortunately, you can also comfortably add a game drive safari to primate experiences in southwestern Uganda on the same trip, which no other country can offer.
The best safari experiences in Uganda for game drives occur all year through Lake Mburo, Queen Elizabeth, Murchison Falls, and Kidepo Valley National Park. Lake Mburo, the smallest national park, has excellent safari experiences for the whole family, including walking safaris, boat trips, and horseback riding safaris that get you an arm’s distance to big animals.
Queen Elizabeth National Park, very famous to most tourists, has the best game drives and boat safari experiences that get close to big animals like lions, buffalo, hippos, elephants, leopards, and small animals like antelope and warthog.
The wildlife attractions of Murchison Falls National Park in the northeast, with the world’s most powerful waterfall, have exciting boat ride experiences on the Nile River. The boats bring tourists close to the river banks, where big and small wild animals come to cool down and drink in the summer heat. A game drive in the park’s vast savannah plains brings you close to lions, elephants, giraffes,  leopards, buffalo, hippos, and big Nile Crocodiles. 
Another unique safari experience in Uganda is coming close to wild Rhinos in Ziwa Rhino Sanctuary, the only protected place where you can see the nearly extinct species. The sanctuary offers an experience to track Rhinos on foot with expert trackers.
Further north in the isolated arid region mixed with vast plains and mountainous landscapes is Kidepo Valley, National Park. Head to the extreme northeastern part if you’re looking for a private experience watching big wild cats and enjoying the landscape views. 

Or email at info@davsafaris.com us to help you put together memorable wildlife-watching experiences of your life.
4. Wildlife Viewing Boat Trips
Boat trips are some of the best means of viewing animals up close without interrupting their daily activities. Uganda offers some of the best wildlife viewing experiences in the comfort of a boat on the Kazinga Channel in Queen Elizabeth, Lake Mburo, and the Nile in Murchison Falls National Parks.
The best wildlife viewing in a boat is on Kazinga Channel, a hippo swamped freshwater channel that links Lake Edward to Lake George, bisecting Queen Elizabeth National Park into two. From the ship, you can view hippos, giant Nile crocodiles, elephant and buffalo herds, and many other animals and birds on the channel’s shore. You can join any launch trips happening in the afternoon or hire a private speed boat to explore the channel. 
The launch safari on the Nile in Murchison Falls National Park is also one of the famous safari experiences in Uganda that brings you close to wild game. However, most tourists take it for the experience to the bottom of the mighty Murchison Falls, where waters of the Victoria Nile squeeze through an 8-meter-wide gauge and plunge 45-meter down with a thunderous roar.
The launch trip starts from Paraa a couple of times a day and rides upstream, showing a fantastic diversity of plant & animal species, including elephants, giraffes, and buffaloes, on the river banks. You can view Nile crocodiles, hippos and many aquatic birds lined on the river banks up to the bottom of the falls. The same experience occurs downstream in the Nile Delta, where visitors meet the mighty shoebill, one of the rarest stork-like birds in the world.
You can reach the jetty and join the launch trip in the afternoon, but most travelers want the tour operator to take care of all the planning. For that, please write us an email at info@davsafaris.com .  
5. Bird Watching
Birding experiences in Uganda offer a treat of rare and colorful bird species. The chance for bird-watching enthusiasts to improve their birding lists dramatically. You can see more than 1,000 bird species in various habitats across Uganda – from montane forests to agricultural lands, wetlands, lakes, and savannahs. Uganda’s Albertine Rift regions in the west and the equator regions attract biodiversity of endemic species, making for the best bird spotting experiences in the country.
Most visitors start their bird-watching safari experiences around Lake Victoria. The Mabamba swamp waters are the best place to watch the highly prized shoebill and many other specials, including the blue swallow, pallid harrier, papyrus gonolek, and swamp flycatcher. Other unique sightings around the city lake include the pygmy goose, white-winged warbler, lesser jacana, Viellot’s weaver, palm-nut vulture, grosbeak weaver, black-headed weaver, Clarke’s weaver, and Carruther’s cisticola, and northern brown-throated weaver.

The entire southwestern Uganda safari circuit up to the northeastern belt offers the best bird-watching spots in the country. However, nothing beats the rainforests of Kibale and Bwindi Impenetrable National Parks, the heart and soul of the best bird-watching safari experiences in Uganda.
Bwindi Impenetrable Forest is the make-and-breaker of birding lists and is home to many endemic and rarest bird species. The forest boasts about 350bird species, including 23 Albertine Rift endemics and 14 not recorded anywhere else in the country.
Walking through Bwindi’s forest birding trails could put you in the path of some of the most famous inhabitants, the mountain gorillas, forest elephants, chimpanzees, and over one thousand butterfly species. Such an experience will stay with you for a lifetime.

6. Whitewater Rafting on The Nile
No place in Africa has the best rafting experiences than at the birth of the mighty Nile River in Jinja. Jinja alone is famous with tourists for its adrenaline adventures enlisted on the best safari experiences in Uganda list. Here, you will experience some of the world’s finest grade 5 whitewater rafting, bungee jumping, horseback riding, and quad biking adventure activities. Whether you are a solo traveler looking for fun, a random tourist, or a high adventure enthusiast, you’ll find something near the Nile source in Jinja City.
Whitewater rafting in Uganda is considered one of the best one-day safari experiences, especially if you are an active adventurer and want to know how Ugandan cultures intermix with contemporary east and western cultures. It is an excellent addition to the other five safari experiences in Uganda listed above.

7. Hiking and Mountain Climbing 
Uganda does not fall short of hiking and mountain climbing attractions, offering some of the best adventure safari experiences on the continent. From world-renowned forest trails to snow-capped peaks above the clouds, there’s a hiking trail through tunning beauty and the quality of the experiences to the visitors. The southwestern region is covered in stunning landscapes and vegetation, offering unique animal and birdlife encounters on the trails.
Whether you prefer long walks in ancient forests or hipped for a multi-day mountain climbing challenge, Uganda has a hiking spot for every type of hiker. 
The Rwenzori Mountains standing elegantly on the western border, protect 996 square kilometers of magical lakes, vegetation, rocky outcrops, cliffs, high glaciers, and snowy peaks; a hiker’s dreamland. A multiple-day hiking experience to the 4th highest peak in Africa at 5,109, Mount Stanley’s Margherita Peak, is of the most revered safari experiences in Uganda.
If you’re just starting out for active walking, look to the eastern border at Mount Elgon National Park. Mount Elgon stands 4,321 meters at Wagai with triking features, including one of the largest intact calderas globally. The warm springs by the Suam River, Kitum, Ngwarisha,  Chepnyalil, and Makingeny caves. The 200 ft wide and 660 ft Kitum cave walls contain salt deposits, a magnet to wild elephants. You could be lucky to meet them in the area. 
On the southwestern border, Virunga extinct volcanoes Mount Muhavura, Gahinga, and Sabinyo, offer some of the most adventurous safari experiences in Uganda. Mgahinga National Park protects the base of the three volcanoes on the Ugandan side, creating a natural home for uncountable animal and plant species, including the endangered mountain gorillas. Mountain gorillas attract most visitors, though!.
Not far from Mgahinga, another independent rainforest that covers the mountainous landscape of the Rift valley, Bwindi Impenetrable Forest holds the highest number of mountain gorillas of the other three protected forest reserves. Bwindi is a nature hiker’s heaven, offering some of the oldest forest trails in the world. And most of them are a day’s hike through the ancient forest.

You should book some of these safari experiences in Uganda. www.davsafaris.com 
Uganda is one of those new cool players in the African travel market. Game safaris experiences that the colonial players killed off are slowly returning. Uganda even has an extra card that beats the competition, hands down.
Uganda has the most adventurous primate experiences at the most affordable prices and one of the world’s most successful sustainable tourism programs. You will have the best safari experiences with us planning your trip. Send us an email at info@davsafaris.com for s free quotation.

---
## [matthewgperry/dwm](https://github.com/matthewgperry/dwm)@[67d76bdc68...](https://github.com/matthewgperry/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Thursday 2022-05-19 15:31:41 by Chris Down

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
## [facebook/hhvm](https://github.com/facebook/hhvm)@[09db476765...](https://github.com/facebook/hhvm/commit/09db476765a1f4051eed71303aaec674d086ceeb)
#### Thursday 2022-05-19 16:19:49 by Hunter Goldstein

Typecheck `ext_std_classobj`

Summary:
Let's get `ext_std_classobj` well typed: we mainly want this for `get_class`, but this also uncovers some other issues.
 ---
Our logic for determining the expected function signature for a `__Native` function was slightly off. HHVM cannot, for it's native interface, represent nullable types: "nullability" is as good as `mixed`. Unfortunately, this logic would fall over on "nullable collections" (e.g.: nullable types with a `<` in their name). It would prioritize the collection part, assume the output could never be null, and promptly crash when it was. The only callsite here is in `hphp/runtime/vm/as.cpp`, in `type_constraint_to_data_type`, so I ended up just in-lining and simplifying the logic: we no longer check if something is a "collection." Assuming nobody is doing something like:
```
function foobar(); arraykey<Bing>;
```
The logic seems equivalent here.
 ---
`object` is a PHP type that used to mean "all classes;" it's since been killed in Hack given it was horribly unsound (you could call any method on it / access any prop, and you'd get back `TAny`). I've added a stub type `object` that aliases to `dynamic`. This is good enough for the typechecker, and close to morally correct, and allows HHVM to retain it's current behavior ... which is that unknown types in native functions are treated as if they're object names.

Reviewed By: aorenste

Differential Revision: D36355501

fbshipit-source-id: 157c67e1657efd921f8ee48b63ef60b4a0feb226

---
## [gitpodify/gitpodified-workspace-images](https://github.com/gitpodify/gitpodified-workspace-images)@[34969796da...](https://github.com/gitpodify/gitpodified-workspace-images/commit/34969796daff4137de8c63155954519ee16a8261)
#### Thursday 2022-05-19 16:30:06 by Andrei Jiroh Halili

chore(github-actions): 💚 add some workflow hacks to free up space for Dazzle builds and sync processes

God bless if GitHub didn't ban us because of this.

Signed-off-by: GitHub <noreply@github.com>

---
## [fmagin/cle](https://github.com/fmagin/cle)@[5e01abe4bc...](https://github.com/fmagin/cle/commit/5e01abe4bc8206aa45a9c9259fa4ce198840d741)
#### Thursday 2022-05-19 18:13:28 by Audrey Dutcher

Refactor CLE to separate linking from mapping and relocation (#230)

* Actually calculate the needed area for static TLS data. see #211 and #192

* Refactor loading into separate linking/mapping/relocating phases

* Fix TLS for real. now there's a notion of being able to specifically allocate a thread, which does not happen by default

* Cope with java tls bullshit in a stupid way for now

* jesus fucking christ

* docstring lint

* add additional stopgap for unknown data allocations

* make firmware test less dependent on exact address layouts (since the extern allocations changed)

---
## [SouthyOsmanli/sojourn-station](https://github.com/SouthyOsmanli/sojourn-station)@[796aeaa98f...](https://github.com/SouthyOsmanli/sojourn-station/commit/796aeaa98f76c2a6ef7a94e540d3b8f7efcb027b)
#### Thursday 2022-05-19 18:14:31 by lolman360

fixes stacks deleting randomly (#3357)

* whoo

* god i fucking hate stackcode

thank you kevinz

---
## [bansheerubber/eggscript-interpreter](https://github.com/bansheerubber/eggscript-interpreter)@[ced6be8509...](https://github.com/bansheerubber/eggscript-interpreter/commit/ced6be85098ffb2248c0f6f85c2b8191a3c52f0f)
#### Thursday 2022-05-19 19:11:06 by bansheerubber

performance improvement? who knows at this point

what is performance anyways? why do people make a big deal out of it? is it actually important? i assume it is, because people keep talking about it. but every time i seek out performance i only find pain. pain and suffering that is unimaginable. stuck in a prison of my own making for days just to find that i did not achieve performance. why must i suffer when i look outside and the rest of life is moving along without me? the ducks in the sky that fly past my house do not know the meaning of performance and even if they did, they would not care for it. the plant that grows in my backyard cannot even have thoughts. how blissful it must be, to not know the meaning of performance.

---
## [FraEgg/android_kernel_oneplus_msm8998](https://github.com/FraEgg/android_kernel_oneplus_msm8998)@[91a9e91029...](https://github.com/FraEgg/android_kernel_oneplus_msm8998/commit/91a9e91029ffc61fce24204c43e5d27e7e382b07)
#### Thursday 2022-05-19 19:37:26 by Maciej Żenczykowski

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
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[5d4ed67daf...](https://github.com/Perkedel/Kaded-fnf-mods/commit/5d4ed67dafb896e12a4669a4dc901a4159324450)
#### Thursday 2022-05-19 20:15:59 by Joel Robert Justiawan

[skip ci] immense

immense disappointment something that inspired us had us something. people seems anti-apologize that makes us very confused whether or not to also anti-forgive..

For life. God will see our hatred in the day of judgement, what if He saw that hatred? what do we gonna do now? just one makes trouble you know. But at the same time, it could be.. that something may not outright serious in their change.

well honestly that is for another day, but it's serious and considered require asap actions. peck, I need help.

Yoinkered another gf variants

deyoink thicc gf. confirmed that was tracened without permission. And I did not get to download the last update. peck!

well atleast we have Redsty Phoenix gf yess. idk man

installed template speaker (no gf) & floating gf.

attempted to fix week 7 song 3. oh no. times up.

UNTESTED. CRASH OCCUR

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[23aef65ad5...](https://github.com/pariahstation/Pariah-Station/commit/23aef65ad58754e8327151ece4c0efa6d810e1ed)
#### Thursday 2022-05-19 20:22:56 by SabreML

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607) (#704)

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

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ebb9739dbb...](https://github.com/mrakgr/The-Spiral-Language/commit/ebb9739dbb467498e03cd5c0764757f4ace4f2bb)
#### Thursday 2022-05-19 20:42:21 by Marko Grdinić

"11:40am. Let me read the Tenken chapter and I will start modeling.

11:55am. Let me start modeling. I do not feel like it, but I'll get into it once I start.

60 days remaining in the Moi trial. I really like how long it is. I am going to have to figure out how to reset the counter once it runs out. At 300$ it is too expensive for me to just buy it.

I'll buy it once I start making money though.

11:55am. Let me busy myself with the door a bit more. Forget hurrying and the later stages. Right now I am feeling fatigued and should just focus on a single thing.

12:55pm. Let me add some extra pieces on the grill.

2:10pm. This is terrible. I accidentally erased a few grill pieces and the door. I thought I was hiding it. What the hell? Damn these metal latches are difficult to do. I am not sure that I am doing it right. It might have been better to make it straightforwardly and then deform it.

At any rate, I am going to have to angle the doro back into place.

2:20pm. To make sure it does not happen again I spent some proper time locking the objects.

2:25pm. Let me take a little breather here.

I am exhausting myself here for no reason at all. Instead of doing it like in Zbrush by starting with a solid and cutting it up, here I am drawing lines on air offsetting and extruding them. The way I am doing it now is a lot harder than the laternative! Also even though Moi's ability to do deformations is far inferior to poly programs, it is not non existed. I should have used it bend the hinge.

2:30pm. Ok, let me do this final part. This time properly.

Today's modeling session is such a shameful display, it like I am not even paying attention to the possibilities. Cutting things up should always be at the forefront of my mind.

5pm. Focus me, I am almost done with the second pass for the doorway. I bussied myself with a lot of what will turn out to be irrelevant details, but this is good modeling practice. I won't do the curtains, but how about I at least do the hangers for them. I'll model a single one.

5:35pm. Time for a lunch break.

6:05pm. Damn it, I timed out the capcha. I guess I won't be starting part 3 today. It is a pity.

When I timeout a RapidGator capha it tells me to wait an hour and then 2 more hours after that. It seems to be designed to annoy the user.

Also, in all this time I am yet to get a reply to the Substance Painter issue. I am going to leave it completely out of mind.

Now, let me finish modeling the curtain piece now that I've come tihs far.

6:30pm. Ugh, let me investigate how sweep works. I need to figure out two rail sweeps.

8:10pm. Finally done for the day. Two rail sweep worked great. The reason why it did not initially is because one of the curves wasn't closed. It had a very tiny gap, I barely realized it.

It did some intricate stuff on the clam clipper for the curtains. It is some nice modeling. I spent what must be hours on what the user will never even see. But I am happy regardless.

I feel like I have a handle on Moi. I really like modeing in it. If I ever want to practice my drawing skills I should take these models and use them as a reference.

Right now the balcony entryway is really quite nice. Tomorrow, I will deal with the bed. It should not take more than an hour, at least in Moi. Blankets and various clothing pices I will do in Blender as well as the bed wrinkles.

8:30pm. Let me do a bit extra. I just want to put screws in two places. Then I'll post a screenshot in the /wip/ thread.

8:35pm. Also I finally figured out how to disable hidden (occluded) lines. There is that setting in the options. This will make things a lot easier in the future. It really gets tiresome when the snap to jumps through everything when there are a lot of objects present in the scene. I should ask how to turn toggling it into a hotkey. I'll look in the shortcuts list first.

8:45pm. Sigh, very nice. Doing what I did today in Blender would have been quite hard.

10:25pm. https://www.youtube.com/watch?v=iXu7BMWvBGQ
The Benefits of Drawing Before Painting (Quickest Way to Learn Both)

Let me watch this. I want some clues as to how to learn painting.

https://youtu.be/iXu7BMWvBGQ?t=105
> My experience is that people that learned how to draw first adapted to painting extremely quickly and passed up all the people that didn't draw and just been painting for a few years.

The other guy follows up saying that drawing is the foundation of painting. Ok, I guess I can just focus on drawing then.

> Perspective? It is going to be so much harder to learn perspective through painting.

https://youtu.be/iXu7BMWvBGQ?t=332
> I remember seeing an artist in LA who worked tonally right from the beginning, he'd arranged masses of oil paint and he'd use a fan brush to blend it and then he'd gradually blend and blend and blend and blend, and do these beautiful portraits...so clearly value in a fog that gradually crispens. And he had a good eye. But it isn't the way, certainly not the way that a 3d program works. It can't render, it can't give you light and dark until it has a scaffolding of something to put the light and dark on. And so that to me is my biased way of how I think a student should learn.

Never saw this channel before, I'll check it out."

---
## [Forgind/msbuild](https://github.com/Forgind/msbuild)@[a572dc6b79...](https://github.com/Forgind/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Thursday 2022-05-19 20:42:28 by Forgind

Fix low priority issues (#7413)

Thanks @svetkereMS for bringing this up, driving, and testing.

This fixes two interconnected issues.
First, if a process starts at normal priority then changes to low priority, it stays at normal priority. That's good for Visual Studio, which should stay at normal priority, but we relied on passing priority from a parent process to children, which is no longer valid. This ensures that we set the priority of a process early enough that we get the desired priority in worker nodes as well.

Second, if we were already connected to normal priority worker nodes, we could keep using them. This "shuts down" (disconnects—they may keep running if nodeReuse is true) worker nodes when the priority changes between build submissions.

One non-issue (therefore not fixed) is connecting to task hosts that are low priority. Tasks host nodes currently do not store their priority or node reuse. Node reuse makes sense because it's automatically off always for task hosts, at least currently. Not storing low priority sounds problematic, but it's actually fine because we make a task host—the right priority for this build, since we just made it—and connect to it. If we make a new build with different priority, we disconnect from all nodes, including task hosts. Since nodeReuse is always false, the task host dies, and we cannot reconnect to it even though if it didn't immediately die, we could, erroneously.

On the other hand, we went a little further and didn't even specify that task hosts should take the priority assigned to them as a command line argument. That has been changed.

svetkereMS had a chance to test some of this. He raised a couple potential issues:

conhost.exe launches as normal priority. Maybe some custom task dlls or other (Mef?) extensions will do something between MSBuild start time and when its priority is adjusted.
Some vulnerability if MSBuild init code improperly accounts for timing
For (1), how is conhost.exe related to MSBuild? It sounds like a command prompt thing. I don't know what Mef is.
For (2), what vulnerability? Too many processes starting and connecting to task hosts with different priorities simultaneously? I could imagine that being a problem but don't think it's worth worrying about unless someone complains.

He also mentioned a potential optimization if the main node stays at normal priority. Rather than making a new set of nodes, the main node could change the priority of all its nodes to the desired priority. Then it can skip the handshake, and if it's still at normal priority, it may be able to both raise and lower the priority of its children. Since there would never be more than 2x the "right" number of nodes anyway, and I don't think people will be switching rapidly back and forth, I think maybe we should file that as an issue in the backlog and get to it if we have time but not worry about it right now.

Edit:
I changed "shuts down...worker nodes when the priority changes" to just changing their priority. This does not work on linux or mac. However, Visual Studio does not run on linux or mac, and VS is the only currently known customer that runs in normal priority but may change between using worker nodes at normal priority or low priority. This approach is substantially more efficient than starting new nodes for every switch, disconnecting and reconnecting, or even maintaining two separate pools for different builds.

---
## [MidoriWroth/Skyrat-tg](https://github.com/MidoriWroth/Skyrat-tg)@[c5f0ea76e0...](https://github.com/MidoriWroth/Skyrat-tg/commit/c5f0ea76e0fa1d1236fe04a2edaf6d9c047fc7c8)
#### Thursday 2022-05-19 20:56:05 by SkyratBot

[MIRROR] Vim mecha changes [MDB IGNORE] (#12981)

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

---
## [smxi/inxi](https://github.com/smxi/inxi)@[6023702097...](https://github.com/smxi/inxi/commit/60237020970e3720d9a5cc2428cc28a1c10df9f9)
#### Thursday 2022-05-19 21:17:48 by Harald Hope

A nice release, some good corner case bug and glitch fixes, along with some much
needed documentation fixes to bring inxi-values.txt up to date for changes that
have been evolving steadily. And a useful option for nvidia legacy card info.

I'm hoping that will help support people and users as nvidia open source driver
gets more usable in the future, since that will never support legacy cards, only
the current series supported by 510/515 drivers.

Also, in inxi-perl/tools, new tools and data so you can reproduce certain arcane
data assembly features like disk vendors and nvidia product ids.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. Not known yet if you can get Wayland display drivers along with kernel gpu
drivers. In other words, is a similar use of kernel/display driver as in Xorg
found with Wayland? Hard to dig up actual answers to questions like this.

2. Similarly, unknown if it's possible to get current active xorg display
driver, not just the list from Xorg.0.log file. No idea how to discover that,
there are cases where past use of Xorg leaves log file present, but drivers are
not used with Wayland, leading to confusing driver reports. Issues 1 and 2 are
similar but probably have similar solutions.

--------------------------------------------------------------------------------
BUGS:

1. Very subtle failure caused by odd mount point in partitions: a too loose
regex rule designed to capture spaces in device names was running loose to the
end of the string, where it was triggered by a number in the mount point.

Fix was to make rule much more strict, now needs to match 3 number space in a
row after the initial part, and then a number%

2. Bug in corner case, with Monitors, if > 2 connected monitors, and 1 disabled,
inxi was trying to test numeric position values for the disabled monitor, which
with xrandr, has no position values, thus tripping undefined pos-x and pos-y
errors. Thanks to fourtysixandtwo for spotting this corner case.

3. Bug in wan IP, if dig failed, set_dowloader() is not set unless other
parameters were used, which results in failing to set parameters for downloader,
which leads to screen errors spraying out. Thanks to Manjaro user exaveal for
posting this issue, with error outputs, which helped pinpoint the cause.

--------------------------------------------------------------------------------
FIXES:

1. More absurd xorg port ID variations: DP-1 kernel, DP1-1 X driver. Wny?
Trying to add in XX-?\d+-\d+ variation, which I think will be safe, made the
first - optional, though it's just idiotic for this amount of randomness to be
allowed to exist in the 21st century. If this reflects other discipline failures
in Xorg, it starts to get somewhat more obvious why Wayland was considered as
the only forward path, though that's just as chaotic and disorganized... but in
different ways.

2. Removed darwin distro version detection, which of course broke, and using
standard fallback for BSD made out of uname array bits. If it works, it works,
if not, who cares. This should handle issue #267 hopefully.

3. Trying for more monitor matches, now in cases where 1 monitor display ID
remained unmatched, and 1 sys kms id remains unused, assume the remaining
nonitor ID is a match and overwrite the unmatched message for that ID. This
will cover basically all single monitor match failure cases, and many multi
monitor failures with only 1 out of x monitor ids unmatched. While guessing a
bit, it's not a bad guess, and will slightly expand the number of matched
monitor ids. This extends the previous guess where if single monitor and
unmatched, use it to cover > 1 monitors, with 1 unmatched.

4. LINES_MAX configuration item did not assign to right variable when -1 value.
Used non-existing $size{'output-block'} instead of correct $use{'output-block'}

5. Forgot to add pkg to --force, goes with --pkg.

6. Finally! Added in busybox shell detection, it's not of course reliable if
they change internal light shells, but all the docs say they use ash, so now
it will show shell: ash (busybox) to make it clear. Hurray!! This means that
tinycore users will get this long awaited feature! Ok, ok, long awaited by
probably only me, but since I package inxi for busybox, it was on my todo list.

7. Cleaned up and re-organized many disk vendor matching rules, made them easier
to read and debug, going along with Code 3, vendors.pl development and release.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. New feature: in -Ga, if Nvidia card, shows last supported nvidia legacy
series driver (like 304.xx), status, microarch. If --nvidia and EOL, shows
last-supported: kernel: xorg: info. This should be useful for support people,
we'll see.

-Gx shows nvidia microarchitecture, if it was found. This is based on matching
tables so will go out of date if you have non current inxi's, but that's life.

If --nvidia or --nv shortcut is used instead, triggers -Ga and shows much more
nvidia driver data for legacy, and for EOL drivers, last supported kernel, xorg,
and last release version. --nvidia also adds process node if available.

More important perhaps is the fact that as of May 2022, nvidia is starting the
process of open sourcing its current latest driver (515, but Turning, Ampere
architectures only so far), which will only support non legacy nvidia cards,
making detection of legacy cards even more important to support people and end
users, since that will be a common question support people will have: does my
card support the open source driver?"

Read about the new open sourcing of the 515 nvidia module:
https://developer.nvidia.com/blog/nvidia-releases-open-source-gpu-kernel-modules/
https://github.com/NVIDIA/open-gpu-kernel-modules
https://www.phoronix.com/scan.php?page=article&item=nvidia-open-kernel&num=1

2. Going along with new and upgraded tools in Code 3, massive, huge, upgrade to
disk vendors, 100s of new matches, biggest upgrade ever for disk vendors. This
feature should work much better now with the new backend tools.

3. Added shortcuts: --mm for --memory-modules, --ms for --memory-short.

--------------------------------------------------------------------------------
CHANGES:

1. None.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Big update to docs/inxi-values.txt. This had gotten really out of date, with
incorrect hash and other internal data assignments, all updated to be current,
along with sample greps to make it easier to locate changes in the future as
well. This makes this document fairly up to date and useful again for dev
reference purposes, should such a dev ever appear, lol. Many values had not
been updated after global refactors, like switching to the %risk data for all
arm/mips/ppc platform types, and making %load, %use, %force, %fake uses more
consistent. Doing this helped expose some subtle bugs and failure cases in
inxi as well.

2. Added to -h and man -Ga Nvidia option info. Fixed some typos and glitches.
Includes new --nvidia / --nv options for full data.

--------------------------------------------------------------------------------
CODE:

1. Changed $dl{'no-ssl-opt'} to $use{'no-ssl'} and $dl{'no-ssl'}, that was a
confusing inconsistency.

2. Added comma separated list of --dbg numbers, since often > 1 is used. Saves
some debugging time, otherwise nothing changes.

3. Huge new public release of some back end tools in new section:
inxi-perl/tools
* vendors.pl - disk vendors tool, with data in lists/disks*.txt
* ids.pl - nvidia product id generator tool, with data in lists/nv_*

4. While doing vendors.pl, I noticed that the use of array ref for $vendors was
not done correctly, that's fixed now, simplifies it slightly.

---
## [netflixfurimmer/Multi_Panel-](https://github.com/netflixfurimmer/Multi_Panel-)@[b80d26722c...](https://github.com/netflixfurimmer/Multi_Panel-/commit/b80d26722c8620e2221cb5e6f551b9188764ed7c)
#### Thursday 2022-05-19 23:24:33 by ZFX_HACRYPT Exploit

Multi_Panel Loud DDOS Panel Slamming 20 gig dstat      Tags  ddos attack, ddos attack explained, ddos panel, ddos attack roblox, ddosing, ddos tool, ddos apex legends, ddos roblox, ddos attack live, ddos attack tutorial, ddos attack kali linux, ddos attack website free, a ddos attack, ddosing a scammer, ddos a website, ddosing a ddoser, ddosing a minecraft server, doxing school, ddos a ip, ddos a router, ddos botnet, ddos booter, ddos bots tf2, ddos by daylight, ddos bot, ddos blizzard, ddos bot discord, ddos bluetooth, ddos crypto, ddos cloudflare, ddos coin, ddos csgo, ddos call of duty, ddos cod, ddos computerphile, ddos clash royale, c ddos script, reaper.c ddos, white c ddos, ddos c'est quoi, ddos discord, ddos dbd, ddos dead by daylight, ddos discord server, ddos download, ddos detection, ddos discord bot, ddos destiny 2, ddos explained, ddos em biet anh dang nghi gi, ddos error, ddos event, ddos exploit, ddos er, ddos eli5, ddos ethereum, attacco dos e ddos, o'que e ddos, ddos free, ddos fivem server, ddos fortnite, ddos from iphone, ddos facebook, ddos fortnite server, ddos fivem, ddos free tool, ddos ghost data, ddos gta 5, ddos gta, ddos gaming, ddos game servers, ddos glaive, ddos gta online, ddos github, ddos hack, ddos how to, ddos hacking song, ddos hacker, ddos hypixel, ddos hping3, ddos home router, ddos hammer, ddos in effect, ddos i_o, ddos internet attack, ddos ip address, ddos in kali linux, ddos is back, ddos in python, ddos in valorant, i does, i doesn't matter, i does what i wish to, i doesn't matter the rock, i does try to make you happy, i doesn't, i does do it like a boss machel montano, i doesn't matter how old i am, ddos jail, ddos jedag jedug, ddos jokes, ddos juniper, ddos jak zrobić, jensen ddos, jinn ddos, javascript ddos attack, ddos kali linux, ddos king, ddos kali, ddos karma, ddos kali linux 2021, ddos kali linux github, ddos kahoot, ddos kellogg's, ddos live, ddos league of legends, ddos ltg, ddos linux, ddos loic, ddos lucid, ddos link, ddos live attack, ddos mitigation, ddos meaning, ddos minecraft server, ddos mitigation techniques, ddos meme, ddos music, ddos multi tool, ddos methods, fivem ddos, ddos nasıl atılır, ddos net, ddos nedir, ddos news, ddos neighbors wifi, ddos network attack, ddos nfl mateja, ddos nasıl atılır discord, ddos overwatch, ddos on xbox, ddos on phone, ddos osrs, ddos overwatch ps4, ddos on kali, ddos on ps4, ddos on android, i_o ddos, o que é ddos ataque, o que e ddos, ddos protection, ddos panel free, ddos panel source, ddos python, ddos panel source code, ddos ps4, ddos protection by cloudflare, ddos questions, ddos quick guide, ddos que es, mac quayle ddos hacking song, comment ddos quelqu'un, ddos quelqu'un sur discord, ddos roblox server, ddos rainbow six siege, ddos roblox attack 2021, ddos ripper, ddos roblox script, ddos rocket league, ddos rust, ddos script, ddos school, ddos song, ddos script python, ddos software, ddos scammer, ddos school wifi, ddos someone, ddos tutorial, ddos titanfall 2, ddos tf2, ddos tool python, ddos tool free, ddos termux, ddos tool download, ddos using kali, ddos using python, ddos using ip, ddos using termux, ddos using cmd, ddos urban, ddos udp flood, ddos using a ldap reflection attack, how do u ddos someone, ddos vs dos, ddos valorant, ddos voip, ddos vs vpn, ddos vs dox, ddos vps, ddos vpn, ddos virus, gta v dos, ddos websites free, ddos website, ddos with kali, ddos with python, ddos warzone, ddos wifi, ddos with cmd, ddos wifi router, ddos w notatniku, jak ddosowac w minecraft, jak ddosowac w cmd, ddos w cmd, ddos xbox, ddos xbox 2021, ddos xbox one, ddos xbox live, ddos xbox gamertag, ddos xbox booter, ddos xbox party, xqc ddos, project x ddos, ddos x jedag jedug, ddos yiyen yayıncı, ddos yourself, ddos youtube, ddos yesterday, ddos yourself test, ddos your own network, ddos you, ddos your friends, dos y dos, ataque dos y ddos, ddos zoom meeting, ddos zoom, ddos zombie, ddos zombie nets, ddos zombie attack, ddos vent, ddos in effect xenoblade, ddos attack on zoom meeting, jak z ddosować kogos, ddos 127.0.0.1, ddos 101, ddos windows 10, ddos cs 1.6 server, titanfall 1 ddos, ddos tool windows 10, cách ddos 1 trang web, ddos cs 1.6, ddos 2021, ddos 2016, ddos 2019, 2b2t ddos, tf2 ddos 2021, dbd ddos 2021, ddos attack 2021, titanfall 2 ddos, titanfall 2 ddos update, titanfall 2 ddos attack, destiny 2 ddos, titanfall 2 ddos is back, slavehack 2 ddos, titanfall 2 ddos dlc, titanfall 2 ddos lore, ddos 33, teamspeak 3 ddos attack, teamspeak 3 ddos, ddos 403, ddos layer 4, ddos playstation 4, ddos gtps 4, ddos left 4 dead 2, layer 4 ddos script,

Multi_Panel
Loud DDOS Panel Slamming 20 gig dstat      Tags  ddos attack, ddos attack explained, ddos panel, ddos attack roblox, ddosing, ddos tool, ddos apex legends, ddos roblox, ddos attack live, ddos attack tutorial, ddos attack kali linux, ddos attack website free, a ddos attack, ddosing a scammer, ddos a website, ddosing a ddoser, ddosing a minecraft server, doxing school, ddos a ip, ddos a router, ddos botnet, ddos booter, ddos bots tf2, ddos by daylight, ddos bot, ddos blizzard, ddos bot discord, ddos bluetooth, ddos crypto, ddos cloudflare, ddos coin, ddos csgo, ddos call of duty, ddos cod, ddos computerphile, ddos clash royale, c ddos script, reaper.c ddos, white c ddos, ddos c'est quoi, ddos discord, ddos dbd, ddos dead by daylight, ddos discord server, ddos download, ddos detection, ddos discord bot, ddos destiny 2, ddos explained, ddos em biet anh dang nghi gi, ddos error, ddos event, ddos exploit, ddos er, ddos eli5, ddos ethereum, attacco dos e ddos, o'que e ddos, ddos free, ddos fivem server, ddos fortnite, ddos from iphone, ddos facebook, ddos fortnite server, ddos fivem, ddos free tool, ddos ghost data, ddos gta 5, ddos gta, ddos gaming, ddos game servers, ddos glaive, ddos gta online, ddos github, ddos hack, ddos how to, ddos hacking song, ddos hacker, ddos hypixel, ddos hping3, ddos home router, ddos hammer, ddos in effect, ddos i_o, ddos internet attack, ddos ip address, ddos in kali linux, ddos is back, ddos in python, ddos in valorant, i does, i doesn't matter, i does what i wish to, i doesn't matter the rock, i does try to make you happy, i doesn't, i does do it like a boss machel montano, i doesn't matter how old i am, ddos jail, ddos jedag jedug, ddos jokes, ddos juniper, ddos jak zrobić, jensen ddos, jinn ddos, javascript ddos attack, ddos kali linux, ddos king, ddos kali, ddos karma, ddos kali linux 2021, ddos kali linux github, ddos kahoot, ddos kellogg's, ddos live, ddos league of legends, ddos ltg, ddos linux, ddos loic, ddos lucid, ddos link, ddos live attack, ddos mitigation, ddos meaning, ddos minecraft server, ddos mitigation techniques, ddos meme, ddos music, ddos multi tool, ddos methods, fivem ddos, ddos nasıl atılır, ddos net, ddos nedir, ddos news, ddos neighbors wifi, ddos network attack, ddos nfl mateja, ddos nasıl atılır discord, ddos overwatch, ddos on xbox, ddos on phone, ddos osrs, ddos overwatch ps4, ddos on kali, ddos on ps4, ddos on android, i_o ddos, o que é ddos ataque, o que e ddos, ddos protection, ddos panel free, ddos panel source, ddos python, ddos panel source code, ddos ps4, ddos protection by cloudflare, ddos questions, ddos quick guide, ddos que es, mac quayle ddos hacking song, comment ddos quelqu'un, ddos quelqu'un sur discord, ddos roblox server, ddos rainbow six siege, ddos roblox attack 2021, ddos ripper, ddos roblox script, ddos rocket league, ddos rust, ddos script, ddos school, ddos song, ddos script python, ddos software, ddos scammer, ddos school wifi, ddos someone, ddos tutorial, ddos titanfall 2, ddos tf2, ddos tool python, ddos tool free, ddos termux, ddos tool download, ddos using kali, ddos using python, ddos using ip, ddos using termux, ddos using cmd, ddos urban, ddos udp flood, ddos using a ldap reflection attack, how do u ddos someone, ddos vs dos, ddos valorant, ddos voip, ddos vs vpn, ddos vs dox, ddos vps, ddos vpn, ddos virus, gta v dos, ddos websites free, ddos website, ddos with kali, ddos with python, ddos warzone, ddos wifi, ddos with cmd, ddos wifi router, ddos w notatniku, jak ddosowac w minecraft, jak ddosowac w cmd, ddos w cmd, ddos xbox, ddos xbox 2021, ddos xbox one, ddos xbox live, ddos xbox gamertag, ddos xbox booter, ddos xbox party, xqc ddos, project x ddos, ddos x jedag jedug, ddos yiyen yayıncı, ddos yourself, ddos youtube, ddos yesterday, ddos yourself test, ddos your own network, ddos you, ddos your friends, dos y dos, ataque dos y ddos, ddos zoom meeting, ddos zoom, ddos zombie, ddos zombie nets, ddos zombie attack, ddos vent, ddos in effect xenoblade, ddos attack on zoom meeting, jak z ddosować kogos, ddos 127.0.0.1, ddos 101, ddos windows 10, ddos cs 1.6 server, titanfall 1 ddos, ddos tool windows 10, cách ddos 1 trang web, ddos cs 1.6, ddos 2021, ddos 2016, ddos 2019, 2b2t ddos, tf2 ddos 2021, dbd ddos 2021, ddos attack 2021, titanfall 2 ddos, titanfall 2 ddos update, titanfall 2 ddos attack, destiny 2 ddos, titanfall 2 ddos is back, slavehack 2 ddos, titanfall 2 ddos dlc, titanfall 2 ddos lore, ddos 33, teamspeak 3 ddos attack, teamspeak 3 ddos, ddos 403, ddos layer 4, ddos playstation 4, ddos gtps 4, ddos left 4 dead 2, layer 4 ddos script,

---
## [LordCupcakeIX/AutoTrimps](https://github.com/LordCupcakeIX/AutoTrimps)@[f7b39ffdb5...](https://github.com/LordCupcakeIX/AutoTrimps/commit/f7b39ffdb51d3a4ae1748556e0767ccd67539602)
#### Thursday 2022-05-19 23:33:31 by SadAugust

Fixing bugs and adding universe selection feature

Heyy, I made a few modification to graphs for my AT fork and figured I might as well share since it fixes a few bugs that I've at least been annoyed by quite a bit. If you want to test it out first to make sure it's all working you can test it on https://SadAugust.github.io/AutoTrimps_Local. Changed I've made are listed below, I've only done minimal testing but haven't found any issues with it.

Removed minified version of code to make it readable

Added option to select Universe which will visibility of U1 and U2 graphs depending on the selection. Reduces a ton of unnecessary settings from cluttering the list and figured I'd make it easier to expand for if we do get more universes.

Remembers graph selection when reloading the page instead of defaulting to helium/radon per hour

Hides portals from other universes showing so if U2 graphs are being looked at you won't see U1 portals in the sidebar, should fix bugs like void maps being unreadable when there's a significant difference in portals between the 2 universes.

Fixed it not drawing graphs properly when reopening Graphs after the initial load as it was a nuisance having to go to another graph and back to get it to display anything.

---
## [DarkoniusXNG/oaa](https://github.com/DarkoniusXNG/oaa)@[841368b6b0...](https://github.com/DarkoniusXNG/oaa/commit/841368b6b064c700c6194d8e46d798e0d4494ed1)
#### Thursday 2022-05-19 23:46:40 by Darko V

Modifiers changes (May 2022) (#3351)

* Cycled Out modifiers: Hyper Lifesteal, Blood Magic, Healer and Brute.
* Randomize button will no longer randomize the 'None' option.
* Buffed Timeless Relic modifier from 25% to 30%.
* Telescope modifier now also provides 400 bonus vision (day/night).
* Fixed Telescope modifier cast range bonus not stacking with other cast range bonuses.
* Fixed Creed of Omniscience and Telescope neutral items cast range bonuses not stacking with Octarine Core or Far Sight cast range bonuses.
* Random Draft number of banned heroes increased from 70 to 75.
1) Added Aghanim, Nimble and Sorcerer modifiers.
2) Updated tooltip for Wisdom modifier.
3) Bonus AoE/Radius modifier now ignores:
- Arc Warden Flux search radius
- Drow Ranger agility range penalty
- Monkey King Wukong's Command
- Phantom Assassin Blur
- Spectre Desolate
4) Bonus AoE/Radius now improves Sohei's Dash width.
5) Diarrhetic auto-poop-ward check-for-wards-radius increased from 200 to 300. This means auto-pooped wards will be farther from each other.
6) Explosive Death modifier will now proc on Tempest Doubles and heroes that are reincarnating.
7) Attack Range Switch modifier bonus attack range reduced from 600 to 500.
8) Attack Range Switch modifier bonus projectile speed increased from 900 to 1100.
9) Added Max Power modifier
10) Fixed tooltip for modifiers saying undefined when 'Random' option is selected.

---

