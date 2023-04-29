## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-28](docs/good-messages/2023/2023-04-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,147,040 were push events containing 3,247,602 commit messages that amount to 241,679,250 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [FreetoZ/cmss13](https://github.com/FreetoZ/cmss13)@[b451aba2d4...](https://github.com/FreetoZ/cmss13/commit/b451aba2d4fd87a3b5cceaaba6955b8b783f84b2)
#### Friday 2023-04-28 00:42:35 by Hopekz

Fix a start now error and add the ability of queuing the start of the game (#3090)

This PR does two things.

Fixes this error when trying to start early

![dreamseeker_lIUnkd0lFZ](https://user-images.githubusercontent.com/24533979/232609965-5cf94825-0671-420b-8625-16f505f26d63.png)


And adds queuing meaning that if an admin wants to start a game early
during loading; it will now tell them that the game will launch as soon
as it is available then waits for the game to be ready before starting.

Before this PR it just tells you that the game isn't ready then you have
to wait for it to load and launch the "start now" command again.

Does not bypass the "are you sure?" check because it has been moved to
the front.

Honestly made this PR because I hate waiting for the start I just want
to do it once when I see the game window then step away for like a
minute instead of having to wait for it.


:cl: Hopek
add: Adds the support for queuing the round start meaning that if an
admin pressed "start now" it will actually wait until the game is loaded
then immediately start the game as expected versus telling you to try
later.
fix: fixed the "start now" verb displaying that the game has already
started when it is loading because it didn't understand how to read the
game state properly.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [FeenieRU/Fluffy-STG](https://github.com/FeenieRU/Fluffy-STG)@[7c6e64caef...](https://github.com/FeenieRU/Fluffy-STG/commit/7c6e64caefea860c27c7f11f16d067f99a25320b)
#### Friday 2023-04-28 00:56:46 by SkyratBot

Stops station blueprints from expanding areas of non atmos adjacent turfs. [MDB IGNORE] (#20480)

* Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

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

* Stops station blueprints from expanding areas of non atmos adjacent turfs.

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [TeDGamer/cmss13](https://github.com/TeDGamer/cmss13)@[d728da3e02...](https://github.com/TeDGamer/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Friday 2023-04-28 01:07:11 by Puckaboo2

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
## [Pyrotechnics2/cmss13-PyroMap](https://github.com/Pyrotechnics2/cmss13-PyroMap)@[4cf0651670...](https://github.com/Pyrotechnics2/cmss13-PyroMap/commit/4cf06516705b3e0f4a6f446cd36eaa15b554a561)
#### Friday 2023-04-28 01:32:23 by BlackCrystalic

Fixes queen stat bug (#3168)

# About the pull request

Good morning VIETNAM!
That again happened! We found some mistake!

# Explain why it's good for the game

That not good for game, because I fixend so usual staff, like timer for
queen, he can abuse that to make engage on last second and marines -
bruh, young queen, FIGHT! and BANG! Screech on ALL marines... Stupid
folks.

(devs trying to find and fix bugs)
https://www.youtube.com/watch?v=ryNSpF9I3rE

# Changelog

:cl:
fix: Stat proc replaced with get_status_tab_items, fixed issue with
QUEEN additional status
/:cl:

Co-authored-by: BlackCrystalic <blackcrystalic@inbox.ru>

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[43473a4dac...](https://github.com/Wallemations/heavenstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Friday 2023-04-28 01:32:42 by san7890

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
## [ubccsss/ubccsss.org](https://github.com/ubccsss/ubccsss.org)@[17535fd8bd...](https://github.com/ubccsss/ubccsss.org/commit/17535fd8bd547ba27171b824bb6722646b30d237)
#### Friday 2023-04-28 03:14:20 by csssbot

New review for CPSC 210 by ubcstudent2 (#443)

> The concepts in this course are useful. The course overall is good,
but I have a big issue with PraireLearn just makes everything so much
harder for no reason. In this class we use a system called PrairieLearn
for exams and practice exams. To put it frankly, this system is
horrible. First of all, why are we writing code in a web browser? This
course should learn from its pre-req CPSC 110 and move onto programming
in an IDE for exams and all practices. Also it should really have
autograders. Trying to match our answers with the solution when the
solution can be often coded in maybe ways is horrible.

For practice problems, you can only answer the question once, if you
want to try again, you have to creat another instance of the whole
practice set. The text editor is bulky and annoying. Exams seriously
tests more on predicting what the question writer wants. It is also very
hard to perfect grades, because of multiple choice. You can easily get 0
on a question if you just miss a few details.

PraireLearn randomizes the order of answer choices for some reason.
Consider this arbitrary case , if the question involves 3 variables,
usually the question would list the answer choices (1 1), (1 2), (2, 1),
(2, 2), (3, 1), (3, 2) or in some other order. With the order randomized
it could be (2, 2), (1 2), (1 1), (3, 1) , (2, 1), (3, 2). Which messes
up the flow of natural problem solving especially when the answer
choices are full sentences and you need to pick out which parts are
different.

PraireLearn randomizes variable names. Again, this makes every
unnecessarily harder for no reason. They love using arbitrary names with
no meaning at all like "smurf", "lorem", "ipsum." Again, you have to
look back and forth to the question. Even if they just used random
everyday words, it would make it easier.

The questions are just not that clear. If you have a slightly different
interpretation you can expect a maximum of 50% on that question.

Overall the course material is very very easy, but the PraireLearn
system just suck. 0/10. It adds so much extra resistance to the
otherwise very easy course material. CPSC 210 can easily be a 3 credit
course. Also its hard to wrap my head around how a "second year"
computer science course at "a good" university has so much overlap with
Programming 10, 11, 12 in highschools.

>
> Difficulty: 2/5
> Quality: 2/5
> <cite><a href=''>ubcstudent2</a>, Apr 27 2023, course taken during
2022W1</cite>
<details><summary>View YAML for new review</summary>
<pre>
  - author: ubcstudent2
    authorLink: 
    date: 2023-04-27
    review: |
The concepts in this course are useful. The course overall is good, but
I have a big issue with PraireLearn just makes everything so much harder
for no reason. In this class we use a system called PrairieLearn for
exams and practice exams. To put it frankly, this system is horrible.
First of all, why are we writing code in a web browser? This course
should learn from its pre-req CPSC 110 and move onto programming in an
IDE for exams and all practices. Also it should really have autograders.
Trying to match our answers with the solution when the solution can be
often coded in maybe ways is horrible.
      
For practice problems, you can only answer the question once, if you
want to try again, you have to creat another instance of the whole
practice set. The text editor is bulky and annoying. Exams seriously
tests more on predicting what the question writer wants. It is also very
hard to perfect grades, because of multiple choice. You can easily get 0
on a question if you just miss a few details.
      
PraireLearn randomizes the order of answer choices for some reason.
Consider this arbitrary case , if the question involves 3 variables,
usually the question would list the answer choices (1 1), (1 2), (2, 1),
(2, 2), (3, 1), (3, 2) or in some other order. With the order randomized
it could be (2, 2), (1 2), (1 1), (3, 1) , (2, 1), (3, 2). Which messes
up the flow of natural problem solving especially when the answer
choices are full sentences and you need to pick out which parts are
different.
      
PraireLearn randomizes variable names. Again, this makes every
unnecessarily harder for no reason. They love using arbitrary names with
no meaning at all like "smurf", "lorem", "ipsum." Again, you have to
look back and forth to the question. Even if they just used random
everyday words, it would make it easier.
      
The questions are just not that clear. If you have a slightly different
interpretation you can expect a maximum of 50% on that question.
      
Overall the course material is very very easy, but the PraireLearn
system just suck. 0/10. It adds so much extra resistance to the
otherwise very easy course material. CPSC 210 can easily be a 3 credit
course. Also its hard to wrap my head around how a "second year"
computer science course at "a good" university has so much overlap with
Programming 10, 11, 12 in highschools.
      
    difficulty: 2
    quality: 2
    sessionTaken: 2022W1

<pre>
</details>This is an auto-generated PR made using:
https://github.com/ubccsss/course-review-worker

---
## [tonyvitonis/git](https://github.com/tonyvitonis/git)@[07f91e5e79...](https://github.com/tonyvitonis/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Friday 2023-04-28 03:26:19 by Jeff King

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
## [instret/linuxlabs](https://github.com/instret/linuxlabs)@[561d896a14...](https://github.com/instret/linuxlabs/commit/561d896a14684eb648a138fd18f9084c51b2dd14)
#### Friday 2023-04-28 03:34:08 by Michal Vlasák

tools: labs: qemu: Add run-qemu.sh as alternative

TL;DR: In one window run `make -j$(ncproc) console` and `cd` to some
lab's subdirectory (`skels/...`). In second window `cd` to matching
`skels/...` subdirectory, edit source files and compile with something
like `kmake` (`alias kmake='make -C "$HOME/src/linux/" M="$(pwd)"'`) as
needed. The `skels` directory is shared between the host and the guest,
thus in the first window, so you can just `insmod` and `rmmod` the
compiled modules. You can kill the VM by `CTRL-a x` (if you made some
writes from the VM it might be a good idea to run `sync` first). Samba
and QEMU are required.

Full description:

To be honest I don't like the current QEMU setup. I am sure there are
things it does that I don't understand yet, because I have not yet
finished all the labs, but in any case I think that the setup can be
improved.

Some things in particular I don't like about the current setup:

 - "Huge" opaque `.ext4` images are used, even though the contents of
   the  root file system are not that large.
 - While running QEMU newly built modules can't be copied to the image.
 - Mounting and unmounting the `.ext4` image for copying the modules
   requires `sudo`.
 - The networking setup seems too complex, requires `sudo` and was
   broken (at least for me - IIRC I didn't get IP through DHCP), thus I
   also didn't get `ssh` to work. I also seem to be not the only one
   having issues with this:
   https://github.com/linux-kernel-labs/linux/pull/240#issuecomment-956219190
 - `dnsmasq` and `nttctp` mostly don't start correctly (they are not
   killed correctly by the previous run) - this isn't a problem on my
   end, as demonstrated by the output at
   https://linux-kernel-labs.github.io/refs/heads/master/info/vm.html,
   which shows the same issues.
 - Running `minicom` is required to access the serial port, thus at
   least two terminals are required for working with the VM (not a huge
   problem for me personally, since I use `tmux`, but I know some people
   complain about this). The setup also seems unnecessarily complex.
 - I remember a lot of the `.mon` `.pts` files being left uncleaned in
   some cases.
 - I recall warnigns about some of the entries added to `/etc/inittab`
   being ignored.
 - Even though root login requires no password I have to enter the
   `root` username.

In this commit I introdoce an alternative way of running QEMU through a
new `run-qemu.sh` script. The setup is laregely independent and its user
interface consists of `console` and `gui` targets. I tried to make the
script parameterizable through environment variables (inherited from
Make variables), though it may be argued that the default values should
be encoded in Makefile rather than in the script like they are now. I
have no strong opinions about that, it's' just that the current state
allows running the script in standalone fashion.

What the setup brings:

 - A rootfs is extracted from the official Yocto Project tarball and
   kept in a directory that is shared through  [Samba as network
   share](https://www.kernel.org/doc/html/latest/filesystems/cifs/cifsroot.html).
   The `skels` directory is shared as well. Thus the modules can be
   freely tweaked / compiled / ran from either the host or guest.
 - The QEMU stdio serial console setup is used (`ttyS0` on the kernel
   side). This means that running QEMU results in the serial console
   being mapped directly to standard input and output of the terminal -
   `minicom` is not needed. This is the console mode (`make console`).
 -  The setup allows also allows the virtual machine to be run in
    graphical mode (`make gui`).
 - Root is logged in automatically in `console` mode (though similar
   thing could be done for the `gui` mode).
 - Although Samba (`smbd`) is required, `sudo` or root access is not.
 - Networking through QEMU's default [SLIRP backend](https://wiki.qemu.org/Documentation/Networking#User_Networking_.28SLIRP.29).
   DHCP is handled by the kernel, which overcomes some problems I had
   with the System V init system in the Yocto images.
 - The compilation can largely be done with something like this `kmake`
   alias: `alias kmake='make -C "$HOME/src/linux/" M="$(pwd)"'`
   (customize as needed). Though this is not enough for some labs (I no
   longer remember the details, but I think it was some of the earlier
   labs which had dependencies between modules, I think I used the
   classic `make build` for that.

Known issues:

 - SSH support is currently missing. This both requires more featureful
   Yocto images and is IMO unnecessary, since it wouldn't bring much
   benefit over the console mode. Though it can be easily achieved by
   using QEMU option like `-nic user,hostfwd=tcp::2222-:22`, which would
   allow SSH'ing into the guest by something like `ssh -p 2222
   root@localhost`.
 - I used a slightly less advanced setup while doing the labs, so the
   lab workflow with this particular setup is largely untested. There
   may be problems with file permissions due to the samba share.
 - The guest seems to fail to shutdown correctly in a timely manner. I
   just took the habbit of killing qemu with `CTRL-a` followed by `x`,
   potentially running `sync` first to ensure my work is saved (though
   rarely did I actually modify anything on the guest side).

[The former setup](https://github.com/vlasakm/linux/commit/720bd6444a036c2ae6a3e76b7f6aac72f562053a)
I used contains some details of the SSH setup if anyone is interested in
that. It was the basis for this PR, so some ideas can be seen there
(Samba share for `skels`), but I didn't take particular care with [the
kernel config](https://github.com/vlasakm/linux/commit/0290919905e7f4fe3562a46d3274f8d41ad02c55)
and the automounting didn't really work (the `init` would try to mount
the filesystem before networking was up).

What I evaluated and didn't use in the end:

 - At first I tried to extend my former setup by just automounting the
   Samba share. I didn't manage to do this - the (non)workings of init
   scripts seem to be beyond me. If anyone is interested here are a few
   pointers:
   [[1]](https://unix.stackexchange.com/questions/169697/how-does-netdev-mount-option-in-etc-fstab-work),
   `/etc/inittab`, `/etc/init.d/mountall.sh`, `/etc/init.d/mountnfs.sh`.
 - I tried using `9p` [[2]](https://wiki.qemu.org/Documentation/9p),
   [[3]](https://wiki.qemu.org/Documentation/9psetup)
   [[4]](https://wiki.qemu.org/Documentation/9p_root_fs) which is built
   into QEMU and can be compiled into the kernel. With `mapped-xattr`
   security model it would be too cumbersome to create the rootfs, and
   `passthrough` would require root privileges. It is also very slow.
   There are also some problems with trying to use it as rootfs, maybe
   specific to `linux-kernel-labs` kernel version or config. Ask me if
   interested.
   [[5]](https://lists.gnu.org/archive/html/qemu-devel/2016-09/msg07184.html)
   [[6]](https://lore.kernel.org/linux-fsdevel/20210608153524.GB504497@redhat.com/)
   [[7]](https://lore.kernel.org/all/YL1eM+mzjuggDvqp@codewreck.org/T/)
 - QEMU has an option to setup the Samba share on its own, though I
   found a custom config (based on the QEMU one) to be easier - allows
   customization like multiple shares, unix extensions, different port,
   etc.

Signed-off-by: Michal Vlasák <lahcim8@gmail.com>
Signed-off-by: Daniel Baluta <daniel.baluta@nxp.com>

---
## [EssieSteam13/css-exercises](https://github.com/EssieSteam13/css-exercises)@[046c3f0184...](https://github.com/EssieSteam13/css-exercises/commit/046c3f0184b8e4773ec1cecdca76b9e561fc9a4c)
#### Friday 2023-04-28 03:35:23 by Essence Ferguson

Complete 2nd Foundation Lesson

I learned how to apply ID and Class selectors. I also missed that comma
was supposed to be a semi-colon for over 30 minutes. Which in my opinion
was ridiculous. That was my first typo problem in coding so far. I
laughed, but it will not be funny AT ALL in future tense XD! I als got
to work with font families.

---
## [Xoxeyos/Yogstation](https://github.com/Xoxeyos/Yogstation)@[818973e1e9...](https://github.com/Xoxeyos/Yogstation/commit/818973e1e91edd0d62357f0ca4361916fb1d3f69)
#### Friday 2023-04-28 04:24:38 by wejengin2

fixes some issues in infiltrator base (#17861)

* huh

* man

* adds griddle

* that's really funny but fuck you

---------

Co-authored-by: Byemoh <baiomurang@gmail.com>

---
## [Lucas32578/Humanities-Semester-Project](https://github.com/Lucas32578/Humanities-Semester-Project)@[d934533077...](https://github.com/Lucas32578/Humanities-Semester-Project/commit/d9345330778ca8cae19d93ad9eab710802879f2d)
#### Friday 2023-04-28 04:31:42 by Your Name

javascript being stupid and useless "security" bullshit making it so i can only run certain code on the live version because iframes suck

---
## [alienatiz/pe_kernel_xiaomi_lavender](https://github.com/alienatiz/pe_kernel_xiaomi_lavender)@[913870e6a0...](https://github.com/alienatiz/pe_kernel_xiaomi_lavender/commit/913870e6a08b069c8ff8d1c4f9146bcdaa69b4ec)
#### Friday 2023-04-28 05:18:54 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cb1388ed9e...](https://github.com/odoo-dev/odoo/commit/cb1388ed9e64ced4e0d85cf5778192dfbdfd5995)
#### Friday 2023-04-28 06:10:52 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

closes odoo/odoo#119246

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4
Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2d008739c5...](https://github.com/treckstar/yolo-octo-hipster/commit/2d008739c50e0d28f62c8715d35de13f4c2a61a0)
#### Friday 2023-04-28 06:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Unleash/unleash](https://github.com/Unleash/unleash)@[2765ae2c70...](https://github.com/Unleash/unleash/commit/2765ae2c707eab4717a5e149672bb02035a8f58d)
#### Friday 2023-04-28 06:59:45 by Thomas Heartman

feat: unify error responses (#3607)

This PR implements the first version of a suggested unification (and
documentation) of the errors that we return from the API today.

The goal is for this to be the first step towards the error type defined
in this internal [linear
task](https://linear.app/unleash/issue/1-629/define-the-error-type
'Define the new API error type').

## The state of things today

As things stand, we currently have no (or **very** little) documentation
of the errors that are returned from the API. We mention error codes,
but never what the errors may contain.

Second, there is no specified format for errors, so what they return is
arbitrary, and based on ... Who knows? As a result, we have multiple
different errors returned by the API depending on what operation you're
trying to do. What's more, with OpenAPI validation in the mix, it's
absolutely possible for you to get two completely different error
objects for operations to the same endpoint.

Third, the errors we do return are usually pretty vague and don't really
provide any real help to the user. "You don't have the right
permissions". Great. Well what permissions do I need? And how would I
know? "BadDataError". Sick. Why is it bad?

... You get it.

## What we want to achieve

The ultimate goal is for error messages to serve both humans and
machines. When the user provides bad data, we should tell them what
parts of the data are bad and what they can do to fix it. When they
don't have the right permissions, we should tell them what permissions
they need.

Additionally, it would be nice if we could provide an ID for each error
instance, so that you (or an admin) can look through the logs and locate
he incident.

## What's included in **this** PR?

This PR does not aim to implement everything above. It's not intended to
magically fix everything. Its goal is to implement the necessary
**breaking** changes, so that they can be included in v5. Changing error
messages is a slightly grayer area than changing APIs directly, but
changing the format is definitely something I'd consider breaking.

So this PR:

- defines a minimal version of the error type defined in the [API error
definition linear
task](https://linear.app/unleash/issue/1-629/define-the-error-type).
- aims to catch all errors we return today and wrap them in the error
type
-   updates tests to match the new expectations.

An important point: because we are cutting v5 very soon and because work
for this wasn't started until last week, the code here isn't necessarily
very polished. But it doesn't need to be. The internals can be as messy
as we want, as long as the API surface is stable.

That said, I'm very open to feedback about design and code completeness,
etc, but this has intentionally been done quickly.

Please also see my inline comments on the changes for more specific
details.

### Proposed follow-ups

As mentioned, this is the first step to implementing the error type. The
public API error type only exposes `id`, `name`, and `message`. This is
barely any more than most of the previous messages, but they are now all
using the same format. Any additional properties, such as `suggestion`,
`help`, `documentationLink` etc can be added as features without
breaking the current format. This is an intentional limitation of this
PR.

Regarding additional properties: there are some error responses that
must contain extra properties. Some of these are documented in the types
of the new error constructor, but not all. This includes `path` and
`type` properties on 401 errors, `details` on validation errors, and
more.

Also, because it was put together quickly, I don't yet know exactly how
we (as developers) would **prefer** to use these new error messages
within the code, so the internal API (the new type, name, etc), is just
a suggestion. This can evolve naturally over time if (based on feedback
and experience) without changing the public API.

## Returning multiple errors

Most of the time when we return errors today, we only return a single
error (even if many things are wrong). AJV, the OpenAPI integration we
use does have a setting that allows it to return all errors in a request
instead of a single one. I suggest we turn that on, but that we do it in
a separate PR (because it updates a number of other snapshots).

When returning errors that point to `details`, the objects in the
`details` now contain a new `description` property. This "deprecates"
the `message` property. Due to our general deprecation policy, this
should be kept around for another full major and can be removed in v6.

```json
{
  "name": "BadDataError",
  "message": "Something went wrong. Check the `details` property for more information."
  "details": [{
    "message": "The .params property must be an object. You provided an array.",
    "description": "The .params property must be an object. You provided an array.",
  }]
}
```

---
## [LucasP0326/CERAEBRU](https://github.com/LucasP0326/CERAEBRU)@[0026bb9568...](https://github.com/LucasP0326/CERAEBRU/commit/0026bb9568d24ac6fba6a721fa8c5c244a19f414)
#### Friday 2023-04-28 07:02:00 by LucasP0326

I did a lot of cool shit commit

Guess the cool ass shit we have:
--DIALOGUE EVERYWHERE
--RETICLE THAT FUCKING MOVES
--WE GOT A FUCKING NEWS FEED VIDEO
--CUSTOM FUCKING MUSIC FOR SAID NEWS
--SPECIAL "ROGUE" ENDING ADDED
--AND MORE (I forgor)

---
## [benjaminjkern/cuttlefishlang](https://github.com/benjaminjkern/cuttlefishlang)@[96d5c53d0e...](https://github.com/benjaminjkern/cuttlefishlang/commit/96d5c53d0e00ac83b9b2889dd4693ad904d5e684)
#### Friday 2023-04-28 07:29:34 by benjaminjkern

This shit is HARD! WIP: Need to:
- finish making heuristics fully lazy and dependent on input types
- Make all of this work with parsing
- SOmehow for generic heuristics it needs to iterate over every possible generic (Easy if it finds a good case but I think in theory it could keep iterating forever which is annoying) (Might just be able to get away with some basic stuff though)

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[21464fe41c...](https://github.com/PKRoma/Terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Friday 2023-04-28 08:01:51 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [amtoine/nushell](https://github.com/amtoine/nushell)@[2e01bf9cba...](https://github.com/amtoine/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Friday 2023-04-28 08:02:00 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [mattdway/CreateWithVR](https://github.com/mattdway/CreateWithVR)@[ab51f1112d...](https://github.com/mattdway/CreateWithVR/commit/ab51f1112d71ca5e120d47d5e7a4213d4dc073cf)
#### Friday 2023-04-28 08:28:10 by mattdway

04-27-23 v4.0.0 Commit

04-27-23 v4.0.0 Commit
From Feb 18 to April 27

- Many ascetic material and texture changes to the room
- I added spot lights to the book rack for effect.
- I changed out the coffee table and the four doors of the cabinets with a blue glass material.
- I added multiple blue point lights to the new glass material coffee table and to the inside of the cabinets to give this a cool modern look.
- I changed the wall material to gray.
- I changed the door material to a mustard yellow.
- I changed the chair color, the trunk color and the cabinet door and drawer door color to blue.
- I changed all the cabinet handles to black (the cabinet with the two doors I ended up adding a metalic backing using a 3D cube game object overlay and I did the same thing with the handles only using a black metalic material for the handles.
- I changed the top of the cabinets material to a metalic black.
- Added the modern book rack (free asset) to the room and I populated these with books and sockets for each book.
- I changed out the rug from the purple and gray (80's style) to the cool gray with the diamond.  I did this by changing not the material but the mesh filter.
- I changed the clock from black to red.  I did this by downloading the working black clock (the black clock asset had serious problems in the 2020 version) from the 2021 starter files on the Learn.Unity.Com Create with VR section and then by changing not the material but the mesh filter.
- I changed the couch texture from white to black and I added in a leather material (I downloaded from free leather chair assets for their texture files and I used those to create my own material for the couch).
- I changed all the room lighting to white to give this a cool, more modern, look.  The yellow lighting was also giving the black and grays in the room (couch, walls) more of a brownish tint at times.  There's still a little bit of yellow light from the sunset (Enviorment Skybox) from outside but all inside lighting is now white). I also rebaked my lightmap (I left the book case light, the coffee table and cabinet lights dynamic because they needed to be to really read as lights -- plus the light bounces dynamically off the glass texture, which is the effect I was going for).
= I created my own fire particle effect from a YouTube tutorial.  This also means that the free fire asset I was using before (that didn't look great and that had multiple layer stop errors) is no longer a part of this project (removed from the Project folder).
- Added the "It's Fine" meme.
- Got the asset from Thingiverse, converted the STL to OBJ and I brought this in and assembled.
- I then used 3D object overlays so that I could add material colors (my Blender skills aren't there yet!) and these were single game objects so adding multiple materials weren't possible due to there being only a single mesh filter for the entire object).
= I then positioned this outside the window
- I added cool creeping fire particle effect from the free Unity particle effect asset and I created and added my own smoke particle effect (from a YouTube tutorial).
= I then wrote a script that activated this game object whenever the rug fire was instantiated and I used a coroutine to keep this visible for 10 seconds (the same amount of time before the rug fire game object is destroyed), before disabling the It's Fine meme again.  This has the effect of having the meme visible until the last flame is extinguished (as the ten second timers is started every time the rug fire is lit).  It also has the effect of adding more and more smoke every time the rug fire is lit (making the meme disapear in smoke if lighting additional rug fires.
- Added the "Legend of Zelda" meme.
- I got the wood sword and the cave wizard assets from Thingiverse
- I assembled and converted the STL to OBJ and I brought this in and assembled.
I then used 3D object overlays so that I could add material colors (my Blender skills aren't there yet!)
- I created my own handle out of Unity 3D cylinders so that I could add the alternating colors via materials, appropiately.
- I scaled everything appropiately to have this be the correct size when held.
- I created cave walls with a texture material and a back wall, floor and ceiling with a black texture.
- I replicated the cave wizard's message from the Legend of Zelda game using TMP canvas, image and TMP components.
- I added Unity lighting to the fire 3D objects on either side of him.
- I added an Audio Source to the wooden sword using a downloaded FX used in the original game whenever Link picked up an item.
- I added collider, rigid body and XR Grab Interactable components to the sword.
- I linked the audio source to the OnSelect event of the XR Grab Interactable component.
- I then wrote a script, attached to the cave, that activates the cave around the player for 3 seconds and then deactivates it again after.
- I linked this to the OnSelect event for the XR Grab Interactable for the sword, as well.
- I modified and prefabbed the Unity fireball particle effect from the free Unity particle effect asset (changed the size of the partile to only be one fireball, changed the start size for all parent and child elements in the fireball particle effect, I changed the added a collier and rigidbody to this, I changed the size angle from 360 to 9 so that these fireballs would spawn from the tip of the sword and not randomly all around the player)
- I created a new script, and I copied and pasted (reused) the Fire() method from the dart gun to make it so that the sword shoots fire balls (like in the game when Link has full health). This also included creating an empty game object with the transform set appropiately and placed at the sword.
- Improved the rug fire by adding my own fire particle and smoke particle effect
- I made the darts stick to the wall surfaces (anything with a tag of wall).  These darts also unstick after a period of time and sometimes don't stick at all (they are 'suctioncups,' after all :))
- I fixed the tennis racket attach point so that this is held in a natural and authentic position (thanks to my student who helped with this).
- I added art lights to each of the three paintings (made out of scaled cubes with a black metalic material and spot lights).

- I added and worked more on the dart game:
- I added an activation area that starts this with TMP for score, points granted, and a timer along with playing an free retro arcade starting up FX sound effect.
- There are collision and point calculation issues.  I have an idea for a rebuild of my own target (rather than the paper target) -- I just haven't sat down to work on this yet.  Part of the issue is the dart calculating twice when stuck to a collider and another issue is when a dart lands between two colliders.  Creating a dart board with offset layers should fix the second piece.  I added a bool variable check to try and mitigate the first.
- Current version has torus shaped colliders for each ring and individual collision detection and point awarded.
- There is also a GameManager.cs script that manages the overall mini-game.
- There is a count down timer that writes the time remanining to a TMP, using a free retro arcade font.
- Points awarded are written for about 2 seconds to a TMP, using a free retro arcade font and a retro arcade points FX sound effect.
- Overall score is calucated and displayed in another TMP, using a free retro arcade font
- The timer doesn't yet do anything when time runs out.
- An unknown bug has caused the timer to stop working (isn't starting the count down currently).
- I need to add win and lose screens.

Other things I fixed:
- The front door hinges were no longer allowing the door to open.  Replacing it with the Unity prefab and then readding all my components and materials fixed this.
- The front door handle was no longer grabbable (most likely do to a change I made in the asset parent/child relationship to try and fix a different issue).  Restoring the door from the Unity prefab also put this back the way it was before.
- The Front Door toggle button was no longer working -- fixing the door and relinking assets to my button's script fixed this issue.
- I fixed the rug teleportation, the new game activation teleportation area and front door mat teleportation staying on bug - just needed to add events to my Settings menu for continuous motion to turn the teleportation anchor off for those two teleportation areas.
- Moved the teleporation mats back along the east wall (with the addition of the modern book rack these needed to also be moved back so that the player isn't teleporting uncomfortably close to that book rack).
- I fixed the rug fire not working bug
- I fixed the XR Rig not working in the Peaceful Nowhere scene
- I updated XRIT again and this broke all the References in the XR Origin and children again, so I remapped these appropiately.

- I updated the version number and build date on the Welcome board.

To do next:
I need to decide if I want the gym aesthetics to be the same or different from the main room, I need to add in the correct XR Origin to that scene, I need to create buttons in the main room and in the gym that changes to those scenes as well as adding writing the scripts and adding the climbing mechanics to this scene.

I fixed the lack of .git folder (this project was no longer a git repository) so that I could commit to this GitHub on this date.

That's all for now.
@mattdway mattdway committed on April 27

---
## [tomaarsen/argilla](https://github.com/tomaarsen/argilla)@[4c5f51377e...](https://github.com/tomaarsen/argilla/commit/4c5f51377e374fb30649bdc7b9a3291db21c5bb8)
#### Friday 2023-04-28 08:30:56 by Tom Aarsen

Use `rich` for logging, tracebacks, printing, progressbars (#2350)

Closes #1843

Hello!

## Pull Request overview
* Use [`rich`](https://github.com/Textualize/rich) for logging,
tracebacks, printing and progressbars.
* Add `rich` as a dependency.
* Remove `loguru` as a dependency and remove all mentions of it in the
codebase.
* Simplify logging configuration according to the logging documentation.
* Update logging tests.

## Before & After
[`rich`](https://github.com/Textualize/rich) is a large Python library
for very colorful formatting in the terminal. Most importantly (in my
opinion), it improves the readability of logs and tracebacks. Let's go
over some before-and-afters:
<details><summary>Printing, Logging & Progressbars</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219089678-e57906d3-568d-480e-88a4-9240397f5229.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219089826-646d57a6-7e5b-426f-9ab1-d6d6317ec885.png)

Note that for the logs, the repeated information on the left side is
removed. Beyond that, the file location from which the log originates is
moved to the right side. Beyond that, the progressbar has been updated,
ahd the URL in the printed output has been highlighted automatically.

</details>

<details><summary>Tracebacks</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219090868-42cfe128-fd98-47ec-9d38-6f6f52a21373.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219090903-86f1fe11-d509-440d-8a6a-2833c344707b.png)

---

### Before:

![image](https://user-images.githubusercontent.com/37621491/219091343-96bae874-a673-4281-80c5-caebb67e348e.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219091193-d4cb1f64-11a7-4783-a9b2-0aec1abb8eb7.png)

---

### Before

![image](https://user-images.githubusercontent.com/37621491/219091791-aa8969a1-e0c1-4708-a23d-38d22c2406f2.png)

### After

![image](https://user-images.githubusercontent.com/37621491/219091878-e24c1f6b-83fa-4fed-9705-ede522faee82.png)

</details>

## Notes
Note that there are some changes in the logging configuration. Most of
all, it has been simplified according to the note from
[here](https://docs.python.org/3/library/logging.html#logging.Logger.propagate).
In my changes, I only attach our handler to the root logger and let
propagation take care of the rest.

Beyond that, I've set `rich` to 13.0.1 as newer versions experience a
StopIteration error like discussed
[here](https://github.com/Textualize/rich/issues/2800#issuecomment-1428764064).

I've replaced `tqdm` with `rich` Progressbar when logging. However, I've
kept the `tqdm` progressbar for the [Weak
Labeling](https://github.com/argilla-io/argilla/blob/develop/src/argilla/labeling/text_classification/weak_labels.py)
for now.

One difference between the old situation and now is that all of the logs
are displayed during `pytest` under "live log call" (so, including
expected errors), while earlier only warnings were shown.

## What to review?
Please do the following when reviewing:
1. Ensuring that `rich` is correctly set to be installed whenever
someone installs `argilla`. I always set my dependencies explicitly in
setup.py like
[here](https://github.com/nltk/nltk/blob/develop/setup.py#L115) or
[here](https://github.com/huggingface/setfit/blob/78851287535305ef32f789c7a87004628172b5b6/setup.py#L47-L48),
but the one for `argilla` is
[empty](https://github.com/argilla-io/argilla/blob/develop/setup.py),
and `pyproject.toml` is used instead. I'd like for someone to look this
over.
2. Fetch this branch and run some arbitrary code. Load some data, log
some data, crash some programs, and get an idea of the changes.
Especially changes to loggers and tracebacks can be a bit personal, so
I'd like to get people on board with this. Otherwise we can scrap it or
find a compromise. After all, this is also a design PR.
3. Please have a look at my discussion points below.

## Discussion
`rich` is quite configurable, so there's some changes that we can make
still.
1. The `RichHandler` logging handler can be modified to e.g. include
rich tracebacks in their logs as discussed
[here](https://rich.readthedocs.io/en/latest/logging.html#handle-exceptions).
Are we interested in this?
2. The `rich` traceback handler can be set up to include local variables
in its traceback:
<details><summary>Click to see a rich traceback with local
variables</summary>


![image](https://user-images.githubusercontent.com/37621491/219096029-796b57ee-2f1b-485f-af35-c3effd44200b.png)
    </details>
Are we interested in this? I think this is a bit overkill in my opinion.
3. We can suppress frames from certain Python modules to exclude them
from the rich tracebacks. Are we interested in this?
4. The default rich traceback shows a maximum of 100 frames, which is a
*lot*. Are we interested in reducing this to only show the first and
last X?
5. The progress bar doesn't automatically stretch to fill the full
available width, while `tqdm` does. If we want, we can set `expand=True`
and it'll also expand to the entire width. Are we interested in this?
6. The progress "bar" does not need to be a bar, we can also use e.g. a
spinner animation. See some more info
[here](https://rich.readthedocs.io/en/latest/progress.html#columns). Are
we interested in this?

---

**Type of change**

- [x] Refactor (change restructuring the codebase without changing
functionality)

**How Has This Been Tested**

I've updated the tests according to my changes.

**Checklist**

- [x] I have merged the original branch into my forked branch
- [ ] I added relevant documentation
- [x] follows the style guidelines of this project
- [x] I did a self-review of my code
- [x] I added comments to my code
- [ ] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works

- Tom Aarsen

---
## [Iajret/tgstation](https://github.com/Iajret/tgstation)@[a6f49ed542...](https://github.com/Iajret/tgstation/commit/a6f49ed54255f9a8d4dfc27bc397e56f87029cb8)
#### Friday 2023-04-28 09:02:29 by san7890

Refactors Suiciding Variable Into Trait (#74150)

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

---
## [mummypikachu/pokemon-showdown](https://github.com/mummypikachu/pokemon-showdown)@[a31fc84c43...](https://github.com/mummypikachu/pokemon-showdown/commit/a31fc84c43d112cd91596df3fc8f69460581f5ca)
#### Friday 2023-04-28 09:53:37 by VanillaKun45

Vanilla's 4AM Blaze Buffs

These buffs are based on Drayano's ROM hacks but some are original.

- NEW SIGNATURE MOVE: #910 Tyrant's Wrath
50 BP Phys Fire Triple Axel (Typhlosion)

- Typhlosion now has Solar Power and Desolate Land (fuck you) and learns Headlong Rush
- Leavanny now gets Play Rough
- Rotom-Fan gets Lightning Rod
- Tyranitar now gets Rock Wrecker
- Vivillon is Bug/Fairy and now gets Moonblast and Dazzling Gleam, slight stat buff
- Base Lucario gets Adaptability
- Misdreavus stat boosts and is Ghost/Fairy

---
## [D19127919/GE-Final-Asessment](https://github.com/D19127919/GE-Final-Asessment)@[348f58dd14...](https://github.com/D19127919/GE-Final-Asessment/commit/348f58dd1400276c15f4e392f17cf9bafe1c02a2)
#### Friday 2023-04-28 10:01:09 by D19127919

follow up tweaks

I hate my life.
In other news, had to 1:1 copy-paste the example avoidance behaviour since I could not figure out how it worked.
I'll revisit it if I have time, but I figure I'll lose fewer points by having a complete project with that one bit of copy-paste than I would by having an original working avoidance behaviour and nothing else.

---
## [draganjovanovich/Open-Assistant](https://github.com/draganjovanovich/Open-Assistant)@[b9c60ed582...](https://github.com/draganjovanovich/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Friday 2023-04-28 13:04:39 by Tobias Pitters

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
## [chadoh/poemey-writes](https://github.com/chadoh/poemey-writes)@[2b23d37c98...](https://github.com/chadoh/poemey-writes/commit/2b23d37c98670b67079498698ff068b3ed11d7c0)
#### Friday 2023-04-28 13:09:37 by Chad Ostrowski

add Prayer for Productivity poem

I've been enjoying the feeling of productivity lately, but I've been
doubting that I'm actually working on anything worthwhile. Being
productive on the wrong thing is worse than being unproductive. It's
anti-productive, no matter what it feels like.

If you work on someone else's dream, you don't need to worry about that.
You can trust that your boss or CEO knows that the mission is noble, and
enjoy your toil without worry. You can be fulfilled, by the standards of
our workist culture, without wasting time thinking about if your toil
amounts to anything worthwhile.

So this is a poem that's a little bit about that.

---
## [overhangio/tutor](https://github.com/overhangio/tutor)@[fccfe78939...](https://github.com/overhangio/tutor/commit/fccfe78939a4c9c314bfabe893f46628de1b729e)
#### Friday 2023-04-28 13:50:35 by Régis Behmo

feat: persistent bind-mounts

This is an important change, where we get remove the previous `--mount`
option, and instead opt for persistent bind-mounts.

Persistent bind mounts have several advantages:
- They make it easier to remember which folders need to be bind-mounted.
- Code is *much* less clunky, as we no longer need to generate temporary
  docker-compose files.
- They allow us to bind-mount host directories *at build time* using the
  buildx `--build-context` option.
- The transition from development to production becomes much easier, as
  images will automatically be built using the host repo.

The only drawback is that persistent bind-mounts are slightly less
portable: when a config.yml file is moved to a different folder, many
things will break if the repo is not checked out in the same path.

For instance, this is how to start working on a local fork of
edx-platform:

    tutor config save --append MOUNTS=/path/to/edx-platform

And that's all there is to it. No, this fork will be used whenever we
run:

    tutor images build openedx
    tutor local start
    tutor dev start

This change is made possible by huge improvements in the build time
performance. These improvements make it convenient to re-build Docker
images often.

Related issues:
https://github.com/openedx/wg-developer-experience/issues/71
https://github.com/openedx/wg-developer-experience/issues/66
https://github.com/openedx/wg-developer-experience/issues/166

---
## [BOO1980/boo-self](https://github.com/BOO1980/boo-self)@[f92f252bd5...](https://github.com/BOO1980/boo-self/commit/f92f252bd59fda882a31f641063932c7e79bedcd)
#### Friday 2023-04-28 14:05:21 by Hayley

Self: Unfuck yourself - I expect nothing accept everything 2

---
## [NexIsDumb/FNF-PsychEngine](https://github.com/NexIsDumb/FNF-PsychEngine)@[2e53ec4276...](https://github.com/NexIsDumb/FNF-PsychEngine/commit/2e53ec4276533623938420ba62bb9bfdc762ba09)
#### Friday 2023-04-28 15:11:10 by ⍚~Nex

making this commit to restart the checks

i hate my life

---
## [chaosvolt/Cataclysm-BN](https://github.com/chaosvolt/Cataclysm-BN)@[08d54d0287...](https://github.com/chaosvolt/Cataclysm-BN/commit/08d54d0287a1313cb810a1d3d74ca0e531189ae1)
#### Friday 2023-04-28 15:40:40 by KheirFerrum

Fix MGOAL_FIND_ITEM_GROUP, fix up some code (#2546)

* Reorganize

Code still sucks. In particular recruit_class doesn't compare properly with npc->my_class so MGOAL_RECRUIT_NPC_CLASS fails horribly even if you fix up that area of code to it actually points to type->recruit_class instead of recruit_class

For that matter mission has a select copy of several mission type defs and I can only assume this is due to legacy fuckery.

* Fix mission.cpp

Now will only allow you to select items if you have enough of them, and will only consume the necessary amount.

Added documentation for MGOAL_FIND_ITEM_GROUP

Thank god this wasn't too much work.

---
## [preminger/singularity](https://github.com/preminger/singularity)@[553118d0bb...](https://github.com/preminger/singularity/commit/553118d0bb930c3cba8a744953d275d356fdef63)
#### Friday 2023-04-28 15:52:53 by David Trudgian

Allow kernel squashfs / extfs mount to be disabled in singularity.conf

In singularity.conf, add two directives `allow kernel squashfs` and
`allow kernel extfs` which default to 'yes'. When set to 'no', these
directives prevent a squashfs mount or extfs mount from being
performed through the kernel. Note that this only happens in setuid
mode / as root.

squashfs and extfs mounts are added from the various locations that
handle loopback mounting of a filesystem image. The image could be a
container rootfs, an overlay, or an image bind. In each case the image
may be a standalone file or embedded in a SIF.

The simplest place to gate these mounts is in mount.AddImage, via the
existing check that the fs type is authorized as the source for an
image mount.

Authorized filesystems for image mounts are held in a package var. At
the start of container creation we now explicitly authorize squashfs
and extfs, unless disabled by singularity.conf.

Relying on a package scope variable isn't ideal. We have multiple
processes at container creation, so the authorization must be
performed in the right place. e2e tests have been added to verify
overlay, image bind, and container rootfs image flows.

Gating the filesystems earlier in the `PrepareConfig` portion of the
runtime is, in my opinion, more liable to errors as the checks would
have to be replicated in the multiple places that images are handled.

Ideally the mount.System could perhaps hold the list of allowed /
disallowed filesystems, that could be set when it is created. However,
this would require a large amount of refactoring to complex and
critical code.

---
## [Adriamarhua/evals](https://github.com/Adriamarhua/evals)@[776e4fa212...](https://github.com/Adriamarhua/evals/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Friday 2023-04-28 16:55:11 by JPrenter

Financial Math (Evals) (#566)

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
finance

### Eval description

Asks the model to calculate how much interest would be owed on a credit
card by a certain date, if a payment was made once but debt remains on
the card.

### What makes this a useful eval?

Finance is likely to be one of the biggest opportunities for LLMs to be
useful, because financial education is incredibly poor globally and the
impact of a mistake in financial calculations is severe. This eval tests
the models ability to combine math with its understanding of a topic
(finance). We plan to use this type of math at
[Dollarwise](https://www.dollarwise.ca) frequently going forward,
including integration into your comparison products. However, for this
to work reliably it's important that the model here can natively
understand financial concepts and apply math to them.

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
- [X] Include at least 100 high quality examples (it is okay to only
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
`evals/registry/evals/{name}.yaml`
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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 24th of September,
Sarah had spent $1237.42 on her credit card for the month of September.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued.Today is the
27th of September and Sarah makes a payment of $125 towards her credit
card. How much interest will she have been charged by October 15th if
she makes no additional payments? If the final interest figure is more
than 2-decimal places, always round down. Answer ONLY with a dollar
figure. Do not output any logic, output only the dollar figure for how
much interest she was charged for the period."}], "ideal": "9.42"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 19th of February,
Jason had spent $15.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 23rd of February and he makes a payment of $1 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.07"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 12th of February,
Jason had spent $10,674.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 18th of February and he makes a payment of $1,000 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "52.59"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 2nd of August, Jason
had spent $15,674.21 on his credit card for the month of August. This
credit card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. Today is the
18th of August and he makes a payment of $1,000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "79.77"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 15th of August, Jason
had spent $1000 on his credit card for the month of August. This credit
card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. mToday is the
18th of August and he makes a payment of $1000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.00"}
  ```
</details>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a0a76c2154...](https://github.com/mrakgr/The-Spiral-Language/commit/a0a76c21549a746f4e88182aaf4878e153844719)
#### Friday 2023-04-28 18:04:52 by Marko Grdinić

"6:30pm. https://youtu.be/kQPbuV-ZaVY
INTERVIEW CODING CHALLENGES

Is this guy really some god tier programmer?

https://youtu.be/zA1KuiAULEQ?t=1199
> Why bother with HTTP when every can easily be gRPC?

Isn't that over HTTP?

7:05pm. https://youtu.be/zA1KuiAULEQ?t=1510
> Config driven development.

This is an interesting term to keep in mind.

https://youtu.be/zA1KuiAULEQ?t=1633
> Mechanical sympathy.

I really like these two words.

https://youtu.be/zA1KuiAULEQ?t=1913

He makes his own prediciton which is that we are going to run into CPU power problem.

And admittedly, my reason is telling me that he is right, though I'll interpret his prediction as being about computation in general.

I wouldn't be in this shit if hardware growth was decent.

Yeah, I am fanboying over AI chip companies doing something miraculous, but remember how that turned out for me over the last decade?

That company I've pinned my hopes on will just turn out to be a dud, and then what?

I'd be better off putting my faith in the big cloud hyperscalers to give me something good, than AI chip startups.

https://youtu.be/zA1KuiAULEQ?t=1940
> We need a magical revolution that will just change stuff quite a bit.

He predicts a slow increase and that we are just about to hit the golden age of computing.

> This is just about the best time to be a programmer.

Then the video cuts off abruptly.

https://youtu.be/n7F7wMdgfuI?t=55
> Working in open source, is really, really hard. And it's not fun.

https://youtu.be/n7F7wMdgfuI?t=213
> Right now in our soft engineering world, the interviews are the easiest they've ever been.

https://youtu.be/n7F7wMdgfuI?t=277
> For me it takes 3 interviews to get into the interview world.

https://youtu.be/n7F7wMdgfuI?t=861
> I couldn't afford a house in the yard with a Netflix salary.

I recall those were 400k/year. What the hell?

https://youtu.be/n7F7wMdgfuI?t=1019
> This C++ is a really great language to learn in school.

Yeah, no.

https://youtu.be/n7F7wMdgfuI?t=1076
> A better kata: start a websocket server and build a chatroom.

https://youtu.be/n7F7wMdgfuI?t=1113
> I am out of my depth, I am not drawn to anything.

Kek. I could say the same thing.

https://youtu.be/n7F7wMdgfuI?t=1349
> Someone says I have a cool voice, I don't have a cool voice, I sound like a cartoon character.

https://youtu.be/n7F7wMdgfuI?t=1375
> Right now, the programming world is much harder. To get in is much harder.

https://youtu.be/n7F7wMdgfuI?t=1446
> He choose the world possible time ever to quit a job.

https://youtu.be/n7F7wMdgfuI?t=1519

This is good advice. I should ask the interviewer how I could have done better in interviews.

8:05pm. https://youtu.be/kUs-fH1k-aM
Do you REALLY need SSR?

https://youtu.be/MCQWfMg0Z9w?t=613
> A teacher once told me 90% of learning is teaching.

I never thought about it like that, but I will admit that doing Youtube vids is motivating me a lot.

I am not sure I'd have the drive to self improve without it.

8:25pm. https://youtu.be/02Dsv86tEPo?t=2444
【艦これ Heavy/Power Metal】Best of Yellow Squadron

Forget prime. Let me do some reading.

4/28/2023

8:40am. Let me read the Baki chapter first and then I'll get started.

8:55am. Let me start.

https://youtu.be/_p16mwfE9as
If you only learn ONE Shortcut... Make it this one! Davinci Resolve

I'll start with this, then Theo's SSR vid, then the microservice vid from yesterday.

The Kaminaki threads are really drawing me in, but I'll leave the anime for later.

https://youtu.be/_p16mwfE9as?t=94

Ohhhhhhhhhhhh!!!

You can paste the vids like this without them having the audio?

That was one of my major annoyances with DR and now it is resolved.

https://youtu.be/_p16mwfE9as?t=215

I had no idea.

https://youtu.be/_p16mwfE9as?t=299

This is an excellent video.

9:10am. Let me move on to Theo's vid.

https://youtu.be/kUs-fH1k-aM?t=494
Do you REALLY need SSR?

https://youtu.be/kUs-fH1k-aM?t=746

Ok, I am kind of tuning out here. What is going on? It doesn't matter too much.

https://youtu.be/kUs-fH1k-aM?t=1073
> Most sites and most experience should default to SSR when they can.

Hmmm...

https://youtu.be/46DkGih90a8
I Have Never Worked | Prime Reacts

9:35am. Let me watch this just for 5m.

https://youtu.be/46DkGih90a8?t=1266
> If this has been a common experience, there is no wonder there have been so many layoffs.

I've read the article itself a few days ago, but it is interesting how many people in his chatroom confirm what it is saying while Prime himself is the one being shocked.

10:10am. Ok, enough of these. Let me chill for a bit, and I'll finish the microservice vid from yesterday. I'll go start from finish instead of skipping it.

10:40am. Let me start for realsies.

It is time for microservices.

https://youtu.be/DFDbh1c9zyE
What are microservices?!?!? Let’s build one with .NET and Docker!

I am going to focus on this and then I am going to turn the poker app into a microservice. It is at that point that it will be worth putting on my resume.

https://youtu.be/DFDbh1c9zyE?t=449

I once watched a 1h video on Docker, but never used it properly. maybe this time around I will.

https://youtu.be/DFDbh1c9zyE?t=925

Why not copy them all at once?

https://youtu.be/DFDbh1c9zyE?t=1016

This is a good video.

11:10am. https://youtu.be/sstOXCQ-EG0
Let's Learn .NET - Microservices

I am not going to watch this, it's two hours.

Where is that learning path he mentioned.

https://learn.microsoft.com/en-us/dotnet/architecture/microservices/

> We wrote this guide for developers and solution architects who are new to Docker-based application development and to microservices-based architecture. This guide is for you if you want to learn how to architect, design, and implement proof-of-concept applications with Microsoft development technologies (with special focus on .NET) and with Docker containers.

Ok...

https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/docker-application-state-data

I am skimming through this, and I see that this is going to be another potus.

Nevermind these books and tutorials. Let me get started on video 32.

11:25am. You know what, let me get rid of env files. They are just washing my time.

11:35am.

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import {resolve} from 'node:path'

const config = {
    PORT: 8080,
    PROXY_PORT: 5000,
    ROOT: "src/client",
    DEPLOY: "deploy/public"
}

// https://vitejs.dev/config/
export default ({mode}) => {
    const target = `http://localhost:${config.PROXY_PORT}`

    return defineConfig({
        root: config.ROOT,
        build: {
            outDir: resolve(process.cwd(), config.DEPLOY)
        },
        server: {
            port: config.PORT,
            proxy: {
                "/api": {target, changeOrigin: true},
                "/socket": {target, ws: true}
                }
            },
        plugins: [react()],
        define: {
            // remotedev will throw an exception without this.
            global: {}
            }
        })
}
```

I am just doing some cleaning up of the project build.

```
caught Error: createRoot(...): Target container is not a DOM element.
    at createRoot (react-dom.development.js:29345:11)
    at Object.createRoot$1 [as createRoot] (react-dom.development.js:29800:10)
    at exports.createRoot (client.js:12:16)
    at Program_Internal_withReactSynchronousUsing (react.fs:57:32)
    at App.fs:188:9
    at App.fs:21:4
```

I am trying to run the Leduc applciation and am getting this error.

```
open Feliz
let view model dispatch =
    Html.div [
        Html.text "Hello"
    ]
```

What happens when I make the view this?

```
<body>
    <div id="root"></div>
    <script type="module" src="output/App.js"></script>
</body>
```

What is going on here? Here the id is root.

```
|> Program.withReactSynchronous "elmish-app"
```

But here it is looking for elmish app. I wonder how that happened?

```
<div id="app"></div>
```

Let's just make it app.

Yeah, now it prints hello.

11:45am. Pushed that into master. I git rid of the html and react courses.

Now...

11:55am. How do I edit the starting timecode again.

https://youtu.be/r20NdlqwSPU
Markers in Davinci Resolve and How to Export Markers for YouTube Chapters in DaVinci Resolve 18

This video shows it all. I compained about the advice, but in the end I couldn't find a better way.

https://youtu.be/r20NdlqwSPU?t=160

Why are so many timeline options only available when right clicking in the media pool?

12pm. Damnit. Resolve got me good here. For some reason these settings aren't in the cut page.

I did try right clicking on it before looking at the video for advice, but they weren't there. For fuck's sake.

12:20pm. I am 1m in, and need to take a break as I am getting hungry.

Let me stop here.

This served as an ice breaker.

2:20pm. Done with breakfast and chores.

Today I am taking a vacation so let me watch another ep of Kaminaki. Then I will resume.

The anime is pretty fun.

2:35pm. Ok, I'll get serious here.

I know that I am spending my good hours relaxing instead of programming, but anime is less fun when you are stressed out and tired after working for an entire day.

2:40pm. Now where was I?

3:35pm. How do I import from another video. Could I import the previous timeline. I want that merely for the sake of getting the audio from where it was left off previously.

https://youtu.be/J5R0wsAwCGk
Copy and paste TIMELINE to different project! Davinci Resolve Quick Tip!

https://youtu.be/J5R0wsAwCGk?t=20

This is the shortest tip that I've ever seen. Upvoted and close.

Oh, I can just paste a clip directly as well! That is even better for what I want to do.

7:10pm. Done with lunch and another round of chores. I guess I'll stop the session here.

Currently I am 7.5m into the screencast. I'll up my pace tomorrow.

Time to rest. Today was quite leisurely.

By the looks of things, microservices shouldn't be hard.

For some reason auth was way harder than it had any right to be which is why it took so long. But with this...

I'll acquire a lasting skill.

7:35pm. Actually websockets aren't too less expensive...but still 3x is not insignificant.

7:55pm. Had to do some extra editing.

8pm. I am 8:45m in.

Not bad.

Let me close here. I am pleased with my work today.

Tomorrow, I'll have a chance to do some interesting programming."

---
## [MF366-Coding/The-Psychologist](https://github.com/MF366-Coding/The-Psychologist)@[470f3814ae...](https://github.com/MF366-Coding/The-Psychologist/commit/470f3814aea022ccb15a6ad21d79075dca0e2741)
#### Friday 2023-04-28 18:13:50 by MF366-Coding

DONE FOR THE DAY

In summary, here is what I fixed:
* Added bosses I forgot about that (thank god I have a "paper" backup lmfao)
* Commented. A LOT.
* Easter Eggs :laughing:
* Saving and Loading Death checks
* Resetting Death Checks
* Forgot to close parentesis
* Forgot to add the underscore (the variable name was wrong)

I think that is all...
Did I forgot anything? I do not care if I did...

It was a pain to write the summary, so let's keep it like this, ok?

Tell me if you like it, Norb!

See ya bud! :wave: :heart:

---
## [zqjo39/overtime](https://github.com/zqjo39/overtime)@[3f21fe1c87...](https://github.com/zqjo39/overtime/commit/3f21fe1c87e4de0fed6c60dc26348d9d352668a3)
#### Friday 2023-04-28 18:33:05 by zqjo

doing..! ,:')

(i am doing both charts and employee manager at once, and hoo boy why is this so challenging-)
((i have also decided to make my life a living hell by also doing user pages too. which are also broken. WOOOOOOOOOO-))

---
## [bobskunk/coolstation](https://github.com/bobskunk/coolstation)@[553a9f502d...](https://github.com/bobskunk/coolstation/commit/553a9f502d2b4a11eaa005889f1d893d946de284)
#### Friday 2023-04-28 19:20:37 by BatElite

More minegen messing (#178)

* replace bullshit in mine map gen with turf flags

* kill quality, add starstone generation to zlevels

* Crop borders when iterating, define BS for CSGetSolid

* Inline CAGetSolid into desert gen, fucking hell

* explain some shit

* Erebite, miraclium now generate in z levels

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[2b2cb3dff6...](https://github.com/carlarctg/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Friday 2023-04-28 19:21:37 by LemonInTheDark

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
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[56d960a763...](https://github.com/BlueMemesauce/tgstation/commit/56d960a7630d0b03bfcd59c073b29393a70a1891)
#### Friday 2023-04-28 19:33:41 by GoldenAlpharex

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
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[3fdd716da5...](https://github.com/BlueMemesauce/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Friday 2023-04-28 19:33:41 by Cheshify

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
## [bee-on-the-green/back](https://github.com/bee-on-the-green/back)@[53032ec78f...](https://github.com/bee-on-the-green/back/commit/53032ec78f2b6547f45b12e743531a96f02a1290)
#### Friday 2023-04-28 19:57:36 by bee

Add files via upload

I have started the conky: it now provides: 


* Number of seconds since Epoch Time
* Age of $USER in days
* Uptime
* Remaining memory on nvme
* Remaining memory on SD card/  other removable media
* Ram usage
* CPU stats
* Load average in the last minute
* Temperature
* A quote from the computer. So far, and for testing purposes, I have set simple rules, these need to become more complex. Currently, Grep chooses 2 random words. They are separated by the verb 'to be' (is if the first word is singular; are if plural); If a word start with a capital letter, it is assumed that it refer to a person, it is placed in the first position). 

The Conky needs to become interactive: the user will be able to choose keywords, and the type of content she/he want to see. 

What I want to achieve:

Use the contend of the user's mailbox, as random quotes will be more relevant and funny.

Also, random pictures will appear from time to time (taken from the user 'Picture folder')

Same thing for videos: keywords will be used to grep subtitles, the part of the movie will then be displayed for a few seconds.

Also, I would like to be able to scrap images from the web, images that are related to the keyword.

In the future, I would like to use a desktop AI to generate relevant quotes. The user will have the ability to complain if she/he does not like the content. The machine will be able to know the user better.

Also, the AI will be able to provide advice/quotes/ideas. In case there is a way for the AI to access a log of the user behavior, it will learn and adapt.

To sum up, the whole idea is to provide the user with a digital sister/brother, able to provide funny content, funny while being relevant.

Everything is written thanks to Bash. Ideally, everything would need to be translated so that the user can benefit from a graphical interface, whether on Linux or Windows).

I only know Bash (and I am not very good at it (I started to do little scripts 6 month ago; I am not that young anymore, it does not really help; moreover, I am a people orientated person: computer seems very alien to me...but I love to learn new things, things that I am not supposed to be able to achieve).

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[129c74c945...](https://github.com/tgstation/tgstation/commit/129c74c945a3fe0bce2c29065f69424ce8551670)
#### Friday 2023-04-28 20:24:42 by carlarctg

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
## [amazon-mt8183-devs/android_kernel_amazon_mt8183](https://github.com/amazon-mt8183-devs/android_kernel_amazon_mt8183)@[03ef59458d...](https://github.com/amazon-mt8183-devs/android_kernel_amazon_mt8183/commit/03ef59458d50de3736336de9a24cec86a4aebf8b)
#### Friday 2023-04-28 20:41:20 by Christian Brauner

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
## [wilbertpol/mame](https://github.com/wilbertpol/mame)@[c4a19a68a6...](https://github.com/wilbertpol/mame/commit/c4a19a68a67cd32ffaaa37edfd6f1c2ba347905f)
#### Friday 2023-04-28 21:13:12 by Ivan Vangelista

New systems marked not working
------------------------------
Desert Gold (20202311, ASP) [anonymous, Heihachi_73]
Diamond Eyes (10129211, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (10177911, ASP) [anonymous, Heihachi_73]
Silk Road (10176811, ASP) [anonymous, Heihachi_73]
Snap Shot (20115211, ASP) [anonymous, Heihachi_73]
The Golden Gong (20196011, ASP) [anonymous, Heihachi_73]
Wild Cougar - Power Pay (30214211, ASP) [anonymous, Heihachi_73]
Wings over Olympus (10176511, ASP) [anonymous, Heihachi_73]

New clones marked not working
-----------------------------
5 Dragons (10176611, ASP) [anonymous, Heihachi_73]
5 Dragons (10178611, New Zealand) [anonymous, Heihachi_73]
5 Koi - Power Pay (1J016211, ASP) [anonymous, Heihachi_73]
50 Lions (0152077, US) [anonymous, Heihachi_73]
100 Lions (30223811, ASP) [anonymous, Heihachi_73]
Arabian Nights (10122611, ASP) [anonymous, Heihachi_73]
Big Ben (10169611, ASP) [anonymous, Heihachi_73]
Buccaneer (10181911, ASP) [anonymous, Heihachi_73]
Buffalo (20232611, ASP) [anonymous, Heihachi_73]
Brazil (10218511, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (20265311, New Zealand) [anonymous, Heihachi_73]
Dream Catcher (10172921, ASP) [anonymous, Heihachi_73]
Fire Dancer (10191311, ASP) [anonymous, Heihachi_73]
Fortune King (10230911, ASP) [anonymous, Heihachi_73]
Geisha (10122011, ASP) [anonymous, Heihachi_73]
Geisha (10112411, ASP) [anonymous, Heihachi_73]
Go For Green (10122111, ASP) [anonymous, Heihachi_73]
Golden Pyramids (10196511, ASP) [anonymous, Heihachi_73]
Heart of Gold (10184211, ASP) [anonymous, Heihachi_73]
Helen of Troy (10129121, ASP) [anonymous, Heihachi_73]
Helen of Troy (10116411, ASP) [anonymous, Heihachi_73]
Hollywood Dreams (10122811, ASP) [anonymous, Heihachi_73]
Helen of Troy (10122711, ASP) [anonymous, Heihachi_73]
House of Hearts (10208411, ASP) [anonymous, Heihachi_73]
Indian Dreaming (10192211, ASP) [anonymous, Heihachi_73]
King of the Nile (10127511, ASP) [anonymous, Heihachi_73]
Let's Go Fish'n (10223911, ASP) [anonymous, Heihachi_73]
Money Tree (10122211, ASP) [anonymous, Heihachi_73]
Paris Lights (10139011, ASP) [anonymous, Heihachi_73]
Peacock Magic (10134311, ASP) [anonymous, Heihachi_73]
Pelican Pete (10196211, ASP) [anonymous, Heihachi_73]
Pirates (10122311, ASP) [anonymous, Heihachi_73]
Pompeii (10122411, ASP) [anonymous, Heihachi_73]
Queen of Sheba (30146921, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10204311, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10192311, ASP) [anonymous, Heihachi_73]
Queen of the Nile Special Edition (10127411, ASP) [anonymous, Heihachi_73]
Ruby Magic (10148811, ASP) [anonymous, Heihachi_73]
Scatter Magic II (10122511, ASP) [anonymous, Heihachi_73]
Spring Festival (20267211, New Zealand) [anonymous, Heihachi_73]
Tigress (20243811, ASP) [anonymous, Heihachi_73]
Tiki Torch (10124011, New Zealand) [anonymous, Heihachi_73]
Torch of the Gods (20210211, ASP) [anonymous, Heihachi_73]
Turtle Treasure (10239811, ASP) [anonymous, Heihachi_73]
Where's The Gold (10177111, ASP) [anonymous, Heihachi_73]
Wild Cats (20258111, ASP) [anonymous, Heihachi_73]
Wild Goose (10155911, ASP) [anonymous, Heihachi_73]
Wild Panda (20225011, ASP) [anonymous, Heihachi_73]
Zorro (20167511, ASP) [anonymous, Heihachi_73]

-aristocrat/aristmk6.cpp updates:
* dumped 3 more System EPROM Sets [anonymous, Heihachi_73]
* renamed "Malaysian" games to ASP as the games don't have any specific region, only the BIOS does [Heihachi_73]

---
## [leweafan/beats](https://github.com/leweafan/beats)@[7cd75b2a14...](https://github.com/leweafan/beats/commit/7cd75b2a14704c3c87bd7456660f17de706725d9)
#### Friday 2023-04-28 22:10:48 by Andrew Kroh

Use include/exclude instead of whitelist/blacklist (#19325) (#23132)

While looking up some config info for winlogbeat, I came across this *whitelist/blacklist* section.

I submit this PR because black lives matter, racism is evil, and we should all help out to make the world a tiny bit better for our brothers and sisters of color ✊🏾

(cherry picked from commit 096344e3f1ac837eec9c6229bdb5e44740a1342d)

Co-authored-by: Joost De Cock <joost@decock.org>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[d31e3d3b83...](https://github.com/Buildstarted/linksfordevs/commit/d31e3d3b83819a94f103943b1a29b1f1887c59db)
#### Friday 2023-04-28 23:06:45 by Ben Dornis

Updating: 4/28/2023 11:00:00 PM

 1. Added: The Growing "Contentful" Gap - Web Performance Consulting
    (https://timkadlec.com/remembers/2023-04-23-growing-contentful-gap/)
 2. Added: SQL Is All You Need
    (https://jordivillar.com/blog/sql-is-all-you-need/)
 3. Added: Now that's what I call a Hacker
    (https://www.jitbit.com/alexblog/249-now-thats-what-i-call-a-hacker/)
 4. Added: Unleash Your Potential As a Brand
    (https://iaziz786.com/blog/branding-yourself/)
 5. Added: Blog | Samuel
    (https://samuelselleck.com/blog/)
 6. Added: Just Works For Me
    (https://den.dev/blog/just/)
 7. Added: Great and terrible mindsets are contagious
    (https://kyleprifogle.com/good-environments/)
 8. Added: The unpleasant hackiness of CSS dark mode toggles
    (https://code.mendhak.com/css-dark-mode-toggle-sucks/)
 9. Added: Episode 458 - Integration Patterns
    (https://azpodcast.azurewebsites.net/post/Episode-458-Integration-Patterns)
10. Added: Is Krita ready for HDR painting?
    (https://notes.ericjiang.com/posts/1241)
11. Added: Why it is becoming harder to choose a phone
    (http://shashanksthoughts.blogspot.com/2023/04/why-it-is-becoming-harder-to-choose.html)
12. Added: Maybe Great — No Idea Blog
    (https://noidea.dog/maybe-great)
13. Added: Economic disruption means more Creators
    (https://nickhayden.com/blog/economic-disruption-means-more-creators/)

Generation took: 00:06:35.1637545
 Maintenance update - cleaning up homepage and feed

---
## [newstools/2023-information-nigeria](https://github.com/newstools/2023-information-nigeria)@[517360fb77...](https://github.com/newstools/2023-information-nigeria/commit/517360fb776e90fca2d6fa6e5fb911bc274e07a3)
#### Friday 2023-04-28 23:07:02 by Billy Einkamerer

Created Text For URL [www.informationng.com/2023/04/8-year-old-girl-tests-positive-for-hiv-after-her-mothers-boyfriend-allegedly-raped-her-in-delta.html]

---
## [git/git](https://github.com/git/git)@[7891e46585...](https://github.com/git/git/commit/7891e465856e539c4a102dadec6dca9ac51c38df)
#### Friday 2023-04-28 23:29:16 by Jeff King

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[cfc384a3ff...](https://github.com/git-for-windows/git/commit/cfc384a3ff701124c2bd3f872fac31c8f1c89317)
#### Friday 2023-04-28 23:31:53 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---

