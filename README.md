## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-23](docs/good-messages/2021/2021-12-23.md)


1,570,211 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,570,211 were push events containing 2,330,813 commit messages that amount to 176,361,705 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 47 messages:


## [DirectProject/nhin-d](https://github.com/DirectProject/nhin-d)@[24a76ec595...](https://github.com/DirectProject/nhin-d/commit/24a76ec595ae7f887423bb0f33db7d049c743c8b)
#### Thursday 2021-12-23 00:04:02 by Joseph Shook

Wip .NET Core upgrade

MdnMonitor compiling and passing tests.  Using Common.Logging.Framework, finally getting away from diagnostics.nlog static creation an that custom ioc.  It is a painful and slow process.  I don't like that MdnMonitor has a dependency on config.store but that is another day.  Kind of thinking of using Steeltoe so that is creeping in some.  Might use it's discovery and, ... maybe MdnMonitor can write to RabbitMQ or Kafka as a way to schedule timeout checks.  Not sure if Steeltoe is staying up with the times.  This is all because I am comparing this MdnMonitor to the one in the Java RI Micro-Service implementation using Spring Boot.

Other misc refactoring.  Eventually I can get the branch in shape breaking dependencies and moving from the old SmtpAgentConfig.Xml injection in favor of the standard ASP.NET DI and appsettings.json technique.  I have written some ugly code putting up with XML deserialization.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[03267085b8...](https://github.com/Buildstarted/linksfordevs/commit/03267085b8f93dcffe6f638e4bc7e870a1e35efa)
#### Thursday 2021-12-23 00:06:31 by Ben Dornis

Updating: 12/23/2021 12:00:00 AM

 1. Added: How IPFS is broken
    (https://fiatjaf.com/d5031e5b.html)
 2. Added: The Case Against Work-Life Balance: Owning Your Future
    (https://shyamsankar.com/the-case-against-work-life-balance-owning-your-future)
 3. Added: The Tragedy of Safari – Magic Lasso Adblock
    (https://www.magiclasso.co/insights/tragedy-of-safari/)
 4. Added: The Asymmetry of Open Source - Matt Holt
    (https://matt.life/writing/the-asymmetry-of-open-source)
 5. Added: Dear Self; We Need To Talk About Social Media
    (https://acesounderglass.com/2021/12/04/dear-self-we-need-to-talk-about-social-media/)
 6. Added: Cloud Security Breaches and Vulnerabilities: 2021 in Review
    (https://blog.christophetd.fr/cloud-security-breaches-and-vulnerabilities-2021-in-review/)
 7. Added: Diablo IV Quarterly Update—December 2021
    (https://news.blizzard.com/en-us/diablo4/23746639/diablo-iv-quarterly-update-december-2021)

Generation took: 00:06:20.0949562

---
## [mhansonp/geode](https://github.com/mhansonp/geode)@[68b9080e84...](https://github.com/mhansonp/geode/commit/68b9080e84054f059b8c3e9b4aff9034fb302353)
#### Thursday 2021-12-23 00:09:07 by Dale Emery

GEODE-9872: Make test framework code assign ports (#7176)

* GEODE-9872: Make test framework code assign ports

PROBLEM

`DistTXPersistentDebugDUnitTest ` failed in CI because it accidentally
connected to a locator from another test
(`ClusterConfigLocatorRestartDUnitTest`).

CAUSE

`ClusterConfigLocatorRestartDUnitTest` attempts to restart a
locator on a port in the ephemeral port range.

Here is the sequence of events:
1. `ClusterConfigLocatorRestartDUnitTest ` started a locator on an
   ephemeral port. In this CI run it got port 37877.
2. `ClusterConfigLocatorRestartDUnitTest` stopped the locator on port
   37877.
3. `DistTXPersistentDebugDUnitTest` started a locator on an ephemeral
   port. In this CI run it got 37877.
4. `ClusterConfigLocatorRestartDUnitTest ` attempted to restart the
   locator on port 37877. That port was already in use in
   `DistTXPersistentDebugDUnitTest`'s locator, and as a result the two
   tests became entangled.

CONTRIBUTING FACTORS

`DistTXPersistentDebugDUnitTest` uses `DUnitLauncher` to start its
locator. By default, `DUnitLauncher` starts its locator on an ephemeral
port.

`ClusterConfigLocatorRestartDUnitTest` uses `ClusterStartupRule` to
start several locators. By default, `ClusterStartupRule` starts each
locator on an ephemeral port.

SOLUTION

Change `DUnitLauncher` and `ClusterStartupRule` to assign locator ports
via `AvailablePortHelper` if the test does not specify a particular
port.

I considered changing only `ClusterConfigLogatorRestartDUnitTest` to
assign the port that it intends to reuse. But:
- That would fix only this one test, though an unknown number of tests
  similarly attempt to reuse ports assigned by framework code. Numerous
  of those tests have already been changed to assign ports explicitly,
  but an unknown number remain.
- It is quite reasonable for this test and others to assume that, if the
  test framework assigns a port on the test's behalf, then the test will
  enjoy exclusive use of that port for the entire life of the test. I
  think the key problem is not that tests make this assumption, but that
  the framework code violates it.

Changing the test framework classes that tacitly assign ports
(`DUnitLauncher` and `ClusterStartupRule`) makes them behave in a way
that tests expect.

* Add new port var to dunit sanctioned serializables

---
## [dotnet/maui](https://github.com/dotnet/maui)@[ac6befcbee...](https://github.com/dotnet/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Thursday 2021-12-23 00:11:28 by Jonathan Peppers

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
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[d005d76f0b...](https://github.com/timothymtorres/tgstation/commit/d005d76f0bd201060b6ee515678a4b6950d9f0eb)
#### Thursday 2021-12-23 00:43:24 by Kylerace

Fixes Massive Radio Overtime, Implements a Spatial Grid System for Faster Searching Over Areas (#61422)

a month or two ago i realized that on master the reason why get_hearers_in_view() overtimes so much (ie one of our highest overtiming procs at highpop) is because when you transmit a radio signal over the common channel, it can take ~20 MILLISECONDS, which isnt good when 1. player verbs and commands usually execute after SendMaps processes for that tick, meaning they can execute AFTER the tick was supposed to start if master is overloaded and theres a lot of maptick 2. each of our server ticks are only 50 ms, so i started on optimizing this.

the main optimization was SSspatial_grid which allows searching through 15x15 spatial_grid_cell datums (one set for each z level) far faster than iterating over movables in view() to look for what you want. now all hearing sensitive movables in the 5x5 areas associated with each spatial_grid_cell datum are stored in the datum (so are client mobs). when you search for one of the stored "types" (hearable or client mob) in a radius around a center, it just needs to

    iterate over the cell datums in range
    add the content type you want from the datums to a list
    subtract contents that arent in range, then contents not in line of sight
    return the list

from benchmarks, this makes short range searches like what is used with radio code (it goes over every radio connected to a radio channel that can hear the signal then calls get_hearers_in_view() to search in the radios canhear_range which is at most 3) about 3-10 times faster depending on workload. the line of sight algorithm scales well with range but not very well if it has to check LOS to > 100 objects, which seems incredibly rare for this workload, the largest range any radio in the game searches through is only 3 tiles

the second optimization is to enforce complex setter vars for radios that removes them from the global radio list if they couldnt actually receive any radio transmissions from a given frequency in the first place.

the third optimization i did was massively reduce the number of hearables on the station by making hologram projectors not hear if dont have an active call/anything that would make them need hearing. so one of hte most common non player hearables that require view iteration to find is crossed out.

also implements a variation of an idea oranges had on how to speed up get_hearers_in_view() now that ive realized that view() cant be replicated by a raycasting algorithm. it distributes pregenerated abstract /mob/oranges_ear instances to all hearables in range such that theres at max one per turf and then iterates through only those mobs to take advantage of type-specific view() optimizations and just adds up the references in each one to create the list of hearing atoms, then puts the oranges_ear mobs back into nullspace. this is about 2x as fast as the get_hearers_in_view() on master

holy FUCK its fast. like really fucking fast. the only costly part of the radio transmission pipeline i dont touch is mob/living/Hear() which takes ~100 microseconds on live but searching through every radio in the world with get_hearers_in_radio_ranges() -> get_hearers_in_view() is much faster, as well as the filtering radios step

the spatial grid searching proc is about 36 microseconds/call at 10 range and 16 microseconds at 3 range in the captains office (relatively many hearables in view), the new get_hearers_in_view() was 4.16 times faster than get_hearers_in_view_old() at 10 range and 4.59 times faster at 3 range

SSspatial_grid could be used for a lot more things other than just radio and say code, i just didnt implement it. for example since the cells are datums you could get all cells in a radius then register for new objects entering them then activate when a player enters your radius. this is something that would require either very expensive view() calls or iterating over every player in the global list and calling get_dist() on them which isnt that expensive but is still worse than it needs to be

on normal get_hearers_in_view cost the new version that uses /mob/oranges_ear instances is about 2x faster than the old version, especially since the number of hearing sensitive movables has been brought down dramatically.

with get_hearers_in_view_oranges_ear() being the benchmark proc that implements this system and get_hearers_in_view() being a slightly optimized version of the version we have on master, get_hearers_in_view_as() being a more optimized version of the one we have on master, and get_hearers_in_LOS() being the raycasting version currently only used for radios because it cant replicate view()'s behavior perfectly.

---
## [Gopall/crawl](https://github.com/Gopall/crawl)@[070a2a64fb...](https://github.com/Gopall/crawl/commit/070a2a64fb29b2c910b5e7a89e561f090fa03f63)
#### Thursday 2021-12-23 01:11:51 by Kate

Allow demons and holies to be feared/berserked

As part of an effort to reduce the number of effects that are restricted
to natural monsters only, to increase some of the distinctions between
undead/demonic/nonliving holinesses, and to allow some more flavourful
interactions.

Lore-wise, demons and holies are supposed to be of similar stock aside from
their god alignment, so are grouped together here. They're also established
to be like living creatures in a number of ways - they're generally
intelligent, can be poisoned, and have souls, so it feels appropriate for
them to feel emotions in some way and be able to go berserk and be feared.
(Importantly this also allows the zealot's sword to send divine allies
berserk, for any TSO worshippers who happen to find it.)

---
## [yuberee/Frostrial](https://github.com/yuberee/Frostrial)@[712998bc7e...](https://github.com/yuberee/Frostrial/commit/712998bc7e21178c7217b5446b66f26c54c27313)
#### Thursday 2021-12-23 01:42:02 by Grodbert

hand drill animation

fuck this stupid animation piece of shit

---
## [pengxiangyu/incubator-doris](https://github.com/pengxiangyu/incubator-doris)@[ef2ea1806e...](https://github.com/pengxiangyu/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Thursday 2021-12-23 03:16:49 by HB

[docs] Improve the chapter on debugging FE in doc.  (#7309)

At present, there are defects in the chapter on debugging FE in doc. My colleagues and I stepped on the pit when 
building the debugging environment, so I want to improve this chapter in combination with my own stepping on the pit 
experience.

The following is my explanation of the changes: 

1. mkdir -p ./thirdparty/installed/bin
explain: When I downloaded versions 0.14 and 0.15, there were no files under thirdparty, so I didn't know whether to 
create it myself or what to do. Finally, I decided to create it myself. I think it's necessary to add instructions here.

2. Add installation thrift@0.13.0 Failed handling method. 
explain: My colleagues and I failed to find the installation package when executing the installation command, and finally 
found a solution on GitHub. Therefore, I added the handling method of the problem to avoid other Mac users from 
getting stuck in this place.

3. Fixed an error in the generated code description.
explain: Before I finished building the code, I debugged FE, and I failed all the time. Idea hints that no files can be found. 
Later, after consulting with morningman in wechat group, it was understood that `mvn install -DskipTests` does not 
need to execute `mvn generate-sources` after execution. This is inconsistent with the description in the document and 
needs to be corrected.

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[b2ba847c22...](https://github.com/BlueMemesauce/tgstation/commit/b2ba847c223dcbdc49c85a46156d5dbc28dbe5bd)
#### Thursday 2021-12-23 03:26:10 by LemonInTheDark

Reduces the move delay buffer to 1 tick (#63332)

We've got this delay buffer behavior
Idea is basically, if we're just holding down the key, just keep adding to the old delay
This way, fractional move delays make sense

Was added in this commit 491bdac

When it was added, movement was triggered by verbs sent by the client
So we needed a big grace window to account for networking delay

Don't need that anymore cause we use keyLoop, so let's just cut it all the way down

Why?
Because right now if you somehow manage to input a move afer move_delay is up
but before the window runs out, you will be elidgable for a new move before you visually reach the tile

Got a dm from mothblocks about this last night, something about flash stepping? IDK I don't play here
Seems silly though, let's sweep this up

Oh and mothblocks owes me a pizza, please add this to the commit history so it can be certified as a part of the blockchain

---
## [phial3/guava](https://github.com/phial3/guava)@[e015172847...](https://github.com/phial3/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Thursday 2021-12-23 03:30:04 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [AryanTommer/businessall](https://github.com/AryanTommer/businessall)@[3ca10b9692...](https://github.com/AryanTommer/businessall/commit/3ca10b9692b9dae988fbe3c528b96814e3cb5cf3)
#### Thursday 2021-12-23 03:39:05 by David Beguin

[IMP] im_livechat : optimize reports queries

Before, the duration and time to answer where computed based on the
mail channel creation date and
- the first message date from operator (for time to answer)
- the last message date (for duration)
But as the mail channel can be created long ago before the first message,
the result was not really representative.

Now, we are basing the computation only based on the messages.
Time to answer : first message date from operator - first message date
Duration : last message date - first message date

It allows, with the add of the second join on mail_message,
to simplify the extraction of those two indicator by removing the long
subselects.

Also, we fix the nbr_message in operator by adding the missing distinct.

Special mention to @jem-odoo who clearly did (almost) all the work :
This guy is amazing ! After a long and mature reflexion,
he finally put all his mighty power to enhance thoses reports
to give the users a wonderfull experience full of flowers and
peacefull sun, but also fast as a energized rabbit superhero !
Hail to him ! The One, the Only, the Chosen..
If you see him around the corner, please give him all your love
and gratitude ! Voilà voilà..

Task ID : 1895998
Closes PR #28283

---
## [AryanTommer/businessall](https://github.com/AryanTommer/businessall)@[855c6dac25...](https://github.com/AryanTommer/businessall/commit/855c6dac25fccaf9312543022001ed0b360d6e13)
#### Thursday 2021-12-23 03:49:12 by RomainLibert

[IMP] lunch: automatize lunch orders

We would like to automatize lunch as currently all orders are manually ordered and validated,
and a cash move has to be manually created each time you want to credit the wallet of some user.

1/ In this commit we add a new widget that comes with the kanban view
   and will allow to take orders in a friendly manner.
2/ We also add a lunch.supplier model this also allows you to configure an
   automatic ordering via email.
3/ Introduces new lunch.location model to replace res.partner on suppliers
4/ New mail template for automatic ordering
5/ Add the concept of new products (mark a product as new until some date)
6/ The toppings are now defined by product category
7/ Lunch.order removed, lunch.order.line renamed into lunch.order
8/ New SQL report to get the wallet content (aggregate of lunch.cashmove and lunch.order)
9/ New setting to allow negative wallet (aka overdraft)
10/ Application now remembers what notes and toppings you last ordered with your product
11/ You can change your location using the widget on the kanban view
12/ Edition of the order can be done until the order is arrived

TaskID: 1856876
TaskID: 1916105

closes odoo/odoo#30028

---
## [AryanTommer/businessall](https://github.com/AryanTommer/businessall)@[42fbee83ad...](https://github.com/AryanTommer/businessall/commit/42fbee83ad2f3f33188cf27a1449b8875c2d8a2a)
#### Thursday 2021-12-23 03:50:46 by Xavier Morel

[IMP] qweb: stop requiring t-name-flagged sub-node

QWeb's rendering currently *requires* that when loading a document
instead of rendering the document itself it will render a sub-node
with a properly labeled t-name. If a view is invoked by id, ir.qweb
will look for a child with a t-name and fix up that t-name such that
the base qweb object will find and render it.

This feature mostly exists for JS compatibility (because a single
document can contain multiple cross-linkable templates, and it was
useful for cross-implementation tests though I'm not sue they're even
checked anymore), and the <template> tag kinda took care of it,
however with a more proper qweb view it becomes more of a liability /
pain in the ass.

Note: turns out there are bits of javascript which read server
templates (???) and need to be altered to correctly handle the lack of
<templates> wrapping.

---
## [HanshenWang/project-isidore](https://github.com/HanshenWang/project-isidore)@[4a526fee36...](https://github.com/HanshenWang/project-isidore/commit/4a526fee36b233c1edd329beb2f1906578711d58)
#### Thursday 2021-12-23 04:44:50 by Hanshen Wang

Docs: Change License from LGPL 3.0 to AGPL 3.0.

Moving from weak copyleft to network protective copyleft.

Copyleft v. Permissive Licensing Rationale:
===========================================

"And you shall know the truth: and the truth shall make you free."

Free to do what? To know that adhering to the Truth means doing what one ought,
not whatever our fallen nature pleases. Whether from first principles or
experience, we know that human law must curtail behaviors when man fails to obey
the Truth and use his inviolable free will to say no to what is good, beautiful
and true. And the law must remain just when doing so, defined in the words of
the Thomists to mean "rendering to each his due".

Simply put, permissive licenses gives the developer the choice to restrict the
freedom of the end users. What freedoms?

From the FSF,

1. the freedom to use the software for any purpose,
2. the freedom to change the software to suit your needs,
3. the freedom to share the software with your friends and neighbors, and
4. the freedom to share the changes you make.

Freely you have received, and freely you must give. To have enjoyed these
freedoms and then to deny them to others would be hypocritical. That cannot be
denied. The golden rule is indeed reciprocal, and from this property Copyleft
licenses have also been termed reciprocal licenses, or viral licenses.

The warranty disclaimer in both Copyleft and Permissive also curtails some
freedoms. The freedom to engage in bad faith and frivolous lawsuits. Reciprocal
licensing curtails the freedom to deny others the four freedoms you have
received.

Some common objections:
=======================

1. GPL software restricts user freedom in practice.

Some have correctly identified copyleft licenses impede recombining with closed
source software.

On the contrary, the fault does not lie with the free software
portion of the equation but rather the closed source software that has decided
to deny the four freedoms. It can be easily seen that if both sides of the
equation were closed source software, the impedance to the end user would be
even greater.

2. GPL software prevents monetization.

This stems from confusion regarding liberty and gratis. Please note that the
author is too influenced by Thomas Sowell and Friedrich Hayek to consider a
central command economy a good idea for us fallible humans. If there is a need
to pigeonhole me into a political party, I am fiscally and socially
conservative. Of course wealth is not an inherent evil, it feels silly to even
have to type that. Nor was it ever my objective to bring Heaven unto earth and
usher in a gratis software utopia. Greed and intemperance are violations of
natural law no matter your political stripe.

On the contrary, It does not follow that reciprocal licensing disallows
commercialization. That would analogous to saying following the golden rule
makes for bad business.

This is not an either/or choice between copyleft and commercial licenses. It is
a both/and situation when one is able to include dual licenses. Reciprocity can
be in code or it can be in cash. Even projects solely GPL licensed have been
successfully monetized, though it can be argued the highest goal for such
projects was never a monetary one.

3. Reciprocity makes for bad business.

Wealth, as explained by Aquinas, is not the last end of man. In other words, not
an unqualified good. Not an end in of itself, but a means to an end. It makes no
sense on the individual or societal level to place wealth over justice. Unless
one has the position that a corrupt society is better than a just one.

On the contrary, anybody seriously placing monetary gain over justice would do
well to remember epistemology reminds us of our limited ability to see the
future. Indeed, 10 dead heroes are better men than 9 live cannibals. The flesh
may be weak, but it is ethical, proper and just to recognize such an ordering.
Only willful blindness and a misguided will reckons otherwise.

"Men are qualified for civil liberty in exact proportion to their disposition to
put moral chains upon their own appetites, in proportion as their love to
justice is above their rapacity,in proportion as their soundness and sobriety of
understanding is above their vanity and presumption,in proportion as they are
more disposed to listen to the counsels of the wise and good, in preference to
the flattery of knaves. Society cannot exist, unless a controlling power upon
will and appetite be placed somewhere; and the less of it there is within, the
more there must be without. It is ordained in the eternal constitution of
things, that men of intemperate minds cannot be free. Their passions forge their
fetters." Edmund Burke.

As repeated from the beginning of the commit message, Freedom is doing what you
ought, not what you want.

"And you shall know the truth: and the truth shall make you free."

4. My project will see less contributions due to current company policy

Out of all professions and trades, it is economists and businessmen who
understand most intimately that "there is no free lunch". As mentioned in
question 2, what is being objected here is the obligation to reciprocate. To
have their cake and eat it too, so to speak.

On the contrary, the goal for widespread adoption and therefore contributions is
a distinct goal from the preservation of the four freedoms. It is absolutely not
entirely separate, for any artifact deprived of human creative powers wilts and
dies (remember scientists shout "Eureka" and not "Genesis"). To that end, take
solace in the words of Thomas Paine, "Heaven knows how to put a proper price
upon its goods; and it would be strange indeed if so celestial an article as
FREEDOM should not be highly rated." A price worth paying.

If only this was a technical objection, but alas, here free software
evangelists share more in common with the Apostles than they are comfortable
admitting.

And so Burke, with much better rhetoric than I, expounds succinctly, "the less
of it there is within, the more there must be without." I somehow doubt the
FSF's existence is because Richard Stallman decided law was a more fulfilling
pursuit than his love of computer science. Michael Jackson got it right, be the
man in the mirror.

Compliance in layman's terms (not legal advice, please don't take it as such)
=============================================================================

To comply with the spirit of GPL is simple. If you do not modify the GPL
software by creating a derivative work but simply use it, you are under no
obligation to "reciprocate" by opening up your original work.

If you do modify the GPL software or create a derivative work by incorporating
the GPL code (possible because of the four freedoms extended to you), AND you do
NOT distribute the software, you are under no obligation to "reciprocate" by
opening up your original work. It's worth mentioning that this has been
interpreted to mean "internal use" within a company or organization is a-ok.

If you then proceed to distribute the derivative work, then the steps to
'reciprocate' is simple: release the source code of said derivative work so the
freedoms you have enjoyed may be enjoyed by our progeny. Here the AGPL adds to
the regular GPL clause 13, whereby distribution is taken to include interaction
through a remote network. The industry term is Software-as-a-Service.

Again, please consult a lawyer for advice. See also the precedence set by the
iText infringement claim by Bruno Lowagie.

Conclusion
==========

It's with such reasoning that I decided to license this project as AGPL-3.0 or
later. Now to be realistic, I foresee myself as the only developer for the
future. That does mean if I am convinced that a permissive license or the
0clause BSD pseudo public domain license is the best fit for this project, I am
all for switching. Please don't take this writing as the unilateral endorsement
of copyleft licenses for every single open source project.

---
## [HanshenWang/project-isidore](https://github.com/HanshenWang/project-isidore)@[b9016d708c...](https://github.com/HanshenWang/project-isidore/commit/b9016d708cbfce69811089c069381b5a45c0cb5f)
#### Thursday 2021-12-23 04:46:11 by Hanshen Wang

Docs: Change License from LGPL 3.0 to AGPL 3.0.

Moving from weak copyleft to network protective copyleft.

Copyleft v. Permissive Licensing Rationale:
===========================================

"And you shall know the truth: and the truth shall make you free."

Free to do what? To know that adhering to the Truth means doing what one ought,
not whatever our fallen nature pleases. Whether from first principles or
experience, we know that human law must curtail behaviors when man fails to obey
the Truth and use his inviolable free will to say no to what is good, beautiful
and true. And the law must remain just when doing so, defined in the words of
the Thomists to mean "rendering to each his due".

Simply put, permissive licenses gives the developer the choice to restrict the
freedom of the end users. What freedoms?

From the FSF,

1. the freedom to use the software for any purpose,
2. the freedom to change the software to suit your needs,
3. the freedom to share the software with your friends and neighbors, and
4. the freedom to share the changes you make.

Freely you have received, and freely you must give. To have enjoyed these
freedoms and then to deny them to others would be hypocritical. That cannot be
denied. The golden rule is indeed reciprocal, and from this property Copyleft
licenses have also been termed reciprocal licenses, or viral licenses.

The warranty disclaimer in both Copyleft and Permissive also curtails some
freedoms. The freedom to engage in bad faith and frivolous lawsuits. Reciprocal
licensing curtails the freedom to deny others the four freedoms you have
received.

Some common objections:
=======================

1. GPL software restricts user freedom in practice.

Some have correctly identified copyleft licenses impede recombining with closed
source software.

On the contrary, the fault does not lie with the free software
portion of the equation but rather the closed source software that has decided
to deny the four freedoms. It can be easily seen that if both sides of the
equation were closed source software, the impedance to the end user would be
even greater.

2. GPL software prevents monetization.

This stems from confusion regarding liberty and gratis. Please note that the
author is too influenced by Thomas Sowell and Friedrich Hayek to consider a
central command economy a good idea for us fallible humans. If there is a need
to pigeonhole me into a political party, I am fiscally and socially
conservative. Of course wealth is not an inherent evil, it feels silly to even
have to type that (it is written, man must eat by the sweat of his brow). Nor
was it ever my objective to bring Heaven unto earth and usher in a gratis
software utopia. Greed and intemperance are violations of natural law no matter
your political stripe.

On the contrary, It does not follow that reciprocal licensing disallows
commercialization. That would analogous to saying following the golden rule
makes for bad business.

This is not an either/or choice between copyleft and commercial licenses. It is
a both/and situation when one is able to include dual licenses. Reciprocity can
be in code or it can be in cash. Even projects solely GPL licensed have been
successfully monetized, though it can be argued the highest goal for such
projects was never a monetary one.

3. Reciprocity makes for bad business.

Wealth, as explained by Aquinas, is not the last end of man. In other words, not
an unqualified good. Not an end in of itself, but a means to an end. It makes no
sense on the individual or societal level to place wealth over justice. Unless
one has the position that a corrupt society is better than a just one.

On the contrary, anybody seriously placing monetary gain over justice would do
well to remember epistemology reminds us of our limited ability to see the
future. Indeed, 10 dead heroes are better men than 9 live cannibals. The flesh
may be weak, but it is ethical, proper and just to recognize such an ordering.
Only willful blindness and a misguided will reckons otherwise.

"Men are qualified for civil liberty in exact proportion to their disposition to
put moral chains upon their own appetites, in proportion as their love to
justice is above their rapacity,in proportion as their soundness and sobriety of
understanding is above their vanity and presumption,in proportion as they are
more disposed to listen to the counsels of the wise and good, in preference to
the flattery of knaves. Society cannot exist, unless a controlling power upon
will and appetite be placed somewhere; and the less of it there is within, the
more there must be without. It is ordained in the eternal constitution of
things, that men of intemperate minds cannot be free. Their passions forge their
fetters." Edmund Burke.

As repeated from the beginning of the commit message, Freedom is doing what you
ought, not what you want.

"And you shall know the truth: and the truth shall make you free."

4. My project will see less contributions due to current company policy

Out of all professions and trades, it is economists and businessmen who
understand most intimately that "there is no free lunch". As mentioned in
question 2, what is being objected here is the obligation to reciprocate. To
have their cake and eat it too, so to speak.

On the contrary, the goal for widespread adoption and therefore contributions is
a distinct goal from the preservation of the four freedoms. It is absolutely not
entirely separate, for any artifact deprived of human creative powers wilts and
dies (remember scientists shout "Eureka" and not "Genesis"). To that end, take
solace in the words of Thomas Paine, "Heaven knows how to put a proper price
upon its goods; and it would be strange indeed if so celestial an article as
FREEDOM should not be highly rated." A price worth paying.

If only this was a technical objection, but alas, here free software
evangelists share more in common with the Apostles than they are comfortable
admitting.

And so Burke, with much better rhetoric than I, expounds succinctly, "the less
of it there is within, the more there must be without." I somehow doubt the
FSF's existence is because Richard Stallman decided law was a more fulfilling
pursuit than his love of computer science. Michael Jackson got it right, be the
man in the mirror.

Compliance in layman's terms (not legal advice, please don't take it as such)
=============================================================================

To comply with the spirit of GPL is simple. If you do not modify the GPL
software by creating a derivative work but simply use it, you are under no
obligation to "reciprocate" by opening up your original work.

If you do modify the GPL software or create a derivative work by incorporating
the GPL code (possible because of the four freedoms extended to you), AND you do
NOT distribute the software, you are under no obligation to "reciprocate" by
opening up your original work. It's worth mentioning that this has been
interpreted to mean "internal use" within a company or organization is a-ok.

If you then proceed to distribute the derivative work, then the steps to
'reciprocate' is simple: release the source code of said derivative work so the
freedoms you have enjoyed may be enjoyed by our progeny. Here the AGPL adds to
the regular GPL clause 13, whereby distribution is taken to include interaction
through a remote network. The industry term is Software-as-a-Service.

Again, please consult a lawyer for advice. See also the precedence set by the
iText infringement claim by Bruno Lowagie.

Conclusion
==========

It's with such reasoning that I decided to license this project as AGPL-3.0 or
later. Now to be realistic, I foresee myself as the only developer for the
future. That does mean if I am convinced that a permissive license or the
0clause BSD pseudo public domain license is the best fit for this project, I am
all for switching. Please don't take this writing as the unilateral endorsement
of copyleft licenses for every single open source project.

---
## [TriHardspace/MAXXBox](https://github.com/TriHardspace/MAXXBox)@[f2168238ca...](https://github.com/TriHardspace/MAXXBox/commit/f2168238caf1df6acdf04fa97594cc926a7a3eac)
#### Thursday 2021-12-23 06:16:51 by Tyler Hoban

Merge pull request #8 from TriHardspace/main

fuck you jenkins

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[01ffad9320...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/01ffad93208a163379a7fb269802f8ac47fca336)
#### Thursday 2021-12-23 06:24:18 by Petr Mladek

kthread: add kthread_create_worker*()

Kthread workers are currently created using the classic kthread API,
namely kthread_run().  kthread_worker_fn() is passed as the @threadfn
parameter.

This patch defines kthread_create_worker() and
kthread_create_worker_on_cpu() functions that hide implementation details.

They enforce using kthread_worker_fn() for the main thread.  But I doubt
that there are any plans to create any alternative.  In fact, I think that
we do not want any alternative main thread because it would be hard to
support consistency with the rest of the kthread worker API.

The naming and function of kthread_create_worker() is inspired by the
workqueues API like the rest of the kthread worker API.

The kthread_create_worker_on_cpu() variant is motivated by the original
kthread_create_on_cpu().  Note that we need to bind per-CPU kthread
workers already when they are created.  It makes the life easier.
kthread_bind() could not be used later for an already running worker.

This patch does _not_ convert existing kthread workers.  The kthread
worker API need more improvements first, e.g.  a function to destroy the
worker.

IMPORTANT:

kthread_create_worker_on_cpu() allows to use any format of the worker
name, in compare with kthread_create_on_cpu().  The good thing is that it
is more generic.  The bad thing is that most users will need to pass the
cpu number in two parameters, e.g.  kthread_create_worker_on_cpu(cpu,
"helper/%d", cpu).

To be honest, the main motivation was to avoid the need for an empty
va_list.  The only legal way was to create a helper function that would be
called with an empty list.  Other attempts caused compilation warnings or
even errors on different architectures.

There were also other alternatives, for example, using #define or
splitting __kthread_create_worker().  The used solution looked like the
least ugly.

Link: http://lkml.kernel.org/r/1470754545-17632-6-git-send-email-pmladek@suse.com
Signed-off-by: Petr Mladek <pmladek@suse.com>
Acked-by: Tejun Heo <tj@kernel.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Steven Rostedt <rostedt@goodmis.org>
Cc: "Paul E. McKenney" <paulmck@linux.vnet.ibm.com>
Cc: Josh Triplett <josh@joshtriplett.org>
Cc: Thomas Gleixner <tglx@linutronix.de>
Cc: Jiri Kosina <jkosina@suse.cz>
Cc: Borislav Petkov <bp@suse.de>
Cc: Michal Hocko <mhocko@suse.cz>
Cc: Vlastimil Babka <vbabka@suse.cz>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: YousefAlgadri <yusufgadrie@gmail.com>
Signed-off-by: Thoreck <maulanafajar751@gmail.com>
Signed-off-by: Tiktodz <kuplemarkeple@gmail.com>

---
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[abaa5bf05f...](https://github.com/rHermes/adventofcode/commit/abaa5bf05fa669090688966f11eb88ff6bd667f6)
#### Thursday 2021-12-23 07:07:46 by Teodor Spæren

2021 Day 22

Well, what a day! This is the most challenging task this year I think, I
have not done much of 3D programming like this. It is something that I
want to get better at however, so I really should look into this!

I solved part one fast enough, but I already knew what part two was
going to be. I initially tried to find a library to do the collision
detection and this is where I spent most of my time.

None of them did really what I wanted and it was too much new
information to look into to get a good score. After about 2 hours 45
minutes, I started trying to hack together something with the excellent
"intervaltree" library.

I use 3 levels of the intervaltrees and use that. It took a little while
to figure out how to do everything, but in the end it worked, to my
surprise. I think I should have done this right away, as I briefly
considered it, but judged that it would not work and be hard.

I think this is the best takeaway here, that you should try to stick
with what you know until that doesn't work, then look for new libraries.
Had I started trying to hack something together, I would have been able
to solve the task and maybe place.

I also had a OOM error in the middle of this, trying to apply my part
one solution to part two. This didn't work out to well :P

I'm really excited to see how others solved this, and to clean up my
solution files a bit!

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 22   00:08:03    283      0   03:13:50   2014      0

---
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[2a4b0f8908...](https://github.com/rHermes/adventofcode/commit/2a4b0f8908cfc89db0e966ddb66ea0c4c729a3d8)
#### Thursday 2021-12-23 07:07:46 by Teodor Spæren

2021 Day 23

It's my birthday and for a present, I got a really nice task!

I realized quite quickly that this is really some sort of "towers of
Hanoi" variant, that can be solved without doing any sort of graph
search. I also realized that trying to be smart about this, would lead
me to spending much more time than if I just go with being stupid about
it :P

I ended up doing a BFS search of the board for each creature each turn
first, then I filter out the moves that are not valid for a creature to
make and the remaining possibilities is what I go off. I use an A*
search to move through the possibilities with a custom made, simple
heuristic.

I hardcoded the animal names and number, which would be a mistake in
part two, but whatever. I'm quite pleased with my part one, I did it as
quickly as I think I could.

Part two was a real nice challenge, but I made quite an important
mistake, which is why I spent almost an hour on part two, instead of 10
minutes. I forgot to update the "done" check, so the algorithm didn't
stop.

I would have found a solution much earlier if not for this, but this did
lead me to try a bunch of different approaches and small optimizations.
One of these is to convert from a pure "BFS" to a A* for the node
exploration. I also added in the concept of "moves" and such. I also
realized that it doesn't really matter which instances of the different
type of creatures are where, so I reduced the "seen" memory usage quite
a lot there, by ignoring the order as I went in.

The reason I realized that I had wrong "done" function is actually that
I had put process to run on my input in the background and it completed
without finding a solution. Once I saw that, it took 2 minutes to find
the answer.

I'm very happy with today, my placing could have been better, but I
don't think I would have made it to the leaderboard anyway, so I'm ok
with this. The task was fun and I had a blast!

For part two, I didn't change my board parsing, I just manually created
the extended board. This means that as of now, part two has to be run
against the "inp.txt" file, but I will change this when I clean up!

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 23   00:46:37    703      0   01:39:37    352      0

---
## [connectuum/poemdown](https://github.com/connectuum/poemdown)@[ac8d660c18...](https://github.com/connectuum/poemdown/commit/ac8d660c186d92c85c5a82de54f1113319649ee7)
#### Thursday 2021-12-23 07:46:05 by connectuum

flowed input into html conversion into overlay view

finally, we're into some more interesting work. glad to be through the frustration of deployment actions. the need to commit each test-trial into the repository, combined with the long turnaround time between each test, combined with the guess-the-magic-numbers feeling of configuration files, made it an especially annoying task.

so: _thrilled_ to be through with initial project setup and config. getting started with work on an idea is difficult enough on its own. and for the moment, it seems the headwinds will relent.

within this commit, i decided on a first task: read and react to input text. 

for the reading: an event handler collects the current text upon each change. this stumped me for a bit. i initially used the `onchange` handler, but received no events. i side-tracked into reviewing/debugging the handler function itself, but eventually returned to the source of the problem: it demands the `oninput` handler.

for the reaction: added a static class for converting poemdown text into other formats. for now, we just need `ToHtml()`. i had a little fun with it. and then _Hourglass_ came on while i was working here, and some comments spilled out.

seeing the lyrics as "two" jumped at me. [mitosis monkey, right in two]. human systems express stress as sharpening spears of opposition and fear. one way to inoculate: become more deeply interconnected. connection provides the strain of context. it resists spiky behaviors. [you pull the elastic], [the elastic pulls back].

after the conversion, the resulting HTML flows into the `div.overlay`, which renders exactly on top of the `textarea`. i'm not sure if this approach will be sufficient, but i'd rather not bring in a third-party library for this. i think we'll just need syntax highlighting here (and not all the text-formatting buttons that most of these libraries would provide).

bug: newline-to-break conversion
soon: regular expressions
horizon: d3 and force-directed graphs

---
## [KMatias123/NoCheatPlus](https://github.com/KMatias123/NoCheatPlus)@[3695671d3b...](https://github.com/KMatias123/NoCheatPlus/commit/3695671d3bb71cfd425876c1e358e8753c281337)
#### Thursday 2021-12-23 08:01:58 by Lysandr0

[Bleeding] Bunnyhop, bunnyfly, bug fixes.

Several/Major bunny adjustments (+ on the fly bug fixes)

1) Bunnyhop and slopes:
a) Let bunnyhop apply on yDistance
slopes (the jumping envelope is never hit: gravity hits harder here).
b) Grounded acceleration case (air-ground(landing), 0 hDist diff  ->
ground-ground,  0 hDist diff-> ground-ground, sudden mini burst of speed with no yDistance.
For this phase, we simply give players more momentum via bunnyhop ticks and increase speed slightly.
c) Continuous slope-jumping on ice will still fail  as speed  will keep increasing with each hop (Slime and normal ground seems fine)
d) Observed: edge case where bunnyfly speed decreases extremely little (in-air), thus, if the player has recently jumped up a slope and the hDist difference is small enough, the movement is allowed (should be confined more perhaps).

2) Get rid of that bloody sfOnIce legacy counter, at last.

3) Patch unintentional bypass with ice and headobstr.(bunnyhop -> drop speed below allowed to force set allowHop to true and to increase allowed friction speed -> bunnyhop again with higher speed (yOnGround case applies).

4) Cleanup, "simplify" (Where possible. Still too much spaghetti. Perhaps it's time for a rework :p).

5) Headbangbunny:
a) Don't wildcard; model should be decent enough now.
b) Observed: yet another case where clients can reach increasingly higher speed on ground: Touching ground in bunnyfriction with 0.3 speed -> ground-ground acceleration with 0.4 speed (bunnyhop) -> lifting off with increasing speed 0.5 (subsequent bunnyhop).

6) Hotfix for #171 : Allow bunny to consume the buffer.

7) Always clear hAcc on headbang.

8) On the fly:
a) sfVLTime -> sfVLMoveCount: we count moves, not time here.
b) Fix hopping right into a web (vertical).
c) Distinguish body in water VS body out of water when enforcing liquid->liquid speed limit: Magic has been warped for some time, how did we not get buried with reports about this !?
(Revert value to this commit: https://github.com/Updated-NoCheatPlus/NoCheatPlus/commit/c4331e1ffd4c7c17c43dba03f98f6feb875ada5b#diff-4adf02d4661b4aa4c5031880e2dd87200601581264a6d62eb56ce8c4b1606040 ).
d) Don't allow players to stand anywhere between minimum ground height and block height on ladders: fixes some fastladder bypasses (For @xaw3ep  is the Ground_Height flag still necessary? Seems like it's safe to remove)
Also slightly stricter climbable checking (step).

