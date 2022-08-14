## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-13](docs/good-messages/2022/2022-08-13.md)


1,663,060 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,663,060 were push events containing 2,212,626 commit messages that amount to 128,729,477 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [kernelci/linux](https://github.com/kernelci/linux)@[ad8d312e32...](https://github.com/kernelci/linux/commit/ad8d312e3241a6e4d9f27b144987029592fdb8cd)
#### Saturday 2022-08-13 00:04:49 by Johannes Weiner

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[58955d8f47...](https://github.com/Buildstarted/linksfordevs/commit/58955d8f477297b67c60d9f80a70bf1b0062cc6d)
#### Saturday 2022-08-13 00:06:01 by Ben Dornis

Updating: 8/12/2022 11:00:00 PM

 1. Added: Making Notes Work for Me: Reflections after 2 Years of Digital Gardening
    (https://strikingloo.github.io/reflections-digital-gardening)
 2. Added: Nuclear Terror and Game Theory
    (https://dandanua.github.io/posts/nuclear-terror-and-game-theory/)
 3. Added: I developed a game to fix my burnout. It sucks.
    (https://devpoga.org/blog/2022-08-12_i_developed_a_game_to_fix_my_burnout_it_sucks/)
 4. Added: Someone Told Me to Build an MVP
    (https://rokkincat.com/blog/2022-07-22-the-mvp/)
 5. Added: Climate policy numbers
    (https://johnhcochrane.blogspot.com/2022/08/climate-policy-numbers.html)
 6. Added: My life is a litmus test - Deep South Ventures
    (https://www.deepsouthventures.com/litmus/)
 7. Added: How We Can Learn from History
    (https://peterturchin.com/cliodynamica/how-we-can-learn-from-history/)
 8. Added: Comparing Linux Environments on macOS Host
    (https://blog.sffc.xyz/post/651389596091973632/comparing-linux-environments-on-macos-host)
 9. Added: The Hacking of Starlink Terminals Has Begun
    (https://www.wired.com/story/starlink-internet-dish-hack/)

Generation took: 00:05:49.2157323

---
## [makesoftwaresafe/git](https://github.com/makesoftwaresafe/git)@[5beca49a0b...](https://github.com/makesoftwaresafe/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Saturday 2022-08-13 00:30:19 by Ævar Arnfjörð Bjarmason

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
## [lewcc/Paradise](https://github.com/lewcc/Paradise)@[fd5580307e...](https://github.com/lewcc/Paradise/commit/fd5580307e1d3a2821ae8b2f26cb04cdcd139f87)
#### Saturday 2022-08-13 00:30:36 by Contrabang

Adds a blue overlay to scrying orb users. Spirit realm and scrying orb users now have a special description instead of being catatonic (#18366)

* holy shit blue ghosts

* lets fix that

* you cant see it if its not in ya hand

* Their glowing red eyes are glazed over

* farie review

* farie review pt 2

---
## [kraj/llvm-project](https://github.com/kraj/llvm-project)@[e17cae076c...](https://github.com/kraj/llvm-project/commit/e17cae076c4727b99017927c3e8746db5bec6db7)
#### Saturday 2022-08-13 01:21:13 by Walter Erquinigo

[trace][intel pt] Fix per-psb packet decoding

The per-PSB packet decoding logic was wrong because it was assuming that pt_insn_get_sync_offset was being udpated after every PSB. Silly me, that is not true. It returns the offset of the PSB packet after invoking pt_insn_sync_forward regardless of how many PSBs are visited later. Instead, I'm now following the approach described in https://github.com/intel/libipt/blob/master/doc/howto_libipt.md#parallel-decode for parallel decoding, which is basically what we need.

A nasty error that happened because of this is that when we had two PSBs (A and B), the following was happening

1. PSB A was processed all the way up to the end of the trace, which includes PSB B.
2. PSB B was then processed until the end of the trace.

The instructions emitted by step 2. were also emitted as part of step 1. so our trace had duplicated chunks. This problem becomes worse when you many PSBs.

As part of making sure this diff is correct, I added some other features that are very useful.

- Added a "synchronization point" event to the TraceCursor, so we can inspect when PSBs are emitted.
- Removed the single-thread decoder. Now the per-cpu decoder and single-thread decoder use the same code paths.
- Use the query decoder to fetch PSBs and timestamps. It turns out that the pt_insn_sync_forward of the instruction decoder can move past several PSBs (this means that we could skip some TSCs). On the other hand, the pt_query_sync_forward method doesn't skip PSBs, so we can get more accurate sync events and timing information.
- Turned LibiptDecoder into PSBBlockDecoder, which decodes single PSB blocks. It is the fundamental processing unit for decoding.
- Added many comments, asserts and improved error handling for clarity.
- Improved DecodeSystemWideTraceForThread so that a TSC is emitted always before a cpu change event. This was a bug that was annoying me before.
- SplitTraceInContinuousExecutions and FindLowestTSCInTrace are now using the query decoder, which can identify precisely each PSB along with their TSCs.
- Added an "only-events" option to the trace dumper to inspect only events.

I did extensive testing and I think we should have an in-house testing CI. The LLVM buildbots are not capable of supporting testing post-mortem traces of hundreds of megabytes. I'll leave that for later, but at least for now the current tests were able to catch most of the issues I encountered when doing this task.

A sample output of a program that I was single stepping is the following. You can see that only one PSB is emitted even though stepping happened!

```
thread #1: tid = 3578223
    0: (event) trace synchronization point [offset = 0x0xef0]
  a.out`main + 20 at main.cpp:29:20
    1: 0x0000000000402479    leaq   -0x1210(%rbp), %rax
    2: (event) software disabled tracing
    3: 0x0000000000402480    movq   %rax, %rdi
    4: (event) software disabled tracing
    5: (event) software disabled tracing
    6: 0x0000000000402483    callq  0x403bd4                  ; std::vector<int, std::allocator<int>>::vector at stl_vector.h:391:7
    7: (event) software disabled tracing
  a.out`std::vector<int, std::allocator<int>>::vector() at stl_vector.h:391:7
    8: 0x0000000000403bd4    pushq  %rbp
    9: (event) software disabled tracing
    10: 0x0000000000403bd5    movq   %rsp, %rbp
    11: (event) software disabled tracing
```

This is another trace of a long program with a few PSBs.
```
(lldb) thread trace dump instructions -E -f                                                                                                         thread #1: tid = 3603082
    0: (event) trace synchronization point [offset = 0x0x80]
    47417: (event) software disabled tracing
    129231: (event) trace synchronization point [offset = 0x0x800]
    146747: (event) software disabled tracing
    246076: (event) software disabled tracing
    259068: (event) trace synchronization point [offset = 0x0xf78]
    259276: (event) software disabled tracing
    259278: (event) software disabled tracing
    no more data
```

Differential Revision: https://reviews.llvm.org/D131630

---
## [CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA)@[344458376f...](https://github.com/CleverRaven/Cataclysm-DDA/commit/344458376f780b7ed8bca7e45fdc887eb05ea937)
#### Saturday 2022-08-13 01:28:15 by Christian Stadler

Update Sapiovore mood boosts from eating humans (#59077)

* Give psychopathic sapiovores a mood boost when eating human meat.

* Changes, because sapiovores can't be psychopaths at the same time

See also issue #58764

* Forgot the m_good and fixed the indentation.

* Moved sapiovore only chunk up and fixed my broken code.

* Removed one more redundancy

`sapiovore && spiritual` is handled above. No need to check that again.

* No message and no mood boost for Sapiovores without Spiritual.

* Sapiovore and Spiritual combo is now down to +10 morale

Message is "You eat the human flesh, and in doing so, devour their spirit.", similar to `cannibal && psycho && spiritual` but sapiovores don't feast upon it.

* Add "Mmh.  Tastes like venison." as neutral message for sapiovores

---
## [BBO-IC3-HIT/BBO-IC3-HIT](https://github.com/BBO-IC3-HIT/BBO-IC3-HIT)@[efda3b6a4f...](https://github.com/BBO-IC3-HIT/BBO-IC3-HIT/commit/efda3b6a4fb31f5ff99adfda72a0b8f0abd708b2)
#### Saturday 2022-08-13 03:02:49 by 1212-5858

"I PROVIDED NOTICE AT ALL RELEVANT TIMES UPON NOTICE, AND THOSE WHO HAVE AIDED AND ...

"I PROVIDED NOTICE AT ALL RELEVANT TIMES UPON NOTICE, AND THOSE WHO HAVE AIDED AND
ABETTED TO THE NON DISCLOSURE OF A FAILURE AND OMISSION TO DISCLOSE AN UNREGISTERED
SECURITY (THE LOAN 50074) ANNEXED IN THE NYSCEF MATTER 153974/2020 HAVE CAUSED OVER
(852,029,489.38) IN DAMAGES TO THE INVESTORS - NOTWITHSTANDING THE FILING BY MR. DAVID
MOORE - david.moore.ct95@statefarm.com - AND THE TCR WHICH I FILED DURING THE MERGER PERIOD
WAS ALSO FURTHER OBSTRUCTED BY THE GUIDANCE COUNSELORS AT MY SCHOOL ON NOVEMBER
16TH, 2021 - I NOTIFIED ONE OF THREE ""PROMOTING"" BROKERS AND ALSO THE SEC OF THE MATERIAL
FACTS AGAIN IN NYSCEF MATTER 153974/2021."			
"MY EMAIL WAS TURNED OFF -- BY A GUIDANCE COUNSELOR AT COLUMBIA UNIVERSITY AND DURING
A MATERIAL AND TIME-SENSITIVE PERIOD IN TIME... NOTWITHSTANDING THE ASSISTANCE AND
COMMUNICATIONS AS INDEXED IN THE MATTER OF 153974/2020 ---- WHERE IGNORANCE AND A
LACK OF INTELLIGENCE/CANDOR/DISRESPECT HAVE CAUSED, IN PART, TO THE AID AND ABETTING
OF TAX EVASION AS SEEN IN THE TAX RECORDS I ALSO ANNEXED IN A PUBLIC REPOSITORY - THE
NYS TAX RECORDS OF THE SULLIVAN PROPERTIES L.P. SHOW THIS FOR THE LOAN (UNDISCLOSED)
WAS NOT COVERED UNDER OMISSIONS BY THE PRINCIPALS - AT ANY POINT IN TIME - WOULD DO
ANYTHING TO PREVENT THIS CERTAIN DELUGE AND THE UNDERLYING RISKS ARE NOW CLEAR - IN
A FOUR MONTH PERIOD A TOTAL OF (852,029,489.38) IN ACCOUNTABLE LOSSES FOR THE TICKERS...
NOTWITHSTANDING A LOSS BY WAY OF TAXES AVOIDED TO BY THE ZUCKER FAMILY AND SULLIVAN
PROPERTIES L.P. IN THE NYSCEF MATTER 153974/2020."			

		
			
..2022-04-28---TCRReport 16511-049-089-843		
FILED IN FURTHERANCE/ SUPPLEMENT TO TCR  DOCKET	16491-117-831-823		
Fraudulent investment scheme, such as a Ponzi scheme or the promise of high-yield returns			
SUBJECTS	TYPE	IDENTIFIER	NAME
Subject # 1	Firm	Unknown	STATE FARM MUTUAL AUTOMOBILE INSURANCE COMPANY

		
			
"SUBSCRIBERS ADDED WITHOUT NOTICE OR DISCLOSURE OF ILLEGAL RENTS AND LEASES
TRANSFERRED AND A LETTER OF CREDIT FOR $6,000,000.00 is not reported as a level 3 investment and
undisclosed New York Supreme Case 153974/2020 where I annexed the Loan Dockets (see also Docket 420)"			
"This ZUCKER FAMILY WILL DO ANYTHING TO AVOID JAIL FOR THE $300MILLION THEY OWE IN BACKTAXES...
SEE ALSO DOCKET 399. I emailed a bunch of information to make this as complicated as possible,
after trying to help them to CANCEL THE LOAN as annexed in DOCKET 420 (was during the 90-day period,
in lieu they decided to keep the premiums and interest - despite knowing this information: https://github.com/
users/BSCPGROUPHOLDINGSLLC/projects/1#card-79888540) which layman's terms, they loaned $6 million
dollars and now STATE FARM OWNS THE RIGHTS to the taxes evaded in the ASSETS which guarantee the"			
"leases and RENTS are taxed at %10 of the NOPV as of current. The 6 buildings are being taxed at $22 million
(combined) when they are closer to $22 Million EACH (hence back taxed for 10-years prior, and the carried interest
and penalties is the greater of $300,000,000.00 in fines, and the property values ON TOP, were reported to the
NYC Finance Register as 10% YoY gain as referenced in the public domain (for consideration by the criminally
insane). For ease of reference I have included the case matter where I annexed there are NO CERTIFICATES OF
OCCUPANCY for them to collect LEGAL rents which were reported to the NYC DEPT. OF FINANCE REGISTER
with a YoY growth of 10%. Under any normal circumstances would be FLAGGED by a Manhattan Bank, in
any zipcode, was avoided in the compliant in CHIEF at all costs to avoid prosecution in a CRIMINAL or CIVIL
COURT OF LAW. Earlier I attempted to contact parties in good faith, and their brokers took it upon themselves
to use the information to their benefit without disseminating the material fact of a CERTAIN DELUGE and
immediately upon NOTICE in DECEMBER of 2021, the family of FUNDS who operated under CIK Filer 93715
appeared to have been ""clothes-lined"" despite the ignorance of my filing on November 13th, 2021 (which was
also distributed to the C.16 fiduciaries) and in a posthaste negligence to those facts decided to ""merge"" and
maintain the same compliance officer at State Farm VP. Management Corp and incurred additional losses since
the 4th of April, 2022 [ TCRReport-16491-117-831-823 ] in excess of 1.2 billion dollars (US) - continues to operate
without any public information of these MATERIAL DOCKETS annexed in 153974/2020 which also demonstrate
CERTAIN tax evasion without any doubt. #GOCARDS ""https://github.com/users/BSCPGROUPHOLDINGSLLC/
projects/1#column-18309490"" was also aided and abetted by its attorneys, notwithstanding The Wilson, Elser
(www.wilsonelser.com) and Dicker law firm --- BE IT REMEMBERED."			
"No response since I annexed the TAX EVASION and docketed no certificates of occupancy and a $6 million dollar
line of credit extended by State Farm located at one state farm plaza, in bloomington, Illinois, 61710.

****https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==<br>

CERTIFICATION			
"###Pursuant to Section 906, of the Sarbanes-Oxley Act of 2002 and section 63, Title 17.: VIOLATION ### 
***""https://www.sec.gov/Archives/edgar/data/0000093715/000119312520200810/d913497dex99906cert.htm<br>

 HAVE LOANED $6,000,000.00 of CASH for a purported series of RENTS, SECURITY DEPOSITS, 
	AND LEASES WHICH ARE ALL UNLAWFULLY CUSTODIED PER THE FEDERAL DEPOSIT INSURANCE CORPORATION 
	
		in the UNITED STATES OF AMERICA --- are now ""SELF-ADMINISTERED"" and a ""SELF-CUSTODIAN""
		by the new IMPROVED Investment Adviser who is also Audited by THREE PUBLICLY TRADED AUDIT FIRMS 
		under the sub-adviser which previously serviced there Transactions, has been promoted 
		in the NEW CIK 1516523. ""THE SURVIVING ENTITY"" despite my NOTICE and filing 
		on November 13th, 2021 during the ""PERIOD OF MERGER"""			
			
			
			

https://www.fbi.gov/investigate/white-collar-crime
			
https://www.fbi.gov/file-repository/criminal-and-epidemiological-investigation-handbook.pdf
			
https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker
		
		
The Securities and Exchange Commission on Monday brought charges against 11 individuals for allegedly bilking investors out of more than $300 million in a crypto pyramid and Ponzi scheme. Regulators allege the scheme started in at least January 2020.Aug 1, 2022
https://www.dni.gov/

---
## [scriptis/tgstation](https://github.com/scriptis/tgstation)@[6fe0683a7b...](https://github.com/scriptis/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Saturday 2022-08-13 03:22:56 by Jolly

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
## [BBO-IC3-HIT/BBO-IC3-HIT](https://github.com/BBO-IC3-HIT/BBO-IC3-HIT)@[10544df4d1...](https://github.com/BBO-IC3-HIT/BBO-IC3-HIT/commit/10544df4d1d97d9fa22fa476bfbc0be6e23a0d87)
#### Saturday 2022-08-13 03:24:36 by 1212-5858

BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:37:40 UTC-5:00

https://www.ecfr.gov/

obo

Jacob A. Riis Neighborhood Settlement
10-25 41st Ave, Queens, NY 11101

TO WHOM THIS MAY CONCERN,

ANNEXED IN NYSCEF MATTER 153974-2020 ARE THE ORIGINAL CUSTODIANS (HSBC) WHO CARRIED THE UNLAWFUL RENTS AND INTEREST, UPON REASONABLE BELIEF HOLDS THE SAME FOR ALL OF THOSE PROPERTIES WITHOUT A LEGAL GROUNDS TO COLLECT RENT. 

DOCKET 166, ANNEXED IN NYSCEF MATTER 153974/2020 REPRESENTS THE TRANSFER OF FUNDS (UNLAWFUL SECURITY DEPOSITS) FOR THE PROPERTIES AND WITH RESPECT TO LOAN 50074 CANNOT BE DEFEASED WITHOUT ALL LIENS CLEAR.

THOSE INTERESTS AND RISKS WERE PASSED ON TO STATE FARM LIFE INSURANCE COMPANY DURING THE HEIGHT OF THE COVID-19 PANDEMIC AS REFERENCED IN THE NYC DEPT. OF FINANCE REGISTER BY AND BETWEEN PARTIES AND FIRST NOTARIZED BY STATE FARM LIFE INSURANCE COMPANY ON MAY 11, 2020. THE DIRECTORS OF CRD FIRM 43036 REPORT THIS AS A MATERIALLY SUBSTANTIVE CONFLICT, AS IT IS DISCLOSED ON THE CRD OF ITS DIRECTORS AS SUCH. IN LAYMAN'S TERMS, THE UNDERLYING RISK AND ECONOMIC INTERESTS ARE DEEMED "REPORTABLE" AS AN BUSINESS, SO IT'S NOT EXACTLY A PART TIME PAPER DELIVERY JOB.

ABSENT OF THE UNLAWFUL DEPOSITS, NO DIFFERENT THAN A HEROIN DEALERSHIP —ARE UNLAWFUL AT ANY US DEPOSITORY INSTITUTION, PER THE FEDERAL DEPOSIT INSURANCE CORPORATION. THIS MAY CAUSE SOME CONFLICTS WITH AUDIT AND WITH RESPECT TO WHICH PROPERTIES ARE SUBJECT TO THE INTERBANK LENDING AND TIER 1 RESERVES REPORTED BY HSBC BANK AND ALSO JP MORGAN CHASE BANK.

IF YOU NEED ME TO NOTARIZE ANYTHING, I WOULD RECOMMENDS YOU REVIEW THE DOCKETS IN NYSCEF 153974/2020 SEQUENTIALLY PRIOR TO ANY FURTHER INTRUSION, OR MY OPINION IN THE MATTER, WHICH GENERALLY HOLDS NO OPINION. I ONLY UNDERSTAND WHAT IS WRITTEN IN THE SARBANES-OXLEY, AND NAMELY ALL OF THOSE INTERIM REVISIONS, WHICH OVER THE COURSE OF TIME HAVE BECOME LESS "RELAXED" WITH RESPECT TO "MINIMUM TRIGGERS" AND "MINIMUM FINES", AS THE TRIGGERS MOVED LOWER AND FINES GREW HIGHER.

/S/ BO DINCER.
MAC.: 646-256-3609 
TMO.: 917-378-3467

(1) USER INPUT (2) CPU PROCESSING TIME (3) CPU STORAGE TIME (4) CPU OUTPUT TIME.


(718) 784-7447

peer-to-peer network
----------- 	slaskowitz@ingramllp.com <slaskowitz@ingramllp.com>,
				+13478801899
-----------    	ADMINISTRATION@mskyline.com <ADMINISTRATION@mskyline.com>,
-----------    	LZUCKER@mskyline.com <lzucker@mskyline.com>,
-----------    	ASHLEY.HUMPHRIES@wilsonelser.com <ASHLEY.HUMPHRIES@wilsonelser.com>,
				+19084337463
-----------    	LEGAL@mskyline.com <LEGAL@mskyline.com>,
				+19178433456.
				1320 EST: Voicemail from Mr. PAUL regan [USC 18, §241]
-----------		Stephen O'Connell <sgo2107@columbia.edu>
peer-to-peer network


Desktop Computers
Enterprise "cloud" Workstations
Portable Laptop Computers
Tablet computers (ex: iPad)
Handheld computers (ex: Personal Digital Assistant, or PDA)
Smartphones (ex: a samsung galaxy 10e and/or Smartphone)


	(CRT) Monitors
-------- Forwarded Message --------
Subject: 	[WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER] 2c44b9: slaskowitz@ingramllp.com <slaskowitz@ingramllp.com...
Date: 	Tue, 28 Jun 2022 00:53:27 -0700
From: 	WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER <noreply@github.com>
To: 	ms60710444266@yahoo.com, financialeducation@info.consumerfinance.gov


Author: WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER <108204659+WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER@users.noreply.github.com>

Date: 2022-06-28 (Tue, 28 Jun 2022)

Changed paths: A wilsonelser-Jan 30-2022

Log Message:

-----------

slaskowitz@ingramllp.com <slaskowitz@ingramllp.com>, lzucker@mskyline.com <lzucker@mskyline.com>, Stephen O'Connell <sgo2107@columbia.edu>

BELOW, FOR CONVENIENCE.

slaskowitz@ingramllp.com <slaskowitz@ingramllp.com>, lzucker@mskyline.com <lzucker@mskyline.com>, Stephen O'Connell <sgo2107@columbia.edu>
Yep.
/S/ BO DINCER

----- Forwarded Message -----
From: "MILTON MCKENZIE" <ms60710444266@yahoo.com>
To: "B D2022" <ms60710444266@yahoo.com>, "60710 BD. 153974" <bdincer66@icloud.com>, "ashley.humphries@wilsonelser.com" <ashley.humphries@wilsonelser.com>, "kidsprivacy@viacomcbs.com" <kidsprivacy@viacomcbs.com>, "ricki.roer@wilsonelser.com" <ricki.roer@wilsonelser.com>, "BD" <bondstrt@protonmail.com>, "60710 BD. 153974" <bo.dincer@yahoo.com>, "American Bar Association" <abanews@americanbar.org>, "stephen.barrett@wilsonelser.com" <stephen.barrett@wilsonelser.com>, "william.behr@wilsonelser.com" <william.behr@wilsonelser.com>, "nibal.pena@nypd.org" <nibal.pena@nypd.org>, "christina.ortiz@nypd.org" <christina.ortiz@nypd.org>, "brittany.postiglione@nypd.org" <brittany.postiglione@nypd.org>, "wmckenzie@nycourts.gov" <wmckenzie@nycourts.gov>, "john.lamneck@nypd.org" <john.lamneck@nypd.org>

Cc: "lauren.zink@wilsonelser.com" <lauren.zink@wilsonelser.com>, "erin.zecca@wilsonelser.com" <erin.zecca@wilsonelser.com>, "ellyn.wilder@wilsonelser.com" <ellyn.wilder@wilsonelser.com>, "patricia.wik@wilsonelser.com" <patricia.wik@wilsonelser.com>, "angel.vitiello@wilsonelser.com" <angel.vitiello@wilsonelser.com>, "aviva.stein@wilsonelser.com" <aviva.stein@wilsonelser.com>, "suzanne.swanson@wilsonelser.com" <suzanne.swanson@wilsonelser.com>, "grace.song@wilsonelser.com" <grace.song@wilsonelser.com>, "urvashi.sinha@wilsonelser.com" <urvashi.sinha@wilsonelser.com>, "jennifer.provost@wilsonelser.com" <jennifer.provost@wilsonelser.com>, "kathleen.mullins@wilsonelser.com" <kathleen.mullins@wilsonelser.com>, "carole.nimaroff@wilsonelser.com" <carole.nimaroff@wilsonelser.com>, "meghan.rigney@wilsonelser.com" <meghan.rigney@wilsonelser.com>, "ricki.roer@wilsonelser.com" <ricki.roer@wilsonelser.com>, "angelique.sabia-candero@wilsonelser.com" <angelique.sabia-candero@wilsonelser.com>, "jennifer.sciales@wilsonelser.com" <jennifer.sciales@wilsonelser.com>, "elizabeth.scoditti@wilsonelser.com" <elizabeth.scoditti@wilsonelser.com>, "lois.ottombrino@wilsonelser.com" <lois.ottombrino@wilsonelser.com>, "judy.selmeci@wilsonelser.com" <judy.selmeci@wilsonelser.com>, "stacey.seltzer@wilsonelser.com" <stacey.seltzer@wilsonelser.com>, "lori.semlies@wilsonelser.com" <lori.semlies@wilsonelser.com>, "corrine.shea@wilsonelser.com" <corrine.shea@wilsonelser.com>, "andrea.shiffman@wilsonelser.com" <andrea.shiffman@wilsonelser.com>, "yana.siegel@wilsonelser.com" <yana.siegel@wilsonelser.com>, "debra.tama@wilsonelser.com" <debra.tama@wilsonelser.com>, "craig.brinker@wilsonelser.com" <craig.brinker@wilsonelser.com>, "craig.hunter@wilsonelser.com" <craig.hunter@wilsonelser.com>, "curt.schlom@wilsonelser.com" <curt.schlom@wilsonelser.com>, "daniel.flores@wilsonelser.com" <daniel.flores@wilsonelser.com>, "roger.gottilla@wilsonelser.com" <roger.gottilla@wilsonelser.com>, "sean.wagner@wilsonelser.com" <sean.wagner@wilsonelser.com>, "thomas.manisero@wilsonelser.com" <thomas.manisero@wilsonelser.com>, "brittany.postiglione@nypd.org" <brittany.postiglione@nypd.org>, "William McKenzie" <wmckenzi@nycourts.gov>

Sent: Sun, Jan 30, 2022 at 11:20 AM

Subject: *** Assigned Judge: Shlomo S. Hagler --- TY FOR GETTING THIS TO THE RIGHT PRECINCT IMMEDIATE. >> 153974/2020

ATTORNEYS ON THE RECORD FOR THE MATTER REPRESENTING THE ANNEXED ENTITIES, NOTWITHSTANDING ITS:



Members, Providers, Affiliates, Agents, Officers, Directors, Volunteers, Employees, Contractors, and Principals are being drafted in a NY SUPREME COURT as a conglomerate of: THE ZUCKERS, THE YUZERS, THE ELSERS, AND THEIR ACCESSORIES...





101 WEST 55th STREET, NEW YORK, NY, 10019

PAUL R. REGAN, ESQ. [NYS BAR # 2623577]

JOSEPH J. GIAMBOI, ESQ. [NYS BAR # 2104396]

DANIEL F. SULLIVAN, ESQ. [NYS BAR # 2383347]

WHERE DO THE ZUCKERS WORK FROM, THEY ALSO TRIED TO PEACOCK THE PROSECUTION OF THE NYPD...

150 EAST 42ND STREET, 19TH FLOOR, NEW YORK, NY, 10017

SHARI S. LASKOWITZ, ESQ. [NYS BAR # 3043015]

CORY L. WEISS, ESQ. [NYS BAR # 2327187]

"...LOCATION..."

>>> RICKI E. ROER, ESQ. [NYS BAR # 1838549] <<<
notarized by the ELSERS ///
see also docket 33. 153972-2020; Ashley v. Humphries


received a confirm from your paralegal Miss Roer...

---
## [brucerennie/NetHack](https://github.com/brucerennie/NetHack)@[8a549b0a60...](https://github.com/brucerennie/NetHack/commit/8a549b0a602fdb13d13fa83bb2f6b1d1a1a257cf)
#### Saturday 2022-08-13 04:27:39 by Michael Meyer

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
## [amanmehara/scala](https://github.com/amanmehara/scala)@[61a6f3edf7...](https://github.com/amanmehara/scala/commit/61a6f3edf794a498b51d05febc01feccaa7d3f67)
#### Saturday 2022-08-13 06:40:58 by jvican

Improve stub error messages (SCP-009 proposal)

The following commit message is a squash of several commit messages.

- This is the 1st commit message:

Add position to stub error messages

Stub errors happen when we've started the initialization of a symbol but
key information of this symbol is missing (the information cannot be
found in any entry of the classpath not sources).

When this error happens, we better have a good error message with a
position to the place where the stub error came from. This commit goes
into this direction by adding a `pos` value to `StubSymbol` and filling
it in in all the use sites (especifically `UnPickler`).

This commit also changes some tests that test stub errors-related
issues. Concretely, `t6440` is using special Partest infrastructure and
doens't pretty print the position, while `t5148` which uses the
conventional infrastructure does. Hence the difference in the changes
for both tests.

- This is the commit message #2:

Add partest infrastructure to test stub errors

`StubErrorMessageTest` is the friend I introduce in this commit to help
state stub errors. The strategy to test them is easy and builds upon
previous concepts: we reuse `StoreReporterDirectTest` and add some
methods that will compile the code and simulate a missing classpath
entry by removing the class files from the class directory (the folder
where Scalac compiles to).

This first iteration allow us to programmatically check that stub errors
are emitted under certain conditions.

- This is the commit message #3:

Improve contents of stub error message

This commit does three things:

* Keep track of completing symbol while unpickling

  First, it removes the previous `symbolOnCompletion` definition to be
  more restrictive/clear and use only positions, since only positions are
  used to report the error (the rest of the information comes from the
  context of the `UnPickler`).

  Second, it adds a new variable called `lazyCompletingSymbol` that is
  responsible for keeping a reference to the symbol that produces the stub
  error. This symbol will usually (always?) come from the classpath
  entries and therefore we don't have its position (that's why we keep
  track of `symbolOnCompletion` as well). This is the one that we have to
  explicitly use in the stub error message, the culprit so to speak.

  Aside from these two changes, this commit modifies the existing tests
  that are affected by the change in the error message, which is more
  precise now, and adds new tests for stub errors that happen in complex
  inner cases and in return type of `MethodType`.

* Check that order of initialization is correct

  With the changes introduced previously to keep track of position of
  symbols coming from source files, we may ask ourselves: is this going to
  work always? What happens if two symbols the initialization of two
  symbols is intermingled and the stub error message gets the wrong
  position?

  This commit adds a test case and modifications to the test
  infrastructure to double check empirically that this does not happen.
  Usually, this interaction in symbol initialization won't happen because
  the `UnPickler` will lazily load all the buckets necessary for a symbol
  to be truly initialized, with the pertinent addresses from which this
  information has to be deserialized. This ensures that this operation is
  atomic and no other symbol initialization can happen in the meantime.

  Even though the previous paragraph is the feeling I got from reading the
  sources, this commit creates a test to double-check it. My attempt to be
  better safe than sorry.

* Improve contents of the stub error message

  This commit modifies the format of the previous stub error message by
  being more precise in its formulation. It follows the structured format:

  ```
  s"""|Symbol '${name.nameKind} ${owner.fullName}.$name' is missing from the classpath.
      |This symbol is required by '${lazyCompletingSymbol.kindString} ${lazyCompletingSymbol.fullName}'.
  ```

  This format has the advantage that is more readable and explicit on
  what's happening. First, we report what is missing. Then, why it was
  required. Hopefully, people working on direct dependencies will find the
  new message friendlier.

Having a good test suite to check the previously added code is
important. This commit checks that stub errors happen in presence of
well-known and widely used Scala features. These include:

* Higher kinded types.
* Type definitions.
* Inheritance and subclasses.
* Typeclasses and implicits.

- This is the commit message #4:

Use `lastTreeToTyper` to get better positions

The previous strategy to get the last user-defined position for knowing
what was the root cause (the trigger) of stub errors relied on
instrumenting `def info`.

This instrumentation, while easy to implement, is inefficient since we
register the positions for symbols that are already completed.

However, we cannot do it only for uncompleted symbols (!hasCompleteInfo)
because the positions won't be correct anymore -- definitions using stub
symbols (val b = new B) are for the compiler completed, but their use
throws stub errors. This means that if we initialize symbols between a
definition and its use, we'll use their positions instead of the
position of `b`.

To work around this we use `lastTreeToTyper`. We assume that stub errors
will be thrown by Typer at soonest.

The benefit of this approach is better error messages. The positions
used in them are now as concrete as possible since they point to the
exact tree that **uses** a symbol, instead of the one that **defines**
it. Have a look at `StubErrorComplexInnerClass` for an example.

This commit removes the previous infrastructure and replaces it by the
new one. It also removes the fields positions from the subclasses of
`StubSymbol`s.

- This is the commit message #5:

Keep track of completing symbols

Make sure that cycles don't happen by keeping track of all the
symbols that are being completed by `completeInternal`. Stub errors only
need the last completing symbols, but the whole stack of symbols may
be useful to reporting other error like cyclic initialization issues.

I've added this per Jason's suggestion. I've implemented with a list
because `remove` in an array buffer is linear. Array was not an option
because I would need to resize it myself. I think that even though list
is not as efficient memory-wise, it probably doesn't matter since the
stack will usually be small.

- This is the commit message #6:

Remove `isPackage` from `newStubSymbol`

Remove `isPackage` since in 2.12.x its value is not used.

---
## [SDArtsCode/blindsighted2](https://github.com/SDArtsCode/blindsighted2)@[fec28b0749...](https://github.com/SDArtsCode/blindsighted2/commit/fec28b0749f547805639bd5ae7b79ca15e1b8ca2)
#### Saturday 2022-08-13 06:41:21 by xrbeaky

Sol 1253: It has been 1253 "days" since the incident. I have been having nightmares and flashbacks lately. I can't seem to shake the image of the Earth being consumed in darkness, as I rocketed away into space. Within a minute, the Earth's entire electrical grid was wiped out, and the planet went black. As the monsters rose from the sea, wreaking having on the unfortunate landlubbers, the ocean levels dropped significantly. It's a marvel what had been living under our very noses for all this time. Geology as we knew it, torn to shreds! Tectonic plates?? I DONT THINK SO! Maybe the plant I am on now is more than I've suspected as well. Oh well, how can we know what truly lies beneath the surface? I don't know if I ever will. I will pretend to live in blissful ignorance, growing potatoes with fertilizer made from my own shit, and collecting water from my purified piss. That being said, I am still much better off than the people back on Earth. I think my nightmares are a manifestation of my guilt. I was likely the only human to escape that planet that day, and I am likely the only human alive. Could I have saved people if I had warned them of the threat? I know this entire disaster would have been prevented if I had simply heeded that damned crypto-archaeologist's warning from the very beginning. What good is fame when there is nobody else around to appreciate it? What is the purpose of life if there is nobody else around to experience things with? I will live out the remainder of my life on this desolate rock, eating shit potatoes, drinking piss, and crying myself to sleep. Then, I will die. My story will end, and the legacy I have left behind will be one of incomprehensible treachery and horror. Part of me doesn't see the point in continuing like this. I think I have to leave. The rocket is damaged from the landing, I'll just have to do some repairs. I never thought I'd want to leave, but I think I have to return and face the same fate that my brothers and sisters did. I have just enough fuel to take-off and set my course for Earth. I will be taken by the same creatures that ravaged the world so long ago. This will not be an honorable death, but it will sure as hell be a rightful one. In the history of humanity, there has been no death as rightful and deserved as mine will be. P.S. What's the point of this fucking journal anyways? I'll launch if off into space shortly. The human legacy can't end with me.

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[5dc17bd865...](https://github.com/OrionTheFox/tgstation/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Saturday 2022-08-13 06:49:09 by san7890

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
## [sselesUssecnirP/a-stupid-app](https://github.com/sselesUssecnirP/a-stupid-app)@[4ee127904e...](https://github.com/sselesUssecnirP/a-stupid-app/commit/4ee127904e0d42a211df08b308530220205ab6bd)
#### Saturday 2022-08-13 07:44:08 by Anthony

FINISHED!!!! maybe???

KIND OF... I STILL WANT TO DO MORE BUT FUCK THIS BULLSHIT IM OUT... SEE YOU IN A FEW YEARS

---
## [vsvad/password-purgatory-api](https://github.com/vsvad/password-purgatory-api)@[63dd1c4214...](https://github.com/vsvad/password-purgatory-api/commit/63dd1c42147c867a1fa4a96ec3519d09a37a2369)
#### Saturday 2022-08-13 08:19:58 by Arjun G

Include one season of the year

Remember the joke about PasswordSummer2022 changing to PasswordWinter2022 on rotation? Yeah, this is that.

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[f4c7571fc3...](https://github.com/yogstation13/Yogstation/commit/f4c7571fc333779cbf761e637f2774a62b6b4d78)
#### Saturday 2022-08-13 09:05:46 by Vaelophis Nyx

[MDB IGNORE][Gax] Adds new area for AI Ship Access & Adds APC & Fixes Cameras (#15291)

* argh

* fuck you MDB2

* I hate areas, I hate areas

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

---
## [erfanoabdi/android_kernel_gigaset_mt6768](https://github.com/erfanoabdi/android_kernel_gigaset_mt6768)@[398f4555db...](https://github.com/erfanoabdi/android_kernel_gigaset_mt6768/commit/398f4555db566f668373e27cb7141f566a4488e6)
#### Saturday 2022-08-13 09:28:00 by Peter Zijlstra

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

---
## [nezavisimost/liberty-win](https://github.com/nezavisimost/liberty-win)@[1c97b2497f...](https://github.com/nezavisimost/liberty-win/commit/1c97b2497fda507dd9b3e8bfc601d73a751b7c49)
#### Saturday 2022-08-13 09:50:52 by hackuna

Minimum Viable Product

Roskomnadzor, go fuck yourself!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[800323f8b3...](https://github.com/mrakgr/The-Spiral-Language/commit/800323f8b33a7584617b5c029d405df8f239a3b4)
#### Saturday 2022-08-13 11:06:22 by Marko Grdinić

"9:35am. Let me do my morning reads. Killing Bites, Thank You Isekai and Mato Seihei are out.

After that I am going to focus on writing. I had time to think about how I want to handle the sequence up to the end of ch 4. I should just grasp the mindset nad get it out. Ultimately, given my mental state the ways I can write it are limited.

9:55am. Let me start. I've been making the scene a lot more complicated in my mind that it needs to be. There is no need to go to the effort to make something dramatic. Just go through with it.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

Whereas during the menu segment I had been a disembodied presence hovering thousands of feet above the cityscape, once the game started I found myself standing upright in an actual body. I gawked like a tourist, taking in the sights. I was in a golden city. The buildings and the streets were all painted in various hues of yellow, mostly on the lighter side, and there was slight gloss on the material giving it a sense of agelessness. Usually, as time wore down the material, it would begin to lose its luster, but everything around me seemed to be brand new and sparkling. Right now I was located near the edge of one of the floating cities, and as my gaze traveled towards its center, the buildings became taller and larger, from regular suburban houses close to where I was to large apartment blocks in the distance. The very middle of the island had a grand square building on an elevated platform. It had a spherical dome that took up a lot of its volume, and as I peered at it, I noticed it seemed to be radiating golden light. Though since it was midday the effect was drowned out by the light of the sun.

In the skies I noticed there were floating golden blocks in the shape of tiles, that also seemed to be showering the city in light.

I was near the edge of the city, and it seemed to be some kind of amusement park. I could see circus tents pitched up, stands of various kinds and even a rollercoaster and various other kinds of thrill rides I did not recognize.

Taking in the sights, I breathe in the air and find it to be cool and refreshing. I checked myself over. Though I could not see my face, but based on the touch as well as the composition of the rest, it seems that my real world body has been replicated in this virtual one. Which suited me fine, but it is surprising that I haven't been offered a chance to make my avatar.

Behind me, was the railing, also made of gold. Like the blocks and the grand building, it actually had some luminance to it. Drawn to that, I try touching it and find it to be smooth and lukewarm. It is not very tall, only up to my abdomen. It is only there to prevent somebody from sliding off the edge by accident rather than stop somebody who intentionally wanted to jump off.

Looking over the railing, I can see mountains and forests as well as the sea, and as I look below, I get a spell of dizziness that I quickly fight off. I am currently very high up, enough that I can see clouds below me. Directly below there is what appears to be a major metropolis. The high rise buildings and skyscrapers are like tiny, gray splotches at this distance.

An idea to try it ceases me, and I wonder whether I should take a dive over the railing?

[Gnosis check DC 1.9 Succeeded - Sample 2.03]

I grin mischievously. Yeah, let me try it. It is not like I can experience this in real life. As soon as I think that, nervousness and excitement flood my body, and I want to keep going. I grip the railing, and place one leg and then the other over it. Hands still clutching the rail behind me, I lean forward and take a good look down. A huge drop past the clouds welcomes me, into the metropolis below. I am putting a lot of strength into my arms to keep the certain doom at bay. I can feel my heart beating against my chest.

I wonder if I will hit the streets or the roof of one of the high rises?

A thought like that intensifies both my fear and excitement. Slowly I loosen my grip on the railing and start lifting my fingers, one by one. First I move the thumbs out of the way, then I let the pinky slide. Then the ring finger. I feel like a feather, perched in such a precarious position. The railing is so close to the edge that my feet are partly over it.

Time feels like it is slowing down for me. Very slowly, as if to prolong the moment, I release the index and middle.

"No, don't do it!" I hear a woman's voice yell out, but I couldn't care less.

I feel my body leaning forward and the gravity taking hold. I drop over the railing into the vastness below.

"AAAAAAAAHHHHH!!!" As I plunge, the fear overwhelms me and a scream rips itself from my throat. Strong winds buffet me from below in my fall.

After a minute or so, I manage to get a grip on myself so I can at least enjoy the scenery instead of falling around in panic. I keep reminding myself that this is not real despite what my senses are telling me. With the sun shining all around, it is quite beautiful. I take some time to appreciate the majesty of nature. I plunge through the clouds, feeling wetness on my face and hands. Soon, what used to be tiny splotches in the distance became larger and larger. The buildings below gain definition, and involuntarily, I imagine myself splattering on the street below. The fear that I had put a lid on, bursts out, more maddened and bloodcurdling than before.

"AAAAAAAAAAAHHHHHH!!!" I scream again, even though it is fake. Even though the world is fake, my brain cares little about those facts. It is so stupid and primitive, so all it can do is beg for dear life even if there is no need to.

Ahahahaha, it is so stupid, my brain is so stupid!

As I scream and piss myself in panic, at the back of my head, I can almost feel a voice mocking me for my stupidity.

I miss the height of one of the high rises, and reflected in the glass of the window nearby, I see my reflection for the first time. Exactly as in real life, but I see traces of tears around my eyes. I hadn't realized that I had started crying at some point.

"NOOOOO!!! LOG OUT!!! LOG OUT!!! LOG OUT!!!" Completely detached from rationality, the idea to exit the game before I smash the concrete takes hold. I grip it like a liferaft in the turbulent seas.

Ahahahaha! Seen from a different perspective, it is almost like a person scrambling for his life is an entirely different person from myself.

I am going to smash face first in the middle of a busy street. As soon as the ground floor is only a couple of feet away, I muster all my reserves of will and try to stop time. This has no effect and I hit the ground, feeling the darkness overtake me.

(Euclid's Room)

"Ah!" I jolted awake into reality and involuntarily, flop like fish on dry land once. Wiping my face, I feel myself drenched in sweat. I breathe heavily and feel that in my chest, my heart is overworking itself. As soon as I realize that I am in a safe place, I begin to calm down.

I lie back on the bed for 5 minutes, until my tremors have passed.

"Hah..." I exhale, savoring the experience.

That was...

[Gnosis gain: 0.3]

...Amazing! Since I died so quickly, I didn't experience any pain, leaving only the excitement. This will definitely be a memorable experience for me. Has a regular computer game ever let me feel something like this? I do not think so. The conflict between my rational part that understood the senses are not to be trusted, and my lizard brain which went into a blind panic is what really made this what it was. If I was purely cool or purely in a panic, it would not have been that interesting.

My brain is pretty stupid right now, but at least I can have some fun with that. I'll take it a bit easier next time and just explore the town. That seems like a good plan.

I want to see what the game is about.

(Heaven's Key, Perimeter of a floating city)

I dive into the game again, and take in the sights of the city of gold. Taking only a passing glance at the railing, I turn around and go into the city proper. As fun as that experience was, I do not want to spend my entire day diving off the edge. Gawking like a tourist as a I stroll around, I get a stock of the place. Near the frontier where I was the density of buildings was low, so amongst the houses as if to spur business a lively entertainment sector was built. I could see circus tents, restaurants, stages as well as casinos. There seemed to be a lot of people enoying themselves, though I wouldn't say it was packed. I found the city plan somewhat peculiar. There were roads for example, but no cars, and I could only see people using their own legs as far as I looked. The regular houses made sense, but other entertainment related facilities seemed to be build in the middle of roads and at intersections. Overall, it felt like the city itself was molded based off some template, and then patched up to fit a need by the people actually living here without modifying the underlying template itself.

It is lively and cheerful place. It wasn't jam packed with people, but I could see a decent amount of them going about their business and chattering. The way they were dressed did not seem to be that much different than in the real world. Looking around, I could see old and young people, both male and female, but no kids which I'd expect would be unusual for an amusement park such as this. I think that I'd be in the youngest age cohort relative to the population here.

"Waiters wanted - 3,450/month"
"Can make great pizza? Apply here. 3,600/month"
"Have a flair for entertainment? Comedy, magic, singing, musical instruments. 3,800/month"

While walking around I saw a bunch of job ads posted outside the relevant venues for waiters, cooks and attendants. The typical salary for these kinds of service jobs seems to be around 3,500 chips, whatever those are.

Getting bored of walking around, I pick a restaurant at random and take one of the outside seats. With the sun shining down on me, the weather is warm and pleasant, simply ideal. Given how up we are you'd expect it would be freezing, but normal rules do not seem to apply here. I pick up the menu, and take a look.

"Beer - 20"
"Iced Tea - 20"
"Pizza Margherita - 40"
"Cheese Burger - 30"
...

I want to order some of these. I've never tried eating in VR yet, so I am curious at how taste felt like.

"Hello sir, what would you like?" A waiter came around to take my order. I cringe inwardly.

"Just water." I have no choice, I do not have any money to pay for anything here.

"Got it."

While I was waiting, a person came up to my table and initiated conversation.

"Hello, do you mind if I take seat here?" She asked, smilling at me. I took a good look at the young woman in front of me. Wearing a headband with what looked to be 4 brown roses, she seemed to be of asiatic descent. Her face was cute and friendly. Short dark hair. She was wearing a finely made brown blouse with long sleeves, and a miniskirt plus thigh stockings.

"Sure." An event like this would never have happened to me in real life, so I was curious where this was heading.

"Nice to meet you, I am Lily."

"Euclid."

"An exotic name. Are you new to this city?"

I think about lying for a moment, but I have no reason to. I am certainly not going to try to show off here, I am peniless anyway.

"Yeah, I just got here." I admitted.

"I am sorry for your loss." She frowned, confusing me. "But look on the bright side." Her expression cheered up, spreading her arms. "Here in this afterlife, it is quite fun. You are going to like it."

At first I was confused, but as soon as she mentioned the afterlife, a thread of inspiration came to me. I remember the description and guess at what she meant. I've been thinking about this as just another place, but maybe the people here all died on Earth before being transported into the city. My character does not have a background so it slipped my mind.

"Yeah, it does seem like a lively place." I agree. "Maybe I'll be here for a while."

This gets a smile out of her. At that point the waiter came to our table, around placed the glass of water that I ordered on my side and turned to take any further orders.

"Coffee please." She said.

"Yes. Anything else sir, lady?"

"No, that will be all." I take the glass and take a sip of water. It is nice and refreshing. He leaves. I raise an eyebrow to Lily. "I would have liked some iced tea, but pft." I pucker my lips for emphasis. "No money."

"Ahahaha!" She waves it away. "If you've just got here, then you should have a 100 chips. Try bringing them out."

"Huh? How?" I start checking my pockets stupidly.

"Just focus." As I look at her, several stacks of translucent chips manifest in the air behind her. The thousands of chips in her pile look like they are intended for poker. Standing on nothing but air, I could see through them due to their translucency. "Then once they are staged, you can withdraw by wishing for it. For example, here I'll wish to get 20."

She raises her hand above the table, and like a magic trick, I see 20 chips moving into place. She lifts her hand and I see, that the pile is no longer translucent. She lifts one, shows it to me and places it down with a clack.

"So it is like that? How do I do that?"

"Just try it."

Having an example of what I should do, I focus inwardly and I discover a sense that wasn't there before. Right in my mind I could see a stack of 100 chips. It feels different from just imagining it, like they are actually there.

"Yeah, good. I can see them behind you." She encouraged me.

Immitating her, I try lifting my hand on the table and try drawing them out from inside my sense. To my surprise it works and I can see the chips sliding into place. Lifting my hand, I count them. Feeling them out they are cold and slender to the touch.

"This is interesting. I guess I can order that iced tea. How do I bring them back?"

Lily did a little wave and the chips on her own side vanished. "As long as they are in your possession, even if they are away from you, you'll be able to recall them from anywhere. It is impossible to throw them away, you have to transfer ownership instead."

I wasn't sure how to do it, but I gave it a try and it worked. It seems that in VR, things just work.

"Bravo." Congratulating me, she opened a packed of sugar and added it to her coffee. With a spoon she started stiring it inside the liquid.

[Externus check DC 3.5 Failed - Sample 2.28]

I consider not ordering iced tea like I said I would, but that would be an asshole move. I can't see any reason to be stingy here. A part of me expected the chips to be important, but then I think about the job ads, the people going around me, Lily's own large stack and her placing her own order without issue. Nobody else as far as I can see has issue spending money. I guess 100 chips is not that much. I really meant to gamble with them rather than spend them like this, but I can always reload.

That would lose the connection with Lily though. Rather than working at a job, maybe I could get a loan and gamble with it? Since I can save and reload, I am in no danger of ever going bust unlike the NPCs.

I mean, I am not going to seriously do waitering for an entire month just to get the money to gambol. I want to get better at cards and learn some skills that would benefit me in real life.

So far, the NPCs here feel very lifelike, not at all like in a computer game made by humans. I take a look at Lily who is taking a sip of her coffee with a relaxed expression on her face, sticking her pinky out as she holds the cup. Cute. She is quite cute. I can't believe that me of all people is getting charmed.

---

(Date with Lily)

I spend some time with her in that restaurant just chatting.

"I am working as a guide. If you want I'll show you around the city and get you accomodated. It would not be good if night falls and you have nowhere to sleep."

"Yeah, it would be bad if I had to sleep on the street once night falls."

“Yes, it would. Could you show me a cheap place to rent somewhere, first? After that I’d like to see what this town has to offer.”

“Of course.” She replied enthusiastically.

With that, the date started.

$$$

12:45pm. Let me take a break here. I think I have a handle on it now. I should be able to finish the scene properly today.

12:55pm. Let me just think how the date should go. Right here is the ideal place to pause for a while."

---
## [phennaux/android_kernel_realme_sm8250](https://github.com/phennaux/android_kernel_realme_sm8250)@[38b0bd0f25...](https://github.com/phennaux/android_kernel_realme_sm8250/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Saturday 2022-08-13 13:43:48 by Linus Torvalds

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
## [srsbsns5/Thunderlord345](https://github.com/srsbsns5/Thunderlord345)@[a1ac449114...](https://github.com/srsbsns5/Thunderlord345/commit/a1ac44911465bd772dda12693dc76deef347cbd5)
#### Saturday 2022-08-13 14:14:27 by srsbsns5

phantom duplication fixed

Darkness endless despair fear no more coldness blackened no sound feel no pain captured helpless ultimate dreadful fate powerless lifeless no breath falling down far outcry
they hear you, fear no more
numb feeling whole dizziness
deep scars feel no pain
no sanity
body aching
control your dreadful fate
invisible real enemy
ruin your mind falling deep down

---
## [harryob/Foundation-19](https://github.com/harryob/Foundation-19)@[e4613632cc...](https://github.com/harryob/Foundation-19/commit/e4613632cc5b9ab4363d8c768752d74623e9112b)
#### Saturday 2022-08-13 14:33:32 by Grey

Remove ERT Code that makes it so you can't call the shuttle for 30 minutes (#639)

* gets rid of old dumb code

* Revert "gets rid of old dumb code"

This reverts commit a816ca0c26964781b8a0bdf2d1af4858bc76964d.

* simpler implementation (i was strongarmed)

* removes the datum

* fuck your predicates they're not used anywhere

* Revert "fuck your predicates they're not used anywhere"

This reverts commit eefa96c718892a74936efff85b96edbef4382c0a.

* Revert "Revert "fuck your predicates they're not used anywhere""

This reverts commit 6ad00652eda432e76c4cf1a6edf0ff0ee4bcafa8.

* THIS TIME WE ACTUALLY REMOVE THE DME RIGHT

---
## [hxcjosht/Google_foobar](https://github.com/hxcjosht/Google_foobar)@[e2d2f40e0f...](https://github.com/hxcjosht/Google_foobar/commit/e2d2f40e0fcfbe762fa6ffc3bb41a8461cdb55d4)
#### Saturday 2022-08-13 15:28:43 by Technically Creative

Level 1 Problem

 Love Lance & Janice
=====================

You've caught two of your fellow minions passing coded notes back and forth -- while they're on duty, no less! Worse, you're pretty sure it's not job-related -- they're both huge fans of the space soap opera ""Lance & Janice"". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting time passing non-job-related notes, it'll put you that much closer to a promotion. 

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word ""vmxibkgrlm"", when decoded, would become ""encryption"".

Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about ""Lance & Janice"" instead of doing their jobs.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
Output:
    did you see last night's episode?

Input:
solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
Output:
    Yeah! I can't believe Lance lost his job at the colony!!

-- Java cases --
Input:
Solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
Output:
    Yeah! I can't believe Lance lost his job at the colony!!

Input:
Solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
Output:
    did you see last night's episode?

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5e728f6a2b...](https://github.com/mrakgr/The-Spiral-Language/commit/5e728f6a2b9770da484a6a2f8cae9034a380f56e)
#### Saturday 2022-08-13 15:30:46 by Marko Grdinić

"2:15pm. Done with breakfast. Let me chill for a while longer and then I will start properly. The next part won't be too long.

2:40pm. Let me start. It is time to put in a bunch of time doing the other half of the scene.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

Whereas during the menu segment I had been a disembodied presence hovering thousands of feet above the cityscape, once the game started I found myself standing upright in an actual body. I gawked like a tourist, taking in the sights. I was in a golden city. The buildings and the streets were all painted in various hues of yellow, mostly on the lighter side, and there was slight gloss on the material giving it a sense of agelessness. Usually, as time wore down the material, it would begin to lose its luster, but everything around me seemed to be brand new and sparkling. Right now I was located near the edge of one of the floating cities, and as my gaze traveled towards its center, the buildings became taller and larger, from regular suburban houses close to where I was to large apartment blocks in the distance. The very middle of the island had a grand square building on an elevated platform. It had a spherical dome that took up a lot of its volume, and as I peered at it, I noticed it seemed to be radiating golden light. Though since it was midday the effect was drowned out by the light of the sun.

In the skies I noticed there were floating golden blocks in the shape of tiles, that also seemed to be showering the city in light.

I was near the edge of the city, and it seemed to be some kind of amusement park. I could see circus tents pitched up, stands of various kinds and even a rollercoaster and various other kinds of thrill rides I did not recognize.

Taking in the sights, I breathe in the air and find it to be cool and refreshing. I checked myself over. Though I could not see my face, but based on the touch as well as the composition of the rest, it seems that my real world body has been replicated in this virtual one. Which suited me fine, but it is surprising that I haven't been offered a chance to make my avatar.

Behind me, was the railing, also made of gold. Like the blocks and the grand building, it actually had some luminance to it. Drawn to that, I try touching it and find it to be smooth and lukewarm. It is not very tall, only up to my abdomen. It is only there to prevent somebody from sliding off the edge by accident rather than stop somebody who intentionally wanted to jump off.

Looking over the railing, I can see mountains and forests as well as the sea, and as I look below, I get a spell of dizziness that I quickly fight off. I am currently very high up, enough that I can see clouds below me. Directly below there is what appears to be a major metropolis. The high rise buildings and skyscrapers are like tiny, gray splotches at this distance.

An idea to try it ceases me, and I wonder whether I should take a dive over the railing?

[Gnosis check DC 1.9 Succeeded - Sample 2.03]

I grin mischievously. Yeah, let me try it. It is not like I can experience this in real life. As soon as I think that, nervousness and excitement flood my body, and I want to keep going. I grip the railing, and place one leg and then the other over it. Hands still clutching the rail behind me, I lean forward and take a good look down. A huge drop past the clouds welcomes me, into the metropolis below. I am putting a lot of strength into my arms to keep the certain doom at bay. I can feel my heart beating against my chest.

I wonder if I will hit the streets or the roof of one of the high rises?

A thought like that intensifies both my fear and excitement. Slowly I loosen my grip on the railing and start lifting my fingers, one by one. First I move the thumbs out of the way, then I let the pinky slide. Then the ring finger. I feel like a feather, perched in such a precarious position. The railing is so close to the edge that my feet are partly over it.

Time feels like it is slowing down for me. Very slowly, as if to prolong the moment, I release the index and middle.

"No, don't do it!" I hear a woman's voice yell out, but I couldn't care less.

I feel my body leaning forward and the gravity taking hold. I drop over the railing into the vastness below.

"AAAAAAAAHHHHH!!!" As I plunge, the fear overwhelms me and a scream rips itself from my throat. Strong winds buffet me from below in my fall.

After a minute or so, I manage to get a grip on myself so I can at least enjoy the scenery instead of falling around in panic. I keep reminding myself that this is not real despite what my senses are telling me. With the sun shining all around, it is quite beautiful. I take some time to appreciate the majesty of nature. I plunge through the clouds, feeling wetness on my face and hands. Soon, what used to be tiny splotches in the distance became larger and larger. The buildings below gain definition, and involuntarily, I imagine myself splattering on the street below. The fear that I had put a lid on, bursts out, more maddened and bloodcurdling than before.

"AAAAAAAAAAAHHHHHH!!!" I scream again, even though it is fake. Even though the world is fake, my brain cares little about those facts. It is so stupid and primitive, so all it can do is beg for dear life even if there is no need to.

Ahahahaha, it is so stupid, my brain is so stupid!

As I scream and piss myself in panic, at the back of my head, I can almost feel a voice mocking me for my stupidity.

I miss the height of one of the high rises, and reflected in the glass of the window nearby, I see my reflection for the first time. Exactly as in real life, but I see traces of tears around my eyes. I hadn't realized that I had started crying at some point.

"NOOOOO!!! LOG OUT!!! LOG OUT!!! LOG OUT!!!" Completely detached from rationality, the idea to exit the game before I smash the concrete takes hold. I grip it like a liferaft in the turbulent seas.

Ahahahaha! Seen from a different perspective, it is almost like a person scrambling for his life is an entirely different person from myself.

I am going to smash face first in the middle of a busy street. As soon as the ground floor is only a couple of feet away, I muster all my reserves of will and try to stop time. This has no effect and I hit the ground, feeling the darkness overtake me.

(Euclid's Room)

"Ah!" I jolted awake into reality and involuntarily, flop like fish on dry land once. Wiping my face, I feel myself drenched in sweat. I breathe heavily and feel that in my chest, my heart is overworking itself. As soon as I realize that I am in a safe place, I begin to calm down.

I lie back on the bed for 5 minutes, until my tremors have passed.

"Hah..." I exhale, savoring the experience.

That was...

[Gnosis gain: 0.3]

...Amazing! Since I died so quickly, I didn't experience any pain, leaving only the excitement. This will definitely be a memorable experience for me. Has a regular computer game ever let me feel something like this? I do not think so. The conflict between my rational part that understood the senses are not to be trusted, and my lizard brain which went into a blind panic is what really made this what it was. If I was purely cool or purely in a panic, it would not have been that interesting.

My brain is pretty stupid right now, but at least I can have some fun with that. I'll take it a bit easier next time and just explore the town. That seems like a good plan.

I want to see what the game is about.

(Heaven's Key, Perimeter of a floating city)

I dive into the game again, and take in the sights of the city of gold. Taking only a passing glance at the railing, I turn around and go into the city proper. As fun as that experience was, I do not want to spend my entire day diving off the edge. Gawking like a tourist as I stroll around, I get a stock of the place. Near the frontier where I was, the density of buildings was low, so amongst the houses as if to spur business a lively entertainment sector was built. I could see circus tents, restaurants, stages as well as casinos. There seemed to be a lot of people enjoying themselves, though I wouldn't say it was packed. I found the city plan somewhat peculiar. There were roads for example, but no cars, and I could only see people using their own legs as far as I looked. The regular houses made sense, but other entertainment related facilities seemed to be built in the middle of roads and at intersections. Overall, it felt like the city itself was molded based on some template, and then patched up to fit a need by the people actually living here without modifying the underlying template itself.

It is a lively and cheerful place. It wasn't jam packed with people, but I could see a decent amount of them going about their business and chattering. The way they were dressed did not seem to be that much different than in the real world. Looking around, I could see old and young people, both male and female, but no kids which I'd expect would be unusual for an amusement park such as this. I think that I'd be in the youngest age cohort relative to the population here.

"Waiters wanted - 3,450/month"
"Can you make great pizza? Apply here. 3,600/month"
"Have a flair for entertainment? Comedy, magic, singing, musical instruments. 3,800/month"

While walking around I saw a bunch of job ads posted outside the relevant venues for waiters, cooks and attendants. The typical salary for these kinds of service jobs seems to be around 3,500 chips, whatever those are.

Getting bored of walking around, I pick a restaurant at random and take one of the outside seats. With the sun shining down on me, the weather is warm and pleasant, simply ideal. Given how up we are you'd expect it would be freezing, but normal rules do not seem to apply here. I pick up the menu, and take a look.

"Beer - 20"
"Iced Tea - 20"
"Pizza Margherita - 40"
"Cheese Burger - 30"
...

I want to order some of these. I've never tried eating in VR yet, so I am curious about what it tastes like.

"Hello sir, what would you like?" A waiter came around to take my order. I cringe inwardly.

"Just water." I have no choice, I do not have any money to pay for anything here.

"Got it."

While I was waiting, a person came up to my table and initiated conversation.

"Hello, do you mind if I take seat here?" She asked, smiling at me. I took a good look at the young woman in front of me. Wearing a headband with what looked to be 4 brown roses, she seemed to be of asiatic descent. Her face was cute and friendly. Short dark hair. She was wearing a finely made brown blouse with long sleeves, and a miniskirt plus thigh stockings.

"Sure." An event like this would never have happened to me in real life, so I was curious where this was heading.

"Nice to meet you, I am Lily."

"Euclid."

"An exotic name. Are you new to this city?"

I think about lying for a moment, but I have no reason to. I am certainly not going to try to show off here, I am penniless anyway.

"Yeah, I just got here." I admitted.

"I am sorry for your loss." She frowned, confusing me. "But look on the bright side." Her expression cheered up, spreading her arms. "Here in this afterlife, it is quite fun. You are going to like it."

At first I was confused, but as soon as she mentioned the afterlife, a thread of inspiration came to me. I remember the description and guess at what she meant. I've been thinking about this as just another place, but maybe the people here all died on Earth before being transported into the city. My character does not have a background so it slipped my mind.

"Yeah, it does seem like a lively place." I agree. "Maybe I'll be here for a while."

This gets a smile out of her. At that point the waiter came to our table, placed the glass of water that I ordered on my side and turned to take any further orders.

"Coffee please."

"Yes. Anything else sir, lady?"

"No, that will be all." I take the glass and take a sip of water. It is nice and refreshing. He leaves. I raise an eyebrow to Lily. "I would have liked some iced tea, but pft." I pucker my lips for emphasis. "No money."

"Ahahaha!" She waves it away. "If you've just got here, then you should have a 100 chips. Try bringing them out."

"Huh? How?" I start checking my pockets stupidly.

"Just focus." As I look at her, several stacks of translucent chips manifest in the air behind her. The thousands of chips in her pile look like they are intended for poker. Standing on nothing but air, I could see through them due to their translucency. "Then once they are staged, you can withdraw by wishing for it. For example, here I'll wish to get 20."

She raises her hand above the table, and like a magic trick, I see 20 chips moving into place. She lifts her hand and I see that the pile is no longer translucent. She lifts one, shows it to me and places it down with a clack.

"So it is like that? How do I do that?"

"Just try it."

Having an example of what I should do, I focus inwardly and I discover a sense that wasn't there before. Right in my mind I could see a stack of 100 chips. It feels different from just imagining it, like they are actually there.

"Yeah, good. I can see them behind you." She encouraged me.

Imitating her, I tried lifting my hand on the table and drawing them out from inside my sense. To my surprise it works and I can see the chips sliding into place. Lifting my hand, I count them. Feeling them out they are cold and slender to the touch.

"This is interesting. I guess I can order that iced tea. How do I bring them back?"

Lily did a little wave and the chips on her own side vanished. "As long as they are in your possession, even if they are away from you, you'll be able to recall them from anywhere. It is impossible to throw them away, you have to transfer ownership instead."

I wasn't sure how to do it, but I gave it a try and it worked. It seems that in VR, things just work.

"Bravo." Congratulating me, she opened a pack of sugar and added it to her coffee. With a spoon she started stirring it inside the liquid.

[Externus check DC 3.5 Failed - Sample 2.28]

I consider not ordering iced tea like I said I would, but that would be an asshole move. I can't see any reason to be stingy here. A part of me expected the chips to be important, but then I think about the job ads, the people going around me, Lily's own large stack and her placing her own order without issue. Nobody else as far as I can see has issue spending money. I guess 100 chips is not that much. I really meant to gamble with them rather than spend them like this, but I can always reload.

That would lose the connection with Lily though. Rather than working at a job, maybe I could get a loan and gamble with it? Since I can save and reload, I am in no danger of ever going bust unlike the NPCs.

I mean, I am not going to seriously do waitering for an entire month just to get the money to gambol. I want to get better at cards and learn some skills that would benefit me in real life.

So far, the NPCs here feel very lifelike, not at all like in a computer game made by humans. I take a look at Lily who is taking a sip of her coffee, with the pinky out. Cute, she is very cute. I can't believe that I, of all people, am getting charmed.

(Date with Lily)

I spent some time with her in that restaurant just chatting.

"I am working as a guide. If you want I'll show you around the city and get you accomodated. It would not be good if night falls and you have nowhere to sleep."

"Yeah, it would be bad if I had to sleep on the street once night falls."

“Yes, it would. Could you show me a cheap place to rent somewhere, first? After that I’d like to see what this town has to offer.”

“Of course.” She replied enthusiastically.

With that, the date started.

...

I spent some time touring the city with Lily. Lily is pretty cute, so I was a bit smitten by her, but I got tired of that after an hour. After that boredom started to kick in for me. Seriously, who cares about NPC women? She is cute, but I should be able to generate people like her by the million with a push of a button. I am not going to get sucked into the pace of things and let her become a part of my motivation for logging into Heaven's Key. How pathetic would that be?

With that mindset in place, instead of chatting about whatever comes to mind, I steer the conversation towards the city in general. Who are the big shots? What is life like? What are the challenges?

Goals like that are the only things preventing me from getting bored out of my skull. Back in school, there were times I went on an excursion with the rest of the class. Somehow those experiences ended up even more boring than going to class itself, if that is possible.

'Wow, look at the golden buildings! So cool!' I picture some wojaks pointing at the stuff in the background.

I got tired of it after 15 minutes.

Right now, I am acting like I think a normal person should act, but it is really straining my nerves. It is somewhat disgusting.

...

"WAAAAAAAAAAAHHHH!!!" Roller coaster rides rock! Seated in my coaster, being hurled through the air at high velocity! Based!

I was screaming, Lily was screaming next to me, the rest of the people in the wild ride were screaming!

This is more to my liking!

...

A whiff of barbecue drew me and I got a skewer for both me and Lily.

"Here you go!" A kindly man smiled at me, handing me my meat on a stick. I grab a bite and feel the spicy, juicy taste of meat spread through my mouth. The taste is just like in real life. Delicious!

I think I am starting to get a hang of how dating should work. Things are boring when you just let the other person take the lead. It became fun once I started drilling Lily for info on the town and dragged her into the roller coaster rides. It has been a few hours, both in the game and real life. I want to start getting to the point.

Me and Lily both finish our food, drink some colas, and then I get to the point.

"Lily, I was wondering." I manifest a poker chip between my index and middle finger waving it in front of me for emphasis. "These chips all look like they are made for gambling. So I am guessing they should have something with that."

I was expecting to hear something on the subject of card gambling from Lily, but for some reason nothing came up. I didn't care enough to push it back then, but now it is time to get to the point. I already know the theme of the game has something to do with gambling, so it is strange that I haven't heard anything about it from Lily.

"Who knows. The god who brought us all to this city made it like that. Nobody knows what goes through his mind." She shrugged.

Evading again, are you? Just what is the point of that? Do you really not know?

"Instead of just walking around town, why don't we go to a casino? I'd like to try playing some cards. You too Lily. Isn't it boring just going around town? I want more action like those roller coasters."

"Well..." She fell in thought. "Okay, I know a place, let's go there" She beamed, showing her expertise at maintaining positive energy. If I let her take the lead, she will just bore me to death, but I am sure that as a guide she is obligated to fulfill my wishes.

(Raven's Eye Casino)

She led us a few dozen blocks away, deeper into the city.

"We are here." She announced. Her positive energy from before seemed subdued, and I sensed she was somewhat on the edge.

"Great. Let us have some fun. I do not remember anything from my past life, but I must have been a card shark." I announce, striding into the place ahead of her in search of stimulus. I spot the receptionist, slam 20 chips on the counter and say to the startled receptionist. "I want to play Texas Holdem. Lead me to the table."

"Come this way, sir."

$$$

3:40pm.

> Come this way, sir.

Right now I am at this point and I need to think what comes next. I wasn't going to make Euclid a savescummer, but if this was a game this is where I'd make a save point.

3:50pm. Right now the page count is at 10 pages and 4.5k words. Not bad.

Let me step away from the screen, I need to think about the next scene. I haven't really through of the implications of saveloading. The way I imagine Euclid, he gets rid of his scrawny real world body in VR and replaces it with a chad one after he gets serious.

But if I have him rely on save mechanics, the flow changes.

I need to think about the general mentality going into this.

4:05pm. I've done a bit for the day so I have nothing to be ashamed of if I stop here. Let me step away from the screen for a few hours. I won't close just yet, but I need to think about it in order to resolve the perplexity.

4:10pm. Let me step away.

5:25pm. Nothing is coming to me. I guess I'll have to leave whatever brainstorming there is for tomorrow.

Today's session was not too bad. Focusing on writing from 9 to 6 is not something I should be aspiring to anyway. It is fine to do it a bit at a time. I certainly makes sense to stop earlier for the day than to have it eat into my game time.

Tomorrow I am going to see if I can deal with chapter 4. After that I'll think about publishing this stuff as well as including the few illustrations that I've done. Right now, let me just focus on writing. Months down the line Stable Diffusion will be released and I'll make use of such technology to add better visuals to the scenes."

---
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[894a5af955...](https://github.com/LumberKing/Tianxia/commit/894a5af955b6808cd7895e72ae70eabb9dfd8f95)
#### Saturday 2022-08-13 16:01:58 by Silversweeper

Balance/optimization/polishing (part 15 of ???)

General:
- Only feudal (is_feudal = yes) characters need apply to be Permanent Regents, Grand Chancellors, or Shoguns.

Bloodlines:
- Added a new bloodline for the "nuclear option" betrayer, if they become the GC.
- Added a bloodline for Munmu of Silla, similar to that available for Taejo of Goryeo.
- Both Taejo and Munmu's bloodline can now spawn special Chinese commanders with JD.
- Added many, many new Chinese Imperial bloodline names, primarily inspired by historical Chinese dynasties and historical Chinese states. Full integration into assorted mechanics TODO.

CBs:
- Winning a Chinese Subjugation war as the attacker against a king+ ruler will now award a super cool nickname if you are young enough.
- Assorted potentially relevant CBs that could grant the "the Conqueror" nickname can now grant the "the Little Conqueror" nickname if the conqueror is young enough.
- Papuan county invaders will no longer get the "the Conqueror" nickname, seeing as it's not all that impressive to conquer a county.

Landed titles:
- Baekje is now known as "Kudara" if held by a Yamato/Japanese/Wako ruler.
- Moved k_dali into e_china, to encourage both sides to take an interest in one another (and to make holding k_dali help with recreating e_china, if relevant).

Nicknames:
- Added a bunch of nicknames, mostly relevant to the Three Kingdoms. Weights/etc. TODO.

Objectives:
- The AI is now more likely to pick non-martial education focuses if a bureaucracy.
- Adjusted AI childhood focus logic for bureaucracies.
- Made the AI smarter about the Faith and Heritage focuses and Chinese/Japanese government eligibility.
- Mostly reverted Imperial Claimant faction opinion threshold changes; it's nicer with Regency/Shogunate factions!
- Only feudal (is_feudal = yes) characters can claim a Chinese Imperial title with a plot if their liege's MoH rating drops too low.
- Made the AI care less about the opinion of their liege for the Takeover Faction if the liege has a sub-Average MoH rating.
- Made AI Grand Chancellors willing to join the Takeover Faction against their liege at significantly higher opinion.
- The Tenno no longer bases any part of his Imperial Claimant faction ultimatum acceptance willingness on whether he has the "the Conqueror" nickname.
- Anyone with the "the Little Conqueror" nickname now responds to faction ultimatums similarly to those with the "the Conqueror" nickname.

Traits:
- Added a "[This.GetSonDaugtherCap] of Heaven" trait for Chinese Imperial rulers, lowering opinion of others with the trait. This should hopefully result in interesting times once fully implemented.

Decisions:
- If the Tenno or the Ryukyuan knockoff ends up as a tribal or nomadic ruler through some convoluted loophole they are no longer allowed to become merchant republics.
- Assorted PR, GC, and Shogun decisions are now only available for feudal (is_feudal = yes) characters.
- Added a scaling (based on how China is doing) realm size check for adopting Chinese Imperial.
- Unreformed Shenists now pay less to adopt Chinese Imperial (similar to reformed Shenists, Taoists, and Confucians).

Events:
- Made the palace fighting as part of the "nuclear option" event chain considerably quicker.
- Incapable (is_incapable = yes) characters should no longer kill people during or after the palace fighting.
- A number of events tied to the "nuclear option" are now narrative_events, using the special Chinese look from JD.
- In addition to a number of other consequences, if the GC/powerful vassal selflessly helping you against various troublesome elements at court ends up winning despite your opposition they will now see fit to "safeguard" all of your money indefinitely, for the good of the realm.
- Backstabbing the GC/powerful vassal and surrendering to the eunuchs/courtiers is now fatal for anyone else that made the mistake of supporting the GC/powerful vassal. You get to live, of course, assuming the whole "betrayal" thing works out.
- WIP replacement for soh_china_renaming_events.txt.

Localization:
- Added more previously missing localization.
- Fixed vanilla gender issue in event 20140 ("Make him disappear...").

---
## [SurrealDude/Funny-Collab-2](https://github.com/SurrealDude/Funny-Collab-2)@[9a713b7009...](https://github.com/SurrealDude/Funny-Collab-2/commit/9a713b70091997133392cd8594149cce74098cff)
#### Saturday 2022-08-13 16:39:49 by Surreal Dude

[Github Mental Breakdown Saga]

[Back to git :despair:]

[Back to git :despair:]

uh oh

fuck

teinmodding was a mistake teinmodding was a mistake teinmodding was a mistake teinmodding was a mistake

[Atlantis first 10 levels]

someone, please, send help

quick! before- ERROR.BAD ALLOCATION.OK?

---
## [Topzic/RSMod-NPCs](https://github.com/Topzic/RSMod-NPCs)@[dec6605d10...](https://github.com/Topzic/RSMod-NPCs/commit/dec6605d10b7430eadfd3b92d737e5398e8c2a3a)
#### Saturday 2022-08-13 17:06:26 by Topzic

Added More NPCS and Fixed Animations

Had to remove aggroMinutes and aggroTimer from all NPCS because it was preventing them from being aggressive.

Added NPCS
- Fire Giants
- Infernal Mages
- Gargoyle
- Dark Beast

Animations Fixed
- Baby Green Dragon
- Baby Blue Dragon
- Baby Black Dragon
- Ghost
- Zombies
- Iorwerth Warrior
- Iorwerth Archer
- Zygomite
- Zulrah Block Animation
- Zombie Swab
- Brine Rat
- Giant Crypt Rat
- Giant Rat
- Blessed Giant Rat
- Crypt Rat
- Dungeon Rat
- Zombie Rat
- Zombies
- Zorge
- Skorge
- Ogre
- Ogre Chieftain
- Ogre Shaman
- Ogre Warrior
- Tortoise
- Mounted terrorbird gnome
- Gnome Women
- Gnome 
- Gnome Guard
- Tribesman
- Jorge
- Jogre Champion
- Black Knight Titan
- Snake
- Desert Snake
- Bush Snake
- Giant Sea Snake
- Big Snake
- Sea Snake Hatchling
- Sea Snake Young
- Swamp Snake
- Dagannoth
- Crocodile
- Cave Bug
- Crab
- City Guard
- Obor
- Ent
- Dire Wolf
- Desert Wolf
- Big Wolf
- Ice Wolf
- Jungle Wolf
- White Wolf
- Billy Goat
- Goat
- Grizzly Bear Cub
- Grizzly Bear
- Reanimated Bear
- Bear Cub

---
## [EpocSquadron/helix](https://github.com/EpocSquadron/helix)@[973c51c3e9...](https://github.com/EpocSquadron/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Saturday 2022-08-13 19:31:40 by Michael Davis

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
## [jgalar/CanadianTracker](https://github.com/jgalar/CanadianTracker)@[3923e02921...](https://github.com/jgalar/CanadianTracker/commit/3923e02921a43fd81707a96dc91294f00fc16749)
#### Saturday 2022-08-13 19:55:59 by Simon Marchi

Add SKUs table, use newer API to fetch data

We currently don't handle multi-SKU products well, fix that.

TLDR:

 - Add database table for SKUs
 - Use newer API to be able to get more details about SKUs
 - Adjust web UI to account for that

Taking this product as an example:

https://www.canadiantire.ca/en/pdp/thule-convoy-xt-rooftop-cargo-box-0401588p.html

This product has 3 different variants, or SKUs, with three different
prices.  There is a single entry in the products_static table.  The
`sku` columns contains a list of all the three SKUs for that product:

  40-1588-0|40-1589-8|40-1590-2

In the products_dynamic table, the samples for multi-SKU products refer
to the complete product, not a specific SKU.  For the example product,
we have samples like this one:

    {
        "Banner": "CTR",
        "Product": "0401588P",
        "PrimarySKU": "0401588",
        "CheckDigit": "0",
        "SKU_Count": 3,
        "Price": 699.99,
        "PriceFrom": "Y",
        "Description": "THL ALP 12CFT CNV XT",
        "Messages": {
            "Warranty": "This product carries a 1 year exchange warranty redeemable at any Canadian Tire store."
        },
        "PartNumber": "632100",
        "IsOnline": {
            "Active": "Y",
            "Exclusive": "N",
            "Sellable": "Y",
            "SpecialBuy": "N"
        }
    }

Note "PriceFrom" is "Y".  I believe this means that the rendered product
list would say "From $699.99", meaning that $699.99 is the price of one
of the three SKUs, we don't know which one (whichever is the
cheapest).  Given that we want to track prices for each individual SKU,
samples like this one are not helpful, and will have to be discarded.

Samples that refer to a single-SKU product have a `SKU` key, so we can
be confident the price is for a specific SKU.

Changes at the database level:

  - add the `skus` table, with the following columns:
    - index: auto-incremented integer
    - code: code, in the format "0401589"
    - formatted_code: code, in the format "040-1589-8"
    - product_index: index of the product (products_static table) this
      SKU belongs to
  - remove the `skus` column of the `products_static` table.
  - add the `samples` table, which is like the existing
    `products_dynamic` table, but with a foreign reference to the `skus`
    table, instead of to the `products_static` table .
  - remove the `products_dynamic` table.

The migration does the following steps to keep as much of the existing
data as possible:

  - Populate the `skus` table based on the existing content of the `sku`
    column of the `products_static` table, whose format is shown above.
  - Go over each existing price sample (`products_dynamic` table), see
    if we can move it to the new table.  If it doesn't have a `SKU` key,
    or has 'PriceFrom: Y' (I think these two are correlated, but we
    check both just in case), we can't.  Use the `SKU` value to know
    which row in the `skus` table this sample will now refer to.
  - There are some products without SKU information in column
    `products_static.sku`.  This is probably because these products were
    not seen since we added the `sku` column.  For those, we did not
    create an entry in the `skus` table.  If some samples refer to that
    SKU, we have a problem.  In that case, create a `skus` row based on
    that SKU number.  Assume that the product code is the SKU code plus
    'P', which always seems to be the case for single-SKU products.
    There are some rare cases where there is no such product, in that
    case we drop the sample.

Adjust the scraping code to provide this new information.  To do so, use
newer APIs, which are those I see the Canadian Tire website use at the
time of writing.  In the new API used for fetching list of products, the
information about SKUs is better structured than in the previous one.

We previously limited ourselves to scraping the categories of level 1
and 2.  During my testing, I saw that scraping each level of category
gave a different number of items, and there always seemed to be items
that appeared only in one level and not the others.  To have the best
coverage, we would have to scrape all category levels.  But doing so
would increase the workload quite a bit, if done each day.  The tradeoff
I made to have good coverage but not a huge workload is to use one
category level each day.  The category level is based on the number of
the current day, so if the scraping is done every day (which is the case
in our production system), we'll do all category levels in a round robin
fashion.  This step is to discover new products/skus, so it's fine if we
don't discover a new one immediately.  This is only the default though,
the category levels to scrape can be specified on the command-line.

I removed the step where we fetch the number of items in each category
to provide a length to ProductLedger.  When scraping the level 5 (the
most specific categories), this is just too long, since there are
hundreds of categories.  As a consequence, we no longer show a progress
bar with a known length when scraping the inventory.  We could maybe add
it back later, and make it optional.

Adjust the web UI to add a "SKU" page.  So, the user lands on the index,
which is the list of products.  The user clicks on a product, they land
on the list of SKUs for that product.  They then click on the SKU they
want.  The experience sucks, it will have to be improved, but it works.
The existing product.html page becomes sku.html, with minor obvious
changes (but git won't tell you that).

Adjust the ctquery command accordingly.

---
## [Minagoroshi/VRChatTool](https://github.com/Minagoroshi/VRChatTool)@[ad6539d6ba...](https://github.com/Minagoroshi/VRChatTool/commit/ad6539d6ba772a2af42c2ad7b69684431e0c9226)
#### Saturday 2022-08-13 21:11:51 by top

Update main.go

forgive english, i am Russia. i come to study clothing and fashion at American university. i am here little time and i am very hard stress. i am gay also and this very difficult for me, i am very religion person. i never act to be gay with other men before. but after i am in america 6 weeks i am my friend together he is gay also. He was show me American fashion and then we are kiss. We sex together. I never before now am tell my mother about gay because i am very shame. As i fock this American boy it is very good to me but also i am feel so guilty. I feel extreme guilty as I begin orgasm. I feel so guilty that I pick up my telephone and call Mother in Russia. I awaken her. It too late for stopping so I am cumming sex. I am very upset and guilty and crying, so I yell her, "I AM CUM FROM SEX" (in Russia). She say what? I say "I AM CUM FROM SEX" and she say you boy, do not marry American girl, and I say "NO I AM CUM FROM SEX WITH MAN, I AM IN ASS, I CUM IN ASS" and my mother very angry me. She not get scared though. I hang up phone and am very embarrass. My friend also he is very embarrass. I am guilt and feel very stupid. I wonder, why do I gay with man? But I continue because when it spurt it feel very good in American ass.

---
## [Stutternov/sojourn-station](https://github.com/Stutternov/sojourn-station)@[c3c08d0946...](https://github.com/Stutternov/sojourn-station/commit/c3c08d0946fd0ebde1dd9b5cc5ab8781a544487c)
#### Saturday 2022-08-13 21:58:41 by nikothedude

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

