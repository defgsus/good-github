## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-16](docs/good-messages/2022/2022-07-16.md)


1,686,984 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,686,984 were push events containing 2,213,362 commit messages that amount to 126,819,079 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [Jolly-66/Skyrat-tg](https://github.com/Jolly-66/Skyrat-tg)@[a1fe30230b...](https://github.com/Jolly-66/Skyrat-tg/commit/a1fe30230baaef9736cebee442c902180ff85ce5)
#### Saturday 2022-07-16 00:02:56 by SkyratBot

[MIRROR] [MDB Ignore] Shifts all (sane) varedited signs to directionals  [MDB IGNORE] (#14549)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

* updates all our maps

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [heterosys/llvm-nightly](https://github.com/heterosys/llvm-nightly)@[7c51f02eff...](https://github.com/heterosys/llvm-nightly/commit/7c51f02effdbd0d5e12bfd26f9c3b2ab5687c93f)
#### Saturday 2022-07-16 00:04:41 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could exposed a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [rtyh12/roll-of-the-dice](https://github.com/rtyh12/roll-of-the-dice)@[4a526ac3cf...](https://github.com/rtyh12/roll-of-the-dice/commit/4a526ac3cf295ac774c33f315e7abd5554a90eb6)
#### Saturday 2022-07-16 00:32:24 by Mihai Verzan

Add Json testing stuff (HOPE IT DOESNT BREAK SHIT)

boy howdy sure do hope it doesn't break everything lol sorry if it does

rip

---
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[6fe0683a7b...](https://github.com/CursedBirb/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Saturday 2022-07-16 01:12:36 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---
## [fakhrads/android_kernel_samsung_a50-common](https://github.com/fakhrads/android_kernel_samsung_a50-common)@[7b5b087f82...](https://github.com/fakhrads/android_kernel_samsung_a50-common/commit/7b5b087f82ef1de3382d03064e0952e11a4663b4)
#### Saturday 2022-07-16 01:21:39 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, tbsvc, and typec as they do not exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [arizvisa/dotfiles](https://github.com/arizvisa/dotfiles)@[eb65b98a43...](https://github.com/arizvisa/dotfiles/commit/eb65b98a43ff6efd2f789c96fb4f6b8f67c7f023)
#### Saturday 2022-07-16 03:39:56 by Ali Rizvi-Santiago

cargo is completely fucking stupid..i can't believe they hardcoded 4 profiles, have their own config file, and don't fucking let you set a default one.
even dune lets you fucking do this, and i thought dune was fucking miserable. boy, do i stand fucking corrected.

---
## [newstools/2022-daily-post-nigeria](https://github.com/newstools/2022-daily-post-nigeria)@[b7d512481f...](https://github.com/newstools/2022-daily-post-nigeria/commit/b7d512481f2723e07674aa1a26f6dcedac36fc41)
#### Saturday 2022-07-16 03:42:25 by Billy Einkamerer

Created Text For URL [dailypost.ng/2022/07/15/i-begged-god-to-take-my-life-at-20-adekunle-gold-reveals-frustrating-times/]

---
## [iKeramat/msm-4.19](https://github.com/iKeramat/msm-4.19)@[13ab91c37d...](https://github.com/iKeramat/msm-4.19/commit/13ab91c37d9661ffb65a72002647c477034ebbb1)
#### Saturday 2022-07-16 04:07:19 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>

---
## [purplefoxy27/CHOMPStation2](https://github.com/purplefoxy27/CHOMPStation2)@[4704df506b...](https://github.com/purplefoxy27/CHOMPStation2/commit/4704df506bfccd3f4ef9d75a3cf1a4f6f63ca4e3)
#### Saturday 2022-07-16 04:23:30 by Victor Zisthus

Massive Broad Scope Changes

NEW STUFF
Added in a custom thermal regulator for the wilderness shelter.

Southern Cross now has a Bluespace Radio!

Added a subspace radio, and allowed it to be made in the autolathe.

ALL MAPS:
Added lighting to dark areas. Did not touch lighting in maintenance areas.

DECK ONE:
Adjusted exterior lattice network.

DECK TWO:
Fixed a bug with Shieldgen.

Moved the Engine SMES powernet sensor off of a pump.

Removed the second freezer air alarm to prevent pressure alarms from going off every shift. (I got my revenge on the laws of thermodynamics with the new custom regulator, don't worry.)

Put a new subspace radio in the bar.

Adjusted exterior lattice network.

DECK THREE:
Removed a duplicate shower curtain in one of the dorm rooms.

SURFACE OUTPOST:
This PR will cause a conflict with #4061 but I am willing to help Enzo with the project as needed~

A friend and boy waits for the miners every shift.

Moved some stuff around at surface S&R per a reported issue. FIXES #4072

Fixed a bug with the hunting lockers and doors. Security should have access to them now.

Fixed a bug with the Hunting Pen shield generators.

CAVES:
Cleared the rock around the outpost, added a new door to allow moving around the exterior.

EXPLO CARRIER:
Put the new Bluespace Radio on the table in the gateway prep room.

WILDERNESS + SKY ISLANDS:
Overhauled the wilderness shelter! It now has a crew quarters room, First Aid, a second floor, and a utility room. It's only powered by a single advanced RTG that's barely able to keep up with power demand when the place is abandoned, so be sure to bring resources from mining and science to get the other RTG's up and running!

---
## [VioletN/orbstation](https://github.com/VioletN/orbstation)@[fdd8036140...](https://github.com/VioletN/orbstation/commit/fdd80361406f7b9ff8568237a933f9926b527c28)
#### Saturday 2022-07-16 05:35:25 by BluBerry016

Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because (#68126)

Drips the SHIT out of the SBC Starfury while not completely overhauling it. Touches everything NOT in engineering or southward (because I love how scuffed that part is and refuse to touch it on principle) - Also converts one map varedit into a real boy subtype, and moves tiny fans to their own file.

Mandatory disclosure on the gameplay changes:
Fighters 1 and 3 are now NOT in the hangar, and are now attached to the formerly unused gunnery rooms.
Cryo now works. Yeah. I know.
You can actually open the anesthetic closet now.
Everyone now shares three spawners. This doesn't reduce the amount of people who can play when this rolls, as I've adjusted var/uses in accordance: it just reduces clutter.
A few of the horizontal double airlocks have been compacted into glass_large airlocks.
The bar windows now actually have grilles like they were meant to.
Four turbines have shown up. They aren't functional*, they just look like gunnery and conveniently fit in the spots. I'm sure this is space OSHA compliant.
The map is ever so slightly smaller, vertically. This should distance us from an edge case where somehow all space levels are too cluttered for this to spawn properly, for the time being.

*Technically there's nothing stopping you from using them besides the amount of time it'd take for the operatives to kick your ass

This map was originally designed wayyy back before we even had the computer sprites we have now, (#27760 if you want to see SOUL) and it shows. While it will never have it's SM again, we can at least make the thing much nicer to look at.

---
## [nnnaojp/boxing_color_timer](https://github.com/nnnaojp/boxing_color_timer)@[eb3f8d4f2b...](https://github.com/nnnaojp/boxing_color_timer/commit/eb3f8d4f2b40c6afccbb19c4df3ba8f016b5f817)
#### Saturday 2022-07-16 07:16:49 by gaki

**Privacy Policy**

nnnao built the BOXING COLOR TIMER app as a Free app. This SERVICE is provided by nnnao at no cost and is intended for use as is.

This page is used to inform visitors regarding my policies with the collection, use, and disclosure of Personal Information if anyone decided to use my Service.

If you choose to use my Service, then you agree to the collection and use of information in relation to this policy. The Personal Information that I collect is used for providing and improving the Service. I will not use or share your information with anyone except as described in this Privacy Policy.

The terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, which are accessible at BOXING COLOR TIMER unless otherwise defined in this Privacy Policy.

**Information Collection and Use**

For a better experience, while using our Service, I may require you to provide us with certain personally identifiable information. The information that I request will be retained on your device and is not collected by me in any way.

The app does use third-party services that may collect information used to identify you.

Link to the privacy policy of third-party service providers used by the app

*   [Google Play Services](https://www.google.com/policies/privacy/)

**Log Data**

I want to inform you that whenever you use my Service, in a case of an error in the app I collect data and information (through third-party products) on your phone called Log Data. This Log Data may include information such as your device Internet Protocol (“IP”) address, device name, operating system version, the configuration of the app when utilizing my Service, the time and date of your use of the Service, and other statistics.

**Cookies**

Cookies are files with a small amount of data that are commonly used as anonymous unique identifiers. These are sent to your browser from the websites that you visit and are stored on your device's internal memory.

This Service does not use these “cookies” explicitly. However, the app may use third-party code and libraries that use “cookies” to collect information and improve their services. You have the option to either accept or refuse these cookies and know when a cookie is being sent to your device. If you choose to refuse our cookies, you may not be able to use some portions of this Service.

**Service Providers**

I may employ third-party companies and individuals due to the following reasons:

*   To facilitate our Service;
*   To provide the Service on our behalf;
*   To perform Service-related services; or
*   To assist us in analyzing how our Service is used.

I want to inform users of this Service that these third parties have access to their Personal Information. The reason is to perform the tasks assigned to them on our behalf. However, they are obligated not to disclose or use the information for any other purpose.

**Security**

I value your trust in providing us your Personal Information, thus we are striving to use commercially acceptable means of protecting it. But remember that no method of transmission over the internet, or method of electronic storage is 100% secure and reliable, and I cannot guarantee its absolute security.

**Links to Other Sites**

This Service may contain links to other sites. If you click on a third-party link, you will be directed to that site. Note that these external sites are not operated by me. Therefore, I strongly advise you to review the Privacy Policy of these websites. I have no control over and assume no responsibility for the content, privacy policies, or practices of any third-party sites or services.

**Children’s Privacy**

These Services do not address anyone under the age of 13. I do not knowingly collect personally identifiable information from children under 13 years of age. In the case I discover that a child under 13 has provided me with personal information, I immediately delete this from our servers. If you are a parent or guardian and you are aware that your child has provided us with personal information, please contact me so that I will be able to do the necessary actions.

**Changes to This Privacy Policy**

I may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes. I will notify you of any changes by posting the new Privacy Policy on this page.

This policy is effective as of 2022-07-16

**Contact Us**

If you have any questions or suggestions about my Privacy Policy, do not hesitate to contact me at gakiwork@gmail.com.

This privacy policy page was created at [privacypolicytemplate.net](https://privacypolicytemplate.net) and modified/generated by [App Privacy Policy Generator](https://app-privacy-policy-generator.nisrulz.com/)

---
## [toufune/kernel_xiaomi_juice](https://github.com/toufune/kernel_xiaomi_juice)@[704151b8c0...](https://github.com/toufune/kernel_xiaomi_juice/commit/704151b8c09b0e0cc5e1bb398c5a4cc704808af9)
#### Saturday 2022-07-16 09:01:27 by Linus Torvalds

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6e935098e7...](https://github.com/mrakgr/The-Spiral-Language/commit/6e935098e7450fbadb00c06ecd3f530861e5614a)
#### Saturday 2022-07-16 10:14:56 by Marko Grdinić

"9:05am. I am up. I actually got into BG2 yesterday and did not notice the time until it was 11:30pm. I went to bed a bit later than usual and am feeling groggy.

9:10am. Note that I got this after having my application rejected, so the other party actually put some thought into the reply.

> At some point I'd love to build an ML version of algo model what we are working on but that's probably 9 months away on the roadmap.
> In the meantime we are working away building out the Haskell platform and we can't afford to spend what to us right now is big money on someone that cannot come in and immediately upgrade what we have from a Haskell perspective.
> Perhaps we can talk in a year if you are back on the market then?

Got a reject from the Haskell place, probably because there is nothing Haskell related is on my resume. I actually thought about this position during the night, and thought how the interview would go, and it gave me flashbacks to how much pain in the ass getting anything done in Haskell was. For this interview I'd need to prepare so I know how read and write from arrays and such, as well as use dictionaries. There are better people for this position than me, and they actually like using Haskell. It is not worth either my or the company's time to delve into this.

If this was an F# position, I'd strongly object, but let me move on here.

9:25pm. I did a diplomatic reply agreeing and telling them that while I'd be able to use Haskell proficiently, they'd be better off finding somebody who enjoys working in it.

That is one position down. I'll have to wait for a reply from the other 7. It has only been a day so it is not surprising I got nothing back yet.

Though it was a reject, it was from a real person and for sensible reaosns so I can accept it.

9:40am. Right now I am still chilling. Mato and Kiling Bites are out. Let me have those and then I am going to get started on playing with the free tier.

10:15am. Let me start. I've spent the whole morning doing nothing and I am still groggy.

10:20am. Stop reading BG2 guides and focus. I want to get my AWS proficiency up.

https://aws.amazon.com/getting-started/?sc_icampaign=grizzly_getting-started-center_default-ed&sc_ichannel=ha&sc_icontent=awssm-evergreen-default&sc_iplace=ed&trk=ha_awssm-evergreen-default

Let me focus on this. How about I aim for Hello World on AWS Lambda? After that I'll look into containers.

https://www.cloudwards.net/cloud-computing-statistics/
> The “cloud.” What was once a trendy, science fiction–sounding buzzword has become an inescapable part of our everyday personal and professional lives. Even though we understand what the cloud does, the way it works and how it is evolving is a far more complex subject. This list of cloud computing statistics will give you an idea of just how significant it really is.

> Based on market share, the largest cloud computing company in the world is Amazon Web Services. A subsidiary of Amazon, AWS currently holds 31 percent of the market, followed by Microsoft Azure at 20 percent and Google Cloud at seven percent. Founder Jeff Bezos attributes AWS’ enormous success to its seven-year head start before facing serious competition. This allowed AWS to evolve at a more leisurely pace and to develop more functionalities.

I wanted to find that out. It seems AWS has a solid lead over others.

> Cloud gaming works similarly to streaming services; rather than installing a video game on your computer, you can stream it to your display instead. In 2020, the global cloud gaming market was worth $470 million. With a predicted CAGR of 48.2 percent, it is expected that it will reach $7.24 billion in revenue by 2027.20 Read our online gaming statistics to learn more.

Does this really make sense for gaming?

10:35am. Ok, stop reading that.

https://aws.amazon.com/getting-started/?sc_icampaign=grizzly_getting-started-center_default-ed&sc_ichannel=ha&sc_icontent=awssm-evergreen-default&sc_iplace=ed&trk=ha_awssm-evergreen-default

Let me focus on some light tutorials here. I had such good sleep lately, but blew it yesterday by going over 11pm by accident.

https://aws.amazon.com/getting-started/guides/setup-environment/?pg=gs&sec=gtkaws

Let me just do this. I'll make it my goal to access the CLI. Let me sign in.

https://aws.amazon.com/getting-started/guides/setup-environment/module-one/

It seems I do not have an AWS account just yet, only an Amazon one. Let me make one.

10:50am. https://aws.amazon.com/getting-started/guides/setup-environment/module-one/

This is complicated, it is already asking me for my card. For reasons, I'll have to wait a few hours to get this done.

Hmmmm, instead of my father's what if I used my own card? Let me check the expiration dates.

> Thank you for creating an Amazon Web Services (AWS) account. For the next 12 months, you'll have free access to all AWS services within the limits of the Free Tier.

I am only on step 3, but I got a confirmation email. Let me try logging in.

Oh it does work. I guess I can leave the later steps for later. Let me just check out my cards.

This is a good sign that I should get my bank accounts in order. I have a bunch of money in my wallet just sitting there uselessly, and it is time to make use of it.

10:55am. I have a debit card, but it expired like a month ago. I'll have to make a trip to the bank and order a new one.

There is no way around it. It is time to get professional. But for now let me just see if I can make use of the free tier.

https://aws.amazon.com/getting-started/guides/setup-environment/module-two/?refid=ha_awssm-evergreen-default

Nevermind doing this right now. I'll deal with it after I complete registration.

https://aws.amazon.com/getting-started/guides/setup-environment/module-three/?refid=ha_awssm-evergreen-default

Skip the CLI for now.

> This will use a t3.micro instance, which is covered by the AWS Free Tier for the first 12 months. The --automatic-stop-time-minutes will automatically shut down the instance after the period of minutes has elapsed which will help keep you within the 750h / month free tier. The above command will return the environment ID of your Cloud9 environment in the following format:

24*30 = 720.

So the only way to exceed the 750h/month limit is to spin off multiple instances. I guess there will be no restrictions on that then. The free tier is good enough to learn from. It if were 750m instead, I'd be in trouble.

11:10am. I'll have to set up the CLI and the console, but I want to go even simpler.

https://aws.amazon.com/getting-started/hands-on/run-serverless-code/?pg=gs&sec=lyfa

Let me do the serverless hello world.

> Recently we released the .NET 6 managed runtime for Lambda. Along with the new Lambda runtime we have also been working on a new framework for writing .NET 6 Lambda functions called Lambda Annotations. The Annotations framework makes the experience of writing Lambda feel more natural in C#. It also takes care of synchronizing the...

It seems .NET 6 has some stuff for Lambda? Since I am at it, I should check out what F# has for this.

11:15am. Yeah this is it. I was stuck as a programmer since last year, but breaking new ground is always exciting. Forget the interviews until I get the bank account in order.

https://aws.amazon.com/blogs/developer/introducing-net-annotations-lambda-framework-preview/

> However, source generators are only available for C# which means that, unfortunately, the Annotations framework cannot be used for Lambda functions written using F#.

11:25am. I realized an optimization I could make to the ref counter. As long as the function args only have suppressed decrefs, it is safe to eliminate them. This would make tail recursive loops significantly more effcient.

In fact, this would apply to all variables. Incdec elimination is always viable as long as the dec is suppresed for all branches.

11:30am. This is a good idea. I'd need to make a pass to propagate the suppressed variables backwads, use that to eliminate the increfs, and then forward again to eliminate the decrefs. But once I had that I'd have very efficient tail call loops even with ref counting. I'll do it if I have time. For now it is not important, let me focus on AWS.

11:40am. Now I am thinking about how to do that optimization. I'd need to use two sets, one for propagating suppressed vars and one for propagating decrefed vars. At every let statement, unboxing and function start I'd then incref eliminate those...

Actually, is there any need to propagate the suppressed vars?

Wouldn't it be enough to just propagate the decrefed vars and only do incref elimination on vars not in that set? There are only two kinds of decrefs, suppressed and regural. If they are not regular then they must be suppressed.

Not to mention, there are in fact 3 types vars, the ones on the LocalReturnData ends, but those should also count as suppressed for the purpose of this optimization pass.

By doing things like so, I'd save myself a lot of effort. There is really no reason not to do this.

11:45am. I'll leave the idea aside. I'll make a note linking to this line count.

11:50am. Hmmm, no I thought it might work for any statement but I can see that being broken.

Right now I am thinking what if I passed in an array and an item from that array as two separate args while the optimization is active...it would work.

11:55am. Yeah, focus me. I need to get back to AWS. Just why did I not get the Hello World done?

Agh, no, the optimization would not work in all cases. If I do this optimization I could potentially be passing args with a ref count of 0 in other functions. And those might increment and then decrement it, free it out of turn. Nasty. Yeah, it seems really obvious now that I see this case.

So is the problem then only the vars passed to other funs? Well, there is also the args passed into arrays and pretty much everything.

I do not want to be passing ref count 0 objects around. It is dangerous.

Just forget about it. I can use regular loops for performance. Ref counting is hard to make efficient.

12:05pm. I click on Lambda and ...

> Thanks for signing up for Amazon Web Services. If we have directed you to this page, then you have not finished registering. Make sure you have done the following:

Maybe it is just as well that I took the time to think through that optimization.

12:10pm. I can't even get to step 2 right now. I'll try registering using my fathers card once he gets back from work and just switch to mine once I get the bank account reactivated.

12:15pm. Let me have breakfast here."

---
## [HonoreDB/cockroach](https://github.com/HonoreDB/cockroach)@[cc5bde5c7a...](https://github.com/HonoreDB/cockroach/commit/cc5bde5c7abdf732695bc798afb47c6053e922e7)
#### Saturday 2022-07-16 12:07:46 by craig[bot]

Merge #82440

82440: admission,storage: introduce flush tokens to constrain write admission r=tbg,irfansharif a=sumeerbhola

In addition to byte tokens for writes computed based on compaction rate
out of L0, we now compute byte tokens based on how fast the system can
flush memtables into L0. The motivation is that writing to the memtable,
or creating memtables faster than the system can flush results in write
stalls due to memtables, that create a latency hiccup for all write
traffic. We have observed write stalls that lasted > 100ms.

The approach taken here for flush tokens is straightforward (there is
justification based on experiments, mentioned in code comments):
- Measure and smooth the peak rate that the flush loop can operate on.
  This relies on the recently added pebble.InternalIntervalMetrics.
- The peak rate causes 100% utilization of the single flush thread,
  and that is potentially too high to prevent write stalls (depending
  on how long it takes to do a single flush). So we multiply the
  smoothed peak rate by a utilization-target-fraction which is
  dynamically adjusted and by default is constrained to the interval
  [0.5, 1.5]. There is additive increase and decrease of this
  fraction:
  - High usage of tokens and no write stalls cause an additive increase
  - Write stalls cause an additive decrease. A small multiplier is used
    if there are multiple write stalls, so that the probing falls
    more in the region where there are no write stalls.

Note that this probing scheme cannot eliminate all write stalls. For
now we are ok with a reduction in write stalls.

For convenience, and some additional justification mentioned in a code
comment, the scheme uses the minimum of the flush and compaction tokens
for writes to L0. This means that sstable ingestion into L0 is also
subject to such tokens. The periodic token computation continues to be
done at 15s intervals. However, instead of giving out these tokens at
1s intervals, we now give them out at 250ms intervals. This is to
reduce the burstiness, since that can cause write stalls.

There is a new metric, storage.write-stall-nanos, that measures the
cumulative duration of write stalls, since it gives a more intuitive
feel for how the system is behaving, compared to a write stall count.

The scheme can be disabled by increasing the cluster setting
admission.min_flush_util_fraction, which defaults to 0.5 (corresponding
to the 0.5 lower bound mentioned earluer), to a high value, say
10.

The scheme was evaluated using a single node cluster with the node
having a high CPU count, such that CPU was not a bottleneck, even
with max compaction concurrency set to 8. A kv0 workload with high
concurrency and 4KB writes was used to overload the store. Due
to the high compaction concurrency, L0 stayed below the unhealthy
thresholds, and the resource bottleneck became the total bandwidth
provisioned for the disk. This setup was evaluated under both:
- early-life: when the store had 10-20GB of data, when the compaction
  backlog was not very heavy, so there was less queueing for the
  limited disk bandwidth (it was still usually saturated).
- later-life: when the store had around 150GB of data.

In both cases, turning off flush tokens increased the duration of
write stalls by > 5x. For the early-life case, ~750ms per second was
spent in a write stall with flush-tokens off. The later-life case had
~200ms per second of write stalls with flush-tokens off. The lower
value of the latter is paradoxically due to the worse bandwidth
saturation: fsync latency rose from 2-4ms with flush-tokens on, to
11-20ms with flush-tokens off. This increase imposed a natural
backpressure on writes due to the need to sync the WAL. In contrast
the fsync latency was low in the early-life case, though it did
increase from 0.125ms to 0.25ms when flush-tokens were turned off.

In both cases, the admission throughput did not increase when turning
off flush-tokens. That is, the system cannot sustain more throughput,
but by turning on flush tokens, we shift queueing from the disk layer
the admission control layer (where we have the capability to reorder
work).

Screenshots for early-life: Flush tokens were turned off at 22:32:30. Prior to that the flush utilization-target-fraction was 0.625.
<img width="655" alt="Screen Shot 2022-06-03 at 6 35 14 PM" src="https://user-images.githubusercontent.com/54990988/171970564-ba833e1f-b6e2-4fcd-9ee2-25228341065c.png">
<img width="663" alt="Screen Shot 2022-06-03 at 6 35 28 PM" src="https://user-images.githubusercontent.com/54990988/171970574-13e6114a-2467-48e2-a238-3b01ea32a5d6.png">

Screenshots for later-life: Flush tokens were turned off at 22:03:20. Prior to that the flush utilization-target-fraction was 0.875.
<img width="665" alt="Screen Shot 2022-06-03 at 6 07 50 PM" src="https://user-images.githubusercontent.com/54990988/171970732-09b60827-7687-46de-964e-a9f97388c4fc.png">
<img width="658" alt="Screen Shot 2022-06-03 at 6 08 03 PM" src="https://user-images.githubusercontent.com/54990988/171970738-efe7a1fd-cbfd-450d-a3ac-06f681b1d190.png">

These results were produced by running
```
roachprod create -n 2 --clouds aws  --aws-machine-type=c5d.9xlarge --local-ssd=false --aws-ebs-volume-type=gp2 sumeer-io
roachprod put sumeer-io:1 cockroach ./cockroach
roachprod put sumeer-io:2 workload ./workload
roachprod start sumeer-io --env "COCKROACH_ROCKSDB_CONCURRENCY=8"
roachprod run sumeer-io:2 -- ./workload run kv --init --histograms=perf/stats.json --concurrency=1024 --splits=1000 --duration=30m0s --read-percent=0 --min-block-bytes=4096 --max-block-bytes=4096 {pgurl:1-1}
```

Fixes #77357

Release note (ops change): Write tokens are now also limited based on
flush throughput, so as to reduce storage layer write stalls. This
behavior is enabled by default. The cluster setting
admission.min_flush_util_fraction, defaulting to 0.5, can be used to
disable or tune flush throughput based admission tokens, for writes
to a store. Setting to a value much greater than 1, say 10, will
disable flush based tokens.

Co-authored-by: sumeerbhola <sumeer@cockroachlabs.com>

---
## [ThomasAdam/got-portable](https://github.com/ThomasAdam/got-portable)@[8a35f56cb4...](https://github.com/ThomasAdam/got-portable/commit/8a35f56cb42a2c9617008c6e68cccf9b62939243)
#### Saturday 2022-07-16 12:29:52 by Tracey Emery

import gotwebd

thread fcgi response to client for rendering in browser as data is returned

fix potential problem with a stuck loop if the client is hammering the server with random clicks and stop/restarts

render our index! WOOHOO! small var refactoring.

fcgi.c to handle all clean-up, various error clean-up

remove output used to trace down got bug

temporarily stop overloading a socket, but a better solution needs to be found

return on fcgi_gen_response, so we can track if a client is writable or not
this stops page creation when the client is unavailable

remove old comments

enable profile building, although, i don't think this works thoroughly in a priv/proc daemon

catch more errors

correctly count repos

remove temp logger

we don't need to start our responder thread so early. move it to fcgi.c and start when we start processing html

kill the unneeded thread, stop queueing responses, and just write to clients immediately

clean up some memory leaks and dead stores

rework querystring so an error can be displayed instead of showing the index on
querystring error

get framework in place for the rest of the content

add server struct to response struct

bo last commit

get back a usable gotweb. not sure what i was thinking yesterday

properly move our structs around this time

remember index page for sitelink, fix leak

unused var is annoying, so stop it for now. don't forget to change this!

style

briefs nearly completed.

finish briefs output

add briefs to summary

cleanup some html

properly retrieve next and previous commit ids for list navigation

follow naddy's stailq macro change

we will never have a previous link on the summary page

goto correct label, so we get a previous link on the last page of briefs

don't wrap short line

simplify got_get_repo_commits code

start rendering a diff

start rendering a diff

this was by accident

finish diff output

functions cleanup

prepare for fd request

that was a stupid idea, just flush the priv_fd

bo that too. that won't work eith with append in mkstemp

that isn't going to work

actually zero out the priv_fd

missed seek to beginning of file was overwriting first line of diff

fsync our fd as well

add link to repo path by sitelink and add back verbose fcgi debugging that was removed

add modest write heuristics to fcgi_send_response

fix dead assignments and XXX comment where a leak is happening that I can't find right now

there was no leak. stsp is brilliant and knew it was the cache growing

prevent double-free, render prettier err output if we can

remove unused variables

correctly fix double-free

fix gotwebd to build with main's changes after rebase

fix double-free

don't error on index if pack files missing and fixup some error handling

render commits

finish up tag briefs and start the tag page

finish up tag page

unbreak TAGS and SUMMARY actions

grab the correct tag from the queue

unbreak TAGS and SUMMARY actions again

update some error handling

clean up unneeded code and start tree output

render tree

render branches

remove tags from summary if there aren't any

fix tree div structure and start blob render

render blob

render blame

fix tree href in briefs

clean up some css

add headref to querystrings

load correct commit for tree and diff

fixup some error output

update some copyright dates

add full SNI support

rm debug line found by Lucas6023, notified via IRC. thanks!!

fix tree

fix crash when querystring is manipulated to not have a commit id in certain
instances. also break a stuck while loop on client error.

fix for new got_object_id_by_path arguments

rebase and fix

prep for multiple fds per socket, instead of just one

fix overlooked shift/reduce conflicts

backout priv_fds as a list. after discussion with stsp, an array and length are the better direction

prepare array of fds to pass into got functions

make a new set of pack fds, which will be passed to got_repo_open

work with new pack_fds in got_repo_open

give output when no tags exist

escape html in blame output

change files listed in tree view to show blob, file commits, and blame, instead of blob, blob, blame. idea from mp4 on irc. this is way more handy.

stop populating the queue from the headref and figure out previous commit id
while iterating. this should reduce some overhead.

actually purge our sockets instead of not using the function

start work with new blob

rm volatile

use new diff

change func names

no more temp files

increase blame number line width

set content-type to text/plain so firefox won't download files

rm test infra for now

account for -Wwrite-strings

fix for sigs and algorithm choice

clean up some leaks and other mistakes

---
## [Jangsoodlor/JPG-to-PDF-with-CLI](https://github.com/Jangsoodlor/JPG-to-PDF-with-CLI)@[4ce88fab4d...](https://github.com/Jangsoodlor/JPG-to-PDF-with-CLI/commit/4ce88fab4d3077fb72a50edf9e2a1ee0b7ea2a78)
#### Saturday 2022-07-16 12:37:24 by Jangsoodlor

I really love Nanahira.

Like, a lot. Like, a whole lot. You have no idea. I love her so much that it is inexplicable, and I'm ninety-nine percent sure that I have an unhealthy obsession. I will never get tired of listening that sweet, angelic voice of hers. It is my life goal to meet up her with her in real life and just say hello to her.

I fall asleep at night dreaming of her holding a personal concert for me, and then she would be sorry tired that she comes and cuddles up to me while we sleep together. If I could just hold her hand for a brief moment, I could die happy. If given the opportunity, I would lightly nibble on her ear just to hear what kind of sweet moans she would let out. Then, I would hug her while she clings to my body hoping that I would stop, but I only continue as she moans louder and louder.

I would give up almost anything just for her to look in my general direction. No matter what I do, I am constantly thinking of her. When I wake up, she is the first thing on my mind. When I go to school, I can only focus on her. When I go come home, I go on the computer so that I can listen to her beautiful voice. When I go to sleep, I dream of her and I living a happy life together. She is my pride, passion, and joy. If she were to call me "Onii-chan," I would probably get diabetes from her sweetness and die.

I wish for nothing but her happiness. If it were for her, I would give my life without any second thoughts. Without her, my life would serve no purpose. I really love Nanahira.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2c9f09a1a9...](https://github.com/mrakgr/The-Spiral-Language/commit/2c9f09a1a972004ac240d73392f9ad986502853b)
#### Saturday 2022-07-16 12:47:47 by Marko Grdinić

"12:40pm. Done with breakfast.

12:55pm. Let me finish my reading and I will resume?

Doing what exactly? Well, I just browse the AWS site for a bit. Right now my focus is extremely low, I really need to get some practical experience to digest the book learning. But until I get access to my financials sorted out, it can't be helped.

I'll do a tour of AWS and Azure, track down that ML related cloud service. It is going to be a bit tedious, maybe I'll take a break earlier today than usual. Who knows how long this will take.

If I let the current crop of applications pass and apply again in a few months instead that is fine.

1:20pm. I've started. My tension is uselessly high right now.

https://aws.amazon.com/getting-started/guides/deploy-webapp-ec2/module-one/

This is too rough to just read. It too boring unless I can follow along.

Let me change gears and check out Azure.

https://docs.microsoft.com/en-us/learn/azure/

https://customers.microsoft.com/en-us/story/1498781140435260527-forza-horizon-5-crosses-finish-line-fueled-by-azure-kubernetes-service
> When it launched, Forza Horizon 5 saw more than 10 million concurrent players—the biggest first week in Xbox Game Studios history—drive across vibrant, virtual landscapes and face off in thrilling tournaments and challenges. Forza Horizon 5 is also a stunning win behind the scenes, where Azure platform as a service (PaaS) provides a virtual crew, and a Windows-based container architecture adapts to changing demand at warp speed.

> "With our compute, storage, and data stacks all on Azure, our engineering teams can now spend more time building new experiences for our players rather than managing our infrastructure."

https://youtu.be/2vMEQ5zs1ko
Kubernetes vs. Docker: It's Not an Either/Or Question

https://azure.microsoft.com/en-us/free/

Free Azure account for 30 days. Maybe this thing won't ask me for my credit card.

> The answer came from a technology that ForzaTech didn’t expect—Kubernetes, the popular container orchestration platform. “We had never used container technology whatsoever. There was never any reason to even look into Kubernetes,” Hennessy recalls. But the team leaned into the curve. “Within a month, basically we had converted our services over to AKS and had everything running.”

> AKS also allowed the team to iterate much faster during stress testing, a mission-critical step in preparing for the big launch day. Before moving to AKS, it could take ForzaTech developers half an hour to swap out old images on their VMs and prepare them for load. In AKS, this process takes seconds. The extra speed enables the team to instantly make repairs, overcome roadblocks, and scale as needed. In addition, the team can script cluster updates ahead of time, adding flexibility and agility to the demanding stress tests.

> The Forza Horizon 5 architecture includes 17 core services that run in AKS. Among them, the leaderboard service tells users where they rank, while the user-generated content (UGC) service supports the ability for players to upload photos and other content. The auction house service enables players to sell cars to each other, and the analytics service collects game and player telemetry used in reports.

My current level of concurrency skills is not enough. Commercial software is all about scale. I need to broaden my knowledge if I really want to be worthy of a 200k/year salary. I want to be able to do all of the above on my own.

It is not actually big deal. Behind it all is message passing and I have a firm handle on that. But I still need some knowledge of the systems themselves. I do not want to keep my employers waiting. I might be willing to bullshit about my experiene to get the ball rolling, but I won't about my skills.

1:40pm. https://docs.microsoft.com/en-us/learn/paths/az-900-describe-cloud-concepts/?wt.mc_id=acom_newtoazure_webpage_azuremktg
https://docs.microsoft.com/en-us/learn/azure/

Let me watch the first thing and then I am going to check out some learning paths and register for Azure.

https://youtu.be/2vMEQ5zs1ko
Kubernetes vs. Docker: It's Not an Either/Or Question

Let me start with this thing.

https://youtu.be/2vMEQ5zs1ko?t=403
> The applications can now speak to each other just by using the service names that are laid out in Kubernetes.

Ok, I get it. Kubernettes works with Docker to make scaling easier. AWS makes it sound like an either or thing.

https://docs.microsoft.com/en-us/learn/paths/az-900-describe-cloud-concepts/?wt.mc_id=acom_newtoazure_webpage_azuremktg

Let me watch the stuff here.

2:10pm. This is so boring. Let me just try registering on Azure. A month will be long enough either way even if I miss a few days.

2:15pm. Nope, it also wants my card number. I am stuck for now.

2:20pm. https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/tour-of-azure-services

Who is going to learn all this trivial. Some people have those kinds of brains suitable for tackling quiz shows, but I do not.

> The Azure free student account is an offer for students that gives $100 credit and free developer tools. Also, you can sign up without a credit card.

Let me try this thing.

> Use your university or school email to sign up and renew each year you're a student

Nope, I don't have this and I need it as expected.

https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/case-study-introduction

Doing something like making a website would be interesting at this point as it would serve as an icebreaker. Right now I feel like I am slamming behind a glass screen.

https://docs.microsoft.com/hr-hr/learn/modules/azure-architecture-fundamentals/regions-availability-zones

Already covered this concept in AWS.

2:40pm. For the next hour before my dad gets back I am stuck, so I might as well take a break. Right now my brain is blocked up. I am at my limit how much raw text I can ingest. I need to move to digesting instead before I can consume more.

You know what, let me take a bath here, so I do not have to later. I'll commit here and resume when I got the AWS account operational. My goal for the day is to at least get the AWS Lambda to run.

In addition to everything else, doing something like a website that fetches from a database and displays it would not be bad. Some icebreaking there to get into the cloud grove would be good. I should aim to get all of the weaknesses as a programmer out of the way in one fell swoop."

---
## [pri0818/android_kernel_realme_sm7125](https://github.com/pri0818/android_kernel_realme_sm7125)@[693ed357e3...](https://github.com/pri0818/android_kernel_realme_sm7125/commit/693ed357e36f9caeadcfbcace590467d13d15f27)
#### Saturday 2022-07-16 13:18:13 by Peter Zijlstra

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
Signed-off-by: CloudedQuartz <ravenklawasd@gmail.com>
Signed-off-by: pri0818 <priyanshusinghal0818@gmail.com>

---
## [A-freedom/beamCalculator](https://github.com/A-freedom/beamCalculator)@[1fc2674406...](https://github.com/A-freedom/beamCalculator/commit/1fc267440652bfd0ef965bfde09ff92593ca6e5d)
#### Saturday 2022-07-16 13:20:41 by A-freedom

I can't get the deflection to work if the supports are in the center of the beam by using the integration method ,there is no problem with the code the code run exactly like I want to run , but I believe that the problem is in my 'MATH' ,since it seems like I will not be able to solve it in the moment ,so I will try the singularity function method

I did disable calculating deflection because I couldn't to make it work so I will star redoing my logic for the start in hope that will make a change .

sofat I have been able to get the defliction function work with some cases but still there are some bugs need to be fix like the one with  Exam:Mid_Term 2022

note:: now all function start from there local zero I find that this methond working just find and there is no need to change it. And If needed it will be way easier to just convert the output than refracting the source code. So from now and then the locals zeros will be the official method

and after two days of doing nothing I fixed the bug, I found the bug which was a laze shit I did with the 'd' variable when I was refactoring the code in calculateDeflection line 233

---
## [nicopap/bevy](https://github.com/nicopap/bevy)@[4847f7e3ad...](https://github.com/nicopap/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Saturday 2022-07-16 14:41:51 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [wwjiang007/linuxkit](https://github.com/wwjiang007/linuxkit)@[860934d5d9...](https://github.com/wwjiang007/linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Saturday 2022-07-16 15:10:38 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [Kimiblock/mcctl](https://github.com/Kimiblock/mcctl)@[2ce0bdc8cc...](https://github.com/Kimiblock/mcctl/commit/2ce0bdc8cc1e0820ee395020d4d10226bb9bdcff)
#### Saturday 2022-07-16 16:08:21 by Kimiblock

Support chromedriver method to download spigotmc.org files, fuck you cloudflare

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[69417bfde6...](https://github.com/mrakgr/The-Spiral-Language/commit/69417bfde65d06b7d085d32fa560dc41eac6afe6)
#### Saturday 2022-07-16 16:24:14 by Marko Grdinić

"4:05pm. Hygiene - check.

4:20pm. Let me rant a bit since I have time. It does not seem like I'll be doing any programming today.

I am thinking back to the AWS videos. Remember when they talked about the Route 53, which is AWS's DNS service? It feels like I am closer to bringing it together. I have no exp in web services, and I've been really wondering what I would do if I had to do this all from scratch, but AWS really does do the hard stuff of running a server. The same goes for the other cloud providers. As long as I play in that sandbox, I could become a web expert without having to understand the intricacies of networking at the low level.

All I really need to understand are the fundamentals of concurrency in other words.

Even if did a distributed large NN model, there is only one way to transfer data between instances and that is using messages. Messages are the universal standard no matter what protocol you use.

My confidence is really high now that I've stepped into this.

As trite as the AWS intro was, it mostly presented me with solutions to the problems I'd have. The cloud gives me everything I need to scale. As an individual human I am not going to get a better offer than it.

An AI that needs to run its mind on a cluster 24/7 with full utilization could realize benefits by managing its own hardware, but I do not have the mental resources of Skynet.

It matters little. If Skynet could make 100$/h, then it won't matter much to it whether it is spending 1$/h or 0.01$/h to run itself. It should be able to cover the cloud costs either way. So I should not worry about this either.

This is a counterargument towards my previous position. It felt right that I should be able to get my own AI chip, but feelings are just that.

I was in fact on the wrong path, so it is no wonder that I've failed.

5:05pm. I've had a talk with my dad, and he suggested I pass in the number of my account as my card. Somehow that did not even occur to me. I financially illiterate by this point. How do I even log into my netbanking service? Let me check out the journal from last year. I think I revisited that then.

I can't find anything. Maybe it was even further than a year back.

Now what is my username at the bank?

I remember going to a bank years back and doing something there. I think that was to renew my card. Maybe it was to open the Spiral Collective thing?

5:20pm. I am confused how this the login card is supposed to be used. I found my username I think, but what about the password? ...I threw it into the thash 15m ago along with the 2018 annual report.

I got it back.

> Niste korisnik NetBanking aplikacije. Uslugu možete ugovoriti u poslovnici Banke. (Br.poruke: 15012)

It is outright telling me I am not a Netbanking user. The reason this is happening is because netbanking is probably for business users now, but personal accounts are some weirdly named mobile service called Georges. I can't log in to see whan my forex account number is. But I think it does need a card for this, not the account number, right?

5:35pm. This is going to be hard. My father is being stubborn about letting me borrow his card so I can register for the free tier, and now I am in a humiliating situation of having to needle him about it.

I am thinking of trying to pass off the expired card. He mentioned something about it being mailed by the bank, but that I don't remember that ever happening. He also mentioned that new card I'll get would have the same number. But if it turns out to be inactive, I'd end up wasting the entire day tomorrow.

...No, I forgot. It is asking me for the expiration date outright. I have no idea what would be for the newer card as I do not have it.

5:50pm. I give up. I guess I'll have to find something else to do other than AWS tomorrow as it is Sunday. I am 35 years old, so I am not going to pester my parents until things go my way. Doing that would be too degrading.

> We will not charge you for usage below AWS Free Tier limits. We may temporarily hold up to $1 USD (or an equivalent amount in local currency) as a pending transaction for 3-5 days to verify your identity.

Maybe this whole thing is for nothing - I could get outright rejected if I give another person's card. This could just lead to further trouble down the road.

Let me avoid this. He is basically doing me a favor here, even if he is playing it safe merely out of instinct.

5:55pm. I think for the first time in a while, I have an excuse to take a vacation. I'll visit the bank on Monday and hope they have the card waiting for me in their vault, but if they don't and require me to wait until it can be reissued, so be it.

6:05pm. Miserable, just miserable. The next week looks dark indeed.

C backend TODO:
Tuple/Layout/Closure env size ordering

I'll take the opportunity to take care of this particular issue tomorrow then, since I have the time. I could also go back to work on that skeleton in Blender while I am at it. For me, it has become a matter of pride to pursue something. If playing games would give me power, I'd play those.

It is not like I've given up on art. I just decided that I wanted money after all. Just because I want money more does not mean I do not want to do Heaven's Key. It is merely a matter of prioritization.

What I want I want most right now is to level up my cloud skills to the point I could tackle any challenge in the wild whatsoever. It is a must have skill for working at startups, and I am not going to get a support role, but be right in the thick of it.

It is important to me. It is like food, when you have it, you do not think about it. But if you don't, it is the center of all your concerns."

---
## [alfredggttv/ATM7_questV2_update](https://github.com/alfredggttv/ATM7_questV2_update)@[8bff1fe476...](https://github.com/alfredggttv/ATM7_questV2_update/commit/8bff1fe4769e3ecd98814c640bc44640ee6e9f1a)
#### Saturday 2022-07-16 18:08:12 by 90

Add more starting books

Tome now also includes guides/READMEs from Blood Magic, Evilcraft, RFTools, Roots Classic, SecurityCraft, Silent Gear, Spice of Life: Carrot Edition, The One Probe and The Twilight Forest.

---
## [fuckdedeurkruk/frameworks_base](https://github.com/fuckdedeurkruk/frameworks_base)@[4f678219b0...](https://github.com/fuckdedeurkruk/frameworks_base/commit/4f678219b071dda266d3ef9e00371b59bdfec34b)
#### Saturday 2022-07-16 18:11:30 by Joey Huab

PixelPropsUtils: Spoof play store once again

* Diablo Immortal fuck you

---
## [Tiamat-Tech/sucrase](https://github.com/Tiamat-Tech/sucrase)@[18e6886f1d...](https://github.com/Tiamat-Tech/sucrase/commit/18e6886f1d67df09cee080e6edb3bf5358bf982a)
#### Saturday 2022-07-16 18:45:29 by Alan Pierce

Update README benchmark to latest numbers (#724)

The README benchmark numbers were last updated in January 2021, so this PR
updates it to see what's changed since then.

To help understand the underlying reasons for changes in numbers, I updated
each piece incrementally and re-ran the benchmark at each step. For the numbers
shown here, I ran the full benchmark 3 times and took the best time for each
tool.

Here's the original benchmark:
```
            Time            Speed
Sucrase     1.64 seconds    220221 lines per second
swc         2.13 seconds    169502 lines per second
esbuild     3.02 seconds    119738 lines per second
TypeScript  24.18 seconds   14937 lines per second
Babel       27.22 seconds   13270 lines per second
```

Since running the previous benchmark, I switched from a 2016 Intel MacBook Pro
to a 2020 M1 MacBook Air, so I simulated the original benchmark on my new
laptop by using Sucrase 3.17.0, the pinned versions of all other tools, and
Node 14. Results:
```
Sucrase     0.76 seconds    477950 lines per second
swc         1.05 seconds    344215 lines per second
esbuild     1.43 seconds    253143 lines per second
TypeScript  9.28 seconds    38943 lines per second
Babel       11.03 seconds   32758 lines per second
```
Over a 2x improvement for all tools just from the new laptop! Pretty incredible
in my opinion.

Then I upgraded to Node 18, still running the old version of all tools:
```
Sucrase     0.64 seconds    563963 lines per second
swc         1.04 seconds    348526 lines per second
esbuild     1.42 seconds    254111 lines per second
TypeScript  7.99 seconds    45210 lines per second
Babel       10.3 seconds    35076 lines per second
```
About a 10-20% improvement for tools written in JS just from upgrading Node. As
expected, swc and esbuild aren't affected by the node upgrade.

Then I upgraded all tools to latest (and addressed a breaking change in esbuild
usage):
```
Sucrase     0.65 seconds    558226 lines per second
swc         1.24 seconds    290311 lines per second
esbuild     1.47 seconds    245861 lines per second
TypeScript  8.97 seconds    40258 lines per second
Babel       9.02 seconds    40032 lines per second
```
Interestingly, most tools got a little slower, which isn't too surprising given
that bug fixes and scope creep can gradually hurt performance.

Then I updated the usage of Sucrase and swc to account for better configuration
since last time. Most notably, Sucrase now has a `disableESTransforms` option
that should be used in most cases these days (and I'm hoping to make it the
default in a future semver-major release), and that better matches how all of
the other tools are configured here. Results:
```
Sucrase     0.57 seconds    636975 lines per second
swc         1.19 seconds    304526 lines per second
esbuild     1.45 seconds    248692 lines per second
TypeScript  8.98 seconds    40240 lines per second
Babel       9.18 seconds    39366 lines per second
```
It looks like `disableESTransforms` resulted in about a 15% speedup for Sucrase.

As always, there are plenty of caveats with these measurements, which are
mentioned in the docs in the benchmark file, but I think they still are fair.

One part that I didn't update yet is the Jest codebase being transpiled. I don't
anticipate that having a meaningful effect on the benchmark numbers.

---
## [Razican/diesel](https://github.com/Razican/diesel)@[448df6b615...](https://github.com/Razican/diesel/commit/448df6b61566dbd419554fc82abd018357848846)
#### Saturday 2022-07-16 19:16:23 by Georg Semmler

Address #3173

This is a tricky one. It seems like the behaviour described in that
issue should work out of the box, but it doesn't. I've spend some time
to investigate various solutions to make this work, but I came to the
conclusion that the current behaviour is the correct one.

The underlying issue here is that such an query promotes the inner
`Nullable<_>` of the field onto the outer `Queryable` wrapper. Without
`Selectable` that would require a select clause like
`.select((table::column.assume_not_null(),).nullable())`. This is
technically a safe pattern, but requires the usage of the "advanced"
`assume_not_null()` method to forcibly convert types to their not null representation.

Possible solutions tried to make the enable constructs shown in that
issue:

* I've tried to make the `impl Selectable for Option<T>` return the
following `SelectExpression`:
`dsl::Nullable<dsl::AssumeNotNull<T::SelectExpression>>`
where `AssumeNotNull` converts each tuple element to the corresponding
not nullable expression, while `Nullable` wraps the tuple itself into a
nullable type wrapper.
* I've tried to apply a similar approach like that one above, but only
for derived impls by manipulating the generated code for a optional
field with `#[diesel(embed)]`

Both solutions require changes to our sql type system, as for example
allowing to load a non nullable value into a `Option<T>` to enable their
usage in a more general scope as the presented example case.
(See the added test cases for this). That by itself would be fine in my
opinion, as this is always a safe operation. Unfortunately the
`AssumeNotNull` transformation would be applied recursively for all
sub-tuples, which in turn would cause trouble with nested joins (again
see the examples). We would be able to workaround this issue by allowing
the `FromSql<ST, DB> for Option<T>` impl for non-nullable types to catch
null values, which in turn really feels like a bad hack. (You would like
to get an error there instead, but nested nullable information are
gone.)
All in all this lead me to the conclusion that the current behaviour is
correct.

This PR adds a few additional tests (an adjusted version of the test
from the bug report + more tests around nested joins) and does move
around some code bits that I noticed while working on this.

I think the official answer for the bug report would be: Either wrap the
inner type also in an `Option` or provide a manual `Selectable` impl
that does the "right" thing there.

---
## [Syncxv/music-player-flutter](https://github.com/Syncxv/music-player-flutter)@[d0a35e7540...](https://github.com/Syncxv/music-player-flutter/commit/d0a35e7540ef25cf92b8962863708d2420343730)
#### Saturday 2022-07-16 22:33:19 by Syncxv

todo: write serlaizer class

how the fuck am i gonna do this

DART KINDA SUCKS THERE ARE -1 FEATURES MAN
SO INFLEXIABLE WHAT THE FUCK
I JUST WANT TO RESTRICT WAHT TTYPES THE GENERIC CAN BE WHY IS THAT SO HARD

---
## [willcrichton/cargo](https://github.com/willcrichton/cargo)@[6a4d98d232...](https://github.com/willcrichton/cargo/commit/6a4d98d2327124ca52bb9f67d6ad0097eb6b2e65)
#### Saturday 2022-07-16 22:34:38 by bors

Auto merge of #10472 - epage:add, r=ehuss

feat: Import cargo-add into cargo

### Motivation

The reasons I'm aware of are:
- Large interest, see #5586
- Make it easier to add a dependency when you don't care about the version (instead of having to find it or just using the major version if thats all you remember)
- Provide a guided experience, including
  - Catch or prevent errors earlier in the process
  - Bring the Manifest format documentation into the terminal via `cargo add --help`
  - Using `version` and `path` for `dependencies` but `path` only for `dev-dependencies` (see crate-ci/cargo-release#288 which led to killercup/cargo-edit#480)

### Drawbacks

1. This is another area of consideration for new RFCs, like rust-lang/rfcs#3143 (this PR supports it) or rust-lang/rfcs#2906 (implementing it will require updating `cargo-add`)

2. This is a high UX feature that will draw a lot of attention (ie Issue influx)

e.g.
- killercup/cargo-edit#521
- killercup/cargo-edit#126
- killercup/cargo-edit#217

We've tried to reduce the UX influx by focusing the scope to preserving semantic information (custom sort order, comments, etc) but being opinionated on syntax (style of strings, etc)

### Behavior

Help output
<details>

```console
$ cargo run -- add --help
cargo-add                                                                                                                                  [4/4594]
Add dependencies to a Cargo.toml manifest file

USAGE:
    cargo add [OPTIONS] <DEP>[`@<VERSION>]` ...
    cargo add [OPTIONS] --path <PATH> ...
    cargo add [OPTIONS] --git <URL> ...

ARGS:
    <DEP_ID>...    Reference to a package to add as a dependency

OPTIONS:
        --no-default-features     Disable the default features
        --default-features        Re-enable the default features
    -F, --features <FEATURES>     Space-separated list of features to add
        --optional                Mark the dependency as optional
    -v, --verbose                 Use verbose output (-vv very verbose/build.rs output)
        --no-optional             Mark the dependency as required
        --color <WHEN>            Coloring: auto, always, never
        --rename <NAME>           Rename the dependency
        --frozen                  Require Cargo.lock and cache are up to date
        --manifest-path <PATH>    Path to Cargo.toml
        --locked                  Require Cargo.lock is up to date
    -p, --package <SPEC>          Package to modify
        --offline                 Run without accessing the network
        --config <KEY=VALUE>      Override a configuration value (unstable)
    -q, --quiet                   Do not print cargo log messages
        --dry-run                 Don't actually write the manifest
    -Z <FLAG>                     Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for
                                  details
    -h, --help                    Print help information

SOURCE:
        --path <PATH>        Filesystem path to local crate to add
        --git <URI>          Git repository location
        --branch <BRANCH>    Git branch to download the crate from
        --tag <TAG>          Git tag to download the crate from
        --rev <REV>          Git reference to download the crate from
        --registry <NAME>    Package registry for this dependency

SECTION:
        --dev                Add as development dependency
        --build              Add as build dependency
        --target <TARGET>    Add as dependency to the given target platform

EXAMPLES:
  $ cargo add regex --build
  $ cargo add trycmd --dev
  $ cargo add --path ./crate/parser/
  $ cargo add serde serde_json -F serde/derive
```

</details>

Example commands
```rust
cargo add regex
cargo add regex serde
cargo add regex@1
cargo add regex@~1.0
cargo add --path ../dependency
```
For an exhaustive set of examples, see [tests](https://github.com/killercup/cargo-edit/blob/merge-add/crates/cargo-add/tests/testsuite/cargo_add.rs) and associated snapshots

Particular points
- Effectively there are two modes
  - Fill in any relevant field for one package
  - Add multiple packages, erroring for fields that are package-specific (`--rename`)
  - Note that `--git` and `--path` only accept multiple packages from that one source
- We infer if the `dependencies` table is sorted and preserve that sorting when adding a new dependency
- Adding a workspace dependency
  - dev-dependencies always use path
  - all other dependencies use version + path
- Behavior is idempotent, allowing you to run `cargo add serde serde_json -F serde/derive` safely if you already had a dependency on `serde` but without `serde_json`
- When a registry dependency's version req is unspecified, we'll first reuse the version req from another dependency section in the manifest.  If that doesn't exist, we'll use the latest version in the registry as the version req

### Additional decisions

Accepting the proposed `cargo-add` as-is assumes the acceptance of the following:
- Add the `-F` short-hand for `--features` to all relevant cargo commands
- Support ``@`` in pkgids in other commands where we accept `:`
- Add support for `<name>`@<version>`` in more commands, like `cargo yank` and `cargo install`

### Alternatives

- Use `:` instead of ``@`` for versions
- Flags like `--features`, `--optional`, `--no-default-features` would be position-sensitive, ie they would only apply to the crate immediate preceding them
  - This removes the dual-mode nature of the command and remove the need for the `+feature` syntax (`cargo add serde -F derive serde_json`)
  - There was concern over the rarity of position-sensitive flags in CLIs for adopting it here
- Support a `--sort` flag to sort the dependencies (existed previously)
  - To keep the scope small, we didn't want general manifest editing capabilities
- `--upgrade <POLICY>` flag to choose constraint (existed previously)
  - The flag was confusing as-is and we feel we should instead encourage people towards `^`
- `--allow-prerelease` so a `cargo add clap` can choose among pre-releases as well
  - We felt the pre-release story is too weak in cargo-generally atm for making it first class in `cargo-add`
- Offer `cargo add serde +derive serde_json` as a shorthand
- Infer path from a positional argument

### Prior Art

- *(Python)* [poetry add](https://python-poetry.org/docs/cli/#add)
  - `git+` is needed for inferring git dependencies, no separate  `--git` flags
  - git branch is specified via a URL fragment, instead of a `--branch`
- *(Javascript)* [yarn add](https://yarnpkg.com/cli/add)
  - `name@data` where data can be version, git (with fragment for branch), etc
  - `-E` / `--exact`, `-T` / `--tilde`, `-C` / `--caret` to control version requirement operator instead of `--upgrade <policy>` (also controlled through `defaultSemverRangePrefix` in config)
  - `--cached` for using the lock file (killercup/cargo-edit#41)
  - In addition to `--dev`, it has `--prefer-dev` which will only add the dependency if it doesn't already exist in `dependencies` as well as `dev-dependencies`
  - `--mode update-lockfile` will ensure the lock file gets updated as well
- *(Javascript)* [pnpm-add](https://pnpm.io/cli/add)
- *(Javascript)* npm doesn't have a native solution
  - Specify version with ``@<version>``
  - Also overloads `<name>[`@<version>]`` with path and repo
    - Supports a git host-specific protocol for shorthand, like `github:user/repo`
    - Uses fragment for git ref, seems to have some kind of special semver syntax for tags?
  - Only supports `--save-exact` / `-E` for operators outside of the default
- *(Go)* [go get](https://go.dev/ref/mod#go-get)
  - Specify version with ``@<version>``
  - Remove dependency with ``@none``
- *(Haskell)* stack doesn't seem to have a native solution
- *(Julia)* [pkg Add](https://docs.julialang.org/en/v1/stdlib/Pkg/)
- *(Ruby)* [bundle add](https://bundler.io/v2.2/man/bundle-add.1.html)
  - Uses `--version` / `-v` instead of `--vers` (we use `--vers` because of `--version` / `-V`)
  - `--source` instead of `path` (`path` correlates to manifest field)
  - Uses `--git` / `--branch` like `cargo-add`
- *(Dart)* [pub add](https://dart.dev/tools/pub/cmd/pub-add)
  - Uses `--git-url` instead of `--git`
  - Uses `--git-ref` instead of `--branch`, `--tag`, `--rev`

### Future Possibilities

- Update lock file accordingly
- Exploring the idea of a [`--local` flag](https://github.com/killercup/cargo-edit/issues/590)
- Take the MSRV into account when automatically creating version req (https://github.com/killercup/cargo-edit/issues/587)
- Integrate rustsec to report advisories on new dependencies (https://github.com/killercup/cargo-edit/issues/512)
- Integrate with licensing to report license, block add, etc (e.g. https://github.com/killercup/cargo-edit/issues/386)
- Pull version from lock file (https://github.com/killercup/cargo-edit/issues/41)
- Exploring if any vendoring integration would be beneficial (currently errors)
- Upstream `cargo-rm` (#10520), `cargo-upgrade` (#10498), and `cargo-set-version` (in that order of priority)
- Update crates.io with `cargo add` snippets in addition to or replacing the manifest snippets

For more, see https://github.com/killercup/cargo-edit/issues?q=is%3Aissue+is%3Aopen+label%3Acargo-add

### How should we test and review this PR?

This is intentionally broken up into several commits to help reviewing
1. Import of production code from cargo-edit's `merge-add` branch, with only changes made to let it compile (e.g. fixing up of `use` statements).
2. Import of test code / snapshots.  The only changes outside of the import were to add the `snapbox` dev-dependency and to `mod cargo_add` into the testsuite
3. This extends the work in #10425 so I could add back in the color highlighting I had to remove as part of switching `cargo-add` from direct termcolor calls to calling into `Shell`

Structure-wise, this is similar to other commands
- `bin` only defines a CLI and adapts it to an `AddOptions`
- `ops` contains a focused API with everything buried under it

The "op" contains a directory, instead of just a file, because of the amount of content.  Currently, all editing code is contained in there.  Most of this will be broken out and reused when other `cargo-edit` commands are added but holding off on that for now to separate out the editing API discussions from just getting the command in.

Within the github UI, I'd recommend looking at individual commits (and the `merge-add` branch if interested), skipping commit 2.  Commit 2 would be easier to browse locally.

`cargo-add` is mostly covered by end-to-end tests written using `snapbox`, including error cases.

There is additional cleanup that would ideally happen that was excluded intentionally from this PR to keep it better scoped, including
- Consolidating environment variables for end-to-end tests of `cargo`
- Pulling out the editing API, as previously mentioned
  - Where the editing API should live (`cargo::edit`?)
  - Any more specific naming of types to reduce clashes (e.g. `Dependency` or `Manifest` being fairly generic).
- Possibly sharing `SourceId` creation between `cargo install` and `cargo edit`
- Explore using `snapbox` in more of cargo's tests

Implementation justifications:
- `dunce` and `pathdiff` dependencies: needed for taking paths relative to the user and make them relative to the manifest being edited
- `indexmap` dependency (already a transitive dependency): Useful for preserving uniqueness while preserving order, like with feature values
- `snapbox` dev-dependency: Originally it was used to make it easy to update tests as the UX changed in prep for merging but it had the added benefit of making some UX bugs easier to notice so they got fixed.  Overall, I'd like to see it become the cargo-agnostic version of `cargo-test-support` so there is a larger impact when improvements are made
- `parse_feature` function: `CliFeatures` forces items through a `BTreeSet`, losing the users specified order which we wanted to preserve.

### Additional Information

See also [the internals thread](https://internals.rust-lang.org/t/feedback-on-cargo-add-before-its-merged/16024).

Fixes #5586

---
## [cadergator10/opencomputer-security-system](https://github.com/cadergator10/opencomputer-security-system)@[d411aae656...](https://github.com/cadergator10/opencomputer-security-system/commit/d411aae6564b9fda507e88593a0f98784e8d902f)
#### Saturday 2022-07-16 22:51:26 by Cade

Sector extreme prototype finished

This, is a buggy prototype that likely will not work
Dear God...
There's more
No...

Through a few hours of constant pain, sweat, tears, and blood (maybe not blood though), I managed to "finish" the system. i can't really think of anything else that must be added before testing, so it's time for testing. yaaaaay...
Another thing I made was rangeextender, because I plan on adding the ability to use a linking card in doorcontrol systems, so your server can send messages to doorcontrols outside of the range of modems and in other dimensions, if thats what you like...

---