9) Move bunny stuff into its own workaround class (Coherence).

Missing:
1) Transitions stay problematic:
headobstructed -> head free / headobstructed on ice -> headobstructed on normal ground.

2) Bunnyhop while skimming over the edges of blocks. (video: https://www.dropbox.com/s/tdk1rdf9r3xwz5l/Edge_test.mov?dl=0 )
It does look like it's a problem with ice only (likely due to past moves being updated to not being on ice when touching the ground, the "lowjump problem" contributes as well).

3) Random setbacks when moving off from ice. Couldn't nail down the reason, let the buffer deal with this bullshit for now. Hopefully the higher modifier aids a little...

4) Hacc needs adjustments to take into account all illustrated cases.

5) Hop-after-velocity #171
Also applies when stopping to fly in air at high speed and falling. Looks like velocity isn't extended for long enough?

---
## [AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL)@[6274ad4594...](https://github.com/AFLplusplus/LibAFL/commit/6274ad4594af86869f7f678f9321d24851efe634)
#### Thursday 2021-12-23 08:10:14 by Andrea Fioraldi

Refactor libafl_qemu creating the Emulator struct and post syscall hooks (#430)

* working without asan.rs

* working asan

* update fuzzers

* mremap in snapshot

* sugar

* python

* fix python

* clippy

* fmt

* fuck you loader

---
## [leapofazzam123/termux-plus](https://github.com/leapofazzam123/termux-plus)@[cb2db3d995...](https://github.com/leapofazzam123/termux-plus/commit/cb2db3d995398511013e1441fe907c0a8cbaf401)
#### Thursday 2021-12-23 09:26:10 by Leap of Azzam

i hate my life

Signed-off-by: Leap of Azzam <leapofazzam@gmail.com>

---
## [Instrex/Deliverance](https://github.com/Instrex/Deliverance)@[a95fc0cd02...](https://github.com/Instrex/Deliverance/commit/a95fc0cd0238cbca0695371b6d444e9a4d328127)
#### Thursday 2021-12-23 09:56:09 by jubbalub

Lots of stuff, see description

* Eddie has a bit less health
* Nutcracker can now eat Boom Flies, Bonies, Suckers, and a few other things
* Nutcrackers now produce a few bone shots whenever they bite in the Ashpit
* Raga's homing shots now fire in an arc
* Rosenburg now shoots tar shots in the Dank Depths, blood shots in Chapter 4/4.5, a mix of mud shots and rocks in the Mines, and a mix of bone shots and rocks in the Ashpit.
* Added Ashpit variant for Musk (might not be used, we'll see)
* Peabody in Dross now uses poop-colored projectiles and brighter creep
* Added Mausoleum and Gehenna variants for Seraphim (wip)
* Added new visual effects to Cracker, Creampile, Eddie, Fistulauncher and its bomb, Peabody, Peamonger, Raga, Rosenberg, Seraphim, Stonelet, and Tinhorn

---
## [Chia-Network/chia-blockchain](https://github.com/Chia-Network/chia-blockchain)@[7949033929...](https://github.com/Chia-Network/chia-blockchain/commit/7949033929384e16d2537c179b1ee3fda7285959)
#### Thursday 2021-12-23 10:31:21 by dustinface

tests: Use `temp_dir` as `tmp2_dir`, drop `temp_dir` if canceled (#9601)

If you currently cancel the test during the plot setup phase it just
removes the whole directoy and with it all the test plots for no good
reason. At least in my opinion its just annoying. Sure, you can clone
the `test-cache` repo and copy them over if this happens but i still
think its better to just merge this PR :)

---
## [larsrh/website](https://github.com/larsrh/website)@[091f58bb75...](https://github.com/larsrh/website/commit/091f58bb7581920f8ea557a061dfae9477fdcbfa)
#### Thursday 2021-12-23 11:02:38 by Joy Heron

Add a scale of spacing variables which can be used for spacing

This is just a suggestion and can be tweaked for personal
preference. One trick to achieving consistent visual spacing is
to use a spacing scale instead of just choosing random values.
My personal preference is to use Fibonacci numbers for the scale,
so this adds some custom CSS properties which map to Fibonacci
values. These values can then be used within the CSS code.

When these values are used in the entirety of the webpage (including
the margins for headings, paragraphs, etc.), then it really helps
to achieve visual harmony. That would be a bit too large of a
change for a single commit, so this only tweaks a few CSS rules to
use the new spacing scale

This also adds a few utility classes for adding a `margin-top` to
certain elements. This change is _very_ controversial, because many
developers do not like utility classes. However, I've recently
begun to question that opinion. In my opinion, the spacing should
be a first class citizen of the CSS container components into
which we place our components. However, there are a lot of instances
where we need something like "Glue Code" to bring different
components together within a UI and give them the correct amount
of spacing. I think that utility classes are a good use case for
this particular problem -- like for the `Copy 🍪 to clipboard`
button: in this instance the button needs a bit of a margin-top,
but if we were to write a whole new class for this specific
instance of the button within the UI, it would be extremely hard
to reuse it. With utility classes, it's easier to achieve a
_certain_ amount of reusability.

Note: This method of defining spacing has a downside of not working
in super old browsers (e.g. IE11) because they do not support CSS
properties. That is a tradeoff that I personally make for my own
personal site, but if that is problematic for you, then you could
also decide not to use CSS properties but just use the scale values
directly in the CSS code (e.g. `margin-bottom: 1.25rem` instead of
`margin-bottom: var(--spacer-md);`).

---
## [ousvat/flutter](https://github.com/ousvat/flutter)@[99977cea1c...](https://github.com/ousvat/flutter/commit/99977cea1c4ab14dbd46866df8711d5a91af16f9)
#### Thursday 2021-12-23 11:29:12 by Pierre-Louis

[Fonts] Update icons (#95007)

* update icons

All existing codepoints are stable, with 2 exceptions `wifi_tethering_error_rounded_sharp` and `wifi_tethering_error_rounded_outlined`.

Add 1028 new icons. Codepoints:
airline_seat_individual_suite_baseline, airline_seat_legroom_reduced_baseline, airline_seat_legroom_normal_baseline, airline_seat_recline_normal_baseline, airline_seat_legroom_extra_baseline, airline_seat_recline_extra_baseline, airline_seat_flat_angled_baseline, align_horizontal_center_baseline, account_balance_wallet_baseline, align_horizontal_right_baseline, arrow_drop_down_circle_baseline, airplanemode_inactive_baseline, align_horizontal_left_baseline, align_vertical_bottom_baseline, align_vertical_center_baseline, admin_panel_settings_baseline, assignment_turned_in_baseline, assistant_navigation_baseline, add_photo_alternate_baseline, airplanemode_active_baseline, assignment_returned_baseline, assistant_direction_baseline, auto_awesome_mosaic_baseline, auto_awesome_motion_baseline, access_time_filled_baseline, accessible_forward_baseline, add_circle_outline_baseline, add_to_home_screen_baseline, align_vertical_top_baseline, arrow_back_ios_new_baseline, arrow_circle_right_baseline, arrow_circle_right_outlined, accessibility_new_baseline, add_shopping_cart_baseline, airline_seat_flat_baseline, arrow_circle_down_baseline, arrow_circle_left_baseline, arrow_circle_left_outlined, arrow_circle_right_rounded, arrow_forward_ios_baseline, assignment_return_baseline, add_location_alt_baseline, airplanemode_off_baseline, app_registration_baseline, app_settings_alt_baseline, arrow_circle_left_rounded, assured_workload_baseline, assured_workload_outlined, account_balance_baseline, airplane_ticket_baseline, airplanemode_on_baseline, airport_shuttle_baseline, alternate_email_baseline, arrow_circle_right_sharp, arrow_circle_up_baseline, arrow_drop_down_baseline, arrow_right_alt_baseline, assignment_late_baseline, assistant_photo_baseline, assured_workload_rounded, auto_fix_normal_baseline, account_circle_baseline, arrow_back_ios_baseline, arrow_circle_left_sharp, arrow_downward_baseline, assignment_ind_baseline, autofps_select_baseline, access_alarms_baseline, accessibility_baseline, add_moderator_baseline, add_to_photos_baseline, airline_stops_baseline, airline_stops_outlined, all_inclusive_baseline, arrow_drop_up_baseline, arrow_forward_baseline, assured_workload_sharp, auto_fix_high_baseline, access_alarm_baseline, account_tree_baseline, add_business_baseline, add_location_baseline, add_reaction_baseline, add_to_drive_baseline, add_to_queue_baseline, airline_stops_rounded, announcement_baseline, app_blocking_baseline, app_shortcut_baseline, app_shortcut_outlined, architecture_baseline, arrow_upward_baseline, aspect_ratio_baseline, attach_email_baseline, attach_money_baseline, auto_awesome_baseline, auto_fix_off_baseline, auto_stories_baseline, access_time_baseline, account_box_baseline, add_a_photo_baseline, add_comment_baseline, add_ic_call_baseline, adf_scanner_baseline, adf_scanner_outlined, agriculture_baseline, amp_stories_baseline, app_shortcut_rounded, apps_outage_baseline, apps_outage_outlined, arrow_right_baseline, attach_file_baseline, attractions_baseline, attribution_baseline, auto_delete_baseline, accessible_baseline, add_circle_baseline, adf_scanner_rounded, airline_stops_sharp, apps_outage_rounded, area_chart_baseline, area_chart_outlined, arrow_back_baseline, arrow_left_baseline, assessment_baseline, assignment_baseline, attachment_baseline, audio_file_baseline, audio_file_outlined, audiotrack_baseline, auto_graph_baseline, add_alarm_baseline, add_alert_baseline, add_chart_baseline, ads_click_baseline, ads_click_outlined, alarm_add_baseline, alarm_off_baseline, all_inbox_baseline, alt_route_baseline, analytics_baseline, animation_baseline, apartment_baseline, app_shortcut_sharp, area_chart_rounded, art_track_baseline, assistant_baseline, audio_file_rounded, autorenew_baseline, ad_units_baseline, add_call_baseline, add_card_baseline, add_card_outlined, add_link_baseline, add_road_baseline, add_task_baseline, addchart_baseline, adf_scanner_sharp, ads_click_rounded, airlines_baseline, airlines_outlined, alarm_on_baseline, approval_baseline, apps_outage_sharp, av_timer_baseline, ac_unit_baseline, add_box_baseline, add_card_rounded, airlines_rounded, airplay_baseline, all_out_baseline, android_baseline, archive_baseline, area_chart_sharp, article_baseline, audio_file_sharp, adjust_baseline, ads_click_sharp, anchor_baseline, add_card_sharp, adobe_baseline, adobe_outlined, airlines_sharp, alarm_baseline, album_baseline, apple_baseline, apple_outlined, adobe_rounded, apple_rounded, apps_baseline, abc_baseline, abc_outlined, adb_baseline, add_baseline, air_baseline, aod_baseline, api_baseline, atm_baseline, abc_rounded, adobe_sharp, apple_sharp, abc_sharp, baby_changing_station_baseline, battery_charging_full_baseline, browser_not_supported_baseline, bluetooth_connected_baseline, bluetooth_searching_baseline, bluetooth_disabled_baseline, branding_watermark_baseline, border_horizontal_baseline, brightness_medium_baseline, batch_prediction_baseline, bookmark_outline_baseline, breakfast_dining_baseline, battery_unknown_baseline, bluetooth_audio_baseline, bluetooth_drive_baseline, bookmark_border_baseline, bookmark_remove_baseline, border_vertical_baseline, brightness_auto_baseline, brightness_high_baseline, browser_updated_baseline, browser_updated_outlined, business_center_baseline, bedroom_parent_baseline, bookmark_added_baseline, brightness_low_baseline, browse_gallery_baseline, browse_gallery_outlined, browser_updated_rounded, bakery_dining_baseline, battery_alert_baseline, battery_saver_baseline, bedroom_child_baseline, block_flipped_baseline, blur_circular_baseline, border_bottom_baseline, browse_gallery_rounded, brunch_dining_baseline, backup_table_baseline, battery_full_baseline, beach_access_baseline, bedroom_baby_baseline, bike_scooter_baseline, bookmark_add_baseline, border_clear_baseline, border_color_baseline, border_inner_baseline, border_outer_baseline, border_right_baseline, border_style_baseline, brightness_5_baseline, brightness_4_baseline, brightness_1_baseline, brightness_7_baseline, brightness_6_baseline, brightness_3_baseline, brightness_2_baseline, broken_image_baseline, browser_updated_sharp, bubble_chart_baseline, build_circle_baseline, battery_std_baseline, bedtime_off_baseline, bedtime_off_outlined, blur_linear_baseline, book_online_baseline, border_left_baseline, browse_gallery_sharp, bedtime_off_rounded, border_all_baseline, border_top_baseline, bug_report_baseline, burst_mode_baseline, back_hand_baseline, back_hand_outlined, backspace_baseline, bar_chart_baseline, bloodtype_baseline, bluetooth_baseline, bookmarks_baseline, bus_alert_baseline, back_hand_rounded, backpack_baseline, bathroom_baseline, bedtime_off_sharp, beenhere_baseline, blur_off_baseline, bookmark_baseline, bungalow_baseline, business_baseline, balance_baseline, balance_outlined, balcony_baseline, bathtub_baseline, bedtime_baseline, biotech_baseline, blender_baseline, blur_on_baseline, back_hand_sharp, backup_baseline, balance_rounded, ballot_baseline, badge_baseline, bento_baseline, block_baseline, brush_baseline, build_baseline, balance_sharp, bolt_baseline, book_baseline, bed_baseline, boy_baseline, boy_outlined, boy_rounded, boy_sharp, check_box_outline_blank_baseline, closed_caption_disabled_baseline, connect_without_contact_baseline, control_point_duplicate_baseline, call_missed_outgoing_baseline, cancel_schedule_send_baseline, check_circle_outline_baseline, circle_notifications_baseline, collections_bookmark_baseline, content_paste_search_baseline, content_paste_search_outlined, calendar_view_month_baseline, cancel_presentation_baseline, center_focus_strong_baseline, chat_bubble_outline_baseline, compass_calibration_baseline, confirmation_number_baseline, connecting_airports_baseline, connecting_airports_outlined, content_paste_search_rounded, calendar_view_week_baseline, cast_for_education_baseline, chrome_reader_mode_baseline, closed_caption_off_baseline, connecting_airports_rounded, calendar_view_day_baseline, candlestick_chart_baseline, candlestick_chart_outlined, center_focus_weak_baseline, cleaning_services_baseline, comments_disabled_baseline, comments_disabled_outlined, content_paste_off_baseline, content_paste_search_sharp, create_new_folder_baseline, currency_exchange_baseline, currency_exchange_outlined, candlestick_chart_rounded, catching_pokemon_baseline, charging_station_baseline, close_fullscreen_baseline, comments_disabled_rounded, confirmation_num_baseline, connecting_airports_sharp, content_paste_go_baseline, content_paste_go_outlined, currency_bitcoin_baseline, currency_bitcoin_outlined, currency_exchange_rounded, card_membership_baseline, contact_support_baseline, content_paste_go_rounded, credit_card_off_baseline, currency_bitcoin_rounded, calendar_month_baseline, calendar_month_outlined, calendar_today_baseline, call_to_action_baseline, camera_enhance_baseline, camera_outdoor_baseline, candlestick_chart_sharp, cast_connected_baseline, change_history_baseline, child_friendly_baseline, closed_caption_baseline, cloud_download_baseline, cloudy_snowing_baseline, comments_disabled_sharp, compare_arrows_baseline, control_camera_baseline, corporate_fare_baseline, crop_landscape_baseline, currency_exchange_sharp, currency_franc_baseline, currency_franc_outlined, currency_pound_baseline, currency_pound_outlined, currency_ruble_baseline, currency_ruble_outlined, currency_rupee_baseline, currency_rupee_outlined, calendar_month_rounded, call_received_baseline, camera_indoor_baseline, card_giftcard_baseline, change_circle_baseline, checklist_rtl_baseline, chevron_right_baseline, contact_phone_baseline, content_paste_baseline, content_paste_go_sharp, control_point_baseline, crop_original_baseline, crop_portrait_baseline, currency_bitcoin_sharp, currency_franc_rounded, currency_lira_baseline, currency_lira_outlined, currency_pound_rounded, currency_ruble_rounded, currency_rupee_rounded, currency_yuan_baseline, currency_yuan_outlined, camera_front_baseline, cameraswitch_baseline, check_circle_baseline, chevron_left_baseline, cloud_circle_baseline, cloud_upload_baseline, coffee_maker_baseline, comment_bank_baseline, connected_tv_baseline, construction_baseline, contact_mail_baseline, contact_page_baseline, content_copy_baseline, credit_score_baseline, cruelty_free_baseline, cruelty_free_outlined, currency_lira_rounded, currency_yen_baseline, currency_yen_outlined, currency_yuan_rounded, calendar_month_sharp, call_missed_baseline, camera_rear_baseline, camera_roll_baseline, card_travel_baseline, celebration_baseline, chat_bubble_baseline, clean_hands_baseline, cloud_queue_baseline, collections_baseline, contactless_baseline, content_cut_baseline, coronavirus_baseline, countertops_baseline, credit_card_baseline, crop_rotate_baseline, crop_square_baseline, cruelty_free_rounded, currency_franc_sharp, currency_pound_sharp, currency_ruble_sharp, currency_rupee_sharp, currency_yen_rounded, call_merge_baseline, call_split_baseline, camera_alt_baseline, car_rental_baseline, car_repair_baseline, cell_tower_baseline, cell_tower_outlined, child_care_baseline, cloud_done_baseline, cloud_sync_baseline, cloud_sync_outlined, co_present_baseline, co_present_outlined, color_lens_baseline, currency_lira_sharp, currency_yuan_sharp, calculate_baseline, call_made_baseline, carpenter_baseline, cell_tower_rounded, cell_wifi_baseline, chair_alt_baseline, check_box_baseline, checklist_baseline, checkroom_baseline, clear_all_baseline, cloud_off_baseline, cloud_sync_rounded, co_present_rounded, copyright_baseline, crop_16_9_baseline, crop_free_baseline, cruelty_free_sharp, currency_yen_sharp, call_end_baseline, campaign_baseline, category_baseline, code_off_baseline, colorize_baseline, compress_baseline, computer_baseline, contacts_baseline, contrast_baseline, contrast_outlined, copy_all_baseline, crop_din_baseline, crop_5_4_baseline, crop_7_5_baseline, crop_3_2_baseline, cell_tower_sharp, cloud_sync_sharp, co_present_sharp, comment_baseline, commute_baseline, compare_baseline, compost_baseline, compost_outlined, contrast_rounded, cottage_baseline, cached_baseline, camera_baseline, cancel_baseline, casino_baseline, castle_baseline, castle_outlined, chalet_baseline, church_baseline, church_outlined, circle_baseline, coffee_baseline, commit_baseline, commit_outlined, compost_rounded, cookie_baseline, cookie_outlined, create_baseline, cabin_baseline, cable_baseline, cases_baseline, castle_rounded, chair_baseline, check_baseline, church_rounded, class_baseline, clear_baseline, close_baseline, cloud_baseline, commit_rounded, contrast_sharp, cookie_rounded, cake_baseline, call_baseline, cast_baseline, chat_baseline, code_baseline, compost_sharp, copy_baseline, crib_baseline, crop_baseline, castle_sharp, church_sharp, co2_baseline, co2_outlined, commit_sharp, cookie_sharp, css_baseline, css_outlined, cut_baseline, co2_rounded, css_rounded, co2_sharp, css_sharp, do_not_disturb_on_total_silence_baseline, directions_railway_filled_baseline, directions_transit_filled_baseline, drive_file_rename_outline_baseline, directions_subway_filled_baseline, desktop_access_disabled_baseline, drive_file_move_outline_baseline, directions_boat_filled_baseline, directions_bus_filled_baseline, directions_car_filled_baseline, download_for_offline_baseline, dashboard_customize_baseline, developer_board_off_baseline, disabled_by_default_baseline, domain_verification_baseline, drive_file_move_rtl_baseline, drive_file_move_rtl_outlined, drive_folder_upload_baseline, directions_railway_baseline, directions_transit_baseline, do_not_disturb_alt_baseline, do_not_disturb_off_baseline, drive_file_move_rtl_rounded, data_thresholding_baseline, data_thresholding_outlined, device_thermostat_baseline, directions_subway_baseline, do_not_disturb_on_baseline, data_exploration_baseline, data_exploration_outlined, data_thresholding_rounded, directions_ferry_baseline, directions_train_baseline, disabled_visible_baseline, disabled_visible_outlined, display_settings_baseline, display_settings_outlined, dnd_forwardslash_baseline, document_scanner_baseline, drive_file_move_rtl_sharp, data_exploration_rounded, delivery_dining_baseline, departure_board_baseline, design_services_baseline, desktop_windows_baseline, developer_board_baseline, directions_bike_baseline, directions_boat_baseline, directions_walk_baseline, disabled_visible_rounded, display_settings_rounded, domain_disabled_baseline, downhill_skiing_baseline, drive_file_move_baseline, data_saver_off_baseline, data_thresholding_sharp, delete_forever_baseline, delete_outline_baseline, density_medium_baseline, density_medium_outlined, developer_mode_baseline, device_unknown_baseline, directions_bus_baseline, directions_car_baseline, directions_off_baseline, directions_run_baseline, do_disturb_alt_baseline, do_disturb_off_baseline, do_not_disturb_baseline, drag_indicator_baseline, data_exploration_sharp, data_saver_on_baseline, density_large_baseline, density_large_outlined, density_medium_rounded, density_small_baseline, density_small_outlined, devices_other_baseline, dinner_dining_baseline, disabled_visible_sharp, display_settings_sharp, do_disturb_on_baseline, download_done_baseline, delete_sweep_baseline, density_large_rounded, density_small_rounded, do_not_touch_baseline, done_outline_baseline, door_sliding_baseline, double_arrow_baseline, dry_cleaning_baseline, dynamic_feed_baseline, dynamic_form_baseline, data_object_baseline, data_object_outlined, density_medium_sharp, description_baseline, desktop_mac_baseline, do_not_step_baseline, donut_large_baseline, donut_small_baseline, downloading_baseline, drag_handle_baseline, data_array_baseline, data_array_outlined, data_object_rounded, data_usage_baseline, date_range_baseline, density_large_sharp, density_small_sharp, device_hub_baseline, dialer_sip_baseline, difference_baseline, difference_outlined, directions_baseline, dirty_lens_baseline, do_disturb_baseline, domain_add_baseline, domain_add_outlined, door_front_baseline, dangerous_baseline, dark_mode_baseline, dashboard_baseline, data_array_rounded, difference_rounded, disc_full_baseline, domain_add_rounded, door_back_baseline, drive_eta_baseline, data_object_sharp, deselect_baseline, deselect_outlined, discount_baseline, discount_outlined, done_all_baseline, doorbell_baseline, download_baseline, data_array_sharp, deselect_rounded, details_baseline, devices_baseline, dialpad_baseline, diamond_baseline, diamond_outlined, difference_sharp, discord_baseline, discord_outlined, discount_rounded, domain_add_sharp, deblur_baseline, deblur_outlined, dehaze_baseline, delete_baseline, diamond_rounded, dining_baseline, discord_rounded, domain_baseline, drafts_baseline, deblur_rounded, deselect_sharp, discount_sharp, deck_baseline, diamond_sharp, discord_sharp, dock_baseline, done_baseline, draw_baseline, draw_outlined, deblur_sharp, dns_baseline, draw_rounded, dry_baseline, duo_baseline, dvr_baseline, draw_sharp, 4g_plus_mobiledata_baseline, 4g_mobiledata_baseline, 4k_plus_baseline, 4mp_baseline, 4k_baseline, 5k_plus_baseline, 5mp_baseline, 5g_baseline, 5k_baseline, 8k_plus_baseline, 8mp_baseline, 8k_baseline, 1x_mobiledata_baseline, 1k_plus_baseline, 18mp_baseline, 15mp_baseline, 14mp_baseline, 19mp_baseline, 11mp_baseline, 17mp_baseline, 16mp_baseline, 13mp_baseline, 12mp_baseline, 10mp_baseline, 123_baseline, 123_outlined, 10k_baseline, 123_rounded, 1k_baseline, 123_sharp, enhance_photo_translate_baseline, emoji_transportation_baseline, electrical_services_baseline, emoji_food_beverage_baseline, enhanced_encryption_baseline, edit_notifications_baseline, expand_circle_down_baseline, expand_circle_down_outlined, edit_location_alt_baseline, electric_rickshaw_baseline, escalator_warning_baseline, expand_circle_down_rounded, electric_scooter_baseline, exposure_minus_1_baseline, exposure_minus_2_baseline, earbuds_battery_baseline, edgesensor_high_baseline, edit_attributes_baseline, event_available_baseline, expand_circle_down_sharp, exposure_plus_1_baseline, exposure_plus_2_baseline, edgesensor_low_baseline, electric_moped_baseline, emoji_emotions_baseline, exposure_neg_1_baseline, exposure_neg_2_baseline, edit_calendar_baseline, edit_calendar_outlined, edit_location_baseline, elderly_woman_baseline, elderly_woman_outlined, electric_bike_baseline, emoji_objects_baseline, emoji_symbols_baseline, error_outline_baseline, exposure_zero_baseline, extension_off_baseline, e_mobiledata_baseline, edit_calendar_rounded, elderly_woman_rounded, electric_car_baseline, emoji_events_baseline, emoji_nature_baseline, emoji_people_baseline, event_repeat_baseline, event_repeat_outlined, emoji_flags_baseline, engineering_baseline, euro_symbol_baseline, event_repeat_rounded, exit_to_app_baseline, expand_less_baseline, expand_more_baseline, explore_off_baseline, edit_calendar_sharp, elderly_woman_sharp, ev_station_baseline, event_busy_baseline, event_note_baseline, event_seat_baseline, edit_note_baseline, edit_note_outlined, edit_road_baseline, emergency_baseline, emergency_outlined, equalizer_baseline, escalator_baseline, event_repeat_sharp, extension_baseline, edit_note_rounded, edit_off_baseline, elevator_baseline, emergency_rounded, explicit_baseline, exposure_baseline, earbuds_baseline, egg_alt_baseline, egg_alt_outlined, elderly_baseline, explore_baseline, edit_note_sharp, egg_alt_rounded, emergency_sharp, expand_baseline, eject_baseline, email_baseline, error_baseline, event_baseline, east_baseline, edit_baseline, egg_alt_sharp, euro_baseline, eco_baseline, egg_baseline, egg_outlined, egg_rounded, egg_sharp, 2k_plus_baseline, 24mp_baseline, 21mp_baseline, 23mp_baseline, 22mp_baseline, 20mp_baseline, 2mp_baseline, 2k_baseline, 3g_mobiledata_baseline, 30fps_select_baseline, 3d_rotation_baseline, 3k_plus_baseline, 30fps_baseline, 360_baseline, 3mp_baseline, 3k_baseline, 3p_baseline, 60fps_select_baseline, 6_ft_apart_baseline, 6k_plus_baseline, 60fps_baseline, 6mp_baseline, 6k_baseline, 7k_plus_baseline, 7mp_baseline, 7k_baseline, 9k_plus_baseline, 9mp_baseline, 9k_baseline, format_textdirection_l_to_r_baseline, format_textdirection_r_to_l_baseline, format_list_numbered_rtl_baseline, face_retouching_natural_baseline, format_indent_decrease_baseline, format_indent_increase_baseline, format_align_justify_baseline, format_list_bulleted_baseline, format_list_numbered_baseline, format_strikethrough_baseline, face_retouching_off_baseline, fiber_manual_record_baseline, filter_center_focus_baseline, flip_camera_android_baseline, format_align_center_baseline, format_line_spacing_baseline, featured_play_list_baseline, fiber_smart_record_baseline, file_download_done_baseline, format_align_right_baseline, format_color_reset_baseline, file_download_off_baseline, filter_tilt_shift_baseline, fire_extinguisher_baseline, font_download_off_baseline, format_align_left_baseline, format_color_fill_baseline, format_color_text_baseline, format_underlined_baseline, free_cancellation_baseline, free_cancellation_outlined, favorite_outline_baseline, follow_the_signs_baseline, format_underline_baseline, forward_to_inbox_baseline, free_cancellation_rounded, family_restroom_baseline, favorite_border_baseline, filter_list_alt_baseline, filter_list_off_baseline, filter_list_off_outlined, flip_camera_ios_baseline, format_overline_baseline, format_overline_outlined, fullscreen_exit_baseline, featured_video_baseline, filter_alt_off_baseline, filter_alt_off_outlined, filter_b_and_w_baseline, filter_list_off_rounded, filter_vintage_baseline, fitness_center_baseline, flashlight_off_baseline, flight_takeoff_baseline, folder_special_baseline, format_overline_rounded, free_breakfast_baseline, free_cancellation_sharp, file_download_baseline, filter_alt_off_rounded, filter_9_plus_baseline, filter_frames_baseline, flashlight_on_baseline, flip_to_front_baseline, folder_delete_baseline, folder_delete_outlined, folder_shared_baseline, font_download_baseline, format_italic_baseline, format_shapes_baseline, fast_forward_baseline, file_present_baseline, filter_drama_baseline, filter_list_off_sharp, find_in_page_baseline, find_replace_baseline, fire_hydrant_baseline, flight_class_baseline, flight_class_outlined, flip_to_back_baseline, flutter_dash_baseline, folder_delete_rounded, format_clear_baseline, format_overline_sharp, format_paint_baseline, format_quote_baseline, fast_rewind_baseline, file_upload_baseline, filter_alt_off_sharp, filter_list_baseline, filter_none_baseline, fingerprint_baseline, flag_circle_baseline, flag_circle_outlined, flight_class_rounded, flight_land_baseline, flourescent_baseline, folder_copy_baseline, folder_copy_outlined, folder_open_baseline, format_bold_baseline, format_size_baseline, fact_check_baseline, filter_alt_baseline, filter_hdr_baseline, first_page_baseline, fit_screen_baseline, flag_circle_rounded, flash_auto_baseline, folder_copy_rounded, folder_delete_sharp, folder_off_baseline, folder_off_outlined, folder_zip_baseline, folder_zip_outlined, fork_right_baseline, fork_right_outlined, forward_10_baseline, forward_30_baseline, foundation_baseline, front_hand_baseline, front_hand_outlined, fullscreen_baseline, fiber_dvr_baseline, fiber_new_baseline, fiber_pin_baseline, file_copy_baseline, file_open_baseline, file_open_outlined, fireplace_baseline, flash_off_baseline, flight_class_sharp, folder_off_rounded, folder_zip_rounded, food_bank_baseline, fork_left_baseline, fork_left_outlined, fork_right_rounded, forward_5_baseline, front_hand_rounded, functions_baseline, facebook_baseline, fastfood_baseline, favorite_baseline, feedback_baseline, festival_baseline, file_open_rounded, filter_8_baseline, filter_5_baseline, filter_4_baseline, filter_9_baseline, filter_1_baseline, filter_7_baseline, filter_6_baseline, filter_3_baseline, filter_2_baseline, flag_circle_sharp, flash_on_baseline, flatware_baseline, fmd_good_baseline, folder_copy_sharp, fork_left_rounded, factory_baseline, factory_outlined, fmd_bad_baseline, folder_off_sharp, folder_zip_sharp, fork_right_sharp, forward_baseline, front_hand_sharp, factory_rounded, female_baseline, file_open_sharp, filter_baseline, fitbit_baseline, fitbit_outlined, flight_baseline, folder_baseline, forest_baseline, forest_outlined, fork_left_sharp, fence_baseline, fitbit_rounded, flaky_baseline, flare_baseline, foggy_baseline, forest_rounded, forum_baseline, face_baseline, factory_sharp, feed_baseline, flag_baseline, flip_baseline, fort_baseline, fort_outlined, fax_baseline, fax_outlined, fitbit_sharp, forest_sharp, fort_rounded, fax_rounded, fort_sharp, fax_sharp, generating_tokens_baseline, generating_tokens_outlined, generating_tokens_rounded, grid_goldenratio_baseline, generating_tokens_sharp, gps_not_fixed_baseline, g_mobiledata_baseline, group_remove_baseline, group_remove_outlined, g_translate_baseline, golf_course_baseline, group_remove_rounded, graphic_eq_baseline, group_work_baseline, gpp_maybe_baseline, gps_fixed_baseline, grid_view_baseline, group_add_baseline, group_off_baseline, group_off_outlined, group_remove_sharp, gpp_good_baseline, gradient_baseline, grid_4x4_baseline, grid_3x3_baseline, grid_off_baseline, group_off_rounded, gamepad_baseline, gesture_baseline, get_app_baseline, gif_box_baseline, gif_box_outlined, gpp_bad_baseline, gps_off_baseline, grading_baseline, grid_on_baseline, garage_baseline, gif_box_rounded, group_off_sharp, groups_baseline, games_baseline, gavel_baseline, grade_baseline, grain_baseline, grass_baseline, group_baseline, gif_box_sharp, girl_baseline, girl_outlined, gite_baseline, gif_baseline, girl_rounded, girl_sharp, horizontal_distribute_baseline, hdr_enhanced_select_baseline, home_repair_service_baseline, headphones_battery_baseline, history_toggle_off_baseline, hourglass_disabled_baseline, h_plus_mobiledata_baseline, health_and_safety_baseline, hearing_disabled_baseline, highlight_remove_baseline, horizontal_split_baseline, hourglass_bottom_baseline, hdr_auto_select_baseline, holiday_village_baseline, horizontal_rule_baseline, hourglass_empty_baseline, hdr_off_select_baseline, hourglass_full_baseline, hdr_on_select_baseline, highlight_alt_baseline, highlight_off_baseline, hourglass_top_baseline, h_mobiledata_baseline, heart_broken_baseline, heart_broken_outlined, help_outline_baseline, high_quality_baseline, house_siding_baseline, headset_mic_baseline, headset_off_baseline, heart_broken_rounded, help_center_baseline, hide_source_baseline, history_edu_baseline, home_filled_baseline, hotel_class_baseline, hotel_class_outlined, how_to_vote_baseline, hdr_strong_baseline, headphones_baseline, hide_image_baseline, hotel_class_rounded, how_to_reg_baseline, handshake_baseline, handshake_outlined, heart_broken_sharp, highlight_baseline, home_mini_baseline, home_work_baseline, houseboat_baseline, handshake_rounded, handyman_baseline, hardware_baseline, hdr_auto_baseline, hdr_plus_baseline, hdr_weak_baseline, home_max_baseline, hotel_class_sharp, hdr_off_baseline, headset_baseline, healing_baseline, hearing_baseline, hexagon_baseline, hexagon_outlined, history_baseline, hls_off_baseline, hls_off_outlined, hot_tub_baseline, handshake_sharp, hdr_on_baseline, height_baseline, hexagon_rounded, hiking_baseline, hls_off_rounded, hotel_baseline, house_baseline, https_baseline, hail_baseline, help_baseline, hevc_baseline, hexagon_sharp, hive_baseline, hive_outlined, hls_off_sharp, home_baseline, html_baseline, html_outlined, http_baseline, hvac_baseline, hive_rounded, hls_baseline, hls_outlined, html_rounded, hub_baseline, hub_outlined, hd_baseline, hls_rounded, hub_rounded, hive_sharp, html_sharp, hls_sharp, hub_sharp, keyboard_double_arrow_right_baseline, keyboard_double_arrow_right_outlined, keyboard_double_arrow_down_baseline, keyboard_double_arrow_down_outlined, keyboard_double_arrow_left_baseline, keyboard_double_arrow_left_outlined, keyboard_double_arrow_right_rounded, keyboard_double_arrow_down_rounded, keyboard_double_arrow_left_rounded, keyboard_double_arrow_right_sharp, keyboard_double_arrow_up_baseline, keyboard_double_arrow_up_outlined, keyboard_double_arrow_down_sharp, keyboard_double_arrow_left_sharp, keyboard_double_arrow_up_rounded, keyboard_double_arrow_up_sharp, keyboard_arrow_right_baseline, keyboard_command_key_baseline, keyboard_command_key_outlined, keyboard_control_key_baseline, keyboard_control_key_outlined, keyboard_arrow_down_baseline, keyboard_arrow_left_baseline, keyboard_command_key_rounded, keyboard_control_key_rounded, keyboard_option_key_baseline, keyboard_option_key_outlined, keyboard_backspace_baseline, keyboard_option_key_rounded, keyboard_arrow_up_baseline, keyboard_capslock_baseline, keyboard_command_key_sharp, keyboard_control_key_sharp, keyboard_control_baseline, keyboard_option_key_sharp, keyboard_return_baseline, keyboard_voice_baseline, keyboard_hide_baseline, kebab_dining_baseline, kebab_dining_outlined, keyboard_alt_baseline, keyboard_tab_baseline, kebab_dining_rounded, kitesurfing_baseline, kebab_dining_sharp, kayaking_baseline, keyboard_baseline, king_bed_baseline, key_off_baseline, key_off_outlined, kitchen_baseline, key_off_rounded, key_off_sharp, key_baseline, key_outlined, key_rounded, key_sharp, label_important_outline_baseline, local_convenience_store_baseline, local_fire_department_baseline, local_laundry_service_baseline, local_grocery_store_baseline, lte_plus_mobiledata_baseline, leave_bags_at_home_baseline, location_searching_baseline, laptop_chromebook_baseline, library_add_check_baseline, lightbulb_outline_baseline, local_gas_station_baseline, local_post_office_baseline, location_disabled_baseline, local_attraction_baseline, local_print_shop_baseline, local_restaurant_baseline, location_history_baseline, label_important_baseline, local_printshop_baseline, laptop_windows_baseline, local_activity_baseline, local_car_wash_baseline, local_hospital_baseline, local_pharmacy_baseline, local_shipping_baseline, lte_mobiledata_baseline, label_outline_baseline, legend_toggle_baseline, library_books_baseline, library_music_baseline, linked_camera_baseline, local_airport_baseline, local_florist_baseline, local_library_baseline, local_parking_baseline, location_city_baseline, layers_clear_baseline, linear_scale_baseline, local_dining_baseline, local_movies_baseline, local_police_baseline, location_off_baseline, location_pin_baseline, lock_outline_baseline, low_priority_baseline, lunch_dining_baseline, leaderboard_baseline, leak_remove_baseline, library_add_baseline, line_weight_baseline, local_drink_baseline, local_hotel_baseline, local_offer_baseline, local_phone_baseline, local_pizza_baseline, location_on_baseline, laptop_mac_baseline, light_mode_baseline, line_style_baseline, local_cafe_baseline, local_mall_baseline, local_play_baseline, local_taxi_baseline, lock_clock_baseline, lock_reset_baseline, lock_reset_outlined, label_off_baseline, landscape_baseline, last_page_baseline, lens_blur_baseline, lightbulb_baseline, line_axis_baseline, line_axis_outlined, live_help_baseline, local_atm_baseline, local_bar_baseline, local_see_baseline, lock_open_baseline, lock_reset_rounded, looks_one_baseline, looks_two_baseline, language_baseline, leak_add_baseline, line_axis_rounded, link_off_baseline, list_alt_baseline, logo_dev_baseline, logo_dev_outlined, live_tv_baseline, lock_reset_sharp, logo_dev_rounded, looks_5_baseline, looks_4_baseline, looks_6_baseline, looks_3_baseline, loyalty_baseline, luggage_baseline, laptop_baseline, launch_baseline, layers_baseline, line_axis_sharp, liquor_baseline, living_baseline, logout_baseline, label_baseline, light_baseline, login_baseline, logo_dev_sharp, looks_baseline, loupe_baseline, lens_baseline, link_baseline, list_baseline, lock_baseline, loop_baseline, lan_baseline, lan_outlined, lan_rounded, lan_sharp, integration_instructions_baseline, indeterminate_check_box_baseline, insert_chart_outlined_baseline, image_not_supported_baseline, image_aspect_ratio_baseline, imagesearch_roller_baseline, important_devices_baseline, incomplete_circle_baseline, incomplete_circle_outlined, insert_drive_file_baseline, insert_invitation_baseline, insert_page_break_baseline, insert_page_break_outlined, invert_colors_off_baseline, incomplete_circle_rounded, insert_page_break_rounded, interpreter_mode_baseline, interpreter_mode_outlined, invert_colors_on_baseline, import_contacts_baseline, insert_emoticon_baseline, install_desktop_baseline, install_desktop_outlined, interpreter_mode_rounded, incomplete_circle_sharp, insert_comment_baseline, insert_page_break_sharp, install_desktop_rounded, install_mobile_baseline, install_mobile_outlined, import_export_baseline, install_mobile_rounded, interpreter_mode_sharp, invert_colors_baseline, image_search_baseline, info_outline_baseline, insert_chart_baseline, insert_photo_baseline, install_desktop_sharp, ice_skating_baseline, insert_link_baseline, install_mobile_sharp, inventory_2_baseline, interests_baseline, interests_outlined, inventory_baseline, ios_share_baseline, icecream_baseline, insights_baseline, interests_rounded, interests_sharp, image_baseline, inbox_baseline, input_baseline, info_baseline, iron_baseline, iso_baseline, javascript_baseline, javascript_outlined, join_inner_baseline, join_inner_outlined, join_right_baseline, join_right_outlined, javascript_rounded, join_full_baseline, join_full_outlined, join_inner_rounded, join_left_baseline, join_left_outlined, join_right_rounded, join_full_rounded, join_left_rounded, javascript_sharp, join_inner_sharp, join_right_sharp, join_full_sharp, join_left_sharp, online_prediction_baseline, open_in_browser_baseline, open_in_new_off_baseline, ondemand_video_baseline, offline_share_baseline, outdoor_grill_baseline, outgoing_mail_baseline, outlined_flag_baseline, offline_bolt_baseline, open_in_full_baseline, other_houses_baseline, offline_pin_baseline, open_in_new_baseline, open_with_baseline, outbound_baseline, opacity_baseline, outbond_baseline, outbox_baseline, outlet_baseline, output_baseline, output_outlined, output_rounded, output_sharp, no_encryption_gmailerrorred_baseline, notification_important_baseline, notifications_active_baseline, notifications_paused_baseline, not_listed_location_baseline, notifications_none_baseline, notifications_off_baseline, near_me_disabled_baseline, nightlight_round_baseline, notification_add_baseline, notifications_on_baseline, navigate_before_baseline, no_meals_ouline_baseline, no_meeting_room_baseline, network_locked_baseline, no_photography_baseline, nordic_walking_baseline, not_accessible_baseline, not_interested_baseline, nature_people_baseline, navigate_next_baseline, network_check_baseline, night_shelter_baseline, no_encryption_baseline, notifications_baseline, now_wallpaper_baseline, nearby_error_baseline, network_cell_baseline, network_ping_baseline, network_ping_outlined, network_wifi_baseline, new_releases_baseline, network_ping_rounded, nights_stay_baseline, no_accounts_baseline, no_backpack_baseline, no_stroller_baseline, no_transfer_baseline, not_started_baseline, now_widgets_baseline, navigation_baseline, nearby_off_baseline, nightlight_baseline, no_luggage_baseline, north_east_baseline, north_west_baseline, network_ping_sharp, new_label_baseline, newspaper_baseline, newspaper_outlined, next_plan_baseline, next_week_baseline, nightlife_baseline, no_drinks_baseline, newspaper_rounded, no_flash_baseline, no_meals_baseline, note_add_baseline, note_alt_baseline, near_me_baseline, no_cell_baseline, no_food_baseline, numbers_baseline, numbers_outlined, nature_baseline, newspaper_sharp, no_sim_baseline, numbers_rounded, north_baseline, notes_baseline, note_baseline, numbers_sharp, nat_baseline, nfc_baseline, miscellaneous_services_baseline, mark_unread_chat_alt_baseline, mark_unread_chat_alt_outlined, motion_photos_paused_baseline, mark_unread_chat_alt_rounded, media_bluetooth_off_baseline, mobile_screen_share_baseline, motion_photos_pause_baseline, markunread_mailbox_baseline, media_bluetooth_on_baseline, motion_photos_auto_baseline, mark_email_unread_baseline, mark_unread_chat_alt_sharp, medication_liquid_baseline, medication_liquid_outlined, messenger_outline_baseline, missed_video_call_baseline, mode_edit_outline_baseline, monochrome_photos_baseline, motion_photos_off_baseline, mark_chat_unread_baseline, medical_services_baseline, medication_liquid_rounded, mic_external_off_baseline, motion_photos_on_baseline, multitrack_audio_baseline, my_library_books_baseline, my_library_music_baseline, manage_accounts_baseline, mark_email_read_baseline, mic_external_on_baseline, mobile_friendly_baseline, monetization_on_baseline, money_off_csred_baseline, multiline_chart_baseline, maps_home_work_baseline, mark_as_unread_baseline, mark_chat_read_baseline, medication_liquid_sharp, mobiledata_off_baseline, mode_of_travel_baseline, mode_of_travel_outlined, model_training_baseline, monitor_weight_baseline, movie_creation_baseline, my_library_add_baseline, manage_search_baseline, military_tech_baseline, mode_of_travel_rounded, monitor_heart_baseline, monitor_heart_outlined, move_to_inbox_baseline, multiple_stop_baseline, mail_outline_baseline, meeting_room_baseline, mode_comment_baseline, mode_standby_baseline, monitor_heart_rounded, movie_filter_baseline, mode_of_travel_sharp, music_video_baseline, my_location_baseline, markunread_baseline, medication_baseline, merge_type_baseline, mobile_off_baseline, mode_night_baseline, monitor_heart_sharp, more_horiz_baseline, motorcycle_baseline, music_note_baseline, mediation_baseline, menu_book_baseline, menu_open_baseline, messenger_baseline, microwave_baseline, mode_edit_baseline, money_off_baseline, more_time_baseline, more_vert_baseline, move_down_baseline, move_down_outlined, music_off_baseline, maps_ugc_baseline, maximize_baseline, mic_none_baseline, minimize_baseline, mood_bad_baseline, move_down_rounded, message_baseline, mic_off_baseline, monitor_baseline, move_up_baseline, move_up_outlined, margin_baseline, memory_baseline, mosque_baseline, mosque_outlined, move_down_sharp, move_up_rounded, moving_baseline, museum_baseline, masks_baseline, merge_baseline, merge_outlined, money_baseline, moped_baseline, mosque_rounded, mouse_baseline, movie_baseline, mail_baseline, male_baseline, menu_baseline, merge_rounded, mode_baseline, mood_baseline, more_baseline, move_up_sharp, man_baseline, man_outlined, map_baseline, mic_baseline, mms_baseline, mosque_sharp, man_rounded, merge_sharp, mp_baseline, man_sharp, panorama_photosphere_select_baseline, panorama_horizontal_select_baseline, panorama_wide_angle_select_baseline, production_quantity_limits_baseline, playlist_add_check_circle_baseline, playlist_add_check_circle_outlined, panorama_vertical_select_baseline, photo_size_select_actual_baseline, playlist_add_check_circle_rounded, perm_device_information_baseline, phone_bluetooth_speaker_baseline, photo_size_select_large_baseline, photo_size_select_small_baseline, precision_manufacturing_baseline, picture_in_picture_alt_baseline, playlist_add_check_circle_sharp, published_with_changes_baseline, perm_contact_calendar_baseline, panorama_photosphere_baseline, pause_circle_outline_baseline, private_connectivity_baseline, private_connectivity_outlined, panorama_horizontal_baseline, panorama_wide_angle_baseline, pause_circle_filled_baseline, person_add_disabled_baseline, person_remove_alt_1_baseline, pest_control_rodent_baseline, play_circle_outline_baseline, playlist_add_circle_baseline, playlist_add_circle_outlined, private_connectivity_rounded, pause_presentation_baseline, photo_camera_front_baseline, picture_in_picture_baseline, play_circle_filled_baseline, playlist_add_check_baseline, playlist_add_circle_rounded, power_settings_new_baseline, panorama_fish_eye_baseline, panorama_vertical_baseline, perm_data_setting_baseline, person_pin_circle_baseline, photo_camera_back_baseline, pie_chart_outline_baseline, pivot_table_chart_baseline, portable_wifi_off_baseline, private_connectivity_sharp, panorama_fisheye_baseline, perm_contact_cal_baseline, perm_device_info_baseline, person_add_alt_1_baseline, play_circle_fill_baseline, playlist_add_circle_sharp, pending_actions_baseline, perm_camera_mic_baseline, personal_injury_baseline, phone_forwarded_baseline, phonelink_erase_baseline, phonelink_setup_baseline, playlist_remove_baseline, playlist_remove_outlined, people_outline_baseline, perm_phone_msg_baseline, perm_scan_wifi_baseline, person_add_alt_baseline, person_outline_baseline, personal_video_baseline, phone_callback_baseline, phone_disabled_baseline, phonelink_lock_baseline, phonelink_ring_baseline, picture_as_pdf_baseline, playlist_remove_rounded, pregnant_woman_baseline, present_to_all_baseline, print_disabled_baseline, perm_identity_baseline, person_remove_baseline, person_search_baseline, phone_android_baseline, phone_enabled_baseline, phone_in_talk_baseline, phonelink_off_baseline, photo_library_baseline, play_disabled_baseline, play_for_work_baseline, playlist_play_baseline, point_of_sale_baseline, priority_high_baseline, pan_tool_alt_baseline, pan_tool_alt_outlined, pause_circle_baseline, pest_control_baseline, phone_iphone_baseline, phone_locked_baseline, phone_missed_baseline, phone_paused_baseline, photo_camera_baseline, photo_filter_baseline, playlist_add_baseline, playlist_remove_sharp, price_change_baseline, pan_tool_alt_rounded, paragliding_baseline, photo_album_baseline, play_circle_baseline, play_lesson_baseline, power_input_baseline, price_check_baseline, privacy_tip_baseline, punch_clock_baseline, punch_clock_outlined, party_mode_baseline, pedal_bike_baseline, people_alt_baseline, perm_media_baseline, person_add_baseline, person_off_baseline, person_pin_baseline, pin_invoke_baseline, pin_invoke_outlined, plagiarism_baseline, play_arrow_baseline, psychology_baseline, public_off_baseline, punch_clock_rounded, pan_tool_alt_sharp, phonelink_baseline, piano_off_baseline, pie_chart_baseline, pin_invoke_rounded, power_off_baseline, pageview_baseline, pan_tool_baseline, panorama_baseline, password_baseline, payments_baseline, pentagon_baseline, pentagon_outlined, phishing_baseline, phishing_outlined, pin_drop_baseline, plumbing_baseline, plus_one_baseline, podcasts_baseline, polyline_baseline, polyline_outlined, portrait_baseline, post_add_baseline, punch_clock_sharp, push_pin_baseline, padding_baseline, palette_baseline, pattern_baseline, payment_baseline, pending_baseline, pentagon_rounded, percent_baseline, percent_outlined, phishing_rounded, pin_end_baseline, pin_end_outlined, pin_invoke_sharp, polyline_rounded, polymer_baseline, preview_baseline, publish_baseline, paypal_baseline, paypal_outlined, people_baseline, percent_rounded, person_baseline, pin_end_rounded, policy_baseline, public_baseline, pages_baseline, paste_baseline, pause_baseline, paypal_rounded, pentagon_sharp, phishing_sharp, phone_baseline, photo_baseline, piano_baseline, pinch_baseline, pinch_outlined, place_baseline, polyline_sharp, power_baseline, print_baseline, paid_baseline, park_baseline, percent_sharp, pets_baseline, pin_end_sharp, pinch_rounded, poll_baseline, pool_baseline, paypal_sharp, php_baseline, php_outlined, pin_baseline, pix_baseline, pix_outlined, php_rounded, pinch_sharp, pix_rounded, php_sharp, pix_sharp, quick_contacts_dialer_baseline, quick_contacts_mail_baseline, qr_code_scanner_baseline, question_answer_baseline, queue_play_next_baseline, query_builder_baseline, question_mark_baseline, question_mark_outlined, question_mark_rounded, query_stats_baseline, queue_music_baseline, question_mark_sharp, quickreply_baseline, qr_code_2_baseline, qr_code_baseline, queue_baseline, quora_baseline, quora_outlined, quiz_baseline, quora_rounded, quora_sharp, signal_wifi_statusbar_connected_no_internet_4_baseline, signal_cellular_connected_no_internet_4_bar_baseline, signal_cellular_connected_no_internet_0_bar_baseline, signal_wifi_connected_no_internet_4_baseline, sentiment_very_dissatisfied_baseline, signal_wifi_statusbar_4_bar_baseline, signal_wifi_statusbar_null_baseline, sentiment_very_satisfied_baseline, settings_input_component_baseline, settings_input_composite_baseline, settings_system_daydream_baseline, subdirectory_arrow_right_baseline, security_update_warning_baseline, sentiment_satisfied_alt_baseline, settings_backup_restore_baseline, subdirectory_arrow_left_baseline, sentiment_dissatisfied_baseline, settings_accessibility_baseline, settings_input_antenna_baseline, shopping_cart_checkout_baseline, shopping_cart_checkout_outlined, signal_cellular_no_sim_baseline, signal_cellular_nodata_baseline, signal_wifi_4_bar_lock_baseline, stay_current_landscape_baseline, stay_primary_landscape_baseline, screen_lock_landscape_baseline, screen_search_desktop_baseline, settings_applications_baseline, settings_input_svideo_baseline, shopping_cart_checkout_rounded, signal_cellular_4_bar_baseline, signal_cellular_0_bar_baseline, star_border_purple500_baseline, stay_current_portrait_baseline, stay_primary_portrait_baseline, screen_lock_portrait_baseline, screen_lock_rotation_baseline, security_update_good_baseline, signal_cellular_null_baseline, store_mall_directory_baseline, send_time_extension_baseline, send_time_extension_outlined, sentiment_satisfied_baseline, settings_brightness_baseline, settings_input_hdmi_baseline, shopping_cart_checkout_sharp, signal_cellular_alt_baseline, signal_cellular_off_baseline, sports_martial_arts_baseline, sports_martial_arts_outlined, send_time_extension_rounded, settings_bluetooth_baseline, share_arrival_time_baseline, sports_martial_arts_rounded, sports_motorsports_baseline, stacked_line_chart_baseline, sentiment_neutral_baseline, settings_ethernet_baseline, settings_overscan_baseline, signal_wifi_4_bar_baseline, signal_wifi_0_bar_baseline, sim_card_download_baseline, slow_motion_video_baseline, speaker_notes_off_baseline, sports_basketball_baseline, sports_gymnastics_baseline, sports_gymnastics_outlined, sports_volleyball_baseline, stacked_bar_chart_baseline, stop_screen_share_baseline, self_improvement_baseline, send_and_archive_baseline, send_time_extension_sharp, settings_display_baseline, settings_suggest_baseline, sports_gymnastics_rounded, sports_martial_arts_sharp, screen_rotation_baseline, security_update_baseline, settings_remote_baseline, shopping_basket_baseline, signal_wifi_bad_baseline, signal_wifi_off_baseline, social_distance_baseline, space_dashboard_baseline, sports_baseball_baseline, sports_football_baseline, sports_handball_baseline, strikethrough_s_baseline, safety_divider_baseline, send_to_mobile_baseline, settings_phone_baseline, settings_power_baseline, settings_voice_baseline, share_location_baseline, sim_card_alert_baseline, snippet_folder_baseline, sports_cricket_baseline, sports_esports_baseline, sports_gymnastics_sharp, sports_kabaddi_baseline, star_purple500_baseline, satellite_alt_baseline, satellite_alt_outlined, schedule_send_baseline, sd_card_alert_baseline, sensor_window_baseline, settings_cell_baseline, shopping_cart_baseline, shutter_speed_baseline, skateboarding_baseline, skip_previous_baseline, smart_display_baseline, smoking_rooms_baseline, sort_by_alpha_baseline, south_america_baseline, south_america_outlined, speaker_group_baseline, speaker_notes_baseline, speaker_phone_baseline, sports_hockey_baseline, sports_soccer_baseline, sports_tennis_baseline, sticky_note_2_baseline, satellite_alt_rounded, saved_search_baseline, scatter_plot_baseline, screen_share_baseline, scuba_diving_baseline, scuba_diving_outlined, shopping_bag_baseline, smart_button_baseline, smart_screen_baseline, snowboarding_baseline, soup_kitchen_baseline, soup_kitchen_outlined, south_america_rounded, sports_rugby_baseline, sports_score_baseline, star_outline_baseline, scuba_diving_rounded, sensor_door_baseline, sensors_off_baseline, shield_moon_baseline, shield_moon_outlined, snowshoeing_baseline, soup_kitchen_rounded, splitscreen_baseline, sports_golf_baseline, square_foot_baseline, star_border_baseline, stop_circle_baseline, satellite_alt_sharp, scoreboard_baseline, scoreboard_outlined, screenshot_baseline, sd_storage_baseline, search_off_baseline, select_all_baseline, shield_moon_rounded, short_text_baseline, show_chart_baseline, shuffle_on_baseline, single_bed_baseline, smartphone_baseline, smoke_free_baseline, sms_failed_baseline, snowmobile_baseline, south_america_sharp, south_east_baseline, south_west_baseline, spellcheck_baseline, sports_bar_baseline, sports_mma_baseline, ssid_chart_baseline, ssid_chart_outlined, storefront_baseline, straighten_baseline, streetview_baseline, sanitizer_baseline, satellite_baseline, scoreboard_rounded, scuba_diving_sharp, skip_next_baseline, slideshow_baseline, smart_toy_baseline, soup_kitchen_sharp, space_bar_baseline, ssid_chart_rounded, star_half_baseline, star_rate_baseline, save_alt_baseline, schedule_baseline, security_baseline, set_meal_baseline, settings_baseline, shield_moon_sharp, shop_two_baseline, shortcut_baseline, signpost_baseline, signpost_outlined, sim_card_baseline, sledding_baseline, snapchat_baseline, snapchat_outlined, straight_baseline, straight_outlined, stroller_baseline, sailing_baseline, save_as_baseline, save_as_outlined, savings_baseline, scanner_baseline, science_baseline, scoreboard_sharp, sd_card_baseline, segment_baseline, sensors_baseline, shopify_baseline, shopify_outlined, shuffle_baseline, signpost_rounded, snapchat_rounded, snowing_baseline, speaker_baseline, ssid_chart_sharp, stadium_baseline, stadium_outlined, storage_baseline, straight_rounded, subject_baseline, save_as_rounded, schema_baseline, school_baseline, search_baseline, shield_baseline, shop_2_baseline, shopify_rounded, shower_baseline, snooze_baseline, source_baseline, sports_baseline, square_baseline, square_outlined, stadium_rounded, stairs_baseline, stream_baseline, scale_baseline, scale_outlined, score_baseline, share_baseline, signpost_sharp, snapchat_sharp, south_baseline, speed_baseline, spoke_baseline, spoke_outlined, square_rounded, stars_baseline, start_baseline, start_outlined, store_baseline, storm_baseline, straight_sharp, style_baseline, save_as_sharp, save_baseline, scale_rounded, sell_baseline, send_baseline, shop_baseline, shopify_sharp, sick_baseline, soap_baseline, sort_baseline, spoke_rounded, stadium_sharp, star_baseline, start_rounded, stop_baseline, sip_baseline, sms_baseline, spa_baseline, square_sharp, scale_sharp, sd_baseline, spoke_sharp, start_sharp, radio_button_unchecked_baseline, remove_circle_outline_baseline, rotate_90_degrees_ccw_baseline, radio_button_checked_baseline, remove_shopping_cart_baseline, replay_circle_filled_baseline, report_gmailerrorred_baseline, rotate_90_degrees_cw_baseline, rotate_90_degrees_cw_outlined, rotate_90_degrees_cw_rounded, running_with_errors_baseline, restore_from_trash_baseline, real_estate_agent_baseline, record_voice_over_baseline, remove_from_queue_baseline, rotate_90_degrees_cw_sharp, radio_button_off_baseline, remove_moderator_baseline, room_preferences_baseline, roundabout_right_baseline, roundabout_right_outlined, radio_button_on_baseline, reduce_capacity_baseline, restaurant_menu_baseline, roundabout_left_baseline, roundabout_left_outlined, roundabout_right_rounded, remove_red_eye_baseline, report_problem_baseline, roller_skating_baseline, roller_skating_outlined, roundabout_left_rounded, rounded_corner_baseline, railway_alert_baseline, recent_actors_baseline, remove_circle_baseline, repeat_one_on_baseline, request_quote_baseline, rocket_launch_baseline, rocket_launch_outlined, roller_skating_rounded, roundabout_right_sharp, r_mobiledata_baseline, ramen_dining_baseline, receipt_long_baseline, request_page_baseline, restore_page_baseline, rocket_launch_rounded, room_service_baseline, rotate_right_baseline, roundabout_left_sharp, rate_review_baseline, remember_me_baseline, remove_done_baseline, restart_alt_baseline, ring_volume_baseline, roller_skating_sharp, rotate_left_baseline, rule_folder_baseline, ramp_right_baseline, ramp_right_outlined, repeat_one_baseline, report_off_baseline, restaurant_baseline, rocket_launch_sharp, run_circle_baseline, ramp_left_baseline, ramp_left_outlined, ramp_right_rounded, read_more_baseline, recommend_baseline, rectangle_baseline, rectangle_outlined, recycling_baseline, recycling_outlined, repeat_on_baseline, replay_10_baseline, replay_30_baseline, reply_all_baseline, rice_bowl_baseline, rv_hookup_baseline, ramp_left_rounded, rectangle_rounded, recycling_rounded, replay_5_baseline, reset_tv_baseline, rss_feed_baseline, ramp_right_sharp, raw_off_baseline, receipt_baseline, refresh_baseline, reorder_baseline, restore_baseline, reviews_baseline, roofing_baseline, ramp_left_sharp, raw_on_baseline, rectangle_sharp, recycling_sharp, reddit_baseline, reddit_outlined, redeem_baseline, remove_baseline, repeat_baseline, replay_baseline, report_baseline, rocket_baseline, rocket_outlined, router_baseline, rowing_baseline, radar_baseline, radio_baseline, reddit_rounded, reply_baseline, rocket_rounded, route_baseline, route_outlined, redo_baseline, room_baseline, route_rounded, rsvp_baseline, rule_baseline, reddit_sharp, rocket_sharp, rtt_baseline, route_sharp, update_disabled_baseline, u_turn_right_baseline, u_turn_right_outlined, u_turn_left_baseline, u_turn_left_outlined, u_turn_right_rounded, unfold_less_baseline, unfold_more_baseline, unpublished_baseline, unsubscribe_baseline, upload_file_baseline, u_turn_left_rounded, u_turn_right_sharp, unarchive_baseline, u_turn_left_sharp, umbrella_baseline, upcoming_baseline, upgrade_baseline, usb_off_baseline, update_baseline, upload_baseline, undo_baseline, usb_baseline, transfer_within_a_station_baseline, text_rotation_angledown_baseline, text_rotation_angleup_baseline, text_rotate_vertical_baseline, text_rotation_down_baseline, text_rotation_none_baseline, thumb_down_off_alt_baseline, transit_enterexit_baseline, turn_slight_right_baseline, turn_slight_right_outlined, table_restaurant_baseline, table_restaurant_outlined, thumb_up_off_alt_baseline, tips_and_updates_baseline, tips_and_updates_outlined, trending_neutral_baseline, turn_sharp_right_baseline, turn_sharp_right_outlined, turn_slight_left_baseline, turn_slight_left_outlined, turn_slight_right_rounded, table_restaurant_rounded, temple_buddhist_baseline, temple_buddhist_outlined, thermostat_auto_baseline, timer_10_select_baseline, tips_and_updates_rounded, turn_sharp_left_baseline, turn_sharp_left_outlined, turn_sharp_right_rounded, turn_slight_left_rounded, tab_unselected_baseline, tablet_android_baseline, takeout_dining_baseline, temple_buddhist_rounded, text_rotate_up_baseline, theater_comedy_baseline, thumb_down_alt_baseline, thumbs_up_down_baseline, timer_3_select_baseline, travel_explore_baseline, turn_sharp_left_rounded, turn_slight_right_sharp, table_restaurant_sharp, text_decrease_baseline, text_decrease_outlined, text_increase_baseline, text_increase_outlined, time_to_leave_baseline, tips_and_updates_sharp, track_changes_baseline, trending_down_baseline, trending_flat_baseline, turn_sharp_right_sharp, turn_slight_left_sharp, turned_in_not_baseline, tap_and_play_baseline, temple_buddhist_sharp, temple_hindu_baseline, temple_hindu_outlined, text_decrease_rounded, text_increase_rounded, text_snippet_baseline, thumb_up_alt_baseline, turn_sharp_left_sharp, table_chart_baseline, temple_hindu_rounded, text_fields_baseline, text_format_baseline, tire_repair_baseline, tire_repair_outlined, transgender_baseline, trending_up_baseline, trip_origin_baseline, two_wheeler_baseline, table_rows_baseline, table_view_baseline, tablet_mac_baseline, taxi_alert_baseline, text_decrease_sharp, text_increase_sharp, thermostat_baseline, thumb_down_baseline, tire_repair_rounded, toggle_off_baseline, turn_right_baseline, turn_right_outlined, table_bar_baseline, table_bar_outlined, tag_faces_baseline, temple_hindu_sharp, timelapse_baseline, timer_off_baseline, toggle_on_baseline, touch_app_baseline, transform_baseline, translate_baseline, turn_left_baseline, turn_left_outlined, turn_right_rounded, turned_in_baseline, table_bar_rounded, task_alt_baseline, telegram_baseline, telegram_outlined, terminal_baseline, terminal_outlined, theaters_baseline, thumb_up_baseline, timeline_baseline, timer_10_baseline, tire_repair_sharp, tonality_baseline, tungsten_baseline, turn_left_rounded, telegram_rounded, terminal_rounded, terrain_baseline, textsms_baseline, texture_baseline, timer_3_baseline, traffic_baseline, turn_right_sharp, table_bar_sharp, tablet_baseline, tiktok_baseline, tiktok_outlined, turn_left_sharp, tv_off_baseline, tapas_baseline, telegram_sharp, terminal_sharp, tiktok_rounded, timer_baseline, title_baseline, today_baseline, token_baseline, token_outlined, topic_baseline, train_baseline, task_baseline, token_rounded, toll_baseline, tour_baseline, toys_baseline, tram_baseline, tune_baseline, tab_baseline, tag_baseline, tiktok_sharp, toc_baseline, try_baseline, tty_baseline, token_sharp, tv_baseline, system_security_update_warning_baseline, system_security_update_good_baseline, switch_access_shortcut_add_baseline, switch_access_shortcut_add_outlined, switch_access_shortcut_add_rounded, switch_access_shortcut_add_sharp, supervised_user_circle_baseline, swap_horizontal_circle_baseline, switch_access_shortcut_baseline, switch_access_shortcut_outlined, system_security_update_baseline, switch_access_shortcut_rounded, swap_vertical_circle_baseline, switch_access_shortcut_sharp, supervisor_account_baseline, system_update_alt_baseline, swap_vert_circle_baseline, system_update_tv_baseline, swipe_right_alt_baseline, swipe_right_alt_outlined, surround_sound_baseline, swipe_down_alt_baseline, swipe_down_alt_outlined, swipe_left_alt_baseline, swipe_left_alt_outlined, swipe_right_alt_rounded, swipe_vertical_baseline, swipe_vertical_outlined, switch_account_baseline, subscriptions_baseline, subtitles_off_baseline, sunny_snowing_baseline, support_agent_baseline, swipe_down_alt_rounded, swipe_left_alt_rounded, swipe_vertical_rounded, switch_camera_baseline, sync_disabled_baseline, system_update_baseline, swipe_right_alt_sharp, swipe_up_alt_baseline, swipe_up_alt_outlined, switch_right_baseline, switch_video_baseline, sync_problem_baseline, superscript_baseline, swipe_down_alt_sharp, swipe_left_alt_sharp, swipe_right_baseline, swipe_right_outlined, swipe_up_alt_rounded, swipe_vertical_sharp, switch_left_baseline, swap_calls_baseline, swap_horiz_baseline, swipe_down_baseline, swipe_down_outlined, swipe_left_baseline, swipe_left_outlined, swipe_right_rounded, subscript_baseline, subtitles_baseline, summarize_baseline, swap_vert_baseline, swipe_down_rounded, swipe_left_rounded, swipe_up_alt_sharp, synagogue_baseline, synagogue_outlined, sync_lock_baseline, sync_lock_outlined, swipe_right_sharp, swipe_up_baseline, swipe_up_outlined, synagogue_rounded, sync_alt_baseline, sync_lock_rounded, support_baseline, surfing_baseline, swipe_down_sharp, swipe_left_sharp, swipe_up_rounded, subway_baseline, synagogue_sharp, sync_lock_sharp, sunny_baseline, swipe_baseline, swipe_up_sharp, sync_baseline, youtube_searched_for_baseline, yard_baseline, wifi_tethering_error_rounded_baseline, wifi_protected_setup_baseline, wifi_tethering_error_baseline, wifi_tethering_error_outlined, wifi_tethering_off_baseline, workspaces_outline_baseline, wallet_membership_baseline, wheelchair_pickup_baseline, wifi_tethering_error_sharp, workspace_premium_baseline, workspace_premium_outlined, workspaces_filled_baseline, workspace_premium_rounded, wallet_giftcard_baseline, waterfall_chart_baseline, wb_incandescent_baseline, wifi_calling_3_baseline, wifi_tethering_baseline, workspace_premium_sharp, wrong_location_baseline, wallet_travel_baseline, warning_amber_baseline, wb_iridescent_baseline, wb_twighlight_baseline, web_asset_off_baseline, where_to_vote_baseline, wifi_password_baseline, wifi_password_outlined, water_damage_baseline, wifi_calling_baseline, wifi_channel_baseline, wifi_channel_outlined, wifi_password_rounded, woo_commerce_baseline, woo_commerce_outlined, work_outline_baseline, watch_later_baseline, waving_hand_baseline, waving_hand_outlined, wb_twilight_baseline, web_stories_baseline, wifi_channel_rounded, woo_commerce_rounded, water_drop_baseline, water_drop_outlined, waving_hand_rounded, wifi_password_sharp, workspaces_baseline, wallpaper_baseline, warehouse_baseline, warehouse_outlined, watch_off_baseline, watch_off_outlined, water_drop_rounded, wb_cloudy_baseline, web_asset_baseline, wifi_channel_sharp, wifi_find_baseline, wifi_find_outlined, wifi_lock_baseline, woo_commerce_sharp, wordpress_baseline, wordpress_outlined, wrap_text_baseline, warehouse_rounded, watch_off_rounded, waving_hand_sharp, wb_shade_baseline, wb_sunny_baseline, whatsapp_baseline, whatsapp_outlined, whatshot_baseline, wifi_find_rounded, wifi_off_baseline, wine_bar_baseline, wordpress_rounded, work_off_baseline, warning_baseline, water_drop_sharp, wb_auto_baseline, webhook_baseline, webhook_outlined, weekend_baseline, whatsapp_rounded, widgets_baseline, wysiwyg_baseline, warehouse_sharp, watch_off_sharp, webhook_rounded, wechat_baseline, wechat_outlined, wifi_find_sharp, window_baseline, wordpress_sharp, watch_baseline, water_baseline, waves_baseline, wechat_rounded, whatsapp_sharp, woman_baseline, woman_outlined, wash_baseline, webhook_sharp, west_baseline, wifi_baseline, woman_rounded, work_baseline, web_baseline, wechat_sharp, wc_baseline, woman_sharp, vertical_align_bottom_baseline, vertical_align_center_baseline, vertical_distribute_baseline, videogame_asset_off_baseline, vertical_align_top_baseline, video_camera_front_baseline, volunteer_activism_baseline, video_camera_back_baseline, video_collection_baseline, view_comfortable_baseline, view_compact_alt_baseline, view_compact_alt_outlined, videogame_asset_baseline, view_compact_alt_rounded, volume_down_alt_baseline, vertical_split_baseline, video_settings_baseline, view_comfy_alt_baseline, view_comfy_alt_outlined, visibility_off_baseline, voice_over_off_baseline, verified_user_baseline, video_library_baseline, view_carousel_baseline, view_comfy_alt_rounded, view_compact_alt_sharp, view_headline_baseline, view_timeline_baseline, view_timeline_outlined, vaping_rooms_baseline, vaping_rooms_outlined, video_stable_baseline, videocam_off_baseline, view_compact_baseline, view_sidebar_baseline, view_timeline_rounded, vaping_rooms_rounded, video_label_baseline, view_agenda_baseline, view_column_baseline, view_comfy_alt_sharp, view_kanban_baseline, view_kanban_outlined, view_module_baseline, view_stream_baseline, volume_down_baseline, volume_mute_baseline, vpn_key_off_baseline, vpn_key_off_outlined, video_call_baseline, video_file_baseline, video_file_outlined, view_array_baseline, view_comfy_baseline, view_in_ar_baseline, view_kanban_rounded, view_quilt_baseline, view_timeline_sharp, visibility_baseline, voice_chat_baseline, volume_off_baseline, vpn_key_off_rounded, vape_free_baseline, vape_free_outlined, vaping_rooms_sharp, vibration_baseline, video_file_rounded, view_cozy_baseline, view_cozy_outlined, view_list_baseline, view_week_baseline, voicemail_baseline, volume_up_baseline, vaccines_baseline, vaccines_outlined, vape_free_rounded, verified_baseline, videocam_baseline, view_cozy_rounded, view_day_baseline, view_kanban_sharp, vignette_baseline, vpn_key_off_sharp, vpn_lock_baseline, vaccines_rounded, video_file_sharp, vpn_key_baseline, vape_free_sharp, view_cozy_sharp, vrpano_baseline, vaccines_sharp, villa_baseline, zoom_out_map_baseline, zoom_in_map_baseline, zoom_in_map_outlined, zoom_in_map_rounded, zoom_in_map_sharp, zoom_out_baseline, zoom_in_baseline}
❌ new codepoints file does not contain all 7315 existing codepoints. Missing: {baby_changing_station, battery_charging_full, browser_not_supported, bluetooth_connected, bluetooth_searching, bluetooth_disabled, branding_watermark, border_horizontal, brightness_medium, batch_prediction, bookmark_outline, breakfast_dining, battery_unknown, bluetooth_audio, bluetooth_drive, bookmark_border, bookmark_remove, border_vertical, brightness_auto, brightness_high, business_center, bedroom_parent, bookmark_added, brightness_low, bakery_dining, battery_alert, battery_saver, bedroom_child, block_flipped, blur_circular, border_bottom, brunch_dining, backup_table, battery_full, beach_access, bedroom_baby, bike_scooter, bookmark_add, border_clear, border_color, border_inner, border_outer, border_right, border_style, brightness_5, brightness_4, brightness_1, brightness_7, brightness_6, brightness_3, brightness_2, broken_image, bubble_chart, build_circle, battery_std, blur_linear, book_online, border_left, border_all, border_top, bug_report, burst_mode, backspace, bar_chart, bloodtype, bluetooth, bookmarks, bus_alert, backpack, bathroom, beenhere, blur_off, bookmark, bungalow, business, balcony, bathtub, bedtime, biotech, blender, blur_on, backup, ballot, badge, bento, block, brush, build, bolt, book, bed, airline_seat_individual_suite, airline_seat_legroom_reduced, airline_seat_legroom_normal, airline_seat_recline_normal, airline_seat_legroom_extra, airline_seat_recline_extra, airline_seat_flat_angled, align_horizontal_center, account_balance_wallet, align_horizontal_right, arrow_drop_down_circle, airplanemode_inactive, align_horizontal_left, align_vertical_bottom, align_vertical_center, admin_panel_settings, assignment_turned_in, assistant_navigation, add_photo_alterna…

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[adcef91015...](https://github.com/mrakgr/The-Spiral-Language/commit/adcef91015166d8198a9c83d4e395510eea24899)
#### Thursday 2021-12-23 12:17:29 by Marko Grdinić

"9:50am. The internet is down. Don't tell me the budget is spent already?

I actually must have woken up an hour or two ago and just spent my time in thought.

I've decided - if Spiral gets no bite, and in the future I am forced to finance all my research out of my own pocket, I am going to leave the public work done here as it is and take the genetic programming work, the AI backends and work on the language private.

Hmmmm, it is still not back. Let me change it to the slow line.

10:25am. Ok, I am almost ready to start. Let me chill a bit more and then I'll get on with it.

10:50am. Let me start. It is time to get busy with the HDRI. I really needed a break after yesterday. I finished at 9pm after all. Let me not rush myself and do it one step at a time. I had a good long morning break.

I still need some time to settle my emotions, but it will happen over time.

I am thinking what I am going to do that AI chip, and something like doing a ref counted interpreter for the sake of GP research would be a PhD difficulty project for the average researcher. I myself could do it in a month or two, but imagine anyone trying to do this in C or even Assembly. It would be very difficult.

This is providence. My programming skills couldn't get me to my goal directly, but I'll get a reward for my language work eventually. Spiral could be a good for a lot of things, but making the AI chip into an oracle that will give me the true ML algorithms is something it is uniquely suited for. I am going to get divine feel of inspiration like in 2013 when I first came to an understanding of the self improvement loop once again.

But today, I will prove my will through art.

11:05am. Maybe I will be done with the HDRI. Maybe tomorrow. And maybe the day after. It does not matter. The time is going to get invested in it.

First of all, I need the basics. Let me make a jewel, a simple 6 vertex object. Then I will think about how distribut it around a shell of some other object.

This is simple, but I do not have any experience with geometry nodes. I've played with shaders so I can find my way around them now, but I've only watched tutorials for geometry nodes.

11:15am. I just about managed to remember that it is possible to drag the object from the collection window into the node window. That saves me doing the object info node.

11:20am. Oh, wow, this actually went a lot smoother than it would.

I used the Instance on Points node, connected the Group Input to Points, and the shard to the instance. And I passed that the output and as a result I have the shard on all the sphere points.

11:35am. I am trying to get my bearings. Geometry nodes have textures. They can even distribute volume to points. This stuff is powerful.

11:40am. How do I randomize the points?

Let me take a short break here.

12pm. Let me resume, I had to run. I should take a longer break here, but I want to grind at it for a while longer. Right now I am not doing much, and I am seemingly wasting time, but this kind of practice is important to internalize the material.

12:05pm. I had some time to think. If the problem was just to randomize the positions, I could use subdivide on the original mesh and then use the fractal option to make it noisy.

But I also want to randomize the rotations. I can only do that in geometry nodes. That having said, the random value option is just for scalars. it has the ID option which I am guessing could be used to generate a bunch of them, but I do not know how combine the scalar socket with geometry socket that vectors use.

I do not know. I am going to have to watch some tuts on this. How do I add noise to instance positions and rotations? That is the question. Let me start by searching for searching for...

https://www.youtube.com/results?search_query=geometry+node+random

https://www.youtube.com/playlist?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB

This is a whole series on just geometry nodes. Given what I am working on, this might be a good idea to go through. Now that I have an actual use case in mind, I'd be really motivated to learn this.

https://www.youtube.com/watch?v=KntGPD1k7v0
07-Points and Instancing -Geometry Nodes( Fields) For Beginners / Blender 3.0

Let me start near the end since that is what Google gave me.

https://youtu.be/KntGPD1k7v0?t=185

He already went beyond what I could think of. Those speed tutorials are one thing, but these in depth courses are really valuable. Programming is one thing, but Blender really goes well with video for obvious reasons. These Youtube videos are a godsend. Imagine trying to learn Blender without them, I'd never get anywhere.

https://youtu.be/KntGPD1k7v0?t=302

Ahhh, right. I could use the noise texture to randomize the points. Why didn't I think of that?

He is working really fast here. Instead of adding the position to the Musgrave texture, he could have plugged it in directly into it.

https://youtu.be/KntGPD1k7v0?t=374

I have everything I need here. Let me give it a try.

12:50pm. Oh, I got a good effect. I quite like this. Adding the noise texture to the position offset is the way to go. Since 3d noise texture duplicates are equivalent I used the 4d one for rotation.

1pm. I've parameterized the size as well using the map range node.

1:05pm. If I am to describe it, right now it looks like an asteroid field wrapped in a sphere. This is quite good.

1:10pm. I am an easy person to please. I am just stading here in admiration of my own work. This was a really simple task, and I've conquered it. The larger shards are quite dominant, but not overbearing. I'll want to add more spheres. I need more smaller shards to populate the scenery. Maybe I'll add a few big ones by hand.

1:15pm. Let me stop here. It is time for breakfast. In honor of finishing this first step, I should watch the other geometry nodes videos from the course.

Though before that, I should just finish this project. It won't be hard at all. And going through course after that will allow me to reconsider my choices in light of new knowledge afterwards. That will be the best way to learn the material."

---
## [cloudflare/wrangler2](https://github.com/cloudflare/wrangler2)@[78cd0804de...](https://github.com/cloudflare/wrangler2/commit/78cd0804def1a3246f8a4f6b1695bd91e81c1ad1)
#### Thursday 2021-12-23 15:06:38 by Sunil Pai

implement custom builds, for `dev` and `publish` (#149)

* implement custom builds, for `dev` and `publish`

The code here is a bit jank, but we should probably refactor the way we pass arguments to dev and publish to 'fix' it properly. Anyway.

This PR adds custom builds to wrangler2 (https://developers.cloudflare.com/workers/cli-wrangler/configuration#build).
- In `wrangler.toml`, you can configure `build.command` and `build.cwd` and it'll be called before `publish` or `dev`. There's some discussion to be had whether we're going to deprecate this config commands, but we'll support it until then anyway.
- We _don't_ support `build.watch_dir`. We could, and I'm happy to add it after we discuss; but the idea is that watching shouldn't be wrangler's responsibility (which we've already broken with plain `dev`, and `pages dev`, so maybe we're wrong)
- You can pass the command after a last `--` in the cli (no support for `cwd` there). eg - `wrangler dev output/index.js -- some-build-command --out output/index.js`.

* Add a changeset

* fix lint error

* update snapshot tests

* remove `--`, add `watch_dir`

- removed the `--` option. We should have documentation showing how to do this with bash etc.
- Added support for `watch_dir`
- also added a definition for running tests from the root because it was annoying me to keep changing dirs to run tests

* log the name of the file that changed during a custom build

---
## [HanshenWang/project-isidore](https://github.com/HanshenWang/project-isidore)@[e09c22b938...](https://github.com/HanshenWang/project-isidore/commit/e09c22b938c44f144289af668cfc7cdb7e244603)
#### Thursday 2021-12-23 16:32:47 by Hanshen Wang

Docs: Change License from LGPL 3.0 to AGPL 3.0.

Moving from weak copyleft to network protective copyleft.

Copyleft v. Permissive Licensing Rationale:
===========================================

"And you shall know the truth: and the truth shall make you free."

Free to do what? To know that adhering to the Truth means doing what one ought,
not whatever our fallen nature pleases. Whether from first principles or
experience, we know that human law must curtail behaviors when man fails to obey
the Truth and use his inviolable free will to say no to what is good, beautiful
and true. And the law must remain just when doing so, defined in the words of
the Thomists to mean "rendering to each his due".

Simply put, permissive licenses gives the developer the choice to restrict the
freedom of the end users. What freedoms?

From the FSF,

1. the freedom to use the software for any purpose,
2. the freedom to change the software to suit your needs,
3. the freedom to share the software with your friends and neighbors, and
4. the freedom to share the changes you make.

Freely you have received, and freely you must give. To have enjoyed these
freedoms and then to deny them to others would be hypocritical. That cannot be
denied. The golden rule is indeed reciprocal, and from this property Copyleft
licenses have also been termed reciprocal licenses, or viral licenses.

The warranty disclaimer in both Copyleft and Permissive also curtails some
freedoms. The freedom to engage in bad faith and frivolous lawsuits. Reciprocal
licensing curtails the freedom to deny others the four freedoms you have
received.

Some common objections:
=======================

1. GPL software restricts user freedom in practice.

Some have correctly identified copyleft licenses impede recombining with closed
source software.

On the contrary, the fault does not lie with the free software
portion of the equation but rather the closed source software that has decided
to deny the four freedoms. It can be easily seen that if both sides of the
equation were closed source software, the impedance to the end user would be
even greater.

2. GPL software prevents monetization.

This stems from confusion regarding liberty and gratis. Please note that the
author is too influenced by Thomas Sowell and Friedrich Hayek to consider a
central command economy a good idea for us fallible humans. If there is a need
to pigeonhole me into a political party, I am fiscally and socially
conservative. Of course wealth is not an inherent evil, it feels silly to even
have to type that (it is written, man must eat by the sweat of his brow). Nor
was it ever my objective to bring Heaven unto earth and usher in a gratis
software utopia. Greed and intemperance are violations of natural law no matter
your political stripe.

On the contrary, It does not follow that reciprocal licensing disallows
commercialization. That would analogous to saying following the golden rule
makes for bad business.

This is not an either/or choice between copyleft and commercial licenses. It is
a both/and situation when one is able to include dual licenses. Reciprocity can
be in code or it can be in cash. Even projects solely GPL licensed have been
successfully monetized, though it can be argued the highest goal for such
projects was never a monetary one.

3. Reciprocity makes for bad business.

Wealth, as explained by Aquinas, is not the last end of man. In other words, not
an unqualified good. Not an end in of itself, but a means to an end. It makes no
sense on the individual or societal level to place wealth over justice. Unless
one has the position that a corrupt society is better than a just one.

On the contrary, anybody seriously placing monetary gain over justice would do
well to remember epistemology reminds us of our limited ability to see the
future. Indeed, 10 dead heroes are better men than 9 live cannibals. The flesh
may be weak, but it is ethical, proper and just to recognize such an ordering.
Only willful blindness and a misguided will reckons otherwise.

"Men are qualified for civil liberty in exact proportion to their disposition to
put moral chains upon their own appetites, in proportion as their love to
justice is above their rapacity,in proportion as their soundness and sobriety of
understanding is above their vanity and presumption,in proportion as they are
more disposed to listen to the counsels of the wise and good, in preference to
the flattery of knaves. Society cannot exist, unless a controlling power upon
will and appetite be placed somewhere; and the less of it there is within, the
more there must be without. It is ordained in the eternal constitution of
things, that men of intemperate minds cannot be free. Their passions forge their
fetters." Edmund Burke.

As repeated from the beginning of the commit message, Freedom is doing what you
ought, not what you want.

"And you shall know the truth: and the truth shall make you free."

4. My project will see less contributions due to current company policy

Out of all professions and trades, it is economists and businessmen who
understand most intimately that "there is no free lunch". As mentioned in
question 2, what is being objected here is the obligation to reciprocate. To
have their cake and eat it too, so to speak.

On the contrary, the goal for widespread adoption and therefore contributions is
a distinct goal from the preservation of the four freedoms. It is absolutely not
entirely separate, for any artifact deprived of human creative powers wilts and
dies (remember scientists shout "Eureka" and not "Genesis"). To that end, take
solace in the words of Thomas Paine, "Heaven knows how to put a proper price
upon its goods; and it would be strange indeed if so celestial an article as
FREEDOM should not be highly rated." A price worth paying.

If only this was a technical objection, but alas, here free software evangelists
share more in common with the Apostles than they are perhaps more comfortable
than admitting.

And so Burke, with much better rhetoric than I, expounds succinctly, "the less
of it there is within, the more there must be without." I somehow doubt the
FSF's existence is because Richard Stallman decided law was a more fulfilling
pursuit than his love of computer science. Michael Jackson got it right, be the
man in the mirror.

Compliance in layman's terms (not legal advice, please don't take it as such)
=============================================================================

To comply with the spirit of GPL is simple. If you do not modify the GPL
software by creating a derivative work but simply use it, you are under no
obligation to "reciprocate" by opening up your original work.

If you do modify the GPL software or create a derivative work by incorporating
the GPL code (possible because of the four freedoms extended to you), AND you do
NOT distribute the software, you are under no obligation to "reciprocate" by
opening up your original work. It's worth mentioning that this has been
interpreted to mean "internal use" within a company or organization is a-ok.

If you then proceed to distribute the derivative work, then the steps to
'reciprocate' is simple: release the source code of said derivative work so the
freedoms you have enjoyed may be enjoyed by our progeny. Here the AGPL adds to
the regular GPL clause 13, whereby distribution is taken to include interaction
through a remote network. The industry term is Software-as-a-Service.

Again, please consult a lawyer for advice. See also the precedence set by the
iText infringement claim by Bruno Lowagie.

Conclusion
==========

It's with such reasoning that I decided to license this project as AGPL-3.0 or
later. Now to be realistic, I foresee myself as the only developer for the
future. That does mean if I am convinced that a permissive license or the
0clause BSD pseudo public domain license is the best fit for this project, I am
all for switching. Please don't take this writing as the unilateral endorsement
of copyleft licenses for every single open source project.

And Godspeed to the FSF for the work they do.

---
## [oxidecomputer/hubris](https://github.com/oxidecomputer/hubris)@[184549a5f0...](https://github.com/oxidecomputer/hubris/commit/184549a5f075866067ef62eb693959850ee0d192)
#### Thursday 2021-12-23 17:00:58 by Cliff L. Biffle

Remove "standalone" build.

I introduced the standalone build early on as a way of quickly iterating
on a single task, without waiting for an entire image to build -- an
equivalent to `cargo check`. It has proven somewhat useful but also
breaks things.

- The standalone build does not build the actual code you'd ship, it
  instead configures the code in "standalone mode" where a bunch of
  stuff is arbitrarily stubbed out. This means that getting a successful
  standalone build tells you little about the real build.

- You can also _forget_ to put in the standalone magic, in which case
  your actual firmware builds, but then someone else doing a
  "standalone" build later faces a cryptic failure. This is why the
  standalone builds are run in CI -- to avoid this.

- As we introduce increasing levels of configurability in tasks,
  stubbing that configuration out in arbitrary ways is getting harder.
  When it was a matter of conditional compilation driven by board name,
  we could sprinkle in some `feature = "standalone"` hacks to guide it.
  As we move toward task slots and general configuration data in the
  app.toml, the main distinguishing feature of the standalone build --
  that it does not _have_ an app.toml -- starts to become a real pain.

My iteration workflow is currently served by `cargo xtask build`. I am
not aware of any reliable way of getting RLS/rust-analyzer to work on
Hubris, even _with_ the standalone build, so this shouldn't regress
editor support.

---
## [ncrecc/christmasspecial](https://github.com/ncrecc/christmasspecial)@[39163b95db...](https://github.com/ncrecc/christmasspecial/commit/39163b95db41d96cda158bef20d71522aa6b09d0)
#### Thursday 2021-12-23 17:45:17 by wibi

holy shit
- buster: fixed scrap crystal having no sfx
- buster: fixed revelation, in order: erroring, casting forward, and giving blessings to the enemy instead of you
- bert: fixed passives with effects in before start turn, like hot table, applying twice if you're warrior
- bert: added more passive equipment for A Bonus
- bert: added rainmaking for Something Large
- bert: marked slushie, sing, tree shake, stygian blade, divine grip, and luck omen as excludefromrandomlists
- bert: rewrote A Spell to specify it just has to be a *valid* witch spell
- bert: retooled A Flower to be a mana generator instead of just any mana equipment
- bert: added more mana-generating equipment for A Flower
- diane: fixed thief's generator never being shuffled
- diane: some if(simulation) wrapping for thief items
- diane: excluded nicholas from thief's episode due to gift bag giving thief too many items
- diane: main menu credits now point out that they're incomplete and player must beat an episode to view full credits
- diane: changed credits music to angelmoon's ice stage remix
- diane: tidied up the credits a bit
- diane: excluded bounty hunter from jester becasue making cards unavailable for reasons other than chain doesn't work right
- diane: fixed offset of christmas ghosts

---
## [thevandie/KirieStation](https://github.com/thevandie/KirieStation)@[0b5947a20f...](https://github.com/thevandie/KirieStation/commit/0b5947a20f2f218ad0e3f972add1e6ea5a90a9b5)
#### Thursday 2021-12-23 17:47:06 by Kirie Saito

6 MONTHS. SIX FUCKING MONTHS OF THIS CRAP I FINALLY FIXED IT (#376)

FUCK YOU

---
## [occivink/mpv](https://github.com/occivink/mpv)@[f6c81047fa...](https://github.com/occivink/mpv/commit/f6c81047fa5a9199084fa92327c41c6d8a16b059)
#### Thursday 2021-12-23 18:26:10 by wm4

player: do not fall back to a default track with explicit selections

Consider e.g. --aid=2 with a file that has only 1 track. Then it would
fall back to selecting track 1. Stop doing this. If no matching track is
found, this will not select any track now.

Note that the fingerprint stuff (track_layout_hash in the source)
prevents softens the impact of this change. Without the fingerprint,
playing a dual-audio file with the second track selected, and then a
single-audio file, would play the second file without audio. But the
fingerprint resets it due to differences in the track list.

Try to exhaustively document this and tricky interactions between the
other features. What a damn mess, I think it's simply cursed. Of course
it's still my fault.

See: #7608

---
## [BasedJellyfish11/Advent-of-Code-2021](https://github.com/BasedJellyfish11/Advent-of-Code-2021)@[914cd1caed...](https://github.com/BasedJellyfish11/Advent-of-Code-2021/commit/914cd1caed59b28ac8a88ea8ebdff6cfa22d1f79)
#### Thursday 2021-12-23 18:59:23 by PaumIsMe

The worst god damn piece of code I've written in my existance on this planet but fuck it I got my stars

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[14de5de38b...](https://github.com/mrakgr/The-Spiral-Language/commit/14de5de38b42cb3a6ae8176c29717be15b669548)
#### Thursday 2021-12-23 19:49:35 by Marko Grdinić

"2:10pm. Done with breakfast and chores. Let me chill just a bit and then I will resume. Since I did the first sphere my mood has gone up.

2:45pm. Let me start. I'll add a few more spheres.

Actually, let me do with just two. There is too much stuff in the sky now in fact. Let me add some fog.

3:20pm. How do I get Bloom effects in Cycles?

https://youtu.be/Tu3U6wD7lu4
Blender - Cycles Bloom and Glow (Blender 2.8)

https://youtu.be/Tu3U6wD7lu4?t=33

Huh does emission actually work in Eevee? If so that would be cool. I'll have to look that up.

https://youtu.be/SN8nJXn7CqI
How to add BLOOM effect in CYCLES with ease - Blender

Let me also watch this. Rather than get this effect in the compositor I'd like to know how to get it in regular view if possible.

https://youtu.be/SN8nJXn7CqI?t=51

I need to remember to turn up the number of bounces for volume.

4:25pm. Sigh, this is driving me crazy. I can't get it to work the way I want. I should also really familiar with the shader geometry node.

Let me try nesting the shard. What I am trying to right is the outline, but the texture is giving me trouble. If only get something that depends on the distance from the edge.

https://blender.stackexchange.com/questions/114079/cycles-nodes-is-it-possible-to-get-distance-to-nearest-edge

Hmmm, not quite what I was looking for, but I might be able to use this. In fact, I wanted to in fact use this, but I could not get the effect to work with facing and fresnel. I might be able to combine facing with this to get the effect that I desire.

https://blenderartists.org/t/is-there-a-distance-based-texture-for-blender/1186832

> This would be very nice to have in Blender. There’s a Geometry node in Cycles, but I think you can only measure the distance between the outer limits of the object that has the material applied to it.

I should check this out.

4:40pm. https://youtu.be/8qKLkDr09Pk?t=157
Blender - Stylized Emission Shader (Blender 2.8)

I've been imaging something like this.

https://docs.blender.org/manual/en/latest/render/shader_nodes/input/geometry.html

I don't understand how to use this effectively. Well, let me get back into the fray.

It is always little things like this that waste your time.

5pm. Ok, at this point I am so into my issue that I've completely forgotten what my original purpose was. Let me watch some tutorials.

https://youtu.be/sFtRC9e9W2I
Blender Tutorial: Silhouette Rendering and Workflow

https://youtu.be/sFtRC9e9W2I?t=129

I'll keep the tree addon in mind, but I did not come here for this.

https://docs.blender.org/manual/en/dev/modeling/geometry_nodes/geometry/geometry_proximity.html

I should try out this node. It is a thing now. Ah, whops this is a geometry mode node.

Honestly, what I think I need is facing. Let me just try ramping up the bevel for some reason the previous one did not work correctly.

This is so ridiculous. I have no idea what is going on anymore.

The more I mess around, the more confused I seem to be getting.

5:35pm. https://youtu.be/sJTEJKQ0lYw
Blender Toon Shader

Maybe I want something like this for the shard. I am not sure myself.

https://youtu.be/sJTEJKQ0lYw?t=335

Wait, what is the backface? Is that what I am looking for?

https://www.youtube.com/results?search_query=blender+backface

I did not understand how to get the effect he got. Let me look at some of the other vids.

https://youtu.be/_GgTx49QyyM
Backface Culling in Blender for Surprisingly Better Lighting

I am not sure what exactly do I want, but I sort of want to be able to make the objects pop out in a scene.

6:05pm. Ok, I get what culling is.

https://youtu.be/sJTEJKQ0lYw?t=333

Ah, wait. I am not thinking about this right. He scaled up the monkey head and then overleaid it with the original. Or rather he did something along those lines. Backface culling has nothing to do with it.

https://youtu.be/yjJWEsjR79Q
Change Your Understanding of Normals In Eight Minutes

Let me watch this.

6:50pm. Had to leave for lunch.

7:15pm. Done with the orange. Let me resume.

7:30pm. I basically got nothing done today. I did not even watch the geometry nodes video.

I think I am coming to some understanding though. I intuitively know that just having white jewels is too boring, so I want to spice things up.

https://www.youtube.com/results?search_query=blender+aura

Let me watch the normals video. Then I will watch this. I had trouble dealing with the gradient textures. I want more control over that.

https://youtu.be/g57mNKE8IYc?t=322

Hmmm, what is this?

https://youtu.be/g57mNKE8IYc?t=368

Do normal maps do anything when using Cycles?

https://youtu.be/g57mNKE8IYc?t=444

Blender uses OpenGL for normal maps. I need to keep that in mind.

https://youtu.be/9ehbb93atqo
Blender Energy FX Tutorial |Blender

Let me watch this. I really need to play with textures a bit to give some interest to the scenery.

https://youtu.be/9ehbb93atqo?t=107

This is really cool. If I could get this to work on cube and diamonds that would be best. I should make that my project for tomorrow. Let me try it now. I am dying of curiosity.

7:55pm. I downloaded the pack and am looking at the first material for this. It is quite elaborate. I also see that Voronoi Texture has distance to edge option. Wow.

8:05pm. Surprisngly, I learned a lot just by looking at the material and trying things out.

The most important discovery that I made is that the way I've been using the layer weight node was wrong. There is nothing wrong with it specifically, but once I turn a cube into a diamond, the normals get messed up. That is why I've been getting confusing results. My perplexity was not there for nothing. It seems that when you set normals from faces, the facing gets fixed, and I get the kind of outline I've been desiring. This is really good.

Ok, I think I understand where I went wrong.

1) Not paying attention to normals. I actually hadn't watched a single video on them up to now.
2) Not studying visual effects.

Also it seems shader nodes support variables. There are all sorts of purple fields in the first material indicating that it is linked to variable. This is also something I hadn't known about.

I realize another thing. The way I thought Cycles works was absolutely wrong. It is definitely affected by normals as much as anything else. Normals are subtle, but I think the time has come to study them. Let me watch that video for a bit and then I will call it a day.

I really wasted hours over nothing today, but I suppsoe that is better than wasting days. I'll learn from this make progress tomorrow.

https://youtu.be/9ehbb93atqo?t=122

Ah, so that is what the vars are. Ok.

https://youtu.be/9ehbb93atqo?t=266

This is really informative. I really should be watching this when I am fresher.

But I am convinced - I definitely was not wrong to concentrate so much on the outlines of the shards. The outlines are pretty important. They can make the objects come into focus or blend into the background. Just a simple fbloom effect is not enough to satisfy me here. There needs to be more. I should also get familiar with how the UVs are generated in the texture coordinates node. I watched a tutorial, but I do not understand what is going on under the hood.

8:25pm. https://youtu.be/9ehbb93atqo?t=466

I am confused here. Maybe I am not paying attention by this point, but what is he trying to achieve?

Ah, he is making an effect. I see.

https://youtu.be/9ehbb93atqo?t=695

This isn't a hard tutorial to follow.

https://youtu.be/9ehbb93atqo?t=858

What happens to the normals if you do this? I really need to study up on that so that I do not get messed up again. For all I know, some of the inperfections in the base mesh might be due to normals being off rather than dyntopo's ugly topology. It is something that will bear investigation when I get back to sculpting.

I should also turn some of the main settings in the material option into properties. That will make things more reusable. I'll leave studying that for tomorrow.

1) Normals.
2) Properties.
3) Visual effects. The materials pack as well.
4) The geometry nodes course.

https://youtu.be/9ehbb93atqo?t=932

Also let me stop this here, I am too tired to do this anymore. If I want to prove my will, I should do it by starting a bit earlier tomorrow.

Let me rest here.

The starry sky would be a lot easier if I did a crappy job, but I want to do a good job. The more I do in Blender, the less I'll have to do in Clip Studio when I get to it."

---
## [Psychtoolbox-3/Psychtoolbox-3](https://github.com/Psychtoolbox-3/Psychtoolbox-3)@[83625da653...](https://github.com/Psychtoolbox-3/Psychtoolbox-3/commit/83625da653ab3aa0edb5cfd840d5e67540ae40dd)
#### Thursday 2021-12-23 19:53:25 by kleinerm

Merge pull request #749 from Psychtoolbox-3/master

PTB BETA update 3.0.18.2.

## General

- Cleanups and refactoring, mostly irrelevant to end users.

- Various help text and documentation updates.

- Various improvements to demos and tests, done as part of the validation and compatibility work
  for Matlab R2021b on Ubuntu 20.04.3-LTS, MS-Windows 10 21H1 and macOS 10.15.7 Catalina final.
  Sponsored by Mathworks, thanks! (https://www.mathworks.com/solutions/neuroscience.html)

- New demo BasicSoundPhaseShiftDemo.m - Realtime phase-shifting of sine wave tones.

## Linux

- Note that modern AMD Polaris graphics cards under Linux 5.14 with the latest AMDVLK v2021.Q4.1
  AMD Vulkan driver now support 16 bpc framebuffers for native 12 bpc output. In principle this
  would also work with earlier AMD Sea Islands and Volcanic Islands gpu's, but needs a custom built
  amdvlk driver, which we have available, but won't provide for free.

- Some diagnostic improvements for pixel identity passthrough.

- Substantial improvements to NVidia Optimus laptop support when using the proprietary NVidia
  OpenGL driver. "help HybridGraphics" for details. Laptops with Intel integrated graphics chips
  and NVidia discrete gpu's should work with proper timing and timestamping now on modern Linux
  distributions like Ubuntu 20.04.3-LTS. AMD Ryzen integrated graphics + NVidia discrete gpu's
  should also work better wrt. quality and timing, although limitations wrt. performance exist with
  AMD's display driver and there might be unknown edge cases with broken visual stimulus onset
  timestamping. I do have some (Linux kernel patch) solution for that, which provides excellent quality.
  That solution is a hack though, and implementing a proper solution for the official Linux kernel
  will take time to implement and get upstreamed, especially with the lack of proper funding. We
  haven't decided if and under what conditions we will provide the inofficial - hacky, but well working -
  solution. The only sure thing is we won't provide it for free.

  **Please note that our general advice is to avoid hybrid graphics dual-gpu laptops. Single gpu
     machines require less setup and have less potential for bugs and complications. Also, on
     Windows, these dual-gpu laptops are pure trouble. These improvements for Linux are just
     to lessen the impact of a bad purchase decision as far as this is possible.**

## macOS

- Switch supported and required Octave version to Octave 6.4. Octave 6.3 will likely continue to work.

- Try to detect if we are running on Apple silicon "M1 SoC" ARM - Macs with Apples proprietary
  gpu. This will enable workarounds that allow Screen() to at least limp along, still with totally
  broken visual stimulation timing and timestamping, but at least getting a picture onto the screen,
  instead of complete failure. Also detect and report macOS variant and version, ie. Intel (supported)
  or ARM M1 SoC (unsupported), macOS 10.15 (supported), macOS 11/12 (unsupported).

- Fix KbQueueCreate() crash if running in a single-threaded host runtime, iow. ``octave-cli``. More
  importantly, this should avoid some keyboard queue crashes under macOS with some Python runtimes.
  Ditto for Screen().

- Note that MoltenVK 1.1.5 should be used for Vulkan on macOS.
  
## Windows

- Switch supported and required Octave version to Octave 6.4. Octave 6.3 will likely continue to work.

- Try to detect Windows version more reliable. Report Windows 11 as officially unsupported/untested.

- Fix for Vulkan display backend for AMD graphics on Windows. Try to handle problems switching to
  "fullscreen exclusive mode" better. Both the latest NVidia and AMD drivers have various bugs and
  issues. We better try to work around them as good as we can, instead of just showing a black
  screen. This is highly fragile under current Windows-10 due to poor graphics driver quality, and
  may result in compromised presentation timing and timestamping. Luckily the only meaningful use
  cases for Vulkan on Windows are HDR-10 display modes atm., so the damage is limited. Our guess
  at the moment is that AMD driver versions older than 20.11.2 may work ok, ie. ones from before
  November 2020. For people who want HDR display with proper timing, upgrading to AMD on Linux is
  recommended.

---
## [dtolnay/rust](https://github.com/dtolnay/rust)@[b269213b35...](https://github.com/dtolnay/rust/commit/b269213b35f102a22b5a9645de48814fa255f7a2)
#### Thursday 2021-12-23 20:28:51 by Matthias Krüger

Rollup merge of #91387 - graydon:E0038-clarification, r=wesleywiser

Clarify and tidy up explanation of E0038

I ran into E0038 (specifically the `Self:Sized` constraint on object-safety) the other day and it seemed to me that the explanations I found floating around the internet were a bit .. wrong. Like they didn't make sense. And then I went and checked the official explanation here and it didn't make sense either.

As far as I can tell (reading through the history of the RFCs), two totally different aspects of object-safety have got tangled up in much of the writing on the subject:
  - Object-safety related to "not even theoretically possible" issues. This includes things like "methods that take or return Self by value", which obviously will never work for an unsized type in a world with fixed-size stack frames (and it'd be an opaque type anyways, which, ugh). This sort of thing was originally decided method-by-method, with non-object-safe methods stripped from objects; but in [RFC 0255](https://rust-lang.github.io/rfcs/0255-object-safety.html) this sort of per-impossible-method reasoning was made into a per-trait safety property (with the escape hatch left in where users could mark methods `where Self:Sized` to have them stripped before the trait's object safety is considered).
  - Object-safety related to "totally possible but ergonomically a little awkward" issues. Specifically in a trait with `Trait:Sized`, there's no a priori reason why this constraint makes the trait impossible to make into an object -- imagine it had nothing but harmless `&self`-taking methods. No problem! Who cares if the Trait requires its implementing types to be sized? As far as I can tell reading the history here, in both RFC 0255 and then later in [RFC 0546](https://rust-lang.github.io/rfcs/0546-Self-not-sized-by-default.html) it seems that the motivation for making `Trait:Sized` be non-object-safe has _nothing to do_ with the impossibility of making objects out of such types, and everything to do with enabling "[a trait object SomeTrait to implement the trait SomeTrait](https://rust-lang.github.io/rfcs/0546-Self-not-sized-by-default.html#motivation)". That is, since `dyn Trait` is unsized, if `Trait:Sized` then you can never have the automatic (and reasonable) ergonomic implicit `impl Trait for dyn Trait`. And the authors of that RFC really wanted that automatic implicit implementation of `Trait` for `dyn Trait`. So they just defined `Trait:Sized` as non-object safe -- no `dyn Trait` can ever exist that the compiler can't synthesize such an impl for. Well enough!

However, I noticed in my reading-and-reconstruction that lots of documentation on the internet, including forum and Q&A site answers and (most worrying) the compiler explanation all kinda grasp at something like the first ("not theoretically possible") explanation, and fail to mention the second ("just an ergonomic constraint") explanation. So I figured I'd clean up the docs to clarify, maybe confuse the next person less (unless of course I'm misreading the history here and misunderstanding motives -- please let me know if so!)

While here I also did some cleanups:

  - Rewrote the preamble, trying to help the user get a little better oriented (I found the existing preamble a bit scattered).
  - Modernized notation (using `dyn Trait`)
  - Changed the section headings to all be written with the same logical sense: to all be written as "conditions that violate object safety" rather than a mix of that and the negated form "conditions that must not happen in order to ensure object safety".

I think there's a fair bit more to clean up in this doc -- the later sections get a bit rambly and I suspect there should be a completely separated-out section covering the `where Self:Sized` escape hatch for instructing the compiler to "do the old thing" and strip methods off traits when turning them into objects (it's a bit buried as a digression in the individual sub-error sections). But I did what I had time for now.

