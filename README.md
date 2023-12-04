## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-03](docs/good-messages/2023/2023-12-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 6,960,375 were push events containing 7,459,453 commit messages that amount to 190,436,532 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [newren/git](https://github.com/newren/git)@[859e88dcde...](https://github.com/newren/git/commit/859e88dcde553c0f82c6581364ee0c156ca01b15)
#### Sunday 2023-12-03 00:29:19 by Elijah Newren

completion: avoid user confusion in non-cone mode

It is tempting to think of "files and directories" of the current
directory as valid inputs to the add and set subcommands of git
sparse-checkout.  However, in non-cone mode, they often aren't and using
them as potential completions leads to *many* forms of confusion:

Issue #1. It provides the *wrong* files and directories.

For
    git sparse-checkout add
we always want to add files and directories not currently in our sparse
checkout, which means we want file and directories not currently present
in the current working tree.  Providing the files and directories
currently present is thus always wrong.

For
    git sparse-checkout set
we have a similar problem except in the subset of cases where we are
trying to narrow our checkout to a strict subset of what we already
have.  That is not a very common scenario, especially since it often
does not even happen to be true for the first use of the command; for
years we required users to create a sparse-checkout via
    git sparse-checkout init
    git sparse-checkout set <args...>
(or use a clone option that did the init step for you at clone time).
The init command creates a minimal sparse-checkout with just the
top-level directory present, meaning the set command has to be used to
expand the checkout.  Thus, only in a special and perhaps unusual cases
would any of the suggestions from normal file and directory completion
be appropriate.

Issue #2: Suggesting patterns that lead to warnings is unfriendly.

If the user specifies any regular file and omits the leading '/', then
the sparse-checkout command will warn the user that their command is
problematic and suggest they use a leading slash instead.

Issue #3: Completion gets confused by leading '/', and provides wrong paths.

Users often want to anchor their patterns to the toplevel of the
repository, especially when listing individual files.  There are a
number of reasons for this, but notably even sparse-checkout encourages
them to do so (as noted above).  However, if users do so (via adding a
leading '/' to their pattern), then bash completion will interpret the
leading slash not as a request for a path at the toplevel of the
repository, but as a request for a path at the root of the filesytem.
That means at best that completion cannot help with such paths, and if
it does find any completions, they are almost guaranteed to be wrong.

Issue #4: Suggesting invalid patterns from subdirectories is unfriendly.

There is no per-directory equivalent to .gitignore with
sparse-checkouts.  There is only a single worktree-global
$GIT_DIR/info/sparse-checkout file.  As such, paths to files must be
specified relative to the toplevel of a repository.  Providing
suggestions of paths that are relative to the current working directory,
as bash completion defaults to, is wrong when the current working
directory is not the worktree toplevel directory.

Issue #5: Paths with special characters will be interpreted incorrectly

