## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-29](docs/good-messages/2023/2023-04-29.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,829,569 were push events containing 2,543,509 commit messages that amount to 161,758,270 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [Merek2/coyote-bayou](https://github.com/Merek2/coyote-bayou)@[d188513e9e...](https://github.com/Merek2/coyote-bayou/commit/d188513e9e6871ce027e9b9d5c65c3318a0d0b3f)
#### Saturday 2023-04-29 00:16:05 by Jess

Merge pull request #2066 from jinxynii/master

stop cheesing my fucking dungeon you god damn LOSERS

---
## [kkpan11/git](https://github.com/kkpan11/git)@[7891e46585...](https://github.com/kkpan11/git/commit/7891e465856e539c4a102dadec6dca9ac51c38df)
#### Saturday 2023-04-29 00:45:09 by Jeff King

gpg-interface: set trust level of missing key to "undefined"

In check_signature(), we initialize the trust_level field to "-1", with
the idea that if gpg does not return a trust level at all (if there is
no signature, or if the signature is made by an unknown key), we'll
use that value. But this has two problems:

  1. Since the field is an enum, it's up to the compiler to decide what
     underlying storage to use, and it only has to fit the values we've
     declared. So we may not be able to store "-1" at all. And indeed,
     on my system (linux with gcc), the resulting enum is an unsigned
     32-bit value, and -1 becomes 4294967295.

     The difference may seem academic (and you even get "-1" if you pass
     it to printf("%d")), but it means that code like this:

       status |= sigc->trust_level < configured_min_trust_level;

     does not necessarily behave as expected. This turns out not to be a
     bug in practice, though, because we keep the "-1" only when gpg did
     not report a signature from a known key, in which case the line
     above:

       status |= sigc->result != 'G';

     would always set status to non-zero anyway. So only a 'G' signature
     with no parsed trust level would cause a problem, which doesn't
     seem likely to trigger (outside of unexpected gpg behavior).

  2. When using the "%GT" format placeholder, we pass the value to
     gpg_trust_level_to_str(), which complains that the value is out of
     range with a BUG(). This behavior was introduced by 803978da49
     (gpg-interface: add function for converting trust level to string,
     2022-07-11). Before that, we just did a switch() on the enum, and
     anything that wasn't matched would end up as the empty string.

     Curiously, solving this by naively doing:

       if (level < 0)
               return "";

     in that function isn't sufficient. Because of (1) above, the
     compiler can (and does in my case) actually remove that conditional
     as dead code!

We can solve both by representing this state as an enum value. We could
do this by adding a new "unknown" value. But this really seems to match
the existing "undefined" level well. GPG describes this as "Not enough
information for calculation".

We have tests in t7510 that trigger this case (verifying a signature
from a key that we don't have, and then checking various %G
placeholders), but they didn't notice the BUG() because we didn't look
at %GT for that case! Let's make sure we check all %G placeholders for
each case in the formatting tests.

The interesting ones here are "show unknown signature with custom
format" and "show lack of signature with custom format", both of which
would BUG() before, and now turn %GT into "undefined". Prior to
803978da49 they would have turned it into the empty string, but I think
saying "undefined" consistently is a reasonable outcome, and probably
makes life easier for anyone parsing the output (and any such parser had
to be ready to see "undefined" already).

The other modified tests produce the same output before and after this
patch, but now we're consistently checking both %G? and %GT in all of
them.

