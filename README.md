## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-09](docs/good-messages/2022/2022-05-09.md)


1,723,072 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,723,072 were push events containing 2,820,814 commit messages that amount to 213,788,231 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [Lastprismer/FargowiltasSouls](https://github.com/Lastprismer/FargowiltasSouls)@[df7c27eb16...](https://github.com/Lastprismer/FargowiltasSouls/commit/df7c27eb16e2e5d05bcab70599aec5d1e99d2f06)
#### Monday 2022-05-09 00:00:39 by terrynmuse

sibling pets are master drop now instead of emode nohit
devi pet talks because fuck you i can do that (has toggle)

---
## [Son-of-Space/tgstation](https://github.com/Son-of-Space/tgstation)@[98f32035d8...](https://github.com/Son-of-Space/tgstation/commit/98f32035d8dbd6b925700e9934652d03739f024b)
#### Monday 2022-05-09 01:24:14 by LemonInTheDark

Parallax but better: Smooth movement cleanup (#66567)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

---
## [Nyanotrasen/Nyanotrasen](https://github.com/Nyanotrasen/Nyanotrasen)@[b6c6b747e2...](https://github.com/Nyanotrasen/Nyanotrasen/commit/b6c6b747e20a8dba398ae53579f0cb0c60d5c14d)
#### Monday 2022-05-09 01:39:06 by Rane

Shrink Ray (#66)

* Basic infrastructure

* It just works

* Give them item

* holy shit that was painful

* shrink ray

* Add tech

* Stopped unintentional change

* Don't affect windows

---
## [Asteroiddust/Grasscutter](https://github.com/Asteroiddust/Grasscutter)@[fbaeaee4b5...](https://github.com/Asteroiddust/Grasscutter/commit/fbaeaee4b5aa82fe10897b60ea642d4428e8abd8)
#### Monday 2022-05-09 02:54:30 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [LukeSandsor/GitFit-App](https://github.com/LukeSandsor/GitFit-App)@[581b91acff...](https://github.com/LukeSandsor/GitFit-App/commit/581b91acff84fb97f45824bbf79384b501b06dde)
#### Monday 2022-05-09 04:39:41 by Lucas Reyna

after painfully implementing contexts into the CalendarPage.js, I am happy to announce that the calendar will now load info on a specific day. The code looks kinda like garbage, but it works for now. I just hope that there won't be many slow downs when incorporating the backend. We'll have to see about caching, maybe.

---
## [ionutnechita/linux-sunlight](https://github.com/ionutnechita/linux-sunlight)@[213d266ebf...](https://github.com/ionutnechita/linux-sunlight/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Monday 2022-05-09 05:25:12 by Linus Torvalds

gpiolib: acpi: use correct format characters

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

---
## [linkmia/_posts](https://github.com/linkmia/_posts)@[807dfd6968...](https://github.com/linkmia/_posts/commit/807dfd69681b445ebbba2a0d3472ec0088003dd2)
#### Monday 2022-05-09 05:37:53 by linkmia

Create I LOVES WHEN HIS HARD COCK FUCK MY TINY TIGHT ASS  PAINFUL ANAL WITH TEEN | ANAL FUCK for the little Princess

I LOVES WHEN HIS HARD COCK FUCK MY TINY TIGHT ASS  PAINFUL ANAL WITH TEEN | ANAL FUCK for the little Princess

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[0504c0a2b4...](https://github.com/san7890/bruhstation/commit/0504c0a2b466d617efd4dcc77b092fcdbdad24be)
#### Monday 2022-05-09 06:29:44 by LemonInTheDark

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
## [SabreML/Pariah-Station](https://github.com/SabreML/Pariah-Station)@[95db2c6bfc...](https://github.com/SabreML/Pariah-Station/commit/95db2c6bfc84871f2fa51eeef253f681dc46a632)
#### Monday 2022-05-09 07:34:25 by Kapu1178

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301) (#696)

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

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [acts-project/acts](https://github.com/acts-project/acts)@[6e1fd31474...](https://github.com/acts-project/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Monday 2022-05-09 07:45:14 by Stephen Nicholas Swatman

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
## [rohittembhurne2194/ICTSBMALL_ULB](https://github.com/rohittembhurne2194/ICTSBMALL_ULB)@[918ed4d8d8...](https://github.com/rohittembhurne2194/ICTSBMALL_ULB/commit/918ed4d8d86133b808010add9e7504944ca9d3e9)
#### Monday 2022-05-09 08:05:39 by umeshl@appynitty.com

Changes done By Millionaire persone and its me peaceMinded Aka Umesh I will be definitely successfull in six months and create my own rooms and trading destop with led tv and my dreams bedroom i will be successfull in my trading career ameen god bless me thanku for support and yours guidedess my gods

---
## [7891523620/World-Trade-Matka](https://github.com/7891523620/World-Trade-Matka)@[5b5680ba6d...](https://github.com/7891523620/World-Trade-Matka/commit/5b5680ba6d469e73460c6c9815ca9b218d0fb65b)
#### Monday 2022-05-09 08:21:49 by 7891523620

Add files via upload


International Mother's Day

Aperson who deserves to be the most cherished, loved, respected, admired, cared for, and every other thing that can be showered upon someone, is the only one in the whole world. One of the most admirable and strong bonds that one can have in today’s time is with their mothers. That is a relationship incomparable. A mother’s love is immeasurable.

As said, the highest amount of love and respect, if it should be given to someone, it should be to mothers. Not just your mother but to every single woman who is, was, and is going to be a mother. The woman who gave birth to you nourished you to be able to open your eyes when you enter the world with her blood, gave you the strength, and stood as your backbone just so you could stand out there and shine, she deserves to be given the priority in everything.


 
No matter how many days, months or years it takes, repaying our mothers for what they have done and can do for us is just not possible. To try and do that just a bit, there’s a whole day dedicated to mothers; Mother’s Day.


Mother’s Day is celebrated on the second Sunday of May, every year. This day isn’t just dedicated to the mothers but motherhood and maternal bonds are also a part of the reason for the day being celebrated. The day is celebrated worldwide. However, it was in the US in 1907 that it was first introduced and celebrated. A woman named Anna Jarvis was the reason that the world celebrated Mother’s day today. It was on the day of her mother's funeral in 1905, that she decided to establish the campaign for celebrating a day for mothers every year. It was then that she organized the first Mother’s Day service of worship, after two years. The church in which this was organized, Andrews Methodist Episcopal Church in West Virginia, now serves as the international Mother’s Day Shrine. Anna Jarvis was majorly focused on injured officers of the American Civil War, regardless of whose side were they on. She was a peace activist. To address general medical problems, she introduced Mother’s Day Work Clubs. She, along with another dissident, Julia Ward Howe had been encouraging the making of a "Mother's Day For Peace". It was the day that was going to be when moms would ask that their children and husbands weren’t under the compulsion to go to war and not be killed. Anna Jarvis believed that ‘the individual who has accomplished more for you than anybody on the planet’, and for her, it was the mothers of the world. Celebrating a day for mothers solely and tributing everything to the person who will love you the most ever in your entire life is one of the greatest things you can do for that person, for your mother. However, Anna Jarvis’ initiation of establishing a Mother’s Day in the world didn’t have such positive and appreciative thoughts when the campaign was introduced. In 1908, the government of the US, the Congress, rejected the idea of initiating the campaign, taking it further as a joke and claiming that if they agreed to set in a day like that, more like a day for mothers-in-law will also come up in line. This surely didn’t amuse Anna at all as after three years of utmost dedication and hard work to finish what she started, the US government established Mother’s Day to be on the second Sunday of May every year in 1911.

---
## [tremes/api-1](https://github.com/tremes/api-1)@[5b82635ef1...](https://github.com/tremes/api-1/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Monday 2022-05-09 09:00:56 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [FeenieRU/Skyrat-tg](https://github.com/FeenieRU/Skyrat-tg)@[a0fa5ba3ce...](https://github.com/FeenieRU/Skyrat-tg/commit/a0fa5ba3ce25d019dafa88e1d606e079f7649cc6)
#### Monday 2022-05-09 09:27:13 by SkyratBot

[MIRROR] Updates Maps And Away Missions MD [MDB IGNORE] (#13095)

* Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

* Updates Maps And Away Missions MD

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [pb00068/Stockfish](https://github.com/pb00068/Stockfish)@[cb9c2594fc...](https://github.com/pb00068/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Monday 2022-05-09 10:25:27 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [GetComponents/Catflife](https://github.com/GetComponents/Catflife)@[0fa986c6d0...](https://github.com/GetComponents/Catflife/commit/0fa986c6d02db3f755d24f3061727dcabe3f3cdc)
#### Monday 2022-05-09 12:06:54 by Jan Pluschkell

Implemented Tims shit bitch fuck + UI render layer

---
## [nbyavuz/postgres](https://github.com/nbyavuz/postgres)@[c40ba5f318...](https://github.com/nbyavuz/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Monday 2022-05-09 13:33:49 by Tom Lane

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
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[cd1b891d79...](https://github.com/GoblinBackwards/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Monday 2022-05-09 15:08:57 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [erisly/misskey](https://github.com/erisly/misskey)@[4cd8928afa...](https://github.com/erisly/misskey/commit/4cd8928afa9faf1778be13998d064e92febd6643)
#### Monday 2022-05-09 16:25:20 by PikaDude

wouldn't it be funny if they ignored their tests

why fucking have them if you just merge shit that always fails

---
## [Mortalitas/GShade-Presets](https://github.com/Mortalitas/GShade-Presets)@[dcdb3bb7d2...](https://github.com/Mortalitas/GShade-Presets/commit/dcdb3bb7d29f1d2a27d5a64c853fe95f2f4d44df)
#### Monday 2022-05-09 17:04:29 by ellie t

MagicBloom.fx flicker bug fix

In some extreme light conditions, mostly at night with a flickering light source nearby lighting up multiple differently colored moving surfaces ie. light reflections lighting up a character (mostly when close up but can happen from further away), the bloom adaptation from MagicBloom.fx will go haywire due to the other settings being pretty aggressive and it'll start making the screen flicker anywhere from "quite a lot" to "a LOT and violently" (pure white screen to very dark and so on).   

Restoring that value to a more sensible value like the default 0.100 instead of the current 1.000 completely fixes that issue for no visible difference since this only affects the speed at which it changes not the change itself.  

The whole preset being taxing already due to being made for screenshots mostly, I don't see a reason for it to require instantaneous transitions for its effects since your framerate will be heavily cut anyways on most systems.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8b3ce39ca0...](https://github.com/mrakgr/The-Spiral-Language/commit/8b3ce39ca0ffd4f60e7f2bc37a8a989d24cc5461)
#### Monday 2022-05-09 17:32:15 by Marko Grdinić

"11:10am. I woke up late today and have been chilling.

Let me start. It is time to start packing away that course. I want to see what HS sculpting is all about. The course by Cane was interesting, but not thorough enough. The stuff by Pavlovich was like reading an encyclopedia. I really need somebody to demo me the proper workflow up front.

11:25am. Maybe it would not be bad to follow this course along. Why don't I do that? It should be good exercise.

11:45am. I do not know why, but it never occured to me to isolate select and then mask out all those parts while I was wondering how to turn polygroups into masks. It is really a pity.

12:05pm. Focus me, let me go through the last video of the first section. It will only start getting more intense from here. Seriously, why not create this helmet? It would be way more impressive than modeling the room. If I could do this, I'd definitely get to the intermediate level with Zbrush. This would put me into a good position for any further poly modeling.

As I said, I do not like the regular styles. If you are going to do booelans, you either need NURBs, or dense meshes like the ones Zbrush supports. Doing a boolean and then spending ages cleaning up only to get a poor result is bullshit.

12:30pm. 5/50. There are about 50 parts each about 12m long in this course. I am done with the intro part, and now it is time for the block out. Let me go for it.

I can only gain by following this course. The biggest gains are always at the start.

Let me stop here so I can have breakfast. I've been starting them too late lately. Hell, even now is late.

So let me take a break. I have the whole day to dedicate myself to this.

1:20pm. Let me do the chores and then I will resume.

1:30pm. Done. Let me resume. Time to start part 5.

1:45pm. He is going to be using trim curve to clean up the extract, but it would be better for me to use the knife curve. It gives a lot better topology and is a better version of rtim in all respects. But rather than clean up like this, it really would be better to just use the smooth groups brush before doing the extract. Well, maybe. Or maybe do the extract, and then knife it into shape. Right now he is just repeating the mask work. Let me watch the video and then I will immitate what he is doing.

Also that is righ - why is he using divisions when he is going to be booleaning?

...It seems he intended to delete lower.

Rather than doing all this, isn't there a polish option he could have used that also preserves the edges? Seriously, he shouldn't be doing it like this and the trimming is changing the angle of the sides unless he is specifically going for that.

1:55pm. Let me make the same piece. These videos might be long, but they are very slowly paced. In terms of actual content, the course by Cane is a lot longer.

2:10pm. Zbrush crashed and took my work with it. At first the knife tool simply stopped working, when I tried putting it close to the mesh it just died.

2:25pm. Done with 5/50. Time for 6.

2:50pm. Focus me, stop posting in the /wip/ thread.

3:10pm. Some of the edges are a tiny bit chipped, but nevermind that.

Now comes the upper half. I wonder how I managed to do the mirror anti symetrically last time?

3:15pm. Enough, let me start 7/50.

3:55pm. Had to take a break. Let me resume.

4:05pm. Let me do the stuff he did in 7 and I'll move to 8.

4:30pm. Let me move on to 8. By accident I put in some stuff on the back of the helmet. I can be absent minded sometimes.

Focus me, let me move on to 8.

4:45pm. Let me do the front plate.

4:55pm. Fuck Zbrush. Why is switching subtools not reacting properly?

5:10pm. Navigating in Zbrush is so damn difficult. Why does pressing right click keep opening up the space menu, what the hell?

I also did that thing again where I somehow switch the pen so masks only in the eraser mode by accident.

5:20pm. https://www.zbrushcentral.com/t/how-to-disable-right-click-menu-answered/313829
> Turn off Preferences>Interface>Navigation>Enable RightClick Popup and store the new configuration by pressing Shift+Ctrl+i.

5:25pm. I've gotten some good results from the hPolish brush. Because of symmetry the knife was not really working out for me. I also did use it to smooth out the cutter bottom. Had I used the smooth brush, it would have wrecked the edges. I really do like hPolish.

Now that I've gotten the above, hopefully navigating will be less annoying. Zbrush's interface can be outright hostile.

At any rate, I am done with the face plate. Let me move on to 9/50. This is a bit fun. I honestly do enjoy this more than box/subdiv modeling.

6:25pm. Wow, I really got into it. I really do like this style. It gives good looking results. Let me have lunch here. I'll want to at least watch part 9 today.

6:55pm. Done with lunch. Let me watch part 9...Oh no wait, I already covered that. Next is 10/50 instead.

You know, instead appoending those cylinders and then resizing them manually which took forever, I should have just used an IMM primitives brush. I did not occur to me to do this. But I did want some practice bringing in other objects so I guess it is fine if I make this mistake at least once.

7pm. I think I'll stop here for the day. No need to start anything else. I had a really good run today. Too bad I did not wake up at 9pm like usual.

Doing things like this is more like how I imagined art would be. I am going to get my fill of Zbrush, then do the rig in Moi.

7:10pm. I am sure that as far as learning art programs goes, I should be done with all of it apart from Zbrush, and if ever Marvelous Designer. I've grasped what Hopscutter are well enough and it does not seem like I need anything else on that front.

7:15pm. I am not sure what I really want from 3d anymore. I guess I'll have my fill of it, and move to grinding 2d. If I am going to get anywhere in 3d, somewhat ironically, I need to stop working on props. What I am doing here with replicating the desk, the monitor and now the rig is too time consuming either way. I could paint a picture of it in 1/10th of the time it takes me to model, texture, set it up in Clarisse, and that is underestimating it.

I am interested in knowing how to model, but not so much in actually doing it.

One plan that has been flashing in my head lately is to use simple models, but to focus my effort on texturing instead. Then I could repaint it by hand to get rid of the awkwarness of that.

7:20pm. This rig for example. I could just make it a box, but do all the details in substance and it would take me a lot less time than what I am trying to do now.

7:20pm. Now that I have some experience, I do not think that 3d is really overlooked as far as 2d art is concerned. But Substance Painter itself might be.

I want to put in more effort into art, just until I am satisfied.

I've been going at it so hard driven by insecurity. Today might be the most standard session in a long while.

Let me just stop it here. I might as well read Fable, reread UQ Holder, finish the last two eps of Magia Record. Unwinding after work is an important part of it. Laziness becomes good at some point. You can't make a single thing your whole life, you need at least a few.

7:25pm. Tomorrow, I should consider pausing a bit and give Moi a try.

One thing Zbrush has shown me is the power of projective cuts. They are unbelievably powerful when it comes to doing art. Moi actually has great support for them too, but if it was not for Zbrush I would not have even thought of using them as my primary modeling tool.

Even though Moi and Zbrush are very different programs, their working styles are actually quite similar

7:30pm. I am going to try waking up tomorrow at 9pm as is usual and get more work done. It is ironic that now that I am actually getting my hands dirty instead of boring myself with tutorials, I start shifting my schedule towards getting up late."

---
## [Wisemonster/goon-flock](https://github.com/Wisemonster/goon-flock)@[bdad398f9e...](https://github.com/Wisemonster/goon-flock/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Monday 2022-05-09 18:33:45 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [BenVillalobos/msbuild](https://github.com/BenVillalobos/msbuild)@[a572dc6b79...](https://github.com/BenVillalobos/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Monday 2022-05-09 18:42:20 by Forgind

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
## [eschnett/Yggdrasil](https://github.com/eschnett/Yggdrasil)@[b1469b44df...](https://github.com/eschnett/Yggdrasil/commit/b1469b44df4c63961a6c0f0387a89ef4ef24aa26)
#### Monday 2022-05-09 19:39:06 by Elliot Saba

[GCCBootstrap_jll] Build using `crosstool-ng` (#4753)

In the beginning, I wanted to compile a nice little standalone `GCC_jll`
that could be hooked together with a `Glibc_jll` and a `Binutils_jll`,
and a `LinuxKernelHeaders_jll`, etc...  That work is sitting in [0] but
bootstrapping is such a giant pain in the neck that I wanted to give up
the complexity of bootstrapping to instead focus on simply building each
product in isolation.  This _vastly_ reduces the amount of work
necessary to get things working, but it introduces a new dependency: we
need a base C compiler and libc that are already compiled for the target
platform.  To be precise, we need a `build -> host` compiler in order to
build a `host -> target` compiler.  We already have one of those for all
of our current platforms, so I could generate `GCC_jll` packages, but
then when we want to add a new platform, we'd be in trouble.  For this
reason, I realized we'll never truly escape the bootstrapping problem.

I thought about reverting back to the bootstrapping configuration we've
had until now, but rebelled at the thought.  Then I discovered
crosstool-ng, and realized that I could separate concerns here: I can
use ct-ng to build a working cross-toolchain for each target, then use
that compiler to do a much simpler build for all of the other
components.  Therefore, I extract the work of getting a bootstrap build
onto crosstool-ng, and then use that to do whatever other builds I want
in the presence of a fully-functional cross-compiler.

This also breaks the need for the initial bootstrap to be quite as
restricted as the target toolchain.  The GCC that we build technically
doesn't need to run everywhere, it just needs to generate code that runs
everywhere.  We can build GCC against glibc 2.19, and then at build time
have it link the code it generates against glibc 2.12.2, and that will
work just fine for BB.  The compiler may be using a newer glibc to run,
but when it builds, it uses whatever glibc is placed within the target
sysroot.  This also means we don't need to do things like build GFortran
as part of our bootstrap; we can build it later, in the simpler build
script.

In principle, we don't actually need a GCCBootstrap for all platforms.
We only need a functional cross-compiler.  Theoretically, we could use
Clang to do the bootstrapping.  But I'm not going to fully embrace that
because I know that compiling Glibc with Clang is a pain, so for
`*-linux-gnu` at the very least, we're not going to attempt that.  On
macOS and FreeBSD however, there is a possibility that we can use Clang
as our "bootstrap compiler" in order to generate the actual GCC_jlls.

[0] https://github.com/JuliaPackaging/Yggdrasil/tree/sf/gcc

---
## [3nws/twint](https://github.com/3nws/twint)@[4b76906c9b...](https://github.com/3nws/twint/commit/4b76906c9b8a0a7787149531ebded1a664c1b1fb)
#### Monday 2022-05-09 20:11:36 by Enes

Revert "I hate my life"

This reverts commit 5a787edc521d1c59eac7e8beb75299d84db82062.

---
## [3nws/twint](https://github.com/3nws/twint)@[976c5b1574...](https://github.com/3nws/twint/commit/976c5b157439e5960f95216c98a4bd24f75924aa)
#### Monday 2022-05-09 20:11:36 by Enes

Revert "Revert "I hate my life""

This reverts commit 4b76906c9b8a0a7787149531ebded1a664c1b1fb.

---
## [xeome/laptopdots](https://github.com/xeome/laptopdots)@[f792894a27...](https://github.com/xeome/laptopdots/commit/f792894a27cbf6f89e9bc7c5661d1c92e3258e2d)
#### Monday 2022-05-09 21:46:39 by xeome

Connection terminated.

I'm sorry to interrupt you Elizabeth, if you still even remember that name. But I'm afraid you've been misinformed. You are not here to receive a gift, nor have you been called here by the individual you assume. Although you have indeed been called.

You have all been called here. Into a labyrinth of sounds and smells, misdirection and misfortune. A labyrinth with no exit, a maze with no prize. You don't even realize that you are trapped. Your lust for blood has driven you in endless circles, chasing the cries of children in some unseen chamber, always seeming so near, yet somehow out of reach.

But you will never find them, none of you will. This is where your story ends.

And to you, my brave volunteer, who somehow found this job listing not intended for you. Although there was a way out planned for you, I have a feeling that's not what you want. I have a feeling that you are right where you want to be. I am remaining as well, I am nearby.

This place will not be remembered, and the memory of everything that started this can finally begin to fade away. As the agony of every tragedy should. And to you monsters trapped in the corridors: Be still and give up your spirits, they don't belong to you.

For most of you, I believe there is peace and perhaps more waiting for you after the smoke clears. Although, for one of you, the darkest pit of Hell has opened to swallow you whole, so don't keep the devil waiting, old friend.

My daughter, if you can hear me, I knew you would return as well. It's in your nature to protect the innocent. I'm sorry that on that day, the day you were shut out and left to die, no one was there to lift you up into their arms the way you lifted others into yours. And then, what became of you.

I should have known you wouldn't be content to disappear, not my daughter. I couldn't save you then, so let me save you now.

It's time to rest. For you, and for those you have carried in your arms.

This ends for all of us.

End communication.

---
## [HotCrossBun030/hcb_funkin_midis](https://github.com/HotCrossBun030/hcb_funkin_midis)@[b526bdf273...](https://github.com/HotCrossBun030/hcb_funkin_midis/commit/b526bdf27358a1fd56d316a4cc30ac671382769b)
#### Monday 2022-05-09 22:00:29 by HotCrossBun030

update to show im not dead!!!

ye

new songs with midis!!!:
- B-Side Philly Nice
- B-Side Roses
- Holy shit dave fnfnt
- Ron (Vs. Ron April Fools Update)
- Manifest
- Expurgation
- Animal
- Detected

updates to older ones:
-Onslaught is now at it's correct BPM. (300BPM)
-Made Bloodshed overall more accurate to the original.

---
## [ArchGryphon9362/climatechange](https://github.com/ArchGryphon9362/climatechange)@[daeebfed5e...](https://github.com/ArchGryphon9362/climatechange/commit/daeebfed5eb3d1f868823ebbca0da014d85b45b2)
#### Monday 2022-05-09 22:46:47 by Lex Nastin

Create Flow For Presentation
This flow will let us set up the presentation, any quizes, etc. It will
have the presentation itself in other words. Also some code cleanup
stuff, but yeah. Also, kinda began filling out the text, button, and
image classes, so yeah. Very limited on time as I have the stupid and
the lazy which are diseases causing you to turn a 3 month project into a
1 week rush. :cry:

---
## [chynwe-bekee/SCOLIOSIS-RESEARCH-AWARENESS](https://github.com/chynwe-bekee/SCOLIOSIS-RESEARCH-AWARENESS)@[4f354a4b3b...](https://github.com/chynwe-bekee/SCOLIOSIS-RESEARCH-AWARENESS/commit/4f354a4b3b5ac820450bc4702f834f701cebc5ed)
#### Monday 2022-05-09 23:16:59 by Chinwenmeri Amalaha

Update README.md

SCOLIOSIS
According to world wide science,Scoliosis is a sideways curvature of the spine. Scoliosis is a sideways curvature of the spine that most often is diagnosed in adolescents. While scoliosis can occur in people with conditions such as cerebral palsy and muscular dystrophy, the cause of most childhood scoliosis is unknown.Cerebral palsy (CP) is a group of disorders that affect a person's ability to move and maintain balance and posture. CP is the most common motor disability in childhood. Cerebral means having to do with the brain. Palsy means weakness or problems with using the muscles while Muscular dystrophy is a group of diseases that cause progressive weakness and loss of muscle mass. In muscular dystrophy, abnormal genes (mutations) interfere with the production of proteins needed to form healthy muscle. There are many kinds of muscular dystrophy. Many sources stated that the cause of scoliosis is unknown, but it is known that it can be from childhood or can affect an adult usually by aging, natural wear and tear or as a result of arthritis that occur in the spine. It is also discovered that this curvature can be treated both in adults or adolescent either by surgery or by observing therapy and avoiding the certain event that reoccurs and cases the shift. Scoliosis affects 2-3 percent of the population, or an estimated six to nine million people in the United States. Scoliosis can develop in infancy or early childhood. However, the primary age of onset for scoliosis is 10-15 years old, occurring equally among both genders.In conclusion,Scoliosis can affect people of any age, gender, race, and from all sectors of the socioeconomic spectrum. With close to seven million people currently living with scoliosis in the United States alone, when you factor in estimates of people living with the condition unaware, plus diagnosed cases from around the world, the number would be even more surprisin and it can be treted actually. The conclusion here will be drawn from the sample of data from orthopedic hospital from a town in the eastern part of Nigeria. It can be concluded that scoliosis is peculiar with  female  and their (parent) occupation has a huge role to play as this something to do with the level of awareness.It is advised that parents should closely watch their kids as they grow to be able to correct it on time and reduce pain their kids will experience as they grow.about 30 percent — require bracing, and an even smaller percent — about 10 percent — of patients actually require surgery. Scoliosis can be treated best on or  before the child hits is 14 years old, but when it has to do with an adult, he/she can still get the required treatment whether surgically or with the use of braces.

---

