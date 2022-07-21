## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-20](docs/good-messages/2022/2022-07-20.md)


1,833,485 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,833,485 were push events containing 2,721,571 commit messages that amount to 192,826,463 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [CHOMPStation2/CHOMPStation2](https://github.com/CHOMPStation2/CHOMPStation2)@[4704df506b...](https://github.com/CHOMPStation2/CHOMPStation2/commit/4704df506bfccd3f4ef9d75a3cf1a4f6f63ca4e3)
#### Wednesday 2022-07-20 00:18:07 by Victor Zisthus

Massive Broad Scope Changes

NEW STUFF
Added in a custom thermal regulator for the wilderness shelter.

Southern Cross now has a Bluespace Radio!

Added a subspace radio, and allowed it to be made in the autolathe.

ALL MAPS:
Added lighting to dark areas. Did not touch lighting in maintenance areas.

DECK ONE:
Adjusted exterior lattice network.

DECK TWO:
Fixed a bug with Shieldgen.

Moved the Engine SMES powernet sensor off of a pump.

Removed the second freezer air alarm to prevent pressure alarms from going off every shift. (I got my revenge on the laws of thermodynamics with the new custom regulator, don't worry.)

Put a new subspace radio in the bar.

Adjusted exterior lattice network.

DECK THREE:
Removed a duplicate shower curtain in one of the dorm rooms.

SURFACE OUTPOST:
This PR will cause a conflict with #4061 but I am willing to help Enzo with the project as needed~

A friend and boy waits for the miners every shift.

Moved some stuff around at surface S&R per a reported issue. FIXES #4072

Fixed a bug with the hunting lockers and doors. Security should have access to them now.

Fixed a bug with the Hunting Pen shield generators.

CAVES:
Cleared the rock around the outpost, added a new door to allow moving around the exterior.

EXPLO CARRIER:
Put the new Bluespace Radio on the table in the gateway prep room.

WILDERNESS + SKY ISLANDS:
Overhauled the wilderness shelter! It now has a crew quarters room, First Aid, a second floor, and a utility room. It's only powered by a single advanced RTG that's barely able to keep up with power demand when the place is abandoned, so be sure to bring resources from mining and science to get the other RTG's up and running!

---
## [dod-ccpo/atat-web-api](https://github.com/dod-ccpo/atat-web-api)@[fe7822640e...](https://github.com/dod-ccpo/atat-web-api/commit/fe7822640e46849165c70b7c3eddccc6e316a837)
#### Wednesday 2022-07-20 00:45:52 by Kyle Laker

Support custom domains for the API Gateway

This adds support for custom domains to the API Gateway. The way that
this is handled requires changes to a few core constructs within the
environment as well as a little bit of gluing AWS resources together.
First, API Gateway does not directly support custom domains on private
endpoints. This requires us to put _something_ in front of it that can
speak HTTPS with a valid certificate for a custom name. This uses a load
balancer. Because of issues experienced during troubleshooting, it was
easier to just add support for _both_ types of Load Balancers and we can
toggle between them in the future as needed.

Now, as for how we implement the Load Balancer's Target Group... that
requires a little more involvement. To start with, ELBv2 only supports a
few types of targets by default: EC2 Instances, IP Addresses, Lambda
Functions, and ALBs. Unfortunately, a VPC Endpoint (which is what we
have with our API Gateway Private Endpoints) isn't any of those things
directly. But it does have an IP address (well... it actually has
several). Unfortunately, no tooling directly exposes the IP addresses
based on VPC Endpoint ID; especially not CloudFormation/CDK.
Fortunately, with Custom Resources, we can glue together several AWS API
calls to describe the endpoint and get its associated Elastic Network
Interfaces (ENIs) and then describe those to get their IP addresses
(because despite ENIs being a lovely abstraction in EC2/AWS, an ELBv2
cannot target them).

Unfortunately, the CDK is very helpful. And by being so helpful, it
provides a lot of abstractions around ELBv2 Target Groups. But this
breaks the ability to just yeet arbitrary JSON into the `Targets`
property of the `AWS::ElasticLoadBalancingV2::TargetGroup` resource. No
matter what you try to do, the CDK either wraps it in a list or very
(not-so) helpfully tries to validate it (which won't work because with
our custom resource, it ends up being a `Fn::GetAtt`). And because it's
an intrinsic function and not actual raw data, we can't treat it like an
object and split it, iterate over it, or any other fun magic (in the
CDK, it's a `Token`). So we have to just treat it as an opaque object.
The only way we can effectively provide that as an opaque object is to
use escape hatches in the CDK to pass it directly to the underlying
CloudFormation resource property. That means that our Custom Resource
has to return a valid JSON object that can be passed to the `Targets`
object.

The configured Load Balancer will then balance across all the IP address
(and hopefully does so somewhat intelligently based on availability zone
since we do provide that data). The HTTPS/TLS certificate from ACM is
attached to the load balancer and that results in the certificate
matching the DNS name.

This does require two changes for consumers of the API:

 1. Consumers must now use the DNS name. The regional endpoint for the
    API is no longer available
 2. Consumers must pass the `x-apigw-api-id` header, as described in the
    [API Gateway docs for invoking via the DNS name][1]

Finally, this should not cause any issues for Developers' sandbox
environments. Those should be able to trivially be built without DNS
names and without VPC connectivity.

This implementation does have a few trade-offs as it closely ties the
usage of a custom domain to the usage of a VPC. For our use case, that
is likely pretty acceptable since any environments where we'd specify a
custom name, we'd also have a VPC. Second, we may need to kick off
something to re-trigger the custom resource at some point in the future
if we for any reason see the underlying IPs change without the VPCE ID
changing (but that is extremely unlikely to happen).

One option that was available that was rejected for now was having the
ALB target a Lambda to handle balancing between the VPC endpoints. This
would have resulted in additional code needing to be executed on _every_
request (so in many cases, doubling our number of Lambda function
invocations) and would have just added another link in the chain of
request/response size limitations that would become somewhat harder to
debug. Not using the Lambda option also allows us to maintain the
ability to use either an NLB or an ALB, whichever is most appropriate.

[1]: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-test-invoke-url.html#apigateway-private-api-public-dns

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/RELATIVES](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/RELATIVES)@[a20088c286...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/RELATIVES/commit/a20088c2865f9b61ca0695b5586288c48ca06129)
#### Wednesday 2022-07-20 00:53:52 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY/blob/main/README.md

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY

Re federal file finders anonymous number 2.eml
FILED NEW YORK COUNTY CLERK 07_31_2020 04 47 AM INDEX NO. 153974_2020.eml
Re DOC Constituent Services - Auto Reply Email Acknowledgement DO NOT REPLY .eml
Fwd Not read Fwd Fwd C16-93715.eml
Fwd # 50074 90849565 --- WHAT IS IT EXACTLY YOU ALL ARE PROTECTING--- SOMETHING MUCH DEEPER .eml
HALE ISMET, AN ACCESSORY TO SHARI - FINDS THIS FUNNY..eml
Re $$$$$$ GS _ JOB REGISTRATIONS ---) WERE CONTACTED..eml
Fwd quash .eml
Re $$$$$$ GS _ JOB REGISTRATIONS ---) WERE CONTACTED.-1.eml
Re $$$$$$ GS _ JOB REGISTRATIONS ---) WERE CONTACTED.-2.eml
FEDERAL BANK INVESTIGATION, HSBC, JPM..eml
USC 18 §225. Continuing financial crimes enterprise-.eml
Fwd Fwd Fwd so that's why they call it a 1212-5858 --- DID NOT KNOW THAT. WHATTTTTTT .eml
Fwd [BSCPGROUPHOLDINGSLLC_ELSER-AND-DICKER] 80bec9 C16-93715 1516523 [ SFITX STFGX STFBX SFBDX ] #1.eml
Fwd 16537-714-487-492, OMISSIONS, OBSTRUCTION, FITNESS, ETC..eml
mainLINE THESE KNOWN INDIVIDUALS - AIDED AND ABETTED AS ACCESSORIES TO THE ZUCKER ENTERPRISES.eml
Fwd Fwd TY FOR TAKING A LOOK AT THIS..eml
Re # USC Title 18. VIOLATIONS --- ANNEXED IN NYSCEF 153974_2020 [ LOAN 50074 EST ++ ].eml
Re Fwd GFY.eml
Re Fwd GFY --- I DON'T KNOW WHAT AGENCY IT IS... I KNOW ONE GUY..eml
Re MSCO 0_. SHARED_ .eml
if you understand what a piece of shit is ) you will understand why ZUCKERS and Counselors belong in PRISON.eml
Fwd # 50074 90849565 --- WHAT IS IT EXACTLY YOU ALL ARE PROTECTING--- SOMETHING MUCH DEEPER -1.eml
Fwd DFS calculator..eml
Fwd DFS calculator. BIG OOPS.eml
Re THAT'S MISSES 1212-5858, TO YOU AS WELL..eml
combined CERTIFICATES of OCCUPANCY for all buildings as of FY 2022..eml
(EDELIVERY@MORGANSTANLEY.COM, RULE-COMMENTS@SEC.GOV).eml
Re Fw Away from email - Re Automatic reply FEDERAL BANK INV.eml
VIOLATION OF CIVIL RIGHTS, PRIVACY & CONFIRMED USC TITLE 18.225, 18.21, 18.4, 18.3, 18.2.eml
Fwd USC 18 §225. Continuing financial crimes enterprise-.eml
Fwd Automatic reply FEDERAL BANK INVESTIGATION, HSBC, JPM..eml
RE TAX RISKS and LETTER OF CREDIT 50074 --- rents and leases transferred to State Farm .eml
Fwd Fwd Proof of service receipt.eml
Fwd LOAN 50074 SEC FILER 93715 CIK 1516523 AND NYSCEF DOCKETS IN 153974_2020.eml
NO MANDATORY ATTENDANCE REQUIRED. DOCKETS CLEAR ---.eml
Fwd C16-93715 1516523 OBSTRUCTION OMISSION.eml
Fwd 30 year rate.eml
Fwd Fwd OBSTRUCTION & Summary Notes for Review..eml
Fwd Your Monthly NY Commercial Real Estate Digest.eml
June 29, 2022 at 12 01 09 PM EDT.eml
Re Automatic reply VIOLATION OF CIVIL RIGHTS, PRIVACY & CONFIRMED USC TITLE 18.225, 18.21, 18.4, 18.3, 18.2.eml
Fwd 93715 MERGED INTO 1516523 UNDER OMISSIONS, OBSTRUCTION, FITNESS, ETC..eml
Fwd 93715 - 153974_2020 --- 1516523.eml