---
## [SilentEnforcer/tgwr-mod](https://github.com/SilentEnforcer/tgwr-mod)@[7ab848b0ac...](https://github.com/SilentEnforcer/tgwr-mod/commit/7ab848b0acd5e972f8a63bd1c9f96dee7ad20f75)
#### Thursday 2021-12-23 21:14:47 by fallgelb22061940

removed my "feature"

enjoy cringe larp path and remember to walk today instead of laying in pc chair fuckers :trollface: :trollface: :trollface:

---
## [KennyThrug/KGLGE](https://github.com/KennyThrug/KGLGE)@[968e40ff87...](https://github.com/KennyThrug/KGLGE/commit/968e40ff877ade1bea0ca56d98b674742244b1d7)
#### Thursday 2021-12-23 22:13:29 by KennyThrug

Get Rid of Warnings

I know this is totally in the wrong branch, but like, I wanted to get rid of the warnings... Oops I'm the only person working on this project so fuck you

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[671cfe24be...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/671cfe24bec0746211f74b7ca6d0d0f6ff6fbd23)
#### Thursday 2021-12-23 22:29:34 by Christian Morales

Christian feels like a moron for not understanding basic math

Discuss in the next meeting:
- Is Dashing the way we want it?
- Is damage knockback the way we want it?

