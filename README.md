## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-26](docs/good-messages/2022/2022-05-26.md)


1,785,810 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,785,810 were push events containing 2,808,625 commit messages that amount to 185,933,858 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [Lucas7yoshi/fivem](https://github.com/Lucas7yoshi/fivem)@[02df4a52b1...](https://github.com/Lucas7yoshi/fivem/commit/02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9)
#### Thursday 2022-05-26 03:05:16 by blattersturm

tweak(client/core): nvidia, fuck you.

Apparently ba693365d151cb3d61e1fd1bc08f9f65f66d13ae wasn't enough to fix
the .toc corruption from nvPSShaderDiskCache.cpp/the NvShaderDiskCache
perf strategy.

Instead, this change just disables the shader cache entirely. Using a
hacky way.

---
## [Lucas7yoshi/fivem](https://github.com/Lucas7yoshi/fivem)@[6051b8790c...](https://github.com/Lucas7yoshi/fivem/commit/6051b8790c185b2435da75c2f41f59ec3be4578f)
#### Thursday 2022-05-26 03:05:16 by blattersturm

Revert "tweak(client/core): nvidia, fuck you."

The gift that keeps on giving: NVIDIA drivers. Some users seem to crash
in new places with `disable.txt` present and used.

Seriously?!

This reverts commit 02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[ed6a292644...](https://github.com/crawl/crawl/commit/ed6a29264452cc4126f7b10dd71d160c275365d9)
#### Thursday 2022-05-26 03:21:05 by Nicholas Feinberg

New species: Star

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species! Stars
have an exciting variety of bonuses - good attributes and
aptitudes across the board, passive mapping, damage shaving (ala
Deep Dwarves), and eventually innate MP and HP regen. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Stars are humanoid beings. (In the night sky, they look like
  dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Stars' LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- A future commit will make stars shine.

---
## [francinum/Pariah-Station](https://github.com/francinum/Pariah-Station)@[c77fb1e795...](https://github.com/francinum/Pariah-Station/commit/c77fb1e7959bec41276673ba903da1625be8b68e)
#### Thursday 2022-05-26 03:51:52 by Octus

Parallax but better: Smooth movement cleanup (#66567) (#724)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [SabreML/Pariah-Station](https://github.com/SabreML/Pariah-Station)@[23aef65ad5...](https://github.com/SabreML/Pariah-Station/commit/23aef65ad58754e8327151ece4c0efa6d810e1ed)
#### Thursday 2022-05-26 04:01:02 by SabreML

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607) (#704)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[95db2c6bfc...](https://github.com/pariahstation/Pariah-Station/commit/95db2c6bfc84871f2fa51eeef253f681dc46a632)
#### Thursday 2022-05-26 04:02:34 by Kapu1178

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301) (#696)

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

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [Mu-L/hhvm](https://github.com/Mu-L/hhvm)@[648c963897...](https://github.com/Mu-L/hhvm/commit/648c963897f25839c9d1697939acaf8762a64978)
#### Thursday 2022-05-26 04:39:39 by Lucian Wischik

mitigate HackIDE:idle messages

Summary:
There are two separate things going on with this diff. Both are prompted by a user repro where the progress-message "[HackIDE:idle]" keeps popping up.

**Fewer IDE_IDLE**. The behavior of hh_server is, if it receives an RPC from clientLsp, then it must receive a subsequent IDE_IDLE message from clientLsp before it will do any typechecking. It does this because it takes ~1s for hh_server to wind down a typecheck and then start one up again, which made things clunky and slow when you were doing a lot of typing and interrupting a typecheck with every keystroke you made. The design is that IDE_IDLE only gets sent after the LSP queue has been emptied.

We had accidentally gotten this code wrong at times, so that sometimes the IDE_IDLE message didn't get sent and hence hh_server got permanently stuck, but that seems to have been fixed for a year or more. The final robust design was that for every single event (other than "tick" meaning no-event), then clientLsp would believe it needed to send IDE_IDLE.

This became a bit inessential with clientIdeDaemon, where we'd send IDE_IDLE even after clientIdeDaemon had handled a hover request all by itself, but wasn't too bad.

It became downright frustrating with streaming-IDE-errors, where hh_server sends error updates while a typecheck is underway. Every single one of these counted as an event, which prompted the catch-all robust design to think it needed to send an IDE_IDLE, so it did, which caused hh_server to interrupt then restart its typechecking for ~1s to deal with this message. DOH!

This diff changes clientLsp so that we only think we need to send IDE_IDLE after having sent some kind of message to hh_server (apart from sending IDE_IDLE to hh_server).

**Unclear status**. When hh_server received and processed IDE_IDLE, then it would update progress.PID.json accordingly, and the command-line hh_client would display the progress message [HackIDE:idle]. But then it takes ~1s for bulk typechecking to resume, we're not going to display any progress message until it does, so users just see [HackIDE:idle] even when they know there's a lot of typechecking to do and they just wish it would get on with it. This is confusing to us on the hack team, and to users.

This diff makes a minor change. It now displays [HackIDE:idle] while it embarks upon handling this request, and [HackIDE:idle done] after it's finished. In this way, we on the hack team will at least know that the "idle" command-handling is done, and what we're witnessing is the ~1s it takes to resume after the interruption.

(I think it's good that users and we on the hack team will know WHICH interruption is the cause for the ~1s resumption that we're seeing.)

Did all these interruptions cause actual slowness in overall typechecking time? -- not that I could reasonably measure, not within the bounds of noise.

Reviewed By: CatherineGasnier

Differential Revision: D36392047

fbshipit-source-id: 245f22eb33e9aeb034f8a7a193f3c941ed257610

---
## [Musketeer-Chess/Fairy-Stockfish](https://github.com/Musketeer-Chess/Fairy-Stockfish)@[57bda214fc...](https://github.com/Musketeer-Chess/Fairy-Stockfish/commit/57bda214fcc8cd9d40fd3fd6f43c766ac9f88662)
#### Thursday 2022-05-26 04:58:31 by Snowmoondaphne

Update variants.ini

I'm really sorry to tell you this,,,

The positions of Black's Queen and Cardinal have been swapped in Pandemonium. Therefore, the definition has changed and it is necessary to modify it

[pandemonium]
variantTemplate = shogi
pieceToCharTable = PNBRFSA.UV.++++++++.++Kpnbrfsa.uv.++++++++.++k
maxFile = 9
maxRank = 9
pocketSize = 9
startFen = rnbsksbnr/2+f1+u1+a2/p1p1p1p1p/4v4/9/4V4/P1P1P1P1P/2+F1+U1+A2/RNBSKSBNR[] w - - 0 1
customPiece1 = o:NA
customPiece2 = s:WF
customPiece3 = u:D
customPiece4 = w:DWF
cast = false
pieceDrops = true
capturesToHand = true
immobilityIllegal = true
soldier = p
knight = n
bishop = b
rook = r
king = k
queen = q
commoner = g
dragonHorse = h
bers = d
alfil = a
archbishop = c
chancellor = m
fers = f
wazir = v
centaur = t
promotionRank = 7
promotedPieceType = p:g n:o b:h r:d a:c v:m f:q s:w u:t
doubleStep = false
perpetualCheckIllegal = true
nMoveRule = 0
nFoldValue = loss
stalemateValue = loss

Could you please modify the definition like this?

Sorry again for the troublesome request,,,

---
## [swuff-star/LostInTransit](https://github.com/swuff-star/LostInTransit)@[0b22404831...](https://github.com/swuff-star/LostInTransit/commit/0b22404831fc891591fb87749bb9e522aba440b0)
#### Thursday 2022-05-26 05:06:19 by Nebby

I'd fuck a Qu from all tomorrows, my life is worthless anyways

---
## [Michaelleojacob/waldo-with-backend](https://github.com/Michaelleojacob/waldo-with-backend)@[cd5f81bcdf...](https://github.com/Michaelleojacob/waldo-with-backend/commit/cd5f81bcdffa979636c3d2d08088e8928b8cc9e5)
#### Thursday 2022-05-26 05:53:34 by mig

I can add data to firestore holy shit

turned out my .env was incorrect. So my app couldn't get ahold of my firebase/firestore. I needed to add REACT_APP_ to each of my .env variables.

changed the firebase rules a ton of times thinking the rules were the issue. turned out to be .env though

---
## [skepfusky/skepfusky.xyz](https://github.com/skepfusky/skepfusky.xyz)@[9c7fc75d7b...](https://github.com/skepfusky/skepfusky.xyz/commit/9c7fc75d7b57c97959aeb9641a8ffcaeac06f72f)
#### Thursday 2022-05-26 06:43:43 by Kerby Keith Aquino

Listing stuff from static generated stuff lole

HOLY SHIT IT WORKS

that stupid one line goddamn

---
## [ethan-xd/ethan-xd.github.io](https://github.com/ethan-xd/ethan-xd.github.io)@[cbf8952c66...](https://github.com/ethan-xd/ethan-xd.github.io/commit/cbf8952c6684ae6b82b163d84603418657a3e4bd)
#### Thursday 2022-05-26 07:29:46 by Ethan

facebook defeated again fuck your ads bitch fucker

---
## [Loovemaker/Set-Card-Game.swiftpm](https://github.com/Loovemaker/Set-Card-Game.swiftpm)@[3858059396...](https://github.com/Loovemaker/Set-Card-Game.swiftpm/commit/38580593965e6f2d9d324145e79e2260423002ac)
#### Thursday 2022-05-26 08:20:59 by Loovemaker

Add license:
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[357b4ca002...](https://github.com/treckstar/yolo-octo-hipster/commit/357b4ca0022a10ee1961f0541105ffe866f0f323)
#### Thursday 2022-05-26 09:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [DAVTOURS/7-Things-you-should-not-miss-on-a-safari-in-East-Africa](https://github.com/DAVTOURS/7-Things-you-should-not-miss-on-a-safari-in-East-Africa)@[ddb864ce3d...](https://github.com/DAVTOURS/7-Things-you-should-not-miss-on-a-safari-in-East-Africa/commit/ddb864ce3d1f8c71d57accdb97f82e56e16a8105)
#### Thursday 2022-05-26 09:40:26 by Dav Safaris

7 Things you should not miss on a safari in East Africa

7 Things you should not miss on a safari in East Africa
 
East Africa is a magical place with some of the best safari experiences on the continent that will leave you breathless. The region offers incredible wildlife encounters and scenic landscape views ranging from mountains, and lush tropical forests, to the big five wonders and great apes. 
Words can’t do justice to the magnificence of the Safari experiences in East Africa. We dedicate this post to giving you the top most popular adventures you can have in Kenya, Uganda, Tanzania, and Rwanda.

1. Big five game viewing safaris
The big five animals, lion, elephant, leopard, buffalo, and hippo, are Africa’s most incredible wildlife and the main reason many tourists come to East Africa for safari holidays. The big five earned their name in the 20th century with wealthy big-game hunters from Europe who found it challenging to gun down these beautiful animals. 

Today the big five are the biggest names in conservation and tourism. Seeing the Big 5 African animals living wild and free in their natural habitats is one of the best safari experiences in East Africa. Although they still face cruel threats from poachers, the big five roam freely in some of the best safari reserves in East Africa.

A well-planned short safari combination to see the big five (and much more besides) in Kenya would be the Masai Mara (for lion, buffalo, leopard, and elephant) and Lake Nakuru National Park (for black and white rhino). You can also have Big five safari experiences in Kenya in Tsavo East, Tsavo West, Laikipia Plateau, Amboseli, Samburu-Buffalo Springs-Shaba, and Meru. 
 
You’ll visit Serengeti and Ngorongoro Conservation Area when you travel to Tanzania for the big-five experience. Serengeti gives the added excitement of witnessing the epic Great Migration as well. Watching the rhinos in the Ngorongoro Conservation Area is extra special because they are confined to the Crater area, making sightings of these shy creatures even easier.

In Uganda, you’ll drive through Murchison Falls National Park to spot the big five. And in Rwanda, your Big five experiences will happen only in Akagera National Park in the extreme northeast.

2. Wildebeest migration safaris
Watching and following the Great Migration is one of East Africa’s safari experiences that no die-hard safari lover should miss. The spectacle is arguably wild Nature’s greatest show, with millions of wildebeest, gazelle, and zebra, traversing across the Serengeti in Tanzania and Maasai Mara in Kenya. 

Naturally, ferocious predators follow the herds for an easy meal, making for exhilarating wildlife experiences. The migration storms forward no matter the obstacles along the way, so it’s survival of the fittest.

The animals collectively travel across the savannah plains following the rains and searching for greener pastures. Although it’s not a set route, the beasts follow roughly the same yearly pattern. 
 
The migration experience has become the postcard picture of East Africa. Think vast open savanna plains flooded with wildlife and flat-topped bushes on the horizon against the signature red African sunset.

The best safari experiences in East Africa, watching and following the Great Migration, are best in Masai Mara. Here, you’ll watch the beast herds struggle to cross the Mara River from Serengeti into the Maasai Mara National Reserve and back into Tanzania. From here, they make their way toward the Serengeti National Park, the ideal location to watch the birth of the beasts. 

3. Climbing Mount Kilimanjaro
Climb to the roof-top of Africa and experience East Africa’s picturesque landscape from the sky on the continent’s highest mountain, Mount Kilimanjaro (Uhuru Summit (5,895 m)). You do not have to be an experienced mountain climber to conquer Kilimanjaro. You do not need mountain climbing equipment but a good pair of hiking boots and determination to climb to the top.

However, it would be best if you didn’t assume that the climbing mount Kilimajaro experience is a walk in the park. It is a grueling climb under often trying weather conditions on uneven terrain while being exposed to the elements. But the overwhelming sense of achievement and incredible views from the summit will be one of your best safari experiences in East Africa. 
 
Get into Kilimanjaro a day before the climb, settle in at your hotel, and get a briefing. The climbing experience starts early in the morning amid banana plantations on Kilimanjaro’s heavily cultivated lower slopes. The most popular Kili hiking trail passes through dense rainforests and alpine meadows, crosses a barren lunar landscape, and ascends a slippery slope to the peak, revealing breathtaking views over the plains far below. 

There are more than eight possible hiking trails. Selecting the best depends on what terrain you can handle, your acclimatization profile, the scenery, and the cost of the experience.

It can take at least 5-10 days to Uhuru Summit and back with a budget of at least $1600. The price can include entry fees, guides, rangers, porters, and a cook. Unfortunately, you cannot go on your own; you must be accompanied by a ranger and guide from the park headquarters. 

Book your experience with Dav Safaris Ltd or with the many operators in Arusha and Moshi. Encounter will manage your accommodation, gear, guides, and everything else.

4. Mountain gorilla trekking in Uganda or Rwanda
Mountain gorilla trekking in Uganda and Rwanda’s rainforests is undoubtedly one of the best safari experiences in East Africa. Mountain gorillas are one of the most endangered animals on the planet. As few as 1000 live in a small East African region; being close to these magnificent primates is one of life’s most rewarding experiences.

Mountain gorillas live only in mountain forests above 2000 meters in two populations around the Great Rift Valley. One population occupies the misty forest slopes on the Virunga Volcanoes Mountains that straddle the Uganda, Rwanda, and DR Congo borders. The second population of gorillas was cut off from the bigger bunch because of human settlements and lives in Uganda’s Bwindi Impenetrable National Park.
 
You cannot mention the best safari experiences in East Africa and not include the gorilla trekking experience because of its direct involvement with wildlife and community conservation. The gorilla trekking experience highly depends on the communities surrounding the protected areas and the conservation efforts by governments where they live and dedicated wildlife conservation organizations. A gorilla trekking trip is a huge contribution to the sustainable programs that protect the endangered apes within their natural habitat. And what better way to travel than to travel for the good of nature conservation.

There are only two airports you can fly in to track the gorillas; Entebbe International Airport, located about 500 km from Bwindi; and Kigali International Airport, located about 100 km from Volcanoes National Park. The two national parks offer the best safari experiences with mountain gorillas. You would need at least three nights in the country.

However, Volcanoes National Park in Rwanda offers the high-end of the budget, with gorilla permits going for $1500 per person. On the other hand, Uganda provides a more manageable budget for the experience, with gorilla tickets going for $700 per person. Accommodation at both national parks is readily available just outside the entrances offering world-class lodges to just a place to stay.

The gorilla trekking experience is extremely in high demand, meaning that you can’t just walk to the park and buy an entry ticket. The number of visitors is restricted to a few individuals per day, so you have to book months in advance to secure your permit. It’s on a first-come, first-serve basis.

To avoid bad experiences associated with local logistics, book through a trusted safari operator like Dav Safaris Ltd. They’ll secure your gorilla permit from the government, book your accommodation,  transport and manage your entire trip.

5. Chimpanzee Trekking in Uganda

  
Chimpanzee trekking in Kibale Forest is one of the most unmissable safari experiences in East Africa. Chimpanzees have for a long time been known to mimic human cultures and share the highest percentage of our DNA than any other animal. The trekking experience allows tourists to get the closest to these great apes and observe their exciting behaviors and body structures.

There are many attractions across Africa where you can get close to the chimps. Still, because Uganda has a high concentration of them and a successful conservation tourism program, your best experience with the chimps will be in Kibale National Park. The park has more than 1500 chimps, 13 other primate species, and a list of other exciting animals to encounter.

Chimpanzee trekking experiences in Kibale occur daily in the early mornings and spend almost half the day in the rainforest. Some chimpanzee groups are habituated for tourism, which means that you can spend at least an hour observing their peculiar behaviors. Other chimp groups are not fully habituated, and you can spend almost the whole day walking among them. Armed rangers and expert guides manage the excursion, allowing you to come close to the endangered primates at the most comfortable pace.

You should know that the chimpanzee experience demands moderate physical fitness, although anyone above 15 years can do it. These primates are hyper-active and swiftly move across the rainforest from 2 km to 10 km in a day. So keeping up with their movements is an active experience that will require a bit of your energy. Some exercises before booking your chimpanzee trek will be of outstanding contribution to a good experience.

A chimp permit costs $200 in Kibale Forest or less in other forests like Budongo and Kyambura Gorge. The habituation experience with the chimps for a whole day costs $250 per person. 

You basically need about three nights in the country to pull off a great experience with the chimps. You could also add the gorilla trekking experience to your trip. Gorillas are located about 350 km from the chimps in Kibale, and the two safari experiences are a great combination.

Please email us at info@davsafaris.com  to help you plan your chimpanzee trekking experience in Uganda with trusted local expertise.

6. Beach holiday in Zanzibar
Zanzibar Island was once a bustling trading center and important spice route. Today, it is one of Africa’s most tranquil and idyllic vacation destinations. Zanzibar offers serene safari experiences strolling along the soft, delicate, white sand beaches.
 
The Island’s unending miles of seashore that embrace its marine ecology is the last stop after exploring the mainland East Africa attraction. 

The Island’s lush tropical vegetation creates a vibrant, verdant contrast to the magnificence of the beaches; you can enjoy the spectacular African sunrises from the east of the Island or the golden colors of the breathtaking sunsets on the west coast. Birders will enjoy the many colorful Zanzibari birds, including the yellow-collared lovebird. 

Zanzibar is not simply a single island of the Indian Ocean but an archipelago of Unguja, Zanzibar, Pemba Island, and surrounding islands like Chapwani, Mnemba, Chumbe Bawe, Changuu, and others.

The glorious Zanzibar beaches and coral reef experiences are perfect for families and honeymooners. There is superb boutique accommodation and all the indulgences for a relaxed traveler.

7. Watching The Tree Climbing Lions 
Driving through the vast plains of Lake Manyara Park in Tanzania or Ishasha Sector of Queen Elizabeth National Park in Uganda will reward you with scenic landscape views and one of the most unforgettable safari experiences in East Africa; watching the exceptional tree-climbing lions. 
 
In Ishasha, you can watch these interesting lions atop huge fig tree branches as they keenly watch their prey of peacefully grazing impala, gazelle, and kob herds. You may catch the rare spectacle of the tree lion pouncing on the ground for a kill if you’re fortunate. 

The advantage of watching them in Isasha is that you can add the gorilla trekking experience in Bwindi (65 km) to your trip.

You can spot the other tree-climbing population of lions around Tarangire and Lake Manyara National Parks in Southern Tanzania. Their awkward, almost unnatural behavior of climbing trees with their massive weight is a sharp contrast to the excellent agility of leopards.

The sight is fascinating, and watching a 200-kg agile cat navigate the thin branches of a fig tree is one of the unique safari experiences in East Africa.

A Safari in East Africa
In Africa, there’s nowhere that you’ll get the most authentic wildlife experience than in East Africa. East Africa is a classic safari destination with seasoned experiences for all types of travelers, including you.

However, planning a safari in East Africa can be a daunting experience if you do it on your own. That’s why we are here. Dav Safaris Ltd specializes in planning and managing safari experiences in East Africa. We give you the best advice, help you plan your safari, handle the local logistics and manage your confirmed trip.

Send us an email at info@davsafaris.com  to ask for a free quote and start planning your experiences in East Africa.

---
## [darshan-/PurpOS](https://github.com/darshan-/PurpOS)@[df057ac2da...](https://github.com/darshan-/PurpOS/commit/df057ac2da643d16708d2c7374c33a1b06a2094d)
#### Thursday 2022-05-26 09:58:40 by Darshan-Josiah Barber

Cleanup.  Try PurpOS as name.  (I liked the idea of four letters before OS (just to be centered, which is silly, but what I was thinking), and I love the color purple, so I considered PurpOS, and I liked that it sounds rather like purpose (in fact, I'm saying it like purpose is spelled but not pronounced: purp-ose), and it doesn't seem to be in use by anyone else.)  At least with qemu, invariant tsc seems a no-go?  It's so confusing, and I keep reading different things about what's supported, what's contant, what's invariant.  It's clearly what I want, what any OS would want, and all current cpus seem to do it, but it 's so confusing when you can count on it.  But it seems clear that the qemu cpu (regardless of any command line options) reports itself as not supporting invariant tsc.  So I want to figure out ACPI tables and HPET.

---
## [ryota-murakami/devtools](https://github.com/ryota-murakami/devtools)@[7b8fe215c6...](https://github.com/ryota-murakami/devtools/commit/7b8fe215c6a81864e01b6950687216c61fba95f1)
#### Thursday 2022-05-26 10:36:46 by Josh Morrow

Motivation and Changes

Soft focus has been a theoretical goal of the front-end team for close
to a month at this point (although it was really just me tinkering and
thinking for the first couple of weeks). And that has produced some
results, but there's still quite a bit in motion, as well as some
unknowns. Technically, all we need to do to enable V1 of soft focus is
not onload regions upon the focus window changing (we still issue the
load command, because if we are already loaded it is a noop, and if the
backend has unloaded a portion of the recording that the user has asked
for, we need to ensure that we reload it). One thing that jumps out as
soon as you enable soft-focus is that we need more specific points to
pass for ranges to backend functions like getHitCounts. I tried just
using getPointNearTime with the focus window times, but that is no good,
because it always returns the beginning of the region, so sub-region
focus windows end up looking like windows of 0 length in point-terms.
Instead, I do a more sophisticated version of what we were doing
previously with timeline seeks:

Any time we get a timestamped point from the backend, we store it in a
sorted array in redux. Then, when the user sets the focus window, we use
that point array to approximate the point that lies near the user's
selected times. This is sometimes not very fine-grained, but here's the
elegant part: if there is stuff that matters around the area that is
being selected (for instance, analysis hits), then we will have stored
fine-grained point correlations already, and we won't be vastly off.
Conversely, if the points we have are really rough approximations, it is
unlikely that they will affect anything anyways, because the user has
not looked at anything of interest around them.

I was prepared for this to be terrible, but in my relatively limited
experience... it's pretty good? I think at the very least it is good
enough to enable it internally and poke around.

Followups:

- We should actually soft-focus analyses, but I will wait on Mark's
rewrite of the analysisManager before making that change.

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[01a6ade18c...](https://github.com/Sonic121x/Skyrat-tg/commit/01a6ade18cfcc1b79e5f5dace05c5e9c1e89b919)
#### Thursday 2022-05-26 11:07:52 by SkyratBot

[MIRROR] Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. [MDB IGNORE] (#13758)

* Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)

About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

* Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs.

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [Team-Compliance/ImmortalHearts2](https://github.com/Team-Compliance/ImmortalHearts2)@[17ad71c7a8...](https://github.com/Team-Compliance/ImmortalHearts2/commit/17ad71c7a85713f2b5472659764db230693b99a0)
#### Thursday 2022-05-26 11:14:18 by BrakeDude

Fixes: at almost max hp using items like Nail not healing half soul/black/immortal heart.
Bugs: some inconsistency with soul and black hearts turning into eachother when picking up bone hearts and immortal hearts with more than 1 bone heart (idk that's why i write inconsistent. Black heart sorting kinda pain in the ass)

---
## [Salex08/Merchant-Station-13](https://github.com/Salex08/Merchant-Station-13)@[f51ff8cdbd...](https://github.com/Salex08/Merchant-Station-13/commit/f51ff8cdbd744bf998ea669bab7e523eb023baa9)
#### Thursday 2022-05-26 11:35:32 by hamurlik

Adds simpson skintone (#138)

* Adds simpson skintone

The sign is a subtle joke. The shop is called "Sneed's Feed & Seed", where feed and seed both end in the sound "-eed", thus rhyming with the name of the owner, Sneed. The sign says that the shop was "Formerly Chuck's", implying that the two words beginning with "F" and "S" would have ended with "-uck", rhyming with "Chuck". So, when Chuck owned the shop, it would have been called "Chuck's Fuck and Suck".

Co-authored-by: EtraIV <34369281+EtraIV@users.noreply.github.com>

---
## [StephenCleary/comments.stephencleary.com](https://github.com/StephenCleary/comments.stephencleary.com)@[2484692221...](https://github.com/StephenCleary/comments.stephencleary.com/commit/2484692221096def22e4ce067166395272c888f5)
#### Thursday 2022-05-26 12:51:16 by Comment Bot

(Staticman) Eric Lynch: Final correction.  Boy, I do apologize!

Both "Task.Run" and "await Task.Yield()" were producing similar results, solving half of my problem.  The unpredictability of log message order (from ILogger) was not helping me diagnose and solve the issue.

Ultimately, I had to do the following to solve my whole problem...

In my constructor...
Create a TaskCompletionSource.
Use "IHostApplicationLifetime.ApplicationStarted.Register" to register a method that sets the result for the TaskCompletionSource (when the application truly starts).

In my ExecuteAsync...
"await" the completion of the TaskCompletionSource.
"await Task.Yield()" so that the "gotcha" in BackgroundService doesn't block the application from starting.

Previous approaches failed after about a half-dozen iterations.  After hundreds of iterations, using the new approach, and checking the boolean that backs my TaskCompletionSource (instead of my unreliable application log), I am now confident that this "magic" recipe works.

This was so much fun I wonder if it wouldn't have been easier to simply roll my own BackgroundService! 

Anyhow, thanks again for the advice of others on this thread, it was invaluable in solving many of the issues I encountered.

https://blog.stephencleary.com/2020/05/backgroundservice-gotcha-startup.html#comment-871b4370-dcf2-11ec-9ac6-0d52c0a36a91

---
## [abhishek1994-ux/-MyCloudDiary](https://github.com/abhishek1994-ux/-MyCloudDiary)@[698d6af608...](https://github.com/abhishek1994-ux/-MyCloudDiary/commit/698d6af608898c3cd7464ede75fdc5e1c115e06d)
#### Thursday 2022-05-26 14:23:44 by Abhishek Shrivastava

AWS Community Builders Directory 

So happy to be listed in awscommunity Builders Directory .

Thanks to Jason Dunn Shafraz Rahim Taylor Katherine Lacy and AWS CB Team for such an amazing initiative to connect with people and grow.

If you want to explore more about the program ,find it here : https://lnkd.in/dn7zx6Ri

AWS Community Builder Live Directory ,check out here : https://lnkd.in/dA-4V-tU

It has been a very busy year for me with managing multiple things in life while remaining a part of this program.

1) Preparing for AWS Certs and acing AWS Solution Architect Associate Certification at the first go.
2) Going through different AWS Serverless services and exploring unexplored areas like AWS DevOps services.
3) Engaging with AWS Internal different Product Teams and learning their plans on new features.
4) Also, Putting up all Practical AWS knowledge into blogs at Hashnode.

The Amazon Web Services (AWS) Community Builders program offers technical resources, mentorship, and networking opportunities to AWS technical enthusiasts and emerging thought leaders who are passionate about sharing knowledge and connecting with the technical community.

Isn't it cool and exciting on seeing all this mission & milestones ? Also, there are cool rewards for the same activities. Do check the screenshot. From getting certification voucher, goodies, AWS credits to getting an sponsored opportunity to visit Amazon Web Services (AWS) ReInvent USA event. There is lot more to add.

I am also listed under Serverless Category of AWS Community Builders Directory at https://lnkd.in/d5jdVFuP

---
## [GNUWeeb/linux](https://github.com/GNUWeeb/linux)@[07dea58b67...](https://github.com/GNUWeeb/linux/commit/07dea58b67cce6b7dd21fe0918f1849e11fb595f)
#### Thursday 2022-05-26 14:56:34 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

commit c570449094844527577c5c914140222cb1893e3f upstream.

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
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [Kordasauter/roprime-simulator.com](https://github.com/Kordasauter/roprime-simulator.com)@[717200d35a...](https://github.com/Kordasauter/roprime-simulator.com/commit/717200d35afa10279e03f398bc92cb6b6aa280b2)
#### Thursday 2022-05-26 15:03:20 by Kordasauter

Decisive battle's monsters

26/05/2022:
Has been Added :
Isle of Bios monsters
Corrupt Orc Baby
Corrupt Baby Desert Wolf
Corrupt Familiar
Corrupt Orc Warrior
Corrupt Desert Wolf
Corrupt Familiar
Corrupt Orc Zombie
Corrupt Verit
Corrupt Megalodon
The Death Ankou
Morse's Cave monsters
Weakened Morocc
Morroc Man
Morocc Necromancer
Morocc's Ghoul
Morocc's Osiris
Morocc's Archer Skeleton
Morocc's Wraith
Morocc's Verit
Morocc's Plankton
Nightmarish Jitterbug monsters
Grand Pere
Pere(Dancer)
Pere(Ukelele)
Pere(Bass)
Pere(Whip)
Jitterbug
Temple of Demon God monsters
Frost Spider
Frenzied Kasa
Mad Salamander
Brinaranea
Muspellskoll
Demigod
Morroc the Desparate
Morroc of the Genesis
Morroc of the Sabbath
Morroc Apostle Ahat
Morroc Apostle Shnaim
Flame Basin monsters
Fire Condor
Fire Sandman
Fire Frilldora
Fire Golem
Faceworm Nest Dungeon monsters
Faceworm
Faceworm Queen
Faceworm Dark
Faceworm Queen (Red)
Faceworm Queen (Green)
Faceworm Queen (Yellow)
Faceworm Larva
Sara's Memory monsters
Irene The Wise Elder
Payon Soldier (1st)
Payon Soldier (2nd)
Guard Dog (1st)
Guard Dog (2nd)

---
## [transcom/mymove](https://github.com/transcom/mymove)@[8af1f5a031...](https://github.com/transcom/mymove/commit/8af1f5a03143dce4ab3c6aa01b8772cd2f41adb9)
#### Thursday 2022-05-26 15:14:30 by Marty Boren

Very rough skeleton of move code search

after many moons of struggle, I've finally got something that
kinda works.
There's an endpoint for searching for moves.
and an office page with a search box that hits that endpoint
and drops the results in a table.

i was really struggling to get the react part of this to work without
setting off an infinite loop, so now that I've finally gotten there
i want to commit even though this is still full of debug cruft.

lots of exciting things left to do, such as:
- the moves that are returned by the endpoint are missing most of the
  stuff they should have.
- We also can't search for DoD ID
- interface for passing search info between things is inconsistent

---
## [INL/lexonomy](https://github.com/INL/lexonomy)@[8fd301ac95...](https://github.com/INL/lexonomy/commit/8fd301ac95fa531c8ac7f9ed904011d9629ed791)
#### Thursday 2022-05-26 15:33:54 by KCMertens

Rewrite dictionary indexing, entry read+write

There are a lot of changes in this commit, but most are just noise due to some added type checking.

1. The database
The database has had a refactor.
- Remove the needs_refac, needs_resave and needs_refresh columns, added needs_update as a more generic column
- Add flag column. Defaults to empty string. The flag is still kept in the XML as well (because of interop with old dictionaries and because this way we can ectract existing flags when users upload a new dictionary - assuming they conform to our way of doing things)

2. Entry creation/update
This is completely rewritten.
The core entry point is now ops.createEntry(), this is always used, whenever an entry is created or updated.
With the help of some util functions the entry is completely validated and resaved every time (because the user can do whatever they want to the xml, even completely change it).
This also makes it so that whenever any config has changed we just re-run this function for every entry and everything out of date property fixes itself.

3. Subentries
The subentry system has had some changes:
Previously:
- The subentry would be a complete instance, meaning all the subentry's xml would be contained in every parent entry.
- On load by the client, the subentry was surrounded with <lxnm:subentryParent>, which the client detected.
- On save: the <lxnm:subentryParent> was removed again and the subentry copied and saved in the database. Additionally all other parents of the subentry were updated with the subentry's new xml.
This had some limitations, most importantly all xml extraction functions (for title, sortkey, flag, etc) would also match inside subentries, because they were part of the same xml tree.

The new situation:
- XML of subentries is now removed from the parentEntry, and instead a single reference/link placeholder element is inserted before it is saved to the database.
I've chosen to re-use <lxnm:subentryParent id="..."> for this. The id attributes points to a regular entry in the database that contains the subentry. There is no difference in how a subentry is treated from a normal entry otherwise.
- Subentries can be edited separately, and the parents will never need an update unless the subentry is completely deleted.
- **The client needs an update to retrieve the subentry's xml separately**

Previously a subentry was just a specific element name/tag.
However now it is also possible to specify that the element needs a certain attribute to be considered a subentry.
This was required to support newer formats such as TEI-lex0, where a subentry is just an <entry type="relatedEntry>, which we otherwise can't differentiate from a normal <entry>.
This can be configured in the subbing page. It's possible to require just that a certain attribute exists, or require that the attribute exist and also has a specific value.

4. Flagging:
Flags are now also put in a database columnn. For the rest, there are no changes, flags are still keps in sync with the entry's XML, but this removes the need to parse every entry when loading the entry list.

5. Migration:
There is a migration script website/migrate.py which will migrate every dictionary's database schema.
Dictionaries that use one of the rewritten features (flagging, subentries) will have every entry marked as needs_update, which will run when they are first loaded.
NOTE: This is unfortunate, but the first load of the dictionary will be tremendously slow as all entries might need to be updated before the entrylist can be shown.

6. Other notes:
I've attempted to consolidate most of the entry functions.
ops.searchEntries() can search entries by their headword/searchables. It only uses and returns the IDs and Sortkeys, so results can be further used as needed.
ops.sortEntries() can sort the results of searchEntries based on collator and reverse settings
ops.readEntries() actually reads and processes the entries. It has some flags to retrieve xml, parse xml, extract plaintext title, or run xslt/html conversion (because those are heavy operations and you might not always need their result).
	The returned results are ready to send to the frontend.
	It also retrieves the entry's child- and parentEntry IDs, so returns their subentries, or - when it is a subentry itself - where it is used.

---

XML parsing is a headache - especially when cutting up larger documents, and namespace issues crop up because the declaration is lost.
ops.parse() parses xml in a straightforward manner - it pretty much ignores namespaces, and just treats a namespace as if the element or attribute was literally called "someNamespace:someElement".
This means that to match inside the result, you need to specify the namespace prefix inside the attribute/element name.

---

Importing a dictionary is also mostly rewritten because it could not handle elements being nested inside themselved, as the regex would match up wrong.
Ex:
<entry>
	...
	<entry type="relatedEntry"> <!-- actually a subentry -->
	</entry>
</entry>
would previously match up the opening tag with the subentry closing tag and horribly crash because of unbalanced tags.

---

I've also attempted to include type information as much as possible, and codified most of the configs used in the back-end.
This requires Python 3.8, but I very strongly think the developer quality-of-life we get back is worth it.

---
## [Fargowilta/FargowiltasSouls](https://github.com/Fargowilta/FargowiltasSouls)@[46801ba085...](https://github.com/Fargowilta/FargowiltasSouls/commit/46801ba0858df4151b6065a927856c5f44242278)
#### Thursday 2022-05-26 15:49:16 by terrynmuse

recovering is now rush job, cannot be removed until boss fight ends
adjusted implementation of mutant's spiraling spheres
the rings in mutant's maso p2 animation still track him while fading away
reduced increased undead miner spawn rate from mining helmet
-50% damage for all whips except leather
all summons have diminishing returns
 when over 3 minions of same type, damage decreases, max -50% nerf at 9 minions
 applies to minion shots too
 doesnt apply to stardust dragon and eater staff
 doesnt apply to summon damage that isnt from true "minions" (e.g. destroyer guns)
nerfs restored
 stardust dragon
 sdmg
 last prism
raised ml core life boost from x2 to x2.5 to compensate 1.4 power creep
buffed staff of unleashed ocean, fishrons now use local iframes
 nerfed base damage to compensate
 reduced dust a bit
buffed drakovi minion, water shot uses local iframes
removed omniscience staff
buffed big brain buster, now caps at 10 slots
fixed bbb being able to eat slots with no benefit after capping out
fixed stardust ench spawning guardian and it dying every tick when guardian toggle off
added rain ench inner tube toggle
added crystal ench effect toggles
added red riding toggle
removed huntress debug text

---
## [Chromosore/dotfiles](https://github.com/Chromosore/dotfiles)@[1095fe20b9...](https://github.com/Chromosore/dotfiles/commit/1095fe20b9687ca4a0036fd142e79c95858d45cc)
#### Thursday 2022-05-26 16:06:23 by Chromosore

nvim: Rewrite `init.vim` in lua!

Whoa, quite a huge change! (I mean, not really, but it is more a
symbolic change. It means that I'm getting in the *lua* era! (Yes, lua
in neovim has been a thing for like [insert number] years, but...))

I still haven't gotten a package manager (and I might never have one),
so I had to write my own lazy-loading framework which quickly turned
into an overgrown yet minimal package manager (that does not handle
downloading the packages). Ok, it isn't *this* overgrown: it basically
loads packages with `:packadd`, remembers which packages have already
been loaded and handles lazy-loading, with a rudimentary spec format.

Did I mention that I need lazy loading for only *1* plugin? (nerdtree)

Enough of half-joking. Even if this lazy-loading framework isn't like
*that* refined, I think it introduces an interesting separation between
*downloading* packages and *loading* packages. What I mean by this is
that this framework could be a standalone plugin that you'd use along
with like `packer.nvim` or more realistically `paq.nvim` (because packer
already provides some level of lazy-loading) to lazy load plugins that
you mark as `opt`.

Or to go even further, you could use `minpac`, which doesn't even handle
loading regular packages (it delegates this to vim8/neovim). (it isn't
really much further, it just works, because you'd need to adapt the
framework (which I should find a name because writing "the framework"
gets tiring) to search in a custom path to work with packer/paq)

Oh I should definitely make this a separate package!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[269cc1b0d3...](https://github.com/mrakgr/The-Spiral-Language/commit/269cc1b0d38533a0b2fa224448b7ac16411e6d14)
#### Thursday 2022-05-26 16:45:42 by Marko Grdinić

"8:30am. Watched some drawing perspective videos yesterday. Before I completely give up, is it possible for me to learn how to draw in perspective?

I played around with one point perspective yesterday, and there might be something to it. I learned about it last year, but I thought it was some nonsense.

I tried moving a few cubes around in Blender, importing the screenshot and to my surprise the angles line up when I draw straight lines through the center. Visually I thought the wuoldn't. It just goes to show biased my own perspective is.

https://youtu.be/4L6ZBjOS48M
Drawing perfect backgrounds with perspective rulers! | Jake Hercy Draws

I learned about perspective tools in CSP last year, but instead of being arrogant about it, I think this time I will pay attention. If I could somehow draw in 3d space directly, that would be a huge improvement in my drawing ability. I already have a feel for 3d. Let me just chill a little first.

8:50am. I am not against drawing in 3d space directly with something like a grease pencil. I could lock the camera in place and do 3d modeling without moving around. That would be a lot closer to drawing in 2d. I should consider it.

Let me just read Inglis first. I went to bed at 11am yesterday as I was so exhausted.

https://youtu.be/4L6ZBjOS48M?t=138
> Your strokes will draw automatically along the guidelines as long as the ruler is enabled.

https://youtu.be/4L6ZBjOS48M?t=209

Right now she is doing here what I want to do.

https://youtu.be/4L6ZBjOS48M?t=226

Hmmm...

https://youtu.be/EqegNrJJh3g
How to master 3D... for comics! | Jake Hercy Draws

9:20am. This video is on using 3d assets in CSP. I guess it would not be bad to get familiar with it.

9:30am. https://youtu.be/_fn9ux9bL2A?t=8
How to extract an EASY perspective grid in Clip Studio Paint!

Let me watch this as well, then I am going to give these pespective rulers and grids a try.

https://youtu.be/_fn9ux9bL2A?t=46

Hmmm, CSP has basic primitive shapes. Well, of course it would, but it never occured to me to look for them. Yeah, this is a great opportunity to get familiar with 3d in CSP. I've been thinking as just a 2d app, but that is not true.

https://youtu.be/_fn9ux9bL2A?t=158

He is going to use the cube as the basis for his perspective grid. It was not a bad idea to click on this video.

9:40am. Let me play with perspective a little. I am going to give the room a try again and see how far that gets me. This is the way to get better, you get a new tool and then try to master it. Scribbling lines would get me nowhere even if I spent years doing it.

10:25am. Yeah, this is pretty powerful. I should have been using it. But just this won't make me a good artist. But mastering sculpting to a greater degree might. So that is what I should be doing much like I pivoted yesterday.

First of all, let me try the Malt example file again. After that I'll ask the author how to open it.

10:30am. Hmmm, I just found the screenshots from my old base mesh. Looking at the face, the lips are too small. The soles of the feet are bad. The hindarm is too muscular. I got the body itself right. Well, I'll get it right next time around.

Malt.

https://github.com/bnpr/Malt/releases

Maybe I just need an earlier version. Naw, let me try out the very latest from 15h ago.

///

Python: Traceback (most recent call last):
  File "C:\Program Files\Blender Foundation\Blender 3.1\3.1\scripts\startup\bl_operators\userpref.py", line 782, in execute
    shutil.rmtree(path)
  File "C:\Program Files\Blender Foundation\Blender 3.1\3.1\python\lib\shutil.py", line 739, in rmtree
    return _rmtree_unsafe(path, onerror)
  File "C:\Program Files\Blender Foundation\Blender 3.1\3.1\python\lib\shutil.py", line 612, in _rmtree_unsafe
    _rmtree_unsafe(fullname, onerror)
  File "C:\Program Files\Blender Foundation\Blender 3.1\3.1\python\lib\shutil.py", line 612, in _rmtree_unsafe
    _rmtree_unsafe(fullname, onerror)
  File "C:\Program Files\Blender Foundation\Blender 3.1\3.1\python\lib\shutil.py", line 612, in _rmtree_unsafe
    _rmtree_unsafe(fullname, onerror)
  File "C:\Program Files\Blender Foundation\Blender 3.1\3.1\python\lib\shutil.py", line 617, in _rmtree_unsafe
    onerror(os.unlink, fullname, sys.exc_info())
  File "C:\Program Files\Blender Foundation\Blender 3.1\3.1\python\lib\shutil.py", line 615, in _rmtree_unsafe
    os.unlink(fullname)
PermissionError: [WinError 5] Access is denied: 'C:\\Users\\Marko\\AppData\\Roaming\\Blender Foundation\\Blender\\3.1\\scripts\\addons\\BlenderMalt\\.MaltPath\\Bridge\\ipc\\Ipc.dll'

location: <unknown location>:-1

///

Now I can't unistall it. Let me try running Blender in admin mode.

That worked. Let me install it again.

10:40am. Maybe those socket errors from yesterday were because I was not running it in admin mode. It seems to be using IPC to commnicate. It reminds me of Spiral, though with Spiral I had to go over the network card.

10:50am. The examples work now.

11:05am. Let me take a break here. I need to think what is next anyway. Should I try shading the stuff in the room with Malt? It might be worth a try.

11:45am. Perspective is powerful. I think with it, I could sketch the room to a much greater degree of accuracy. But would doing that kind of thing be particularly better than doing it in Moi for example?

I guess it could be faster.

11:55am. I don't know. Do I go for Malt or no?

If I had time I should go for it, but would it really be useful for illustrations?

No forget it. Modeling is the sweet spot of 3d. I should stay in it. Adding a shitload of shading concerns on top would just make things difficult to deal with. I got good advice in that other thread to make the scene lighting theatrical.

https://blenderartists.org/t/how-do-i-render-a-scene-where-most-of-the-lights-comes-from-grills/1381668/30

///

Looks good.

Remember – when you have things like “light coming in through a door,” that’s a so-called “practical light.” It’s a thing which we know in real life is “a source of light.” But for rendering purposes, as with a theater set, it probably shouldn’t be a source of light. Instead, you “put lights up in the loft of the theater” and use those to provide the actual illumination, which just has to look plausible.

///

12pm. Though I do like the Luxcore solution quite a bit. I need to do less work, not more. If I focused on rendering I could make the scene better, but if I instead focused just on modeling, I could get many more scenes done.

Messing with Malt shaders is really technical and could take months to master in its current state. Let me start the Zbrush course by Pablo. I should break the ice with it.

12:05pm. For now, how about I just focus on getting clean line art for my art?

When I feel like I've mastered that subject than Malt, painting, whatever techniques will be next. This is a good way of going at it.

I mean sure, getting good painting from my models would be good. But I should tackle the challenges one step at a time.

I really needed to render the room, because that will be the basis from getting a good drawing from it, but I should say task complete and get on with it.

Moi will be very formidable when it comes to giving me good drawings.

12:10pm. Let me focus on the course.

I should not lose sight of my goals. My goal is not to get 3/5 in art, but to find ways of getting good results the fastest.

12:25pm. 10m in. This seems like it will be a good course as he is covering his entire workflow. There is even coloring at the end.

Yeah, I'll be able to make use of this. Let me go through the course, and then I will focus on getting line art of the room scene. Freestyle edges by themselves are not good enough, I'd want hatching at a minimum, and even painting after that. I am not sure how I will do it, but that will be my goal.

If I can do all of that smoothly, I can consider myself 3/5 in 3d. I'll be almost ready to start Heaven's Key on the art side. I'll want to refine my methods a bit further, and do the cover, but after that I'll move on to music.

12:40pm. I never checked out Pinterest. He says that the algorithm the website is using to match images is absolutely the best.

12:45pm. Let me stop here at 23m.

12:50pm. Actually all the trays are taken up, let me go at it for 10m more.

1pm. He mentions that Zbrush started as an illustration software.

Right now I am looking at a crappy sculpt of Darth Vader and he is showing me it from various angles and renders.

1:10pm. It seems he does the painting in Krita and PS. I thought he might be painting it directly in Zbrush, but it seems not. He says that Zbrush is just for forms and volumes.

He says that the really powerful part of Zbrush are the custom masks that can be taken into PS for a lot more control.

...Let me try stopping for breakfast here again. I get the sense that this course will be very instructive. Whatever masks Zbrush is generating, I bet I'll be able to get them from Blender as well.

2:15pm. Let me chill a bit more and then I will start. Yeah, I made the right choice going with the Zbrush course rather than messing with shaders. Although I do not know how yet, having Blender generate various kinds of AOVs that I can take into CSP to do something good will be a more workable workflow. I am going to wrap things up by the end of next month and have something that I can use.

2:40pm. I do not feel like it, but let me just get through this. I am not sure if I am interested in following along. I should just watch this stuff and extract his techniques. Though the course is 18h, only a third of that is watching, the rest involves self work. It is fine if I just learn his workflow and leave the rest for later.

3:10pm. > What would you suggest to drive a consistent color look when using Zbrush to illustrate an entire graphic novel?

He going into something involving polypaint masks and polygrouping masks.

...Let me get back to it. I'll rant later. I am getting distracted with this journal.

3:25pm. He really likes Meobius, but I don't in particular. Though, just from this little bit, I am starting to get an inkling how I should be working. Take a step back to take two steps forward. I also came to an understanding that I should be modeling with respect to how future filters will interpret the data. I need a bit more. I do not know whether I will be diving into Malt. Probably I am not going to be able to use PBRs like Cycles and Luxcore as they are too slow. I'll have to find a way to make Eevee work.

3:50pm. Time for part 2 of day 1.

4pm. Let me take a break.

4:30pm. Let me resume.

4:40pm. Come to think of it, back in Malt when I tried a light, it had a power and radius. Isn't radius what I need to control the falloff. I'll keep it in mind.

The choice of renderer here is not so trivial for me. I can't really afford to wait for Luxcore to finish, so after I am done with this Zbrush for Illustrators course I might have a reason to dive into it. If needed I'll open various issues and ask the author to explain what various shaders do.

4:40pm. He is really praising Krita's brush engine. He says it is superior to Photoshop. I wonder how it would compare to CSP.

Huh, what sort of brush is this? I never saw anything like it in CSP.

4:50pm. Yeah these brushes are amazing. They feel like like they have real texture rather than just random scattering like in CSP and Substance Painter. It is really a pity I do not have the skill to take advantage of them.

5:05pm. Right now I am just watching him scribble over the canvas. Let me pause for a bit so I can rant.

I am thinking what the secret behind that comic renderer could be and it really can't be else but simple threesholding. I could a lot of elaborate linework simply from that, for chara models. What he showed me was remarkable. I couldn't draw Darth Vader, but I could certainly make a crappy scult of him. And that scult when converted to a drawing looks very good.

Remember the first scene that I did - the one with the couch. The first thing I grasped for was falloff for the stars. I didn't really like how it came out, but it turns out Malt has rim light. And that might be exactly what I would have wanted back then.

I should make it a priority to investigate toon shading with both Eevee and Malt. I should try sculpting an anime character after I am done with the room.

5:35pm. Estab Life is out. Let me just finish this video.

6:10pm. Day one was really boring overall. I really want to move on to the next parts. I liked the Darth Vader stuff, I think tomorrow he should be going into that in more depth.

Right now I do not feel like putting another 3h of tutorials.

Right now I am thinking to the October of last year. Remember when I was studying Illustrator and thought about tracing Milim Nava before giving up because it would be easy. Tracing her would be easy, but trying to draw her from imagination from a different perspective would be impossible for me.

But I could sculpt her. There are some anime sculptors on Youtube like Yan and Flycat, but they aren't targeting 2d via 3d directly. I should really try it. Maybe I'll end up liking the results. I do not like the CG style 3d anime, but maybe I could make it feel more organic thought both sculpting and compositing.

Pablo's art does not look 3d at all, and yet it is. So there is potential for me to adapt sculpting to whatever I like.

6:15pm. To be fair, Estab Life is really going a long way to change my mind on CG anime, but it not what I am aiming for exactly.

I haven't done it right. I need to put on a filter and then make the sculpt conformal to it. I should have done that back in January. Instead of going into modeling I spend so much time messing with Houdini.

Even now doing this room feels like I am messing around.

I should know what I need to do by the end of this course.

My main mistake is not recognizing the benefits that grayscale and crunching out the midtones brings. I only cared about precision and scale. This really reflects my Jan-March obsession with scattering well. I haven't been just trying to get better, I've also been searching for what better is.

As far as sculpting is concerned, going anime style will allow me to get away with much crappier models and have them look well.

In fact, once I start turning the room into a drawing, it might turn out that a lot of the detailing I did was a waste of time.

6:25pm. Yeah, this is why I am still 2/5 and not 3/5. If I am doing 3d models that will get converted into 2d, the rules are different.

Getting good 2d drawing using 3d gives me a natural way to continue improving my skills.

6:30pm. With the photorealistic 3d of the kind I've been studying I have to do thing like UV unwrapping, texturing, rendering which would take a lot of my time. The models have to be good to be realistic. That means having to do beveling. It is really a lot longer process. Pro 3d artists would skip large parts of that process by buying assets online, but I do not have the cash for that workflow. I'll only be able to get so far with Persia.

6:35pm. I am going to figure this out. Even if I go the CG route, since I am aiming for illustrations, I do not have to have those obvious cell shaded shadows in the end product. 3d will find a way. I am going to take care of the room and that way deal with my environment drawing and painting needs. AFter that I'll get back to chara modeling. This time I will do it right.

6:40pm. Let me close here. This is going to be a hot summer, but I am going to break into 3/5 in art, 2d or not. I'll bust through my lack of visual acuity with raw technical prowess. A mark of a pro is being able to go from A to Z without getting stuck inbetween. I am going to grasp my method and move on to bigger things."

---
## [lyricalpaws/Twxtter-main](https://github.com/lyricalpaws/Twxtter-main)@[eeb1630211...](https://github.com/lyricalpaws/Twxtter-main/commit/eeb163021133141bc6ea14e4fef173cadff98754)
#### Thursday 2022-05-26 17:50:00 by Chloe Carver-Brown

Fuck you baltimore

Signed-off-by: Chloe Carver-Brown <admin@twxtter.com>

---
## [Vestiiso/HvorErDuVen](https://github.com/Vestiiso/HvorErDuVen)@[e106e678a5...](https://github.com/Vestiiso/HvorErDuVen/commit/e106e678a553416010a84b0ac78608296379297f)
#### Thursday 2022-05-26 18:49:06 by Vestiiso

HOLY SHIT 30 TIMER SENERE... FUCKING ENDELIG VIRKER DET LORT!!!!!!!!!

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[908e8c9b0d...](https://github.com/mbs-octoml/mbs-tvm/commit/908e8c9b0d4e09dede18e0a2db7f0d3220018c6f)
#### Thursday 2022-05-26 19:04:35 by Mark Shields

** Collage v2 sketch ***

- Polish compiler_function_utils for splitting out
- Mark functions as extern.
- Get rid of relay.ext.cutlass
- kExternalSymbol:String ----> kExtern:Bool
- Host glitch if PlanDevices run before CollagePartition
- Fix unit test
- Make load_static_library first class python func
- Get CUTLASS going on graph executor as well as vm
- Include export_library in estimate_seconds
- Rollback DSOLibrary changes.
- Add StaticLibraryNode and switch CUTLASS to use it
  This avoids the crazy serialize/deserialize/load hackery, which I'll now remove.
- Get running again
- CUTLASS picks up all options from 'cutlass' external codegen target.
- Revert false starts with cutlass handling
- Get CUTLASS going with program-at-a-time tuning and compilation instead of
  function at a time.
- Save DSOLibraries by contents rather than by reference.
- futzing with libraries
- revert unnecessary cutlass changes
- starting unit test for dsolibrary save
- Prepare scalar changes for PR.
- Eager candidate cost measurement.
- More conv2d_cudnn.cuda training records.
- cleanup before rebase
- Use 'regular' target when build, not external codegen target
- Tuned for -libs=cudnn
- Tune before collage not during
- Bring over target changes
- Fix GetSpecName
- Try again on python target changes, this time leave check_and_update_host_consist unchanged
- Revert python target changes to try again less agressively
- Few other cleanups
- Switch to 'external codegen targets' style
- Woops, run just_tvm after collage to pick up tuning logs
- Finish tuning for rtx3070
- Run them all!
- Update tuning logs
- Share global vars in the candidate function cache
- Finished tuning mobilenet, started on resnet50.
- Include model name in logs to make sure we don't get anything mixed up
- Drop -arch=sm_80
- Fix MaxCoalesce
- Attach external_symbol to lifted functions
- Add missing node registration, but leave VisitAttrs empty for now
- Make MaxCoalesce as aggressive as possible, since simple impl did not handle sharing.
- Finish tuning resnext50
- Improve coelescing
- Account for coelesced functions when outlining final module
- Fix caching, for real this time.
- More nn.conv2d autotvm tuning records, but still not done with resnext50_32_4d.
- OutlineExternalFunction both when preparing to estimate cost and after optimal
  partitioning applied.
- Use fp16 in TensorRT only if model's 'main_dtype' is float16.
- Fix CostEstimator caching issue
- More Target cleanup (while waiting for tuning runs)
- Better logging of candidates
- Support export to ONNX
- Fix merge
- Part-way through tuning for mobilenet.
- Add resnext50_32x4d
- Lift all "Compiler" functions before estimating to ensure no Relay passes are run on them
- Still trying
- Trying to track down weird failure in conv2d compute.
- Switch tensorrt to be fully pattern & composite function based
- Combiner rule for tuple projection
- Allow build to fail in estimate_seconds
- Add mobilenetv2 and resnet50v2 to menagerie
- Update CompilationConfig to handle target refinement
- Nuke remaining uses of TargetMap in favor of CompilationConfig
  (still needs to be pushed into python side)
- Save/Load dso libraries (needed for Cutlass with separated run)
- Move models into separate file
- gpt2_extract_16 and autotvm tuning log
- Handle missing tuning log files
- fp16 support in scalars and the tensorrt runtime.
- Wrap runner in nsys nvprof if requested
- Enforce strict compile/run time separation in preparation for profiling
- Better logging of final optimal partitioning and state of all candidates
- Fix handling of tuples and InlineComposites fixup pass.
- Fix TensorRT pattern bugs
- Pass max_max_depth via PassContext
- Better logging so can quickly compare specs
- BUG: Benchmark the partitioned rather than original model!!!
- Use median instead of mean
- Back to GPT2
- Make sure all function vars have a type
- Don't extract tasks if estimating BYOC-only
  (Was double-tuning every cutlass kernel).
- Make sure cudnn pattern table is registered
- Enable cudnn, get rid of support for op-predicate based BYOC integrations
- Enable cublas
- And yet another go at pruning unnecessary candidates.
- Another go at pruning unnecessary candidates
- Fix CompositePartitionRule use
- Fix a few bugs with new TensorRT pattern-based integration
- Rework RemoveSubCandidatesCombinerRule for soundness
- Better logging
- Bug fixes
- Implement critical nodes idea for avoiding obviously unnecessary candidates
- Promote DataflowGraph from alias to class so can cache downstream index set
- Quick check to avoid unioning candidates which would create a cycle
- Host out CandidatePartitionIndex and add rules to avoid small candidates subsumed by containing candidates
- GetFunction can legitimately return nullptr
- rename tuning log
- Support for int64 literals
- Switch GPT2 to plain model
- Fix library cloberring issue for cutlass
- actually checkin 'built in' tuning log (covers mnist & gpt2 only)
- trying to debug gpt2
- Update TargetKind attribute name
- working through gpt2 issues
- checkin tuning records for MNIST (with hack to not retry failed winograd)
- Autotvm tuning disabled if log file empty (default)
- Autotvm tuning during search working
- tune during search
  (but does not load tuned records after search!)
- About to add tuning to estimate_seconds
- Split out the combiner rules & make them FFI friendly
- Rework comments
- Estimate IRModule instead of Function (closer to meta_schedule iface)
- Add 'host' as first-class partitioning spec
  (Avoids special casing for the 'leave behind for the VM' case)
- Move CollagePartitioner to very start of VM compiler flow (not changing legacy)
- Fix bugs etc with new SubGraph::Rewrite approach
  Ready for updating RFC to focus on partitioning instead of fusion.
- Working again after partition<->fusion split.
- Add PrimitivePartitionRule
- Refactor SubGraph Extract/Rewrite
- Rename kernel->partition, fusion->partition
- Next: make nesting in "Primitive" an explicit transform
- respect existing target constraints from device planner
- make 'compiler' and 'fusion_rule' attributes avail on all target kinds
- moved design to tvm-rfcs, https://github.com/apache/tvm-rfcs/pull/62
- incorporate comments
- avoid repeated fusion
- fix trt type checking
- better logs
- pretty print primitive rules
- fix tensorrt
- multiple targets per spec
- don't extract candidate function until need cost
  Need to bring CombineByPrimitives back under control since lost depth limit.
- cleaned up fusion rule names
- added 'fuse anything touching' for BYOC
- Finish dd example
- Add notion of 'MustLower', even if a candidate fires may still need to consider
  leaving node behind for VM (especially for constants).
- starting example
- finished all the dd sections
- documentation checkpoint
- docs checkpoint
- more design
- starting on dd
- runs MNIST with TVM+CUTLASS+TRT
- cutlass function-at-a-time build
- need to account for build_cutlass_kernels_vm
- move cutlass tuning into relay.ext.cutlass path to avoid special case
- add utils
- don't fuse non-scalar constants for tvm target.
- stuck on cuda mem failure on conv2d, suspect bug in main
- where do the cutlass attrs come from?
- running, roughtly
- pretty printing, signs of life
- wire things up again
- Switch SubGraph and CandidateKernel to TVM objects
- naive CombineByKindFusionRule, just to see what we're up agaist
  Will switch to Object/ObjectRef for SubGraph and CandidateKernel to avoid excess copying.
- preparing to mimic FuseOps
- rework SubGraph to use IndexSet
- rough cut at MaximalFusion
- split SubGraph and IndexSet in preparation for caching input/output/entry/exit sets in SubGraph.
- top-down iterative handling of sub-sub-graphs
- about to give up on one-pass extraction with 'sub-sub-graphs'
- Add notion of 'labels' to sub-graphs
- Rework FusionRules to be more compositional
- partway through reworking fusion rules, broken
- SubGraph::IsValid, but still need to add no_taps check
- dataflow rework, preparing for SubGraph::IsValid
- explode into subdir
- mnist with one fusion rule (which fires twice) working
- switch to CandidateKernelIndex
- Confirm can measure 'pre-annotated' primitive functions
- checkpoint
- stuff
- more sketching
- dominator logging

---
## [00ze-cyclone/Yogstation](https://github.com/00ze-cyclone/Yogstation)@[c3e823d052...](https://github.com/00ze-cyclone/Yogstation/commit/c3e823d052f6e07b6d1f571d0989c6305b53d5f6)
#### Thursday 2022-05-26 19:33:02 by Jamie D

Adds APC and different areas for the multiple air alarms.. why could you siphon interrogation from perma.. (#14163)

* Update Space_Station_13_areas.dm

* Fixes Brig to not be Shit

* Fixes Areastring

* other maps

* Update code/game/area/Space_Station_13_areas.dm

* Fucking hate baiomu so much

* fucking apc

---
## [00ze-cyclone/Yogstation](https://github.com/00ze-cyclone/Yogstation)@[8b77243ce9...](https://github.com/00ze-cyclone/Yogstation/commit/8b77243ce9da72645291d6f22f798bc32611a706)
#### Thursday 2022-05-26 19:33:02 by TheRyeGuyWhoWillNowDie

Makes bloodbrothers start with the makeshift weapons book learned. (Jamie Edition) (#14094)

* makes blood brothers a bit less shit

* oopsie

* improve???

* what

* huh??

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[7704865bbe...](https://github.com/san7890/bruhstation/commit/7704865bbea1d1787fb13374f63e076418e8ba7b)
#### Thursday 2022-05-26 20:55:10 by san7890

OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN

OH GOD OH FUCK OH SHIT OH LORD - SPACE WAS BROKEN

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

---
## [se7ensde/platform_vendor_spark](https://github.com/se7ensde/platform_vendor_spark)@[59fa231439...](https://github.com/se7ensde/platform_vendor_spark/commit/59fa23143952d237eb9bcc8386479ecf51d430da)
#### Thursday 2022-05-26 21:01:31 by se7ensde

Add my Vandalism font and fuck you if you dont like it bitch

---
## [Offroaders123/Skincraft](https://github.com/Offroaders123/Skincraft)@[d1fdc36098...](https://github.com/Offroaders123/Skincraft/commit/d1fdc36098376859af1e2d8c11723a674f43dd11)
#### Thursday 2022-05-26 22:06:22 by Offroaders123

Organizing the Classic Source: Pt. 2

Wrote another Node script to un-nest a lot of the extra folders that contained some of the app state renders.

I think these were mostly generated by the Flash decompiler tool, so I don't think all of these were necessarily all part of the original SVF. Either way, they are super helpful to get some of the missing resources that weren't decompiled directly (Like the Skincraft logo itself, that seems to only be in this folder).

Using Node for organizing file and folder structures is just blowing my mind! This is so powerful. You can really do anything you'd like with it. There are so many tools available to you in the fs module, it's insanely helpful! This would've taken ages to do myself, haha.

---
## [m00tiny/python-practice](https://github.com/m00tiny/python-practice)@[a8275c34bc...](https://github.com/m00tiny/python-practice/commit/a8275c34bca35379a6265da97e8e091158668761)
#### Thursday 2022-05-26 23:19:36 by Stuart Gray

uploading the solution to hacker rank's infamous camelCase 4 challenge that FUCKING SUCKS to be stuck on because you can't see the FUCKING TEST CASE THAT ITIT IS FAILING ON

---
## [NBRET-TOUCH-WASH/martyrdom](https://github.com/NBRET-TOUCH-WASH/martyrdom)@[f340c176dc...](https://github.com/NBRET-TOUCH-WASH/martyrdom/commit/f340c176dcadc2096452f37b5b4c29fbfd36365c)
#### Thursday 2022-05-26 23:28:47 by NBRET-TOUCH-WASH

SHIT WON'T WORK

FUCK YOU
FUCK PYTHON
FUCK PYTHON IMPORTS
I HATE YOU
I AM THIS CLOSE TO MAKING A REBIRTH BRANCH AND STUFFING EVERYTHING IN ONE SINGLE DIRECTORY, AND WHY NOT ONE SINGLE FUCKING FILE

GO FUCK YOURSELF

---
## [gitster/git](https://github.com/gitster/git)@[bdaf1dfae7...](https://github.com/gitster/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Thursday 2022-05-26 23:31:35 by Tao Klerks

branch: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local topic branch from an existing
remote branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the upstream tracking branch.

When the user pushes with a default "git push", with the intention of
pushing their (new) topic branch to the remote, they get an error, and
(amongst other things) a suggestion to run "git push origin HEAD".

If they follow this suggestion the push succeeds, but on subsequent
default pushes they continue to get an error - so eventually they
figure out to add "-u" to change the tracking branch, or they spelunk
the push.default config doc as proposed and set it to "current", or
some GUI tooling does one or the other of these things for them.

When one of their coworkers later works on the same topic branch,
they don't get any of that "weirdness". They just "git checkout
feature1" and everything works exactly as they expect, with the shared
remote branch set up as remote tracking branch, and push and pull
working out of the box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

An experienced git user might say "well yeah, that's what it means to
have the remote tracking branch set to origin/master!" - but the
original user above didn't *ask* to have the remote master branch
added as remote tracking branch - that just happened automatically
when they branched their feature branch. They didn't necessarily even
notice or understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the topic branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make this "branches have the same name locally as on the remote"
workflow less painful / more obvious by introducing a new
branch.autosetupmerge option called "simple", to match the same-name
"push.default" option that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

Update the error displayed when the 'push.default=simple' configuration
rejects a mismatching-upstream-name default push, to offer this new
branch.autosetupmerge option that will prevent this class of error.

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Also extend the existing branch tests with three new cases testing
this option - the obvious matching-name and non-matching-name cases,
and also a non-matching-ref-type case. The matching-name case needs to
temporarily create an independent repo to fetch from, as the general
strategy of using the local repo as the remote in these tests
precludes locally branching with the same name as in the "remote".

Signed-off-by: Tao Klerks <tao@klerks.biz>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---

