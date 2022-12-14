## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-13](docs/good-messages/2022/2022-12-13.md)


2,162,366 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,162,366 were push events containing 3,254,203 commit messages that amount to 270,585,990 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [AttorneyOnline/AO2-Client](https://github.com/AttorneyOnline/AO2-Client)@[4938937c3e...](https://github.com/AttorneyOnline/AO2-Client/commit/4938937c3e4a371fdff20603cae6bb367036dcfc)
#### Tuesday 2022-12-13 00:28:08 by Salanto

Fix compile error of legacy RPC lib

Fuck the game SDK, holy shit that code is so reliant on a shitty game engine that this is honestly better for now.

---
## [dariota/Advent-of-Code](https://github.com/dariota/Advent-of-Code)@[aa28983964...](https://github.com/dariota/Advent-of-Code/commit/aa28983964ac6b00377f4625574980533df2be21)
#### Tuesday 2022-12-13 00:38:49 by Dário Tavares Antunes

Day 12, this thing can't get signal

I shouldn't be surprised that the equipment the elves use needs to be at
quite an elevation to actually work, and yet I somehow am. It seems like
it actually needs a line of sight? Mad.

On the bright side, I got to go for a pretty nice hike. Shame I didn't
pack my camera since I suspect something like falling into a damn river
would happen, lovely sights.

---
## [sdmanchiraju/zulip](https://github.com/sdmanchiraju/zulip)@[23a776c144...](https://github.com/sdmanchiraju/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Tuesday 2022-12-13 00:41:59 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [Jolly-66/Skyrat-tg](https://github.com/Jolly-66/Skyrat-tg)@[82fc8c522e...](https://github.com/Jolly-66/Skyrat-tg/commit/82fc8c522e50ccabd853493afaee43f76930529c)
#### Tuesday 2022-12-13 00:51:10 by SkyratBot

[MIRROR] Excercise Equipment is now craftable [MDB IGNORE] (#17495)

* Excercise Equipment is now craftable (#71190)

## About The Pull Request

Imagine if you will a humble chaplain who wants nothing more than for
all of the spiritual folk on the station to get as massive gains as they
can, after finding that they can not just make more exercise equipment
and that the station does not have any in public places, they go annoy
security enough to get into permabrig only to find out that they cant
even unwrench the equipment and move it to the church!!!

NOT ANYMORE!!!

![jS2aBMBa0B](https://user-images.githubusercontent.com/116288367/200889423-f1b6365c-24c4-4f45-8ca4-c96c9085cf27.png)
crafting recipies

![dreamseeker_O4BgBRsFa8](https://user-images.githubusercontent.com/116288367/200889002-8dd7c927-0745-46a9-a4bc-578c7279042a.gif)
demonstrating unwrenching and wrenching equipment

![dreamseeker_hCFQJZdzoS](https://user-images.githubusercontent.com/116288367/200889019-5f4c8399-d539-4d84-8a3f-7735c3ba1f68.gif)
crafting a punching bag and punching it

Now you can craft as much exercise equipment as you want! May everyone
on the station get as strong as possible and not just prisoners.

Also I changed the message that plays when you try to use exercise
equipment someone else is using into a balloon alert.

![dreamseeker_PwNesmcR1f](https://user-images.githubusercontent.com/116288367/200890964-4f9fa3ee-ce07-4e6e-815c-a3f4593d06b1.png)

## Why It's Good For The Game

Access to exercise equipment on some maps is limited to static positions
and is currently mostly only for prisoners as every map does not have
public exercise equipment. Expanding the access means that you can have
a Drill Sargent Head of Security or Captain who commands people use
these or allows a psychologist to prescribe healthy exercise habits to
their patients.

I think having the potential for exercise equipment on every map is more
fun and also if prisoners get their hands on tools they should be
allowed to mess with these to annoy security or aid in their escape.

## Changelog
:cl:
add: the punching bag, bench press, and chest press are all able to be
crafted and unanchored.
add: crafting recipes for the above
qol: changed a chat message into a balloon alert
qol: adds screentips to equipment (thanks for suggesting i do this
mothblocks!)
/:cl:

* Excercise Equipment is now craftable

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>

---
## [Clarencepricemegatron83/Clarencepricemegatron83](https://github.com/Clarencepricemegatron83/Clarencepricemegatron83)@[46b471712a...](https://github.com/Clarencepricemegatron83/Clarencepricemegatron83/commit/46b471712a3af850b85f96f7b53e3dd6155bc7ac)
#### Tuesday 2022-12-13 02:32:08 by Clarencepricemegatron83

Create Check this shit out my bro

Hey friends and strangers my name is Clarence but you can call me Megatron I'm not a hacker but I getted hacked and I'm tired of that shit it's time for me to reconnect with some one I can trust if your reading this you gotta be areal motherfucker I'm from Texas college station Texas TAM Texas am university I'm a pretty cool cat as hit it's hard to find people to trust these days sooo hit me up I just started.

---
## [kaiykay/businessman-and-situation-](https://github.com/kaiykay/businessman-and-situation-)@[f75ed60cb6...](https://github.com/kaiykay/businessman-and-situation-/commit/f75ed60cb6e669f2b235fb467779f49f8727b710)
#### Tuesday 2022-12-13 02:48:31 by kaiykay

business 

2022 Is a chance to get rich!

 Just use your phone and you can earn big anytime, anywhere!



 Working from home is a dream for many people, some just chat, or surf the internet to pass the time, but some people know how to make money from their mobile phones.
 1-2 hours a day, you can earn IDR 15-40 million per month via WhatsApp. Please take 5 minutes to read this article, because this is an opportunity you don't want to miss.




 My friend Anjas Mara, a skilled worker with a monthly salary of 7.8 million rupiah, has made more money since he learned how to make money with his cell phone.  He bought a new car, he plans to travel, and now his life has more meaning!




 Another friend of mine is Farah, a mother who quit her job to take care of her children and family and lives in poverty.  When he learned a new way to make money, he made Rp. 5 million in a week.  The standard of living has also improved greatly.


 When they add mentor contacts, start learning and try new ways of making money via WhatsApp, money is easy, it only takes 20 minutes to see how it works.  They can make money regardless of place or time, using their free time, They can earn 500 thousand rupiah - 1.5 million rupiah per day, and all their friends also want to be like them!


 Everyone can try this way of making money, civil servants, housewives, shop owners, and all walks of life.  Teach yourself how to make money with tutors.


 You work hard every day, but you don't have enough income to buy the things you want or even to cover your family's expenses.  Feeling unfulfilled in life, if you are willing to change the status quo, you can learn how others have succeeded in making money, to make life better.


 Pick up your phone, call this WhatsApp number and take this opportunity to make your dream come true now!


 You have an opportunity to make money from your mobile and you can really make money from home.




 message area


 After knowing this, my career and life stabilized


 I think I'm the first to know this information


 I've added the tutor's contact details on WhatsApp, hope you can reply as soon as possible.  I want to know how to make money with my phone.


 thank you very much!  !  Excellent service!  !  !  Very satisfied!  !  !


 I introduced this to my father.  In fact, he now makes more money than I do!


 This online training team is amazing, I couldn't believe it at first.  Really make money after joining.  I don't have to worry about makeup and money for clothes now.


 I knew from the start and have made money many times.  I am satisfied with this life.


 I have added a mentor on WhatsApp, please advise.  Thank you!


 I want it too, I don't want to miss this opportunity, many friends have already tried it

---
## [angad777/next.js](https://github.com/angad777/next.js)@[1bbd264216...](https://github.com/angad777/next.js/commit/1bbd2642164098ceb9cebfb36deba9aed7e8a53b)
#### Tuesday 2022-12-13 03:16:38 by abdennor

Add additional fix in hydration error document (#40675)

I had the same issue, so the fix that worked for me was pulled from this
thread https://stackoverflow.com/a/71870995

I have been experiencing the same problem lately with NextJS and i am
not sure if my observations are applicable to other libraries. I had
been wrapping my components with an improper tag that is, NextJS is not
comfortable having a p tag wrapping your divs, sections etc so it will
yell "Hydration failed because the initial UI does not match what was
rendered on the server". So I solved this problem by examining how my
elements were wrapping each other. With material UI you would need to be
cautious for example if you use a Typography component as a wrapper, the
default value of the component prop is "p" so you will experience the
error if you don't change the component value to something semantic. So
in my own opinion based on my personal experience the problem is caused
by improper arrangement of html elements and to solve the problem in the
context of NextJS one will have to reevaluate how they are arranging
their html element

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->


## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm lint`
- [ ] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [miniusAreas/Skyrat-tg](https://github.com/miniusAreas/Skyrat-tg)@[44612df948...](https://github.com/miniusAreas/Skyrat-tg/commit/44612df9486b77e52ca88c8dc9063ee8f7f8ecc7)
#### Tuesday 2022-12-13 03:41:42 by SkyratBot

[MIRROR] The screwdriver cocktail is now the world's worst screwdriver [MDB IGNORE] (#17354)

* The screwdriver cocktail is now the world's worst screwdriver (#70862)

## About The Pull Request

Screwdriver cocktail now secretly works as a screwdriver... just, the
worst one ever. How the fuck are you doing that?!

## Why It's Good For The Game

It's funny and I bet someone has tried this before

## Changelog

:cl:
add: Screwdriver cocktails now work as the world's worst screwdriver
/:cl:

* The screwdriver cocktail is now the world's worst screwdriver

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[44008f485d...](https://github.com/ArtemisStation/artemis-tg/commit/44008f485d6d72537935cfa8a3a5b6140eece744)
#### Tuesday 2022-12-13 04:26:33 by Jacquerel

Fishing-themed Escape Shuttle (#71805)

## About The Pull Request

I can't do much coding until you review my other PRs so I'm making a
mapping PR instead.
I actually made this a while ago while I was trying out strongDMM. It
turns out: it's a good tool and easy to use.

![2022 12 09-10 51
26](https://user-images.githubusercontent.com/7483112/206686234-ae952ba3-2cb4-4093-80a0-d086fe95a3fc.png)

This mid-tier shuttle isn't enormous and is shaped like a fish. It
dedicates much of its internal space to an artificial fishing
environment, plus fishing equipment storage. Plus look at that lovely
wood panelling!
There's not a lot of seating or a large medbay, but there's five fishing
rods for people to wrestle each other over plus some aquariums to store
your catches in.

It contains a variety of fishing biomes (ocean, moisture trap, hole,
portal) but I couldn't fit "lava" in there even though I wanted to
because it's hardcoded to only have fish in it on the mining z-level.
If you're very lucky and nobody shoves you, the time between the shuttle
docking at the station and arriving at Centcomm might be enough time for
you to catch maybe four entire fish. Wow!

## Why It's Good For The Game

There are plenty of novelty shuttle options but I think this one is good
for a personal touch of "the Captain would rather be fishing than
hearing you complain about the nuclear operatives".

## Changelog

:cl:
add: Tell your crew how much you care by ordering a shuttle where half
of the seats have been removed so that you can get some angling done
before you clock out.
/:cl:

---
## [Exr0nRandomProjects/22math435_tda](https://github.com/Exr0nRandomProjects/22math435_tda)@[57bfb257ae...](https://github.com/Exr0nRandomProjects/22math435_tda/commit/57bfb257aed3ea490ad0f2deb7987e842b7b7611)
#### Tuesday 2022-12-13 05:29:12 by Huxley Marvit

Meet me at midnight
(Ooh, ooh, ooh, whoa whoa whoa whoa whoa)
Staring at the ceiling with you
Oh, you don't ever say too much
And you don't really read into
My melancholia
I've been under scrutiny (yeah, oh yeah)
You handle it beautifully (yeah, oh yeah)
All this shit is new to me (yeah, oh yeah)
I feel a lavender haze creeping up on me
So real, I'm damned if I do give a damn what people say
No deal, the 1950s shit they want from me
I just wanna stay in that lavender haze
(Ooh, ooh, whoa whoa whoa whoa whoa)
All they keep asking me (all they keep asking me)
Is if I'm gonna be your bride
The only kind of girl they see (the only kind of girl they see)
Is a one night or a wife
I find it dizzying (yeah, oh yeah)
They're bringing up my history (yeah, oh yeah)
But you aren't even listening (yeah, oh yeah)

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[2b68a2d0c7...](https://github.com/Offroaders123/NBTify/commit/2b68a2d0c7e6a2d863d3e746d8e06bbc2d2541c7)
#### Tuesday 2022-12-13 07:42:19 by Offroaders123

Accepting ArrayBufferLike for Reading

Woo hoo, got it working!!! Super happy to figure out the typings dilemma. My hack: Redefine `toString()` on `interface ArrayBuffer` as an `as const` string, `"[object ArrayBuffer]"`. Not the prettiest, but also very beautiful. It doesn't add any types for fake property definitions, and it's only inside of NBTify, it can't escape out of the library. Amazing.

I'm probably gonna add this to the issue page to show how I solved it, as it ended up fixing all of the typing issues between `Uint8Array`, which was one of the holdups for implementing this relatively easy thing.

Ok, so down to the actual changes. Now you can simply pass in a raw `ArrayBuffer` or `SharedArrayBuffer` into the Read module, rather than needing it to be wrapped in a `Uint8Array` view. This is super awesome, as I really like the ability to use this with Promise chaining, and without having to make `Uint8Array` objects everywhere. This will be the most useful on the web side of things I feel, like for use with `fetch()`, `Response()`, things like that. And, probably Workers too, come to think of it! Haven't deeply experimented with Workers yet, but not having to manually wrap anything in a `Uint8Array` will be greatly awesome, less implementation details to worry about. It just works!
```ts
import NBT, { NBTData } from "nbtify";

const result: NBTData = await fetch("./level.dat")
  .then(response => response.arrayBuffer())
  .then(NBT.read);
```

---
## [tomponline/lxd](https://github.com/tomponline/lxd)@[de0d151a2c...](https://github.com/tomponline/lxd/commit/de0d151a2cc9bd8cef31431e126649e2b6a18be7)
#### Tuesday 2022-12-13 08:12:12 by Thomas Parrott

lxd/instance/drivers/driver/qemu: Fix macvlan NICs losing connectivity on LXD restart

Switch to using monitor.SendFile() rather than monitor.SendFileWithFDSet(), as there
appears to be some rather strange behaviour going on with QEMU when used with macvtap
NICs.

If you pass the macvtap file handles using monitor.SendFileWithFDSet() it will use a
separate FD set for each file handle. This works fine, and I can see the correct file
handles opened by the QEMU process. But when LXD is restarted (the monitor connection
is closed), the file handles are closed by QEMU, causing the connectivity to break.

I have experimented with using the same FD set for all file handles associated to a
particular macvtap NIC. This didn't fix the issue.

I also tried hard coding the FD set ID to 0. This meant that the macvtap NIC would
share an FD set with the root disk device. Interestingly this solved the issue.
However it made me uncomfortable as the root disk is only configured by referencing
the FD set ID itself, rather than a particular FD inside the set. So I don't think
that sharing an FD set with multiple devices is a good idea.

However it got me thinking that perhaps the fact that the root disk is referencing
the FD set by ID (i.e using file=/dev/fdset/0 in its config) meant that QEMU somehow
realised that the FD set should be persisted even after the monitor has disconnected.

I confirmed that using the same FD set (even if a different ID than 0) for macvtap NICS
as the root disk device fixed the issue.

But because of my discomfort at that scenario (explained above) I instead looked for
a different solution. Before introducing multi-queue macvlan support for VMs we were
using monitor.SendFile() which worked fine. However I had switched to using the
monitor.SendFileWithFDSet() function as the former didn't support accessing the specific
FD number that was created inside QEMU. I thought we needed this because all the
documentation around using multi-queue macvtap devices showed the use of numeric FDs.

However on further exploration it turns out that we can infact use monitor.SendFile,
and by sending each file handle with a unique name we can then refer to those file
handles using the same names in `fds` setting for the macvtap devices.

Note: Because the `fds` list is colon separated one cannot use colons in the file
handle names. And I also experienced issues with connectivity when using dashes in
the file handle names. So I opted for using full-stops instead.

Fixes #11201

Signed-off-by: Thomas Parrott <thomas.parrott@canonical.com>

---
## [RealMalachi/s2disasm](https://github.com/RealMalachi/s2disasm)@[6c2dc0c02c...](https://github.com/RealMalachi/s2disasm/commit/6c2dc0c02ced4277fc2089ad12e2796ba0162bd4)
#### Tuesday 2022-12-13 08:26:53 by Malseri-SpicyBread

Major (WIP) optimization to SS ring objects

Optimized some SS objects, but one of the methods was kinda stupid. Made it so the art scaling animation code is literally just "transfer anim to mapping_frame". This is faster, but breaks ring animations. That's why I didn't just change anim to mapping_frame
Before I add custom animation code to the rings, I want to fix a layering issue you can see  with the rings here. Since the only priority I changed was the ring sparkle, I can assume the original game had this issue too. Bombs don't have it, so I'll start from there.
I'd also like to increase the animation on the SS rings if possible.

Also, trying to make each type of game alteration a separate commit now, since I plan to make progress slower and less chaotic.

---
## [Chainsawicus/cmss13](https://github.com/Chainsawicus/cmss13)@[eb4886c115...](https://github.com/Chainsawicus/cmss13/commit/eb4886c115a0965a347783b87eb3415f098c2c1f)
#### Tuesday 2022-12-13 09:40:48 by carlarctg

Spitter Rework (#1541)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Design doc:

https://hackmd.io/@waltuh/Sy0A1SnEo
Slightly inaccurate as my brainworms enticed me to change and add mini
features.

Approved by Walter, ignorepproved by Gevonius and Satanbatros


https://cdn.discordapp.com/attachments/280051925154660363/1041475609165045770/image.png

Changes:
- Spit doesn't spatter by default, instead it's now a faster, weak
7-tile* projectile that deals 20 damage with a faster spit cooldown.
Fully accurate at 6 tiles, inaccurate at 7 tiles but can sometimes hit.
- Frenzy replaced with 'charge spit'. Halved speed buff, added +5 armor
buff, the next spit will deal 10 more damage and coat humans in acid but
have only 5* tiles of range.
- Acid spray halves damage every time someone walks on it. However, its
damage is spread over legs and feet, and if someone who is spattered
with acid is hit by it, their acid spatter will be strengthened, dealing
more damage, lasting longer, and needing two rolls to clear up. Also,
the bonus damage didn't actually work, now it does.

* Projectile range code is SHIIIT and breaks on diagonals so the range
variable is increased.

Also, queen acid spit spatters and has 1 second less extra cooldown
because find and replace caused it and I didn't think it was a change
worth removing. It's neat, maybe they'll actually use it now.

Added support for balloonchat colors. (Even TG doesn't have this, we're
awesome now!)

Renamed vision_distance parameter to max_distance so it's similar to
visible_message

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

As stated in the hackmd, spitter is very ineffective without using the
oversight-exploit infinite acid spray spam, and its combo (acid spatter
into spray) does not actually help, as the stun stops the human from
getting further hit by the spray and the bonus damage does not actually
apply thanks to shitcode. This PR makes it so that the combo is indeed
more effective than making humans walk into the spray.

Again as stated, spitter suffers from a strange issue where it's
actually not good at harassing from range despite that being its
purpose, since it has a low range. By letting it be long ranged by
default and choose to go short range, it adds a lot of depth and
versatility and lets it actually harass marines.

As always they can just. Shoot it to make it go away. 

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
refactor: Added support for balloonchat colors. (Even TG doesn't have
this, we're awesome now!)
add: Spitter rework!
add: Spit is now full screen range but weaker.
add: Frenzy is renamed and causes spit to inflict spatter coating.
add: Acid spray's damage is halved every time it hits a human, but if it
hits someone coated in acid it will enhance it, making it more dangerous
and need two rolls to shake off.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [Chainsawicus/cmss13](https://github.com/Chainsawicus/cmss13)@[146d4a3fa8...](https://github.com/Chainsawicus/cmss13/commit/146d4a3fa87a25a16e7246c32d85b6b57614adc5)
#### Tuesday 2022-12-13 09:40:48 by carlarctg

Cloaked belltower alpha increased from 10 (scout) to 35. (#1768)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Var change.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

You may think this is a 'ided' change, that I got owned by a bell tower
and opened this PR. But believe me, it's the exact other way around.

I play engineer often, especially on New Varadero, and every time I pick
the cloaked bell. It is hilariously busted, but that's not actually the
point here. The reason I'm making this PR is because it is genuinely
_impossible_ to find the belltower if it's fully cloaked. If you don't
memorize the placement you quite literally HAVE to right click over
every single tile in the region because the alpha value is SO low it is
just not feasible to detect. I'm saying this as an engineer, it's too
damn much, it takes me half a minute to find my tower and pack it up
again. Worse, sometimes people take it or a xeno slashes it while I'm
being defibbed and I can't tell if I just can't find it or what.

The difference between scout's cloak and the belltower's cloak is that
scout has a large one color silhouette and is constantly moving, and can
additionally be detected through walls by xenos, though again, not the
reason for this. The belltower has a small, thin silhouette that has
lots of gaps in its sprite, making it very hard to locate by hand.

That this will weaken the belltower against xenos is no surprise, but I
don't think that's a problem. As I said, the belltower is busted. I say
this as someone who uses it more than has it used against them. 6
seconds of superslow in a 4x4/5x5 range!

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
balance: Increased alpha (reduced camo) of the camo belltower from 10 to
35. This is mainly meant for engineers to be able to see their tower to
pick it up, but the inevitable balance changes aren't unintended.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [Linnea-Olofsson-nti-johanneberg/zoo2022](https://github.com/Linnea-Olofsson-nti-johanneberg/zoo2022)@[50992bfc79...](https://github.com/Linnea-Olofsson-nti-johanneberg/zoo2022/commit/50992bfc793bb243b56e68180c183a9e39d9af83)
#### Tuesday 2022-12-13 09:52:38 by Linnea-Olofsson-nti-johanneberg

lektion 3

Något är fel på mitt grid skall lista ut vad fan som är felet på det.
JAG GER UPP!!!
NÅGOT ÄR FEL PÅ DENNA BITCHEN.
MATTIAS JAG VILL INTE.
DETTA ÄR SÅ DUMT.
JAG SKA FAN JOBBA VARJE FUCKING DAG NU FÖR ATT LÖSA DENNA BITCHEN.
MASSA SHIT ÄR JU FAN RÖD.
JAG SKA FAN KOLLA OM VIDEOS.
FY FAN.
ok nvm Linus hjälpte mig. Det blev lite bättre nu.

---
## [LyaaaaaGames/AIdventure_Localization](https://github.com/LyaaaaaGames/AIdventure_Localization)@[27ea880669...](https://github.com/LyaaaaaGames/AIdventure_Localization/commit/27ea8806696af55c72c377b25c30a35c29b8c358)
#### Tuesday 2022-12-13 09:58:49 by Lyaaaaaaaaaaaaaaa

Added many keys for the 1.5.0 of AIdventure.

- UPDATE_CONTENT
- ITEM_URL
- YOUR_ITEMS
- SUCCESS_UPLOAD_TO_WORKSHOP
- DISPLAY_ONLY_PNG
- DOWNLOAD_
- FAILED_UPLOAD_TO_WORKSHOP
- FRIENDS_ONLY
- I_ACCEPTED_TOS
- PREVIEW_IMAGE
- PRIVATE
- PUBLIC
- READ_TOS
- SELECT_LANGUAGE
- SHARE
- SHARE_CONTENT
- TYPE_OF_FILE
- UPLOAD_TO_WORKSHOP
- VISIBILITY
- WORKSHOP_UPLOAD_ACCEPT_DIALOG
- WORKSHOP_UPLOAD_BUTTON_HINT
- 1ST_PERSON
- 2ND_PERSON
- ADVENTURE
- CYBERPUNK
- DARK
- DYSTOPIAN
- FANTASY
- FEMALE_PROTAGONIST
- HISTORICAL
- HORROR
- LGBTQ
- LOREBOOK_INCLUDED
- MALE_PROTAGONIST
- MEDIEVAL
- MODERN_ERA
- MYSTERY
- PIRATE
- POST_APOCALYPTIC
- ROMANCE
- SCIENCE_FICTION
- STEAMPUNK
- THRILLER
- UPLIFTING
- WILD_WEST
- ZOMBIE

---
## [peff/git](https://github.com/peff/git)@[bccd4ce097...](https://github.com/peff/git/commit/bccd4ce097e48728a734d068a07ff2409542167c)
#### Tuesday 2022-12-13 10:55:20 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [JetBrains/intellij-community](https://github.com/JetBrains/intellij-community)@[eaec1ec320...](https://github.com/JetBrains/intellij-community/commit/eaec1ec320ce8cbc7cb48f6f069ed7078ae9938c)
#### Tuesday 2022-12-13 10:58:05 by Sergei Tachenov

[UI] IDEA-304712 Move appendInplaceComments to BGT update

The appendInplaceComments method used to be called on the EDT
during painting. It's potentially slow, and it's also a bad practice
to do any state computations during painting anyway.

Fix by moving the relevant logic into the node's update() and
appending the comments directly to PresentationData.

This turned out to be trickier than it seems. The Project view has a lot
of different node types, some of which are even in 3rd party plugins.
They all extend ProjectViewNode (except Rider that extends AbstractTreeNode).
However, it's not easy to put the logic there as it's a part of the lang-api module,
while the logic itself is in the lang-impl module. And logic doesn't belong to the API
module anyway.

The solution is, of course, dependency inversion, but it's not easy to inject a reference
to an interface into ProjectViewNode (let alone AbstractTreeNode) because
we have no control of how these objects are constructed.
Of course, it's possible to delegate this job to some parent or owner
object like the Project View Pane, for example. However, this creates unnecessary coupling
and would require some dirty hacks to get to those nodes and inject the needed references
into them.

Thankfully, most (if not all) Project View nodes that actually use inplace comments
extend AbstractPsiBasedNode, so we just put the actual comment producer there.

The new interfaces for this DI is InplaceCommentProducer (that produces the actual
comments) and InplaceCommentAppender that appends them (either to the presentation
when the new approach is used or to the renderer for the legacy case).

In case there are nodes that don't provide an inplace comment producer,
we still revert to the old logic. This has an unfortunate side effect of calling
getValue() on a node, which is the very potentially slow operation we're trying
to get rid of, but at least we now don't call it on AbstractPsiBasedNode anymore,
and those calls were probably the vast majority (if not all) slow operation calls.

One more trick involved is to convert the plain presentation's text (myPresentableText)
to the colored text before appending comments because many presentations don't
use colored text by default. Just appending comments would override the plain text
and, e.g., class and file names in the Project View would disappear. This is what the new
ensureColoredTextIsUsed() method in PresentationData is for.

GitOrigin-RevId: d7da0fc059d6d70ff369ea981501c5008b53b20d

---
## [jakewilliami/advent-of-code](https://github.com/jakewilliami/advent-of-code)@[35be1a3a74...](https://github.com/jakewilliami/advent-of-code/commit/35be1a3a748614539069d9aa8971df4ecf3e23bf)
#### Tuesday 2022-12-13 11:34:20 by Jake Ireland

Solve AoC Day 13 2022 in Julia

I had a friend's birthday dinner tonight, and we went to see a show
afterwards, so I could only start this 5 and a half hours after the
problem came out.  It's a shame, as I really enjoyed this one, and
found it quite simple (utilising Julia's multiple dispatch and
customisable sorting); it only took less than 45 minutes to complete
both parts.

---
## [robotduinom/PsychonautStation](https://github.com/robotduinom/PsychonautStation)@[58b61a17a7...](https://github.com/robotduinom/PsychonautStation/commit/58b61a17a78e90ea9da91351572abee9a4f93ccb)
#### Tuesday 2022-12-13 11:35:08 by Jacquerel

Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

---
## [Mu-L/NetHack](https://github.com/Mu-L/NetHack)@[b2fe51490d...](https://github.com/Mu-L/NetHack/commit/b2fe51490dac43cac70ec29c6958467b0fa9bdd4)
#### Tuesday 2022-12-13 12:22:57 by PatR

tty-style role selection for curses

Move the tty role/race/&c selection from wintty.c to role.c and remove
its references to BASE_WINDOW.  Have curses call the same routine now
so that the player has the option to choose role, race, gender, and
alignment in any order and to confirm or override random settings
prior to starting play.  Also if you went through "who are you?" then
final confirmation includes an extra menu choice to rename the hero.

It still has the quirk of sometimes remembering some of the previous
aspects when you re-pick a new value for some aspect which already
been selected.

The menus pop up on top of the copyright screen and that looks a bit
strange.  I don't think core code has any way to erase that base
window without erasing the entire screen so to fix the strangeness
the window ports would need to do that before calling the selection
routine.  I didn't do that because the very first prompt, "Shall I
pick ... for you? [ynaq]" shows up in that window rather than in a
popup over it, and having it be all by itself on an otherwise blank
screen seemed to be even stranger.

X11 and Qt both have more sophisticated selection routines so I
haven't tried to switch either of them to use this.  They both use a
fancy role-selection-specific menu with all the aspects present at
once so this wouldn't fit without more work than I care to tackle.

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[00d3780c38...](https://github.com/Huffie56/cmss13/commit/00d3780c382c704f24e5c6f24aa36d88d509b7ea)
#### Tuesday 2022-12-13 12:42:24 by carlarctg

PDT/L Buff (#1757)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

PDT/L kits now fold into cardboard.

Added many spare PDT/L kits and batteries to req. (Marines dropped them
off at req once they realized they were shitty milsurp knockoffs)

Made minibatteries tiny.

Added boldwarning span macro.

Improved locator tube sprites: Now has a pop-out battery slot at the top
that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.

Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Fixed a bug in which a string referenced a null var.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

When I saw the PDT/L kit, I was very interested. It seemed like a great
way to encourage teamwork and buddying up with some fun lore flavor on
the side. However, trying it out, it really feels bare-bones. I get it's
supposed to be 'crappy' because Boots magazine subscriber items suck and
so do the lives of every private on the corps, but the way that's
implemented really ruins the extremely cool concept that is being able
to locate your fellow buddies across the battlefield, so you don't need
to continually say HEY WHERE ARE YOU over comms in the many times you'll
get split up.

Thus I've heavily buffed them around the board, which you may think is
going way too far, and to an extent, you're _right._ It's intentional.
This is a really cool item that actively encourages teamwork and that's
why I would rather swing the buff hammer too hard than give it a paltry
buff and some qol that ultimately nobody cares about. It's the same as
the spotter kit. It's nuts, but needs teamwork to actually be useful.
And this should be encouraged.

If it is still deemed too strong, there are things we can do to
laterally nerf it without closing the PR outright. Making the tube not
work if the bracelet holder's dead, having it needs comms to work come
to mind, but there are surely others.

> Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

The intention here is to let marines actually resupply their kits once
they run dry, and if they're proactive, maybe grab some and bring them
to FOB with them. Despite the description, the cells cannot easily be
recharged as power cell chargers are different from rechargers, they are
effectively Bay12 legacy that is VERY hard to come across.

'What if someone carries like 5 of them in their bag? That'd completely
nullify the power drain part.'

The stinger here is 'in the bag'. There are not enough reasons to carry
bags and satchels in this game right now as the sheer amount of storage
for goods marines have make them a one-man-army with two primaries. If a
marine forgoes a shotgun that might save them from a 1-pounce capping
runner for 5 spare LT batteries, a default medkit, and two flare boxes,
they are well within their rights to do so.

> Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)

This lets req drop them off at FOB if they eventually figure out they
can drop unvended surplus there. If this somehow happens, marines who
never even glanced at the kit in loadout or prep will notice it exists
and maybe, just maybe, use them!

> Made minibatteries tiny.

You may think this contradicts my earlier point about sacrificing
storage value, but _actually_ think about it. All webbing types, armor
slots, pouches, belts, even the helmet, all share the common attribute
of not caring about item size. If it's small or medum it still takes 1
out of the 3 slots in medium armor. Any storage item that isn't a
satchel, effectively. Every spare battery taken directly in the average
marine's inventory is one slot less for 5 shotgun shells, one magazine,
one unga juice flask, binoculars. What this means in the end is simply
that marines may carry one to two spare batteries in their helmet (I
think) at the cost of Drip which few marines will trade for, and satchel
marines don't have to sacrifice a lot of space for the spare battery.
Plus, it makes sense, why wouldn't a small AA rechargeable battery be
tiny.

> Improved locator tube sprites: Now has a pop-out battery slot at the
top that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

This looks so sick!

> Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Adding sounds to items should be standarized, I think. There are so many
cool sounds in the sound/machines folder that go unused. Personally i
felt like these small stupid sounds added a LOT to the atmosphere of
this tiny locator tube and bracelet. Alien Isolation is known for its
sounds, we should strive to emulate that.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
add: Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.
qol: PDT/L kits now fold into cardboard.
add: Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)
balance: Made minibatteries tiny.
refactor: Added boldwarning span macro.
imageadd: Improved locator tube sprites: Now has a pop-out battery slot
at the top that shows up if emptied. The main green stripe is now a
battery indicator with appropiately-faded-out yellow warning and
blinking red danger sprites. The small notch at the bottom is now a
bracelet indicator that turns off without a battery and blinks red if
the bracelet was somehow destroyed.
qol: The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.
soundadd: Added a ton of sounds to interactions with the PDT/L kit.
Beeps on scanning, buzzes on errors, clicks on handling.
fix: Fixed a bug in which a string referenced a null var.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[ce39f048bf...](https://github.com/Huffie56/cmss13/commit/ce39f048bf5eb25e2a93d7355327ccacc0504b01)
#### Tuesday 2022-12-13 12:42:24 by carlarctg

Buffed, resprited, enhanced Oppressor. (#1732)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

**Resprited Oppressor! Pics here:**


![image](https://user-images.githubusercontent.com/53100513/204121775-9f4acd11-d818-46e8-81d3-c38bdfdabf5c.png)

Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Oppressor can hook over the M2C and M56D again.

Oppressor can hook over ledges. (UNIMPLEMENTED)

Tail stab's main ability usage is moved to a different proc for future
custom tail stabs.

Redesigned Tail Stab for Oppressor. Tail seize now utilizes a projectile
and beams to fire a 3-tile reaching tail hook, that pulls in AND DOES
NOT STUN marines. (It slows them for 0.5 seconds)

![Screenshot_20221127-032533~2](https://user-images.githubusercontent.com/53100513/204122365-e1ee57f7-1b9d-443e-a45c-dceec07a88d3.png)

Oppressor's abduct has had its effect strings changed to imply coiling
and uncoiling of the tail. Captured targets will now have a beam of the
Oppressor's tail attached to them (Purely visual) until they reach the
Praetorian, alongside an overlay of the vice grip on their legs.

Added a proc, .ammo/on_bullet_generation(), for the ammo datum to apply
effects to the generated bullet/projectile.

Added the bound_beam variable to projectiles. Could be used in the
future for things like harpoon guns, lasers, etc.

Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

Videos tomorrow.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Animated telegraphs looked really cool, but (I presume) were removed
because BYOND sometimes freezes or starts animations midway through when
short lived animated objects show up, for some reason. I effectively
made it so these are irrelevant by slapping on the border - The animated
effects are just a bonus and will not impact visibility, and in fact
enhance it.

> Oppressor can hook over the M2C and M56D again.

Everyone I've talked to agrees that there really is no reason for these
weapons to protect from abduction. The player can just.. move out of the
way, or even rest if they're in a crowded spot. It's also very
frustrating to see it get in the way of *other* abducts that bonk into
it. The player is going immobile in range of a xenomorph that punishes
immobility.

> Oppressor can hook over ledges. (UNIMPLEMENTED)

Couldn't replicate this issue for some reason... So uh. I dunno.

> Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)

Geeves approved.

This looks so fucking awesome. The slow is barely a thing, so I wouldn't
fret about slow creep. The reaching hook does no damage, only pulls
targets closer. This isn't necessarily super strong, but it's mega cool
and fits with Oppressor's theme of dislocation. I also changed the
windup from 1s to 0.5s so it can be utilized during combat, but this
could be reverted if it's too strong somehow.

> Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

This looked stinky on the tail seize.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: Carlarc, Mikola Wei

imageadd: Resprited Oppressor, sprites made by Mikola Wei.
imageadd: Re-added animated telegraphs for Abduction. They've been
tweaked to always have the default border - that way, the weird way
byond handles short-lived animated objects doesn't make the telegraph
absurdly small. It can always be easily seen.
balance: Oppressor can hook over the M2C and M56D again.
refactor: Tail stab's main ability usage is moved to a different proc
for future custom tail stabs.
add: Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)
imageadd: Oppressor's abduct has had its effect strings changed to imply
coiling and uncoiling of the tail. Captured targets will now have a beam
of the Oppressor's tail attached to them (Purely visual) until they
reach the Praetorian, alongside an overlay of the vice grip on their
legs.
refactor: Added a proc, .ammo/on_bullet_generation(), for the ammo datum
to apply effects to the generated bullet/projectile.
refactor: Added the bound_beam variable to projectiles. Could be used in
the future for things like harpoon guns, lasers, etc.
fix: Fixed non-damaging projectiles causing a blood spurt. (It was
checking flags && FLAG instead of flag & flag, remember to use
CHECK_BITFIELD folks!)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

Co-authored-by: harryob <me@harryob.live>

---
## [ingar-sa/mappevurdering](https://github.com/ingar-sa/mappevurdering)@[8a1038c1d6...](https://github.com/ingar-sa/mappevurdering/commit/8a1038c1d6ebbc7b7dbc6d61dde746ced67e2a0c)
#### Tuesday 2022-12-13 13:17:57 by Ingar Solveigson Asheim

Holy fucking shit! Holy fucking shit! Holy fucking shit! Holy fucking shit! Holy fucking shit!

---
## [andrewboywew/app-dev](https://github.com/andrewboywew/app-dev)@[b8b2ee8d4e...](https://github.com/andrewboywew/app-dev/commit/b8b2ee8d4e6f70a757cf1c15c80ee5866584355d)
#### Tuesday 2022-12-13 13:58:11 by andrewboywew

Update README.md

One Piece - The Japanese manga series One Piece was created by Eiichiro Oda. Since July 1997, it has been serialized in Shueisha's shnen manga magazine Weekly Shnen Jump, and as of November 2022, its individual chapters have been collected into 104 tank-bon volumes. The plot centers on the exploits of Monkey D. Luffy, a young man whose unintended consumption of a Devil Fruit left him with a body made of rubber. In order to succeed Gol D. Roger as the new King of the Pirates, Luffy explores the Grand Line with his pirate band, the Straw Hat Pirates, in search of the ultimate treasure known as the "One Piece."

Wednesday - Based on the The Addams Family character Wednesday Addams, Wednesday is a coming-of-age supernatural comedic horror television series in the United States. Jenna Ortega plays the titular role in this film, which was co-written by Alfred Gough and Miles Millar. Catherine Zeta-Jones, Luis Guzmán, Isaac Ordonez, Gwendoline Christie, Riki Lindhome, Jamie McShane, Fred Armisen, and Christina Ricci play supporting roles. Tim Burton, who also acts as executive producer, directed four of the eight episodes. The main girl, who goes by the title, tries to solve a monstrous mystery at her school.

Chainsaw Man - Tatsuki Fujimoto is the author and illustrator of the Japanese manga series Chainsaw Man (Japanese:, Hepburn: Chens Man). From December 2018 to December 2020, its first part was serialized in Shueisha's shunen manga magazine Weekly Shunen Jump. In July 2022, its second part started serialization in Shueisha's online magazine Shunen Jump+. As of October 2022, its chapters have been compiled into 12 tank-bon volumes. The plot of Chainsaw Man centers on Denji, a poor young man who enters into a deal to have his body fused with that of a canine devil named Pochita, giving him the power to turn specific body parts into chainsaws.

Stranger Things - The 1980s are shown in the fictional rural Indiana town of Hawkins in the television series Stranger Things. Although the neighboring Hawkins National Laboratory purports to do scientific research for the US Department of Energy, it actually conducts covert paranormal and supernatural operations, some of which use human test subjects. They unwittingly opened a connection to "the Upside Down," an alternative reality, and its influence begins to have disastrous effects on the citizens of Hawkins.

Money Heist - Money Heist is a Spanish heist crime drama television series developed by Lex Pina, whose name translates to "The House of Paper" in English. From the viewpoint of one of the thieves, Tokyo (Ursula Corberó), the series follows two meticulously planned heists carried out by the Professor (Lvaro Morte), one on the Royal Mint of Spain and the other on the Bank of Spain. Flashbacks, time jumps, hidden character motivations, and an unreliable narrator are used to add intricacy to the real-time-like narrative.

Alice in Borderland - Based on the Haro Aso manga of the same name, Alice in Borderland (Japanese:, Hepburn: Imawa no Kuni no Arisu) is a 2020 Japanese science fiction thriller drama streaming television series. The series, which was directed by Shinsuke Sato, features Kento Yamazaki and Tao Tsuchiya as pals who are stranded in an abandoned Tokyo and forced to compete in risky games, the nature of which are dictated by playing cards. Players begin with "visas," which are then extended as they advance through the games. If the visas run out, the people are blasted down with red lasers and put to death.

---
## [Danielsn1/Assignment-2](https://github.com/Danielsn1/Assignment-2)@[c885ed5ba6...](https://github.com/Danielsn1/Assignment-2/commit/c885ed5ba62a418e17a1cf5495f582e51590de90)
#### Tuesday 2022-12-13 14:05:29 by Jack Castiglione

Update client.py

I cannot believe that Rahul got up at 1 yesterday with me (but hes not even that sick hes just piggybacking off me) and then went to the arena and then we ate dinner at 7 (even though he told me 6 so I had to wait in the arena for an hour) and then came back and WENT TO BED AT 7:30!!! You know what I did while he was gone? I hung out with some friends and I TOOK A NAP. DOES HE EXPECT ME TO SLEEP 27 HOURS A DAY??????

Also there's one part (Line 24) where I wasn't sure what to put, ok thanks.

---
## [Empire-Strikes-Back/Travis-Walker](https://github.com/Empire-Strikes-Back/Travis-Walker)@[66da945227...](https://github.com/Empire-Strikes-Back/Travis-Walker/commit/66da94522737f251c1aa9a506d6ddb483b2140bc)
#### Tuesday 2022-12-13 14:32:30 by Travis-Walker

oh, Bard - his name is Bard - how do you know? - I asked him

like Blake Griffin I want to play

unlike Chuck Carrol I don't want to be robbed - I don't want to sit and be dead

I heard Jesus - about lost sheep, enemies and love, man going to Jericho, reborn

let my identity fruit be peach
let me run - even though I don't yet know who I'll be
like Thorin before meeting Gandalf don't yet know he's going on a quest

:Stephen-Colbert you're in a new movie - Battle of Fie Armies - what do you think about the ending?
:Benedict-Smaug-Cumberbatch I don't know - I haven't read the books
:Stephen it's gonna get you - right here

---
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[e9cff525dc...](https://github.com/RikuTheKiller/tgstation/commit/e9cff525dc5b57153af3b4bb9039de08d6823805)
#### Tuesday 2022-12-13 14:34:33 by tralezab

Refactors Pirates into Pirate Gangs, Adds the Psyker-gang as new pirates (#71650)

## About The Pull Request

### Refactor
Pirate gangs are now datumized for extendability, custom dialogue, etc.

### Psyker Gang 🧠 
Psyker-gang Members are pirates who are... yes, Psykers. They're on a
gore-binge and need some money for more hits of gore!

- Gore autoinjectors, filled with dirty kronkaine. Don't overdose,
you'll go splat.
- Psykerboost armor, reactive armor that refreshes psychic abilities.
Given to the leader.

- [x] @Fikou is making the map :D

## Why It's Good For The Game

God I fucking love variety also now we can add as many different pirates
as we so desire

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/205342701-9cba63ef-a22c-4f07-9b48-8793c4a2b5af.png)
  
</details>

## Changelog
:cl: Tralezab code, Fikou's map, PigeonVerde and Halcyon for sprites!
add: Psyker-gangers are new pirates
refactor: refactored pirate code so we can add more in the future
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [ngoduyanh/nrs-impl-kt](https://github.com/ngoduyanh/nrs-impl-kt)@[5f44cb47bf...](https://github.com/ngoduyanh/nrs-impl-kt/commit/5f44cb47bf524fb43a9687df6027eb7a855783f8)
#### Tuesday 2022-12-13 14:42:00 by ngoduyanh

chore(impl): :rocket: rank `Higashi no Sora Kara Hajimaru Sekai`

Re:Stage! (Re:ステージ!, Risutēji) is a Japanese multimedia franchise by Pony Canyon and Comptiq. It features character designs and illustrations by artist Tsubasu Izumi, series composition and story by Team Yoree (Yoriko Tomita, Yasuko Kamo and Tatsuhiko Urahata), and music by Kohta Yamamoto. The story revolves around female junior high school idols who aim to become a top in Prism Stage, a nationwide tournament where many middle school idols compete and become top idols. These girls are divided into several units. Their stories are serialized in monthly Comptiq and short stories are released online via the official website.

Thank you for your service.
But under a new sky, a new love began to sprout.

4ever :goat:

---
## [DarkLevelSS13/IS12-Warfare](https://github.com/DarkLevelSS13/IS12-Warfare)@[1867654758...](https://github.com/DarkLevelSS13/IS12-Warfare/commit/186765475881bf58bbee319880653287d578820b)
#### Tuesday 2022-12-13 15:18:44 by Matt

Should fix the issue of loading the wrong CSS by making them all the same fuck you

---
## [redromnon/HeroicGamesLauncher](https://github.com/redromnon/HeroicGamesLauncher)@[3f6541c8a7...](https://github.com/redromnon/HeroicGamesLauncher/commit/3f6541c8a700511cea9f0c9b572a5d2138ee76e3)
#### Tuesday 2022-12-13 15:38:12 by Mathis Dröge

Improve README and developer experience (#1807)

* Update VSCode configuration

* Lots of README changes

- Update our bages; might've overdone it a little, but they're fun to add :^)
- Add badges for Web Technologies used
- Rewrite & bump up system requirements a bit
- Wrap the Language list, Development in a container, and Screenshots in
  <details>; this makes the page load faster and makes it seem less
  daunting
- Add a Flathub badge to the Flatpak section
- Unify Linux install instructions (as much as possible)
- Remove 3rd-party APT repository
  In my opinion, we have enough distribution formats already, and the
  install instructions are a little dodgy
- Add Beta AUR package to the list
- Clarify Windows install instructions by splitting up WinGet and manual
  install
- Make "Development environment" its own section
- Remove Beta and Alpha notes on Windows and macOS build instructions
- Explain what exactly is happening when you run `yarn dev` and in which
  scenarios you might want to use it
- Move the "Back to top" badge to the actual bottom of the page

* Add a Content Security Policy

This doesn't really do much in our situation:
- Just in case someone ever manages to load a website in Heroic's main
  window, no JS can run inside it
- Gets rid of the warning in the console when testing with `yarn dev`

I've tested the Webviews (unaffected) and links to ProtonDB and such
(also unaffected, not sure why though). Please test if this breaks
anything

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[70bcd3b6fb...](https://github.com/Huffie56/cmss13/commit/70bcd3b6fbcf17b4c26640321f23c83da0ab80a3)
#### Tuesday 2022-12-13 16:56:00 by carlarctg

Queen eye shuffles weed sprites when passing over them. (#1901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Queen eye shuffles weed sprites when passing over them.

Fixed some single letter vars so the mantainer agenda can't delay this
PR from merging.



<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game


> Queen eye shuffles weed sprites when passing over them.

It's a way for marines to know there's an entire queen eye looking over
them. Basically means an MD isn't 100% necessary to know the queen will
broadcast the location of your flank to the entire hive.

https://streamable.com/kmnd72

It's more subtle than i wanted it to be, but WCYD. Also doesn't work on
corner sprites.

Also, it looks fucking creepy as hell! It's awesome.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: Queen eye shuffles weed sprites when passing over them.
fix: Fixed some single letter vars so the mantainer agenda can't delay
this PR from merging.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [anoobindisguise/Cataclysm-DDA](https://github.com/anoobindisguise/Cataclysm-DDA)@[8e39d6f97c...](https://github.com/anoobindisguise/Cataclysm-DDA/commit/8e39d6f97c358c72a3dacc7c2f3ce955ecb30e81)
#### Tuesday 2022-12-13 17:14:34 by casswedson

fix: edge case ci error exit (#62660)

so a step of the reviewer workflow always runs, good it is the actual
magical step doing the hard work, but if the workflow gets canceled, the
step exits with an error code, I actually knew this but me from like a
day ago was like:
"nah man this won't bother me in the future."

guess what; after a couple hours I was felling the pain my perfectionist
subconscious was putting me through, plus odd error code exits aren't
very professional or clean or pleasing I'd say, also someone may think
it's weird, look into it, waste time looking at my code

title: do not draw much attention

Co-authored-by: casswedson <casswedson@users.noreply.github.com>

---
## [Jaden-PHILIPPINES/VGP-P3-2022-2023](https://github.com/Jaden-PHILIPPINES/VGP-P3-2022-2023)@[e96fdd137c...](https://github.com/Jaden-PHILIPPINES/VGP-P3-2022-2023/commit/e96fdd137c55d1e3c56bf8cd9f7689eb63c19b6b)
#### Tuesday 2022-12-13 17:24:57 by Jaden Morales

Revert "Fuck you luck"

This reverts commit d172736fc5497c08a7d96b9e75599b8c711769b5.

---
## [emillon/dune](https://github.com/emillon/dune)@[905c043f82...](https://github.com/emillon/dune/commit/905c043f82f575e75a75a2105ef16dc20c1c141c)
#### Tuesday 2022-12-13 18:00:38 by Etienne Millon

Add shell completion

This provides a shell completion mechanism for dune. This relies on the
bash completion API, which can be used with zsh as well.

The architecture is:

- `dune complete script` outputs a script to be sourced in the user's
  shell. It is comprised of a `_dune` function and the `complete -F
  _dune dune` command to register it. The `_dune` function can be used
  in cram tests to write natural-looking tests for this feature.
- this script calls `dune complete command` with the partial
  command-line. This internal command parses it to determine what the
  word being completed refers to: a command name, an argument name, or
  an argument value. The first two ones are part of the metadata
  `cmdliner` knows about; the last one is provided through a completion
  function that can be passed in one the `Arg` functions.
- the interface between `bash` and `dune complete command` is simple:
  it passes the command line and a position to complete at (this is
  necessary to encode the difference between `dune bui<tab>` and `dune
  build <tab>` for example), and reads an array from the output of the
  command.

The things I'm happy with:

- it is small!
- coverage is pretty good: command names, arguments (positional and
  optional, including optional arguments with optional names), and the
  `--` construct are supported. So, this is likely to improve the user
  experience already.
- it is easy to test through cram or unit tests (I chose the former).

Now, for the ugly bits...

- this effectively is a partial reimplementation of cmdliner inside
  `complete.ml`. If the exact parsing rules are different, it means that
  we can complete to something with different or wrong semantics.
- the vendored copy of cmdliner is patched to expose so that it is
  possible to use the private APIs. these two points need to be resolved
  before we can think about how to upstream this.
- some bits of the cmdliner API need to be modified to provide
  completion automatically. For example for things like `enum` it's easy
  to provide a completion function automatically.
- it is difficult to define the right API for the completion functions.
  `unit -> string list` is a first approximation but with some
  limitations. For example, getting a list of buildable targets needs to
  run under `Fiber`, but we can't pollute the API with it. Interestingly
  enough, algebraic effects seem like they would be an interesting
  solution for this.
- at the moment, we're not relying on the shell's completion helpers to
  complete things like filenames. To support this we would either need
  to implement that in OCaml, or extend the bash/dune interface so that
  the completion function could call `compgen -f` based on the dune
  output.
- as a way to tie the two previous points: if we wanted to complete
  `dune build dir/file<tab>`, it would be a lot more efficient to pass
  the prefix to the build system and let it compute just the targets
  that match this, rather than compute everything and filter it
  afterwards. So that prefix would need to appear in the completion API.

Signed-off-by: Etienne Millon <me@emillon.org>

---
## [steven52880/Grasscutter](https://github.com/steven52880/Grasscutter)@[88bc5c4c54...](https://github.com/steven52880/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Tuesday 2022-12-13 20:36:03 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [mpaliwoda/advent-of-code-2022](https://github.com/mpaliwoda/advent-of-code-2022)@[2b008f87a2...](https://github.com/mpaliwoda/advent-of-code-2022/commit/2b008f87a2e80dca7fadd17e52349b99643abece)
#### Tuesday 2022-12-13 21:04:57 by Marcin Paliwoda

Day 9 - Dear diary,

Brain fried, I think I'm gonna give up soon.

Please send help as I'm unable to understand what's going on anymore.

Lovely elves, please don't make me go on that rope again.
The only worse thing to happen to me would be implementing A* algo.
Hope that doesn't happen.

// narrator:
//      it totally will happen

---
## [vbraun/sage](https://github.com/vbraun/sage)@[d2a2415104...](https://github.com/vbraun/sage/commit/d2a2415104cfacbf2d13f8930e6457bf36b39e17)
#### Tuesday 2022-12-13 21:45:13 by Release Manager

Trac #32841: zn_poly removal

The zn_poly SPKG is used by sage in only one place. In hypellfrob.cpp's
`interval_products_wrapper()`, there is a case...

{{{#!C++
if (!force_ntl  &&  modulus <= (1UL << (ULONG_BITS - 1)) - 1)
{
   // Small modulus; let's try using zn_poly if we're allowed.
   ...
}}}

But sometimes that fails, and the fallback is to use NTL anyway. The
zn_poly project was abandoned upstream in 2008:

  https://web.maths.unsw.edu.au/~davidharvey/code/zn_poly/index.html

We've forked it to keep it building on modern systems,

  https://gitlab.com/sagemath/zn_poly

but the build system is still a mess. Erik started an autotools branch
(https://gitlab.com/sagemath/zn_poly/-/tree/autotooling), but it never
got finished, because the source layout is a bit weird for autotools and
it should most likely be redone from scratch.

And zn_poly is not packaged in Gentoo because of how many hacks it still
requires to build on a distro with stronger user experience
expectations:

  https://github.com/cschwan/sage-on-gentoo/blob/master/sci-
libs/zn_poly/zn_poly-0.9.2.ebuild

In short, we're not getting a lot of benefit out of zn_poly these days,
and nothing breaks if we remove it, because the one function that uses
it falls back to the more-reliable NTL anyway.

In this ticket we remove the zn_poly SPKG, to avoid having to rewrite
its build system some day.

URL: https://trac.sagemath.org/32841
Reported by: mjo
Ticket author(s): Michael Orlitzky
Reviewer(s): Dima Pasechnik

---
## [RimiNosha/Skyrat-tg](https://github.com/RimiNosha/Skyrat-tg)@[84b1612201...](https://github.com/RimiNosha/Skyrat-tg/commit/84b161220115e3243272299b3f8f3cb29d484709)
#### Tuesday 2022-12-13 21:49:34 by SkyratBot

[MIRROR] Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. [MDB IGNORE] (#18019)

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. (#71674)

## About The Pull Request

- The chaplain choice beacon now uses a radial to select the armor set,
instead of a list, giving the user a preview of what each looks like.

![image](https://user-images.githubusercontent.com/51863163/205417930-f5ceab11-6974-48a9-a871-abcb8228bcf2.png)

- Lots of additional cleanup to choice beacon code in general. Less copy
pasted code.
- All beacons now speak from the beacon with their message, instead of
some going by "headset message". Soul removed

## Why It's Good For The Game

I always forgot when selecting my armor which looks like what, and
choosing an ugly one is a pain since you only get one choice. This
should help chaplains get the armor they actually want without needing
to check the wiki.

## Changelog

:cl: Melbert
qol: The chaplain's armament beacon now displays a radial instead of a
text list, showing previews of what all the armor sets look like
qol: (Almost) all choice beacons now use a pod to send their item,
instead of just magicking it under your feet
code: Cleaned up some choice beacon code.
/:cl:

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup.

* update modular

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [EastsidePreparatorySchool/ChemLogs](https://github.com/EastsidePreparatorySchool/ChemLogs)@[5378148e25...](https://github.com/EastsidePreparatorySchool/ChemLogs/commit/5378148e25d6156a49286cc3311862a8389b469c)
#### Tuesday 2022-12-13 23:11:51 by Cluelessbutnothomeless

Test Page for Chemical Searching

When I started this page I had no idea what I was doing. I still have no idea what I am doing. But I can attest that the above code works, the majority of the time at least. I'm not sure how detailed this description is supposed to be but I will keep it short. It looks good I guess, at the very least its not an abhorrent aberration grotesque to all animal eyes. So that's good. :) While some might say I took my inspiration from the Nordstrom Active Apparel website I would be quick to remind them that there is a high possibility that Nordstrom stole their design form someone else and therefore my acting is the equivalent of balancing the cosmic scales. Now I'm sure being a cosmic balancer puts me dead in the sights of more than one ancient prophecy but I will remind the reader that I am still me. Still the same coder struggling to comprehend whether or not html is a language or a jumble of misshapen letters. Alas we have come to the end of my summary, I should hope it was informative to have a description of my mindset when coding the page. Maybe even helpful? Humbly, Aroura

---
## [maesierra/adventOfCode2022](https://github.com/maesierra/adventOfCode2022)@[ca98746e21...](https://github.com/maesierra/adventOfCode2022/commit/ca98746e21cc1b3229a21da809e2d5a5e98dd8f3)
#### Tuesday 2022-12-13 23:44:29 by maesierra

day13

Today was extremelly painful in Go. Object Oriented Programing is good. Inheritance is good
It doesn't solve all the problems, but for some of them is so elegant an nice.

Aparently you cannot cast from interface into concrete type and with no method overloading there is no way to do Comparable interface
At least int good old C you can cast a pointer into anything (be a pointer my friend)
In the end I have to do a horrible solution with composition. Yes you can use composition instead of inheritance but is ugly and more error prone

And pointers... I'm getting used to start thining in pointer terms
again. But I'd rather write stupid Java boilerplate than having this
headaches of pointers. Pointers are difficult and error-prone

---
## [nuke-ops/Nostra-13](https://github.com/nuke-ops/Nostra-13)@[8eec99b320...](https://github.com/nuke-ops/Nostra-13/commit/8eec99b3206e917bd711987a80422168de53f83d)
#### Tuesday 2022-12-13 23:55:19 by LemonInTheDark

Caches GetJobName. Fuck you (#274)

* Caches GetJobName. Fuck you

This code made me deeply upset, WHY IS IT RECURSIVE WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY

* Centcom handling, properly this time

* Empties out real_job_name

* Sets real_job_name up in the right place

* Moves real_job_name to SSjob, uses modularTM

* Yeet

* Removes old code, swaps over to the SSjob list

* dme changes

* indents... comments

Co-authored-by: SandPoot <enric_gabirel@hotmail.com>

---

