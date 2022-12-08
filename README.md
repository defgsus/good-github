## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-07](docs/good-messages/2022/2022-12-07.md)


2,050,340 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,050,340 were push events containing 3,127,234 commit messages that amount to 255,746,657 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[6120721323...](https://github.com/sleepynecrons/cmss13/commit/6120721323b6431a1d43d89d7354e1ea1763a734)
#### Wednesday 2022-12-07 00:06:12 by carlarctg

Added various flasks to loadouts and canteen vendors. (#1802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Added a canteen (item) from an unused sprite.

Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

All flasks (and canteen (item)) can be selected in the character loadout
items menu at the bottom.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

The old W-Y flask looked more like a skull than the logo. The gold badge
bit was legacy from bay12.

> Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Legacy renaming.

> Added a canteen (item) from an unused sprite.

Cool sprite. Fucked up we didn't have canteens until now when, uh.
That's what people actually use in the military, not flasks. (To my
knowledge)

> Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

Canteens are the standard military container, W-Y flasks in the vendors
are a good Lore way to show how much of a WY suckup the USCM is.

> All flasks, vacuum and leather included, (and canteen (item)) can be
selected in the character loadout items menu at the bottom.

I think these flasks are cool ways to add flavor to your character, and
it's a shame most of them either weren't in the game or were in very
annoying to find places.

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

imageadd: Resprited the W-Y Flask. Removed the gold badge from the
former detective's flask.
add: Renamed the former detective's flask and bar flask into the brown
and black, respectively, leather flasks.
add: Added a canteen (item) from an unused sprite.
add: Canteens (item) and W-Y flasks can now be found in the canteen
(place) vendors.
add: All flasks, vacuum and leather included, (and canteen (item)) can
be selected in the character loadout items menu at the bottom.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [Luunae/advent-of-code-2022](https://github.com/Luunae/advent-of-code-2022)@[91a78c61cb...](https://github.com/Luunae/advent-of-code-2022/commit/91a78c61cb8d9df0280a3f7a890be7b74a3b87dc)
#### Wednesday 2022-12-07 00:39:48 by Luna

Refactored to allow for addition of testing

Goddesses fucking damnit I hate the typing/usability tradeoff.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[c8f4d4ae04...](https://github.com/cmss13-devs/cmss13/commit/c8f4d4ae042be6fb59f29031eb0a56926e32ab3a)
#### Wednesday 2022-12-07 01:16:02 by carlarctg

Money Rework (#1831)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Added a variable to paygrades called pay_multiplier. This multiplies the
starting amount of money from bank accounts.

Refactored how bank accounts are created so the above could work.

Drastically nuked the amount of money people start with. People can no
longer start with thousands of dollars.... they now get 30-50. This
value is multiplied by the pay_multiplier below.

Added pay_multiplier to all paygrades. The higher your rank, the more
money you'll start with, based on this multiplier. (For example, a Major
will have a pay multiplier of 4.) Includes strange roles like VAIPO,
UPP, PMCs, RESS...

Non-binary WY executives may now spawn with 'Mx.' as their
communications prefix.

Altered the prices of cigarette vending machines around to overall make
them more expensive. PFCs will not be able to buy Executive Select with
their starting cash.

Made cassetes and Souto from vendors more expensive. Buying food from
Hot Foods now costs money. Marine coffee now has an appropiate
description. Souto vendors no longer vend water bottles.

Fixed default parent type dollar items being worth 0 money...

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

> Drastically nuked the amount of money people start with. People can no
longer start with thousands of dollars.... they now get 30-50. This
value is multiplied by the pay_multiplier below.

Lore. The live of a private sucks. Monkeysfist suggested this value.
Still enough to buy all essentials, scavenge some money if you want to
buy the good cigarette packs down in the colony.

> Added pay_multiplier to all paygrades. The higher your rank, the more
money you'll start with, based on this multiplier. (For example, a Major
will have a pay multiplier of 4.) Includes strange roles like VAIPO,
UPP, PMCs, RESS...

Why were paygrades added without affecting pay. Why could PFCs start
with 3 thousand dollars and COs with 50 dollars total.

> Non-binary WY executives may now spawn with 'Mx.' as their
communications prefix.

Inclusivity win! Doesn't actually do anything as we do not have
nonbinary characters.

> Altered the prices of cigarette vending machines around to overall
make them more expensive. PFCs will not be able to buy Executive Select
with their starting cash.

> Made cassetes and Souto from vendors more expensive. Buying food from
Hot Foods now costs money. Marine coffee now has an appropiate
description. Souto vendors no longer vend water bottles.

It's funny to make the lives of marines miserable.

> Fixed default parent type dollar items being worth 0 money...

This will let marines money scrounge.

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

Irrelevant.

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
add: Added pay_multiplier to all paygrades. The higher your rank, the
more money you'll start with, based on this multiplier. (For example, a
Major will have a pay multiplier of 4.) Includes strange roles like
VAIPO, UPP, PMCs, RESS...
del: Drastically nuked the amount of money people start with. People can
no longer start with thousands of dollars.... they now get 30-50 dollars
total. This value is multiplied by the pay_multiplier above.
spellcheck: Non-binary WY executives may now spawn with 'Mx.' as their
communications prefix.
balance: Altered the prices of cigarette vending machines around to
overall make them more expensive. PFCs will not be able to buy Executive
Select with their starting cash.
del: Made cassetes and Souto from vendors more expensive. Buying food
from Hot Foods now costs money. Marine coffee now has an appropiate
description. Souto vendors no longer vend water bottles.
fix: Fixed default parent type dollar items being worth 0 money...
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [TheNeoGamer42/Shiptest](https://github.com/TheNeoGamer42/Shiptest)@[3efa9b5382...](https://github.com/TheNeoGamer42/Shiptest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Wednesday 2022-12-07 01:42:20 by Zevotech

undoes a fuckup on a ruin (#1578)

* undoes a fuckup on a ruin
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
sets light range to 2 on the ruin areas of beach_colony.dmm
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the brackets) if you have tested your changes and this is ready for review. Leave unticked if you have yet to test your changes and this is not ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that any issues found during tested have been addressed.

## Why It's Good For The Game
the ruin is no longer pitch fucking dark in the middle of a daylit planet (hopefully)
<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
fix: changes light range to 2 on the areas of beach_colony
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

* im stupid

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[eb4886c115...](https://github.com/ThePiachu/cmss13/commit/eb4886c115a0965a347783b87eb3415f098c2c1f)
#### Wednesday 2022-12-07 02:04:49 by carlarctg

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
## [SPLURT-Station/S.P.L.U.R.T-Station-13](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13)@[8eec99b320...](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13/commit/8eec99b3206e917bd711987a80422168de53f83d)
#### Wednesday 2022-12-07 02:22:33 by LemonInTheDark

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
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[9499a1542b...](https://github.com/Jolly-66/tgstation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Wednesday 2022-12-07 02:37:22 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

---
## [gavinhoward/bc](https://github.com/gavinhoward/bc)@[3cb0a4b2ec...](https://github.com/gavinhoward/bc/commit/3cb0a4b2ec65cfed9d147180230e416b4639e834)
#### Wednesday 2022-12-07 02:46:46 by Gavin Howard

Fix the fatal I/O error with editline on FreeBSD-CURRENT and dwm

This was caused by libedit returning an error when it was just
interrupted. I assumed libedit would be better than that. <facepalm>

I should not have assumed.

Unfortunately, libedit is still a problem because it will forget
everything typed at the prompt. It will also reprint the prompt if I
don't tell it not to. Hence, the extra global boolean in this commit.

So yeah, libedit sucks.

Signed-off-by: Gavin Howard <gavin@yzena.com>

---
## [martinjosef97/app-dev](https://github.com/martinjosef97/app-dev)@[4d73262f85...](https://github.com/martinjosef97/app-dev/commit/4d73262f85f22a4cedd1f2b994cc15f932901619)
#### Wednesday 2022-12-07 04:47:43 by martinjosef97

Rev .1

*Added Movie Titles and Bugfixes v0.1 Alpha
Sonic The Movie is about a blue hedgehog that saves the city.
The Simpsons is a Comedy Show from the 90s and has been adopted in a movie once.
Back to The Future is about time travel between Marty which he needs to save the doctor before his death.
Dumb and Dumber is about two idiots driving a car and causing chaos in the city.
Willy Wonka is about a magical chocolate factory making experimental chocolates for kids and alike.
Thunder Days is about a racer that has been injured and recovered miraculously and tried to race again.
Friday the 13th is about a serial killer that hunts people in the Fridays of the 13th.
Home Alone is about a boy that is stuck in New York and is finding his way back to his home town in order to see his parents again.

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[9bacf1ac5c...](https://github.com/Offroaders123/NBTify/commit/9bacf1ac5c3a4b9b27279322be28e64c2ad78de5)
#### Wednesday 2022-12-07 04:53:41 by Offroaders123

Explicit Read Options

Added support for explicitly disabling specific read properties as needed. Previously, the `read()` function would always just smart it's way around getting the file to open, but I want to also allow you to try and open the data as you need to. If you want to try and specifically open a file using big endian, and with a Bedrock header, why not? Not sure what kind of wackiness is out there, so this allows you to be more explicit with what exactly you're trying to open. I think this could be helpful if you're trying to figure out the format of an existing NBT file you may have, and to where NBTify isn't able to deduce it's format for some reason. More config, the better!

This first version for these additional options initially deal with declaring no compression is used, and that a Bedrock header check should/n't be performed or not. Next one to work on will be the `isNamed` option, which will be replacing `named`. I'm using the `is-*` prefix since that will better represent that you are passing a boolean, rather than a value, unlike the options for the `NBTData` constructor, and `write()` function, which accept the values themselves, which will then in return distinguish which format settings you'd like to use.

TypeScript also really helped out with this a lot. I also tried to do this a while back, but things got too messy/confusing. I left it to the auto setting (which works great on it's own) until I could figure it out exactly. Another big part is deciding to use `null` to represent where you specifically don't want a config option to be set. `undefined` is essentially reserved for what auto/smart would be, and `null` is for where you don't want to use any of the option values, or the auto/smart setting. This `null` behavior is only applicable to optional properties, like `compression` or `isBedrockLevel`, whereas `endian` has to be either `big`, `little`, or auto/smart. That one has to be provided one way or another.

This also fixes being able to pass in `zlib` as a compression format, and the `read()` function still auto-reading as `gzip`. Yeah, that was super wonky. `zlib` has merely been a placeholder for the whole time so far though, so it's not breaking or anything for it to not have worked in the first place. Still weird though. So now `compression` has to be explicity set to `gzip` or left as `undefined` to decompress with gzip, and it won't work with anything else (`zlib` or `null`).

---
## [keydon/adventOfCode](https://github.com/keydon/adventOfCode)@[5295c407b2...](https://github.com/keydon/adventOfCode/commit/5295c407b27ea1a004ead42f0a46b9bf062bbe97)
#### Wednesday 2022-12-07 04:58:10 by Lukas Bugaj

--- Day 6: Tuning Trouble ---
The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the star fruit grove.

As you move through the dense undergrowth, one of the Elves gives you a handheld device. He says that it has many fancy features, but the most important one to set up right now is the communication system.

However, because he's heard you have significant experience dealing with signal-based systems, he convinced the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.

How many characters need to be processed before the first start-of-packet marker is detected?

--- Part Two ---
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

How many characters need to be processed before the first start-of-message marker is detected?

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[e10c157179...](https://github.com/Offroaders123/NBTify/commit/e10c1571791ca760d4c8562fee0ddd50ace50592)
#### Wednesday 2022-12-07 04:59:41 by Offroaders123

isNamed Option: Part Two

This adds the actual implementation for the `isNamed` handling. It also includes the auto handling too :O

That Never Nester technique is working wonders on this function. These optional property code block handling segments work amazing! I didn't even see that pattern until I did the Never Nester trick on it. This essentially makes it so the rest of the function after the checks are marked as safe (non-`undefined`), since they return early from the function with the correct value! Outstandingly neat!!! That happened to work out that way, I'm not sure if I could've planned that structure. I was gonna make a snippet to describe it to you to see how it works, but I'm not gonna make a demo as close to the actual code that shows how it works, haha. I tried to make it, but it's just the same code again. So the island exit early lines are on lines 35 and 49 of `read.ts`. They will deduce the property type of the file using `try {} catch {}` blocks, and then they will re-call the same function again, recursively until one of the types passes! (That description actually turned out really nice) This in result causes everything after the recursive-call blocks to then narrow the parameter type to remove `undefined`, because you already `return`ed from that initial function call, where it wasn't declared! It's then in that next function call where that parameter has now been deduced, and is no longer `undefined`. Wow. Wow, wow, wow, wow, WOW! Maybe there's a graph-like tool in Chrome DevTools that can draw out the function stack so you can see how it runs? That would probably help explain it too.

This is sick, I love that this is a thing. Oh yeah, this project is turning a year old in about a week. Pog XD

*Edit: Oh yeah, I was gonna initially try to add the `isNamed` handling further into the `endian` try-catch loop, but this setup renders that totally unnecessary! I'm super happy about that, because that would've without question been a spaghetti code nightmare with even more nested try-catch statements. I already don't like how many try-catch nestings there are, and that would've made it a lot worse. I may look into adding `.catch()` statements to the end of the `await` calls, luckily since the `read()` function is async. I know how to use `.then()` nicely now, but I haven't done much with `.catch()` yet. Guess there's no reason to `await` around, HAHA! I think that may take care of some of the try-catch nesting hopefully. That would look amazing as simple callbacks :)

---
## [Sala/adventofcode](https://github.com/Sala/adventofcode)@[34ac077de4...](https://github.com/Sala/adventofcode/commit/34ac077de4558db28868d59be06a4d626fffab95)
#### Wednesday 2022-12-07 05:52:32 by sălă

today was a good day for science.
happy with the result and the structure
you could say that "hai că s-a terminat șmecheria"
last night we had a really nice gathering with some college friends

---
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[860f1f6dee...](https://github.com/rHermes/adventofcode/commit/860f1f6dee1b655e028a63a86a1b919e3ab90e47)
#### Wednesday 2022-12-07 06:06:34 by Teodor Spæren

2022 Day 7

Well, finally a good task! This was very interesting!

It's a very interesting task, especially if you only see part 1. You
have two choices, which is either to just focus on the files, or to
actually build a tree structure with empty directories also. I chose to
go for just files in the end, but I spent a bit of time deciding this,
which turned out to be a mistake in the end.

What I spent the most time on here, was actually building the logical
tree. I should have been better here, I simply couldn't get my head
around it for a little while, but it's really quite simple. You can just
keep a list of the files and for each of them update the size of all
directories above. This is what I ended up doing, but I got side
tracked, thinking I should do this more effectively by building up the
total size from the bottom up.

This is more effective, but it's also harder. There are so few files in
this tree, so in the end I just went for a more bruteforce solution. I
might clean this up more later.

The second part came quite easy, once I had parsed the task correctly.

I didn't do to well on the leaderboard, mainly due to using so long  on
building the logical tree. I blame this on early in the morning, but
more importantly not having done the important work of warming up with
graph structures in python before AoC this year.

Either way, this was a really good day, hoping for more days like this!

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  7   00:30:11   2041      0   00:34:46   1667      0

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[25d4afc869...](https://github.com/Jackraxxus/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Wednesday 2022-12-07 06:07:10 by Iamgoofball

Retires explosive lance crafting to a nice farm upstate where it has plenty of room to run around (#71256)

## About The Pull Request

You can no longer craft explosive lances.

## Why It's Good For The Game

Explosive lances are unhealthy for the game in it's current iteration.
Many years ago when the game was more loose and we weren't dealing with
players who treat the game like competitive TTT or Town of Salem,

They are a one shot kill weapon, which is the most powerful kind of
weapon in every gamemode. @JohnFulpWillard likened it to 1f1, a concept
from Town of Salem players where the town trades 1 person for 1 bad guy.

Modern ss13 design includes a significantly heavier load of antagonists
that aren't fixed roundstart compared to when the e-lance went in.

When we added the e-lance, if nuke ops spawned, that was it, there was
nuke ops, if you e-lanced the nuke ops and died you were dead until the
next round.

Nowadays you're rolling for lone operative, blob, wizard, disease,
revenant, and every other fun enjoyable antagonist role under the sun.

I can e-lance a nuke op/cultist/traitor/revolutionary/any bad guy in the
game as a non-antag assistant, die, and have a good chance to roll
another, way more fun antag in deadchat.

My change to make the e-lance a proper "we both die" tool didn't
actually help because I didn't quite realize that to the modern SS13
player because of how we designed Dynamic and antagonists in the modern
era, death is, frankly, not a punishment anymore.

It's time we admit the facts, items designed in 2015 SS13 in #12389
simply don't hold up in a healthy manner in 2022 SS13. Dying in SS13 in
2015 was a significantly different experience with different
consequences than it has now, and right now "kills you when you use it"
is not the same massive downside it was 7-8 years ago.

## Changelog
:cl:
del: You can no longer craft explosive lances.
/:cl:

---
## [AllanTaylor314/AdventOfCode](https://github.com/AllanTaylor314/AdventOfCode)@[ac44edfaa9...](https://github.com/AllanTaylor314/AdventOfCode/commit/ac44edfaa968808187b9df13e0673ba38e8e7e8b)
#### Wednesday 2022-12-07 06:19:09 by Allan Taylor

2022 Day 7

This is awful - globals everywhere and horrible hacks. I might tidy it up, or it might stay like this forever

---
## [01ste02/AoC2022](https://github.com/01ste02/AoC2022)@[44a3f39a2b...](https://github.com/01ste02/AoC2022/commit/44a3f39a2bb35f6bc5acf5448a04e0efa3f4bcf8)
#### Wednesday 2022-12-07 06:50:08 by Oskar Stenberg

Day 7. Advent of Bash going strong - but I will start slipping down from place 12 now. It took me 20 minutes to sort and find the smallest directory needed. Bash has limitations in places I do not like to admit, but it works. I'll be damned if it doesn't work. It still feels like a good idea and experience to write these challenges in bash - even though the language is not really made for it - but the portability of it is amazing. No compiler to install, and can run on most systems by default. I believe that all my solutions so far would be sh-compatible as well..

---
## [etherware-novice/tgbagilsstation](https://github.com/etherware-novice/tgbagilsstation)@[e9cff525dc...](https://github.com/etherware-novice/tgbagilsstation/commit/e9cff525dc5b57153af3b4bb9039de08d6823805)
#### Wednesday 2022-12-07 07:09:19 by tralezab

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
## [etherware-novice/tgbagilsstation](https://github.com/etherware-novice/tgbagilsstation)@[ebc0227176...](https://github.com/etherware-novice/tgbagilsstation/commit/ebc0227176b5213f379eefc3f5c6aa7be2d09c0a)
#### Wednesday 2022-12-07 07:09:19 by Tastyfish

Makes dog a basic mob [MDB IGNORE] (#70799)


About The Pull Request

    Made a basic version of the pet base called /mob/living/basic/pet. It's significantly more stripped down from the old simple_animal one, because its half collar stuff and...

    Made the collar slot a component that you could theoretically remove from a pet to disable the behavior, or add to any other living mob as long as you set up the icon states for the collar (or not, the visuals are optional).
        The corgi's collar strippable slot is now generally the pet collar slot, and in theory could be used for other pet stripping screens.

    I also gutted the extra access card code from /mob/living/basic/pet as it's only being used by corgis. Having a physical ID is now just inherent to corgis, as they're the only ones that could equip it anyway.

    Ported the make_babies() function from simple_animals to a new subtree and associated behavior, called /datum/ai_planning_subtree/make_babies that uses blackboards to know the animal-specific info.
        Note that it's marginally improved, as the female walks to the male first instead of bluespace reproduction.

    Tweaked and improved the dog AI to work as a basic mob, including making /datum/idle_behavior/idle_dog fully functional.

    Made a /datum/ai_planning_subtree/random_speech/dog that pulls the dynamic speech and emotes to support dog fashion.

I've tested base collars across multiple pet types.

For dogs, I've tested general behavior, fetching, reproduction, dog fashion, and deadchat_plays, covering all the oddities I'm aware of.

image
Why It's Good For The Game

Very big mob converted to a basic mob.
Changelog

cl
fix: Lisa no longer uses bluespace when interacting with Ian.
refactor: A large portion of dog code was re-written; please report any strange bugs.
/cl

---
## [JoshuaMeyer1/InvestmentPortfolioManagementSystem](https://github.com/JoshuaMeyer1/InvestmentPortfolioManagementSystem)@[ebb145c0a3...](https://github.com/JoshuaMeyer1/InvestmentPortfolioManagementSystem/commit/ebb145c0a3f260c51f82a14bf3a8d23ea44e4fbb)
#### Wednesday 2022-12-07 07:20:33 by sjs262

GOT THE GRAPH WORKING FUCK YOU CHARTJS YOU SHIT OF PIECE

---
## [tbg/cockroach](https://github.com/tbg/cockroach)@[97054a0e76...](https://github.com/tbg/cockroach/commit/97054a0e76049cd8f78d8b534ab1e2107be9f2ed)
#### Wednesday 2022-12-07 07:57:58 by Tobias Grieger

kvnemesis: uniquely identify all versions

This is essentially a v2 of kvnemesis. While a lot of code has changed, it's not a rewrite, rather we are actually bringing kvnemesis closer to the idea which ultimately led to it being built. That idea is that if values can uniquely identify the operation which wrote them, serializability checking becomes easier as any observation of a value totally orders the reader and the writer with respect to each other. "Easier" meant both simpler code, as well as actually being able to computationally do the verification on complex histories.

Prior to this PR, kvnemesis was writing unique values where it could, but it couldn't do it for deletions - after all, a deletion is like writing a "nothing" to MVCC, and there wasn't any way to make two "nothings" distinguishable. Having broken with the basic premise of unique values, there was a lot of bending over backwards going on to avoid, for the most part, devolving into a "normal" serializability checker. However, for contrived edge cases this would not be avoidable, and so there would be histories that kvnemesis just couldn't handle.

"v2" (this PR) gets this right. The main contribution is that we now thread kvnemesis' sequence numbers all the way down into MVCC and back up with the RangeFeed. Values are now truly unique: a deletion tombstone is identifiable via its `MVCCValueHeader`, which carries the `kvnemesisutil.Seq` of the `Operation` that originally wrote it. On top of this, everything "just works" as you expect.

Plumbing testing-only fields through the KV API protobufs isn't something that was taken lightly and that required a good amount of deliberation. However, we figured out a clever (maybe too clever?) way to have these fields be zero-sized in production, meaning they cannot possibly affect production logic and they also do not influence struct sizes or the wire encoding. As a drawback, kvnemesis requires the `crdb_test` build tag (it will `t.Skip()` otherwise).

The remainder of this PR is mostly improvements in code quality. `echodriven` testing was introduced for many of the tests that could benefit from it. The core components of kvnemesis were reworked for clarity (the author spent the first week very confused and wishes for that experience to remain unrepeated by anyone). kvnemesis also tracks the execution timestamps as reported by the KV layer, which a future change could [use](https://github.com/cockroachdb/cockroach/issues/92898) for additional validation.

Of note is the updated doc comment, which is reproduced below in entirety.

Fixes #90955.
Fixes #88988.
Fixes #76435.
Fixes #69642.

----

Package kvnemesis exercises the KV API with random concurrent traffic (as
well as splits, merges, etc) and then validates that the observed behaviors
are serializable.

It does so in polynomial time based on the techniques used by [Elle] (see in
particular section 4.2.3), using the after-the-fact MVCC history as a record
of truth. It ensures that all write operations embed a unique identifier that
is stored in MVCC history, and can thus identify which of its operations'
mutations are reflected in the database ("recoverability" in Elle parlance).

A run of kvnemesis proceeds as follows.

First, a Generator is instantiated. It can create, upon request, a sequence
in which each element is a random Operation. Operations that are mutations
(i.e. not pure reads) are assigned a unique kvnemesisutil.Seq which will be
stored alongside the MVCC data written by the Operation.

A pool of worker threads concurrently generates Operations and executes them
against a CockroachDB cluster. Some of these Operations may
succeed, some may fail, and for some of them an ambiguous result may be
encountered.
Alongside this random traffic, kvnemesis maintains a RangeFeed that ingests
the MVCC history. This creates a "carbon copy" of the MVCC history.

All of these workers wind down once they have in aggregate completed a
configured number of steps.

Next, kvnemesis validates that the Operations that were executed and the
results they saw match the MVCC history, i.e. checks for Serializability. In
general, this is an NP-hard problem[^1], but the use of unique sequence
numbers (kvnemesisutil.Seq) makes it tractable, as each mutation in the MVCC
keyspace uniquely identifies the Operation that must have written the value.

We make use of this property as follows. First, the Validate method iterates
through all Operations performed and, for each, inspects

- the type of the Operation (i.e. Put, Delete, Get, ...),
- the (point or range) key of the operation, and
- its results (i.e. whether there was an error or which key-value pairs were returned).

Each atomic unit (i.e. individual non-transactional operation, or batch of
non-transactional operations, or transaction) results in a slice (in order
in which the Operations within executed[^2]) of observations, where each
element is either an observed read or an observed write.

For example, a Batch that first writes `v1` to `k1`, then scans `[k1-k3)`
(reading its own write as well as some other key k2 with value v2) and then
deletes `k3` would generate the following slice:

       [
         observedWrite(k1->v1),
         observedScan(k1->v1, k2->v2),
         observedWrite(k3->v3),
       ]

Each such slice (i.e. atomic unit) will then be compared to the MVCC history.
For all units that succeeded, their writes must match up with versions in
the MVCC history, and this matching is trivial thanks to unique values
(including for deletions, since we embed the kvnemesisutil.Seq in the value),
and in particular a single write will entirely fix the MVCC timestamp at
which the atomic unit must have executed.

For each read (i.e. get or scan), we compute at which time intervals each
read would have been valid. For example, if the MVCC history for a key `k1`
is as follows:

                  k1

       	 -----------------
       	 t5      v2
       	 t4
       	 t3
       	 t2     <del>
       	 t1      v1

then

  - observedGet(k1->v1)  is valid for [t1,t2),
  - observedGet(k1->nil) is valid for [0,t1) and [t2,t5), and
  - observedGet(k1->v2)  is valid for [t5,inf).

By intersecting the time intervals for each Operation in an atomic unit, we
then get the MVCC timestamps at which this Operation would have observed what
it ended up observing. If this intersection is empty, serializability must have
been violated.

In the error case, kvnemesis verifies that no part of the Operation became visible.
For ambiguous results, kvnemesis requires that either no Operation become visible,
or otherwise treats the atomic unit as committed.

The KV API also has the capability to return the actual execution timestamp directly
with responses. At the time of writing, kvnemesis does verify that it does do this
reliably, but it does not verify that the execution timestamp is contained in the
intersection of time intervals obtained from inspecting MVCC history[^3].

[Elle]: https://arxiv.org/pdf/2003.10554.pdf
[^1]: https://dl.acm.org/doi/10.1145/322154.322158
[^2]: there is currently concurrency within the atomic unit in kvnemesis. It
could in theory carry out multiple reads concurrently while not also writing,
such as DistSQL does, but this is not implemented today. See:
https://github.com/cockroachdb/cockroach/issues/64825
[^3]: tracked in https://github.com/cockroachdb/cockroach/issues/92898.

Epic: none
Release note: None

---
## [thomaspeeler/stats15final](https://github.com/thomaspeeler/stats15final)@[0d88f34eb2...](https://github.com/thomaspeeler/stats15final/commit/0d88f34eb2453ceb83a21b52125e7599d60c944f)
#### Wednesday 2022-12-07 08:02:09 by thomaspeeler

done(?)

i cant be bothered to do any more data modeling, i don't think its going to really be of any use, the section is worth 40 points but i don't fucking know what he wants, so what we have is what he gets; for the section i mostly took inspiration from the airbnb report, minus residual plots because i don't know how those work at all and i don't think he'll be expecting something of that caliber. the report is at 46 pages so its fine for length but i think all that's needed to finishing touches on univariate color and then final overview to fix anything that's off. ill start compiling findings tomorrow but i wrote a lengthy conclusion section that summarizes most things. I'm very tired.

its midnight. there are people yelling outside.

---
## [limchiawei9539/Grasscutter](https://github.com/limchiawei9539/Grasscutter)@[88bc5c4c54...](https://github.com/limchiawei9539/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Wednesday 2022-12-07 08:29:07 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [tomponline/lxd](https://github.com/tomponline/lxd)@[bc1e75f7c8...](https://github.com/tomponline/lxd/commit/bc1e75f7c84b2bb284037ba3fd8be2b8031ddc45)
#### Wednesday 2022-12-07 08:48:56 by Thomas Parrott

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
## [LukasH0lm/MyTunes](https://github.com/LukasH0lm/MyTunes)@[6fd173dc55...](https://github.com/LukasH0lm/MyTunes/commit/6fd173dc5556010e91a64e913f993ed8e3e9d5b2)
#### Wednesday 2022-12-07 11:23:41 by lukash0lm

Fixed Sune's shit ass volume bar
bro legit why the fuck did he do it so bøffet, like fr tho who the fuck initializes a volume bar's max value to the current value like wtf?????

---
## [NoKohi/cmss13](https://github.com/NoKohi/cmss13)@[146d4a3fa8...](https://github.com/NoKohi/cmss13/commit/146d4a3fa87a25a16e7246c32d85b6b57614adc5)
#### Wednesday 2022-12-07 11:50:52 by carlarctg

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
## [MikaelahJ/EmployeeOfTheMonth](https://github.com/MikaelahJ/EmployeeOfTheMonth)@[c42a3aa1e7...](https://github.com/MikaelahJ/EmployeeOfTheMonth/commit/c42a3aa1e72c6fb1ae32e782b90b9abe1ddcadc2)
#### Wednesday 2022-12-07 11:54:29 by turbosnacko

BloodsplashDMGtaken

Frames för en animation som spelas upp när spelaren tar damage. Det är en skvätt med blod.

“They say when you die, you shit your pants, but not me. I’m gonna shit my heart.” – Xavier

---
## [VoltageOS-staging/frameworks_base](https://github.com/VoltageOS-staging/frameworks_base)@[323e58fbd7...](https://github.com/VoltageOS-staging/frameworks_base/commit/323e58fbd7d3b1fb656a965042a03bc43dbb1d7f)
#### Wednesday 2022-12-07 13:04:06 by Joey Huab

core: Refactor Pixel features

* Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

* Default Pixel 5 spoof for Photos and only switch
  to Pixel XL when spoof is toggled.

* We will try to bypass 2021 features and Raven
  props for non-Pixel 2021 devices as apps usage
  requires TPU.

* Remove P21 experience system feature check

Signed-off-by: Dmitrii <bankersenator@gmail.com>

---
## [ConchuOD/linux](https://github.com/ConchuOD/linux)@[6403dfa78c...](https://github.com/ConchuOD/linux/commit/6403dfa78c2de84d0989460869f901d986695160)
#### Wednesday 2022-12-07 13:11:41 by Conor Dooley

fpga: add PolarFire SoC IAP support

Add support for "IAP" reprogramming of the FPGA fabric on PolarFire SoC.

Signed-off-by: Conor Dooley <conor.dooley@microchip.com>
---

Hey all,
RFC yadda yadda, but not asking people to look at the code per se -
really what I am sending this RFC to achieve is a bit of feedback on
what the re-programming "flow" looks like.

PolarFire and the SoC variants are flash FPGAs. All well and good for
PolarFire, but for PolarFire SoC in IAP mode it is re-programmed from
the on-board SoC. The spi-slave stuff that Ivan upstreamed recently
works too, but that's only when you have an external programmer.

IAP, or In Application Programming, a programming running on the cpu
cores writes the FPGA bitstream, or I suppose "firmware" in Linux land,
out to a flash chip which the system then will use to reprogram the
FPGA. When IAP is initiated, the system controller will take the FPGA
down completely & do the reprogramming. This means, once Linux (or some
other program) kicks off the re-programming (in write_complete() below)
the system will *immediately* power cycle, whether the reprogramming
passes or not. You can see in my write_complete() implementation, that I
do not expect the function to return, unless we catch an error case early.

From my cursory looking around, there doesnt appear to me to be all that
much info in-tree about what each FPGA does when you reprogram it, but
it doesn't appear that for other FPGAs the CPUs get shut down during
this kind of self-reprogramming?

The alternative approach would be to use the "auto update" mode, which
just installs an image that will not be used until the FPGA is rebooted
in the regular way. Then, on reboot, the system controller would pluck
the image from its flash chip and program the FPGA with it. From the
last time I looked at the documentation (and the implementations) it
seemed that people had custom (and out of tree) ways to initiate/handle
the programming, so perhaps I have the freedom to do the "auto update"
approach, even if it may be a little different to other implementations?

If I've missed something, please let me know. I hope I have!

I've only recently got a board capable of testing this & have not yet
tested my code here in anger etc, it's just the high level thoughts
about how to approach the re-programming in an FPGA manager friendly way
that I'm looking for comments on.

@LKP folks, if you happen to see this - you can disable building this
patch, it won't without some dependencies ;)

Thanks,
Conor.

---
## [MuseSystems/musebms](https://github.com/MuseSystems/musebms)@[067ce465d2...](https://github.com/MuseSystems/musebms/commit/067ce465d2f702c527f870ef6e5257242a68bdf9)
#### Wednesday 2022-12-07 13:19:57 by Steven C. Buttgereit

Refactor MssubMcp API & Runtime Assumptions

Much to unpack in this commit.

The first thing to address is we preliminarily settle a debate about
where the primary runtime boundaries lie in regard to what is just a
collection of supervisors and services and where we should be defining
OTP Applications.  In this case the subsystem level becomes the level of
the OTP Application.  This means we make firmly establish what processes
exist, how they're identified or accessed, how they are started and
updated, and how everything is bootstrapped.  The original think was to
leave many of these decisions to the top level application for the
maximum flexibility, but in retrospect that's not really necessary and
adds additional complexity.  By the time we have a subsystem defined we
can have stronger opinions about what the runtime properties should be
that the subsystem supports, leaving the top level application to really
be a consumer of the services provided as is.  My feeling right now is
that this will leave the supervisory trees and service access in the
correct state that we'll want to see in the overall running application
into which the subsystem has been incorporated.  I feel reasonably
confident that this is a correct level of abstraction, though working
problems of a more distributed architecture and runtime environment
could still change my mind on this.

The second item addressed is that MssubMcp now wraps the APIs of its
components and offers its own Public API for those component functions.
This I am much less confident about; indeed my gut feeling is that this
is ultimately going to be proved an incorrect approach, but there are
some positive arguments that do support the approach that are currently
driving the decision.  It was looking like there could be a fair amount
of ceremony in executing component processes in the MCP Subsystem
runtime service context (correct database, correct enums service,
correct settings service).  By wrapping the component APIs in calls
which ensure the correct service context is set and then returned to the
prior state, we can remove that burden from the calling code.  We also
relieve the development process of the top level application from the
cognitive load of understanding all of the underlying components and
their individual APIs. And then I would also expect that the subsystem
API could remain more stable over time where component APIs may need to
be more volatile.  On the downside we have increased indirection between
the top level caller and the code actually doing the work; we have code
that only serves as wrapper code to maintain or add when a component
does change in a way that needs to be surfaced at the subsystem API
level; probably small performance impacts to manage the indirection;
leaks in the abstraction, such as not eliding the component types &
typespecs which would cause even more duplication or extra maintenance
to address.  The work is done and I'm going to see if there is some
value in it or not by working the application proper.  At the time the
decision was taken some of the service context support from the
subsystem wasn't there and was only developed to make the wrapped API
easier... but I think those components may make the feared ceremony of
the top level caller dealing with the service context moot and the
component API wrapping unnecessary; this includes the mcp_opfn macro
(terrible name, will probably change), the start_mcp_service_context &
stop_mcp_service_context functions, and the process_operation function.

Anyway this commit makes these changes and also sets up the
documentation required for the wrapped API.  Tests have been updated as
well, though we do not focus on testing the wrapped API beyond the
incidental integration test usages.  This is something to be rectified
should the commitment to the wrapped API become stronger (I'm kinda
hoping I end up ripping it out).

---
## [lukelhi/guava](https://github.com/lukelhi/guava)@[8a676ade61...](https://github.com/lukelhi/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Wednesday 2022-12-07 13:30:38 by cpovirk

Make the build work under more JDK versions.

(Guava is already _usable_ under plenty of verions. This change affects only people who build it themselves.)

And run CI under JDK17. Maybe this will make CI painfully slow, but we'll see what happens. If we want to drop something, we should consider whether to revert 17 or to drop 11 instead (so as to maintain coverage at the endpoints of \[8, 17\]).

## Notes on some of the versions

### JDK9

I expected Error Prone to work, but I saw `invalid flag: -Xep:NullArgumentForNonNullParameter:OFF`, even though that flag is [already](https://github.com/google/guava/blob/166d8c0d8733d40914fb24f368cb587a92bddfe0/pom.xml#L515) part of [the same `<arg>`](https://github.com/google/error-prone/issues/1086#issuecomment-411544589), which works fine for other JDK versions. So I disabled Error Prone for that version.

Then I had a Javadoc problem with the `--no-module-directories` configuration from cl/413934851 (the fix for https://github.com/google/guava/issues/5457). After reading [JDK-8215582](https://bugs.openjdk.org/browse/JDK-8215582) more carefully, I get the impression that that flag might not have been added until 11: "addressed in JDK 11, along with an option to revert to the old layout in case of need." So I disabled it for 9-10.

Then I ran into a problem similar to https://github.com/bazelbuild/bazel/issues/6173 / [JDK-8184940](https://bugs.openjdk.java.net/browse/JDK-8184940). I'm not sure exactly what tool produced a file with a month of 0, but it happened only when building `guava-tests`. At that point, I gave up, though I left the 2 above workarounds in place.

### JDK10

This fails with some kind of problem finding a Guice dependency inside Maven. I didn't investigate.

### JDK15 and JDK16

These fail with [the `TreeMap` bug](https://bugs.openjdk.org/browse/JDK-8259622) that [our collection testers had detected](https://github.com/google/guava/issues/5801#issue-1068748849) but we never got around to reporting. Thankfully, it got reported and [fixed](https://github.com/openjdk/jdk/commit/2c8e337dff4c84fb435cafac8b571f94e161f074) for JDK17. We could consider suppressing the tests under that version.

### JDK18, JDK19, and JDK20-early-access

These fail with [`SecurityManager` trouble](https://github.com/google/guava/issues/5801#issuecomment-1293817701).

## Notes on the other actual changes

### `maven-javadoc-plugin`

I set up `maven-javadoc-plugin` to use `-source ${java.specification.version}`. Otherwise, it would [take the version from `maven-compiler-plugin`](https://github.com/google/guava/issues/5801#issuecomment-1314291284). That's typically fine: Guava's source code targets Java 8, so `-source 8` "ought" to work. But it doesn't actually work because we also pass Javadoc the _JDK_ sources (so that `{@inheritDoc}` works better), which naturally can target whichever version of the JDK we're building with.

### Error Prone

While Error Prone is mostly usable [on JDK11+](https://errorprone.info/docs/installation), some of its checks have [problems under some versions](https://github.com/google/error-prone/issues/3540), at least when they're reporting warnings.

This stems from its use of part of the Checker Framework, which [doesn't support JDKs in the gap between 11 and 17](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/framework/src/main/java/org/checkerframework/framework/source/SourceChecker.java#L553-L554). And specifically,  it looks like the Checker Framework is [trying to look up `BindingPatternTree` under any JDK12+](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/javacutil/src/main/java/org/checkerframework/javacutil/TreeUtils.java#L131-L144). But `BindingPatternTree` (besides not being present at all [until JDK14](https://github.com/openjdk/jdk/commit/229e0d16313b10932b9ce7506d84096696983699#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R41)) didn't declare that method [until JDK16](https://github.com/openjdk/jdk/commit/18bc95ba51b6864150c28985e65b6f784ea8ee2c#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R39).

Anyway, the problem we saw was [a `NoSuchMethodException` during the `AbstractReferenceEquality` call to `NullnessAnalysis.getNullness`](https://oss-fuzz-build-logs.storage.googleapis.com/log-a9d04aa2-8b5a-47ca-8066-7e6b38548064.txt), which uses Checker Framework dataflow.

To address that, I disabled Error Prone for the versions under which I'd expect the `BindingPatternTree` code to be a problem.

(I also disabled it for JDK10: As noted above, Error Prone [supports JDK11+](https://errorprone.info/docs/installation). And as noted further above, Maven doesn't get far enough with JDK10 to even start running Error Prone.)

Fixes https://github.com/google/guava/issues/5801

RELNOTES=n/a
PiperOrigin-RevId: 488902996

---
## [MMMiracles/tgstation](https://github.com/MMMiracles/tgstation)@[83f475aa7e...](https://github.com/MMMiracles/tgstation/commit/83f475aa7ec4290c6961f1f14c5da80f340989b8)
#### Wednesday 2022-12-07 13:37:16 by tralezab

Adds the DNA Infuser, a genetics machine you feed corpses to infuse their DNA with yours! What could go wrong?! (#71351)

## About The Pull Request  
Adds the "DNA Infuser" to genetics. One person enters, a corpse is added
to the machine, and you can activate the machine to "infuse" the subject
with the DNA. This converts one random organ from a set into the
mob-related organ.

### Rat mutation 🐀

Rats can be fed in to turn you into a rat-creature-thing!
```diff
+See better in the dark
+Can pretty much eat anything! Toxic foods, gross foods, whatever works!
+Smaller, and can climb tables
?Randomly squeaks occasionally?
-Take twice as much damage
-Vulnerable to flashes
-Gets hungry MUCH quicker.
-Yes, eat anything, but only ENJOY dairy.
```
Having every rat organ at once allows you to ventcrawl nude!

### Carp mutation 🐟 

Carp work for a mutation as well!
```diff
+Strong jaws, that drop teeth over time!
+Space immunity! Breathe in space, unbothered by pressure or cold!
+Smaller, and can climb tables
-Can't block your jaws with a mask
-Can't take the heat, overheats easily
-Can only breathe in environments that have minimal or no oxygen
-Nomadic. If you don't enter a new zlevel for awhile, you'll start feeling anxious.
```
Having every carp organ at once allows you to swim through space!

### Fly mutation 🪰 

Any corpses without organs to turn into turn into fly organs! Fly organs
now have a bonus for collecting them all, transforming you into a fly,
when you pass the threshold. But even without those, fly organs are
technically... organs. They most of the time work like normal ones.

## Todo 🐦 

- [x] Finish the infuser code
- [x] Create a little booklet that shows what kind of shit you can turn
into, hopefully i can autogenerate this based off of organ set subtypes
list
- [x] sprite/slap a color on rat mutant organs
- [x] Maybe make a *few* more organ sets

## Why It's Good For The Game 🐑 

Oops, I forgor to fill this out! My hackmd is here.

https://hackmd.io/@bazelart/ByFkhuUIi

## Changelog 🧬 

:cl: Tralezab code, Azlan + Azarak (Az gaaang) for the organs
add: Added the DNA infuser to genetics! Person goes in, corpse goes in,
and they combine!
add: Try not to turn yourself into a fly, OK?
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [cosmeticsshop/perfumes](https://github.com/cosmeticsshop/perfumes)@[dbf8496b07...](https://github.com/cosmeticsshop/perfumes/commit/dbf8496b0788d704ad899b075e38d0e3930c640c)
#### Wednesday 2022-12-07 15:48:00 by cosmeticsshop

Update README.md

Fall In Love with PERFUMES FOR MAN AS GIFT
As the festival season is going on, so why not buy some gifts. If you want to give gifts to your fiancé, husband, friend and so on then the perfume is the best gift option. With this you can make their day full of fragrance.  
Choosing the best perfume is a difficult undertaking. These are not simple designations; the difference is in the product's concentration. Many users find the best for them, but it is difficult for them to navigate and thus choose the proper bottle. So, in order to distinguish them and use them wisely, you must first learn more about their composition and function. So, how can you pick the best perfume among Eau de Toilette, Eau De Toilette Spray, Eau De Parfum, and Perfume?
About concentration:
Concentration is a basic mixture of pure raw materials like that fragrances, oils, natural or synthetic materials and so on, which is diluted to facilitate its evaporation. It’s mostly depending on the type of brand.
Finding a new perfume is not the easiest endeavor. There are almost unlimited options, and it can be difficult to know where to begin. Let us be your wingman as we run through some of the best-selling men's perfumes from cosmetics-beauty shop.
1.	Invictus Victory Eau De Parfum Spray
2.	Bad Boy Eau De Toilette Spray
3.	Man Eau De Toilette Spray
4.	Olympea Legend Eau De Parfum Spray
5.	Rochas Man Eau De Toilette Spray
6.	Steel Essence For Man Eau De Toilette Spray
Any of these greatest perfumes for men’s that last a long time should be purchased. Also, regardless of which one you choose, you can be confident that you will not be disappointed because each of them is unique and superior in their own right.

---
## [Frank-py/Japy](https://github.com/Frank-py/Japy)@[8c2130d0e3...](https://github.com/Frank-py/Japy/commit/8c2130d0e38fff4b632e28950da98782112f652e)
#### Wednesday 2022-12-07 16:23:12 by Daniel

I am actually so fucking pissed bro this is so fucking annoying nothing ever works this is so fucking shit fuck this shit please help

---
## [gopipate/zulip](https://github.com/gopipate/zulip)@[23a776c144...](https://github.com/gopipate/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Wednesday 2022-12-07 16:50:17 by Mateusz Mandera

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
## [apollographql/router](https://github.com/apollographql/router)@[cfb421a564...](https://github.com/apollographql/router/commit/cfb421a5646de4ae5d5634415c86336d70c6fb90)
#### Wednesday 2022-12-07 17:15:33 by Bryn Cooke

Fixes #2123 (#2162)

Issue was introduced with #2116 but no release had this in.

Move operations would insert data in the config due to the delete magic
value always getting added. Now we check before adding such values.

We may need to move to fluvio-jolt longer term.

<!--
First, 🌠 thank you 🌠 for considering a contribution to Apollo!

Some of this information is also included in the /CONTRIBUTING.md file
at the
root of this repository.  We suggest you read it!

  https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md

Here are some important details to keep in mind:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will
take more than an hour, please make sure it has been discussed in an
        issue first. This is especially true for feature requests!

* 💡 Features
Feature requests can be created and discussed within a GitHub Issue.
Be sure to search for existing feature requests (and related issues!)
prior to opening a new request. If an existing issue covers the need,
please upvote that issue by using the 👍 emote, rather than opening a
        new issue.

* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.

* 📖 Contribution guidelines
Follow https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
associated issues! Documentation in the docs/ directory should be
updated
        as necessary.  Finally, a /CHANGELOG.md entry should be added.

We hope you will find this to be a positive experience! Contribution can
be
intimidating and we hope to alleviate that pain as much as possible.
Without
following these guidelines, you may be missing context that can help you
succeed
with your contribution, which is why we encourage discussion first.
Ultimately,
there is no guarantee that we will be able to merge your pull-request,
but by
following these guidelines we can try to avoid disappointment.

-->

Co-authored-by: bryn <bryn@apollographql.com>

---
## [jemand771/advent-of-code](https://github.com/jemand771/advent-of-code)@[df685d0751...](https://github.com/jemand771/advent-of-code/commit/df685d0751a459b9635ac20ff33063cfe3b6b306)
#### Wednesday 2022-12-07 18:02:32 by Willy

day 7

this is so fucking stupid but I'm sick and can't think straight, might aswell embrace the stupidity

---
## [JulietteDestang/GitWorkshop](https://github.com/JulietteDestang/GitWorkshop)@[07236404b1...](https://github.com/JulietteDestang/GitWorkshop/commit/07236404b1e45934aaf52ea53bb7993c8b3a7e1b)
#### Wednesday 2022-12-07 18:18:32 by Timothée de Boynes

[ADD] The feature

yes fuck you i don't want to creuse my mind to make a good comit

---
## [imLinguin/HeroicGamesLauncher](https://github.com/imLinguin/HeroicGamesLauncher)@[3f6541c8a7...](https://github.com/imLinguin/HeroicGamesLauncher/commit/3f6541c8a700511cea9f0c9b572a5d2138ee76e3)
#### Wednesday 2022-12-07 18:37:55 by Mathis Dröge

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
## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[ce39f048bf...](https://github.com/sleepynecrons/cmss13/commit/ce39f048bf5eb25e2a93d7355327ccacc0504b01)
#### Wednesday 2022-12-07 19:50:54 by carlarctg

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
## [hivbot/voiceflow-runtime](https://github.com/hivbot/voiceflow-runtime)@[130ccda3fe...](https://github.com/hivbot/voiceflow-runtime/commit/130ccda3fe90b2a9925b9ca757e96824d8948e33)
#### Wednesday 2022-12-07 19:54:11 by Tyler Han

feat: nlc entity filling (PL-000) (#449)

<!-- You can erase any parts of this template not applicable to your Pull Request. -->

**Fixes or implements PL-000**

### Brief description. What is this change?
this fix requires a long description, but the code is pretty hard to navigate as well so I'll do my best to explain.
I've noticed terrible performance for the capture step/entity filling feature if the model is untrained. We should have a decent fallback measure if the NLP isn't working.

[NLC](https://github.com/voiceflow/natural-language-commander) is a library we use to handle regex matching against intent utterances and extracting entities when the NLP is untrained. It will only match if the user types everything correctly letter for letter.

In the current implementation of entity filling (called dialog management in the code atm, a bit confusing I know, just assume dialog management = entity filling), if we know the user is trying to fill a SPECIFIC entity of an intent, we first make a match of [their intent against the general model](https://github.com/voiceflow/general-runtime/blob/8e22616890c8c4d011ea12845ae463df788d34e4/lib/services/nlu/index.ts#L85-L115). 

Then we also check it against a `dmPrefix`'ed intent utterances:
![Screen Shot 2022-12-05 at 3 56 39 PM](https://user-images.githubusercontent.com/5643574/205741203-edfacfad-90ab-4161-a4ed-c00e941a8fce.png)
![Screen Shot 2022-12-05 at 4 03 47 PM](https://user-images.githubusercontent.com/5643574/205742304-013944b3-8577-4dd0-8258-a34928eaf666.png)

These are special utterances tied to the intent, the prefix is just a hash of the intent name. When we know the user is trying to fill for a specific intent, we call the NLP and prepend the prefix to their raw text query:
https://github.com/voiceflow/general-runtime/blob/8e22616890c8c4d011ea12845ae463df788d34e4/lib/services/dialog/index.ts#L125-L128

So if they said "quote for life insurance" as `query` we would first run it against the NLP normally and then against "1f79373e6d quote for life insurance" as `query`. The LUIS model already has these utterances with prefixes baked in, the NLC does not. 

Also our [predict](https://github.com/voiceflow/general-runtime/blob/8e22616890c8c4d011ea12845ae463df788d34e4/lib/services/nlu/index.ts#L24) code comes in 3 stages:
1. try against the NLC regex but hard matching for slots. If the utterance is something like "quote for {insuranceType}" only valid forms of the slot are okay. They can't say "quote for toilet paper" and expect NLC to match
2. call the actual `luis-authoring-service` endpoint and check against the actual NLP
3. if the user never trained their model, try against NLC regex but open matching flow slots, If the utterance is something like "quote for {insuranceType}" then  "quote for toilet paper" will match the intent and insuranceType = "toilet paper"

What this PR does is if we KNOW that we're looking for the entity of a specific intent, we pass that through when generating the NLC model, and inject that intent's slots' (`intent.slots[].dialog.utterances`) utterances, with prefixes, into the actual utterances of the intent.

[we have this `handleDialog` function for NLC]( "quote for toilet paper"), but looked through the source code, it never worked. It relies on `slot.dialog.utterances` which was never getting passed in:
https://github.com/voiceflow/general-runtime/blob/15a8cfbad416a14af7c194bc59b1516325b50ea3/lib/services/nlu/nlc.ts#L155-L162
`filledEntities` never contains the `dialog.utterances` required, so this would be `NoneIntent` all the time anyways.

TLDR, if we are looking for a specific intent's slots' utterances, just add them to the regex model with a prefix. 

In action:
![Screen Shot 2022-12-05 at 3 47 43 PM](https://user-images.githubusercontent.com/5643574/205746744-b4315ef2-1d2e-4e44-967f-b22be2fbf2c8.png)

Co-authored-by: Tyler Han <tylerhan97@gmail.com>

---
## [ksqsf/emacs-config](https://github.com/ksqsf/emacs-config)@[c3830296f6...](https://github.com/ksqsf/emacs-config/commit/c3830296f676604909e452e6f586c60687afad98)
#### Wednesday 2022-12-07 20:11:17 by ksqsf

[git] Quick clone.

When making random contributions to GitHub repositories, editing on
GitHub is convenient, but it suffers from severe usability issues:

1. You cannot edit multiple files at once.  This is the most annoying
issue.

2. You cannot update your pull request later using the Web interface.

3. You cannot change the name of the patch branch.  (By default, it's
called 'patch-N', which is not the most descriptive name.)

4. You cannot benefit from Git hooks.

This list goes on and on.

Therefore, it's often desired to have a local clone of the repository.
And some projects even forbid the use of the Web interface!

My current workflow using Magit + Forge:

1. magit-clone: Customize magit-clone-default-directory to make this
easier.

2. N c f: fork this repo to my personal account.

3. (Optional) Create a branch for this patch with my own choice of the
branch name.

4. Make changes.

5. Commit changes.

6. Push to a new branch in my personal repo.

7. N c p: Make a pull request.

Compared to GitHub's Web interface, this streamlined workflow is fast,
rock-solid, and full-featured!  You also have access to other (Ma)Git
goodies, such as you can create patches easily using 'W c c'.

Initially, I wanted to use Org-protocol to quickly initiate Git clone
from the Web page.  However, it seems copy & paste is not that bad.

---
## [SakuraKat/Discord-GPT-J-bot](https://github.com/SakuraKat/Discord-GPT-J-bot)@[fd061d23c6...](https://github.com/SakuraKat/Discord-GPT-J-bot/commit/fd061d23c6bdd1271c06918485f45432cc951971)
#### Wednesday 2022-12-07 20:13:44 by SakuraKat

submodules updated, i still dont know why it asks me to do it, so in future itll be called "submodules fuck you" or in short sfu

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[bce6fc7842...](https://github.com/re621/dnpcache/commit/bce6fc7842fbef8e95e845c3f267b7e2b9be607f)
#### Wednesday 2022-12-07 21:27:05 by bitWolfy

Add 989 artists to the DNP list.

Added: malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, peshky, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, malachimoet, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, infinitedelusion, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, 100101, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, devildjmachine, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, jdlaclede, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, trunchbull, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, whippytail, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[661eaa985e...](https://github.com/lessthnthree/tgstation/commit/661eaa985e32056cc25f32bd81d9106861a4f9f8)
#### Wednesday 2022-12-07 21:31:55 by MrMelbert

Important heretic spell rebalancing (#71620)

## About The Pull Request

Nerfs
- Furious steel cooldown: 30s -> 60 seconds (when ascended: 10s -> 30s)
- Furious steel: Now affected by antimagic
- Cleave cooldown: 40s -> 45s
- Cleave range: 9 tiles -> 4 tiles
- Cleave wound: Now has natural clotting, changing the amount of blood
loss from inf -> ~40%
- Blood siphon range: 9 tiles -> 6 tiles
- Void Pull: Now affected by antimagic
- Void Phase: Now affected by antimagic

Buffs
- Void Blast cooldown: 60s -> 30s

Other
- Rust Formation now has a "distinct" icon
- Void Blast now has a "distinct" icon

## Why It's Good For The Game

A lot of these spells were extremely oppressive, and made it pretty much
a joke to get away with anything.
They were no-brainer choices, and as a result no one really pathed into
anything else but these.

- Furious Steel: 
- Now that blade heretics have "realignment" in their repertoire, which
offers them another counter for being hit by disablers or batons, this
spell doesn't need to have such an insanely high uptime. The spell
should be used for initiating and obtaining the lead in a combat,
instead of having nigh-invulnerability for most periods.
- Additionally, antimagic protection was kind of missing, which was
partially an oversight of it not being a `/magic` projectile.
 
- Cleave:
- Cleave was by far the most absurd ability available bar none. This
spell was guaranteed death in 30 seconds if the target had no way to
stop the bloodflow immediately. AND it could be casted from across the
screen. This brings cleave's range into midrange between you and the
target, giving a lot more opportunity to be aware for the victim.
- Critical bleed wounds had a negative clotting rate, meaning that prior
you would bleed to 0% from cleave if you didn't stop it. Not very fun,
so with the default clotting rate it now stops at 60% blood flow -
enough to be lethal if untreated, but doesn't completely tap you out
   - **Alternatives**: 
      - Keep the no clotting, make it a pure melee / touch spell. 
      - Reduce the cooldown, make it a projectile
- Change it to be like a cool scythe attack that comes out of the caster
and does a sweep

- Blood Siphon: 
- This was primarily done to slot in better with Cleave's range
decrease, encouraging more close range combat between the two. Getting
point clicked from across the screen isn't fun.

- Void Pull and Phase:
- Largely done for consistency. These are spells which cause damage, so
anti-magic should stop the damage from the spells.

- Void Blast
- I have no idea why I made the cooldown so high on this, 1 minute made
it almost worthless.

TLDR: Instakill click spells from across the screen bad, invulnerability
bad

## Changelog

:cl: Melbert
balance: Heretic: Furious Steel's cooldown has been doubled (30s ->
60s), and abides by antimagic
balance: Heretic: Cleave's cooldown has increased by 5s, range has been
decreased to 4 tiles, and wound applied now has natural clotting
balance: Heretic: Blood Siphon's range has been decreased to 6 tiles
balance: Heretic: Void Pull and Phase abide by antimagic
balance: Heretic: Halved Void Blast's cooldown to 30s
qol: Heretic: Void Blast and Rust Formation now have distinct icons 
/:cl:

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[00d3780c38...](https://github.com/Huffie56/cmss13/commit/00d3780c382c704f24e5c6f24aa36d88d509b7ea)
#### Wednesday 2022-12-07 22:05:42 by carlarctg

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
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[fcdf5d850c...](https://github.com/lessthnthree/Skyrat-tg/commit/fcdf5d850c47ac8c9c17045bb5a021d8283d3c0c)
#### Wednesday 2022-12-07 22:54:41 by SkyratBot

[MIRROR] Psykers [MDB IGNORE] (#17825)

* Psykers (#71566)

## About The Pull Request
Finishes #66471
At burden level nine (or through a deadly genetic breakdown), you now
turn into a psyker.
This splits your skull in half and transforms it into a weird fleshy
mass. You become blind, but your skull is perfectly suited for sending
out psychic waves. You get potent psy abilities.
First one is brainwave echolocation, inspired by Gehennites (but not as
laggy).
Secondly, you get the ability of Psychic Walls, which act similarly to
wizard ones, but last shorter, and cause projectiles to ricochet off
them.
Thirdly, you get a projectile boost ability, this temporarily lets you
fire guns twice as fast and gives them homing to the target you clicked.
Lastly, you get the ability of psychic projection. This terrifies the
victim, fucking their screen up and causing them to rapidfire any gun
they have in their general direction (they'll probably miss you)
With most of the abilities being based around guns, a burden level nine
chaplain now gets a new rite, Transmogrify. This lets them turn their
null rod into a 5-shot 18 damage .77 revolver. The revolver possesses a
weaker version of antimagic (protects against mind and unholy spells,
but not wizard/cult ones). It is reloaded by a prayer action (can also
only be performed by a max burdened person).
General Video: https://streamable.com/w3kkrk
Psychic Projection Video: https://streamable.com/4ibu7o

![image](https://user-images.githubusercontent.com/23585223/204150279-a6cf8e2f-c678-476e-b72c-6088cd8b684b.png)

## Why It's Good For The Game
Rewards the burdened chaplain with some pretty cool stuff for going
through hell like losing half his limbs, cause the current psychics dont
cut it as much as probably necessary, adds echolocation which can be
used for neat stuff in the future (bat organs for DNA infuser for
example).

## Changelog
:cl: Fikou, sprites from Halcyon, some old code from Basilman and
Armhulen.
refactor: Honorbound and Burdened mutations are brain traumas now.
add: Psykers. Become a psyker through the path of the burdened, or a
genetic breakdown.
add: Echolocation Component.
/:cl:

Co-authored-by: tralezab <spamqetuo2@ gmail.com>
Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

* Psykers

* commented out stuff is now in

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: tralezab <spamqetuo2@ gmail.com>
Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [HSavinien/cub3d](https://github.com/HSavinien/cub3d)@[5d7f9d033b...](https://github.com/HSavinien/cub3d/commit/5d7f9d033b8921023aae5a640cc885e4fe484372)
#### Wednesday 2022-12-07 23:30:52 by Theo Mongellaz

after three days of work and suffering, behold, here is the exact same thing chloe already did, but with uglier colors. fuck my life...

---

