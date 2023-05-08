## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-07](docs/good-messages/2023/2023-05-07.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,884,408 were push events containing 2,722,365 commit messages that amount to 147,795,627 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 68 messages:


## [bearrrrrrrr/coyote-bayou](https://github.com/bearrrrrrrr/coyote-bayou)@[27993e1350...](https://github.com/bearrrrrrrr/coyote-bayou/commit/27993e1350d80ac72d35a3cc9db0f8db055be3ba)
#### Sunday 2023-05-07 00:38:06 by Tk420634

You're a swamp lizard, Harry

Adds a magic quirk with curated magic choices.

-Healing Staff Sprite is fuckled
-Spellblade Sprite is also fuckled

---
## [NemesisTheory/s2p](https://github.com/NemesisTheory/s2p)@[11d4c01ab4...](https://github.com/NemesisTheory/s2p/commit/11d4c01ab42fb5072d4bdbed9c1437a6283d6d43)
#### Sunday 2023-05-07 00:51:20 by NemesisTheory

I'm ALWAYS GONE WITH THE WIND

CRAWLING IN AND OUT OF MY MIND
GOD KNOW I LOST ALL MY FAITH,
A SICKNESS WITH NO REMEDY
EXCEPT THE ONES INSIDE OF ME (inside of me)
YOU EVER WONDER HOW DEEP YOU CAN SINK INTO NOTHING AT ALL?
DISINTEGRATE, ANNIHILATE ME

---
## [YassevZriona/Meow-Meow-Fork](https://github.com/YassevZriona/Meow-Meow-Fork)@[72135fb148...](https://github.com/YassevZriona/Meow-Meow-Fork/commit/72135fb148a44eeb548478cd270af0d78489fb76)
#### Sunday 2023-05-07 01:35:58 by Yassev

Incomplete content pack manager but some fixes and improvements included

