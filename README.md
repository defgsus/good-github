## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-06](docs/good-messages/2022/2022-02-06.md)


1,483,527 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,483,527 were push events containing 2,125,611 commit messages that amount to 127,330,482 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [absent-cc/backend](https://github.com/absent-cc/backend)@[aa8032af78...](https://github.com/absent-cc/backend/commit/aa8032af780821183796c743eca3b1953a07d5b1)
#### Sunday 2022-02-06 00:39:00 by Kevin Yang

fixed the fucking pathing holy shit. Now everything is relative and testing and main scripts work

---
## [PeterGottesman/dwm](https://github.com/PeterGottesman/dwm)@[67d76bdc68...](https://github.com/PeterGottesman/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2022-02-06 00:55:02 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [jewelml11/CPT167](https://github.com/jewelml11/CPT167)@[e444c3df37...](https://github.com/jewelml11/CPT167/commit/e444c3df37c329baf2f8c9eab89f8229901948e6)
#### Sunday 2022-02-06 04:15:25 by jewelml11

My latest project for CPT 167 JewelProgram5.java

VVV Had to solve the below problem VVV
Program 5 – Summerville Sea World, improved
PROGRAM DESCRIPTION
Well, the new Summerville SeaWorld™ folks liked what you did last time, but as happens with most customers, they decided they wanted a little more functionality.  The basic functionality is still there.  From last week, here is what they wanted.
Your program will need to control, manage, and track all the ticket sales.  There are going to be three categories of tickets to track:  free admission, juniors, and adults.  Toddlers five and under will be allowed in for free; but of course, we still need to track those, since there are limited seats for each show.  Juniors, those between the ages of 6 and 16, will be charged $7.50 per ticket; and anyone over 16 will be charged the adult price of $11.50 per ticket.
As mentioned above, they want a little more functionality.  First, they want to limit the number of tickets.  The arena seats 430 people.  They want the main loop to exit if the number of tickets sold reaches that limit.  If the last ticket purchase exceeds this number, just accept the purchase.  The staff will keep nine folding chairs available in case the arena is slightly over booked.  That is, if 425 tickets are sold and the next customer wants 7 tickets, just sell all seven tickets.  The total tickets sold will be 432, but that is allowed.
The new manager of Summerville Sea World is a numbers guy.  He is considering offering a 10% group discount for ticket purchase of 5 or more of the same type of ticket.  However, he isn’t sure just how much that might cost the company.  He wants a trial run to show how many tickets were purchased in a group of five or more for each ticket type.  In the final report, he would like additional information showing how much a 10% discount for those tickets would actually cost the company.
SPECIFIC DIRECTIONS
This week, we are studying methods, so of course you should make methods part of this program.  Here are the required methods:
    • displayWelcome – a void method just welcoming the user
    • getValidatedTicketSelection – returns an uppercase character representing the user’s selection.  It will only return a valid selection.  This means that if the user enters an invalid selection they will be prompted for another selection until a valid selection is made.
    • getTicketSelection – displays the menu to the user; returns an unvalidated character typed in by the user.  Note, the selections presented to the user will be stored as static final variables in the main class.  They do not need to be passed to the method.  Remember that just as before, this menu needs the option to Quit.
    • getValidatedTicketCount – prompts the user for how many tickets they desire to purchase and returns an integer entered by the user; the integer is guaranteed to be greater than zero and no more than 10.  Unlike in our previous program, if the user enters an invalid number you should inform them of the error and prompt for a new number until a valid number is entered.
    • displaySinglePurchase – displays the type of ticket they are buying, the number they are buying, and the cost for the ticket(s).  This method should be passed the ticket type, the number being purchased and the total cost.
    • displayFinalReport – as before, it will display
        ◦ the total number of purchases
        ◦ total numbers of each ticket type (toddler, junior, and adult) sold, individually
        ◦ total dollar sales for each ticket type
        ◦ total number of tickets sold overall
        ◦ total dollar sales for all tickets
In addition, it will display
    • the number of potential discounted tickets for each ticket type
    • the discount for each ticket type; that is, 10 percent of the price for the discounted tickets
    • the cost to the company; that is, the sum of the discounts
As before, when the program starts up, just provide a welcome, present your menu, and then start asking for ticket sales.  From main, you should simply call the displayWelcome and getValidatedTicketSelection methods.
When entering the while-loop, you will need to check that the employee has not entered ‘Q’.  You will also need to check that there are still seats left.  This is best done in a Boolean expression in the while-condition.  Any other approach complicates the code.
As before, each time through the loop, you should only sell one type of ticket:  toddler, junior, or adult.  To determine how many tickets the customer wants, your program should call getValidatedTicketCount. 
As before, you will be accumulating appropriate totals for the end of the program, so make sure your program takes care of those needs inside your loop also.  You should also keep track of the number of purchases.  So, if a customer wants 10 junior tickets, it is only one purchase.  You will need a counter to keep track of purchases.
Because of the new statistics, you should also capture the number of tickets sold for each ticket type when the type is five or more.  This means that you will need to have three variables, one for each ticket-type.  (Technically, only two variables are needed since the toddler tickets are free; however, if the company decides to start charging for the toddler tickets, and your code is well written, you will only need to modify the price of the toddler ticket.)
For each individual ticket sale call the displaySinglePurchase method.  Note: this method should be called only once in your loop.  It should not be called inside the selection structure.  Design your code so that you can make the call near the end of the while-loop.
At the very end of the loop, call the getValidateTicketSelection method again to update your LCV.
Once the operator decides to select quit, or all of the tickets have been sold, display the final report.
As before, your final results must be laid out in a business-like report with headings, etc.  
TURN IN:  a data dictionary for this program, a complete flowchart, and the zipped Eclipse project.  Submit everything into D2L.  Note that from now on, you will need to include a Data Dictionary; IPO charts are no longer accepted.
Important Note:  Until now, our programs have been fairly simple.  Now that you have been introduced to while-loops, our programs become more interesting, and more difficult.  If it occurs to you to try to write this program without planning it all out, then you are seriously missing the point of this class.  There are quite a few details that you are unlikely to get right without thinking them all through and planning them out very carefully.  You don’t necessarily have to finish a perfect flowchart before coding, but you had better draw some semblance of a plan first, and use it to figure out when each requirement has to appear and be taken care of!!
SAMPLE MENU
Ticket Menu
T) Toddler  0.00
J) Junior   7.50
A) Adult   11.50
Please select your ticket type:
SAMPLE FINAL REPORT
PORPOISE TICKET SALES REPORT
Total Purchases: 64
Tickets Purchased:
Type     Sold     Value
Toddler    27      0.00
Junior    129    967.50
Adult     152   1748.00
=======================
Total     308   2715.50

