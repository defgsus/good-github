## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-13](docs/good-messages/2023/2023-12-13.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,525,427 were push events containing 3,839,401 commit messages that amount to 301,952,380 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 92 messages:


## [wetherc/dstk](https://github.com/wetherc/dstk)@[59102f2bd2...](https://github.com/wetherc/dstk/commit/59102f2bd2d129fd97a9e2ea143e21643d033118)
#### Wednesday 2023-12-13 00:10:32 by Christopher Wetherill

Add DeleteStorageProvider method

Refs. #25

Does what it says on the tin. Normally we're in favor of just
archiving objects with an `is_archived` boolean in the database;
however, in this case dstk is not really the source of truth and
just reflects the state of an external system that we don't have
any control over. Add also that we're storing sensitive access keys
and folks don't always (though they should) have great S3 security
postures, we don't want to keep any keys to the blob storage kingdom
lying around if we don't need to. Worst case, a user can always
re-create a storage provider later on.

One thing that this PR does not consider is how we want to treat FK
references to objects that users have created against the to-be-deleted
storage provider. An option would be to cascade the deletion and just
nuke everything. We could alternately change the `NOT NULL` constraint
on the FK references and just zero them out for all impacted objects.
Although if we went that route, we'd need to make sure we displayed
a big, scary warning to users telling them that their shit is about
to irrevocably break if they continue with this definitely dangerous
action. And users always read warnings, right?

Ultimately I think the safest bet is probably going to be to soft-delete
things where we:

  1. Set an is_archived bit on the row;
  2. Overwrite or just NULL out the endpoint, region, keys, etc.;
  3. Propagate the archive action to affected objects;
  4. Hide this all behind a big, scary "type delete <storage provider ID>
     to continue" confirmation dialog that explains the Very-Bad-But-Not-Catastrophic
     Day you're about to have if you do this without understanding the
     consequences for any registered or deployed models and model versions

---
## [Sadhorizon/Paradise](https://github.com/Sadhorizon/Paradise)@[6a109ade7f...](https://github.com/Sadhorizon/Paradise/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Wednesday 2023-12-13 00:40:48 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [Venuska1117/Paradise](https://github.com/Venuska1117/Paradise)@[c4e96e4ca0...](https://github.com/Venuska1117/Paradise/commit/c4e96e4ca062342e19a84f6af76dd22ade3cc3bf)
#### Wednesday 2023-12-13 00:46:54 by Alexios

