## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-26](docs/good-messages/2022/2022-07-26.md)


1,982,320 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,982,320 were push events containing 3,004,989 commit messages that amount to 226,322,001 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 59 messages:


## [Oyu-De/Paradise](https://github.com/Oyu-De/Paradise)@[fd5580307e...](https://github.com/Oyu-De/Paradise/commit/fd5580307e1d3a2821ae8b2f26cb04cdcd139f87)
#### Tuesday 2022-07-26 02:07:56 by Contrabang

Adds a blue overlay to scrying orb users. Spirit realm and scrying orb users now have a special description instead of being catatonic (#18366)

* holy shit blue ghosts

* lets fix that

* you cant see it if its not in ya hand

* Their glowing red eyes are glazed over

* farie review

* farie review pt 2

---
## [mrpibb4201337/mojave-sun-13](https://github.com/mrpibb4201337/mojave-sun-13)@[2996f41136...](https://github.com/mrpibb4201337/mojave-sun-13/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Tuesday 2022-07-26 02:17:17 by EdwardNashton

Update Time: Machinery to People (#2096)

* Update Time: Machinery to People

Added a recorders and server racks all over the city.

Slightly changed a "Cheap Motel" near Police Dept.

Slightly changed Police Dept.

Slightly updated Chemical Factory and Weather Station.

* Update time: small fixes

Changed a servers on Power Plant.

* Update Time: that god damn room in PD

I hope we're done with it.

* Update Time: small fix

Removed a potential feature with "shutter trap" in PD.

* Update Time: fixes and updating Water Treatment Station

You made me do this, Original.

* Update Time: one day the south dir comes, we'll place our stuff and go

Sometimes you get too picky

Co-authored-by: Edward Nashton <eddienigma48@gmail.com>

---
## [moon-java/mitigation-timeline](https://github.com/moon-java/mitigation-timeline)@[66bdd1e258...](https://github.com/moon-java/mitigation-timeline/commit/66bdd1e258ab7d2c80fdf3468e12dbe3a3c8cc4b)
#### Tuesday 2022-07-26 02:33:38 by moon-java

DSR timelines are done, holy fuck

plus a shitty little script for converting excel spreadsheets into js timelines and an example sheet

---
## [AlvCyktor/Yogstation](https://github.com/AlvCyktor/Yogstation)@[5bbc6a2401...](https://github.com/AlvCyktor/Yogstation/commit/5bbc6a2401361e71f4c6fb0ad173900153603787)
#### Tuesday 2022-07-26 03:14:52 by Marmio64

Sinful demon changes + re-enable (#14345)

* first wave of demon changes

many changes
1: gluttonous demons hunger 3x as fast as normal people
2: all demons no longer enter softcrit (still can enter hardcrit), are geneless, dont suffocate in crit, and have stable hearts.
3: true demon form deals 20 damage instead of 24 (wrath is 24 instead of 28). Health is lowered to 160 and health regen per hit is now 8 instead of 10. To compensate, they are ever so slightly faster, but are still slower than everyone but podpeople. Demons also lose 2 hp every life tick (a life tick is generally 2 seconds, so 2 hp every 2 seconds), so as to try to deter you from staying in demon form the entire round.
4: objectives are made a bit less murderbone-ey.
5: sinful demon spawns slightly less often

* re enables event

* fixes

* removes chance for envy to get an identity theft objective

* word change

* sinful demon is rarer still

honestly, they arent very interesting if they happen too much, so i'd like them to mildly rare

Co-authored-by: Jamie D <993128+JamieD1@users.noreply.github.com>

---
## [hejohns/.rc](https://github.com/hejohns/.rc)@[a92ce5725b...](https://github.com/hejohns/.rc/commit/a92ce5725b6fa9e92b14842864c20a1800a0e50a)
#### Tuesday 2022-07-26 03:28:35 by hejohns

This is incredibly stupid but it's better now

I managed to spend 6 hours configuring latex fonts, then title
formatting
I hate myself but at least it looks better now
I also went through all my books to find font names
palatino and sabon were the two fonts that were disclosed

---
## [sergiogallegos/terminal](https://github.com/sergiogallegos/terminal)@[9ccd6ecd74...](https://github.com/sergiogallegos/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Tuesday 2022-07-26 03:36:18 by Mike Griese

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
## [anrui2032-OpenSource/android_kernel_oppo_msm8939](https://github.com/anrui2032-OpenSource/android_kernel_oppo_msm8939)@[8706ba85b7...](https://github.com/anrui2032-OpenSource/android_kernel_oppo_msm8939/commit/8706ba85b7efaa646dd885a3fa9bf4b489a4c823)
#### Tuesday 2022-07-26 04:16:24 by Masahiro Yamada

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
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kevin F. Haggerty <haggertk@lineageos.org>
Change-Id: Ic632eaa7777338109f80c76535e67917f5b9761c

---
## [newstools/2022-the-star](https://github.com/newstools/2022-the-star)@[e50d6e9033...](https://github.com/newstools/2022-the-star/commit/e50d6e90330cff51848879ae448551e01c3587ef)
#### Tuesday 2022-07-26 04:37:24 by Billy Einkamerer

Created Text For URL [www.the-star.co.ke/sasa/entertainment/2022-07-25-stivo-simple-boy-proposes-to-his-girlfriend/]

---
## [LordSaladin/CHOMPStation2](https://github.com/LordSaladin/CHOMPStation2)@[4704df506b...](https://github.com/LordSaladin/CHOMPStation2/commit/4704df506bfccd3f4ef9d75a3cf1a4f6f63ca4e3)
#### Tuesday 2022-07-26 05:02:50 by Victor Zisthus

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
## [andmeics/gcc](https://github.com/andmeics/gcc)@[5493ee7145...](https://github.com/andmeics/gcc/commit/5493ee7145a05dc32bc6d802da2f8237293012d3)
#### Tuesday 2022-07-26 06:18:06 by Alexandre Oliva

i386 testsuite: cope with --enable-default-pie

Running the testsuite on a toolchain build with --enable-default-pie
had some unexpected fails.  Adjust the tests to tolerate the effects
of this configuration option on x86_64-linux-gnu and i686-linux-gnu.

The cet-sjlj* tests get offsets before the base symbol name with PIC
or PIE.  A single pattern covering both alternatives somehow triggered
two matches rather than the single expected match, thus my narrowing
the '.*' to not skip line breaks, but that was not enough.  Still
puzzled, I separated the patterns into nonpic and !nonpic, and we get
the expected matchcounts this way.

Tests for -mfentry require an mfentry effective target, which excludes
32-bit x86 with PIC or PIE enabled, that's why the patterns that
accept the PIC sym@RELOC annotations only cover x86_64.  mvc7 is
getting regexps extended to cover PIC reloc annotatios and all of the
named variants, and tightened to avoid unexpected '.' matches.

The pr24414 test stores in an unadorned named variable in an old-style
asm statement, to check that such asm statements get an implicit
memory clobber.  Rewriting the asm into a GCC extended asm with the
variable as an output would remove the regression it checks against.
Problem is, the literal reference to the variable is not PIC, so it's
rejected by the elf64 linker with an error, and flagged with a warning
by the elf32 one.  We could presumably make the variable references
PIC-friendly with #ifdefs, but I doubt that's worth the trouble.  I'm
just arranging for the test to be skipped if PIC or PIE are enabled by
default.


for  gcc/testsuite/ChangeLog

	* gcc.target/i386/cet-sjlj-6a.c: Cope with --enable-default-pie.
	* gcc.target/i386/cet-sjlj-6b.c: Likewise.
	* gcc.target/i386/fentryname3.c: Likewise.
	* gcc.target/i386/mvc7.c: Likewise.
	* gcc.target/i386/pr24414.c: Likewise.
	* gcc.target/i386/pr93492-3.c: Likewise.
	* gcc.target/i386/pr93492-5.c: Likewise.
	* gcc.target/i386/pr98482-1.c: Likewise.

---
## [kutemeikito/android_kernel_xiaomi_ginkgo](https://github.com/kutemeikito/android_kernel_xiaomi_ginkgo)@[94dcc8ba0f...](https://github.com/kutemeikito/android_kernel_xiaomi_ginkgo/commit/94dcc8ba0f832418c3bde81fad8dbb1ca25feaaf)
#### Tuesday 2022-07-26 06:42:04 by Peter Zijlstra

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
Signed-off-by: Fiqri Ardyansyah <fiqri15072019@gmail.com>
Signed-off-by: Edwiin Kusuma Jaya <kutemeikito0905@gmail.com>

---
## [JihadZoabi/Aleph](https://github.com/JihadZoabi/Aleph)@[0e026863f1...](https://github.com/JihadZoabi/Aleph/commit/0e026863f11b16a753c6c48e527b5908a7b6a505)
#### Tuesday 2022-07-26 07:09:49 by Eyal Z

The Sun is, by far, the nearest star to Earth. The distance from Earth to Sun is
150 million kilometers (km), which equals
1 astronomical unit (AU), which equals
8.3 light minutes (that is, the distance traveled by light in 8.3 minutes).
By contrast, the distance from Earth to Proxima Centauri (the next nearest star) is
40 trillion kilometers, which equals
270,000 astronomical units, which equals
4.2 light years (ly).
It's much easier to study the nearby Sun than the much-more-distant other stars.
The Sun is made of dense gas. The average density of the Sun is about 1400 kilograms per cubic meter, 40 percent greater than the density of water. The Sun remains gaseous (rather than liquid or solid) at these high densities because of its extraordinarily high temperature, which prevents the ions within the Sun from bonding together. The gas of which the Sun is made is mostly ionized hydrogen and ionized helium, the two simplest chemical elements. The Sun thus contains positively charged hydrogen nuclei, positively charged helium nuclei, and negatively charged electrons. Because photons scatter readily from free electrons, the Sun is opaque (you can't see through the Sun to see the stars behind it).

As you know from Astronomy 161, a hot, dense, opaque object (such as the Sun, or the filament of a light bulb) produces a continuous blackbody spectrum of light. The temperature at the Sun's surface is 5800 Kelvin; the Sun's blackbody spectrum thus peaks at a wavelength of 500 nanometers, in the visible range of the spectrum. [For a review of blackbody radiation, see chapter 5 of the textbook, or the relevant Astronomy 161 web page.] The luminosity of the Sun (that is, the amount of energy it radiates away per second in the form of light) is very large, thanks to the Sun's high temperature and large surface area. The total luminosity of the Sun is 3.9 x 1026 watts. (That is, 390 trillion trillion watts.)

(2) The Sun remains hot because it is powered by nuclear fusion in its core.
The Sun has been shining away for 4.6 billion years. For well over 3 billion years, according to the fossil record, life has existed on Earth. The fact that life was not scorched or frozen out of existence during that time span indicates that the luminosity of the Sun has been fairly steady. What energy source has kept the Sun hot for billions of years, instead of cooling off like an unplugged iron?
What about chemical sources, such as the burning of hydrogen? (We know there's plenty of hydrogen in the Sun.) Burning one kilogram of hydrogen to form water, by the reaction
2H + O -> H2O + energy,
releases 140 million joules of energy. (The `joule' is the standard unit of energy in the metric system. It is the energy required to keep a 1 watt light bulb lit up for 1 second. 140 million joules is equivalent to 33,000 Calories or 40 kilowatt-hours.) If the Sun consisted entirely of hydrogen (which it doesn't), and if you could find a source of oxygen with which to burn it (never mind where all that oxygen would come from), it could keep the Sun at its present luminosity for a mere 20,000 years.

A more potent energy source is needed to keep the Sun shining for billions of years. What about nuclear fusion? Four hydrogen nuclei can be fused together into a helium nucleus, accompanied by the release of energy:
4H -> He + energy.
Fusing one kilogram of hydrogen into helium releases 630 trillion joules of energy. That's nearly 5 million times what you'd get by burning the same hydrogen to get water. Thus, fusion of hydrogen will keep the Sun shining at a constant luminosity not for 20 thousand years, but for as much as 100 billion years.

(3) When hydrogen is fused into helium, matter is converted into energy.
The Sun, like most stars, is powered by the fusion of hydrogen into helium (what the textbook misleadingly calls `hydrogen burning'). You may well ask, ``Where does all that energy come from when hydrogen is fused into helium? Isn't energy conserved?'' There is another question you can ask. The total mass of four hydrogen nuclei is 6.693 x 10-27 kilograms. The mass of a helium nucleus is 6.645 x 10-27 kilograms. Thus, there is a loss of 0.048 x 10-27 kilograms every time a helium nucleus is formed by fusion. The loss is small, but real. You may then ask, ``Where does that mass go when hydrogen is fused into helium? Isn't mass conserved?''
Albert Einstein provided us with an answer to our questions. He pointed out that mass can be converted into energy, and vice versa. The `exchange rate' between mass and energy is given by the famous equation
E = m c2
where E = energy, m = mass, and c = the speed of light in a vacuum (300,000,000 ometers/second). Thus, the total amount of MASS+ENERGY is conserved.

Every second, as we have seen, the Sun creates E = 3.9 x 1026 joules of energy. To balance the books, every second the Sun destroys m = E/c2 = 4.3 x 109 kilograms of mass. This mass loss, equivalent to more than 4 million tons per second, is accomplished by fusing 600 million tons of hydrogen into 596 million tons of helium.

It should be noted that fusion of atomic nuclei is difficult to initiate. Atomic nuclei are positively charged; thus each nucleus repels each other nucleus. In order to fuse two nuclei together, they must be brought very close together, so that the strong (but short-range) nuclear force that holds nuclei together can do its work. In order for two positively charged nuclei to overcome their electric repulsion and come very close, they have to collide at high speeds. High speeds for individual nuclei imply that the gas in which they exist is very hot (more than 10 million degrees Kelvin). These high temperatures are not found at the Sun's surface, but only in its hot, dense core.

---
## [roboswell/data](https://github.com/roboswell/data)@[7b230d7672...](https://github.com/roboswell/data/commit/7b230d7672c7d809a5a685376e832b98e3e107e8)
#### Tuesday 2022-07-26 07:10:25 by roboswell

World Happiness Report - 2019 Survey Data, Augmented with Data from Other Sources

This csv file contains the data from the 2019 World Happiness Report survey, combined with data from other sources. These additional sources and variables include the following:
The 2019 Legatum Prosperity Index: 
-Adult Skills
-Pre-Primary Education
-Primary Education
-Secondary Education
-Tertiary Education
-Government Effectiveness
-Regulatory Quality (e.g. the level of ease with which companies can enter into and engage in the economy vs. regulatory burdens which may impede economic progress)
-Rule of Law, Behavioural Risk Factors (i.e., measurements of life style risk levels which contribute to overall levels of health, and to the susceptibility to illness, injury, and death among the population of a given country)
-Care Systems (the capacity of the given country to effectively respond to or cure illness once such diseases are already amongst the population)
-Longevity (which includes multiple categories of mortality rates)
-Mental Health (which measures the extent and magnitude of mental health conditions among thhe population)
-Physical Health (which captures the extent and magnitude of physical health conditions affecting the population)
-Preventative Interventions (which measures the level of capacity a country has to prevent illnesses and the spread of disease which could affect mortality rates.)
-Contract Enforcement
-Property Rights
-Basic Services
-Connectedness (which measures the ability of the population to engage in a range of normal activities, physically or digitally)
-Material Resources (capturing the proportion of the population which has the minimum essential income/resources to survive and live well.
-Nutrition (which indicates the level to which diverse healthy food is available to the population)
-Protection from Harm
-Shelter
-Absence of Legal Discrimination
-Social Tolerance
-Politically Related Terror and Violence
-Property Crime
-Terrorism (captures the quantity of attacks, and injuries and fatalities in each country which have resulted, as well as the costs incurred by the economy as a result)
-Violent Crime
-War and Civil Conflict
-Civic and Social Participation
-Institutional Trust
-Interpersonal Trust
-Personal and Family Relationships (which measures the strength and closeness of such relationships, on average, in a given country)
-Social Networks (which measures the strength and closeness of relationships beyond family and friends) 
World Inequality Database:
-"Percent_of_pre-tax_nat_income_of_bottom_50%" - which measures the percent of national income in the hands of the bottom half of the population, and as such is a measure of economic inequality
World Bank World Development Indicators:
-Urban population (% of total population)
UNDP:
-IHDI - The Inequality-Adjusted Human Development Index
Gallup Analytics:
-Answer to survey question: Never a time in past year without money for food (which is based on a worldwide survey question with respect to the last 12 months, for the most recent year up to 2019 in which the question was asked in a given country)
SIPRI's dataset on military spending as a percentage of GDP, and a dataset on overall government spending as a percentage of GDP:
-Non-military government spending as a percent of GDP

---
## [REALHaydenGaming/PE-tutorials](https://github.com/REALHaydenGaming/PE-tutorials)@[30c23187d5...](https://github.com/REALHaydenGaming/PE-tutorials/commit/30c23187d5034a5ce1d414371915e177c522f0bb)
#### Tuesday 2022-07-26 07:35:59 by Not_HaydenGaming

CUSTOM CUM TRANSITION REAL 100%

alright for real, I got that done in 30 minutes, cuz fuck you vs dave revenge 3.5

---
## [REALHaydenGaming/PE-tutorials](https://github.com/REALHaydenGaming/PE-tutorials)@[20f8d5167c...](https://github.com/REALHaydenGaming/PE-tutorials/commit/20f8d5167cb23910fd9fd5d6b0c491d78064345d)
#### Tuesday 2022-07-26 07:37:24 by Not_HaydenGaming

CUSTOM CUM TRANSITION 100% REAL

got that done in 15 minutes, cuz fuck you dave's revenge 3.5

---
## [Sn1p3rr3c0n/RWoM](https://github.com/Sn1p3rr3c0n/RWoM)@[a3fda50b81...](https://github.com/Sn1p3rr3c0n/RWoM/commit/a3fda50b81f45b3b47b1499ec7920ec99d89cea6)
#### Tuesday 2022-07-26 08:04:52 by TorannD

v2.5.7.3 update

New:
 o Summoner Defense Pylon art and sound updates and configuration tweaks courtesy of Djeeshka

Tweaks:
 o Mage light performance improvements
 o Undead auto undraft performance improvements
 o Death retaliation will no longer summon meteors on pawns under a roof
 o Brightmage shooting accuracy penalty reduced
 o Ranger and Sniper now have a small shooting accuracy bonus
 o Elixir can be autocast and will target nearby injured pawns
 o Transcendent thought bonus for the use of magic duration increased 24->60 in-game hours
 o More distinction between Venerated and Abhorrent magic precepts
 o Sentinel health slightly increased
 o Demons will no longer jump to another target if engaged with their target in melee
 o Demon armor rating increased by ~10% and rewards increased
 o Golems will start with a name by default
 o Wandering Lich event earliest start time delayed from 90 days -> 250 days

Bug fixes:
 o Wave of fear causing errors for unique enemies
 o Disabled traits removed from arcane inspiration
 o Dormant Mecha Golem gatling gun requires line of sight to fire
 o Fix for spirit wolf dying in a caravan
 o Faceless will no longer have the option to pick up enchantment gems
 o Psionic dash will automatically cancel if within a cell of the map edge
 o Fixed golem draw depth for various upgrades
 o Golems losing name or settings after being upgraded

---
## [fikono/duckstation](https://github.com/fikono/duckstation)@[f9212363d3...](https://github.com/fikono/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Tuesday 2022-07-26 08:36:50 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---
## [EvilDragonfiend/BeeStation-Hornet-Evildragon](https://github.com/EvilDragonfiend/BeeStation-Hornet-Evildragon)@[3249b4560b...](https://github.com/EvilDragonfiend/BeeStation-Hornet-Evildragon/commit/3249b4560b568fe762f2a695a6427bab7c56c649)
#### Tuesday 2022-07-26 09:28:47 by DrDuckedGoose

Lasso Fix (#7345)

* Merge https://github.com/BeeStation/BeeStation-Hornet into annoying-thing Merge conflicts :)

* Initial - 23 7 22

- Doesn't allow dead mobs to be ridden
- Space walk is now specific to the mob

* Actually Fix It - 23 7 22

* Fuck - 23 7 22

- Fix being able to tame human
- Fix being able to tame the dead

* Update carp_lasso.dm

* You boys fucked buckle code - 23 7 22

* Update carp_lasso.dm

* Update riding.dm

* fix icon - 24 7 22

* Review Changes - 24 7 22

---
## [apache/spark](https://github.com/apache/spark)@[c4c623a3a8...](https://github.com/apache/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Tuesday 2022-07-26 09:37:31 by Hyukjin Kwon

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
## [Poojawa/VOREStation-fork](https://github.com/Poojawa/VOREStation-fork)@[3d00a4cfda...](https://github.com/Poojawa/VOREStation-fork/commit/3d00a4cfda06fd4440ee6460792d423ee60c62a9)
#### Tuesday 2022-07-26 10:00:14 by Poojawa

Finally working as intended

Fuck you, snowflake taste proc. Just. fuck you.

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[63cefdbb5e...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/63cefdbb5e54d27c39c1fe0dc5a93038d67389b9)
#### Tuesday 2022-07-26 10:03:32 by AmyBSOD

Messages

This is what I have to say to people who really think I'd be grateful if they make deconstructed variants of my game (already a sacrilege) and then expect me to be fucking grateful (inexcusable insult). Anyway, the person in question has been added to the list(TM) now, and no apologies or excuses will be considered.

For me, this annoyance has been dealt with now, any attempt to mention such variants or their creators again will result in immediate and permanent bans from the IRC and subreddit for the perpetrators. And now that this is done, we'll once again focus on the only game that matters, which is SLEX, of course.

---
## [15peaces/15-3athena](https://github.com/15peaces/15-3athena)@[2e283b56ec...](https://github.com/15peaces/15-3athena/commit/2e283b56ecf8bb28d14a860354ca53f3eb306e8b)
#### Tuesday 2022-07-26 10:24:43 by 15peaces

== Bug fixing & more ==
=General:
*Merged missing changes from 3ceam rev. 835

*Partial rewrite of the chat system.
-Thanks to @rathena.
-This replaces the old temp-fix for 2015+ clients with the missing zero termination.
-This should also fix some random dcs and visual glitches related to some chat messages (aka random text at the end of some messages)

*Fixed an issue where the attr_fix database was not read correctly, causing element calculations to be wrong.

*Gold Thief Bug card / Wand of Hermode now blocks the following status's....
-Adoramus / Imprison / Manhole / Chaos (Chaos Panic) / Bloody Lust / Insignia's / Blood Sucker.

=Skills:
*WL_HELLINFERNO
-Recoded the skill.
-Now deals 2 seprate hits of damage.
-The first hit is fire damage and the 2nd hit is shadow damage.
-Chance of burning now only applies to the fire damage.
-Magic Power status now properly increases the damage of both hits.

*RA_ELECTRICSHOCKER
-Official duration reduction formula added.

*SR_FALLENEMPIRE
-Now uses its official status and prevents regular attacking and movement.

*WM_DANCE_WITH_WUG
-Now gives a ATK bonus to Ranger/Minstrel/Wanderer type jobs.

*SO_VACUUM_EXTREME
-Recoded the skill.
-Affected enemy's will now be pulled to the center of the AoE.
-Duration of status is now that of the AoE's remaining active time.
-Duration reduction formula updated to official.
-No longer affects those in Hallucination Walk or Hovering status.
-Note: The durations basicly act as strength power.
-The Vacuum's strength is affected by skill level and weakens over time as the AoE is active. The higher your STR, the stronger the vacuum's suction strength you can resist. 120 STR for example lets you resist a vacuum that has a duration or 6
-seconds or less remaining.

*GN_SPORE_EXPLOSION
-Recoded the skill.
-Countdown now handled the same way like Venom Splasher.
-Target carrying the spore bomb will always be hit by the explosion.
-The explosion animation will now only appear on the exploading target.

*AB_OFFERTORIUM
-Now removes the following status's from the caster....
-Poison / Curse / Confusion / Blind / Bleeding / Burning / Frost / Hallucination / Mandragora / Guillotine Cross Poisons (Except Oblivion).

---
## [avar/git](https://github.com/avar/git)@[6a40c781a3...](https://github.com/avar/git/commit/6a40c781a382ba5fb3ae11e8e75bcffd3c6afa64)
#### Tuesday 2022-07-26 10:46:49 by Ævar Arnfjörð Bjarmason

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

---
## [Trilbyspaceclone/sojourn-station](https://github.com/Trilbyspaceclone/sojourn-station)@[ef4665ec90...](https://github.com/Trilbyspaceclone/sojourn-station/commit/ef4665ec90474cf5ac5f6aff34b6fd30e365429d)
#### Tuesday 2022-07-26 11:16:04 by DimmaDunk

I HATE LIVERMED, I HATE LIVERMED, I HATE LIVERMED!!! (#3714)

* Makes combat medical kits better

- Replaces Dylovene pill bottle on Combat Medical Kit with Carthatoline pill bottle, as every chem inside it already WAS an upgrade over their normal counterparts, making it better at halting toxins damage and preventing liver from killing you. Also adds a Sanguinum syrette to stave off massive bloodloss which would cause the former as well.
- Replaces one of the Quicklot syrettes with a Sanguinum syrette on the Oxygen Deprivation First Aid Kit for better treatment of causes of oxyloss.
- Standardizes pill icons based on chem colors across all pre-built pills for easier reognition.
- Guarantees the "skill issue/salt PR" tag since it doesn't fix underlying issues of current medical system

* Adds carthatoline pills to deferred and corpsman large kit

Keeping in line with the rest of the PR.

* Blood regen pills!

- Adds pre-made Ferritin-Hemosiderin pills composed of iron and protein to help regenerate lost blood
- Replaces Sanguinum syrette on combat kit with ferritin-hemosiderin pill bottle
- Combat surgery kits now really hold advanced tools (except bone gel since the adv version is Soteria made)
- Makes the advanced bone gel item description not a copypaste of its stock counterpart

* Forgot a comma

Damn my haste.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d8d830dc12...](https://github.com/mrakgr/The-Spiral-Language/commit/d8d830dc124e18f08a71ac08bab12fc7903d7fb9)
#### Tuesday 2022-07-26 11:22:44 by Marko Grdinić

"7:50am. I am up.

7:55am. I think this might be a little too early to get up, but it is fine. In 3h, at 11:15am I have an interview with Neurolabs.

8:40am. Let me get started. Let me watch a Python pSql vid.

8:45am. https://www.postgresqltutorial.com/postgresql-python/

No problem, there are tutorials. Let me watch a video first. After the Neurolabs interview who knows what goal I will have. Ideally, I would study a single tech stack like ASP.NET and get a job with it, but that is not realistic. I have to gain proficiency in whatever the employer is using.

8:55am. It really is a drag to seriously try to commit to learning anything right now. I'll go to the NeuroLabs interview in 2h, and no doubt they will have another tech stack.

I do not mind commiting myself to learning something, but I do not want to commit myself to learning several things.

Hopefully, I'll get a mobile today so I can register to AWS and start studying distributed ML on it.

9:05am. https://youtu.be/M2NzvnfS-hI?t=415

I really like this. Note that he just gives the relevant data to a function and gets back the context. Constrast that with .NET where you need to do several magical things.

https://youtu.be/M2NzvnfS-hI?t=579

This way of creating a table is quite straightforward compared to doing migrations.

https://youtu.be/M2NzvnfS-hI?t=742

This is really nice. It is very easy to learn. Still, once you have EF up and running, it would be less type safe and maintainable.

https://youtu.be/M2NzvnfS-hI?t=1126

I see. This is why there is an update, instead of a get and set.

9:30am. https://youtu.be/M2NzvnfS-hI?t=1259

This is a good video. I am very at ease with this sort of programming instead of the .NET stuff.

https://youtu.be/M2NzvnfS-hI?t=1357

The with clause won't close the connection? That feels wrong. I should double check that, but nevermind.

9:40am. This is nice and clean, I do not really feel like studying it for longer. I thought it would be a huge mess like EF.

Incidentally, what I feel like studying more today is EF.

9:45am. Let me just go through the Ishizoku raw and then I'll get started on that. I actually haven't read the mange, so I do not mean to imply that I am catching up. I will pick it up.

10:15am. Dad found one of his old mobiles for me. Now I can get to work on doing what I really want. Also the weather is turning sour and now a cool breeze is blowing through my room. So nice after the sauna like temps of the past week.

Ok, first of all, let me see if I can find a way to create an mToken in the web George app. Then I'll be able to activate the mobile one. This is the most ideal way to spend the morning.

10:20am. Hmmm, I checked my mail and I see I got a reject at Kalepa. I wonder why? Who knows. I didn't expect to get a reject like this, but after some behaviral interview.

I guess I'll move on to the next one.

10:25am. I am distracted. Focus me.

10:30am. No, it is no good. I'll have to make a trip to the bank to get an mToken so I can actiate the mobile George.

10:40am. It will have to be after the interview which is in 35m.

10:45am. What a drag. The only thing I am glad is that HR did not waste my time with an initial HR problem. I feel it is a red flag that the interviewing pipeline has so many behavioral tests. The company feels controling.

10:50am. At this rate, I am going to have to expand my reach. I'll look into AI jobs...

https://ai-jobs.net/

Something like this.

Otherwise I'll have to expand my vision to full stack dev jobs as well as lowering my salary range. Either way is fine. The goal of getting a job is to make money for myself, not to have fun. After 3 years of that I can just transition to trading.

10:50am. Let me read the EF framework tutorial for 10m.

10:55am. Oh wow, there is really huge thunder outside. What do I do now? I might have to reschedule?

11am. I'll reschedule.

12:35pm. I am back. There was a crack of lightning, but it passed almost immediatelly. I could have done the interview. Nevermind that, what is important is that I went to the bank and got that mToken. Let me have breakfast and I'll try registering on AWS again. It might not be George, but simply the mobile being old that was the problem.

1pm. Done with breakfast. Let me try registering on AWS.

FFFFFFFFFFFFFFFFFFFF---Nothing is showing up!

What the hell?

> Što je VISA Secure?
> VISA Secure je besplatna usluga sigurne kupnje debitnim karticama na internetu. Prilikom potvrde online kupnje, korisnik se autentificira, odnosno banci potvrđuje identitet prijavom u mToken biometrijom (PIN telefona, otisak prsta ili prepoznavanje lica na pametnom telefonu).

So do I need to use this Visa secure service?

1:10pm. My bank is really fucking with me here. Let me try calling it again. I think the teller yesterday gave me bad advice. What was the number again?

1:15pm. Everybody is busy, I can't get in touch.

Let me send an email. This time I'll attach a screenshot.

1:20pm. Done. Let me close everything. The thunder is making me nervous."

---
## [snuffop/doomemacs](https://github.com/snuffop/doomemacs)@[b07614037f...](https://github.com/snuffop/doomemacs/commit/b07614037f7670682d2c193d83abdb9eed9f218e)
#### Tuesday 2022-07-26 11:25:24 by TEC

fix(mu4e): support mu 1.8

Thanks to some combination of ignorance and obstinance, mu4e has thrown
compatibility to the wind and completely ignored the exitance of
define-obsolete-function-alias. Coupled with the inconsistent/partial
function renaming, this has made the mu4e 1.6⟶1.8 change particularly
annoying to deal with.

By suffering the pain of doing the mu4e author's work for them, we can
use defalias to give backwards compatibility a good shot for about 60
functions. Some mu4e~x functions are now mu4e--x, others are unchanged,
and then you've got a few odd changes like mu4e~proc -> mu4e--server and
mu4e-search-rerun. The form of message :from entries has also changed,
and a new (mu4e) entrypoint added supplanting mu4e~start.

Fix: #6511
Close: #6549
Co-authored-by: Rahguzar <aikrahguzar@gmail.com>

---
## [mosra/corrade](https://github.com/mosra/corrade)@[41ad045a43...](https://github.com/mosra/corrade/commit/41ad045a439089de35ca2a1be51e20a61a01dd95)
#### Tuesday 2022-07-26 11:33:50 by Vladimír Vondruš

Cpu: give up on extra instruction sets on GCC 4.8.

I was happy when I realized that if I enable a single target and then
include an intrinsics header, the instruction set is then not tied to
other targets enabled at the same time. I.e., if I do

    #pragma GCC push_options
    #pragma GCC target("avx")
    #include <immintrin.h>
    #pragma GCC pop_options

    #pragma GCC push_options
    #pragma GCC target("lzcnt")
    #include <lzcntintrin.h>
    #pragma GCC pop_options

(plus the __AVX__ and __LZCNT__ macro push/pop of course) instead of

    #pragma GCC push_options
    #pragma GCC target("avx")
    #pragma GCC target("lzcnt")
    #include <immintrin.h> // also grabs LZCNT
    #pragma GCC pop_options

then I can use LZCNT without having to enable AVX as well. What I didn't
know back then was that on GCC 4.8 this works the other way as well --
so now I cannot use LZCNT together with AVX, because the compiler
somehow remembers that LZCNT can be used only if target is EXACTLY what
was used at the point when the intrinsics header was included, instead
of if it just CONTAINS that. Haha. Which makes it pretty useless in
practice, since e.g. the String additions I have use LZCNT / TZCNT with
either SSE2 or AVX2. Since SSE2 is implicit, that worked, but as soon I
got to the AVX code path, it no longer did, failing with a linker error.

The commit that makes all this unnecessary on GCC 4.9 is mostly just
header updates, but also two minor code changes, and those changes seem
to be *essential* for this to work. Meaning, I just have no way to make
my use case work with GCC 4.8:
https://github.com/gcc-mirror/gcc/commit/97db2bf7fb10e7eb2e8224e0471b56976f133843

While I could work around this with nasty ifdefs in user code, I feel
like the more robust way is to just not have the CORRADE_ENABLE_ macros
for the extra instruction sets there at all, thus avoiding any further
suffering right from the start. For the "base" instruction sets it seems
fine so far, most probably because there's some inheritance / dependency
between them. I hope I wouldn't need to drop those too.

---
## [OdysiaHallow/coyote-bayou](https://github.com/OdysiaHallow/coyote-bayou)@[eab43e488d...](https://github.com/OdysiaHallow/coyote-bayou/commit/eab43e488d564b0f079d7b0694afac1adb05c907)
#### Tuesday 2022-07-26 11:36:01 by Marrone

Loadout Update

General Description: This PR updates several loadouts for followers, wastelanders, far-landers, and the Redwater faction.

FOLLOWERS CHANGES

STARTING TEXT
- Starting text, including Description, Enforces and Forbids, have been edited to reflect the standard the server wants to see and has also omitted references to NCR and the Legion.
- For Admin and Guard there is slightly different text to match their job descriptions.

LOADOUTS

- Removed CHEMWIZ trait which somehow fixed them not having CHEMWHIZ
- Professors now have Loadouts, two robust options which provide new machine boards to the Followers when they join as part of their loadout. The two loadouts are Environmental Scientist who has hydroponic boards, and Medical Specialist who has a blood bank.

- Specialists have some tweaks to make Medical Researcher more robust by adding a Bluespace syringe and an advanced health analyzer to their loadout.

- Randomly it seems the Volunteer loadout which has tools and construction stuff, had a chemist PDA. This has been removed and now the weakest loadout, the Student, has a PDA.

- Followers Guard had a tweak, the long range loadout has a scope, and the shotgun for the short range loadout has been changed to a police shotgun which is more inline with the aesthetic, and starts with bean bag rounds - though its total capacity is 6 as opposed to the previous 4.

These changes are intended to bring more value and encourage more players to participate in these roles. If you have any suggestions for additions, changes or subtractions let me know in the comments.

WASTELANDER CHANGES

LOADOUTS

Several additions and tweaks have been done to the Wastelander loadouts in order to properly reflect a myriad of playstyles.

- Small changes include, changing a welding helmet to welding goggles, adding extra magazines where there was only 1, tweaking the settler loadout to be more settler-y by giving them glass instead of wood, giving them a more melee focused build that resemble tools, and adding seeds to their loadout.  The Wasteland Medic has been tuned down with salts and surgery bag removed, and the Vaultie has lost their headset radio.

- 10 new Wastelander loadouts have been added, the Gambler which has a lot of interesting RP items, the Vaquero which allows players to explore another aesthetic in-line with the South West, the Hobo loadout for those who want a challenge, the Hombre loadout to replace the desert ranger one so it is more in-line with our current lore and to get away from New Vegas, Ex-Military for those who want to LARP as a soldier or mercenary, a brand new Brotherhood of Steel waster loadout that does not have grenades and is more balanced with other waster loadouts, Eidelon loadout for those who wish to be sneaky and slightly Russian if they so wish, the Aviator loadout to allow players some options to have that air pilot aesthetic, the Trapper loadout for that CLASSIC CLASSIC Fallout experience, and finally the Trouper loadout for all of the bottoms out there.

FAR-LANDER CHANGES

- I have created a whole new set of traits and it took a lot of work, having to do multiple things seven times over and over to make a book that allows you to pick from a list a traitbook which makes it so you can craft one of the seven different former tribes armor and garments. Rejoice!

- The loadouts for Far-Landers have been reduced from 21-3 to 5. To those who wish for aesthetic or loadout options which have been omitted from this decision, let me know and I can tweak some things or add another class since I removed a lot, but they must be more generalized so that specific tribes arent tied to actual loadout options.

REDWATER CHANGES

- Redwater Slave, my favourite job, no longer has explosive collars; they are now shock collars. Aww man, I wanted to be round ended.

- A whole new job was added called Redwater Resident. They will be in charge of supervising and protecting Redwater, and act as inhabitants of the town; they may travel outside of the town to gather materials but otherwise should be staying in the area and around town. They are equipped in quite a robust manner, so anyone who dares to battle the town better be geared to the teeth.

- The Overboss keeps spawning in Nash naked. I fixed this. They now have clothes, and also spawn in Redwater.

---
## [JihadZoabi/Aleph](https://github.com/JihadZoabi/Aleph)@[f84ebc4836...](https://github.com/JihadZoabi/Aleph/commit/f84ebc483618dd3ad7ef87d4d31fb350331dab0e)
#### Tuesday 2022-07-26 11:56:33 by Eyal Z

Turning the other cheek
From Wikipedia, the free encyclopedia
Jump to navigationJump to search

Jesus taught turning the other cheek during the Sermon on the Mount.
Turning the other cheek is a phrase in Christian doctrine from the Sermon on the Mount that refers to responding to injury without revenge and allowing more injury. This passage is variously interpreted as accepting one's predicament, commanding nonresistance or advocating Christian pacifism.

Contents
1	Scriptural references
2	Interpretations
2.1	Christian anarchist interpretation
2.2	Nonviolent resistance interpretation
3	See also
4	References
5	Further reading
6	External links
Scriptural references
The phrase originates from the Sermon on the Mount in the New Testament. In the Gospel of Matthew chapter 5, an alternative for "an eye for an eye" is given by Jesus:

38You have heard that it was said, "An eye for an eye and a tooth for a tooth." 39But I say to you, Do not resist the one who is evil. But if anyone slaps you on the right cheek, turn to him the other also. 40And if anyone would sue you and take your tunic, let him have your cloak as well. 41And if anyone forces you to go one mile, go with him two miles. 42Give to the one who begs from you, and do not refuse the one who would borrow from you.

— Jesus Christ, English Standard Version (Matthew 5:38–42)
In the Sermon on the Plain[1] in the Gospel of Luke chapter 6, as part of his command to "love your enemies", Jesus says:

27But I say to you who hear, Love your enemies, do good to those who hate you, 28bless those who curse you, pray for those who abuse you. 29To one who strikes you on the cheek, offer the other also, and from one who takes away your cloak do not withhold your tunic either. 30Give to everyone who begs from you, and from one who takes away your goods do not demand them back. 31And as you wish that others would do to you, do so to them.

— Jesus Christ, English Standard Version (Luke 6:27–31)
Interpretations
This phrase, as with much of the Sermon on the Mount, has been subject to both literal and figurative interpretations.

Christian anarchist interpretation
Main article: Christian anarchism
According to this interpretation the passages call for total nonresistance to the point of facilitating aggression against oneself, and since human governments defend themselves by military force, some have advocated Christian anarchism, including Leo Tolstoy who elucidated his reasoning in his 1894 book The Kingdom of God Is Within You.

Nonviolent resistance interpretation
The scholar Walter Wink, in his book Engaging the Powers: Discernment and Resistance in a World of Domination, interprets the passage as ways to subvert the power structures of the time.[2]

At the time of Jesus, says Wink, striking backhand a person deemed to be of lower socioeconomic class was a means of asserting authority and dominance. If the persecuted person "turned the other cheek," the discipliner was faced with a dilemma: The left hand was used for unclean purposes, so a back-hand strike on the opposite cheek would not be performed. An alternative would be a slap with the open hand as a challenge or to punch the person, but this was seen as a statement of equality. Thus, by turning the other cheek, the persecuted was demanding equality.

Wink continues with an interpretation of handing over one's cloak in addition to one's tunic. The debtor has given the shirt off his back, a situation forbidden by Hebrew law as stated in Deuteronomy (24:10–13). By giving the lender the cloak as well, the debtor was reduced to nakedness. Wink notes that public nudity was viewed as bringing shame on the viewer, and not just the naked, as seen in Noah's case (Genesis 9:20–23).

Wink interprets the succeeding verse from the Sermon on the Mount as a method for making the oppressor break the law. The commonly invoked Roman law of Angaria allowed the Roman authorities to demand that inhabitants of occupied territories carry messages and equipment the distance of one mile post, but prohibited forcing an individual to go further than a single mile, at the risk of suffering disciplinary actions.[3] In this example, the nonviolent interpretation sees Jesus as placing criticism on an unjust and hated Roman law, as well as clarifying the teaching to extend beyond Jewish law.[4]

---
## [FVRTH3R/Convergence](https://github.com/FVRTH3R/Convergence)@[02c7936421...](https://github.com/FVRTH3R/Convergence/commit/02c79364211e7c8c27ad29beff68b9b526552eca)
#### Tuesday 2022-07-26 12:13:21 by FVRTH3R

oh for fucks sake its 20 god damn 22 why the fuck does the fucking br tag not fucking work and why the fuck does markdown not have fucking alignment yet

---
## [zardoy/vscode-better-snippets](https://github.com/zardoy/vscode-better-snippets)@[1e6f46d2bd...](https://github.com/zardoy/vscode-better-snippets/commit/1e6f46d2bd858b49ffceb3bb5ac8779330e62c0c)
#### Tuesday 2022-07-26 12:56:11 by Vitaly

feat: Trigger Characters! (#16)

presenting you absolutely new feature! Now you can target some snippets to only show after typing specific character!
It wasn't possible before to split snippets into groups, but now you can do this with new `when.triggerCharacters` optional array.
Even if you have quick suggestions enabled, it doesn't mean it would show snippets after typing every character (even space).
What if we wanted to quickly specify true/false after property name or expand it as a method?

```ts
const config = {
  enableFeature
  customMethod
}
```

Here, we have two properties, we want to quickly specify `true` on first and epxand method on second.
Firstly, let's assume that we don't want complicated checks and hacks. No typing snippets.

We could add a snippet to expand it to `true`/method after a single word on the line so we could type space and... the snippet won't appear, yes, because you firstly need to trigger completions and only then you can select it, this can be super annoying

```ts
enableFeature t -> true
```

```json
{
            "name": "t",
            "body": ": true,",
            "when": {
                "lineHasRegex": "^\\s*\\w+ $",
                "triggerCharacters": [
                    " "
                ]
            },
            "replaceTriggerCharacter": true
        },
        // to expand it as method
                {
            "name": "fun",
            "body": "($1) {\n\t$0\n},",
            "when": {
                "lineHasRegex": "^\\s*\\w+ $",
                "triggerCharacters": [
                    " "
                ]
            },
            "replaceTriggerCharacter": true
        },
```

Also, as you can see, we also now have optional `replaceTriggerCharacter` setting, because we want to remove the trigger character (space in our case):

```ts
enableFeature t
enableFeature: true,
```

> You can use `-` or even `:` as a trigger character here

Also, as you can see now, they doesn't suffer with global snippets/completions. And, you also can't get them if you retrigger completions (you need to type space again), so this is ideal for *in-flow* snippets.

In theory it can be also used, as postfix:

```json
        {
            "name": "tChar",
            "body": "translate(0, $0)",
            "when": {
                "lineRegex": "\\wPos.$",
                "triggerCharacters": [
                    "."
                ]
            }
        }
```

// But please, don't, it'll turn into annoyance that you need write dot again. Make sure you specify additional regex.

To also register snippet as regular snippet (so it will also appear after retriggering completions), add empty string to the array of trigger characters:

`triggerCharacters: ['.', '']`

Note, that TS is currently working on providing solutions for usecases from the beginning, but examples above still would be useful for JS.

---
## [IMIO/appy](https://github.com/IMIO/appy)@[e221320300...](https://github.com/IMIO/appy/commit/e221320300f16630b9244e265579a26e704a29df)
#### Tuesday 2022-07-26 13:17:34 by odelaere

literally clone appy like a fucktard because shit is going wild...

---
## [AdvancedProgrammingSUT2022/project-group-04](https://github.com/AdvancedProgrammingSUT2022/project-group-04)@[dc15efe4a2...](https://github.com/AdvancedProgrammingSUT2022/project-group-04/commit/dc15efe4a2231cc0a5f0bd3fbe2c0172bebff754)
#### Tuesday 2022-07-26 15:04:42 by AlirezaRM

there's no time for us. there's no place for us. what is this thing that builds our dreams yet slips away from us. who wants to live forever who wants to live forever oh ooo oh there's no chance for us. It's all decided for us. This world has only one sweet moment aside for us. Who wants to live forever who wants to live forever ooh. Who dares to love forever oh oo woh, When love must die. But touch my tears with your lips. Touch my world with your fingertips And we can have forever And we can love forever ----- FOREVER IS OUR TODAY ----

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[fb723f9b84...](https://github.com/mrakgr/The-Spiral-Language/commit/fb723f9b84476f9d052daa79ced0d2648d35cc1d)
#### Tuesday 2022-07-26 15:20:56 by Marko Grdinić

"2:35pm. I am back. Yesterday, when I was activating the cards, I sent an email asking how. Then I found the option in the George web app and did it. In the meantime I got a reply that I did not read.

But in it turns out there was some pertinent information. It says there is a post activation step where I have to insert a card into a bankomat or a POS device (whatever that is) and then either withdraw money or check my balance. An hour after that, I'll be able to use the card to do online purchasing.

Gahhhhhhh!!!

I though the step I did to activate them yesterday would be enough!

I wish I could say that I should have read the reply, but the desktop version of the George app is bugged and the message wouldn't load in full. I certainly won't waste my time inspecting the source just to extract the wall of text when I've already found the solution. I'll have to make a trip into town again so I can use the bankomat. Nevermind that for now.

2:50pm. https://time.is/GMT+1

I find this site extremely confusing. I should be GMT+1, but this is showing me the time that was an hour ago.

Could this site that is on top of Google be persistently showing me the wrong time. I mean, it can't be that I am wrong about my time zone. It is UTC+1 and not UTC+2 according to what I've set in Windows settings.

https://www.timeanddate.com/worldclock/timezone/utc1

https://24timezones.com/time-zone/cest
> CEST (Central European Summer Time) is one of the well-known names of UTC+2 time zone which is 2h. ahead of UTC (Coordinated Universal Time).The time offset from UTC can be written as +02:00.

2:55pm. What the hell?

I am playing with timezones in Windows.

UTC - 12:55pm.
UTC (+ 00:00) - 1:55pm.
UTC (+ 01:00) - 2:55pm.

Also for some +00:00 options it just shows the regular 12:55pm.

Damn it, Windows timezones are not to be trusted! The locations are right, but the stuff in the parenths isn't!

3pm. It seems the Neurolabs interview was actually at 12:15pm today. I thought it was an hour earlier! Let me double check the AssemblyAI one.

6:30pm UTC. So 8:30pm. in my own timezone.

And the GI interview is at 9:30pm. I am sure of that.

> I am free between 10-19 CEST. Hopefully, the weather won't interfere again.

I'll reschedule the Neurolabs for sometime tomorrow.

3:10pm. It is good that I managed to find this mistake in place. I wonder how I would have reacted today if the weather hadn't interrupted. I'd have come into zoom and wondered why the interviewer isn't coming in for an entire hour. I'd start filling his inbox asking why isn't he coming. I'd probably just give up after half an hour and wash my hands clear of Neurolabs.

The weather saved me today.

I absolutely made the right decision to not risk going through the storm. Imagine if it turned out to be serious, my computer got fried and I got the interview time wrong to boot. That would have been hillarious.

3:15pm. As for Kalepa, given its disfunctionality, I think the most likely case is that the slot simply got filled and I got auto-rejected, but it might simply be that the engineer responsible for the tech interview looked at my commit history, saw me having trouble with mobile phones and cut the thread short. I can't rule it out completely.

Hopefully in the future I'll have more badass stories to tell in these commits, about distributed NNs training. Once I open an AWS account, my next goal will be to get access to Tenstorrent, Groq and Graphcore chips over the cloud. I want to give programming them a try. That would be cool, and might open some doors if I could impress people at those companies with my skills. I'll say I am a Google research engineer playing with these things in my own time.

Got a reply from NeuroLabs.

4pm UTC means 6pm in my own timezone.

Neurolabs: 6pm – 6:45pm, Wed Jul 27, 2022

It seems I'll have two interviews close together. Ok.

Right. First, let me disable the alarm on the old mobile. I do not want it going off at 11am every Tuesday.

3:50pm. I'll make a trip to the city in 5-15m to do the post-activation step.

4:25pm. I am back. I am so mentally drained of this.

I went to the bankomat and activated the cards there. I did the balance check as requested. It seems the web activation was useless.

Now, let me try AWS. If that fails, I'll try it in an hour.

4:30pm. It failed. I'll have to try later.

If that fails, I am not sure what I will do.

4:35pm. Fuck banks, and fuck AWS.

Internet banking was a mistake.

Today my entire day was taken up by this shit, and it is still not done. Will it work in an hour? If it does not, what I will try doing is registering to AWS through my mobile. It is going to be a pain typing in all those passwords over the phone screen, but I will get to the stage where it fails.

Then if it fails again, I will write down the steps, go to the bank again, and have them guide me step by step.

https://www.erstebank.hr/hr/pomoc/help-center/on-line-bankarstvo/george/george-app/kako-potpisujem-transakcije-u-georgeu

> Ako ste se na George Web prijavili mTokenom, transakcije ćete potpisivati push notifikacijom koja će stići na Vaš mobilni uređaj. Ako vam notifikacija nije stigla, otvorite svoj George App i u svom profilu pod mToken potražite „transakcije za potpisivanje“.

Wait, what is this? Translated into English what I have to do is: Open George -> Profile -> mToken -> Transaction Signature Requests.

Let me try again on AWS.

4:45pm. I confirmed that transaction request and managed to complete the AWS registration.

Halleluyah!!!

Now I need to wait for the email that my AWS account has been created.

> Welcome to Amazon Web Services
> For the next 12 months, you'll have free access to core AWS compute, storage, database, and application services within the limits of the Free Tier.

I got in!

4:50pm. I finally cleared this shitty quest.

4:55pm. It feels much better now that I've managed to do what I set out to do for the day. With this I can do what I wanted after I'd completed the C backend - skill up on the cloud.

Tomorrow I'll do some hello world tier programs on the AWS. While I am doing that, on the side I'll investigate whether I can get access to those AI chips via their cloud offerings, assuming they have them.

Let me just state it up front - I am not looking to do the poker player and rock the online dens as before. What I want to do now is just satisfy my curiosity and get some skills programming these things. I really am curious how programming devices with no shared (global) memory would be like. I want to put Spiral to work on that. I have the C backend, so I want to adapt it to the problem.

I could do a genetic programming system on it, and that would be remarkable change in my approach towards ML research, but without the resources to sink into this, I am not expecting much.

I do believe in AI chips. Local memory is a no-brainer and I honestly feel that the chips are suspiciously bad on those ML benchmarks. Maybe for what I want to do, those benchmarks do not matter. I want to investigate that. GPUs certainly wouldn't be good for what I want to do.

5:05pm. I am ashamed of myself. That I failed at poker is one thing.

But if I did it before the NN era, I could very well have suceeded. I would have gone with half symbolic, half evolutionary approach, and that would have worked much better than my current one. Plus because of how I would have approached the challenge, even if I couldn't create a great bot using those techniques, at least I would have been a proper scientist, rather than an embarassment.

With AI chips, I can bridge the path not taken, with my current one.

One other thing - I am applying to ML jobs, but they don't matter too much. It is not like I'll get tasked with making Skynet. Maybe at AssemblyAI I could put my ML library skills to use, but most ML jobs are just doing trivial library things.

I've been thinking, and if it is just for money, I am more attracted to regular programming work than ML at this point. That sort of thing would be halfway challenging.

I used to look down on webdev, but I think exercising my reactive programming skills would be cool. ML is hyped, but it's salaries are not higher than regular dev work despite that. Before I got good at concurrency, I would dread working on frontends, but with my current skills, it seems like a relaxing thing to do.

5:10pm. Well, I'll see how it goes. This Kalepa reject caught me flat footed today, it is like a bullet out of nowhere. I was ready for a battle, but it turns out I'd already lost it.

5:15pm. I used to be sure, but before I get complacent again, I think it would be good to get at least one offer.

My prediction is that at other places, they won't have such a ridiculous amount of behavioral tests in the pipeline. Kalepa fears the autist.

Let me close here for the day, I've ranted enough. Anime, Pathfinder Kingmaker, the usual. I am really enjoying PK with Call of the Wild mod."

---
## [Higgin/tgstation](https://github.com/Higgin/tgstation)@[9428d97a4f...](https://github.com/Higgin/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Tuesday 2022-07-26 15:21:01 by Imaginos16

[MDB IGNORE] The Tilening V2 - Damaged Tile Overlays Edition (#67761)


About The Pull Request

Hello once more! As we near summer, I continued to reminisce on several PRs done throughout last year! One of them was the controversial, but rather positive Tilening V1, as done by me and Twaticus a while back (#58932), and felt I could've done a better job with how it was presented.

And thus, thanks to @Fikou encouraging me with a very interesting find of a previous tile resprite attempt, I've successfully done it!

Ladies and Gentlemen, I present to you all, Tilening Version Two!
image

Now this isn't your run of the mill tile resprite. While I did improve the appearance of several tiles I haven't touched last time (including the showroom/freezer tiles now), I decided to do something special that most mappers shall appreciate!

Don't you hate it when of all damaged states, there's only ones for grey tiles when we have white, black, terracotta and a bunch of other materials? Don't you wish they were overlays instead?

Well golly gee do I have good news for you!
image
image

After painstakingly spending at least several hours trying to learn enough code to pull it off, I have successfully made it so most tiles display transparent versions of damage overlays over them! This means mappers can express their creativity that much better! And thanks to how the code is written, its super easy to snowflake certain tile types to make them use unique damaged states (looking at you wooden tiles), so fret not in that aspect.

Credits to:
@WJohn For actually making those damaged overlays! Wouldn't've done the PR if it wasn't for you.
@dragomagol, @RigglePrime and @LemonInTheDark for helping me out in a VC at 10 PM to 12 AM troubleshooting the code to make this improvement work!
Why It's Good For The Game

The shading is done better as compared to last time, making them feel more cubical and less like a pancake when seen from above! This PR also makes it so that we never ever have to touch damaged tiles ever again potentially, saving up some RSC regarding icons.

However, due to how damaged tiles are currently mapped in, rather than overlayed as I envision in the future, it'll require a PR by San to be merged later that should make it safe to remove these icons.
Changelog

cl PositiveEntropy, WJohnston, Dragomagol, LemonInTheDark, Riggle
imageadd: Resprites most variety of tiles into a better shaded version!
code: Damaged floors are now damaged overlays, meaning that most tiles should properly display a damaged state!
/cl

---
## [intel/llvm](https://github.com/intel/llvm)@[7c51f02eff...](https://github.com/intel/llvm/commit/7c51f02effdbd0d5e12bfd26f9c3b2ab5687c93f)
#### Tuesday 2022-07-26 15:21:36 by Matheus Izvekov

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
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[d7b901d7d2...](https://github.com/cockroachdb/cockroach/commit/d7b901d7d28ceb4900dd60c5c73b2180089a3e3a)
#### Tuesday 2022-07-26 15:46:50 by craig[bot]

Merge #84618 #84674 #85034 #85042

84618: sql: add new index_recommendation column r=maryliag a=maryliag

This commit adds a new column index_recommendations
STRING[] to:
crdb_internal.node_statement_statistics
crdb_internal.cluster_statement_statistics
system.statement_statistics
crdb_internal.statement_statistics

Part of #83782

Release note (sql change): Adding new column index_recommendations
to crdb_internal.node_statement_statistics,
crdb_internal.cluster_statement_statistics, system.statement_statistics
and crdb_internal.statement_statistics

84674: changefeedccl/schemafeed: ignore unwatched column drops  r=jayshrivastava a=jayshrivastava

Closes https://github.com/cockroachdb/cockroach/issues/80982

Release note (enterprise change): Previously, if you dropped
a column with the schema_change_policy 'stop', the changefeed
would stop. Dropping a column with a different policy would
result in previous rows being retransmitted with the
dropped column omitted.

In some cases, a changefeed may target specific columns
(a column family) of a table. In these cases, if a non-target
column is dropped, it does not make sense to stop the changefeed
or retransmit values because the column was not visible to
a consumer sink to begin with.

With this change, dropping an non-target column from a
table will not stop the changefeed when the
schema_change_policy is 'stop'. With any other policy,
dropping a non-target column will not trigger a backfill.

85034: sql: better tracing of apply joins r=yuzefovich a=yuzefovich

**sql: add tracing spans for each iteration of apply join**

This commit creates a separate tracing span for each iteration of apply
join and recursive CTE execution to make the traces easier to digest.

Release note: None

**sql: log DistSQL diagrams when tracing is enabled**

This commit makes it so that we always include all DistSQL diagrams into
the trace. This could be especially helpful when executing apply join
iterations to understand the plan that each iteration gets. This commit
also removes an environment variable that used to control this logging
previously since I don't think anyone has used it in years now that we
have better tools for debugging (like a stmt bundle).

Informs: #https://github.com/cockroachlabs/support/issues/1681.

Release note: None

85042: logictest: remove spec-planning configs r=yuzefovich a=yuzefovich

This commit removes `local-spec-planning`, `fakedist-spec-planning`, and
`5node-spec-planning` logic test configurations since they seem to be
not very useful at the moment. They were introduced to support the new
DistSQL spec factory, but that work has been postponed with no active
development at the moment, so it seems silly to run most of the logic
tests through the configs that are largely duplicate of the other
default ones (because most of the `Construct*` methods are not
implemented in the new factory). Once the active development on the new
factory resumes, it'll be pretty easy to bring them back to life, but at
the moment let's reduce the amount of tests we run without really losing
any test coverage.

Release note: None

Co-authored-by: Marylia Gutierrez <marylia@cockroachlabs.com>
Co-authored-by: Jayant Shrivastava <jayants@cockroachlabs.com>
Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>

---
## [Higgin/tgstation](https://github.com/Higgin/tgstation)@[fdd8036140...](https://github.com/Higgin/tgstation/commit/fdd80361406f7b9ff8568237a933f9926b527c28)
#### Tuesday 2022-07-26 15:55:50 by BluBerry016

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
## [clayne/oiio](https://github.com/clayne/oiio)@[afc2bd1649...](https://github.com/clayne/oiio/commit/afc2bd1649a921c56192bbf8c3b326b137237c31)
#### Tuesday 2022-07-26 16:57:44 by Larry Gritz

parallel.h refactoring and add support for TBB (#3473)

Hide nearly all of the implementation of the parallel_for family of
methods rather than expose them as inline. This gives us more freedom
to change the implementation in the future without breaking ABI.

Deprecate the parallel methods that take task functions whose first
parameter is the thread ID. The only reason they existed is because
our cobbled together thread_pool used that in its inner workings.  But
there are good reasons why we should not expose that:

  * We never used it anyway.

  * It was not very useful, since sometimes it was a real thread ID, but
    other times it was -1 in cases where the calling thread executed the
    task directly.

  * It is inconsistent with other thread pool implementations that we may
    wish to try in the future.

So better just to not expose those thread IDs at all. Mark those
versions of the parallel loops as deprecated and schedule them for
removal in OIIO 3.0.

If TBB is detected at build time, support will be built in that allows
either the old OIIO built-in pool, or TBB, depending on the setting of
a new global OIIO attribute, "use_tbb" (default 0), if set to nonzero
will use the TBB thread pool.

In my experiments, the TBB thread pool seems slightly better -- I
think because there is less overhead, and maybe the clever
work-stealing it does elps to load balance. It's not used by default,
set the attribute if you want to use it (assuming the build
included. After we've had a chance to test more thoroughly, we may
change to use TBB by default. I'm interested to hear people's thoughts
on the matter.

One case where you almost certainly will want to use the TBB thread
pool is if you're using libOpenImageIO from within an application that
uses TBB for its own threding -- that way you're using one pool for
everything, rather than have two separate thread pools that don't know
about each other (and probably twice as many threads as you have
cores)..

---
## [lucaskroni/Frontend](https://github.com/lucaskroni/Frontend)@[340de148c0...](https://github.com/lucaskroni/Frontend/commit/340de148c0a77703f8153b8c5ed3f681fce8a1f9)
#### Tuesday 2022-07-26 17:00:27 by lkronlac

Yooo fam its time to goo now so yeah ehm yeah what we did today is we did add all of the components and somebug fixing yeah that is pretty much all

Good morning today you should do some styling and animating i know you like that but idk if thats so cool but well go through it we dont care if its not cool if it benefit us we going

Also show bernhard what it looks so far and tell em ther is a headset and mouse next to you in the thingy there the schiebewagon-teil-kasten am boden links von dir

oh yeah lastly ma boy you got this stay humble and stay givin you a beast there is no if feel like it consistency my boy consistency, brush your teeth and no going to bed before its done

oh yeah good morning and have a nice day

---
## [lucaskroni/Frontend](https://github.com/lucaskroni/Frontend)@[00c6f5b14a...](https://github.com/lucaskroni/Frontend/commit/00c6f5b14a8e04955666eb939456dc324c7a65b0)
#### Tuesday 2022-07-26 17:00:27 by lkronlac

Yooo my guy we got to style now leeetttss goood ok and yeah actually add the optional vals

Today we did some error correction and we where happy that is works now kind of

Yoo listen fam you keep it going u got this and remember brush your teeth and no bed until your done big ups have a nice day today or tomorrow yeah

---
## [paul-maidment/assisted-service](https://github.com/paul-maidment/assisted-service)@[564650feca...](https://github.com/paul-maidment/assisted-service/commit/564650feca372064314282d98d6fd9c6ee69bd2c)
#### Tuesday 2022-07-26 17:22:37 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition (#4072)

For context, this is a service-side follow-up to:

https://github.com/openshift/assisted-installer-agent/pull/388

and also this small agent fix https://github.com/openshift/assisted-installer-agent/pull/403

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

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, when a user imports a cluster, we will inspect the `params.NewImportClusterParams.APIVipDnsname`
parameter and extract:

- The cluster name
- The cluster base domain

The cluster name will override the name given in `params.NewImportClusterParams.Name`,
see diff comment for more information on why.

The cluster base domain will be used to set the `BaseDNSDomain` of the
cluster, because up until now we didn't set it for imported cluster.

The reason `BaseDNSDomain` and `Name` have to be correctly set is
because the DNS validations use them to construct the domain names
that are being validated.

Also updated some validation messages for the API connectivity check and
DNS validations.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

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

---
## [Nyanotrasen/Nyanotrasen](https://github.com/Nyanotrasen/Nyanotrasen)@[e454ba6bd0...](https://github.com/Nyanotrasen/Nyanotrasen/commit/e454ba6bd034cb4b3682808e9fced42c1c295f1a)
#### Tuesday 2022-07-26 18:11:37 by Rane

Despair (#298)

* Include thrown entity in ThrowAttemptEvent

* whoops cringe

* lgtm

* woops i broke shit

* make them scream

* holy shit laugh at this man

* remove logger

* dont let you carry yourself

---
## [Expensify/react-native](https://github.com/Expensify/react-native)@[47280de85e...](https://github.com/Expensify/react-native/commit/47280de85e62f33f0b97bc1ed7c83bc6ca0dc7d4)
#### Tuesday 2022-07-26 18:56:49 by Joshua Gross

New Props parsing infrastructure for perf improvements: visitor pattern vs random-map-access pattern (ViewProps, minus YogaLayoutableShadowNode)

Summary:
Perf numbers for this stack are given in terms of before-stack and after-stack, but the changes are split up for ease of review, and also to show that this migration CAN happen per-component and is 100% opt-in. Most existing C++ components do not /need/ to change at all.

# Problem Statement

During certain renders (select critical scenarios in specific products), UIManagerBinding::createNode time takes over 50% of JS thread CPU time. This could be higher or lower depending on the specific product and interaction, but overall createNode takes a lot of CPU time. The question is: can we improve this? What is the minimal overhead needed?

The vast, vast majority of time is taken up by prop parsing (specifically, converting JS values across the JSI into concrete values on the C++ props structs). Other methods like appendChild, etc, do not take up a significant amount of time; so we conclude that createNode is special, and the JSI itself, or calling into C++, is not the problem. Props parsing is the perf problem.

Can we improve it? (Spoiler: yes)

# How does props parsing work today?

Today, props parsing works as follows:

1. The ConcreteComponentDescriptor will construct a RawPropsParser (one per component /type/, per application: so one for View, one for Image, one for Text... etc)
2. Once per component type per application, ConcreteComponentDescriptor will call "prepare" on the RawPropsParser with an empty, default-constructed ConcreteProps struct. This ConcreteProps struct will cause RawProps.at(field) for every single field.
3. Based on the RawProps::at calls in part 2, RawPropsParser constructs a Map from props string names (width, height, position, etc) to a position within a "value index" array.
4. The above is what happens before any actual props are parsed; and the RawPropsParser is now ready to parse actual Props.
5. When props are actually being parsed from a JSI dictionary, we now have two phases:
  1. The RawPropsParser `preparse`s the RawProps, by iterating over the JSI map and filling in two additional data structures: a linear list of RawValues, and a mapping from the ValueIndex array (`keyIndexToValueIndex_`; see step 3) to a value's position in the values list (`value_` in RawPropsParser/RawProps);
  2. The ConcretePropT constructor is called, which is the same as in step 2/3, which calls `fieldValue = rawProps.at("fieldName")` repeatedly.
  3. For each `at` call, the RawProps will look up a prop name in the Map constructed in step 3, and either return an empty value, or map the key name to the `keyIndexToValueIndex_` array, which maps to a value in `values_`, which is then returned and further parsed.

So, a few things that become clear with the current architecture:

1. Complexity is a property of the number of /possible/ props that /can/ be parsed, not what is actually used in product code. This violates the "only pay for what you use" principal. If you have `<View opacity={0.5} />`, the ViewProps constructor will request ~170 properties, not 1!
2. There's a lot of pre-parsing which isn't free
3. The levels of indirection aren't free, and make cache misses more likely and pipelining is more challenging
4. The levels of indirection also require more memory - minor, but not free

# How can we improve it?

The goal is to improve props parsing with minimal or zero impact on backwards-compability. We should be able to migrate over components when it's clear there's a performance issue, without requiring everything gets migrated over at once. This both (1) helps us prove out the new architecture, (2) derisks the project, (3) gives us time, internally and externally, to perfect the APIs and gradually migrate everything over before deleting the old infrastructure code entirely.

Thus, the goal is to do something that introduces a zero-cost abstraction. This isn't entirely possible in practice, and in fact this method slightly regresses components that do not use the new architecture /at all/, while dramatically improving migrated components and causing the impact of the /old/ architecture to be minimal.

# Solution

1. We still keep the existing system in place entirely.
2. After Props are constructed (see ConcreteComponentDescriptor changes) we iterate over all the /values/ set from JS, and call PropsT::setProp. Incidentally, this allows us to easily reuse the same prop for multiple values for "free", which was expensive in the old system.
3. It's worth noting that this makes a Props struct "less immutable" than it was before, and essentially now we have a "builder pattern" for Props. (If we really wanted to, we could still require a single constructor for Props, and then actually use an intermediate PropsBuilder to accumulate values - but I don't think this overhead would be worth for the conceptual "immutability" win, and instead a "Construct/Set/Seal" model works fine, and we still have all the same guarantees of immutability after the parsing phase)

# Implementation Details
# How to properly construct a single Prop value

Minor detail: parsing a single prop is a 3-step process. We imagine two scenarios: (1) Creating a new ShadowNode/Props A from nothing/void, so the previous Props value is just the default constructor. (2) Cloning a ShadowNode A->B and therefore Props A must be copied to Props B before parsing.

We will denote this as a clone from A->B, where A may or may not be a previous node or a default-constructed Props node; and imagine in particular that we're setting the "opacity" value for PropsB.

We must first (1) copy a value over from the previous version of the Props struct, so B.opacity = A.opacity; (2) Determine if opacity has been set from JS. If so, and there is a value, B.opacity = parse(JSValue). (3) If JS has passed in a value for the prop, BUT the value is `null`, it means that JS is resetting or deleting the prop, so we must set it BACK to the default. In this case we set PropsB.opacity = DefaultConstructedProps.opacity.

We must take care in general to ensure that the correct behavior is achieved here, which should help to explain some of the code below.

## String comparisons vs hash comparisons

In the previous system, a RawPropsKey is three `const char*` strings, concatenated together repeatedly /at runtime/. In practice, the ONLY reason we have the prefix, name, suffix Key structure is for the templated prop parsing in ViewProps and YogaStyableProps - that's it. It's not used anywhere else. Further, the key {"margin", "Left", "Width"} is identical to the key {"marginLeftWidth", null, null} and we don't do anything fancy with matching prefixes before comparing the whole string, or similar. Before comparison, keys are concatenated into a single string and then we use `strcmp`. The performance of this isn't terrible, but it's nonzero overhead.

I think we can do better and it's sufficient to compare hashed string values; even better, we can construct most of these /at compile time/ using constexpr, and using `switch` statements guarantee no hash collisions within a single Props struct (it's possible there's a collision between Props.cpp and ViewProps.cpp, for example, since they're different switch statements). We may eventually want to be more robust against has collisions; I personally don't find the risk to be too great, hash collisions with these keys are exceedingly unlikely (or maybe I just like to live dangerously). Thus, at runtime, each setProp requires computing a single hash for the value coming from JS, and then int comparisons with a bunch of pre-compiled values.

If we want to be really paranoid, we could be robust to hash collisions by doing `switch COMPILED_HASH("opacity"): if (strcmp(strFromJs, "opacity") == 0)`. I'm happy to do this if there's enough concern.

## Macros

Yuck! I'm using lots of C preprocessor macros. In general I found this way, way easier in reducing code and (essentially) doing codegen for me vs templated code for the switch cases and hashing prop names at compile-time. Maybe there's a better way.

Changelog: [Added][Fabric] New API for efficient props construction

Reviewed By: javache

Differential Revision: D37050215

fbshipit-source-id: d2dcd351a93b9715cfeb5197eb0d6f9194ec6eb9

---
## [MuchMarts/Afirmacijas](https://github.com/MuchMarts/Afirmacijas)@[f99b09fb41...](https://github.com/MuchMarts/Afirmacijas/commit/f99b09fb41dfbed8033d429bf7e27ccc8e5de434)
#### Tuesday 2022-07-26 19:11:22 by DrgnInventor

PAIN AND SUFFERING

Gods have lied potatos have grown and forks have won. This stupid thing aint working and im not sure why I dont want to rewrite it but like why you no work

---
## [MicrosoftDocs/OfficeDocs-Exchange](https://github.com/MicrosoftDocs/OfficeDocs-Exchange)@[b258c0d83e...](https://github.com/MicrosoftDocs/OfficeDocs-Exchange/commit/b258c0d83e34b4e47365e103ffb8379d2d24c7ed)
#### Tuesday 2022-07-26 19:31:10 by Jak

Add more emphasis to risks of extending SPF

Hi,

I believe there should be slightly more warning as to the full impact of adding a new IP address to the SPF record.

This documentation is slightly misleading as it implies at several points in Option 2 that this doesn't allow sending to external recipients, e.g. Line 200 in the "Limitations of direct send"
> Direct send cannot be used to deliver email to external recipients
Whereas following the steps and adding the IP address to the SPF record is sufficient to authorise any users of that IP address to send to external recipients and represent the domain (I'm not mentioning DKIM here because neither does the documentation and we can't assume that all organisations make use of it or enforce it via DMARC).

My real-world experience is that in our company, we were looking at implementing Option 2 to enable a multi-function printer to scan-to-email. The IP address in use is the public IP of our office, which all traffic goes through via NAT. We also have a guest WiFi network that allows guests to access the internet without having access to our office network, but it uses the same NAT IP.
The problem with Option 2 is that any guest WiFi user could send email as any user of our domain, which is a breach of our security requirements.

Step 1 does make reference to the risk:
> You can share your static IP address with other devices and users, but don't share the IP address with anyone outside of your company.

But I'm concerned that it's not highlighted, and other references in Option 2 to direct send not being able to send externally are a little misleading and undermine the message that there is a security risk when adding new IP addresses to the SPF record.

Interested to hear your thoughts,

Thanks,
Jak

---
## [entrez/NetHack](https://github.com/entrez/NetHack)@[95868cc708...](https://github.com/entrez/NetHack/commit/95868cc70853d61ef1d31beb4e4c5b67d6266af2)
#### Tuesday 2022-07-26 19:35:27 by Michael Meyer

Shopkeepers hold a grudge against past thieves

When you steal from a shop, its shopkeeper will remember you as a thief
and charge you higher prices in the future (as well as be more curt and
less polite in interactions with you, though not outright hostile) even
if you pacify them, or die on the level and revisit it later as a bones
file.  This was an idea aosdict had, and I think it makes sense that a
shopkeeper doesn't forgive and forget, immediately returning to treating
you exactly like anyone else, just because you were terrorized into
paying her back.  Paying a shopkeeper off may cause her to stop actively
attacking you, but it feels like she'd have her eye on you as a known
thief going forward (and maybe would hang up a sign with your picture,
saying something like "DO NOT ACCEPT CHECKS FROM THIS HERO").

This surchage already existed, but since it was tied to active anger
(which typically causes a shopkeeper to quickly abandon their shop to
follow you) it was somewhat rare to see it in action.

I did not implement it here, but one possible further tweak might be to
clear the surcharge if the shopkeeper is pacified via taming magic
(which more-or-less magically brainwashes the target to feel positively
towards the hero) but not if you simply pay your debts.

---
## [batrick/ceph](https://github.com/batrick/ceph)@[afc554a805...](https://github.com/batrick/ceph/commit/afc554a8057cddca8a3ffbdd19d9f4c0417764d1)
#### Tuesday 2022-07-26 20:28:36 by Patrick Donnelly

qa: use postmerge hooks for filtering stock kernel

Up to now, the k-stock kernel required an awkward matrix configuration
to ensure that we're only testing the rhel stock kernel. This is
basically done by overriding (evil) the yaml fragment specifying the
distribution.  So, you'd have a config like:

	fs/snaps/{begin clusters/1a3s-mds-1c-client conf/{client mds mon osd} distro/{ubuntu_latest} mount/kclient/{mount overrides/{distro/stock/{k-stock rhel_8} ms-die-on-skipped}} objectstore-ec/bluestore-bitmap overrides/{whitelist_health whitelist_wrongly_marked_down} tasks/workunit/snaps}

One would rightly believe it's running with ubuntu but, actually, the
rhel_8 fragment overrides this.

Instead of this, we're using the new postmerge teuthology hooks to
filter our configs containing k-stock when the rhel distribution is not
selected.

This is great (and a small change by itself) but doing so would bias the
selection of jobs towards k-testing/fuse which do not drop configs not
using rhel. To work around this, we add another two rhel (three total)
fragments to the custom `qa/cephfs/distro` to compensate. The extra two
rhel fragments drop if the k-stock config is not in use.  This also
uses the teuthology postmerge hooks.

Simultaneously, we're dropping the random selection of distributions as
it's no longer necessary with nested subsets (another newer teuthology
feature). Instead, modify fs:* sub-suites to divide jobs by 2 to
approximate.

Signed-off-by: Patrick Donnelly <pdonnell@redhat.com>

---
## [newstools/2022-vanguard-nigeria](https://github.com/newstools/2022-vanguard-nigeria)@[bdef9fcd0b...](https://github.com/newstools/2022-vanguard-nigeria/commit/bdef9fcd0bf8285f241d26a76a9a94dfa5586f8b)
#### Tuesday 2022-07-26 20:42:48 by Billy Einkamerer

Created Text For URL [www.vanguardngr.com/2022/07/bbnaija-housemate-amaka-says-ready-to-annoy-her-ex-boyfriends-level-up-as-nigerian-nicki-minaj/]

---
## [Shaddoll/cadence](https://github.com/Shaddoll/cadence)@[add4b390ad...](https://github.com/Shaddoll/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Tuesday 2022-07-26 21:11:27 by Steven L

Standardizing cancellation behavior: a canceled workflow never starts a new run (#4898)

# Summary for busy people

Workflow cancellation was kinda weird and confusing, and left some awful, unrecoverable, and un-*preventable* edge cases (particularly with child workflows).  It also left users with no way to reliably stop work, aside from termination.  Termination is inherently "unclean" and risky, so it should not be required to achieve something outside exceptional circumstances where recovery is not possible.

This commit changes that: cancellation is now "sticky", and a canceled workflow does not ever trigger a new run after it completes, regardless of how it completes, so it can be used as a reliable "stop processing after cleanup" tool.  The final state of a canceled workflow's run is now *always* a successful completion with a value, canceled, or timed out. (termination remains always "terminated")  
A canceled workflow can still start and abandon child workflows, so all current behavior with retries / continue as new / etc can be replicated with child workflows if desired.

A fair bit of (not very complex) additional work here and in nearly all other repos is required to truly complete this, but it is *functional* and non-optional with this commit alone.  
In particular, adding a dynamic config to (temporarily!) restore old behavior should be fairly easy if it proves to be needed.

# More details and motivation

Part 1 of [many, tbd, in multiple repos] involved in changing workflow cancellation to reliably end workflows.
Tests will be coming soon, for now I'm using a fairly simple set of workflows and checking the resulting histories exhaustively by hand.

The primary motivation for these changes is to address some impossible-to-recover-from scenarios when canceling child workflows.  After further exploration and discussion we've realized that, without these changes, there is *no reliable way* to stop a sequence of workflows without relying on termination, which we consistently treat as a fallback / impure-but-necessary ultimate hammer.

Workflows should not *need* to rely on termination to achieve a desired behavior.  With these changes, cancellation becomes capable of *guaranteeing* that workflows end within some finite time, which is a unique ability and makes it much more consistent and reliable.  
Turning this into a "complete" change will require quite a few tests, documentation changes, client-side changes (to allow recording more info, and likely changing test suites), and some smallish database and maybe RPC changes (to hold/return more data in cancellation errors).

We are also not currently planning on making this configurable.  It's seen as a correction of an under-specified and somewhat flawed chunk of behavior, more than "a change".  
Existing workflows will not experience replay errors, but it is still a substantial *semantic* change, though from what we have seen cancellation is relatively rarely used (partly due to its complex behavior).  If issues are encountered / if users end up needing it, it should be fairly easy to add a per-domain/tasklist/workflow type configuration value, but it will be opt-*out*, not opt-*in*.

# What was happening

Previously, workflow behavior on cancellation was pretty frequently surprising to our users, arguably inconsistent, and not very well documented:

| **PREVIOUS**  | **simple**               | **retry**                                 | **cron**                                | **retry+cron**                                    |
|--------------:|--------------------------|-------------------------------------------|-----------------------------------------|---------------------------------------------------|
| **success**   | success                  | success                                   | success<br>continue cron<br>cron        | success<br>continue cron<br>cron<br>retry         |
| **cancel**    | canceled                 | canceled                                  | canceled                                | canceled                                          |
| **retryable** | (n/a, fatal)             | continue retry<br>retry<br>recorded error | (n/a, fatal)                            | continue retry<br>cron<br>retry<br>recorded error |
| **fatal**     | failed<br>recorded error | failed<br>recorded error                  | continue cron<br>cron<br>recorded error | continue cron<br>cron<br>retry<br>recorded error  |
| **continue**  | continue immediately     | continue immediately<br>retry             | continue immediately                    | continue immediately<br>retry                     |
| **timeout**   | timeout                  | continue retry<br>retry<br>recorded error | continue cron<br>cron<br>recorded error | continue retry<br>cron<br>retry<br>recorded error |

A legend is:
- success / etc shows the final state of the canceled run (success = completed with a value that can be retrieved)
- "continue X" covers what source is used to compute the next run's starting delay (cron, retry, or no delay)
- "cron" / "retry" shows whether or not cron/retry configuration is carried over to the new run
  - note that cron is lost by default with continue-as-new
- and "recorded error" is whether or not the returned error is saved in its entirety (type + reason + details)

This largely summarizes as "cancellation works when you end with the canceled-context error", say from `ctx.Err()`, otherwise it behaves like normal (or nearly) and many scenarios will start a new run.
That's somewhat reasonable, but it's fairly "fragile" (it depends on what you return, and there are *many* ways for code to return some other error), and most importantly it means *there is no reliable way to stop a workflow* except to terminate it.

That has severe consequences in at least two scenarios:
1. When termination is *unsafe*
2. When a parent workflow cancels a child by canceling its context

For 1, for manual cancellations it's potentially reasonable to just terminate a run that begins after a successful cancel... but in principle if you're using cancellation it implies that termination is *not* desired, and potentially not safe to do.  Canceling may result in a brand new run that immediately starts new behavior, leaving you with no safe window to terminate and not leave bad state lingering.  
So users wanting a safe way to stop a sequence of workflows have no reliable way to do so.

For 2, it puts parent+child workflows in an extremely awkward, and essentially unrecoverable scenario.  Cancellation is a *one time event*, and as far as the parent is concerned, if the child/its context is canceled, the child is canceled...  
...but if the child then starts a new run for *any* reason (retry, cron, reset, etc), that new run is no longer canceled.  The parent has no way to know this has happened, and has no way to *re*-cancel the new child, so it can easily lead to the collection of workflows getting into an impossible state that it never recovers from.

Both cases are able to lead to unreliable behavior which can only use termination to stop, and for which no "safe" option exists.

After reviewing some customer issues and desires and thinking about things, we've settled on "cancel should guarantee that things stop".  Not necessarily in a timely manner, but that's fine.  And if a workflow wants to run behavior longer or larger than its current run can achieve, it has a workaround: start a new (likely child) workflow to do the cleanup.

# What happens now

So that's what this PR does, in a minimal / to-be-polished way so we can start running it for our stuck users while we flesh out tests and change other behaviors.

Currently that means our cancellation behavior is now:

| **CURRENT**    | **simple**                                | **retry**                                 | **cron**                                  | **retry+cron**                            |
|--------------:|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **success**   | success                                   | success                                   | success                                   | success                                   |
| **cancel**    | canceled                                  | canceled                                  | canceled                                  | canceled                                  |
| **retryable** | (n/a, fatal)                              | canceled<br>recorded error (details only) | (n/a, fatal)                              | canceled<br>recorded error (details only) |
| **fatal**     | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) |
| **continue**  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  |
| **timeout**   | timeout                                   | timeout                                   | timeout                                   | timeout                                   |

And the new "details" entries cover whether or not an error's "details" (the custom encoded data, not reason or type) are saved.  Unfortunately the current cancellation event (and clients' API) does not allow recording all data, or any in some cases, so the original reason/message and error type are lost and are replaced with a canceled error.

Now, cancellation *always* ends workflows with the current run.  Returning a value will return that value, including in cron scenarios, timeouts are still timeouts (and they imply a possibly un-clean termination), and _all_ errors or attempts to continue-as-new will instead result in a canceled state.

# Future changes to make to finish this effort

With further changes to the clients and RPC/storage models, canceled errors will store more details about what was returned.  E.g. continue-as-new does not record what was *attempted* to be started, and other error types lose their "reason" (i.e. the message) and type but not details.  Pretty clearly this is sub-par, and we should be capable of reporting the actual return in full so it can be retrieved if needed.  This is also why returning a value now always ends in a completed state, so successful completions do not lose those values.

Prior to merging into master / a release, we may end up making this configurable (likely with a default of opt-out), to address both the sub-par information recording and the semantically-breaking behavior change.  Docs changes are also due, as well as some integration tests, client library changes (e.g. to make sure the test suite reflects the new behavior), etc.

Another gap to plug is that resetting a workflow does not "forward" the canceled state to the new run.  We should probably be treating cancellation like we do signals: cancel the new run if the current run is canceled.  This will ensure that you can reset a child and retain the parent's cancellation, so it'll very likely become the default behavior, but we'll allow overriding it.  Resets are manual actions, they can break the rules if desired.  And they can just manually cancel later if they decide they do want it.

And last and perhaps least: it's quite strange that continue-as-new does not retain cron config.  At least from the Go client.  I suspect it's just not adding to / pulling from the context correctly.

---
## [mrwallace888/OWNH-Carson-System](https://github.com/mrwallace888/OWNH-Carson-System)@[5b3912cfb2...](https://github.com/mrwallace888/OWNH-Carson-System/commit/5b3912cfb25f0411829d1e700728a1a7c3fd3c32)
#### Tuesday 2022-07-26 21:13:56 by Jack Foxtrot

Carson has received its 1.0 update!

# What's new?
### Ah jeez, what *hasn't* changed since release 0.4?

- The *Carson* star itself has been given tweaks and a fresh coat of paint.
- All planets have been completely rebuilt and revamped with new terrain as well as given proper generated heightmaps. No more taking the standard terrain texture and grayscaling it, save a few tweaks here and there.
-  Increased heightmap resolution to 1024 at the equator thanks to the introduction of LODs allowing for higher resolution while keeping frames stable. It allows for mountains, cracks, craters, and shorelines to be much more defined, and helps to keep things detailed when on the surface.
- Added another new planet named *Dester*.
- Added props such as trees and cacti to some planets, further helping to keep things detailed when on the surface.
- Added rain to Pyer.

# What now?
### Well, a couple things...
The original idea behind *Carson* was that I wanted to create a star system that felt immersive.  The celestial bodies showcased in *Outer Wilds* as well as the beautiful star systems made by other talented people are rather tiny; you can walk across the circumference of a planet in about a minute give or take, which isn't big at all.

I figured the best thing to do was make a much bigger star system, but also without being *too* big. It's a very sensitive scale to balance, mind you, because if you make it too big then it'll just become boring and likely frustrating. But too small and it breaks immersion.

*Carson* was inspired by the *Kerbol* system (as well as modded solar systems via *Kopernicus*) as shown in the famous spacecraft simulator *Kerbal Space Program*, as seen by *Carson*'s overall planetary designs.

What I wanted to figure out was just *how big* to make my objects. I settled around the size they are now. I estimated it to be the sweet spot for size. Again, I wanted my system to be big enough to be immersive, but not too big to be frustrating for people or boring. I had to take into consideration that the ship, vanilla-wise anyways, is pretty slow too.

Obviously, this mod has its flaws; a lot of them, mind you. But I've had fun developing this mod and some of the wonderful people like Trifid on the *Outer Wilds Modding* Discord server appreciate the creative decisions I took when developing it. After all, if I'm going to make a planet, *I'm going to make a planet*. Because planets are huge.

I hope you've enjoyed the effort I've put into this regardless. It definitely does something different from other systems in *New Horizons*, and that was pretty much the whole scope of the mod.

### This is not the end.
I want to clarify that I am nowhere near finished with this mod. Plenty of updates are planned for the future. I just figured that the current version, with all the blood, sweat, and tears put into it, was a nice stable update to release with. More celestial bodies or maybe even more stars are planned. We'll see. But I also don't want my mod to get *too* bloated file-wise. Unfortunately, most systems made with *New Horizons* grow outdated and broken as support is dropped for them, whether because of personal reasons or whatever else. I'll be doing my best to keep my system up-to-date and fix anything that breaks in the future. I'll need to anyways if I'm going to add new content.

Thanks for downloading *Carson*, and stay tuned for more!

---
## [zombocom/syntax_suggest](https://github.com/zombocom/syntax_suggest)@[4dfa1b2a3a...](https://github.com/zombocom/syntax_suggest/commit/4dfa1b2a3a39a89ac3a37a54bbc1b2ac862e01d5)
#### Tuesday 2022-07-26 21:22:23 by schneems

This is a difficult problem

The algorithm builds a pretty good looking tree but then it sees this:

```
  1  class Blerg
❯ 2    Foo.call do |lol
❯ 3      print lol
❯ 4    end # one
  5    print lol
  6    class Foo
  7    end # two
  8  end # three
```

It thinks that there are two invalid nodes here

```
❯ 2    Foo.call do |lol
```

and

```
❯ 4    end # one
```

While it's obvious to you and me that they belong together the search algorithm calls a `multiple_invalid_parents` and continues to explore both which gives us the weird output:


```
       +Unmatched `|', missing `|' ?
       +Unmatched keyword, missing `end' ?
       +
       +  1  class Blerg
       +❯ 2    Foo.call do |lol
       +  4    end # one
       +  6    class Foo
       +  8  end # three
       +Unmatched `end', missing keyword (`do', `def`, `if`, etc.) ?
       +
       +  1  class Blerg
       +  2    Foo.call do |lol
       +❯ 4    end # one
       +  6    class Foo
       +  7    end # two
       +  8  end # three
```

Interesting enough if we combined these two it would be the perfect output, which makes me think it's not a different problem than the "fix it in post" ones I mentioned on the last commit, but rather might be a variation on them.

Sometimes we only match the `end` but not the source line. Other times we match the end AND the source line if they both have a syntax error on them. 

A harder case is replacing the mismatched pipe with something mismatched up like

```
        class Blerg
          Foo.call }
            print haha
            print lol
          end # one
          print lol
          class Foo
          end # two
        end # three
```

Gives us:

```
❯ 1  class Blerg
  9  end # three
Unmatched `}', missing `{' ?

  1  class Blerg
❯ 2    Foo.call }
  5    end # one
  7    class Foo
  9  end # three
Unmatched `end', missing keyword (`do', `def`, `if`, etc.) ?

  1  class Blerg
❯ 5    end # one
  7    class Foo
  8    end # two
  9  end # three
Unmatched `end', missing keyword (`do', `def`, `if`, etc.) ?

  1  class Blerg
❯ 9  end # three
```

So it's like double the problem from before. `class Blerg/end # three` belong together and `Foo.call }/end #one` belong together. Technically one of these is not a good match `class Blerg/end # three`. 

We could do something naive that might work long term or try to get more clever. 

It seems like we could add another grouping round after the search round. We could try to intelligently pair nodes together and do fancy stuff like re-check parsability of the daocument. That would be the advanced path.

The "easy" path would be to shove all these groups together at the very end so that the output might look like this:

```
❯ 1  class Blerg
❯ 2    Foo.call }
❯ 5    end # one
❯ 9  end # three
```

Which is honestly pretty good. Not ideal, but good. The main downside is we would eventually need a way to split off ACTUAL multiple syntax errors and report on them. I don't remember at this point if that was a feature of the old algorithm or not. If not, then it's no regression so maybe it's fine to start there.

So that's good. Maybe the search algorithm is good enough and it's just up to touching up the post operations. Here's the list from last time of the failure:

### Needs investigation 0

```
  1  class Blerg
❯ 2    Foo.call do |a
  5    class Foo
  6    end # two
  7  end # three
Unmatched `end', missing keyword (`do', `def`, `if`, etc.) ?

  1  class Blerg
❯ 3    end # one
  5    class Foo
  6    end # two
  7  end # three
  handles mismatched | (FAILED - 1)

Failures:

  1) Integration tests that don't spawn a process (like using the cli) handles mismatched |
     Failure/Error: raise("this should be one failure, not two")

     RuntimeError:
       this should be one failure, not two
     # ./spec/integration/dead_end_spec.rb:603:in `block (2 levels) in <module:DeadEnd>'
```

### Needs investigation 1

Expected:

```
          7  context "test" do
        ❯ 8    it "should" do
          9  end
```

Actual

```
       +Unmatched keyword, missing `end' ?
       +
       +  1  context "foo bar" do
       +❯ 7  context "test" do
       +  9  end

     # ./spec/integration/dead_end_spec.rb:418:in `block (2 levels) in <module:DeadEnd>'
```


### Needs investigation 2


Expected:

```
    it "finds a naked end" do
      source = <<~'EOM'
        def foo
          end # one
        end # two
      EOM

      io = StringIO.new
      DeadEnd.call(
        io: io,
        source: source
      )

      expect(io.string).to include(<<~'EOM')
        ❯ end # one
      EOM
    end
```

Actual:


```
       +Unmatched `end', missing keyword (`do', `def`, `if`, etc.) ?
       +
       +  1  def foo
       +❯ 3  end # two
```



## Fix it in post 1 

```
       +Unmatched `end', missing keyword (`do', `def`, `if`, etc.) ?
       +
       +   1  describe "things" do
       +   2    it "blerg" do
       +   3    end
       +❯  6    end
       +   8    it "zlerg" do
       +   9    end
       +  10  end

     # ./spec/integration/dead_end_spec.rb:227:in `block (2 levels) in <module:DeadEnd>'
```

Several of these repeated


## Fix it in post 2

Subtly different:


```
       +Unmatched `end', missing keyword (`do', `def`, `if`, etc.) ?
       +
       +   2  RSpec.describe AclassNameHere, type: :worker do
       +   3    describe "thing" do
       +  13    end # line 16 accidental end, but valid block
       +❯ 23    end # mismatched due to 16
       +  24  end

     # ./spec/integration/dead_end_spec.rb:481:in `block (2 levels) in <module:DeadEnd>'
```


Next time I want to look at "### Needs investigation 2" to see how it compares/contrasts to the other ones.

---
## [h3xx/dotfiles](https://github.com/h3xx/dotfiles)@[52f946a68c...](https://github.com/h3xx/dotfiles/commit/52f946a68c5c22467832086fdf50209d1a99da0b)
#### Tuesday 2022-07-26 21:27:32 by Dan Church

cron: Fix clean-chrome-tmp.sh

Wasn't properly deleting all it should.

Changes it to assume if there isn't a socket in the dir, it's not in
use.

Fuck you chrome.

---
## [AdvancedProgrammingSUT2022/project-group-07](https://github.com/AdvancedProgrammingSUT2022/project-group-07)@[7234cf20b6...](https://github.com/AdvancedProgrammingSUT2022/project-group-07/commit/7234cf20b67edf73d8672994cc09210b8be96c60)
#### Tuesday 2022-07-26 21:31:52 by Mahan Bayhaghi

Trade and diplomacy !

* diplomacy and trade basic logic added (basic!)

haghighatan holy jesus christ
this is a lot of logic

* diplomacy is in good shape

honestly i don't care if it is not like the pdf
i just think it is good :)

* i forgot to add files :)

* logic of trade added

* i forgot to add trading asset (again)

* diplomacy panel is done (not that stylish yet)

---
## [chadvandy/nagash](https://github.com/chadvandy/nagash)@[b3cd88505a...](https://github.com/chadvandy/nagash/commit/b3cd88505a11d2886e929e7f71190591e67cfd9e)
#### Tuesday 2022-07-26 21:38:56 by Scott (JvJ)

Eco changes and additional tweaks and fixes

- removed tomb guard/halberds from subhorde T3 war beast chain
- small growth tweaks across the board for hordes
- settlements +15 base growth, should help to compensate from the lack of province growth from T2/T3 settlements
- settlement major main chain income increased 10/15/20/25 % increase per tier (mostly effects special settlements because growth) T1 income remains the same
- settlement minor main chain income +25
- settlement income chain now 150/250/400, removed movement buff, local upkeep reduction 10/20/30
- horde BP/Mort/Sub horde Industry chain added a base 50 to all tiers
- control outpost chain effect now province wide, removed LD debuff, enemy forces start winded (hopefully will push less reliance on the income chain)
- corruption outpost chain now gives a small but spooky garrison
- arkhan staff no longer gives PO bonuses
- husk dark conduit skill now correctly gives +2 horde growth
- husk innate now gives additional growth
- fixed dodgy building chain slot unlock (left over from a previous attempt at being clever)
- removed loc references to dodgy building chain slot unlocks
- added references to spirit hosts and fell spectres for the ancient terrors red line skill loc.
- wight king/vampire/gunnery wight mounts now correctly applied
- fixed capacity issue with wight kings and tomb princes
- fixed krell anc typo
- fixed hidden movement modifiers for nagashizzar
- re-evaluated lahmia ghoul upkeep reduction to co-exist with the 50% reduction tech (no longer -100% at T5 gives -40% which = to 90% with the tech)
- spirit hosts/bone golems/spectres/necro knights/hexwraiths now take 2 turns to recruit

---
## [chadvandy/nagash](https://github.com/chadvandy/nagash)@[7060e9e6fe...](https://github.com/chadvandy/nagash/commit/7060e9e6fe7dbf0bb3ed94e819a36abacab250d8)
#### Tuesday 2022-07-26 21:47:52 by Scott (JvJ)

Economy changes and some bug fixes

- removed tomb guard/halberds from subhorde T3 war beast chain
- small growth tweaks across the board for hordes
- settlements +15 base growth, should help to compensate from the lack of province growth from T2/T3 settlements
- settlement major main chain income increased 10/15/20/25 % increase per tier (mostly effects special settlements because growth) T1 income remains the same
- settlement minor main chain income +25
- settlement income chain now 150/250/400
- horde BP/Mort/Sub horde Industry chain added a base 50 to all tiers
- syphon outpost chain effect now province wide, removed LD debuff, enemy forces start winded (hopefully will push less reliance on the income chain)
- corruption outpost chain now gives a small but spooky garrison
- arkhan staff no longer gives PO bonuses
- husk dark conduit skill now correctly gives +2 horde growth
- husk innate now gives additional growth
- fixed dodgy building chain slot unlock (left over from a previous attempt at being clever)
- removed loc references to dodgy building chain slot unlocks
- added references to spirit hosts and fell spectres for the ancient terrors red line skill loc.
- wight king/vampire/gunnery wight mounts now correctly applied
- fixed capacity issue with wight kings and tomb princes
- fixed krell anc typo

---
## [Spectrum-Kernel/kernel_xiaomi_sm6250](https://github.com/Spectrum-Kernel/kernel_xiaomi_sm6250)@[19551e9952...](https://github.com/Spectrum-Kernel/kernel_xiaomi_sm6250/commit/19551e995238429829074034b890c07fc8d9c28f)
#### Tuesday 2022-07-26 21:53:43 by Maciej Żenczykowski

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
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [checkraisefold/Foundation-19](https://github.com/checkraisefold/Foundation-19)@[befabcec33...](https://github.com/checkraisefold/Foundation-19/commit/befabcec333347ce6b918d67d4c884b9e0dcefea)
#### Tuesday 2022-07-26 22:58:08 by TenameACAccount

more dcz changes yay (#548)

* Update site53-1.dmm

* fallout 5 on the byond engine

* fuck you box

Co-authored-by: UserU <37943518+User-U-U@users.noreply.github.com>

---
## [zunath/SWLOR_Haks](https://github.com/zunath/SWLOR_Haks)@[6ffa92d6cc...](https://github.com/zunath/SWLOR_Haks/commit/6ffa92d6cc5883cce0bc077245f3f7d5a9f1a75f)
#### Tuesday 2022-07-26 23:29:57 by Scott Finlay

Patch for Head Pack 4 (#146)

- Re-added overwritten head 54, now as Head 100. Over-wrote ugly old NWN head that nobody used because I didn't want to fuck with IDs

- Adjusted scaling on Male Hum/Mir/Chi/Ech 50 & 51

---