The entries in the sparse-checkout file are patterns, not paths.  While
most paths also qualify as patterns (though even in such cases it would
be better for users to not use them directly but prefix them with a
leading '/'), there are a variety of special characters that would need
special escaping beyond the normal shell escaping: '*', '?', '\', '[',
']', and any leading '#' or '!'.  If completion suggests any such paths,
users will likely expect them to be treated as an exact path rather than
as a pattern that might match some number of files other than 1.

However, despite the first four issues, we can note that _if_ users are
using tab completion, then they are probably trying to specify a path in
the index.  As such, we transform their argument into a top-level-rooted
pattern that matches such a file.  For example, if they type:
   git sparse-checkout add Make<TAB>
we could "complete" to
   git sparse-checkout add /Makefile
or, if they ran from the Documentation/technical/ subdirectory:
   git sparse-checkout add m<TAB>
we could "complete" it to:
   git sparse-checkout add /Documentation/technical/multi-pack-index.txt
Note in both cases I use "complete" in quotes, because we actually add
characters both before and after the argument in question, so we are
kind of abusing "bash completions" to be "bash completions AND
beginnings".

The fifth issue is a bit stickier, especially when you consider that we
not only need to deal with escaping issues because of special meanings
of patterns in sparse-checkout & gitignore files, but also that we need
to consider escaping issues due to ls-files needing to sometimes quote
or escape characters, and because the shell needs to escape some
characters.  The multiple interacting forms of escaping could get ugly;
this patch makes no attempt to do so and simply documents that we
decided to not deal with those corner cases for now but at least get the
common cases right.

Signed-off-by: Elijah Newren <newren@gmail.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[41026ae8b1...](https://github.com/Paxilmaniac/Skyrat-tg/commit/41026ae8b1a14b9380ca7af9885939c9f2dc060e)
#### Sunday 2023-12-03 00:30:27 by SkyratBot

[MIRROR] Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun [MDB IGNORE] (#25365)

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

## About The Pull Request
One of the "monkey cubes" in Birdshot's tool storage was actually a
gorilla cube. This was funny up until people realized it was a thing and
now people are using it intentionally to grief. I'd rather not.

It's a different cube now. I don't want to spoil it but it won't kill
anyone, just make people laugh.

I added a different fun item to another tile in tool storage. Again, no
spoilers, read the code if you really want to know what it was.

## Why It's Good For The Game
I like the "cube says it's a monkey but it's not" joke. It was funny
when people thought it was a monkey, used it, and got killed by it.
Problem is, people know what it is now and have used it for grief
purposes, so we can't have nice things. Gorillas are stupid hard to kill
and will de-limb people by looking at them.

I wanted to add something else fun to replace it that isn't just the
exact same joke but now it won't kill you, so I did.

## Changelog
:cl: Vekter
del: Replaced the "monkey cube" in Birdshot's tool storage with a
different "monkey cube".
add: Added a fun surprise item to Birdshot's tool storage to compensate
for the above change.
/:cl:

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [zuu95/app-dev](https://github.com/zuu95/app-dev)@[2d1bb9d55c...](https://github.com/zuu95/app-dev/commit/2d1bb9d55c097675e58db9bed0d7a7026062d0c8)
#### Sunday 2023-12-03 01:13:09 by zuu95

Update README.md

These movies and series are the last ones that I recently watched.
Movies
Gangnam Blues 
Gangnam Blues is a riveting South Korean crime film set against the backdrop of Seoul's Gangnam district. Its intense storyline and compelling characters make it a must-watch.
The Wolf of Wall Street 
Directed by Martin Scorsese, The Wolf of Wall Street is a wild ride through the world of excess and finance, featuring Leonardo DiCaprio's unforgettable performance as Jordan Belfort.
Margin Call 
Margin Call provides a gripping look into the high-stakes world of investment banking during the 2008 financial crisis. The stellar cast and taut storytelling make it a standout in the genre.
Series 
Tom and Jerry
Tom and Jerry, the classic cat-and-mouse duo, never fails to bring laughter. The timeless antics of these two animated characters have made it a cherished series for generations.
Dora The Explorer 
Join Dora and her monkey friend Boots on exciting adventures! Dora the Explorer combines education with fun, making it an ideal series for children and a nostalgic favorite for many.
Oggy and the Cockroaches
Oggy and the Cockroaches is a hilarious animated series that follows the constant battle between Oggy, a laid-back cat, and three mischievous cockroaches. The slapstick humor and clever storytelling make it a joy to watch.

---
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[9ff9e4b9a8...](https://github.com/RigglePrime/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Sunday 2023-12-03 01:17:35 by necromanceranne

Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

## About The Pull Request

Allows for damage falloff to apply to more than just shotgun pellets.
Now any projectile can have a damage falloff defined.

Scatter Laser shells no longer use the minigun beams to determine their
damage. Instead they use the actually defined scatter laser beams. Those
beams do 7.5 damage per pellet, times by 6 pellets.

Scatter laser beams now have damage falloff, a separately defined
(positive) wounding power from normal beams, and wound falloff.

Scatter laser shells can be printed from security protolathes once you
have weapon tech.

Scatter laser shells _may_ be damaged by EMPs based on severity. The
result is that it fires a practically useless volley of laser fire. They
cause a honk sound when they hit, so you know when you've shot one of
these.

## Why It's Good For The Game

Well, we want shotguns universally to not be defined by their damage
output (especially extreme damage output) but by niche.

What does the scatter laser shell currently occupy as a niche?

The single highest damage output of any projectile weapon in direct
damage. The thing we don't want of shotguns, and it is reigning champion
of all guns.

Okay, that's a bit misleading, because obviously it is competing with
the likes of .50 BMG which does 70 damage outright and dismembers limbs,
potentially doing upwards of 90 damage if it does, and also hard stuns
people. Obviously _that_ is technically a stronger bullet.

But not for raw damage, because the scatter laser does 90 damage out the
gate, barring any potential wounding that might occur which increases
the damage multiplicatively. No gimmicks, no extra procs, nothing. It's
just 15 force lasers (with no damage dropoff) split between 6 beams.

And the reason for this is because this shell has been nerfed once prior
by making it not fire 6 normal laser shots into someone. That was 120
damage at the time, 120 to 90 was...I guess a nerf during the taser era.
Depends on how you viewed it. Buckshot was doing like 80 at the time,
believe me it was a wild period. But anyway, when we did the whole
damage rearrangement over the course of the laser few years, every other
shell got touched except this one for some reason. Even pulse slugs lost
10 damage while this was still sitting on 90 force point blank.

So what is the new niche? Well, it's laser buckshot. That's not a niche
but crew don't get buckshot, so this is their buckshot. It wounds real
good. Real goddamn good. And its is a laser. It fits the aesthetic,
obviously.

Okay, thanks.

## Changelog
:cl:
balance: Scatter laser shells actually utilize the _real_ scatter laser
beam. This comes with damage changes. And wounding power.
feature: EMPs can potentially damage scatter laser shells.
refactor: All projectiles can now have damage falloff defined. Yay.
balance: Scatter laser shells can be printed when weapons technology is
researched.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[071f6063e6...](https://github.com/RigglePrime/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Sunday 2023-12-03 01:17:35 by carlarctg

Adds charges to omens and omen smiting. Reduces omen bad luck if nobody's nearby. (#78899)

## About The Pull Request

refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.

qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)

fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.

## Why It's Good For The Game

> refactor: Adds charges to omens and omen smiting rather than only
being permanent or one-use. Mirrors now grant seven bad luckers.

Allows for someone to get between 1-infinity omen accidents. Seriously
why wasnt this a thing before

> qol: Reduces omen bad luck if nobody's nearby.

I LOVE this quirk, but trying to do antything at all except 'Suffer
Miserably' is nigh impossible. To alleviate life a little, making it so
that you have a lesser chance of suffering misfortune if nobody's around
will be the perfect compromise. It makes life easier but doesn't
compromise funny moments.

Any client in viewrange will disable the reduction. This includes
ghosts.

## Changelog

:cl:
refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.
qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)
fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[b65f729901...](https://github.com/RigglePrime/tgstation/commit/b65f729901fdb342b832fb3365d72afd076f8c3b)
#### Sunday 2023-12-03 01:17:35 by lizardqueenlexi

Nanotrasen basic mobs. (#78917)

## About The Pull Request

First and foremost, converts all Nanotrasen simplemobs into basic mobs.

To avoid messy and redundant code, or god forbid, making Nanotrasen mobs
a subtype of Syndicate ones, I've made Syndicate, Russian, and
Nanotrasen mobs all share a unified "Trooper" parent. This should have
no effect on their behaviors, but makes things much easier to extend
further in the future.

While most of this PR is pretty cut-and-dry, I've done a couple notable
things. For one, all types of ranged trooper will now avoid friendly
fire, instead of shooting their friends in the back. Even the Russians
have trigger discipline.

I've also created a new AI subtree that allows mobs to call for
reinforcements. I've hopefully made this easy to extend, but the
existing version works as follows:

- A mob with this subtree that gains a target that is also a mob will
call out to all mobs within 15 tiles.
- If they share a faction, mobs receiving the call will have the target
added to their retaliate list, and have a new key set targeting the
calling mob.
- If they have the correct subtree in their AI controller, called-to
mobs will then run over to help out.

Sadly, this behavior is currently used only by a few completely unused
Nanotrasen mobs, so in practice it will not yet be seen.

Finally, I've fixed a minor issue where melee Russian mobs punch people
to death despite holding a knife. They now use the proper effects for
stabbing instead of punching.
## Why It's Good For The Game

Removes 8 more simple animals from the list.

As said above, making all "trooper" type mobs share a common parent cuts
down on code reuse, ensures consistency of behavior, and makes it much
easier to add new troopers not affiliated with these groups. I expect
that I'll make pirates share this same parent next.

The new "reinforcements" behavior, though extremely powerful, opens up
exciting new opportunities in the future. There aren't many existing
behaviors that allow basic mobs to work _together_ in interesting ways,
and I think adding some enemy teamwork could be fun.
## Changelog
:cl:
refactor: Hostile Nanotrasen mobs now use the basic mob framework. This
should make them a little smarter and more dangerous. Please report any
bugs.
fix: Russian mobs will now actually use those knives they're holding.
/:cl:

---
## [bjornbytes/lovr](https://github.com/bjornbytes/lovr)@[fbae4d1961...](https://github.com/bjornbytes/lovr/commit/fbae4d19610919e877a8ed9b3955d6ce9b83fd64)
#### Sunday 2023-12-03 01:19:49 by bjorn

Fix possible crash with Font:getLines and Pass:text;

- Font:getLines/Pass:text use temp memory for strings/vertices.
- Due to the recent morgue fix, resizing the atlas will now do a GPU
  submit to flush the transfers before destroying the atlas.
- This GPU submit also rewinds the temp allocator, invalidating the
  temp memory used for the lines/vertices, causing a use-after-free.

There are 2 changes here:

- Only flush transfers if the destroyed resource actually has pending
  work (we're already tracking this w/ lastTransferRead/Write).
- Restore the allocator cursor after doing the submit.

Having to restore the allocator offset is kinda tricky/complicated,
which sucks.  Other solutions might be:

- Avoid using temp memory in those Font methods.  More generally, adopt
  a rule where you can't use temp memory if it's possible that there
  will be a submit while you're using the temp memory.
- Find some way to stop destroying the old font atlas during a resize?
- Don't rewind the temp allocator on every GPU submit.  Instead only
  rewind it at the end of a frame, or only when Lua does the submit.

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[be24b429c0...](https://github.com/KenAdeniji/WordEngineering/commit/be24b429c0d25aa004899ded861965034557901e)
#### Sunday 2023-12-03 01:32:38 by Ken Adeniji

							<a
								href="http://e-comfort.ephraimtech.com/WordEngineering/WordUnion/GetAPage.html?word=You%20must%20still%20get%20directive%20from%20God...as%20making%20you%3F"
								data-HisWordID="158874"
								data-ContactID="774"
								data-Commentary="You must still know...out of your life."
								data-Location="Bedroom: After rinsing ass with left palm and water"
								data-url="google.com/books/edition/Shoe_Dog/wO3PCgAAQBAJ?hl=en&gbpv=0"
								datetime="2023-12-02T17:14:00"
							>
								You must still get directive from God...as making you?
							</a>

---
## [tiluuta/LAspots](https://github.com/tiluuta/LAspots)@[4d01fd6a7d...](https://github.com/tiluuta/LAspots/commit/4d01fd6a7d9fdf55c84bc9ef1c5bb25ceb48e707)
#### Sunday 2023-12-03 02:43:10 by Khalil Mayden

randomize shit

fucking hell this is SO FUCKING ANNOYING AHHHH WHY IS THERE DETAILS ERROR NOW

---
## [TheBronJameOffical/lobotomy-corp13](https://github.com/TheBronJameOffical/lobotomy-corp13)@[07a5135fd3...](https://github.com/TheBronJameOffical/lobotomy-corp13/commit/07a5135fd31c40f7928d39721fc3d7425e551682)
#### Sunday 2023-12-03 03:28:19 by The Bron Jame Offical

Carbon Claw (#1646)

new content babey

i ahve made a severe lapse in my judgement and I do not expect to be forgiven. yadda yadda something reaping what i've sown something

Claw stuff

Claw sounds

CLAW ARMORRRRRRR

claw antag

please work

some of egors fixes

visual updates

new antag things

justice mod

fuckin, 1 god damn character change

Spans and rebase

more changes

what the hell

what the hell!!!!!

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[b5e095e380...](https://github.com/ReturnToZender/ReturnsBubber/commit/b5e095e380e729793628d254bb441f51ecdb046b)
#### Sunday 2023-12-03 04:00:12 by Waterpig

[MODULAR] Refactors (hopefully) all borg modular changes into one module, adds raptor borgs (#777)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Originally I was supposed to only add raptor borgs, but I am simply too
insane to let this shitcode slide.

Moves most if not all borg modular changes into one module folder
because by god these were spread out over like 8 files.
Improves modularity a bit by moving some borg related bubber edits on
skyrat into our modular files.
Adds raptor borgs

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Modularity good.
Code organizing good.

https://en.wikipedia.org/wiki/Technical_debt

Also new borg sprites are cool, I guess. See icondiff bot for those
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
image: New borg sprites: Raptor
refactor: Moved most if not all bubber borg code into one modular folder
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

---
## [The-Web-Imagineers/Microsoft-Edge-browser](https://github.com/The-Web-Imagineers/Microsoft-Edge-browser)@[1224662a98...](https://github.com/The-Web-Imagineers/Microsoft-Edge-browser/commit/1224662a982d3151b7dfabdcc027d68f17447ee3)
#### Sunday 2023-12-03 04:15:07 by Victor Keenom

Update The Evolution of Internet Explorer

A readme.md file is a text file that contains information about a project, such as its description, features, installation, usage, license, and contributors. It is usually written in Markdown, a lightweight markup language that allows you to format text using simple syntax.

To generate a readme.md file, you can follow these steps:

1. **Create a new file**: In your GitHub repository, click on "Add file" and then "Create new file". Name the file "readme.md" and make sure it is in the root directory of your project.
2. **Write the content**: Use Markdown syntax to write the content of your readme.md file. You can use headings, lists, tables, code blocks, links, images, and other elements to make your file informative and attractive. You can also use emojis to add some personality to your file.
3. **Preview and save**: Before saving your file, you can preview how it will look on GitHub by clicking on the "Preview" tab at the top of the editor. If you are satisfied with your file, click on "Commit new file" at the bottom of the page.

Here is an example of a readme.md file for a fictional project called Next Horizon:

# Next Horizon

Next Horizon is a web app that helps you unleash your potential by providing you with personalized insights, tips, and resources based on your goals and interests.

![Screenshot of Next Horizon]

## Features

- **Set your goals**: Choose from a variety of categories, such as health, education, career, and hobbies, and set your specific goals for each one.
- **Track your progress**: See how far you have come and how much you have left to achieve your goals. Get feedback and encouragement along the way.
- **Learn new skills**: Discover new skills that can help you reach your goals faster and easier. Watch videos, read articles, and take quizzes to learn from experts and peers.
- **Connect with others**: Join a community of like-minded people who share your goals and interests. Chat, collaborate, and exchange ideas with them.

## Installation

To install Next Horizon, you need to have Node.js and npm installed on your computer. Then, follow these steps:

1. **Clone the repository**: Run the following command in your terminal to clone the Next Horizon repository:

```bash
git clone https://github.com/next-horizon/next-horizon.git
```

2. **Install the dependencies**: Navigate to the project directory and run the following command to install the required packages:

```bash
npm install
```

3. **Start the server**: Run the following command to start the server on your local machine:

```bash
npm start
```

4. **Open the app**: Open your browser and go to http://localhost:3000 to see the app in action.

## Usage

To use Next Horizon, you need to create an account and log in. Then, you can:

- **Create your profile**: Fill in your name, email, and password, and choose your avatar and background image.
- **Select your goals**: Browse through the categories and select the goals that you want to pursue. You can also create your own custom goals.
- **View your dashboard**: See your goals, progress, skills, and community on your dashboard. You can also access your settings and notifications from here.
- **Explore the app**: Click on any of the icons on your dashboard to access the corresponding features. You can also use the search bar to find specific topics or users.

## License

Next Horizon is licensed under the MIT License. See the [LICENSE] file for more details.

## Contributors

Next Horizon is developed by a team of passionate developers who want to help people achieve their dreams. Here are the contributors:

- **Alice**: Alice is the project manager and the lead developer of Next Horizon. She is responsible for overseeing the development process and ensuring the quality of the code. She is also skilled in web design and user interface.
- **Bob**: Bob is the backend developer of Next Horizon. He is responsible for creating the server, the database, and the API for the app. He is also proficient in security and authentication.
- **Charlie**: Charlie is the frontend developer of Next Horizon. He is responsible for creating the client-side logic and the user interface for the app. He is also experienced in web animation and interactivity.

[CONTRIBUTING]

---
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[893e0e151c...](https://github.com/Stutternov/f13tbd/commit/893e0e151c05648fd712f75e24520fc77354ed39)
#### Sunday 2023-12-03 04:25:37 by lolman360

robot update/rework (#204)

## About The Pull Request

does a lot of changes to robots
all changes TBD

robots are now much faster (0.3 slowdown instead of 1).
they are also somewhat tankier across the board to compensate for their
lack of armor (0 armor btw)

robot modules have been revisited:
medical assaultron was rolled into medical borg and is now an altskin.
mining borg now has a shovel, and its emag module is a rocketsledge that
mines better and has 12 less damage.
engiborg's emag module is also a rocketsledge (uncreative)
assaultron was rolled into secborg and is now an altskin.
vtec has been nerfed significantly from -1 slowdown to -0.25

gutsy flamethrower nerfed significantly: 1s firedelay, 33% lower
projectile count, actual energy cost

all robots now have the wastebot faction, since all selectable sprites
are fo13 robots anyways. this also makes slugs do 90 damage to them,
which is extremely funny and something i might remove. again, tbd



## Why It's Good For The Game

as long as they're pickable they should be functional

## Pre-Merge Checklist
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.


## Changelog

:cl:
add: new stuff to robots
del: old stuff from robots
tweak: robots can now patch nests
balance: robots are overall buffed (holy shit their slowdown was
dogshit)
/:cl:

---
## [Touhou-13/Assistant-Daisensou-Touhou-13](https://github.com/Touhou-13/Assistant-Daisensou-Touhou-13)@[248e30344b...](https://github.com/Touhou-13/Assistant-Daisensou-Touhou-13/commit/248e30344b49f69cdbfbea62ed0d8f2853a70547)
#### Sunday 2023-12-03 04:46:38 by SkyratBot

[MIRROR] Makes Telekinesis + Russian Revolver Interaction more fair [MDB IGNORE] (#25042)

* Makes Telekinesis + Russian Revolver Interaction more fair (#79740)

## About The Pull Request

Fixes #77238

Basically, you were able to just spam kill people with the russian
revolver if you had telekinesis, which isn't really fair. Now, after
taking a leaflet out of the the discussion in that issue report, you can
still pull off the same party trick... once...

Basically, let's just say that when you focus on firing the gun in your
mind... you're also pointing it directly at your mind (your brain (your
skull (you instantly die))). This occurs even if the projectile doesn't
actually touch you (because that would be hellish to account for) but
you're the one who's playing russian roulette man

You still get to do some collateral damage because that's still a very
funny interaction but you only get to do it once per life. I don't know
if people will be happy to revive you after you "shoot" them. Also, the
way it's coded means that you can still leave the revolver on the table
and fire it at your foot or something, or just use it normally, as a
telekinesis user. This _only_ applies to distance-based firings.
## Why It's Good For The Game

The russian revolver is specifically coded to prevent you from damaging
other people, and this was a pretty silly way to sidestep that based on
the checks. Instead, let's make it so that you can still do this
admittedly funny interaction, but with enough reason to not do it (the
reason being that you'll always get fucking blatted).
## Changelog
:cl:
balance: After a string of unfortunate incidents, persons with
telekinesis have been strongly warned against playing Russian Roulette,
as they tend to hyperfixate on the gun a bit too much and end up firing
it directly at their head.
/:cl:

* Makes Telekinesis + Russian Revolver Interaction more fair

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Touhou-13/Assistant-Daisensou-Touhou-13](https://github.com/Touhou-13/Assistant-Daisensou-Touhou-13)@[5761091212...](https://github.com/Touhou-13/Assistant-Daisensou-Touhou-13/commit/57610912121327266d1b5b47eb6d93bfb33d8362)
#### Sunday 2023-12-03 04:46:38 by SkyratBot

[MIRROR] Revert "if you die in a mech you are ejected" [MDB IGNORE] (#25051)

* Revert "if you die in a mech you are ejected" (#79768)

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

* Revert "if you die in a mech you are ejected"

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [samehbenamor/androidprojectpdm](https://github.com/samehbenamor/androidprojectpdm)@[5d56539ebe...](https://github.com/samehbenamor/androidprojectpdm/commit/5d56539ebe7239098645ed448bc7ab3f3df4305b)
#### Sunday 2023-12-03 05:12:29 by Sameh

Tried making modify work

I am extremely depressed and the only thing truly keeping me from killing myself is typing code. I am miserable and desperate to escape the loneliness I feel as I type this description and I know that no one will ever read this ever and know that I am deep down suffering with racing non-stop thoughts about suicide and ending it all.

---
## [Camillei/app-dev](https://github.com/Camillei/app-dev)@[e4bf7099f0...](https://github.com/Camillei/app-dev/commit/e4bf7099f0ac5e6b3c6768069d35e03869cee3bb)
#### Sunday 2023-12-03 05:29:10 by Camillei

Update README.md

La La Land is about two people are drawn by their common desire to do what they love; The Uncanny Counter is all about a highschooler student with a disability who is enlisted to be part of the group of paranormal counters; To all the boys I loved is all about a teenage girl who sent letters to her five crushes, but never meant to sent them, now they are out and wreaking havoc on her life.

---
## [maaacha/f13tbd](https://github.com/maaacha/f13tbd)@[ec2004b453...](https://github.com/maaacha/f13tbd/commit/ec2004b453a5da2b81513777b420a23a845825e3)
#### Sunday 2023-12-03 05:40:09 by Stutternov

Logistics Officer Buff!!!! (Fuck you, leftover Yellowstone change) (#280)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

Tl;dr - Took the explosive granter off the construction loadout of CE
(why did they have it, they already had the one with C4 with that
trait.......... leftover Yellowstone change) and gave it instead to the
Logistics Officer since they realistically should have it as they do gun
crafting.

Also - it makes it so LO's can make mortar rounds now. Also-also, took
away the X4 off CE since it's strong. Gave them 2 C4 instead.

## Why It's Good For The Game

LO buff omg

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
removes: Removed explosive crafting and BP off of CE construction
loadout.
removes: Removed X4 off of CE explosive loadout option, replaced it with
C4
add: Added explosive perk book to LO so they can craft mortars,
grenades, and be useful. (I will buff them more soon so NCR has to use
them more.)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [maaacha/f13tbd](https://github.com/maaacha/f13tbd)@[e208ee981e...](https://github.com/maaacha/f13tbd/commit/e208ee981e86227c2a19b6ae4e35f489be0b0de3)
#### Sunday 2023-12-03 05:40:09 by SM45H

Khans map (My Git borked on last pr) (#285)

********* EDIT ***********
My last pr got closed because I was having errors with my github and had
to wipe it. The khamp is 90% the same as before. I removed the upper
level defense post and removed the lower sentry post's weather cover. I
added more trash piles in khamp, added an advanced workbench and two
advanced salvage spawns in the back thats protected with indestructible
walls so it cant be cheesed. I also made sure it was at the very end of
the bunker so it had to be earned. The back dungeon is much harder than
any other factions "down river". I also removed the wasteland medical
spawners, and replaced them with a few static meds. While I was mapping,
I fixed the church's zoning by heavens night, basically giving it a
roof.
********* EDIT ***********


Updated the khans, gave khamp character and flow, as well as beautifying
it. most of what was in the khamp as far as resources, was moved over
give or take a few things. moved the khans "down river" to the bunker
they use to run out of, filled with plenty of mobs. Most notable gear in
the back is one set of Khan armor(full helm and coat) as well as some
money and gunbook 3. Past servers, khans had a gun book down river. They
have to fight the khan killer ghoul and his little gang of attack
ghouls, and several mirelurks and a few mirelurk nests.

Gunpowder, metal, glass are with the spiders, and bbq sauce, mustard
packets, and hot sauce packets are guarded by mister handies and
cockroach. I added a few Easter eggs and funnies in khamp, that
including past khan dog, sunflower (forgor gurilla), a few batteries in
the river because, where else are you suppose to toss out your old car
batteries.

Khans base, while a bit bigger, does stay within the old dense rock
space they could mine out and stay within.





![image](https://github.com/f13babylon/f13babylon/assets/151568060/637ba21d-70f1-4eef-9ebc-2c8c31916b45)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/c0574a7a-aa19-456d-baf9-5116107ed8b9)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/fe2c4c81-f6ba-487a-a7c8-287bc8397ff1)

---
## [cyphar/runc](https://github.com/cyphar/runc)@[bdf6ec8a05...](https://github.com/cyphar/runc/commit/bdf6ec8a05db4429b9e381b58fa39fbade2ae8d1)
#### Sunday 2023-12-03 05:41:34 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not strictly necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) since
only operating on the actual inodes associated with the tid requires
this locking, but because of the pre-3.17 fallback for CentOS, we have
to do this in most cases.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[1a2ab1b13c...](https://github.com/OrionTheFox/Skyrat-tg/commit/1a2ab1b13c2da4eee7c39df31695926b13048063)
#### Sunday 2023-12-03 05:58:26 by SkyratBot

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
## [Somya2505/PRODIGY_DS_01](https://github.com/Somya2505/PRODIGY_DS_01)@[f93d0aa496...](https://github.com/Somya2505/PRODIGY_DS_01/commit/f93d0aa496fac2cd042912d9b81d7b1f55bf1740)
#### Sunday 2023-12-03 07:48:35 by Somya Sanjana Biswal

Update README.md

Employee Data Visualization Tool

BarChartVisualizer for Employee Dataset

Welcome to the Employee Data Visualization Tool repository! This project provides a versatile solution for creating insightful bar charts or histograms to visualize the distribution of variables within an employee dataset. Whether you're examining the age distribution, gender breakdown, or any other key demographic, our BarChartVisualizer is designed to empower you with clear and compelling visualizations.

Features : 

Variable Versatility: Visualize the distribution of both categorical and continuous variables within your employee dataset.

User-Friendly Interface: The tool offers an intuitive interface, ensuring a seamless experience for users of all levels, from beginners to experienced data analysts.

Customization Capabilities: Tailor your visualizations to your specific requirements with customizable parameters, allowing you to highlight the nuances of your employee data.

Enhanced Data Exploration: Gain deeper insights into your employee dataset by exploring the distribution patterns of various variables, enabling a better understanding of workforce demographics.

Getting Started

Clone the Repository: Start by cloning this repository to your local machine to access the BarChartVisualizer tool.

Documentation: Refer to the provided documentation to understand how to use the tool effectively and explore its features.

Contribute: We welcome contributions! Feel free to contribute to the development or report any issues to help us improve this visualization tool.

Dependencies :
Python 3.x
pandas
matplotlib

License
This project is licensed under the MIT License, so feel free to use, modify, and distribute it.

We believe that effective data visualization is crucial for understanding workforce dynamics, and our Employee Data Visualization Tool is here to simplify that process. Dive into your employee dataset with confidence, create compelling visualizations, and uncover meaningful insights.

Happy charting!

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[eb246c21f6...](https://github.com/Time-Green/tgstation/commit/eb246c21f6eb5380dc56e5779fcd51d11437557c)
#### Sunday 2023-12-03 09:09:58 by san7890

Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

---
## [ynot01/Yogstation](https://github.com/ynot01/Yogstation)@[75c13f4eff...](https://github.com/ynot01/Yogstation/commit/75c13f4effbd82c8dc661c6b3bbc0146de44fded)
#### Sunday 2023-12-03 10:11:14 by cowbot92

[PORT] Adds several more signs for the bar to use (#20997)

* yo fuck emisssives

that shit sucks

* sure the rest of these can come too

I guess

* no 100% orange juice

sorry

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[0d5f9907a2...](https://github.com/norsvenska/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Sunday 2023-12-03 13:03:03 by Jacquerel

Shapechange health transfer tweaks (#79009)

## About The Pull Request

Fixes #78721
This PR does a handful of things behind the scenes to increase the
consistency of shapechange health tracking.

First of all we adjust the order of operations taken when you restore
the original body. The implementation as-was would remove the status
effect midway through and null a bunch of variables we tried to continue
using. This would result in several runtimes and code failing to run,
with the upshot that untransforming upon death would leave the caster
completely alive, with the corpse of its transformed shape at its feet.
Oops.

Additionally while testing this I realised that transferring the damagew
as also kind of fucked.
We wouldn't bother to do it at _all_ if you died, which is a shame, so I
made it simply heal you instead of reviving you so we can always do it.
Then as noted in the linked issue, we were applying all transferred
damage to a single limb, which could exceed the health of the limb and
remove damage. Now we spread it around the body.

Finally, applying damage to a human using the "force" flag would often
actually apply less damage to their _health_ than expected. This is
because arms and legs contribute only 75% of their damage taken to a
mob's overall health.
Now instead of reading `health` we read `total damage` which ignores the
limb damage modifier.

The end result of this is that if you transform into a corgi, take 50%
of your health, and transform back then you will have 50% of your health
as a human.
Previously the result would be that you'd have ~63%, then transforming
into a corgi would leave you with ~63% of a corgi's health, then
transforming back into a human would leave you at about 71%... and so on
and so forth. Now it doesn't do that.

## Changelog

:cl:
fix: Dying when using (most) shapeshift spells will now kill you rather
than having you pop out of the corpse of your previous form.
fix: Damage will now be accurately carried between forms rather than
being slightly reduced upon each transformation.
/:cl:

---
## [leomartins1999/advent-of-code](https://github.com/leomartins1999/advent-of-code)@[0db05e42ee...](https://github.com/leomartins1999/advent-of-code/commit/0db05e42ee734e7052b5cf9cea37064ac357ae2a)
#### Sunday 2023-12-03 13:42:27 by leomartins1999

2023 - Day 3 (#39)

* WIP iterate symbols impl

* Forgive father for I have sinned; Part 1 solution

* Add part 2... not that bad tbh

* Initial refactors

* Initial refactors

* Delete very ugly code; My sins are forgiven

* Final improvements

---
## [Martin301020/appdev](https://github.com/Martin301020/appdev)@[a3cf12adf7...](https://github.com/Martin301020/appdev/commit/a3cf12adf75b0b0702849b1e31a7214fdfa3e9c7)
#### Sunday 2023-12-03 13:55:42 by Martin301020

Update README.md

Trolls Band Together is a 2023 American animated jukebox musical comedy film produced by DreamWorks Animation and distributed by Universal Pictures, based on the Good Luck Trolls dolls from Thomas Dam. It serves as the sequel to Trolls World Tour (2020), and the third installment in the Trolls franchise. The film was directed by Walt Dohrn and co-directed by Tim Heitz, from a screenplay written by Elizabeth Tippet. Anna Kendrick, Justin Timberlake, Zooey Deschanel, Christopher Mintz-Plasse, Icona Pop, Anderson .Paak, Ron Funches, Kenan Thompson, Kunal Nayyar and Dohrn reprise their voice roles from previous films, with newcomers Eric André, Kid Cudi, Daveed Diggs, Troye Sivan, Camila Cabello, Amy Schumer, Andrew Rannells, RuPaul and Zosia Mamet joining the ensemble voice cast. In the film, Poppy (Kendrick) and Branch (Timberlake), who are officially a couple, attempt to rescue Floyd (Sivan) while reuniting Branch's brothers after the boyband phenomenon, BroZone, was disbanded.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[68bae36771...](https://github.com/treckstar/yolo-octo-hipster/commit/68bae3677136eeb937c6a22c24e53230804b434e)
#### Sunday 2023-12-03 14:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[100124757f...](https://github.com/Mirag1993/mrdg/commit/100124757f6aca1111cf238014b93f9812e237c6)
#### Sunday 2023-12-03 14:23:24 by Mirag1993

Eoehoma Firearms (& friends) (#2315)

![Screenshot_5451](https://github.com/shiptest-ss13/Shiptest/assets/58402542/08f9b0ee-15db-4091-a974-6d887cd85259)

Holy shit, this should not have taken a year to make

Adds the E-10, E-11, E-40, E-50, and E-60 to the game. Weapons
manufactured by defunct firearms company Eoehoma Firearms.

Founded in 77 FS, Eoehoma was a early pioneer of ‘hybrid’ Solarian and
Kalixcian laser weapons. The company went bankrupt due to increasingly
poor and risky decision making, and all of it's patents were bought out
by Nanotrasen. While Nanotrasen's Emitters bear a striking resemblance
to the E-50, otherwise Nanotrasen has not produced any of Eoehoma's old
weapons, instead focusing on Sharplite designed weapons.

Other changes:
- NT and Sharplite weapons have different fire sounds from each other
- Laser weapons buffed to 20 -> 25 damage
- Pulse shots don't destroy walls and are now 50 -> 40 damage
- Emitter shots now do 30 -> 60 damage
- Various grammar fixes
- Removes some non-lore compliant mentions
- Adds a manufacturer indicator to many guns
- Ports https://github.com/tgstation/tgstation/pull/60353
- Resprites various laser weaponry, notably the pulse guns.
- Deathsquad and ERT/LP hardsuits have been redone

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/c5df7029-95da-4041-b8b1-e4cfd35436dd)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/f72a3672-e996-4fdd-a68d-4553655f1a0c)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/7bd2dc53-ab29-49e8-8f90-87d4c72583f9)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/4bdc6493-4c94-49d0-995b-2a450d738211)
ceredits to tetrazeta for the unfinished deathsquad sprite, i simply
finished it and touched it up

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/517b72e3-c72b-4875-a6fb-84c017105908)

One of the last things i remember the old leads planned was to buff
lasers to make them stand up to the various ballistics better. Also
allows Pulse Rifles to be more used in events by nerfing them to not be
comedically overpowered. Now they are just Overpowered.

More ruin content and such. I'm sure the maptainers will make good use
of this stuff.

And sprites, i fucking love sprites

:cl: retlaw34, tetrazeta
add: Eoehoma Firearms, a new guns manufacturer!
add: ERT and "Asset Protection" Hardsuits have gotten a new look!
add: New laser fire sounds

balance: Lasers now do slightly more damage
balance: Pulse rifles don't destroy walls anymore and do slightly less
damage, and have lost their stun mode.
balance: Emitters do 60 damage and create turf fires on hitting a
non-supermatter object.
fix: Various laser weapons that had broken autofire (E-TAR and the Tesla
Cannon) now work

spellcheck: Grammar on some descriptions was corrected.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: retlaw34 <58402542+retlaw34@users.noreply.github.com>
Co-Authored-By: Mark Suckerberg <mark@suckerberg.gay>
Co-Authored-By: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [Shalz-sha/Unemployment-Analysis-with-Python](https://github.com/Shalz-sha/Unemployment-Analysis-with-Python)@[337649fa54...](https://github.com/Shalz-sha/Unemployment-Analysis-with-Python/commit/337649fa541dbfb9737dea2a5b02165d57718d62)
#### Sunday 2023-12-03 14:53:56 by Shalini.R

Add files via upload

🚀 OASIS INFOBYTE DATA SCIENCE INTERNSHIP TASK 2: Unemployment Analysis with Python

Excited to share the outcomes of Task 2 in my Oasis InfoByte Data Science Internship journey! 📈

Domain: Unemployment Analysis with Python

🌐 Problem Statement:
Addressing the surge in unemployment rates during the Covid-19 pandemic, I delved into a robust data science project. The objective was to meticulously analyze unemployment trends across regions and time, unraveling compelling insights from the data.
Key Highlights:
📊 Exploratory Data Analysis:
Conducted a comprehensive exploration of the dataset, focusing on its structural nuances.
Ensured data quality through rigorous examinations of null values and duplicates.
Applied effective data cleaning and manipulation techniques to enhance dataset integrity.

💡 Data Visualization:

Utilized Plotly Express and Matplotlib for visually compelling state-wise unemployment rate representations.
Explored correlation matrices to uncover intricate relationships between independent features.
Delved into day and month-wise analyses, revealing captivating patterns during the pandemic year of 2020.

📈 Insights Unveiled:

Discovered strong positive correlations between labor participation rates and latitude.
Identified critical features, such as estimated employed and estimated unemployment rate, showcasing robust negative correlations.
Analyzed month and day-wise unemployment trends, spotlighting May 2020 with the highest rates and month-end peaks.

Visual Storytelling:
📊 State-Wise Unemployment Rate:
📊 Correlation Matrix:
📊 Month and Day-Wise Analysis:
📊 Region-Wise Analysis:

Conclusion:

Task 2 has been an enlightening journey into the intricacies of unemployment data. The correlation matrix and visualizations serve as powerful tools in identifying key patterns and trends.
Next Steps:
Continued exploration into feature selection for optimal model performance.
Ongoing analysis to unveil region-specific nuances in unemployment dynamics.
Gratitude for the enriching experience at Oasis InfoByte! 🌟 Excited for the next strides in data science! 🚀
hashtag#DataScience hashtag#DataAnalysis hashtag#UnemploymentAnalysis hashtag#Python hashtag#OasisInfoByte hashtag#DataInsights

---
## [amitranjan93/Projects](https://github.com/amitranjan93/Projects)@[bb8cf69a72...](https://github.com/amitranjan93/Projects/commit/bb8cf69a721624ed5533064f6e643422af4625cc)
#### Sunday 2023-12-03 15:03:46 by amitranjan93

WatchList Application

I'm thrilled to announce the launch of my latest project: the Movie WatchList Application! 🚀

📌 Key Features:
✨ Spring REST: Providing seamless API endpoints for a smooth user experience.
✨ Spring MVC: Ensuring a robust and user-friendly web application.
✨ Spring JPA: Simplifying data access and management.
✨ Thymeleaf as a template engine: Creating dynamic and responsive web pages.
✨ Spring Lombok : is a java library tool that is used to minimize/remove the boilerplate code and save the precious time of during development by just using some annotations.
✨ MySQL database: Securely storing your valuable movie data.

With this application, you can:
🎥 Browse and search for your favorite movies.
📝 Add movies to your personal watchlist.
🔍 Update comments of movies.
📦 Implicitly fetch movie rating and priority.

Our custom validation ensures that your movie data is accurate and secure.

Whether you're a movie enthusiast or just looking for something fun to watch, the Movie WatchList Application has got you covered! 🌟

---
## [ioccc-src/temp-test-ioccc](https://github.com/ioccc-src/temp-test-ioccc)@[75ac0752ed...](https://github.com/ioccc-src/temp-test-ioccc/commit/75ac0752edfa4bf79d3222ea35cedccd6f281944)
#### Sunday 2023-12-03 15:25:56 by Cody Boone Ferguson

Add 2012/grothe/try.sh + format/typo checks

And since the try.sh scrambles and descrambles a cookie recipe I will
offer this funny story from decades ago that my mum tells every so
often: my uncle, who lived with my parents, and my father were at home
and they made 12 dozen cookies. They called my mum at her work and told
her: we made twelve dozen cookies and we saved you one! My mum thought
they meant she saved them one dozen cookies, already suggesting they had
eaten too many. But no. They left her one cookie! The reason is they
couldn't get the milk and cookies balanced so the only obvious thing to
do was to eat 143 cookies.  Obviously. They were quite sick and nobody
was sympathetic to their ridiculous stunt.

So let that be a lesson to anyone who decides they want to eat 143
cookies: just eat 142 and you'll be just fine, weight gain
notwithstanding! :-) (Okay maybe keep it at 24 .. unless they're
chocolate in which case you might want to eat three, four, five, however
many dozen you can fit in your stomach.)

Only the last paragraph is not sincere. The first really did happen.

---
## [oatm22/minetest-mygame](https://github.com/oatm22/minetest-mygame)@[4bb4a2a818...](https://github.com/oatm22/minetest-mygame/commit/4bb4a2a8187d036325482bb727a65b899f8991bd)
#### Sunday 2023-12-03 15:41:03 by Yaya - Nurul Azeera Hidayah @ Muhammad Nur Hidayat Yasuyoshi

Update Malay translations
1. Added missing translation to the following files:
  beds.ms.tr, creative.ms.tr, default.ms.tr, farming.ms.tr,
  fire.ms.tr, sethome.ms.tr
2. Changes some translation as per following:
  a. beds.ms.tr
    - Leave Bed changed from Bangun (wake up) to Tinggalkan Katil
      (leave bed, in literal sense) just because the button would
      be interpreted by some people as 'wake up on next morning'
      (ie. skipping night) instead of 'wake up interrupting current
      sleep progress' which is the intended meaning.
  b. boats.ms.tr
    - Boat cruise mode changed from Mod bot layar makan angin to
      Mod jelajah bot, the original translation is more like direct
      translation, and this has been changed to more natural one
      to make sure player know that the mode is a cruise control.
    - Reset changed from Set semula to Tetap semula, this is for
      standardizing with existing term used in various places.
  c. default.ms.tr
    - Page \@1 of \@2 changed from the short form to the long form.
    - Mese Crystal Fragment had missing word 'Kristal' re-added.
  d. dye.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.
  e. game_commands.ms.tr
    - respawn changed from lahir semula (reborn) to jelma semula
      (reappear), this is to make it consistent with the language
      used in multiple other games that had similar respawning
      system, and avoiding the religious context of life that is
      implied by the use of previous translation.
    - spawnpoint changed from titik permulaan (starting point) to
      titik jelma ((re)appear point), see previous point.
  f. tnt.ms.tr
    - Gun Powder changed from Serbuk Senjata Api (firearms powder)
      to Serbuk Letupan (explosion powder) because that is the
      proper translation, the latter is still the term used even
      when talking about actual firearm, the former didn't exist
  g. vessels.ms.tr
    - item changed from barang (thing) to item, this is mainly
      because some of the 'item' that could be stored are not
      some solid 'thing' where the word barang could be used for,
      so using the word item here keep it neutral.
  h. wool.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.

---
## [mosra/magnum-extras](https://github.com/mosra/magnum-extras)@[d0e7354e26...](https://github.com/mosra/magnum-extras/commit/d0e7354e26c3816225e925f6cf84a657a6706e32)
#### Sunday 2023-12-03 15:51:43 by Vladimír Vondruš

Whee: rework BaseLayer and TextLayer style assignment.

Requiring the calling code to have a compile-time-sized struct felt like
a good idea in theory. In practice it's absolutely horrendous tho, as:

 - The calling code then has to ensure matching order between a style
   enum and a style struct, which is extremely hard to maintain without
   a nasty preprocessor magic.
 - Defining a builtin style means either having to define & document a
   struct that glues a LayerStyleCommon instance together with several
   LayerStyleItem instances, which is nasty on its own, and then have to
   *somehow* populate it. Which in a (C++11) constexpr context means
   either using the implicit initializer, again losing any mapping from
   the actual enum values to the order (thus gaining *nothing* from such
   a "named tuple" definition), or having to give up on any constexpr
   use and assign to the named fields in order to ensure at least some
   ordering sanity.
 - It's extremely annoying and / or impossible to extend the style
   definition for custom widgets -- one has to *derive a struct* for
   that, and then somehow copy the original builtin data to its prefix.
 - The error message when the layer style count differs from the actual
   passed data is total garbage. Nobody is interested in how many bytes
   something occupies, they want to know *what is wrong* and the API
   isn't capable of saying or even knowing that.

So now it's instead a setStyle() API taking the LayerStyleCommon
instance and a (contiguous) list of LayerStyleItem. A downside is that
the (GL) implementation then does two GL buffer uploads, alternatively
it could put them together and upload at once (which means a nasty temp
allocation). With Vulkan (and I hope WebGPU) this won't be a problem as
there's a way to submit multiple uploads in a single command, or just
memory-mapping the buffer and doing a copy directly.

Extending a style is then a matter of creating an array that's larger
than the compile-time constant, having the custom style items start from
that constant, and copying the original data to prefix of that array.
Simple.

For the TextLayer this also merges the previous setStyle() and
setStyleFonts() APIs together, because they were always meant to be
called together anyway. It makes the whole usage a lot less janky and
unclear.

---
## [KikoWen0/NebulaStation](https://github.com/KikoWen0/NebulaStation)@[d751e1c642...](https://github.com/KikoWen0/NebulaStation/commit/d751e1c64246612f02089bc4059f3dc686edad2a)
#### Sunday 2023-12-03 16:10:44 by DaCoolBoss

Adds garbage dumpster ruins (#79446)

## About The Pull Request
Adds 4 small space ruins. Each is a dumpster in space containing hostile
mobs to fight and items to bring back to the station. There's a
decommissioned garbage truck pulling each dumpster which acts as a
staging area before you take on the mobs inside.
All the fights are in cramped dark areas with full pressure, air is
breathable but sometimes has miasma in it so beware of getting sick. So
you can drop your space suit and put on armour, but PKAs won't fire at
full power and keeping a gas mask on is recommended.
Also all the dumpsters look the same from the outside so you gotta crawl
inside to know what's inside. And no you can't metagame it with mesons
either.

Comes in the following flavours:
Food Waste
Full of trash from kitchens, and food. Some of the food is still edible.
There's a lot of territorial rats. You can chop them up into meat if you
want more food. The big prize is a big vat of cooking oil.

Medical Waste
Spare organs, cyberorgans and almost a full set of old surgical gear.
There's a syndicate agent here up to no good and he has a GUN. The gun
blows up when the agent dies so you can't get it. There's a few corpses
of different species in bodybags and some spare corpse parts so you can
bring them back to the station and give them to the coroner. Also a
single use eyestealer in a safe (the cool way to do surgery) and a bug
from the old traitor objective that doesn't do jack but can probably
still get you thrown in perma.

Construction Garbage
Tools and construction materials here, including a cool hammer that fits
in a tool belt and can function as a crowbar. There's also a drug lab
with plenty of weird pills to eat, cigarettes to eat and an angry
russian drug dealer who will stab you if he sees you. He has a badass
lighter and a flamethrower you can take after you kill him. Setting fire
to things in here is not recommended because of all the welding fuel.

Mall Trash
Action figures, trading cards, Christmas crackers and other trash the
local mall tossed out. Also a mothman used to live here but he got eaten
by giant spiders so you can grab his stuff, including snacks and a
civilian modsuit with no mods (wow). You can cut through the webs to
kill the spiders or let them eat you too if you want.
## Why It's Good For The Game
More content for space explorers.
More variety to the potential dangers of space, now u can get sick and
die or get eaten by rats (this is hobo RP)
Better environmental storytelling. Now instead of players left asking
"what happens to the garbage when it goes into space" they can rest
assured that there's busted ass garbage trucks in space. All their
questions are answered.
Loot that encourages working with people on the station. Raw food for
the kitchen, rats for genetics, organs for the coroner, etc
## Changelog
:cl:
add: 4 new space ruins
/:cl:

---
## [KikoWen0/NebulaStation](https://github.com/KikoWen0/NebulaStation)@[a5fabd8819...](https://github.com/KikoWen0/NebulaStation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Sunday 2023-12-03 16:10:44 by Profakos

Changes to the lore of Knock (#79542)

## About The Pull Request

This PR renames Knock to Lock, and changes most of the knowledge gain
lore.

## Why It's Good For The Game

The Knock Lore, is based on the Knock Principle from Cultist Simulator,
with the path description being copied from the wiki. Many other
keywords and concepts are fully lifted from that game (Locksmith's
Secret, Mother Of Ants, etc). In my vision, if a heretic path has to be
based on a principle from cultist simulator, it should have its own
spin, and also, the knowledge gain texts should tell a story. For
example, Ash tells the story of a watchman burning down their city after
being betrayed, and Cosmic is a love story between a knowledge seeker
and a monster from the beyond.

So I have decided to reflavour Knock. I have changed the name to Lock,
so at least it would feel similar, just like how Blade is akin to Edge.
Many powers also block people or confuse their paths instead of opening
new ways, and thus, I feel a path whose name implies that it *both*
opens and closes would be more self describing.

I have changed most of its lore to be about the Locked Labyrinth, where
knowledge seekers willingly trap themselves and submit themselves to
servitude to find ultimate freedom by progressing through its trials.
These are the Stewards, who are basically workers in an infinite and
malicious hotel in their dreams. Consider them assistants if you will
(this wasn't my intention when I wrote the lore, but thinking about it
in retrospect, it honestly fits). In the implied story, the heretic
joins their ranks, but keeps getting closer to the more corrupt members,
along with parasitic spirits. Ultimately, they manage to open the
Labyrinth's core, letting out the Stewards, allowing them to manifest in
the forms of heretic summon creatures.

The side path spells and the lock knowledge ritual I have not touched,
they were fine. Some items have been renamed and repathed.

I have kept the distinctive sound effect for using the Grasp, as its
unique enough. Though if someone did have a nice sound effect for
turning a lock and added some filters, I would add it.

**DB Issue**

I have renamed the achievement's define to MEDAL_LOCK_ASCENSION but kept
the value as "Knock", as I don't know how trigger a change in the DB. If
this is a blocking change, I'll try to figure out how to make a
migration file.

**Future improvements**

I would also come back later with another PR, that hands out names to
the eldritch beings spawned by the portal, based on the Stewards in the
knowledge gain lore that I added, along with some new ones that fit the
theme, and some jokey ones like Minotaur.

## Changelog

:cl:
spellcheck: Renamed Knock to Locks, and changed most of the flavor text
of knowledge gain, and renamed some items and knowledges from the path.
/:cl:

---
## [Aliscans/crawl](https://github.com/Aliscans/crawl)@[dffb6e3712...](https://github.com/Aliscans/crawl/commit/dffb6e3712f7bc9ff45b6ae244928f1d806afe75)
#### Sunday 2023-12-03 16:32:32 by regret-index

Brain Feed -> Brain Bite (minor damage + mp drain, no int drain)

Brain Feed is an extremely weird monster spell in most games. With so
little stat drain around by default in a three-rune game, individual hits
against a stat approach 0 extremely rarely unless a player has next to
none, which is influenced heavily by character start combo and very little
by normal character growth. The relatively minor hit of intelligence also
does very little for its use on higher Int characters aside from slightly
worsening spell success rates, which works weirdly against the flavour of
various brain-eating monsters not actually caring about the quality of
brain so much as just killing those with incidentally little of it.

It's kind of difficult to tell what this spell should do. It'd be entirely
possible to make it drain a lot more intelligence or percentage-based +
flat intelligence to make actually effect more characters, but while
strategic damage of a restorable sort would be more mechanical diversity,
screwing with spell success chances and non-tangible damage rolls aren't
mechanics we've kept to the present day (c.f. skilldrain, old sap magic).
So, I'm sidestepping the original effect of the spell entirely, while
focusing still on its theme.

Brain Feed is now revised into Brain Bite, a mildly-experimental mix of half
a Smite plus a percentile version of Draining Gaze- 4-8 irresistable direct
damage doubled if you have no mp, then draining 20% of one's max mp (rounded
down). (This now also works on monsters, dealing damage checking on antimagic
and then applying antimagic.) The percentage part lets it scale across the
game (compared to Draining Gaze rapidly heavily draining most player mp), and
irresistable but restrained damage sources are currently pretty reserved
designs (Smiting, Damnation, usually Torment) that could be iterated further
upon.

(It'd be good to think over what the point of statdrain even is outside
of Hell, Tomb, and klown pies. Possibly a variant of flaying but only
for stats would be interesting, possibly making an even shorter para but
with brief stat-zero would be an interesting revision of current para.
This is kind of out of this particular commit's scope, though- getting
to stat zero via Brain Feed didn't really happen for a very large number
of character combinations, so concerns over that are minimal.)

Tile update uses the old mimic teeth tile by coolio, modified by jpeg,
on top of the current Brain Feed icon by snw-0.

---
## [depoz0/G2station](https://github.com/depoz0/G2station)@[c9d2c940d8...](https://github.com/depoz0/G2station/commit/c9d2c940d87f5205bdf882280af074b132e1af6c)
#### Sunday 2023-12-03 16:56:27 by Vekter

Ports feral cats and feral cat grenades from Hippie (#80031)

## About The Pull Request
Feral Cats are just a hostile variant of cats that will fuck you up if
they see you. They are added solely for the sake of feral cat grenades -
a new, interesting, and fuzzy way to get out of a jam or just wreak
havoc around you. Each one costs 5 TC and spawns 5 really pissed off
cats to chase down assistants in the hallway.

They don't currently ignore traitors or the person who threw them - I
haven't worked out how to do that with our faction system (Hippie gave
them the syndicate faction but traitors don't get that on our codebase).
If anyone wants to contribute or help me suss that out it'll be cool,
otherwise just don't be around if there's nobody else for them to maul.

## Why It's Good For The Game
They're funny.

## Changelog
:cl: Vekter
add: Added a new hostile variant of cats, "feral cats".
add: Added a new traitor item, "feral cat grenades". For 5 TC, you too
can throw a grenade at someone and make five cats maul them to death.
/:cl:

---
## [pivovarit/AoC_2023_go](https://github.com/pivovarit/AoC_2023_go)@[a255be01b4...](https://github.com/pivovarit/AoC_2023_go/commit/a255be01b41da92b5434150a0fe69e621a90ce26)
#### Sunday 2023-12-03 18:31:43 by Grzegorz Piwowarek

Day 3 (#6)

### Day 3: Gear Ratios

You and the Elf eventually reach a gondola lift station; he says the
gondola lift will take you up to the water source, but this is as far as
he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a
problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't
working right now; it'll still be a while before I can fix it." You
offer to help.

The engineer explains that an engine part seems to be missing from the
engine, but nobody can figure out which one. If you can add up all the
part numbers in the engine schematic, it should be easy to work out
which part is missing.

The engine schematic (your puzzle input) consists of a visual
representation of the engine. There are lots of numbers and symbols you
don't really understand, but apparently any number adjacent to a symbol,
even diagonally, is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

Here is an example engine schematic:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```
In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
number is adjacent to a symbol and so is a part number; their sum is
4361.

Of course, the actual engine schematic is much larger. What is the sum
of all of the part numbers in the engine schematic?

#### Part Two

The engineer finds the missing part and installs it in the engine! As
the engine springs to life, you jump in the closest gondola, finally
ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still
wrong? Fortunately, the gondola has a phone labeled "help", so you pick
it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the
window. There stands the engineer, holding a phone in one hand and
waving with the other. You're going so slowly that you haven't even left
the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine
is wrong. A gear is any * symbol that is adjacent to exactly two part
numbers. Its gear ratio is the result of multiplying those two numbers
together.

This time, you need to find the gear ratio of every gear and add them
all up so that the engineer can figure out which gear needs to be
replaced.

Consider the same engine schematic again:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```
In this schematic, there are two gears. The first is in the top left; it
has part numbers 467 and 35, so its gear ratio is 16345. The second gear
is in the lower right; its gear ratio is 451490. (The * adjacent to 617
is not a gear because it is only adjacent to one part number.) Adding up
all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

---
## [ekaitz-zarraga/AhoTTS](https://github.com/ekaitz-zarraga/AhoTTS)@[9b801ca791...](https://github.com/ekaitz-zarraga/AhoTTS/commit/9b801ca7919079f00181c4cc266f0fb506ab69d3)
#### Sunday 2023-12-03 19:23:53 by Ekaitz Zarraga

Clean warnings and reformat:

This uncovered many bugs:

- Ambiguous ifs
- Unexpected fallthroughs in switches

And many more!
It's possible that my fixes broke some stuff, as the algorithms are not
clear.

Also the formatting was so awful this changeset is really ugly. I'm
sorry.

---
## [kabae25/vex-u-23-24](https://github.com/kabae25/vex-u-23-24)@[f42e386af0...](https://github.com/kabae25/vex-u-23-24/commit/f42e386af072172321ac40421d3df9ae434ccd0d)
#### Sunday 2023-12-03 19:40:22 by rohan908

I AM GOING FUCKING INSANE KILL ME

climb shit fuck this

---
## [Rohail33/Realking_kernel_sm8250](https://github.com/Rohail33/Realking_kernel_sm8250)@[df3814efcb...](https://github.com/Rohail33/Realking_kernel_sm8250/commit/df3814efcb863ab19136f0b447c99a6e9abfe6d1)
#### Sunday 2023-12-03 21:29:58 by Angelo G. Del Regno

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
## [1393F/tgstation](https://github.com/1393F/tgstation)@[c63b233f42...](https://github.com/1393F/tgstation/commit/c63b233f42a46d9373fd41b3f69edde3d2d48002)
#### Sunday 2023-12-03 21:57:46 by _0Steven

Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

---
## [1393F/tgstation](https://github.com/1393F/tgstation)@[492ed90f28...](https://github.com/1393F/tgstation/commit/492ed90f28dfd213e9438509653727f788efcebd)
#### Sunday 2023-12-03 21:57:46 by necromanceranne

Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs. 

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

---
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[ccb9ce38a7...](https://github.com/Stutternov/f13tbd/commit/ccb9ce38a7e26763f93c089bd0a65c9e35b70243)
#### Sunday 2023-12-03 22:32:11 by panzerr1944

no mans land; kebob changes (#166)

## About The Pull Request

![image](https://github.com/f13babylon/f13babylon/assets/76122712/cb2a0acd-9aa7-4a0c-bc3a-651c2b0104d4)
Kebab now has renegades. And it's loot increased / fixed.


https://github.com/f13babylon/f13babylon/assets/76122712/22a30f2e-354c-4988-8ac7-e39e9fce9c51

## Why It's Good For The Game
NML's town is no longer free loot. Rather, an optional bunker that the
other factions might jump you at. Kind of like normal bunkers in that
way, except with current NML rules you aren't going to lose your
everything. Just your life until someone revives you. I like the no gear
looting in NML rule, it's kinda funny.

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
ADDED MOBS:
1x pa claw
6x r. docs
3x r. snipers
2x r. meisters
4x r. defenders
6x r. soldiers
10x r. grunts
9x r. prospects
2x r. engies
3x r. guardians
(Total: 46)
REMOVED MOBS:
4x Legendary Ghouls
6x Legendary Mutants
2x Legendary Deathclaws
(Total: 12)
ADDED/EDITED LOOT:
2x Superhigh Ballistic Spawners
1x Mid-High E-Weapon Spawner
1x Mid-High Ballistic Weapon Spawner
1x Mid E-Weapon Spawner
1x Mid Ballistic Spawner
1x NVG Spawner
1x Gauss Rifle Spawner
1x Deluxe Stock Parts Spawner
1x (x10) Strange Seeds Spawner
1x Unique Weapon Spawner
1x High Ballistic Print
1x VHigh Ballistic Print
1x DC Medicine Journal
1x Chemistry Book
1x Random Armor Spawner
1x T4 Armor Spawner
1x Bowl of Fruit
CHANGED TERRAIN / WALLS / MISC:
Sandbags on the main road
Sandbags at the farm and graveyard
Indestructible Walls for south-side to prevent cheese
Replaced see-through airlock with high-sec one in clinic for d-claw
-
Everything else is unedited from current Kebab to my knowledge.

---
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[a2491a3c89...](https://github.com/Stutternov/f13tbd/commit/a2491a3c89e4fa54e2c112902162278493f10945)
#### Sunday 2023-12-03 22:32:11 by Mazzinsanity

Enables Podpeople as a Roundstart Species (May need to be enabled on the box) (#194)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Makes a WEAKENED version of Podpeople selectable as a roundstart
species. Their maluses and bonuses are as follows:
- 1.25 damage modifiers for Brute/Burn
- Restore 2 hunger and heal 0.2 Brute, 0.2 Burn, 0.1 Toxin when in
light.
- Reverse effects in darkness.

Changes podpeople bloodtype to EZ Nutrient
## Why It's Good For The Game
This lets people play as anthropomorphic Broc flowers.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
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
add: enabled podpeople as a roundstart species
balance: rebalanced weak podpeople healing
tweak: changed podpeople bloodtype to EZ Nutrient
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---

