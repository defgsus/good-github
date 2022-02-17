## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-16](docs/good-messages/2022/2022-02-16.md)


1,777,453 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,777,453 were push events containing 2,882,923 commit messages that amount to 210,996,623 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [wraith-54321/fulpstation](https://github.com/wraith-54321/fulpstation)@[b59f03e592...](https://github.com/wraith-54321/fulpstation/commit/b59f03e592ce72f069760eba0f9eb30eeacd16c1)
#### Wednesday 2022-02-16 00:32:09 by John Willard

Deputy update (#428)

* deputy berets cant be knocked off, deputies get tablets, service deputy beret buff.

* fuck you

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[8f32cbe38d...](https://github.com/timothymtorres/tgstation/commit/8f32cbe38d956e06c919be36386da76befb0555b)
#### Wednesday 2022-02-16 00:46:45 by LemonInTheDark

Reworks janitor cyborg cleaning, focus on the slipping (#64131)

Alt of #64105 and #64126 (I'm sorry Novva, I should have said something earlier)
I main janitor. As a janitor main, my greatest joy in life is slipping people who ignore my signs

I've seen some people complain about janitor borgs, so I decided to look into em

Unfortunately, not only is the janitor borg just a straight upgrade to janitors, it has absolutely no reason to use most of its kit
We give it standard cleaning supplies, and hell even bespoke tools to deal with leaving slippery tiles everywhere, but we also just let them clean anything they can walk over

This seems a bit too much to me, even for borgs. Also it's like, really boring

So what if we made their movement based cleaning cost something? How about we make it suck water from their bucket. Use the same pattern as mop code, make it twice as expensive though. Give it a slowdown, some sound cues, and an action button to trigger it all

---
## [Toastgoats/tgstation](https://github.com/Toastgoats/tgstation)@[7bead07444...](https://github.com/Toastgoats/tgstation/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Wednesday 2022-02-16 01:04:49 by John Willard

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
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[b710cb1d57...](https://github.com/zx2c4/linux-rng/commit/b710cb1d5715e5bc3652930dfe6a196d5353df93)
#### Wednesday 2022-02-16 01:40:04 by Jason A. Donenfeld

random: use linear max-period irq extractor

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As a permutation of only two
rounds, there are some easily searchable differential trails in it, and
as a means of preventing malicious irqs, it completely fails, since it
xors new data into the entire state every time. It can't really be
analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in this
context, in case a malicious irq compromises a per-cpu fast pool within
the 64 interrupts / 1 second window, and then inside of that same window
somehow can control its return address and cycle counter, even if that's
a bit far fetched. However with a very CPU-limited budget, actually
doing that remains an active research project (and perhaps there'll be
something useful for Linux to come out of it). And while the abundance
of caution would be nice, this isn't *currently* the security model, and
we don't yet have a fast enough solution to make it our security model.
Plus there's not exactly a pressing need to do that. (And for the
avoidance of doubt, the actual cluster of 64 accumulated irqs still gets
dumped into our cryptographically secure input pool.)

So, for now we are going to stick with the existing irq security model,
which assumes that each cluster of 64 irq cycle counter samples are
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions. However, when
considering this for our four-word accumulation, versus NT's one-word,
we run into potential problems because the words don't contribute to
each other, and some may well be fixed, which means we'd need something
to schedule on top. And more importantly, our distribution is not
2-monotone like NT's, because in addition to the cycle counter, we also
include in those 4 words a register value, a return address, and an
inverted jiffies. (Whether capturing anything beyond the cycle counter
in the interrupt handler is even adding much of value is a question for
a different time.)

So since we have 4 words, and not all of them are 2-monotone, we look
for a linear extractor with proofs for more complex distributions. It
turns out that a max-period linear function fits this bill quite well,
easily extending to the larger state size and the fact that we're mixing
in more than just the cycle counter. By picking one that is max-period,
there are no non-trivial invariant subspaces, unlike NT's rotate-xor,
which means we benefit from the analysis of <https://eprint.iacr.org/2021/1002>
which gives proofs that linear functions with only trivial invariant
subspaces make very good entropy extractors for the type of complex
distributions that we have, when accumulating entropy via S←AS⊕X, where
S is our pool vector, X is the new irq data vector, and A is our
function's matrix.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, https://א.cc/fvEu8uYd>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, and is therefore max-period,
fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in irq context.

As a final note, the previous fast_mix() was contributed by an anonymous
author, which, I've been told, has made some legally-minded people a bit
uncomfortable and is also against the kernel project's "real name"
policy.

Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Cc: Eric Biggers <ebiggers@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[38e16bfede...](https://github.com/zx2c4/linux-rng/commit/38e16bfede51ea17e7cdd1a4b5efb54be8d03962)
#### Wednesday 2022-02-16 02:17:50 by Jason A. Donenfeld

random: use linear max-period irq extractor

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As a permutation of only two
rounds, there are some easily searchable differential trails in it, and
as a means of preventing malicious irqs, it completely fails, since it
xors new data into the entire state every time. It can't really be
analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in this
context, in case a malicious irq compromises a per-cpu fast pool within
the 64 interrupts / 1 second window, and then inside of that same window
somehow can control its return address and cycle counter, even if that's
a bit far fetched. However with a very CPU-limited budget, actually
doing that remains an active research project (and perhaps there'll be
something useful for Linux to come out of it). And while the abundance
of caution would be nice, this isn't *currently* the security model, and
we don't yet have a fast enough solution to make it our security model.
Plus there's not exactly a pressing need to do that. (And for the
avoidance of doubt, the actual cluster of 64 accumulated irqs still gets
dumped into our cryptographically secure input pool.)

So, for now we are going to stick with the existing irq security model,
which assumes that each cluster of 64 irq data samples are mostly
non-malicious and not colluding with an infoleaker. With this as our
goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a *max-period* linear function fits
this bill quite well, easily extending to the larger state size and the
fact that we're mixing in more than just the cycle counter. By picking
one that is max-period, there are no non-trivial invariant subspaces,
unlike NT's rotate-xor, which means we benefit from the analysis of
<https://eprint.iacr.org/2021/1002> which gives proofs that linear
functions with only trivial invariant subspaces make very good entropy
extractors for the type of complex distributions that we have, when
accumulating entropy via S←AS⊕X, where S is our pool vector, X is the
new irq data vector, and A is our function's matrix.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/fvEu8uYd>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, and is therefore max-period,
fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in irq context.

As a final note, the previous fast_mix() was contributed by an anonymous
author, which, I've been told, has made some legally-minded people a bit
uncomfortable and is also against the kernel project's "real name"
policy.

Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Cc: Eric Biggers <ebiggers@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [ksh93/ksh](https://github.com/ksh93/ksh)@[2bc2d38e94...](https://github.com/ksh93/ksh/commit/2bc2d38e9446cd67a3036107c11a625c9dc6764a)
#### Wednesday 2022-02-16 02:59:49 by Martijn Dekker

Backport 'read -a' and 'read -p' from ksh 93v-/2020

ksh2020 may have been abandoned but it's still in several distros.
It supports bash-style -a (same as -A) and -p (prompt string)
options for the read command. This has created a user expectation
for those options to work on 93u+m. That, plus my opinion that the
old varname?prompt argument syntax is frankly dreadful (it's unsafe
by default due to pathname expansion of an unquoted '?'), made me
decide that ksh 93u+m is better off backporting the 93v-/2020
changes to 'read' -- even if it does take an ugly hack to preserve
compatibility with old -p usage, which causes ksh to read from the
active co-process (new usage: -u p). But we can improve that hack.

For comparison, the 93v- beta version of b_read() is here:
https://github.com/ksh93/ast-open-archive/blob/be2ec79f/src/cmd/ksh93/bltins/read.c#L204-L372

src/cmd/ksh93/bltins/read.c: b_read():
- Backport the -p changes, with the following modifications.
- Improve compatibility for legacy -p option usage (which causes
  ksh to read from a co-process). Compatibility handling is
  activated when a coprocess is active and '-p' is followed by a
  valid vname (variable name). The 93v-/2020 code did not correctly
  detect a vname; it used a flawed approach involving a check
  against a regex. Dot variables or the legacy vname?prompt syntax
  were not handled. We now test this by temporarily getting rid of
  the ?prompt (if any), then calling nv_open() with the
  NV_VARNAME|NV_NOFAIL flags (the latter flag prevents an error
  message, not an actual failure) and seeing if a pointer is
  returned. This guarantees consistency as nv_open() is also used
  for the actual read operation. The side effect is that it will
  add a node for a valid vname that doesn't exist yet, but that's
  not a problem as we're about to create that variable anyway.
- Rename the misleadingly named 'name' variable to 'prompt'.
  It points to the prompt string, not to a variable name.

src/cmd/ksh93/data/builtins.c: sh_optpwd[]:
- Add -a as an alterative to -A. All that is needed is adding '|a'
  and optget(3) will automatically convert it to 'A'.
- Backport the new documentation with significant edits.
- Tweaks.

src/cmd/ksh93/sh.1:
- Update accordingly.
- Tidy up the unreadable mess that was the 'read' documentation.
  The options are now shown in a list.

Resolves: https://github.com/ksh93/ksh/issues/463

---
## [Roblox-Thot/cashmoney-con.tk](https://github.com/Roblox-Thot/cashmoney-con.tk)@[5e6492f945...](https://github.com/Roblox-Thot/cashmoney-con.tk/commit/5e6492f945d83888cafb6d6c09f05c33d12a6368)
#### Wednesday 2022-02-16 03:03:49 by Roblox Thot

Update LICENSE

fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you

---
## [chensun/website](https://github.com/chensun/website)@[bdc0145c1f...](https://github.com/chensun/website/commit/bdc0145c1fa6297e5c737d45411dc82f26c96a0b)
#### Wednesday 2022-02-16 03:19:29 by Rui Vasconcelos

rm RFMVasconcelos (#2981)

Dear community,

In the last 2 years, I have had the great pleasure to be part of the community building this amazing open-source tool. I am quite satisfied in feeling that I left a small dent in the overall experience for new users.

Today I see my path take a different course, which I am excited to invest my full energy into. 🚀

I was also very lucky to work on Canonical's distribution - which I leave in the great hands of @knkski  @DomFleischmann and more. 

If you want to stay in touch, please connect via LinkedIn.

I nominate @knkski to take on some of the responsibilities I held, in his own capacity, given his 3 years of dedication to Kubeflow.

With Gratitude,
Rui

---
## [Atheos/Atheos](https://github.com/Atheos/Atheos)@[905c954630...](https://github.com/Atheos/Atheos/commit/905c954630ab51ce1660d93e4cb0f906a1fa672e)
#### Wednesday 2022-02-16 03:37:29 by Liam Siira

Honestly should have commit more often because the amount of changes to the website are quite drastic.
Luckily the website is still pretty basic and not really a "for-production" codebase. In summary, I've been trying to update the site to be a fully fledged home page for Atheos and provide everything I feel users of Atheos would deserver. I've turned the website into more of a PHP router with markdown files and some probably stupid complex PHP action in the background. Hopefully this is a good direction, if not, I just wasted my time; no big deal. It's not a hard site to code for or make changes to. I'm sorry about not committing more often for each individual change.

---
## [entrez/EvilHack](https://github.com/entrez/EvilHack)@[a4e0378bb5...](https://github.com/entrez/EvilHack/commit/a4e0378bb510209b72eafd3dcfa0d7d4caf8c638)
#### Wednesday 2022-02-16 03:57:17 by k21971

Fix: cursed light vs worn light.

From NetHack 3.7 git commit e8341dc (modified, with bug fixes from
commit a1feac4):

'Another gold dragon scales/mail issue, reported bu vultur-cadens:
reading a cursed scroll of light extinguishes carried light sources
except for wielded Sunsword and worn gold dragon scales/mail; there
was a special message for Sunsword (preventing the hero from being in
darkness) but no such message for gold dragon scales/mail.  Replace
the special message with a more generic one applicable to both cases.

Also, implement the suggestion that cursed light degrade the amount
of light being emitted (which varies by bless/curse state) for those
two cases.  Sunsword has a 75% chance to resist, gold dragon scales
25% chance.  And add the inverse:  blessed scroll of light might
increase the amount of light by improving their bless/curse state.
The resistance check applies here too and isn't inverted; Sunsword
is still fairly likely to resist.

Uncursed scroll of light, spell of light regardless of skill, zapped
or broken wand of light have so such effect.'

This affects EvilHack's shield of light also.

---
## [Colon-D/sa2-mirror-mission-4](https://github.com/Colon-D/sa2-mirror-mission-4)@[5c9e08d574...](https://github.com/Colon-D/sa2-mirror-mission-4/commit/5c9e08d574b37a6a5e908e1c2f707aa5b60d4931)
#### Wednesday 2022-02-16 03:58:31 by Colon-D

Fix Mech's Guns & Upper Bodies not rotating correctly

trial and error baby

guns and upper bodies are dumb and stupid when mirroring the player on
the x axis xor the z axis. they are NOT dumb and stupid when both
applied.
to make the gun not dumb and stupid, we need to tell it that it is
facing 180 degrees more than it thinks it is. idk why this works but it
does.
to make the upper body not dumb and stupid, we need to tell it to be
mirrored, that is negated from 360 degrees. idk why this works either.

moral of the story, spend a dozen hours looking for something and you
might find it.

---
## [subash2001/kernel_realme_RMX1821](https://github.com/subash2001/kernel_realme_RMX1821)@[a0c54efb9a...](https://github.com/subash2001/kernel_realme_RMX1821/commit/a0c54efb9ac613cf4f97da2aa88e2c289da56f37)
#### Wednesday 2022-02-16 04:24:52 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

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

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[af609afe70...](https://github.com/Koi-3088/ForkBot.NET/commit/af609afe708ff9fe88646a16b5991d40bd9cd0b3)
#### Wednesday 2022-02-16 05:02:36 by Koi

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
## [XertroV/aec-membership-test-simulator](https://github.com/XertroV/aec-membership-test-simulator)@[55ecd1780f...](https://github.com/XertroV/aec-membership-test-simulator/commit/55ecd1780fc235887af14d8210300ca2c32e11bc)
#### Wednesday 2022-02-16 05:48:14 by Max Kaye

well, I think we can conclude that this shit's fucked.

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[16b667bdd3...](https://github.com/repinger/exynos9611_m21_kernel/commit/16b667bdd3647d4741c39d9973ef1fcdedacad1e)
#### Wednesday 2022-02-16 05:52:04 by Masahiro Yamada

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
## [darlyneleongomez/Laravel-dar](https://github.com/darlyneleongomez/Laravel-dar)@[7f86e8cf23...](https://github.com/darlyneleongomez/Laravel-dar/commit/7f86e8cf232e2c8d38995800280a6ce391839814)
#### Wednesday 2022-02-16 06:34:58 by darlyneleongomez

Delete LARAVEL

<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400"></a></p>

<p align="center">
<a href="https://travis-ci.org/laravel/framework"><img src="https://travis-ci.org/laravel/framework.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

## About Laravel

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel takes the pain out of development by easing common tasks used in many web projects, such as:

- [Simple, fast routing engine](https://laravel.com/docs/routing).
- [Powerful dependency injection container](https://laravel.com/docs/container).
- Multiple back-ends for [session](https://laravel.com/docs/session) and [cache](https://laravel.com/docs/cache) storage.
- Expressive, intuitive [database ORM](https://laravel.com/docs/eloquent).
- Database agnostic [schema migrations](https://laravel.com/docs/migrations).
- [Robust background job processing](https://laravel.com/docs/queues).
- [Real-time event broadcasting](https://laravel.com/docs/broadcasting).

Laravel is accessible, powerful, and provides tools required for large, robust applications.

## Learning Laravel

Laravel has the most extensive and thorough [documentation](https://laravel.com/docs) and video tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.

If you don't feel like reading, [Laracasts](https://laracasts.com) can help. Laracasts contains over 1500 video tutorials on a range of topics including Laravel, modern PHP, unit testing, and JavaScript. Boost your skills by digging into our comprehensive video library.

## Laravel Sponsors

We would like to extend our thanks to the following sponsors for funding Laravel development. If you are interested in becoming a sponsor, please visit the Laravel [Patreon page](https://patreon.com/taylorotwell).

### Premium Partners

- **[Vehikl](https://vehikl.com/)**
- **[Tighten Co.](https://tighten.co)**
- **[Kirschbaum Development Group](https://kirschbaumdevelopment.com)**
- **[64 Robots](https://64robots.com)**
- **[Cubet Techno Labs](https://cubettech.com)**
- **[Cyber-Duck](https://cyber-duck.co.uk)**
- **[Many](https://www.many.co.uk)**
- **[Webdock, Fast VPS Hosting](https://www.webdock.io/en)**
- **[DevSquad](https://devsquad.com)**
- **[Curotec](https://www.curotec.com/services/technologies/laravel/)**
- **[OP.GG](https://op.gg)**
- **[CMS Max](https://www.cmsmax.com/)**
- **[WebReinvent](https://webreinvent.com/?utm_source=laravel&utm_medium=github&utm_campaign=patreon-sponsors)**
- **[Lendio](https://lendio.com)**
- **[Romega Software](https://romegasoftware.com)**

## Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the [Laravel documentation](https://laravel.com/docs/contributions).

## Code of Conduct

In order to ensure that the Laravel community is welcoming to all, please review and abide by the [Code of Conduct](https://laravel.com/docs/contributions#code-of-conduct).

## Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via [taylor@laravel.com](mailto:taylor@laravel.com). All security vulnerabilities will be promptly addressed.

## License

The Laravel framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

---
## [praveentml/Stockfish](https://github.com/praveentml/Stockfish)@[cb9c2594fc...](https://github.com/praveentml/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Wednesday 2022-02-16 06:42:58 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [Legonzaur/NorthstarLauncher](https://github.com/Legonzaur/NorthstarLauncher)@[db0af63704...](https://github.com/Legonzaur/NorthstarLauncher/commit/db0af63704a6fbc57e80a9db01bbc01b79339d9f)
#### Wednesday 2022-02-16 07:20:23 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [freedesktop/NetworkManager](https://github.com/freedesktop/NetworkManager)@[dac12a8d61...](https://github.com/freedesktop/NetworkManager/commit/dac12a8d6178a6d82fc0913ad8825c8556380ba8)
#### Wednesday 2022-02-16 09:06:48 by Thomas Haller

platform: support IPv6 mulitpath routes and fix cache inconsistency

Add support for IPv6 multipath routes, by treating them as single-hop
routes. Otherwise, we can easily end up with an inconsistent platform
cache.

Background:
-----------

Routes are hard. We have NMPlatform which is a cache of netlink objects.
That means, we have a hash table and we cache objects based on some
identity (nmp_object_id_equal()). So those objects must have some immutable,
indistinguishable properties that determine whether an object is the
same or a different one.

For routes and routing rules, this identifying property is basically a subset
of the attributes (but not all!). That makes it very hard, because tomorrow
kernel could add an attribute that becomes part of the identity, and NetworkManager
wouldn't recognize it, resulting in cache inconsistency by wrongly
thinking two different routes are one and the same. Anyway.

The other point is that we rely on netlink events to maintain the cache.
So when we receive a RTM_NEWROUTE we add the object to the cache, and
delete it upon RTM_DELROUTE. When you do `ip route replace`, kernel
might replace a (different!) route, but only send one RTM_NEWROUTE message.
We handle that by somehow finding the route that was replaced/deleted. It's
ugly. Did I say, that routes are hard?

Also, for IPv4 routes, multipath attributes are just a part of the
routes identity. That is, you add two different routes that only differ
by their multipath list, and then kernel does as you would expect.
NetworkManager does not support IPv4 multihop routes and just ignores
them.
Also, a multipath route can have next hops on different interfaces,
which goes against our current assumption, that an NMPlatformIP4Route
has an interface (or no interface, in case of blackhole routes). That
makes it hard to meaningfully support IPv4 routes. But we probably don't
have to, because we can just pretend that such routes don't exist and
our cache stays consistent (at least, until somebody calls `ip route
replace` *sigh*).

Not so for IPv6. When you add (`ip route append`) an IPv6 route that is
identical to an existing route -- except their multipath attribute -- then it
behaves as if the existing route was modified and the result is the
merged route with more next-hops. Note that in this case kernel will
only send a RTM_NEWROUTE message with the full multipath list. If we
would treat the multipath list as part of the route's identity, this
would be as if kernel deleted one routes and created a different one (the
merged one), but only sending one notification. That's a bit similar to
what happens during `ip route replace`, but it would be nightmare to
find out which route was thereby replaced.
Likewise, when you delete a route, then kernel will "subtract" the
next-hop and sent a RTM_DELROUTE notification only about the next-hop that
was deleted. To handle that, you would have to find the full multihop
route, and replace it with the remainder after the subtraction.

NetworkManager so far ignored IPv6 routes with more than one next-hop, this
means you can start with one single-hop route (that NetworkManger sees
and has in the platform cache). Then you create a similar route (only
differing by the next-hop). Kernel will merge the routes, but not notify
NetworkManager that the single-hop route is not longer a single-hop
route. This can easily cause a cache inconsistency and subtle bugs. For
IPv6 we MUST handle multihop routes.

Kernels behavior makes little sense, if you expect that routes have an
immutable identity and want to get notifications about addition/removal.
We can however make sense by it by pretending that all IPv6 routes are
single-hop! With only the twist that a single RTM_NEWROUTE notification
might notify about multiple routes at the same time. This is what the
patch does.

The Patch
---------

Now one RTM_NEWROUTE message can contain multiple IPv6 routes
(NMPObject). That would mean that nmp_object_new_from_nl() needs to
return a list of objects. But it's not implemented that way. Instead,
we still call nmp_object_new_from_nl(), and the parsing code can
indicate that there is something more, indicating the caller to call
nmp_object_new_from_nl() again in a loop to fetch more objects.

In practice, I think all RTM_DELROUTE messages for IPv6 routes are
single-hop. Still, we implement it to handle also multi-hop messages the
same way.

Note that we just parse the netlink message again from scratch. The alternative
would be to parse the first object once, and then clone the object and
only update the next-hop. That would be more efficient, but probably
harder to understand/implement.

https://bugzilla.redhat.com/show_bug.cgi?id=1837254#c20

---
## [Ashsky72/dr.semmelweis_handwashing](https://github.com/Ashsky72/dr.semmelweis_handwashing)@[e74a64e931...](https://github.com/Ashsky72/dr.semmelweis_handwashing/commit/e74a64e93168e00696c0d470d855a3202642dbe5)
#### Wednesday 2022-02-16 09:08:38 by Ashish Kumar

Rename README.md to Analysis insights

What happens when the data shows you need to change a current approach or business practice? Any kind of change can be very hard—even with supporting data. If you’re at a large company, it can be very difficult to get executives and teams to re-examine previously successful practices and adopt new ones. Even agile startups are no less immune to “staying the course” when a potential new direction conflicts with the founders or investors’ opinions and beliefs.

If data is becoming more and more critical to our business success, why do we still struggle to listen to it on a regular basis? Embracing data has been a problem for humanity long before the appearance of databases, spreadsheets, and dashboards. While we may aspire to rely more on data in our decision-making, human nature can get in the way as we resist new ideas or insights.

One illustrative example involves a Hungarian doctor from the mid-nineteenth century named Ignaz Semmelweis (1818-1865). In 1846, he was appointed as an assistant at a Vienna hospital with two maternity clinics for training doctors and midwives. Similar to other hospitals around the world at this time, many admitted mothers were dying of a mysterious illness called puerperal or childbed fever. Semmelweis discovered a disturbing trend where its doctors’ clinic ( clinic 1) had an average mortality rate of 9.9%, which was significantly higher than that of its midwives’ clinic ( clinic 2 ).

Fig 1 and 2

Semmelweis was determined to identify the cause of this noticeable difference between the two clinics. At the time, there was no notion of germs or infections so he considered a variety of potential causes such as bad ventilation, overcrowding, delivery methods, and even religion. An unfortunate event triggered Semmelweis’s aha moment. When a close friend at the hospital was conducting an autopsy, he was accidentally poked by a student’s scalpel and later died from the wound. As Semmelweis performed the difficult post-mortem examination, he noticed a strong similarity in the pathology of his friend’s illness and that of the women who died of childbed fever.

At the Vienna hospital, it was part of the doctors' study to perform autopsies in the morning and then spend the rest of their day attending patients in the maternity ward without ever washing their hands. Unlike the doctors, the midwives performed no autopsy work and were not in contact with any corpses. Semmelweis hypothesized that some kind of poisonous particles were being transferred by the doctors from the cadavers to the patients in the maternity clinic. He found a chlorinated lime solution was strong enough to remove the putrid smell of the autopsy tissue from the doctors’ hands and determined it would be ideal for removing these deadly contaminants.

Two months after the death of his friend, he introduced a new handwashing policy for the doctors to use the chlorinated lime solution after any autopsies. When he launched the new policy, the monthly mortality rate was 12.2% in the doctors’ clinic. Semmelweis’s new policy had an immediate impact, and the death rate was lowered to 2.2% (an 82% decrease). 

( Fig.3 ,4, 5 and 6)
After several months of significantly lower mortality rates, he still observed student doctors who were not following the policy. After introducing stricter controls on the negligent doctors, Semmelweis was able to lower the mortality rate even further with two months where no mothers died of childbed fever.

Semmelweis couldn’t scientifically prove why his handwashing policy worked—that wouldn’t happen until chemist Louis Pasteur discovered the germ theory of disease in the mid-1860s. What the doctor had was more than 18 months of statistical data showing his handwashing approach worked and that such practices could save the lives of thousands of expectant mothers. He had the truth but it was not enough.

 he faced sharp criticism, ridicule and resistance from the established medical community.
 
 In 1849, he was unable to renew his position in the maternity ward and was blocked from obtaining similar positions in Vienna. A frustrated and demoralized Semmelweis moved back to Budapest. He watched his theory be openly attacked in medical lecture halls and medical publications.
 
Two weeks later he died at the age of 47 succumbing to an infected wound inflicted by the asylum’s guards.

What can we learn from Semmelweis’s experience?

Semmelweis’s data met three key criteria- it was truthful, valuable and actionable—but he ultimately failed to see his ideas adopted in his lifetime. He stumbled in one essential area—the communication of his data. I’ve identified four oversights that may have prevented Semmelweis from communicating his ideas more effectively.

1. Timeliness and Clarity
Semmelweis took 14 years to officially publish his childbed fever findings in 1861. Up until this time, his work was shared within the medical community by his colleagues and students. Unfortunately, these associates misinterpreted and misrepresented Semmelweis’s claims, causing many obstetricians to dismiss, refute or ignore them.

Key takeaway: "If you possess insights that are critical to your business success, you have a duty to communicate them clearly in a timely manner."

2.Narrative Evokes Emotion

One of the biggest mistakes Semmelweis made was he failed to tell a story with his data. Interesting statistics alone won’t persuade skeptical minds. The data-driven doctor missed an opportunity to weave his facts into a compelling data story that connected with his audience on an emotional level.

Key takeaway: "Don’t rely on just logic and reason to make your points. Decisions are more often made by emotion, and an effective narrative can touch your audience in ways the numbers alone never will."

3.The Power of Data Visualization

Finally, Semmelweis failed to visualize his numbers effectively as he relied primarily on data tables. Well-designed charts can make insights come to life.It’s true Semmelweis didn’t have access to visualization tools like we do today, but that didn’t stop another physician John Snow in 1854 from creating a map visualization to effectively illustrate a cholera outbreak in London

Key takeaway: "Data can often be communicated more powerfully with data visualizations than just tabular data. Charts should reinforce your key points and make it easier for your audience to follow your data story."

---
## [ChiefDrOwonikoko1/docs](https://github.com/ChiefDrOwonikoko1/docs)@[4a18dea78a...](https://github.com/ChiefDrOwonikoko1/docs/commit/4a18dea78ab7006a1e4a572bb41d5346be31e535)
#### Wednesday 2022-02-16 11:44:41 by ChiefDrOwonikoko1

Top Best Most Powerful spiritual herbalist 

Description:

+2347017229671,NO CRIME IN TRYING, Because IF YOU FALL,YOU WILL SURELY RISE BY YOUR EFFORTS,So do not HIDE YOUR PROBLEMS....
Do you know you can be WEALTHY without HUMAN BEING SACRIFICE,so CHIEF ORIOGBO OWONIKOKO of IJEBU LAND,also the BAAJITO ISEGUN OF IJEBU IGBO is here to help people's that come to seek of his help,He hate lie,just be Loyal and honest to him and explain everything you need to him with open mind,All the problem you share shall be solved by the powerful grace of God...... His shrine was Located at IJEBU IGBO OGUN STATE NIGERIA, Do not says you have been SCAM for so many times that you will Relenting,if you fall,you will surely rise by all your efforts...... It's true that a lot of fake HERBALIST and NATIVE DOCTOR in SOCIAL MEDIA,Just know that what you seen can never use to deceive you..... You will open your eyes very well before you make any steps..... You can contact within if you need of anykind of spiritual purpose...such as follows: MAKING MONEY WITHOUT HUMAN SACRIFICE, SEARCHING FOR PREGNANCY, ANAEMIA, TYPHOID,GOLORIA, APPENDIX,MALARI, and many more, BET9JA SUCCESS, PROMOTION AT WORK, INSTANT MONEY, DO AS I SAY, COMMAND TONE, POWER TO PERFORM MIRACLE, CROWD PULLER, BUSINESS BOOSTER, BODY PROTECTION, DISSAPIARING POWER, LOTTO SUCCESS, OSHOLE TUTU, EYONU AYE, IRADAPA, RECOVERY OF LOST GLORY, ASINA OLA, SUCCESS IN EVERYTHING....and so on.. CHIEF ORIOGBO OWONIKOKO is her for you anytime any day, You can come to him and explain whatever you want to the Ancestors and it shall be grant by the powerful grace of God.... Hotline:+2347017229671..... CHIEF ORIOGBO OWONIKOKO was know every part of the world by his great hand work,he also send his product to every where you are under the planet of God......
MOTTO:GREAT MAN DESERVE GREAT REWARDS...
NOTICE:IF ANYBODY TRY TO COPY THIS ADVERT TO SCAM OR DO BAD ONLINE,ITS GOD OF IRON,THUNDER that will KILL THE KIND OF PERSON and HIS/HER FAMILIES MEMBERS IN PAIN......

---
## [bytewax/bytewax](https://github.com/bytewax/bytewax)@[8a6f0c0886...](https://github.com/bytewax/bytewax/commit/8a6f0c08867939b52421e10998546ba2850090b9)
#### Wednesday 2022-02-16 12:07:47 by David Selassie

Introducing: exhash

Missed out on [this crucial little note for Python's
`__hash__`](https://docs.python.org/3.9/reference/datamodel.html#object.__hash__):

> By default, the `__hash__()` values of str and bytes objects are
> "salted" with an unpredictable random value. Although they remain
> constant within an individual Python process, they are not
> predictable between repeated invocations of Python.

This means that having Timely route using Python's `hash` is fine
within one process, but breaks between multiple processes. Running the
wordcount demo with multiple procs, I occasionally get duplicate
counts because as it's doing `reduce_epoch` it thinks two instances of
`("the", 1)` are not the same key.

The "easier" way to fix this is to set the env var
[`PYTHONHASHSEED`](https://docs.python.org/3.9/using/cmdline.html#envvar-PYTHONHASHSEED). But
I don't think that's the best idea for a few reasons:

1. It's another gotcha for running multiple procs.

2. It's another source of coordination between cluster processes.

3. It feels weird to explain in one of our first tutorials that you
   need to use this obscure Python interpreter env var to make things
   work, and if you forget, there aren't errors, just wrong answers.

So my thought was to create an analagous `exhash` which explicitly is
meant to capture a consistent hash.

I did this using `functools.singledispatch` so you can write a version
for each type, and it'll call the right version. This will let users
add their own custom types later if they want. It returns a
[`hashlib`](https://docs.python.org/3/library/hashlib.html) algorithm
object (which doesn't actually have a formal type...). Which bytewax
will ask for the digest from and pass onto the Rust hashing machinery.

You can optionally pass in an algorithm object to support easy hashing
of nested types as you'll see in the `tuple` and `frozenset`
implementations.

Worries:

- This is also a little bit magic and another bit of conceptual
  overhead, although I'm hoping that if you stick to pretty common
  Python types you won't even need to touch this.

- Should we allow implementations for mutable objects like `list` and
  `set`? I haven't thought through what situations might cause a
  mutable list to "change" while sitting in a Rust `HashMap` and mean
  that all hell could break loose. I think this could happen if you
  use things like `stateful_map` and store and mutate values while
  also passing them on. I define some exception raising
  implementations for mutable types, but people could still override
  this if they want.

---
## [mkingopng/feedback_prize](https://github.com/mkingopng/feedback_prize)@[0ac7dd8361...](https://github.com/mkingopng/feedback_prize/commit/0ac7dd836192f6e2009d4dabca53e0f32f325a0a)
#### Wednesday 2022-02-16 12:31:37 by mkingopng

ok a few pennies have just dropped after talking with Wilson and re-reading a bunch of posts on the discussion.

Big shout out to Wilson. Talking through this with you and then going through my notes again has made me rethink a lot of things i thought I'd resolved.

2x longformers does NOT mean that we're training two models at the same time (dumb-ass). It means that we train twice, with different parameters/hyperparameters and the use both sets of checkpoints to do inference.

second, i really just need 5 folds. 10 is overkill.

Third, i need ot dial back the max_length. max_length=4096 was not used in training. Abishek specifically says this in the forum. His naming for one of his model directories gives a big hint -> 1536 is the max_length for one of the models. It isn't yet clear what the max_length was for the others, however there is some useful EDA I did at the beginning of the competition that gives some helpful insights (perhaps).

Fourth, I'm using the wrong model. abishek is NOT just using longformer-base-4096. He is either using longformer-large-4096 AND longformer-base-4096, or he is using both longformer-large-4096. His inference code implies the latter however his data structure implies the former.

Fifth, the f1 score I'm getting in training should be a pretty good leading indicator of what I'll get at inference. If I'm getting low 0.60's in training there is no reason to expect that this will do better at inference. For this reason the training run I'm doing now will NOT work out. However, I'm going to let it finish just because its been pissing me off. The upside is that with all the changes mentioned above, future training runs will not be like this EPIC pain-fest.

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[1d8f94f1b7...](https://github.com/zx2c4/linux-rng/commit/1d8f94f1b797b0b2cfcc6ab2a8d0b58ac3afc546)
#### Wednesday 2022-02-16 12:39:13 by Jason A. Donenfeld

random: use linear max-period irq extractor

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As an ARX permutation of only
two rounds, there are some easily searchable differential trails in it,
and as a means of preventing malicious irqs, it completely fails, since
it xors new data into the entire state every time. It can't really be
analyzed as a random permutation, because it clearly isn't, and it can't
be analyzed as an interesting linear algebraic structure either, because
it's also not that. There really is very little one can say about it in
terms of entropy accumulation. It might diffuse bits, some of the time,
maybe, we hope, I guess. But for the most part, it fails to accomplish
anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in this
context, in case a malicious irq compromises a per-cpu fast pool within
the 64 interrupts / 1 second window, and then inside of that same window
somehow can control its return address and cycle counter, even if that's
a bit far fetched. However with a very CPU-limited budget, actually
doing that remains an active research project (and perhaps there'll be
something useful for Linux to come out of it). And while the abundance
of caution would be nice, this isn't *currently* the security model, and
we don't yet have a fast enough solution to make it our security model.
Plus there's not exactly a pressing need to do that. (And for the
avoidance of doubt, the actual cluster of 64 accumulated irqs still gets
dumped into our cryptographically secure input pool.)

So, for now we are going to stick with the existing irq security model,
which assumes that each cluster of 64 irq data samples is mostly
non-malicious and not colluding with an infoleaker. With this as our
goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the case with the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a *max-period* linear function fits
this bill quite well, easily extending to the larger state size and to
the fact that we're mixing in more than just the cycle counter. By
picking one that is max-period, there are no non-trivial invariant
subspaces, unlike NT's rotate-xor, which means we benefit from the
analysis of <https://eprint.iacr.org/2021/1002>. This paper gives proofs
that linear functions with only trivial invariant subspaces make very
good entropy extractors for the type of complex distributions that we
have, and suggests that we extract entropy via S←AS⊕X, where S is our
pool vector, X is the new irq data vector, and A is the transformation
matrix.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/fvEu8uYd>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, and is therefore max-period,
fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in irq context.

As a final note, the previous fast_mix() was contributed by an anonymous
author, which violates the kernel project's "real name" policy and has
ruffled the feathers of legally-minded people. Replacing this function
with this commit should now clear up those concerns.

Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Cc: Eric Biggers <ebiggers@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [haruInDisguise/dwm](https://github.com/haruInDisguise/dwm)@[67d76bdc68...](https://github.com/haruInDisguise/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-02-16 12:45:08 by Chris Down

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
## [pmotschmann/Evolve](https://github.com/pmotschmann/Evolve)@[2cd5860161...](https://github.com/pmotschmann/Evolve/commit/2cd5860161e23a0a160cd9c4be4876fbf98dbd6b)
#### Wednesday 2022-02-16 13:04:14 by Beorseder

Calculator Updates, Minor Bug Fixes, and Info

Perks:
Added Doomed achievement to the perks lists because there's no way to know that it unlocks Hellscape/Eden planets otherwise.
Added Governor CRISPR tree to perks list.
Fixed Evolve Journeyman not showing the full list of values in the wiki perks page if the perk was not yet obtained.

Calculators:
Updated Plasmid/Anti-Plasmid gain calculators with the new caps on gains, the High Population trait, being Synthetic genus for MADs, and being in Truepath, and AI Apocalypse reset.
Updated Phage gain calculator with Truepath and AI Apocalypse reset.
Updated Dark Energy bonus calculator with Lemon Cleaner perk.
Added AI Core gain and bonus calculators.
Added gain calculators to AI Apocalypse reset entry.
Updated Job Stress calculator to be fixed and accommodate for trait rankings and, the Emotionless trait and to fix Titan Colonist string.

Wiki Info:
Added information about Sludge's modification costing 10x more and their inability to remove Ooze to the Failed Experiment entry. Also fixed the data link to MAD reset.
Similarly added to CRISPR Mutation entry that Sludge also have 10x costs.
Added to Raid, Siege, and Terrorist Attack events how they don't happen in Truepath.
Added Pillage event(s) entry to Major Events page.
Updated Llama Minor Event with trait restrictions.
Updated Ascension reset entry with information on the geology buff and Ascended planets.
Added wiki effect to Alien Biotech tech.

Textual:
Fixed Entertainer tooltip showing twice the effect of Musical.
Fixed Gauss Rifles showing the effect for Disruptor Rifles.
Fixed some wiki fuel cost displays.
Fixed Water Freighter tooltip showing half the Helium-3 cost. Fixes #713
Fixed some typos.
Changed instances of "space cost creep" to "non-homeworld cost creep" to indicate that they apply to Hell Dimension as well.
Updated Pig-Latin.

Misc:
Exporting the save now updates accelerated time bank to account for if someone is paused and exports, updating their save's current time and thus losing all that accelerated time.
Fixed CRISPR and Blood Infusions being affected by adjustCosts when checking their affordability, which caused some issues with traits shifting their costs around making the coloring inaccurate sometimes near the cost.
Fixed Ritual Casting not showing up in Industry in Cataclysm.
Fixed bug where, if not Preloading Tab Content, shifting to another tab when in the custom lab and then shifting back to Civilization tab would not show the custom lab anymore. Fixes #671
Detritivores no longer see the Farming ritual as it doesn't do anything for them.
Fixed bug with building the Forward Base not reloading space to show the Troop Lander and Crashed Ship structures.

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[c293c6dd81...](https://github.com/zx2c4/linux-rng/commit/c293c6dd81135d838d697a2db1606303291fe4c9)
#### Wednesday 2022-02-16 13:28:50 by Jason A. Donenfeld

random: use linear max-period interrupt extractor

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As an ARX permutation of only
two rounds, there are some easily searchable differential trails in it,
and as a means of preventing malicious interrupts, it completely fails,
since it xors new data into the entire state every time. It can't really
be analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in the
interrupt handler itself, in case a malicious interrupt compromises a
per-cpu fast pool within the 64 interrupts / 1 second window, and then
inside of that same window somehow can control its return address and
cycle counter, even if that's a bit far fetched. However with a very
CPU-limited budget, actually doing that remains an active research
project (and perhaps there'll be something useful for Linux to come out
of it). And while the abundance of caution would be nice, this isn't
*currently* the security model, and we don't yet have a fast enough
solution to make it our security model.  Plus there's not exactly a
pressing need to do that. (And for the avoidance of doubt, the actual
cluster of 64 accumulated interrupts still gets dumped into our
cryptographically secure input pool.)

So, for now we are going to stick with the existing interrupt security
model, which assumes that each cluster of 64 interrupt data samples is
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the case with the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions.

However, when considering this for our four-word accumulation, versus
NT's one-word, we run into potential problems because the words don't
contribute to each other, and some may well be fixed, which means we'd
need something to schedule on top. And more importantly, our
distribution is not 2-monotone like NT's, because in addition to the
cycle counter, we also include in those 4 words a register value, a
return address, and an inverted jiffies. (Whether capturing anything
beyond the cycle counter in the interrupt handler is even adding much of
value is a question for a different time.)

So since we have 4 words, and not all of them are 2-monotone, we instead
look for a proven linear extractor that works for more complex
distributions. It turns out that a *max-period* linear function fits
this bill quite well, easily extending to the larger state size and to
the fact that we're mixing in more than just the cycle counter. By
picking one that is max-period, there are no non-trivial invariant
subspaces, unlike NT's rotate-xor, which means we benefit from the
analysis of <https://eprint.iacr.org/2021/1002>. This paper gives proofs
that linear functions with only trivial invariant subspaces make very
good entropy extractors for the type of complex distributions that we
have, and suggests that we extract entropy via S←AS⊕X, where S is our
pool vector, X is the new interrupt data vector, and A is the
transformation matrix.

This commit implements one such very fast and high diffusion max-period
linear function in a Feistel-like fashion, which pipelines quite well.
On an i7-11850H, this takes 34 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://א.cc/fvEu8uYd>, proves that
this construction does indeed yield a linear function of order 2^128-1
whose minimal polynomial is primitive, and is therefore max-period with
no non-trivial invariant subspaces, fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose a function with pretty high diffusion, even higher than the
original fast_mix(). In other words, we probably don't regress at all
from a perspective of diffusion, even if it's not really the goal here
anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now matches that model much more rigorously. Plus the
performance is better, which perhaps matters in interrupt context.

As a final note, the previous fast_mix() was contributed on the mailing
list by an anonymous author, which violates the kernel project's "real
name" policy and has ruffled the feathers of legally-minded people.
Replacing this function should clear up those concerns.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[49bb20bbcd...](https://github.com/payday-restoration/restoration-mod/commit/49bb20bbcdd563dc83518a19482985676a270cf2)
#### Wednesday 2022-02-16 17:57:31 by SonicSoapyBoi

HOLY SHIT WHY YOU HAVE SWEDISH COLORS?!

Fixed Zombie Zeal Cloakers having swedish textures
-Added Summers and his Co. back to Boiling Point
-Added Winters to First World Bank (i did some tests here and he works good here)

---
## [haruka98/keyboard-sounds-cpp](https://github.com/haruka98/keyboard-sounds-cpp)@[3169ee6723...](https://github.com/haruka98/keyboard-sounds-cpp/commit/3169ee67234c1c8fcb88ec7d1e6aa4a935da51f9)
#### Wednesday 2022-02-16 18:55:30 by Lilly meow

fuck you

Signed-off-by: Lilly <justsweetluna@gmail.com>

---
## [Appboy/dd-trace-rb](https://github.com/Appboy/dd-trace-rb)@[3fef0d3e0c...](https://github.com/Appboy/dd-trace-rb/commit/3fef0d3e0c104fda8e7fcfee6298e82c2a7f3ae7)
#### Wednesday 2022-02-16 19:27:15 by Ivo Anjo

[PROF-3425] Bootstrap profiling native extension

My current plan is to use the profiling native extension to:

* Enable use of libddprof, a (native) shared library which allows
  datadog profilers to share common code.

  One of the main advantages of this library is that it will include
  its own profile encoding implementation, which will enable us to
  drop profiler's dependency on the `google-protobuf` gem.
  Right now, we need to tell customers to manually it when onboarding,
  see <https://docs.datadoghq.com/tracing/profiler/enabling/?code-lang=ruby>,
  which is annoying.

* Call Ruby VM APIs that are otherwise unavailable or costly when
  called from Ruby code.

But in this commit, I decided to scale it way, way, way back to
just the basics: add an empty native extension, and the
scaffolding to load and test it.

Thus, I hope that by releasing the next version of dd-trace-rb
with the empty native extension we can to validate the approach,
or otherwise root out corner cases that we may have missed.

Furthermore, I'll point out that if our plans of a "big gem" go
forward, having this kind of non-trivial addition on the gem
is supposed to be the norm, not the exception ;)

---

EVEN SO, because this is a non-trivial change, here's my notes on
possible concerns, in Q&A form:

**Q1**: Will requiring customers to compile a native extension during
        `gem install ddtrace` cause issues?

**A1**: No, because of our dependencies. dd-trace-rb currently has
two dependencies: `ffi` and `msgpack`. Both of those gems rely on
native components, and neither of them (as of this writing) ships
pre-compiled extensions (*except on Windows), as can be seen on
rubygems.org:

* <https://rubygems.org/gems/ffi/versions>
* <https://rubygems.org/gems/msgpack/versions>

This fortunate state of affairs means that customers already need
to have a working setup for building native extensions, and so our
addition of a native extension does not make it any harder for them
to onboard.

**Q2**: Will this cause problems for Windows users?
**A2**: The `ffi` and `msgpack` gem ship precompiled binaries for
Windows, so the reasoning from A1 doesn't apply to these users.

For Windows, it's possible that customers that previously
were getting by without needing an environment to build Ruby native
extensions will no longer be able to install dd-trace-rb.
But:

* `gem install rails` on Windows pulls at least one native
  extension that needs to be compiled, so if you can't build
  dd-trace-rb, you can't install `rails` either
* Recent versions of `msgpack` (since 1.4.2, from 2021-02-01)
  don't provide binaries either. This means that, out of the
  box, even before this change, `gem install ddtrace` fails
  on Windows if you don't have a build environment, because
  rubygems tries to download the latest version of `msgpack`.
  (Rather than picking an older version that ships a precompiled
  build.)

So my assertion is, I don't believe we'll have any customers
that A) run on Windows and B) don't have a setup for building
native extensions.

BUT, if this assertion turns out to be wrong, we have the option
of doing the same thing that `ffi` and `msgpack` do: ship
prebuilt versions of `ddtrace` for Windows users.

**Q3**: Should we provide precompiled versions of the gem right now instead?
**A3**: Precompiled versions of the gem introduce complexity into
our release process (now we have several artifacts, that may
need to be generated on multiple machines); it also may pose
compatibility issues, given our Ruby 2.1 to 3.0 support Matrix.

So, given the fortunate state we're in (see A1), I think we should
avoid them as much as possible.

**Q4**: Why write the extension in C and not Rust?
**A4**: The Ruby VM APIs and headers are written in C. They cannot be
directly used from Rust (e.g. a few things are actually implemented
as preprocessor macros), and thus, to write an extension using Rust,
we'd need to rely on community-built bindings that translate the
Ruby VM headers into Rust.

I've investigated the state of these bindings, and the only two
that are still maintained are:

* https://crates.io/crates/rosy
* https://crates.io/crates/rutie

Unfortunately, there don't seem to be a lot of gems using them and
support for older Rubies, 32-bit OSs and Windows seems spotty.
So... not in a great state at the moment for our usage.

The second issue is that using Rust pushes us into needing to
provide binary builds through rubygems.org -- we definitely can't
assume that customers will have a working Rust compiler around.

We plan on implementing libddprof (the profiling shared library)
using Rust, but because it doesn't need to talk to Ruby VM APIs
(we'll wrap them with some C code in this profiling native extension),
we don't need to worry about bindings, and also we get a bit more
flexibility on binary builds, since we don't need to link to the
Ruby VM from Rust code.

**Q5**: Can you use dd-trace-rb without the native extension?
**A5**: Yes...ish. The extension must get built during `gem install`,
but we handle any issues that may happen while loading it.
So, if you're working on the gem, or the extension gets built
but doesn't load properly, there should be no impact to the rest
of the library; only the profiler will refuse to work.

**Q6**: Will this impact JRuby users?
**A6**: No. We'll skip trying to compile and load the native
extension on JRuby. (Profiling is anyway not supported on JRuby).

---
## [Ebin-Halcyon/Shiptest](https://github.com/Ebin-Halcyon/Shiptest)@[5e29827ceb...](https://github.com/Ebin-Halcyon/Shiptest/commit/5e29827cebbb7cd08d4bf5b210675526f324bf6d)
#### Wednesday 2022-02-16 19:46:19 by Zephyr

Spacemandmm fixes (#799)

* do it

Signed-off-by: Matthew <matthew@tfaluc.com>

* little more detail here

Signed-off-by: Matthew <matthew@tfaluc.com>

* put it in the wrong dmi

Signed-off-by: Matthew <matthew@tfaluc.com>

* Update code/game/objects/items/tools/chisel.dm

Copy paste gp BRRR

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

* resolve some issues that spacemandmm is complaining about because got fucking damn is it annoying when I am trying to code something and I get nonstop errors about stupid issues. also did you know that people though rand was exclusive on the high end? its actually not, both params are inclusive, which is stupid since this is different to almost every other god damn language

Signed-off-by: Matthew <matthew@tfaluc.com>

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

---
## [Perkedel/IvanC-MIDI-Play-Plugin](https://github.com/Perkedel/IvanC-MIDI-Play-Plugin)@[e98b906507...](https://github.com/Perkedel/IvanC-MIDI-Play-Plugin/commit/e98b9065079e24f5d891ec8bcf605457aa885ce1)
#### Wednesday 2022-02-16 20:07:01 by Joel Robert Justiawan

adissu's Loop pefeya

installed loop based on adissu's work on the loop. sorry, I have to... find ways to playhead.

https://forum.juce.com/t/how-to-loop-midi-file/33837/10?u=joelwindows7

PAIN IS TEMPORARY, GLORY IS FOREVER lol Wintergatan

We got more finding with bespoke!

re expand the tutorial to be even more beginner friendly as more as possible.

---
## [Perkedel/IvanC-MIDI-Play-Plugin](https://github.com/Perkedel/IvanC-MIDI-Play-Plugin)@[d844c9b79a...](https://github.com/Perkedel/IvanC-MIDI-Play-Plugin/commit/d844c9b79a62e8da8fdc116601d440ca84f9ab3c)
#### Wednesday 2022-02-16 20:14:30 by Joel Robert Justiawan

Oh yeah one more note

Did you know, I have to be scammed by kushview just to get that Element working. Yep, I paid once for it that version. Remember folks, don't ever buy this! No, not the quality or what. Buying once only grants 1 version that's it. the download expires in 14 days after checkout. to have latest version all the time, you must subscribe. sell your soul.

Doesn't mean I encourage sparsdat game, NO NO NO! This is about Adobe level of soul hostage! There is no lifetime always latest version of this kushview Element.

Don't confuse Element with Riot chat! that's different.

also I saw a bit of trouble with Vital VSTi. contents si more is paid and I felt it absurd except of course text to synth (which is computationally expensive & is done on Vital server to achieve, make sense). I suggest you check Vitalium. but that doesn't mean you shall not try Vital itself. Vitalium is fork of Vital, because Matt does not like users contribution. pls link unfa's video, Difference between Vital & Vitalium.

Taviar!

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[04fac05ccc...](https://github.com/san7890/bruhstation/commit/04fac05ccc898697e9391979fe7c9439c25f7827)
#### Wednesday 2022-02-16 20:24:27 by san7890

The Science Lobby; Or, How I Learned To Embrace Congruence

This is a multi-factorial PR in a broader series meant to address the fact that areas are too massive. Today's episode includes the following:

This section of the halls are just incredulously fucking massive. I think the reasoning behind this (I may be wrong) is that no one bothered to make an area/sprite for the very distinct Science Lobby on Delta (as well as Meta and Tram). This PR is someone bothering.

To achieve good symmetry, I also made the area colloquially known as the Medbay Lobby it's own area as well with the already-existing area. Had to shuffle some stuff around, but I think it's not incredibly ugly. Peep a look:

---
## [exordium-vic3/exordium-vic3.github.io](https://github.com/exordium-vic3/exordium-vic3.github.io)@[143d8334f0...](https://github.com/exordium-vic3/exordium-vic3.github.io/commit/143d8334f05734d8758187aa7cd23a1611277a3a)
#### Wednesday 2022-02-16 20:40:17 by exordium-vic3

Tell 😑👀 the men I'm 🙋 coming 🍆 Tell 🗣🗣 them 🤔🎆 count 🙌💯 the 👏👏 days ⏰⌛ I 😏 can 🔫🔫 feel the 👏❤ night 🌃🕕 passing by 👏 like a ❗👏 mistake ✌😷 waiting ⌚ for me 😭 Caught up in my 👈 feelings 😭💕 Overthink the truth 😍😍 Fantasize you've left 👈👈 me behind ↩ and 💰🚟 I'm 🙋🙅 turned 🔄↪ back running for 🔄 you 👀 Make 🖌💰 it 💡 up ❤ to me, 🏻 you 👳 know 🤔 it's 👉💦 better Make 👊 it up 👆⬆ to 📴 me, you 🤓 know 🤔💼 it's 😮✋ better 💋👎 Be sweet 🍬💦 to 😊 me, 🏣😥 baby 🏻👶 I wanna 😡🙇 believe 😏😨 in you, 👉 I 👁👁 wanna believe (Be sweet) 💦 Be 💰 sweet 🍭💜 to 👉🌅 me, baby I wanna believe in you, 😍👼 I wanna 😏🙈 believe in 👈👇 something 👱 So come and 👏 get 🎆 your 👖🏻 woman 👧😂 (Come and 🅱➕ get your woman) 👩💁 Pacify her rage (Pacify her 😘 rage) Take the 🌊 time ⏰ to 💰💦 undo your 🏾 lies, make 🖕👏 it up once 💯 more 😒 with feeling 😩 Recognize your 👏 mistakes and I'll let 👌✋ you ☝ back 😯🏼 in Realize 😎🤔 not 👎❌ too 👌🍆 late, ⏰ loved you ♀ always 🕰⏳ Make ☝📓 it up 🙆⬆ to me, 👈💑 you know it's 🐈 better ↗🐬 Make 😤 it up ⬆🔺 to 😥 me, 😭🙋 you know it's better 👊 Be ❌👏 sweet 🍬 to ♀💰 me, ⓜ baby ❗👶 I wanna 😯 believe 🙊🌈 in you, 🏃 I 👀🏋 wanna ♀🏿 believe (Be 🐝🐝 sweet) 😝 Be sweet 🍑🍯 to 🔟 me, 👨🙋 baby 🏿👼 I 👀 wanna 😤 believe 😱 in you, 🔥‼ I 😂🙋 wanna believe 🔯⁉ in 👏👻 something 💦 Be 👬🐝 sweet 😱🍬 to 👌 me, 💦😍 baby 👼 I wanna 😤 believe in you, I 💘 wanna 😯 believe 🏻🙏 (Be 👌🐝 sweet) Be sweet 🍗 to 🎲 me, baby 😫🏻 I wanna believe 💭🙌 in 👇 you, I ♂ wanna believe 🏻 in 📥 something 👈

---
## [crccheck/dotfiles](https://github.com/crccheck/dotfiles)@[b6078fa4d6...](https://github.com/crccheck/dotfiles/commit/b6078fa4d6ebda06ac3ad3e77bbd56a0c72468f9)
#### Wednesday 2022-02-16 20:53:17 by Chris Chang

Fuck you, Apple (#3)

* random dotfile config tweaks

* checkin iterm

* delete some obsolete helper bin

* updates so far

* fix title was stripping too much

* add miro window manager

* learning hammerspoon, enable numpad keys

* get middle screen working

* fucking piece of shit

---
## [mapmeld/determined](https://github.com/mapmeld/determined)@[08888717a6...](https://github.com/mapmeld/determined/commit/08888717a6db21304115cd119ebb5d926d51c88e)
#### Wednesday 2022-02-16 21:57:14 by Bradley Laney

feat: unify task logs [DET-6062, DET-6063, DET-6064, DET-6065, DET-6066] (#3070)

This change adds persistent logs for all task types (well, all except poor old checkpoint GC). This means that logs are written to the logging back-end as configured in the master (PostgreSQL through master or Elastic) by Fluentbit and accessible through APIs in the master that translate reads to the back-end's language. To allow for this change, many other changes were required. A (probably) non-exhaustive list follows:
* Trial logs used to go to a `trial_logs` table or index. I tried to not tear the codebase asunder forever with trials and the others using different tables/queries/structs/etc everywhere. Existing tasks were marked has having `log_version == 0` and the old `trial_logs` table now serves logs those tasks (only trials). From now on, all tasks are written with `log_version == 1` and queries for their logs are routed to the `task_logs` table. The old trial logs table (now the `log_version == 0` table) is mothballed - it (mostly) shouldn't be touched again and the old logs should load from there fine forever while new features can be built on the new table. There were alternatives besides leaving trials and task logs separate forever that I shied away from; e.g., I considered a migration to update the trial logs table to schema of the task logs table, but since we access task logs by task_id, this would require rewriting the index on trial_id or adding one on task_id which is too expensive for a migration. This solution balances complexity, maintainability and migration cost.
* Because task logs went through the master, we were free to built features like readiness checks on top of them. Now that they don't, before logs leave the container a small helper script skims them, checks for the readiness logs and posts readiness to a new API. I considered alternatives here, too, like reading the logs back in on the master side, but that incurs a lot more overhead I felt this was more flexible anyway.
* The old events endpoint used to return logs, now it doesn't. This was because it (the eventManager that backed the endpoint) used to _store_ the logs, and now it doesn’t. In my opinion, the work to read the log stream and the old event stream and merge them is low value and annoying. Users should just prefer the new `/api/v1/tasks/:id/logs` endpoint for logs and rely on events to get the few task events that were relied on. Events will likely be supplanted by a task state watcher of some time so webui/cli can just watch for the readiness bit to flip.

---
## [SaintPatricksGitcoin/LibAFL](https://github.com/SaintPatricksGitcoin/LibAFL)@[a0ce4cfd68...](https://github.com/SaintPatricksGitcoin/LibAFL/commit/a0ce4cfd68ef3ab428d2e8398030c83e6992cc45)
#### Wednesday 2022-02-16 22:21:49 by Dominik Maier

Ignored qemu fuzzer for non-linux (#397)

* ignored qemu fuzzer for non-linux

* fixed cfg

* ignore rm -rf errors in make short_test (fuck you macos)

Co-authored-by: Andrea Fioraldi <andreafioraldi@gmail.com>

---
## [Le-Technologue/minishell](https://github.com/Le-Technologue/minishell)@[ae61181be1...](https://github.com/Le-Technologue/minishell/commit/ae61181be1ec6a81f545e23316fa89bec5cb8a7c)
#### Wednesday 2022-02-16 23:07:02 by William Cazorla

Refactoring context stack, many fixes...
- Sorry this is a big one, got lost a little in the debugging. But I'll
  try to make sense of it.
- I chose to refactor the context stack, in a more containerized, object
  manner, to avoid mistakes and to redo the dark magic of the interpreter
  loop end conditions in a more explicit and consciencious way.
- I had to do the complete_pipe function right now in order to exit the
  interpreter loop definitely and gracefully, by actually emptying the
  context stack to signal for its end!
- While doing so I broke a few things, but I fixed many more in the end.
- I ended end modularising some more, and I tried to put the exceptions
  checks closer to the parsing functions causing them, instead of having
  to rely on a single clusterfuck boolean formula at the end of the
  interpreter loop or buried inside the data storage functions.
- I added testing functions to print the context stack during the
  debugging.
- One nasty mistake I made was to forgot some wording pushes upon
  meeting pipe chars, also using a >= REDIREC check for pipe syntax errors,
  which occulted WORD, which is higher than REDIREC... I'll pin that on
  my lack of sleep and try to fix it now.

---
## [CalrethilOfMirkwood/FeanorBot](https://github.com/CalrethilOfMirkwood/FeanorBot)@[081ce8e26f...](https://github.com/CalrethilOfMirkwood/FeanorBot/commit/081ce8e26f26916e7aebcfd7c6ed283c0641de2b)
#### Wednesday 2022-02-16 23:58:57 by Sophie Park

amino furry noldo anime +18 rolplay chat

What the fuck did you just fucking say to me, you little shit? I’ll have you know I am the top Tolkien scholar on the Internet, and I’ve won numerous Balrog-related disputes, and I have over 300 confirmed re-reads of The Silmarillion. I am trained in Bombadilian slam poetry and I’m the top Sindarin linguist on madghosts. You are nothing to me but just another seventh age pleb. I will smite you with precision the likes of which has never been seen before on Middle Earth, mark my fucking words. You think you can get away with saying you read and enjoyed Tolkien’s work to me over the Internet? Think again, dotard. As we speak, I’m gathering an alliance of wroth and ruin to avenge this misdeed so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can ace trivia anywhere, anytime, and I can list each character’s seven hundred names, and that’s just off the top of my head. Not only am I extensively trained in literary analysis, but I have memorized the entire works of Tolkien and I will use it to its full extent to sunder your miserable ass from the face of Arda like Numenor and Beleriand, you fell shit. If only you could have known what unholy doom your little clever comment was about to bring down upon you, maybe you would have held your forked fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re going straight to the fucking void, kiddo.

---