Glitches:

- Need to make the player invulnerable while parrying or they'll sometimes hit bullets after a parry
- Sometimes player will keep zooming past enemies in a yo-yo zoom
- Parrying an enemy who shoots projectiles leads to a few problems. Preferably I would like it if one parry captured an attack and a bullet I want it to maybe
destroy the bullet object? We should also have stunned enemies unable to spawn more bullets. Or even maybe stop enemies from spawning bullets during a danger
zone attack? This might mean we will want to make bullet spawning part of Universal Enemy Behavior? Food for thought... This also makes me wonder what we should
do if you're sandwiched between two danger zone attacks? What takes priority? What happens if you're halfway through a yo-yo zoom and you parry a Danger Zone attack?
Will it cause nested Yo-Yo loops? Ehhhhh fuck it whatever I'm tired I got work in the mornin I'm gettin too old for this shit I'm a week away from retirement I can't
relate to these kids no more with their tiktaks and their fuckin whatever you have it fuckin I don't know, fugehtabouteeet.
- Whooooo lord yo-yo zooming is scuffed, it has a ton of issues that might be easier to discuss in a meeting.
- Grappling when next to an object you collide with will cause all kinds of bullshit
- Player is able to parry after getting hit. Maybe disable parry button after taking damage?

Shit Done Today:
- Become invincible after successful parry
- Tried to fix the glitch of zooming past stuff by calculating the amount of distance you zoom but it wasn't working out

