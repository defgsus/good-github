## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-02](docs/good-messages/2022/2022-02-02.md)


1,707,224 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,707,224 were push events containing 2,758,424 commit messages that amount to 209,193,902 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [Maven85/kodi](https://github.com/Maven85/kodi)@[ee5e0a485b...](https://github.com/Maven85/kodi/commit/ee5e0a485ba8b2321f50f493a7a10a063f8f54f7)
#### Wednesday 2022-02-02 00:00:10 by fritsch

AESinkAudioTrack: Pause-Burst - a little revisit

Pause-Bursts in RAW format are a red hering in general as they rely on
a non-existing API within Android. The implementation opens the audio
device but directly pauses it, hoping that internally the system does
the needful to keep the sink alive.

Sadly this happens intransparent for kodi, as the reported buffer of the
device stays zero. VideoPlayer calls AddPause multiple times in the
beginning to sync audio and video properly, while expecting that pause
bursts on audio side will fill up the sink (prepare it) and on the same time
causing a certain stable or better said: known delay when real data is
added later on.

The implementation asks android to pause, but blocks video player for the
amount of millis that it wants to add, stating: buffer is already filled.

As we sleep the non-existing data in, we need to "hack" the way back, remember
buffer is empty and not filled when first AddPacket is coming. We fake
this situation further until the real audio data has reached the same level
then we continue normally. Especially the way out is the hack as AE
exactly knows that out of a sudden 10 ms of data cannot be added in 0 ms if
the buffer is actually full. Though AE nicely gives us some time to get
our stuff in line.

But hack stays hack. If someone of google reads this:
Please add a method where you expose your IEC Packer so that we can create
and enqueue pause_bursts like normal audio. That way these hacks here would
not be needed at all.

---
## [Tanguan2/301-lab4-demo](https://github.com/Tanguan2/301-lab4-demo)@[46ca6fa786...](https://github.com/Tanguan2/301-lab4-demo/commit/46ca6fa786220da000d78a7b80b8441c264d09bf)
#### Wednesday 2022-02-02 00:33:27 by Tanguan2

I am that guy you are not that guy however in my opinion !

---
## [magatsuchi/tgstation](https://github.com/magatsuchi/tgstation)@[6ed2fafd4e...](https://github.com/magatsuchi/tgstation/commit/6ed2fafd4eccdc6f11e53acb9a1017b037d76360)
#### Wednesday 2022-02-02 00:39:08 by Iamgoofball

Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

---
## [JMartinez9820/Project_Brutality](https://github.com/JMartinez9820/Project_Brutality)@[98b24dc485...](https://github.com/JMartinez9820/Project_Brutality/commit/98b24dc4852882e8b7c8347a9474beca13e076f3)
#### Wednesday 2022-02-02 01:29:25 by Jason Martinez

Nazi Possession fix, Belphegor gore fix, Hell trooper...

and vicious imp heads added.
Nazi:
- Possession fixed
- Updated the charging and firing frames
Belphegor/Knight
- Fixed red blood issue
Demon Tech Trooper and Vicious Imp:
- Added decapitated heads

---
## [Alexandah/mOuSe_prototype](https://github.com/Alexandah/mOuSe_prototype)@[bf1a8ee721...](https://github.com/Alexandah/mOuSe_prototype/commit/bf1a8ee721c27d71c197b1054cc78cbf0e89927d)
#### Wednesday 2022-02-02 02:47:55 by Alexander Davis

added very basic test code to confirm that moving windows with keyboard events works easily. it does. fuck you react!

---
## [joshuabezaleel/porter](https://github.com/joshuabezaleel/porter)@[786738a7c3...](https://github.com/joshuabezaleel/porter/commit/786738a7c33b725fa1fae253f9ca789438553d33)
#### Wednesday 2022-02-02 03:30:20 by Carolyn Van Slyck

Use a distroless base image (#1656)

* Use distroless base image

Use a distroless base image for our porter docker images. This
has less of an attack surface because it only ships
the essentials to run porter, not the extra stuff that usually comes
with a linux distribution.

Signed-off-by: Carolyn Van Slyck <me@carolynvanslyck.com>

* Apply suggestions from code review

Signed-off-by: Carolyn Van Slyck <me@carolynvanslyck.com>

Co-authored-by: Nathaniel "Church" Hatfield <church13halo@gmail.com>

* Move agent's run.sh into Go

Since the nonroot distroless image doesn't have a shell, we can't use
run.sh to copy the porter config files into PORTER_HOME at container
start. I have implemented that in Go (sorry it's a lot vs what good ole
cp did for us under the hood).

One trick is that when /porter-config is mounted into the container by
k8s, it uses symlinks like this:

/porter-config
  ..data/porter.config
  porter.config -> ..data/porter.config

So it's not a straightforward as you'd think at first glance.

Signed-off-by: Carolyn Van Slyck <me@carolynvanslyck.com>

* Apply suggestions from code review

Signed-off-by: Carolyn Van Slyck <me@carolynvanslyck.com>
Co-authored-by: Vaughn Dice <vaughn.dice@fermyon.com>
Co-authored-by: Nathaniel "Church" Hatfield <church13halo@gmail.com>
Co-authored-by: Vaughn Dice <vaughn.dice@fermyon.com>

---
## [LingLuoEtherealling/rufus](https://github.com/LingLuoEtherealling/rufus)@[252759eb91...](https://github.com/LingLuoEtherealling/rufus/commit/252759eb917018392913245f58ab321a7ed5b42b)
#### Wednesday 2022-02-02 05:36:41 by Pete Batard

[grub] add yet another frigging patch to GRUB "2.04"

* GRUB 2.0 maintainer think they're doing a fine job, even when there are
  CRITICAL SECURITY FIXES that should warrant an immediate out of bound
  release, and instead consider that waiting MONTHS or YEARS to release
  anything is not a big deal at all.
* Ergo, distros, such as Ubuntu, start to pick whatever security patches
  they see fit, since they can simply not RELY on the upstream project to
  produce security releases in a timely manner. One such patch is:
  https://lists.gnu.org/archive/html/grub-devel/2021-03/msg00012.html
* But since there is no new GRUB release per se, they still call their GRUB
  version, onto which they applied patches that have come into existence
  more than 2 years after the actual 2.04 release, "GRUB 2.04".
* Obviously, since GRUB 2.04 + literally hundreds of cherry picked patches
  does deviate a lot from the last release, THINGS BREAK IN SPECTACULAR
  FASHION, such as the recently released Ubuntu 21.04 failing to boot with
  the error: grub_register_command_lockdown not found.
* Oh, and of course, regardless of all the above, if you ask anyone, they'll
  tell you that there's nothing fundamentally wrong with the GRUB release
  process (even if they should long have released 2.05, 2.05-1 and 2.05-2,
  were their maintainer ready to acknowledge that delaying releases DOES
  CREATES MAJOR ISSUES DOWSTREAM, as many people REPEATEDLY pointed to them
  on the GRUB mailing list) or with the Ubuntu GRUB versioning process (that
  really shouldn't be calling their version of GRUB "grub-2.04" but instead
  something like "grub-2.04_ubuntu"). Oh no siree! Instead, the problem must
  all be with Rufus and its maintainer, who should either spend their lives
  pre-emptively figuring which breaking patch every other distro applied out
  there, or limit media creation to DD mode, like any "sensible" person
  would do, since DD mode is the ultimate panacea (Narrator: "It wasn't").
* So, once again, a massive thanks to all the people who have been involved
  in the current GRUB 2.0 shit show, whose DIRECT result is to make end
  users' lives miserable, while GRUB maintainers are hell bent on continuing
  to pretend that everything's just peachy and are busy patting themselves
  on the back on account that "Fedora recently dropped more than 100 of the
  custom patches they had to apply to their GRUB fork" (sic). Nothing to see
  here, it's just GRUB maintainer's Jedi business as usual. Besides, who the
  hell cares about Windows users trying to transition to Linux in a friendly
  manner anyway. I mean, as long as something doesn't affect existing Linux
  users, it isn't a REAL problem, right?...

---
## [patevs/terminal](https://github.com/patevs/terminal)@[b1ace967a2...](https://github.com/patevs/terminal/commit/b1ace967a2f2bf17fdcb7dd4f1426b014378b83c)
#### Wednesday 2022-02-02 07:13:18 by Mike Griese

Two belling fixes (#12281)

Sorry for combining two fixes in one PR. I can separate if need be.

* [x] Closes #12276:
  - `"bellSound": null` didn't work. This one was easier, and is atomically in bcc2ca04fc14f39f37849b4bd837ad6cdb4cdaaa. Basically, we would deserialize that as an array with a single empty string in it, which we'd try to then play. I think it's more idomatic to have that deserialized as an empty array, which correctly falls back to playing the default sound.
* [x] Closes #12258: 
  - This one is the majority of the rest of the PR. If you leave the MediaPlayer open, then the media keys will _affect the Terminal_. More importantly, once the bell sounds, they'd replay the bell, which is insane. So the fix is to re-create the media player when we need it. We do this per-pane for simpler lifetime tracking. I'm not worried about the overhead of creating a mediaplayer here, since we're already throttling bells.
* Originally added in #11511
* [x] Tested manually
  - Use [`no.mp4`](https://www.youtube.com/watch?v=x2w9TyCv2gk) for this since that's like, 17s long
  - Checked that closing panes / the terminal while a bell was playing didn't crash
  - Playing a bunch of bells at once works
  - closing a pane stops the bell it's playing
  - once the bell stops, the media keys went back to working for Spotify
* [x] I work here

---
## [RevolutionPi/linux](https://github.com/RevolutionPi/linux)@[9443d6dbbc...](https://github.com/RevolutionPi/linux/commit/9443d6dbbcc1f36ba048895e9afca738847155b6)
#### Wednesday 2022-02-02 08:29:21 by Vladimir Oltean

net: dsa: be compatible with masters which unregister on shutdown

[ Upstream commit 0650bf52b31ff35dc6430fc2e37969c36baba724 ]

Lino reports that on his system with bcmgenet as DSA master and KSZ9897
as a switch, rebooting or shutting down never works properly.

What does the bcmgenet driver have special to trigger this, that other
DSA masters do not? It has an implementation of ->shutdown which simply
calls its ->remove implementation. Otherwise said, it unregisters its
network interface on shutdown.

This message can be seen in a loop, and it hangs the reboot process there:

unregister_netdevice: waiting for eth0 to become free. Usage count = 3

So why 3?

A usage count of 1 is normal for a registered network interface, and any
virtual interface which links itself as an upper of that will increment
it via dev_hold. In the case of DSA, this is the call path:

dsa_slave_create
-> netdev_upper_dev_link
   -> __netdev_upper_dev_link
      -> __netdev_adjacent_dev_insert
         -> dev_hold

So a DSA switch with 3 interfaces will result in a usage count elevated
by two, and netdev_wait_allrefs will wait until they have gone away.

Other stacked interfaces, like VLAN, watch NETDEV_UNREGISTER events and
delete themselves, but DSA cannot just vanish and go poof, at most it
can unbind itself from the switch devices, but that must happen strictly
earlier compared to when the DSA master unregisters its net_device, so
reacting on the NETDEV_UNREGISTER event is way too late.

It seems that it is a pretty established pattern to have a driver's
->shutdown hook redirect to its ->remove hook, so the same code is
executed regardless of whether the driver is unbound from the device, or
the system is just shutting down. As Florian puts it, it is quite a big
hammer for bcmgenet to unregister its net_device during shutdown, but
having a common code path with the driver unbind helps ensure it is well
tested.

So DSA, for better or for worse, has to live with that and engage in an
arms race of implementing the ->shutdown hook too, from all individual
drivers, and do something sane when paired with masters that unregister
their net_device there. The only sane thing to do, of course, is to
unlink from the master.

However, complications arise really quickly.

The pattern of redirecting ->shutdown to ->remove is not unique to
bcmgenet or even to net_device drivers. In fact, SPI controllers do it
too (see dspi_shutdown -> dspi_remove), and presumably, I2C controllers
and MDIO controllers do it too (this is something I have not researched
too deeply, but even if this is not the case today, it is certainly
plausible to happen in the future, and must be taken into consideration).

Since DSA switches might be SPI devices, I2C devices, MDIO devices, the
insane implication is that for the exact same DSA switch device, we
might have both ->shutdown and ->remove getting called.

So we need to do something with that insane environment. The pattern
I've come up with is "if this, then not that", so if either ->shutdown
or ->remove gets called, we set the device's drvdata to NULL, and in the
other hook, we check whether the drvdata is NULL and just do nothing.
This is probably not necessary for platform devices, just for devices on
buses, but I would really insist for consistency among drivers, because
when code is copy-pasted, it is not always copy-pasted from the best
sources.

So depending on whether the DSA switch's ->remove or ->shutdown will get
called first, we cannot really guarantee even for the same driver if
rebooting will result in the same code path on all platforms. But
nonetheless, we need to do something minimally reasonable on ->shutdown
too to fix the bug. Of course, the ->remove will do more (a full
teardown of the tree, with all data structures freed, and this is why
the bug was not caught for so long). The new ->shutdown method is kept
separate from dsa_unregister_switch not because we couldn't have
unregistered the switch, but simply in the interest of doing something
quick and to the point.

The big question is: does the DSA switch's ->shutdown get called earlier
than the DSA master's ->shutdown? If not, there is still a risk that we
might still trigger the WARN_ON in unregister_netdevice that says we are
attempting to unregister a net_device which has uppers. That's no good.
Although the reference to the master net_device won't physically go away
even if DSA's ->shutdown comes afterwards, remember we have a dev_hold
on it.

The answer to that question lies in this comment above device_link_add:

 * A side effect of the link creation is re-ordering of dpm_list and the
 * devices_kset list by moving the consumer device and all devices depending
 * on it to the ends of these lists (that does not happen to devices that have
 * not been registered when this function is called).

so the fact that DSA uses device_link_add towards its master is not
exactly for nothing. device_shutdown() walks devices_kset from the back,
so this is our guarantee that DSA's shutdown happens before the master's
shutdown.

Fixes: 2f1e8ea726e9 ("net: dsa: link interfaces with the DSA master to get rid of lockdep warnings")
Link: https://lore.kernel.org/netdev/20210909095324.12978-1-LinoSanfilippo@gmx.de/
Reported-by: Lino Sanfilippo <LinoSanfilippo@gmx.de>
Signed-off-by: Vladimir Oltean <vladimir.oltean@nxp.com>
Tested-by: Andrew Lunn <andrew@lunn.ch>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: Philipp Rosenberger <p.rosenberger@kunbus.com>

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[22e37babea...](https://github.com/Zeodexic/tsorcRevamp/commit/22e37babea0e566472fe94bf003cf6b50d144a22)
#### Wednesday 2022-02-02 09:18:42 by timhjersted

Artorias, lothric edits

Initial work begun on giving Artorias' attacks new sounds since they all previously used the same ones (still not finished as there are few sounds in the projectiles themselves that still need changing to an ice/electric sound)
Some of Artorias' attacks are now dependent on player range and proc less often, to make the fight less chaotic (just a temp measure until a proper boss rework)
Artorias now spawns Black Lothric Knights, because it kinda makes sense (lore-wise)
Lothric Knights now trigger crippled in HM when very close, for 1 second
Fire sound added to Ringed Knight's fire breath attack
Even less "you hear footsteps"
Zombie Worms spawn far less often, because they're just not that cool (imo)

---
## [Moffein/SniperClassic](https://github.com/Moffein/SniperClassic)@[c1d0f4ffbb...](https://github.com/Moffein/SniperClassic/commit/c1d0f4ffbbe60c7fc5baa2b58b3d084acf8f5a72)
#### Wednesday 2022-02-02 10:08:21 by TheTimeSweeper

oh yeah committing is a thing

lost in tweak creep again
sniper skin icons
transparencys on mastery guns, untested
fix to jerky aimyaw
terrible hacky fix to the gun floating off hands, untested, gotta see if it fucks with animations

---
## [xSkyyy/Nya](https://github.com/xSkyyy/Nya)@[887e29f4a3...](https://github.com/xSkyyy/Nya/commit/887e29f4a3d7bb1a97c276934b9e0b53020e1c7a)
#### Wednesday 2022-02-02 10:35:13 by Sky

remove outdated file (fuck you mac. why wont you let me commit from visual studio :rage:)

---
## [ProjectRadiant/packages_apps_Launcher3](https://github.com/ProjectRadiant/packages_apps_Launcher3)@[bde891c90f...](https://github.com/ProjectRadiant/packages_apps_Launcher3/commit/bde891c90f1e41ee9932c4342c874c602eb86da3)
#### Wednesday 2022-02-02 11:36:57 by Alex Cruz

Launcher3: Restart with change only on exit

This change allow the user to change everything they have to inside the
homescreen activity and only restart on exit. Previously this was a pain
in the fucking ass because you had to go in and set each option one by one
with a restart inbetween. At least now is not that big of a pain.

- Restart on destroy (hitting the back button, actionbar arrow)
- Restart when a chance is made and the home button is pressed

** Thanks "Jack" for code to detect home button
https://stackoverflow.com/a/27956263

- Cleaned up restart code

eyosen adapted to 10

Change-Id: I4962916ae0bd59d08247b59de585a97a2b9da3a1

---
## [zhengshuxin/wiredtiger](https://github.com/zhengshuxin/wiredtiger)@[24d35561e3...](https://github.com/zhengshuxin/wiredtiger/commit/24d35561e328e6568992bcafa18a560d56688185)
#### Wednesday 2022-02-02 11:44:15 by Keith Bostic

WT-5521 Cache stuck during format initial load, configured with library checkpoints (#5233)

* If reconciliation requires multiple blocks and checkpoint is running we'll eventually fail.
It's possible this is a big page that will take a lot of writes, avoid wasted work.

* Quit doing so much work in format's read-scan, it's not that useful any more and we're have already
verified the load.

* Configuring WiredTiger library checkpoints is done separately, rather than as part of the
original database open because format tests small caches and you can get into cache stuck
trouble during bulk load. Imagine a single thread doing lots of inserts and creating huge
leaf pages. Those pages can't be evicted when there are checkpoints running in the tree and
the cache gets stuck. That workload is unlikely enough the library can't handle it, and we
configure it away here.

---
## [aslepakurov/starlarky](https://github.com/aslepakurov/starlarky)@[d890c3a1f0...](https://github.com/aslepakurov/starlarky/commit/d890c3a1f06c520aca1bfa46346192de67963b33)
#### Wednesday 2022-02-02 11:48:22 by Mahmoud Abdelkader

Update Starlark to Tip (https://github.com/bazelbuild/bazel/commit/be96ade1cb6033d68d30ef9d20b063b87b86e646#diff-37cd73cae488b2421089c2b94c9a869cfb4a5f109753f60602b1dd20959bc573)

Changelog
for (Master)[https://github.com/bazelbuild/bazel/commit/be96ade1cb6033d68d30ef9d20b063b87b86e646#diff-37cd73cae488b2421089c2b94c9a869cfb4a5f109753f60602b1dd20959bc573]:

- Builtins injection: Rename _internal to _builtins and add functionality  …  This object is used in @_builtins .bzl files but is not accessible to user code. The `toplevel` and `native` fields give access to the *native* (pre-injected) values of symbols whose post-injected values are available to user .bzl files. For instance, -`_builtins.toplevel.CcInfo` in @_builtins code gives the original CcInfo definition from the Java code, even if `CcInfo` in a regular .bzl file refers to an injected value. (To avoid ambiguity, `CcInfo` itself is not a valid top-level symbol for @_builtins .bzl files.) The `internal` field contains any value registered via ConfiguredRuleClassProvider.Builder#addStarlarkBuiltinsInternal(). The `getFlag()` method can retrieve the values of StarlarkSemantics flags. Because of how flags are stored, it requires that a default value be given.
-  Starlark: better errors on integer overflow  …  Before:
```
>> [1] * (1 << 30) * (1 << 5)
Exception in thread "main" net.starlark.java.eval.Starlark$UncheckedEvalException: java.lang.ArrayIndexOutOfBoundsException: arraycopy: last destination index 1073741824 out of bounds for object array[0] (Starlark stack: [<toplevel>@<stdin>:1:1])
net.starlark.java.eval.Starlark.fastcall(Starlark.java:621)
net.starlark.java.eval.Starlark.execFileProgram(Starlark.java:892)
...
exit 1
```

Now:
```
>> [1] * (1 << 30) * (1 << 5) Traceback (most recent call last):
File "<stdin>", line 1, column 21, in <toplevel>
Error: got 34359738368 for repeat, want value in signed 32-bit range
```
-  starlark: int: ignore base prefix unless matches explicit base  …  Previously, when int was called with an explicit base, it would report an error if the digit string starts with a base prefix for a different base, such as int("0b101", 16). Now, it uses the base prefix only if it matches the requested base, so the example above would return 0x0b101, as would int("0x0b101", 16). See github.com/google/starlark-go/pull/344
-  starlark: delete StarlarkFile.parseWithPrelude  …  It was an obstacle to interpreter optimizations, as it caused a single StarlarkFile to contain statements whose locations come from different files. The previous workspace logic used parseWithPrelude to concatenate all the statements of the WORKSPACE files (prefix + main + suffix) and then split them into chunks, ignoring---crucially, several days work revealed---file boundaries. The splitChunks logic now achieves the same effect by representing chunks as lists of nonempty partial files, and calling execute() for each partial file in the chunk. The chunk splitting tests have been rewritten, clarified, and expanded to exercise the chunk-spans-file-boundaries case. Many thanks to Jon Brandvein for hours of help trying to figure out what the workspace logic does. It is not our team's finest work. Also: - minor consequent simplifications to parser and lexer. - narrow the scope of various try blocks (sorry, messy diff).
-  starlark: remove redundant pattern validity check in Printer  …
-  starlark: support %x, %X, and %o conversions in 'string % number'  …  Also, improve operand type error message to show type, not value. See github.com/bazelbuild/starlark/pull/154 for spec change.
-  Starlark: StarlarkInt.{floordiv,mod} now work with 64-bit integers  …  * No special case for 32-bit integers, division is slow anyway * Switch `mod` to use `Math.floorMod` for simplicity/safety Closes #12667.
-  starlark: delete deprecated EvalException(Location) constructor  …  ...as there are, at long last, no further uses within Bazel. Also, clarify doc comments regarding EvalException.callstack.
-  bazel analysis: preparatory cleanup to SRCTU error reporting  …  This change causes the error handling logic in StarlarkRuleConfiguredTargetUtil (SRCTU) to avoid the EvalException(Location) constructor. Instead, the auxiliary location, if any, of provider instantiation is simply prepended to the error message (see the infoError function) in anticipation of being printed after a newline. For example:  ERROR p/BUILD:1:1:\n  foo.bzl:1:2: <provider-related message> createTarget uses a distinct exception, BadImplementationFunction, for errors that arise not from the Starlark implementation function but from the post-processing of the providers. A follow-up change will replace this exception by directly reporting events to the handler, thus permitting both higher quality structured errors capable of reporting more than one relevant location, and multiple errors in a single pass. However, that change is too tricky to accomplish in this CL. Also: - move "advertised provider" and "orphaned file" checks into createTarget. - add comments to document this particularly painful code. - delete EvalException.getDeprecatedLocation.
-  Starlark: long StarlarkInt multiply without BigInteger  …  Use Hacker's Delight 8-2. Closes #12643.
-  bazel packages: use EventHandler not EvalException in .bzl "export" o…  …  …peration This allows us to delete one of the deprecated EvalException(Location,...) constructors. Similar follow-up changes (events not exceptions) will be required to eliminate the remaining such constructor. As a bonus, this approach allows multiple errors to be reported at once.

---
## [Bcadren/crawl](https://github.com/Bcadren/crawl)@[6fa8fe62d9...](https://github.com/Bcadren/crawl/commit/6fa8fe62d9c5aeac982110c2abf0cb1474054219)
#### Wednesday 2022-02-02 11:56:37 by Lucien

Move Reaper from Second Tier demon (2) to spiritual being (R). Additionally change holiness from demonic to non-living (the personification of death itself isn't really evil; just, a force of nature like an elemental). It will no longer be summoned by demon-summoning effects, but still are found in hell and pan and still come from mummy death curses and normal necromancy miscasts.

---
## [Hedda/wiki](https://github.com/Hedda/wiki)@[0caec94829...](https://github.com/Hedda/wiki/commit/0caec94829ff9cb74d31c22e5663569c796a1adc)
#### Wednesday 2022-02-02 14:16:07 by Hedda

Create General_Zigbee_Best_Practices_and_Troubleshooting_Tips.md

Suggest adding this to a troubleshooting section as questions and issues or problems related to range or coverage as well as Zigbee network stability with lost connections due to common known sources of interference are very common today.

As new Zigbee implementations and Zigbee devivces are more getting popular, new end-user beginners and new Zigbee users are posting in community forums about issues/problems related to Zigbee range and stability would have been resolved by simply following some kind of best practice guide.

The recommendations are otherwise largely indirectly based on posts in different communities with recommendations from experienced Zigbee developers (like Koen Kanters a.k.a. "Koenkk" of Zigbee2MQTT fame and Omer Kilic a.k.a. "omerk" who designed the open-source zzh adapter) plus several longer Zigbee range discussions threads found all around in the Home Assistant / ZHA / Zigpy, Zigbee2MQTT, Hubitat, and  openHAB community forums with users tips on how-to improve network range and stability and other support channels.

These suggestions is meant to act as general advice Zigbee to help users on relatively simple actions they can and should take if they wish to greatly improve signal range and mesh network coverage or lessen possible signal interference due to electromagnetic interference (a.k.a. radio interference). All of these essential actions to set up a solid Zigbee network can easily and relatively quickly be solved by the users themselves. Also following the recommendations as a new user and Zigbee beginners should a lot of people much frustration as poor signal reception quality can cause intermittent connection issues which can be a pain to troubleshoot.

Again, for example, the most important advice posted in the forums is for users to use a long USB-extension cable for their Zigbee Coordinator and to also buy more "Zigbee Router" devices (normally AC mains-powered Zigbee devices) to their home because they will route/repeat the Zigbee communication and as such extend the network range. Also, more common advice is upgrading firmware on both Zigbee Coordinator as well as Zigbee devices, or just buying a better Zigbee Coordinator adapter if users are using ones that are based on an obsolete chip and/or one for which the firmware is no longer maintained by the manufacturer.

FYI, my research reference and indirectly inspirations include info from Habitat and basic Zigbee troubleshooting tips in other communities:

https://www.usb.org/sites/default/files/327216.pdf
https://docs.hubitat.com/index.php?title=How_to_Build_a_Solid_Zigbee_Mesh
https://www.zigbee2mqtt.io/guide/faq/
https://gadget-freakz.com/how-to-improve-your-zigbee-network/
https://zigbeealliance.org/news_and_articles/step-by-step-guide-getting-started-with-zigbee/
https://nts.com/services/education/articles/zigbee-best-practices/
https://www.digikey.com/en/articles/tips-for-optimizing-performance-and-energy-use-of-zigbee-radios
https://www.control4.com/docs/product/zigbee/best-practices/english/revision/B/
https://community.hubitat.com/t/xiaomi-aqara-devices-pairing-keeping-them-connected/623
https://community.smartthings.com/t/faq-networking-and-reducing-channel-interference-between-wifi-and-zigbee/40159/3
https://phoscon.de/en/support
https://www.metageek.com/training/resources/zigbee-wifi-coexistence/
https://notenoughtech.com/featured/a-simple-trick-to-reduce-zigbee-coordinator-wifi-interference/

---
## [hiyokun-d/newYears2023](https://github.com/hiyokun-d/newYears2023)@[9aa604aab0...](https://github.com/hiyokun-d/newYears2023/commit/9aa604aab0789fe809b07a8ad34ac779ee6254e1)
#### Wednesday 2022-02-02 14:43:04 by nothing

update just a little bit update and just add NEWS this is just from indonesia so why not? this is my website so FUCK YOU

---
## [ltratt/yk](https://github.com/ltratt/yk)@[36b368803b...](https://github.com/ltratt/yk/commit/36b368803b5a10541483f7fe667b92c5b2cfad91)
#### Wednesday 2022-02-02 15:06:10 by Laurence Tratt

Don't grab the THREAD_MTTHREAD on every control point call.

We can't rely on thread locals being fast (on some platforms they are,
on some they aren't; Rust's thread locals are, currently, not fast
because of the lazy loading) so we want to avoid accessing them in the
control point's fast paths.

This commit moves loading from the `THREAD_MTTHREAD` thread local to
only those portions of code that really need access to it. Mostly this
is fairly simple, but there is one horrible hack in here that will
probably haunt me in my dreams until I can think of a better way of
doing this.

However, getting rid of this thread local should be worth it, as it will
allow us to port back more of the old test suite. At that point,
refactoring the evil hack should be doable with more confidence, because
there'll be a test suite to catch (at least some) errors!

---
## [mbauhardt/dwm](https://github.com/mbauhardt/dwm)@[67d76bdc68...](https://github.com/mbauhardt/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-02-02 15:13:20 by Chris Down

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
## [vignetteapp/MediaPipe.NET](https://github.com/vignetteapp/MediaPipe.NET)@[6ae6e5a21e...](https://github.com/vignetteapp/MediaPipe.NET/commit/6ae6e5a21e671a171bda3803925e96071311e73c)
#### Wednesday 2022-02-02 15:28:17 by Ayane

Le unhaskellize

🖑Hey🖐 buddy,👬 I think🤔 you've 👉got the 🛇wrong🚫 door🚪 the 🐄leather🐄 club's ♴two♴ blocks down☟. 🖕Fuck🖕↗You↘.Oh, Fuck♂You 🐄leather🐄 man ❓Maybe❔ 👬you and I👬 should settle it💪 👇right here👇 on the 💍ring💍 if you think🤔 your so 💪tough💪. Oh yea?😡 I'll kick👣 your ass!👊 Ha!😂 Yeah right👍 man. Let's go!✔ Why don't you🤔 get out of that 🐄leather stuff?🐄 I'll strip👙 down☟ out of this and we'll settle👪 it right here👇 in the ring. What ❔❓❔do you say? 🤐Yeah⁉ no problem buddy👬❗ You got it. 🖒Get out of that uh, jabroni outfit👕👔👖. Yeah, smart🤔 ass. I'll show😡you who's the ☝boss☝ of this 🏋gym.🏋

Signed-off-by: GitHub <noreply@github.com>

---
## [oracle/dtrace-linux-kernel](https://github.com/oracle/dtrace-linux-kernel)@[83f02cf9b0...](https://github.com/oracle/dtrace-linux-kernel/commit/83f02cf9b0ce18b6a27d34c6a25933791779e807)
#### Wednesday 2022-02-02 16:11:01 by Nick Alcock

waitfd: new syscall implementing waitpid() over fds

This syscall, originally due to Casey Dahlin but significantly modified
since, is called quite like waitid():

	fd = waitfd(P_PID, some_pid, WEXITED | WSTOPPED, 0);

This returns a file descriptor which becomes ready whenever waitpid()
would return, and when read() returns the return value waitpid() would
have returned.  (Alternatively, you can use it as a pure indication that
waitpid() is callable without hanging, and then call waitpid()).  See the
example in tools/testing/selftests/waitfd/.

The original reason for rejection of this patch back in 2009 was that it
was redundant to waitpid()ing in a separate thread and transmitting
process information to another thread that polls: but this is only the
case for the conventional child-process use of waitpid().  Other
waitpid() uses, such as ptrace() returns, are targetted on a single
thread, so without waitfd or something like it, it is impossible to have
a thread that both accepts requests for servicing from other threads
over an fd *and* manipulates the state of a ptrace()d process in
response to those requests without ugly CPU-chewing polling (accepting
requests requires blocking in poll() or select(): handling the ptraced
process requires blocking in waitpid()).

There is one ugliness in this patch which I would appreciate suggestions
to improve (due to me, not due to Casey, don't blame him).  The poll()
machinery expects to be used with files, or things enough like files
that the wake_up key contains an indication as to whether this wakeup
corresponds to a POLLIN / POLLOUT / POLLERR event on this fd.  You can
override this in your poll_queue_proc, but the poll() and epoll() queue
procs both have this interpretation.

Unfortunately, this is not true for waitfds, which wait on the the
wait_chldexit waitqueue, whose key is a pointer to the task_struct of
the task being killed.  We can't do anything with this key, but we
certainly don't want the poll machinery treating it as a bitmask and
checking it against poll events!

So we introduce a new poll_wait() analogue, poll_wait_fixed().  This is used
for poll_wait() calls which know they must wait on waitqueues whose keys are
not a typecast representation of poll events, and passes in an extra
argument to the poll_queue_proc, which if nonzero is the event which a
wakeup on this waitqueue should be considered as equivalent to.  The
poll_queue_proc can then skip adding entirely if that fixed event is not
included in the set to be caught by this poll().

We also add a new poll_table_entry.fixed_key.  The poll_queue_proc can
record the fixed key it is passed in here, and reuse it at wakeup time to
track that a nonzero fixed key was passed in to poll_wait_fixed() and that
the key should be ignored in preference to fixed_key.

With this in place, you can say, e.g. (as waitfd does)

        poll_wait_fixed(file, &current->signal->wait_chldexit, wait,
                POLLIN);

and the key passed to wakeups on the wait_chldexit waitqueue will be
ignored: the fd will always be treated as having raised POLLIN, waking
up poll()s and epoll()s that have specified that event.  (Obviously, a
poll function that calls this should return the same value from the poll
function as was passed to poll_wait_fixed(), or, as usual, zero if this
was a spurious wakeup.)

I do not like this scheme: it's sufficiently arcane that I had to go
back to my old commit messages to figure out what it was doing and
why.  But I don't see another way to cause poll() to return on
appropriate activity on waitqueues that do not actually correspond to
files.  (I do wonder how signalfd works.  It doesn't seem to need any of
this and I don't understand why not.  I would be overjoyed to remove the
whole invasive poll_wait_fixed() mess, but I'm not sure what to replace
it with.)

Orabug: 29891866
Signed-off-by: Nick Alcock <nick.alcock@oracle.com>
Signed-off-by: Kris Van Hees <kris.van.hees@oracle.com>
Signed-off-by: Tomas Jedlicka <tomas.jedlicka@oracle.com>
Signed-off-by: Eugene Loh <eugene.loh@oracle.com>
Signed-off-by: David Mc Lean <david.mclean@oracle.com>
Signed-off-by: Vincent Lim <vincent.lim@oracle.com>
Reviewed-by: Nick Alcock <nick.alcock@oracle.com>

---
## [TimPoppel/SNSGameJam](https://github.com/TimPoppel/SNSGameJam)@[a0ebe518f6...](https://github.com/TimPoppel/SNSGameJam/commit/a0ebe518f615217143f22bc72b25693be351a834)
#### Wednesday 2022-02-02 16:25:31 by Sem

fuck you tim, i hate you. ye you go fetch little baby man

---
## [invertego/mame](https://github.com/invertego/mame)@[a49e215466...](https://github.com/invertego/mame/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Wednesday 2022-02-02 16:37:39 by Firehawke

Apple II updates for January 2022 (#9189)

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Earth Science: Interplanetary Travel (cleanly cracked) [4am, Firehawke]
Isaac Newton and F.I.G. Newton (cleanly cracked) [4am, Firehawke]
Return to Reading: The Call of the Wild (cleanly cracked) [4am, Firehawke]
The German Hangman (cleanly cracked) [4am, Firehawke]
Legionnaire (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Bridge Tutor with Precision and Scientific Bidding (cleanly cracked) [4am, san inc, Firehawke]
The French Hangman (cleanly cracked) [4am, Firehawke]
The Russian Hangman (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Mickey's Space Adventure [4am, Firehawke]
The Environment Life Dynamic [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Stellar Power [4am, Firehawke]

New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Ken Uston's Professional Blackjack (Version 1.12) (cleanly cracked) [4am, Firehawke]
Dinosaur's Lunch (cleanly cracked) [4am, Firehawke]
Race Car Keys (cleanly cracked) [4am, Firehawke]
Functional Harmony: Basic Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Diatonic Seventh Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Borrowed and Altered Chords (cleanly cracked) [4am, Firehawke]
Building Reading Skills: The Letter-Sound Farm (cleanly cracked) [4am, Firehawke]
Follow Me (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

The German Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Russian Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Spanish Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Exploring Library Land (cleanly cracked) [4am, Firehawke]
Library Treasure Hunt (cleanly cracked) [4am, Firehawke]
Expedition U.S.A.! (cleanly cracked) [4am, Firehawke]
Codes and Cyphers (cleanly cracked) [4am, san inc, Firehawke]
Ripley's Believe It Or Not: Beginning Library Research Skills (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Glutton [4am, Firehawke]

---
## [braindedboi/kernel_realme_moon](https://github.com/braindedboi/kernel_realme_moon)@[df502c8f48...](https://github.com/braindedboi/kernel_realme_moon/commit/df502c8f480f0592fe3ab07599045a7aed64118a)
#### Wednesday 2022-02-02 17:56:27 by Wang Han

moon: power: Introduce OnePlus 3 fingerprintd thaw hack
Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

Signed-off-by: braindedboi <boibrainded@gmail.com>

---
## [braindedboi/kernel_realme_moon](https://github.com/braindedboi/kernel_realme_moon)@[1ab72e9259...](https://github.com/braindedboi/kernel_realme_moon/commit/1ab72e9259564a6baa30d19ff47e7996796689ba)
#### Wednesday 2022-02-02 18:04:54 by Wang Han

moon: power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b

Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: braindedboi <boibrainded@gmail.com>

Co-authored-by: Cyber Knight <cyberknight755@gmail.com>

---
## [39alpha/eq3_6](https://github.com/39alpha/eq3_6)@[e02e416649...](https://github.com/39alpha/eq3_6/commit/e02e416649ee99d6d987045e4feb6d8ca2adc7cf)
#### Wednesday 2022-02-02 18:15:49 by Cole Mathis

Update eq6 code because THERES A FUCKING DUPLICATED LINE IN THE GOD DAMN SOURCE CODE!!! Tucker Ely pointed out that line 927 and 928 are duplicated, one was deleted here."

---
## [cpcallen/blockly](https://github.com/cpcallen/blockly)@[c03fb8bfad...](https://github.com/cpcallen/blockly/commit/c03fb8bfad05a8ca813519ef0900d3f62bf9132c)
#### Wednesday 2022-02-02 18:53:25 by Christopher Allen

Experimental conversion of blockly.js to ES Module

To see if my theory about module loading was correct, and that we
would be fine so long as the module loader didn't attempt to
load any goog.module after the first ES Module, I have converted
blockly.js to ESM.

The conversion is a terrible quick hack; all the stuff concerning
get/set accessors is totally broken and there are lots of other
problems, but it is functional otherwise.

And module loading does appear to be working correctly.

There is a problem, however: doing

    var Blockly = goog.require('Blockly');

in blockly_uncompiled.js doesn't work, because (curse you, base.js!)
goog.require only returs the module export object when called from
a goog.module (or ES module, presumably), not when called from a
script.

I've tried to work around this using goog.module.get but for some
reason it is also just returning null.  Further investigation
required!

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Wednesday 2022-02-02 19:33:12 by Albert Liu

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
## [BrandonJorgen/Cavalry](https://github.com/BrandonJorgen/Cavalry)@[94e5838b55...](https://github.com/BrandonJorgen/Cavalry/commit/94e5838b5560acb625f32863897c9b2a5685281d)
#### Wednesday 2022-02-02 19:44:05 by Brandon

life continues to be pain and I have to fix epic's shit

---
## [avar/git](https://github.com/avar/git)@[c6b0437db0...](https://github.com/avar/git/commit/c6b0437db037f3e41cf0c0af8e764ce506c441c1)
#### Wednesday 2022-02-02 20:03:35 by Ævar Arnfjörð Bjarmason

object-file.c: do fsync() and close() before post-write die()

Change write_loose_object() to do an fsync() and close() before the
oideq() sanity check at the end. This change re-joins code that was
split up by the die() sanity check added in 748af44c63e (sha1_file: be
paranoid when creating loose objects, 2010-02-21).

I don't think that this change matters in itself, if we called die()
it was possible that our data wouldn't fully make it to disk, but in
any case we were writing data that we'd consider corrupted. It's
possible that a subsequent "git fsck" will be less confused now.

The real reason to make this change is that in a subsequent commit
we'll split this code in write_loose_object() into a utility function,
all its callers will want the preceding sanity checks, but not the
"oideq" check. By moving the close_loose_object() earlier it'll be
easier to reason about the introduction of the utility function.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [Sb0009/holberton-system_engineering-devops](https://github.com/Sb0009/holberton-system_engineering-devops)@[8a24e1189f...](https://github.com/Sb0009/holberton-system_engineering-devops/commit/8a24e1189fd70d1673a4f3a1f9ea9949dd23eac5)
#### Wednesday 2022-02-02 20:45:53 by Siham Badyine

0x00. Shell, basics

READ THE F**KING  MANUAL !

&#127946;
0. Where am I?
Write a script that prints the absolute path name of the current working directory.

Example:

$ ./0-current_working_directory
/0x00-shell_basics
$



1. What’s in there?
Display the contents list of your current directory.

2. There is no place like home
Write a script that changes the working directory to the user’s home directory.

You are not allowed to use any shell variables



3. The long format
Display current directory contents in a long format


4. Hidden files
Display current directory contents, including hidden files (starting with .). Use the long format.


5. I love numbers
Display current directory contents.

Long format
with user and group IDs displayed numerically
And hidden files (starting with .)



6. Welcome
Create a script that creates a directory named my_first_directory in the /tmp/ directory.


7. Betty in my first directory
Move the file betty from /tmp/ to /tmp/my_first_directory.


8. Bye bye Betty
Delete the file betty.

The file betty is in /tmp/my_first_directory



9. Bye bye My first directory
Delete the directory my_first_directory that is in the /tmp directory.

10. Back to the future
Write a script that changes the working directory to the previous one.

11. Lists
Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.


12. File type
Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.

13. We are symbols, and inhabit symbols
Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.


14. Copy HTML files

Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.


15. Let’s move
Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.

You can assume that the directory /tmp/u will exist when we will run your script


16. Clean Emacs
Create a script that deletes all files in the current working directory that end with the character ~.


17. Tree
Create a script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.

You are only allowed to use two spaces (and lines) in your script, not more.



18. Life is a series of commas, not periods
Write a command that lists all the files and directories of the current directory, separated by commas (,).

Directory names should end with a slash (/)
Files and directories starting with a dot (.) should be listed
The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
Only digits and letters are used to sort; Digits should come first
You can assume that all the files we will test with will have at least one letter or one digit
The listing should end with a new line


19. File type: School

Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.

---
## [MichaelDanlin/roll20-character-sheets](https://github.com/MichaelDanlin/roll20-character-sheets)@[0a85fe1d43...](https://github.com/MichaelDanlin/roll20-character-sheets/commit/0a85fe1d43b6b0ffd568266e0cec323743276af4)
#### Wednesday 2022-02-02 20:53:52 by MichaelDanlin

Update Genesys-CharacterSheet.html

Adding the ability to add different Knowledge skills to the actual knowledge section, being able to have magical attacks in the personal weapons section, and adding differing weapon combat skills for vehicles.

I am terrible at coding so there is probably a lot of issues. But my friends and I would love to see these additions made

---
## [wbt0010/GBC-Developer](https://github.com/wbt0010/GBC-Developer)@[631768321d...](https://github.com/wbt0010/GBC-Developer/commit/631768321d265b573ce0f974d1105589d4ca1d96)
#### Wednesday 2022-02-02 21:13:01 by ezra

holy fuck it finally compiles

sorry if I broke other stuff
update your gbdk I updated to the modern dependencies

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[8921b20492...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/8921b204928b9ea36753dff7ad869d322f26fb06)
#### Wednesday 2022-02-02 21:22:44 by Peter Zijlstra

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
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [argarak/uqm-vita](https://github.com/argarak/uqm-vita)@[604063805d...](https://github.com/argarak/uqm-vita/commit/604063805d12644e31cf4c208e8d281b10d9806f)
#### Wednesday 2022-02-02 21:59:18 by argarak

support for vita filesystem paths

new error to fix: "Fatal error: Could not find content"
paths seem to be accepted and work now, i think?

this filesystem stuff is kinda the worst and my implementation
is ridiculously hacky. this took many hours, this uio code is
not fun but i think i'm getting to the end of it now, let's
hope...

i will remove all the crazy debug printfs in a future commit
still not sure if i will need those for debugging next time

---
## [johnrambow/p-g-wodehouse_a-gentleman-of-leisure](https://github.com/johnrambow/p-g-wodehouse_a-gentleman-of-leisure)@[fa0fa6c864...](https://github.com/johnrambow/p-g-wodehouse_a-gentleman-of-leisure/commit/fa0fa6c86481f7bc29898a28f8f427d2062d3511)
#### Wednesday 2022-02-02 22:16:23 by John Rambow

[Editorial] Removing unneeded hyphens to match Merriam-Webster; adding a few commas for clarity

as they stood there,
billiard-ball, etc.
blasting-powder
brain-processes
Breaking-off
cigarette-case
clothes-brush
coat-collar
danger-signal
dinner-table
dressin’-room chasin’ around for de jool-box,
dressing-gong
Golden-haired little Jimmy Mullins
good-humour
half bad (?)
half-a-crown
half-past eight, etc.
hare-and-hounds
hind-leg
love-letters
master-burgler
middle-age
money-market
mooring-rope
morning-room
Nerve centres
newly-born sense
off as a sudden, awful suspicion,
opera-glasses
plainclothes
pocket-money
police-station
postage-stamp
score-sheet
station door
supper-table
treasure-hunt
What made you do it?” he asked abruptly echoing her own question.

---
## [conceptdev/maui](https://github.com/conceptdev/maui)@[ac6befcbee...](https://github.com/conceptdev/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Wednesday 2022-02-02 22:42:44 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---

