## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-30](docs/good-messages/2023/2023-08-30.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,280,588 were push events containing 3,447,931 commit messages that amount to 258,178,160 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [Prequal-Digital/git](https://github.com/Prequal-Digital/git)@[8f23432b38...](https://github.com/Prequal-Digital/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Wednesday 2023-08-30 00:23:14 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [langchain-ai/langchain](https://github.com/langchain-ai/langchain)@[d57d08fd01...](https://github.com/langchain-ai/langchain/commit/d57d08fd01e05889af4e59fa3577c824de6df09d)
#### Wednesday 2023-08-30 00:23:31 by nikhilkjha

Initial commit for comprehend moderator (#9665)

This PR implements a custom chain that wraps Amazon Comprehend API
calls. The custom chain is aimed to be used with LLM chains to provide
moderation capability that let’s you detect and redact PII, Toxic and
Intent content in the LLM prompt, or the LLM response. The
implementation accepts a configuration object to control what checks
will be performed on a LLM prompt and can be used in a variety of setups
using the LangChain expression language to not only detect the
configured info in chains, but also other constructs such as a
retriever.
The included sample notebook goes over the different configuration
options and how to use it with other chains.

###  Usage sample
```python
from langchain_experimental.comprehend_moderation import BaseModerationActions, BaseModerationFilters

moderation_config = { 
        "filters":[ 
                BaseModerationFilters.PII, 
                BaseModerationFilters.TOXICITY,
                BaseModerationFilters.INTENT
        ],
        "pii":{ 
                "action": BaseModerationActions.ALLOW, 
                "threshold":0.5, 
                "labels":["SSN"],
                "mask_character": "X"
        },
        "toxicity":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        },
        "intent":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        }
}

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})

print(response['output'])


```
### Output
```
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii validation...
Found PII content..stopping..
The prompt contains PII entities and cannot be processed
```

---------

Co-authored-by: Piyush Jain <piyushjain@duck.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Bagatur <baskaryan@gmail.com>

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[d1afd66508...](https://github.com/Ical92/tgstation/commit/d1afd66508ed3474ca6179d54294742bef531419)
#### Wednesday 2023-08-30 00:28:05 by san7890

The Curse Of The Slot Machine - Now Clone-less (#77841)

## About The Pull Request

Hey there,

I think it's commonly held that clone damage sucks and is overused. One
of the last places where it was in slot machine code as a type of
"immutable" damage that would cause you to die if you didn't leave and
get medical attention. It had a lot of silliness and I'm not sure if a
lot of it was meant to work the way it was, but here we are.

So, what's the changes?

* The Cursed Slot Machine will give you a status effect that will
"curse" you with repeated damage. After five curses, you get gibbed
(similar to the old behavior of the machine). Each curse has it's own
change to the status effect, with a lot of depth included. Let me know
if the fluff messages about the status effect change sucks, I think it's
neat though.
* A person with the curse will smoke. I wanted this to look a bit more
"steamy" or grey, but I think it's a decent way of communicating that
shit is fucked up with that dude.
* You also get a branded wound after your first failure at the slot
machine. Ouchers. Should get it looked at by a doctor.
* We also throw a nice screen alert and all of that jazz.
* I also cleaned up all of the code relating to the slot machine
(including a stupid double and), and did some tinkering with the status
effects framework to get the desired effect I wanted. I hope you enjoy
it as much as I did making it. We use cooldowns and stuff between slot
machine pulls.
* If _anyone_ wins on the slot machine, all curses/brands are lifted.
Lucky jackpot!
* A lot of the stuff in this code has a lot of vars that might not be
modified codewise in case admins still want to jank with this for
events.
## Why It's Good For The Game

Clone damage stinks, and I don't really like it as a way to subvert the
whole "oh you can't use legion cores to get your way". It's a cursed
slot machine, and it should do long term damage so that even if you
expend all of the resources on the station, it might all be for naught.
It's a horrible price to pay in your search for that d20. I think the
negative side effects are pretty OK as far as balance, earlier
iterations of this concept had you die _way_ too fast.

All in all, it's just way more of an interesting interaction than "you
take damage and then go to medbay and then come back in the hopes of
gambling a d20".
## Changelog
:cl:
add: The Lavaland Cursed Slot Machine of Greed suddenly seems a lot more
sinister...
refactor: Instead of taking clone damage from the cursed slot machine,
you now get a status effect with a number of curses associated with it.
There's some interesting florid language associated with the status
effect as a nicety until your eventual gibbing from chasing that prize.
/:cl:

I remain undecided if I should keep the curse limit uncapped (but have
the damages increase rapidly after the 5-curse threshold), so I left it
as the `gib()` from the old code. Let me know your thoughts, but I
really don't like the thought that getting the fabled d20 is easy.

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[f0dc574c37...](https://github.com/Jolly-66/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Wednesday 2023-08-30 00:39:37 by carlarctg

Added Omen Spontaneous Combustion and light tube and mirror effects (#77175)

## About The Pull Request

Cursed crewmembers can randomly, extremely rarely, spontaneously combust
for no reason.

Cursed crewmembers can get zapped by nearby light tubes.

Cursed crewmembers can freak out when passing by mirrors.

To make up for these, triggering a cursed effect is slightly less than
half as likely now when walking around now.

## Why It's Good For The Game

Cursed is fun as hell, but after a certain point it gets kind of
monotonous - it's airlocks, vending machines, and the rest is too rare
to count. We need more ways to comically get hurt in the game.

You might dislike the 'reduced effects' bit but trust me it is
incredibly frickin' common to have shit happen to you. Add to the
occasional vending machine and airlock crushes the near-constant light
tubes all over the station? Yeah, that needs a toning down else it will
be just a tad too miserable to be funny. Also cause the poor janitor
unneeded stress.

## Changelog

:cl:
add: Cursed crewmembers can randomly, extremely rarely, spontaneously
combust for no reason.
add: Cursed crewmembers can get zapped by nearby light tubes.
add: Cursed crewmembers can freak out when passing by mirrors.
add: To make up for these, triggering a cursed effect is slightly less
than half as likely now when walking around now.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[f3072d7377...](https://github.com/nikothedude/Skyrat-tg/commit/f3072d7377bda026c1d6ae709d1311609226f115)
#### Wednesday 2023-08-30 01:36:31 by SkyratBot

[MIRROR] Adds a unique medibot to the Syndicate Infiltrator [MDB IGNORE] (#23084)

* Adds a unique medibot to the Syndicate Infiltrator (#77582)

## About The Pull Request

Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)

Fixed an issue that made mapload medibots unable to load custom skins.

This PR adds a medibot subtype to the simple animal freeze list, which I
don't think is a big deal as this isn't a 'true' simplemob but just a
slightly altered medibot, similarly to my 'lesser Gorillas' in the
summon simians PR.

## Why It's Good For The Game

> Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though.

I know what the inmediate reaction is here - but hear me out. Besides
the meme of the month, it really, genuinely is cute and amusing to have
a friendly medibot that shows dismay when you're arming the nuke and
horror when it blows up (with you, hopefully, at the syndibase), and
still fits quite well within SS13's charm and flavor. The reference
isn't overt and in-your-face.

Besides that, slip-ups, friendly fire, and accidents are semi-common on
the shuttle and, just like Wizards, nukies deserve a bot to patch their
wounds up.

> (It's also in the Interdyne Pharmaceuticals ship, renamed)

I think it makes sense for the pharmacists to have an evil medibot!

> Fixed an issue that made mapload medibots unable to load custom skins.

Fixed "bezerk" skin not appearing. Didn't fix it being ugly as sin
though.

## Changelog

:cl:
add: Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)
fix: Fixed an issue that made mapload medibots unable to load custom
skins.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Adds a unique medibot to the Syndicate Infiltrator

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

---
## [zai-tm/XaiSharp](https://github.com/zai-tm/XaiSharp)@[40234dd252...](https://github.com/zai-tm/XaiSharp/commit/40234dd252a908c931ebec3659274e3e724ed4c6)
#### Wednesday 2023-08-30 01:44:05 by Zai

dfsfsdfsdsdffsdgfdssdfg I HATE MY LIFEeasdffdfdsfsd

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[c968edab30...](https://github.com/Paxilmaniac/tgstation/commit/c968edab306659606da4f39bc178851a5a24405c)
#### Wednesday 2023-08-30 01:52:40 by carlarctg

Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome (#77277)

## About The Pull Request

Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror or the cursed springs
are the most accessible sources)

Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the shuttle has just less than half of its usual refueling
time left. However, it gives the cargo budget an influx of 3000 credits!

Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

## Why It's Good For The Game

First off, here is my reasoning for why these need altering at all.

Players will always naturally gravitate to the wackiest and
most-out-there options, in this case this applies to shuttles. It's why
the Monastery or the Asteroid or Daniel are reasonably common sights,
more common than some of the 'boring' shuttle options that don't need
unlock with an emag.

The problem here, as I see it, is that there is no incentive
what-so-ever to NOT purchase these 'wacky' shuttles. Some of the
shuttles in the code are just way too stupid to be seen on most or even
some rounds (Arena, Disco Inferno?), so they require rare unlocks to
occur. Wacky shuttles being spammed round after round are bad due to
several reasons:
1. Players will run every joke to the ground. Wacky conditionless
shuttles take up a large amount of space in the shuttle memeplex, so
they are disproportionately seen in comparison to any of the
less-extravagant but more grounded and actually interesting options.
(Medisim? Monkeys anyone?). This ends up making the wacky shuttles
actually *less* wacky and just the stale and boring options.
2. Wacky shuttles affect the end-round quite a lot. This is fine, of
course, but not when these wacky shuttles can be seen every round.
3. These wacky shuttles don't have proper facilities. None of them have
a good medical section, or emergency supplies, or enough room. This gets
pretty annoying pretty fast.
4. One Funny Guy (the quintessential example being the clown with a dead
captain's ID) is all but guaranteed to try to buy the funniest and most
annoying shuttle to piss off the rest of the crew. With how Funny and
Annoying these shuttles are, not to mention how dirt-cheap they are (or
literally give you money!), they're easily the most seen alternate
shuttles, which isn't good when they alter how the round-end plays so
heavily.

> Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror is the most accessible
source)

The Wabbajack has a endless source of voluntary Polymorphs with a
comically low price, which means it is purchased endlessly by crew, not
to mention being literally a source of free syndiborgs and xenos. While
I'm not a balanceposter, this does come with some annoyances especially
for antagonists who just randomly get blown up by an assault borg. This
is fine and fun every so often, but not as a common occurrence, not as a
guaranteed every-round option. I think it's an excellent candidate for
an unlock condition.

> Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the emergency shuttle is more than halfway refueled.
However, it gives the cargo budget an influx of 3000 credits!

This is LITERALLY 'haha grief shuttle', I have no idea how it even got
in as a condition-less shuttle. You see the captain buy it For No Raisin
Lul 2 minutes in, sigh to yourself, and secure an EVA suit when the
shuttle lands to try to survive in the unbelievably cramped space.
(Someone always blows it up.)

Instead of being JUST Grief Shuttle, now it has some interesting reasons
to exist. Revs and you're dirt-poor? Nukies just declared war after the
Clown bought ten crates of creampie dufflebags? Buy this shuttle and get
an influx of money.

> Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

This one isn't as egregious as the above, but I believe my personal
dislike of it extends to a game design level, to an extent. One person
can buy this shuttle and the crew as a whole are left to groan as they
prepare for a noisy, confusing shuttle in which everyone is ten tiles
shifted to their left as their sprite does the most ridiculous dance
seen in SS13 history. 'Just turn the music off!': I'm glad this is an
option, but it doesn't change how much this shuttle alters things. It's
fine as a sendoff to a nice, chill greenshift, but as a constant sight
in red shifts it's just... frustrating. And purchased BECAUSE it's
frustrating, to the short-lived schadenfreude of one person and the
frustration of others.

And then the unbreakable disco machine. Why is it unbreakable. If the
crew doesn't want to listen to the thing, let them break it? Buy Disco
Inferno if you want an unbreakable disco.

Some of these changes are probably over-the-top, but remember that these
will still be seen in-game, just a bit rarer. Worst case scenario the
shuttle replacement event will let them have their time in the
limelight.

## Changelog

:cl:
balance: Lepton Violet (wabbajack) shuttle must be unlocked by having
some form of polymorph happen in-game first (Pride Mirror or the cursed
springs are the most accessible sources)
balance: Scrapheap shuttle can only be bought if the Cargo budget is
below 600 credits, and the shuttle has just less than half of its usual
refueling time left. However, it gives the cargo budget an influx of
3000 credits!
qol: Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.
/:cl:

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[1c852d2863...](https://github.com/Paxilmaniac/tgstation/commit/1c852d2863622bb24acf7511d7a9bb06813619fc)
#### Wednesday 2023-08-30 01:52:40 by EOBGames

Martian Food: A Taste of the Red Planet (#75988)

## About The Pull Request
Adds a selection of new foods and drinks based around Mars.
More information on Mars can be found here:
https://github.com/tgstation/common_core/blob/master/Interesting%20Planets/Human%20Space/The%20Sol%20System.md
To summarise for the general audience, Mars is a vital colony of the
Terran Federation, having been primarily settled (at least originally)
by Cybersun Industries to harvest its lucrative supplies of plasma, the
second largest in human space behind Lavaland. This has given Mars a
diverse culture evolving from the mostly East Asian colonists, and their
food reflects this.

Thanks to Melbert for their work on the soup portion of this PR.

The food:
Martian cuisine draws upon the culinary traditions of East Asia, and
adds in fusion cuisine from the later colonists. Expect classics such as
ramen, curry, noodles and donburi, as well as new takes on the formula
like the Croque-Martienne, Peanut Butter Ice Cream Mochi, and the
Kitzushi- chilli cheese and rice inside a fried tofu casing. Oh, and
lots of pineapple. The Martians love pineapple:

![image](https://github.com/tgstation/tgstation/assets/58124831/c9ae33a1-e03a-4f94-8ce0-8ad124e88e8d)
Also included are some foods for Ethereals, which may or may not be
hinting at something I've got planned...

The drinks:
Four new base drinks make their way to the game, bringing with them a
host of new cocktails: enjoy new ventures in bartending with Coconut
Rum, Shochu/Soju, Yuyake (our favourite legally-distinct melon liqueur),
and Mars' favourite alcoholic beverage, rice beer. Each is available in
the dispenser, as well as bottles in the booze-o-mat:

![image](https://github.com/tgstation/tgstation/assets/58124831/914a6e2a-7ef5-4791-ae31-d08fa9211083)

The recipes:
To make your (and the wiki editors) lives easier, please find below the
recipes for both foods and drinks:
Food: https://hackmd.io/@EOBGames/BkVFU0w9Y
Drinks: https://hackmd.io/@EOBGames/rJ1OhnsJ2
## Why It's Good For The Game
Another lot of variety for the chef and bartender, as well as continuing
the work started with lizard and moth food in getting Common Core into
the game in a tangible and fun way.
## Changelog
:cl: EOBGames, MrMelbert
add: Mars celebrates the 250th anniversary of the Martian Concession
this year, and this has brought Martian cuisine to new heights of
popularity. Find a new selection of Martian foods and drinks available
in your crafting menu today!
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Jackal-boop/tgstation](https://github.com/Jackal-boop/tgstation)@[74198373da...](https://github.com/Jackal-boop/tgstation/commit/74198373dada9f9d9e7c01e0337ba8ef04447583)
#### Wednesday 2023-08-30 02:09:13 by GuillaumePrata

Fixes vents having "infinite" pressure caps. (#77686)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Unary vents didn't have a pressure cap on either pressuring or siphoning
mode.
This allowed 2 unintended behaviours that are now fixed:

The first is that unary vents on pressuring mode would work as "better"
Injectors, there is some small pros and cons to each, but we shouldn't
have 2 atmos devices that achieve the same goal of "put as much pressure
as you have available gas" into a tile.

The second is that while on siphoning mode it could bypass the pressure
caps other atmos pressure/volume pumps have and "put as much pressure as
you have available gas" into pipelines, canisters, etc.

## Mid PR changes

As it was requested to add a new way to achieve infinite pressure,
volume pumps that are overclocked will not have a pressure cap anymore
in the most streamlined way for new and veteran players.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Atmos has a lot of cheese strats that we can use to achieve goals, it is
part of the charm in mastering the system for a lot of players and it
does add some interesting mentoring scenarios where an Elder Atmosian
teaches Eldritch pipe knowledge to new players.

But then it comes the problem that a lot of these are unintented and
thus are not taken in consideration when doing important balance
changes, contradict other "atmos logic", are secret club knowledge that
can only be passed from player to player, etc, etc.

The "put infinite pressure on a tile" change is not that important, as
that is the injectors' job already.

Now the "put infinite pressure on a pipeline" is something unique (As
far as I'm aware since I purposely avoid learning Eldritch atmos tricks)
and it is used to achieve a few goals like high temperature/pressure
burns.

This one is kinda sad to lose, but if we are going to have an atmos
machinery that allows us to "put infinite pressure on a pipeline" that
should be in the tin, new players should look into the device and know
what atmos goals they can achieve with it, future coders should take
that balance in consideration, etc, etc.

And as it was requested to keep the old trick in game, volume pumps do
not have a pressure cap anymore.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl: Guillaume Prata
fix: Unary vents have a pressure cap on both their pressuring and
siphoning mode now, preventing the bypass trick of putting "infinite"
pressure on tiles/pipelines.
balance: Overclocked Volume Pumps do not have a pressure cap anymore.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [LorenzoF765/GAT360Final](https://github.com/LorenzoF765/GAT360Final)@[216e1304b1...](https://github.com/LorenzoF765/GAT360Final/commit/216e1304b1761726a9efb38ee2005e2af9b61703)
#### Wednesday 2023-08-30 02:11:34 by Matthan Cantrell

Merge pull request #6 from LorenzoF765/main

fuck you john

---
## [Jaybirdnerd/Citadel-Station-13-RP](https://github.com/Jaybirdnerd/Citadel-Station-13-RP)@[7d600bf36a...](https://github.com/Jaybirdnerd/Citadel-Station-13-RP/commit/7d600bf36a691d4be27e852eed0106a1564d7aee)
#### Wednesday 2023-08-30 02:25:20 by TheObserver-sys

More plants, new chems, new carpet generation techniques, plantcell buff, and the drills now have a GPS signal! (#5912)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/4d3a51f1-7d2b-4d56-9971-7f33d76610f1)

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/608ba481-2499-4bf0-a25c-cc503655bf7d)

New! Exciting! Things! YEEHAW!

Okay, hype aside, this adds two plants from Main -- the third, and most
powerful sister of the ambrosia family, and the better grass, carpet!

Ambrosia Gaia: A difficult plant to keep alive, being very vulnerable to
weeds, pests, and any amount of toxins in the tray, as well as voracious
when it comes to nutrients and water. In exchange, the plant produces a
very, very powerful healing agent: Earthsblood.

For the cost of your brain, your ability to gauge how injured you are,
and when it works again, the ability to see clearly, your body will be
repaired in miraculous ways! (4/4 Brute Burn, 4 tox, 10 oxy, 2 clone).
The current damage is set to 1 brain damage, which means you'd need to
use a fair amount to die -- but not treating it will debilitate you.
Overdoses at over 15u.
In the future, it will also be a usable plant chem -- but let's not
worry about that until after I scream at the entirety of botany.

Carpet: Grass mutation, pull it free, get free carpet tile. OR! Mix with
the items in the image to create New! and Exciting! colors. Mix 2 parts
liquefied carpet, with 1 part plasticide, and you too can redecorate
like the best of them*

*some colors still have to be bought from cargo.
*someone help me make it a sprayable so we don't need solidification
please....

This also buffs a certain aspect of xenobotany -- plant cells.
For reasons only known to god.. and I think he left baycode a long time
ago, plant cells could only ever reach a maximum rating of 2000. As a
large cell. So you can't stuff it in a gun. This is dogshit --
especially for the challenge of reaching 200 potency on a plant, a feat
that is nearly impossible. The math has been buffed, so if you even
manage to get to 100, you at least have a Rating 20000 cell, something
you can run a department off of if straits are dire.

The final, and more QoL thing than straight buff or new thing: GPS
Drills
Drills now have a GPS signal. Never lose a pesky drill again!*
*you did remember your GPS device, yeah?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Give a xenobotanist something worth working to in normal gameplay, and
they'll endeavour to do so while waiting for the fun plants to come back
to station. Don't, and watch them just kinda wilt waist deep in glow
berries, gold apples, and ice chilis. Also, it's easier than you think
to lose a giant drill when you've stepped away from the planet for a
long while. only to come back later. Putting GPSes in them just means
you can continue the work again.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Two new plants, Ambrosia Gaia, and Carpet
add: New chems! Earthsblood, trading the mind for the body, and Carpet
and it's many mixtures, capable of being solidified later!
qol: Mining Drills now have an integral GPS. It took strength of a
million men to not make the tag DRILLD0 as a terrible joke.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: TheObserver-sys <Gizmomaster777@gmail.com>
Co-authored-by: Captain277 <agentraven16@gmail.com>

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[78289cc18a...](https://github.com/Superlagg/coyote-bayou/commit/78289cc18a77a43ebb92b21561afea7a7ae4bb3a)
#### Wednesday 2023-08-30 02:41:19 by Tk420634

Fixes scorb

idk why the shits even broken what in the god damn I hate this fucking code

---
## [Medizeal22/Liberty-Station-13](https://github.com/Medizeal22/Liberty-Station-13)@[14a2aff333...](https://github.com/Medizeal22/Liberty-Station-13/commit/14a2aff3335d2cc93ac8f0f4f7da9d6b3d48aaa4)
#### Wednesday 2023-08-30 02:56:47 by ThePainkiller

Erismed4 patches

- Lowers overdose of Party Drops and Menace
- improves upon certain wound fixing methods
- Surgical "tape" is gone, why would we need that when we always had bone gel for doing the exact same procedure a year ago
- Hyperzine renamed to Chronos. No longer a drug, considered a stim now, effects largely remain the same with no emote spam, but it will consume the user's sanity the more it's on them, causing halucinations and sanity loss. Overdose causes mental breakdown, hallucinations, jitteriness, nerve damage and fatal brain damage.
- Various stim recipes tweaked
- Medical stack items costs shuffled around
- Bone grafting to bone fixing
- Detox given Purger chem quality for treatment on toxin accumulation wounds
- Fixes overdose of Baton and Claw energy drinks to damage their respective organs instead of just the heart
- Combat chem injector has basic combat chems now instead of just hyperzine and free food/meds
- Organ fabricator no longer spills biomatter on the floor when deconstructed, handled as a proper lathe with no bullshit since Biomatter is no longer a "church" material

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[c6e0ba7516...](https://github.com/Bubberstation/Bubberstation/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Wednesday 2023-08-30 03:58:44 by SkyratBot

[MIRROR] Drill module automatically disables if it's about to drill into gibtonite [MDB IGNORE] (#22990)

* Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

* Drill module automatically disables if it's about to drill into gibtonite

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [rsalmaso/mame](https://github.com/rsalmaso/mame)@[dbb0909cba...](https://github.com/rsalmaso/mame/commit/dbb0909cbab3f2094088a42687894e0e6053986b)
#### Wednesday 2023-08-30 06:16:15 by wilbertpol

msx1_flop.xml: Added 105 working items, and replaced one item. (#11511)

* Replaced Konami Game Collection 3: Shooting Series (Japan) with a better dump. [file-hunter]

New working software list items (msx1_flop.xml)
-------------------------------
10 Programas Serie Oro (Spain) [file-hunter]
20 Programas Serie Oro (Spain) [file-hunter]
747 400b Flight Simulator (Europe, cracked) [file-hunter]
Alfabet en Deelsom (Netherlands) [file-hunter]
Alien Panic (Spain) [file-hunter]
Andon (Japan, hacked) [file-hunter]
Duad-MSX (Japan) [file-hunter]
Engels + Procenten (Netherlands) [file-hunter]
Fracta (Brazil) [file-hunter]
Graphos III (Brazil) [file-hunter]
Gruta de Maquine (Brazil)
The Iron Gauntz (Japan, prototype) [file-hunter]
Konami Game Collection 1: Action Series (Japan, alt) [file-hunter]
Konami Game Collection 4: Sports Series 2 (Japan, alt) [file-hunter]
Lettergrijper + Geld (Netherlands) [file-hunter]
Manuscript (United Kingdom) [file-hunter]
MSX Compilation 5 (Netherlands) [file-hunter]
MSX PageMaker DeLuxe (Brazil) [file-hunter]
Music Creator (Netherlands) [file-hunter]
Professional Data Retrieve (Brazil) [file-hunter]
Professional Paint (Brazil) [file-hunter]
Professional Publisher (Brazil, cracked) [file-hunter]
Rekenen tot 20 + Optellen en aftrekken tot 100 + Taalbedrijf (Netherlands) [file-hunter]
SF Zone 1999 (Japan) [file-hunter]
Simulador Profesional de Tenis (Spain) [file-hunter]
Super Procole (Japan) [file-hunter]
Super Procole 2 (Japan) [file-hunter]
Super Procole 3 (Japan) [file-hunter]
Supersellers 1 (Netherlands) [file-hunter]
Twin Hammer (Korea) [file-hunter]
The Wood (Spain) [file-hunter]
Woordmaker en Cijferend Vermenigvuldigen (Netherlands) [file-hunter]
Word Plus (Brazil) [file-hunter]
Wordstore+ (Netherlands) [file-hunter]
Zen (United Kingdom) [file-hunter]
3D Maze [Chalky]
666 - Uma Aventura Macabra [file-hunter]
8192 Story Tower [NAGI-P SOFT]
Baruko [file-hunter]
Blinky's Scary School [file-hunter]
Bounce Mania [MSXdev]
Burner Burst [file-hunter]
Buster Mystery [file-hunter]
City (Japan) [file-hunter]
Defence (v1.3) [MSXdev]
Galaxy Zone [aburi6800]
Ghosts'n Goblins (v1.1.0) [file-hunter]
Hibernated 1 - This Place is Death [file-hunter]
Hibernated 1 - Eight Feet Under [file-hunter]
JUMPER [NAGI-P SOFT]
Kame Graphics [file-hunter]
Kill Mice [MSXdev]
Las Aventuras de Rudolphine Rur (Spanish) [Dwalin]
Las Aventuras de Rudolphine Rur (Spanish, xmessage) [Dwalin]
Last War [NAGI-P SOFT]
Last War II [NAGI-P SOFT]
Logic (Russia) [file-hunter]
Mars [NAGI-P SOFT]
Mars II [NAGI-P SOFT]
May The Force Be With You [Cobinee]
Maze Chase [JLTurSan]
Micro Rocketz [MSXdev]
Mood Land [file-hunter]
Muhonmourn 3 (v1.1) [MSXdev]
Muhonmourn 3 (v1.1, with Ninja Tap support) [file-hunter]
Muhonmourn 3 (v1.0) [file-hunter]
Nibbles [file-hunter]
Oceano [file-hunter]
Paint-it (rev2) [file-hunter]
Paint-it (rev1) [file-hunter]
Paint-it [file-hunter]
Palhada City (Brazil) [file-hunter]
Penguin Catcher (v1.1) [MSXdev]
Penguin Catcher (v1.0) [file-hunter]
Pyramid Quest [Crappysoft]
Raftoid [PlattySoft]
Roger Dice (Spain) [oniric-factor]
Search for Mum (Netherlands) [file-hunter]
Sim City [file-hunter]
Storm Rescue [Concurso MSX-BASIC]
Stripgirl [file-hunter]
SubCommander (v1.02) [MSXdev]
SubCommander (older) [file-hunter]
Super Adventure [file-hunter]
The Tower of Gold [MSXdev]
UZIX (v1.0.0) [UZIX]
Wash Man (v2.8) [MSXdev]
Wash Man (v1.9) [file-hunter]
Wash Man (v1.5) [file-hunter]
Wash Man (v1.3) [file-hunter]
Wash Man (v1.2) [file-hunter]
Wash Man (v1.1) [file-hunter]
Wash Man (v1.0) [file-hunter]
Wired Shooting [Cobinee]
MSXMAS Demo [file-hunter]
Xadrama [file-hunter]
Xarchon [file-hunter]
XOR [Chalky]
XOR (older) [file-hunter]
Yellow Submarin [file-hunter]
Yobai [file-hunter]
Zero Gravity [file-hunter]
The zoBITRONics Inc [Hannu Töyrylä]
Zone TNT [MSXdev]
La Abadia del Crimen (Spain, alt) [file-hunter]

---
## [MellowArpeggiation/fung.js](https://github.com/MellowArpeggiation/fung.js)@[900e168d47...](https://github.com/MellowArpeggiation/fung.js/commit/900e168d47efc222c9a3d698ecd391c35e6be7fc)
#### Wednesday 2023-08-30 06:23:44 by George Paton

This is a horrible workaround, but it does work. Mobile browser vendors get your shit together I fucking swear to god

---
## [inkoalawetrust/Military-Vehicles-Pack](https://github.com/inkoalawetrust/Military-Vehicles-Pack)@[eb84b38aa9...](https://github.com/inkoalawetrust/Military-Vehicles-Pack/commit/eb84b38aa96ba2e1e75d70906928664ae07555e0)
#### Wednesday 2023-08-30 06:34:43 by inkoalawetrust

Tank now intentionally runs over enemies & corpses

- Gave the tank the ability to deliberately run over enemies as an attack. If the tanks' enemy is weak enough and not a ranged enemy (e.g a Demon, but not some kind of melee enemy with as much health as a Hell Baron) it will intentionally attack by running them over. Alternatively, it will crush even ranged enemies, as long as they are weak enough, such as Zombiemen.
- Added the ability for the tank to crush corpses like the APC. Also controlled through User_CrushMode, it doesn't affect the tanks' ability to push things out of the way however.
- Doubled the tanks' crushing damage from 6 to 12 per step.
- Finished the hulls' obituaries.
- Fixed a magical regression caused in the corpse seeking code during the GetClosestActor() call.

---
## [mdazfar2/aws_AI_finger_webApp_live](https://github.com/mdazfar2/aws_AI_finger_webApp_live)@[631083fc4b...](https://github.com/mdazfar2/aws_AI_finger_webApp_live/commit/631083fc4bfd5bed88467496880d5e7829ef35e0)
#### Wednesday 2023-08-30 07:16:40 by Md Azfar Alam

Update README.md

# aws_AI_finger_webApp_live
Introducing FingerConnect: Seamlessly bridge the gap between your Android mobile and your PC with a touch of innovation!

Have you ever wished for a magical connection between your smartphone and your computer? Look no further – FingerConnect is here to make your dreams a reality. 🌟

Imagine this: effortlessly launching applications and instances on your PC by simply showing your finger on your Android mobile. With FingerConnect, we've turned this imaginative concept into a tangible, cutting-edge project that showcases the true power of seamless device integration.

Our open-source project allows you to harness the potential of your devices like never before. By uploading the entire codebase to our GitHub profile, we're sharing the magic with the global community of tech enthusiasts, creators, and innovators. Whether you're a seasoned developer, a curious hobbyist, or just someone intrigued by the possibilities, FingerConnect invites you to explore, experiment, and contribute.

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[22c8f24b2c...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/22c8f24b2ca76e0512368ecbbab3c4196e8462a0)
#### Wednesday 2023-08-30 07:29:25 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>
Signed-off-by: pix106 <sbordenave@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [eryue0220/react](https://github.com/eryue0220/react)@[ac1a16c67e...](https://github.com/eryue0220/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Wednesday 2023-08-30 07:48:40 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [msft-mirror-aosp/platform.external.bpftool](https://github.com/msft-mirror-aosp/platform.external.bpftool)@[911adbfc89...](https://github.com/msft-mirror-aosp/platform.external.bpftool/commit/911adbfc89e7fd80e576bcf4578ec4da5b74a87a)
#### Wednesday 2023-08-30 09:43:20 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Thanks also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Acked-by: Jakub Kicinski <kuba@kernel.org>
Link: https://lore.kernel.org/r/20230719140858.13224-3-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [msft-mirror-aosp/platform.external.bpftool](https://github.com/msft-mirror-aosp/platform.external.bpftool)@[e0e6b3aaa9...](https://github.com/msft-mirror-aosp/platform.external.bpftool/commit/e0e6b3aaa9cff3103de7c7e0d778a875d897c556)
#### Wednesday 2023-08-30 09:43:20 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Thanks also to Andrii Nakryiko for early API discussions wrt Meta's BPF prog
management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Link: https://lore.kernel.org/r/20230719140858.13224-2-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [Mission23/journal-micah](https://github.com/Mission23/journal-micah)@[087caef6a3...](https://github.com/Mission23/journal-micah/commit/087caef6a3c75a17ebb8e6554c7ad4049cf442fb)
#### Wednesday 2023-08-30 10:26:35 by Micah

Attack at Exxon

I started some edits on our wiki tonight. Trouble tickets. They started
attqcking me at home so i came for a cigarette. This woman pulls up,
and something shot from the rear passenger tire. I thought I'd let her
know.

She already knew. But I don't think she's heard the truth about her
company's church activities until i told her just one small bit of
them lately.

Yes. This massacre is just a piece of what that good Christian
Innameonly Agency has done in churches. Black And white churches. They
dont give a fuck. They want their money, they know what they need to
do to get it, they dont mind doing it at all.

My boss, He dont mind doing them either. They WILL live, He always
leave things living. They just wont like it anymore.

---
## [robtfm/bevy](https://github.com/robtfm/bevy)@[44f677a38a...](https://github.com/robtfm/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Wednesday 2023-08-30 11:10:51 by Sélène Amanita

Improve documentation relating to `Frustum` and `HalfSpace` (#9136)

# Objective

This PR's first aim is to fix a mistake in `HalfSpace`'s documentation.

When defining a `Frustum` myself in bevy_basic_portals, I realised that
the "distance" of the `HalfSpace` is not, as the current doc defines,
the "distance from the origin along the normal", but actually the
opposite of that.

See the example I gave in this PR.

This means one of two things:
1. The documentation about `HalfSpace` is wrong (it is either way
because of the `n.p + d > 0` formula given later anyway, which is how it
behaves, but in that formula `d` is indeed the opposite of the "distance
from the origin along the normal", otherwise it should be `n.p > d`)
2. The distance is supposed to be the "distance from the origin along
the normal" but when used in a Frustum it's used as the opposite, and it
is a mistake
3. Same as 2, but it is somehow intended

Since I think `HalfSpace` is only used for `Frustum`, and it's easier to
fix documentation than code, I assumed for this PR we're in case number
1. If we're in case number 3, the documentation of `Frustum` needs to
change, and in case number 2, the code needs to be fixed.

While I was at it, I also :
- Tried to improve the documentation for `Frustum`, `Aabb`, and
`VisibilitySystems`, among others, since they're all related to
`Frustum`.
- Fixed documentation about frustum culling not applying to 2d objects,
which is not true since https://github.com/bevyengine/bevy/pull/7885

## Remarks and questions

- What about a `HalfSpace` with an infinite distance, is it allowed and
does it represents the whole space? If so it should probably be
mentioned.
- I referenced the `update_frusta` system in
`bevy_render::view::visibility` directly instead of referencing its
system set, should I reference the system set instead? It's a bit
annoying since it's in 3 sets.
- `visibility_propagate` is not public for some reason, I think it
probably should be, but for now I only documented its system set, should
I make it public? I don't think that would count as a breaking change?
- Why is `Aabb` inserted by a system, with `NoFrustumCulling` as an
opt-out, instead of having it inserted by default in `PbrBundle` for
example and then the system calculating it when it's added? Is it
because there is still no way to have an optional component inside a
bundle?

---------

Co-authored-by: SpecificProtagonist <vincentjunge@posteo.net>
Co-authored-by: Alice Cecile <alice.i.cecile@gmail.com>

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[d5b1193802...](https://github.com/insertnamehere123/cmss13/commit/d5b119380250ea512db2a5319e36592c7f604250)
#### Wednesday 2023-08-30 12:15:28 by fira

FOB Tents  (#3509)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Sprites stolen from thwomper and sammy, available NOW with game code!

Adds a few tents to be used in FOB building, mainly for organizational
purposes but also providing small gameplay benefits. At current the main
goal is to incentive usage to organize and liven up FOB, so the buffs
are rather small.

There are 4 tent types:
* The Command Tent is a 2x3 structure that comes bundled with an
overwatch console, a phone, and two (2) chairs.
* The Medical Tent is a 2x3 structure that comes with a NanoMED, 2
roller beds, and slightly buffs surgery (10% less time taken, and a very
token pain/failure chance improvement)
* The Requisitions Tent is a 4x3 structure that comes with a phone,
rack, desks, and a variant of the old APC vendor that can stock
materials and regular ammunition. The vendor starts empty, save for some
tables/racks/paperwork for organization purposes. It is only useable
with requisitions access.
* The Big Tent is a bigger tent for all your organizational needs: 3x3.
Get creative.

The tents also provide decent additional protection against cold
environements. Unfortunately, rain/snow will visually pour through it, i
can't do much about that.

The tents are extremely vulnerable to explosives and xeno claws. For
simplicity and technical reasons, they are currently NON REDEPLOYABLE
and NON REPLACEABLE. The tent destruction will destroy/disable linked
objects (console/vendor etc). Be mindful of where you place them.

**Mind that the tents may not work out for all LZ FOBs due to the
required space. I expect people will find ways to make it work anyway
but it might take a while.**

# Explain why it's good for the game

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

I'm lazyyy i forgot and already closed the game... If you actually want
em bug me and i'll add em
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

:cl: Firartix , Thwomper and Sammy
add: Added four types of tents to liven up FOB. They provide cold
protection and benefits depending on their type. The tents spawn in
Requisitions roundstart near the mortar. They're vulnerable to
explosives and xenomorphs, and NON REPLACEABLE. Mind where you put them!
add: The Command tent comes equipped with an overwatch console and a
phone.
add: The Medical tent provides a small boost to surgery speed/pain
carried out inside it.
add: The Requisitions tent provides a restockable vendor, desk, and
furniture for organization.
add: The Big tent is just a big tent, and provides you a slate to
organize the way you want.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [mcdofrenchfreis/biofrost-kernel-realme-trinket](https://github.com/mcdofrenchfreis/biofrost-kernel-realme-trinket)@[d008163df4...](https://github.com/mcdofrenchfreis/biofrost-kernel-realme-trinket/commit/d008163df4ee8545475985da59b711632c4cf52c)
#### Wednesday 2023-08-30 13:04:11 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>

---
## [mcdofrenchfreis/biofrost-kernel-realme-trinket](https://github.com/mcdofrenchfreis/biofrost-kernel-realme-trinket)@[1d6fd76a5e...](https://github.com/mcdofrenchfreis/biofrost-kernel-realme-trinket/commit/1d6fd76a5ed51a32ad090de48033acc523ed7d25)
#### Wednesday 2023-08-30 13:10:54 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>

---
## [MobilePorting/FNF-PsychEngine-Mobile](https://github.com/MobilePorting/FNF-PsychEngine-Mobile)@[1c55e6d3c4...](https://github.com/MobilePorting/FNF-PsychEngine-Mobile/commit/1c55e6d3c48c7f626fa284345c05adfacbd51e76)
#### Wednesday 2023-08-30 13:13:10 by Lily

Revert "fuck you iOS"

This reverts commit 405324b42dcc6e8b08d1bfe5d31dfc14d6de8443.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d24bcb4a84...](https://github.com/treckstar/yolo-octo-hipster/commit/d24bcb4a84d988116bc20197c2044998045e1b5e)
#### Wednesday 2023-08-30 13:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [narickmann/opencast-studio](https://github.com/narickmann/opencast-studio)@[e8f8d53bc8...](https://github.com/narickmann/opencast-studio/commit/e8f8d53bc8a3da297d394dcaef622032a0c5407e)
#### Wednesday 2023-08-30 13:53:11 by Lukas Kalbertodt

Fix theme bug where always light theme colors were used

This is... annoying. So my previous hacky solution with `colorz` was
broken. That object was always exactly what I put in, so all code
referring to it always used the light mode colors. The `colors` field
is instead replaced by theme-ui, at some point, magically, to contain
strings with `var()` references. We have to use those to get the correct
colors all the time. I tried a `get colorz() { return this.colors }`
but that didn't work either as the getter was evaluated very early, and
also only once, at which point `colors` was not transformed yet.

So I decided to just bite the bullet and search&replace all cases, using
`colors` instead. This adds some ugly `?.` accesses and loses type
safety. It's basically a `record<string, any>` here. So we won't catch
color name typos, for example.

It seems that theme-ui is just not really designed for Typescript.
Usually, you also specify colors just as strings, i.e. `bg: "primary"`
which is also not type safe.

Maybe I can improve this in the upcoming redesign work, but for now we
should just fix the bug.

---
## [getcord/sdk-js](https://github.com/getcord/sdk-js)@[3512ba4269...](https://github.com/getcord/sdk-js/commit/3512ba4269c182e56befddfa0b15f4d8b8475472)
#### Wednesday 2023-08-30 14:21:48 by Josh Watzman

Remove/replace lodash

lodash was designed for a world a decade ago, where JS wasn't nearly as
advanced as it is today, and reflects that world. It's still got a ton of
useful utility functions, but their implementation leaves a lot to be desired.
It's a gigantic library code-size-wise, because the implementations try to deal
with now-ancient browsers with limited JS. Worse, the way it was written isn't
amenable to tree-shaking, and it has a frankly bizzare split between its cjs
and esm versions that cause us huge build system headaches. It also looks like
lodash is no longer under active development, with no commits in the last
couple of years.

But worst is that it's so easy to accidentally include the whole darn thing and
inflate the size of `sdk.latest.js` -- which #5845 did, by ~23k *compressed*
bytes (~4%!), and I only noticed because I just so happened to be looking at
some logging I added months ago.

And there isn't even a good way to fix it due to our build system
issues. The default lodash package is cjs-only, which is fine for our
internal build since we compile from esm to cjs anyway. But for our OSS
packages, we provide both esm and cjs versions, so that doesn't work.
(It *might* without the esModuleInterop issues we have, but that's an
entire other can of worms.) There is an esm version of lodash, but it's
a completely separate package, and using that breaks our internal build.
I could dig into what's going on here and try to solve it -- it probably
is solvable -- or we could move away from the only package in the entire
world which has caused us this sort of grief.

This PR replaces all of our usage of lodash with other things.


Reviewers: #infra, flooey, elenaperezrioja

Reviewed By: elenaperezrioja

Pull Request: https://github.com/getcord/monorepo/pull/5983

monorepo-commit: 86b7f6e096204ed757a3a5706570f218d1feae8d

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[a95d6a3656...](https://github.com/cmss13-devs/cmss13/commit/a95d6a3656ff6dd7ff220bb30259080c231d0f03)
#### Wednesday 2023-08-30 14:44:42 by QuickLode

PMC Survivors can now use WY channel (#4234)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.
Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

It allows PMC Survivors to utilize the WY channel.
# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->
Allowing PMC Survivors to communicate and thus RP better with WY assets
and within themselves. Team-based survivors should stick together
because lone wolves are not good for RP - I think we have seen a lot of
evidence from Chance's Claim survivors who, upon withdrawing, break
apart and cannot ever regroup due to communication impossibilities. From
an outsider's perspective, the impact of seeing a 'team' of survivors vs
a single survivor is a difference like night and day. With the former
being much more immersive and reflective of the professionalism a team
would have.

Also all that aside it was unintended for PMC Survivors to not have WY
comms - consider this a bugfix haha

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
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
fix: PMC Survivors now can use WY Comms.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [openembedded/openembedded-core](https://github.com/openembedded/openembedded-core)@[387b276c2d...](https://github.com/openembedded/openembedded-core/commit/387b276c2d56d58c2a25d59984fcaaf9c88ac788)
#### Wednesday 2023-08-30 14:52:09 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [yoctoproject/poky](https://github.com/yoctoproject/poky)@[89394ac832...](https://github.com/yoctoproject/poky/commit/89394ac832e1a3f584271e3c855168c78b75e471)
#### Wednesday 2023-08-30 14:53:03 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

(From OE-Core rev: 387b276c2d56d58c2a25d59984fcaaf9c88ac788)

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[76cec56fc9...](https://github.com/Jolly-66/JollyStation/commit/76cec56fc93219d27aa0dbd1e0d201b98deaadd8)
#### Wednesday 2023-08-30 15:07:54 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks (#7173)

Original PR: https://github.com/tgstation/tgstation/pull/77393
-----
## About The Pull Request

Goliath's sand digging behaviour could potentially target a turf that's
actually unreachable by the goliath, e.g.
```
G#
#T
```
where G - goliath # - wall T - target turf. fixed that, but i think
there could be something easier here, maybe instead grabbing turfs in
goliath's `view()`? unsure

The component goliaths use to telegraph their attacks
(`basic_mob_attack_telegraph`) casts a `do_after()` to perform the
attack, but it was not actually checking for the target staying in melee
range, as it was using the source goliath as both `user` and `target`,
so it didn't actually care at all for the target. Implemented an
`extra_checks` to `Adjacent()` since that's the closest we get for melee
range shenanigans I suppose
This still allows the source basicmob to attack the target if the target
moves around the source basicmob.

`!`Goliaths were also able to summon tentacles on a target that moved
into cover and still stayed in the `find_potential_targets` target
range. Which meant more wallhacks. This was a thing for the base
`find_potential_targets`, meaning that every basic mob using it was a
dirty haxxor (or very vengeful). Fixed that by making
`find_potential_targets` also check for `can_see()` before proceeding
further down `find_potential_targets/perform()`. `!` The only exception
to this check currently are bileworms.

`!`Goliath tentacles were not spawning in mineral turfs as their
`Initialize()` checked for closed turfs before handling mineral turf
mining. Fixed that as well.

## Why It's Good For The Game

![Dr__Hax_by_Didgeridoo_Dealer](https://github.com/tgstation/tgstation/assets/75863639/fbcbfc1b-f489-435e-bb01-677f55398787)

## Changelog

:cl:
fix: fixed goliaths digging sand that they can't actually reach (behind
windows or inbetween closed turfs)
fix: fixed goliaths melee attacking their target despite the target
running away from goliath melee range
fix: fixed goliath tentacles not spawning in mineral turfs
fix: fixed goliaths summoning tentacles on targets that moved behind
cover but stayed in their targeting range. this applies for most basic
mobs, really, so if any basic mob was targeting you despite you hauling
ass behind cover, they shouldn't anymore
/:cl:

---------

Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>

---
## [pulumi/pulumi](https://github.com/pulumi/pulumi)@[3d9ddb2981...](https://github.com/pulumi/pulumi/commit/3d9ddb2981016dbdfa7ff4293b2eb814e9d11ce1)
#### Wednesday 2023-08-30 15:32:33 by Fraser Waters

Support bailing from RunFunc (#13804)

**Background**

The result.Result type is used by our CLI implementation to communicate
how we want to exit the program.

Most `result.Result` values (built from errors with `result.FromError`)
cause the program to print the message to stderr and exit the program
with exit code -1.
The exception is `result.Bail()`, which indicates that we've already
printed the error message, and we simply need to `exit(-1)` now.

Our CLI command implementation use `cmdutil.RunResultFunc` which takes a
`func(...) result.Result` to implement this logic.

`cmdutil` additionally includes a `cmdutil.RunFunc` which takes a
`func(...) error` and wraps it in `RunResultFunc`, relying on
`result.FromError` for the conversion:

    func RunFunc(run func(...) error) func(...) {
        return RunResultFunc(func(...) result.Result {
            if err := run(...); err != nil {
                return result.FromError(err)
            }
            return nil
        })
    }

**Problem**

In CLI contexts where we're using an `error`, and we want to print an
error message to the user and exit, it's desirable to use diag.Sink to
print the message to the user with the appropriate level (error,
warning, etc.) and exit without printing anything else.

However, the only way to do that currently is by converting that
function to return `result.Result`, turn all error returns to
`result.FromError`, and then return `result.Bail()`.

**Solution**

This change introduces a `result.BailError` error that gets converted
into a `result.Bail()` when it passes through `result.FromError`.

It allows commands implementations that use `error` to continue
returning errors and still provide an ideal CLI experience.

It relies on `errors.As` for matching, so even if an intermediate layer
wraps the error with `fmt.Errorf("..: %w", ErrBail)`, we'll recognize
the request to bail.

BailError keep track of the internal error that triggered it, which
(when everything is moved off of result and onto error) means we'll
still be able to see the internal errors that triggered a bail during
debugging.

Currently debugging engine tests is pretty horrible because you often
just get back a `result.Result{err:nil}` with no information where in
the engine stack that came from.

**Testing**

Besides unit tests, this includes an end-to-end test for using
RunResultFunc with a bail error.
The test operates by putting the mock behavior in a fake test, and
re-running the test binary to execute *just that test*.

**Demonstration**

This change also ports the following commands to use BailError: cancel,
convert, env, policy rm, stack rm.

These command implementations are simple and were able to switch easily,
without bubbling into a change to a bunch of other code.

---
## [rdragan/tgstation](https://github.com/rdragan/tgstation)@[b0ec1e4098...](https://github.com/rdragan/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Wednesday 2023-08-30 15:40:04 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---
## [dwhiteplume/dwhiteplume.github.io](https://github.com/dwhiteplume/dwhiteplume.github.io)@[4dca39fee0...](https://github.com/dwhiteplume/dwhiteplume.github.io/commit/4dca39fee08b6534756162f9b75b71f6918e20c7)
#### Wednesday 2023-08-30 17:42:34 by Darius Whiteplume

Update index.html

Fixed the favor the editor did for me. Can editors stop completing tags for me? Is that so hard? Can a mfucker who grew up with Notepad write his own damn code for a minute without you messing me up when I’m not looking? Are you even listening, internet? Is this thing on?

Anyway, I fixed the closing tag. Enjoy.

---
## [BlackHC/skorch](https://github.com/BlackHC/skorch)@[df92d4d5e3...](https://github.com/BlackHC/skorch/commit/df92d4d5e3cc5991330e339d6c8d6c83798f0caa)
#### Wednesday 2023-08-30 18:16:04 by Benjamin Bossan

Allow regression with 1d targets (#974)

* Allow regression with 1d targets

This change makes it possible to pass a 1-dimensional y to
`NeuralNetRegressor`.

Problem description

Right now, skorch requires the `y` passed to `NeuralNetRegressor.fit` to
be 2-dimensional, even if there is only one target, as is the most
common case. This problem has come up a few times in the past, but
mostly it's just an annoyance - just do `y.reshape(-1, 1)` and you're
good (the error message says as much).

There are, however, also cases where it's not so easy to solve. For
instance, in #972, a user reports that they cannot use skorch with
sklearn's `BaggingRegressor`. The problem is that even if `y` is
reshaped, once it is passed to the net from `BaggingRegressor`, it is 1d
again. I assume that `BaggingRegressor` internally squeezes `y` at some
point.

This PR lifts the 2d restriction check.

Initial motivation

Why does skorch require `y` to be 2d? I couldn't remember the initial
reasoning and did some archeology.

I found this comment:

(https://github.com/skorch-dev/skorch/commit/2f00e2570460fe0a6acd8db94c4d8624b3ddd1eb#diff-66ed08bca4d171889565d0285a36b9b47e0e91e3b33d85c51352d8eb00faefac):

>         # The problem with 1-dim float y is that the pytorch DataLoader will
>         # somehow upcast it to DoubleTensor

This strange behavior should not be an issue anymore, so if that was the
only problem, we should be able to just remove the constraint, right?

Problems with removing the constraint

Unfortunately, it's not that easy. The issue comes down to the
following: When we remove the constraint and allow the target `y` to be
1d, but the prediction `y_pred` is still 2d, the criterion `nn.MSELoss`
will probably do the wrong thing. What exactly is wrong? Instead of
calculating the squared error for each sample pair, the criterion
will broadcast the vector and calculate _all squared errors_ between
each sample, then return the mean of that. To demonstrate, let's remove
the reduction step and look at the shape:

```python
>>> import torch
>>> criterion = torch.nn.MSELoss(reduction='none')
>>> y = torch.rand(100)
>>> y_pred = torch.rand((100, 1))
>>> y.shape, y_pred.shape
(torch.Size([100]), torch.Size([100, 1]))
>>> se = criterion(y_pred, y)
/home/vinh/anaconda3/envs/skorch/lib/python3.10/site-packages/torch/nn/modules/loss.py:536: UserWarning: Using a target size (torch.Size([100])) that is different to the input size (torch.Size([100, 1])). This will likely lead to incorrect results due to broadcasting. Please ensure they have the same size.
  return F.mse_loss(input, target, reduction=self.reduction)
>>> se.shape
torch.Size([100, 100])
```

As can be seen, PyTorch broadcasts the two arrays, leading to 100x100
errors being calculated. Thankfully, PyTorch warns about potential
issues with that.

The current solution is to accept this behavior and hope that the users
will indeed see the warning. If they don't see it or ignore it, it could
be a huge issue, because they still get a loss scalar and might even see
a small improvement in the loss during training. But the model will not
converge and it's going to be a huge pain to debug the bug, if it's even
identified as such.

Just to be clear, existing code, which uses 2d targets, will not be
affected by the change introduced in this PR and is still the preferred
way (IMO) to use regression in skorch.

Rejected solutions

I did consider the following solutions but rejected them.

Raising an error when shapes mismatch

This would remove the risk of users missing the warning. The problem
with this is that mismatching shapes can be okay in certain
circumstances. Some criteria don't expect target and prediction to have
the same shape, so we would need to check based on criterion. Moreover,
theoretically, users may indeed want to broadcast. Raising an error
would prevent that and users may have to resort to subclassing to
circumvent the error.

Automatic reshaping

We could automatically add/remove dimensions if we see that they
mismatch. This has the same problems as the previous solution regarding
the dependence on the type of criterion. Furthermore, automatic
adjustment of the user's output is prone to run into issues in some edge
cases (e.g. when the broadcasting is actually desired).

* Fix error when initializing BaggingRegressor

For Python 3.7, CI got:

TypeError: __init__() got an unexpected keyword argument 'estimator'

for BaggingRegressor. Probably it installs an older version of sklearn,
which uses a different argument name. Passing as positional arg should
fix it.

* Reviewer comment: typo

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

* Reviewer comment: typo

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

---------

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[20c8c9783a...](https://github.com/vampirebat74/lobotomy-corp13/commit/20c8c9783a1486e549cab49a0c1c5b33d79baf0a)
#### Wednesday 2023-08-30 18:35:56 by Mr.Heavenly

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes suit check in assimilate() proc

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes dismembering

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

breach is more dangerous

compiles

bug fix

fixes simple mob

bug fixes

Panic fixed!!!!

stuff

---
## [Fuyukai/Reborn-Rebalance](https://github.com/Fuyukai/Reborn-Rebalance)@[de31477245...](https://github.com/Fuyukai/Reborn-Rebalance/commit/de314772454179e7921793b25779d89c1078d9a2)
#### Wednesday 2023-08-30 18:51:03 by Lura Skye

rebalance serra's gym battle.

- FUCK bright powder
- glaceon has ice scales to make it even more absurdly bulky
- alolatails now has a recovery move instead of NP
- lapras has AV instead of the evasion seed
- frosmoth has LO for max fuck youness
- replace froslass with cetitan (lol, fuck your theme)

---
## [alexchen2/Chord-Recombinator-Web](https://github.com/alexchen2/Chord-Recombinator-Web)@[87198a7e4a...](https://github.com/alexchen2/Chord-Recombinator-Web/commit/87198a7e4a04366404d123e7f021788c0cbe0538)
#### Wednesday 2023-08-30 19:12:35 by Alex Chen

Finished table dropdown

- Added table row dropdown feature, displaying staff with specific chord notes (using VexFlow library)
- Fixed music.js not recognizing dominant 13ths or acoustic scales (due to JS not supporting negative indexing with brackets)
- Significantly increased amount of stress and pain working on this goddamn stupid project :D

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[3f30dbe611...](https://github.com/newstools/2023-new-york-post/commit/3f30dbe611eeb9897f72e4d6abcc6435a9d5138b)
#### Wednesday 2023-08-30 19:16:11 by Billy Einkamerer

Created Text For URL [nypost.com/2023/08/30/i-caught-my-boyfriend-cheating-right-before-our-9-week-vacation-heres-how-i-got-revenge/]

---
## [powerhome/playbook](https://github.com/powerhome/playbook)@[205619a0e9...](https://github.com/powerhome/playbook/commit/205619a0e9ce327306acf84735c13ea4ed356c7b)
#### Wednesday 2023-08-30 19:28:39 by Gavin Huang

[PLAY-972] dateTime Bug Fixes (#2716)

**What does this PR do?**
- Corrects incorrect weekdays by removing the `getUTC` functions
- In the DB, for example, the date was August 15, 2023 01:30:00. The
`toWeekday` function formatted the date from UTC to Local Time, but
`getUTCDay()` went back to grab the UTC date. This issue was evident
with late-day appointments. Therefore, we should not be using any
`getUTC` functions.
- Corrects two bugs Jason found within`fromNow()`:
  - Remove period from "years ago"
- Fix miscalculation of "milliseconds in a month" - this was causing any
past date with a timestamp of "x months ago" to have a random number
- Updates `toLocaleString()` to use `en-US`
- Hayden R. reported he was receiving `undefined NaN`. Upon
investigation, certain locales (like en-GB [Great Britain]), can't use
functions like `getMonth()` so it was returning `undefined NaN`. We
default to `en-US` because internationalization and formatting does not
matter since Playbook formats dates in a specific way.

**Screenshots**

**Before**

![Before](https://github.com/powerhome/playbook/assets/47684670/07303adf-f2eb-4d7b-a0ba-ad82cf7f945c)

**After**

![After](https://github.com/powerhome/playbook/assets/47684670/8696283f-d4b4-4ab3-9302-c9651af672cd)

**How to test?** Steps to confirm the desired behavior:
1. The weekday problem was experienced in the [Sales
Books](https://nitro.powerhrg.com/sales/reps/11115/sales_books?rep_filter%5Bdate%5D%5Byear%5D=2023&rep_filter%5Bdate%5D%5Bmonth%5D=8).
In Miguel Picart's (or any RC), select their "Books" tab, select "All
Appointments", find any place that has 2+ appointments the same day -
they should be correct.
2. For Hayden's bug, impersonate Hayden and in his user profile ensure
that the address is showing as his European address. Go to a Runway
ticket and check the reviewers, he should not see `undefined NaN`. We
should also ensure that Hayden can see a date after the release.

#### Checklist:
- [X] **LABELS** Add a label: `enhancement`, `bug`, `improvement`, `new
kit`, `deprecated`, or `breaking`. See [Changelog &
Labels](https://github.com/powerhome/playbook/wiki/Changelog-&-Labels)
for details.
- [X] **DEPLOY** I have added the `milano` label to show I'm ready for a
review.
- [ ] **TESTS** I have added test coverage to my code.

---------

Co-authored-by: Nida Ghuman <nidaqg@gmail.com>

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[1b315a616f...](https://github.com/spockye/Shiptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Wednesday 2023-08-30 20:08:59 by Thedragmeme

Aegis update + patient clothing (#2150)

## About The Pull Request
The Aegis:
![2023-07-09 06 32
40](https://github.com/shiptest-ss13/Shiptest/assets/81540056/cf262257-1699-40e0-bcb1-6dc60f1e98a6)
I've touched up the central hallway's decals, they always bothered me
but at the time of the Aegis' creation, I wasn't as well versed with map
making as I am now. They're small tweaks that look better to me. The
smart fridge was removed and turned into a board, originally you could
access the smart fridge from outside of the ship, which wasn't intended.
Added some new posters. Compressed the number of red lockers down and
cleaned up the main hallway. I gave the psychologist a dart gun because
honestly, it sounded really funny.

![dart
riffle](https://github.com/shiptest-ss13/Shiptest/assets/81540056/eb10154a-1e28-4a5d-b41b-9b20f92b71a9)

Also, there are more seeds to make food with. There were like only two
food seeds and like five flowers before.

The Patient set:


![patient](https://github.com/shiptest-ss13/Shiptest/assets/81540056/65066ea3-92d1-4233-9bf6-a6448d43b11f)

Kepori and Vox versions are available. Long-term patients now spawn with
the white gown and slippers. The previous clothes they spawned with were
always intended to be replaced.

Hopefully, this PR also fixes long-term patients spawning with borked
ID's.

## Why It's Good For The Game

Fixing stuff, making stuff look better, and adding new RP opportunities
with clothes are good.

## Changelog

:cl: Drag
add: Adds a bunch of shit to the Aegis, nothing earth shattering
add: Added the patient set, along with Vox and Kepori compatible sprites
tweak: tweaked with the Aegis' decals
fix: (Hopefully) Fixes the Aegis' patient Id's
:cl:

---------

Signed-off-by: Thedragmeme <81540056+Draggeru@users.noreply.github.com>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [YakumoChen/tgstation](https://github.com/YakumoChen/tgstation)@[2d34c7433a...](https://github.com/YakumoChen/tgstation/commit/2d34c7433a0c5315e6a46f7e32e2c9a6c90280b3)
#### Wednesday 2023-08-30 20:19:59 by Andrew

New Mech UI and equipment refactor (#77221)

![bWJlVIDO53](https://github.com/tgstation/tgstation/assets/3625094/d75030b5-59e9-43f6-96b4-1b7564caceef)

## About The Pull Request

Made a new UI and refactored some mech code in the process.

Fixes #66048
Fixes #77051
Fixes #65958 ??? if it was broken
Fixes #73051 - see details below
Fixes other undocumented things, see changelog.

## Why It's Good For The Game

The UI was too bulky and Mechs were too complex for no reason. 
Now they follow some general rules shared between other SS13 machinery,
and there is less magic happening under the hood.

## Detailed Changes

### New Mech UI, Air Tank and Radio as separate modules

Previous UI for comparison:

<img alt="9SScrXAOjy"
src="https://github.com/tgstation/tgstation/assets/3625094/904e3d07-e7d7-4d3a-a062-93e0e35b4b66">

Previously mechs came with radio pre-installed and air canisters
magically pre-filled with air even when you build one in fab.
Radio and Air Tanks are now both utility modules that are optional to
install. Gas RCS thrusters still require Air Tank module to operate.

This made the Mechs more barebones when built, giving you only the basic
functionality.

<img alt="5SDMlXTJxv"
src="https://github.com/tgstation/tgstation/assets/3625094/b9364230-49ac-416b-aa70-e851fbf2050e">

To compensate this change, all mechs got two extra utility module slots.

All other modules got new UI. And ore box now shows the list of ores
inside.

<img alt="SRX5FjvsHA"
src="https://github.com/tgstation/tgstation/assets/3625094/cbe2e98d-1cd4-4667-8dae-2f9227b4b265">

### Mounted Radio

Works as a normal radio, but with subspace transmission. Available from
the basic mech research node and can be printed in fab.

### Cabin Sealing

To compensate for the lack of air tank by default, mechs with enclosed
cabin (e.g. all except Ripley) got an ability to toggle cabin exposure
to the outside air. Exiting the mech makes cabin air automatically
exposed.

When you seal the cabin, it traps some of the outside air inside the
cabin and you can breathe with this air to perform a short space trips.
But the oxygen will run out quickly and CO2 will build up.

Sealing the cabin in space will make the cabin filled with vacuum, and
it will stay there until you return to air environment and unseal the
cabin, letting the breathable air to enter. There are temperature and
pressure sensors that turn yellow/red when the corresponding warning
thresholds are reached.

You could also use personal internals in combination with cabin sealing
for long space travels, so Air Tank is completely optional now and
mostly needed when you need RCS thruster.

### RCS thrusters

They are now available earlier in tech tree and consume reasonable
amount of air (5 times more than human jetpacks), and they don't work
without Mounted Air Tank, unless it's an Ion thruster variant.

### Mounted Air Tank

Available from the basic mech research node and can be printed in fab.
Built model comes empty, and syndicate mechs come with one full of
oxygen.

<img alt="GrFDrH5Hwe"
src="https://github.com/tgstation/tgstation/assets/3625094/b677b705-bda0-4c8c-96c7-d32bf7bf9f28">

Can be switched to pressurize or not pressurize the cabin. Releases gas
only when the cabin is sealed shut. Starts releasing automatically, but
can be toggled to not release if you want to use it just as a portable
canister.

Cabin pressure can now be configured in the module UI instead of
Maintenance UI.

Can be attached to a pipe network when the mech is parked above a
connection port.

Comes with a pump that works similarly to the portable pump. It lets you
vent the air tank contents outside, or suck air from the room to fill
the air tank. Intended to provide an ability to fill the air tank
without the need to bother with pipes.

Also has gas sensors that display gas mix data of the tank and the cabin
(when sealed).

### Stock part changes

All mechs now require a servo motor and they reduce mech movement power
consumption instead of scanning module.

Scanning modules are optional for mech operation (still required to
build) and the lack of one disables the following UI elements:

- Display of mech integrity (you can still see the alerts or examine the
mech to get rough idea)
- Display of mech status on internal damage (and you can't repair what
you can't diagnose)

The rating of scanning module doesn't have any effect as of now.

Cargo mech comes without it roundstart.

<img alt="2vDtt99oqb"
src="https://github.com/tgstation/tgstation/assets/3625094/147144ca-824e-4501-acf5-6ee104f309e7">

Capacitors now also reduce light power usage and raise the overclocking
temperature thresholds (see below).

### Maintenance

Maintenance UI removed, and its logic migrated to other places.

Access modification now managed inside the mech, and anyone who can
control the mech, can adjust the access in the same way as they can set
DNA key.

To open the maintenance panel you just need a screwdriver. It is instant
when the mech is empty and it has a 5 second delay when there is an
occupant to avoid in-combat hacking and part removal. It will alert the
occupant that someone is trying to tinker with their mech.


![image](https://github.com/tgstation/tgstation/assets/3625094/1abfca3c-8ba9-44b0-913c-c209564b91fd)

Once the panel is open, you can see the part ratings:


![image](https://github.com/tgstation/tgstation/assets/3625094/404f95bb-9f74-4e5b-a975-5ab6f74bdfa9)

With open panel you can hack the mech wires (roboticists can now see
them):

<img alt="mj205G2qDa"
src="https://github.com/tgstation/tgstation/assets/3625094/44cea0d1-44b4-4b50-b1d3-a97c0056bab3">

There are wires for:
- Enabling/Disabling ID and DNA locks
- Toggling mech lights
- Toggling mech circuits malfunction (battery drain, sparks) 
- Toggling mech equipment malfunction (to repair after EMP or cause
EMP-like effect, disarming mech)
- 3 dud wires that do nothing

The hacker may be shocked if the mech power cell allows.

When the panel is open and the user has access to the mech, they can
remove parts with a crowbar:

<img alt="jR40gyTWtJ"
src="https://github.com/tgstation/tgstation/assets/3625094/b573f5b9-b8ea-412e-b3e0-c872e01e0c23">

Hitting the mech with an ID from outside now toggles the ID Lock on/off
if the ID has sufficient access.

### Power consumption and overclocking

Rebalanced mech power consumption. T4 parts were not working in
Syndicate Mechs, as their effect was not calculated until you manipulate
parts manually. Constructed mechs with t1 parts even had their energy
drain reduced with upgrade to t1.

Now all mechs apply their base step power usage correctly don't ignore
the stock parts.

Servo tier now reduces base power consumption by 0% at t1, 50% at t2,
33% at t3 and 25% at t4
Capacitor tier now reduces base power consumption of mele attacks,
phasing and light by the same amounts.

Gygax leg actuators overload replaced with mech overclocking. Any mech
can be overclocked by hacking wires, but only Gygax has a button for
toggling it from the Cabin.

Now there is an overclock coefficient. 1.5 for Gygax and other mechs, 2
for Dark Gygax.

When overclocked, mechs moves N times faster, but consumes N times more
power.


![image](https://github.com/tgstation/tgstation/assets/3625094/01e285fd-6fd6-4558-8277-2ed3abf474d8)

While overclocked, mech heats up every second, regardless of movement,
and starts receiving internal and integrity damage after a certain
temperature threshold. The chance is 0% at the threshold, and 100% at
thresholds * 2. The roll happens every tick. Capacitor upgrades this
threshold, letting you overclock safely for longer periods.


![image](https://github.com/tgstation/tgstation/assets/3625094/80d90cea-0d20-4054-9369-a47deb6f52f2)

When you stop overclock, the temperature goes back down.

### Other changes and fixes

Concealed weapon bay now doesn't show up when you examine the mech, so
it's actually concealed now.

New radio module can properly change its frequency, as it didn't work
for previous radio.

Launcher type weapons were ignoring cooldowns and power usage, so you
could spam explosive banana peals, while they should have a 2 second
cooldown:
<img alt="q5GjUsHwGr"
src="https://github.com/tgstation/tgstation/assets/3625094/d102725d-e9e1-4588-9d6c-b9e38b7a6535">

Now this is fixed and all launcher type weapons properly use power and
have their cooldowns working.
And now they have the kickback effect working (when it pushes you in the
opposite direction in zero gravity on throw).

Thermoregulator now heats/cools considering heat capacity instead of
adding/reducing flat 10 degrees. So you can heat up cabin air quicker if
the pressure is low.

There were some other sloppy mistakes in mech code, like some functions
returning too early, blocking other functionality unintentionally. Fixed
these and made some other minor changes and improvements.

## Changelog

:cl:
refactor: Refactored Mech UI
refactor: Refactored mech radio into a utility module, adding extra slot
to all mechs
refactor: Refactored mech air tank into a utility module with an air
pump, adding extra slot to all mechs
refactor: Refactored mech cabin air - there is now a button to seal or
unseal cabin to make it airtight or exchanging gases with the
environment
refactor: Removed mech maintenance UI Access is set in mech UI, and
parts are ejected with a crowbar
add: Mech now has wires and can be hacked
qol: Roboticists now can see MOD suit and mech wires
add: Mechs now require servo motor stock part and it affects movement
power usage instead of scanning module
add: Scanning module absence doesnt block mech movement and hides some
UI data instead. Big Bess starts without one.
qol: Hitting mech with ID card now toggles ID lock on/off if the card
has required access
fix: Fixed concealed weapon bay not being concealed on mech examine
fix: Fixed mech radio not changing frequency
fix: Fixed mech launcher type weapons ignoring specified cooldown
fix: Fixed mech launcher type weapons not using specified power amount
fix: Fixed mech temperature regulator ignoring gas heat capacity
fix: Fixed mech stopping processing other things while not heating
internal air
fix: Fixed mech being able to leave transit tube in transit
fix: Fixed mech internal damage flags working incorrectly
fix: Fixed Gygax leg overloading being useless
fix: Fixed mechs ignoring their stock parts on creation. Syndicate mechs
now stronger against lasers and consume less energy on move. Upgrading
from tier 1 to tier 2 doesn't make mech consume MORE energy than before
the upgrade.
balance: Rebalanced mech energy drain with part upgrades. Base energy
drain reduced by 50%, 33%, 25% with upgrades and applies to movement
(Servo rating), phasing, punching, light (Capacitor rating).
balance: Hydraulic clamp now can force open airlocks
balance: Made mech RCS pack consume reasonable amount of gas
code: Fixed some other minor bugs and made some minor changes in the
mech code
/:cl:

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [wangbinyq/Mind-Expanding-Books](https://github.com/wangbinyq/Mind-Expanding-Books)@[4e8712a154...](https://github.com/wangbinyq/Mind-Expanding-Books/commit/4e8712a154e98ffdf23093b46d770fa20fc3bca6)
#### Wednesday 2023-08-30 21:00:03 by bschlagel

Added "Pilgrim at Tinker Creek"

Really wonderful book about nature, the passage of time, and really paying attention to the world around you. The whole book could almost be categorized as prose poetry; it's not a large volume but took me a while to get through just due to the sheer density of lush and sensitive description. It chronicles a year in which both nothing and everything seems to happen; Dillard mostly hangs out around her home and its backyard creek (or at least, the book is constrained mostly to these experiences) but manages to evoke transcendent beauty and spirituality, capturing cycles of predator and prey, weather, and her own reactions to the unfolding of life in its infinite forms.

---
## [wangbinyq/Mind-Expanding-Books](https://github.com/wangbinyq/Mind-Expanding-Books)@[4d0e21a999...](https://github.com/wangbinyq/Mind-Expanding-Books/commit/4d0e21a99952ca434acec05b346ef75ce2147bd9)
#### Wednesday 2023-08-30 21:00:03 by bschlagel

Add Bolo'bolo

* Added "Bolo'bolo"

Weird and wonderful little book that proposes a whole societal structure of radical autonomous communities — complete with an invented language to describe the parts of this new community vision, and their machinations. Very eye-opening; in some ways it's a strange and impractical utopian dream; in others it's a sobering and critical plea for reorganizing society along lines of greater sustainability and social cohesion. Very interesting whichever way you look at it!

---
## [wangbinyq/Mind-Expanding-Books](https://github.com/wangbinyq/Mind-Expanding-Books)@[46feb27687...](https://github.com/wangbinyq/Mind-Expanding-Books/commit/46feb27687f389f8d6246e7fbd9858b7a9d183f7)
#### Wednesday 2023-08-30 21:00:03 by bschlagel

Added "Le Ton beau de Marot" (#150)

An incredible book about the art of translation, and a million other very welcome tangents. Hofstadter spins endless threads of ideas around a fascinating central premise: that a specific favorite poem of his, by a fairly obscure 16th century French poet, can spark an infinite variety of translations. There are 80+ of these translations sprinkled throughout the book, from friends and family, students and colleagues, noted translators and computer programs (and many by Hofstadter himself). Among them, a feast of academic lessons and personal reflections interwoven into a testament to the complexity and magic of translation and a whole lot of fascinating problems posed by language, literature, cognition and more. I've owned Hofstadter's infamous Gödel, Escher, Bach for a few years now, and still haven't finished swashbuckling my way through it — but I found this one thematically related yet more accessible, a great entrance point to a capacious and curious mind.

---
## [TheUnholyWrath/oaa](https://github.com/TheUnholyWrath/oaa)@[dfd37e4cec...](https://github.com/TheUnholyWrath/oaa/commit/dfd37e4cec57fca863fee0f25abf5da0b2be213a)
#### Wednesday 2023-08-30 22:16:46 by Darko V

Updated some outdated item builds (#3535)

* Updated item builds/guides to 7.33d for:
Abaddon, Bane, Beastmaster, Brewmaster, Broodmother, Chen, Nightstalker. Clockwerk, Dark Seer, Dark Willow, Dazzle, Ember Spirit, Sohei, Luna, Medusa, Naga Siren, Outworld Devourer, Phantom Lancer, Puck, Queen of Pain, Storm Spirit, Techies, Underlord, Anti-Mage, Arc Warden, Axe, Batrider, Bristleback, Centaur Warruner, Chaos Knight, Windranger, Winter Wyvern, Lycan, Magnus, Marci, Mirana, Pangolier, Snapfire, Vengeful Spirit, Void Spirit, Spirit Breaker, Enigma, Lone Druid, Nyx Assassin, Phoenix, Sand King and Io.

* Removed Arcane Blink from all item builds/guides.

---
## [peff/git](https://github.com/peff/git)@[c508be9d59...](https://github.com/peff/git/commit/c508be9d59f2fa3d922fccbb216bfa9205270326)
#### Wednesday 2023-08-30 22:30:19 by Jeff King

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
## [BoopEnthusiast/LiDar-Game](https://github.com/BoopEnthusiast/LiDar-Game)@[5c86a5aa48...](https://github.com/BoopEnthusiast/LiDar-Game/commit/5c86a5aa4869d3ed50d6d0b4fe8f575cec3e37e6)
#### Wednesday 2023-08-30 22:52:36 by Boop

:shrug:

Yeah idk what this is fuck this shit though

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[fb4587b336...](https://github.com/tgstation/tgstation/commit/fb4587b3368ebb55e0cc10f8c650abcc26afa5d4)
#### Wednesday 2023-08-30 22:53:14 by san7890

Cursed Slot Machine Fixes (#77989)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

A lot of these were stuff I did in response to reviews but apparently
didn't test extremely thoroughly. My bad.

* The proc for checking if the machine is in use is split out into its
own thing for clarity, and for potential reuse.
* The signal is no longer fucked up so you can actually get more than
one curse out of the slot machine as intended.
* Admin heals (and admin heals only) can remove the status effect. This
is just in case someone fucks up a variable when running an event and
wants to quickly heal some people while they varedit it to actually be a
proper event.
* Some nice code stuff while I was there, we don't need to be
typecasting to human anymore so it's nice to fix that.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Fixes are good.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
fix: The Cursed Slot Machine should now actually give you more than one
pull.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[81246ff8f4...](https://github.com/c0ntradicti0n/dialectics/commit/81246ff8f4e839e7cab86acc214c933cdfd4c8d3)
#### Wednesday 2023-08-30 23:38:57 by Stefan Werner

Automated TOC Commit: 2/1/2/1/1/.Love.md 2/1/2/1/3/.Indifference.md 2/1/3/2/3/1/.Analysis.md 2/1/3/1/3/3/.Texture.md 2/1/2/2/3/.Smell.md 2/1/3/1/3/.Feeling.md 2/1/3/1/2/1/.Melody.md 2/1/2/2/3/1/.Fragrant.md 2/1/2/1/1/2/.Contempt.md 2/1/2/1/3/2/.Boredom.md 2/1/3/2/1/2/.Recollection.md 2/1/2/1/2/1/.Joy.md 2/1/3/2/.Cognition.md 2/1/2/2/.Sensations.md 2/1/2/1/2/3/.Neutrality.md 2/1/2/3/2/.Pessimism.md 2/1/2/1/2/.Hate.md 2/1/2/2/_Physical-Gustatory/Olfactory.md 2/1/3/1/.Perception.md 2/1/3/1/1/1/.Color.md 2/1/2/2/3/3/.Neutral.md 2/1/2/2/2/.Taste.md 2/1/3/3/_Instinct-Reflection.md 2/1/2/3/3/.Realism.md 2/1/2/2/3/2/.Stench.md 2/1/3/1/1/2/.Shade.md 2/1/3/3/2/.Insight.md 2/1/3/2/1/1/.Imagination.md 2/1/3/2/_Abstract-Concrete.md 2/1/2/1/2/2/.Despair.md 2/1/3/_Aware-Unaware.md 2/1/3/2/2/2/.Long-Term.md 2/1/3/1/2/.Hearing.md 2/1/2/2/1/3/.Tapping.md 2/1/2/3/1/.Optimism.md 2/1/2/2/1/1/.Stroking.md 2/1/3/2/2/1/.Short-Term.md 2/1/3/2/3/3/.Evaluation.md 2/1/3/1/2/3/.Harmony.md 2/1/2/2/2/1/.Sweet.md 2/1/3/2/3/2/.Synthesis.md 2/1/2/1/1/1/.Compassion.md 2/1/3/3/3/.Forethought.md 2/1/2/1/3/1/.Interest.md 2/1/2/1/_Affection-Aversion.md 2/1/2/2/2/3/.Sour.md 2/1/3/1/1/.Seeing.md 2/1/2/1/3/_Engagement-Disengagement.md 2/1/3/1/3/2/.Roughness.md 2/1/3/3/.Intuition.md 2/1/3/1/3/_Smooth-Jagged.md 2/1/2/2/1/2/.Hitting.md 2/1/3/1/3/1/.Softness.md 2/1/3/1/1/3/.Brightness.md 2/1/3/2/2/.Memory.md 2/1/3/1/2/2/.Rhythm.md Feeling.md" 2/1/2/1/.Emotions.md 2/1/2/2/2/2/.Bitter.md 2/1/3/2/3/_Break-Combine/Assess.md 2/1/2/1/3/3/.Distraction.md 2/1/2/2/1/.Touch.md 2/1/2/1/1/3/.Apathy.md 2/1/3/1/_Visual-Auditory/Tactile.md 2/1/2/3/_Positive-Negative.md 2/1/3/2/1/3/.Decision.md 2/1/3/2/3/.Judgment.md 2/1/2/_Pleasure-Pain.md 2/1/3/2/1/.Thought.md 2/1/2/3/.Moods.md 2/1/2/2/3/_Attractive-Repulsive.md 2/1/3/2/2/3/.Reflexive.md

---

