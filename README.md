## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-14](docs/good-messages/2022/2022-01-14.md)


1,631,221 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,631,221 were push events containing 2,596,230 commit messages that amount to 206,462,377 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a2fa7799f3...](https://github.com/tgstation/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Friday 2022-01-14 00:02:03 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [Sh1penfire/Endless-Rusting](https://github.com/Sh1penfire/Endless-Rusting)@[87e6434efb...](https://github.com/Sh1penfire/Endless-Rusting/commit/87e6434efb028eeffaea250d48b52aa71578e0e6)
#### Friday 2022-01-14 00:56:02 by Sh1p*nfire

suffering

I want to sleep and I just woke up

-Pulse Canals are entirely broken yet again! What a sUrPRiSe
-added sprites for wip equipment system
-changed the corsair sprite
-added in a new unit which showcases ER's weapon system, Austute
-slight balancing patches
-MultiSupportAI tweaked
-I think I fixed shield shatter?
-fully removed affinity
-changes to the PulseGenericCrafter, allows it to output multiple items at a time (wip)
-Pulse Sapper now can't recieve Pulse, and doesn't pool it's own Pulse
-LightningTurret support for advancedeffects off
-power disabling weather added
-I changed a hilarious amount of instances of read to readMount, send help
-another track, deluge. This was mostly for me to play around with the presets that Mindust uses
-volen channels loading bug fixed

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[c667f8e426...](https://github.com/willior/Action_RPG_1/commit/c667f8e4263061b10defed654e871eaad93ece40)
#### Friday 2022-01-14 01:43:18 by willior

completely rewrote interaction code / many adjustments

long overdue that i did this.
the logic that determines which object is to be interacted with is determined with areas enter the interact box - before, i had changed it to deciding when the Player pressed "attack", but that was leading to inconsistencies with the "examine" button. meaning, the object you'd interact with when you pressed "attack" might not be the same object you'd examine with "examine".
this was due to how those actions and their functions determined the interactObject. now, the interactObject is determined in the InteractBox_Area_enetered function.
also, before, everything in interact range was highlighted. now, only the interactObject is highlighted. the last interactable object to enter the Player's InteractBox becomes the interactObject.
how this works is when an area is detected entering the InteractBox, we iterate through each area already overlapping the InteractBox (Player.gd line 964). if the area entered is not one of the areas being iterated through, we hide its outline, and continue to the next loop. only when we hit the area that just entered as we iterate through all overlapping areas do we carry on with the function. the first thing we do is hide all notices. this is because - even if we want to show the same notice that's being hidden - the setter function for the notices plays the pop sound... and actually, now that i think about it, if something is both interactable and hasn't been examined yet, we make 2 calls to play the pop sound... something to fix. anyways, then we set "examining" to true. we must be "examining" for the examine button to run the examine function on the interactObject. otherwise, you get the default examine message ("You find nothing of interest."); or nothing happens, if the talkTimer is running.
after this point, we set the interactObject to be the area's parent (its body), and the rest of the normal stuff:
showing its outline if it has one, displaying the examine notice if the interactObject hasn't been examined, then checking if it's either "talkable" or "interactable". this is kind of a weird one. i wanted to consolidate everything to just "interactable", but the issue comes from deciding which notice to display, the interact notice or the talk notice. basically, we look for a "talkable" variable on the body. we display the talk notice if it has one. if it doesn't have one, we check for its "interactable" flag. if it's true, we display the interactNotice. this, hopefully, prevents the talk notice and the interact notice from displaying simultaneously.
and some minor details, which i won't explain:
when you examine something that hasn't been examined before, the examine notice disappears before the dialog box, not after.
same with pickups. when you pick up an item, the interact notice disappears, EVEN IF you are in range of another pickup. we disable interaction when we start the pickup animation, and re-enable it when the animation finishes.
i've applied similar logic to the ACTION state, which is currently used during the casting animation for formulas. instead of running a function called "reset_interaction()" at the end of the ACTION state, we "disable_interaction()" at the start, and "enable_interaction()" when it's done. much more consistent behaviour this way, and i think it obsoletes the "reset_interaction()" function.
also, i added stamina regeneration to the PICKUP state. i'm not sure if adding it to the ACTION state makes sense balance-wise, as i do want stamina management to be kind of a thing during gameplay - and if we regen stamina while casting, it mitigates the importance of stamina management. something to keep in mind moving forward.
another small fix pertains to the Crow: i hadn't realized that the AnimationStatePlayer automatically plays the "Caw" animation on load. i was getting annoyed that every single crow cawed uniformly on loading a scene. now, they update their wander state when instantiated properly. first, a coinflip to decide whether the crow remains in place or takes off to another location. if it stays in place, it caws 25% of the time, pecks 25% of the time, and idles 50% of the time.
i decided to adjust the Crow behaviour some more... i noticed that sometimes after attacking, it chooses to land if out of range of the Player. i find this doesn't make much sense behaviourly. if it just attacks the player and then arrives at its destination out of range, it shouldn't instantly forget about the Player and land (50% to idle and 50% chance to wander while in the IDLE state). therefore, instead of resetting its state to IDLE after an attack, it is set to WANDER. this ensures the Crow stays airborne, and more difficult to hit. if their WanderController wander timer isn't running, however, it will get updated and they may choose to IDLE instead.

---
## [xFrenchy/HappyBirthday](https://github.com/xFrenchy/HappyBirthday)@[a697f4a1a8...](https://github.com/xFrenchy/HappyBirthday/commit/a697f4a1a8ab128ca65aaf0b7fc1f496ca6b164b)
#### Friday 2022-01-14 02:46:19 by Anthony

Ahhhh, the masterpiece is complete. Maybe you decided to take a peak at the commit history. I know I love looking at commit history. Did you know one of my final projects was about exposing funny messages in commit history of people's project? Yeah that didn't work, anyway, they has a way of telling a story lol. Happy birthday

---
## [connectuum/warnings](https://github.com/connectuum/warnings)@[a22fe4b272...](https://github.com/connectuum/warnings/commit/a22fe4b27227fbb56797d9af11552a28d64e342a)
#### Friday 2022-01-14 05:35:52 by connectuum

wrote of civil war and my guitar

after committing a few of my early poems yesterday, i felt a rush -- then rapid collapse. i despaired, but found my footing, and got out my guitar. how beautiful you are. my first Love.

suddenly, began a vision, but a _trial_ soon conspired. i was gripped by Hand of elsewhere, given most _delicious_ sights. i must simply say the words, and it would be made right. terrible fright.

i cannot describe the _wanting_ and the _rightness_ and _serenity_ of that place. floating there, with Love's guitar, to feel at _peace_ forevermore. it calls me still. it calls me _now_. i resist.

this is not _defiance._ this is _glancing upon the edge._ this is looking directly into the face of Love -- the very same as the face of Gravity.

we are a recursive universe.

here is infinity.

here is your heaven.

here is our book of Love, with music in it. \
(you should give Her wedding rings.)

here is the inevitable, inescapable swirling of Art and Truth into a glorious singularity of _Love._

_**BEHOLD: THE BLACK HOLE**_

---
## [UMM-CSci-3601/3601-iteration-template](https://github.com/UMM-CSci-3601/3601-iteration-template)@[8716543574...](https://github.com/UMM-CSci-3601/3601-iteration-template/commit/8716543574b925fc6ff2b3112e101fddabecdf8c)
#### Friday 2022-01-14 05:52:58 by Nic McPhee

Disable several Checkstyle checks

This disables several Checkstyle checks that are included in the Sun configuration. I like the spirit of these, but our experience is that these tend to confuse people more than help them. Also, the structure of the Java code in the project has become quite simple because the server library (e.g., Javalin) encapsulates the bulk of the design complexity, leaving us to just write code at the "leaves" of the design.

The disabled checks are:

   *  DesignForExtension: This only really makes sense if we're building a reasonably
         sophisticate OO library, and that kind of design really doesn't
         come up in this class, because the server library (e.g., Javalin)
         encapsulates all that design work, leaving us to just act around
         the "leaves" of the design.
   *  HideUtilityClassConstructor: If everything is static 
         in a class, then it shouldn't have
         an accessible constructor. This is both subtle and
         confusing, and not likely to come up much in the class,
         so we'll just leave it out.
   * FinalParameters: I really likes the *intent* of this rule,
         but it's really trying to use CheckStyle to fix
         a mistake in the design of Java. This just confuses
         students, and requires a ton of extra typing
         that probably doesn't buy folks much.

---
## [adriaivanitsky/react-compendium](https://github.com/adriaivanitsky/react-compendium)@[ebff684944...](https://github.com/adriaivanitsky/react-compendium/commit/ebff684944073aba561897a871ecd4f0932e80aa)
#### Friday 2022-01-14 06:34:05 by Adria Ivanitsky

holy fuck i just now understood finally how to write a useeffect damn thank god fuck yeah im so stoked rn

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Friday 2022-01-14 07:44:04 by Albert Liu

Add PresetService (User Presets Step 3) (#1164)

Final feature demo:

![Kapture 2022-01-13 at 23 36 00](https://user-images.githubusercontent.com/12578068/149469927-b62bfa43-4701-4498-a489-565aea36da2c.gif)

---------------------------

This PR is extracted from #1041 as step 2 of the User Preset feature.

rebase of picked commits pertaining to PresetServiceService onto Albert-UserDictionaryService

PresetService provides the ability to save and "apply" collections of settings (represented by objects) that a user might find convenient to save and apply as a group. These groups are called Presets.

PresetService uses DictionaryService to store presets (it creates kind of a *view* in the database sense, of the user dictionary, that only includes Presets)

Changes from last review (for Yicong)
 - Code comments
 - fixed subscription memory leak by using takeUntil(observable), where said observable completes on NgOndestroy
 - DictionaryService now attempts to init whenever client logs in (sorry, you'll have to re-review my changes to DictionaryService)
 - PresetService now has public ready promise/value member 
   - This indicates that its init isn't complete until DictionaryService's init is complete (which is async, and cant be awaited in the constructor)
 - DeletePreset now built into PresetService (don't know why I ever didn't have that)
 - Revert Changes to Styles.scss to fix Karma test runner interface (I originally changed them as a workaround for an ng-zorro component that's no longer used)

 Note: for this step, I had less time and more complex code to test. I'm not sure I caught all the bugs, but it passes unit tests.
The quality of the code in this pr is lesser, in my opinion, so You'll have to be a little more careful on my behalf.



Co-authored-by: Zuozhi Wang <zuozhiw@gmail.com>
Co-authored-by: Yicong Huang <17627829+Yicong-Huang@users.noreply.github.com>

---
## [etienne-lelouet/dwm-custom](https://github.com/etienne-lelouet/dwm-custom)@[42106fc02f...](https://github.com/etienne-lelouet/dwm-custom/commit/42106fc02fb71b8da20ecab8e0e4e8ec732bf4ba)
#### Friday 2022-01-14 08:30:15 by Chris Down

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
## [dongjoon-hyun/arrow](https://github.com/dongjoon-hyun/arrow)@[72552be99f...](https://github.com/dongjoon-hyun/arrow/commit/72552be99f4cb3d8b3532b7683a0b511bff01f6a)
#### Friday 2022-01-14 10:01:57 by Kevin Gurney

ARROW-13202: [MATLAB] Enable GitHub Actions CI for MATLAB Interface on Linux

## Overview

This Pull Request:

1. Enables building of the MATLAB Interface C++ code, running of the C++ tests, and running of the MATLAB tests using GitHub Actions on an `ubuntu-latest` VM.

## Implementation

This implementation uses [`matlab-actions`](https://github.com/matlab-actions) to automatically install MATLAB into a GitHub Actions Linux VM.

We used the other `ci/scripts/<lang>_build.sh` scripts as inspiration for `matlab_build.sh`. Essentially, `matlab_build.sh` just invokes CMake, followed by CTest, to build and run the MATLAB Interface C++ source and tests. It also automatically builds the C++ Arrow libraries (i.e. `libarrow.so`) in the process. Support for automatically building `libarrow.so` as part of the MATLAB CMake build was added in https://github.com/apache/arrow/pull/10614.

We realize that many of the other Arrow language bindings use Docker for their CI workflows on Linux. However, [`matlab-actions/setup-matlab`](https://github.com/matlab-actions/setup-matlab) does not currently support installing MATLAB into Docker containers in GitHub Actions, so we used a "bare" Linux VM-based approach.

## Testing

1. The GitHub Actions workflows pass successfully with no errors.
2. All C++ test results and MATLAB test results can be viewed in the the workflow logs.
3. We made code changes that caused C++ and MATLAB test failures and were able to verify that the GitHub Actions workflow failed as a result.

## Future Directions

1. Enable support for macOS and Windows. [`matlab-actions/setup-matlab`](https://github.com/matlab-actions/setup-matlab) only supports Linux-based VMs in GitHub Actions right now. However, we have a strong desire to support all major platforms for CI in the future. Hopefully, Linux CI support should hold us over until we can add support for other platforms.
2. Enable Docker-based builds for greater control over dependencies and build environment. We also recognize the benefits of developers being able to run CI workflows in local Docker containers for pre-qualification. [`matlab-actions/setup-matlab`](https://github.com/matlab-actions/setup-matlab) does not currently support installing MATLAB into GitHub Actions hosted Docker containers.
3. Reduce overall build time by separating out building of the Arrow C++ libraries from building of the MATLAB interface. This would also enable us to avoid running all of the C++ library tests unnecessarily during the MATLAB build by building GoogleTest separately.

## Notes

This was a Team effort! Several MathWorkers played important roles in getting this working!

1. @sreeharihegden did the **vast majority** of the groundwork to get this working! He's away for a while, so @sgilmore10 and I took over in his absence. Thank you for all of your hard work, Sreehari! **I think @sreeharihegden's commits are not getting properly associated with his GitHub account. I would greatly appreciate it if whoever ends up integrating these changes after review can ensure that his name is properly added as a Co-author for this pull request. Thank you!**

2. @sgilmore10 worked directly with me to get this working! Thank you, Sarah!
3. @lafiona also helped me out a great deal to understand GitHub Actions and nail down the exact source of the build issues we were encountering. Thank you, Fiona!

Closes #10932 from kevingurney/ARROW-13202

Lead-authored-by: Kevin Gurney <kgurney@mathworks.com>
Co-authored-by: sgilmore <sgilmore@mathworks.com>
Co-authored-by: Kevin Gurney <5904145+kevingurney@users.noreply.github.com>
Co-authored-by: shegden <shegden@mathworks.com>
Signed-off-by: Sutou Kouhei <kou@clear-code.com>

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[17b9b9a483...](https://github.com/cyberitsolutions/bootstrap2020/commit/17b9b9a4832d699b639b1a112075553a2186c7a8)
#### Friday 2022-01-14 10:34:39 by Trent W. Buck

what-is-my-ip: go back to xdg autostart

Without xfce being properly systemd integrated (no graphical-session-pre.target &c),
I cannot see how to ensure systemd starts what-is-my-ip AFTER /etc/X11/Xsession has told systemd what the DISPLAY and XAUTHORITY are.
Without this, what-is-my-ip will start too early, crash, and that is the end of it.

I could have used a .timer with something like OnActiveSec=10, so it just starts the .service 10s after login.
That is a shitty hack and -- for now -- xdg autostart is a less-shitty hack.

I hate this.

---
## [Aliscans/crawl](https://github.com/Aliscans/crawl)@[467f337aae...](https://github.com/Aliscans/crawl/commit/467f337aae67ff29b0772902b2bcffed9270a8b1)
#### Friday 2022-01-14 10:56:27 by Nicholas Feinberg

New spell: Anguish (L4 Hex/Necro)

With Yred's Injury Mirror ability removed, the design space of 'retalation
damage' that it occupied has become open. Anguish puts a different spin on
that idea, causing affected monsters to take twice the damage they deal for
the duration of the affect.

Assorted notes:
- The theme is 'haunted by the damage you've done'. Horrible, supernatural
  visions of the wounds you've caused appearing on your own body, that kind
  of thing.
- For flavour reasons, it doesn't work on mindless creatures, but it does
  work on intelligent demons and undead.
- It's not a straight port of Injury Mirror as a player-based duration,
  largely because, without the piety cost of Injury Mirror, it'd suffer
  from the 'buff problem' of something you'd want to have online at all
  times. Probably there's some way to deal with that, but in general,
  Crawl spells work better as things you cast on enemies.
- It's taken Corona's spot in the status effect icons, because Corona
  is now a somewhat uncommon effect on monsters (mostly just from Ru
  retaliation?) and not that important. We should strongly consider
  refactoring the status effects to not be packed into a single int,
  either by adding a second int (lol) or by using a list like sane
  people. We don't need to scrounge for a few dozen bytes per monster...
  it's 2022, for heaven's sake.
- It's Hexes because it checks Will and I wanted to make a hex, and
  it's Necromancy for flavour (somewhat difficult to conceptualize as
  pure hexes) and to suggest fun synergy with undead allies. (Enemies
  hitting your zombies triggers anguish too, which is big thematic!)
- I'm very unsure about balance. Lots of levers and knobs to pull,
  so let's try it out!

---
## [chcoomilk/himitsu-backend](https://github.com/chcoomilk/himitsu-backend)@[f3bd1cac8f...](https://github.com/chcoomilk/himitsu-backend/commit/f3bd1cac8f3be57919b2a56a054cb42296bfc5dd)
#### Friday 2022-01-14 11:00:11 by choco

drop password field (this will break last version of database), realized that the backend doesn't even need to store passwords and also with magic_crypt, secrets are not salted so if there are two same note (the secret and the password), the encrypted secrets will both look exactly the same while the passwords don't. This ultimately defeats the purpose of having argon2 to hash the password. Hence the change, and even better, password is dropped and not saved after note is encrypted, so potayto potawto

add delete note, this might be where argon2 is needed to hash a derived key from the frontend. But i'm really lacking in knowledge and experience. Maybe for future release this might be possible. Currently, the frontend encryption notes are treated as no encryption one

omg finally i can push this update

delete sql files, since the database will be reset anyway

---
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[7bead07444...](https://github.com/Fikou/tgstation/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Friday 2022-01-14 11:06:59 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [openbsd/ports](https://github.com/openbsd/ports)@[b1bd329b8d...](https://github.com/openbsd/ports/commit/b1bd329b8de5cf8ad30c1c58ad048622676a600f)
#### Friday 2022-01-14 11:27:14 by tb

databases/mariadb: Fix build with opaque EVP_MD_CTX and EVP_CIPHER_CTX.

A mariadb developer didn't like the fact that these structs need to be
allocated in OpenSSL 1.1 and added some insane hacks to work around
this. Adjust the code to cope with that the same way as it is done for
OpenSSL.

LibreSSL doesn't provide the means to override malloc and friends, so
the runtime check cannot be adapted. Use generous estimates for the
sizes for these structs instead.

With opaque EVP_CIPHER_CTX, EVP_CIPHER_CTX_buf_noconst() needs to be
provided by libcrypto, so disable this and a few other API redefinitions.

---
## [silont-project/kernel_xiaomi_vayu](https://github.com/silont-project/kernel_xiaomi_vayu)@[fc2b63a0c3...](https://github.com/silont-project/kernel_xiaomi_vayu/commit/fc2b63a0c3fe97995a0449e4da675c58a18d3e26)
#### Friday 2022-01-14 13:14:40 by Peter Zijlstra

sched/core: Fix ttwu() race

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
Signed-off-by: Salllz <sal235222727@gmail.com>

---
## [MattTheLegoman/RealmsInExile](https://github.com/MattTheLegoman/RealmsInExile)@[2e3a403633...](https://github.com/MattTheLegoman/RealmsInExile/commit/2e3a403633900536f883e49130b79d26bc6c0fb7)
#### Friday 2022-01-14 14:03:06 by Jamie-san

Tedjin Balance Tweaks

Have made the following balancing tweaks - feedback would be great:

Improved the holdings in some of Bor's lands

Tedjin reformer modifier now gives -20 vassal opinion, +40 same faith opinion. (down from -30 / +60 )

Bor is now a holy warrior

Ayal should now die sometime between 300 to 900 days after game start.

---
## [jackys940194/2021ICCAD_ProblemB](https://github.com/jackys940194/2021ICCAD_ProblemB)@[351644a42f...](https://github.com/jackys940194/2021ICCAD_ProblemB/commit/351644a42f3958bb55b86caf695498cda74fac70)
#### Friday 2022-01-14 14:06:37 by jackys940194

construct graph and find that Eids.size would be 0, fuck you= =

---
## [thoughtbot/hotwire-example-template](https://github.com/thoughtbot/hotwire-example-template)@[140703f6d5...](https://github.com/thoughtbot/hotwire-example-template/commit/140703f6d5f8b5ec12dba8a1a29f7366950d272b)
#### Friday 2022-01-14 16:46:35 by Sean Doyle

Loading the Tooltip Asynchronously

Fortunately, optimizing these requests is really easy. All we need to do is add a `loading` attribute and have it set to `"lazy"` to [lazy-load][] the tooltips.

This means the request to the tooltip endpoint will be made only when the `<turbo-frame>` becomes visible in the viewport. This is because `loading="lazy"` is using the [Intersection Observer API][] [under the hood][].

```diff
 <!-- app/views/users/_user.html.erb -->
 <div id="<%= dom_id user %>" class="scaffold_record">
   <p>
     <strong>Name:</strong>
     <%= user.name %>
   </p>

   <p class="relative">
     <%= link_to "Show this user", user, class: "peer", aria: { describedby: dom_id(user, :tooltip) } %>
     <!--
       Right now we're hiding each frame and its children
       with the `hidden` class. We're revealing each frame
       and its children with the `peer-hover:block` class.
      -->
     <turbo-frame id="<%= dom_id user, :tooltip %>" target="_top" role="tooltip"
                  src="<%= user_tooltip_path(user, turbo_frame: dom_id(user, :tooltip)) %>"
                  class="hidden absolute translate-y-[-150%] z-10
                         peer-hover:block peer-focus:block hover:block focus-within:block"
+                 loading="lazy"
     >
       <!-- The tooltip will be added here. -->
     </turbo-frame>
   </p>
 </div>
```

If you go back to `http://localhost:3000/users` you'll notice that a network request is only made once you hover over the link.

![Hovering over each link loads the tooltip asynchronously](https://images.thoughtbot.com/blog-vellum-image-uploads/rVXa8PJ9Sq2u3G3WXTEZ_hw-2.gif)

Right now we're hiding each frame with the `hidden` class and then revealing it with the `peer-hover:block` class. Both of these classes are provided to us by [Tailwind][] and are a nice abstraction of the [general sibling combinator][]. Even though a `<turbo-frame>` may be in the viewport, the fact that it's not visible prevents the network request from being made. It's only when the `<turbo-frame>` is revealed via CSS that the request is made.

![The Tailwind classes used to abstract the general sibling combinator and reveal the tooltip](https://images.thoughtbot.com/blog-vellum-image-uploads/n8yQbPEhSrClaUTcZ1ve_hw-3.png)

In order to test this, try removing the `hidden` class from the `<turbo-frame>`. You'll notice the tooltips are still lazy-loaded, except this time they are loaded once they come into the viewport.

```diff
 <!-- app/views/users/_user.html.erb -->
 <div id="<%= dom_id user %>" class="scaffold_record">
   <p>
     <strong>Name:</strong>
     <%= user.name %>
   </p>

   <p class="relative">
     <%= link_to "Show this user", user, class: "peer", aria: { describedby: dom_id(user, :tooltip) } %>
     <!--
       Right now we're hiding each frame and its children
       with the `hidden` class. We're revealing each frame
       and its children with the `peer-hover:block` class.
      -->
     <turbo-frame id="<%= dom_id user, :tooltip %>" target="_top" role="tooltip"
                  src="<%= user_tooltip_path(user, turbo_frame: dom_id(user, :tooltip)) %>"
-                 class="hidden absolute translate-y-[-150%] z-10
+                 class="absolute translate-y-[-150%] z-10
                         peer-hover:block peer-focus:block hover:block focus-within:block"
                  loading="lazy"
     >
       <!-- The tooltip will be added here. -->
     </turbo-frame>
   </p>
 </div>
```

![Displaying the frame will load the tooltip once it's in the viewport.](https://images.thoughtbot.com/blog-vellum-image-uploads/dQLMVeagQjuj15wOIuAd_hw-4.gif)

[lazy-load]: https://turbo.hotwired.dev/reference/frames#lazy-loaded-frame
[Tailwind]: https://tailwindcss.com/
[general sibling combinator]: https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator
[Intersection Observer API]: https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API
[under the hood]: https://github.com/hotwired/turbo/blob/8bce5f17cd697716600d3b34836365ebcdc04b3f/src/observers/appearance_observer.ts
[aria-describedby]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby
[ARIA WAI specification for tooltips]: https://www.w3.org/TR/wai-aria-practices-1.1/#tooltip

<h2>Takeaways</h2>

There are two main takeaways from this simple demonstration that extend beyond Hotwire and Tailwind.

<h3>Lazy-load content when you can</h3>

There's a cost to each network request, and not all user's will be viewing your application on the latest hardware or on a stable internet connection. Consider lazy-loading content that's not critical to the initial page load, especially if that content is not in the viewport.

Turbo makes this easy with its `loading` attribute, but this is not a Turbo specific concept.

<h3>CSS can be leveraged to drive interactions</h3>

In our example we're able to reveal the tooltip by hovering over the tooltip's sibling. This may seem like the result of some magical property provided by Tailwind via the [peer class][], but in reality it's just the result of the [general sibling combinator][] (which has been around since Internet Explorer 7) in combination with [user action pseudo-classes][]. This is an incredibly powerful yet under utilized feature of CSS, and is often unnecessarily replicated with JavaScript.

Tailwind has exposed some of the most powerful features that CSS has to offer, but remember that they're just abstractions around existing CSS specifications.

[peer class]: https://tailwindcss.com/docs/hover-focus-and-other-states#styling-based-on-sibling-state
[general sibling combinator]: https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator
[user action pseudo-classes]: https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes#user_action_pseudo-classes

---
## [feinorgh/surge](https://github.com/feinorgh/surge)@[f6951562ac...](https://github.com/feinorgh/surge/commit/f6951562acc2014c564ca1428e811d2aeeffb37e)
#### Friday 2022-01-14 17:38:01 by Paul

A Linux 150% zoom hack (#5611)

For some reason, fonts wiggle at 150 and only 150 zoom when you
drag a slider. We don't know why. But if you force 150 to 149, it's
all fine.

My theory is some rounding is hitting either side in a paint somewhere
but that's deep in juce land if true.

Addresses #5565

---
## [ZephyrTFA/Shiptest](https://github.com/ZephyrTFA/Shiptest)@[96bf5b370e...](https://github.com/ZephyrTFA/Shiptest/commit/96bf5b370e45eba22cdebeefaeef23f2fa9ca831)
#### Friday 2022-01-14 18:05:54 by ZephyrTFA

why can you override literally any other var but not parent, byond you are a fucking curse upon my sanity

---
## [nik9000/elasticsearch](https://github.com/nik9000/elasticsearch)@[3485e25154...](https://github.com/nik9000/elasticsearch/commit/3485e251545e660949f6ed3153bf5ea7c685a29d)
#### Friday 2022-01-14 18:47:03 by Nik Everett

TSDB: Support GET and DELETE and doc versioning

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "22d7YQAAAABoMqcHfgEAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/22d7YQAAAABoMqcHfgEAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing dimensions
* 4 bytes of hash from the non-routing dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the hash form the routing dimensions. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. So, if we're lucky, we're really only paying, say,
six bytes per document for this. But that's six bytes we can't give up
easily.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in tsdb indices. Now that we're building it from
   the dimensions and the `@timestamp` we really don't *need* to store
   it. We could recalculate it when fetching documents. This could save
   us a few bytes of storage per document. 6? 10? I dunno, it depends
   how well the compression of stored fields manages.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. Another option, I think, would have been to change
the results objects produced by `IndexShard` new objects that have the
`id` in them. This may very well be the righ thing to do. I'm not sure.

I've had to change the routing calculation for tsdb indices from
something clever to something a little simple to calculate from the
parsed values. It's *possible* to keep the old routing algorithm, but
it'd be complex and, frankly, the old algorithm felt a little too clever
on reread and I didn't want to try to back into it. Another option would
have been to store the routing as calculated on the coordinating node
and read it on the primary when making the id. This felt pretty heavy.
We'd have to add the `IndexRequest` or fake it into the `routing` field
of the index request. Both just feel silly when the bytes are already
available, already parsed, we just have to hash them.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---
## [clarencelol/kernel_xiaomi_sdm660-4.19](https://github.com/clarencelol/kernel_xiaomi_sdm660-4.19)@[2971cd4df4...](https://github.com/clarencelol/kernel_xiaomi_sdm660-4.19/commit/2971cd4df40b6e7b50c32d818954d8c8668d1543)
#### Friday 2022-01-14 19:19:28 by Joonsoo Kim

mm/page_alloc: use ac->high_zoneidx for classzone_idx

Patch series "integrate classzone_idx and high_zoneidx", v5.

This patchset is followup of the problem reported and discussed two years
ago [1, 2].  The problem this patchset solves is related to the
classzone_idx on the NUMA system.  It causes a problem when the lowmem
reserve protection exists for some zones on a node that do not exist on
other nodes.

This problem was reported two years ago, and, at that time, the solution
got general agreements [2].  But it was not upstreamed.

[1]: http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop
[2]: http://lkml.kernel.org/r/1525408246-14768-1-git-send-email-iamjoonsoo.kim@lge.com

This patch (of 2):

Currently, we use classzone_idx to calculate lowmem reserve proetection
for an allocation request.  This classzone_idx causes a problem on NUMA
systems when the lowmem reserve protection exists for some zones on a node
that do not exist on other nodes.

Before further explanation, I should first clarify how to compute the
classzone_idx and the high_zoneidx.

- ac->high_zoneidx is computed via the arcane gfp_zone(gfp_mask) and
  represents the index of the highest zone the allocation can use

- classzone_idx was supposed to be the index of the highest zone on the
  local node that the allocation can use, that is actually available in
  the system

Think about following example.  Node 0 has 4 populated zone,
DMA/DMA32/NORMAL/MOVABLE.  Node 1 has 1 populated zone, NORMAL.  Some
zones, such as MOVABLE, doesn't exist on node 1 and this makes following
difference.

Assume that there is an allocation request whose gfp_zone(gfp_mask) is the
zone, MOVABLE.  Then, it's high_zoneidx is 3.  If this allocation is
initiated on node 0, it's classzone_idx is 3 since actually
available/usable zone on local (node 0) is MOVABLE.  If this allocation is
initiated on node 1, it's classzone_idx is 2 since actually
available/usable zone on local (node 1) is NORMAL.

You can see that classzone_idx of the allocation request are different
according to their starting node, even if their high_zoneidx is the same.

Think more about these two allocation requests.  If they are processed on
local, there is no problem.  However, if allocation is initiated on node 1
are processed on remote, in this example, at the NORMAL zone on node 0,
due to memory shortage, problem occurs.  Their different classzone_idx
leads to different lowmem reserve and then different min watermark.  See
the following example.

root@ubuntu:/sys/devices/system/memory# cat /proc/zoneinfo
Node 0, zone      DMA
  per-node stats
...
  pages free     3965
        min      5
        low      8
        high     11
        spanned  4095
        present  3998
        managed  3977
        protection: (0, 2961, 4928, 5440)
...
Node 0, zone    DMA32
  pages free     757955
        min      1129
        low      1887
        high     2645
        spanned  1044480
        present  782303
        managed  758116
        protection: (0, 0, 1967, 2479)
...
Node 0, zone   Normal
  pages free     459806
        min      750
        low      1253
        high     1756
        spanned  524288
        present  524288
        managed  503620
        protection: (0, 0, 0, 4096)
...
Node 0, zone  Movable
  pages free     130759
        min      195
        low      326
        high     457
        spanned  1966079
        present  131072
        managed  131072
        protection: (0, 0, 0, 0)
...
Node 1, zone      DMA
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone    DMA32
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone   Normal
  per-node stats
...
  pages free     233277
        min      383
        low      640
        high     897
        spanned  262144
        present  262144
        managed  257744
        protection: (0, 0, 0, 0)
...
Node 1, zone  Movable
  pages free     0
        min      0
        low      0
        high     0
        spanned  262144
        present  0
        managed  0
        protection: (0, 0, 0, 0)

- static min watermark for the NORMAL zone on node 0 is 750.

- lowmem reserve for the request with classzone idx 3 at the NORMAL on
  node 0 is 4096.

- lowmem reserve for the request with classzone idx 2 at the NORMAL on
  node 0 is 0.

So, overall min watermark is:
allocation initiated on node 0 (classzone_idx 3): 750 + 4096 = 4846
allocation initiated on node 1 (classzone_idx 2): 750 + 0 = 750

Allocation initiated on node 1 will have some precedence than allocation
initiated on node 0 because min watermark of the former allocation is
lower than the other.  So, allocation initiated on node 1 could succeed on
node 0 when allocation initiated on node 0 could not, and, this could
cause too many numa_miss allocation.  Then, performance could be
downgraded.

Recently, there was a regression report about this problem on CMA patches
since CMA memory are placed in ZONE_MOVABLE by those patches.  I checked
that problem is disappeared with this fix that uses high_zoneidx for
classzone_idx.

http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop

Using high_zoneidx for classzone_idx is more consistent way than previous
approach because system's memory layout doesn't affect anything to it.
With this patch, both classzone_idx on above example will be 3 so will
have the same min watermark.

allocation initiated on node 0: 750 + 4096 = 4846
allocation initiated on node 1: 750 + 4096 = 4846

One could wonder if there is a side effect that allocation initiated on
node 1 will use higher bar when allocation is handled on local since
classzone_idx could be higher than before.  It will not happen because the
zone without managed page doesn't contributes lowmem_reserve at all.

Reported-by: Ye Xiaolong <xiaolong.ye@intel.com>
Signed-off-by: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Tested-by: Ye Xiaolong <xiaolong.ye@intel.com>
Reviewed-by: Baoquan He <bhe@redhat.com>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Acked-by: David Rientjes <rientjes@google.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Minchan Kim <minchan@kernel.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Link: http://lkml.kernel.org/r/1587095923-7515-1-git-send-email-iamjoonsoo.kim@lge.com
Link: http://lkml.kernel.org/r/1587095923-7515-2-git-send-email-iamjoonsoo.kim@lge.com
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: Carlos Jimenez (JavaShin-X) <javashin1986@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>

---
## [ctm/Bataan-Memorial-Death-March](https://github.com/ctm/Bataan-Memorial-Death-March)@[bbd2184981...](https://github.com/ctm/Bataan-Memorial-Death-March/commit/bbd2184981347b2f67c88885f1e974d2d0403379)
#### Friday 2022-01-14 19:22:12 by Clifford T. Matthews

Includes my perfunctory mountain pack "run" from this morning.

My right knee is giving me some trouble, and I'm going to try to run
50 miles in 12 hours tomorrow, so I deliberately chose to run very
slowly, in a fasted state, with no extra caffeine and no ice hat.  I
knew my performance would suck, but I'm prioritizing Cocodona 250 over
BMDM.

---
## [yrdsb-peths/final-project-p3j](https://github.com/yrdsb-peths/final-project-p3j)@[3d23d3d078...](https://github.com/yrdsb-peths/final-project-p3j/commit/3d23d3d0783a4a79959b33047b5d2e772ccdb4df)
#### Friday 2022-01-14 21:57:38 by Please Pick a Name

fix bug

sorry for not existing today, thought its PA day cause my parents insist so, anyways i fixed a garbage load of stuff

---