Discount Statistics
Ticket     Discount    Potential
Type       Eligible     Discount
Toddler          18         0.00
Junior           39        29.25
Adult            12        13.80
=============================
Total Discount   69        43.05

---
## [olstinker/cart263](https://github.com/olstinker/cart263)@[773b54b65f...](https://github.com/olstinker/cart263/commit/773b54b65f9050ff00a3d7ba9b9fe704a780cb7c)
#### Sunday 2022-02-06 04:54:34 by olstinker

Added some wacky images because for some reason I was getting errors when trying to reference local assets?

- So I had to do some very rudimentary p5 drawing, and link to gifs online lol

Just FYI I had some issues during this exercise and therefore wasn't able to make it as fleshed out as I would have liked.

I had a lot of trouble referencing specific objects in different JSON files, even though following along with Pippin's structure seems very straightforward.

For example:
https://github.com/dariusk/corpora/blob/master/data/humans/richpeople.json

I wasn't able to reference the "name" object properly and I'm not sure what I was doing wrong. I'd figure it would be something like "object.richPeople[0].name" but that didn't work. So I must be doing something wrong!  I ran into similar issues with other JSON files that had very different formats which was frustrating (mostly because I had a concept that I thought would be fun--to make the user some kind of horrible corporate assassin).

Also, for some reason when I loaded assets (JSON or images), I would get an error in the console when one of the assets was a link to an online source and one was stored in my local assets folder. Not sure why this was an issue!

Anywho, thanks for your time and for the extension!

---
## [Hook7733/Hook7733](https://github.com/Hook7733/Hook7733)@[f84047b90c...](https://github.com/Hook7733/Hook7733/commit/f84047b90cf075c5ec1e9a85451eeb3bd325585f)
#### Sunday 2022-02-06 06:36:18 by Hook7733

Update README.md

https://youtube.com/channel/UCYvxbcMeGi7zGQxnOEVIGJw follower like, and subscribe, im a spiritual rapper who speak positive mystical words of glory, and have desire  to create a nonprofit organization from the disabled do to me losing my hole left arm which was amputated  from drugs  it took the pain of hardship subsequently my own mistake  brought  this pain  establishing change cresting a new heart mind body and soul

---
## [benbot16/Shiptest](https://github.com/benbot16/Shiptest)@[031c0866ed...](https://github.com/benbot16/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Sunday 2022-02-06 06:59:18 by SweetBlueSylveon

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
## [geky/equeue-rust](https://github.com/geky/equeue-rust)@[60e5ade1bc...](https://github.com/geky/equeue-rust/commit/60e5ade1bc0dc82207d5d46d161878ddacd61f90)
#### Sunday 2022-02-06 07:07:53 by Christopher Haster

Refactored wait_async implementations a bit, and fixed multi-consumer issues

This is a perfect example of feature creep.

Equeue is intended to provide a synchronization facility for asynchronous
code (either threads or interrupts depending on your system). So you would
expect Equeue to be marked as Send+Sync, marker traits in Rust which indicate
your type is thread-safe.

This is all fine and good, except in Rust, Send+Sync only applies to
whole objects, not individual functions. This means if Equeue is marked
as Send+Sync, _all_ methods must be synchronized. Originally intended
as a multi-producer, single-consumer sort of system, this raises the
question, what happens if you call dispatch from multiple threads?

Fortunately, due to the synchronization required between producers
and consumers, synchronizing dispatch actually comes for free. And with
a bit of tweaking it can actually be well behaved, distributing events
across whichever threads are dispatching. Well, originally the first thread
that arrived would get all ready events, potentially starving other
consumers, but it was just a bit of tweaking which also helped simplify
the code (deduplicated cancel and unqueue).

So here we are, with the _possibility_ that a user calls dispatch from
multiple threads, and Equeue potentially distributing events across
threads evenly. Except this suddenly changes the expected behavior and
implementation of the underlying semaphore. Originally it was a simple
binary semaphore, implementable with an atomic bool that was cleared
by which ever thread woke up. But we need to wake up _every_ thread,
otherwise only on thread will do all the work.