Glitches Fixed:

Noticed Glitches:

I'll come back to this grapple zoom shit later I got eggnog to drink and a broken car to despair over.

---
## [kevineby/crawl](https://github.com/kevineby/crawl)@[cae3918e47...](https://github.com/kevineby/crawl/commit/cae3918e4765b1eef0c1b274a64638582d4d312e)
#### Thursday 2021-12-23 22:52:10 by Perry Fraser

Improve Ratskin Cloak god interactions

[Committer's note:
- Don't allow the cloak to spawn rats that should hate you
  (hell rats under good gods, any rats under Oka or Sac Love)
- Unmark the cloak as evil.]

Closes #2102

---
## [Gurky-Kronos/pfQuest-turtle](https://github.com/Gurky-Kronos/pfQuest-turtle)@[6bb36ee048...](https://github.com/Gurky-Kronos/pfQuest-turtle/commit/6bb36ee0489a4daab1b556d958f8cc384686f142)
#### Thursday 2021-12-23 22:56:51 by Gurky

Quests, Items, Objects, Units

Added:

Quests:
You Reap What You Sow
Fallen Adventurers
Preventive Strike
Trapped in the Nightmare
Serpentbloom
Down With the Sickness
Preventing Poison
Kodo Hunt
Mother of the Hollow
Troubles From Distant Lands
Trader's Misfortune
Mastering the Arcane
Arcane Arms
A Glittering Opportunity
A Bloody Good Deed

