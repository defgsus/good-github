## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-21](docs/good-messages/2022/2022-07-21.md)


2,000,135 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,000,135 were push events containing 3,003,898 commit messages that amount to 212,505,123 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [crowlogic/arb4j](https://github.com/crowlogic/arb4j)@[9ef602fc9f...](https://github.com/crowlogic/arb4j/commit/9ef602fc9fd2c1e9042c143f92193cb8cc2c64ab)
#### Thursday 2022-07-21 00:37:57 by Ωω

crow@bb:~$ lookup excellent
4 definitions found

From The Collaborative International Dictionary of English v.0.48
[gcide]:

  Excellent \Ex"cel*lent\, a. [F. excellent, L. excellens, -entis,
     p. pr. of excellere. See {Excel}.]
     1. Excelling; surpassing others in some good quality or the
        sum of qualities; of great worth; eminent, in a good
        sense; superior; as, an excellent man, artist, citizen,
        husband, discourse, book, song, etc.; excellent breeding,
        principles, aims, action.
        [1913 Webster]

              To love . . .
              What I see excellent in good or fair. --Milton.
        [1913 Webster]

     2. Superior in kind or degree, irrespective of moral quality;
        -- used with words of a bad significance. [Obs. or
        Ironical] "An excellent hypocrite." --Hume.
        [1913 Webster]

              Their sorrows are most excellent.     --Beau. & Fl.

     Syn: Worthy; choice; prime; valuable; select; exquisite;
          transcendent; admirable; worthy.
          [1913 Webster]

From The Collaborative International Dictionary of English v.0.48
[gcide]:

  Excellent \Ex"cel*lent\, adv.
     Excellently; eminently; exceedingly. [Obs.] "This comes off
     well and excellent." --Shak.
     [1913 Webster]

From WordNet (r) 3.0 (2006) [wn]:

  excellent
      adj 1: very good;of the highest quality; "made an excellent
             speech"; "the school has excellent teachers"; "a first-
             class mind" [syn: {excellent}, {first-class},
             {fantabulous}, {splendid}]

From Moby Thesaurus II by Grady Ward, 1.0 [moby-thesaurus]:

  216 Moby Thesaurus words for "excellent":
     Al, Attic, Daedalian, Grade A, a cut above, above, adept,
     admirable, adroit, advantageous, aesthetic, aggrandized, ahead,
     apotheosized, apt, artistic, ascendant, auspicious, authoritative,
     awesome, bang-up, banner, beatified, beneficial, benevolent,
     better, big, blue-ribbon, bon, bonny, bonzer, boss, bravura, braw,
     brilliant, bueno, bully, bunkum, canonized, capital, capping,
     champion, chaste, choice, chosen, classic, classical, clean,
     clever, cogent, commendable, cool, coordinated, crack, crackerjack,
     cunning, cute, daedal, dandy, deft, deified, dexterous, dextrous,
     diplomatic, distinguished, eclipsing, elegant, elevated, eminent,
     ennobled, enshrined, enthroned, estimable, exalted, exceeding,
     excelling, exceptional, expedient, expert, extraordinary, fair,
     famous, fancy, fantastic, favorable, fine, finer, first-class,
     first-rate, first-string, glorified, good, goodish, goodly,
     graceful, grand, great, greater, handy, healthy, hear, held in awe,
     helpful, high, high and mighty, higher, immortal, immortalized,
     in ascendancy, in good taste, in the ascendant, ingenious, kind,
     laudable, lofty, magic, magisterial, magnified, major, marked,
     masterful, masterly, matchless, mighty, neat, nice, no mean, noble,
     nonpareil, notable, noteworthy, number one, of choice, of quality,
     one up on, ordinary, outstanding, over, par excellence, peerless,
     pleasant, pleasing, politic, prime, professional, proficient,
     profitable, pure, quality, quick, quiet, quite some, rare, ready,
     regal, remarkable, resourceful, restrained, ripping, rivaling,
     royal, sainted, sanctified, select, shrined, simple, skillful,
     slap-up, slick, smashing, some, sound, sovereign, splendid,
     statesmanlike, sterling, stunning, stylish, subdued, sublime,
     super, superb, supereminent, superior, superlative, supreme,
     surpassing, swingeing, tactful, tasteful, terrific, the best,
     the compleat, the complete, throned, top, top-hole, top-notch,
     topping, transcendent, transcendental, transcending, unaffected,
     understated, unobtrusive, upper, useful, valid, very good,
     virtuoso, virtuous, well-chosen, well-done, without equal,
     workmanlike, worthy