For systems with multi-cores, this means that the underlying semaphore
implementation should use some primitive, such as a conditional
semaphore, in order to wake up all events. Annoyingly, this is more
complicated, and potentially tricky to get right.

All for a library that is most likely used only single-core systems.

Fortunately, those can use the original binary semaphore, and ignore
the unreasonable possiblity of the multiple dispatches on multiple
threads. They would only end up starving each other anyways.

---
## [SuperiorOS-Violet/android_packages_apps_Launcher3](https://github.com/SuperiorOS-Violet/android_packages_apps_Launcher3)@[f80ec203e2...](https://github.com/SuperiorOS-Violet/android_packages_apps_Launcher3/commit/f80ec203e2684bcab3577d11a2d88cc5ee22af7d)
#### Sunday 2022-02-06 09:01:48 by Alex Cruz

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
## [ow0x/aikaterna-cogs](https://github.com/ow0x/aikaterna-cogs)@[1dc7d9272a...](https://github.com/ow0x/aikaterna-cogs/commit/1dc7d9272a2de0310da069f2083e5f82fe8efb07)
#### Sunday 2022-02-06 09:25:37 by ow0x

whether it's kato stealing others code without...

credits or fetching user bios against terms of service or just logging end user data en masse like a sheep, or draper asking others to participate in witch hunting to join a user's server who submitted shitty PR#4752 last year or to join dpy server to hunt down which bot is tracking user avatars without consent and shit and create drama there (which forced danny to intervene) but not say a word when poor historian is doing the same thing ORRR just start mudslinging drama in #advanced-coding. thank fuck karma gets to these saints much later if not sooner.

---
## [realmercy/esmBot-legacy](https://github.com/realmercy/esmBot-legacy)@[cffac57671...](https://github.com/realmercy/esmBot-legacy/commit/cffac57671a5ba9749ada21d6704032e9028298f)
#### Sunday 2022-02-06 09:55:25 by realmercy

Revert "fuck you"

This reverts commit d5bad253081420273d1138f4b348b0c69984f23f.

---
## [damerell/crawl](https://github.com/damerell/crawl)@[93842f7414...](https://github.com/damerell/crawl/commit/93842f7414b4e84b795e7a4a26d75f695b99acde)
#### Sunday 2022-02-06 10:42:05 by Floodkiller

Remove old malmutate

We all hate it so we're taking a leaf out of Gooncrawl's book.

Partially remove monster Malmutate

Removes Malmutate from nequxecs and cacodemons, the two most common
malmutaters (thanks to the overuse of demons throughout Extended and
summoners).

Nequoxecs get Paralyze, to match their 'mind flayer' theme. This should be
a threat at lower levels, but easily resisted by late-game characters (a
single pip of MR reduces success rate to 35%, two pips to 10%, etc.).

Cacodemons get Entropic Weave, to synergize with their digging and adding
to their 'disrupt the player from bigger threats' toolset.

This should reduce Malmutate enough to test to see if it needs to be
changed/removed from orbs of fire/shining eyes (as well as if Mnoleg needs
malmutate on hit removed).

(cherry picked from commit 15298a4ded55fc89561f5a8eb9934c3134e019ac)

Change Malmutate spell effect

From mutating the player to deteriorating all the players stats by
1+(1d4, average of 2 rolls). This will only affect Orbs of Fire as they
are the only monster left that has the Malmutate spell and I'm too lazy
to change the name in the source code for everything. This only affects
the spell version of Malmutate, not any other version that may exist
(i.e. Mnoleg melee, spell miscasts, etc).

Also left a note for myself to look into at some point.

(cherry picked from commit a2afb6c259e3b450e53f4dd65fb524583356f8c3)

Tone done new Malmutate

Waaaaaay too rough, oops

(cherry picked from commit 0d295a6d73b7014d2814741962ae627de7b1b361)

Give shining eyes Polymorph instead of Malmutate

Fits the theme of slimes and form changing while getting rid of the
Malmutate devil. Also upped the spellpower per HD of Polymorph for
monster casting, which hopefully shouldn't matter as only shining eyes
can cast it normally. Might need to tweak down the modifier a bit if it
is too extreme, but wanted to make sure they were still a threat.

(cherry picked from commit 3c9b759b45d4f420ddbd22d0fa63e83be52bfce9)

---
## [RemcoDEV/maui](https://github.com/RemcoDEV/maui)@[ac6befcbee...](https://github.com/RemcoDEV/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Sunday 2022-02-06 10:59:07 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [urbanstylehomes/pico_ducky_rickroll](https://github.com/urbanstylehomes/pico_ducky_rickroll)@[669ef39956...](https://github.com/urbanstylehomes/pico_ducky_rickroll/commit/669ef39956d5d33e27deb585dc071c405f439e5f)
#### Sunday 2022-02-06 11:02:55 by urbanstylehomes

M3M Capital Grugaon

<a href="https://www.getluxuryhomes.com">Get luxury Homes</a> 
Luxury living in Gurgaon
 
 The economy is steadily growing and so is the lifestyle of people.