---
## [BobNewman-max/thewasteland](https://github.com/BobNewman-max/thewasteland)@[fbdae279c1...](https://github.com/BobNewman-max/thewasteland/commit/fbdae279c184074b4868391070e97451d5bfd124)
#### Wednesday 2022-07-20 01:05:07 by BobNewman-max

Legion cent buff (And legate.)

looking at their armor, combat styles and use in-game. Cent just gets fucking melted by anything with a gun and a dream. Might as well buff it so the faction lead has faction lead tier armor. 

Keep in mind, a combat body armor set holds higher average values then cent armor. Lets change that. 

Legate armor also got buffed, not that it matters. Thats just for admins.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[4f9df17cb1...](https://github.com/Paxilmaniac/Skyrat-tg/commit/4f9df17cb150bd073914527bce381b583cf83657)
#### Wednesday 2022-07-20 01:48:04 by magatsuchi

[FIXED MIRROR] Tsu's Brand Spanking New Storage: or, How I Learned to Refactor For Skyrat (#14868)

* Tsu's Brand Spanking New Storage: or, How I Learned To Pass Github Copilot As My Own Code

* Delete storage.dm

* yippee

* shit

* holy shit i am stupid

* more fixes

* fuck

* woops

---
## [StarbloomSS13/StarbloomSS13](https://github.com/StarbloomSS13/StarbloomSS13)@[635f518d04...](https://github.com/StarbloomSS13/StarbloomSS13/commit/635f518d04a30c4c9f977c0570d480f8d44e56d1)
#### Wednesday 2022-07-20 01:59:22 by notfrying1pans

web edit fuck yoooou

i swear to fucking god if this resets line endings or some shit im gonna scream

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[6fe0683a7b...](https://github.com/LemonInTheDark/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Wednesday 2022-07-20 02:01:23 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---
## [DunniDee/Project-R](https://github.com/DunniDee/Project-R)@[c0ae7f5186...](https://github.com/DunniDee/Project-R/commit/c0ae7f5186f02f0538109693a911f40d872f5c9b)
#### Wednesday 2022-07-20 02:59:15 by Dunstan

Motor and UI Changes

Fuck you fraser ive neuterd your shit

---
## [openeuler-mirror/kernel](https://github.com/openeuler-mirror/kernel)@[a58b2aed55...](https://github.com/openeuler-mirror/kernel/commit/a58b2aed5535805d852dd51897dc4a174a1d218d)
#### Wednesday 2022-07-20 03:33:00 by Linus Torvalds

gpiolib: acpi: use correct format characters

stable inclusion
from stable-v5.10.112
commit 9709c8b5cdc88b1adb77acdbfd6e8a3f942d9af5
category: bugfix
bugzilla: https://gitee.com/openeuler/kernel/issues/I5HL0X

Reference: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=9709c8b5cdc88b1adb77acdbfd6e8a3f942d9af5

--------------------------------

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Zheng Zengkai <zhengzengkai@huawei.com>
Acked-by: Xie XiuQi <xiexiuqi@huawei.com>

---
## [dackerman/nixos-config](https://github.com/dackerman/nixos-config)@[a8edde3101...](https://github.com/dackerman/nixos-config/commit/a8edde31015baf66f759f3110c97f5531b00a165)
#### Wednesday 2022-07-20 04:07:25 by David Ackerman

Resolve horrible cider/shadowcljs issue

My JDK was stripped of Doclet for some reason, similar to what people
experienced with Guix. Therefore whenever I tried to use cider-jack-in
on my clojurescript project which uses shadow-cljs, I would get these
weird ClassNotFoundExceptions. Oddly, I didn't see then when using
leiningen - I wonder if lein bundled some other version of the JDK but
shadow-cljs uses my system version? Either way, using this version of
openjdk seems to have done the trick (before it was v11 or so).

This issue has more detail:
https://github.com/clojure-emacs/orchard/issues/152

---
## [pop-os/linux](https://github.com/pop-os/linux)@[7c3649dfa1...](https://github.com/pop-os/linux/commit/7c3649dfa1f60bf4c4ebe71b70d26eafa883cb54)
#### Wednesday 2022-07-20 04:30:00 by Peter Zijlstra

objtool: Fix symbol creation

commit ead165fa1042247b033afad7be4be9b815d04ade upstream.

Nathan reported objtool failing with the following messages:

  warning: objtool: no non-local symbols !?
  warning: objtool: gelf_update_symshndx: invalid section index

The problem is due to commit 4abff6d48dbc ("objtool: Fix code relocs
vs weak symbols") failing to consider the case where an object would
have no non-local symbols.

The problem that commit tries to address is adding a STB_LOCAL symbol
to the symbol table in light of the ELF spec's requirement that:

  In each symbol table, all symbols with STB_LOCAL binding preced the
  weak and global symbols.  As ``Sections'' above describes, a symbol
  table section's sh_info section header member holds the symbol table
  index for the first non-local symbol.

The approach taken is to find this first non-local symbol, move that
to the end and then re-use the freed spot to insert a new local symbol
and increment sh_info.

Except it never considered the case of object files without global
symbols and got a whole bunch of details wrong -- so many in fact that
it is a wonder it ever worked :/

Specifically:

 - It failed to re-hash the symbol on the new index, so a subsequent
   find_symbol_by_index() would not find it at the new location and a
   query for the old location would now return a non-deterministic
   choice between the old and new symbol.

 - It failed to appreciate that the GElf wrappers are not a valid disk
   format (it works because GElf is basically Elf64 and we only
   support x86_64 atm.)

 - It failed to fully appreciate how horrible the libelf API really is
   and got the gelf_update_symshndx() call pretty much completely
   wrong; with the direct consequence that if inserting a second
   STB_LOCAL symbol would require moving the same STB_GLOBAL symbol
   again it would completely come unstuck.

Write a new elf_update_symbol() function that wraps all the magic
required to update or create a new symbol at a given index.

Specifically, gelf_update_sym*() require an @ndx argument that is
relative to the @data argument; this means you have to manually
iterate the section data descriptor list and update @ndx.

Fixes: 4abff6d48dbc ("objtool: Fix code relocs vs weak symbols")
Reported-by: Nathan Chancellor <nathan@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Borislav Petkov <bp@suse.de>
Acked-by: Josh Poimboeuf <jpoimboe@kernel.org>
Tested-by: Nathan Chancellor <nathan@kernel.org>
Cc: <stable@vger.kernel.org>
Link: https://lkml.kernel.org/r/YoPCTEYjoPqE4ZxB@hirez.programming.kicks-ass.net
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [Sirryan2002/Paradise](https://github.com/Sirryan2002/Paradise)@[ab7a358506...](https://github.com/Sirryan2002/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Wednesday 2022-07-20 05:44:13 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [levackt/SecretNetwork](https://github.com/levackt/SecretNetwork)@[a8ffddebfe...](https://github.com/levackt/SecretNetwork/commit/a8ffddebfe95cb7bad51eb0ecdcdcd7108319d1c)
#### Wednesday 2022-07-20 06:26:52 by Cashmaney

Setting up gitpod username with proper permissions on github

Also, fuck you wavy lines logo

---
## [snehapatil0519/Training-Institute-Pune](https://github.com/snehapatil0519/Training-Institute-Pune)@[a2e2ca0e04...](https://github.com/snehapatil0519/Training-Institute-Pune/commit/a2e2ca0e043634b0ef45207a82346b5ee99cc6d6)
#### Wednesday 2022-07-20 07:30:59 by snehapatil0519

Update README.md

                                                                                                                                          By- Sneha Patil
                                                                                                                                          Date- 20th July,2022

The term Digital Marketing was first used in the 1990s. The digital age took off with the coming of the internet and the development of the Web 1.0 platform. The Web 1.0 platform allowed users to find the information they wanted but did not allow them to share this information over the web.

KEY POINTS TO REFER
•	What is Digital Marketing?
•	Benefits of Digital Marketing
•	What does Digital Marketing Consist of
•	SEO
•	SMM
•	Content Writing
•	Digital Marketing Measurement

What is Digital Marketing?
Digital Marketing is an umbrella term for the marketing of products or services using digital technologies, mainly on the Internet, but also including Mobile Phones, display advertising and any other digital medium.
Benefits of Digital Marketing
	Time and Effort saving
	Flexibility
	Real Time Analysis
	Impactful
	Economical
	Instant Feedback
What does Digital Marketing Consist Of
Digital Marketing can be broken down into 8 mainly categories into:
•	Search Engine Optimization
•	Pay-Per-Click
•	Social Media Marketing
•	Content Marketing
•	Email Marketing
•	Mobile Marketing
•	Marketing Analytics
•	Affiliate Marketing
What is SEO?
SEO means Search Engine Optimization and is the process used to optimize a website’s technical configuration, content relevant and link popularity so it’s pages can become easily findable, more relevant and popular towards user search queries, and as a consequence, search engines rank them better.
There Are Three Kinds Of SEO Are:
On-Page SEO:  Anything on your Web Pages that is – Blogs, Product Copy, Web Copy
Off-Page SEO: Anything which happens away from your website that helps with your SEO strategy – Backlinks
Technical SEO: Anything technical undertaken to improve Search Rankings – Site Indexing to help spiders crawling.
Pay-Per-Click (PPC)
What is PPC (Pay-Per-Click) Marketing? Pay-Per-Click marketing is a way of using Search Engine Advertising to generate clicks to your website’s, rather than “earning” those clicks organically.
Using PPC you will enjoy certain advantages over other forms of online marketing methods:
1.	Fast Measurable Results
2.	You have control of Budget And Scheduling
3.	Target Audience
4.	You only pay for clicks
5.	Get on the top spot of Google’s page 1 Search Results instantly.
What is SMM?
Social Media Marketing is a form of Internet Marketing that uses Social Media Apps as a Marketing Tool. These Social Media platforms enable brands to connect with their audience to: build a brand, increase sales, drive traffic to a website.
Social Media Marketing gives you:
1.	Increased Brand Awareness
2.	More Inbound Traffic
3.	Improved Search Engine Rankings
4.	Higher Conversion Rates
5.	Better Customer Satisfaction
6.	Improved Brand Loyalty
7.	More Brand Authority
Content Writing
Content Writing is the process of Writing, Editing and Publishing Content in a digital format. That Content can include blog posts, video or podcasts scripts, e-books or white papers, press release, product category description, landing page or Social Media copy and do many other things. Creating an Outline is a “Great” First step in the Content writing Process. Outlines help your content come out better for the reasons like force you to put all your thoughts down in an organized way which really speeds up the writing process.
Email Marketing
Email Marketing is a form of Marketing that can make the customers on your email list aware of new products, discounts, and other services. It can also be a softer sell to educate your audience on the value of your brand or keep them engaged between purchases. It can also be anything in between.
Mobile Marketing
Mobile Marketing is a multi-channel online marketing technique focused at reaching a specific audience on their smartphones, feature phones, tablets or any other related devices through websites, E-mail, SMS and MMS social media, or Mobile Applications.
Marketing Analytics
Marketing Analytics is the use of data to evaluate the effectiveness and success of marketing activities. By integrating marketing AI into your business strategy, you can gather deeper consumer insights, optimize your marketing objectives, and get a better return on investment.
Affiliate Marketing
Affiliate Marketing is an advertising model in which is a company compensates third-party publishers to generate traffic or leads to the company’s products and services. The third-party publishers are affiliates and the commissions fee incentivizes them to find ways to promote the company.

---
## [Fabizocker456/test](https://github.com/Fabizocker456/test)@[49aefd8e17...](https://github.com/Fabizocker456/test/commit/49aefd8e173e92e482c0950320e44adbe6a57fbb)
#### Wednesday 2022-07-20 09:35:33 by Fabizocker456

idk

Like you,  I am frequently haunted by profound questions related to man's
place in the Scheme of Things.  Here are just a few:

	Q -- Is there life after death?
	A -- Definitely.  I speak from personal experience here.  On New
Year's Eve, 1970, I drank a full pitcher of a drink called "Black Russian",
then crawled out on the lawn and died within a matter of minutes, which was
fine with me because I had come to realize that if I had lived I would have
spent the rest of my life in the grip of the most excruciatingly painful
headache.  Thanks to the miracle of modern orange juice, I was brought back
to life several days later, but in the interim I was definitely dead.  I
guess my main impression of the afterlife is that it isn't so bad as long
as you keep the television turned down and don't try to eat any solid foods.
		-- Dave Barry

---
## [Fabizocker456/test](https://github.com/Fabizocker456/test)@[e57b4f765e...](https://github.com/Fabizocker456/test/commit/e57b4f765ef2be3ac25e2f000b09655e16396885)
#### Wednesday 2022-07-20 10:04:47 by Fabizocker456

idk

A fellow bought a new car, a Nissan, and was quite happy with his purchase.
He was something of an animist, however, and felt that the car really ought
to have a name.  This presented a problem, as he was not sure if the name
should be masculine or feminine.
	After considerable thought, he settled on an naming the car either
Belchazar or Beaumadine, but remained in a quandry about the final choice.
	"Is a Nissan male or female?" he began asking his friends.  Most of
them looked at him pecularly, mumbled things about urgent appointments, and
went on their way rather quickly.
	He finally broached the question to a lady he knew who held a black
belt in judo.  She thought for a moment and answered "Feminine."
	The swiftness of her response puzzled him. "You're sure of that?" he
asked.
	"Certainly," she replied. "They wouldn't sell very well if they were
masculine."
	"Unhhh...  Well, why not?"
	"Because people want a car with a reputation for going when you want
it to.  And, if Nissan's are female, it's like they say...  `Each Nissan, she
go!'"

	[No, we WON'T explain it; go ask someone who practices an oriental
	martial art.  (Tai Chi Chuan probably doesn't count.)  Ed.]

---
## [Fabizocker456/test](https://github.com/Fabizocker456/test)@[ef059cd0d8...](https://github.com/Fabizocker456/test/commit/ef059cd0d8bb76a3e257db426167cdc902d39079)
#### Wednesday 2022-07-20 10:25:37 by Fabizocker456

idk

Where, oh, where, are you tonight?
Why did you leave me here all alone?
I searched the world over, and I thought I'd found true love.
You met another, and *PPHHHLLLBBBBTTT*, you wuz gone.

Gloom, despair and agony on me.
Deep dark depression, excessive misery.
If it weren't for bad luck, I'd have no luck at all.
Oh, gloom, despair and agony on me.
		-- Hee Haw

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ab02ec5048...](https://github.com/mrakgr/The-Spiral-Language/commit/ab02ec5048e4082bf7df1e3e63917fd9240efdf7)
#### Wednesday 2022-07-20 10:30:39 by Marko Grdinić

"8:15am. I am up. Let me catch up with some of my follows and then I will resume the ASP.NET course. This course is more important than the networking one. Even if I knew everything there is to know about the internet, it would be like knowing everything about the physical road system. It would make no difference in how cars are to be driven on them. The same goes for networking. I'd still use some library/framework/API that abstract the details away into message passing. Let me chill for a bit. Any mail?

1 accept...from a place I already had an accept. What the hell?

It seems my profile is featured somewhere. Let me change the availability to 'Open To Offers' from 'Open To Interviews'. Right now I am busy.

8:50am. Done chilling. Let me start resume the course. I want to get it out of the way today.

```html
<footer class="border-top footer text-muted">
```

This class attribute...that's for CSS if I recall correctly?

9am. Yeah, yesterday I was just too tired to do this kind of curious exploration. When you are tired, curiosity goes out the window and at best, you just want to grind it through. That is not the right mindset? Learning without curiosity is not effective.

Let me backtrack a bit. Actually these weird partial views tripped me up last time as well.

For a C# program, the whole structure of the project is so unusual. I can't tell what goes where, and the way things are linked is so magical. I really don't like that kind of thing.

Ironically, a situation like this is something a novice would be better mentally prepared to handle.

https://youtu.be/hZ1DASYd9rk?t=2760
Learn ASP.NET Core MVC (.NET 6) - Full Course

Let me backtrack to here. I am going to really focus on what he is saying.

I should be good for anything programming wise, but there are sometimes weird challenges such as this one.

https://youtu.be/hZ1DASYd9rk?t=2885

So how would you include the partial view in Index?

I'll keep that mystery in mind.

https://youtu.be/hZ1DASYd9rk?t=3040

This is informative. I am still not completely sure what that tag helper is supposed to be, what is that * at the start?

```chtml
@using BulkyBookWeb
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
```

It is a weird kind of import. This is why I really hated ASP.NET back in 2020. But I will ignore the misgiving about its design. I do not really care either way. In fact, I want to prove that it does not matter. The real skill in cloud and webdev is in managing concurrency, not this.

https://youtu.be/hZ1DASYd9rk?t=3126

Let me take a short break.

9:30am. Ok, focus me, stop watching Dave's videos. It is time for ASP.NET. I just had to see what he had to say about the Inquisitor.

https://youtu.be/hZ1DASYd9rk?t=3194

I think I can get into this.

There is an alternative path to what I've taken where instead of even caring about ML, I just studied stuff like this. Had I done this after high school was over, I'd have been a millionaire several times over by now. Instead I stupidly went into trading. I didn't want to work hard then, but I sure do now.

I guess I've matured a little. I guess it can't be helped that without experience, I'd make poor decisions. That's life.

The problem is that I've spent 16 years wandering, and this is a big chunk of time for a human. If my lifespan was a 1,000 years, it really wouldn't matter. I could have plenty of time to correct my direction.

If the Singularity comes to pass, aging is going to become history, so I won't have to worry about my lifespan anymore.

I should aim for that. I am not old enough to the pursuit.

9:40am. https://youtu.be/hZ1DASYd9rk?t=3200

I am distractible right now. But that is fine. It does not matter if I take 8h to get through this course, I will do it.

9:50am. https://youtu.be/hZ1DASYd9rk?t=3394

I am thinking about it. To get ASP.NET, I think I'll need to study a bunch of examples and go through the docs after this course. After that I'll really internalize the framework and will be able to move into webdev should I want to.

https://youtu.be/hZ1DASYd9rk?t=3430

Right now I am a bit lost as to what the difference between Razor pages and MVC is. I'll assume the course will cover this.

10am. Focus me. Learning the web stuff as well as the cloud and maxing them out is the final frontier to me. I really am very complete as a programmer and after I learn this, I will be good at everything. ML is important and highly paid, but it is not vital before the next wave starts. I have the time to do whatever I want.

10:05am. https://youtu.be/hZ1DASYd9rk?t=3581

I am confused. How do I get the hot reload to work.

https://youtu.be/hZ1DASYd9rk?t=3535

Yeah, now it is like here.

It seems he ran it in debug mode.

https://www.youtube.com/results?search_query=.net+hot+reload

No, it is not the debug mode. The preview version is old so it might have been moved somewhere.

https://youtu.be/ibZGWkA7fXE
Let's talk about the removal of hot reload from dotnet watch situation

There is some controversy surrounding the feature. Did it get removed?

https://youtu.be/4S3vPzawnoQ
.NET 6 Hot Reload in Visual Studio 2022, VS Code, and NOTEPAD?!?

I am just watching my time with this. Let me go back to the course. Maybe it will explain how to get the feature to work. If not I'll do a search online.

https://youtu.be/hZ1DASYd9rk?t=3730

Damn it, this did not answer my questions. I am going to have to do some research on how to get hot reloading to work. Let me watch the last video I linked to.

10:25am. https://youtu.be/4S3vPzawnoQ?t=139

Let me take a short break here.

10:45am. Let me resume. Let me figure out hot reloading.

https://youtu.be/4S3vPzawnoQ?t=616

The hot reload button comes once you start the process.

https://youtu.be/4S3vPzawnoQ?t=625

No, it is not appearing for me.

10:55am. Forget it, I do not want to waste any more time on this. I'll just ask on SO.

11am. https://stackoverflow.com/questions/73048719/why-is-the-hot-reload-button-not-showing-up

I've asked. I'll probably get an answer for this. Now nevermind this. Maybe the IDE is buggy or I need to enable some setting. I can still work without it.

https://youtu.be/hZ1DASYd9rk?t=3730

Let me get back to the course.

https://youtu.be/hZ1DASYd9rk?t=3905

I'll have to refresh my memory of how to write properties in F#. Hmmm, how will their defaults work?

https://youtu.be/hZ1DASYd9rk?t=4133

Let me pause here so I can implement this.

```fs
namespace BulkyBookWeb.Models
```

Actually, I never realized that `namespace` is a keyword in F#. I literally never used it. Was this a recent addition to the language or was I ignorant the whole time?

...I was ignorant the whole time. I see.

11:20am. I made an F# file inside a folder and the IDE is not working properly.

https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/members/properties

It started working after restarting the IDE. It seems the language server can have issues. Now let me also add annotations.

```fs
namespace BulkyBookWeb.Models

open System
open System.ComponentModel.DataAnnotations

type Category() =
    [<Key>]
    member val Id = -1 with get, set
    [<Required>]
    member val Name = null with get, set
    member val DisplayOrder = -1 with get, set
    member val CreateDateTime = DateTime.Now with get, set
```

Let me start things off like so.

11:30am. https://youtu.be/hZ1DASYd9rk?t=4175

I do not get it. Is the database server supposed to be running in the background?

> There are some libraries, such as the Entity Framework (System.Data.Entity) that perform custom operations in base class constructors that don't work well with the initialization of automatically implemented properties. In those cases, try using explicit properties.

Good thing I saw this warning. Still what do I do about it? Nevermind it for now.

11:35am. Right now it feels like I am stuck. It might have been better to have used C# for this assignment. I'll open a new project in it later.

Right now I need to figure out how to get a SQL server going.

https://youtu.be/hZ1DASYd9rk?t=292

I guess I should try installing SQL server.

https://www.microsoft.com/en-us/sql-server/sql-server-downloads

Should I get the express or the regular version? I already have it installed from before, but I am just not sure how to run it.

Wait, I see that in the SQL configuration manager there is something. Yeah, it is running in the background and even taking up memory.

11:45am. Ok, I do have some kind of server running it seems. For some reason it has exactly the same name as my computer.

https://youtu.be/hZ1DASYd9rk?t=4149

Ok, nevermind. Let me just play along with what I have. I'll assume I have enough for now. This is way more confusing to me than it should be.

https://youtu.be/hZ1DASYd9rk?t=4172

The version he has is similar to mine. Ok.

12:05pm. I just realized that VS itself has a bunch of stuff for dealing with servers. Maybe I do not need the SMSS for connecting to the server? Nevermind it for now.

At 452m downloads, EntityFrameworkCore sure is popular. All this just shows how out of touch I am with the nuts and bots of commercial programming. Commercial programming is all about databases.

```fs
namespace BulkyBookWeb.Data

open Microsoft.EntityFrameworkCore

type ApplicationDbContext() =
    inherit DbContext()
```

I've gotten this far. Let me continue moving forward.

https://youtu.be/hZ1DASYd9rk?t=4785

Mhhh, I am not sure how to deal with uninitialized properties in F#. I actually don't know how to code this in the language. I might have to go into C#.

```fs
type ApplicationDbContext(opts) =
    inherit DbContext(opts)

    [<DefaultValue>]
    val mutable q : int
```

Instead of switching languages, should I try to use this approach?

No, I think I am better off switching here. Who knows how the reflection the thing is doing will interact with the F# code. I was prepared for everything but uninited properties.

> There are some libraries, such as the Entity Framework (System.Data.Entity) that perform custom operations in base class constructors that don't work well with the initialization of automatically implemented properties. In those cases, try using explicit properties.

```fs
namespace BulkyBookWeb.Data

open Microsoft.EntityFrameworkCore
open BulkyBookWeb.Models

type ApplicationDbContext(opts) =
    inherit DbContext(opts)

    member val Categories = Unchecked.defaultof<Category> with get, set
```

This will just end up being a null.

```fs
namespace BulkyBookWeb.Models

open System
open System.ComponentModel.DataAnnotations

type Category() =
    [<Key>]
    member val Id = 0 with get, set
    [<Required>]
    member val Name = Unchecked.defaultof<string> with get, set
    member val DisplayOrder = 0 with get, set
    member val CreateDateTime = DateTime.Now with get, set
```

I want to give this a try.

> There are some libraries, such as the Entity Framework (System.Data.Entity) that perform custom operations in base class constructors that don't work well with the initialization of automatically implemented properties. In those cases, try using explicit properties.

It says `System.Data.Entity`. Maybe the newer Entity framework is not busted for F#. I do not want to switch after all, let me try pushing through with F#. If it fails, I'll move to C#. The amount of code written so far is insignificant anyway.

12:25pm. Let me stop here for now. This was a decent morning session.

On one hand, the difficulty of this is not significant. But the way it has been structured prevents me from using any of my previous skills to easily digest it. But that will hold only to a point. Once I get through the initial stages, gravity will reassert itself and I will be able to fall into proper programming."

---
## [wincent/wincent](https://github.com/wincent/wincent)@[877f81e8f9...](https://github.com/wincent/wincent/commit/877f81e8f9e56d3cf884ad0695b276b2dd193634)
#### Wednesday 2022-07-20 10:58:49 by Greg Hurrell

chore(ssh): add notes on `TCPKeepAlive` etc to Codespaces config

From `man ssh_config`:

     TCPKeepAlive
             Specifies whether the system should send TCP keepalive
             messages to the other side.  If they are sent, death of the
             connection or crash of one of the machines will be properly
             noticed.  However, this means that connections will die
             if the route is down temporarily, and some people find it
             annoying.

             The default is yes (to send TCP keepalive messages), and
             the client will notice if the network goes down or the
             remote host dies.  This is important in scripts, and many
             users want it too.

             To disable TCP keepalive messages, the value should be set
             to no.  See also ServerAliveInterval for protocol-level
             keepalives.

I have done a fair bit of connection troubleshooting over the last week
or so, and was wondering if this might help. As the docs say, when this
is `yes` (the default), "connections will die if the route is down
temporarily". I am not sure how long a route can be down "temporarily"
without it actually being fatal to the connection, but it wouldn't seem
to hurt to turn this to `no` in case it does help in some rare cases.

In reality, however, there is _no_ value in changing this setting,
because of the way codespaces work: you run `gh cs ssh` and what
actually happens under the covers is your `ssh` command connects to
_localhost_ (that connection is never going to die under normal
circumstances) and `gh` takes care of proxying the actual traffic via
magical means. So in this commit, I'm just putting a comment in the
config explaining all of this.

In any case, I don't need anything special to notice when one of these
connections is down anyway: I'm usually actively using the SSH session
interactively if I care. For this reason, there's _also_ no benefit in
turning on `ServerAliveInterval` (defaults to 0) either. Leaving these
at their defaults, which means they do nothing:

     ServerAliveCountMax
             Sets the number of server alive messages (see below) which
             may be sent without ssh(1) receiving any messages back from
             the server.  If this threshold is reached while server
             alive messages are being sent, ssh will disconnect from the
             server, terminating the session.  It is important to note
             that the use of server alive messages is very different
             from TCPKeepAlive (below).  The server alive messages are
             sent through the encrypted channel and therefore will
             not be spoofable.  The TCP keepalive option enabled by
             TCPKeepAlive is spoofable.  The server alive mechanism is
             valuable when the client or server depend on knowing when a
             connection has become unresponsive.

             The default value is 3.  If, for example,
             ServerAliveInterval (see below) is set to 15 and
             ServerAliveCountMax is left at the default, if the
             server becomes unresponsive, ssh will disconnect after
             approximately 45 seconds.

     ServerAliveInterval
             Sets a timeout interval in seconds after which if no data
             has been received from the server, ssh(1) will send a
             message through the encrypted channel to request a response
             from the server.  The default is 0, indicating that these
             messages will not be sent to the server.

---
## [paul-maidment/assisted-service](https://github.com/paul-maidment/assisted-service)@[564650feca...](https://github.com/paul-maidment/assisted-service/commit/564650feca372064314282d98d6fd9c6ee69bd2c)
#### Wednesday 2022-07-20 11:10:45 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition (#4072)

For context, this is a service-side follow-up to:

https://github.com/openshift/assisted-installer-agent/pull/388

and also this small agent fix https://github.com/openshift/assisted-installer-agent/pull/403

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, when a user imports a cluster, we will inspect the `params.NewImportClusterParams.APIVipDnsname`
parameter and extract:

- The cluster name
- The cluster base domain

The cluster name will override the name given in `params.NewImportClusterParams.Name`,
see diff comment for more information on why.

The cluster base domain will be used to set the `BaseDNSDomain` of the
cluster, because up until now we didn't set it for imported cluster.

The reason `BaseDNSDomain` and `Name` have to be correctly set is
because the DNS validations use them to construct the domain names
that are being validated.

Also updated some validation messages for the API connectivity check and
DNS validations.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [robtfm/bevy](https://github.com/robtfm/bevy)@[4847f7e3ad...](https://github.com/robtfm/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Wednesday 2022-07-20 12:57:45 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [kittywhiskers/dash](https://github.com/kittywhiskers/dash)@[67ceda1b5a...](https://github.com/kittywhiskers/dash/commit/67ceda1b5aa0c51f1fdce4fb71ccba1922e880f6)
#### Wednesday 2022-07-20 14:14:56 by fanquake

Merge #18295: scripts: add MACHO lazy bindings check to security-check.py

5ca90f8b598978437340bb8467f527b9edfb2bbf scripts: add MACHO lazy bindings check to security-check.py (fanquake)

Pull request description:

  This is a slightly belated follow up to #17686 and some discussion with Cory. It's not entirely clear if we should make this change due to the way the macOS dynamic loader appears to work. However I'm opening this for some discussion. Also related to #17768.

  #### Issue:
  [`LD64`](https://opensource.apple.com/source/ld64/) doesn't set the [MH_BINDATLOAD](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) bit in the header of MACHO executables, when building with `-bind_at_load`. This is in contradiction to the [documentation](https://opensource.apple.com/source/ld64/ld64-450.3/doc/man/man1/ld.1.auto.html):
  ```bash
  -bind_at_load
       Sets a bit in the mach header of the resulting binary which tells dyld to
       bind all symbols when the binary is loaded, rather than lazily.
  ```

  The [`ld` in Apples cctools](https://opensource.apple.com/source/cctools/cctools-927.0.2/ld/layout.c.auto.html) does set the bit, however the [cctools-port](https://github.com/tpoechtrager/cctools-port/) that we use for release builds, bundles `LD64`.

  However; even if the linker hasn't set that bit, the dynamic loader ([`dyld`](https://opensource.apple.com/source/dyld/)) doesn't seem to ever check for it, and from what I understand, it looks at a different part of the header when determining whether to lazily load symbols.

  Note that our release binaries are currently working as expected, and no lazy loading occurs.

  #### Example:

  Using a small program, we can observe the behaviour of the dynamic loader.

  Conducted using:
  ```bash
  clang++ --version
  Apple clang version 11.0.0 (clang-1100.0.33.17)
  Target: x86_64-apple-darwin18.7.0

  ld -v
  @(#)PROGRAM:ld  PROJECT:ld64-530
  BUILD 18:57:17 Dec 13 2019
  LTO support using: LLVM version 11.0.0, (clang-1100.0.33.17) (static support for 23, runtime is 23)
  TAPI support using: Apple TAPI version 11.0.0 (tapi-1100.0.11)
  ```

  ```cpp
  #include <iostream>
  int main() {
  	std::cout << "Hello World!\n";
  	return 0;
  }
  ```

  Compile and check the MACHO header:
  ```bash
  clang++ test.cpp -o test
  otool -vh test
  ...
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE

  # Run and dump dynamic loader bindings:
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=no_bind.txt ./test
  Hello World!
  ```

  Recompile with `-bind_at_load`. Note still no `BINDATLOAD` flag:
  ```bash
  clang++ test.cpp -o test -Wl,-bind_at_load
  otool -vh test
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE
  ...
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=bind.txt ./test
  Hello World!
  ```

  If we diff the outputs, you can see that `dyld` doesn't perform any lazy bindings when the binary is compiled with `-bind_at_load`, even if the `BINDATLOAD` flag is not set:
  ```diff
  @@ -1,11 +1,27 @@
  +dyld: bind: test:0x103EDF030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x103EDF030 = 0x7FFF70C9FA58
  +dyld: bind: test:0x103EDF038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x103EDF038 = 0x7FFF70CA12C2
  +dyld: bind: test:0x103EDF068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x103EDF068 = 0x7FFF70CA12B6
  +dyld: bind: test:0x103EDF070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x103EDF070 = 0x7FFF70CA1528
  +dyld: bind: test:0x103EDF080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x103EDF080 = 0x7FFF70C9FAE6
  <trim>
  -dyld: lazy bind: test:0x10D4AC0C8 = libsystem_platform.dylib:_strlen, *0x10D4AC0C8 = 0x7FFF73C5C6E0
  -dyld: lazy bind: test:0x10D4AC068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x10D4AC068 = 0x7FFF70CA12B6
  -dyld: lazy bind: test:0x10D4AC038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x10D4AC038 = 0x7FFF70CA12C2
  -dyld: lazy bind: test:0x10D4AC030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x10D4AC030 = 0x7FFF70C9FA58
  -dyld: lazy bind: test:0x10D4AC080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x10D4AC080 = 0x7FFF70C9FAE6
  -dyld: lazy bind: test:0x10D4AC070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x10D4AC070 = 0x7FFF70CA1528
  ```

  Note: `dyld` also has a `DYLD_BIND_AT_LAUNCH=1` environment variable, that when set, will force any lazy bindings to be non-lazy:
  ```bash
  dyld: forced lazy bind: test:0x10BEC8068 = libc++.1.dylib:__ZNSt3__113basic_ostream
  ```

  #### Thoughts:
  After looking at the dyld source, I can't find any checks for `MH_BINDATLOAD`. You can see the flags it does check for, such as MH_PIE or MH_BIND_TO_WEAK [here](https://opensource.apple.com/source/dyld/dyld-732.8/src/ImageLoaderMachO.cpp.auto.html).

  It seems that the lazy binding of any symbols depends on whether or not [lazy_bind_size](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) from the `LC_DYLD_INFO_ONLY` load command is > 0. Which was mentioned in [#17686](https://github.com/bitcoin/bitcoin/pull/17686#issue-350216254).

  #### Changes:
  This PR is one of [Corys commits](https://github.com/theuni/bitcoin/commit/7b6ba26178d2754568a1308d3d44e038e9ebf450), that I've rebased and modified to make build. I've also included an addition to the `security-check.py` script to check for the flag.

  However, given the above, I'm not entirely sure this patch is the correct approach. If the linker no-longer inserts it, and the dynamic loader doesn't look for it, there might be little benefit to setting it. Or, maybe this is an oversight from Apple and needs some upstream discussion. Looking for some thoughts / Concept ACK/NACK.

  One alternate approach we could take is to drop the patch and modify security-check.py to look for `lazy_bind_size` == 0 in the `LC_DYLD_INFO_ONLY` load command, using `otool -l`.

ACKs for top commit:
  theuni:
    ACK 5ca90f8b598978437340bb8467f527b9edfb2bbf

Tree-SHA512: 444022ea9d19ed74dd06dc2ab3857a9c23fbc2f6475364e8552d761b712d684b3a7114d144f20de42328d1a99403b48667ba96885121392affb2e05b834b6e1c

---
## [Fabizocker456/test](https://github.com/Fabizocker456/test)@[46651cb565...](https://github.com/Fabizocker456/test/commit/46651cb565757f7b0f71269dd463fc0bf19b8e8a)
#### Wednesday 2022-07-20 14:34:58 by Fabizocker456

idk

Article the Third:
	Where a crime of the kidneys has been committed, the accused should
	enjoy the right to a speedy diaper change.  Public announcements and
	guided tours of the aforementioned are not necessary.
Article the Fourth:
	The decision to eat strained lamb or not should be with the "feedee"
	and not the "feeder".  Blowing the strained lamb into the feeder's
	face should be accepted as an opinion, not as a declaration of war.
Article the Fifth:
	Babies should enjoy the freedom to vocalize, whether it be in church,
	a public meeting place, during a movie, or after hours when the
	lights are out.  They have not yet learned that joy and laughter have
	to last a lifetime and must be conserved.
		-- Erma Bombeck, "A Baby's Bill of Rights"

---
## [Fabizocker456/test](https://github.com/Fabizocker456/test)@[dc9fda0790...](https://github.com/Fabizocker456/test/commit/dc9fda07900a42c32548fb9c7198793a475d457a)
#### Wednesday 2022-07-20 14:38:20 by Fabizocker456

idk

	There was a mad scientist (a mad... social... scientist) who kidnapped
three colleagues, an engineer, a physicist, and a mathematician, and locked
each of them in seperate cells with plenty of canned food and water but no
can opener.
	A month later, returning, the mad scientist went to the engineer's
cell and found it long empty.  The engineer had constructed a can opener from
pocket trash, used aluminum shavings and dried sugar to make an explosive,
and escaped.
	The physicist had worked out the angle necessary to knock the lids
off the tin cans by throwing them against the wall.  She was developing a good
pitching arm and a new quantum theory.
	The mathematician had stacked the unopened cans into a surprising
solution to the kissing problem; his dessicated corpse was propped calmly
against a wall, and this was inscribed on the floor:
	Theorem: If I can't open these cans, I'll die.
	Proof: assume the opposite...

---
## [A-freedom/beamCalculator](https://github.com/A-freedom/beamCalculator)@[546d60367a...](https://github.com/A-freedom/beamCalculator/commit/546d60367a6e01c9c28511f9e7227b1198c043df)
#### Wednesday 2022-07-20 14:49:42 by A-freedom

I can't get the deflection to work if the supports are in the center of the beam by using the integration method ,there is no problem with the code the code run exactly like I want to run , but I believe that the problem is in my 'MATH' ,since it seems like I will not be able to solve it in the moment ,so I will try the singularity function method

I did disable calculating deflection because I couldn't to make it work so I will star redoing my logic for the start in hope that will make a change .

sofat I have been able to get the defliction function work with some cases but still there are some bugs need to be fix like the one with  Exam:Mid_Term 2022

note:: now all function start from there local zero I find that this methond working just find and there is no need to change it. And If needed it will be way easier to just convert the output than refracting the source code. So from now and then the locals zeros will be the official method

and after two days of doing nothing I fixed the bug, I found the bug which was a laze shit I did with the 'd' variable when I was refactoring the code in calculateDeflection line 233

Now we can calculate reactions from supports

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[8aff471f54...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/8aff471f542ae7ac8407f3c0fae93bda9747e722)
#### Wednesday 2022-07-20 16:02:40 by NeroOneTrueKing

Goat rework part 2 -- better boons!

Offer corpses directly to the Goat for credit.
Kill enemies with a drooling weapon (and the Goat auto-eats their corpse) for a reduced amount of credit.
Spread the Goat's influence for credit.

Once you've accumulated enough credit, 'apply'ing the holy symbol will offer a variety of boons from the Goat, costing some credit.

 - healing:      the effects of a potion of Goat's Milk, madness included
 - vitality:     cures Sterility, or, the effects of a potion of restore ability (minus its sanity recovery)
 - blessing:     the effects of a scroll of remove curse
 - fortune:      removes negative luck and adds some more luck on top
 - intervention: temporarily summons some tame Dark Young

If you have accumulated enough credit (overall, not your current balance), the following three perma-boons are also available, and the standard boons are stronger.
 - bite:         acidify your weapon
 - hunger:       drool your weapon
 - knowledge:    gain the Word of Knowledge

Credit gain suffers diminishing returns, so if you want a perma-boon, spend your credit on lesser boons along the way!

Numbers may still need tweaking.

---
## [Fabizocker456/test](https://github.com/Fabizocker456/test)@[e1aa7e74eb...](https://github.com/Fabizocker456/test/commit/e1aa7e74eb6f79185a569e236418190f2f354da0)
#### Wednesday 2022-07-20 16:21:36 by Fabizocker456

idk

"How do you know she is a unicorn?" Molly demanded.  "And why were you afraid
to let her touch you?  I saw you.  You were afraid of her."
	"I doubt that I will feel like talking for very long," the cat
replied without rancor.  "I would not waste time in foolishness if I were
you.  As to your first question, no cat out of its first fur can ever be
deceived by appearances.  Unlike human beings, who enjoy them.  As for your
second question --"  Here he faltered, and suddenly became very interested
in washing; nor would he speak until he had licked himself fluffy and then
licked himself smooth again.  Even then he would not look at Molly, but
examined his claws.
	"If she had touched me," he said very softly, "I would have been
hers and not my own, not ever again."
		-- Peter S. Beagle, "The Last Unicorn"

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2d5cae98a3...](https://github.com/mrakgr/The-Spiral-Language/commit/2d5cae98a38f2b5aee75bb15fe02138249ded233)
#### Wednesday 2022-07-20 16:31:39 by Marko Grdinić

"1:05pm. Let me just finish ice cream and I will resume.

1:30pm. Let me resume. Let stop reading that HN thread on EE wages.

https://youtu.be/hZ1DASYd9rk?t=4896

I was here last.

https://youtu.be/hZ1DASYd9rk?t=4943

C#'s autocomplete here is really cool. I had no idea that existed.

https://youtu.be/hZ1DASYd9rk?t=4961

Damn, I do not have this method. Just what did it change to? Let me check out all the add methods with generics.

Wait, I see it. It did not change. It is just that the chain type changes.

```fs
        builder
            .Services
            .AddDbContext<ApplicationDbContext>()
            .AddControllersWithViews()
            .AddRazorRuntimeCompilation()
```

Hopefully this should work.

```fs
.AddDbContext<ApplicationDbContext>(fun options -> options.UseSqlServer())
```

I need this to work, but it does not even after I've installed the relevant package. Do I need to open some namespace? Let me first restart the IDE.

...Nope, neither restarting nor opening the relevant modules is doing anything for me. Let me watch the video for a bit longer, and if I don't get an idea I'll switch to C#.

Wait, wait, I see that he is using the entity framework core.

```fs
.AddDbContext<ApplicationDbContext>(fun o -> o.UseSqlServer() |> ignore)
```

Finally figured it out. Ghhhh...Let me march on.

```fs
.AddDbContext<ApplicationDbContext>(fun o -> o.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")) |> ignore)
```

Ok.

1:55pm. https://www.entityframeworktutorial.net/efcore/entity-framework-core-migration.aspx

I am a bit confused what the point of doing migrations is.

https://stackoverflow.com/questions/38173404/the-term-add-migration-is-not-recognized
> Just install Microsoft.EntityFrameworkCore.Tools package from nuget:

i see. Let me give it a try.

```
(base) PM> add-migration AddCategoryToDatabase
Build started...
Build succeeded.
Microsoft.EntityFrameworkCore.Infrastructure[10403]
      Entity Framework Core 6.0.7 initialized 'ApplicationDbContext' using provider 'Microsoft.EntityFrameworkCore.SqlServer:6.0.7' with options: None
The project language 'F#' isn't supported by the built-in IMigrationsCodeGenerator service. You can try looking for an additional NuGet package which supports this language; moving your DbContext type to a C# class library referenced by this project; or manually implementing and registering the design-time service for the programming language.
```

Sigh. Ok, I see. For this particular course I should just move to C#. I really should not treat it as a programming course. You can't really call this programming.

2:10pm. Ah, damn it. Let me go back through the video.

2:15pm. Oh, I see. It seems the C# version of the project has hot reload in fact.

2:25pm. I did the migration in a C# project. There are too many surprising aspects to using ASP.NET, but nevermind that for now. Let me push forward. Where was I?

2:35pm. https://youtu.be/hZ1DASYd9rk?t=5465

It will create an optimized version of the SQL query, and it will automatically run that query on the database.

https://youtu.be/hZ1DASYd9rk?t=5465

From the perspective of programming, so far everything in the course is extremely weird. No wonder I got so mad in 2020 when I tried using this as a part of grasping how to do a language server. Rather than using C# to make web apps, it is more like using tools which are using C# itself. So far the course is 1.5h in and I've written only a bit over a dozen lines of code, each of them very lightweight. Maybe things will change a bit later.

https://youtu.be/hZ1DASYd9rk?t=5495

Agh, it is not colon, but equal. I was wondering whether that was right, and it turns out it was an error.

2:40pm. What did `update-database` do just now?

2:45pm. https://youtu.be/hZ1DASYd9rk?t=5556

So far so good. I really wonder where it is putting this database.

Let me just continue moving forward.

Focus me. I should be able to finish this course today. After that I'll have time to digest it.

3pm. https://youtu.be/hZ1DASYd9rk?t=5804

This course is slowly chipping away at my will. My 6.5 years of experience as a programmer literally don't matter at all for this. Even after I finish the course, I am not sure I'd be willing to use ASP.NET for anything. I might want to try Svelte after this.

https://youtu.be/hZ1DASYd9rk?t=5804

But let me finish it. I already over 50% done. I might as well go all the way.

https://youtu.be/hZ1DASYd9rk?t=5964

How did he insert the date like that?

3:15pm. https://youtu.be/hZ1DASYd9rk?t=6126

C#'s autocomplete is shockingly good.

https://youtu.be/hZ1DASYd9rk?t=6257

Not a fan of automatic type inference.

https://youtu.be/hZ1DASYd9rk?t=6441

Why isn't the model named?

3:30pm. Why is it necessary to even declare the type of the model?

3:35pm. https://youtu.be/hZ1DASYd9rk?t=6534

I've gotten an urge to just watch this for a bit.

But let me fight against it. Right of all, let me put an item into the table. I have no idea how he inserted it, but there is a way to do it.

```fs
> System.DateTime.Now.ToString();;
val it: string = "7/20/2022 3:37:11 PM"
```

Yeah, this works as input. Ok. I think he must have pressed something to get the default value, but I am not sure what. Let me check the comments.

No solution there.

Nevermind, let me move forward. The next I have to take care of the view.

3:50pm. Yeah, it works fine. I think I am getting into the ASP.NET way of doing things.

https://youtu.be/hZ1DASYd9rk?t=6800

This copy pasting he did for the theme is so nasty. He should have created a separate .css file for the navbars.

I'll try doing that myself after I finish the chapter. Right now I am in the watching mood.

4:05pm. https://youtu.be/hZ1DASYd9rk?t=7143

Let me pause here, I need a break.

I feel like I am getting a grasp for ASP.NET now. I see that the structure of a ASP.NET program has a lot of similarity to an Elm or a Svelte one. There are the views, but there is also the plumbing. But whereas with the two languages I mentioned, I needed only 5m to grasp their essence, I only noticed the similarity with ASP.NET after 2 hours.

4:30pm. Before, the data flow was completely opaque. This is an indication of bad design. But nevermind that. I'll finish this course. I might want to spread it over two days. I do not feel like rushing to complete it today.

...I am looking through the TOC, and I see the Azure part is only the last 12m. That is no big deal.

Today I've been getting SSL handshaking errors on 4chan all day. Is there something wrong with its server, or is the problem on my end? None of my other haunts have this issue.

4:35pm. Forget that. It is good that I am getting the errors. I can focus on getting through the course. Let me go back and I will put the CSS themes in. Let me do it.

https://bootswatch.com/

These are the free themes for Bootstrap.

```html
<script src="~/lib/bootstrap/dist/js/bootstrap.bundle.min.js"></script>
```

This confuses me. This file actually isn't there in the folder.

```html
<link rel="stylesheet" href="~/lib/bootstrap/dist/css/bootstrap.min.css" />
```

The same goes for this.

4:50pm. I am confused, since I have the bootstrap themes as css, what is the library itself supposed to be doing?

Also those min files, is the file really missing or is ASP.NET doing the minimization on its own?

I have no idea.

Forget this for now.

5pm. I thought for the navbar he pasted CSS, but it was layout itself.

```html
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
```

Where is this button supposed to be, I can't see it anywhere.

5:05pm. Nope, even if I try adding text it does not work. My HTML knowledge is minimal so who knows what the reason is.

5:30pm. There is some back and forth in the SO issue.

https://youtu.be/hZ1DASYd9rk?t=6886

So far I've managed to get to this point. Following the course has been worth it. I do understand ASP.NET a lot better than before.

There are some mysteries with the way the scripts are included, what the middleware in program.cs does, the overall compilation scheme, but I can see the basic dataflow now. Let me start a Razor project instead of a MVC one. I want to see what the difference is.

5:35pm. I get it. It just uses `asp-pages` to link and does not have the controllers.

https://youtu.be/hZ1DASYd9rk?t=6892

Let me get back to the video. I am almost at the 2h mark. Let me do those icons.

5:40pm. https://youtu.be/hZ1DASYd9rk?t=7190

Let me pause here. Maybe I'll stop here for the day.

5:45pm. Though I haven't finished the course, I feel like I get what ASP.NET is about. In 2020, the design completely perlexed me, but now I do grasp the essence of it.

I am not sure this kind of framework is my cup of tea. But it definitely would be usable.

If I really had the motivation to go this route, I'd need to finish this project and study it for a couple of days, but that would be enough to attain a level of basic proficiency. Right now I don't know how to make webapps yet, but I do know enough to satisfy my curiosity.

6pm. ASP.NET is weird, but it is not fundamentally different from other reactive approaches.

I think that if I really want to make webapps, I should pick up Svelte or Elm, or some F# web solution, and figure out how to communicate with a database. That should not be too hard.

6:10pm. I suppose today went well. ASP.NET's design is weirdly arbitrary, based around side effects, so it took me 8h to go through just 2 from the course. If I was studying a functional framework, I'd be far faster.

I really should focus on the functional approach to this, it would allow me to develop a lot further.

6:10pm. With ASP.NET out of the way, what am I going to do tomorrow? I guess I'll watch some of the networking course.

Could I do anything practical instead? I could check out the functional webdev libraries and so on.

6:25pm. Let me close here. It is fun time. Baldur's Gate. Manga, novels, anime.

Tomorrow, I'll watch some of the networking course while I think what my new goal should be. I really need AWS access to make proper progress in my skills. Right now I am just tidying up loose ends, and I'll be through them soon enough."

---
## [avar/git](https://github.com/avar/git)@[52c092ca17...](https://github.com/avar/git/commit/52c092ca173319e56cb04f37712558b99990199c)
#### Wednesday 2022-07-20 17:03:32 by Ævar Arnfjörð Bjarmason

test-lib.sh: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [aosp-sweet/android_kernel_xiaomi_sweet](https://github.com/aosp-sweet/android_kernel_xiaomi_sweet)@[c6e2bf1a01...](https://github.com/aosp-sweet/android_kernel_xiaomi_sweet/commit/c6e2bf1a011311bbb8b9a396b636ff1d2c5c3f17)
#### Wednesday 2022-07-20 17:07:05 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [jderusse/symfony](https://github.com/jderusse/symfony)@[338daf25c9...](https://github.com/jderusse/symfony/commit/338daf25c9589e2b93b4d7d693b4a49f7da677db)
#### Wednesday 2022-07-20 17:11:02 by Nicolas Grekas

feature #46751 [VarExporter] Add trait to help implement lazy loading ghost objects (nicolas-grekas)

This PR was merged into the 6.2 branch.

Discussion
----------

[VarExporter] Add trait to help implement lazy loading ghost objects

| Q             | A
| ------------- | ---
| Branch?       | 6.2
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | -
| License       | MIT
| Doc PR        | -

This PR packages an implementation of [lazy loading ghost objects](https://www.martinfowler.com/eaaCatalog/lazyLoad.html) in a single `LazyGhostObjectTrait` (as a reminder, a lazy ghost object is an object that is created empty and that is able to initialize itself when being accessed for the first time.)

By using this trait, ppl can easily turn any existing classes into such ghost object implementations.

I target two use cases with this feature (but ppl are free to be more creative):
1. lazy proxy generation for service containers;
2. lazy proxy generation for entities.

In all cases, the generation itself is trivial using inheritance (sorry `final` classes.) For example, in order to turn a `Foo` class into a lazy ghost object, one just needs to do:
```php
class FooGhost extends Foo implements LazyGhostObjectInterface
{
    use LazyGhostObjectTrait;
}
```

And then, one can instantiate ghost objects like this:
```php
$fooGhost = FooGhost::createLazyGhostObject($initializer);
```

`$initializer` should be a closure that takes the ghost object instance as argument and initializes it. An initializer would typically call the constructor on the instance after resolving its dependencies:
```php
$initializer = function ($instance) use ($etc) {
    // [...] use $etc to compute the $deps
    $instance->__construct(...$deps);
};
```

Interface `LazyGhostObjectInterface` is optional to get the behavior of a ghost object but gives a contract that allows managing them when needed:
```php
    public function initializeLazyGhostObject(): void;
    public function resetLazyGhostObject(): bool;
```

Because initializers are *not* freed when initializing, it's possible to reset a ghost object to its uninitialized state. This comes with one limitation: resetting `readonly` properties is not allowed by the engine so these cannot be reset. The main target use case of this capability is Doctrine's EntityManager of course.

To work around the limitation with `readonly` properties, but also to allow creating partially initialized objects, `$initializer` can also accept two more arguments `$propertyName` and `$propertyScope`. When doing so, `$initializer` is going to be called on a property-by-property basis and is expected to return the computed value of the corresponding property.

Because lazy-initialization is *not* triggered when (un)setting a property, it's also possible to do partial initialization by calling setters on a just-created ghost object.

---

You might wonder why this PR is in the `VarExporter` component? The answer is that it reuses a lot of its existing code infrastructure. Exporting/hydrating/instantiating require using reflection a lot, and ghost objects too. We could consider renaming the component, but honestly, 1. I don't have a good name in mind; 2. changing the name of a component is costly for the community and 3. more importantly this doesn't really matter because this is all low-level stuff usually.

You might also wonder why this trait while we already have https://github.com/FriendsOfPHP/proxy-manager-lts and https://github.com/Ocramius/ProxyManager?

The reason is that the code infrastructure in ProxyManager is heavy. It comes with a dependency on https://github.com/laminas/laminas-code and it's complex to maintain. While I made the necessary changes to support PHP 8.1 in FriendsOfPHP/proxy-manager-lts (and submitted those changes [upstream](https://github.com/Ocramius/ProxyManager/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc+author%3Anicolas-grekas)), getting support for new PHP versions is slow and complex. Don't take me wrong, I don't blame maintainers, ProxyManager is complex for a reason.

But ghost objects are way simpler than other kind of proxies that ProxyManager can produce: a trait does the job. While the trait itself is no trivial logic, it's at least plain PHP code, compared to convoluted (but needed) code generation logic in ProxyManager.

If you need any other kind of proxies that ProxyManager supports, just use ProxyManager.

For Symfony, having a simple lazy ghost object implementation will allow services declared as lazy to be actually lazy out of the box (today, you need to install proxy-manager-bridge as an optional dependency.) \o/

Commits
-------

27b4325f78 [VarExporter] Add trait to help implement lazy loading ghost objects

---
## [zacuel/Odin-Css-Final](https://github.com/zacuel/Odin-Css-Final)@[a48ffc95d4...](https://github.com/zacuel/Odin-Css-Final/commit/a48ffc95d462dc9e3203aa6f77558b29bbf84024)
#### Wednesday 2022-07-20 19:15:37 by zacuel

Good Commit Next Commit to be Experimental

As an experiment I am going to fuck shit up with something silly and then pull this commit rather than the sillyness I am about to be committing.

---
## [GuyBronson/EndlessExpanse](https://github.com/GuyBronson/EndlessExpanse)@[dce84ca13d...](https://github.com/GuyBronson/EndlessExpanse/commit/dce84ca13d4a05f6314cfcde8c65805c4d626cab)
#### Wednesday 2022-07-20 20:32:34 by GuyBronson

Merge pull request #38 from Ganransu/master

FUCK YOU KEVIN

---
## [RomanRenders/mern-expenses-app](https://github.com/RomanRenders/mern-expenses-app)@[dad52a5380...](https://github.com/RomanRenders/mern-expenses-app/commit/dad52a5380a2bcdf939c34397f1b1f207be0c7be)
#### Wednesday 2022-07-20 22:33:52 by Roman Navarro

FUCK THIS SHIT FUCK BRAD TRAVERSY FUCKING FAGGOT BROKEN ASS TUTORIAL

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[1c6a6528ab...](https://github.com/willior/Action_RPG_1/commit/1c6a6528ab2b4e4145891fae8064285cfa1e188a)
#### Wednesday 2022-07-20 22:55:36 by willior

several bug fixes / added RollUp animation

one of the major bugs encountered was that if you were to get stunned during an attack, you wouldn't get stunned. you'd receive the Stun node, but the "Hit" animation would play instead of the "Stun" animation, and you'd be able to act normally. this was particularly troublesome because the same issue did not occur when incurring Stun during other actions/animations - eg., getting stunned during a Roll would cancel the Roll animation and put you in the Stun state immediately.
i don't know exactly why this was happening, but one of the causes was that hit_start() was being called at the beginning of each Hit Animation, as opposed to being called through code. also, it was being called twice. i don't know why. again, this problem was only happening during attack animations. so, instead of calling hit_start() from the Hit animations, we now call it when we determine the Player should be staggered, and it is from this hit_start() function that the animation gets played, and not the other way around. this seems to have fixed the issue.
so that was confusing, but, summarized:
before, when staggered, we'd set the state to HIT and play the "Hit" animation. from this animation, we'd call hit_start(), which handles some of the hit mechanics.
now, when staggered, we call hit_start() via code, which sets the HIT state and plays the "Hit" animation in addition to handling hit mechanics.
also fixed some very minor issues regarding charging and rolls. now, when we roll with a charge, the charging is stopped immediately, but is retained until "roll_check_queued_action()" is called from the Roll Animation, which checks if any applicable actions (namely, attacks & techs) have been buffered. if a tech is queued, we call check_weapon_charge() to determine the tech. if not, we call charge_reset().
a Roll animation calls several functions:
1. roll_state(delta): called every frame of the ROLL state. determines velocity (via boolean roll_moving), plays animation, and monitors attack inputs.
2. roll_stamina_drain(): this should be re-named because it does more than just drain stamina, now. it sets roll_moving to true, which determines how roll_state() sets the velocity. it also sets the evasion_action_bonus, a large flat bonus to the evasion stat during the "moving" period of the Roll.
3. roll_stop(): sets roll_moving to false;
4. roll_check_queued_action(): checks if tech_queued is true, which is determined by the roll_state(delta) function (if a player releases the attack button with with a charge_level > 0, then tech_queued is set to true). if it is, gets the current input_vector, sets the appropriate animationTree blend_position, and calls check_weapon_charge() - which sets tech_queued to false, gives a slight movement boost in the direction the Player is facing, and calls start_tech(stats.charge_level) - then returns out of the function. if that doesn't occur (ie. is tech_queued = false), we reset the charge. then, we check if attack_queued is true, and call evade_animation_finished() if it is. when we do this, we "cancel" the remainder of the roll animation.
5. roll_animation_finished(): resets charge (which is now redundant since we reset the charge in the previous function...) and calls evade_animation_finished().
also note that the last two functions listed check for Stun nodes before anything else. this shouldn't occur because we want the animation to be interrupted when we get stunned, making it so these functions don't get called, but they are there for safety. i should rigidly test whether the checks are still required.
also note that in order to queue a Tech during a Roll, the attack button must be released BEFORE check_queued_action() gets called (when the "get up" frames start). however, regular attacks can still be queued during the "get up" frames, and will be unleashed following the completion of the full roll animation.

---