Items:
Country Pumpkin Seeds
Mountain Berries Seeds
Striped Melon Seeds
Magic Mushroom Spores
Squealer Thornmantle's Mane
Sickly Gazelle Flesh Sample
Summer Dew
Life's Dawn
Vulpa Bloom
Moontouched Wood
Crystal of the Serpent
Everchanging Essence

Objects:
Ripe Garden Pumpkin
Garden Berry Bush
Ripe Garden Watermelon
Summer Dew
Life's Dawn
Vulpa Bloom
Mysterious Glittering Object

Units:
Kern Mosshoof
Chok'Garok
Ureda
Kheyna Spinpistol
Aneka Konko

I believe some of the quests need races,faction,classes added to them which I will visit later.

---
## [trpsl/davinci-kernel](https://github.com/trpsl/davinci-kernel)@[e1893819d0...](https://github.com/trpsl/davinci-kernel/commit/e1893819d0e22198439d53509b79f080b31b8a5b)
#### Thursday 2021-12-23 23:00:48 by Peter Zijlstra

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
## [ccprince/advent-of-code-2021](https://github.com/ccprince/advent-of-code-2021)@[b348d585b0...](https://github.com/ccprince/advent-of-code-2021/commit/b348d585b0b8e9280a38849a94c579873b1ea83b)
#### Thursday 2021-12-23 23:39:36 by Charles Prince