now! time for 7 hours of school since my parents got me extra school on weekend... I hate my life

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[200b739c0a...](https://github.com/CoiledLamb/lorbstation/commit/200b739c0a0bbfff95dbfd697786013c92cb6cf6)
#### Sunday 2023-05-07 01:44:37 by Kyle Spier-Swenson

Refactors and defuckulates dbcore. Adds support for min_threads rustg setting, Reduce query delay, Make unit tests faster (#74852)

dbcore was very fuckulated.

It had 3 lists of queries, but they all had their own current_run style
list to support mc_tick_check (as it was already being done before with
the undeleted query check, so i can understand why they ~~cargo culted~~
mirrored the behavior) This was silly and confusing and unneeded given
two of those loops can only process at most 25 items at a time on
default config, plus these were cheap operations (ask rustg to start
thread, ask rustg to check on thread).

Because of the confusingness of the 6 lists for 3 query states, The code
to run pending/queued queries immediately during world shutdown was
instead looking at the current_run list for active queries, **meaning
those queries got ran twice.**

The queued query system only checked the current active query count in
fire(), meaning even when there was nothing going on in this subsystem
new queries had to wait for the next fire() to run (10 ticks, so 500ms
on default config)

Those have all been fixed.

the config `BSQL_THREAD_LIMIT` has been renamed to
`POOLING_MAX_SQL_CONNECTIONS` and its default was lowered to match
MAX_CONCURRENT_QUERIES .

added a new config `POOLING_MIN_SQL_CONNECTIONS`, allowing you to
pre-allocate a reserve of sql threads.

The queue processing part of SSdbcore's fire() has been made to not obey
mc_tick_check for clarity and to make the following change easier to do:

If there is less than `MAX_CONCURRENT_QUERIES` in the active queue, new
queries activate immediately.

(its ok that there are two configs that kinda do the same thing,
POOLING_MAX_SQL_CONNECTIONS maps to max-threads in the mysql crate, and
it seems to only be a suggestion, meanwhile MAX_CONCURRENT_QUERIES can't
do anything during init, which is when the highest amount of concurrent
queries tend to happen.)

:cl:
config: database configs have been updated for better control over the
connection pool
server: BSQL_THREAD_LIMIT has been renamed to
POOLING_MAX_SQL_CONNECTIONS, old configs will whine but still work.
fix: fixed rare race condition that could lead to a sql query being ran
twice during world shutdown.
/:cl:

I have not tested this pr.

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[773cc9542a...](https://github.com/CoiledLamb/lorbstation/commit/773cc9542a54837fc52b15eb09cc98d7226049fb)
#### Sunday 2023-05-07 01:44:37 by MrMelbert

Adds admin alert for revs created through traitor panel (#74862)

## About The Pull Request

So like, using traitor panel to make revs doesn't work. 

Revolutions live and die, currently, by the revolution ruleset datum
dynamic creates. It manages the hostile environment and also processes
to check whether either side should be winning or not.

This means that the revolutionary buttons in the traitor panel are kind
of noob-admin-bait. You press it for a funny revolution and then you
realize it's screwed when all the heads are dead and everyone's
stumbling around cluelessly

This has a proper solution, albeit somewhat difficult - separate out the
revolution from the ruleset, make admin spawned revs create a
revolution. I can do this but it's a lot of effort and this works in the
meanwhile

Pops up a TGUI alert when an admin presses "add revolutionary" in
traitor panel when there is no ongoing revolution. Simply enough, gives
them an alert that it will not work correctly. Lets them decide whether
they want to deal with that. (Because you can manually deal with it via
proc calls, if you've got code smarts.)

## Why It's Good For The Game

Stops admins from stumbling into the same trap without warning.

Can be removed in the future easily when revs are coded better. 

## Changelog

:cl: Melbert
admin: Adds a warning that spawning revs via traitor panel will not
function as expected.
/:cl:

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[821123b598...](https://github.com/CoiledLamb/lorbstation/commit/821123b59850bc4d0556b8dd7e0cf169f7fa6bc3)
#### Sunday 2023-05-07 01:44:37 by ChungusGamer666

Makes a whole bunch of wooden objects flammable (#74827)

## About The Pull Request

This whole PR started because I realized that baseball bats are not
actually flammable which I found weird, then I looked at a whole bunch
of other stuff that really should be flammable but also isn't.

## Why It's Good For The Game

Makes wooden objects behave slightly more consistently? Honestly, most
of these seem like oversights to me.

## Changelog

:cl:
balance: The following structures are now flammable: Picture frame,
fermenting barrel, drying rack, sandals, painting frames, paintings,
spirit board, notice board, dresser, displaycase chassis, wooden
barricade
balance: The following items are now flammable: Baseball bat, rolling
pin, mortar, coffee condiments display, sandals, wooden hatchet, gohei,
popsicle stick, rifle stock
/:cl:

---
## [MechanicTC2/PokeFever](https://github.com/MechanicTC2/PokeFever)@[2c20789382...](https://github.com/MechanicTC2/PokeFever/commit/2c207893824c3ac66c0944781c15563fe58677a5)
#### Sunday 2023-05-07 01:52:16 by MechanicTC

Merge pull request #49 from MechanicTC2/FelixtheL

fuck you

---
## [keg038/hello-world](https://github.com/keg038/hello-world)@[31854db059...](https://github.com/keg038/hello-world/commit/31854db0594dabb709f3dc839ba6195cd6ae3ec5)
#### Sunday 2023-05-07 02:06:41 by keg038

Update README.md

Tried to make my students laugh with a terrible dad joke that wasn't funny.

---
## [kas-catholic/confessit-web](https://github.com/kas-catholic/confessit-web)@[e1f4dc5804...](https://github.com/kas-catholic/confessit-web/commit/e1f4dc5804740d506df16e16d0795411203c4eba)
#### Sunday 2023-05-07 02:22:55 by Mike

Update Examination

A deacon reached out to me via email to note that suicidal thoughts are
not in themself sinful (though could be a sign of depression, anxiety,
or other mental illness and might still require help). As such, we
should update the text to read simply,

> Did I attempt suicide?

CCC 2281-2283

---
## [khalid3456/GlucoTru-USA-Official-Site-100-Natural-And-Pure](https://github.com/khalid3456/GlucoTru-USA-Official-Site-100-Natural-And-Pure)@[af0dcfb604...](https://github.com/khalid3456/GlucoTru-USA-Official-Site-100-Natural-And-Pure/commit/af0dcfb604a34d22cedb22a51c5cb7e47d0a5dae)
#### Sunday 2023-05-07 02:33:32 by Khalid Hussain

https://www.us-neurorise-us.us/neurorise-try

NeuroRise™: Doctor Formulated Natural Hearing Support Formula
NeuroRise is an all-natural supplement that combines twenty different ingredients to aid general health, concentration, and the symptoms associated with hearing loss.
https://www.us-neurorise-us.us/neurorise-try
If you are looking for an ear supplement to enhance your hearing health, This hearing support formula can help. The product contains an all-natural blend of powerful ingredients that work together to improve hearing and tinnitus symptoms without side effects.

So, try the NeuroRise supplement out for yourself and experience the numerous hearing and brain health benefits that follow along with it.

visa
Scientific Breakthrough
April 2023 - New Scientific Discovery
The Scientific Breakthrough You’ve Been Waiting For....
A true labor of love, NeuroRise is the product of 8 years of research and a team of dedicated medical professionals working day and night to unlock the secrets of a healthier, happier life.

Featuring all-natural ingredients that have a proven effect on maintaining a healthy auditory system, is an all-in-one supplement that takes care of your ears and ensures they remain healthy and functional.

---
## [jnutt367/psalms](https://github.com/jnutt367/psalms)@[02ad0cce77...](https://github.com/jnutt367/psalms/commit/02ad0cce77afd847fdd9212bea40b32f152d1728)
#### Sunday 2023-05-07 02:35:23 by Jason Nutt (He/Him) Christian Developer/Creator

Update index.js

A shiggaion[b] of David, which he sang to the Lord concerning Cush, a Benjamite.
1 Lord my God, I take refuge in you;
    save and deliver me from all who pursue me,
2 or they will tear me apart like a lion
    and rip me to pieces with no one to rescue me.

3 Lord my God, if I have done this
    and there is guilt on my hands—
4 if I have repaid my ally with evil
    or without cause have robbed my foe—
5 then let my enemy pursue and overtake me;
    let him trample my life to the ground
    and make me sleep in the dust.[c]

6 Arise, Lord, in your anger;
    rise up against the rage of my enemies.
    Awake, my God; decree justice.
7 Let the assembled peoples gather around you,
    while you sit enthroned over them on high.
8     Let the Lord judge the peoples.
Vindicate me, Lord, according to my righteousness,
    according to my integrity, O Most High.
9 Bring to an end the violence of the wicked
    and make the righteous secure—
you, the righteous God
    who probes minds and hearts.

10 My shield[d] is God Most High,
    who saves the upright in heart.
11 God is a righteous judge,
    a God who displays his wrath every day.
12 If he does not relent,
    he[e] will sharpen his sword;
    he will bend and string his bow.
13 He has prepared his deadly weapons;
    he makes ready his flaming arrows.

14 Whoever is pregnant with evil
    conceives trouble and gives birth to disillusionment.
15 Whoever digs a hole and scoops it out
    falls into the pit they have made.
16 The trouble they cause recoils on them;
    their violence comes down on their own heads.

17 I will give thanks to the Lord because of his righteousness;
    I will sing the praises of the name of the Lord Most Hig

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[f1fef9b0c3...](https://github.com/OrionTheFox/Skyrat-tg/commit/f1fef9b0c3f10e6191ed51be93d092050e77c531)
#### Sunday 2023-05-07 03:42:50 by SkyratBot

[MIRROR] Demotes Psyker Pirates to Bounty Hunter Duty [MDB IGNORE] (#20951)

* Demotes Psyker Pirates to Bounty Hunter Duty (#75031)

This PR demotes the Psyker-gang from a pirate team to a fugitive hunting
team. For more information on Psyker pirates, please refer to #71650.

Stuff this also does in the process:
- Gives fugitive hunters their own subfolder in the fugitives antagonist
folder, moves some of their stuff into hunter-specific files rather than
interlacing it with the rest of the fugitive code.
- Moves the hunter backstories to defines, to make reading things easier
while I made this change.
- Exhaustively moves everything related to psykers from being
pirate-oriented to hunter-oriented (typepaths, locations where stuff is
defined, etc. There should be nothing left behind related to psykers in
anything pirate related). (Tell me if I missed anything somehow).

They still get their ship (they even get their own custom
psyker-friendly prisoner capsule). They still have a bunch of lethally
chambered firearms. They're the same gunrunning nutcases they were
before, just as bounty hunters.

To assist with basic tasks such as "getting to the station" or "figuring
out who the fuck we're supposed to be kidnapping", the psykers have
"acquired" a Seer to assist them. They can _try_ to coordinate the
psykers and lead them through situations where their impairments put
them at too great a disadvantage. If you're one of the psykers, make
sure to keep this guy alive at all costs!

Why are they called Shikaris instead of hunters? Mariam-Webster says
it's a Hindi word for some kind of hunter/tracker, and it sounded like
something a bunch of space-junkies would call themselves because they
think it sounds cool.

They now also come with a slightly different motivation, now that they
can't directly threaten the crew for money. Psyker hunters now arrive
tasked with a dirty kidnapping job, payment rendered in GORE.
## Why It's Good For The Game

Psykers aren't up to the challenge of being pirates. They're bogged down
by a number of fundamental issues that render them unable to do anything
expected of pirates. As it currently stands, they present about as much
threat as you would expect from three blind junkies with guns.

Removing them wholesale would be kind of lame. They can function as a
bunch of chaotic-neutral gun-toting space-maniacs, but for the purposes
of gameplay, keeping them as pirates would be a waste of their talents.

Moving them to a lower-stakes role not only moves them to a niche they
are more capable of filling, but gives players a more lax environment to
get a grip on playing psyker without being overwhelmed.

Giving them a seeing-eye role should bring a more unique dynamic to how
psykers are played (that is, some semblance of organization rather than
blind flailing), and should help get over the mechanical hurdles of
being a psyker until better solutions can be made. It shouldn't be too
big of an impact on balance considering the psyker gang only has three
spawns, while most hunter packs have 4+.

* Demotes Psyker Pirates to Bounty Hunter Duty

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [NemesisTheory/s2p](https://github.com/NemesisTheory/s2p)@[608afcd0dc...](https://github.com/NemesisTheory/s2p/commit/608afcd0dc14a63b53110c3b96c60fb95880ff4a)
#### Sunday 2023-05-07 04:05:23 by NemesisTheory

IF GOD IS MY WITNESS, HE'LL SEE THAT ALL IS NOT WELL

CHRIST, WHAT A SIGHT, FOR SORE EYES
LOOKING DOWN ON US
ALL THE CHILDREN THAT YOU DESPISE
GOD ONLY KNOWS WHY WE WERE BORN TO BURN, OH
GOD ONLY KNOWS WHY WE WERE BORN TO BURN
A BULLET IN THE NECK DOESN'T FEEL MUCH LIKE LOVE
A MESSAGE OF REJECTION, SENT FROM ABOVE
NO FLAGS, NO HOLY BOOKS
I'LL BE IN HELL WITH THE MISUNDERSTOOD
THE SONS AND DAUGHTERS
THAT YOU WISHED TO FORGET
A DESPERATE PICTURE, OF GOD'S REGRET
ARE WE PERFECT MISTAKES? OR ALMIGHTY FUCK UPS,
ONE THING'S FOR SURE, HE DOESN'T FUCKING LOVE US, BLEGH!
HE DOESN'T FUCKING LOVE US
HATE MUST WEIGH ON YOU LIKE A BROKEN CROSS,
HATE, THE DIVIDING LINE WE'LL NEVER STEP ACROSS
OUTCAST, AND REJECT
OUTCAST, AND REJECT,
FATHER, FATHER, HOW I'VE LET YOU DOWN,
A FUCKING TYRANT IN A HOLLOW CROWN
FATHER, FATHER, HOW I'VE LET YOU DOWN,
A FUCKING TYRANT IN A HOLLOW CROWN

---
## [MaxineHelsel/CDF-Quest](https://github.com/MaxineHelsel/CDF-Quest)@[afc7de5484...](https://github.com/MaxineHelsel/CDF-Quest/commit/afc7de5484980f2fb18a8ce0dfff22d6972950da)
#### Sunday 2023-05-07 04:08:52 by Maxine Helsel

idk what fuck you i just need to fix something in stable and have to
commit changes to switch branches :middle_finger:

---
## [tonyvitonis/git](https://github.com/tonyvitonis/git)@[7891e46585...](https://github.com/tonyvitonis/git/commit/7891e465856e539c4a102dadec6dca9ac51c38df)
#### Sunday 2023-05-07 04:33:48 by Jeff King

gpg-interface: set trust level of missing key to "undefined"

In check_signature(), we initialize the trust_level field to "-1", with
the idea that if gpg does not return a trust level at all (if there is
no signature, or if the signature is made by an unknown key), we'll
use that value. But this has two problems:

  1. Since the field is an enum, it's up to the compiler to decide what
     underlying storage to use, and it only has to fit the values we've
     declared. So we may not be able to store "-1" at all. And indeed,
     on my system (linux with gcc), the resulting enum is an unsigned
     32-bit value, and -1 becomes 4294967295.

     The difference may seem academic (and you even get "-1" if you pass
     it to printf("%d")), but it means that code like this:

       status |= sigc->trust_level < configured_min_trust_level;

     does not necessarily behave as expected. This turns out not to be a
     bug in practice, though, because we keep the "-1" only when gpg did
     not report a signature from a known key, in which case the line
     above:

       status |= sigc->result != 'G';

     would always set status to non-zero anyway. So only a 'G' signature
     with no parsed trust level would cause a problem, which doesn't
     seem likely to trigger (outside of unexpected gpg behavior).

  2. When using the "%GT" format placeholder, we pass the value to
     gpg_trust_level_to_str(), which complains that the value is out of
     range with a BUG(). This behavior was introduced by 803978da49
     (gpg-interface: add function for converting trust level to string,
     2022-07-11). Before that, we just did a switch() on the enum, and
     anything that wasn't matched would end up as the empty string.

     Curiously, solving this by naively doing:

       if (level < 0)
               return "";

     in that function isn't sufficient. Because of (1) above, the
     compiler can (and does in my case) actually remove that conditional
     as dead code!

We can solve both by representing this state as an enum value. We could
do this by adding a new "unknown" value. But this really seems to match
the existing "undefined" level well. GPG describes this as "Not enough
information for calculation".

We have tests in t7510 that trigger this case (verifying a signature
from a key that we don't have, and then checking various %G
placeholders), but they didn't notice the BUG() because we didn't look
at %GT for that case! Let's make sure we check all %G placeholders for
each case in the formatting tests.

The interesting ones here are "show unknown signature with custom
format" and "show lack of signature with custom format", both of which
would BUG() before, and now turn %GT into "undefined". Prior to
803978da49 they would have turned it into the empty string, but I think
saying "undefined" consistently is a reasonable outcome, and probably
makes life easier for anyone parsing the output (and any such parser had
to be ready to see "undefined" already).

The other modified tests produce the same output before and after this
patch, but now we're consistently checking both %G? and %GT in all of
them.

Signed-off-by: Jeff King <peff@peff.net>
Reported-by: Rolf Eike Beer <eb@emlix.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [NemesisTheory/s2p](https://github.com/NemesisTheory/s2p)@[23135f8849...](https://github.com/NemesisTheory/s2p/commit/23135f8849ef9f8db2ae741c95cf625526faa9fb)
#### Sunday 2023-05-07 04:34:37 by NemesisTheory

Remember when Hell had frozen over?

The cold still burns underneath my skin
The water is rising all around me,
And there is nothing left I can give.

ALL THESE TEARS I'VE SHED,
I SAW THE WILDFIRE SPREAD
YOU SAID YOU CHEATED DEATH,
BUT HEAVEN WAS IN MY HEAD.

THEY SAY "THE GOOD DIE YOUNG",
NO USE IN SAYING "WHAT IS DONE, IS DONE"
'CAUSE IT'S NEVER ENOUGH
AND WHEN THE NIGHT GIVES WAY,
IT'S LIKE A BRAND-NEW DOOMSDAY.

WHAT WILL BE, WILL BE,
EVERY RIVER FLOWS INTO THE SEA
BUT IT'S NEVER ENOUGH
AND WHEN THE NIGHT GIVES WAY,
IT'S LIKE A BRAND-NEW DOOMSDAY.

NO MATTER WHAT THEY SAY,
IT'S LIKE A BRAND-NEW DOOMSDAY.

The ember still glow when I'm sober,
The gold in the flames burn brighter now
I have to rebuild, now it's over
Maybe now I'm lost I can live.

Souls don't break, they bend
BUT I SOMETIMES FORGET,
I HAVE TO DO THIS FOR YOU
AND THE ONLY WAY OUT IS THROUGH.

YEAH, DEATH IS AN OPEN DOOR.

Words the prophets said,
Still swimming through my head
Now there's no stars left in the sky,
'Cause this well will never run dry.
What if I completely forget?
What if I never accept?
'Cause when you fade away,
It's like a brand-new doomsday.

YEAH.

THEY SAY "THE GOOD DIE YOUNG",
NO USE IN SAYING "WHAT IS DONE, IS DONE"
'CAUSE IT'S NEVER ENOUGH
AND WHEN THE NIGHT GIVES WAY,
IT'S LIKE A BRAND-NEW DOOMSDAY.

WHAT WILL BE, WILL BE,
EVERY RIVER FLOWS INTO THE SEA
BUT IT'S NEVER ENOUGH
AND WHEN THE NIGHT GIVES WAY,
IT'S LIKE A BRAND-NEW DOOMSDAY.

NO MATTER WHAT THEY SAY,
IT'S LIKE A BRAND-NEW DOOMSDAY.

Rest in peace, Tom Searle.

---
## [Anthony-Monistere/hello-world](https://github.com/Anthony-Monistere/hello-world)@[b7a1778d23...](https://github.com/Anthony-Monistere/hello-world/commit/b7a1778d2397483f44da090940ea0da0b27cf6a4)
#### Sunday 2023-05-07 05:17:21 by Anthony-Monistere

Update README.md

Tried to make my student laugh with a terrible dad joke that wasn't funny.

---
## [asad0206/frontend-sprint](https://github.com/asad0206/frontend-sprint)@[e7e9a6cc57...](https://github.com/asad0206/frontend-sprint/commit/e7e9a6cc5767250b12c713510ddee9853e066fc0)
#### Sunday 2023-05-07 08:13:04 by asad0206

Merge pull request #2 from asad0206/newComm

die suck fuck you

---
## [lllgts/android_kernel_xiaomi_cepheus](https://github.com/lllgts/android_kernel_xiaomi_cepheus)@[1768c8271f...](https://github.com/lllgts/android_kernel_xiaomi_cepheus/commit/1768c8271f178c1da80e8f4a76a0273d99ce3832)
#### Sunday 2023-05-07 08:18:22 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[1674f25725...](https://github.com/Thunder12345/tgstation/commit/1674f25725c25e15769b031553b42144f526f841)
#### Sunday 2023-05-07 08:42:16 by John Willard

New Medical job: The Coroner (#75065)

## About The Pull Request

HackMD: https://hackmd.io/RE9uRwSYSjCch17-OQ4pjQ?view

Feedback link: https://tgstation13.org/phpBB/viewtopic.php?f=10&t=33972

Adds a Coroner job to the game, they work in the Medical department and
have their office in the Morgue.
I was inspired to make this after I had played my first round on
Paradise and messed around in there. The analyzer is copied from there
(https://github.com/ParadiseSS13/Paradise/pull/20957), and their
jumpsuit is also mostly stolen from it (i just copied the color scheme
onto our own suits).

Coroners can perform autopsies on people to see their stats, like this

![image](https://user-images.githubusercontent.com/53777086/235369225-805d482c-56c0-441c-9ef8-a42d0a0192bc.png)

They have access to Medbay, and on lowpop will get Pharmacy (to make
their own formaldehyde). They also have their own Secure Morgue access
for their office (doubles as a surgery room because they are edgelords
or whatever) and the secure morgue trays.

Secure Morgue trays spawn with their beepers off and is only accessible
by them, the CMO, and HoS. It's used to morgue Antagonists. Security's
own morgue trays have been removed.

The job in action


https://cdn.discordapp.com/attachments/950489581151735849/1102297675669442570/2023-04-30_14-16-06.mp4

### Surgery changes

Autopsies are a Surgery, and I tried to intertwine this with the
Dissection surgery.
Dissections and Autopsies both require the Autopsy scanner to perform
them, however you can only perform one on any given body. Dissections
are for experiments, Autopsies is for the paper of information.

Dissected bodies now also give a ~20% surgery speed boost, this was
added at the request of Fikou as a way to encourage Doctors to let the
Coroner do their job before reviving a body.
I also remember the Medical skill, which allowed Doctors to do surgery
faster on people, and I hope that this can do something like that
WITHOUT adding the potential for exploiting, which led to the skill's
downfall.

### Morgue Improvements

Morgue trays are no longer named with pens, they instead will steal the
name of the last bodybag to be put in them.

Morgue trays are also removed from Brig Medical areas and Robotics, now
they have to bring their corpses to the Morgue where the Coroner can
keep track and ensure records are properly updated.

### Sprite credits

I can't fit it all in the Changelog, so this is who made what

McRamon
- Autopsy scanner

Tattax 
- Table clock sprites and in-hands

CoiledLamb
- Coroner jumpsuits & labcoats (inhand, on sprite, and their respective
alternatives)
- Coroner gloves
- CoronerDrobe (the vending machine)

## Why It's Good For The Game

This is mostly explained in the hackmd, but the goal of this is:

1. Increase the use of the Medical Records console.
2. Add a new and interesting way for Detectives to uncover mysteries.
3. Add a more RP-flavored role in Medical that still has mechanics tied
behind it.

## Changelog

:cl: JohnFulpWillard, sprites by McRamon, tattax, and Lamb
add: The Coroner, a new Medical role revolving around dead corpses and
autopsies.
add: The Coroner's Autopsy Scanner, used for discovering the cause for
someone's death, listing their wounds, the causes of them, their
reagents, and diseases (including stealth ones!)
qol: Morgue Trays are now named after the bodybags inside of them.
balance: The morgue now has 'Secure' morgue trays which by default don't
beep.
balance: Security Medical area and Robotics no longer have their own
morgue trays.
balance: Dissected bodies now have faster surgery speed. Autopsies also
count as dissections, however they're mutually exclusive.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[fc1471c818...](https://github.com/AnywayFarus/Skyrat-tg/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Sunday 2023-05-07 08:52:49 by SkyratBot

[MIRROR] Deadchat Announcement Variety Pack 1 [MDB IGNORE] (#20957)

* Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat.
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

* Deadchat Announcement Variety Pack 1

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [NemesisTheory/s2p](https://github.com/NemesisTheory/s2p)@[f95a86dad8...](https://github.com/NemesisTheory/s2p/commit/f95a86dad839d4989cf15cd90b0904a6f42eb4e2)
#### Sunday 2023-05-07 09:00:52 by NemesisTheory

DO YOU CROSS YOUR HEART WHEN YOU HOPE TO DIE?

ARE YOU SLEEPING DEEP IN THE HURRICANE?
IV'S IN THE ARM, FORGETTING TO FEEL
WE'RE CRAWLING ON ALL FOURS,
WILL YOU FALL ON THAT SWORD IN THE SECOND COMING?
YOU'RE GONNA TASTE THE ASH AND DUST,
'CAUSE THIS WORLD IS DYING IN OUR ARMS.

Now the wheels are turning,
What would you do, to stay alive, if the planet was burning?

You want to make your Hell a reality?
Black lungs for the young, if they dare to breathe (if they dare to breathe, woah-oh),
Sure sounds like heaven to me,
You gotta cut the roots, to kill the weeds
No place to go, if we don't believe (if we don't believe, woah-oh)
Good lord it's enough to plague a saint.

GIVE US A JUDAS STEER WE COULD DEIFY,
YEAH, WE ALL PRETEND WE'RE THE RENEGADES
SO WASH US AWAY, GARROTED BY HALO
TAKE A BOW 'CAUSE TIME, IS RUNNING OUT,
THERE'S NO DOUBT THAT THE END IS COMING
YOU'RE GONNA TASTE THE ASH,
AND YOU'RE GONNA TASTE THE DUST
'Cause this world is dying in our arms.

Now the wheels are turning,
What would you do, to stay alive, if the planet was burning?

You want to make your Hell a reality?
Black lungs for the young, if they dare to breathe (if they dare to breathe, woah-oh),
Sure sounds like heaven to me,
You gotta cut the roots, to kill the weeds
No place to go, if we don't believe (if we don't believe, woah-oh)
Good lord it's enough to plague a saint.

Good lord it's enough to plague a saint.

Post-love, post-truth,
Justice lays bound and black-bagged, ready for the guillotine
We can all plead guilty when they ask,
"WHERE WERE YOU WHEN THE GODS CLIPPED THE WINGS OF THE PHOENIX?"
THEY CLIPPED THE WINGS OF THE PHOENIX, OH!

WHEN WILL WE WRESTLE THE WORLD,
FROM THE FOOLS, AND THEIR GOLD,
AND THEIR FUCKING COVENANT? (We're done waiting)
WILL ENOUGH BE ENOUGH,
WHEN WE'RE HOLDING ON for dear life?

You want to make your Hell a reality?
Black lungs for the young, if they dare to breathe (if they dare to breathe, woah-oh),
Sure sounds like heaven to me,
You gotta cut the roots, to kill the weeds
No place to go, if we don't believe (if we don't believe, woah-oh)
Good lord it's enough to plague a saint.

It's enough to plague a saint,
It's enough to plague a saint,
It's enough to plague a saint.

OH!
UGH, WE CAN ALL PLEAD GUILTY WHEN THEY ASK,
"WHERE WERE YOU WHEN THE GODS CLIPPED THE WINGS OF THE PHOENIX?"

---
## [QuicheLorraine3600/StupidTestSlayerToolkit](https://github.com/QuicheLorraine3600/StupidTestSlayerToolkit)@[b8627a8d9b...](https://github.com/QuicheLorraine3600/StupidTestSlayerToolkit/commit/b8627a8d9b17db0fc931894f9a9b69d6d9370e18)
#### Sunday 2023-05-07 09:07:03 by Clément Moréna

🎉 Let the Stupid Test Slaying Begin! 🚀
With this first commit, we're launching our "Stupid Test Slayer Toolkit" into the world. This comprehensive set of resources and tips is designed to help students of all ages and levels prepare for, navigate, and conquer even the most ridiculous tests.

We believe that no test should stand in the way of your dreams and aspirations, and that with the right tools and mindset, anything is possible. From flashcards to study guides, mnemonic devices to mindfulness exercises, our toolkit has everything you need to succeed.

So let's get started! With the "Stupid Test Slayer Toolkit" at your side, you're unstoppable. Together, we'll slay those stupid tests and achieve greatness. 🎉🗡️💪

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[e1221c986f...](https://github.com/Time-Green/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Sunday 2023-05-07 09:16:49 by san7890

Chasm Hell On Icebox - 300 Active Turfs on Prod Moment (#74410)

## About The Pull Request

Spontaneous regressions introduced by #74359
(1e58c1875d9e2f48a306fe31a0626dbbb1990ff9).
```txt
 - Z-Level 2 has 150 active turf(s).
 - Z-Level 3 has 150 active turf(s).
 - Z-Level trait Ice Ruins Underground has 300 active turf(s).
 - Z-Level trait Mining has 300 active turf(s).
 - Z-Level trait Station has 300 active turf(s).
 - End of active turf list.
 ```

![image](https://user-images.githubusercontent.com/34697715/229213138-5a6a7a4f-edec-47ab-8def-ee4e4bddfe61.png)

Basically the lavaland ruin sucks dogshit and I had to do a lot of stuff to account for everything failing. There was even a moment where we were adding something to `flags_1` instead of `turf_flags` and that was also really bad to figure out.

![image](https://user-images.githubusercontent.com/34697715/229213428-63bb1f6e-6f88-4604-a3c6-e08e20cbfa7a.png)

i also had to add orange genturfs because it was really getting bad with all of the assertions we had to keep making, especially since stuff like this could also show up:

![image](https://user-images.githubusercontent.com/34697715/229213562-4a145453-5f90-4d05-b8cc-5c1beec2b0dd.png)

That's the prison in the red box, those are active turfs because a chasm scraped it away.

Sorry if this is hard to follow but I promise you everything in this is essential. I wish we didn't have to rely on turf flags as much as we do but this is a fix PR, not a refactor.
## Why It's Good For The Game

Even one active turf on IceBox ate up _three_ seconds of SSair's initialization every single time it was really fucking bad.

We haven't had to deal with chasms for about two years so there's a lot of mapping assertions we made since they just weren't a thing, but now they're back so lets do it properly.
## Changelog
:cl:
fix: The prison on IceBox should no longer leak air as often.
/:cl:

I have compiled this map about 30 times until active turfs stopped fucking happening and now I am content. This likely doesn't fix _everything_ because some stuff can still be hidden to me, and we still have PRs that need to be merged to reduce the amount of noise we're getting on prod.

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[0a1f7e8de2...](https://github.com/Time-Green/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Sunday 2023-05-07 09:16:49 by Hatterhat

Thrown containers splashing on mobs spill some contents on the floor (#74345)

## About The Pull Request
Spiritual continuation of tgstation/tgstation#74187.

![image](https://user-images.githubusercontent.com/31829017/228645705-5a32cc67-37e0-48d6-9e95-6006f455ed3c.png)
Reagent containers that splash their contents on people also splash the
floor - the amount that gets splashed on the floor is the amount that
missed the target.
### Mapping March

Ckey to receive rewards: N/A (it's not a mapping PR)

## Why It's Good For The Game
Splashing people with a molotov filled with Random Shit now also
splashes that Random Shit all around, making them slightly more spicy to
play around with. Unfortunately, I couldn't figure out how to make fuel
puddles ignite off of lit objects resting on top of them (there's no
item-level proc for hotspot exposure or something). If anyone wants to
advise me on how to make that happen, that'd be cool.

## Changelog
:cl:
add: Reagent containers that splash on people when thrown (e.g.
molotovs) now spill their contents on both target and turf. (This means
that throwing molotovs with enough fuel spills fuel puddles, throwing
beakers with acid spills acid on the floor, etc. etc.) Unfortunately,
molotovs still lack the ability to ignite their own spilled fuel, but
we'll get there one day.
/:cl:

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f3549a4aec...](https://github.com/tgstation/tgstation/commit/f3549a4aeca6701a2969a63b7d4034d5bc560cb6)
#### Sunday 2023-05-07 09:22:04 by Thunder12345

De-holes holy arrows (#75184)

## About The Pull Request

Covers the 2-pixel hole in the holy arrow sprite with 1 alpha pixels to
prevent unintentional missed clicks.

## Why It's Good For The Game

It's annoying and a bad experience to think you clicked on a sprite but
actually landed on a tiny transparent hole and clicked nothing or the
object below the one you wanted.

## Changelog
:cl:
image: Holy arrows are now 15% less holy (You can no longer click on the
2-pixel hole in the arrowhead and unintentionally click the object below
the arrow instead.)
/:cl:

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[1b5c0489a4...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/1b5c0489a4088dca925ab061a389d95005c95820)
#### Sunday 2023-05-07 10:54:00 by san7890

`ex_act()` will work on basic mobs again (lol) + Unit Test (#74953)

basically ex_act's implementation on basic mobs would call parent and
then react to it's value, this is presumably to do the first check about
space vine mutations and whatever. the problem is that the `/mob/living`
implementation would itself also call parent, and that would always
return null because `/atom/proc/ex_act` doesn't have a set return value.
So, this simply would _always_ early return, with ex_act presumably
*never* working on basic mobs for at least four months now.

I decided to then change up the return values for pretty much all
implementations of `ex_act()` since there was no rhyme or reason to
returning null/FALSE/TRUE, and documenting why it's like that.

Just to make sure I wasn't breaking anything doing this (at least on
base implementations), I wrote a unit test for all of the three major
physical types in game (objs, mobs, turfs) because i am a paranoid
fuckar. we should be good to go now though.
## Why It's Good For The Game

i noticed this because placing c4's on sargeant araneus wouldn't
actually damage it whatsoever. now it actually does the stated 30
damage, but araneus has like 250 health so it doesn't actually matter in
the long run. whatever at least it does the damn 30 now.

also adds a unit test for this specific case as well as a range of other
cases to ensure this stuff doesn't silently break in this way anymore

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[f2fd69a49a...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/f2fd69a49a7d9308eb695c0368163d2f63a53a54)
#### Sunday 2023-05-07 10:54:00 by ArcaneMusic

Minerals have been refactored so costs and minerals in items are now in terms of mineral defines. (#75052)

Ladies, Gentlemen, Gamers. You're probably wondering why I've called you
all here (through the automatic reviewer request system). So, mineral
balance! Mineral balance is less a balance and more of a nervous white
dude juggling spinning plates on a high-wire on his first day. The fact
it hasn't failed after going on this long is a miracle in and of itself.

This PR does not change mineral balance. What this does is moves over
every individual cost, both in crafting recipes attached to an object
over to a define based system. We have 3 defines:

`sheet_material_amount=2000` . Stock standard mineral sheet. This being
our central mineral unit, this is used for all costs 2000+.
`half_sheet_material_amount=1000` . Same as above, but using iron rods
as our inbetween for costs of 1000-1999.
`small_material_amount=100` . This hits 1-999. This covers... a
startlingly large amount of the codebase. It's feast or famine out here
in terms of mineral costs as a result, items are either sheets upon
sheets, or some fraction of small mats.

Shout out to riot darts for being the worst material cost in the game. I
will not elaborate.

Regardless, this has no functional change, but it sets the groundwork
for making future changes to material costs much, MUCH easier, and moves
over to a single, standardized set of units to help enforce coding
standards on new items, and will bring up lots of uncomfortable balance
questions down the line.

For now though, this serves as some rough boundaries on how items costs
are related, and will make adjusting these values easier going forward.

Except for foam darts.

I did round up foam darts.

Adjusting mineral balance on the macro scale will be as simple as
changing the aforementioned mineral defines, where the alternative is a
rats nest of magic number defines. ~~No seriously, 11.25 iron for a foam
dart are you kidding me what is the POINT WHY NOT JUST MAKE IT 11~~

Items individual numbers have not been adjusted yet, but we can
standardize how the conversation can be held and actually GET SOMEWHERE
on material balance as opposed to throwing our hands up or ignoring it
for another 10 years.

---
## [jmillikin/upstream__rules_rust](https://github.com/jmillikin/upstream__rules_rust)@[80f0eb488a...](https://github.com/jmillikin/upstream__rules_rust/commit/80f0eb488ab9cabc4920ac446478cbf2feedc3f3)
#### Sunday 2023-05-07 11:44:25 by scentini

Support for `no_std` mode (#1934)

Initial support for `no_std` mode.
This allows us to
1. Don't pass the whole standard library to compile actions that specify `no_std`
2. Conditionally select `crate_features` and `deps` based on whether `no_std` mode is used.
Currently the only supported modes are `off` and `alloc`, with a possibility to expand in the future.

The `no_std` support comes with the following caveats:
1. Targets in `exec` mode are still built with `std`; the logic here being that if a device has enough space to run bazel and rustc, std's presence would not be a problem. This also saves some additional transitions on `proc_macro`s (they need `std`), as they are built in `exec` mode.
2. Tests are still built with `std`, as `libtest` depends on `libstd`

There is quite an ugly hack to make us be able to `select` on the `no_std` flavor taking `exec` into account; I'm looking forward to the day where Bazel will expose better ways to inspect the cfg.

There is also one part I didn't manage to make work - having a `rust_test` that tests the `rust_shared_library` in `cc_common.link` mode; I got a link error for missing `__rg_alloc` & co. symbols, which should be present as we pass `--@rules_rust//rust/settings:experimental_use_global_allocator=True`. Unfortunately I could only spot this error on CI, and could not reproduce locally. I removed the test because the `rust_shared_library` is already tested via a `cc_test`. I will however give another shot at inspecting how my local setup differs from CI.

The `rust_binary` source code in `main.rs` was borrowed from https://github.com/jfarrell468/no_std_examples, big thanks to @jfarrell468 for letting me use it.

Co-authored-by: Krasimir Georgiev <krasimir@google.com>
Co-authored-by: UebelAndre <github@uebelandre.com>

---
## [Watermelon914/tgstation](https://github.com/Watermelon914/tgstation)@[551a09211b...](https://github.com/Watermelon914/tgstation/commit/551a09211b4091320ff871e78d93efa2775df6bc)
#### Sunday 2023-05-07 11:44:41 by carlarctg

Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool (#74744)

## About The Pull Request

Replaced the subspace amplifier in the Black Market Uplink's crafting
recipe with a signaller and a microlaser.

Added the Black Market Uplink to the maintenance loot pool.
## Why It's Good For The Game

The BMU is an _extremely_ rare device to find in rounds. It can quite
literally ONLY be found via the crafting recipe, and with how stupidly
bloated the crafting lists are, it isn't something many people know
about. All this means that a very unique and engaging gimmick item is
tragically extremely obscured.

To add to this, the recipe requires a _subspace amplifier_. These items
are UNBELIEVABLY rare - they need you to vend them from a techfab with
bluespace communication technology researched, which is fair to say is
not a common thing. Sometimes maps have them in tech storage, but even
then you have to break and enter which can be quite risky at times and
an annoying blockade the other times.

The black market items are not worth this much hassle. They are all
small cute gimmicky objects that do not heavily impact the round. By
making it not only easier to craft with common items, but also appear in
the maintenance loot pool, this will make assistants find out about it
more often, which can further incentivize them to utilize the **cargo
bounty system** to get enough money to buy their funny gadgets.

Another idea would be to make the uplink appear as a bounty item, which
would be a great way to tell players it exists and encourage them to mix
both systems together. The system for getting items is also
unnecessarily, miserably awful - your item either gets literally thrown
into space from a random direction, or it is teleported silently without
warning in 60 seconds onto a completely random place which can very much
include Security, Command, the Vault, or other high-security areas.
Needing to B&E into these areas to get your durathread vest is, uh. Not
worth it. However these aren't part of this PR, unless they're given the
A-OK. (also maybe make it cargo purchasable?)
## Changelog
:cl:
balance: Makes Black Market Uplinks more easily craftable, adds them to
uncommon maint loot pool
/:cl:

---
## [Watermelon914/tgstation](https://github.com/Watermelon914/tgstation)@[2778badd94...](https://github.com/Watermelon914/tgstation/commit/2778badd94fd9dbd958c09bcb66c8c5da9314783)
#### Sunday 2023-05-07 11:44:41 by necromanceranne

Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate (#74703)

## About The Pull Request

Nitrous Oxide, rather than directly subtracting blood volume per tick,
instead applies the anticoagulant trait ''TRAIT_BLOODY_MESS''. It shares
this with heparin.

However, unlike, heparin, coagulants like Sanguirite will remove the
trait and allow for continued clotting while the reagent is present,
neutering the nitrous oxide's anticoagulant effects (but not the other
parts)

Heparin, on the other hand, will purge Sanguirite while it is in you
system. You must remove the heparin before you can apply an
anticoagulant.

## Why It's Good For The Game

Nitrous Oxide, on top of being a knockout chem that causes you to
suffocate and become drowsy, just starts deleting blood rapidly. About
15 units of it, standard in a syringe, will kill you in about a minute,
but you'll be unconscious for most of it (you'll be at around 50%-60%
blood by the time it is out of your system, so as good as dead). It
doesn't matter that it metabolizes quickly either, since because it
isn't a toxin, it doesn't get purged by livers/improved livers, so you
will probably metabolize all of the chem that enters your system.

Blood is one of those 'hidden damage types', a bit like brain damage.
Once you start losing it _directly,_ you probably don't have a lot of
options to resolve it (unlike a bleed, which you do in various manners),
and the means of causing blood loss has been mostly pretty well
controlled as of late. Heparin directly interacts with wounds as a good
example.

Blood loss is also tied into oxyloss, which is another very mean damage
type in that it causes you to fall into unconsciousness at 50 damage, so
significantly more lethal than normal damage, kept in check by the fact
that breathing restores some of it. Nitrous oxide, you might note,
causes you to stop breathing.

It's cheaper to make than either heparin or lexorin, and since it isn't
a toxin like those chems, it is able to circumvent a few game mechanics
to simply just start killing you. It does the work of chloral hydrate,
lexorin and heparin while it has a remarkably easy recipe.

Following the example of how lexorin was pulled into line, and
consistency with heparin, I've made nitrous oxide an anticoagulant that
may or may not come into play as one. I think this is more up to date
with the state of toxins and chem warefare as a whole, and works with
the relative ease in making nitrous oxide. And it has been this way for
about 5 years, before we got wounds.

(did I mention that nitrous oxide is also an explosive if it gets hot
enough?)

## TL;DR

I think a chem with a pretty basic recipe shouldn't be doing the work of
5 other, more complicated, chemicals while also not being a toxin and
also not interacting with the wounds system or purity system whatsoever.
And being an explosive.

## Changelog
:cl:
balance: Nitrous oxide, the reagent, increases bleed rate from wounds
rather than directly subtracting blood. It can be counteracted using
coagulants (such as those in epipens).
balance: Heparin purges coagulants. You have to remove heparin from
someone's system before you can use coagulants.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [NemesisTheory/s2p](https://github.com/NemesisTheory/s2p)@[d4d8a9f0e0...](https://github.com/NemesisTheory/s2p/commit/d4d8a9f0e00d16899a2a2f3c2eb4570061bb446e)
#### Sunday 2023-05-07 12:02:48 by NemesisTheory

There's a rose that blooms, through the cracks in the concrete,

Staining the prison floor
There's a pilgrimage waiting, sat at the doorstep,
Rotting beneath the sun.

When there's nowhere left to hide, we'll be searching for a shortcut,
Ire and denial are as thick as thieves
Soon there'll be nothing left of me, nothing left of me
Don't forget to breathe, don't forget to breathe, don't forget to breathe.

Tell me how to coexist, when a fraction only wants war,
Hopelessly in love with our gritted teeth
Soon there'll be nothing left of me, nothing left of me
Don't forget to breathe, I forgot to breathe, and look who's on the throne now.

A dead heretic, with no storm left to weather,
Afraid to admit, it won't sustain the spirit
A new counterfeit, like flight without feathers,
Ready to submit, it won't sustain the spirit.

It won't sustain the spirit.

So we fall to our knees, and beg for reprieve, but,
It's almost time for the curtain call
The apostles will sing, and lead us from sin, but,
They hold all of our bones in their hands.

We all, swim against the tide until it puts us on the back foot,
Nothing's ever tasted half as good as grief
Soon there'll be nothing left of me, nothing left of me,
Don't forget to breathe, don't forget to breathe, don't forget to breathe.

'Cause I'm staring at a fist and it's asking if I want more,
Clarity will visit, but it's only brief
Soon there'll be nothing left of me, nothing left of me,
Don't forget to breathe, don't forget to breathe, don't forget to breathe.

A dead heretic, with no storm left to weather,
Afraid to admit, it won't sustain the spirit
A new counterfeit, like flight without feathers,
Ready to submit, it won't sustain the spirit.

It won't sustain the spirit,
It won't sustain the spirit,
It won't sustain the spirit,
It won't sustain the spirit.

---
## [hipe/tmx](https://github.com/hipe/tmx)@[1acd90469d...](https://github.com/hipe/tmx/commit/1acd90469d75bed90b7997d4c6d6bb97e666aa67)
#### Sunday 2023-05-07 12:49:15 by Mark Meves

upgrade(STM): Attempt to upgrade all packages (3, v, SEE)

Synopsis:
+ In order to troubleshoot what we're attempting in the next step
  after this, we attempted to upgrade all our packages. We approached
  this by removing *all* explicit version numbers from pubspec.yaml
  where possible. (We call it "autobleed", the imaginary service that
  automatically upgrades packages and looks at what breaks. This is
  a step towards that.
+ (Certainly, if an under-development package goes into production,
  it should *not* be on autobleed. But we are a long way away from that.)
+ It seems that this upgrade advanced sqlparser by one minor version
  which seems to have broken its attempts at parsing our code that comes
  as an example from google. This commit has a fix for that (more below).
+ (SEE) Our generated schema shows a new problem: We want the
  auto-increment behavior when doing CREATE; we don't know how to
  get that without passing NULL as the id; we don't know how to do
  that unless we make that field nullable; WHICH in turn has impact
  in how the 'CREATE TABLE' is generated which in turn may create the
  column as not the special sqlite magic "integer not null primary key"
  etc. What we suspect is the case is we need the CREATE TABLE magic
  from *before* we introduced this ID field as nullable (a bad workaround.
  we need to find the correct fix for this.)

Narrative:

OK so here's a story: I got a runtime error from something
"floor" related, when attempting to implement 'DELETE' (which is itself
a story)..

+ Do I learn to step-debug into vendor code?
+ Where are the dart files of a package stored locally?
+ What if I need to step-debug into a vendor's package?

I decided to "back up a step" and attempt to get all packages upgraded.
This seems to have revealed a bit of a dependency hell I'm in; but I
don't yet know enough to assess this.

What was unimaginable was that a query so simple could be messing up
their SQL parser. My query was simply:

    Select * from Like

Now, *I* see something suspicious there; but I left the SQL in there
EXACTLY as the demo had it.

Anyway, what it seems like happened is the "sqlparser" package
correctly made itself more strict like I recommended. I CORRECTLY
GUESSED THE FIX, but lordy that was close to being *really* annoying.

(times)
  11:44  (mark this event: gonna learn to stream results)
  16:36  we suspect some version hell is breaking how our
         queries got parsed

---
## [NemesisTheory/s2p](https://github.com/NemesisTheory/s2p)@[5039c7bd78...](https://github.com/NemesisTheory/s2p/commit/5039c7bd78d102b8c7ce98f9deb021d831676a5a)
#### Sunday 2023-05-07 13:51:44 by NemesisTheory

AN IRON FIST IN A VELVET GLOVE,

ANOTHER VULTURE POSING AS A DOVE
DO YOU HAVE NO SHAME? LOOK AT WHAT YOU'VE BECOME,
YOU ARE THE REASON WE ARE BITTER AND THEN SOME, BLEGH!

BITTER AND THEN SOME.

THEY SING OF SAVIOURS, WE SING OF SORROW,
BUT WE'RE STILL HOLDING ON, TO DEAR LIFE
YOU SOLD US ALL DOWN THE RIVER,
I HOPE YOU CHOKE ON THE VOWS THAT YOU FAILED TO DELIVER.

YOU SAID YOU'D CHANGE THE WORLD, BUT DEATH STILL FLIES EAST
THE BLIND LEAD THE BLIND, SO WE BOMB FOR PEACE.

GRAVEDIGGER, there's blood on your hands,
You built this empire on salt and sand
NOT ALL IS FAIR IN LOVE AND WAR,
HISTORY REPEATS, WE'VE SEEN THIS ALL BEFORE.

WE'VE GIVEN THE VAMPIRES,
THE KEYS TO THE BLOOD BANK, OH!

THEY SAY THE MORE THINGS CHANGE, THE MORE THEY STAY THE SAME,
WHILE THE LIARS LEECH, THE CROOKED PREACH
SO LIE THROUGH YOUR TEETH, LIKE LIKE YOU MEAN IT,
IT BEGGARS BELIEF, DO YOU REALLY THINK, THAT WE STILL FUCKING BELIEVE IT?

YOU FUCKING PARASITE, BLEGH!

THERE'S NO ROOM IN HERE, FOR AN HONEST MAN,
Only callous and cold hearts.

GRAVEDIGGER, there's blood on your hands,
You built this empire on salt and sand
NOT ALL IS FAIR, IN LOVE AND WAR,
HISTORY REPEATS, WE'VE SEEN THIS ALL BEFORE.

OPPRESSOR, you built this empire on salt and sand,
OPPRESSOR, you built this empire on salt and sand.

AN IRON FIST IN A VELVET GLOVE,
ANOTHER VULTURE POSING AS A DOVE
DO YOU HAVE NO SHAME? LOOK AT WHAT YOU'VE BECOME,
YOU ARE THE REASON WE ARE BITTER AND THEN SOME, BLEGH!

BITTER AND THEN SOME.

THEY SING OF SAVIOURS, WE SING OF SORROW,
BUT WE'RE STILL HOLDING ON, FOR DEAR LIFE.

---
## [Aerden/tgstation](https://github.com/Aerden/tgstation)@[c0ef4ba907...](https://github.com/Aerden/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Sunday 2023-05-07 14:09:12 by tralezab

Adds the Dark Matt-eor when you emag a stupid amount of meteor shields + lots of meteor file sorting + qol + dark matter singularity + dark matt-eor summoning final traitor objective (#74330)

## About The Pull Request

<details>
  <summary>Dark Matt-eor Image</summary>
  

![image](https://user-images.githubusercontent.com/40974010/228368755-34ae5f89-e1bb-498b-bbf8-a14ff4240dc0.png)

</details>

> A barely visible blur in the cosmic darkness, like a ghostly shadow on
a moonless night. A piercing howl in the vacuum of space, as if it were
tearing the fabric of reality. A twisted halo of light around it,
bending and breaking the rays of distant suns. A shower of quantum
sparks, flickering and fading in its wake. A dark matter meteor (dark
matt-eor) is a wonder to witness, and to dread.

> A sudden impact, like a hammer blow to the heart of the station. A
violent tremor, shaking and shattering the metal walls and windows. A
deafening roar, as the air rushes out of the breached hull. A blinding
flash, as the dark matter meteor unleashes its hidden energy. A tiny
black hole, forming and growing in the center of the station. A
relentless pull, dragging everything towards the abyss. A dark matter
meteor is incredibly deadly.

Emagging too many meteor shields will summon a dark matt-eor. This comes
with several warnings, and after awhile, warns the station that someone
is trying to summon a dark matteor.

The dark matt-eor itself is not that damaging in its impact, but drops a
singularity in its final resting place.

## Why It's Good For The Game

It's a new way to terrorize a round as an antagonist. Before, emagging a
lot of meteor shields would basically make meteor showers the only event
that can run, which is cool, but since constant meteor waves are going
to destroy the station, let's also throw in the mother of all meteors!

This also adds warnings to spamming emagging meteor shields, which imo
needs it. The round ends when someone spams emagged meteor shields, and
since they're meteor shields nobody is going to reasonably check on
them.

## Changelog
:cl:
add: The dark matt-eor
add: Summon a dark matt-eor final traitor objective
add: Dark matter singularity variant, which can't grow as big as a
regular singularity but hungers for blood
code: cleaned up/sorted meteor shield code, satellite control, and more
qol: added a lot of feedback to interacting with meteor shields
balance: emagging a lot of meteor shields warns the station, but
emagging enough of them summons a Dark Matt-eor.
/:cl:

---
## [Aerden/tgstation](https://github.com/Aerden/tgstation)@[ccef887efe...](https://github.com/Aerden/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Sunday 2023-05-07 14:09:12 by san7890

Lints Against Unmanaged Local Defines (#74333)

# MAINTAINER - USE THE BUTTON THAT SAYS "MERGE MASTER" THEN SET THE PR
TO AUTO-MERGE! IT'S MUCH EASIER FOR ME TO FIX THINGS BEFORE THEY SKEW
RATHER THAN AFTER THE FACT.

## About The Pull Request

Hey there,

This took a while to do, but here's the gist:

Python file now regexes every file in `/code` except for those that have
some valid reason to be tacking on more global defines. Some of those
reasons are simply just that I don't have the time right now (doing what
you see in this PR took a few hours) to refactor and parse what should
belong and what should be thrown out. For the time being though, this PR
will at least _halt_ people making the mistake of not `#undef`ing any
files they `#define` "locally", or within the scope of a file.

Most people forget to do this and this leads to a lot of mess later on
due to how many variables can be unmanaged on the global level. I've
made this mistake, you've made this mistake, it's a common thing. Let's
automatically check for it so it can be fixed no-stress.

Scenarios this PR corrects:

* Forgetting to undef a define but undeffing others.
* Not undeffing any defines in your file.
* Earmarking a define as a "file local" define, but not defining it.
* Having a define be a "file local" define, but having it be used
elsewhere.
* Having a "local" define not even be in the file that it only shows up
in.
* Having a completely unused define*

(* I kept some of these because they seemed important... Others were
junked.)
## Why It's Good For The Game

If you wanna use it across multiple files, no reason to not make it a
global define (maybe there's a few reasons but let's assume that this is
the 95% case).

Let me know if you don't like how I re-arranged some of the defines and
how you'd rather see it be implemented, and I'd be happy to do that.
This was mostly just "eh does it need it or not" sorta stuff.

I used a pretty cool way to detect if we should use the standardized
GitHub "error" output, you can see the results of that here
https://github.com/san7890/bruhstation/actions/runs/4549766579/jobs/8022186846#step:7:792
## Changelog
Nothing that really concerns players.

(I fixed up all this stuff using vscode, no regexes beyond what you see
in the python script. sorry downstreams)

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[2b2cb3dff6...](https://github.com/Striders13/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Sunday 2023-05-07 14:13:06 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [kewbish/ubccsss.org](https://github.com/kewbish/ubccsss.org)@[17535fd8bd...](https://github.com/kewbish/ubccsss.org/commit/17535fd8bd547ba27171b824bb6722646b30d237)
#### Sunday 2023-05-07 14:49:24 by csssbot

New review for CPSC 210 by ubcstudent2 (#443)

> The concepts in this course are useful. The course overall is good,
but I have a big issue with PraireLearn just makes everything so much
harder for no reason. In this class we use a system called PrairieLearn
for exams and practice exams. To put it frankly, this system is
horrible. First of all, why are we writing code in a web browser? This
course should learn from its pre-req CPSC 110 and move onto programming
in an IDE for exams and all practices. Also it should really have
autograders. Trying to match our answers with the solution when the
solution can be often coded in maybe ways is horrible.

For practice problems, you can only answer the question once, if you
want to try again, you have to creat another instance of the whole
practice set. The text editor is bulky and annoying. Exams seriously
tests more on predicting what the question writer wants. It is also very
hard to perfect grades, because of multiple choice. You can easily get 0
on a question if you just miss a few details.

PraireLearn randomizes the order of answer choices for some reason.
Consider this arbitrary case , if the question involves 3 variables,
usually the question would list the answer choices (1 1), (1 2), (2, 1),
(2, 2), (3, 1), (3, 2) or in some other order. With the order randomized
it could be (2, 2), (1 2), (1 1), (3, 1) , (2, 1), (3, 2). Which messes
up the flow of natural problem solving especially when the answer
choices are full sentences and you need to pick out which parts are
different.

PraireLearn randomizes variable names. Again, this makes every
unnecessarily harder for no reason. They love using arbitrary names with
no meaning at all like "smurf", "lorem", "ipsum." Again, you have to
look back and forth to the question. Even if they just used random
everyday words, it would make it easier.

The questions are just not that clear. If you have a slightly different
interpretation you can expect a maximum of 50% on that question.

Overall the course material is very very easy, but the PraireLearn
system just suck. 0/10. It adds so much extra resistance to the
otherwise very easy course material. CPSC 210 can easily be a 3 credit
course. Also its hard to wrap my head around how a "second year"
computer science course at "a good" university has so much overlap with
Programming 10, 11, 12 in highschools.

>
> Difficulty: 2/5
> Quality: 2/5
> <cite><a href=''>ubcstudent2</a>, Apr 27 2023, course taken during
2022W1</cite>
<details><summary>View YAML for new review</summary>
<pre>
  - author: ubcstudent2
    authorLink: 
    date: 2023-04-27
    review: |
The concepts in this course are useful. The course overall is good, but
I have a big issue with PraireLearn just makes everything so much harder
for no reason. In this class we use a system called PrairieLearn for
exams and practice exams. To put it frankly, this system is horrible.
First of all, why are we writing code in a web browser? This course
should learn from its pre-req CPSC 110 and move onto programming in an
IDE for exams and all practices. Also it should really have autograders.
Trying to match our answers with the solution when the solution can be
often coded in maybe ways is horrible.
      
For practice problems, you can only answer the question once, if you
want to try again, you have to creat another instance of the whole
practice set. The text editor is bulky and annoying. Exams seriously
tests more on predicting what the question writer wants. It is also very
hard to perfect grades, because of multiple choice. You can easily get 0
on a question if you just miss a few details.
      
PraireLearn randomizes the order of answer choices for some reason.
Consider this arbitrary case , if the question involves 3 variables,
usually the question would list the answer choices (1 1), (1 2), (2, 1),
(2, 2), (3, 1), (3, 2) or in some other order. With the order randomized
it could be (2, 2), (1 2), (1 1), (3, 1) , (2, 1), (3, 2). Which messes
up the flow of natural problem solving especially when the answer
choices are full sentences and you need to pick out which parts are
different.
      
PraireLearn randomizes variable names. Again, this makes every
unnecessarily harder for no reason. They love using arbitrary names with
no meaning at all like "smurf", "lorem", "ipsum." Again, you have to
look back and forth to the question. Even if they just used random
everyday words, it would make it easier.
      
The questions are just not that clear. If you have a slightly different
interpretation you can expect a maximum of 50% on that question.
      
Overall the course material is very very easy, but the PraireLearn
system just suck. 0/10. It adds so much extra resistance to the
otherwise very easy course material. CPSC 210 can easily be a 3 credit
course. Also its hard to wrap my head around how a "second year"
computer science course at "a good" university has so much overlap with
Programming 10, 11, 12 in highschools.
      
    difficulty: 2
    quality: 2
    sessionTaken: 2022W1

<pre>
</details>This is an auto-generated PR made using:
https://github.com/ubccsss/course-review-worker

---
## [umut-er/pool-for-physicists-only](https://github.com/umut-er/pool-for-physicists-only)@[42c03f6a75...](https://github.com/umut-er/pool-for-physicists-only/commit/42c03f6a75d001c33d4dc62656189a8c26b20af2)
#### Sunday 2023-05-07 15:27:55 by Umut Utku ERŞAHİNCE

fix: now implementing the complicated ball-cushion formula.
Several hours of work (mostly debugging) done, several more to go! Proceed with caution if you want to change these stuff!
There is an issue where we can't detect some collisions. This is in my opinion not a bug in the implementation. Our approach needs to change to fix this. Don't know how commonly this happens or whether it will affect regular user experience. Playtesting is required after pockets are implemented and game is operational.

---
## [jnutt367/psalms](https://github.com/jnutt367/psalms)@[9ee1ec4517...](https://github.com/jnutt367/psalms/commit/9ee1ec45174e83abba45b6ceda6a6896b6ac440f)
#### Sunday 2023-05-07 15:36:21 by Jason Nutt (He/Him) Christian Developer/Creator

Update index.js

For the director of music. According to gittith.[b] A psalm of David.
1 Lord, our Lord,
    how majestic is your name in all the earth!

You have set your glory
    in the heavens.
2 Through the praise of children and infants
    you have established a stronghold against your enemies,
    to silence the foe and the avenger.
3 When I consider your heavens,
    the work of your fingers,
the moon and the stars,
    which you have set in place,
4 what is mankind that you are mindful of them,
    human beings that you care for them?[c]

5 You have made them[d] a little lower than the angels[e]
    and crowned them[f] with glory and honor.
6 You made them rulers over the works of your hands;
    you put everything under their[g] feet:
7 all flocks and herds,
    and the animals of the wild,
8 the birds in the sky,
    and the fish in the sea,
    all that swim the paths of the seas.

9 Lord, our Lord,
    how majestic is your name in all the earth!

---
## [gilramot/Rich-Presence-U-DB](https://github.com/gilramot/Rich-Presence-U-DB)@[2cf4f40e9a...](https://github.com/gilramot/Rich-Presence-U-DB/commit/2cf4f40e9a337a60cbdad571c97d4c12202aa24b)
#### Sunday 2023-05-07 15:42:33 by ninstar

+32 New Nintendo Switch titles

Bayonetta Origins: Cereza and the Lost Demon
Blaster Master Zero
Blaster Master Zero 2
Blaster Master Zero 3
Chocobo GP
Freedom Planet
FUZE Player
FUZE4 Nintendo Switch
GRIS
Guacamelee! 2
Guacamelee! Super Turbo Championship Edition
Hotline Miami Collection
Ittle Dew
Ittle Dew 2+
KLONOA Phantasy Reverie Series
Octopath Traveler II
Resident Evil 0
Resident Evil 4
Resident Evil Revelations
Resident Evil Revelations 2
River City Girls
River City Girls 2
River City Girls Zero
RPG Maker MV
RPG Maker MV Player
SAMURAI SHODOWN
Shovel Knight Dig
Shovel Knight Pocket Dungeon
Super Chariot
Superliminal
The Binding of Isaac: Afterbirth+
UNO

---
## [gilramot/Rich-Presence-U-DB](https://github.com/gilramot/Rich-Presence-U-DB)@[f42a3a1ef5...](https://github.com/gilramot/Rich-Presence-U-DB/commit/f42a3a1ef58eac7176a9eb618ecc837b53508b82)
#### Sunday 2023-05-07 15:42:33 by ninstar

+41 New Nintendo Switch titles

Advance Wars 1+2: Re-Boot Camp
Atelier Ryza 3: Alchemist of the End & the Secret Key
Chained Echoes
Dead Cells
Digimon Survive
Disney Dreamlight Valley
FINAL FANTASY
FINAL FANTASY II
FINAL FANTASY III
FINAL FANTASY IV
FINAL FANTASY V
FINAL FANTASY VI
GUILTY GEAR
GUILTY GEAR XX ACCENT CORE PLUS R
Gunman Clive HD Collection
It Takes Two
Katana ZERO
Kaze and the Wild Masks
KINGDOM HEARTS Melody of Memory
Minecraft Legends
MLB The Show 23
Neon White
Ninjin: Clash of Carrots
Pirate Pop Plus
Puyo Puyo Tetris 2
Rain World
Rogue Legacy
Rogue Legacy 2
Spelunky
Spelunky 2
STAR WARS Republic Commando
Super Meat Boy
Super Meat Boy Forever
Super Punch Patrol
Temtem
Tetris® Effect: Connected
The Legend of Heroes: Trails to Azure
The Messenger
TowerFall
Ultimate Chicken Horse
Wolfstride

---
## [TerraFirmaCraft/TerraFirmaCraft](https://github.com/TerraFirmaCraft/TerraFirmaCraft)@[7f26f8da15...](https://github.com/TerraFirmaCraft/TerraFirmaCraft/commit/7f26f8da152642c5a9856a254b5dac4bb015d9a8)
#### Sunday 2023-05-07 16:21:53 by AlcatrazEscapee

I swear to everloving gods above and below this block item placement code is going to be the death of me, it's going to drive me absolutely and completely out of my mind. Every little line, little bug, every tiny little problem and it's never ending, I feel like I might go berserk. And, they're coming to take me away, haha, to the funny farm, where life is beautiful all the time and I'll be happy to see those nice young men in their clean white coats and they're coming to take me away, haha.

---
## [EduardoMunozGomez/wagic](https://github.com/EduardoMunozGomez/wagic)@[273d666bcc...](https://github.com/EduardoMunozGomez/wagic/commit/273d666bcce8d7cf360a869e2f288c5843fbb55d)
#### Sunday 2023-05-07 16:29:35 by Eduardo MG

New cards from MOC, MOM

March of the Machine Commander (MOC)
March of the Machine (MOM)
A few others from BRO and ONE
Some old auras that get sacrificed at end of turn if you cast them as if they had flash
fixed Fire Prophecy
NEW:
Umori, the Collector
Rootwire Amalgam
Steel Seraph
Tyrranax Rex
Paladin of Predation
Axgard Artisan
Zephyr Winder
Phyrexian Pegasus
Orthion, Hero of Lavabrink
Surrak and Goreclaw
Angelic Intervention
Pile On
Terror of Towashi
Interdisciplinary Mascot
Fertilid's Favor
Vengeant Earth
Sidar Jabari of Zhalfir
Moira and Teshar
Shalai and Hallar
Vodalian Wave-Knight
Bitterthorn, Nissa's Animus
Herald of Hoofbeats
Chivalric Alliance
Darksteel Splicer
Mistmeadow Vanisher
Death-Greeter's Champion
Hedron Detonator
Pain Distributor
Locthwain Lancer
Schema Thief
Exsanguinator Cavalry
Nesting Dovehawk
Filigree Vector
Conjurer's Mantle
Infernal Sovereign
Firemane Commando
Goro-Goro and Satoru
Katilda and Lier
Slimefoot and Squee
Soar
Armor of Thorns
Grave Servitude
Lightning Reflexes
Spider Climb
Parapet
Mystic Veil
Relic Ward
Titania, Voice of Gaea
Titania, Gaea Incarnate
Professional Face-Breaker
Oracle's Vault
Volcanic Spite

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[93294a1291...](https://github.com/re621/dnpcache/commit/93294a129156976b7c66c26122e876549e178a34)
#### Sunday 2023-05-07 16:30:50 by bitWolfy

Remove 1094 artists from the DNP list.

Removed: alradeck, asuka_kurehito, waynekan, lhacedor, dativyrose, digitallis, nosylvsforwork, lacrimale, kaitzuwu, ihoundr, elranno, doublepopsicle, gaturo, aquariusfox, mpcx, kattalu, lintu, goobysart, lemonlycan, dylbun, fxscreamer, nt6969, lewdliege, reallyhighriolu, melbaka, saint_lum, kivaaa66, kivalewds, kazoko_(artist), barachaser, shadowthelastalpha, teke, crittermatic, ribboncable, domasarts, ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, peshky, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, verdantphysician, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [OneAsianTortoise/tgstation](https://github.com/OneAsianTortoise/tgstation)@[912e843f53...](https://github.com/OneAsianTortoise/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Sunday 2023-05-07 16:39:24 by san7890

Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:


![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.


![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

---
## [Omar-HeshamR/first_pr_evals](https://github.com/Omar-HeshamR/first_pr_evals)@[ab5f7b2a89...](https://github.com/Omar-HeshamR/first_pr_evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Sunday 2023-05-07 17:01:07 by oscar-king

Counting bigrams in sentences (#302)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [Omar-HeshamR/first_pr_evals](https://github.com/Omar-HeshamR/first_pr_evals)@[b170a21cf3...](https://github.com/Omar-HeshamR/first_pr_evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Sunday 2023-05-07 17:01:07 by Sam Ennis

Computer Science Theory (#83)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [Omar-HeshamR/first_pr_evals](https://github.com/Omar-HeshamR/first_pr_evals)@[b5da073c21...](https://github.com/Omar-HeshamR/first_pr_evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Sunday 2023-05-07 17:01:07 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [RickDB/PlexAniSync-Custom-Mappings](https://github.com/RickDB/PlexAniSync-Custom-Mappings)@[827f6488b5...](https://github.com/RickDB/PlexAniSync-Custom-Mappings/commit/827f6488b54179c5e3d8c4f21b9ce8a1ff8a82c5)
#### Sunday 2023-05-07 18:15:50 by Soitora

Add multiple series

Bakuman
Black Lagoon
Classroom of the Elite
Ergo Proxy
Fena: Pirate Princess
Frieren
Fullmetal Alchemist & Brotherhood
Jujutsu Kaisen
Kaiju No. 8
Komi Can't Communicate
MASHLE
Monogatari
My Dress-Up Darling
Rent-a-Girlfriend
Skip and Loafer
Mato Seihei no Slave
Steins;Gate & 0
The Promised Neverland
Tokyo Revengers

---
## [Kreanto-org/kreanto](https://github.com/Kreanto-org/kreanto)@[cb8e533bd5...](https://github.com/Kreanto-org/kreanto/commit/cb8e533bd55f664402bc373a93c13c15c9433ac2)
#### Sunday 2023-05-07 18:17:28 by SantiagoVira

go to way too much trouble to make a cool animation in html god damn git shut up i will make my commit messages as long as I want fuck u

---
## [Nova-Kernels/kernel_xiaomi_mt6785](https://github.com/Nova-Kernels/kernel_xiaomi_mt6785)@[5fe9ec77a8...](https://github.com/Nova-Kernels/kernel_xiaomi_mt6785/commit/5fe9ec77a872d3e56487d93fae408e1d4c71419c)
#### Sunday 2023-05-07 18:35:10 by Peter Zijlstra

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
## [smxi/inxi](https://github.com/smxi/inxi)@[ed7049fcc1...](https://github.com/smxi/inxi/commit/ed7049fcc14fd5a1bb7e01b9674ad4c64e90cefa)
#### Sunday 2023-05-07 19:01:16 by Harald Hope

Completion of the audio fixes and improvements of 3.3.26. Added less common
sound servers like EsounD and aRts, and made state reports more accurate for
ALSA.

Major USB code and data upgrades/refactors. The USB changes prepare inxi for USB
4, and adds lanes and Si/IEC speeds to the report. It is important to determine
what USB mode you are running in with 3.x and 4. These changes conform more
closely to how the USB consortium wants USB speeds refered to.

With more robust USB data, this data now appears in a similar form as pcie: data
for Devices, -A, -E, -G, -N, and for -D drives, as usb: plus rev, speed, lanes,
mode, with the -xx/-a options, like pcie. This has been a long standing
oversight and weakness of inxi USB and Device data, but now the two are fully
integrated, including for drives, which was quite tricky to get working.

Added netpkg and Zenwalk support to packages and repos. Also added repos support
for sbopkg and slpkg, and updated package tools for Slackware.

And more distros added to system base feature, and a few more for main ID.

Improved --recommends report quite a bit, now it's more granular for missing
packages and package manager reports, and also fixed a long standing missing
current shell + version issue. Added the final package manager type, pkgtool
(Slackware), that will be supported, which makes for 4, which is enough. Note
that other package managers can be added following the documentation
instructions for packagers, but this is enough for out of the box pm handling.

Fixed a long standing oddity with how free / /proc/meminfo report MemTotal vs
the actual physical RAM. I believe this issue also showed with GPU assigned RAM,
but now for all but short form, shows Memory/RAM: available: ... used: ...

--------------------------------------------------------------------------------
SPECIAL THANKS:

1. To the Slackware people at linuxquestions.org forums, who helped, again, on
this audio feature, even finding current or not too old systems that use some of
the new / old audio servers (EsoundD) running in the wild, which I never
expected to see. And also for exposing some weak spots in the USB advanced
logic, and helping with the sbopkg and slpkg repo logic and tools reports.

2. To the Manjaro forum users, for providing cases that show where inxi can be
improved. The audio server/api issue, the current USB 3/4 upgrade, were
initiated by threads pointing to things that could be improved in inxi. So I
guess the real thanks are for using inxi enough to trigger cases that show where
it's weak or can be better. Note that this requires that I follow roughly their
forums, however I only look at threads that seem like they might be of general
interest, or which suggest a possible weak spot in inxi, and I don't follow them
consistently. More reliable is to file github issues, since I will always see
those.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. DesktopData: at one point, BunsenLabs Debian OpenBox had XDG_CURRENT_DESKTOP
set to XFCE, which it isn't, but inxi can't work around such hacks, plus I don't
even know if Bunsen is around anymore anyway.

2. DesktopData: CODE 1 reminds us that the time to depend on x tools like xprop
for anything re desktop/wm detections is fast drawing to a close, true Wayland
will not have xprop, unless it's running on xwayland, which is not something
that should be relied on. Maybe recheck Moksha/Enlightenment which depend on
xprop for version detection.

The list of xprop detected wm/desktops in get_env_xprop_misc_data() is almost
all X only wm/desktops, so those should be safe unless one of them decides to
work on a wayland comositor.

3. BSD: ongoing weaknesses in BSD data sources make maintaining feature parity
impossible, but I am trying to get the BSD data as clean and consistent as
possible. I wish this were not the case, but the fact is, /sys is expanding and
creating excellent and reliable data sources with every major Linux kernel
update, and so far nothing comparable has appeared in the BSDs. This is just
reality, it's not a condemnation, but something like the /proc then /sys file
systems are an excellent idea, well worth emulating.

4. For the RAM available/total clarification, there's a slight issue because
free/meminfo show MemAvailable as Free for use RAM, but dmesg shows available
meaning what was available to the system during boot, minus the reserved
percentage. Since we needed one term, available to System offers the closest
in terms of technical precision without being too verbose. Technically available
in this context means: total physical minus 'kernel code' minus 'reserved'.

--------------------------------------------------------------------------------
BUGS:

1. CheckRecommends: See Fix 6b, more or less a bug, but really just a fix.

2. AUDIO: for USB devices, put extra data into row 0, no matter which row the
USB device is. This led to the extra data for USB being assigned to the wrong
row. Sigh.

3. OptionsHandler: When show{'ram'} was set, for bsd, set use{'bsd-raid'}, which
makes both show raid and ram fail for BSD. Oops. User mode RAM data only seen in
OpenBSD so far. This made loading $dboot{'ram'} fail, and any raid as well,
sigh, unless -m was also tripped.

--------------------------------------------------------------------------------
FIXES:

1. DistroData: typo for Arch base: was ctios, was supposed to be ctlos.

2a. DesktopData: found case where xprop -root not present (Void Linux), so xfce
test failed. Split to new function dedicated to xfce detection that doesn't use
xprop data. Also, XFCE is working on their Wayland version, which would in
theory not even have xprop by default.

Also, the base version number test for xfce depended on xprop, but
xprop doesn't even have that xfce version data anymore, so just checking if
xfce(4|5|)-panel exist and assigning primary version based on that test.

2b. DesktopData: Also see See CODE 1a,1b for further xprop and test fixes that
could have led to false positive or negative test conditions for the items that
used xprop tests. These tests are all xprop agnostic now, if it's there, they
will use it, if not, do the best they can.

3. PackageData: fixed legacy dpkg-query, old version did not support -f shortcut
for --showformat. This made dpkg package listing fail.

4a. GRAPHICS: Added legacy XFree86.0.log to X log path detection, that was an
oversight. Also added legacy module syntax _drv.o (not _drv.so). This gets X
driver data now for very old systems.

4b. GRAPHICS: fixed corner case where no x driver data, running as root, was not
supposed to show 'note: X driver n/a' message, that was a holdover from before
driver output was cleaned up and driver: N/A shows when no drivers at all found.
Just forgot to remove it when doing recent updates in the driver section, maybe?

5. REPOS/PackageData: For netpkg Zenwalk Slackware systems, showed only slackpkg
repo data, empty, and showed the Slackware pm, not netpkg for pm. See
Enhancements 5, 6.

6. REPOS: removed slapt_get file /etc/slapt-get/pubring.kbx, that's not a repo
file. Thanks chrisreturn for pointing that out.

7a. CheckRecommends: See also CODE 6. Fixed case where > 1 package manager is
detected on system, now lists them one by one for detected, and shows package
install options as well. Before only picked first detected, which could lead
to wrong results for Missing Package lists.

7b. CheckRecommends: Fixed glitch, forgot to update the current shell/version
when ShellData was refactored, this led to no current shell + version showing
up in recommends core tools report.

8. RAM: fixed speed_mapper string match to allow for older syntaxes. This is as
far as known OpenBSD only, from dboot data. Matches then converts PC2700 to
PC-2700 which then allows for mapping.

9. RAM/PROCESSES/INFO/SHORT: Finally tracked down a long time oddity, where for
example:
 RAM: total: 31.28 GiB
does not match 32 GiB physical installed. This is because that is the total
available after kernel and system reserved RAM is deducted, and in some cases,
GPU allocated RAM. There are also corner cases where the listed amount can be
less due to physical RAM damage, but that's uncommon.

Added explanation of why it's different, and what available is referring to in
man -m/--memory.

Changed -m, -tm to show:

System RAM: available: 31.28 GiB used 26.23 GiB (83.9%)

and -I to show:

Memory: available: 31.28 GiB used 26.23 GiB (83.9%)

You can get the 'reserved' and 'kernel code' data from dmesg, but since Debian
made that root/sudo tool, can't count on being able to parse that out of dmesg,
plus you can never count no dmesg anyway since it can get overwritten by kernel
oops or wonky device etc. inxi doesn't use dmesg data for Linux for this reason.

... [    0.000000] Memory: 32784756K/33435864K available (10252K kernel code,
1243K rwdata, 3324K rodata, 1584K init, 2280K bss, 651108K reserved, 0K
cma-reserved)

Also removed Raspberry Pi video RAM added back in to total now that it's clear
it's what is available. This may also make systems with GPU using system RAM
more correct.

9. SENSORS: sensors /sys tried to create concatenated string with $unit $value
but these are not necessarily defined, that needed to be protected with defined
tests.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1a. AUDIO: JACK: added helper nsmd (new session manager), and its recommended
gui agordejo. That's the drop in replacement for non-session-manager, the dev of
which apparently lost interest in that project. But the ID method will work fine
for for either, since both ran as nsmd.

1b. AUDIO: PULSE: added pulseaudio-alsa plugin support for helpers. This is like
pipewire-alsa plugin, just alsa config file. Only seen in Arch Linux so far, but
if others use similar paths for the glob pattern, they will also work fine.

Also added pulseaudio-esound-compat plugin, which is easier to detect with
/usr/bin/esdcompat.

Also added paman, pulseaudio manager.

1c. AUDIO: ESOUND,ARTS: added legacy esd (EsounD aka: Enlightened Sound Daemon)
and aRts sound server support, with basic help/tools. These are quite old, but
are still occasionally seen in the wild on newer systems, surprisingly enough.

1d. AUDIO: ALSA: added alsactl to alsa tools. Missed that one, it's an /sbin
type utility.

1e. AUDIO: ALSA: First try at ALSA compiled in but inactive report,  previously
depended on active only state of the API. Now uses compiled in SND_ kernel
switch using the /boot/config-[kernel] file, which is a big expensive parse but
only will activate on Linux kernels with no /proc/asound present. This fallback
fails if kernel config file not present: /boot/config-$(uname -r).

1f. AUDIO: OSS: added tool ossctl.

1g. AUDIO: NAS: added helper: audiooss which is an OSS compat layer.

2a. DistroData: added Arch base distros: ArchEX, Bridge Linux, Condres OS,
Feliz, LiriOS, Magpie, Namib, Porteus, RevengeOS, SalientOS, VeltOS.

None of these are verified. Some don't exist anymore.
Source: https://www.slant.co/topics/7603/~arch-linux-based-distributions

2b. DistroData: added ubuntu lunar 23-4 release id.

2c. DistroData: added porteux, added porteux, zenwalk to slackware systembase

3. DesktopData/GRAPHICS: added Smithay Wayland compositor. Not verified.

4a. UsbData/UsbItem: added USB lanes (-Jxx) and mode (-Ja), to add more useful
data about USB revision and mode names the USB group has created. Otherwise it's
too difficult to try to explain it. Note that -Jxx lanes follows other inxi
items that show PCIe lanes as an -xx item to try to keep it consistent.

This also consolidates the bsd and linux data sources, see CODE 5.

Note modes and lanes are Linux only because the revision number, lanes, and
speed used to determine mode are only natively available in Linux as actual
internal data values. If this changes BSD support will be added in the future.

The BSD rev and speed data is synthesized completely by inxi using some string
values, and thus is not reliable, which means that pretending inxi can get this
granular with data that is not coming directly from the system itself is
probably not a good idea.

Following wikipedia mode names: https://en.wikipedia.org/wiki/USB4

These are the known possible combinations:
rev: 1.0 mode: 1.0 lanes: 1 speed: 1.5 Mbps
rev: 1.1 mode: 1.0 lanes: 1 speed: 1.5 Mbps
rev: 1.1 mode: 1.1 lanes: 1 speed: 12 Mbps
rev: 2.0 mode: 1.0 lanes: 1 speed: 1.5 Mbps
rev: 2.0 mode: 1.1 lanes: 1 speed: 12 Mbps
rev: 2.0 mode: 2.0 lanes: 1 speed: 480 Mbps
rev: 2.1 mode: 2.0 lanes: 1 speed: 480 Mbps
rev: 3.0 mode: 3.2 gen-1x1 lanes: 1 speed:  5 Gbps
rev: 3.0 mode: 3.2 gen-1x2 lanes: 2 speed: 10 Gbps
rev: 3.1 mode: 3.2 gen-1x1 lanes: 1 speed:  5 Gbps
rev: 3.1 mode: 3.2 gen-1x2 lanes: 2 speed: 10 Gbps
rev: 3.1 mode: 3.2 gen-2x2 lanes: 2 speed: 20 Gbps [seen this case]
rev: 3.2 mode: 3.2 gen-1x1 lanes: 1 speed:  5 Gbps [wrong rev: seen this case]
rev: 3.2 mode: 3.2 gen-1x2 lanes: 2 speed: 10 Gbps [wrong rev: possible case]
rev: 3.2 mode: 3.2 gen-2x1 lanes: 1 speed: 10 Gbps
rev: 3.2 mode: 3.2 gen-2x2 lanes: 2 speed: 20 Gbps
rev: 3.2 mode: 4-v1 gen-3x2 lanes: 2 speed: 40 Gbps [not seen, but possible]
rev: 4 mode: 4-v1 gen-2x1 lanes; 1 speed: 10 Gbps
rev: 4 mode: 4-v1 gen-2x2 lanes: 2 speed: 20 Gbps
rev: 4 mode: 4-v1 gen-3x1 lanes: 1 speed: 20 Gbps
rev: 4 mode: 4-v2 gen-3x2 lanes: 2 speed: 40 Gbps
rev: 4 mode: 4-v2 gen-4x1 lanes: 1 speed: 40 Gbps
rev: 4 mode: 4-v2 gen-4x2 lanes: 2 speed: 80 Gbps
rev: 4 mode: 4-v2 gen-4x3-asymmetric lanes: 3 up, 1 down speed:120 Gbps

I believe 120Gbps takes the 2 lanes of tx/rx and converts 2 rx lanes to tx so
the entire lane is dedicated to transmit. and the third lane is dedicated to rx.

Includes error message for unknown usb 3/4 rev/speed match combos. These can be
bad hardware self reporting or unknown other issues.

4b. USB: Added Si/IEC speeds (base 2, base 10). -Ja triggers extra IEC, base 2
Bytes (xxx [MG]iB/s). -Jx triggers basic standard Si xxx [MG]b/s base 10 bits.

5a. PackageData: added netpkg as package tool. This stores data in same location
as slackpkg, but assume if exists directory /var/netpkg, then the system is
using netpkg as pm, not slackpkg.

5b. PackageData: added Slackware sbopkg, sboui as tools for pkgtool and netpkg.

6a. REPOS: added netpkg (Zenwalk Slackware based pm) repo report.

6b. REPOS: added sbopkg basic repo report. This handles both value syntax types,
as well as the ability of /root config file to overwrite /etc config repo.

6c. REPOS: added slpkg repo report. This handles their old and newer syntax.

7a. CheckRecommends: For Slackware users, added pkgtool missing package name,
also will use netpkg so hopefully Zenwalk uses same package names.

7b. CheckRecommends: Added radeon to kernel modules checks.

8. AUDIO/BLUETOOTH/DRIVES/GRAPHICS/NETWORK: For USB, -[ADEGN]xx adds rev, speed,
lanes. -[ADEGN]a adds mode.

9. RAM: Updated RAM PC DDR in speed_mapper(), which is as far as I know only
used by OpenBSD, which allows for MT/s speeds as non-root user, which is nice.
That list hadn't been updated in a long time, so filled out DDR 1-5 PCx-yyyy
ids.

--------------------------------------------------------------------------------
CHANGES:

1a. USB: For -Jxy1, speed is now a child of rev: parent. This goes along with
mode: and lanes: being children of rev:. This follows how USB consortium wants
to refer to USB revisions now: by speed, lanes, and modes, the latter being the
technical term, the speed being the marketing term.

1b. USB: If no speed data found, show N/A. This should almost never happen
except for very old Linux and rarely with BSD.

1c. USB: Device type is lower cased except for abbreviations (type-C, HID). This
makes it more consistent as a value.

1d. USB: Show basic Si speed with -Jx, and adds new IEC speed with -Ja.

2. CheckRecommends: See ENHANCEMENT, CODE 6. Now showing row by row package
managers and missing packages, by package manager(s).

3. DRIVES: Changed long standing redundant use of 'type':
type: USB ... type: HDD
to:
type: USB ... tech: HDD
'tech:' means the technology used, HDD, SDD, and if we can ever figure out how
to detect it, Hybrid Hard Drive (HHD),

4. AUDIO/BLUETOOTH/DRIVES/GRAPHIC/NETWORK: moved 'type: USB' pair to after
driver for -A/-E/-G/-N, which allows it to be the parent of the new USB data
block. Negative is it moves it a bit further back in the line.

For Drives, it moves it from after /dev.. maj-min to after block-size, However,
with -D/-Dx, it's last in the line, which is nice. This is the only way I could
find to make it more consistent across all possible USB device/drive type
reports.

5. INFO/RAM/PROCESSES: Changed -I:

Memory: [total] used:
to:
Memory: available: [total] used:

Changed -tm/-m to be consistent:

Memory: RAM: total: .. used..
to:
Memory: System RAM: available: ... used:..

This corrects a long standing inaccuracy where MemTotal is not actually the full
system RAM, but is the RAM minus reserved stuff for system and kernel, and GPU
memory in some cases.

--------------------------------------------------------------------------------
DOCUMENTATION:

1a. DOCS: docs/inxi-audio.txt: ongoing updates, adding more information, more
on helpers, detection methods, etc.

1b. DOCS: New: docs/inxi-usb.txt: USB info, update, added more, a work in
progress.

1c. DOCS: docs/inxi-custom-recommends.txt: name in inxi comment did not match,
and updated to new comment cleaned up syntax in example. Fixed inxi comment file
name.

1d. DOCS: New: docs/inxi-unit-handling.txt: To document how inxi handles
size/speed data internally, and ideally, to help integrate all those methods
into one big tool one day, not spread across many area.

1e. DOCS: New: docs/inxi-repo-package-manager.txt: To start to document arcana
and methods and commands and outputs for package managers. Since this is a late
start, will take time to complete, but better late than never.

2a. MAN/OPTIONS: updated for USB -Jx, -Jxx, -Ja, adding lanes, mode, iec speed
items.

2b. MAN/OPTIONS: fixed error which had USB speed as -Jxxx instead of -Jxx. Also
then changed speed to be -Jx.

2c. MAN/OPTIONS: updated for repos for SBOPKG, SBOUI, SLPKG, and added
SLAPT_GET, I'd forgotten that one.

2d. MAN/OPTIONS: updated for -xx[ADEGN] USB rev, speed, lanes; for -a[ADEGN]
updated for USB mode.

2e. MAN/OPTIONS: updated for memory available/used changed.

3. MAN: fixed some inconsistent use of short/long form display in extra data
options.

--------------------------------------------------------------------------------
CODE:

1a. DesktopData: New function for xfce only detections, turns out xprop is not
necessarily installed, Void Linux for example had failed ID. Old version
required xprop to do the tests, which was not robust and failed in this case.
Function: get_env_xfce_data(). Also made xprop data optional for all the
xxx_xprop_data desktop tests, not just some of them. This will forward proof
the desktops

1b. DesktopData: Fixed bad parens in test cases, was not correctly organized.
if (a || b || (c || d) && e)
was supposed to be:
if (a || b || ((c || d) && e))
Odd how those types of glitches creep in, one fix is also to just make the lines
break more reasonably so the conditions are easier to parse visually.

2a. DEBUGGER: Added /etc/X11/XF86Config-4 xorg conf file to debugger.

2b. DEBUGGER: audio_data(): added audio server versions to cover all known ones.

3. MemoryData: changed all $memory to array references, got rid of split :
separators, which were clearly legacy items leftover from bash/gawk days. Also
changed MemoryData::get('splits') to get('full') to reflect this change.

This change should be transparent though it may introduce corner case undefined
value situation but that should not happen since array values are defined first.

4. UsbData: Refactor of usb speed, rev, added lanes, mode. Refactored most of
the bsd/linux rev/speed logic, merged some of bsd speed/rev into the new
version_data() function, which loads all the data based on what is calling it.
This helps consolidate the logic across usb data sources.

5a. GLOBAL: made functions/methods use same comment syntax for args:
 args: 0:...; 1:...
always starting with 0, to match array index. Same syntax for return array index
values. In some cases simply note a variable is passed by ref:
 args: $value passed by reference.

5b. GLOBAL: made all sub/functions/methods follow the same spacing syntax. This
seems to be a good compromise for space/readability. Note that adding in these
new lines added about 400 lines to the total length, plus the line breaks that
were already there. Yes, inxi has a lot of sub routines! aka functions and
sometimes aka methods.

[empty line]
[comments]
sub [name] {

Packages/classes now also all follow the same spacing rules:

[empty line]
[comments]
{
package [name];
[empty line]
[comments]
sub [name] {
...
}
}

Internally, subs generally do not use any empty lines unless it makes sense to
do so for some specific reason.

5c: GLOBAL: made start of sub comments be upper case, I have a bad habit of
typing comments in lower case, easier to read if it's reads like a normal
sentence.

6. CheckRecommends: refactored entire items logic, set global hash for test
items. Made support > 1 detected package manager.

7. REPOS: cleaned up comments for package manager/repo blocks.

8. SENSORS: sensors_sys failed to reset to undefined $unit and $value, and also
failed to test if they were defined before using them in concatenation.

---
## [Khan/genqlient](https://github.com/Khan/genqlient)@[ff790e1c06...](https://github.com/Khan/genqlient/commit/ff790e1c0631db0144b0752fbf3890cb622432e9)
#### Sunday 2023-05-07 19:15:14 by Ben Kraft

Add an option to handle enums with ugly casing (#270)

There are a bunch of places in genqlient where we just kind of hope you
don't have ridiculous casing conflicts in your schema. Apparently with
enum values there are actual schemas that have this problem! Now we have
an option to disable. I ended up putting it all under `casing` instead
of in `bindings` so we can clearly document the list of algorithms we
support, and so we can have an `all_enums` value if you're working with
a schema with a lot of this; in the future we may want to add similar
behavior for types/fields, add more possible algorithms (e.g. to make
things unexported), etc.

I added tests for the new feature, although the way the tests are set up
it wasn't convenient to do so for a schema where this is actually
required. I also added a check for case conflicts that points you to
this option. (I don't want to do it automatically for reasons described
in the issue; mainly it just seemed a bit too magical.)

Fixes #265.

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[fa0225b05c...](https://github.com/Jackraxxus/tgstation/commit/fa0225b05c5411c46187f67816f8363e7dd91f30)
#### Sunday 2023-05-07 19:16:43 by san7890

Converts Spiderlings from Structures to Basic Mobs (#75001)

If I could've made this more atomic, I would have in a heartbeat, trust
me.

## About The Pull Request

Hey there. People were mocking us for having spiderlings still be a
subtype of `/obj/structure`. I decided to take a lot of time to fix
that. A lot of behavior it was implementing was just pseudo-mob stuff,
so it was actually easier than it looked for the raw conversion. A lot
of the footwork on spider stuff in the basic framework was already done
previously by Jacquerel, so that was pretty nice.

However, there are two new things that weren't introduced in the code
that had to be put in.

A) A component to handle growth and differentiation into a mob. This may
have already existed, no clue. If it does (and it's NOT
evolutionary_leap), let me know.
B) AI Behavior to handle seeking out a vent, entering a vent, and then
exiting out of a different vent. I may have gone a bit wacky on the
code, but it certainly works as expected (spiderling goes in one vent,
exits the other). Let me know if you can think of a way it can be better
optimized, but it was deliberately written to be very failsafey in case
shit goes yonkers.

One fundamental difference between structure spiderlings and basic mob
spiderlings (beyond the AI and not just a random prob() check for
movement) is the fact that they had vent movement coded in... but we
_really_ don't need stuff like that for our intents and purposes. If the
range turns out to be too OP in the current framework, we can always
change it up a bit, but also there's a _lot_ of vents we can end up in
the station (my testing had one spiderling end up in the AI sat to get
obliterated).
## Why It's Good For The Game

Spiderlings aren't structures! They behave like a mob should! Players
can possess spiderlings! They work seamlessly with differentiating into
a giant spider! Better AI! More room for people to add into this very
under-utilized buggers!
## Changelog
:cl:
refactor: Spiderlings are now basic mobs, report any complete
weirdness/deviation from known behavior. They should be a lot more
intelligent now though.
add: AI Spiderlings are super fragile, but they're also super fast,
especially when they get into a vent. Once they're in circulation, they
could end up everywhere! Maybe in the armory, maybe in a locked closet
in maintenance. Be sure to be vigilant and splat them whenever you can
to save the station from a whole lotta heartache!
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [m00nyONE/HodorReflexes](https://github.com/m00nyONE/HodorReflexes)@[f94c8cdf96...](https://github.com/m00nyONE/HodorReflexes/commit/f94c8cdf963ada33211c553c91022d107376df0f)
#### Sunday 2023-05-07 19:17:57 by m00nyONE

remove build.ps1 . thank you windows zip CmdLet for destroying 2 build after another. i should have known better you fucking peace of shitsoftware! maybe use standard encodeing next time

---
## [net-lisias-ksp/KSPe](https://github.com/net-lisias-ksp/KSPe)@[43eea13a1a...](https://github.com/net-lisias-ksp/KSPe/commit/43eea13a1ac3d548920ecb38b20b6b181c91d504)
#### Sunday 2023-05-07 19:32:47 by Lisias T

Throwing Exceptions when trying to load an Already Loaded Assembly. Should mitigate the https://github.com/TweakScale/Companion_Frameworks/issues/6 problem, as well any other idiot that do the same stupidity as I did. #facePalm

---
## [Thlumyn/Skyrat-tg_thlumyn](https://github.com/Thlumyn/Skyrat-tg_thlumyn)@[c5a7f5a7c9...](https://github.com/Thlumyn/Skyrat-tg_thlumyn/commit/c5a7f5a7c93f96cc047297ed8ee61cce02626c75)
#### Sunday 2023-05-07 19:42:11 by SkyratBot

[MIRROR] Mimes can no longer write without breaking their vow. [MDB IGNORE] (#20841)

* Mimes can no longer write without breaking their vow. (#74674)

## About The Pull Request

I feel this is gonna be unpopular with the lazy mime players.

Also, this is an idea I had in my backlog for a while now

![image](https://user-images.githubusercontent.com/53777086/231355622-2c5d5d5a-813d-420c-ae42-c1bdc657f3ba.png)

This removes the Mime's ability to write on paper while they're on their
vow of silence.
This can be compared to hand language, which doesn't let you speak
despite not being considered "talking", and PDA messaging, which does
the same.

Mimes can still write with their pen, which is a nice invisible white
color. I thought I would keep it in as I find that interaction funny to
have a Mime give someone just a blank paper, unknowing that there's text
on it.
Spraycans/Telekinesis/Circuits are also left unaffected because they
require actual effort to obtain (doing genetics, doing circuits, or
printing spraycans which take a lot of inventory space and is limited),
compared to paper which you can carry hundreds of papers around and is
bountiful across the station.

I thought this was attempted at least once, but I can't find any PR that
mentions it, so I'm shooting my shot to see if this is something we'd
want.

## Why It's Good For The Game

Mimes using paper is a lazy way to bypass their one job gimmick: Emoting
over talking.

If they get a job change, they can simply break their vow to access
paper writing abilities, so this doesn't affect that really. It more-so
hits the Mimes who uses the job for the free spells/healing
abilities/etc, and bypasses the downsides (im aware its harder to get
people to read paper than it is to talk to them, but you can literally
get the mute quirk and itll have the same effect without being the whole
job).

The point is, you don't get invisible walls for free; it comes at a cost
of not being able to talk to people. If you want to talk, then break
your vow, lose access to your Mime abilities, and remake it later when
the cooldown is over. You're not meant to do both.

## Changelog

:cl:
balance: Mimes can no longer write on paper without breaking their vow.
/:cl:

* Mimes can no longer write without breaking their vow.

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [newstools/2023-independent-nigeria](https://github.com/newstools/2023-independent-nigeria)@[96709ebeff...](https://github.com/newstools/2023-independent-nigeria/commit/96709ebeffcc2e3ef412d0c2f7baf0a43a2d04eb)
#### Sunday 2023-05-07 20:31:47 by Billy Einkamerer

Created Text For URL [independent.ng/what-i-want-god-to-do-in-my-life-before-i-die-kumuyi/]

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[ad302f209f...](https://github.com/MTandi/tgstation/commit/ad302f209f4fc0b739c6eea8e6be92da05e2742c)
#### Sunday 2023-05-07 21:03:26 by Zytolg

Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] (#73502)

## About The Pull Request
--- 

The Space Tram is currently spaced. This is a known issue with not the
map, but Trams in general. The Space Tram is a Space Tram to encourage a
fix. Until then, the Space Tram is a maint tram that's an actual hazard
but cannot directly kill anyone, including lizards. Enjoy the commodity
as you zip from secmaint to medmaint.
-------------------------------------------------------

I... really don't know if I should be proud of myself here. This whole
process has been akin to a fever dream and it has only been little over
a month since I first created the .dmm for this. What started as a
simple yet humble reimagining of Birdboat has turned into an entirely
new station, and blown past Metastation sized proportions. This has been
my most expansive project yet, and somehow it's also been my quickest.
So without further ado, I unveil Birdshot - Successor to Birdoat.

-------------------------------------------------------

**Due to recent cost expenditures on Icemoon projects, and a growing
need for orbital research stations, Nanotrasen has decided to pull
Birdboat Station out of mothball after nearly 5 years of abandonment.**

Since then, the station has seen a variety of changes at the hands of
the various vagabond lawless scum and villains that have decided to make
the abandoned station their home. Do not fret though, a Nanotrasen
Operation has secured the companies rightful property for corporate use
once again, though you'll need to be the stewards of the remaining
cleanup operation.

------------------------------------------------------

Now, as you might have guessed by now, Birdshot is heavily based on
Birdboat station. Many of the decisions here follow the original layout,
and what had to be modified or moved still tries its best to replicate
and imitate what bird being said. At least, that was the idea initially.
This has very much grown into its own beast and as such, while the main
inspiration has been Birdboat, there are a lot of new ideas thrown into
the mix that really give this station its own unique and deserving
identity. Maybe it's not perfect, but I've been inspired by @MMMiracles
own performance with Tramstation to keep working on Birdshot and
updating it with better and improved faculties. For now, though the
station is in a playable state, and that means I'm making a PR. If I had
to borrow the words of the good MMM, I would call this **Birdshot:
Season 0**


![BirdSHOTFULL2-26-S](https://user-images.githubusercontent.com/33048583/221432760-27af1889-d2d0-4861-9435-df4258525fae.png)



See the image in more detail here: https://imgur.com/iT5Vi8k



## Why It's Good For The Game

We've been with the same 5 maps for a while now. @san7890 jokingly said
that I could sacrifice Metastation back in November if I remade Birdboat
but modern. Obviously that wasn't going to happen, yet I was spurred on
by the idea. When I began this in earnest early this January, @EOBGames
said that a Birdboat sized map would replace Kilostation in the
rotation. Interestingly we're not a small map anymore so I honestly have
no clue where this goes. Maybe that ephemeral 6th map slot that's been
rumored.

What I can say, is that Birdshot is wholly unlike anything else that is
currently in rotation. It's got an engineering section that feels way
too small for a station of that size, almost evocative of Cere. Cargo is
blessed with a Boutique that makes use of @Fikou's new mannequin dolls.
Command is outfitted with a Corporate Guest Suite, and Officials sent
from Nanotrasen can embark from their ferry into the safety of their own
Corporate Dock. Elements of Cerestation are present, yet not in a way
that makes traversal annoying. Furthermore we have **2 Trams** (that I
have yet to get functional but we'll get there) on Birdshot, that's
right 2. One Security Prison Tram, and then other, a Space Tram. Both
Novel in their own ways. Departments on Birdshot twist and turn, and
there's an abundance of Maintenance Tunnels to cut through everything,
for the brave and the bold that is. And there's plenty left to discover,
but I'd rather let Birdshot speak for itself. I'm proud of this one.

If you want something new, this is something that is almost the complete
opposite of Chilled Station - Explicitly Designed to send you back to
the metal death trap that is: **Space Station 13.**


## Changelog
:cl:
add: Birdshot station has been pulled out of Mothball.
add: New station areas and places to visit. A Mix of Kilo and Delta
maints with winding shortcutting paths.
add: A host of new shuttles to support this bold endeavor to reclaim
something that really shouldn't be reclaimed.
add: Two Trams, Two Trams.
add: For the last time Bob, the gaping hole is a **feature.** Use the
breach shutters or have the virologist make starlight.
add: A smiling salute to stations past...
add: Secrets.


/:cl:

---------

Co-authored-by: Zytolg <theoriginaldash@gmail,com>

---
## [highlight/highlight](https://github.com/highlight/highlight)@[18d94ccc74...](https://github.com/highlight/highlight/commit/18d94ccc7425a9441000e1bf4a7f92565898666e)
#### Sunday 2023-05-07 21:18:55 by Lewis Liu

Enable Reflame for Highlight web app (#4586)

## Summary

<!--
Ideally, there is an attached Linear ticket that will describe the
"why".

If relevant, use this section to call out any additional information
you'd like to _highlight_ to the reviewer.
-->

This PR finally enables [Reflame](https://reflame.app/)
[previews](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
for the Highlight web app. 🥳

### What does this mean for me?

First you'll need to sign up at https://reflame.app, connect your GitHub
account, and ask @Vadman97 for an invite to the highlight organization.

Then, once this PR is merged, every time you push up a change to the web
app (in /frontend) or any of its dependencies, you'll get a Reflame
preview link on your commit immediately, usually within 3 seconds,
instead of however many minutes it used to take:
![Screenshot 2023-04-13 at 5 40 57
PM](https://user-images.githubusercontent.com/6934200/231912410-5dc2880d-353c-402e-8562-67ce4ee54137.png)

In addition, you'll have access to the Reflame [VSCode
extension](https://marketplace.visualstudio.com/items?itemName=reflame.agent)
for development, which deploys your changes usually within ~500ms of a
file save, and then reflects your changes instantly with a full browser
refresh in production mode, or with state-preserving React fast refresh
in development mode. See development mode in action here:


https://user-images.githubusercontent.com/6934200/231914985-3679e955-ddcf-4ad1-9c7e-1c7451dc3ef5.mp4

It's worth noting that Reflame is actually _deploying your changes to
the internet_ every time, so you can send these links to yourself to
check your changes on another device (even multiple devices
simultaneously), or share them with teammates or customers to give them
a sneak peak of what you're working on, iterate with their feedback, and
have those changes reflected on their browsers in real time (even if
they're on the other side of the world)!

### How do I even review this? There's like 500 files here?!

I'd recommend reviewing either commit by commit and skipping the 2nd
commit, or by viewing all files changed and skipping over everything in
`__generated` folders, since they only contain files generated using the
newly added build scripts. This should leave only about 30 files to
review, and most of the changes are a only a couple of lines long.

These scripts and generated files are a temporary stop-gap to support
features that don't have first-class support in Reflame yet,
specifically:

- Reading version from package.json
- CSS/SCSS modules
- Tailwind
- SVGR
- Git Submodules
- Vanilla Extract

These are roughly ranked in order of how quickly I think they will get
first-class support in Reflame, at which point we'll be able to remove
the associated scripts and generated files. Notably, Vanilla Extract is
as far down the list as it is because it requires executing
user-supplied code as part of its build process, which is going to take
quite a bit of work to enable safely in a multitenant system like
Reflame (but I do plan on tackling this eventually as I get closer to
building features like testing and backend APIs support). Though we may
still be able to get rid of the build script sooner than that by
building it into the VSCode extension if there's enough demand.

Outside of the script and configuration changes, there are a few
additional source changes for compatibility. I left comments on the PR
for every one of these explaining the motivation behind them. I've also
split most of them out into separate PRs so they can be reviewed, tested
and shipped independently:

- https://github.com/highlight/highlight/pull/5086
- https://github.com/highlight/highlight/pull/5087
- https://github.com/highlight/highlight/pull/5088
- https://github.com/highlight/highlight/pull/5089 

## How did you test this change?

<!--
Frontend - Leave a screencast or a screenshot to visually describe the
changes.
-->

A lot of care has gone into making sure your existing local dev workflow
works exactly as you're used to (just with a few more scripts running
than before), and that the production deployment process remains
untouched as well. If you notice any material differences in any of your
day to day workflows while trying out this PR, or in the Render preview
deploys, please let me know and I'll try to address it ASAP.

I've tried following the [docker dev guide
here](https://www.highlight.io/docs/getting-started/self-host/dev-deployment-guide)
and running `yarn dev:frontend` (without the `doppler run --` part), and
both seem to be working identically as on main as far as I can tell,
though for the latter I'm missing a few env vars from doppler so
couldn't verify past the login screen, will need your help to make sure
everything works as expected there.

If you want to try out Reflame before this PR gets merged, just make a
branch off of this PR (previews are not working for this PR because it's
coming from a fork, and the appId in the config is for the
highlight/highlight repo, but it should work if you cherry pick these
commits into another branch within this repo). The VSCode extension
should also just work once you get a VSCode account.
[Here's](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
the preview I'm using to test my changes.

Would love to make Reflame better with your feedback! Just leave a
comment here, [shoot me an email](mailto:lewis@reflame.app), or ask for
an invite to the #highlight-reflame channel in Slack to chat there or
send me a DM.

## Are there any deployment considerations?

<!--
 Backend - Do we need to consider migrations or backfilling data?
-->

Definitely would be helpful to get a Render preview for this to poke
around in.

---
## [Filipianosol/TownOfHostEdited](https://github.com/Filipianosol/TownOfHostEdited)@[2f95978b5f...](https://github.com/Filipianosol/TownOfHostEdited/commit/2f95978b5f67ac712f055fc3986de7cc3eff7d6d)
#### Sunday 2023-05-07 21:34:15 by Filipianosol

Workaholic: Can't win after they died: default OFF

On the current default settings Workaholic doesn't stand a chance.

By default everyone can see who the Workaholic is. Because of this,
players can rush to hunt them down or vote them off and there is no
punishment for doing so, as by default they can't win once they've died.
You could override their tasks to 2 or 3 to give them a chance but then
it becomes a ridiculous role that dies/wins too quickly in my opinion,
like a worse version of YouTuber.

This is why instead I'm proposing `Can't win after they died` be set to
OFF by default. I believe default settings should be reasonable so that
players' first experience with a role is positive and they don't just
end up hating the role because of them.

This setup (`Can't win after they died` OFF +
`Everyone knows who the Workaholic is` ON) also matches the original
Workaholic behavior from TOH_Y.

---
## [zerbina/nimskull](https://github.com/zerbina/nimskull)@[c4250cc115...](https://github.com/zerbina/nimskull/commit/c4250cc11536bf6c8922bbd192d2ec39142d46d9)
#### Sunday 2023-05-07 22:37:51 by Saem Ghani

Parser: drop direction `reports` dependencies

This removes direct dependency on `reports`, but an indirect one still
exists via `msgs`. It's pretty trivial indirection at the moment, but
after dropping direct reports dependencies the API can be changed more
drastically.

A number of changes were required in order to make this possible, here
is an overview:

- smaller parser public API & simpler implementation
- added `parse` compiler command, for devs
- parser error message improvements
- fixes to `astrepr` logic and output
- lots of style clean-ups

Details
=======

Slimmer `parser` Public API
---------------------------

Previously the parser had many public procedures (eg: `isOperator`,
`getTok`, `skipComment`, etc) that would allow fine grained control for
other modules.

There are many issues with this:
- there are no consumers of this API
- lots of public API surface to test
- the API itself was bad, it conflated lexing and parsing

The public API surface for the parser has been reduced significantly,
now consisting of:
- `openParser`
- `parseTopLevelStmt`
- `parseAll`
- `closeParser`
- `parseString`

That's it, which frankly reads far more sensibly.

Simplified `parser` Implementation
----------------------------------

- removed `InternalReport`, `reports_parser`, and `reports_enum` imports
- introduced diagnostics for the parser, akin to the lexer, `ParseDiag`
- `ParseDiag` favours data over strings
- `ParsedNode` now has its own kind enum, mostly a subset of
   `TNodeKind`, but entirely compatible

Consolidated a pattern within the parser, where a node was created with
the current token's information, and then the token was immediately
consumed via `getTok` to advance the `lexer`. This is captured in the
newly introduced `newNodeConsumingTok`.

Long-term, itemizing these traversal/consumption patterns will make the
parser logic not only more regular, but also highlight oddities in the
grammar as the implementation will be convoluted.

Parsing/Diagnostics Performance
-------------------------------

`ParsedNode` uses a lightweight `ParsedToken`

Introduce `ParsedToken`, a smaller data type, storing the least amount
of data required from `lexer.Token` for `ParsedNode`. This not only
saves memory, but the runtime performance impact on my machine is
roughly 33% faster full compiler testament run for all targets

- before change: 3+ minutes
- after change:  2+ minutes

Added specialized diagnostic/report kinds for:
- empty accent quote when ident expected
- msg for asm statements without a string literal
These reduces the amount of string data carried around in the compiler.

Improved Custom Numeric Literal Handling
----------------------------------------

- the `lexer` still does silly things for lexing these
- it just does less work and produces better data
- fewer string operations and hacks are required by the `parser`

Parser Diagnostic/Reporting - Invalid Indentation
-------------------------------------------------

- now has correct source line information
- tracks instantiation and submission location
- has the appropriate severity
- improved phrasing for indent error from possible missed `=` character
- adjusted tests for the above

Parser Diagnostic/Reporting - Malformed Call Syntax
---------------------------------------------------

- `parser` detects malformed calls and sets better line info
- net-net the user will have a better chance to find the issues

Parser Diagnostic/Reporting - Misc
----------------------------------

- token rendering call out keywords via prefix, eg: `keyword template`
- inconsistent spacing style check shows the problematic source

Removed unused report kinds:
- `rparIdentOrKwdExpected`
- `rparRotineExpected`
- `rparPragmaAlreadyPresent`

Parse Compiler Command
----------------------

`parse` command:
- added `parse` command, which outputs the parsed ast for a file
- usage: `nim parse foo.nim`
- super useful for diffing parser output changes
- heavily leverages `astrepr`

`astrepr` module:
- `astrepr.treeRepr` now works for `ParsedNode`, was previously broken
- AST trasversal is now exhaustive and breakages less likely to pass CI

`astrepr` output improvements, mainly for `ParsedNode`:
- `astrepr` now shortens ParsedNodeKind enum
- output now includes line and column information
- comments no longer result in excessive new line output
- fixed many formatting issues for `ParsedNode` output
- improved `astrepr`'s output for custom numeric literals

Canonical Filenames Performance Issue
-------------------------------------

Also discovered a performance issue with canonical filenames option and
the `nimdebugstacktrace` option. Removed some of the pain, but canonical
file paths result in significant performance issues due to filesystem
IO. I've fixed part of it and filed an issue:
https://github.com/nim-works/nimskull/issues/546

Other Improvements
------------------

- introduced `debugutils.setFrame` template for frame msg hints
- above `setFrame` avoids the canonical path performance hit
- removed circular dependency between `ast` and `options` module
- document unused parser reports and other outliers
- move `isImportedException` to `ast/types`, whice drops `front/options`
  cyclic depencdency from `ast/ast_query`
- fixed docs in nimlexbase, also easier to understand
- `ast.toPNode` now handles `nil` input
- `syntaxes.parseFile` returns `ParsedNode`, allows avoiding unnecessary
  conversions in future use cases where only `ParsedNode` is required

Special Mentions
----------------

Thanks, clyybber and zerbina for the reviews!

Misc
----
- remove blank space characters from otherwise empty lines
- remove awful code style of `0 < foo.len`
- fixed a number of typos in comments
- adjusted a few tests to ensure they pass

---
## [Xoffio/nushell](https://github.com/Xoffio/nushell)@[2e01bf9cba...](https://github.com/Xoffio/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Sunday 2023-05-07 22:37:56 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1a918a2e14...](https://github.com/tgstation/tgstation/commit/1a918a2e1411f58e5a90f587a92daebebb9ac395)
#### Sunday 2023-05-07 22:45:22 by Jacquerel

Golem Rework (#74197)

This PR implements this design document:
https://hackmd.io/@Y6uzGFDGSXKRaWDNicSiEg/BkRr176st
Put briefly, this will remove every existing golem subtype and
consolidate golems into a single species with cool new sprites.
NOT implemented from that PR is the ability to eat Telecrystals, I
couldn't come up with an appropriate visual that can stack with the
existing ones, but that should be a reasonably trivial add for a future
artist & developer.

New Golems have a food-based mechanic where their hunger decays pretty
quickly and can only be replenished by eating minerals. They start
moving slower as they get hungrier, until eventually they become
completely immobilised and need to be rescued.
Eating different kinds of minerals will visually change your sprite and
give you a special effect in a similar way to old golems, but temporary.
While transformed, you can't eat any other kind of mineral which would
transform you (but can still consume glass).
To see the full list of effects, look at the hackmd above.

In service of these sprites working I have refactored the
`species/offset_features` feature by killing it and delegating that
responsibility to limbs instead. Rather than applying an offset to items
due to your species, it is due to your weird head or arms. This makes
overall more sense to me, but it inflates the code changes in this PR
somewhat.
It doesn't make a lot of sense to atomise unfortunately because that
code also seemed to be entirely unused until I tried to use it in this
PR, so you wouldn't be able to tell if my changes broke anything. I
might make a downstream sad by doing this.

All of the actual numbers in this PR are made up and only loosely
tested, it will need some testmerges to gather feedback about whether it
sucks or not.

Other relevant changes:
I reworked how bioscrambling works based off bodypart bodytypes, to
automatically exclude golem limbs in either direction. There's really no
way to have those work on humans or vice versa. Organs still fly though.

---
## [Vexylius/tgstation](https://github.com/Vexylius/tgstation)@[b3e5642d94...](https://github.com/Vexylius/tgstation/commit/b3e5642d94caab455bea8b71e244081249cb2924)
#### Sunday 2023-05-07 22:52:50 by san7890

Fixes Active Turf Scenario on Tramstation (#74354)

## About The Pull Request

On the tin. Basically whenever `atmoscilower_2.dmm` would invoked
`atmoscilower_attachment_a_2.dmm`, it would trigger an active turf in
this location since it doesn't have a "ceiling". (as well as there being
an "aired" turf mingling with airless turfs)

This caused the following report:
```txt
 - All that follows is a turf with an active air difference at roundstart. To clear this, make sure that all of the turfs listed below are connected to a turf with the same air contents.
 - In an ideal world, this list should have enough information to help you locate the active turf(s) in question. Unfortunately, this might not be an ideal world.
 - If the round is still ongoing, you can use the "Mapping -> Show roundstart AT list" verb to see exactly what active turfs were detected. Otherwise, good luck.
 - Active turf: Station Asteroid (163,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (163,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (164,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (164,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,80,2) (/area/station/asteroid). Turf type: /turf/open/misc/asteroid/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (166,81,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,83,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/iron/smooth. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,83,3) (/area/station/asteroid). Turf type: /turf/open/openspace/airless. Relevant Z-Trait(s): Station.
 - Z-Level 2 has 8 active turf(s).
 - Z-Level 3 has 1 active turf(s).
 - Z-Level trait Station has 9 active turf(s).
 - End of active turf list.
```

This is what it looked like when it was reproduced on my machine:


![image](https://user-images.githubusercontent.com/34697715/228689991-d9cc87c3-f931-4513-8399-928c93def605.png)


Surprisingly not that hard to debug, albeit tedious. At least I know
that this was the issue with 100% confidence.
## Why It's Good For The Game

Ate up 0.1 seconds of init on my machine. That's silly.
## Changelog
No way players care

---
## [newstools/2023-daily-post-nigeria](https://github.com/newstools/2023-daily-post-nigeria)@[78d526879d...](https://github.com/newstools/2023-daily-post-nigeria/commit/78d526879df7e65644a316295245b252006d05bd)
#### Sunday 2023-05-07 23:08:36 by Billy Einkamerer

Created Text For URL [dailypost.ng/2023/05/07/i-cant-stop-cheating-on-you-rapper-big-xhosa-tells-girlfriend/]

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[96dbd3a8b7...](https://github.com/i3roly/glibc_ddwrt/commit/96dbd3a8b7243414e3061786b73d862a5c0ea8b5)
#### Sunday 2023-05-07 23:15:49 by gagan sidhu

[v52549] fix signal quality on status page, add frr/snort to big builds

- trying to use pcre2 on this snort, so it's a little broken right now
  as i figure out how to tidy up some calls for the rules. it works fine
  without the rule files though. if you really need to use snort and
  you're on a big build, just use entware since /usr/local/bin takes
  precedent over /usr/bin

- i added frr to the big builds and also the lootbag, just because
  assfuck is obssessed with it. i don't understand what the big deal is,
  but it's there.

- i fixed a weird issue with the signal quality always being 100%. i
  have no idea why, but it seems when this variable is passed through
  the ioctl it's parsed as an unsigned character, meaning it's 256
  larger than it should be. the numbers now match what's returned by
  "iwpriv <interface> show stainfo" so i think we're okay.

they should call snort daryl cause that mf got a new nose he love it so
much, realtalk99 on that.

---

