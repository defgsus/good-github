## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-31](docs/good-messages/2023/2023-12-31.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,568,713 were push events containing 3,073,998 commit messages that amount to 126,745,196 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [M-D-Team/ait-fabric-1.20.1](https://github.com/M-D-Team/ait-fabric-1.20.1)@[baabc3b7ce...](https://github.com/M-D-Team/ait-fabric-1.20.1/commit/baabc3b7cebfc0e1882d636c777c9570220a2a62)
#### Sunday 2023-12-31 00:33:18 by Loqor

moved the registries to where they belong FUCK YOU CREATIVIOUS

---
## [YakumoChen/tgstation](https://github.com/YakumoChen/tgstation)@[71b45e54ad...](https://github.com/YakumoChen/tgstation/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Sunday 2023-12-31 00:44:06 by san7890

Puts all traits in the globalvars file + CI Testing (#79642)

## About The Pull Request

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-


![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit
## Why It's Good For The Game

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)
## Changelog

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[c00f7d53a3...](https://github.com/Pickle-Coding/tgstation/commit/c00f7d53a32801b7afd923f268da30fb2f99bbd5)
#### Sunday 2023-12-31 01:02:19 by MGOOOOOO

The Inversenning : Superior Healing Medications (#79342)

Introducing new inverse reagents for existing superior healing
medications! This push includes...

**Benzoic Acid** : Inverse of Salicylic Acid. Robust fertilizer that
provides a decent range of benefits for plant life.

**Oxymetholone** : Inverse of Oxandrolone. Anabolic steroid that
promotes the growth of muscle during and after exercise.

**Bamethan** : Inverse of Salbutamol. Blood thinner that drastically
increases the chance of receiving bleeding wounds.

**Pendetide** : Inverse of Pentetic Acid. An unusual bioradioactive drug
that purges basic radiation healing chems. Also increases the severity
of radiation poisoning.

**Hyoscyamine** : Inverse of Atropine. Heals heart and stomach damage,
and slowly removes minor toxin damage.

**Ammoniated Sludge** : Inverse of Ammoniated Mercury. A ghastly looking
mess of mercury by-product which causes bursts of manic hysteria.

**Inreziniver** : Inverse of Rezadone. Makes the user horribly afraid of
all things related to carps.

This is an effort to add more variety to the existing inverse reagent
system within chemistry. Not only should this variety serve to provide
additional options for a Chemist to experiment with, they should also
broaden the possibilities for already existing strategies.

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[b7b0932c4b...](https://github.com/IndieanaJones/tgstation/commit/b7b0932c4b5b3d4f9386b6dce514ee1ba3e25a05)
#### Sunday 2023-12-31 01:05:19 by distributivgesetz

Delamination variants are now locked in after the countdown is reached (#80324)

## About The Pull Request

Does what it says on the tin.
## Why It's Good For The Game

This effectively changes one and only one thing: 

The "All Within Theoretical Limits" achievement is easier/fairer to get
with this. Previously, if you edged a crystal with the gas composition
method to get a resonance cascade, you had to make sure that your gas
composition stayed until it left the explosion point, which made the
achievement extremely finnicky and unfun to get this way. Regular
delaminations won't really be affected, because yeah. It's at the
explosion point. What are you going to do about it?

This makes the achievement easier to cheese, but honestly, in my opinion
as person who added the achievement, meh. If people feel like this isn't
good for the achievement, say something in the comments.

Closes #79528

## Changelog
:cl:
balance: Delamination variants no longer change once the explosion point
has been reached.
/:cl:

---
## [kkpan11/comprehensive-rust](https://github.com/kkpan11/comprehensive-rust)@[c9f66fd425...](https://github.com/kkpan11/comprehensive-rust/commit/c9f66fd425ec7f6e5e80eb5622c6e40d85ceedd3)
#### Sunday 2023-12-31 01:13:57 by Martin Geisler

Format all Markdown files with `dprint` (#1157)

This is the result of running `dprint fmt` after removing `src/` from
the list of excluded directories.

This also reformats the Rust code: we might want to tweak this a bit in
the future since some of the changes removes the hand-formatting. Of
course, this formatting can be seen as a mis-feature, so maybe this is
good overall.

Thanks to mdbook-i18n-helpers 0.2, the POT file is nearly unchanged
after this, meaning that all existing translations remain valid! A few
messages were changed because of stray whitespace characters:

     msgid ""
     "Slices always borrow from another object. In this example, `a` has to remain "
    -"'alive' (in scope) for at least as long as our slice. "
    +"'alive' (in scope) for at least as long as our slice."
     msgstr ""

The formatting is enforced in CI and we will have to see how annoying
this is in practice for the many contributors. If it becomes annoying,
we should look into fixing dprint/check#11 so that `dprint` can annotate
the lines that need fixing directly, then I think we can consider more
strict formatting checks.

I added more customization to `rustfmt.toml`. This is to better emulate
the dense style used in the course:

- `max_width = 85` allows lines to take up the full width available in
our code blocks (when taking margins and the line numbers into account).
- `wrap_comments = true` ensures that we don't show very long comments
in the code examples. I edited some comments to shorten them and avoid
unnecessary line breaks — please trim other unnecessarily long comments
when you see them! Remember we're writing code for slides :smile:
- `use_small_heuristics = "Max"` allows for things like struct literals
and if-statements to take up the full line width configured above.

The formatting settings apply to all our Rust code right now — I think
we could improve this with https://github.com/dprint/dprint/issues/711
which lets us add per-directory `dprint` configuration files. However,
the `inherit: true` setting is not yet implemented (as far as I can
tell), so a nested configuration file will have to copy most or all of
the top-level file.

---
## [thegrb93/Bubberstation](https://github.com/thegrb93/Bubberstation)@[8f3d1036c8...](https://github.com/thegrb93/Bubberstation/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Sunday 2023-12-31 03:02:52 by SkyratBot

[MIRROR] Refactor icemoon wolves into basic mobs and add taming + pack behavior [MDB IGNORE] (#25126)

* Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Refactor icemoon wolves into basic mobs and add taming + pack behavior

---------

Co-authored-by: Ephemeralis <Ephemeralis@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [Omgise/Et-Futurum-Requiem](https://github.com/Omgise/Et-Futurum-Requiem)@[aef5968a71...](https://github.com/Omgise/Et-Futurum-Requiem/commit/aef5968a71be261fc3f72f2848a6c2ba5e8cab5a)
#### Sunday 2023-12-31 03:17:54 by Roadhog360

OK SMARTASS INTERPRETER JUST HAVE IT ALL
OH THIS IS MISSING OH THAT IS MISSING WHO FUCKING CARES JUST COMPILE IT ANYWAYS AND IGNORE THE ONE GODDAMN MISSING FUNCTION UNTIL I COMMIT THE CODE
People be like "oh just use branches" "just commit a bit at a time" I TRY THAT AND THIS SHIT IS WHAT FUCKING HAPPENS
build failed build fauileldd sdfbsfogdiuhaeraipiz[p
It just leads to build failures
So when people tell me to use branches to confuse my code or make more """""organized""""" commits I link them to this message. Yes I'm tilted
Let's see Gradle fail this one too because it likes to be an asshole

- Add soul fire gen through WorldGenSoulFire and apply it to NetherChunkProvider, so soul fire appears on soul soil when enabled
- Due to failures with forge's custom item entity system, it has been removed and replaced with a mixin. Bugs include custom item-entities jittering when first spawned in and /give not dispensing the item into the player's inventory. It's clear the custom item entity system was NOT thoroughly tested by Forge. Old uninflammable items that exist in the world will be converted to the regular item entities automatically.
  - A system to add/remove items via the config or mod code will be added in the future, as well as adjusting their buoyancy
 - Add a biome list helper function to Utils.java, to make it easier to create biome lists with certain blacklists

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[bce2a4a224...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/bce2a4a224b65f8093999d598f1b80f59ba3d03d)
#### Sunday 2023-12-31 03:54:27 by jimmyl

69 new vox phrases (#80577)

# attempt 2 of #80569 (no rizz, gyatt, or mothblocks this time)
# created via https://github.com/AlexMorgan3817/ss13-vox

## About The Pull Request

69 or so roughly new phrases
words of note: felinid, jolly, christmas, lightbulb, present, presents,
lizard, lizardperson, never, thanks, while, was, okay, had, her, some
numbers, ever
wordlist used (duplicates inside:)

[common.txt](https://github.com/tgstation/tgstation/files/13765603/common.txt)



https://github.com/tgstation/tgstation/assets/70376633/adaa1607-8c18-4fed-a6e8-1b7ac0db3303





https://github.com/tgstation/tgstation/assets/70376633/ffbd1b1d-6b2c-4921-ae77-45ea4056348f



## Why It's Good For The Game

vox shenanigans

## technobabble
anyway so getting the shitty project running took me 80 hours or so over
many attempts but
the linked fork has less of that poetry python bullshit
just dont install python3.6 its pointless, install python3
anyway so run sudo python3 setup.py
follow instructions till it actually works
generate.sh will not work well so just run "sudo python3 create.py"
directly
also you could just skip the sudo part by just running sudo -i before
all that
create.py will create both voices for vox_masc and vox_fem for some
reason but you could avoid that by removing masc or whatever the fuck
the sex is called from create.py to save some time by doing fem solely
also you should set codebase to tg in codebase.yaml and replace
tglist.jinja2 in templates with this
```
GLOBAL_LIST_INIT(vox_sounds, list(
  {%- for sex, phrases in SEXES.items() %}
    {%- for phrase in phrases %}
"{{- phrase.id -}}" = 'sound/vox_fem/{{- phrase.id -}}.ogg',
    {%- endfor %}
  {%- endfor %}
))
```
which should create roughly correct code for tg but you still need to do
some text work
like removing duplicates n stuff and moving sounds from dist/sounds to
the actual proper sound folder

anyway thank you for coming to my rant

## Changelog
:cl:
add: 69(roughly?) new vox phrases
/:cl:

---
## [AnonWasTaken/sixflags](https://github.com/AnonWasTaken/sixflags)@[34170c1dec...](https://github.com/AnonWasTaken/sixflags/commit/34170c1dece6c36bf6804df8338470f998a44f9e)
#### Sunday 2023-12-31 04:21:28 by AnonWasTaken

All Star

Somebody once told me
The world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb
With her finger and her thumb
In the shape of an L on her forehead

Well, the years start coming
And they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart
But your head gets dumb

So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go
You'll never shine if you don't glow

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold

It's a cool place and they say it gets colder
You're bundled up now
But wait till you get older
But the meteor men beg to differ
Judging by the hole in the satellite picture

The ice we skate is getting pretty thin
The water is getting warm
So you might as well swim
My world's on fire, how about yours?
That's the way I like it
And I never get bored

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
And all that glitters is gold
Only shooting stars

Somebody once asked
Could I spare some change for gas?
I need to get myself away from this place
I said: Yep, what a concept
I could use a little fuel myself
And we could all use a little change

Well the years start coming
And they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart
But your head gets dumb

So much to do, so much to see
So what's wrong with taking the back streets
You'll never know if you don't go (go!)
You'll never shine if you don't glow

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid

And all that glitters is gold
Only shooting stars break the mold
And all that glitters is gold
Only shooting stars break the mold

---
## [bunnymatic/bryantstreetstudios](https://github.com/bunnymatic/bryantstreetstudios)@[cc61dc4fc9...](https://github.com/bunnymatic/bryantstreetstudios/commit/cc61dc4fc9631aef16e116130499478ef5ad8b41)
#### Sunday 2023-12-31 04:57:17 by Jon Rogers

Add selenium so we can do full JS browser testing

problem
--------

Running full e2e tests now that we're doing more react is important.  We
need our browser to have JS support.  But the current Capybara setup
just uses the `rack_test` driver which does not have JS support.

solution
--------

This PR introduces selenium and webdrivers gems and sets up capybara so
that we can tag certain tests with `type: :e2e` and they will run
selenium and a browser.  It also includes support for headed or headless
chrome for testing.  By default it's headed for development so we'll see
the tests run.  If this turns out to be too annoying we can switch it
later.

changes
------

* add e2e spec around editable content for events/cms entries
* split css and js entries
* move from `thin` to `puma`
* add tests controller and sample data create/delete endpoints
* revamp admin js and application js so that they were correct for our
  test runner
* reinstate content block edits and fix that so it works.

notes
------

I spent a lot of time trying to get the database transaction issue
figured out with no luck.  The basic issue is that in the rspec example
or it block, if you use factory bot to create database entries, that
data is in a transaction which is separate from the db connection that
the app is using which means the application does *not* see that
creation.  Rspec-Rails and some other rails stuff has tooling to get
around this but I was unable to figure out how to leverage that here or
mimic it.

Because of this, I added a tests_controllers.rb file and a
`tests/sample_data` endpoint that *only* works if you're in test mode
(for safety).

When we write e2e tests we should populate this sample data such that it
is a valid start up scenario for *all* e2e tests.  We can think of it as
a set of seed data for a test instance of the application.  Currently,
we're going to start with 1 active event and 2 cms entries for the two
pages that show custom cms content.  I could imagine a default
"exclusion" item... in the future.

It's not great but it's better than not having full feature e2e tests.

Exercise for the author and reader
-------------------

I don't understand `@use` vs `@import` in SCSS and I feel like I should.

---
## [maxwaldman8/Deceptive-Perspectives](https://github.com/maxwaldman8/Deceptive-Perspectives)@[aa5801cb95...](https://github.com/maxwaldman8/Deceptive-Perspectives/commit/aa5801cb95e480f9410ba9ae6abb8bc652908ebf)
#### Sunday 2023-12-31 05:20:39 by maxwaldman8

A lot of changes

Organization, implemented the Y, and improved the movement controller.

BUGS/MISSING FEATURES SO FAR THAT I HAVE FOUND: Keyhole animation breaks when you press play (maybe we can make it so you can't press play when the keyhole animation is running), movement controller is still pretty bad, hole item on canvas goes out of frame, no Y item texture (using brick as placeholder), no play button without Y texture, no Y texture to go on top of that texture (using brick as placeholder) (note: I have a solution for the no y on door texture), and maybe we could make the parts of the play button falling a little more random with animation which also would make the hole not go offscreen (and they also fall differently if you pause while they are falling).

Also Adrian had an idea of "skeletons in the closet" for like a bedroom or something with a closet but one of the bones of the skeleton is a "skeleton key" which opens a door (but it gets used up). I also thought that maybe we could do hint messages appearing if you spend a while on a puzzle (that can be turned on and are off by default or maybe the opposite of that). For example:

A while on pause puzzle: "Think outside of the box"
Even longer on pause puzzle (it will have already told you the controls earlier: "Remember: Esc to pause"
Even longer on pause puzzle: "Esc to go outside of the box"
Way too long on pause puzzle (for other ones would also just give the solution): "Go into the pause menu and try to move around after a second to complete the puzzle"

I think either that or just a hint section of the menu would be good.

Also Adrian played through it and said that the Y puzzle was really hard because of all of the different symbols in the logo so we should definitely add hints for that.

Sorry this is so long but one last thing I think there could be like a piece of paper somewhere with a code that you dial into the phone and press the # then the screen turns on and it shows an easter egg.

---
## [beartype/beartype](https://github.com/beartype/beartype)@[6a191af44a...](https://github.com/beartype/beartype/commit/6a191af44aa549878afd14fccf994e9c16d3fdc8)
#### Sunday 2023-12-31 06:15:03 by leycec

PEP 695 `type` aliases x 9.

This commit is the next in a commit chain adding support for PEP
695-compliant type aliases (i.e., type hints instantiated by statements
of the form ``type {alias_name} = {alias_value}``, available under
Python ≥ 3.12), en-route to resolving feature request #297 kindly
submitted by the magical rainbow GitHub unicorn @EtaoinWu (Yue Wu).
Specifically, this commit continues brutally applying a hardcore AST
transformation just to force PEP 695 to comply with our will. Will you
just stop sucking it already, PEP 695? PEP 695 as if written by Terry
Pratchett:

> "I didn do nuffin."

(*Bland blemish on a Flemish flamingo!*)

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[25be46a37d...](https://github.com/ReturnToZender/ReturnsBubber/commit/25be46a37dfd73308619ad393479bb06cc233ced)
#### Sunday 2023-12-31 06:20:28 by aKromatopzia

fixes for teshvali cybernetics (#900)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

# OOPS
So in the previous and now closed PR
(https://github.com/Bubberstation/Bubberstation/pull/871#issue-2049760879)
I forgot to commit changes to tgstation.dme. So while the files are now
in the code... they're not enabled. Oops.

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

I didn't notice some more minor changes in the testmerge. This rectifies
some of that - new vars, and such. After I fix the new bugs inherent to
this... Which have now been fixed. ~~Although the current version should
still be functional, teshari cybernetic limbs take approximately 10%
more damage than they should due to the missing var. I think. The var is
weird, and honestly seems to be a redundancy? better safe than sorry.~~
This PR actually enables the previous PR and fixes some things which
would have caused minor statistical inconsistencies on the scale of
+-1-5 damage taken.
### Advanced Raptor limbs
Oh, also advanced cybernetic limbs were implemented since the downstream
made them obtainable. They're a bit brighter than the regular limbs.

![Screenshot_57](https://github.com/Bubberstation/Bubberstation/assets/94389683/9421bc98-1944-4bfe-b707-817123ab8ce1)
![Screenshot_56](https://github.com/Bubberstation/Bubberstation/assets/94389683/870b334a-ce7f-4708-ad97-e0a9d1972b42)
![Screenshot_58](https://github.com/Bubberstation/Bubberstation/assets/94389683/b681ebea-2272-4f38-87ea-adcd75a6aed7)



<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

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
fix: ACTUALLY enables teshvali cybernetics
add: advanced raptoral cybernetics
fix: some vars that were added in the downstream are now correctly
implemented.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---------

Co-authored-by: Waterpig <49160555+Majkl-J@users.noreply.github.com>
Co-authored-by: projectkepler-RU <99981766+projectkepler-ru@users.noreply.github.com>

---
## [user-why-red/san_kernel_xiaomi_sdm660_419](https://github.com/user-why-red/san_kernel_xiaomi_sdm660_419)@[cfbef24cde...](https://github.com/user-why-red/san_kernel_xiaomi_sdm660_419/commit/cfbef24cde597a129006e19e74792837fac4f387)
#### Sunday 2023-12-31 06:24:57 by Peter Zijlstra

UPSTREAM: sched/core: Fix ttwu() race

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: Santhosh <san8754513543@gmail.com>

---
## [SpessManCN/BrainTrauma-1995](https://github.com/SpessManCN/BrainTrauma-1995)@[1a2ab1b13c...](https://github.com/SpessManCN/BrainTrauma-1995/commit/1a2ab1b13c2da4eee7c39df31695926b13048063)
#### Sunday 2023-12-31 06:49:28 by SkyratBot

[MIRROR] Touches up Moffuchi's pizzeria  [MDB IGNORE] (#25246)

* Touches up Moffuchi's pizzeria  (#79899)

## About The Pull Request
I've given the icebox pizzeria ruin a few small improvements:
- Firstly, The kitchen is actually stocked with tomatoes from the get
go. Along with a few mothic themed ingredients for those signature
mothic pizzas we all know and love (And hate for being such a pain to
make)
- The discarded air alarm frames have been replaced with working ones
(I'm unsure if this was intentional or not)
- Some drinking glasses have been added to the bar
- And finally a pacman has been placed in the backroom along with some
plasma to power the place
## Why It's Good For The Game
This place gets overlooked a lot because its completely powerless, and
doesn't actually give you enough from the get go to make even a basic
pizza besides the tomato seeds a lot of people are gonna miss. This
gives the ruin just a little more life to maybe be worth trekking out
for. And having mothic themed ingredients in the **MOFFIC** Pizzeria
just makes sense even if they are a bitch to make.

Not sure if this counts as a balance change or a QOL so feel free to
yell at me if I've labelled this wrong, I have been advised that this
SHOULD be the latter at least.
## Changelog
:cl:
qol: Mothuchi's pizzeria has been improved slightly! Order yourself a
fresh mothic pizza today!
/:cl:

* Touches up Moffuchi's pizzeria

---------

Co-authored-by: DaydreamIQ <62606051+DaydreamIQ@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [a3-Prjkt/kernel_xiaomi_sm8250](https://github.com/a3-Prjkt/kernel_xiaomi_sm8250)@[eb32c22f37...](https://github.com/a3-Prjkt/kernel_xiaomi_sm8250/commit/eb32c22f377767a83f13b09ba2c3c4919593b20c)
#### Sunday 2023-12-31 07:34:08 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

---
## [checkraisefold/Foundation-19](https://github.com/checkraisefold/Foundation-19)@[f717155e32...](https://github.com/checkraisefold/Foundation-19/commit/f717155e32508fd2f2ef5e781b93f0996391fa0e)
#### Sunday 2023-12-31 08:18:50 by cheesePizza2

Removes old control room + mapping improvements (#1407)

* mapping is fun!

* fuck you

* there is a ghost in my computer that is reverting my changes before i can commit them

* fixes

* fuckyou

* trigger Github actions

---
## [emiya27/Stellaris_kernel_sony_tama](https://github.com/emiya27/Stellaris_kernel_sony_tama)@[671b308a50...](https://github.com/emiya27/Stellaris_kernel_sony_tama/commit/671b308a5065975588405fe6bf52eb08aacd3636)
#### Sunday 2023-12-31 09:21:12 by Greg Kroah-Hartman

Merge 4.9.233 into android-4.9-q

Changes in 4.9.233
	xfs: catch inode allocation state mismatch corruption
	xfs: validate cached inodes are free when allocated
	xfs: don't call xfs_da_shrink_inode with NULL bp
	net: phy: mdio-bcm-unimac: fix potential NULL dereference in unimac_mdio_probe()
	crypto: ccp - Release all allocated memory if sha type is invalid
	media: rc: prevent memory leak in cx23888_ir_probe
	ath9k_htc: release allocated buffer if timed out
	ath9k: release allocated buffer if timed out
	PCI/ASPM: Disable ASPM on ASMedia ASM1083/1085 PCIe-to-PCI bridge
	ARM: 8986/1: hw_breakpoint: Don't invoke overflow handler on uaccess watchpoints
	drm/amdgpu: Prevent kernel-infoleak in amdgpu_info_ioctl()
	drm: hold gem reference until object is no longer accessed
	f2fs: check memory boundary by insane namelen
	f2fs: check if file namelen exceeds max value
	9p/trans_fd: abort p9_read_work if req status changed
	9p/trans_fd: Fix concurrency del of req_list in p9_fd_cancelled/p9_read_work
	x86/build/lto: Fix truncated .bss with -fdata-sections
	x86, vmlinux.lds: Page-align end of ..page_aligned sections
	fbdev: Detect integer underflow at "struct fbcon_ops"->clear_margins.
	rds: Prevent kernel-infoleak in rds_notify_queue_get()
	xfs: fix missed wakeup on l_flush_wait
	uapi: includes linux/types.h before exporting files
	install several missing uapi headers
	net/x25: Fix x25_neigh refcnt leak when x25 disconnect
	net/x25: Fix null-ptr-deref in x25_disconnect
	sh: Fix validation of system call number
	net: lan78xx: add missing endpoint sanity check
	net: lan78xx: fix transfer-buffer memory leak
	mlx4: disable device on shutdown
	mlxsw: core: Increase scope of RCU read-side critical section
	mlxsw: core: Free EMAD transactions using kfree_rcu()
	ibmvnic: Fix IRQ mapping disposal in error path
	mac80211: mesh: Free ie data when leaving mesh
	mac80211: mesh: Free pending skb when destroying a mpath
	arm64: csum: Fix handling of bad packets
	usb: hso: Fix debug compile warning on sparc32
	qed: Disable "MFW indication via attention" SPAM every 5 minutes
	nfc: s3fwrn5: add missing release on skb in s3fwrn5_recv_frame
	parisc: add support for cmpxchg on u8 pointers
	net: ethernet: ravb: exit if re-initialization fails in tx timeout
	Revert "i2c: cadence: Fix the hold bit setting"
	xen-netfront: fix potential deadlock in xennet_remove()
	KVM: LAPIC: Prevent setting the tscdeadline timer if the lapic is hw disabled
	x86/i8259: Use printk_deferred() to prevent deadlock
	random32: update the net random state on interrupt and activity
	ARM: percpu.h: fix build error
	random: fix circular include dependency on arm64 after addition of percpu.h
	random32: remove net_rand_state from the latent entropy gcc plugin
	random32: move the pseudo-random 32-bit definitions to prandom.h
	ext4: fix direct I/O read error
	USB: serial: qcserial: add EM7305 QDL product ID
	net/mlx5e: Don't support phys switch id if not in switchdev mode
	ALSA: seq: oss: Serialize ioctls
	Bluetooth: Fix slab-out-of-bounds read in hci_extended_inquiry_result_evt()
	Bluetooth: Prevent out-of-bounds read in hci_inquiry_result_evt()
	Bluetooth: Prevent out-of-bounds read in hci_inquiry_result_with_rssi_evt()
	omapfb: dss: Fix max fclk divider for omap36xx
	vgacon: Fix for missing check in scrollback handling
	mtd: properly check all write ioctls for permissions
	leds: wm831x-status: fix use-after-free on unbind
	leds: da903x: fix use-after-free on unbind
	leds: lm3533: fix use-after-free on unbind
	leds: 88pm860x: fix use-after-free on unbind
	net/9p: validate fds in p9_fd_open
	drm/nouveau/fbcon: fix module unload when fbcon init has failed for some reason
	cfg80211: check vendor command doit pointer before use
	igb: reinit_locked() should be called with rtnl_lock
	atm: fix atm_dev refcnt leaks in atmtcp_remove_persistent
	tools lib traceevent: Fix memory leak in process_dynamic_array_len
	xattr: break delegations in {set,remove}xattr
	binder: Prevent context manager from incrementing ref 0
	ipv4: Silence suspicious RCU usage warning
	ipv6: fix memory leaks on IPV6_ADDRFORM path
	vxlan: Ensure FDB dump is performed under RCU
	net: lan78xx: replace bogus endpoint lookup
	Revert "vxlan: fix tos value before xmit"
	usb: hso: check for return value in hso_serial_common_create()
	Smack: fix use-after-free in smk_write_relabel_self()
	tracepoint: Mark __tracepoint_string's __used
	gpio: fix oops resulting from calling of_get_named_gpio(NULL, ...)
	cgroup: add missing skcd->no_refcnt check in cgroup_sk_clone()
	EDAC: Fix reference count leaks
	arm64: dts: qcom: msm8916: Replace invalid bias-pull-none property
	arm64: dts: exynos: Fix silent hang after boot on Espresso
	m68k: mac: Don't send IOP message until channel is idle
	m68k: mac: Fix IOP status/control register writes
	platform/x86: intel-hid: Fix return value check in check_acpi_dev()
	platform/x86: intel-vbtn: Fix return value check in check_acpi_dev()
	ARM: at91: pm: add missing put_device() call in at91_pm_sram_init()
	ARM: socfpga: PM: add missing put_device() call in socfpga_setup_ocram_self_refresh()
	drm/tilcdc: fix leak & null ref in panel_connector_get_modes
	Bluetooth: add a mutex lock to avoid UAF in do_enale_set
	fs/btrfs: Add cond_resched() for try_release_extent_mapping() stalls
	drm/radeon: Fix reference count leaks caused by pm_runtime_get_sync
	video: fbdev: neofb: fix memory leak in neo_scan_monitor()
	md-cluster: fix wild pointer of unlock_all_bitmaps()
	drm/nouveau: fix multiple instances of reference count leaks
	drm/debugfs: fix plain echo to connector "force" attribute
	mm/mmap.c: Add cond_resched() for exit_mmap() CPU stalls
	brcmfmac: To fix Bss Info flag definition Bug
	iwlegacy: Check the return value of pcie_capability_read_*()
	usb: gadget: net2280: fix memory leak on probe error handling paths
	bdc: Fix bug causing crash after multiple disconnects
	dyndbg: fix a BUG_ON in ddebug_describe_flags
	bcache: fix super block seq numbers comparision in register_cache_set()
	ACPICA: Do not increment operation_region reference counts for field units
	agp/intel: Fix a memory leak on module initialisation failure
	video: fbdev: sm712fb: fix an issue about iounmap for a wrong address
	console: newport_con: fix an issue about leak related system resources
	video: pxafb: Fix the function used to balance a 'dma_alloc_coherent()' call
	iio: improve IIO_CONCENTRATION channel type description
	leds: lm355x: avoid enum conversion warning
	media: omap3isp: Add missed v4l2_ctrl_handler_free() for preview_init_entities()
	scsi: cumana_2: Fix different dev_id between request_irq() and free_irq()
	drm/mipi: use dcs write for mipi_dsi_dcs_set_tear_scanline
	cxl: Fix kobject memleak
	drm/radeon: fix array out-of-bounds read and write issues
	scsi: powertec: Fix different dev_id between request_irq() and free_irq()
	scsi: eesox: Fix different dev_id between request_irq() and free_irq()
	media: firewire: Using uninitialized values in node_probe()
	media: exynos4-is: Add missed check for pinctrl_lookup_state()
	xfs: fix reflink quota reservation accounting error
	PCI: Fix pci_cfg_wait queue locking problem
	leds: core: Flush scheduled work for system suspend
	drm: panel: simple: Fix bpc for LG LB070WV8 panel
	scsi: scsi_debug: Add check for sdebug_max_queue during module init
	mwifiex: Prevent memory corruption handling keys
	powerpc/vdso: Fix vdso cpu truncation
	staging: rtl8192u: fix a dubious looking mask before a shift
	PCI/ASPM: Add missing newline in sysfs 'policy'
	drm/imx: tve: fix regulator_disable error path
	USB: serial: iuu_phoenix: fix led-activity helpers
	usb: dwc2: Fix error path in gadget registration
	scsi: mesh: Fix panic after host or bus reset
	Smack: fix another vsscanf out of bounds
	Smack: prevent underflow in smk_set_cipso()
	power: supply: check if calc_soc succeeded in pm860x_init_battery
	selftests/powerpc: Fix CPU affinity for child process
	selftests/powerpc: Fix online CPU selection
	s390/qeth: don't process empty bridge port events
	wl1251: fix always return 0 error
	net: spider_net: Fix the size used in a 'dma_free_coherent()' call
	fsl/fman: use 32-bit unsigned integer
	fsl/fman: fix dereference null return value
	fsl/fman: fix unreachable code
	fsl/fman: check dereferencing null pointer
	fsl/fman: fix eth hash table allocation
	dlm: Fix kobject memleak
	pinctrl-single: fix pcs_parse_pinconf() return value
	drivers/net/wan/lapbether: Added needed_headroom and a skb->len check
	net/nfc/rawsock.c: add CAP_NET_RAW check.
	net: Set fput_needed iff FDPUT_FPUT is set
	USB: serial: cp210x: re-enable auto-RTS on open
	USB: serial: cp210x: enable usb generic throttle/unthrottle
	ALSA: usb-audio: Creative USB X-Fi Pro SB1095 volume knob support
	ALSA: usb-audio: fix overeager device match for MacroSilicon MS2109
	ALSA: usb-audio: add quirk for Pioneer DDJ-RB
	crypto: qat - fix double free in qat_uclo_create_batch_init_list
	crypto: ccp - Fix use of merged scatterlists
	fs/minix: check return value of sb_getblk()
	fs/minix: don't allow getting deleted inodes
	fs/minix: reject too-large maximum file size
	ALSA: usb-audio: work around streaming quirk for MacroSilicon MS2109
	9p: Fix memory leak in v9fs_mount
	parisc: mask out enable and reserved bits from sba imask
	ARM: 8992/1: Fix unwind_frame for clang-built kernels
	xen/balloon: fix accounting in alloc_xenballooned_pages error path
	xen/balloon: make the balloon wait interruptible
	smb3: warn on confusing error scenario with sec=krb5
	PCI: hotplug: ACPI: Fix context refcounting in acpiphp_grab_context()
	btrfs: don't allocate anonymous block device for user invisible roots
	btrfs: only search for left_info if there is no right_info in try_merge_free_space
	btrfs: fix memory leaks after failure to lookup checksums during inode logging
	iio: dac: ad5592r: fix unbalanced mutex unlocks in ad5592r_read_raw()
	xtensa: fix xtensa_pmu_setup prototype
	powerpc: Fix circular dependency between percpu.h and mmu.h
	net: ethernet: stmmac: Disable hardware multicast filter
	net: stmmac: dwmac1000: provide multicast filter fallback
	net/compat: Add missing sock updates for SCM_RIGHTS
	md/raid5: Fix Force reconstruct-write io stuck in degraded raid5
	bcache: allocate meta data pages as compound pages
	mac80211: fix misplaced while instead of if
	MIPS: CPU#0 is not hotpluggable
	ext2: fix missing percpu_counter_inc
	ocfs2: change slot number type s16 to u16
	ftrace: Setup correct FTRACE_FL_REGS flags for module
	kprobes: Fix NULL pointer dereference at kprobe_ftrace_handler
	watchdog: f71808e_wdt: indicate WDIOF_CARDRESET support in watchdog_info.options
	watchdog: f71808e_wdt: remove use of wrong watchdog_info option
	watchdog: f71808e_wdt: clear watchdog timeout occurred flag
	pseries: Fix 64 bit logical memory block panic
	mfd: arizona: Ensure 32k clock is put on driver unbind and error
	USB: serial: ftdi_sio: make process-packet buffer unsigned
	USB: serial: ftdi_sio: clean up receive processing
	gpu: ipu-v3: image-convert: Combine rotate/no-rotate irq handlers
	iommu/omap: Check for failure of a call to omap_iommu_dump_ctx
	iommu/vt-d: Enforce PASID devTLB field mask
	i2c: rcar: slave: only send STOP event when we have been addressed
	clk: clk-atlas6: fix return value check in atlas6_clk_init()
	pwm: bcm-iproc: handle clk_get_rate() return
	Input: sentelic - fix error return when fsp_reg_write fails
	drm/vmwgfx: Fix two list_for_each loop exit tests
	net: qcom/emac: add missed clk_disable_unprepare in error path of emac_clks_phase1_init
	nfs: Fix getxattr kernel panic and memory overflow
	fs/ufs: avoid potential u32 multiplication overflow
	mfd: dln2: Run event handler loop under spinlock
	ALSA: echoaudio: Fix potential Oops in snd_echo_resume()
	sh: landisk: Add missing initialization of sh_io_port_base
	khugepaged: retract_page_tables() remember to test exit
	mm: Avoid calling build_all_zonelists_init under hotplug context
	Linux 4.9.233

Signed-off-by: Greg Kroah-Hartman <gregkh@google.com>
Change-Id: Ied62cb0768f5bd8e989d75e7c2ccf6f1e6f2efd4

---
## [Maybe-Anton/Shiptest](https://github.com/Maybe-Anton/Shiptest)@[d1339da7b3...](https://github.com/Maybe-Anton/Shiptest/commit/d1339da7b3fe7a9303cbdc93e2d836ec82460a26)
#### Sunday 2023-12-31 10:24:58 by zevo

Nerfs legion core implanting to not be an aheal (#2590)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
The legion core implant now gives you a potent heal of all four damage
types (-100 brute -100 burn -50 tox -50 oxy) instead of a literal aheal.
It now also deals 10 clone damage as a drawback to organics/FBPS (IPCS
excluded because they cant use clone damage medicine).
Due to how adjustBruteLoss and adjustBurnLoss work, the implanted core
no longer heals mechanical bodyparts, making it mostly useless for IPCs
and FBPs only healing oxygen and toxin damage.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
1. Player accessible aheals are not good and encourage exploiting to
cure ailments or gain an advantage.
2. Synthetics could use self-surgery to implant legion cores on the go
for a safety net heal. While not necessarily bad, it was insanely
powerful as an aheal and negated the requirement of stabilizing the core
and getting another person to put it in you.
3. It had literally no drawbacks. A strong consumable healing ability is
cool, but it should come with a cost.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: legion core implanting no longer aheals you on use
add: legion core implant now just does a potent organic heal with minor
clone damage when used
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: zevo <95449138+Zevotech@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [depoz0/G2station](https://github.com/depoz0/G2station)@[33e10634ba...](https://github.com/depoz0/G2station/commit/33e10634ba89c28c1ca3518068e916ec0a10b33e)
#### Sunday 2023-12-31 10:38:57 by Iamgoofball

Fixes Holy Water performing water metabolization twice, giving more blood and making you less drunk (#80440)

## About The Pull Request

~~Fixes Holy Water taking double the time it's supposed to take to
deconvert, and fixes it metabolizing out at twice the normal speed.~~

Fixes Holy Water performing water metabolization twice, giving more
blood and making you less drunk

## Why It's Good For The Game

lmfao ~~this is why deconversion for cult sucked~~ so bad

## Changelog

:cl:
fix: Fixes Holy Water giving you more blood and making you less drunk
than water normally does.
/:cl:

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[06d0f6cb6f...](https://github.com/NetBSD/pkgsrc/commit/06d0f6cb6f4ae12662875afbf52a5fc1b3be243d)
#### Sunday 2023-12-31 10:46:42 by adam

scummvm: updated to 2.8.0

ScummVM 2.8.0

New games

The team was quite busy working on new engines and enhancing existing ones. The list of supported games grew noticeably, and we now support these additions:

Adibou 1
Classical Cats
The Dark Eye
Dark Side
Escape From Hell
Gadget: Invention Travel and Adventure
Gobliiins 5
The Excavation of Hob's Barrow
Kingdom: The Far Reaches
Might and Magic Book One
Muppet Treasure Island
Nancy Drew: The Final Scene
Nancy Drew: Message in a Haunted Mansion
Nancy Drew: Secrets Can Kill
Nancy Drew: Stay Tuned for Danger
Nancy Drew: Treasure in the Royal Tower
Primordia
Reah: Face the Unknown
Schizm: Mysterious Journey
Shardlight
Strangeland
Syberia and Syberia II (macOS versions only)
Technobabylon
The Vampire Diaries
Whispers of a Machine
Wrath of the Gods and four other Director titles.
14 AGS titles by Stranga and Cloak and Dagger
All together, we’ve introduced 50 new games and five new engines.

New platforms

We are happy to see the RetroArch port being properly rewritten, and the port is now part of our source code. The Atari port has also been redone from scratch and now talks natively to the hardware, skipping SDL as an intermediate layer. That made many more games playable on the platform. The Atari FireBee port is still using the SDL library, though.

Speed-optimized graphics

Thanks to the work of one of the GSoC participants this year, Wyatt Radkiewicz (a.k.a. eklipsed), we now use CPU-specific SIMD instructions such as SSE, AVX2, and NEON for drawing graphics in the AGS engine and in some generic routines. This led to 4-14x speedup in drawing for many cases.

Networking games

This year, we merged with the Backyard Sports Online project, which made it possible to play Backyard Football, Backyard Baseball 2001 and Backyard Football 2002 over the internet with other humans. Also, the Moonbase Commander support is in active playtesting mode, though not yet ready for prime time.

Notable engine enhancements

The AGS engine has been brought up to version 3.6.0.53 from upstream.

For many engines, we added support for numerous Chinese and Japanese game variants.

Believe it or not, we implemented a lot of native GUI dialogs for SCUMM games, bringing them closer to the original experience. We also rewrote the sound code for the SCUMM Humongous Entertainment games, making them flawless.

We performed a deep review of the Broken Sword 1 game engine, implementing some small, previously unnoticed things like scene transitions, in-game menu peculiarities, accurate fonts, idle animations, and more. Now, the game is absolutely faithful to the original.

---
## [MichielSaey/clickup-time-tracker](https://github.com/MichielSaey/clickup-time-tracker)@[2fcc0001c9...](https://github.com/MichielSaey/clickup-time-tracker/commit/2fcc0001c91f54eef8d2cd82302583e1cfb99437)
#### Sunday 2023-12-31 11:04:52 by Michiel Saey

This thing is what you show people to make the write functional code...

Maneged to pass the start and end dates to the statistics components, but had its own pandora's box abd came with the problem that I had to call the events function twice.

Thinking to pass the events data to statics comp, but that would mean having to calculate the statics in the "front", not that there really is a front, so maybe that isn't a problem.

 Just want to get this over with so i never have to touch electron again.

 "Why should this Electron be saved? Doesn't it seem profoundly sick? Diseased? Like PWA has to be better, purely by the virtue that this is awful."

---
## [FardinOhe/Event-Management](https://github.com/FardinOhe/Event-Management)@[27d078b4fc...](https://github.com/FardinOhe/Event-Management/commit/27d078b4fc91267bcc9dcae174404b5dd63a40b0)
#### Sunday 2023-12-31 11:20:32 by FardinOhe

Create Portfolio

"Welcome to our Portfolio, a curated collection of our finest work and a testament to our dedication to creativity, innovation, and excellence. As architects of memorable experiences, we take pride in showcasing a diverse array of projects that span across industries and embody our commitment to exceeding expectations.

Explore a tapestry of events, each woven with meticulous planning, thoughtful design, and flawless execution. From corporate galas that captivate audiences to intimate weddings that celebrate love in its purest form, our Portfolio is a testament to our versatility and ability to transform visions into reality.

Every entry in our Portfolio is a chapter in our story, narrating the unique challenges we've overcome, the partnerships we've forged, and the success stories we've written together with our clients. Immerse yourself in the visual and narrative journey of events that left lasting impressions, whether through immersive branding experiences, cutting-edge technology integration, or the seamless orchestration of complex logistical details.

Our commitment to excellence extends beyond aesthetics; it's about crafting experiences that resonate, inspire, and endure in the memories of attendees. As you navigate through our Portfolio, envision the possibilities for your next event, knowing that our team stands ready to bring your vision to life with the same passion, precision, and creativity that defines our body of work.

Join us on this visual odyssey, where each project is more than an event—it's a testament to our unwavering pursuit of perfection and our dedication to making every moment unforgettable. Welcome to a showcase of innovation, inspiration, and the artistry that defines our approach to event management."

---
## [Erol509/Bubberstation](https://github.com/Erol509/Bubberstation)@[2805c86c81...](https://github.com/Erol509/Bubberstation/commit/2805c86c811fde2450a054a25c7a665b77df47e5)
#### Sunday 2023-12-31 11:29:49 by Nerevar

[THE HALF-MODULAR PRINCE] Snalance (Snail Balance) and Snissues (Snail Issues) Adjustment (#25439)

* initial d

* holy shit i forgot

* i got so much cheese in my pocket, they thought I was a fucking calzone

* opp was sneak-dissing on the 'gram, turned his city into pompeii

* Just fixing some diffs (line breaks should match tg)

* Fixes these edit comments

---------

Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [an0rak-dev/Avatar](https://github.com/an0rak-dev/Avatar)@[d05206556c...](https://github.com/an0rak-dev/Avatar/commit/d05206556c93499eed865ca12892314ee66b1fae)
#### Sunday 2023-12-31 11:34:34 by Sylvain Nieuwlandt

Add Readme, License and CI.

It's not because I'm working alone on this that I should work as a
savage. I thought it will be fun to integrate the linting steps as
reviews from the github action bot (Yeah, I know it might not sound
fun but it is !).

Got a MetaQuest 3 for Christmas from my insanely crazy wife. Guess
that this project will take another slow down because I'll try to
create a commercial game with it.

Changelog: other

---
## [deltanedas/ss14-docs](https://github.com/deltanedas/ss14-docs)@[4feada28fb...](https://github.com/deltanedas/ss14-docs/commit/4feada28fbf0cdd543026992706dd770c4edfb35)
#### Sunday 2023-12-31 11:44:46 by Kevin Zheng

Add atmos roadmap (#78)

# Roadmap For Atmospherics

## Background

Most atmos players currently agree that atmos is not very fun to play,
for some of the following reasons:

1. There is little content to play after round-start setup. Part of the
problem is that things like distro and TEG are "set up and forget".

2. Atmos can't actually rectify atmos problems in a reasonable amount of
time. For example, if there actually is a plasma leak, scrubbers
typically work too slowly resulting in the plasma inevitably being lit
before it can be cleaned up.

3. Atmos techs don't play with the rest of the station, preferring to
isolate themselves to produce a funny green gas that is only
particularly useful for shuttle bombing. Mechanics like this violate the
[fundamental design
principles](en/general-development/feature-proposals/ss14-fundamental-design-principles.md).
While these mechanics shouldn't be removed per-se, more focus should be
given to mechanics that increase interactions with the station, like
making sure the air is breathable and well-heated.

## Proposal

Make atmos more fun to play by adding more challenges and processes
semi-inspired by real life.

**An atmos tech's primary job is to keep the station livable and
breathable.** There are a lot of interesting real life challenges
associated with making this happen, not in the least of which is that in
space, every gas molecule wants desperately to escape into the cold of
space. There is also the challenge of keeping the station appropriately
temperature-regulated despite the cold outside and occasional plasma
fires inside.

Where it does not conflict with fun (see below), **incorporate realistic
processes and simulations**. As stated in the [fundamental design
principles](en/general-development/feature-proposals/ss14-fundamental-design-principles.md),
intuitive simulation makes for a better game. Having real-life analogs
for gas behaviors helps make both atmos more discoverable and intuitive
for new players and also caters to atmos nerds.

None of these realism additions require any sort of math to play. Only a
basic understanding of the following principles should be enough to
understand and play:

1. You should not be able to spin energy out of thin air.
2. When given a choice, gas flows from high pressure to low pressure.
3. When given a choice, temperature transfers from hot to cold.

### An Interlude on Realism

The chief objective of a game is to be fun to play, and not to be
realistic. Where realism conflicts with fun, fun should be chosen every
time.

**However,** games are most fun when players have a sense of agency
(their actions matter in determining the final outcome of the game) and
when their challenges are struggles are believable.

In order for players' challenges and struggles to be believable, the
game universe must obey a consistent system of rules and physical
limitations. It would not be fun if players have a way to *deux ex
machina* out of every imaginable problem (e.g. Nukies? Why don't we use
the magical remote control that makes all the nukies disappear? After
all, we have *spess magic*.) We're in space, and it should be hard to
get gases because they tend to escape into... you know... space. Not
every station should have a magical gas miner.

But guess what? It turns out that realism provides both a set of
interesting problems and a set of rules for how a universe should
consistently behave. So by making things more realistic, we get both
interesting mechanics and a set of consistent rules for free. Of course
realism doesn't trump fun, and if it is fun to make something that is
unrealistic (e.g. plasma gas), then we should always pick fun.
**However, where realism does not conflict with being fun, then we
should opt to be realistic because it provides a set of interesting
problems and consistent rules.**

After all, why do we say that *PV=nRT*? Shouldn't we make up a different
gas law because realism is bad?

## High-Priority Proposals

These proposals should be implemented first, because they have an
outsized impact on atmos balance as a whole.

- **Phase out gas miners for all upstream maps.** It doesn't make sense
that all stations have free and plentiful sources of gas, otherwise you
might as well be on a planet. This is a game that is literally set in
space. It would make sense to keep a few specialty miners, e.g. for
plasma, if a station is set on a plasma mining planet. But in general,
all other gases should be imported via gas canisters. Miners should
still be kept available for any forks that choose to use them.

- This solves problems (1) and (3). Maintaining a livable atmos would
involve work during the round beyond setting up distro to pipe gas from
miners. It would help increase interactions with other departments, such
as cargo and salvage as atmos needs to order gas.

- Ensuring a appropriate round-start supply of gas would make the game
playable without a functional cargo department.

- This would discourage fighting fires or atmos problems by wholesale
spacing a section. There is currently very little downside to spacing a
section to get rid of problems because of an unlimited gas supply.

- There is [overwhelming consensus on mappers for
this](https://discord.com/channels/310555209753690112/770682801607278632/1162179968915210280).

- As an interim or for very low pop-count maps, keep miners but make
them mine gas at low temperature that has to be heated up before use.
This preserves a bit of an incentive for atmos players to not space a
section at the first sign of trouble.

- **Globally increase MaxTransferRate** for devices that are not
flow-based, e.g. pumps.

- This solves problem (2). Among other things, it would make scrubbers
and other devices actually useful for combating atmospheric problems.
Currently players prefer to just space everything. Increasing this would
provide a feasible alternative.

## Medium Priority

- **Make all atmos devices flow-based.** This means driving gas flow as
a result of pressure differences created using pumps. The specific
offenders are currently any "pumped" device that is not a dedicated
pump, e.g. air vents, scrubbers, filters, and mixers.

- This addresses an issue about atmos intuition and accessibility.
Players should not have to understand the internal workings of the pipe
net system (e.g. a pipe is one big node, gases move between them). In
real life, a fan or pump creates a pressure difference, and pressure
differences drive gas flow. If you blow on one end of a straw, you can
expect it to come out of the other end, not get stuck in a pipe net.

- This also addresses (2). Instead of having a fixed upper bound on
volume transfer, transfer rates would always depend on the pressure
difference that you create.

- **Add maximum temperature and pressure limits for most devices.** It
does not make sense that you can contain the surface of the sun in your
pipes. Adding limits would encourage designing processes and systems
that work within reasonable constraints.

- Some "sub-optimal" setups are really unintuitive and wouldn't work in
real life due to temperature and pressure limits.

- There are some concerns about being able to run burn chambers and the
TEG. The screenshot below demonstrates a TEG that is capable of powering
an entire large-sized station (256.8 kW current output, the peak output
is quite a bit higher) with a maximum pressure excursion of 1600 kPa. It
shows that pipes that burst at reasonable pressures are entirely
consistent with having burn chambers. You just need to set them up
correctly.


![image](https://user-images.githubusercontent.com/3229565/274441724-712f4ebf-7440-4d81-879e-19aa29788822.png)

- This addresses problem (1), the "set up and forget" issue by adding
temperatures and pressures to monitor. It also allows the opportunity
for sabatoge.


- **Make heaters and freezers thermodynamically sound.** Keeping a
station properly heated or cooled is actually a substantial real-life
problem. Why deprive atmos techs an actual challenge that keeps gameplay
interesting? Because of the existence of generators like the TEG,
keeping things thermodynamically balanced is also a great way to prevent
infinite power hacks.

## Low Priority

- **Make station air flow-based.** Currently, air vents release air when
the pressure is too low, and by default scrubbers only scrub waste
gases. So if for some reason the station gets cold, there's no easy way
to cycle the air out and heat it up. Of course, you could set all the
scrubbers to siphon, heat your distro, and then set the air alarm to
fill. But that would just be describing a bad way of doing what real
life HVAC systems have always been doing: keep the air flowing.

- This addresses problem (2) by making it possible to better regulate
station temperature.

- **Make heaters and freezers binary.** Just like your central heating
and air conditioning circulate air through heat/cold coils, gases should
flow across heaters and freezers in order to exchange temperature.

- **Adding process-based alternatives to scrubbers and filters.** For
example, with gas reaction-based scrubbing processes, scrubbers with
limited uses, or physical processes.

- This addresses problems (1) and (3) by adding more content that is
directly related to the well-being of the station.

- One of the most pressing challenges in the real world is "how do you
separate different kinds of gas." Most current methods of gas extraction
are based on chemistry (e.g. real life carbon dioxide scrubbers contain
chemicals that react with CO2, pulling it out) or physical methods (e.g.
fractional distillation, where you cool down air in different stages to
get liquid nitrogen, oxygen, etc.) This creates a lot of opportunity for
new game play mechanics and industrial processes. This would also give
more opportunities to add gas-based reactions (i.e. more content).

- This does not advocate for removal of scrubbers and filters, but
rather makes it a mapper option, e.g. whether to use scrubbers at
round-start or make atmos set up a system depending on the desired level
of role-play.

- When set up correctly, these should have much higher processing rates
than scrubbers. This should give an incentive to set these up, e.g. on
longer rounds, while still keeping scrubbers as an option.

- This adds "optimization, tinkering, and creation of intricate builds."

- **Add gas condensation.** This would enable fractional distillation
and permit conversion between gas and the equivalent reagent.

- **Add pump efficiency curves.** Pumps have to work harder when they
create a larger pressure difference. As a result, pumping from 1 atm to
2 atm should be easier (read: faster) than pumping from 1 atm to 10 atm.
You could create a multi-stage pump, and indeed, that is what people in
real life do, at the trade-off of less throughput.

- **Breaking windows at high enough tile pressure differences.** To
handle explosions and resulting space wind without leaning on the
explosino system, and to encourage people to design burn chambers with
more controlled burns instead of always putting their pedal to the
metal.

- **Various QoL improvements** such as the RPD.

---
## [ParadiseSS13/Paradise](https://github.com/ParadiseSS13/Paradise)@[a069966658...](https://github.com/ParadiseSS13/Paradise/commit/a069966658a0a5b4a56dea7467a623ac658088d1)
#### Sunday 2023-12-31 12:51:47 by Zack

Qol improvements for the ghost bar (#23421)

* Added some garbage bins, added a vender for the ghost bar kitchen

* Fixed the floor under a table

* Moved the shadycig vender a bit more to the wall and removed a beaker that I placed on accident

* Removed a wall behind a vender

* fuck you merge masters

---------

Co-authored-by: S34N <12197162+S34NW@users.noreply.github.com>

---
## [L7NEG/Ultimate-Menu](https://github.com/L7NEG/Ultimate-Menu)@[f6455a8fa9...](https://github.com/L7NEG/Ultimate-Menu/commit/f6455a8fa9327899a831c7bbd2f39bcd29c4a740)
#### Sunday 2023-12-31 13:21:23 by L7NEG

V19 Changelogs

V19 ChangeLogs:

Updated For 1.68

Added Vehicle > Ultimate Vehicle Spawner Menu (With 1.68 New Vehicles) (Credits generic.goose On Discord For His Cool Ultimate Vehicle Spawner / L7NEG For Adding Save Nearest Vehicle In Saved Vehicles Menu)

Updated Remote Nightclub Safe Money Loop To 1.68 In Ultimate Money Methods Menu

Added Events Menu > Yeti Hunt Menu (Credits ShinyWassabi For The Globals And Coordinates On UC)

Added 1.68 Unlocker Menu > Unlock 1.68 New Vehicles (Credits ShinyWassabi For The Globals On UC)

Rmoved 1.68 Unlocker Menu > Enable Vincent Contact Missions

Added Back 1.68 Unlocker Menu > Enable Enable Deleted Vehicles

Added Back 1.68 Unlocker Menu > Enable Knife And Baseball Bat Skins In GunVan

Fixed Spawn Vehicle In Online Players Troll Menu (Please Note That The Total Number Of Players Means The Whole Players In Your Session Its Called From Kiddion Api So Dont Worry If You See That The Total Number Of Online Players Is Diff As It Collects Those Who Are Watching The Session You Play)

BugFixes And Overall Improvements

Updated Credits Section

Updated Missions Selector And Cooldown Menu

And That's It Bros

I Hope You All To Have A Great Day In Your Real Life Enjoy ❤️

---
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[dd11a6d43b...](https://github.com/rmellis/HelpUKR-master/commit/dd11a6d43b4d7269302f607da4dd7cffdee39084)
#### Sunday 2023-12-31 14:52:56 by rmellis

Added Day 676 - Targets and Days (TL) Eng+Ukr

Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
Million payment terminals in Russia stopped working since yesterday because we disabled Evotor, the top online cash register maker. Some sellers had up to 90% non-cash turnover, right before New Year's. It's likely causing huge losses to the aggressor's economy. This reflects in agitated customers and sellers.
Remember, every dollar lost in their economy means less funding for the war. That's the impact of economic sanctions, and our efforts too.
/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Мільйон платіжних терміналів по всієї рашці не працює зі вчора, бо ми поклали Евотор - найбільшого виробника онлайн-кас. Деякі продавці мали до 90% безготівкового обігу, ще і напередодні Нового Року. Це мають бути мільярдні збитки для економіки агресора тільки від цієї однієї нашої операції. Я вже не кажу про роздратованих москалів по обидва боки прилавка.
Нагадаємо, що кожен втрачений долар економіки, це втрачений цент на фінансування війни. Так працюють економічні санкції, так працюємо і ми.

---
## [LionsPhil/pixmasclock](https://github.com/LionsPhil/pixmasclock)@[2b499d3c96...](https://github.com/LionsPhil/pixmasclock/commit/2b499d3c96cf862d1d138b9bb9dede8a9815240b)
#### Sunday 2023-12-31 14:59:09 by LionsPhil

SDL 2 support (without removing SDL 1)

Second binary, which is actually partially because I plan to stick a
menu on this thing for HyperPixel touchscreen purposes.

Slightly ugly SDLVERSION hacks, but mostly the two are compatible. The
big changes are contained to the separate main binary, needing to do
different graphics setup.

render() must now use the provided, not remembered, framebuffer, and
report if it wants to update the screen, which the main binary takes
care of (flip for SDL1, more complicated dance for SDL2).

Some changes around palette handling. Also surface creation---SDL2 is
more pedantic about complaining if you hand it a pixel format bitfield
at the same time as saying "paletted, please".

VSCode noise.

Flag which hacks are working or misbehaving weirdly under SDL2.

Yes, this all needs a pile of refactoring, but as always time is short.

---
## [truecharts/charts](https://github.com/truecharts/charts)@[550367183d...](https://github.com/truecharts/charts/commit/550367183d70ebeff5d6759c29db1254cebbf21c)
#### Sunday 2023-12-31 15:00:13 by TrueCharts Bot

chore(deps): update container image ghcr.io/linkwarden/linkwarden to v2.4.5@0247ad1 by renovate (#16677)

This PR contains the following updates:

| Package | Update | Change |
|---|---|---|
|
[ghcr.io/linkwarden/linkwarden](https://togithub.com/linkwarden/linkwarden)
| minor | `v2.3.0` -> `v2.4.5` |

---

> [!WARNING]
> Some dependencies could not be looked up. Check the Dependency
Dashboard for more information.

---

### Release Notes

<details>
<summary>linkwarden/linkwarden (ghcr.io/linkwarden/linkwarden)</summary>

###
[`v2.4.5`](https://togithub.com/linkwarden/linkwarden/releases/tag/v2.4.5)

[Compare
Source](https://togithub.com/linkwarden/linkwarden/compare/v2.4.4...v2.4.5)

#### What's Changed

-   small improvement + better error handling

**Full Changelog**:
https://github.com/linkwarden/linkwarden/compare/v2.4.4...v2.4.5

###
[`v2.4.4`](https://togithub.com/linkwarden/linkwarden/releases/tag/v2.4.4)

[Compare
Source](https://togithub.com/linkwarden/linkwarden/compare/v2.4.3...v2.4.4)

#### What's Changed

- bugs fixed by [@&#8203;daniel31x13](https://togithub.com/daniel31x13)
in
[https://github.com/linkwarden/linkwarden/pull/379](https://togithub.com/linkwarden/linkwarden/pull/379)

**Full Changelog**:
https://github.com/linkwarden/linkwarden/compare/v2.4.3...v2.4.4

###
[`v2.4.3`](https://togithub.com/linkwarden/linkwarden/releases/tag/v2.4.3)

[Compare
Source](https://togithub.com/linkwarden/linkwarden/compare/v2.4.2...v2.4.3)

#### What's Changed

- Bug fixed by [@&#8203;daniel31x13](https://togithub.com/daniel31x13)
in
[https://github.com/linkwarden/linkwarden/pull/375](https://togithub.com/linkwarden/linkwarden/pull/375)
- hotfix by [@&#8203;daniel31x13](https://togithub.com/daniel31x13) in
[https://github.com/linkwarden/linkwarden/pull/376](https://togithub.com/linkwarden/linkwarden/pull/376)

**Full Changelog**:
https://github.com/linkwarden/linkwarden/compare/v2.4.2...v2.4.3

###
[`v2.4.2`](https://togithub.com/linkwarden/linkwarden/releases/tag/v2.4.2)

[Compare
Source](https://togithub.com/linkwarden/linkwarden/compare/v2.4.1...v2.4.2)

#### What's Changed

- minor bug fixed by
[@&#8203;daniel31x13](https://togithub.com/daniel31x13) in
[https://github.com/linkwarden/linkwarden/pull/372](https://togithub.com/linkwarden/linkwarden/pull/372)

**Full Changelog**:
https://github.com/linkwarden/linkwarden/compare/v2.4.1...v2.4.2

###
[`v2.4.1`](https://togithub.com/linkwarden/linkwarden/releases/tag/v2.4.1)

[Compare
Source](https://togithub.com/linkwarden/linkwarden/compare/v2.4.0...v2.4.1)

#### What's Changed

- updated README by
[@&#8203;daniel31x13](https://togithub.com/daniel31x13) in
[https://github.com/linkwarden/linkwarden/pull/363](https://togithub.com/linkwarden/linkwarden/pull/363)
- updated README by
[@&#8203;daniel31x13](https://togithub.com/daniel31x13) in
[https://github.com/linkwarden/linkwarden/pull/364](https://togithub.com/linkwarden/linkwarden/pull/364)
- bugs fixed by [@&#8203;daniel31x13](https://togithub.com/daniel31x13)
in
[https://github.com/linkwarden/linkwarden/pull/366](https://togithub.com/linkwarden/linkwarden/pull/366)

**Full Changelog**:
https://github.com/linkwarden/linkwarden/compare/v2.4.0...v2.4.1

###
[`v2.4.0`](https://togithub.com/linkwarden/linkwarden/releases/tag/v2.4.0)

[Compare
Source](https://togithub.com/linkwarden/linkwarden/compare/v2.3.0...v2.4.0)

### Linkwarden 2.4

Read the blog: https://blog.linkwarden.app/releases/v2.4

#### What's New?

##### 🎨 Much Improved Design

Enjoy a visual upgrade with sleeker icons, enhanced coloring, and
redesigned link cards for a more engaging experience. Huge thanks to
[DaisyUI](https://daisyui.com) for this!

##### 🏛️ All Bookmarks Now Get Archived!

There is a background script that automatically processes each link,
creating archived versions without any user intervention. So from now
on, every bookmark you save, **including those imported from other
sources**, is automatically preserved, this means you'll have access to
your favorite article even if the original content is gone!

##### 🗃️ Archive Formats Other Than Webpages

You can now archive Links that contain a PDF or Image and link
preservation is no longer limited to webpages, for example:
https://www.africau.edu/images/default/sample.pdf

##### 📋 Added Compact List View

This new feature introduces a list-based format for viewing bookmarks.
It's designed for those who prefer a more structured and straightforward
way to browse their saved links. This view can be especially handy for
quickly scanning through numerous bookmarks, making it easier to find
what you're looking for.

##### 👍 Enhanced User Experience

There are many improvements made to enhance the user experience of the
app, like for instance you can now add new Collections right from the
navbar. Also when you try to delete a Link, you get a "Are you sure"
prompt to prevent accidentally deletion of your Links.

##### 🔐 Added Many More Single Sign-On and Oauth Integrations

From Authentik, to Apple, Google, and more... The list goes on.

##### ✅ And more...

Check out the full changelog below.

**Full Changelog**:
https://github.com/linkwarden/linkwarden/compare/v2.3.0...v2.4.0

</details>

---

### Configuration

📅 **Schedule**: Branch creation - "before 10pm on monday" in timezone
Europe/Amsterdam, Automerge - At any time (no schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR has been generated by [Renovate
Bot](https://togithub.com/renovatebot/renovate).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzNy4xMTUuMCIsInVwZGF0ZWRJblZlciI6IjM3LjExNS4wIiwidGFyZ2V0QnJhbmNoIjoibWFzdGVyIn0=-->

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a886801dc4...](https://github.com/treckstar/yolo-octo-hipster/commit/a886801dc43b0d51722158054e1cd44032d87e92)
#### Sunday 2023-12-31 15:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Qwertytoforty/Paradise](https://github.com/Qwertytoforty/Paradise)@[6a109ade7f...](https://github.com/Qwertytoforty/Paradise/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Sunday 2023-12-31 15:26:10 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [huytran17/cheerup](https://github.com/huytran17/cheerup)@[316e2276ee...](https://github.com/huytran17/cheerup/commit/316e2276eed1f9dbb35ad055d6e87826ec1360a4)
#### Sunday 2023-12-31 16:33:17 by huytran17

Last commitment of 2023. Thank you all for coming in my life. Not necessarily good, not necessarily bad, neither praiseworthy nor blameworthy. But all are valuable pieces of luggage for me to move forward. Thanks for everything, 2023.

---
## [Road-to-56-RP/roadto56rp](https://github.com/Road-to-56-RP/roadto56rp)@[8ef61ada41...](https://github.com/Road-to-56-RP/roadto56rp/commit/8ef61ada416bee946097def779e43d3e85efab5c)
#### Sunday 2023-12-31 16:44:13 by Warlider

MEFO Free baby

- Canceling and Renewing MEFO's is free now (simpy fucked himself, might as well make it free)
- Once more fixed "Democratic Socialism" being borked. Imagine making a focus name that has overlap with ideology. Wunderbar.

---
## [callgirlsingoa1/Call-Girl-In-Goa-Panaji-9289866737-Goa-Russian-Escort-Service](https://github.com/callgirlsingoa1/Call-Girl-In-Goa-Panaji-9289866737-Goa-Russian-Escort-Service)@[a5bf4c09bc...](https://github.com/callgirlsingoa1/Call-Girl-In-Goa-Panaji-9289866737-Goa-Russian-Escort-Service/commit/a5bf4c09bc61b153b151d0c45dbedd6d8f301a2a)
#### Sunday 2023-12-31 17:09:36 by callgirlsingoa1

Add files via upload

Call Girl In ✂️ North Goa ✂️9289866737 ✂️ Goa Russian Escort Service
Note :- Pic Collectors . time passers , Bargainers Stay Away . Call Girls In All Goa Area Door Step Delivery We Offering You 100% Genuine Completed Body And Mind Relaxation With Happy Ending ServiCe Done By Most Attractive Charming Soft Spoken Bold Beautiful Full Cooperative Independent And Agency Escort Girls Available In All Star Hotel And Resorts Guest house ServiCe In All Over Goa

We Have Extremely Beautiful Broad Minded Cute Sexy And Hot Call Girls and Escorts, We Are Located in 3* 4* 5* Hotels in Goa. Safe And Secure High Class Services Affordable Rate 100% Satisfaction, Unlimited Enjoyment. Any Time for Model/Teens Escort in Goa High Class luxury and Premium Escorts ServiCe.

CALL US High Class Luxury and Premium Escorts ServiCe We Provide Well Educated, Royal Class Female, High-Class Escorts Agency Offering a Top High Class Escorts Service In the & Several Nearby All Places Of Goa Our Service Available IN All 3/4/5 STAR HOTEL ,Out Call Services.24 hrs

Locations: Baga, Calangute, Candolim, Arpora, Anjuna, Morjim, Vagator, Dona Paula, Panaji, Arambol, Ashvem, Bardez, Nerul, Nagoa, Porvorim, Sangolda, Siolom, Mapusa Miramar and All over North Goa.

ALL OVER South Goa Colva Margao Benalium Varca Mobor Majorda Agonda canacona Call 24×7. Your assistance for your service…9289866737

---
## [Project-Mist-OS/frameworks_base](https://github.com/Project-Mist-OS/frameworks_base)@[5b324a1928...](https://github.com/Project-Mist-OS/frameworks_base/commit/5b324a19280358c1426d7e4043e019099045f4bb)
#### Sunday 2023-12-31 17:22:47 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>
Signed-off-by: Hưng Phan <phandinhhungvp2001@gmail.com>

---
## [PigeonLord/Shiptest](https://github.com/PigeonLord/Shiptest)@[b22529fc74...](https://github.com/PigeonLord/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Sunday 2023-12-31 17:32:12 by zevo

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
## [arsLan4k1390/Cherrygram](https://github.com/arsLan4k1390/Cherrygram)@[6fb8120768...](https://github.com/arsLan4k1390/Cherrygram/commit/6fb8120768ce0733ea801e0d5dec0a45542ed120)
#### Sunday 2023-12-31 18:04:10 by arsLan4k1390

Fix Package Installer crash on ShitOS (Android 14 QPR1)

Package installer on Pixel Experience has been crashing because of the resolution of background. I hate Google and Pixel devices. This is another reason to use Samsung devices - my Samsung device has never had this problem on Android 14.

---
## [propbreakerfpv/ripgrep](https://github.com/propbreakerfpv/ripgrep)@[082245dadb...](https://github.com/propbreakerfpv/ripgrep/commit/082245dadb3854238e62b91aa95a46018cf16ef1)
#### Sunday 2023-12-31 18:38:28 by Andrew Gallant

cli: replace clap with lexopt and supporting code

ripgrep began it's life with docopt for argument parsing. Then it moved
to Clap and stayed there for a number of years. Clap has served ripgrep
well, and it probably could continue to serve ripgrep well, but I ended
up deciding to move off of it.

Why?

The first time I had the thought of moving off of Clap was during the
2->3->4 transition. I thought the 3.x and 4.x releases were great, but
for me, it ended up moving a little too quickly. Since the release of
4.x was telegraphed around when 3.x came out, I decided to just hold off
and wait to migrate to 4.x instead of doing a 3.x migration followed
shortly by another 4.x migration. Of course, I just never ended up doing
the migration at all. I never got around to it and there just wasn't a
compelling reason for me to upgrade. While I never investigated it, I
saw an upgrade as a non-trivial amount of work in part because I didn't
encapsulate the usage of Clap enough.

The above is just what got me started thinking about it. It wasn't
enough to get me to move off of it on its own. What ended up pushing me
over the edge was a combination of factors:

* As mentioned above, I didn't want to run on the migration treadmill.
This has proven to not be much of an issue, but at the time of the
2->3->4 releases, I didn't know how long Clap 4.x would be out before a
5.x would come out.
* The release of lexopt[1] caught my eye. IMO, that crate demonstrates
exactly how something new can arrive on the scene and just thoroughly
solve a problem minimalistically. It has the docs, the reasoning, the
simple API, the tests and good judgment. It gets all the weird corner
cases right that Clap also gets right (and is part of why I was
originally attracted to Clap).
* I have an overall desire to reduce the size of my dependency tree. In
part because a smaller dependency tree tends to correlate with better
compile times, but also in part because it reduces my reliance and trust
on others. It lets me be the "master" of ripgrep's destiny by reducing
the amount of behavior that is the result of someone else's decision
(whether good or bad).
* I perceived that Clap solves a more general problem than what I
actually need solved. Despite the vast number of flags that ripgrep has,
its requirements are actually pretty simple. We just need simple
switches and flags that support one value. No multi-value flags. No
sub-commands. And probably a lot of other functionality that Clap has
that makes it so flexible for so many different use cases. (I'm being
hand wavy on the last point.)

With all that said, perhaps most importantly, the future of ripgrep
possibly demands a more flexible CLI argument parser. In today's world,
I would really like, for example, flags like `--type` and `--type-not`
to be able to accumulate their repeated values into a single sequence
while respecting the order they appear on the CLI. For example, prior
to this migration, `rg regex-automata -Tlock -ttoml` would not return
results in `Cargo.lock` in this repository because the `-Tlock` always
took priority even though `-ttoml` appeared after it. But with this
migration, `-ttoml` now correctly overrides `-Tlock`. We would like to
do similar things for `-g/--glob` and `--iglob` and potentially even
now introduce a `-G/--glob-not` flag instead of requiring users to use
`!` to negate a glob. (Which I had done originally to work-around this
problem.) And some day, I'd like to add some kind of boolean matching to
ripgrep perhaps similar to how `git grep` does it. (Although I haven't
thought too carefully on a design yet.) In order to do that, I perceive
it would be difficult to implement correctly in Clap.

I believe that this last point is possible to implement correctly in
Clap 2.x, although it is awkward to do so. I have not looked closely
enough at the Clap 4.x API to know whether it's still possible there. In
any case, these were enough reasons to move off of Clap and own more of
the argument parsing process myself.

This did require a few things:

* I had to write my own logic for how arguments are combined into one
single state object. Of course, I wanted this. This was part of the
upside. But it's still code I didn't have to write for Clap.
* I had to write my own shell completion generator.
* I had to write my own `-h/--help` output generator.
* I also had to write my own man page generator. Well, I had to do this
with Clap 2.x too, although my understanding is that Clap 4.x supports
this. With that said, without having tried it, my guess is that I
probably wouldn't have liked the output it generated because I
ultimately had to write most of the roff by hand myself to get the man
page I wanted. (This also had the benefit of dropping the build
dependency on asciidoc/asciidoctor.)

While this is definitely a fair bit of extra work, it overall only cost
me a couple days. IMO, that's a good trade off given that this code is
unlikely to change again in any substantial way. And it should also
allow for more flexible semantics going forward.

Fixes #884, Fixes #1648, Fixes #1701, Fixes #1814, Fixes #1966

[1]: https://docs.rs/lexopt/0.3.0/lexopt/index.html

---
## [Raskulk/Improved-Mobile-main.scm](https://github.com/Raskulk/Improved-Mobile-main.scm)@[c6fa6a714d...](https://github.com/Raskulk/Improved-Mobile-main.scm/commit/c6fa6a714d98ce67896d724da6d511fa1207db9f)
#### Sunday 2023-12-31 18:44:53 by Raskulk

v38

(new version of Sanny Builder, had to recompile the sources)
Changes from 31.12.23 (version 38):
I wish you all a happy New Year!
- After the "Big Smoke" mission at the Los Santos cemetery, the grave of CJ's mother is now covered with earth, a monument appears near it.
- After the Los Sepulcros mission at the Los Santos cemetery, Kane's grave is now covered with earth, a monument appears near it.
- On the "555 We Tip" mission, you now have to drive yourself into the garage to put drugs in the prosecutor's car.
- Near the Los Santos Police Station, you can now view information about parking lots.
- On the "Black Project" mission, the searchlights now switch to search mode if the main character opens fire with any weapon except a pistol with a silencer.
- The behavior of the military has been slightly redesigned on the Black Project mission.
- On the pimp mission, the level scale now looks similar to other side missions.
- Added unused text during the completion of the pimp's mission (appears only when the mission is completed again).
- On the Mountain Cloud Boys mission, Blood Feathers now have unique models.
- On the mission "The Da Nang Thang", Snakehead's accuracy and attack speed were increased.
- On the "Dam and Blast" mission, the guards now have increased accuracy.
- CJ's phrases in a hidden knife attack are now pronounced only outside of missions.
- Some bugs have been fixed.

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[fc530572f6...](https://github.com/AnywayFarus/Skyrat-tg/commit/fc530572f6bbe4db0a36df35251a2dd7e62c6b64)
#### Sunday 2023-12-31 19:04:05 by SkyratBot

[MIRROR] Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors [MDB IGNORE] (#25493)

* Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/80158 by making
curses block you from playing Russian roulette regardless of whether or
not there's a live bullet in your Russian revolver's chamber.

A Russian revolver has been added to the contraband section of each Good
Clean Fun vendor.

## Why It's Good For The Game

The bug is incredibly funny, but ~~I want GBP~~ probably should be
fixed.

There's no actual way to get (more) Russian revolvers outside of the
mapstart ones, and that can be a bit stifling to gimmicks that involve
them. And Russian roulette IS a game.

Like the roundstart ones, you could unload these vendor revolvers for
.357 bullets, but you can already just print .357 bullets from a hacked
autolathe directly, so I don't think that's an issue.

## Changelog

:cl: ATHATH
fix: Spacemen can no longer use curses to cheat at Russian roulette by
selectively blocking attempts to shoot themselves.
add: A Russian revolver has been added to the contraband section of each
Good Clean Fun vendor.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors

---------

Co-authored-by: ATH1909 <42606352+ATH1909@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [petre-symfony/30-Days-with-Last-Stack-2023](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023)@[3e7222832c...](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023/commit/3e7222832c34d6704c96eaf7d289fe08c06320aa)
#### Sunday 2023-12-31 19:10:23 by petrero

25.11 Pointing Tailwind at your Component PHP Classes
 - Though, one detail. Tailwind scans our source files, finds all the Tailwind classes we're using and includes those in the final CSS file. And because we're now including classes inside PHP, we need to make sure Tailwind sees those.

 In tailwind.config.js, on top, I'll paste in one more line to make it scan our Twig component PHP classes

 Changing the Component Tag Name
 - Ok, we're nearly done for today - but I want to celebrate and use the new component in one more spot: on the voyage index page, for the "New Voyage" button.

 Open index.html.twig... change this to a <twig:Button>... then we can remove most of these classes. The bold is specific to this spot I think

 When we refresh... it renders! Though... when I click... nothing happens! You probably saw why: this is now a button, not an a tag.

 That's okay: we can make our component just a bit more flexible. In Button.php, add another property: string $tag defaulting to button

 Then in the template, use {{ tag }} for the starting tag and the ending tag

 Finish in index.html.twig: pass tag="a"

 Now over here... when we click... got it!

 That's it! I hope you love Twig components as much as I do. But they can do even more! I didn't tell you how you can prefix any attribute with : to pass dynamic Twig variables or expressions to a prop. We also didn't discuss that the component PHP classes are services. Yea, you can add an __construct() function, autowire other services, like VoyageRepository, then use those to provide data to your template... making the entire component standalone and self-sufficient. That's one of my favorite features.

 Tomorrow we're going to keep leveraging Twig components to create a modal component... then see just how easily we can use modals whenever we want.

---
## [Lambdagon/fc](https://github.com/Lambdagon/fc)@[9e7ad80845...](https://github.com/Lambdagon/fc/commit/9e7ad80845887de75d998e80a9e0741e3f1f2c2e)
#### Sunday 2023-12-31 19:28:24 by Rainer

unprefabbed broken weapons, made the vermin8 not just suck, deluxe shades not fucked up, made the pot not evil

---
## [ProfessorSidon/VGC-Damage-Calculator-Chinese](https://github.com/ProfessorSidon/VGC-Damage-Calculator-Chinese)@[90ebab0707...](https://github.com/ProfessorSidon/VGC-Damage-Calculator-Chinese/commit/90ebab070756a16e150c0b43c34b2618817bce6b)
#### Sunday 2023-12-31 19:47:45 by nerd-of-now

Added ??? type, remember gen/level, 2x BP button, more nat dex field conditions, minor damage adjustments

- Added the ??? type to gens 2-4, yes it's different from no typing
- The calc will now remember the last level system and gen that the user used
- Changed the 2x attack field from a dropdown list to a button
- Removed Typeless from the options for Tera Type
- Changed where Aura Wheel checks for its type change
- Changed how the calc handles ignoring abilities so that the moves that ignore abilities will also affect things like Friend Guard and Aura Break
- Added a check for Struggle to Wonder Guard
- Fixed OHKO move logic (was reverse of what it was supposed to be)
- Fixed the Hydro Steam/Utility Umbrella interaction
- Fixed the Power-Up Punch/Parental Bond interaction (a +6 Power-Up Punch would incorrectly calc for a +7 second hit)
- The calc will correctly save and export male Indeedee now
- Added a few more default abilities

---
## [peterlevel1/react](https://github.com/peterlevel1/react)@[b6978bc38f...](https://github.com/peterlevel1/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Sunday 2023-12-31 20:20:15 by Andrew Clark

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
## [petre-symfony/30-Days-with-Last-Stack-2023](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023)@[d3127a151d...](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023/commit/d3127a151d5ea8ac27535be72f4a556cb0737ec5)
#### Sunday 2023-12-31 21:36:15 by petrero

26.9 Finally, let's frost this cake. Near the bottom of the content, I'll paste in the planet checkboxes

 This is more boring code! I loop over the planets and render input check boxes. My Symfony controller is already set up to read the planets parameter and filter the query.

 Final test. Open it up. Lovely! Now watch: click a few. When I press "See Results", the table should update. Boom. It did!

 But the coolest part is... how this worked! Think about it: I click this button... and the table reloads. That means the form is submitting. But... what caused that? Look at the button: there's no code to submit the form. So what's going on?

 Remember: this button, the planet checkboxes and this modal physically live inside the <form> element. And what happens when you press a button that lives inside a form? It submits the form! We run the modal#close, but we also allow the browser to do the default behavior: submitting the form. This is ancient alien technology at work!

 On the close button, I was a bit sneaky. When I added that, I included a type="button". That tells the browser to not submit any form that it might be inside. That's why when we click "X", nothing updates. But when we click "see results", the form submits.

 Woh! Best day ever! Tomorrow, it's time to look at Live components, where we take Twig components and let them re-render on the page via Ajax as the user interacts when them.

---
## [SRockt/SRockt](https://github.com/SRockt/SRockt)@[c4008aa1ac...](https://github.com/SRockt/SRockt/commit/c4008aa1acbde852eeab681e791f09729ce2d60c)
#### Sunday 2023-12-31 23:19:01 by Siegfried Serve

{
    "githubPullRequests.remotes": [
        "origin",
        "upstream",
        "dscho:drive-less-symlinks",
        "@ext:GitHub.vscode-pull-request-github remotes"
    ],
    "workbench.settings.applyToAllProfiles": [
        "githubPullRequests.remotes",
        "git.branchValidationRegex"
    ],
    "githubIssues.queries": [
        {
            "label": "Meine Probleme",
            "query": "default"
        },
        {
            "label": "Erstellte Probleme",
            "query": "author:${user} state:open repo:${owner}/${repository} sort:created-desc"
        },
        {
            "label": "Aktuelle Probleme",
            "query": "state:open repo:${owner}/${repository} sort:updated-desc"
        }
    ],
    "window.menuBarVisibility": "classic",
    "workbench.colorTheme": "PowerShell ISE",
    "cloudcode.autoDependencies": "off",
    "security.promptForLocalFileProtocolHandling": false,
    "github.copilot.advanced": {

    },
    "cloudcode.duetAI.project": "glassy-clock-403222",
    "editor.unicodeHighlight.nonBasicASCII": false,
    "mssql.enableQueryHistoryCapture": false,
    "mssql.objectExplorer.groupBySchema": true,
    "git.enableSmartCommit": true,
    "gitlens.ai.experimental.provider": "anthropic",
    "gitlens.ai.experimental.anthropic.model": "claude-2.1",
    "git.autofetch": true,
    "git.autoStash": true,
    "git.branchRandomName.dictionary": [
        "adjectives",
        "animals",
        "numbers"
    ],
    "git.branchRandomName.enable": true,
    "git.branchSortOrder": "alphabetically",
    "git.branchValidationRegex": "vscode.git",
    "git.commandsToLog": [
        "vscode.git"
    ],
    "git.defaultCloneDirectory": ""
}
<!DOCTYPE html><html class="maestro maestro--responsive global-header" lang="de" xml:lang="de" xmlns="http://www.w3.org/1999/xhtml"><head><script nonce="AwAFyR8mbB48mik7l2cB">
window._goch_ = {};
window.addEventListener('click', function(event) {
    'use strict';
    for (var elm = event.target; elm; elm = elm.parentElement) {
        if (elm.id &&
            window._goch_.hasOwnProperty(elm.id) &&
            window._goch_[elm.id].call(elm, event) === false) {
            event.preventDefault();
        }
    }
}, true);
window._csp_external_script_nonce = "e2lVsGiUH3tX0noOW1W+"</script><link href="https://cfl.dropboxstatic.com" rel="preconnect" /><link href="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" rel="shortcut icon" /><title>Dropbox</title><meta content="noindex, nofollow, noimageindex" name="robots" /><meta content="origin-when-cross-origin" name="referrer" /><meta content="width=device-width, initial-scale=1" name="viewport" /><meta content="app-id=327630330" name="apple-itunes-app" /><script type="text/javascript" nonce="AwAFyR8mbB48mik7l2cB">if (window.performance && window.performance.mark) { window.performance.mark("requirejs_start"); }</script> <link crossorigin="anonymous" href="https://cfl.dropboxstatic.com/static/metaserver/static/js/alameda_bundle/alameda_bundle_chrome_de-vflU8rBSF.js" as="script" nonce="e2lVsGiUH3tX0noOW1W+" rel="preload" type="text/javascript" /> <script type="text/javascript" nonce="AwAFyR8mbB48mik7l2cB">
            (()=>{"use strict";const e=window;let a;const r=()=>{a=[],e.addRequireLoadCallback=e=>a.push(e),e.configureRequire=function(){const a=arguments;e.addRequireLoadCallback(()=>e.configureRequire.apply(null,a))},e.define=function(){const a=arguments;e.addRequireLoadCallback(()=>e.define.apply(null,a))},e.preLoadFile=(...a)=>{e.addRequireLoadCallback(()=>e.preLoadFile.apply(null,a))}};r(),e._insertRequireShim=r,e.InitRequireJs=r=>{e.requireContexts={},e.performance&&null!=e.performance.now&&(requirejs.onResourceLoad=(a,r,i)=>{const l=e.performance.now(),n=e.requireContexts[a.id];if(n){r.id in n.module_callback_times||(n.module_callback_times[r.id]={});const e=n.module_callback_times[r.id];e.loadTime=l,r.url&&(e.url=r.url),r.id&&(e.name=r.id),r.parentMap&&r.parentMap.url&&(e.parent=r.parentMap.url)}}),e.configureRequire=r,e.addRequireLoadCallback=e=>e(),a.forEach(e=>e())}})();

            window.CSP_SCRIPT_NONCE = "AwAFyR8mbB48mik7l2cB";
            </script> <script async="async" crossorigin="anonymous" src="https://cfl.dropboxstatic.com/static/metaserver/static/js/alameda_bundle/alameda_bundle_chrome_de-vflU8rBSF.js" type="text/javascript" nonce="e2lVsGiUH3tX0noOW1W+"></script> <link crossorigin="anonymous" href="https://cfl.dropboxstatic.com/static/metaserver/static/fonts/paper-atlasgrotesk/AtlasGrotesk-Regular-Web-vflk7bxjs.woff2" as="font" rel="preload" type="font/woff2" /><link crossorigin="anonymous" href="https://cfl.dropboxstatic.com/static/metaserver/static/fonts/paper-atlasgrotesk/AtlasGrotesk-Medium-Web-vfl38XiTL.woff2" as="font" rel="preload" type="font/woff2" />  <style>
            * { font-weight: inherit; }
            html { box-sizing: border-box; }
            /* To remove Firefox's extra padding */
            button::-moz-focus-inner,
            input[type='button']::-moz-focus-inner,
            input[type='submit']::-moz-focus-inner,
            input[type='reset']::-moz-focus-inner {
              padding: 0;
              border: 0 none;
            }
            [class^='maestro-sidebar'] { box-sizing: border-box; }
            .maestro body,
            .maestro .normal {
                font-family: AtlasGrotesk, sans-serif;
                font-size: 14px;
                -moz-osx-font-smoothing: grayscale;
                -webkit-font-smoothing: antialiased;
            }
            .maestro input,
            .maestro textarea,
            .maestro select,
            .maestro button:not(.dig-Button, .dig-StylelessButton, .dig-DatePicker-day, .dwg-button2) {
                font-family: AtlasGrotesk, sans-serif;
                -moz-osx-font-smoothing: grayscale;
                -webkit-font-smoothing: antialiased;
            }
            .maestro body {
              margin: 0;
            }
            .embedded-app {
              top: 0;
              bottom: 0;
              padding-left: 240px;
            }
            .embedded-app__error-state {
              display: block;
              text-align: center;
              align-items: center;
              justify-content: center;
              flex-direction: column;
              bottom: 0;
            }
            .embedded-app__error-state img {
                height: 300px;
                width: 300px;
            }
            .maestro-loading-spinner-wrapper {
              position: fixed;
              top: 0;
              right: 0;
              bottom: 0;
              left: 0;
              display: flex;
              justify-content: center;
            }
            .maestro-loading-spinner {
              position: absolute;
              top: 33%;
              width: 24px;
              height: 24px;
              background-image: url('https://cfl.dropboxstatic.com/static/metaserver/static/images/icons/ajax-loading-small-blue@2x-vfl14X6Ll.gif');
              background-size: 24px 24px;
              /* So the center of the image is used to center the element. */
              transform: translate(-50%, -50%);
            }</style> <style type="text/css"></style><script type="text/javascript" nonce="AwAFyR8mbB48mik7l2cB">if (window.performance && window.performance.mark) { window.performance.mark("ensemble_payload_start"); }</script> <script type="text/javascript" nonce="AwAFyR8mbB48mik7l2cB">(function(){"use strict";const PerfTimer="object"==typeof performance&&"function"==typeof performance.now?performance:Date,FAST_FRAME_THRESHOLD=20,SLOW_FRAME_THRESHOLD=34;class CPUIdleMonitor{constructor(){this.idleCPUTime=0,this.busyCPUTime=0,this.startedTracking=PerfTimer.now(),this.lastFrame=this.startedTracking,this.requestID=requestAnimationFrame((()=>{this.updateCPUTimes()})),console.timeStamp&&console.timeStamp("cpu_idle_tracking_started")}updateCPUTimes(e={forceUpdate:!1,currentCPUSpan:0}){const t=PerfTimer.now(),s=t-this.lastFrame;let r;this.lastFrame=t,r=s>=SLOW_FRAME_THRESHOLD?0:s<=FAST_FRAME_THRESHOLD?1:(SLOW_FRAME_THRESHOLD-s)/(SLOW_FRAME_THRESHOLD-FAST_FRAME_THRESHOLD);let n=s*(1-r);e.forceUpdate&&n<e.currentCPUSpan&&(n=Math.min(s,e.currentCPUSpan)),this.busyCPUTime+=n,this.idleCPUTime+=s-n,e.forceUpdate||(this.requestID=requestAnimationFrame((()=>{this.updateCPUTimes()})))}stop(){null!==this.requestID&&(console.timeStamp&&console.timeStamp("cpu_idle_tracking_stopped"),cancelAnimationFrame(this.requestID),this.requestID=null)}getIdleCPUTime(){return this.idleCPUTime}getCPUTimeSnapshot(e){return void 0!==e&&this.updateCPUTimes({forceUpdate:!0,currentCPUSpan:e}),{idleTime:this.idleCPUTime.toString(),busyTime:this.busyCPUTime.toString()}}getTotalTrackedTime(){return this.idleCPUTime+this.busyCPUTime}getIdlePercentOfTracked(){const e=this.idleCPUTime+this.busyCPUTime;return 0===e?0:this.idleCPUTime/e}getUntrackedTimeSinceTTFB(){if("object"!=typeof performance||"function"!=typeof performance.now||"object"!=typeof performance.timing||"number"!=typeof performance.timing.responseStart||"number"!=typeof performance.timing.navigationStart)return null;const e=performance.timing.responseStart-performance.timing.navigationStart;return this.startedTracking-e}}function reportNonceMismatch(e,t){window.addRequireLoadCallback((()=>{setTimeout((()=>{const s=new Error("Refused to execute script from because window.CSP_SCRIPT_NONCE is defined and the nonce doesn't match.");throw s.excExtra={page_nonce:e,script_tag_nonce:t,err_version:3},s.tags=["csp-nonce-error"],s}),0)}))}const hasPerfNow=!(!window.performance||!window.performance.now);function consoleTimeStamp(e){console.timeStamp&&console.timeStamp(e)}class EnsembleStopwatch{constructor(){this._data={}}getNow(){if(hasPerfNow)return window.performance.now()}markSpan(e,t={}){if(consoleTimeStamp(e),"number"!=typeof t.startTime&&(t.startTime=0),"number"!=typeof t.endTime){const e=this.getNow();if(void 0===e)return;t.endTime=e}t.startTime=Math.round(t.startTime),t.endTime=Math.round(t.endTime),this._data[e]?console.error("stopwatch error: spanName has been used before: "+e):this._data[e]={start:t.startTime,end:t.endTime,annotations:t.annotations||{}}}getData(){const e={};for(const t in this._data)if(this._data.hasOwnProperty(t)){const s=this._data[t];e[t]={end:s.end,start:s.start,annotations:s.annotations}}return e}}class EventTracker{constructor(){this._postEventCallbacks=[],this._eventMarked=!1}callAfterEvent(e){this._eventMarked?e():this._postEventCallbacks.push(e)}_triggerPostEventCallbacks(){for(const e of this._postEventCallbacks)e();this._postEventCallbacks=[]}markEvent(){if(this._eventMarked)throw new Error("event can't be marked twice");this._eventMarked=!0,this._triggerPostEventCallbacks()}}const ScriptTypes=["text/javascript","text/ecmascript","application/javascript","application/ecmascript","",void 0];function insertPagelet(e,t){return e.innerHTML=t,t=>_evaluateScripts(e,t)}function evaluateScript(e,t){const s=document.createElement("div");return s.innerHTML=e,_evaluateScripts(s,t)}function _evaluateScripts(e,t){const s=e.getElementsByTagName("script");for(let e=0;e<s.length;e++){const r=s[e];if(-1===ScriptTypes.indexOf(r.type))continue;const n=r.nonce||r.getAttribute("nonce"),o=window.CSP_SCRIPT_NONCE;if(o===n){if(r.src)throw new Error("Do not add scripts with src in the pagelet html, they should instead be loaded via requirejs or as pagelet dependencies");eval.call(window,r.innerHTML)}else t(o,n)}}const loaderOrder=["edison:preloadCss","js:requireCssWithComponent","js:require_css","loadCssWithCache","ensemble","CssEntryPoint","css-modules"],sortedLoaders=["css-modules"];function findInsertPosition(e,t,s){if(s[t].length>0){if(sortedLoaders.includes(t)){const r=s[t];for(let t=0;t<r.length;t++){const{elem:s,path:n}=r[t];if(n>e.path)return[s,t]}}return[s[t][s[t].length-1].elem.nextElementSibling,null]}const r=loaderOrder.indexOf(t);for(let e=r-1;e>=0;e--){const t=s[loaderOrder[e]]||[];if(t.length>0)return[t[t.length-1].elem.nextElementSibling,null]}for(let e=r+1;e<loaderOrder.length;e++){const t=s[loaderOrder[e]]||[];if(t.length>0)return[t[0].elem,null]}return[null,null]}function injectCssElement(e,t,s,r,n){e.elem.setAttribute("data-loader",t),e.elem instanceof HTMLStyleElement&&e.elem.setAttribute("path",e.path);let o=null,i=null;n||([o,i]=findInsertPosition(e,t,s)),null===i?s[t].push(e):s[t].splice(i,0,e),o?r.insertBefore(e.elem,o):r.appendChild(e.elem)}function injectCss(e,t,s=document){const r=s.defaultView;r.__injectCssCache||(r.__injectCssCache={"edison:preloadCss":[],"js:require_css":[],"js:requireCssWithComponent":[],loadCssWithCache:[],ensemble:[],CssEntryPoint:[],"css-modules":[]});const n=r.__injectCssCache;n[t]=n[t]?n[t]:[];const o=sortedLoaders.includes(t);if(!o&&e.length>1){const[r]=findInsertPosition(e[0],t,n),i=s.createDocumentFragment();for(const s of e)injectCssElement(s,t,n,i,!o);null===r?s.head.appendChild(i):s.head.insertBefore(i,r)}else for(const r of e)injectCssElement(r,t,n,s.head,!1)}const _loadedCSS={},_CSSElements={};function appendLinkTags(e,t,s,r){const n=[];for(const e of t){const t=_CSSElements[e];if(t)if(_loadedCSS[e])s();else{const r=t.onload,n=t.onerror;t.onload=()=>{s(),r()},t.onerror=()=>{s({resource:e,type:"stylesheet"}),n()}}else{const t=document.createElement("link");if(t.href=e,t.rel="stylesheet",t.onload=()=>{_loadedCSS[e]=!0,s()},t.onerror=()=>{s({resource:e,type:"stylesheet"})},r)for(const[e,s]of Object.entries(r))0===e.indexOf("data-")&&t.setAttribute(e,s);n.push({elem:t,path:e}),_CSSElements[e]=t}}injectCss(n,"ensemble",e)}function appendScriptTags(e,t,s,r){let n;window.hasOwnProperty("_csp_external_script_nonce")&&(n=window._csp_external_script_nonce);for(const o of t){const t=document.createElement("script");if(t.src=o,t.type="text/javascript",t.async=!0,t.onload=()=>{s()},t.onerror=()=>{s({resource:o,type:"script"})},n&&t.setAttribute("nonce",n),r)for(const[e,s]of Object.entries(r))0===e.indexOf("data-")&&t.setAttribute(e,s);e.appendChild(t)}}class ResourceLoader{constructor(e,t){this.totalResources=0,this.loadedResources=0,this.onLoadCallbacks=[],this.errors=[],e.stylesheets&&(this.totalResources+=e.stylesheets.length),e.scripts&&(this.totalResources+=e.scripts.length),t&&this.onLoadCallbacks.push(t),0!==this.totalResources?this.loadResources(e.stylesheets,e.scripts,e.dataAttributes):setTimeout(this.runCallbacks.bind(this),0)}isDoneLoading(){return this.loadedResources===this.totalResources}addOnLoadCallback(e){if(this.isDoneLoading())throw new Error("ResourceLoader error: added callback after resources have finished loading");this.onLoadCallbacks.push(e)}loadResources(e,t,s){const r=function(e){this.loadedResources+=1,e&&this.errors.push(e),this.loadedResources===this.totalResources&&this.runCallbacks()}.bind(this);if(e&&appendLinkTags(document,e,r,s),t){const e=document.createDocumentFragment();appendScriptTags(e,t,r,s),document.body.appendChild(e)}}runCallbacks(){let e;if(0!==this.errors.length){e={failedStylesheets:[],failedScripts:[]};for(const t of this.errors)"stylesheet"===t.type?e.failedStylesheets.push(t.resource):"script"===t.type&&e.failedScripts.push(t.resource)}for(let t=0;t<this.onLoadCallbacks.length;t++)this.onLoadCallbacks[t](e)}}function doFrameBust(e){if(e.mini_frame_bust){let e=!1;try{e=top.location.hostname===self.location.hostname}catch(e){}if(self!==top&&!e){setTimeout((()=>{window.DB_FRAME_BUST=!0,document.body.innerHTML="<img src='https://cfl.dropboxstatic.com/static/metaserver/static/images/logo.png' id='frame-bust-image'/>",document.getElementById("frame-bust-image").addEventListener("click",(function(e){top.location.href=window.location.href}))}),4);try{top.location.replace(self.location.href)}catch(e){console.error(e)}}}e.frame_bust&&self===top&&(document.body.style.display="")}class TTITracker{constructor(){this._postTTICallbacks=[],this.ttiMarked=!1}callAfterTTI(e){this.ttiMarked?e():this._postTTICallbacks.push(e)}_triggerPostTTICallbacks(){for(const e of this._postTTICallbacks)e();this._postTTICallbacks=[]}markTTI(){clearTimeout(this.ttiTimeoutId),setTimeout((()=>{this.ttiMarked=!0,this._triggerPostTTICallbacks();const e=document.createEvent("Event");e.initEvent("TTI",!0,!0),window.dispatchEvent(e)}),0)}startTTITimeout(e,t){this.ttiTimeoutId=setTimeout((()=>{t&&t(),this._triggerPostTTICallbacks()}),e)}}function validateObjectProperties(e,t,s){for(const r of Object.keys(s)){if(!Object.prototype.hasOwnProperty.call(t,r))throw new Error(e+" missing required property '"+r+"'");let n,o=!1;const i=s[r];if(null!==i)if("object"==typeof i?(n=i.kind,o=i.nullable):n=i,o){if(null!=t[r]&&typeof t[r]!==n)throw new Error(e+" property '"+r+"' has incorrect type. Expected '"+n+"' or null, got '"+typeof t[r]+"'")}else{const s=typeof t[r];if(s!==n)throw new Error(e+" property '"+r+"' has incorrect type. Expected '"+n+"', got '"+s+"'")}}}function validatePageletConfig(e){if(null==e)throw new Error("Pagelet config is null or undefined");if("object"!=typeof e)throw new Error("Pagelet config is not an object");switch(validateObjectProperties("Pagelet config",e,{name:"string",driver:"string"}),e.driver){case"simple":_validateSimplePageletConfig(e);break;case"requirejs":case"js_only":_validateRequireJSPageletConfig(e);break;case"inline":_validateInlinePageletConfig(e);break;default:throw new Error("Unknown pagelet config driver '"+e.driver+"'")}return e}function _validateSimplePageletConfig(e){if(validateObjectProperties("Pagelet config",e,{html:"string",script:{kind:"string",nullable:!0},stylesheets:null}),!Array.isArray(e.stylesheets))throw new Error("Pagelet config property 'stylesheets' has incorrect type. Expected 'Array' or null, got '"+typeof e.stylesheets+"'");for(const t of e.stylesheets)if("string"!=typeof t)throw new Error("Pagelet config property 'stylesheets' has an element of incorrect type. Expected 'string', got '"+typeof t+"'")}function _validateRequireJSPageletConfig(e){if(validateObjectProperties("Pagelet config",e,{html:"string",stylesheets:null}),!Array.isArray(e.stylesheets))throw new Error("Pagelet config property 'stylesheets' has incorrect type. Expected 'Array' or null, got '"+typeof e.stylesheets+"'");for(const t of e.stylesheets)if("string"!=typeof t)throw new Error("Pagelet config property 'stylesheets' has an element of incorrect type. Expected 'string', got '"+typeof t+"'")}function _validateInlinePageletConfig(e){validateObjectProperties("Pagelet config",e,{html:"string",style:{kind:"string",nullable:!0},script:{kind:"string",nullable:!0}})}function validateUsers(e){if(!Array.isArray(e))throw new Error("users must be an array");for(let t=0;t<e.length;t++){_validateUser(e[t])}}function _validateUser(e){if(validateObjectProperties("User",e,{userId:"number",displayName:"string",personalName:{kind:"string",nullable:!0},isActive:"boolean",isTeam:"boolean",teamName:{kind:"string",nullable:!0},teamSize:"number",redirectUrl:{kind:"string",nullable:!0},role:"string"}),-1!==e.userId&&!e.isTeam&&null==e.personalName)throw new Error("Non-team user must have 'personalName' set");if(e.isTeam&&null==e.teamName)throw new Error("Team user must have 'teamName' set");if(e.isTeam&&-1===e.teamSize)throw new Error("Team user must have 'teamSize' set");if(-1===["work","personal"].indexOf(e.role))throw new Error(`role ${e.role} is not recognized`);if(-1===e.userId&&null==e.redirectUrl||-1!==e.userId&&null!=e.redirectUrl)throw new Error("User property 'redirectUrl' must be set if and only if the user is not paired")}class Viewer{constructor(e){if(!e.users)throw new Error("Viewer config must contain users. Config: "+JSON.stringify(e));validateUsers(e.users),this.users=e.users}getActiveUser(){for(let e=0;e<this.users.length;e++)if(this.users[e].isActive)return this.users[e];return null}getUserById(e){for(let t=0;t<this.users.length;t++){const s=this.users[t];if(s.userId===e)return s}throw new Error(`user ${e} is not in the current viewer`)}isValidRole(e){return-1!==["personal","work"].indexOf(e)}}let started=!1;function startVisibilityWatcher(){if(!started&&window.performance&&window.performance.mark){started=!0;const e=()=>{const e=document.visibilityState;e&&window.performance.mark(`VisibilityState.${e}`)};e(),document&&document.addEventListener&&document.addEventListener("visibilitychange",e,!1)}}const cpuIdleMonitor=new CPUIdleMonitor;startVisibilityWatcher();const CLIENT_HANDLED_QUERY_PARAMS={role:!0,email_just_verified:!0,email_just_verified_and_changed:!0,oref:!0,always_show_progressbar:!0,from_scl_sync_modal:!0};let jsStopwatch;function registerEnsembleStopwatch(){jsStopwatch=new EnsembleStopwatch}class Pagelet{constructor(e,t){this.name=e.name,this.driver=e.driver,this.exceptionInfo=t}}class SimplePagelet extends Pagelet{constructor(e,t){super(e,t),this.html=e.html,this.script=e.script,this.stylesheets=e.stylesheets}initializeLoad(e,t,s,r){const n=()=>{this.renderHtml(e),t?s.callAfterTTI((()=>this.loadScript())):this.loadScript(),r()};this.stylesheets&&this.stylesheets.length>0?new ResourceLoader({stylesheets:this.stylesheets},n):n()}renderHtml(e){const t=document.getElementById(e);if(!t)throw new Error("Unable to find pagelet targetElementId '"+e+"'");t.innerHTML=this.html}loadScript(){null!=this.script&&globalEval(this.script)}getDOMInteractive(){throw new Error("SimplePagelet does not track DOMInteractive")}}function globalEval(script){eval(script)}class RequireJSPagelet extends Pagelet{constructor(e,t,s){super(e,t),this.html=e.html,this.stylesheets=e.stylesheets,this._ensemble=s}insertIntoDOM(e,t,s){const r=document.getElementById(e);r.style.visibility="hidden",r.style.position="absolute";const n=insertPagelet(r,this.html);t?s.callAfterTTI((()=>n(reportNonceMismatch))):n(reportNonceMismatch),jsStopwatch.markSpan("dws_pagelet_render_on_page_"+e),jsStopwatch.markSpan("dws_pagelet_render_on_page_"+this.name),jsStopwatch.markSpan("dws_pagelet_render_on_page_uncached_"+this.name)}_showPageletElement(e){const t=document.getElementById(e);t.style.position="",t.style.visibility="visible"}initializeLoad(e,t,s,r){jsStopwatch.markSpan("dws_start_initialize_load_uncached_"+this.name),jsStopwatch.markSpan("dws_pagelet_payload_available_"+e),this.insertIntoDOM(e,t,s),this._domInteractive=(new Date).getTime(),console.timeStamp&&console.timeStamp("DOMInteractive"),"embedded-app"===e&&(this._ensemble.waitingForCss=!0),new ResourceLoader({stylesheets:this.stylesheets},(()=>{this._showPageletElement(e),"embedded-app"===e&&(this._ensemble.waitingForCss=!1,this._ensemble.mark_tti_callback()),jsStopwatch.markSpan("dws_pagelet_css_loaded_"+e),jsStopwatch.markSpan("dws_pagelet_load_stylesheet_"+this.name),jsStopwatch.markSpan("dws_pagelet_load_stylesheet_uncached_"+this.name),r()}))}getDOMInteractive(){if(!this._domInteractive)throw new Error("DOMInteractive has not been logged");return this._domInteractive}}class JSOnlyPagelet extends RequireJSPagelet{constructor(e,t,s){super(Object.assign(Object.assign({},e),{driver:"requirejs",html:""}),t,s)}_showPageletElement(e){}insertIntoDOM(e){jsStopwatch.markSpan("dws_pagelet_render_on_page_"+e),jsStopwatch.markSpan("dws_pagelet_render_on_page_"+this.name),jsStopwatch.markSpan("dws_pagelet_render_on_page_uncached_"+this.name)}}function removeServiceWorker(){navigator.serviceWorker&&navigator.serviceWorker.getRegistration().then((function(e){e&&e.unregister()}))}class Ensemble{constructor(){this.bufferedEventEmitter=null,this.globalHeaderEventEmitter=null,this.eventEmitter=null,this.ttiTracker=new TTITracker,this.ttiMarked=!1,this.ttiTracker.callAfterTTI((()=>this.ttiMarked=!0)),this.pageletsByElemId={},this.waitingForCss=!1,this.mark_tti_callback=()=>{},this.constModules={},this.constModuleCallbacks={},this._placeholderLoadedTrackerByElemId={},this.exceptionInfo=null,registerEnsembleStopwatch(),jsStopwatch.markSpan("dws_ensemble_constructor")}init(e){const t=jsStopwatch.getNow();if(jsStopwatch.markSpan("dws_ensemble_begin_init"),!e)throw new Error("Missing ensemble configuration");if(!e.viewerData)throw new Error("Missing viewer data needed to initialize the Ajax calls afterwards");if(!e.jsCsrfCookieName)throw new Error("Missing jsCsrfCookieName info for CSRF cookie");if(!e.frameProtection)throw new Error("Missing frameProtection");if(!e.errorStrings)throw new Error("Missing errorStrings");if(!e.dwsPageName)throw new Error("Missing dwsPageName");if(!e.exceptionInfo)throw new Error("Missing exceptionInfo");if(doFrameBust(e.frameProtection),!e.ttiTimeoutMS)throw new Error("Missing ttiTimeoutMS needed to ensure post-TTI pagelets always load");this.ttiTracker.startTTITimeout(e.ttiTimeoutMS,(()=>jsStopwatch.markSpan("dws_tti_timeout_expired"))),jsStopwatch.markSpan("dws_tti_timeout_started"),this.viewer=new Viewer(e.viewerData),this.jsCsrfCookieName=e.jsCsrfCookieName,this._embeddedAppPagelet=null,this.errorStrings=e.errorStrings,this.dwsPageName=e.dwsPageName,this.exceptionInfo=e.exceptionInfo,this.lazyLoadJQuery=e.lazyLoadJQuery;try{this.switchedAccounts=!!sessionStorage.getItem("Ensemble.switchedAccounts"),sessionStorage.removeItem("Ensemble.switchedAccounts")}catch(e){console.error(e),this.switchedAccounts=!1}removeServiceWorker(),this.prefetchedResourcesLoader=new ResourceLoader({stylesheets:e.prefetchResources.stylesheets,scripts:e.prefetchResources.scripts}),window.addRequireLoadCallback((()=>{if(window.requireContexts.externals){const e=this.lazyLoadJQuery?["react","react-dom"]:["jquery","react","react-dom"];window.requireContexts.externals.require(e,(()=>{jsStopwatch.markSpan("dws_core_externals_loaded")}))}}));const s=jsStopwatch.getNow(),r=cpuIdleMonitor.getCPUTimeSnapshot(s&&t?s-t:void 0);jsStopwatch.markSpan("dws_ensemble_init",{annotations:r})}getPageName(){return this.dwsPageName}getExceptionInfo(){return this.exceptionInfo}markTTI(){this.ttiTracker.markTTI()}stopwatchPagelet(e,t){const s=cpuIdleMonitor.getCPUTimeSnapshot(),r="dws_"+e+"_"+t;console.timeStamp&&console.timeStamp(r),jsStopwatch.markSpan(r,{annotations:s})}insertAfterTTI(e){this.ttiTracker.callAfterTTI((()=>evaluateScript(e,reportNonceMismatch)))}snapshotTimingProfile(){cpuIdleMonitor.stop();const e={idleCPUTime:cpuIdleMonitor.getIdleCPUTime(),totalTrackedCPUTime:cpuIdleMonitor.getTotalTrackedTime()},t=cpuIdleMonitor.getUntrackedTimeSinceTTFB();return t&&(e.untrackedTimeAfterFirstByte=t),e}showError(e){document.body.innerHTML='\n      <link href="https://cfl.dropboxstatic.com{\'/static/metaserver/static/css/font_paper_atlas_grotesk.css\'}" rel="stylesheet">\n    ';const t=document.createElement("div");t.id="dws-error",t.innerHTML=`\n      <div class="embedded-app__error-state">\n        <img alt="" src="https://assets.dropbox.com/www/en-us/illustrations/spot/target-miss.svg" />\n        <p>${this.errorStrings.sorryForTheHiccup}</p>\n        <p>\n          <a class="reload-link" href="#">\n            ${this.errorStrings.tryRefreshingYourPage}\n          </a>\n        </p>\n        <span id="debug_info"></span>\n      </div>\n    `,document.body.appendChild(t);const s=document.querySelectorAll(".embedded-app__error-state .reload-link");for(let e=0;e<s.length;e++)s[e].addEventListener("click",(()=>window.location.reload()))}setupPlaceholder(e,t,s,r,n,o,i){if(!this.prefetchedResourcesLoader.isDoneLoading())return void this.prefetchedResourcesLoader.addOnLoadCallback((()=>{this.setupPlaceholder(e,t,s,r,n,o,i)}));const a=new EventTracker;this._placeholderLoadedTrackerByElemId[s]=a,this._setupPagelet(e,t,!1,(()=>{}),(()=>a.markEvent()),r,n,o,i)}setupPagelet(e,t,s,r,n,o,i,a,l){if(!this.prefetchedResourcesLoader.isDoneLoading())return void this.prefetchedResourcesLoader.addOnLoadCallback((()=>{this.setupPagelet(e,t,s,r,n,o,i,a)}));const c=()=>{this._setupPagelet(e,t,s,r,(()=>null==l?void 0:l()),n,o,i,a)},d=this._placeholderLoadedTrackerByElemId[e];null!=d?d.callAfterEvent(c):c()}_setupPagelet(e,t,s,r,n,o,i,a,l){const c=validatePageletConfig(t);jsStopwatch.markSpan("dws_before_internal_setup_pagelet_uncached_"+c.name);const d={pagelet_client_load_time:(new Date).getTime()/1e3,pagelet_element_id:e,pagelet_name:t.name,repo_rev:o,served_by_hostname:i,yaps_project:a,yaps_deployment:l};let h;switch(t.driver){case"requirejs":h=new RequireJSPagelet(t,d,this);break;case"js_only":h=new JSOnlyPagelet(t,d,this);break;case"simple":h=new SimplePagelet(t,d);break;default:throw new Error(`unrecognized driver ${t.driver}`)}this.pageletsByElemId[e]=h,"embedded-app"===e&&(this._embeddedAppPagelet=h),h.initializeLoad(e,s,this.ttiTracker,n),r&&(s?this.ttiTracker.callAfterTTI(r):r())}loadCSS(e,t){new ResourceLoader({stylesheets:e,dataAttributes:t?{"data-pagelet":t}:void 0})}getEmbeddedAppDOMInteractive(){if(!this._embeddedAppPagelet)throw new Error("Cannot get DOMInteractive, embedded app is not initialized");return this._embeddedAppPagelet.getDOMInteractive()}getPageletInfoForExceptionReporting(){const e=[];for(const t in this.pageletsByElemId)this.pageletsByElemId.hasOwnProperty(t)&&e.push(this.pageletsByElemId[t].exceptionInfo);return e}requestConstModule(e,t,s){this.constModules[t]||(this.constModules[t]={}),this.constModuleCallbacks[t]||(this.constModuleCallbacks[t]={}),e in this.constModules[t]?s(this.constModules[t][e]):(this.constModuleCallbacks[t][e]||(this.constModuleCallbacks[t][e]=[]),this.constModuleCallbacks[t][e].push(s))}defineConstModule(e,t,s){if(this.constModules[t]||(this.constModules[t]={}),e in this.constModules[t])return;this.constModules[t][e]=s;const r=this.constModuleCallbacks[t]&&this.constModuleCallbacks[t][e];if(r){for(const e of r)e(s);this.constModuleCallbacks[t][e]=[]}}processChunk(e,t,s){const r=window.performance&&window.location.search.indexOf("show_debug_spans")>-1;r&&window.performance.mark(`${e} ${t} processChunk start`);const n=jsStopwatch.getNow();s();const o=jsStopwatch.getNow();n&&o&&(cpuIdleMonitor.updateCPUTimes({forceUpdate:!0,currentCPUSpan:o-n}),jsStopwatch.markSpan(`dws-processChunk-${e}-${t}`,{startTime:n,endTime:o,annotations:cpuIdleMonitor.getCPUTimeSnapshot(o-n)})),r&&(window.performance.mark(`${e} ${t} processChunk end`),window.performance.measure(`${e} ${t} processChunk`,`${e} ${t} processChunk start`,`${e} ${t} processChunk end`))}preLoadJs(e,t){window.preLoadFile&&window.preLoadFile(e)}_hasOnlyClientHandledQueryParams(e){const t=e.split("&");for(const e of t){if(!(e.split("=")[0]in CLIENT_HANDLED_QUERY_PARAMS))return!1}return!0}_getCookieValue(e){const t=document.cookie.match("(^|; )"+e+"=([^;]*)");return t?t[2]:""}getCsrfToken(){return this._getCookieValue(this.jsCsrfCookieName)}getJSStopwatchData(){const e=jsStopwatch.getData();return window.timingCraftPrefetchStart&&(e.craft_fast_prefetch_start={end:window.timingCraftPrefetchStart,start:0,annotations:{}}),window.timingCraftPrefetchDone&&(e.craft_fast_prefetch_done={end:window.timingCraftPrefetchDone,start:0,annotations:{}}),e}}window.ensemble=new Ensemble})();
</script>  </head><body><script type="text/javascript" nonce="AwAFyR8mbB48mik7l2cB">if (window.performance && window.performance.mark) { window.performance.mark("body_start"); }</script> <div id="pagelet-0"></div><div id="pagelet-1"></div><div id="pagelet-2"></div><div id="pagelet-3"></div><div id="pagelet-4"></div>  <script type="text/javascript" nonce="AwAFyR8mbB48mik7l2cB"> addRequireLoadCallback(function(){
define("metaserver/static/js/modules/constants/page_load", [], function() {
            return {"COUNTRY_OVERRIDE": false, "PUBLIC_MODE_OVERRIDE": null, "REPO_REV": "e27313f4c53a40bd60f54babd8daa5ade9ced7bc", "HOSTNAME": "atlas-dropins-live-prod-pdx-564b7c88cb-s6s6d", "YAPS_DEPLOYMENT": "prod-pdx", "YAPS_PROJECT": "atlasservlet.dropins-live", "PAGE_LOCALE": "de", "SESSION_ID": "148131182027354817762016026028562153939", "IS_SELENIUM_TEST": false, "__esModule": true};
        });
        define("metaserver/static/js/modules/constants/request", [], function() {
                var o = {"LOGGED_OUT_X_DROPBOX_UID": -1, "IS_HTTP2": true, "PAGE_LOAD_TIME": 1704061203, "REQUEST_ID": "ed3a2f982fbc44ee85d2e8dff6a516e7", "REQUEST_START_TIME": 1704061203400, "REQUEST_TRACING_ENABLED": false, "HTTP3_SUPPORT_ENABLED": false, "__esModule": true};
                /* global: ensemble is global for maestro pages */
                if (window.ensemble && window.ensemble.getRequestId) {
                    o.REQUEST_ID = ensemble.getRequestId();
                }
                return o;
            });

/* global: require */
require.config({context: "externals"})(["metaserver/static/js/modules/constants/page_load"]);
});
</script><script type="text/javascript" nonce="AwAFyR8mbB48mik7l2cB">
            /* global: configureRequire comes from the
               fake_require_snippet (ui/page/script_tags.py) */
            configureRequire({"baseUrl": "https://cfl.dropboxstatic.com/", "bundles": {"pkg-core": ["js/browser/browser_detection"], "pkg-exception-reporting": ["js/browser/cookies", "js/common/exception_tag_registry", "metaserver/static/js/clean/csrf", "metaserver/static/js/core/assert", "metaserver/static/js/core/exception", "metaserver/static/js/core/exception_info", "metaserver/static/js/core/tracekit", "metaserver/static/js/core/xhr", "metaserver/static/prod_assets_web_modules/tracekit"], "pkg-api_v2": ["metaserver/static/js/api_v2/client_base", "metaserver/static/js/api_v2/error", "metaserver/static/js/api_v2/noauth_client", "metaserver/static/js/api_v2/transport/fetch", "metaserver/static/js/api_v2/types", "metaserver/static/js/core/transport/fetch_utils"], "pkg-growth_features": ["metaserver/static/js/clean/server_side_client_view_bridge"], "pkg-api_v2-extra": ["metaserver/static/js/core/attribution_header", "metaserver/static/prod_assets_web_modules/eventemitter3"], "pkg-core-url-and-css": ["metaserver/static/js/core/uri"], "pkg-timing": ["metaserver/static/js/metrics/index", "metaserver/static/js/metrics/server_view_sink", "metaserver/static/js/metrics/unload", "metaserver/static/js/uuid/insecure_uuid", "typescript/dropbox/proto/apex_metrics_web/apex_metrics_web_pb", "typescript/libraries/shared/apex-metrics/src/clock", "typescript/libraries/shared/apex-metrics/src/executor", "typescript/libraries/shared/apex-metrics/src/hyperloglog", "typescript/libraries/shared/apex-metrics/src/index", "typescript/libraries/shared/apex-metrics/src/instant", "typescript/libraries/shared/apex-metrics/src/internal", "typescript/libraries/shared/apex-metrics/src/metrics", "typescript/libraries/shared/apex-metrics/src/metrics_reporter", "typescript/libraries/shared/apex-metrics/src/murmur", "typescript/libraries/shared/apex-metrics/src/no_op", "typescript/libraries/shared/apex-metrics/src/sink/apiv2_sink", "typescript/libraries/shared/apex-metrics/src/sink/coin", "typescript/libraries/shared/apex-metrics/src/sink/database", "typescript/libraries/shared/apex-metrics/src/sink/filter", "typescript/libraries/shared/apex-metrics/src/sink/index", "typescript/libraries/shared/apex-metrics/src/sink/instrumentation", "typescript/libraries/shared/apex-metrics/src/sink/platform", "typescript/libraries/shared/apex-metrics/src/sink/serialization", "typescript/libraries/shared/apex-metrics/src/types", "typescript/libraries/shared/apex-metrics/src/validate"], "pkg-timing-helpers": ["metaserver/static/js/user_centric_perf_metrics/component_visually_complete/ajax", "metaserver/static/js/user_centric_perf_metrics/component_visually_complete/constants", "metaserver/static/js/user_centric_perf_metrics/component_visually_complete/network_idle_observable", "metaserver/static/prod_assets_web_modules/@dropbox/ttvc"], "pkg-misc2": ["metaserver/static/prod_assets_web_modules/@bufbuild/protobuf", "metaserver/static/prod_assets_web_modules/common/any_pb"], "pkg-external": ["metaserver/static/prod_assets_web_modules/common/_commonjsHelpers", "metaserver/static/prod_assets_web_modules/tslib"], "pkg-react": ["metaserver/static/prod_assets_web_modules/react", "metaserver/static/prod_assets_web_modules/react-dom"]}, "context": "externals", "map": {"*": {"metaserver/static/js/reactserver_stubs/__unstubbed_purify": "metaserver/static/prod_assets_web_modules/dompurify", "metaserver/static/js/modules/core/langpack": "json_loader!js/langpack/icu-de.json", "@adyen/adyen-web": "metaserver/static/prod_assets_web_modules/@adyen/adyen-web", "@bufbuild/connect-web": "metaserver/static/prod_assets_web_modules/@bufbuild/connect-web", "@bufbuild/protobuf": "metaserver/static/prod_assets_web_modules/@bufbuild/protobuf", "@dropbox/api-v2-client": "metaserver/static/prod_assets_web_modules/@dropbox/api-v2-client", "@dropbox/dig-components/accordion": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/accordion", "@dropbox/dig-components/aspect_ratio": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/aspect_ratio", "@dropbox/dig-components/avatar": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/avatar", "@dropbox/dig-components/badge": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/badge", "@dropbox/dig-components/badges": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/badges", "@dropbox/dig-components/banner": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/banner", "@dropbox/dig-components/breadcrumb": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/breadcrumb", "@dropbox/dig-components/buttons": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/buttons", "@dropbox/dig-components/card": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/card", "@dropbox/dig-components/carousel": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/carousel", "@dropbox/dig-components/chip": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/chip", "@dropbox/dig-components/chips": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/chips", "@dropbox/dig-components/click_outside": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/click_outside", "@dropbox/dig-components/combinations": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/combinations", "@dropbox/dig-components/controls": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/controls", "@dropbox/dig-components/date_picker": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/date_picker", "@dropbox/dig-components/drawer": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/drawer", "@dropbox/dig-components/dropzone": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/dropzone", "@dropbox/dig-components/form_row": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/form_row", "@dropbox/dig-components/global_header": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/global_header", "@dropbox/dig-components/hooks": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/hooks", "@dropbox/dig-components/jest_after_env_setup": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/jest_after_env_setup", "@dropbox/dig-components/layer": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/layer", "@dropbox/dig-components/list": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/list", "@dropbox/dig-components/menu": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/menu", "@dropbox/dig-components/modal": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/modal", "@dropbox/dig-components/motion": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/motion", "@dropbox/dig-components/overlay": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/overlay", "@dropbox/dig-components/progress_indicators": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/progress_indicators", "@dropbox/dig-components/skeleton": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/skeleton", "@dropbox/dig-components/slider": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/slider", "@dropbox/dig-components/snackbar": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/snackbar", "@dropbox/dig-components/stepper": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/stepper", "@dropbox/dig-components/table": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/table", "@dropbox/dig-components/tabs": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/tabs", "@dropbox/dig-components/text_fields": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/text_fields", "@dropbox/dig-components/tooltips": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/tooltips", "@dropbox/dig-components/truncate": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/truncate", "@dropbox/dig-components/typeahead": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/typeahead", "@dropbox/dig-components/typography": "metaserver/static/prod_assets_web_modules/@dropbox/dig-components/typography", "@dropbox/dig-content-icons": "metaserver/static/prod_assets_web_modules/@dropbox/dig-content-icons", "@dropbox/dig-foundations": "metaserver/static/prod_assets_web_modules/@dropbox/dig-foundations", "@dropbox/dig-icons": "metaserver/static/prod_assets_web_modules/@dropbox/dig-icons", "@dropbox/dig-icons/assets": "metaserver/static/prod_assets_web_modules/@dropbox/dig-icons/assets", "@dropbox/dig-illustrations": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations", "@dropbox/dig-illustrations/hero/apple-picking": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/apple-picking", "@dropbox/dig-illustrations/hero/archeologist-dig": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/archeologist-dig", "@dropbox/dig-illustrations/hero/artist-painter": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/artist-painter", "@dropbox/dig-illustrations/hero/assess-with-purpose": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/assess-with-purpose", "@dropbox/dig-illustrations/hero/balance-woman": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/balance-woman", "@dropbox/dig-illustrations/hero/baton-pass": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/baton-pass", "@dropbox/dig-illustrations/hero/bike-courier": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/bike-courier", "@dropbox/dig-illustrations/hero/bike-shop": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/bike-shop", "@dropbox/dig-illustrations/hero/bird-perch": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/bird-perch", "@dropbox/dig-illustrations/hero/birthday-picture-family": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/birthday-picture-family", "@dropbox/dig-illustrations/hero/bowl-empty": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/bowl-empty", "@dropbox/dig-illustrations/hero/bridge": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/bridge", "@dropbox/dig-illustrations/hero/browsing-supermarket": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/browsing-supermarket", "@dropbox/dig-illustrations/hero/checking-workload": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/checking-workload", "@dropbox/dig-illustrations/hero/checklist-nursery": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/checklist-nursery", "@dropbox/dig-illustrations/hero/coffee-shop": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/coffee-shop", "@dropbox/dig-illustrations/hero/collaboration-remote": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/collaboration-remote", "@dropbox/dig-illustrations/hero/collaboration-review": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/collaboration-review", "@dropbox/dig-illustrations/hero/community-garden": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/community-garden", "@dropbox/dig-illustrations/hero/conference-call": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/conference-call", "@dropbox/dig-illustrations/hero/construction-planning": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/construction-planning", "@dropbox/dig-illustrations/hero/coupon": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/coupon", "@dropbox/dig-illustrations/hero/courtroom": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/courtroom", "@dropbox/dig-illustrations/hero/crystal-ball": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/crystal-ball", "@dropbox/dig-illustrations/hero/deliver-boxes": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/deliver-boxes", "@dropbox/dig-illustrations/hero/delivery-truck": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/delivery-truck", "@dropbox/dig-illustrations/hero/desk-laptop": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/desk-laptop", "@dropbox/dig-illustrations/hero/desk-notebook": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/desk-notebook", "@dropbox/dig-illustrations/hero/developer-desk-1": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/developer-desk-1", "@dropbox/dig-illustrations/hero/developer-desk-2": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/developer-desk-2", "@dropbox/dig-illustrations/hero/developer-esignature": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/developer-esignature", "@dropbox/dig-illustrations/hero/developer-esignature-2": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/developer-esignature-2", "@dropbox/dig-illustrations/hero/developer-esignature-3": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/developer-esignature-3", "@dropbox/dig-illustrations/hero/device": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/device", "@dropbox/dig-illustrations/hero/device-home-office": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/device-home-office", "@dropbox/dig-illustrations/hero/device-install": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/device-install", "@dropbox/dig-illustrations/hero/devices-couch": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/devices-couch", "@dropbox/dig-illustrations/hero/dia-de-muertos": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/dia-de-muertos", "@dropbox/dig-illustrations/hero/diwali": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/diwali", "@dropbox/dig-illustrations/hero/document-pile": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/document-pile", "@dropbox/dig-illustrations/hero/dropbox-delivers": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/dropbox-delivers", "@dropbox/dig-illustrations/hero/esignature-laptop": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/esignature-laptop", "@dropbox/dig-illustrations/hero/esignature-template": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/esignature-template", "@dropbox/dig-illustrations/hero/family-gathering": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/family-gathering", "@dropbox/dig-illustrations/hero/fingerprint-scanner": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/fingerprint-scanner", "@dropbox/dig-illustrations/hero/fleet-of-ships": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/fleet-of-ships", "@dropbox/dig-illustrations/hero/group-huddle": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/group-huddle", "@dropbox/dig-illustrations/hero/handshake-interview": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/handshake-interview", "@dropbox/dig-illustrations/hero/healthcare-doctor": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/healthcare-doctor", "@dropbox/dig-illustrations/hero/healthcare-therapist": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/healthcare-therapist", "@dropbox/dig-illustrations/hero/home-meditation": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/home-meditation", "@dropbox/dig-illustrations/hero/home-office": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/home-office", "@dropbox/dig-illustrations/hero/hospital-reception": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/hospital-reception", "@dropbox/dig-illustrations/hero/house-large": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/house-large", "@dropbox/dig-illustrations/hero/house-painting": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/house-painting", "@dropbox/dig-illustrations/hero/hr-virtual": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/hr-virtual", "@dropbox/dig-illustrations/hero/insurance-agent": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/insurance-agent", "@dropbox/dig-illustrations/hero/insurance-agent-desk": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/insurance-agent-desk", "@dropbox/dig-illustrations/hero/interview-lineup": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/interview-lineup", "@dropbox/dig-illustrations/hero/invest-in-success": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/invest-in-success", "@dropbox/dig-illustrations/hero/ipad-esignature": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/ipad-esignature", "@dropbox/dig-illustrations/hero/learn-to-unlearn": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/learn-to-unlearn", "@dropbox/dig-illustrations/hero/logging-in": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/logging-in", "@dropbox/dig-illustrations/hero/mapping-out-the-forest": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/mapping-out-the-forest", "@dropbox/dig-illustrations/hero/moving-boxes": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/moving-boxes", "@dropbox/dig-illustrations/hero/ocean-cargo-ship": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/ocean-cargo-ship", "@dropbox/dig-illustrations/hero/office-fax": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/office-fax", "@dropbox/dig-illustrations/hero/office-light-off": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/office-light-off", "@dropbox/dig-illustrations/hero/on-demand-business": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/on-demand-business", "@dropbox/dig-illustrations/hero/on-demand-warehouse": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/on-demand-warehouse", "@dropbox/dig-illustrations/hero/open-package": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/open-package", "@dropbox/dig-illustrations/hero/orchestra": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/orchestra", "@dropbox/dig-illustrations/hero/outdoor-signing": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/outdoor-signing", "@dropbox/dig-illustrations/hero/overflowing-file-cabinet": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/overflowing-file-cabinet", "@dropbox/dig-illustrations/hero/peaceful-gardening": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/peaceful-gardening", "@dropbox/dig-illustrations/hero/phone-picture-family": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/phone-picture-family", "@dropbox/dig-illustrations/hero/phone-picture-friends": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/phone-picture-friends", "@dropbox/dig-illustrations/hero/procurement-shipping-container": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/procurement-shipping-container", "@dropbox/dig-illustrations/hero/procurement-small-business": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/procurement-small-business", "@dropbox/dig-illustrations/hero/real-estate-buyer": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/real-estate-buyer", "@dropbox/dig-illustrations/hero/real-estate-sign": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/real-estate-sign", "@dropbox/dig-illustrations/hero/realtor": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/realtor", "@dropbox/dig-illustrations/hero/receive-fax": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/receive-fax", "@dropbox/dig-illustrations/hero/relaxed-working-from-home": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/relaxed-working-from-home", "@dropbox/dig-illustrations/hero/remote-outside-working": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/remote-outside-working", "@dropbox/dig-illustrations/hero/remote-work": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/remote-work", "@dropbox/dig-illustrations/hero/roadblock": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/roadblock", "@dropbox/dig-illustrations/hero/scan": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/scan", "@dropbox/dig-illustrations/hero/security-archive": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/security-archive", "@dropbox/dig-illustrations/hero/security-camera-weather": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/security-camera-weather", "@dropbox/dig-illustrations/hero/security-display-case": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/security-display-case", "@dropbox/dig-illustrations/hero/send-receive-fax": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/send-receive-fax", "@dropbox/dig-illustrations/hero/share": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/share", "@dropbox/dig-illustrations/hero/share-idea": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/share-idea", "@dropbox/dig-illustrations/hero/sharing-box": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/sharing-box", "@dropbox/dig-illustrations/hero/ship": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/ship", "@dropbox/dig-illustrations/hero/shipyard": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/shipyard", "@dropbox/dig-illustrations/hero/side-mirror-view": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/side-mirror-view", "@dropbox/dig-illustrations/hero/sign": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/sign", "@dropbox/dig-illustrations/hero/signature-desktop": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/signature-desktop", "@dropbox/dig-illustrations/hero/signature-digital": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/signature-digital", "@dropbox/dig-illustrations/hero/signature-paper": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/signature-paper", "@dropbox/dig-illustrations/hero/sports-stadium": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/sports-stadium", "@dropbox/dig-illustrations/hero/stationary-bike": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/stationary-bike", "@dropbox/dig-illustrations/hero/students-1": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/students-1", "@dropbox/dig-illustrations/hero/students-2": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/students-2", "@dropbox/dig-illustrations/hero/study-group": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/study-group", "@dropbox/dig-illustrations/hero/supreme-court": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/supreme-court", "@dropbox/dig-illustrations/hero/team-cheerleaders": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/team-cheerleaders", "@dropbox/dig-illustrations/hero/team-esignature": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/team-esignature", "@dropbox/dig-illustrations/hero/team-filmmakers": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/team-filmmakers", "@dropbox/dig-illustrations/hero/team-hands": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/team-hands", "@dropbox/dig-illustrations/hero/team-hike": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/team-hike", "@dropbox/dig-illustrations/hero/team-lift": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/team-lift", "@dropbox/dig-illustrations/hero/tech-data-center": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/tech-data-center", "@dropbox/dig-illustrations/hero/tech-laptop": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/tech-laptop", "@dropbox/dig-illustrations/hero/tech-research-lab": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/tech-research-lab", "@dropbox/dig-illustrations/hero/telescope": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/telescope", "@dropbox/dig-illustrations/hero/thinking": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/thinking", "@dropbox/dig-illustrations/hero/to-do-list": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/to-do-list", "@dropbox/dig-illustrations/hero/toss-wastebasket": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/toss-wastebasket", "@dropbox/dig-illustrations/hero/travel-backpack": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/travel-backpack", "@dropbox/dig-illustrations/hero/travel-hike": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/travel-hike", "@dropbox/dig-illustrations/hero/travel-market": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/travel-market", "@dropbox/dig-illustrations/hero/travel-scooter": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/travel-scooter", "@dropbox/dig-illustrations/hero/travel-van": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/travel-van", "@dropbox/dig-illustrations/hero/van-cityscape": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/van-cityscape", "@dropbox/dig-illustrations/hero/vase-repair": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/vase-repair", "@dropbox/dig-illustrations/hero/vault": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/vault", "@dropbox/dig-illustrations/hero/video-analytics": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/video-analytics", "@dropbox/dig-illustrations/hero/video-call-collage": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/video-call-collage", "@dropbox/dig-illustrations/hero/video-editing": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/video-editing", "@dropbox/dig-illustrations/hero/video-stream": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/video-stream", "@dropbox/dig-illustrations/hero/vista": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/vista", "@dropbox/dig-illustrations/hero/warehouse-forklift": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/warehouse-forklift", "@dropbox/dig-illustrations/hero/water-cooler": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/water-cooler", "@dropbox/dig-illustrations/hero/whiteboard": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/whiteboard", "@dropbox/dig-illustrations/hero/work-desk": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-desk", "@dropbox/dig-illustrations/hero/work-desk-headset": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-desk-headset", "@dropbox/dig-illustrations/hero/work-desk-plant": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-desk-plant", "@dropbox/dig-illustrations/hero/work-desk-video-call": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-desk-video-call", "@dropbox/dig-illustrations/hero/work-from-home-1": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-from-home-1", "@dropbox/dig-illustrations/hero/work-from-home-2": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-from-home-2", "@dropbox/dig-illustrations/hero/work-from-home-3": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-from-home-3", "@dropbox/dig-illustrations/hero/work-from-home-4": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-from-home-4", "@dropbox/dig-illustrations/hero/work-from-home-5": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-from-home-5", "@dropbox/dig-illustrations/hero/work-mug": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-mug", "@dropbox/dig-illustrations/hero/work-outside": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/work-outside", "@dropbox/dig-illustrations/hero/worker-cafe": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/worker-cafe", "@dropbox/dig-illustrations/hero/workshop-integration": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/workshop-integration", "@dropbox/dig-illustrations/hero/workshop-tools": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/hero/workshop-tools", "@dropbox/dig-illustrations/spot/analyze": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/analyze", "@dropbox/dig-illustrations/spot/artist-painter": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/artist-painter", "@dropbox/dig-illustrations/spot/artist-sculptor": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/artist-sculptor", "@dropbox/dig-illustrations/spot/attention-knock": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/attention-knock", "@dropbox/dig-illustrations/spot/attention-ring": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/attention-ring", "@dropbox/dig-illustrations/spot/balloon-gone": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/balloon-gone", "@dropbox/dig-illustrations/spot/balloon-pop": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/balloon-pop", "@dropbox/dig-illustrations/spot/bike-1": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/bike-1", "@dropbox/dig-illustrations/spot/bike-2": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/bike-2", "@dropbox/dig-illustrations/spot/bike-courier": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/bike-courier", "@dropbox/dig-illustrations/spot/bike-shop": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/bike-shop", "@dropbox/dig-illustrations/spot/bird-perch": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/bird-perch", "@dropbox/dig-illustrations/spot/bowl-empty": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/bowl-empty", "@dropbox/dig-illustrations/spot/box-empty": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/box-empty", "@dropbox/dig-illustrations/spot/box-empty-link": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/box-empty-link", "@dropbox/dig-illustrations/spot/browser-extension": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/browser-extension", "@dropbox/dig-illustrations/spot/building-office": "metaserver/static/prod_assets_web_modules/@dropbox/dig-illustrations/spot/building-office", "@dropbox/dig-illustrations/spot/building-storefront": "metase…

---