Day 23

I nearly gave up on this one, so many times. I lost sleep last night,
pondering the right data structures. I never got one I really liked,
but one I thought would work. Then, trying to find the valid moves
at any given state took longer than I think it really needed to; my
knowledge of recursive graph-search algorithms is very week, and then
even the iterative one took a bunch of time.

After all that, my solution was too damn slow -- ~20 seconds for the
small version of part 1, >15 minutes for the large one in part 2.

I was ready to throw in the towel on part two, when I remembered a
couple of optimizations I thought about, but skipped -- specifically,
forcing moves into rooms to go as far in as possible, and once a
room contained only correct amphipods, those 'pods stayed in place.

Adding those dropped the runtime for each part down to a handful
of seconds! Good enough.

---
## [h-lame/advent-of-code](https://github.com/h-lame/advent-of-code)@[a8a62967c7...](https://github.com/h-lame/advent-of-code/commit/a8a62967c798ea5479fcac45b99bde7b2467d5da)
#### Thursday 2021-12-23 23:42:09 by Murray Steele

Solution Day 22 2021

Things are definitely getting harder.  This one I got the solution to part 1 fairly quickly in terms of time spent, and I had a fair idea of what was needed for part 2, just didn't have the right thoughts on how to implement the thing.  Finally clawed out some time to google and ended up cribbing some of the intersection methods from a python solution I saw, then implemented my algorithm on top.  Lots of silly mistakes in the python -> ruby transliteration and (another) lack of test cases meant I took ages to get it working.