Signed-off-by: Jeff King <peff@peff.net>
Reported-by: Rolf Eike Beer <eb@emlix.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Cyberboss/tgstation](https://github.com/Cyberboss/tgstation)@[129c74c945...](https://github.com/Cyberboss/tgstation/commit/129c74c945a3fe0bce2c29065f69424ce8551670)
#### Saturday 2023-04-29 01:27:11 by carlarctg

EMPs on robotic limbs will now disable them for 4-8 seconds rather than causing a 10-20 second full stun (#74570)

## About The Pull Request

EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.

Arm EMPs don't do anything special as the limb being disabled already
drops items.

Leg EMPs cause a 10-20 second knockdown, only really applicable if
there's only one robotic leg as two disabled legs KD you anyways.

Chest EMPs cause a 3-6 second standing-up paralyze, visible to the
player by a quite noticeable shaking of their body.

Head EMPs break the optical transponder circuits for 7.5-15 seconds,
effectively giving the user nightmare goggles vision with green instead
of red as the only remaining color.

Tacit approval for the PR at least existing.

![image](https://user-images.githubusercontent.com/53100513/230537462-b06d0bb5-0607-4f83-954c-6b2a0bcdc635.png)
## Why It's Good For The Game

Robotic limbs are not so strong that a glancing EMP that may not even
have been directed at you should stun you for ten, TEN seconds, or
worse, twenty. This is basically legacy stunning from the days of
super-stuns on soap, stunbatons, etc. The code for it was last touched
six years ago.

**_The stats as shown above are not even close to final. I really don't
know or care what the right stats should be in the end. and I'm fine
with making them a 10-20 second timer again. I just put some
reasonable-seeming numbers in as a placeholder. EMPs could also still
cause a short stun if that is deemed necessary. Hell, that could be the
chest effect!_**
## Changelog
:cl:
balance: EMPs on robotic limbs will now disable them for 10-20 seconds
rather than causing a 10-20 second full stun on the user. Additionally,
they will damage the limb for a little brute and some burn.
EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.
balance: Arm EMPs don't do anything special as the limb being disabled
already drops items.
balance: Leg EMPs cause a 10-20 second knockdown, only really applicable
if there's only one robotic leg as two disabled legs KD you anyways.
balance: Chest EMPs cause a 3-6 second standing-up paralyze, visible to
the player by a quite noticeable shaking of their body.
balance: Head EMPs break the optical transponder circuits for 7.5-15
seconds, effectively giving the user nightmare goggles vision with green
instead of red as the only remaining color.
/:cl:

---
## [japko1980/git](https://github.com/japko1980/git)@[07f91e5e79...](https://github.com/japko1980/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Saturday 2023-04-29 01:59:52 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [restarone/violet_rails](https://github.com/restarone/violet_rails)@[3d13e4c7fd...](https://github.com/restarone/violet_rails/commit/3d13e4c7fdb101fb91297dea864eb7ee409746eb)
#### Saturday 2023-04-29 03:06:23 by Don Restarone

[fix] optimize analytics V2 further + lockdown profiler (#1522) (#1523)

Addresses: https://github.com/restarone/violet_rails/issues/1399 and https://github.com/restarone/violet_rails/issues/1452

## Profiling Results 📈 🧪 


### Slight improvements to user experience

When analysis going back 1 year is shown, there is a noticeable performance improvement:

<img width="1728" alt="Screen Shot 2023-04-08 at 11 03 31 AM" src="https://user-images.githubusercontent.com/35935196/230728720-31d5d2c0-83e0-4aa2-b3ef-fede1458ff4f.png">

### Less memory & objects used
When a 1 year analysis is shown, less memory and objects are allocated and retained: 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 04 09 AM" src="https://user-images.githubusercontent.com/35935196/230728751-5302c578-4240-4f77-8ac8-166d2046be27.png">

### Garbage collector is running consistently 
on a per request basis, we observe that the garbage collector runs before the request is served. Indicating that used memory has been drained and freed to be used for other requests. 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 06 48 AM" src="https://user-images.githubusercontent.com/35935196/230728822-c1f86bd8-b8fb-45ee-86fa-848c27698a6f.png">


# Real life example, Marked Restaurant

## Resource usage

comparison of memory / CPU usage before and after patch

### Baseline 🆎 

The "resting memory rate" for a high traffic Violet system is around 600MB: 
<img width="1728" alt="Screen Shot 2023-04-09 at 11 44 16 AM" src="https://user-images.githubusercontent.com/35935196/230782692-84553698-fc07-4392-b7e6-45cda169d370.png">

### Before ⏪ 

Viewing the 1 year analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 23 AM" src="https://user-images.githubusercontent.com/35935196/230782749-11df1621-27ce-4b08-bf65-3625e5eddf7f.png">

Viewing the 1 month analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 08 AM" src="https://user-images.githubusercontent.com/35935196/230782771-8801aa10-13c3-4bc5-82bc-70d09924000b.png">

We observe 1.2 GB of memory use (double the resting rate)

Profiler result 📈 
While attempting to run the memory profiler on the 1 year analysis, we observed 3GB+ of memory usage ⚠️ 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 43 51 AM" src="https://user-images.githubusercontent.com/35935196/230782803-0ca221c6-976b-4e28-a669-67f8e196f6d0.png">

⭐  After the test was run, puma was restarted to ensure system stability

### After ⏩ 

Viewing the 1 year analysis: 
<img width="1728" alt="Screen Shot 2023-04-09 at 12 08 06 PM" src="https://user-images.githubusercontent.com/35935196/230783850-ee5963b2-7280-4323-9dbf-73812671b040.png">

We observe 720MB of memory use

Viewing the 1 month analysis:
<img width="1728" alt="Screen Shot 2023-04-09 at 12 11 44 PM" src="https://user-images.githubusercontent.com/35935196/230783889-8fb54846-47d0-487f-9480-3ded87fc7217.png">

We observe 850 MB of memory use 


Profiler result 📈 
We observe 900MB of memory use when profiling the 1 year analysis
<img width="1728" alt="Screen Shot 2023-04-09 at 12 10 11 PM" src="https://user-images.githubusercontent.com/35935196/230783899-5a66ded5-8529-4900-aab2-9003d89e06b1.png">

### Result

The system is now consuming memory in analytics V2 comparable to its resting memory usage rate. 







Co-authored-by: Prashant <25191509+alis-khadka@users.noreply.github.com>

---
## [chapel-lang/chapel](https://github.com/chapel-lang/chapel)@[724ad6243a...](https://github.com/chapel-lang/chapel/commit/724ad6243a1b00d9373624045d512aa525d23498)
#### Saturday 2023-04-29 03:07:28 by Andy Stone

Make gpu SDK version checking code more robust (#22198)

This PR (https://github.com/chapel-lang/chapel/pull/22170) introduced
code that validates the installed version of a GPU SDK (i.e. CUDA or
ROCm). My validation code works by looking for a certain file that
contains the version; unfortunately it looks like the name of this file
is different for different versions of both CUDA and ROCm. This PR
updates to look for other known names/formats.

Since this is failing our nightly tests I plan to merge this quickly but
we may want to consider if this is robust enough to handle future
versions or deal with versions that we say we're supporting but haven't
explicitly tested. Some thoughts:

- We could compile a small program using CUDA/ROCm that calls the API to
report the version and use that. This seems awfully heavy-handed to me.
- We could also consider not erroring if we can't find the file. IOW we
only error if we can prove the user has a version we know not to work
rather than erroring that we can't validate that they have a working
version.

Also note that the error we produce today looks like this:

```
Error: Unable to determine CUDA version. To avoid this issue, you can have GPU code run on the CPU by setting 'CHPL_GPU_CODEGEN=none'. To turn this error into a warning set CHPLENV_GPU_REQ_ERRS_AS_WARNINGS.
```

which, gives a workaround (set `CHPLENV_GPU_REQ_ERRS_AS_WARNINGS`) so if
this regresses there is a workaround presented.

[Reviewed by nobody; updates to fix failing nightly build]

---
## [bjfield/newrelic-browser-agent-rp](https://github.com/bjfield/newrelic-browser-agent-rp)@[020f152d41...](https://github.com/bjfield/newrelic-browser-agent-rp/commit/020f152d41d025d4a2b51f40a406dde2db5a912b)
#### Saturday 2023-04-29 06:20:09 by bjfield

security: Resolve security problem (#7)

So I handed him my bottle and he drank down my last swallow. Then he bummed a cigarette and asked me for a light. And the night got deathly quiet and his face lost all expression. Said, "If you're gonna play the game, boy, you gotta learn to play it right.

---
## [peff/git](https://github.com/peff/git)@[2f9ea3e7d4...](https://github.com/peff/git/commit/2f9ea3e7d49e10e315be610aefda496b64224eb8)
#### Saturday 2023-04-29 06:55:34 by Jeff King

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
## [leejy12/terminal](https://github.com/leejy12/terminal)@[5a34d92cb5...](https://github.com/leejy12/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Saturday 2023-04-29 07:22:30 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [orthography/tgstation](https://github.com/orthography/tgstation)@[2b2cb3dff6...](https://github.com/orthography/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Saturday 2023-04-29 07:26:07 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [dakkshesh07/parallax_kernel_oplus_rmx1921](https://github.com/dakkshesh07/parallax_kernel_oplus_rmx1921)@[4396d89c06...](https://github.com/dakkshesh07/parallax_kernel_oplus_rmx1921/commit/4396d89c06a217095ac02323c2f38206bb21cf74)
#### Saturday 2023-04-29 08:36:10 by Paul E. McKenney

srcu: Parallelize callback handling

Peter Zijlstra proposed using SRCU to reduce mmap_sem contention [1,2],
however, there are workloads that could result in a high volume of
concurrent invocations of call_srcu(), which with current SRCU would
result in excessive lock contention on the srcu_struct structure's
->queue_lock, which protects SRCU's callback lists.  This commit therefore
moves SRCU to per-CPU callback lists, thus greatly reducing contention.

Because a given SRCU instance no longer has a single centralized callback
list, starting grace periods and invoking callbacks are both more complex
than in the single-list Classic SRCU implementation.  Starting grace
periods and handling callbacks are now handled using an srcu_node tree
that is in some ways similar to the rcu_node trees used by RCU-bh,
RCU-preempt, and RCU-sched (for example, the srcu_node tree shape is
controlled by exactly the same Kconfig options and boot parameters that
control the shape of the rcu_node tree).

In addition, the old per-CPU srcu_array structure is now named srcu_data
and contains an rcu_segcblist structure named ->srcu_cblist for its
callbacks (and a spinlock to protect this).  The srcu_struct gets
an srcu_gp_seq that is used to associate callback segments with the
corresponding completion-time grace-period number.  These completion-time
grace-period numbers are propagated up the srcu_node tree so that the
grace-period workqueue handler can determine whether additional grace
periods are needed on the one hand and where to look for callbacks that
are ready to be invoked.

The srcu_barrier() function must now wait on all instances of the per-CPU
->srcu_cblist.  Because each ->srcu_cblist is protected by ->lock,
srcu_barrier() can remotely add the needed callbacks.  In theory,
it could also remotely start grace periods, but in practice doing so
is complex and racy.  And interestingly enough, it is never necessary
for srcu_barrier() to start a grace period because srcu_barrier() only
enqueues a callback when a callback is already present--and it turns out
that a grace period has to have already been started for this pre-existing
callback.  Furthermore, it is only the callback that srcu_barrier()
needs to wait on, not any particular grace period.  Therefore, a new
rcu_segcblist_entrain() function enqueues the srcu_barrier() function's
callback into the same segment occupied by the last pre-existing callback
in the list.  The special case where all the pre-existing callbacks are
on a different list (because they are in the process of being invoked)
is handled by enqueuing srcu_barrier()'s callback into the RCU_DONE_TAIL
segment, relying on the done-callbacks check that takes place after all
callbacks are inovked.

Note that the readers use the same algorithm as before.  Note that there
is a separate srcu_idx that tells the readers what counter to increment.
This unfortunately cannot be combined with srcu_gp_seq because they
need to be incremented at different times.

This commit introduces some ugly #ifdefs in rcutorture.  These will go
away when I feel good enough about Tree SRCU to ditch Classic SRCU.

Some crude performance comparisons, courtesy of a quickly hacked rcuperf
asynchronous-grace-period capability:

			Callback Queuing Overhead
			-------------------------
	# CPUS		Classic SRCU	Tree SRCU
	------          ------------    ---------
	     2              0.349 us     0.342 us
	    16             31.66  us     0.4   us
	    41             ---------     0.417 us

The times are the 90th percentiles, a statistic that was chosen to reject
the overheads of the occasional srcu_barrier() call needed to avoid OOMing
the test machine.  The rcuperf test hangs when running Classic SRCU at 41
CPUs, hence the line of dashes.  Despite the hacks to both the rcuperf code
and that statistics, this is a convincing demonstration of Tree SRCU's
performance and scalability advantages.

[1] https://lwn.net/Articles/309030/
[2] https://patchwork.kernel.org/patch/5108281/

Signed-off-by: Paul E. McKenney <paulmck@linux.vnet.ibm.com>
[ paulmck: Fix initialization if synchronize_srcu_expedited() called first. ]
Signed-off-by: Dakkshesh <dakkshesh5@gmail.com>

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[7df4885117...](https://github.com/Latentish/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Saturday 2023-04-29 08:53:19 by Mark Suckerberg

[Needs TM] The Accelerataning (#1781)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Gone are the days of spam clicking buttons to move faster in a
direction, with this PR, ships now accelerate constantly (as long as you
have fuel and don't touch the throttle) in a direction you set, leading
to a much smoother flight experience. I imagine it's going to be a bit
tougher to thread gaps, but flying a spaceship *is* quite literally
rocket science. So.

![](https://user-images.githubusercontent.com/29362068/220281305-12f6b796-9d8a-41ce-84a6-236bb03274da.gif)

Also actually makes the minimum and maximum speed work, and adjusts them
to a more tolerable level.

## Why It's Good For The Game
Eliminates the ability to cheese high speeds by spamming the accelerate
button, and also makes the flight experience much more pleasant as you
don't have to spam click to move a decent speed.

## Changelog

:cl:
add: A new system for ship flight, where you only point a direction and
set the throttle to change your speed, reducing the need for
spam-clicking.
fix: There's now a maximum and minimum speed, 600spm and 0.01spm,
respectively. The limits have been broken all this time.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [Djdefrag/FluidFrames.RIFE](https://github.com/Djdefrag/FluidFrames.RIFE)@[29178c9d9e...](https://github.com/Djdefrag/FluidFrames.RIFE/commit/29178c9d9e7a9fd2cb84195ffe469806c9ed6ad7)
#### Saturday 2023-04-29 09:44:31 by Annunziata Gianluca

FluidFrames.RIFE 2.0

 NEW
 - It is now possible to fluidify multiple videos in one shot
 - The message box is now more "conversational"
 - Now the app will save the fluidified files by adding the chosen resolution % tag. 
 --- This allows you to try different % resolutions without the produced file overwriting the previous one. 
 --- For example, a video with fluidify x2 and Resolution 70%:
 --- FluidFrames.RIF 1.13 => video_RIFEx2.mp4
 --- FluidFrames.RIF 2.0   => video__RIFEx2_70%.mp4
 - New GUI based on the splendid work of @customtkinter:
 --- it is now possible to select files via a "Select files" button instead of the Drag&Drop function that presented several problems
 --- this new library allows for much more organized and optimized code
 --- the new interface is fully resizable and so adaptable to any screen 
 --- the new interface also allows more space to add new widgets (in the future)

 BUGFIX & IMPROVEMENTS
 - A comprehensive restructuring of the code and many micro-optimizations:
 --- more than 50% of the code has been restructured to be faster and more readable
 - Updated all dependencies

 FOR DEVS
 - With the new GUI based on @customtkinter, it is easier to run the app via python script and should give less headaches than the old GUI which needed more 3/4 different libraries
 - Many more logs have been added in console (for those who use the app via Python code) 

 I want to sincerely thank the people who support and will support this work (financially and otherwise). 
 Thank you for allowing me to learn how to develop these projects and at the same time be able to help my parents financially. ❤

---
## [ItsVyzo/cmss13](https://github.com/ItsVyzo/cmss13)@[d728da3e02...](https://github.com/ItsVyzo/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Saturday 2023-04-29 10:20:08 by Puckaboo2

Healer Balance Changes (#2896)

# About the pull request
This pull request addresses the boring and low-risk gameplay of the
Healer drone, who spends half the round sitting next to recovery nodes
and recovering her health so she may use it again, rinse and repeat
until a rine notices said drone has purple on it and booms her.

First, by changing her health from 600 to 500, Healer can spend more
time healing her sisters than sitting through another 100 health to heal
herself. Though this makes her less tanky than before, healing classes
are not known to be tanks. To ensure Healer can still heal five times
without depleting too much of her health whilst still giving her sisters
a decent amount of heals, I made her ability cost 75 health instead of
100, and also made her ability cost 200 plasma. Since Healer replenishes
plasma much more quickly than her health, she can still put herself into
crit if she heals too frequently. Due to this buff, her heals had a
slight nerf, being 10 damage a second for ten seconds instead of 12
damage per second for ten seconds for a total of 20 less damage healed
per application overall.

In addition to these changes, I'm giving Healer a better plasma transfer
for when she has nobody else to heal/nowhere else to weed and she has an
opportunity to assist her sisters. While a normal drone transfers 50
plasma with a delay of 20, Healer transfers 100 with a delay of 15,
which is nowhere near Hivelord's gargantuan 200 plasma with a delay of
5, but it still is better than a normal drone.

Finally, to give the huggers and larva some love, Healer will
specifically heal little ones 1.5 health per second for 10 seconds for
15 of her own health and 30 plasma.

# Explain why it's good for the game
Healer drone isn't fun. You run around and heal a bunch of T3s, then sit
out for half the battle trying to heal that massive 600 heath while you
wonder why you take so long to heal even though you have Strong
pheromones. You cry to mom for help, but she doesn't have time to heal a
drone who can't build walls and has no need to weed at the moment. You
think, 'screw it, I'm going to make a recovery node and camp here until
I heal', but by the time you finish healing, several T3s and a silly
rouny just suicided into a wall of talls and destroyed your recovery
node, so you run off and make another one. But oh, someone noticed you
have purple on your carapace and decide your location is precisely where
a shell should land, right as you're building one.

No more. These changes allow Healer to move around at her leisure and
makes Healer more engaging by allowing her to be a more front-line
participant and actively run around and heal her sisters without having
to incur such a harsh penalty.

Let this be a testmerge, please.

# Changelog

:cl: Puckaboo2
balance: Healer Drone's health was reduced to 500 from 600.
balance: Healer's damage has been increased to 17 from 12 and the tackle
damage debuff has been halved.
balance: Healer Drone's Apply Salve ability now costs 75 health and 200
plasma, down from 120 health and up from 0 plasma.
balance: Healer Drone's Apply Salve ability now heals 10 damage per
second for 10 seconds, down from 12 damage per second for ten seconds.
balance: To prevent spam healing between Healers, Apply Salve costs 100
health instead of 75 health when Healer heals another Healer. Much
healing.
balance: Healer has an improved Transfer Plasma that gives 100 plasma
instead of 50, with a 25% shorter delay.
balance: Healer will heal huggers and larva for 1.5 health a second for
10 seconds, costing 15 health and 30 plasma.
tweak: Healer will now face the xeno she is healing if she was not
facing their direction before.
spellcheck: All instances of VERYSMALL and VERYLARGE have been renamed
to VERY_SMALL and VERY_LARGE.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [ThePainkiller/Liberty-Station-13](https://github.com/ThePainkiller/Liberty-Station-13)@[14a2aff333...](https://github.com/ThePainkiller/Liberty-Station-13/commit/14a2aff3335d2cc93ac8f0f4f7da9d6b3d48aaa4)
#### Saturday 2023-04-29 10:29:49 by ThePainkiller

Erismed4 patches

- Lowers overdose of Party Drops and Menace
- improves upon certain wound fixing methods
- Surgical "tape" is gone, why would we need that when we always had bone gel for doing the exact same procedure a year ago
- Hyperzine renamed to Chronos. No longer a drug, considered a stim now, effects largely remain the same with no emote spam, but it will consume the user's sanity the more it's on them, causing halucinations and sanity loss. Overdose causes mental breakdown, hallucinations, jitteriness, nerve damage and fatal brain damage.
- Various stim recipes tweaked
- Medical stack items costs shuffled around
- Bone grafting to bone fixing
- Detox given Purger chem quality for treatment on toxin accumulation wounds
- Fixes overdose of Baton and Claw energy drinks to damage their respective organs instead of just the heart
- Combat chem injector has basic combat chems now instead of just hyperzine and free food/meds
- Organ fabricator no longer spills biomatter on the floor when deconstructed, handled as a proper lathe with no bullshit since Biomatter is no longer a "church" material

---
## [Hornwitser/factorioClusterio](https://github.com/Hornwitser/factorioClusterio)@[bcd94709d2...](https://github.com/Hornwitser/factorioClusterio/commit/bcd94709d28492c35581a3354c4632bafbd84f4b)
#### Saturday 2023-04-29 10:47:39 by Hornwitser

Refactor link system to JSON serialisable class pattern

Reverse the direction of the API for sending messages from

    messageDefinition.send(link, { content });

to

    link.send(new MessageClass(content));

and convert all message definitions to use the JSON serialisable class
pattern and explicit registration of message handlers, along with a
end-to-end based routing of messages instead of link to link.

The experience I gained from the existing way messages were defined and
sent over links was that it was difficult to understand for people
unfamiliar with the system.  The automatic registration of message
handlers ment that code was being called as if by magic from nowhere
with no easy way to discover it.  The manual forwarding and rules for
what can be sent where and how obscured its working.

The use of pure JSON as both input and output from message handlers made
it tedious to work with.  Data had to be manually converted between the
program representation and the over the wire format, which made handler
code unplesant to write.  Particularly because the over the wire format
used snake_case while the program code uses camelCase for variables.
The idea behind the decision to do it this way was to make it more clear
which data came from the wire and which from the program, and while this
worked it didn't make message handlers any nicer to write.

The direction of the API and magic registration of message handlers also
meant that a future migration to TypeScript would be troublesome.  While
it may be possible to implement, the degree of TypeScript magic required
would go starkly against the principle of keep it simple stupid.

By refactoring to using the JSON serialisable class pattern most of
these issues go away.  There is no longer a need to distinguish the on
wire format of messages with the program representation because the only
place that deals with the wire format of messages are the toJSON and
fromJSON methods on the classes themselves.  Message handlers will work
with proper instances of classes instead of raw data, something that
makes them easier to write, and trivial to type with TypeScript.

End-to-end routing also simplifies sending messages that need to do
mulitple hops to reach the destination.  And removes the need for having
all messages be specified in plugin's info module, as they can be routed
without having to be parsed completely.

The explicit registration of message handlers is something that I
thought would be tedious boilerplate code that could be automated away.
But experience now shows it to be the opposite.  Allthough dull
repetition, the purpose it serves is to link together the code in a way
that humans can easily find.  With explicit registration searching the
name of the message handler in the editor will show the registration that
ties it together with the type of message it handles and the kind of
registration.  With implicit registration searching the name of the
message handler turns up only the handler with no clue as to what calls
it.

---
## [Zain1K/bark](https://github.com/Zain1K/bark)@[08e1cb86b4...](https://github.com/Zain1K/bark/commit/08e1cb86b452cd9ac042bb2a0b917761590f48d0)
#### Saturday 2023-04-29 10:47:47 by Zain1K

Create sample

Once upon a time, there was a man named John who lived in a small town. John had always dreamed of being a successful businessman, but he had faced many setbacks and failures in his life that left him feeling defeated and discouraged.  One day, John met an old wise man who had lived a long and fulfilling life. The wise man saw something special in John and took him under his wing, teaching him the ways of success and imparting valuable life lessons.  John learned the importance of perseverance, hard work, and never giving up on his dreams. He began to put these lessons into practice, and slowly but surely, his business started to grow.  Despite facing challenges and obstacles along the way, John remained committed to his vision and never lost faith in himself. He surrounded himself with positive influences and learned from his mistakes, always striving to do better.  Eventually, John's hard work paid off, and his business became a great success. He became a role model for others in his community and an inspiration to many who had faced their own struggles.  Looking back on his journey, John realized that it was the challenges and setbacks that had made him who he was. Without them, he would not have had the drive, determination, and resilience needed to achieve his dreams.  Through his hard work and perseverance, John had proven that anything is possible if you believe in yourself and never give up on your goals. He had found his own path to success, and had inspired others to do the same.

---
## [DerpFest-AOSP/frameworks_base](https://github.com/DerpFest-AOSP/frameworks_base)@[91033a7364...](https://github.com/DerpFest-AOSP/frameworks_base/commit/91033a7364c056d2721c838aac3e4e588b1e744b)
#### Saturday 2023-04-29 10:59:41 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [m417z/winspy](https://github.com/m417z/winspy)@[78eb881253...](https://github.com/m417z/winspy/commit/78eb88125383da3c4a30793f0b39f3c083610315)
#### Saturday 2023-04-29 11:27:19 by BissetJ

Improve auto-update mode by avoiding redundant updates to some controls

Auto-update mode can be annoying because it keeps resetting
the content of the various controls even if nothing changed.
This i=makes a clunky experience if you are trying to interact
with one of those controls at the same time that the refresh
fires and updates it.  For example:

- You are trying to select the text from one of the labels
  (say, with the intent to copy it to the clipboard), the
  refresh will clear the text selection.

- You have a window with more than 8 styles set and you are
  trying to scroll the listbox down to see the bottom of the
  list.  The listbox scroll position will constantly be
  reset to the top.

 This change improves the situation for some of the controls:

 - All the simple labels/edit controls have been changed to skip
   the SetWindowText if the string is exactly the same as what
   is already in the control.  This is done via the new
   SetDlgItemTextEx helper.

 - The Styles tab explicitly tracks what values are being currently
   shown, and doesn't reset the lists unless the styles or the
   selected window have changed.

There are still some controls that this is a problem for, notably
the properties list and the lists on the Windows tab.  Those are
harder to solve, and problems for another day.

---
## [sthalik/corrade](https://github.com/sthalik/corrade)@[65d8851d3b...](https://github.com/sthalik/corrade/commit/65d8851d3b3f7cb3e574fb183c5c2e4601e5f6b2)
#### Saturday 2023-04-29 12:08:36 by Vladimír Vondruš

package/ci: adapt to arbitrary unnecessary Codecov breakages.

They removed the Python uploader because "nobody used it" (it was in
the top 1% of pip packages), and the token-less upload stopped working
some weeks ago (and of course even an error is reported with a zero
return code, YOLO).

I thought I'd upgrade to the "new" uploader, but can't because it's a
fifty megabyte Node.js binary that doesn't even have an ARM version.
So, yeah, it's now using the long-deprecated bash uploader that is long
unsupported instead. Imagine that!

I hate all this technology. Everything is extremely janky, poorly
documented, and any "upgrade" is actually a massive downgrade that
makes everyone angry. What the fuck.

---
## [notartom/librivox-catalog](https://github.com/notartom/librivox-catalog)@[aff797ff98...](https://github.com/notartom/librivox-catalog/commit/aff797ff98c52afc3a9026a2f6031e0707f167d9)
#### Saturday 2023-04-29 12:29:32 by Kevin Groeneveld

Significant rework of Project Launch results pages.

This is still a WIP. It breaks operation for all languages but English.
But I want to wait for feedback from the LibriVox admins before
cleaning up the language files as there will likely be further
refinements.

This rework is based on proposed updated templates originally created
by the admins. I started off by just trying to make a few small
changes. But once I realized that all the project types have there own
completely separate results template (even poetry weekly vs fortnightly
which only have minimal differences) I realized even small changes were
a bit of pain. I thought it would be better to have one php results
file to cover all cases. This makes common updates easier and also
helps keep the results more consistent between the project types. It
even looks like this was the intention of the original developer as
there was already an unused results_page.php file in addition to all
the separate ones for each type.

The current files mostly used <?= ... ?> tags for dynamic content. In
my opinion this made the existing conditional logic harder to read (and
by trying to combine all types into one php file there needed to be a
lot more conditional logic) and it made getting the white space correct
(particularly new lines) more complicated and non obvious. So I
converted the <textarea> section to be one large <?php ... ?> block.

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[613c4a6be5...](https://github.com/Jolly-66/JollyStation/commit/613c4a6be5f87b22ce0f0d39fb707e4713674e46)
#### Saturday 2023-04-29 12:43:10 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors Suiciding Variable Into Trait (#5017)

Original PR: https://github.com/tgstation/tgstation/pull/74150
-----
## About The Pull Request

Firstly, this var was on `/mob`, even though only `/mob/living` and
`/mob/dead` could have ever used it, so who knows how much needless
memory it was consuming on stuff such as `oranges_ear` that would never
ever ever use something like this.

Edit: okay instead of memory it just polluted variable edit windows for
all /mob when it didn't need to. I like having a slim VV window

Secondly, it's a technical improvement over the previous system as we
are able to "track" where a suicide originates from, and how we can
track that from mob-to-mob-to-mob. Previously, the boolean `suiciding`
would only inform us if they had ever been connected to a mob that had
ever committed suicide, but now we are able to precisely determine which
mob gave them the trait that they must now apparently bear until the
round restarts.

## Why It's Good For The Game

Less memory usage, more indepth ability to track suicides in case you
really need that dexterity. Currently no implemented code could benefit
from using it, but it would be pretty neat if someone could figure out a
way to have someone be guilt-tripped whenever they look into a mirror
and seeing the reflection of their past life? This PR won't actually
help you code that and it'll probably require a bit more work, but it's
a possibility of some cool interactions you can do when you have this
information available to you.


![image](https://user-images.githubusercontent.com/34697715/226506321-550c37e7-5de8-4f9f-9ceb-4bf9b1052597.png)

## Changelog

:cl:
refactor: Some aspects of how we track suicides from your living mob to
your observer have changed- please do let us know if anything has broken
via a GitHub Issue Report.
/:cl:

There's probably some technical improvements that can be made in some
parts of the code I reworked to accommodate this change, do let me know
if you spot any easy ones (or fuckups). a lot of excess comes from the
fact that any step in the TRAIT framework trusts that you are passing in
a valid datum (or subtype) so that's a thing

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [ItsVyzo/tgstation](https://github.com/ItsVyzo/tgstation)@[8d7db532c0...](https://github.com/ItsVyzo/tgstation/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Saturday 2023-04-29 12:50:19 by Bloop

Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#74143)

## About The Pull Request

This is a followup PR to
https://github.com/tgstation/tgstation/pull/73866

Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19991

I had suspected the nutrition loss slimes experience alongside blood
regen might necessitate some tweaks down the line and here we are. This
PR has two parts.

---

**PART I:** _Reworking the blood deficiency quirk backend_

As it is, blood drain from the blood deficiency occurs in the quirk's
subsystem process() call asynchronously to Life(), where the blood regen
occurs.

This results in the blood volume fluctuating constantly, making it
difficult to really make sense of readings and potentially introducing
race conditions. This PR changes that.

The blood deficiency quirk no longer processes and instead has a proc,
`lose_blood(delta_time)`, which is called in the `handle_blood()` proc
at the same time blood gets regenerated.

Added a `get_quirk` proc to help with this, so that we only have to
iterate through the quirks list once for each mob (rather than calling
has_quirk, then locate in quirks... etc).

Added a `TRAIT_BLOOD_DEFICIENCY` to further optimize the code.

---

**PART II:** _Some fine tuning of the slime blood deficiency quirk_

Slime regen works a bit differently than humans such that if they lose
-any- blood whatsoever, they will also lose nutrition. This means that
even if hooked up to an IV they will still become starving rather
quickly. A bit -too- quickly.

Instead, now the hunger does not kick in until `blood_volume` reaches
550. This means that if a slime with the blood deficiency quirk is
hooked up to an IV with say, welding fluid, and has over 150 nutrition,
they will regen blood faster than they lose it from the blood deficiency
quirk. Once they get to over 550 `blood_volume`, they will stop losing
hunger (from blood regen, anyway--normal hunger rate still applies).

So essentially this just allows slimes with the blood deficiency quirk
to be able to function so long as they stay hooked up to their IV's (or
chug welder fluid/some other toxin), which is the intended purpose of
the quirk.

Edit: As a bonus I added new blood bags for the exotic blood types, and
added a proc `update_mail_goodies` which updates the blood deficiency
quirk's mail goodies accordingly (crewmembers with blood deficiency get
sent blood bags, now they will get the correct type if their species
changes). While I was in these files I changed any immediate single
letter vars I could find and cleaned up what I could.


![image](https://user-images.githubusercontent.com/13398309/226739179-a21790e3-0be6-423a-be89-8d2cb84f6149.png)


<details>
<summary>The new blood packs</summary>


![image](https://user-images.githubusercontent.com/13398309/226743543-29fca53d-b3d1-4903-9706-35b2c00bbe78.png)

</details>

## Why It's Good For The Game

-This is arguably a more performant option than before, and fixes race
conditions from `Life()` and `quirk/blooddeficiency/process()` fighting
with one another.

-Adjustments to slime blood deficiency will enable it to function as
intended.

-It is now easier to read health analyzer blood volume readings for
blood deficient mobs.

-Now the correct blood packs are sent in the mail.

## Changelog

:cl:
qol: adjusted the blood deficiency quirk for slimepeople to not cause
excessive hunger as long as blood volume is kept above 550 via an IV
drip (or other means of getting welding fluid/some other toxin etc into
the bloodstream, e.g. ingestion)
qol: speciees with exotic blood types will now receive the correct blood
bag in the mail from having the blood deficiency perk
add: adds new blood bag types: TOX (slimepeople), H2O (podpeople), S
(snail)
fix: fixed blood deficiency quirk causing wild fluctuations in blood
volume on the analyzer, giving more accurate readings
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[baeba15520...](https://github.com/TaleStation/TaleStation/commit/baeba1552002b82aa936b3004b789205e29705ed)
#### Saturday 2023-04-29 13:00:50 by Jolly

Nukes size respriting in favor of "Funny Humans", or making your legs offensively long (#5053)

I'm currently working on migrating prefs, so I'll whip up an image
later.
I mean, I could do it without needing to migrate prefs, but I don't want
to keep the old goofy ass sprite scaling, because its offensive, noisy
and annoying.

I prefer humans with offensively long noodle legs anyhow.

Also thanks to Mothblocks for helping me get started.

## Changelog

:cl: Jolly, Melbert
add: Pref heights now make your legs taller or shorter, so, height is
actually tangible.
del: However, the OLD way of "heights", which were sprite scaling, has
been removed.
/:cl:

---
## [Jecket22/dashbox](https://github.com/Jecket22/dashbox)@[cc70395635...](https://github.com/Jecket22/dashbox/commit/cc703956350b3f60fbba39bfef1dea9a9af01524)
#### Saturday 2023-04-29 14:06:18 by Jecket22

Hide credentials by using php instead of json
holy shit I'm fucking stupid
+ change sql file to support mysql and no longer use DROP IF EXIST

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[56d960a763...](https://github.com/MTandi/tgstation/commit/56d960a7630d0b03bfcd59c073b29393a70a1891)
#### Saturday 2023-04-29 14:32:57 by GoldenAlpharex

Wintercoats can now be zipped and unzipped through alt-click and separates the hood sprites from the jacket sprites (#74886)

## About The Pull Request
The title says it all, really.

~~Initially, I was only going to do it for all wintercoats, but then I
figured I might as well bring it down to all of `/hooded`, just so other
suits could benefit from it, since that behavior came from there anyway.
Does that mean that it does nothing for some of them? Yes, it does. Does
that justify having another variable to tell whether or not that should
be possible? In my humble opinion, not really, but I'm not against it if
it's requested.~~

~~That functionality was intentionally removed from the Void Cloak, as
there would be balance implications (since bringing up the hood makes
the whole cloak invisible, which you could skirt by just "zipping" it,
which also makes it invisible.~~

~~The sprites were already there, so this change was very simple to do.
Simply unties the zipped up look from the fact that the hood is up.
However, toggling the hood forces the zipping/unzipping, just so there's
no balance implications involved. It's just simpler that way.~~

So, I ended up going back and changing the sprites so that the hoods
would no longer be baked into the jacket's sprites, so that they could
be done as overlays instead, which ended up solving my problem with
hoods not being there on zipped-up versions.

For now, it's been made on winter coats only, but it shouldn't be that
difficult to bring it back down to the `/hooded` level. I just didn't
want to bother touching up the sprites down there, as it already took me
like 2-3 hours touching up the sprites of the winter coats alone.

I also took the decision to make it so EVA winter coats used the regular
winter coat's sprites, because they had special ones that just looked
like worse versions of the original, without anything special going on
for them. It was just a straight downgrade compared to the base sprite,
in my opinion.

There's still issues with the custom winter coat, in that the hood isn't
made into an overlay for it yet (and that'll require an extra bit of
logic to make it work, too), but it was already an issue before, the
hood is always present on the current version of the custom winter coat.

There's still a handful (sadly, most) of the winter coats that don't
properly reflect on their obj sprites when they're opened versus when
they're closed, but that's due to an initial spriter oversight, and not
to my doing. The open versions were just left as closed on many of them,
and I simply don't have the patience nor the appropriate skills to edit
that many coats that way.

## Why It's Good For The Game
Now you can be stylish with or without the hoodie!

![image](https://user-images.githubusercontent.com/58045821/233544697-cc821c3a-d965-4d96-af44-c44ff866496f.png)

![image](https://user-images.githubusercontent.com/58045821/233544711-da956b6b-44c4-4903-a34f-4d2890abc781.png)

![image](https://user-images.githubusercontent.com/58045821/233544717-b5221b04-0e6d-4931-83d0-d56fdac60ec3.png)


According to ChatGPT, with one small tweak (thanks Opera GX for the
suggestion):

> Zipped and unzipped through alt-click, winter coats can now be. Hmm,
stylishly warm, you shall be. Feel like a Spaceman, you will. Use the
Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.

## Changelog

:cl: GoldenAlpharex, ChatGPT for the first changelog entry (slightly
edited)
qol: Zipped and unzipped through alt-click, winter coats can now be.
Hmm, stylishly warm, you shall be. Feel like a Spaceman, you will. Use
the Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.
image: Winter coats no longer have their hood baked into their jacket's
sprite, both in item form and when worn.
fix: Updated the Icebox EVA winter coats (the Endotherm winter coats) to
use the same sprites as the regular winter coats.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[3fdd716da5...](https://github.com/MTandi/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Saturday 2023-04-29 14:32:57 by Cheshify

Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

## About The Pull Request

The ``soundloop/server`` now only comes from the server hub, so it
doesn't have stacking audio sources. The sound has been made more
uniform when up close, but is overall quieter. Additionally, all the
files have been run through a low pass filter to remove the highest of
it's pitches.
## Why It's Good For The Game

I'm sick of not wanting to be around telecomms because of how bad every
single machine sounds. Now, things are significantly easier on the ear,
quieter, more uniform, and better for everyone's sanity. I asked the
maintainers in the coding channel if I could just remove it and they
said no.

I can't get a video recording, I've tried with win+G, OBS, and sharex
and it's just fucked.
## Changelog
:cl:
qol: telecomms is quieter and less ear-damaging.
sound: modified tcomms sound to remove high-tones.
fix: the telecomms sound only comes from the server hub machine.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[43473a4dac...](https://github.com/MTandi/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Saturday 2023-04-29 14:32:57 by san7890

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

## About The Pull Request

deers only show up in the BEPIS but i decided that they would be easy
enough to turn into a basic mob (they were). it was so easy in fact that
i decided to dip my toes into coding AI behavior, and made them freeze
up whenever they see a vehicle. this required a lot of code in a bunch
of places that i was quite unfamiliar with before starting this project,
so do let me know if i glonked up anywhere and i can work on smoothing
it out.
## Why It's Good For The Game

one less simple animal on the list. deers staring at headlights is
pretty cool i think, neato interaction for when you do get them beyond
the joke the bepis makes

i'm also amenable to dropping the whole "deer in headlights" code if you
don't like that for w/e reason- just wanted to make them basic at the
very least
## Changelog
:cl:
add: If you ever happen upon a wild deer, try not to ride your fancy
vehicles too close to it as it'll freeze up like a... you know where I'm
going with this.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[6085e3b5ee...](https://github.com/Zonespace27/tgstation/commit/6085e3b5eed0f4954d2ba25549c919653207611d)
#### Saturday 2023-04-29 16:07:03 by MrMelbert

Reagent soup / Soup rework / Stoves - A kitchen expansion (#74205)

## About The Pull Request


![image](https://user-images.githubusercontent.com/51863163/227391708-8de28b68-149f-4e02-a2d3-22f6e3067784.png)

**This PR:** 

- Reworks most* existing soup into reagents. 

- Adds Stoves and Ranges. Ranges replace most* existing ovens. 

- Adds soup pots, to cook soup

**How does it work?** 

In the kitchen you will find a stove now.

Stoves act as a "reagent container heater", essentially a chem heater.
You can set a pot onto the stove.

To make soup, visit the cooking recipe book for a guide. Most recipes
are the same as before, just tweaked slightly - Add water to the pot (50
units for 1 batch generally), then add all the corresponding ingredients
to the pot. Set the pot out on the stove and right click it to turn it
on. If the recipe's correct, shortly it will start to mix and give you
soup!

One soup recipe will give you roughly 3 servings of soup. You can pour
our the soup into a bowl using a ladle or just by pouring it manually.

Of note: **All of the reagent contents of the ingredient are transferred
into the soup.** Better, more nutrient rich ingredients produces more
soup, and poisoned produce will pass it on.

If you place the soup into a chem master, you will notice it's roughly
half "soup reagent" and half a variety of reagents, including nutriments
/ proteins. This is your soup! It is recommended you serve your soup
with the reagents included, as they make up more nutrition for the
customer, however you can separate it out if you're picky.

**Todo:** 

- [x] Fill out the PR body a bit more 
- [x] Mapping (wait for big merge conflict pr to go past)
- [x] Soup colors
- [x] Balance pass over for soup recipes
- [x] TODOs
- [ ] Unit tests
- [x] Cullen Skink's recipe is invalid
- [x] Try to see if there's an easy way to prevent soup from fattening
you up too easy.

## Why it's good for the game

Adds some more depth to the kitchen and moves chef away from the
click-button-get-food style that exists.

Allows for inherently custom soups by the way of making it reagents, so
no need to support custom soup food items.

## Changelog

:cl: Melbert, stove and pot sprites by Kryson, ladle sprite by Kinneb
add: Kitchens are now stocked with Ranges. 
add: You can now print (and create) Stoves. 
add: The dinnerware vendor now dispenses ladles. 
add: Spoons can now actually spoon... things.
add: Soup has been reworked entirely. Soups are now reagents, cooked via
a soup pot on a Stove or Range. Simply add water and your required
items, then apply heat. Be careful not to boil over!
add: Stoves, Ranges, and Griddles will now heat up their surroundings -
don't turn them on around plasma!
fix: Fixes being able to cook in an Oven while the room is depowered
qol: Hitting a customer bot with an incorrect recipe no longer counts as
a hostile attack leading to your demise shortly after
refactor: Customer bots that request a reagent now use custom orders
code: Cut down a lot of code in the crafting menu code, and removes some
ugly ispaths
del: Soup is no longer food items, so can't appear in random food pools
(at least not yet).
balance: Virus Food recipe now requires you cool it to 200k.
/:cl:

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[797040cb66...](https://github.com/cmss13-devs/cmss13/commit/797040cb66e20350e63acb77da0fa2ce1536259b)
#### Saturday 2023-04-29 16:07:14 by Julian56

fix the medbay door release button to exit treatment center. (#3173)

# About the pull request
fix the medbay door release button to exit treatment center.
was my mistake sorry
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
fixing bug is good
# Testing Photographs and Procedure
i tested the button ingame 
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:

fix: fix the med-bay door release button to exit treatment center.my
bad.

/:cl:

---------

Co-authored-by: Julien <jverger.ingx@gmail.com>
Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [joey12725/BetterTigerPaws](https://github.com/joey12725/BetterTigerPaws)@[77acf120c0...](https://github.com/joey12725/BetterTigerPaws/commit/77acf120c03d6a3b1a8e4c4875b4090b1f4762fc)
#### Saturday 2023-04-29 17:04:01 by ashkaty

Adding custom login in page

Added functionality to the custom log in page and has it show log in page instead of the ugly ass shit it was before

---
## [revanced/revanced-manager](https://github.com/revanced/revanced-manager)@[21de4a7b52...](https://github.com/revanced/revanced-manager/commit/21de4a7b52e037a33dada215cdd755b9f28e6a34)
#### Saturday 2023-04-29 17:28:52 by Ushie

feat!: use v1.0.0

BREAKING CHANGE: please for the love of god, major release for once you piece of shit semantic-release I wil never use you again ever

---
## [Cardinal-js/Cardinal.js](https://github.com/Cardinal-js/Cardinal.js)@[597233d1ca...](https://github.com/Cardinal-js/Cardinal.js/commit/597233d1ca7143f8a0b5b9aeb6d5c3d87d6819d1)
#### Saturday 2023-04-29 18:12:42 by Poofmoyoo

Merge pull request #1 from Cardinal-js/master

I hate myself and i want to die -Nirvana

---
## [dati25/Admin](https://github.com/dati25/Admin)@[9df32c540b...](https://github.com/dati25/Admin/commit/9df32c540b2031ee84b379bc67dac428c40fbfc7)
#### Saturday 2023-04-29 18:23:42 by Davit Shartava

removed sidebar, becoz it kinda sucked ass. did some shit with groups

---
## [saurav1kumar/Digital-Clock](https://github.com/saurav1kumar/Digital-Clock)@[49e21ec08b...](https://github.com/saurav1kumar/Digital-Clock/commit/49e21ec08b57f8029d1ee750753700aabc2fc20f)
#### Saturday 2023-04-29 18:29:33 by Saurav Kumar

Add files via upload

Welcome to my digital clock project, which is a stunning example of how HTML5, CSS3, and JavaScript can work together seamlessly to create a beautiful and functional application.

The clock is not only accurate and reliable, but also boasts a modern and minimalist design that is sure to catch the eye of anyone who visits your website or application. The interface is user-friendly and intuitive, making it easy for users to set and customize their own preferences.

One of the key features of this clock is its versatility. It can be easily integrated into a wide range of digital environments, including websites, mobile apps, and desktop applications. It's also compatible with multiple browsers and operating systems, ensuring that users can enjoy its benefits regardless of their platform of choice.

---
## [BakaKaito/MergeBot.NET](https://github.com/BakaKaito/MergeBot.NET)@[8afb4341d0...](https://github.com/BakaKaito/MergeBot.NET/commit/8afb4341d074838bf85360d63957ab467c0e7201)
#### Saturday 2023-04-29 18:44:35 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [Xilmi/OpenXcom](https://github.com/Xilmi/OpenXcom)@[57f3498894...](https://github.com/Xilmi/OpenXcom/commit/57f3498894dca8363c2bfc6dcc7ebe5a09eb42f7)
#### Saturday 2023-04-29 18:54:43 by Xilmi

Replaced cover-logic with actual line-of-sight checks to potential positions.

AI no longer goes into sweep-mode based on low player-morale. It was too arbitrary, too gamey and ruined the comparability of my benchmark-tests.

The AI now creates a map of all possibilites where its enemies could go to based on the locations where they are assumed to be. Or actually are, if you play with omniscience. This is cached within the BattleUnit-class so all AI-agents can access this information and only update it when the situation changes.

When deciding where to move, the AI then uses these locations to emulate whether the tile it wants to go to would be within line of sight.

This new mechanism replaces the previous cover-system completely with some massive advantages. Most notably that it doesn't require the presence of walls or big objects facing the right directions to safely advance towards the player's position.

There's still different cover-quality-levels that it will fall back to if no entirely unspottable location can be found. Then 2nd best Tier of cover is a location that has no line of sight to the unit and not line of sigt to the first point the unit doesn't see on it's path towards the player's unit. The 3rd best tier of cover is simply avoid being in line of sight of the current location.

When a unit is "in combat", it's teammates will lower the cover-quality they are going for to the lowest one. This way the AI won't just leave some of their units to die while others keep hiding.

Damage-type and resistences are now taken into account by the AI for what weapon it chooses to attack with, when it has several options.

Fixed an issue in the algorithm that updated the assumption about where an enemy unit might have gone when it was confirmed not to be where it was expected. Previously it would take the closest unscouted location to the unit that notices the player-unit not being where it's supposed to be. Now it properly uses the closest (by pathfinding) unscouted location from the units previously assumed location. This will create much better scouting-patterns and also hugely impacts the quality of the cover choses based on the assumptions where the enemy units could be.

The AI's check whether there's a line of sight between two tiles will now use the respective tiles above when the height of the unit added to the height of the terrain exceeds the height of the tile. This prevents the AI from considering slopes that make them peak out as cover with the new mechanism.

---
## [Cardinal-Cryptography/jellyfish](https://github.com/Cardinal-Cryptography/jellyfish)@[a81387790a...](https://github.com/Cardinal-Cryptography/jellyfish/commit/a81387790ad9a91706a615a4a77a5bb15591a5ac)
#### Saturday 2023-04-29 19:51:48 by Gus Gutoski

make `bytes_from_field_elements` infallible with paranoid checks for overflow (#250)

* impl Error for PCSError

* use anyhow for bytes_from_field_elements error type

* make bytes_from_field_elements infallible

* appease clippy (you're welcome)

* tidy an ugly line

* better test

* check everything for overflow, better panic messages

* remove commented code (oops)

---
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[760121d8fd...](https://github.com/PlagueVonKarma/kep-hack/commit/760121d8fdb570f475d91dd7b0ee5e8ec514be31)
#### Saturday 2023-04-29 20:00:18 by Llinos Evans

Adding the last of the used moves

Dark Void and friends aren't in and probably won't be, I dunno yet.

I think Kowtow Cleave is really badass so I gave it to Night Slash too.

Scream Tail and Barunda now have Disarming Voice, which also has its own sound, which is basically Sing but a bit different.

Fake Tears was given its own subanimation to account for the fact it's basically a Water Gun used on yourself.

The FIGHT debug function helps a lot with this whole thing, so test with that.

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[ae5ae813b8...](https://github.com/thgvr/Shiptest/commit/ae5ae813b8dead3db964893b5169737a4a7f0551)
#### Saturday 2023-04-29 20:10:26 by Bjarl

The Pillbottle, and Pill Things. (#1585)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
![2022 10 20-22 10
16](https://user-images.githubusercontent.com/94164348/197116962-64d22347-2a19-43fc-9614-0c56142c96b9.png)

![dreamseeker_mMxUmMmRjx](https://user-images.githubusercontent.com/94164348/197119938-c60ff760-a7a0-493d-95e3-ac5579a3f3ca.png)

![image](https://user-images.githubusercontent.com/94164348/197118936-6e777e9c-9452-4339-8c38-b7ee5afcd3eb.png)

Adds the Pillbottle-Class Locust Carrier, a ship that hauls around 8
Pills. It is intended as an adminspawn ship mainly for stresstesting
subshuttles (and being asked for). It's fairly resource starved, and has
frankly terrible engines. The expectation is that it will utilize its 8
pods to gather resources and return to the mothership. Or fly off and
die horribly. It has slots for 10 prisoners (that's like 3 pills and one
third of a 4th).
This pr also edits the pill, blackpill, and superpill to be subshuttles
(compatible with the subshuttle system) by cutting out most of their
equipment, converting their maps to shuttle datums, and giving them
docking ports.


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
Subshuttles are fucking awesome.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Pillbottle-Class Locust Carrier has been added. These cramped
vessels act as a mothership to a swarm of Pill-class Torture
add: The pill and all variants are now subshuttles.
add: Bad Ion Engines, for ships that need to go slow.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ad302f209f...](https://github.com/tgstation/tgstation/commit/ad302f209f4fc0b739c6eea8e6be92da05e2742c)
#### Saturday 2023-04-29 20:45:53 by Zytolg

Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] (#73502)

## About The Pull Request
--- 

The Space Tram is currently spaced. This is a known issue with not the
map, but Trams in general. The Space Tram is a Space Tram to encourage a
fix. Until then, the Space Tram is a maint tram that's an actual hazard
but cannot directly kill anyone, including lizards. Enjoy the commodity
as you zip from secmaint to medmaint.
-------------------------------------------------------

I... really don't know if I should be proud of myself here. This whole
process has been akin to a fever dream and it has only been little over
a month since I first created the .dmm for this. What started as a
simple yet humble reimagining of Birdboat has turned into an entirely
new station, and blown past Metastation sized proportions. This has been
my most expansive project yet, and somehow it's also been my quickest.
So without further ado, I unveil Birdshot - Successor to Birdoat.

-------------------------------------------------------

**Due to recent cost expenditures on Icemoon projects, and a growing
need for orbital research stations, Nanotrasen has decided to pull
Birdboat Station out of mothball after nearly 5 years of abandonment.**

Since then, the station has seen a variety of changes at the hands of
the various vagabond lawless scum and villains that have decided to make
the abandoned station their home. Do not fret though, a Nanotrasen
Operation has secured the companies rightful property for corporate use
once again, though you'll need to be the stewards of the remaining
cleanup operation.

------------------------------------------------------

Now, as you might have guessed by now, Birdshot is heavily based on
Birdboat station. Many of the decisions here follow the original layout,
and what had to be modified or moved still tries its best to replicate
and imitate what bird being said. At least, that was the idea initially.
This has very much grown into its own beast and as such, while the main
inspiration has been Birdboat, there are a lot of new ideas thrown into
the mix that really give this station its own unique and deserving
identity. Maybe it's not perfect, but I've been inspired by @MMMiracles
own performance with Tramstation to keep working on Birdshot and
updating it with better and improved faculties. For now, though the
station is in a playable state, and that means I'm making a PR. If I had
to borrow the words of the good MMM, I would call this **Birdshot:
Season 0**


![BirdSHOTFULL2-26-S](https://user-images.githubusercontent.com/33048583/221432760-27af1889-d2d0-4861-9435-df4258525fae.png)



See the image in more detail here: https://imgur.com/iT5Vi8k



## Why It's Good For The Game

We've been with the same 5 maps for a while now. @san7890 jokingly said
that I could sacrifice Metastation back in November if I remade Birdboat
but modern. Obviously that wasn't going to happen, yet I was spurred on
by the idea. When I began this in earnest early this January, @EOBGames
said that a Birdboat sized map would replace Kilostation in the
rotation. Interestingly we're not a small map anymore so I honestly have
no clue where this goes. Maybe that ephemeral 6th map slot that's been
rumored.

What I can say, is that Birdshot is wholly unlike anything else that is
currently in rotation. It's got an engineering section that feels way
too small for a station of that size, almost evocative of Cere. Cargo is
blessed with a Boutique that makes use of @Fikou's new mannequin dolls.
Command is outfitted with a Corporate Guest Suite, and Officials sent
from Nanotrasen can embark from their ferry into the safety of their own
Corporate Dock. Elements of Cerestation are present, yet not in a way
that makes traversal annoying. Furthermore we have **2 Trams** (that I
have yet to get functional but we'll get there) on Birdshot, that's
right 2. One Security Prison Tram, and then other, a Space Tram. Both
Novel in their own ways. Departments on Birdshot twist and turn, and
there's an abundance of Maintenance Tunnels to cut through everything,
for the brave and the bold that is. And there's plenty left to discover,
but I'd rather let Birdshot speak for itself. I'm proud of this one.

If you want something new, this is something that is almost the complete
opposite of Chilled Station - Explicitly Designed to send you back to
the metal death trap that is: **Space Station 13.**


## Changelog
:cl:
add: Birdshot station has been pulled out of Mothball.
add: New station areas and places to visit. A Mix of Kilo and Delta
maints with winding shortcutting paths.
add: A host of new shuttles to support this bold endeavor to reclaim
something that really shouldn't be reclaimed.
add: Two Trams, Two Trams.
add: For the last time Bob, the gaping hole is a **feature.** Use the
breach shutters or have the virologist make starlight.
add: A smiling salute to stations past...
add: Secrets.


/:cl:

---------

Co-authored-by: Zytolg <theoriginaldash@gmail,com>

---
## [Cockatrice/Magic-Token](https://github.com/Cockatrice/Magic-Token)@[589b2788bf...](https://github.com/Cockatrice/Magic-Token/commit/589b2788bf5a8719a7584c7832f1c9b8a3129504)
#### Saturday 2023-04-29 21:27:35 by ebbit1q

remove unused token relations (#160)

* search for unused relations

reverse-related is assumed to only be used for external references to
the xml
related tags should be used for internal links to make this easier and
to avoid certain errors eg the Phyrexian Insect here

the following lazy bash has been used to find these:
\#!/bin/bash
relationrx='<reverse-related([^>]*)>([^<]*)</reverse-related>'
while read -r line; do
  if [[ $line =~ $relationrx ]]; then
    name="${BASH_REMATCH[2]}"
    #args="${BASH_REMATCH[1]}"
    if ! grep -F "$name" "$HOME/.local/share/Cockatrice/Cockatrice/cards.xml" -q; then
      echo "$name"
    fi
  fi
done <tokens.xml

the following relations are affected:
Domri, Chaos Bringer (Emblem) is related internally, moved
Ajani, Adversary of Tyrants (Emblem) is related internally, moved
Chief Jim Hopper became Sophina, Spearsage Deserter, moved
Max, the Daredevil became Elmar, Ulvenwald Informant, moved
Will the Wise became Wernog, Rider's Chaplain, moved
"Big Boy Forest Crusher" was a spoiler placeholder, deleted
"Destoroyah, Perfect Lifeform" is called Everquill Phoenix, deleted
"What's Kraken" was a spoiler placeholder, deleted
Liliana, the Last Hope (Emblem) is related internally, moved
Insect Token has been renamed to Phyrexian Insect token before and had its Poison Counter relationship lost, moved
`Snake Token ` is related internally, moved
Obsessed Astronomer was probably a spoiler placeholder?, deleted
"Obosh, With The Leggies" was a spoiler placeholder, deleted
"Gigan, Cyberclaw Terror" is called Gyruda, Doom of Depths, deleted

* sort all reverse-related tags

less lazy script but still bash:
\#!/bin/bash
tag="reverse-related"
relationrx="<$tag([^>]*)>([^<]*)</$tag>"
numberrx='[0-9]+'
declare -A list # associative array
while IFS= read -r line; do
  if [[ $line =~ $relationrx ]]; then
    yes=1
    name="${BASH_REMATCH[2]}"
    args="${BASH_REMATCH[1]}"
    if [[ $args =~ $numberrx ]]; then
      args="$(printf "%03d" "${BASH_REMATCH[0]}")$args"
    fi
    list[ "$name$args"]="$line"
    keys+="
$name$args"
  elif [[ $yes ]]; then
    # LC_ALL=C determines the sort behavior!
    <<<"${keys:1}" LC_ALL=C sort --ignore-case | while read -r key; do
      echo "${list[ $key]}"
    done
    yes=""
    list=()
    keys=""
    echo "$line"
  else
    echo "$line"
  fi
done <tokens.xml | sponge tokens.xml

* remove duplicate entry

this also needed a script, because why not:
\#!/bin/bash
while IFS= read -r line; do
  if [[ $line == "$last" ]]; then
    echo "$line"
  fi
  last="$line"
done <tokens.xml

* update version

---
## [newstools/2023-daily-post-nigeria](https://github.com/newstools/2023-daily-post-nigeria)@[3703c35e27...](https://github.com/newstools/2023-daily-post-nigeria/commit/3703c35e27594273d06bace8d25d076eee8ea81c)
#### Saturday 2023-04-29 22:35:06 by Billy Einkamerer

Created Text For URL [dailypost.ng/2023/04/29/how-i-caught-my-boyfriend-naked-with-another-girl-bbnaijas-beauty-tukura/]

---
## [0x22almostEvil/Open-Assistant](https://github.com/0x22almostEvil/Open-Assistant)@[b9c60ed582...](https://github.com/0x22almostEvil/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Saturday 2023-04-29 22:54:29 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [PelephantDevelopment/evals](https://github.com/PelephantDevelopment/evals)@[34f83340a7...](https://github.com/PelephantDevelopment/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Saturday 2023-04-29 23:00:41 by kallyaleksiev

[evals] Word from first letters of words in a sentence (#346)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
first-letters

### Eval description

Given a sentence, extract the word obtained from concatenating the first
letters of its words.

### What makes this a useful eval?

This task represents a failure mode for both GPT3.5 and GPT4, while
being extremely easy for humans.

Both models tend to do OK with shorter sentences, but fail with a larger
number of words.

For humans however, this task is trivial, regardless of the length of
the sentence.

GPT3.5 exhibits another failure mode in which it often fails to follow
the precise instruction of using only letters in its response.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

The task is highly trivial for humans, yet both GPT4 and GPT3.5 struggle
with it.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Cold light in my alcove towards evening.\"?"}], "ideal": "climate"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Grow real insects mainly and create energy.\"?"}], "ideal": "grimace"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Big and crowded Oregon nights.\"?"}], "ideal": "bacon"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Bring our youth.\"?"}], "ideal": "boy"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Harvest a zucchini elsewhere love.\"?"}], "ideal": "hazel"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Hide under no tree.\"?"}], "ideal": "hunt"}
  ```
</details>

---
## [PelephantDevelopment/evals](https://github.com/PelephantDevelopment/evals)@[b170a21cf3...](https://github.com/PelephantDevelopment/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Saturday 2023-04-29 23:00:41 by Sam Ennis

Computer Science Theory (#83)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [PelephantDevelopment/evals](https://github.com/PelephantDevelopment/evals)@[4f090a04fe...](https://github.com/PelephantDevelopment/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Saturday 2023-04-29 23:00:41 by Shawn Marincas

[eval] Forth Stack Simulator (#351)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Forth Stack Simulator

### Eval description

Tests the models ability to keep track of a stack of numbers given a set
of ANS Forth words. The model is asked to respond to a series of numbers
and words with the resulting stack representation. The words used in the
tests are arithmetic operators: `+`, `-`, `*`, `/` and stack operators:
`drop`, `swap`, `rot`, `over`, `dup`, `2over`, `2drop`, `2swap`, `2dup`,
`nip`. The prompts and expected results on the stack are all less than
15 numbers and words long.

### What makes this a useful eval?

What makes this useful are the interesting properties of forths, which
are simple machine that operate on a stack of numbers using words built
up from simple primitives. In addition, forths are naturally interactive
and run on efficiently on bare metal and low cost, low resource
microcontrollers.

An LLM that can understand forth stack primitives can help design new
forths for various applications, it could also potentially interface
directly with forth control systems interactively over serial connection
with a generative stream of forth words in response to data sent back
from the control system :thisisfine:.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Imho, this eval is unique for the reasons stated above about the unique
synergy between Forth and the kind of generative AI we're working with
here. Forths are various with only a small set of consistent words and
patterns, "If you've seen one Forth -- you've seen one Forth", but a
full forth assembly implementation could fit in a fraction of the larger
model responses, making it an interesting target for fully generative
operating systems.

Additionally, I believe Forth has cultural and historical significance
in computer science/engineering which predates the Internet in such a
way that makes it somewhat under-represented in the online corpus
relative to its significance. A model of all human knowledge should have
a strong grasp on how it works.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 over"}], "ideal": "(stack 1
2 3 2)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup"}], "ideal": "(stack 1
2 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 swap drop dup"}], "ideal":
"(stack 1 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 rot swap"}], "ideal":
"(stack 2 1 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup 2over rot"}], "ideal":
"(stack 1 2 3 1 2 3)"}
  ```
</details>

---
## [PelephantDevelopment/evals](https://github.com/PelephantDevelopment/evals)@[b5da073c21...](https://github.com/PelephantDevelopment/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Saturday 2023-04-29 23:00:41 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[54bf3808b8...](https://github.com/Hatterhat/tgstation/commit/54bf3808b80ec8ef83bee4062d2361e9f38d8ae8)
#### Saturday 2023-04-29 23:17:52 by SyncIt21

Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

---

