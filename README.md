## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-01](docs/good-messages/2022/2022-03-01.md)


1,744,005 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,744,005 were push events containing 2,824,798 commit messages that amount to 230,731,270 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [MC-Market-org/mcm4csharp](https://github.com/MC-Market-org/mcm4csharp)@[9133ee8f46...](https://github.com/MC-Market-org/mcm4csharp/commit/9133ee8f46df49e03532e676cc764124241f6692)
#### Tuesday 2022-03-01 00:01:27 by AllyMarthaJ

Note to self, Ally sucks at coding at night. Debugging + fixes.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[1067dcffb3...](https://github.com/LemonInTheDark/tgstation/commit/1067dcffb37f8c99c9e76e45dcd93b36cd0cf9cf)
#### Tuesday 2022-03-01 00:39:23 by LemonInTheDark

Adds a colorblind accessability testing tool

I keep finding myself worrying about if things I create will be parsable
for colorblind people. So I've made a debug tool for approximating
different extreme forms of colorblindness.

It's very very much a hack. We can't do the proper correction required
to actually deal directly with long medium and short wavelengths of
light, so we need to rely on approximations. Part of that means say,
bright things being brighter then they ought to be. S not how people
actually experience things, but it's not something we can do anything
about in byond.

Anyway uh, it works by taking color matrixes, and using the plane master
grouping system floyd added to apply them to most all parts of the game
you would want to color correct.

There's some slight fragility here, but I couldn't think of a better way
of handling it.

We also need to deal with planes that have BLEND_MULTIPLY as their
blendmode, since that fucks up the filter. I've come up with a hack for
it, since I wanted to avoid breaking anything.

Oh and since I want it to apply to huds too I added plane masters to
represent them. I think that's about it.

---
## [abnerrjo/Naruto_Ninpou](https://github.com/abnerrjo/Naruto_Ninpou)@[41313d9d7e...](https://github.com/abnerrjo/Naruto_Ninpou/commit/41313d9d7e350d8192fb024fec099d317638e39a)
#### Tuesday 2022-03-01 00:56:19 by AkatsukiGhost

Random

Haven't Done:

- Fixed transformation silence bug
- Fixed permanently paused unit bug
- Fixed Sasori ring gold cooldown being global
- Fixed Onooki Q movespeed issue
- Fixed bug with -autobuy not doing the correct stat build if you used -swap, type -autonew to refresh after swap and then -autobuy
- Fixed Edo Tobirama being paused longer then he should in his W
- Fixed Yata Mirror pause still pausing if the invulnerability is purged
- Added Light Attack passive to the perfect ultimate weapons
- Changed Spirit Orbs damages or adjusted % a little (spirit effects are all the same for Ultimate / Elemental Weapons)
	- Splash Damage (passive, 50 damage bonus in 300 radius)
	- Bash (passive, 15% chance to stun for 1s)
	- Chilling Attack (passive, 50% slow for 1.5s)
	- Corrosive Attack (passive, -10 armor)
	- Chain Lightning (passive, 5% chance to deal 300 damage)
	- Critical Strike (passive, 15% to deal 6 x damage)
	- Light Attack (passive, 10% chance to silence for 1s)
- Dark Totsuka now causes -10 armor on auto attacks
- Fixed Executioner Blade being unable to get picked up from your box
- Thunder Totsuka now has a 5% chance to proc chain lightning
- Heaven Stone corrosive attacks from -25 to -15
- Reduced Shinigami Mask corrosive attacks from -15 to -10

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[4051ad647e...](https://github.com/tgstation/tgstation/commit/4051ad647e3e94ea5c722cee18cecf350270ab6f)
#### Tuesday 2022-03-01 01:17:22 by LemonInTheDark

Space drifting fixes and cleanup (#64915)

* Fixes infi pushing off something in space

Right now you can just push "into" a dense object forever, and depending
on your move rate, just kinda glide

We can fix that by checking if we're trying to push "off" something
we're moving towards

* Makes pushing off something shift it instantly

Currently if you kick off something in space it waits the delay of the
move to start drifting. Looks dumb, let's not

* Updates backup movement to properly account for directional windows. GOD I HATE DIRECTIONAL DENSITY SHOOOOOT MEEEEEEEEEEEEEEEEEEE

* Uses range instead of orange so standing on the same tile as a directional counts properly, rather then suddenly entering a drift state. I hate it here

* Ensures all args are named, updates implementations of the proc with the new arg

---
## [hasperxz/PocketMine-MP](https://github.com/hasperxz/PocketMine-MP)@[f506c922b5...](https://github.com/hasperxz/PocketMine-MP/commit/f506c922b501d733f1ea90e556f97738b6ebff69)
#### Tuesday 2022-03-01 01:20:39 by Dylan K. Taylor

phpstan.neon.dist: fix indentation inconsistency
fuck you, phpstorm!

it doesn't have an option to use tabs for indentation in YAML, and YAML is the closest thing to NEON, so ...

---
## [rayat-amperity/react-date-range](https://github.com/rayat-amperity/react-date-range)@[b3ef7e7930...](https://github.com/rayat-amperity/react-date-range/commit/b3ef7e7930f3cb730ce2fb9a8a38994b83f0f196)
#### Tuesday 2022-03-01 02:07:49 by rayat

Sort README props table alphabetically

Thank you so much for this library and its ongoing maintenance and development - I love it and depend on it in many ways. 

I wish to contribute a documentation PR whose need is prob imaginary on my part, but is arguably more in-line with typical conventions or assumptions ( at least as far as random tables of text on the internet are concerned ). 

I could not discern a pattern or sort-order by which this table was previously ordered, however I found myself frequently wishing it were so alphabetically. I ask that you consider this PR as I frequently would look for props whose exact spelling I did not know or remember, yet at least had a good guess for the first few letters, or let me know if anything else is requested on my part.

If may have missed any preferred sort-order, I apologize!!

Also, I used the github "edit file" feature - I hope I did not mess up any templates or PR rules. Please let me know and I'll remake this ASAP.

Thanks again for all the hard thankless work.

---
## [Sedna-Games/Zero-Possession-Prototype](https://github.com/Sedna-Games/Zero-Possession-Prototype)@[64478f1022...](https://github.com/Sedna-Games/Zero-Possession-Prototype/commit/64478f1022ce8b50c3a832cdc3888462e3697b9d)
#### Tuesday 2022-03-01 03:48:11 by Hamraj

[WIP] More Buildings

- yeah still a long ass way to go but im faster at the shit now

---
## [ozzono/scripts](https://github.com/ozzono/scripts)@[b5f105da89...](https://github.com/ozzono/scripts/commit/b5f105da89b032cf3867edfeea5454326861297f)
#### Tuesday 2022-03-01 04:19:50 by Hugo Virgilio

Fortune Commit: (1) Avoid fried meats which angry up the blood.
(2) If your stomach antagonizes you, pacify it with cool thoughts.
(3) Keep the juices flowing by jangling around gently as you move.
(4) Go very lightly on the vices, such as carrying on in society, as
	the social ramble ain't restful.
(5) Avoid running at all times.
(6) Don't look back, something might be gaining on you.
		-- S. Paige, c. 1951

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[5d2929e314...](https://github.com/repinger/exynos9611_m21_kernel/commit/5d2929e314e08b2b7abfb4f68523ed4b0acd97f2)
#### Tuesday 2022-03-01 04:35:47 by Dave Chiluk

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

---
## [dragomagol/event-winter-ball-2021](https://github.com/dragomagol/event-winter-ball-2021)@[7bead07444...](https://github.com/dragomagol/event-winter-ball-2021/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Tuesday 2022-03-01 06:25:13 by John Willard

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
## [Georgehkj125/PassGen](https://github.com/Georgehkj125/PassGen)@[74cda2b9c1...](https://github.com/Georgehkj125/PassGen/commit/74cda2b9c1f7fa0ac48bd557eb46f8f5355eeb6b)
#### Tuesday 2022-03-01 08:21:43 by George Helvin K J

Python Passgen.py

import random
import sys
from math import log

if sys.version_info < (3, 0):
    input = raw_input

# Just some colors and shit
white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'

print ('''%s        __   __           
 ▒█▀▀█ █▀▀█ █▀▀ █▀▀ ▒█▀▀█ █▀▀ █▀▀▄ _red_master_(OB_Security)_
 ▒█▄▄█ █▄▄█ ▀▀█ ▀▀█ ▒█░▄▄ █▀▀ █░░█ 
 ▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ▒█▄▄█ ▀▀▀ ▀░░▀ %s\n''' % (red, end))

print ('''%s
▒█▀▄▀█ █░░█ ░░▀ █▀▀ █▀▀ █▀▀▄ 
▒█▒█▒█ █░░█ ░░█ █▀▀ █▀▀ █▀▀▄ 
 █░░▒█ ░▀▀▀ █▄█ ▀▀▀ ▀▀▀ ▀▀▀░ %s \n''' % (green, end))
       
name = input('%s Name of a RANDOM person: ' % que).lower()
choice = input('%s Obsfucate the name? [Y/n] ' % que).lower()
if choice == 'n':
	obsfucate = False
else:
	obsfucate = True

first = ['had', 'throws', 'buys', 'bites', 'blows', 'hates', 'likes', 'bangs', 'tarzan', 'has', 'boils', 'wants', 'roasts', 'fly', 'eats', 'licks', 'sucks', 'rides', 'kills', 'screws', 'destroys', 'cuts']

second = ['your', 'our', 'racist', 'hairy', 'many', 'green', 'giant', 'all', 'three', 'five', 'hundred', 'ugly', 'my', 'black', 'nice', 'small', 'horny', 'little', 'ten', 'loverboy', 'wwe', 'password', 'super']

third = ['hammers', 'apples', 'monkeys', 'babies', 'kids', 'hands', 'horses', 'trees','stones', 'cats', 'asses', 'computers', 'mangoes', 'dildos', 'poles', 'dogs', 'pussies', 'aliens', 'hackers', 'brother',]

seperators = ['-', '.', '*', '+', '~', '_', '/', '\\', '@']

generated_passwords = []

def generate(name):
	wordlist = []
	wordlist.append(random.choice(first))
	wordlist.append(random.choice(second))
	wordlist.append(random.choice(third))
	seperator = random.choice(seperators)
	name = name.title()
	if obsfucate:
		name = name.replace('a', '4').replace('h', '3').replace('e', '3').replace('i', '!').replace('l', '1').replace('t', '7').replace('s', '$').replace('o', '0')
	password = name + seperator + seperator.join(wordlist)
	generated_passwords.append(password)
	print (' %s|%s %-35s%s|%s %-20s%s|%s' % (green, end, password, green, end, (log(82)/log(2)) * len(password), green, end))

def initiate():
	print ('')
	print (' %s+------------------------------------+---------------------+%s' % (green, end))
	print (' %s| Passwords                          | Entropy             |%s' % (green, end))
	print (' %s+------------------------------------+---------------------+%s' % (green, end))
	for y in range(0, 10):
		generate(name)
	print (' %s+--------------------------+-------------------------------+%s' % (green, end))
	choice = input('\n%s Generate more passwords? [y/N] ' % que).lower()
	if choice == 'y':
		initiate()
	else:
		quit()

initiate()

---
## [cyberknight777/dragonheart_kernel_oneplus_sm8150](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150)@[f47aff2472...](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150/commit/f47aff247285a70a2cd868ca16e9d8261e6d4db6)
#### Tuesday 2022-03-01 10:43:04 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [NBtheMC/The-Adventurers-Guild](https://github.com/NBtheMC/The-Adventurers-Guild)@[5c73ebe393...](https://github.com/NBtheMC/The-Adventurers-Guild/commit/5c73ebe3931add9eb1cb88f560425dba12112f72)
#### Tuesday 2022-03-01 11:03:47 by Eric Long

OMG so many fucking storylets

they're fucking done. And they're mostly setup. Yeah. sure.

---
## [PamposhMam/silver-pancakce-real](https://github.com/PamposhMam/silver-pancakce-real)@[c412c48d4b...](https://github.com/PamposhMam/silver-pancakce-real/commit/c412c48d4b7e86f85f7bc37b039df57f43dbd303)
#### Tuesday 2022-03-01 11:08:51 by PamposhMam

Update flood.py

Done. Holy nuts, Chloe, it's done! It works on my repo and everything! OMG! I'm so happy! I've been trying to fix my issues since frigging SUNDAY! Thank you for always being such an amazing lab partner! It works now! YAY! It took 6 weeks to get here, but it all works! No more need for collab or anything! 😭

---
## [minisan/dbot](https://github.com/minisan/dbot)@[3d94be426b...](https://github.com/minisan/dbot/commit/3d94be426b4d9b23c1a26d3e5c47b47314c8902b)
#### Tuesday 2022-03-01 11:57:54 by 몽스탕

Revert "Fuck you Too"

This reverts commit a710c02e53bb8f1ef6514afa2ea7afe83b59ba39.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Tuesday 2022-03-01 13:13:13 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [etothex23/PythonGui](https://github.com/etothex23/PythonGui)@[ecde59518f...](https://github.com/etothex23/PythonGui/commit/ecde59518f10d47b251a8573de7435767f5b87ea)
#### Tuesday 2022-03-01 14:46:59 by etothex

fuck you git you suck. pycharm sucks too. You fucking losers make it more difficult just to set and get files it is not worth using

---
## [JaLang-Organization/Compiler](https://github.com/JaLang-Organization/Compiler)@[aaaceabe62...](https://github.com/JaLang-Organization/Compiler/commit/aaaceabe627a58c171e8a05cc6e447b5f0605ba0)
#### Tuesday 2022-03-01 15:13:30 by Jadefalke

semantic analyzer shit idk what im doing fuck ahhhh what do I do help someone help me with this shit fuck idk how to do this thing and im very confsued about this shit so I dont know what to do and I dont make any progress and stuff YEAH

---
## [Le-Technologue/minishell](https://github.com/Le-Technologue/minishell)@[88f5e2cabf...](https://github.com/Le-Technologue/minishell/commit/88f5e2cabffba9535a23f62165f4a8227d1e0b9b)
#### Tuesday 2022-03-01 15:47:12 by William Cazorla

(；⌣̀_⌣́) expdvar refactor...
- While I fixed #42 segf on void variables in one sec, I realised that my
  var expansion function behavior was missing some cases while exiting
  or entering double quotes, so I redid it more thoroughly... which took me
  6 hours.
- This resulted the addition of a powerful vctr_insert function in the libft
  to manipulate the prb->word buffer at will.
- It was hard as the return_env_var function is giving us raw data and
  the norm only allows us so much lines to parse it.
- Should I have used some sort of function pointer logic to change the
  wording function accordingly to the lexical context/the type of word
  we are parsing, delegating wording rules to each parser instead of
  trying to implement the grammar globally ? Even if this push was a
  pain, in the end I think I was right to do my parsing this way, the
  only trouble was that we were short in time.

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[95c9edda63...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/95c9edda636c57e6122ae85c7ef78627e2dc5faa)
#### Tuesday 2022-03-01 16:29:51 by AmyBSOD

Oh my god Amy you sick freak

If the hdf crew hadn't banned my game yet, they'd do so when seeing this commit. In a way I should probably be grateful because now I can simply add such shit to the game without a care in the world :-P

---
## [brandisher/api](https://github.com/brandisher/api)@[5b82635ef1...](https://github.com/brandisher/api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Tuesday 2022-03-01 16:37:47 by W. Trevor King

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
## [Cenrus/tgstation](https://github.com/Cenrus/tgstation)@[8f32cbe38d...](https://github.com/Cenrus/tgstation/commit/8f32cbe38d956e06c919be36386da76befb0555b)
#### Tuesday 2022-03-01 16:46:29 by LemonInTheDark

Reworks janitor cyborg cleaning, focus on the slipping (#64131)

Alt of #64105 and #64126 (I'm sorry Novva, I should have said something earlier)
I main janitor. As a janitor main, my greatest joy in life is slipping people who ignore my signs

I've seen some people complain about janitor borgs, so I decided to look into em

Unfortunately, not only is the janitor borg just a straight upgrade to janitors, it has absolutely no reason to use most of its kit
We give it standard cleaning supplies, and hell even bespoke tools to deal with leaving slippery tiles everywhere, but we also just let them clean anything they can walk over

This seems a bit too much to me, even for borgs. Also it's like, really boring

So what if we made their movement based cleaning cost something? How about we make it suck water from their bucket. Use the same pattern as mop code, make it twice as expensive though. Give it a slowdown, some sound cues, and an action button to trigger it all

---
## [wiktorek140/msm-4.9-new](https://github.com/wiktorek140/msm-4.9-new)@[50d53ecddb...](https://github.com/wiktorek140/msm-4.9-new/commit/50d53ecddbc9dd92494d47fd3babc18c5bbcd12e)
#### Tuesday 2022-03-01 17:11:30 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db

---
## [jro1979oliver/kernel_motorola_msm8998](https://github.com/jro1979oliver/kernel_motorola_msm8998)@[06c566a7cf...](https://github.com/jro1979oliver/kernel_motorola_msm8998/commit/06c566a7cf7ac5b7a5d11449d7e52153ea1e3824)
#### Tuesday 2022-03-01 17:23:57 by Maciej Żenczykowski

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
## [tannerhelland/PhotoDemon](https://github.com/tannerhelland/PhotoDemon)@[9ea86606d9...](https://github.com/tannerhelland/PhotoDemon/commit/9ea86606d931e4bc1c69fe6955a3a6aa56184a98)
#### Tuesday 2022-03-01 17:59:53 by Tanner

SVG import now supported!

Hell yeah, this is exciting!  I didn't think SVG import would ever be *truly* feasible, but here we are.

SVG support in PhotoDemon is now available thanks to the open-source resvg library by Yevhenii Reizner:

https://github.com/RazrFalcon/resvg

resvg is written in rust.  I'm using a (lightly) customized version of its available C interface in PhotoDemon.
 My changes were mostly reworking it to export stdcall interfaces, and I had to rewrite some function decs to avoid passing UDTs ByVal.  Maybe later I can upload my build configuration to a separate repo so others can review/use it.

This initial build just "silently" loads SVGs without user input.  I like how other software provides a small UI at load-time, so the user can specify custom rasterization dimensions.  I will look at doing this, but it's a little wonky because PD specifically avoids load-time UIs because they break batch processing.  I'll need to be careful when implementing such a feature.

At any rate, this brings a best-in-class SVG parser to PhotoDemon which is all I've ever wanted.  Many thanks to the resvg project for making this possible.

(Also still TODO: verifying XP support.  I'm not entirely sure my rust build chain covered this, but I'll check soon.)

---
## [zkxs/puzzle-game-design](https://github.com/zkxs/puzzle-game-design)@[722162e081...](https://github.com/zkxs/puzzle-game-design/commit/722162e081d112bbdd25faaca2f86940d33528da)
#### Tuesday 2022-03-01 18:25:27 by Michael Ripley

In theory this will work now

- nuke jquery I hate it so much
- use onload like a caveman
- nuke all my bullshit code

---
## [safwan6363/my-files](https://github.com/safwan6363/my-files)@[388a47dfc8...](https://github.com/safwan6363/my-files/commit/388a47dfc873b28b460a012e2a5b95e74c0f0c28)
#### Tuesday 2022-03-01 18:38:55 by safwan6363

what?

seriously what do i do. nothing is fun anymore i have no idea how
i even reached this far doing this shit that i probbaly don't even
enjoy on the inside my life is a complete mess i casn't talk with
anybody everything is dull and boring

---
## [Sidneys1/OlcPixelRayTracer](https://github.com/Sidneys1/OlcPixelRayTracer)@[a58175e39d...](https://github.com/Sidneys1/OlcPixelRayTracer/commit/a58175e39d3c5e7bfb953435178ec5dfade9dfb0)
#### Tuesday 2022-03-01 20:40:00 by Sidney Borne

Add diffuse lighting.

Let's add a single point light source to our scene. We'll add a member
to our game class to represent this. We'll use a class member instead of
a constant so that we can change the position of the light later. We'll
initialize this value in the constructor to be 500 units behind and 500
units above our origin.

Diffuse lighting is frighteningly simple - we already know that a dot
product between two vectors returns a value that roughly describes the
similarity of the vectors. To implement simple diffuse lighting, we can
multiply our sample color by a dot product between the surface normal
vector and a vector pointing towards our single light source.

Let's add a section to our SampleRay function after we apply reflections
where we'll apply diffuse lighting. The process only requires three
lines of code! First we'll create a normalized ray at the intersection
point, pointing towards the light point (we do this by subtracting the
light point from the intersection point). Secondly, we'll calculate the
dot product between our light ray and the surface normal we already
have.

Running our project now will highlight a problem: the top halves of our
Shapes look correct (towards the light), but the bottoms have a
corrupted look. You'll remember that the dot product of two vectors lies
in the range -1 to 1. As we reach the side of our Shapes pointing away
from the light, our dot product enters the negative range - and
"negative" colors are certainly a concept our data types are unprepared
to handle! To fix this let's clamp the dot product value to the range
0 to 1 - this way all negative values are discarded.

Running our project now looks correct! The tops of our shapes are light,
while the bottoms are almost pitch black. Since darkness isn't terribly
interesting, let's add a global ambient light, which we'll implement as
a new constant. By adding our global light value to the dot product
we'll ensure that our diffuse lighting never completely darkens our
scene.

Running our project now displays simple diffuse lighting without
darkening any parts of our scene entirely.

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[1b9c50e2ae...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/1b9c50e2ae1e5fca135e24e11a8bdf0012f89563)
#### Tuesday 2022-03-01 21:17:23 by AmCath

My love for the whole "Spooky" portrait thing stems, I think, from a love of the old stuff KR used to do. Not to get all "SOVL KINO OLD GOOD NEW BAD," but the stuff like the old Halloween stuff, or the Christmas updates or hell even the ancient April fools thing that KR got rid of a while back was and still is super cool. It represented a different time, the old wild west days I guess. One of my fav things about working on KX is the fact that that attitude and style lives on.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3bd5a2d8df...](https://github.com/tgstation/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Tuesday 2022-03-01 23:10:03 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [rbleattler/IISLogManager](https://github.com/rbleattler/IISLogManager)@[5a47540495...](https://github.com/rbleattler/IISLogManager/commit/5a475404954c3a3a0bde449642bd7ee03b43057a)
#### Tuesday 2022-03-01 23:57:45 by Robert Bleattler

fix nuspec to follow old stupid nuget rules. I hate you nuget. die in a fire

---