The increasing demand from people means luxurious apartments as well as investment options. 
Location is one of the prime components that qualifies an apartment as luxurious, and when we talk about the location,  get luxury homes will help you find  residential hubs with a choice of ready-to-move-in luxury apartments. Gurgaon is also called the Millennium City by many, owing to the rapid pace of development that the region witnessed at the start of the millennium, considered a profitable investment by one and all. Get luxury homeswill offer you multiple options to choose from keeping the neighborhood which offers safety, security and convenience as the prime objective.
Connectivity is keytowards every business and entertainment center of Gurugram.The city limits are rapidly developing and the connectivity network of transportation is growing in concurrence.Independent Floors at DLF Gardencity are ideal for corporate honchos and their families to make it their abode.
DLF has nearly 70 years of track record of sustained growth, get luxury homes has credit to establish a few of the most astonishing projects in the millennium city of Gurgaon. DLF India has launched numerous ultra-luxury apartments in Gurgaon and developed international standard of luxury living. Get luxury homes in townships comprising of luxury villas, executive floors, and plots in Gurgaon. We are presenting independent floors at DLF Gardencity, Gurugram. DLF Garden City, Independent Low Rise Low-Density Floors, Project by DLF India Limited, Sector 92, Gurgaon. Besides offering an abundance of nature's delights, DLF Gardencity is located in close proximity to well-planned social and physical infrastructure, including business districts, hotels, schools, hospitals, multiplexes, clubs, golf courses, and a variety of other leisure and retail options. DLF India Limited is the undisputed leader in the Indian real estate market.
Total Units Approx. => 148
Plot Sizes (Sq. Yd.) => 218, 250, 270, 300 & 330 Sq Yd
Typology & Configuration => 3 & 4 BHK + Servant/Store Room
Total Height => Basement + Stilt + 4 Independent Low Rise Floors
Total Parking => 2 Parkings Each Floor
Built-Up Area => Approx. 1800 Sq. Ft. – 2350 Sq. Ft.
Expected Price Range => Approx. INR 1.10 Crore – INR 1.65 Crore
Payment Plan => 25%-75%
Expected Possession => 2.5 Years


 The Garden City is located in Sector 91/ 92, Gurgaon. Cyber City is located just 15 minutes away from the DLF Garden City.
Corporate Greens is also located just 5 minutes away from the project. Indira Gandhi International Airport is located just 25 minutes away from the DLF Garden City.
Booking Amount => INR 5.00 Lakhs 
Social infrastructure, like schools, parks, and banks, surrounds the Sector 92 area. It is also very well-connected to various parts of the city by public transport network.
With 1000 acres of green surroundings, the residents of Garden City will lead a healthy life and breathe in the fresh air. Make DLF Garden City Floors in Gurgaon your home in green heaven where you will have the opportunity to live in a pure environment.

---
## [newstools/2022-sabc-news-online](https://github.com/newstools/2022-sabc-news-online)@[b832c43a03...](https://github.com/newstools/2022-sabc-news-online/commit/b832c43a036d8091ee68b665159167dac4fd9bb6)
#### Sunday 2022-02-06 15:14:39 by Billy Einkamerer

Created Text For URL [www.sabcnews.com/sabcnews/a-man-sentenced-life-imprisonment-for-raping-his-then-girlfriend/]

---
## [lidatong/agnostic-orderbook](https://github.com/lidatong/agnostic-orderbook)@[328d6c2eb8...](https://github.com/lidatong/agnostic-orderbook/commit/328d6c2eb8cd8883913316da6d3a0fb781e07613)
#### Sunday 2022-02-06 15:48:18 by Charles Li

feat: optimize critbit using serum

feat: almost compiling...

feat: holy shit it compiles

fix: size panic, warnings, get unit tests passing

chore: bump to 2021 ed, solana 1.9.4

feat: add solana-profiler for profiling compute units

chore: CLion is stupid at linting

chore: explicit BorshDeserialize because CLion is stupid, fix warnings

chore: gitignore cargo lock

perf: unsafely transmute Vec<u8> into Slab DST [u8] a la Serum

Revert "perf: unsafely transmute Vec<u8> into Slab DST [u8] a la Serum"

This reverts commit 403d9e72b76781a99140609d9d6b00422f06d576.

chore: remove todo about DST