One mis-step I took was my "merge_cubes" method.  I thought it would be better to merge cubes if they were contiguous so that the reactor would have less cubes to look at per instruction, however, my method of merging cubes involved multiple passes through the cubes.  This is fine for on instructions because I was only looking at a small subset of cubes - those changed in the addition process.  However, for the off instructions I ended up looking at the complete set of cubes in the reactor.  This takes ages given my algorithm (loop until nothing changes, and look at every cube against every other cube and stop looking if something changes), and while it may have been correct - the reactor contained the smallest set of cubes, it was slow.  In the "what if I...?" stages of perf tweaks I stopped calling this method, having identified it as a choke point and the thing completed in 24s, having previously been running for 24mins without completion.

Ah well.  A good lesson in premature optimisations, particularly when they optimise the wrong thing.

I've a feeling I might be done.  The problems require lots more time, and I just don't think I can carve out more time for it.

---
## [Utumno/wrye-bash](https://github.com/Utumno/wrye-bash)@[711ea185be...](https://github.com/Utumno/wrye-bash/commit/711ea185bec43d70d887512f10530029ecdd9a90)
#### Thursday 2021-12-23 23:51:51 by MrD

FName: EEE tests for FNDict

EEE test immutability - copies
EEE add del self.__dict__ to ci_body?

An initial version of this branch had Paths replaced with CIstr's. That
turned out to be highly unsatisfactory:

- CIstr I created to use internally in LowerDict - LD is the API, not
CIstr.
- body_ and ext_ wrappers are too slow - the code looked more ugly and
os.path.splitext (an expensive operation) kept proliferating
- those DataStore keys are really a beast of its own kind (corresponding
to filenames) and by the lesson this very branch teaches us better have
a specialized type for them
- turns out I wanted to keep Path's ability to compare with strings -
but I wanted this as efficient as possible - can't have slots
unfortunately but other than that given that FName *can only be
instantiated with unicodre strings* I was able to drop the
`if type is str` checks in FNDict dunder methods
- FName(CIstr) would be too much nesting and probably performance (lookups
of methods traverse the mro -TODO: time) - anyway FName is-not a CIstr

Check if FName should be the usual case in comparisons (try: except AE)
once I have scanned the code

SSS:

return None if None is passed (duh)

Backwards compat TTT  EEE move forward_compat_path_to_fn below FNDict

Well I kept adding backwards compat and even with dedicated functions:

@@ -428,6 +431,2 @@ def __repr__(self):
 # backwards and forward compat functions
-def backwards_compat_fn_to_path(di, value_type=lambda x: x):##: [backwards compat] drop in 312+
-    return {GPath_no_norm('%s' % k): value_type(v) for k, v in di.items()}
-def backwards_compat_fn_to_path_list(li, ret_type=list):
-    return ret_type(map(GPath_no_norm, map(str, li)))
 def forward_compat_path_to_fn(di, value_type=lambda x: x):##: [forward compat] drop 313+

this was getting out of hand  -  so:

@@ -378,2 +378,5 @@ def ci_body(self):

+    def __reduce__(self):##: [backwards compat] drop in 312+ (but still store strs)
+        return GPath_no_norm, (str(self),)

@@ -553,2 +552,5 @@ def __repr__(self):

+    def __reduce__(self): #[backwards compat]we 'd rather not save custom types
+        return dict, (dict(self),)

I think now I got them all :)
Note I pickle the cache factory (GPath_no_norm) - so when I load
settings I already cache the filenames - can't think of anything bad
(apart that this won't carry to pre GPath_no_norm  versions of bash -
that is pre 307 as 662423530ff1ba4219ed0b2cc91effd5306a5ca2 on 307, but
I don't think many people will update to 310 and then go back to 306)

Edit: was bitten bitterly by my smart idea (stays a smart idea, but).
So I was testing a bashed patch and some form ids had Paths instead of
FNames and this drove me nuts, had put breakpoints everywhere and still
couldn't find where these Paths were from - turns out we use deepcopy
(yes I used to know) and deepcopy will use __reduce__ if it's there.
This incidentally gave me an idea for optimizing the Path copies
currently.

squash! FN

@@ -394,5 +388,4 @@ def __eq__(self, other):
         except AttributeError:
-            if isinstance(other, str):
-                return self._lower == other.lower()
-            return NotImplemented
+            # this will blow if other is not a str even if it defines lower
+            return self._lower == str.lower(other)
     def __ne__(self, other):

eee test  deepcopy

squash! fe24d5da24b5a8694835e81cee307ddad94bde2a

Yey:

self = FName('path.txt'), other = bolt.Path('path.txt')

    def __eq__(self, other):
        try:
            return self._lower == other._lower # (self is other) or self...
        except AttributeError:
            # this will blow if other is not a str even if it defines lower
>           return self._lower == str.lower(other)
E           TypeError: descriptor 'lower' for 'str' objects doesn't apply to a 'Path' object

@@ -459,3 +459,3 @@ def test__eq__(self):
         # fname and paths
-        assert fn == GPath('path.txt') ##: Oops do we want this?
+        with pytest.raises(TypeError): assert fn != GPath('path.txt')
         # paths and None
@@ -470,3 +470,3 @@ def test__eq__(self):
         assert empty == ''
-        assert empty == GPath('') ##: Oops do we want this?
+        with pytest.raises(TypeError):assert empty != GPath('')
         for other in (b'', None, [], [1], True, False, 55):
@@ -505,4 +505,4 @@ def test_dict_keys(self):
         assert FN in fn_keys_dict # yey
-        assert GPath(file_str) in fn_keys_dict ##: Oops do we want this?
-        assert GPath(FILE_STR) in fn_keys_dict ##: Oops do we want this?
+        with pytest.raises(TypeError): assert GPath(file_str) in fn_keys_dict
+        with pytest.raises(TypeError): assert GPath(FILE_STR) in fn_keys_dict
         string_keys_dict = {file_str: 1}
@@ -527,4 +527,4 @@ def test_sets_lists(self):
             assert FN in fn_set # yey
-            assert GPath(file_str) in fn_set ##: Oops do we want this?
-            assert GPath(FILE_STR) in fn_set ##: Oops do we want this?
+            with pytest.raises(TypeError): assert GPath(file_str) in fn_set
+            with pytest.raises(TypeError): assert GPath(FILE_STR) in fn_set
             string_set = cont_type([file_str])

---

