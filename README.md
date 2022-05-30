## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-29](docs/good-messages/2022/2022-05-29.md)


1,514,916 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,514,916 were push events containing 2,158,173 commit messages that amount to 110,096,458 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[245ec35dae...](https://github.com/tgstation/tgstation/commit/245ec35dae59d0edc92663ccb8012b27d5e1a198)
#### Sunday 2022-05-29 00:02:38 by LemonInTheDark

Removes (in) smoke and foam reactions (#67270)

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

---
## [SilverLongjohns/Regalia-Game-Jam](https://github.com/SilverLongjohns/Regalia-Game-Jam)@[26264399ee...](https://github.com/SilverLongjohns/Regalia-Game-Jam/commit/26264399eea5e2f83b1ff8f5ea8ea01fc877e1f0)
#### Sunday 2022-05-29 00:03:21 by Gigabell

Learning Stuff

Dear Diary
Today I learned basic shit and I'm saving it here so i dont forget.

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[ce0aff7526...](https://github.com/StarStation13/StarStation13/commit/ce0aff7526158133acd1b53bd5d2d9d6ac9578f3)
#### Sunday 2022-05-29 00:29:15 by GoldenAlpharex

Fixed Icebox's lower two z-levels not being included in the Map Compile action (#66503)

Did you know that you could currently put a bunch of random shit in the lower levels of icebox and the map compile would be none the wiser?

I sure did.

I hate that it's done manually this way, but honestly it's not worth refactoring the whole action to make it work differently.

Ensuring that the lower levels work properly is, in fact, a good thing.

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[cd294e9040...](https://github.com/Shadow-Quill/tgstation/commit/cd294e9040505e73e46384d6166015afa43217f3)
#### Sunday 2022-05-29 00:29:57 by vincentiusvin

Scipaper rebalancing: Nitrium and halon shell removal. Nitrous added. Emphasis on BZ. (#66738)

Similar in spirit to #65707, with some more changes.

Restructured the gaseous experiments to:

    Nitrous (practice experiment)
    BZ (mainstay experiment)
    Hyper-Nob (lategame/once-in-a-while experiment)

Added a mining partner.

Moved adv weaponry lock to normal weaponry under reactionless. Toned down t3 reactionless.

BZ locks adv engi. Medbay unbridled by toxin gasses now.

Removed Xenobio's BZ Can.
Why It's Good For The Game

My original intent with papers was expanding the difficulty range of toxins. Both to things harder than tritium (nob, nitrium, etc) and also to things easier than tritium (bz, reactionless, etc).

In that process, I feel that i strayed a bit to the harder side, this PR is an attempt to tone down the overall difficulty of some of the gaseous experiments a notch.

Nitrous now takes place of the old BZ, BZ takes place of old nitrium/halon, and noblium stays because it's difficulty is in a pretty good spot for a relatively unimportant but nice to have tech.

While we're at it, I also added more emphasis to BZ production to toxins instead of tritium. This will hopefully incentivize people to try the department out. There is a risk of this being a bit of a chore, but I believe that the relevant atmos gameplay loop is strong enough to have it be fun. You need to check on the chamber, turn on pipes, adjust the input rate, and many more that makes it significantly more fun to do.

We do this by:

    Locking advanced engineering with BZ (organs and implants lock lifted). Depending on feedback i wont mind changing this around if you want to suggest another node as long as it's of similar or very slightly less importance.

    Getting rid of xeno's BZ can. Some xeno players need it for making slimes sleep, with their roundstart supply removed there should be a significant demand for the BZ production in toxins to go online asap.

If you have been paying attention to our PRs, i have been working to make BZ production as seamless and quick as possible in toxins. My five map prs #66454 #66198 #66064 #66010 #65857 have been building up to this. You can make BZ relatively quickly with the new freezer chamber in place. Probably even faster than ordering it in cargo, which is a fine ballpark to use if you want to make changes to it.

If you want to know how to operate it, here is a wiki guide in place https://tgstation13.org/wiki/User:Vincentius_vin/Sandbox#BZ_Synthesis. We will move it to the main toxins page once the rest of the page is finished, pictures are added, 

Made adv engi tech node require bz shells as an experiment, organs no longer need it.
Adv mining no longer requires adv engi.
Removed nitrium and halon shell, implant experiment lock lifted because of the former.
Relocked sec 1 tech node to need pressure bombs, sec 2 no longer needs tritium bomb.
Made advanced pressure bombs easier to do without funny fusion gases.
Added a new mining partner that accepts smaller (even non-atmos/non-ordnance related) bombs
Added more options to purchase nodes in the paper partners. Your point gain stays the same though.
Removed roundstart BZ can from xenobio.

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[70a87f9510...](https://github.com/pariahstation/Pariah-Station/commit/70a87f95100c290699ce5b92bb099d2f56bbb336)
#### Sunday 2022-05-29 01:59:41 by Gallyus

HOLY SHIT SHUT UP (#742)

* HOLY SHIT SHUT UP

* Apply suggestions from code review

* seeba sauce

---
## [EdwardNashton/mojave-sun-13](https://github.com/EdwardNashton/mojave-sun-13)@[2996f41136...](https://github.com/EdwardNashton/mojave-sun-13/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Sunday 2022-05-29 02:11:32 by EdwardNashton

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
## [darkxex/pcsx2](https://github.com/darkxex/pcsx2)@[89f10e1605...](https://github.com/darkxex/pcsx2/commit/89f10e160572063b4871bfb8d0c6ffff54f9543a)
#### Sunday 2022-05-29 02:21:33 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [Mahima-Anand/BusinessOnBot-Task](https://github.com/Mahima-Anand/BusinessOnBot-Task)@[39d7c4e1d3...](https://github.com/Mahima-Anand/BusinessOnBot-Task/commit/39d7c4e1d321d085b76fb04ba35a81344c2c20bb)
#### Sunday 2022-05-29 03:50:58 by Hi , I'm Mahima

Readme.md

Sentiment Analysis on Covid-19 Tweets
The use of social media has increased over the past two years due to Covid-19 pandemic. The main objective of this analysis is to understand public sentiment. A lot of people have used social media as a medium to express their feelings and emotions where some people conveyed sad messages while others shared positive content. People have also used social media to seek medical help related to vaccines and others. Analyzing these types of data posted on social media might help us analyze and solve many issues related to the pandemic. In this analysis, I have used classification in Machine Learning algorithms to find out whether the sentiment portrayed by the tweets on Twitter is positive or negative.

---
## [Bm0n/tgstation](https://github.com/Bm0n/tgstation)@[27946f516d...](https://github.com/Bm0n/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Sunday 2022-05-29 05:18:11 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [JDeepD/git-1](https://github.com/JDeepD/git-1)@[bdaf1dfae7...](https://github.com/JDeepD/git-1/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Sunday 2022-05-29 06:19:31 by Tao Klerks

branch: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local topic branch from an existing
remote branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the upstream tracking branch.

When the user pushes with a default "git push", with the intention of
pushing their (new) topic branch to the remote, they get an error, and
(amongst other things) a suggestion to run "git push origin HEAD".

If they follow this suggestion the push succeeds, but on subsequent
default pushes they continue to get an error - so eventually they
figure out to add "-u" to change the tracking branch, or they spelunk
the push.default config doc as proposed and set it to "current", or
some GUI tooling does one or the other of these things for them.

When one of their coworkers later works on the same topic branch,
they don't get any of that "weirdness". They just "git checkout
feature1" and everything works exactly as they expect, with the shared
remote branch set up as remote tracking branch, and push and pull
working out of the box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

An experienced git user might say "well yeah, that's what it means to
have the remote tracking branch set to origin/master!" - but the
original user above didn't *ask* to have the remote master branch
added as remote tracking branch - that just happened automatically
when they branched their feature branch. They didn't necessarily even
notice or understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the topic branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make this "branches have the same name locally as on the remote"
workflow less painful / more obvious by introducing a new
branch.autosetupmerge option called "simple", to match the same-name
"push.default" option that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

Update the error displayed when the 'push.default=simple' configuration
rejects a mismatching-upstream-name default push, to offer this new
branch.autosetupmerge option that will prevent this class of error.

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Also extend the existing branch tests with three new cases testing
this option - the obvious matching-name and non-matching-name cases,
and also a non-matching-ref-type case. The matching-name case needs to
temporarily create an independent repo to fetch from, as the general
strategy of using the local repo as the remote in these tests
precludes locally branching with the same name as in the "remote".

Signed-off-by: Tao Klerks <tao@klerks.biz>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[2d31f31fbf...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/2d31f31fbf65c0ef2b4ecc4f92525e249647ba38)
#### Sunday 2022-05-29 07:11:46 by petrero

9.1. Profiler: Your Debugging Best Friend - composer require debug

  Time to install our second package. And this one is fun. Let's commit our changes first: it'll makes it easier to check out any changes that the new package's recipe makes.

  Add everything:

    git add .
  That looks fine so... commit:

    git commit -m "Added some Tiwggy goodness"
  Beautiful.

  The debug Pack
  Now run:

    composer require debug
  So yes, this is another Flex alias... and apparently it's an alias for symfony/debug-pack. And we know that a pack is a collection of packages. So instead of adding this one line to our composer.json file, if we check, it looks like it added one new package up under the require section - this is a logging library - and... all the way at the bottom, it added a new require-dev section with three other libraries.

  The difference between require and require-dev isn't too important: all of these packages were downloaded into our app, But as a best practice, if you install a library that's only meant for local development, you should put it into require-dev. The pack did that for us! Thanks pack!

  Recipe Changes
  - Back at the terminal, this also installed three recipes! Ooh. Let's see what those did. I'll clear the screen and run:

    git status
  So this is familiar: it modified config/bundles.php to activate three new bundles. Again, bundles are Symfony plugins, which add more features to our app.

  It also added several configuration files to the config/packages/ directory. We will talk more about these files in the next tutorial, but, on a high level, they control the behavior of those bundles.

  The Web Debug Toolbar And Profiler
  - So what did these new bundles give us? To find out, head over to your browser and refresh the homepage. Holy cats, Batman! It's the web debug toolbar. This is debugging madness: a toolbar full of good info. On the left, you can see the controller that was called along with the HTTP status code. There's also the amount of time the page took, the memory it used and also how many templates were rendered through Twig: this is the cute Twig icon.

  On the right side, we have details about the Symfony local web server that's running and PHP info.

  But you haven't seen the best part: click any of these icons to jump into the profiler. This is the web debug toolbar... gone crazy. It's full of data about that request, like the request and response, all of the log messages that happened during that request, information about the routes and the route that was matched, Twig shows you which templates were rendered and how many times they were rendered... and there's configuration information down here. Phew!

  But my most favorite section is Performance. This shows a timeline of everything that happened during the request. This is great for two reasons. The first is pretty obvious: you can use this to find which parts of your page are slow. So, for example, our controller took 20.4 millisecond. And within the controller's execution, the homepage template rendered in 3.9 milliseconds and base.html.twig rendered in 2.8 milliseconds.

  The second reason this is really cool is that it uncovers all the hidden layers of Symfony. Set this threshold down to zero. Previously, this only displayed things that took more than one millisecond. Now it's showing everything. You don't need to worry about the vast majority of the stuff, but it's super cool to see the layers of Symfony: the things that happen before and after your controller is executed. We have a deep dive tutorial for Symfony if you want to learn more about this stuff.

  The web debug toolbar and profiler will also grow with our app. In a future tutorial, when we install a library to talk to the database, we will suddenly have a new section that lists all of the database queries that a page made and how long each took.

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[14940106da...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/14940106da403d026e5bbe303e98ff5ac9468c1b)
#### Sunday 2022-05-29 07:11:46 by petrero

8.3. Twig Inheritance

  Block Names
  - Oh, and the names of these blocks are not important. If you want to rename them after your favorite 90's sitcom character, do it. Just remember to also update its name in any child templates.

  You can also add more blocks. Every block you add is just another potential override point.

  Default Block Content
  - Oh, and you may have noticed that blocks can have default content. Look at the page right now: the title says "Welcome". That's because the title block has default content... and we're not overriding it. Let's change the default title to "Mixed Vinyl".

  So now that will be the title of every page on our site... unless we override that. In our template, either above block body or below - the order of blocks doesn't matter - add {% block title %}, {% endblock %} and, in between "Create a new Record".

  And now... yes! This page has a custom title.

  Adding to (Instead of Replacing) the Parent Block
  - Oh, and you might be wondering:

    What if I don't want to replace a block entirely.... but instead, I want to add to a block?

  That's totally possible. In base.html.twig, the title block is set to "Mixed Vinyl". If we wanted to prepend our custom title to that, we could say "Create a new Record" then use the "say something" tag to print a function called parent().

  That does exactly what you'd expect: it finds the parent template's content for this block.. and prints it. Refresh and... that's so nice.

  Template Inheritance is Class Inheritance
  - If you're ever confused about how template inheritance works, it's useful, for me at least, to think about it exactly like object-oriented inheritance. Each template is like a class and each block is like a method. So the homepage "class" extends the base.html.twig "class", but overrides two of its methods. If that only confused you, don't worry about it.

  So... that's it for Twig. You're basically a Twig expert, which I'm told is a popular topic at parties.

  Next: one of the killer features of Symfony is its debugging tools. Let's get these installed and check 'em out.

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[e4fd5fa046...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/e4fd5fa0463c5d1599325fe273bda0c99750a682)
#### Sunday 2022-05-29 07:11:46 by petrero

9.2. Profiler: Your Debugging Best Friend

  dump() and dd() Functions
  - Ok, so the debug pack installed the web debug toolbar. It also installed a logging library that we'll use later. And it installed a package that gives us two fantastic debug functions.

  Head over to VinylController. Pretend that we're doing some developing and we need to see what this $tracks variable looks like. It's pretty obvious in this case, but sometimes you'll want to see what's inside a complex object.

  To do that, say dd($tracks) where "dd" stands for dump and die.

  So if we refresh... yup! That dumps the variable and kills the page.

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[ee4dbd422a...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/ee4dbd422a17cd746030291031c0850021c9a05b)
#### Sunday 2022-05-29 07:11:46 by petrero

9.5. Profiler: Your Debugging Best Friend

  And even more useful, in Twig only, you can use dump() with no arguments.

  This will dump all variables that we have access to. So here's the title variable, tracks and, surprise! There's a third variable called app. This is a global variable that we have in all templates... and it gives us access to things like the session and user data. And... we just discovered it by being curious!

  So now that we've got these awesome debugging tools, let's turn to our next job... which is to make this site less ugly. Time to add CSS and a proper layout to bring our site to life!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ae82ed4c6d...](https://github.com/mrakgr/The-Spiral-Language/commit/ae82ed4c6d966ab49b4cac03393b4b2af568f715)
#### Sunday 2022-05-29 10:43:25 by Marko Grdinić

"10am. Let me start. I'll focus on the course, I am worn down from yesterday. I've started obsessing endlessly about hatching. I meant to try out the Mangaka plugin, but let me just focus on the course now. I'll tackle it properly after I get my current task out of the way.

10:10am. It seems Sculptis Pro works for polypainting. Yeah, it would, I didn't think of this.

10:15am. 14m in. It seems the NPR filters will be in the second block. He remarks that some of us as really excited about it.

Absolutely.

10:35am. He is filling various objects with color to use as a mask in PS. The is the simplest one can do it. Indeed.

11:15am. Focus me. Why is he polygrouping in addition to poly painting. I know that polypaint is for masks. What about this?

It seems his intent is to use it as a separate, more nuanced mask. Polypaint groups objects together, but polygroup is more precise. Now he is in work mode. I can start skipping.

11:30am. https://www.youtube.com/watch?v=cJ83xWGtQtg
Hollow Knight Mini Concert

I'll leave this for later. At this point I am actively skipping part of the course. It does not matter. Let me just see what he does with NPR filters and PS and then I am done with this.

11:35am. Focus me, let me move on to the NPR filters. Trying to go through a course like this without following along, but just watching sucks just as much as I'd have expected it to.

Time for day 5.

11:50am. https://deepdreamgenerator.com/ddream/usyjn4ge8wu

Got 13 likes here. I thought I would not et anything. Come to think of it, I should have a put a link to this yesterday in the journo, but it slipped my mind. Right now I just logged in because I started wondering whether it had some anime style baselines.

12:25pm. Come to think of it, how does dithering work during the posterization process?

https://youtu.be/yxogCdsDjYo?t=561
Blender NPR Basics 2: A Classic Painterly Rendering Method

Found and started watching this. So you can get a painterly result by cruching the midtones, and then doing some filtering.

https://www.youtube.com/user/MicJej

It might be worth watching all of these here.

https://youtu.be/X8YkWdhty7I?t=277

Hmmm, it does not go into the implementation. Nevermind. Maybe it just adds a grid of points to the original image before cruching it. That is how I would try implementing it.

https://blendermarket.com/products/cavity-pass

Somebody did a cavity pass in the compositor. I wonder how he extracted the actual curvature in order to do that.

12:40pm. Let me go back to the course. I am 40m out of 110 into the part 1 of day 5. Actually, let me have a break here. After that I'll clear day 5 and think about what to do next. Most likely...

Yeah, I'll have to check out substance. Blender's compositor does not have the splatter capability."

---
## [PetkovSvetoslav/Java-Basic-Programing](https://github.com/PetkovSvetoslav/Java-Basic-Programing)@[a2f20aa2e3...](https://github.com/PetkovSvetoslav/Java-Basic-Programing/commit/a2f20aa2e36f6909a24f3e2e8c56f9aa6d233c4f)
#### Sunday 2022-05-29 10:45:56 by Svetoslav Krasimirov Petkov

Fishing boat

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
## [newstools/2022-punch-nigeria](https://github.com/newstools/2022-punch-nigeria)@[98d60a53ab...](https://github.com/newstools/2022-punch-nigeria/commit/98d60a53abab1f28d50065281aa0059ffe1ea786)
#### Sunday 2022-05-29 10:51:28 by Billy Einkamerer

Created Text For URL [punchng.com/after-10-year-relationship-marias-ex-boyfriend-battered-killed-her-for-seeking-better-life-with-new-lover-sister/]

---
## [newstools/2022-punch-nigeria](https://github.com/newstools/2022-punch-nigeria)@[d8c3183385...](https://github.com/newstools/2022-punch-nigeria/commit/d8c3183385ebf052da6c723ce98f34c174834ea5)
#### Sunday 2022-05-29 10:52:53 by Billy Einkamerer

Created Text For URL [punchng.com/i-battled-depression-suicidal-thoughts-for-years-yet-no-one-understood-my-struggle-filmmaker/]

---
## [Krutoy242/Enigmatica2Expert-Extended](https://github.com/Krutoy242/Enigmatica2Expert-Extended)@[f00b8b6585...](https://github.com/Krutoy242/Enigmatica2Expert-Extended/commit/f00b8b65852455bc12d72c9328f2582685699a23)
#### Sunday 2022-05-29 11:19:11 by Krutoy242

✏️ Recipes:

New recipes:
- [Gaia Spirit] add Peaceful recipe
- [Rat Toga] now craftable in Peaceful
- [Treated Stick] in different machines

Cheaper:
- [Conglomerate Of Life]
- [Crystallized Lapis Lazuli Shard] and other shards in [Starlight Infuser]
- [Inventory Rerouter]
- [Cursed Heart]
- [Enchanced Heart]
- [Compact machine wall]

Fixes:
- [Polymer Clay] fix bucket variant. Now craftable in [Fluid Crafter]
- [<endreborn:block_end_stone_smooth>][<endreborn:block_end_stone_pillar>][<endreborn:chiseled_end_bricks>] add to [Chisel]
- Remove enchantments since they are duplicates from other mods: Cyclic's **Auto-Smelt** and **Magnet**, EnderIO's **AutoSmelt**

---
## [hrzntal/horizon](https://github.com/hrzntal/horizon)@[db1f299865...](https://github.com/hrzntal/horizon/commit/db1f2998657331873027feca14236ebb73dc02d0)
#### Sunday 2022-05-29 11:27:05 by Alex 'Avunia' Takiya

Removes hrzn/ dir; bye BST - hello FRETs (#674)

* Move emote code and sfx

Moves the emote code and sfx away from the hrzn/ directory
Also removes some obsolete or not needed vars and code paths.
Additionally, reworks screams to be keyed lists.

* Moves cargo crate code to core

* Removes hrzn/ dir, mods icspawn and more

Changes:
- Moves all files out of hrzn/ and removes the folder
- Moves the hrvfoxcat suit to its proper core file
- Adds & removes a few debug snowflake objects
- Renames Bluespace Techs to Fast Response Emergency Techs (FRET Agents)
- Adds quiet spawn-in and -out for IC-spawning
- Adds SM hallucination resistance to the debug glasses
- Renames the admin janni outfit and IDs to the FRET Agents
- Adjust admin outfit for FRET, adds Hardsuit FRET outfit
- Makes a few strings in observer.dm on the IC-spawn-in code macros

* Converts indentation from spaces to tabs

* Fix accidentally redefining proc for bag of holding

This is why its bad to do this sleep deprived

* Replace FRET clothing with tactical turtleneck for now

Also fix name by removing the fwd slash and putting the second name in
brackets instead

* Replace HoS with ablative trenchcoat for FRET outfit

* Fixes screaming emote

Holy balls fuck whoever worked on this shit before me

* Set return value for initialize of return_back to parent proc

---
## [jonab03/MatterMegadrive](https://github.com/jonab03/MatterMegadrive)@[4ddf4099e1...](https://github.com/jonab03/MatterMegadrive/commit/4ddf4099e12a6f8a7bc84f383c0977aca6b1e94d)
#### Sunday 2022-05-29 11:48:32 by JonaB03

Fix and adjust Omni-Tool mining speed

The Omni-Tool has a rather subtle bug that shows up when you mine
blocks with a high hardness.

Since this weapon doesn't use the default block breaking mechanics
they had to be reimplemented. This was done poorly.

The author tried to implement scaling based on the damage modifier but
this was done in a way that caused the multiplier to be applied to the
current damage rather than the damage that gets applied that tick.

This causes multiplicative scaling on the current damage making it go
up much quicker than it should.

This is different from the default methods causing a de-sync between
the client and the server by making the client have it's mining go
much faster.
I correct this by:

1. Doing the damage scaling in the new getDigSpeed() method.
2. Correcting the partial block breaking to what the default methods use.

This exposed the rather shameful default mining speed. I decided to
change it to 9 after some in game testing. This is 3x the speed of an
un-enchanted diamond pickaxe and 1.5x of the tritanium pickaxe.

This speed is rather quick whilst not making it trivial to get over the
"instant mining" threshold.

These changes aren't particularly clean in my opinion but they work
and don't seem to have any nasty side effects.

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[d3dff0454a...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/d3dff0454a31e05b40da8171d2b148b5c66f5039)
#### Sunday 2022-05-29 12:48:20 by petrero

11.1. Generate Urls & bin/console

  There are two different ways that we can interact with our app. The first is via the web server... and that's what we've been doing! We got to a URL and... behind the scenes, it executes public/index.php, which boots up Symfony, calls the routing and runs our controller.

  Hello bin/console
  - What's the second way we can interact with our app? We haven't seen it yet: it's via a command line tool called bin/console. At your terminal run:

    php bin/console
  ... to see a bunch of commands within this script. I love this thing. It's full of stuff to help us debug, eventually it will have code-generation commands, commands for setting secrets: all kinds of good stuff that we're going to discover little-by-little.

  But I do want to point out that... there's nothing special about this bin/console script! It's just a file: there's literally a bin/ directory with a console file inside. You'll probably never need to open this file or think about it, but it is useful. Oh, and on most systems, you can just run:

    ./bin/console
  ... which looks cooler. Or sometimes you may see me run:

    symfony console
  ... which is just another way to execute this file. We'll talk more about this in a future tutorial.

  bin/console debug:router
  - The first command I want to check out inside of bin/console is debug:router:

    php bin/console debug:router
  This is awesome. It shows us every route in our app, like our two routes for / and /browse/{slug}. What are these other routes? They come form the web debug toolbar and profiler system... and they're only here while we're developing locally.

  Ok, back on our site.... at the top of the page, we have two non-functional links to the homepage and browse page. Let's hook these up. Open templates/ base.html.twig... and search for a tags. Here we go.

  So it would be really easy to get this working by just href="/". But instead, whenever we link to a page in Symfony, we're going to ask the routing system to generate a URL for us. We'll say:

    Please generate the URL to the homepage's route, or the browse page's route.

  Then, if we ever change the URL of a route, all our links will instantly update. Magic.

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[23e3e18ba2...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/23e3e18ba2ed58a1635825bc61b6b0d2ce2dae3c)
#### Sunday 2022-05-29 12:48:20 by petrero

12.1. JSON API Endpoint

  In a future tutorial, we're going to create a database to manage songs, genres, and the mixed vinyl records that our users are creating. Right now, we're working entirely with hardcoded data... but our controllers - and - especially templates won't feel that much different once we make this all dynamic.

  So here's our new goal: I want to create an API endpoint that will return the data for a single song as JSON. We're going to use this in a few minutes to bring this play button to life. At the moment, none of these buttons do anything, but they do look pretty.

  Creating the JSON Controller
  - The two steps to creating an API endpoint are... exactly the same as creating an HTML page: we need a route and a controller. Since this API endpoint will be returning song data, instead of adding another method inside of VinylController, let's create a totally new controller class. How you organize this stuff is entirely up to you.

  Create a new PHP class called SongController... or SongApiController would also be a good name. Inside, this will start like any other controller, by extending AbstractController. Remember: that's optional... but it gives us shortcut methods with no downside.

  Next, create a public function called, how about, getSong(). Add the route... and hit tab to auto-complete this so that PhpStorm adds the use statement on top. Set the URL to /api/songs/{id}, where id will eventually be the database id of the song.

  And because we have a wildcard in the route, we are allowed to have an $id argument. Finally, even though we don't need to do this, because we know that our controller will return a Response object, we can set that as the return type. Make sure to auto-complete the one from Symfony's HttpFoundation component.

  Inside the method, to start, dd($id)... just to see if everything is working.

  Let's do this! Head over to /api/songs/5 and... got it! Another new page.

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[f5a79d3ea6...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/f5a79d3ea6e080c50203f5959a3f5d4f0727842a)
#### Sunday 2022-05-29 12:48:20 by petrero

16.1. Setting up Webpack Encore - composer require encore

  Our CSS setup is fine. We put files into the public/ directory and then... we point to them from inside our templates. We could add JavaScript files the same way.

  But if we want get truly serious about writing CSS and JavaScript, we need to take this to the next level. And even if you consider yourself a mostly backend developer, the tools we're about to talk about will allow you to write CSS and JavaScript that feels easier and is less error-prone than what you're probably used to.

  The key to taking our setup to the next level is leveraging a node library called Webpack. Webpack is the industry standard tool for packaging, minifying and parsing your frontend CSS, JavaScript, and other files. But don't worry: Node is just JavaScript. And its role in our app will be pretty limited.

  Setting up Webpack can be tricky. And so, in the Symfony world, we use a lightweight tool called Webpack Encore. It's still Webpack... it just makes it easier! And we have a free tutorial about it if you want to dive deeper.

  Installing Encore
  - But let's do a crash course right now. First, at your command line, make sure you have Node installed:

    node -v
  You'll also need either npm - which comes with Node automatically - or yarn:

    yarn --version
  Npm and yarn are Node package managers: they're the Composer for the Node world... and you can use either. If you decide to use yarn - thats what I'll use - make sure to install version 1.

  To install Encore, run:

    composer require encore
  This installs WebpackEncoreBundle. Remember, a bundle is a Symfony plugin. And this package has a recipe: a very important recipe. Run:

    git status

  The Encore Recipe
  - Ooh! For the first time, the recipe modified the .gitignore file. Let's go check that out. Open .gitignore. The stuff on top is what we originally had... and down here is the new stuff added by WebpackEncoreBundle. It's ignoring the node_modules/ directory, which is basically the vendor/ directory for Node. We don't need to commit that because those vendor libraries are described in another new file from the recipe: package.json. This is Node's composer.json file: it describes the Node packages that our app needs. The most important one is Webpack Encore itself, which is a Node library. It also has a few other package that will help us get our job done.

  The recipe also added an assets/ directory... and a configuration file to control Webpack: webpack.config.js. The assets/ directory already holds a small set of files to get us started.

---
## [opencart/opencart](https://github.com/opencart/opencart)@[89c304ae61...](https://github.com/opencart/opencart/commit/89c304ae61fb683b2ca8ff7dcf5ceabfc4f5a0eb)
#### Sunday 2022-05-29 13:21:13 by Anton

OC4 return created module_id

IMHO every single model function, creating a row in DB, must return this row id after executed.

I can check `$module_id = $this->db->getLastId();` in my code on clean opencart installation.
But what if this model function calls any `after` events which also insert rows into DB?

This is not a developer friendly software architecture when you need to create hacks, hooks, workarounds and other voodoo magic to get a single value for page redirect.

BUG:
By the way on creating, for example a banner module, on save you are not redirected to created module page. 
So every click on Save button just creates a duplicate of a module.

---
## [ranvis/putty](https://github.com/ranvis/putty)@[c19e7215dd...](https://github.com/ranvis/putty/commit/c19e7215ddd1d6a890fdb94d89bc5ccb46151363)
#### Sunday 2022-05-29 13:26:14 by Simon Tatham

Replace mkfiles.pl with a CMake build system.

This brings various concrete advantages over the previous system:

 - consistent support for out-of-tree builds on all platforms

 - more thorough support for Visual Studio IDE project files

 - support for Ninja-based builds, which is particularly useful on
   Windows where the alternative nmake has no parallel option

 - a really simple set of build instructions that work the same way on
   all the major platforms (look how much shorter README is!)

 - better decoupling of the project configuration from the toolchain
   configuration, so that my Windows cross-building doesn't need
   (much) special treatment in CMakeLists.txt

 - configure-time tests on Windows as well as Linux, so that a lot of
   ad-hoc #ifdefs second-guessing a particular feature's presence from
   the compiler version can now be replaced by tests of the feature
   itself

Also some longer-term software-engineering advantages:

 - other people have actually heard of CMake, so they'll be able to
   produce patches to the new build setup more easily

 - unlike the old mkfiles.pl, CMake is not my personal problem to
   maintain

 - most importantly, mkfiles.pl was just a horrible pile of
   unmaintainable cruft, which even I found it painful to make changes
   to or to use, and desperately needed throwing in the bin. I've
   already thrown away all the variants of it I had in other projects
   of mine, and was only delaying this one so we could make the 0.75
   release branch first.

This change comes with a noticeable build-level restructuring. The
previous Recipe worked by compiling every object file exactly once,
and then making each executable by linking a precisely specified
subset of the same object files. But in CMake, that's not the natural
way to work - if you write the obvious command that puts the same
source file into two executable targets, CMake generates a makefile
that compiles it once per target. That can be an advantage, because it
gives you the freedom to compile it differently in each case (e.g.
with a #define telling it which program it's part of). But in a
project that has many executable targets and had carefully contrived
to _never_ need to build any module more than once, all it does is
bloat the build time pointlessly!

To avoid slowing down the build by a large factor, I've put most of
the modules of the code base into a collection of static libraries
organised vaguely thematically (SSH, other backends, crypto, network,
...). That means all those modules can still be compiled just once
each, because once each library is built it's reused unchanged for all
the executable targets.

One upside of this library-based structure is that now I don't have to
manually specify exactly which objects go into which programs any more
- it's enough to specify which libraries are needed, and the linker
will figure out the fine detail automatically. So there's less
maintenance to do in CMakeLists.txt when the source code changes.

But that reorganisation also adds fragility, because of the trad Unix
linker semantics of walking along the library list once each, so that
cyclic references between your libraries will provoke link errors. The
current setup builds successfully, but I suspect it only just manages
it.

(In particular, I've found that MinGW is the most finicky on this
score of the Windows compilers I've tried building with. So I've
included a MinGW test build in the new-look Buildscr, because
otherwise I think there'd be a significant risk of introducing
MinGW-only build failures due to library search order, which wasn't a
risk in the previous library-free build organisation.)

In the longer term I hope to be able to reduce the risk of that, via
gradual reorganisation (in particular, breaking up too-monolithic
modules, to reduce the risk of knock-on references when you included a
module for function A and it also contains function B with an
unsatisfied dependency you didn't really need). Ideally I want to
reach a state in which the libraries all have sensibly described
purposes, a clearly documented (partial) order in which they're
permitted to depend on each other, and a specification of what stubs
you have to put where if you're leaving one of them out (e.g.
nocrypto) and what callbacks you have to define in your non-library
objects to satisfy dependencies from things low in the stack (e.g.
out_of_memory()).

One thing that's gone completely missing in this migration,
unfortunately, is the unfinished MacOS port linked against Quartz GTK.
That's because it turned out that I can't currently build it myself,
on my own Mac: my previous installation of GTK had bit-rotted as a
side effect of an Xcode upgrade, and I haven't yet been able to
persuade jhbuild to make me a new one. So I can't even build the MacOS
port with the _old_ makefiles, and hence, I have no way of checking
that the new ones also work. I hope to bring that port back to life at
some point, but I don't want it to block the rest of this change.

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[21ac902556...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/21ac90255638f03b2e6f4c42509e5edf559e2099)
#### Sunday 2022-05-29 14:46:56 by petrero

20.4. Real-World Stimulus Example

  Ok, so how do we use the axios library? By importing it!

  At the top of this file, we're already importing the Controller base class from stimulus. Now import axios from 'axios'. As soon as we do that, Webpack Encore will grab the axios source code and include it in our built JavaScript files.

  Now, down here, we can say axios.get() to make a GET request. But... what should we pass for the URL? It needs to be something like /api/songs/5... but how do we know what the "id" is for this row?

  Stimulus Values
  - One of the coolest things about Stimulus is that it allows you to pass values from Twig into your Stimulus controller. To do that, declare which values you want to allow to passed in via a special static property: static values = {}. Inside, let's allow an infoUrl value to be passed. I totally just made up that name: I'm thinking we'll pass in the full URL to the API endpoint. Set this to the type that this will be. So, a String.

  We'll learn how we pass this value from Twig into our controller in a minute. But because we have this, below, we can reference the value by saying this.infoUrlValue.

  So how do we pass that in? Back in homepage.html.twig, add a second argument to stimulus_controller(). This is an array of the values you want to pass into the controller. Pass infoUrl set to the URL.

  Hmm, but we need to generate that URL. Does that route have a name yet? Nope! Add name: 'api_songs_get_one'.

  Perfect. Copy that... and back in the template, set infoURl to path(), the name of the route... and then an array with any wildcards. Our route has an id wildcard.

  In a real app, these tracks would probably each have a database id that we could pass. We don't have that yet... so to, kind of, fake this, I'm going to use loop.index. This is a magic Twig variable: if you're inside of a Twig for loop, you can access the index - like 1, 2, 3, 4 - by using loop.index. So we're going to use this as a fake ID. Oh, and don't forget to say id: then loop.index.

  Testing time! Refresh. The first thing I want you to see is that, when we pass infoUrl as the second argument to stimulus_controller, all that really does is output a very special data attribute that Stimulus knows how to read. That's how you pass a value into a controller.

  Click one of the play links and... got it. Every controller object is passed its correct URL!

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[9390655477...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/9390655477ef59268ecdfa23db1660c787be69e4)
#### Sunday 2022-05-29 14:46:56 by petrero

17.1. Packaging JS and CSS with Encore

  When we installed Webpack Encore, its recipe gave us this new assets/ directory. Check out the app.js file. Interesting. Notice how it imports this bootstrap file. That's actually bootstrap.js: this file right here. The .js extension is optional.

  JavaScript Imports
  - This is one of the most important things that Webpack gives us: the ability to import one JavaScript file from another. We can import functions, objects... really anything from another file. We're going to talk more about this bootstrap.js file in a little bit.

  To see how this all works, in app.js, add a console.log().

  Ok... so who reads these files? Because... they don't live in the public/ directory... so we can't create script or link tags that point directly to them.

  webpack.config.js
  - To answer that, open webpack.config.js. Webpack Encore is an executable binary: we're going to run it in a minute. When we do, it will load this file to get its config.

  And while there are a lot of features inside of Webpack, the only thing we need to focus on right now is this one: addEntry(). This app could be anything... like dinosaur, it doesn't matter. I'll show you how that's used in a minute. The important thing is that it points to the assets/app.js file. Because of this, app.js will be the first and only file that Webpack will parse.

  It's pretty cool: Webpack will reads the app.js file and then follow all of the import statements recursively until it finally has a giant collection of all the JavaScript and CSS our app needs. Then, it will write that into the public/ directory.

  Running Webpack Encore
  - Let's see it in action. Find your terminal and run:

    yarn watch
  This is, as it says, a shortcut for running encore dev --watch. If you look at your package.json file, it came with a script section with some shortcuts.

  Anyways, yarn watch does two things. First, it created a new public/build/ directory and, inside, app.css and app.js files! But don't let the names fool you: app.js contains a lot more that just what's inside assets/app.js: it contains all the JavaScript from all the imports it finds. app.css contains all the CSS from all the imports.

  The reason these files are called app.css and app.js is because of the entry name.

  So the takeaway is that, thanks to Encore, we suddenly have new files in a public/build/ directory that contain all the JavaScript and CSS our app needs!

  The Encore Twig Functions

  Open your base layout: templates/base.html.twig. The secret is in the encore_entry_link_tags() and encore_entry_script_tags() functions. I bet you can guess what these do: add the link tag to build/app.css and the script tag to build/app.js.

  You can see this in your browser. View the source for the page and... yup! The link tag for /build/app.css... and script tag for /build/app.js. Oh, but it also rendered two other script tags. That's because Webpack is really smart. For performance purposes, instead of dumping one gigantic app.js file, sometimes Webpack will split it into multiple, smaller files. Fortunately, these Encore Twig functions are smart enough to handle that: it will include all the link or script tags needed.

  The most important thing is that the code that we have in our assets/app.js file - including anything it imports - is now functioning and showing up on our page!

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[b7872960ba...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/b7872960ba77852b77dbfa593952f89ae7ad894c)
#### Sunday 2022-05-29 15:03:05 by petrero

21.2. Turbo: Supercharge you App - yarn install --force

  In fact, find your terminal that's running yarn watch. We've got an error! It says the file @symfony/ux-turbo/package.json cannot be found, try running yarn install --force.

  Let's do that! Hit control+C to stop this... and then run

    yarn install --force
  or npm install --force. Then, restart Encore with:

    yarn watch
  The other file the recipe modified was assets/controllers.json. Let's go take a look at that: assets/controllers.json. This is another thing that's unique to Symfony UX. Normally, if we want to add a stimulus controller, we put it into the controllers/ directory. But sometimes, we might install a PHP package and that may want to add its own Stimulus controller into our app. This syntax basically says:

  Hey Stimulus! Go load this Stimulus controller from that new @symfony/ux-turbo package.

  Now this particular Stimulus controller is a little weird. It's not one that we're going to use directly inside of the stimulus_controller() Twig function. This is, kind of a, fake controller. What does it do? Just by it being loaded, it's going to activate the Turbo library.

  Hello Turbo! By Full-Page Refreshes
  - So I keep talking about Turbo. What is Turbo? Well, by running that composer require command... then reinstalling yarn, the Turbo JavaScript is now active and running on our site. What does it do? It's simple: it turns every link click and form submit on our site into an Ajax call. And that makes our site feel lightning fast.

  Check it out. Do one last full refresh. And then watch... if I click Browse, there was no full page refresh! If I click these icons, no refresh! Turbo intercepts those clicks, makes an Ajax call to the URL, and then puts that HTML onto our site. This is huge because, for free, our app suddenly looks and feels like a single page app... without us doing anything!

  The Web Debug Toolbar & Profiler for Ajax Requests
  - Now, one other cool thing you'll notice is that even though full page reloads are gone, these Ajax calls do show up on the web debug toolbar. And you can click to go see the profiler for that Ajax call really easily. This Ajax part of the web debug toolbar is even more useful with Ajax calls for an API endpoint. If we hit the play icon... that 7 just went up to 8... and here's the profiler for that API request! I'll open that link in a new window. That's a super easy way to get to the profiler for any Ajax request.

  So Turbo is amazing... and it can do more. There are some things you need to know about it before shipping it to production, and if you're interested, yup! We have a full tutorial about Turbo. I wanted to mention it in this tutorial because Turbo is easiest if you add it to your app early on.

  All right, congratulations! The first Symfony 6 tutorial is in the books! Pat yourself on the back... or better, find a friend and give them a crisp high five.

  And keep going! Join us for the next tutorial in this series, which will take you from a budding Symfony developer to someone who really understands what's going on. How services work, the point of all of these configuration files, Symfony environments, environmental variables, and a lot more. Basically everything you'll need to do whatever you want with Symfony.

  And if you have any questions or ideas, we are here for you down in the comments section below the video.

  Alright friends, see you next time!

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[0525ad7577...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/0525ad75774453cb7ea2a2c5e5c25f00fdc699e4)
#### Sunday 2022-05-29 15:43:18 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: RyuujiX <saputradenny712@gmail.com>
Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [ForumPlayer/activate-linux](https://github.com/ForumPlayer/activate-linux)@[6012d283ca...](https://github.com/ForumPlayer/activate-linux/commit/6012d283caeb096b9667ce759f0eeb92c0e99005)
#### Sunday 2022-05-29 16:23:05 by Reperak

Fix rgba_color_string returning default

Shame on me for not testing before submitting #65, and shame on the people who reviewed #65 for trusting my stupid ass.

Fixes #99

---
## [CluckeyMcCormick/fictional-guacamole](https://github.com/CluckeyMcCormick/fictional-guacamole)@[8060022302...](https://github.com/CluckeyMcCormick/fictional-guacamole/commit/806002230242678c843322d3a5d7a6599e9a47b0)
#### Sunday 2022-05-29 16:25:24 by frick-nedrickson

Update XSM to 1.5.4

I've had an extended hiatus - I was doing a lot. Painting 40k Kill
Team models, writing Monster-of-the-Week episodes, absolutely LOSING
myself to Elden Ring. But it's always good to come back to
programming, which is always my favorite.

Anyway, such a long hiatus means I've kinda lost track of what I was
doing. But there's always maintenance of a sort to be done! First up,
our plugins.

The previous XSM version was lingering around 1.4.6, but had since
been updated to 1.5.4 (1.5.5 on the GitLab version). The update
doesn't seem to have caused any issues, so now we need to take a look
at the other plug-ins...

---
## [Adamo2499/i-rule-translations](https://github.com/Adamo2499/i-rule-translations)@[2da56ed7da...](https://github.com/Adamo2499/i-rule-translations/commit/2da56ed7daa171bca85e2e16fb3ff70acd0acd4b)
#### Sunday 2022-05-29 16:34:02 by SlayerIbn

"Bucle" is pure shit and doesn't have the meaning that I want, "Ciclo" is fucking perfect

---
## [Clemens85/runningdinner](https://github.com/Clemens85/runningdinner)@[0b076a73b1...](https://github.com/Clemens85/runningdinner/commit/0b076a73b12a16fe6ca676a5e685313e2e7ac08e)
#### Sunday 2022-05-29 16:57:20 by Clemens Stich

Fuck you circleci... why don't you recognize Optional?!

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8a60a438a2...](https://github.com/treckstar/yolo-octo-hipster/commit/8a60a438a2239fdd0e0facc2f48b8869414199bf)
#### Sunday 2022-05-29 17:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [GamingInfinite/PlantsVsZombies-WebEngine](https://github.com/GamingInfinite/PlantsVsZombies-WebEngine)@[8e20df0fbc...](https://github.com/GamingInfinite/PlantsVsZombies-WebEngine/commit/8e20df0fbcba4b0d37376e18e8ab5f2330e976be)
#### Sunday 2022-05-29 17:41:32 by GamingInfinite

Projectiles and ReadMe Update

Pea Shooters (Kind Of) Work.  If you've been following my twitter (who has really) then you'll know that I still haven't implemented Zombies, and for that reason it just fires forever.  Thankfully I am clearing up ram as needed whenever projectiles are never going to be seen on screen again.

Also yeah I updated the ReadMe to accurately reflect whatever the hell is going on and also included Shields at the Top Where the Logo is going to be with all the relevant tech stack bullshit their.

---
## [F1restar4/DSharpPlus](https://github.com/F1restar4/DSharpPlus)@[8380b5b2de...](https://github.com/F1restar4/DSharpPlus/commit/8380b5b2deb9f2243c87e3277a34902ec08bb716)
#### Sunday 2022-05-29 19:06:32 by InFTord

[ci-skip] Fix docs typos in DiscordRestClient (#1317)

* Update DiscordRestClient.cs

* insanity

edited all of this with github site editor
madness
editing 2k lines of code is kinda pain with github site editor

* im idiot

* fixing...

* uh oh

* i love fixing docs

* fixing inconsistent ID stuff..

---
## [newstools/2022-the-sun-nigeria](https://github.com/newstools/2022-the-sun-nigeria)@[14496d5477...](https://github.com/newstools/2022-the-sun-nigeria/commit/14496d5477fea0e3a49b7f4d85c6e838e674a744)
#### Sunday 2022-05-29 19:09:12 by Billy Einkamerer

Created Text For URL [www.sunnewsonline.com/14-year-enugu-girl-was-with-boyfriend-not-kidnapped-police/]

---
## [pgrzesik/aws-cdk](https://github.com/pgrzesik/aws-cdk)@[c071367def...](https://github.com/pgrzesik/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Sunday 2022-05-29 19:34:36 by Kaizen Conroy

feat(glue): support partition index on tables (#17998)

This PR adds support for creating partition indexes on tables via custom resources.
It offers two different ways to create indexes:

```ts
// via table definition
const table = new glue.Table(this, 'Table', {
  database,
  bucket,
  tableName: 'table',
  columns,
  partitionKeys,
  partitionIndexes: [{
    indexName: 'my-index',
    keyNames: ['month'],
  }],
  dataFormat: glue.DataFormat.CSV,
});
```

```ts
// or as a function
table.AddPartitionIndex([{
  indexName: 'my-other-index',
  keyNames: ['month', 'year'],
});
```

I also refactored the format of some tests, which is what accounts for the large diff in `test.table.ts`. 

Motivation: 
Creating partition indexes on a table is something you can do via the console, but is not an exposed property in cloudformation. In this case, I think it makes sense to support this feature via custom resources as it will significantly reduce the customer pain of either provisioning a custom resource with correct permissions or manually going into the console after resource creation. Supporting this feature allows for synth-time checks and dependency chaining for multiple indexes (reason detailed in the FAQ) which removes a rather sharp edge for users provisioning custom resource indexes themselves.

FAQ:

Why do we need to chain dependencies between different Partition Index Custom Resources? 
  - Because Glue only allows 1 index to be created or deleted simultaneously per table. Without dependencies the resources will try to create partition indexes simultaneously and the second sdk call with be dropped.

Why is it called `partitionIndexes`? Is that really how you pluralize index?
  - [Yesish](https://www.nasdaq.com/articles/indexes-or-indices-whats-the-deal-2016-05-12). If you hate it it can be `partitionIndices`.

Why is `keyNames` of type `string[]` and not `Column[]`? `PartitionKey` is of type `Column[]` and partition indexes must be a subset of partition keys...
  - This could be a debate. But my argument is that the pattern I see for defining a Table is to define partition keys inline and not declare them each as variables. It would be pretty clunky from a UX perspective:
    ```ts
    const key1 = { name: 'mykey', type: glue.Schema.STRING };
    const key2 = { name: 'mykey2', type: glue.Schema.STRING };
    const key3 = { name: 'mykey3', type: glue.Schema.STRING };
    new glue.Table(this, 'table', {
      database,
      bucket,
      tableName: 'table',
      columns,
      partitionKeys: [key1, key2, key3],
      partitionIndexes: [key1, key2],
      dataFormat: glue.DataFormat.CSV,
    });
    ```

Why are there 2 different checks for having > 3 partition indexes?
  - It's possible someone decides to define 3 indexes in the definition and then try to add another with `table.addPartitionIndex()`. This would be a nasty deploy time error, its better if it is synth time. It's also possible someone decides to define 4 indexes in the definition. It's better to fast-fail here before we create 3 custom resources.

What if I deploy a table, manually add 3 partition indexes, and then try to call `table.addPartitionIndex()` and update the stack? Will that still be a synth time failure?
  - Sorry, no. 

Why do we need to generate names?
  - We don't. I just thought it would be helpful.

Why is `grantToUnderlyingResources` public?
  - I thought it would be helpful. Some permissions need to be added to the table, the database, and the catalog.

Closes #17589.

----

*By submitting this pull request, I confirm that my contribution is made under the terms of the Apache-2.0 license*

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[097c6bdb97...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/097c6bdb976fc4026cbab015f972f8dc23ded6d4)
#### Sunday 2022-05-29 22:32:38 by Angelo G. Del Regno

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

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [yurical/Auxio](https://github.com/yurical/Auxio)@[c6d7d8fe39...](https://github.com/yurical/Auxio/commit/c6d7d8fe39ae0f84051482961c3d2ad5ae64137a)
#### Sunday 2022-05-29 23:25:40 by OxygenCobalt

playback: implement "safe" slider wrapper

Implement a safe slider wrapper that does not crash with invalid values
as often.

Slider is a terrible component that is not designed with Auxio's
use-case in the slightest. Instead of gracefully degrading with invalid
values, it just crashes the entire app, which is horrible for UX.

Since SeekBar is a useless buggy version-specific sh******ed mess too,
we have no choice but to wrap Slider in a safe view layout that
hopefully hacks with the input enough to not crash the app when doing
simple seeking actions.

I hate android so much.

Resolves #140.

---
## [testy-Entertainment/bigkity-os](https://github.com/testy-Entertainment/bigkity-os)@[ead165fa10...](https://github.com/testy-Entertainment/bigkity-os/commit/ead165fa1042247b033afad7be4be9b815d04ade)
#### Sunday 2022-05-29 23:42:42 by Peter Zijlstra

objtool: Fix symbol creation

Nathan reported objtool failing with the following messages:

  warning: objtool: no non-local symbols !?
  warning: objtool: gelf_update_symshndx: invalid section index

The problem is due to commit 4abff6d48dbc ("objtool: Fix code relocs
vs weak symbols") failing to consider the case where an object would
have no non-local symbols.

The problem that commit tries to address is adding a STB_LOCAL symbol
to the symbol table in light of the ELF spec's requirement that:

  In each symbol table, all symbols with STB_LOCAL binding preced the
  weak and global symbols.  As ``Sections'' above describes, a symbol
  table section's sh_info section header member holds the symbol table
  index for the first non-local symbol.

The approach taken is to find this first non-local symbol, move that
to the end and then re-use the freed spot to insert a new local symbol
and increment sh_info.

Except it never considered the case of object files without global
symbols and got a whole bunch of details wrong -- so many in fact that
it is a wonder it ever worked :/

Specifically:

 - It failed to re-hash the symbol on the new index, so a subsequent
   find_symbol_by_index() would not find it at the new location and a
   query for the old location would now return a non-deterministic
   choice between the old and new symbol.

 - It failed to appreciate that the GElf wrappers are not a valid disk
   format (it works because GElf is basically Elf64 and we only
   support x86_64 atm.)

 - It failed to fully appreciate how horrible the libelf API really is
   and got the gelf_update_symshndx() call pretty much completely
   wrong; with the direct consequence that if inserting a second
   STB_LOCAL symbol would require moving the same STB_GLOBAL symbol
   again it would completely come unstuck.

Write a new elf_update_symbol() function that wraps all the magic
required to update or create a new symbol at a given index.

Specifically, gelf_update_sym*() require an @ndx argument that is
relative to the @data argument; this means you have to manually
iterate the section data descriptor list and update @ndx.

Fixes: 4abff6d48dbc ("objtool: Fix code relocs vs weak symbols")
Reported-by: Nathan Chancellor <nathan@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Borislav Petkov <bp@suse.de>
Acked-by: Josh Poimboeuf <jpoimboe@kernel.org>
Tested-by: Nathan Chancellor <nathan@kernel.org>
Cc: <stable@vger.kernel.org>
Link: https://lkml.kernel.org/r/YoPCTEYjoPqE4ZxB@hirez.programming.kicks-ass.net

---
## [robn/mujmap](https://github.com/robn/mujmap)@[b961b9032e...](https://github.com/robn/mujmap/commit/b961b9032e024c84044d8667ff8dbf47a45d70e6)
#### Sunday 2022-05-29 23:52:21 by Eliza Velasquez

Add troubleshooting section with auth guide

Also adds more warnings to the "migration" section, as I am becoming
increasingly paranoid that someone might behave like me and recklessly
try to migrate without doing the proper precautions, destroying their
notmuch database they spent hours working on (which in my case was not
because of mujmap, but because I tried to switch protonmail IMAP
clients, which was a horrible idea to do without backing up that I
immediately regretted)

---

