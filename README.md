## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-29](docs/good-messages/2023/2023-12-29.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,628,503 were push events containing 3,398,705 commit messages that amount to 177,382,074 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [WarlockD/tgstation](https://github.com/WarlockD/tgstation)@[33e10634ba...](https://github.com/WarlockD/tgstation/commit/33e10634ba89c28c1ca3518068e916ec0a10b33e)
#### Friday 2023-12-29 00:15:31 by Iamgoofball

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3f9df35c14...](https://github.com/treckstar/yolo-octo-hipster/commit/3f9df35c145f2ef8822996b22ea9c2c74f77b8ab)
#### Friday 2023-12-29 00:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [StrangeWeirdKitten/Skyrat-tg](https://github.com/StrangeWeirdKitten/Skyrat-tg)@[b072ecd91f...](https://github.com/StrangeWeirdKitten/Skyrat-tg/commit/b072ecd91ff78f8c0f190e0bf647f34f46a855a0)
#### Friday 2023-12-29 00:25:10 by SkyratBot

[MIRROR] Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white [MDB IGNORE] (#25803)

* Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white (#80450)

## About The Pull Request

This rounds up the "Other" (Brainwashed, Hypnotised, Wizard Revenge, and
Obsession) antagonist category into the new "Deviant Crew" category.
This tab is white!

Obsessed crew are now displayed in the orbit panel (no other antagonists
in this group are though).

The Spacetime Aberrations (Paradox Clone) group has also been changed to
be white.

Here's how that looks:

![image](https://github.com/tgstation/tgstation/assets/28870487/415b8cbb-7ac3-4e24-9f74-466480c2aab0)
## Why It's Good For The Game

As was the case with paradox clones, observers can already discern when
a player is obsessed. It shouldn't be a pain to observe these guys,
especially when they're a more RP oriented antag that are (usually)
deserving of the audience.

I made paradox clones and obsessed the same color because they're both
in the broader spectrum of "fucked up crew".

Also converts common text entries to a single define. That is good
coding practice I think.
## Changelog
:cl: Rhials
qol: Obsessed crewmembers are now displayed in the orbit panel.
qol: The Paradox Clone orbit menu tab is now white. Neat!
/:cl:

* Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [Sonic121x/FluffySTG](https://github.com/Sonic121x/FluffySTG)@[e44cfc63c7...](https://github.com/Sonic121x/FluffySTG/commit/e44cfc63c7451181e1b5b9dec33e6805b384c3b0)
#### Friday 2023-12-29 00:30:42 by Iajret Creature

[THE HALF-MODULAR PRINCE] Snalance (Snail Balance) and Snissues (Snail Issues) Adjustment (#1219)

* initial d

* holy shit i forgot

* i got so much cheese in my pocket, they thought I was a fucking calzone

* opp was sneak-dissing on the 'gram, turned his city into pompeii

* Just fixing some diffs (line breaks should match tg)

* Fixes these edit comments

---------

Co-authored-by: Nerevar <12636964+Nerev4r@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [lessthnthree/Bubberstation](https://github.com/lessthnthree/Bubberstation)@[25be46a37d...](https://github.com/lessthnthree/Bubberstation/commit/25be46a37dfd73308619ad393479bb06cc233ced)
#### Friday 2023-12-29 00:51:19 by aKromatopzia

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
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[f12a571a6c...](https://github.com/f13babylon/f13babylon/commit/f12a571a6c81e870f28ed2f8f430b10371707a8d)
#### Friday 2023-12-29 01:14:32 by panzerr1944

Fixes & Balance; the Big One (Ready) (#426)

## About The Pull Request
Meganerfs plascutter damage so they're not comically OP. Rebel deleted
all their PRs, so I'm redoing them all in this one too. Currently
includes;
Removes Dumb Chems (https://github.com/f13babylon/f13babylon/pull/424)
Rear Ech becomes Off-Duty + Vet Ranger Tweaks
(https://github.com/f13babylon/f13babylon/pull/371)
Crafting Recipe Adjustments, Explosive Skill Given to More Roles, &
Fixes for Scribes (https://github.com/f13babylon/f13babylon/pull/374)
Gun-Bloat-B-Gone, Fixes to Bolt Actions, Colt 10mm Revolver, AK-112, &
Loadout Changes (https://github.com/f13babylon/f13babylon/pull/418)
Direct excerpt from Gun-Bloat-B-Gone;
This is a massive compiled PR since I had to keep doing the following
while making it:

Issue of the NCR Captain getting a revolver that could deflect 50% of
incoming rounds, this stacked with katanas and worked with shields.
Issue of Vex getting a P-90. I wanted to reduce their slots as well in
this PR but instead I simply added the AK-112 and gave them that. This
is a nerf, sorry dudes but your P-90 was way too fucking cracked.
Bolt actions had WAY too much slowdown to ever be viable. This has been
greatly reduced.
M1 Carbine, Commando Carbine, and Delise Carbine have been removed from
rotation (but will be left in code for now). Reason why is all 3 are
useless due to Smg+pistol buffs and use pistol calibers, which has
damage drop off now. While I personally liked the M1 it didn't have a
niche, wasn't.. great to begin with, and has been thrown to the wayside.
In these guns place other more useful guns have been added to their loot
tier.
Various fire-delay fixes I got complaints about being too high/low.
Adds knockback to the powerfist. I don't actually know WHY people wanted
that back, since imo it made it worse, but whatever. Also buffed its
damage/AP to compete with most other melee weapons.
Removed Paladin Polearm from rotation. Weapon was really - weird? And
was meant for Brotherhood. Since the Ballistic Fist has gotten a good
buff due to fire delay fix, I added it instead to the Enclave Gunny in
its place. This will be way better for them, has a very good niche, and
also gave them a plasma glock with it.
Also, adds two new guns in the place of those removed:

10mm revolver - Reason is this gun existed prior and adds a
lower-caliber revolver using pistol rounds. Gun auto-ejects casings, is
able to compete with the N-99. Basically a harder-hitting, slower
firing, N-99 that cant take attachments.
AK112 - This gun is practically needed and is a 'lore accurate' version
that I could reason. The P-90 and assault carbine are way too good for
round start guns for most roles. As such, I've replaced them with this
gun near entirely. The AK-112 hits as hard as the P90, so 5 less damage,
but also has 2 extra spread over the assault carbine AND, unlike either,
fires at the same RPM as the R-91. So it actually is a real CHOICE if
you're going to use this, or an R-91.
Armor fixes:

Functioning PA now has the same stats as salvaged PA (baring the
slowdown). There was no reason salvaged PA was better than functioning
PA with just 0.1 more slowdown. (Bumped T-51 bullet protection up by 5,
and laser up by 10. Reason was to make this in-line as what it was
prior.)
Enclave PR that has been up has been incorporated baring the plasma
changes. This makes Enclave armor have SLIGHTLY better rad protection
than normal combat armor, and makes their armor craftable.
NCR wound protection has been touched up a tad, it was really bad and I
genuinely feel bad NCR players had to deal with that.
Enclave Changes
Roles were really heavy for their gear. In exchange for letting them
keep their faction gear being high-end, their slots have been reduced to
9 combat slots.

Marines 5 -> 3
Specialist 2 -> 0
Sergeants 2 -> 2
Armored Infantry 0 -> 1
Gunnery Sergeant 1 -> 1
LT 1 -> 1
Synthetic 1 -> 1
Scientists have gone unchanged and have kept both slots.

Also, Sergeants have lost their APA. In exchange, they have been given
Marine armor. The heavy gunner, however, has been given the choice
between a plasma caster and the Minigun and has kept their APA.
Gunnery has gotten XO-1 variant of APA, which is green and SLIGHTLY
better so he sticks out.

Loadout changes are various, took away MP5s, gave them newly converted
R-93's that are single shot 5mm guns. Gave them a trench gun, upon
request, for their alternative loadout. Gave the Gunnery a G-11 and
moved his caster over to the Armored Infantry. Sergeants lost their
carbines, got AK-112s which are more fair for their automatic gear.

## Why It's Good For The Game
No ez mass printable hyperop infinite ammo plasmacutter dual wield
memery. Fixes from Rebels PRs which are all good for the server and
balance as a whole (see links above). Better enclave base. It's still
bad, but it's better. For enclave base, see here;

![image](https://github.com/f13babylon/f13babylon/assets/76122712/06401e23-71e7-4aba-bdeb-d5d56a3d8bec)

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
🆑 
balance: plascutter damage nerfed to 1, 2 and 0 respectively
removes: Various chems from rotation.
tweak: Adjusted space drugs name to fit lore better.
tweak: Removes bullet bouncing off Vet Range default, makes it a loadout
choice option.
tweak: Adds deagle to AMR as a sidearm.
tweak: Renames rear-ech to off-duty. (Their display has changed too but
code path name has been left due to it effecting played hours on a
faction if changed.)
balance: Removed blueprints that are unbalanced/unneeded, substituted
some. See description for full list.
added: More explosive crafting trait to roles. See description for
fulllist.
fixes: Fixes oversights of books, such as the senior scribe having a
mid-surgery book on the shield scribe loadout. They already had mid-med.
Etc.
balance: removes ghoul and radroach spawners from enclave base
tweak: shuffles 2 door downs at the enclave base and removes a cell
tweak: adds a pair of binos to enclave base
remove: locker-room from enclave base
add: 3 un-used rooms for bunker duties
add: scientist office
remove: some wasted space in the bottom right
add: orion trail arcade machine
add: 2 extra tools for use roundstart
add: 20 gunpowder, 100 metal, 50 glass roundstart
add: roundstart rng foodspawners in cafeteria
add: pre-built DNA manipulator with disks
tweak: See description, massive changes to: Fire delay of guns, 2 new
weapons, removal of bloat-y weapons, bolt action slowdown, misc changes
to weapon slowdown/stats, armor value fixes, and merging Enclave PR as
asked by Foxeye into this one.
balance: swapped the town sheriff dep's police rifles for 2 trail
carbines, a cowboy repeater and a brush gun
🆑

---
## [nushell/nightly](https://github.com/nushell/nightly)@[21b3eeed99...](https://github.com/nushell/nightly/commit/21b3eeed99b3beb45b10a266ec05f4eabf897796)
#### Friday 2023-12-29 01:15:22 by Yash Thakur

Allow spreading arguments to commands (#11289)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

Finishes implementing https://github.com/nushell/nushell/issues/10598,
which asks for a spread operator in lists, in records, and when calling
commands.

# Description
<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

This PR will allow spreading arguments to commands (both internal and
external). It will also deprecate spreading arguments automatically when
passing to external commands.

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

- Users will be able to use `...` to spread arguments to custom/builtin
commands that have rest parameters or allow unknown arguments, or to any
external command
- If a custom command doesn't have a rest parameter and it doesn't allow
unknown arguments either, the spread operator will not be allowed
- Passing lists to external commands without `...` will work for now but
will cause a deprecation warning saying that it'll stop working in 0.91
(is 2 versions enough time?)

Here's a function to help with demonstrating some behavior:
```nushell
> def foo [ a, b, c?, d?, ...rest ] { [$a $b $c $d $rest] | to nuon }
```

You can pass a list of arguments to fill in the `rest` parameter using
`...`:
```nushell
> foo 1 2 3 4 ...[5 6]
[1, 2, 3, 4, [5, 6]]
```

If you don't use `...`, the list `[5 6]` will be treated as a single
argument:

```nushell
> foo 1 2 3 4 [5 6] # Note the double [[]]
[1, 2, 3, 4, [[5, 6]]]
```

You can omit optional parameters before the spread arguments:
```nushell
> foo 1 2 3 ...[4 5] # d is omitted here
[1, 2, 3, null, [4, 5]]
```

If you have multiple lists, you can spread them all:
```nushell
> foo 1 2 3 ...[4 5] 6 7 ...[8] ...[]
[1, 2, 3, null, [4, 5, 6, 7, 8]]
```

Here's the kind of error you get when you try to spread arguments to a
command with no rest parameter:

![image](https://github.com/nushell/nushell/assets/45539777/93faceae-00eb-4e59-ac3f-17f98436e6e4)

And this is the warning you get when you pass a list to an external now
(without `...`):


![image](https://github.com/nushell/nushell/assets/45539777/d368f590-201e-49fb-8b20-68476ced415e)


# Tests + Formatting
<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- `cargo test --workspace` to check that all tests pass (on Windows make
sure to [enable developer
mode](https://learn.microsoft.com/en-us/windows/apps/get-started/developer-mode-features-and-debugging))
- `cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

Added tests to cover the following cases:
- Spreading arguments to a command that doesn't have a rest parameter
(unexpected spread argument error)
- Spreading arguments to a command that doesn't have a rest parameter
*but* there's also a missing positional argument (missing positional
error)
- Spreading arguments to a command that doesn't have a rest parameter
but does allow unknown arguments, such as `exec` (allowed)
- Spreading a list literal containing arguments of the wrong type (parse
error)
- Spreading a non-list value, both to internal and external commands
- Having named arguments in the middle of rest arguments
- `explain`ing a command call that spreads its arguments

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

# Examples

Suppose you have multiple tables:
```nushell
let people = [[id name age]; [0 alice 100] [1 bob 200] [2 eve 300]]
let evil_twins = [[id name age]; [0 ecila 100] [-1 bob 200] [-2 eve 300]]
```

Maybe you often find yourself needing to merge multiple tables and want
a utility to do that. You could write a function like this:
```nushell
def merge_all [ ...tables ] { $tables | reduce { |it, acc| $acc | merge $it } }
```

Then you can use it like this:
```nushell
> merge_all ...([$people $evil_twins] | each { |$it| $it | select name age })
╭───┬───────┬─────╮
│ # │ name  │ age │
├───┼───────┼─────┤
│ 0 │ ecila │ 100 │
│ 1 │ bob   │ 200 │
│ 2 │ eve   │ 300 │
╰───┴───────┴─────╯
```

Except they had duplicate columns, so now you first want to suffix every
column with a number to tell you which table the column came from. You
can make a command for that:
```nushell
def select_and_merge [ --cols: list<string>, ...tables ] {
  let renamed_tables = $tables
    | enumerate
    | each { |it|
      $it.item | select $cols | rename ...($cols | each { |col| $col + ($it.index | into string) })
    };
  merge_all ...$renamed_tables
}
```
And call it like this:
```nushell
> select_and_merge --cols [name age] $people $evil_twins
╭───┬───────┬──────┬───────┬──────╮
│ # │ name0 │ age0 │ name1 │ age1 │
├───┼───────┼──────┼───────┼──────┤
│ 0 │ alice │  100 │ ecila │  100 │
│ 1 │ bob   │  200 │ bob   │  200 │
│ 2 │ eve   │  300 │ eve   │  300 │
╰───┴───────┴──────┴───────┴──────╯
```

---

Suppose someone's made a command to search for APT packages:

```nushell
# The main command
def search-pkgs [
    --install                   # Whether to install any packages it finds
    log_level: int              # Pretend it's a good idea to make this a required positional parameter
    exclude?: list<string>      # Packages to exclude
    repositories?: list<string> # Which repositories to look in (searches in all if not given)
    ...pkgs                     # Package names to search for
] {
  { install: $install, log_level: $log_level, exclude: ($exclude | to nuon), repositories: ($repositories | to nuon), pkgs: ($pkgs | to nuon) }
}
```

It has a lot of parameters to configure it, so you might make your own
helper commands to wrap around it for specific cases. Here's one
example:
```nushell
# Only look for packages locally
def search-pkgs-local [
    --install              # Whether to install any packages it finds
    log_level: int
    exclude?: list<string> # Packages to exclude
    ...pkgs                # Package names to search for
] {
  # All required and optional positional parameters are given
  search-pkgs --install=$install $log_level [] ["<local URI or something>"] ...$pkgs
}
```
And you can run it like this:
```nushell
> search-pkgs-local --install=false 5 ...["python2.7" "vim"]
╭──────────────┬──────────────────────────────╮
│ install      │ false                        │
│ log_level    │ 5                            │
│ exclude      │ []                           │
│ repositories │ ["<local URI or something>"] │
│ pkgs         │ ["python2.7", vim]           │
╰──────────────┴──────────────────────────────╯
```

One thing I realized when writing this was that if we decide to not
allow passing optional arguments using the spread operator, then you can
(mis?)use the spread operator to skip optional parameters. Here, I
didn't want to give `exclude` explicitly, so I used a spread operator to
pass the packages to install. Without it, I would've needed to do
`search-pkgs-local --install=false 5 [] "python2.7" "vim"` (explicitly
pass `[]` (or `null`, in the general case) to `exclude`). There are
probably more idiomatic ways to do this, but I just thought it was
something interesting.

If you're a virologist of the [xkcd](https://xkcd.com/350/) kind,
another helper command you might make is this:
```nushell
# Install any packages it finds
def live-dangerously [ ...pkgs ] {
  # One optional argument was given (exclude), while another was not (repositories)
  search-pkgs 0 [] ...$pkgs --install # Flags can go after spread arguments
}
```

Running it:
```nushell
> live-dangerously "git" "*vi*" # *vi* because I don't feel like typing out vim and neovim
╭──────────────┬─────────────╮
│ install      │ true        │
│ log_level    │ 0           │
│ exclude      │ []          │
│ repositories │ null        │
│ pkgs         │ [git, *vi*] │
╰──────────────┴─────────────╯
```

Here's an example that uses the spread operator more than once within
the same command call:
```nushell
let extras = [ chrome firefox python java git ]

def search-pkgs-curated [ ...pkgs ] {
  (search-pkgs
      1
      [emacs]
      ["example.com", "foo.com"]
      vim # A must for everyone!
      ...($pkgs | filter { |p| not ($p | str contains "*") }) # Remove packages with globs
      python # Good tool to have
      ...$extras
      --install=false
      python3) # I forget, did I already put Python in extras?
}
```

Running it:
```nushell
> search-pkgs-curated "git" "*vi*"
╭──────────────┬───────────────────────────────────────────────────────────────────╮
│ install      │ false                                                             │
│ log_level    │ 1                                                                 │
│ exclude      │ [emacs]                                                           │
│ repositories │ [example.com, foo.com]                                            │
│ pkgs         │ [vim, git, python, chrome, firefox, python, java, git, "python3"] │
╰──────────────┴───────────────────────────────────────────────────────────────────╯
```

---
## [Funkeke/langchain](https://github.com/Funkeke/langchain)@[d4f45b1421...](https://github.com/Funkeke/langchain/commit/d4f45b1421ec8b56fe6aeed84f81ca1b3f91383f)
#### Friday 2023-12-29 01:20:40 by Sypherd

core(minor): Allow explicit types for ChatMessageHistory adds (#14967)

<!-- Thank you for contributing to LangChain!

Replace this entire comment with:
  - **Description:** a description of the change, 
  - **Issue:** the issue # it fixes (if applicable),
  - **Dependencies:** any dependencies required for this change,
- **Tag maintainer:** for a quicker response, tag the relevant
maintainer (see below),
- **Twitter handle:** we announce bigger features on Twitter. If your PR
gets announced, and you'd like a mention, we'll gladly shout you out!

Please make sure your PR is passing linting and testing before
submitting. Run `make format`, `make lint` and `make test` to check this
locally.

See contribution guidelines for more information on how to write/run
tests, lint, etc:
https://python.langchain.com/docs/contributing/

If you're adding a new integration, please include:
1. a test for the integration, preferably unit tests that do not rely on
network access,
2. an example notebook showing its use. It lives in `docs/extras`
directory.

If no one reviews your PR within a few days, please @-mention one of
@baskaryan, @eyurtsev, @hwchase17.
 -->
## Description
Changes the behavior of `add_user_message` and `add_ai_message` to allow
for messages of those types to be passed in. Currently, if you want to
use the `add_user_message` or `add_ai_message` methods, you have to pass
in a string. For `add_message` on `ChatMessageHistory`, however, you
have to pass a `BaseMessage`. This behavior seems a bit inconsistent.
Personally, I'd love to be able to be explicit that I want to
`add_user_message` and pass in a `HumanMessage` without having to grab
the `content` attribute. This PR allows `add_user_message` to accept
`HumanMessage`s or `str`s and `add_ai_message` to accept `AIMessage`s or
`str`s to add that functionality and ensure backwards compatibility.

## Issue
* None

## Dependencies
* None

## Tag maintainer
@hinthornw
@baskaryan 

## Note
`make test` results in `make: *** No rule to make target 'test'.  Stop.`

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[b7ca70e472...](https://github.com/cheesePizza2/Foundation-19/commit/b7ca70e472782606c7fac09026471575745ccb74)
#### Friday 2023-12-29 02:01:19 by cheesePizza2

Fixes goals system harddels (#1316)

* shit

* fuck you

* removes spaces

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[a666b103d3...](https://github.com/cheesePizza2/Foundation-19/commit/a666b103d3adcbcc9d954d05bad4e348f0d6ffaa)
#### Friday 2023-12-29 02:01:19 by cheesePizza2

Fixes CDZ Medical Checkpoint windoors (#1386)

* changes

* fuck me

* fuck you

---
## [foxymegneil/f13babylon](https://github.com/foxymegneil/f13babylon)@[fc41127084...](https://github.com/foxymegneil/f13babylon/commit/fc41127084c96e75ed37c1e51c6ad9d2305da643)
#### Friday 2023-12-29 02:36:39 by Stutternov

Shield Change (As Requested) (#381)

## About The Pull Request

Was requested to do this upon issues with shields. 

So, before some shields literally had the health of Bubblegum + armor on
them as well. The health has been greatly reduced on some, some others
have been buffed at lower end.

Telescopic shield has also been removed since it's busted as hell, had
2250 health, tons of armor, and such.

## Why It's Good For The Game

Some shields that were even labeled as removed were still in the game,
like the Telescopic. Others got buffed by someone last week for some
reason despite stam damage being fucked, etc.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
balance: Rebalances shields integrity.
removes: Telescopic shield (Use the riot, it's identical but just not
telescopic.)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[1f3b68a068...](https://github.com/treckstar/yolo-octo-hipster/commit/1f3b68a068b5025329ed22bba89e454c4e48c5d5)
#### Friday 2023-12-29 03:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [TeamIndustrialST/Industrial-addon-remake](https://github.com/TeamIndustrialST/Industrial-addon-remake)@[bd21ba511c...](https://github.com/TeamIndustrialST/Industrial-addon-remake/commit/bd21ba511cc337b3fe3942fdfa16ce858dd815b5)
#### Friday 2023-12-29 03:32:44 by jl

DIE YOU FUCKING ASSHOLE PEICE OF SHIT YOU LITTLE POOPYHWEAD YOU LITTLE POOPIER DSAAEJFDDFSDFSIODFSJFSJFSDSFDSFDJOIFDJOJSFODI

---
## [cockinstitute/cockinstituteweb](https://github.com/cockinstitute/cockinstituteweb)@[1c021eefed...](https://github.com/cockinstitute/cockinstituteweb/commit/1c021eefed6748c742d628fb143b6f7b5283f446)
#### Friday 2023-12-29 05:02:56 by cockinstitute

Delete explosionstile.png

bro I am a programmer's worst nightmare holy shit I am so sorry lmao

---
## [pooka109/crawl](https://github.com/pooka109/crawl)@[645d2ae13f...](https://github.com/pooka109/crawl/commit/645d2ae13f9e5acbda4b4080bf64c5fbcc20e7d9)
#### Friday 2023-12-29 05:08:35 by regret-index

Spruce up each rune-guarding Pan lords' realm

The bulk of particular enemy decisions for most of the four fixed Pan lords
enemies were made ages ago, before we had nearly so many varied monsters
for almost any branch in general. Since there's been such a massive influx
of new monsters to work with compared to so far back in the past, it'd be
reasonable to further add to the gimmickry the lords themselves already
brandish, rather than focus on plain + common + weak flavour choices for
Pan vaults like occultists, large abominations, or weaker skeletons.

 * Mnoleg's level uses very few very ugly things, abominations, or
   tentacled monstrosities for a lot more protean progenitors and shadow
   demons- the former for more interesting shapechanging, the latter to
   fit the summoning (and since Tartarus lost them). There's far too many
   of the former melee-only types before extended, and Mnoleg lacks much
   for noticeable spawns beyond eyes and cacodemons- these two will both
   help. (Note: Don't use proteans beyond Zot, Zigs, and Mnoleg's floor.
   Zot non-draconians get very limited to no non-Zig drift or bleed to
   keep them distinct and dramatic.)

 * Gloorx Vloq's level loses lorocyproca and demonic crawlers for reapers
   and entropy weavers, while upgrading the skeletons hard. While this
   loses a bit of spectral flavour and demon presence, demonic crawlers
   have no real threat in Pan and there's some interest in removing
   lorocyprocas for more interesting tier-2 designs in the future.
   Meanwhile, entropy weavers still can corrode even extended characters,
   and reapers have a new effect plus aren't much prominent in Tartarus
   anymore. (This is a bit of placeholder future-proofing: if a new
   summoning tier-2 does end up existing, then shadow demons could fit
   here better over some other spawns, like shadow wraith and soul eater
   explicit placements, and those demons can replace Mnoleg's shadow
   demons.)

 * Lom Lobon's level loses arcanists and occultists, as they're pretty
   mundane mortal scholars of magic for extended. Instead, to represent
   more interesting mystics across the Dungeon, there's now small amounts
   of one conjurer from each of the Lair roulette branches- nagaraja,
   merfolk aquamancers, fenstrider witches, and jorogumo. They readily
   match up with the green deaths or blizzard demons already present, and
   while mostly not too extra dangerous at Pan depth they're more
   interesting to see than the prior options.

 * Cerebov, the most infamous and intimidating lord of Pandemonium, loses
   orange demons and crimson imps for pretty rainbow fluttering insects.
   They're definitely not the newly revised, rarely used elsewhere,
   very fire-focused sun moths.

 * Each of the unrand lords vaults places an increasing clump of demonspawn
   related to the lord in question for each rune you have on you when
   entering. Mnoleg gets corrupters (summoning), Gloorx Vloq gets black
   suns (necromancy), Lom Lobon gets blood saints (conjurations), and
   Cerebov gets warmongers (big equipment). There's not any extra in the
   given levels beyond those initial counts, though, so they shouldn't
   make the levels blend together too hard with the rest of Pan.

 * Also, the non-holy guaranteed demonic rune vaults and Mnoleg's realm
   both contain some potions of mutation now, to compensate for when the
   old potion of cure / beneficial mutation shuffling removed the (very
   delayed, unreliable, heavily guarded) potions of cure mutation in the
   holy pan level. Those holies should be revised to be less boring, at
   some point, but for now, it should make those vaults feel more
   worthwhile.

This also updates arenasprint and the chasing-across-Pan / orb run spawns
of the lords for those four new sets, a few new tile choices to reduce the
use of generic D floor and wall tiles, deals with teleport islands in Lom's
realm, and tweaks a varied number of vaults to even out some higher and
lower vault lethality ends. Maybe eventually Pan will be varied enough to
be made yet shorter and extended could be made shorter in general?...

---
## [lintangtimur/overthrow3-source](https://github.com/lintangtimur/overthrow3-source)@[d2ecaffbce...](https://github.com/lintangtimur/overthrow3-source/commit/d2ecaffbce8514ee5b60c3d7bb88b775b283258e)
#### Friday 2023-12-29 05:22:11 by lintangtimur

2.3.1.0
• Fixed the new neutral items not being affected by the bonus neutral item stats upgrade

BROODMOTHER:
• Fixed Spin Web's health regen talent

CRYSTAL MAIDEN:
• Removed Frostbite's duration upgrade
• Frostbite/Crystal Clone's cooldown & manacost upgrade decreased from 10% --> 8% (max count decreased from 8 --> 5)
• Crystal Clone's distance/radius upgrade is now linked with its cooldown & manacost upgrade

ENIGMA:
• Replaced Midnight Pulse's current health as damage upgrade with a +15/15/20/20 base damage upgrade for Octet/Quintet/Duo/FFA

GYROCOPTER:
• Fixed Call Down's missile damage upgrade and updated it to +100

IO:
• Tether's movement speed bonus upgrade decreased from 3% --> 2% and now also grants +10 damage per second

KEEPER OF THE LIGHT:
• Replaced Will-o-Wisp's hit count upgrade with a +25/25/30/35 damage upgrade for Octet/Quintet/Duo/FFA

MEDUSA:
• Split Shot's outgoing damage upgrade's max count decreased from 2 --> 1

PHANTOM ASSASSIN:
• Phantom Strike's duration upgrade increased from 0.2 --> 0.3

OMNIKNIGHT:
• Guardian Angel's cooldown/manacost upgrade's max count increased from 6 --> 10
• Guardian Angel's duration upgrade increased from 0.7 --> 1

SVEN:
• God's Strength's slow resistance upgrade increased from 6% --> 6.25% (max count decreased from 10 --> 8

TERRORBLADE:
• Metamorphosis' duration decreased from 30 --> 25
• Metamorphosis' duration talent decreased from 20 --> 10
• Metamorphosis' cooldown decreased from 150 --> 60
• Metamorphosis' cooldown talent decreased from 20 --> 8

TIDEHUNTER:
• Anchor Smash's damage reduction upgrade decreased from 7.5% --> 5%

UNDERLORD:
• Pit of Malice's pit duration reverted to vanilla (8 --> 12)
• Replaced Pit of Malice's radius upgrade with a +40 ensnare damage upgrade

URSA:
• Overpower's slow resistance upgrade's max count increased from 10 --> 14

VENGEFUL SPIRIT:
• Nether Swap now has a +70 damage upgrade/shield upgrade
• Nether Swap's shield duration upgrade increased from 0.5 --> 2 and now has a max count of 5

WINDRANGER:
• Removed Gale Force's radius upgrade

WITCH DOCTOR:
• Voodoo Restoration's heal upgrade increased from 7 --> 10

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[4c32b30565...](https://github.com/lessthnthree/effigy-se/commit/4c32b305659c00804eda67e56249b6edb92fa907)
#### Friday 2023-12-29 05:34:37 by Time-Green

Organ movement refactor *Un-nullspaces your organs* (#79687)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

closes #53931, #70916, #53931

Organs were previously stored in nullspace. Now they are stored in their
prospective bodyparts. Bodyparts are now stored in the mob.

I've also had to refactor a lot of code concerning organ movement.
Previously, organs were only moved into bodyparts once the bodyparts
were removed. To accomodate this change, two major distinctions have
been made:

**Bodypart removal/insertion**
Called only when an organ is taken out of a bodypart. Bodypart overlays,
damage modifiers or other changes that should affect a bodypart itself
goes here.

**Mob insertion/removal**
Called when an organ is removed from a mob. This can either be directly,
by taking the organ out of a mob, or by removing the bodypart that
contains the organ. This lets you add and remove organ effects safely
without having to worry about the bodypart.

Now that we controle the movement of bodyparts and organs, we can fuck
around with them more. Summoning someones head or chest or heart will
actually kill them now (and quite violently I must say (chest summoning
gibs lol)).

https://github.com/tgstation/tgstation/assets/7501474/5efc9dd3-cfd5-4ce4-b70f-d0d74894626e

I´ve also added a unit test that violently tears apart and reconstructs
a person in different ways to see if they get put toghether the right
way

This will definitely need a testmerge. I've done a lot of testing to
make sure interactions work, but more niche stuff or my own incompetence
can always slip through.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

A lot of organ work is quite restricted. You can't C4 someones heart,
you cant summon their organs and a lot of exceptions have to be made to
keep organs in nullspace. This lets organs (and bodyparts) play more
nicely with the rest of the game. This also makes it a lot easier to
move away from extorgans since a lot of their unique movement code has
been removed and or generalized.

I don't like making PRs of this size (I'm so sorry reviewers), but I was
in a unique position to replace the entire system in a way I couldn't
have done conveniently in multiple PRs

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
refactor: Your organs are now inside your body. Please report any issues
with bodypart and organ movement, including exotic organ, on github and
scream at me
fix: Cases of unexpected organ movement, such as teleporting bodyparts
and organs with spells, now invokes a proper reaction (usually violent
death)
runtime: Fixes HARS runtiming on activation/deactivation
fix: Fixes lag when species swapping
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [wiverns/GalaxiaStation-WIV](https://github.com/wiverns/GalaxiaStation-WIV)@[1e3ea20492...](https://github.com/wiverns/GalaxiaStation-WIV/commit/1e3ea20492c5e105e6e5cfbbcaed8149f7c7cbf8)
#### Friday 2023-12-29 06:06:51 by wiverns

Disables the annoying fear of Santa from the claustrophobia quirk

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
What it says on the top: This just disables the fear of santa within the claustrophobia quirk.

<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

## How This Contributes To The Skyrat Roleplay Experience
It's funny the first time you get the pun, but then afterwards all it does it interrupt RP and force people with the quirk to either leave or ask people to stop wearing hats, which isn't fun for anyone.

<!-- Please add a short description of why you think these changes would benefit the game and the roleplay atmosphere of the server. If you can't justify it in words, it might not be worth adding. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely observed by players or admins you should add a changelog. If your change does NOT meet this description, remove this section. Be sure to properly mark your PRs to prevent unnecessary GBP loss. You can read up on GBP and it's effects on PRs in the tgstation guides for contributors. Please note that maintainers freely reserve the right to remove and add tags should they deem it appropriate. You can attempt to finagle the system all you want, but it's best to shoot for clear communication right off the bat. -->

:cl:
del: Holiday spirit will no longer suffocate claustrophobes
/:cl:

---
## [wiverns/effigy-se](https://github.com/wiverns/effigy-se)@[472927b282...](https://github.com/wiverns/effigy-se/commit/472927b282514628164cd53d775104c2acd87ea9)
#### Friday 2023-12-29 06:07:49 by KingkumaArt

Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#79803)

## About The Pull Request

Simply put, due to how "caseless" is an element added to the ammo when
it hits something, but ammo is qdeleted upon hitting someone. If shot
point blank without combat mode (for some reason) it tries to add
caseless to an ammo that no longer exists. For some reason, the result
of this is to just fucking crash DS instead of aborting the adding of
the element. The ammo isnt reusable anymore, but I'll take that over
crashing.

## Why It's Good For The Game

Removes a game-breaking bug. I hate gun ammo code so much. 

## Changelog



:cl:
fix: Stopped a DS crash when shooting a rebar crossbow in specific
circumstances.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [beartype/beartype](https://github.com/beartype/beartype)@[4850ab2dd0...](https://github.com/beartype/beartype/commit/4850ab2dd0593e940e1662f42235b92c7f92f8cc)
#### Friday 2023-12-29 08:05:37 by leycec

PEP 695 `type` aliases x 7.

This commit is the next in a commit chain adding support for PEP
695-compliant type aliases (i.e., type hints instantiated by statements
of the form ``type {alias_name} = {alias_value}``, available under
Python ≥ 3.12), en-route to resolving feature request #297 kindly
submitted by the magical rainbow GitHub unicorn @EtaoinWu (Yue Wu).
Specifically, this commit begins brutally applying a hardcore AST
transformation just to force PEP 695 to comply with our will. Will you
just stop sucking it already, PEP 695? PEP 695 as if written by Terry
Pratchett:

> "I didn do nuffin."

(*Ridiculous ridicule invites vectorless invective!*)

---
## [HuskkyQ/react](https://github.com/HuskkyQ/react)@[b6978bc38f...](https://github.com/HuskkyQ/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Friday 2023-12-29 08:22:40 by Andrew Clark

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
## [dcunited001/.emacs.guix](https://github.com/dcunited001/.emacs.guix)@[a432bb7590...](https://github.com/dcunited001/.emacs.guix/commit/a432bb7590e66ae2000a5f6fdf22096ef81c7d97)
#### Friday 2023-12-29 09:42:22 by David Conner

NICE 2 KNOW ABOUT THE SCHEMA STORE FINALLY (... GOD FUCKING DAMMIT)

... i don't want to see this fucking comment everytime i use that snippet... the
total lack of decent documentation on LSP server configuration has probably cost
me hundreds of hours. thanks a lot microsoft! was i supposed to just use vscode?

oh i know! i'll just magically get a job and then around the water cooler,
everyone will tell me the answers? god i fucking hate my life.

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[7399505916...](https://github.com/Drulikar/cmss13/commit/7399505916bc89355516bb853d63b0e7ec3e1612)
#### Friday 2023-12-29 10:05:29 by cuberound

lowers DS sentrygun to 200 from 500 (#5225)

# About the pull request
lowers price of DS installed sentrygun to 200 from 500.

# Explain why it's good for the game

Based on git lense, the cost of 500 points has been fixed for at least 6
years ( from what I understand form the moment the fabricator was
added?). The sentryguns are not worth 500 points at the slightest, from
dozens of rounds of experience I can say that the fire off 20 shots max
before they die ( unless you do some DS hold after hijack, but that
hardly counts). The main issue anyone has with it is when you install 3
of them in south part of DS and I am willing t take suggestions how to
adress this issue, but it is minor one, as xenos never realy have to
fight them as they basicly get to shoot only while marines are pushed
into DS and are about to evac and queen can hijack without getting
anywhere near them ( or can just let marines evac and then take out the
sentryguns with ease after she calls the ship back down). More marines
evacing thanks to sentrguns might make the hijack more enjoyable for
both sides. Also lowering the price will only mean you see sentryguns
installed on ds more often, buying 20 of them will have no bigger effect
then 7.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: DS installed sentrygun price lowered to 200
/:cl:

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [Robbbert/mameui](https://github.com/Robbbert/mameui)@[6557f865fb...](https://github.com/Robbbert/mameui/commit/6557f865fbd6398553f7e469812f3c57ca2379ac)
#### Friday 2023-12-29 11:24:54 by ArcadeShadow

spectrum_cass.xml: Added 112 items (110 working), and replaced one item with a better dump. (#11871)

* Replaced Bloody with a better dump. [Spectrum Computing]
* Removed Bobo (Erbe) as it is a duplicate dump.
* Cleaned up metadata based on information from Spectrum Computing.

New working software list items (spectrum_cass.xml)
--------------------------------------------
Advanced Zombie Survival Lawnmower Simulator [Spectrum Computing]
Adventures of Buratino [Spectrum Computing]
Aknadach [Spectrum Computing]
Aknadach (Softhouse) [Spectrum Computing]
Airborne Ranger (Erbe, two sided tapes) [Spectrum Computing]
Aliens: Neoplasma (v1.3, English, AY sound) [Spectrum Computing]
Aliens: Neoplasma (v1.3, English, Turbo Sound) [ZX Online]
Aliens: Neoplasma (v1.3, Russian, AY sound) [Spectrum Computing]
Aliens: Neoplasma (v1.3, Russian, Turbo Sound) [ZX Online]
Aliens: Neoplasma (v1.3, Spanish, AY sound) [Spectrum Computing]
Aliens: Neoplasma (v1.3, Spanish, Turbo Sound) [Spectrum Computing]
All Hallows: Rise of the Pumpkin [Spectrum Computing]
All Hallows: Rise of the Pumpkin (ULA Plus) [Spectrum Computing]
Alta Tension (Erbe - Serie Leyenda) [Spectrum Computing]
Angel Nieto Pole 500cc (IBSA - Serie Leyenda) [Spectrum Computing]
Autocrash [Spectrum Computing]
Black Lamp [Spectrum Computing]
Bloody Paws [Spectrum Computing]
Bloody Paws (bug fix) [Spectrum Computing]
Bomb Bomb Buster [Spectrum Computing]
Bomb Bomb Buster (first version) [Spectrum Computing]
Bomb Bomb Buster (alt) [Spectrum Computing]
Bomb Bomb Buster (easy version) [Spectrum Computing]
Captain America in the Doom Tube of Dr Megalomann [Spectrum Computing]
Comando Quatro [Spectrum Computing]
Comando Tracer [Spectrum Computing]
Corrupt [Spectrum Computing]
Cosmic Payback [Spectrum Computing]
Crimbo - A Gloop Troops Tale [Spectrum Computing]
Dirty Dozer [Spectrum Computing]
Dizzy III - Fantasy World Dizzy - Extended Edition 2023 (English, mod) [The Dizzy Fansite]
Dizzy III - Fantasy World Dizzy - Extended Edition 2023 (Russian, mod) [The Dizzy Fansite]
Doom (pre-release) [Spectrum Computing]
Doombase (System 4) [Spectrum Computing]
Emilio Butragueño Futbol 2 (large cardboard case) [Spectrum Computing]
Equinox (Erbe, medium case) [Spectrum Computing]
Equinox (Erbe - Serie Leyenda) [Spectrum Computing]
Evil Realm + Bugout [Planeta Sinclair]
Existenz: Crazy Delfox [Spectrum Computing]
Fire Desire [Spectrum Computing]
Fist-Ro Fighter [Spectrum Computing]
Frost Byte (Erbe - Serie Leyenda) [Spectrum Computing]
Funky Fungus Reloaded (English) [World of Spectrum Classic]
Funky Fungus Reloaded (French) [World of Spectrum Classic]
Funky Fungus Reloaded (German) [World of Spectrum Classic]
Funky Fungus Reloaded (Italian) [World of Spectrum Classic]
Funky Fungus Reloaded (Portuguese) [World of Spectrum Classic]
Funky Fungus Reloaded (Spanish) [World of Spectrum Classic]
Get Out of Mars [Spectrum Computing]
Gloop Troops [Spectrum Computing]
Gloop Troops: The Lost Crown [Spectrum Computing]
Hammer Boy [Spectrum Computing]
Impossible Mission (Compulogical) [Spectrum Computing]
Ivan 'Ironman' Stewart's Super Off Road Racer (MCM) [Spectrum Computing]
Jackson City [Spectrum Computing]
Justin [Spectrum Computing]
Justin and The Lost Abbey [Spectrum Computing]
Leaderboard (Erbe) [Spectrum Computing]
Load'N'Run (Italy) N. 6 - Giugno 1984 [Edicola 8 Bit]
Load'N'Run (Italy) N. 7 - Luglio-Agosto 1984 [Edicola 8 Bit]
Load'N'Run (Italy) N. 8 - Settembre 1984 [Edicola 8 Bit]
MagicAble [Spectrum Computing]
Mantronix (Zafi Chip) [Spectrum Computing]
Mapsnatch [Spectrum Computing]
Marie Celeste (Clube Nacional de Aventura, pirate) [Planeta Sinclair]
Marsmare: Alienation [Spectrum Computing]
Mega-Corp [Spectrum Computing]
Metal Man [Spectrum Computing]
Metal Man Reloaded (English) [Spectrum Computing]
Metal Man Reloaded (Czech) [Spectrum Computing]
Metal Man Reloaded (Italian) [Spectrum Computing]
Metal Man Reloaded (Polish) [Spectrum Computing]
Metal Man Reloaded (Russian) [Spectrum Computing]
Metal Man Reloaded (Spanish) [Spectrum Computing]
Metal Man Remixed [Spectrum Computing]
Mr. Hair & The Fly [Spectrum Computing]
Mr. Hair & The Fly (alt) [Lee Stevenson]
Nemesis the Warlock (Erbe) [Spectrum Computing]
Oberon 69 [Spectrum Computing]
Rana Rama [Spectrum Computing]
Robot - The Impossible Mission (QAOP keys) [Spectrum Computing]
Robot - The Impossible Mission (ZXKM keys) [Spectrum Computing]
Rubicon (Rucksack Games) [Spectrum Computing]
Rubicon (Rucksack Games, ULA Plus) [Spectrum Computing]
Schizoids (Nuova Newel) [Planeta Sinclair]
Seraphima (English) [ZOSYA entertainment]
Seraphima (Portuguese) [ZOSYA entertainment]
Seraphima (Russian) [ZOSYA entertainment]
Seraphima (Yandex Retro Games Battle v3 competition) [ZOSYA entertainment]
Simon [Spectrum Computing]
Skull & Crossbones (Dro Soft) [Spectrum Computing]
Sky Runner (Z Cobra) [World of Spectrum]
Souls Remaster [Spectrum Computing]
Space Monsters Meet THE HARDY [Spectrum Computing]
Starring Charlie Chaplin (Erbe) [Spectrum Computing]
Starring Charlie Chaplin (Erbe - Serie Leyenda) [Spectrum Computing]
The Hair-Raising Adventures of Mr. Hair [Spectrum Computing]
The Prayer of the Warrior [Spectrum Computing]
The Prayer of the Warrior (demo) [Spectrum Computing]
The World War Simulator: Part One (English) [Spectrum Computing]
The World War Simulator: Part One (Spanish) [Spectrum Computing]
The World War Simulator: Part II (Spanish) [Spectrum Computing]
Tokyo Gang [Spectrum Computing]
Toyota Celica GT Rally (Dro Soft) [Spectrum Computing]
Tus Juegos №3 [Planeta Sinclair]
W.A.R (Erbe) [Spectrum Computing]
Xarax (Potz Blitz) [Spectrum Computing]
Xecutor (Dro Soft) [World of Spectrum]
Yokai Monk (v1.7) [Spectrum Computing]
Yokai Monk (v1.8) [Spectrum Computing]

New software list items marked not working (spectrum_cass.xml)
--------------------------------------------
Cosmic Debris (ZX Data) [Spectrum Computing]
Zorro (Erbe, medium case) [Spectrum Computing]

---
## [BurgerLUA/Bubberstation](https://github.com/BurgerLUA/Bubberstation)@[8f3d1036c8...](https://github.com/BurgerLUA/Bubberstation/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Friday 2023-12-29 11:45:47 by SkyratBot

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
## [WekufuStudios/WekufuStudios.github.io](https://github.com/WekufuStudios/WekufuStudios.github.io)@[4b83778f0d...](https://github.com/WekufuStudios/WekufuStudios.github.io/commit/4b83778f0db8ba0e8da8c0a736ee5fb1a43638ea)
#### Friday 2023-12-29 11:52:38 by Mateu

Fuck YouTube, videos on the page are from an Indivious instance now

---
## [coatlessali/GLCoreScissors](https://github.com/coatlessali/GLCoreScissors)@[4b6a8dcc65...](https://github.com/coatlessali/GLCoreScissors/commit/4b6a8dcc65f57dc32be5584c1b3421ec283d8d01)
#### Friday 2023-12-29 14:44:26 by coatlessali

Update README.md

coatlessali releases new Stupid Piece of Shit that Doesn't Fucking Work

---
## [an0rak-dev/Avatar](https://github.com/an0rak-dev/Avatar)@[b5e801ca8d...](https://github.com/an0rak-dev/Avatar/commit/b5e801ca8d0dab1ea692f26f119bb1cb2067e4c7)
#### Friday 2023-12-29 15:12:49 by Sylvain Nieuwlandt

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
## [RosSample/massmeta](https://github.com/RosSample/massmeta)@[5f305ca5f7...](https://github.com/RosSample/massmeta/commit/5f305ca5f7b3143360c2107102ea10ad96326839)
#### Friday 2023-12-29 15:25:01 by ATH1909

Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

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

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Jozefwl/beim-shopping-list](https://github.com/Jozefwl/beim-shopping-list)@[dc5ba5ac72...](https://github.com/Jozefwl/beim-shopping-list/commit/dc5ba5ac72a630ae53f8c00300543a32e88b6a71)
#### Friday 2023-12-29 15:38:04 by Jozef W

Unit tests are hard

god save my soul

- Changed a bunch of stuff so it works properly
- Unit tests have helped me understand how shit my code actually is
- I cannot spend time with friends, I must code
- I am literally fainting behind my computer and I have low or high or something with my blood pressure
- Coffee is the only drink i have known for the past seven days
- Where God
- Must unit test

---
## [Honzoraptor31415/CodeConnect](https://github.com/Honzoraptor31415/CodeConnect)@[93c5bb8721...](https://github.com/Honzoraptor31415/CodeConnect/commit/93c5bb8721444a02a72de1d1f037e97301bab3b8)
#### Friday 2023-12-29 16:26:38 by Honzoraptor

Made it cleaner, but it doesn't work now

Added a .env file, which contains the firebase's secret stuff and which is also in the .gitignore. Also instead of document.title = 'smth' I used svelte:head, because idk. Well the auth doesn't work now: in the /signup when I try to create an account, it says 'auth is not defined', but when I define auth by basicly rewriting the whole Firebase.js (which is now btw isn't in the .gitignore), it says some stupid shit like 'two fuckers have the same outpot at node_modules/some-shit'. idk

---
## [catfooo/final-boiler-plate-monorepo](https://github.com/catfooo/final-boiler-plate-monorepo)@[401d22076b...](https://github.com/catfooo/final-boiler-plate-monorepo/commit/401d22076b1355220d97d1d9ffc474856ca4e6c7)
#### Friday 2023-12-29 16:28:42 by So Youn Choi

, and then, friday? cant believe it! anyway, today is today. and i want to move forward. not just gathering lego that ive already heard from somewhere, but using new type of lego, or get new use of it, or... idk. i was just not feeling that today is finished. was not happy today. the place i work, was full of sad people that work because they work. like pushing button in order to extend life. being middle of them, got negative effect from them. not eating properly also, might made me not happy mood. managed to eat on my way home finally. and now its kind of full of energy. not freezing with window open. but this school made me to have routine, and taught me that something very bad might happen if i lose that. so i need to admit that i am a human. but yea, dandelion thing. we wait for light, we wait for spring, we wait for warm. user might experience same for me. old gubbe might came for the user and say, my daughter might need bundle of dandelion for this and that, or might she saw place with full of dandelion at this humid dark cold freezing night. might be dying of severe cold, expecting that god might forgive her... to help being forgived by god, for user itself, also, play a role as being forgived. why the user wandering in the dark? did the user expelled from somewhere? is this experience of almost-dying-moment-of-cold plays as punishment for user itself? from somewhere? why? what happened? and how? how can we go back? how can we go back to where we were? with new dandelion that we gathered from ths journey???

---
## [TheTerBobornator/funkinPhysicsSource](https://github.com/TheTerBobornator/funkinPhysicsSource)@[e17f5f173c...](https://github.com/TheTerBobornator/funkinPhysicsSource/commit/e17f5f173c43eac7408768c9111a52263acd320a)
#### Friday 2023-12-29 16:40:32 by TheTerBobornator

2.0.1 Hotfix yay!!

holy shit what the fuck was i on with the last commit i do not know how github works *help*

anyway this is the hotfix it may or may not be on gamebanana now idk i also just fucked up the repo for here sooo badly jfc i dont know what happened but uh heres the proper thing sorry guys

---
## [SingingSpock/sojourn-station](https://github.com/SingingSpock/sojourn-station)@[762705eff9...](https://github.com/SingingSpock/sojourn-station/commit/762705eff975e6acaed923eb24d1225bc50f9978)
#### Friday 2023-12-29 16:44:01 by CDB

Defib revert (#4891)

* Update defib.dm

This is very likely going to flourish into a whole ream of medical tweaks but for now starting with this because it's been bugging me.

Reverts the defib brainloss revive cap, defibs no longer check your braindamage value as a part of the process of determining if you can be defibb'd.  They only check if you have a brain, a ckey and if you need to be nanopaste'd.

This does mean the bug where you can be revived with a "dead" brain(and thus brought back in an "incomplete" form) is probably back and I'll tackle that shit later since it requires more in depth messing with. I'd like to ask that you fuckers *not* bypass this penalty by running to cryo and then coming right back up.

* Medical map changes

New storage closet for medical in the lower area, includes a lathe with some basic materials,(plus a lethals disk so SLT stop dying when they wrongly choose the bullpip primary.) basic medical disks, recharger, smartfridge(in case you want to put hyperzine away from the main floor.), and wall storage locker.

Relocates many of the most commonly pilfered medical stuff to this single closet. The medkits, defib(which now has a spare cell that actually matches it.)

Also gives medical a couple jars of bare-minimum meds in said closet.

Medical blood-freezer is still in the main area for obvious reasons however it now has access requirements.

Adds a few missing total lockdown shutters for medical.

Moves the medbay-lower break room(the lil tiiny one), adds a new hallway between lower med and lower research - puts the tiny breakroom there.

Medical rejoice, replaces the flimsy thin railings in the substation with reinforced orange railings. Roaches/spiders can no longer just fall down into that little glass area(Though people can still vault it fairly easily.)

Shrinks the medical shower from 4 stalls to 2.

* Revert "Medical map changes"

This reverts commit d62882ece7e0bd141c3347ff0cdbff21b67b052c.

* SLT buffs

SLTs can now select a Humility as their starting main-arm. It comes with the weapon preloaded and one spare cell.

Humility additionally no longer uses large cells, who tfs idea was this? switches it back to medium and lowers the charge cost to 100. No more 40 magazine shotgun jfc.

Gas mask added to SLT locker.

SLTs now begin with a pair of sterile shock gloves, complete with a kinda okay coder sprite. For removing particularly rude people from medical.

Removes the erroneous insulation on the regal gloves.

* HG

* Update stungloves.dm

fixes an incomplete desc.

---
## [SingingSpock/sojourn-station](https://github.com/SingingSpock/sojourn-station)@[3409d0b3ec...](https://github.com/SingingSpock/sojourn-station/commit/3409d0b3ec3ac4c5a8e9bd7a0118581c9749ed51)
#### Friday 2023-12-29 16:44:01 by benj8560

misc map fixes (#4883)

* map stuff

* small touchup

* stuff!

more minor fixes!

Relocates Ians dinner so it's not hiding away inside a closet where he can't enjoy it assumed unintended. Also returns Runtimes food to her from the old map.

Corrects the micromeds in dorms to using offsets rather then being lodged insdie a wall.

Relocates the Turbine cooling chamber blast door button to the GMs storage room and gives it a atmos ID lock for good mesure. Should keep those trainees away from the funny room.

Adds a sec cam I forgot to the new atmos hard storage room.

Moves poly into the GMs breakroom and gives him a few crackers to eat/grab. The stamp is finally free!

* weh

fixes the missing cables preventing the Terminal Lounge from getting power. You know small lounge near the big shuttle pad for ebents.

* buttttton

adds a button to control the shutter for blackshields maint backdoor

---
## [RustWorks/zola-A-fast-static-site-generator](https://github.com/RustWorks/zola-A-fast-static-site-generator)@[e25915b231...](https://github.com/RustWorks/zola-A-fast-static-site-generator/commit/e25915b2315c24bb343a91a55eb92455534ea396)
#### Friday 2023-12-29 16:59:13 by Chris Morgan

Support and default to generating Atom feeds

This includes several breaking changes, but they’re easy to adjust for.

Atom 1.0 is superior to RSS 2.0 in a number of ways, both technical and
legal, though information from the last decade is hard to find.
http://www.intertwingly.net/wiki/pie/Rss20AndAtom10Compared
has some info which is probably still mostly correct.

How do RSS and Atom compare in terms of implementation support? The
impression I get is that proper Atom support in normal content websites
has been universal for over twelve years, but that support in podcasts
was not quite so good, but getting there, over twelve years ago. I have
no more recent facts or figures; no one talks about this stuff these
days. I remember investigating this stuff back in 2011–2013 and coming
to the same conclusion. At that time, I went with Atom on websites and
RSS in podcasts. Now I’d just go full Atom and hang any podcast tools
that don’t support Atom, because Atom’s semantics truly are much better.

In light of all this, I make the bold recommendation to default to Atom.

Nonetheless, for compatibility for existing users, and for those that
have Opinions, I’ve retained the RSS template, so that you can escape
the breaking change easily.

I personally prefer to give feeds a basename that doesn’t mention “Atom”
or “RSS”, e.g. “feed.xml”. I’ll be doing that myself, as I’ll be using
my own template with more Atom features anyway, like author information,
taxonomies and making the title field HTML.

Some notes about the Atom feed template:

- I went with atom.xml rather than something like feed.atom (the .atom
  file format being registered for this purpose by RFC4287) due to lack
  of confidence that it’ll be served with the right MIME type. .xml is a
  safer default.

- It might be nice to get Zola’s version number into the <generator>
  tag. Not for any particularly good reason, y’know. Just picture it:

    <generator uri="https://www.getzola.org/" version="0.10.0">
	Zola
    </generator>

- I’d like to get taxonomies into the feed, but this requires exposing a
  little more info than is currently exposed. I think it’d require
  `TaxonomyConfig` to preferably have a new member `permalink` added
  (which should be equivalent to something like `config.base_url ~ "/" ~
  taxonomy.slug ~ "/"`), and for the feed to get all the taxonomies
  passed into it (`taxonomies: HashMap<String, TaxonomyTerm>`).
  Then, the template could be like this, inside the entry:

    {% for taxonomy, terms in page.taxonomies %}
        {% for term in terms %}
            <category scheme="{{ taxonomies[taxonomy].permalink }}"
		term="{{ term.slug }}" label="{{ term.name }}" />
	{% endfor %}
    {% endfor %}

Other remarks:

- I have added a date field `extra.updated` to my posts and include that
  in the feed; I’ve observed others with a similar field. I believe this
  should be included as an official field. I’m inclined to add author to
  at least config.toml, too, for feeds.
- We need to have a link from the docs to the source of the built-in
  templates, to help people that wish to alter it.

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[b7b0932c4b...](https://github.com/Ical92/tgstation/commit/b7b0932c4b5b3d4f9386b6dce514ee1ba3e25a05)
#### Friday 2023-12-29 17:13:57 by distributivgesetz

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
## [RedSkulHYDRA/frameworks_base](https://github.com/RedSkulHYDRA/frameworks_base)@[7767366495...](https://github.com/RedSkulHYDRA/frameworks_base/commit/776736649598f6886230f4dd561bbdb768352316)
#### Friday 2023-12-29 17:53:22 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [Kkthnx-Wow/LatencyGuard](https://github.com/Kkthnx-Wow/LatencyGuard)@[4a1ece26de...](https://github.com/Kkthnx-Wow/LatencyGuard/commit/4a1ece26dee303ca46362e835308b894e2e5aadd)
#### Friday 2023-12-29 18:09:23 by Kkthnx

🎉 Release: LatencyGuard v1.0 - Dynamic Latency Optimization

🚀 We're excited to announce the release of LatencyGuard v1.0! This version marks a significant milestone in providing a seamless and optimized gameplay experience for World of Warcraft players.

🌟 Key Features:
- 📶 Dynamic Spell Queue Window Adjustment: Automatically adapts to current network latency for optimal performance.
- 🎚️ User-Controlled Settings: Customizable latency threshold and feedback options.
- 💾 Persistent Configuration: Settings are saved and retained across game sessions.
- 📈 Enhanced Gameplay: Reduced lag impact, ensuring smoother and more responsive gameplay.

🔍 This release has undergone thorough testing to ensure reliability and performance. We're committed to continuous improvement and eagerly await your feedback.

🙌 A big thank you to our community for your support and suggestions. Enjoy the enhanced gaming experience with LatencyGuard v1.0!

#WoWAddon #LatencyGuard #GamingExperience

---
## [myrmyxo/cave](https://github.com/myrmyxo/cave)@[5e5e020f84...](https://github.com/myrmyxo/cave/commit/5e5e020f840b206a7eeae930e898df17f33f7f5a)
#### Friday 2023-12-29 18:27:51 by myrmyxo

The Plantening 2 (RT-Plant growth), Oceanning, Gardening, and normal coordinating and dictionaring

LOTS OF SHIT HAS CHANGED !

-------------------------------------------------------------------

Modifications of the "engine" idk :
- the y coordinates have been FLIPPED ! Now, instead of having increasing y from top to bottom, y increase from BOTTOM to TOP like in any normal game like minecrap or turdaria (love these game btw). This should make things easier. For the rendering part, I just flip the bitmap lol, but gravity changed direction for creatures, water, and plants were made to grow the other way too.
- there is no LoadedChunks array anymore, it has been replaced by a DICTIONARY ! This makes stuff WAY more easy to manage like actually. This also made the teleporting water bug DISAPPEAR ! I am so happy with this information.

--------------------------------------------------

Biomes :
-OCEAN BIOME has been added ! This biome (biome index 8) is well, an ocean biome, very blue, that is very particular compared to other biomes : it is SEALED OFF from other biomes by a sort of cell wall at its edge (when ocean biome = around 50%) that is kinda thick and prevents water from leaking out unless players decide to I guess. Terrain generation is very different : instead of the noise value having to be between let's say 120 and 160 for there to be air and if not it's water, now it has to be over like 180. This makes it so there are very big caves spaces, sometimes spanning around the entier biome, which look rad tbh. Because of this, every plant in this biome (unless inside an air-filled structure) is kelp, both ground kelp and ceiling kelp. And almost all entites are fish. However, since its generation works on a threshold basis of the humidity value, obsidian biomes are cut by it and it can look weird. Same for forests and fairy biomes that are often on the edge and thus are cut. Will have to assign a unique noise value to it prolly, should be ok to do.
-Deep cold biome renamed frost biome but who cares honestly

--------------------------------------------

PLANTS ! The big of the update
- Vine plants have been added ! These work like ceiling kelp, except they spawn outside of water, can be LONG (like up to 40 in length), and alternate x/x+1 every 2 tiles instead of 1 tiles like a ceiling kelp. So :
_ _- -_ _- -_ _ - - instead of _-_-_-_-_- but vertical lmfao.
They are made out of plant matter but also possess FLOWERS, that are the shape of a "+", with every tile being a petal except from the center one being pollen tile :
_o_
oxo       - _ = air, o = petal, x = pollen.
_o_
A special black variant spawns in the obsidian biome.
- Some mushrooms dance. This is a bug due to ceiling making them alternate growthlevels but it's funny lmfao.
-PLANTS NOW GROW IN REAL TIME IN A LOGICAL FASHION ! They now have growth levels that increase over time, making the plants taller and taller until it reaches its maximum. it has been made so flowers and branches sprout at the same location at every growth rate so it makes sense. Works nice ! They legit look like they're growing which is super cool. Still gonna improve it to be more efficient and not have to recreate the whole plant at every growth rate test. Plants also will not overlap with terrain and will stop growing if they bump into it (both stems and branches for trees, branches stopping changes nothing but the stem stopping stops everything).
- it is now possible for the player to place EVERY plant that in the game (from their inventory) in a similar fashion to entities. Both plants and entities have subtypes also. Plants are placed at growth rate 0 and grow over time (very fast).
- Plants don't have an ARRAY for their fillstates anymore but a DICTIONARY. The bitmap is made from it and it's (probably) much more efficient this way.
- The saving system is still in .txts and not .json I will work on that now nyehehehehe so plants don't have their growthLevels saved for now (sad) and spawn/respawn ALWAYS at growth level 0 or 1.
- Growth level 0 is plant being invisible now instead of 1 in size. Basically not started growing.

--------------------------------------------------------

LIQUIDS :
- Since oceon biomes were making the whole fucking game lag like crazy due to attemping to move every water tiles at every frame, I added a temporary isStable thing that makes water movement not being tested if no water was moved in or out or inside at that frame. modifications to the chunk will retrigger the chunk, but it doesn't work well and water often floats for a while for no reason. Thus, additionnally the game checks random chunks for water movement but uhhhhh that's not very normal lmfao. Will have to change that.

------------------------------------------

Milcellaneous :
- why the fuck is Knight of Despair in my files what she doing there what
- I added a font for letters, both upper and lowercase, and many symbols like maths, punctuation, brackets/parentheses and shit. Still need to cut that one into a dict for a rendering system. Will prolly make that dict contain numbers as well and write number after string parsing it'll be easier and more efficient prolly that /10 like a dumbass in a for loop lol.

---
## [natjms/njms.ca](https://github.com/natjms/njms.ca)@[06d63315fd...](https://github.com/natjms/njms.ca/commit/06d63315fdabbd269d8b53ab49a3074136364580)
#### Friday 2023-12-29 19:17:14 by njms

Update wording in A leap of faith versus the willingness to Know

I doubt anyone will ever read this; maybe this is just for myself.
I do want the changes to be addressed somewhere, somehow.

I cut out my reading list. Partly, this was because it felt
tangential to the main point I wanted to develop in this section,
which is that you should seek out the voices you were never allowed
to hear. Secondly, when I went back to double check that both of
the authors were "actually white" I rapidly ran into the wall of
"what the fuck does 'actually white' even mean??", as one does.

Judith Butler is Jewish, importantly, something I didn't even realize,
and while I embarrasingly don't know that much about Judaism, I do
have at least one Jewish friend who's complained before about how
being lumped into "whiteness" can erase your Jewish identity. I
didn't want to do this.

Secondly, I didn't like the last few paragraphs. I didn't like how they
were worded. Listing an effectively "extinct" gender identity like that
of the Gala next to two-spirit people felt wrong; I worried that I
might be conveying the idea that the only transness that exists today
is the one produced by the modern, western, LGBT community. So,
I made some edits that I hope clarify that this is not the case.

---
## [Poobslag/turbofat](https://github.com/Poobslag/turbofat)@[bc5c066bf9...](https://github.com/Poobslag/turbofat/commit/bc5c066bf96084d1e590ba0e689429ff1ea0709a)
#### Friday 2023-12-29 19:23:42 by Poobslag

Rebalanced boss levels, '9 lives' levels.

This '9 lives' thing was mostly meant as a silly joke about cats having
nine lives. Now that we're making lives actually matter in career mode,
these levels should just have a normal amount.

Rebalanced, renamed boss levels. Before, boss levels 4 and 6 were things
like "Score $500 in 3 minutes" which were a huge step down from levels
like "Score $500 in 100 lines." I much prefer boss levels being big/epic
things which are longer, harder or with faster-moving pieces.

The boss level 'boss-poki' seems brutal with a score requirement of
$2000. However, ordinary levels like 'Mozzarella Sticks' have a score
requirement of $1100 so it shouldn't be too unusual. It's possible we'll
tweak these all to be easier based on player feedback.

Purged old levels. This includes old boss levels like 'boss-3k' and old
regular levels like 'five_course_meal' which were removed.

---
## [BogCreature/Shiptest](https://github.com/BogCreature/Shiptest)@[40dfaf3734...](https://github.com/BogCreature/Shiptest/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Friday 2023-12-29 19:38:16 by Imaginos16

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Ravendwyr/FrankerFaceZ](https://github.com/Ravendwyr/FrankerFaceZ)@[6e78fd7cab...](https://github.com/Ravendwyr/FrankerFaceZ/commit/6e78fd7caba59e4237853257e2006973c7e3c4ab)
#### Friday 2023-12-29 20:43:24 by SirStendec

4.64.0

This update adds a check that forces users to agree to YouTube's Terms of Service before they are able to view rich embeds for YouTube links. I personally do not agree with this, but we were required to implement this in order to maintain access to YouTube's API. Actually, they said "API Clients must state in their own terms of use that, by using those API Clients, users are agreeing to be bound by the YouTube Terms of Service." but that's obviously ridiculous for this use case. This is my compromise. Sorry for the inconvenience, everyone. This also comes with aesthetic tweaks to make YouTube's compliance team happy. Woo...

* Added: Setting to display labels on highlighted chat messages giving the reason why the message was highlighted.
* Added: System to force users to agree to a service's Terms of Service before displaying rich content from specific providers. So far this is only used by YouTube.
* Changed: Made the background of highlighted words in chat messages slightly smaller.
* Fixed: A few page elements in mod view not being themed correctly.
* Fixed: Timestamps displaying with an hour when they obviously do not need to.
* API Added: `main_menu:open` event for a general way to open the main menu.
* API Added: Settings UI elements using components using the `provider-mixin` can now override the provider key they use by setting an `override_setting` value on their definition.
* API Changed: The `chat.addHighlightReason(key, data, label)` method now takes an optional `label` parameter to set the text that appears on chat messages when the setting to display labels is enabled.

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[f717155e32...](https://github.com/Foundation-19/Foundation-19/commit/f717155e32508fd2f2ef5e781b93f0996391fa0e)
#### Friday 2023-12-29 20:58:52 by cheesePizza2

Removes old control room + mapping improvements (#1407)

* mapping is fun!

* fuck you

* there is a ghost in my computer that is reverting my changes before i can commit them

* fixes

* fuckyou

* trigger Github actions

---
## [Thera-Pissed/Shiptest](https://github.com/Thera-Pissed/Shiptest)@[da4c03da8f...](https://github.com/Thera-Pissed/Shiptest/commit/da4c03da8f9f95952acba2e0d2a236c297fed2d3)
#### Friday 2023-12-29 21:05:41 by zevo

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
## [cowprotocol/services](https://github.com/cowprotocol/services)@[1fe4c4485a...](https://github.com/cowprotocol/services/commit/1fe4c4485a2d5d8a557ff663a5163c9d83f9ec25)
#### Friday 2023-12-29 21:08:32 by Martin Beckmann

Reduce memory consumption of `RecentBlockCache` (#2102)

# Description
Our `RecentBlockCache` works like this:
1. somebody requests liquidity
2. cache checks if it's already known
3. if it's not in the cache query the blockchain
4. store in cache
5. remember requested liquidity source for updating it in the background

Whenever we see a new block we fetch the current liquidity for all the
liquidity sources and write them to the cache together with their block.
We have a max cache duration. Whenever the cached state exceeds that
duration we remove the oldest entries.

This implementation uses unnecessarily much memory in 2 ways:
1. We can fetch liquidity for quotes. For those requests it's okay to
return liquidity that is not 100% up-to-date. However, we still remember
the requested liquidity source for future updates. This is not great
because we can receive quote requests for all sorts of random tokens
we'll never see again.
2. We cache state for the same liquidity source for multiple blocks. But
the cache only has 2 access patterns:
    * "Give me the most recent available on the blockchain"
    * "Give me the most recent available in the cache"
There is no access pattern "Give me cached liquidity specifically from
an older block with number X"
That means it's enough to keep the most recent data for any liquidity
pool cached at any point.
    
We can see these 2 things at play with this
[log](https://production-6de61f.kb.eu-central-1.aws.cloud.es.io/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'2023-11-28T16:18:27.243Z',to:'2023-11-28T17:55:08.577Z'))&_a=(columns:!(log),filters:!(),grid:(columns:('@timestamp':(width:164))),index:c0e240e0-d9b3-11ed-b0e6-e361adffce0b,interval:auto,query:(language:kuery,query:'mainnet%20and%20driver%20and%20(log:%20%22the%20cache%20now%20contains%20entries%22%20or%20log:%20%22fetched%20liquidity%20sources%22)'),sort:!(!('@timestamp',desc)))).
After ~1h of operation it shows a single `RecentBlockCache` holding ~20K
items. On an average auction we can fetch ~800 uni v2 sources. We
currently have a configuration where we cache up to 10 blocks worth of
data. Meaning we have roughly 8K cache entries for liquidity that is
needed in auction and 12K entries that's only needed for quotes.
Also this is only for a single univ2 like liquidity source. In total we
have 4 different ones configured in our backend.

# Changes
We address `1` by not remembering liquidity sources for background
updates for quote requests.
We address `2` by throwing away all the duplicated data.

## How to test
I did a manual set up where I run an autopilot locally in shadow mode
(fetch auction from prod mainnet) and a driver with all liquidity
sources enabled.
I collected 3 graphs in total to measure the impact of this change on
the memory.
1. This graph is the status quo (very noisy and not really reproducable
across runs)
<img width="1617" alt="0_current_no_optimizations"
src="https://github.com/cowprotocol/services/assets/19190235/0997b34f-8f30-43c4-a797-5e3cf7bccbbf">

2. This graph applies one optimization that is not part of this PR to
make the memory consumption more predictable across runs. I want to
merge that optimization as well but right now it's very hacky. However,
I will include this optimization in all my graphs because it makes the
impact of each optimization easier to spot.
<img width="1420" alt="1_with_univ2_call_optimization"
src="https://github.com/cowprotocol/services/assets/19190235/6f259fa4-4fcd-45dd-ba37-160962065ab3">

3. The effects of this PR's optimization. The memory usage is more
stable over all and grows less over time.
<img width="1607" alt="2_cache_eviction"
src="https://github.com/cowprotocol/services/assets/19190235/ec5b5712-e4e3-4c4e-8feb-dc46e2cfa3f3">

---
## [Cthulhu80/cmss13](https://github.com/Cthulhu80/cmss13)@[fa754d7a7f...](https://github.com/Cthulhu80/cmss13/commit/fa754d7a7f71e0a10b8b424037cf344d82d653b0)
#### Friday 2023-12-29 21:59:22 by InsaneRed

Fixes synths being unlungeable while in "critical state" (#5303)

# About the pull request

Synths were given immunity to dragging from old code back when they
could go into 'crit' so they dont get dragged to hell, however they no
longer have a crit state but still keep the immunity lunges also do not
work because of this. this is not intended.

# Explain why it's good for the game

bugfix


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>
yeah i tested it also no you cant get dragged while dead

</details>


# Changelog
:cl:
fix: Synths are no longer immune to lunges / dragging while in 'critical
state' since they dont go into crit.
/:cl:

Co-authored-by: InsaneRed <prodexter31@outlook.comm>

---
## [kawoppi/froggystation](https://github.com/kawoppi/froggystation)@[66b8b1d866...](https://github.com/kawoppi/froggystation/commit/66b8b1d8669379eac50fa358a3eb5e7707b46f25)
#### Friday 2023-12-29 22:18:41 by Fikou

Revert "if you die in a mech you are ejected" (#79768)

Reverts tgstation/tgstation#79380
this is literally what the mech removal tool is for. gameplay reasons
for that tool missing do not mean that we need to remove its use - if
you want a better solution then let people purchase it... or just smash
the mech- you saving their life and them being sad about their mech is
really funny
the original pr being marked as qol when that was a specific balance
change is very stupid

## Changelog
🆑
del: if you die in a mech you again don't automatically eject
/🆑

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[acc17d5cdf...](https://github.com/RustingWithYou/Aurora.3/commit/acc17d5cdf8de4369524645005976e8025edbd11)
#### Friday 2023-12-29 22:20:15 by RustingWithYou

Uueoa-Esa Sector

stonks

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

merchant guild camp

guwandi

gawgaryn and katas

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

merchant guild camp

gawgaryn and katas

hegemony base

oasis clans

vihnmes tweak

ruined wasteland village

siakh and izweski outpost

izweski outpost fix

vihnmes tweaks and baseturf tweaks

vihnmes spawner fix

flag fixes

ozeuoi fixes

thakh and skakh sites

reclaimers, bugs and martial artists

bug lighting fix/start of ouerea

ouerea versions of bar, village and heph facility

ouerea, functional edition

aut'akh compound and hegemony base

autakh books

fishing league farm

bunch of generic ruins

bunch more sites

uncomments

genericifies plantspawner

pid away sites

skrell and sol away sites for ouerea

fixes hegemony base path

unexploded nuclear bomb

moghes memorial and sky behemoth wreckage

heph planetary mining station

miners guild outpost

guild mining camps on moghes and ouerea

replaces random gun with random civgun

welcome messages and siakh fixes

siakh area change

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

ouerea versions of bar, village and heph facility

aut'akh compound and hegemony base

bunch more sites

uncomments

genericifies plantspawner

skrell and sol away sites for ouerea

fixes hegemony base path

moghes memorial and sky behemoth wreckage

plant spawners, fixing banned ruins and broken ghostroles

thakh seeds

fixes thakh pilgrim spawn

fixes seed packet spawn and cargo price coeffs

written languages

paper fixes

klax scrubbers to stop vhoron vhires

updates miners guild stuff now the station is merged

indent fix

fixes atmos generation that i broke

ruin banning and literal bug fixes

solarian asteroid ruin

sol asteroid ruin 2: electric boogaloo

sol aseroid tweak

ouerea nt ruin

aaa
omgolo fixes

tret fake planet

engi stuff

ouerea flags

ouerean revolution memorial

a BUNCH of changes

terrain tweaks

Revert "terrain tweaks"

This reverts commit 8a961212d968afb1daa6d381a0786850c2626e73.

sandbike stuff

ihss reclamation 1

ihss reclamation 2

ihss reclamation 3

ihss reclamation 4

ihss reclamation 5

ihss relamation 6

ihss reclamation final tweaks

welcome messages that were missing

3/4 1

colors

access

dorviza limbs & mikuetz languages

hephaestus bans

ouerea ghostrole tweaks

wasteland radiation + fixes

rifles & geigers

fuck you, no lights

hegemony visitor event

more fedship

freewater & caligae fixes

ouerea battlefield

yet more fedship

feuahfiehg

fedship & map fixes

reclamation fixes & warblers

names & fluff

no more dead bug storage

fedbrained

access changes

flag

existing ships can spawn in uwu

the 3/4ing

area flags

fuck this event

skakhpilled and priestcore

airlock update

ihss airlocks

better plant code

yeah

overmap site updates

ert

access fixes and dead guwandi storage

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[4f1e976048...](https://github.com/RustingWithYou/Aurora.3/commit/4f1e9760481d760b6bcbdc2149b872158e3f1429)
#### Friday 2023-12-29 22:24:38 by RustingWithYou

kaneyama power station

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

glowing screen: you should kill yourself, now

light

kaneyama map

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

glowing screen: you should kill yourself, now

kaneyama map

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

bridge & icons

shuttl

grass

spawnroom

byeah

checkpoints

sovl

CONTENT

plant

da files

icons & assets

byeah

big hivebot icon

ecd

messages

ECD as easy as 1-2-3

a bunch of shit

TREES

grass

areas

byeah

guns

title screen

ambience

rain & water

ligt

power

also apc fixes

tcomms fix

ecd

spooking the synthetics & slowdown

fuck you, point verdant

area check works

byeah

---
## [someone58198186911/TuxOwner.cc](https://github.com/someone58198186911/TuxOwner.cc)@[ce0754ccc9...](https://github.com/someone58198186911/TuxOwner.cc/commit/ce0754ccc9b79b2af8b460703664fc8a9c5a5046)
#### Friday 2023-12-29 22:29:25 by someone58198186911

yes i stole this shit from 8dcc's tf2 cheat. shut up lol

---
## [Sorrowfulwinds/Shadowcat-Baps-Your-Code](https://github.com/Sorrowfulwinds/Shadowcat-Baps-Your-Code)@[33cae266af...](https://github.com/Sorrowfulwinds/Shadowcat-Baps-Your-Code/commit/33cae266af864b22c509f65ffff3ad7277bbb459)
#### Friday 2023-12-29 22:58:15 by Captain277

Subtypes Corporate Crates, Fixes Mapped Biohazard Crate, Renames Advanced Voidsuit (#6126)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. *Fixes Bug With Corporate Crates, Subtypes Them.*
2. *Removes Varedited Biohazard Bin and Places Normal Biohazard Bin.*
3. *Changes Advanced Voidsuit Name to Advanced Hardsuit.*

## Why It's Good For The Game

1. _I received reports of one specific corporate crate not rendering
properly when opened. As I inspected it, I realized it would be more
efficient to subtype all corporate crates, so I did that. HOWEVER, this
did not repair the initial bug. For some reason the crate was not
rendering its 'aethersecureopen' state, even though all variables and
code seemed to be working properly. No other crate exhibited this issue.
I discovered that by changing the name of the icon state from
'aethersecureopen' to 'aethersecopen', the state began to enforce and
render properly. I suspected it might be a name length issue, but tests
with other equally long icon states in the crate section disproved this
theory. This may warrant further investigation._
2. _This one avoided detection during my initial sweep through. Can't
remember who just went in and tried to varedit bins to fix biohazards,
but hopefully this is the last one they touched._
3. _This has been driving me crazy for a few days, and yesterday
especially. The Advanced Voidsuit is clearly misnamed, as it is in fact
a Hardsuit. When I tried to order these yesterday I overlooked this
cargo entry twice because I was looking for a hardsuit, not a voidsuit.
This just fixes the name._

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
add: Adds Corporate Crate Subtype, Reassigns Corporate Crates to It.
fix: Fixes incorrectly mapped biohazard bin.
tweak: Changes Name: Advanced Voidsuit to Advanced Hardsuit.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [TheParasiteProject/frameworks_base](https://github.com/TheParasiteProject/frameworks_base)@[8f552bfa93...](https://github.com/TheParasiteProject/frameworks_base/commit/8f552bfa93b47e2b457f18377e6e923275f4e5f8)
#### Friday 2023-12-29 23:12:45 by Kuba Wojciechowski

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
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[8893f847a0...](https://github.com/PlagueVonKarma/kep-hack/commit/8893f847a0d83fc3c535838530916e3b909178f6)
#### Friday 2023-12-29 23:21:45 by Martha Schilling

HAHAHA FUCK YOU YUJIROU

WE WIN

PRAISE BE TO RAINBOW METAL PIGEON, OH MY GOD

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b72f7329e1...](https://github.com/tgstation/tgstation/commit/b72f7329e1d9be1da7299a78e8b895acbd1927fc)
#### Friday 2023-12-29 23:52:45 by jimmyl

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

