## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-29](docs/good-messages/2022/2022-04-29.md)


1,571,077 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,571,077 were push events containing 2,593,144 commit messages that amount to 191,270,893 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[a137c15a79...](https://github.com/BlueMemesauce/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Friday 2022-04-29 00:53:11 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [david-fong/okiidoku](https://github.com/david-fong/okiidoku)@[683c42b7ec...](https://github.com/david-fong/okiidoku/commit/683c42b7ec28f9508b7d59bb5e97d7f2d2f82da2)
#### Friday 2022-04-29 02:41:58 by david-fong

add examples and try to get complete template argument deduction

Ran into problems related to variant-of-span mapping back to layout of
variant-of-array and how to change the order of the backed variant-of-array
only given the variant-of-span.

Thought hard about why I made GridSpan and GridArr in the first place
and tried to come to a comclusion on whether that separation is actually
valuable. You can find that in the TODO.md file. The conclusion: I
currently cannot think of a good reason for that separation. I think I
should get rid of it and make my life easier.

I learned some CTAD stuff and attempted to read the standardese on
template deduction for functions and classes. Bit of a shame that it
seems to now be going to waste. Maybe it will be useful later though.

---
## [dec-a-dance/blps](https://github.com/dec-a-dance/blps)@[5adb9b8cb0...](https://github.com/dec-a-dance/blps/commit/5adb9b8cb00998fe9a22c98044f13329fd4407c3)
#### Friday 2022-04-29 02:46:17 by dec-a-dance

THIS SHIT FINALLY WORKS
but i really hate my life
actually: wildfly deploy + xml data storaging.

---
## [rdxzv/msm-4.14](https://github.com/rdxzv/msm-4.14)@[37004ffb3b...](https://github.com/rdxzv/msm-4.14/commit/37004ffb3bbd52adc28dc6fd73a7810000c053e6)
#### Friday 2022-04-29 03:16:59 by Yaroslav Furman

power: supply: force disable frame pointers and optimize for size

Holy fucking shit this is so retarded, it doesn't boot with frame pointers.

Signed-off-by: Yaroslav Furman <yaro330@gmail.com>

This is possibly breaking the DS28E16 verification driver
Signed-off-by: Forenche <prahul2003@gmail.com>
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [GesuBackups/goonstation](https://github.com/GesuBackups/goonstation)@[bdad398f9e...](https://github.com/GesuBackups/goonstation/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Friday 2022-04-29 04:07:00 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[855e1360c0...](https://github.com/PKRoma/Terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Friday 2022-04-29 06:50:00 by Mike Griese

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
## [coloradocolby/blues-stack](https://github.com/coloradocolby/blues-stack)@[1a2fc417f3...](https://github.com/coloradocolby/blues-stack/commit/1a2fc417f3f527cb4d2513a90efa4367fce16399)
#### Friday 2022-04-29 07:10:49 by colby thomas

update setup-test-env.ts to fix jest errors

I cloned the blues stack tonight and was writing some tests, only to find that when I tried to access the match `toBeInTheDocument` it didn't exist. Updating this line as so made everything work as you'd expect.

Which is kinda odd to me, honestly, because importing the `extend-expect` file should do is run the following code
```
// eslint-disable-next-line
require('./dist/extend-expect')
```

whereas not specifying the file, and using the `main` property in the package.json which points to `dist/index.js` just calls this code 

```
"use strict";

require("./extend-expect");
```

However the latter makes the ts compiler happy

---
## [Offroaders123/Flatlands](https://github.com/Offroaders123/Flatlands)@[2573f31c93...](https://github.com/Offroaders123/Flatlands/commit/2573f31c93a15962b388fd85b9fb343907072a6c)
#### Friday 2022-04-29 07:43:24 by Offroaders123

Item Animation Rendering! + New Debug Entries

Additions:
- Added item animation rendering for the player! Now the Fire item will render it's keyframes in-line with how it appears in the hotbar already. They are currently not in-sync, since one is handled with CSS, and the other is with the game canvas, but I will address that later, possibly by syncing up the hotbar keyframes with the game loop's tick count. Related to this, the keyframe duration for the hotbar render of the item now uses the item's animation duration property, rather than being a magic number of 750ms, which is what the Fire item happened to be. There is still a magic number sort of thing in use for the CSS animation for the item rendering, and I will be addressing that later by using Web Animations to render the keyframes, rather than a direct @keyframes entry in the page's styles itself. This will eventually allow the keyframes to be driven by the item property itself also, just like the other ones that describe the item.
- Added a toggle for item textures which will determine whether you want the texture to be flipped to have a custom render when the player holds it. Originally, all items used this method, but some don't need this effect, and it looks better to render them without it. The reason for having that method before was to make sure the Hatchet is rendered in the correct direction, with the sharp end facing away from the player. It wouldn't make sense for him to hold it towards him, haha. But for the Fire or Pizza items, they render better in their default rotation and inversion. Now they only rotate horizontally when the player faces left. I plan to further expand a better implementation for this later on also, maybe to deal with shadows or things like that. I mention that, because the Hatchet is facing the correct way, but the shadow is on the top of the item handle, rather than on the bottom, like it appears in the hotbar. This is the same for the other tools. I was going to make only the Hatches use the special rendering, but then it would be the only one with the shadow on the top, and I didn't like that. For now, the tools are consistently incorrect XD
- Added a Tick Time entry to the Debug menu! This shows the equivalent time the game is at, compared to the existing Game Time entry, which shows the time of the document itself (the one that should be spot on). I want to further debug if my game loop code is solid enough to keep the two numbers in sync as they should be the same with the logic that catches the game up to any time missed since the last loop.
- Similar to the Tick Time, a new Milliseconds entry has been added! This and the previous new entry helped me debug the calculations for adding the animated item rendering to the canvas, as I designed the duration for item animations to be listed in milliseconds. I had to make sure that my ticks to milliseconds conversion was correct.

Changes:
- Tidied up some of the player rendering logic. Some of the old checks were still around from before the new Definitions Loader update that prevented properties from being accessed before they had loaded in.
- Fire is now the default selected slot for the player! Thought I'd show off the new in-game animation, as I think it looks fantastic! :D

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[529bd674a8...](https://github.com/treckstar/yolo-octo-hipster/commit/529bd674a812c05782dadc8f88322a172d2c2fbf)
#### Friday 2022-04-29 08:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [PixelExperience-Devices/kernel_oneplus_sm8150](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150)@[044c3164db...](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150/commit/044c3164db8a50542569e6f15c23b1a5e09357b4)
#### Friday 2022-04-29 08:34:06 by alk3pInjection

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
## [kevinkimdevera/rathena](https://github.com/kevinkimdevera/rathena)@[d617d9f083...](https://github.com/kevinkimdevera/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Friday 2022-04-29 10:50:45 by Aleos

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
## [Den-Xero/Journeyman_Game](https://github.com/Den-Xero/Journeyman_Game)@[796d38e2c7...](https://github.com/Den-Xero/Journeyman_Game/commit/796d38e2c7e86b63a1e168ad32b7ae0f591cb43e)
#### Friday 2022-04-29 14:35:58 by McConnell2111

Added Custom Keybinds again this time on my own branch

i have time to rant today so what shall we talk about? ooo F1 that was good today, boring ass redbull 1,2 but the madlad lando p3 which was pog. le clair got fked on the same corner he came off in quali which was dumb af. ooo also the LCS finals was today a quick 3-0 for EG which is eh but they did do the same thing as G2 which is intresting since they are in the same bracket as eachother for MSI so thats spicy but G2's real enemy is T1 with Faker the beast. erm what else.... pfft i dunno got any good series to watch? still waiting on moon knight new ep and halo but its weekly which is lame. yeah thats about it from me this time. cya next time.

---
## [huhridge/spicetify-cli](https://github.com/huhridge/spicetify-cli)@[0a89573c1c...](https://github.com/huhridge/spicetify-cli/commit/0a89573c1ce2f4ed3f4cdaac7651bc34dffb3a0a)
#### Friday 2022-04-29 15:23:37 by Łukasz Ordon

fix: `New Releases` custom app for Spotify 1.1.81+ (#1563)

* Fix `New Releases` custom app for Spotify 1.1.81+

- Based on proposed fix for `Shuffle+` (#1559)
- Fixes #1539 #1530 

Notes:
- Can probably be written nicer - this is my scuffed attempt to fix it
- May or may not actually show all new releases for all followed artists - have over 665 of them but I don't think I'm getting all of them (see below)
- May or may not return `error 500` (added `.catch()` block keeps it from breaking whole custom app)

* Minimize `internal server error: 500`...

...for big libraries of followed artists.

Changes:
- Change `URL` to query only discographies
- Limit amount of queried albums to 5

Notes:
- This does **NOT** fixes erroring fully - it only maxes out amount of data you can query before getting rate limited
- The more options you select (ex. albums + EPs + podcasts), the less data you may receive
- To max number of albums received, I recommend to select only `Albums` (since `Singles and EPs` will probably get displayed anyway...)

* Add notifications when error occurred

Notifications added:
- Error code (`500`, `429` etc.)
- Amount of followed artists to fetch releases from
- Amount of followed artists failed to fetch releases from

I guess we have to get along with getting `500-ed` - one time it fetches everything instantly, second time it drops 60 artists...

* "Prettify" file to pass `Prettier` test

* Fix filtering, counter...

- Fixing filtering as no matter was what set in config, it always displayed everything as "Album"
- Fixing "Missing releases from..." counter - should properly reset now

What broke again:
- "Appears on" releases cannot be retrieved with that API endpoint - this filter is just there and doesn't do anything - this prevents from showing everything as "Appears on" etc.

Notes:
- There seem to be an API endpoint for retrieving "Related content" stuff - problem is that would query everything TWICE... which breaks everything even more (and we don't wanna do that)
- If someone knows how to query everything using separate endpoint without doing it 4 times, let me know...

* Forgor `( )`... Oops... :skull:

I forgor 💀

* Include requested changes

Changes:
- Properly encode URI including variables
- Make `limit` variable customizable via settings (set default to 5)
- Make error messages as "dev console only"

Notes:
- Errors displayed in console may be a little spammy - if we get error early, there may be lots of lines displaying it + counter...
   * I'm not too sure how to tackle this - just remove them altogether? Or is there a function that could "suppress" them?
   * Switching from normal `log` to `debug` may help a little as they will be only visible if user has set their console log level to include `Verbose`
- Making `limit` customizable may lead to even more errors but fuck it I guess - it's better to have a choice than not, right?
   * It can be manually input via custom app settings (same place where other options are) - there is no list etc. - it's just normal input field
- Set `offset` value as const `0` and not making it customizable (cause why would you want to start searching from ex. 3rd album instead of beginning, right?)
- Leaving `Fetching releases from...` notification cause it looks cool - it's fun to know how many followed artists you have 😆

---
## [Rombuilding-X00TD/asus_sdm660](https://github.com/Rombuilding-X00TD/asus_sdm660)@[235f6ced28...](https://github.com/Rombuilding-X00TD/asus_sdm660/commit/235f6ced28118f8a0e713909b27455113c48e8b6)
#### Friday 2022-04-29 15:52:04 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db

---
## [landonf/freebsd-ports](https://github.com/landonf/freebsd-ports)@[e250aeb4a1...](https://github.com/landonf/freebsd-ports/commit/e250aeb4a1399664907d0df0605a3577ba671609)
#### Friday 2022-04-29 16:54:05 by Tobias C. Berner

KDE: Update KDE Gear to 22.04

Thursday, 21 April 2022

Welcome to KDE Gear ⚙️ 22.04!

Skip to What’s New

KDE Gear ⚙️ 22.04 brings you all the updates added to a long list of KDE
apps over the last four months. KDE programs allow you to work, create
and play without having to submit yourself to extortionate licenses and
intrusive advertising, or surrender your privacy to unscrupulous
corporations.

Below you will discover a selection of the changes added in the last
four months to software designed to make your life better. But remember,
there is much, much more: games, social media apps, utilities for
communicating, developing and creating stuff… All these things have been
worked on to give you more stability and boost your productivity.

If you want to see a full list of everything we have done, check out the
complete changelog.

WARNING: There’s a lot!

All the details can be found here:
	https://kde.org/announcements/gear/22.04.0/

---
## [Underdisc/underdisc.github.io](https://github.com/Underdisc/underdisc.github.io)@[b42fe4f64f...](https://github.com/Underdisc/underdisc.github.io/commit/b42fe4f64fd21916473a4024cccba84b65f3267c)
#### Friday 2022-04-29 17:16:42 by Underdisc

A fat update.

I shortened the text on the home page because the old text feels cringy now.

The way the main layout works has changed significantly. I can't really justify these changes other than the fact that it makes more sense to me. I don't even fully remember what my problem was with the original style sheet besides being confused by it. I'm not that great with css, so forgive my ignorance.

The stupid accent bars are gone. It looks better.

The date tags have been removed from the blog index markdown. They weren't needed anymore.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6c89fcb099...](https://github.com/mrakgr/The-Spiral-Language/commit/6c89fcb0992c1a0c7ecd94506340e9f8ec5b2834)
#### Friday 2022-04-29 18:41:12 by Marko Grdinić

"9:10am. I got up a while ago and have been chilling. It is time to start. Let me set the last part of the course to download. Speaking of courses.

https://youtu.be/rkiNs3AQg_o
Principles of Sculpting | Complete Guide to Zbrush 2022

This came out 2 days ago. The vid is 1.5 hours long and it is a part of a bigger Zbrush course.

9:15am. Focus me, I've been checking my email and the only noteworthy thing is recruiter spam by Turing. I actually don't get those very often. I think I applied to one of those remote work companies and got shot down last year. It might have even been Turing. It is a lackluster opportunity. With my skills I really should be ignoring recruiters down left and right, instead of getting them over couple of months.

So I do not get stressed by bait like from last time, it is AI chips or nothing. People doing ML with today's shit tier algorithms are everywhere. Such jobs are not interesting and will not get me closer to the Singularity. Deep learning and GPUs were interesting for a while, but now I sleep on them.

9:20am. Now focus, let me set the last part to download.

https://youtu.be/wDMdDvxf5fo?t=1312
Hardsurface sculpting in Zbrush: 12 techniques you need to know!

I'll resume from here.

9:25am. Good, I did not mess up the capcha. It will be done in a few hours. Let me just chill a bit first.

9:55am. I had insight that using the project option for Dynamesh might lead to edge preservation, and I see that I was completely right. It seems the algo will add more details on the edges when it is turned on. This is great. It makes it so much better than Blender's remesher.

10am. Let me start here. I had a relaxing morning, but I want to ramp up the pace.

10:05am. Done with the video from yesterday.

https://youtu.be/edu9bHhJF6A
ZBrush Hard Surface - Tips & Tricks VOL. 2

https://www.youtube.com/watch?v=X2xkhQ0e4mE
Creating Clean Topology using Booleans, ZRemesher and ZModeler - ZBrush Top Tips - Stephen Anderson

Let me watch the later one first.

https://youtu.be/X2xkhQ0e4mE?t=301

It seems Zbrush can mask borders. This is something to keep in mind.

https://youtu.be/X2xkhQ0e4mE?t=341

Is he just clicking on the edges with the select lasso?

10:15am. Yes, I've tried it out. It seems that clicking on edges with the select lasso hides the entire loop.

https://youtu.be/X2xkhQ0e4mE?t=544

Local symmetry does not work like I thought it would. It seems it can work based on the target, in this case a single island.

10:25am. https://www.youtube.com/watch?v=edu9bHhJF6A
ZBrush Hard Surface - Tips & Tricks VOL. 2

Let me move on to this.

10:50am. https://youtu.be/edu9bHhJF6A?t=930

This way of adding holes is pretty fascinating.

11am. The course finished download. Let me deal with the current vid first. I a third into it.

https://youtu.be/edu9bHhJF6A?t=1138

It just occured to me that bending like this could be useful for bending limbs in case the right is not there.

https://youtu.be/edu9bHhJF6A?t=1201

It would have been faster to just use knife to begin with.

12pm. Finally done with those basic vids. I feel like I overdid it. I should have started work on the monitor yesterday, but nevermind that.

Finally, it is time for the radio course. After I get the tutorial urges out of my system, I'll be able to move on from this.

12:10pm. Let me start it. I'll want to finish it today and dedicate tomorrow to doing the monthly review.

12:35pm. I can't link to the video, but let me post some quotes.

> Chamfers are a little harder in this, I haven't found a definitive way to do chamfers.

Chamfers being what Moi calls fillets and Blender calls bevels.

2:10pm. Done with breakfast, don't have chores today. How about I deal with the course and call it a day early today for once? I don't have to max out my stress meter every single day. I'll aim to finish it a bit earlier and then prepare my mind for getting back into the game myself. Maybe I could even start the review today.

2:15pm. Let me get on with it.

2:20pm. Wow, I have 3.5 hours left. This won't be that easy to clear. Just about the entire day should be enough.

2:25pm. > I use a mouse, don't need a table. Don't listen to the tablet people they are lying to you.

2:45pm. Right now he just took a soft edge and made it hard. How would I do something like that in Moi?

https://youtu.be/5QCyXglgBzs
Removing Fillets in MoI3D

Let me watch this again.

3pm. https://youtu.be/5QCyXglgBzs?t=174

I've internalized it.

3:10pm. Watched another Moi vid as well. I got it. Now, let me get back to the Zbrush course.

I wanted to say this - regardless of what style one is using: NURBs, subdiv, box or sculpting, the operations are remarkably similar.

How do I put it? NURBS for example has characteristics of not having topology, but all the operations it does are applicable to polygonal styles as well. In fact, whether it be NURBS or polygons, neither of them has something the other doesn't.

Admittedly, some things are easier depending on the style.

Pros:

NURBs: No topology. Easy booleans.
Subdiv: Good at mixing curved and flat surfaces.
Box: Efficient topology.
Sculpting: Easy deformation. High poly.

Cons:
NURBs: Restricted to simple deformations.
Subdiv: Incompatible with booleans.
Box: Hard to deal with curved surfaces. Low poly.
Sculpting: Imprecise.

Sculpting is particularly good at making gradual changes to get the desired result, which is why it has become so dominant for various tasks.

Zbrush could learn a little from NURBs programs though.

3:20pm. Let me get back to the course.

4pm.

> All that I've done here and here can be extrapolated to the entirety of this model.

If this is his workflow it might have been easier to just do it in Moi.

His workflow is mostly using projections, masks and booleans. When he does use brushes it is just to make a fillet. He certainly does not need a table for this. Tablets are useful for beating organic objects into shape, but this...

Well, it is rather insightful. I can translate his workflow pretty succinctly into Moi.

Could I do it in Blender using the box modeling style?

...Yeah, sure why not.

Really, the it is just the subdiv style that is the odd one here as it restricts the kinds of things I can do.

Let me resume instead of standing here in a dze. I need to finish part 2 and move on. Somehow I thought it would be shorted. I thought it would be 30m, but instead it is 50. I guess I have another 3h waiting for me after this.

4:30pm. Oh lol, I just noticed he has the Activate Windows watermaked in the bottom right corner. I can't believe I missed this.

4:30pm. Done with part 2. Part 3, has 3 hours in total. It is split into 3 sections.

4:45pm. https://youtu.be/dxphTat6tcc
030 ZBrush 2018 Crease And Bevel Deformers

I am wondering if there is a neat way to get a round bevel on an curved edge of an object. Easy with other styles, but I haven't seen it here.

4:45pm. Forget it, let me get back to the course. I do not have to go through it in its entirety. I got the gist of the style. But let me learn a bit more on it. I'll want to free up my mind for tomorrow.

4:50pm.

> Cane Townsend: Large part of becoming proficient at making aestetically appealing choices in your designs come down to how many times you can mess up and correct yourself. It is the process of elimination. We do this with everything we learn. If you can make those decisions faster without the weight of constraints breathind down your neck every time you make a design decision that requires a lot of preplanning then you will naturally improve at an accelerated rate. This was my discovery when I first switched over from Max to 3d Coat. Max was very rigid and 3d Coat was just the opposite. It was fluid and flexible, and I had no idea how much the constraints were governing my decisions until I no longer had them.

> My brain could now solely focus on the design instead of splitting in half trying to manage both the topology and the design at the same time.

5pm. When doing corners it might be better for him to mask out a whole part and then go over it with the opposite operation. That way he could get a clean cut out on the mask. Instead I've seen him struggle to do curves. As an artist, he is not overly dexterous, but I doubt I'd be any better myself.

That is why I've been wanting the Moi style. Instead of using Lazy Mouse, the system for solection where you can tap alt and draw a quick Bezier is really good. I wish I could use regular brushes that way. You can use shift to go straight, but not do the kind of arc the curve brushes can do.

It might be worth asking about this on /3/.

> CT: Sometimes in this timelapse, I'll jump the gun and some forms that are a little bit, smaller than I should be doing at that exact moment. And that is not such a big deal with Zbrush. In other softwares like poly or CAD you have to make sure that you don't chamfer or fillet too early as it can hinder the flexibility of the design in the future. We don't have that inside of Zbrush.

5:05pm. He talks for 5m and says he will just let me watch for another 55.

5:25pm. I am playing with the curve and I just found out something good. When you use a curve with the smooth brush, it will automatically extend when used at polygroup edges. This could be really useful for filleting curved edges.

Also after you draw a regular curve, you can go into stroke options and press the smooth button to smooth it out. With this feature it is not really necessary for it to have those kind of arcs. Still...

http://docs.pixologic.com/reference-guide/stroke/curve/

///

Bend mode allows the editing of individual points on the curve to create a new curve. The number of points that fall under the cursor, and are therefore edited, is controlled by the Curve Edit Radius (below). When the cursor is over an editable curve, hitting the hotkey S and adjusting the Draw Size slider will actually adjust the Curve Edit Radius, making precise adjustment of curves easy.

A Bend can be applied by hovering over any of the points along the curve and then moving your cursor to pull the point and create the desired angle. The amount of bend at the cursor location is defined by the Curve Falloff settings, located at the bottom of the Curve menu. A Curve Falloff which has the point at the top left will produce a rounded curve deformation while a curve falloff which goes to the bottom right of the curve line will produce an angular curve. Bend mode is enabled by default.

If Bend mode is turned off, the curve can be edited as a whole, without changing its shape.

///

Hrmmm, I'll have to try this out later.

https://youtu.be/J1Txk6wt7kw
071 ZBrush 2021.6 - Curve Overview & Refresher, Including New Bend Start and Bend End Functionality!

Let me watch this.

https://youtu.be/7dkRLmLnTTY
How to use LIQUID and ELASTIC CURVES in Zbrush 2018 - 60 Second Tutorial

First this.

6pm. Had to leave for lunch. Let me watch the video above.

6:15pm. https://youtu.be/N8eLiz_kYo4?t=37
072 ZBrush 2021.6 - Curve Alpha Brushes, Repel Strength, Picker Options, and more!!

You can use this to do a sweep.

6:25pm. No, I do not feel like watching all of that, it is 20m. Enough of curves. Let me get back to the course.

6:45pm. I do not feel like watching the entire timelapse start to finish. Let me move to the next part.

7:10pm. Enough of part 2. Let me move on to the last section and I'll be done.

This course has been extremely educational. It broadened my horizons considerably. Of course, it is not like I could dive in and be an expert off the bat, but I really understand the power of masking and projections now.

I had no idea that hard surface sculpting could be this viable.

7:15pm. > Cane Townsend: Whenever I post my work, I often get messages asking whether I use Fusion or some other traditional hard surface program.

He notes that this does speak to the average person's ability to actually see the slight surface imperfections and says that this is due to the textures and the lighting distracting from the viewport imperfections.

7:30pm. I am done.

7:50pm. Yeah, there is nothing I want to watch anymore.

7:55pm. I am done with tutorials. The only other program I can foresee myself studying would be Marvelous Designer. But now I've done a mostly complete tour.

Adobe Illustrator, Clip Studio Paint, Blender, Houdini, Clarisse, Substance Painter & Designer, Moi 3d, and now Zbrush. The last 4 were in the last month alone. These are all the art programs I've studied in depth. Blender and Houdini take the lead in the time spent studying them.

Now, I need to get serious. I am going to finish the monitor, texture it and move to the rig. I'll do the props in my room using Moi. Zbrush would be overkill. They are simple enough and have little in the way of detail. I want to get through this matery challenge that really should be been way easier than I have been making it.

Really, any style will do here.

But I really was missing the quad remesher. The subdiv style benefits from using ngons and triangles, but that results in abysmall topology.

What Cane showed me was just one way of doing it. It was quite effective sure, but I'll find my own way.

I have the power to do it now.

Just think - at the start of the month, I hadn't even known how to properly bevel edges. I was a complete hard surface beginner. But now I should be better.

I just need some practice.

8:10pm. It sure took some time for me to get all the basics down. I might not even need Marvelous Designer for clothing for all I know. Zbrush has some of that functionality, but I have no idea how extensive it is.

I do not need to worry too much about clothes. I need to make sure it fits and that the creases are there, but that is just an extension of skills I already have. it would be another thing if I wanted to do animation, but I should manage it with sculpting.

The same thing goes for creating natural disasters like tsunamis and such. No way am I going to waste my time trying to simulate that in Houdini when I am just doing an illustration.

I put all this effort into texturing too, but having great looking textures is only important up close. For things further off, I can get away with a lot less detail.

8:25pm. If I was really good at 2d, I would never bother going to these lengths, but I can only make up for my lack of ability to throw a punch by getting a gun. That is the kind of thing this is.

8:30pm. Tomorrow, I'll do the review. Right now let me close early for once. I've been having extended study sessions for a long time now. Next month is going instead be filled with modeling and texturing sessions. If I just continued studying any further, even I myself would start doubting my intentions."

---
## [shiou0319/web-programming-exercise](https://github.com/shiou0319/web-programming-exercise)@[4998124b4c...](https://github.com/shiou0319/web-programming-exercise/commit/4998124b4cccaf38d835bce8333e99148a5e8eca)
#### Friday 2022-04-29 18:51:44 by shiou0319

Add files via upload

(0) Download the official NCKU logo 1 and Lucid Dreamer mp3 (on moodle) files, and store the files in the directory “Media” under your home.
(1) Use the local file you just stored in the Media directory to insert the logo 1. Adjust the width of the logo to 200.
(2) Use the link of logo 2 to insert the logo 2 directly. Adjust the width of the logo to 200. Add link in the logo 2 and make it link to the homepage of NCKU (web.ncku.edu.tw).
(3) Use the mp3 file as the background music. Show the controller of the music. By default, make themusic play automatically and muted while user open the page. (Tested by Edge)
(4) Embed this Youtube video in you page (https://www.youtube.com/watch?v=6V7oVQ05oSA). Make sure the video cannot be played in Fullscreen. Set the width to 640 and the height to 360.
(5) Create a hyperlink “Email me”. After being clicked, the link will open your default email application and tend to send an email to you student email account.
(6) Create a hyperlink “Contact NCKU”. After being clicked, the link will open your default phone application and tend to call NCKU (06) 275-7575.
(7) Add an unordered list, “My favorite sites:”, and an ordered list under Facebook for the following items:
˙Youtube
˙Wikipedia
˙Amazon
˙Facebook
A. Instagram
B. WhatsApp
C. Oculus VR
(8) Create following table by <table>. (note: border="1")
Fruit Juice Drinks and Meals
Fruit Juice Drinks
Apple Orange Screwdriver
Meal Breakfast 0 1 0
Lunch 1 0 0
Dinner 0 0 1
Total 1 1 1

---
## [lyz-code/blue-book](https://github.com/lyz-code/blue-book)@[2f0e0532d5...](https://github.com/lyz-code/blue-book/commit/2f0e0532d53d86385fb36bb396f198b3d7b3fde5)
#### Friday 2022-04-29 19:38:56 by Lyz

feat(code_learning): Introduce guidelines to learn how to code

Learning to code is a never ending, rewarding, frustrating, enlightening task.
In this article you can see what is the generic roadmap (in my personal opinion)
of a developer. As each of us is different, probably a generic roadmap won't
suit your needs perfectly, if you are new to coding, I suggest you find
a [mentor](mentoring.md) so you can both tweak it to your case.

feat(frontend_learning): Introduce guidelines to learn how to become a frontend developer

This section is the particularization of the [Development learning article](code_learning.md) for a frontend developer, in particular a [Vue](vuejs.md) developer.

A Front-End Developer is someone who creates websites and web applications. It's
main responsibility is to create what the user sees.

The basic languages for Front-End Development are [HTML](html.md),
[CSS](css.md), and [JavaScript](javascript.md). Nowadays writing interfaces with
only the basic languages makes no sense as there are other languages and
frameworks that make better and quicker solutions. One of them is
[Vue](vuejs.md), which is the one I learnt, so the whole document will be
focused on this path, nevertheless there are others popular ones like:
[Bootstrap](https://www.w3schools.com/whatis/whatis_bootstrap.asp),
[React](react.md), [jQuery](https://www.w3schools.com/jquery/default.asp) or
[Angular](https://www.w3schools.com/jquery/default.asp).

The difference between Front-End and Back-End is that Front-End refers to how
a web page looks, while back-end refers to how it works.

feat(mentoring): Introduce the concept and guidelines of mentorship

[Mentoring](https://en.wikipedia.org/wiki/Mentorship) is a process for the
informal transmission of knowledge, social capital, and the psychosocial support
perceived by the recipient as relevant to work, career, or professional
development; mentoring entails informal communication, usually face-to-face and
during a sustained period of time, between a person who is perceived to have
greater relevant knowledge, wisdom, or experience (the mentor) and a person who
is perceived to have less (the apprentice).

feat(park_programming): Introduce the park programming concept

Park programming is as you may guess, programming in parks. It includes
guidelines on:

* How to park program
* Finding the best spots
* Finding the best times

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8e7bbd8ed2...](https://github.com/mrakgr/The-Spiral-Language/commit/8e7bbd8ed23996b6c4264bc6fc7efa3c122cd7b5)
#### Friday 2022-04-29 20:53:35 by Marko Grdinić

"9pm. Actually I feel like doing it a bit more.

https://youtu.be/fS8e0x03p_s
[Blender] Modeling Realistic Sci-Fi Helmet w/ Rachel Frick | Part 1: Beginning Modeling

This was posted in that old HS thread on /3/.

https://youtu.be/fS8e0x03p_s?t=908

I am just skimming stuff here. The most interesting part to me is how she is retopoing here. Yeah, to get smooth surfaces, blocking out using the sculpting brushes and then switching gears into this might be a really good idea.

Sculpting brushes are good for sketching things out, and subdiv would be good for edge control once you have the basic shape down. I should consider this kind of thing for the monitor if the quad remesher fails me.

I actually hadn't considered doing things like that as it would be too much work, but it might be less work than the possibilities.

Sculpt and retopo for HS modeling? Why not. Maybe the chads do do it like that.

This way would bring all the styles together. I should go for it.

https://youtu.be/fS8e0x03p_s?t=374
> My way of thinking about sculpting is just as a 2d sketch for my 3d model.
> The sculpt itself took only 40m to make.

I should aspire to this.

https://youtu.be/muHEQu_tNAY?t=17

Doing it like this certainly makes more sense than trying to polish it, at least in Blender. Subdiving would give you those smooth polished surfaces along with the edges on its own. But that is assuming you could get the quad topology right in the first place.

https://youtu.be/muHEQu_tNAY?t=678

Here she is mentioning that sometimes it happens with crease that top faces will pinch over the bottom faces, and suggest to just use edge loops when that happens.

9:45pm. https://youtu.be/5Hl3qI81aTc?list=PL4w6jm6S2lzu4pj4SsPdw62qx6tXqpefE&t=10

There is absolutely no reason why I shouldn't be able to do something like this. It really did take her 40m to model it. This is not a speedup like the radio for example.

https://youtu.be/5Hl3qI81aTc?list=PL4w6jm6S2lzu4pj4SsPdw62qx6tXqpefE

She applied the first level and will got a bit further to add extra details to the model.

10:05pm. Hmmm, right! This is what I did wrong with the monitor. I put the loop edges microscopically close isntead of doing the densible thing of applying the modifier once and refining it.

I should have noted it, but with just a single level of subdiving there was no pinching in those corners. They only became a problem afterwards.

https://youtu.be/5Hl3qI81aTc?list=PL4w6jm6S2lzu4pj4SsPdw62qx6tXqpefE&t=681

She applies it again.

10:10pm. https://youtu.be/5Hl3qI81aTc?list=PL4w6jm6S2lzu4pj4SsPdw62qx6tXqpefE&t=779

This method is quite elegant. I should have watched this video earlier. It would have given me a lot of inspiration.

Watching this is the most ideal way of finishing the month.

https://youtu.be/5Hl3qI81aTc?list=PL4w6jm6S2lzu4pj4SsPdw62qx6tXqpefE&t=829

Hmmm, why is she splitting that edge? It does not seem to be doing anything.

https://youtu.be/5Hl3qI81aTc?list=PL4w6jm6S2lzu4pj4SsPdw62qx6tXqpefE&t=878
> It's crazy just, um, just what a couple of loop edge will do to just strengthen those bevels. Those beveled edges like this. And they always catch the light so nicely. And you'll see when I light this how great those beveled edges catch the light. And you can see just little glints shimmering off of them.

https://youtu.be/5Hl3qI81aTc?list=PL4w6jm6S2lzu4pj4SsPdw62qx6tXqpefE&t=1151

Ah, yes compositing. Something I don't care about. Maybe I'll have to at some point.

10:30pm. Let me close for real. This kind of workflow is a closer match to what I should be doing. Instead of ramming 3 subdiv levels off the bat, I should have gradually increased them during my work on the monitor. Cleaning up after booleans couldn't be helped.

Yeah, what I needed is not Zbrush specifically, though I might very well end up using it. I knew I was missing something in subdiv modeling, it was gradually scaling the complexity threeshold.

Those who live by inspiration, die by inspiration. I missed the right thoughts. Even though I saw Arrimus using subdiv I did not get it until now.

10:40pm. I won't put myself into a situation, where I'd need to immitate Cane's technique. Such a messy way of doing it does not really suit my way of working.

But doing the initial step in Moi/Zbrush and retopoing using the subdiv style would suit me quite well. Whether I use Zbrush or Blender for that part does not matter.

I am going to focus on these thoughts and hold them in my sight all the way to completion.

I am going to clear this mastery challenge. Not only will I clear it, I will aim to do it at an record pace starting from here. Nothing is more amateurish than taking weeks and even months what should be done in a day. I've been instane for the past 7 months and it is time that I establish a regular pace when doing art, much like in programming."

---
## [stassa/nests-and-insects](https://github.com/stassa/nests-and-insects)@[067d5920f1...](https://github.com/stassa/nests-and-insects/commit/067d5920f1e8c43ee108c821deddaaf6b38efcea)
#### Friday 2022-04-29 21:46:43 by YeGoblynQueenne@splinter

Small corrections.
* ADOM is Ancient Domains of "Mystery", not "Darkness", you idiot.
* Wasps don't live many years so they can't be raiding Bees' nests over
  many years.

---
## [gitster/git](https://github.com/gitster/git)@[bdaf1dfae7...](https://github.com/gitster/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Friday 2022-04-29 22:13:20 by Tao Klerks

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
## [FelemixX/Compiler-theory](https://github.com/FelemixX/Compiler-theory)@[8a93b6f383...](https://github.com/FelemixX/Compiler-theory/commit/8a93b6f383c2483956b286cc2e2e8e302c4981ed)
#### Friday 2022-04-29 22:33:04 by FelemixX

Create README.md

This is the most fucked up shit u've ever seen. I'm fucking hate my teacher.

---
## [newstools/2022-startribune](https://github.com/newstools/2022-startribune)@[fbd8df963f...](https://github.com/newstools/2022-startribune/commit/fbd8df963f6560d1c48b4323fc59bbb99af257d5)
#### Friday 2022-04-29 22:53:43 by Billy Einkamerer

Created Text For URL [www.startribune.com/40-year-sentence-for-man-who-fatally-shot-his-ex-girlfriend-in-her-crystal-home/600169066/]

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[a0fa5ba3ce...](https://github.com/Paxilmaniac/Skyrat-tg/commit/a0fa5ba3ce25d019dafa88e1d606e079f7649cc6)
#### Friday 2022-04-29 23:18:43 by SkyratBot

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

