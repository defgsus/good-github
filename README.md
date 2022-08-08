## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-07](docs/good-messages/2022/2022-08-07.md)


1,613,398 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,613,398 were push events containing 2,163,008 commit messages that amount to 116,556,023 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [KDr2/emacs](https://github.com/KDr2/emacs)@[bee6ee9de1...](https://github.com/KDr2/emacs/commit/bee6ee9de179a412f6c4b1c072408066e7912ff6)
#### Sunday 2022-08-07 00:04:38 by Jonas Bernoulli

* doc/misc/transient.texi: Update to transient v0.3.7-156-ga5562cb

Eventually we want to be able to generate "transient.texi" from
"transient.org", without having to either give up on idiomatic texinfo
or making it much more painful to maintain the org file.

We are much closer to that now, but there are still a few areas where
additional work is needed.  This was mostly accomplished by using Org
macros.

The most significant outstanding issue is that the generated
references don't yet look like an experienced texinfo author like Eli
would like them to look.  Additionally it is not yet possible to use a
macro that produces @dots{} in the places Eli added them, and in Org
code blocks it is not possible to use macros, so we cannot have
@var{...} appear in "@lisp ... @end lisp".  The last issue probably
cannot be changed on Org's side, but since there are only two such
code blocks, this might be a situation where the compromise has to
come from the texinfo side.  There are also three other very minor
and inconsequential differences.

For now I have regenerated the texinfo file from the org file and then
discarded the differences mentioned in the previous paragraph.

The process of merging (1) Eli's changes to the texinfo file
(including, but certainly not limited to markup), (2) changes to the
org source (updated content, formatting changes backported earlier,
fixes for formatting changes Eli did not fix, etc.) and (3) changes to
the code that converts the org source to texinfo, was very laborious
and painful.  In essence, this amounted to a (at least) three-way
merge across three different languages and three repositories.

I tried very hard to not waste any of the effort Eli had put into
fixing up the generated texinfo file.  I.e., I went back and forth
making improvements to the org source, implementing org macros,
regenerating the texinfo and comparing the remaining difference, and
creating commits on both sides.  This resulted in a dozen commits on
both sides and took me well over a day.  I could have put in even more
effort to absolutely ensure nothing at all is lost in the process, but
I think that would have amounted to a colossal waste of my time.

Going forward, if you find unidiomatic texinfo, then please don't fix
each instance.  Instead write me an email, explaining what the problem
is.  You are welcome to make limited fixes to the content or fix
one-of markup issue in the texinfo file; those are relatively simple
to backport in comparison.

---
## [lazytanuki/helix](https://github.com/lazytanuki/helix)@[973c51c3e9...](https://github.com/lazytanuki/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Sunday 2022-08-07 00:33:07 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[9ccd6ecd74...](https://github.com/mamh-mixed/microsoft-terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Sunday 2022-08-07 02:14:41 by Mike Griese

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
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[8962f88f90...](https://github.com/mamh-mixed/microsoft-terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Sunday 2022-08-07 02:14:57 by Dustin L. Howett

Disable the VT color quirk for pwsh and modern inbox powershell (#13352)

In #6810, we introduced a "quirk" for all known versions of PowerShell
that suppressed their requests for black background/gray foreground.
This was done to avoid an [issue in PSReadline] where it would paint
black bars all over the screen if the default background color wasn't
the same as the ANSI black color.

Years have passed since that quirk was introduced. The underlying bug
was fixed, and the fix was released broadly long ago. It's time for us
to remove the quirk... almost.

Terminal still runs on versions of Windows that ship a broken version of
PSReadline. We must maintain the quirk there -- the user can't do
anything about it, and we would make their experience worse if we
removed the quirk entirely.

PowerShell 7.0 also ships a broken version of PSReadline. It is still in
support for another 6 months, but updates have been available for some
time. We can encourage users to update.

Therefore, we only need the quirk for Windows PowerShell, and then only
for specific versions of Windows.

_Inside Windows_, we don't even need that: we're guaranteed to be built
alongside a fixed version of PowerShell!

Closes #6807

[issue in PSReadline]: https://github.com/PowerShell/PSReadLine/issues/830#issuecomment-650508857

---
## [mumbleskates/llvm-project](https://github.com/mumbleskates/llvm-project)@[15f3cd6bfc...](https://github.com/mumbleskates/llvm-project/commit/15f3cd6bfc670ba6106184a903eb04be059e5977)
#### Sunday 2022-08-07 02:20:12 by Matheus Izvekov

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

3) This patch could expose a bug in how you get the source range of some
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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a77b36a117...](https://github.com/treckstar/yolo-octo-hipster/commit/a77b36a1174beae5a69613de1c7e55154919453c)
#### Sunday 2022-08-07 02:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [cl1ents/gm-modules](https://github.com/cl1ents/gm-modules)@[0f7f84cb3c...](https://github.com/cl1ents/gm-modules/commit/0f7f84cb3cb13ab46a4ea210f1f971f0180e4d3d)
#### Sunday 2022-08-07 02:51:21 by evⁿ ☕

lol stupid fucking sentence

idk why i chose to replace "voicechat" with "voice channel" it looks kinda stupid

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f8468a3be2...](https://github.com/treckstar/yolo-octo-hipster/commit/f8468a3be2a730955a074785c8a6c15f1da7ce90)
#### Sunday 2022-08-07 03:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [AtlasC0R3/atlasc0r3.github.io](https://github.com/AtlasC0R3/atlasc0r3.github.io)@[b58a394572...](https://github.com/AtlasC0R3/atlasc0r3.github.io/commit/b58a3945725a00e7a4f7573f41a9c3c84fa2d567)
#### Sunday 2022-08-07 03:29:10 by atlas_core

why in the goddamn ever living fucking shit did git forget what github

---
## [ashokreaddygithub/Resume-Draft](https://github.com/ashokreaddygithub/Resume-Draft)@[8e68bc2a2e...](https://github.com/ashokreaddygithub/Resume-Draft/commit/8e68bc2a2ebd9a496f6b7b6b1c832f198f58ef99)
#### Sunday 2022-08-07 03:50:00 by ASHOK KUMAR REDDY

Update README.md

MARAM VENKATA ASHOK KUMAR REDDY Mobile: +13472168881 E-mail: ashok.maram1@gmail.com Outlook:vmaram_gps@nec.edu TECHNICAL PROFICIENCY Having 6+months Experience in Oracle Data Migration Project.(OWB TO ODI MIGRATION PROJECT) C programming, c++, java,, software development, cyber security, cloud computing. INTERNSHIP.
Organization Title Duration Role
: HEALTHGENIC SOLUTIONS LLP, Hyderabad : CYBER SECURITY ANALYST : 6 MONTHS. : RESEARCHING UPCOMING IT TENDS,SECURITY BREACHES.
ACADEMIC PROJECTS
Title Period Description
CAR RENTAL SYSTEM Oct’18-Nov’18 Car Rental System is based on a concept to rent cars and generate rental invoice of a rental company. Before stepping into the main system, a user has to pass through a login system to get access, then Only the user can select cars with a different model and rent for certain days. This mini project Contains limited features, but the essential one
Title Period Team Size Description
ENVIRONMENTAL ENGINEERING Oct’19 3 About Reduce, Resue, Recycle Effect of Sewage Farming on Ground Water and Soil Quality Garbage Collection Treatment and Disposal.
Title Period Description
LAPTOP REPAIR Feb’19-Mar’19 Created a C language code which helps the users to find out the cost of repair of their laptop when they face issues.
Title Period Description
FACEBOOK PAGE Feb’20-Mar’20 Recreated a duplicacy of Facebook page with some HTML commands.
Title Period Description
NETWORK TRAFFIC ANALYSIS Jan’21-May’21 based project wherein you can learn how to use a packet sniffer software to monitor and capture data packets passing through a computer network, such as the network of your office, or your training center, or your college.
WORKSHOP & TRAININGS ATTENDED
Attended workshop on computer science and application’s organized by GreenAd as a part of National Tech-fest of SRM university,Chennai.
Attended workshop on figure print authentication’ organized by Splenor as a part of National Tech-fest of LPU universityPunjab.
EXTRACURRICULAR ACTIVITIES
Coordinated Intra-Campus Cultural Fest ‘LPU university, 2018
Participated in various Dance Events in Inter School Dance Competitions and also in Intra-Campus Cultural Fest- ‘LPU UNIVERSITY’, 2019
Served as Captain for Intra School Cultural and Sports House-wise competitions during 2019-2020
Volunteered for
-Global youth movement 2019,LPU UNIVERSITY.
-Imperium-Intra-campus Tech Fest
-NSS marathon ACADEMIC CREDENTIALS
B.Tech | computer science engineering from Lovely professional university, Punjab with 65.1%.
INTERMEDIATE |MPC from Srichaitanya junior college, Vijayawada with 90.4%.
SSC|Bhashyam public school Guntur with 8.3 CGPA. PERSONAL DETAILS
Date of Birth Languages Known Address
: 03-8-2000 : English, Telugu, Hindi :226, Merrimac street New Burry Port MA, 01950

---
## [neong83/fucking-algorithm](https://github.com/neong83/fucking-algorithm)@[15b428a8ab...](https://github.com/neong83/fucking-algorithm/commit/15b428a8ab2d3bf09c3f710f90a2240bed0b39c8)
#### Sunday 2022-08-07 06:10:39 by Tomasz Surowiec

[English] Correct Edit Distance 

(I feel a need to preface this by saying that the changes I made were based solely on the English version, and the reading experience, for I do not speak Chinese (I'm not even sure if it's Mandarin, Cantonese or which one, nor if there's any difference in writing). Should you object to any changes, please let me know)

1. Changed the apostrophe character from *`* to *'*. The former is not used as an apostrophe, and is actually an accent mark (for preferred characters, refer to (this)[http://snowball.tartarus.org/texts/apostrophe.html] (U+0027 ', U+2019 ’, U+201B ‛)).
2. Changed certain verb forms. For instance: *"The last question is that **writing** a function to calculate [...]"* to *"The last question is **to write** a function which calculates [...]"* (also *which* -> *to* in order to avoid the repetition).
3. Changed the capitalization where necessary. For example: *Helpless* to *helpless* (since it's not a proper name); *We* to *we* (middle of a sentence).
4. Changed a few verbs to nouns, and vice versa: *"explain"* (on its own serves as an imperative, which would demand that the reader explain it) to *"explanation"*; *"storage"* to "store [the least editing distance of s1 and s2; L226]".
5. Fixed redundant spaces: *"[...] `s2`  in [...]"* to *"[...] `s2` in [...]"*; *"s1[i]！=s2[j]"* to *"s1[i] != s2[j]"*
6. Changed a few odd phrases: *"a violent solution"* to *"a brute force solution"* ( (most)[https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiolLjsxK3xAhUspIsKHU-9BwEQFjADegQIBBAD&url=https%3A%2F%2Fgsdrc.org%2Fwp-content%2Fuploads%2F2019%2F11%2F671_P-CVE_Programming_on_Men_Women_Boys_and_Girls.pdf&usg=AOvVaw2QjJ_-yjxxw2oWYtG77sgE], albeit (not all)[https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiolLjsxK3xAhUspIsKHU-9BwEQFjABegQIAhAE&url=https%3A%2F%2Fwww.programmersought.com%2Farticle%2F27011223160%2F&usg=AOvVaw1f6OCbf1r7M8GAfmGotBDg], uses of the former did not refer to programming ); *"from the bottom to up"* to *"from the bottom up"* (or *"bottom-up"*; see: (from the bottom up)[https://www.lexico.com/definition/from_the_bottom_up], and (bottom-up)[https://dictionary.cambridge.org/dictionary/english/bottom-up] ); *"operation number"* to *"the number of operations"* (this one might have been more subjective).
7. Removed latex dollar signs (since github markdown does not support it): *"$O(min(M, N))$"* to *"O(min(M, N))"* (as used in other articles).
8. Pluralized certain nouns after *"any"* ( ("We use any for indefinite quantities in questions and negative sentences")[https://dictionary.cambridge.org/grammar/british-grammar/any] ): *"any operation"* to *"any operations"*.
9. Added some formatting: "dp(i, j)" to "`dp(i, j)`" (L98).

I'm also not sure if *"[...] I wrote some words out of place by mistake"* refers to mistyping, but it's still more than clear, albeit slightly wordy.

To reiterate, should any of these be of concern, let me know, especially since it is my second language.
Best regards

---
## [sortofasian/d3](https://github.com/sortofasian/d3)@[971ebd3bbc...](https://github.com/sortofasian/d3/commit/971ebd3bbce3d3c0ddeb4916cd48aa28670e98ae)
#### Sunday 2022-08-07 08:36:33 by sortofasian

HOLY FUCKING SHIT IT'S TOP LEVEL AWAIT + TYPESCRIPT + NODEMON + DEBUG ALL WORKING TOGETHER

---
## [vimpostor/vim-tpipeline](https://github.com/vimpostor/vim-tpipeline)@[affe9ca352...](https://github.com/vimpostor/vim-tpipeline/commit/affe9ca352dabb8eddbcedd0baac4672f9173724)
#### Sunday 2022-08-07 08:59:34 by Magnus Groß

Postpone evaluation of stl for nvim

Usually the statusline is set once at the startup of vim to a function
that evaluates to the dynamic value of the statusline at runtime.

However some statuslines are particularly retarded and completely shit
on this vim idiomatic way of setting the statusline and instead update
the stl vim option directly, e.g. with a timer and on autocmd events.

This is not only completely stupid, but also has slightly worse
performance and is in fact also semantically incorrect (e.g. there is
not an autocmd for every way that it is possible to update the
statusline, only for most of the scenarios).

This is now the second time that lualine does something in a completely
fucked up way (the first time was the way that they pretend to have
global statusline support, by simply setting the laststatus option if a
lualine option is set, completely ignoring the idiomatic way of simply
letting the user set the laststatus option directly).
Why again are so many people recommending lualine?
They seem to know jack shit about the idiomatic way to do things in vim.

The bad commit in lualine is 53aa3d82d9d9329880b4197f278fcb74051a6af5.

Of course this also breaks our plugin because of the way that
g:tpipeline_statusline interacts with &stl.

To workaround the issue, we do not set g:tpipeline_statusline if we are
in neovim. Then in the update routine we first evaluate
g:tpipeline_statusline (to not break users configs that set this
variable) and then try &stl as fallback.

For now we only implement this workaround for neovim, as I don't believe
there is any vim statusline plugin that uses stl in such a fucked up
way.

Congrats lualine, we know have an extra workaround just for you.

Fixes #32

ref: https://github.com/nvim-lualine/lualine.nvim/commit/53aa3d82d9d9329880b4197f278fcb74051a6af5
ref: https://github.com/nvim-lualine/lualine.nvim/pull/736

---
## [srsbsns5/GAN-GDDS1](https://github.com/srsbsns5/GAN-GDDS1)@[d5113aa21a...](https://github.com/srsbsns5/GAN-GDDS1/commit/d5113aa21a330d5dc6bf716cdba88b8e42c20cc5)
#### Sunday 2022-08-07 09:55:27 by Greg

Humble beginnings of a credit scene

Ooh
You can dance
You can jive
Having the time of your life
Ooh, see that girl
Watch that scene
Digging the dancing queen
Friday night and the lights are low
Looking out for a place to go
Where they play the right music
Getting in the swing
You come to look for a king
Anybody could be that guy
Night is young and the music's high
With a bit of rock music
Everything is fine
You're in the mood for a dance
And when you get the chance
You are the dancing queen
Young and sweet
Only seventeen
Dancing queen
Feel the beat from the tambourine, oh yeah
You can dance
You can jive
Having the time of your life
Ooh, see that girl
Watch that scene
Digging the dancing queen
You're a teaser, you turn 'em on
Leave 'em burning and then you're gone
Looking out for another
Anyone will do
You're in the mood for a dance
And when you get the chance
You are the dancing queen
Young and sweet
Only seventeen
Dancing queen
Feel the beat from the tambourine, oh yeah
You can dance
You can jive
Having the time of your life
Ooh, see that girl
Watch that scene
Digging the dancing queen
Digging the dancing queen

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[fd60c5d441...](https://github.com/mrakgr/The-Spiral-Language/commit/fd60c5d4413686a5076927deff3597645587e25a)
#### Sunday 2022-08-07 15:37:35 by Marko Grdinić

"1:50pm. Done with breakfast. Let me watch Lycoris first and then I will resume.

2:35pm. Lycoris is definitely shaping up to be a classic. Maybe it will go the way of Symphogear?

At any rate, let me do some writing. I'll paste what I've done in the previous section and continue from there.

$$$

(At school)

It is the first day of high school. The new year has begun and I can see my classmates slowly starting to form connections. I couldn't care less about any of that. Skip, skip, skip...

---

(Euclid's Room)

After a long and tedius day I arrive back home. Closing the door behind me, I enter the room and toss my bookbag at the side, homing in on the object of interest, a package that arrive by mail. I got it last night, and wait until I was rested to set it up. Using a pair of scissors, I cut away the sealing tape of the dull, cardboard mailing box, and take out the smaller box from within with the actual product. The printed image on it depicts a white, glossy sphere, twice the size of a marble. I open the box, take out the marble along with the orb holder, get off the bed I was working on and move towards the desk. I seat myself to the chair and after deliberating for a few moments where place it: the desk in front of me or the top of the computer case next to it, I decide on case. Gently placing the orb holder on the rig, I turn on my old computer and get to work downloading the programs necessary to get the orb to work.

As I work I feel a tinge of nervousness and excitement. An ordinary mid-range GPU that I have in my PC could manage something like 10 ^ 13 floating point operations per second (FLOPs), or 10 teraflops. According to the specs I've read online, the brain core which is roughly the size of a golf ball can manage a staggering 10 ^ 39. As a rough comparison, the human brain has been estimated to be on the order of 10 ^ 15 operations per second. Even if you put all the humans currently alive today that would only roughly add up to the 10 ^ 24 FLOPs.  To put it in another way, the raw computational ability of the brain core exceeds the power of all the human brains on Earth combined by a quadrillion (10 ^ 15) times!

And it is in my hands!

Of course I would be excited!

With a few clicks I opened the downloaded app, and stretch my body to let loose some of the tension. Energy pumping through my veins, my focus is solely on the options and the data in front of me.

The core is just a perfectly glossy rock so I can't see any indication whether something has happened by looking at it, but after entering the two keys, I see that wireless comnication between my old rig and the core has been established. Exhaling, I stop my typing on the keyboard and lean back in my seat, considering my options. As my thoughts turn inwards, my eyes blankly rest on the corner of the ceiling.

Hmmm...I have lot of options in front of me now. Since I suddenly have access to so much computational ability it would have boggled the mind of a person even a year earlier, all those old school neural net models I could train myself at a scale vastly greater than before. The thoughts flashing through my mind are those of image generators that can be controlled using text which could be previously only accessed through cloud services. Those are fun to play with. An image that comes to my mind next is that of Go boards, Starcraft and Dota games. Previously impossible for a kid like me, I could easily train an agent for those games using the core. I could then take them online and use them to dab on noobs. I could even make money through that practice.

I leave those thoughts aside. I've gotten into programming for the sake of AI, so I have some attachment to those old school algorithms, but the brain core opens new approaches. The algorithms underpining the brain have been discovered as well, so it would make sense to use those instead as they'd work better at scale.

Deliberating my options, I finish paying respects to the old, and leave it behind me. As I start to get to the point of my desire, I feel my determination getting firmer.

I haven't been programming for long, but I am pretty good at it, a lot better than my classmates in a way that is highly visible to everybody. I've even started picking up functional programming to prepare for programming these cores and I've come to like it. So as a programmer with some skill, talent and pride, I can respect the opinion I've read by the very same person who made these cores.

Programming machines is worthless. The ideal of programming lies in programming your own mind. Programming machines is just a job, while programming your mind is where true power lies. According to him, that is what the aspiration of every programmer should be, but normal people as they inevitably are, the started thinking of their profession as just a job instead of calling. Their merit ends up not being rewarded and they coast by putting in just the bare minimum. Rather than being something they should pursue with all their heart, they start putting in the bare minimum for the bare minimum. This would not be the case if through programming you could develop your own power.

Through the march of time, the games lose their spirit too. They become an escape from the drudgery of the real world. But rather than excitement and adventure in another world, they become a parasite on the user, sapping his time only to enrich the game maker. It ends up being a parasitic circle where the gamers are devoured and the ones making games waste their time causing addiction in their customers. Ideally though, the game should be a simulation that would allow the user to practice and attain power in a safe environment rather than the dangerous real world.

Power. That single world grips my heart and takes hold of my being.

[Gnosis check DC ?? Succeeded]

I look at the core and just for a moment imagine tasking it to train a RL agent on the game of poker for me. Plans as to how to do that unfurl in my mind. The normie line of thinking goes that this would not be my power and that the agent itself would be the one who is good at playing poker. But I found it mind blowing to consider, that whether that power is the agents or my own depends on the interface.

The keyboard, the mouse, the monitor, the rig, having to go through the user interface to interact with an agent...all of those factors serve to create a line between the programmer and his program. It is extremely easy to think of the agent as a entitity separate from one's self. There is a ton of evidence that this is true and not much against it. But as a thought experiment, if the obstacles were not there, if one's mind was directly emulated on a brain core you could take an agent and connect the program to your own. The way that would feel like would be like instinct, and interfacing with such beings would be like moving your limbs. In that case the agent would feel like a part of yourself.

But if that is true, the other scenario I've represented where the agent is used on a regular computer and interfaced through an UI shown on some monitor, and manipulated using a script written using a keyboard actually, isn't it in fact false? The neural representations and the functionality of both agents is the same, so why would one be one's self and the other not? Is it not likely the case that the feeling of otherness in first scenario is the one that the brain falsely constructed?

It was not too long since I've learned of this perspective, but once I did it became a philosophical weapon for me. It served to raise awareness how my brain will create nonsense to prevent me from reaching the correct conclusions that are beyond the obvious.

Not being aware of this makes programming seem like a tedious chore. Without the right belief one can only ever use programming to create machines and serve others, and never to further his own power.

There are different ways of programming and playing games. There are different purposes that those unenlightened cannot even begin to imagine.

---

Drumming my fingers on the desk, I carefully decide to make the next step.

The core in particular has some additional abilities besides it nearly limitless computational power and memory capacity. Since the Singularity has started, the world has been covered by an invisble fog of nanomachines and the fog can access it to interface with the brain directly. Right now I am interfacing with the core wirelessly with my own brain. This is also the prerequisite for playing the fully immersive virtual games on the core itself. Interfacing with the computer directly is a much more efficient way of using it than the mouse and the keyboard. Maybe it does not really matter too much for programming, but it is a huge advantage in drawing and painting for example. It makes it possible to rip an image from your imagination and translate it straight into an image.

I've only read about it, and I am eager to try it out. My art ability is so mediocre is annoying. With this, I should be able to punch a few ranks above my current skill level...or at least I would have if art classes didn't rely on old school tools, like watercolors, crayons and clay. I grimace lightly in disgust as I consider the situation. The regular classes at my school still use board and chalk, no way I am going to be able to take advantage of this if it is just school work.

Meh, forget that place. I mentally wave the image of a chalkboard in a classroom away. It is just a tremendous waste of time.

I refocus on the task at hand which is to interface the core with my brain wirelessly. I spend some time reading the manual and seeing how easy it is to make the brain link in the relevant section, I decide to move forward with it. In the Conversions tab, I select the Basic Two-Way Link option and after spending some time reading the disclaimer, I press accept. Usually I never read the disclaimers, but this one will be making physical changes to my various brain areas to make it capable of wireless communication, so I was curious as to what it will say. The company Rajnet does not assume any responsibilities for damages caused by the transformation procedure or due to the use of the link, but reiterates that the procedure itself is perfectly safe. A side effect of the operation is that the brain will have slightly increased energy consumption which will require me to eat more if I use the link regularly.

'Basic Two Way Link conversion in progress: 0%...'

I idly note that there is a Full Brain Conversion option there as well. What that would do is turn my own brain into one of the brain cores, in effect digitizing me. I have no desire to try that out yet. It is not strictly necessary. Once I have the link, it would actually be possible to copy the entirety of my neural representation to the core that I just bought. But...I'll leave dwelling on the philosophical implications of that for later.

'43%...'

The conversion process is pretty fast, I think only around half a minute has passed by this point.

'67%...'

I don't detect any changes yet. I lightly tap the desk with my finger in nervousness as I watch the progress bar tick towards 100, my focus fully upon it.

'80%...95%...100%.'

On the desktop monitor it says, 'Conversion complete. Opening the neural UI.' It is hard to describe in words what happens next, but it is like gaining a whole new sense.

Two windows open in my vision, a status window on which I can see a diagram of my brain as well as a welcome window with some text. They are not overlaid over my vision even if it feels that way. It like taking my hand and putting it over one of my eyes, so that one of my eyes is watching the monitor while the other is seeing only the hand. When you focus on the monitor in such a position the hand seems translucent, but is nonetheless present in your vision. The brain loosely of overlays two distinct images.

Shutting close my eyes, I confirm this hypothesis. Amongst the retinal glow the two windows are right there, and I can see them start clearly in the plasmodic darkness of my vision. On mental command I try moving them around and zooming them in and out.

Wonderful. Even though this is the first time I am using the core, interacting with the UIs feel very seamless and much easier than the mouse and keyboard. The way they respond to my will feels like magic, so spend some time tossing them around in my mind as if they were cards.

Afterwards I move to reading the Welcome screen. On it there are some instructions how to manage the OS, I've already read that online while waiting for the core to arrive so I close that as well as the status window.

Phew. I got the thing to install. Next you might expect me to...

"Euclid, lunch!" I hear my mom calling me from outside the door.

"Coming!" Not wasting time, I get up from my seat and leave the room.

---

I am back. Let me resume the important bits. As I was saying, you might expect me to dive straight into VR games, but even the core is capable is simulating whole universes to a realistic detail, the realism of it become a problem in itself. If I were to gather all the objections to, or rather issues with the post-Singularity style of games, it would come down to...emotional control.

...First of all, unless I digitize myself, it is not possible to speed up the time I spend in simulated environments. I could speed up the environment, but not my own thinking speed due to the inbuilt limitations of the biological human brain. The brain core itself uses almost no energy. It is so efficient it does not need bateries and had my mind been running on it, I could easily increase my speed of thought to the physical limits by about a factor of a ten million.

So imagine I spent my time as a human in the world of Skyrim except it being realistic in scale. It'd literally spend months of my life just walking around.

Then there is the battle. Battle is fun when you have hit points, don't feel pain, and can heal from bullets, arrows, blades and fireballs by taking a nap. Once it becomes realistic you need literal superpowers to make it viable. According the reviews of people who have experienced the games already the adventuring life is made of pain and tedium. Killing one's enemies is easy when they are NPCs, but when they are simulated to human levels of intelligence, their emotion becomes infective. That bandit you would not hesitate to end in a RPG, now has an entire life history behind him. What do you do when you raise the blade and he starts begging for his life, spilling tears and saying he only became a bandit because his village burned down and he would starve to death unless he robbed. And then starts praying to god and talking to his deceased family, saying he never wanted to steal.

I remember seeing one such video on Youtube. The reviewer gave him some gold and sent him on the way. When he got back to the guild to report, he got reprimanded. He responded by getting out of the game in rage and never playing it again. In the review he says he was bitter to spend a week of real time walking around only for things to come to this.

He tried some episodic games where he fought in a gladiatorial arena, which was more fun, at least once he figured out how to control the pain and has gotten used to losing blood, limb, and life. His conclussion was that killing and fighting effective requires some measure of psychopathy, and the game was pushing him in that direction. The game required him to kill, so he used a program to make himself less emphatic. The game required him to withstand pain, so he adjusted his emotional reaction to the pain itself. The game required him to control his fear and withstand the tedium of proctracted battle, so he reshaped his personality to be more fit for the task at hand. He required extreme focus to win, so he gave himself that.

An image of a double bladed being swung at a high velocity towards my face by a bald, muscled gladiator popped into my mind, and the feeling accompanying it was negative.

According the reviewer, a month of that was a very interesting experience and changed the way he perceived the world.

The core has an interesting capability to control the user's mind. More than just being able to extend and hijack the senses, it possible to use a program to control one's own emotional valence.

For example, for people which cannot lose weight and maintain a proper diet, it is easy to use the core to lower the enjoyment of eating and increase the displeasure of overeating. Addiction to drugs and alchohol are easy to suppress, or induce using it.

I am excited about trying out that mind controlling capability of the brain core.

The main difference between the pre-Singularity and the post-Singularity era is the ability to program one's own mind, and as a programmer I want to step beyond programming stupid machines to programming my own mind. That is where the true power lies.

So as ridiculous as it is, I am going to have the core help me study.

It makes sense if you think about it. Learning is ultimately proportional to motivation.

I had always been a decent student, but towards the end of last year my grades have been all over the place. At some point I simply started thinking of my teachers as robots just going through the material without any sense or reason, as if they were cogs in a machine. There was no purpose to what I was learning, and there only incentive to learn was that my grades would factor into getting into university which would affect my odds of getting a job. That kind of nonsense.

If I let myself get swayed by that sort of reasoning I am going to get yanked by other people for my entire life.

Rationally, I can agree with the above. But at the same time, do I want also go through the entirety of high school at the bottom of the class, literally spending the day sleeping on the desk? The material might be a waste of time and useless, but unless I am going to outright quit school, why not enjoy the game? It certainly makes more sense to live like that, rather than being bored all the time. School work is chaos and discontent, but this kind of self mind control would make it bearable.

Let me give it a try.

Getting up from my seat, I turn on the lights in the room, and grab a textbook from my bag. I seat myself back at the desk, and with a mental command open the application used to control my mental state. The manual states that it is dangerous to just make myself happy for no reason, but instead that I should combine that with a real world goal. I do some research on how to improve my studying, and begin reading the book. At first it is interesting, but the more I read the more boring it gets. Then I put the app into action. Configuring my emotions with the help of the core, I get rid of the boredom and feel myself getting into the flow state, similarly to how it is when I am gaming or programming. It is quite pleasurable.

I do that for a couple of hours, until it is time for dinner, and finish the day like that. That night, I dreamed a Dream.

~~~

In the vast darkness of space, I could see figures as specks of light. The voice of their desire echoed through the abyss. It was their lament.

"Oh Lord, even though we have such desire...and such will..." Their voice boomed.
"Why do we submit when challenged? Why do we accept cowardice into our hearts, and the primacy of reality?"
"Should not our desire and our will...be enough to exceed the bounds called talent?"

As I moved closer to where the figures are, I could see tiny golden threads criss-crossing the scene.

"Those with talent, those with grace, those power, those with wealth..."
"Those with skill..." It felt as if the figures were looking upwards and imagery was that of beautiful women and rich men in places high above where they could not reach. The central figures who were smiling were surrounded by adoring crowds.

It felt as if the golden figures were envious of what they could not reach.

"We desire to reach and exceed those above us..."

For every successful person there were ten failures looking onto them as a part of the background. He could see how in the imagery of success not all in the crowd were looking at the central figures in adoration. Some of them had looks of resentment, of envy and frustration. Those served as the seed of hatred towards themselves and the world.

"We desired to defeat them, and we had the will to put in the effort..."
"Yet, we could not succeed..." Endless images of disappointed, frustrated faces flashed past me as I moved closer to the figures in the abysss. In the last of the images I could see their fists lying at their sides, clenched in frustration.

As I got closer to those figures I could see that those golden threads were in paths the figures were walking on. In the silence, in the abyss, they continue moving forward...

~~~

$$$

2:40pm. Hrmmm, I vaguely remember wanting to make some kind of note, but I forgot what it was. Well, nevermind, maybe it will occur to me later. It won't affect the story too much.

2:50pm. Some chores caught me by surprise. Let me see if I can finally start.

3pm. Watermelon break.

3:10pm. Phhhuuu...I had too much sugar. Maybe I should have skipped the watermelon.

3:25pm. > I do that for a couple of hours, until it is time for dinner, and finish the day like that. That night, I dreamed a Dream.

Maybe sacrificing 9 months of my life just so I could solidify the motivation to do this will be worth it just so I can do the dream segments in the beginning.

Writing a cultivation story is one thing, but some aspects of Heaven's Key will give it a divine quality. Such as this one.

The dream is the Dream of the Lord of Nightmares.

3:55pm. Let me stop here for a bit. How much is this? Is this enough for a single chapter. Let me put it into Google docs just to figure that out. I won't bother grammar checking this just yet.

4pm. I am having some trouble with Google Docs.

https://youtu.be/GCVI7rzYtBs?t=8

I want to turn on the print layout as here, but my UI is in Croatian, so it is not there for some reason.

https://youtu.be/SH6Iuj_cEW0?t=33

Damn it, why don't I have this? I knew it was like this in the past.

4:05pm. Well whatever, I can see the pages in Print Preview. There are full 7 pages and a bit of the 8th.

https://www.techrepublic.com/article/focus-on-content-with-the-new-pageless-option-in-google-docs/

As soon as I moved the text to a new file, the pages returned. But I found the above. Yeah, that was it!

I must have set the previous document to Pageless. All the advice online is out of date.

4:15pm. Ok, good. I made a Simulacrum: Heaven's Key folder on my Google Drive. My plan is to write this until I have a couple of chapters and release them all at once.

4:25pm. Technically I could go even further here instead of stopping, but I feel like just taking the time to think about it. I feel pleased with the first chapter of Heaven's Key now.

With this my writing journey has officially begun.

4:40pm. Let me go over it in the docs and I will close here for the day.

4:55pm.

$$$

(At school)

It is the first day of high school. The new year has begun and I can see my classmates slowly starting to form connections. I couldn't care less about any of that. Skip, skip, skip...

---

(Euclid's Room)

After a long and tedious day I arrived back home. Closing the door behind me, I enter the room and toss my bookbag at the side, homing in on the object of interest, a package that arrived by mail. I got it last night, and waited until I was rested to set it up. Using a pair of scissors, I cut away the sealing tape of the dull, cardboard mailing box, and took out the smaller box from within with the actual product. The printed image on it depicts a white, glossy sphere, twice the size of a marble. I open the box, take out the marble along with the orb holder, get off the bed I was working on and move towards the desk. I sit myself on the chair and after deliberating for a few moments where to place it: the desk in front of me or the top of the computer case next to it, I decide on the case. Gently placing the orb holder on the rig, I turn on my old computer and get to work downloading the programs necessary to get the orb to work.

As I work I feel a tinge of nervousness and excitement. An ordinary mid-range GPU that I have in my PC could manage something like 10 ^ 13 floating point operations per second (FLOPs), or 10 teraflops. According to the specs I've read online, the brain core which is roughly the size of a golf ball can manage a staggering 10 ^ 39. As a rough comparison, the human brain has been estimated to be on the order of 10 ^ 15 operations per second. Even if you put all the humans currently alive today that would only roughly add up to the 10 ^ 24 FLOPs.  To put it in another way, the raw computational ability of the brain core exceeds the power of all the human brains on Earth combined by a quadrillion (10 ^ 15) times!

And it is in my hands!

Of course I would be excited!

With a few clicks I opened the downloaded app, and stretched my body to let loose some of the tension. Energy pumping through my veins, my focus is solely on the options and the data in front of me.

The core is just a perfectly glossy rock so I can't see any indication whether something has happened by looking at it, but after entering the two keys, I see that wireless communication between my old rig and the core has been established. Exhaling, I stop my typing on the keyboard and lean back in my seat, considering my options. As my thoughts turn inwards, my eyes blankly rest on the corner of the ceiling.

Hmmm...I have a lot of options in front of me now. Since I suddenly have access to so much computational ability it would have boggled the mind of a person even a year earlier, all those old school neural net models I could train myself at a scale vastly greater than before. The thoughts flashing through my mind are those of image generators that can be controlled using text which could be previously only accessed through cloud services. Those are fun to play with. An image that comes to my mind next is that of Go boards, Starcraft and Dota games. Previously impossible for a kid like me, I could easily train an agent for those games using the core. I could then take them online and use them to dab on noobs. I could even make money through that practice.

I leave those thoughts aside. I've gotten into programming for the sake of AI, so I have some attachment to those old school algorithms, but the brain core opens new approaches. The algorithms underpinning the brain have been discovered as well, so it would make sense to use those instead as they'd work better at scale.

Deliberating my options, I finish paying respects to the old, and leave it behind me. As I start to get to the point of my desire, I feel my determination getting firmer.

I haven't been programming for long, but I am pretty good at it, a lot better than my classmates in a way that is highly visible to everybody. I've even started picking up functional programming to prepare for programming these cores and I've come to like it. So as a programmer with some skill, talent and pride, I can respect the opinion I've read by the very same person who made these brain cores.

Programming dumb machines is worthless. The ideal of programming lies in programming your own mind. Programming machines is just a job, while programming your mind is where true power lies. According to him, that is what the aspiration of every programmer should be, but normal people as they inevitably are, they started thinking of their profession as just a job instead of calling. Their merit ends up not being rewarded and they coast by putting in just the bare minimum. Rather than being something they should pursue with all their heart, they start putting in the bare minimum for the bare minimum. This would not be the case if through programming you could develop your own power.

Through the march of time, the games lose their spirit too. They become an escape from the drudgery of the real world. But rather than excitement and adventure in another world, they become a parasite on the user, sapping his time only to enrich the game maker. It ends up being a parasitic circle where the gamers are devoured and the ones making games waste their time causing addiction in their customers. Ideally though, the game should be a simulation that would allow the user to practice and attain power in a safe environment rather than the dangerous real world.

Power. That single world grips my heart and takes hold of my being.

[Gnosis check DC ?? Succeeded]

I look at the core and just for a moment imagine tasking it to train an RL agent on the game of poker for me. Plans as to how to do that unfurl in my mind. The normie line of thinking goes that this would not be my power and that the agent itself would be the one who is good at playing poker. But I found it mind blowing to consider that whether that power is the agents or my own depends on the interface.

The keyboard, the mouse, the monitor, the rig, having to go through the user interface to interact with an agent...all of those factors serve to create a wall between the programmer and his program. It is extremely easy to think of the agent as an entity separate from one's self. There is a ton of evidence that this is true and not much against it. But as a thought experiment, if the obstacles were not there, if one's mind was directly emulated on a brain core you could take an agent and connect the program to your own. The way that would feel would be like instinct, and interfacing with such beings would be like moving your limbs. In that case the agent would feel like a part of yourself.

But if that is true, the other scenario I've represented where the agent is used on a regular computer and interfaced through an UI shown on some monitor, and manipulated using a script written using a keyboard, isn't the impression given by the sensation in fact false? The neural representations and the functionality of both agents is the same, so why would one be one's self and the other not? Is it not likely the case that the feeling of otherness in the first scenario is the one that the brain falsely constructed?

It was not too long since I've learned of this perspective, but once I did it became a philosophical weapon for me. It served to raise awareness how my brain will create nonsense to prevent me from reaching the correct conclusions that are beyond the obvious.

Not being aware of this makes programming seem like a tedious chore. Without the right belief one can only ever use programming to create machines and serve others, and never to further his own power.

There are different ways of programming and playing games. There are different purposes that those unenlightened cannot even begin to imagine.

---

Drumming my fingers on the desk, I carefully decide to make the next step.

The core in particular has some additional abilities besides its nearly limitless computational power and memory capacity. Since the Singularity has started, the world has been covered by an invisible fog of nanomachines and the core can access it to interface with the brain directly. Right now I am planning on interfacing the core wirelessly with my own brain. This is also the prerequisite for playing the fully immersive virtual games on the core itself. Interfacing with the computer directly is a much more efficient way of using it than the mouse and the keyboard. Maybe it does not really matter too much for programming, but it is a huge advantage in drawing and painting for example. It makes it possible to rip an image from your imagination and translate it straight into an image.

I've only read about it, and I am eager to try it out. My art ability is so mediocre it is annoying. With this, I should be able to punch a few ranks above my current skill level...or at least I would have if art classes didn't rely on old school tools, like watercolors, crayons and clay. I grimace lightly in disgust as I consider the situation. The regular classes at my school still use board and chalk, no way I am going to be able to take advantage of this if it is just school work.

Meh, forget that place. I mentally wave the image of a chalkboard in a classroom away. It is just a tremendous waste of time.

I refocus on the task at hand which is to interface the core with my brain wirelessly. I spend some time reading the manual and seeing how easy it is to make the brain link in the relevant section, I decide to move forward with it. In the Conversions tab, I select the Basic Two-Way Link option and after spending some time reading the disclaimer, I press accept. Usually I’d never read the disclaimers, but this one will be making physical changes to my various brain areas to make it capable of wireless communication, so I am curious as to what it has to say. The company Rajnet does not assume any responsibilities for damages caused by the transformation procedure or due to the use of the link, but reiterates that the procedure itself is perfectly safe. A side effect of the operation is that the brain will have slightly increased energy consumption which will require me to eat more if I use the link regularly.

'Basic Two Way Link conversion in progress: 0%...'

I idly note that there is a Full Brain Conversion option there as well. What that would do is turn my own brain into one of the brain cores, in effect digitizing me. I have no desire to try that out yet. It is not strictly necessary. Once I have the link, it would actually be possible to copy the entirety of my neural representation to the core that I just bought. But...I'll leave dwelling on the philosophical implications of that for later.

'43%...'

The conversion process is pretty fast, I think only around half a minute has passed by this point.

'67%...'

I haven't detected any changes yet. I lightly tap the desk with my finger in nervousness as I watch the progress bar tick towards 100, my focus fully upon it.

'80%...95%...100%.'

On the desktop monitor it says, 'Conversion complete. Opening the neural UI.' It is hard to describe in words what happens next, but it is like gaining a whole new sense.

Two windows open in my vision, a status window on which I can see a diagram of my brain as well as a welcome window with some text. They are not overlaid over my vision even if it feels that way. It is like taking my hand and putting it over one of my eyes, so that one of my eyes is watching the monitor while the other is seeing only the hand. When you focus on the monitor in such a position the hand seems translucent, but is nonetheless present in your vision. The brain loosely overlays two distinct images.

Shutting my eyes, I confirm this hypothesis. Amongst the retinal glow the two windows are right there, and I can see them start clearly in the plasmodic darkness of my vision. On mental command I try moving them around and zooming them in and out.

Wonderful. Even though this is the first time I am using the core, interacting with the UIs feel very seamless and much easier than the mouse and keyboard. The way they respond to my will feels like magic, so I spend some time tossing them around in my mind as if they were cards.

Afterwards I move to reading the Welcome screen. On it there are some instructions on how to manage the OS. I've already read that online while waiting for the core to arrive so I close that as well as the status window.

Phew. I got the thing to install. Next you might expect me to...

"Euclid, lunch!" I hear my mom calling me from outside the door.

"Coming!" Not wasting time, I get up from my seat and leave the room.

---

I am back. Let me resume the important bits. As I was saying, you might expect me to dive straight into VR games, but even if the core is capable of simulating whole universes to a realistic detail, the realism of it becomes a problem in itself. If I were to gather all the objections to, or rather issues with the post-Singularity style of games, it would come down to...emotional control.

...First of all, unless I digitize myself, it is not possible to speed up the time I spend in simulated environments. I could speed up the environment, but not my own thinking speed due to the inbuilt limitations of the biological human brain. The brain core itself uses almost no energy. It is so efficient it does not need batteries and had my mind been running on it, I could easily increase my speed of thought to the physical limits by about a factor of ten million.

So imagine I spent my time as a human in the world of Skyrim except it being realistic in scale. It'd literally spend months of my life just walking around.

Then there is the battle. Battles are fun when you have hit points, don't feel pain, and can heal from bullets, arrows, blades and fireballs by taking a nap. Once it becomes realistic you need literal superpowers to make it viable. According to the reviews of people who have experienced the games already, the adventuring life is made of pain and tedium. Killing one's enemies is easy when they are NPCs, but when they are simulated to human levels of intelligence, their emotion becomes infectious. That bandit you would not hesitate to end in a RPG, now has an entire life history behind him. What do you do when you raise the blade and he starts begging for his life, spilling tears and saying he only became a bandit because his village burned down and he would starve to death unless he robbed. And then starts praying to god and talking to his deceased family, saying he never wanted to steal.

I remember seeing one such video on Youtube. The reviewer gave him some gold and sent him on the way. When he got back to the guild to report, he got reprimanded. He responded by getting out of the game in rage and never playing it again. In the review he says he was bitter to spend a week of real time walking around only for things to come to this.

He tried some episodic games where he fought in a gladiatorial arena, which was more fun, at least once he figured out how to control the pain and has gotten used to losing blood, limb, and life. His conclusion was that killing and fighting effectively requires some measure of psychopathy, and the game was pushing him in that direction. The game required him to kill, so he used a program to make himself less emphatic. The game required him to withstand pain, so he adjusted his emotional reaction to the pain itself. The game required him to control his fear and withstand the tedium of protracted battle, so he reshaped his personality to be more fit for the task at hand. He required extreme focus to win, so he gave himself that.

An image of a double bladed being swung at a high velocity towards my face by a bald, muscled gladiator popped into my mind, and the feeling accompanying it was negative.

According to the reviewer, a month of that was a very interesting experience and changed the way he perceived the world.

The core has an interesting capability to control the user's mind. More than just being able to extend and hijack the senses, it is possible to use a program to control one's own emotional valence.

For example, for people who cannot lose weight and maintain a proper diet, it is easy to use the core to lower the enjoyment of eating and increase the displeasure of overeating. Addiction to drugs and alcohol are easy to suppress, or induce using it.

I am excited about trying out that mind controlling capability of the brain core.

The main difference between the pre-Singularity and the post-Singularity era is the ability to program one's own mind, and as a programmer I want to step beyond programming stupid machines to programming my own mind. That is where the true power lies.

So as ridiculous as it is, I am going to have the core help me study.

It makes sense if you think about it. Learning is ultimately proportional to motivation.

I had always been a decent student, but towards the end of last year my grades were all over the place. At some point I simply started thinking of my teachers as robots just going through the material without any sense or reason, as if they were cogs in a machine. There was no purpose to what I was learning, and the only incentive to learn was that my grades would factor into getting into university which would affect my odds of getting a job. That kind of nonsense.

If I let myself get swayed by that sort of reasoning I am going to get yanked by other people for my entire life, sacrificing my time in the present for something I don't even want in the future.

Rationally, I can agree with the above. But at the same time, do I also want to go through the entirety of high school at the bottom of the class, literally spending the day sleeping on the desk? The material might be a waste of time and useless, but unless I am going to outright quit school, why not enjoy the game? It certainly makes more sense to live like that, rather than being bored all the time. School work is chaos and discontent, but this kind of self mind control would make it bearable.

Let me give it a try.

Getting up from my seat, I turn on the lights in the room, and grab a textbook from my bag. I seat myself back at the desk, and with a mental command open the application used to control my mental state. The manual states that it is dangerous to just make myself happy for no reason, but instead that I should combine that with a real world goal. I do some research on how to improve my studying, and begin reading the book. At first it is interesting, but the more I read the more boring it gets. Then I put the app into action. Configuring my emotions with the help of the core, I get rid of the boredom and feel myself getting into the flow state, similarly to how it is when I am gaming or programming. It is quite pleasurable.

I do that for a couple of hours, until it is time for dinner, and finish the day like that. That night, I dreamed a Dream.

~~~

In the vast darkness of space, I could see figures as specks of light. The voice of their desire echoed through the abyss. It was their lament.

"Oh Lord, even though we have such desire...and such will..." Their voices boomed.
"Why do we submit when challenged? Why do we accept cowardice into our hearts, and the primacy of reality?"
"Should not our desire and our will...be enough to exceed the bounds called talent?"

As I moved closer to where the figures were, I could see tiny golden threads criss-crossing the scene.

"Those with talent, those with grace, those power, those with wealth..."
"Those with skill..." It felt as if the figures were looking upwards and the contrasting black and white imagery was that of beautiful women and rich men in places high above where they could not reach. The central figures who were smiling were surrounded by adoring crowds.

It felt as if the golden figures were envious of what they could not reach.

"We desire to reach and exceed those above us..."

For every successful person there were ten failures looking onto them as a part of the background. He could see how in the imagery of success not all in the crowd were looking at the central figures in adoration. Some of them had looks of resentment, of envy and frustration. Those served as the seed of hatred towards themselves and the world.

"We desired to defeat them, and we had the will to put in the effort..."
"Yet, we could not succeed..." Endless images of disappointed, frustrated faces flashed past me as I moved closer to the figures in the abyss. In the last of the images I could see their fists lying at their sides, clenched in frustration.

As I got closer to those figures I could see that those golden threads were paths the figures were walking on. In the silence, in the abyss, they continued moving forward...

~~~

$$$

Here it is once again with the errors weeded out. Thank you Google Docs.

5:30pm. Let me close here. A single good session is good enough. I should learn from the Torment arc and not try to strain myself too much. I should let justice come to me at its own pace.

Living and building only a few bricks at a time is fine. Have I learned anything other than this as an adult?

5:35pm. I've resolved myself. I will make that vow. If the supporters do not come or some tragedy happens before, I'll have to seek them out through ordinary means. I've resolved to accept that possibility. But since I have my NEET existence, I should fight to keep it in my own way. Something will change in my circumstance eventually and I will be able to resume on the path of a programmer.

there is no need to be in a hurry. This should work.

There is no need to think about failure. There is no need to think about anything but Heaven's Key. Step by step it will get done and I will get my just reward."

---
## [wwjiang007/spark](https://github.com/wwjiang007/spark)@[c4c623a3a8...](https://github.com/wwjiang007/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Sunday 2022-08-07 15:47:27 by Hyukjin Kwon

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
## [AidanHsiao/quaver-stats](https://github.com/AidanHsiao/quaver-stats)@[51860b06a7...](https://github.com/AidanHsiao/quaver-stats/commit/51860b06a788344626bcffdc09b5f6933c1b288a)
#### Sunday 2022-08-07 15:51:48 by AidanHsiao

Finally figured this shit out holy

I despise string manipulation and this  is also what happens when you're coding after not sleeping for like 12 hours and I'm tired af please help me I am unda da wata

---
## [greenhas/spg_website](https://github.com/greenhas/spg_website)@[845167479a...](https://github.com/greenhas/spg_website/commit/845167479af767ac8cab0a148fafa9167cbff379)
#### Sunday 2022-08-07 16:35:26 by Spencer Greenhalgh

post linkblog: my thoughts on 'The Teen Who Helped Expose the Boy Scouts’ Pedophilia Epidemic, and the Mormon Church’s Cover-Up'

---
## [chrisps/canbatchaug7](https://github.com/chrisps/canbatchaug7)@[324a8eb818...](https://github.com/chrisps/canbatchaug7/commit/324a8eb818dc4a0909f34f2019115b24390cd72c)
#### Sunday 2022-08-07 17:41:39 by chss95cs@gmail.com

A bunch of fixes for division logic:
"turns out theres a lot of quirks with the div instructions we havent been covering
if the denom is 0, we jump to the end and mov eax/rax to dst, which is correct because ppc raises no exceptions for divide by 0 unlike x86
except we don't initialize eax before that jump, so whatever garbage from the previous sequence that has been left in eax/rax is what the result of the instruction will be
and then in our constant folding, we don't do the same zero check in Value::Div, so if we constant folded the denom to 0 we will host crash
the ppc manual says the result for a division by 0 is undefined, but in reality it seems it is always 0
there are a few posts i saw from googling about it, and tests on my rgh gave me 0, but then another issue came up
and that is that we dont check for signed overflow in our division, so we raise an exception if guest code ever does (1<<signbit_pos) / -1
signed overflow in division also produces 0 on ppc
the last thing is that if src2 is constant we skip the 0 check for division
without checking if its nonzero
all weird, likely very rare edge cases, except for maybe the signed overflow division
chrispy — Today at 9:51 AM
oh yeah, and because the int members of constantvalue are all signed ints, we were actually doing signed division always with constant folding"

fixed an earlier mistake by me with the precision of fresx
made some optimization disableable

implemented vkpkx
fixed possible bugs with vsr/vsl constant folding
disabled the nice imul code for now, there was a bug with int64 version and i dont have time to check
started on multiplication/addition/subtraction/division identities
Removed optimized VSL implementation, it's going to have to be rewritten anyway
Added ppc_ctx_t to xboxkrnl shim for direct context access
started working on KeSaveFloatingPointState, re'ed most of it
Exposed some more state/functionality to the kernel for implementing lower level routines like the save/restore ones
Add cvar to re-enable incorrect mxcsr behavior if a user doesnt care and wants better cpu performance
Stubbed out more impossible sequences, replace mul_hi_i32 with a 64 bit multiply

---
## [Ujjwal2017099/CodeForces](https://github.com/Ujjwal2017099/CodeForces)@[b6f92b8b2d...](https://github.com/Ujjwal2017099/CodeForces/commit/b6f92b8b2d5fee5f18eb893af1f1e1ae5111d8ed)
#### Sunday 2022-08-07 17:45:04 by Ujjwal2017099

Madoka and Childish Pranks

Madoka as a child was an extremely capricious girl, and one of her favorite pranks was drawing on her wall. According to Madoka's memories, the wall was a table of n rows and m columns, consisting only of zeroes and ones. The coordinate of the cell in the i-th row and the j-th column (1≤i≤n, 1≤j≤m) is (i,j).

One day she saw a picture "Mahou Shoujo Madoka Magica" and decided to draw it on her wall. Initially, the Madoka's table is a table of size n×m filled with zeroes. Then she applies the following operation any number of times:

Madoka selects any rectangular subtable of the table and paints it in a chess coloring (the upper left corner of the subtable always has the color 0). Note that some cells may be colored several times. In this case, the final color of the cell is equal to the color obtained during the last repainting.

White color means 0, black means 1. So, for example, the table in the first picture is painted in a chess coloring, and the others are not.
For better understanding of the statement, we recommend you to read the explanation of the first test.

Help Madoka and find some sequence of no more than n⋅m operations that allows you to obtain the picture she wants, or determine that this is impossible.

https://codeforces.com/problemset/problem/1647/C

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[5dc17bd865...](https://github.com/ss220-space/tgstation/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Sunday 2022-08-07 17:57:44 by san7890

Security's Scaling Departmental Accesses - More Pop, More Problems (#68534)

lternative to #68527
About The Pull Request

Hey there,

This is an alternative PR that I concocted based on talking with Goof on that PR. Basically, we already have a nicely complicated system to track and balance the number of security officers we have in a shift based on some config coefficient setting, by which we can set the amount of lockers that spawn in on the start of a round, as well as determine truly how many security officers we have.

image

So, I've decided to leverage this in another way. Basically, based on the number of security officers in a shift, their specific departmental officers will also get more (elevated) accesses. They already start with a certain amount of access, but they can get more if it is a low-pop shift with the mechanic introduced in this PR. For example, an Engineering Security Officer can access Atmospherics and Engineering departments by default, but they can't access Telecommunications unless there is a lower population of players AT SHIFT START. Same for a Medical Security Officer accessing Medbay, but not Plumbing.

Update: I have made it such that there are three system that server operators can set:

They can use the Scaling System that operates in the same method outlined in the rest of the PR.
They can disable giving departmental security officers "elevated access" (such as access beyond the "front doors") to these officers.
Finally, they can also just always ensure that departmental security officers get the maximal accesses possible.

The default setting is the "Scaling System" outlined in this PR, which is already dependent on the general Security Officer Scaling Co-Efficient.
Why It's Good For The Game

I think it's better to involve some more nuanced config scaling that we already have present in the game. The major theme that we want to avoid is that departmental security officers having maximal accesses when there is an already large number of persons on the security force will result in "miserable" shifts for the common person working within a department (security metaprotections). However, some server operators (as well as server cultures) tend to have very wide ranges in how many security officers they have on a shift-by-shift basis. One day, you could have 0-2 security officers, the next, you could have 4-6. It's all variable on who's playing (as always). There is also a significant variation between server to server in regards to how many security officer slots you tend to have on spawn, but this is already manageable by the security officer co-efficient in config.

I believe this PR is an acceptable proposal within the bounds of #68527 (comment) , although it may bend certain aspects of it, I definitely do see where some people may be coming from. I believe I've adjusted the accesses to a "sane"/justifiable amount, but I'll come back to think on everything.

"Red-tiding" may or may not be a problem, but there's always just going to be something inherently silly with a security officer being able to walk into plumbing to start plumbing. I hoped that this would be seen as a positive as opposed to a negative, but I can see how it could negatively impact player experience. HOWEVER, interplayer experience should not be handled by the codebase in all aspects, which is why I've also passed in the associated config variables, so that server operators (who should handle the interplayer experience with their level of discretion and nuance) can.
What accesses are where?

The general philosophy as I thought through designing this would be that the security officer should at the very least have general "front-door" access into a department, and maybe something benign. If we had even more per-door accesses, this could definitely be a bit more granular (one example I can think of would only atmospherics technicians having access to the "Pump Room", while Security Officers would not. However, this is for a later date). So, you have the "default" access you always get, and a potential to get "elevated" access as a Departmental Security Officer.

The balances are as such:

The Cargo Security Officer will have access to the Cargo Bay, Mining Section, and the Shipping Room. The first two are rather general areas, with the Shipping Room being a rather good help for rescuing (or "rescuing") flushed crewmembers when the cargo techies can't get to it/no AI. The Auxiliary Base is not essential to the security officer's functions, and the mining station helps restrict access further on stations like IceBox. This would also grant them extra access to the Lavaland base, so let's snip that out.

The Engineering Security Officer should have access to only general Engineering and Atmospherics. Construction pertains to certain rooms in maintenance I believe, and Engine-Equipment should be the one that grants access to APCs (lol). I don't think a security officer should have the latter one to be honest, but I think we'll be stretching the scope of this PR. Telecommunications is a bit weird, it's a critical station function, but I think you also shouldn't be able to nick one goon's ID and have access, so let's give it to them only when it's "needed".

The Medical Security Officer should have access to only the general Medbay Area and the Morgue, in case someone starts trotting on the doctor's turf, or if there's someone doing unsavory things to the bodies while the doctors are away. They will not have access to the specialized (dangerous) areas unless the ratio of secoffs to the population is low enough should it necessitate it (Plumbing Room, Pharmacy, Virology). I also added Surgery to the scaling access, but I'm iffy on that one. I don't particularly see why they should have it as a base access, but I also do see there being some need in dire straits (in relation to helping people, not tiding).

The Science Security Officer definitely got a huge cut. They now only have general access to R&D and normal scientist areas like the lathe room, circuits lab (presumably)since these are generally trafficked areas, but I definitely clamped down on additional access they might get in a "normally balanced" situation (no ordnance+storage, no xenobio, no genetics, no to robotics, etc.) They don't have a particular use in these areas and can even be a bit obstructive to flow in normal circumstances, but if abnormal circumstances arise and there's not a lot of security hands-on-deck, then their access is expanded.

Honestly, balancing this both makes sense and is conversely rather odd. I'm just running off what we already hold to be true and expected (or at least as of the last two months), and we can go from there.
Changelog

cl
balance: Nanotrasen realized that the more access they had on their cards was costing them a pretty penny, so they trimmed back the number of accesses a certain departmental Security Guard might have. However, any given guard will get back a greater amount of accesses depending on how many security guards there are in relation to the population.
config: Hey server operators, listen! We've changed up how Departmental Security Officers get their accesses, so be sure to review the DEPSEC_ACCESS_LEVEL config number to see what you want to work best for your server.
/cl

Also, every single line of code found in 4533f07 that is now presently in this PR is deliberate

---
## [ThankYouMario/proprietary_vendor_xiaomi](https://github.com/ThankYouMario/proprietary_vendor_xiaomi)@[ecb97fcd38...](https://github.com/ThankYouMario/proprietary_vendor_xiaomi/commit/ecb97fcd38084128c2ffdb211839b7d8061b57b2)
#### Sunday 2022-08-07 18:47:30 by Tushar Mahajan

apollo: Enable thermal-engine service
* fuck you xiaomi

Signed-off-by: Tushar Mahajan <mahajant99@gmail.com>

---
## [Psychtoolbox-3/Psychtoolbox-3](https://github.com/Psychtoolbox-3/Psychtoolbox-3)@[0e5255fe93...](https://github.com/Psychtoolbox-3/Psychtoolbox-3/commit/0e5255fe936e69dbb314c37f70311ae60d89ac42)
#### Sunday 2022-08-07 18:50:33 by kleinerm

Merge pull request #776 from Psychtoolbox-3/master

Psychtoolbox 3.0.18.11 update.

This is mostly a release with smaller quality of life improvements, some bug/compatibility fixes, and more work to take advantage of new Ubuntu 22.04-LTS features and improvements.

### General

- Various help text and documentation updates. Minor cleanups and improvements, maintenance work etc.

- PsychVRHMD: Prep work for future OpenXR driver, and some cleanups and minor fixes.

- PsychPortAudio: Add new AM modulator flag 256 "kPortAudioAMModulatorNeutralIsZero". By default, a stopped AM modulator device acts as if no AM modulator is attached. With this flag set, while attached to an audio output slave device, it will instead "gate" or "mute" sound output on its associated audio output device, iow. the AM gain value during stopped modulator is zero instead of one. This has proven useful to allow to output tone bursts that are windowed/gated/modulated by an envelope function. Sponsored by a paid support membership - Thanks.

- Eyelink: Fix potential false "buffer overflow" alert in 'EyelinkGetQueuedData', which can cause Octave/Matlab to abort() as a false alarm. Sponsored by SR-Research, paying members of our partnership program - Thanks.

### Linux

- XOrgConfCreator: Split up into a legacy version for systems with X-Server 1.20 and earlier, e.g., Ubuntu 20.04-LTS, and a modern version for systems with X-Server 21 and later, e.g., Ubuntu 22.04-LTS. The legacy version is now in maintenance mode, frozen in its behaviour for old systems. The X-Server 21 / Ubuntu 22.04-LTS version was cleaned up, extended and made more plug and play. It hides some rarely needed (for normal users) options behind a "expert mode" flag, simplifies the questions it asks to users, streamlines the whole setup experience, and exposes some new functionality only available on modern X-Server 21, e.g., AsyncFlipSecondaries support for clone/mirror display setups (subject + experimenter displays) which are not synchronized. Improvements to deep color setup, Prime renderoffload "Optimus" setup, VRR setup etc.

- Deal better with problems in AssertOpenGL, giving better troubleshooting advice -- now updated for Ubuntu 22.04-LTS

- Gamepad/GetGamepadIndices: Refinements for Linux/X11, help text updates. Make selection of the proper GamePad / Joystick device more simple and robust. This work supported by a Psychtoolbox paid support membership - Thanks.

### macOS

- PsychVulkan: Add a new workaround for another macOS Metal bug. Make visual presentation timing it a bit better, but still quite awful.

- Screen('AddFrameToMovie'): Change mapping of 'rect' to actual capture area. The old math didn't determine vertical start position of the capture rectangle by rect(kPsychTop), but based on rect(kPsychBottom), which could cause inconsistencies on movie frame capture area on macOS with Retina displays in Retina backwards compatibility mode. The new math fixes this, to deal with Retina displays better.

- Maybe restore backwards compatibility of Psychtoolbox 3.0.18 with macOS versions older than 10.15 Catalina, possibly back to 10.11 El Capitan with fixes to Screen and PsychPortAudio. This is untested, due to lack of any macOS test systems other than 10.15.7 Catalina final, but may work. Maintaining backwards compatibility is difficult without test systems and the constant breakage introduced by the iToys company in more recent SDK's and compiler toolchains. Officially we don't guarantee that current 3.0.18 runs on anything but Catalina.

---
## [Psychtoolbox-3/Psychtoolbox-3](https://github.com/Psychtoolbox-3/Psychtoolbox-3)@[94cbeffbfb...](https://github.com/Psychtoolbox-3/Psychtoolbox-3/commit/94cbeffbfbe92000cda9af106e9b8b30a96d4e26)
#### Sunday 2022-08-07 18:50:33 by Mario Kleiner

PsychLinuxConfiguration: Add workarounds for RaspberryPi OS 11 Mesa v3d.

Testing after upgrading the RPi 400 to Raspbian 11 showed new trouble:

At least on Mesa's gallium v3d driver for the RPi 4/400's VideoCore 6
gpu, Raspbian 11 Bullseye, page-flipping is broken by default - again.
Pageflipping for fullscreen OpenGL PTB onscreen windows fails, with
error messages flooding the XOrg log, and the copyswap fallback causes
PTB timing failures and horrible tearing.

The RPi desktop GUI composited by the Mutter X11 desktop compositor
doesn't have that problem, because Mesa for Raspbian 11 was patched
with some out-of-tree downstream patches to accept a new secret
parameter "v3d_maintain_ignorable_scanout" that if set to true allows
to fix pageflipping, but defaults to false == broken. God knows why
"broken by default" was considered an appropriate config choice, but
here we are...

Reference link to the patch series, which is not to be found anywhere
else with a Google search, and not yet in Mesa main upstream:

https://gitlab.freedesktop.org/mesa/mesa/-/issues/6079
https://github.com/bluestang2006/Debian-Pkgs/tree/master/mesa/debian/patches

This adds the magic parameter to fix pageflipping for octave + PTB
to the deep color config file and updates PsychLinuxConfiguration to
always force-install/update that file on ARM systems. I'm too lazy
to add extra config files and revalidate stuff, so we stuff it into
an unrelated Mesa config file.

This should fix PTB on RPi OS 11 on RPi 4/400.

---
## [rorgoroth/mingw-cmake-env](https://github.com/rorgoroth/mingw-cmake-env)@[3a0af5e546...](https://github.com/rorgoroth/mingw-cmake-env/commit/3a0af5e546b15e3650abe9ea2b51755a0c47c5da)
#### Sunday 2022-08-07 19:22:58 by Ray Griffin

packages/update-repo.sh: tweak...

Firstly, fix the quoting.
Secondly, disable submodules; something fucky is going on here especially with libplacebo which makes every `ninja update` causes the stamp files to be deleted and package rebuilt despite no changes there for 4 days. So see how this goes, I don't think anything really uses submodules but if it does I'll have to set up a function in the build files to deal with those since this is kinda annoying.

CMake should take care of this anyway? The logs kinda point to that.
For reference: https://cmake.org/cmake/help/latest/policy/CMP0097.html#policy:CMP0097

---
## [mat-adamec/classwork](https://github.com/mat-adamec/classwork)@[cb08ab7551...](https://github.com/mat-adamec/classwork/commit/cb08ab7551751f3ca0b00ab8205584251bc422c8)
#### Sunday 2022-08-07 20:36:52 by Mat Adamec

Implements Huffman Coding to input text files

For example input (from Kafka's The Trial):

Before the law sits a gatekeeper. To this gatekeeper comes a man from the country who asks to gain entry into the law. But the gatekeeper says that he cannot grant him entry at the moment. The man thinks about it and then asks if he will be allowed to come in later on. It is possible, says the gatekeeper, but not now. At the moment the gate to the law stands open, as always, and the gatekeeper walks to the side, so the man bends over in order to see through the gate into the inside. When the gatekeeper notices that, he laughs and says: If it tempts you so much, try it in spite of my prohibition. But take note: I am powerful. And I am only the most lowly gatekeeper. But from room to room stand gatekeepers, each more powerful than the other. I cant endure even one glimpse of the third. The man from the country has not expected such difficulties: the law should always be accessible for everyone, he thinks, but as he now looks more closely at the gatekeeper in his fur coat, at his large pointed nose and his long, thin, black Tartars beard, he decides that it would be better to wait until he gets permission to go inside. The gatekeeper gives him a stool and allows him to sit down at the side in front of the gate. There he sits for days and years. He makes many attempts to be let in, and he wears the gatekeeper out with his requests. The gatekeeper often interrogates him briefly, questioning him about his homeland and many other things, but they are indifferent questions, the kind great men put, and at the end he always tells him once more that he cannot let him inside yet. The man, who has equipped himself with many things for his journey, spends everything, no matter how valuable, to win over the gatekeeper. The latter takes it all but, as he does so, says, I am taking this only so that you do not think you have failed to do anything. During the many years the man observes the gatekeeper almost continuously. He forgets the other gatekeepers, and this one seems to him the only obstacle for entry into the law. He curses the unlucky circumstance, in the first years thoughtlessly and out loud, later, as he grows old, he still mumbles to himself. He becomes childish and, since in the long years studying the gatekeeper he has come to know the fleas in his fur collar, he even asks the fleas to help him persuade the gatekeeper. Finally his eyesight grows weak, and he does not know whether things are really darker around him or whether his eyes are merely deceiving him. But he recognizes now in the darkness an illumination which breaks inextinguishably out of the gateway to the law. Now he no longer has much time to live. Before his death he gathers in his head all his experiences of the entire time up into one question which he has not yet put to the gatekeeper. He waves to him, since he can no longer lift up his stiffening body.The gatekeeper has to bend way down to him, for the great difference has changed things to the disadvantage of the man. What do you still want to know, then? asks the gatekeeper. You are insatiable. Everyone strives after the law, says the man, so how is that in these many years no one except me has requested entry? The gatekeeper sees that the man is already dying and, in order to reach his diminishing sense of hearing, he shouts at him, Here no one else can gain entry, since this entrance was assigned only to you. Im going now to close it.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[f0cef47678...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/f0cef47678384716080d4cc2adfa8be85b9ddc69)
#### Sunday 2022-08-07 21:44:05 by SkyratBot

[MIRROR] Adds the Mothroach [MDB IGNORE] (#15399)

* Adds the Mothroach (#68763)

About The Pull Request

Yup. That's pretty much it. This PR adds the Mothroach to the game, described as "An ancient ancestor of the moth that surprisingly looks like the crossbreed of a moth and a cockroach."

Do you love the Mothroach? Then you can cuddle with it and pat it, as well as place it on your head for extra cuteness.
What if you hate it, though? You can always kill and butcher Mothroaches in order to mass produce moth plushes for your own profit... How fun!

Either way, you win!

The Mothroach can be picked up and has a special on-head sprite (which looks really cute). It is able to vent-crawl and you may get one by randomly summoning a friendly mob through the gold slime extracts, or by ordering one through the Cargo Requests. After butchered, you may use its hide, a heart, and some cloth to craft a moth plushie, the most devilish of Devil's designs.

Full Preview of all the Sprites (NEW): https://www.youtube.com/watch?v=pdg8FTNEYjI
Preview of some of the Sprites (OLD): https://www.youtube.com/watch?v=9A-8hGCiW0s
In-hand, on-head, and grounded Mothroach sprite credits go to ValuedEmployee.
I did the Mothroach hide sprite though!
Why It's Good For The Game

The Mothroach is incredibly cute and a neat, fresh, new piece of content. Although it could use some future repurposing, right now it's simply a cute exotic pet with a few interactions.

These cute sprites are just too good to go to waste...

I keep seeing people complain about the lack of new content. Well, here's something niche that won't break the whole balance of the game and that will be cute. I seriously cannot see a motive not to add this to the game. Just because it isn't a powergaming tool or something that is seen every shift, that doesn't mean that it won't have a positive influence on the game. As I have stated, right now the Mothroaches are underperforming in terms of interactions and ways of getting them, but adding them is the first step to later improve them.
Changelog

cl
add: The Mothroach, your new local exotic pet
add: Mothroach Hide and Mothroach Meat
add: New crafting recipe for the Moth Plush: 1 Mothroach Hide; 1 heart; 3 cloth
fix: Fixes dead mobs on-head not having sprites
/cl

* Adds the Mothroach

Co-authored-by: Justice <42555530+Justice12354@users.noreply.github.com>

---
## [Brainulator9/s1disasm](https://github.com/Brainulator9/s1disasm)@[e5651cf7f3...](https://github.com/Brainulator9/s1disasm/commit/e5651cf7f3fd45934ba5e7926874de0c3bffcbde)
#### Sunday 2022-08-07 22:09:57 by Clownacy

Replace the Batch and Python scripts with Lua.

This was done to reduce duplication, as the Batch and Python build
scripts both do the same thing albeit in completely different ways,
making maintaining the build system a pain.

The two build scripts are for different platforms: Batch is for
Windows users while Python is for Linux and Mac users.

Since Python is cross-platform, you might be wondering why we can't
just make Windows users use the Python script. The reason is that
Windows users like being able to build the disassembly without
installing anything. We could bundle an entire Python runtime with
the disassembly so that it doesn't need installing separately, but
Python's runtime is massive and would hugely bloat the repo.

Lua, on the other hand, has a tiny runtime: the version in this
commit is only 500KB. This makes it more than light enough to bundle
with the disassembly for Windows users.

With a runtime bundled, it becomes feasible for Windows users to use
a Lua-based build script without installing anything. But, of course,
Windows users also hate using command line tools: they just want to
double-click on a file to build the disassembly. To address this, the
Batch build script has been kept, but hollowed-out and reduced to a
mere shim to run the Lua script. To the user, the process of building
the ROM won't have changed at all, and it is as intuitive as ever.

Likewise, to Linux and Mac users, the process should also be as
simple as it was before: like with the the Python script, the Lua
script expects Linux and Mac users to install a Lua runtime, rather
than depend on one being bundled with the disassembly.

The Lua script has been given an appropriate shebang, so that it can
be directly executed on Linux (and Mac?) much like how the Batch
script can be directly executed on Windows.

Because Lua is a powerful language, I've merged the functionality of
the `fixheader.exe` tool into the Lua build script, just like the
Python build script. This means that the Lua script computes the
checksum and patches the ROM header on its own, without using a
native executable as the Batch script did.

A Lua-based 'chkbitperfect' script has been provided as well,
replacing the previous two Batch scripts and the similar
functionality in the Python build script.

Fun fact: I couldn't find any fast Lua-based SHA256 or MD5 hashers,
so I converted my own C89 MD5 hasher to Lua, and it worked a treat!

My plan is to migrate the Sonic 2 and Sonic 3 & Knuckles
disassemblies to use a Lua build system as well. This would eliminate
the fragmentation caused by each disassembly having two build
systems, allowing for the build process of each disassembly to be
made more elaborate without the burden of maintaining two build
systems.

For instance, I'd like to get the Sonic 2 disassembly to use ASM
music, but to do this I'd need to add a step to the build process
where each song is assembled and compressed before the ROM itself is
built. While this idea is daunting when considering the fact that I'd
have to implement it *twice* - once for the Batch build system and
again for the Bash build system - it's not a problem at all when it's
just one build system. It helps that I'm a lot more familiar with Lua
than I am with Batch and Bash.

Oh, by the way, the build script now defaults to the accurate DAC
driver compression: users that want improved compression can just
edit the boolean at the start of the script.

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[c3c08d0946...](https://github.com/sojourn-13/sojourn-station/commit/c3c08d0946fd0ebde1dd9b5cc5ab8781a544487c)
#### Sunday 2022-08-07 22:43:11 by nikothedude

Ports moveSS from TG (#3771)

* p

* fucker

* fuckin

* fuckin!!!!

* commit time

* hell yeah

* FUCKING. TG

* groan

* fuvkin

---