chore: debug solana unit test issue

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b697654271...](https://github.com/mrakgr/The-Spiral-Language/commit/b6976542716aed54d64bf9b13af51fa2765edaa6)
#### Sunday 2022-02-06 17:36:20 by Marko Grdinić

"10:30am. Let me chill a bit and then I will start.

11:05am. Let me start. Let me try the polyfill idea I got in a reply. After that I'll scatter some flowers. Finally. I need to bring this overly long adventure to a close.

Hmmm, after a fuse, the add version results in less vertices in the end.

11:10am. I had the bright idea of selecting only the crisscrossing edges. I meant to then pass that into polywire in order to get a different radius for those, but it is not working. It ends up selecting the adjacent primitive as well.

Convert to line does nothing to help me.

Forget it. Let me focus on the wines.

11:25am. The flowers are going through the construction mesh. I knew this would happen. But how do I fix this? Raycast? No there isn't such a node. There is a ray node. Let me read the manual for it. If I cannot deal with this, I can just leave Houdini until lot later.

Hmmm, Ray seems to be the equivalent of shrinkwrap in Blender.

Well, let me ask next.

11:40am. I've decided. Either today or tomorrow are going to be the last days of me using Houdini. Let me try painting my own mask. I've been doing it for almost 3 weeks and I am still struggling with very basic things.

11:50am. No this is not going to work. Paining a mask like I am trying to do now is a different thing from scattering the flowers directly like I could in Blender. I could use the scatter addon and that would tell me right away where I lie.

I need to find a programmatic solution. If I have to do it by hand, I might as well throw Houdini in the trash.

https://youtu.be/4TyDLdHPhC0
Houdini | Intersection Analysis Geometry Node

11:55am. While I was dallying Blender 3.2 Alpha came out and 3.1 is in Beta.

Ok, let me think. What am I going to do about this problem?

https://www.toadstorm.com/blog/?p=493

Read random things, watch random tutorials as usual.

https://www.sidefx.com/tutorials/game-tools-calculate-occlusion/?collection=47

Let me watch this.

12:20pm. https://www.sidefx.com/tutorials/the-complete-a-z-terrain-handbook/

I gave it a try at pointing my own mask, but it is not satisfying me.

Ok, as my last thing in Houdini, let me learn a bit about heightfields and this terrain stuff. After that I'll pat myself on the back for persevering with it for so long and check out whan new features Blender has. Houdini is just too tough.

12:45pm. https://youtu.be/Qp-VjCHTrzo?t=14
Houdini: Avoid Geometry-Intersections in For-Loops (where you copy geometries to points)

Let me watch this. Oh, it seems like it is exactly what I want.

https://youtu.be/Qp-VjCHTrzo?t=325

Damn it, it is this node. I already watch a tutorial on it, but did not peg it as what I need.

1:05pm. Ok, I guess I do not need to drop Houdini just yet. With the intersection analysis node, I can just check whether it intersects the frame.

Let me stop here.

One thing I want to figure out is why the boolean union is failing me.

1:10pm. I got some good replies in that thread. I'll have to go over it. Nevermind that for now. Let me do the chores here, and after that comes breakfast.

2:45pm. Done with breakfast and chores. Let me resume. First of all, let me try the bool union. I want to wigure out why they are giving me trouble. After that I'll ask about why opening the file gives me that strange error. After that I'll get busy with figuring out how to drop those flowers on intersect.

2:50pm. Ok, I see. It seems all I had to do was add more topology. When there is too little of it, the nodes can act weird.

3pm. Did the power thing for the `@curveu`.

///

>>880516 (You)
you could check for intersections the scatter point normals and remove them before the copy:

https://www.sidefx.com/docs/houdini/vex/functions/intersect.html
https://www.sidefx.com/docs/houdini/vex/functions/removepoint.html

won't be perfect,

if you didn't already know:
variables in the vex reference that are preceeded by '&' means the function is writing to those variables, so you need to create those vars beforehand and the feed them into the function.

alternatively, create density masks from attribute transfer or mask from geometry.

or for more accurate, slower checks, you can do volumesample checks post-copy.

///

///

>>880516 (You)
Try deleting points that are close to the beams?

///

This last post had a vex node in a screenshot. It is not what I am looking for. Though it should be worth keeping in mind for later. Nevermind it for now.

https://www.sidefx.com/docs/houdini/vex/functions/removepoint.html

Hrmmm, I am going to have to learn some vex. Ok, first off, let me ask about the loading issue.

3:15pm. Posted the question. Now let me continue forward. I need to deal with intersecting flowers.

https://www.sidefx.com/docs/houdini/vex/functions/intersect.html

Hmmm, I thought this would be a geo node, but this is a vex function. Instead of outright geo intersection, it does a ray from an origin point. Hmmm, that is rough. I am not good at programming with this yet. Let me go with what I saw in the Youtube tutorial.

Let me do some factoring out.

3:55pm. Ok, I did the intersection analasys thing, though it really takes a while. Instead of copying to point, it might be better to take a bounding box.

4pm. Ok, that was one thing. What should I do next? I surely did not have in mind to do just a single type of flower. They aren't oriented correctly either.

4:05pm. Had to flip a setting in scatter and align. Now they are fine. I am surprised what a good job it did. Exactly what I wanted of it. It could easily have been the case that it did the sides wrong. Scatter and align is great.

Let me try just a single thing. I want to try replacing the whole geometry with a bounding box.

Indeed, that speeds up the Intersection Analysis node massively.

Nevermind that for now.

4:20pm. Focus me. What should I do here?

Add a bunch more curves as stalks. Put flowers on that. Then I'll be done. Also add some variation to the existing flower, right now they are all the same size. I should just turn on the pscale for that and let the scatter node deal with that automatically.

But before that, let me do some factoring. Let me factor out the pool from the island. I hate those merge nodes, they make it hard to see what is going on.

At this point, I should really start thinking about how to make use of subnets.

4:40pm. Right now I am messing with the frame again. It is really strange that selecting the criss crossing frames and using the polywire separately on that did not work for me. Just how did I mess that up? Let me do it properly this time.

5pm. I am trying to figure out how to do endpoint selection, so I can just snag the bulb to the last point properly.

Ahhh, group by range. Right. I forgot.

5:25pm. I finally figured out how to orient the last point correctly. Ok.

Let me think. What do I want to do now. Well obviously, how about I turn that into a function. Also I'd like to know how to do something like 90% leaf and 10% branch.

Let me save this thing here.

5:35pm. https://www.youtube.com/results?search_query=houdini+subnetwork

I need to focus. Let me watch some of these.

https://youtu.be/w8yBoO-qvsk
5 Ways to Organize your Network in Houdini 17.5

I guess this will do.

https://youtu.be/w8yBoO-qvsk?t=580

This is one of the issues that has bee troubling me. It never occured to me to just use an object merge.

Time for lunch. I'll finish this when I get back.

6:15pm. Done with lunch. Let me get back to the video.

6:30pm. Let me close here for the day. I do not feel like it anymore.

https://www.youtube.com/watch?v=MGxNuS_-bpo
Blender 3.1 New Geometry Nodes Tutorial

Maybe I'll watch this for a bit, but all I want to do now is much on an orange. I am done. I am going to finish the vine thing tomorrow, and move on to the pool and the props. I'll want to start by factoring out the wine functionality into subnets and figure out how to access that functionality from other objects.

I guess I won't be dumping Houdini after all. I am putting in the effort and somehow progress is coming to me, as slow as it is.

I'll finish at least one scene in it."

---
## [ajmilala/coursera-course-module4-assignment](https://github.com/ajmilala/coursera-course-module4-assignment)@[72c45e2525...](https://github.com/ajmilala/coursera-course-module4-assignment/commit/72c45e2525073ad9511f5a8c86a2e25c6e85895a)
#### Sunday 2022-02-06 18:01:39 by ibrahim inusa

README.md

Time to complete: About 30 minutes.

Ask questions in Discussions if you get stuck! We are all learning, and going through getting stuck and then unstuck (even with someone's help) can be a very valuable learning experience!

Summary: In this assignment, you are going to loop over an array of names and print out either a hello or goodbye to that name to the browser console. If the name starts with a letter j or J, you are to print out Goodbye JSomeName. If the name starts with any other letter, you are to print out Hello SomeName.

However, in order to do that printing you will have to use 2 externally provided libraries whose code is not 100% ready to be used. Using the things we've learned in this module, your job will be to fix the code in those libraries.

You will get some starter code to work with where all the steps of what you need to do are clearly spelled out for you.

Here is what you will need to do in order to complete the assignment:

    (If you haven't already) Create a GitHub.com account and a repository that you will use for this class.

    (If you haven't already) Follow the Development Setup Video (beginning of Module 1) instructions on how to create a repository and set it up such that you can host and view your finished web pages on GitHub Pages, i.e., GitHub.io domain name. You will need to provide that URL for your peer review.

    Create a folder in your repository that will serve as a container folder for your solution to this assignment. You can call it whatever you want. For example, module4-solution or mod4_solution, etc.

    You will need to download the starter files for this project and copy them into your solution container folder (e.g., into module4-solution). Since assignments and starter code get updated from time to time, don't assume that you have the latest version already on your system. The best way to ensure that you are working with the very latest starter code is either git clone the fullstack-course4 repository into a new directory OR, if you've already done 'git clone' previously, you can simply open up your command prompt (cmd on Windows or Terminal on Mac), navigate to the folder where the fullstack-course4 repository was previously cloned into and do: git pull.

    This will update your local copy of the repository with whatever changes have been made since the last update.

    As a reminder, the full repository URL is: https://github.com/jhu-ep-coursera/fullstack-course4

    Once the local repository on your system is up to date, YOU HAVE A CHOICE! If you want a slightly more challenging assignment, use the code in the "harder" folder as your starting point. If you want a slightly less challenging assignment, use the code in the "easier" folder as your starting point. The difference between the two starting points is that in the "easier" starting point, there are a few steps that are already completed for you.

    Harder: If you want a slightly more challenging assignment, copy all the contents of the fullstack-course4/assignments/assignment4/assignment4-solution-starter/harder folder into your newly created solutions container folder for this assignment, e.g., 'module4-solution'.

    Easier: If you want a slightly less challenging assignment, copy all the contents of the fullstack-course4/assignments/assignment4/assignment4-solution-starter/easier folder into your newly created solutions container folder for this assignment, e.g., 'module4-solution'.

    NOTE: the provided starter code will not run. It is up to you to follow the instructions to get it to run. Once you've copied the starter code of your choice into your solution folder, open up your solution folder in the code editor. Open up script.js file and follow the steps.

    When you are continuously working on the assignment, use Browser Sync and keep Chrome open to the Console tab of the Chrome Developer Tools. You will likely see errors there to start with. Follow the steps outlined in the starter code and those errors should go away by the time you finish the last step. If you still see errors at that point or you are not seeing the output you're supposed to see, you probably made a mistake somewhere, so look into that and investigate.

    Remember, if you are stuck, ask questions on the course Discussion forum.

    That's it!

---
## [ajmilala/-coursera-course-module5-assignment-](https://github.com/ajmilala/-coursera-course-module5-assignment-)@[f1b2c338fd...](https://github.com/ajmilala/-coursera-course-module5-assignment-/commit/f1b2c338fdccff075bb2934ac19b6e4eb17153fa)
#### Sunday 2022-02-06 18:34:16 by ibrahim inusa

READMED.md

Time to complete: About 30 minutes.

Ask questions in Discussions if you get stuck! We are all learning, and going through getting stuck and then unstuck (even with someone's help) can be a very valuable learning experience!

Summary: In this assignment, we are going to have a bit of fun with our built restaurant web application. The front page of our web app contains 3 clickable tiles: Menu, Specials, and Map. If you click on the Specials tile, you will be taken to a single category page where all the menu items that belong to the Specials menu category will be shown. Your task in this assignment is to alter this behavior such that when the user clicks on the Specials tile, the web app takes the user to a random single category menu page, listing menu items in the category, be it "Lunch", "Dinner", "Sushi", etc. That way, any random category can become the Specials! What fun! (not! :-) )

In order to accomplish this, we need to change the home HTML snippet and, besides pulling it dynamically from the server, also insert a random category short_name into the function call of the following code. Previously, the code to send the user to the "Specials" category was this:

<a href="#" onclick="$dc.loadMenuItems('SP');">

For this assignment, we changed this line to prepare it for a random category short_name to be this:

<a href="#" onclick="$dc.loadMenuItems({{randomCategoryShortName}});">

Here is what you will need to complete the assignment:

    (If you haven't already) Create a GitHub.com account and a repository that you will use for this class.

    (If you haven't already) Follow the Development Setup Video (beginning of Module 1) instructions on how to create a repository and set it up such that you can host and view your finished web pages on GitHub Pages, i.e., GitHub.io domain name. You will need to provide that URL for your peer review.

    Create a folder in your repository that will serve as a container folder for your solution to this assignment. You can call it whatever you want. For example, module5-solution or mod5_solution, etc.

    You will need to download the starter files for this project and copy them into your solution container folder (e.g., into 'module5-solution'). Since assignments and starter code get updated from time to time, don't assume that you have the latest version already on your system. The best way to ensure that you are working with the very latest starter code is either 'git clone' the fullstack-course4 repository into a new directory OR, if you've already done 'git clone' previously, you can simply open up your command prompt (cmd on Windows or Terminal on Mac), navigate to the folder where the fullstack-course4 repository was previously cloned into and do: git pull

    This will update your local repository with whatever changes have been made since the last update.

    As a reminder, the full repository URL is: https://github.com/jhu-ep-coursera/fullstack-course4

    Once you update your repository, copy all the contents of the fullstack-course4/assignments/assignment5/assignment5-solution-starter folder into your newly created solutions container folder for this assignment, e.g., module5-solution.

    Once that's done, you are ready to start coding the solution.

    NOTE: the provided code will not run. It is up to you to follow the instructions to get it to run.

    You are NOT allowed to change the home-snippet.html file. Any adjustments to the value of randomCategoryShortName property needs to be done in Javascript code.

    There are 4-5 fairly simple steps to implement the required functionality.

    Open up js/script.js file.
    Find TODO: STEP 0, and follow the instructions until you are done with TODO: STEP 4.

    If you've watched the lectures, the code should be very familiar to you.

    Once you are done, verify that the desired functionality is working correctly. Use Browser Sync or deploy your solution to GitHub pages.

    Load the home page in the browser.
    Click on the Specials tile. A single page category with a list of menu items for some category should appear.
    Click on the restaurant logo to go back to the home page.
    Click on the Specials tile again. Most likely, a different single page category page will be shown.

    Repeat this several times to make sure that most of the time you see a different single category page.

    That's it!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b48cda6afa...](https://github.com/tgstation/tgstation/commit/b48cda6afa047be95390dc1360e8d899ec6394b0)
#### Sunday 2022-02-06 19:32:15 by LemonInTheDark

Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

* Please stop typecasting target, noooooooooooooooooo

* Fixes harddels in pinned module code

The logic for pinned modules was intentionally hanging references to the
mob that pinned the action button. I have depression.

The pinned_to list also was never fully cleared, but that would have
just exasperated the issue. I've converted its use of mobs to refs, and
its use of the module var into something better managed

(Friendly reminder that actions will persist in your nightmares forever
unless they are manually qdel'd, this code wasn't doing that.

Also cleaned up how the pinned_to list is managed, hopefully it's a bit
more action centered now

---
## [mosra/corrade](https://github.com/mosra/corrade)@[09ae21d470...](https://github.com/mosra/corrade/commit/09ae21d4700a50cfc97f0de4144a73cf0db3c5f9)
#### Sunday 2022-02-06 19:59:33 by Vladimír Vondruš

Add CORRADE_MSVC2022_COMPATIBILITY as well.

Sorry that I was optimistic! That I thought I'd only handle the cases
where /permissive- makes a difference and everyhting will be sunshine
and butterflies again! HAHA LOL NO.

If it would just misparse something or have trouble matching some
template, I'd sigh and accept that as a quirk that won't just go away.
But the damn thing crashes! The same way it crashed two years ago! And
four years ago! FFS!

---
## [AospExtended-Devices/kernel_oneplus_sm8150](https://github.com/AospExtended-Devices/kernel_oneplus_sm8150)@[e7fe64241e...](https://github.com/AospExtended-Devices/kernel_oneplus_sm8150/commit/e7fe64241eae3a01b0f38521537cfbc1e4747db6)
#### Sunday 2022-02-06 20:30:50 by alk3pInjection

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
## [CameronWoof/tgstation](https://github.com/CameronWoof/tgstation)@[413fd90502...](https://github.com/CameronWoof/tgstation/commit/413fd9050271829e2899b88a676995ae2517111c)
#### Sunday 2022-02-06 20:33:56 by GoldenAlpharex

Dullahan Partial Refactor: They Work Again Edition (#63696)

So, a few months ago I was like "hmm there's something weird going on with party pods...", which got me looking into important_recursive_hearers or something like that. I spoke about it in the coding channel and Kyler actually fixed it before I did. But I also caught a similar glitch with Dullahans, so I decided to investigate...

Two months later...

I present to you a partial unfuckening of the Dullahans, in that I made them fully functional once again:

They only hear speech through their head (not sounds, sadly, someone else would have to tell me how to do that because I otherwise really wouldn't know how to do it in a sane way), they speak through their head, runechat-included.
When you spawn a Dullahan, you're set to look through the Dullahan's eyes (so from their head), and that doesn't reset when you log off and back in, or admin-ghost and come back in your body.
When you're looking through your head, your view will no longer be reset to your body upon entering a locker, which is nice to avoid not being blind while looking through your body.
Dullahan heads no longer look completely lifeless and without organs. They have eyes that don't look dead and that even match the player's intended eye color.
Dullahan can now properly examine things from their head, which was intended and 100% not functional.
Dullahan heads now speak with the proper name of their owner, instead of having a random name attached to it at round-start.
Dullahan heads are also now properly named too.
Dullahans can now properly whisper, sing and do all these funny things that they were unable to do before.
Dullahan whispers will now properly respect the range of the whisper.
Dullahans can now succumb in hardcrit by whispering, as intended. This potentially fixes other species that worked similarly not being able to succumb, like abductors, although I didn't test if they normally could, I just know they absolutely will be able to now.
When switching from Dullahans to a different species, your old head will no longer stay behind.
I also added a proc for species to do some code when we get a ckey login in our mob, which could potentially be useful for other stuff in the future, but it was necessary here as the view is reliant on the client, which we want to ensure doesn't get weird view glitches like having their head's vision overlay while actually being centered on their body.

I also made it so say() now takes a range argument, which is 7 by default, just so things that aren't humans can also whisper and do all those kinds of things. Going with that, there's probably a few more things that will be able to be done better thanks to this, although I haven't tested every edge case with this, but I doubt it will make much of a difference in the future.

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[15e72c8d35...](https://github.com/Zeodexic/tsorcRevamp/commit/15e72c8d3551c84dc14e8444b9d8e0960b6ce758)
#### Sunday 2022-02-06 21:32:51 by timhjersted

Added Ancient Oolacile Demon boss and more

Added new (early-game) Ancient Oolacile Demon event with 3 main attack phases (will likely do another round of balancing after feedback)
Polished Basilisk Shifter and Hunter
Gave Hero of Lumelia some more sounds
Artorias drops his ring again, which now grants immunity to powerful curse buildup and freezing
Fixed Red Knights sometimes not shooting its spear after getting hit and gave it an ominous sound
Tweaked spawns for dunlendings, hollow warriors, tibian valkyries, and undead casters (generally to not spawn in crimson)
Gave Great Red Knight some more new attacks (still could use some more polish)
Changed dust effect for dark inferno debuff
EnemyCursedBreath doesn't collide with tiles now
EnemySpellGreatFireballBall has a ton of potential sounds with notes for projectiles
JungleWyvernFire debuffs are less harsh if Skeletron hasn't been defeated (used for new boss)
Changed more projectile sounds

---
## [learnmonkey/learnmonkey.github.io](https://github.com/learnmonkey/learnmonkey.github.io)@[14792cae65...](https://github.com/learnmonkey/learnmonkey.github.io/commit/14792cae65065ff0ad95392297565db6b84863d6)
#### Sunday 2022-02-06 22:09:18 by Danny Wang (ThePeeps191)

Merge pull request #26 from ThePeeps191/main

fuck you @calgary34

---
## [jpfraneto/rudraky](https://github.com/jpfraneto/rudraky)@[ccc78837ee...](https://github.com/jpfraneto/rudraky/commit/ccc78837ee39a885fe674941e955436b5ff543c6)
#### Sunday 2022-02-06 22:18:52 by jpfraneto

Dia 16. I started weird today because Im at my parents house and it is after lunch, but then I got into the flow and started doing things that needed to be done. Now the whole functionality for the kriya is working great, I feel like I could do a class tomorrow with this app working as it is. That makes me proud. What I really need to work on and make better is the way that the design looks, and that is something that has always been part of what I need to work on. I devote too much time to making it work properly in the functional part, but the design part is as important because if it is catchy people will tend to use it. There is a lot of work to be done in this aspect, and I think that as I create stuff with which people interact with, Ill get better at this part of the creation of apps. It is amazing how it is always a blank canvas, and this is what I face when I do this kind of work. The open void of endless posibilities. Thats where I learn!

---
## [dubitabley/weekendgame](https://github.com/dubitabley/weekendgame)@[aede9cdb30...](https://github.com/dubitabley/weekendgame/commit/aede9cdb3086296dc4faef23dee02e5194a90662)
#### Sunday 2022-02-06 22:21:59 by dubitable

Had the most painful experience of my life.

Why oh why are svgs so awkward to work with on the web.

---
## [denzkie18/FNovels-Version-2](https://github.com/denzkie18/FNovels-Version-2)@[bfc9ff8ed6...](https://github.com/denzkie18/FNovels-Version-2/commit/bfc9ff8ed638b349fd6d42f7417872629790f6df)
#### Sunday 2022-02-06 22:23:29 by denzkie18

Update My-Girlfriend-Cheated-on-Me-With-a-Senior-so-Im-Cheating-on-Her-With-His-Girlfriend-LN.html

---
## [vercel/next.js](https://github.com/vercel/next.js)@[91146b23a2...](https://github.com/vercel/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Sunday 2022-02-06 22:51:02 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [lolipuru/crystalized](https://github.com/lolipuru/crystalized)@[d020797786...](https://github.com/lolipuru/crystalized/commit/d02079778681348e4ea35835e0647fd9e7a639e0)
#### Sunday 2022-02-06 22:54:49 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

---

