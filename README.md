## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-23](docs/good-messages/2023/2023-11-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,672,319 were push events containing 3,855,078 commit messages that amount to 252,254,252 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 81 messages:


## [cam900/mame](https://github.com/cam900/mame)@[96ab505d66...](https://github.com/cam900/mame/commit/96ab505d665a886809e8109a55d5e13fb7e520aa)
#### Thursday 2023-11-23 00:01:56 by ArcadeShadow

ibm5170_cdrom.xml: Added 21 items (18 working). (#11760)

New working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
5 Plus One: Pack 12 - Ghostbusters II [redump.org]
Brutal: Paws of Fury (Europe) [redump.org]
Darkseed (Germany, Action Sixteen release) [redump.org]
Dune (Europe, White Label release) [redump.org]
Dune II - Battle for Arrakis (Netherlands) [redump.org]
Dune II - Battle for Arrakis (Germany, PC Games Collection 2 release) [redump.org]
Dune II - The Building of a Dynasty (USA, Gold Medal 12 CD Pack) [redump.org]
Fables & Fiends - Book Three: Malcolm's Revenge (Europe, Japan) [redump.org]
Fables & Fiends - Book Two: The Hand of Fate (UK, Sold Out release) [redump.org]
Jurassic Park (Europe) [redump.org]
Jurassic Park (Germany) [redump.org]
Jurassic Park (USA) [redump.org]
Star Control [redump.org]
Stellar 7 (USA) [redump.org]
Stellar 7 (USA, alt) [redump.org]
The Cool Croc Twins + Magic Boy (Europe, 2 Game Pack release) [redump.org]
The Cool Croc Twins + Magic Boy (Netherlands) [redump.org]
The Dig (Japan) [redump.org]

New NOT working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
Darkseed (USA) [redump.org]
Darkseed (USA, alt) [redump.org]
Dogfight: 80 Years of Aerial Warfare (Europe) [redump.org]

---
## [kurtamohler/pytorch](https://github.com/kurtamohler/pytorch)@[5f504d1de7...](https://github.com/kurtamohler/pytorch/commit/5f504d1de74a5189f93e65aa9283fc4607b8631c)
#### Thursday 2023-11-23 00:14:16 by Pedro Caldeira

Check for boolean values as argument on pow function.  (#114133)

Hello everyone! 😄
Also @lezcano , nice to meet you! :)

Sorry if I miss anything, this is my first time around here. 🙃

This PR basically makes the same behaviour for cuda when using `torch.pow`. Basically Python considers True as 1 and False as 0. I just added this check into `pow` function. From what I understood, when I do `.equal` for `Scalar` that is boolean, I'm sure that types match so that won't cause more trouble.

I know that the issue suggest to disable this case but that could be a little more complicated, in my humble opinion. And that can create some compability problems too, I guess.

My argument is that code below is correct for native language, so I guess it does makes sense sending booleans as Scalar.

```
$ x = True
$ x + x
2
```

This was my first test:
```
Python 3.12.0 | packaged by Anaconda, Inc. | (main, Oct  2 2023, 17:29:18) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.pow(torch.tensor([1, 2], device='cuda'), True)
tensor([1, 2], device='cuda:0')
>>> torch.pow(torch.tensor([1, 2]), True)
tensor([1, 2])
>>> torch.pow(torch.tensor([1, 2]), False)
tensor([1, 1])
>>> torch.pow(torch.tensor([1, 2], device='cuda'), False)
tensor([1, 1], device='cuda:0')
```

I've run `test_torch.py` and got following results, so my guess is that I didn't break anything. I was just looking for a test that uses linear regression, as suggested.

```
Ran 1619 tests in 52.363s

OK (skipped=111)
[TORCH_VITAL] Dataloader.enabled		 True
[TORCH_VITAL] Dataloader.basic_unit_test		 TEST_VALUE_STRING
[TORCH_VITAL] CUDA.used		 true

```
(I can paste whole log, if necessary)

If this is a bad idea overall, dont worry about it. It's not a big deal, it's actually a two line change 😅  so can we talk of how do things in a different strategy.

For the record I've signed the agreement already. And I didn't run linter because it's not working 😞 . Looks like PyYaml 6.0 is broken and there's a 6.0.1 fix already but I have no idea how to update that 😅

Fixes #113198

Pull Request resolved: https://github.com/pytorch/pytorch/pull/114133
Approved by: https://github.com/lezcano

---
## [jemsgithub04/app-dev](https://github.com/jemsgithub04/app-dev)@[bb629c82ca...](https://github.com/jemsgithub04/app-dev/commit/bb629c82ca993ee78b462f687c1975eb38006624)
#### Thursday 2023-11-23 00:29:25 by jemsgithub04

Update README.md

-The Witcher-
The story begins with Geralt of Rivia, Crown Princess Cirilla of Cintra, and the quarter-elf sorceress Yennefer of Vengerberg at different points in time, exploring formative events that shape their characters throughout the first season, before eventually merging into a single timeline.

Geralt and Ciri are linked by destiny since before she was born when he unknowingly demanded her as a reward for his services by invoking "the Law of Surprise". After the two finally meet, Geralt becomes the princess's protector and must help her and fight against her various pursuers to prevent her Elder Blood and powerful magic from being used for malevolent purposes and keep Ciri and their world safe.

-The Boys-
The Boys is set in a universe where superpowered individuals (colloquially known as "supes") are recognized as heroes by the general public and work for a powerful corporation known as Vought International that markets and monetizes them. Outside their heroic personas, most supes are corrupt and self-serving. The series primarily focuses on two groups: the Boys, a team of vigilantes looking to bring down Vought and its corrupt superheroes, and the Seven, Vought's premier superhero team overseen by executive Madelyn Stillwell.

-Gen V-
At the Godolkin University School of Crimefighting, founded by Thomas Godolkin, young adult superheroes ("supes") put their moral boundaries to the test by competing for the university’s top ranking and a chance to join The Seven, Vought International's elite superhero team. When the school’s dark secrets come to light, they must decide what kind of heroes they want to become.

---
## [unicode-org/unicodetools](https://github.com/unicode-org/unicodetools)@[a68eedc9ec...](https://github.com/unicode-org/unicodetools/commit/a68eedc9ec900a785c0dbd6fe1dc06dfd783064c)
#### Thursday 2023-11-23 00:29:32 by Markus Scherer

UCA 16.0 delta 11

From Ken:

At this point there are only 4 more characters to deal with: the Garay and
Tulu-Tigalari gemination marks and the nasalization and lengthener marks
for Ol Onal. All four are gc=Mn and as discussed above should probably end
up with secondary weights.

Because the addition of script-specific secondary weights requires some
corresponding code changes to the sifter code, I have saved these four
to the last. I will provide the intercalation points for unidata.txt,
but then also spell out in detail what corresponding changes need to
be made to the source code to enable the extension of the list of defined
secondary weights. At that time I will also update the various dates
and version information in the sifter source code, so that allkeys.txt and
other output files get stamped with the correct versions and dates.

1. Ol Onal MU and IKIR (1E5EE..1E5EF).

Thinking about these overnight, there doesn't seem to be any strong
case for these requiring *script-specific* secondary weights. They
are the only combining marks used in Ol Onal. One is just a dot above
and the other is just a dot below (and only used on one letter).
Their collation implications can be handled simply be equating them
to the generic above and generic below secondary weights.

Intercalate 1E5EE and 1E5EF into unidata.txt in the combining marks
section after the 4 Nag Mundari combining marks, and weight them
as generic above and generic below.

Regenerate allkeys.txt and examine the diff against allkeys-16.0.0d10.txt.
(This can be done with a diff, because the two marks are being given
existing secondary weights.)

2. Garay and Tulu-Tigalari gemination marks (10D6A, 113D2)

These were discussed at some length above. For consistency with
similar cases in other scripts, a solution that gives them script-specific
secondary weights seems best. Both occur in scripts that have other
combining marks that these gemination marks should be distinguished from.

Introducing new secondary weights in the sifter is much less automatic
than just letting the sifter assign new primary weights. Because the
sifter's generation of allkeys.txt is still tightly coupled to the
generation of the symbolic forms used for the CTT table for ISO 14651,
the code needs to be touched to introduce new secondary weight symbols
in the correct order. (At some point soon, we might decide to give up
on generating the CTT table for ISO 14651, but that is a separate
decision that would require a significant overhaul of the code to clean
up the sifter, and shouldn't be considered now simply to avoid the
work for two new secondaries for 16.0.)

So first I detour to do the 16.0 updating of the sifter.

unisift.c

Update the two version strings and the versioned file names to 16.0.0.
The copyright year hasn't (yet) changed since this code was last touched
for 15.1.

For consistency in documentation, update the NOTDEF section of the
switch statement in unisift_ForceToSecondary() for the three Tulu-Tigalari
and one Gurung Khema mark that were equated to generic anusvara,
visarga, etc. This doesn't impact the actual code, but is good practice
for bookkeeping on these exceptions.

unisyms.c

Bump up the NUMSECONDSYMS constant from 261 to 263 for the two new weights
to be added.

There are no strong rules for which order new secondaries need to be
intercalated in, and no obvious positions, since Tulu-Tigalari and
Garay are both new. To keep things simple, I chose to add both of them
together, right after the existing entry for the Soyombo gemination mark
in secondSyms[]:

"<D11A98>", /* Soyombo gemination mark */
"<D10D6A>", /* Garay gemination mark */
"<D113D2>", /* Tulu-Tigalari gemination mark */

That requires a corresponding addition of two entries to secondSymVals[]:

/* Soyombo, Garay, Tulu-Tigalari */
    0x11A98, 0x10D6A, 0x113D2,

And then, the actual two entries for 10D6A and 113D2 need to be moved
into unidata.txt in the same relative position, right after 11A98.

I also made two small tweaks to ranges in dumpCollatingSymbols() to ensure
that those ranges pick up the new Gurung Khema and Symbols for Legacy
Computing Supplement blocks when dumping collating symbols for the CTT
for 14651. Corresponding tweaks needed to be made to the ranges
in unisift_BuildSymWtTree().

This manual insertion of secondary marks is, of course, very tedious
and error-prone in cases where several new marks need to be added
for a version. It would be helpful if it could be automated a
bit more, but the work involved has never risen to the level where
it could offset the considerable effort that would be required to
figure out and implement actual automation here. The whole issue
of secondary weights in DUCET has seen an extensive amount of
custom tinkering over the years, in large part to keep the
inflation of secondary values under control, and to avoid breaking
out of the magic number range: 0021..01FF for secondaries, so
the DUCET table could keep the lowest primary weight stable
at 0200. We would have broken the bank years ago, if not for
the considerable work in custom folding of lots of secondary
weights for marks in different scripts into common, generic
secondary weight values.

Rebuild the sifter and deploy.

Regenerate allkeys.txt and verify that the two new secondary
weights have been added correctly, and that the secondary weight
range shows in the output diagnostics as having been bumped
up to 263. My first run for this in fact turned up an underlying
problem in my library when I checked for the magic number 263
and came up one short in the output. I had mistakenly given
an Alphabetic value to 10D6A, which resulted in the sifter giving
it a primary weight, instead of the desired secondary weight
next to the other two gemination marks. Correction of the
library resulted in the expected output in allkeys.txt:

11A98 ; [.0000.00D2.0002] # SOYOMBO GEMINATION MARK
10D6A ; [.0000.00D3.0002] # GARAY CONSONANT GEMINATION MARK
113D2 ; [.0000.00D4.0002] # TULU-TIGALARI GEMINATION MARK

For these secondary weight changes, another necessary check
is to verify that the CTT generation picked up the correct
new symbols. For that I check the ctt14651.txt output file:

collating-symbol <D11A98>  % SOYOMBO GEMINATION MARK
collating-symbol <D10D6A>  % GARAY CONSONANT GEMINATION MARK
collating-symbol <D113D2>  % TULU-TIGALARI GEMINATION MARK
...
<D11A98>  % SOYOMBO GEMINATION MARK
<D10D6A>  % GARAY CONSONANT GEMINATION MARK
<D113D2>  % TULU-TIGALARI GEMINATION MARK
...
<U11A98> IGNORE;<D11A98>;<MIN>;<SFFFF> % SOYOMBO GEMINATION MARK
<U10D6A> IGNORE;<D10D6A>;<MIN>;<SFFFF> % GARAY CONSONANT GEMINATION MARK
<U113D2> IGNORE;<D113D2>;<MIN>;<SFFFF> % TULU-TIGALARI GEMINATION MARK

And everything seems to be in order there. If the tables in unisyms.c
are not correctly updated, these symbol assignments for the CTT can easily end
up with off-by-one errors, throwing the table completely out of
whack.

4 more down, 0 to go. Yay!

Archive this delta 11:

unidata-16.0.0d11.txt (1603293 bytes, 10/09/2023)

Generate decomps-16.0.0d11.txt (sifter -t unidata-16.0.0d11.txt) to
document the changes in decompositions for this version of UCA.
I diff this file against the released version for 15.1.0: decomps-15.1.0d4.txt
to see what changed. It shows all the new decompositions, including all
the synthetic decomposition additions for collation. It also shows
the order change for the two secondary decompositions for Kannada
and Sinhala, discussed above.

----

From Ken via email:

As usual, there are also some small modifications to the sifter source code,
particularly to deal with the introduction of new secondary weights for UCA 16.0.
I was able to pare away various secondaries and get the additions down to just
two new secondary weights --
but any addition of a secondary requires some work on the sifter code.
And there are always version and a few range updates required for a new version, as well.

Note that handling the full new set (1177 characters) for Unicode 16.0
in the sifter requires that some character properties outside of UnicodeData.txt
also be updated correctly.
The most important of these is Alphabetic, which depends on Other_Alphabetic in PropList.txt.
To a lesser extent, the values for Diacritic and Extender (also in PropList.txt)
might impact a few weight assignments.
I very strongly recommend that before going much further on script-by-script UCA work,
particularly for the abugidas,
that you first take a break to do a complete update of PropList.txt for 16.0.
Neglecting that step will just lead to confusion and
characters out of place later on in the UCA work,
particularly when you get to Tulu-Tigalari.

---
## [unicode-org/unicodetools](https://github.com/unicode-org/unicodetools)@[5eaa3a86a6...](https://github.com/unicode-org/unicodetools/commit/5eaa3a86a6c110c092ccb0ab5713cfefd2dc433f)
#### Thursday 2023-11-23 00:29:32 by Markus Scherer

UCA 16.0 delta 7

From Ken:

1. Todhri

Given all the complications of Kirat Rai to start off the day, I'm rewarding
myself before lunch by dealing with an easy case: Todhri. This is just a straight
unicameral alphabet, with no complications other than two letters that have
canonical equivalent sequences.

Move the relevant entries for Todhri (105C0..105F3), in code point order, into
unidata.txt, right after Vithkuqi. Apply the CONTRACTION pragma to the
two decomposed vowels, 105C9 and 105E4.

Generate allkeys.txt and verify that Todhri weights are as expected,
including the two contractions.

2. Sunuwar

This is another simple one, another simple unicameral alphabet with no marks,
and with the desired collation order the same as the code point order.

Move the relevant entries for Sunuwar (10BC0..11BE0), in code point order, into
unidata.txt, right after Tangsa (and ahead of the Kirat Rai I just added).
Leave the one punctuation sign to deal with later.

Generate allkeys.txt and verify that Sunuwar weights are as expected.

3. Gurung Khema

Gurung Khema is a bit more complicated. This one is an abugida, and it
has decomposition and contraction issues for the vowel signs.

First move all the relevant entries for Gurung Khema (16100..1612F),
in code point order, into unidata.txt, right after Sunuwar.

The 8 multi-part vowels with decompositions, 16121..16128, need to have
the CONTRACTION pragma, as the intent is for the vowels to all get
primary weights. 3 of the multi-part vowels, 16126..16128, have full
decompositions into sequences of three parts. Because of this, as for
Kirat Rai discussed above, those three need to have the full decompositions
added in their entries as secondary decompositions. The entries
affected are:

16126;GURUNG KHEMA VOWEL SIGN O;Mn;16121 1611F, 1611E 1611E 1611F;;;;;
16127;GURUNG KHEMA VOWEL SIGN OO;Mn;16122 1611F, 1611E 16129 1611F;;;;;
16128;GURUNG KHEMA VOWEL SIGN AU;Mn;16121 16120, 1611E 1611E 16120;;;;;

A replication note for when trying to build allkeys.txt with sifter in
the unicodetools: Before the sifter will work correctly for weighting of
abugidas, the Alphabetic property has to be updated for the repertoire in
question. In particular, all gc=Mn or gc=Mc vowel signs, consonant signs,
and length marks in abugidas need to be set explicitly to Other_Alphabetic
in PropList.txt first (and the relevant derivations be run based on that).
Otherwise, during the sift process, the sifter won't see these as
alphabetic and branch down the path for primary weights, but rather will
identify them as otherwise unaccounted for combining marks, and attempt
to give them secondary weights. Anusvaras and visargas also should be
set to Other_Alphabetic, but those are already bled off in unidata.txt by being
given explicit decompositions to generic marks.

Another piece of the puzzle is that nuktas and viramas (including killers)
should be given the Diacritic property in PropList.txt, but these are
more marginal for sifter behavior. Most nuktas are now bled off with
explicit decompositions, and the viramas are almost all picked up in
the sifter via their ccc=9 values. This could become a problem in the
future if SAH insists on ccc=0 for some newly encoded viramas, at which
point the sifter code may need an update to catch any combining
mark viramas (or conjoiners and killers) with ccc=0. The example we have for
16.0, in Kirat Rai, is not a problem, because that is gc=Lm, ccc=0,
so the sifter gets its Alphabetic status from gc=Lm and assigns it a
primary weight.

Generate allkeys.txt and verify that Gurung Khema weights are as expected,
with special attention to the vowel contractions.

4. Tulu-Tigalari

First move all the relevant entries for Tulu-Tigalari (11380..113D0),
in code point order, into unidata.txt, right after Grantha.

Put in the CONTRACTION pragma for the 3 two-part dependent vowel signs,
113C5, 113C7, 113C8. Do the same for each of the 4 two-part independent
vowel signs, 11383, 11385, 1138E, 11391.
Those aren't contiguous in code point order, so should use
multiple entries for the pragma, to make sure they don't pick up entries
that they shouldn't.

Now, checking against the detailed specification of the collation order
in the proposal (L2/22-031), invert the order of 113B3 LLA and 113B4 RRA,
so the collation order is RRA < LLA. That seems to be a deliberate choice
in the proposal.

Next move 113D1 TULU-TIGALARI REPHA into unidata.txt, immediately after
the RA (113AC). The repha is a separately encoded form of ra.

Note that for the Tulu-Tigalari vowels, there are deliberate encoding
gaps for short e and short o. Those might be added to the encoding later
on, in which case they would intercalate neatly in the gaps, and would
fit in the same places in the primary collation order. There is one
anomaly in the specification of collation in that it specifies the
primary order for vowel sign o, even though that is not encoded.
There is also a typo indicating: vowel sign vocalic ll << vowel sign ee.
That should be a primary distinction, like all the rest. Ignored.

The au length mark (113C8) only occurs as the second part of some
two-part vowels, and is basically would not be weighted alone
in most text, because it is basically bled by contractions that
form the weights for atomically encoded two-part vowels.
It makes more sense to give it a primary order
*after* the viramas, so I have reversed the position in unidata.txt,
as compared to the specification in the proposal. See the treatment
for Grantha, which has similar components.

The pluta (113D3) is not in L2/22-031. It was added later, based on
Srinidhi and Sridatta's L2/22-260.
L2/22-260 is silent about its ordering. It is a letter that serves
as a different kind of vowel lengthener. I'm giving it a primary order
after the au length mark. Again, see the comparable treatment of
the same component in Grantha.

The gemination mark (113D2) is also not in L2/22-031, but comes from
L2/22-260, which is silent about its ordering. However, the comparison
is made there to Gurmukhi addak (0A71), Khojki sign shadda (11237), and Soyombo
gemination mark (11A98). For DUCET, 0A71 is given a Gurmukhi-specific
secondary weight. The Khojki shadda is simply equated to the Arabic shadda.
The Soyombo gemination mark is given a Soyombo-specific secondary weight.
On balance, it seems best to just add a new secondary weight for the
Tulu-Tigalari gemination mark. I defer that to later, along with any
other new secondary weight additions required. Remember that Garay is
also introducing a gc=Mn gemination mark, so I have to figure out how to
deal with that one, too. So later.

Regenerate allkeys.txt, and verify that the Tulu-Tigalari weights
are as expected, with special attention to the various vowel contractions
and to the few other characters that receive primary weight not in
code point order, as noted above.

5. Ol Onal

Ol Onal is another easy one. It is a simple alphabet. The proposal (L2/22-151R)
specifies that the collation order is simply the same as the encoding order,
however, the discussion of the use of the two combining marks, MU (nasalization,
a dot above) and IKIR (lengthening, a dot below) suggests to me that it makes
more sense to give them secondary weights. That is, rather than what is
specified in the proposal:

A < A+MU < A+IKIR < A+IKIR+MU = A+MU+IKIR

what probably makes more sense for ordering is:

A << A+MU << A+IKIR << A+IKIR+MU = A+MU+IKIR

which would be accomplished better with secondary weights for MU and IKIR.

The proposal compares these two marks to the corresponding marks in Ol Chiki,
which are spacing and given gc=Lm, and the corresponding marks in Nag Mundari,
which are non-spacing diacritics. For best consistency, I think we should
follow the pattern of Nag Mundari, which gives the two non-spacing marks
secondary weights, rather than the Ol Chiki pattern, where the spacing
modifier letters get primary weights.

In any case, since the preferred solution involves assigning new secondary
weights, I defer the MU and IKIR to a later draft when I deal with those.

So for now, for the rest of the alphabet, I move all the letters (1E5D0..1E5ED)
and the HODDOND (1E5F0), in code point order, into unidata.txt right after Ol Chiki.

Regenerate allkeys.txt, and verify that the Ol Onal weights are
as expected.

I'll save Garay for the next delta.

233 more down, 771 to go.

Archive this delta 7:

unidata-16.0.0d7.txt (1569698 bytes, 10/08/2023)

---
## [Luftkommando/Shiptest](https://github.com/Luftkommando/Shiptest)@[2a74c23d62...](https://github.com/Luftkommando/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Thursday 2023-11-23 00:31:03 by Imaginos16

Nerfs the everloving almighty shit out of the jungle demonic office ruin (#2430)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Nerfs the ruin by removing most of its gamer gear, and changing the
syndicate hardsuit you find into a scarlet hardsuit.


Not to mention the two goddamn deathsquad hardsuits all there,
wholesale, for free.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a8333190-37ce-441f-a746-bb5f2fc26828)

This shit is not okay jesus fucking christ, two deathsquad hardsuits?
Are you insane?
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
balance: The Jungle Demonic Office Ruin has now been appropriately
balanced, now only having a scarlet hardsuit, decent syndicate armor,
and a bulldog with no spare mags.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Luftkommando/Shiptest](https://github.com/Luftkommando/Shiptest)@[bf4671ff83...](https://github.com/Luftkommando/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Thursday 2023-11-23 00:31:03 by retlaw34

Gun rework (#1601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
WIP.

if it wasn't obvious, very based off tgmc 

this reworks how guns work, by making them 4x more lethal without
touching a single damage value

its a bit difficult to put into words what this does, so i think these 3
gunfights i did with a good friend explains it better than i ever could

https://streamable.com/09in19
https://streamable.com/yel56o
https://streamable.com/x2a0he

if you didnt watch these videos:
- New guns sounds, TGMC as usual. but some racking sounds are from CEV
eris
- guns now can be wielded, if unwielded, they may cause recoil which not
only makes your shots less accurate, but 'scrolls' your screen
- new suppression effects
- getting hit hard enough scrolls your screen
- anything getting hit shakes you as feedback, not just bullets
- bullets can ricochet naturally upon hitting a surface at a step angle.
does not auto aim at your target, so be careful. ricochet sfx taken from
CEV eris
- new effects for bullet impacts. sound effects were taken from TGMC and
https://github.com/Skyrat-SS13/Skyrat-tg/pull/11697
- adds the cattleman revolver and Himehabu 22lr pistol. sprites by yours
truely

big problem is, in order for all of this to work, a certain key needs to
be binded to rack the gun. by default this is SPACE, but moost already
have it binded to 'hold throw mode', which is an issue. for one, not
only you need to ask everyone to rebind their controls to a very
important key, but also a key dedicated to just racking the gun can
cause issues. im up for any solutions

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game

people dont fear gunfights. they think its just a way to pvp. people
should be afraid of gunfights, feel the pain OOCly when their blorbo
gets hit

## Changelog

:cl:
add: 22lr and cattleman revolver
add: many gun sounds
balance: guns reworked
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: retlaw34 <bruhasdfasdfasdf@waifu.club>

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[b3f97b0115...](https://github.com/unit0016/effigy-se/commit/b3f97b01152fa1427b848f0ca3b03ea6bd5b014d)
#### Thursday 2023-11-23 00:47:22 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[3f7a9d4563...](https://github.com/TaleStation/TaleStation/commit/3f7a9d45637afe0e30abfe9481051aa12a0dd0ea)
#### Thursday 2023-11-23 00:59:50 by TaleStationBot

[MIRROR] [MDB IGNORE] fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#8668)

Original PR: https://github.com/tgstation/tgstation/pull/79783
-----
This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---------

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[800ad77ed2...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/800ad77ed29fd7c68ddc0cac3112f45e1e1c3015)
#### Thursday 2023-11-23 01:02:10 by DBGit42

Adds Affection Aversion quirk (#25194)

* Adds Affection Aversion quirk

Stops affection modules. Very simple.

* I hate you, github

May or may not do anything. Stop giving me a merge conflict. Stop it.

* Revert "I hate you, github"

This reverts commit 6515023cc3f72d97d90bbdf982857b1d2724b1cf.

* Attempts to revert traits.dm

Because something went TERRIBLY wrong with my fork and/or my editor and I'm not sure why.

* Added quirk proper now that my fork is unfucked

Why did this even happen?

* These lists are alphabetized

* Same here

---------

Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [KeRSedChaplain/Bubberstation](https://github.com/KeRSedChaplain/Bubberstation)@[c034314f1b...](https://github.com/KeRSedChaplain/Bubberstation/commit/c034314f1b41c2f9ad1e66d939b95f49a0d2f36e)
#### Thursday 2023-11-23 01:05:29 by SkyratBot

[MIRROR] Basic skeletons [MDB IGNORE] (#24545)

* Basic skeletons (#79206)

## About The Pull Request

Turns skeletons (the simple animal version) into basic mobs. This was
another incredibly simple conversion, since skeletons don't really do
anything but walk at you and beat you to death.

Because I thought it was funny, though, skeletons will now seek out
cartons of milk and drink them. Real milk will heal them for a
significant amount, but soymilk, being false milk, will deal them
grievous injury instead! Skeletons beware... I didn't add any other
sorts of milk due to limited ability with existing AI behaviors to
identify milk containers (they actually only look for the carton items).

Other than that, I've done some flavor adjustment for skeletons' attacks
- their effects and sounds will now suit the weapon they're actually
holding - for example, skeleton templars now actually use their swords
instead of slashing you with their horrible fingers. Along with this I
gave the basic skeletons a normal slashing sound, instead of the weird,
impactless hallucination sound they used to use for some reason. I never
liked that sound.

Finally, I've reflavored the spear-wielding skeleton mobs to "undead
settlers", following the naming of the corpses dropped by snow legions
as of #76898, rather than being named after an offensive term for Inuit
people. These skeletons do, after all, appear in settlements on alien
worlds.

To enable the flavor of milk drinking, I expanded the `basic_eating`
component to allow drinking rather than eating flavor, with a different
sound and its own set of verbs. This deletes whatever they drink from,
but c'est la vie.
## Why It's Good For The Game

Ticks 6 more entries off the simple animal freeze. While skeletons are
still extremely simple, being largely-identical mobs that only exist to
beat you to death, being basic mobs should make them slightly better at
this job. Also, again, I think it's really funny that you can distract
skeleton mobs with milk, or even hurt them.
## Changelog
:cl:
refactor: Hostile skeleton NPCs now use the basic mob framework. They're
a little smarter, and they also have a slightly improved set of attack
effects and sounds. They love to drink milk, but will be harmed greatly
if any heartless spaceman tricks them into drinking soymilk instead.
Please report any bugs.
/:cl:

* Basic skeletons

* updatepaths

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [KeRSedChaplain/Bubberstation](https://github.com/KeRSedChaplain/Bubberstation)@[0e3b7d842b...](https://github.com/KeRSedChaplain/Bubberstation/commit/0e3b7d842b40525754a931903dded315f5a0270e)
#### Thursday 2023-11-23 01:05:29 by SkyratBot

[MIRROR] Adds a Syndicate Monkey Agent beacon uplink item [MDB IGNORE] (#24550)

* Adds a Syndicate Monkey Agent beacon uplink item (#79012)

## About The Pull Request

Adds a Syndicate Monkey Agent beacon uplink item. It spawns a dapper
monkey that must follow your orders.

Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

Added a more modularlike subtype for antagonist spawners to reduce
future hardcoding.

Gave the syndicate turtleneck a monkey sprite, from SS14!

## Why It's Good For The Game

I want to see the clown driving security insane with 2-3 monkeys and an
incredible amount of pranking. Or an assistant killing everyone with his
monkey friends while wearing a monkey suit. Or a geneticist sending out
mutated monkeys to kill people. Or a scientist equipping his monkeys
with bombs or xenobiology equipment and sending them out to wreak havoc.

6 TC is only enough for two monkeys, but you can get a third if you
finish any kind of objective.

> Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

We can't have the monkey mafia without guns, come on. The guns are weak
and only usable by monkeys. Additionally, they're restricted to
entertainment only.

Credit to SS14 for the monky turtleneck sprite.

## Changelog

:cl:
add: Adds a Syndicate Monkey Agent beacon uplink item. It spawns a
dapper monkey that must follow your orders.
add: Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.
refactor: Added a more modularlike subtype for antagonist spawners to
reduce future hardcoding.
sprite: Gave the syndicate turtleneck a monkey sprite, from SS14!
/:cl:

---------

Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Adds a Syndicate Monkey Agent beacon uplink item

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[6cba827dd3...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/6cba827dd3489b719152aef1175525e95debeb03)
#### Thursday 2023-11-23 01:06:39 by necromanceranne

[READY] The Tackleling: Unarmed bonuses and features contribute to tackle success and failure, significant outcome overhaul, among other things (#79721)

## About The Pull Request

### Tackling Outcomes

Tackling now determines success based on outcome categories. These are
derived from the typical attacker/defender roll that would have
previously determined the outcome on its own. A negative roll results in
a negative outcome, a positive roll a positive outcome, and a result of
exactly 0 resulting in a neutral outcome.

The result of your roll are then passed along to the relevant proc to
determine severity. The derived roll is multiplied by 10 (or -10 for the
negative roll to get a positive value to roll with). Then we see if our
final roll fits a severity bracket. Negative outcomes will roll to
determine their outcome, and potentially could roll a less severe
outcome than what our first roll would suggest.

For positive outcomes, the defender's melee armor reduces the severity
of the outcome.
For negative outcomes, the attacker's melee armor improves the potential
outcome and at least prevents more severe backlash. It'll still be
negative, you can't move from a negative outcome to a positive outcome
just from good armor.

Most of the outcomes are fairly similar to the current outcomes, but
with the inclusion of staggering one or both parties to make the
subsequent potential grabs _stickier_, if that makes sense.

Neutral is now a mutual stagger, but also the tackler being left
upright. It's effectively net zero.

### Blocking

Blocking is checked on impact, and results in a neutral outcome if the
defender successfully blocks. This means our tackler isn't too severely
impacted from an unsuccessful tackle

### Additional Changes

Your arms ``unarmed_effectiveness`` now contributes to the attack mod
and defense mod of tackles. For humans tackling humans, this often
results in a net neutral result. But if you have a better arm, or the
tackle target has worse arms, this can alter the outcome significantly.

Any tackler with the trait TRAIT_NOGUNS (like bezerkers, Sleeping Carp
users or the very unlikely chance ninjas are tackling while wearing
their armor) gains a bonus to their tackles.

Any suit that prevents shove knockdowns grants an attack bonus, and not
just riot armor. This now includes Mk.1 Swat suits, the ones from the
SWAT crate in cargo.

Settlers are vulnerable to tackles, much like their dwarf cousins.
They're also just as bad at tackles.

Security lockers come with gripper gloves, and the sec vendor has 5 sets
of gripper gloves as standard items. They also have a +1 skill bonus.
This should encourage people to use tackling a bit more without having
to always seek out the best gear to accomplish the task. (particularly
since security is inherently pretty good at tackling with the outcome
changes).

The HoS gets a pair of gorilla gloves in his garment bag. If he wants
them.

The shove slowdown is now a new status effect, Staggered. This is just
better functionality overall. Any instance of adding the shove slowdown
now makes our target staggered.

## Why It's Good For The Game

Tackling is a bit outdated, to say the least. Not much content has been
added for a while that isn't strictly meme content. With these changes,
tackling should be slightly more nuanced, considering elements such as
unarmed effectiveness, the presence of martial arts, and actually
properly checking block rather than notionally checking block. There is
also more opportunity to protect yourself from tackle outcomes, both
positive and negative.

It also should be a little fairer to be on the receiving end of tackles
if you have taken the time to layer up defenses against it. Attackers
often overwhelmed defenders due to numbers favoring attackers more than
defenders.

Closes some really outdated design that was resulting in some really
bizarre behaviour with regards to layered defenses against attack not
having the same meaning against tackles, if only because it was looking
for the wrong things and not even the correct parts of what it was
looking for. Namely, blocking and shielding.

The inclusion of more gripper gloves and a good outcome from using them
will hopefully incentivize people to consider tacking as a useful tool,
if a bit risky still due to the splat mechanics.

## Changelog
:cl:
balance: Judo Joe, archnemesis of Maint Khan, has begun re-airing his
midnight infomercials shilling his extremely expensive Tackle Supreme
Judo Karate Training video tapes. Unable to pass up a 'bargain',
Nanotrasen has purchased these tapes en masse. Tackling techniques have
started to improve, as well as Nanotrasen's tackling instructional
algorithms within tackle gloves.
balance: The outcomes for tackling are more equalized. It isn't as feast
or famine, and should be somewhat more controllable without becoming too
severe.
add: Blocking successfully against a tackle will force the tackle to be
a neutral outcome.
add: Unarmed effectiveness from arms now contributes to attacking with
and defending from tackles.
add: Those who refuse to use firearms (like Sleeping Carp users and
insane unholy berzerkers) are better at tackling others.
add: Riot specialized armor, and not just riot armor, now contributes
meaningfully to tackling effectiveness.
balance: MK.1 Swat Suits, the ones that come in SWAT crates, now
functions similarly to riot armor.
add: Settlers from the outer rims have noticed they aren't very good at
protecting themselves against Judo Joe's clearly discriminatory tackling
techniques.
add: Security lockers come with gripper gloves, security vendors now
sell them as standard items, and the HoS' garment bag now has a pair of
gorilla gloves. Gripper gloves have a positive skill bonus to tackling.
add: Being insane also makes you INSANELY good at tackling but also
INSANELY likely to eat shit on a whiff. DO OR DIE, BITCH.
refactor: Shoving slowdown and all its implementations now use a status
effect, Staggered.
/:cl:

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[4d4aa72e33...](https://github.com/Latentish/Shiptest/commit/4d4aa72e33bd20077d09d320f07a0a5608298cb2)
#### Thursday 2023-11-23 01:07:15 by lizardqueenlexi

Removes "fat" status and everything related. (#2516)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

As the title says, eating too much no longer makes you "fat". You suffer
no slowdown or mood debuff from eating too much, and in general, the
game will not take every opportunity to make fun of you.

Notable removals/changes:
- The "fat sucker" machine is totally gone.
- Shady Slim's cigarettes have been removed (since they only existed to
interact with this mechanic).
- Lipoplasty surgery is gone.
- The nutrition setting of scanner gates is gone.

There are a couple of other removals too, like Gluttony's Wall, that I
think were already not in use on this codebase.

One thing I'm not completely satisfied with was the change to mint
toxin, which now does quite literally nothing. I don't think this is
especially a problem, it just makes its existence a bit vestigial.

Also includes an UpdatePaths script to delete all removed objects, just
in case.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/105025397/a1dd0981-94fc-4766-a34d-cce31a42b412)

Basically, removes some shitty "jokes" about fat people. It's an
extremely mean-spirited feature that serves no actual purpose, and
punishes you for clicking on a burger one time too many. It could
potentially be replaced later with a less mean-spirited "overeating"
mechanic, but I'm dubious as to whether that would be any fun either.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the "fat" status - overeating now has no negative effects.
del: Removed lipoplasty surgery.
del: Removed the fat sucker machine.
tweak: Scanner gates no longer have a "nutrition" option available.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [mackmln/app-dev](https://github.com/mackmln/app-dev)@[a0a8365d11...](https://github.com/mackmln/app-dev/commit/a0a8365d111181d36146fb19c889a1dce461384d)
#### Thursday 2023-11-23 01:12:10 by mackmln

Update README.md

In 1985, teenager Marty McFly lives in Hill Valley, California, with his depressed alcoholic mother, Lorraine; his older siblings, who are professional and social failures; and his meek father, George, who is bullied by his supervisor, Biff Tannen. After Marty's band fails a music audition, he confides in his girlfriend, Jennifer Parker, that he fears becoming like his parents despite his ambitions.

---
## [FitzRoxas/App---Dev](https://github.com/FitzRoxas/App---Dev)@[919d37e301...](https://github.com/FitzRoxas/App---Dev/commit/919d37e301e2af0380d90444bf8607315e94c22e)
#### Thursday 2023-11-23 01:18:59 by FitzRoxas

Update README.md

The Notebook- In 1940s South Carolina, mill worker Noah Calhoun (Ryan Gosling) and rich girl Allie (Rachel McAdams) are desperately in love. But her parents don't approve. When Noah goes off to serve in World War II, it seems to mark the end of their love affair. In the interim, Allie becomes involved with another man (James Marsden). But when Noah returns to their small town years later, on the cusp of Allie's marriage, it soon becomes clear that their romance is anything but over.

The Great Gatsby - Midwest native Nick Carraway (Tobey Maguire) arrives in 1922 New York in search of the American dream. Nick, a would-be writer, moves in next-door to millionaire Jay Gatsby (Leonardo DiCaprio) and across the bay from his cousin Daisy (Carey Mulligan) and her philandering husband, Tom (Joel Edgerton). Thus, Nick becomes drawn into the captivating world of the wealthy and -- as he bears witness to their illusions and deceits -- pens a tale of impossible love, dreams, and tragedy.

---
## [Elpabarog/app-dev](https://github.com/Elpabarog/app-dev)@[f664598313...](https://github.com/Elpabarog/app-dev/commit/f664598313ab3e83983ab87e97ff4c087b87a31b)
#### Thursday 2023-11-23 01:19:48 by Elpabarog

Update README.md

# Titanic

- James Cameron's "Titanic" is an epic, action-packed romance 
  set against the ill-fated maiden voyage of the R.M.S. Titanic; the 
  pride and joy of the White Star Line and, at the time, the largest 
  moving object ever built. She was the most luxurious liner of her 
  era -- the "ship of dreams" -- which ultimately carried over 
  1,500 people to their death in the ice cold waters of the North 
  Atlantic in the early hours of April 15, 1912.


# The Karate Kid

- When his mother's career results in a move to China, 12-year- 
   old Dre Parker (Jaden Smith) finds that he is a stranger in a 
   strange land. Though he knows a little karate, his fighting skills 
   are no match for Cheng, the school bully. Dre finds a friend in 
   Mr. Han (Jackie Chan), a maintenance man who is also a 
   martial-arts master. Mr. Han teaches Dre all about kung fu in 
   the hope that Dre will be able to face down Cheng and perhaps 
   win the heart of a pretty classmate named Mei Ying.


# The Notebook

- In 1940s South Carolina, mill worker Noah Calhoun (Ryan 
  Gosling) and rich girl Allie (Rachel McAdams) are desperately in 
  love. But her parents don't approve. When Noah goes off to 
  serve in World War II, it seems to mark the end of their love  
  affair. In the interim, Allie becomes involved with another man 
  (James Marsden). But when Noah returns to their small town 
  years later, on the cusp of Allie's marriage, it soon becomes 
  clear that their romance is anything but over.

---
## [Elpabarog/app-dev](https://github.com/Elpabarog/app-dev)@[c578fa1157...](https://github.com/Elpabarog/app-dev/commit/c578fa11571860c9b2071dad0187159f6ee0ac08)
#### Thursday 2023-11-23 01:26:40 by Elpabarog

Update README.md

# Titanic

- James Cameron's "Titanic" is an epic, action-packed romance 
  set against the ill-fated maiden voyage of the R.M.S. Titanic; the 
  pride and joy of the White Star Line and, at the time, the largest  
  moving object ever built. She was the most luxurious liner of her 
  era -- the "ship of dreams" -- which ultimately carried over 
  1,500 people to their death in the ice cold waters of the North 
  Atlantic in the early hours of April 15, 1912.



## The Karate Kid

- When his mother's career results in a move to China, 12-year- 
   old Dre Parker (Jaden Smith) finds that he is a stranger in a 
   strange land. Though he knows a little karate, his fighting skills 
   are no match for Cheng, the school bully. Dre finds a friend in  
   Mr. Han (Jackie Chan), a maintenance man who is also a 
   martial-arts master. Mr. Han teaches Dre all about kung fu in 
   the hope that Dre will be able to face down Cheng and perhaps 
   win the heart of a pretty classmate named Mei Ying.



### The Notebook

- In 1940s South Carolina, mill worker Noah Calhoun (Ryan 
  Gosling) and rich girl Allie (Rachel McAdams) are desperately in 
  love. But her parents don't approve. When Noah goes off to 
  serve in World War II, it seems to mark the end of their love 
  affair. In the interim, Allie becomes involved with another man 
  (James Marsden). But when Noah returns to their small town 
  years later, on the cusp of Allie's marriage, it soon becomes 
  clear that their romance is anything but over.

---
## [YhuCaCla/app-dev](https://github.com/YhuCaCla/app-dev)@[a90255455e...](https://github.com/YhuCaCla/app-dev/commit/a90255455e4bf15386d83a157c1b7ee9f68f9b37)
#### Thursday 2023-11-23 01:27:08 by YhuCaCla

Update README.md

'Avatar'
Sixteen years after the Na'vi repelled the RDA invasion of Pandora, Jake Sully, chief of the Omatikaya clan, raises a family with Neytiri, including sons Neteyam and Lo'ak, daughter Tuk, and adopted daughter Kiri. Spider, the Pandora-born human son of Colonel Miles Quaritch, visits their children while being raised by scientists who stayed on Pandora. To the Na'vi's dismay, the RDA returns to colonize Pandora, led by Frances Ardmore. Quaritch's Recombinant serves as their leader.

Jake leads a guerilla campaign against the RDA, capturing Jake's children during a counterinsurgency mission. After spending time with Spider, Quaritch learns about Na'vi culture and language. The family retreats to Pandora's eastern sea, where they learn the ways of the reef people, develop a spiritual bond with the sea, and befriend Tsireya, daughter of Chief Tonowari and his wife Ronal.

'A time called You'
A Time Called You is a story about Jun-hee, who is still grieving the loss of her boyfriend Yeon-jun in the year 2023, a year after his passing. She somehow travels back in time to 1998 and wakes up inhabiting the body of a different person, 18-year-old Min-ju. As she navigates this new reality, she meets Si-heon, who bears an uncanny resemblance to her deceased boyfriend, adding to the emotional complexity of her journey.

---
## [YhuCaCla/app-dev](https://github.com/YhuCaCla/app-dev)@[2fea354bdf...](https://github.com/YhuCaCla/app-dev/commit/2fea354bdf96162baf636f72f862fc385eff0ed7)
#### Thursday 2023-11-23 01:31:23 by YhuCaCla

Update README.md

'Avatar'
Sixteen years after the Na'vi repelled the RDA invasion of Pandora, Jake Sully, chief of the Omatikaya clan, raises a family with Neytiri, including sons Neteyam and Lo'ak, daughter Tuk, and adopted daughter Kiri. Spider, the Pandora-born human son of Colonel Miles Quaritch, visits their children while being raised by scientists who stayed on Pandora. To the Na'vi's dismay, the RDA returns to colonize Pandora, led by Frances Ardmore. Quaritch's Recombinant serves as their leader.

Jake leads a guerilla campaign against the RDA, capturing Jake's children during a counterinsurgency mission. After spending time with Spider, Quaritch learns about Na'vi culture and language. The family retreats to Pandora's eastern sea, where they learn the ways of the reef people, develop a spiritual bond with the sea, and befriend Tsireya, daughter of Chief Tonowari and his wife Ronal.

'A Time Called You'
A Time Called You is a story about Jun-hee, who is still grieving the loss of her boyfriend Yeon-jun in the year 2023, a year after his passing. She somehow travels back in time to 1998 and wakes up inhabiting the body of a different person, 18-year-old Min-ju. As she navigates this new reality, she meets Si-heon, who bears an uncanny resemblance to her deceased boyfriend, adding to the emotional complexity of her journey.

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[b7ca70e472...](https://github.com/cheesePizza2/Foundation-19/commit/b7ca70e472782606c7fac09026471575745ccb74)
#### Thursday 2023-11-23 01:59:52 by cheesePizza2

Fixes goals system harddels (#1316)

* shit

* fuck you

* removes spaces

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[a666b103d3...](https://github.com/cheesePizza2/Foundation-19/commit/a666b103d3adcbcc9d954d05bad4e348f0d6ffaa)
#### Thursday 2023-11-23 01:59:52 by cheesePizza2

Fixes CDZ Medical Checkpoint windoors (#1386)

* changes

* fuck me

* fuck you

---
## [AnouarXperience/MyCourses-App-Launch](https://github.com/AnouarXperience/MyCourses-App-Launch)@[1cd879c9ef...](https://github.com/AnouarXperience/MyCourses-App-Launch/commit/1cd879c9effe98b4fd6d20a22da45854c5cce3d7)
#### Thursday 2023-11-23 02:43:09 by lanwaros

📚 **MyCourses App Launch - Version 1.0.0**

Embark on an enhanced learning journey with the launch of the "MyCourses App"! This commit marks the introduction of Version 1.0.0, designed to elevate your learning experience.

**Key Features:**
- **User-Friendly Design:** Navigate through courses and resources effortlessly with an intuitive interface.
- **Course Management:** Access, enroll, and keep track of your courses in one centralized location.
- **Multimedia Learning:** Enjoy a variety of multimedia resources for an engaging learning experience.
- **Mobile Accessibility:** Optimized for mobile devices, making learning convenient anytime, anywhere.
- **Built with Android Studio:** Developed using Android Studio for a robust and efficient app.

**Tech Stack:**
- Frontend: Android Studio
- Version Control: Git, GitHub

This release lays the foundation for an accessible and dynamic learning platform. We look forward to enhancing your learning experience in future updates. Happy learning! 🎓🚀

---
## [hello-smile6/solanum](https://github.com/hello-smile6/solanum)@[06c5309534...](https://github.com/hello-smile6/solanum/commit/06c53095343c2756208f6398bb7e00fb2cbe46dd)
#### Thursday 2023-11-23 03:02:34 by Ed Kellett

m_sasl: Remove implicit abort on registration

This doesn't make sense in a world where post-registration SASL is
allowed, and should fix one case of an annoying login desync that's seen
in the real world.

Specifically, when a client sends its final AUTHENTICATE and Atheme
receives it, it sends an SVSLOGIN for that client. If the client sends
us its CAP END *before* we see the SVSLOGIN, the implicit abort will try
to abort the SASL session that's already succeeded.

Atheme interprets this as an instruction to forget about the successful
SASL session; you'll connect unidentified. But it's already sent
SVSLOGIN, which will log the client in ircd-side, causing ircd and
services views to differ until the user authenticates again manually.

I think allowing a SASL session to be aborted when it has already
succeeded is an Atheme bug, and it can still be triggered without this
change. But our behaviour here seems silly anyway.

---
## [xuhancn/pytorch](https://github.com/xuhancn/pytorch)@[a911b4db9d...](https://github.com/xuhancn/pytorch/commit/a911b4db9d82238a1d423e2b4c0a3d700217f0c1)
#### Thursday 2023-11-23 03:25:06 by voznesenskym

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang
ghstack dependencies: #113926

---
## [wingyplus/dagger](https://github.com/wingyplus/dagger)@[80180aaaed...](https://github.com/wingyplus/dagger/commit/80180aaaed1e1e91a13dbf7df7e0411a9a54c7d3)
#### Thursday 2023-11-23 03:35:39 by Justin Chadwell

Fix secret scrubbing log latency (#6034)

* fix: use custom implementation for secret scrubbing

This was a fun exercise in processing streams in go, and an absolutely
massive nerd-snipe :(

Essentially, we need a custom transformer to handle *precisely* matching
Reads on the underlying source with the output - we shouldn't hold
output any longer than is absolutely neccessary.

To be able to do this at all in any reasonable way, we need a trie, and
handle *all* the secrets at once, instead of doing multiple passes.
Multiple passes won't work, since it's possible to accidentally trim too
much at each step, which would be very sad.

> e.g. imagine secrets (aaa, bbb, ccc, etc), and an input (cba)
>
> In removing secret aaa, we would trim to cb, then we'd remove bbb to
> trim to c, then finally trim to nothing. However, this is overly
> enthusiastic, we could easily just trim to cb, if we knew about all
> the secrets at once.

So, we need a trie, and we need a custom implementation of one. This is
because *no off the shelf implementation* seems to allow traversing the
trie state-by-state. Thankfully, it's a pretty short implementation to
implement one from scratch, and not too much harder to turn it into a
radix tree (which lets us use quite a lot less memory).

With our trie, we can implement our custom transformer, which is *an
utter pain*. Honestly, the comments should explain all the fun edge
cases it's possible to hit. There's a lot of tests added as well, each
of which was a real horrible thing I hit while implementing it.

I played around a bit with benchmarking, but ugh, it's a *tiny* bit
slower than the original implementation (maybe by like ~25%?). It's not
huge, but the latency problem is *actually solved*. Some potential
things I did look into and gave up on:
- Only copy into dstBuf when dst is full (requires tons of extra
conditionals, so slows everything down).
- Avoid copies at all costs by having "virtual buffer pointers" into
src, that indicate future data to copy (not only is this *slower*, the
logic becomes truly incomprehensible).
- Playing with off-the-shelf radix tree implementations, but they're so
inconvenient to use for this specific use case, it'd be way more
trouble than it'd be worth.

Any ideas welcome, but honestly, I've looked at enough flamegraphs
today.

Signed-off-by: Justin Chadwell <me@jedevc.com>

* test: avoid use of require.Eventually for secret scrubbing

Signed-off-by: Justin Chadwell <me@jedevc.com>

---------

Signed-off-by: Justin Chadwell <me@jedevc.com>

---
## [cyphar/runc](https://github.com/cyphar/runc)@[83e0f02417...](https://github.com/cyphar/runc/commit/83e0f024179a1b5ba12be5e7810c73948aeab209)
#### Thursday 2023-11-23 03:37:05 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not strictly necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) since
only operating on the actual inodes associated with the tid requires
this locking, but because of the pre-3.17 fallback for CentOS, we have
to do this in most cases.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [Arborsm/GregTech-Modern](https://github.com/Arborsm/GregTech-Modern)@[852bb70272...](https://github.com/Arborsm/GregTech-Modern/commit/852bb70272ec9040d0dc6d1b695442a43f3969c3)
#### Thursday 2023-11-23 04:14:48 by screret

Byproduct limiting (#572)

* it doesn't crash but kinda doesn't work either

* Holy shit it works!!!! gonna implement multiblock voiding mode button in separare PR.

* final lil' fixes

* reviews?

---
## [dudw/ripgrep](https://github.com/dudw/ripgrep)@[082245dadb...](https://github.com/dudw/ripgrep/commit/082245dadb3854238e62b91aa95a46018cf16ef1)
#### Thursday 2023-11-23 04:18:49 by Andrew Gallant

cli: replace clap with lexopt and supporting code

ripgrep began it's life with docopt for argument parsing. Then it moved
to Clap and stayed there for a number of years. Clap has served ripgrep
well, and it probably could continue to serve ripgrep well, but I ended
up deciding to move off of it.

Why?

The first time I had the thought of moving off of Clap was during the
2->3->4 transition. I thought the 3.x and 4.x releases were great, but
for me, it ended up moving a little too quickly. Since the release of
4.x was telegraphed around when 3.x came out, I decided to just hold off
and wait to migrate to 4.x instead of doing a 3.x migration followed
shortly by another 4.x migration. Of course, I just never ended up doing
the migration at all. I never got around to it and there just wasn't a
compelling reason for me to upgrade. While I never investigated it, I
saw an upgrade as a non-trivial amount of work in part because I didn't
encapsulate the usage of Clap enough.

The above is just what got me started thinking about it. It wasn't
enough to get me to move off of it on its own. What ended up pushing me
over the edge was a combination of factors:

* As mentioned above, I didn't want to run on the migration treadmill.
This has proven to not be much of an issue, but at the time of the
2->3->4 releases, I didn't know how long Clap 4.x would be out before a
5.x would come out.
* The release of lexopt[1] caught my eye. IMO, that crate demonstrates
exactly how something new can arrive on the scene and just thoroughly
solve a problem minimalistically. It has the docs, the reasoning, the
simple API, the tests and good judgment. It gets all the weird corner
cases right that Clap also gets right (and is part of why I was
originally attracted to Clap).
* I have an overall desire to reduce the size of my dependency tree. In
part because a smaller dependency tree tends to correlate with better
compile times, but also in part because it reduces my reliance and trust
on others. It lets me be the "master" of ripgrep's destiny by reducing
the amount of behavior that is the result of someone else's decision
(whether good or bad).
* I perceived that Clap solves a more general problem than what I
actually need solved. Despite the vast number of flags that ripgrep has,
its requirements are actually pretty simple. We just need simple
switches and flags that support one value. No multi-value flags. No
sub-commands. And probably a lot of other functionality that Clap has
that makes it so flexible for so many different use cases. (I'm being
hand wavy on the last point.)

With all that said, perhaps most importantly, the future of ripgrep
possibly demands a more flexible CLI argument parser. In today's world,
I would really like, for example, flags like `--type` and `--type-not`
to be able to accumulate their repeated values into a single sequence
while respecting the order they appear on the CLI. For example, prior
to this migration, `rg regex-automata -Tlock -ttoml` would not return
results in `Cargo.lock` in this repository because the `-Tlock` always
took priority even though `-ttoml` appeared after it. But with this
migration, `-ttoml` now correctly overrides `-Tlock`. We would like to
do similar things for `-g/--glob` and `--iglob` and potentially even
now introduce a `-G/--glob-not` flag instead of requiring users to use
`!` to negate a glob. (Which I had done originally to work-around this
problem.) And some day, I'd like to add some kind of boolean matching to
ripgrep perhaps similar to how `git grep` does it. (Although I haven't
thought too carefully on a design yet.) In order to do that, I perceive
it would be difficult to implement correctly in Clap.

I believe that this last point is possible to implement correctly in
Clap 2.x, although it is awkward to do so. I have not looked closely
enough at the Clap 4.x API to know whether it's still possible there. In
any case, these were enough reasons to move off of Clap and own more of
the argument parsing process myself.

This did require a few things:

* I had to write my own logic for how arguments are combined into one
single state object. Of course, I wanted this. This was part of the
upside. But it's still code I didn't have to write for Clap.
* I had to write my own shell completion generator.
* I had to write my own `-h/--help` output generator.
* I also had to write my own man page generator. Well, I had to do this
with Clap 2.x too, although my understanding is that Clap 4.x supports
this. With that said, without having tried it, my guess is that I
probably wouldn't have liked the output it generated because I
ultimately had to write most of the roff by hand myself to get the man
page I wanted. (This also had the benefit of dropping the build
dependency on asciidoc/asciidoctor.)

While this is definitely a fair bit of extra work, it overall only cost
me a couple days. IMO, that's a good trade off given that this code is
unlikely to change again in any substantial way. And it should also
allow for more flexible semantics going forward.

Fixes #884, Fixes #1648, Fixes #1701, Fixes #1814, Fixes #1966

[1]: https://docs.rs/lexopt/0.3.0/lexopt/index.html

---
## [Marrone321/STALKER-13](https://github.com/Marrone321/STALKER-13)@[1ad74ef093...](https://github.com/Marrone321/STALKER-13/commit/1ad74ef0939fc81f96ea3e4485a0b82406a6d22e)
#### Thursday 2023-11-23 04:26:07 by ProtivogaSpriter

FUCK YOU FUCK YOU

FUCK YOU!!!!

this literally comments out the entire renegades job file

---
## [Marrone321/STALKER-13](https://github.com/Marrone321/STALKER-13)@[fa6e6ee157...](https://github.com/Marrone321/STALKER-13/commit/fa6e6ee1574cec2561d35f89969beaa595f11094)
#### Thursday 2023-11-23 04:26:07 by emoats18

Merge pull request #214 from ProtivogaSpriter/srptotr

FUCK YOU FUCK YOU

---
## [nehaareddy/dsa0302-nlp](https://github.com/nehaareddy/dsa0302-nlp)@[fa145f0c49...](https://github.com/nehaareddy/dsa0302-nlp/commit/fa145f0c49b489aa1201161890a7781c2b375d35)
#### Thursday 2023-11-23 04:28:24 by nehaareddy

OUTPUT

Sentence 1: The cat sat on the mat.

Word: cat
Definitions:
- feline mammal usually having thick soft fur and no ability to roar: domestic cats; wildcats
- an informal term for a youth or man
- a spiteful woman gossip
- the leaves of the shrub Catha edulis which are chewed like tobacco or used to make tea; has the effect of a euphoric stimulant
- a whip with nine knotted cords
- a large tracked vehicle that is propelled by two endless metal belts; frequently used for moving earth in construction and farm work
- any of several large cats typically able to roar and living in the wild
- a method of examining body organs by scanning them with X rays and using a computer to construct a series of cross-sectional scans along a single axis
- beat with a cat-o'-nine-tails
- eject the contents of the stomach through the mouth
Synonyms:
- puke, disgorge, bozo, upchuck, Caterpillar, computerized_axial_tomography, guy, true_cat, regorge, spue, kat, cast, computed_axial_tomography, cat, purge, cat-o'-nine-tails, vomit_up, computed_tomography, chuck, computerized_tomography, qat, barf, be_sick, CT, vomit, spew, retch, African_tea, khat, regurgitate, honk, Arabian_tea, hombre, sick, big_cat, quat, throw_up, CAT

Word: sat
Definitions:
- the seventh and last day of the week; observed as the Sabbath by Jews and some Christians
- be seated
- be around, often idly or without specific purpose
- take a seat
- be in session
- assume a posture as for artistic purposes
- sit and travel on the back of animal, usually while controlling its motions
- be located or situated somewhere
- work or act as a baby-sitter
- show to a seat; assign a seat for
- serve in a specific professional capacity
Synonyms:
- baby-sit, Saturday, pose, seat, model, Sabbatum, ride, sit_down, Sat, sit_around, sit, posture

Word: on
Definitions:
- in operation or operational
- (of events) planned or scheduled
- with a forward motion
- indicates continuity or persistence or concentration
- in a state required for something to function or be effective
Synonyms:
- along, on

Sentence 2: The dog barked loudly.

Word: dog
Definitions:
- a member of the genus Canis (probably descended from the common wolf) that has been domesticated by man since prehistoric times; occurs in many breeds
- a dull unattractive unpleasant girl or woman
- informal term for a man
- someone who is morally reprehensible
- a smooth-textured sausage of minced beef or pork usually smoked; often served on a bread roll
- a hinged catch that fits into a notch of a ratchet to move a wheel forward or prevent it from moving backward
- metal supports for logs in a fireplace
- go after with the intent to catch
Synonyms:
- chase_after, blackguard, andiron, go_after, frank, track, chase, pawl, heel, Canis_familiaris, weenie, trail, cad, hot_dog, tag, dog, hound, give_chase, wiener, click, frump, domestic_dog, wienerwurst, dog-iron, tail, detent, frankfurter, hotdog, firedog, bounder

Word: barked
Definitions:
- speak in an unfriendly tone
- cover with bark
- remove the bark of a tree
- make barking sounds
- tan (a skin) with bark tannins
Synonyms:
- bark, skin

Sentence 3: She played the piano beautifully.

Word: played
Definitions:
- participate in games or sport
- act or have an effect in a specified way or with a specific effect or outcome
- play on an instrument
- play a role or part
- be at play; be engaged in playful activity; amuse oneself in a way characteristic of children
- replay (as a melody)
- perform music on (a musical instrument)
- pretend to have certain qualities or state of mind
- move or seem to move quickly, lightly, or irregularly
- bet or wager (money)
- engage in recreational activities rather than work; occupy oneself in a diversion
- pretend to be somebody in the framework of a game or playful activity
- emit recorded sound
- perform on a certain location
- put (a card or piece) into play during a game, or act strategically as if in a card game
- engage in an activity as if it were a game rather than take it seriously
- behave in a certain way
- cause to emit recorded audio or video
- manipulate manually or in one's mind or imagination
- use to one's advantage
- consider not very seriously
- be received or accepted or interpreted in a specific way
- behave carelessly or indifferently
- cause to move or operate freely within a bounded space
- perform on a stage or theater
- be performed or presented for public viewing
- cause to happen or to occur as a consequence
- discharge or direct or be discharged or directed as if in a continuous stream
- make bets
- stake on the outcome of an issue
- shoot or hit in a particular manner
- use or move
- employ in a game or in a specific position
- contend against an opponent in a sport, game, or battle
- exhaust by allowing to pull on the line
- (of games) engaged in
Synonyms:
- wreak, roleplay, meet, bet, make_for, work, recreate, toy, act, spiel, trifle, diddle, encounter, played, dally, playact, wager, take_on, play, fiddle, bring, represent, run, flirt, act_as

Word: piano
Definitions:
- a keyboard instrument that is played by depressing keys that cause hammers to strike tuned strings and produce sounds
- (music) low loudness
- used chiefly as a direction or description in music
- used as a direction in music; to be played relatively softly
Synonyms:
- soft, forte-piano, pianissimo, piano, softly, pianoforte

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[52f69b96ee...](https://github.com/Bubberstation/Bubberstation/commit/52f69b96eebfbe14a763ae9c5a8dd7ef156c4582)
#### Thursday 2023-11-23 04:44:31 by The-Sun-In-Splendour

mid-round salt pr about EMP mold because being repeatedly shocked 500 times in a row unless you get charcoal (now called syniver or whatever fuck new chems) is not what I consider to be fun gameplay (#755)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
emp mold mosquitoes no longer put you in shock stunlock hell because
that shit is not funny
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game
it made me mad and this is a salt pr

![image](https://github.com/Bubberstation/Bubberstation/assets/70348069/b5002caa-d401-478a-9d48-fbc772c05b3e)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
balance: emp mold mosquitoes no longer shock you all the time until you
have a stroke irl over the annoyance
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---
## [NVIDIA/Fuser](https://github.com/NVIDIA/Fuser)@[922fab891f...](https://github.com/NVIDIA/Fuser/commit/922fab891f98f2cedb7fc7f8a408000e9c874309)
#### Thursday 2023-11-23 05:37:38 by Gao, Xiang

Refactor ldmatrix and mma input scheduling (#1303)

This PR is stacked on https://github.com/NVIDIA/Fuser/pull/1311

Similar to https://github.com/NVIDIA/Fuser/pull/1210, this PR schedules
the allocation domain of mma inputs and ldmatrix. Similar to the
situation of https://github.com/NVIDIA/Fuser/pull/1210, the modified
piece of code was initially implemented prior to the invention of
allocation, therefore there were some hacks around there.

For the case of ldmatrix, if you look at the official doc
https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#warp-level-matrix-instructions-ldmatrix,
you will find that, there are basically two correct but different
schedules:
1. If you look at the memory format of which thread own which part of
the tensor, from this information, you will able to derive one schedule.
Let's call this memory-layout-based schedule.
2. If you look at which thread should pass the address of which item as
an operand to this instruction, from this information, you will be able
to derive another schedule. Let's call this indexing-based schedule.

Unfortunately, these two schedules does not match. Prior to this PR, we
were uniquely using the indexing-based schedule. This is fine with
ldmatrix, but the index of mma inputs is basically incorrect, and
therefore a hacked index was used.

I believe the most natural way to implement these two separate schedules
is as follows: Assume we have a fusion:
```C++
Tregister = ldmatrix(Tsmem)
Tregister2 = broadcast(Tregister)
... = mma(Tregister2, ...)
```
then the allocation domain of `Tregister2` and `Tregister` must be
scheduled as memory-layout-based schedule, the leaf domain of
`Tregister` must be scheduled as the indexing-based schedule. The leaf
domain of `Tregister2` should be scheduled similar to
memory-layout-based schedule.

In this PR, I refactored the mma swizzler for mma inputs to implement
the above design. In the refactored code, `scheduleTuringOperandRead`
schedules the memory-layout-based schedule, and `scheduleLdMatrix`
starts from the memory-layout based schedule, and generates the
indexing-based schedule on top of it.

Due to this change, the codegen of `MmaOp` no longer needs special
handling the index, it is now just a naive:
```C++
  void handle(const MmaOp* mma) final {
    indent() << genMmaOp(mma) << "(\n";
    indent() << kTab << gen(mma->out()) << ",\n";
    indent() << kTab << gen(mma->inA()) << ",\n";
    indent() << kTab << gen(mma->inB());
    code_ << ");\n";
  }
```

However, our current sync analysis and indexing infrastructure is not
capable of analyzes this style of scheduling, and therefore, I would
need to add additional hacking points to them:

- In our sync analysis, currently, it always assume that the
parallelization of the leaf domain determines which thread owns which
item. With the allocation domain support, it is actually the
parallelization of the *allocation* domain determines which thread owns
which item. In a perfect world, for exprs other than ldmatrix, warp
shuffling, and mma op, the analysis based on leaf domain should match
with the analysis based on the allocation, because, for example, if you
do `y = sin(x)`, there is no way that `y` get the result from other
threads, but our system should not assume that the analysis based on
leaf domain always match with the analysis based on the allocation
generally. Unfortunately, at the current state, our system can not
handle this correctly. So I added one hack to it: if the expr is
ldmatrix, assume the schedule is correct and just give up sync analysis.
I think for now, this is a valid solution, because we will be rewriting
our sync analysis with `IdModel` anyway.
- In our indexing of `MmaOp` producer, we are incorrectly marking some
of allocation domain as zero domain, where it should not be. Similar to
the above point, the mma op implies warp shuffling of data. During
indexing, it does make sense to replay consumer as producer, but only to
the block level. Within a warp, it makes no sense to replay the producer
as consumer. I think we should carefully think about the design when we
are rewriting our indexing with `IdModel`, but for this PR, I just
manually set the last three `IterDomain`s of mma input as special and
not treat them as zero domain.

I believe this PR is an improvement compared to the previous approach,
because it has less special handling in the schedule itself, but I still
think we are far from supporting ldmatrix and mma ops elegantly. In the
future, I think we should:
1. Reconsider the design of different domains, leaf vs allocation, etc.
and figure out what is the best way to schedule ldmatrix.
2. When we rewriting, we should keep the indexing of ldmatrix and mma in
mind, and make sure that it can be supported without any hack in the new
system.

---
## [lgritz/OpenImageIO](https://github.com/lgritz/OpenImageIO)@[84c84bd21f...](https://github.com/lgritz/OpenImageIO/commit/84c84bd21f63a1a090877f7ebe7e39a503c116ce)
#### Thursday 2023-11-23 05:40:45 by Larry Gritz

fix: oiiotool --autocc and color config inventory cleanup

The important bug fix is in oiiotool image input when autocc is used,
where we reversed the sense of a test and did the autocc-upon-input if
the file's color space was equivalent to the scene_linear space
(pointlessly), and skipped the conversion if they were different (oh
no, big bug!).

Along the way:

* Add missing try/catch around OCIO call that should have had it.

* Some very ugly SPI-specific recognize-by-name color space heuristics.
  I hate this, sorry, but it solves a really important problem for me.

* A bunch of additional debugging messages during color space inventory,
  enabled only when debugging, so nobody should see these but me.

* A couple places where we canonicalize the spelling of "oiio:ColorSpace".

Note that there is still an issue with the color space classification
using OCIO 2.3+'s identification of built-in equivalents by
name. These are shockingly expensive. I will return to this later.

---
## [MendozaSalaw/app-dev](https://github.com/MendozaSalaw/app-dev)@[fd894659c5...](https://github.com/MendozaSalaw/app-dev/commit/fd894659c556e10182342dc885857b7eed25df3a)
#### Thursday 2023-11-23 06:29:19 by MendozaSalaw

Update README.md

Eren Yeager is a boy who lives in the town of Shiganshina, located on the outermost of three circular walls which protect their inhabitants from Titans. In the year 845, the first wall (Wall Maria) is breached by two new types of Titans, the Colossal Titan and the Armored Titan. During the incident, Eren's mother is eaten by a Smiling Titan while Eren escapes. He swears revenge on all Titans and enlists in the military along with his childhood friends Mikasa Ackerman and Armin Arlert.

---
## [zphtet/react](https://github.com/zphtet/react)@[ac1a16c67e...](https://github.com/zphtet/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Thursday 2023-11-23 06:50:23 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [James-Day/LeetCode](https://github.com/James-Day/LeetCode)@[07ff2b28fc...](https://github.com/James-Day/LeetCode/commit/07ff2b28fc93e848ce8c0e1a8aaa005aa5bf30c2)
#### Thursday 2023-11-23 06:54:51 by James-Day

Daily LeetCode (11/23)

I really enjoyed this daily. Another medium that I was able to solve
without too much trouble. I honestly thought that my solution must not
have been optimized because the solution is O(n*mlog(n)) time
complexity. Overall it was a cool problem. I wish there was some way to
not sort same sections of the array multiple times, But I just couldn't
think of a way around it.(I don't think it's possible anyway)

---
## [UncertainSchrodinger/PathOfBuilding](https://github.com/UncertainSchrodinger/PathOfBuilding)@[4eed4f6051...](https://github.com/UncertainSchrodinger/PathOfBuilding/commit/4eed4f6051359b576d284c2420e96b9dd181606b)
#### Thursday 2023-11-23 07:05:54 by Tatu Argillander

lua: Use regular require instead of LoadModule

LoadModule just seems to do some convoluted require. It'll load the
module as text, pass it back down to lua for evaluation and then call it
as a function. All of this is done through loadfile and friends.

It's a table. Just fucking return it and require it.

Unless there's some magic here I'm too fucking stupid to understand.

---
## [Addust/Yogstation](https://github.com/Addust/Yogstation)@[bc3374c7da...](https://github.com/Addust/Yogstation/commit/bc3374c7dacf3b2db39fe1c4dc36551d7ba82f79)
#### Thursday 2023-11-23 07:49:53 by cowbot92

Even Further Heretic Adjustments: New minor things, Bug fixes, Heretic path adjustments and movement adjustments! (#20843)

* a whole lot of shit

yessir

* gun stuff

crazy

* haha

fuck guns

* my brain bursts

it hurts

* so much shit

im done

* fuck forgot this

god damn low memory mode

* removes backslashes

really linter

* oops

typos

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[94603a2a96...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/94603a2a9636ab5a9e8ded9247b490a5d6670da4)
#### Thursday 2023-11-23 08:33:23 by SkyratBot

[MIRROR] Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) [MDB IGNORE] (#25102)

* Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#79803)

## About The Pull Request

Simply put, due to how "caseless" is an element added to the ammo when
it hits something, but ammo is qdeleted upon hitting someone. If shot
point blank without combat mode (for some reason) it tries to add
caseless to an ammo that no longer exists. For some reason, the result
of this is to just fucking crash DS instead of aborting the adding of
the element. The ammo isnt reusable anymore, but I'll take that over
crashing.

## Why It's Good For The Game

Removes a game-breaking bug. I hate gun ammo code so much.

## Changelog

:cl:
fix: Stopped a DS crash when shooting a rebar crossbow in specific
circumstances.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP)

---------

Co-authored-by: KingkumaArt <69398298+KingkumaArt@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [howlagon/banana_farmer](https://github.com/howlagon/banana_farmer)@[bf1038ddd3...](https://github.com/howlagon/banana_farmer/commit/bf1038ddd36b0cf132338bba26480c6e95e84611)
#### Thursday 2023-11-23 09:07:12 by howlagon

fix average (for the 4th fucking time now), fix logger (again. stop breaking you stupid bitch)

---
## [Offroaders123/Dino-TSX](https://github.com/Offroaders123/Dino-TSX)@[868539ae9e...](https://github.com/Offroaders123/Dino-TSX/commit/868539ae9e95b012449d2861334de565057f429e)
#### Thursday 2023-11-23 09:10:44 by Offroaders123

Proper Property Validation

Proper property checking! This programmatically sorts the prototypes to only get the setter-supported, or value-based properties on the prototypes. This does the same work which I just did manually in the previous last steps, in that I check the property descriptor types of the value itself, to check whether it's a value which can be applied to, hence making it something which should be available in JSX-land. `Object.getOwnPropertyDescriptors()` shows more entries which previously weren't accessible from my original checking, so I think that's why those values are there now as well. Looked into the legacy prototype management properties/methods, and turns out those aren't documented by TS's types, I think because they are essentially heavily deprecated, and they don't want people to look into trying to use those, since they aren't reliably implemented in terms of the spec.

I'm really happy that my eyeball-knowledge of what properties should be present, was actually right! That means my general understanding is really close to how things are, that's relieving to me. Nothing changed except for the constructors and the legacy getter implementations. I know what essentially all of the element properties do/what their general ideas are. I definitely want to continue working on ARIA accessibility attributes though, I can do much better at that for my components.

https://stackoverflow.com/questions/30158515/list-all-prototype-properties-of-a-javascript-object
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/__defineGetter__

Listening to Storm Corrosion with this one. I really like the listen now. I think my more extreme musical listens recently have helped me understand this album a bit more, or maybe it's just the listening experience that's key for it. It's late at night, so I think it matches the mood accordingly.

Now I'm listening to Raven, trying to find the connections between Sectarian (Grace for Drowning as a whole), Storm Corrosion, and Raven. Small instances feel like they foreshadow and reference the others, and I want to figure out what it is about it. Man, I love Luminol.

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[6304f127e1...](https://github.com/Danielkaas94/DTAP/commit/6304f127e14d69c544118bb0f70d6e25fd031027)
#### Thursday 2023-11-23 09:33:45 by Daniel Kaas Bundgaard Jørgensen

💀 Martyr 💀
Take the angels away
The only ones who knew already know my name
Times re-known for a war
To be the only one that ever knew the way

Don’t be a martyr, it will be alright
I can see you've run out...
But still you make the most of making the most

I don’t want nobody to haunt me
Every time I see your face in the night
I know it’s all the voice in my head.
Time, time, it’s all been time
I feel the call of all the things that I dread
I know it's all a voice in my head...

Take the anger away
So many come, so many seem to go that way
It’s on now...
Digging a hole in the soul
To see the confines of the mental overload
You melted it all down

I don’t want nobody to haunt me
Every time I see your face in the night
I know it’s all the voice in my head.

But still you make the most of making the most.
I can see you’ve run out
But still you make the most of making the most.

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[4e00f5722d...](https://github.com/Danielkaas94/DTAP/commit/4e00f5722d99c6e9c2d64d7f00549737886a500e)
#### Thursday 2023-11-23 09:35:22 by Daniel Kaas Bundgaard Jørgensen

😵‍💫💔 Head On To Heartache (Let Them Rot) 💔😵‍💫
Secure and hold fast, before you lose control!

Its hell and high water
Believe in gods, hooves, horns and thunder
Days of wrath don't go seeking shelter
Poison creeps, serpents slither, then slumber
Bastards, paradise, true the bargain was made
Full thrust enticed to an early grave
Deals were struck late into a cold winters eve
The table was set, laid out for the feast..

Secure and hold fast, before you lose control
Head on to Heartache, Beware of the promises made
Head on to Heartache, steadfast to an early grave (let the rot!)

Deals with the Devil, theres no second best
It's in my nature to say fuck the rest
Ever thought the world was crashing down?
Man the people were talking all around

---
## [aromanovich/temporal](https://github.com/aromanovich/temporal)@[1be76e3583...](https://github.com/aromanovich/temporal/commit/1be76e3583ef01ba9f79503e81fed5b7c9ab389c)
#### Thursday 2023-11-23 10:51:42 by Tim Deeb-Swihart

Replace gogo/protobuf with google/protobuf (#5032)

**What changed?**

gogo/protobuf has been replaced with Google's official go compiler. 

**Why?**

gogo/protobuf has been deprecated for some time and the community is
moving on, building new tools (like vtproto) atop google's v2 compiler.

**How did you test it?**

`make test`

**Potential risks**

1. The change from embedded gogo-generated-structs to
google-generated-pointers-to-structs created a risk of nil pointer
exceptions. I've fixed all the ones our tests found but it's possible
there are more lurking in the new code.
2. This change may cause our performance to decrease. Certainly
encoding/deconding of proto objects will become slower, but the overuse
of pointers by the google compiler may negatively affect our overall
performance. We'll need to keep an eye on the GC stats
3. This breaks the HTTP API. We will not support [shortand payload
encoding](https://github.com/temporalio/proposals/blob/master/api/http-api.md#payload-formatting)
in this first pass; that will come once this initial work is in testing.

**Breaking changes for developers**

- `*time.Time` in proto structs will now be
[timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/protobuf@v1.31.0/types/known/timestamppb#section-documentation)
- `*time.Duration` will now be
[durationpb.Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb)
- V2-generated structs embed locks, so you cannot dereference them. `go
vet` will scream at you about this. If you need a copy, use
`proto.Clone`.
- If the performance of this sucks then I will either update our code
generator to add shallow-clone methods or hand-roll the ones we need
- Proto enums will, when formatted to JSON, now be in
`SCREAMING_SNAKE_CASE` rather than `PascalCase`. We decided (in
discussion with the SDK team) that now was as good a time as any to rip
the bandage off.
- Proto objects, or objects embedding protos, cannot be compared using
`reflect.DeepEqual` or _anything_ that uses it. This includes `testify`
and `mock` equality testers!
- You will need to use the `common/testing/protorequire`,
`common/testing/protoassert`, or `common/testing/protomock` packages
instead. I've implemented proto-compatible matchers and assertions there
for all cases I've encountered
- If you need `reflect.DeepEqual` for any reason you can use
`go.temporal.io/api/temporalproto.DeepEqual` instead

Note that history loading will not be impacted by the JSON changes: I
rewrote history loading to dynamically fix incoming history JSON data
(like all our other sdks); you can find this code in [my fork of our go
API](https://github.com/tdeebswihart/temporal-api-go/blob/master/internal/temporalhistoryv1/load.go)
alongside its tests.

**🚨Sharp Edges Introduced🚨**

Beware `*timestamppb.Timestamp.AsTime()`. If you need to extract a time
value from a proto time (timestamppb) **always** make sure to check
whether it's nil first. When the proto object is `nil` `AsTime()` will
return a non-zero time at the proto epoch: UTC midnight on January 1,
1970.

I've made this mistake multiple times during this transition and each
time it's been a pain to debug

**Is hotfix candidate?**

No.

---
## [Teuhon-Rakennusyhtio/Jumpnaut](https://github.com/Teuhon-Rakennusyhtio/Jumpnaut)@[b0e35e89ea...](https://github.com/Teuhon-Rakennusyhtio/Jumpnaut/commit/b0e35e89eac4f368164f4c482cdee9717bca84d3)
#### Thursday 2023-11-23 11:03:54 by Alex Yli-Paavalniemi

Now you cant scroll to settings in the start menu by accident. Also probably some other fixes but I cant remember after trying to wrestle with that shit fuck menu again

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7f8957cdda...](https://github.com/treckstar/yolo-octo-hipster/commit/7f8957cdda0a93afab1646b89d791d146af9bc90)
#### Thursday 2023-11-23 11:22:06 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [TailerDerdan/TaleMaker](https://github.com/TailerDerdan/TaleMaker)@[f556a4b9cc...](https://github.com/TailerDerdan/TaleMaker/commit/f556a4b9cc8d0b028f4f7baa32916e78ad005813)
#### Thursday 2023-11-23 12:05:53 by UnionMaki

It starts with one
All I know
It's so unreal
Watch you go
I tried so hard and got so far
But in the end, it doesn't even matter
I had to fall to lose it all
But in the end, it doesn't even matter
One thing, I don't know why
It doesn't even matter how hard you try
Keep that in mind, I designed this rhyme
To remind myself of a time when I tried so hard
In spite of the way you were mockin' me
Actin' like I was part of your property
Remembering all the times you fought with me
I'm surprised it got so far
Things aren't the way they were before
You wouldn't even recognize me anymore
Not that you knew me back then
But it all comes back to me in the end
You kept everything inside
And even though I tried, it all fell apart
What it meant to me will eventually
Be a memory of a time when I
I tried so hard and got so far
But in the end, it doesn't even matter
I had to fall to lose it all
But in the end, it doesn't even matter
One thing, I don't know why
It doesn't even matter how hard you try
Keep that in mind
I designed this rhyme to explain in due time
All I know
Time is a valuable thing
Watch it fly by as the pendulum swings
Watch it count down to the end of the day
The clock ticks life away
It's so unreal
You didn't look out below
Watch the time go right out the window
Tryin' to hold on, they didn't even know
I wasted it all just to watch you go
I kept everything inside
And even though I tried, it all fell apart
What it meant to me will eventually be a memory
Of a time when I tried so hard

---
## [CollaboraOnline/online](https://github.com/CollaboraOnline/online)@[3185307c7a...](https://github.com/CollaboraOnline/online/commit/3185307c7afa5e76bd10b76a2d97ecbdbc97455a)
#### Thursday 2023-11-23 13:23:25 by Skyler Grey

Stop hiding both menu and notebookbar softlocking

Previously, when using the Collapse_Notebookbar postmessage or
equivalent ui_defaults (SpreadsheetToolbar=false, etc.), particularly in
compact mode, it was possible to additionally hide the menu bar. As the
button to show the menu bar is on the notebookbar, this meant that you
couldn't reactivate either notebookbar or menubar until you refreshed
the page. This is particularly annoying in integrators that may not
provide an easy way to reload the page

This commit makes it so that hiding the menu bar automatically
uncollapses the notebookbar and won't let it be collapsed again. Whether
the notebook bar should be collapsed (the last thing done to it was a
collapse) is remembered and restored after the menu bar is shown again,
so if you send a postmessage that will affect the state of the
notebookbar after the menu is shown (even though it will not affect the
notebookbar's state immediately)

Caveats:
- If you are hiding the notebookbar to limit the control the user has,
  that's broken by this commit as it makes it impossible to hide both
  the menu and notebook bars at the same time.
- The notebook bar will be hidden again when re-showing the menu bar,
  however there still isn't a way to hide the notebook bar in normal
  use (i.e. without using either postmessage or ui_defaults) while in
  compact mode (although there is a workaround to show it- switching
  into tabbed mode and then back!). It might be nice to have one.

Other considered solutions:
- We could add a new button that allowed you to reopen the menu if both
  menu and notebookbar were hidden
  - Not sure there's much benefit to this over just doing what we're
    doing here, and it's harder to implement
- We could disable the button to hide the menu bar when the notebookbar
  is collapsed
  - As far as I know, there's no button in the UI to show the notebook
    bar. This would make it impossible to hide the menu bar if the
    notebookbar was hidden via postmessage or ui_defaults

Signed-off-by: Skyler Grey <skyler.grey@collabora.com>
Change-Id: Ieab6d72a6be181aba88e9a5b21dda16a369b9e54

---
## [ty88k/rust](https://github.com/ty88k/rust)@[a660516334...](https://github.com/ty88k/rust/commit/a6605163346d7680502d8e2c1e5aaf1dc3229e41)
#### Thursday 2023-11-23 14:16:58 by Matthias Krüger

Rollup merge of #117596 - thomcc:core_macro_diag_items, r=Nilstrieb

Add diagnostic items for a few of core's builtin macros

Specifically, `env`, `option_env`, and `include`. There are a number of reasons why people might want to look at these in lints (For example, to ensure that things behave consistently, detect things that might make builds less reproducible, etc).

Concretely, in PL/Rust (well, `plrustc`) we have lints that forbid these (which I'd like to [add to clippy as restriction lints](https://rust-lang.zulipchat.com/#narrow/stream/257328-clippy/topic/Landing.20a.20flotilla.20of.20lints.3F) eventually), and `dylint` also has [lints that look for `env!`/`option_env!`](https://github.com/trailofbits/dylint/blob/109a07e9f27a9651ef33b6677ccaddd21466e97a/examples/general/env_cargo_path/src/lib.rs) (although perhaps not `include`), which would benefit from this.

My experience is that it's pretty annoying to (robustly) check uses of builtin macros without these IME, although that's perhaps just my own fault (e.g. I could be doing it wrong).

At `@Nilstrieb's` suggestion, I've added a comment that explains why these are here, even though they are not used in the compiler. This is mostly to discourage removal, although it's not a big deal if it happens (I'm certainly not suggesting the presence of these be in any way stable).

---

In theory this is a library PR (in that it's in library/core), but I'm going to roll compiler because the existence of this or not is much more likely something they care about rather than libs. Hopefully nobody objects to this.

r? compiler

---
## [OfficalDoritos/casey](https://github.com/OfficalDoritos/casey)@[3b722450c0...](https://github.com/OfficalDoritos/casey/commit/3b722450c06b6ddf056ff3bfcabc9ce4d8c9d0d4)
#### Thursday 2023-11-23 14:24:13 by Jay

The pits of hell await yet another target
man FUCK whoever wrote javascript this some doodoo ass shit wtfffffffff

---
## [weaveworks/tf-controller](https://github.com/weaveworks/tf-controller)@[c9e629b3da...](https://github.com/weaveworks/tf-controller/commit/c9e629b3da8dc72f725910b6d3f4ee9233fdff79)
#### Thursday 2023-11-23 14:52:24 by Balazs Nadasdi

fix: add unique hash to cloned source to avoid conflict.

Issue
-----

When more than one Terraform resource points to the same git repository,
when we clone the Source object, it does not create a new cloned Source
object as the PullRequest ID is the same, the source name is the same,
and we use only these two values to generate the name of the cloned
resource.

Solution
--------
Add a short and deterministic hash to the name of the cloned Source
object.

Another thoughts
----------------
It's not necessary to get a deterministic unique string, it could be
random as we save the result as SourceRef. I decided to use a short
(first 10 bytes of a sha256 hash), because if in the future we have to
regenerate the values somehow, then we don't have to care about
migration, extra compatibility checks. I know it's not likely we need
this, but generating a random number
- doesn't yield shorter code.
- still doesn't guarantee it will not generate a conflicting name, and
  knowing computers, I think it's even more likely (still unlikely) to
  generate the same random value if the two generation happens (nearly)
  at the same time.

Additional changes
------------------
- Removed the hardcoded index-magic from poll_test. For some reasons it was not
  always in order. I don't know what changed tho.

Notes
----
Compatibility:
I was thinking about what happens with old resources, but after I spent
some time on it, my conclusion is "they are not affected". We don't
calculate names when we look up source objects for terraform objects.
Their name is already saved as SourceRef. We generate this game only on
newly created resources, therefore it does not break anything already in
place.

Fixes #923

References:
- https://github.com/weaveworks/tf-controller/issues/923

Signed-off-by: Balazs Nadasdi <balazs@weave.works>

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[1a2ddececa...](https://github.com/sqnztb/Skyrat-tg/commit/1a2ddececa5cbc3b3aed161765eab4ebdda105c7)
#### Thursday 2023-11-23 15:13:11 by SkyratBot

[MIRROR] new space ruin, the biological research outpost [MDB IGNORE] (#24662)

* new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles

https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566

https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past

https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range

https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that

https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae

## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* new space ruin, the biological research outpost

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [SajmiMohammed/Luminar](https://github.com/SajmiMohammed/Luminar)@[f0b5e10d5b...](https://github.com/SajmiMohammed/Luminar/commit/f0b5e10d5b0b95b91d97614afb3f03b7e0749d23)
#### Thursday 2023-11-23 15:22:52 by SajmiMohammed

Add files via upload

Data Science endeavor : Sleep Disorder Analysis!

Key Features of the Dataset:
Comprehensive Sleep Metrics: Explore sleep duration, quality, and factors influencing sleep patterns.
Lifestyle Factors: Analyze physical activity levels, stress levels, and BMI categories.
Cardiovascular Health: Examine blood pressure and heart rate measurements.
Sleep Disorder Analysis: Identify the occurrence of sleep disorders such as Insomnia and Sleep Apnea.

Dataset Columns:
Person ID: An identifier for each individual.
Gender: The gender of the person (Male/Female).
Age: The age of the person in years.
Occupation: The occupation or profession of the person.
Sleep Duration (hours): The number of hours the person sleeps per day.
Quality of Sleep (scale: 1-10): A subjective rating of the quality of sleep, ranging from 1 to 10.
Physical Activity Level (minutes/day): The number of minutes the person engages in physical activity daily.
Stress Level (scale: 1-10): A subjective rating of the stress level experienced by the person, ranging from 1 to 10.
BMI Category: The BMI category of the person (e.g., Underweight, Normal, Overweight).
Blood Pressure (systolic/diastolic): The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.
Heart Rate (bpm): The resting heart rate of the person in beats per minute.
Daily Steps: The number of steps the person takes per day.
Sleep Disorder: The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).

Details about Sleep Disorder Column:
    None: The individual does not exhibit any specific sleep disorder.
    Insomnia: The individual experiences difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep.
    Sleep Apnea: The individual suffers from pauses in breathing during sleep, resulting in disrupted sleep patterns and potential health risks.

Dataset  link : https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset

---
## [starrm4nn/tgstation](https://github.com/starrm4nn/tgstation)@[bed92e193c...](https://github.com/starrm4nn/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Thursday 2023-11-23 16:16:19 by san7890

Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

---
## [starrm4nn/tgstation](https://github.com/starrm4nn/tgstation)@[5175ae0637...](https://github.com/starrm4nn/tgstation/commit/5175ae06374450b87324bb280c754e53880b7b16)
#### Thursday 2023-11-23 16:16:19 by John Willard

TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.


https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

---
## [jeffcragg/libgdx](https://github.com/jeffcragg/libgdx)@[e1d1fdc5fb...](https://github.com/jeffcragg/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Thursday 2023-11-23 16:25:58 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [morloc-project/morloc](https://github.com/morloc-project/morloc)@[abdee336b0...](https://github.com/morloc-project/morloc/commit/abdee336b03e7537ea10ad08dcf331935aa193cb)
#### Thursday 2023-11-23 16:49:37 by Zebulun Arendsee

Fix record type inference. Sort of.

The case study now works for real. Now stubs and the output looks grand.

My happiness is tempered by the dreadful mess in my typechecker. I need
to do a full rewrite of the typesystem.

First, I need to completely remove the default types in the
existentials. These defaults require baking *far* too much
language-specific detail into the compiler and they also make everything
very ugly. Instead, I should use the type aliases the user provides for
defaults.

Then I need to walk through the entire checker and check my math. I need
to formalize the front and back typechecker and the relations between
them. And how does packing fit in? Also, the eta-handling is hacky as
hell. After writing my paper, I may need to take some time to read up on
type theory and get back to formally describing the code.

Well, that is what I always say, isn't it? But I just get deeper in
debt. Sigh. Well, in reality, the next thing I do will probably be to
add typeclasses. But can I get that working on my messy foundation?

And I need to improve the generation of diagnostics.

---
## [chancancode/discourse](https://github.com/chancancode/discourse)@[42ef186aee...](https://github.com/chancancode/discourse/commit/42ef186aee6dab3951dba55fccab3c394d9d4b93)
#### Thursday 2023-11-23 17:02:16 by Godfrey Chan

Enable Embroider/Webpack code spliting for Wizard

* Move Wizard back into main app, remove Wizard addon
* Remove Wizard-related resolver or build hacks
* Add a `app/static` folder in the app, add it to `staticAppPaths`
* Install and enable `@embroider/router`
* Add "wizard" to `splitAtRoutes`

In a fully optimized Embroider app, route-based code splitting more
or less Just Work™ – install `@embroider/router`, subclass from it,
configure which routes you want to split and that's about it.

However, our app is not "fully optimized", by which I mean we are
not able to turn on all the `static*` flags.

In Embroider, "static" means "statically analyzable". Specifically
it means that all inter-dependencies between modules (files) are
explicitly expressed as `import`s, as opposed to `{{i18n ...}}`
magically means "look for the default export in app/helpers/i18n.js"
or something even more dynamic with the resolver.

Without turning on those flags, Embroider behaves conservatively,
slurps up all `app` files eagerly into the primary bundle/chunks.
So, while you _could_ turn on route-based code splitting, there
won't be much to split.

The commits leading up to this involves a bunch of refactors and
cleanups that 1) works perfectly fine in the classic build, 2) are
good and useful in their own right, but also 3) re-arranged thigns
such that most dependencies are now explicit.

With those in place, I was able to move all the wizard code into
the "app/static" folder. Embrodier does not eagerly pull things from
this folder into any bundle, unless something explicitly "asks" for
them via `imports`. Conversely, thigns from this folder are not
registered with the resolver and are not added to the `loader.js`
registry.

In conjunction with route-based code splitting, we now have the
ability to split out islands of on-demand functionalities from the
main app bundle.

When you split a route in Embroider, it automatically creates a
bundle/entrypoint with the relevant routes/templates/controllers
matching that route prefix. Anything they import will be added to
the bundle as well, assuming they are not alreay in the main app
bundle, which is where the "app/static" folder comes into play.

The "app/static" folder name is not special. It is configured in
ember-cli-build.js. Alternatively, we could have left everything
in their normal locations, and add more fine-grained paths to the
`staticAppPaths` array. I just thought it would be easy to manage
and scale, and less error-prone to do it this way.

Note that putting things in `app/static` does not guarentee that
it would not be part of the main app bundle. For example, if we
were to add an `import ... from "app/static/wizard/...";` in a
main bundle file (say, `app.js`), then that chunk of the module
graph would be pulled in. (Consider using `await import(...)`?)

Overtime, we can build better tooling (e.g. lint rules and babel
macros to make things less repetitive) as we expand the use of
this pattern, but this is a start.

---
## [Krashly/Ark-Station-13](https://github.com/Krashly/Ark-Station-13)@[248e30344b...](https://github.com/Krashly/Ark-Station-13/commit/248e30344b49f69cdbfbea62ed0d8f2853a70547)
#### Thursday 2023-11-23 17:05:10 by SkyratBot

[MIRROR] Makes Telekinesis + Russian Revolver Interaction more fair [MDB IGNORE] (#25042)

* Makes Telekinesis + Russian Revolver Interaction more fair (#79740)

## About The Pull Request

Fixes #77238

Basically, you were able to just spam kill people with the russian
revolver if you had telekinesis, which isn't really fair. Now, after
taking a leaflet out of the the discussion in that issue report, you can
still pull off the same party trick... once...

Basically, let's just say that when you focus on firing the gun in your
mind... you're also pointing it directly at your mind (your brain (your
skull (you instantly die))). This occurs even if the projectile doesn't
actually touch you (because that would be hellish to account for) but
you're the one who's playing russian roulette man

You still get to do some collateral damage because that's still a very
funny interaction but you only get to do it once per life. I don't know
if people will be happy to revive you after you "shoot" them. Also, the
way it's coded means that you can still leave the revolver on the table
and fire it at your foot or something, or just use it normally, as a
telekinesis user. This _only_ applies to distance-based firings.
## Why It's Good For The Game

The russian revolver is specifically coded to prevent you from damaging
other people, and this was a pretty silly way to sidestep that based on
the checks. Instead, let's make it so that you can still do this
admittedly funny interaction, but with enough reason to not do it (the
reason being that you'll always get fucking blatted).
## Changelog
:cl:
balance: After a string of unfortunate incidents, persons with
telekinesis have been strongly warned against playing Russian Roulette,
as they tend to hyperfixate on the gun a bit too much and end up firing
it directly at their head.
/:cl:

* Makes Telekinesis + Russian Revolver Interaction more fair

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Krashly/Ark-Station-13](https://github.com/Krashly/Ark-Station-13)@[5761091212...](https://github.com/Krashly/Ark-Station-13/commit/57610912121327266d1b5b47eb6d93bfb33d8362)
#### Thursday 2023-11-23 17:05:10 by SkyratBot

[MIRROR] Revert "if you die in a mech you are ejected" [MDB IGNORE] (#25051)

* Revert "if you die in a mech you are ejected" (#79768)

Reverts tgstation/tgstation#79380
this is literally what the mech removal tool is for. gameplay reasons
for that tool missing do not mean that we need to remove its use - if
you want a better solution then let people purchase it... or just smash
the mech- you saving their life and them being sad about their mech is
really funny
the original pr being marked as qol when that was a specific balance
change is very stupid

## Changelog
🆑
del: if you die in a mech you again don't automatically eject
/🆑

* Revert "if you die in a mech you are ejected"

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [jefft0/gno](https://github.com/jefft0/gno)@[24d89a4f5d...](https://github.com/jefft0/gno/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Thursday 2023-11-23 17:28:46 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[0141f96a13...](https://github.com/Time-Green/tgstation/commit/0141f96a1312dcf2326c28d73a7a91cefc8354c4)
#### Thursday 2023-11-23 17:30:46 by Ephemeralis

Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [xXPawnStarrXx/tgstation](https://github.com/xXPawnStarrXx/tgstation)@[68cd638330...](https://github.com/xXPawnStarrXx/tgstation/commit/68cd6383306e3f37d36cdc82113ada320b6e6365)
#### Thursday 2023-11-23 18:38:29 by Donglesplonge

swaps one of the fridges in snowcabin to be in line with the rest  (#79414)

## About The Pull Request

In truth, this is an IDED PR (this is not at all sarcasm, and as we all
know nobody would lie on the internet) that came about from a round i
just got done playing wherein i was in snowcabin trying to cook up some
food for fun, well wouldn't you know it i couldn't open one of the
fridges, what gives? well i got to thinkin it has to do with the fridge
type used, for some reason the fridge that holds the universal enzyme
uses the freezer/fridge/kitchen type instead of the fridge/open type
that the other two do, so i went ahead and just changed it off to the
other fridge types so now anyone can open it.

## Why It's Good For The Game

its a bit stupid to have a single fridge thats different from the rest
for no discernable reason, i can't think of any reason universal enzyme
would need to be guarded ever, you could just say "well why not go back
onto the station and grab some if the fridge is locked", well if for
some reason i'm barred from the station i want to be able to use as many
tools within my reach as possible preferably without many hoops, and
this ones unnecessary.

## Changelog

fix: changes the type of fridge used to hold the universal enzyme in the
snowcabin gateway's kitchen, letting everyone access it like the rest of
the fridges.

/:cl:

---
## [jongan69/cinemaswipe](https://github.com/jongan69/cinemaswipe)@[f58cf42efd...](https://github.com/jongan69/cinemaswipe/commit/f58cf42efd197d4f3e9c4e5bc974a8117bdac41c)
#### Thursday 2023-11-23 18:58:44 by jongan69

Last one for the day, can stand the ai api key bullshit who the fuck cares fuck your key its not that cool

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[7fce8cd805...](https://github.com/Jolly-66/tgstation/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Thursday 2023-11-23 19:33:26 by san7890

Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[2562f0997a...](https://github.com/Jolly-66/tgstation/commit/2562f0997a73a52c4ada51c7e0d9996fea4ee573)
#### Thursday 2023-11-23 19:33:26 by MrMelbert

Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished (#79694)

## About The Pull Request

Related: #78017 

Stop drop and roll is no longer instant -5 fire stacks -> stun -> wait. 

Now, when you stop drop and roll, every time you roll you will lose 1
firestack.

A roll is triggered every 0.8 seconds. Moving, getting up, or becoming
incapacitated / stunned will stop you from rolling.
_(This number puts it roughly equivalent to its current rate.)_

While rolling, your hands are blocked (you cannot use items, hold
things, etc.)
Additionally, you will roll until all firestacks are cleared. 

## Why It's Good For The Game

Getting stunned for 6 seconds because you decide to stop and roll is a
little silly. Reasonably you could stop rolling and get back up should
the need arise, such as "oh god there's more fire I gotta relocate".

By changing it to a gradual thing, it makes it a bit more reasonable and
fair.
- New players who immediately slam "STOP DROP ROLL" because the alert on
their screen tells them to are no longer helpless for 6 whole seconds
- People who hit the resist key, intending to interact with something
else (such as a bola) are no longer stuck rolling when they did not want
to

## Changelog

:cl: Melbert
balance: Stop, drop, and roll no longer instantly clears 5 fire stacks
off of you - Instead, it will clear 1 fire stack off of you every time
you roll, with a roll every 0.8 seconds.
balance: Stop, drop, and roll no longer stuns you for 6 seconds.
Instead, it will knock you to the floor while you are rolling. Moving
around or getting up will cancel the roll, and you cannot use items
while rolling around.
balance: Stop, drop, and roll will now repeat until the fire is put out
or you get up.
/:cl:

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[742971675d...](https://github.com/Jolly-66/tgstation/commit/742971675de266aa4ebe671dc5175a5c543d93d7)
#### Thursday 2023-11-23 19:33:26 by san7890

Fixes Relay Attackers Misfire (#79731)

## About The Pull Request

Fixes #76079

Basically we were both not getting all of the args that we recieve from
`COMSIG_ITEM_AFTERATTACK` which included the very important
`proximity_flag` which tells us if the person was in range to actually
hurt us or not. This means that clicking a mob with this element with a
stack of metal from across the room would cause them to aggro, which
makes no sense whatsoever. Let's actually use that proximity check.

We listen for projectiles hitting us separately, don't worry.
## Why It's Good For The Game

It just makes no damn sense, fixes some weird ass behavior. 
## Changelog
:cl:
fix: Bar Bots (and several other mobs) will no longer aggro on you if
you click on them with a "forceful" item from halfway across the room.
/:cl:

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[2532911353...](https://github.com/Jolly-66/tgstation/commit/2532911353d63661b735004f2895103d45858b50)
#### Thursday 2023-11-23 19:37:24 by LemonInTheDark

Adds pathmaps, refactors pathfinding a bit (#78684)

## About The Pull Request

Implements /datum/pathfind/sssp, which generates /datum/path_map

/datum/path_maps allow us to very efficently generate paths to any turf
they contain from their central point.

We're effectively running the single source shortest paths algorithm.
We expand from the center turf, adding turfs as they're found, and then
processing them in order of addition.
As we go, we remember what turf "found" us first. Reversing this chain
gives us the shortest possible path from the center turf to any turf in
its range (or the inverse).

This isn't all that useful on its own, outside of a few niche cases
(Like if we wanted to get the farthest reachable turf from the center)
but if we could reuse the map more then once, we'd be able to swarm
to/from a point very easily.

Reuse is a bit troublesome, reqiures a timeout system and a way to
compare different movables trying to get paths.
I've implemented it tho. I've refactored CanAStarPass to take a datum,
/datum/can_pass_info. This is built from a movable and a list of access,
and copies all the properties that would impact pathfinding over onto
itself.

There is one case where we don't do this, pathing over openspace
requires checking if we'd fall through the openspace, and the proc for
that takes an atom.
So instead we use the weakref to the owner that we hold onto, and hold
copies of all the values that would impact the check on the datum.

When someone requests a swarmed path their pass info is compared with
the pass info of all other path_maps centered on their target turf. If
it matches and their requested timeout isn't too short, we just reuse
the map.

Timeout is a tricky thing because the longer a map exists the more out
of date it gets.
I've added a few age defines that let you modulate your level of risk
here. We default to only allowing maps that are currently
being generated, or finished generating in our tick. 
Hopefully this prevents falling into trouble, but consumers will need to
allow "failed" movements.

As a part of this datumized pass info, I've refactored pathfinding to
use access lists, rather then id cards directly. This also avoids some
dumbass harddel oppertunities, and prevents an idcard from changing mid
path.

Did a few things to the zPass procs, they took args that they did NOT
need, and I thought it'd be better to yeet em.

If you'd all like I could undo the caching/can_pass_info stuff if you'd
all like. I think it's useful generally because it avoids stuff changing
mid pathfind attempt, but if it's too clunky I could nuke it.

Oh also I added optional args to jps that constricts how it handles
diagonals. I've used this to fix bot paths.

## Why It's Good For The Game

Much of this is redundant currently. I'm adding it because it could have
saved hugglebippers, and because I get the feeling it'll be useful for
"grouping" mobs like bees and such.
We're doing more basic mob work currently and I want to provide extra
tools for that work.


https://github.com/tgstation/tgstation/assets/58055496/66aca1f9-c6e7-4173-9c38-c40516d6d853

## Changelog
🆑
add: Adds swarmed pathfinding, trading accuracy for potential
optimization of used correctly
fix: Bots will no longer take diagonal paths, preventing weirdo looking
path visuals
refactor: Refactored bits of pathfinding code, hopefully easier to add
new pathfinding strategies now
/🆑

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[b77fa8c2a2...](https://github.com/Jolly-66/tgstation/commit/b77fa8c2a2490b43bf9174271ebfad72c4782d98)
#### Thursday 2023-11-23 19:37:24 by LemonInTheDark

Starlight Control (Aurora works now, space gas doesn't touch starlight, narsie ending effects) (#78877)

## About The Pull Request

[Implements a setter for starlight
variables](https://github.com/tgstation/tgstation/commit/af34f06b418b039b2ead90b29112b30adea4bc68)

I want to start to modify starlight more, and that means I need a way to
hook into everything that uses it and update it, so we can modify it on
the fly.

This does that, alongside removing space overlays from nearspace (too
many false positives) and making the aurora modify all turfs projecting
starlight, rather then all turfs in an area.

Do still need to figure out handling for the starlight color usage in
turf underlays tho (I gave up, we just keep it static. I'll fix it
someday but the render_relay strategy just doesn't work with its masking
setup)

[Reworks how starlight overlays
work](https://github.com/tgstation/tgstation/commit/9da4bc38e223e0ce2d91b0c8beddf1ebba968b9c)

Instead of setting color on the overlays directly, we instead store an
object with our current settings in every mob's screen, and
render_target it down onto our overlays.

This lets us update overlay colors VERY trivially. Just need to set
color on the overlay var. Makes modifying starlight a lot cheaper.

It doesn't work on area overlays, because suffering, and it MIGHT induce
extra cost on clients. if it does we can do something about that, we'll
play it by ear

[Removes parallax starlight
coloring.](https://github.com/tgstation/tgstation/commit/5f701a1b137c7d4c333929e4cbfdd9d4aa8656d6)

I'm sorta iffy on the color, the effect can be real oppressive in some
cases, and I'd like to use starlight color for more events in world, and
having it vary can make that looking nice hard.

[Adds some visual effects to narsie being
summoned](https://github.com/tgstation/tgstation/pull/78877/commits/a423cfcb2ba9c0d729b06c36dd7d38ff68c967c2)

As the rune drawing progresses space (starlight and parallax) go from
normal to greyscale. Then, right about when narsie shows up, starlight
becomes vibrant red.

It's a nice effect. I wanna do more shit like this, I think it'll
improve vibes significantly.
## Why It's Good For The Game

Can't embed it because of github's upload limit, can show a
[link](https://cdn.discordapp.com/attachments/458452245256601615/1160821856358645860/2023-10-08_22-31-22.mp4?ex=65360e99&is=65239999&hm=680e33e4e0026b89e132afc50c04a648a24f869eb662f274a381a5de5c5a36f2&)
for the narsie stuff

Here's
[one](https://cdn.discordapp.com/attachments/326831214667235328/1160813747196141568/2023-10-08_22-34-10.mp4?ex=6536070c&is=6523920c&hm=f8d571d1013da89887f49f3fec99f632251eeeac83085aa7dde97009aee3922f&)
for the aurora too.

This gives us more pretty starlight shit, and the ABILITY to do more
pretty starlight shit. I'm pretty jazzed, and I hope people use this
proc more (keeping in mind that it's pretty hard on the lighting system,
and needs significant delay between changes)
## Changelog

🆑
add: Narsie summoning has had some effects added to space and starlight
del: Removes the link between spacegas color and starlight. It was a
slight bit too vibrant and I think impacted the vibe too wildly to be
incidental.
fix: The aurora event actually... works now. Space lights up and all
that
/🆑

---
## [AnuravModak/pennylane](https://github.com/AnuravModak/pennylane)@[47e74e16d0...](https://github.com/AnuravModak/pennylane/commit/47e74e16d0fb27aedc5ffab69aefaf5188115038)
#### Thursday 2023-11-23 20:50:54 by Matthew Silverman

simplify state reordering logic (#4817)

**Context:**
I wrote the same function twice, differing only by state flattening, to
get the DQ upgrade done. It's starting to cause trouble.

**Description of the Change:**
Greatly simplified the state re-arrangement logic. There used to be a
whole mess of things happening, but now things are much more
straightforward.
1. `simulate` first puts things in our "standard" order, and this means
that if any measured wires are not also operator wires, they are put to
the _end_ of our tape wires. Therefore, for each measured-only wire, we
just have to stack a `zeros_like(state)` to the last axis of our final
state! `simulate` never tried to transpose wires back to a different
ordering, so that was always wasted work.
2. `StateMP.process_state` _always_ receives the full state, and never
needed to pad. No other device has done this optimization (the function
used to literally just `return state` before DQ2 migration), and
`simulate` already ensures that the final state has all wires in it -
they just might be out of order. The only thing we might need from
`process_state` is a transposition to the correct wire order. The
inputted `wire_order` _should_ always be `range(len(wires))`, but
whatever, we don't need to assume that.

I'll paint a picture for a normal scenario:

```python
@qml.qnode(qml.device("default.qubit", wires=3))
def circuit(x):
    qml.RX(x, 0)
    qml.CNOT([0, 2])
    return qml.state()
```

What happens with this QNode?
1. Device preprocessing sticks the device wires (`[0, 1, 2]`) onto the
`StateMP`
2. `simulate` maps the wires to our standard order. I'll demonstrate
(with `probs` so I can specify wires):

```pycon
>>> qs = qml.tape.QuantumScript([qml.RX(1.1, 0), qml.CNOT([0, 2])], [qml.probs(wires=[0, 1, 2])])
>>> qs.map_to_standard_wires().circuit
[RX(1.1, wires=[0]), CNOT(wires=[0, 1]), probs(wires=[0, 2, 1])]
```

3. Operate on the 2-qubit state, then stack another `[[0, 0], [0, 0]]`
on the end of it (wire "1")
4. `StateMP(wires=[0, 1, 2]).process_state(state, wire_order=[0, 2, 1])`
transposes the result to the correct order

I also changed the torch tests to stop using a deprecated setter for
default float types.

**Benefits:**
Duplicate code is cleaned up, existing code is simplified, no
unnecessary call to transpose.

**Possible Drawbacks:**
- Have to call `qml.math.stack` for every wire that was not operated on.
Hopefully this is usually not a lot, and it's not that costly anyway
- functions now do less than they used to (I see this as a perk - they
now do _exactly_ what they're supposed to)

---
## [yvanzo/musicbrainz-server](https://github.com/yvanzo/musicbrainz-server)@[41b5efc95c...](https://github.com/yvanzo/musicbrainz-server/commit/41b5efc95c13ee269e436a9864744de6d81bf7ca)
#### Thursday 2023-11-23 20:51:19 by Michael Wiencek

MBS-13310: Add new empty artist credits to unreferenced_row_log (#3105)

When artists are merged, `Data::ArtistCredit::merge_artists` is called, which
inserts new artist credits: each appearance of the old artist is replaced by
the new one.  If the old AC had no references, it will have had an entry in the
`unreferenced_row_log` table already; we should make sure to update that to
point to the new AC, if the new one also has no references.

Remember that because artist credits have MBIDs, we'd like to preserve them
from deletion where possible: there's a 2-day delay before we cleanup empty
ACs, allowing time for them to be re-used with their original MBIDs intact.
This applies to redirected MBIDs too; so while inserting empty artist credits
may seem silly, these empty ACs are in fact redirected to from a (now-deleted)
empty AC which hadn't been cleaned up yet.

---
## [rfbergeron/bompiler](https://github.com/rfbergeron/bompiler)@[a2d94e26c6...](https://github.com/rfbergeron/bompiler/commit/a2d94e26c67672d1f3c08a613371e2a8786aac0c)
#### Thursday 2023-11-23 21:28:56 by Robert

Integrating the new type system into the compiler requires far too many
changes for them to be comprehensively documented in a single message
and lead me to discover some bugs and other rough edges that I had to
smooth out to make the process easier. I have tried to document as many
as possible in this list.

- Add more functions which allow you to query information about types.
- Indicate whether or not a function type was declared in the old style
  in the function's type rather than in its symbol.
- Add function which takes a types information and turns it into a
  regular form so that, for example, all integers have the same
  representation regardless of which specifiers were used to declare the
  type. For example, after being normalized, `long`, `signed long`,
  `long int`, and `signed long int` all look the same to the compiler.
- Store function parameter type info instead of symbols. Symbols are not
  necessary for semantic analysis of parameters. The type of the symbol
  is good enough.
- Check the types of scalar initializers. This wasn't being done and I
  only noticed because of an unrelated bug. The code for initializers
  should really be cleaned up so that I don't miss something like this
  again.
- Changed how errors are represented. This was necessary because of the
  changes to the type system, which is responsible for propogating
  errors. Arrays are used to hold multiple errors, instead of the badlib
  linked list, which was clunky and bad.
- Emit syntax tree nodes for automatic pointer conversions. This was
  done to make determining when a node's type information should be
  freed easier.
- Perform pointer conversions in parser rules, rather than inside the
  functions invoked by the parser rules. This improves code readability
  at the expense of making parser rules more verbose.
- Improve how the `va_list` builtin is handled. The only information
  exposed outside of the parser is the type of the builtin after it has
  been subjected to pointer conversions. The name of the struct now also
  has a `__builtin_` prefix so that it is not mistaken for other unique
  names and no checks need to be made to ensure that we do not
  free/double free it.
- Get rid of attributes.h and attributes.c. These files accumulated a
  bunch of disparate stuff and was basically utils.h by another name.
  Contents moved to lyutils, astree, strset, and symtable.
  `MAX_IDENT_LEN` is defined in multiple places with a macro, but oh
  well.
- Move parser-specific functions into their own file, parser.c, which is
  included at the end of the bison input file. This allows ccls to do
  its thing and is also, in my opinion, a little cleaner.
- The make ci directive now checks that the code has been formatted
  instead of formatting it automatically. This is just personal
  preference.
- Remove `-Wno-unused` from compilation options. Unused parameters
  either removed or cast to void at the top of the function. Most unused
  parameters should be placeholders in case I ever decide to start using
  `snprintf`.
- Switch from `-Og` to `-O0` compiler option. `-Og` still sometimes
  optimizes variables away, which makes debugging harder.
- Fix a longstanding bug in debug that resulting in the '@' flag not
  being handled correctly. Not sure how I never caught that one before.
- Fix bug in `translate_va_arg` which set the `first_instr` member
  incorrectly, resulting in instructions being emitted in the incorrect
  order.
- Fix application of qualifiers and storage class specifiers when a type
  id specifier is used. Qualifiers are applied to the outermost
  declarator if it is a pointer; otherwise, qualifiers and storage class
  specifiers are applied to the "root" type (a base type, struct, union,
  or enum)
- Make more functions static

---
## [Profakos/orbstation](https://github.com/Profakos/orbstation)@[c63b233f42...](https://github.com/Profakos/orbstation/commit/c63b233f42a46d9373fd41b3f69edde3d2d48002)
#### Thursday 2023-11-23 22:35:00 by _0Steven

Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

---
## [Profakos/orbstation](https://github.com/Profakos/orbstation)@[492ed90f28...](https://github.com/Profakos/orbstation/commit/492ed90f28dfd213e9438509653727f788efcebd)
#### Thursday 2023-11-23 22:35:00 by necromanceranne

Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs. 

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

---
## [MichaelHinrichs/SPORE-Creatures-extract](https://github.com/MichaelHinrichs/SPORE-Creatures-extract)@[89a93afa81...](https://github.com/MichaelHinrichs/SPORE-Creatures-extract/commit/89a93afa81df0b02fd6c22a5472b879d7822f8d1)
#### Thursday 2023-11-23 22:57:04 by NintenHero

FUCK YOU!

Apparently checking the build for Windows just DOES'NT WORK!
https://steveellwoodnlc.medium.com/ci-for-open-source-dotnet-13d15a770fe9

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[d3f79b6612...](https://github.com/effigy-se/effigy-se/commit/d3f79b6612ee31503bae890c460c54ca2f5252dc)
#### Thursday 2023-11-23 23:16:35 by san7890

Puts all traits in the globalvars file + CI Testing (#79642)

## About The Pull Request

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-

![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit
## Why It's Good For The Game

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)
## Changelog

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).
# Conflicts:
#	tgstation.dme

---
## [zungusonz/-27630236059-BLACK-MAGIC-LOVE-SPELLS-IN-ALBERTON-BENONI-SPRINGS-BOKSBUR-BEDFORDVIW-PRETORIA](https://github.com/zungusonz/-27630236059-BLACK-MAGIC-LOVE-SPELLS-IN-ALBERTON-BENONI-SPRINGS-BOKSBUR-BEDFORDVIW-PRETORIA)@[c35dc2f068...](https://github.com/zungusonz/-27630236059-BLACK-MAGIC-LOVE-SPELLS-IN-ALBERTON-BENONI-SPRINGS-BOKSBUR-BEDFORDVIW-PRETORIA/commit/c35dc2f06863135619c198a48a6c64cf46d2320f)
#### Thursday 2023-11-23 23:32:21 by zungusonz

Create README.md love spell


+27630236059 INSTANT LOVE SPELL CASTER IN ALBERTON௵+̳2̳7̳630236059 ALBERTON, MONTANA, TOKYO, SEOUL, SINGAPORE.._ MAGIC RING FOR LOVE IN COSMOS CITY, CENTURION, DURBAN, OSLO, WELLINGTON, NEPAL, SOSHANGUVE, GA RANKUWA, KWAMHLANGA @(FORTUNE Teller OBSESSION SPELL CASTER IN DIEPSLOOT, JOHANNESBURG, LOTUS GARDENS, PRETORIA NORTH. EMAIL;papandmamazungu@gmail.com
Dr. Zungu a Traditional Spiritual healing has been more or less for ages and it has given most loyal clients well-to-do happiness in interchange problems and you may habit it too. As a healer I use a variety of roots, bark, herbs, flowers, and supplementary products gone making my expected medicines. Most of my treatments are focused on the imbalances in your body. If the source of the ailment is the primary concern, consequently back come up with the money for the right herbs. Mama ZUNGU Real Love Spells That Work Berlin, +27630236059  Marriage spells Bangkok, Thailand Obsession spell, Attraction spell, Crush spell, Win the lottery spell Hawaii Voodoo lost love spells to bring back a lost lover In Amsterdam, black magic love spells caster in Paris, spell to bring lost lover back, Gay Love Spells that Work, Spiritual Love Spells, Powerful Psychic Love Spells that work, Marriage love spell casting in Canberra, Witchcraft Love spells Specialist, Break them up spell,+ 27630236059 Best Traditional Spiritual Healer in Cairo, Sangoma with trusted Spells in Gauteng, Worlds Top lost love spell caster, couple break up spells Maryland, black or white magic love spells, marriage love spells, Powerful Traditional Healer in Cape Town, Love spells caster in Victoria, Voodoo love marriage spells Melbourne, bring back lost lover spell in Wellington, Herbalist Sangoma and spiritual Marriage consultant in Polokwane, powerful love spell London, revenge of the raven curse, Mama ZUNGU break up spells, do love spells work, magic spells, protection spell, curse removal Spell, Wicca witchcraft to remove negative energy, removing curse spells, spiritual cleansing, African witchcraft healer. AUTHENTIC LOST LOVE SPELL CASTER DOHA, +27630236059  Real Magic Court Case Spells Lansing, Michigan Overnight Revenge Death spells To Kill Your Ex Instantly London, Love Spells Caster in Maryland, real black magic spells that work, African traditional healer, guaranteed black magic love spells Juba, Instant Black Magic Spells To Kill Someone, powerful white magic spell casters in Amsterdam, witchcraft money spells, Lesbian Attraction love spells in Boston, Powerful Magic Love Spells , powerful binding spell to cement your true love forever, gambling spells, fertility spells caster. , revenge spells, voodoo death spells that work overnight, Candle Spells to Bring Back Lost Love, Business Growth Spells, online powerful voodoo spell caster Cuba, Genuine Love Spells in Georgia, Psychic Reading in NEW YORK, Easy candle spells to win court cases, Spells and Rituals To Help Win Your Court Case, Hoodoo Spells To Get Justice and Help You Win In Court, Court cases magic spells, Court Case Ritual, justice spells to get released from jail/prison, Spell Magic To Get Charges Dropped, Legal Spells To Get Rid Of Legal Problems, Discipline someone with voodoo revenge spells, Get rid of enemies & regain confidence using voodoo revenge spells, EFFECTIVE COURT CASE RITUAL SPELL, POWERFUL SPELL TO KEEP YOU OUT OF CRIMES AND PRISON +27630236059, candle witchcraft Potomac Manors, lost love potion spell Hammersmith London, real love spells in Texas, spells to bring back a lover Forest Hill North Toronto Ontario, TOP LOVE SPELL BRANT, TOP LOVE SPELL FOREST HILL TORONTO, do love spells actually work Overland Park Kansas, love spells that work fast Olathe Kansas, self love candle West Mount West Vancouver British Columbia, voodoo spell caster in Vancouver British Columbia, BEST PSYCHIC NEAR ME TORONTO , bay leaf love spell City Of Westminster, honey spell jar in Glencoe Illinois, miss me spell in Napa California, spell to get ex back San Jose California, PSYCHIC READINGS IN TORONTO , cast a love spell online in Frisco Texas, love potion wicca Frisco Texas, real spell casters in Brewer Subdivision Hillsborough Ca, spells to get your ex back in Los Altos California, TOP LOVE SPELL IN BRIDLE PATH, TOP LOVE SPELL in ROSEDALE, do love spells really work in Bridgeport Ct, love spells that work immediately Larchmont Ny, self love spell jar in Central Park South, white magic love spells in Washington Dc, BEST TOP LOVE SPELLS CASTER IN KINGSTON. best love spells Bridle Path Toronto Ontario, instant love spell Frisco Texas, most powerful love spell Frisco Texas, spell to get him back in McKinney Texas, SIMPLE LOVE SPELLS MARKHAM , cast a spell online in Forest Hill South & UCC Toronto Ontario, Love spell Atherton, real voodoo spell Pearland Texas, spells to make him come back Maidenhead, TOP LOVE SPELL CALGARY, TOP LOVE SPELLS IN TORONTO , +27630236059  How do love spells work Los Altos Hills CA, love spells that work instantly Old
Greenwich Ct, self love spell Rumson Nj, wiccan love spells Billionaires Row New York, BRING BACK LOST LOVER LOVE SPELLS FAST IN Kavieng , best spell caster Chalfont Saint Giles London, lemon break up spell Santa Cruz California, new moon love spell Markham Ontario, spell to get my ex back in Frisco Texas, easy love spells Bronxville New York, love spells that work overnight South Lake Texas, simple love spells Central Park Tower, witch love spell Stanford University, EXCELLENT ASTROLOGER in MADRID, break a love spell in King George Park Westmount Montreal Quebec, lost love spells in London, obsession love spell Crestline Heights Mountain Brook Al, spell to get rid of someone Roxboro Calgary Alberta, EASY LOVE SPELLS MARKHAM, TOP BEST LOVE SPELLS IN ROME come back to me spell English Village Mountain Brook Al, love spell jar Cherry Hills Village Colorado, red candle love spell West Menlo Park Atherton Town Ca, spells to make someone love you Palm Beach Florida, TOP LOVE SPELL ONTARIO, TOP PSYCHIC HEALER NEAR ME TORONTO +27630236059  ex back spell Frisco Texas, love spells to get your ex back London, soul binding spells Frisco Texas, lust spell Manhattan New York, FORE MOST PSYCHIC LOVE READINGS IN Wellington, break up spell Short Hills New Jersey, love attraction spell Urban Honolulu HI, pink candle love spell in South ills Millburn Town ship NJ, spell to keep someone away Bellevue Washington, GET BACK EX LOVER IMMEDIATELY TORONTO, TOP BEST PSYCHIC IN TORONTO, come to me candle love spell in Texas, spells voodoo in Scarsdale NY., BEST ASTROLOGER IN FLORIDA. Powerful love spell Mama ZUNGU +27630236059 Revenge of the raven curse. Break up spells. Magic spells. Protection spell. Curse removal. Remove negative energy. Curse spells. Spiritual cleansing. Africa witch craft healers. Hex removal. Spiritual healing spell. Wicca witchcraft. Good luck charm. Break up spells. Magic love spells Sangoma traditional medicine. Gay love spell. Real magic spells. The spell to defeat your rival. Fertility spells. Divorce spell. Marriage spells. Native healer. Fortune teller. Madness caused by witchcraft. Break Up & Come Back To Me Get your ex back, even if they are currently with another lover. They will break up and he or she will come back to you, to be in your loving arms, the way it should have been all along. Break them up and bring back your lost love with The Break Up and Come Back To Me Love Spell . Binding Love Spells Meant for more serious relationships like marriage, or the path to something very special and permanent. Once the binding love spell is cast, it is extremely difficult to reverse. It is highly recommended that you ensure you are choosing the right person for yourself before asking us to cast The Binding Love Spell . Stop Divorce Are you going through a divorce you just dont want? Still feel strong love towards your husband or wife and they no longer feel the same way? If its not about the legal fees, division of personal property, the countless arguments, or nights on the couch. Stop a divorce with The Stop a Divorce Love Spell, PLEASE NOTE THAT MY SPELLS ARE BASED ON AFRICAN TRADITIONAL HEALING AND A BELIEF IN THE MYSTICAL. RESULTS VARY FROM INDIVIDUAL TO INDIVIDUAL. Have a serious problem that needs fixing? +27630236059  Rustenburg, Brits, Makanda, Mafikeng, Zeerust, Vryburg, Ventersdorp, Nelspruit, Secunda, Witbank, Middelburg, Pongola, Piet Retief, Malelane, Evander, Kinrose, WITBANK Kriel, Carolina, Bethal, Ermelo, Naas, , Hazyview, Hendrina, Bushbuckridge, Belfast, Polokwane, Mokopane, Northam, Thohoyandou, Louis Trichardt, Musina, Entabeni, Ladybrand, Ficksburg, Kroonstad, Klerksdorp, Odendaalsrus, Vereeniging, Sasolburg, Carletonville, Westonaria, Parys, Kimberly, Kuruman Grahamstown, Queenstown, East London, Bloemfontein, Welkom, Polokwane, Musina, Maseru, Gaborone, Manzini, Nairobi. We perform this come-to-me love spell that works instantly with the aim of bringing back the victim to the person performing the magic. Have you lost your lover? Do u need to solve any relationship problem? Contact the powerful spells caster with love spells that work overnight and love spells that really work. Have you found yourself infatuated with a special someone you think could be the one? Are you looking for a spell to provide them with a nudge in the right direction? Or maybe the spell you cast didnt achieve the results you were hoping for?
CALL/WHATSAPP; +27630236059
EMAIL; papandmamazungu@gmail.com

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[6d5aa5121e...](https://github.com/effigy-se/effigy-se/commit/6d5aa5121eb08bec19d3d5413f45a216af8a2c1e)
#### Thursday 2023-11-23 23:48:42 by san7890

Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

---
## [AtomBlade/Lost-Era-Modpack](https://github.com/AtomBlade/Lost-Era-Modpack)@[300d72c910...](https://github.com/AtomBlade/Lost-Era-Modpack/commit/300d72c9100474130a177c853b3bf9aef4d0eefa)
#### Thursday 2023-11-23 23:54:04 by TechnoParadox

v1.5.3

-The modpack will check for the user RAM before launch
-Waystones work interdimensionally (includes scrolls)
-Re-enabled thaumcraft 4 metal transmutations
-Disabled Wizardry's Disarmament spells on players
-Disabled unnecessary update checkers
-Reduced the deafening from Waystones by 60%
-Increased visibility while under the night sky
-Gardens are now spreadable but only drop seeds
-Buffed weak food value of some foods
-Hunger is now easier on lower difficulties
-Healing no longer consumes hunger
-GT4 Ores now have tooltips indicating where these are found
-Completely reworked Project Red pipes into Thaumcraft 4 including Thaumonomicon entries
-Added TC4 aspects for dozens of mobs and blocks
-Added dozens of entries to TC4 Crop and meat duplication
-NEI item visibility now handled by INPure
-Nerfed Mek's wind generation at higher altitude but buffed at lower ones
-Buffed Mek's Energy Storage multiblock
-Rework energy consumption of every Mek Machine (mostly lower consumption)
-Minechem can now decompose farmable materials
-Totem of Undying can now be found as loot
-Whitestone is now made from Totem of Undying
-Volcanos are now made of obsidian
-Reduced Grow Light consumption
-Fixed potential Potion ID conflicts
-Fixed Bees spawning harmful flora
-Buffed GT4 ore distribution in specific scenarios
-Fixed GT4 ore generation in the Nether
-Reworked Extra TiC compatibility
-Buffed weak fuels for the Compression and Energizing Dynamos
-Metallurgy metal and Tinker Metals now share the same stats
-Buffed Gas and RF capacity of Compact Machines
-Blacklisted XP Phial from Loonium
-Phantom Hands have a running cost of 10 LP
-Reworked Dagger of Sacrifice and Sacrificial Dagger
-Every instance of Ghast and Blaze now shed their items overtime
-Blaze Lamp cannot be used as furnace fuels anymore as a result of the above
-Soul Campfire no longer can be automated with hoppers
-Buffed TC4 Magic Biomes occurrences
-Disabled Ender Collector (unfixable dupe)
-Disabled Ender Dragon Girl
-Disabled Magnetic Force
-Disabled AE2 quartz tools
-Buffed Ars Magica 2 recipes
-Fixed End Crystal exploit
-Food records no longer persist through death
-Added missing recipes for AE2 Cards
-Extra TiC's Mana Steel parts are obtained by throwing iron parts in a mana pool
-Extra TiC's Thaumium parts are obtained by throwing iron parts in a cauldron with Praecantatio
-Extra TiC's magic materials can no longer be crafted in the Tool Table
-Added Smeltery integration to Extra TiC's magic materials
-Cheaper QED
-Snails are no longer fishes
-Wild Barley has been nerfed to be worst than barley (still grows 3x faster)
-Salt is now created by cooking water buckets
-Additional foods from the drying rack
-Cheaper Safari nets and Porta Spawners
-You can now empty Nuclearcraft capsules
-Remove the necessity of plates in the RF technological tree
-Removed needlesss microcrafting form Steve's Carts

---

