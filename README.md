## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-30](docs/good-messages/2022/2022-07-30.md)


1,462,573 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,462,573 were push events containing 2,018,219 commit messages that amount to 121,228,003 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [tuxedocomputers/linux](https://github.com/tuxedocomputers/linux)@[99ce4b0505...](https://github.com/tuxedocomputers/linux/commit/99ce4b05058fb42a64a58edb033e5d3a417e1ffc)
#### Saturday 2022-07-30 01:12:33 by Peter Zijlstra

objtool: Fix symbol creation

commit ead165fa1042247b033afad7be4be9b815d04ade upstream.

Nathan reported objtool failing with the following messages:

  warning: objtool: no non-local symbols !?
  warning: objtool: gelf_update_symshndx: invalid section index

The problem is due to commit 4abff6d48dbc ("objtool: Fix code relocs
vs weak symbols") failing to consider the case where an object would
have no non-local symbols.

The problem that commit tries to address is adding a STB_LOCAL symbol
to the symbol table in light of the ELF spec's requirement that:

  In each symbol table, all symbols with STB_LOCAL binding preced the
  weak and global symbols.  As ``Sections'' above describes, a symbol
  table section's sh_info section header member holds the symbol table
  index for the first non-local symbol.

The approach taken is to find this first non-local symbol, move that
to the end and then re-use the freed spot to insert a new local symbol
and increment sh_info.

Except it never considered the case of object files without global
symbols and got a whole bunch of details wrong -- so many in fact that
it is a wonder it ever worked :/

Specifically:

 - It failed to re-hash the symbol on the new index, so a subsequent
   find_symbol_by_index() would not find it at the new location and a
   query for the old location would now return a non-deterministic
   choice between the old and new symbol.

 - It failed to appreciate that the GElf wrappers are not a valid disk
   format (it works because GElf is basically Elf64 and we only
   support x86_64 atm.)

 - It failed to fully appreciate how horrible the libelf API really is
   and got the gelf_update_symshndx() call pretty much completely
   wrong; with the direct consequence that if inserting a second
   STB_LOCAL symbol would require moving the same STB_GLOBAL symbol
   again it would completely come unstuck.

Write a new elf_update_symbol() function that wraps all the magic
required to update or create a new symbol at a given index.

Specifically, gelf_update_sym*() require an @ndx argument that is
relative to the @data argument; this means you have to manually
iterate the section data descriptor list and update @ndx.

Fixes: 4abff6d48dbc ("objtool: Fix code relocs vs weak symbols")
Reported-by: Nathan Chancellor <nathan@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Borislav Petkov <bp@suse.de>
Acked-by: Josh Poimboeuf <jpoimboe@kernel.org>
Tested-by: Nathan Chancellor <nathan@kernel.org>
Cc: <stable@vger.kernel.org>
Link: https://lkml.kernel.org/r/YoPCTEYjoPqE4ZxB@hirez.programming.kicks-ass.net
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
CVE-2022-29900
CVE-2022-29901
Signed-off-by: Thadeu Lima de Souza Cascardo <cascardo@canonical.com>

---
## [HalfdeadKiller/HDK-Foundation-19](https://github.com/HalfdeadKiller/HDK-Foundation-19)@[ea904cd81f...](https://github.com/HalfdeadKiller/HDK-Foundation-19/commit/ea904cd81f16d6feb161b0dbd24eca7524df15ab)
#### Saturday 2022-07-30 03:09:38 by Calyxman

Makes Crisis robot actually worth using. (#576)

* Adds adrenaline to paramedic borg hypospray

Kinda weird how the robot whos meant to be doing paramedic shit doesnt have shit to restart the heart or apply allergic reaction first aid???
Adds /datum/reagent/medicine/adrenaline to the crisis borghypo.

* Adds ATK, ABK to Crisis Cyborg

Adds the advanced trauma and burn kits to the Crisis cyborg. This makes it a direct tradeoff between Crisis and Emergency Response flying. ER has more mobility, but worse gear for medical treatment, while the Crisis cyborg has less mobility but better gear.

* Adds tylenol and dexalin to crisis borg

Why tf does the surgical borg, specializing in surgical procedures, have better equipment for the medical doctor job than the actual medical cyborg?
Tradeoff between Emergency Response and Crisis: Crisis has lower mobility, but better gear, and Emergency Response has higher mobility but worse gear.

---
## [HalfdeadKiller/HDK-Foundation-19](https://github.com/HalfdeadKiller/HDK-Foundation-19)@[96615f6506...](https://github.com/HalfdeadKiller/HDK-Foundation-19/commit/96615f650661292a92b79eb1983064556188cb37)
#### Saturday 2022-07-30 04:07:27 by harryob

LFification, again, maybe for real this time (#568)

* what is this cursed shit

* shut up PLEASE

* everything non-LF should be LFd

Co-authored-by: tichys <tichman27@gmail.com>

---
## [weiplanet/free-programming-books](https://github.com/weiplanet/free-programming-books)@[97016edd67...](https://github.com/weiplanet/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Saturday 2022-07-30 05:23:31 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [obsproject/cef](https://github.com/obsproject/cef)@[1cc2af87cf...](https://github.com/obsproject/cef/commit/1cc2af87cf6bbdac9e1dbccb5efdfd1934c63062)
#### Saturday 2022-07-30 06:25:20 by Jim

Legendary 4638 shared texture perf improvement

This fixes remaining performance and frame pacing issues when using CEF
95 with texture sharing on Windows. I hacked Chromium internally to
treat shared textures similarly to how the 3770 method worked.

Let me document my little adventure.

First, we were getting system freezes, and from analysis of the
bluescreen dumps, they were always during synchronization, so I had a
hunch: "are keyed mutexes doing this?" The system freeze issue left me
hopeless. I already had a disdain for the stupid keyed mutexes, and due
to my immense hatred of them, I was angry and I just wanted to try
removing them, because 1.) What if they were the cause? (They were), and
2.) I hated them anyway. It was an irrational vendetta, and I was on a
war path to remove them just in the *slightest* chance that those god
forsaken keyed mutexes were the cause.

So I got angry and decided to remove them from almost everything in
Chromium just to see if it would fix the system freeze issue. I removed
their usage from almost everything in Chromium related to GLImageDXGI.

Let me go on a rant about keyed mutexes. I hate keyed mutexes. I *want*
synchronization between devices, but what I *don't* want is to be forced
to swap stupid "keys" between the two devices; especially if you're in a
situation where you cannot pass the next key value to the next device so
the next device knows what key to use, because then, the original device
can no longer lock the object anymore, and the object is completely
forfeit. Then you get suck in a situation where you're forced to wait
infinitely if you have no way of telling the other device to use the
correct key. I wish I could suggest a better design, but all I know is
that I hate it, it's an insufferable design as it is right now, and I
don't think there's a single human being on the planet who will ever
convince me otherwise. Absolutely insufferable design. I've always hated
them and always will.

Anyway, sorry about that. Like I was saying, I removed keyed mutex usage
from texture sharing inside chromium. But the problem is that with the
4638 version of shared textures, it was about 5 textures which were used
round-robin. Because we were forced to remove keyed mutexes (which were
crashing the entire system), we could no longer synchronize between
client and Chromium, thus frame pacing issues were introduced. Even
flushing wasn't helping. They weren't noticeable, and we were *almost*
just going to use it as it, but I decided I wasn't finished with my war
path.

I had fixed the system freeze issue by removing keyed mutexes, but now
there was this frame pacing issue. So, I was upset, and I tried many
different techniques to try to synchronize. Flushing, more textures,
less textures, trying to adjust timing; I thought it was hopeless, until
I started looking at the 3770 version and started looking around
4638 code for ways I could do the same thing. I had already removed
keyed mutex objects from GLImageDXGI objects, but then I realized: what
if I just add the same staging/CopyResource method 3770 did, and then
just use one shared texture? 3770 worked amazingly well, so why not try
it? Through much toil and experimentation, I got it working.

However, there was still one annoying caveat. Because of the fact that
Chromium now only deals with NT-style HANDLE objects for shared
textures, it would duplicate handles every time it was passed. There was
no way of detecting whether we were already using the same shared
texture (and CompareObjectHandles in KernelBase didn't work), so we had
to recreate the stupid texture object every time. So I introduced a new
OnAcceleratedPaint2 function specifically to specify whether the texture
has been changed -- that way we don't need to have to continually keep
recreating the god-forsaken texture object.

All these things combined has won us a huge victory, not only did we
solve the system freeze issue, but we also reduced the amount of
resources being used from the original version by removing the round
robin, eliminated frame pacing issues, and improved the perf back to
3770 levels. In fact, I'm pretty sure that perf levels are even better
than they were even with the keyed mutex version (if they weren't
causing stupid system freezes), because the keyed mutex version forced
INFINITE lock durations due to the inability to relay keys.

After 27.2 had this issue, I had to delay the release, and I spent a
week toiling over this. To get the system freeze issue fixed, and then
to get perf levels back to 3770 levels. And I did it by sifting through
millions of lines of Chromium code.

Needless to say I feel really damn good right now. This was a legendary
fix. I'm sorry, I need a little bit of ego just for once. I feel like
I've earned it.

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[b15331b4df...](https://github.com/Hatterhat/Skyrat-tg/commit/b15331b4df9bd525ba80b284beb3442f180c01be)
#### Saturday 2022-07-30 06:28:20 by OrionTheFox

[MANUAL MIRROR] The GAGening: Clothesmate edition [MDB IGNORE] (#15100)

* The GAGening: Clothesmate edition

* ThisShouldWork

* hgnbhg

* would probably help to have the right .dmi

* fixed?

* Fuck you

Co-authored-by: Twaticus <46540570+Twaticus@users.noreply.github.com>

---
## [xgqt/melpa](https://github.com/xgqt/melpa)@[570bde6b4b...](https://github.com/xgqt/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Saturday 2022-07-30 06:33:02 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [peterhauke/blog_robinwieruch_content](https://github.com/peterhauke/blog_robinwieruch_content)@[7e53db9c45...](https://github.com/peterhauke/blog_robinwieruch_content/commit/7e53db9c455baae6fb2a30e38172d142ef92b2c8)
#### Saturday 2022-07-30 06:40:22 by Peter Hauke

Improve and Correct the English language

The & should not really be used as a shortcut for 'and' -- a lot of people do this, but it is ugly and not really correct. I almost never use the & sign, unless it is part of the code.

'via' is obviously a Latin word, and generally, good written English tries to avoid the use of Latin if it is not necessary. Some English language learners will not know what 'via' means.

I would probably normally write 'from the command line', but 'on the command line' is not wrong. However, I used 'on' because you use it later.

'kinda', as well as 'gonna', 'wanna' is not correct at all. This is how many people speak, but it should really be avoided in writing. 

I added "With the 'useCustom' hook" -- I think that is correct.

I did not replace 'caveat'. Again this is Latin. I would have to change the whole phrase, so I left it as it was.

People use 'pretty' instead of 'almost', 'really', etc. But it is generally wrong. 'pretty' means that something is nice or beautiful. I avoid using it in that way.

Why write four words when one will do? I changed 'Last but not least' to 'Finally', they really mean the same.

---
## [PrinceGul786/PrinceGul786](https://github.com/PrinceGul786/PrinceGul786)@[8a541422db...](https://github.com/PrinceGul786/PrinceGul786/commit/8a541422dbb35e069e2cac19b3d675a79eb42fa9)
#### Saturday 2022-07-30 08:17:45 by Shahzado Gul

Update README.md

A passionate Software Developer ,Computer Programmer & tech evangelist fascinated by new tech-trends. Playing the part in bringing digital revolution and tech-awareness in the world.'
The perfectionist geek living in Metaverse, having a deep obsession with cyberpunk things, gaming, web3 & beautiful user interface designs.
You'll find me coding in the deep caves of Python's programming language, hunting for treasures of modern programming concepts, because I love to code and hunt bugs.
I am a patient of the Blockchain Love Syndrome caused by Centralization-o-Phobia, and my mind’s Solidity is (Rust)ed. I am a foodie! The delicious taste of Truffle and Ganache is too mouthwatering for me to resist, causing me to crave the yummy taste of Remix.
I prepare for university exams just a night before, the rest of the semester passes by reading exceptions of the node package manager, the error logs, which are longer than my whole semester’s syllabus.
If experimenting and messing around with different Operating Systems and their crucial files is like shooting one’s foot, then believe me, I hate my feet.
Computer hardware fascinates me very much, as if I have spent my whole childhood inside a transistor of a Pentium II CPU, thus very curious to know about my neighbors.
For me, the petrichor smell of Raspberry Pi & Arduino boards (even after short circuit) is far superior than that of gasoline. I wanted to become a surgeon and studied computer anatomy a lot. Till now, I have performed successful surgeries on 5 + laptops (some died in result).
I have a serious crush on DevOps concepts and am currently finding ways to understand them with the help of AWS.
Apart from that, I'm a helping hand for the learners; helping people to learn and grow. I believe in quality education & am eager to promote it. 
Thanks to my strong communication skills along with good team management courage, I want to develop in filed technology I am working on various projects to make people digital. I know how technology can develop a nation. 
If technology were a fire, I would jump right into it.
There are very rare things that fascinate me a lot, like rebirth of a star and innovations in technology.
I am the storehouse of bigger thoughts & huge optimism.
On a mission to transform billion of lives.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[81e5a6bd79...](https://github.com/treckstar/yolo-octo-hipster/commit/81e5a6bd7968458bec910086ae89a1be8f5cf09a)
#### Saturday 2022-07-30 08:22:02 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [adamhoof/MedunkaOpBarcode](https://github.com/adamhoof/MedunkaOpBarcode)@[f7bda682a6...](https://github.com/adamhoof/MedunkaOpBarcode/commit/f7bda682a6498fbce123315970293d04beab7bc5)
#### Saturday 2022-07-30 08:42:14 by adamhoof

add error handling everywhere oh my god i want to cry why is it this way man this really sucks

---
## [Liberation546/slugstation](https://github.com/Liberation546/slugstation)@[5bbc6a2401...](https://github.com/Liberation546/slugstation/commit/5bbc6a2401361e71f4c6fb0ad173900153603787)
#### Saturday 2022-07-30 08:51:55 by Marmio64

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
## [ByaCherX/git](https://github.com/ByaCherX/git)@[5cb28270a1...](https://github.com/ByaCherX/git/commit/5cb28270a1ff94a0a23e67b479bbbec3bc993518)
#### Saturday 2022-07-30 09:59:19 by Ævar Arnfjörð Bjarmason

pack-objects: lazily set up "struct rev_info", don't leak

In the preceding [1] (pack-objects: move revs out of
get_object_list(), 2022-03-22) the "repo_init_revisions()" was moved
to cmd_pack_objects() so that it unconditionally took place for all
invocations of "git pack-objects".

We'd thus start leaking memory, which is easily reproduced in
e.g. git.git by feeding e83c5163316 (Initial revision of "git", the
information manager from hell, 2005-04-07) to "git pack-objects";

    $ echo e83c5163316f89bfbde7d9ab23ca2e25604af290 | ./git pack-objects initial
    [...]
	==19130==ERROR: LeakSanitizer: detected memory leaks

	Direct leak of 7120 byte(s) in 1 object(s) allocated from:
	    #0 0x455308 in __interceptor_malloc (/home/avar/g/git/git+0x455308)
	    #1 0x75b399 in do_xmalloc /home/avar/g/git/wrapper.c:41:8
	    #2 0x75b356 in xmalloc /home/avar/g/git/wrapper.c:62:9
	    #3 0x5d7609 in prep_parse_options /home/avar/g/git/diff.c:5647:2
	    #4 0x5d415a in repo_diff_setup /home/avar/g/git/diff.c:4621:2
	    #5 0x6dffbb in repo_init_revisions /home/avar/g/git/revision.c:1853:2
	    #6 0x4f599d in cmd_pack_objects /home/avar/g/git/builtin/pack-objects.c:3980:2
	    #7 0x4592ca in run_builtin /home/avar/g/git/git.c:465:11
	    #8 0x457d81 in handle_builtin /home/avar/g/git/git.c:718:3
	    #9 0x458ca5 in run_argv /home/avar/g/git/git.c:785:4
	    #10 0x457b40 in cmd_main /home/avar/g/git/git.c:916:19
	    #11 0x562259 in main /home/avar/g/git/common-main.c:56:11
	    #12 0x7fce792ac7ec in __libc_start_main csu/../csu/libc-start.c:332:16
	    #13 0x4300f9 in _start (/home/avar/g/git/git+0x4300f9)

	SUMMARY: LeakSanitizer: 7120 byte(s) leaked in 1 allocation(s).
	Aborted

Narrowly fixing that commit would have been easy, just add call
repo_init_revisions() right before get_object_list(), which is
effectively what was done before that commit.

But an unstated constraint when setting it up early is that it was
needed for the subsequent [2] (pack-objects: parse --filter directly
into revs.filter, 2022-03-22), i.e. we might have a --filter
command-line option, and need to either have the "struct rev_info"
setup when we encounter that option, or later.

Let's just change the control flow so that we'll instead set up the
"struct rev_info" only when we need it. Doing so leads to a bit more
verbosity, but it's a lot clearer what we're doing and why.

An earlier version of this commit[3] went behind
opt_parse_list_objects_filter()'s back by faking up a "struct option"
before calling it. Let's avoid that and instead create a blessed API
for this pattern.

We could furthermore combine the two get_object_list() invocations
here by having repo_init_revisions() invoked on &pfd.revs, but I think
clearly separating the two makes the flow clearer. Likewise
redundantly but explicitly (i.e. redundant v.s. a "{ 0 }") "0" to
"have_revs" early in cmd_pack_objects().

While we're at it add parentheses around the arguments to the OPT_*
macros in in list-objects-filter-options.h, as we need to change those
lines anyway. It doesn't matter in this case, but is good general
practice.

1. https://lore.kernel.org/git/619b757d98465dbc4995bdc11a5282fbfcbd3daa.1647970119.git.gitgitgadget@gmail.com
2. https://lore.kernel.org/git/97de926904988b89b5663bd4c59c011a1723a8f5.1647970119.git.gitgitgadget@gmail.com
3. https://lore.kernel.org/git/patch-1.1-193534b0f07-20220325T121715Z-avarab@gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [fsociety-tribute/barbet](https://github.com/fsociety-tribute/barbet)@[70649c5fd7...](https://github.com/fsociety-tribute/barbet/commit/70649c5fd791aab2ad752dd7122583eba76bd3bd)
#### Saturday 2022-07-30 11:13:05 by Peter Zijlstra

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
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>

---
## [divinity76/hestiacp](https://github.com/divinity76/hestiacp)@[365dab5670...](https://github.com/divinity76/hestiacp/commit/365dab5670f6d1a862858be01638072eeb2ec1db)
#### Saturday 2022-07-30 11:34:04 by divinity76

Use secure RNG to generate passwords (#2726)

* use secure rng to generate passwords

quoting MDN:
>Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead

My rng is kinda shitty, i know there is some fast way to cut down higher digits to get a digit in range without introducing bias, but i also know that other people have introduced bias by trying to do that on an initially secure rng and getting it wrong (iirc it's discussed here? https://www.youtube.com/watch?v=LDPMpc-ENqY - been years since i saw the talk, but i know Lavavej discussed it in one of his presentations, i think it was that one)  , but anyway this is fast enough, and secure.

* shorter name

* randomString2 / centralize js string generation

* missed 2

---
## [greenforce-project/llvm-project](https://github.com/greenforce-project/llvm-project)@[15f3cd6bfc...](https://github.com/greenforce-project/llvm-project/commit/15f3cd6bfc670ba6106184a903eb04be059e5977)
#### Saturday 2022-07-30 12:16:57 by Matheus Izvekov

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
## [stenzek/duckstation](https://github.com/stenzek/duckstation)@[f9212363d3...](https://github.com/stenzek/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Saturday 2022-07-30 13:55:17 by IlDucci

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
## [skandog/p](https://github.com/skandog/p)@[db38897957...](https://github.com/skandog/p/commit/db3889795728f5aff64c119e96cc01115ed17d37)
#### Saturday 2022-07-30 14:58:54 by skandog

omg i love arshi so much, he helped work out wtf was causing so much issues with the emotion syled comps, i shouldnt have set the type to be module, next handles tyhat already

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[c0d1971261...](https://github.com/mrakgr/The-Spiral-Language/commit/c0d197126164ac1702ca3fba6268d2af3332a505)
#### Saturday 2022-07-30 16:27:35 by Marko Grdinić

"7:55am. The amount of pressure this is putting on me is unfathomable. Blowing a few interviews on my initial attempt is not big deal, but for me to not be able to sleep over the night due to it is just pathetic. The cool attitude I am trying in this journal is just fakery and my ego is as brittle as glass.

Let me check my mail. Nothing. I won't be able to salvage the GI thread. The poor F2F interview cannot be made up by brilliant follow up emails. Just what will I have to do in order to keep cool in the future? How do I deal with questions? That is what I should focus on.

8:40am. At any rate, I think the 150-200k range is too much for me right now. I do not have the mettle for it.

Also ML jobs are really a bad fit for me for some reason. Spiral has cursed me. If you imagine an ML job simply being about running a model using PyTorch/Tensorflow on a static dataset and not much beyond that, then ML is the easiest thing ever. But I am always desperate to connect my job search into my actual obsession. If it was something like frontend/backend work which is not even my specialty, I would find it much easier to keep cool.

What 3 words best describe you? Courage, persistence, obsession.

If I ever got asked that, that is how I would answer it.

I am not sure if I should be proud of that last one. It kept me going for a while, but is hindering me now.

8:50am. One thing I've realized is that when applying to small startups - GI is 10 people, and Neurolabs is small enough that the CTO and founder had time to interview me personally. With small companies such as these you can directly get a chance to talk to people in important positions. That could open some opportunities to make connections if I wanted to become a consultant. Maybe I could apply for short term projects.

That that takes real entrepreneurial initiative that I honestly do not have.

9:10am. One mistake that I've made which I will fix during the next round of applications is to record both myself and the screen for later reviewing. I need to see what impression I give off. Also need to get my nervousness under control. Sometimes it manifests as tremors, and I bet the other party notices even though I didn't see them react. I am going to read those interviewing, salary negotiation tips in /twg/ from start to finish. Also I will figure out how the GI recruiter did her background bluring. That was really cool and improved her impression. She lived in a fancy apartment given the vibrancy of colors in the background.

9:20am. Forget fancy plans, get through the initial interview, to the tech one. That should be my current goal. I got the resume under control and now I get a decent hit rate. Now I need to focus on the next phase.

By Croatian standard, 100-150k is plenty high, nobody is going to look down on me because I got something like 130 instead of 150. I can always get a higher paying job once I adjust to remote work.

9:25am. I am looking at the GI page and by the looks of it, they have plenty of PyTorch open source implementations.

So it is super vanilla what they are doing. I'd literally have an easier time getting into them with less ML expertise. I have the wrong mentality for work. Work is stitching together various libraries.

9:30am. I need to put in some proper planning for ML interviews. The interview two days ago was a wreck. When talking about my accomplishments, I need to keep up a normie aura instead of trying to sweep the audience on a wild ride.

9:35am. In the future I definitely won't schedule interviews very late in the day. I'll stick to European positions.

In order to do interviews properly, I need proper rest during the night and proper mindset during the day. Nervousness and lack of rest combine to give me a manic aura. Lack of proper preparation as well. I should at least be able to recall all the lines on my resume.

9:40am. At least these jobs are in reach if I could stretch out my hand longer. If it weren't for the updated resume, I'd literally be spending all my time applying to no avail. Right now I can at least get proper practcie intervewing.

I will overcome my fear and adjust properly to the lifestyle. That should be my main priority. Forget studying AWS for now.

9:50am. If necessary I am going to get the lowest paying job available to me and work it for a few months to get over my nervious tics. I need to adjust talking with humans who aren't in my close circle.

This mental disease that I have with ML and nervousness is quite serious.

Maybe there are some online chatrooms where I can have face to face conversations with randos?

It would be cheaper to just spend a while just going through this exercise than burn my interview slots on practice. It would be smoother ramp up.

10:10am. I am coming up with a plan. What if I made a post on the Reddit programming sub asking for interview partners? Maybe I could tutor some beginners and do their homework, things of that sort.

10:15am. Helping others could be helping myself in this case.

10:20am. Today I am not going to do anything as my brain is stretched to the breaking point.

Maybe I should start a Youtube channel and do some programming on it, explaining my thought process. I am ranting all day in this journal, but that is only exercising my writing. To pass the interviews I need talking skills. But to get ideas for what to do I should try reaching out to people.

10:55am. Actually of all things, maybe it is my accent and way of speaking that is getting me filtered. I said I lived in the US for a decade, but my speaking proficiency is only so-so. I have to strain my brain to get the words out. This would definitely be noticeable.

Maybe I should do some Spiral tutorial videos as exercise?

11:10am. Come to think of it, I just remembered there is a beginner programming sub. I could tutor some noobs there.

11:45am. Well, if the situation is that serious that I am considering the above, maybe I should just remove the lower limit on my asking price. Rather than wasting my time teaching noobs, even the lowliest paid job would be sufficient to acclimate myself back to the workspace.

Now that I've summarized it, the main challenge of being a pro programmer is being extroverted. This is highly ironic given the subject matter.

11:50am. My own brain is sabotaging me and steering me towards lowly paid jobs.

1:50pm. https://www.freecodecamp.org/news/how-not-to-bomb-your-offer-negotiation-c46bb9bc7dea/
https://www.freecodecamp.org/news/ten-rules-for-negotiating-a-job-offer-ee17cccbdab6

I lost Neurolab because I said the first number. As soon as 150k went out of my mouth, the CTO turned off and started looking for a cheaper candidate. Why wouldn't he?

Going into the future I need to keep in mind.

And going into the future, I need to keep in mind that absolutely nobody will pay me to make low level tools. Big companies can afford to sponsor that kind of work, but start ups just want library donks.

Which is kind of tragic that I got ghosted by the AssemlyAI HR drone. I'd be well suited for such a role. Getting what you want is really a crapshot. I need to be prepared for any arbitrary goal. My background might make me too expensive to all these startups.

> “Getting a job” implies that jobs are a resource out in the world, and you’re attempting to secure one of these resources. But that’s completely backwards. What you are actually doing is selling your labor, and a company is bidding for it.

> Eventually, they’ll give you information about the offer. Write it all down. Doesn’t matter if they’re going to send you a written version later, write everything down.

...

> The importance of positivity

> Staying positive is rule #4 of negotiation. Even if the offer sucks, it’s extremely important to remain positive and excited about the company. This is because your excitement is one of your most valuable assets in a negotiation.

> A company is making you an offer because they think you’ll do hard work for them if they pay you. If you lose your excitement for the company during the interview process, then they’ll lose confidence that you’ll actually want to work hard or stay there for a long time. Each of those makes you less attractive as an investment. Remember, you are the product! If you become less excited, then the product you’re selling actually loses value.

This is pretty harsh.

> If a candidate often uses expressions such as “whatever”, “I don’t mind”, “It doesn’t bother me” and other similar phrases, you may be dealing with someone who simply doesn’t care enough.

https://resources.workable.com/stories-and-insights/phone-screen-interview

Oh crap, I made this mistake at Kalepa when I got asked at working at a large company vs a startup. The HR drone literally asked me that question twice.

Aghhh, and at GI as well now that I think about it. She showed me a video that was glitchy. I thought it was an accident and said it does not matter, but she might have done that on purpose! Shit!

Also I wanted to end the interview early. That was negative. I need to exhude interest in the company.

> Be suspicious of candidates who can’t explain what they did in their previous job or what their studies were about.

It is not that easy to lie on your resume.

> It isn’t a good sign if a candidate has nothing to ask you.

I also made this mistake at GI. I only asked them about how they intend to pursue general intelligence.

In hindsight, I was destined to bomb GI.

Even that thing where she talked about her own background was to get me to let my guard down.

What brilliant follow up emails? In her eyes I was worse than I even thought. I was wrong. I thought that the intro interview was just a meaningless formality, but it turns out it is quite an important filter that I need to get through.

I do not know where it was, but I remember saying I have a lot of money saved up in one interview. Big mistake.

No wonder I bombed all of them.

It looks very suspicious that some guy from Croatia worked at MS, Google and Tesla.

It might have get me initial hits, but I'll have a hard time getting through the intro interviews, it is more than just nervousness. I will simply never be an ideal candidate. I can only push forward to the technical interviews.

https://generallyintelligent.ai/blog/2022-01-20-our-hiring-process/

A lot of programming interviews. This is the ideal case. Kalepa had a ton of behavioral ones.

Instead of trying to do it this route, maybe I should start grinding leetcode? No. I need to test the process thoroughly.

2:35pm. My god, what a pain in the ass. Maybe I should get back to being an artist.

https://www.freecodecamp.org/news/how-not-to-bomb-your-offer-negotiation-c46bb9bc7dea/

I am looking at all these mind games, and thinking how can I do this if I am already so nervous?

2:50pm. No, there is a way to go through. I mean, if they thought that I was 100% fake, there would be no need to arange a meeting. Even with such a suspicious resume as mine, I got a 50% hit rate. I'll have to do careful preparation and planning so I can go to the technical side of things

3pm. Let me go to bed here. I am just so tired, from last night and I am going like the walking dead.

5:40pm. I give up. This intro hurdle would be something a weaker programmer than me could easily cross, but I just do not have the determination to fake eagerness. I just don't feel any of the work is meaningful. I want the money, but I've been conflicted at an inner level from the start.

The GI recruiter pretty much destroyed me with her finely executed glitchy video trick. She'd say 'The video is glitchy.' and I would respond 'It does not matter.' I remember this happening twice. I didn't think the companies would care that much about having programmers that really want to work, but it makes sense.

To produce programs, two things are needed: will and skill. Of the two, I'd actually put will above skill. With skill, but no will the employee would just sit on his ass, but with will, but weak skill, the work would still get done.

This introductory call is not at all useless, and it is pretty much there to weed out people with insufficient determination. I honestly thought HR drones were retards at first, but what just happened chills me to the bone. I am just really unlucky to have my nature.

5:45pm. What I want to do right now is start writing Heaven's Key. I can do anything in life, so I might as well create the story that I want. Since I have my accounts set up, I'll open a Patreon.

I really hope this is not the start of me ending up dying of hunger on the street in a decade or so.

5:50pm. I'll forget about art and music and simply get it out. I want to write so I might as well do that.

Maybe it won't be too horrible and I'll make enough donations to at least hit the 100$ a month target. Yeah, right. I just can't imagine Heaven's Key being in any way popular. But I am going to do it. After it and Hatred, maybe I'll even do Heart's Desire.

5:55pm. At this point I have no idea how the Singularity will play out in the real world. Given how GPUs went, Google will write some library to run ML models on them. And then what? Will every person in the world just get his own super AI?

I really hate this timeline. There is no magic in it. I just can't think of any way to be my own boss with my programming skills.

Ok, first of all, let me join the DALLE list.

https://openai.com/dall-e-2/

I'll pay 0.1$ an image if needed. It could be worth it. I have a bunch of dollars in my account now. It should add a bit of omph to the VN.

I am not sure how long it will take until I get an invite, but I'll be writing for the next few months at least. I'll go back and illustrate parts of it retroactively. I'll do the bad end scene with the skeleton myself before that. But I do not feel like sculpting the skelly, I'll get a model of it off the net somewhere.

I'll make heavy use of style transfer and photographs, if I did my own modeling I will never get anywhere. I'll also do some drawing. I'll get over myself and doodle something on the CSP base mesh for the characters. As for music...who knows. I have the tunes in my head, but who knows where I will find the will to cultivate it.

An easy life is the best. I'll write during the day, and play games after 6pm.

6:15pm. It is ridiculous. An ordinary person, if he had the skills and the chance to make over a yearly salary in a single month would definitely do all he could to grasp the opportunity. But I myself am arrogant and demonic. I can't see these opportunities as anything other than dirt.

I'd be willing to do these shitty jobs as the money is good, but trying to get me to pretend to be eager to do it is just too much. The HR drones win this round, and maybe the war.

6:20pm. Let me close here. I really hope I'll get some proper sleep tonight otherwise my brain will explode. So far it has been 3 consecutive days of restless nights. I'll try playing Pathfinder Kingmaker in order to exhaust it. Let me start by watching Overlord ep 4."

---
## [fermion87/SWLOR_Haks](https://github.com/fermion87/SWLOR_Haks)@[6ffa92d6cc...](https://github.com/fermion87/SWLOR_Haks/commit/6ffa92d6cc5883cce0bc077245f3f7d5a9f1a75f)
#### Saturday 2022-07-30 16:39:36 by Scott Finlay

Patch for Head Pack 4 (#146)

- Re-added overwritten head 54, now as Head 100. Over-wrote ugly old NWN head that nobody used because I didn't want to fuck with IDs

- Adjusted scaling on Male Hum/Mir/Chi/Ech 50 & 51

---
## [juniorvigneault/speculative.play](https://github.com/juniorvigneault/speculative.play)@[26288e6865...](https://github.com/juniorvigneault/speculative.play/commit/26288e6865cc5d63a73d0877eae840cdcab97970)
#### Saturday 2022-07-30 16:58:22 by miamiv1ce

THE END

Hello, so this is the end of my project. It's nowhere near finished, but I can't work on this anymore.

I don't think working on something has made me this depressed and unhappy and anxious as working on this project, ever. I worked about 80 hours on it, 20 more than i was supposed to, and it's still very underdevelopped. I think there is something really nice and interesting about putting videos and accessing them through an elaborate menu, but nothing speaks to me anymore in terms of content/concept, nothing makes me laugh and I feel lost and I feel like I want to destroy everything about my concept and start again, only with the technical aspects (videos, dialogs, menus...) and build an entirely new project. I want to do that but It would probably take me about 60 hours again, and I don't have time anymore.

I'll try to do something with this later on, something more meanignful and interesting. Something actually playable. Not to sound dramatic but now i need this thing to be as far away from me and my mind as possible. Seriously I cannot take it anymore.

The thing is I didn't really have FUN working on this thing. Probably cause it was not funny to me in the end. When I have fun working on stuff I want to work on it all the time. I wish it went that way. UHH. Sorry to be so dramatic but it's been a really intense and weird last month thinking about this thing, dreading it. Dreading working on it, dreading starting over. Just dread.

In the end I was going for a sort of app where you can buy memories and own them as if they were yours. A marketplace for memories. Ads for memories. I really like the concept and everything. I think it could be a nice game. But I feel like it would take me another 3-4 months working on this to make it actually good.

I have to concentrate on other things.

---
## [GremlingSS/funset-pastryland](https://github.com/GremlingSS/funset-pastryland)@[eab43e488d...](https://github.com/GremlingSS/funset-pastryland/commit/eab43e488d564b0f079d7b0694afac1adb05c907)
#### Saturday 2022-07-30 17:03:56 by Marrone

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
## [newstools/2022-national-daily-nigeria](https://github.com/newstools/2022-national-daily-nigeria)@[4b72cae877...](https://github.com/newstools/2022-national-daily-nigeria/commit/4b72cae8771309d9a3f9ff4fd069584f7635bf6d)
#### Saturday 2022-07-30 17:23:50 by Billy Einkamerer

Created Text For URL [nationaldailyng.com/ghanaian-big-girl-arrested-for-stabbing-her-canadian-boyfriend-to-death/]

---
## [sottenad/jService](https://github.com/sottenad/jService)@[27f72f2ef5...](https://github.com/sottenad/jService/commit/27f72f2ef55cca17175db54a77cb56cd2048dbbd)
#### Saturday 2022-07-30 17:51:38 by Krikor Ailanjian

Added game

My team at work used to play jeopardy on the Google assistant app after stand up every day. the app was horrible and kept crashing so used your API to build a better version in browser, here it is. Thank you so much for working on this it's really great, when it went down for a few days we had to go back to the app and it was a real pain so really thankful you have this up!!

---
## [amantu-qbit/qb-vehiclekeys-1](https://github.com/amantu-qbit/qb-vehiclekeys-1)@[757fdd0859...](https://github.com/amantu-qbit/qb-vehiclekeys-1/commit/757fdd0859013e45f9d432fa894f0ecb03d8bbf5)
#### Saturday 2022-07-30 17:58:18 by ItsANoBrainer

Proper Refactor

Refactored the entire resource because the key system was not working.

No longer does a server callback 10 or so times a second, on top of other bad practices.

Tested pretty much everything with my devs, but there might be some weird issues we havnt found. Please lookover as I've been going crazy with the small tedious issues I've come across doing this.

Throwing this up to get feedback, and for people to use who want it.

Features:

- Keys are saved server side, and sent to each client when they are added or removed, as well as on character selection. This allows characters to leave and come back in the same server uptime session and still have the same keys
- Keys are only pulled from the server once on character load
- Giving keys has 3 types, /givekeys with an id will attempt to give keys you have to an id, not including an id will try to give it to the closest person, and if you're in a vehicle it will give to everyone
- Can only give keys to vehicles you have keys to
- Server event to force acquire keys to a plate for a person (for lockpicking/stealing/spawning, etc.)
- Can Carjack an NPC with a gun, has different percentages to work based on weapon (config)
- Take keys from dead npc drivers
- Can lockpick a car to unlock the doors
- Can hotwire a car if you're in the driver seat of the vehicle you dont have keys to to get keys
- Keeps the engine of a vehicle off if you dont have keys to it (allows other resources to attempt to toggle car engine without needing to interface if you have keys or not)
- Vehicle blacklist system for vehicles you dont want to be lockable (always unlocked)
- Police Alerts from lockpicking/hotwiring/carjacking
- Export to check if you have keys to a vehicle
- Locking/unlocking with hotkey
- Locking/unlocking and giving keys uses a custom GetVehicleInDirection you are facing for realism/accuracy
- Fully compatible with old resource. Has an event handler for 'vehiclekeys:client:SetOwner' in which it gives keys for that plate
- Some other shit I probably forgot

TODO:
- Add LOCALE support
- Stop peds from wanting to get back into the vehicle they just got carjacked out of as they're fleeing

---
## [sha5b/telesis.website.starter](https://github.com/sha5b/telesis.website.starter)@[1782520b6f...](https://github.com/sha5b/telesis.website.starter/commit/1782520b6fa843ffc8666f8cab0459ff303e9f97)
#### Saturday 2022-07-30 18:55:33 by sha5b

Added MDX Database

yeah i know what a stupid idea but i dont want to install antoher stupid paackge for some stupid shitz

---
## [rlawoehd187/android_kernel_pantech_msm8974](https://github.com/rlawoehd187/android_kernel_pantech_msm8974)@[db4a8bafc6...](https://github.com/rlawoehd187/android_kernel_pantech_msm8974/commit/db4a8bafc6e00ca9b18cb85ced63bf6afaa4e33a)
#### Saturday 2022-07-30 19:21:36 by Masahiro Yamada

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
[haggertk: Backport to 3.4. Omit cpu, hdaudio, ipack, mei, mipscdmm,
 rapidio, ulpi]
Signed-off-by: Kevin F. Haggerty <haggertk@lineageos.org>
Change-Id: Ic632eaa7777338109f80c76535e67917f5b9761c

---
## [OptiCloud-AB/spark](https://github.com/OptiCloud-AB/spark)@[c4c623a3a8...](https://github.com/OptiCloud-AB/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Saturday 2022-07-30 20:34:47 by Hyukjin Kwon

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
## [justinpryzby/postgres](https://github.com/justinpryzby/postgres)@[9c30a7fc2f...](https://github.com/justinpryzby/postgres/commit/9c30a7fc2fe095fce8a6f283bf81a97e197a4794)
#### Saturday 2022-07-30 21:29:25 by Tomas Vondra

Showing applied extended statistics in explain

Hi,

With extended statistics it may not be immediately obvious if they were
applied and to which clauses. If you have multiple extended statistics,
we may also apply them in different order, etc. And with expressions,
there's also the question of matching expressions to the statistics.

So it seems useful to include this into in the explain plan - show which
statistics were applied, in which order. Attached is an early PoC patch
doing that in VERBOSE mode. I'll add it to the next CF.

A simple example demonstrating the idea:

======================================================================

  create table t (a int, b int);
  insert into t select mod(i,10), mod(i,10)
    from generate_series(1,100000) s(i);

  create statistics s on a, b from t;
  analyze t;

test=# explain (verbose) select * from t where a = 1 and b = 1;
                          QUERY PLAN
---------------------------------------------------------------
 Seq Scan on public.t  (cost=0.00..1943.00 rows=10040 width=8)
   Output: a, b
   Filter: ((t.a = 1) AND (t.b = 1))
   Statistics: public.s  Clauses: ((a = 1) AND (b = 1))
(4 rows)

test=# explain (verbose) select 1 from t group by a, b;
                              QUERY PLAN
----------------------------------------------------------------------
 HashAggregate  (cost=1943.00..1943.10 rows=10 width=12)
   Output: 1, a, b
   Group Key: t.a, t.b
   ->  Seq Scan on public.t  (cost=0.00..1443.00 rows=100000 width=8)
         Output: a, b
         Statistics: public.s  Clauses: (a AND b)
(6 rows)

======================================================================

The current implementation is a bit ugly PoC, with a couple annoying
issues that need to be solved:

1) The information is stashed in multiple lists added to a Plan. Maybe
there's a better place, and maybe we need to invent a better way to
track the info (a new node stashed in a single List).

2) The deparsing is modeled (i.e. copied) from how we deal with index
quals, but it's having issues with nested OR clauses, because there are
nested RestrictInfo nodes and the deparsing does not expect that.

3) It does not work for functional dependencies, because we effectively
"merge" all functional dependencies and apply the entries. Not sure how
to display this, but I think it should show the individual dependencies
actually applied.

4) The info is collected always, but I guess we should do that only when
in explain mode. Not sure how expensive it is.

5) It includes just statistics name + clauses, but maybe we should
include additional info (e.g estimate for that combination of clauses).

6) The clauses in the grouping query are transformed to AND list, which
is wrong. This is easy to fix, I was lazy to do that in a PoC patch.

7) It does not show statistics for individual expressions. I suppose
examine_variable could add it to the rel somehow, and maybe we could do
that with index expressions too?

regards

--
Tomas Vondra
EnterpriseDB: http://www.enterprisedb.com
The Enterprise PostgreSQL Company

From 4629d1d9b1fc5f6c3bc93e0544b0c022345086c9 Mon Sep 17 00:00:00 2001
From: Tomas Vondra <tomas.vondra@postgresql.org>
Date: Thu, 18 Mar 2021 15:09:24 +0100
Subject: [PATCH] show stats in explain

---
## [siberfx/tutorials](https://github.com/siberfx/tutorials)@[200ebf5527...](https://github.com/siberfx/tutorials/commit/200ebf5527e603829b5122fc533e41a5a47c98cc)
#### Saturday 2022-07-30 21:42:31 by Michał Bundyra

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
## [axmyo/Cow-s-Helper](https://github.com/axmyo/Cow-s-Helper)@[eb3ce21f02...](https://github.com/axmyo/Cow-s-Helper/commit/eb3ce21f02877d3d0cfcfe518ea07be8d5bad721)
#### Saturday 2022-07-30 21:51:36 by Axmyo Dev

thank boosters in general.

fuck you steak, never edit this code again.

---
## [MuchMarts/Afirmacijas](https://github.com/MuchMarts/Afirmacijas)@[f99b09fb41...](https://github.com/MuchMarts/Afirmacijas/commit/f99b09fb41dfbed8033d429bf7e27ccc8e5de434)
#### Saturday 2022-07-30 21:55:02 by DrgnInventor

PAIN AND SUFFERING

Gods have lied potatos have grown and forks have won. This stupid thing aint working and im not sure why I dont want to rewrite it but like why you no work

---
## [bearrrrrrrr/coyote-bayou](https://github.com/bearrrrrrrr/coyote-bayou)@[27e461bd68...](https://github.com/bearrrrrrrr/coyote-bayou/commit/27e461bd68d992ca88ce3940cf43293100f904ed)
#### Saturday 2022-07-30 22:31:30 by OdysiaHallow

Shit Pit Salvation

Bug fixes to Redwater plus a new clinic and moving the gallows, and the tribe got some love. Love you Oli <3

---
## [alphaprime7/learning-c-and-c-](https://github.com/alphaprime7/learning-c-and-c-)@[e1722df7cf...](https://github.com/alphaprime7/learning-c-and-c-/commit/e1722df7cf2ece75737c4f2f2f692718c5742532)
#### Saturday 2022-07-30 22:33:34 by SwaggyT

Add files via upload

This did expose me to the basics however and might explain why on a good day when i can remember this, things seem a little easier.
Also it helped with dealing with intimidation and might explain why i enjoy Rcpp even though i suck at it.

---
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[921941520f...](https://github.com/newstools/2022-metro/commit/921941520f74787f4653bf73298fadd9705355f7)
#### Saturday 2022-07-30 23:15:25 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/07/30/i-fell-in-love-with-her-the-day-we-met-then-she-told-me-she-had-a-boyfriend-17064326/]

---

