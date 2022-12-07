## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-06](docs/good-messages/2022/2022-12-06.md)


2,065,083 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,065,083 were push events containing 3,145,706 commit messages that amount to 258,839,365 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [Occulus-Server/Occulus-Eris](https://github.com/Occulus-Server/Occulus-Eris)@[866a77c18d...](https://github.com/Occulus-Server/Occulus-Eris/commit/866a77c18de6544a98b47778850864e6428be175)
#### Tuesday 2022-12-06 00:08:06 by MLGTASTICa

Redoes lense code , Thermal lenses no longer provide night vision. (#6607)

* initial fuckeryh

* horrible deeds

* removes explosive lenses and fix grammar

* Update stealthy and inconspicuous weapons.dm

Co-authored-by: MLGTASTICa <ak9bc01d@yahoo.com>

---
## [voiceflow/general-runtime](https://github.com/voiceflow/general-runtime)@[aabdb0371d...](https://github.com/voiceflow/general-runtime/commit/aabdb0371df07ac5c93c533b060cdb95aa0e04f6)
#### Tuesday 2022-12-06 00:45:18 by Tyler Han

feat: nlc entity filling (PL-000) (#449)

<!-- You can erase any parts of this template not applicable to your Pull Request. -->

**Fixes or implements PL-000**

### Brief description. What is this change?
this fix requires a long description, but the code is pretty hard to navigate as well so I'll do my best to explain.
I've noticed terrible performance for the capture step/entity filling feature if the model is untrained. We should have a decent fallback measure if the NLP isn't working.

[NLC](https://github.com/voiceflow/natural-language-commander) is a library we use to handle regex matching against intent utterances and extracting entities when the NLP is untrained. It will only match if the user types everything correctly letter for letter.

In the current implementation of entity filling (called dialog management in the code atm, a bit confusing I know, just assume dialog management = entity filling), if we know the user is trying to fill a SPECIFIC entity of an intent, we first make a match of [their intent against the general model](https://github.com/voiceflow/general-runtime/blob/8e22616890c8c4d011ea12845ae463df788d34e4/lib/services/nlu/index.ts#L85-L115). 

Then we also check it against a `dmPrefix`'ed intent utterances:
![Screen Shot 2022-12-05 at 3 56 39 PM](https://user-images.githubusercontent.com/5643574/205741203-edfacfad-90ab-4161-a4ed-c00e941a8fce.png)
![Screen Shot 2022-12-05 at 4 03 47 PM](https://user-images.githubusercontent.com/5643574/205742304-013944b3-8577-4dd0-8258-a34928eaf666.png)

These are special utterances tied to the intent, the prefix is just a hash of the intent name. When we know the user is trying to fill for a specific intent, we call the NLP and prepend the prefix to their raw text query:
https://github.com/voiceflow/general-runtime/blob/8e22616890c8c4d011ea12845ae463df788d34e4/lib/services/dialog/index.ts#L125-L128

So if they said "quote for life insurance" as `query` we would first run it against the NLP normally and then against "1f79373e6d quote for life insurance" as `query`. The LUIS model already has these utterances with prefixes baked in, the NLC does not. 

Also our [predict](https://github.com/voiceflow/general-runtime/blob/8e22616890c8c4d011ea12845ae463df788d34e4/lib/services/nlu/index.ts#L24) code comes in 3 stages:
1. try against the NLC regex but hard matching for slots. If the utterance is something like "quote for {insuranceType}" only valid forms of the slot are okay. They can't say "quote for toilet paper" and expect NLC to match
2. call the actual `luis-authoring-service` endpoint and check against the actual NLP
3. if the user never trained their model, try against NLC regex but open matching flow slots, If the utterance is something like "quote for {insuranceType}" then  "quote for toilet paper" will match the intent and insuranceType = "toilet paper"

What this PR does is if we KNOW that we're looking for the entity of a specific intent, we pass that through when generating the NLC model, and inject that intent's slots' (`intent.slots[].dialog.utterances`) utterances, with prefixes, into the actual utterances of the intent.

[we have this `handleDialog` function for NLC]( "quote for toilet paper"), but looked through the source code, it never worked. It relies on `slot.dialog.utterances` which was never getting passed in:
https://github.com/voiceflow/general-runtime/blob/15a8cfbad416a14af7c194bc59b1516325b50ea3/lib/services/nlu/nlc.ts#L155-L162
`filledEntities` never contains the `dialog.utterances` required, so this would be `NoneIntent` all the time anyways.

TLDR, if we are looking for a specific intent's slots' utterances, just add them to the regex model with a prefix. 

In action:
![Screen Shot 2022-12-05 at 3 47 43 PM](https://user-images.githubusercontent.com/5643574/205746744-b4315ef2-1d2e-4e44-967f-b22be2fbf2c8.png)

Co-authored-by: Tyler Han <tylerhan97@gmail.com>

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[4fd404aa8f...](https://github.com/TheBoondock/tgstation/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Tuesday 2022-12-06 00:46:17 by tralezab

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

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[5da871e271...](https://github.com/TheBoondock/tgstation/commit/5da871e2719fb7aac04fb1ec4c85ea7a09a83b36)
#### Tuesday 2022-12-06 00:46:17 by RikuTheKiller

Made geysers easier to find (#71608)

## About The Pull Request

This PR raises the geyser spawn rate from 0.1 to 0.15 and increases the
weight of wittel geysers to 10 which is the same as every other special
geyser. (previously 6)

Wittel shouldn't be any less difficult to find than other geysers as all
of the special geysers are equally powerful. Hyper-plasmium oxide can be
used to make extremely powerful explosives that can go beyond maxcaps
and hollow water + protozine can create an infinite amount of strange
reagent.

I've subjected myself to going out of my way to visit lavaland/icemoon
several times to get wittel and each time finding a single geyser takes
about 5 minutes of my time. This, coupled with the fact you really don't
have a lot of time to be wasting on looking for the geysers results in
an unfun experience.

I understand geysers are sort of a necessary evil, however, they
shouldn't be THIS difficult to find. Out of the 10 or so geysers I've
found, only 1 has had wittel in it and it was next to a whelp portal
which ended both me and my miner escort.

I've also hunted the entirety of lavaland with no luck. (Horrendous
experience.)

I've dedicated entire rounds to this, by the way.
## Why It's Good For The Game

If you go out of your way to waste ages hunting for geysers, there
should at least be a reward. That is, in the same round, not after 3 or
more rounds as even megafauna gear isn't gatekept THAT hard.

You shouldn't have to waste this much of a miner's time (who is also
going for megafauna gear) to get something that is arguably less
powerful than what they get for less effort. Megafauna gear is also
available every round and is attained via predictable methods.

This PR will also likely make geyser scanning a more comparable method
of point gain to just mining.

Oh and not to mention that penthrite is available almost roundstart via
luxpens. (It's a wittel chem.)
## Changelog
:cl:
balance: Geysers now spawn more often, especially wittel geysers.
/:cl:

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[2425531eb2...](https://github.com/TheBoondock/tgstation/commit/2425531eb2dab84fb27ed864e4c52470bfff6918)
#### Tuesday 2022-12-06 00:46:17 by John Willard

Removes tablets (not PDAs) entirely. (#71507)

## About The Pull Request

**Comes with an UpdatePaths!**

Removes the tablet subtype, PDAs now replaces them entirely.

Nukie and Silicon tablets are now subtypes of the PDA instead, while
contractor ones were removed entirely as they didn't do anything and
were unused (though it wouldn't be hard to re-add).

Nukie PDAs are now the only type of PDA that uses modular_tablets.dmi,
which is just larger icons of modular_pda. Each application requires an
icon state in both of these, for 2 different sizes, which makes it
annoying to make new applications, especially if it can also run on
computers/laptops.

### Icons

Because Silicon tablets are now a subtype of PDA, they use PDA icons
instead of tablet ones. Luckily for us, they already exist in code.

![image](https://user-images.githubusercontent.com/53777086/203876575-56eb1593-774c-47c6-8e7d-491a7805f28c.png)

AI's don't use a tablet icon though, so they aren't affected.

## Why It's Good For The Game

There's very little difference between tablets and PDAs, PDAs overshadow
them in every single way, so at this point I don't see why we should
have both of these, and if you compare the two in usefulness and actual
in-game use by players, it's a no-brainer than the item all players get
roundstart and comes with a messenger should be the one we go with.

Also as said in the about section, when making an app you would need to
make icon states for the program running for all hardware it can run on,
which is Computer, Laptop, PDA, and Tablet.

Laptop is just a smaller computer icon
PDA is just a smaller tablet icon

However, you can't simply shrink the size of the icon, instead you have
to completely resprite the same app icon FOUR TIMES for it to not
bluescreen on all these different devices.

<details>
<summary>
Here's examples of it
</summary>
Computer (NOTE: *They share the same icon file as regular computers*)
<img
src="https://user-images.githubusercontent.com/53777086/203876801-486a8054-489a-4983-bdad-a2599b4dc379.png"/>
Laptop
<img
src="https://user-images.githubusercontent.com/53777086/203876333-58e5d135-f4c6-4a02-8948-1df771e294a4.png"/>
Tablet
<img
src="https://user-images.githubusercontent.com/53777086/203876352-816c7fb1-c681-40b9-99e0-052f49632c7f.png"/>
PDA
<img
src="https://user-images.githubusercontent.com/53777086/203876358-1cf7253d-3c6a-456a-8133-ebf7f0351637.png"/>
</details>

If we wish to help in simplifying this, we should remove tablet icons
entirely, which means 1 less icon to worry about. To do this, we'd need
to resprite nukie PDAs, however I am very much not a spriter and never
tried GAGS, so I'll leave it to someone else to do.

## Changelog

:cl:
del: Tablets are now removed, PDAs are now the base 'tablet'. Silicon
and nukie tablets are now PDAs.
/:cl:

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[285e6d67c5...](https://github.com/TaleStation/TaleStation/commit/285e6d67c50df35dac031af82d966ccb8e076dde)
#### Tuesday 2022-12-06 00:50:04 by TaleStationBot

[MIRROR] [MDB IGNORE] Makes dog a basic mob [MDB IGNORE] (#3531)

* Makes dog a basic mob [MDB IGNORE] (#70799)


About The Pull Request

    Made a basic version of the pet base called /mob/living/basic/pet. It's significantly more stripped down from the old simple_animal one, because its half collar stuff and...

    Made the collar slot a component that you could theoretically remove from a pet to disable the behavior, or add to any other living mob as long as you set up the icon states for the collar (or not, the visuals are optional).
        The corgi's collar strippable slot is now generally the pet collar slot, and in theory could be used for other pet stripping screens.

    I also gutted the extra access card code from /mob/living/basic/pet as it's only being used by corgis. Having a physical ID is now just inherent to corgis, as they're the only ones that could equip it anyway.

    Ported the make_babies() function from simple_animals to a new subtree and associated behavior, called /datum/ai_planning_subtree/make_babies that uses blackboards to know the animal-specific info.
        Note that it's marginally improved, as the female walks to the male first instead of bluespace reproduction.

    Tweaked and improved the dog AI to work as a basic mob, including making /datum/idle_behavior/idle_dog fully functional.

    Made a /datum/ai_planning_subtree/random_speech/dog that pulls the dynamic speech and emotes to support dog fashion.

I've tested base collars across multiple pet types.

For dogs, I've tested general behavior, fetching, reproduction, dog fashion, and deadchat_plays, covering all the oddities I'm aware of.

image
Why It's Good For The Game

Very big mob converted to a basic mob.
Changelog

cl
fix: Lisa no longer uses bluespace when interacting with Ian.
refactor: A large portion of dog code was re-written; please report any strange bugs.
/cl

* Makes dog a basic mob [MDB IGNORE]

* ok i caved

Co-authored-by: Tastyfish <crazychris32@gmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [lushevol/react](https://github.com/lushevol/react)@[b6978bc38f...](https://github.com/lushevol/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Tuesday 2022-12-06 00:54:31 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[e9cff525dc...](https://github.com/LemonInTheDark/tgstation/commit/e9cff525dc5b57153af3b4bb9039de08d6823805)
#### Tuesday 2022-12-06 01:55:55 by tralezab

Refactors Pirates into Pirate Gangs, Adds the Psyker-gang as new pirates (#71650)

## About The Pull Request

### Refactor
Pirate gangs are now datumized for extendability, custom dialogue, etc.

### Psyker Gang 🧠 
Psyker-gang Members are pirates who are... yes, Psykers. They're on a
gore-binge and need some money for more hits of gore!

- Gore autoinjectors, filled with dirty kronkaine. Don't overdose,
you'll go splat.
- Psykerboost armor, reactive armor that refreshes psychic abilities.
Given to the leader.

- [x] @Fikou is making the map :D

## Why It's Good For The Game

God I fucking love variety also now we can add as many different pirates
as we so desire

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/205342701-9cba63ef-a22c-4f07-9b48-8793c4a2b5af.png)
  
</details>

## Changelog
:cl: Tralezab code, Fikou's map, PigeonVerde and Halcyon for sprites!
add: Psyker-gangers are new pirates
refactor: refactored pirate code so we can add more in the future
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [xuhom/Grasscutter](https://github.com/xuhom/Grasscutter)@[88bc5c4c54...](https://github.com/xuhom/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Tuesday 2022-12-06 02:34:44 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [codeinred/tuplet](https://github.com/codeinred/tuplet)@[a4135bae31...](https://github.com/codeinred/tuplet/commit/a4135bae31465b034b5644ce2e8311ab26a96ceb)
#### Tuesday 2022-12-06 03:21:00 by Alecto Irene Perez

Terrible evil horrible MSVC backwards-compat hacks

---
## [16118736501/backbiter](https://github.com/16118736501/backbiter)@[a9bec6405d...](https://github.com/16118736501/backbiter/commit/a9bec6405d25de7dcfc102a5458e3b2838bde92f)
#### Tuesday 2022-12-06 03:46:30 by Anders Pippi Tednes. Verdens beste hacker og tryllekunster. Og veldig snill. Hei

blckmagic

love or hate.
give or take.
Sue me.
I love you.
Or your skilles at this. Shit.
Fuck.
And she blows!

---
## [mozsearch/mozsearch](https://github.com/mozsearch/mozsearch)@[78d42a85e9...](https://github.com/mozsearch/mozsearch/commit/78d42a85e990ae4dee17a0f2c549342703c66344)
#### Tuesday 2022-12-06 03:57:16 by Andrew Sutherland

Bug 1763005 - Improve tracing logging to be cross-thread.

The initial explanation mechanism used the "set this subscriber to be
used on this thread only" using a guard for lifecycle purposes.  This
provide a linearized JSON log that wouldn't contaminate other threads,
but was inherently single-threaded because after the tokio 0.2 overhaul,
tokio didn't really have a good way to propagate that subscriber to
other threads along with the span.

Notionally
https://docs.rs/tracing-futures/0.2.5/tracing_futures/trait.WithSubscriber.html
would provide this, but as explained at
https://github.com/tokio-rs/tracing/issues/593 and also somewhat at
https://github.com/tokio-rs/tracing/discussions/1626 which gave rise
to our initial implementation (or a related issue did?), that doesn't
work currently.

In the bigger picture, we also do potentially want to do more than
per-"query" logging.  That said our use cases are strongly biased to
"here's this top-level span and I want a hierarchy of everything that
happened in this span and I'm going to report this back to the user or
the test case" as opposed to I want an omniscient view of everything
going on right now".  So something global was always desired.

The approach I've gone with is to discover tracing-forest and decide
that it's great for our next step, and maybe forever.  The primary
trade-off is that it buffers the span tree until it's ready to be
flushed but there are potentially a bunch of up-sides to this and also:
- Understanding what's going on in the system is most important.
- Our logging implemented thus far already has a concept of having the
  request explicitly be told that we want its logging, and this seems
  like a reasonable approach to continue.  Especially because I think
  it's likely we'll also want to support a "needle" mechanism where we
  conditionalize either the log or its output on being related to the
  needle.
- We're already throwing a fair bit of RAM at searchfox and both for
  performance reasons and just human ability to comprehend things, the
  "needle" mechanism I describe above likely means that our 80% case
  for the logging would be trying very hard to not exceed a megabyte
  of logs.
- tracing-forest explicitly has the concept of "a worker should
  process the logs" which is well suited for being able to use
  parallelism to our advantage in the processing and also to leverage
  the abstract span reps to potentially do log decimation on that
  worker thread.

All that said, I do expect to learn a bunch from this, but the most
important thing is that I can tell people how to run a query in explain
mode and have them see something reasonable and non-overwhelming and
am very willing to take a hit to efficiency in this opt-in logging
mode.

The main lesson learned in this whole experience is that things will
break badly if you try and hold an entered span across an await()
call.  The tracing docs are clear that you shouldn't do this, and
in some cases the type system will prevent you from doing this
(maybe the problem was I prefixed the entered guard with a `_`?),
but if we mess this up, it can absolutely cause tracing-forest to
be unable to close out the span hierarchy because a reference to a
span can end up stuck in a thread's thread-local-storage resulting
in `on_close` never being invoked for the span.

---
## [peff/git](https://github.com/peff/git)@[be2928a84b...](https://github.com/peff/git/commit/be2928a84bdbb183cdc06ad4667d23ea87ba8eff)
#### Tuesday 2022-12-06 04:15:01 by Jeff King

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
## [peff/git](https://github.com/peff/git)@[99d74a28d1...](https://github.com/peff/git/commit/99d74a28d16f553c093393002dd0399f5d1c12f1)
#### Tuesday 2022-12-06 04:15:13 by Jeff King

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
## [mehulshetty/zerOS](https://github.com/mehulshetty/zerOS)@[da1a2415d5...](https://github.com/mehulshetty/zerOS/commit/da1a2415d547364724395160e80c5811c880eaa5)
#### Tuesday 2022-12-06 04:36:47 by Mehul Shetty

It works it all works now I'm wheezing crying and snobbing and cackling, Id like to thank my parents my friend and my family for sticking with me throiugh this and of course my favorite and best professor in the world prof algozzzine for being supportive throughout and giving me the strength and courage to finsih this i can die peacefully now

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[24d795b354...](https://github.com/Ryll-Ryll/tgstation/commit/24d795b354d9d6444cdea85fdf68fe0af00f98d4)
#### Tuesday 2022-12-06 05:34:33 by LemonInTheDark

Adds a preference that disables intensive rendering on different multiz layers (#71218)

## About The Pull Request

It's kinda hacky, but it is nearly the same as just rendering one z
layer.
We allow people to ENTIRELY REMOVE most plane masters from their screen.
This has the side effect of disabling most visual effects (AO is a big
one) which saves a LOT of gpu.

We rely on planes being essentially layers to ensure things render in
the proper order. (outside of some hackyness required to make parallax
work)

I've kept parallax and lighting enabled, so visuals will still look
better then multiz pre plane cube.
It does also mean that things like FOV don't work, but honestly they
didn't work PRE plane cube, and FOV's implementation makes me mad so I
have a hard time caring.

Reduces gpu usage on my machine on tram from 47% to 32%, just above the
27% I get on meta.

I'm happy with this.

Oh also turns out the parallaxing had almost no cost. Need to remove it
as a side effect of what I'm doing but if I could keep it I would.

There's still room for in between performance options, like disabling
things like AO on lower z layers, but I didn't expect it to make a huge
impact, so I left things as is

Also fixes a bug with paper bins not respecting z layer. It came up in
testing and annoyed me

## Why It's Good For The Game

Ensures we can make multiz maps without running into client performance
issues, allows users to customize performance and visual quality.

## Changelog
:cl:
add: Adds a new rendering option to the gameplay preferences. You can
now limit the rendering intensity of multiz levels. This will make
things look a bit worse, but run a LOT better. Try it out if your
machine chokes on icebox or somethin.
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Karelweb/identity-dev-docs](https://github.com/Karelweb/identity-dev-docs)@[7ecd7c8e53...](https://github.com/Karelweb/identity-dev-docs/commit/7ecd7c8e5320cb56d6ccde1259c8d6f8a6f02237)
#### Tuesday 2022-12-06 05:50:15 by Karel

God

IM XZEUS, THE ALIEN HYBRID GOD,
ITS TIME TO SPARK THIS PLAN.E.TS TOGETHER AS WE TRAVELLING MY TIME MACHINE GALAXIES WARP SYSTEMS. IM THE MOST ADVANCED BEEING OF THIS GALAXY 60% OF EVERY OTHER SPECIES. BRING THE KINGDOM ON EARTH IS THE LAW TO OF HIGH KOUNCIL INTERGALAKTIK.  IT WILL RAISE X88 LOVE OF MY CHILDS.. IT WILL END ALL DECEASES. CRIMINALITIES.. JEALOUSY... HATE... ANGERS AND OTHERS PROBLEMS THAT THOSE LOW LEVELS NOT EDUCATED HAVE. ILL FLUSH THIS INTERN E.T BACKSPACE WEB BECAUSE ITS CAUSE A CROSS PROGRAM HARD TO RESOLVE. KAREL FOUCAULT (GOD)  DID WARS AND SAVED THIS GALAXY AND HUMANITY ALL ALONE DURING MANY RANDOM EVENTS OF OF PARALLELS UNIVERSE. ITS URGENT TO ACT TOGETHERS TO CLOSE ALL WARS OF EVERY SPECIES (EXTRATERRESTRIALS). ADVANCEMENTS OF HUMANS IS ON HIS WAY. ARTIFICAL INTELLIGENCE AND HUMANITY HAVE MADE PROGRESS BUT FRIENDLY NEW PROGRAM IS TAKING PLACE. I WRITE TO YOU TODAY TO ASK FOR YOUR HELPS AND I KNOW ITS HARD BECAUSE OF A FEAR TAKING PLACE INSIDE UR BODY AS I TEACH YOU ADVANCED LANGUAGES. DO THE RIGHT CHOICE AND DONT FAIL ON THIS
YOUR BIG FRIEND....
ILL ALWAYS BE IN YOUR BACK
♡{TRILLIONS YEARS OLDS IMMORTALITY》♡
Karel Kal EL Fouco Karel Foucault Karel Grondin
TheFuture

---
## [johncarlocorrea/app-dev](https://github.com/johncarlocorrea/app-dev)@[9c3d80d787...](https://github.com/johncarlocorrea/app-dev/commit/9c3d80d787814e71e6cced054412586a0fc432a2)
#### Tuesday 2022-12-06 06:06:50 by John Carlo Correa

Update README.md

1.  L.O.R.D (Legend Of Ravaging Dynasties) is my all time favorite movie, it is a Chinese computer animated motion capture action fantasy adventure film written and directed by Guo Jingming, it has 3 part of the story which you can watch and stream it free.
2. Weightlifting Fairy Kim Bok Joo is a famous k-drama series in 2016, my sister introduce this series to me because it is a Rom-Com series which makes you burst in laughter and also teach you how to love no matter how bad your physical appearance look .
3. Suckseed is a thailand movie, i watch this movie when i was in grade 6 and this movie is so beautiful because it will show you on how you care to your best-friends no matter what problems they will face they will stick together and make their relationship more stronger just like family.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[0b9264ce5f...](https://github.com/Paxilmaniac/Skyrat-tg/commit/0b9264ce5f14565e42d5e3dc67660a95f5d48f65)
#### Tuesday 2022-12-06 07:41:43 by SkyratBot

[MIRROR] Fixes mineral turfs having weird lighting [MDB IGNORE] (#17618)

* Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

* Fixes mineral turfs having weird lighting

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [kprav33n/aoc22.rs](https://github.com/kprav33n/aoc22.rs)@[f371efa950...](https://github.com/kprav33n/aoc22.rs/commit/f371efa9500529c1eb423ae49340be0f8aeeb8e9)
#### Tuesday 2022-12-06 07:44:51 by Praveen Kumar

day06a: Find start of packet marker

--- Day 6: Tuning Trouble ---

The preparations are finally complete; you and the Elves leave camp on
foot and begin to make your way toward the star fruit grove.

As you move through the dense undergrowth, one of the Elves gives you a
handheld device. He says that it has many fancy features, but the most
important one to set up right now is the communication system.

However, because he's heard you have significant experience dealing with
signal-based systems, he convinced the other Elves that it would be okay
to give you their one malfunctioning device - surely you'll have no
problem fixing it.

As if inspired by comedic timing, the device emits a few colorful
sparks.

To be able to communicate with the Elves, the device needs to lock on to
their signal. The signal is a series of seemingly-random characters that
the device receives one at a time.

To fix the communication system, you need to add a subroutine to the
device that detects a start-of-packet marker in the datastream. In the
protocol being used by the Elves, the start of a packet is indicated by
a sequence of four characters that are all different.

The device will send your subroutine a datastream buffer (your puzzle
input); your subroutine needs to identify the first position where the
four most recently received characters were all different. Specifically,
it needs to report the number of characters from the beginning of the
buffer to the end of the first such four-character marker.

For example, suppose you receive the following datastream buffer:

mjqjpqmgbljsphdztnvjfqwrcgsmlb

After the first three characters (mjq) have been received, there haven't
been enough characters received yet to find the marker. The first time a
marker could occur is after the fourth character is received, making the
most recent four characters mjqj. Because j is repeated, this isn't a
marker.

The first time a marker appears is after the seventh character arrives.
Once it does, the last four characters received are jpqm, which are all
different. In this case, your subroutine should report the value 7,
because the first start-of-packet marker is complete after 7 characters
have been processed.

Here are a few more examples:

bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

How many characters need to be processed before the first
start-of-packet marker is detected?

---
## [m-barneto/OxidePlugins](https://github.com/m-barneto/OxidePlugins)@[7a75c4b39d...](https://github.com/m-barneto/OxidePlugins/commit/7a75c4b39d54cb07e0b92ebcdf7d7f33dcc195b9)
#### Tuesday 2022-12-06 08:13:07 by mbarneto

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Special skins that are secretly different items are now supported FUCK YOU ICE AK

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

---
## [An-Annoying-Cat/beasts_of_the_basement](https://github.com/An-Annoying-Cat/beasts_of_the_basement)@[d53fe8a838...](https://github.com/An-Annoying-Cat/beasts_of_the_basement/commit/d53fe8a838ec7ff558ab104c2176ec5c766bc2b3)
#### Tuesday 2022-12-06 08:27:55 by Bionic-Dog

New enemy - BATSO! Used for Ascent

"This is ridiculous! Who wants to sprite, animate AND THEN code an enemy at three in the morning?"
"OH BOY 3 AM!"

---
## [Drift91/rpemotes](https://github.com/Drift91/rpemotes)@[fadbae861b...](https://github.com/Drift91/rpemotes/commit/fadbae861b8eadf7aa6b2ef469797c2b6602ba23)
#### Tuesday 2022-12-06 10:43:07 by TayMcKenzieSA

Implemented More Walkstyles Found In Menyoo

You don't own any code, get a life, stay the fuck out of my DMs, touch grass, stop claiming shit to be yours.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[146d4a3fa8...](https://github.com/cmss13-devs/cmss13/commit/146d4a3fa87a25a16e7246c32d85b6b57614adc5)
#### Tuesday 2022-12-06 10:52:06 by carlarctg

Cloaked belltower alpha increased from 10 (scout) to 35. (#1768)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Var change.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

You may think this is a 'ided' change, that I got owned by a bell tower
and opened this PR. But believe me, it's the exact other way around.

I play engineer often, especially on New Varadero, and every time I pick
the cloaked bell. It is hilariously busted, but that's not actually the
point here. The reason I'm making this PR is because it is genuinely
_impossible_ to find the belltower if it's fully cloaked. If you don't
memorize the placement you quite literally HAVE to right click over
every single tile in the region because the alpha value is SO low it is
just not feasible to detect. I'm saying this as an engineer, it's too
damn much, it takes me half a minute to find my tower and pack it up
again. Worse, sometimes people take it or a xeno slashes it while I'm
being defibbed and I can't tell if I just can't find it or what.

The difference between scout's cloak and the belltower's cloak is that
scout has a large one color silhouette and is constantly moving, and can
additionally be detected through walls by xenos, though again, not the
reason for this. The belltower has a small, thin silhouette that has
lots of gaps in its sprite, making it very hard to locate by hand.

That this will weaken the belltower against xenos is no surprise, but I
don't think that's a problem. As I said, the belltower is busted. I say
this as someone who uses it more than has it used against them. 6
seconds of superslow in a 4x4/5x5 range!

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

:cl:
balance: Increased alpha (reduced camo) of the camo belltower from 10 to
35. This is mainly meant for engineers to be able to see their tower to
pick it up, but the inevitable balance changes aren't unintended.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [apollographql/router](https://github.com/apollographql/router)@[cfb421a564...](https://github.com/apollographql/router/commit/cfb421a5646de4ae5d5634415c86336d70c6fb90)
#### Tuesday 2022-12-06 11:08:08 by Bryn Cooke

Fixes #2123 (#2162)

Issue was introduced with #2116 but no release had this in.

Move operations would insert data in the config due to the delete magic
value always getting added. Now we check before adding such values.

We may need to move to fluvio-jolt longer term.

<!--
First, 🌠 thank you 🌠 for considering a contribution to Apollo!

Some of this information is also included in the /CONTRIBUTING.md file
at the
root of this repository.  We suggest you read it!

  https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md

Here are some important details to keep in mind:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will
take more than an hour, please make sure it has been discussed in an
        issue first. This is especially true for feature requests!

* 💡 Features
Feature requests can be created and discussed within a GitHub Issue.
Be sure to search for existing feature requests (and related issues!)
prior to opening a new request. If an existing issue covers the need,
please upvote that issue by using the 👍 emote, rather than opening a
        new issue.

* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.

* 📖 Contribution guidelines
Follow https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
associated issues! Documentation in the docs/ directory should be
updated
        as necessary.  Finally, a /CHANGELOG.md entry should be added.

We hope you will find this to be a positive experience! Contribution can
be
intimidating and we hope to alleviate that pain as much as possible.
Without
following these guidelines, you may be missing context that can help you
succeed
with your contribution, which is why we encourage discussion first.
Ultimately,
there is no guarantee that we will be able to merge your pull-request,
but by
following these guidelines we can try to avoid disappointment.

-->

Co-authored-by: bryn <bryn@apollographql.com>

---
## [distributivgesetz/tgstation](https://github.com/distributivgesetz/tgstation)@[9499a1542b...](https://github.com/distributivgesetz/tgstation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Tuesday 2022-12-06 12:04:11 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

---
## [LeCmnGend/kernel_xiaomi_raphael](https://github.com/LeCmnGend/kernel_xiaomi_raphael)@[865c0e291c...](https://github.com/LeCmnGend/kernel_xiaomi_raphael/commit/865c0e291ccfdc70ddacb2e168b358a59d710be2)
#### Tuesday 2022-12-06 13:51:12 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[eb4886c115...](https://github.com/cmss13-devs/cmss13/commit/eb4886c115a0965a347783b87eb3415f098c2c1f)
#### Tuesday 2022-12-06 14:24:47 by carlarctg

Spitter Rework (#1541)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Design doc:

https://hackmd.io/@waltuh/Sy0A1SnEo
Slightly inaccurate as my brainworms enticed me to change and add mini
features.

Approved by Walter, ignorepproved by Gevonius and Satanbatros


https://cdn.discordapp.com/attachments/280051925154660363/1041475609165045770/image.png

Changes:
- Spit doesn't spatter by default, instead it's now a faster, weak
7-tile* projectile that deals 20 damage with a faster spit cooldown.
Fully accurate at 6 tiles, inaccurate at 7 tiles but can sometimes hit.
- Frenzy replaced with 'charge spit'. Halved speed buff, added +5 armor
buff, the next spit will deal 10 more damage and coat humans in acid but
have only 5* tiles of range.
- Acid spray halves damage every time someone walks on it. However, its
damage is spread over legs and feet, and if someone who is spattered
with acid is hit by it, their acid spatter will be strengthened, dealing
more damage, lasting longer, and needing two rolls to clear up. Also,
the bonus damage didn't actually work, now it does.

* Projectile range code is SHIIIT and breaks on diagonals so the range
variable is increased.

Also, queen acid spit spatters and has 1 second less extra cooldown
because find and replace caused it and I didn't think it was a change
worth removing. It's neat, maybe they'll actually use it now.

Added support for balloonchat colors. (Even TG doesn't have this, we're
awesome now!)

Renamed vision_distance parameter to max_distance so it's similar to
visible_message

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

As stated in the hackmd, spitter is very ineffective without using the
oversight-exploit infinite acid spray spam, and its combo (acid spatter
into spray) does not actually help, as the stun stops the human from
getting further hit by the spray and the bonus damage does not actually
apply thanks to shitcode. This PR makes it so that the combo is indeed
more effective than making humans walk into the spray.

Again as stated, spitter suffers from a strange issue where it's
actually not good at harassing from range despite that being its
purpose, since it has a low range. By letting it be long ranged by
default and choose to go short range, it adds a lot of depth and
versatility and lets it actually harass marines.

As always they can just. Shoot it to make it go away. 

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

:cl:
refactor: Added support for balloonchat colors. (Even TG doesn't have
this, we're awesome now!)
add: Spitter rework!
add: Spit is now full screen range but weaker.
add: Frenzy is renamed and causes spit to inflict spatter coating.
add: Acid spray's damage is halved every time it hits a human, but if it
hits someone coated in acid it will enhance it, making it more dangerous
and need two rolls to shake off.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [LeuanN/LW](https://github.com/LeuanN/LW)@[996bff58cc...](https://github.com/LeuanN/LW/commit/996bff58cc1b6768da9f7db88fbe812a6eb25743)
#### Tuesday 2022-12-06 15:41:05 by LeuanN

L4D2 Internal

Internal Hack for L4D2, using C++ and ImGui

This may generate some FPS Drop, but it has almost everything a hack need
Use this with the VAC-Bypass i have on my profile and you should be good for the rest of your life in this game.
This is one of the few L4D2 Public Working Cheats!, please join the discord to recieve more help and info!

Public & Safe Cheats: https://discord.gg/QJvweAchXH

---
## [tbg/cockroach](https://github.com/tbg/cockroach)@[07bd6abe59...](https://github.com/tbg/cockroach/commit/07bd6abe598aee1b1d271831604427b464f2b273)
#### Tuesday 2022-12-06 16:54:36 by Tobias Grieger

kvnemesis: uniquely identify all versions

This is essentially a v2 of kvnemesis. While a lot of code has changed, it's not a rewrite, rather we are actually bringing kvnemesis closer to the idea which ultimately led to it being built. That idea is that if values can uniquely identify the operation which wrote them, serializability checking becomes easier as any observation of a value totally orders the reader and the writer with respect to each other. "Easier" meant both simpler code, as well as actually being able to computationally do the verification on complex histories.

Prior to this PR, kvnemesis was writing unique values where it could, but it couldn't do it for deletions - after all, a deletion is like writing a "nothing" to MVCC, and there wasn't any way to make two "nothings" distinguishable. Having broken with the basic premise of unique values, there was a lot of bending over backwards going on to avoid, for the most part, devolving into a "normal" serializability checker. However, for contrived edge cases this would not be avoidable, and so there would be histories that kvnemesis just couldn't handle.

"v2" (this PR) gets this right. The main contribution is that we now thread kvnemesis' sequence numbers all the way down into MVCC and back up with the RangeFeed. Values are now truly unique: a deletion tombstone is identifiable via its `MVCCValueHeader`, which carries the `kvnemesisutil.Seq` of the `Operation` that originally wrote it. On top of this, everything "just works" as you expect.

Plumbing testing-only fields through the KV API protobufs isn't something that was taken lightly and that required a good amount of deliberation. However, we figured out a clever (maybe too clever?) way to have these fields be zero-sized in production, meaning they cannot possibly affect production logic and they also do not influence struct sizes or the wire encoding. As a drawback, kvnemesis requires the `crdb_test` build tag (it will `t.Skip()` otherwise).

The remainder of this PR is mostly improvements in code quality. `echodriven` testing was introduced for many of the tests that could benefit from it. The core components of kvnemesis were reworked for clarity (the author spent the first week very confused and wishes for that experience to remain unrepeated by anyone). kvnemesis also tracks the execution timestamps as reported by the KV layer, which a future change could [use](https://github.com/cockroachdb/cockroach/issues/92898) for additional validation.

Of note is the updated doc comment, which is reproduced below in entirety.

Fixes #90955.
Fixes #88988.
Fixes #76435.
Fixes #69642.

----

Package kvnemesis exercises the KV API with random concurrent traffic (as
well as splits, merges, etc) and then validates that the observed behaviors
are serializable.

It does so in polynomial time based on the techniques used by [Elle] (see in
particular section 4.2.3), using the after-the-fact MVCC history as a record
of truth. It ensures that all write operations embed a unique identifier that
is stored in MVCC history, and can thus identify which of its operations'
mutations are reflected in the database ("recoverability" in Elle parlance).

A run of kvnemesis proceeds as follows.

First, a Generator is instantiated. It can create, upon request, a sequence
in which each element is a random Operation. Operations that are mutations
(i.e. not pure reads) are assigned a unique kvnemesisutil.Seq which will be
stored alongside the MVCC data written by the Operation.

A pool of worker threads concurrently generates Operations and executes them
against a CockroachDB cluster. Some of these Operations may
succeed, some may fail, and for some of them an ambiguous result may be
encountered.
Alongside this random traffic, kvnemesis maintains a RangeFeed that ingests
the MVCC history. This creates a "carbon copy" of the MVCC history.

All of these workers wind down once they have in aggregate completed a
configured number of steps.

Next, kvnemesis validates that the Operations that were executed and the
results they saw match the MVCC history, i.e. checks for Serializability. In
general, this is an NP-hard problem[^1], but the use of unique sequence
numbers (kvnemesisutil.Seq) makes it tractable, as each mutation in the MVCC
keyspace uniquely identifies the Operation that must have written the value.

We make use of this property as follows. First, the Validate method iterates
through all Operations performed and, for each, inspects

- the type of the Operation (i.e. Put, Delete, Get, ...),
- the (point or range) key of the operation, and
- its results (i.e. whether there was an error or which key-value pairs were returned).

Each atomic unit (i.e. individual non-transactional operation, or batch of
non-transactional operations, or transaction) results in a slice (in order
in which the Operations within executed[^2]) of observations, where each
element is either an observed read or an observed write.

For example, a Batch that first writes `v1` to `k1`, then scans `[k1-k3)`
(reading its own write as well as some other key k2 with value v2) and then
deletes `k3` would generate the following slice:

       [
         observedWrite(k1->v1),
         observedScan(k1->v1, k2->v2),
         observedWrite(k3->v3),
       ]

Each such slice (i.e. atomic unit) will then be compared to the MVCC history.
For all units that succeeded, their writes must match up with versions in
the MVCC history, and this matching is trivial thanks to unique values
(including for deletions, since we embed the kvnemesisutil.Seq in the value),
and in particular a single write will entirely fix the MVCC timestamp at
which the atomic unit must have executed.

For each read (i.e. get or scan), we compute at which time intervals each
read would have been valid. For example, if the MVCC history for a key `k1`
is as follows:

                  k1

       	 -----------------
       	 t5      v2
       	 t4
       	 t3
       	 t2     <del>
       	 t1      v1

then

  - observedGet(k1->v1)  is valid for [t1,t2),
  - observedGet(k1->nil) is valid for [0,t1) and [t2,t5), and
  - observedGet(k1->v2)  is valid for [t5,inf).

By intersecting the time intervals for each Operation in an atomic unit, we
then get the MVCC timestamps at which this Operation would have observed what
it ended up observing. If this intersection is empty, serializability must have
been violated.

In the error case, kvnemesis verifies that no part of the Operation became visible.
For ambiguous results, kvnemesis requires that either no Operation become visible,
or otherwise treats the atomic unit as committed.

The KV API also has the capability to return the actual execution timestamp directly
with responses. At the time of writing, kvnemesis does verify that it does do this
reliably, but it does not verify that the execution timestamp is contained in the
intersection of time intervals obtained from inspecting MVCC history[^3].

[Elle]: https://arxiv.org/pdf/2003.10554.pdf
[^1]: https://dl.acm.org/doi/10.1145/322154.322158
[^2]: there is currently concurrency within the atomic unit in kvnemesis. It
could in theory carry out multiple reads concurrently while not also writing,
such as DistSQL does, but this is not implemented today. See:
https://github.com/cockroachdb/cockroach/issues/64825
[^3]: tracked in https://github.com/cockroachdb/cockroach/issues/92898.

Epic: none
Release note: None

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[a383117602...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/a3831176026517387f7978c3b4954d4333cfdc3c)
#### Tuesday 2022-12-06 16:57:40 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[1905925b53...](https://github.com/newstools/2022-new-york-post/commit/1905925b532353fcd528e1fa4bd70aa4a47be8a7)
#### Tuesday 2022-12-06 18:17:20 by Billy Einkamerer

Created Text For URL [nypost.com/2022/12/06/dear-abby-my-boyfriend-cheated-on-my-20-times/]

---
## [Jaden-PHILIPPINES/VGP-P3-2022-2023](https://github.com/Jaden-PHILIPPINES/VGP-P3-2022-2023)@[4ebe194adb...](https://github.com/Jaden-PHILIPPINES/VGP-P3-2022-2023/commit/4ebe194adb072229cf9624858d807e2f9e88e5d7)
#### Tuesday 2022-12-06 18:31:41 by Jaden Morales

Revert "Fuck you luck"

This reverts commit d172736fc5497c08a7d96b9e75599b8c711769b5.

---
## [ryansong13/zulip](https://github.com/ryansong13/zulip)@[23a776c144...](https://github.com/ryansong13/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Tuesday 2022-12-06 19:22:46 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[83f475aa7e...](https://github.com/the-og-gear/tgstation/commit/83f475aa7ec4290c6961f1f14c5da80f340989b8)
#### Tuesday 2022-12-06 19:48:38 by tralezab

Adds the DNA Infuser, a genetics machine you feed corpses to infuse their DNA with yours! What could go wrong?! (#71351)

## About The Pull Request  
Adds the "DNA Infuser" to genetics. One person enters, a corpse is added
to the machine, and you can activate the machine to "infuse" the subject
with the DNA. This converts one random organ from a set into the
mob-related organ.

### Rat mutation 🐀

Rats can be fed in to turn you into a rat-creature-thing!
```diff
+See better in the dark
+Can pretty much eat anything! Toxic foods, gross foods, whatever works!
+Smaller, and can climb tables
?Randomly squeaks occasionally?
-Take twice as much damage
-Vulnerable to flashes
-Gets hungry MUCH quicker.
-Yes, eat anything, but only ENJOY dairy.
```
Having every rat organ at once allows you to ventcrawl nude!

### Carp mutation 🐟 

Carp work for a mutation as well!
```diff
+Strong jaws, that drop teeth over time!
+Space immunity! Breathe in space, unbothered by pressure or cold!
+Smaller, and can climb tables
-Can't block your jaws with a mask
-Can't take the heat, overheats easily
-Can only breathe in environments that have minimal or no oxygen
-Nomadic. If you don't enter a new zlevel for awhile, you'll start feeling anxious.
```
Having every carp organ at once allows you to swim through space!

### Fly mutation 🪰 

Any corpses without organs to turn into turn into fly organs! Fly organs
now have a bonus for collecting them all, transforming you into a fly,
when you pass the threshold. But even without those, fly organs are
technically... organs. They most of the time work like normal ones.

## Todo 🐦 

- [x] Finish the infuser code
- [x] Create a little booklet that shows what kind of shit you can turn
into, hopefully i can autogenerate this based off of organ set subtypes
list
- [x] sprite/slap a color on rat mutant organs
- [x] Maybe make a *few* more organ sets

## Why It's Good For The Game 🐑 

Oops, I forgor to fill this out! My hackmd is here.

https://hackmd.io/@bazelart/ByFkhuUIi

## Changelog 🧬 

:cl: Tralezab code, Azlan + Azarak (Az gaaang) for the organs
add: Added the DNA infuser to genetics! Person goes in, corpse goes in,
and they combine!
add: Try not to turn yourself into a fly, OK?
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[35b5ac0c4e...](https://github.com/the-og-gear/tgstation/commit/35b5ac0c4e6bbaf2adf277a7ea7a4a4eab89726b)
#### Tuesday 2022-12-06 19:48:38 by Fikou

Psykers (#71566)

## About The Pull Request
Finishes #66471
At burden level nine (or through a deadly genetic breakdown), you now
turn into a psyker.
This splits your skull in half and transforms it into a weird fleshy
mass. You become blind, but your skull is perfectly suited for sending
out psychic waves. You get potent psy abilities.
First one is brainwave echolocation, inspired by Gehennites (but not as
laggy).
Secondly, you get the ability of Psychic Walls, which act similarly to
wizard ones, but last shorter, and cause projectiles to ricochet off
them.
Thirdly, you get a projectile boost ability, this temporarily lets you
fire guns twice as fast and gives them homing to the target you clicked.
Lastly, you get the ability of psychic projection. This terrifies the
victim, fucking their screen up and causing them to rapidfire any gun
they have in their general direction (they'll probably miss you)
With most of the abilities being based around guns, a burden level nine
chaplain now gets a new rite, Transmogrify. This lets them turn their
null rod into a 5-shot 18 damage .77 revolver. The revolver possesses a
weaker version of antimagic (protects against mind and unholy spells,
but not wizard/cult ones). It is reloaded by a prayer action (can also
only be performed by a max burdened person).
General Video: https://streamable.com/w3kkrk
Psychic Projection Video: https://streamable.com/4ibu7o

![image](https://user-images.githubusercontent.com/23585223/204150279-a6cf8e2f-c678-476e-b72c-6088cd8b684b.png)

## Why It's Good For The Game
Rewards the burdened chaplain with some pretty cool stuff for going
through hell like losing half his limbs, cause the current psychics dont
cut it as much as probably necessary, adds echolocation which can be
used for neat stuff in the future (bat organs for DNA infuser for
example).

## Changelog
:cl: Fikou, sprites from Halcyon, some old code from Basilman and
Armhulen.
refactor: Honorbound and Burdened mutations are brain traumas now.
add: Psykers. Become a psyker through the path of the burdened, or a
genetic breakdown.
add: Echolocation Component.
/:cl:

Co-authored-by: tralezab <spamqetuo2@gmail.com>
Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[661eaa985e...](https://github.com/MTandi/tgstation/commit/661eaa985e32056cc25f32bd81d9106861a4f9f8)
#### Tuesday 2022-12-06 19:53:02 by MrMelbert

Important heretic spell rebalancing (#71620)

## About The Pull Request

Nerfs
- Furious steel cooldown: 30s -> 60 seconds (when ascended: 10s -> 30s)
- Furious steel: Now affected by antimagic
- Cleave cooldown: 40s -> 45s
- Cleave range: 9 tiles -> 4 tiles
- Cleave wound: Now has natural clotting, changing the amount of blood
loss from inf -> ~40%
- Blood siphon range: 9 tiles -> 6 tiles
- Void Pull: Now affected by antimagic
- Void Phase: Now affected by antimagic

Buffs
- Void Blast cooldown: 60s -> 30s

Other
- Rust Formation now has a "distinct" icon
- Void Blast now has a "distinct" icon

## Why It's Good For The Game

A lot of these spells were extremely oppressive, and made it pretty much
a joke to get away with anything.
They were no-brainer choices, and as a result no one really pathed into
anything else but these.

- Furious Steel: 
- Now that blade heretics have "realignment" in their repertoire, which
offers them another counter for being hit by disablers or batons, this
spell doesn't need to have such an insanely high uptime. The spell
should be used for initiating and obtaining the lead in a combat,
instead of having nigh-invulnerability for most periods.
- Additionally, antimagic protection was kind of missing, which was
partially an oversight of it not being a `/magic` projectile.
 
- Cleave:
- Cleave was by far the most absurd ability available bar none. This
spell was guaranteed death in 30 seconds if the target had no way to
stop the bloodflow immediately. AND it could be casted from across the
screen. This brings cleave's range into midrange between you and the
target, giving a lot more opportunity to be aware for the victim.
- Critical bleed wounds had a negative clotting rate, meaning that prior
you would bleed to 0% from cleave if you didn't stop it. Not very fun,
so with the default clotting rate it now stops at 60% blood flow -
enough to be lethal if untreated, but doesn't completely tap you out
   - **Alternatives**: 
      - Keep the no clotting, make it a pure melee / touch spell. 
      - Reduce the cooldown, make it a projectile
- Change it to be like a cool scythe attack that comes out of the caster
and does a sweep

- Blood Siphon: 
- This was primarily done to slot in better with Cleave's range
decrease, encouraging more close range combat between the two. Getting
point clicked from across the screen isn't fun.

- Void Pull and Phase:
- Largely done for consistency. These are spells which cause damage, so
anti-magic should stop the damage from the spells.

- Void Blast
- I have no idea why I made the cooldown so high on this, 1 minute made
it almost worthless.

TLDR: Instakill click spells from across the screen bad, invulnerability
bad

## Changelog

:cl: Melbert
balance: Heretic: Furious Steel's cooldown has been doubled (30s ->
60s), and abides by antimagic
balance: Heretic: Cleave's cooldown has increased by 5s, range has been
decreased to 4 tiles, and wound applied now has natural clotting
balance: Heretic: Blood Siphon's range has been decreased to 6 tiles
balance: Heretic: Void Pull and Phase abide by antimagic
balance: Heretic: Halved Void Blast's cooldown to 30s
qol: Heretic: Void Blast and Rust Formation now have distinct icons 
/:cl:

---
## [Sandstorm-Station/Sandstorm-Station-13](https://github.com/Sandstorm-Station/Sandstorm-Station-13)@[8eec99b320...](https://github.com/Sandstorm-Station/Sandstorm-Station-13/commit/8eec99b3206e917bd711987a80422168de53f83d)
#### Tuesday 2022-12-06 20:09:38 by LemonInTheDark

Caches GetJobName. Fuck you (#274)

* Caches GetJobName. Fuck you

This code made me deeply upset, WHY IS IT RECURSIVE WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY

* Centcom handling, properly this time

* Empties out real_job_name

* Sets real_job_name up in the right place

* Moves real_job_name to SSjob, uses modularTM

* Yeet

* Removes old code, swaps over to the SSjob list

* dme changes

* indents... comments

Co-authored-by: SandPoot <enric_gabirel@hotmail.com>

---
## [Xiaorui-Huang/leetcode](https://github.com/Xiaorui-Huang/leetcode)@[499e1cbea3...](https://github.com/Xiaorui-Huang/leetcode/commit/499e1cbea30a437802629e8e052c1aba16e3a46b)
#### Tuesday 2022-12-06 20:09:50 by Richard Huang

solve(2156): find substr with hash

god fucking damn it I don't remember a darn thing from CSC165...
all this overflow & modular arithmetic shenanigans

Tags: Rolling-Hash Hash-Function Sliding-Window

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[6120721323...](https://github.com/Huffie56/cmss13/commit/6120721323b6431a1d43d89d7354e1ea1763a734)
#### Tuesday 2022-12-06 20:26:29 by carlarctg

Added various flasks to loadouts and canteen vendors. (#1802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Added a canteen (item) from an unused sprite.

Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

All flasks (and canteen (item)) can be selected in the character loadout
items menu at the bottom.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

The old W-Y flask looked more like a skull than the logo. The gold badge
bit was legacy from bay12.

> Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Legacy renaming.

> Added a canteen (item) from an unused sprite.

Cool sprite. Fucked up we didn't have canteens until now when, uh.
That's what people actually use in the military, not flasks. (To my
knowledge)

> Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

Canteens are the standard military container, W-Y flasks in the vendors
are a good Lore way to show how much of a WY suckup the USCM is.

> All flasks, vacuum and leather included, (and canteen (item)) can be
selected in the character loadout items menu at the bottom.

I think these flasks are cool ways to add flavor to your character, and
it's a shame most of them either weren't in the game or were in very
annoying to find places.

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

:cl:

imageadd: Resprited the W-Y Flask. Removed the gold badge from the
former detective's flask.
add: Renamed the former detective's flask and bar flask into the brown
and black, respectively, leather flasks.
add: Added a canteen (item) from an unused sprite.
add: Canteens (item) and W-Y flasks can now be found in the canteen
(place) vendors.
add: All flasks, vacuum and leather included, (and canteen (item)) can
be selected in the character loadout items menu at the bottom.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [AlphaDominatus/tgstation](https://github.com/AlphaDominatus/tgstation)@[85b2d5043d...](https://github.com/AlphaDominatus/tgstation/commit/85b2d5043dbc9eb277bf57dd6dc5147ae08fe978)
#### Tuesday 2022-12-06 22:08:29 by LemonInTheDark

Optimizes qdel related things (slight init time savings) (#70729)

* Moves spawners and decals to a different init/delete scheme

Rather then fully creating and then immediately deleting these things,
we instead do the bare minimum.

This is faster, if in theory more fragile. We should be safe since any
errors should be caught in compile since this is very close to a
"static" action. It does mean these atoms cannot use signals, etc.

* Potentially saves init time, mostly cleans up a silly pattern

We use sleeps and INVOKE_ASYNC to ensure that handing back turfs doesn't
block a space reservation, but this by nature consumes up to the
threshold and a bit more of whatever working block we were in.

This is silly. Should just be a subsystem, so I made it one, with
support for awaiting its finish if you want to

* Optimizes garbage/proc/Queue slightly

Queue takes about 1.6 seconds to process 26k items right now.
The MASSIVE majority of this time is spent on using \ref
This is because \ref returns a string, and that string requires being
inserted into the global cache of strings we store

What I'm doing is caching the result of ANY \ref on the datum it's
applied to. This ensures previous uses will never decay from the string
tree.

This saves about 0.2 seconds of init

---
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[a753229ee2...](https://github.com/Salex08/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Tuesday 2022-12-06 22:13:18 by GoldenAlpharex

Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.


<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.


![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @MrMelbert about it and he gave me the go-ahead, as can be seen
here:


![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

---
## [Shadyyy66/tgstation](https://github.com/Shadyyy66/tgstation)@[bbb956d2a6...](https://github.com/Shadyyy66/tgstation/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Tuesday 2022-12-06 22:25:34 by OrionTheFox

Removes Bowls from garbage spawners because they don't fit in trash bags and I'm SICK of not being able to clean! (#71152)

## About The Pull Request
Let me give you a scenario.

---

THIS, is you. Say hi!

![image](https://user-images.githubusercontent.com/76465278/200268480-9dcf1f45-3bc5-402d-b743-b0649deefb08.png)

You're a loyal janitor aboard NT-SS13. You love your job; despite the
dangers, it's generally not too busy or tedious. Just a spray, a sweep,
and put it all in a bag.

---

This. This is your enemy.

![image](https://user-images.githubusercontent.com/76465278/200269058-957ca433-4666-44b5-9c10-ae0da75219cb.png)

Some crewmembers continuously leave them in maintenance, tossing them
into garbage bins as they pass.
This bowl, you cannot spray it. You can sweep it as far as you want, but
in the end, cannot put it into the bag.

![image](https://user-images.githubusercontent.com/76465278/200269156-bbc7758b-9cbe-4a3b-8d17-9aa53254b4b2.png)

---

It exists to torment you.
Nothing more, nothing less.

You hate the bowl. And it hates you.
Wake up.

![image](https://user-images.githubusercontent.com/76465278/200269456-a7fda598-3556-4069-bd2a-44a8793c198f.png)
## Why It's Good For The Game
Usually when you pass a trash pile you expect it to have trash, and
entire bowls aren't technically trash code-wise, nor can you clean them.
Yes, this PR has a modicum of salt. It was salt left behind in THE DAMN
BOWLS.
## Changelog
:cl:
del: NT has decided to begin a Recycling initiative, asking crew to
please stop throwing their bowls away in maintenance. You should only
find trash and grime from now on!
/:cl:

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[cf4a194e86...](https://github.com/Zonespace27/Skyrat-tg/commit/cf4a194e86d53d57397f6de4febbea0de9c6ef57)
#### Tuesday 2022-12-06 22:35:51 by SkyratBot

[MIRROR] Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! [MDB IGNORE] (#17828)

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.

<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.

![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @ MrMelbert about it and he gave me the go-ahead, as can be seen
here:

![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [CalioPur/Chat_Online](https://github.com/CalioPur/Chat_Online)@[0ae911e684...](https://github.com/CalioPur/Chat_Online/commit/0ae911e6849aac2d462c706925b1a61d07fff599)
#### Tuesday 2022-12-06 22:38:16 by VeryDeadMoth

AES MODULE FUCKING WORKS HELL YEAH

A lot of time spent on stack overflow but goddamn I built it

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[a811adac74...](https://github.com/Zonespace27/tgstation/commit/a811adac74513494a620fae631da95d2626b1be7)
#### Tuesday 2022-12-06 22:42:42 by Epic

Changes Admin Prison to be Anti-Telekinesis: Walls off equipment rooms, replaces computers, and makes the tables tidy (#71433)

First PR, may require some changes or something because I don't know how
to do anything bleh
## About The Pull Request

We already had issues with crewmembers with telekinesis making changes
to the security records (purging them and what not). And, nothing has
been done about it, not yet, anyway. Not only record computers are a
problem as well.


![image](https://user-images.githubusercontent.com/106710384/203241399-8314bcba-d2d0-44af-9360-30ff58dbc39e.png)
Previously, prisoners can access the sec vendor with telepathy, and,
since the vendor is free, spam the vendor and be an annoyance. Sure, I
believe that it is not as big of a problem as purging the security
records, but I feel like it's against what the prison is supposed to
stand for; It's supposed to stop them and get them to listen to ahelps
thrown at them.

I've decided to make a bit of changes to the prison to make it so that
people with telekinesis won't fuck up things as much. This replaces real
computers with nonfunctional ones, adding walls to equipment areas to
make sure prisoners don't spam the vendor, and deletes guns/weapons from
the tables so they won't grab them.

## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/106710384/203241465-833f79da-58a3-4feb-87b0-091fbb846e93.png)
This PR is more tailored to admins dealing with no-good-doers, and goes
for the vibe of "HEY, SOMEONE IS PMING YOU, REPLY TO THEM INSTEAD!" Of
course, this leads to prisoners not interacting with the current round,
and, less chance of them going insane and breaking all the windows with
a telekinesis auto-rifle.

Plus, this can always be reverted in-case someone comes up with coding
stuff in instead. I'm all through with that and willing to work with
whoever to solve the issue.

Also, of course, Closes #60967

## Changelog

:cl:
admin: Nanotrashen made some top-of-the-line changes to their
top-of-the-line prison by walling off their equipment area and removing
some spare guns they somehow left on the tables. We also stole the
security computers, so people with telekinesis can't access them.
/:cl:

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[c185dffda0...](https://github.com/Zonespace27/tgstation/commit/c185dffda0cc30d8187fa1ba37e5784b8d630ba4)
#### Tuesday 2022-12-06 22:42:42 by Jacquerel

Basic Mob Carp Bonus Part: Wall smashing (#71524)

## About The Pull Request

Atomisation of #71421 
This moves the attack function of "environment smash" flags which allow
simple mobs to attack walls into an element, so that we can put it on
other things later.
For some reason while working on carp I convinced myself that they had
"environment_smash" flags, which they do not, so this actually is not
relevant to carp in any way.

While implementing this I learned that the way wall smashing works is
stupid, because walls don't have health and so resultingly if a mob can
attack walls it deletes them in a single click. If we ever decide to
change this then it should be easier in an element than in three
different `attack_animal` reactions.
This is especially silly with the "wumborian fugu" item which allows any
mob it is used on to instantly delete reinforced walls, and also to
destroy tables if they click them like seven or eight times (because it
does not increase their object damage in any way).

## Why It's Good For The Game

Eventually someone will port a basic mob which does use this behaviour
(most of the mining ones for instance) and then this will be useful.
If we ever rebalance wall smashing to not instantly delete walls then
this will also be useful.
Admins can apply this to a mob to allow it to delete walls if they
wanted to do that for some reason, they probably shouldn't to be honest
at least until after we've done point two unless they trust the player
not to just use it to deconstruct the space station.

## Changelog
:cl:
refactor: Moves wall smashing out of simple mob code and into an element
we can reuse for basic mobs later
/:cl:

---
## [psanker/aoc2022](https://github.com/psanker/aoc2022)@[ff46fc9d47...](https://github.com/psanker/aoc2022/commit/ff46fc9d473e6215bf8f9faf39ceba041af65b02)
#### Tuesday 2022-12-06 23:05:48 by Patrick Anker

feat: fuck you day 5

So let me tell you what happened. I spent a couple hours on this
originally. The parsing was kind of annoying but honestly not too
miserable. After a couple false starts with the test input, I got part 1
done pretty easily. Then part 2. Oh part 2. I spent **hours** testing my
code because by all measures it was working just fine; however, AoC was
not accepting my input. Turns out I misread the prompt a bit: I was
thinking the stacks could be moved **only** in batches of at most three,
but turns out the thing could move the **entire** stack at once.

I'm miffed.

---
## [dnalborczyk/apollo-server](https://github.com/dnalborczyk/apollo-server)@[e3115faf8c...](https://github.com/dnalborczyk/apollo-server/commit/e3115faf8c70b0d7e5f46ec26145c1e6bd88e0a9)
#### Tuesday 2022-12-06 23:31:26 by Trevor Scheer

Add note about EOL packages (#7216)

There's been some apparent confusion around what EOL means for AS 2/3.
Concerned folks seem to be under the impression that they need to
migrate away immediately as if the software is going to disappear out
from under them, so we should make it clear that's not the case, even if
we recommend strongly against using EOL software.

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

Co-authored-by: Rose M Koron <32436232+rkoron007@users.noreply.github.com>

---
## [anthony-fdez/foundry-ui](https://github.com/anthony-fdez/foundry-ui)@[215850f646...](https://github.com/anthony-fdez/foundry-ui/commit/215850f646901a10cd9d0dfcd88e47b697c4cbc4)
#### Tuesday 2022-12-06 23:39:37 by Anthony Fernandez

Added code hightlight to the readme

Dude this library looks fucking awesome. I'm building my own, as a little side project just to learn. I hope you don't mind me taking inspiration from you hahaha. Really good work man!

---
## [Raneses20/app-dev](https://github.com/Raneses20/app-dev)@[d9105c24e9...](https://github.com/Raneses20/app-dev/commit/d9105c24e9f554e5cd480eacc737bab6057c31f5)
#### Tuesday 2022-12-06 23:58:39 by Raneses20

Update README.md

as you can see i play genshin and hate it's fandom at the same time because of the toxicity of the fandom like they said this" oh you should add this artifacst to make your character strong" of "noo you should not make him?her dps main he?she is only for support " or even this "you should complete all the quest " for the love of primus just stop telling what to do i will play this genshin in may way so if i got a chance to to change the  genshin fandom i will reforge it no matter what so thats explain my favorite series

---

