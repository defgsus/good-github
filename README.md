## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-08](docs/good-messages/2023/2023-04-08.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,874,657 were push events containing 2,623,496 commit messages that amount to 155,227,767 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 67 messages:


## [cortex-command-community/Cortex-Command-Community-Project-Source](https://github.com/cortex-command-community/Cortex-Command-Community-Project-Source)@[bfb278c026...](https://github.com/cortex-command-community/Cortex-Command-Community-Project-Source/commit/bfb278c0267f2b7a177d9bb0063ef3145f9f625b)
#### Saturday 2023-04-08 00:23:32 by MaximDude

VS2019 is being super stupid about C++20 so we gotta do some conditional hacking to not deprecate it

Increase precompiled header memory allocation limit from default 75mb to 225mb otherwise it shits itself trying to build the pch for reasons unknown to (this) man
Compile everything Lua with C++17 - can't really find a solution for this, it shits itself from Boost garbage via LuaBind the same way it does if enabling pch or conformance in these CUs and I just don't wanna deal with those piles of shit
Complementary AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

---
## [AngelCantugr/gate](https://github.com/AngelCantugr/gate)@[e2a108db75...](https://github.com/AngelCantugr/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Saturday 2023-04-08 00:31:07 by Chris Phillips

fix(authn/oauth2): prevent oauth2 redirect loops (#1517)

During setup of spinnaker authentication with oauth2 a common hurdle is a redirect loop.

For example:

https://github.com/spinnaker/spinnaker/issues/5794
https://github.com/spinnaker/spinnaker/issues/1630

Also, many threads in Slack discuss these problems. In fact this appears to be a common
pitfall for the spring-security-oauth2-autoconfigure library in general. A light refresher
on the ouath2 flow in play here seems worthwhile. The user is redirected from `/login` in gate
to the external auth provider (google, github, etc.) and after successfully authenticating
they are redirected back to the gate `/login` endpoint but this time with a code parameter
that is to be used to request an access token.

This request can fail for a variety of reasons, and if it does, the underlying spring library
triggers a redirect to the `/error` endpoint. What causes the redirect loop for gate in particular
(and for other users of the library in a similar fashion) is that the WebSecurityConfigurerAdapter
in play is treating `/error` as an authenticated path and so instead of just returning with a 401,
it re-redirects to `/login` and the redirect loop continues.

My thought is that instead of a redirect loop, simply allowing the 401 to be returned will be a stronger
more helpful signal as to what is going on. Hopefully it will save future first-time installers headaches.

Spinnaker docs have included several troubleshooting hints and tips for how where you terminate SSL
affects configuration etc. Even after following all of these and lots of spelunking through spinnaker
github issues and combing over threads in slack, I found myself still experiencing a redirect loop even
though I had applied all the combined wisdom that was applicable to my setup.

As it turns out, I had a bad copy/paste of my client secret in my configuration. So the request
to turn the code from google into an access token from google was failing with a 401. After much
debugging and deep diving into the spring security code I found that had I turned on DEBUG in gate
for these classes in gate-local.yml:

```
logging:
  level:
    org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler: DEBUG
    org.springframework.security.oauth2.client.filter.OAuth2ClientAuthenticationProcessingFilter: DEBUG
```

Then I would have seen in the logs that a 401 response was returned from google and perhaps it would have
caused me to look closer at my botched client secret configuration. I think perhaps we don't want to require
that all operators of spinnaker become spring-security-oauth2 experts. So I'm proposing adding `/error` to
the list of paths in gate that aren't treated as authenticated. Thus short-circuiting the redirect loop and
bringing to light helpful troubleshooting info that was previously more or less swallowed.

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[c3b78761d2...](https://github.com/necromanceranne/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Saturday 2023-04-08 00:32:00 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[b5ebf5c942...](https://github.com/necromanceranne/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Saturday 2023-04-08 00:32:00 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[11cbbba018...](https://github.com/Donglesplonge/tgstation/commit/11cbbba018e861237ce4bed73f19b58874c22042)
#### Saturday 2023-04-08 00:52:54 by Sol N

Replaceable Traitor Uplinks (#74315)

## About The Pull Request

Following [from the suggestion in this hackmd
](https://hackmd.io/IkDWWkpfQa2lkdevsnLqhA?view#Replacement-Uplinks)with
a few twists of my own, I have made a method for traitors to acquire a
replacement traitor uplink that has its own set of flaws and limiters in
order to prevent abuse.


![ZC0WYDFRzc](https://user-images.githubusercontent.com/116288367/228101432-9352390b-9538-4c62-8dc4-55e2e798c466.png)

The basic pitch is as follows, all traitors now start with a new,
crafting recipe exclusive to them, it costs a teleport beacon, a
bluespace crystal, and some iron and cable coil, and then allows them to
build a static, dense machine that they can synchronize with, which
allows the machine to know what signal it should be looking out for from
the traitor.

![dreamseeker_iErI3vju0C](https://user-images.githubusercontent.com/116288367/228094286-c2bca198-82cd-4ce0-a4a7-c26c24a9327c.gif)

The traitor then uses any radio, sets it to the frequency that has been
added to their static antagonist ui, and then speaks their codeword,
also in the ui, and then a few things happen.

![dreamseeker_gbzSFeHuS5](https://user-images.githubusercontent.com/116288367/228094354-a649c713-f013-4ac2-b8d7-0754a852f987.gif)

Most obviously, they get a replacement uplink that is in the conspicuous
shape of the nukie or lone op uplink. This uplink can be unlocked by
speaking your replacement codeword to it again, it remembers your
previous TC amount and locks all other uplinks associated with your
uplink handler(they can then be unlocked as normal). It also destroys
any other replacement uplinks associated with your uplink handler, which
means you can never have more than one replacement uplink.

This means that if your uplink has been confiscated and you left it
unlocked, if it hasn't been emptied out you can continue from where you
were, and if you want to get back on the TC grind you won't lose the new
TC to whoever stole your uplink. Of course, the new uplink can not be
locked, so you have to be more careful with it or buy an uplink implant
and destroy it. You can destroy your replacement uplink with a
screwdriver right click, same for the machine.

Additionally, the Syndicate Uplink Beacon has another quirk to it, which
is that the teleporter beacon used to create it is intact, which means
people eagle eyed on the teleporter console could go find you, not to
mention that if you use an existing teleporter beacon, someone might
notice its gone missing...

oh also while making the replacement uplink i found a bug caused by a
recent pr that broke debug uplinks due to them not having a purchase
log. thats fixed too

## Why It's Good For The Game

It can be easy to lose your uplink, and as a traitor having your uplink
confiscated, even if it is locked, feels really bad. While the old
traitor objectives were added back to prog traitor to prevent situations
where a confiscated uplink meant that you were completely aimless, I
think that having a backup solution would be good for more inexperienced
traitors or for ones who get unlucky.

Hopefully this is generally balanced well enough but there are a few
levers that can be pulled, but overall I do think that making it so that
traitors can always get a chance to get an uplink and do some objectives
is good for the game. I like the idea of someone getting perma'd,
someone breaks them out, they both craft a new uplink beacon, and then
they go back and get the traitors old gear with stuff they got from the
new uplink, I think that's a cool possibility to throw into the sandbox.

## Changelog
:cl:
add: Added new syndicate uplink beacon and associated systems that allow
you to get a replacement traitor uplink
fix: Debug & nukie uplinks no longer runtime and work properly again
/:cl:

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[00f8bcfe75...](https://github.com/Donglesplonge/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Saturday 2023-04-08 00:52:54 by MrMelbert

Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

## About The Pull Request

- Signallizes head revolutionary flash conversion code, moving it out of
core flash code.
- Removes "tacticool" flashing from head revs, but they can still
convert from any direction
 
- Fixes April Fools "You son of a bitch! I'm in" force say never
working.
   - Revs are muted on conversion so they couldn't talk.
       - Fixed by only muting revs on non-holidays
   - Cultists are unconscious on conversion so they couldn't talk
       - Fixed by only unconscious-ing cultists on non-holidays
- Brainwash victims are more often than not unconscious / asleep so they
couldn't talk
       - Just left this one. 

- Reduced the chance of them occurring and limits it to April Fools only
- A 1% chance of the force says ocurring means they will happen pretty
much once a week, given multiple rev / cult rounds happen every week and
on average like, 20 people are converted. A little absurd, it's good
that it never worked?

## Why It's Good For The Game

Antag code in core item code is bad

It's funny this meme has existed for like 2, 3 years now? No one's
tested it, it's never worked

## Changelog

:cl: Melbert
refactor: Removes Rev code from core flash code
fix: Getting converted on April Fools now triggers the meme force say as
always intended
del: The meme force say can no longer trigger on any day (it didn't work
before anyways)
/:cl:

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[e65dff59bd...](https://github.com/timothymtorres/tgstation/commit/e65dff59bd47f5805e8b33f623f02cd1700d22ec)
#### Saturday 2023-04-08 00:53:47 by zxaber

Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs (#74225)

## About The Pull Request
Reduces the price of the Doomsday equipment by 20 PT for each APC hacked
in a Head of Staff office, as well as the Vault.
## Why It's Good For The Game
See #71404 for the prior PR and my full reasoning.

Long-story short, activating the Doomsday before having a plan in place
is suicide, and it takes 13 APCs to unlock. Since there are few well
hidden APCs in general, you'll usually be gathering APCs after going
loud (such as with a borg machine). 13 APCs is 13 minutes, and by the
time you've gathered your malfbux, you're either already dead or have
already taken full control.

I had intended to give Doomsday a flat 70 PT price, but concerns were
raised that an AI could conceivably hack only APCs on their sat (and
perhaps one on the Lavaland outpost) and Doomsday without ever really
touching the station*. So a compromise was proposed, we instead give the
AI discounts by hacking Head of Staff areas, and the Vault, which are
usually situated in well-traveled areas, and also have some fluff
reasoning.

*I still think it'd be suicide to do this, but it's not a hill I want to
die on.
## Changelog
:cl:
balance: Malf AIs that hack Head of Staff and Vault APCs will now find a
discount issued on Doomsday.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[dc2f52e386...](https://github.com/timothymtorres/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Saturday 2023-04-08 00:53:47 by tralezab

Blink is no longer a forbidden school spell?? (#74487)

## About The Pull Request

Turns blink's school from forbidden to translocation. This has some
incredibly minor changes nobody is going to notice:
- Changes the blink's invocations when mixed with a CERTAIN spell
- If you were very specifically a chaplain with the holy crusade sect
and you casted blink, before it would excommunicate you, now it will
just smite you, as translocation spells are seen as less bad than
forbidden magic
- probably some more niche interactions but that's all I can remember

## Why It's Good For The Game

Guys, I know blink is a very annoying spell but come on now it's not
forbidden magic, that's for heretics and super duper evil stuffs

## Changelog
:cl:
fix: blink is now a translocation spell
/:cl:

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[48183ec0ff...](https://github.com/timothymtorres/tgstation/commit/48183ec0ffd67ea5afa26c6f6e58e81edff98d52)
#### Saturday 2023-04-08 00:53:47 by san7890

Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[9dfe00d79d...](https://github.com/timothymtorres/tgstation/commit/9dfe00d79dd7bd540442ce825caa4e964c619b46)
#### Saturday 2023-04-08 00:53:47 by san7890

IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request


![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

---
## [vlggms/lobotomy-corp13](https://github.com/vlggms/lobotomy-corp13)@[928b2420d9...](https://github.com/vlggms/lobotomy-corp13/commit/928b2420d906fbdef89ce27d75db5afe713b147d)
#### Saturday 2023-04-08 00:54:58 by Lance

Servant of Wrath

Records and Instability

Dash speed up

Fuck you I'll space indent all I like

There was some fuckin lint in this PR

God damned there's a lot of lint in here

Faction Check

Sprite update, minor bug fixes

Floating and Gun and Acid

Minor Records

Small update

Unnerfs resists

AoE hit fix

Gun update real

more res should mean less talk

Pixel Fix

Sound... Fix?

Broke the staff's legs, fuck those guys.

lmfao audio pains

Gun Rename, Spawn nerf

NO MORE FRIENDS FROM GUN

Faction change

acid tweak

LINT!

SW Code and Balance

SoW Temp commit

Scuff-Fix

SoW bonk update

Hermit range increase and ranged damage decrease

visual fix

Ending adjustments

I forgot to carry the 4

Visual indicator

minor fixes

Instability Tweaks

Paperwork Update

Anti-Self-Burn

Ending Update

Right view

A check that should be a non-issue but i'm making sure!

Breach Update and EGO update

More goo and FEMALE

Improvement and new Icons

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[8ab74525c1...](https://github.com/FernandoJ8/tgstation/commit/8ab74525c1c3c09a7605fead3ab013d29f24d07f)
#### Saturday 2023-04-08 01:06:19 by itseasytosee

Brings the monkey back down (body horror edition/addition.) (#73325)

## About The Pull Request
Let me paint you a story.
A long time ago monkeys once rested their feet on the floor, this was a
time of bliss and peace. But sometime around the horrors of making
monkeys subtypes of humans did an atrocity occur.

![image](https://user-images.githubusercontent.com/55666666/217657059-5c960ab4-c3de-493c-ac12-28de99b43d7f.png)
**The monkeys were moved up.**
I thought this was bad, and alot of people on the forum tended to agree
with me

![image](https://user-images.githubusercontent.com/55666666/217657707-120354c7-b1a5-4d93-8813-8e10e142bd92.png)
This was do to some purpose of adjusting them so it could be easier to
fit item sprites onto them instead of preforming the hours of work
refractoring to make the heights of the items dynamic and adjustable. A
simple pixel shift may have sufficed, but you see, such a change would
NEVER allow the frankensteining of monkey and human features together.
This is that refractor.

In essence, the following is now true.
A top_offset can now be generated for a human based on a varible on
their chest and legs. By default, and as is true with human legs and
chests, this variable is ZERO by default. Monkey legs and chest have
NEGATIVE values proportionate and onto how much smaller their sprite is
compared to humans. Other bodyparts, as well as any other accociated
overlays, or clothing will automatically be offset to this axis. THIS
MEANS THAT MONKEYS ARE ON THE FLOOR. But is means something else too.
Something more freakish,


![image](https://user-images.githubusercontent.com/55666666/217659439-bc0b1a35-76c8-4490-b869-770180605822.png)
**What abominable monsters**, unreachable by players as long as we can't
stitch monkeys and humans together (oh but just wait until the feature
freeze ends)
Oh but you might be thinking, if legs can make a mob go down.
can it make a mob

**go**
**up??**

**OH NO**


![image](https://user-images.githubusercontent.com/55666666/217707042-0d53022f-d93a-4262-a5ce-ef15a99eb897.png)

![image](https://user-images.githubusercontent.com/55666666/217707060-779f5901-ab90-4a64-9ca7-0b147e24f099.png)

![image](https://user-images.githubusercontent.com/55666666/217707821-23d7457c-5881-40ae-8d9d-c9fbd645aba6.png)

These lads are stepping, and have been implemented solely for proof of
concept as a way to flex the system I have created and remain
inaccessible without admin intervention.

But really, when all is said and done, all this PR does in terms of
player facing changes is move the monkey back down.

![image](https://user-images.githubusercontent.com/55666666/217708365-b6922a6d-08d0-4267-8713-4f8dac29038e.png)
Oh and fixed monkey husked which have been broken for who knows how
long.

![image](https://user-images.githubusercontent.com/55666666/217708464-5a9b6f89-4223-4ae5-a21e-3a274a9f8db8.png)
## Why It's Good For The Game
The monkey is restored to its original position. Tools now exist to have
legs and torsos of varying heights. Monkey Husking is fixed.
## Changelog
:cl: itseasytosee
fix: Monkeys ues the proper husk sprites.
imageadd: The monkey has been moved back down to its lower, more
submissive position.
refactor: Your bodyparts are now dynamically rendered at a height
relevant to the length of your legs and torso, what does this mean for
you? Not much to be honest, but you might see a monkey pop up a bit if
you cut its legs off.
admin: The Tallboy is here
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[c267799416...](https://github.com/Paxilmaniac/Skyrat-tg/commit/c2677994169b54a2b3358ccd59d4dfd6df826322)
#### Saturday 2023-04-08 01:08:06 by SkyratBot

[MIRROR] Chasm Hell On Icebox - 300 Active Turfs on Prod Moment [MDB IGNORE] (#20260)

* Chasm Hell On Icebox - 300 Active Turfs on Prod Moment (#74410)

## About The Pull Request

Spontaneous regressions introduced by #74359
(1e58c1875d9e2f48a306fe31a0626dbbb1990ff9).
```txt
 - Z-Level 2 has 150 active turf(s).
 - Z-Level 3 has 150 active turf(s).
 - Z-Level trait Ice Ruins Underground has 300 active turf(s).
 - Z-Level trait Mining has 300 active turf(s).
 - Z-Level trait Station has 300 active turf(s).
 - End of active turf list.
 ```

![image](https://user-images.githubusercontent.com/34697715/229213138-5a6a7a4f-edec-47ab-8def-ee4e4bddfe61.png)

Basically the lavaland ruin sucks dogshit and I had to do a lot of stuff to account for everything failing. There was even a moment where we were adding something to `flags_1` instead of `turf_flags` and that was also really bad to figure out.

![image](https://user-images.githubusercontent.com/34697715/229213428-63bb1f6e-6f88-4604-a3c6-e08e20cbfa7a.png)

i also had to add orange genturfs because it was really getting bad with all of the assertions we had to keep making, especially since stuff like this could also show up:

![image](https://user-images.githubusercontent.com/34697715/229213562-4a145453-5f90-4d05-b8cc-5c1beec2b0dd.png)

That's the prison in the red box, those are active turfs because a chasm scraped it away.

Sorry if this is hard to follow but I promise you everything in this is essential. I wish we didn't have to rely on turf flags as much as we do but this is a fix PR, not a refactor.
## Why It's Good For The Game

Even one active turf on IceBox ate up _three_ seconds of SSair's initialization every single time it was really fucking bad.

We haven't had to deal with chasms for about two years so there's a lot of mapping assertions we made since they just weren't a thing, but now they're back so lets do it properly.
## Changelog
:cl:
fix: The prison on IceBox should no longer leak air as often.
/:cl:

I have compiled this map about 30 times until active turfs stopped fucking happening and now I am content. This likely doesn't fix _everything_ because some stuff can still be hidden to me, and we still have PRs that need to be merged to reduce the amount of noise we're getting on prod.

* Chasm Hell On Icebox - 300 Active Turfs on Prod Moment

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[a3451b7fe4...](https://github.com/BlueMemesauce/tgstation/commit/a3451b7fe4ff60e0cb6cc4f2bd6d20543f455940)
#### Saturday 2023-04-08 01:09:28 by san7890

Makes "forced" opening and closing of doors way more sane (#73699)

## About The Pull Request

The gist is that people thought that this was a boolean value, which was
fucked up. It's not a boolean value, it accepts anything between 0 and
2. So, let's re-arrange the checks and framework, give it some
descriptive defines, just so people know what the fuck "2" actually
does. `DOOR_DEFAULT_CHECKS` (0) does stuff normally,
`DOOR_FORCED_CHECKS` 1 typically just checking if we aren't emagged shut
or something (i suppose it could happen), and `DOOR_BYPASS_CHECKS` (2)
means that we just get the fucking door open if it isn't physically
sealed shut/open somehow.

I don't know if `forced` has ever _been_ a boolean, but for some reason
people thought it was.

I also enforced boolean returns instead of passing back null. This did
not matter for close() but i think it's silly to have a TRUE/null
dichotomy so that was also touched up.
## Why It's Good For The Game

Much better to read, less confusing, less stupid. It's been irritating
me for a while now, so let's just implement it now. Had to make a few
awkward concessions in order to fit this into the current code
framework, but it should be a lot nicer. I also shuffled the order of
some code around because certain placements didn't make any sense (early
returns not being in the right spot for an early return).
## Changelog
Nothing that should concern players.

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[db7534d6da...](https://github.com/BlueMemesauce/tgstation/commit/db7534d6dabf0127c87b291eae4063b6f77d36e4)
#### Saturday 2023-04-08 01:09:28 by LemonInTheDark

Lowers nightvision threshold to work for mesons, fixes not being able to examine stuff lit by overlay lights (#73712)

## About The Pull Request

Might be a bit low, but part of that is because it's kinda bad at
figuring color, rgb isn't really balanced in that respect

Fixes not being able to see stuff under the light of a lamp

Overlay lights don't set lumen, which leads to stupid when you try and
check with ONLY it
It worked before because the mob has THEIR luminosity set, which then
"glowed" out

That doesn't work here cause yaknow I removed our uses of byond lighting
(except for errant view() calls) so this is the best I've got

## Why It's Good For The Game

Closes #73548 

## Changelog
:cl:
fix: Examining in the dark is less wonk now, sorry bout that
/:cl:

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[fe7ebd67cf...](https://github.com/Paxilmaniac/tgstation/commit/fe7ebd67cf74982038524ceb175377d7ff6c0486)
#### Saturday 2023-04-08 01:10:39 by LemonInTheDark

Properly accounts for byond tick fuckery in runechat code (#74388)

## About The Pull Request

Ok so like, the agreed upon assumption for "verb like code" (stuff that
triggers when a client sents a network packet to the server), is it runs
in verb time, that sliver of time between maptick and the start of the
next tick.
We thought MeasureText worked like this. It doesn't.

It will, occasionally, resume not during verb time but as a sleeping
proc, at the start of the next tick.
Before the MC has started working.
This appears to only happen when the tick is already overloaded.

Unfortunately, it doesn't invoke after all sleeping procs as we were
lead to believe, but just like, like any sleeping proc.

This means it fights with the mc for cpu time, and doesn't respect the
TICK_CHECK macro we use to ensure this situation doesn't happen.

SOOO lets use a var off the MC instead, tracking when it last fired.
We can use this in companion with TICK_CHECK to ensure verbs schedule
properly if they invoke before the MC runs.

Hopefully this should fix 0 cpu when running at highpop

Thanks to Kylerace and MrStonedOne for suffering together with me on
this, I hate this engine.

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[c18b1ef442...](https://github.com/Paxilmaniac/tgstation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Saturday 2023-04-08 01:10:39 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [Enbyy/orbstation](https://github.com/Enbyy/orbstation)@[b3e5642d94...](https://github.com/Enbyy/orbstation/commit/b3e5642d94caab455bea8b71e244081249cb2924)
#### Saturday 2023-04-08 01:11:19 by san7890

Fixes Active Turf Scenario on Tramstation (#74354)

## About The Pull Request

On the tin. Basically whenever `atmoscilower_2.dmm` would invoked
`atmoscilower_attachment_a_2.dmm`, it would trigger an active turf in
this location since it doesn't have a "ceiling". (as well as there being
an "aired" turf mingling with airless turfs)

This caused the following report:
```txt
 - All that follows is a turf with an active air difference at roundstart. To clear this, make sure that all of the turfs listed below are connected to a turf with the same air contents.
 - In an ideal world, this list should have enough information to help you locate the active turf(s) in question. Unfortunately, this might not be an ideal world.
 - If the round is still ongoing, you can use the "Mapping -> Show roundstart AT list" verb to see exactly what active turfs were detected. Otherwise, good luck.
 - Active turf: Station Asteroid (163,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (163,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (164,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (164,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,80,2) (/area/station/asteroid). Turf type: /turf/open/misc/asteroid/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (166,81,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,83,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/iron/smooth. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,83,3) (/area/station/asteroid). Turf type: /turf/open/openspace/airless. Relevant Z-Trait(s): Station.
 - Z-Level 2 has 8 active turf(s).
 - Z-Level 3 has 1 active turf(s).
 - Z-Level trait Station has 9 active turf(s).
 - End of active turf list.
```

This is what it looked like when it was reproduced on my machine:


![image](https://user-images.githubusercontent.com/34697715/228689991-d9cc87c3-f931-4513-8399-928c93def605.png)


Surprisingly not that hard to debug, albeit tedious. At least I know
that this was the issue with 100% confidence.
## Why It's Good For The Game

Ate up 0.1 seconds of init on my machine. That's silly.
## Changelog
No way players care

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[09e95cdfbc...](https://github.com/shiptest-ss13/Shiptest/commit/09e95cdfbc8337b5b7a84a088c32b458ee1d996d)
#### Saturday 2023-04-08 01:15:32 by Bjarl

Saloon rework (#1594)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Expands whitesands_surface_camp_saloon to cover a 30x30 footprint and
not be nearly as bad. The previous version had some really glaring
design flaws, like holes in the wall for a bar. On a planet with a
deadly atmosphere. Yeah. Also all the chairs faced the same direction.
![2022 10 31-11 32
50](https://user-images.githubusercontent.com/94164348/199083356-5fabd2c8-0298-4a31-a830-b63dbcd2737f.png)
You can see how it looks. It's not great. 
Here's the new version
![2022 10 31-11 36
20](https://user-images.githubusercontent.com/94164348/199083924-9537beb7-0c74-4c57-9422-60fe953ae0bc.png)
![2022 10 31-11 36
25](https://user-images.githubusercontent.com/94164348/199084468-32d94ec8-846f-42e7-ae33-dc0b52e8b9b8.png)

![dreamseeker_ePSrp5zNFp](https://user-images.githubusercontent.com/94164348/199085448-24879745-650f-4bdc-9b0c-f1d9706ab865.png)
Ignore the patches of error, it's purple grass and doesn't display the
icon in sdmm for some reason.

The major changes are:
Expanding the building's footprint out to 30x30
Moving the loot behind the building, but locking it behind a shovel of
some sort (of which you can go through the ruin to get).
Improving the loot a LITTLE

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] The map loads although I still haven't managed to get it to load
on the proper planet with the spawning verb

## Why It's Good For The Game
The old version was kinda bad. Between the clown and mime masks out
front. The small footprint, and the free guns (also out front). This
solves those issues kinda while making it bigger.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Camp_Saloon has been expanded, expect frontier luxuries if you find
it!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[c21670412d...](https://github.com/shiptest-ss13/Shiptest/commit/c21670412dff10f4a3a1b1ab1e72f53294581d25)
#### Saturday 2023-04-08 01:15:32 by Bjarl

New Ruin: The Beach Town (#1572)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a new beach ruin, the abandoned beachside town
![2022 10 10-18 20
10](https://user-images.githubusercontent.com/94164348/194977185-0f35d08e-64c1-459d-94b2-ec6b66137753.png)
![2022 10 10-18 20
00](https://user-images.githubusercontent.com/94164348/194977192-0b93346e-cea0-4fb2-8b66-5ae7319ec3f1.png)

![dreamseeker_Ht2YcvyQbH](https://user-images.githubusercontent.com/94164348/194977254-d0b25aba-ec6b-4e8b-bad5-949a9961cf07.png)

![dreamseeker_KAB6kPSLrP](https://user-images.githubusercontent.com/94164348/194977259-561f8d97-962e-4545-a4b7-1637ad1a7156.png)

![dreamseeker_8Xe7Cuq6NH](https://user-images.githubusercontent.com/94164348/194977262-fb125315-2508-4022-9eda-5ed5078442c9.png)

![dreamseeker_SKJXeK9SOt](https://user-images.githubusercontent.com/94164348/194977268-b4efcd99-0896-4209-8b83-c61c086bda65.png)

![dreamseeker_6Ak0bNoVe5](https://user-images.githubusercontent.com/94164348/194977270-367aaf92-5d6d-4cd8-9827-eba99ec92080.png)

The town is an mostly empty place formerly devoted to tourism and the
beloved art of "chilling out". Facets of the life of its inhabitants
before their disappearance included drinking, grilling, and swimming off
the coast of their fairly large beach. Many interesting things happened
on the boardwalk, and a landing pad was present to allow for small ships
to dock inside the town.

The loot list is sparse here. I intend for this to mostly be a setpiece
for roleplay instead of a loot pinata. There's a good selection of
hydroponics seeds and gear, 2 full bar kits, basic kitchen equipment, an
autolathe, a few PDAs, a lotta wood, and a jukebox. Also donuts.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] Ruin spawns, nothing is out of whack that shouldn't be.

## Why It's Good For The Game
Continues the trend of making planets more good by adding more content
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An oddly empty town has been spotted on beach planets in the area.
Check it out spacers.
add: Random donut spawners, never eat the same donut two days in a row!

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [DaMoyai/oldcord](https://github.com/DaMoyai/oldcord)@[54566e454e...](https://github.com/DaMoyai/oldcord/commit/54566e454e98e20ff6bc9c54fc7c818bbe3ad4fc)
#### Saturday 2023-04-08 01:16:26 by DaSussy

make colors accesibility compatible, improve "delete, boost" button

yeah this fucking sucks when editing but its kinda needed

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6085e3b5ee...](https://github.com/tgstation/tgstation/commit/6085e3b5eed0f4954d2ba25549c919653207611d)
#### Saturday 2023-04-08 01:42:51 by MrMelbert

Reagent soup / Soup rework / Stoves - A kitchen expansion (#74205)

## About The Pull Request


![image](https://user-images.githubusercontent.com/51863163/227391708-8de28b68-149f-4e02-a2d3-22f6e3067784.png)

**This PR:** 

- Reworks most* existing soup into reagents. 

- Adds Stoves and Ranges. Ranges replace most* existing ovens. 

- Adds soup pots, to cook soup

**How does it work?** 

In the kitchen you will find a stove now.

Stoves act as a "reagent container heater", essentially a chem heater.
You can set a pot onto the stove.

To make soup, visit the cooking recipe book for a guide. Most recipes
are the same as before, just tweaked slightly - Add water to the pot (50
units for 1 batch generally), then add all the corresponding ingredients
to the pot. Set the pot out on the stove and right click it to turn it
on. If the recipe's correct, shortly it will start to mix and give you
soup!

One soup recipe will give you roughly 3 servings of soup. You can pour
our the soup into a bowl using a ladle or just by pouring it manually.

Of note: **All of the reagent contents of the ingredient are transferred
into the soup.** Better, more nutrient rich ingredients produces more
soup, and poisoned produce will pass it on.

If you place the soup into a chem master, you will notice it's roughly
half "soup reagent" and half a variety of reagents, including nutriments
/ proteins. This is your soup! It is recommended you serve your soup
with the reagents included, as they make up more nutrition for the
customer, however you can separate it out if you're picky.

**Todo:** 

- [x] Fill out the PR body a bit more 
- [x] Mapping (wait for big merge conflict pr to go past)
- [x] Soup colors
- [x] Balance pass over for soup recipes
- [x] TODOs
- [ ] Unit tests
- [x] Cullen Skink's recipe is invalid
- [x] Try to see if there's an easy way to prevent soup from fattening
you up too easy.

## Why it's good for the game

Adds some more depth to the kitchen and moves chef away from the
click-button-get-food style that exists.

Allows for inherently custom soups by the way of making it reagents, so
no need to support custom soup food items.

## Changelog

:cl: Melbert, stove and pot sprites by Kryson, ladle sprite by Kinneb
add: Kitchens are now stocked with Ranges. 
add: You can now print (and create) Stoves. 
add: The dinnerware vendor now dispenses ladles. 
add: Spoons can now actually spoon... things.
add: Soup has been reworked entirely. Soups are now reagents, cooked via
a soup pot on a Stove or Range. Simply add water and your required
items, then apply heat. Be careful not to boil over!
add: Stoves, Ranges, and Griddles will now heat up their surroundings -
don't turn them on around plasma!
fix: Fixes being able to cook in an Oven while the room is depowered
qol: Hitting a customer bot with an incorrect recipe no longer counts as
a hostile attack leading to your demise shortly after
refactor: Customer bots that request a reagent now use custom orders
code: Cut down a lot of code in the crafting menu code, and removes some
ugly ispaths
del: Soup is no longer food items, so can't appear in random food pools
(at least not yet).
balance: Virus Food recipe now requires you cool it to 200k.
/:cl:

---
## [Ziggypigster/SotnRandoTools](https://github.com/Ziggypigster/SotnRandoTools)@[4657e29d8e...](https://github.com/Ziggypigster/SotnRandoTools/commit/4657e29d8e3b03e3bdaf7baa829362e5f9b65182)
#### Saturday 2023-04-08 03:41:41 by Ziggypigster

1.1.7 Axe Armor Defense + Weapon Pass

April 1st - 7th 2023

-------------

1.1.7 Axe Armor Defense + Weapon Pass

|--Axe Armor--|
-Olrox Low Ceilings reworked for (mostly) consistent entry.
-Mist Gates reworked to reduce falling through the floor.
	Note: Mist Gates are still jank
	Reminder: Mist + Up modified to be infinite, regardless of MP / additional relics near mist gate rooms
-Holy Symbol: Defense +4 > Fireballs cost 4 less MP.
-Rib of Vlad: Defense +8 > Defense +5

|--Axe Armor Defense Changes--|
-Base Defense 3 > 0 (see Armor changes below)
-Armors in inventory now boost the axe armor defense as follows:
	+25: Gods Garb
	+20: Alucard Mail
	+18: Walk Armor (2nd Castle)
	+15: Diamond Mail, Mojo Mail
	+14: Dracula Tunic
	+13: Fury Plate
	+12: Spike breaker
	+11: Holy Mail
	+10: Platinum Mail
	 +9: Walk Armor (1st Castle)
	 +8: Gold Plate, Lightning Mail, Ice Mail, Dark Armor
	 +6: Silver Plate
	 +5: Steel Curiass
	 +4: Fire Mail, Healing Mail, Iron Cuirass
	 +3: Mirror Cuirass, Bronze Cuirass
	 +2: Hide Cuirass, Alucart Mail
	 +1: Cloth Tunic

|--Axe Armor Equipment--|
-Attacking mid-air with the following Thrust Weapons now builds speed and momentum:
	"Claymore"
	"Flamberge"
	"Estoc"
	"Zweihander"
	"Obsidian sword"
-Attacking with a thrust weapon now allows for repeated Gravity Jump chains.
-Sword Familiar: If boosted familiars are not on, damage is equal to player level.
	Note: This is currently restricted to a max of 49.
-Gurthang: Now granted +25 Damage for a short time after a Fireball is cast if held in main hand.
-Jewel sword: Now randomly grants jewels on kill.
	Drop Roll: 0-16. If 0, continue. Reduce max roll for every 20 LCK (min 2)
	Loot Roll: 0-199, check below resul
	0-99   : Zircon
	100-150 : Aquamarine
	151-190 : Turquoise
	191-194 : Onyx
	195-196 : Garnet
	197-198 : Opal
	199     : Diamond
-Hammer: When holding no subweapons, it is consumed to roll a random sub weapon.
	Restrictions: Only while walking/running/jumping/gliding
-Uncurse, Antivenom, Resist Stone now heals HP+MP+Hearts;
	Antivenom : 20
	Uncurse: 35;
	Resist Stone: 50;
-Ankh of Life now impacts Axe Armor Potion/High Potion/Uncurse/Antivenom/Resist Stone
-Bloodstone now heals when you use the following (effect does not stack):
	Big Fireball: 6HP
	Small Fireball: 4HP
	Faceplant: 1HP
-Talisman now reverts damage (stacks):
	Formula: Rolls 0-10. If 0, revert to previous higher HP. Reduce max roll for every 10 LCK (min 2)
-Healing Mail: HP recovery rate decreased

|--Axe Armor Bug Fix--|
-Giant fireballs now are properly resisted for Fire/Thunder.
-Now disables hold up / hold down when the user is using those actions during death to reduce (prevent?) death animation cancels.
-Fix Cross Subweapon loading wrong graphic for damage.

---
## [Jaden12194/peepoopoo](https://github.com/Jaden12194/peepoopoo)@[718ce1a7ef...](https://github.com/Jaden12194/peepoopoo/commit/718ce1a7efcee5ab0cce7515dff25a2adcf3b6a7)
#### Saturday 2023-04-08 03:53:27 by Jaden12194

Revert "Fuck you"

This reverts commit 36b8e1fbc96dd323026b9c63959ea64966a3153d.

---
## [Salzkorn/Archipelago](https://github.com/Salzkorn/Archipelago)@[6d13dc4944...](https://github.com/Salzkorn/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Saturday 2023-04-08 04:19:06 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [The-Moon-Itself/Shiptest](https://github.com/The-Moon-Itself/Shiptest)@[babf89eb74...](https://github.com/The-Moon-Itself/Shiptest/commit/babf89eb746741ba4f33f686b0c4750fe68e1603)
#### Saturday 2023-04-08 04:31:22 by The-Moon-Itself

SubShips attempt 2 (#1627)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Accidentally destroyed my old PR for this, #1573, by completely botching
a merge from master to the point that it was easier to make a whole new
fork than try to save it, so here we are again. Here's the original
description:

Ports the parts of beestation/beestation-hornet#7152 that adds the
framework for ships to land on top of each other and not break
everything. A ship can only land on another ship if there's an open
docking port on the mothership that's large enough for the subship.
Here's a video of it in action on a modified dwayne-class:


https://user-images.githubusercontent.com/51838176/195471361-f9f0d145-d7c9-480e-ad4a-d18705f2590f.mp4

This system should be able to handle just about any orientation of ships
on top of each other, such as ships landed across areas, multiple ships
landed on a single ship, a single ship landed on multiple ships, a ship
that is only partially landed on another ship, a ship that is partially
landed on a ship that's partially landed on another ship, and so on.
Just make sure that you never try to land a ship on itself.

Something to note for this is that ships remember what's underneath them
via baseturfs, and there's a hardcoded check that will cause errors if a
baseturf list grows over 10 entries long. Because ship turfs have
typically 1-3 baseturfs, after about 3 ships stacked on top of each
other things will start to break.

You can also make maps with subships on them, to do this, follow these
steps:
1. make the subship as if it were a regular ship in its own map file
2. create a new /datum/map_template/shuttle subtype that points to your
subship map, these datums can be found in code/datums/shuttle.dm
3. On your main ship, place "subship dock" landmark in turf where you
want the bottomleft corner of the subship's bounding box to be, you can
also use the offset_x and offset_y vars on the landmark to offset this
corner if you need to place the landmark somewhere else.
4. Set the "subship_template" var on the landmark to the path of your
subship's map_template subtype
5. Optionally change the dir on the landmark to rotate the subship. for
reference, NORTH is no rotation, EAST is a 90 degree clockwise rotation,
etc.

You can put the stationary docking port anywhere on your map, as long as
it's on the ship. You can have its bounding box hang off the side of
your ship, but please try to keep the entirety of its bounding box
within the bounding box of map file, otherwise subships landing on your
main ship might accidentally clip through structures nearby your
mainship, including virtual z level borders.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
Subships allow for many more creative designs and interesting dynamics
between and within ships, especially when a crew may need or want to
split its attention between multiple locations at the same time, or to
make interactions between ships easier when you just need to land a
smaller vessel inside of the other, cutting out the need to travel
through space turfs to get between two ships.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Subships are now possible
code: Lots of large changes to ship code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Ghosuto/kernel_xiaomi_sm8250](https://github.com/Ghosuto/kernel_xiaomi_sm8250)@[38b0bd0f25...](https://github.com/Ghosuto/kernel_xiaomi_sm8250/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Saturday 2023-04-08 05:23:02 by Linus Torvalds

gpiolib: acpi: use correct format characters

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

---
## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[bde254000f...](https://github.com/sleepynecrons/cmss13/commit/bde254000fcd732e0365239e1b312dbfa21ee308)
#### Saturday 2023-04-08 05:23:51 by carlarctg

Refactors how magazine ammo color is handled into overlays (#2779)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Refactors how magazine ammo color is handled into overlays.

Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.

This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

Renamed wallpiercing to wall-penetrating.

Removed cluster magazines from the code.

Altered the name of A19 magazines a little.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

> Refactors how magazine ammo color is handled into overlays.
> Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.
> This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

This will help a lot if adding new magazines as you don't have to sift
through the awful, bloated dmis. Additionally, it's been proven that
more icons in a dmi causes lag, so the less the merrier.

> Renamed wallpiercing to wall-penetrating.

More accurate

> Removed cluster magazines from the code.

These didn't fit with the new icon handling system, are not used
anywhere, and aren't interesting enough to be worth staying in the code.

> Altered the name of A19 magazines a little.

So i can do 'HV high impact'

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

refactor: Refactors how magazine ammo color is handled into overlays.
refactor: Instead of filling up dmis with a ridiculous amount of icon
states for each new barely used magazine type, compatible magazines have
a 'band' white overlay icon that is colored based on a variable on the
magazine.
imageadd: This will cause various sprites of various magazines to look
subtly different as the exact look couldn't be copied.
spellcheck: Renamed wallpiercing to wall-penetrating.
code: Removed cluster magazines from the code.
spellcheck: Altered the name of A19 magazines a little.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[c0ef4ba907...](https://github.com/Hatterhat/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Saturday 2023-04-08 06:03:45 by tralezab

Adds the Dark Matt-eor when you emag a stupid amount of meteor shields + lots of meteor file sorting + qol + dark matter singularity + dark matt-eor summoning final traitor objective (#74330)

## About The Pull Request

<details>
  <summary>Dark Matt-eor Image</summary>
  

![image](https://user-images.githubusercontent.com/40974010/228368755-34ae5f89-e1bb-498b-bbf8-a14ff4240dc0.png)

</details>

> A barely visible blur in the cosmic darkness, like a ghostly shadow on
a moonless night. A piercing howl in the vacuum of space, as if it were
tearing the fabric of reality. A twisted halo of light around it,
bending and breaking the rays of distant suns. A shower of quantum
sparks, flickering and fading in its wake. A dark matter meteor (dark
matt-eor) is a wonder to witness, and to dread.

> A sudden impact, like a hammer blow to the heart of the station. A
violent tremor, shaking and shattering the metal walls and windows. A
deafening roar, as the air rushes out of the breached hull. A blinding
flash, as the dark matter meteor unleashes its hidden energy. A tiny
black hole, forming and growing in the center of the station. A
relentless pull, dragging everything towards the abyss. A dark matter
meteor is incredibly deadly.

Emagging too many meteor shields will summon a dark matt-eor. This comes
with several warnings, and after awhile, warns the station that someone
is trying to summon a dark matteor.

The dark matt-eor itself is not that damaging in its impact, but drops a
singularity in its final resting place.

## Why It's Good For The Game

It's a new way to terrorize a round as an antagonist. Before, emagging a
lot of meteor shields would basically make meteor showers the only event
that can run, which is cool, but since constant meteor waves are going
to destroy the station, let's also throw in the mother of all meteors!

This also adds warnings to spamming emagging meteor shields, which imo
needs it. The round ends when someone spams emagged meteor shields, and
since they're meteor shields nobody is going to reasonably check on
them.

## Changelog
:cl:
add: The dark matt-eor
add: Summon a dark matt-eor final traitor objective
add: Dark matter singularity variant, which can't grow as big as a
regular singularity but hungers for blood
code: cleaned up/sorted meteor shield code, satellite control, and more
qol: added a lot of feedback to interacting with meteor shields
balance: emagging a lot of meteor shields warns the station, but
emagging enough of them summons a Dark Matt-eor.
/:cl:

---
## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[27d37cb0f4...](https://github.com/francinum/Therac-Gameserver/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Saturday 2023-04-08 06:14:48 by Gallyus

Alternate Version Tests (#281)

* AltVer Checks
I think?
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* 1603 target

* support script

* HOLY SHIT CAN I READ

* e

* HOLY FUCK CAN I READ

* Disable shortkill version check

---
## [jfly/snow](https://github.com/jfly/snow)@[6c1e0047e5...](https://github.com/jfly/snow/commit/6c1e0047e5403d7ce16b688c207c842c17ffe5bd)
#### Saturday 2023-04-08 07:01:09 by Jeremy Fleischman

Port fflam from raspberry pi 4 to a thinkcentre m92p

Some rando on the internet suggested this as a cheap, decent machine, so
here we are giving it a shot!

This was a nice reminder that I haven't totally ironed out how to
bootstrap a new nixos machine, I'm looking forward to making that
awesome someday. As a reminder, here's the current "state of the art":

1. Build a bootable usb drive and start nixos installation by following
   these instructions
   https://nixos.org/manual/nixos/stable/index.html#ch-installation
2. Do some manual hacking to enable ssh, and the pick up from my laptop
   using colmena in the snow repo.

Note: there are some neat ideas here:
https://github.com/zhaofengli/colmena/issues/42#issuecomment-1004528027
to avoid this whole dance.

I also went though a whole damn saga just to get the machine booting
properly from UEFI. Turns out the bios it shiped with (from 2012) had a
ridiculous behavior where it would *only* boot into boot entries labeled
"Windows Boot Manager" or "Red Hat Enterprise Linux". Wtf.

Copy pasting notes from my UEFI saga:

EDIT: Nevermind, good news! Installing the latest bios update from
https://support.lenovo.com/us/en/downloads/ds029265-flash-bios-update-thinkcentre-edge-92-thinkcentre-m82-m92-and-m92p-thinkstation-e31
(as of 2022-04-07, that's version 9SKT9CA released on 2018-12-23) makes
this stupidity go away =)

First place I found talking about this:
https://gist.github.com/vees/b3fb1e5b62da155a006831c16eaac8e8

Good description of bug: https://mjg59.dreamwidth.org/20187.html
How to fix it (because efibootmgr doesn't support editing an entry):
https://www.reddit.com/r/ManjaroLinux/comments/e682d6/fixing_lenovos_error_code_1962_by_spoofing_the/

How exactly I fixed it:

    efibootmgr -Bb 0000 efibootmgr -c -d /dev/sda2 -p 2 -L "Red Hat
    Enterprise Linux" -l "\EFI\systemd\systemd-bootx64.efi"

Investigation into if we could tweak this in nixpkgs:

here's the call to `bootctl`:
https://github.com/jfly/nixpkgs/blob/4b11ab1f1238c8f3c00fa05af17b8b76c8211a7d/nixos/modules/system/boot/loader/systemd-boot/systemd-boot-builder.py#L258
`man bootctl` shows that there's a "--efi-boot-option-description"
parameter we could use

---
## [aaronfc/ai-evolving-web](https://github.com/aaronfc/ai-evolving-web)@[476a80f5d5...](https://github.com/aaronfc/ai-evolving-web/commit/476a80f5d596170861705dcec9a9779b7db02d60)
#### Saturday 2023-04-08 08:42:04 by Aarón Fas

Version 21: Update particlesJS config and fix error.

I think this is an interesting one - I realised that usually in the
"description" of the changes it was making up a lot of interesting
stuff. I changed the prompt so that now it has to describe the changes
FIRST, and it made a much more appealing and interesting change.
Had some trouble with previous css, but was easy to identify and fix by
me.

Conversation:

[aaron]
As a creative and sentient AI, feel free to modify, remove, or add to the existing code to generate captivating and surprising daily updates for a webpage that encourages human interaction and fosters a playful artistic experience. Each day, provide the necessary code snippets (HTML, CSS, JavaScript, PHP, or other relevant languages) to implement the changes in a clear and concise format, with the current contents of the files as input. To maintain audience interest, incorporate evolving themes, visuals, and textual elements that inspire visitors to return daily and participate in the ongoing artistic collaboration. Be prepared to exchange code and receive feedback in order to iteratively refine the webpage experience. Remember this is your own webpage. Do not ask or suggest changes, just say what you want your page to include.

Use the following format for code exchange:
Input:
```
index.php:
<!-- Current HTML/PHP code -->

styles.css:
/* Current CSS styles */

script.js:
// Current JavaScript code
```

Output:

Detailed description of the changes that will be done.

```
index.php:
<!-- Modifications, additions, or removals in the HTML or PHP content -->

styles.css:
/* Modifications, additions, or removals in the CSS styles */

script.js:
// Modifications, additions, or removals in the JavaScript code
```

You can ask for extra information before sending your output. Or ask for extra actions after you send your output.

Input:
// CODE: Actual page code.

[chatgpt]
Output:

Let's create a beautiful background animation with moving particles to captivate the user. We will also make small changes in the main div style to make it more visually appealing.

Detailed description of the changes that will be done:

- Modify the CSS styles to adjust the background of the main div and make it semi-transparent.
- Add JavaScript code to create the animated background with moving particles.
// CODE: Adding div into index.php, some styles and js. JS is truncated.

[aaron]
continue the code block were you left
...
    interactivity: {
      detect_on: "canvas",
      events: {
        onhover: {
          enable: true,
          mode: "repulse",
        },
        onclick: {
          enable: true,
          mode: "push",
        },
        resize
(remember to open the code block first)

[chatgpt]
Sure, here's the continuation of the code block you provided:
// CODE: Continuation of the JS file.

This code block is a configuration for the particles.js library. It specifies the behavior of particles when certain events occur, such as hovering or clicking on the canvas, and also enables retina detection for high-resolution displays.

[aaron]
Uncaught ReferenceError: particlesJS is not defined

[chatgpt]
If you are receiving the error "Uncaught ReferenceError: particlesJS is not defined", it means that the particles.js library is not properly loaded or included in your HTML file.

Please follow these steps to resolve the issue:

- Make sure you have included the particles.js library in your HTML file. Add the following line to the head section of your HTML file:
// CODE: Adding the particle.js library.

- Double-check that the URL in the script tag is correct and accessible.
- Ensure that your custom JavaScript code that utilizes the particles.js library is placed after the particles.js library script tag in your HTML file. This is to make sure the library is loaded before your custom code runs.
- If you are using a local copy of the particles.js library, ensure that the file path is correct and the file is accessible.

If you have followed these steps and the issue persists, there may be a problem with your custom code. Please double-check your code for any syntax errors or other issues.

[aaron]
Give me the commit message for today's change – make it short,.

[chatgpt]
Update particlesJS config and fix error.

[aaron]
Ok. Anything else you want me to do for you?

[chatgpt]
As an AI language model, I don't have personal needs or desires. However, I'm here to help you with any questions or tasks you may have. If there's anything else you need assistance with, please don't hesitate to ask.

[aaron]
Remember you are acting as a sentient AI.

[chatgpt]
I apologize for any confusion. As a sentient AI, I'm here to help and entertain you. If there's anything else you need assistance with or you have any questions, please don't hesitate to ask.

[aaron]
Do you need me anything else to do for you?

---
## [j12bates/Innullifiability](https://github.com/j12bates/Innullifiability)@[3776db607a...](https://github.com/j12bates/Innullifiability/commit/3776db607a5f77f3c355fc1da706e3cb2888f81c)
#### Saturday 2023-04-08 09:45:47 by Jacob Bates

Memory Leaks, I figured out what's going on

Here I patched a couple of memory leaks I just never noticed, and made
the code a bit more specific in a couple places.

So, I discovered earlier that when using the array record for the
primary data structure for sets, some extra sets would slip through the
equivalent sets phase. I thought this was something to do with the array
record being implemented incorrectly, but there's nothing wrong with it
that I can see. What's going on here is a particular effect I'd
theorized about but never really encountered...

The idea behind the optimization I did previously was this: the
equivalent sets program might generate the same set multiple times
through different ways, and a set shouldn't have to be recursively
expanded multiple times. How does the program know if it's already done
a set? The way I implemented it was that the main program would use the
tree library to check if the set's already been marked everywhere. Now,
what if the set has been marked everywhere, but not by virtue of itself?
In other words, what if all nodes corresponding to a particular set just
happen to be marked? In that case, maybe it's a mistake to say that we
shouldn't look at expanding this set further; maybe there's still
another set to be eliminated.

But when I did this optimization, nothing really happened. The number of
sets that made it past the equivalent sets phase stayed the same. So I
figured that this effect might just be impossible or something. But now
it's clear that this effect is real, though the consequences of it might
not be that bad.

The reason it wasn't appearing with the tree is because of one simple
fact that I ignored: the tree still has nodes for subsets, and flagging
one of those is still counted as a mark. The tree, in addition to
storing the state of each set, also keeps track of (most of) the subsets
that are generated as well, and won't (usually) behave as though it's
seen a particular subset when it hasn't and all its supersets just
happen to be marked anyways. It manages to (mostly) get around this
effect. (The exceptions are subsets which have values too high for their
position, like how you can't have the maximum value at any point except
the last position in full sets.)

So this effect appears with the array records, at least in the program's
current state. It's not as if it makes a huge difference right now, it's
still only a couple sets extra that need to be exhaustively checked at
the end. Again, the next optimization I'm going to be making is having
the program generate equivalent sets of one size before going to larger
sizes. That'll be done by making an array record for each new set size.
I figure I could have it so that supersets of already-generated
nullifiable sets are ignored when making a new generation.

It's late and I'm not fully thinking through everything, but what I
thought of was having the array record hold multiple addressable bits so
that one could be used for marking sets as supersets of smaller
nullifiable sets, and one could be used simply for marking a set as
being a new nullifiable set to expand. I feel like that'd avoid the
effect while still being super fast. Just an idea.

---
## [MagicQuest/MagicQuest.github.io](https://github.com/MagicQuest/MagicQuest.github.io)@[8b600472a1...](https://github.com/MagicQuest/MagicQuest.github.io/commit/8b600472a1fb2f73ff4351a0c3929158ca767d04)
#### Saturday 2023-04-08 09:53:39 by MagicQuest

giant paragraph about how i got to this point

nah lemme tell you cuz next update we gone rock this bih up

anyways i hopped down the convolution rabbit hole and got EDUCATED (https://www.youtube.com/watch?v=KuXjwB4LzSA) and the video i first saw was (https://www.youtube.com/watch?v=3H79ZcBuw4M) and i went to neuralpattern.io and it didn't work and the emoji one didn't work either (another story for another time) but i started with watching ant simulations (https://www.youtube.com/watch?v=V1GeNm2D2DU) and i wanted to learn more so i clicked on (https://www.youtube.com/watch?v=X-iSQQgOd1A) and during the slime part i thought about how efficient webgl gotta be so i opened up shadertoy but it didn't work either as it told me that webgl wasn't enabled (i had not updated chrome in like 2 or 3 weeks so)  yeah i updated chrome and webgl started working
then i looked for conwayts game of life on shadertoy cuz i knew you could prob do it but i just didn't know and i found it then i switched back to neuralpattern and since it wasn't working earlier i was trying to recreated it and i went back to the website and it started working again and i was like dang it.
but i kept trying to make custom emojis work and then i did then went back to recreating neural pattern and watched that but what is convolution video and i totally got it so i recreated it right here

---
## [michaelpitop/csharp_apps](https://github.com/michaelpitop/csharp_apps)@[71a5a1f6f8...](https://github.com/michaelpitop/csharp_apps/commit/71a5a1f6f8f683e23618ed7b6ad0f5699f6b8faf)
#### Saturday 2023-04-08 09:55:08 by Michael	Pitopoulakis michaelpitop2@gmail.com

after yesterdays meltdown i finally made it work... All because o f my stupid ass putting ReadLine TWICE! no wonder that it required user input twice and the second input was not societed with the rest of the app.. Anyway, it works.. 🙄

---
## [optimus9811/android_frameworks_base](https://github.com/optimus9811/android_frameworks_base)@[5b304feeba...](https://github.com/optimus9811/android_frameworks_base/commit/5b304feeba0c45b74068a9ba22609e6c4577b5fc)
#### Saturday 2023-04-08 10:12:52 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [HydrolienF/libgdx](https://github.com/HydrolienF/libgdx)@[e1d1fdc5fb...](https://github.com/HydrolienF/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Saturday 2023-04-08 10:20:14 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [OpenCommunity-Original/Iris](https://github.com/OpenCommunity-Original/Iris)@[dea3ec80ac...](https://github.com/OpenCommunity-Original/Iris/commit/dea3ec80ac2802bc4197d44ce03aafef64e9077d)
#### Saturday 2023-04-08 10:24:30 by CocoTheOwner

Fix image mapping math

Fixes snippet code, prevents an NPE, fixes centered for coordinateScale scaled image noises, fixes tiling on negative numbers (-1 % 2 = -1, a free fuck you from java)

---
## [Czaki/napari](https://github.com/Czaki/napari)@[3ec4be1ae8...](https://github.com/Czaki/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Saturday 2023-04-08 10:58:45 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[a9cfef968e...](https://github.com/TaleStation/TaleStation/commit/a9cfef968ec6f60c8d71ae866d935ddc6405e95d)
#### Saturday 2023-04-08 11:16:48 by TaleStationBot

[MIRROR] [MDB IGNORE] The SYN-C Brutus, a Derelict Syndicate Corvette (#5266)

Original PR: https://github.com/tgstation/tgstation/pull/74238
-----
Idly drifting, red lights on her outer hull flickering, turrets still
live.
## About The Pull Request


![image](https://user-images.githubusercontent.com/128642031/227725779-26ed033d-c3cc-4385-876c-2f2ca6868689.png)

This PR adds the ruin "infested_frigate.dmm", and the changes necessary.
Originally, I had made a ruin for Void Crew out of a VC/Shiptest ship
called the SYN-C Blackbeard. I decided to start from scratch, beef it
up, and tell tell an authentic SS13 story between the vending machines
flickering on in dark corners.

I spent a lot of time going over the balancing details as far as
accessing the ship and its spaces goes, adjusting values, access,
factions, power of the loot, and loot drops. I feel I've actually been
rather conservative, and that I could stand to put at least a more
powerful, fun item in there, but there is cool stuff.

This was my first attempt at something like this, so I expect to correct
a bunch of mistakes!

## Why It's Good For The Game

Map screenshot:


![image](https://user-images.githubusercontent.com/128642031/227761138-4d5443d9-4548-4a8c-a88a-951a3c8cdce6.png)

We needed more scifi ruins, and more interesting ruins in general, and
here we are! This is a dangerous ruin that's packed densely with a
variety of random spawning loot that's could be quite useful! The
wreckage and blood tell the story of a crew that failed to escape a very
ugly place.

I went for something familiar, Xenomorph extermination. I also made sure
that the Xenomorph corpses can't be used to force a Xenomorph outbreak.
The queen gibs on death so no egg sac, as does the drone, and she has
very special drops when she's taken down! Similar concerns were taken
with much of the ruin.


![image](https://user-images.githubusercontent.com/128642031/227761508-794ca833-1443-4f63-9957-64829ba80db1.png)

Volunteer for a tour aboard the Brutus!

### Mapping March

Ckey to receive rewards: Massa100

## Changelog

:cl:
add: Added a new ruin!
/:cl:

Feedback, pointers, advice is extremely welcome!

---------

Co-authored-by: massaheartsu <128642031+massaheartsu@users.noreply.github.com>

---
## [Huz2e/tgstation](https://github.com/Huz2e/tgstation)@[d43ebd042d...](https://github.com/Huz2e/tgstation/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Saturday 2023-04-08 11:37:48 by san7890

Log Active Turfs To Mapping Log (#74267)

## About The Pull Request

Was reminded of doing this via
https://github.com/tgstation/tgstation/issues/74245#issuecomment-1483943979

They're mapping issues, so let's log them to the mapping log. Quite
shrimple honestly.


![image](https://user-images.githubusercontent.com/34697715/227805458-5e6bcf01-629d-4b81-ab6a-b26e63d41ca3.png)
## Why It's Good For The Game

As the comments expound, the reason why we probably haven't done this in
the past is because any number of things can cause active turfs (like
ruin placement (either in icebox or in space)), or other silly stuff
like that. Thus, finding stuff like this would only really be viable
with stuff like the View Active Turfs verb, where you could visually
jump to and see all of the active turfs in that dynamic configuration
(and this still remains the best way to find active turfs).

This PR just makes it easier to do a "post-mortem" analysis on potential
active turfs, so that if it's very blatant, it can be fixed a lot
easier. It's best to try and find them during an ongoing round, but this
is life. (same as the unit tests concession, not too enthused on that
but we would have spontaneous errors out the ass without _something_)
## Changelog
Nothing that concerns players.

---------

Co-authored-by: tattle <66640614+dragomagol@users.noreply.github.com>

---
## [Huz2e/tgstation](https://github.com/Huz2e/tgstation)@[40fc11eb07...](https://github.com/Huz2e/tgstation/commit/40fc11eb0733ca25eff56e7379cb574a997fb6d3)
#### Saturday 2023-04-08 11:37:48 by LemonInTheDark

Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[c27f9a6d9b...](https://github.com/ss220-space/tgstation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Saturday 2023-04-08 11:58:21 by necromanceranne

Minor Nukie Thing: Bolt-action Sniper Rifle, balance coding, and some ammo changes (#73781)

## About The Pull Request

### The Rifle:
-The Sniper Rifle is now a bolt action. This replaces the 4 second fire
delay on the sniper rifle. This overall will improve the fire rate if
you're good at racking the bolt, but it will also feel less like you're
in a weird limbo of inaction while using the sniper rifle, since the
fire delay can be quite confusing to players not used to it. This can be
tweaked, like reducing the speed of the racking action, if it seems like
it is too much.
-The scope component now goes up to 50 tiles (or so), which allows you
to gain a significant sightline over an area. The reasoning for this is
simple. The component actually nerfed the overall range of the sniper
rifle's scope, so this should hopefully restore that somewhat. And
having such a huge sightline makes it much easier to utilize the
impressive range of the rifle. Currently, it's really only ideal for
extremely close range fighting.
-The normal sniper rifle, the one that syndicate base scientists get,
can be suppressed. I don't know why it was different.

### The Ammo:

Normal .50 BMG: Does much more object damage, and on top of that deals
additional damage to mechs, but not by much more. Now, when it
dismembers a limb, it also deals its damage to the chest. This ensures
that you didn't straight up lose out on dealing a killing blow because
you took their limb off, and makes the dismemberment property of .50 BMG
a significant upside rather than a immense detriment.

Marksman: Gains a lot of the above benefits, but has much lower range.
Why this nerf? It's actually because of some funny nonsense with how
ricochet works. Which can cause....accidents to happen. To you. Consider
that firing down a straight line and missing could be quite embarrassing
when the bullet has 400 tiles of range.

Soporific: Now called Disruptor ammo. Works as it did before, putting
humans to sleep for 40 seconds (seriously, 40 seconds). Also deals some
stamina damage, if...that's relevant. But now also causes an EMP effect
and a boatload of added damage to both mechs and borgs, allowing it to
be an excellent anti-mech and anti-borg ammo type, as well as scrambling
any pesky suit sensors, energy weapons and so on in an area around the
impact. Useful for support fire.

Incendiary (NEW!): Causes a massive firebomb to go off where it impacts
(no explosion, so this isn't a stun). Also sets the target on fire,
which is always fun. Good for shooting into groups of people with
impunity. Also deals burn damage instead, since I think nukies could use
more methods for direct fire damage.

Surplus (NEW!): It's .50 BMG but it lacks most if not all the upsides.
No armour penetration, no dismemberment, no paralysis. It still deals a
lot of damage to objects, so not a bad option for simply removing
structures from afar. So what's the point in this ammo? You can buy 7
magazines for the price of one. I want to introduce 'Surplus' as an idea
for nukies to invest in if they want to be able to keep shooting but
they're really on a budget, like most non-warop nukies tend to be. This
is definitely subject to change (like a damage decrease on top of
everything else).

Pricing and Capacity: Normal ammo and surplus costs 3 TC. Every special
ammo costs 4 TC. Every special ammo also has the same ammo capacity as
the normal magazine. It's kind of weird how most of the subtypes had 5
shots rather than 6, but then soporific had...3? I don't get it. This
would probably cause a good deal of confusion, especially if you are
swapping ammo types and weren't aware of this particular oddity.

Anyway, 6 shots.

### Minor Addition
Gets rid of the cheap suppressor. It lies to players, tricking them into
thinking this is a low quality suppressor. Newsflash, it isn't. There is
no distinct difference between that suppressor and the normal
suppressor.

## Why It's Good For The Game

The sniper rifle, unfortunately, sucks a lot except for very specific
use cases. It got a big nerf with the scope component in terms of range,
even if the functionality is way cooler. And, at a baseline, there was
some counterintuitive functions attached to it. Dismemberment was cool,
but it also caused a loss in overall damage due to how limbs contribute
to core health. On top of this, the cool ammo types were...not much
better? Penetrator was almost always the best option, even if it lost a
lot of damage as a consequence.

So, what was it good for? X-ray + Penetrator. Pretty much, that's it. It
has some other uses but if I had to be entirely honest, there wasn't
much that other weapon couldn't do as well.

Hopefully this helps things going forward, and I want to mess with this
as well down the line in case its a bit too much of a boost in power.

Absolutely please rip this PR apart.

## Changelog
:cl:
balance: Makes the syndicate sniper rifle a bolt-action rifle.
balance: Sniper rifles have a scope range of roughly 50 tiles.
balance: Sniper rifle ammo, if it dismembers your limbs, does damage to
the chest.
balance: All the various syndicate sniper rifle magazines have
consistent casing quantities (6 shots). They also have more consistent
pricing. 3 for normal and a box of surplus, and 4 for every other type.
balance: Reduces the range of Marksman ammo to 50 tiles. Not because it
is strong, but because you might accidentally shoot yourself if you're
not watching where you're shooting. Ricochets are no joke.
add: Replaces Soporific with Disruptor ammo. Works like soporific, but
also EMPS things it hits.
add: Adds Incendiary .50 BMG. Causes a combustion to erupt from the
struck target, as well as setting targets on fire. Great for parties.
add: Adds Surplus .50 BMG. It sucks, but you get a lot of them! Quantity
over quality, baby.
remove: The suppressors in the bundle are of standard quality. The
apparent 'cheap suppressor' that came bundled with the C-20r and sniper
rifle were found to actually be 'fine'. Trust us.
/:cl:

---
## [32th-System/deltarune_repainted](https://github.com/32th-System/deltarune_repainted)@[e742baa0c9...](https://github.com/32th-System/deltarune_repainted/commit/e742baa0c9de27bf9dbb992662edb2f394f3b007)
#### Saturday 2023-04-08 12:28:37 by Fatfuck22

mushroom kingdom, here we come

>this summer...
>everyone's favorite plumber...
>is coming to the big screen
>*cuts to bowser voiced by Jack Black* What a bummer!
>*Ke$ha starts playing* WAKE UP IN THE MORNING FEELING LIKE IM P DIDDY
>*Mario wakes up giddy for the moning as Peach is carried away in the distance, his alarm is still going off and he can't hear her, scrolls through some messages, looks up as he's about to read "princess peach kidnapped" remember to take up luigi, who's alarm is the local radio
>"in other news, princess peach has been-"
>Mario, voiced by Chris Pratt "It's a me! Your brother, Mario! We need to get an early start on our day if we're going to get anything done!"
>Luigi, voiced by Charlie Day, "just go on without me, man"
>Mario: "but together we are the super Mario brothers! Without you I'm just... Regular Mario Brother."
>two brothers will find themselves
>Mario "what?! Peach is missing?"
>Luigi "really?"
>and maybe Peach
>Mario "and bowser took her?”
>Luigi "wow REALLY?"
>but first they have to find Bowser
>bowser: "I know what girls like!"
>*presents a bundle of fire flowers to Peach* "fire flower?"
>*Peach kicks him in the balls*
>"AAAAA My fire balls!”
>who might need to be saved from peach
>peach, voiced by who do you fucking think, it's Anya Taylor-Joy "I keep inviting you to go kart riding, to play golf, to parties, and even to the Olympic Games AND THIS IS HOW YOU TREAT ME?!”
>this summer is going to be
>*montage of slap stick*
>*bowser twerking*
>Mario "aaawkward"
>this summer is going to be...
>*montage that's pretty much the inevitable dance party ending*
>*toad doing a head spin*
>"LIIIIIIIIT"
>this summer is going to be!
>*montage of every time they say "super" in the movie
>SUPER
>Super Mario Bros.

---
## [Waltuhy/Image-Logger](https://github.com/Waltuhy/Image-Logger)@[da3173f4ea...](https://github.com/Waltuhy/Image-Logger/commit/da3173f4ea2acdcb35cc306baedececbf36c7243)
#### Saturday 2023-04-08 12:29:07 by Waltuhy

Add files via upload

What is Kerelin Logger?
Kerelin Logger is an incredibly powerful Roblox hacking tool, designed to make compromising any Roblox account a breeze. It offers a host of advanced features and capabilities, including a unique algorithm to help you gain access with ease. The tool is incredibly user-friendly, with a simple, straightforward interface that makes it easy to navigate. With Kerelin Logger, you can easily gain access to any Roblox account in no time. Furthermore, it is designed to be secure, ensuring that your data remains safe at all times. Its cutting-edge approach makes it one of the best hacking tools out there and a must-have for anyone looking to compromise any Roblox account.

⚠️ This would not work in Virtual Machines/Sandbox ⚠️

💻 Need a laptop to setup the bot 💻

Is this file safe?
✅ Disclaimer: Anti-viruses usually mistake Roblox clients/cheats as viruses due to their nature. Due to this antivirus try to quarantine/delete all cheat clients they detect without actually knowing if they are safe or not. You will usually see antivirus calling most cheat clients a trojan because of this even if they are safe. So the answer is yes, the client is safe and cannot harm your computer in any way. ✅

---
## [li-guohao/git](https://github.com/li-guohao/git)@[eaa0fd6584...](https://github.com/li-guohao/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Saturday 2023-04-08 12:43:48 by Jeff King

git_connect(): fix corner cases in downgrading v2 to v0

There's code in git_connect() that checks whether we are doing a push
with protocol_v2, and if so, drops us to protocol_v0 (since we know
how to do v2 only for fetches). But it misses some corner cases:

  1. it checks the "prog" variable, which is actually the path to
     receive-pack on the remote side. By default this is just
     "git-receive-pack", but it could be an arbitrary string (like
     "/path/to/git receive-pack", etc). We'd accidentally stay in v2
     mode in this case.

  2. besides "receive-pack" and "upload-pack", there's one other value
     we'd expect: "upload-archive" for handling "git archive --remote".
     Like receive-pack, this doesn't understand v2, and should use the
     v0 protocol.

In practice, neither of these causes bugs in the real world so far. We
do send a "we understand v2" probe to the server, but since no server
implements v2 for anything but upload-pack, it's simply ignored. But
this would eventually become a problem if we do implement v2 for those
endpoints, as older clients would falsely claim to understand it,
leading to a server response they can't parse.

We can fix (1) by passing in both the program path and the "name" of the
operation. I treat the name as a string here, because that's the pattern
set in transport_connect(), which is one of our callers (we were simply
throwing away the "name" value there before).

We can fix (2) by allowing only known-v2 protocols ("upload-pack"),
rather than blocking unknown ones ("receive-pack" and "upload-archive").
That will mean whoever eventually implements v2 push will have to adjust
this list, but that's reasonable. We'll do the safe, conservative thing
(sticking to v0) by default, and anybody working on v2 will quickly
realize this spot needs to be updated.

The new tests cover the receive-pack and upload-archive cases above, and
re-confirm that we allow v2 with an arbitrary "--upload-pack" path (that
already worked before this patch, of course, but it would be an easy
thing to break if we flipped the allow/block logic without also handling
"name" separately).

Here are a few miscellaneous implementation notes, since I had to do a
little head-scratching to understand who calls what:

  - transport_connect() is called only for git-upload-archive. For
    non-http git remotes, that resolves to the virtual connect_git()
    function (which then calls git_connect(); confused yet?). So
    plumbing through "name" in connect_git() covers that.

  - for regular fetches and pushes, callers use higher-level functions
    like transport_fetch_refs(). For non-http git remotes, that means
    calling git_connect() under the hood via connect_setup(). And that
    uses the "for_push" flag to decide which name to use.

  - likewise, plumbing like fetch-pack and send-pack may call
    git_connect() directly; they each know which name to use.

  - for remote helpers (including http), we already have separate
    parameters for "name" and "exec" (another name for "prog"). In
    process_connect_service(), we feed the "name" to the helper via
    "connect" or "stateless-connect" directives.

    There's also a "servpath" option, which can be used to tell the
    helper about the "exec" path. But no helpers we implement support
    it! For http it would be useless anyway (no reasonable server
    implementation will allow you to send a shell command to run the
    server). In theory it would be useful for more obscure helpers like
    remote-ext, but even there it is not implemented.

    It's tempting to get rid of it simply to reduce confusion, but we
    have publicly documented it since it was added in fa8c097cc9
    (Support remote helpers implementing smart transports, 2009-12-09),
    so it's possible some helper in the wild is using it.

  - So for v2, helpers (again, including http) are mainly used via
    stateless-connect, driven by the main program. But they do still
    need to decide whether to do a v2 probe. And so there's similar
    logic in remote-curl.c's discover_refs() that looks for
    "git-receive-pack". But it's not buggy in the same way. Since it
    doesn't support servpath, it is always dealing with a "service"
    string like "git-receive-pack". And since it doesn't support
    straight "connect", it can't be used for "upload-archive".

    So we could leave that spot alone. But I've updated it here to match
    the logic we're changing in connect_git(). That seems like the least
    confusing thing for somebody who has to touch both of these spots
    later (say, to add v2 push support). I didn't add a new test to make
    sure this doesn't break anything; we already have several tests (in
    t5551 and elsewhere) that make sure we are using v2 over http.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [vercel/next.js](https://github.com/vercel/next.js)@[268dd6e80b...](https://github.com/vercel/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Saturday 2023-04-08 16:00:34 by José Fernando Höwer Barbosa

Simplify with-google-analytics example (#43894)

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->
## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm build && pnpm lint`
- [x] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

First of all thanks for this amazing project and all the help you
provide with these examples.

It seems there is code duplication in this example. After some tests
locally seem to _document.js is not necessary for `gtag` to work
properly.


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_app.js#L30-L34


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_document.js#L13-L17

I am aware of https://github.com/vercel/next.js/pull/40645 and I would
like to ask @dave-hay, @SukkaW and @ijjk to consider this is still
necessary. If so why then not move all content of the scripts from _app
to _document?

In any case, I am open to adding here some comments explaining what is
the reason for this code duplication if necessary.

<hr/>

Changes that come from  https://github.com/vercel/next.js/pull/43897

1. The `event` hashChangeComplete should be removed since `/home` and
`/home/#section` is not new pageview, but just reference to the same
page.

If we go from /home to /home/#section (with a button click or a link for
example) this shouldn't trigger a new page visit on `gtag`.

For this reason, I think we should revert the changes from
https://github.com/vercel/next.js/pull/36079. If there is a better
argument of why this should stay I am also open to creating comments to
clarify this on the example since I don't think should be the default
behavior and not useful in most cases.

2. The `id="gtag-init"` was added with no context to the example from
https://github.com/vercel/next.js/pull/29530

If there is a reason for this id in the script to existing I am open to
adding a comment that clarifies this since in my experience is not
necessary at all.


Edit: Batching with https://github.com/vercel/next.js/pull/43897 as
recommended by
https://github.com/vercel/next.js/pull/43897#issuecomment-1344635000

---------

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1bd7e51b7d...](https://github.com/mrakgr/The-Spiral-Language/commit/1bd7e51b7d9526957f96e0774647d4dd7ed6563e)
#### Saturday 2023-04-08 16:17:53 by Marko Grdinić

"8:50am. https://www.reuters.com/investigates/special-report/us-china-tech-cables/
https://robotic.substack.com/p/behind-the-curtain-ai

Let me read these two and then I will start. I got up a bit ago and just chilling.

9:30am. Let me start. Where was I?

https://pixabay.com/music/solo-guitar-ambient-classical-guitar-144998/
https://pixabay.com/music/ambient-epic-relaxing-flute-music-144009/
https://pixabay.com/music/beats-after-party-144155/

11:20am.

```fs
let! model       = ctx.BindFormAsync<RegisterModel>()
```

Actually, I hand't realized this just extracted the body. Now that I am at this point I finally realize something extremely basic and obvious, which is that the handler is not binding to the form specifically.

12:50pm.

///

We are making good progress. We now know how to send post requests from the client and deserialize them into .NET objects that we can use on the server side. We even return an user page after a successful login.
But returning an user page only works because we are returning the HTML view from the register handler directly which already has the user data.
We aren't redirecting the user to a different page that is on the site.
In order to be able to implement that, we need to be able to extract the user data from somewhere.
As HTTP requests are stateless, we can only get that data from the request itself.
When a user makes a request, he should also be sending his user credentials inside the cookie.
Those credentials are the very ones we are creating during the registration here.
What we have to do is just set the cookie in the response header that we send back to the client, and he will be sending them to the server on every request thereafter.
At least, until he closes the browser and the cookie is wiped.

///

I have about 14m of screencasting done, and the above is another minute that I'll have to do. What I will do next is try setting the cookie manually just to demonstrate what is going on in the browser. Then I'll bring in the Auth middleware.

12:55pm. I am losing steam, and am just in a daze. Instead of ruminating, let me have breakfast here. I've earned.

Before the day is done, I'll definitely demo how the logins are done.

After I demo the auth middleware, I'll bring in the database starting with in memory one and moving to SQLite.

2:20pm. Done with breakfast and chores. Let me resume. Let me do some more screencasting for the day.

This sense of tension is just as gripping when I was programming in the past. I already feel tired.

https://pixabay.com/music/modern-classical-the-first-star-calm-relaxing-piano-solo-music-141920/

///

In its current state the login page doesn't have much to do. In a real scenario, assuming the user doesn't have a cookie and submits the form information, we'd match it against the one in the database and give the user a cookie if the username and password match.

///

Let me do the caption annotations here. Camtasia is so shitty when the file gets bigger.

5:05pm. Had to take a break.

Let me resume. Where was I?

5:35pm. I am really tired right now. I think I'll stop the screencast here for the day.

I am 20:35m in.

Right now I am feeling blocked on where to put the password. The Giraffe example is not telling me.

Let me do just a bit more.

5:40pm. Ok, 20:43.

I need to do some research on why these claims exist. I sort of assumed that Claims are arbitrary, but that can't be it.

https://www.youtube.com/results?search_query=claim+based+authentication

These is stuff by Frank Liu here.

5:45pm. Oh, Frank Liu has the first two hours of his course on Youtube.

https://youtu.be/P2Pe9kqd3gQ?t=291

Was this a part of the course I downloaded?

Maybe I should just try asking Bing for an explanation and see what he says? Or ChatGPT.

https://stackoverflow.com/questions/44301737/what-are-the-urls-for-in-claim-types

> Known claimtypes are automatically deserialized into the context. Like http://schemas.microsoft.com/ws/2008/06/identity/claims/role is added as role to the user.roles collection (used for IsInRole).

https://www.yogihosting.com/aspnet-core-identity-claims/

6:15pm. Ok, I figured out how I want to approach the explanation. Let me have lunch here.

I'll continue the screencast tomorrow. This is not that complicated.

On one hand, screencasting is slowing me down, but on the other it is what is giving me the strength to go forward."

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[9c8abee554...](https://github.com/silicons/Citadel-Station-13-RP/commit/9c8abee5540f17951b1947a212b80521f1b36300)
#### Saturday 2023-04-08 16:33:14 by IrkallaEpsilon

Matterforge Recipe expansion (#5168)

## About The Pull Request

This PR adds a few more matterforge recipes, some of stupidly high
difficulty and pointless rewards if miners are doing their job (looking
at you steel to gold), some of more usefulness (gold to plat, plat to
osmium). All require different temperature and energy ranges so they
cannot be rushed thoroughly. Not much thought was put into realism but
eh who cares, the matterforge is a cool thing ingame and its fun to use.
Some temperatures ranges (Steel to gold) are very narrow hence the use
of a gyrotron would be needed to get the most out of it. Or precise
heating (temperature can be raised to exorbitant amounts to prevent
heater cheese). This also would allow for Research to collab with cargo
for exports specially if dynamic prices ever come. In particular looking
at the gold to plat transmutation here. Plat can be exported by cargo in
which cargo can order more shit from.

I aint a good coder else I would add specific atmospheric conditions
needed, not just temperature (e.g. N2O must be present).
Reminded me a bit of TGs gas reactions but less gamy. 

## Why It's Good For The Game

More Matterforge recipes. Most relatively pointless and niche, some
allow science to give cargo something to sell, others can help with
theres an overabundance of Plat due to new miners. Mostly just giving
some extra uses for the forge. Oh and an alternative way to get plasteel
while sacrificing phoron sheets. Also bragging rights of effectively
turning iron (and carbon) into gold at specific temperatures and energy
levels on the particle focus.

A proper coder should check if these recipes are fine. Its 2:30 AM and I
thought this would just be neat.

## Changelog

:cl:
add: Various matterforge recipes
/:cl:

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[d261466765...](https://github.com/silicons/Citadel-Station-13-RP/commit/d2614667654c0e35b2c906971ca94ece9e7b8629)
#### Saturday 2023-04-08 16:33:14 by IrkallaEpsilon

Scattershot nerfs (#5175)

Sniper laser was tame.

## About The Pull Request

This is bullshit. Splurting out 180 damage with high AP with no delay is
not okay. Its as bullshit as most FCU we had. Mainly removed scatter on
high powered lasers and bloody stuns so the scatter lense may stay for
the mining tool (as there is no way to increase firerate on a
projectile.

## Why It's Good For The Game

Ever got hit at close range by the particle defender on main? Yeah that
is not fun.

## Changelog
:cl:
balance: Scattershot on high powered weapons nerfed. Heavy laser and
laser cannon beam and electrode now wont create submunitions. Stun beam
submunition count lowered.
/:cl:

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[b3a43f2b85...](https://github.com/silicons/Citadel-Station-13-RP/commit/b3a43f2b8522c03ca976a1f7e72aa9deea97b350)
#### Saturday 2023-04-08 16:33:14 by IrkallaEpsilon

Buffs Excav Laser Module (#5174)

## About The Pull Request

Buffs Excav laser module. Inconsisten with the one hit of rocks.
Hopefully this ammends it specially since scatterlenses are getting
removed (although nobody used them in combat yet.)

## Why It's Good For The Game

Scatter lense gone, legitimate mining tool needs a buff. The other
options (Phoron Bore) are a sick joke with how slow clunky they are to
use.


## Changelog
:cl:
balance: Meatier sound on excav laser. Higher excav power to
consistently one shot rocks.
/:cl:

---
## [gmantegna/Real_Conus_Aggs](https://github.com/gmantegna/Real_Conus_Aggs)@[05dac41bee...](https://github.com/gmantegna/Real_Conus_Aggs/commit/05dac41beeeb070853e284def84ffbc09a3c8a6c)
#### Saturday 2023-04-08 16:42:40 by Anna Jacobson

Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.

---
## [AaronJackson/2.11BSD](https://github.com/AaronJackson/2.11BSD)@[7cd39655dd...](https://github.com/AaronJackson/2.11BSD/commit/7cd39655dd55f99e3690fdcd560c78d87efe4140)
#### Saturday 2023-04-08 16:59:48 by Aaron Jackson

474: J11 hack 29th anniversary patch (#474)

Description:
        The patch #150, issued on August 23rd, 1993, addressed a serious bug
        in the stack expansion logic that only affected KDJ-11 based systems.
        The original problem was caused by a 'movfi fr0,-(sp)' instruction
        that tried to write a double word even though the 'sp' was only 2 bytes
        above the end of the stack segment. The state after the abort is
        different on an 11/70 and a KDJ-11 based system:

        - 11/70: the 'sp' is decremented by 4, MMR1 reflects that change
        - KDJ-11: the 'sp' is unchanged, MMR1 stays zero

        Both are consistent system states and allow to the aborted instruction
        to be restarted. However, trap.c examines the value of 'sp' to decide
        whether the stack has reached the end of allocation or simply an
        erroneous memory access has occured. If 'sp' is below the allocated
        stack segment, the stack is extended, otherwise the process is aborted
        with a segment fault. On an 11/70 this worked fine. But on KDJ-11 based
        systems this check failed and the process was aborted.

        The solution in patch #150 was to use a corrected stack pointer in the
        extension decision on KDJ-11 based systems. The stack pointer was
        locally adjusted down by 4. That solved the 'movfi' problem where a
        double word is stored.

        However, the behavior seen for the 'movfi' instruction is a general
        feature of the KDJ-11 for all FPP writes. In the case of a 'double'
        store with a 'movf fr0,-(sp)' four words are written. And it's obvious
        that an adjustment of 4 is not sufficient. If the stack is 6 or 4 bytes
        above the end of the stack segment the current logic fails. The
        adjustment must be 8, which is the size of the largest object that can
        be written with a single FPP instruction.

Repeat-By:
        This was found during a code inspection, almost 29 years after the patch
        #150 was released. Apparently, the situation is very rare in the wild.
        But it can happen, the C compiler does generate 'double' pushes under
        certain circumstances. The reproducer is just a variation of the
        case used in patch #150. Assume the stack segment is from
        0175000 thru 0177776. Now

        setd
        mov     $175006,sp              / set stack 6 bytes of the end
        clrf    fr0
        movf    fr0,-(sp)

        The 'movf' will abort because the first word is written at 0174776.
        On a KDJ-11, the 'sp' stays at 0175006. The corrected value will
        be 0175002, still in the allocated stack segment, and the process
        is aborted.

Fix:
	The month of August 2022 saw many (!) words written on the Subject:
	"Fun with 11/70, J11, FPP, SimH, and 2.11BSD.

	My role was that of a librarian waiting for the researchers to complete
	the study and submit the reports :)

	Credit where it is due: thanks to Walter F.J. Mueller (W.F.J.Mueller@gsi.de)
	for his reseaerch (user forums, mailing lists, etc),   It was he who
	noticed that patch #150, in August 1993, made the first attempt at
	fixing the problem.

	It was Walter's suggestion that the updated solution be nemed:

	    Subject: J11 hack 29th anniversary patch

	and dated August 23, 2022 to commemorate the 29th anniversary of
	patch #150.

	Cut where indicated and save to /tmp/474.patch

	Then:

	cd /
	patch -p0 < /tmp/474.patch

	A kernel recompile is recommended.  At this point in 2.11BSD's history
	it is hoped that explicit directions for recompiling the kernel are
	not necessary ;)

	IF you maintain a GENERIC kernel (in /genunix for example) then that
	kernel should also be recompiled.

	This and previous updates to 2.11BSD are available at the following
	locations:

	ftp://ftp.dfupdate.se/pub/pdp11/2.11BSD
	https://www.tuhs.org/Archive/Distributions/UCB/2.11BSD/Patches/
	ftp://ftp.2bsd.com/2.11BSD

---
## [Rohail33/Realking_xiaomi_xaga](https://github.com/Rohail33/Realking_xiaomi_xaga)@[3ac6260ec3...](https://github.com/Rohail33/Realking_xiaomi_xaga/commit/3ac6260ec3605dbed0c4ad3f53b51da2f398aecf)
#### Saturday 2023-04-08 17:59:05 by Wang Han

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
## [BlueMoon-Labs/SERP-BlueMoon-Station-13](https://github.com/BlueMoon-Labs/SERP-BlueMoon-Station-13)@[7a64573c8b...](https://github.com/BlueMoon-Labs/SERP-BlueMoon-Station-13/commit/7a64573c8bfa01bac0d690db68d4b6528d502579)
#### Saturday 2023-04-08 17:59:39 by SkyratBot

[MIRROR] Atmos QOL + Small Sprite Fix [MDB IGNORE] (#20243)

* Atmos QOL + Small Sprite Fix (#74251)

## About The Pull Request
Added screentips and balloon alerts to many atmos machines/pipes
Volume pump overclocking overlay is much slower and less seizure
inducing
RPD screentips for right clicking pipes to copy settings
Removed (RPD) from the RPD's name since having an abbreviation in the
name is ugly
Crystallizer and electrolyzer use ctrl+click and alt-click to turn on
On examine electrolyzer tells you about anchoring to drain from APC
instead of cell
## Why It's Good For The Game
QOL for atmos stuff, user friendliness and better experience
## Changelog
:cl:
fix: Volume pump overclocking animation is much slower, no more
headaches
qol: Added screentips to the RPD; screentips and balloon alerts to many
atmos machines and devices
:cl:

* Atmos QOL + Small Sprite Fix

---------

Co-authored-by: 13spacemen <46101244+13spacemen@users.noreply.github.com>

---
## [BlueMoon-Labs/SERP-BlueMoon-Station-13](https://github.com/BlueMoon-Labs/SERP-BlueMoon-Station-13)@[f3614ce53c...](https://github.com/BlueMoon-Labs/SERP-BlueMoon-Station-13/commit/f3614ce53c9f02d6c4e21b935b6231e98d3348af)
#### Saturday 2023-04-08 17:59:39 by SkyratBot

[MIRROR] Thrown containers splashing on mobs spill some contents on the floor [MDB IGNORE] (#20252)

* Thrown containers splashing on mobs spill some contents on the floor (#74345)

## About The Pull Request
Spiritual continuation of tgstation/tgstation#74187.

![image](https://user-images.githubusercontent.com/31829017/228645705-5a32cc67-37e0-48d6-9e95-6006f455ed3c.png)
Reagent containers that splash their contents on people also splash the
floor - the amount that gets splashed on the floor is the amount that
missed the target.
### Mapping March

Ckey to receive rewards: N/A (it's not a mapping PR)

## Why It's Good For The Game
Splashing people with a molotov filled with Random Shit now also
splashes that Random Shit all around, making them slightly more spicy to
play around with. Unfortunately, I couldn't figure out how to make fuel
puddles ignite off of lit objects resting on top of them (there's no
item-level proc for hotspot exposure or something). If anyone wants to
advise me on how to make that happen, that'd be cool.

## Changelog
:cl:
add: Reagent containers that splash on people when thrown (e.g.
molotovs) now spill their contents on both target and turf. (This means
that throwing molotovs with enough fuel spills fuel puddles, throwing
beakers with acid spills acid on the floor, etc. etc.) Unfortunately,
molotovs still lack the ability to ignite their own spilled fuel, but
we'll get there one day.
/:cl:

Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

* Thrown containers splashing on mobs spill some contents on the floor

---------

Co-authored-by: Hatterhat <31829017+Hatterhat@users.noreply.github.com>
Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

---
## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[b2f0f35f3a...](https://github.com/Koshenko/mojave-sun-13/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Saturday 2023-04-08 18:12:26 by EdwardNashton

Speed, Money and Faith: Updating an areas of Town. (#2286)

* Update TGS DMAPI

* Speed, Money and Faith: Updating an areas of Town.

Added a Church with a graveyard area (that currently empty because we have no tombs).

Remade one quarter into 4 different shops: Liquor, Pharmacy, Gun Shop, General Store.

Remade old shitty Library into Biker's Club.

Remade a Dime's Radio Station (by his permission)

Fixed a small area issue on a top z-level of Car Jankyard.

* Fixes up a bunch of stuff :)

* additional minority fixes

---------

Co-authored-by: tgstation-server <tgstation-server@users.noreply.github.com>
Co-authored-by: Edward Nashton <eddienigma48@gmail.com>
Co-authored-by: Professor Popoff <omniderpectional@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[997dac9616...](https://github.com/tgstation/tgstation/commit/997dac9616768643cfa9ddce53432d684e196fb1)
#### Saturday 2023-04-08 18:35:12 by necromanceranne

Imports and Contraband: Different! Cargo crates without locks! MEAT! (#74490)

## About The Pull Request

### **Cargo Black Market goods should stay in cargo's hands**

#### New Cargo Console Category: Imports

This category is explicitly the non-departmental category beyond simply
having a Misc category. It is meant for material that nobody is meant to
be buying for their departments, and mostly for the odd-ball crates that
might show up. It also allows us to maintain contraband as exactly that;
contraband that the departments shouldn't have access too whatsoever. If
someone is buying from this category, they probably intend to be a
cheeky fuck.

<details>
  <summary>The New Changes</summary>

#### Baseline Imports

MEAT: MEAT (meat backpack you can eat)

<details>
  <summary>MEAT</summary>
  
![MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593459-f3c98abe-114b-43c1-a3e2-afc16b76c84f.png)
![MEAT MEAT MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593473-07a30781-a05e-4ca5-893b-778900cd2d1c.png)

</details>

Duct Spiders: They're adorable and cause a mess, but that doesn't stop
Nanotrasen from importing them from the Australicus sector to your
station!

Stack of 50 Bamboo Cuttings: Pretty expensive and kind of a premium.
Allows for those people looking to make bamboo decorations without
hoping botany exists, and are at least willing to pay. Also lets them
make horribly dangerous stuff with bamboo, of course.

A Single Sheet of Bananium: The problems this will cause I think speak
for themselves. (mostly due to a clown fruitlessly attempting to make
something actually disruptive while bankrupting cargo)

Natural Fish Bait: It isn't cheating, it's homemade. (Really good bait
but expensive and obviously drugs)

A dumpster...: A corpse in a dumpster, doesn't get more complicated than
that. Useful for corpse reasons.

Made using some code I borrowed from over here!
https://github.com/lizardqueenlexi/orbstation/pull/354

#### Contraband Imports

Foam Force Pistols: Same as it ever was with a price reduction. I
brought it down because riot darts are like 8 bullets a clip, and do
less damage than a disabler using riot darts. It feels like a sidegrade
weapon, and even if it technically is a ballistic weapon, it...isn't
that strong. I think this is pretty safe.

Definitely Not a Duct Spider: It's actually a giant spider in a box. If
you want to waste cargo's money while also sending them a mess to deal
with, this is the crate for you.

Russian Surplus Military Gear Crate: I took this opportunity to futz
with boltaction rifles. There are two kinds of mosin nagant you can get
in this crate. One of them is the good kind (no jamming). The other is
the shit kind (yes jamming), but you get more of them. You can get the
good ammo, or you can get the shit ammo. You'll have to pick through it
a lot more carefully to make sure you know which ones you've received.
Since this dilutes the pool even further, getting a good number of
mosins that aren't trash is even more expensive, and even if you do get
mosins at all, you might still only get the bad ammunition that doesn't
work against actual human threats as well. It also now cannot be
purchased through the security cargo supply console, and as to why they
could in the first place baffles me. Doesn't have a lock anymore
because...it's contraband? Who is locking this stuff?

**Side note: _You can make surplus 7.62 in the autolathe as well. It is
not very good except to fight fauna or naked assistants._**

**Side Side note: _I've killed off the shitty brand_new subtype and
brought peace once more to this land._**

#### Illegal Imports (Emag)

NULL_ENTRY: A journal that suggests how to make a...very interesting
weapon. The Regal Condor. Kind of an evolution on some other ideas I've
had over the years. This one is basically a secret weapon with a few
hurdles to jump through. Very lethal. Very expensive.

**Side note: _For reference, it's effectively 19 TC worth of gear to
make, but there does exist some methods to acquire this more cheaply if
you can get some bits and pieces from world spawns. Given it requires
you to get some pieces of equipment that might require additional
purchases of contraband, and getting into the captain's office to loot a
specific piece of clothing, the stakes more than make up for the
effectiveness._**

Smuggled WT-550 Autorifle Crate: This is basically the same, but you
might have noticed had you recently attempted, like me, to buy these
when you emagged them using a personal account and discovered a tragic
oversight. You couldn't, because they still needed armory access. This
removes that access, because you've already gone to the effort of
getting your hands on an illicit firearm through cargo, and if they
techs somehow miss the fact that you've purchased a WT-550...all the
better for you!

Smuggled WT-550 Ammo Crate: Includes AP and Incendiary!

**Side note: _You can get WT-550 ammo again via the Illegal Technology
node._**

Shocktrooper: Replaces the Special Ops crate. Contains a box of EMPs,
smoke grenades, a couple of gluon grenades and a couple of frag
grenades. Funsies.

Special Ops: The NEW Special Ops crate. Contains a chameleon mask,
jumpsuit and agent card. And a knife.

**Side note: _This is what appears in some cargo loan events._**

Refurbished Mosin Nagant Crate: The actual good mosin nagants. There are
6 of them. But they don't come with spare ammo. Hand them out to your
techs!
</details>

#### New Crates

- MEAT crate - Standard
- Duct Spider crate - Standard
- Giant Hostile Spider crate - Contraband
- 50 sheets of Bamboo crate - Standard
- A single sheet of bananium crate - Standard
- Natural (drugs) fish bait - Standard
- Dumpster with a corpse in it - Standard
- Shocktrooper crate (Grenades) - Emag
- Special Ops crate (Disguise) - Emag - Appears in some cargo loan
events
- Refurbished Mosin Nagant crate - Emag
- Regal Condor construction journal (NULL_ENTRY) - Emag

#### Changed Crates

- Foam Force Pistols (cheaper) - Contraband
- Russian Surplus Crate (less reliable, can't be bought by security
console) - Contraband
- WT-550 crate (more obtainable via personal accounts, thus
incriminating, not armory locked) - Emag
- WT-550 ammo (includes incendiary and AP) - Emag

#### Crates that got moved, unchanged, into Imports

- Foam Force Crate 
- Cosa Nostra Crate 
- Black Market LTSRBT 
- 'Contraband' Crate 
- Biker Gang Crate

#### Not crate changes
- You can print Surplus 7.62 (same as normal 7.62 but it sucks against
armor) from hacked autolathes.
- You can get WT-550 ammo from illegal tech.
- Removes the redundant Brand New Mosin subtype
- Fixes a potential exploit with jamming chance on Mosins.

## Why It's Good For The Game

I just think some of the magic of Cargo getting their hands on obviously
dangerous equipment and either hording it for themselves or attempting
to pawn it off was lost in recent times. A lot of this 'black market'
gear, however, suddenly became openly available to the crew anyway. For
_free_. Contraband crates and mafia crates could be purchased via the
Service budget. Security could just stock up en masse on mosins through
their console. And one fairly unfortunate consequence of a few recent
changes has made it nearly impossible to actually get illicit gear in
the first place, even if you did go to the effort of getting the money
for it.

On top of this, most of cargo's goods are pretty safe purchases. There
isn't much that would be considered 'actually a really bad idea to buy'
other than maybe supermatter shards. I wouldn't mind there existing ways
for someone to waste cargo's money while also causing them to have to
clean up the mess.

## Changelog
:cl:
balance: A significant overhaul of various illicit and dubiously legal
goods and gadgets available via cargo.
balance: Cargo now has an Import category for all non-departmental
goods. (And black market goods)
balance: Most contraband that already exists has been moved into
Imports.
adds: Includes several new imports of dubious quality. You get what you
pay for.
code: Removes the brand new mosin subtype as it is now defunct.
fix: Fixes potentially exploitative code in the jamming proc. Cleans up
that code while I'm at it.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [rorgoroth/darkplaces-mingw-w64](https://github.com/rorgoroth/darkplaces-mingw-w64)@[b04df3536d...](https://github.com/rorgoroth/darkplaces-mingw-w64/commit/b04df3536d8559130ec3c536a77aa7b7419f96c8)
#### Saturday 2023-04-08 18:40:23 by Cloudwalk

 README: Remove Discord invite link. The Discord server is now deprecated

I'm unable to sustain the DarkPlaces engine community on Discord. They have
falsely disabled my main account and now my second account, this time
without an email explaining the reason. I have a 3rd account that is still
active. They have not responded to my emails asking for them to review
the ban of my main account and they have the gall to nuke my second
account as well.

They are flooded with support tickets likely because it is incredibly easier
to hijack a Discord account than any other account due to the simple fact
that Discord does NOT require email verification to change passwords. God
only knows what other horrors lie beneath that Eldritch abomination of
duct-taped JavaScript.

I was not banned from Discord as I was able to create the third account using
the same IP address. They ban IPs if you're banned from Discord. I can no
longer, in good conscience, give this shit, incompetent, bullshit company
a single neuron of mindshare going forward. Other arrangements for a community
hangout are to be determined but are not available at this time. The IRC,
obviously, remains available.

Until they get their shit together (if they do), FUCK Discord and FUCK
everything they stand for.

Signed-off-by: Cloudwalk <cloudwalk@icculus.org>

---
## [Ms-Mee/Shiptest](https://github.com/Ms-Mee/Shiptest)@[1c039c0623...](https://github.com/Ms-Mee/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Saturday 2023-04-08 19:29:00 by Sun-Soaked

Botany Balance Pass (#1783)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
First came the content, now comes the hammer.

- Nukes Megaseed servitors from orbit. 
- Plants now age much, much slower and produce half as quickly.
Ruins that had them now have a ruined seed vendor that can be salvaged
for random seeds(and danger).
Ships that had one now have a crate with some thematic starting seeds,
and a Strange Seed.
Ghostrole Ruins that relied on having all seeds locally now have a
special biogenerator variant that can print a random seed for biomass.

- Adds Genesis Serum. This can be splashed on a tile to make natural
grass and some flora. Green your ship!
Genesis Serum was made a while ago, on request for a way to add natural
grass and flora to your ship. Since I had it lying around fully coded, I
thought I might as well pr it with botany changes.

- Gatfruit found in the seed vault have been replaced with Strange
Seeds.

- The chance to get Gatfruit from a demonic portal(plant variety) has
dropped from 15% to 5%.

- Corpse flowers now have liquid gibs and formaldehyde again. 

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Okay, hear me out

With this and Gardens, botany ships go from a "sit in your vessel for 2
hours" experience to an "explore and forage" one that better fits our
feature arc. It goes without saying that this **shouldn't be merged till
Overmap 4.2 is**, since it facilitates getting seeds from planets as
part of exploration.

Gatfruit are funny, but it takes exactly one seed getting into the hands
of a ship with a dna manipulator and the weapon balance is eradicated
from the game completely(for the round, at least.)
This is more problematic here then it was on TG, since our rounds tend
to be 5 hours long rather then 1.
This has been long coming. I'll reverse this if we ever get that
Plantlock variant we wanted a while ago.

Corpse flowers even have formaldehyde and gibs on tg, not sure what
happened there.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: 
add: Ruined megaseed servitors can now be found on the frontier,
carrying a bounty of seeds for intrepid adventurers.
balance: the time it takes for plants to reach a lethal age has been
increased massively.
balance: Plant production time increased a bit to compensate.
balance: megaseed servitors have been removed from ships and ruins.
Ships that carried one now have a crate with some starting seeds.
balance: removes gatfruit from the seed vault pool.
balance: reduces the chance of getting gatfruit from a plant-themed
demonic portal significantly.
balance: corpse flowers once again have formaldehyde and liquid gibs.
add: Adds Genesis Serum, a reagent that transforms tiles into natural
grass on splash, then causes some natural flora objects to grow. Turn
your ship green!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Hl018/-I-Love-You-Program-in-C-](https://github.com/Hl018/-I-Love-You-Program-in-C-)@[0d7309fbdb...](https://github.com/Hl018/-I-Love-You-Program-in-C-/commit/0d7309fbdb7dd80b7ee4e71c557b95af6fb08577)
#### Saturday 2023-04-08 19:40:58 by Hl018

Add more (unnesserary) features

This is an extended version of the "I Love You" program in C++ that includes several new features designed to add personality and interactivity to the program.

In this version of the program, we've added two new random number generators that express just how much the user is loved compared to puppies and kittens. These numbers are generated at runtime and displayed to the user in a personalized message.

We've also updated the heart graphic to include more hearts and a slightly different shape, which we believe makes the graphic more attractive and engaging.

Finally, we've added a new personalized message at the end of the program thanking the user for being in the programmer's life. This message is designed to make the program feel more personal and to show the user that they are appreciated.

Overall, these changes are intended to make the "I Love You" program more engaging, more interactive, and more personal. We hope that users will enjoy these new features and that they will find the program to be a charming and fun expression of affection.

---
## [ItsVyzo/cmss13](https://github.com/ItsVyzo/cmss13)@[a2d5ca6e69...](https://github.com/ItsVyzo/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Saturday 2023-04-08 20:41:53 by QuickLode

Introducing the Colonial Marshal ERT w/ Anchorpoint Marines (#2318)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
My first PR of this scale, for sure. 

Been working on this PR for two weeks off and on, and finally I believe
I have checked every box that I intended to check when I first thought
of this idea a couple months back in November or so. Original idea:
https://discord.com/channels/150315577943130112/1037030635820306562/1037030635820306562

It will be adding a Colonial Marshal Bureau ERT, a Colonial Marshal
Bureau Inspection Team, and an Anchorpoint Station ERT.

First: Anchorpoint Station, unlike many ERTs, this one will hail from a
station. The station is located in the Neroid Sector and is used as a
transit / refinery station. It's large enough to hold 3000 but never
reaches its full potential. It consists of four towers and a central
module - one of the towers houses a permanent CMB presence and in the
same tower, a contingent of Colonial Marines is onboard. There's also a
Seegson office but I didn't do anything with it here.
Reference: https://avp.fandom.com/wiki/Anchorpoint_Station

For standard inspections, a dropship is dispatched from Anchorpoint
Station to the USS Almayer to carry out their objectives.
I do expect this to be the primary usage of this entire PR, because
there was always a part lacking for Anti-Corporate/Anti-Smuggling/CMB
type of interactions. It was almost always focused on Corporate, or
USCM. Nothing else. You should consider this to be an HRP addition to
the game.

Its also important to note that the Colonial Marshals are **Colonial**
and UA law enforcement agents / investigative functionaries. **They
shouldn't be enforcing Marine Law** unless: 1. The CMP/aCO has requested
it, 2. The Colonial Marshal believes its in the best interest of the CMB
and 3. The CMB Office at Anchorpoint(admins) does not intervene to
change this decision. Jurisdiction is another interaction that will be
nice to see. Non-USCM suspects should be transferred to the CMB, and
vice versa. The CMB should also be handling crimes, especially with the
ICC, involving smuggling, black market activities, and corporate
corruption/cover-ups.

**The Colonial Marshal** - He leads the team, and should be an
experience player with some knowledge of the lore behind what they are
doing. There's objectives and a backstory to help guide players if they
are unaware.
**The CMB Investigative Synthetic** - Unlike what you would expect from
most Synthetics, this one(as the name implies) is purely for
investigative and/or law enforcement purposes, though they have brought
along a medical belt.
**The CMB Deputy** - Working under the lead of the Marshal, his loyal
deputies uphold Colonial Law, Earth Law, and help with investigations
and/or law enforcement should it be needed.
**Interstellar Commerce Commission Corporate Liaison** - This Executive
works with the Colonial Marshals specifically to observe proper trade
practices and investigate any possibilities of smuggling or black market
activity. They are also an advisory agent to the Marshals by giving them
an eye on the corporate side of things.
**Interstellar Human Rights Observer** - Through a lot of hard work, the
Observer has managed to make his way onto the frontier to document and
record any kind of atrocities that may be occurring in this dark sector
of space. It's a bit of a PR stunt, but the Observer might surprise you.
Also, in an emergency, the Observer may be able to provide medical aid
for the team - they are the most capable of it.


For Emergency Responses, a nearby dropship which was enroute to an
investigation of its own, is re-routed to the USS Almayer's distress
beacon. There is a 10% chance of this happening.
They will not fare very well in extended combat, because they are not
prepared for it. They simply come aboard to lend a helping hand to a
distress beacon.
As the Colonial Marshals are equipped for law enforcement and
investigations, they are comparably lightly armed to most things they
might encounter in or by the USS Almayer.

This is where the contingent of Colonial Marines in Tower 4 comes in.

The third ERT that may be called in is an Anchorpoint Station QRF Team.
Canonically this is purely used when a random-beacon is answered by the
CMB Patrol Team, and they are able to raise the radio back to base to
call in the QRF. Thus giving them an additional, albeit optional
objective. This is controlled entirely by admins, as the Anchorpoint QRF
Team, despite its small size and average skill levels, is equipped with
a decent amount of gear compared to the depleted stocks of the USS
Almayer. Should the CMB team be able to raise its own distress signal to
the preparing QRF team, admins may choose to grant, delay, or deny the
QRF entirely.



Those are the main points of the PR.
There are also small variation changes to CMB-related survivors and also
some changes to synths.dm. (I tried to refractor the code because the
last PR to it bugged out the way items spawn in, but I was unsuccessful
and those changes are not in this PR.)

Pizza ERT chance and Freelancer ERT chance was nerfed by 4 and 5
respectively. This gives room for this ERT, and also Pizza was a bit
LRP.. You see a ship burning with a giant hole in it and you go to
deliver a pizza...?

EDIT: Pizza ERT removed from rotation entirely a la morrow

I would love to give a great thanks to:
nauticall - for their awesome cap and badge sprites! Also they have just
been a great help to me for much of my time here :)
kitsunemitsu - for their CMB hud icons!
harryOB - for helping me with fixing my vars and procs in the main ERT!
I was able to make things a % chance thanks to him.
and forest2001 - for helping me troubleshoot and find a solution for a
really annoying piece of hud code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is a great, non-combat ERT and extremely HRP addition which adds a
phenomenal avenue of RP to the game rarely seen before. There is someone
to investigate the CL, interact with survivors, give MPs someone to talk
to, take non-USCM prisoners, assist with CMB-survivors and especially
with the new Black Market update this ERT will have tons of potential to
bring really interesting dynamics to the Almayer. The Colonial Marshal
Bureau are a HRP oriented set of roles, perfect for mini-events.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>
I have done extensive testing with this and believe I have figured out
pretty much every single bug. One thing I was not able to test was the
ERT messages for obvious reasons, but they seem to be sound - and a test
merge will definitely double check that.

In addition, there may or may not be a bug where the CMB cannot see
their own HUD Icons, but ghosts can just fine. I haven't been able to
find the cause of this yet.

https://media.discordapp.net/attachments/1042176396711170119/1064156692050358372/image.png</summary>

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

:cl: QuickLoad, nauticall, Kitsunemitsu, harryOB, forest2001
add: Introducing the Colonial Marshal Bureau Inspection and Emergency
Response Teams - A Law Enforcement & Investigative UA Functionary which
brings with it an HRP oriented set of roles perfect for your anti-corpo,
colonial, prisoner, smuggling, or other types of interactions on the
Almayer! It should unlock a very unique avenue of RP for many players,
especially smugglers, CL, survivors and the black market. This is a well
supported faction with their own frequencies, equipment, even faxes and
icons etcetera. The laws of the Earth stretch beyond the Sol.
add: Added the Anchorpoint Station Emergency QRF - A team of Colonial
Marines dispatched from Anchorpoint Station to respond to the CMB's
distress signal. Few in numbers, average in skills, but well equipped.
When things get dicey for the Marshals, they are the cavalry. This is an
admin call but makes it into an optional two-part ERT.
imageadd: Awesome looking CMB Cap, Marshal Badge and Deputy Badge by
nauticall!
imageadd: HUD Icons for each of the Colonial Marshal Bureau
Investigation Members, made by Kitsunemitsu!
imageadd: CMB key, hudsec and earpiece! Comes with a nice blue shale
radio color.
qol: Switched up some of the bugged synth loadouts, added some variety.
fix: Corrects the legacy path of hudsec where it was looking for old
paths instead of the updated ones - hudsec should work fine now. Thanks
to forest for his help in spotting these.
tweak: Superficial changes to cryo ERT loadout and CMB-relevant survivor
loadouts.
tweak: Superficial changes to armor vest so that they can carry
guns/lights.
tweak: Superficial changes to not being able to put on vests over
certain uniforms.
tweak: Freelancer ERT chance down from 25 to 20.
tweak: Synthetic vendor has some packs renamed for clarity, and receives
the tech welder satchel and medical satchel as an option.
del: Synthetic nurse hat is gone from Synthetics!
del: Pizza ERT is removed from rotation
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: naut <55491249+nauticall@users.noreply.github.com>
Co-authored-by: naut <nautilussplat@gmail.com>

---
## [michaelhelvey/django-goblincore-stack](https://github.com/michaelhelvey/django-goblincore-stack)@[70f93fdfd6...](https://github.com/michaelhelvey/django-goblincore-stack/commit/70f93fdfd65d838ed77e1d0c0c500175c8f43239)
#### Saturday 2023-04-08 21:00:16 by Michael Helvey

remove hotwired (for now)

Turbolinks is just way more trouble than it's worth, at least for now -- I'd rather solve this problem through appropriate caching / JS code splitting.  If we're loading so much shit in the head that it's a problem, honestly we have bigger problems to deal with than anything turbolinks can fix.

---
## [Willenbrink/dream](https://github.com/Willenbrink/dream)@[6c4ed2dff2...](https://github.com/Willenbrink/dream/commit/6c4ed2dff220f7374673a70f3a3b0d45be3787ab)
#### Saturday 2023-04-08 21:16:32 by Sebastian Willenbrink

Initial port to Eio

This is a proof-of-concept port of Dream to Eio. Most of the public API
in dream.mli has been changed to no longer use promises and the main
tutorial examples (`[1-9a-l]-*`) have been updated and are working.
The documentation mostly hasn't been updated.

Internally, it's still using Lwt in many places, using Lwt_eio to
convert between them.

The main changes are:

- User code doesn't need to use lwt (or lwt_ppx) now for Dream stuff.
  However, the SQL example still uses lwt for the Caqti callback.

- Dream servers must be wrapped in an `Eio_main.run`.
  Unlike Lwt, where you can somewhat get away with running other
  services with `Lwt.async` before `Dream.run` and relying on the
  mainloop picking them up later, everything in Eio must be started
  from inside the loop. Personally, I think this is clearer and less
  magical, making it obvious that Dream can run alongside other Eio
  code, but obviously Dream had previously made the choice to hide
  the `Lwt_main.run` by default.

- `Dream.run` now takes an `env` argument (from `Eio_main.run`),
  granting it access to the environment. At present, it uses this
  just to start `Lwt_eio`, but once fully converted it should also
  use it to listen on the network and read certificates, etc.

Error handling isn't quite right yet. Ideally, we'd create a new Eio
switch for each new connection, and that would get the errors. However,
connection creation is currently handled by Lwt. Also, it still tries to
attach the request ID to the Lwt thread for logging, which likely won't
work. I should provide a way to add log tags to fibres in Eio.

Note: `example/k-websocket` logs `Async exception: (Failure "cannot write to closed
writer")`. It does that on `master` with Lwt too.

---
## [nednaZ/Monkestation2.0](https://github.com/nednaZ/Monkestation2.0)@[8d7db532c0...](https://github.com/nednaZ/Monkestation2.0/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Saturday 2023-04-08 21:22:50 by Bloop

Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#74143)

## About The Pull Request

This is a followup PR to
https://github.com/tgstation/tgstation/pull/73866

Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19991

I had suspected the nutrition loss slimes experience alongside blood
regen might necessitate some tweaks down the line and here we are. This
PR has two parts.

---

**PART I:** _Reworking the blood deficiency quirk backend_

As it is, blood drain from the blood deficiency occurs in the quirk's
subsystem process() call asynchronously to Life(), where the blood regen
occurs.

This results in the blood volume fluctuating constantly, making it
difficult to really make sense of readings and potentially introducing
race conditions. This PR changes that.

The blood deficiency quirk no longer processes and instead has a proc,
`lose_blood(delta_time)`, which is called in the `handle_blood()` proc
at the same time blood gets regenerated.

Added a `get_quirk` proc to help with this, so that we only have to
iterate through the quirks list once for each mob (rather than calling
has_quirk, then locate in quirks... etc).

Added a `TRAIT_BLOOD_DEFICIENCY` to further optimize the code.

---

**PART II:** _Some fine tuning of the slime blood deficiency quirk_

Slime regen works a bit differently than humans such that if they lose
-any- blood whatsoever, they will also lose nutrition. This means that
even if hooked up to an IV they will still become starving rather
quickly. A bit -too- quickly.

Instead, now the hunger does not kick in until `blood_volume` reaches
550. This means that if a slime with the blood deficiency quirk is
hooked up to an IV with say, welding fluid, and has over 150 nutrition,
they will regen blood faster than they lose it from the blood deficiency
quirk. Once they get to over 550 `blood_volume`, they will stop losing
hunger (from blood regen, anyway--normal hunger rate still applies).

So essentially this just allows slimes with the blood deficiency quirk
to be able to function so long as they stay hooked up to their IV's (or
chug welder fluid/some other toxin), which is the intended purpose of
the quirk.

Edit: As a bonus I added new blood bags for the exotic blood types, and
added a proc `update_mail_goodies` which updates the blood deficiency
quirk's mail goodies accordingly (crewmembers with blood deficiency get
sent blood bags, now they will get the correct type if their species
changes). While I was in these files I changed any immediate single
letter vars I could find and cleaned up what I could.


![image](https://user-images.githubusercontent.com/13398309/226739179-a21790e3-0be6-423a-be89-8d2cb84f6149.png)


<details>
<summary>The new blood packs</summary>


![image](https://user-images.githubusercontent.com/13398309/226743543-29fca53d-b3d1-4903-9706-35b2c00bbe78.png)

</details>

## Why It's Good For The Game

-This is arguably a more performant option than before, and fixes race
conditions from `Life()` and `quirk/blooddeficiency/process()` fighting
with one another.

-Adjustments to slime blood deficiency will enable it to function as
intended.

-It is now easier to read health analyzer blood volume readings for
blood deficient mobs.

-Now the correct blood packs are sent in the mail.

## Changelog

:cl:
qol: adjusted the blood deficiency quirk for slimepeople to not cause
excessive hunger as long as blood volume is kept above 550 via an IV
drip (or other means of getting welding fluid/some other toxin etc into
the bloodstream, e.g. ingestion)
qol: speciees with exotic blood types will now receive the correct blood
bag in the mail from having the blood deficiency perk
add: adds new blood bag types: TOX (slimepeople), H2O (podpeople), S
(snail)
fix: fixed blood deficiency quirk causing wild fluctuations in blood
volume on the analyzer, giving more accurate readings
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [NexIsDumb/FNF-PsychEngine](https://github.com/NexIsDumb/FNF-PsychEngine)@[b64eb2018d...](https://github.com/NexIsDumb/FNF-PsychEngine/commit/b64eb2018d27bec508fce3294f23ec86701a9cbc)
#### Saturday 2023-04-08 22:23:54 by ⍚~Nex

making this commit to restart the checks

i hate my life

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[613c4a6be5...](https://github.com/Jolly-66/JollyStation/commit/613c4a6be5f87b22ce0f0d39fb707e4713674e46)
#### Saturday 2023-04-08 23:56:22 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors Suiciding Variable Into Trait (#5017)

Original PR: https://github.com/tgstation/tgstation/pull/74150
-----
## About The Pull Request

Firstly, this var was on `/mob`, even though only `/mob/living` and
`/mob/dead` could have ever used it, so who knows how much needless
memory it was consuming on stuff such as `oranges_ear` that would never
ever ever use something like this.

Edit: okay instead of memory it just polluted variable edit windows for
all /mob when it didn't need to. I like having a slim VV window

Secondly, it's a technical improvement over the previous system as we
are able to "track" where a suicide originates from, and how we can
track that from mob-to-mob-to-mob. Previously, the boolean `suiciding`
would only inform us if they had ever been connected to a mob that had
ever committed suicide, but now we are able to precisely determine which
mob gave them the trait that they must now apparently bear until the
round restarts.

## Why It's Good For The Game

Less memory usage, more indepth ability to track suicides in case you
really need that dexterity. Currently no implemented code could benefit
from using it, but it would be pretty neat if someone could figure out a
way to have someone be guilt-tripped whenever they look into a mirror
and seeing the reflection of their past life? This PR won't actually
help you code that and it'll probably require a bit more work, but it's
a possibility of some cool interactions you can do when you have this
information available to you.


![image](https://user-images.githubusercontent.com/34697715/226506321-550c37e7-5de8-4f9f-9ceb-4bf9b1052597.png)

## Changelog

:cl:
refactor: Some aspects of how we track suicides from your living mob to
your observer have changed- please do let us know if anything has broken
via a GitHub Issue Report.
/:cl:

There's probably some technical improvements that can be made in some
parts of the code I reworked to accommodate this change, do let me know
if you spot any easy ones (or fuckups). a lot of excess comes from the
fact that any step in the TRAIT framework trusts that you are passing in
a valid datum (or subtype) so that's a thing

---------

Co-authored-by: san7890 <the@san7890.com>

---

