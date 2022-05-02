## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-01](docs/good-messages/2022/2022-05-01.md)


1,501,208 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,501,208 were push events containing 2,212,778 commit messages that amount to 139,245,552 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[7c61bf65f2...](https://github.com/tgstation/tgstation/commit/7c61bf65f2b3c661bf622864bb7596e0e89d1f28)
#### Sunday 2022-05-01 00:02:50 by vincentiusvin

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)


About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

---
## [dub-stack/chakra-radix-colors](https://github.com/dub-stack/chakra-radix-colors)@[733ee8c55a...](https://github.com/dub-stack/chakra-radix-colors/commit/733ee8c55ad5b4b6765a775ecfb13f025c6fc81a)
#### Sunday 2022-05-01 00:49:55 by Spencer Duball

test(checkbox): Holy shit that was painful. Looks like cypress caches  inbetween tests and doesn't refresh these until a new  with a different query happens???

---
## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[cd2bd18cf8...](https://github.com/Tastyfish/Skyrat-tg/commit/cd2bd18cf8193c7cfc2f0014ef449baa8792aad4)
#### Sunday 2022-05-01 01:01:26 by SkyratBot

[MIRROR] Creates Linters for (bad) Commented Out Lines in Maps [MDB IGNORE] (#12543)

* Creates Linters for (bad) Commented Out Lines in Maps (#65888)

* Creates CI Linters for Commented Out Lines in Maps

Creates Linters for (bad) Commented Out Lines in Maps

Hey there,

This PR is made because what happened in #65837 was fucking horrible awful shit that I'm still dealing with a few days after I fixed it. This _should hopefully_ add a new linter for commented out lines of code in a .DMM file, and HOPEFULLY doesn't flag the commented line that prevents unwanted TGM > DMM conversion.

As a proof to see if it works, I'll be adding a comment to Line 2 of IcemoonUnderground_Above.dmm. Hopefully, on the first CI check, it'll fail. I'll remove that line so it doesn't make its way into production (it will suck).

* Creates Linters for (bad) Commented Out Lines in Maps

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [holychowders/serenity](https://github.com/holychowders/serenity)@[49b087f3cd...](https://github.com/holychowders/serenity/commit/49b087f3cd49261164bd4556cd6e9e0d95a3afc1)
#### Sunday 2022-05-01 02:21:13 by kleines Filmröllchen

LibAudio+Userland: Use new audio queue in client-server communication

Previously, we were sending Buffers to the server whenever we had new
audio data for it. This meant that for every audio enqueue action, we
needed to create a new shared memory anonymous buffer, send that
buffer's file descriptor over IPC (+recfd on the other side) and then
map the buffer into the audio server's memory to be able to play it.
This was fine for sending large chunks of audio data, like when playing
existing audio files. However, in the future we want to move to
real-time audio in some applications like Piano. This means that the
size of buffers that are sent need to be very small, as just the size of
a buffer itself is part of the audio latency. If we were to try
real-time audio with the existing system, we would run into problems
really quickly. Dealing with a continuous stream of new anonymous files
like the current audio system is rather expensive, as we need Kernel
help in multiple places. Additionally, every enqueue incurs an IPC call,
which are not optimized for >1000 calls/second (which would be needed
for real-time audio with buffer sizes of ~40 samples). So a fundamental
change in how we handle audio sending in userspace is necessary.

This commit moves the audio sending system onto a shared single producer
circular queue (SSPCQ) (introduced with one of the previous commits).
This queue is intended to live in shared memory and be accessed by
multiple processes at the same time. It was specifically written to
support the audio sending case, so e.g. it only supports a single
producer (the audio client). Now, audio sending follows these general
steps:
- The audio client connects to the audio server.
- The audio client creates a SSPCQ in shared memory.
- The audio client sends the SSPCQ's file descriptor to the audio server
  with the set_buffer() IPC call.
- The audio server receives the SSPCQ and maps it.
- The audio client signals start of playback with start_playback().
- At the same time:
  - The audio client writes its audio data into the shared-memory queue.
  - The audio server reads audio data from the shared-memory queue(s).
  Both sides have additional before-queue/after-queue buffers, depending
  on the exact application.
- Pausing playback is just an IPC call, nothing happens to the buffer
  except that the server stops reading from it until playback is
  resumed.
- Muting has nothing to do with whether audio data is read or not.
- When the connection closes, the queues are unmapped on both sides.

This should already improve audio playback performance in a bunch of
places.

Implementation & commit notes:
- Audio loaders don't create LegacyBuffers anymore. LegacyBuffer is kept
  for WavLoader, see previous commit message.
- Most intra-process audio data passing is done with FixedArray<Sample>
  or Vector<Sample>.
- Improvements to most audio-enqueuing applications. (If necessary I can
  try to extract some of the aplay improvements.)
- New APIs on LibAudio/ClientConnection which allows non-realtime
  applications to enqueue audio in big chunks like before.
- Removal of status APIs from the audio server connection for
  information that can be directly obtained from the shared queue.
- Split the pause playback API into two APIs with more intuitive names.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [Khalvat-M/kernel_samsung_msm8974](https://github.com/Khalvat-M/kernel_samsung_msm8974)@[dd1c947224...](https://github.com/Khalvat-M/kernel_samsung_msm8974/commit/dd1c94722430a3bafe227caa9ed8c9f5a911a808)
#### Sunday 2022-05-01 05:18:49 by Linus Torvalds

mm: get rid of 'vmalloc_info' from /proc/meminfo

It turns out that at least some versions of glibc end up reading
/proc/meminfo at every single startup, because glibc wants to know the
amount of memory the machine has.  And while that's arguably insane,
it's just how things are.

And it turns out that it's not all that expensive most of the time, but
the vmalloc information statistics (amount of virtual memory used in the
vmalloc space, and the biggest remaining chunk) can be rather expensive
to compute.

The 'get_vmalloc_info()' function actually showed up on my profiles as
4% of the CPU usage of "make test" in the git source repository, because
the git tests are lots of very short-lived shell-scripts etc.

It turns out that apparently this same silly vmalloc info gathering
shows up on the facebook servers too, according to Dave Jones.  So it's
not just "make test" for git.

We had two patches to just cache the information (one by me, one by
Ingo) to mitigate this issue, but the whole vmalloc information of of
rather dubious value to begin with, and people who *actually* want to
know what the situation is wrt the vmalloc area should just look at the
much more complete /proc/vmallocinfo instead.

In fact, according to my testing - and perhaps more importantly,
according to that big search engine in the sky: Google - there is
nothing out there that actually cares about those two expensive fields:
VmallocUsed and VmallocChunk.

So let's try to just remove them entirely.  Actually, this just removes
the computation and reports the numbers as zero for now, just to try to
be minimally intrusive.

If this breaks anything, we'll obviously have to re-introduce the code
to compute this all and add the caching patches on top.  But if given
the option, I'd really prefer to just remove this bad idea entirely
rather than add even more code to work around our historical mistake
that likely nobody really cares about.

Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Change-Id: Ia17de8b8f49d801efa5aaff3c61ba4c1082dc1e3

---
## [DamienCassou/magit](https://github.com/DamienCassou/magit)@[ab801de538...](https://github.com/DamienCassou/magit/commit/ab801de53827a232b7806362fb08ca804f27c6d0)
#### Sunday 2022-05-01 06:21:16 by Jonas Bernoulli

magit-section-context-menu: Support non-section branches

We use section keymaps to implement context-sensitive menus but
branches are not always represented using sections.  To support
such "painted branches" anyway use fake sections, which closely
mirror the commit section in which the click occurred.

This admittedly is ugly and somewhat risky, but seems to work well.
`magit-section-update-highlight' would break due to this hack, so
we avoid calling it.  If it turns out that things also break due
to this kludge, then we might have to revert.

---
## [teenshowstep/rathena](https://github.com/teenshowstep/rathena)@[d617d9f083...](https://github.com/teenshowstep/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Sunday 2022-05-01 06:39:24 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [Starloader-project/Starloader-API](https://github.com/Starloader-project/Starloader-API)@[a22f579f16...](https://github.com/Starloader-project/Starloader-API/commit/a22f579f16f400eab01bdffc3fddb80697c1e20a)
#### Sunday 2022-05-01 07:06:58 by Geolykt

Savegame metadata API v1

There is the need for more codecs and overall a more polished API,
but this is at least usable for small-sized objects. For any objects
over 32k bytes in size, this is not really an option though I will eventually
search for one.

This system is also able to load vanilla saves, though right now the user
is not able to save vanilla saves though API-wise this is allowed.
The goal will be to allow the player to choose between savegame systems,
though this might be a bit annoying so I am not too sure about that.

Anyways, I am a bit surprised that I did not see the need of such an API
beforehand because quite honestly you need this for EVERYTHING.
I should also improve SpStarmap a bit more, there is an awful lot of unmapped
stuff used in the vanilla savegame format class.

Another thing that might be interesting to know is whether this API
is capable of actually surviving for long in the wild - while I have tried
to write it in a way that it is versatile, I am not really pleased with it
even if it largely met my expectations for the API. There are a lot of design
flaws but I don't think that you can get rid of them anytime soon. I should
also get rid of Optional getters as they are kindof prone to errors

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[dca0edc30e...](https://github.com/jlsnow301/tgstation/commit/dca0edc30e9db1424dffb582c5e8d075e0581ac0)
#### Sunday 2022-05-01 07:38:15 by B4CKU

Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

---
## [buzzcut-s/kernel-x86](https://github.com/buzzcut-s/kernel-x86)@[58eb76ae93...](https://github.com/buzzcut-s/kernel-x86/commit/58eb76ae93ccfdd2932088bead6cc8ccf3a8b836)
#### Sunday 2022-05-01 08:57:44 by Matt Kramer

ALSA: hda/realtek: Add alc256-samsung-headphone fixup

[ Upstream commit ef248d9bd616b04df8be25539a4dc5db4b6c56f4 ]

This fixes the near-silence of the headphone jack on the ALC256-based
Samsung Galaxy Book Flex Alpha (NP730QCJ). The magic verbs were found
through trial and error, using known ALC298 hacks as inspiration. The
fixup is auto-enabled only when the NP730QCJ is detected. It can be
manually enabled using model=alc256-samsung-headphone.

Signed-off-by: Matt Kramer <mccleetus@gmail.com>
Link: https://lore.kernel.org/r/3168355.aeNJFYEL58@linus
Signed-off-by: Takashi Iwai <tiwai@suse.de>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Laboredih123/goonstation](https://github.com/Laboredih123/goonstation)@[bdad398f9e...](https://github.com/Laboredih123/goonstation/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Sunday 2022-05-01 09:19:39 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [POETICREALATHEART/POETICREALATHEART](https://github.com/POETICREALATHEART/POETICREALATHEART)@[0752de9ffd...](https://github.com/POETICREALATHEART/POETICREALATHEART/commit/0752de9ffd029b3438456accc0c341314de3d754)
#### Sunday 2022-05-01 11:16:20 by Poetic

Create FUNDING.yml

4 DEFRNT APPS TO SHUT IT DOWN MEANING BLOCK THERE PRIVTE SHOWS OR INTERUPT THEN AN JUST BE A PAIN I GAVE SUMONE 750 AN THEY RAPE HER IN FRONT 400 PEOPLE LIVE WHILE THEY GIFTED AN AG IT ON SHE NOW MISSING SHE WOULD BEEN THE 6 PERSON I HELP CAHNGED HER LIFE IN STEAD IT DID THE OPSITE WHEN I GAVE THE GIRL THE MONEY SHE GAVE IT BACK I DO MJUSIC AN SHE SONG WTH ME TWICE FIRST TIME I HURD HER I CRYED I CHOOSE PEOPLE HER HAVE SUM KIND OF WAY TO REACH PEOPLE WITH NO HOPE SO THEY CAN SEE THERE IS AN NOT TO EVER GIVE UP THAT THERE IS SUM GOOD PEOPLE OUT THERE AN TO BELIEVE THIS GIRL THEY MADE EXAMPLE OF AN IVE BEEN FIGHTING WTH THEM MY OWN WAYS LAST TWO MONTHS THEY MADE A SONG WQITH HER SCRFEAMNGG NOOONONO AN ASDDKING FOR GOD HELP AS THE HOOK TO TORTURE ME I MADE 8 FREESYTYLES AN TELLING WHATTHEY DID AN DISSING BACK AN 2 MONTHS FOUR APPS I INTRUPT THERE SHOWS WTH HIS GIRLS ON THM I TAKE CONTROLL OF THE BROADCAST WERE THEY HAVE NO CHOICE BUT TO LISTEN TELLING THE GIRL STORY AN WHT HE DID CUS ALL THEY DO IS REACT THE GIRL GETING RAPE LIKJE ITS FUNNY ONKLY THING I AINT BEEN ABLE TO DO YET IS BLOCK THERE PREMIUM SHOW WERE THERY MAKE THERE REAL MONEY BUT IVE BEEN WINING THE PEOPLE AN THEY ALL STAND BEHIUND ME BUT ARE SO SCARED OF THIS GUY AN DO WHT EVR HE SAYS BUT DONT WANNA SAME TO HAPPEN TO HIM IVE HAD ALL DEFRNTY PEOPLE THREATEN MY LIFE FAMILY FROM ALL RACES TO MY SAME TOWN YET I DONT Care i still fght i gave her the money wth her not asking for it she gave it bavck i thought she wAS BEING STUBBORN SO THEN I DROP IT ON THE APP AT ONCE IN A WAY SHE HAD TO TAKE IT SHE THEN VANSHED FOR 17 TIL I SLEPT WTH A GIRL AN THE GIRL GOT IN CONTACT WTH HER 2 DAYS LATER ACRFOSS MY SCREEN THERE WAS A GIRL FLASHING THE GIRL BUT NAKED GET BEST HOG ITIED COMNG ACROSDS MY SCREEN THEY NEVER ASK FOR MONEY NOR DID WANT SANYTHNG FROM ME I OFFER EVERYTHNG ICOULD EVEN MYSELF THEY DIDNT WANT IT INSTEAD THEY JUST WANT ED TO SHOW EVERY ONE WHT THEY WERE DOING TO HER TO PUT FEAR INTO THEM I SPOKE OUT AN AM NOT GIVEING UP BUT NEED SUM SOPORT ON HOW I CAN BLOCK THE PREM WHN ON THERE OR INTRUPT THEN TO MAKE NOT WHT THEY WERE EXPTEING OR PAID FOR I FIGHT FOR THE PEOLE AN TO SHOW THERE IS HOPE ANN IM JUST ONE PERSON STANDING UP TO THEM AN LOOK WHAT HAPPEN FOR ONE MONTH NOONE CARRIED HIS NAME CUS OF ME BUT IM ONLY ONE IF MORE OF THM STOOD UP IT WOULD MATTER I HAVE NOTHNG AN ONLY STARTTED LEARNING AN TEAching my self code an cookie s so i v=can do whAT I BEEN DOIING WHAT I DO NOW ON THE APP AN THEY HAte it

---
## [i05nagai/aws-cdk](https://github.com/i05nagai/aws-cdk)@[c071367def...](https://github.com/i05nagai/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Sunday 2022-05-01 11:43:35 by Kaizen Conroy

feat(glue): support partition index on tables (#17998)

This PR adds support for creating partition indexes on tables via custom resources.
It offers two different ways to create indexes:

```ts
// via table definition
const table = new glue.Table(this, 'Table', {
  database,
  bucket,
  tableName: 'table',
  columns,
  partitionKeys,
  partitionIndexes: [{
    indexName: 'my-index',
    keyNames: ['month'],
  }],
  dataFormat: glue.DataFormat.CSV,
});
```

```ts
// or as a function
table.AddPartitionIndex([{
  indexName: 'my-other-index',
  keyNames: ['month', 'year'],
});
```

I also refactored the format of some tests, which is what accounts for the large diff in `test.table.ts`. 

Motivation: 
Creating partition indexes on a table is something you can do via the console, but is not an exposed property in cloudformation. In this case, I think it makes sense to support this feature via custom resources as it will significantly reduce the customer pain of either provisioning a custom resource with correct permissions or manually going into the console after resource creation. Supporting this feature allows for synth-time checks and dependency chaining for multiple indexes (reason detailed in the FAQ) which removes a rather sharp edge for users provisioning custom resource indexes themselves.

FAQ:

Why do we need to chain dependencies between different Partition Index Custom Resources? 
  - Because Glue only allows 1 index to be created or deleted simultaneously per table. Without dependencies the resources will try to create partition indexes simultaneously and the second sdk call with be dropped.

Why is it called `partitionIndexes`? Is that really how you pluralize index?
  - [Yesish](https://www.nasdaq.com/articles/indexes-or-indices-whats-the-deal-2016-05-12). If you hate it it can be `partitionIndices`.

Why is `keyNames` of type `string[]` and not `Column[]`? `PartitionKey` is of type `Column[]` and partition indexes must be a subset of partition keys...
  - This could be a debate. But my argument is that the pattern I see for defining a Table is to define partition keys inline and not declare them each as variables. It would be pretty clunky from a UX perspective:
    ```ts
    const key1 = { name: 'mykey', type: glue.Schema.STRING };
    const key2 = { name: 'mykey2', type: glue.Schema.STRING };
    const key3 = { name: 'mykey3', type: glue.Schema.STRING };
    new glue.Table(this, 'table', {
      database,
      bucket,
      tableName: 'table',
      columns,
      partitionKeys: [key1, key2, key3],
      partitionIndexes: [key1, key2],
      dataFormat: glue.DataFormat.CSV,
    });
    ```

Why are there 2 different checks for having > 3 partition indexes?
  - It's possible someone decides to define 3 indexes in the definition and then try to add another with `table.addPartitionIndex()`. This would be a nasty deploy time error, its better if it is synth time. It's also possible someone decides to define 4 indexes in the definition. It's better to fast-fail here before we create 3 custom resources.

What if I deploy a table, manually add 3 partition indexes, and then try to call `table.addPartitionIndex()` and update the stack? Will that still be a synth time failure?
  - Sorry, no. 

Why do we need to generate names?
  - We don't. I just thought it would be helpful.

Why is `grantToUnderlyingResources` public?
  - I thought it would be helpful. Some permissions need to be added to the table, the database, and the catalog.

Closes #17589.

----

*By submitting this pull request, I confirm that my contribution is made under the terms of the Apache-2.0 license*

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2fd3da7903...](https://github.com/treckstar/yolo-octo-hipster/commit/2fd3da79036d8a1f558abfdeef39abc7233b6dc2)
#### Sunday 2022-05-01 12:22:02 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [RyanTLG/GamerItems](https://github.com/RyanTLG/GamerItems)@[555113e04e...](https://github.com/RyanTLG/GamerItems/commit/555113e04ef098d70b3436629a029500d0895aef)
#### Sunday 2022-05-01 12:42:11 by RyanTLG

update name

FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU

---
## [kane-f/vgstation13](https://github.com/kane-f/vgstation13)@[620e9e480e...](https://github.com/kane-f/vgstation13/commit/620e9e480e17c337eb674c7649534bb37e89fe1f)
#### Sunday 2022-05-01 12:46:21 by Eneocho

pAI medical chems buff (#32388)

* pAI medical chems

* Update pai.dm

* DexalinPlus?

* Some more chems, for effect

* Fix?

* do you feel it now mr dream checker

* i need better glasses holy shit i'm blind

* dexp to dex

---
## [LordCupcakeIX/AutoTrimps](https://github.com/LordCupcakeIX/AutoTrimps)@[f7b39ffdb5...](https://github.com/LordCupcakeIX/AutoTrimps/commit/f7b39ffdb51d3a4ae1748556e0767ccd67539602)
#### Sunday 2022-05-01 13:51:07 by SadAugust

Fixing bugs and adding universe selection feature

Heyy, I made a few modification to graphs for my AT fork and figured I might as well share since it fixes a few bugs that I've at least been annoyed by quite a bit. If you want to test it out first to make sure it's all working you can test it on https://SadAugust.github.io/AutoTrimps_Local. Changed I've made are listed below, I've only done minimal testing but haven't found any issues with it.

Removed minified version of code to make it readable

Added option to select Universe which will visibility of U1 and U2 graphs depending on the selection. Reduces a ton of unnecessary settings from cluttering the list and figured I'd make it easier to expand for if we do get more universes.

Remembers graph selection when reloading the page instead of defaulting to helium/radon per hour

Hides portals from other universes showing so if U2 graphs are being looked at you won't see U1 portals in the sidebar, should fix bugs like void maps being unreadable when there's a significant difference in portals between the 2 universes.

Fixed it not drawing graphs properly when reopening Graphs after the initial load as it was a nuisance having to go to another graph and back to get it to display anything.

---
## [dave-burke/rpn-calc](https://github.com/dave-burke/rpn-calc)@[3153c244b5...](https://github.com/dave-burke/rpn-calc/commit/3153c244b53eb23ac097d5745869ded3d81d6f40)
#### Sunday 2022-05-01 14:24:24 by Dave Burke

Configure vitest

Setting 'globals: true' works fine on the CLI but VSCode still has a fit
that it can't find 'test' and 'expect'. Importing manually seems to
work, but it's an annoying workaround.

VSCode also complains about the triple-slash declaration in
vite.config.ts and says that the file isn't part of the project. I think
it doesn't recognize the "references" entry for tsconfig.node.json that
lists vite.config.ts. Having to ignore the config file is annoying, but
it's a small file so the risk is not so bad I suppose.

But holy crap the js/ts community needs to get its shit together.

---
## [maayanKash/opentitan](https://github.com/maayanKash/opentitan)@[29b8d2c3e7...](https://github.com/maayanKash/opentitan/commit/29b8d2c3e7fde48a117a31241c508bd4325f5b88)
#### Sunday 2022-05-01 14:29:56 by Rupert Swarbrick

[dv,verilator] Make multiple sim_ctrl extensions play nicely

I'd finally got annoyed enough about not being able to pass "-t" in
the middle of a command line to figure out what was going on. It turns
out that by default getopt_long rearranges its arguments to put all
positional args at the end. That's nice, because it allows you code to
easily support stuff like

   my_program -a -b positional0 -c -d positional1

and, post-parse, it will find positional0 and positional1 as the last
two arguments. (If long enough in the tooth, you might remember having
to do "my_program -a -b -c -d positional0 positional1" for some
programs: this is what getopt fixes for us!)

Unfortunately, this behaviour plays havoc when more than one parser
wants to look at argv at once. For example, suppose you have

   my_program --some-args ARG --no-args

and you parse this twice. The first parser understands --no-args and
the second understands --some-args. With the default behaviour and ":"
at the start of the optstring, the first parser will ignore the
unknown --some-args argument and move the positional ARG to the end.
But then the second parser sees

  my_program  --some-args --no-args ARG

and tries to pass "--no-args" as the value to "--some-args". Much
confusion ensues...

Fortunately, we can pass '-' at the start of optstring to disable this
behaviour. The result is harder to parse if you're interested in
positional arguments (which is why this isn't the default behaviour)
but works when you have multiple parsers that have to place nicely
together.

Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

---
## [cygnus-rom/packages_apps_Settings](https://github.com/cygnus-rom/packages_apps_Settings)@[cea0ee02f4...](https://github.com/cygnus-rom/packages_apps_Settings/commit/cea0ee02f4c329a3961749ea2a52ab9ca9a733b3)
#### Sunday 2022-05-01 15:23:06 by Dhruv

Settings: COMPILE KOTLIN FILES FOR GODS SAKE

 I fucked my brains over this for 2hrs, fuck you Android

---
## [go-gitea/gitea](https://github.com/go-gitea/gitea)@[3725fa28cc...](https://github.com/go-gitea/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Sunday 2022-05-01 16:11:25 by Gusted

Improve UI on mobile (#19546)

Start making the mobile experience not painful and be actually usable. This contains a few smaller changes to enhance this experience.

- Submit buttons on the review forms aren't columns anymore and are now allowed to be displayed on one row.
- The label/milestone & New Issue buttons were given each own row even tough, there's enough place to do it one the same row. This commit fixes that.
- The issues+Pull tab on repo's has a third item besides the label/milestone & New Issue buttons, the search bar. On desktop there's enough place to do this on one row, for mobile it isn't, currently it was using for each item a new row. This commits fixes that by only giving the searchbar a new row and have the other two buttons on the same row.
- The notification table will now be show a scrollbar instead of overflow.
- The repo buttons(Watch, Star, Fork) on mobile were showing quite big and the SVG wasn't even displayed on the same line, if the count of those numbers were too high it would even overflow. This commit removes the SVG, as there isn't any place to show them on the same row and allows them to have a new row if the counts of those buttons are high.
- The admin page can show you a lot of interesting information, on mobile the System Status + Configuration weren't properly displayed as the margin's were too high. This commit fixes that by reducing the margin to a number that makes sense on mobile.
- Fixes to not overflow the tables but instead force them to be scrollable.
- When viewing a issue or pull request, the comments aren't full-width but instead 80% and aligned to right, on mobile this is a annoyance as there isn't much width to begin with. This commits fixes that by forcing full-width and removing the avatars on the left side and instead including them inline in the comment header.

---
## [CHEMAMET/Supervised-Learning-Decision-Trees-and-SVM](https://github.com/CHEMAMET/Supervised-Learning-Decision-Trees-and-SVM)@[1f4893baf1...](https://github.com/CHEMAMET/Supervised-Learning-Decision-Trees-and-SVM/commit/1f4893baf1e034d3892167aaf4b1348bed337c7b)
#### Sunday 2022-05-01 16:57:19 by Cherotich Faith

Add files via upload

Part 1: Decision trees:
For this section, you should build a model that makes the above prediction. You should not use individual decision trees, rather you should use at least 2 out of the 3 advanced models we have studied: Random forests, Ada boosted trees, and gradient boosted trees.
Try and optimize each of the models, making sure to document how you've set up your hyperparameters.
Identify which of the 2 models you trust most, and use your model to determine which features are most impactful in influencing the prediction
Note that with decision trees, you don't need to do a lot of data cleaning. This will be very different with SVM.
Part 2: SVM:
In this section, you may be required to clean the data a little bit so as to make sense of the features.
Document what transformation you've done on the data.
Apply Polynomial, linear and rbf kernel function to build your SVM model and then evaluate their performance and pick the kernel that performs the best. Remember to tune your parameters to improve the performance of your model. To make your life easier, make sure to visualize the models you've created. Use any two features to build the models for this step.
Hint: You may want to use decision trees to give you the most preferable features you can use. but also keep in mind that those features might not be suitable for SVM. It might be a good idea to graph them first.

After getting your best performing kernel, use this kernel together with your tuned parameters and repeat the prediction but this time using additional features. Compare the model you've just created with the 2-features version.

1.1 Defining the Research Question
a) Specifying the Question
The research question is to use the given variables to build a model to predict whether or not a patient has hypothyroid.

b) Defining the Metric of Success
This project will be successful when:

1)We Identify the most crucial independent variables that affect Hypothyroidism.

2)The model achieves atleast 80% accuracy

3)Have the lowest RMSE score possible

c) Understanding the context
The context of this data set is in a medical domain. As a data scientist approached by Nairobi Hospital, my job is to look at the different features provided and use them to determine whether or not a patient has hypothyroid.

Hypothyroidism (underactive thyroid) is a condition in which your thyroid gland doesn't produce enough of certain crucial hormones.

Hypothyroidism may not cause noticeable symptoms in the early stages.

Over time, untreated hypothyroidism can cause a number of health problems, such as obesity, joint pain, infertility and heart disease.

Hence the need for early detection.

Hypothyroidism may be due to a number of factors.

Risk factors Although anyone can develop hypothyroidism, you're at an increased risk if you:

Are a woman

Are older than 60

Have a family history of thyroid disease

Have an autoimmune disease, such as type 1 diabetes or celiac disease

have been treated with radioactive iodine or anti-thyroid medications

Received radiation to your neck or upper chest

Have had thyroid surgery (partial thyroidectomy)

Have been pregnant or delivered a baby within the past six months

d) Experimental Design
Data cleaning & preparation

a) loading libraries and data set

b) remove missing values & duplicates

c) remove and/or rename columns where necessary

d) change data type where necessary

Exploratory Data Analysis

a) univariate analysis

b) bivariate analysis

Modeling

a) Decision Trees

Carry out feature engineering & selection

Split data into train & test sets

Use random forest, Ada Boost, and/or Gradient Boost

Visualize the decision trees created

Optimize the models

Select the model you trust most (random forest, ada boosted forest, gradient boosted forest) & identify the most impactful features

b) Support Vector Machines

Clean data & document

Apply polynomial, linear, & rbf kernels

Evaluate kernel performance & select best-performancing kernel

Use tuned hyperparameters on best kernel to make predictions

Conclusion

Dataset
Dataset Files

Source [http://bit.ly/hypothyroid_data]

Dataset Columns
Age

Sex

on_thyroxine

query_on_thyroxine

on_antithyroid_medicationthyroid_surgery

query_hypothyroid

query_hyperthyroid

pregnant

sick

lithium

goitre

TSH_measured

TSH

T3_measured

TT4_measured

TT4

e) Appropriateness of the Data
After going through the data set, I can confidently say that it is not appropriate for effectively answering the research question. For starters, it has way more observations of those whose status is negative than those who actually have hypothyroid. It also has way more female patients than males, and most of the patients are within the 40-60 age range. Furthermore, there was a lot of missing data which had to be imputed, meaning that the new and cleaned data set might not have accurately reflected reality. So this data set is very highly biased and not appropriate.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6471ac26d0...](https://github.com/mrakgr/The-Spiral-Language/commit/6471ac26d04fb526f0439b04cb4953dff6e9516b)
#### Sunday 2022-05-01 17:12:40 by Marko Grdinić

"9:20am. Let me get started. I am eager to try out Retopoflow.

12:50pm. Done with breakfast and chores. I've been doing retopology all this time.

12:55pm. I can't really grasp the essence of edge flow. I want a bit more practice. I need to find a way of organizing it that makes sense to me.

1:30pm. I don't get this shit at all.

1:35pm. The quad remesher is just so bad at obeying material boundary constraints. I get all sort of nasty shit in the corners. But the overall topolgy is not bad at all. It certainly looks cleaner than my own.

1:45pm. This is such a waste of time. I need to pause.

Do I have to do the review?  Let me short one.

///

I've been working on a desk model and that has led me to an adventure of picking up all sort of things. Substance Painter & Designer, Moi 3d, Zbrush. Blender addons like Hops, MESHmachine and now Retopoflow. I spent a lot of time watching tutorials. I feel like my skillset is fairly broad if shallow right now. I need to get practice instead of touring the landscape. Right now, mesh topology is kicking my ass, but I'll get through it. So far, I am 7 months into the my 3d art journey. The way it has been going on is that I'd find a subject of interest, get moderately proficient at it and then leave to do something else. Because I am constantly moving from what I am good to what I am bad from the outside it seems like I am a permanent beginner, but should get over that before long. I think I've covered all the major art programs at this point apart from Marvelous Designer which I might not even need.

Hopefully, by the end of the month I should be able to dealing with modeling my room which will allow me to move on to more interesting things.

So far, I haven't found this boring, but I am afraid for time. Should I really be doing art when I am a programmer? Should I be pursuing AI like I have before? Is this all a waste of time?

It is a slow period. Right now we are at a boring juncture when the new AI hardware wave is on the horizon, but hasn't quite gotten here yet. I got into programming back in 2015 because I thought that after I've gotten good at current techniques I'd be able to make something decent, but since I couldn't my interest towards GPUs and deep learning is at an all time low. There is no point in pushing it. Deep learning will hardly be the last word in AI and something will come along to rekindle my interest. There are 10k neuroscientists in the world, and surely they'll come up with something good given enough time.

So I can afford to take it easy for a bit before getting my hands on that hardware.

If you are a company making or using novel AI hardware, and want to add functional programming to your toolset, consider checking out [Spiral](https://github.com/mrakgr/The-Spiral-Language) and sponsoring a backend for it. Though please, no more GPUs. They were interesting last decade, but they are old now.

///

This is good enough.

2:25pm. I simply do not feel like doing much more. I doubt people care about me reviewing Moi.

I've been focusing so hard on placing vertices that I have a slight headache right now.

2:25pm. It is super annoying how you can't rotate using shift plus number keys in retopoflow.

3pm. I give up. This is not working for me. It would have far, far faster to just redo the model using the box modeling style and then project it onto the original one. What is happeing now to me is beyond ridiculous. I have no idea what I am doing. I am not sure I even need to retopo the monitor. Do the distortions it has even matter?

https://www.youtube.com/results?search_query=retopology

Let me watch some of these.

https://youtu.be/IihK5bFZSz8
This Technique is Ridiculously Overpowered! | Retopology Masters 11

https://youtu.be/026bDGQYYqc
Zbrush - Fast ProBoolean and Nurbs Retopology

https://youtu.be/026bDGQYYqc?t=403

For him the results are good.

4:10pm. I am done. After how many days of this, I've decided that I don't need retopology. What I did was quad remesh it to 100k faces. That gave a good result. Then I went over it with the red matcap to see if I could see any shading artifacts. I could not compared to the original.

That confirms it that there is nothing wrong with my model. What I did was planar decimate it with an 0.1 degree angle and then triangulated it.

4:10pm. Touched up the back part.

Right now I have a strong headache from all the zoning that I've been in.

The main reason why I wanted to do this was to understand what good topology is. But I've been too arrogant. I am not better than the subdiv modifier.

I am bashing my head trying to understand what is wrong with triangles and poles, but in the end, just like with that cylinder, the way to deal with them is to add some extra bits for edge control. If I want all quads, that is easy, just subdivide and you'll get that all quad topology either way.

The edge work that I did on the monitor was just too hard for the quad remeshers to deal with.

Retopoing the model seemed like a good idea initially, but lowering the face count will always lower the quality. I thought that with better tools I'd be able to get a higher level of precision, but with Retopoflow I am always dragging points by hand. This is a far cry from the precise placement of faces by the subdiv modifier.

Whether it be me, the Zremesher or the Exoside one in Blender, it is impossible to capture the elegance of the original model. Let this be a lesson to me.

I am not going to try retopology again unless I have a concrete reason to do so.

Now...

https://www.youtube.com/c/Arrimus3D/search?query=retopology

Right now I am too tired to plonk the thing into Substance, so let me watch some of these. I want to understand the subject of topology better. Tomorrow I'll wrap up the monitor, put into the Clarisse scene, and then move on to the rig.

https://youtu.be/yQ6huO0AF8Q
Retopology Masters #1 - Settings

https://youtu.be/yQ6huO0AF8Q?t=990

I am watching him do this and wondering how the quad remesher would handle it. Why don't I give it a try?

5:15pm. Decided to stop for a bit so I could do the chores. Let me get back to playing around. The quad remesher works differently than the Max one. It does seem like it does not need an explicit subdivision step before it is hit.

Yeah, the quad remesher might be nice, but it also requires even quads to really work well. Otherwise the small details will get paved over. That is why I could not get it to preserve the edges. Now...

Let me just do some investigation on the subdiv. What happens when it splits a trinangle?

5:30pm. Ok, I see. The subdiv is made for more than just quad. Triangles and ngons are a part of the modeling process, and I should master their use. So far I keep hearing poles bad, but until I figure out why that is, I should just ignore that advice.

Trying to retopo a completed subdiv model by hand is just spew. The elegant curvature would be wrecked. There is no point to it.

https://youtu.be/NEM6-od1k34
HUGE Polygon Fillets with Smooth Boolean

Now I am just watching random stuff.

5:55pm. https://youtu.be/FdXf2Kq6s4I
Retopology Masters #2 - Basic Uses

I could call it a day now, but let me watch this just for leisure. It might have something interesting to me here. I am into retopo right now so I might as well go for it.

https://youtu.be/FdXf2Kq6s4I?t=425

This is how I did the monitor. Interesting way of modeling. It is fairly freeform since you can make cuts and such.

https://youtu.be/FdXf2Kq6s4I?t=472

I wish he'd go into detail what is wrong with this topology. He says it would need a lot of fixing, but why?

https://youtu.be/FdXf2Kq6s4I

This has all the same issues as the monitor except in larger number. Now that he put on the retopo modifier he wrecked everything. What is he going to do to get back to the original result?

https://youtu.be/FdXf2Kq6s4I?t=687

He says it looks just as good as if he did it manually.

But as a result all the edge work is wrecked and the visual appeal is far lower. It is not worth reducing the poly count by 10x just to get this.

https://youtu.be/FdXf2Kq6s4I?t=778

These swift loops are cool. I haven't seen a feature like them in Blender.

https://youtu.be/f0OWJnCGCSc
Frequently Asked Questions on Topology

This caught my eye.

> Why are trinagle bad, why are ngons bad...

Seems like my kind of video. This is exactly what I wanted to hear. Topology guides had that deformation example, but I am not buying it.

https://youtu.be/f0OWJnCGCSc?t=54

It seems subdividion is important because the camera would subdivide based on distance.

https://youtu.be/f0OWJnCGCSc?t=77
> If you guys want to work on video games, topology is not as important to you.

https://youtu.be/f0OWJnCGCSc?t=627

Yeah, but as a result you lose detail. If it is clothing, maybe you want pinching.

6:45pm. https://youtu.be/GSnQAh8SxUQ
Retopology Masters #3 - Clean Spline Modeling

Let me close here, these vids are just making my headache worse. It is time to unwind. I have to close before 10pm at some point. My usual rule was to close at 6pm. I've been breaking that compulsively in recent time. By that I mean since I started my art journey.

https://youtu.be/f0OWJnCGCSc
Frequently Asked Questions on Topology

Let me plug this again. The video had a lot of nuance to it, and he would use trinagle and ngons depending on the circumstance.

I'll go with the rule of going with what looks good and not think about it any further. I don't want to spend any more time on this.

7pm. Tomorrow, I am showing the model into Substance and moving on to the rig after that. I should not spend much time on Substance as I just need to put in the samsung logo and some tiny icons on the top. In fact, it might be good to do these as separate objects so I do not waste texture space. The monitor is uniform balck so it is pointless to much work.

Hmmm, to get room for that decal instead of using a separate object, it might be worth it...

Actually, why don't I use a separate object and just project it to the surface? Who wants to mess with separate UV sets. It would be a nightmare to modify topology just to do this.

Yeah, this is good. I am finally thinking how to get rid of this obligation.

As per plan, I'll do the rest of the room in Moi as it would be the easiest to do it in that.

7:10pm. I am going to get nearer to the conlussion of all of this find my workflow. Just like with programming, I am not looking to work for anybody else, I just want to do what I want and sustain myself through that. Life is long, and the few years until AI hardware become commonplace are also long. So I should spend that time constructively."

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[614bf05b40...](https://github.com/NetBSD/pkgsrc/commit/614bf05b4085f0cfb256be411ca24874562f8402)
#### Sunday 2022-05-01 17:25:11 by mef

(textproc/R-readr) Updated 2.0.1 to 2.1.2

# readr 2.1.2

* `read_table()`, `read_log()`, and `read_delim_chunked()` (and
  friends) gain the `show_col_types` argument found elsewhere. All
  `read_*()` functions now respect the `show_col_types` argument or
  option, even when using the first edition parsing engine (#1331).

* `show_progress()` uses `rlang::is_interactive()` instead of
  `base::interactive()` (#1356).

* `read_builtin()` does more argument checking, so that we catch
  obviously malformed input before passing along to `utils::data()`
  (#1361).

* `chickens.csv` and `whitespace-sample.txt` are new example datasets
  accessible via `readr_example()` (#1354).

# readr 2.1.1

* Jenny Bryan is now the maintainer.

* Fix buffer overflow when trying to parse an integer from a field
  that is over 64 characters long (#1326)

# readr 2.1.0

* All readr functions again read eagerly by default. Unfortunately
  many users experienced frustration from the drawbacks of lazy
  reading, in particular locking files on Windows, so it was decided
  to disable lazy reading default.  However `options(readr.read_lazy =
  TRUE)` can be used to set the default to by lazy if desired.

* New `readr.read_lazy` global option to control if readr reads files
  lazily or not (#1266)

# readr 2.0.2

* minor test tweak for compatibility with testthat 3.1.0 (#@lionel-, #1304)

* `write_rds()` gains a `text=` argument, to control using a text
  based object representation, like the `ascii=` argument in
  `saveRDS()` (#1270)

---
## [der-lyse/newsboat](https://github.com/der-lyse/newsboat)@[fc4a2205b7...](https://github.com/der-lyse/newsboat/commit/fc4a2205b71885b6cf19ff9a50993cae568308cf)
#### Sunday 2022-05-01 17:46:50 by Lysander Trischler

Remove trailing whitespace

Trailing whitespace is not harmful, but unnecessary and ugly in my
opinion. I configured my editor to highlight it, so I see it all the
time, which is a bit annoying. Let's get rid of it.

Actually regenerating the filter produces some slightly different code
with my installed version of cococpp (Coco/R Jan 02, 2012), so I just
kept the old code and removed the trailing spaces and tabulators.

`make fmt` now also removes trailing whitespace from all the text files.
Since not only source files but any text files might be subject to
introducing new trailing whitespace, CI will not skip that formatting
task anmyore for documentation-, translation-, contribution- and/or
snap-only changes. It's not executed unconditionally all the time.

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[a0fa5ba3ce...](https://github.com/Nerev4r/Skyrat-tg/commit/a0fa5ba3ce25d019dafa88e1d606e079f7649cc6)
#### Sunday 2022-05-01 20:31:27 by SkyratBot

[MIRROR] Updates Maps And Away Missions MD [MDB IGNORE] (#13095)

* Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

* Updates Maps And Away Missions MD

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [lgritz/oiio](https://github.com/lgritz/oiio)@[594776d9c6...](https://github.com/lgritz/oiio/commit/594776d9c617ab05b3cf0ff17d69dff908c1ae7e)
#### Sunday 2022-05-01 20:31:44 by Larry Gritz

Speed up case insensitive string comparisons (#3388)

Oh boy, never leave anything unbenchmarked.

Turns out the boost::algorithm functions we were relying on underneath
many Strutil "case-insensitive" comparisons were ridiculously slow.
We thought they were good enough because they allowed specification of
locale, so we could just pass the static classic locale, and so they
would be inexpensive because they didn't have to query the current
locale.  But this is wrong, they were still ghastly.

So here I rewrite Strutil::iequals, iless, starts_with, istarts_with,
ends_with, iends_with in terms of a new (internal) Strutil::strcasecmp
and strncasecmp (which underneath handle differences in platform, and
use the locale-independent versions). The net result is that most of
those case-independent comparisons speed up by a factor of
50-100x. Wow.

I still need to tackle the family of 'ifind' related functions. They
are a bit trickier. But I'll leave them for another time, because I
need to roll this present fix out right away to fix a real production
bottleneck.

(Worth noting: iequals is instrumental when you're searching a
ParamValueList for a particular name, which is what happens when you
look up attributes from an ImageSpec, which is what happens when you
call get_texture_info(), which is what underlies OSL gettextureinfo()
calls in the cases that they cannot be constant-folded during runtime
optimization. So this came to my attention when analyzing a slow scene
whose shaders had a pathological explosion of gettextureinfo calls that
couldn't be optimized away.)

---
## [PopFlamingo/swift-nio](https://github.com/PopFlamingo/swift-nio)@[d62c733653...](https://github.com/PopFlamingo/swift-nio/commit/d62c733653ae5388a0f9d47025c983a0c3165682)
#### Sunday 2022-05-01 20:45:47 by Cory Benfield

Extract PriorityQueue to its own module. (#1932)

Motivation:

I'd like to move EmbeddedChannel and friends out of the main NIO
repository and into their own module. Unfortunately, EmbeddedChannel
shares the PriorityQueue implementation we wrote with the various POSIX
channels. To avoid duplicating the code, we should pull it out to its
own module.

However, we've never wanted to commit to the API of this data structure,
and the same is true now. To that end, I'm pulling it into an
underscored module that is not a product of the package.

We could have used the `@_spi` annotation here but honestly I'm a bit
nervous about doing that at the low-level of NIO itself, as if the Swift
team does change the spelling of it at any point in the future we'll be
in real trouble. This way works almost as well, and makes our intent a
lot clearer.

Modifications:

- Extracted Heap and PriorityQueue to a new module.
- Made everything @inlinable to do our best to make performance
  acceptable.

Result:

We can re-use PriorityQueue.

---
## [ExpHP/truth](https://github.com/ExpHP/truth)@[93b985269d...](https://github.com/ExpHP/truth/commit/93b985269dd714f7a7cabd73ac7fe91a22d9c898)
#### Sunday 2022-05-01 20:57:39 by Michael Lamparski

add --output option to decompilation

Somebody is having trouble with decompilation producing mojibake
in the output file.  I think > for output redirection might not work
so well on CMD. (maybe '>' does ANSI? maybe rust is writing UTF-8 to
the ANSI APIs? I don't know. First let's find out if this even works!)

An --output option should resolve this problem by making text encodings
a non-issue (the OS must assume we're writing binary).  And honestly,
not having it just feels assymetric compared to compilation, so it
should be there anyways.

---
## [bellegarde-c/android_kernel_gnumdk_sm8150](https://github.com/bellegarde-c/android_kernel_gnumdk_sm8150)@[4239d5c977...](https://github.com/bellegarde-c/android_kernel_gnumdk_sm8150/commit/4239d5c9777ff5477473fc3d156d6ea61f2aae0c)
#### Sunday 2022-05-01 21:22:04 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: Zlatan Radovanovic <zlatan.radovanovic@fet.ba>

---
## [Vetpetmon-Labs/Wyrms-of-Nyrus](https://github.com/Vetpetmon-Labs/Wyrms-of-Nyrus)@[7825f1fb59...](https://github.com/Vetpetmon-Labs/Wyrms-of-Nyrus/commit/7825f1fb59aac8fc3e66072b5cca82417fc1c58f)
#### Sunday 2022-05-01 23:02:12 by Vetpetmon

OH MY FUCKING GOD WHEN ARE YOU GOING TO WORK PROPERLY.

---

