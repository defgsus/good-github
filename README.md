## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-24](docs/good-messages/2022/2022-06-24.md)


1,741,565 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,741,565 were push events containing 2,560,037 commit messages that amount to 179,808,863 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8f0df7816b...](https://github.com/tgstation/tgstation/commit/8f0df7816bae3c5dedf599611cda3e6039024e14)
#### Friday 2022-06-24 01:42:16 by Kylerace

(code bounty) The tram is now unstoppably powerful. it cannot be stopped, it cannot be slowed, it cannot be reasoned with. YOU HAVE NO IDEA HOW READY YOU ARE (#66657)

ever see the tram take 10 milliseconds per movement to move 2100 objects? now you have
https://user-images.githubusercontent.com/15794172/166198184-8bab93bd-f584-4269-9ed1-6aee746f8f3c.mp4
About The Pull Request

fixes #66887

done for the code bounty posted by @MMMiracles to optimize the tram so that it can be sped up. the tram is now twice as fast, firing every tick instead of every 2 ticks. and is now around 10x cheaper to move. also adds support for multiz trams, as in trams that span multiple z levels.

the tram on master takes around 10-15 milliseconds per movement with nothing on it other than its starting contents. why is this? because the tram is the canary in the coal mines when it comes to movement code, which is normally expensive as fuck. the tram does way more work than it needs to, and even finds new ways to slow the game down. I'll walk you through a few of the dumber things the tram currently does and how i fixed them.

    the tram, at absolute minimum, has to move 55 separate industrial_lift platforms once per movement. this means that the tram has to unregister its entered/exited signals 55 times when "the tram" as a singular object is only entering 5 new turfs and exiting 5 old turfs every movement, this means that each of the 55 platforms calculates their own destination turfs and checks their contents every movement. The biggest single optimization in this pr was that I made the tram into a single 5x11 multitile object and made it only do entering/exiting checks on the 5 new and 5 old turfs in each movement.
    way too many of the default tram contents are expensive to move for something that has to move a lot. fun fact, did you know that the walls on the tram have opacity? do you know what opacity does for movables? it makes them recalculate static lighting every time they move. did you know that the tram, this entire time, was taking JUST as much time spamming SSlighting updates as it was spending time in SStramprocess? well it is! now it doesnt do that, the walls are transparent. also, every window and every grille on the tram had the atmos_sensitive element applied to them which then added connect_loc to them, causing them to update signals every movement. that is also dumb and i got rid of that with snowflake overrides. Now we must take care to not add things that sneakily register to Moved() or the moved signal to the roundstart tram, because that is dumb, and the relative utility of simulating objects that should normally shatter due to heat and conduct heat from the atmosphere is far less than the cost of moving them, for this one object.
    all tram contents physically Entered() and Exited() their destination and old turfs every movement, even though because they are on a tram they literally do not interact with the turf, the tram does. also, any objects that use connect_loc or connect_loc behalf that are on the same point on the tram also interact with each other because of this. now all contents of the tram act as if theyre being abstract_move()'d to their destination so that (almost) nothing thats in the destination turf or the exit turf can react to the event of "something laying on the tram is moving over you". the rare things that DO need to know what is physically entering or exiting their turf regardless of whether theyre interacting with the ground can register to the abstract entered and exited signals which are now always sent.
    many of the things hooked into Moved(), whether it be overrides of Moved() itself, or handlers for the moved signal, add up to a LOT of processing time. especially for humans. now ive gotten rid of a lot of it, mostly for the tram but also for normal movement. i made footsteps (a significant portion of human movement cost) not do any work if the human themselves didnt do the movement. i optimized has_gravity() a fair amount, and then realized that since everything on the tram isnt changing momentum, i didnt actually need to check gravity for the purposes of drifting (newtonian_move() was taking a significant portion of the cost of movement at some points along the development process). so now it simply doesnt call newtonian_move() for movements that dont represent a change in momentum (by default all movements do).

also i put effort into 1. better organizing tram/lift code so that most of it is inside of a dedicated modules folder instead of scattered around 5 generic folders and 2. moved a lot of behavior from lift platforms themselves into their lift_master_datum since ideally the platforms would just handle moving themselves, while any behavior involving the entire lift such as "move to destination" and "blow up" would be handled by the lift_master_datum.

also
https://user-images.githubusercontent.com/15794172/166220129-ff2ea344-442f-4e3e-94f0-ec58ab438563.mp4
multiz tram (this just adds the capability to map it like this, no tram does this)
Actual Performance Differences

to benchmark this, i added a world.Profile(PROFILER_START) and world.Profile(PROFILER_START) to the tram moving, so that it generates a profiler output of all tram movement without any unrelated procs being recorded (except for world.Profile() overhead). this made it a lot easier to quantify what was slowing down both the tram and movement in general. and i did 3 types of tests on both master and my branch.

also i should note that i sped up the "master" tram test to move once per tick as well, simply because the normal movement speed seems unbearably slow now. so all recorded videos are done at twice the speed of the real tram on master. this doesnt affect the main thing i was trying to measure: cost for each movement.

the first test was the base tram, containing only my player mob and the movables starting on the tram roundstart. on master, this takes around 13 milliseconds or so on my computer (which is pretty close to what it takes on the servers), on this branch, it takes between 0.9-1.3 milliseconds.

ALSO in these benchmarks youll see that tram/proc/travel() will vary significantly between the master and optimized branches. this is 100% because there are 55 times more platforms moving on master compared to the master branch, and thus 55x more calls to this proc. every test was recorded with the exact same amount of distance moved

here are the master and optimized benchmark text files:
master
master base tram.txt
https://user-images.githubusercontent.com/15794172/166210149-f118683d-6f6d-4dfb-b9e4-14f17b26aad8.mp4
also this shows the increased SSlighting usage resulting from the tram on master spamming updates, which doesnt happen on the optimized branch

optimized
optimization base tram.txt
https://user-images.githubusercontent.com/15794172/166206280-cd849aaa-ed3b-4e2f-b741-b8a5726091a9.mp4

the second test is meant to benchmark the best case scaling cost of moving objects, where nothing extra is registered to movement besides the bare minimum stuff on the /atom/movable level. Each of the open tiles of the tram had 1 bluespace rped filled with parts dumped onto it, to the point that the tram in total was moving 2100 objects. the vast majority of these objects did nothing special in movement so they serve as a good base case. only slightly off due to the rped's registering to movement.

on master, this test takes over 100 milliseconds per movement
master 2000 obj's.txt
https://user-images.githubusercontent.com/15794172/166210560-f4de620d-7dc6-4dbd-8b61-4a48149af707.mp4

when optimized, about 10 milliseconds per movement
https://user-images.githubusercontent.com/15794172/166208654-bc10086b-bbfc-49fa-9987-d7558109cc1d.mp4
optimization 2000 obj's.txt

the third test is 300 humans spawned onto the tram, meant to test all the shit added on to movement cost for humans/carbons. in retrospect this test is actually way too biased in favor of my optimizations since the humans are all in only 3 tiles, so all 100 humans on a tile are reacting to the other 99 humans movements, which wouldnt be as bad if they were distributed across 20 tiles like in the second test. so dont read into this one too hard.

on master, this test takes 200 milliseconds
master 300 catgirls.txt

when optimized, this takes about 13-14 milliseconds.
optimization 300 catgirls on ram ranch.txt
Why It's Good For The Game

the tram is literally 10x cheaper to move. and the code is better organized.
currently on master the tram is as fast as running speed, meaning it has no real relative utility compared to just running the tracks (except for the added safety of not having to risk being ran over by the tram). now the tram of which we have an entire map based around can be used to its full potential.

also, has some fixes to things on the tram reacting to movement. for example on master if you are standing on a tram tile that contains a banana and the TRAM moves, you will slip if the banana was in that spot before you (not if you were there first however). this is because the banana has no concept of relative movement, you and it are in the same reference frame but the banana, which failed highschool physics, believes you to have moved onto it and thus subjected you to the humiliation of an unjust slipping. now since tram contents that dont register to abstract entered/exited cannot know about other tram contents on the same tile during a movement, this cannot happen.

also, you no longer make footstep sounds when the tram moves you over a floor
TODO

mainly opened it now so i can create a stopping point and attend to my other now staling prs, we're at a state of functionality far enough to start testmerging it anyways.

add a better way for admins to be notified of the tram overloading the server if someone purposefully stuffs it with as much shit as they can, and for admins to clear said shit.
automatically slow down the tram if SStramprocess takes over like, 10 milliseconds complete. the tram still cant really check tick and yield without introducing logic holes, so making sure it doesnt take half of the tick every tick is important
go over my code to catch dumb shit i forgot about, there always is for these kinds of refactors because im very messy
remove the area based forced_gravity optimization its not worth figuring out why it doesnt work
fix the inevitable merge conflict with master lol
create an icon for the tram_tunnel area type i made so that objects on the tram dont have to enter and exit areas twice in a cross-station traversal

    add an easy way to vv tram lethality for mobs/things being hit by it. its an easy target in another thing i already wanted to do: a reinforced concept of shared variables from any particular tram platform and the entire tram itself. admins should be able to slow down the tram by vv'ing one platform and have it apply to the entire tram for example.

Changelog

cl
balance: the tram is now twice as fast, pray it doesnt get any faster (it cant without raising world fps)
performance: the tram is now about 10 times cheaper to move for the server
add: mappers can now create trams with multiple z levels
code: industrial_lift's now have more of their behavior pertaining to "the entire lift" being handled by their lift_master_datum as opposed to belonging to a random platform on the lift.
/cl

---
## [Xen0byte/terminal](https://github.com/Xen0byte/terminal)@[8962f88f90...](https://github.com/Xen0byte/terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Friday 2022-06-24 01:52:41 by Dustin L. Howett

Disable the VT color quirk for pwsh and modern inbox powershell (#13352)

In #6810, we introduced a "quirk" for all known versions of PowerShell
that suppressed their requests for black background/gray foreground.
This was done to avoid an [issue in PSReadline] where it would paint
black bars all over the screen if the default background color wasn't
the same as the ANSI black color.

Years have passed since that quirk was introduced. The underlying bug
was fixed, and the fix was released broadly long ago. It's time for us
to remove the quirk... almost.

Terminal still runs on versions of Windows that ship a broken version of
PSReadline. We must maintain the quirk there -- the user can't do
anything about it, and we would make their experience worse if we
removed the quirk entirely.

PowerShell 7.0 also ships a broken version of PSReadline. It is still in
support for another 6 months, but updates have been available for some
time. We can encourage users to update.

Therefore, we only need the quirk for Windows PowerShell, and then only
for specific versions of Windows.

_Inside Windows_, we don't even need that: we're guaranteed to be built
alongside a fixed version of PowerShell!

Closes #6807

[issue in PSReadline]: https://github.com/PowerShell/PSReadLine/issues/830#issuecomment-650508857

---
## [zeeb92/tgstation](https://github.com/zeeb92/tgstation)@[9428d97a4f...](https://github.com/zeeb92/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Friday 2022-06-24 02:41:47 by Imaginos16

[MDB IGNORE] The Tilening V2 - Damaged Tile Overlays Edition (#67761)


About The Pull Request

Hello once more! As we near summer, I continued to reminisce on several PRs done throughout last year! One of them was the controversial, but rather positive Tilening V1, as done by me and Twaticus a while back (#58932), and felt I could've done a better job with how it was presented.

And thus, thanks to @Fikou encouraging me with a very interesting find of a previous tile resprite attempt, I've successfully done it!

Ladies and Gentlemen, I present to you all, Tilening Version Two!
image

Now this isn't your run of the mill tile resprite. While I did improve the appearance of several tiles I haven't touched last time (including the showroom/freezer tiles now), I decided to do something special that most mappers shall appreciate!

Don't you hate it when of all damaged states, there's only ones for grey tiles when we have white, black, terracotta and a bunch of other materials? Don't you wish they were overlays instead?

Well golly gee do I have good news for you!
image
image

After painstakingly spending at least several hours trying to learn enough code to pull it off, I have successfully made it so most tiles display transparent versions of damage overlays over them! This means mappers can express their creativity that much better! And thanks to how the code is written, its super easy to snowflake certain tile types to make them use unique damaged states (looking at you wooden tiles), so fret not in that aspect.

Credits to:
@WJohn For actually making those damaged overlays! Wouldn't've done the PR if it wasn't for you.
@dragomagol, @RigglePrime and @LemonInTheDark for helping me out in a VC at 10 PM to 12 AM troubleshooting the code to make this improvement work!
Why It's Good For The Game

The shading is done better as compared to last time, making them feel more cubical and less like a pancake when seen from above! This PR also makes it so that we never ever have to touch damaged tiles ever again potentially, saving up some RSC regarding icons.

However, due to how damaged tiles are currently mapped in, rather than overlayed as I envision in the future, it'll require a PR by San to be merged later that should make it safe to remove these icons.
Changelog

cl PositiveEntropy, WJohnston, Dragomagol, LemonInTheDark, Riggle
imageadd: Resprites most variety of tiles into a better shaded version!
code: Damaged floors are now damaged overlays, meaning that most tiles should properly display a damaged state!
/cl

---
## [Tax0787/Beryllium-tree-main-Neutron](https://github.com/Tax0787/Beryllium-tree-main-Neutron)@[b270b793b4...](https://github.com/Tax0787/Beryllium-tree-main-Neutron/commit/b270b793b4405b44325bf534a1cd298fb124193b)
#### Friday 2022-06-24 04:05:34 by Tax0787

make good for ..... md file...
joke : holy shit!! I can't speak English!!
I go to run English!!

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b8566b2ef4...](https://github.com/treckstar/yolo-octo-hipster/commit/b8566b2ef4bf6c8d19e64053376bce797ed00614)
#### Friday 2022-06-24 04:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [metabase/metabase](https://github.com/metabase/metabase)@[9c4e73899e...](https://github.com/metabase/metabase/commit/9c4e73899e8914fd41e85987d4a652a9b6058d8a)
#### Friday 2022-06-24 04:47:01 by dpsutton

Enterprise settings (#23441)

* Allow for disabling settings

Disabled settings will return their default value (else nil if no
default is set). This allows us to have enterprise override settings and
use them from regular OSS code without classloaders, extra vars,
remembering to check if the feature is enabled, etc.

Motivating examples are the appearance settings. We allow
`application-font` setting to change the font of the application. This
is an enterprise feature, but anyone can post to
`api/setting/application-font` and set a new value or startup as
`MB_APPLICATION_FONT=comic-sans java -jar metabase.jar` and have the
functionality.

Same thing for application colors in static viz. The calling code just
calls `(settings/application-colors)` and uses them but doesn't check if
the enterprise settings are enabled. To do this correctly, you have to
remember to implement the following onerous procedure:

A whole namespace for a setting
```clojure
(ns metabase-enterprise.embedding.utils
  (:require [metabase.models.setting :as setting :refer [defsetting]]
            [metabase.public-settings :as public-settings]
            [metabase.public-settings.premium-features :as premium-features]
            [metabase.util.i18n :refer [deferred-tru]]))

(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :getter (fn []
            (when (premium-features/hide-embed-branding?)
              (or (setting/get-value-of-type :string :notification-link-base-url)
                  (public-settings/site-url)))))
```

And then in the calling code you have to do the procedure to
conditionally require it and put it behind a var that can handle it
being nil:

```clojure
;; we want to load this at the top level so the Setting the namespace defines gets loaded
(def ^:private site-url*
  (or (u/ignore-exceptions
        (classloader/require 'metabase-enterprise.embedding.utils)
        (resolve 'metabase-enterprise.embedding.utils/notification-link-base-url))
      (constantly nil)))

;; and then the usage
(defn- site-url
  "Return the Notification Link Base URL if set by enterprise env var, or Site URL."
  []
  (or (site-url*) (public-settings/site-url)))
```

Far nicer to just place the following into the regular public-settings
namespace:

```clojure
(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :enabled?    premium-features/hide-embed-branding?)
```

Then no need for a custom namespace to hold this setting, no need to
have an extra var to point to the setting else a fallback value.

Note that this feature is not required on every enterprise feature we
have. We a namespace `metabase-enterprise.sso.integrations.sso-settings`
that has 24 settings in it, all of which are enterprise features. But
these features are used in our enterprise sso offerings and are directly
referenced from the enterprise features. No need for the extra var to
point to them and the flag checks happen in other parts.

* Mark the UI/UX customization settings as requiring whitelabeling

Mark the following settings as requiring
premium-settings/enable-whitelabeling? (aka token check)

- application-name
- loading-message (override of "doing science")
- show-metabot (override of showing our friendly metabot)
- application-colors
- application-font
- application-logo-url
- application-favicon-url

Updates the helper functions for colors to use the setting rather than
feeling entitled to use a lower level `setting/get-value-of-type`. We
need the higher level api so it takes into account if its enabled or
not.

* Move notification-link-base-url into regular settings with enabled?

* Cleanup ns

---
## [TestSklave11/ECommerceTestProjekt](https://github.com/TestSklave11/ECommerceTestProjekt)@[fe3171675a...](https://github.com/TestSklave11/ECommerceTestProjekt/commit/fe3171675ac8eda64846764c4aa908766fba9df0)
#### Friday 2022-06-24 05:20:51 by TestSklave11

Update index.html

I want to be your Slave so deeply. I will work for free and give you money. I am the real deal. I am a deep wet dream my brother. Call me Testsklave11  !

---
## [TimJones7/IdentityFramework1-FrankLiu](https://github.com/TimJones7/IdentityFramework1-FrankLiu)@[0700e8828a...](https://github.com/TimJones7/IdentityFramework1-FrankLiu/commit/0700e8828a8dcddd73a6bbb0de6f83f64e0dff1d)
#### Friday 2022-06-24 05:42:27 by Tim Jones

god damn fucking adding project to solution and its not in fukin github

---
## [Pusheon/Mewdeko](https://github.com/Pusheon/Mewdeko)@[bdf8b8ccb4...](https://github.com/Pusheon/Mewdeko/commit/bdf8b8ccb405c2e13a77611c5e458ce692efbdeb)
#### Friday 2022-06-24 05:59:17 by Yuno Gasai

upgrade packages and add string extension, fuck you M$

---
## [rohittembhurne2194/ICTSBMALL_ULB](https://github.com/rohittembhurne2194/ICTSBMALL_ULB)@[bc0bee9426...](https://github.com/rohittembhurne2194/ICTSBMALL_ULB/commit/bc0bee94260bcb00739ee48d1a3497c2c64e17b7)
#### Friday 2022-06-24 06:28:34 by umeshl@appynitty.com

Chnages done By Millionaire persone and its me peaceminded aka Umesh i Will Be definielty successfull in this year in trading as well as i will be open my youtube channel for vloging and trading thanku god for this beautifull life sorry  for my any mistake god is with me always god blessed me

---
## [Anlominus/HacKingPro](https://github.com/Anlominus/HacKingPro)@[ee3f002e32...](https://github.com/Anlominus/HacKingPro/commit/ee3f002e3208379e69db2928c66d4d62b5f93b47)
#### Friday 2022-06-24 06:32:52 by Aภl๏miuภuຮ

PhishMailer

PhishMailer
Coded By BiZken

Special Thanks To Fanny Hasbi For helping Me With The Code Structure: https://github.com/fannyhasbi

PhishMailer Will Help You To Create Professional Phishing Emails Fast And Easy

If You Copy The Code And Make Your Own, Don't forget To Give Me Some Credit Kid!
You Don't Get Creds Using This Tool
Legal Disclaimer
I Won't Say That You Can Only Use This Tool For Educational Purposes And That You Can't Use It To Hack Other People Because I Have used It To Hack Others But Remember That It Is Illegal To Do It So If You Get Caught You're On Your Own Don't Come To Me And Blame Me For It

Features
Phishing Email Creator With 20 Different Templates:
Instagram
Facebook
Gmail(2)
Twitter
Paypal
Snapchat(2)
Spotify
Linkedin
Discord
Dropbox
Steam
RiotGames (League Of Legends)
Rockstar SocialClub
BlockChain
DreamTeam
000Webhosting
AskFM
Gamehag
And More Are On The Way
Creates .HTML
Send your emails to your target
Easy To Use

---
## [FantasticFwoosh/Merchant-Station-13](https://github.com/FantasticFwoosh/Merchant-Station-13)@[2a3b63c243...](https://github.com/FantasticFwoosh/Merchant-Station-13/commit/2a3b63c2434fec55f7dd1f232455d1594c21809f)
#### Friday 2022-06-24 07:07:40 by BettonnCZ

Adds a new sprite for the stacker (#196)

fuck you

---
## [itIsMaku/fivem](https://github.com/itIsMaku/fivem)@[02df4a52b1...](https://github.com/itIsMaku/fivem/commit/02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9)
#### Friday 2022-06-24 07:50:00 by blattersturm

tweak(client/core): nvidia, fuck you.

Apparently ba693365d151cb3d61e1fd1bc08f9f65f66d13ae wasn't enough to fix
the .toc corruption from nvPSShaderDiskCache.cpp/the NvShaderDiskCache
perf strategy.

Instead, this change just disables the shader cache entirely. Using a
hacky way.

---
## [itIsMaku/fivem](https://github.com/itIsMaku/fivem)@[6051b8790c...](https://github.com/itIsMaku/fivem/commit/6051b8790c185b2435da75c2f41f59ec3be4578f)
#### Friday 2022-06-24 07:50:00 by blattersturm

Revert "tweak(client/core): nvidia, fuck you."

The gift that keeps on giving: NVIDIA drivers. Some users seem to crash
in new places with `disable.txt` present and used.

Seriously?!

This reverts commit 02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9.

---
## [Taliyan13/Fab-Freak-web-application](https://github.com/Taliyan13/Fab-Freak-web-application)@[ccf9a2c658...](https://github.com/Taliyan13/Fab-Freak-web-application/commit/ccf9a2c6588d60610ddc6276cfb33c7a85923185)
#### Friday 2022-06-24 08:01:48 by Taliyan13

Add files via upload

Fab-freak app Was created in order to reduce the quick online shopping and emphasize the clothes and footwear we have in the private closet and can integrate perfectly with Other items from our closet.
A bright spot on combinations we would not think of and rush to purchase a new item.
The app allows you to assemble and upload locks from existing items in your personal closet, store the items under categories - work, entertainment, event, studies - share them with friends who also downloaded the app and take inspiration from combinations of people on net.

---
## [oslocyclotronlab/ompy](https://github.com/oslocyclotronlab/ompy)@[413d25cb40...](https://github.com/oslocyclotronlab/ompy/commit/413d25cb4003b6e527e854bad837656044b9fe14)
#### Friday 2022-06-24 09:42:52 by Erlend Lima

Major rewrite of OMpy. Incomplete, and should NOT be used yet.

An incomplete summary:

* vector
  - Either (`values` and `E`) or `path` is mandatory for initialization.
    Allowing for partial initialization has only been a source for complex
    initialization logic and a cause for bugs. No other code in ompy relies on
    partial initialization, so this feature is removed.
  - Remove `shape` as an argument for initialization.
  - Fix bug with how `std` can overwrite the loaded std to `None`.
  - Rename the argument `E_new` of `Vector.closest()` to `E`.
    Make the argument names in line with the rest of the code.
    The suffix `new` is redundant as there are no other `E` vectors to be confused with.
  - Change name of `cumulative()` to `cumsum()` to be in line with `numpy.cumsum()`
  - Change the default value of `factor` to `1.0` in `cumsum()` and remove superfluous `None`.
  - Add `set_order()`, a wrapper around numpy `set_order`. This is to make it
    easier to set the bit alignment when calling cython.
  - Change `verify_equidistant() -> None` to new `is_equidistant() -> bool`.
    Makes it more usable to check if a vector is equidistant instead of
    raising an exception.
  - Add `sum()` as a wrapper around `np.sum(vector.values)`.
  - Rename `cut_nan()` to `drop_nan()`. This is in line
    with the usual meaning of `drop`, as `cut` implies the
    ends are being trimmed, not that elements in the middle are
    removed.

* matrix
  - Either (`values`, `Ex` and `Eg`) or `path` is mandatory for initialization.
    See ^vector.
  - Make several methods return self for easier chaining.
  - Add `to(unit)` for changing the units and returning a copy.
  - Add `to_same_Ex(E)` and `to_same_Eg(E)` methods to set
    the `E` to be compatible in units with Ex and Eg.
    Allows for easier comparisons of the magnitudes.
  - Remove `ZerosMatrix`.
    Adding a type for only initialization is cumbersome, as a type should
    capture different behavior, not content.
  - Add units to `Eg` and `Ex`.
  - Deprecate `fill`. Use `Matrix[i, j] += c`, `Matrix(Eg, Ex) += c`,
  - Change default value of `inplace` to `False` for `cut()`, `cut_like()` and
    `cut_diagonal()`.
  - Fix a bug in `cut` where the boundaries could be set incorrectly.
  - Add two new methods for creating a sub-matrix:
    - IndexLocator
    - ValueLocator
  - `projection` is simplified by relying on `ValueLocator` and returns a `Vector`.
    The upper bound `Emax` is no longer inclusive by default.
  - The `plot_projection` is useless and is removed.
    One can instead use `mat.projection(args and kwargs).plot()`.
  - There seems to be a bug (or perhaps feature?) with matplotlib where
    the cmap range favors lower values, and the range has a maximum range. The result
    is that even though a matrix contains large bins, the bins are not represented in the
    cmap, leading to confusion. Possible solution: If we detect bins with negligible counts
    and a too narrow cmap range, set vmin to something sensible. This is implemented and seems to
    work well.

* Extractor
  - Fix issue 181
  - Add a simple load method. Not enough to reconstruct an Extractor.

* General Changes
  - This patch contains a whole load of breaking changes.
    The rationale is that the earlier code had several design
    decisions I thought were clever and flexible, but that have
    proven to be unnecessary and only make it easier to introduce bugs.
  - Rename `Union[T, None]` to `Optional[T]`.
  - Make `inplace` arguments default to `False`.
    The reasoning is that most Pythonic functions with an option
    for inplace mutation opts for immutable by default.
    In addition, almost all usages in OMpy use `inplace=False`.
  - Add `binwidth` argument to `rebin()`.

* Units
  - The units of energy for both vectors and matrices defaults to `keV`.
  - The units are stripped if the energy is involved in any computation.

* Rebinning
  - The rebinning fails if rebinning to smaller bins,
    and in some edge cases due to float rounding error.
  - The rebinning does not preserve Poisson statistics.

* Unresolved problems
  - Setting default values in plotting functions will override
    the default values the user has earlier set implicitly.
  - How to handle `om.Vector(values=values)` without any energies?
    I see no reason to not provide the energy. If the user only wants to use
    the vector with values, then a numpy array should have sufficed. They main
    reason one would omit the energy is by mistake, in which case it should
    be reported as an error. This is default behavior for now.
  - Should Vector/Matrix copy their arguments by default?
    If true, then one will exclude a source of sloppy error, but
    at the expense of bloated memory usage.
    If false, then the user error might go up, but the behavior will
    be more consistent with Pythonic usage of references instead of copies.
    To err on the side of caution, it arguments are copied.
  - Vector&Matrix arithmetic is not implemented.
    I don't know whether it makes sense to ever perform Vector*Matrix.
  - `Matrix.cut()` is unpythonic, with `Matrix = Matrix[start:stop, start:stop]`
    being more natural. For slicing with energy one can use 'Matrix.loc[]'. However,
    one of the reason we implemented `.cut()` in the first place is because of the
    trickiness of inclusive or exclusive values. Having already thought through it and
    defaulted to inclusive energies, we can save future headache by using `.cut` instead
    of square brackets.
  - Have `turbo` as default colormap?
  - The argument `factor` in `vector.cumsum` (formerly `vector.cumulative`)
    seems arbitrary. What is the reasoning for its inclusion?
  - In general, rebinning does not preserve total count.
    For nice numbers, numbers we usually use while testing, the
    counts are preserved. The problem is when the number of bins increases,
    upscaling the data se
    - Rebinning does not take into account std or variable bin size.
  - It might be ergonomic to introduce a generalized way to
    manipulate the vectors/matrices while preserving their
    integrity, similar to pandas `df.apply` or `df.query`.
  - I suggest we avoid the copy module as much as possible.
    Despite its name, it does not actually copy an object, it only
    copies a particular type of "variable" (formally only elements
    of __slots__). Using it leads to loads of nasty edge cases where
    attributes go missing or have wrong values. The new
    `clone()` method is functionally equivalent to a clean copy,
    by creating a new object with the same values.
  - 'response.py' is a Cthulhuian mess. Should be refactored.

* Pet Peeve Proposals
  None of these changes are implemented, but are thorns that
  annoy me.
  - Change the return value of `.plot()` functions to
    `ax` instead of `(fig, ax)`. I usually ignore the `fig` value,
    forcing me to use type `_, ax = mat.plot()`. If I would like
    to use `fig`, it can be recovered from `ax` with `ax.figure`.
  - Remove `path` arguments from `__init__()`. The `__init__()`s
    of the different classes are terribly complicated. Would remove
    the surface for bugs and mental complexity by forcing some of the arguments
    to become obligatory instead of optional. The logic performed by
    `path` can be move to a `classmethod` instead. This is more inline with
    how other packages like `numpy` and `pandas` work. For example:

    ```python
    # Before
    mat = om.Matrix(Eg=Eg, Ex=Ex, values=values)
    mat2 = om.Matrix(path="path/file.npy")
    # this raises our custom ValueError
    mat = om.Matrix(Eg=Eg, values=values)

    # After
    mat = om.Matrix(Eg=Eg, Ex=Ex, values=values)
    mat2 = om.Matrix.load(path="path/file.npy")
    mat3 = om.load(path="path/file.npy")
    # this raises inbuilt TypeError
    mat = om.Matrix(Eg=Eg, values=values)
    ```

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ad9c77cb7a...](https://github.com/mrakgr/The-Spiral-Language/commit/ad9c77cb7a1b0d75a3a1749937afbd1c5151f8be)
#### Friday 2022-06-24 10:08:46 by Marko Grdinić

"The spot in the middle is too empty. Let me put down the Grand Casino.

4pm. It crashed so hard it took down the whole rig with it. Thankfully I am saving as I go along.

Right now I am trying to get the overall color composition right. Having an emissive floor is not a good idea. It messed with the light from other sources.

4:10pm. It crashed again. Maybe it is linked to Cycles being on.

4:15pm. And again. Ugh. Reminds me of V-Ray in Houdini.

4:25pm. This is the 4th time Cycles took down my entire system. Sigh...

4:35pm. 5th time. Blender is very crash happy in the latest version. Let me play around with the monkey head. I want to refresh my memory of the volume shader.

4:40pm. 6th time, this time on just the monkey head. Were the older version this unstable? Cycles in unusable here.

https://developer.blender.org/T96133

Let me play around in 3.1. Then I will check out 3.0.

Since the file appears to be forward compatible, let me take advantage of that to open it in 3.1.

4:55pm. Too bad Scatter 5 does not work in 3.1. I am obligated to use 3.2 now.

5:10pm. It crashes even with F12. 7th time.

Yeah, Cycles in unusable in 3.2.

I could try upgrading the graphics driver and seeing if that helps. But otherwise, let me just use Eevee. Or even Luxcore.

5:35pm. It seems this scene will get done one reset at a time. Let me take a break so I can upgrade my graphics drivers. Maybe that will help. This is not just an ordinary crash. Each time it took down the entire system.

5:45pm. The driver seems to be a decent behind. I had 517 while the latest is 571. The driver install does not allow me to leave out GeForce Experience. Well, as long as it does not bother me on startup I'll be happy.

Ok, let me give it a try. But I am not too hopeful. This is serious issue. If this does not work, I might end up having to use Eevee.

The save is actually corrupted.

5:55pm. Thankfully there are backups. I am not losing much except time.

I need to stop. I can't work like this.

Did Cycles work in 3.1, I think it did not crash there.

Ok, can I convert the Scatter 5 scene into Blender instances and import them in 3.2.

7:05pm. Done with lunch. While I was busy with that the render finished properly in the background. It seems that 3.1 is stable for me. Now that I have this, let me put it through style transfer.

```py
def save_path(data,path):
    """Returns the save path."""
    def get_name(x):
        base_name = ntpath.basename(data[x][0])
        return ntpath.splitext(base_name)[0]

    a_path = get_name('A_paths')
    image_name = '%s (%s).png' % (a_path, get_name('B_paths'))
    return os.path.join(path, a_path, image_name)
```

Let me change the way saving is done a little. I'll have it create it own dir for every image.

```py
os.makedirs(save_path,exist_ok=True)
```

I think I need to plug this in. Let me try it.

```
PermissionError: [Errno 13] Permission denied: './results/floating city v0\\floating city v0 (anime glasses girl).png'
```

Hmmm...

```
os.makedirs(os.path.dirname(save_path),exist_ok=True)
```

Let me try this.

7:20pm. Yeah, that works. While that is going on I might as well do a bug report.

No, I want to test 3.1 more thoroughly before I jump to conclussion that it is more stable.

7:25pm. Right now what happened is that the style transfer crashed and took the OS with it. Is my GPU dying?

7:35pm. I suppose this will do.

7:55pm. https://developer.blender.org/T99116
Cycles crashes after a few minutes of work

I opened this, but the bug report is not very informative, so I am not sure if anything will come of it.

This scene is cursed!

How is it possible that I am running into problems with Cycles all of a sudden. Just how am I supposed to do this scene?

8:05pm. Let me post one of the images that came out well in /wip/ and then I'll close.

///

This scene is cursed. I got a grasp on Scatter 5, and minus the bugs, its manual mode is revolutionary. It is to scattering what sculpting is to modeling.

I ran into all sorts of bugs with it, found workarounds with the help of the author, but now that I am doing shading I can't go more than 2m without Cycles crashing and taking the OS with it. This is not happening with previous 3.1 version of Blender so I managed to export the building instances and render it there.

I have no choice, but to keep going forward. I have a vague sense of what I want to do, but I am having trouble understanding how to make the scene impactful.

This particular style is not bad in isolation, but I don't think it will work once I add the other half of the scene. The way I am visualizing it is a view of the floating city from below as the golden light from it washes over the landscape. This particular style will make everything golden and that detail would get washed out.

///

I guess I'll post it on Twitter as well.

8:40pm.

> This sounds like a bug in OS or your hardware is failing. I would recommend to check system temperatures, and voltages in case of PSU failiure.
> I don't think remember any issue with similar symptoms to be ever confirmed as bug in Blender.

Got this reply from a Blender dev. Maybe I should open the rig and dust it off. Maybe there is a program that can help me diagnose temperatures and voltages? I should look for it.

8:45pm. Getting called a schizo and told to take my meds on /wip/ is really annoying. Maybe I should drop that place, like I said I would the last two times? Let me do a style transfer on a crab image, reply with it and then I am done for the day.

It actually did crash once while doing style transfer earlier. This really makes me concerned about the state of my hardware. It is quite scary. If the PC gives out before I can make money from Heaven's Key to replace it I really will drop all the art practice and get a job. Some things you simply have to take as an omen.

9pm. https://openhardwaremonitor.org/
> The Open Hardware Monitor is a free open source software that monitors temperature sensors, fan speeds, voltages, load and clock speeds of a computer.

I'll try this program tomorrow. I'll close here today.

*

9:20pm. I got told that it looks like an AI made it. This is due to there being too little variation in the image. Ignoring the big unique one in the middle, the city has only 4 different types of buildings. I need at least 7, and that is 6 of different sizes and rotations. Since this is not a forest, but a city, I can't do rotations and scaling arbitrarily, so I probably need even more. 4 versions for each of the 4 types of buildings. This rule of 7 is a pro tip from Blender Bob, it makes sense to me.

Edit: Also, come to think of it, phrasing it that way is also an attempt at suppression since they know well enough I want to use AI. There is a good cop/bad cop routine going on there, whether purposeful or not. If I fall into the mindset of being petulant and responding to their framing, I'll end up acting like a schizo for real. Much like leaving the PL sub, it is time to abort the /wip/ thread for good.

9:30pm. Forget this. It is time to relax.

11:10pm. > Behind every one of the four beyond Grade A Supers in the Shattered Star Ring were numerous financial groups. A powerful organization would always draw a large number of willing sponsors; thus, these powerful beings never needed to be afraid of going broke. Many of the financial groups in the universe were past the stage of accumulating wealth, and if they were not able to convert their wealth into influence or something useful, their wealth was no more than a useless string of numbers. Investing their wealth into such organizations that housed powerhouses was the best option for them.

Wise author. This is a good point for why people would give money to Ames.

11:55am. Given that it crashed once during style transfer, the CPU itself might be getting overheated. I am going to have to think about what I want to do carefully. I'll take the measurements tomorrow, if it turns out the temps are the problem, I'll open up the rig, dismantle the CPU and the GPUs and clean up the dust inside.

If that fails...then I'll stop work on Heaven's Key and get a programming job. It is one thing to not have hardware to do ML, but if I can't do rendering or style transfer, then there is no point in pursing this plan anymore. The rig is over 7 years old now, so it would not be strange if it started showing signs of wear and tear at some point.

12:20am. This is not the first time it has happened, remember those Luxcore renders before? This might be linked to that.

6/24/2022

11:40am. Damn, I went to bed at 2am, but had trouble falling asleep, so it is not wonder I am this late. My anxiety was high tonight, but surprisingly just telling myself to stop thinking about the troublesome stuff and go to sleep was enough. Even though I am up this late, I actually slept well. Not ideally, but I am not fatigued like I would be usually.

Right now, my main priority will be to check the temps as rendering is done in Blender. If this trouble does not have an easy explanation like CPU or the GPU overheating, then I am going to abort the Heaven's Key quest. What the dev says about this possibly being a hardware error makes complete sense to me. I couldn't write a program to crash the whole OS even if I wanted to. If something was really wrong with Cycles it would crash just Blender, not the whole system.

If the CPU and the GPU are overheating, I can make the problem better by cleaning up the dust inside the rig, but if not, I am screwed. So let me make sure of that.

12pm. Mhhhh, I do not see an option to do regular logging to hard disk. I really want to compare the start and just before it crashes. Right now there is too much info in the application, I can't follow it and play with Blender at the same time.

It has some kind of web server that I could use to exchange data, but I do not know how to make use of that.

12:05pm. https://www.reddit.com/r/buildapc/comments/8dg2op/software_that_can_save_cpu_temperature_vs_time_to/

///

I use Open Hardware Monitor and it is great. You dismissed it, but it does exactly what you want - if you toggle Log Sensors under Options, it will automatically save all sensor data as a function of time to a dated file in the directory the executable is in. The logging interval can be set as well. You can also use the Plot function to visualize your data as they are being recorded.

It is also open source, which is a big plus for me.

///

Oh, really? Great. That solves all my problems.

Before I start, let me chill a little. I guess I'll skip the morning session."

---
## [alphagov/govuk-prototype-kit](https://github.com/alphagov/govuk-prototype-kit)@[2423f4c6df...](https://github.com/alphagov/govuk-prototype-kit/commit/2423f4c6dfb5d04c060fd209fafccce7c89cbdcb)
#### Friday 2022-06-24 12:01:20 by Laurence de Bruxelles

Change tests to generate a release archive only once

Use a lockfile to make sure that if the test helper `mkReleaseArchive()`
is called more than once, it won't create more than one
`create-release-archive` process. The behaviour we want is that it all
calls will block until the initial process has finished.

The way I figured to do that was that all calls try and acquire a
lockfile (atomically), if that lockfile is already held that means
another call is already creating the release archive. When the lockfile
is released, the process should have successfully created a release
archive, so no extra work is needed.

Unfortunately, in Node.js it seems there is no way to block waiting for
a lockfile to be released, so we have to rewrite the test utils and all
relevant tests to be asynchronous. To be fair they should have been
asynchronous in the first place, but it was still a very painful
process.

Note that I haven't rewritten the scripts in `cypress/scripts` to use
async functions; without the use of top-level await it was a bit more
effort than I was prepared to do, compounded with the fact that
there doesn't seem to be an easy way to await `child_process.spawn()`
(`util.promisify` doesn't work), and async `child_process.exec()` and
`child_process.execFile()` don't do `stdio: 'inherit'`. Maybe the only
way around it is to use the `execa` library (: Anyway I couldn't be
dealing with that, so now we have to deal with duplication in
`__tests__/util`. There are ...ways... to reduce the duplication
(proper-lockfile does this with its `lib/adapter` module) but they are a
bit magic, and plus it means writing our code using callbacks, which is
just... woof. No.

Anyway as you can tell this is has been a great learning opporunity :')
Just use async the first time and save myself the pain later!!

---
## [cj-de/Boston-lost](https://github.com/cj-de/Boston-lost)@[ce197303bb...](https://github.com/cj-de/Boston-lost/commit/ce197303bb52dccb6c95c428505e823f00255c66)
#### Friday 2022-06-24 13:14:14 by cj-de

Apache junction 

The police were I live have allowed a group of ppl to gangstalk me for over 8 in September will be 9 years. I'm not crazy the get you all raped up in white collar corporate...... Hospitals labeled crazy... With some b.s. open case shit... You have ruined my life, future in fact what the fuck half the ppl that gangstalk are meth and heroin addicts and shit my bad pharmacy government dope fines

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[88b245aa46...](https://github.com/cockroachdb/cockroach/commit/88b245aa469ee6302a25d3ac4cbe58b23927831d)
#### Friday 2022-06-24 15:13:22 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here]
(https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox]
(https://ant.design/docs/react/getting-started) (render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox]
(https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here]
(https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

---
## [shantanu-sarkar/kernel_sm8150](https://github.com/shantanu-sarkar/kernel_sm8150)@[78f486bfc8...](https://github.com/shantanu-sarkar/kernel_sm8150/commit/78f486bfc851eed70b8e0edc8666208418770ee0)
#### Friday 2022-06-24 15:40:40 by alk3pInjection

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
## [proffrink1/mame](https://github.com/proffrink1/mame)@[ba63081d10...](https://github.com/proffrink1/mame/commit/ba63081d109c904902958c6324b013cb10b42732)
#### Friday 2022-06-24 16:40:34 by 0kmg

gameboy.xml: Added 21 more prototypes. (#9962)

* gameboy.xml: Added 21 more prototypes.

New working software list additions
-----------------------------------
Astérix (earlier prototype) [VGHF, Hidden Palace]
Astérix (early prototype) [VGHF, Hidden Palace]
Asteroids (prototype) [VGHF, Hidden Palace]
Barbie - Game Girl (prototype) [VGHF, Hidden Palace]
Battle Ships (Spain, prototype) [VGHF, Hidden Palace]
Blaster Master Boy (USA, prototype) [VGHF, Hidden Palace]
Bomb Jack (earlier prototype) [VGHF, Hidden Palace]
Bomb Jack (later prototype) [VGHF, Hidden Palace]
Bonk's Adventure (USA, prototype) [VGHF, Hidden Palace]
Bubble Ghost (prototype) [VGHF, Hidden Palace]
Catrap (prototype) [Forest of Illusion, Swanhubstream]
Cosmo Tank (USA, prototype) [VGHF, Hidden Palace]
Dropzone (prototype, alt) [VGHF, Hidden Palace]
Gauntlet II (prototype) [Forest of Illusion, Rezrospect]
Ghostbusters II (prototype) [VGHF, Hidden Palace]
Kung-Fu Master (prototype) [Forest of Illusion, FNeogeo]
Mysterium (prototype) [Forest of Illusion, Rezrospect]
Obélix (Europe, French / German, prototype) [Forest of Illusion]
Prince of Persia (prototype) [Forest of Illusion, FNeogeo]
The Blues Brothers (prototype) [Forest of Illusion, FNeogeo]
Triumph (prototype) [Gaming Alexandria]

---
## [woodsts/linux-stable-rt](https://github.com/woodsts/linux-stable-rt)@[226b3c797c...](https://github.com/woodsts/linux-stable-rt/commit/226b3c797c6246e14c713d048cdb3490a1f67701)
#### Friday 2022-06-24 17:02:43 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [tuh8888/melpa](https://github.com/tuh8888/melpa)@[570bde6b4b...](https://github.com/tuh8888/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Friday 2022-06-24 17:18:31 by Jonas Bernoulli

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
## [yuzefovich/cockroach](https://github.com/yuzefovich/cockroach)@[0a3447944a...](https://github.com/yuzefovich/cockroach/commit/0a3447944ae259b725ebff7d84cecd1b6a1de19c)
#### Friday 2022-06-24 18:04:13 by craig[bot]

Merge #80894 #81200 #81330 #81406

80894: build,gcp: enable nightly config to run GCP unit tests r=adityamaru a=adityamaru

Previously, the `pkg/cloud/gcp` tests package was skipped on CI
because most of the tests require credentials, and we risked exfiltration
of these secrets when running on public teamcity agents.

With the ability to run tests on agents that are not part of the public
pool we now have a `Cloud Unit Test` config that runs these tests nightly.
This change adds the script invoked by the config and cleans up the unit
tests to be more uniform in their authentication and environment variable
checks.

Informs: https://github.com/cockroachdb/cockroach/issues/80877

Release note: None

81200: ui: Improve time picker keyboard input r=jocrl a=jocrl

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here](https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox](https://ant.design/docs/react/getting-started) 
(render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox](https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here](https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

81330: authors: add annrpom to authors r=annrpom a=annrpom

Release note: None

81406: geomfn: check NaN coordinates for ST_MinimumBoundingCircle r=rafiss a=otan

Resolves #81277

Release note (bug fix): Fix a bug where ST_MinimumBoundingCircle with
NaN coordinates could panic.

Co-authored-by: Aditya Maru <adityamaru@gmail.com>
Co-authored-by: Josephine Lee <josephine@cockroachlabs.com>
Co-authored-by: Annie Pompa <annie.pompa@cockroachlabs.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>

---
## [blahberi/SIEPS](https://github.com/blahberi/SIEPS)@[542443ae43...](https://github.com/blahberi/SIEPS/commit/542443ae43e0ee15cf1cc40b77c5b4f8c3e0a59e)
#### Friday 2022-06-24 19:27:24 by kamoodi

ok i have no idea how his code works so i reverted it but theres an easy bug i fixed so youre welcome

fuck you i dont want to write a description

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Friday 2022-06-24 19:30:49 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [DunceAH/new-silver-rythym-rush-characters](https://github.com/DunceAH/new-silver-rythym-rush-characters)@[7dcd5c2c99...](https://github.com/DunceAH/new-silver-rythym-rush-characters/commit/7dcd5c2c9950e9bfb643cc33ef76689262c79383)
#### Friday 2022-06-24 19:32:02 by Dunce_cap

I HATE PLACING THUMBS CORRECTLY

FIXED ALT'S WEIRD MESSED UP THUMBS FACING THE WRONG WAY BECAUSE IM A STUPID IDIOT!!!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9842383936...](https://github.com/mrakgr/The-Spiral-Language/commit/9842383936054a3bd7ae75b633bdc55e288a00ee)
#### Friday 2022-06-24 19:54:05 by Marko Grdinić

"5:20pm. I am strugging to get this to work. I've figured out what the card is, and I've renamed the right one to eth0. I've even done the correct step of doing into the interfaces file and pointing that at eth0. I do not know why, but that is not working.

///

1. burn Ubuntu 14 server in DD mode
2. install LAMP and SSH server during install
3. sudo apt-get update & sudo apt-get upgrade
4. wget http://packages.grasehotspot.org/pool/main/g/grase-repo/grase-repo_1.8_all.deb
5. sudo dpkg -i grase-repo_1.8_all.deb
6. sudo apt-get update
7. sudo apt-get install grase-www-portal grase-conf-freeradius
8.
    remember MAC of main card using ifconfig
	sudo nano /etc/default/grub
	GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0"
	sudo update-grub
	reset
	sudo nano /etc/udev/rules.d/70-persistent-net.rules
	swap router names as needed
9.
	sudo nano /etc/network/interfaces
	edit to refer to eth0 instead of p1p1 or whatever
///

This time I was smart enough to write all the steps down.

But that very last step is not working for me. The internet connection only seems to work if both the relevant card in the '/etc/udev/rules.d/70-persistent-net.rules' file and in the '/etc/network/interfaces' file is named p1p1. This was supposed to be very straightforward, but now Ubuntu is making me suffer and wasting my time again.

Did I miss some step?

https://askubuntu.com/questions/489914/ubuntu-14-04-network-problem
> sudo service network-manager restart

I am sure I never tried this before.

> I modified `/etc/default/grub`, did the grub update, and sure enough the internet connection goes down. I changed the names so that the correct MAC is pointing to eth0, but that did not work. What worked is changing the main card's name from `eth0` to `p1p1`. That makes the Internet work again.

This is exactly the same problem I had before. But unlike last time, renaming it in the interfaces file is not enough to fix the issue.

5:35pm. This is really strange. I am having some inspiration. Does it work if I only set it as p1p2? I get the sense that the interfaces file is not working for whatever reason, but I need to make sure of it.

Let me try again.

6:05pm. The internet works when I set the router to any other name than eth0. This might be due to a name conflict with Grase Hotspot.

Given this, my belief that the main connection should be eth0 is shaken. Does it necessarily have to be eth0, or am I misremembering and could perhaps put it as eth1 last time as well?

Whatever, let me read LM until he gets back. Maybe it will turn out to be okay. If it does not, I'll have to continue work on this. I have no idea what I will do.

7:10pm. I took the chance to have lunch.

Today really demonstrates what the problem is with trying to cultivate multiple skills. The ones not being used simply fade from memory. If I did not keep a journal with notes, trying to trace the steps would be 10x harder. This is not a matter of effort - my memory is simply not good enough to keep all that is needed in it.

This is who knows how many time that I've done this and it is still giving me trouble. A specialist could do this in half an hour.

But today is fine. I might not have any art, but realizing what is causing the crashes and resolving it is like getting a superpower. I'll be able to rest much more easily from here on out.

7:40pm. Right now I am just waiting for dad to finish lunch, so he can come here and test the hotspot. After that it will be out of my hands. I'll also request his help in cleaning up the rig. No doubt after years, there should be a lot of dust on the CPU which should reduce the efficiency of cooling.

9:35pm. I am finally done with it. I had to reinstall it from scratch, but this time I have the proper recipe.

///

1. burn Ubuntu 14 server in DD mode
2. install LAMP and SSH server during install - optional, will be downloaded off the net automatically in case you forgot
3. sudo apt-get update & sudo apt-get upgrade - dpkg will give a weird error if it is out of date
4.
    ifconfig - remember the MAC of main card for the later steps
	sudo nano /etc/default/grub
	edit it so: GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0"
	sudo update-grub
	reset - this will create the rules file
	sudo nano /etc/udev/rules.d/70-persistent-net.rules
	swap router names as needed
5.
	sudo nano /etc/network/interfaces
	edit to refer to eth0 instead of p1p1 - grase needs eth0 to be the internet connection
6. wget http://packages.grasehotspot.org/pool/main/g/grase-repo/grase-repo_1.8_all.deb
7. sudo dpkg -i grase-repo_1.8_all.deb
8. sudo apt-get update
9. sudo apt-get install grase-www-portal grase-conf-freeradius

///

I had the idea of shuffling some of the steps around and that turned out to resolve the issue. I didn't remember it wrong - eth0 has to be the main connection for Grase Hotspot to work. I am really glad to be finally done with it. Every time this happens my dad pesters me about that 'command' I put in to fix things. I forgot what it was so I looked up the Google Groups for my posts on the grase group and remembered what it was. It seems uploads were very slow zero and turning GRO fixed that. That has nothing to do with today's issue.

9:50pm. I am really glad that I have that thing off my hands. It ate my entire day. But it is just as well, it is not like it started particularly well. Last night I was anxious about having to get a job due to my hardware failing, but luck is still on my side. I was fully determined to drop Heaven's Key if that happened, but it seems I will be developing my art skills for a while longer.

Whether that is good for either me or the world remains to be seen."

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[95ffcd4e19...](https://github.com/MTandi/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Friday 2022-06-24 19:58:58 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [mauriciozuardi/seedsigner](https://github.com/mauriciozuardi/seedsigner)@[425d8552ff...](https://github.com/mauriciozuardi/seedsigner/commit/425d8552ff6381b28acfbc70e2f747e58b797699)
#### Friday 2022-06-24 20:17:33 by Marc G

Update README.md

Mauricio - I apologize that I am just learning Github, so I had to make a fork of yours, as i didnt have write access. 
I have proposed here, some wording on Keybase, and what it actually achieves, vs just a Pubkey download. Confirming its the key that is used in all the online presence of the SS project. 

Please let me know what you think of the wording and explanation. I still want to cleanup around the key verify command. The warning is still there and I think there are flags/options to remove it. 

Lastly for tonight, do you have any experience regarding the verify command vs checking the SHA256 sum? I am starting to wonder if the SHA256 check is included in the Verify command, do the documentation is very brief. I will keep looking more at that. 

also please Let me know if its better for me to [somehow] write my changes over into your branch/fork?  

Thanks, this was very interesting learning about keybase.io and identity proofing in the online world.!
Marc.

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[9ccd6ecd74...](https://github.com/microsoft/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Friday 2022-06-24 23:20:31 by Mike Griese

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

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[442432ea15...](https://github.com/microsoft/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Friday 2022-06-24 23:21:17 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---

