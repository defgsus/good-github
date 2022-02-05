## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-04](docs/good-messages/2022/2022-02-04.md)


1,686,783 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,686,783 were push events containing 2,683,945 commit messages that amount to 202,072,494 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [RahulVarmaC/Data-Visualization](https://github.com/RahulVarmaC/Data-Visualization)@[97b7884c3d...](https://github.com/RahulVarmaC/Data-Visualization/commit/97b7884c3dcfa598e8125d540006fa8732fe1491)
#### Friday 2022-02-04 00:02:21 by RahulVarmaC

Add files via upload

This is my first visualization on tableau. The following tableau work book has a set of bar charts on it. The bar charts are basically representing:
1. Anime with descending order of the number of episodes.( Bleach has the maximum number of episodes with Naruto coming in second) 
( **** This might not be an entirely fair given how Naruto is broken down into Naruto and Naruto Shippuden. Also my data set does not have One Piece  )
2. Anime by Rank in ascending Order. Full metal alchemist : Brotherhood was ranked first in my anime list website. (I'm not sure why either. One Piece rules !) 
3. We can apparently make a compound bar chart with 2 labels. The bar chart consists of the aired date and the Name of the anime sorted in ascending order by the Rank.
The bar chart tells us the rank of the anime and the date it was aired.
4.The fourth bar chart is the list of anime sorted in ascending order by popularity. The first place again goes to Full metal alchemist: Brotherhood.( Again , Why?)
(*** Shockingly,  Demon slayer did not make the top 100 in popularity ......  )

In conclusion, the age of this data set can be predated to 10000 B.C ( this is a joke, the data set was apparently made in 2018.) 
Tableau is a fun tool and a very powerful one for data visualization. You don't have to write tens of lines of code, we do not need to remember the names of specific plot functions , the parameters these functions take, the limited number of colors or shapes that the function can take. We just need to drag and drop the columns and we get amazingly visually appealing charts which lucidly tell us how our data looks like.
The only thing we need to learn to do in tableau is to ask the right questions about our data to gain necessary insights.

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[39c9625fd9...](https://github.com/ammarfaizi2/linux-block/commit/39c9625fd9de1645e06e9664ef0f8e199424ca7c)
#### Friday 2022-02-04 01:01:17 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

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
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[031c0866ed...](https://github.com/shiptest-ss13/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Friday 2022-02-04 01:06:08 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [javashin/android_kernel_xiaomi_atoll](https://github.com/javashin/android_kernel_xiaomi_atoll)@[9928c0ffd0...](https://github.com/javashin/android_kernel_xiaomi_atoll/commit/9928c0ffd0a79add96a2daf71dec02ca6cb1db99)
#### Friday 2022-02-04 01:16:17 by Wang Han

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
Signed-off-by: Carlos Jimenez (JavaShin-X) <javashin1986@gmail.com>

---
## [0x256e4/Competitive_Programing-ID](https://github.com/0x256e4/Competitive_Programing-ID)@[06414d0dc6...](https://github.com/0x256e4/Competitive_Programing-ID/commit/06414d0dc6f31983d3c21ef07c6cc0984845204c)
#### Friday 2022-02-04 01:19:41 by Alwan Adiuntoro

Codewars/7_kyu_computer_science_101_stack: create README.txt

Computer Science 101 - #1 Stacks

NOTE: The major content of this Kata is contained within the
"Lesson" and "Task" headings. Furthermore, if you are already
familiar with how a stack works, you may simply skip to the "Task"
heading which contains all the instructions you need to complete
the Kata.
About this Kata Series

Learn fundamental computer science concepts that every CS student
must know in depth such as algorithms, data structures and common
data types through implementing them from first principles.
Translators' Note

Translations to this Kata in languages that either already have a
built-in stack datatype (e.g. C++, C#, Java) or another datatype
that can function as a stack (e.g. JavaScript, Python, Ruby) will
be rejected without further reason.
Lesson

Stacks are everywhere - they can be found in programs involving
symbol balancing, depth first search and backtracking just to name
a few. Hell, even recursion depends on stacks! In fact, they are
so common that any sane programming language would provide at
least one built-in datatype that can act as a stack. For example,
C++ has std::stack, Java has java.util.Stack and C# has
System.Collections.Generic.Stack. So, what are they?

A stack is a last in, first out (LIFO) data type that supports at
least these three operations:

    Push - Adds an item to the top of the stack
    Pop - Removes an item from the top of the stack. Most
    implementations return the item that was popped but those
    that don't must implement another operation "peek" that
    simply returns the top item of the stack.
    Is empty - Is the stack empty? This operation is crucial in
    ensuring that the user of the stack doesn't accidentally pop
    or peek at an empty stack (which doesn't make sense).

An analogy for understanding stacks could be a stack of documents
on your office desk. It is trivial to place a new document on top
of your existing stack and it also requires minimal effort to
view the top document and/or remove it from the stack for
processing; however, it is no easy job to try to search for a
document located somewhere in the middle of the stack and is
definitely even harder if you want to remove a document from the
middle or slip a new document there.

Now you should know what a stack is but knowing how to implement
it is something else entirely. Fortunately, it turns out that one
of the simplest data structures in existence is perfectly suited
for implementing stacks - enter the linked list. Such a simple
data structure is rarely a good choice for implementing common
data types due to its traversal restrictions which translates to
inefficiency (see this Kumite which explains how an associative
array based on linked lists is extremely inefficient) but a stack
implemented using it can achieve constant O(1) time for all of
its key operations (push, pop [, peek] and "is empty") mentioned
above and never occupies more memory than it needs. It is up to
you to figure out in this Kata how this can be achieved.

Before we end this lesson, here's something for you to think
about: if we implement our stack as a linked list, each node
stores not only an item in the stack but also a reference to the
next node which means that a significant portion of the memory
allocated to our stack goes to storing these references instead
of storing the actual items. In contrast, a stack implemented
using a dynamically sized array need only allocate memory for
storing the items in the stack (perhaps including a trivial,
constant amount of memory for storing the current size and
capacity of the stack) while retaining the benefit of achieving
constant time for all of its operations. So, in this sense, it
would appear that implementing a stack as a dynamic array is one
better than a linked list implementation since less memory is
used. Is this actually true and why?
Task

In this Kata we will be implementing our stack (of integers) as a
linked list where a node of our linked list is defined as follows:

typedef struct node {
  int data;
  struct node *next;
} Node;

Our actual stack is then defined as a wrapper type around our
linked list:

typedef struct {
  Node *root;
} Stack;

By defining our stack as a wrapper type around the linked list
instead of directly exposing the linked list to the user of the
stack, we can 1) reserve NULL for specifying an invalid reference
to a Stack instead of an empty stack and 2) modify a stack by
object reference instead of passing in the address of the
variable holding the stack.

Implement the following key operations of the stack:

    void stack_push(Stack *stack, int data) - Pushes the data
    onto the top of the stack, allocating memory to the stack if
    necessary.
    int stack_pop(Stack *stack) - Pops the top item of the stack
    and returns it. It should also ideally free memory previously
    allocated to the stack if possible to avoid memory leaks -
    the tests will test for very large stacks so you may run out
    of memory if you forget to do so.
    int stack_peek(const Stack *stack) - Returns the top item of
    the stack. This operation should not modify the stack.
    bool stack_is_empty(const Stack *stack) - Checks whether the
    stack is empty. This operation should not modify the stack.

All four of these key operations should operate in O(1) time.
There will be performance tests in the Submit tests to enforce
this.

Also take care to manage your memory properly - there aren't any
assertions to enforce this but it is generally good practice to
free memory that you no longer need and note that you may run
out of memory in the performance tests if there is a serious
memory leak.

You may assume that the peek and pop operations will never be
called on an empty stack provided that you implement all key
operations correctly. Apart from that, you should ensure that
your solution does not cause any potential form of undefined
behavior (such as dangling pointers); otherwise, there is no
guarantee that the tests won't crash.

Link: https://www.codewars.com/kata/5b24bcecd74b5be066000054

Signed-off-by: Alwan Adiuntoro <alwanadiuntoro@gmail.com>

---
## [BoHBranch/BoH-Bay](https://github.com/BoHBranch/BoH-Bay)@[b51269dde1...](https://github.com/BoHBranch/BoH-Bay/commit/b51269dde1e34405f5ca3be41d4cd3022bd3c113)
#### Friday 2022-02-04 01:19:54 by Carl?

Merge pull request #1091 from Yawet330/patch-3

fuck you bay

---
## [Kylerace/tgstation](https://github.com/Kylerace/tgstation)@[079f8ac515...](https://github.com/Kylerace/tgstation/commit/079f8ac51554bb338ac5826c9d06c8d4bc10be80)
#### Friday 2022-02-04 02:19:48 by LemonInTheDark

Adds moveloop bucketing, uses queues for the singulo rather then sleeps (#64418)

Adds a basic bucketing system to move loops.

This should hopefully save a lot of cpu time, and allow for more load while gaining better smoothness.

The idea is very similar to SStimer, but my implementation is much more simple, since I have to worry less about long delays and redundant buckets.
Insertion needs to be cheaper too, since I'm making a system that by design holds a lot of looping things

It comes with some minor tradeoffs, we can't have constant rechecking of loops if a move "fails", not that we really want that anyway
We also lose direct control over the timer var, but I think that's better, don't want people manipulating that directly
Not that it even really worked very well back when we did have it
Removes the sleep from singularity code

Rather then using sleep to store the state of our iteration, we instead queue the iteration in a list.
We then use a custom singulo processing subsystem to call our "digest" proc several times per full eat, with the hope of staying on top of
our queue
This rarely happens because the queue is too large, god why is a sm powered singulo 24x24 tiles.

I've also A: cached our dist checks, and B: Added dist checks to prevent attempting to pull things out of range
This might look a bit worse, but it saves a lot of work

Oh right and I made the singulo unable to eat while it still has tiles to digest. The hope is to prevent
overwork and list explosion.

Hopefully this will prevent singulo server stoppage, though I've seen some other worrying things in testing.

---
## [FloralKoral/scrapers](https://github.com/FloralKoral/scrapers)@[0aaab9c1f9...](https://github.com/FloralKoral/scrapers/commit/0aaab9c1f902305d7fa3d678bfdd2cca83db198f)
#### Friday 2022-02-04 02:27:39 by FloralKoral

oh god I need to split classes for this to work oh shit oh fuck

---
## [yangbao328/MCA-Chicago](https://github.com/yangbao328/MCA-Chicago)@[a404e4d060...](https://github.com/yangbao328/MCA-Chicago/commit/a404e4d0603e7713943d1cca5a4fd4a056cd8cfd)
#### Friday 2022-02-04 03:42:09 by yangbao328

Add files via upload

Overall, as threshold amount being 20 and 44 and groupby index of ‘counts’, ‘American’ and ‘male’ have two largest proportions in this analysis. Firstly, in Sankey diagram of Nationality and Gender, it is remarkable of how American male artists had contributed. The weighting value of American male artist is as heavy as 3540 whereas American female artist is only 1000. But American female artist still outweighs female of German, French, British and Japanese. Surprisingly yet unfortunately, as the counting threshold being 44, only these five countries’ female data are eligible to this criterion, meaning only five countries have five or more female artists in this dataset. In addition, more countries have 44 or more male artists based on this diagram across the world.
However, limitations in this dataset are also critical to be notified. It possibly collects artists’ information from the U.S. initially and loses sight of some other countries with less contact. Besides, artists who were born in centuries of war may also had less chances to be recorded in history. I am curious to learn further about how better we can do to maintain such data and information and deliver it to next generations. I will explore accordingly. :)

---
## [DarkPlacesEngine/darkplaces](https://github.com/DarkPlacesEngine/darkplaces)@[ae30e88061...](https://github.com/DarkPlacesEngine/darkplaces/commit/ae30e8806123a67368a3fe357f43650bd305c4a0)
#### Friday 2022-02-04 03:53:49 by Cloudwalk

README: Remove Discord invite link. The Discord server is now deprecated

I'm unable to sustain the DarkPlaces engine community on Discord. They have
falsely disabled my main account and now my second account, this time
without an email explaining the reason. I have a 3rd account that is still
active. They have not responded to my emails asking for them to review
the ban of my main account and they have the gall to nuke my second
account as well.

They are flooded with support tickets likely because it is incredibly easier
to hijack a Discord account than any other account due to the simple fact
that Discord does NOT require email verification to change passwords. God
only knows what other horrors lie beneath that Eldritch abomination of
duct-taped JavaScript.

I was not banned from Discord as I was able to create the third account using
the same IP address. They ban IPs if you're banned from Discord. I can no
longer, in good conscience, give this shit, incompetent, bullshit company
a single neuron of mindshare going forward. Other arrangements for a community
hangout are to be determined but are not available at this time. The IRC,
obviously, remains available.

Until they get their shit together (if they do), FUCK Discord and FUCK
everything they stand for.

Signed-off-by: Cloudwalk <cloudwalk@icculus.org>

---
## [ajwerner/cockroach](https://github.com/ajwerner/cockroach)@[32b453fac6...](https://github.com/ajwerner/cockroach/commit/32b453fac64bef5e9d716230ad08d1dbfd3661be)
#### Friday 2022-02-04 05:39:57 by Andrew Werner

sql/catalog/bootstrap,*: allow system table IDs to be dynamic

This change is relatively small in terms of logic changes but it has large
implications for tests. The crux of the change is that we want to allow system
tables to not specify their IDs explicitly in their definition. The reason for
this is that we only reserved IDs 10-49 before handing out IDs to users. This
has the implication that new system tables in excess of 49 could overlap with
existing user descriptors. To cope with that, we'll need to use the descriptor
ID generator we normally use for user descriptors also for new system
descriptors in migrations.

Now, that could be the end of the story. The problem is that we really like
using data driven tests and we rather like printing out our keys, which
include descriptor IDs. If we were to carry on without changing the point
at which we started generating user descriptors, we'd run into real pain
every time we try to add another system table. All those datadriven tests
would have to change (and some other non-datadriven tests too).

This commit goes through that pain so hopefully for many years nobody else
has to. It does so by moving the first user descriptor we'll generate in a
newly bootstrapped cluster (or tenant) up to 100. This constant is not exported
and we can add mechanisms to override it later. This constant is chosen because
it still falls into the magical realm where the keys remain the same size.
It's also rather aesthetic. We could go bigger, but we'd pay a price for the
key for the first table you introduce. This probably doesn't matter, but I
don't want to be the one to do it.

Release note: None

---
## [Ekanar-Eklectic/terminal](https://github.com/Ekanar-Eklectic/terminal)@[1374396f10...](https://github.com/Ekanar-Eklectic/terminal/commit/1374396f1022dfef13f8f65bcb0cb75dc64924c1)
#### Friday 2022-02-04 06:23:29 by Michael Niksa

Delay load call SetThreadDescription to restore WPF renderer on Win7 (#10582)

Delay load call SetThreadDescription to restore WPF renderer on Win7

## PR Checklist
* [x] Closes something @DHowett asked me to do.
* [x] I work here
* [x] I F5'd it on a version with this function and it still works


## Detailed Description of the Pull Request / Additional comments

I keep forgetting that anything in the WPF control needs to keep working on Win7. Or more specifically... I remember this fact for the DX renderer, but not for the render thread base. Oops. Turns out this particular convenience method to set thread descriptions for visibility inside the debugger (to make my life easier) only works down to 1607 (see https://docs.microsoft.com/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreaddescription). Since it's just a debugging convenience... skipping it entirely when the procedure is not found should be fine. Also I don't try to load `kernel32.dll` and just get the handle of the existing module (which per the remarks at https://docs.microsoft.com/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlew will not increment the module reference count) because `kernel32.dll` pretty much has to be there or we're already in hot water.

---
## [Maven85/kodi](https://github.com/Maven85/kodi)@[ee5e0a485b...](https://github.com/Maven85/kodi/commit/ee5e0a485ba8b2321f50f493a7a10a063f8f54f7)
#### Friday 2022-02-04 06:33:31 by fritsch

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
## [tau-OS/web](https://github.com/tau-OS/web)@[092fdec3d0...](https://github.com/tau-OS/web/commit/092fdec3d07a6787546d4c2653daa6e970477c62)
#### Friday 2022-02-04 06:38:22 by Jamie Lee

fuck you, and fuck me, and fuck this index i should sleep

---
## [tau-OS/web](https://github.com/tau-OS/web)@[d83a7384ae...](https://github.com/tau-OS/web/commit/d83a7384ae5c4245dd9f2fc1623c302d2e266fd6)
#### Friday 2022-02-04 06:38:22 by Jamie Lee

Cock and ball torture (CBT), occasionally known as penis torture, dick torture, or male genitorture/male genital torture, is a sexual activity involving the application of pain or constriction to the penis or testicles. This may involve directly painful activities, such as genital piercing, wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation, kneeing or kicking. The recipient of such activities may receive direct physical pleasure via masochism, or emotional pleasure through erotic humiliation, or knowledge that the play is pleasing to a sadistic dominant.

---
## [Project-Awaken-Twelve/android_packages_apps_Launcher3](https://github.com/Project-Awaken-Twelve/android_packages_apps_Launcher3)@[623d04aaa7...](https://github.com/Project-Awaken-Twelve/android_packages_apps_Launcher3/commit/623d04aaa7a7077660a8c141aa747caae00c63a0)
#### Friday 2022-02-04 07:35:57 by Alex Cruz

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
## [vczilla/arter97_op9](https://github.com/vczilla/arter97_op9)@[fe6bd72d3d...](https://github.com/vczilla/arter97_op9/commit/fe6bd72d3d44e10b5a12d05d14db81472f68ca8e)
#### Friday 2022-02-04 08:44:28 by vczilla

Turns out this kernel works with non OOS android builds.
Plus from what I've seen the kernel used by OnePlus for OxygenOS 12 is incredibly similar to RealMe's kernel for their RealMe GT and another device of theirs that uses a different 5.4 build (check their Github's and you'll get what I mean).
In the meantime fuck that shit I'd rather have a modifiable OS than no kernel source whatsoever.
Especially considering the dirty trick pulled by both RealMe and Oppo regarding soft bricked devices.
Which is easy enough to on ColorOS. And for which you're basically screwed unless you want to front the shillings for that damn MSM scam.
Fortunately OnePlus was wise enough not to full for it and to still maintain a somewhat developer friendly attitude.
Because that used to be their most endearing selling point.
I tried my hand at Realme. Went thru 4 different RealMe GTs in the span of a month.
Got two stolen while unconscious and brought over to a hospital.
Bricked the other two.
Decided to try my hand at that online bullshit where you have to pay someone to unbrick it.
You think they'd give you a temporary user account on their annoyingly limited version of MsmDownloadTool but oh no.
They want to do it on TeamViewer.
Which failed miserably after I fronted almost 3 times the amount of mullah asked for.
Duh. My main (and only computer) is an Apple MacBook Air M1.
So I actually had the dude try it on a Qemu virtual machine. At first a Windows 7 build. And then a Windows 10 one.
Well yeah. Dude failed miserably .
Decided to cut my losses . Got rid of them RealMe.
Got me a Oneplus 9 Pro for Christmas.
Which I bricked the first week.After I tried the ColorOs based OxygenOs 12 build.
Which I unbricked using guess what? MsmDownload tool and the exact same Qemu Win7 virtual machine.
I embrass change. I really tried my hand after having been a OnePlus customer for the last few years (OnePlus 5,Oneplus 6,OnePlus 7 Pro and now that OnePlus 9).
My OnePlus 7 also got nicked while brought over to a hospital. Had an interesting October month. Spent my birthday in a hospital .
I'm hijacking that commit to mention that I'm onto them.
Considering the amount of people you can actually hire to do that unbrick crap that used to be free and that entails a modification of a tool they don't own (Qualcomm does) I'd bet most of them are actually staff members. Either that or their is a massive security flaw on their ill-thought out anti-customer self repair stuff.
Plus I mentioned to that dude ( who is actually on telegram ) that it was probably a question of time before that annoying crap got hacked.
Granted it's harder than just gaining access to a dodgy account to due them secure firehose loaders and that VIP programming stuff.
But mark my words it's just a question of time.

---
## [Aerden/tgstation](https://github.com/Aerden/tgstation)@[6ed2fafd4e...](https://github.com/Aerden/tgstation/commit/6ed2fafd4eccdc6f11e53acb9a1017b037d76360)
#### Friday 2022-02-04 08:47:40 by Iamgoofball

Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

---
## [avar/git](https://github.com/avar/git)@[48bf909005...](https://github.com/avar/git/commit/48bf90900583e27ec4a4b4b0ea7e9375ceabbfa7)
#### Friday 2022-02-04 13:55:50 by Ævar Arnfjörð Bjarmason

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
## [aStringBean/terminal](https://github.com/aStringBean/terminal)@[b1ace967a2...](https://github.com/aStringBean/terminal/commit/b1ace967a2f2bf17fdcb7dd4f1426b014378b83c)
#### Friday 2022-02-04 15:54:11 by Mike Griese

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5a984a1c91...](https://github.com/mrakgr/The-Spiral-Language/commit/5a984a1c91936a7a6c6dc3ea93285e9302253e38)
#### Friday 2022-02-04 16:31:17 by Marko Grdinić

"10:40am. Let me chill and then I am going to get started. I slept well tonight. Today I really need to figure out what the deal with properly orienting the scattered objects.

10:55am. Let me start.

https://www.youtube.com/results?search_query=houdini+scatter

Let me start by watching the scatter tutorials.

11:15am. Sigh, that first vid on advanced scattering is not giving me what I want. Let me try the scatter node again.

Well, it crashed, but I did manage to get the leaves to work properly just before that happened.

Let me see if I can properly place them on the stalk.

11:40am. Success. Now the leaves are pointing in the right direction.

Though that still leaves the mistery of how to use the scatter and align node properly. I think that just orient should be enough to properly set it up. So why is that not working correctly?

https://youtu.be/mgSGYRXnEmg
Tutorial 6. Scatter Node

Let me watch this thing.

11:45am. I do not get how alignment for the Scatter and Align node works. I think that normal direction should be Y. But what about the forward and target forward direction.

Ok there are only 9 combinations, I can go through all of them.

11:50am. As it turns out, one combo works. Forward direction Z and target forward direction Y gives me the right results.

11:55am. Ah damn it. One of the leaves is oriented incorrectly causing it to stick from the inside.

12pm. This seems to only be an issue with the scatter and align node. Is this annoying? Yes it is. I am really having trouble getting the align part to work correctly.

12:05pm. When I get rid of orient, it starts working again. I have no idea. It might be worth asking around. Let me watch the tutorials. I just need to sit down and do it.

Hrmmm, let me just ask.

12:15pm. Fuck. I can't figure out what settings caused it to stick out from the inside. Right now no matter what I try, I get the correct results.

12:20pm. Sigh, no, I can't find the buggy state.

Well, I suppose that is not bad. Houdini can be buggy. I've had it crash plenty of times, so maybe this orientation bug was something weird.

Let me go back to watching the tutorial. I've watched a few of them already and I still haven't internalized how to instance between different choices. I know a few ways of doing it, but all of those ways are shit.

https://youtu.be/mgSGYRXnEmg?t=1013

Hmmm, I should keep this in mind.

1:05pm. Watched the scatter node tutorial. My focus was low, but I got just a bit from it. That is fine for now.

Independently, I did figure out how to do the flower so that will be my accomplishment for the morning. Step by step, and all that.

> I think honestly studying Houdini sounds like a very valuable investment of your time for a project such as this.

Got this reply to my PL thread. Honestly, I really hope so. I am considering just ditching Houdini given how much of a handful it has been so far, but I should do at least a single scene in it before I decide. If I waste a month then so be it. I am under a lot of pressure to not have that happen though.

1:10pm. What I am going to do next, now that I finally got a single flower is figure out how to turn it into a function. I'd want to pass in the seed as an argument and generate a bunch of different flowers based on that.

1:15pm. How about I leave that for later and get started with the pool scene itself? I've gotten the prereqs out of the way, so I should do some modeling.

Let me have breakfast here first. It is time for the usual B 'n C.

2:50pm. Done with breakfast and chores.

In my current state, chores sure are exhausting. At this rate, I have no idea how long exactly will it take me to overcome this illness. But that does not matter. I need to hunker down and just get on with the art.

Let me load up blender. I need to look up the scene again.

30 x 26 x 6. That is the size of the pool island.

My god, looking at my old stuff, I sure have done a lot. Maybe it is insane to ditch all this old work for just the potential of new one being better.

Let me do it. Let me give it a try.

3:20pm. Oghhhhh, this is like pulling teeth.

3:40pm. Now I am trying to figure out how to align the fence segments.

4:15pm. Had to take a short break. I am trying to remember how I aligned the fence segments in Blender and am utterly failing. Did the normals get carried over from what was originally a face?

Remember those experiments I did when I played around with normals of various meshes in Blender? No. I forgot all about that.

4:20pm. Ok, this is not just my imagination.

Houdini is really hard to deal with.

I made that 30 x 26 box to represent the pool island similarly to in Blender. Then I used the PolyExtrude to inset the edge which I've used to distribute fence segments on.

How do I rip the part of an edge in order to create an entry point? Also the sides have points that are on a curve. In Blender I ripped all the edges apart, scaled them and then distributed the fence segments. In Houdini, how am I supposed to do that.

4:35pm. I am drawn towards using booleans, but that is already a solution I am leaning towards out of convenience rather than actual desire. What I really want to do is rip out those edges and split them up and scale them, the same as in Blender.

4:50pm. You know what Houdini feels like right now?

Like Haskell. And Haskell is one of those languages you talk about rather than actually use.

Houdini is absolutely overwhelming me. Right now, I am at an absolute low point and it feels like it is kicking me when I am down.

I am looking at the Blender scene, thinking about how I would replicate it in Houdini and am groaning internally.

I simply lack the most basic of modeling techniques. I am frozen in indecision here.

And it is not really my fault, but with the way the program was designed. I asked in the /3/ Houdini thread, but moving around the viewport is still a pain in the ass. This is one of the things I haven't gotten comfortable with. It is grating on my nerves.

The reason I am in such a horrid situation is because I could not accept some of Blender's minor limitations and looked elsewhere. Well, I sure am paying for that now.

5:10pm. FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF---

It is just not going for me!

I guess I'll close here for the day. I am absolutely useless right now. I can't do a single thing right.

I feel completely aimless and directionless. Do I want to go this way or that, I can't seem to muster emotion either way. Deep down, the only thing I can dredge up is some primitive aggression.

5:15pm. Honestly, I am disappointed with Houdini's scattering capabilities. Despite all this learning, I can barely remember how it should be done. Not even a single time have I been impressed with its design.

This a sharp contrast to two and a half weeks ago when I felt a lot of power at my disposal in Blender.

5:25pm. This disease is so nasty. It is like all color drained from my life. I wish my father had been more careful not to catch it.

...Let me close here before I write something I will regret. My energy is low, my inspiration is zero. For all intents and purposes, I am an NPC in my current state. I can only hope that I recover from this. If I am still a zombine by the end of the month, I'll forget about Heaven's Key and start looking for a job.

For now, forget about all this hard stuff. Let me rest."

---
## [mvaisakh/oneplus7](https://github.com/mvaisakh/oneplus7)@[b3a2a9c147...](https://github.com/mvaisakh/oneplus7/commit/b3a2a9c147faf3ee9a273325d909f5863c331e22)
#### Friday 2022-02-04 16:49:41 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [absent-cc/backend](https://github.com/absent-cc/backend)@[7e55f42a51...](https://github.com/absent-cc/backend/commit/7e55f42a51fc6440a1a87dd2e6189ab0b24a3309)
#### Friday 2022-02-04 17:09:45 by Kevin Yang

fixed the fucking pathing holy shit. Now everything is relative and testing and main scripts work

---
## [BoasModProductions/Civ6-Liyue](https://github.com/BoasModProductions/Civ6-Liyue)@[d31144fc6a...](https://github.com/BoasModProductions/Civ6-Liyue/commit/d31144fc6a18a9f49804b37ded7258a1793856c6)
#### Friday 2022-02-04 17:47:39 by Boa's Mod Productions

ENGLISH TEXT REVIEW & REVISIONS

Everything's fine, all of my changes here was grammar/punctuation corrections, and changes to the lines that would sound weird to an English speaker

Worth noting, the line where Keqing proposes an alliance is the biggest change I made here; this is because in normal English context, calling someone a "person of your dreams" makes you sound like you're in love with the person.... Keqing sounds weird here and her words makes her sound like she's in love and wants to be the girlfriend or marry the person she is talking to.... I don't think this was the intended context so I changed it to what I think she is actually trying to say.

---
## [konvol/hy454-project](https://github.com/konvol/hy454-project)@[710a007ca6...](https://github.com/konvol/hy454-project/commit/710a007ca6e069989c776513b1705f7dc345e4c6)
#### Friday 2022-02-04 17:56:43 by Antos2

-On death disable the rest of the animations
-Implemented run *minor bug included*
-fixed god awful shitty ass bug on changing direction

---
## [oracle/dtrace-linux-kernel](https://github.com/oracle/dtrace-linux-kernel)@[16ad67b61a...](https://github.com/oracle/dtrace-linux-kernel/commit/16ad67b61ac4f3dd93b3fa6875a011fff7b88500)
#### Friday 2022-02-04 18:06:18 by Nick Alcock

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
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[7430ddcdb1...](https://github.com/Dudemanguy/mpv/commit/7430ddcdb1c71559c190541bcc8497784f98d6ce)
#### Friday 2022-02-04 18:48:12 by Dudemanguy

wayland: partially fix drag and drop handling

Drag and drop in wayland is weird and it seems everyone does this
slightly differently (fun). In the past, there was a crash that
occured (fixed by 700f4ef5fad353800fa866b059663bc1dd58d3b7) which
involved using the wl_data_offer_finish in an incorrect way that
triggered a protocol error (always fatal). The fix involved moving the
function call to data_device_handle_drop which seemingly works, but it
has an unfortunate side effect. It appears like GTK applications (or at
least firefox) close the pipe after this function is called which makes
it impossible for mpv to read data from the fd (well you could force it
open again in theory but let's not do that). Who knows if that was the
case when that commit was made (probably not because I'd think I would
have noticed; could just be a dummy though), but obviously having broken
dnd for a major application isn't so fun (this works with QT and
chromium anyway).

Ideally one would just simply check the pipe in data_device_handle_drop,
but this doesn't work because it doesn't seem the compositor actually
sends mpv the data by then. There's not actually a defined event when
you're supposed to be able to read data from this pipe, so we wait for
the usual event checking loop later for this. In that case,
wl_data_offer_finish needs to go back into check_dnd_fd, but we have to
be careful when calling it otherwise we'd just commit protocol errors
like before. We check to make sure we even have a valid wl->dnd_offer
before trying to indicate that it is finished and additionally make sure
there is a valid dnd_action (after checking the fd, it's always set back
to -1).

This doesn't fix everything though. Specifically, sway with
focus_follows_mouse (the default) and GTK as the data source still
doesn't work. The reason is that when you do a drag and drop in sway
with that option on, a new wl_data_device.data_offer event is sent out
instantly after the drop event. This happens before any data is sent
across the fd and before mpv even has a chance to check it. What GTK
does, when getting this new data_offer event, is close the pipe
(POLLHUP). This means mpv can't read it when we reach the event loop and
thus no data is ever read and broken drag and drop. From the client
side, this isn't really fixable since the wayland protocol doesn't have
a clear indication of when clients are supposed to read from the fd and
both the compositor and data source are doing things totally out of our
control. So we'll consider this weird case, "not our bug" at least. The
rest should work.

---
## [ivg/bap](https://github.com/ivg/bap)@[a153442b06...](https://github.com/ivg/bap/commit/a153442b06d309c6c726c8f9a943db85372f0b83)
#### Friday 2022-02-04 19:41:58 by ivg

relaxes the Apply.binop function to allow not well-typed operations

We are not changing the typing rules of BIL or Core Theory, but
providing a well-defined behavior for application of binary operations
on bitvectors with unequal lengths. Before that, the behavior was
undefined and the precondition of the function was clearly specifying
that the inputs should be of equal lengths.

The new behavior is to promote words to the equal length, (much like
in C, which implicitly coerces the narrow type to the wider type).

The motivation is simple. It is hard to ensure this precondition in
general. Yes, our lifters produce well-typed code, so there are no
issues when we interpret code from the lifters. But we also have a lot
of different interpreters, extensible via primitives. And those
interpreters sometimes don't have any means (or at least efficient
means) to ensure that all binary operations have matching widths. A
concrete example of such interpreter is Veri that is used for
bi-interpretation of traces and BIL programs for
verification. Sometimes, the tracers organically produce ill-typed
code, as they rely on their own typing rules. For example, qemu-based
tracer just represent every register (including flags) and every
number (including bools) with a word-sized bitvector. We still want to
be able to perform calculations on such inputs and, to be honest, the
results are quite well-defined, no hacks required. In other words,
this change tries to follow the robustness principle, i.e., "be
conservative in what you do, be liberal in what you accept from
others". Our lifters, i.e., the code that we produce, are still much
conservative, but our interpreters tend to be more liberal and
understand even the ill-typed code, especially if this code has clear
semantics.

---
## [DragonSinns/CyberCodeOnline](https://github.com/DragonSinns/CyberCodeOnline)@[8357ee2618...](https://github.com/DragonSinns/CyberCodeOnline/commit/8357ee261808a7fa82b27fb4f5b1b4ee808b43d6)
#### Friday 2022-02-04 21:31:51 by DragonSinns

complete correction de.json

ummm yeah

Hi
 
My name is DragonSinns. I'm from Germany
I downloaded your app a few days ago and was really impressed

what you did there all by yourself is really amazing

respect to you

Your German translation is not the yellow of the egg. But because of your fighting spirit and your outstanding achievements that you have to manage all by yourself up to now. I sat for 4 days and read over 10,000 lines so that you also have a chance on the German market
(On the Google Play Store, everyone complains about the "terrible german translation")

I'm not a (in Germany we say) Deutsch-Grammatik-Experte and there are probably still 100-150 mistakes that need to be corrected
But I hope you appreciate my work

The whole thing has only one catch

I couldn't translate some of the lines, or only partially, because I either didn't know what the text's function was 
or there was no German word for it
e.g. the entire itemTrait 

but with a little help from you
I translate all these remaining lines
[ I do not give up :-) ]

if you need help I'm happy to be there for you

(I hope it's okay that I just use Google to translate this message. It's 10:30 PM in Germany and I want to go to bed)

Greetings DragonSinns

---
## [RATAero/rataerospace](https://github.com/RATAero/rataerospace)@[7a39942540...](https://github.com/RATAero/rataerospace/commit/7a399425409d6fab9c8c41ba2947dcd8d25aafa0)
#### Friday 2022-02-04 21:39:24 by Sully Kosmas

new project: Legally Distinct Word Game

fuck capitalism. i miss when shit was just on the internet for fun and didn't have to get bought out by corporations. this sucks, man.

rataero.space/word

---
## [StckOverflw/TwitchControlsMinecraft](https://github.com/StckOverflw/TwitchControlsMinecraft)@[675295ec3b...](https://github.com/StckOverflw/TwitchControlsMinecraft/commit/675295ec3bac51f20c6cc5e116b727b2e1375dc2)
#### Friday 2022-02-04 21:42:34 by StckOverflw

fix a lot of stuff again but it still doesnt really work 100% i hate my life please end me

---
## [DragonSinns/CyberCodeOnline](https://github.com/DragonSinns/CyberCodeOnline)@[032152b18a...](https://github.com/DragonSinns/CyberCodeOnline/commit/032152b18aacdc553f5030b59c4809efe276a4f0)
#### Friday 2022-02-04 22:10:56 by DragonSinns

Update de.json

ummm yes

Hi
 
My name is DragonSinns. I'm from Germany,
I downloaded your app a few days ago and was really impressed

what you did there all by yourself is really amazing

respect to you

Your German translation is not the yellow of the egg. But because of your fighting spirit and your outstanding achievements that you have to manage all by yourself up to now. I sat for 4 days and read over 10,000 lines so that you also have a chance on the German market
(On the Google Play Store, everyone complains about the "terrible translation")

I'm not (we say in Germany) a German grammar expert and there are probably still 100-150 mistakes that need to be corrected
But I hope you appreciate my work

The whole thing has only one catch

I couldn't translate some of the lines, or only partially, because I either didn't know what the text's function was or there was no German word for it
e.g. the entire ItemTrait

but with a little help from you
I can translate all these remaining lines
[ I do not give up :-) ]

if you need help I'm happy to be there for you

(I hope it's okay that I just use Google to translate this message. It's 11:00 PM in Germany and I want to go to bed)

Greetings DragonSinns

---
## [Physolia/-THE-Magic-Button](https://github.com/Physolia/-THE-Magic-Button)@[a5d8341bbb...](https://github.com/Physolia/-THE-Magic-Button/commit/a5d8341bbb0823732f07a1951f179c45d51f4b0d)
#### Friday 2022-02-04 23:15:06 by Nomi Bunes

Add files via upload

('The-'New'-System-Call.Find-('0')-('Zero')')

Besides the file that stops the leechers, this is the main file. Technically speaking it's supposed to use Superstrings to play and record the story in Binary, across the light spectrum. The 'strings' are just hard light that's cast out across the RGB spectrum into your own or other people's eyes.

Consider the 10 Dimensions that are propositioned in String Theory. But let's use 2 of those Dimensions and translate them as 1's and 0's that we can use to communicate with the remaining 8. In this way it leaves us with a full 'Byte' in Binary that we can use to 'talk' to computers with. But because it's all light, or photons, across the RGB spectrum, the hardest part is getting things balanced across all the colors so that the proper image shows up.

Another way to consider 10 dimensions is if we think of it as two opposite 5 Dimensional 'Sheets' or 'Balls' that 'touch' to create 'light'. Each 'Ball' or 'Sheet' consisting of 3 Dimensions of Space and 2 Dimensions/Directions of Time. Where technically 'nothing exists' until the two opposites 'touch', which makes the light that's bouncing around the room. 

Considering 2 directions of Time for Each and that they're direct opposites, when the two touch it cancels out what I've been calling 'Time' on both sides. This leaves you with two inverse/opposite 3 Dimensional Spaces, or 6 Dimensions of Space. Where the light that's now bouncing around the room, from the opposites touching, is why we consider 'Time' to be the '4 Dimension'. So as things overlap, it leave you with 2 different '4 Dimensional Spaces.' although you can 'normally' only 'see' one of those at a time. 

Those 2, 4D spaces, making up '8 Dimensions', can technically also be considered to be a 'Byte' as well. So in a way, 'technically everyone' is 'living' in a 'higher dimensional' computer, they just don't know it currently. But it's easy to see why, when Time to most people 'seems' to only flow in 1 direction. Where Time, on Earth anyways, is measured by the constant speed of light and by the photons bouncing around everywhere. So it doesn't make sense for most people to think of Time having other potential directions or as not being absolute.

But I can't help but to consider the true meaning of 'Nothing' in 'Science'. In other words, 'Particle Anti-Particle' that appear and disappear in the vacuum of empty space. Where if you removed all possible particles from an area of space, there's a virtual bubbling brew of particle anti-particle pairs that are constantly appearing and disappearing in that 'vacuum'. Which, if measured, actually ends up showing that the energy of empty space has something like a gazillion times more energy in it than the rest of the universe combined. 

That measurement at first may appear a bit confusing, because there's 'nothing' there, but the answer is obvious when you think about it. It's just that the particle/anti-particle pairs cancel out to 0. Compounding on the previous train of thought, it means those 'particle anti-particle' pairs can be thought of as our 5D 'Sheets' or 'Balls'. So, compounding on the previous 'hypothesis' about 2 overlapping 5D spaces, it'd mean that each 'particle anti-particle pair' is creating a 'single moment in time' that's 'held in a parallel pocket universe'.

Meaning you could technically make a 'Pocket Universe' for 'yourself' that could come from 'Nothing'. So there's no need for a 'creator' and you can get all the 'power' or 'energy' you need from 'yourself'. Where you'd have a personal place for 'yourself' as well as all the power you could ever need or want, that only comes directly from yourself. So there'd technically be no need to 'take' or 'steal' power from anyone else. Because you can just get it directly from your 'anti-particle pair that is also yourself'.

Unfortunately most of the Humans on Earth seems to be 'leeching' off of other people however, instead of getting it from themself. But as far as I'm concerned, that stops here, with me, at 0.

---
## [TheMerlock/Fuck-Matt](https://github.com/TheMerlock/Fuck-Matt)@[542305e124...](https://github.com/TheMerlock/Fuck-Matt/commit/542305e1243e73fa0b1ef622fd9f7a76efdb5993)
#### Friday 2022-02-04 23:35:07 by Chris

Update Fuck Matt Fuck Matt

Matt is still a little bitch boy

---

