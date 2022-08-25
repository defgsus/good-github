## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-24](docs/good-messages/2022/2022-08-24.md)


2,055,366 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,055,366 were push events containing 3,157,727 commit messages that amount to 246,694,688 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6f2354e694...](https://github.com/tgstation/tgstation/commit/6f2354e694f3412a76b383f684a0bfc85a448d8e)
#### Wednesday 2022-08-24 00:09:26 by san7890

Fixes Fucked Job Requirement Displays (#69368)

* Fixes Fucked Job Requirement Displays

Hey there,

I fucked up in #68856 (5b77361d399ba0dd992e61a16b9bbe38e8aa5a60). We weren't supposed to add another MINUTES multiplication here. I don't even remember why I did this if we are being perfectly honest with each other. Whoops.

fix: You should now no longer need thousands of hours to unlock your favorite head of staff role.

---
## [glyphr-studio/Glyphr-Studio-2](https://github.com/glyphr-studio/Glyphr-Studio-2)@[036655067a...](https://github.com/glyphr-studio/Glyphr-Studio-2/commit/036655067a56ab3d8a6e0f71973c53b7de5f047e)
#### Wednesday 2022-08-24 00:09:44 by Matt LaGrandeur

FUCK YOU I INDENT WITH TABS :shipit:

I spent 10 minutes converting all the spaces. #worthit

---
## [giordano/BinaryBuilderBase.jl](https://github.com/giordano/BinaryBuilderBase.jl)@[cf90fb4377...](https://github.com/giordano/BinaryBuilderBase.jl/commit/cf90fb437738ecc8495b9ac150c7e8436f3110e2)
#### Wednesday 2022-08-24 00:15:36 by Keno Fischer

Add support for building sanitizer-enabled jlls

This adds support for automatically adding the appropriate `-fsanitize=`
flags when the platform includes a `sanitizer` tag. This is particularly
intended for msan, which requires that all .so's in the system are built
using it, but could be useful for other sanitizers also.

There's a couple annoyances. One is that we don't currently actually ship
the sanitizer runtime libraries in our rootfs. Thus, if we want to start
using this, we'd have to add a BuildDependency on LLVMCompilerRT_jll and
manually copy the runtime libraries into place. Not the end of the world,
but certainly a wart.

The other issue is that `platform_matches` (which is defined in Base) of
course currently ignores the `sanitizer` tag. In theory it is possible
to add a custom compare strategy, but since we're specifying the target
by triplet, we can't really add that. Easy enough to add manually here,
but does make me wonder whether the custom compare strategies in Base
actually fit the use case.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6940c3bb59...](https://github.com/treckstar/yolo-octo-hipster/commit/6940c3bb59664cbee12b24a2a953120e68cb6057)
#### Wednesday 2022-08-24 00:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [vini1264/DNF-reimposition](https://github.com/vini1264/DNF-reimposition)@[7d7987b624...](https://github.com/vini1264/DNF-reimposition/commit/7d7987b6243892edbe0fc232c253980a02d02160)
#### Wednesday 2022-08-24 00:26:31 by Justin Marshall

Added "damn that's the second those alien bastards shot up my ride" to map05_night and new music from LOTB

---
## [turtle0x1/LxdMosaic](https://github.com/turtle0x1/LxdMosaic)@[a906d78221...](https://github.com/turtle0x1/LxdMosaic/commit/a906d782218f53d5a41f98078ccbdf06b368de3d)
#### Wednesday 2022-08-24 02:00:22 by turtle0x1

Remove deprecated /deploymentProgress/:deploymentId route from event.js

Removes;
  - `vendor` phone-home string from deployments
  - deploymentProgress/:deploymentId route from event.js

Its a route that doesn't require authentication that could be abused,
really it should be allowed to stay but this commit removes all the code
at once so it could be undone.

The rational behind it is that once a cloud-init is done running
its an endpoint that can be called to say "yes im done setting up".

Its a route that cant really ever have auth on it, but;
 - We have no security docs warning about it (its not a real vuln)
 - Deployments is kinda dead, it needs an overhall
 - The code it called had been removed before and this was just a stub

This is a shame because I remeber the pain of getting it working, but
that will teach me to push code that isn't ready!

---
## [besteon/Ironmon-Tracker](https://github.com/besteon/Ironmon-Tracker)@[761fe4b0f1...](https://github.com/besteon/Ironmon-Tracker/commit/761fe4b0f171d6fca47aa72e196aa42680da7279)
#### Wednesday 2022-08-24 02:16:13 by Zac Elsik

Some randomized moves still showed "1" power

This correctly captures all weird power but actually no-power moves:
Guillotine (12)
Horn Drill (32)
SonicBoom (49)
Low Kick (67)
Counter (68)
Seismic Toss (69)
Dragon Rage (82)
Fissure (90)
Night Shade (101)
Bide (117)
Psywave (149)
Super Fang (162)
Flail (175)
Reversal (179)
Return (216)
Present (217)
Frustration (218)
Magnitude (222)
Hidden Power (237)
Mirror Coat (243)
Endeavor (283)
Sheer Cold (329)

---
## [dnaspider/dna](https://github.com/dnaspider/dna)@[facc41116f...](https://github.com/dnaspider/dna/commit/facc41116f6e34d41b7c6eeb9ae3edd8aaa5482a)
#### Wednesday 2022-08-24 02:47:29 by Pete

🧬🕷⌨

<RGB~:> possible bug(s) worked out.

Assuming nothing broke from adding & references in struct Multi {}.

Must go to bed otherwise would stay up cracking away at this. Will be back tomorrow evening for more.
Check out the Odysee tunes in the mean time (yes thats me on the beats; recording).
Good night friends

---
## [ziglang/zig](https://github.com/ziglang/zig)@[a31b449b55...](https://github.com/ziglang/zig/commit/a31b449b55c32eba1cb61a48753a6fc98696c98f)
#### Wednesday 2022-08-24 04:38:02 by Andrew Kelley

make LLVM and Clang emit DWARF 4 instead of 5

This reverts 6d679eb2bcbe76e389c02e0bb4d4c4feb2847783 and additionally
changes the command line parameters passed to Clang to match.

Clang 14 defaults to DWARFv5 which is an interesting choice. v5 has been
out for 5 years and yet Valgrind does not support it, and apparently
neither does either GDB or LLD, I haven't determined which, but I wasn't
able to use GDB to debug my LLVM-emitted dwarf 5 zig code that was linked
with LLD.

A couple years ago when I was working on the self-hosted ELF linker, I
emitted DWARFv5 but then downgraded to v4 when I realized that third
party tools were stuck in the past. Years later, they still are.

Hopefully, Clang 14's bold move will inspire third party tools to get
their shit together, however, in the meantime, everything's broken, so
we're passing `-gdwarf-4` to clang and instructing LLVM to emit DWARFv4.

Note that Zig's std.debug code *does* support DWARFv5 already as of a
previous commit that I made today.

---
## [juju/juju](https://github.com/juju/juju)@[19b18fec85...](https://github.com/juju/juju/commit/19b18fec85754efe2d8cae9e452ae3de831ff154)
#### Wednesday 2022-08-24 05:46:38 by Juju bot

Merge pull request #14511 from benhoyt/openstack-auth-error

https://github.com/juju/juju/pull/14511

This slightly improves the error message during OpenStack authentication when the code is trying to authenticate against a v3 server but the credentials look like v2 credentials. Previously the code would fall back to using a v2 client and the next call would give a 404 error, now it doesn't fall back when it knows the server is v3 ("v3" in the URL) so we get a 401 authentication error immediately.

## Checklist

- [x] Code style: imports ordered, good names, simple structure, etc
- [x] Comments saying why design decisions were made
- [x] Go unit tests, with comments saying what you're testing
- [ ] ~[Integration tests](https://github.com/juju/juju/tree/develop/tests), with comments saying what you're testing~
- [x] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages

## QA steps

* Set up an OpenStack cluster for testing (I used the single VM [devstack](https://docs.openstack.org/devstack/yoga/guides/single-vm.html) system using Multipass). This took at least 45 minutes to initialize the VM, set up all the packages, etc.
* Set up a Juju cloud using `juju add-cloud` with the novarc file method described [here](https://juju.is/docs/olm/openstack). The novarc file can be downloaded from the cluster's Dashboard, using the "Download OpenStack RC file" button under API Access.
* Add a credential, but make the password incorrect so auth is going to fail (I changed "password" to "passwordx").
* Try to `juju bootstrap openstack`.

However, here's where I started to run into trouble. First I got this error:

```
$ juju bootstrap openstack
ERROR cannot create a client: version part of identity url http://10.244.209.44/identity not valid
```

Fix is to update Juju's `clouds.yaml` regions endpoint from "endpoint: http://10.244.209.44/identity" to "endpoint: http://10.244.209.44/identity/v3". Not sure why this isn't included in the novarc correctly, as it's definitely a v3 endpoint.

The next error I got was

```
ERROR auth options fetching failed
caused by: request available auth options: request (http://10.244.209.44/) returned unexpected status: 200; error info: 

... lots of HTML output ...
```

This is because goose's client.baseURL is not set (""). It doesn't look like it can be set via config due to the use of NewClient, which is what's being used here. So you have to hack-fix goose [here](https://github.com/go-goose/goose/blob/e7e49e456da1f62c629a2fc6944fe96b2af94368/client/client.go#L701) (and use replace for goose in `go.mod`):

```diff
$ git diff
diff --git a/client/client.go b/client/client.go
index 2b10185..e812d3e 100644
--- a/client/client.go
+++ b/client/client.go
@@ -698,7 +698,7 @@ func (c *authenticatingClient) IdentityAuthOptions() (identity.AuthOptions, erro
 return identity.AuthOptions{}, gooseerrors.Newf(err, "trying to determine auth information url")
 }
 // this cannot fail.
- authInfoPath, _ := url.Parse("/")
+ authInfoPath, _ := url.Parse("/identity") // TODO
 baseURL = parsedURL.ResolveReference(authInfoPath).String()
 }
 authOptions, err := identity.FetchAuthOptions(baseURL, c.httpClient, c.logger)
```

I don't understand how this ever worked. I'm guessing that most OpenStack installs have a root of "/" (with the domain being `identity.foo.bar` or whatever), whereas with devstack you're using an IP address with a base URL of "/identity". I think Goose needs fixing here, but I've spent enough time on this now and don't really know what the correct fix is anyway.

With those two fixes in place, now when you `juju bootstrap openstack` you'll actually see the issue at hand.

```
# BEFORE fix
$ juju bootstrap openstack
ERROR authentication failed.: authentication failed
caused by: requesting token failed
caused by: Resource at http://10.244.209.44/identity/v3/tokens not found
caused by: request (http://10.244.209.44/identity/v3/tokens) returned unexpected status: 404; error info: <!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>

# AFTER fix
$ juju bootstrap openstack
ERROR authentication failed
caused by: requesting token: Unauthorised URL http://10.244.209.44/identity/v3/auth/tokens
caused by: request (http://10.244.209.44/identity/v3/auth/tokens) returned unexpected status: 401; error info: Failed: 401 error: The request you have made requires authentication.
```

## Bug reference

https://bugs.launchpad.net/juju/+bug/1980474

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[f8ec12e778...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/f8ec12e778b6499f24085d99a719aa470710be18)
#### Wednesday 2022-08-24 06:51:24 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [Austerror/otservbr-global-1](https://github.com/Austerror/otservbr-global-1)@[fbd70d116c...](https://github.com/Austerror/otservbr-global-1/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Wednesday 2022-08-24 07:47:06 by rigis1

Fixes and add blood brothers quest till mission 4 (#753)

Fix:
• electric sparks
• baking
• filling fluids container
• the hunt for the sea serpent quest

Add:
• questlog entry for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• storages for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• keywords for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• condition to harlow travel to vengoth
• holy water to henricus shop
• food for blood brothers quest
• spawn npc ortheus and jack springer, monster gaffir
• npc jack springer 
• ugly monster loot
• events to gaffir and ugly monster
• ice cracking
• basic events for bosses Sir Nictros and Sir Baeloc
• basic spawn boss for levers
• access to falcon bastion

---
## [pprmint/pprmint.art-Next](https://github.com/pprmint/pprmint.art-Next)@[a97d57b56a...](https://github.com/pprmint/pprmint.art-Next/commit/a97d57b56ab0787325ccdb36fc3ba621284d9422)
#### Wednesday 2022-08-24 08:33:58 by pprmint

By our goddess and saviour Hatsune Miku, how the fuck are the PCs we use at work so fucking slow holy shit which fucker approved this pile of e-waste.

---
## [GabrielaKoleva/Conditional-Statements-Advance-SoftUni](https://github.com/GabrielaKoleva/Conditional-Statements-Advance-SoftUni)@[dc238eeb4f...](https://github.com/GabrielaKoleva/Conditional-Statements-Advance-SoftUni/commit/dc238eeb4f4cf69a1a6a320314f184c93b20c4ce)
#### Wednesday 2022-08-24 09:01:18 by GabrielaKoleva

Create Summer Outfit

It's summer with very changeable weather and Victor needs your help. Write a program that, based on the time and degrees, recommends what clothes Victor should wear. Your friend has different plans for each stage of the day, which also require different looks, you can see them from the table.

Exactly two lines are read from the console:
• Degrees - an integer in the range [10…42]
• Text, time of day - with options - "Morning", "Afternoon", "Evening"

10 <= degrees <= 18
Morning                   Outfit = Sweatshirt      Shoes = Sneakers
Afternoon                Outfit = Shirt               Shoes = Moccasins
Evening                    Outfit = Shirt               Shoes = Moccasins

18 < degrees <= 24
Morning                   Outfit = Shirt               Shoes = Moccasins
Afternoon                Outfit = T-Shirt            Shoes = Sandals
Evening                    Outfit = Shirt               Shoes = Moccasins

degrees >= 25
Morning                   Outfit = T-Shirt             Shoes = Sandals
Afternoon                Outfit = Swim Suit         Shoes = Barefoot
Evening                    Outfit = Shirt                 Shoes = Moccasins

To print a single line to the console: "It's {degrees} degrees, get {clothes} and {shoes}."

---
## [rporres/sretoolbox](https://github.com/rporres/sretoolbox)@[c273cfd768...](https://github.com/rporres/sretoolbox/commit/c273cfd76837512eb44abfde5a1a46dac355a3e4)
#### Wednesday 2022-08-24 09:18:30 by Rafa Porres Molina

Content-Type based equality for version 2 images

The Docker Image Manifest V 2, Schema 2 spec states that header should
be used to determine the kind of image that it is returned, a
multi-architecture image (aka "fat" image) that returns a manifest list
or a simple image (returns a manifest). The OCI spec is not as clear but
it also mentions the header as the way to distinguish images since
`mediaType` is not mandatory.

This patch adds support for comparations via the `Content-Type` header
for both Docker and OCI images.

Tests have been added for all the equality cases. Manifests have been
taken from real-life examples when available or from the spec examples.
A new dependency (`requests-mock`) has been added as it wasn't possible
to mock `requests.get` directly using MagicMock as it is a default in
the `_request_get` method signature. Anyway, writing tests using
`requests-mock` has proven to be a very pleasant experience.

`Pipenv.lock has been regenerated due to the addition of the new
dependency.

Signed-off-by: Rafa Porres Molina <rporresm@redhat.com>

---
## [queercpu/script](https://github.com/queercpu/script)@[260852cb42...](https://github.com/queercpu/script/commit/260852cb427e02b7bdbdee35621a6e639660c1e0)
#### Wednesday 2022-08-24 10:17:52 by home.cpu

did alot of clean up on veronica,and wrote in more shit, made it till moment veronica enters the hotel room to meet chess, she was just fuming about how to make her panties drop with food... then its a cut back to twigs. had doubts / insecurities while writing today but nothing too serious, i end up calming myself down, i did 3d work today too, the dvd8 model, i learned about interpolation with textures, using closest over linear to get a more gritty old game render with blender. played around with it on coconuts etc, it was exciting to unlock that... but it doesn't look automatically good on everything else, only some things look good with that grittiness.  i made the quaternion heart as well, with a glass shattering animation sketched out in renpy with white flashes.  there are random notes laying around but im a little delierious. i also played a ton of piano / church music and exported a few cuts casino gracious cookie. churchchapel...wanna put glass shatter sound but gnna do it later i think.

---
## [wangyum/spark](https://github.com/wangyum/spark)@[c4c623a3a8...](https://github.com/wangyum/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Wednesday 2022-08-24 10:33:04 by Hyukjin Kwon

[SPARK-39869][SQL][TESTS] Fix flaky hive - slow tests because of out-of-memory

### What changes were proposed in this pull request?

This PR adds some manual `System.gc`. I know enough that this doesn't guarantee the garbage collection and sounds somewhat funny but it works in my experience so far, and I did such hack in some places before.

### Why are the changes needed?

To deflake the tests.

### Does this PR introduce _any_ user-facing change?

No, dev and test-only.

### How was this patch tested?

CI in this PR should test it out.

Closes #37291 from HyukjinKwon/SPARK-39869.

Authored-by: Hyukjin Kwon <gurwls223@apache.org>
Signed-off-by: Hyukjin Kwon <gurwls223@apache.org>

---
## [tauri-apps/cargo-mobile](https://github.com/tauri-apps/cargo-mobile)@[420f6723df...](https://github.com/tauri-apps/cargo-mobile/commit/420f6723df1d74374f7df6f0604fc25281c2174c)
#### Wednesday 2022-08-24 11:29:09 by Amr Bashir

feat: enhance wry android template (#32)

* feat: enhance wry android template

* fuck you UNC paths

* remove ios config

* revery jvm args

---
## [rjusto/git](https://github.com/rjusto/git)@[5beca49a0b...](https://github.com/rjusto/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Wednesday 2022-08-24 11:47:08 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [aslenofarid/kernel_asus_sdm660](https://github.com/aslenofarid/kernel_asus_sdm660)@[92fc45936b...](https://github.com/aslenofarid/kernel_asus_sdm660/commit/92fc45936b5f9d92f01eadcbb7b9bbec95a74597)
#### Wednesday 2022-08-24 12:15:58 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: Albert I <kras@raphielgang.org>

---
## [GabrielaKoleva/Conditional-Statements-Advance-SoftUni](https://github.com/GabrielaKoleva/Conditional-Statements-Advance-SoftUni)@[acd1086b60...](https://github.com/GabrielaKoleva/Conditional-Statements-Advance-SoftUni/commit/acd1086b607c5352d95e28583e3da81ca8c0fd3b)
#### Wednesday 2022-08-24 12:21:35 by GabrielaKoleva

Create Fishing Boat

Tony and friends loved to go fishing, they are so passionate about fishing that they decided to go fishing by boat. The price for renting the vessel depends on the season and the number of fishermen.

The price depends on the season:
• The price for renting the ship in the spring is BGN 3,000.
• The price for renting the ship in summer and autumn is BGN 4,200.
• The price for renting the ship in winter is BGN 2,600.

Depending on their number, the group benefits from a discount:
• If the group is up to 6 people inclusive - 10% discount.
• If the group is from 7 to 11 people inclusive - 15% discount.
• If the group is 12 or more - 25% discount.

Fishermen enjoy an additional 5% discount if they are an even number, unless it is autumn - then they do not have an additional discount.

Write a program to calculate whether the fishermen will collect enough money.

Login
Exactly three lines are read from the console.
• Group budget – an integer in the range [1…8000]
• Season - text: "Spring", "Summer", "Autumn", "Winter"
• Number of fishermen – an integer in the range [4…18]

Exit
To print one line to the console:
• If the budget is sufficient:
"Yes! You have {the remaining money} leva left."
• If the budget IS NOT sufficient:
"Not enough money! You need {amount that does not reach} leva."

Amounts must be formatted to two decimal places.

---
## [DEFRA/water-abstraction-service](https://github.com/DEFRA/water-abstraction-service)@[2d323eb53e...](https://github.com/DEFRA/water-abstraction-service/commit/2d323eb53ec13b6483b95f8dc3c3cfcede5a8ef3)
#### Wednesday 2022-08-24 12:36:33 by Alan Cruikshanks

Set up background tasks module (#1784)

https://eaflood.atlassian.net/browse/WATER-3745

> We have started this change again because [PR #1766](https://github.com/DEFRA/water-abstraction-service/pull/1766) had gone so far done a possible path that it made merging/rebasing overly complex. Simpler to start again!

We are separating out our background BullMQ tasks so that they run on a background instance. The foreground (existing instance) can then just focus on handling requests from the UI, including adding the initial jobs that kick off background processes.

We had initially looked at splitting out `QueueManager` into a `WorkerManager` (see [PR #1766](https://github.com/DEFRA/water-abstraction-service/pull/1766)). But we then found that the background instance also needs to know about queues. This is because a number of the `onComplete()` worker handlers add new jobs to queues based on the results of the main worker handler.

So, we moved a number of the changes we were making into separate PR's, which focused on refactoring the QueueManager ready to allow us to make the changes we need to support a background instance.

This PR is those changes.

** Notes

- Use fork mode for service-background
  For a standard web-app or API you would typically run it using [cluster mode](https://pm2.keymetrics.io/docs/usage/cluster-mode/). This is some cleverness built into Node.js which allows multiple processes to be spawned that still share the same ports. How many is determined by the number of CPU's available. It's a codeless way to scale an app based on the resources available. To that pm2 will also act as a load balancer between the processes.

  By default pm2 runs apps using fork mode (would love to link to a page but there ain't none!) This is the equivalent of what you do when running it locally. If you wanted to start a second instance you'd have to run it on a different port.

  The reason for the change is because we are not using the background instance as a web app or API. Instead, we're using it to run processes in the background that should only be run once. What is happening in production at the moment is

  - normal service starts up using pm2 with config set to cluster mode and `max` instances. Assume pm2 finds 2 CPU's so creates 2 instances of the app
  - each app will instantiate BullMQ workers as part of start up (it will also try to register the queues in parallel!) Current count is we have 13 of them, so that's 26 additional processes started behind the scenes on top of our 2 apps
  - a job is added to a queue and both workers created for the queue fight to process it
  - then double all this because we have 2 EC2 instances running in AWS

  A background job is only expected to be run once so typically you'll designate one of your EC2 instances to handle them. However, we were treating our background service like a scaling web-app which makes controlling and debugging much more complicated.

  We've still to think about how we handle a worker per EC2 instance (it may be fine). But on an instance there should just be 1 background service running.

- Wrap worker forking in service check
  What do you know!? There is _another_ way we create blasted workers/jobs in this service 😫

  In this case we are forking a child process and doing all the work in there. The BullMQ job triggers the work in the child process so it looks like the worker is done. The work in this case is like syncing WRLS invoices with all the transaction detail in the CM is taking place. The problem was the code was creating the fork as soon as the file was required. As this is happening in order to pass it to the QueueManager to register the queue, it meant the foreground service was spawning sub processes that would never be used. After reading the PM2 docs, the app name set in ecosystem.config.json is made available as an env var to the running apps. So, we use that to check if we are running in the foreground or background instance. Then, only if we are on the background instance do we create the fork and spawn the child process.

  Note - This forking was supposedly done as a performance optimisation. We don't believe it helps with performance (in fact it possibly degrades it) but it would solve a worker taking to long and becoming susceptible to loosing its job lock and therefore failing. We really need to remove this unnecessary complexity.

- Refactor job files
  We make a few small changes to `process-charge-version-year.js` and `update-invoices.js`

  - Add `'use strict'` to the top of `update-invoices`
  - Destructure `fork` from `child_process`
  - Sort out `require()` statements (vendor, project then constants)
  - Change the `exports` section to a standard `module.exports`

- Increase V8's old memory section via pm2 config
  `--max-old-space-size` is an argument you can set when calling node that it will pass on to tje underlying V8 engine. From the node documents

  > Sets the max memory size of V8's old memory section. As memory consumption approaches the limit, V8 will spend more time on garbage collection in an effort to free unused memory.
  >
  > On a machine with 2 GiB of memory, consider setting this to 1536 (1.5 GiB) to leave some memory for other uses and avoid swapping.
  <https://nodejs.org/api/cli.html#useful-v8-options>

  The default is 2GB which can be seen by checking `heap_size_limit` after doing the following

  ```
  node

  > v8.getHeapStatistics()
  {
    ....
    heap_size_limit: 2197815296,
  }
  ```
  <https://stackoverflow.com/a/63495296/6117745>

  The essence of this change is to improve performance. The background instance is where all our work is done and where we often have to hold a large amount of data in memory. The theory is the more memory you've got to hold stuff, the less the garbage collector has to be called in to ensure you don't run out of memory. We're only setting this when running in `production` mode, which will only be when running in our AWS environments.

- Only create worker and scheduler in background
  We coming to the end of our changes to support splitting the work of the service project. Both foreground and background need to know about the queues. But only the background instance needs to create the instances of Worker and QueueScheduler to process the queues. So, we add a check (similar to what we did with the jobs that are using `fork()`) into the `QueueManager` to only create them if we are the background instance.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[ce25fdf1bd...](https://github.com/pytorch/pytorch/commit/ce25fdf1bdb4b21da48178aa6729a4e4f917d04b)
#### Wednesday 2022-08-24 13:18:15 by Andrew Gu

Update base for Update on "[FSDP] Generalize prefetching; lower unshard/reshard to handle"


### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`. 

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any extra overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between. If we remove the mixed precision stream, the low precision shard is allocated and copied to in the all-gather stream (including the non-blocking CPU -> GPU copy if using CPU offloading). 

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. IIUC, the overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.


### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)
  
  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)
  
  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>



[ghstack-poisoned]

---
## [AkashicBearer/DokiDoki-Recode](https://github.com/AkashicBearer/DokiDoki-Recode)@[586ace52ce...](https://github.com/AkashicBearer/DokiDoki-Recode/commit/586ace52ce3d633d679e9f656524cc4b12ee16f7)
#### Wednesday 2022-08-24 13:24:31 by Akashic Bearer

Roleplay Commands added:
Alarm ✅
AMazing ✅
Blush ✅
clap ✅
coffee ✅
shrug ✅
sip ✅
sleepy ✅
smoke ✅
sit ✅
confused ✅
cry ✅
dance ✅
dodge ✅
Happy ✅
Hide ✅
facedesk ✅
facepalm ✅
pout ✅
run ✅
triggered ✅
money ✅
nom ✅
nosebleed ✅
ok ✅
party ✅
peek ✅
puke ✅
Baka ✅
Bite ✅
Boop ✅
Cuddle ✅
Cute ✅
Fight ✅
Highfive ✅
Hug ✅
Kill ✅
Kiss ✅
laugh ✅
lick ✅
stare ✅
tickle ✅
winkc
Blyat ✅
fbi ✅
lonely ✅
love ✅
mad ✅
pat ✅
poke ✅
punch ✅
slap ✅
smug ✅
salute ✅
scared ✅
shocked ✅
shoot ✅
wave ✅
wasted ✅
yeet ✅

---
## [jottofar/cluster-version-operator](https://github.com/jottofar/cluster-version-operator)@[9222fa9a66...](https://github.com/jottofar/cluster-version-operator/commit/9222fa9a6616b58a8056c780b9a6252e82a26e37)
#### Wednesday 2022-08-24 13:32:44 by W. Trevor King

pkg/cvo/sync_worker: Trigger new sync round on ClusterOperator versions[name=operator] changes

David and Stephen identified an uneccessary delay [1]:

* 9:42:00, CVO gives up on Kube API server ClusterOperator [2]
* 9:42:47, Kube API server operator achieves 4.12 [3]
* 9:46:22, after a cool-off sleep, the CVO starts in on a new manifest graph-walk attempt [4]
* 9:46:34, CVO notices that the Kube API server ClusterOperator is happy [5]

The 3+ minute delay from 9:42:47 to 9:46:22 is not helpful, and we've
probably had delays like this since my old e02d1489a5
(pkg/cvo/internal/operatorstatus: Replace wait-for with single-shot
"is it alive now?", 2021-05-13, #560), which landed in 4.6.

This commit introduces a "ClusterOperator bumped
versions[name=operator]" trigger to break out of the cool-off sleep.

There's plenty of room to be more precise here.  For example, you
could currently have a versions[name=operator] bump during the sync
loop that the CVO did notice, and that queued notification will break
from the sleep and trigger a possible useless reconciliation round
while we wait on some other resource.  You could drain the
notification queue before the sleep to avoid that, but you wouldn't
want to drain new-work notifications, and I haven't done the work
required to be able to split those apart.

I'm only looking at ClusterOperator at the moment, because of the many
types the CVO manages, ClusterOperator is the one we most frequently
wait on, as large cluster components take their time updating.  It's
possible but less likely that we'd want similar triggers for
additional types in the future (Deployment, etc.), if/when those types
develop more elaborate "is the in-cluster resource sufficient happy?"
checks.

The panic-backed type casting in clusterOperatorInterfaceVersionOrDie
also feel like a hack, but I wasn't able to find a cleaner way to get
at the structured information I want.  Improvements welcome :)

[1]: https://bugzilla.redhat.com/show_bug.cgi?id=2117033#c1
[2]: From Loki: E0808 09:42:00.022500       1 task.go:117] error running apply for clusteroperator "kube-apiserver" (107 of 806): Cluster operator kube-apiserver is updating versions
[3]: $ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/origin-ci-test/logs/periodic-ci-openshift-release-master-ci-4.12-upgrade-from-stable-4.11-e2e-gcp-sdn-upgrade/1556564581915037696/artifacts/e2e-gcp-sdn-upgrade/openshift-e2e-test/build-log.txt | grep 'clusteroperator/kube-apiserver versions:'
     Aug 08 09:33:48.603 I clusteroperator/kube-apiserver versions: raw-internal 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
     Aug 08 09:42:47.917 I clusteroperator/kube-apiserver versions: operator 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
[4]: From Loki: I0808 09:46:22.998344       1 sync_worker.go:850] apply: 4.12.0-0.ci-2022-08-07-192220 on generation 3 in state Updating at attempt 5
[5]: From Loki: I0808 09:46:34.556374       1 sync_worker.go:973] Done syncing for clusteroperator "kube-apiserver" (107 of 806)

---
## [TheCanoePirates/TCPStation](https://github.com/TheCanoePirates/TCPStation)@[22d57da140...](https://github.com/TheCanoePirates/TCPStation/commit/22d57da14091d9bf7d8e1dcb7a5104b3f89eeec5)
#### Wednesday 2022-08-24 14:12:06 by LemonInTheDark

Readds Alien Vore (#68312)

* Readds Alien Vore

Aliens can now eat people again. Behavior was removed by #43991 (b6c41e3b328078b72bd0f88fd46719aa99c55be2)
because nasku thought it was weird, and the code was really bad.

I think it's funny, and I've made the code not trashtier.

Basically, an alien can agressive grab any living mob. If they stay next
to the mob, facing them for 13 seconds, they will "eat" the mob,
IE:insert them into a list on their custom stomach.

The xeno can then hit an action button to spit out the mob, alongside
some acid.

If the mob is alive enough to pull out a weapon inside the xeno/has one
on it, they can attack the xeno from inside, dealing damage to the
creature and its stomach. If the stomach drops below a threshold, the
mob gibs the xeno and escapes.

I've done my best to steer things away from horny and into gross, though
I'm aware you fucks do your best to blur that line.

Anyway something something balance change something something lets xenos
abduct people more easily, I'm mostly doing this cause I think it has
soul.

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[4c8cfb57aa...](https://github.com/pytorch/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Wednesday 2022-08-24 14:24:18 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [Dazz1994/solid-engine](https://github.com/Dazz1994/solid-engine)@[2711a70565...](https://github.com/Dazz1994/solid-engine/commit/2711a7056550d0627ef32ac9b146f7edf6c088ad)
#### Wednesday 2022-08-24 14:47:43 by Dazz1994

help

I haven't got a clue what im doing with this but I need to get into my cheating girlfriends phone

---
## [Grim-Jokes/interview-accountapi](https://github.com/Grim-Jokes/interview-accountapi)@[a5f5c20f77...](https://github.com/Grim-Jokes/interview-accountapi/commit/a5f5c20f7754c9a7dc92398e61f3d5db5c14fb4b)
#### Wednesday 2022-08-24 15:20:18 by Daniel Szekely

create Client constructor function

First iteration of creating the client isntance. Unfortunately
is is a more OOP approach than what is idiomataic to Go.

Inspiration came form AWS SDK, Typescript and DDD (layerered
architecture) experience.

The idea is that I want to write some unit tests without requring a
a database + webserver to be running.

By following the black  box testing mindset:

`NewClient().FetchAccount()` tells the developer nothing in terms of
just how the data is retrieved. It could be the http/lib, it could
be some other 3rd party library.

This also means, that FetchAccount(), for example, is not unit testable
as we're forced to communicate with external services.

By having to mock out http.Get, we break blackbox rule by having the
test know what underlying libraries are being used, leading to brittle
tests in the case of migrations to other libraries.

By dependency injecting the http.Get (or a wrapper function, really)
we give control to the callers in terms how the Get operates.
The tests gain control by passing in a mock function returning the
data exactly as needed.

So if we move from http.Get to something else, the tests can remain
largely unchanged.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e4dc9ce3f1...](https://github.com/mrakgr/The-Spiral-Language/commit/e4dc9ce3f11241ec51275d06a5cebeeb137d61fb)
#### Wednesday 2022-08-24 16:05:35 by Marko Grdinić

"9:50am. One who does not aspire to greatness is not a living being, but at the same time, I can recognize that being a commoner has its own strength. Having a regular job, or writing as I am now, there is something to it.

I've gone to bed too late last night. I was playing Pathfinder, but it is pretty boring. I made the mistake of installing the craft magic items mod. Without it, I'd have so much useless gold, but with it I've pretty much broken the game.

9:55am. I'd be better off playing Dark Souls 2 or Lona RPG, than spending so much time being a janitor in Pathfinder. I wish the game was balanced around Respec and Craft Items mods. The game was a lot more fun when I didn't know how to play it and had to web and grease everything to stop the enemies from slaughtering the party.

A similar thing ruined the Rance Quest game for me as well. At the beginning it was fun and challenging, but later the battles devolved to just sweeping the field with mage AOE attacks.

10am. At any rate, I've gotten the 100 views on a single fiction achievement on Royal Road. For some reason the latest chapter still only has 3 views.

I won't worry about it unless I am done with Heaven's Key and nobody is reading the thing. I've been hoping to get some comments, plenty of stories have them, but I never seem to get people wanting to talk to me about the story. It is quite sad.

10:05am. Let me chill a little, I am groggy. After that I am going to focus on writing. I want to be done with chapter 6, so I can get to the more interesting parts after Euclid starts modifying himself for real.

This is really the evil of staying up late. I am sacrificing my good time just to play useless games.

10:10am. Let me read the Urasekai Picnic chapter that came out yesterday.

10:25am. Satanophani raws as well. I am still groggy. I swear I'll go to bed on proper time tonight. I am going to really focus on writing. Heaven's Key has a while to go. I want to write it for a few months to get a sense where I stand.

11am. I need to get started. I am still groggy, but it is fine. Forget writing for other people. I should write to satisfy this deep yearning in me. This loneliness that seeks the Singularity. Gettign a job would not fed that urge in me.

11:10am. Actually, let me take a nap. I was going to write more stuff from Euclid's point of view, but now I think it is time to pivot.

11:30am. I want to intensify the conflict in a smooth manner.

12:05pm. I've been getting some inspiration. I meant to just start writing, but I realized that going with Euclid's POV would be boring. I think it should be possible to make chapter 6 a lot better.

I titled it Inspired Desire, but I think I'll change it to Lit Fuse. The Inspired Desire will come in the next chapter.

12:20pm. Right now I am reading the /crpg/ thread on /vg/. Let me have breakfast.

1:10pm. Done with breakfast. Should I try some writing?

I am currently at 94 pages, so it is high time to spice things up. It is good if I bring in other people's perspective at this point.

$$$

(Heaven's Key, Computer shop)

Vividly, the image before me crystalized into my eyes. In front of me, past the glass pane of the shop were cores! Brain cores! Shining, gleaming, brain cores!

Excited, I ran quickly into the shop, not even realizing how strange it was that while all the other shops were locked, this one didn't even have a lock on the door. The door just swung open for me automatically.

I grabbed a brain core off the shelf, using a mental command I tried connecting to it, and found that it worked. It worked just like the real thing. The brain conversion options were already there, but I could not use it as my brain was already a core, even in the simulated world. Using the core I grabbed off the shelf, I could see a diagram of my own brain. My thoughts turbulent, I realized that all the NPCs here could in fact enter the self-improvement loop and become the Inspired themselves. I thought I had huge advantages, but that wasn't the case.

If I had something special, it is not talent or intelligence, but desire.

I wanted power, but as it happens, I was the only one in this world who was filling to pay the price for it.

I thought it might as well be me in Mickey's place. If nobody gave me a chance, I would just be another ghost in the garden, but that is not the case. The chance has always been there, but Mickey never took it. I understand it now.

I am special, and it is my desire that makes me so. Whoever made this world saw to it that justice existed in it.

It is what I would have done. A universe where all of those with desire can rise is a just one. It is enough to give a chance to other people, it is not anyone's responsibility to make them want to take it.

I clutch the core to my chest and then pocket it, intent on bringing it out of here. My mind that was wavering becomes steely and I decide.

I won't take it easy on the NPCs, and I won't regret the battles that are to come.

I swear it on my desire, that I will rise. I will escape this city and into the real world beyond.

(Heaven's Key, Streets)

I march out of the shop, intent on my destination. At this point due to all the aimless wandering, I've become completely lost, but it should not be hard to find my way back to the inn. I scale one of the larger apartment buildings, and from the high vantage points of the external corridor, in the distance spot the rollercoaster I rode with Lily. Establishing the direction, I get back to the streets and head towards it. It has been a couple of hours since I went out into the city, and in a few more I am guessing the morning should arrive. I remember that cores exist in this world, and on mental command I try accessing, not the real world core which houses my actual self, but the one in the game. A sense connects to it, and I bring up the time.

4:38am.

I have time. If it becomes known that I slipped out of the inn during the night, Lily might get suspicious of me, I do not want her to think that I am anything more than an easy mark. I want her to show me around more casinos. Right now she is my only connection here.

It won't take me more than an hour and a half to get back to the perimeter, but then I'll have to spend time figuring out where the inn was.

I get an idea, and try accessing the core I pocketed from the computer shop. I tried searching for a map application, and to my pleasant surprise I found it. The game core, I'll call it that as opposed to the main core I am on, has a tracking ability. As long as I make use of this, I'll never get lost again in the future.

I am feeling pretty lucky right now. I mean, I just found some guy in a park to talk to, as well as a computer shop. It is not like finding some priceless treasure by accident, but everyone in this world is out to get me, so finding my footing, and so quickly, is a large gain.

Block by block, I make my way to the perimeter. In the distance, I can see the sun's rays starting to break out.

(Heaven's Key, Perimeter)

I finally got back to the familiar area where I first came to the city. Not far from me, I can see the restaurant where I met Lily. I check the time.

6:10am.

It won't be long before people start waking up, so I have to get back. I put a marker on the core's map to indicate where I currently am and scroll it, trying to find the nearest resting places. It seems that map is somewhat out of date. Some of the buildings, in particular the circus tents, which I can see around me do not seem to be on it. Neither do the new venues built in the middle of intersections. Maybe the map on this core is how the city was originally?

I think about it for a moment. Yeah, that is most likely the case.

On impulse, I decide to just save here.

6:15am.

It would be best for me to try to retrace my steps by feeling rather than relying on the map. The inn should not be too far from where I am, but if I get lost, I can always reload to where I am and try again.

(Heaven's Key, Side of the inn)

My sense of direction does not seem too be bad. It took me quarter of an hour to find my way back to the inn. When I slipped out a couple of hours ago, it was through the window. I did that movie trick where I tied a couple of bed sheets together in knots and use them as a rope. My room was on the second floor, so it wasn't too high up, but not so low that I can just jump up to it. The bedsheet rope was still there where I left it, snaking out of the open window of my room.

I came up to it, and gave it a little tug as a test only to have the sheets unravel midway.

Right now, I am stuck with having a sheet in my hand, thinking what I should do. I observe the other end. Though it would be rough, if I did a little run and skid up the wall I could probably grab the other end and let myself in that way. I crumple the bedsheet in my hand into a ball and throw it into the room. Then I back up and prepare to take a run. Just before I start, I get an idea. I remember the night in the park, and how Mickey taught me to manifest food. And he gave me an idea to how to unlock doors using gel.

Instead of straining myself here, let me try making a ladder.

In my hand I manifest a chip and focus my will upon it.

Ladder, ladder, ladder...

I visualize it in my mind and project it into the space in front of me. I feel something trying to come out, but it is difficult.

My image is vague, but I persevere. Rather just any kind of ladder, I think of a wood ladder I once saw used. I remember and focus on the dry feel of food. I focus on how the bars are slotted into the two pillars. It starts to feel vivid. The wood ladder manifests in front of me, right where I wanted it to be. I realize that I feel a certain connection between the chip in my hand and the ladder. I don't probe it with my sense, instead I pocket it and grab the ladder bar and start climbing my way up. It is a short climb, and go through the window unimpeded. Then I grasp the chip in my hand, feel it out in my mind and cut the mental connection between it and the ladder.

I stick my head outside and confirm that the ladder has vanished. After that I drag the sheet that was sticking out back in and close the window.

6:40am. Safe!

As I check the time, outside, I can see people starting to go about their business and the city becoming lively. Maybe somebody spotted me climbing back into my room, but it does not matter. Since I was getting back in, they'll be able to deduce that I was playing hocky during the night rather than a burglar. There isn't a crime to report and I doubt whoever is Lily's boss has eyes everywhere. The pattern I've established won't be distrupted.

Sigh. I plop myself on the bed and take of my shoes.

I am quite tired right now. I went out at around 10:30pm and have been wandering all this time. 8 hours of physical activity is enough to make my feet quite sore. I rub my head against the smooth pillow.

I lie there for a while. I can feel myself getting drowsy.

This is not good. If I fall asleep here, Lily will come by to drag me out just when I am getting some shut eye.

With a mental command, I save and then exit the game.

(Helix Studio, Regent Suite)

I'll have to make some compromises. I can't avoid having my body be tired, but if I get a good night's rest in a different place, it will be reflected inside the game. 8 hours of exertion is not enough to allow me to fall asleep, so for the next 4 hours I might as well watch anime and play regular games.

Right now I am in the very luxurious living room of the cruise suite. I grab a cola from the fridge, pour myself a glass, and then start exploring the place. I find the bedroom. The bed is oversized as one would expect, but as if the designers knew what I like, they placed a desk with a PC there. I seat myself in my rightful place, and push on the power button on the black case. The monitor comes to life. The OS is of course prepared. The Internet speeds have gone way up since the Singularity started, so I don't find it hard to pirate a game and start it. Before I get into it, I close the shutters to darken the room. Only a couple of rays are getting in through the cracks, just the way I like it. I sit myself back on my battle seat and start clicking away.

Ironically, despite being legacy hardware simulated on the core, the computer is actually better than the one I have in real life. It has the latest AMD CPU and the Nvidia GPU, I've checked the setting.

Playing games inside a game, this really is the next level! I become immersed.

After a couple of hours of battling monsters, the fatigue really starts hitting me. I hit the sheets, and with a mental command change the environment settings to night time. What was once a clear day immediatelly shifts to a starry night. No longer bothered by the light, I shut my eyes and let the sleep come to me.

I don't have school tomorrow, so I do not have to worry about the time.

(Heaven's Key, Inn)

    In the dark days remember,
    Necromutation is Transcendence.
    - Loading Blurb

"If Lily, the guide who was with me before, comes by tell her I'll be at the casino we were yesterday." I told the proprietress of the inn and left.

(Heaven's Key, Streets)

It was early morning, and people were starting work. Mickey told me that new arrivals happened between 7 and 12pm, so people have to be ready to welcome them. Scamming them out of money was what powered the city's economy. I really gained a lot from Mickey explaining to me that we are all active illusions here. It is possible to infer a lot from that.

None of the citizens, as opposed to arrivals, had to work for food specifically. It is easy to understand why that is, they can just magic it out of thing air. Furthermore, there were no diseases here. Neither did people age, as they were holograms. Mickey didn't know how old the city was, but even so, that might be that there might be people here who are thousands and even tens of thousands of years old. As for getting injured, those would need a doctor, but not like in the real world. In this city, the doctor would be a hypnotist trying to convince the patient that his arm isn't broken, once that is accomplished it would become the truth. Furthermore, everyone in the city was an arrival from the world below, there were no children born of pregnancy.

Given all that, without having to worry about food, shelter or health, it is easy to see what the citizens would be obsessed about. Money.

This is a really good environment for me to learn to gamble.

As I made my way through the increasingly busy streets, I remarked this to myself. The golden rays of light illuminated the streets in their luster. The dawn had arrived.

(Heaven's Key, Raven's Eye Casino)

Raven's Eye Casino was not a large building, its defining trait was the cartoony logo of what appeared to be a raven's claw clutching some circles. Playing here is going to essentially be my job for a while, so I better get used to it. I intend to make use of the mind controlling program if I ever sense myself getting tired of it. Retreat is not an option. I have to win here. I need to find what my limits are. Only after I grasp what they are, can I start work on exceeding them.

I push the door open and make my way inside. I do not bother the receptionist and instead make my way straight to the game room. If Dale is there, I'll play against him and his group, otherwise anyone is fine.

I save here.

If the bet is something like a single chip, I'll let the result be as it is. In fact, losing minor games would be good, as it would make Dale and the guide more confident about raising the stakes against me. There isn't any doubt whether I'll win or not. This is a game, and I can't possibly lose it with the ability to save and load it. The real risk is me getting tired. Right now, everything is fun and exciting, but how will I feel after playing for a year? 10 years? A 100 years?

Imagine living like this for 10,000s of years, stuck on this brain core.

Before I uploaded myself, I could barely stand school for a single week. Will I really be able to do this?

(Heaven's Key, Game floor of the Raven's Eye Casino)

I look around for Dale's group, or anyone else for that matter, and it seems nobody is here. I idly wonder if there might be some people here, just in the duel space? Mickey called it the shadow realm. What do I do now? Awkward, I wander around and checking the seats, I realize that some of them have white dics on them, like tags. I think about what it might mean, and I realize that they might be there to indicate that the host is currently in a duel. If I try moving it...

I try picking the tag up, and my hand passes through it. This confirms my suspiction. Such an illusory thing is definitely this game's style.

I check the other tables in the room, but none of them have these dics on the seats. Since I am eager to start, I take an empty seat at the table with the discs. I wonder what would happen if I was sitting in the seat that was already occupied and the host returned from the duel? I might get telefragged, so it is best that I do not risk.

I spend some time like that, just waiting...

~~~

High above the surface of the world, golden cities floated, shinning their radiance on the world below. In the side of Earth that was lighted by the sun, there were like dots, but closer to the shadows where the vantage point was there were such islands of light.

"Euclid has started playing the game."

The scenery shifted to show him playing with a different group from yesterday. Compared to the adults around him, he was nothing more than a glasses wearing kid, focusing on the game in front with a smug look. He tries his best to keep a poker face when in the hand, but when he wins he smiles, and when he loses he feels the sting. He gets careless when he is out of the hand.

"He imagines this is how he would rise."

The scenery changed to him going into the casino in the morning, and then immediatelly the afternoon came and showed him stepping in the opposite direction.

"It is not like that."

A scene was shown of Euclid at the table going all-in. What was once a small stack, increased and increased.

Euclid was seated at the table facing his opponents. And behind him was an enormous pile of chips as tall as a mountain. Hundreds of thousands, millions!

"No!"

With red paint, that scene became crossed out.

"Euclid thinks he has time to play around, but a fuse has already been lit."

A scene of a lit fuse leading to stacks of explosives came about.

"Unbeknowst to him, the preparations to eradicate him are already being made..."

The scene changed to a building deeper in the city. Inside it, the guide Lily was seated at the desk of her office looking ready to begin he work for the day.

~~~

(Lily POV - Heaven's Key, Lily's Office)

After giving one last check to my attire, I put away the mirror and prepare to step out of my office, when I hear a knocking on the door.

"Enter." I call out.

"Hello." A young woman entered. She had a youthful face, and a her short hair was in twintails. This innocent look was out of tune with the military style camos she was wearing. "I have a report, boss."

I knew her well. Last night when that kid started avoiding payment and gave me that ridiculous story about throwing himself off the school building due to not wanting to work, I immediatelly became suspicious of him. I gave a task to some subordinates of mine to keep track of him so he does not slip away with the chips. I also requested the intelligence department to look into his background. Though it is rare that a citizen would pretend to be a newcomer, it is not impossible. Right now I am afraid that Euclid might be a weak expert trying to make use of me to fish.

If that is the case, then there is no point in me trying to act friendly. I'll just request an enforcer to take care of it and move on to the next assignment.

"I didn't expect to hear from you so early. Have you found anything suspicious about the newcomer?"

"I saw him slipping out his room last night. I followed him the entire time."

"Tch!" I clicked my tongue. "I knew it, I am the one getting tricked here. I'll have an enforcer take care of it." I seat myself back at my desk and lean in. I shake my head in disappointment. Requesting an enforcer would lower my evaluation, but it couldn't be helped.

"No, I don't think he is a hustler. Based on what I've observed he really is a newcomer."

"Really?" I look at her slightly incredulous. Lisa nods and seats herself opposite of me. "Let me show you some of the fotage. Typically when people are with others, they put on appearances, but when they are alone their true intentions come to light. I am quite sure he didn't notice me following him."

She picks out a core and sends some data over to me. We start going over it.

...

"After he left his room, take a look at how he is looking around at the streets as if everything is new to him."

...

"Hello, is anyone in there!?" I saw a video clip of Euclid yelling and slamming on the appartment doors. I looked at Ellie, as if seeking confirmation. She nodded.

"I have it all recorded. He spent two hours trying out various apartments to see if any were empty." Ellie explained. "He must have given the people inside some of them a big scare. Nothing good happens in this city when somebody visits in the dead of night."

...

I saw Euclid sating himself on the park fountain. Then followed the two-man night party between the ghost he had met and him.

"That is a lot, kid. You shouldn't have given me so much. Once you drop to 0, you'll die you know?" After a moment of thought, Mickey asks. "How much do you have left?"

A bit later I saw him giving 20 chips to the ghost for what was basic information my supervisor taught me on my first day here. I pause the clip.

"Ellie, send somebody to get those chips from the ghost." I told Ellie.

"Already did boss."

"Good job."

...

"Here is the part where it gets interesting. I only showed you some clips, but the kid spent 8 hours acting like a tourist that just got here."

The clip she showed was that of Euclid looking at an open window on the second floor of a building. He was outside the inn, and had to get back in through the window of his room. A bedsheet rope was leading into it from the outside. He gave a tug and it unraveled. Then have backed up, tossed the loose sheet inside and posed as if he wanted to make a run for the wall. Just as he was about to start, he changed his mind, calmly walked up to the room and manifested a ladder. The he went up it inside.

I knew what Ellie was trying to show to me. A citizen who was trying to commit a crime would have never acted like this. A citizen woudn't wander around doing stupid experiments. At the very least, he would not spend time thinking about how to get up to the second floor, but just bring up the ladder immediately.

Euclid really was a newcomer. Really?

"When he clipped out, I expected he would met up with his accomplice to hand over the chips he had gotten, but what happened instead is that he just toured the city. I was really surprised."

"And you say, it is not likely that he is pretending?" I asked for confirmation.

"Sometime people coming from below are familiar with using the brain core to manipulate their own emotions, but that kind of thing is limited and they tend to act robotically. Such people tend to be hard working, but that sort of mental hacking is not good at immitating curiosity and surprise."

For that reason, people tend to not use it here. I sometimes use it when things get tedious, but my supervisor taught me not to rely on it as it inhibits creativity too much.

"I'd bet on it that he really is a newcomer." Ellie continued.

I tapped my finger on the table, deep in thought.

"I guess I'll hold off on calling an enforcer then." I sighed. "Thank you, Ellie."

"You are welcome, boss!" She beamed.

"You can leave. I am going to have to make some arrangments for this."

"I've been up all night, I am going to bed." Ellie stretched. "Lisa is tracking him right now. Since Euclid has been up all night and must be tired, now is a good time to try to squeeze him dry."

"Okay."

"See you tonight." Ellie gave a little wave and opened the door before fading into invisibility and vanishing into thin air. There was only a slight visual distortion in the air as she closed the door behind her, and then I was alone in my office. I couldn't hear her footsteps when she moved like that.

I think for a bit and then I make a decision. Even though calling an enforcer would lower my evaluation, I have other things to do than trying to pull a thorn in my side. Even if Euclid might be a newcomer, if he is good at cards, then it is not worth it for me to try to gamble it out of him. Yesterday he's had a lot of luck so I am not sure what his skill is. I'll play with him today and if it looks like he is good, I'll abort and move on to the next mark.

I've been in this city for 50 years, so I am good at cards compared to those below. I should be able to tell whether he is a young online pro or a fool. Well, even if he is a former, he can't compare to the actual experts fighting life and death matches here. Since he wasn't chosen to become a citizen, he is going to lose either way in the end. It is a pity.

But that is how we in the city live.

Unless we want to disappear ourselves we have no choice, but to take from those who wander in.

$$$

3:50pm. Let me pause here. I've just finished a decent amount of text. I am low on inspiration right now.

What needs to happen next is Euclid demolishing Lily and her party using cheap saveloading tactics. After she gets pushed enough, then the enforcers come in and the death matches start. At that point Heaven's Key will begin for real. All the craziness of Simulacrum and the self improvement loop will be unlocked. It will be a based story.

Let me paste it into docs.

A bit over 9 pages. 4.3k words currently.

4:25pm. I need some time to recharge. Maybe that is it for today's session. I could have done more if I weren't so tired from gaming. From here on out, I am going to do it properly and not mess with staying up late.

Remember, it is better to end the work day early than to stay up late.

Tomorrow, I am going to see if I can finish the chapter. Right now let me just chill. It is only Wednesday, but it feels like it is Friday. I shouldn't pressure myself in times like these.

5:10pm. I am thinking. I really meant to have Euclid face a low level executor, but since he is savescumming his way through, that will immediatelly will result in him getting a top level adversary. He won't be able to beat that guy so easily.

5:20pm. Yeah, it is no wonder I can't write. Given the direction the story took, it changed the implications of Euclid's actions.

Should I have him be on the run and escape until the first Heaven's Key tournament?

5:35pm. At times like these, I am not sure if I am the one writing the story, or if the story is writing itself.

5:40pm. But I like it when it writes itself.

5:45pm. It is not like the bunch of scenes I had in my mind were a coherent story. They were really a few cool scenes. And a few cool scenes does not a story make.

5:50pm. Just what is my true worth as a writer? I'll know by the end of the year. Until then I will keep pushing myself. Though doing this is fun, I really need the money from the RR audience if I want to continue beyond Heaven's Key. I am not sure how long Heaven's Key will take me. I might be done by the end of next month for all I know. Or maybe it will continue for a lot longer.

All I know is that to give this a honest try.

Last time I was obsessed about the self improvement loop, but now I want to bring it all together into a coherent worldview.

That decision not to separate the machines and man to begin with was a great step forward in the AI friendliness debates, but even so that really does not counter any of the concerns of AI risk theorists. It just turns humans into risks, rather than alleviating any of their concerns.

But I've decided, the resolution to this is literally to have a god provide a wall of separation between the Inspired. Giving people the ability to program themselves is just, but so is letting them eat the universe. Letting the individuals grow is right.

What isn't right is letting the capable people suffer the fate of being devoured.

I've been wondering whether I should be getting a job and competing with Deepmind directly, but that is ridiculous. Also in the future when the Singularity starts, there are going to be kids in the situation of simply not having accumulated enough computational resources to compete. It is ridiculous to say to somebody such people that they could have won - yeah, if they won the lotery and used that to buy computers. It would happen in some timeline.

6pm. Without the Lord of Nightmares, every timeline would be Google winning. Kids like Euclid will be too unlikely to matter in the probability distribution of universes.

Ok, 300 pages. Right now the chapters that I've released are at 94. 300 should be enough to bootstrap what is on RR. After that I am going to leave some for my Patreon. If I could get a couple of people giving me 5$/month that would be a big difference from making 0$ a month. I can't compare myself to that absolute unit making 30k/month from writing. I am really wondering whether something like 30$ would be achievable for me.

I need to write a good story, but good, bad...what do I know of them? I only know what I like. That is what I'll do."

---
## [OlegGirko/dash](https://github.com/OlegGirko/dash)@[a00da7fb0e...](https://github.com/OlegGirko/dash/commit/a00da7fb0e8380dccd2922c3e12e8c36b1eeff8b)
#### Wednesday 2022-08-24 16:31:24 by Wladimir J. van der Laan

Merge #10271: Use std::thread::hardware_concurrency, instead of Boost, to determine available cores

937bf4335 Use std::thread::hardware_concurrency, instead of Boost, to determine available cores (fanquake)

Pull request description:

  Following discussion on IRC about replacing Boost usage for detecting available system cores, I've opened this to collect some benchmarks + further discussion.

  The current method for detecting available cores was introduced in #6361.

  Recap of the IRC chat:
  ```
  21:14:08 fanquake: Since we seem to be giving Boost removal a good shot for 0.15, does anyone have suggestions for replacing GetNumCores?
  21:14:26 fanquake: There is std::thread::hardware_concurrency(), but that seems to count virtual cores, which I don't think we want.
  21:14:51 BlueMatt: fanquake: I doubt we'll do boost removal for 0.15
  21:14:58 BlueMatt: shit like BOOST_FOREACH, sure
  21:15:07 BlueMatt: but all of boost? doubtful, there are still things we need
  21:16:36 fanquake: Yea sorry, not the whole lot, but we can remove a decent chunk. Just looking into what else needs to be done to replace some of the less involved Boost usage.
  21:16:43 BlueMatt: fair
  21:17:14 wumpus: yes, it makes sense to plan ahead a bit, without immediately doing it
  21:18:12 wumpus: right, don't count virtual cores, that used to be the case but it makes no sense for our usage
  21:19:15 wumpus: it'd create a swarm of threads overwhelming any machine with hyperthreading (+accompanying thread stack overhead), for script validation, and there was no gain at all for that
  21:20:03 sipa: BlueMatt: don't worry, there is no hurry
  21:59:10 morcos: wumpus: i don't think that is correct
  21:59:24 morcos: suppose you have 4 cores (8 virtual cores)
  21:59:24 wumpus: fanquake: indeed seems that std has no equivalent to physical_concurrency, on any standard. That's annoying as it is non-trivial to implement
  21:59:35 morcos: i think running par=8 (if it let you) would be notably faster
  21:59:59 morcos: jeremyrubin and i discussed this at length a while back... i think i commented about it on irc at the time
  22:00:21 wumpus: morcos: I think the conclusion at the time was that it made no difference, but sure would make sense to benchmark
  22:00:39 morcos: perhaps historical testing on the virtual vs actual cores was polluted by concurrency issues that have now improved
  22:00:47 wumpus: I think there are not more ALUs, so there is not really a point in having more threads
  22:01:40 wumpus: hyperthreads are basically just a stored register state right?
  22:02:23 sipa: wumpus: yes but it helps the scheduler
  22:02:27 wumpus: in which case the only speedup using "number of cores" threads would give you is, possibly, excluding other software from running on the cores on the same time
  22:02:37 morcos: well this is where i get out of my depth
  22:02:50 sipa: if one of the threads is waiting on a read from ram, the other can use the arithmetic unit for example
  22:02:54 morcos: wumpus: i'm pretty sure though that the speed up is considerably more than what you might expect from that
  22:02:59 wumpus: sipa: ok, I back down, I didn't want to argue this at all
  22:03:35 morcos: the reason i haven't tested it myself, is the machine i usually use has 16 cores... so not easy due to remaining concurrency issues to get much more speedup
  22:03:36 wumpus: I'm fine with restoring it to number of virtual threads if that's faster
  22:03:54 morcos: we should have somene with 4 cores (and ￼ actually test it though, i agree
  22:03:58 sipa: i would expect (but we should benchmark...) that if 8 scriot validation threads instead of 4 on a quadcore hyperthreading is not faster, it's due to lock contention
  22:04:20 morcos: sipa: yeah thats my point, i think lock contention isn't that bad with 8 now
  22:04:22 wumpus: on 64-bit systems the additional thread overhead wouldn't be important at least
  22:04:23 gmaxwell: I previously benchmarked, a long time ago, it was faster.
  22:04:33 gmaxwell: (to use the HT core count)
  22:04:44 wumpus: why was this changed at all then?
  22:04:47 wumpus: I'm confused
  22:05:04 sipa: good question!
  22:05:06 gmaxwell: I had no idea we changed it.
  22:05:25 wumpus: sigh ￼
  22:05:54 gmaxwell: What PR changed it?
  22:06:51 gmaxwell: In any case, on 32-bit it's probably a good tradeoff... the extra ram overhead is worth avoiding.
  22:07:22 wumpus: https://github.com/bitcoin/bitcoin/pull/6361
  22:07:28 gmaxwell: PR 6461 btw.
  22:07:37 gmaxwell: er lol at least you got it right.
  22:07:45 wumpus: the complaint was that systems became unsuably slow when using that many thread
  22:07:51 wumpus: so at least I got one thing right, woohoo
  22:07:55 sipa: seems i even acked it!
  22:07:57 BlueMatt: wumpus: there are more alus
  22:08:38 BlueMatt: but we need to improve lock contention first
  22:08:40 morcos: anywya, i think in the past the lock contention made 8 threads regardless of cores a bit dicey.. now that is much better (although more still to be done)
  22:09:01 BlueMatt: or we can just merge #10192, thats fee
  22:09:04 gribble: https://github.com/bitcoin/bitcoin/issues/10192 | Cache full script execution results in addition to signatures by TheBlueMatt · Pull Request #10192 · bitcoin/bitcoin · GitHub
  22:09:11 BlueMatt: s/fee/free/
  22:09:21 morcos: no, we do not need to improve lock contention first.   but we should probably do that before we increase the max beyond 16
  22:09:26 BlueMatt: then we can toss concurrency issues out the window and get more speedup anyway
  22:09:35 gmaxwell: wumpus: yea, well in QT I thought we also diminished the count by 1 or something?  but yes, if the motivation was to reduce how heavily the machine was used, thats fair.
  22:09:56 sipa: the benefit of using HT cores is certainly not a factor 2
  22:09:58 wumpus: gmaxwell: for the default I think this makes a lot of sense, yes
  22:10:10 gmaxwell: morcos: right now on my 24/28 physical core hosts going beyond 16 still reduces performance.
  22:10:11 wumpus: gmaxwell: do we also restrict the maximum par using this? that'd make less sense
  22:10:51 wumpus: if someone *wants* to use the virtual cores they should be able to by setting -par=
  22:10:51 sipa: *flies to US*
  22:10:52 BlueMatt: sipa: sure, but the shared cache helps us get more out of it than some others, as morcos points out
  22:11:30 BlueMatt: (because it means our thread contention issues are less)
  22:12:05 morcos: gmaxwell: yeah i've been bogged down in fee estimation as well (and the rest of life) for a while now.. otherwise i would have put more effort into jeremy's checkqueue
  22:12:36 BlueMatt: morcos: heh, well now you can do other stuff while the rest of us get bogged down in understanding fee estimation enough to review it ￼
  22:12:37 wumpus: [to answer my own question: no, the limit for par is MAX_SCRIPTCHECK_THREADS, or 16]
  22:12:54 morcos: but to me optimizing for more than 16 cores is pretty valuable as miners could use beefy machines and be less concerned by block validation time
  22:14:38 BlueMatt: morcos: i think you may be surprised by the number of mining pools that are on VPSes that do not have 16 cores ￼
  22:15:34 gmaxwell: I assume right now most of the time block validation is bogged in the parts that are not as concurrent. simple because caching makes the concurrent parts so fast. (and soon to hopefully increase with bluematt's patch)
  22:17:55 gmaxwell: improving sha2 speed, or transaction malloc overhead are probably bigger wins now for connection at the tip than parallelism beyond 16 (though I'd like that too).
  22:18:21 BlueMatt: sha2 speed is big
  22:18:27 morcos: yeah lots of things to do actually...
  22:18:57 gmaxwell: BlueMatt: might be a tiny bit less big if we didn't hash the block header 8 times for every block. ￼
  22:21:27 BlueMatt: ehh, probably, but I'm less rushed there
  22:21:43 BlueMatt: my new cache thing is about to add a bunch of hashing
  22:21:50 BlueMatt: 1 sha round per tx
  22:22:25 BlueMatt: and sigcache is obviously a ton
  ```

Tree-SHA512: a594430e2a77d8cc741ea8c664a2867b1e1693e5050a4bbc8511e8d66a2bffe241a9965f6dff1e7fbb99f21dd1fdeb95b826365da8bd8f9fab2d0ffd80d5059c

---
## [AxolotlClient/AxolotlClient-mod](https://github.com/AxolotlClient/AxolotlClient-mod)@[242f0ff090...](https://github.com/AxolotlClient/AxolotlClient-mod/commit/242f0ff0908ea3a908b157f2087673fa14319297)
#### Wednesday 2022-08-24 16:36:39 by moehreag

fun with particles

- lots of other things because I hate myself
- funny color things (move chroma option to color selector)

---
## [Ocramius/laminas-coding-standard](https://github.com/Ocramius/laminas-coding-standard)@[e64c11b798...](https://github.com/Ocramius/laminas-coding-standard/commit/e64c11b798f9b6e515194bf4de23346a2742b39b)
#### Wednesday 2022-08-24 17:43:46 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [jgudec/android_kernel_samsung_exynos2200](https://github.com/jgudec/android_kernel_samsung_exynos2200)@[9b38af8962...](https://github.com/jgudec/android_kernel_samsung_exynos2200/commit/9b38af89626e78d55306f8663d2b793ef63971c3)
#### Wednesday 2022-08-24 18:01:53 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [tomconnell-wf/gopherjs](https://github.com/tomconnell-wf/gopherjs)@[6af4ff4bf0...](https://github.com/tomconnell-wf/gopherjs/commit/6af4ff4bf0ebfe1903973afc5a1dc4f81a78d808)
#### Wednesday 2022-08-24 18:47:35 by Tom Connell

Switch from using Javascript object properties to using a Javascript Map for Go Maps

The main motivation for this change is to improve the performance of len() on maps.  Previously, len() would compile to javascript that called `Object.keys().length`.  This iterates the whole map to get its length.

Using the benchmarks added in this commit, on a map with 10000 elements:
BenchmarkMapLen             	    9886	    115719 ns/op

Now, len() just calls to javascript Map API, Map.size, which now as fast as calling len() on a slice.
BenchmarkMapLen             	1000000000	         0.5100 ns/op

So, changes are to statements.go and expressions.go to change how compling to Javascript works, to utilize the javascript Map API.  There are a few prelude changes to support that, also.

There are reflect and reflectlite changes to adjust where to get the value information off the Typ.

Fix indentation 📏

Genmin 🤖

FIx typoes

Add tests of map.  I hope adding the assert package as a dependency is okay.  🤞

Refine map tests ✨

Update assignment to use javascript Map api.  🔧

Update map tuple return and delete to use javascript Map api 🗺

Generate prelude min 🏭

Update prelude min 🏭

I did not mean to change this significant whitespace 😬

I did not mean to change this significant whitespace 😬

I did not mean to change this significant whitespace 😬

Clean up 🧹

Handle nil maps in loops 🔁

Use vanilla go to test ✅

Try maintaining the keys as object props and in a map object. 💡

Multiline these in a separate branch for cleaner diffs in other branch. 🧹

Possibly make diffs a tad better. 🤷‍♂️

Update expressions.go

Missed a case 😳

Comment explanation of strategy ✍️

Avoid double clone and excessive calls to size ♊️

Force go.mod to include vfsgen 🏴‍☠️

Clean up log statement 🧹

Add another test case ✅

Back this out, it isn't a function call, and isn't expensive. 👋

Might as well add a range test 🚂

Add benchmarks 📐

Update prelude_min.go

Cruft cleaner 🧹

Back out double-set of properties and map elements. 🚚

Some reflect changes. 😵‍💫

go generate 🏭

Flail, attempting to change all the correct reflections.  😵‍💫

Update reflectlite.go

I think this fixes the remained of reflection 😵‍💫

Ugh, generation had my working copy printlns 😵‍💫

I keep finding reflective things 🪩

Whoa.  Be very, very careful or things will evaluate in a different way than expected.  😵‍💫

I clearly don't understand this with enough depth, so change as little as possible. 😬

Fix internalize/eternalize 🔧

Yikes.  Watch out for those missing semicolons.  :astonished:

Update expressions.go

Add brackets around the expression `len(map[k]v{})` compiles to.

This ensures the correct operator precedence when evaluated in a broader
expression context.

Handle nil maps in `reflect` `mapaccess()` `mapdelete()` functions.

Previously those functions relied on a hack that `false[key]` evaluates
to `undefined`, just as if the key isn't in the map. However, calling a
function throws an exception.

reflect: Don't coerce `keyFor()` return value to string.

Previously when we were using object properties, JS runtime would coerce
property maps to strings even for non-string types (like numbers). This
is no longer the case with the `Map` type, so we must preserve the type
unchanged, or `Map.get()` returns `undefined`.

Update natives VFS.

Deleting keys from a map while iterating was shortchanging the number of iterations.  😵‍💫

Semicolons, again!  😡

Only call delete if it is a function.  😬

Remove commented statement 👋

Clean up after rebase 🧹

Exercise wrapping and unwrapping structs containing maps :running:

These tests should only run in a js build context :alien:

It seems like a struct named `Map` could shadow the scope of `window.Map` and cause unexpected behavior.

That's my hunch anyway.  The code at https://github.com/gopherjs/gopherjs/blob/a4630ec28c790dd1be785f097d0268c4aa4a423f/nosync/map.go#L37 was making an object that didn't have a `.get` function.  This fixes it.

The before Javascript:
```
	Map.ptr.prototype.LoadOrStore = function(key, value) {
		var _entry, _key, _tmp, _tmp$1, _tmp$2, _tmp$3, _tuple, actual, key, loaded, m, ok, value, value$1, x;
		actual = $ifaceNil;
		loaded = false;
		m = this;
		_tuple = (x = m.m, (_entry = typeof x.get === "function" ? x.get($emptyInterface.keyFor(key)) : undefined, _entry !== undefined ? [_entry.v, true] : [$ifaceNil, false]));
		value$1 = _tuple[0];
		ok = _tuple[1];
		if (ok) {
			_tmp = value$1;
			_tmp$1 = true;
			actual = _tmp;
			loaded = _tmp$1;
			return [actual, loaded];
		}
		if (m.m === false) {
			m.m = new Map();
		}
		_key = key; (m.m || $throwRuntimeError("assignment to entry in nil map")).set($emptyInterface.keyFor(_key), { k: _key, v: value });
		_tmp$2 = value;
		_tmp$3 = false;
		actual = _tmp$2;
		loaded = _tmp$3;
		return [actual, loaded];
	};
```

$global will be reliable regardless of runtime.  🪨

Add a test for looping on nil maps ☑️

Make the range map statement code a little less cringy ✨

Add a test case specifically for embedded js objects. ✅

Add a test for multiple deletes and delete on a nil map. ✅

These only can run in js.  If only I could remember that.  🤦‍♂️

This is my curse.  😫

Get rid of backticks 👋

Backtick exodus 🛸

Bye backticks 👋

Needless whitespace 👋

Break up complicated map expressions 🔪

Change test style to Got, Want idiom. 📖

Additional test style 🕴

---
## [vito/bass](https://github.com/vito/bass)@[49ab5c9974...](https://github.com/vito/bass/commit/49ab5c9974d4e163e58915fdaaa0734bf8e35938)
#### Wednesday 2022-08-24 18:55:12 by Alex Suraci

shim: reap zombies

rather than forcing folks to configure a dumb-init entrypoint, we'll
just have the shim handle reaping zombies, since it's already there, and
it's pretty handy to not have to ever think about this

sidebar: we're getting into "how i learned to stop worrying and love the
shim" territory. it's a bit of a pain to have to maintain, but it sure
grants a lot of flexibility!

---
## [GabrielePicco/CryptoBuzz](https://github.com/GabrielePicco/CryptoBuzz)@[d5b560ca3d...](https://github.com/GabrielePicco/CryptoBuzz/commit/d5b560ca3d0d1444d878d0b0c2f02ac985f2aa33)
#### Wednesday 2022-08-24 19:11:14 by root

Adding article: John McAfee's ex-girlfriend claims he faked his death with 'pretend' suicide after receiving mysterious call (6306779704811875b0a8fdcc)

---
## [aCrockofSchmidt/100-Days-of-Code-Python](https://github.com/aCrockofSchmidt/100-Days-of-Code-Python)@[0018b0918d...](https://github.com/aCrockofSchmidt/100-Days-of-Code-Python/commit/0018b0918d6d34ec9935177a600585585e763b4a)
#### Wednesday 2022-08-24 19:29:59 by aCrockofSchmidt

initial commit

Another frustrating experience. The challenge itself wasn't overly difficult, but finding the right elements was excruciating. And every run through the code took time only to find "element isn't actionable" or "element couldn't be found". So annoying.

I did this one on my own but admit to requiring some help to get xpaths correct. So, not a complete self creation but mostly. The hints in the instructions helped a little bit too, though I created a module rather than keeping the classes inside MAIN.PY.

All these challenges that require me to screw around with new social media accounts or worse, mess with my existing ones, are proving a drain. I don't like upsetting a well established applecart just for some silly "lesson".

---
## [endlessm/linux](https://github.com/endlessm/linux)@[7a2d8c2e9c...](https://github.com/endlessm/linux/commit/7a2d8c2e9ccfd80874573014c46b44088414d18d)
#### Wednesday 2022-08-24 20:07:32 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

BugLink: https://bugs.launchpad.net/bugs/1981649

commit c570449094844527577c5c914140222cb1893e3f upstream.

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Kamal Mostafa <kamal@canonical.com>
Signed-off-by: Stefan Bader <stefan.bader@canonical.com>

---
## [msrd0/bitmap-font](https://github.com/msrd0/bitmap-font)@[b374b3c35f...](https://github.com/msrd0/bitmap-font/commit/b374b3c35f8c019e0d4ddcc1767fd00a0910936d)
#### Wednesday 2022-08-24 21:06:36 by Dominic

shut up clippy ur stupid

honestly, tabs are so much better than spaces because
THEY CAN FUCKING ADAPT TO YOUR PREFERENCES

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[ddbdc64157...](https://github.com/ammarfaizi2/linux-fork/commit/ddbdc6415722db3f227bc80f9824f52fdce20fcb)
#### Wednesday 2022-08-24 21:51:41 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [12944qwerty/chat-components](https://github.com/12944qwerty/chat-components)@[337765e739...](https://github.com/12944qwerty/chat-components/commit/337765e739c7c7274e62f9f9fa5713786d731257)
#### Wednesday 2022-08-24 21:52:23 by Justice Almanzar

Create a markdown rule, rather than injecting the parser (#1)

* rename component

* add markdown rule instead of injecting parser

* add lookbehind and lookahead

* fuck you "text" rule

* version bump

---
## [ericberman/MyFlightbookWeb](https://github.com/ericberman/MyFlightbookWeb)@[f8e2d5324b...](https://github.com/ericberman/MyFlightbookWeb/commit/f8e2d5324b56eaec4c7e4fdd5f3ec1afce7c6e79)
#### Wednesday 2022-08-24 22:25:28 by ericberman

Issue #972: force postback for "show all" large logbooks

Gridviews suck performance when more than a few hundred rows, so force postback for "show all" if you have that many.  I'm using 500 flights as the threshold.

Trouble is, that the "show all" link was inside of a popmenu, so you can't make it a trigger.  Aargh.  So had to re-arrange the header of the logbook slightly to use CSS based pop-up instead of popmenu.  But alas, it (kinda) works.

---
## [alikhanyyan/Java-CodeSignal](https://github.com/alikhanyyan/Java-CodeSignal)@[00afb4161b...](https://github.com/alikhanyyan/Java-CodeSignal/commit/00afb4161b85dcc6548a03eef953c25fb62a952f)
#### Wednesday 2022-08-24 23:28:01 by Meri Alikhanyan

Seats in Theater

Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since the exit is located right behind your row to the left. All you need to do is climb over your seat and make your way to the exit.

The main problem is your shyness: you're afraid that you'll end up blocking the view (even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns to your left. To gain some courage, you decide to calculate the number of such people and see if you can possibly make it to the exit without disturbing too many people.

Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.

---
## [itsmeowForks/BeeStation-Hornet](https://github.com/itsmeowForks/BeeStation-Hornet)@[f9e73ec305...](https://github.com/itsmeowForks/BeeStation-Hornet/commit/f9e73ec305bcee7ec22b081d53ebd7c3f81b625b)
#### Wednesday 2022-08-24 23:43:46 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---

