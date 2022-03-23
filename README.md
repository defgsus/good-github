## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-22](docs/good-messages/2022/2022-03-22.md)


1,700,242 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,700,242 were push events containing 2,705,845 commit messages that amount to 200,990,507 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [kangwenhang/terminal](https://github.com/kangwenhang/terminal)@[855e1360c0...](https://github.com/kangwenhang/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Tuesday 2022-03-22 00:11:41 by Mike Griese

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

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[28ee8129a5...](https://github.com/Buildstarted/linksfordevs/commit/28ee8129a53ed83d09310b762b481d0c56d4e83b)
#### Tuesday 2022-03-22 01:06:22 by Ben Dornis

Updating: 3/22/2022 1:00:00 AM

 1. Added: Plain Text Sports
    (https://plaintextsports.com/)
 2. Added: Structured (Synchronous) Concurrency
    (https://fsantanna.github.io/structured-concurrency.html)
 3. Added: You, your parents, and the hotness of who you marry
    (https://dynomight.net/hotness/)
 4. Added: Non-dotcom domains hurt startups
    (https://www.darrennix.com/blog/non-dotcom/)
 5. Added: Building Your Own Nodemon
    (https://hire.jonasgalvez.com.br/2022/mar/20/building-your-own-nodemon/)
 6. Added: Hacks can be Good Code Too
    (https://brianschrader.com/archive/hacks-can-be-good-code-too/)
 7. Added: SendilKumarN
    (https://sendilkumarn.com/blog/my-views-on-zig-2022/)
 8. Added: How To Criticize Coworkers
    (https://alexturek.com/2022-03-18-How-to-criticize-coworkers/)
 9. Added: Penny Wise and Cloud Foolish
    (https://danielcompton.net/2022/03/21/penny-wise-cloud-foolish)
10. Added: Error handling across different languages
    (https://blog.frankel.ch/error-handling/)
11. Added: Brian Robert Callahan
    (https://briancallahan.net/blog/20220321.html)
12. Added: My self-hosting setup has an UPS now, here's my experience with it
    (https://ounapuu.ee/posts/2022/03/21/ups-i-did-it-again/)

Generation took: 00:06:11.7140322
 Maintenance update - cleaning up homepage and feed

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[211a90331c...](https://github.com/ammarfaizi2/linux-block/commit/211a90331ccd425eeb7fc3df09a310730ae54b57)
#### Tuesday 2022-03-22 01:21:11 by Palmer Dabbelt

RISC-V: Don't check text_mutex during stop_machine

We're currently using stop_machine() to update ftrace, which means that
the thread that takes text_mutex during ftrace_prepare() may not be the
same as the thread that eventually patches the code.  This isn't
actually a race because the lock is still held (preventing any other
concurrent accesses) and there is only one thread running during
stop_machine(), but it does trigger a lockdep failure.

This patch just elides the lockdep check during stop_machine.

Fixes: c15ac4fd60d5 ("riscv/ftrace: Add dynamic function tracer support")
Suggested-by: Steven Rostedt <rostedt@goodmis.org>
Reported-by: Changbin Du <changbin.du@gmail.com>
Signed-off-by: Palmer Dabbelt <palmerdabbelt@google.com>
Signed-off-by: Palmer Dabbelt <palmer@rivosinc.com>

--

Changes since v1 [<20210506071041.417854-1-palmer@dabbelt.com>]:
* Use ftrace_arch_ocde_modify_{prepare,post_process}() to set the flag.
  I remember having a reason I wanted the function when I wrote the v1,
  but it's been almost a year and I forget what that was -- maybe I was
  just crazy, the patch was sent at midnight.
* Fix DYNAMIC_FTRACE=n builds.

---
## [987123879113/pcsx2](https://github.com/987123879113/pcsx2)@[d6684efd26...](https://github.com/987123879113/pcsx2/commit/d6684efd262ef1c83d37c50b48edc478952dddf9)
#### Tuesday 2022-03-22 01:21:42 by RedDevilus

GameDB: GS HW Batch X

Relevant:
Bully
Colosseum - Road to Freedom
Dark Chronicle (Dark Cloud 2)
Killzone
God of War
Gun
Midnight Club 3
Mortal Kombat - Deadly Alliance
Need for Speed Carbon / Most Wanted / Undercover
Prince of Persia - Sand of Time / The Two Thrones / Warrior Within
Resident Evil 4 (BioHazard 4)
Thrillville / Off the Rails

---
## [pixelcmtd/CMMSS](https://github.com/pixelcmtd/CMMSS)@[9ead3d1f64...](https://github.com/pixelcmtd/CMMSS/commit/9ead3d1f64e81e03b05e37cda3467c431417a32d)
#### Tuesday 2022-03-22 01:29:28 by pixel

turned homebrew analytics off

fuck you homebrew devs why do you think this is a good idea

---
## [antimike/music](https://github.com/antimike/music)@[5451b05301...](https://github.com/antimike/music/commit/5451b05301e164aeb1cdcd30aa12dd220a41db33)
#### Tuesday 2022-03-22 02:08:07 by Michael Haynes

import itunes-library-dirs library Ludwig van Beethoven, \320\237\321\221\321\202\321\200 \320\230\320\273\321\214\320\270\321\207 \320\247\320\260\320\271\320\272\320\276\320\262\321\201\320\272\320\270\320\271; Daniel Barenboim, Pinchas Zukerman, Jacqueline du Beethoven_ Violin Sonatas Nos 7-10 _ Tchaikovsky_ Piano 01 Sonata for and No 7 in C minor, Op 30 2 _Eroica__ I Allegro con brio 02 II Adagio cantabile 03 III Scherzo 04 IV Finale 05 8 G major, 3_ assai 06 Tempo di Minuetto 07 vivace 08 10 96 _The Cockcrow__ moderato 09 espressivo 11 Poco allegretto Pink Welcome to the Machine Purple In-A-Gadda-Da-Vida (Instrumental) In-a-Gadda-da-Vida (Full Extended Album Version) In\342\200\220A\342\200\220Gadda\342\200\220Da\342\200\220Vida Another One Bites Dust Keep Yourself Alive Year of Love Suzanne The Queen Soldier Beach Good Vibrations Boys Do You Want Know a Secret Girl Day Sunshine Got Get Into My Life Here, There Everywhere In Lovely Rita What SPOKEY DOKEY Dark Side Speak Me Breathe On Run Great Gig Sky Money Us Them Any Colour Like Brain Damage Eclipse cover Planet Telex Bends High Dry Fake Plastic Trees Bones (Nice Dream) Just Iron Lung Bullet Proof Wish Was Black Star Sulk 12 Street Spirit (Fade Out) Reel Big Turn Radio Sell Out Richard Se\303\261or Juan Hungarian Dance #1 Minor Quintet f movement Quartet #3 c Minor, 1stmvmt_ Minor,Op 3rd Movement_ #5 f# Intro To Epistrophy I'll Never Find Where Is Love_ Intermezzo minor 76, String #2 G, 111 -1st Mvmt_ 111-2nd 111-3rd 13 111-4th 14 Capriccio d 15 Concerto D, 77-3rd Royal Crown Mugzy\342\200\231s Hey Pachuco! Live Walkin\342\200\231 Blues Park\342\200\231s Place Datin\342\200\231 With Dough Trouble Tinsel Town Topsy Rise Fall Mondello Honey Child (reprise) Sarah As Follows We Won't Lost & Defeated Night God-Fearing Not Yet Overture Cinders Sea Wants, Will For Garden\342\200\231s End {Explain} Albatross New Amazing Things Always on This Line Woman by Well Hammer Apology Showstopper Could Belong Save Introducing Under 21 Scott Joplin; Joplin_ His Complete Please Say A Picture Her Face Crush Collision March Harmony Club Waltz Combination Original Rags Maple Leaf Rag Swipesy - Cake Walk Sunflower Slow Drag Peacherine Augustan Easy Winners Cleopha Strenuous Am Thinking Pickanniny Days 16 Ragtime 17 Breeze from Alabama 18 Elite Syncopations 19 Majestic 20 Entertainer Something Doing 22 Weeping Willow 23 Little Baby 24 Palm 25 Favorite 26 Sycamore 27 Cascades 28 Chrysanthemum 29 Rosebud Bethena 31 Leola 32 Dear 33 Binks 34 Eugenia 35 Antoinette 36 Snoring Sampson 37 Gladiolus 38 Searchlight 39 Nonpareil 40 When Your Hair Snow 41 Rose 42 Heliotrope Bouquet 43 School 44 Fig 45 Sugar Cane 46 Pine Apple 47 Wall 48 Solace 49 Pleasant Moments 50 Country 51 Paragon 52 Euphonic Sounds 53 Stoptime 54 Felicity 55 Highlights From _Treemonisha_ 56 Real 57 Prelude Act 3 58 Frolic Bears 59 Lovin' Babe 60 Joplin's 61 Kismet 62 Magnetic 63 Reflection 64 Silver Swan 65 Lily 66 Sensation Simon Homeward Bound At Zoo 59th Bridge Song (Feelin\342\200\231 Groovy) Asking Emily, Whenever May Scarborough Fair Canticle Mrs Robinson Boxer Why Don\342\200\231t Write So Long, Frank Lloyd Wright That Silver\342\200\220Haired Daddy Mine Over Troubled Water Sound Silence Rock Old Friends Bookends Theme Leaves Are Green Kathy\342\200\231s Steve Miller Joker Stone Temple Dead Bloated Sex Type Thing Wicked Garden Memory Sin Naked Sunday Creep Piece Pie Plush Wet Bed Crackerman River Goes Tried True_ Best Tom\342\200\231s Diner 99 F\302\260 Ted La Espada de la Tico All\342\200\220American Move Dirty Stab Back Along It Ends Tonight Change Mind Drive 11_11 P Inside Top World Straitjacket Feeling I\342\200\231m Waiting Can\342\200\231t Take Avett January Wedding Hard Day\342\200\231s Should Have Known Better If Fell Happy And Tell Buy Time at All I\342\200\231ll Cry Instead Said Today Home Be Before You\342\200\231ve Hide Away Need You\342\200\231re Going Lose Naturally It\342\200\231s Only Too Much See I\342\200\231ve Seen Dizzy Miss Lizzy Let Two Dig Pony Across Universe Maggie Mae I've After 909 Blue Magical Mystery Tour Fool Hill Flying Jay Way Mother Walrus Hello Goodbye Strawberry Fields Forever Rich Man U Prudence Glass Onion Ob\342\200\220La\342\200\220Di, Ob\342\200\220La\342\200\220Da Wild Continuing Story Bungalow Bill While Guitar Gently Weeps Happiness Warm Gun Martha Tired Blackbird Piggies Rocky Raccoon Pass By Road_ Julia Birthday Yer Nature\342\200\231s Son Everybody\342\200\231s Except Monkey Sexy Sadie Helter Skelter Long Revolution 1 Savoy Truffle 9 Come Busted Rump Countdown Breaks Down Leavin\342\200\231 Trunk Heavy Soul She Said, Eyes Yearnin\342\200\231 Brooklyn 240 Years Midnight Hurt Hold Arms Boy Least Likely Party Gentle Fur Soft as Monsters Paper Cuts Panda Cola Spiders Close Glad Hitched Wagon Battle Sleeping Pillow Hugging Grudge Tiger Heart God Takes Care \320\241\320\262\321\217\321\202\320\276\321\201\320\273\320\260\320\262 \320\242\320\265\320\276\321\204\320\270\320\273\320\276\320\262\320\270\321\207 Pianists 20th Century, Volume 84_ Sviatoslav Richter 2, 18_ Moderato sostenuto scherzando Preludes, major B-flat 4 D 5 Etudes, C-sharp E F-sharp 6 D-flat E-flat Waldszenen 82_ Eintritt Einsame Blumen Verrufene Stelle Freundliche Landschaft Herberge Vogel Als Prophet Jagdlied Abschied Toccata C, Fantasie 17_ Durchaus Fantastisch Und Leidenschaftlich Vorzutragen Im Legendenton Langsam Getragen Durchweg Leise Zu Halten Etwas Bewegter

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[8b1ec33143...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/8b1ec331432234f358b26ee1627c10358ccae6a7)
#### Tuesday 2022-03-22 03:00:42 by LeonY24

P90 (#12125)

* P90 SMG

le new gun for new away mission we're planning to make

* Update p90.dm

* includes p90.dm

my fucking retard ass hadnt shit included bruh

---
## [linux-chenxing/linux](https://github.com/linux-chenxing/linux)@[c570449094...](https://github.com/linux-chenxing/linux/commit/c570449094844527577c5c914140222cb1893e3f)
#### Tuesday 2022-03-22 03:02:04 by Jason A. Donenfeld

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
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c7b09fab02...](https://github.com/treckstar/yolo-octo-hipster/commit/c7b09fab023f07c79164a65af776423e5077e841)
#### Tuesday 2022-03-22 05:00:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Slothy-lol/AkarisSubnauticaMods](https://github.com/Slothy-lol/AkarisSubnauticaMods)@[b148469804...](https://github.com/Slothy-lol/AkarisSubnauticaMods/commit/b148469804f71538f371b03dbe86083a8ead0f62)
#### Tuesday 2022-03-22 06:22:22 by Nagorogan

changed shit

changed shit. Had super in depth description before, real funny too, but github fucked me over and I don't have it. Now you just get this. Blame github not me.

---
## [Stygota/CodeWars_JSKata](https://github.com/Stygota/CodeWars_JSKata)@[cfa8b85996...](https://github.com/Stygota/CodeWars_JSKata/commit/cfa8b85996499638128686ca9f40820f07993767)
#### Tuesday 2022-03-22 07:54:48 by Christopher Fuller

Adds numbers of arbitrary length taken as strings.  Returns the answer
as a string as well.  I couldn't remember my basis representation from
high school number theory super well, so I kind of hacked how I handled
carries.  I suppose I could have used bitshifts and base 2 conversions
along with complements to do it, but my brain just wasn't firing.

---
## [Cygnus-devices/device_xiaomi_sdm845-common](https://github.com/Cygnus-devices/device_xiaomi_sdm845-common)@[1d39b80ad6...](https://github.com/Cygnus-devices/device_xiaomi_sdm845-common/commit/1d39b80ad68251184b58888ba7fa5f879e57c255)
#### Tuesday 2022-03-22 10:05:56 by Dhruv Gera

rootdir: Spoof selinux state

Fuck you google and your cts

---
## [influxdata/influxdb_iox](https://github.com/influxdata/influxdb_iox)@[55643945a1...](https://github.com/influxdata/influxdb_iox/commit/55643945a1a654d0db0bcc5eb0a42d7c3185efa9)
#### Tuesday 2022-03-22 11:17:08 by Marco Neumann

refactor: `querier` w/o `db` (#4063)

* feat: `TombstoneRepo::list_by_table`

* feat: `ParquetFileRepo::list_by_table_not_to_delete`

* refactor: `querier` w/o `db`

Get the `querier` to work w/o relying on `db`. A few notes:

- Testing is kinda shallow, we really need to get `query_tests` working
  w/ `querier` (see #3934).
- We still run a sync loop for namespaces, tables and schemas. This will
  be a replaced by "update namespace incl. tables and schemas on demand".
  Note however that we cannot fetch single tables and schemas on demand
  at the moment, because DataFusion doesn't implement async schema
  inspection (only `scan` / "give me all the chunks" is async). I think
  that's OK for now and we can address this later.
- There is NO cache for parquet files and tombstones at the moment. For
  correctness, they need to be fetched in a single transaction (or we
  need a kinda tricky sequence number / logical clock tracking) and I am
  not sure yet how this makes sense when we have the ingester data wired
  up and predicates pushed down to the catalog (see next point). So
  let's measure first and then decide on a caching strategy for this.
- Predicates are currently NOT pushed down to the catalog. I'll need to
  figure out how to extract time range from generic DataFusion
  expressions to make that work (it's easier for InfluxRPC queries, but
  they are not tested at the moment, see first point).

Sorry that this commit is kinda huge. I initially planned to only
migrate the chunks away from `db` and leave the tables and schemas for a
follow-up PR, but the DataFusion trait structure (chunks are bound to
their tables) makes this kinda pointless.

Closes #3974.

* docs: explain what we're doing

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

* docs: mention tracking issues

* docs: explain what we're doing

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

---
## [postgresql-cfbot/postgresql](https://github.com/postgresql-cfbot/postgresql)@[ec62cb0aac...](https://github.com/postgresql-cfbot/postgresql/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Tuesday 2022-03-22 11:47:01 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [chandu078/kernel_oneplus_sm8350](https://github.com/chandu078/kernel_oneplus_sm8350)@[57a6948cb8...](https://github.com/chandu078/kernel_oneplus_sm8350/commit/57a6948cb87a8775c4715a2a7e34c35cb50bb75d)
#### Tuesday 2022-03-22 12:24:58 by alk3pInjection

disp: msm: Handle dim for udfps

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
## [cristhianbenitez/cristhianbenitez.xyz](https://github.com/cristhianbenitez/cristhianbenitez.xyz)@[b8d85cf88b...](https://github.com/cristhianbenitez/cristhianbenitez.xyz/commit/b8d85cf88b17643b3d4bae5a7aa1d2b9bc335373)
#### Tuesday 2022-03-22 14:39:13 by Cristhian

feat(blogpost): first blog post ever, hard as fuck boi

just a blog post to understand a topic better, sorry I just do this for my brain

---
## [newstools/2022-the-chronicle](https://github.com/newstools/2022-the-chronicle)@[c7086f73cb...](https://github.com/newstools/2022-the-chronicle/commit/c7086f73cb54040af8ef2deb73a589af595ac31d)
#### Tuesday 2022-03-22 14:53:41 by Billy Einkamerer

Created Text For URL [www.chronicle.co.zw/15-year-old-girl-kills-friend-for-snatching-her-boyfriend/]

---
## [ghostwriter/laminas-org-laminas-component-installer](https://github.com/ghostwriter/laminas-org-laminas-component-installer)@[4a882e650d...](https://github.com/ghostwriter/laminas-org-laminas-component-installer/commit/4a882e650d8a280b2f33b65b493e25d9e0bccbd3)
#### Tuesday 2022-03-22 15:56:03 by Michał Bundyra

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
## [princepalsingh-apple-com-au/docs](https://github.com/princepalsingh-apple-com-au/docs)@[e21742f355...](https://github.com/princepalsingh-apple-com-au/docs/commit/e21742f355bfffb176646235ce5d6198234fe09d)
#### Tuesday 2022-03-22 15:59:36 by princepalsingh-apple-com-au

Github-private◻️⬜️◾️◼️🆕

The social media platform for trading, Collaborative way.
where only friend list will be from the person working industry with resources provided by Org’s(Domain) 
With 100 %
Content provide by our platform is comes under Our
Polices only till the user became our partner or affiliate.
Our Ai technology make your day hustle free as sharing your 
Personal data in open web surface which leads to decrease social reach as compare to estimate reach.
All social media task can be perform under one platform user need basic knowledge about social platform they are using or going to use. 
The best part about our platform interface -
- 


VIRTUAL machine use as platform 
For our platform Be-one.

For making individual basic knowledge our platform going affiliate or take help from our respected Logo’s (All the brands help G-human to  get discover) as i able to see the things really clear that money is no more in my fair list as able to see only the possibilities  we can do or till now we did.

Due to respect of hands hits key then words 
I will try to take care of every expect written on white papers.. 

In this project I trust on the Amazing companies… 
I will pay 💰 ASWELL.
I know they never stoping me to create my one 😂.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[65329f4fac...](https://github.com/pytorch/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Tuesday 2022-03-22 16:50:15 by Edward Z. Yang

Disable meta device tests.

After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Pull Request resolved: https://github.com/pytorch/pytorch/pull/74468

Approved by: https://github.com/mruberry

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[8f1c87d1ca...](https://github.com/EaW-Team/equestria_dev/commit/8f1c87d1cad704ed0301c72ea0d0988246844462)
#### Tuesday 2022-03-22 16:57:29 by Philetairos

CTH can now get dragons because fuck you :sunglasses:

---
## [staten-island-tech/vue-project-2-ainu](https://github.com/staten-island-tech/vue-project-2-ainu)@[aaab2719a7...](https://github.com/staten-island-tech/vue-project-2-ainu/commit/aaab2719a745d2dd0269a41e878d4db8515a9af4)
#### Tuesday 2022-03-22 17:44:01 by darrenh6

12 Stout Street

Yuh
Real Rx
I used to wake up in my room in the morning
Put on my dirty shoes in the morning
Heard momma crying last night
Think the lights finna go out
Only thing on my mind is hitting a lick
Her Friend in prison for doing some shit
Say I'mma go to prison for doing some shit
Only thing on my mind is booming a bitch
12 Stout Street, I hated that house
I had to learn early on bein' a man about
My momma ain't never buy me shit
I sold drugs and robbed for all my shit
Momma said, "Baby that was years ago"
"Don't stress about shit that happened years ago"
This shit'd take a bitch years to know
I cried in the cold till my tears was froze
I hit a lick to help my momma out
How the fuck my mom the one to kick me out?
How the fuck you gonna send me out to the streets?
How the fuck you gonna say I can't come home to sleep?
How the fuck I come out your pussy and you
Choose your husband like you knew that Friend before me?
How the fuck you gon' turn your back on me?
How the fuck you gon' leave me flat on E?
How you gon' do that knowing they killed my dad?
You supposed to be my mom and my dad
I wish that fucking house would burn down
I couldn't tell you then but shit, I'll tell you now
For so many years, I held it down
I never in my life wanted to sell drugs
I would've been cool with playing games and shit
But instead I'm running with the gang and shit
Robberies done turned into shootings
Your son done did a gang and shit
It'd take a year to explain this shit
We don't stay safe, we stay dangerous
They took my brother, that fucked me up
Perc after perc, they fucking me up
Thousand percs later, still don't do nothing
Shits barely working, they're supposed to make me numb
Had flashbacks to when I was young
Bitches used to laugh and call me a bum
I was with Face, shot my first gun
Before Neo or Jet Li, I was the one
My momma ain't see it but the streets did
Said I wouldn't be shit, streets made me shit
Going through withdrawal, got me sick
I'm stretched back to back, I'm 'bout to flip
Don't look at me funny, you don't know shit 'bout me
Stood on the block with dreams of an Audi
Had a nightmare sleeping in my Audi
A Friend caught me lacking and pulled me out it
Big ass pistol to my mouthpiece
And it happened in front of 12 Stout Street

---
## [klingtnet/static-site-generator](https://github.com/klingtnet/static-site-generator)@[710c13630f...](https://github.com/klingtnet/static-site-generator/commit/710c13630fa866e82e9d68b696ad25c66ef11f7b)
#### Tuesday 2022-03-22 18:08:55 by Andreas Linz

Disable Go 1.17 in CI

🤦 I replaced interface{} already with any, of course I need to disable
Go 1.17 then.  Stuff like this happens when there is not enough time
anymore for open source work.  Priorities change over time, especially
since Covid forced most of us to stop doing (indoor) sports, meet
friends and colleagues in person, go to concerts and so on and so forth.
God, I'm missing going to concerts.  Anyways, my focus has changed a bit
and my private life is more important, hence open source work will get
less priority.  I program for fun and I hope it stays that way.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8a1d33c430...](https://github.com/mrakgr/The-Spiral-Language/commit/8a1d33c430f43fe4456f5c745407b78d3d51f7d6)
#### Tuesday 2022-03-22 19:55:09 by Marko Grdinić

"11:15am. Heroine Survival is so good I ended up reading it till 2am so I could reach the end of the assassin guild arc. Aria is the most hardcore 8 year old little girl of all time. Cold gleam in her eyes, intelligence too high is never tricked, when reincarnated does not bitch and decides to become the strongest to exist. That one last one does not fit the chinaman meme. Some other girl got reincarnated and tried to body snatch her, but the MC killed her instead and acquired her memories. That set the tone for the story.

11:50am. Ah, let me skip the morning session. Let me see if I got any answers on the forum.

I've been thinking during the night and there should be something more to painting using particle points. Just putting in a flat radius? Meh. Surely that is not it.

So towards that end, let me get the 2.5gb example file. I should study that. Did I get any replies on the forum?

12pm. Let me unpack it. I guess I'lll just transition into breakfast. I actually woke up quite early today, but did not feel like getting up. I am in a lazy mood. I'll get into it as I go along. I want to figure out how to do my own scratch textures today.

Damn, it seems I got part 2, two times instead of part 1 and part 2.

...Given that is is 9.5gb, the course by Shrimp will take a while to download.

1:15pm. Enough reading, let me do the chores. After that I'll study the Clarisse examples.

1:30pm. Done with chores. Let me start.

> UV baking
> The setup in this project lets you make a tileable scratch texture from a render. This project also shows how to bake a material using the UV bake feature.

Oh, wow, these Clarisse examples are very thorough. There are 18 different projects. To study all of this properly would take me a decent amount of time.

Hrrmmmmm...

Since things are like, I guess I'll pause my push to do the room and instead study for a few days.

https://vimeo.com/247302953?embedded=true&source=video_title&owner=1723479
Houdini Illume | COPs with Mike Lyndon

Let me start with this. What I intended to do for scraches is scatter them and then bake them using COPs. It seems that since Clarisse can do it natively, that won't be necessary, but still, let me watch the video for a bit. I'll crib it for ideas a little. I'll watch it for half an hour without commiting just yet.

1:45pm. Let the song finish and I will start.

2:10pm. 23m in and he is still ranting about random stuff.

2:20pm. Forget, he spent the first 25m talking about nothing so that now that he is finally getting to the point I've lost all interest. Let me take a break. After that I'll study the Clarisse projects while listening to music. That is the best way to spend totday.

2:40pm. Let me resume. Time to figure out those scratches. Let me check out the UV baking project.

2:55pm. This is a bit tough. I am having trouble finding my way around.

///

In the projects folder located in the archive you will find some useful examples.
Before opening any project, you must set the content directory of Clarisse ($CDIR) to the folder where you unzipped the content archive.
To set the content directory in Clarisse go to Edit > Preferences... / Project and set Content Directory.

///

I forgot to do this.

For some reason increasing the refinement count is not working.

3:10pm. Oh, the refinement count has finally started working again.

3:15pm. It stopped working. Is it just taking it really long to do it? I have no idea. I don't see any progress being made. What an annoying bug.

Oh, it started working all of a sudden. How it it go to 6 without me knowing? Oh these scraches are quite nice. At first it felt like I was seeing texturing seams, but they are not there anymore.

3:20pm. I am thinking what do I do now. This stuff is hard to understand just from looking at it. What I should do is dedicate myself and try to rebuild it piece by piece. The resources are there, what I need to do is understand it well enough to make it mself from scratch. That should be my mission. First of all, let me try to understand how baking itself works. Let me check the docs for that.

3:40pm. Took a break. I seem to be doing that a bit much today. Here is the first mission. I need to figure out how regular UV baking works. After that I'll start replicating the features of the example project.

Let me do it. I knew this was possible, but I never tried it before in either Blender or Houdini.

3:50pm. I scattered a bunch of flattened spheres like on the floor yesterday. Now I need to figure out how to bake them.

...I do not really understand how to set it up. The docs describe the UV bakign simply enough - just send rays outside from the object being baked. But how do I run that. It talks about some script in the shelf. Let me try using it but I do not think it will work.

https://youtu.be/S3I9F2kerRM
How To Bake Textures

Let me watch this.

https://youtu.be/S3I9F2kerRM?t=344

He says the viewer performs the linear to sRGB correction. This is why the image came out differenly when saved.

https://youtu.be/S3I9F2kerRM?t=378

Here is yet another convertion.

https://youtu.be/S3I9F2kerRM?t=502
> This process can be used to bake very complex and render expensive patterns to very simple set of texture maps that can even be painted on in dedicated softwares like Substance Painter.

https://youtu.be/C2fCRnbeSkw
Per-instance edition in Scatterers

> Bake and edit a scatterer

Let me watch this as well.

It has some stuff. Ok, focus me.

Now that I roughly know the process let me try my first bake.

4:40pm. Why can the UV projection mode even be disabled?

Ah, wait. I think I get it. If it is disabled, then it could potentially bake just what is on the surface.

4:45pm. Yeah, the scrach shadows and the light scattering gets baked into the image in that case. That is how that complex setup was baked despite the two objects being the same size.

https://youtu.be/S3I9F2kerRM?t=149

I need to keep in mind the middle click trick when it comes to selecting the material of the machine.

Ok, I have a grasp on that. Let me try to get the script to work.

4:55pm. Got it. The reason the script failed for me last time is probably just because I failed to pass in an a filename. Note that it was not obvious that this was the problem because the error window did not say what the error actually was.

Let me try moving the scatterer below the grid.

...When I do that I need to change the projection mode to inside. Ok.

I've grasped how this works. Let me also cover the AOVs. Let me slap some noise as color, roughness and metalicity. Then I will try replicating what he did in the video when he separated them.

5:15pm. I need to wrap my head around AOVs. Let me take a look at the video again.

6:10pm. Let me take a break here.

6:20pm. I am back. My progress has been extremely slow today. I am going to put in some overtime as I can still keep going.

Right now I am having trouble getting that basemetal file to load. For some reason it is not working properly even though it shows up in the Windows viewer.

I keep making the same mistake in the material editor. I copied the original thing, deleted the nodes, but that I ended up wiping what I had originally.

6:35pm. A few undos did the trick. This time I made sure to contextualize the material before duplicating it.

6:50pm. I do not know what went wrong last time, but something did. The metalroughness image came out grayscale. How did I even manage that?

I do not know why. This problem only happens when I click render using the Render Manager.

Hmmm, I see. There is a bug when I have the metalroughness be a two channel variable. It does not save it correctly. In fact, when I set the LUT to srgb, it crashes!

Maybe I should report this kind of bug. It does not happen when I use the UV Baker shelf tool though. I think from now I should just stick to 3 channel vars.

Now, let me see if the textures load correctly.

7pm. Let me go have lunch.

7:20pm. I am back.

7:30pm. I am munching on a mandarin as I think of what to do next. The textures load correctly. How about I make that but report? No, it seems it is all done through the bug tracker. Since I am pirating, it would be unwise to out myself too easily. I'll store it at the back of my mind and report when I buy the full version.

Now what is next? I understand how to bake with this, I should have enough to create the scratch texture that I want. But before that let study the UV baking project more. How did they get those curved shapes?

7:45pm. I am really surprised. They did not import an object from somewhere else that is in the shape of a curve. Rather it is a standard polysphere with a deformer applied to it.

I had no idea this was possible.

I am going to have to investigate this. Hmmm, the celular noise texture looks exactly like a radial gradient. I am going to play a little with this.

This is strange. How did I use the gradient texture on that planet ring?

8:30pm. I played with it and I get it now. I am in awe though.

Trying to make curve like this wouldn't even have been on the list for me. It would have been way easier to go into Houdini or Blender and just bend a flattened sphere. Getting the parameters for this right so it looks like it does is not easy.

8:40pm. I am still playing with it.

8:45pm. Let me just close here. I really haven't been particularly productive today, but I am too tired to continue.

Tomorrow, I will resume my study of the UV baking project. I think now that I understand UV baking itself, I have the most important thing down so the rest should be easier to learn.

Hmmm...at this point I should also go back to the Clarisse tutorial, the very last part of it, and refresh my memory of how AOVs work. I am a bit confused how those inbuilt ones are supposed to be used. Right now I created custom ones, but do the inbuilt ones get filled automatically in the render layer?

I don't really need to know that right now, but I find this design confusing, so I'd like to clear it up. Clarisse is a tool I should understand completely.
"

---
## [tiwai/sound](https://github.com/tiwai/sound)@[ef248d9bd6...](https://github.com/tiwai/sound/commit/ef248d9bd616b04df8be25539a4dc5db4b6c56f4)
#### Tuesday 2022-03-22 20:53:35 by Matt Kramer

ALSA: hda/realtek: Add alc256-samsung-headphone fixup

This fixes the near-silence of the headphone jack on the ALC256-based
Samsung Galaxy Book Flex Alpha (NP730QCJ). The magic verbs were found
through trial and error, using known ALC298 hacks as inspiration. The
fixup is auto-enabled only when the NP730QCJ is detected. It can be
manually enabled using model=alc256-samsung-headphone.

Signed-off-by: Matt Kramer <mccleetus@gmail.com>
Link: https://lore.kernel.org/r/3168355.aeNJFYEL58@linus
Signed-off-by: Takashi Iwai <tiwai@suse.de>

---
## [MetaMask/controllers](https://github.com/MetaMask/controllers)@[fef7cbc50f...](https://github.com/MetaMask/controllers/commit/fef7cbc50ffe6398da8ba864788b3604dbd464a9)
#### Tuesday 2022-03-22 22:05:16 by Elliot Winkler

WIP: Use Polly to mock HTTP requests in tests

**tl;dr:** I've introduced Polly as a replacement for Nock as I believe
it will lead to more readable and authentic tests. A few things:

* This is a proof of concept – I've only added it to
  CollectiblesController to start out with.
* All I've done is replace Nock requests with Polly requests. Ideally,
  we wouldn't need to mock anything manually at all and let Polly do its
  thing. Unfortunately, some HTTP requests that we are mocking no longer
  work.
* In the future, we should investigate using Ganache instead of hitting
  mainnet and exposing our Infura project id in tests.

---

Currently there are a couple of problems with our tests as it relates to
network requests:

1. We do not prevent network requests from being made. There are
   some tests which use Nock to mock requests, but not all requests are
   being mocked, and we are unaware which ones are actually going
   through.
2. Nock, although a popular package, is rather cumbersome to use, and
   makes tests difficult to understand and follow.

To address these problems, this commit replaces Nock with Polly. Polly
is a package developed by Netflix that intercepts all HTTP requests and
automatically captures snapshots (recordings) of these requests as they
are being made. These recordings are then used in successive test runs.
You can also manually mock requests if you want more manual control.

\## Why introduce another package? Why is Nock not sufficient?

When mocking requests with Nock, you must first hit the request you want
to mock for real and obtain its response data. From here you can either
copy the data and paste it straight into your test, or you can provide
mock data based on the shape of the data.

However, there are two problems with this:

1. Mocks take up space in your test, so you will probably find yourself
   extending a collection of mocks you've assembled at the top of the
   file. Once you have enough, who knows which mocks serve which tests?
2. Once you've added a mock to your test, that mock stays forever. If
   the API changes in the future, or stops working altogther, you will
   never know until you remove that mock.

Polly removes both of these problems:

1. Because Polly records request snapshots, you don't usually have to
   worry about mocking requests manually. These recordings are kept in
   files which are categorized by the tests which made the requests.
2. Because Polly actually hits the API you're mocking, you can work with
   real data. You can instruct Polly to expire these recordings after a
   designated timeframe to guarantee that your code doesn't break if
   the API ceases to work in the way you expect.

\## What about Nock Back? Doesn't this do the same thing?

It's true that Nock contains a feature to capture requests called Nock
Back. However, this is cumbersome, too:

1. You have to wrap your test in a `nockBack` call.
2. You have to name your recording files.
3. You have to call `nockDone()` in your test.

There is a package called `jest-nock-back` that fixes these issues and
makes using Nock Back very easy. However, it isn't maintained (last
release was 3 years ago) and there isn't a way to automatically expire
your recordings (which I believe is a key feature).

\## What about requests that irreversibly change data?

Some requests make irreversible changes to resources, such as
transferring a token from one account to another.

To handle these types of requests, Polly still lets you manually mock
requests just like Nock. We've configured Polly to not record a request
it doesn't recognize by default, so in this case you'll get a message
when running the test that makes such a request. From there you can make
a decision about how you'd like to mock this request — whether you want
Polly to record the request or whether you'd like to manually mock it.

That said, if the request in question involves a blockchain network,
instead of mocking the request, we might investigate whether it's
possible to use Ganache to perform the irreversible action rather than
actually hitting mainnet or some other network.

\## What are the tradeoffs for Polly vs. Nock?

* Because Polly automatically creates request mocks and these mocks are
  no longer contained in tests, developers will need to be educated
  about Polly (Polly is not as popular as Nock) and remember that it
  exists whenever updating tests.
* If a recording is no longer needed or needs to be updated, the
  associated file holding the recorded information about the request
  needs to be deleted. Finding this file is not a great experience.
* Nock has virtually zero initialization code. Polly's initialization
  code is surprisingly complicated (although that is largely hidden, so
  no one should have to mess with it).

---
## [VladinXXV/tgstation](https://github.com/VladinXXV/tgstation)@[759d24ab14...](https://github.com/VladinXXV/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Tuesday 2022-03-22 22:09:55 by san7890

Four Corners, Red Rover: An Exploration in Decal Trends [MDB IGNORE] (#65290)

* Four Corners, Red Rover: An Exploration in Decaled Trends

You there! What exactly is wrong with this photograph?!

You don't need to tell me, I've boxed it out. There's four individual corners for the decalling. This is weird. You may be asking: Why don't they use the "full tile" turf decals? Let me demonstrate.

Look at the difference between the one at left and the one in the middle. The turf decal totally smothers the nice contrast lines afforded to use by the base turf, causing it to have smooth, clammy exterior. This is probably why no mapper ever uses the full turf decal, much to the chagrin of people who stare at how big the size of this repo is.

Now, what's that on the right? Why, it's the new sprite (and pathing I made) to help counter-act this issue! This perfectly lines up with the contrast lines of the base turf, allowing us to have a non-flattened visualization, while not having four fucking turf decals a turf load upon initialization. How epic!

I've also added "contrasted" variants of the "half" and "anticorner" turf decals for future use. I probably won't go through and update this in this PR, but the opportunity remains available.

I may or not map this change across all the maps. We shall see.

* neutral corners

we love vsc

* no wait

i forgot a bunch of potential edgecases so we'll have to go back. yellow should be fine but neutral, dark, blue, and green should get a second look over

* recheck

found some stuff, probably missed out on others. let us commence forth

* MISTAKE

nearly a fucko bwoingo

* final pass

it compiles and i've had enough, someone else can probably figure it out from this point onwards

* #65230 goated my timbs

now we wait for linters to fail

* YOU DIDN'T SAY THAT THE FIRST TIME

LINTERS AAFAFAFF

---
## [VladinXXV/tgstation](https://github.com/VladinXXV/tgstation)@[884c1eeb62...](https://github.com/VladinXXV/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Tuesday 2022-03-22 22:09:55 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [MetaMask/controllers](https://github.com/MetaMask/controllers)@[729807fe97...](https://github.com/MetaMask/controllers/commit/729807fe97510ee1b59f54fd8417679652d65af0)
#### Tuesday 2022-03-22 22:13:16 by Elliot Winkler

WIP: Use Polly to mock HTTP requests in tests

**tl;dr:** I've introduced Polly as a replacement for Nock as I believe
it will lead to more readable and authentic tests. A few things:

* This is a proof of concept – I've only added it to
  CollectiblesController to start out with.
* All I've done is replace Nock requests with Polly requests. Ideally,
  we wouldn't need to mock anything manually at all and let Polly do its
  thing. Unfortunately, some HTTP requests that we are mocking no longer
  work.
* In the future, we should investigate using Ganache instead of hitting
  mainnet and exposing our Infura project id in tests.

---

Currently there are a couple of problems with our tests as it relates to
network requests:

1. We do not prevent network requests from being made. There are
   some tests which use Nock to mock requests, but not all requests are
   being mocked, and we are unaware which ones are actually going
   through.
2. Nock, although a popular package, is rather cumbersome to use, and
   makes tests difficult to understand and follow.

To address these problems, this commit replaces Nock with Polly. Polly
is a package developed by Netflix that intercepts all HTTP requests and
automatically captures snapshots (recordings) of these requests as they
are being made. These recordings are then used in successive test runs.
You can also manually mock requests if you want more manual control.

## Why introduce another package? Why is Nock not sufficient?

When mocking requests with Nock, you must first hit the request you want
to mock for real and obtain its response data. From here you can either
copy the data and paste it straight into your test, or you can provide
mock data based on the shape of the data.

However, there are two problems with this:

1. Mocks take up space in your test, so you will probably find yourself
   extending a collection of mocks you've assembled at the top of the
   file. Once you have enough, who knows which mocks serve which tests?
2. Once you've added a mock to your test, that mock stays forever. If
   the API changes in the future, or stops working altogther, you will
   never know until you remove that mock.

Polly removes both of these problems:

1. Because Polly records request snapshots, you don't usually have to
   worry about mocking requests manually. These recordings are kept in
   files which are categorized by the tests which made the requests.
2. Because Polly actually hits the API you're mocking, you can work with
   real data. You can instruct Polly to expire these recordings after a
   designated timeframe to guarantee that your code doesn't break if
   the API ceases to work in the way you expect.

## What about Nock Back? Doesn't this do the same thing?

It's true that Nock contains a feature to capture requests called Nock
Back. However, this is cumbersome, too:

1. You have to wrap your test in a `nockBack` call.
2. You have to name your recording files.
3. You have to call `nockDone()` in your test.

There is a package called `jest-nock-back` that fixes these issues and
makes using Nock Back very easy. However, it isn't maintained (last
release was 3 years ago) and there isn't a way to automatically expire
your recordings (which I believe is a key feature).

## What about requests that irreversibly change data?

Some requests make irreversible changes to resources, such as
transferring a token from one account to another.

To handle these types of requests, Polly still lets you manually mock
requests just like Nock. We've configured Polly to not record a request
it doesn't recognize by default, so in this case you'll get a message
when running the test that makes such a request. From there you can make
a decision about how you'd like to mock this request — whether you want
Polly to record the request or whether you'd like to manually mock it.

That said, if the request in question involves a blockchain network,
instead of mocking the request, we might investigate whether it's
possible to use Ganache to perform the irreversible action rather than
actually hitting mainnet or some other network.

## What are the tradeoffs for Polly vs. Nock?

* Because Polly automatically creates request mocks and these mocks are
  no longer contained in tests, developers will need to be educated
  about Polly (Polly is not as popular as Nock) and remember that it
  exists whenever updating tests.
* If a recording is no longer needed or needs to be updated, the
  associated file holding the recorded information about the request
  needs to be deleted. Finding this file is not a great experience.
* Nock has virtually zero initialization code. Polly's initialization
  code is surprisingly complicated (although that is largely hidden, so
  no one should have to mess with it).

---
## [gamma-delta/HexMod](https://github.com/gamma-delta/HexMod)@[b83d09d540...](https://github.com/gamma-delta/HexMod/commit/b83d09d540eb904f19551f0a802c4f525cc65787)
#### Tuesday 2022-03-22 22:15:15 by gamma-delta

im the best fucking coder on planet earth holy shit im so good

---
## [MetaMask/controllers](https://github.com/MetaMask/controllers)@[bece786839...](https://github.com/MetaMask/controllers/commit/bece786839607234493ea95cd8b39e7b80bb205f)
#### Tuesday 2022-03-22 22:19:08 by Elliot Winkler

WIP: Use Polly to mock HTTP requests in tests

**tl;dr:** I've introduced [Polly] as a replacement for Nock as I believe
it will lead to more readable and authentic tests. A few things:

* This is a proof of concept – I've only added it to
  CollectiblesController to start out with.
* All I've done is replace Nock requests with Polly requests. Ideally,
  we wouldn't need to mock anything manually at all and let Polly do its
  thing. Unfortunately, some HTTP requests that we are mocking no longer
  work.
* In the future, we should investigate using Ganache instead of hitting
  mainnet and exposing our Infura project id in tests.

[Polly]: https://netflix.github.io/pollyjs/#/README

---

Currently there are a couple of problems with our tests as it relates to
network requests:

1. We do not prevent network requests from being made. There are
   some tests which use Nock to mock requests, but not all requests are
   being mocked, and we are unaware which ones are actually going
   through.
2. Nock, although a popular package, is rather cumbersome to use, and
   makes tests difficult to understand and follow.

To address these problems, this commit replaces Nock with Polly. Polly
is a package developed by Netflix that intercepts all HTTP requests and
automatically captures snapshots (recordings) of these requests as they
are being made. These recordings are then used in successive test runs.
You can also manually mock requests if you want more manual control.

When mocking requests with Nock, you must first hit the request you want
to mock for real and obtain its response data. From here you can either
copy the data and paste it straight into your test, or you can provide
mock data based on the shape of the data.

However, there are two problems with this:

1. Mocks take up space in your test, so you will probably find yourself
   extending a collection of mocks you've assembled at the top of the
   file. Once you have enough, who knows which mocks serve which tests?
2. Once you've added a mock to your test, that mock stays forever. If
   the API changes in the future, or stops working altogther, you will
   never know until you remove that mock.

Polly removes both of these problems:

1. Because Polly records request snapshots, you don't usually have to
   worry about mocking requests manually. These recordings are kept in
   files which are categorized by the tests which made the requests.
2. Because Polly actually hits the API you're mocking, you can work with
   real data. You can instruct Polly to expire these recordings after a
   designated timeframe to guarantee that your code doesn't break if
   the API ceases to work in the way you expect.

It's true that Nock contains a feature to capture requests called [Nock Back].
However, this is cumbersome, too:

[Nock Back]: https://github.com/nock/nock#nock-back

1. You have to wrap your test in a `nockBack` call.
2. You have to name your recording files.
3. You have to call `nockDone()` in your test.

There is a package called `jest-nock-back` that fixes these issues and
makes using Nock Back very easy. However, it isn't maintained (last
release was 3 years ago) and there isn't a way to automatically expire
your recordings (which I believe is a key feature).

Some requests make irreversible changes to resources, such as
transferring a token from one account to another.

To handle these types of requests, Polly still lets you manually mock
requests just like Nock. We've configured Polly to not record a request
it doesn't recognize by default, so in this case you'll get a message
when running the test that makes such a request. From there you can make
a decision about how you'd like to mock this request — whether you want
Polly to record the request or whether you'd like to manually mock it.

That said, if the request in question involves a blockchain network,
instead of mocking the request, we might investigate whether it's
possible to use Ganache to perform the irreversible action rather than
actually hitting mainnet or some other network.

* Because Polly automatically creates request mocks and these mocks are
  no longer contained in tests, developers will need to be educated
  about Polly (Polly is not as popular as Nock) and remember that it
  exists whenever updating tests.
* If a recording is no longer needed or needs to be updated, the
  associated file holding the recorded information about the request
  needs to be deleted. Finding this file is not a great experience.
* Nock has virtually zero initialization code. Polly's initialization
  code is surprisingly complicated (although that is largely hidden, so
  no one should have to mess with it).

---
## [entrez/xNetHack](https://github.com/entrez/xNetHack)@[879897d885...](https://github.com/entrez/xNetHack/commit/879897d885462664cabcd521ca62fc3fd5a4fcf5)
#### Tuesday 2022-03-22 22:45:38 by copperwater

Add black mold

A new monster? In xNetHack???

This has been planned for quite a while, and only now gotten around to.
The general idea is adding a member to the F class that actually might
pose a threat to the player rather than being firmly in assists-only
status. This is particularly relevant since F monsters grow on moldy
corpses.

The general details of the monster come from SporkHack's gray fungus,
via EvilHack which imported it fairly directly from there. Differences
include:
- It's named "black mold" rather than "gray fungus" because black mold
  is a real-life thing that can grow in living spaces, making the
  inhabitants sick.
- It's modeled after the other molds. It has similar stats, no active
  attacks, etc.
- It doesn't confer poison resistance when eaten. Instead it makes the
  consumer deathly ill when eaten. (Though this is curable by vomiting
  and is therefore labeled as FoodPois -- it's a little weird that the
  sickness from the passive attack is not curable by vomiting and the
  sickness from eating it is, but that's due to the different ways it's
  making you sick, one by having it in your digestive tract and one by
  inhaling spores.)
- It appears quite late for a F monster, with a difficulty of 8.
- The Brewing Patch applies to it, allowing black mold to be fermented
  in fruit juice to later turn to sickness.

Unlike in EvilHack, monster illness is not implemented and so the black
mold's passive attack does nothing when it hits a monster.

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[745426eff2...](https://github.com/Ryll-Ryll/tgstation/commit/745426eff227ff556105147a4802540617decd7b)
#### Tuesday 2022-03-22 23:44:11 by LemonInTheDark

Adds a colorblind accessability testing tool (#65217)

* Adds a colorblind accessability testing tool

I keep finding myself worrying about if things I create will be parsable
for colorblind people. So I've made a debug tool for approximating
different extreme forms of colorblindness.

It's very very much a hack. We can't do the proper correction required
to actually deal directly with long medium and short wavelengths of
light, so we need to rely on approximations. Part of that means say,
bright things being brighter then they ought to be. S not how people
actually experience things, but it's not something we can do anything
about in byond.

Anyway uh, it works by taking color matrixes, and using the plane master
grouping system floyd added to apply them to most all parts of the game
you would want to color correct.

There's some slight fragility here, but I couldn't think of a better way
of handling it.

We also need to deal with planes that have BLEND_MULTIPLY as their
blendmode, since that fucks up the filter. I've come up with a hack for
it, since I wanted to avoid breaking anything.

Oh and since I want it to apply to huds too I added plane masters to
represent them. I think that's about it.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [pj1312/tgstation](https://github.com/pj1312/tgstation)@[dd747fcc5a...](https://github.com/pj1312/tgstation/commit/dd747fcc5a46df051a5fe0e42950c46c72269244)
#### Tuesday 2022-03-22 23:56:42 by MrMelbert

BIDDLE HERETICS: Heretic revamp! (Shadow Realm, UI Overhaul, Refactoring, and Murderhoboing Tweaks)  (#64658)

About The Pull Request

This PR seeks to revamp heretic in it's almost entirety.

Closes #58435
Closes #62114
Closes #63605

image
Gameplay changes:

    The heretic no longer starts with a Codex Cicatrix or a Living Heart.
        Heretics now draw transmutation runes by using any writing tool while having Mansus Grasp active.
            The Mansus Grasp can be used to remove heretic runes.
        Draining influences can be done with "right click".
            While draining, people who examine you may get a message hinting that you're interacting with an influence.
            Drained influences can also be dispersed with anomaly neutralizers!
        The Codex Cicatrix is now a researchable item that lets you gain additional knowledge from influences.
            The Codex can still draw and remove runes, and does it faster.
        The Living Heart is now the heretic's heart. Literally. It's the heart in their chest. Their heart takes on the appearance of a living heart, and they can pulse it on demand to track their targets. This makes an audible noise.
            If your heart is lost (you're disemboweled or whatever), you need to do a ritual to regain it!

    Casting any heretic spell (besides Grasp) requires a Focus.
        A Heretic Focus is a neck item they can transmute.
        Heretic robes also function as a focus when toggled up.
        Ascending also disables the need for a focus, because of course.

    Heretics now gain 1 knowledge point passively every 20 minutes.

    Sacrificing has been revamped entirely.
        A heretic now gains four sacrifice targets on spawn.
            One random crewmember
            One member of their department
            One member of security
            One member of command (a "high value" sacrifice)
        You can sacrifice people who are in in soft-crit, hard-crit, or dead.
        Sacrificing someone will cuff them (if they are not), HEAL them, revive them, and set them unconscious. After a short time. they will be sent to a shadow realm. This shadow realm is themed to your heretic type.
            The shadow realm is a 2 minute long survival challenge where the sacrificee is subject to a constant barrage of shadowy hands.
            If they survive, they are teleported back to a random turf with no memory of how they got there. They'll also slur a TON to get the point across.
            If they die, their corpse is teleported back to a random turf on the station.

    No more multi-hearting! Your targets are your own.
        BUT adds a knowledge that allows heretics to reroll their sacrifice targets with a ritual.

    Each path now has a "Rituals of Knowledge". These are randomly generated rituals that may be difficult to complete but awards knowledge points in return.

    Ascending now has some requirements.
        To learn the ascension ritual, you need to complete all of the objective you are assigned.
        The ascension ritual now each have a varied requirement, instead of "needing 3 bodies" only.

    Other minor gameplay changes:
        Lots of balance tweaking.
            Buffed some summons.
            Buffed the Lord of the Night very slightly.
            Nerfed the Madness Mask.
        Put a limit on the amount of blade transmutations possible at once. 3 for flesh, 2 for other paths.
        Logs of BUG fixing.
        Rust Grasp is now based on right click for surfaces instead of combat mode.
        General grammar and flavor tweaks a ll around.

Admin / code changes:

    Revamped the way heretics appear within the traitor panel.
        You can now easily see who they're targeting for sacrifice and what they have researched
        Also adds some helpful buttons to heretics, like giving them points!
    Refactored much, much of heretic code
        LIKE ALL OF HERETIC CODE WAS IN 4 FILES.
            Split up all the knowledge, spells, and items that belong to the heretic into their own files and folders.
        Not only that, but everything internally was still named "Eldritch Cultist" and similar.
            Almost every mention of "Eldritch Cultist" has been properly replaced by "Heretic".
    Much better reference handling all around.
    General code improvements over heretic stuff.
    Unit tests, because of course.

Todo

Sprites for the focus

    Look at adding 1-2 other objectives prior to ascension. Theft? Special rituals? ("Rust [x] tiles to be able to ascend")

Why It's Good For The Game
Okay but why?

Heretics are not in a good place at the moment, this much is clear. They've been completely disabled on MRP for this reason.

The reasoning is simple: A lot of murder.
There's nothing inherently wrong with an antagonist heavy with murder, but the Heretic really missed the mark.
Gib, gib, gib, then ascend so you can keep killing.

In the background, the Heretic was FULL of flavorful spells, rituals, and "lore" stolen from Cultist Simulator that was unfortunate enough to be shackled to the heretic's gameplay loop.

So, this revamp aims to amend that:

Dial back the heretic's focus on mass murder and put more focus on the heretic's interesting flavor.
Spooky maintenance rituals, knowledge seeking maniac.

    Sacrifice no longer outright kills / requires murder, meaning a heretic can progress without racking up a bodycount.
    Influence is gained passively over time, so they can spend influence on more interesting side paths.
    Side paths are required to progress to ascension, so they're encouraged to explore new things.

Ultimately, while there still may be a little way to go, this PR seeks to take a good leap in starting it.
Changelog

cl Melbert
add: Large scale heretic revamp!
expansion: The Codex Cicatrix is no longer a roundstart heretic item. Research is handled through their antag info UI. Rune drawing is done by using a writing tool with Mansus Grasp active in your offhand. The actual Codex is an unlockable ritual item now.
expansion: The Living Heart is no longer a roundstart heretic item - their actual heart now becomes their Living Heart, and it makes a sound when triggered. Losing your heart (being disemboweled) will require you to do a ritual to regain it.
expansion: The Hereic Antag UI has been overhauled, and now hosts much of their mechanics as well as providing some helpful tips for newer players.
expansion: Most heretic spells now require a focus to cast. All heretics can make a basic focus necklace, and some heretic equipment also functions as a focus. (Credit to Imaginos for the focus sprite!)
expansion: Heretics now passively gain +1 influence every 20 minutes.
expansion: Heretic sacrificing has been reworked. You can now sacrifice people who are in soft crit or weaker. Sacrificing someone heals them, cuffs them, and teleports them to the SHADOW REALM, where they must dodge a barrage of hands to survive. Survive long enough and you return without memory - die, and your body will be thrown back.
expansion: Heretics now have a few new rituals, including the Ritual of Knowledge, a randomly generated ritual that awards knowledge points.
expansion: Heretic ascension now has a few requirements - you must complete your objectives assigned to you prior to learning the final ritual, and all the final rituals have been changed a bit!
qol: Using the Heretic's Mansus Grasp on surfaces (EX: Rust Grasp) now works on right-click, instead of combat mode.
qol: Used heretic influences can now be removed with a Anomaly Neutralizers.
balance: Some heretic rituals are now limited in the amount they can make. You can only have up to 2 heretic blades crafted at once (3 if you are Path of Flesh).
balance: The Lord of the Night has been buffed to be a little scarier. Did you know the Lord of the Night can eat arms to regain body parts and heal?
balance: Buffed some heretic summons - mostly their health pools.
balance: Nerfed the heretic's Mask of Madness. It can no longer infinite stam-crit you.
balance: Nerfed the heretic's ash mark.
balance: Nerfed a bunch of on-hit-heretic-blade effects. Many effects only apply on mark detonation now: Void blade silence, flesh blade wounds, ash blade gasp cooldown refund.
fix: Fixed quite a few bugs and unintended behaviors with heretic code.
refactor: Refactored and improved much of Heretic code. Improved the file structure dramatically.
admin: The heretic's traitor panel has been beefed up a bit.
/cl

---

