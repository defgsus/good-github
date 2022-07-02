## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-01](docs/good-messages/2022/2022-07-01.md)


1,749,168 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,749,168 were push events containing 2,593,959 commit messages that amount to 192,422,806 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[707fbfac7e...](https://github.com/jlsnow301/tgstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Friday 2022-07-01 00:17:49 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [masutto/qb-core](https://github.com/masutto/qb-core)@[9d83a952c2...](https://github.com/masutto/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Friday 2022-07-01 01:00:00 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[9ccd6ecd74...](https://github.com/microsoft/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Friday 2022-07-01 01:10:54 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[446f280757...](https://github.com/microsoft/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Friday 2022-07-01 01:13:24 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [StephenSpoerri/Hwk30.6](https://github.com/StephenSpoerri/Hwk30.6)@[978f4d5a5d...](https://github.com/StephenSpoerri/Hwk30.6/commit/978f4d5a5d5cd0953a915e72343ad566e03fa5c4)
#### Friday 2022-07-01 01:20:31 by StephenSpoerri

Add files via upload

This data is to show the frequency of 'Random sweeps for contraband not including dog sniffs'  done to African American children in American schools
The mean is lower than the median in this data set therefore there are outliers on the low side therefore this could show that in most schools there are few random sweeps that are done on African American children but in a small amount of schools there are more cases of racial profiling by doing random searches for contraband which could be evidence of racial profiling in the United States of America.
However, the standard deviation is low (0.40 to two d.p) so this shows that the aforementioned problem applies to a lesser extent but due to the 68, 95, 99.7 rule that we read about in chapter 2 of the Charles Wheelan's book this is (most likely) an issue in some American schools.
I am interested in this topic because I want to learn more about racially profiling in the United States so I can obtain a better understanding on this topic; especially due to the current social climate in the United States. I think that learning about this is important especially for people that are not people of colour so they can better sympathise and understand the struggling of others

---
## [TAN-Gaming/reactos](https://github.com/TAN-Gaming/reactos)@[4471ee4dfa...](https://github.com/TAN-Gaming/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Friday 2022-07-01 03:05:02 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [kittywhiskers/dash](https://github.com/kittywhiskers/dash)@[67ceda1b5a...](https://github.com/kittywhiskers/dash/commit/67ceda1b5aa0c51f1fdce4fb71ccba1922e880f6)
#### Friday 2022-07-01 03:34:20 by fanquake

Merge #18295: scripts: add MACHO lazy bindings check to security-check.py

5ca90f8b598978437340bb8467f527b9edfb2bbf scripts: add MACHO lazy bindings check to security-check.py (fanquake)

Pull request description:

  This is a slightly belated follow up to #17686 and some discussion with Cory. It's not entirely clear if we should make this change due to the way the macOS dynamic loader appears to work. However I'm opening this for some discussion. Also related to #17768.

  #### Issue:
  [`LD64`](https://opensource.apple.com/source/ld64/) doesn't set the [MH_BINDATLOAD](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) bit in the header of MACHO executables, when building with `-bind_at_load`. This is in contradiction to the [documentation](https://opensource.apple.com/source/ld64/ld64-450.3/doc/man/man1/ld.1.auto.html):
  ```bash
  -bind_at_load
       Sets a bit in the mach header of the resulting binary which tells dyld to
       bind all symbols when the binary is loaded, rather than lazily.
  ```

  The [`ld` in Apples cctools](https://opensource.apple.com/source/cctools/cctools-927.0.2/ld/layout.c.auto.html) does set the bit, however the [cctools-port](https://github.com/tpoechtrager/cctools-port/) that we use for release builds, bundles `LD64`.

  However; even if the linker hasn't set that bit, the dynamic loader ([`dyld`](https://opensource.apple.com/source/dyld/)) doesn't seem to ever check for it, and from what I understand, it looks at a different part of the header when determining whether to lazily load symbols.

  Note that our release binaries are currently working as expected, and no lazy loading occurs.

  #### Example:

  Using a small program, we can observe the behaviour of the dynamic loader.

  Conducted using:
  ```bash
  clang++ --version
  Apple clang version 11.0.0 (clang-1100.0.33.17)
  Target: x86_64-apple-darwin18.7.0

  ld -v
  @(#)PROGRAM:ld  PROJECT:ld64-530
  BUILD 18:57:17 Dec 13 2019
  LTO support using: LLVM version 11.0.0, (clang-1100.0.33.17) (static support for 23, runtime is 23)
  TAPI support using: Apple TAPI version 11.0.0 (tapi-1100.0.11)
  ```

  ```cpp
  #include <iostream>
  int main() {
  	std::cout << "Hello World!\n";
  	return 0;
  }
  ```

  Compile and check the MACHO header:
  ```bash
  clang++ test.cpp -o test
  otool -vh test
  ...
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE

  # Run and dump dynamic loader bindings:
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=no_bind.txt ./test
  Hello World!
  ```

  Recompile with `-bind_at_load`. Note still no `BINDATLOAD` flag:
  ```bash
  clang++ test.cpp -o test -Wl,-bind_at_load
  otool -vh test
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE
  ...
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=bind.txt ./test
  Hello World!
  ```

  If we diff the outputs, you can see that `dyld` doesn't perform any lazy bindings when the binary is compiled with `-bind_at_load`, even if the `BINDATLOAD` flag is not set:
  ```diff
  @@ -1,11 +1,27 @@
  +dyld: bind: test:0x103EDF030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x103EDF030 = 0x7FFF70C9FA58
  +dyld: bind: test:0x103EDF038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x103EDF038 = 0x7FFF70CA12C2
  +dyld: bind: test:0x103EDF068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x103EDF068 = 0x7FFF70CA12B6
  +dyld: bind: test:0x103EDF070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x103EDF070 = 0x7FFF70CA1528
  +dyld: bind: test:0x103EDF080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x103EDF080 = 0x7FFF70C9FAE6
  <trim>
  -dyld: lazy bind: test:0x10D4AC0C8 = libsystem_platform.dylib:_strlen, *0x10D4AC0C8 = 0x7FFF73C5C6E0
  -dyld: lazy bind: test:0x10D4AC068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x10D4AC068 = 0x7FFF70CA12B6
  -dyld: lazy bind: test:0x10D4AC038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x10D4AC038 = 0x7FFF70CA12C2
  -dyld: lazy bind: test:0x10D4AC030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x10D4AC030 = 0x7FFF70C9FA58
  -dyld: lazy bind: test:0x10D4AC080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x10D4AC080 = 0x7FFF70C9FAE6
  -dyld: lazy bind: test:0x10D4AC070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x10D4AC070 = 0x7FFF70CA1528
  ```

  Note: `dyld` also has a `DYLD_BIND_AT_LAUNCH=1` environment variable, that when set, will force any lazy bindings to be non-lazy:
  ```bash
  dyld: forced lazy bind: test:0x10BEC8068 = libc++.1.dylib:__ZNSt3__113basic_ostream
  ```

  #### Thoughts:
  After looking at the dyld source, I can't find any checks for `MH_BINDATLOAD`. You can see the flags it does check for, such as MH_PIE or MH_BIND_TO_WEAK [here](https://opensource.apple.com/source/dyld/dyld-732.8/src/ImageLoaderMachO.cpp.auto.html).

  It seems that the lazy binding of any symbols depends on whether or not [lazy_bind_size](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) from the `LC_DYLD_INFO_ONLY` load command is > 0. Which was mentioned in [#17686](https://github.com/bitcoin/bitcoin/pull/17686#issue-350216254).

  #### Changes:
  This PR is one of [Corys commits](https://github.com/theuni/bitcoin/commit/7b6ba26178d2754568a1308d3d44e038e9ebf450), that I've rebased and modified to make build. I've also included an addition to the `security-check.py` script to check for the flag.

  However, given the above, I'm not entirely sure this patch is the correct approach. If the linker no-longer inserts it, and the dynamic loader doesn't look for it, there might be little benefit to setting it. Or, maybe this is an oversight from Apple and needs some upstream discussion. Looking for some thoughts / Concept ACK/NACK.

  One alternate approach we could take is to drop the patch and modify security-check.py to look for `lazy_bind_size` == 0 in the `LC_DYLD_INFO_ONLY` load command, using `otool -l`.

ACKs for top commit:
  theuni:
    ACK 5ca90f8b598978437340bb8467f527b9edfb2bbf

Tree-SHA512: 444022ea9d19ed74dd06dc2ab3857a9c23fbc2f6475364e8552d761b712d684b3a7114d144f20de42328d1a99403b48667ba96885121392affb2e05b834b6e1c

---
## [matthiaskrgr/rust](https://github.com/matthiaskrgr/rust)@[335e7d3e33...](https://github.com/matthiaskrgr/rust/commit/335e7d3e33300942ce99e7010a31ad4c1086a36a)
#### Friday 2022-07-01 04:06:01 by Matthias Krüger

Rollup merge of #98745 - thomcc:build-dir-arg, r=jyn514

Add a `--build-dir` flag to rustbuild

This adds an optional `--build-dir <path>` flag to rustbuild (to both the python and rust code in src/bootstrap). If provided, it overrides build directory from the config file (if any was provided).

My reason for wanting this is that I often will make a change, save, and then go run `x.py check` or `x.py test` (or something). Because I've saved, vscode will start doing its thing in the background, but this will take the file lock, preventing `x.py` from running until vscode finishes whatever it's doing (since the manually invoked x.py won't be able to acquire said file lock). This is annoying, because I'd rather the command I explicitly invoke *not* wait for r-a to complete, as r-a's check is conceptually a background task (and one which can take quite some time to complete).

Anyway, while there are likely other ways this could be handled, if you have the disk space an easy way is to just have vscode be configured to use a different build directory, and then they never have to block each-other.

This can currently be arranged without this patch, by maintaining two `config.toml`s, one of which has a different build dir, and just exists to be passed into the overridden check command in vscode.

Unfortunately, this has the downside of requiring I maintain two `config.toml`s and keep them (at least somewhat) in sync, aside from the build dir. I dislike for several reasons, not the least of which because I know myself well enough to know that these will inevitably get out of sync and confuse me in the future (perhaps this case would be different since I've thought about it enough to write this patch? Who knows, I'd rather not find out).

Either way, it would be much easier for me to have a way for *only* the build directory to differ, which this patch provides by way of a new flag.  I suggested this to `@jyn514` who indicated it sounded reasonable so long as it didn't add too much complexity, which I think I've achieved, but he can be the judge.

Anyway, with this patch I can just use something like `["python3", "x.py", "check", "--build-dir", "build-vscode", "--json-output"]` as the overridden check command to rust-analyzer, and do not need to futz with any additional `config.toml`s. Which is very nice!

I've tested this manually, and can confirm that it works. I'm not sure if it needs automated tests, or where I should add them if so.

r? `@jyn514` (who has had to put up with my complaints about this... many times. <3)

---
## [darshan-/PurpOS](https://github.com/darshan-/PurpOS)@[8573019c1a...](https://github.com/darshan-/PurpOS/commit/8573019c1a538d837d7fa38e9c6f1a4cd040e656)
#### Friday 2022-07-01 07:03:04 by Darshan-Josiah Barber

Okay, cool, that took all of 5 or 10 seconds longer to sort out.  It had previously been fine to print before the console was set up, and to printf once the heap was set up, and I remember maknig sure the heap was set up, so thinking printf was okay.  But console wasn't set up, so default active console was -1.  So I had silent memory corruption, and all of the strange behavior seems compatible with that.  I think it's likely fine to printTo before console is set up (haven't checked and not sure), but besides removing the offending printf statement I don't need, I'm now also checking that at (active terminal) is set before printing.  (I could default to 0 or 1... but I don't really care right now.)  So now I thing can go back to checking that malloc works the way I was just experimenting with changing to when this all happend.  And then get back to setting up a readline syscall, and then get back to setting up a basic shell in userspace, and get prompting upon process completion working properly, and everthing else I was in the middle of having fun with.

I think there are some broader lessons here around this type of bug and thinking about how to avoid or lessen the likelihood of similar ones in the future.  And around how defeated I felt, and afraid that it was a deeper, fundamental problem with my approach (which, sure, they may be some, but sensing the fear and despair is what's interesting here -- discovering a fundamental problem with my approach would be an opportunity to deepend my understanding, which is a lot of the point of this project), and got ungrounded and spacey.  Getting focused on: okay, so where are we getting stuck when booting fails?  Can't we go slow, do some output, and narrow it down to exactly where it's happening?  And of course, we could, and finally did.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[16553f6c35...](https://github.com/mrakgr/The-Spiral-Language/commit/16553f6c3516cf62c8e6cedc29d665f5dfad4c45)
#### Friday 2022-07-01 07:28:49 by Marko Grdinić

"8:30am. I got up at 6:30am and have been doing chores since then. I need some time to cool down.

I've been thinking about the job quest. Whether it is worth it for me to find a job all depends on the cost of training a system like DALLE.

https://news.ycombinator.com/item?id=31228710
> One thing I’ve not seen mentioned/asked about DALL-E 2, which I’m really, really intrigued about is what hardware its typically running on and the average time it takes for image generation? Maybe I’ve somehow missed it, but I’m really intrigued by what their hardware set up is and how long it on average takes to generate the eight images from a users text input? I’m guessing it’s really quick, but I honestly have no idea… How does this system scale? Typical cost per image generated?

8:50am. https://twitter.com/alexjc/status/1348267025320304641
> My current estimate for training DALL·E is around $300k-$500k, since it's around 15x smaller than GPT-3 and that's estimated to have cost $4.6M. DALL·E has an additional VQVAE2 decoder, which may increase training times...

Forget this. I am not going to work for 5 years just to gamble on a single training run.

8:55am. Yeah, the Singularity in this timeline is so far is incredibly bootleg. Let me post a link.

https://semianalysis.substack.com/p/nvidia-in-the-hot-seat
> Intel Habana, Graphcore, Google TPU, and Nvidia A100 Compared In AI Training

I saw this 2 days ago, but I missed my chance to post it so let me do it now.

I really expected the AI chips to be able to beat the GPU 10x initially and 100x at the end of the road, and this is without memristor breakthroughs.

Instead I have this trash where they outright fail to beat the GPUs on most tasks, and when the finally win, it is something trivial like 30%. I do not buy the excuse the software is the problem, NNs aren't that hard to program.

Just what can I do with this? I'd like to get a job so I can actually buy something with that money. But this certainly is not worth buying. So I do not really need a job after all.

I wish I could do something about my mother's cancer situtation, but cancer is not something I can deal with using the power of money either. Even if I cryofroze her once the situation got bad enough, I'd need post Singularity tech to resurrect her. And is we are talking post-Singularity, things like asking whoever is running the universe for backups, and even something like resimulating the universe becomes viable. I am not going to bother thinking too seriously about these matters.

So in the end, I could only get a better GPU and CPUs with the money from a job I would get. Not useless, but it is not a big deal either given the Moore's Law breakdown.

Getting a job would only matter if it would get me the kind of hardware I'd need to train DALLE cheaply.

9:05am. Even if I got a job, I can't bet on the hardawre improvements bringing the figure down significantly in 5 years time.

There are basically only two things that matter at this point:

* Revolutionary algorithmic improvements that could make RL viable. If I could make guaranteed money via RL, I could then reinvest it and form a positive feedback loop.
* Memristor breakthroughs leading to huge hardware improvements. This might be needed to enable the algo revolution. Also would actually allow me to cultivate DALLE style systems cheaply even without revolutionary algo advances.

What are the chances of the two points happening in the next 5 years? Who knows.

Even if the second point happened today, it would still take years for the devices to be commercially viable. Realistically, it could happen in the next few years, but it is the kind of thing that I need to see to believe it first. I won't forget how I got suckered the last decade by the memristor hype.

9:10am. The first point would have the most immediate effect and would make my poker plan viable even with today's hardware. Since it is just knowledge, once it is shared it would have tremendous impact on RL.

It is a big mystery to me if the brain algorithm could be run efficiently on GPUs, or if it requires novel hardware. On the issue of whether intelligence could be optimally run on GPUs or whether it requires neuromorphic chips, either side seems equaly plausible to me.

9:15am. Since the situation is like this, I am helpless regarding anything I want to do. I can only sit tight and work on my hobbies.

Just forget this thing. The pursuit of Singularity might only become viable 10 years from now, and 10 years from now who knows what will happen. I could be dead for all I know. I am just human. 10 years is perfectly long enough to develop and die cancer myself or get hit by a truck while taking out the trash.

9:20am. 500k to train DALLE is not exorbiantly expensive. It is not 50M. But no starving artist such as myself could afford such a figure anyway.

9:25am. Forget this. I have plenty of time to practice drawing, music, 3d, write and finish the C backend for Spiral.

This NEET existence is something I've earned by finishing school a decade and a half ago, so I might as well stay snug.

Let me read Baki here. Egg of the Elf is out as well. I'll try to put in a few hours into doing 3d today, just placing boxes in the right spots. Right now I am still groggy so I do not feel like it. Maybe I'll take a nap."

---
## [Akuma-Reiki/ult-hitbox-editor](https://github.com/Akuma-Reiki/ult-hitbox-editor)@[0fa9dd4b3e...](https://github.com/Akuma-Reiki/ult-hitbox-editor/commit/0fa9dd4b3e263e78c72230433084d97277f53a4f)
#### Friday 2022-07-01 07:40:29 by Akuma-Reiki

fixed an error and prolly some other stuff

stupid fucking is_excute instead of is_execute
who the fuck made this game
fuck you sakurai

---
## [AngelicosPhosphoros/rust](https://github.com/AngelicosPhosphoros/rust)@[07f586fe74...](https://github.com/AngelicosPhosphoros/rust/commit/07f586fe746a362fdebfc1cec0016dd024780dce)
#### Friday 2022-07-01 08:07:15 by Dylan DPC

Rollup merge of #96642 - thomcc:thinbox-zst-ugh, r=yaahc

Avoid zero-sized allocs in ThinBox if T and H are both ZSTs.

This was surprisingly tricky, and took longer to get right than expected. `ThinBox` is a surprisingly subtle piece of code. That said, in the end, a lot of this was due to overthinking[^overthink] -- ultimately the fix ended up fairly clean and simple.

[^overthink]: Honestly, for a while I was convinced this couldn't be done without allocations or runtime branches in these cases, but that's obviously untrue.

Anyway, as a result of spending all that time debugging, I've extended the tests quite a bit, and also added more debug assertions. Many of these helped for subtle bugs I made in the middle (for example, the alloc/drop tracking is because I ended up double-dropping the value in the case where both were ZSTs), they're arguably a bit of overkill at this point, although I imagine they could help in the future too.

Anyway, these tests cover a wide range of size/align cases, nd fully pass under miri[^1]. They also do some smoke-check asserting that the value has the correct alignment, although in practice it's totally within the compiler's rights to delete these assertions since we'd have already done UB if they get hit. They have more boilerplate than they really need, but it's not *too* bad on a per-test basis.

A notable absence from testing is atypical header types, but at the moment it's impossible to manually implement `Pointee`. It would be really nice to have testing here, since it's not 100% obvious to me that the aligned read/write we use for `H` are correct in the face of arbitrary combinations of `size_of::<H>()`, `align_of::<H>()`, and `align_of::<T>()`. (That said, I spent a while thinking through it and am *pretty* sure it's fine -- I'd just feel... better if we could test some cases for non-ZST headers which have unequal and align).

[^1]: Or at least, they pass under miri if I copy the code and tests into a new crate and run miri on it (after making it less stdlibified).

Fixes #96485.

I'd request review ``@yaahc,`` but I believe you're taking some time away from reviews, so I'll request from the previous PR's reviewer (I think that the context helps, even if the actual change didn't end up being bad here).

r? ``@joshtriplett``

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[675ccb4ee7...](https://github.com/git-for-windows/git/commit/675ccb4ee7a2df1d6f24d813fa68111d8a02973e)
#### Friday 2022-07-01 09:52:24 by Glen Choo

setup.c: create `discovery.bare`

There is a known social engineering attack that takes advantage of the
fact that a working tree can include an entire bare repository,
including a config file. A user could run a Git command inside the bare
repository thinking that the config file of the 'outer' repository would
be used, but in reality, the bare repository's config file (which is
attacker-controlled) is used, which may result in arbitrary code
execution. See [1] for a fuller description and deeper discussion.

A simple mitigation is to forbid bare repositories unless specified via
`--git-dir` or `GIT_DIR`. In environments that don't use bare
repositories, this would be minimally disruptive.

Create a config variable, `discovery.bare`, that tells Git whether or
not to die() when it discovers a bare repository. This only affects
repository discovery, thus it has no effect if discovery was not
done, e.g. if the user passes `--git-dir=my-dir`, discovery will be
skipped and my-dir will be used as the repo regardless of the
`discovery.bare` value.

This config is an enum of:

- "always": always allow bare repositories (this is the default)
- "never": never allow bare repositories

If we want to protect users from such attacks by default, neither value
will suffice - "always" provides no protection, but "never" is
impractical for bare repository users. A more usable default would be to
allow only non-embedded bare repositories ([2] contains one such
proposal), but detecting if a repository is embedded is potentially
non-trivial, so this work is not implemented in this series.

[1]: https://lore.kernel.org/git/kl6lsfqpygsj.fsf@chooglen-macbookpro.roam.corp.google.com
[2]: https://lore.kernel.org/git/5b969c5e-e802-c447-ad25-6acc0b784582@github.com

Signed-off-by: Glen Choo <chooglen@google.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [WraithKim/together-bot](https://github.com/WraithKim/together-bot)@[89ad31f1d4...](https://github.com/WraithKim/together-bot/commit/89ad31f1d402625be396fc5a5d6fe17f7f863544)
#### Friday 2022-07-01 10:56:26 by wraithkim

뻑업, 퍼큐, 퍼킹 추가

- fuck up, fuck you, fucking의 한국 발음.

---
## [h-vetinari/scipy](https://github.com/h-vetinari/scipy)@[0b53fc4c9c...](https://github.com/h-vetinari/scipy/commit/0b53fc4c9c593ee524a003296da6be83c9d41a28)
#### Friday 2022-07-01 11:41:33 by Tyler Reddy

MAINT: SCIPY_USE_PROPACK

* this is effectively a forward port and modernization
of the release branch `PROPACK` shims that were added in
gh-15432; in short, `PROPACK` + Windows + some linalg backends
was causing all sorts of trouble, and this has never been resolved

* I've switched to `SCIPY_USE_PROPACK` instead of `USE_PROPACK`
for the opt-in, since this was requested, though the change
between release branches may cause a little confusion (another
release note adjustment to add maybe)

* I think the issues are painful to reproduce; for my part,
I did the following just to check the proper skipping/accounting
of tests:

- `SCIPY_USE_PROPACK=1 python dev.py -j 20 -t scipy/sparse/linalg`
  - `932 passed, 172 skipped, 8 xfailed in 115.57s (0:01:55)`
- `python dev.py -j 20 -t scipy/sparse/linalg`
  - `787 passed, 317 skipped, 8 xfailed in 114.80s (0:01:54)`

* why am I doing this now? well, to be frank the process of manually
backporting this for each release is error-prone, and may cause
additional confusion/debate, which I'd like to avoid. Besides, if it
is broken in `main` we may as well have the shims there as well. I would
point out that you may want to add `SCIPY_USE_PROPACK` to 1 or 2 jobs
in CI? The other reason is that if usage of `PROPACK` spreads, I don't
want to be manually applying more skips/shims on each release (which
I already had to do here with two new tests it seems)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5986bfbdd2...](https://github.com/mrakgr/The-Spiral-Language/commit/5986bfbdd26269f9ef44f84a5d1d61433edecedc)
#### Friday 2022-07-01 11:45:43 by Marko Grdinić

"https://www.nextbigfuture.com/2020/11/memristors-and-hpe-machine-focused-computer-research-seems-almost-dead.html

Sad. Forget about memristors for now.

11:15am. Done with breakfast. Let me try working on that skeleton for a bit. I want to go to bed, but am too agitated to do that. I wouldn't be able to get any good rest at this point.

11:20am. I created the Eaten in Darkness - Gray Goo folder and saved the default cube as `skeleton.blend`.

Now what is next. I've resized the cube a bit, but I am not sure what the width and the depth of a human body is.

Let me open the anatomy for sculptors book.

11:30am. Page 9 of 220 has a pretty good skelly profile image from both sides.

11:40am. Interesting that you can change between objects while in edit mode using Alt Q. I don't think that a year ago Blender had this feature. It will be convenient.

At any rate, I am starting to feel it a bit. Just one big box for the body does not do much for me, but now that I am trying to figure out the proportions of the head I am getting into it. Usually what I'd do is important the ref image directly into Blender and set it on the background, but I want to move away from that.

I want to try doing the skeleton using my own aesthetic sense while going back and forth between the book and Blender. That should lead to better learning.

11:45am. Focus on Blender, not on this journal. Get back to work me.

12:15pm. Oh yes, feet. Right now I am just trying to stay awake.

But besides that I am making steady if very slow progress.

12:50pm. Let me take a short break here and then I will write down my thoughts.

1:25pm. I back. Anyway, I am done with the first block out phase. This bring back memories to the base mesh I did. I found it quite hard to immitate what Flycat was doing back then. For example when he did the back and the neck, getting the exact angle was difficult. But now I do not think that matters much.

What this version is, is merely a launch off point for the subsequent phase. I do not need to concern myself too much with details and angles.

If I could see the compled image superimposed on these primitives then yes, I'd be able to see where I am going wrong. But even so this is good enough to get a sense of the proportions. With just a cube I had a very rough view, but with this version, I can see much better. I can see the head, the arms, the legs, the chest, the buttocks and the abdomen. They are roughly in the right place.

Now, if it was Yan or Flycat, they'd jump into the sculpting phase.

But I have a better idea - why not go for another block out phase? There is no reason why it has to be only a single one. Now that I have a body made of large primitives, why not go for a body made of larger primitives and use the previus phase as a scaffolding?

This is the way to do it. It gets to the essence of sketching in 2d art.

If I follow this path, I think for models that I am familiar with I should be able to make them from imagination. This is like the holy grail of 2d art, but in 3d it would not be a big deal.

But you do need to follow the proper workflow. Imagine trying to do it like the anime head guy - unless you can xerox it like Kim Jung Gi you'd never get anywhere using such a method.

1:35pm. The block out I have right now is suitable for a body, but for the next step, I'll want to move to modeling individual bones. I won't bother detailing them, and some composites like the ribcage and the spine, I won't bothe individuating, but otherwise, the final product of this version should be recognizable as a low poly skelly.

1:40pm. I do not feel like doing it now. Today was just an icebraker, and I keep yawning from lack of sleep.

Yesterday I went to bed too late given how early I am getting up. At slightly before 11pm. This beats my usual 1-2am, but I guess I am still not getting enough sleep.

There is no helping it, doing these chores so early in the morning for the sake of winter preparation will distrupt my rhythm. Maybe I'll get used to it by tomorrow.

Let me go to bed for a while.

Even though I won't be doing the work that I should, I will stick to my principles and not play games or read novels or manga. This will help with building my determination.

A pro would breeze through this, but I can only treat this project like I would a programming project. In programming I have a hard time starting on new parts too, and I always just take the time to brainstorm it. This helps me get motivated to do the work as well."

---
## [CarmenUZH/Pong](https://github.com/CarmenUZH/Pong)@[0d3666b4a6...](https://github.com/CarmenUZH/Pong/commit/0d3666b4a64a780724e52d5196e772ebc5907c95)
#### Friday 2022-07-01 12:56:00 by Carmen

Damn bitch, i just wanted Pong

Honestly, are you okay?

---
## [omertuc/assisted-installer-agent](https://github.com/omertuc/assisted-installer-agent)@[0ac51c03dc...](https://github.com/omertuc/assisted-installer-agent/commit/0ac51c03dc6cb9e93f3bf0a6acfedcf6202eaad1)
#### Friday 2022-07-01 13:31:35 by Omer Tuchfeld

MGMT-10973 - Copy coredns & keepalived static pod manifests in day-2 connectivity-check ignition

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

However, that ignition file is incomplete as currently we only include
necessary information in it (because that file is very big). The parts
of that file that we care in this case are currently missing, so we have
to modify the agent to include those files.

This commit does that. A follow-up commit will be done on the service to
actually check for the presence of these files in this ignition to make
the decision of whether the cluster is managed or not, and in turn turn
on the necessary validations if not.

# Ignition Files

The ignition files we currently include are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

# Agent version skew concerns

We also call the `agentVersionSkewHack` function which adds a fake file
to the ignition config that can be used by the service to know whether
this the ignition file was filtered by a recent version of the agent or
not.

Since the *absence* of the coredns and keepalived files copied by
`copyIgnitionManagedNetworkIndications` indicates that the cluster is
running a non-managed-network cluster, the service has no way to know
whether the absence is due to that ignition file being processed by an
old agent or due to an actual absence. To overcome this ambiguity, we
add this dummy file to the ignition which can help the service tell
those two situations apart.

---
## [mootowncow/topaz](https://github.com/mootowncow/topaz)@[b9df27472a...](https://github.com/mootowncow/topaz/commit/b9df27472a832d88b0e7d4c7154dbbe6f455be27)
#### Friday 2022-07-01 13:33:52 by Shiyo

MMM adjustments

Increased the fTP of "Cursed Sphere Nightmare" used by Terrorfly to 5(was 1.5)

Increased the amount of status effects drained by Debilitating Drone to 7(was 1 random)

Increased the fTP of "Somersault" to 2.0(was 1.5)

Terror Flys Amnesia aura should now have 0 downtime in it's application.

Awful Eye Nightmare now properly resets hate when the enemy is facing Tanihwa.

---
## [lck/tvision](https://github.com/lck/tvision)@[45e408ac9d...](https://github.com/lck/tvision/commit/45e408ac9d41577177484df85ed4c0c766c3691d)
#### Friday 2022-07-01 14:14:13 by magiblot

Fix (TCollection *) to (TSortedCollection *) cast in TSortedListBox::list()

God damn. Because TCollection and TSortedCollection are no more than forward declarations by the time TSortedListBox::list() is defined, the cast is implemented as a reinterpret_cast. As a consequence, invoking TSortedListBox::list() would provide the wrong result.

Amazingly, Borland C++ handles this fine, so I have been hugely confused while debugging this.

This is my first experience where C-style casts have silenced a compilation error.

---
## [Amber-Waters/youDontSeeMe](https://github.com/Amber-Waters/youDontSeeMe)@[f65e24e180...](https://github.com/Amber-Waters/youDontSeeMe/commit/f65e24e1808e3ed85409f0dcb4d85b13431a93bf)
#### Friday 2022-07-01 17:27:10 by Amber Waters

Create iLoveYouALittleALotEtc_cw

DESCRIPTION:

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[0b14f91ce2...](https://github.com/NetBSD/pkgsrc/commit/0b14f91ce29473ac693867cb3a33a6a1218c088c)
#### Friday 2022-07-01 18:19:10 by wiz

mame: update to 0.245.

The highly-anticipated release of MAME 0.245 has finally arrived!
As I’m sure many of you are already aware, we’ve added support for
two elusive arcade games that didn’t see widespread release: Megumi
Rescue and Marble Madness II, and the Konami Polygonet system has
finally come to life. But before we get to that, there are some
changes to MAME’s user interface that you should be aware of. Input
options have been moved off the main menu to a submenu of their
own. Depending on the system, there can be quite a few of them,
and they weren’t all grouped. There’s also a new option to see the
input devices recognised by MAME, which should help with diagnosing
issues.

Megumi Rescue was exhibited at a trade show, but apparently never
sold as an arcade game. A home system port was released, but only
in Japan. The original arcade game uses a vertically-oriented
monitor, and lacks the life bar system and vertical scrolling found
in the home version. Despite the arcade version remaining unreleased,
and the home version never being widespread, the game was widely
copied for TV game systems. It’s nice to see the original preserved
all these years later.

Marble Madness II was considered a failure on location test. It
demonstrates Atari’s complete failure to understand what Mark Cerny
got right when he made the mid ’80s classic. A few examples survived
in the hands of collectors, but the game was never seen widely.

The Polygonet system was Konami’s first foray into 3D arcade games.
It was quite apparent that their in-house system wasn’t able to
compete toe-to-toe with offerings from Sega and Namco. Polygonet
Commanders was added to MAME almost twenty years ago, and saw
sporadic progress for a few years after that. Regular contributor
Ryan Holtz has written an engaging blog post about his adventures
bringing it up to a playable state this month. The two games haven’t
been promoted to working yet as they haven’t been extensively
tested, but we’d love it if you try them out and post your experiences,
good or bad.

We’ve got more complete emulation for three Mac NuBus video cards
this month: the Apple Macintosh Display Card, the SuperMac Spectrum/8
Series III, and the SuperMac Spectrum PDQ. The Macintosh Display
card, which MAME uses by default for the Mac II, now supports
configuring the amount of video RAM installed, as well as a selection
of monitors with correct resolutions, refresh rates and colour
profiles. The SuperMac Spectrum/8 Series III supports on-screen
resolutions up to 1024×768, and virtual desktop resolutions up to
a massive 4096×1536 in Black & White mode. Virtual desktop panning
and desktop zoom are hardware-accelerated. The Spectrum PDQ supports
resolutions up to 1152×870, with hardware acceleration for things
like moving windows in 256-colour modes. Please be aware that MAME
currently has trouble with some combinations of Mac video cards –
if you want to use multiple monitors on your emulated Mac, it’s
best to stick with the Macintosh Display Card or Radius ColorBoard.
If you’re you’re just looking to jump into Mac emulation, there’s
some helpful information to get you started on our wiki.

Thanks in large part to the efforts of Ignacio Prini and Manuel
Gomez Amate, the ZX Spectrum cassette software list now includes
the Spanish MicroHobby magazine cover tape and type-in program
collection. A number of prototypes cartridges have been added for
the Game Boy, Super NES and other consoles. Commodore 64 tapes,
Apple II floppies, and game music rips in VGM format have each seen
a batch of additions.

---
## [Cockatrice/Magic-Token](https://github.com/Cockatrice/Magic-Token)@[589b2788bf...](https://github.com/Cockatrice/Magic-Token/commit/589b2788bf5a8719a7584c7832f1c9b8a3129504)
#### Friday 2022-07-01 18:24:22 by ebbit1q

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
## [Himemoria/android_kernel_xiaomi_mt6768](https://github.com/Himemoria/android_kernel_xiaomi_mt6768)@[1032d22f7a...](https://github.com/Himemoria/android_kernel_xiaomi_mt6768/commit/1032d22f7a61e46e72d2bb266b62d95a259c949c)
#### Friday 2022-07-01 19:35:13 by Peter Zijlstra

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
Signed-off-by: Himemorii <himemori@mail.com>

---
## [Himemoria/android_kernel_xiaomi_mt6768](https://github.com/Himemoria/android_kernel_xiaomi_mt6768)@[14272641bf...](https://github.com/Himemoria/android_kernel_xiaomi_mt6768/commit/14272641bf27fa2de42e44fb2808f898878e19d1)
#### Friday 2022-07-01 19:52:37 by Jan Alexander Steffens (heftig)

ZEN: Implement zen-tune v4.20 over v4.14-arm64

4.9:
In a surprising turn of events, while benchmarking and testing
hierarchical scheduling with BFQ + writeback throttling, it turns out
that raising the number of requests in queue _actually_ improves
responsiveness and completely eliminates the random stalls that would
normally occur without hierarchical scheduling.

To make this test more intense, I used the following test:

Rotational disk1: rsync -a /source/of/data /target/to/disk1
Rotational disk2: rsync -a /source/of/data /target/to/disk2

And periodically attempted to write super fast with:
dd if=/dev/zero of=/target/to/disk1/block bs=4096

This wrote 10gb incredibly fast to writeback and I encountered zero
stalls through this entire test of 10-15 minutes.

My suspicion is that with cgroups, BFQ is more able to properly sort
among multiple drives, reducing the chance of a starved process.  This
plus writeback throttling completely eliminate any outstanding bugs with
high writeback ratios, letting the user enjoy low latency writes
(application thinks they're already done), and super high throughput due
to batched writes in writeback.

Please note however, without the following configuration, I cannot
guarantee you will not get stalls:

CONFIG_BLK_CGROUP=y
CONFIG_CGROUP_WRITEBACK=y
CONFIG_IOSCHED_CFQ=y
CONFIG_CFQ_GROUP_IOSCHED=y
CONFIG_IOSCHED_BFQ=y
CONFIG_BFQ_GROUP_IOSCHED=y
CONFIG_DEFAULT_BFQ=y
CONFIG_SCSI_MQ_DEFAULT=n

Special thanks to h2, author of smxi and inxi, for providing evidence
that a configuration specific to Debian did not cause stalls found the
Liquorix kernels under heavy IO load.  This specific configuration
turned out to be hierarchical scheduling on CFQ (thus, BFQ as well).

4.10:
During some personal testing with the Dolphin emulator, MuQSS has
serious problems scaling its frequencies causing poor performance where
boosting the CPU frequencies would have fixed them.  Reducing the
up_threshold to 45 with MuQSS appears to fix the issue, letting the
introduction to "Star Wars: Rogue Leader" run at 100% speed versus about
80% on my test system.

Also, lets refactor the definitions and include some indentation to help
the reader discern what the scope of all the macros are.

4.11:
Increase MICRO_FREQUENCY_UP_THRESHOLD from 95 to 85
Increase MIN_FREQUENCY_UP_THRESHOLD from 11 to 6

These changes should help make using CFS feel a bit more responsive when
working with mostly idle workloads, browsing the web, scrolling through
text, etc.

Increasing the minimum frequency up threshold to 6% may be too
aggressive though.  Will revert this setting if it causes significant
battery drain.

4.12:
Make bfq the default MQ scheduler

Reduce default sampling down factor from 10 to 1

With the world eventually moving to a more laptop heavy configuration,
it's getting more important that we can reduce our frequencies quickly
after performing work.  This is normal with a ton of background
processes that need to perform burst work then sleep.

Since this doesn't really impact performance too much, lets not keep it
part of ZEN_INTERACTIVE.

Some time ago, the minimum frequency up threshold was set to 1 by
default, but the zen configuration was never updated to take advantage
of it.

Remove custom MIN_FREQUENCY_UP_THRESHOLD for MuQSS / ZEN_INTERACTIVE
configurations and make 1 the default for all choices.

4.18:
Prefer bfq-mq when available if zen interactive is enabled

The bfq-mq elevator is typically one major kernel version ahead in
optimizations and bug fixes due to early access patches in the
algodev/bfq-mq github repository.  Since these patches are typically low
risk and almost always improve performance and/or increase stability,
prefer bfq-mq over bfq when available.

Switch from MuQSS to PDS-mq.

4.19:
Switch from PDS-mq back to MuQSS

4.20:
During some experimentation to influence MuQSS into consolidating strong
single threaded workloads to single cores, I found that the up_threshold
just ends up forcing all cores to run at a higher frequency.

Instead, raising up_threshold back to defaults (95 with micro sampling),
and raising the sampling down factor to 5, the individual cores MuQSS
selects (typically the first few), tend to properly stick to their max
speed and because they complete their tasks faster, MuQSS selects them
again to for the earliest eligible deadline, causing a reciprocal cycle
that improves single thread performance.

Completely fair scheduler (CFS), never really had this issue, but we'll
leave sampling down factor high with CONFIG_ZEN_INTERACTIVE since it'll
benefit CFS users that want higher performance anyway.

Raise minimum CFS latency to 4ms to match 250hz configs.
Raise minimum MuQSS latency to 4ms to match 250hz configs.

Use [defer+madvise] as default khugepaged defrag strategy:

For some reason, the default strategy to respond to THP fault fallbacks
is still just madvise, meaning stall if the program wants transparent
hugepages, but don't trigger a background reclaim / compaction if THP
begins to fail allocations.  This creates a snowball affect where we
still use the THP code paths, but we almost always fail once a system
has been active and busy for a while.

The option "defer" was created for interactive systems where THP can
still improve performance.  If we have to fallback to a regular page due
to an allocation failure or anything else, we will trigger a background
reclaim and compaction so future THP attempts succeed and previous
attempts eventually have their smaller pages combined without stalling
running applications.

We still want madvise to stall applications that explicitely want THP,
so defer+madvise _does_ make a ton of sense.  Make it the default for
interactive systems, especially if the kernel maintainer left
transparent hugepages on "always".

Reasoning and details in the original patch: https://lwn.net/Articles/711248/

Add a scheduler even to multi-queue block devices:
We prefer interactivity to throughput and want BFQ if possible.

Signed-off-by: Albert I <kras@raphielgang.org>
Signed-off-by: Udit Karode <udit.karode@gmail.com>
Signed-off-by: Himemorii <himemori@mail.com>

---
## [Subject9x/battleMETAL](https://github.com/Subject9x/battleMETAL)@[ca4c74d221...](https://github.com/Subject9x/battleMETAL/commit/ca4c74d221119d21578e60cebf137712dd439032)
#### Friday 2022-07-01 20:03:50 by subject9x

major rebuild: mech pieces completely decomposed to field variables.

Why: both server and client code was struggling to manage 6 entities per-mech entity.
+ Server wasting a lot of cyclings updated basic info.
+ SendEntity / predraw had replaced mech rendering, so the server itself no longer needed to care about individual part entities.
(Remember, every model in the server is an entity.)
+ client-side was ALSO having trouble keeping track of client-side mech entities, many AI units when they died were left with dangling weapon or arm models because something failed to update somewhere.

+ Recently thanks to LadyHavoc, she offered the tip that addentity() can be re-used multiple times on a single entity,  like publishing an entity to the renderer.
+ This means that any unit's predraw can just use a SINGLE entity, and swap the model, angle, origins out before each submission.

# rebuilt
+ This massive commit is a huge rebuild. All entity-component based code has been rewired to use flat entity variables like .torL_hp, etc.

+ I've also cleaned out many unused or deprecated functions, and improved Client/Server packet sending.

+ Weapon entites are now promoted to networked.

+ tanks FINALLY hug the ground, no longer 'floating' in air because the engine is axis-aligned bounding boxes.

+ I even fixed an AI bug where a killed bot failed to alert its friends on-death.

+ there are some lingering bugs that I will address, but this captures the big commit.

(only in battleMETAL do some pull requests swing wild.)

---
## [maygamalosman/Bike_ford](https://github.com/maygamalosman/Bike_ford)@[48a3358650...](https://github.com/maygamalosman/Bike_ford/commit/48a3358650f80397af2299072913ecb648ecaf43)
#### Friday 2022-07-01 20:29:50 by maygamalosman

Add files via upload

(Ford Gobike Data Exploration)
==============================

by (May Osman)
-------------------

Dataset
-------
The project consists of two parts,

The first part go through exploring the variables that exist in the Ford GoBike dataset.
i used python tools and libraries to visualize,discover the data set and make the data wrangling
process.

we start depecting the univariate variable ,bivariate variable graphs and at the end  the multivariate  graphs.

The second part will be the explanation part,
with extra discovering for more corrolation between the different variables 

  
The data contain of the main feature (trip duration)plus extra 15 feature like[
'start_time', 'end_time', 'start_station_id','start_station_name',
'start_station_latitude', 'start_station_longitude', 'end_station_id',
'end_station_name','end_station_latitude', 'end_station_longitude', 'bike_id',
'user_type', 'member_birth_year', 'member_gender', 'bike_share_for_all_trip'].

Summary of Findings
-------------------

The most important feature is trip duration ,timing and the count of the trips which is affected by other variables. 

>  the only data available is on febrauary andthe trip duration between male and female users almost similier 
>   male users show slightly longer trip duration than female
>   the older user is 144 years old 
>   the average age is 37 years old


Key Insights for Presentation
-----------------------------


1- Trip Duration takes a long range of time between 100 secs to 2000 secs 

2-Most of the trips time at 8 am and 5 pm whic are the rush hours 

3- Most of trips in san  francisco cattrain station 2& market st 10 , it is the most importat station to care with . 

4- the Male subscriber is most commen users


conclusion:
the users is in the most higer ratio for the both scriber and customer ,
but the subscriber is most biger user sample, even in the midnight when the scriber less than 100 but the customer more than 1200 user,
but the duration for the customer is higer than the scbscriber 

ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
i use the following sources in search:

https://www.geeksforgeeks.org/python-pandas-series-dt-strftime/
https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.strftime.html
https://www.datacamp.com/community/tutorials/python-count
https://www.codegrepper.com/code-examples/python/create+a+list+of+1+to+ten+values+python
https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/




thank you in advance
May

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[4d1bc1ac07...](https://github.com/mbs-octoml/mbs-tvm/commit/4d1bc1ac079b77841b1dc4c0b7a1cdf14152bc35)
#### Friday 2022-07-01 20:49:12 by Mark Shields

** Collage v2 sketch ***

- Fix rebase
- Prepare for rebase
- Move CaptureIndexInSpans to generic tvm.relay.transform
- Fix test_sub_graph.py unit tests
- Make PartitionSpecs 1:1 with Targets
- Fix tests
- Finish merging Matthew's changes
- First pass merging Matthew's changes
- finish fixing lints
- test_tensorrt.py runs
- some lint fixes while waiting
- test annotation fiddles, disable pytorch test
- fix constant handling
- update tests for new API
- Switch TensorRT BYOC integration to IRModule-at-a-time
- [bug] index out of range
- don't need InferTypeExpr
- revert unnecessary changes
- revert unnecessary changes
- fix accumulate bug
- sync with 11481
- Eta-expand tuple ars in candidate partitions
  (so measurements does not need to worry about
  constructing tuple arguments)
- Polish compiler_function_utils for splitting out
- Mark functions as extern.
- Get rid of relay.ext.cutlass
- kExternalSymbol:String ----> kExtern:Bool
- Host glitch if PlanDevices run before CollagePartition
- Fix unit test
- Make load_static_library first class python func
- Get CUTLASS going on graph executor as well as vm
- Include export_library in estimate_seconds
- Rollback DSOLibrary changes.
- Add StaticLibraryNode and switch CUTLASS to use it
  This avoids the crazy serialize/deserialize/load hackery, which I'll now remove.
- Get running again
- CUTLASS picks up all options from 'cutlass' external codegen target.
- Revert false starts with cutlass handling
- Get CUTLASS going with program-at-a-time tuning and compilation instead of
  function at a time.
- Save DSOLibraries by contents rather than by reference.
- futzing with libraries
- revert unnecessary cutlass changes
- starting unit test for dsolibrary save
- Prepare scalar changes for PR.
- Eager candidate cost measurement.
- More conv2d_cudnn.cuda training records.
- cleanup before rebase
- Use 'regular' target when build, not external codegen target
- Tuned for -libs=cudnn
- Tune before collage not during
- Bring over target changes
- Fix GetSpecName
- Try again on python target changes, this time leave check_and_update_host_consist unchanged
- Revert python target changes to try again less agressively
- Few other cleanups
- Switch to 'external codegen targets' style
- Woops, run just_tvm after collage to pick up tuning logs
- Finish tuning for rtx3070
- Run them all!
- Update tuning logs
- Share global vars in the candidate function cache
- Finished tuning mobilenet, started on resnet50.
- Include model name in logs to make sure we don't get anything mixed up
- Drop -arch=sm_80
- Fix MaxCoalesce
- Attach external_symbol to lifted functions
- Add missing node registration, but leave VisitAttrs empty for now
- Make MaxCoalesce as aggressive as possible, since simple impl did not handle sharing.
- Finish tuning resnext50
- Improve coelescing
- Account for coelesced functions when outlining final module
- Fix caching, for real this time.
- More nn.conv2d autotvm tuning records, but still not done with resnext50_32_4d.
- OutlineExternalFunction both when preparing to estimate cost and after optimal
  partitioning applied.
- Use fp16 in TensorRT only if model's 'main_dtype' is float16.
- Fix CostEstimator caching issue
- More Target cleanup (while waiting for tuning runs)
- Better logging of candidates
- Support export to ONNX
- Fix merge
- Part-way through tuning for mobilenet.
- Add resnext50_32x4d
- Lift all "Compiler" functions before estimating to ensure no Relay passes are run on them
- Still trying
- Trying to track down weird failure in conv2d compute.
- Switch tensorrt to be fully pattern & composite function based
- Combiner rule for tuple projection
- Allow build to fail in estimate_seconds
- Add mobilenetv2 and resnet50v2 to menagerie
- Update CompilationConfig to handle target refinement
- Nuke remaining uses of TargetMap in favor of CompilationConfig
  (still needs to be pushed into python side)
- Save/Load dso libraries (needed for Cutlass with separated run)
- Move models into separate file
- gpt2_extract_16 and autotvm tuning log
- Handle missing tuning log files
- fp16 support in scalars and the tensorrt runtime.
- Wrap runner in nsys nvprof if requested
- Enforce strict compile/run time separation in preparation for profiling
- Better logging of final optimal partitioning and state of all candidates
- Fix handling of tuples and InlineComposites fixup pass.
- Fix TensorRT pattern bugs
- Pass max_max_depth via PassContext
- Better logging so can quickly compare specs
- BUG: Benchmark the partitioned rather than original model!!!
- Use median instead of mean
- Back to GPT2
- Make sure all function vars have a type
- Don't extract tasks if estimating BYOC-only
  (Was double-tuning every cutlass kernel).
- Make sure cudnn pattern table is registered
- Enable cudnn, get rid of support for op-predicate based BYOC integrations
- Enable cublas
- And yet another go at pruning unnecessary candidates.
- Another go at pruning unnecessary candidates
- Fix CompositePartitionRule use
- Fix a few bugs with new TensorRT pattern-based integration
- Rework RemoveSubCandidatesCombinerRule for soundness
- Better logging
- Bug fixes
- Implement critical nodes idea for avoiding obviously unnecessary candidates
- Promote DataflowGraph from alias to class so can cache downstream index set
- Quick check to avoid unioning candidates which would create a cycle
- Host out CandidatePartitionIndex and add rules to avoid small candidates subsumed by containing candidates
- GetFunction can legitimately return nullptr
- rename tuning log
- Support for int64 literals
- Switch GPT2 to plain model
- Fix library cloberring issue for cutlass
- actually checkin 'built in' tuning log (covers mnist & gpt2 only)
- trying to debug gpt2
- Update TargetKind attribute name
- working through gpt2 issues
- checkin tuning records for MNIST (with hack to not retry failed winograd)
- Autotvm tuning disabled if log file empty (default)
- Autotvm tuning during search working
- tune during search
  (but does not load tuned records after search!)
- About to add tuning to estimate_seconds
- Split out the combiner rules & make them FFI friendly
- Rework comments
- Estimate IRModule instead of Function (closer to meta_schedule iface)
- Add 'host' as first-class partitioning spec
  (Avoids special casing for the 'leave behind for the VM' case)
- Move CollagePartitioner to very start of VM compiler flow (not changing legacy)
- Fix bugs etc with new SubGraph::Rewrite approach
  Ready for updating RFC to focus on partitioning instead of fusion.
- Working again after partition<->fusion split.
- Add PrimitivePartitionRule
- Refactor SubGraph Extract/Rewrite
- Rename kernel->partition, fusion->partition
- Next: make nesting in "Primitive" an explicit transform
- respect existing target constraints from device planner
- make 'compiler' and 'fusion_rule' attributes avail on all target kinds
- moved design to tvm-rfcs, https://github.com/apache/tvm-rfcs/pull/62
- incorporate comments
- avoid repeated fusion
- fix trt type checking
- better logs
- pretty print primitive rules
- fix tensorrt
- multiple targets per spec
- don't extract candidate function until need cost
  Need to bring CombineByPrimitives back under control since lost depth limit.
- cleaned up fusion rule names
- added 'fuse anything touching' for BYOC
- Finish dd example
- Add notion of 'MustLower', even if a candidate fires may still need to consider
  leaving node behind for VM (especially for constants).
- starting example
- finished all the dd sections
- documentation checkpoint
- docs checkpoint
- more design
- starting on dd
- runs MNIST with TVM+CUTLASS+TRT
- cutlass function-at-a-time build
- need to account for build_cutlass_kernels_vm
- move cutlass tuning into relay.ext.cutlass path to avoid special case
- add utils
- don't fuse non-scalar constants for tvm target.
- stuck on cuda mem failure on conv2d, suspect bug in main
- where do the cutlass attrs come from?
- running, roughtly
- pretty printing, signs of life
- wire things up again
- Switch SubGraph and CandidateKernel to TVM objects
- naive CombineByKindFusionRule, just to see what we're up agaist
  Will switch to Object/ObjectRef for SubGraph and CandidateKernel to avoid excess copying.
- preparing to mimic FuseOps
- rework SubGraph to use IndexSet
- rough cut at MaximalFusion
- split SubGraph and IndexSet in preparation for caching input/output/entry/exit sets in SubGraph.
- top-down iterative handling of sub-sub-graphs
- about to give up on one-pass extraction with 'sub-sub-graphs'
- Add notion of 'labels' to sub-graphs
- Rework FusionRules to be more compositional
- partway through reworking fusion rules, broken
- SubGraph::IsValid, but still need to add no_taps check
- dataflow rework, preparing for SubGraph::IsValid
- explode into subdir
- mnist with one fusion rule (which fires twice) working
- switch to CandidateKernelIndex
- Confirm can measure 'pre-annotated' primitive functions
- checkpoint
- stuff
- more sketching
- dominator logging

---
## [tumenicooks/tumenicooks](https://github.com/tumenicooks/tumenicooks)@[1e41625666...](https://github.com/tumenicooks/tumenicooks/commit/1e41625666b63cdf0e68dbfa70b2e997b90f026c)
#### Friday 2022-07-01 21:27:44 by tumenicooks

Create Day 4: rockpaperscissors

cuz fuck logic amirite, came up with a simpler solution than using >, <, etc etc operators. Was too lazy to change code towards lecture solution cuz I got everything running anyway, including the invalid number prompt.

Also skipped a day cuz literally dropped ded and slept the entire night yesterday

---