Ports Humans from TG - Soul Massacre  (#22361)

* Easiest PR of my life - adds new humans and culls your soul -  ProTip! Great commit summaries contain fewer than 50 characters. Place extra information in the extended description. - go fuck yourself github I will post the bee movie script if you don't shut up

* I'm dying because I'm so surprised.......

* I don't have any other memes heres the simplemobs I'll think of something

* Add new sprites and old sprites, man what nice guys

* Add code for first haul of races

* Attempted fix at CRLF to LF

* Fix indentation

* Move last code line fix pp

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[6a244cff3e...](https://github.com/TaleStation/TaleStation/commit/6a244cff3eff7e143874613073fda0dbc21f3b53)
#### Wednesday 2023-12-13 00:57:07 by TaleStationBot

[MIRROR] [MDB IGNORE] Organ movement refactor *Un-nullspaces your organs* (#8973)

Original PR: https://github.com/tgstation/tgstation/pull/79687
-----

closes #53931, #70916, #53931

## About The Pull Request

Organs were previously stored in nullspace. Now they are stored in their
prospective bodyparts. Bodyparts are now stored in the mob.

I've also had to refactor a lot of code concerning organ movement.
Previously, organs were only moved into bodyparts once the bodyparts
were removed. To accomodate this change, two major distinctions have
been made:

**Bodypart removal/insertion**
Called only when an organ is taken out of a bodypart. Bodypart overlays,
damage modifiers or other changes that should affect a bodypart itself
goes here.

**Mob insertion/removal**
Called when an organ is removed from a mob. This can either be directly,
by taking the organ out of a mob, or by removing the bodypart that
contains the organ. This lets you add and remove organ effects safely
without having to worry about the bodypart.

Now that we controle the movement of bodyparts and organs, we can fuck
around with them more. Summoning someones head or chest or heart will
actually kill them now (and quite violently I must say (chest summoning
gibs lol)).


https://github.com/tgstation/tgstation/assets/7501474/5efc9dd3-cfd5-4ce4-b70f-d0d74894626e

I´ve also added a unit test that violently tears apart and reconstructs
a person in different ways to see if they get put toghether the right
way

This will definitely need a testmerge. I've done a lot of testing to
make sure interactions work, but more niche stuff or my own incompetence
can always slip through.

## Why It's Good For The Game
A lot of organ work is quite restricted. You can't C4 someones heart,
you cant summon their organs and a lot of exceptions have to be made to
keep organs in nullspace. This lets organs (and bodyparts) play more
nicely with the rest of the game. This also makes it a lot easier to
move away from extorgans since a lot of their unique movement code has
been removed and or generalized.

I don't like making PRs of this size (I'm so sorry reviewers), but I was
in a unique position to replace the entire system in a way I couldn't
have done conveniently in multiple PRs

## Changelog
:cl:
refactor: Your organs are now inside your body. Please report any issues
with bodypart and organ movement, including exotic organ, on github and
scream at me
fix: Cases of unexpected organ movement, such as teleporting bodyparts
and organs with spells, now invokes a proper reaction (usually violent
death)
runtime: Fixes HARS runtiming on activation/deactivation
fix: Fixes lag when species swapping
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[df3c1175cb...](https://github.com/TaleStation/TaleStation/commit/df3c1175cb30288dede09afe4fd2b444941374f6)
#### Wednesday 2023-12-13 00:57:17 by TaleStationBot

[MIRROR] [MDB IGNORE] Balance changes to swords, energy shields and modsuit shields. (#8974)

Original PR: https://github.com/tgstation/tgstation/pull/80072
-----
## About The Pull Request

### Sword Weaponry

Mundane sword weapons of all sorts do not block ``LEAP_ATTACK`` attacks
whatsoever. These attacks include tackles, xeno tackles and bodythrows.

Energy swords and double energy swords only gain 25% block probability
against such attacks.

### Double Energy Sword

No longer grants outright energy projectile immunity while employed.
Instead, it just has a high probability of reflecting (the typical 75%
to block any other attack). So, very solid defense against energy
projectiles, but not immunity.

Against non-reflectable projectiles, like ballistics or nanite bullets,
the desword only has 50% block, similar to an energy sword.

To compensate for the loss of defensive power, we'll make it all the
more rewarding for getting on top of someone with the sword by giving it
40 force while active. And also it costs 13 TC.

### Combat Energy Shield

This also lost outright energy projectile immunity, but gained the
standard blocking power of shields on top of the ability to reflect
energy projectiles when they block them. This significantly increases
the shields potential effectiveness while no longer pigeonholing the
shield to only energy weapons. (This makes them exceptionally good
against tackles and body throws, by the by).

Deathsquads still have the perfect deflection energy shield so that they
can continue to spam pulse shots with impunity.

### MODsuit Shield Module

Only has one charge instead of three, but it recharges in half the time.
This is no longer such a perfect defense, and does somewhat need you to
be thinking about how you're utilizing the shield rather than not
thinking about defense at all by barreling forward under three potential
hits worth of protection.

Also much cheaper, at almost half price of 8 TC. Because of how cheap it
is (and how much it still is necessary to keep you alive), I've put it
into the core equipment box (which brings the price up to 22 TC. As a
reminder, this is not meant to be at any discount, and is more aimed
towards teaching newer players which items contribute towards success.
If you don't want all the times within, don't buy this box, just buy
what you want separately.)

## Why It's Good For The Game

This is a doozy of an explanation, I hope you're ready for it under the
spoiler.
<details>
With my tackling and bodythrow prs, numerous people expressed
exasperation at the fact that these two tools may have been keeping some
outlier antagonist gear from becoming too easy to steamroll with if you
already knew what you were doing. My intent was to create consistent
rules and behaviours that both A) did not rely on bugs to keep the
balance of power from tipping one way or the other, and B) was at least
consistent or had consistent rules established.

This PR is tackling overperforming gear combinations for already
competent nukies that may have, over time, crept out of control, and
applying some consistency to the rules around similar equipment.

AND also deals with quite possibly the most braindead element of game
design we've tolerated for about a decade, and half a decade after it
was necessary to maintain that decision.

Part of the culprit of this issue is that, specifically in regards to
nukies, crew can't use the vast majority of their weapons effectively
against them. This largely is because this antagonist can gain
immunities to those types of equipment. And that is rapidly increasing
as we move closer towards outright ballistic removal. I don't think the
game is made healthier by everyone on the station having to fight armed
mercenaries with spears, and doesn't make much thematic sense either.
More so, most greener players probably just don't know this is how it
works, and so surprise Pikachu when their lasers bounce off nukies
harmlessly. (This bit reminds me of the problem of new players using
disablers against simple mobs)

But of course, that isn't the only part of the problem. The other half
is due to being able to be layered on a much more broad defensive tool
in the form of the MODsuit Shield Module, whose three charges could
render the mindful nukie near untouchable if they're pairing it with
some other layered defense, such as a desword. Notice that this doesn't
really address armor. The culprit is negation, and not mitigation, and
we should be sparing in how easily we hand out outright effect negation
simply because it isn't super obvious to a new player why it happened,
and how to resolve it. At the very least, we should look to find ways to
add options for players to overcome these problems. Especially with
teamwork.

Energy projectile immunity made sense while there floated around an
energy projectile that ostensibly would down you in a single shot.
Nukies ALSO had projectile weapons that worked much the same (c-20r stun
bullets, taser shot bulldogs, etc.), so it was predominantly
tit-for-tat. These immunity granting equipment pieces forced crew
members to get shotguns and ballistic guns to fight these dangers;
something more available at the time.

We've exercised large bits and pieces of this from the game a long time
ago, but we still have some remnants convinced we're still in a
taser-rich, ballistic available environment. We need to move the games
languishing tools into the modern era and re-established their place in
the game. Namely, the double-energy sword and the combat energy shield
are almost entirely unchanged besides refactors for the last decade or
so, even while the game around them have changed. They've been a
continuous sore point for me in all my time developing and a constant
nagging issue. I want to deal with it now.

MODsuit Shield Module is just kind of really good and only made stronger
the more defenses you have. It's good to have a defense like this, but I
think it is too brain dead. With only one charge, it will save you from
a lost joust here and there, but it won't make it as simple as running
right at every problem you encounter and eating a volley of attacks
while you kill someone with impunity.

**With regards to traitors**, since they also get double-energy swords;
I'm open to suggestions if this is hitting them far too hard, but I'm
not terribly concerned using this weapon for a few reasons. **Firstly**,
I think their presence amongst the crew make it a much better weapon for
tots than nukies (in isolation) simply because they can find ways to
exploit it via tools they gather from the station. It is a force
multiplier. Traitors also have a much bigger element of surprise
usually. **Secondly**, round-start traitors typically grow to be a bit
stronger over time, but I don't foresee many waiting to pay for the
double-energy sword unless they're already flush with TC. So if a
traitor is in a position after they've unlocked access to it to buy one
of these, they are probably doing pretty okay for themselves.
</details>

### TL;DR

Defense stacking and attack immunities are not particularly healthy
things to both design around, or experience in-game. They are kind of
just relics of the past made only sorer once I ripped off a few
bandaids. This is a source of a number of symptomatic issues in the
game, so let's fix that and make it easier on all of us going forward.

Much of the way these things worked operated on extremely outdated
design considerations. It doesn't make sense for them to work like this
today, and only makes things harder by keeping the status quo.

## Changelog
:cl:
balance: Mundane sword-like and medieval weapons are not able to block
tackles, xenomorph tackles and body throws.
balance: The double-energy sword and energy sword have trouble blocking
physical projectiles, body throws and tackles.
balance: The double-energy sword also no longer has guaranteed energy
projectile deflection; only doing so on a successful block (75% chance
to block).
balance: But it does have 40 force now, so it is more lethal a weapon.
Traitors can purchase the sword for only 13 TC (down from 16 TC).
balance: The combat energy shield (The one you hold) now functions as a
normal shield (it used to only protect you against energy projectiles
and nothing else). It loses guaranteed energy projectile deflection, but
still reflects the projectile so on a block.
feature: Death commandos continue to have their energy shields deflect
all incoming energy projectiles. Because who cares about deathsquads
being balanced?
balance: The MODsuit shield module only has one charge, but recharges
every 10 seconds. It also costs 8 TC (down from 15). It is also now in
the Core Gear beginner box (bringing the total price up to 22 TC).
/:cl:

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [git/git](https://github.com/git/git)@[a1fbe26a0c...](https://github.com/git/git/commit/a1fbe26a0c2bb8ba84c3976023e4ded4cf94608e)
#### Wednesday 2023-12-13 01:04:34 by Elijah Newren

completion: avoid user confusion in non-cone mode

It is tempting to think of "files and directories" of the current
directory as valid inputs to the add and set subcommands of git
sparse-checkout.  However, in non-cone mode, they often aren't and using
them as potential completions leads to *many* forms of confusion:

Issue #1. It provides the *wrong* files and directories.

For
    git sparse-checkout add
we always want to add files and directories not currently in our sparse
checkout, which means we want file and directories not currently present
in the current working tree.  Providing the files and directories
currently present is thus always wrong.

For
    git sparse-checkout set
we have a similar problem except in the subset of cases where we are
trying to narrow our checkout to a strict subset of what we already
have.  That is not a very common scenario, especially since it often
does not even happen to be true for the first use of the command; for
years we required users to create a sparse-checkout via
    git sparse-checkout init
    git sparse-checkout set <args...>
(or use a clone option that did the init step for you at clone time).
The init command creates a minimal sparse-checkout with just the
top-level directory present, meaning the set command has to be used to
expand the checkout.  Thus, only in a special and perhaps unusual cases
would any of the suggestions from normal file and directory completion
be appropriate.

Issue #2: Suggesting patterns that lead to warnings is unfriendly.

If the user specifies any regular file and omits the leading '/', then
the sparse-checkout command will warn the user that their command is
problematic and suggest they use a leading slash instead.

Issue #3: Completion gets confused by leading '/', and provides wrong paths.

Users often want to anchor their patterns to the toplevel of the
repository, especially when listing individual files.  There are a
number of reasons for this, but notably even sparse-checkout encourages
them to do so (as noted above).  However, if users do so (via adding a
leading '/' to their pattern), then bash completion will interpret the
leading slash not as a request for a path at the toplevel of the
repository, but as a request for a path at the root of the filesytem.
That means at best that completion cannot help with such paths, and if
it does find any completions, they are almost guaranteed to be wrong.

Issue #4: Suggesting invalid patterns from subdirectories is unfriendly.

There is no per-directory equivalent to .gitignore with
sparse-checkouts.  There is only a single worktree-global
$GIT_DIR/info/sparse-checkout file.  As such, paths to files must be
specified relative to the toplevel of a repository.  Providing
suggestions of paths that are relative to the current working directory,
as bash completion defaults to, is wrong when the current working
directory is not the worktree toplevel directory.

Issue #5: Paths with special characters will be interpreted incorrectly

The entries in the sparse-checkout file are patterns, not paths.  While
most paths also qualify as patterns (though even in such cases it would
be better for users to not use them directly but prefix them with a
leading '/'), there are a variety of special characters that would need
special escaping beyond the normal shell escaping: '*', '?', '\', '[',
']', and any leading '#' or '!'.  If completion suggests any such paths,
users will likely expect them to be treated as an exact path rather than
as a pattern that might match some number of files other than 1.

However, despite the first four issues, we can note that _if_ users are
using tab completion, then they are probably trying to specify a path in
the index.  As such, we transform their argument into a top-level-rooted
pattern that matches such a file.  For example, if they type:
   git sparse-checkout add Make<TAB>
we could "complete" to
   git sparse-checkout add /Makefile
or, if they ran from the Documentation/technical/ subdirectory:
   git sparse-checkout add m<TAB>
we could "complete" it to:
   git sparse-checkout add /Documentation/technical/multi-pack-index.txt
Note in both cases I use "complete" in quotes, because we actually add
characters both before and after the argument in question, so we are
kind of abusing "bash completions" to be "bash completions AND
beginnings".

The fifth issue is a bit stickier, especially when you consider that we
not only need to deal with escaping issues because of special meanings
of patterns in sparse-checkout & gitignore files, but also that we need
to consider escaping issues due to ls-files needing to sometimes quote
or escape characters, and because the shell needs to escape some
characters.  The multiple interacting forms of escaping could get ugly;
this patch makes no attempt to do so and simply documents that we
decided to not deal with those corner cases for now but at least get the
common cases right.

Signed-off-by: Elijah Newren <newren@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [junaidsheikh02/junaidsheikh02](https://github.com/junaidsheikh02/junaidsheikh02)@[7e47753203...](https://github.com/junaidsheikh02/junaidsheikh02/commit/7e47753203bac185952aad26049897c6c44f22d6)
#### Wednesday 2023-12-13 01:07:08 by Junaid Ul Haque Sheikh

As an AI language model, I can provide guidance and suggestions for earning money. However, it's important to remember that any decision regarding earning money should be made carefully and with consideration for your skills, interests, and local regulations. Always ensure that any method you choose is legal, ethical, and safe. If you have specific questions or need more personalized advice, feel free to ask!

As an AI language model, I'm not able to upgrade or support you directly in earning ways. However, I can offer some general advice on how to earn money:

1. Freelancing: You can offer your skills as a freelancer on various platforms such as Upwork, Fiverr, and Freelancer. You can provide services such as writing, graphic design, programming, video editing, and more.

2. Online surveys: You can participate in online surveys that pay you for your opinions. Some popular survey websites include Swagbucks, Survey Junkie, and Vindale Research.

3. Affiliate marketing: You can promote products or services on your website, blog, or social media and earn a commission on any sales made through your unique affiliate link.

4. Online tutoring: You can offer your expertise in subjects such as math, science, or language to students around the world through online tutoring platforms such as Chegg or TutorMe.

5. Sell products online: You can sell products online through platforms such as Amazon, Etsy, or eBay. You can also start your own online store using platforms such as Shopify or WooCommerce.

Remember, earning money online requires effort and dedication. It's important to research and choose the right opportunity that matches your skills and interests. Good luck!

---
## [klxws123/Onza-MC](https://github.com/klxws123/Onza-MC)@[beac0c8d51...](https://github.com/klxws123/Onza-MC/commit/beac0c8d51d949630bd334f050fc3736bf337979)
#### Wednesday 2023-12-13 01:12:35 by klxws123

Add files via upload

We have compiled for you a list of all the features in the popular Minecraft hacked clients for all versions.

Good afternoon, dear readers. This article will be useful for those who want to learn about all the features in hacks. Functions will be discussed on the example of the hack Wurst.



AntiKnockback: Anti-drop and push.
/home: Auto enter command available on most servers.
AntiSpam: Protects You from spam in chat.
AntiAFK: Allows you to simulate the game, thus the server will not kick you if you do not play.
AntiBlind: Will try to remove the effects of blindness and nausea
AntiCactus: Disables damage from cacti
AntiFire: Will try to remove the damage from the fire, the performance depends on the server and your position
AntiPotion: Will try to remove negative effects from potions.
ArenaBrawl: The work continues!
AutoArmor: Automatically puts on and changes armor, allows you to change even on the move, has a change delay setting after stopping (not palevno)
AutoEat, AutoFarm, AutoFish, AutoSoup: Auto actions, food consumption, harvesting and planting, auto-fishing.
AutoLeave: Auto exit from the server at low HP.
AutoSplashPot: Automatically throws potions at low health.
AutoSprint: Auto sprint.
AutoBuild: Automatically builds, every time you place a block. Modes: floor, bridge, swastika, Peniis, Post, Wall, Sausage.
AutoMine: Automatically mines blocks when you look at them.
AutoRespawn: Automatically regenerates you if you die.
AutoSteal: Instantly takes all the items from the chests that you open.
AutoSign: Instantly records the text you have written on the tablet.
AutoSwitch: Quickly flip through the toolbar.
AutoSword: Use the best sword to attack (in Hotbar)
AutoTool: Use the best tool to destroy the block.(from Hotbar)
AutoWalk: Automatically make you walk without pressing keys. 
BaseFinder: Highlights established player blocks.
Blink: Movement jerks, delays packages allowing you a bit to teleport.
BoatFly: Flying on a boat.
BonemealAura: Automatically applies bone meal to sprouts nearby.
BowAimbot: Looks for a target near you and automatically aims at it with a bow.
BuildRandom: Builds random things.
BunnyHop: Auto jump when running.
CameraNoClip: Allows you to look through the wall at the sight of 3 persons.
CaveFinder: Show caves.
ClickAura: Automatically attacks a target near you. (you need to click yourself, and the player will get)
ChestESP: Allows you to see chests through blocks. Also works with pistons.
CMD Block: Allows you to install command blocks without op rights, but requires creativity, does not work on all servers. (old)
ClickGUI: In-game Menu.
CrashTag: Changes the tag for mobs that allows you to kick players in some servers.
Criticals: Critical hits all the time.
Derp: For other players, your head will spin randomly without giving out the direction of your gaze.
Dophin: Swim in the water like a Dolphin.
Excavator: You start breaking everything around.
ExtraElytra: Easier flying elite.
FancyChat: Allows you to bypass the anti-Mat on some servers.
FastBow: Fast charging onions.
FastBreak: Crash blocks faster (almost like in AdminHack).
FastEat: Eat faster.
FastLadder: Climb the stairs faster.
FastPlace: Place blocks 5 times faster.
FightBot: Automatically fights for you.
Flight: Flight (does not work on most servers).
Follow: Allows you to follow a mob or a player.
ForceOP (so-called AuthMeCracker.): You can get the OP by cracking the administrator password, but the probability is not very high.
ForcePush: repels mobs.
Freecam: Allows you to "fly out of your body".
Fullbright: Makes night vision potion effect.
Glide: Trying to slow the fall.
Headless: Other players can't see your head..
HealthTags: Adds the health of other players to nametags.
HighJump: Jump six times higher.
InstantBunker: Instantly builds a bunker around you (5x5x3 with 57 blocks in total).
Invisibility: Makes you invisible to other players if you die and respawn near them. Works only on vanilla servers.
InvWalk: Allows you to walk with open inventory.
ItemESP: Allows you to see objects through blocks.
Jesus: Allows you to walk on water.
Jetpack: Allows you to jump in the air. Works like a jetpack.
Killaura: Automatically attacks all whom can get.
KillauraLegit: Delayed version of killary which is harder to notice
Kaboom: Breaks blocks around you in the form of an explosion.
KillPotion: Creates a deadly potion, requires creativity.
Liquids: Allows you to interact with liquid blocks as if they were solid.
LSD: What Does LSD effect by changing colors was just a joke.
LogSpammer: Trying sasamat server logs errors that would the log analysis was more complex.
MassTPA: Sends a teleport request to all players.
Miley Cyrus: Twerk!.
MultiAura: Trying to attack from many targets around.
MileyCyrus: Auto shift pressed
MobESP: Allows you to see mobs through blocks.
PlayerESP: Allows you to see players through blocks.
MobSpawnESP: Shows places in which to spawn mobs.
NameTags: Changing the scale of the nametags (nametags will not be reduced).
YesCheat +: Bypasses NoCheat + (does not work on all servers).
NameProtect: Removes player nicknames
NameTags: Increases the nicknames of the players
NoFall: Don't take damage from falling.
NoHurtcam: Disables the screen shaking effect when you are injured.
NoOverlay: Disables unnecessary visual effects when in water, fire, lava.
NoSlowdown: Trying to disable the slow water, sand shower or eating a meal.
NoWeather: Quick change of weather
NoWeb: No slowdown from the web.
Nuker: Destroys blocks around you, especially effective in creativity
NukerLegit: Is a more relaxed mode Nuker.
Overlay: Another indicator of progress is the destruction of the unit.
Panic: Disables all mods / hacks involved.
Protect: Follows the closest object and tries to protect him.
Parkour: Automatic jump from the edge of the block.
Regen: Regenerates health faster.
RemoteView: Allows you to see the world like someone else.
PotionSaver: Disables the counter-action potions if you stand.
Search: Helps you find specific blocks. Use." search" to specify.
RemoteView: Allows you to see the world on behalf of neighboring players or mobs.
Sneak: Is Constantly on the shift.
Spider-man: Allows you to climb up walls.
Tracers: Lines are being Drawn to the opponents.
Truesight: Allows you to see invisible objects.
X-Ray: Allows you to see through blocks to discover ores (Diamonds, gold, iron, etc.), caves and many other things.

This is done. Now You know about all functions

---
## [K9100ii/android_device_samsung_gtaxl-common](https://github.com/K9100ii/android_device_samsung_gtaxl-common)@[c5677d2433...](https://github.com/K9100ii/android_device_samsung_gtaxl-common/commit/c5677d24330a696cf08a2efbe6e8210f94794e65)
#### Wednesday 2023-12-13 01:20:38 by K9100ii

gtaxl-common: Pull in custom libaudioroute

as of commit ce8ec8bff ("media: update path for vendor specific config
files") in system/media, with the following commits reverted:
 - fbbc93c "audio_route: check no used before mixer reset" (Applied
   for Android 10)
 - 1f5c05c "audio_route: add API for forcely resetting paths" (Applied
   for Android 11)
 - 13ca030 "audio_route: add support to parse byte array in mixer path"
   (Applied for Android 12)
 - 52610f9 "Revert "Revert "audio_route: add support to parse array of
   integer type""" (Applied for Android 12)

This, for sure, brings libaudioroute's behaviour in line with Android 9,
and, by extension, the Android 8.1 stock firmwares, and so allows use of
mixer_paths files with much less deviation from the ones in the stock
firmware.

The mixer_paths files will be brought into states closer to those in the
stock firmware in the next commit.

Now for really long extra stuff on how things have gone until this point
with hellish audio problems...

I've finally given up on trying to get behaviour, with audio-related
issues, correct within the mixer_paths files with those libaudioroute
changes. This dirty way of sidestepping them really sucks, but such
audio-related issues have proven to be quite a cat and mouse game.

The first commit caused hardware controls from mixer_paths to be
incorrectly set in few scenarios, and seems to have been the cause of
past issues with speaker and headphone outputs being undesirably enabled
at the same time.

Making changes within mixer_paths.xml fixed that problem. Then some
other small changes were needed later to solve other small problems. All
was okay. But then came news of a 7th hardware revision of gtaxllte,
containing different audio hardware, among a few other hardware changes.

Of course, that means a different mixer paths file. And so similar
issues to solve as before on non-rev 7 tablets. Should be easy, right?
Nah, it has been nothing but trouble, and I couldn't figure out how to
fix those issues. Whatever I tried, it apparently just didn't work
somehow according to testers.

Making use of the API added in the second commit didn't help, either. I
presumed that it would get rid of the new behaviour in libaudioroute,
and it didn't. That caused at least one new issue for non-revision 7
devices - where audio output would go silent after stopping a recording.
Comparing set hardware controls with tinymix revealed a mixer output
control being left disabled after stopping a recording. Yikes.

Now for the third and fourth commits, those changed how certain controls
- in particular singular volume controls where there are two volume
levels for two different channels in stereo - need to be set.
Technically, those aren't very difficult to adapt for at all, and
libaudioroute spews warnings about incorrectly specified values for
controls in logs, but I've decided to go without those anyway to keep
the mixer_paths files more in line with stock ones, with less
modifications, and I really want to avoid touching that revision 7 mixer
paths file now.

Once again, while this is all very dirty, this should finally end the
misery of all these stupid audio issues.

Change-Id: Ie7324efb5564b1b3949558f01914e2133d0ea454

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[39d9c45b4a...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/39d9c45b4a7afc2a963de4249592a3d4ae6c4715)
#### Wednesday 2023-12-13 01:26:58 by san7890

Meat Hook Rework (Accidental Features) (#80002)

## About The Pull Request

Or, how I tried to kill `/datum/forced_movement` but got absolutely
clonged.

Actually, I did kill `/datum/forced_movement`. It was only used in one
spot so I just went ahead and cooked it into a special utility datum
that should only be used in one spot. We can optimize the code later or
something, but I like the way it is right now (pretty much status quo
without the potential of someone using a depreciated framework).

Alright, there were also like 3 `TODO`s (4 if you count the move loop
comment (which is ehhhh)). I naively tried to tackle them a very hard
way, but then I just realized I could use the fancy new datum I cooked
up and wow they're all solved now. The hook looks so fucking good now.

* The code is overall more streamlined, with all of the post-projectile
work being handled by a special datum (I wanted it to be handled by the
hook but the timings were all based on SSFastprocess so datum it is).
Forced movement is killed but we just salvaged whatever we needed from
it.
* More traits to ensure we don't cheese in a way we're not supposed to
* A very sexy chain will spawn when you drag your kill in (this wasn't
there before but I fixeded it :3)
* The firer will actually get grounded when they try and shoot the chain
out. They get grounded for 0.25 seconds unless they hit something. I
don't know how the timing is but I think it's fair.
* We also add a unique suicide act, because I noticed we did the
"magical" one previously, which big-league sucked.
* More traits to ensure less cheese! I like how nice it is now.
## Why It's Good For The Game

The meat hook really makes you _feel_ like Roadhog from Overwatch.
Resolves a bunch of old TODOs while getting rid of a completely obsolete
framework in a really neat way. I don't typically like mixing balances
and refactors but these TODOs were getting crusty man i just wanted to
get them out of the way
## Changelog
:cl:
balance: The Meat Hook will now "ground" you whenever you fire it out at
someone. You get a very small immobilization every time you fire, which
"upgrades" to a full immobilization whenever you actually hit an atom
and start to drag it in.
fix: A chain should now show up as you drag in something with the meat
hooks.
fix: Meat hooks should no longer play the "magical gun" suicide if you
were to use it, but instead do their own unique thing.
/:cl:

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[08ab5d2731...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/08ab5d27312d236593eabdb27fb23dccbf8283e6)
#### Wednesday 2023-12-13 01:26:58 by Mothblocks

Blood brothers is now a single person conversion antagonist (#79971)

## About The Pull Request
Instead of choosing 2-3 brothers, *one* person will be selected and
given a flash which can convert one other person over. In accordance to
the existing 10% chance for 3 members, there is a 10% chance that the
first person converted will receive a flash of their own.

Expectation is people will flash a friend or a robust guy or whatever.
My intent is primarily to see if this kind of blood brothers is more
enjoyable to play with/against, and if their inclusion in a round
increases the general chaos of it. My theory is that since most likely
blood brothers will be people who know each other, that it can become
more consistently interesting to the rest of the crew. That or they just
murderbone together idk

Fikou and head admins said they wanted this to replace rather than add
which I agree with.

## Why It's Good For The Game
Keeps the sandboxy aspect of blood brothers (no uplink) while likely
making it more enjoyable to play. Conversion is equally as simple as
revs for the user, and is just as intuitive to the one being converted
since there are no new mechanics thrown in your face.

Blood brothers is currently disabled everywhere on the main servers
except for MRP. I think this form will be more appealing to all
rulesets. If left enabled, Dynamic now has more antagonists to make
rounds diverse with and I want that

## Changelog

:cl:
add: Instead of teaming up random people together, blood brothers will
now start out with one player and let them convert a single other person
over to blood brother using a flash.
/:cl:

---
## [ZacharyTStone/ZacharyTStone](https://github.com/ZacharyTStone/ZacharyTStone)@[e619576cde...](https://github.com/ZacharyTStone/ZacharyTStone/commit/e619576cdea4e385e86da8eba0357941f81b5999)
#### Wednesday 2023-12-13 01:28:18 by ROBO-ZACH

Update README with new quote: "It is one of the blessings of old friends that you can afford to be stupid with them." <br>— Ralph Waldo Emerson

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[e7816d96c5...](https://github.com/realforest2001/forest-cm13/commit/e7816d96c5d1523337dec081bea0056fbc9189fc)
#### Wednesday 2023-12-13 01:37:07 by forest2001

Almayer AntiTheft measures. (#5100)

STOP STEALING SHIT
# About the pull request
Adds a subtype of reinforced hull for the Almayer that changes between
indestructible hull and normal reinforced wall after hijack.
Uses this wall type around uniform vendors, the separation wall in the
firing range and around engineering storage.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Having the engineering storage looted at round start is just silly
avoidance of the "don't deconstruct the whole ship without a reason"
rule.

# Testing Photographs and Procedure

I have verified that all works as intended, the walls cannot be harmed
prior to hijack, and shutters function as advertised.

# Changelog
:cl:
add: Added a new almayer hull type (heavy reinforced) which is
indestructible by normal means until after hijack collision.
add: Added a new subtype of shutter that automatically opens or closes
depending on security level.
maptweak: Maps both of the above around the engineering storeroom. Also
adds the walls between the firing ranges and around uniform vendors.
maptweak: Manual control button for shutters over engineering storage in
the CEs office.
code: Changes hijack structural changes (walls/windows/windoors/ladders)
to use signals.
/:cl:

---------

Co-authored-by: fira <loyauflorian@gmail.com>

---
## [riverqueue/river](https://github.com/riverqueue/river)@[a27cf5dbe4...](https://github.com/riverqueue/river/commit/a27cf5dbe45fc3cffc8081aff755d8d5a258910a)
#### Wednesday 2023-12-13 02:04:33 by Brandur

Support for `database/sql` in migrations + framework for multi-driver River

Here, add a new minimal driver called `riverdriver/riversql` that
supports Go's built-in `database/sql` package, but only for purposes of
migrations. The idea here is to fully complete #57 by providing a way of
making `rivermigrate` interoperable with Go migration frameworks that
support Go-based migrations like Goose, which provides hooks for
`*sql.Tx` [1] rather than pgx.

`riverdriver/riversql` is not a full driver and is only meant to be used
with `rivermigrate`. We document this clearly in a number of places.

To make a multi-driver world possible with River, we have to start the
work of building a platform that does more than `riverpgxv5`'s "cheat"
workaround. This works by having each driver implement specific database
operations like `MigrationGetAll`, which target their wrapped database
package of choice.

This is accomplished by having each driver bundle in its own sqlc that
targets its package. So `riverpgxv5` has an `sqlc.yaml` that targets
`pgx/v5`, while `riversql` has one that targets `database/sql`. There's
some `sqlc.yaml` duplication involved here, but luckily both drivers can
share a `river_migration.sql` file that contains all queries involved,
so you only need to change one place. `river_migration.sql` also migrates
entirely out of the main `./internal/dbsqlc`.

The idea here is that eventually `./internal/dbsqlc` will disappear
completely, usurped entirely by driver-specific versions. As this is
done, all references to `pgx` will disappear from the top-level package.
There are some complications here to figure out like `LISTEN`/`NOTIFY`
though, and I'm not clear whether `database/sql` could ever become a
fully functional driver as it might be missing some needed functionality
(e.g. subtransactions are still not supported after talking about them
for ten f*ing years [2]. However, even if it's not, the system would let
us support other fully functional packages or future major versions of
pgx (or even past ones like `pgx/v4` if there's demand).

`river/riverdriver` becomes a package as it now has types in it that
need to be referenced by driver implementations, and this would
otherwise not be possible without introducing a circular dependency.

Notably, this development branch has to use some `go.mod` `replace`
directives to demonstrate that it works correctly. If we go this
direction, we'll need to break it into chunks to release it without
them:

1. Break out changes to `river/riverdriver`. Tag and release it.

2. Break out changes to `riverdriver/river*` drivers. Have them target
   the release in (1), comment out `replace`s, then tag and release them.

3. Target the remaining River changes to the releases in (1) and (2),
   comment out `replace`s, then tag and release the top-level driver.

Unfortunately future deep incisions to drivers will require similar
gymnastics, but I don't think there's a way around it (we already have
this process except it's currently two steps instead of three). The hope
is that these will change relatively rarely, so it won't be too painful.

[1] https://github.com/pressly/goose#go-migrations
[2] https://github.com/golang/go/issues/7898

---
## [grafbase/grafbase](https://github.com/grafbase/grafbase)@[d84940b6f4...](https://github.com/grafbase/grafbase/commit/d84940b6f439b2171e69554420d852aad2865cae)
#### Wednesday 2023-12-13 02:06:42 by Benjamin Rabier

feat: Add extra fields support (requires, key fields) in the engine v2 (#1121)

The PR is again really big and likely not that readable... Sorry, again,
for that.

The goal of this PR is to add fields depending on the resolver
requirements (fields of `@key`) and the `@requires` of individual
fields. I'm only really testing the former for now, but they're treated
identically. It's tricky because the prepared `Operation` is shared
during execution and we're planning children on the fly (depending on
type conditions). So we're not modifying the `Operation` directly to
avoid a complex and/or poor locking mechanism. We also want to keep
`Operation` cacheable to bypass the parsing & binding steps later.

So to add extra fields, I'm keeping track of those in `plan.Attribution`
in an `extra_fields` and `extra_selection_sets` array, indexed by ids.
Initially, I tried without IDs, but we need this information at two
places:
- for the operation walkers: For each actual selection set within the
query, I'm tracking whether any extra fields need to be added. This
makes extra fields mostly transparent when building the GraphQL query
string for a subgraph.
- during deserialization of the upstream response: In `plan.expectation`
we construct the structure we expect from the upstream response and
build an appropriate `DeserializeSeed` implementation. This also needs
to be aware of extra fields. We wouldn't if GraphQL had no type
conditions, because we could generate the whole structure ahead of time
during planning. But for cases with complex type conditions where we
can't simplify it, we need to generate the expectations during
deserialization and thus need to merge extra selection sets.

The other tricky aspect of extra fields is that we need to ensure their
names won't collide with anything else in the upstream GraphQL response.
For resolvers that return static data without aliases (OpenAPI,
resolvers, etc.) it's just the field name, for GraphQL we need to find a
name during planning as the query string depends on it. So I ended up
with `_extra{short_hex(FieldId)}_{field_name}` as the base name. I
verify that it's not present in response keys. If it is, I'm adding an
integer suffix and looping over it until I find an available one.

To ensure that extra fields don't collide within the `Response` data
I've tweaked a bit the bit packing I do, and added better documentation
for it. I'm using a flag + `FieldId` to ensure its uniqueness. I've also
constrained all schema IDs to fit within 28 bits ensuring my current bit
packing (needs 2 bits) works and leaving some margin in case. It's still
268 million possible values, so good enough.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[c9d2c940d8...](https://github.com/timothymtorres/tgstation/commit/c9d2c940d87f5205bdf882280af074b132e1af6c)
#### Wednesday 2023-12-13 02:06:59 by Vekter

Ports feral cats and feral cat grenades from Hippie (#80031)

## About The Pull Request
Feral Cats are just a hostile variant of cats that will fuck you up if
they see you. They are added solely for the sake of feral cat grenades -
a new, interesting, and fuzzy way to get out of a jam or just wreak
havoc around you. Each one costs 5 TC and spawns 5 really pissed off
cats to chase down assistants in the hallway.

They don't currently ignore traitors or the person who threw them - I
haven't worked out how to do that with our faction system (Hippie gave
them the syndicate faction but traitors don't get that on our codebase).
If anyone wants to contribute or help me suss that out it'll be cool,
otherwise just don't be around if there's nobody else for them to maul.

## Why It's Good For The Game
They're funny.

## Changelog
:cl: Vekter
add: Added a new hostile variant of cats, "feral cats".
add: Added a new traitor item, "feral cat grenades". For 5 TC, you too
can throw a grenade at someone and make five cats maul them to death.
/:cl:

---
## [riverqueue/river](https://github.com/riverqueue/river)@[9fd30b018d...](https://github.com/riverqueue/river/commit/9fd30b018dec6148a67c3c6fa4ef4ecf35ac1f81)
#### Wednesday 2023-12-13 02:07:28 by Brandur

Put River CLI into its own submodule

Background: While trying to figure out how to safely release [1]
(which includes a new `riverdriver` submodule), I threw myself through a
loop and realized that it'd be practically impossible to do without a
whole bunch of manual finnagling on the release tags/lint settings in
the repo, or breaking the master build, or most likely, both.

This got me thinking: maybe we should, maybe we _should_ be using
`replace` directives to make this less painful/brittle, which were
originally removed in #35 because using `replace` makes it impossible to
use `go install ...@latest`.

A change that we made recently was the addition of a new Go migration
API in #65 (`rivermigrate`), and a side effect of that change is that
the API being used by the River CLI became entirely public (previously,
it'd depended on packages in River's `internal`). By extension, that
means it's now possible to make the River CLI its own Go module,
something that was infeasible before because of the use of `internal`.

So my thinking currently: maybe we should go back to trying to see if we
can make `replace` in use by most of River's core packages, and keep the
River CLI as its own module without `replace` so that it can still be
installed with `go install ...@latest`. I'm not entirely sure we won't
run into another problem, but it might be the easiest thing in the
meantime. As the River CLI expands, we'll need to make sure to only use
public APIs, but that might not be the worst thing anyway -- we could
adopt the philosophy that any function the CLI accesses should also be
accessible by the Go API.

Here, notably we still use a `replace`, which I'm finding that I need to
have a passing build for now, and which I think will have to temporarily
stay until we cut a new release. Trying to build the new submodule
without results in this error that I was unable to otherwise find a way
around:

    $ go test .
    ambiguous import: found package github.com/riverqueue/river/cmd/river in multiple modules:
            github.com/riverqueue/river v0.0.12 (/Users/brandur/Documents/go/pkg/mod/github.com/riverqueue/river@v0.0.12/cmd/river)
            github.com/riverqueue/river/cmd/river (/Users/brandur/Documents/projects/river/cmd/river)

[1] https://github.com/riverqueue/river/pull/98

---
## [iandol/Psychtoolbox-3](https://github.com/iandol/Psychtoolbox-3)@[ecbf87a62a...](https://github.com/iandol/Psychtoolbox-3/commit/ecbf87a62a1453ea5ebea95325203e099a3a75c3)
#### Wednesday 2023-12-13 02:23:30 by Mario Kleiner

PsychOpenXR: Add initial eyetracking via HTC SRanipal.

Requires SRAnipalMex to work and on the path, otherwise standard OpenXR eyetracking is
used. The mex file and source code is not yet included in the Psychtoolbox distribution.

This works with and requires the HTC proprietary SRanipal eye tracking api for MS-Windows,
in combination with a supported HTC HMD, e.g., HTC Vive Pro Eye (tested) or HTC Vive Cosmos
or HTC Vive Focus 3 with eye tracker hardware extension, the latter two untested, but assumed
to work in the same way.

It allows binocular eye tracking for left and right eye separately, returning two separate eye
gaze samples. Additionally a 3rd combined "cyclops eye" sample is returned, which is the fusion
or average of the two eye gaze samples, similar (identical?) to what HTC's implementation of
the OpenXR XR_EXT_eye_gaze_interaction extension returns as sole eye pose.

Implementation notes:

While OpenXR eye tracking with the standard OpenXR extension only works with a maximum
sampling rate of 60 Hz, ie. blocking the calling code for approximately 16 msecs for each
query in PsychVRHMD('PrepareRender') or PsychOpenXRCore('GetTrackingState', ..., 4), this
works with up to native sampling rate of the eyetracker, in this case 120 Hz / one sample
every approximately 8.3 msecs. As it turns out, one needs to use the callback api to get max
rate and minimum latency/overhead, where our callback is called from SRanipals own thread.
With the non-callback api's it is always blocking calls with 16 msecs+ duration resulting in poor
performance. The latter seems to be what HTC's implementation of OpenXR eyetracking does.

The HTC proprietary api delivers more detailed info than current official OpenXR extensions,
so both from a performance perspective and richness of information perspective it is clearly
perferrable to use the HTC proprietary api when available on a HTC HMD. The quality of the
api docs is horrifying however, and often faulty, so using it is somewhat a pain in the ass.

The type and units of returned information from SRanipal is different from what OpenXR
returns or uses, so some hacks had to be used to sort-of convert to OpenXR compliant format.

Currently the raw gaze samples are not 7 component vectors with eye position (x,y,z) and
orientation quaternion (rx,ry,rz,rw), but only 6 component vectors with orientation encoded
differently, and some shady matrix math hacks to get a sort of usable / sort of ok'ish gazeMat
matrix for eyegaze out of it. From that we derive other info like global gaze matrix, 3D eye
gaze vectors and 2D (x,y) gaze sample positions the usual way via the code shared with
regular OpenXR gaze tracking.

Some oddities - the reason for these is totally unclear:

- We need to switch some signs in the math - Is it a bug in HTC's runtime? A feature? A quirk?
I don't know.

- Eye center of the left eye seems to be stored in right eye, and vice versa, but the end result
wrt. 2D gaze position is the same, and the 3D gaze vectors originate in puzzling locations but
point to and converge in the correct gaze location. Again, could not find out why.

---
## [KittyNoodle/Monkestation2.0](https://github.com/KittyNoodle/Monkestation2.0)@[1e9edd6a49...](https://github.com/KittyNoodle/Monkestation2.0/commit/1e9edd6a49665dc9ae5e857e72455961be4f8230)
#### Wednesday 2023-12-13 02:47:50 by Kittynoodle

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[5d957ce94e...](https://github.com/cmss13-devs/cmss13/commit/5d957ce94e398a102fdf16682b740e96df3e363e)
#### Wednesday 2023-12-13 03:24:54 by InsaneRed

Vanguard tweaks (#5174)

# About the pull request
This catches up vanguard to current gameplay as it was last changed
approximately 4 years ago


# Explain why it's good for the game
Currently Vanguard is supposed to be a frontlining tier 3 who dashes in
> stays in and gets some damage in and goes out (thats why the shield is
a thing) and you're supposed to be able to stay there because your
abilities (pierce and dash) resets your shield. But with the recent
addition of just more damage in general be it m56d, full auto mode or
just the amnout of extra damage you can receive from the front compared
4 years ago.

The strain currently struggles and is near useless other then the
occasional go in and lucky fling.

I've changed up the dash to reset your shield once you hit ONE person,
rather then two so that you dont instantly die while going in, the
shield is very situational as it will most likely decay before you can
even go in.

Listening to people who play vanguard, i've also increased the root to
2.5 seconds (this is buffed so when the prae has the shield) the marine
can still shoot back when they're rooted so i dont think the duration is
a big problem (this is going to be a test merge so i will be watching)

# Testing Photographs and Procedure
it just works

</details>


# Changelog

:cl:
balance: Vanguard dash now restores your shield if you hit ANYONE
instead of 2 people.
balance: Vanguard buffed root now roots you for 2.5 seconds, unbuffed
for 1 second
qol: Vanguard's pierce has now a hit sound for better feedback
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>

---
## [chillboy1917/The-World-in-Music](https://github.com/chillboy1917/The-World-in-Music)@[9a5bc53b9d...](https://github.com/chillboy1917/The-World-in-Music/commit/9a5bc53b9d51f0670b5984a9ed2a2ee89da63e5f)
#### Wednesday 2023-12-13 03:46:59 by chillboy1917

Update README.md

## About
This repository contains the ambient music album "The World in Music" by Chill Boy. The album is released under the Creative Commons Attribution 4.0 International license.

## License
The music in this repository is licensed under [CC BY 4.0] https://creativecommons.org/licenses/by/4.0/

## Track Listing
1. The Beginning
2. Hike and Explore
3. Night Wind
4. Sun
5. City 
6. Wood between the Worlds
7. Into The Unknow
8. Clouds
9. Dawn
10. Bonus Track

Album Link: https://www.youtube.com/watch?v=Q4ACWD1Sjx0&list=PLEn9gVLDlsx3K1RiGp_Up4DHmAaP1i5mh&pp=gAQBiAQB

## Usage
Share: Copy and redistribute the material in any medium or format for any purpose, even commercial.

Adapt: Remex, transform and develop the material for any purpose, even commercially.

Remember, all of these freedoms are subject to the condition of providing proper attribution.

## Contact
For any inquiries or collaborations, feel free to contact (Chill Boy) at josuemmixer2022@gmail.com.

---
## [Doubleumc/cmss13](https://github.com/Doubleumc/cmss13)@[dc234c9939...](https://github.com/Doubleumc/cmss13/commit/dc234c9939efeb43170a934437f50148323407f7)
#### Wednesday 2023-12-13 03:51:18 by InsaneRed

Oppressor cooldown changes (#5154)

# About the pull request

Lowers the oppressor tail_abudct (the hook) to 15 seconds of cooldown
and makes the windup faster.

Makes punch shave off cooldown from the abduct for 5 seconds 

All have been tested but i would like this to get testmerged first so i
can actually see the results in game, nothing is set in stone and i want
to edit this further so the cd / cd reduction isnt too powerful, they're
just numbers ive decided were good enough to atleast make the caste
decent for the time being.


# Explain why it's good for the game

Oppressor has been a snoozer strain for a while now where you cast an
ability, and IF it hits you get to play the game otherwise you wait 20
seconds and thats just not fun. Especially for what the ability is, a 20
second cooldown is not worth it.

I've talked with a few people that all agree that the downtime for what
you "could" do with oppressor is not worth it. And i have to agree with
them, the caste feels boring to play and its basically half dead due to
the amnout of downtime you have between abilities compared to how
everything else works. The idea of this is to make it so its not busted
out of its brain but atleast not an observer++ strain so you can feel
more involved in the gameplay.




# Testing Photographs and Procedure
</details>


# Changelog



:cl:
balance: Oppressor tail abduct changed to 15 seconds and lowers the
windup to 7 deciseconds
balance: Changes around the punch effect so that instead of having to
meet demonic standards, you only need to punch to lower your tail/hook
on oppressor.
fix: You will now automatically punch chest if the target you are aiming
at is delimbed instead of doing nothing
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>
Co-authored-by: Birdtalon <birdtalon@gmail.com>

---
## [saethlin/rust](https://github.com/saethlin/rust)@[ee80c8d0a8...](https://github.com/saethlin/rust/commit/ee80c8d0a8bc63b69f68216c5d37f9ab837eedd0)
#### Wednesday 2023-12-13 04:20:47 by bors

Auto merge of #117611 - Nadrieril:linear-pass-take-4, r=cjgillot

Rewrite exhaustiveness in one pass

This is at least my 4th attempt at this in as many years x) Previous attempts were all too complicated or too slow. But we're finally here!

The previous version of the exhaustiveness algorithm computed reachability for each arm then exhaustiveness of the whole match. Since each of these steps does roughly the same things, this rewrites the algorithm to do them all in one go. I also think this makes things much simpler.

I also rewrote the documentation of the algorithm in depth. Hopefully it's up-to-date and easier to follow now. Plz comment if anything's unclear.

r? `@oli-obk` I think you're one of the rare other people to understand the exhaustiveness algorithm?

cc `@varkor` I know you're not active anymore, but if you feel like having a look you might enjoy this :D

Fixes https://github.com/rust-lang/rust/issues/79307

---
## [NexusSocial/nexus-vr](https://github.com/NexusSocial/nexus-vr)@[8621adfec3...](https://github.com/NexusSocial/nexus-vr/commit/8621adfec3a0bf81789c4b0935a0588a59c2d21d)
#### Wednesday 2023-12-13 04:52:22 by Ryan Butler

Added the fucking stupid ass macos libopenxr loader (#8)

---
## [amandarichardsonn/SmartSim](https://github.com/amandarichardsonn/SmartSim)@[1e686ead0d...](https://github.com/amandarichardsonn/SmartSim/commit/1e686ead0d374ab8f41fba7b2d1667e1350e193f)
#### Wednesday 2023-12-13 05:11:16 by Ben Albrecht

SmartSim Singularity Integration (#204)

[committed by @ben-albrecht]
[reviewed by @ashao]

This PR adds the ability for SmartSim to launch workloads in Singularity (Apptainer) as described in https://github.com/CrayLabs/SmartSim/issues/101. It also lays the groundwork for supporting other container runtimes such as docker, shifter, and podman in the future, as well as launching the orchestrator in a container.

## Design Variations

During development, it became clear that a few design changes from the original proposal were required. I have documented them below with their rationale:

#### 1. Argument name: `bind_paths` -> `mount`

The terms bind path and mount are mostly used interchangeably across different container runtimes. When writing tests, I kept forgetting if it was `bind_path` or `bind_paths`, which hinted to me that it was not a great arg name, so I swapped it out for the more succinct and easy to remember `mount`.

#### 2. `create_run_settings(..., container: str)` -> `create_run_settings(..., container: Container)`

We originally thought it would be easier for users to get started with containers by allowing them to pass a string into `create_run_settings(container='singularity')` instead of having to create a Container object. While writing tests, I realized that this was potentially very confusing for users because 1) the `container` arg types change between `create_run_settings` and `RunSettings`, and 2) if you need to add other metadata such as container args or container mount paths, you have to switch from using `create_run_settings` to `RunSettings` in your code, which is very annoying. Because creating Containers is so lightweight, I think it is best to keep the container interface consistent across all functions that accept them.

#### 3. dropped getter/setter methods

Because command generation and validation happens upon execution, users can freely modify `Container.args` and `Container.mount` without getter/setter methods to update any other state. Therefore, I dropped these methods from the interface.

## Testing

Added 2 test suites for containers: One for WLM testing and one for local testing. The local testing suite runs in GitHub actions. Due to the added time from building Singularity and pulling the `container-testing` image, the singularity testing only happens on one configuration of the build matrix: python 3.9 + redisai 1.2.5 on linux

---
## [MrleMrle/Capstone_Project_1](https://github.com/MrleMrle/Capstone_Project_1)@[0c9766b160...](https://github.com/MrleMrle/Capstone_Project_1/commit/0c9766b160c2bad57adb2380efacd24fbae70dd5)
#### Wednesday 2023-12-13 06:24:57 by Mrle

Add files via upload

Instructions for Capstone Project 1 - Online Resume
Project Specifications
Create an HTML file named index.html.

Use the <!DOCTYPE html> declaration at the beginning of the file to indicate that it's an HTML document.

Create a head section that includes a title element with the text "My Resume".

Inside the body section, write HTML code to create an online resume covering the following aspects:

Summary or objective statement

Education (list degrees, schools, and dates)

Work experience (list job titles, employers, dates, and responsibilities)

Skills (list relevant skills or areas of expertise)

Awards, certifications, or other achievements (list any relevant awards, certifications, or other accomplishments)

Use appropriate HTML tags to format the content of each section, such as h1 for section headings and ul or ol for lists.

Use HTML tags to add a profile photo of yourself.

Use relevant anchor tags to create a multi-page website, listing other aspects of your resume such as Hobbies and Contact details.

Add a footer element with your name and any copyright information or other disclaimers. (Hint: use the MDN docs for things you don't know how to do: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer

Save the index.html file and open it in a web browser to ensure that it displays correctly.

Add your website to your GitHub to start building your portfolio.

Publish your website using GitHub pages and share it here (in the Q&A) with other students.

Comment and make suggestions to other students' projects.



Example
https://appbrewery.github.io/capstone-1-example



Requirements
In order to keep the project within scope (time, energy, resource), you can only use HTML to complete thing project. Even if you know CSS and JS (which we're assuming you don't yet), you are expected to only write the website using HTML.

Imagine you are a professional developer working on this project. There will be things you don't know, things you want to do but haven't yet learnt how to. As a professional developer, you need to know the limits of your abilities and look up other things in Google, MDN docs, the internet.



FAQs
1. Can I use these Capstone projects in my job interviews?

Yes! That's the point of these capstone projects. Unlike course projects, which have solution code and video walkthroughs, Capstone Projects are meant to be entirely your "own work". There are over a million students who have enrolled on this web development course worldwide. If you add a course project to your portfolio, it's very likely that your client will know it's from this course. The capstone projects on the other hand, have no solution code, no walk through, no design specs. It's it purely your creation So it can definitely be counted as your own work and be added to your portfolio.

When I hire developers, I always ask for a portfolio. I consider what they have built by themselves to be far more important than which University they went to or if they have a computer science degree. Many of my friends who are CEOs in multi-nationals and startups agree.



2. What if I don't remember how to do something, even though I watched all the videos?

Watching a video is often not enough to learn a skill. That's why these capstone projects are a great opportunity to identify your weak points. While you're building, you'll find yourself stuck or forgetting how to do things. Great! It's then time to review previous lessons or online documentation to fill your knowledge gaps.

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[73df5c563c...](https://github.com/effigy-se/effigy-se/commit/73df5c563cd5ec1032742c989feedc57162c1122)
#### Wednesday 2023-12-13 07:00:45 by Rhials

"Security Implant" rework, prisoner management console updates (#79882)

## About The Pull Request

For the vernacular purposes of the following PR body -- "Security
Implant" refers to the existing subset of implants given, by security,
to captured prisoners and such as a punitive, controlling measure. This
includes the chemical, tracking, and maybe exile implants.

This revamps the functionality of how "security" implants are displayed
on huds, prisoner management console implant controls/readouts, and
their instrumentality. It was also, ultimately, an attempt at nerfing
the tracking implant that spiralled far out of control.

Rather than only displaying chemical on the right and tracking on the
left, all implants with the "security implant" flag will be trackable on
SecHuds. A maximum of two can be implanted at once. This is both due to
technical limitations, but also conveniently provides security a limit
to consider when choosing implants.

Implants now also occupy their HUD slot based on the order they were
implanted in, rather than always occupying the same spot. Neat!


![image](https://github.com/tgstation/tgstation/assets/28870487/68b17dbb-cda4-4c3b-96d4-b3bbcf49b80e)

From two (three if you count the exile implant), there are now five
security implants. _The tracker implant has been split into two of these
implants._

<details>
<summary>Summary of the implants, functions, changes:</summary>
<br>

- **Tracker (Red)** -- No longer grants teleporter beacon. Tracking
radius has been increased from 20 to 35 tiles. The Prisoner Management
Console will now list the area the prisoner is occupying as well.
Disables after the implantee is dead for 10 minutes.
- **Chemical (Blue)** -- No mechanical changes. The implant pad readout
has been modified slightly.
- **Exile (Green)** -- In addition to past functionality, station
shuttle controls (public, mining, etc.) will be unresponsive for the
implantee. Flimsy, but more effective than a stern warning not to come
back from lavaland.
- **Beacon (Yellow)** -- Implantee becomes a teleporter beacon. The
prisoner console will report if their currently occupied area is
hazardous or not, so half of the security team doesn't blindly teleport
into space or lava. Disables after the implantee is dead for 10 minutes.
Available from Cargo.
- **Teleport Blocker (Deep Blue, not shown)** -- Prevents the implantee
from being teleported. Ever wanted to keep a wizard or cultist in a
cell? This is where you can start. Available from Cargo, expensive and
scarce.

Each of the implants has some application that would benefit security if
used on a captured criminal. Their usefulness may overlap in some
places, but the overall range of control these implants give security is
broadened.

</details>

The implant control console has also been given a small facelift.
Certain implants provide more useful readouts that can help officers
locate, control, or capture an implantee, rewarding cooperation between
officers.

It has also been totally converted into TGUI by @MrMelbert. Kickass!

Also, You can now remotely destroy implants, either to relieve criminals
from their punishment or to make room for a different implant. Wardens
should keep hold of their ID and remember to log out, since a motivated
convict could use it to shed their implants!


![tgui](https://github.com/tgstation/tgstation/assets/28870487/3c2ae99f-9c1d-4b18-b4cb-942cc96bcafe)

Everything made in this PR _should_ be scaleable enough to allow for new
security implant types to be implemented with relative ease. The
teleport-blocker implant was a last minute attempt to prove it to
myself. I had a few more ideas for implants in my head, but figured this
PR was already getting big and ugly enough. That is all for another day.

I truly apologize if there's anything I've missed in here. I did a lot
of this over a long period of time and kind of just... sat on it for a
while. If there's any confusing our unexplained changes, feel free to
point them out and I'll try to give an explanation.
## Why It's Good For The Game

The goal of this PR is to give a bit more depth to security's armory
implants. The intent is to present a choice in what implants are given
(rather than just tracker and maybe chem if you're feeling spiteful),
and to make them more useful as punitive/monitoring tools.

The tracker implant needed a nerf (and probably still does regardless of
this PR's success). It's never used for tracking since the teleporter
beacon is much more direct (+ gives a virtually free attack
opportunity), and the tracking range was incredibly subpar. I'd rather
not take toys away from security, but having the best option not be
roundstart gear feels like a fair compromise.

Warden content. Wardens have more gear to budget for and use at their
own (or the HOSes) discretion. The changes to the prisoner console allow
them to coordinate with officers to get good value out of the implants
they've chosen for an implantee.

Gives antagonists an alternate way to get de-implanted, without external
help, that can only be granted at the fault of security. Wardens who
dish out implants must keep an eye on the people carrying them!
## Changelog
:cl: Rhials, MrMelbert
add: The Tracker implant has had its teleport beacon functionality
migrated to the new (cargo accessible) Beacon implant.
add: Teleport Blocker security implant, that prevents the implantee from
teleporting by any means. Purchasable from cargo.
add: Security implants may now be harmlessly self-destructed at the
Prisoner Management Console.
balance: The Tracker implant tracking radius has increased from 20 to 35
tiles. The Prisoner Management Console will track and display the area
the implantee is in as well.
balance: The exile implant now prevents implantees from operating
shuttle controls.
code: Various code improvements and removal of unused vars in the
Prisoner Management Console
code: The HUD slots for chem/tracking implants have been converted to
display any implant with the IMPLANT_TYPE_SECURITY flag and an
associated sprite.
spellcheck: Modifies various implant pad readouts, removing false
information and rewriting some sections.
/:cl:

---------

Co-authored-by: MrMelbert <kmelbert4@gmail.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[7c6f2db6cb...](https://github.com/effigy-se/effigy-se/commit/7c6f2db6cba6aa927ec6f4c4171130b0592591e1)
#### Wednesday 2023-12-13 07:00:45 by John Willard

PDA update (Messenger works while dead, Microwave works, etc). (#80069)

## About The Pull Request

This is an update that touches many more things all at once (compared to
my other PRs) meant to make PDAs in general feel more consistent and not
take away from one of the experiences we want to encourage: interaction
between players.

1. Replaced all checks of a 'pda' with a 'modular pc'. This means
technically (though not done in-game currently) other modpcs can hold an
uplink, and microwaves can charge laptops.
2. Speaking of microwave, they now don't break and require
deconstruction if the cell is removed mid-charge.
3. When a Mod PC is out of power, it will now allow the Messenger to
work (which now also doesn't consume any additional power), if the app
exists on the PC. Here's a video demonstration


https://github.com/tgstation/tgstation/assets/53777086/7ae12f81-a271-49b8-95fa-2ba54d2e2d1f

4. Flashlights can't be turned on while the cell is dead
5. I replaced a bunch of program vars with ``program_flags`` and renamed
``usage_flags`` to ``can_run_on_flags``.
6. Added a debug modPC that has every app installed by default. Mafia
had some issues in the past that were unknown because Mafia wasn't
preinstalled with any tablet so was never in create & destroy nor in any
other unit test. This was just an easy solution I had, but PDAs should
get more in-depth unit tests in the future for running apps n stuff- I
just wanted to make sure no other apps were broken/harddeling.

## Why It's Good For The Game

Currently when a PDA dies, its only use is to reply to PDA messages sent
to you, since you can still reply to them. Instead of just fixing it and
telling players to cope, I thought it would be nice to allow PDA
Messenger to still work, as it is a vital app.
You can call it some emergency power mode or whatever, I don't really
mind the reason behind why it is this way.

When I made cells used more on PDAs, my main goal was to encourage
upgrading your PDA and/or limiting how many apps you use at once, I did
not want this to hit on players who use it as a form of interaction.
This is the best of both worlds, I think.

The rest of the changes is just for modularity, if some downstream wants
to add tablets, phone computers, or whatever the hell else, they can
still get just as far as PDAs should be able to get to, hopefully.

## Changelog

:cl:
add: PDAs with a dead power cell are now limited to using their
Messenger app.
fix: Microwaves now stop charging PDAs if the cell was removed
mid-charge.
fix: Microwaves can now charge laptops.
fix: PDA Flashlights can't be turned on while the PDA is dead.
fix: You can now hold a laptop up to a camera (if it has a notekeeper
app installed) like PDAs already could.
/:cl:

---------

Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [PraveenMohan13/FOP-C](https://github.com/PraveenMohan13/FOP-C)@[779dfcc48e...](https://github.com/PraveenMohan13/FOP-C/commit/779dfcc48e75a75029dc916ac56e8c4c599f3393)
#### Wednesday 2023-12-13 07:32:30 by Praveen_Mohan

DM

Jeni and her brothers Joseph and John found themselves in Narnia, the land of magic during World War III. Narnia was completely filled with gentle people and also it is where the trees sing, the fauns dance, and animals talk. Being from England, Jeni wanted to teach the kids the English language. She started teaching them the alphabet but then she remembered that she might have to go to London and felt sad. John and Joseph discussed with each other and suggested an idea to Jeni to come up with a program so that the kids can learn on their own when she was not there. Can you help Jeni to write a program to check whether the given character is a vowel or consonant or alphabet?

Input Format

The input consists of a character.

Constraints

NA

Output Format

The output should be any one of the below-given strings. Vowel or Consonant or Not an alphabet.

Sample Input 0

e
Sample Output 0

Vowel
Explanation 0

The input character e is a vowel and hence it prints Vowel.

Sample Input 1

Z
Sample Output 1

Consonant
Explanation 1

The input character Z is a consonant and hence it prints Consonant.

---
## [cgnannan/evals](https://github.com/cgnannan/evals)@[ab0b90c5fa...](https://github.com/cgnannan/evals/commit/ab0b90c5fa8b2993f84d68be8bccdb0d377a68de)
#### Wednesday 2023-12-13 07:34:47 by Uday

Eval addition: AI vs Human Text Detector (#1021)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
GPT Model Text Detection

### Eval description

The goal of this evaluation is to test the AI model's ability to
correctly identify whether a given piece of text was generated by a
specific AI model, in this case, the GPT model 'text-davinci-003'. The
model's performance is then measured by its accuracy in making this
determination. The text presented to the AI is diverse and can range
from literary summaries to general discourse, designed to challenge the
AI's understanding and analysis capabilities.

### What makes this a useful eval?

This evaluation serves a critical role in the context of education where
AI technologies are increasingly being used. As AI-generated text
becomes more sophisticated, there's a risk that students might use AI
models to complete assignments, circumventing the learning process. The
ability of an AI to detect whether a piece of text is human-written or
generated by a specific AI model like 'text-davinci-003' is essential to
maintaining academic integrity. This task not only provides a measure of
an AI's discernment capabilities but also has broader implications for
AI ethics and safety.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This evaluation uniquely addresses the intersection of AI and education.
As AI technologies continue to evolve, it is crucial to have mechanisms
in place to detect AI-generated content, particularly in academic
settings where these technologies could be misused. By focusing on the
ability to discern output from a specific AI model, 'text-davinci-003',
this evaluation task pushes AI capabilities while simultaneously
addressing a real and timely issue. It underscores the necessity for AI
to not only be more capable but also more discerning, supporting
academic integrity in the face of rapidly advancing AI technologies.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Green Eggs and Ham' is a children's
book by Dr. Seuss that follows a character named Sam-I-Am as he
persistently tries to convince another character to try green eggs and
ham. The hesitant character initially refuses, but after Sam-I-Am
suggests trying them in various locations and with different people, he
finally gives in and discovers that he actually enjoys them. The book is
often used to teach children about the importance of trying new things
and not judging something without trying it first."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Green Eggs and Ham' by Dr. Seuss is
a children's book about perseverance and trying new things. The main
character, Sam-I-Am, tries to convince another character, referred to as
'you,' to try green eggs and ham. Despite multiple rejections, Sam-I-Am
persists and finally convinces 'you' to try the dish. 'Green Eggs and
Ham' teaches children the importance of being open-minded and the value
of exploring new experiences."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'The Cat in the Hat' by Dr. Seuss is
a whimsical children's story about two siblings, Sally and her brother,
who are left home alone and bored on a rainy day. Suddenly, a
mischievous cat wearing a tall, red-and-white striped hat appears and
devises a plan to entertain the siblings. However, his plan soon turns
chaotic as he unleashes Thing 1 and Thing 2, who wreak havoc in the
house. The children struggle to clean up the mess before their mother
comes home, and the Cat in the Hat helps them put everything back in
order just in time. Along with fun rhymes and colorful illustrations,
the story teaches children about responsibility and the importance of
cleaning up after themselves."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'The Cat in the Hat' by Dr. Seuss is
a children's book about a mischievous cat who creates chaos in a house
while the children, Sally and her brother, are left alone. The cat's
playful antics include balancing items and getting the house in a mess
with Thing One and Thing Two. However, before their mother returns, the
cat tidies everything up and disappears, leaving the children uncertain
if it was all just a dream or not. The book is a classic and teaches
children about the importance of responsibility, accountability, and the
consequences of their actions."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"Dick's novel is set in a future,
totalitarian society where the government controls all aspects of life.
The main character, Andrew, has been drafted into the military and is
stationed on a remote island. He and the other soldiers are forced to
undergo mind-control treatments that erase their memories and make them
into mindless drones. Andrew manages to escape and finds sanctuary in a
group of rebels who fight against the government. The novel explores the
effects of mind control and totalitarianism on the individual and on
society as a whole."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"The novel Mody Dick by Herman
Melville is an epic tale of a seafaring captain's journey to seek
revenge on a giant white sperm whale. The story is full of adventure,
mystery, and suspense, and is considered to be one of the greatest
American novels ever written."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"Mody Dick is an epic novel written
by Herman Melville in 1851. The novel tells the story of Ishmael, a
sailor aboard the whaling ship Pequod, and his voyage to find the
legendary white whale, Moby Dick. The novel is noted for its rich
characters, detailed descriptions of the whaling industry, and the
psychological themes explored by Melville."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Charlotte's Web' is a children's
book written by E.B. White and published in 1952. The story is about a
young pig named Wilbur who is saved from slaughter by a spider named
Charlotte. Charlotte weaves words into her web that make Wilbur famous,
and he lives out his life at the farm."}],"ideal":["Yes"]}
  ```
</details>

---------

Co-authored-by: Uday <udaykumar.1997@gmail.com>

---
## [cgnannan/evals](https://github.com/cgnannan/evals)@[7c3159aaaf...](https://github.com/cgnannan/evals/commit/7c3159aaaf8553ad19d1ba177f602302c06d75c6)
#### Wednesday 2023-12-13 07:34:47 by Fabrizio Ruggeri

Proofreader (#1225)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

proofreader

### Eval description

Asking the model not only to correct some text but also following rules
when correcting. These rules enforce to not correct some parts or to
correct in a specific way.

### What makes this a useful eval?

This come from a real use case where gpt4 was not reliable 100%

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ x Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
music"},{"role":"user","content":"A big thank you to our guitar and base
player"}],"ideal":"A big thank you to our guitar and bass player"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"This is correct!"}],"ideal":"This is
correct!"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is 20th Century Modernist
Art"},{"role":"user","content":"Pablo Picaso's famuos painitng Guernica
dipicts the atrocities of the Spansh Civil War."}],"ideal":"Pablo
Picasso's famous painting Guernica depicts the atrocities of the Spanish
Civil War."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
philosophy"},{"role":"user","content":"Nitsche never wrote Der Wille zur
Schmacht. It was his sister Elisabeth Foerster that compiled the work
and gave it an antisemithic tone."}],"ideal":"Nietzsche never wrote Der
Wille zur Macht. It was his sister Elisabeth Förster that compiled the
work and gave it an antisemitic tone."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"Stop doing this!"}],"ideal":"Stop doing
this!"}

  ```
</details>

---
## [cgnannan/evals](https://github.com/cgnannan/evals)@[c0c784fd97...](https://github.com/cgnannan/evals/commit/c0c784fd978bb2e4bc4b5aef7b0f032fa3b04a75)
#### Wednesday 2023-12-13 07:34:47 by monocle-pastels

[eval] norwegian rhymes (#1248)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

norwegian-rhymes

### Eval description

Check if Norwegian Bokmål words are rhyming 

### What makes this a useful eval?

It's important that GPT understands Norwegian phonetics and language

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This contains multiple cases of most pitfalls when considering what
rhymes in Norwegian.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [] (Ignore if not submitting code) I have run `pip install pre-commit;
pre-commit install` and have verified that `black`, `isort`, and
`autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "avskjed,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "led,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "nett, vet"}],
"ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "deg, vei"}],
"ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "huset,
knuse"}], "ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "her, sær"}],
"ideal": "Yes"}
  ```
</details>

---
## [lolman360/f13tbd](https://github.com/lolman360/f13tbd)@[ba55bbfedf...](https://github.com/lolman360/f13tbd/commit/ba55bbfedfb9c6a9a46c3a4b572c230f5d42ab4a)
#### Wednesday 2023-12-13 08:05:25 by Stutternov

Bobstation Ghost Port (#300)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

Remembered Escape from Navarro and remembered Bobstation codebase had
interesting ghost mechanics with seeing in monochrome while dead and
de-limbed limbs pop off yourself and stay missing as a ghost.

Ended up finding out - most of it would port with ease! Sadly the motion
blur was really too annoying to get working, but I plan to look at it at
some point. And, while I could get monochrome working, I want to run
that by people first. I enjoy it, but I know it fucks with people. But
hey - lookin' gooood.

De-limbing makes the limb disappear on the ghost.

![image](https://github.com/f13babylon/f13babylon/assets/47883419/3b4c7ca3-5761-4159-aedd-e64ae4fc2aa7)

Wearing armor or clothing? Well, it'll stay on you when you're dead!

![image](https://github.com/f13babylon/f13babylon/assets/47883419/bfae701f-5931-4038-b52b-1a429e286882)

And even if you matrix it stays.

![image](https://github.com/f13babylon/f13babylon/assets/47883419/10e63ba4-e6a1-4e15-90da-a1ca82c50535)

## Why It's Good For The Game

It's more of a nice addition to how I even remember ollld TG worked with
ghosts, minus the delimbing and armor. The style kind of fits and makes
ghosts stand out, letting you see who they were - even if you didn't
catch the name - when alive.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: Ports Bobstation's ghost system, preps for eventual porting of
motion blur code portion as well.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: maaacha <116771811+maaacha@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [lolman360/f13tbd](https://github.com/lolman360/f13tbd)@[1d8302d4e3...](https://github.com/lolman360/f13tbd/commit/1d8302d4e35276ca63ba2b5ced5b4719ef36191c)
#### Wednesday 2023-12-13 08:05:25 by Stutternov

Khan Re-Balancing (#292)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

Yeah, so - anyways.......

Khans had some issues with their balance. I've went through and re-did
some of their loadouts for their faction.
- The lever action has been removed from Enforcers, instead it is
replaced with the Auto-5. The Auto-5 is the alternative fit as it
doesn't fit in bags like the lever, holds one less round, but in return
fires slightly faster. This is on-par with actual other factions (as the
only faction that got lever shotguns round start are vet-legion. Auto-5s
are more common.)
- The Enforcer and Smith have kept the selectable trait book, but Khans
over-all had a silly amount of traits. Therefor Chemist and Senior
Enforcer had theirs removed. (Senior has enough perks, and the book for
Chemist made the loadout selection for perks worthless.)
- Smith has lost their explosive crafting, but Chemist has gotten the
advanced explosive crafting book akin to NCR sappers who get the choice
of one. (To make Chemist loadout balanced, the lowsurgery book has been
replaced with medium surgery, since both NCR medics and Legion aux get
mid-surgery, not low)
- Khan armors have had their wound protection updated. They are now
roughly equal to NCR/Legion armor counterparts.
- Khan senior enforcer has had his round-start caps lowered from 1,000
to 500. (Tbh this may still be a bit high but w/e I was suggested this
amount)
- Smith, in exchange for losing explosive trait book, has instead gained
more gun crafting recipes in exchange. Can make all base Khan guns plus
10mm smg and some others. Plus - can make alloys like NCR LO / Legion
forgemaster. (Lost their GnB part 4 server-start learned. Work for it,
like the LO has to.)
- Renamed Khan Smith into Khan Armorer, which is a canon name of a Khan
found in Fallout: NV. Minor change, but tbh fits the role better since
they are mostly focused on gun crafting _and_ smithing.
- Made the Senior Enforcer loadouts actually competitive with each
other. Hammer one now gets a deagle with it to provide a sidearm for
range, the 10mm had to be a meme since it was the WORST option possible
- and is now replaced with a Infiltrator since it's just a slightly
better R-91 with a scope. (I'd argue this makes up for the now lack of
an extra selectable trait for head enforcer.)

Also - small hotfix, why the fuck did the Senior Scribe had low surgery
skill but Scribe has mid-surgery??? Not khan related but come on.....
scribe gaming..........

## Why It's Good For The Game

The major factions on server have gotten a fair bit of balancing
attention but Khans lacked a lot, such as overlooked wound armor
protection, their round start caps, and how many traits they could get
(which honestly felt like an unintended oversight, maybe???)

I think this attempts to re-do the Khan loadouts without per-say
'nerfing' them but rather fixing the fact that many of the loadouts
aren't unique to the role (i.e easily replacing chemist with smith, or
vice-versa) - as this has some buffs as well in things Khans were weak
in, such as Smith not having much unique to them.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
balance: See about section
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [lolman360/f13tbd](https://github.com/lolman360/f13tbd)@[31c7e3d8db...](https://github.com/lolman360/f13tbd/commit/31c7e3d8db0dec0828717112a6ae0f03970d058f)
#### Wednesday 2023-12-13 08:05:25 by JawnWick

Skinwalker-B-Gone/God Bless America: Enclave Bunker/Casper Changes (#299)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

Takes a good chunk (around half) of the salvage cars from the parking
lot entering Casper, and places them in and around the exterior of the
Enclave bunker.

Adds a camera system to the bunker.

Moved prewar weapon spawn behind bunker doors.

## Why It's Good For The Game

Enclave can still do salvaging without John Republic and his troopers
completely taking salvage away from the faction (they shouldn't be doing
this anyway, yall MFs need to ahelp that shit when you see it
happening). They would still need to go to the parking lot to get the
rest that was originally there for the total, but it's more manageable
now.

Camera system because super secret government entity being incapable of
observing their own bunker and the immediate exterior is funny.

Prewar spawn moved because random NCR or Followers guards would rush it
for free gamer gear.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: Bunker camera system
tweak: Salvaging opportunities
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [iandol/Psychtoolbox-3](https://github.com/iandol/Psychtoolbox-3)@[c797954427...](https://github.com/iandol/Psychtoolbox-3/commit/c797954427d133cbe0374f996c14327653a9b37d)
#### Wednesday 2023-12-13 08:27:45 by kleinerm

Merge pull request #823 from Psychtoolbox-3/master

Pull for Psychtoolbox 3.0.19.6 "Raspberry cake" release.

### Compatibility changes wrt. Psychtoolbox 3.0.19.5:

- Psychtoolbox is now tested and supported on Matlab R2023b, instead of R2022b.
  It is expected to continue to work on older releases than R2023b, but no longer
  developed or tested against them.

- Slight behavioral changes in IOPort BreakBehaviour settings on MS-Windows, and
  generally a few IOPort config options. Not expected to affect (m)any user scripts.


### Highlights:

- This release was tested for compatibility with Matlab R2023b on Linux and Windows,
  specifically Ubuntu 22.04.3-LTS with AMD RavenRidge (AMD Ryzen 5 2400G processor
  integrated graphics) and AMD Polaris graphics, and on Microsoft Windows 10 22H2
  with AMD RavenRidge and NVidia GeForce GTX 1650 graphics, and to a lesser degree
  on Ubuntu 20.04.6-LTS and Windows 11 22H2 with Intel Kabylake (GT2) "UHD 620"
  integrated graphics. Testing with some onboard sound chips was also performed.
  The testing led to various smaller improvements, and various workarounds on
  MS-Windows for AMD OpenGL and Vulkan graphics driver bugs, and for some NVidia
  driver bugs, as well as some bugs in Matlab wrt. backwards compatibility and
  OS compatibility. Most improvements in this release are due to that.
  
  This was done as part of out Mathworks 2023/2024 contract for ensuring compatibility
  with recent Matlab releases, spending over 65 work hours. Due to not even remotely
  sufficient funding for this work, no significant testing beyond some very quick touch
  and go spot testing was performed for macOS.

- Substantial movie playback performance improvements in pixelFormat 11 for HDR
  and WCG movies when hardware video decoding is used on Linux and MS-Windows. A
  small fraction of this work was sponsored as part of the Mathworks contract.

- 10 bit deep color framebuffer and HDMI output for the RaspberryPi 4/400 by
  improvements to Psychtoolbox and to the Mesa 23.3.1 OpenGL graphics drivers
  for RaspberryPi's VideoCore 6+ gpu. Mostly paid for by Cambridge Research Systems.


### All:

- Screen: Optimize storage format for LUMINANCE16 textures for texture normalization.
  If a 16 bpc luminance texture is turned into an offscreen window, or drawn into,
  the needed normalization / conversion to RGBA format now converts into RGBA16
  format instead of RGBA32 float format. This retains full precision of the original
  image content, but at half the memory consumption.

- Screen: In DrawTexture(s), always filter planar textures via nearest neighbour
  sampling instead of any of the other filtering/sampling modes, as any sampling
  other than nearest neighbour will cause massive artifacts.

- Screen: Improve performance of HDR movie playback by more efficient use of hardware
  video decoding. Enable the GStreamer movie playback engine in HDR mode (aka pixelFormat 11)
  to accept and handle typical semi-planar YUV formats used for HDR movies when
  gpu hardware accelerated video decoding is in use. This allows GStreamer to avoid
  cpu expensive frame format conversions from semi-planar frames provided by the
  gpu hardware decoders to planar formats previously accepted by PTB's texture
  creation code, leading to way higher performance when such hardware decoders
  are used. Software decoding still works via the previous path, whenever that is
  wanted or needed. Software decoding can also be enforced by disabling of hardware
  decoding by passing in specialFlags1 flag +4 in ``Screen('OpenMovie', ...)``. One
  limitation of the disable is that hardware decoding will stay off for the remainder
  of the whole session, ie. until Octave/Matlab is quit, once the disable flag
  for hardware decoding has been given once in a session. This could be fixed by
  requiring GStreamer 1.20+ as minimum requirement, ie. Ubuntu 22.04 and later.

  Note that I've repurposed/redefined specialFlags1 flag +4 as hw accel disable,
  from previously "draw 2D flow vectors on content for debugging/visualisation".
  This is ok, as the feature was probably never used by anybody, and also because
  this feature is deprecated and unsupported in all supported GStreamer versions
  since quite a while.

  The following new formats are supported for efficient handling:

  - Y42B = YUV planar 4:2:2 with 8 bpc.
  - NV16 = YUV semi-planar 4:2:2 with 8 bpc, aka P208.

  - P0xx formats of YUV semi-planar 4:2:0 sampling with 8, 10, 12 and 16 bpc,
    ie. NV12, P010_10LE, P012, P016. These are the relevant ones for typical
    HDR-10 hardware decoding from H265/HEVC, AV1, and from VP9.

  So far this has been tested on MS-Windows 10 with NVidia GeForce GTX1650 and
  AMD Raven Ridge / Vega as part of a Ryzen 5 2400G processor. On NVidia it shows
  a 2x speedup in decoding speed, to allow playback of 4k HDR at 60 fps with stable
  framerate and none to minimal frame dropping. This typically uses NVCODEC on
  NVidia hardware or Direct3D11/DXVA decoding on NVidia, AMD and Intel gpus.

  Tests on Ubuntu 20.04.6-LTS + Intel Kabylake + GStreamer 1.16, and on two
  Ubuntu 22.04.3-LTS machines with GStreamer 1.20.3, once with AMD Polaris11
  and once with AMD Raven Ridge, also showed 2x performance improvements.
  This uses VAAPI for hardware accelerated video decoding on AMD and Intel,
  and maybe on NVidia, but NVidia is untested so far on Linux.

  Note that while AMD and NVidia worked well in my testing, more often than
  not, Intel Kabylake shit its bed, causing hangs or massive visual artifacts
  in decoded video, on both Ubuntu 20.04 and Windows 11. May or may not be
  general Intel bugs, or may just be a problem on my specific old Intel iGPU.

  Additional successful testing was performed by a user under Windows-10 with
  a NVidia GeForce RTX 3080 with H265 and AV1 4k HDR 60 fps content.

  As a general guideline, as of November 2023, these video codec formats
  are generally hardware accelerated on Linux and Windows with typical
  recent hardware from AMD, NVidia and Intel:

  - MPEG2, VC1, H264, VP8: YUV 4:2:0, 8 bpc.
  - H265, VP9: YUV 4:2:0, 10 bpc HDR.

  - Sometimes also MPEG4, and AV1, the latter only on latest gpu's from
    NVidia, AMD and Intel, specifically NVidia Ampere+ RTX3000+, or AMD RDNA2
    Navi 2nd gen, or Intel Xe+/Arc+ or macOS 14 on Apple M3+.

  For best cross-platform, cross-vendor compatibility and with older hardware,
  the safest choices for high performance playback are probably H264 and H265
  at the moment.

  None of this applies to Apple macOS, as macOS too primitive OpenGL implementation
  currently does not allow use of pixelFormat 11 playback.

- PlayMoviesDemo.m: Optimize further for fast playing movies.
  Suppress costly text drawing for any fps >= 30. Skip wait for flip complete for
  non-HDR playback. Ths way the demo also serves as a real-world performance test.

- `help GetChar`: Update wrt. OS+GUI+Matlab/Octave support, internationalization.

- `PerceptualVBLSyncTest[FlipInfo2]`: Add optimizations, especially for RaspberryPi.
  Avoid redundant stimulus draw in non-stereo mono-mode. Do clear the backbuffer
  after each flip, as that seems to give a substantial performance boost for the
  VideoCore gpu's - See speculation in code comments - probably related to it being
  a tiled renderer, or a split gpu + display engine design at least for VideoCore 6+
  of RaspberryPi 4 and later. I haven't checked the driver source for the more likely
  reason yet.
  
  Another thing that can really help sync tests on the Pi is Priority(1), because
  then gamemode daemon chooses a more aggressive cpu governor. This only matters at
  high display refresh rates though, e.g., on a RPi 400 with a 1920x1080 120 Hz
  display. At somewhat lower refresh rates, e.g., 60 Hz, it isn't needed.

- `IOPort`: Fix 'OpenSerialPort' bugs where default settings override user settings.
  
  As GitHub user @qx1147 found out during a code review, there is a flaw in
  the handling of serial port options, where default serial port options may
  override user provided configuration options, so the wrong settings are
  silently applied! This only happens if the user script provides different
  settings in ``IOPort('OpenSerialPort', ..., settings)``, ie. on initial port
  open. Calls to ``IOPort('ConfigureSerialPort', ..., settings)`` are not
  affected.

  Luckily (dumb luck!), only a few options were mishandled, and most of these
  are rarely changed by user scripts, specifically:
    
  ProcessingMode=Cooked would get ignored, and raw mode used instead. Rarely
  used on Linux/macOS and not supported on Windows anyways. Low impact.
    
  BreakBehaviour=Ignore would be used instead of Flush or Zero. Not a
  problem on Windows, as that is the only supported option. The fact that
  this went unnoticed on Linux/macOS suggests not much use of Flush or Zero
  by users scripts. No use by PTB itself. Low expected impact. Note that the
  implementation of 'Flush' on the Unixes is of questionable use, as Flush
  would not only flush read/write buffers, but also send a SIGINT, which may
  end in unexpected ways on Unix, as we don't handle SIGINT specifically.
  
  StopBits=2 would get ignored and the default of 1 stop bits would be used.
  Unclear how many devices want 2 stop bits, but I haven't ever seen one, so
  probably low expected impact.
  
  DataBits=16 would get ignored on MS-Windows only and replaced by 8 bits,
  whereas other settings are fine, and 16 bits is unsuported on Linux/macOS,
  so probably rarely if ever used. Low expected impact.
  
  FlowControl=None will be used instead of hardware or software flow control.
  This can be a real bummer with potential real impact, as some devices do
  support or recommend active flow control! In the case of PTB, the
  CedrusResponseBox() driver for Cedrus response box devices would have
  liked that setting.
  
  Audit of Psychtoolbox internal user of IOPort, and of the demos, only
  shows one bad case where things went sideways: CedrusResponseBox.m
  This driver requested hardware flow control, but silently got instead NO
  flow control! This is interesting, because during my testing I found
  communication with Cedrus boxes always rather unreliable, and now I have
  to wonder if this was because of the accidental lack of hardware flow
  control? I can't find out, as I lost access to Cedrus devices long ago.
  
  This whole parameter handling is somewhat fragile, and could do with an
  improved implementation, but due to the severe lack of financial funding
  for PTB, this is not an option in the foreseeable future. Not even code
  review or testing of 3rd party contributions, if there were any. Luckily
  this part of the driver is mostly static since years, so I guess we can
  drag our feet longer and sit it out.

  Another problem pointed out by @qx1147 is indeed that wrong options, e.g.,
  due to typos in users experiment scripts, would not lead to an error abort
  or warning, but would get silently ignored in many cases. Not great at all,
  but lack of funding will leave this problems also unsolved in the near- to
  midterm, possibly forever. Life sucks...
    
  See also PR #821 for discussion. Thanks to @qx1147 for catching this!

- psychrange(): Make fallback trigger robust against Matlab R2023b if
  statistics toolbox is not installed.

- help PsychDemos, MovieDemos: Some fixes so Matlabs help system can cope.

- Snd(): Minimal compatibility fix for older Matlab releases. E.g., R2018b
  may need this fix, as reported on the forum.

- FlipTimingWithRTBoxPhotoDiodeTest: Fix useXR flag.

- Cone fundamentals fitting tests: Fix plotting to be usable on different displays.
  Old plot positioning caused UI awkwardness on most monitors. Also fix use of
  savefig() function, which was broken due to incompatible changes in Matlab over
  the years as far as I understand.

- LosslessMovieWritingTest.m: Switch default codec for encoding.
  From long non-existent huffyuv to supported avenc_huffyuv. Update help texts.

- Delete ScreenTest.m the most useless test ever.

- ComputePhotopigmentBleaching(): Fix some bug in example. By David Brainard.

- Minor bug fixes, documentation updates and improvements.


### Linux:

- Psychtoolbox was built and lightly tested against Matlab R2023b.

- PsychHID: Work around latest Matlab R2023b internationalization bugs.
  
  Matlab R2023b, at least on Ubuntu 20.04-LTS and Ubuntu 22.04-LTS, has a
  new compatibility bug, where it provides its own deficient libX11 that
  defines a wrong path to the locale configuration directories. This causes
  failure of international keyboard handling, ie. calls to XSupportsLocale(),
  XSetLocaleModifiers() and XOpenIM() fail. As a consequence, only U.S.
  keyboard layouts get properly handled whenever our our PsychHID/keyboard
  queue based GetChar() implementation is in use, but not other keyboard
  layouts!
    
  It also triggers a warning each time KbQueueCreate() is called, regardless
  if in the context of GetChar/CharAvail/ListenChar, or just for keyboard
  queue operation.
    
  Try to detect and work around this Matlab bug, by detecting the failure
  and then setting the XLOCALEDIR environment variable to override Matlabs
  broken path to a path that is correct at least for Ubuntu 20.04/22.04 and
  for similar Debian(-based) systems. Also try to detect user interference,
  e.g., the user setting a unsuitable XLOCALEDIR, and give troubleshooting
  tips in that case as well.
    
  This fixes the problem with R2023b on at least Ubuntu 20.04 and 22.04.
  The problem could also have been present in R2023a already, but this was
  not ever tested by myself, and I am not aware of any bug reports against
  either R2023a or R2023b.

- Add support to XOrgConfCreator, XOrgConfSelector and PsychLinuxConfiguration
  to allow to enable 10 bpc / 30 bit deep color framebuffers and display over
  HDMI on suitable displays with the RaspberryPi 4 and 400, and likely also the
  RaspberryPi 5. This was only tested on the RaspberryPi 400 under RaspberryPi OS
  versions 11 "Buster" (legacy) and 12 "Bookworm" (most recent one) 32-Bit editions.
  Note that current Psychtoolbox from us currently only works on RaspberryPi OS 11,
  ie. what is now called the "legacy" edition, not yet on the "current" OS version 12.
  Psychtoolbox 3.0.18.12, shipping with OS version 12 will work of course, but it
  does not have this setup code. However, it would work with a manually created
  xorg.conf file.

  Note that 10 bit framebuffers do not work on current versions of RaspberryPi OS
  out of the box. You need to manually install Mesa version 23.3.1 stable or later,
  which has an ETA of sometimes at or after 13th December 2024. Until then, a build
  script can be found under. You can download it, make it executable, and run it to
  build and install a Mesa local build in /usr/local/ compatible with RaspberryPi 4
  and 400, possibly RaspberryPi 5. Use this hacked build and install script at your
  own risk, if it totally breaks your system you get to keep all parts:
  
  https://raw.githubusercontent.com/kleinerm/PiKISS/ForCRS10BitMesa/scripts/config/vulkan.sh

  My enablement work for OpenGL 10 bpc / color depth 30 bit / deep color framebuffer
  support for Mesa 23.3.1+ on the RaspberryPi 4+ was sponsored by a contract from
  Cambridge Research Systems Ltd. Thank you!

- Other smaller refinements to RaspberryPi support.


### Windows:

- Psychtoolbox was built and lightly tested against Matlab R2023b.

- For Vulkan on Windows, reenable fullscreen exclusive support on current AMD drivers
  for proper timing. now works again on AMD gpu's with the latest AMD display drivers,
  version 23.11.1 from November 2023, as tested successfully in both SDR mode and HDR-10
  mode on Windows 10 22H2 with AMD Raven Ridge iGPU of AMD Ryzen 5 2400G APU, aka DCN-1
  display engine and Vega 11 graphics. Hurray!

  Some earlier driver versions might work as well, but this is the only confirmed one
  by testing, so reenable fullscreen exclusive starting with the 23.11.1 release.

- `IOPort`: Fix wrong break condition handling. Ignore break conditions completely
  `(BreakBehaviour=Ignore)`, rather than treating them as errors without further
  handling them in a useful way. Do validate BreakBehaviour parameter to be the only
  currently supported setting. Contributed by GitHub user @qx1147.

- `PsychPortAudio`: Update libportaudio for MS-Windows with latest from upstream Git
  main development branch. This way we get my bug fixes to WASAPI audio capture/input
  timestamping. Testing on MS-Windows 10 and 11 still shows some fragility and oddity
  in audio input capture timestamping, e.g., for voice onset timestamping, or sound
  based timing measurements like KeyboardLatencyTest.m or AudioFeedbackLatencyTest.m.
  These tests may not be very trustworthy on MS-Windows with WASAPI sound backend.

- Screen: Rewrite CRS clut update function RenderClutBits++ as a workaround.
    
  Switch from using point rendering via glVertex2i() of the clut T-Lock update pattern
  to instead using glRasterPos2i + glDrawPixels().
    
  Why? Because the proprietary AMD OpenGL driver on Windows has bugs in
  glVertex2i positioning when rendering to the OpenGL system backbuffer. The
  most easy way to work around this atm. is to use glRasterPos2i + glDrawPixels()
  to avoid the glVertex2i AMD bugs. This has the added benefit that we now use
  this glRasterPos2i + glDrawPixels() combo consistently for all CRS T-Lock rendering,
  ie. FE1 stereo driving and DIO codes, and for identity pixel passthrough tests and
  gamma table tweaking in PsychGPUTestAndTweakGammaTables(). At least we only
  have to think about one potentially broken function (glRasterPos2i()) in the future,
  not two separate ones.
    
  This was found on AMD RavenRidge Vega11 under Windows 10 with AMD driver 23.11.1.
  No such problem happened with the same hardware on Linux during my testing.

- AdditiveBlendingForLinearSuperpositionTutorial.m: Fix clut overlay text, and cleanups.
  Apply same fix as for BitsPlusIdentityClutTest.m for AMD Windows OpenGL driver
  bugs, so text rendering via the Mono++ / M16 clut hardware overlay works.

- BitsPlusIdentityClutTest.m: Work around MS-Windows AMD OpenGL driver bug.
  AMD's current OpenGL driver version 23.11.1 from November 2023 for MS-Windows
  has a bug in that glTexImage2D() does not accept GL_BITMAP texture specs. This
  breaks non-anti-aliased text rendering mode in the drawtext plugin.
    
  Work around this by enabling anti-aliased rendering for the plugin via
  Screen('Preference', 'TextAntiAliasing', 1); However, we don't want anti-aliasing,
  as it potentially interferes with clut overlays on CRS and VPixx devices, so use
  Screen('Preference', 'TextAlphaBlending', 1); to apply Screen('Blendfunction')
  settings during text rendering, but don't actually use Screen('Blendfunction').
  Instead leave alpha-blending at defaults, which is alpha-blending disabled.
  This effectively brings back aliased text rendering which works with the clut
  overlays.

- Screen('ColorRange'): Add workaround for color clamping OpenGL driver bugs.
    
  Turns out the recent proprietary AMD OpenGL driver on MS-Windows has a broken
  color clamping query implementation, which does not report clamp state for
  GL_CLAMP_VERTEX_COLOR_ARB or GL_CLAMP_FRAGMENT_COLOR_ARB.
    
  As such, we get reported failure to change color clamping on Windows 10 + AMD,
  whereas the same code works fine on Windows 10 NVidia or Intel.
    
  Work around this by detecting the failure and auto-selecting our own internal
  GLSL shader based fallback path. This should fix it - at a performance penalty,
  as vertex color clamping can be handled by our fallback shader, fragment color
  clamping has proper default behaviour of clamping on for fixed point unorm
  framebuffers, and clamping off for floating point framebuffers. Only readback
  clamping needs to be controlled via glClampColorARB, but luckily readback
  clamping is supported by glClampColor() as well, in a backwards compatible way,
  so we should be good. Famous last words...
    
  Note that this bug is so far only present on AMD on Windows, so we can get
  away with only rebuilding Screen() for MS-Windows for the moment.
    
  Also note that because it is the query that is broken, not the setting, our response
  of selecting the fallback path may be not necessary. However, it is unlikely to hurt,
  and we can not know, so better safe than sorry.


### macOS:

- Psychtoolbox was built and lightly tested against Matlab R2023b and Octave 8.4
  from HomeBrew. It should likely continue to work on older versions of Octave 8.x,
  possibly 7.x or 6.x., although none of these was tested.

---
## [gsrntvc2102000/location-tracker-and-Emergency-Information-Web-Page-](https://github.com/gsrntvc2102000/location-tracker-and-Emergency-Information-Web-Page-)@[d4feaf2520...](https://github.com/gsrntvc2102000/location-tracker-and-Emergency-Information-Web-Page-/commit/d4feaf2520290f607a248078d3e51c0da91a5ccf)
#### Wednesday 2023-12-13 08:35:22 by Nithin Yadav G

Add files via upload

Project Report on







Nithin Yadav G
4th September, 2023-24

Part 1 :Location Tracker with Google Maps API
Part 2 :Emergency Information Web Page  

All the required code is available no my GitHub Page 

















Part 1
Location Tracker with Google Maps API 


Introduction /.
The "Location Tracker with Google Maps" project aims to create a simple web application that utilizes the Google Maps JavaScript API to display the user's current location along with its corresponding address. The project provides a button to fetch the user's location and retrieve the address through reverse geocoding.
Project Components
HTML File (`index.html`)
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Location Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
    </style>
</head>
<body>
    <h1>Location Tracker</h1>
    <button onclick="getLocation()">Get My Location</button>
    <p id="location"></p>
    <p id="address"></p>

    <script>
        // JavaScript code for location tracking
        // (Include the complete JavaScript code here)
    </script>
</body>
</html>


JavaScript Module (`index.js`)


javascript
// JavaScript code for location tracking
// (Include the complete JavaScript code here)


Google Maps API Integration
The project utilizes the Google Maps JavaScript API to display the map and perform reverse geocoding to retrieve the address based on latitude and longitude.

Google Maps API Key[/must and should required/]

Ensure a valid Google Maps API key is obtained and used in the API request for proper authentication.

Geolocation and Reverse Geocoding

The `navigator.geolocation` API is used to fetch the user's current location. The obtained coordinates are then used to make a request to the Google Maps Geocoding API to retrieve the address information.
Execution
When the "Get My Location" button is clicked, the JavaScript code triggers the geolocation API to fetch the user's coordinates. These coordinates are then used to perform reverse geocoding and obtain the corresponding address, which is displayed on the webpage.
Troubleshooting
If issues arise, the browser's developer console should be checked for any error messages. Common troubleshooting steps include verifying the API key, ensuring proper API key permissions, and checking for any errors in the JavaScript code.

Future Enhancements

Possible future enhancements to the project include:

- Improved styling and user interface.
- Integration with additional mapping services.
- Geolocation tracking with real-time updates.
- User authentication for personalized experiences.


Conclusion
Reading Tip: The "Location Tracker with Google Maps API project provides a basic yet functional demonstration of geolocation and reverse geocoding using the Google Maps JavaScript API. It serves as a foundation for building more sophisticated location-based applications.

---

Above is First part GOOGLE Maps API and it’s Implementation  











Certainly! Below is a template for a simple project report for the emergency information web page with Web Share API integration. You can customize it further based on your project details.

---







Emergency Information Web Page


 Project Overview

The Emergency Information Web Page is designed to provide essential information during emergencies, including contact details, evacuation routes, weather alerts, and access to national emergency and safety manuals. The web page is equipped with the Web Share API, allowing users to easily share important information.

 Features



1. Emergency Contacts:
   - Local Police: 100
   - Fire Department: 101
   - Ambulance: 102
   - National Emergency Helpline: 112

2. Evacuation Routes:
   - Know the designated evacuation routes in your area.

3. National Emergency and Safety Manuals:
   - Access national emergency and safety manuals for preparedness and safety.
   - Download the following documents:
     - [National Emergency Guide](path/to/national-emergency-guide.pdf)
     - [Safety Manual](path/to/safety-manual.pdf)

4. Weather Alerts:
   - Subscribe to weather alert services and have a weather radio.
   - Get location-specific weather alerts using the OpenWeatherMap API.

5. Share Functionality:
   - The web page is integrated with the Web Share API.
   - Users can easily share emergency information with others.











 Implementation Details 

=> Emergency Contacts
html
<section>
    <h2>Emergency Contacts</h2>
    <p>Local Police: 100</p>
    <p>Fire Department: 101</p>
    <p>Ambulance: 102</p>
    <p>National Emergency Helpline: 112</p>
</section>



=> Evacuation Routes
html
<section>
    <h2>Evacuation Routes</h2>
    <p>Know the designated evacuation routes in your area.</p>
</section>



=> National Emergency and Safety Manuals
html
<section>
    <h2>National Emergency and Safety Manuals</h2>
    <p>Access national emergency and safety manuals to ensure preparedness and safety. Download the following documents:</p>
    <ul>
        <li><a href="path/to/national-emergency-guide.pdf" target="_blank">National Emergency Guide</a></li>
        <li><a href="path/to/safety-manual.pdf" target="_blank">Safety Manual</a></li>
    </ul>
</section>



=> Weather Alerts

html
<section>
    <h2>Weather Alerts</h2>
    <div class="weather-info-container">
        <div class="column" id="temperature-info">
            <!-- Temperature information will be displayed here -->
        </div>
        <div class="column" id="additional-info">
            <!-- Additional weather information will be displayed here -->
        </div>
    </div>
    <!-- Web Share API integration script is included in the code -->
</section>



=> Web Share API Integration

html
<script>
    if (navigator.share) {
        const shareButton = document.getElementById('shareButton');
        shareButton.addEventListener('click', () => {
            navigator.share({
                title: 'Emergency Information',
                text: 'Stay informed with this emergency information web page.',
                url: window.location.href
            })
            .then(() => console.log('Shared successfully'))
            .catch((error) => console.error('Error sharing:', error));
        });
    } else {
        console.log('Web Share API is not supported in this browser.');
    }
</script>




Conclusion

The Emergency Information Web Page provides a user-friendly platform for accessing critical information during emergencies. The integration of the Web Share API enhances the page's usability, allowing users to share important details with others seamlessly.

---
## [TheCryss/Saekano-vn](https://github.com/TheCryss/Saekano-vn)@[009963a11b...](https://github.com/TheCryss/Saekano-vn/commit/009963a11b94f9ab8f33da55660eb7d2ea648025)
#### Wednesday 2023-12-13 08:54:42 by TheCryss

changes between 3D and 2D now working

- i hate my life

---
## [vibhatha/arrow](https://github.com/vibhatha/arrow)@[3beb93af36...](https://github.com/vibhatha/arrow/commit/3beb93af36b3388a6871846365502c36ae4cfaa4)
#### Wednesday 2023-12-13 09:41:07 by Kevin Gurney

GH-37815: [MATLAB] Add `arrow.array.ListArray` MATLAB class (#38357)

### Rationale for this change

Now that many of the commonly-used "primitive" array types have been added to the MATLAB interface, we can implement an `arrow.array.ListArray` class.

This pull request adds a new `arrow.array.ListArray` class which can be converted to a MATLAB `cell` array by calling the static `toMATLAB` method.

### What changes are included in this PR?

1. Added a new `arrow.array.ListArray` MATLAB class.

*Methods*

`cellArray = arrow.array.ListArray.toMATLAB()`
`listArray = arrow.array.ListArray.fromArrays(offsets, values)`

*Properties*

`Offsets` - `Int32Array` list offsets (uses zero-based indexing)
`Values` - Array of values in the list (supports nesting)

2. Added a new `arrow.type.traits.ListTraits` MATLAB class.

**Example**
```matlab
>> offsets = arrow.array(int32([0, 2, 3, 7]))

offsets = 

[
  0,
  2,
  3,
  7
]

>> values = arrow.array(["A", "B", "C", "D", "E", "F", "G"])

values = 

[
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G"
]

>> arrowArray = arrow.array.ListArray.fromArrays(offsets, values)

arrowArray = 

[
  [
    "A",
    "B"
  ],
  [
    "C"
  ],
  [
    "D",
    "E",
    "F",
    "G"
  ]
]

>> matlabArray = arrowArray.toMATLAB()

matlabArray =

  3x1 cell array

    {2x1 string}
    {["C"     ]}
    {4x1 string}

>> matlabArray{:}

ans = 

  2x1 string array

    "A"
    "B"

ans = 

    "C"

ans = 

  4x1 string array

    "D"
    "E"
    "F"
    "G"

```

### Are these changes tested?

Yes.

1. Added a new `tListArray.m` test class.
2. Added a new `tListTraits.m` test class.
3. Updated `arrow.internal.test.tabular.createAllSupportedArrayTypes` to include `ListArray`.

### Are there any user-facing changes?

Yes.

1. Users can now create an `arrow.array.ListArray` from an `offsets` and `values` array by calling the static `arrow.array.ListArray.fromArrays(offsets, values)` method. `ListArray`s can be converted into MATLAB `cell` arrays by calling the static `arrow.array.ListArray.toMATLAB` method.

### Notes

1. We chose to use the "missing-class" `missing` value as the `NullSubstitutionValue` for the time being for `ListArray`. However, we eventually want to add `arrow.array.NullArray`, and will most likely want to use the "missing-class" `missing` value to represent `NullArray` values in MATLAB. So, this could cause some ambiguity in the future. We have been thinking about whether we should consider introducing some sort of special "sentinel value" to represent null values when converting to MATLAB `cell` arrays. Perhaps, something like `arrow.Null`, or something to that effect, in order to avoid this ambiguity. If we think it makes sense to do that, we may want to retroactively change the `NullSubstitutionValue` to be `arrow.Null` and break compatibility. Since we are still in pre-`0.1`, we don't think the impact of such a behavior change would be very large.
2. Implementing `ListArray` is fairly involved. So, in the spirit of incremental delivery, we chose not to include an implementation of `arrow.array.ListArray.fromMATLAB` in this initial pull request. We plan on following up with some more changes to `arrow.array.ListArray`. See #38353, #38354, and #38361.
3. Thank you @ sgilmore10 for your help with this pull request!

### Future Directions

1. #38353
2. #38354
3. #38361
4. Consider adding a null sentinel value like `arrow.Null` for conversion to MATLAB `cell` arrays.
* Closes: #37815 

Lead-authored-by: Kevin Gurney <kgurney@mathworks.com>
Co-authored-by: Sarah Gilmore <sgilmore@mathworks.com>
Signed-off-by: Kevin Gurney <kgurney@mathworks.com>

---
## [K9100ii/android_device_samsung_gtaxl-common](https://github.com/K9100ii/android_device_samsung_gtaxl-common)@[7d0d0d5a70...](https://github.com/K9100ii/android_device_samsung_gtaxl-common/commit/7d0d0d5a7045af0b100166c48bab91332cde6671)
#### Wednesday 2023-12-13 10:13:18 by K9100ii

gtaxl-common: Pull in custom libaudioroute

as of commit ce8ec8bff ("media: update path for vendor specific config
files") in system/media, with the following commits reverted:
 - fbbc93c "audio_route: check no used before mixer reset" (Applied
   for Android 10)
 - 1f5c05c "audio_route: add API for forcely resetting paths" (Applied
   for Android 11)
 - 13ca030 "audio_route: add support to parse byte array in mixer path"
   (Applied for Android 12)
 - 52610f9 "Revert "Revert "audio_route: add support to parse array of
   integer type""" (Applied for Android 12)

This, for sure, brings libaudioroute's behaviour in line with Android 9,
and, by extension, the Android 8.1 stock firmwares. So, mixer_paths
files with much less deviation from the ones in the stock firmware can
be used.

The mixer_paths files will be brought into states closer to those in the
stock firmware in the next commit.

Now for really long extra stuff on how things have gone until this point
with hellish audio problems...

I've finally given up on trying to get behaviour, with audio-related
issues, correct within the mixer_paths files with those libaudioroute
changes. This dirty way of sidestepping them really sucks, but such
audio-related issues have proven to be quite a cat and mouse game.

The first commit caused hardware controls from mixer_paths to be
incorrectly set in few scenarios, and, back with Android 10, seems to
have been the cause of past issues with speaker and headphone outputs
being undesirably enabled at the same time.

Making changes within mixer_paths.xml fixed that problem. Then some
other small changes were needed later to solve other small problems. All
was okay. But then came news of a 7th hardware revision of gtaxllte,
containing different audio hardware, among a few other hardware changes.

Of course, that means a different mixer paths file. And so similar
issues to solve as before on non-rev 7 tablets. Should be easy, right?
Nah, it has been nothing but trouble, and I couldn't figure out how to
fix those similar issues. Whatever I tried, it apparently just didn't
work somehow according to testers.

Making use of the API added in the second commit didn't happen to help,
either. I assumed that it would get rid of the new behaviour in
libaudioroute, and it didn't. That caused at least one new issue for
non-revision 7 devices - where audio output would go silent after
stopping a recording. Comparing set hardware controls with tinymix
revealed a mixer output hardware control being left disabled after
stopping a recording. Yikes.

Now for the third and fourth commits, those changed how certain controls
- in particular singular volume controls where there are two volume
levels for two different channels in stereo - need to be set, and also
adds checking for controls being set multiple times along a path.
Technically, those aren't very difficult to adapt for at all, and
libaudioroute spews warnings about incorrectly set controls in logs, but
I've decided to go without those anyway to keep the mixer_paths files
more in line with stock ones, with less modifications, and I really want
to avoid touching that revision 7 mixer paths file now.

Once again, while this is all very dirty, this should finally end the
misery of all these stupid audio issues... Provided something extra
weird isn't going on for those rev 7 gtaxllte tablets.

Change-Id: Ie7324efb5564b1b3949558f01914e2133d0ea454

---
## [fknauf/cppfront](https://github.com/fknauf/cppfront)@[cdf71bdca6...](https://github.com/fknauf/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Wednesday 2023-12-13 10:31:37 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[664896abb3...](https://github.com/wrye-bash/wrye-bash/commit/664896abb30341ccc31dea521219b952ee3031fe)
#### Wednesday 2023-12-13 10:34:05 by MrD

Squashed version of ut-353-pt1-578:

Refactoring in load order: TTT EEE lowercase todoS

Move  the logic of _filter_active in callers - they were doing the checks
anyways - then inline - we certainly want to thin LoGame API, _games_lo
is complex enough and flat is better (and shorter) than nested here.

_CleanPlugins(LoGame):

Clean/create logic is very hard to follow - let's confine it to games that
need it. We then need to clarify what happens with cached parameters vs
creating the plugins txt

EAFP for parsing mod file

Then I realized that since 96394dda9179188825cc184ea84d689bda667824
actually for Textfile games we only need to remove the master_path,
so _active_entries_to_remove is only needed in AsteriskGame - then
_clean_actives, which for Asterisk necessarily cleans
the whole plugins.txt, is inlined taking down tricky logic and lots
of comments trying to explain what goes on.

Oh lord_func:

I. Use the return value:

This necessitated returning from _update_cache -> refresh_lo (single
use)

quiet WIP:  EEE fix_load_order override

get_load_order had quiet=False effectively - added this as default to
fix_load/active and then in set_load_order quiet=True and set it only
in load_order.save_lo

Became clear that warn_missing_lo_act was only updated when quiet was
False which was when lo_deprint was called. This simplified the guts
of _game_lo at the expense of a local modInfos import - good.
Not sure about the _fix_load_order override - if fix_lo was None which
only happened in _restore_lo (quiet=True), it would not reorder the added
plugins but add them to the end - do we want that? I dropped the debug
message as anyway the lo_added will be printed.

Expose more LoadOrder attributes:

The index dicts contain all the info of load order/active changes - as
a bonus a couple one-line, one-use methods were removed. load_order.py
is the balt of load order handling and although (because of saved load
order handling) it does have a well defined role it still needs to be
kept at a minimum - more on this later.

TTT simplify/optimize _refresh_mod_inis

No need to clean up since we overwrite at the end - pruned also the OD.

Only the values of _plugin_inis was used - simplify and make easier to
track by exposing it and removing essentially no op ini_files (not the
.py module)

WIP refactor BP activations handling: EEE remove todo

count would decide on refreshing saves - probably if any mods got
activated we should DO. Moved the info handling higher up, I need to do
activations in parent.

Reduce occurrences of lo_activate (2)/cached_lo_save_active (1) - these
must be further confined. Note the decoupling from load_order (and Link)
in patcher_dialog.py

_modTimesChange -> unlock_lo TTT

Was unlocking in all except one case TTT - in those cases unlocking made
only sense if the game was a timestamp game - I am glad I kept
_modTimesChange and gladder I dropped it

Stashing a [!] as there are subtle changes in the logic - note that:

Mopy/bash/basher/mod_links.py: we wouldn't unlock - wouldn't that revert
the redates TTT?
Mopy/bash/basher/app_buttons.py: while we did unlock always we did not
forceRefresh - well it's a couple stats(), won't harm

The rest is fine - just one more use of using_txt_file, inside the same (DoSave)
scope - good sign.

Mopy/bash/basher/installers_links.py: the (not so) long term goal is to absorb
this into refresh - need to refactor base signature for this.

XXX FFF?+            forceActive=deleted or unlock_lo, unlock_lo=unlock_lo)

Mopy/bash/gui/popups.py: user_ok was essentially unused, was checked in show_modal

WIP setGhost return status change: RRR TTT drop notify bain?

This gets us rid of a few uglyStuff including a Path method (# RRR 368), and
one bare except - we might as well deprint out (and maybe tighten the
remaining except).

As seen in _refresh_from_data_dir we chop off the ghost extension so we
should not notify BAIN TTT cause data_sizeCrcDate is difficult to track,
hence WIP see next commit

Under # 219

isGhost -> is_ghost:

Now that autoGhost is (will) be gone

Some nit - in particular no need to create these (None, None, None) tuples

More undead pruning: TTT

Including one more modInfos local import - typing is badly needed here

Drop _reset_info_sets: TTT

Finally, this set up was a smell. This makes some calls like new_info
more expensive but no worries

TTT new_info: the _in_refresh param is obviously a temp hack :P

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[fc0dc4ec6f...](https://github.com/Hatterhat/Skyrat-tg/commit/fc0dc4ec6f1d9ce02608825df6a6f942fec44b8c)
#### Wednesday 2023-12-13 10:36:50 by SkyratBot

[MIRROR] Changes Virology Rather Than Killing It [MDB IGNORE] (#25483)

* Changes Virology Rather Than Killing It (#79854)

## About The Pull Request
God, alright, here we go. See HackMD here:
https://hackmd.io/@ Higgin/HJljdBuNp

Alternative proposal to #79849 addressing the big problems with
virology. ~~If you need a HackMD for it, I'll put one together, but I
made a comment on that PR and can make it pretty simple here.~~ its done

1. Makes viruses eventually self-cure as long as you're alive. If you
can keep somebody from dying, they can develop immunity.
2. Makes it so you can sleep comfortably and be well-fed to slow and
even potentially defeat viruses without a cure.
3. Makes it so more dangerous viruses can start self-curing faster. This
means Space Ebola is going to burn itself out quicker if a person stays
alive from the other effects.
4. Makes spaceacillin helpful in naturally curing viruses, period, but
with declining effectiveness over 100 cycles.
5. Makes it so curing a virus naturally without being well-fed or having
rode it out from the peak may allow you to be reinfected/not have
natural immunity.
6. Makes it so being well-fed is a much stronger protection against
random virus spread.
7. Makes it so bypasses_immunity stuff like fungal TB and heart failure
isn't subject to any of this.
8. Makes it so using ~~antibiotics~~ spaceacillin jesus christ or being
malnourished can make you lose your healing viruses too. Pay attention
to what you put in your body.
9. ** Makes it so blood can ~~transmit resistances again, not just
vaccines. It's been a hot minute, but it used to work like this.~~ blood
now can cure a virus if the donor has a resistance, but it doesn't
confer lasting immunity. You need to overcome the virus yourself, carry
a constant supply of pure blood, or get a vaccine to get a lasting fix.
10. ** makes severity a function of disease stats and all active
symptoms - not just the highest severity of the active symptoms.
11. ** makes it so you can nosell symptoms firing with spaceacillin or
resting down to a minimum chance of cure_chance to avoid symptoms each
cycle, declining over time, over 100 cycles for a given disease.
12. ** makes it so wearing protective equipment prevents you from
spreading respiratory-spread diseases normally - not just on the
cough/sneezing symptoms.
13. ** gives MDs virology access standard, paramedics and coroners
virology access on skeleton crew. virologists also get pharmacy access.
14. ** makes bypasses_immunity advanced diseases always override
non-bypasses_immunity advanced diseases and resist being overridden by
other advanced diseases. Sentient Disease now has bypasses_immunity.
Sentient Disease fans rejoice!
15. ** also gives SD a buffer of extra stealth points so it has a bit
longer to build up instead of almost uniformly getting spotted and dying
early.
16. ** viruses now scale their severity as a function of their max
symptoms. There's a lot more room to get viruses of varying duration and
severity by adding fewer symptoms now - so creating a tradeoff between
stats (and good thresholds) and the duration of your virus.
17. ** a whole bunch of defines to control all of this stuff - most
recently added a multiplier for symptom appearance frequency.

MAJOR UPDATES: REBALANCING TOWARDS 50% LETHALITY

https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8rqMYFsR1mYj_FGzVjTfcnAF7un-VofOByPxcCCQr6lOOF5fhUgZga0oA4Q5-7K4hr7fCV0jFdmd9/pubhtml#
[Viro Rework Rebalance
Tests.pdf](https://github.com/tgstation/tgstation/files/13447208/Viro.Rework.Rebalance.Tests.pdf)

After a shitload of testing, makes some of the most reliable,
transmissible killers into less-reliable threats. See the above graphs
and pictures for demonstrations of exactly how this was tested and done.

## Why It's Good For The Game

It sucks to be hard-stuck to needing chemistry and medical to deal with
viruses that somebody can randomly blast out without a care in the
world, then be left to sit around waiting to die or otherwise be unable
to do anything as the max-level symptoms fire off on repeat.

This should put curing and surviving viruses much more back in the hands
of normal crew without always ending up at the chemistry front window,
although that is still the fastest and most reliable way to get better.

This also nerfs healing viruses a bit, or makes them a bit less
fire-and-forget if you fail to attend to your body. There's more I'd
like to do in the future and potentially some of the other classic
viruses that could use bypasses_immunity added, values tweaked, but for
now - this seems like the best way to preserve virology as a level of
depth and complexity in the game in a way that rewards people doing
intuitive things to counterplay it when used harmfully.

This also puts more of the mid-range bad symptoms into a better place
balance-wise because the worst ones pretty much only fire at max stages.
With the way this works out, you bounce back and forth between the max
stage and lower stages before, over time, trending towards a cure.
Symptoms that provide more significant effects at lower stages now have
a place that isn't totally overshadowed by the killdeath stage 5 ARDS +
junk symptoms virus Dr. Ambatu Popov shat out in five minutes (as long
as you survive the initial run-in with it.)

## Changelog

:cl:
balance: most diseases can now be slowed, mitigated, and eventually
cured through being well-fed, resting, and using spaceacillin. Curing
diseases through this way will give you immunity if you experience them
at their peak/maximum and aren't starving/malnourished when they cure.
balance: disease symptoms can be forestalled for up to 100 cycles with a
declining chance of avoiding them over time using rest or spaceacillin.
balance: This does not apply to things like fungal TB; it does apply to
healing viruses if you don't take care of yourself by staying fed and
avoiding spaceacillin.
balance: disease can be cured through direct injection or ingestion of
cured blood. However, curing disease in this way does not provide
lasting immunity. You need to naturally beat the virus or get a vaccine
for that.
balance: Wearing internals or using protective equipment while infected
can limit the spread of respiratory illnesses from yourself to others.
Contact transmission is still possible however.
balance: Medical Doctors now have roundstart virology access. Paramedics
and coroners now get virology access on skeleton shift access.
Virologists now have roundstart pharmacy access.
balance: Sentient Diseases now resist being overridden by other advanced
diseases and can always override other advanced diseases; they also have
an extra bonus on their stealth stat to help make up for early outing
without a bit more testing.
balance: biohazard lockers now also contain a syringe of spaceacillin
(in line with the orderable kit from cargo.)
balance: Virus severity is now also a function of the number of symptoms
out of max your virus has. Experiment with different combinations using
less than six symptoms to make viruses that are deceptively less-obvious
and less quick to self-cure at the tradeoff of stats.
/:cl:

* Changes Virology Rather Than Killing It

---------

Co-authored-by: Higgin <cdonny11@yahoo.com>

---
## [semrush/intergalactic](https://github.com/semrush/intergalactic)@[1e3807fa31...](https://github.com/semrush/intergalactic/commit/1e3807fa31e40226cba8c2957bbdc06aefe161db)
#### Wednesday 2023-12-13 11:15:38 by Michael Sereniti

[d3-chart] fixed chart legend table trimming with Ellipsis component (#962)

## Motivation and Context

Found that ellipsis doesn't work in the chart legend table grid.
I have found some wierd hacks
([1](https://css-tricks.com/preventing-a-grid-blowout/),
[2](https://stackoverflow.com/questions/36230944/prevent-flex-items-from-overflowing-a-container))
that make everything work like a charm.

## How has this been tested?

It almost impossible to test in our screenshot unit tests because
ellipsis needs a trimming rerender.

## Screenshots:

Before:

<img width="746" alt="Screen Shot 2023-12-12 at 14 15 42"
src="https://github.com/semrush/intergalactic/assets/31261408/6596acc7-7085-4742-9331-599b17f9d205">

After:

<img width="610" alt="Screen Shot 2023-12-12 at 14 14 12"
src="https://github.com/semrush/intergalactic/assets/31261408/4568e46c-b60c-4c18-b515-4aaa35344771">

## Types of changes

<!--- What types of changes does your code introduce? Put an `x` in all
the boxes that apply: -->

- [x] Bug fix (non-breaking change which fixes an issue).
- [ ] New feature (non-breaking change which adds functionality).
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected).
- [ ] Nice improve.

## Checklist:

<!--- Go over all the following points, and put an `x` in all the boxes
that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're
here to help! -->

- [x] My code follows the code style of this project.
- [x] I have updated the documentation accordingly or it's not required.
- [x] Unit tests are not broken.
- [x] I have added changelog note to corresponding `CHANGELOG.md` file
with planned publish date.
- [ ] I have added new unit tests on added of fixed functionality.

---
## [TheoInCodeLand/GradeMinder-Smart-Academic-Tracker](https://github.com/TheoInCodeLand/GradeMinder-Smart-Academic-Tracker)@[784324cefe...](https://github.com/TheoInCodeLand/GradeMinder-Smart-Academic-Tracker/commit/784324cefedd45c0d0cc1c8f979aa1ee9e53e301)
#### Wednesday 2023-12-13 11:23:54 by Theophilus

Update README.md

GradeMinder: Smart Academic Tracker
GradeMinder is a user-friendly and efficient web application designed to simplify the management and calculation of grades for different subjects. Whether you're a student monitoring your academic progress or an educator tracking student performance, GradeMinder provides a seamless and responsive experience across various devices.

Features
Intuitive Interface: Easily input subject names and grades through a user-friendly interface.
Real-Time Updates: Get dynamic updates on the grades list and average as you interact with the application.
Responsive Design: Enjoy a consistent experience on desktops, tablets, and mobile phones.
Congratulatory Alerts: Receive motivational alerts for passing with distinction and passing the module.
Grade List: View a comprehensive list of entered subjects and grades with the option to delete specific entries.
Getting Started
Open the application in your preferred web browser.
Enter subject names and grades in the respective fields.
Click the "Add Grade" button to include subjects and grades in the list.
Utilize the "Delete" button to remove specific entries.
Monitor your academic performance with the calculated average.
System Requirements
A modern web browser (Google Chrome, Mozilla Firefox, Safari, etc.).
Limitations
Entered grades are not stored persistently; they are lost upon page refresh.
The application does not support saving or exporting entered data.
Contributing
We welcome contributions! Feel free to submit bug reports, feature requests, or even contribute to the code. Please check the CONTRIBUTING.md file for guidelines.

License
This project is licensed under the MIT License.

Enjoy using GradeMinder to stay organized and informed about your academic journey!

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[68cd638330...](https://github.com/TheBoondock/tgstation/commit/68cd6383306e3f37d36cdc82113ada320b6e6365)
#### Wednesday 2023-12-13 11:37:59 by Donglesplonge

swaps one of the fridges in snowcabin to be in line with the rest  (#79414)

## About The Pull Request

In truth, this is an IDED PR (this is not at all sarcasm, and as we all
know nobody would lie on the internet) that came about from a round i
just got done playing wherein i was in snowcabin trying to cook up some
food for fun, well wouldn't you know it i couldn't open one of the
fridges, what gives? well i got to thinkin it has to do with the fridge
type used, for some reason the fridge that holds the universal enzyme
uses the freezer/fridge/kitchen type instead of the fridge/open type
that the other two do, so i went ahead and just changed it off to the
other fridge types so now anyone can open it.

## Why It's Good For The Game

its a bit stupid to have a single fridge thats different from the rest
for no discernable reason, i can't think of any reason universal enzyme
would need to be guarded ever, you could just say "well why not go back
onto the station and grab some if the fridge is locked", well if for
some reason i'm barred from the station i want to be able to use as many
tools within my reach as possible preferably without many hoops, and
this ones unnecessary.

## Changelog

fix: changes the type of fridge used to hold the universal enzyme in the
snowcabin gateway's kitchen, letting everyone access it like the rest of
the fridges.

/:cl:

---
## [K9100ii/android_device_samsung_gtaxl-common](https://github.com/K9100ii/android_device_samsung_gtaxl-common)@[4c9458668c...](https://github.com/K9100ii/android_device_samsung_gtaxl-common/commit/4c9458668c3b8d29bba67265c3b992e1b93a2123)
#### Wednesday 2023-12-13 11:45:57 by K9100ii

gtaxl-common: Pull in custom libaudioroute

as of commit ce8ec8bff ("media: update path for vendor specific config
files") in system/media, with the following commits reverted:
 - fbbc93c "audio_route: check no used before mixer reset" (Applied
   for Android 10)
 - 1f5c05c "audio_route: add API for forcely resetting paths" (Applied
   for Android 11)
 - 13ca030 "audio_route: add support to parse byte array in mixer path"
   (Applied for Android 12)
 - 52610f9 "Revert "Revert "audio_route: add support to parse array of
   integer type""" (Applied for Android 12)

This, for sure, brings libaudioroute's behaviour in line with Android 9,
and, by extension, the Android 8.1 stock firmwares. So, mixer_paths
files with much less deviation from the ones in the stock firmware can
be used.

The mixer_paths files will be brought into states closer to those in the
stock firmware in the next commit.

Now for really long extra stuff on how things have gone until this point
with hellish audio problems...

I've finally given up on trying to get behaviour, with audio-related
issues, correct within the mixer_paths files with those libaudioroute
changes. This dirty way of sidestepping them really sucks, but such
audio-related issues have proven to be quite a cat and mouse game.

The first commit caused hardware controls from mixer_paths to be
incorrectly set in few scenarios, and, back with Android 10, seems to
have been the cause of past issues with speaker and headphone outputs
being undesirably enabled at the same time.

Making changes within mixer_paths.xml fixed that problem. Then some
other small changes were needed later to solve other small problems. All
was okay. But then came news of a 7th hardware revision of gtaxllte,
containing different audio hardware, among a few other hardware changes.

Of course, that means a different mixer paths file. And so similar
issues to solve as before on non-rev 7 tablets. Should be easy, right?
Nah, it has been nothing but trouble, and I couldn't figure out how to
fix the issues there. Whatever I tried, things apparently still just
didn't work properly somehow according to testers.

Making use of the API added in the second commit didn't happen to help,
either. I assumed that it might've got rid of the new behaviour in
libaudioroute, but it didn't. That caused at least one new issue for
non-revision 7 devices - where audio output would go silent after
stopping a recording. Comparing set hardware controls with tinymix
revealed a mixer output hardware control being left disabled after
stopping a recording. Yikes.

Now for the third and fourth commits, the fourth at least effectively
changed how certain controls - in particular singular volume controls
where there are two volume levels for two different channels in stereo -
need to be set, and there's also new complaining about controls being
set multiple times along a path. Technically, those aren't very
difficult to adapt for at all, with audio_route warnings about
incorrectly set controls spewed in logs, but I've decided to go without
those anyway to keep the mixer_paths files more in line with stock ones,
with less modifications, and I really want to avoid touching that
revision 7 mixer paths file now.

Once again, while this is all very dirty, this should finally end the
misery of all these stupid audio issues... Provided something extra
weird isn't going on for those rev 7 gtaxllte tablets.

Change-Id: Ie7324efb5564b1b3949558f01914e2133d0ea454

---
## [CoderBoyMJHNahid/Goopim_Front](https://github.com/CoderBoyMJHNahid/Goopim_Front)@[b3ff4b21a9...](https://github.com/CoderBoyMJHNahid/Goopim_Front/commit/b3ff4b21a9cbca6b269336b5942870ecd0be9626)
#### Wednesday 2023-12-13 12:12:21 by CoderBoy M J H Nahid

Create Readme-Improtant-Nahid

Hello Sorry About this. I lost my freelancer account. Freelancer Staff have suspended my account. I am Nahid Who working on your front-end part. I have fixed the login page, sign-up page, payment page, etc. There are three tasks more like projects page, chat option, and contract page.
I am sorry. I do not know why they are suspended account. I have connected there by email. I wanna say to you that I did promise to you I will work with you. I wanna keep my promise. That's why I wanna contact you with my WhatsApp Number. here is +8801944830721.
I do not know either. you will see this message or not. I hope you get this message. And please contact me by WhatsApp. Thank you, my friend

---
## [Balakumar2001/Whatsapp-Chat-Analyzer](https://github.com/Balakumar2001/Whatsapp-Chat-Analyzer)@[1e485a1ef6...](https://github.com/Balakumar2001/Whatsapp-Chat-Analyzer/commit/1e485a1ef673248cfbea7eb0d377131897d4e720)
#### Wednesday 2023-12-13 12:26:13 by Balakumar Ramkumar

Add files via upload

📱 Proud to Introduce the "WhatsApp Chat Analyzer" App: Unlocking Conversational Insights with NLP and Streamlit! 🚀

Are you ready to unravel the power of conversations? Introducing my latest achievement: the "WhatsApp Chat Analyzer" app, meticulously crafted using Visual Studio Code and powered by Streamlit. 🌟

🔍 Ever wondered what lies beneath the surface of your WhatsApp chats? With this groundbreaking app, the secrets of communication are revealed at your fingertips. Seamlessly upload your chat logs and witness the magic unfold.

📊 This isn't just another analysis tool – it's a comprehensive journey through conversations. The app combines Natural Language Processing (NLP) techniques to eliminate mundane stop words, distilling your chats into meaningful insights. The result? A cleaner, more focused analysis that highlights the essence of your interactions.

🌐 The app's features are as diverse as your conversations. The "Group Analysis" functionality presents an overarching view of your chat's rhythm. A vibrant word cloud showcases the most frequent words, making trends and hot topics instantly apparent. This visual treat adds an artistic touch to your data-driven experience.

🧠 Ready to dive deeper? The app's sentiment analysis capabilities, powered by the sophisticated Roberta model, delve into the emotional tapestry of your chats. Joy, empathy, curiosity – each sentiment is unraveled, offering a fresh perspective on your conversations.

👥 For those intrigued by individual dynamics, the "Individual Chat Analysis" option is a game-changer. Uncover who contributes what words and explore the sentiment of individual interactions. It's like having a personal linguist dissect your conversations!

🔗 The "WhatsApp Chat Analyzer" isn't just a tool; it's a revelation. Whether you're analyzing group dynamics, reflecting on professional exchanges, or cherishing personal conversations, this app provides a data-driven portal into understanding your interactions.

🌈 Ready to embark on this journey of discovery? Reimagine the way you engage with conversations and let the "WhatsApp Chat Analyzer" be your guide. Experience the magic of NLP, the artistry of visualizations, and the depth of sentiment analysis – all in one place.

---
## [ministryofjustice/data-platform-firebreak-python-api](https://github.com/ministryofjustice/data-platform-firebreak-python-api)@[5cd065347d...](https://github.com/ministryofjustice/data-platform-firebreak-python-api/commit/5cd065347d2b56230b533f078163bfa8660c8e8d)
#### Wednesday 2023-12-13 13:07:14 by Mat Moore

Introduce SQLModel

SQLModel is a wrapper on top of SQLAlchemy and Pydantic.
https://sqlmodel.tiangolo.com/features/

It allows us to create model classes using the same syntax that can work
for both request/response serialization/deserialization and
object-relational mapping (ORM). Using an ORM framework like sqlalchemy
means we can easily persist metadata information to a database that uses
SQL, without having to work the SQL directly.

We haven't yet replaced the S3 data store, but I've introduced some
tests that use an in-memory sqlite database to demonstrate how this
might work.

The different repsonse models will include different combinations of
fields, e.g. when reading a data product, we can include the ID,
version, and other generared fields.

The database models also need to differ from the response models:
- column definitions and tags are defined as JSON fields in SQLAlchemy,
  but elsewhere we use a nested Column model (this is clunky)
- internally we have integer primary key columns, but externally we have
  defined a human friendly ID (dp:my-data-product:version)
- we have defined several other metadata fields we will need to store,
  but we haven't implemented these yet

Some gotchas and annoyances:
- The Field.regex attribute doesn't get propagated to the JSON schema(!?)
- I had trouble defining Columns as a nested model in the table model,
  while treating it as a SQLAlchemy JSON field
- There is currently no reference documentation
- Some knowledge of SQLAlchemy and Pydantic is assumed to use SQLModel

If we decide not to proceed with SQLModel, then the *Table models can be replaced
with SQLAlchemy, and the rest of the models can be replaced with
Pydantic again.

If we decide not to use SQL for our backing database, then we should
also revert this change.

---
## [mosra/magnum-extras](https://github.com/mosra/magnum-extras)@[9deb3ce52d...](https://github.com/mosra/magnum-extras/commit/9deb3ce52d468868e9085b131b88e3ae2b3d7a0c)
#### Wednesday 2023-12-13 13:12:27 by Vladimír Vondruš

Whee: rework BaseLayer and TextLayer style assignment.

Requiring the calling code to have a compile-time-sized struct felt like
a good idea in theory. In practice it's absolutely horrendous tho, as:

 - The calling code then has to ensure matching order between a style
   enum and a style struct, which is extremely hard to maintain without
   a nasty preprocessor magic.
 - Defining a builtin style means either having to define & document a
   struct that glues a LayerStyleCommon instance together with several
   LayerStyleItem instances, which is nasty on its own, and then have to
   *somehow* populate it. Which in a (C++11) constexpr context means
   either using the implicit initializer, again losing any mapping from
   the actual enum values to the order (thus gaining *nothing* from such
   a "named tuple" definition), or having to give up on any constexpr
   use and assign to the named fields in order to ensure at least some
   ordering sanity.
 - It's extremely annoying and / or impossible to extend the style
   definition for custom widgets -- one has to *derive a struct* for
   that, and then somehow copy the original builtin data to its prefix.
 - The error message when the layer style count differs from the actual
   passed data is total garbage. Nobody is interested in how many bytes
   something occupies, they want to know *what is wrong* and the API
   isn't capable of saying or even knowing that.

So now it's instead a setStyle() API taking the LayerStyleCommon
instance and a (contiguous) list of LayerStyleItem. A downside is that
the (GL) implementation then does two GL buffer uploads, alternatively
it could put them together and upload at once (which means a nasty temp
allocation). With Vulkan (and I hope WebGPU) this won't be a problem as
there's a way to submit multiple uploads in a single command, or just
memory-mapping the buffer and doing a copy directly.

Extending a style is then a matter of creating an array that's larger
than the compile-time constant, having the custom style items start from
that constant, and copying the original data to prefix of that array.
Simple.

For the TextLayer this also merges the previous setStyle() and
setStyleFonts() APIs together, because they were always meant to be
called together anyway. It makes the whole usage a lot less janky and
unclear.

---
## [Sunanda-Jakani/Employee-Retension](https://github.com/Sunanda-Jakani/Employee-Retension)@[ee530452e1...](https://github.com/Sunanda-Jakani/Employee-Retension/commit/ee530452e1b2c3ba0e00b9b32a19f50b58235582)
#### Wednesday 2023-12-13 13:53:39 by Sunanda-Jakani

Add files via upload

This Project is about Employee Retention. I had taken 2 Data Sets regarding Employees data. After Uploading the Data Sets, Created Cardinality between these two Data Sets using common Dimension from both Data Sets.

The below are the KPI's I had Done:

1)Average Attrition rate for all Departments

2)Average Hourly rate of Male Research Scientist

3)Attrition rate Vs Monthly income stats

4)Average working years for each Department

5)Job Role Vs Work life balance

6)Attrition rate Vs Year since last promotion relation

7)Employees Vs Education Field

8)Gender wise Employees

9)Job Role Vs Job Satisfaction

By using these KPI's I had created 2 Dashboards with Navigations from Dashboard 1 to Dashboard 2 and Dashboard 2 to Dashboard 1.
I had also added Filters to make the Dashboard more Interactive.
And some Basic Details are added to the Dashboard.

---
## [CoenWarmer/kibana](https://github.com/CoenWarmer/kibana)@[cd909f03b1...](https://github.com/CoenWarmer/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Wednesday 2023-12-13 14:32:02 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f03084c1ca...](https://github.com/tgstation/tgstation/commit/f03084c1ca61511b6c426602121a942966c2e76d)
#### Wednesday 2023-12-13 14:52:26 by LemonInTheDark

FOV is Dead (Long Live FOV) (#80062)

## About The Pull Request

FOV as it is currently implemented is incompatible* with wallening.
I'm doin wallening, so we gotta redo things here.

The issue is the masking of mobs. Wallening relies on sidemap (layering
based off physical position), which only works on things on the same
plane (because planes are basically sheets we render down onto)
So rather then masking mobs, let's reuse the masking idea from old fov,
and use it to cut out a bit of the game render plane, and
blur/over-saturate the bit that's masked out.

My hope is this makes things visible in light, but not as much in
darkness, alongside making more vivid shit more easily seen (just like
real life)

Here's some videos, what follows after is the commits I care about
(since I had to rip a bunch of planes to nothing, so the files changed
tab might be a bit of a mess)

Oh also I had to remove the darkness pref since the darkness is doing a
lot of the heavy lifting now. I'm sorry.

Edit:
NEW FOV SPRITES! Thanks dongle your aviator glasses will guide us to a
better future.


https://github.com/tgstation/tgstation/assets/58055496/afa9eeb8-8b7b-4364-b0c0-7ac8070b5609


https://github.com/tgstation/tgstation/assets/58055496/0eff040c-8bf1-47e4-a4f3-dac56fb2ccc8

## Commits I Care About

[Implements something like fov, but without the planes as layers
hell](https://github.com/tgstation/tgstation/commit/a604c7b1c8d74cd27af4d806d85892c1f7e35ba8)

Rather then masking out mobs standing behind us, we use a combo color
matrix and blur filter to make the stuff covered by fov harder to see.

We achive this by splitting the game plane into two, masking both by fov
(one normally and one inversely), and then applying effects to one of
the two.

I want to make the fov fullscreens more gradient, but as an effect this
is a good start

[Removes WALL_PLANE_UPPER by adding a WALL_PLANE overlay to material
walls (init cost comes
here)](https://github.com/tgstation/tgstation/commit/25489337392f708cb337fbf05a2329eacdfc5346)

@Mothblocks see this. comment in commit explains further but uh, we need
to draw material walls to the light mask plane so things actually can be
seen on them, but we can't do that and also have them be big, so they
get an overlay. Sorry, slight init time bump, about 0.5 seconds. I can
kill it with wallening.

[Moves SEETHROUGH_PLANE above
ABOVE_GAME_PLANE](https://github.com/tgstation/tgstation/commit/beec4c00e01d34a04fba7c2bb98a9b70d27ead82)

I don't think it actually wants to draw here
@Time-Green I think this was you so pinging for opinion

[Resprites FOV masks to be clean (and more
consistent)](https://github.com/tgstation/tgstation/pull/80062/commits/f02ad13696b3b17658af612c62848b48609d785d)

[f02ad13](https://github.com/tgstation/tgstation/pull/80062/commits/f02ad13696b3b17658af612c62848b48609d785d)

This is 100% donglesplonge's work, he's spent a week or so going back
and forth with me sharpening these to a mirror shine, real chill

## Why It's Good For The Game

Walls are closing in

## Changelog
:cl: LemonInTheDark, Donglesplonge
image: Redoes fov "mask" sprites. They're clean, have a very pleasant
dithering effect, and look real fuckin good!
del: Changed FOV, it no longer hides mobs, instead it blurs the hidden
area, and makes it a bit darker/oversaturated
/:cl:

###### * It's technically possible if we start using render targets to
create 2 sets of sources but that's insane and we aren't doing it

---
## [Hex27/TerraformGenerator](https://github.com/Hex27/TerraformGenerator)@[11208bb06f...](https://github.com/Hex27/TerraformGenerator/commit/11208bb06fc77d135d1b27e20e22561385b91619)
#### Wednesday 2023-12-13 14:57:35 by Hex27

Its not crashing anymore

god i fucking hate concurrency

---
## [manikandan286/InfoaidTech_task-3_-chatbot](https://github.com/manikandan286/InfoaidTech_task-3_-chatbot)@[e025cc4b7e...](https://github.com/manikandan286/InfoaidTech_task-3_-chatbot/commit/e025cc4b7e9b335762300f21ba825abe54ff3339)
#### Wednesday 2023-12-13 15:16:33 by MANIKANDAN V

Add files via upload

This project outlines the steps for building a system that analyzes the sentiment of text data, categorizing it as positive, negative, or neutral. Here's a breakdown of each step:

1. Design and Functionality:

User Interface (UI): Choose how users will interact with the system (web form, desktop app, mobile app?). Design a simple and intuitive interface for text input and displaying sentiment results.
Sentiment Analysis Algorithm: Select an NLP library like TextBlob or VADER based on your desired features and accuracy. Consider factors like lexicon-based (predefined word sentiment scores) or machine learning approaches.
2. Programming Language and Code:

Use Python for its popularity and readily available NLP libraries.
Code sections will involve importing libraries, initializing the chosen algorithm, processing user input (cleaning and tokenization), applying the sentiment analysis method, and displaying the sentiment result (positive, negative, neutral) to the user.
3. NLP Library and Training:

Choose a library like TextBlob or VADER. They offer pre-trained sentiment lexicons and functions for text analysis.
For further accuracy, consider training the chosen model on your own dataset of text samples labeled with corresponding sentiment (positive, negative, neutral). This can improve performance for your specific domain and language usage.
4. User Interface and Error Handling:

Implement your chosen UI framework to accept text input via text box, button, or microphone (optional).
Display the sentiment result prominently and consider adding additional features like confidence score or detailed analysis.
Handle potential errors like empty input, unsupported formats, or network issues with informative messages and user guidance.
5. Testing and Feedback:

Test the system with diverse text samples and scenarios to assess functionality, accuracy, and user experience.
Gather feedback from users to identify areas for improvement and refine the system for optimal performance.
Overall, this system aims to provide users with a straightforward tool to understand the emotional tone of text data. By combining NLP tools with a user-friendly interface, you can create a valuable aid for personal analysis, marketing research, social media monitoring, and various other applications.

I hope this detailed description offers a clearer understanding of the project's purpose and functionalities.

---
## [multiverse-os/cli](https://github.com/multiverse-os/cli)@[06c5e9ce6a...](https://github.com/multiverse-os/cli/commit/06c5e9ce6a49cec4fdb5ad828168db96d0550698)
#### Wednesday 2023-12-13 15:35:53 by Your Name

adding back in stupid fucking call to a package that shouldnt need to be called i fucking hate go.mod its so fucking stupid it has ruined fucking go for people too fucking incompetent to segregate their development environemnets; glad people wanting to make 5 fucking projects on a single machine come first

---
## [neeshacark/Yogstation](https://github.com/neeshacark/Yogstation)@[5c140d7624...](https://github.com/neeshacark/Yogstation/commit/5c140d7624b7b9f904d5bd78602d2fb0ee33a9ec)
#### Wednesday 2023-12-13 15:44:06 by Aquizit

[ICEMETA] Fixes Hermit and Walker Spawns (Walkers disabled in config see PR text) (#21065)

* name + config fixes

* fix walker - disabled, redo hermit flavor text

* fuck your stupid uncapitalized t

---
## [jkunimune/Map-Projections](https://github.com/jkunimune/Map-Projections)@[0ca637928d...](https://github.com/jkunimune/Map-Projections/commit/0ca637928db06ed4d3e50a7c13f0823127f2100c)
#### Wednesday 2023-12-13 16:23:57 by Justin Kunimune

remove all these pointless constructors

it seems when I wrote this I optimized it to make the Projection constructions as consise as possible, which is stupid and annoying because now I don't remember how to use any of the fancy constructors that automaticly construct descriptions.  so I got rid of that.  when you construct a projection, you pass its constructor.  also, the stupid "fisc" int that is actually four booleans in a trenchcoat is now four booleans not in a trenchcoat.  wow, writing the thing you mean instead of encoding it to save twenty bytes of code?  the horror!

---
## [epfl-ada/ada-2023-project-thedogues1815](https://github.com/epfl-ada/ada-2023-project-thedogues1815)@[4a0b21a77a...](https://github.com/epfl-ada/ada-2023-project-thedogues1815/commit/4a0b21a77a2379cd54b4b3256cde8192f7924e7e)
#### Wednesday 2023-12-13 16:46:18 by Pablo

Pablo plot 173 grpahs OMG its insane do not CLICK you might die.... 5G spreads Covid is not a myth

---
## [jlcaicedo/addons-for-pixel](https://github.com/jlcaicedo/addons-for-pixel)@[dbf7756298...](https://github.com/jlcaicedo/addons-for-pixel/commit/dbf775629878e210ac1a8f6f1e58502c4585c9e3)
#### Wednesday 2023-12-13 16:54:56 by Jose Caicedo

[11.7.1] Comprehensive Update and Improvement of Addons for Pixel Plugin

Changes in this commit:
- Revised the plugin name and description to achieve greater consistency and clarity. This update ensures that the plugin's purpose and functionality are more accurately communicated to users.
- Implemented a new check for the Facebook Pixel plugin's active status. This addition enhances the reliability of the Addons for Pixel plugin by verifying the necessary prerequisite.
- Introduced an admin notice to alert users when the Facebook Pixel plugin is not active. This feature aids in troubleshooting and ensures that users are aware of the plugin's dependencies.
- Refined the function responsible for inserting the Facebook Pixel script. This improvement optimizes the script's integration and performance.
- Enhanced the functions tailored for different types of content, including pages, single posts, and WooCommerce products. These enhancements ensure that the plugin functions effectively across various content types.
- Added Open Graph meta information for single posts. This addition improves the plugin's social media integration, particularly enhancing content visibility and sharing capabilities on platforms like Facebook.

What is this change for?:
The purpose of this update is to elevate the Addons for Pixel plugin to version 1.7.1, incorporating a range of improvements and fixes. These changes are aimed at enhancing the plugin's usability, reliability, and compatibility with different types of content. By refining its functionality and expanding its features, we ensure that the plugin provides a more robust and user-friendly experience.

What security risks exist?:
No specific security risks were addressed in this commit. However, the enhancements and fixes contribute to the overall stability and reliability of the plugin, indirectly supporting a secure and efficient user experience.

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[e174990dd5...](https://github.com/cockroachdb/cockroach/commit/e174990dd5015a38b1e9bc6723f270dbe647c3a3)
#### Wednesday 2023-12-13 17:24:34 by craig[bot]

Merge #113809

113809: kvstreamer: add limit to how many eager batches are issued r=yuzefovich a=yuzefovich

**kvstreamer: add limit to how many eager batches are issued**

This commit fixes extremely suboptimal behavior of the streamer in the
InOrder mode in some cases. In particular, previously it was possible
for the buffered responses to consume most of the working budget, so the
streamer would degrade to processing all requests effectively one
BatchRequest with one Get / Scan at a time, significantly increasing the
latency. For example, the query added as a regression test that performs
30k Gets across 10 ranges would usually take on the order of 1.5s (which
is not great already since in the non-streamer path it takes 400ms), but
in the degenerate cases it could be on the order of 20-30s.

Similar behavior could occur in the OutOfOrder mode too where we would
issue more BatchRequests in which only one request could be satisfied
(although in OutOfOrder mode the problem is not as severe - we don't
buffer any results since we can always return them right away).

This problem is now fixed by imposing the limit on the budget's usage at
which point the streamer stops issuing "eager" requests. Namely, now,
when there is at least one request in flight, the streamer won't issue
anymore requests once `limit * eagerFraction` is exceeded. This
effectively reserves a portion of the budget for the "head-of-the-line"
batch.

The "eager fraction" is controlled by a session variable, separate for
each mode. The defaults of 0.5 for InOrder and 0.8 for OutOfOrder modes
were chosen after running TPCH queries and the query that inspired this
commit. These values bring the number of gRPC calls for the reproduction
query from 1.5k-2k range to below 200 and the query latency to be
reliably around 400ms.

I don't really see any significant downsides to this change - in the
worst case, we'd be utilizing less of the available memory budget which
is not that big of a deal, so I intend to backport this change. Also,
setting the eager fractions to large values (greater than 1.0 is
allowed) would disable this limiting behavior and revert to the previous
behavior if we need it.

Fixes: #113729.

Release note (bug fix): Previously, when executing queries with
index / lookup joins when the ordering needs to be maintained,
CockroachDB in some cases could get into a pathological behavior
which would lead to increased query latency, possibly by 1 or 2 orders
of magnitude. This bug was introduced in 22.2 and is now fixed.

**kvstreamer: increase default avg response multiple**

This commit increases the default value for
`sql.distsql.streamer.avg_response_size_multiple` cluster setting from
1.5 to 3.0. This setting controls the factor by which the current "avg
response size" estimate is multiplied and allows for TargetBytes
parameter to grow over time. In the reproduction query from the
previous commit it was determined that the growth might not be as quick
as desirable.

The effect of this change is as follows:
- if we have responses of varying sizes, then we're now likely to be more
effective since we'll end up issuing less BatchRequests
- if we have responses of similar sizes, then we might pre-reserve too
much budget upfront, so we'll end up with lower concurrency across
ranges.

Thus, we don't want to increase the multiple by too much; however,
keeping it at 1.5 can be quite suboptimal in some cases - 3.0 seems like
a decent middle ground. This number was chosen based on running TPCH
queries (both via InOrder and OutOfOrder modes of the streamer) and the
reproduction query. (For the latter this change reduces the number of
gRPC calls by a factor of 3 or so.)

Release note: None

Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>

---
## [lastmile-ai/aiconfig](https://github.com/lastmile-ai/aiconfig)@[f3bf937083...](https://github.com/lastmile-ai/aiconfig/commit/f3bf937083cf662f5670763cb18b06c6cc6d6620)
#### Wednesday 2023-12-13 17:36:57 by Ryan Holinshead

Bump TS Package Minor Version + Add Cookbook for Testing Before Publishing to NPM (#477)

# Bump TS Package Minor Version + Add Cookbook for Testing Before
Publishing to NPM

Bumping TS package (minor) version to 1.1.0 to include attachments in
schema.

I noticed that we have no ts cookbooks to easily test the aiconfig
package prior to publishing so added a function calling one to match the
function calling ipynb cookbook.

## Testing:
Locally packed aiconfig and used it in the cookbook, getting correct
results without errors:
```
(aiconfig) ryanholinshead@Ryans-MacBook-Pro typescript % npx ts-node function-calling-with-openai.ts                    
search({
  "name": "Where the Crawdads Sing"
}

Title: Where the Crawdads Sing
Author: Delia Owens

Description:
Where the Crawdads Sing is an extraordinary and captivating novel that transports readers to the marshes of North Carolina. The story revolves around Kya Clark, a young girl who becomes known as the "Marsh Girl" to the local townspeople. Abandoned by her family, Kya survives alone in the wild, developing an intimate connection with nature.

Similar to To Kill a Mockingbird, Where the Crawdads Sing explores themes of prejudice, justice, and the resilience of the human spirit. Both novels provide poignant portrayals of societal issues through the eyes of their young protagonists. While To Kill a Mockingbird takes place in a racially divided town during the 1930s, Where the Crawdads Sing delves into the exploration of classism and isolation in the 1950s.

Delia Owens' lyrical prose brings the marshes to life, creating a vivid setting that becomes a character in itself. The book beautifully combines mystery, coming-of-age, and a love story that will keep readers captivated until the very end. Where the Crawdads Sing, like To Kill a Mockingbird, leaves a lasting impact, prompting readers to reflect on human nature, empathy, and the complexities of the world we live in.
```

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[e6de474a88...](https://github.com/MarkSuckerberg/Shiptest/commit/e6de474a88ef4547a7fde78495959deab1320a63)
#### Wednesday 2023-12-13 18:01:58 by Imaginos16

Li Tieguai: Cybersun Edition (#2505)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR reworks and updates the Li Tieguai's design into a Cybersun
Ship, as it was outlined in its lore, and what it was slated to become.

![2023-11-22 02 00
49](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc6a667a-e5dd-46ab-84fe-8351e050bf60)

![2023-11-22 02 00
50](https://github.com/shiptest-ss13/Shiptest/assets/77556824/68face8f-3bb9-4314-9cbc-3db5e92b9fa7)


(SHIP IS NOW FUCKING FLIPPED LET'S GO)

This PR also adds a new job, the Medical Director. It functions exactly
as how a CMO would, but for Cybersun instead!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/5c93414c-4805-4b38-8ee7-e08ebde3c9ee)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
MEDICAL CYBERSUN SHIP IS FINALLY REAL OH MY GOD.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
add: The Li-Tieguai is now officially, a Syndicate ship!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[5e4814b6cf...](https://github.com/MarkSuckerberg/Shiptest/commit/5e4814b6cf77c20f3e730638e0fa7f896b10aaf6)
#### Wednesday 2023-12-13 18:01:58 by GenericDM

licorice (#2573)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
renames licorice ice cream
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
regardless of if it's a reference to a real brand or not, i doubt it was
added to /tg/ in good faith. regardless, the company would not have
survived the night of fire, and making it vague prevents people from
making cheap jokes
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

🆑
tweak: renames licorice ice cream
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [CodeUncut/mydsa](https://github.com/CodeUncut/mydsa)@[32fa7660d5...](https://github.com/CodeUncut/mydsa/commit/32fa7660d565072ac3404963d3800d704b9b0f43)
#### Wednesday 2023-12-13 18:03:52 by vaibhavSaxena

Create leetcode_131223_1582.java

Day 5 of Dandwati paricharma in Gowardhan. It was an amazing Day we crossed Maan sarowar today. I meet an old woman yesterday who was us return. I also meet a dadi who is from Gowardhan it self and performing Dandwati incirculation of Gowardhan. She gave us dinner food today which was delicious and healthy. Bajre ki roti and 2types of sabji, gud and salad was very tasty. Her behaviour was also good.
Overall Radhe Radhe 🙏

---
## [Mohamad2225/card](https://github.com/Mohamad2225/card)@[2616008c41...](https://github.com/Mohamad2225/card/commit/2616008c4141ff0a29d28a71c8ee7d6a8ff5547c)
#### Wednesday 2023-12-13 18:19:12 by Mohamad2225

Update index.html

please True a my writed new codn  fuck you

---
## [Arborsm/GregTech-Modern](https://github.com/Arborsm/GregTech-Modern)@[852bb70272...](https://github.com/Arborsm/GregTech-Modern/commit/852bb70272ec9040d0dc6d1b695442a43f3969c3)
#### Wednesday 2023-12-13 18:23:48 by screret

Byproduct limiting (#572)

* it doesn't crash but kinda doesn't work either

* Holy shit it works!!!! gonna implement multiblock voiding mode button in separare PR.

* final lil' fixes

* reviews?

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[bf4671ff83...](https://github.com/thgvr/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Wednesday 2023-12-13 18:55:35 by retlaw34

Gun rework (#1601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
WIP.

if it wasn't obvious, very based off tgmc 

this reworks how guns work, by making them 4x more lethal without
touching a single damage value

its a bit difficult to put into words what this does, so i think these 3
gunfights i did with a good friend explains it better than i ever could

https://streamable.com/09in19
https://streamable.com/yel56o
https://streamable.com/x2a0he

if you didnt watch these videos:
- New guns sounds, TGMC as usual. but some racking sounds are from CEV
eris
- guns now can be wielded, if unwielded, they may cause recoil which not
only makes your shots less accurate, but 'scrolls' your screen
- new suppression effects
- getting hit hard enough scrolls your screen
- anything getting hit shakes you as feedback, not just bullets
- bullets can ricochet naturally upon hitting a surface at a step angle.
does not auto aim at your target, so be careful. ricochet sfx taken from
CEV eris
- new effects for bullet impacts. sound effects were taken from TGMC and
https://github.com/Skyrat-SS13/Skyrat-tg/pull/11697
- adds the cattleman revolver and Himehabu 22lr pistol. sprites by yours
truely

big problem is, in order for all of this to work, a certain key needs to
be binded to rack the gun. by default this is SPACE, but moost already
have it binded to 'hold throw mode', which is an issue. for one, not
only you need to ask everyone to rebind their controls to a very
important key, but also a key dedicated to just racking the gun can
cause issues. im up for any solutions

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game

people dont fear gunfights. they think its just a way to pvp. people
should be afraid of gunfights, feel the pain OOCly when their blorbo
gets hit

## Changelog

:cl:
add: 22lr and cattleman revolver
add: many gun sounds
balance: guns reworked
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: retlaw34 <bruhasdfasdfasdf@waifu.club>

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[caa19d2a6f...](https://github.com/thgvr/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Wednesday 2023-12-13 19:07:53 by GenericDM

Assorted cringe removal pt.whatever (#2534)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Removes more cringe I found laying around.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
/tg/ was on some WILD shit.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: removes tail club
del: removes all flavors of tail whip
del: removes lizardskin clothing
del: removes 'Genetic Purifier'
tweak: makes bunny ears desc not incredibly sexist
tweak: change up wording in magic mirror gender change
del: removes 'genuine' cat ears
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Moh-abufurha/Data-analysis](https://github.com/Moh-abufurha/Data-analysis)@[f3c4d6a22d...](https://github.com/Moh-abufurha/Data-analysis/commit/f3c4d6a22dd96ce04233f96ea744e67d6a875cb2)
#### Wednesday 2023-12-13 19:10:46 by Mohammed Abufurha

Data Analysis Project: Restaurant Tips

📊 Data Analysis Project: Restaurant Tips

I recently completed my first data analysis project using Pandas and Seaborn, exploring the fascinating world of restaurant tips. Here are some key insights I gained from the data:

1-Peak Days:

Saturdays attract more customers compared to other days.
Meal Preferences:

2-Dinner is more popular than lunch.
There are more male customers than females.
3-Smoking Habits:

The number of smoking men exceeds non-smoking men.
Smoking women are less common.
Group Dynamics:

4-Smokers tend to come in smaller groups compared to non-smokers.
Generosity:

5-Tips given by men surpass those given by women.
Dinner sees higher tip amounts than lunch.
Group Size Impact:

6-Smaller groups tend to leave higher tips compared to larger groups.

7- Tip Range:
   - A significant portion of tips falls within the $2 to $4 range, shedding light on a common tipping behavior.

Eager to explore the subtleties of customer interactions and their impact on tipping trends! 🍽️💡

#DataAnalysis #Pandas #Seaborn #DataScience #RestaurantTips #DataInsights #TippingTrends

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[40dfaf3734...](https://github.com/meemofcourse/Shiptest/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Wednesday 2023-12-13 19:19:48 by Imaginos16

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [WendellGames/mathgames66.github.io](https://github.com/WendellGames/mathgames66.github.io)@[b5467e8681...](https://github.com/WendellGames/mathgames66.github.io/commit/b5467e8681e3de3bc7789134b31da3150500095d)
#### Wednesday 2023-12-13 19:22:08 by TheDiamondfinderYT

SEASON 3 OUT NOW!

 # SEASON 3 OUT NOW!

 ## Summary
A long time in the making, we're proud to release season three! For the sake of getting it out early, it's unfortunately unfinished.
But this was an ambitious update, full of optimizations and roadblocks! We feel that you will still enjoy this update and be excited what's in store
This is a revamp of the current season 2, consisting of a new
 - Search bar
 - Game page
 - File formatting
 - Game page compiling
 - Optimized files for faster load time
 - More detailed info on game pages
 - Cleaner code
 - etc.

 ## Known issues
 - Some games are currently broken (45, thanks rm) and do not have proper iframe configurations. Should be fixed by friday
 - Descriptions are unfinished
 - Python is clunky and hard to understand

---
## [OpentrustAIhub/OpentrustAi](https://github.com/OpentrustAIhub/OpentrustAi)@[da03f8d80e...](https://github.com/OpentrustAIhub/OpentrustAi/commit/da03f8d80e86cfe37cdef636dd9e66e386c5ec70)
#### Wednesday 2023-12-13 19:26:53 by OpentrustAIhub

Create README.md

OpenTrust AI: Challenging Techno Feudalism

Introduction

Welcome to OpenTrust AI, a conceptual beacon in the AI landscape, born from a deep-seated frustration with the current trajectory of major AI platforms. This project is an imaginative response to what I perceive as ‘techno feudalism’ – a term I use to describe the exploitative practices of platforms like Bing and Meta, where creators are often left powerless over their own creations.

The Spark of Rebellion

My journey to conceptualize OpenTrust AI began with a growing anger towards the terms and conditions imposed by these AI giants. The imbalance of power, where creators receive non-commercial rights – a term ambiguously undefined in law – while the platforms seize all commercial benefits, struck me as fundamentally unjust. This is not just unfair; it’s a stifling of creativity and a misappropriation of talent under the guise of technological advancement.

The Core of OpenTrust AI

Envisioning OpenTrust AI, I imagined a platform that would defy these norms. Here are the key ideas:

	•	Ethical AI Development: A world where AI development aligns with the highest ethical standards, respecting creators and users alike.
	•	Transparent Data Practices: Challenging the status quo with clear, fair data practices that empower, rather than exploit, users.
	•	A Stand Against Ambiguity: Addressing the vague notion of ‘non-commercial’ use and advocating for clear, fair usage rights for creators.
	•	Sustainability and Equity: Imagining a monetization model that’s sustainable yet equitable, contrasting sharply with the current techno feudal landscape.

A Thought Experiment

It’s important to clarify that OpenTrust AI, as it stands, is a thought experiment – an idea more than a concrete project. It’s a space for discussion, a platform to share ideas on how we can collectively steer AI towards a more ethical and equitable future.

How to Participate

	•	Join the Discussion: Share your thoughts, experiences, and ideas on how we can challenge and change the current AI paradigms.
	•	Advocate for Change: Use this platform as a starting point to advocate for more ethical AI practices in your communities and networks.

A Note on My Stance

As the initiator of this concept, my role is more of an instigator of ideas rather than a developer. OpenTrust AI is my outlet for expressing frustration and sparking a conversation about how we might do things differently in the world of AI.

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[d49db5d4fe...](https://github.com/Mirag1993/mrdg/commit/d49db5d4fedeca818804070b6ec0eeef64f6b8cf)
#### Wednesday 2023-12-13 19:36:47 by zevo

Massive Ruin Fixes + Removals PR (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

This PR is made so I can stop getting angry at the ruins beyond saving
that are still ingame. My criteria for a ruin being removed is if
another ruin already does its niche better, if the ruin is outdated
and/or the ruin is excessively small or unbalanced. For ruins that dont
meet this criteria but are still outdated, they will be getting balance
fixes and touch ups or a total remap.

This PR is a draft for now because I will need to update the PR
changelog and description as I make changes and communicate with the
maptainers on what stays and what goes.

Adds departmental RND lootdrop spawners for circuit imprinters,
protolathes and techfabs. Excludes omnisci and basic boards from the
drops.
Fixed a space tile under a door and replaced the omnilathe with a
medical lathe on dangerousresearch
Fixed the whitesands saloon not spawning which may have caused some
sandplanets to spawn without a ruin
Fixed harmfactory's nonfunctional traps to now be as lethal as intended.
Also changed the loot in the vault to better reflect the ruin's theme
and difficulty (cargo techfab board instead of omnilathe, adv plasma
cutter instead of combat medkit, less gold more cash, kept the cyberarm
implant).
Fixed provinggrounds magical SMES FINALLY by adding a terminal on the
back. The map should finally function as intended.
Fixed a few dirs on fire extinguisher cabinets and blast door assemblies
in singularity_lab
Removed mechtransport.dmm for being small and bad
Removed some leftover gasthelizards.dmm cruft (VILE)
Removed nucleardump for being an utter mess of an oldcode ruin
Removed gondolaasteroid for being large and empty besides gondolas.
better suited for a jungle planet IMO.
Removed Jungle_Spider. Literally just a box with spiders and cloning
equipment. Small, bad, hard to find, unjustified loot.
Removed Golem_Hijack. Like jungle spider but it was free rnd, an AI
core, a full BSRPED and three golem corpses. With no enemies or
obstacles.
Removed rockplanet_clock for being a tiny lootbox that doesnt fit with
the lore. Also had a quantumn pad.
Removed whitesands_surface_youreinsane. Its a silly little reference to
an old event that unfortunately resulted in a subpar ruin. Could return
as a wasteplanet greeble ruin, but it has to go for now.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

Normally I'm all for remapping instead of removing ruins, but some ruins
are very much beyond saving. Clearing out space for better ruins to take
the spotlight is always nice. Some older ruins are fine but are missing
certain things or have loot that worked fine in the past, but doesn't
reflect the balance we want for ruins in the present.

I will be PR'ing ruins to replace the ones I remove.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl:
add: departmental RND lootdrop spawners for imprinters, protolathes and
techfabs
fix: dangerous_research.dmm now no longer has a space tile under a door
and a medical lathe instead of an omnilathe
fix: whitesands_surface_camp_saloon can now spawn again after its remap
into a functional ruin
fix: harmfactory.dmm's traps now work and loot has been adjusted to fit
the ruin better
fix: provinggrounds.dmm now has a working SMES and power
fix: singularity_lab fire extinguishers and a few poddoors now have
correct dirs
del: mechtransport.dmm and associated code
del: gasthelizards areas
del: nucleardump.dmm and associated code
del: gondolaasteroid.dmm and associated code
del: jungle_spider.dmm and associated code
del: whitesands_golem_hijack.dmm and associated code
del: rockplanet_clock.dmm and associated code
del: whitesands_surface_youreinsane.dmm and associated code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: zevo <95449138+Zevotech@users.noreply.github.com>

---
## [wcarss/c_minecraft_clone](https://github.com/wcarss/c_minecraft_clone)@[a6fdc2d703...](https://github.com/wcarss/c_minecraft_clone/commit/a6fdc2d703f185f5448e48e374e23b52cfb4f662)
#### Wednesday 2023-12-13 19:46:15 by Wyatt Carss

Actually load the frustum data for culling.

HOLY GOODNESS this is a silly bug. I could tell we were drawing _way_
too many cubes, but I assumed it was in the very complicated looking
frustum-culling functions -- likely I pulled something in I shouldn't
have, or misapplied something, or had a typo, or tried some silly hack
in 2010 that I'd forgotten, and would have to re-learn how it all
worked.

Right?

Turns out, not in the slightest! By the old trick of "actually reading
the code", I discovered that the frustum we were checking for presence
in was NEVER INITIALIZED, let alone not kept up to date. I was sitting
here asking myself, "but how can just an x,y,z have enough information?
It should need a directional vector at the least...", and I actually
had all that information all along.

Adding this boosts the framerate from glacial to hot butter and it may
have made the weird lighting glitches go away too. One line fix,
thousand percent difference in quality.

---
## [Mussclik/fishgame](https://github.com/Mussclik/fishgame)@[7f1101de93...](https://github.com/Mussclik/fishgame/commit/7f1101de93c63424a63ac34d08cc359c3825e5af)
#### Wednesday 2023-12-13 20:29:05 by Mussclik

HOLY FUCKING SHIT OMG THE FISH DO FISH THINGS GOOD CORRECT OMG ITS INSANE

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[e0ea0517d3...](https://github.com/lessthnthree/effigy-se/commit/e0ea0517d378a69b042ef2d48d00df658ed86225)
#### Wednesday 2023-12-13 20:31:29 by LemonInTheDark

Icon Autoslicing (#79659)

## About The Pull Request

Ok so you know all the dmis we have that are made to work with the
smoothing system? carpets, walls, etc.

The proper way to edit those is to convert them into a png with 5
"states' it in (one for 0 connections, one for horizontal, one for
vertical, one for all cardinals and one for all directions) and then
modify THAT, then run it through [the cutter
tool.](https://github.com/tgstation/icon-cutter)

But none ever does that, because we explain it fucking nowhere. So
instead, let's keep all those "base" files in the repo, alongside the
configs they work with, and "cut" the pngs into dmis as a part of the
build process.

I wrote a guide for how to interact with this system as a spriter, you
can find it
[HERE](https://github.com/LemonInTheDark/tgstation/blob/slice-the-sky/icons/Cutter.md).

[Adds a icon cutter build
task](https://github.com/tgstation/tgstation/commit/52143d2e96498de92421d516e0dd3f23936f88d8)

This relies on action ninja's hypnagogic (find more
[here](https://github.com/actioninja/hypnagogic)), a rust based icon
cutter.
It operates inline with the file structure, searching the codebase for
templates and resource files and compiling them down to dmis.

It can do way more then just bitmask stuff, but that is what we are
using it for rn.

Hope is to prevent for eternity the "I'm just gonna edit each of these
255 icon states that's how this carpet was made right?" meme, and allow
more expansive use of smoothing in future

[Adds a lint that ensures config files work
right](https://github.com/tgstation/tgstation/commit/21eeab9cf831c5fdac5a9b366478a9dab285c20c)

Checks to ensure they have a paired png and dmi, and also avoids issues
with uncompiled changes by double checking that nothing happens
before/after a cutter run

[Pulls all non smoothed states out of structures into bespoke
dmis](https://github.com/tgstation/tgstation/commit/a730e0cb47fc0a622fe265bccc296cec8d3a8fea)

This is required because the cutter cannot output named icon states,
only the actual cut icon

[Does something similar to
walls](https://github.com/tgstation/tgstation/commit/40780e9481103c8ee9e16538d1c2d0cdc124eeb9)

Moves reinforced walls decon stuff from their icon to a var on the type
and a set of states in the reinforced_states dmi

Moves falsewalls into their own dmi, this involved some changes to
gamecode to ensure falsewalls knew which dmi to use and what key.
Makes falsewalls display as such in editor rather then just walls

Moves smoothrock's gibonite overlays into their own file for similar
reasons

[Same thing different day
(Floors)](https://github.com/tgstation/tgstation/commit/9a3da3b69705278f39af109ac5ce86d27c2479a1)

Pulls bespoke floor icon states into their own file, splits up neon
carpets into multiple files to make cutting possible

[Actually adds the cut templates and their matching png
files](https://github.com/tgstation/tgstation/commit/1bd8920dc90d1ee1b934b6dadc39f2331854f5fa)

Not much to report here, outside of I changed the prefix for bamboo
walls to bamboo_wall so it works with false_walls

## Why It's Good For The Game

![image](https://github.com/tgstation/tgstation/assets/58055496/7c3ac7fb-873c-481b-8667-082e39432876)

None should have to manually edit cut dmis. Ever.
Also this makes adding a new smoothed thing trivial, don't even need to
know what tool you're using to do it. V good v good.
Sets us up nicely for wallening's well, wall of sprites.

Some structural decisions, we are essentially committing build artifacts
here. That's the best way of handling it because otherwise mappers could
need to run build.bat before opening a map, and that is stupid!

## Changelog
:cl:
refactor: (Almost) all smoothed icons can now be edited in their pre cut
forms
/:cl:
# Conflicts:
#	.github/workflows/ci_suite.yml
#	.github/workflows/test_merge_bot.yml

---
## [AsSa4lt/BattleSimulator](https://github.com/AsSa4lt/BattleSimulator)@[f8312585f1...](https://github.com/AsSa4lt/BattleSimulator/commit/f8312585f197f7a4dcfeada492d8b1539193293e)
#### Wednesday 2023-12-13 20:36:46 by Rostyslav

FUCK THIS TASK, I HATE IT SO FUCKING MUCH, I DONT NEED THIS SHIT, I JUST WANT TO TAKE A REST

---
## [The-Powder-Toy/The-Powder-Toy](https://github.com/The-Powder-Toy/The-Powder-Toy)@[fb9cba0d01...](https://github.com/The-Powder-Toy/The-Powder-Toy/commit/fb9cba0d01b211a949bc36a3cfc8e70a07f0b6b4)
#### Wednesday 2023-12-13 20:58:26 by Tamás Bálint Misius

Some native clipboard support for some platforms

I was hoping SDL2 would get this functionality eventually, but nope, proper clipboard support is staged for SDL3, which we're not going to see much of for at least a few more months. This will have to do for 98.0. The feature can be disabled at runtime from powder.pref.

Implementation status:

 - windows (via winapi): has the most friendly api so of course the implementation is flawless and uses every available optimization >_>
 - macos (via cocoa): I'm bad at cocoa so this is only as good as absolutely necessary; TODO: on-demand rendering
 - x11 (via xclip): I am NOT implementing icccm2; TODO: remove reliance on external tools
 - wayland (via wl-clipboard): oh god wayland oh why, you're almost as bad as x11; TODO: remove reliance on external tools
 - android: TODO; is there even a point?
 - emscripten: TODO; the tricky bit is that in a browser we can only get clipboard data when the user is giving it to us, so this will require some JS hackery that I'm not mentally prepared for right now; also I think the supported content types are very limited and you can't just define your own

x11 and wayland support are handled by a common backend which delegates clipboard management to xclip-like external programs, such as xclip itself or wl-clipboard, and can load custom command line templates from powder.pref for use with other such programs.

---
## [mazzinsanity/f13babylon](https://github.com/mazzinsanity/f13babylon)@[e211796729...](https://github.com/mazzinsanity/f13babylon/commit/e2117967298eab34c19e70ff450dabe36981258e)
#### Wednesday 2023-12-13 21:01:34 by panzerr1944

Map Changes, NML Edits, E-Weapon Loot Spawners & More (#303)

## About The Pull Request
Long list of fixes, edits and other things. Check the changelog for a
full list!

## Why It's Good For The Game
Less dumb spawners, better spawners for e-weapons, more cars, less setup
time, harder dungeon, more fun :)

![Screenshot 2023-12-04
142647](https://github.com/f13babylon/f13babylon/assets/76122712/468a97b4-c78d-4c92-8fcf-43d18c841db2)
![Screenshot 2023-12-04
142707](https://github.com/f13babylon/f13babylon/assets/76122712/b7d8a748-3e80-4c04-8af3-f9f660eb55ef)

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
🆑
remove: the 2 unique spawns on the surface/underground that can be
rushed
remove: the 'Left Hand' riot shotgun force-spawner (and Raider T-45b
spawner)
add: a chemlab, basic raider armor, louisville slugger and bino spawners
to Raider Town
add: a few more carpiles around the map
add: a Raiders minidungeon for books 1-3, since everyone else gets it
now it seems
fix: the new Kebab Town (Mobs are harder now. Beware..!) 
remove: the followers Reagent Gun (AGAIN. I did this before and someone
RE-MAPPED IT IN.)
remove: that one dumb as shit rad-puddle from infront of the BOS base 
remove: the force-spawn gauss rifle in no mans land (replaced with
experimental spawner)
add: bodybags for followers
edit: the E-Weapon spawners to the following - | Low = AEP7, Wattz, (low
chance) Wattz Magneto (someone made the AEP7 midtier for some bullshit
reason) | Mid = AER9, Plaspistol, (low chance) Wattz 2k | Mid-High =
AER12, AER9, (low chance) Ion Rifle | High = Plasrifle, Wattz 2kE, RCW,
Tribeam,(low chance) AER14
edit: the Experimental Spawner to the following: M72 Gauss | Peacekeeper
| P90 | Gatling Laser
edit: the Peacekeepers stats (Applied auto-fire shot delay of 2.8 from
1)
fix: Fixed the Remnant Bunker shoot-through wall things by replacing
them
fix: Fixed BOS NML entrance and Enclave NML Entrance
fix: Replaces NML PA claw with an edited Junker Boss (he is hard)
fix: Fixes the boss not firing
remove: the invincible interior walls in kebab, replacing them with
r_walls
fix: NML Turrets shooting NML mobs
tweak: NML kebab melee mobs and boss mobs have melee AP
add: 2 ghoul spawners to north nml + static glowing one
remove: 2 legendary ghouls from north nml
add: 4 ranged mutant spawners to south nml
remove: 2 legendary super mutants from south nml
add: 6 more turrets throughout NML (3 north, 3 south - 2 at each
building, 1 for each exterior melee weapon spawn)
add: renegade flags to kebab
🆑

---------

Co-authored-by: maaacha <116771811+maaacha@users.noreply.github.com>

---
## [dagster-io/dagster](https://github.com/dagster-io/dagster)@[5168f5a8ee...](https://github.com/dagster-io/dagster/commit/5168f5a8ee14ef0af13ff65c9f567d7b27deb437)
#### Wednesday 2023-12-13 21:06:16 by quantum-byte

Fix #7442 / multi threading dropped log entries issue (#18493)

## Summary & Motivation

This MR should (based on my code understanding and testing) fix [issue
7442](https://github.com/dagster-io/dagster/issues/7442). It also fixes
in general randomly dropped user written log messages if logs are being
recorded from multiple threads.
Logging is quite important and its quite annoying to work around this
limitation/bug.

Maybe @sryza or @OwenKephart can have a look, since they already looked
into the 7442 issue.

## How I Tested These Changes

I tested the changes locally with an op/graph, which starts multiple
threads and logs multiple messages in each thread.

```python
import logging
import threading
import time

from dagster import AssetKey, AssetMaterialization, Output, job, op, repository

logger = logging.getLogger(__name__)


def background_thread(thread_name):
    for i in range(0, 5):
        logger.info(f"Background thread: {thread_name} {i}")
        time.sleep(0.5)


@op
def op1():
    yield AssetMaterialization(asset_key=AssetKey(["asset1"]))

    threads = []
    for thread_name in range(0, 5):
        thread = threading.Thread(
            name="background_thread",
            target=partial(background_thread, thread_name),
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    yield AssetMaterialization(asset_key=AssetKey(["asset2"]))
    yield Output(123)


@op
def op2(arg):
    logger.info(f"Result of op1: {arg}")


@job
def dropped_events_job():
    op2(op1())


@repository
def dropped_events_repository():
    return [dropped_events_job]
```

Without my change i was missing a significant chunk of the expected log
messages in the captured log output:

![dropped_logs_without_change](https://github.com/dagster-io/dagster/assets/17649269/d777483a-911b-4010-b2e3-48bf7128437d)

With my change i had the exact amount of log messages in the captured
log output that i expected:

![no_dropped_logs_with_change](https://github.com/dagster-io/dagster/assets/17649269/d09f3617-fa86-415c-b7de-0dadab078b5b)

I also tested the original reproducing code from
https://github.com/dagster-io/dagster/issues/7442:

Without my change:

![grayed_out_op1_without_change](https://github.com/dagster-io/dagster/assets/17649269/c32c39ea-33a6-4207-a8c1-b8ddd30aa437)


With my change:

![green_op1_with_change](https://github.com/dagster-io/dagster/assets/17649269/fac597a6-4e2c-428b-afa4-f7695667ade7)


I am not that familiar with the dagster code. If you can point me to a
place where a unittest for this might go and some info on how to test it
in your opinion, than i will have a look at it.

---------

Co-authored-by: Florian Kaufmann <florian.kaufmann@corpuls.com>

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[71b45e54ad...](https://github.com/Derpguy3/tgstation/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Wednesday 2023-12-13 21:33:24 by san7890

Puts all traits in the globalvars file + CI Testing (#79642)

## About The Pull Request

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-


![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit
## Why It's Good For The Game

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)
## Changelog

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[eb246c21f6...](https://github.com/Derpguy3/tgstation/commit/eb246c21f6eb5380dc56e5779fcd51d11437557c)
#### Wednesday 2023-12-13 21:33:24 by san7890

Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

---
## [sthagen/facebook-pyre-check](https://github.com/sthagen/facebook-pyre-check)@[f5611c955f...](https://github.com/sthagen/facebook-pyre-check/commit/f5611c955f54a60ea9c50875719a14bbd5c29743)
#### Wednesday 2023-12-13 22:16:24 by Steven Troxler

unify transitive successor interface, rename

Summary:
In this commit I'm continuing to try to clean up GlobalResolution interfaces
and eventually eliminate direct access to environments through it; in this
case the ConstraintsSetTest was grabbing a raw environment in order to run
`is_transitive_successor`.

An issue I ran into along the way is that the `GlobalResolution` and
`ClassHierarchy` interfaces for `is_transitive_successor` were not compatible;
the variable names didn't agree! The code was accessing a raw environment
specifically to work around this problem.

I decided that the name `is_transitive_successor` wasn't very informative
anyway; instead I renamed it to `has_transitive_successor` and made the
`~successor` a named argument / the predecessor a positional argument,
so that the name actually translates reasonably to English, as in
"does <predecessor class> have a transitive successor of name ~successor"?

I still hate the naming here, since "successor" actually means "ancestor"
in the type system; we're using terminology coming from thinking about
the MRO in a context where the MRO doesn't matter that much and thinking
about the inheritance DAG would make a lot more sense. But renaming in
terms of ancestors / descendants is a much bigger change than I want to make
right now and might even be controversial. At the moment I just want
consistent interfaces.

Reviewed By: connernilsen

Differential Revision: D52044965

fbshipit-source-id: ae4f6b98f4926c26ff3838f2a2982ba8fb270f01

---
## [temporalio/temporal](https://github.com/temporalio/temporal)@[1be76e3583...](https://github.com/temporalio/temporal/commit/1be76e3583ef01ba9f79503e81fed5b7c9ab389c)
#### Wednesday 2023-12-13 22:29:42 by Tim Deeb-Swihart

Replace gogo/protobuf with google/protobuf (#5032)

**What changed?**

gogo/protobuf has been replaced with Google's official go compiler. 

**Why?**

gogo/protobuf has been deprecated for some time and the community is
moving on, building new tools (like vtproto) atop google's v2 compiler.

**How did you test it?**

`make test`

**Potential risks**

1. The change from embedded gogo-generated-structs to
google-generated-pointers-to-structs created a risk of nil pointer
exceptions. I've fixed all the ones our tests found but it's possible
there are more lurking in the new code.
2. This change may cause our performance to decrease. Certainly
encoding/deconding of proto objects will become slower, but the overuse
of pointers by the google compiler may negatively affect our overall
performance. We'll need to keep an eye on the GC stats
3. This breaks the HTTP API. We will not support [shortand payload
encoding](https://github.com/temporalio/proposals/blob/master/api/http-api.md#payload-formatting)
in this first pass; that will come once this initial work is in testing.

**Breaking changes for developers**

- `*time.Time` in proto structs will now be
[timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/protobuf@v1.31.0/types/known/timestamppb#section-documentation)
- `*time.Duration` will now be
[durationpb.Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb)
- V2-generated structs embed locks, so you cannot dereference them. `go
vet` will scream at you about this. If you need a copy, use
`proto.Clone`.
- If the performance of this sucks then I will either update our code
generator to add shallow-clone methods or hand-roll the ones we need
- Proto enums will, when formatted to JSON, now be in
`SCREAMING_SNAKE_CASE` rather than `PascalCase`. We decided (in
discussion with the SDK team) that now was as good a time as any to rip
the bandage off.
- Proto objects, or objects embedding protos, cannot be compared using
`reflect.DeepEqual` or _anything_ that uses it. This includes `testify`
and `mock` equality testers!
- You will need to use the `common/testing/protorequire`,
`common/testing/protoassert`, or `common/testing/protomock` packages
instead. I've implemented proto-compatible matchers and assertions there
for all cases I've encountered
- If you need `reflect.DeepEqual` for any reason you can use
`go.temporal.io/api/temporalproto.DeepEqual` instead

Note that history loading will not be impacted by the JSON changes: I
rewrote history loading to dynamically fix incoming history JSON data
(like all our other sdks); you can find this code in [my fork of our go
API](https://github.com/tdeebswihart/temporal-api-go/blob/master/internal/temporalhistoryv1/load.go)
alongside its tests.

**🚨Sharp Edges Introduced🚨**

Beware `*timestamppb.Timestamp.AsTime()`. If you need to extract a time
value from a proto time (timestamppb) **always** make sure to check
whether it's nil first. When the proto object is `nil` `AsTime()` will
return a non-zero time at the proto epoch: UTC midnight on January 1,
1970.

I've made this mistake multiple times during this transition and each
time it's been a pain to debug

**Is hotfix candidate?**

No.

---
## [gabrieldodrip990/huecorps-station](https://github.com/gabrieldodrip990/huecorps-station)@[015a3cf18a...](https://github.com/gabrieldodrip990/huecorps-station/commit/015a3cf18a133ef12c1ee5bac4a4179140ecbc75)
#### Wednesday 2023-12-13 22:33:47 by Bloop

[MANUAL MIRROR] Replaces prettierx with the normal prettier (#80189)  (#25538)

* Replaces prettierx with the normal prettier (#80189)

Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
N/A nothing player facing

* Converts this to tsx

* Update JobsPage.tsx

* Update JobsPage.tsx

* Update JobsPage.tsx

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [ToasterBiome/Yogstation](https://github.com/ToasterBiome/Yogstation)@[75c13f4eff...](https://github.com/ToasterBiome/Yogstation/commit/75c13f4effbd82c8dc661c6b3bbc0146de44fded)
#### Wednesday 2023-12-13 22:40:14 by cowbot92

[PORT] Adds several more signs for the bar to use (#20997)

* yo fuck emisssives

that shit sucks

* sure the rest of these can come too

I guess

* no 100% orange juice

sorry

---
## [SauLes95/Advent-of-code](https://github.com/SauLes95/Advent-of-code)@[9d3814b245...](https://github.com/SauLes95/Advent-of-code/commit/9d3814b2454b13bdfe2606e8aee101241f465665)
#### Wednesday 2023-12-13 22:41:49 by SauLes95

Create task1.c

You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:

seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48
The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
With this map, you can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?

---
## [crawl/crawl](https://github.com/crawl/crawl)@[dfa497c050...](https://github.com/crawl/crawl/commit/dfa497c050c372f79a26eca37648bde4a5cc4df0)
#### Wednesday 2023-12-13 22:44:02 by regret-index

New monster: protean progenitors, for Zot

Zot hasn't gotten new monsters besides the addition of then-new ghost moths
13 years ago (8d1b968), or the swapping of fire and ice dragons for already
present prior quicksilver dragons 7 years ago (0b18a7b). Most Zot work
across Crawl's development has been more oriented on adding more and more
stair vaults to Zot or fixing up the non-top-tier monsters otherwise
present: tmons constrict / demonic berserk, curse toe summons, death cob
attack brands, klown chaos, lich and draconian class spells. This is
entirely reasonably behaviour that has relatively evened out Zot's threat
level over time, but it has been a very restrained and compact set for a
while. It wouldn't hurt to try out more. Especially stuff that can break up
Zot's heavy reliance on relatively conventional, highly established, and
spreading elsewhere draconians.

Protean progenitors are transmutations giants for Zot. The origins of all
the dungeon's countless shapeshifters, they first start off as relatively
simple foes- unarmed Irradiate casters with fast regen but poor defenses
and no resistances. When they die, however, they leave behind some last
children in some last new form as they violently split into piles of
'aspiring flesh'- by default two at HD 12, with increasing chances of a
third if it rarely rolls any lower HD. These non-attacking, non-moving
piles will over the course of a few turns polymorph into hasted, mighted
copies of whatever the giant originally tried to transform into, and
never transform again. At HD 12 over the glowing shapeshifter HD 10
default, this gives double-buffed options of e.g. fire and ice dragons,
unarmed ettins, tyrant leeches, alligators, jorogumo, and broodmothers.
A chance to review much earlier branch spawns as a surprise in every giant
provides a bit more variety of bands over Zot's many base and nonbase
draconian packs, while also hewing closer to the weirder spectrum of Zot's
many non-draconic non-elemental monsters.

For now, they eat up a bit of the base draconian and non-base draconian
bands weight, and spawn with a 33% chance to have a second one accompany
them- a quick objstat roll says there should be about 4 of them throughout
Zot and each of Zot's standard base draconians reduced from ~11 to ~10. The
exact strength of these are inherently difficult to assess, so they'll
probably need a fair bit of public testing to see how these work out- base
form's base stats, spawn count, and band count are all easily changed.
They've also only been added to a restrained number of vaults- ones that
span the bulk of Zot's current monster set, or that invoke chaos and flesh.
They might make for reasonable spawns on Mnoleg's level to lower their
reliance on ugly things and eyes, but for now are otherwise only in chaos
zig floors. If we get any other new big Zot monsters, it might be a good
idea to look at slightly reducing the overall spawn count as is done for
Lair.

(Severely placeholder tiles are mostly made of currently unused decade-old
rltiles for large abominations, small abominations, and glowing
shapeshifters, with palettes from Sastreii's ice dragon and radroaches.)

---
## [Ephemeralis/Skyrat-tg](https://github.com/Ephemeralis/Skyrat-tg)@[b574839498...](https://github.com/Ephemeralis/Skyrat-tg/commit/b574839498f606f6279aa0ad4ec312ffd447e637)
#### Wednesday 2023-12-13 22:45:39 by SkyratBot

[MIRROR] fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 [MDB IGNORE] (#25074)

* fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

* fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11

---------

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

---
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[1185c70ab5...](https://github.com/rmellis/HelpUKR-master/commit/1185c70ab51b247ac8af1395c31e1bb0b3f8cb83)
#### Wednesday 2023-12-13 23:14:53 by rmellis

Added Day 658 - Targets and Days (TL) Eng+Ukr

Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
Yesterday's takedown of Kyivstar by the orcs not only disrupted their services but also hampered their "frontline communication". This underscores the enemy's reliance on civilian internet infrastructure for combat in the rear. Our recent focus on internet providers led us to target Starlink in Moscow, adding to our successes. Remember, constant attacks on multiple providers are ongoing. More traffic means more targets. ‍
‍Bring your friends into the IT ARMY!
/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Орки вивівши з ладу Київстар вчора також поклали добру частку свого "фронтового зв'язку", що ще раз показує наскільки активно ворог використовує цивільну інтернет інфраструктуру як для бойових дій так і в тилу. Саме тому останні декілька місяців ми фокусуємось на інтернет-провайдерах.
Вчора в колекцію скальпів додали Старлінк - провайдера в Москві. Для зрозумілості, декілька провайдерів знаходяться постійно під атакою і не всі попадають у звіти. Чим більше ви створюєте трафіку, тим більше цілей ми можемо накрити. Залучайте друзів до IT ARMY!

---