---
## [gitster/git](https://github.com/gitster/git)@[1236c64c85...](https://github.com/gitster/git/commit/1236c64c85c9df4485521a7af11eeee156534099)
#### Thursday 2022-07-21 01:26:07 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

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

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Gurumaragy/Gurumaragy](https://github.com/Gurumaragy/Gurumaragy)@[6abc4d2024...](https://github.com/Gurumaragy/Gurumaragy/commit/6abc4d20241606fa13873ccebcca14660b4779b5)
#### Thursday 2022-07-21 01:35:56 by Gurumaragy

Create {{☎️📞+2348180894378∆}}I want to join occult for ritual money How to join occult for money ritual

I want to join occult for money ritual +2348180894378
  Join,Occult,Money,wealth,Power,Riches,riches,Ritual,Rituals,Fame,Business,Miracle,Protection,Wealth,Secret,Society,Ogboni,Occultism, I want to join occult for money ritual +2348180894378
  Join,Occult,Money,wealth,Power,Riches,riches,Ritual,Rituals,Fame,Business,Miracle,Protection,Wealth,Secret,Society,Ogboni,Occultism Ritual,Nigeria,Ghana,Cameroon,Zambia i want to join occult call +2348180894378 i want to join secret society call+2348180894378 i want to do money ritual call+2348180894378 i want to do money rituals call+2348180894378 i want to be famous call+2348180894378 i want to get rich call+2348180894378 i want to become rich call +2348180894378 i want to get money call+2348180894378 join GURUMARAGY BROTHERHOOD call+2348180894378 i want to make money in nigeria call+2348180894378 +2348180894378 i want to be a millionia call+2348180894378 get quick money call +2348180894378 make real money call  +2348180894378 i want to be whealdy call+2348180894378 join ogboni call+2348180894378 i want to join occult in ghana call+2348180894378 I want to join occult in Nigeria’ call+2348180894378 I want to join real occult in Ghana’ call+2348180894378  how to join occult for ritual money I want to be a great politician I want to be a great man I want to be the richest I want to be a great businessmanI w I want to join occult for money ritual +2348180894378 how to join occult for ritual money I want to be a great politician I want to be a great man I want to be the richest I want to be a great businessmananI to join occult for money rituals  +2348180894378 WhatsApp do not allow poverty to eliminate you, do money rituals to gain fame, riches, power, wealth, and success. Join GURUMARAGY BROTHERHOOD OCCULT, How to join occult to gain all the good things in life it is not your fault if you were born poor but it is your fault if you die power +2348180894378 
Greetings from the great lord lakusta, occult of wealth, fame, power, protection, riches, love, etc…. we are about to share with you a great secret but to start with……… we want to unveil a byte of what we believe and some of the meaning.GURUMARAGY BROTHERHOOD OCCULT society.. is the inclination to pursue a line of work where you carry some level of responsibility and where diplomacy is required in contact with people. the name GURUMARAGY BROTHERHOOD OCCULT gives you the desire to understand and help others with their problems it gives us an inner strength and you become very strong in spirit. though stories and movies have said so many false stories about  GURUMARAGY BROTHERHOOD OCCULT some say they are fallen angels that come down on earth to destroy humanity some say they are sent by the devil from hell to come and destroy men and collect their destiny some say they marine spirit. The Veil of Secrecy Has Been Lifted…. it was not on our initial plan to appear on the internet or in any form of media both traditional or digital but due to the fact that we want to clear the masses curiosity and prove what we stand for, and decide to make a public notice through our press team. After many decades of secrecy and operation in the shadows, we, the illuminated ones from the core of Lucifer(shining star), must begin to form the young membership. More than ever the world needs an elite group of individuals that work to create the fate of the masses. They need us, but we must once again band together What you see in the media today was not the original plan of our organization, and It is not required that you are already super wealthy, or you are already an elite member of government or business…. you must simply seek the light, and seek a world of knowledge that you realize exists, but is not sought after by the masses, You then become enlightened You have made it to the ranks of the worlds most elite group. You have made it here because you chose to seek. Chose to seek the massive knowledge and power that is provided to those that wish to become enlightened. The path of enlightenment is not difficult, but it will not come to those who do not wish to find it.it is for the true seekers with a brave, willing, and strong mind. Never before have we sought out in any outlet be it traditional, print, or digital media a new membership available to the public, and we are not supposed to be on the internet. But we now realize that the public is the ones who seek knowledge, and our family wishes to use it in a way that helps the masses become enlightened, and live in a way that enlightened ones do! Now is the new era of your life! join the great GURUMARAGY BROTHERHOOD OCCULT for fame, wealth, power, protection, etc and eradicate poverty in your life and that of your family the greatest attribute of indefensible people is their capacity to become imperative to the dream and aspirations of others, the secret of happiness is the determination to be happy always, rather than wait for outer circumstance to make one happy THE BENEFITS…………………………….. 1. Spiritual and moral values The GURUMARAGY BROTHERHOOD OCCULT family is a secret society that strives to promote spiritual and moral values. It was founded under principles of love, justice, unity, peace, and relief. The GURUMARAGY BROTHERHOOD OCCULT brings together individuals of goodwill, irrespective of their differences and backgrounds, and ensures that these good men become better in society. 2. Prepares individuals to greatness There are many benefits of being an elite member of the great GURUMARAGY BROTHERHOOD OCCULT such as providing you with the opportunity to fellowship and share knowledge with other members. It also gives you the opportunity to mentor those who want to achieve wealth and overall well-being. The members are reminded to appreciate ethics, morality, and principles, while others find satisf +2348180894378 action in advancing their positions within the society SO THE GOOD NEWS!!!…………………… call  +2348180894378 to join the great GURUMARAGY BROTHERHOOD OCCULT secret society for wealth, power, fame, protection, riches, etc you shall be given an ideals chance to visit the GURUMARAGY BROTHERHOOD OCCULT society temple situated here in Nigeria at OGUN state after your thorough screening and confirmation are completed, no human sacrifice or life needed,  GURUMARAGY BROTHERHOOD OCCULT society brings along wealth and famous in life, you have full access to eradicate poverty away from your life now, build your own dream or someone else will hire you to build theirs.your time is limited so don’t spend it living someone else life It only a member who is been initiated into the fraternity of the occult society has the authority to bring any member to the fraternity, so before you contact any body you must be linked by who is already a member, but if you are lucky to come across this opportunity you are welcome to join us today and realize your dreams life is what we make it, always has been and always will be. Once you become a member you will be rich and famous for the rest of your life, a  GURUMARAGY BROTHERHOOD OCCULT

---
## [Mojave-Sun/mojave-sun-13](https://github.com/Mojave-Sun/mojave-sun-13)@[a7a0e33192...](https://github.com/Mojave-Sun/mojave-sun-13/commit/a7a0e33192ad3fcac5ad64d441f24af6ec852054)
#### Thursday 2022-07-21 01:46:53 by Hekzder

Mob overhaul for DT (#2117)

* Basic mobs

Title

* Start of simple robots

Title

* THE GREAT MOB SOUNDENING

TITLE

* Handies + ranged attack buffs

FASTER!!

* Protectrons, robobrains

* Death sounds and fixes some dumb shit

Title

* NEW ROACHES OMG!!!

WOW!

* Robo sounds

Title

* Mob projectile tweaks

I THINK WE'RE GOOD

* bitty

---
## [RatFromTheJungle/Skyrat-tg](https://github.com/RatFromTheJungle/Skyrat-tg)@[4f9df17cb1...](https://github.com/RatFromTheJungle/Skyrat-tg/commit/4f9df17cb150bd073914527bce381b583cf83657)
#### Thursday 2022-07-21 02:23:42 by magatsuchi

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
## [Rykka-Stormheart/CHOMPStation2](https://github.com/Rykka-Stormheart/CHOMPStation2)@[4704df506b...](https://github.com/Rykka-Stormheart/CHOMPStation2/commit/4704df506bfccd3f4ef9d75a3cf1a4f6f63ca4e3)
#### Thursday 2022-07-21 06:05:43 by Victor Zisthus

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
## [nmagnezi/assisted-service](https://github.com/nmagnezi/assisted-service)@[564650feca...](https://github.com/nmagnezi/assisted-service/commit/564650feca372064314282d98d6fd9c6ee69bd2c)
#### Thursday 2022-07-21 07:22:44 by Omer Tuchfeld

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
## [Kakuta1/kakuta](https://github.com/Kakuta1/kakuta)@[f52bcae0d3...](https://github.com/Kakuta1/kakuta/commit/f52bcae0d3ada94a1f5ac245b3cc65c1bb3defc0)
#### Thursday 2022-07-21 07:55:39 by Kakuta1

Update and rename README.md to I want to join +2348140334665 occult for money ritual 


+2348140334665 #I WANT TO JOIN OCCULT FOR MONEY RITUAL IN DUBAI. #I WANT TO JOIN OCCULT FOR MONEY RITUAL IN NIGERIA. #HOW DO I JOIN THE OCCULT. #I WANT TO JOIN OCCULT FOR MONEY AND POWER IN AFRICA THE SPIRITUAL BROTHERS IS AN ASSOCIATION BLESSED BY THE LORD LUCIFER WHO SHOWER BLESSINGS OF WEALTH, POWER, PROTECTION,RICHES, PROMOTION AND TO MENTION BUT A FEW TO THOSE WHO ARE WILLING TO GIVE THEIR SOULS AS A SIGN OF APPRECIATION TO HIM IN REDEMPTION OF THEIR POOR LIFE. THERE SHOULD BE NO EXCUSE FOR POVERTY SO AS LONG AS THE SOLUTION THE KAKUTA BROTHERS  OCCULT. CONTACT THE SPIRITUAL GRANDMASTER now Call OR WHATSAPP+2348140334665 There is no blood shared if you’ve been accepted to join this organisation you are to pay the price at the age of 75 years you sacrifice yourself to the lord Lucifer this simply means that you are going to die at the age of 85 years. Contact the Grandmaster of THE KAKUTA BROTHERS OCCULT NOW +2348140334665. WELCOME TO THE KAKUTA BROTHERHS OCCULT SOCIETY WHERE TO ACHIEVE ALL YOUR DESIRE IN LIFE, JOIN US NOW AND BE FREE FROM POVERTY AND PAINS, WE ARE HERE TO CHANGE YOU FROM BAD TO GOOD ONCE YOU HAVE THE MIND TO DO WHAT IT TAKE TO MAKE WEALTH AND FORTUNES CALL +2348140334665 NOW! #DO YOU WANT TO JOIN OCCULT SOCIETY TO MAKE MONEY AND TO BE RICH SO THAT PEOPLE WILL RESPECT YOU AND OBEY YOU, #JOIN THE SECRET OF WEALTH BROTHERHOOD OCCULT/ #YOU ARE WELCOME TO THE TEMPLE OF THE KAKUTA BROTHERS WHERE RICHES AND WEALTH ARE BEEN GIVEN TO THE POOR!! #ARE YOU DISAPPOINTED OR TIRED OF THE SITUATION YOU ARE CURRENTLY PASSING THROUGH OR NOT HAPPY BECAUSE ALL YOUR FRIENDS ARE ALREADY RICH BUT YOU ARE STILL LIVING IN POVERTY, #IS YOUR BUSINESS COLLAPSING OR ALREADY COLLAPSED CALL THE KAKUTA BROTHERS TO HELP YOU ON +2348140334665 for  #power #money, #quick riches,and #power to gain contract and The #the Kakuta   brothers occult insists on not to asking any payment for any membership, as it is among the great rule guiding this family. They explain this as a gratitude for personal achievements. Membership is positioned as a great pride and the secret of wealth brotherhood family chooses their members independently and send out private and exclusive invitations but everyone can try to receive such invitation by filling the form the Kakuta brothers occult family connects and unites only the worthiest. That is why you have to be rich, famous and powerful unless you are a member of the fraternity member family, if you want to know how to join the Kakuta brothers occult in #Nigeria and #Ghana#Dubai #canada #Japan #germany just call +2348140334665 THE KAKUTA  BROTHERS AND SHAKE HANDS WITH OUR LORD ” FREEMASONS ” THE GODS OF WEALTH AND RICHES call +2348140334665 Many of us believe that the age of “Money Rituals” is over, but I am sorry to bust your bubble because it still exists in different shapes and sizes. What’s the definition of a Money ritual? Money Rituals are practices by some people who believe they can create wealth for individuals with the use of spells, charms, and sacrifices e.t.c. Money rituals can be traced to various parts of Africa, but it can also be seen in many countries such as India, Nigeria, Ghana and even the west, where people use animals for (sacrifices) without no body effect or human organs of their body, The result of all this is usually seen as “Blood Money” and was commonly attributed to different traditional Gods such as “CHI AKU “(The spirit of wealth), Shankara (The god of thunder), e.t.c. Many people over the years have visited the temple of the secret of wealth brotherhood today they are living in luxury life, and the news of people who have been successful as a member is over the place. Why do you have to sell your kidneys for ipads, iPhones and treasure, why not save your time and join the moving train today without no human blood or fresh, joining the Kakuta brothers occult in Nigeria brings you into the land of the riches where all heart desires is guarantee in DAYS.,and do what your mates would not do and be in real cash and travel to any part of the world Be it #FINANCIAL, #VISA, #MONEY , #WANT TO ASSUME A POSITION, #RITUAL INSTANT MONEY, #SUPERNATURAL WEALTH, #PROTECTION AND #FAME, get in touch. FOR MORE INFORMATION AND INQUIRY CALL +2348140334665 OR Email.... kakutabrotherss@gmail.com

---
## [InvictaLux/gotgirl-nextjs](https://github.com/InvictaLux/gotgirl-nextjs)@[4282859aef...](https://github.com/InvictaLux/gotgirl-nextjs/commit/4282859aefef9a2624feaa5e08db313d85f1c81c)
#### Thursday 2022-07-21 11:58:42 by invictalux

its my fault for sucking at life. gitpush this boulder up this hill one more times a charm

---
## [aramalipoor/awesome-wagmi](https://github.com/aramalipoor/awesome-wagmi)@[058e6ca01c...](https://github.com/aramalipoor/awesome-wagmi/commit/058e6ca01c9b7006d2d907b8b5d6aef4489ebba4)
#### Thursday 2022-07-21 12:08:00 by aram.eth

docs: add Flair platform under products

Flair is a platform that offers [open-source contracts](https://github.com/0xflair/evm-contracts) and React SDK (based on wagmi) for NFT_based projects with features such as NFT Sales, NFT Staking, Revenue Sharing, Allowlists, Royalty Management, etc.

We're using wagmi extensively in our stack and have our React SDK fully open-sourced in https://github.com/0xflair/typescript-sdk

Our React SDK packages aim to be as unopinionated as possible, e.g. https://www.npmjs.com/package/@0xflair/react-openzeppelin

I'm also a sponsor of @tmm for his amazing work on wagmi :)

Feel free to close this PR if you don't think it's the right place to put a link to Flair platform, no hard feelins haha 🌷

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[dd66344197...](https://github.com/treckstar/yolo-octo-hipster/commit/dd66344197fde0fab9b5cf52894f7aa3ffd7d077)
#### Thursday 2022-07-21 12:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Crakenar/WeightApp](https://github.com/Crakenar/WeightApp)@[84a42c861d...](https://github.com/Crakenar/WeightApp/commit/84a42c861da217ff4924e48ac7151ba92657ba81)
#### Thursday 2022-07-21 13:28:59 by Teo Berguerre

fuck you tailwind installation my ass not working FUCK YOU

---
## [JihadZoabi/Aleph](https://github.com/JihadZoabi/Aleph)@[c12065392f...](https://github.com/JihadZoabi/Aleph/commit/c12065392f0045d1a593a1b5298b38b333b55812)
#### Thursday 2022-07-21 13:46:15 by Eyal Z

Despite its cult-status for generations  of  Marxists  and  diabolic  status for opponents, for  many  years  the Communist  Manifesto  actually  had  little  impact  in  the  political world outside the future Germany and radical German-speaking diasporic circles.1 Its initial  print  runs  were  limited,  its circulation  in  its  complete  form2 was  restricted,  its promised translation into other languages was generally long delayed, and Marx and Engels  failed  in  their  efforts  to  import  copies  of  later,  limited  American  editions  to Europe. The Manifesto was read in certain socialist and communist circles for some years after  1848  even  though  the revolutionary  moment  had already  passed  within months  of  its  publication  (Engels  1888:  514-515).  Serious  attention  to  its  contents had to await the world-shaking events of the Paris Commune in 1871, the growth of
 2 a  strong  working  class  movement  committed  to  ‘Continental  Socialism’,  and,  much later, the Bolshevik Revolution. The Commune was crucial because state managers, the security forces, and the bourgeois press claimed that the Communards had been inspired by  that well-known  Communist revolutionary  and  architect  of  conspiracies, Karl  Marx!  The  Commune  resurrected  the  spectre  of  communism  that  had apparently been exorcised for  good  by  the counter-revolutionary turn after the 1848 revolutions.  The  events  of  1871  prompted  broad  interest  in  the  Manifesto  not  only within the dominant classes and state security apparatuses, who wished to discover who  or  what  was  behind  the  insurrection  in  Paris,  but  also  within  the  organized labour movement, which was the main addressee of the Manifesto.3  There  is  a  double  irony  in  this  turn  of  events.  Not  only  was  the  Commune  a spontaneous public uprising  rather  than  a long-planned event but  Marx  and  Engels had intended the Manifesto to end the conspiratorial tradition of German communism in  favour  of  building  a  mass  movement  that  would  grow  stronger  as  capitalism developed.  Subsequent  revolutionary  events  (such  as  the  Russian  Revolutions  in 1917)  and  capitalist  crises  (such  as  the  Great  Depression)  also  spurred waves  of interest in the  Communist  Manifesto. It was in the 20th century that  it won its widest circulation and its hallowed status as 'one of the world's greatest books'. And, just as interest  had  been  spurred  earlier  by  broader  economic  and  political  events,  the collapse of the Soviet Bloc and the apparent demise of the communist movement led to  declining  political  interest  in  the  Manifesto  and  its  contents.  Its  iconic  status continues  nonetheless  because  it  is  now  being  re-interpreted  as  a  prophetic, scientific text on the role of capitalism as the main driving force behind globalization.  The Manifesto as an Historic Document  The Manifesto of the Communist Party  was drafted hastily (in 2-3 weeks at most) in a particular political conjuncture and was intended as a broad statement of the views of  scientific  socialism  in  the  1847-8  period.  It  was  never  intended  as  the  definitive programme of an organized party that would be implemented if, and when, that party won power, whether through peaceful means or violent revolutionary action. Indeed, there was no  organized  Communist  Party as such in  1848  and the very concept  of 'party' referred only to a  broad  current  of  political ideas (Draper 1994: 13-14). Marx
 3 and  Engels  later  described  the  Manifesto  as  an  'historical  document',  insisted  that they had no right to alter it, and therefore refused to correct or update it. At most, its authors  wrote  short  prefaces  to  later  editions  in  German,  French,  Russian,  and English; and Engels honed the first authorized English translation and provided a few addenda  and  corrigenda  in  some  footnotes  (1888).  Overall,  as  Marx  and  Engels noted in their preface to the 1872 German edition:  the  general  principles  laid  down  in  this  Manifesto  are,  on  the  whole,  as correct  today  as  ever.  [But  t]he  practical  application  of  the  principles  will depend,  as the  Manifesto  itself  states,  everywhere  and at  all  times  on  the historical conditions for the time being existing, and for that reason no special stress is laid on the revolutionary measures proposed at the end of Section II (1872: 174-5).   Thus,  while  its  authors  maintained  their  theoretical  commitment  to  the  historical materialist analysis of capitalism and its dynamic and their political commitment to a communist revolution based on a democratic revolution, they certainly changed their views on the more detailed historical analysis, questions of political strategy, and, of course, the famous ten-point ‘party’ programme. The nature of these changes can be seen on a section-by-section basis.   Regarding section I, Marx's views  on  the  dynamic of capital accumulation were still developing.  They  would  receive  their  near-definitive  statement  only  in  Das  Kapital and  even  this  never  achieved  the  completion  Marx  himself  wanted  –  with  at  least three books (those on labour, the state, and crisis and the world market) missing out of  the  six  at  one  time  projected  and  with  two  of  the  ultimately  published  three volumes  being  edited  by Engels  on  the  basis  of Marx’s  often  confused,  confusing, and incomplete draft manuscripts.   Regarding  section  II,  Marx  and  Engels  altered  their  views  on  communism,  party organization,  and  political  democracy  on  several  occasions.  They  did  so  both  as political  events  unfolded  (most  famously  with  the  Paris  Commune,  which  Marx proclaimed had revealed, at last, the proper form of the dictatorship of the proletariat) and  as  parliamentary  democracy  became  more  common  in  advanced  capitalist
 4 states  (Marx  1871;  Marx  and  Engels  1872).  Marx’s  revolutionary  ideas  were  first formulated  before  capitalism  was  consolidated  even  in  England  (the  leading industrial capitalist economy) and at a time when profits rested primarily on absolute surplus-value (which made it hard to concede democratic rights to the working class in comparison with the mass production-mass consumption system that was enabled by the increased importance of relative surplus-value for capitalist expansion).   With the subsequent development of capitalism and capitalist democracy, Marx and Engels would need to consider the prospects of an essentially parliamentary road to socialism  as  opposed  to  their  earlier  view  that  a  bourgeois  democratic  revolution would  make  it  easier  for  the  organized  working  class  and  its  allies  to  overthrow capitalism  through  political  and  military  means.  Both  suggested  that  a  peaceful revolution could be  attained  through parliamentary class struggle rather than violent means and that this was  most  likely  to  occur in America, England, and possibly the Netherlands  –  states  with  relatively  advanced  capitalist  economies,  relatively democratic political regimes, and relatively large and well-organized working classes. The  capacity  of  the  organized  working  class  to  win  votes  where  there  is  universal suffrage  is,  wrote  Engels  (1884:  270),  ‘a  gauge  of  political  maturity’  in  Germany, England,  France,  etc.  But  universal  suffrage  was  certainly  no  guarantee  that socialists  could  win  power  through  a  simple  parliamentary  struggle  without  extra-parliamentary mobilization as well, both to reinforce the parliamentary majority and to prevent  a  military  coup  or  other  form  of  counter-revolution.  Marx  stressed  the importance  of  democratic  majorities  on  several  occasions  (e.g.,  ‘revolutions  will  be made by the majority. No revolution can be made by a party, but [only] by a nation’, Marx 1879: 576). In short, it is probable that both Marx and Engels came to believe, rightly  or  wrongly,  that  the  trend  towards  universal  suffrage  and  the  adoption  of parliamentary  democracy  would  make  it  possible  to  pursue  a  democratic  path  to socialism. This is indicated by the authors’ own arguments regarding the second and third  sections,  namely,  that,  while  the  principles  remain,  the  practical  application must change (Marx and Engels 1872: 174-5).   Regarding section III, which summarizes and criticizes competing views of socialism, there was clearly a massive expansion in the range of socialist and communist views that Marx and Engels would have been obliged to address in any up-dated critique of
 5 alternative  positions.  Indeed,  as  a  later  preface  notes,  ‘it  is  self-evident  that  the criticism  of  Socialist  literature  is  deficient  in  relation  to  the  present-time  because  it comes down only to 1847’ (1872: 175). In addition, the ten-point programme had  ‘in some details become antiquated’ because of industrial advances, extended  political organization  of  the  working  class,  and  the experience  of  the  Paris  Commune,  the political situation  had  been entirely  changed  (1872: 175). We  should also note  that Marx  wrote  little  on  communism  per  se  compared  to  capitalism  after  his  more philosophical period in the 1840s and his political energies were largely devoted from 1867-1874 to organizational work in the International Working Men’s Association and the  campaign  for  democracy.  It  would  also  be  mistaken  to  read  too  much  into  his reflections on post-capitalist social order (for further discussion, see below).  The very brief section IV concerns the ‘position of the communists in relation to the various  existing  opposition  parties’  in  France,  Switzerland,  Poland,  and  Germany and  concludes  with  the  celebrated  exhortation  ‘Proletarians  of  all  countries,  unite!’. Its  authors  generalized  the  original  analysis  beyond  these  initial  four  countries, noting  in  particular  that  the  Manifesto  had  ignored  Russia  and  the  United  States (Marx  and  Engels  1882).  They  also  claimed  that  ‘the  Communists  everywhere support every revolutionary movement against the  existing  social  and  political  order of  things’,  foregrounding  the  property  question  and  labouring  for  the  solidarity  and agreement of the democratic parties of  all  countries  (1872:  174-5).  This is probably why  they  described  the  broad  argument  in  this  section  as  ‘in  principle  still  correct’ (1872: 175).  But  this  conclusion  and its  subsequent  reinforcement provide  only the vaguest  guidelines  for  political  action  and  they  are  based  on  a  ‘strategic essentialism’ that prioritizes a united democratic front based on the property question and led by the most advanced sections of the working class.    The  preceding  comments  might  suggest  that  the  Manifesto  is  an  unimportant document from  the  viewpoint of  Marx's intellectual  development  and this  would  not be  far  wrong.  This  does  not  make  it  unimportant  for  the  development  of  Marxism, socialism, or communism, however, either as such or in terms of their reception and critique. It is nonetheless best to describe its status in the late 19th century and after as a 'classic'  text.  Such a text offers  an  interconnected set of  claims  that  has been superseded  by  later  developments and  is  no  longer  convincing in  its  original  form.
 6 Yet it survives as a theoretical challenge, desideratum, or problem because its way of posing problems remains productive. Thus its authority is ambivalent: it indicates what  must  be  done  but  not  how  to  achieve  it  (Luhmann  1982:  4;  cf.  Baehr  and O’Brien  1994).  This  holds  for  the  Manifesto both  as  a  theoretical statement  about historical materialism and as a proclamation about  the nature and aims of  socialism or  communism  as  a  political  movement.  Thus  it  has  remained  a  central  reference point  for  theoretical  and  political  development  and,  even  as  its  political  relevance appears  increasingly  irrelevant,  this  text  has  helped (and  still  helps)  to  shape  the agenda  of  historical  materialism.  This  was  particularly  important  in  the  nineteenth century  when  the  Manifesto  was  one  of  the  few  works  available  from  Marx  and Engels (as opposed to Engels alone) to introduce historical materialism, the salience of  classes  and  class  struggle,  and  the  basic  economic  and  political  agenda  of revolutionary socialism and communism.  Historical Materialism and Class Struggle   The Communist  Manifesto  draws heavily  on  Marx and  Engels’s  emerging historical materialism from the Economic and Philosophical Manuscripts (Marx 1844) and The Condition  of  the  Working  Class  in  England  (Engels  1845)  through  The  German Ideology  (Marx  and  Engels  1845-46)  and  Poverty  of  Philosophy  (Marx  1847)  to ‘Principles  of  Communism’  (Engels  1847)  as  well  as  on  contemporary  French political theory and practice (Gregory 1978, 1983). It offers a succinct restatement of historical materialism, a positive evaluation of the progressive and revolutionary role of  capitalism  as  propelled  by  its  profit-oriented,  market-mediated  activities,  and  a prophetic sketch  of the  logic  of  capitalism  as a  world-historical and  dynamic  global force. It also repeats earlier arguments from The German Ideology on the economic foundations of capitalist social formations, the development of a centralized capitalist state, the grounding of ruling  ideas  in  the  dominant relations of production, and the connection between social being and social consciousness. In this context, Marx and Engels  argue  that  the contradictions  and  conflicts  of  capitalist  class-society  cannot be resolved solely at an economic level (through trade union struggles); nor purely at a political level – which would leave private property untouched. The proletariat must move from being a class against capital to a class for itself, i.e., move from tactics of local  resistance  to  a  revolutionary  strategy  oriented  to  conquest  of  political  power,
 7 which  will  then  be  used  to  transform  the  economic  foundations  of  contemporary society. This raises important questions about class analysis and class struggle.  The opening section  famously  describes  the history of all  hitherto  existing societies as  the  history  of  class  struggles.  Engels  later  restricted  the  scientific  scope  of  this claim to societies with a written history (1888 English translation: 484n). Even this is insufficient.  For  in  this  form  it  is  essentially  a  propagandistic  claim,  intended  to provide  a  clear  strategic  orientation  and  a  firm  social  basis  for  long-term  political mobilization  in  a  complex  and  unstable  conjuncture.  For  this  was  a  period  in Continental  Europe  when  market  relations  were  still  being  disembedded  from broader political and ideological relations, when the dominance of the capitalist mode of production over other relations of production  was still being established, when an emergent  bourgeoisie  was  still  struggling  in  a  complex  political  conjuncture  to overthrow  or  change  Anciens  Régimes  in  order  to  consolidate  its  hold  in  an emerging  'civil  society',  and  in  a  period  of  widespread  famine  (‘the  hungry  forties’) and  popular  unrest.  In  this  sense  their  claim  is  as  much  a  performative  statement based on a ‘strategic essentialism’ that prioritized class struggle for political ends as it is a foundational scientific statement of historical materialism requiring elaboration and qualification during detailed analyses of actually existing social formations.  This  raises  the  question  whether  Marx’s  and  Engels’s  observations  really  concern the period of primitive accumulation and transition to capitalism or anticipate a future period dominated  by the  logic  of  a  fully consolidated  capitalist mode  of  production. Capitalism has since become the dominant mode of production on a world scale and we  are  now  much  closer  to  the  integrated  world  market  that  was  the  ultimate theoretical  and  practical  horizon  of  Marx’s  analysis  of  the  dynamic  of  capital accumulation (Jessop 2002). Indeed, in this regard, the increasing integration of the world market under the dominance of profit-oriented, market-mediated accumulation has  made  Marx’s  analysis  more  relevant  today  than  in  the  transition  period  during which  the  Manifesto and  Capital  were  written.  But  this  consolidation  has  seen  the social bases of conflicts become far more complex than Marx and Engels envisaged in  the  Manifesto – though  not  necessarily  more  complex  than  the  struggles  they described in their more historical works, such as The Peasant War in Germany, The Class  Struggles  in  France,  The  Eighteenth  Brumaire  of  Louis  Bonaparte,  or
 8 Revolution  and  Counter-Revolution  in  Germany  (Engels  1850,  Marx  1850,  Marx 1852,  and  Engels  1851-52  respectively).  This  makes  it  all  the  more  important  to combine a class perspective with  the  recognition  of other social identities, interests, and  struggles.  Gramsci's  revisions  to  historical  materialism  make  important theoretical and political contributions here (cf. Gramsci 1971, 1995).   From  a  theoretical  viewpoint  we  also  need  to  prioritize  the  critique  of  political economy of capital (as indicated by Marx's Capital) over a political sociology of class. The Manifesto presents only an embryonic critique of political economy and even its political sociology is confusing. Yet the overall description of the dynamic expansion of  capitalism  on  a  world  scale  is  still  powerful  and  prophetic.  It  identifies  what  are still,  some  160  years  later,  major  sites  of  antagonism  in  the  struggle  to  establish bourgeois hegemony not just economically but also in the wider political, social, and ideological sphere. We might note here their stress on the constant revolutionizing of the forces of  production,  the rise of machinofacture  (later  described as the  formally adequate type of labour process for capitalism), the tendential formation of  national economies and national states, the emergence of crises of overproduction coinciding with growing poverty, the resort to economic expansion abroad, the coercive force of international  competition  in  the  world  market,  and  the  growing  significance  of capitalist relations of production as  fetters  on  the  further development of productive forces  and  their  potential  to  free  workers  from  toil  and  poverty.  I  will  comment  on these claims later in  terms  of  their  spatio-temporal significance. The Manifesto  also identifies major sites of antagonism in the struggle to establish bourgeois hegemony not just economically but also more generally that remain significant today.  At this stage in the development of historical materialism, however, there are serious difficulties in the class analysis offered by Marx and Engels in terms of the critique of political  economy  as  well  as  the  political  sociology  of  class.  The  Manifesto  signals the advance that Marx had made (with much help from Engels’ early work on political economy and his analysis of the working class in England) in two respects. First, he retreated  from  his  earlier  grounding  of  the  need  for  revolution  on  a  philosophical anthropology, i.e., a general view about the intrinsic nature of man, to basing it in an economic  and  political  sociology  of  class  relations.  Second,  he  moved  from  his earlier view that the proletariat – those without  property  –  represent  the  interests  of
 9 humankind  in  general  to  a  specific  analysis of  the  proletariat  in  terms  of  the  wage relation  in  capitalism.  But  problems  about  the  nature  of  proletarian  revolution remained  in  the  Communist  Manifesto.  Given  Marx’s  views  on  how  capitalist advances  prepared  ground  for  development  of  revolutionary  consciousness  in proletariat, one might expect the revolution to begin in England, move to France, and then to  Germany.  Yet the Manifesto  was  initially intended for  a  German readership and  Marx  inverted  this  sequence  by  suggesting  that  Germany's  vanguard  role  in Europe in philosophical – if not economic and political – struggle had already led it to adopt  communist  positions.  Moreover,  because  the  German  bourgeoisie  was organizationally  ill-prepared  to  overthrow  the  old  order  and  establish  a  full  liberal bourgeois revolution, its half-hearted  attempts  to  do so would open  a  space  for the German  proletariat  to  push  forward  to  a  communist  revolution.  This  would  only survive, however, if  supported  by the French and English working class  in  an act of international class solidarity.  These  difficulties  are  compounded  by  Marx’s  and  Engels’s  failure  to  provide  a theoretically-grounded definition of classes, resorting to the polarized propagandistic language of “oppressor-oppressed”. It seems that this language is required because pre-capitalist forms of class exploitation are disguised beneath non-economic forms of oppression – whereas capitalist exploitation is based on a formally free exchange in  the  market  place  that  is  nonetheless  rendered  substantively  unequal  by  the distribution  of  private  property  in  the  means  of  production.  Does  this  mean  that rigorous class analysis  can only begin with the emergence  of the wage relation and must then explore their political and ideological overdetermination? The real focus of the  class  analysis  in  the  Manifesto  is  the  bourgeoisie  and  proletariat  with  other classes  fated  to  disappear  or  become  marginal  to  the  main  line  of  class  conflict. Indeed  their  analysis  owes  more  to  the  contemporary  political  sociology  of  class conflict than to a sustained critique of political economy and to the co-authors’ desire to  focus  attention  on  what  they regarded  as the  imminent  revolution.  Hence  their claim that  capitalism  also creates  its  own gravediggers  –  the proletariat.  This  class slowly  begins  to  develop  a  political  class-consciousness  and  learns  to  direct  its struggles  against  the  bourgeoisie  –  every  defeat  is  a  learning  experience  and opportunity to regroup, develop greater solidarity, and to organize through the power
 10 of  association.  Whether  this  is  an  accurate  prediction,  a  performative  claim,  or  an illusion born of revolutionary optimism would be worth exploring.   The Geography of the Manifesto  The  Communist  Manifesto  argues  that  the  global  expansion  of  capital  first postpones,  and  eventually  intensifies,  the  inherent  crisis-tendencies  of  capitalism and  the  prospects  for  communist  revolution  as  capitalism  reaches  its  global limits and can no longer escape a terminal crisis precipitated by working class struggles. It is  common  nowadays  to  claim  that  Marx  and  Engels  anticipated  contemporary accounts  of  globalization  in  the  Manifesto  (Dirlik  2000:  11-12;  Harvey  1996:  2; Renton  2001).  In  this  context,  it  is  said  to  contain  five  substantive  geographical themes (Harvey 2000):  1.  The successive stages in the development of the countryside-city relation and the need to overcome antagonism between exploited rural and urban classes.  2. The  development  of  the  world  market  and  the  resulting  division  of  world  into civilized  and  barbarian  nations  and  a  more  general  centre-periphery  model  of capital  accumulation,  emphasizing  uneven  and  dependent  development  rather than a linear, modernizing catch-up model of economic development. 3. The key role of innovation and investment in transport and communications. 4. The formation  of  national territorial  states  through political  centralization  and the key  role  of  national  markets  and  states  in  promoting  interests  of  national bourgeoisies in their mutual competition. 5.  Communist politics begin at local level and are later organized around the national state  –  this  is  basis  for  international  cooperation  and  global  spread  of  initial revolutionary movements, organized under guidance of communists.   However,  although  Marx  and  Engels  identified  important  spatial  moments  of capitalism in the Manifesto and, indeed, presented the world market as the eventual outcome of capital accumulation, it does not follow that their analysis was essentially spatial.  Indeed,  as  Neil  Smith  notes,  commenting  on  Marx's  work  as  a  whole,  'the lively  spatial  implications  of  Marx's  analyses  were  rarely  developed'  (1984:  81). Moreover, in another seeming paradox, this is especially clear in the Manifesto itself.
 11 For, if it has a grand narrative, it is not a spatial story of inevitable globalization but a temporal story  of inevitable  revolution. It  describes  a  history  of  class  struggles that must culminate in the victory  of  the  proletariat  as  the universal class. When dealing specifically  with  capitalism,  of  course,  it  also  presents  a  spatial  narrative.  It  argues that capitalism is inherently  global  in  its scope and dynamic, involving cosmopolitan production, the world market, the rise of world literature, etc. But this spatialization is still  subordinate  to  a  revolutionary  telos:  its primary  function  is  to universalize  the capital  relation  and  thereby  prepare  the  conditions  for  a  worldwide  revolution. Likewise, as capitalism develops, workers are  concentrated  into  factories  and cities and power is centralized in the hands of a few  large  capitalists.  This  also  serves  to enhance  the  growth  of  revolutionary  consciousness  and  to  politically  isolate  the exploiting class before, finally, the workers of the world unite to overthrow it.   A  similar  subordination  of  space  to  time,  albeit  one  that  endows  capitalism  with  a broad  direction  rather  than  a  specific  telos,  occurs  in  Capital (Postone  1993). This magnum opus  certainly offers  a  spatialized  account  of  primitive  accumulation,  the industrial  revolution,4  and,  indeed,  England's  pioneering,  pre-figurative  role  in industrial capitalism (de te fabula narratur).5 It also offers many incidental comments on space and place, town  and  countryside,  the  social division of labour, changes in means of transportation and communication, colonialism and the world market, and many other spatial themes. When Marx unfolds the basic logic of the fully constituted capitalist  mode  of  production,  however,  he  systematically  privileges  time  over space.6  In  this  respect,  place  and  space  appear  both  as  the  material  support (Graham  2001)  and  material  effect  of  the  logic  of  capitalism  considered  as  an economy  of  time.  Thus  Marx  explains  capital's  self-expansion  in  terms  of  the complex  articulation  between  multiple  concrete  temporalities  and  the  singular abstract  time  of  exchange  value  (Postone  1993:  292-3  and  passim).  He  was  a pioneer  in  both  respects  and,  given  the  absence  of  relevant  concepts in  classical political  economy,  Marx  himself  had  to  develop  an  appropriate  language  for addressing  the  dialectic  among  the  concrete  and  abstract  moments  of  the  time factor.  Among  his  key  concepts  were  labour  time, absolute  surplus  value,  socially necessary  labour  time,  relative  surplus  value,  machine  time,  circulation  time, turnover  time,  turnover  cycle,  socially  necessary  turnover  time,  interest  bearing capital, and expanded reproduction.7 None of this could  have been anticipated from
 12 the ideas in the Communist Manifesto and this indicates the distance that Marx still had to  travel  before  he could  develop  a  well-grounded critique  of  political  economy and grasp the historical specificity of capitalism.  The State and Politics in the Manifesto  As part of its more general development of historical materialism based on ideas first adumbrated in The German Ideology, section one of the Manifesto argues:  Each  step  in  the  development  of  the  bourgeoisie  was  accompanied  by  a corresponding political advance of  that  class.  An  oppressed class under the sway of the  feudal  nobility, an armed  and  self-governing  associations in the medieval  commune;  here  independent  urban  republic  (as  in  Italy  and Germany),  there  taxable  “third  estate”  of  the  monarchy  (as  in  France), afterwards,  in  the  period  of  manufacture  proper,  serving  either  the  semi-feudal or the  absolute  monarchy as a counterpoise against the nobility, and, in fact, cornerstone  of  the great monarchies  in  general,  the bourgeoisie has at last, since the establishment of Modern Industry  and  of  the  world  market, conquered  for  itself,  in  the  modern  representative  state,  exclusive  political sway. The executive of the modern State is but a committee for managing the common affairs of the whole bourgeoisie (Marx and Engels 1848: 486).  This suggests zigs-and-zags, leads-and-lags in the formal constitution of the modern state  –  it  took  economic  and  political  struggles,  trial-and-error  experimentation  to develop  the  modern  representative state.  Unsurprisingly,  given  the  contradiction at the  heart  of  the  democratic  constitution,  i.e.,  it  secures  the  political  power  of  the majority  on  condition  they  refuse  to  claim  social  power  and  it  secures  the  social power  of  the  dominant  classes  on  condition  that  they  abandon  their  monopoly  on political  power  (Marx  1850:  79,  131),  this  is  also  a  fragile  political  regime.  It  is vulnerable to destabilization through the refusal of the subordinate classes to accept only  political  emancipation  and/or  the  refusal  of  the  dominant  class(es)  to  be satisfied with social domination (i.e., with the  de  facto  subordination  of  the exercise of state power to the imperatives of capital accumulation) and their desire to restore their  hold  on political  power. Subsequent  work by  Marx and  Engels would  develop these ideas  and  move  them  away from  the  apparently ‘instrumentalist’  claim  in  the
 13 last  sentence  of  the  quotation  above  –  which  others,  at  least,  seek  to  interpret  in terms of the necessary relative autonomy of the state on the grounds that Marx and Engels see it as administering the common affairs of the whole bourgeois class. This raises  interesting  points  of  interpretation  that  are  better  resolved  by  considering subsequent work on the  state  that  examines  specific epochs and conjunctures. For only  later  in  Marx’s  work  do  we  get  an  appropriate  combination  of  general  form analysis, historically  specific institutional analysis, and  conjunctural class analysis of the state in  capitalist social formations. Nonetheless, even on  the basis of what can be  discerned  in  the  Manifesto,  the  analysis  is  a  programmatic  and  inspirational document  and  claims  (holds  out  the  hope  that),  once  a  liberal  democratic  state  is established, the growing numerical and organizational strength of the proletariat and its  allies  will  enable  a  peaceful  transition  to  social  as  well  as  political  power.  Even here  an  inconsistency is  introduced by  Marx and  Engels, who  expect a  proletarian revolution  to  break  out  first  in  undemocratic  Germany  rather  than  a  semi-parliamentary English state.  Bourgeois Hypocrisy Then and Now  The next two sections merit less attention in what must be a short comment on the Manifesto.  The  presentation  of  communist  political  principles  is  best  read  as  an historical  document.  It  is  an  excellent  and  rhetorically  well-crafted  critique  of  the hypocrisy  of  bourgeois  responses  to  communism.  It  is  also  a  fine  statement  of the broader historical materialist principle that the leading ideas of any age are the ideas of the  ruling class. But certain of the views expressed or implied (e.g., on patriarchy and  the  family)  are  best  interpreted  in  their  historical  context.  And  the  ten-point programme was clearly becoming an anachronism by the 1870s.   The third section, on  other  forms of socialism, has been rendered largely irrelevant, as  Marx  and  Engels  themselves  foresaw,  by  the  continued  development  of capitalism.  But  one  can  derive  some  continuing  pleasure  from  noting  how  certain forms of socialism  have  survived to emerge  in  new guise. Few  critical  observers  in Britain today, for example, would fail to recognize in Tony Blair's Labour Government the  same  species  of  socialism that  Marx  dismissed  as  'conservative or  bourgeois socialism', i.e., a movement that wants the bourgeoisie  without  the  proletariat  or,  at
 14 least,  to  lessen  for  the  bourgeoisie  the  cost  of  maintaining  its  rule.  As  Marx  and Engels wrote, 'its socialism consists precisely in the assertion that the bourgeois are bourgeois – in the interests of the working class'. Indeed, this is a feature of the little-lamented  Third  Way  more  generally  –  which  regards  capitalists  as  entrepreneurial wealth-creators who generate the resources needed to pay for the welfare state and whose  beneficent  action  needs  to  motivated  by  higher  incomes,  lower taxes,  and light-touch regulation.    Some Faulty Predictions?  To reinforce the point that the Manifesto should be seen as a classic text, it is worth recalling some of its predictions that have been shown theoretically and empirically – and, in part, even by Marx himself in theoretical terms – to be mistaken or, at best, partial in their application:  • the growing polarization of classes • the growing immiseration (impoverishment) of the working class •  the steady de-skilling of labour power •  the expulsion of men from the labour force in favour of women and children •  the eventual organization of all proletarians into a single political party •  the proletarian rejection of bourgeois morality, religion, and ideology •  the proletarian rejection of nationalism in favour of international solidarity •  the reduction of national differences through accumulation on a world scale •  Germany is  on  the eve  of  a bourgeois  revolution  as a  prelude  to immediate proletarian revolution  It is not worth rehearsing all of the reasons for these errors, which would take a book or two to develop (for an early political critique, see Bernstein 1961; and, for a book-length academic review of the economic predictions, Gottheil 1966). It is worth noting subsequent changes in  economic  and political developments that  would  undermine or  modify  some  of  these  predictions.  First,  Marx  and  Engels  were  writing  during  a period dominated  by primitive  accumulation and  absolute  surplus-value  rather  than relative  surplus-value,  which  would  change  the  dynamic  of  capital  accumulation,
 15 creating  conditions  for  rising  wages  and  expansion  of  the  new  petty  bourgeoisie. This  would  change  the  context  of  class  struggle. Second,  they were  writing  before the  completion  of  bourgeois  democratic  revolutions  and  the  expansion  of opportunities for mass politics inside normal bourgeois democratic conditions. Third, the  Manifesto  was  commissioned  by  the  Communist  League  and  focused  on  the immediate situation in Continental Europe. Thus the increased importance of Russia, the  United  States,  the  Indian  sub-continent,  and  China  (to  name  four  regions  to which  Marx  paid  increasing  attention  economically  and  politically)  and  the  growing integration  of  the  world  market  were  bound  to change  assessments  of  the  political conjuncture,  the  initial  site  of  a  revolutionary  rupture,  and  the  conditions  for  its consolidation (see Marx to Zasulich 1881a-d; Marx and Engels 1882; Husain 2006). And,  fourth,  in  this  context,  the  increasing  importance  of  monopoly  capitalism, changing  forms  of  imperialism, and  the  world  market  would  modify  the  stakes  and forms of class struggle in metropolitan nations.   The Manifesto as a Literary Text  Regardless of its scientific merits, the Manifesto is a powerfully crafted literary text. It combines a number of genres within one overall format – that of the Manifesto, i.e., a ringing  public  declaration  of  theoretical  principles,  political  aims,  and  activities  to achieve them. The decision to publish a manifesto marked a turn away from previous attempts to state  the  principles of the Communist  League  in the form of  a  credo or catechism and was prompted  in  part  by Engels’s recommendation to  Marx  that  ‘we would do best to abandon the catechetical form … since a certain amount of history has to be narrated’ and, hence, write a manifesto that would enable the presentation of  historical  arguments  (Engels  to  Marx,  23-24  November  1847).  Various  scholars have subjected the Manifesto  to  literary,  rhetorical, argumentative, narrative, critical discourse, and other forms of critique. Among the most evident genres are the gothic horror  story,  historical  narrative,  the  catechism,  the  political  programme,  critique, literary review, a cross-examination in court, a theatrical script with different roles for bourgeoisie  and  proletariat,  and  instruction  in  the  meaning  of  a  classless  society compared with contemporary bourgeois society.   Excursus: The 1859 Preface
 16 The declared purpose  of the 1859 Preface is  to provide a clear statement of Marx’s theoretical  development  over  many  years  of  scientific  study  and  to  identify  the guiding threads of his past and current research. It  is  widely  read  as  a  foundational text of historical  materialism but it is often ambiguous, enigmatic,  or obscure. It was written as hastily as the Manifesto (Marx regularly failed to meet deadlines)  in order to get his Contribution  to  the  Critique of Political Economy published  (Marx  needed the money) by enabling it to seem innocuous enough to pass the Prussian censors (Marx pulled his revolutionary punches in favour of making the text appear historical and  für ewig).  Accordingly,  the  Preface  focuses  on  the  general  logic  of  historical development  and  emphasizes  evolutionary  tendencies  that  are  driven  forward  by emerging structural  contradictions  rather than  by  direct revolutionary  action.  This is reflected in the absence of a focus on class struggle that is even more (or, perhaps, not at  all)  remarkable given  that  the Prussian  censors  would know  him  through his association with the Manifesto as well as his political activities. Like the Manifesto, it also deploys many  metaphors;  but  these are not so  much  used  for rhetorical effect as to indicate sites  of  theoretical problems and possible directions of research. Like the Manifesto, it was little read at the time and had little impact. Its guidelines were relegated  to  a  footnote  to  the  first  volume  of  Capital when  this text  was eventually published  (Marx  1886:  82,  85-86n;  cf.  1873:  27-28;  and  1894:  791).  Yet,  like  the Manifesto,  it  has  since  acquired  an  inordinate  significance  for  the  interpretation  of Marx  and  Marxism  –  in  large  part  because  of  its  celebration  by  Engels  as  the definitive statement of the scientific principles and laws of historical materialism and the  importance  of  the  ultimately  determining  role  of  the  economy  in  historical development. This had the result that  [t]he  better-illustrated  discussions  of  the  Manifesto,  the  more  intensely political  analysis  in  The Eighteenth  Brumaire,  and  the  more  exploratory conceptual studies  in the  economic  works,  from  the Grundrisse  through  the various drafts and published volumes of Capital, were then ‘rigorously’ judged against Marx’s ‘guiding’ insights (Carver 1996: xiv).  This  inordinate  attachment  to  the  1859  Preface  can  be  seen  in  the  conflation  that Engels  makes  between  the  Communist  Manifesto  and  arguments  in  the  Preface. Thus, in his preface to the 1888 English translation of the Manifesto, he argues that:
 17  The  Manifesto  being  our  joint  production,  I  consider  myself  bound  to  state that  the  fundamental  proposition  which forms  its  nucleus belongs  to  Marx. That  proposition  is:  That  in  every  historical  epoch,  the  prevailing  mode  of economic production and  exchange,  and the social  organisation  necessarily follows from  it,  form the  basis  upon which is  built  up, and  from  which alone can  be  explained  the  political  and  intellectual  history  of  that  epoch;  that consequently the whole history  of  mankind  (since the dissolution of primitive tribal society, holding land in common ownership) has been a history of class struggles,  contests  between  exploiting  and  exploited,  ruling  and  oppressed classes; that the history of these class struggles forms a series of evolutions in  which,  nowadays,  a  stage  has  been  reached  where  the  exploited  and oppressed  class  –  the  proletariat  –  cannot  attain  its  emancipation  from  the sway  of  the  exploiting  and  ruling class  –  the bourgeoisie  –  without,  at  the same  time,  and  once  and  for  all  emancipating  society  at  large  from  all exploitation,  oppression,  class distinction  and class  struggles (Engels  1888: 517).  Here Engels introduces ideas from the later Preface into his account of the Manifesto but it would be harder to introduce ideas from the Manifesto into the Preface. For, as many  have  noted,  class  and  class  struggle  are  absent  from  the  latter  text.  Prinz (1969)  offers  the  most  plausible  explanation  for  this:  Marx  consciously  suppressed the  revolutionary  passion  and  references  to  class  struggle  that  might  have  been expected because he hoped to reach German public in an officially sanctioned work by misleading Prussian censors about the true import of his long delayed work.  Taking  the  Manifesto and  the  1859  Preface  as  ‘foundational  texts’  of  historical materialism is  deeply problematic.  Indeed  their emblematic  status  as  master  works of historical materialism owes less to Marx than Engels – who promoted them as key documents  in  the  development  of  historical  materialism,  the  incisive  statements  of the  primacy  of  economic  relations,  and  the  basis  for  socialist  political  organization from  the  1880s  onwards.  Gramsci  highlighted  the  1859  Preface  in  his  prison notebooks  because  of  its  radical  implications  for  the  horizons  of  the  political  class struggle  and  the  appropriate  forms  of  revolutionary  activity.  In  particular,  he

Citations (0)

References (51)

Afterword to the Second German Edition
Chapter
Apr 2008
Karl Marx
View
Show abstract
Manifesto of the Communist Party
Article
Jan 1972
K. MarxF. Engels
View
Preface to the German Edition
Chapter
Dec 1968
R. VogelI. TrautscholdE. Werle
View
Principles of communism (1847)
Chapter
Jan 2012
Friedrich Engels
View
Marx and Engels - The unsung heroes of the democratic breakthrough
Article
Jun 1999SCI SOC
A. Nimtz
View
Show abstract
Background and Ulterior Motive of Marx's "Preface" of 1859
Article
Jul 1969
Arthur M. Prinz
View
Uneven Development: Nature, Capital and the Production of Space
Article
Jan 1986
David M. SmithNeil Smith
View
Further Selections from the Prison Notebooks
Article
Nov 1997Italica
Renate HolubAntonio GramsciDerek Boothman
View
Revolution and Counter-revolution in Germany
Book
Jan 1977
Friedrich EngelsKarl Marx
View
Marx's Economic Predictions.
Article
Jun 1968
Maurice DobbF. M. Gottheil
View
Show more

---
## [Supercolony-net/ink](https://github.com/Supercolony-net/ink)@[341c48b965...](https://github.com/Supercolony-net/ink/commit/341c48b965ee4afab580a2eb74a83763201446f3)
#### Thursday 2022-07-21 13:46:46 by xgreenx

metadata crate:
Updated storage layout in the metadata. Introduces the concept of roots and leafs. Root defines the storage key for all sub-tree until there will be another Root. Leafs are common types that are part of the sub-tree and serialized/deserialized together into one storage key.
Replaced 32 bytes storage key with `u32`.
Added validation that all root storage keys don't overlap. Maybe better to add that error or reuse that validator on the `cargo-contract` side to show a more user-friendly error.
`RootLayout` and validator are used in codegen(next commit). The contract is wrapped into `RootLayout`, and we do validation for that tree.
Metadata now contains name for each struct/enum/variant/field. It is useful information because now the storage key is calculated based on the name of struct/enum/variant/field.

storage crate:
Added a new helper crate `storage/codegen`. It contains some useful functional that is used in `ink_storage_derive` and in `ink_lang_codegen` crates. It has a method that returns all types of the struct/enum/unit and a method that finds "salt" in the generics of the struct/enum. It uses magic constant "KeyHolder"(about that you can read in issue) to find salt, so I tried to have only one place where we are using that constant.

Replaced derive implementation of old trait with new one. You can check the tests to see how the implementation looks like. `Storable` recursively call `encode` and `decode` for all fields. `KeyHolder` return key of the salt. `Item` uses `AutoKey` or key specified by the user. I want to highlight that `PreferredKey` only is used with the `AutoItem` trait. If `PreferredKey` is `AutoKey`, then `AutoItem<AutoGenerated>` select auto-generated key, otherwise preferred. So `AutoItem` trait decides that key to use. It is why derive macro only set `PreferredKey`.
Updated drive for `StorageLayout`, now it uses `u32` and pass name of the struct into metadata.

---
## [move-me-to-ipfs-shipyard/Tamatoa](https://github.com/move-me-to-ipfs-shipyard/Tamatoa)@[924e301a89...](https://github.com/move-me-to-ipfs-shipyard/Tamatoa/commit/924e301a8903bbb5c2749aad982c44ab06bf13a0)
#### Thursday 2022-07-21 14:00:25 by Tamatoa

our wine is wine - because raisins have too much sugar - which feeds yeast and candida

:Kristen-Bell mama, it's time i told you the truth about Ricky
:Jimmy-Kimmel i saw Frozen last night - and it was shit

---
## [laminas/laminas-authentication](https://github.com/laminas/laminas-authentication)@[2bdd7faf28...](https://github.com/laminas/laminas-authentication/commit/2bdd7faf28dffe187cd663c58b9c0c9f935ec95d)
#### Thursday 2022-07-21 14:42:00 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [elastic/ml-cpp](https://github.com/elastic/ml-cpp)@[4bc55b3d04...](https://github.com/elastic/ml-cpp/commit/4bc55b3d04ebf5f2341ad75106e67ec3a7a3d3d9)
#### Thursday 2022-07-21 15:29:54 by Tom Veasey

[ML] Logging enhancements plus compilation speed ups  (#2363)

Currently, logging requires one to manage wrapping up calls to many types in core::CContainerPrinter::print.
It would be nice if the logging experience was more streamlined. Another side effect is we ended up including
core/CContainerPrinter.h very widely, in many cases for LOG_TRACE statements which are compiled away
anyway. It would be nice to avoid this.

This PR introduces a pseudo stream manipulator CScopePrintContainers. This is dropped into our logging
macros so that all log lines simply get containers printed automatically. This approach first detects (at compile
time) whether types can be written directly to a std::ostream and uses this approach in preference. I also fixed
some obvious silly inefficiencies in CContainerPrinter. One might ask why not just specialise operator<< for
std::ostream and containers in the std namespace? I did in fact try this, but it turns out other libraries tend
to do this and you can easily get ODR violations. I hit this exact problem because libtorch does this and I
couldn't then compile pytorch_inference.

Separately, our compile times given the total LOC are rather long. One culprit is logging. Just including
CLogger.h adds around 70k lines to the output of the preprocessor and, for my setup, 0.4s for this step
alone to the compile time of file. Therefore, I've also started addressing some of the bottlenecks. I've migrated
LOG_TRACE to really discard the code altogether. This means we can have a special CLoggerTrace.h which
only optionally includes CLogger.h if we're not compiling with EXCLUDE_TRACE_LOGGING. (I think the
improved build times warrant only finding out later if we break a log line and anyway many things now just
print automatically, so this should be harder to do.) I also add CMemoryFwd.h to avoid including CMemory.h
too widely. This includes a lot of STL headers. Finally, I migrated CLoggerThrottler to a pimpl and moved
some obvious other details out of headers. The upshot for for my dev setup is 15% speed up to build everything.

---
## [peterooch/reactos](https://github.com/peterooch/reactos)@[4471ee4dfa...](https://github.com/peterooch/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Thursday 2022-07-21 15:53:50 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [lucaskroni/Frontend](https://github.com/lucaskroni/Frontend)@[b6863406ed...](https://github.com/lucaskroni/Frontend/commit/b6863406ed4652673bca7e177abef338012f3de9)
#### Thursday 2022-07-21 16:12:26 by lkronlac

Ok my brother you may be havin some big big trouble today but its cool keep your head up and handle it you got this no matter how long no matter how far leeettss gooooo ok yeah have a nice day though

Tasks:
-Look into starting the TemplateCreator jar in here
-and yeah thats it do that and then look what you should do next

---
## [Himemoria/android_kernel_xiaomi_mt6768](https://github.com/Himemoria/android_kernel_xiaomi_mt6768)@[a9fb371623...](https://github.com/Himemoria/android_kernel_xiaomi_mt6768/commit/a9fb371623bcee23712765a6cf9bb40e8464599f)
#### Thursday 2022-07-21 16:42:02 by Peter Zijlstra

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
Signed-off-by: Himemorii <himemori@mail.com>

---
## [ItsSelis/space-station-14](https://github.com/ItsSelis/space-station-14)@[949fbd0194...](https://github.com/ItsSelis/space-station-14/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Thursday 2022-07-21 16:50:57 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [ChameleonCloud/kolla-ansible](https://github.com/ChameleonCloud/kolla-ansible)@[2e5e1b5545...](https://github.com/ChameleonCloud/kolla-ansible/commit/2e5e1b5545a396b216ab5de3441a964b841c8a17)
#### Thursday 2022-07-21 18:14:02 by Radosław Piliszek

[CI] Nullify attempts

Per Clark Boylan's feedback [1], retries cause a retry not only
for pre playbook failures but also for cases where Ansible detects
network connectivity issues and they are caused by disks getting
filled to their fullest. This is an issue we experience that
sometimes results in a POST_FAILURE but certain FAILUREs are
retried which wastes CI resources.
The problematic jobs are ceph jobs. They are to be looked into.
Backport to all branches.
We can adjust retries for the core jobs that do not exhibit the
nasty behaviour but first we can try running without retries
to measure the troublesomeness.

[1] https://review.opendev.org/c/openstack/kolla-ansible/+/843536

Change-Id: I32fc296083b4881e8f457f4235a32f94ed819d9f
(cherry picked from commit 153956e458157e44d73efc3dd369699ff20e4d12)

---
## [niftynei/lightning](https://github.com/niftynei/lightning)@[a9eb87db17...](https://github.com/niftynei/lightning/commit/a9eb87db177aab355991f5cb354f264f6eefae03)
#### Thursday 2022-07-21 18:43:46 by niftynei

bkpr: add journal entry for offset account balances; report listbalances

When the node starts up, it records missing/updated account balances
to the 'channel' events... which is kinda fucked for wallet + external
events now that i think about it but these are all treated the same
anyway so it's fine.

This is the magic piece that lets your bookkeeping data startup ok on an
already running/established node.

---
## [Zytolg/StarbloomSS13](https://github.com/Zytolg/StarbloomSS13)@[635f518d04...](https://github.com/Zytolg/StarbloomSS13/commit/635f518d04a30c4c9f977c0570d480f8d44e56d1)
#### Thursday 2022-07-21 18:52:20 by notfrying1pans

web edit fuck yoooou

i swear to fucking god if this resets line endings or some shit im gonna scream

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[6fe0683a7b...](https://github.com/Wallemations/heavenstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Thursday 2022-07-21 19:07:26 by Jolly

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
## [uber/cadence](https://github.com/uber/cadence)@[add4b390ad...](https://github.com/uber/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Thursday 2022-07-21 19:47:21 by Steven L

Standardizing cancellation behavior: a canceled workflow never starts a new run (#4898)

# Summary for busy people

Workflow cancellation was kinda weird and confusing, and left some awful, unrecoverable, and un-*preventable* edge cases (particularly with child workflows).  It also left users with no way to reliably stop work, aside from termination.  Termination is inherently "unclean" and risky, so it should not be required to achieve something outside exceptional circumstances where recovery is not possible.

This commit changes that: cancellation is now "sticky", and a canceled workflow does not ever trigger a new run after it completes, regardless of how it completes, so it can be used as a reliable "stop processing after cleanup" tool.  The final state of a canceled workflow's run is now *always* a successful completion with a value, canceled, or timed out. (termination remains always "terminated")  
A canceled workflow can still start and abandon child workflows, so all current behavior with retries / continue as new / etc can be replicated with child workflows if desired.

A fair bit of (not very complex) additional work here and in nearly all other repos is required to truly complete this, but it is *functional* and non-optional with this commit alone.  
In particular, adding a dynamic config to (temporarily!) restore old behavior should be fairly easy if it proves to be needed.

# More details and motivation

Part 1 of [many, tbd, in multiple repos] involved in changing workflow cancellation to reliably end workflows.
Tests will be coming soon, for now I'm using a fairly simple set of workflows and checking the resulting histories exhaustively by hand.

The primary motivation for these changes is to address some impossible-to-recover-from scenarios when canceling child workflows.  After further exploration and discussion we've realized that, without these changes, there is *no reliable way* to stop a sequence of workflows without relying on termination, which we consistently treat as a fallback / impure-but-necessary ultimate hammer.

Workflows should not *need* to rely on termination to achieve a desired behavior.  With these changes, cancellation becomes capable of *guaranteeing* that workflows end within some finite time, which is a unique ability and makes it much more consistent and reliable.  
Turning this into a "complete" change will require quite a few tests, documentation changes, client-side changes (to allow recording more info, and likely changing test suites), and some smallish database and maybe RPC changes (to hold/return more data in cancellation errors).

We are also not currently planning on making this configurable.  It's seen as a correction of an under-specified and somewhat flawed chunk of behavior, more than "a change".  
Existing workflows will not experience replay errors, but it is still a substantial *semantic* change, though from what we have seen cancellation is relatively rarely used (partly due to its complex behavior).  If issues are encountered / if users end up needing it, it should be fairly easy to add a per-domain/tasklist/workflow type configuration value, but it will be opt-*out*, not opt-*in*.

# What was happening

Previously, workflow behavior on cancellation was pretty frequently surprising to our users, arguably inconsistent, and not very well documented:

| **PREVIOUS**  | **simple**               | **retry**                                 | **cron**                                | **retry+cron**                                    |
|--------------:|--------------------------|-------------------------------------------|-----------------------------------------|---------------------------------------------------|
| **success**   | success                  | success                                   | success<br>continue cron<br>cron        | success<br>continue cron<br>cron<br>retry         |
| **cancel**    | canceled                 | canceled                                  | canceled                                | canceled                                          |
| **retryable** | (n/a, fatal)             | continue retry<br>retry<br>recorded error | (n/a, fatal)                            | continue retry<br>cron<br>retry<br>recorded error |
| **fatal**     | failed<br>recorded error | failed<br>recorded error                  | continue cron<br>cron<br>recorded error | continue cron<br>cron<br>retry<br>recorded error  |
| **continue**  | continue immediately     | continue immediately<br>retry             | continue immediately                    | continue immediately<br>retry                     |
| **timeout**   | timeout                  | continue retry<br>retry<br>recorded error | continue cron<br>cron<br>recorded error | continue retry<br>cron<br>retry<br>recorded error |

A legend is:
- success / etc shows the final state of the canceled run (success = completed with a value that can be retrieved)
- "continue X" covers what source is used to compute the next run's starting delay (cron, retry, or no delay)
- "cron" / "retry" shows whether or not cron/retry configuration is carried over to the new run
  - note that cron is lost by default with continue-as-new
- and "recorded error" is whether or not the returned error is saved in its entirety (type + reason + details)

This largely summarizes as "cancellation works when you end with the canceled-context error", say from `ctx.Err()`, otherwise it behaves like normal (or nearly) and many scenarios will start a new run.
That's somewhat reasonable, but it's fairly "fragile" (it depends on what you return, and there are *many* ways for code to return some other error), and most importantly it means *there is no reliable way to stop a workflow* except to terminate it.

That has severe consequences in at least two scenarios:
1. When termination is *unsafe*
2. When a parent workflow cancels a child by canceling its context

For 1, for manual cancellations it's potentially reasonable to just terminate a run that begins after a successful cancel... but in principle if you're using cancellation it implies that termination is *not* desired, and potentially not safe to do.  Canceling may result in a brand new run that immediately starts new behavior, leaving you with no safe window to terminate and not leave bad state lingering.  
So users wanting a safe way to stop a sequence of workflows have no reliable way to do so.

For 2, it puts parent+child workflows in an extremely awkward, and essentially unrecoverable scenario.  Cancellation is a *one time event*, and as far as the parent is concerned, if the child/its context is canceled, the child is canceled...  
...but if the child then starts a new run for *any* reason (retry, cron, reset, etc), that new run is no longer canceled.  The parent has no way to know this has happened, and has no way to *re*-cancel the new child, so it can easily lead to the collection of workflows getting into an impossible state that it never recovers from.

Both cases are able to lead to unreliable behavior which can only use termination to stop, and for which no "safe" option exists.

After reviewing some customer issues and desires and thinking about things, we've settled on "cancel should guarantee that things stop".  Not necessarily in a timely manner, but that's fine.  And if a workflow wants to run behavior longer or larger than its current run can achieve, it has a workaround: start a new (likely child) workflow to do the cleanup.

# What happens now

So that's what this PR does, in a minimal / to-be-polished way so we can start running it for our stuck users while we flesh out tests and change other behaviors.

Currently that means our cancellation behavior is now:

| **CURRENT**    | **simple**                                | **retry**                                 | **cron**                                  | **retry+cron**                            |
|--------------:|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **success**   | success                                   | success                                   | success                                   | success                                   |
| **cancel**    | canceled                                  | canceled                                  | canceled                                  | canceled                                  |
| **retryable** | (n/a, fatal)                              | canceled<br>recorded error (details only) | (n/a, fatal)                              | canceled<br>recorded error (details only) |
| **fatal**     | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) |
| **continue**  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  |
| **timeout**   | timeout                                   | timeout                                   | timeout                                   | timeout                                   |

And the new "details" entries cover whether or not an error's "details" (the custom encoded data, not reason or type) are saved.  Unfortunately the current cancellation event (and clients' API) does not allow recording all data, or any in some cases, so the original reason/message and error type are lost and are replaced with a canceled error.

Now, cancellation *always* ends workflows with the current run.  Returning a value will return that value, including in cron scenarios, timeouts are still timeouts (and they imply a possibly un-clean termination), and _all_ errors or attempts to continue-as-new will instead result in a canceled state.

# Future changes to make to finish this effort

With further changes to the clients and RPC/storage models, canceled errors will store more details about what was returned.  E.g. continue-as-new does not record what was *attempted* to be started, and other error types lose their "reason" (i.e. the message) and type but not details.  Pretty clearly this is sub-par, and we should be capable of reporting the actual return in full so it can be retrieved if needed.  This is also why returning a value now always ends in a completed state, so successful completions do not lose those values.

Prior to merging into master / a release, we may end up making this configurable (likely with a default of opt-out), to address both the sub-par information recording and the semantically-breaking behavior change.  Docs changes are also due, as well as some integration tests, client library changes (e.g. to make sure the test suite reflects the new behavior), etc.

Another gap to plug is that resetting a workflow does not "forward" the canceled state to the new run.  We should probably be treating cancellation like we do signals: cancel the new run if the current run is canceled.  This will ensure that you can reset a child and retain the parent's cancellation, so it'll very likely become the default behavior, but we'll allow overriding it.  Resets are manual actions, they can break the rules if desired.  And they can just manually cancel later if they decide they do want it.

And last and perhaps least: it's quite strange that continue-as-new does not retain cron config.  At least from the Go client.  I suspect it's just not adding to / pulling from the context correctly.

---
## [LunarWatcher/upm](https://github.com/LunarWatcher/upm)@[7843701f4c...](https://github.com/LunarWatcher/upm/commit/7843701f4ccc323b29323690dcb5240ef66c7689)
#### Thursday 2022-07-21 20:03:07 by None

Stage one pi compatibility

Worked out installation, and I should in theory have that up and
running. Fucked up on which arm version was selected for node, but
that's a quickfix.

Haven't tested activation because I'm dumb, forgot which version I just
installed, and the lack of @latest symlinks/tracking is starting to
annoy me.

Should also start tracking which versions are actually installed. Not
sure if that's better suited for metadata, or if that's something
I'll just compute at runtime. Not particularly performant, especially if
the underlying file system is shit, but that's a problem for me to
figure out when I start diving into this rabbit hole.

---
## [Fullgayshack/FALL-GUYS-FREE-HACK](https://github.com/Fullgayshack/FALL-GUYS-FREE-HACK)@[10bcc0e64d...](https://github.com/Fullgayshack/FALL-GUYS-FREE-HACK/commit/10bcc0e64dddf0c4dec656e6150d013c45d4aafb)
#### Thursday 2022-07-21 20:09:54 by Fullgayshack

Add files via upload

https://youtu.be/Qs8VAf5ZlqE

fall guys hacks download, fall guys hacks, fall guys hack, fall guys hacks pc, fall guys hack download, fall guys cheat, fall guys hacker, fall guys hacks 2022, fall guys hack 2022, how to hack fall guys pc, fall guys speedhack, fall guys flyhack, fall guys esp, fall guys cheats, fall guys cheat 2022, fall guys fly hack, fall guys speed hack, fall guys, how to hack fall guys, fall guys hack cheat engine, fall guys wallhack, fall guys free hack, fall guys free cheat, fall guys cheat download, fall guys modmenu 2022, fall guys mod menu, fallguys mod menu, fallguys cheat, fall guys hacking, how to hack fall guys 2022, fall guys hacker meme, fall guys hacker loses, fall guys hacker gameplay, hanwe fall guys hacks, willyrex fall guys hacks, linktijger fall guys hacks, hack fall guys, fall guys life hacks, fallguys hack, fall guys cheats 2022, fall guys hack pc, fallguys troll, fallguys funny moments, fall guys hack apk android, fall guys hack tutorial, fall guys hack meme, fall guys hack gameplay, fall guys hack free, how to hack fall guys ps4, fall guys hacking live, fallguys, fall guys cheater, hack no fall guys, hack fall guys 2022, spooky fall guys hack, cheat fall guys, hacks fall guys, fall guys hacker compilation, how to cheat in fall guys, fall guys mobile, fall guys hacks ps4, how to get hacks in fall guys, fall guys modmenu, fall guys cheat undetected, fall guys hack dll, fall guys hack download pc, fall guys hack download tutorial, fall guys hack comp, fall guys life hacksusing hacks to win in fallguys, fall guys hack dll download, fall guys hack client free, all guys hack, danny aarons, danny aarons gk team, fallguys modmenu, danny aarons champs challenge, danny aarons draft challenge, aarons, danny aarons rating teams, ttd danny aarons, more sypherpk, gameplay, stream highlights, highlights, gaming, competitive, fall guy, how to play, sypherpk, new update, streamers react, sypher, how to win fall guys, fall guys tips, sypher plays,

---
## [Florin9doi/pcsx2](https://github.com/Florin9doi/pcsx2)@[d6684efd26...](https://github.com/Florin9doi/pcsx2/commit/d6684efd262ef1c83d37c50b48edc478952dddf9)
#### Thursday 2022-07-21 20:17:16 by RedDevilus

GameDB: GS HW Batch X

Relevant:
Bully
Colosseum - Road to Freedom
Dark Chronicle (Dark Cloud 2)
Killzone
God of War
Gun
Midnight Club 3
Mortal Kombat - Deadly Alliance
Need for Speed Carbon / Most Wanted / Undercover
Prince of Persia - Sand of Time / The Two Thrones / Warrior Within
Resident Evil 4 (BioHazard 4)
Thrillville / Off the Rails

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[4533f07b33...](https://github.com/san7890/bruhstation/commit/4533f07b33324f99cdb186808622314d18a72962)
#### Thursday 2022-07-21 21:12:09 by san7890

Adds Config Settings to Departmental Security Officers

Server Operators can either turn off getting "elevated access" (formerly scaled access) for Departmental Security Officers, using the scaled access system, or always giving them the maximal access.

i'm also adding myself to admins.txt now because it's annoying to deal with now that debug shit is broken

whoops i fucked that up

---
## [p2sr/SourceAutoRecord](https://github.com/p2sr/SourceAutoRecord)@[a4a08c7637...](https://github.com/p2sr/SourceAutoRecord/commit/a4a08c76372045a21afc7aaee90db5dc1c3681f4)
#### Thursday 2022-07-21 21:48:23 by mlugg

:musical_note: fuck you very very much :musical_note:

cause we hate what you do
and we hate your whole crew
so please don't stay in touch

---
## [luthermonson/cluster-api-provider-aws](https://github.com/luthermonson/cluster-api-provider-aws)@[867afc7ac7...](https://github.com/luthermonson/cluster-api-provider-aws/commit/867afc7ac718621a11e00fc2b05589ac2548d4d5)
#### Thursday 2022-07-21 22:08:15 by Claudia Beresford

Fail apidiff make target when git fails

This is a fairly simple fix to ensure that when `git diff` fails on the
`make apidiff` target, the exit code is actually picked up by make.
Previously the exit code from `diff` was "swallowed" by the `if`.

eg:
```
$ cat Makefile
thing:
        if (exit 1); then \
		echo foo; \
        fi
        echo "still here"

$ make thing
still here
$ echo $?
0
```

What we want:
- exit 1 when `git diff` fails
- exit 0 when `grep` fails
- call `go-apidiff` when `git diff` and `grep` succeeds
- exit 1 when `go-apidiff` fails

This is honestly a complete pain to do in a Makefile.

I tried capturing output, moving everything to a script, calling from
one thing to another. But really this is just tricky to do the way we
want in Make.

So, if we can live with a little repetition, we can do the following:
- Check the `git diff` can run, exit 1 if not
- Run the `git diff` again, this time piping the successful command to
  `grep`
- If `grep` fails, then no worries, the target will roll on and exit 0
  like it always has.
- If `grep` succeeds then the `go-apidiff` tool is called and the target
  runs as intended.

------

In the case of `$(APIDIFF_OLD_COMMIT)`, there is some annoying `make`
magic going on here. Which I can't simply make fail since it will cause any
job which uses something in this Makefile to fail out of proximity.
The `shell` is expanded when the file is loaded meaning even targets
which do not care about the value will end up erroring (but not exiting)
when it fails. These are not errors which impact the target's run, but
they look annoying in CI.

Since this var is only used by `apidiff`, we can move it into that
target so it is only evaluated when specifically called.

---
## [syntropy-hullett/bucket-webring](https://github.com/syntropy-hullett/bucket-webring)@[81fa1234d9...](https://github.com/syntropy-hullett/bucket-webring/commit/81fa1234d9f99531f8d98d699249e4c00c4e819f)
#### Thursday 2022-07-21 22:44:52 by rowan tobias

swiftyshq format fix

i was having errors fsr so i thought removing punctuation etc would fix it. We'll See! (sorry if you got notifs for my other prs that i deleted i was struggling.)

---
## [RaveRadbury/tgstation](https://github.com/RaveRadbury/tgstation)@[95ffcd4e19...](https://github.com/RaveRadbury/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Thursday 2022-07-21 22:58:15 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [tdyas/pants](https://github.com/tdyas/pants)@[8742dfae4d...](https://github.com/tdyas/pants/commit/8742dfae4d104e80ce7f1003bd1b1fbe518eb0c2)
#### Thursday 2022-07-21 23:15:05 by Eric Arellano

Add `[python-setup].experimental_lockfile` to consume lockfiles (#12316)

This allows you to use the new lockfile format, generated by pip-tools via `./pants --tag=-lockfile_ignore lock ::` and https://github.com/pantsbuild/pants/pull/12300. 

A lockfile cannot be used at the same time as a constraints file. This makes the code easier to implement and means that we don't break any prior APIs. We will likely deprecate constraints when the dust settles.

There are several major deficiencies:

- Only `pex_from_targets.py` consumes this lockfile. This means that tool lockfiles will now have no constraints and no lockfile, for now.
- Does not handle requirements disjoint to the lockfile.
- Does not support multiple user lockfiles, which, for example, is necessary to properly handle `platforms` with `pex_binary` and `python_awslambda`: we need one lockfile per platform, as demonstrated in https://github.com/Eric-Arellano/lockfile-platforms-problem/tree/main/multiple_pex__stu_proposal.


### Lockfile vs. constraints file (and `[python-setup].resolve_all_constraints`)

We're currently using pip's `--constraints` file support, which allows you to specify constraints that may not actually be used. At the same time, we default to `[python-setup].resolve_all_constraints`, which _does_ first install the entire constraints file, and then uses Pex's repository PEX feature to extract the relevant subset. This is generally a performance optimization, but there are some times `--resolve-all-constraints` is not desirable:

1. It is not safe to first install the superset, and you can only install the proper subset. This especially can happen when `platforms` are used. See https://github.com/pantsbuild/pants/issues/12222.
     - We proactively disable `--resolve-all-constraints` when `platforms` are used.
2. User does not like the performance tradeoff, e.g. because they have a huge repository PEX so it's slow to access.

--

In contrast, this PR stops using `--constraints` and roughly always does `[python-setup].resolve_all_constraints` (we now run `pex -r requirements.txt --no-transitive` and use repository PEXes). Multiple user lockfiles will allow us to solve the above issues:

> 1. It is not safe to first install the superset, and you can only install the proper subset.

We'll have a distinct lockfile for each `platform`, which avoids this situation. See https://github.com/Eric-Arellano/lockfile-platforms-problem/tree/main/multiple_pex__stu_proposal for an example.

> 2. User does not like the performance tradeoff

They can use multiple lockfiles to work around this.

--

Always using `[python-setup].resolve_all_constraints` reduces complexity: less code to support, fewer concepts for users to learn.

Likewise, if we did still want to use `--constraints`, we would also need to upgrade Pex to use Pip 21+, which gained support for URL constraints. We [hacked around URL constraints before](https://github.com/pantsbuild/pants/pull/11907), but that isn't robust. However, Pip 21+ drops Python 2 and 3.5 support: we'd need to release Pex 3 w/o Py2 support, and upgrade Pants to have workarounds that allow Py2 to still be used. To avoid project creep, it's better to punt on Pex 3.

[ci skip-rust]
[ci skip-build-wheels]

---
## [TDKorn/insta-tweet](https://github.com/TDKorn/insta-tweet)@[02f468a0fe...](https://github.com/TDKorn/insta-tweet/commit/02f468a0fe5fe7d68ba6106fd0b2511fac203bb4)
#### Thursday 2022-07-21 23:41:54 by TDKorn

IT WORKED!!! Now to fix everything else

* I swear there's gotta be some sort of frustration threshold you need to cross before this 💩 is allowed to work
    - Like I JUST did this for my other repo you'd think it'd be simple?? Yet here we are

---
* Get rid of the extra stuff in the yaml file and also the extra requirements folder lol idk I thought it'd help

* Update db.rst and db.py WOW was that frustrating
    - v little info on documenting class variables
        > Actually literally found 0 information on getting type hints to work, I got here through trial and error 🐵🧠
    - I can definitely clean it up a lil but for now,  it works and I did try but got frustrated with ```Base.__init__()``` being documented even when I set it as excluded,, like shut up pls

---

