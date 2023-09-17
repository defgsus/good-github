## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-16](docs/good-messages/2023/2023-09-16.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,960,506 were push events containing 2,723,630 commit messages that amount to 153,268,184 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 59 messages:


## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[4b8de7b79f...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/4b8de7b79f0a343dc587d0d17eb9361ecc7103c1)
#### Saturday 2023-09-16 00:07:38 by san7890

Refactors the `notransform` variable into a trait. (#78146)

## About The Pull Request

Hey there,

There were more than a few times (like in cinematic code) where we might
need to accurately know the source of what's adding this trait (or have
multiple sources for the whole 'we don't want this mob to do shit while
we transform this mob'), so in order to rectify this potential issue,
let's refactor it into a trait.

## Why It's Good For The Game

Some code already declared that there might be issues with this being a
boolean var (with no way of knowing _why_ we don't want this mob to not
transform (or not do anything idk). Let's remove those comments and any
future doubt in those instances with the trait macros. Also, stuff like
`TRAIT_IMMOBILIZED` which does a similar thing in many contexts was
already a trait that was regularly added in conjunction with flipping
the variable, so we're able to flatten all that stuff into
`add_traits()` and `remove_traits()` now. nice

I also cleaned up quite a bit of code as I saw it, let me know if it
should be split out but I guarantee that if I didn't do it- no one will
for the next two years.

## Changelog

:cl:
refactor: If you transform into another mob and notice bugs with
interacting with the game world, please create a bug report as this
framework was recently refactored.
/:cl:

Probably fucked up somewhere, lmk

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[f373f05075...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/f373f0507570506470f73d65d105d978e4e7ab8f)
#### Saturday 2023-09-16 00:13:35 by Hatterhat

buffs embed pulling with hemostats, allows wirecutters to pull embeds too (#78256)

## About The Pull Request
- Wirecutters or tools with wirecutter behaviors are now valid for
plucking embeds.
- Pluck speed no longer **starts** at 2.5 seconds, which is a pretty
dang long time, especially if you have bad embed RNG. I'll do the math
and run some more tests in the morning.
- Wirecutters have a speed malus in regards to plucking embeds. I should
probably make it worse to account for, like, jaws of life or something.
- Plucking embeds with wirecutters now hurts! It hurts way less than
ripping it out with your hands, but it still hurts!

For comparison's sake, bare-handed throwing star removal compared to
possible tools.

![image](https://github.com/tgstation/tgstation/assets/31829017/96730fa5-77b8-4f31-83ba-48d36e4e419b)


## Why It's Good For The Game
Embeds kinda suck to deal with. This is intentional - I get that.

However, hemostat pulling is kind of... kind of bad. Awful, really. 2.5
seconds is a lot of time. I know it's not supposed to be the best
option, but if you've got a tool, I'd at least like to think it'd be
slightly less bad than shoving your fingers into your wound?

## Changelog

:cl:
balance: Pulling embedded items e.g. shrapnel with hemostats is now a
lot faster, and scales appropriately with toolspeed.
balance: You can now pull embedded items with wirecutters, at a speed
penalty.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[c6ac468b90...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/c6ac468b9083ff06b36a544382684c86743e953e)
#### Saturday 2023-09-16 00:13:35 by Hatterhat

second pass over the SC/FISHER code, incl. bitflags and PDAs (#78330)

## About The Pull Request
makes `COMSIG_HIT_BY_SABOTEUR` return a bitflag in order to close #78297
(i am very sorry)
fixes #78298
extends flashlight disabling to modular computers incl. PDAs because
somehow i forgot that they had flashlights.
## Why It's Good For The Game
my code sucks and i should make it suck less, actually

## Changelog
i don't think i get to put a code improvement tag if it's not
playerfacing and it's my own fault
:cl:
fix: Flares and candles no longer sound like flashlights when being
turned on.
fix: Getting shot by an SC/FISHER now disables PDA lights for
consistency's sake.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [Rodmjorge/AdvancedSuperMarioWorld](https://github.com/Rodmjorge/AdvancedSuperMarioWorld)@[b3b17920e4...](https://github.com/Rodmjorge/AdvancedSuperMarioWorld/commit/b3b17920e4fa6f67f2c4137b64da13dfd07492bb)
#### Saturday 2023-09-16 00:29:38 by Rodmjorgeh

Prototype koopa troopa and fixed collision issues

FUCKING FINALLY. you really don't know how much effort i put in to make it work. holy shit it's finally over

---
## [NovusSS13/NovusSS13](https://github.com/NovusSS13/NovusSS13)@[42220a7b39...](https://github.com/NovusSS13/NovusSS13/commit/42220a7b39aeac26083ebea3ce571a4b14a41a75)
#### Saturday 2023-09-16 00:35:48 by Bob

dont fill up the fucking list with nulls god damn it

---
## [jlyonsmith/flame](https://github.com/jlyonsmith/flame)@[2f973abe8b...](https://github.com/jlyonsmith/flame/commit/2f973abe8b298a4f6f1164065783de560953d789)
#### Saturday 2023-09-16 00:38:05 by Luan Nico

docs: Improved spellchecking (#2722)

Improve our spellchecker (cspell) configuration and dictionary file
organization.

# Rationale

This is a proposal to establish a few changes:
* better separate our dictionary files into different categories of
types of words we are including
* improve the cspell regexes to be more aggressive
* be less lenient to what kinds of words we are adding to our
dictionaries
* have the dictionary file also serve as an explanation for obscure
references that cannot be easily derived from the word

Essentially my goal is that either when reviewing a PR that adds a new
entry to our dictionary, or when reading the dictionary files
themselves, it is immediately obvious what the entries are and why they
are there. Currently it can be just a dumpster we throw anything into if
spellcheck fails.

# Proposal

This PR-as-a-proposal essentially do the following changes.

## Split Dictionary Files

Proposes a better separation for our dictionary files. Currently we have
3 that are a bit broad and not super clear on what goes where. This
breaks it down a bit more and adds a comment to each file explaining
what kinds of terms should be added to each; that also serves as a
general guidance for what kinds of words should be added to the lexicon
in general, and makes it harder for mistakes to make into it.

* `flame_dictionary`: remains pretty much unchanged; it is dedicated to
Flame-related words, including companies, tools, and libraries (and
their associated concepts) mentioned on our codebase. Basically a
collection of proper-nouns relating to companies and libraries we
mention.
* `dart_dictionary`: new file for Dart and Flutter related terms
* `sphinx_dictionary`: unchanged, for Sphynx related terms
* `people_dictionary`: specific for people names and usernames
referenced on the codebase (in TODOs, mentions, etc)
* `words_dictionary`: actual English-language words (or common
abbreviations) missing from CSpell
* `gamedev_dictionary`: this was our biggest file that contained all
sort of things. it has been mostly broken down and now only contains
general development-adjacent terms and expressions

## Include definitions

Except for the `words` dictionary, which should be self-explanatory (as
it basically covers for "holes" in CSpell standard dictionary, which I
have been finding a bit lacking), every other file will contain terms in
the form:

```
word # definition of the word
```

What exactly the definition is can slightly vary depending on which
dictionary file we are talking about, but the examples should be
self-explanatory.

As an example, for the gamedev file, it should provide some simple
guidance as to what the term means, or if it's an acronym or
abbreviation, what it stands for. The goal is not to teach the entire
concept to someone unfamiliar, but allow them to "google" it for
themselves by giving enough context, so they can confirm their
suspicions. For example, if they see `LTRB` somewhere by itself, they
are not able to "just google that" because it is too vague. The
dictionary file provides enough context for the user to figure out
however much deeper information they want about any particular subject.
It will also disambiguate from any non-Flame related homonyms. For
people on the people file and companies on the flame file, the
description will provide links to clearly disambiguate what they are;
for tools, a brief description of what the tool is for is also included.
And so on.

The goal is not to build a comprehensive, in depth-guide to each word we
use, but rather to give the bare minimum of context on what this term
"is doing" on our codebase.

## Be less lenient with terms

My idea with these two major changes combined, is that we are overall
more tactical about which terms we want to add to the dictionaries.
Adding a word to the dictionary file is essentially giving carte blanche
to anyone in the future to reuse that term anywhere. I think we should
see spellchecker violations as "warnings"; we decide on the set of
warning rules we want to enable for the entire project (hopefully all
the ones that make sense; or have a reason for disabling the ones that
don't). We might need to violate these warnings sporadically, for
example, we ban `print` on the codebase but might need to allow it
specifically in a couple places. But we would not disable the entire
warning to do that, rather we would add a specific comment-bypass on the
smallest possible scope that encompasses all the relevant lines. We
would also add a proper comment explaining why we are bypassing the
general rule in this specific place.

Similarly, we should not have one-off violations on the dictionary file,
even if they make sense in the one place they occur, but we should
encourage more liberal use of scoped bypasses for such cases. These
Ukrainian words are required in this file, but should not be on the
dictionary as it does not make sense to use foreign languages anywhere
else:

```
// used as examples of Ukrainian words on the documentation below
// cSpell:ignore рушниця, рушниці, рушниць
```

It might look inelegant to have to include that, but just like a
warning-bypass comment, accompanied by the explanatory proper-comment,
this actually provides helpful guidance and context for the reader that
might be confused with the usage of incomprehensible terms.

This also encourages people to avoid obscure terms that are not already
in our dictionary (i.e. that we have already "bought in" and paid the
mental load investment cost), making our code (and docs) easier to parse
and read for everyone. I want to be extremely clear that that **does
not** mean we need to "dumb down" anything whatsoever, or do any sort of
gymnastics to avoid the wrath of an incompetent spellchecker.

But, for example [when spelling "cave
ace"](https://github.com/flame-engine/flame/pull/2304) in variable names
in a random example, having it typed as `caveAce` instead of `caveace`
can slightly help with readability, specially for non-native speakers
(like most of us). It is an extremely minor insignificant gain, but
having the dictionary file require a brief description will nudge us to
give a bit more thought into each "bypass" we are adding.

(note: a similar issue that I have not yet addressed is "spine boy", but
I will leave that for followups and just added that one to the
dictionary for now, as I am still over the fence on that one since it is
an actual "known" character with a dedicated page, so it is more like a
proper noun - as a specific decision I think it is out-of-scope of the
broader discussion).

---
## [LiberatedWaveMan/LibPara](https://github.com/LiberatedWaveMan/LibPara)@[acb7352265...](https://github.com/LiberatedWaveMan/LibPara/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Saturday 2023-09-16 00:38:34 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0f84034ebd...](https://github.com/treckstar/yolo-octo-hipster/commit/0f84034ebd71d230d781144b1c6b5f13c7812ec5)
#### Saturday 2023-09-16 01:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [guest3444307/OneshotGB](https://github.com/guest3444307/OneshotGB)@[818dd2751d...](https://github.com/guest3444307/OneshotGB/commit/818dd2751d28f6ff74445dba5aabac36801d55b2)
#### Saturday 2023-09-16 01:42:50 by Max Nexus

9/15/23 Mirror Development 2: Son of Mirror

9/15/23: I always come back... The mirror is in a completely functional state, i just need to change the pallete on some sprites and there we go! I've also optimized Niko's luminous yellow eyes (used to be 2, now its 1), the last thing i did was change the pallete of the docks as a quick test. Man it's insane to think about the fact that i started this back in like the 10th grade, and now i've graduated. Since then i've made a game in unity. (Very annoyed about that fee, i want to move to godot now, I already wanted to before, but this is the push i needed) I also as of writing have yet to release it, i have a bad habit of nearly finishing something, then leaving it to rot for like 6 months, I finished it, i just need to compile the newest build... But anyways, 2.0.0. is nearly finished, I'm going to try and go for The World Machine's 1st anniversary! (9/22) Imagine if i miss it again. Now whats next is to add those changes to the bulb editon, And redo.... THE STAIRS (THE VIETNAM FLASHBACKS DEAR GOD)

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[5046a7d3ae...](https://github.com/nikothedude/tgstation/commit/5046a7d3ae845198e98ff3bc22c31495585e560c)
#### Saturday 2023-09-16 01:50:48 by Fikou

decks of cards no longer have their own wielded var (#78260)

## About The Pull Request
we have the trait for that

## Why It's Good For The Game
Throughout UNDERTALE, we get treated to three story sequences (4 if you
include flowey's fakeout but that's not important). The first is the
intro story, telling the tale of humans and monsters, which shortly
thereafter leads into 201X, and Chara (Toriel's house has “An old
calendar from 201X.”) falling into the underground.

The second is the waterfall flashback, its contents taking place
immediately after the intro segment, as a voice (Asriel) finds the
fallen child.

And finally, the third takes place in the True Pacifist final boss.
We'll get to it in due course, and it will have its own section, but
let's address the first two. Regarding the intro, the first thought one
might have is that simply, while narratively relevant, is not a diegetic
presentation. However, We know that everything after the “201X” frame is
Chara's memory (from an outside perspective, that is,) and we also know
that UNDERTALE LOVES bringing the non-diegetic, the mechanical, the
game, INTO the narrative. Saving, RPG Stats, hell, even the
NarratorChara. Surely the intro can be as well? On top of this, what
does the intro do for the player, as the player? Well, aside from
setting the tone, the intro gives us some setting backstory. It's all
important context, and it certainly helps… but it being in the intro
sequence is not that important; It's all presented throughout the game
via diegetic signs, books, and expositional tortoise war heroes/angry
fish guardswomen. The second half is how Chara fell to the underground,
and while also setting tone and informing the player how their character
arrived. It also creates the false impression for the player that their
character is Frisk, feeding into UNDERTALE's meta narrative; “You are
not your character, and their happy ending is not yours.” If we weren't
playing Chara, this would have no narrative impact. The story beat fails
to land by showing us someone elses' character. But, sure. This could be
a purely non-diegetic intro sequence. Simply put, The 201X portion of
the intro sequence does not make sense from a diegetic or a storytelling
perspective unless we play as Chara.

Flashback number two is explicitly a canonical, diegetic flashback. It
occurs when Frisk escapes Undyne by falling down a massive pit… again.
This time, they land in the garbage zone, black out, and have a
flashback sequence of the first time Asriel found Chara. While serving
the main narrative by setting up Asriel as a character, furthering the
final twist of the meta narrative's pacifist route, and neatly
transitioning between overworld areas, it's also very explicitly
diegetic and cannot be dismissed as an intro sequence. With this in
mind, one question is raised. Why do we see this flashback? If the
player character is Frisk, this makes little sense, why would we see
someone else's flashback and not our own? Same thing applies for a Third
Entity, but even more abstract and illogical. What even are we? Sure,
you could say Chara is somehow attached to us/Frisk and that somehow we
get a flashback from Chara who is somehow knocked unconscious by Frisk
also being knocked unconscious. I used the word somehow three times.
That's not good storytelling. A simpler answer, at least in my view, is
that We Are Chara. When Frisk is knocked unconscious, we, being
ostensibly linked to them as a Spirit/Ghost/Reincarnation/Possessing
Dead Frisk/Demon/Insert fan-theory here/SOUL Fragment, have our only
connection to the world temporarily disabled, rendering us effectively
unconscious and prompting a flashback. Nothing weird with multiple
entities or memory sharing. The waterfall flashback is simply our
memory. Simple. The simplest answers are usually the correct ones.

<details>
<summary>DO NOT RESEARCH</summary>
The third sequence is a connection/extension of the first two, displayed
when we SAVE “Someone Else” during the true pacifist battle with Asriel.
To refresh everyone, here is the direct quotes, taken from the Wiki:


[SAVE]: Someone Else
Strangely, as your friends remembered you... Something else began
resonating within the SOUL, stronger and stronger. It seems that there's
still one last person that needs to be saved. But who...? ... Suddenly,
you realize. You reach out and call their name.
Asriel: “Huh? What are you doing...?”
s
It's at this point that the sequence plays. There's no narration, but we
see the sequence of interactions between Asriel and Chara. There are no
panels (except for the first) that don't contain the both of them.
Following this, we get:

You feel your friends' SOULs resonating within ASRIEL! [This is the
generic flavour text for saving all 6, before “Someone Else”, and
appears at the asterisk above as well]
[SAVE]: Asriel Dreemurr
Asriel:
> “Wh... what did you do...?”
“What's this feeling…? What's happening to me?”
Etc. etc. let me win…
During my first and consecutive playthroughs of UNDERTALE, I came to the
conclusion that Asriel's soul still “Had Some Chara In It.” Saving
“Someone Else” was saving Chara, and then you save Asriel Dreemurr after
the story sequence.

This interpretation no longer feels particularly potent to me, but in
the spirit of completeness I'll address it alongside the more reasonable
“You just save Asriel.” Assuming for a moment though, that we do “Save
Chara”, it's not unreasonable to assume that some of Chara's ‘essence'
(or whatever) was merged with Asriel's and by SAVING them, we're SAVING
the part of them that's inside Asriel.

But I don't like that theory.

Let's talk about SAVING Asriel for a moment.

What is the motivation for doing that? Why would we, in universe, wish
to SAVE him, something that the narration explicitly prompts us to do?
He tried and probably succeeded to kill us, at least once, he wants to
reset the entire timeline, he wants to erase all our friendships, all
our progress.

So, why? Well, it's simple. He's our brother. And we know better than
anyone that he's worth saving. And at the very least, there's something
about Frisk (who appears to have absolutely no personality) that reminds
him of Chara, of us. This is, by his own admission, weird;

Asriel:
“Frisk… You really ARE different from Chara. In fact, though you have
similar, uh, fashion choices… I don't know why I ever acted as if you
were the same person.”

To summarise.

The player SAVING Asriel Dreemurr works best if they are Chara, it
becomes Chara encouraging Frisk to SAVE Asriel too.

Asriel recognises Frisk as Chara throughout the True Pacifist battle
(And Beyond), despite his own admission that this is basically
unfounded. Something is causing this recognition.

In Alphys' true lab, there lies a dusty TV and a stack of VHSes. On
them, lie some of the last words Chara had ever heard from their father.

[Asgore] Chara! You have to stay determined! You can't give up... You
are the future of humans and monsters...

These tapes are not the first time they are heard. Sleeping in Toriel's
guest bed, we dream about them. Suffering a fatal injury, they echo in
our ears. Watching the tape is yet another reveal. It's the chilling
truth that in fact, the words we (if we die a lot) are so familiar with,
are in fact the words we hear on our deathbed.

Storytelling-wise, this reveal; like all the others, fails if we do not
play as Chara.

Aside from Asriel's dialogue, Chara's genocide Narration, and the coffin
in Asgore's basement, this is the only time we hear Chara's name. That
and, this following exchange.

[Flowey]
Hi.
…
Monsters have returned to the surface
Peace and prosperity will rule across the land.
…
Well.
There is one last thing.
…
One being with the power to erase EVERYTHING…
…
I'm talking about YOU.
…
So, please.
Just let them go.
Let Frisk be happy.
…
Well, that's all.
See you later…
Chara.
This, I think, is pretty explicitly definitive. Flowey comes to you. To
us. Tells us to take a deep breath and leave the happy ending intact,
then bids us farewell by our own name.

Regardless of anything else, this definitively proves Chara is the
entity with the power to reset everything by the end of True Pacifist
(Which is a power we have). Flowey positively identifies us as “Chara”,
despite his mistake we discussed in 3C. He's not talking to Frisk,
because he refers to them in the third person.

He is talking to Us. Chara.

I don't want to discuss Flowey's use of “Chara” in Genocide all that
much, because the counter-argument is blindingly simple.

“By the time Flowey first says that name, Chara has overtaken Frisk by
feeding on the power we create for them.”

Of course, under PlayerChara, Flowey's lines still make sense, and
arguably more.

Implications
At this point, I believe the evidence is sufficient to support the
theory. With this in mind, I want to discuss the implications this has
on the narrative and meta-narrative. This is where all those funny
glossary terms come into play.

The pacifist route in UNDERTALE, as discussed above, is textually quite
simple when accepting PlayerChara. The meta-text is also relatively
simple. Meta textually, the Pacifist Route is a dissection of the
suspension of disbelief, examining how we emotionally place ourselves
within fictional worlds, and are often-times torn away from those worlds
as the game comes to an end, left wanting the true emotional connection,
wanting a happy ending that cannot be good enough for us because we're
real and it's not. The reflection of this meta narrative in the textual
narrative, quite naturally flows. We, Chara, want a happy ending. But we
can't have it, it's not our happy ending. We're gone. We've been gone a
long time. Frisk's happy ending can't be good enough for us, because we
won't be around to see it. So, we're left with a choice.

To let Frisk live happily? To accept an ending that might leave us
emotionally wanting, yet preserves our emotional journey?

To reset? To refuse an ending and satiate our emotional emptiness, yet
destroy that very emotional journey we took in the process?

The choice is the same. There is practically no separation between the
diegetic and the meta.

“Can a happy ending be good enough for you?” This question applies to
us, as the real world player running UNDERTALE.exe on our computer, and
us, Chara, the long deceased human who can do little but watch as Frisk
lives the life they wish they still had, or can destroy everything for a
hollow mimicry of that very life.

This message, however, breaks down under one specific circumstance.
Where we force a Third Entity into the mix. This one decision fractures
the cohesion and creates a meta-textually dissonant mess. Now, all of a
sudden, “Can a happy ending be good enough for you?” no longer runs
parallel through both narratives. There is no reason for the Player
Entity to wish to remain, the happy ending should automatically be good
enough because it's the happy ending. Meanwhile, Chara, despite being an
inextricable representation of “A happy ending I can't achieve,” gets
absolutely nothing to do with this meta-narrative because they're just…
not you.

“we are mario in Super Mario 64, but when he says "Thank you so much for
playing my game!" that doesn't mean we aren't still playing as mario” -
PopitTart

This is where things get weird. See, in the Genocide route.. Well, we
see Chara. On Screen. Talk to us.

Now, it can easily be argued that this completely shatters the theory,
but I would disagree. I'm going to endeavour to present a textual
explanation (or two) for this. But first, I want to dissect the
meta-text here.

Now, I'm sure the idea that “The Genocide Route's Meta-Narratve is
Fading Emotional Investment and the way emotional connection with video
games can lead to the very sabotage of that emotional connection” is not
revolutionary. However, what's conspicuously absent from all of the
third entity theorising is the way that this meta-text is mirrored in
the textual narrative.

Once satisfied with a game, having extracted all lines of dialogue and
stat boosts, once reaching all endings, a user will close the game down.
And at some point, perhaps to make room for a new game or perhaps on a
new device, will leave the game uninstalled, either deliberately, or
simply as a consequence of time.

Textually, what happens in the Genocide ending?
Now we have reached the absolute.
There is nothing left for us here.
Let us erase this pointless world, and move on to the next.

The world is destroyed. So much is left unanswered here.
Who is Chara talking to?
Where did Frisk go?
How do they have this much power?
Why would they want this?
If we ‘corrupted' them, what the hell does that even mean?
What is Chara?
For now, let's talk about who Chara is talking to.

The simplest answer is “Perspective switch.” Suddenly, we're not Chara
anymore, now we are Frisk. This meets all the dialogue options and even
vaguely mirrors the meta-text. It also manages to avoid bringing a third
entity along and so is automatically better! But, I find myself still
not fully enjoying this idea.

Remember what I said about Occam's Razor?

I think there's another option. One that doesn't involve three entities,
or even two entities, just Chara. One that mirrors the meta-text to a
degree only Toby Fox could pull off. It's a weird one, and I don't fault
you if you don't get it on your first read, but bear with me here,
because things are about to get

A little
Fucking
Abstract

Let's discard any and all pre-concieved notions of anything and hold one
singular truth above all else. “Chara Is The Player.” What does this
mean for this cutscene?

Well… it means the player is talking to…

THe player?

It also neatly answers the question of motive, so let's throw that out
the skeleton-shaped hole in the window for now.

If the player is talking to the player, this frames Chara's words in a
whole new light.

Every time a number increases, that feeling… That's me. “Chara.”

This line becomes explicitly literal. The Chara on-screen is literally
the player's feeling of satisfaction watching stat increases. But this
is all meta-textual, right? What does this mean for the textual
narrative?

Here's the thing. It can't mean anything, yet means everything.

There is no way to reconcile the fact that a Textually Real character is
directly talking about what the player feels when playing a game to
completion. The barrier between Meta and Textual no longer exists. It
can't. Not here. And with this revelation, everything begins to make
sense.

Your power awakened me from death.

Our power. Our desire to complete UNDERTALE awakens Chara from death.
They become startlingly real. We imbue this fictional character with the
real world desire to consume fiction, destroying enemies and worlds as
we go, increasing our power and our stats. Video Game Accomplishments.
And UNDERTALE has just finished being consumed.

My “human soul”... My “determination”... They were not mine, but YOURS.

Chara, the textual player, acknowledges the meta-textual player's
control over the game world. A control that we surrendered. By engaging
in UNDERTALE in a fully immersed way, we have fed the Diegetic character
that is our player character, Chara. This has continued until we haul
ourself out of the Internal Mode and into the External Mode, revoking
our immersion to make the consumption of content easier, to distance
ourself from the killing.

Raising our LV.

The more we distance ourselves, the less real UNDERTALE's world appears
to us. Once it's done, we're ready to erase this pointless world and
move onto the next. There's just one problem. UNDERTALE knows about us.
It knows we exist and it will abuse that to convey meaning. By revoking
our immersion in UNDERTALE, we end up shattering the barrier between
Meta and Textual, and this occurs because revoking our immersion is a
diegetic decision. Without this barrier, WE, as a character, gain
control of UNDERTALE and use this external mode control to

Erase the world. To uninstall.


This code doesn't actually work, of course. That was pretty obvious by
the fact that it didn't delete your game. But still, this exists in the
code that makes the game window shake when Chara attacks it. This is,
quite literally, intent for Chara to delete UNDERTALE. If you didn't
think Chara was capable of uninstalling your game before, you should
now.

Who is chara talking to?

Us.
How do hey have this much power?

We gave it to them. We Are them, and we deleted UNDERTALE when we were
done with it.
Why would they want this?

We wanted to move onto a new game.
What is Chara?

Us. ( I'll come back to this.)
But wait! What about soulless pacifist?
Well, at that point, you've surrendered Frisk's SOUL to Chara, as in,
you the real player has revoked your emotional attachment to UNDERTALE
and accepted that Chara can have control over the game. You've revoked
your immersion AS Chara, you no longer see yourself a Chara and as such
Chara becomes their own being. You've surrendered, basically. But they
let you play through it. Because why not. You might get attached again,
but that's fine. All that means is that the happy ending that was once
Frisk's, that you, the player, and you, Chara, both once lamented not
being able to live, has now been surrendered to Chara. A warped,
completionist, Chara.

You don't get your happy ending. But Chara does.

You don't even get the solace of knowing someone gets their happy
ending. Because Chara gets it.

Frankly, outside of being “The Player”, I don't think the exact nature
of “Chara” is that crucial. My personal thought is that they're a SOUL
fragment, absorbed by Frisk when they fell on Chara's grave (Frisk could
absorb a human SOUL fragment because said fragment was part monster
SOUL). This fragment gives Frisk the final edge of determination needed
to SAVE.

But, ultimately, that's little more than a fanfiction. And frankly, I
think that's okay. Not everything needs to be impenetrable, as long as
there's enough there to build a stable foundation.

I'd also like to address the nature of SAVING quickly, specifically the
normal version, not the Asriel fight version. People have asked “Why do
we save if it's Frisk's SOUL.” There could be many reasons. Frisk might
just defer control to us. Because we're pushing Frisk over that
Determination limit, we might be privileged to have that control.
</details>

## Changelog

not player visible

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[1552857ff4...](https://github.com/nikothedude/tgstation/commit/1552857ff44a8b481736eda843c5131ad4b761ab)
#### Saturday 2023-09-16 01:50:48 by JupiterJaeden

Balance: Removes anti-drop implants for nukies (#78275)

## About The Pull Request

Removes anti-drop implants being available in nukie implants. Also
rebalances the cybernetic implants bundle to cost 20 TC (value of 24 TC)
since anti-drop has been removed from it.

## Why It's Good For The Game

This is one of the rare few nerf PRs where I was not the one who got
KILLED by the broken OP shit but rather the one using it. I recently
played a nukie round (after hearing that anti-drop had been added) where
I took modsuit shield, dsword, and anti-drop. I got separated from my
team and then proceeded to solo murderbone half the fucking station,
resist MULTIPLE disarms that would have otherwise been successful, get
the disk alone, and nuke. I only had to stop to heal _once_ and honestly
I probably would have been fine if I didn't.

Anti-drop dsword is _insanely_ powerful. Shielded dsword nukies were
already strong enough but were at least somewhat balanced insofar as
there were several ways you could still reliably disarm them and
therefore open them up to more attacks. But now (after
https://github.com/tgstation/tgstation/pull/77330 which added the
anti-drop implants to nukie uplink) you can have shielded anti-drop
dsword nukies. Add stims and some explosives to deal with any static
fortifications the crew might make (like firelock crush relays), and
with a semi-robust player you essentially have a murderbone machine who
can't be killed by any regularly accessible crew counters short of point
blank suicide bombing. We should not have a default nukie loadout that
can only be reliably, regularly countered by a fucking bomb. Especially
since the crew's main easily accessible ballistic is now being nerfed as
well. (https://github.com/tgstation/tgstation/pull/78235)

EDIT: I'd also like to point out that we already don't allow hulks to
use dswords for many of the same reasons.

## Changelog

:cl:
balance: removed anti-drop implants from the nuclear operative uplink
balance: removed anti-drop implant from the nukie implants bundle and
changed its cost to 20 TC
/:cl:

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[172f65989e...](https://github.com/nikothedude/tgstation/commit/172f65989ea40418b1c03316ad3163ee67f06e94)
#### Saturday 2023-09-16 01:50:48 by Jacquerel

Nuclear Operative Jump Jets (#78088)

## About The Pull Request

This PR gives operative MODsuits access to "jump jets".
This is an activated module (starts pinned) with a 30 second cooldown
which removes your personal gravity for 5 seconds and (if possible)
pushes you upwards by one z level. In combination with your regular
jetpack this allows you to fly over gaps, and (most importantly) out of
pits such as you may inadvertently find yourself wandering into on
Icebox.
I have a few other changes I want to make specifically targetted at the
experience of Icebox station destruction causing people to fall several
z levels and get trapped, but this is the first one.

You have to stand still for 1 second to activate the jump jet. This is
because jetpack movement without gravity is actually usually faster than
an operative will walk, and I don't want them to just toggle it as a
sprint button while running around. If people find other tactical uses
for this though I think that's cool.

This module currently isn't available to crew on the tech web, although
maybe someone could add it later if they wanted to. It's not quite so
useful if you don't _also_ have a jetpack though.
I bumped the available complexity of the suits I attached it to up by
the complexity cost of this module so it's not taking up previously
available space.

## Why It's Good For The Game

It's funny when the whole ops team falls in a hole after an explosion
they caused and gets stuck in there fighting Snow Legions but they
should probably have some method for dealing with that.
It also lets them pop back up from the tram hole, a risky proposition
because any flying mob hit by the tram dies almost instantly.

## Changelog

:cl:
add: Operative MODsuits now have an attached "jump jet" which sends you
upwards and allows you to use your jetpack under gravity for a few
seconds, perfect for navigating the pits and valleys of Icebox Station.
/:cl:

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[ac18420676...](https://github.com/nikothedude/tgstation/commit/ac18420676c9daaa94910a1a1f4a2e2d74f0d05d)
#### Saturday 2023-09-16 01:50:48 by Hatterhat

John Splintercell: a gun that is only good for shooting out lights (#78128)

## About The Pull Request
adds the SC/FISHER lightbreaker self-charging energy pistol, which does
0 damage. As a joke.

![image](https://github.com/tgstation/tgstation/assets/31829017/84603fcd-dbc3-4857-a657-98c4bd34e881)


https://github.com/tgstation/tgstation/assets/31829017/97572baa-7421-4800-a60e-2db03f4adc6d

<details><summary>actual details, in case the video wasn't good
enough:</summary>

unless you shoot at light fixtures,

![image](https://github.com/tgstation/tgstation/assets/31829017/54092fbf-cbf6-4750-b2b8-37d643efba2a)
floodlights,

![image](https://github.com/tgstation/tgstation/assets/31829017/90b19560-fa25-471b-9f6f-3147c33e5c56)
or people with flashlights/seclites (even on helmets or guns) (it still
does 0 damage, it just turns off their lights. not permanently)

![image](https://github.com/tgstation/tgstation/assets/31829017/1a83c6f9-8fff-4035-aeeb-515319a3dd40)
it also works on crusher lights. and cyborg headlights. i don't have a
screenshot for it.
doesn't work on flares though.

also it can shoot past machines and lockers

![image](https://github.com/tgstation/tgstation/assets/31829017/8fb0a213-8e4a-42cc-9daa-eae5faf6ee77)
</details>
(also adds a variable for deciding how loud a dry fire sound is, in case
you want to make your gun's empty sound be less loud.)

## Why It's Good For The Game

Adds a silly little tool for silly little men who either really hate
lightbulbs or want to recreate the experience of being John
Splintercell, the lightbulb-assasinating secret agent from Fork Echelon.

## Changelog

:cl:
add: The SC/FISHER disruptor pistol, a very compact, permanently
silenced energy gun, is now stocked in Nanotrasen-accessible black
markets with a price generally somewhere between 400 and 800 credits.
Aspiring users are warned that it's really bad for trying to actually
kill people. Caveat emptor.
add: Guns now have a dry_fire_sound_volume variable, allowing for guns
to be less loud when trying to fire while empty.
fix: Closets and crates now properly count as structures for pass flags
again.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [zeta3301/galois](https://github.com/zeta3301/galois)@[b8343e643f...](https://github.com/zeta3301/galois/commit/b8343e643f6ef19220c9f10ba7ca0a7812ca6a8c)
#### Saturday 2023-09-16 01:57:56 by zeta3301

rewroted my stupid mistaked 2 idiotic degenerate for loops in check_mouse_hover function

---
## [aloshTM/Meteorite-Full](https://github.com/aloshTM/Meteorite-Full)@[328d03f347...](https://github.com/aloshTM/Meteorite-Full/commit/328d03f347df59fdbb7d6fbc593f4a71e137d0cd)
#### Saturday 2023-09-16 02:36:40 by alosh

Adds sushis updated one (fuck you) and adds helios fixed one

---
## [DaedalusDock/daedalusdock](https://github.com/DaedalusDock/daedalusdock)@[56b37a6e3c...](https://github.com/DaedalusDock/daedalusdock/commit/56b37a6e3c54cee460ae4b1c70970698a5e9370c)
#### Saturday 2023-09-16 03:27:18 by Kapu1178

Random things on my todo list, mostly github related (#607)

* Makes the Haunted Eight Ball work(?) (better?) (#78196)

From my recollection the haunted eight ball has been "broken" for like 3
or 4 years. So uh... yea

Makes the Haunted Eight Ball actually, like, work good.

- Fixes all votes counting to 0

- Fixes votes being reported as their vote key and not a flavor message

- Allows ghosts to change their vote

- General small code cleanup

- Calls parent in topic so stat panel clicks work

- Fixes #41718 , again? If it was actually ever fixed, not sure

:cl: Melbert
qol: Haunted 8-ball no longer requires the ghost orbit the petitioner to
submit votes
qol: Haunted 8-ball ghosts can now change their vote after submitting it
fix: Haunted 8-ball no longer always reports "yes"
fix: Haunted 8-ball no longer always reports default "yes", "no", or
"maybe" and now gives a proper eight ball response
fix: Haunted 8-ball can be picked up via the stat panel
/:cl:

* Replace DreamAnnotate action with a python script (#78225)

This PR removes the "Annotate Lints" job step and merges it with the
"Run Linters" step above. To achieve this, I wrote a python script that
should be identical to the action. I even added the ability to read the
output from a file to the script if we ever needed that, but I decided
to have the job step pipe the output into the script instead.

It always bugged me a bit that we had to check the results for a
separate step if we wanted to see the linter results for dm code. I also
noticed a few people getting confused as to why their CI failed on
linters.

Turns out that the action is just a few lines that match the
dreamchecker output and reformat it to a format that GitHub can annotate
code with. It's so brain dead simple that it shouldn't need to be a
whole new step, and for the previous two reasons.

not playerfacing

* Split Run Linters step into multiple steps (#78265)

Splits the big "Run Linters" step into multiple steps. Also since all of
these steps are independent of eachother, I've made them all run
regardless of if the job is currently failing.

<details>
<summary>Proof of testing:</summary>

Fail in install tools, all linting steps are skipped:
https://github.com/distributivgesetz/tgstation/actions/runs/6151628214/job/16692089726
Fail in Run DreamChecker, other steps continue to run:
https://github.com/distributivgesetz/tgstation/actions/runs/6151664705/job/16692203569?pr=2
</details>

<details>
<summary>Pictured: me breaking CI for a day</summary>

https://github.com/tgstation/tgstation/assets/47710522/ea12ad30-2b69-4aa3-9642-7d0818eab2d1

</details>

Going through the Run Linters step has always been a slog. Finding an
error is like finding a needle in a haystack. Seeing what command
exactly went wrong is going to go a long way in helping people find out
which linters have failed.

nothing playerfacing

* Fix some odd vscode highlighting errors in workflow files  (#78274)

few errors which were odd and annoying

stealing PRs from san7890, they wanted to do this

nothing playerfacing

* fuck

* fuck 2

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>

---
## [Karlesjay/2A-Escala-Joshua-1S2324-P1-P2](https://github.com/Karlesjay/2A-Escala-Joshua-1S2324-P1-P2)@[3ed6c351a8...](https://github.com/Karlesjay/2A-Escala-Joshua-1S2324-P1-P2/commit/3ed6c351a883d611889a6bc10ab8bd3bbb8a4572)
#### Saturday 2023-09-16 04:26:09 by P-Elec-2-BSIT-2A-1S2324-Noynay-Karl

Add files via upload

Good Morning Sir Joshua Escala, I'm Karl A. Noynay BSIT-2A 
This is My Assignment in P Elec 1 
"Create a program in java that can accept user input and display it Right after using OOP".

Please ko Sir Salamat kaau and God Bless you po.

---
## [Dragonrster/The-Powder-Toy-Chinese](https://github.com/Dragonrster/The-Powder-Toy-Chinese)@[b99914bac5...](https://github.com/Dragonrster/The-Powder-Toy-Chinese/commit/b99914bac59722bffc53f39eb36baf8cde8539ec)
#### Saturday 2023-09-16 05:28:47 by Tamás Bálint Misius

Fix crash from Lua prompts when exiting the game completely

The problem is that Engine outlives GameController and thus also LuaScriptInterface. The solution is to not try to access LSI's lua_State if it doesn't exist; this is the case in Engine's dtor.

This is ugly as hell and the root of the problem is the cursed ownership model of LuaComponents and Windows by Engine, which I don't think I'll be fixing any time soon.

---
## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[f6a02a6c73...](https://github.com/francinum/Therac-Gameserver/commit/f6a02a6c73d12d6e904c863697246ac02255521f)
#### Saturday 2023-09-16 06:11:36 by Francinum

FUCK YOU BALTIMORE
IF YOU'RE BUYING A NEW COMPUTER SYSTEM THIS WEEKEND I HOPE YOU'RE READY
TO BE CHARGED OUT THE ASS FOR BASIC FEATURES
AUTORUN, STOLEN STRAIGHT FROM BAY'S DECAYING CORPSE.

ALL FOR THE LOW LOW PRICE OF MY SANITY

---
## [BurnerWah/BurnerWah](https://github.com/BurnerWah/BurnerWah)@[72e0981ef4...](https://github.com/BurnerWah/BurnerWah/commit/72e0981ef431e6fd9c6825d5a5a928a8ba59acad)
#### Saturday 2023-09-16 06:39:59 by Burner

Update README.md

honestly nim and scala are too shit to warrant mention, but i will almost unconditionally refuse to use them

trash launguages that can die for all i care

---
## [SpaceLoveSs13/Skyrat-tg](https://github.com/SpaceLoveSs13/Skyrat-tg)@[34306b4266...](https://github.com/SpaceLoveSs13/Skyrat-tg/commit/34306b4266e0cc8219d0bb9ca809350ec4035d3f)
#### Saturday 2023-09-16 06:43:47 by SkyratBot

[MIRROR] Buffs Heretic ash ascension [MDB IGNORE] (#23114)

* Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

* Buffs Heretic ash ascension

---------

Co-authored-by: DaydreamIQ <62606051+DaydreamIQ@users.noreply.github.com>

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[8248bb90df...](https://github.com/Hatterhat/Skyrat-tg/commit/8248bb90df5efaf15a2b3a946c5bae28f0288189)
#### Saturday 2023-09-16 06:55:09 by SkyratBot

[MIRROR] Polymorph belt blacklists several biotypes instead of allowing only organics [MDB IGNORE] (#23620)

* Polymorph belt blacklists several biotypes instead of allowing only organics (#78229)

## About The Pull Request

Title; this makes the belt able to morph into _more_ mobs, but _less
problematic/abusable_ mobs hopefully. It still only functions on
basic/simple_animals, however.

~~Headslugs get a `MOB_UNDEAD` bioflag to prevent morphing into them
completely. Though catching a sentient ling slug and morphing everyone
into it is funny, it's only funny the first 5 times someone does it.
(disclaimer: this is an approximation, i did not actually see a
polymorph belt in-game because i currently play miner and like 10 games
a week tops)
Arguably, this isn't ideal, but it's the closest we get unless we rename
`MOB_EPIC` or something into `MOB_SPECIAL` and let that one be the go-to
bioflag for mobs we don't want **fun** things happen to.~~
`MOB_EPIC` is now `MOB_SPECIAL`. Headslugs get that.
I think the alternative methow could use whatever the gold cores use to
determine what to spawn but that would shift the mobs available for the
belt even more and I can't be assed to figure out how _much_ of a shift
that would be. Dragons or slimes or lavaland mobs would be out, for
example. Don't really vibe with that.

Fixes headslug's description bit that discerns a sentient slug from an
AI one showing up on a dead slug. It can't move while it's dead, no
matter its mind/AI.

Also adds simple dmdoc comments to the defines to help discern a few of
them more easily. Non-quip text suggestions welcome.

## Why It's Good For The Game
- Resolves #77756
- Resolves #78227

More mobs available for the funny belt but less _fun_ mobs should allow
for more stable use of the damn thing. Arguably, some of the mobs that
have been found to be incompatible with the belt are simply lacking a
`MOB_ORGANIC` flag, some of them with no apparent reason. However,
blacklisting potentially problematic biotypes should be easier to design
the unwanted mobs around.
Also consistency, less all-ling stations, code clarity. Whatever.

## Changelog

:cl:
balance: polymorph belt now blacklists mobs that are undead, humanoid,
robotic or spiritual (in nature, not religiously), as well as megafauna
balance: however, this means that it works with more mobs that it should
logically work with, like slimes/bugs/lightgeists etc
fix: fixed headslug shenanigans with the polymorph belt hopefully for
good this time
fix: fixed headslug description mentioning its movement despite the slug
being dead
/:cl:

* Polymorph belt blacklists several biotypes instead of allowing only organics

---------

Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>

---
## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[452d6cbdc7...](https://github.com/francinum/Therac-Gameserver/commit/452d6cbdc7a8c4d3153dccc19ba1426f22d98531)
#### Saturday 2023-09-16 07:52:08 by Gallyus

I hate asset code (#341)

315 fucking icon states
goddamnit it lemon boy what the fuck were you thinking

---
## [notlulz/tgstation](https://github.com/notlulz/tgstation)@[c571222cd7...](https://github.com/notlulz/tgstation/commit/c571222cd79b0d8eab5f18846b43e2af559a6999)
#### Saturday 2023-09-16 07:59:21 by san7890

Readds (some) Knockdown Vomits (#78301)

## About The Pull Request

ALL stunning vomits were nerfed to have just a motionless stun in #70245
(14438a2b7d5d781c340713983f8f07fb09179f08), and while it didn't really
affect game balance beyond just making you not fall on the floor... I
really didn't like it since it was all-or-nothing. Fortunately with
#78191 (a7060641bb0165a7531a3cee007989d9e95741ee), we are able to add
more expression to how a vomit should go down using the new bitflag
system, so I decided to rewrite it back in for a special number of
cases.

I only did it for two cases, but anyone is free to change anything they
think they deserve it via changing the vomit flags that are passed into
the proc. Those cases are:

* Places where you vomit after spinning too hard. You lost balance and
threw up. That makes more sense to me than just being suddenly and
completely motionless without any sign of loss of inertia.
* Organ heal rejections. You literally vomit out an organ. How are you
still standing up? Beyond making no sense in anatomy, you should really
feel the _oomph_ from literally puking out an organ.
## Why It's Good For The Game

This is a bit of flavor that really ensaddened me when I realized it was
removed because it really does miss out on the real and true impact.
While I do agree with some merits of the aforementioned balance PR that
removed it, I do not think that it works at all for a blanket case. Now
that we are able to add this expression, we should, because it's cool.

Also cleaned up some comments I forgot to update from the last time.
## Changelog
:cl:
balance: You will be knocked down again on certain vomits. Don't worry,
you'll deserve it when it happens.
/:cl:

---
## [KA101/KeeperRLCommunityResources](https://github.com/KA101/KeeperRLCommunityResources)@[bdce4cb14e...](https://github.com/KA101/KeeperRLCommunityResources/commit/bdce4cb14e4de520597ec7ff24fa615f72893fcd)
#### Saturday 2023-09-16 08:00:15 by KA101

Buff the beauties

Was asked a while ago to give the combat succubae their touch/love as an additional attack along with weaponry: they just weren't effective as-was.

(And BLEEP is the Extra-Attack syntax a pain for this non-programmer.)

After some experience in A37, opted to also buff their training and base spell-damage.  If I had more energy I'd write them a spellbook to go with.

(Remember! these ladies require Sorcery->AdvSorcery->Demonology->Combat_Succubus: you're dungeon-lvl 2 at ABSOLUTE minimum, more likely 3-4 as minimum, and realistically, closer to 8-10.  They're a mid-to-late game unit.)

---
## [Kirillcas/tgstation](https://github.com/Kirillcas/tgstation)@[72174845f5...](https://github.com/Kirillcas/tgstation/commit/72174845f5b417bf0cbd3f4a8fc66835b052acf8)
#### Saturday 2023-09-16 08:49:20 by Jacquerel

Basic Watchers & Basilisks (#77630)

## About The Pull Request

This one is a double feature because Watchers and Basilisks share the
same typepath. You might see a couple more of those.
As is tradition I decided to fuck with them rather than just port them.
Here's what's up.

**Basilisks**

![image](https://github.com/tgstation/tgstation/assets/7483112/9e4b0115-65dd-4df7-b62a-21c7be8549bf)

![image](https://github.com/tgstation/tgstation/assets/7483112/59162e68-7d73-4659-9531-5078ff751228)

- Have a new soulless sprite which looks less like a living blue hedge.
- Walk at you and shoot you while you are not in range (just like
before).
- Become supercharged if they become "heated" by lava, lasers, or
temperature weapons. This was a feature they also previously had but
they would never encounter lava, so now it also works if you use the
wrong gun on them.
- Lose their supercharge if you cool them down.
- Otherwise pretty normal mobs.

**Watchers**

https://www.youtube.com/watch?v=kOq_Bf78k5A
Here's a traditional video of me intentionally getting hit by mechanics
(trust me its definitely on purpose)

- They glow emmissively a little bit so you can see them from further
away.
- Their eyes light up about 0.5 seconds before they are able to shoot at
you.
- No longer melee attack, instead try to stay out of melee.
- Will occasionally put you into "Overwatch", meaning they will shoot
you rapidly if you move or act while they're staring at you for a brief
time period (after which you become immune for 12 seconds, and during
which other watchers will play fair and stop shooting at you).
- If they start taking damage they will also start using their "Gaze"
attack, look away or suffer some kind of negative effect!
- - Normal watcher gaze flashes and confuses you.
- - Magmawing watcher gaze obviously burns (and briefly stuns) you.
- - Icewing watcher gaze freezes you and throws you backwards.
- Magnetically attract and eat diamonds. They also used to do this, but
just if they happened to coincidentally walk past some.

**Other accompanying changes**

All basic mobs will now adopt the "stop gliding" trait if they get
slowed down too much.
I moved behaviour for "fire a projectile from this atom" into a helper
proc because I was using it in three places and I will probably use it
in more places. There are probably other places in the existing code
which could be using this.
I think I made the basic mob melee attack forecast default a little more
forgiving, they were fucking me up too much and I am the playtester.

## Why It's Good For The Game

Another one off the list.
New tricks for old dogs.
Framework for making mobs with ranged attacks "fairer" (you can see when
they are ready to shoot you).
More (hopefully) versatile AI behaviours which we will reuse later (I
hope I'm not duplicating one someone already made).
If our players "enjoy" them enough we can give more mobs "don't look at
me" mechanics.
Removes some soul sprites.

## Changelog

:cl:
refactor: Basilisks and Watchers now use the basic mob framework. Please
bug report any unusual behaviour.
sprite: Basilisks have new sprites.
add: Basilisks will go into a frenzy if heated by energy weapons or
temperature beams as well as by lava.
add: Watcher eyes will be illuminated briefly when they are ready to
fire at you.
add: Watchers can now briefly put you into "Overwatch" and penalise you
for moving while they can see you.
add: Wounded watchers will occasionally punish players who look at them.
balance: Unusual watcher variants are more likely to appear.
/:cl:

---
## [retlaw34/Shiptest](https://github.com/retlaw34/Shiptest)@[b22529fc74...](https://github.com/retlaw34/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Saturday 2023-09-16 09:33:14 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [retlaw34/Shiptest](https://github.com/retlaw34/Shiptest)@[ee4021c507...](https://github.com/retlaw34/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Saturday 2023-09-16 09:39:48 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [LizzardHD/Hotkey-Manager](https://github.com/LizzardHD/Hotkey-Manager)@[7d7af13ec6...](https://github.com/LizzardHD/Hotkey-Manager/commit/7d7af13ec67674b88136ad956fa223206eb9b871)
#### Saturday 2023-09-16 10:32:17 by LizzardHD

Here's a high-level review of your code:

Organization and Structure:

The code is structured into sections for Hotkey Function, Update/Feedback/Data Functions, Main GUI Functions, and GUI Basic Structure, which is good for readability.
Global Variables:

Be cautious about using too many global variables. It can make the code harder to manage and debug. Consider using classes or functions to encapsulate related data and functionality.
Threading:

It's essential to manage threading carefully. Ensure that threads are started and stopped correctly to prevent issues like freezing the GUI or not being able to stop threads.
GUI Layout:

The GUI layout seems well-organized with frames for different components.
Action Management:

Managing actions with a list of tuples (action type, action value) is a good approach. It allows flexibility in defining actions.
OptionMenu for Hotkeys:

The use of OptionMenu for selecting hotkeys is user-friendly.
Terminal Display:

The terminal display for messages is a helpful feature for user feedback.
Saving and Loading Data:

Saving and loading actions to/from JSON files is a good way to persist data between runs.
Now, let's provide some comments and suggestions for improvement:

Consider encapsulating related functionality into classes or functions to reduce the reliance on global variables and improve code organization.

Ensure that threading is correctly managed, especially when starting and stopping threads. Avoid using global flags for this purpose, as it can lead to synchronization issues.

Add more detailed comments explaining the purpose of each function and class, input parameters, return values, and how they fit into the overall application.

Break down long functions into smaller, more manageable functions with specific responsibilities. This will improve code maintainability.

Consider using constants or enumerations for action types ("Sleep," "Mouse Click," etc.) to avoid hardcoding these values.

Validate user inputs, especially when loading actions or entering action names. Ensure that the code handles edge cases gracefully.

Consider implementing error handling to catch and handle exceptions that may arise during the program's execution.

For a user-friendly experience, you can provide tooltips or tooltips-like help messages to explain the purpose of buttons and UI elements when users hover over them.

Ensure that the UI remains responsive even when long-running operations are in progress. You can achieve this by running time-consuming tasks in separate threads and providing feedback to the user.

Continuously test the application with different scenarios to identify and address potential issues or edge cases.

Remember that improving a large codebase is an iterative process, so you can gradually make these improvements over time. Additionally, consider using version control (e.g., Git) to track changes and collaborate on improvements.

---
## [EuansPrivateORG/DemonGame](https://github.com/EuansPrivateORG/DemonGame)@[6250525b73...](https://github.com/EuansPrivateORG/DemonGame/commit/6250525b73897a7067fb97a22ba30659b27c5c05)
#### Saturday 2023-09-16 10:55:58 by AIE\s200552

REALTIME CSG I LOVWE YOU HOLY SHIT I GOD DAM HATE WHEN THIS ASTUPID BUGH KEEEORPS SDHIASHOWEING UPS

---
## [Aurorastation/Aurora.3](https://github.com/Aurorastation/Aurora.3)@[652a3d02d4...](https://github.com/Aurorastation/Aurora.3/commit/652a3d02d4260aea7f34c64814f409a677b063a0)
#### Saturday 2023-09-16 11:01:54 by Wowzewow (Wezzy)

Adds Storage Container Animations (#17329)

* Much ado about the Bagginses

* god i hate manually mapped shit

* Update code/game/objects/items/weapons/storage/storage.dm

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>

* fixes

* yes

* Update code/game/objects/items/weapons/storage/bags.dm

Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---------

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>
Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---
## [praymeta/Code-Up-Algorithm](https://github.com/praymeta/Code-Up-Algorithm)@[20df56fb2b...](https://github.com/praymeta/Code-Up-Algorithm/commit/20df56fb2b0e55f7062ef5025fc81f2711bd5da8)
#### Saturday 2023-09-16 11:34:27 by 이혁준

백준 29986: Altura Mínima(Minimum Height)

Carlitos is an adventure enthusiast with an insatiable love of amusement parks. Despite his vibrant passion, Carlitos faces a unique challenge: his limited height. As he anxiously plans his weekend adventure, he realizes that his vertical limitations may get in the way of his amusement park experience. It's not just about choosing a park; it's about finding one where he can enjoy the thrill of the rides.

Imagine the kaleidoscope of colors, the jubilant laughter and the adrenaline rush of the rides. Carlitos has always been attracted to the energy of amusement parks. As the weekend approaches, he pores over the park brochures, studying the height requirements of each ride. His goal is to maximize your enjoyment, and that's where you come in.

Your task is to help Carlitos determine the number of rides he can enjoy in a specific park. Considering his height and the minimum height requirements of each ride, guide him to make the most of his amusement park adventure.

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[ed10226825...](https://github.com/lizardqueenlexi/orbstation/commit/ed10226825bbef4e605d7e831ebb1d8f30f805f4)
#### Saturday 2023-09-16 12:09:05 by Jacquerel

Desouls Hivelord (#78213)

## About The Pull Request


![dreammaker_RJz4brjobM](https://github.com/tgstation/tgstation/assets/7483112/e5e4a3e9-ea6b-47f9-887c-3339d24d3fa8)

Replaces the sprite of the hivelord with a new one, in my continuing
quest to annihilate the old asteroid mob sprites.
A (never completed) asteroid mob resprite was actually my first PR, this
one is my 200th.
I am also planning on fucking with basic mob versions of these mobs some
time but the sprites can be atomised out.

In addition to replacing the old-ass MSPaint sprites, this PR also adds
a short death animation effect to the hivelord brood (from hivelords or
legions) which looks nicer than them just vanishing instantly upon
death.

Look at this video for an example of the animation:
https://www.youtube.com/watch?v=cKaskN5-y2A

## Why It's Good For The Game

Looks nicer.

## Changelog

:cl:
image: Hivelords have a new sprite.
image: Hivelord and Legion brood have a death animation.
/:cl:

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[009af8c2ce...](https://github.com/lizardqueenlexi/orbstation/commit/009af8c2ce5c18ca4fdaceb4e4d2c17d8e8d6d00)
#### Saturday 2023-09-16 12:09:05 by nikothedude

[TEST-MERGE FIRST] Wound refactor number two: Full synthetic support (#78124)

## About The Pull Request

Heavily refactors wounds AGAIN.

The primary thing this PR does is completely change how wounds are
generated and added - while the normal "hit a guy til they bleed" stuff
works about the same, asking for a specific type of wound, say, like how
vending machines try to apply a compound fracture sometimes, isnt going
to work if we ever get any non-organic wounds, which the previous
refactor allowed.

With this PR, however...
* You can now ask for a specific type of wound via
get_corresponding_wound_type(), which takes wound types, a limb, wound
series, etc. and will try to give you a wound fitting those
specifications - but also, a wound that can be applied to a limb.
* This will allow for a vending machine to apply a compound fracture to
a human, but a collapsed superstructure (assuming my synth wounds go in)
to a robot

There are now new "series types" and "wound specific types" that allow
us to designate what series are "mainline" and randomly generatable, and
what are "alternate types" and must be generated manually - you can see
the documentation in wounds.dm.

The behavior of limping and interaction delays has been abstracted to
datum/wound from bone wounds to allow just, general ease of development

Pregen data now allows for series-specific wound penalties. Example: You
could set a burn wound's series wound penalty to 40, which would make
wound progression in the burn category easier - but it would not make it
any easier to get a slashing wound. As it stands wound penalties are for
wounds globally

Scar files are now picked in a "priority" list, where the wound checks
to see if the limb has a biostate before moving down in said list.
Example: Wounds will check for flesh first, if it finds it - it will use
the flesh scar list. Failing that, they then check bone - if it uses
that, it will use the bone scar list. This allows for significantly more
modular scars that dont even need much proc editing when a new wound
type is added

Misc changes: most initial() usage has been replaced by singleton
datums, wound_type is now wound_types and thus wounds can accept
multiple wound types, wounds can now accept multiple tool behaviors for
treatment, wounds now have a picking weight so we can make certain
wounds rarer flatly,

This PR also allows for wounds to override lower severity wounds on
generation, allowing eswords to jump to avulsions - but in spirit of
refactoring, this has been disabled by default (see pregen data's
competition_mode var).
## Why It's Good For The Game

Code quality is good!

Also, all the changes above allow wounds to be a MUCH more modular
system, which is one of its biggest problems right now - everything is
kinda hardcoded and static, making creative work within wounds harder to
do.

## Changelog
:cl:
refactor: Refactored wounds yet again
fix: Wounds are now picked from the most severe down again, meaning
eswords can jump to avulsions
fix: Scar descs are now properly applied
/:cl:

---
## [ggoni/ml-design-patterns](https://github.com/ggoni/ml-design-patterns)@[37110a3269...](https://github.com/ggoni/ml-design-patterns/commit/37110a32691d8c63d3c52b842c36e84a3128a9fe)
#### Saturday 2023-09-16 12:34:10 by Robert Lacok

Include a link to open the project 

Hey, I'm reading through the book and thoroughly enjoying it, thanks @lakshmanok! 

I have some trouble viewing the notebooks here on GitHub though (it keeps saying "Sorry, something went wrong", likely hitting some size limits).

I work at Deepnote, and we try to build better data science notebooks. The proposed button opens the repo as a project in Deepnote, and you can view and execute all of the files – it might be helpful for other readers too :)

---
## [xiaomi-mt6765-devs/android_kernel_xiaomi_mt6765](https://github.com/xiaomi-mt6765-devs/android_kernel_xiaomi_mt6765)@[8bddce881a...](https://github.com/xiaomi-mt6765-devs/android_kernel_xiaomi_mt6765/commit/8bddce881ac1ab6dd3da2e1504601eeb2e84b170)
#### Saturday 2023-09-16 12:38:40 by Douglas Anderson

serial: core: Allow processing sysrq at port unlock time

[ Upstream commit d6e1935819db0c91ce4a5af82466f3ab50d17346 ]

Right now serial drivers process sysrq keys deep in their character
receiving code.  This means that they've already grabbed their
port->lock spinlock.  This can end up getting in the way if we've go
to do serial stuff (especially kgdb) in response to the sysrq.

Serial drivers have various hacks in them to handle this.  Looking at
'8250_port.c' you can see that the console_write() skips locking if
we're in the sysrq handler.  Looking at 'msm_serial.c' you can see
that the port lock is dropped around uart_handle_sysrq_char().

It turns out that these hacks aren't exactly perfect.  If you have
lockdep turned on and use something like the 8250_port hack you'll get
a splat that looks like:

  WARNING: possible circular locking dependency detected
  [...] is trying to acquire lock:
  ... (console_owner){-.-.}, at: console_unlock+0x2e0/0x5e4

  but task is already holding lock:
  ... (&port_lock_key){-.-.}, at: serial8250_handle_irq+0x30/0xe4

  which lock already depends on the new lock.

  the existing dependency chain (in reverse order) is:

  -> #1 (&port_lock_key){-.-.}:
         _raw_spin_lock_irqsave+0x58/0x70
         serial8250_console_write+0xa8/0x250
         univ8250_console_write+0x40/0x4c
         console_unlock+0x528/0x5e4
         register_console+0x2c4/0x3b0
         uart_add_one_port+0x350/0x478
         serial8250_register_8250_port+0x350/0x3a8
         dw8250_probe+0x67c/0x754
         platform_drv_probe+0x58/0xa4
         really_probe+0x150/0x294
         driver_probe_device+0xac/0xe8
         __driver_attach+0x98/0xd0
         bus_for_each_dev+0x84/0xc8
         driver_attach+0x2c/0x34
         bus_add_driver+0xf0/0x1ec
         driver_register+0xb4/0x100
         __platform_driver_register+0x60/0x6c
         dw8250_platform_driver_init+0x20/0x28
	 ...

  -> #0 (console_owner){-.-.}:
         lock_acquire+0x1e8/0x214
         console_unlock+0x35c/0x5e4
         vprintk_emit+0x230/0x274
         vprintk_default+0x7c/0x84
         vprintk_func+0x190/0x1bc
         printk+0x80/0xa0
         __handle_sysrq+0x104/0x21c
         handle_sysrq+0x30/0x3c
         serial8250_read_char+0x15c/0x18c
         serial8250_rx_chars+0x34/0x74
         serial8250_handle_irq+0x9c/0xe4
         dw8250_handle_irq+0x98/0xcc
         serial8250_interrupt+0x50/0xe8
         ...

  other info that might help us debug this:

   Possible unsafe locking scenario:

         CPU0                    CPU1
         ----                    ----
    lock(&port_lock_key);
                                 lock(console_owner);
                                 lock(&port_lock_key);
    lock(console_owner);

   *** DEADLOCK ***

The hack used in 'msm_serial.c' doesn't cause the above splats but it
seems a bit ugly to unlock / lock our spinlock deep in our irq
handler.

It seems like we could defer processing the sysrq until the end of the
interrupt handler right after we've unlocked the port.  With this
scheme if a whole batch of sysrq characters comes in one irq then we
won't handle them all, but that seems like it should be a fine
compromise.

Signed-off-by: Douglas Anderson <dianders@chromium.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [lilypond/lilypond](https://github.com/lilypond/lilypond)@[36161db800...](https://github.com/lilypond/lilypond/commit/36161db80089ee75b27f8def40a1af0c5ef0af23)
#### Saturday 2023-09-16 12:47:01 by Jonas Hahnfeld

Remove validation link from website

Having these links and icons was a fashion some years ago, but that
seems to have mostly faded. And the placement on our website looks
quite ugly (in my opinion). Moreover, HTML 4.01 Transitional is not
the latest and greatest anymore, long live HTML 5!

Funnily enough, the added div actually introduces an error since commit
1edb8b3c85 removed the opening paragraph in the hosting_thanks that is
still closed after the validator link. As far as I can tell, it is the
only validation error...

---
## [Mycah142/CEV-Eris](https://github.com/Mycah142/CEV-Eris)@[912aefa27e...](https://github.com/Mycah142/CEV-Eris/commit/912aefa27ee5cc13836f6969b91aea649f6b016c)
#### Saturday 2023-09-16 13:02:45 by Mycah142

fug u leopold

you smarmy bitch fuck your stupid ass unused room I can't wait to put you on meat spikes in it I swear on me mum

---
## [crtoled/ip-public](https://github.com/crtoled/ip-public)@[fc5cf3be71...](https://github.com/crtoled/ip-public/commit/fc5cf3be714284b8b8ba9a74ac7c5229f5644edd)
#### Saturday 2023-09-16 13:39:30 by SA

Merge branch 'main' of https://github.com/crtoled/ip-public into main
fuck you

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[e69e59e2a8...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/e69e59e2a80635e1e23cc79493c92cc87589170f)
#### Saturday 2023-09-16 14:32:49 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>
Signed-off-by: pix106 <sbordenave@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [milansinghal2004/SQL](https://github.com/milansinghal2004/SQL)@[feaba1a107...](https://github.com/milansinghal2004/SQL/commit/feaba1a107342e46ac72035278849f80ef9f8cec)
#### Saturday 2023-09-16 14:33:09 by MILAN SINGHAL

Practice problem - WHERE QUERY

Let us combine what we have learnt from our 'SELECT', 'DISTINCT' and 'WHERE' queries.
From the 'Flights' table - let us find the following
Where the origin of the flight is 'New York'
Output the passenger_name and gender
Expected Output
┌────────────────┬────────┐
│ Passenger_name              │ Gender         │
├────────────────┼────────┤
│ Dia                                    │ Female         │
│ Jackson                            │ Male             │
└────────────────┴────────┘
Remember that the column details are as follows
Passenger_id
Passenger_name
Gender
Origin
Destination

---
## [RohanFredriksson/PokePad-v2](https://github.com/RohanFredriksson/PokePad-v2)@[ec775daff7...](https://github.com/RohanFredriksson/PokePad-v2/commit/ec775daff7ee6941329846cb7ad53971eef754bd)
#### Saturday 2023-09-16 14:56:51 by Rohan Fredriksson

Merge pull request #1 from RohanFredriksson/RohanFredriksson-patch-1

Fuck you

---
## [honeyjain22/Pizza-Plane-Sales](https://github.com/honeyjain22/Pizza-Plane-Sales)@[ecfc1b9416...](https://github.com/honeyjain22/Pizza-Plane-Sales/commit/ecfc1b9416d639ab9ccf78b845577a66d6f22ead)
#### Saturday 2023-09-16 15:06:51 by Honey jain

https://drive.google.com/drive/folders/1ysRthmH0DoVkol8VddeOj57_B0fIJR4b?usp=sharing

Exploring Seasonal Variations in Pizza Sales: Analyzing Monthly Trends and Factors Influencing Sales Fluctuations.

Analyzing Sales by Time of Day: Understanding Breakdowns and Identifying Opportunities for Targeted Marketing.

Unlocking Pizza Preferences: Examining Sales by Category and Demographics to Drive Business Growth.

These revised lines provide a clearer and more concise description of the project's objectives and areas of analysis within the context of pizza sales.

According to data on monthly pizza sales, there are seasonal variations in sales, with some months having lower sales than others. The project may explore possible causes of these variations, such as seasonal factors, promotional activity, or modifications in consumer behaviour.

The breakdown of pizza sales during the morning, afternoon, and evening hours is seen in the data on sales by time of day. The project could study how this breakdown differs by category and whether there are chances to boost sales at particular times of the year.

Last but not least, information on pizza sales by category offers insight into the most well-liked pizza varieties among consumers. The project might look into customer demographics, pizza preference patterns, and possible markets for fresh pizza selections.

The overall goal of the Pizza Sales Project seems to be to better understand pizza sales trends and locate chances to increase sales through the use of data analysis. The project may include suggestions for marketing and promotion plans, adjustments to the menu, or other techniques designed to boost sales and promote business expansion.

---
## [Aztorius/android_kernel_sony_sdm660](https://github.com/Aztorius/android_kernel_sony_sdm660)@[769969b9f3...](https://github.com/Aztorius/android_kernel_sony_sdm660/commit/769969b9f319e5b44ab0f78b796401a7ec9dbd36)
#### Saturday 2023-09-16 15:09:36 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [HEPOSHEIKKI/icecast2-web](https://github.com/HEPOSHEIKKI/icecast2-web)@[bddf883cf1...](https://github.com/HEPOSHEIKKI/icecast2-web/commit/bddf883cf12a64477a1a2fc72cf78bb1645a6d9f)
#### Saturday 2023-09-16 15:59:29 by HEPOSHEIKKI

Fixed a chromium issue (fuck chromium, it's nothing than a pain in my ass nothing works, I got no issues on FF or Safari but chromium as the dominant browser decides to fucking not work)

---
## [HEPOSHEIKKI/icecast2-web](https://github.com/HEPOSHEIKKI/icecast2-web)@[276d0f5aee...](https://github.com/HEPOSHEIKKI/icecast2-web/commit/276d0f5aeebab3a7106e0db4614fa4b2fa5b89c0)
#### Saturday 2023-09-16 16:04:14 by Otto

Added usage because chromium

Seriously chromium is a flaming piece of shit web browser, every other browser works flawlessly with my code with no effort from my side, but chromium, noooo it's too good, too elite for us, normal people and it needs tailored fucking code to play back a god fucking mp3 file.

---
## [Indev450/SRB2Kart-Saturn](https://github.com/Indev450/SRB2Kart-Saturn)@[b53cc6fd2b...](https://github.com/Indev450/SRB2Kart-Saturn/commit/b53cc6fd2bb75d8a7bc15e3277c39990bc189851)
#### Saturday 2023-09-16 16:11:14 by lug420

fuck it palette renderer "lite"

remove the goddamn lookup textures, this atleast runs okish and looks not that bad

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b884200483...](https://github.com/treckstar/yolo-octo-hipster/commit/b884200483e5763ab26fd8c41e04687ba3024d55)
#### Saturday 2023-09-16 17:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [brando90/beyond-scale-language-data-diversity](https://github.com/brando90/beyond-scale-language-data-diversity)@[4953161976...](https://github.com/brando90/beyond-scale-language-data-diversity/commit/495316197635763566ef271db1cdf2f7512934cd)
#### Saturday 2023-09-16 17:29:34 by Brando Miranda

Create plan_div_performance_ginc.md

# Experiment Plan: The Effect of Diversity on Downstream Performance 

## Goal

Essential Goal: Does pre-training on a highly diverse data set lead to high performance on pre-training evaluation sets?
(note: it's more of a causation than a correlation experiment).

## Experiment Plan 1: Concepts in pre-train set intercepting concepts in test set

1. Fix an eval synthetic GINC data set with 10K concepts (~0.024 diversity coeff. with probe network ... TODO1: what is the probe network? whatever ginc alycia used should be fine),
denote it as `C_{test, 10k, ginc}` and generate a data set `D_eval = D_{test, 10k, ginc}` with `n= ?` examples (TODO2 same as alycia's, or original ginc or something that seems reasonable, if I had to guess at least 30 due to CLT but would choose 500 or a sample complexity guess from learning MHHMs or ask Michael original ginc author)`. 
2. Sample `k <= 10K` concepts from `C_{test, 10k, ginc}` to generate a pre-training data set `D_{tr, k, ginc}` using concpets `C_{tr, k, ginc}`.
3. Compute the diversity of the data set of the previous step and denote it as `div_k = div(D_{tr, k, ginc})`.
4. Pre-train a sufficiently large (e.g., deep) transformer model (TODO3: whatever alycia, michael used for ginc, I think it's a custom GPT/decoder model? I strongly recommend a decoder model)
5. Now start plotting 
   6. A (Ess): `x-axis = div_k vs y-axis = performance_i(D_eval)` (tests main hypothesis/essential goal)
   7. B (Ess): `x-axis = align(D_k, D_eval) vs y-axis = performance_i(D_eval)` (sanity check, tests `if as the alignment in pre-train & test set increases ==> increase in performance`)
   8. C (Ess): `x-axis = div_k  vs align(D_k, D_eval)` (sanity check, `if the diversity increases then ==> increases probability of covering test sets which ultimately ==> increases alignment`)
   9. (D (extra): `x-axis = delta in alginment(D_k', D_eval) vs performance_i(D_eval)` (hypothesis, does the most aligned data added cause the most increase in performance?))
   10. (E (extra): `x-axis = div vs ground truth div` (sanity check div correlates with ground truth div))

Then repeat from step 2 but with a different `k` until `k==10k`. 
Alignment is how aligned is the pre-train & test sets with formulas 
- `alg1(D_k, D_eval) = 1 - div(D_k, D_eval) = 1 - E_{B1 ~ D_k, B2 ~ D_eval}[d_cosine(e_{B1}, e_{B2})]`
- `alg2(D_k, D_eval) = d_cosine(e_{D_k}, e_{D_eval})`

Where `e_{D}` is the Task2Vec embedding (diagonal of the FIM of probe network).

Hypothesis being tests, Rational:
- First let's validate/falsify that if the train set has latent concepts samples exactly from the concepts from the test set, if the eval. performance increases. 
  - Sanity check: This is the simplest scenario, if this doesn't work, it might still be worth sampling different concepts to generate the data set, but I wouldn't expect the latter to work, right?
- test if diversity increase ==> performance eval 
- Sanity Check: as `div increases ==> alignment increases`?

Assumptions/Risk:
- Assumption 1: when plotting `performance_i(D_eval)` we will choose at least 3 metrics `i. ppl, ii. token edit distance (or avg token match), iii. extract string match`
- Assumption 2: the model is **sufficiently large** so that even if the diversity increases by "too much", it won't catastrophically forget or new knowledge would interfere with past knowledge.
- Assumption 3: using performance in the y-axis is enough to detect difference (statistical significant)
  - if we can't detect a difference, perhaps we can use effect size in the y-axis?
- Assumption 4: the code alycia has is easy to run + the architecture they have will be easy to train. 
  - wonder if EasyLM (llama v1 or v2 arch would be better?). Ask easy LM when they will include the better llama v2 arch
  - ask on Twitter why llama v2 trains so stably

Comments:
- note: even though the concepts intersect, the sequences are being generated independently (e.g., with a different seed), so there isn't a contamination from the pre-train set to the test set.
- note: I prefer token edit distance vs avg token match, it's similar to average token error but it's more accepted in the NLP literature (TODO: recall from Rylan why it's a good metric).
- note: **comparisons must be fair** e.g., effectively we must only change the data set (and thus diversity) in the experiments when comparing the performance of different methods. 
  - I suggest we fix: 1. arch 2. compute FLOPS (TODO4: get Rylan's formula) 3. tokens trained on/iterations 4. optimizer 5. anything else?
- not essential but if the experiments work it would be nice to have the diversities normalized in this way: `div'_k = (div_k - min_{D} div(D)) / max_{D} div(D)` i.e., center according to the lowest div divide by the largest diversity.

Decision & justifications for TODOs:
- TODO1 Ans: 
- ...

## Experiment Plan 2: Concepts in pre-train set not necessarily intercepting with concepts in test set
Essentially the same set of experiments as in `Experiment Plan 1` but step 2 changes to adding some `k'` new concepts to the current pre-training data set that not deliberately sampled from the set of concepts in the test sets.
Therefore, we are adding new random concepts to the pre-training mixture.

1. Fix an eval synthetic GINC data set with 10K concepts (~0.024 diversity coeff. with probe network),
denote it as `C_{test, 10k, ginc}` and generate a data set `D_eval = D_{test, 10k, ginc}` with `n = 500?` examples. 
2. Sample `k'` new concepts (not necessarily from `C_{test, 10k, ginc}`) to generate a new pre-training data set `D_{tr, k+k', ginc}` using concepts `C_{tr, k+k', ginc}`.
3. Compute the diversity of the data set of the previous step and denote it as `div_k = div(D_{tr, k, ginc})`.
4. Pre-train a sufficiently large (e.g., deep) transformer model
5. Now start plotting 
   6. A (Ess): `x-axis = div_k vs y-axis = performance_i(D_eval)` (tests main hypothesis/essential goal)
   7. B (Ess): `x-axis = align(D_k, D_eval) vs y-axis = performance_i(D_eval)` (sanity check, tests `if as the alignment in pre-train & test set increases ==> increase in performance`)
   8. C (Ess): `x-axis = div_k  vs align(D_k, D_eval)` (sanity check, `if the diversity increases then ==> increases probability of covering test sets which ultimately ==> increases alignment`)
   9. (D (extra): `x-axis = delta in alginment(D_k', D_eval) vs performance_i(D_eval)` (hypothesis, does the most aligned data added cause the most increase in performance?))
   10. (E (extra): `x-axis = div vs ground truth div` (sanity check div correlates with ground truth div))

Comments:
- note: as we include new data `k'`, we can compute the distance from the test set and see if the more aligned the pre-trained data we train on (add) if that predicts/causes the most increase in performance.
  - note: I wonder if we can compute how far the pre-train and test/eval sets are using (normalized?) MSE/NED of MHMMs ground truth params or hellinger distance
    - we could even provide more data for `div vs ground truth div` ! (we don't even need ground truth to be normalized, we can for visualization purposes)

### Random thoughts
Risk:
- Risk: our eval sets are bad. Tim D. mentiond to me MMLU sucks. Let's ask him why he thinks that, document it and ask him/consider using something else (?). Note, if we only have to evaluate then perhaps it's not too expensive/hard to compute eval on MMLU? 

Comments:
- note: for the real data set, let's articulate which evaluation data sets we are using and why. I propose we use at least 2 from the hugging face eval board: ARC, MMLU.
- note: make sure we know what type of eval we are doing. TODO: ask Brando to share ref. on the subtleties on evaluating LLMs e.g., HELM, etc. let's try to summarize it.

---
## [Pyrtle93/alpha_fwb](https://github.com/Pyrtle93/alpha_fwb)@[833de4f21d...](https://github.com/Pyrtle93/alpha_fwb/commit/833de4f21d27d323b7a2ddbc015d6ac711be4002)
#### Saturday 2023-09-16 17:51:03 by Kuba Wojciechowski

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
Signed-off-by: RakeshBatra <raakesh.batra@rediffmail.com>

---
## [RengaN02/PsychonautStation](https://github.com/RengaN02/PsychonautStation)@[fb4587b336...](https://github.com/RengaN02/PsychonautStation/commit/fb4587b3368ebb55e0cc10f8c650abcc26afa5d4)
#### Saturday 2023-09-16 18:35:41 by san7890

Cursed Slot Machine Fixes (#77989)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

A lot of these were stuff I did in response to reviews but apparently
didn't test extremely thoroughly. My bad.

* The proc for checking if the machine is in use is split out into its
own thing for clarity, and for potential reuse.
* The signal is no longer fucked up so you can actually get more than
one curse out of the slot machine as intended.
* Admin heals (and admin heals only) can remove the status effect. This
is just in case someone fucks up a variable when running an event and
wants to quickly heal some people while they varedit it to actually be a
proper event.
* Some nice code stuff while I was there, we don't need to be
typecasting to human anymore so it's nice to fix that.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Fixes are good.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

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
fix: The Cursed Slot Machine should now actually give you more than one
pull.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[dd6f51d9b6...](https://github.com/Paxilmaniac/Skyrat-tg/commit/dd6f51d9b6b970ec16d1398fe12516c039385263)
#### Saturday 2023-09-16 19:57:10 by SkyratBot

[MIRROR] Supermatter Delamination Balance Changes (Real) [MDB IGNORE] (#23670)

* Supermatter Delamination Balance Changes (Real) (#77996)

## About The Pull Request

lord forgive me I fucked up the merge conflict

The supermatter delamination countdown timer (how long it takes to go
boom-boom after hitting 0 integrity) has been lowered from 30 seconds to
13 seconds.
Removing a sliver from the supermatter, the traitor objective, will
further lower that down to 3 seconds.
Changes the wording on the mood effects from the supermatter
delaminating slightly.
The crystal uses SPAN_COMMAND on its final countdown, which means it
talk bigger.

## Why It's Good For The Game

Currently I feel that the supermatter delamination countdown overstays
its welcome. Ideally it provides tension to get the hell out, or perhaps
to make a risky last second play to try and save the supermatter.
However right now its at 30 seconds, which gives no danger of staying in
engineering right up to integrity 0, and keeps the tension at a high
note for too long, almost to the point of awkwardness. 13 seconds is a
good balance between get-the-fuck-out while still giving some leeway for
engineers to escape and crewmembers to jump in lockers, and feels quick
enough to give that danger that the supermatter should provide.
Additionally, removing a sliver from the supermatter lowers the cooldown
to 3 seconds. Right now this is one of the harder tasks a traitor can be
tasked with, while giving relatively little payoff sabatoge-wise. To the
point where I have seen engineers just let the traitor do it, as the
debuff it gives to the supermatter is minor. Now it makes the
supermatter delaminate almost immediately after hitting 0 integrity,
which means it will likely catch some engineers in the blast if a
traitor did it stealthy. This also makes it more risky to try and fix a
delamination if the engineering/security team did not stop the sliver
from being removed. All meaning succeeding at this task should be more
rewarding and damaging.
Finally the mood descriptions for the mood effects you get when a
supermatter delaminates have been changed. Currently they are pretty
gamey, and represent what the player might be thinking more than their
character. Additionally they were not very descriptive of where they
came from, which could be confusing.

## Changelog

:cl: Seven
balance: The supermatter delamination countdown has been lowered from 30
to 13 seconds
balance: Removing a sliver from the supermatter further lowers that down
to 3 seconds
balance: The supermatter crystal uses bigger text on its final countdown
spellcheck: Some supermatter delamination related mood descriptions have
been edited to explain the mood effect better
/:cl:

---------

Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@ users.noreply.github.com>

* Supermatter Delamination Balance Changes (Real)

* Update scram.dm

---------

Co-authored-by: Lufferly <40921881+Lufferly@users.noreply.github.com>
Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@ users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [Aurelien30000/FastAsyncVoxelSniper](https://github.com/Aurelien30000/FastAsyncVoxelSniper)@[8de386b448...](https://github.com/Aurelien30000/FastAsyncVoxelSniper/commit/8de386b44842866527bd87e083bd2b8f5961b525)
#### Saturday 2023-09-16 20:22:25 by Aurélien

Cloud Command System Migration

# Introduction

**This is the first pass of the cloud command migration for FAVS.**
There will be a second one to restore old-fashioned command syntax, tracked as https://github.com/IntellectualSites/fastasyncvoxelsniper/issues/81.

_I have to highlight that this is my first experience with this, must-say wonderful, command system. I have spent a lot of time reading every available documentation and code piece. If @Citymonstret want to take a look and maybe give us tips to avoid "ugly" workarounds or handling, we would be glad!_

The whole pull request has been tested, not yet thoroughly, you can have a global overview, but it is not really ready.

If you have any question or remark, do not hesitate!

--

# General Command Management
I have opted to use the annotations extension of the cloud command system. In my opinion, this is better suited to the current brush format handling which is all done inside brush classes.

**Executors have been kept and brush & performer command are still handled inside their classes.**

- ``Snipe`` class has been extended for a usage as a commander, because FAVS relies on a lot on this class.
- ``CommandRegistry`` is the main place for the whole handling behind the scenes. Otherwise, commands are registered as usually done in cloud, with some specific annotations when needed.

**``SniperCommander`` class is the commander to use with cloud command system. If the player exists, it returns its sniper. Otherwise, it returns a simple ``SniperSender``, similar to ``CommandSender``.**

# Command Manager
FAVS uses the paper command manager, when available, to enjoy some improvements. Falls back to bukkit command manager otherwise.

- Async tab-completions are enabled if available.
- ``Snipe``, ``PerformerSnipe`` & ``Toolkit`` classes are registered into the injector in order to be injected in command methods.
- Command exceptions are adapted and customized with the FAVS message syntax.

# Command Post-Processor
FAVS requires the command post-processor ins order handle specific FAVS behavior.

- Handles the ``@RequireToolkit`` annotation, makes sure the toolkit is available and the value stored.
- Handles the ``@DynamicRange`` annotation, used to define a range from non-constant variables, using reflection.
- Prepares the brush & performer when needed, their ``Snipe`` and stores them.

# Annotations & Parser
FAVS uses some annotations to facilitate development, based on common rules and behaviors.

- Handles the ``@RequireToolkit`` annotation, modifies the command meta.
- Handles the custom command execution method handler, which should differ for brush & performer. Cloud commands are designed to live in a class instance, this is not suitable to the current management of brush & performer. I have opted for a custom execution method which uses the brush & performer instance from the execution context instead of the base instance. _This avoid extra parameters for each command method._

# Arguments
FAVS needs a lot of custom arguments for either factories, registries, custom types, custom needs, etc.

**Suggestions & parsers are also declared via annotations in custom classes.**

# Other Changes
- All classes related to internal command managing from VS have been removed.
- ``FastAsyncVoxelSniper`` class has been removed. As far as I know, this class was useless and is now for sure.
- Some classes and methods have been added or refactored, but the overall codebase is the same to try keeping maximum compatibility.
- Some translations have been reorganized or removed.
- Some code format has been modified, there will be another pull request next year hopefully to unify comments format.
- Improvements to brush properties loading. Previously, all aliases were loaded, subsequently loading the same brush several times.
- Modern switch syntax has replaced old ones.
- General improvements.

# Known Problems:
- There is currently one small issue with static/literal arguments and their aliases. Tab-completions are not handled for all aliases due to https://github.com/Incendo/cloud/blob/master/cloud-core/src/main/java/cloud/commandframework/arguments/StaticArgument.java#L134.
- Brigadier extension is voluntarily not used due to some incompatibilities with FAVS commands syntax.

---
## [Towelstation13/towelstation13](https://github.com/Towelstation13/towelstation13)@[6c7af3b452...](https://github.com/Towelstation13/towelstation13/commit/6c7af3b45234a4109fe0835f3cb5b0ef743e6e4e)
#### Saturday 2023-09-16 20:25:33 by Alexis

Adds the Bluespace Compression kit (#29)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds the Bluespace Compression kit (BCK), a hacked BRPD that can be used
to make items smaller.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## How This Contributes To The Towelstation Roleplay Experience
Funny new traitor item that can be bought for 13 tc.
<!-- Please add a short description of why you think these changes would
benefit the game and the roleplay atmosphere of the server. If you can't
justify it in words, it might not be worth adding. -->

## Proof of Testing

<!-- Include any screenshots/videos/debugging steps of the code
functioning successfully, between the </summary> and </details> code
blocks. -->
<!-- To our mappers and spriters: Posting screenshots of content INSIDE
EDITORS (aseprite, PDN, SDMM, ect) is NOT valid proof of testing. Please
make sure that you COMPILE the game and provide PROOF you tested your
edits. -->

<details>
<summary>Screenshots/Videos</summary>
  

![image](https://github.com/Towelstation13/towelstation13/assets/20053168/ccd56d73-c894-460f-9a46-1702b011486c)

![image](https://github.com/Towelstation13/towelstation13/assets/20053168/bf1c5006-7e3d-403e-bc5d-7768b130d28c)

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
add: Added the bluespace compression kit, which you can use to shrink
items. Purchasable through uplinks for 13 tc.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>

---
## [Der-Floh/i-rule-translations](https://github.com/Der-Floh/i-rule-translations)@[2da56ed7da...](https://github.com/Der-Floh/i-rule-translations/commit/2da56ed7daa171bca85e2e16fb3ff70acd0acd4b)
#### Saturday 2023-09-16 20:43:23 by SlayerIbn

"Bucle" is pure shit and doesn't have the meaning that I want, "Ciclo" is fucking perfect

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[2a3b489eaf...](https://github.com/Zergspower/Skyrat-tg/commit/2a3b489eaf176cfd9c9b85cc87c42927b7aa26e6)
#### Saturday 2023-09-16 21:44:51 by SkyratBot

[MIRROR] Conveyor Belts are now easier to extend and have screentips [MDB IGNORE] (#23679)

* Conveyor Belts are now easier to extend and have screentips (#78278)

## About The Pull Request

Conveyor belt **stacks** now have a better examine text.

Using a conveyor belt stack on a placed conveyor belt now extends the
conveyor belt by 1 tile, linking to it's ID automatically, and makes for
much easier building of conveyor belt setups.

Conveyor belts now come jam packed with screentips.

I've also added the default tile place sound to the usage of conveyor
stacks to provide a tiny bit of audio feedback when placing new conveyor
belts.

## Why It's Good For The Game

Conveyor belts are just mind-numbingly annoying to use in a regular
round, and trying to set up a new conveyor belt setup is confusing if
you don't have ultra specific information about how to make one before
you even start. Hell, I remember I had to add the *real* construction
steps to the wiki like 6 years ago and I STILL hear people getting
confused about how these works.

This improves their ease of use, while also making everyone sleep a
little easier for those of us who use them.

## Changelog

:cl:
qol: Conveyor belts now have screentips and a better examine tip to
teach you how to set one up properly.
qol: Using a conveyor belt stack on a placed conveyor belt will extend
the conveyor belt to the output of that conveyor belt.. You can use this
to place fully integrated conveyor belts much easier now.
/:cl:

* Conveyor Belts are now easier to extend and have screentips

---------

Co-authored-by: ArcaneMusic <41715314+ArcaneMusic@users.noreply.github.com>

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[385ab7a166...](https://github.com/TheBoondock/tgstation/commit/385ab7a1667250947d480725949bec924ce4ac8a)
#### Saturday 2023-09-16 23:05:35 by Pickle-Coding

Changeling armblade gets 35% armour penetration + better wounding. (#77416)

## About The Pull Request
Gives the changeling armblade an armour penetration of 35%. Sets their
bare_wound_bonus to 10 (from 20), and a wound_bonus of 10 (from -20).
## Why It's Good For The Game
The wound bonuses basically gave massive punishment if they attacked
anything but the skin. It honestly felt kinda lame. The better wounding
potential will help bring a bloodier and more exciting atmosphere when a
changeling whips out the blade.

The armour penetration will help reduce dragged out fights that get a
little silly, while keeping the wounding more consistent.
## Changelog
:cl:
balance: Changeling arm blade has an armour penetration of 35%.
balance: Changeling arm blade has a wound bonus of 10, from -20.
balance: Changeling has a bare wound bonus of 10, from 20.
/:cl:

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[38235dce1d...](https://github.com/TheBoondock/tgstation/commit/38235dce1d1644be32d1758dcc18734a17e61b1d)
#### Saturday 2023-09-16 23:05:35 by carlarctg

Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

---
## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[3645fa7d89...](https://github.com/ArcaneDefence/tgstation/commit/3645fa7d8956bed2d3ebff86b072f8b9544d383d)
#### Saturday 2023-09-16 23:33:28 by distributivgesetz

Replaces slime clone damage with a "Covered in Slime" status effect (#77569)

## About The Pull Request

This PR replaces clone damage dealt by slimes with a new status effect,
"Covered in Slime".

The status effect is applied when you wrestle a slime off. The status
effect has a chance of not applying if your biohazard protection on your
head and chest is good enough.

It deals brute damage over time and gets removed when you stand under
the shower for about 10 seconds or when you are about to enter softcrit.

As a direct consequence of adding this feature I added showers to the
North Star and Birdshot Xenobiology Labs. I'm sorry, I'm sure you wanted
to make a statement with this, but we kind of require them in there now.

## Why It's Good For The Game

One source of clone damage eliminated whilst hopefully keeping a
"unique" interaction when dealing with slimes. No other source of clone
damage has been touched.

Clone damage is a damage type that shouldn't exist anymore, it's a relic
left from the era of cloning and it's so specific of a damage type that
it rarely gets used as a result. It really should be a type of
affliction (wound etc) instead of its own damage counter.

However, some things in the game still depend on clone damage being
around, so those needs to be addressed first.
We start off with slimes in this PR.

This status effect either lets you either continue with your work if you
react fast enough or it forces you to medbay, giving a victim more
control over the situation, as opposed to just being dealt a rare damage
type that always forces you to go to medbay if you want it healed.

## Changelog

:cl: distributivgesetz
add: Replaced slime clone damage with a "Covered in Slime" status effect
that deals brute damage over time and can be washed off by standing
under a shower.
add: Northstar and Birdshot Xenobiology have been outfitted with a new
shower.
code: Replaced the magic strings in slime code with macros. Also
included some warnings to anyone daring to touch the macros.
/:cl:

---

