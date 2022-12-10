## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-09](docs/good-messages/2022/2022-12-09.md)


2,082,765 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,082,765 were push events containing 3,102,490 commit messages that amount to 256,244,061 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 61 messages:


## [GreySole/Spooder](https://github.com/GreySole/Spooder)@[8120f971b9...](https://github.com/GreySole/Spooder/commit/8120f971b9184608e6000724c300ccbbfba34526)
#### Friday 2022-12-09 00:18:16 by GreySole

0.3.8 Update

This beast of an update makes a lot of deep changes that I really think should be made to make Spooder more organized and user friendly. Some dependencies have changed as well as folder structures. It’ll probably work if you copy/paste the repo over what you have, but you might as well backup your settings and plugins and restore them in a clean installation.

Regardless, use `npm install` to get the new dependencies!

Init
- Gets network interfaces and recommends 192.168.x.x

OBS
- Added callOBS() global function to make obs websocket calls outside of the module (events)
Web UI
- Prints actual network info to access instead of stored info

- Ngrok integration: Put in your API key in the config tab to have your tunnels and eventsubs all set when starting up. If you want to run Spooder without using this, call `npm run safe`. Recommended for developing where Spooder will get restarted a lot.

- Refresh eventsubs: Deletes all eventsubs and resubscribes with the current callback url. Ngrok will do this automatically. You can do this manually in the EventSub tab.

- Added OBS data to Events tab for OBS commands

- Backup/Restore fix: When importing backups, check/create backup directory

- Config: Like Events, the object structure is built into the UI and will auto fix/upgrade your files.
Customize your Spooder in the Config tab :3

Mod UI

- Mod UI themes are now part of the themes.json file so any themes made will be immortalized.
- New authentication method makes it easier to log in securely. Instead of making an auth token with Twitch, mods now enter their Twitch username and their own password (doesn’t have to be the account’s password, but it can). Finally, mods call ‘!mod verify’ in the Spooder user’s chat to ensure it’s them. Passwords are encrypted and stored in mod.json.
Plugins
- Plugins have been made more “solid”. Information from its package.json is now used for the Web UI. So you get a proper, capitalized name with version numbers and author name.

- Wait for the sample plugin to update, because there’s a lot of good changes in the osc bundle.
- Connect messages now carry info about the overlay/utility. Such as:
-- which version of Spooder it was made for (I want to make auto-updates for the osc-bundle sometime)
-- The plugin’s internal name (can access the plugin’s proper name by accessing activePlugins[pluginname]._name)
-- Any error messages from plugins will also be transmitted so you can see in the Web UI’s OSC Monitor. Gives you a chance to catch it on the fly rather than while testing. Error logs are also stored separately so they won’t shift out of the OSC messages.
Spooder
- Added theme file for saved Mod UI Themes, Custom Spooder, and Web UI Themes (For a later update)
- Added spamguard to mod commands. Call ‘!mod spamguard’ to automatically timeout users spamming commands. Timeouts are specific to Spooder, so there aren’t any role exceptions…unless you would want that. Let me know.
- Chat module switched to tmi.js. I feel it’s better maintained and stable. There are some ways twitch-js formed message objects that are easier to develop with (like emotes), so it builds the tmi object to be more like twitch-js.
- Added OBS commands: setinputmute, switchscenes, and sceneitemenabled. More to come.
- Global functions: You can use these functions in plugins
-- restartChat(message:string): Restarts the chat. You can add a message to say after finishing restart.
-- chatisFirstMessage(message:obj): Returns true or false whether the message is the user’s first message to your channel
-- chatIsReturningChatter(message:obs): Returns true or false whether the message is from a returning chatter.
-- chatIsMod(message:obj): Returns true or false whether the user who sent this message is a moderator.
-- chatIsSubscriber(message:obj): Returns true or false whether the user who sent this message is a subscriber.
-- chatIsBroadcaster(message:obj): Returns true or false whether the user who sent this message is the broadcaster
-- getChatters(type:string): Returns an array of usernames for a specific type. Available types are: mod, vip, all
-- blacklistUser(viewername:string, duration:number (millis): Locks a user from using chat commands for the duration.
-- lockEvent(moduser:string, modCommand:string, target:string): Locks an event from use in chat. moduser is to tell which mod called the command. modCommand is either “lock” or “unlock” and it adapts to booleans and integers. Target is which event to lock.
- Async response commands: To allow API calls within responses like with getChatters()
- OBS event handlers: Control OBS with chat commands, channel point redeems, or OSC
- Mod event handlers: Call mod commands through events. Though chat commands are already built in and there’s not many use cases for redeems. This is still handy to hook an OSC message to a mod command.
- Event timeouts use setTimeout and command durations are now parsed as float: This way you have more precision for timed UDP commands.

There’s probably more features and fixes I don’t know off the top of my head, but this is quite a list as it is lol. I hope this all works well for you, if not, please create an issue here or ask for help on the Discord Server. Happy weaving! /╲/\( º^ ω ^º )/\╱\

---
## [Headstorm/foundry-ui](https://github.com/Headstorm/foundry-ui)@[215850f646...](https://github.com/Headstorm/foundry-ui/commit/215850f646901a10cd9d0dfcd88e47b697c4cbc4)
#### Friday 2022-12-09 00:39:06 by Anthony Fernandez

Added code hightlight to the readme

Dude this library looks fucking awesome. I'm building my own, as a little side project just to learn. I hope you don't mind me taking inspiration from you hahaha. Really good work man!

---
## [crowlogic/arb4j](https://github.com/crowlogic/arb4j)@[03fcf61b48...](https://github.com/crowlogic/arb4j/commit/03fcf61b489b0acbd218a7d84d85495aa39677b8)
#### Friday 2022-12-09 01:23:57 by Stephen Crowley

Revert "fuck that chaos theory shit"

This reverts commit 5c35688d59e3ea09736ee47dc6bf660e52857250.

---
## [emacdona/adventofcode](https://github.com/emacdona/adventofcode)@[7d2c8a2a94...](https://github.com/emacdona/adventofcode/commit/7d2c8a2a949299afef1d16d6b52833ffa1dd0eb3)
#### Friday 2022-12-09 01:59:30 by Ed

holy shit... what a simple, impossibly hard to spot mistake. I was going
crazy -- thinking there was a bug in AoC

---
## [zhonghanyong/cadence](https://github.com/zhonghanyong/cadence)@[add4b390ad...](https://github.com/zhonghanyong/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Friday 2022-12-09 02:58:16 by Steven L

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
## [Willardstation/tg-voidcrew](https://github.com/Willardstation/tg-voidcrew)@[4fd404aa8f...](https://github.com/Willardstation/tg-voidcrew/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Friday 2022-12-09 02:59:01 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms


![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)
  
</details>



## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [Willardstation/tg-voidcrew](https://github.com/Willardstation/tg-voidcrew)@[5da871e271...](https://github.com/Willardstation/tg-voidcrew/commit/5da871e2719fb7aac04fb1ec4c85ea7a09a83b36)
#### Friday 2022-12-09 02:59:01 by RikuTheKiller

Made geysers easier to find (#71608)

## About The Pull Request

This PR raises the geyser spawn rate from 0.1 to 0.15 and increases the
weight of wittel geysers to 10 which is the same as every other special
geyser. (previously 6)

Wittel shouldn't be any less difficult to find than other geysers as all
of the special geysers are equally powerful. Hyper-plasmium oxide can be
used to make extremely powerful explosives that can go beyond maxcaps
and hollow water + protozine can create an infinite amount of strange
reagent.

I've subjected myself to going out of my way to visit lavaland/icemoon
several times to get wittel and each time finding a single geyser takes
about 5 minutes of my time. This, coupled with the fact you really don't
have a lot of time to be wasting on looking for the geysers results in
an unfun experience.

I understand geysers are sort of a necessary evil, however, they
shouldn't be THIS difficult to find. Out of the 10 or so geysers I've
found, only 1 has had wittel in it and it was next to a whelp portal
which ended both me and my miner escort.

I've also hunted the entirety of lavaland with no luck. (Horrendous
experience.)

I've dedicated entire rounds to this, by the way.
## Why It's Good For The Game

If you go out of your way to waste ages hunting for geysers, there
should at least be a reward. That is, in the same round, not after 3 or
more rounds as even megafauna gear isn't gatekept THAT hard.

You shouldn't have to waste this much of a miner's time (who is also
going for megafauna gear) to get something that is arguably less
powerful than what they get for less effort. Megafauna gear is also
available every round and is attained via predictable methods.

This PR will also likely make geyser scanning a more comparable method
of point gain to just mining.

Oh and not to mention that penthrite is available almost roundstart via
luxpens. (It's a wittel chem.)
## Changelog
:cl:
balance: Geysers now spawn more often, especially wittel geysers.
/:cl:

---
## [Willardstation/tg-voidcrew](https://github.com/Willardstation/tg-voidcrew)@[2425531eb2...](https://github.com/Willardstation/tg-voidcrew/commit/2425531eb2dab84fb27ed864e4c52470bfff6918)
#### Friday 2022-12-09 02:59:01 by John Willard

Removes tablets (not PDAs) entirely. (#71507)

## About The Pull Request

**Comes with an UpdatePaths!**

Removes the tablet subtype, PDAs now replaces them entirely.

Nukie and Silicon tablets are now subtypes of the PDA instead, while
contractor ones were removed entirely as they didn't do anything and
were unused (though it wouldn't be hard to re-add).

Nukie PDAs are now the only type of PDA that uses modular_tablets.dmi,
which is just larger icons of modular_pda. Each application requires an
icon state in both of these, for 2 different sizes, which makes it
annoying to make new applications, especially if it can also run on
computers/laptops.

### Icons

Because Silicon tablets are now a subtype of PDA, they use PDA icons
instead of tablet ones. Luckily for us, they already exist in code.

![image](https://user-images.githubusercontent.com/53777086/203876575-56eb1593-774c-47c6-8e7d-491a7805f28c.png)

AI's don't use a tablet icon though, so they aren't affected.

## Why It's Good For The Game

There's very little difference between tablets and PDAs, PDAs overshadow
them in every single way, so at this point I don't see why we should
have both of these, and if you compare the two in usefulness and actual
in-game use by players, it's a no-brainer than the item all players get
roundstart and comes with a messenger should be the one we go with.

Also as said in the about section, when making an app you would need to
make icon states for the program running for all hardware it can run on,
which is Computer, Laptop, PDA, and Tablet.

Laptop is just a smaller computer icon
PDA is just a smaller tablet icon

However, you can't simply shrink the size of the icon, instead you have
to completely resprite the same app icon FOUR TIMES for it to not
bluescreen on all these different devices.

<details>
<summary>
Here's examples of it
</summary>
Computer (NOTE: *They share the same icon file as regular computers*)
<img
src="https://user-images.githubusercontent.com/53777086/203876801-486a8054-489a-4983-bdad-a2599b4dc379.png"/>
Laptop
<img
src="https://user-images.githubusercontent.com/53777086/203876333-58e5d135-f4c6-4a02-8948-1df771e294a4.png"/>
Tablet
<img
src="https://user-images.githubusercontent.com/53777086/203876352-816c7fb1-c681-40b9-99e0-052f49632c7f.png"/>
PDA
<img
src="https://user-images.githubusercontent.com/53777086/203876358-1cf7253d-3c6a-456a-8133-ebf7f0351637.png"/>
</details>

If we wish to help in simplifying this, we should remove tablet icons
entirely, which means 1 less icon to worry about. To do this, we'd need
to resprite nukie PDAs, however I am very much not a spriter and never
tried GAGS, so I'll leave it to someone else to do.

## Changelog

:cl:
del: Tablets are now removed, PDAs are now the base 'tablet'. Silicon
and nukie tablets are now PDAs.
/:cl:

---
## [The-Moon-Itself/Shiptest](https://github.com/The-Moon-Itself/Shiptest)@[3efa9b5382...](https://github.com/The-Moon-Itself/Shiptest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Friday 2022-12-09 03:11:04 by Zevotech

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
## [alexandru-duca/chess-openings](https://github.com/alexandru-duca/chess-openings)@[2aa6e0a446...](https://github.com/alexandru-duca/chess-openings/commit/2aa6e0a446d4edc0ab61757b9dcb10a64f8aa2ff)
#### Friday 2022-12-09 03:46:13 by Alexandru Duca

Scandinavian Defense: Portuguese Gambit

# Changelog
- Removed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. f3 Bf5` named `Scandinavian Defense: Portuguese Variation, Portuguese Gambit`.
- Renamed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` from `Scandinavian Defense: Portuguese Variation` to `Scandinavian Defense: Portuguese Gambit`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` named `Scandinavian Defense: Portuguese Gambit, Banker Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` named `Scandinavian Defense: Portuguese Gambit, Classical Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` named `Scandinavian Defense: Portuguese Gambit, Correspondence Refutation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` named `Scandinavian Defense: Portuguese Gambit, Elbow Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` named `Scandinavian Defense: Portuguese Gambit, Jadoul Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` named `Scandinavian Defense: Portuguese Gambit, Lusophobe Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` named `Scandinavian Defense: Portuguese Gambit, Melbourne Shuffle Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` named `Scandinavian Defense: Portuguese Gambit, Wuss Variation`.

# The Name of `1. e4 d5 2. exd5 Nf6 3. d4 Bg4`
This line `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` in the Scandinavian Defense has many different names across chess literature. Selby Anderson released the book [Center Counter Defense: The Portuguese Variation](https://www.amazon.com/Center-Counter-Defense-Portuguese-Variation/dp/1886846103) in the year 1997 and, apparently, named it `Portuguese Variation`. In his book [Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943), [David Smerdon](https://en.wikipedia.org/wiki/David_Smerdon) called this line `Portuguese Complex`, but he noted that it was also called `Portuguese Opening` as well as `Jadoul Variation` [Section 1]. It's called `Portuguese Gambit` in Wikipedia's [list of chess gambits](https://en.wikipedia.org/wiki/List_of_chess_gambits#Scandinavian_Defense) and `Portuguese Variation` as well as `Jadoul Variation` in Wikipedia's article on the [Scandinavian Defense](https://en.wikipedia.org/wiki/Scandinavian_Defense#2...Nf6). (Unfortunately, I was unable to check the sources Wikipedia provides because I couldn't find the referenced books.)

Since Selby Anderson's book predates all other sources, there is an argument to name this line `Portuguese Variation`. However, Black delays taking back the pawn on d5 twice (first time with `2... Nf6` and second time with `3... Bg4`). This gives White the opportunity to secure the extra pawn with e.g. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4 Bg6 6. c4`. Additionally, Selby Anderson may not have been aware of the dubious nature of this variation ([Stockfish gives White +0.8](https://lichess.org/7CAhQOCs)). Furthermore, David Smerdon repeatedly refers to this line as a gambit despite calling it `Portuguese Complex`. Because of this, I argue that this line should be called the `Portuguese Gambit`.

# Variations in the `Portuguese Gambit`
[Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943) is currently the most extensive book on the `Portuguese Gambit`. It categorizes all major responses from White after `1. e4 d5 2. exd5 Nf6 3. d4 Bg4`. Smerdon also offers creative names for all variations covered by his theory. Here are the variations sorted by chapter:
1. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` is called `The Banker`. (White "banks" the extra pawn with the immediate `5. c4`.)
2. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` is called `The Jadoul`. (Named after [Michel Jadoul](https://de.wikipedia.org/wiki/Michel_Jadoul) who is one of the earliest exponents of the Portuguese Gambit [Introduction, Inspirational Game #1].)
3. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` is called `The Melbourne Shuffle`. (Played by many australian IMs from Melbourne [Chapter 3]. It is named after a [rave dance](https://en.wikipedia.org/wiki/Melbourne_shuffle) which originated in Melbourne.)
4. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` is called `The Correspondence Refutation`. (A line against the `Portuguese Gambit` successfully employed the correspondence community [Chapter 4].)
5. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` is called `The Wuss`. (Apparently, `4. Be2` is a wimpy move and only a [wuss](https://www.merriam-webster.com/dictionary/wuss) would play it.)
6. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` is called `The Lusophobe`. (According to Wikipedia, [Lusophobia](https://en.wikipedia.org/wiki/Lusophobia) is irrational hostility, racism or hatred towards Portugal, the Portuguese people or the Portuguese language and culture. David Smerdon is making a joke by referring to the line `4. Bb5+ Nbd7 5. Be2` as "Anti-Portuguese" or "effective against the Portuguese Gambit".)
7. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` is called `The Elbow`. (Given the effectivness of the line `4. Bb5+ Nbd7 5. Be2`, occasionally playing `4... c6` may discourage players from studying it while preparing against you. Playing `4... c6` is a metaphor for hitting your well prepared opponent with your elbow [Chapter 7].)
8. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` is called `The Classical`. (Refers to the fact that the move `4. Nf3` is principled [Chapter 8].)

---
## [Happykiddo012/app-dev](https://github.com/Happykiddo012/app-dev)@[b2d5d63a50...](https://github.com/Happykiddo012/app-dev/commit/b2d5d63a50d6b4e2e9d3cb8d39013ab93bc14ab7)
#### Friday 2022-12-09 03:56:06 by Happykiddo012

Update README.md

My favorite series is Supernatural because it's all about Sam and Dean Winchester, brothers who go on thrilling but terrifying adventures while hunting monsters, are the focus of this haunting series. The brothers were raised by their father as soldiers who follow enigmatic and demonic beings after their mother was killed by something supernatural. Sam and Dean's investigation into all things that go bump in the night is complicated by secret relationships and violent memories. The brothers must rely on one another as they face new foes as friends betray them and old tricks and tools become useless.

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[bf582cb833...](https://github.com/necromanceranne/tgstation/commit/bf582cb833d89b7121b4fefa37e8da1773783245)
#### Friday 2022-12-09 04:05:39 by Profakos

Trophy case update (#71015)

## About The Pull Request

I have been chipping away/procrastinating at this since May, but after
several years, I have finally updated how Trophy Cases work.

So, what this PR does is the following:

- Standardized everything in persistence.dm to use snake case, and added
basic autodocs
- Automatically moves trophies from data/npc_saves/TrophyItems.json to
data/trophy_items.json. Removed legacy .sav conversion by request, it
has been a long time.
- Trophy cases are opened and loaded the same way you would open a
regular ID locked display case (used curator access, relevant access
autodoc has been updated)
- Instead of cheap plastic replicas that turn to dust anyways, trophy
cases use holograms, which can be dispelled by hand
- Trophy data gets saved if an item stays in the trophy case when the
shuttle arrives to centcom, and the item has a description set. This is
in line with paintings, which has to still hang on the wall at round
end.
- You can edit the description of new trophies by using the librarian's
key to unlock History Mode
- When you click on a closed trophy case, it will open a tgui, and will
not display the case description. It will still do for open cases.
Vendatrays have been updated to do the same.
- The UI's icon uses icon2base64(getFlatIcon(showpiece, no_anim=TRUE)).
Vendatrays have been updated similarly, so items with directions and
animations are displayed properly. The base64 strings are updated in
update_static_data.
- Fixes vendatrays from displaying some characters in strange ways, such
as displaying /improper.
- Renames some one letter, or nonindicate argument and var names in
trophy case code
- Adds a trophy management admin panel, where admins can finally delete
all the curator ID cards swallowed over the years. Or, they can replace
the paths with funny new paths.
- If an entry has an incorrect, no longer existing path, it will be
marked red in the management panel
- Adds MAX_PLAQUE_LEN define, which 144 characters
- Removes start_showpieces from trophy cases, as it was completely
unused. The start_showpiece_type var is still around.
- Moves trophy_message var to trophy cases. Only a dice collector
display case used them in the Snowdin map.

What this PR does not do

- Sadly, it still only saves the base image of an item, and no layers or
altered image states. This has to come in the future.

<details>
<summary>Click here to see various states of the trophy tgUI</summary>
 

![kép](https://user-images.githubusercontent.com/2676196/199545412-e5b7e7a8-59fb-41e6-aca5-6b07ba33501c.png)
Locked history mode, existing item.


![kép](https://user-images.githubusercontent.com/2676196/199545574-9e705603-9b7a-457d-9575-2d4145ad940d.png)
Unlocked history mode, but holographic trophy is present.


![kép](https://user-images.githubusercontent.com/2676196/199545883-45c3916b-011f-462a-8296-6eb13db32158.png)
Locked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199545967-a33e2501-aa5f-473b-b79f-ebd950df2afc.png)
Unlocked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199546100-718bd639-3199-4df7-ad77-ed3dbf27b290.png)
Unlocked history mode, item placed, default text. (Note: this picture is
out of date. The typo has been fixed, and "record a message" is now
"record a description" for consistency)
 

![kép](https://user-images.githubusercontent.com/2676196/199546202-5ebbbd28-907c-4f2d-b7cd-29d2ef21c7f3.png)
Unlocked history mode, item placed, new text.

</details>

<details>
<summary>Click here to see the admin panel</summary>


![kép](https://user-images.githubusercontent.com/2676196/199553349-8684f23f-4699-42f2-a27e-15cccad29d0b.png)


</details>

## Why It's Good For The Game

Less curator ID's stuck in the Trophy Cases, and the existing ones can
be cleaned up. A more immersive Trophy Case user experience, in general.

## Changelog


:cl:
refactor: refactored trophy cases, to be more user friendly
admin: created a trophy managment admin panel
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[cb20ec99f9...](https://github.com/necromanceranne/tgstation/commit/cb20ec99f9cac1f0ca60da1b9dc912ea4e9eebba)
#### Friday 2022-12-09 04:05:39 by san7890

[MDB Ignore] Unit Tests for Invalid Space Turfs (Area Bullshit Edition) (#70967)

## About The Pull Request

So, there's some bullshit with the map loader(?) sometimes where it'll
let space turfs spawn in spots where we REALLY don't want space turfs.
Or, it could also just be a mapper screwing up. Anyways, we might miss
these, so let's set up a broad Unit Test that checks and verifies that
these round-ruining snagglers do _not_ exist.

In order to help me to do this, I standardized and fixed the
nomenclature such that `/area/ruin/space` is default for any map file in
`_maps/RandomRuins/SpaceRuins`, as well as it's subtypes. I also touched
up how we handle shuttle areas in these scenarios. This got a lot of
Unit Test noise filtered out, and is crucial for its functioning. It
should also be how we did it from the start anyways. I added in an
UpdatePaths for any compatible change, but it was completely
non-workable for some of the area type updates.

I also fixed any organic bugs that didn't require an areas type update.
Cool.

Placing space turfs on IceBox:

![image](https://user-images.githubusercontent.com/34697715/199177940-21c64964-1808-41b0-9a92-bf5b82eee2fa.png)

Organically found issues:

![image](https://user-images.githubusercontent.com/34697715/199177972-b27a89de-0e1a-41e5-8fa4-3bee1763b9da.png)

I also added a `planetary` variable to `/datum/map_config` because I
didn't like the hack I was using to see if we had a planetary map, and
I'd rather it just be an explicit variable in the map's JSON.

## Why It's Good For The Game

The less times we get Space Turfs showing up on IceBoxStation, the
better. It also standardizes areas a bit more, which I like (we were
using some incorrect ones in the wrong spots, so those were touched up
in this PR as well). Like, if it's a space ruin, we don't need to use
the lengthy `/area/ruin/unpowered/no_grav` when `/area/ruin/space` does
the same thing.
## Changelog
Nothing in here should concern a player (unless I broke something)

Expect a few commits as I spam unit tests a few times and play
whack-a-mole with bugs.

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[5e1fa22b7e...](https://github.com/sqnztb/Skyrat-tg/commit/5e1fa22b7e0f59e8e60594fb85beaf5adb15fb56)
#### Friday 2022-12-09 04:15:28 by SkyratBot

[MIRROR] Changes Admin Prison to be Anti-Telekinesis: Walls off equipment rooms, replaces computers, and makes the tables tidy [MDB IGNORE] (#17794)

* Changes Admin Prison to be Anti-Telekinesis: Walls off equipment rooms, replaces computers, and makes the tables tidy (#71433)

First PR, may require some changes or something because I don't know how
to do anything bleh
## About The Pull Request

We already had issues with crewmembers with telekinesis making changes
to the security records (purging them and what not). And, nothing has
been done about it, not yet, anyway. Not only record computers are a
problem as well.

![image](https://user-images.githubusercontent.com/106710384/203241399-8314bcba-d2d0-44af-9360-30ff58dbc39e.png)
Previously, prisoners can access the sec vendor with telepathy, and,
since the vendor is free, spam the vendor and be an annoyance. Sure, I
believe that it is not as big of a problem as purging the security
records, but I feel like it's against what the prison is supposed to
stand for; It's supposed to stop them and get them to listen to ahelps
thrown at them.

I've decided to make a bit of changes to the prison to make it so that
people with telekinesis won't fuck up things as much. This replaces real
computers with nonfunctional ones, adding walls to equipment areas to
make sure prisoners don't spam the vendor, and deletes guns/weapons from
the tables so they won't grab them.

## Why It's Good For The Game

![image](https://user-images.githubusercontent.com/106710384/203241465-833f79da-58a3-4feb-87b0-091fbb846e93.png)
This PR is more tailored to admins dealing with no-good-doers, and goes
for the vibe of "HEY, SOMEONE IS PMING YOU, REPLY TO THEM INSTEAD!" Of
course, this leads to prisoners not interacting with the current round,
and, less chance of them going insane and breaking all the windows with
a telekinesis auto-rifle.

Plus, this can always be reverted in-case someone comes up with coding
stuff in instead. I'm all through with that and willing to work with
whoever to solve the issue.

Also, of course, Closes #60967

## Changelog

:cl:
admin: Nanotrashen made some top-of-the-line changes to their
top-of-the-line prison by walling off their equipment area and removing
some spare guns they somehow left on the tables. We also stole the
security computers, so people with telekinesis can't access them.
/:cl:

* Changes Admin Prison to be Anti-Telekinesis: Walls off equipment rooms, replaces computers, and makes the tables tidy

Co-authored-by: Epic <106710384+epicgamer545@users.noreply.github.com>

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[0ca2c0b527...](https://github.com/sqnztb/Skyrat-tg/commit/0ca2c0b527a564de32818057b7fc09eb07875f51)
#### Friday 2022-12-09 04:15:28 by SkyratBot

[MIRROR] Gives bread and cake slice_types and adds screentip verbs to proccessed foods [MDB IGNORE] (#17721)

* Gives bread and cake slice_types and adds screentip verbs to proccessed foods (#71449)

## About The Pull Request

A side effect of my pizza PR #71202 I added contextual screentips as
part of processable.dm. In doing this, I noticed that with a few
exceptions, almost every single bread and cake type copies the proc
exactly the same for every single child of cake or bread, so I put the
proc on the parent of bread and cake and gave them slice_types, making
them more similar to pizza.dm

For everything else I've changed the default that I put in
processable.dm into "slice" or "cut" for things that use the knife and
"flatten" for things that use the rolling pin.

Finally, you can slice bread with saws now, because I think its silly
that only pizza gets this luxury.

## Why It's Good For The Game

Because it wasnt the focus of #71202 I didn't mess with screentips
outside of the pizza file a lot, but now that it's merged I figure I
should go and do that.
As Bread and Cake's processables are almost fully standardized it seems
silly for them to call on the proc 12 times in the same document so I
did this, which also allows for more versatility in editing how they
work as well allow people to, if they want to, add more tool behaviours
in the future without adding in 12 lines of code. Also means that people
who want to add new cake or bread have one less thing to do.

## Changelog

:cl:
add: you can saw bread with a saw into bread slices
qol: added screentip verbs to a bunch of food files
code: bread and cake now have slice types and all only have one call on
the processable.dm proc
/:cl:

* Gives bread and cake slice_types and adds screentip verbs to proccessed foods

* sco'ish

* fuck me ig

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [ShizCalev/tgstation](https://github.com/ShizCalev/tgstation)@[83f475aa7e...](https://github.com/ShizCalev/tgstation/commit/83f475aa7ec4290c6961f1f14c5da80f340989b8)
#### Friday 2022-12-09 04:19:30 by tralezab

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
## [ShizCalev/tgstation](https://github.com/ShizCalev/tgstation)@[35b5ac0c4e...](https://github.com/ShizCalev/tgstation/commit/35b5ac0c4e6bbaf2adf277a7ea7a4a4eab89726b)
#### Friday 2022-12-09 04:19:30 by Fikou

Psykers (#71566)

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

Co-authored-by: tralezab <spamqetuo2@gmail.com>
Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [netaneta123/app-dev](https://github.com/netaneta123/app-dev)@[1df805b760...](https://github.com/netaneta123/app-dev/commit/1df805b760f2136726847ea9e59b83b895936a92)
#### Friday 2022-12-09 04:45:02 by netaneta123

Update README.md

<dl>
<dt> Bleach - Thousand Year Blood War</dt>
<dd> This is about soul reapers, and quincys </dd>
<dt> Kimetsu no yaiba / Demon Slayer </dt>
<dd> This is about hunting demons </dd>
<dt> Neon Evangelion </dt>
<dd> This is mecha anime about robots vs. angels </dd>
</dl>

---
## [SAnschutz/practice-git](https://github.com/SAnschutz/practice-git)@[3e75622506...](https://github.com/SAnschutz/practice-git/commit/3e756225060d96a2bd49ec3bd342b3624a8d725e)
#### Friday 2022-12-09 05:18:21 by gacetta

There is unrest in the galaxy. Revolts. Looting. Riots. Revolution. Resistance. Real trouble in THE EMPIRE. STRIKES. BACK in the day, before he was Darth Vader, he was just a boy named Anakin.

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[9d5df80e01...](https://github.com/swarm-game/swarm/commit/9d5df80e01334fac8118ed96de7bba1b71a123a5)
#### Friday 2022-12-09 05:36:09 by Brent Yorgey

Copy requirements map to robot context when loading a new `ProcessedTerm` (#827)

Closes #540.

When we typecheck and capability check a new term, resulting in a `ProcessedTerm`, we already know the `Requirement`s for all the `def`s it contains.  This PR simply takes all those definition requirements and adds them to `robotContext . defReqs` just before installing the new `ProcessedTerm` in the CESK machine, so that if we ever encounter the name of any of the definitions inside an argument to `build` or `reprogram`---which we capability check at runtime---we will be able to properly match up names with their requirements.

This is a hack for several reasons:
- We really shouldn't be capability-checking arguments to `build` and `reprogram` at runtime in the first place---ideally we should be able to check everything statically.  But fixing that will require implementing #231 .
- We have to do this in three places in the code: when loading a new term into the base when the player hits Enter at the REPL; when executing `run`; and when running the solution from a scenario in the integration tests.  Ideally, there would be only one place, but I don't have a good idea at the moment how to refactor things properly.
- Technically, the names being defined shouldn't be in scope until after their corresponding `def` runs, so it's incorrect to dump them all into the `defReqs` prior to executing any of the `def`s.
    - However, doing it properly, with each name coming into scope with its requirements right after the `def` runs, is very tricky/annoying to implement for more reasons than I care to write about here (believe me, I tried, and it made my brain hurt).  For starters, we don't really have access to the robot state when stepping the CESK machine.
    - The only scenario where this would be a problem is if (1) there is already a name `x` defined, and then we (2) `run` a `.sw` file containing, first, a `build` command whose argument references `x`, and second, a redefinition of `x`.  In that case the `build` would incorrectly decide that the `x` in the argument to `build` has the requirements of the *second* `x` (the one that will be redefined later) even though the first `x` is the one that should still be in scope.  However, this seems like a very unlikely scenario (who would write a `.sw` file that depends on some specific name already being defined before it is run, but then redefines that same name later?) and I'd *much* rather have that obscure problem than the current very relevant and annoying one.

However, it's a simple hack that solves the issue and will be easy to get rid of later if and when we do something better.  I'm a big believer in doing things the right way, but in this instance I definitely think we should just do the simple thing that mostly works and then continue to make it better in the future.

---
## [siimsek/Lightning-Kernel](https://github.com/siimsek/Lightning-Kernel)@[f66ef8aa00...](https://github.com/siimsek/Lightning-Kernel/commit/f66ef8aa00a2f5dafbb48dacda945ec0b5a5d65c)
#### Friday 2022-12-09 06:32:37 by siimsek

    Merge 4.14.301 into android-4.14-stable

    Changes in 4.14.301
    	wifi: mac80211_hwsim: fix debugfs attribute ps with rc table support
    	audit: fix undefined behavior in bit shift for AUDIT_BIT
    	wifi: mac80211: Fix ack frame idr leak when mesh has no route
    	spi: stm32: fix stm32_spi_prepare_mbr() that halves spi clk for every run
    	MIPS: pic32: treat port as signed integer
    	af_key: Fix send_acquire race with pfkey_register
    	ARM: dts: am335x-pcm-953: Define fixed regulators in root node
    	bus: sunxi-rsb: Support atomic transfers
    	ARM: dts: at91: sam9g20ek: enable udc vbus gpio pinctrl
    	nfc/nci: fix race with opening and closing
    	net: pch_gbe: fix potential memleak in pch_gbe_tx_queue()
    	9p/fd: fix issue of list_del corruption in p9_fd_cancel()
    	ARM: mxs: fix memory leak in mxs_machine_init()
    	net/mlx4: Check retval of mlx4_bitmap_init
    	net/qla3xxx: fix potential memleak in ql3xxx_send()
    	xfrm: Fix ignored return value in xfrm6_init()
    	NFC: nci: fix memory leak in nci_rx_data_packet()
    	dccp/tcp: Reset saddr on failure after inet6?_hash_connect().
    	s390/dasd: fix no record found for raw_track_access
    	nfc: st-nci: fix incorrect validating logic in EVT_TRANSACTION
    	nfc: st-nci: fix memory leaks in EVT_TRANSACTION
    	net: thunderx: Fix the ACPI memory leak
    	s390/crashdump: fix TOD programmable field size
    	nios2: add FORCE for vmlinuz.gz
    	arm64: dts: rockchip: lower rk3399-puma-haikou SD controller clock frequency
    	iio: light: apds9960: fix wrong register for gesture gain
    	iio: core: Fix entry not deleted when iio_register_sw_trigger_type() fails
    	kconfig: display recursive dependency resolution hint just once
    	nilfs2: fix nilfs_sufile_mark_dirty() not set segment usage as dirty
    	Input: synaptics - switch touchpad on HP Laptop 15-da3001TU to RMI mode
    	serial: 8250: 8250_omap: Avoid RS485 RTS glitch on ->set_termios()
    	xen/platform-pci: add missing free_irq() in error path
    	platform/x86: asus-wmi: add missing pci_dev_put() in asus_wmi_set_xusb2pr()
    	platform/x86: acer-wmi: Enable SW_TABLET_MODE on Switch V 10 (SW5-017)
    	platform/x86: hp-wmi: Ignore Smart Experience App event
    	tcp: configurable source port perturb table size
    	net: usb: qmi_wwan: add Telit 0x103a composition
    	drm/amdgpu: always register an MMU notifier for userptr
    	iio: health: afe4403: Fix oob read in afe4403_read_raw
    	iio: health: afe4404: Fix oob read in afe4404_[read|write]_raw
    	iio: light: rpr0521: add missing Kconfig dependencies
    	hwmon: (i5500_temp) fix missing pci_disable_device()
    	hwmon: (ibmpex) Fix possible UAF when ibmpex_register_bmc() fails
    	of: property: decrement node refcount in of_fwnode_get_reference_args()
    	net/mlx5: Fix uninitialized variable bug in outlen_write()
    	can: sja1000_isa: sja1000_isa_probe(): add missing free_sja1000dev()
    	can: cc770: cc770_isa_probe(): add missing free_cc770dev()
    	qlcnic: fix sleep-in-atomic-context bugs caused by msleep
    	net: phy: fix null-ptr-deref while probe() failed
    	net: net_netdev: Fix error handling in ntb_netdev_init_module()
    	net/9p: Fix a potential socket leak in p9_socket_open
    	dsa: lan9303: Correct stat name
    	net: hsr: Fix potential use-after-free
    	packet: do not set TP_STATUS_CSUM_VALID on CHECKSUM_COMPLETE
    	net: ethernet: renesas: ravb: Fix promiscuous mode after system resumed
    	hwmon: (coretemp) Check for null before removing sysfs attrs
    	hwmon: (coretemp) fix pci device refcount leak in nv1a_ram_new()
    	perf: Add sample_flags to indicate the PMU-filled sample data
    	btrfs: qgroup: fix sleep from invalid context bug in btrfs_qgroup_inherit()
    	tools/vm/slabinfo-gnuplot: use "grep -E" instead of "egrep"
    	nilfs2: fix NULL pointer dereference in nilfs_palloc_commit_free_entry()
    	x86/bugs: Make sure MSR_SPEC_CTRL is updated properly upon resume from S3
    	arm64: Fix panic() when Spectre-v2 causes Spectre-BHB to re-allocate KVM vectors
    	arm64: errata: Fix KVM Spectre-v2 mitigation selection for Cortex-A57/A72
    	efi: random: Properly limit the size of the random seed
    	ASoC: ops: Fix bounds check for _sx controls
    	pinctrl: single: Fix potential division by zero
    	iommu/vt-d: Fix PCI device refcount leak in dmar_dev_scope_init()
    	tcp/udp: Fix memory leak in ipv6_renew_options().
    	nvme: restrict management ioctls to admin
    	x86/tsx: Add a feature bit for TSX control MSR support
    	x86/pm: Add enumeration check before spec MSRs save/restore setup
    	Bluetooth: L2CAP: Fix accepting connection request for invalid SPSM
    	x86/ioremap: Fix page aligned size calculation in __ioremap_caller()
    	mmc: sdhci: use FIELD_GET for preset value bit masks
    	mmc: sdhci: Fix voltage switch delay
    	proc: avoid integer type confusion in get_proc_long
    	proc: proc_skip_spaces() shouldn't think it is working on C strings
    	v4l2: don't fall back to follow_pfn() if pin_user_pages_fast() fails
    	ipc/sem: Fix dangling sem_array access in semtimedop race
    	x86/nospec: Fix i386 RSB stuffing
    	Revert "x86/speculation: Change FILL_RETURN_BUFFER to work with objtool"
    	Linux 4.14.301

    Change-Id: I4c27385f0c1a0b71629ec158a1ce88540584db49
    Signed-off-by: Greg Kroah-Hartman <gregkh@google.com>

commit 980d7f36ac7b6889bb1415db426a18d0fbc9bdd8
Merge: e0d945721c52 179ef7fe8677
Author: Greg Kroah-Hartman <gregkh@google.com>
Date:   Mon Nov 28 16:00:17 2022 +0000

    Merge 4.14.300 into android-4.14-stable

    Changes in 4.14.300
    	HID: hyperv: fix possible memory leak in mousevsc_probe()
    	net: gso: fix panic on frag_list with mixed head alloc types
    	bnxt_en: fix potentially incorrect return value for ndo_rx_flow_steer
    	net: fman: Unregister ethernet device on removal
    	capabilities: fix undefined behavior in bit shift for CAP_TO_MASK
    	net: lapbether: fix issue of dev reference count leakage in lapbeth_device_event()
    	hamradio: fix issue of dev reference count leakage in bpq_device_event()
    	drm/vc4: Fix missing platform_unregister_drivers() call in vc4_drm_register()
    	ipv6: addrlabel: fix infoleak when sending struct ifaddrlblmsg to network
    	tipc: fix the msg->req tlv len check in tipc_nl_compat_name_table_dump_header
    	dmaengine: mv_xor_v2: Fix a resource leak in mv_xor_v2_remove()
    	drivers: net: xgene: disable napi when register irq failed in xgene_enet_open()
    	net: cxgb3_main: disable napi when bind qsets failed in cxgb_up()
    	ethernet: s2io: disable napi when start nic failed in s2io_card_up()
    	net: mv643xx_eth: disable napi when init rxq or txq failed in mv643xx_eth_open()
    	net: macvlan: fix memory leaks of macvlan_common_newlink
    	arm64: efi: Fix handling of misaligned runtime regions and drop warning
    	ALSA: hda: fix potential memleak in 'add_widget_node'
    	ALSA: usb-audio: Add quirk entry for M-Audio Micro
    	nilfs2: fix deadlock in nilfs_count_free_blocks()
    	drm/i915/dmabuf: fix sg_table handling in map_dma_buf
    	platform/x86: hp_wmi: Fix rfkill causing soft blocked wifi
    	btrfs: selftests: fix wrong error check in btrfs_free_dummy_root()
    	udf: Fix a slab-out-of-bounds write bug in udf_find_entry()
    	cert host tools: Stop complaining about deprecated OpenSSL functions
    	dmaengine: at_hdmac: Fix at_lli struct definition
    	dmaengine: at_hdmac: Don't start transactions at tx_submit level
    	dmaengine: at_hdmac: Fix completion of unissued descriptor in case of errors
    	dmaengine: at_hdmac: Don't allow CPU to reorder channel enable
    	dmaengine: at_hdmac: Fix impossible condition
    	dmaengine: at_hdmac: Check return code of dma_async_device_register
    	x86/cpu: Restore AMD's DE_CFG MSR after resume
    	selftests/futex: fix build for clang
    	drm/imx: imx-tve: Fix return type of imx_tve_connector_mode_valid
    	Bluetooth: L2CAP: Fix l2cap_global_chan_by_psm
    	ASoC: core: Fix use-after-free in snd_soc_exit()
    	serial: 8250_omap: remove wait loop from Errata i202 workaround
    	serial: 8250: omap: Flush PM QOS work on remove
    	tty: n_gsm: fix sleep-in-atomic-context bug in gsm_control_send
    	ASoC: soc-utils: Remove __exit for snd_soc_util_exit()
    	block: sed-opal: kmalloc the cmd/resp buffers
    	parport_pc: Avoid FIFO port location truncation
    	pinctrl: devicetree: fix null pointer dereferencing in pinctrl_dt_to_map
    	net: bgmac: Drop free_netdev() from bgmac_enet_remove()
    	mISDN: fix possible memory leak in mISDN_dsp_element_register()
    	mISDN: fix misuse of put_device() in mISDN_register_device()
    	net: caif: fix double disconnect client in chnl_net_open()
    	xen/pcpu: fix possible memory leak in register_pcpu()
    	drbd: use after free in drbd_create_device()
    	net/x25: Fix skb leak in x25_lapb_receive_frame()
    	cifs: Fix wrong return value checking when GETFLAGS
    	ftrace: Fix the possible incorrect kernel message
    	ftrace: Optimize the allocation for mcount entries
    	ftrace: Fix null pointer dereference in ftrace_add_mod()
    	ring_buffer: Do not deactivate non-existant pages
    	ALSA: usb-audio: Drop snd_BUG_ON() from snd_usbmidi_output_open()
    	USB: serial: option: add Sierra Wireless EM9191
    	USB: serial: option: remove old LARA-R6 PID
    	USB: serial: option: add u-blox LARA-R6 00B modem
    	USB: serial: option: add u-blox LARA-L6 modem
    	USB: serial: option: add Fibocom FM160 0x0111 composition
    	usb: add NO_LPM quirk for Realforce 87U Keyboard
    	usb: chipidea: fix deadlock in ci_otg_del_timer
    	iio: adc: at91_adc: fix possible memory leak in at91_adc_allocate_trigger()
    	iio: trigger: sysfs: fix possible memory leak in iio_sysfs_trig_init()
    	iio: pressure: ms5611: changed hardcoded SPI speed to value limited
    	dm ioctl: fix misbehavior if list_versions races with module loading
    	serial: 8250: Fall back to non-DMA Rx if IIR_RDI occurs
    	serial: 8250_lpss: Configure DMA also w/o DMA filter
    	mmc: core: properly select voltage range without power cycle
    	mmc: sdhci-pci: Fix possible memory leak caused by missing pci_dev_put()
    	misc/vmw_vmci: fix an infoleak in vmci_host_do_receive_datagram()
    	nilfs2: fix use-after-free bug of ns_writer on remount
    	serial: 8250: Flush DMA Rx on RLSI
    	macvlan: enforce a consistent minimal mtu
    	tcp: cdg: allow tcp_cdg_release() to be called multiple times
    	kcm: avoid potential race in kcm_tx_work
    	bpf, test_run: Fix alignment problem in bpf_prog_test_run_skb()
    	kcm: close race conditions on sk_receive_queue
    	9p: trans_fd/p9_conn_cancel: drop client lock earlier
    	gfs2: Check sb_bsize_shift after reading superblock
    	gfs2: Switch from strlcpy to strscpy
    	9p/trans_fd: always use O_NONBLOCK read/write
    	mm: fs: initialize fsdata passed to write_begin/write_end interface
    	ntfs: fix use-after-free in ntfs_attr_find()
    	ntfs: fix out-of-bounds read in ntfs_attr_find()
    	ntfs: check overflow when iterating ATTR_RECORDs
    	Linux 4.14.300

    Change-Id: I6e30b49a26cfda34ab6d259641dc4ea488d312eb
    Signed-off-by: Greg Kroah-Hartman <gregkh@google.com>

commit e0d945721c52855bb58d9b07e344b64d50cb70b4
Merge: d3693c5e4a29 e911713e40ca
Author: Greg Kroah-Hartman <gregkh@google.com>
Date:   Thu Nov 10 20:08:43 2022 +0100

    Merge 4.14.299 into android-4.14-stable

    Changes in 4.14.299
    	NFSv4.1: Handle RECLAIM_COMPLETE trunking errors
    	NFSv4.1: We must always send RECLAIM_COMPLETE after a reboot
    	nfs4: Fix kmemleak when allocate slot failed
    	net: dsa: Fix possible memory leaks in dsa_loop_init()
    	nfc: s3fwrn5: Fix potential memory leak in s3fwrn5_nci_send()
    	nfc: nfcmrvl: Fix potential memory leak in nfcmrvl_i2c_nci_send()
    	net: fec: fix improper use of NETDEV_TX_BUSY
    	ata: pata_legacy: fix pdc20230_set_piomode()
    	net: sched: Fix use after free in red_enqueue()
    	ipvs: use explicitly signed chars
    	rose: Fix NULL pointer dereference in rose_send_frame()
    	mISDN: fix possible memory leak in mISDN_register_device()
    	isdn: mISDN: netjet: fix wrong check of device registration
    	btrfs: fix inode list leak during backref walking at resolve_indirect_refs()
    	btrfs: fix ulist leaks in error paths of qgroup self tests
    	Bluetooth: L2CAP: Fix use-after-free caused by l2cap_reassemble_sdu
    	Bluetooth: L2CAP: fix use-after-free in l2cap_conn_del()
    	net: mdio: fix undefined behavior in bit shift for __mdiobus_register
    	net, neigh: Fix null-ptr-deref in neigh_table_clear()
    	media: s5p_cec: limit msg.len to CEC_MAX_MSG_SIZE
    	media: dvb-frontends/drxk: initialize err to 0
    	i2c: xiic: Add platform module alias
    	Bluetooth: L2CAP: Fix attempting to access uninitialized memory
    	block, bfq: protect 'bfqd->queued' by 'bfqd->lock'
    	btrfs: fix type of parameter generation in btrfs_get_dentry
    	tcp/udp: Make early_demux back namespacified.
    	capabilities: fix potential memleak on error path from vfs_getxattr_alloc()
    	ALSA: usb-audio: Add quirks for MacroSilicon MS2100/MS2106 devices
    	efi: random: reduce seed size to 32 bytes
    	parisc: Make 8250_gsc driver dependend on CONFIG_PARISC
    	parisc: Export iosapic_serial_irq() symbol for serial port driver
    	ext4: fix warning in 'ext4_da_release_space'
    	KVM: x86: Mask off reserved bits in CPUID.80000008H
    	KVM: x86: emulator: em_sysexit should update ctxt->mode
    	KVM: x86: emulator: introduce emulator_recalc_and_set_mode
    	KVM: x86: emulator: update the emulation mode after CR0 write
    	linux/const.h: prefix include guard of uapi/linux/const.h with _UAPI
    	linux/const.h: move UL() macro to include/linux/const.h
    	linux/bits.h: make BIT(), GENMASK(), and friends available in assembly
    	wifi: brcmfmac: Fix potential buffer overflow in brcmf_fweh_event_worker()
    	Linux 4.14.299

    Signed-off-by: Greg Kroah-Hartman <gregkh@google.com>
    Change-Id: Id5fc7f49fbfe0ce07862d5484f49035b8c664206

commit d3693c5e4a29e5e7515848bb515298fac88d3313
Merge: 79b5f31410c5 a901bb6c7db7
Author: Greg Kroah-Hartman <gregkh@google.com>
Date:   Thu Nov 10 20:08:10 2022 +0100

    Merge 4.14.298 into android-4.14-stable

    Changes in 4.14.298
    	ocfs2: clear dinode links count in case of error
    	ocfs2: fix BUG when iput after ocfs2_mknod fails
    	x86/microcode/AMD: Apply the patch early on every logical thread
    	ata: ahci-imx: Fix MODULE_ALIAS
    	ata: ahci: Match EM_MAX_SLOTS with SATA_PMP_MAX_PORTS
    	KVM: arm64: vgic: Fix exit condition in scan_its_table()
    	arm64: errata: Remove AES hwcap for COMPAT tasks
    	r8152: add PID for the Lenovo OneLink+ Dock
    	btrfs: fix processing of delayed data refs during backref walking
    	ACPI: extlog: Handle multiple records
    	HID: magicmouse: Do not set BTN_MOUSE on double report
    	net/atm: fix proc_mpc_write incorrect return value
    	net: hns: fix possible memory leak in hnae_ae_register()
    	iommu/vt-d: Clean up si_domain in the init_dmars() error path
    	media: v4l2-mem2mem: Apply DST_QUEUE_OFF_BASE on MMAP buffers across ioctls
    	ACPI: video: Force backlight native for more TongFang devices
    	ALSA: Use del_timer_sync() before freeing timer
    	ALSA: au88x0: use explicitly signed char
    	USB: add RESET_RESUME quirk for NVIDIA Jetson devices in RCM
    	usb: dwc3: gadget: Don't set IMI for no_interrupt
    	usb: bdc: change state when port disconnected
    	usb: xhci: add XHCI_SPURIOUS_SUCCESS to ASM1042 despite being a V0.96 controller
    	xhci: Remove device endpoints from bandwidth list when freeing the device
    	tools: iio: iio_utils: fix digit calculation
    	iio: light: tsl2583: Fix module unloading
    	fbdev: smscufx: Fix several use-after-free bugs
    	mac802154: Fix LQI recording
    	drm/msm/hdmi: fix memory corruption with too many bridges
    	mmc: core: Fix kernel panic when remove non-standard SDIO card
    	kernfs: fix use-after-free in __kernfs_remove
    	s390/futex: add missing EX_TABLE entry to __futex_atomic_op()
    	Xen/gntdev: don't ignore kernel unmapping error
    	xen/gntdev: Prevent leaking grants
    	mm,hugetlb: take hugetlb_lock before decrementing h->resv_huge_pages
    	net: ieee802154: fix error return code in dgram_bind()
    	drm/msm: Fix return type of mdp4_lvds_connector_mode_valid
    	arc: iounmap() arg is volatile
    	ALSA: ac97: fix possible memory leak in snd_ac97_dev_register()
    	x86/unwind/orc: Fix unreliable stack dump with gcov
    	amd-xgbe: fix the SFP compliance codes check for DAC cables
    	amd-xgbe: add the bit rate quirk for Molex cables
    	kcm: annotate data-races around kcm->rx_psock
    	kcm: annotate data-races around kcm->rx_wait
    	net: lantiq_etop: don't free skb when returning NETDEV_TX_BUSY
    	tcp: fix indefinite deferral of RTO with SACK reneging
    	can: mscan: mpc5xxx: mpc5xxx_can_probe(): add missing put_clock() in error path
    	PM: hibernate: Allow hybrid sleep to work with s2idle
    	media: vivid: s_fbuf: add more sanity checks
    	media: vivid: dev->bitmap_cap wasn't freed in all cases
    	media: v4l2-dv-timings: add sanity checks for blanking values
    	media: videodev2.h: V4L2_DV_BT_BLANKING_HEIGHT should check 'interlaced'
    	i40e: Fix ethtool rx-flow-hash setting for X722
    	i40e: Fix flow-type by setting GL_HASH_INSET registers
    	net: ksz884x: fix missing pci_disable_device() on error in pcidev_init()
    	PM: domains: Fix handling of unavailable/disabled idle states
    	ALSA: aoa: i2sbus: fix possible memory leak in i2sbus_add_dev()
    	ALSA: aoa: Fix I2S device accounting
    	openvswitch: switch from WARN to pr_warn
    	net: ehea: fix possible memory leak in ehea_register_port()
    	can: rcar_canfd: rcar_canfd_handle_global_receive(): fix IRQ storm on global FIFO receive
    	Linux 4.14.298

    Signed-off-by: Greg Kroah-Hartman <gregkh@google.com>
    Change-Id: Icecdfe113c36f021fb51189827cd5c65b67c76e3

---
## [Chubbygummibear/Yogstation-TG](https://github.com/Chubbygummibear/Yogstation-TG)@[8a87301c84...](https://github.com/Chubbygummibear/Yogstation-TG/commit/8a87301c84287ec6f2e1549ba3bb67e071065a63)
#### Friday 2022-12-09 07:57:34 by Vaelophis Nyx

[ASTEROID] Atmos Approved: Atmospherics Changes + More (#16111)

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

* guh

* fuck you mapbot

* need that to breathe!

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

---
## [Evolution-X/frameworks_base](https://github.com/Evolution-X/frameworks_base)@[2752c70fd2...](https://github.com/Evolution-X/frameworks_base/commit/2752c70fd2994f5f527847ad3d87f78260d00a9e)
#### Friday 2022-12-09 08:17:18 by Joey Huab

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

---
## [NamDevW/6-Xau-ki-tu](https://github.com/NamDevW/6-Xau-ki-tu)@[843c23c1bf...](https://github.com/NamDevW/6-Xau-ki-tu/commit/843c23c1bf913ecc5a3f6196a1513b9970836e94)
#### Friday 2022-12-09 08:24:34 by Trần Phương Nam

Create Strong Password.cpp

Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
Example


This password is 5 characters long and is missing an uppercase and a special character. The minimum number of characters to add is .


This password is 5 characters long and has at least one of each character type. The minimum number of characters to add is .

Function Description

Complete the minimumNumber function in the editor below.

minimumNumber has the following parameters:

int n: the length of the password
string password: the password to test
Returns

int: the minimum number of characters to add
Input Format

The first line contains an integer , the length of the password.

The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

Constraints

All characters in  are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ].
Sample Input 0

3
Ab1
Sample Output 0

3
Explanation 0

She can make the password strong by adding  characters, for example, $hk, turning the password into Ab1$hk which is strong.

 characters aren't enough since the length must be at least .

Sample Input 1

11
#HackerRank
Sample Output 1

1
Explanation 1

The password isn't strong, but she can make it strong by adding a single digit.

---
## [BrianAllenBalagot/app-dev](https://github.com/BrianAllenBalagot/app-dev)@[927fd40351...](https://github.com/BrianAllenBalagot/app-dev/commit/927fd40351c16c84bd5136826d302e354ceeab93)
#### Friday 2022-12-09 09:03:19 by BrianAllenBalagot

Update README.md

First Love About two student couple and the girl accident then her memory she forget in the ending the memories back and she find the guy his first love.
That Time I Got Reincarnated as a Slime is anime the guy die then he reincarnate as a slime.
Naruto is a main character in Naruto Shippuden

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9440d42a8e...](https://github.com/tgstation/tgstation/commit/9440d42a8e1c5f268a614948769c67558e79b98d)
#### Friday 2022-12-09 09:35:05 by MrMelbert

Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. (#71674)

## About The Pull Request

- The chaplain choice beacon now uses a radial to select the armor set,
instead of a list, giving the user a preview of what each looks like.


![image](https://user-images.githubusercontent.com/51863163/205417930-f5ceab11-6974-48a9-a871-abcb8228bcf2.png)

- Lots of additional cleanup to choice beacon code in general. Less copy
pasted code.
- All beacons now speak from the beacon with their message, instead of
some going by "headset message". Soul removed

## Why It's Good For The Game

I always forgot when selecting my armor which looks like what, and
choosing an ugly one is a pain since you only get one choice. This
should help chaplains get the armor they actually want without needing
to check the wiki.

## Changelog

:cl: Melbert
qol: The chaplain's armament beacon now displays a radial instead of a
text list, showing previews of what all the armor sets look like
qol: (Almost) all choice beacons now use a pod to send their item,
instead of just magicking it under your feet
code: Cleaned up some choice beacon code. 
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [tonton-golio/computational_physics](https://github.com/tonton-golio/computational_physics)@[27cf4747fa...](https://github.com/tonton-golio/computational_physics/commit/27cf4747fa5099d47c442e031ff074b68f814de1)
#### Friday 2022-12-09 10:03:29 by Riz

Change taxi to microscope

 I hate taxis, they're yellow. The colour yellow is in the bottom 10 percentile of colours. I mean you've got stuff like red, blue, grey, white, why would you paint a taxi yellow??? It doesn't seem to make sense, did the designers just want the taxi to be the ugliest thing on the road? Britain did it right with Hackney Carriages: Classic, beautifully styled, and black. The black cab, to me, is more impressive to see prowling the streets than a yellow cab. Interestingly, both the colours are mentioned in the Wiz Khalifa song: Could Wiz be behind it all? Is he the man pulling the strings between taxis worldwide???

---
## [jackdmorrison/Advent_callendar_2022](https://github.com/jackdmorrison/Advent_callendar_2022)@[c5767db53e...](https://github.com/jackdmorrison/Advent_callendar_2022/commit/c5767db53e8cea171e95751e26b4d7c515ec0b1d)
#### Friday 2022-12-09 11:25:22 by jack morrison

feel stupid

i made solution2 with code i found in the solution megathread because for the first section i was 100% sure i was doing it right but it turns out it was giving me exactly half the amount it should have for my file but for the test it was working correctly, still think it was a good solution but no idea what messes up so i cheated and feel like an idiot

---
## [DEFRA/water-abstraction-system](https://github.com/DEFRA/water-abstraction-system)@[06d45e8627...](https://github.com/DEFRA/water-abstraction-system/commit/06d45e86272fb5a3c2e72fa1376e1d9d1b1c1d65)
#### Friday 2022-12-09 11:30:24 by Alan Cruikshanks

Replacing classes with modules and functions (#46)

> Classes are a template for creating objects.

That is the first sentence of the Mozilla documentation for **Classes**. It is what those of us from other languages understand classes to be for. For some of us though (we're looking at you @Cruikshanks !) classes are _all things_!

Because of that thinking, we've allowed Classes to creep in where they shouldn't really be used. Most noticeably, things like controllers, presenters and services, are formed of purely static methods. There is no real reason to wrap their functionality in a class. They could just be expressed as modules and export their relevant functions.

That's what those experienced with JavaScript are more likely to expect. By not doing things that way we're breaking the [Principle of least astonishment](https://en.wikipedia.org/wiki/Principle_of_least_astonishment).

We believe classes are suitable for our Models, as it follows the convention of [Objection](https://vincit.github.io/objection.js/guide/models.html) and we do create instances of them. Also, classes will be our go-to if we need to create objects in the future.

But before this repo gets too far down the road we're taking this opportunity to refactor things from classes into modules.

---
## [geneoss/rust](https://github.com/geneoss/rust)@[2f506e6dd4...](https://github.com/geneoss/rust/commit/2f506e6dd4eb4a3727aab8ba6349e80e3383dca9)
#### Friday 2022-12-09 11:38:23 by Yuki Okushi

Rollup merge of #101368 - thomcc:wintls-noinline, r=ChrisDenton

Forbid inlining `thread_local!`'s `__getit` function on Windows

Sadly, this will make things slower to avoid UB in an edge case, but it seems hard to avoid... and really whenever I look at this code I can't help but think we're asking for trouble.

It's pretty dodgy for us to leave this as a normal function rather than `#[inline(never)]`, given that if it *does* get inlined into a dynamically linked component, it's extremely unsafe (you get some other thread local, or if you're lucky, crash). Given that it's pretty rare for people to use dylibs on Windows, the fact that we haven't gotten bug reports about it isn't really that convincing. Ideally we'd come up with some kind of compiler solution (that avoids paying for this cost when static linking, or *at least* for use within the same crate...), but it's not clear what that looks like.

Oh, and because all this is only needed when we're implementing `thread_local!` with `#[thread_local]`, this patch adjusts the `cfg_attr` to be `all(windows, target_thread_local)` as well.

r? ``@ChrisDenton``

See also #84933, which is about improving the situation.

---
## [h0yta/adventofcode](https://github.com/h0yta/adventofcode)@[0e90b02486...](https://github.com/h0yta/adventofcode/commit/0e90b02486005f9039b503e1babefce2555d948d)
#### Friday 2022-12-09 12:28:43 by hoyta

Silent night, holy night

All is calm, all is bright.
Round yon Virgin, Mother and Child.
Holy infant so tender and mild,
Sleep in heavenly peace,
Sleep in heavenly peace

---
## [Top300Reyna/app-dev](https://github.com/Top300Reyna/app-dev)@[680bf20df4...](https://github.com/Top300Reyna/app-dev/commit/680bf20df4870f054dfb0f25a3913f4f1bc5453f)
#### Friday 2022-12-09 13:07:51 by Top300Reyna

Update README.md

<h1>Bleach</h1>

<p><strong>Bleach</strong> (stylized as BLEACH) is a <em><strong>Japanese anime television series based on Tite Kubo's original manga series of the same name</strong></em>. It was produced by Studio Pierrot and directed by Noriyuki Abe. The series aired on TV Tokyo from October 2004 to March 2012, spanning 366 episodes. The story follows the adventures of Ichigo Kurosaki after he obtains the powers of a Soul Reaper—a death personification similar to the Grim Reaper—from another Soul Reaper, Rukia Kuchiki. His newfound powers force him to take on the duties of defending humans from evil spirits and guiding departed souls to the afterlife. In addition to adapting the manga series, it is based on, the anime periodically includes original self-contained storylines and characters not found in the manga.
</p>
<p><em>I used to watch <strong>Bleach</strong> a lot when I was a kid, and it was my favorite Anime up until now</em>.
</p>
<p>Here are my top 4 favorite movies on Bleach.
</p>
<ol>
  <li>Bleach the Movie: Memories of Nobody (2006)</li>
  <li>Bleach the Movie: The DiamondDust Rebellion (2007)</li>
  <li>Bleach the Movie: Fade to Black (2008)</li>
  <li>Bleach the Movie: Hell Verse (2010)</li>
</ol>

---
## [Saurav-kattel/expressserver](https://github.com/Saurav-kattel/expressserver)@[9b011f91ff...](https://github.com/Saurav-kattel/expressserver/commit/9b011f91ff888392af76724a0aef94c0a83a31d0)
#### Friday 2022-12-09 13:14:46 by saurav kattel

fustration level 98% with fuck you in cors may be fixed

---
## [ItsVyzo/cmss13](https://github.com/ItsVyzo/cmss13)@[6120721323...](https://github.com/ItsVyzo/cmss13/commit/6120721323b6431a1d43d89d7354e1ea1763a734)
#### Friday 2022-12-09 13:47:56 by carlarctg

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Friday 2022-12-09 13:58:53 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [Kneba/platform_kernel_asus_sdm660](https://github.com/Kneba/platform_kernel_asus_sdm660)@[4b13571d1a...](https://github.com/Kneba/platform_kernel_asus_sdm660/commit/4b13571d1acbeb3a6ae08a9009c42b30d6b6e6f8)
#### Friday 2022-12-09 14:31:30 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [vicirdek/PsychonautStation](https://github.com/vicirdek/PsychonautStation)@[ebc0227176...](https://github.com/vicirdek/PsychonautStation/commit/ebc0227176b5213f379eefc3f5c6aa7be2d09c0a)
#### Friday 2022-12-09 14:57:47 by Tastyfish

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
## [rfl890/rfl890.github.io](https://github.com/rfl890/rfl890.github.io)@[9321969be9...](https://github.com/rfl890/rfl890.github.io/commit/9321969be93cefc27afa9219d15a5b77739e686f)
#### Friday 2022-12-09 15:02:01 by rfl890

FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. 

FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU. FUCK YOU.

---
## [Saurav-kattel/expressserver](https://github.com/Saurav-kattel/expressserver)@[172d507dc0...](https://github.com/Saurav-kattel/expressserver/commit/172d507dc0cc6a581c0705ab562ed79fa89c4b04)
#### Friday 2022-12-09 15:14:41 by saurav kattel

fustration level 99% with fuck you in cors may be fixed 22

---
## [ebuzzing/blessclient](https://github.com/ebuzzing/blessclient)@[4cdb9c1999...](https://github.com/ebuzzing/blessclient/commit/4cdb9c199974373169aa012d23ef394ab3d4f7c0)
#### Friday 2022-12-09 15:14:45 by Justin Hutchings

Add CodeQL security scanning (#177)

Hi, I'm a PM on the GitHub security team. This repository is eligible to try the new [GitHub Advanced Security code scanning](https://help.github.com/en/github/finding-security-vulnerabilities-and-errors-in-your-code/about-code-scanning) beta.

Code scanning runs a static analysis tool called CodeQL which scans your code at build time to find any potential security issues. We've tuned the set of queries to be only the most severe, most precise issues. We'll show alerts in the security tab, and we'll show alerts for any net new vulnerabilities on pull requests as well. We've tried to make this super developer friendly, but we'd love your feedback as we work through the beta. 

If you're interested in trying it out, you can merge this pull request to set up the Actions workflow. You can also get this set up yourself in any additional repositories in this organization by following these [instructions](https://help.github.com/en/github/finding-security-vulnerabilities-and-errors-in-your-code/enabling-code-scanning)

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[efa85b9353...](https://github.com/newstools/2022-new-york-post/commit/efa85b9353196c56fb6b5460ed59021bb4044e6a)
#### Friday 2022-12-09 16:01:42 by Billy Einkamerer

Created Text For URL [nypost.com/2022/12/09/dear-abby-im-sick-of-financially-supporting-my-boyfriend/]

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[f50670b344...](https://github.com/cockroachdb/cockroach/commit/f50670b3440e91bec05aebc1bc425e4dd465583f)
#### Friday 2022-12-09 16:35:57 by Tobias Grieger

rpc: re-work connection maintenance

This commit simplifies the `rpc` package.

The main aim is to make the code and the logging it produces somewhat
clearer and to pave the way for an ultimate merging of `nodedialer` with
`rpc` as well as adoption of the `util/circuit` package (async-based
circuit breaker).

`rpc.Context` hadn't aged well. Back in the day, it was a connection
pool that held on to connections even when they failed. The heartbeat
loop would run forever and its latest outcome would reflect the health
of the connection. We relied on gRPC to reconnect the transport as
necessary.

At some point we realized that leaving the connection management to
gRPC could cause correctness issues. For example, if a node is de-
commissioned and brought up again, gRPC might reconnect to it but
now we have a connection that claims to be for node X but is actually
for node Y. Similarly, we want to be able to vet that the remote
node's cluster version is compatible with ours before letting any
messages cross the connection.

To achieve this, we added `onlyOnceDialer` - a dialer that fails
all but the first attempt to actually connect, and in particular
from that point on connections were never long lived once they
hit a failure state.

Still, the code and testing around the heartbeat loop continued
to nurture this illusion. I found that quite unappealing as it
was sure to throw off whoever would ultimately work on this code.

So, while my original impetus was to produce better log messages
from `rpc.Context` when there were connection issues, I took
the opportunity to simplify the architecture of the code to
reflect what it actually does.

In doing so, a few heartbeat-related metrics were removed, as they made
limited sense in a world where failing connections get torn down (i.e.
our world).

Connection state logging is now a lot nicer. Previously, one would very
frequently see the onlyOnceDialer's error "cannot reuse client
connection" which, if one is not familar with the concept of the
onlyOnceDialer is completely opaque, and for those few in the know is an
unhelpful error - you wanted the error that occurred during dialing.

I paid special attention to the "failfast" behavior. If connections
don't stay in the pool when they are unhealthy, what prevents us from
dialing down nodes in a tight loop? I realized that we got lucky with
our use of onlyOnceDialer because it would always prompt gRPC to do
one retry, and at a 1s backoff. So, the connection would stay in the
pool for at least a second, meaning that this was the maximum frequency
at which we'd try to connect to a down node.

My cleanups to onlyOnceDialer in pursuit of better logging elimitated
this (desirable) property. Instead we now skip the log messages should
they become too frequent. I claim that this is acceptable for now since
the vast majority of callers go through a `node.Diaelr`, which has a
circuit breaker (letting callers through at most once per second).

We previously configured gRPC with a 20s dial timeout. That means that
if a remote is unreachable, we'd spend 20s just trying to dial it,
possibly tying up callers that could be trying a reachable node in the
meantime. That seemed wildly too large; I am reducing it to 5s here
which is still generous (but there's a TLS handshake in here so better
not make it too tight).

We previously tried to re-use connections that were keyed with a NodeID
for dial attempts that didn't provide a NodeID. This caused some issues
over the years and was now removed; the extra RPC connections are
unlikely to cause any issues.

The internal connection map is now a plain map with an RWMutex. This is
just easier and gets the job done. The code has simplified as a result
and it's clearer that it's correct (which it repeatedly was not in the
past).

I implemented redactability for gRPC's `status.Status`-style errors,
so they format nicer and at least we get to see the error code (the
error message is already flattened when gRPC hands us the error,
sadly).

There are various other improvements to errors and formatting. The
following are excerpts from the health channel when shutting down
another node in a local cluster:

Connection is first established:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 3  connection is now ready

n1 goes down, i.e. existing connection is interrupted (this error comes
from `onlyOnceDialer`):

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 35  closing
connection after: ‹rpc error: code = Unavailable desc = connection
error: desc = "transport: Error while dialing connection interrupted
(did the remote node shut down or are there networking issues?)"›

Reconnection attempts; these logs are spaced 1-2s apart:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 37  unable to
connect (is the peer up and reachable?): initial connection heartbeat
failed: ‹rpc error: code = Unavailable desc = connection error: desc =
"transport: Error while dialing dial tcp 127.0.0.1:26257: connect:
connection refused"›

n3 is back up:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 49  connection is now ready

There are other connection errors in the logs that stem from operations
checking for a healthy connection, failing to get through circuit
breakers, etc., such as these:

> [n3,intExec=‹claim-jobs›,range-lookup=/Table/15/4/‹NULL›] 33  unable
to connect to n1: failed to check for ready connection to n1 at
‹127.0.0.1:26257›: ‹connection not ready: TRANSIENT_FAILURE›

Release note (general change): Previously, CockroachDB employed a 20s
connection timeout for cluster-internal connections between nodes.  This
has been reduced to 5s to potentially reduce the impact of network
issues.

Release note (general change): Previously, CockroachDB (mostly) shared a
TCP connection for the KV and Gossip subsystems. They now use their own
connection each, so the total number of outgoing and incoming TCP
connections at each node in the cluster will increase by 30 to 50
percent.

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[00d3780c38...](https://github.com/Huffie56/cmss13/commit/00d3780c382c704f24e5c6f24aa36d88d509b7ea)
#### Friday 2022-12-09 18:00:38 by carlarctg

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
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[ce39f048bf...](https://github.com/Huffie56/cmss13/commit/ce39f048bf5eb25e2a93d7355327ccacc0504b01)
#### Friday 2022-12-09 18:00:38 by carlarctg

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
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[9499a1542b...](https://github.com/mc-oofert/tgstation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Friday 2022-12-09 18:19:50 by itseasytosee

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
## [chickells/freeCodeCamp](https://github.com/chickells/freeCodeCamp)@[3135d2be5f...](https://github.com/chickells/freeCodeCamp/commit/3135d2be5f6ec8d874c883163d3dcc428784f1b2)
#### Friday 2022-12-09 18:21:14 by Chase

AT LEAST IT WORKS ON THE DESKTOP
fuck lol, oh well. it was def sick sitting on the
couch with the crew watching the Brazil v Croatia
game go into PK's with Brazil whiffing their last shot
to lose 4-2

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[58b61a17a7...](https://github.com/tgstation/tgstation/commit/58b61a17a78e90ea9da91351572abee9a4f93ccb)
#### Friday 2022-12-09 18:54:00 by Jacquerel

Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

---
## [HATBE/URLShortener](https://github.com/HATBE/URLShortener)@[3539fc29ea...](https://github.com/HATBE/URLShortener/commit/3539fc29eacd73f409fdc20defedde80c97997ec)
#### Friday 2022-12-09 19:31:54 by HATBE2113

refactor backend, a.k.a overcomplicating stuff, because i hate my life and have no hobbies

---
## [mehulshetty/zerOS](https://github.com/mehulshetty/zerOS)@[da1a2415d5...](https://github.com/mehulshetty/zerOS/commit/da1a2415d547364724395160e80c5811c880eaa5)
#### Friday 2022-12-09 20:08:11 by Mehul Shetty

It works it all works now I'm wheezing crying and snobbing and cackling, Id like to thank my parents my friend and my family for sticking with me throiugh this and of course my favorite and best professor in the world prof algozzzine for being supportive throughout and giving me the strength and courage to finsih this i can die peacefully now

---
## [InfoTeddy/VVVVVV](https://github.com/InfoTeddy/VVVVVV)@[86d90a1296...](https://github.com/InfoTeddy/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Friday 2022-12-09 20:22:49 by Misa

Add color support to Windows console output, properly

This adds color support to the output of the console on Windows. Now if
you're using Windows 10 build 1511 or later (I think it's build 1511
anyway; they added more VT sequence support in later versions), you will
see colors by default. This isn't due to Windows helping in any way;
this commit has to specifically enable it with SetConsoleMode() because
by default, Windows won't enable color support unless we enable it. (Or
if it's enabled in the registry, but having to go through the registry
to enable basic shit like that is completely fucking stupid.)

I tested this in my Windows 10 virtual machine and it's completely
working.

---
## [peff/git](https://github.com/peff/git)@[e2ab31d90c...](https://github.com/peff/git/commit/e2ab31d90c866c8ac525b438c7c0e588916045ac)
#### Friday 2022-12-09 20:28:26 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[3dfeccbf27...](https://github.com/Floofies/Skyrat-tg/commit/3dfeccbf27b8dc53c97c2e9db0f1bdc4fd000ebe)
#### Friday 2022-12-09 20:36:27 by SkyratBot

[MIRROR] Clowns will now always like bananas. [MDB IGNORE] (#17300)

* Clowns will now always like bananas. (#70919)

## About The Pull Request
Clown's liver makes them like bananas, ignoring their racial food
preferences.

## Why It's Good For The Game
I don't think clown moths should vomit from eating bananas. They are
clowns, after all.
Also clowns are healed from eating them, so it's a bit silly that they
vomit from their funny medicine.

## Changelog

:cl:
balance: Non-human clowns enjoy eating bananas now.
/:cl:

* Clowns will now always like bananas.

Co-authored-by: Striders13 <53361823+Striders13@users.noreply.github.com>

---
## [Yotham/BestProfessorsList](https://github.com/Yotham/BestProfessorsList)@[7bf1cfada2...](https://github.com/Yotham/BestProfessorsList/commit/7bf1cfada2341f838f0ea30f2653df9d94bf6af0)
#### Friday 2022-12-09 20:53:21 by ifoster01

PAGINATION!!

It actually works holy shit that was annoying

---
## [Xx-Diego-XX-Agustin-xx-Garcia-xX/RubysAdventureGarcia2](https://github.com/Xx-Diego-XX-Agustin-xx-Garcia-xX/RubysAdventureGarcia2)@[9784927638...](https://github.com/Xx-Diego-XX-Agustin-xx-Garcia-xX/RubysAdventureGarcia2/commit/9784927638271a8405c16f38c8cae71ad7f72858)
#### Friday 2022-12-09 21:12:18 by Xx-Diego-XX-Agustin-xx-Garcia-xX

Ruby's Adventure

Creeper?
Aww, man
So we back in the mine
Got our pickaxe swinging from side to side
Side-side to side
This task, a grueling one
Hope to find some diamonds tonight, night, night
Diamonds tonight
Heads up
You hear a sound, turn around and look up
Total shock fills your body
Oh, no, it's you again
I can never forget those eyes, eyes, eyes
Eyes-eye-eyes
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
'Cause, baby, tonight
You grab your pick, shovel, and bolt again
And run, run until it's done, done
Until the sun comes up in the morning
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
Just when you think you're safe
Overhear some hissing from right behind
Right-right behind
That's a nice life you have
Shame it's gotta end at this time, time, time
Time-time-time-time
Blows up
Then your health bar drops and you could use a one-up
Get inside, don't be tardy
So, now you're stuck in there
Half a heart is left, but don't die, die, die
Die-die-die
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
'Cause, baby, tonight
You grab your pick, shovel, and bolt again
And run, run until it's done, done
Until the sun comes up in the morning
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
Dig up diamonds and craft those diamonds
And make some armor, get it, baby
Go and forge that like you so MLG pro
The sword's made of diamonds, so come at me, bro, huh
Training in your room under the torchlight
Hone that form to get you ready for the big fight
Every single day and the whole night
Creeper's out prowlin', hoo, alright
Look at me, look at you
Take my revenge, that's what I'm gonna do
I'm a warrior, baby, what else is new?
And my blade's gonna tear through you, bring it
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
(Gather your stuff, yeah, let's take back the world)
Yeah, baby, tonight
Grab your sword, armor and go (it's on)
Take your revenge (whoa), oh-oh, oh-oh
So fight, fight, like it's the last, last night
Of your life, life, show them your bite (whoa)
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
'Cause, baby, tonight
You grab your pick, shovel and bolt again
And run, run until it's done, done
Until the sun comes up in the morn'
'Cause, baby, tonight (c'mon, swing your sword up high, c'mon)
The creeper's tryna steal all our stuff again (swing your sword up, oh)

---
## [Woomymy/dotfiles-laptop](https://github.com/Woomymy/dotfiles-laptop)@[724aee8399...](https://github.com/Woomymy/dotfiles-laptop/commit/724aee8399da24861b245c7bc576d49c94e00b4a)
#### Friday 2022-12-09 21:15:59 by Woomymy

kernel/video: Drop nouveau

NVIDIA, fuck you

Signed-off-by: Woomymy <github@woomy.ovh>

---
## [austin-mroz/stk](https://github.com/austin-mroz/stk)@[6d214ca325...](https://github.com/austin-mroz/stk/commit/6d214ca3256e019abec63393303ace48eab59bf2)
#### Friday 2022-12-09 21:26:04 by Lukas Turcani

Add with_ids() (#364)

A type error has been discovered!

```python

a = stk.Alcohol(
    oxygen=stk.O(0),
    hydrogen=stk.H(1),
    atom=stk.C(2),
    bonders=(stk.C(2), ),
    deleters=(stk.O(0), stk.H(1)),
)

clone = a.with_atoms({
    0: stk.C(0),
})

# "oxygen" is actually a carbon!
oxygen = clone.get_oxygen()

```

The solution to this type error is to make the return type of
`with_atoms()` to return either `FunctionalGroup` or
`GenericFuncitonalGroup` as appropriate, but not the most derived type.

However, this is a problem because during construction, we need to make
clones, with different atom ids, but we also need to preserve the most
derived type, because this information may be used by reaction
factories to select an appropriate reaction.  For example, you might
want a specific bond order between alcohol and carboxylic acid
functional groups.

To get around this, I'm adding `with_ids`, it's just like`with_atoms`
except it only lets you change atom ids but not atom types. This means
that the most derived type can be returned. Internal use of
`with_atoms` has been replaced by `with_ids` so that the most derived
type can be preserved.

I am also adding `Bond.with_ids` so that you can use the same `dict`
when using `FunctionalGroup.with_ids` for bonds as well. Otherwise the
user would have to create an id map for the functional groups but an
atom map for bonds, and that's kind of annoying.

Other code changes:

* `src/stk/molecular/functional_groups/.../functional_group.py:260`: I
removed the `_with_atoms` method and replaced it with a new
implementation of `with_atoms`. The new implementation does not return
a clone of the most derived type, instead it always returns a
`FunctionalGroup` instance.
* `src/stk/molecular/.../generic_functional_group.py:63` Replaced the
`_with_atoms` implementation with an implementation of `with_atoms`,
which always returns a `GenericFunctionalGroup` instance.
* `src/stk/molecular/molecules/building_block.py:692`:  Here I removed
the use of `with_atoms` and did not replace it with `with_ids`.
`with_atoms` was being used here to minimize memory usage. I.e. the
functional groups held internally by the building block held the atoms
from `self._atoms`, rather than the atoms the user provided. This means
that the atoms which the user created / provided could be garbage
collected. Because `with_atoms` loses the most derived type, it can no
longer be used here and there is no way to replace its use here with
`with_ids`.
* `src/stk/.../placements_summary/atom_batch.py:45`: I replaced the use
of internal lists with internal tuples, just so that the immutability
is a bit more clear. The downside is an extra iteration, but
immutability is more important in my opinion.

---
## [wfleming/advent-of-code](https://github.com/wfleming/advent-of-code)@[cf6cf601a2...](https://github.com/wfleming/advent-of-code/commit/cf6cf601a25ef8b91b0529fd2c03cf576b761843)
#### Friday 2022-12-09 21:31:35 by Will Fleming

Remove most input files

Recent reddit discussion: https://www.reddit.com/r/adventofcode/comments/zh2hk0/2022friendly_reminder_dont_commit_your_input/

I had always thought the request for this was just "don't collect many
inputs in one public place for people", but a comment on that thread[1]
does cite a tweet by Eric making it clearer that he would prefer people
just not publish their inputs in general. Doesn't seem like he feels
*that* strongly, and seems pretty fine with people sharing inputs a bit
on places like the subreddit to help people work through their bugs, but
I want to be respectful of his wishes so I'm removing mine.

I am, however, opting to disregard the request on the genre of puzzle
where human interpretation of the input is necessary. I.e. a few times
there have been puzzles where the input is some wildly inefficient
assembler program and the way to get the answer is to figure out what
the program is actually doing and then implement that logic efficiently.

I think half the fun of AOC is the community sharing their approaches &
solution approaches. For most puzzles, reading the puzzle & somebody's
code is enough to grok that, but for these kinds of puzzles the critical
step is the human reading the assembler and writing down what it's
doing, and so not sharing the input with the notes on what it's doing is
hiding the only part of the solution that's really worth sharing IMHO.
This is only a handful of puzzles, and as mentioned above it doesn't
seem like Eric's stance on this is too aggressive, so hopefully this is
a reasonable position to take.

I am also not going to the trouble of rewriting history here: if anyone
stumbles across this repo and reads the history, they'll find the
inputs. Again, my read of Eric's requests is to try to avoid making a
bunch of inputs easily discoverable, so I think just removing them
moving forward does that sufficiently.

[1]: https://www.reddit.com/r/adventofcode/comments/zh2hk0/2022friendly_reminder_dont_commit_your_input/izka2wk/

---
## [alexandru-duca/chess-openings](https://github.com/alexandru-duca/chess-openings)@[9f7632e84e...](https://github.com/alexandru-duca/chess-openings/commit/9f7632e84ebf35b79b8d3c08af9b95943cc54e59)
#### Friday 2022-12-09 21:39:18 by Alexandru Duca

Scandinavian Defense: Portuguese Gambit

- Removed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. f3 Bf5` named `Scandinavian Defense: Portuguese Variation, Portuguese Gambit`.
- Renamed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` from `Scandinavian Defense: Portuguese Variation` to `Scandinavian Defense: Portuguese Gambit`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` named `Scandinavian Defense: Portuguese Gambit, Banker Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` named `Scandinavian Defense: Portuguese Gambit, Classical Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` named `Scandinavian Defense: Portuguese Gambit, Correspondence Refutation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` named `Scandinavian Defense: Portuguese Gambit, Elbow Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` named `Scandinavian Defense: Portuguese Gambit, Jadoul Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` named `Scandinavian Defense: Portuguese Gambit, Lusophobe Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` named `Scandinavian Defense: Portuguese Gambit, Melbourne Shuffle Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` named `Scandinavian Defense: Portuguese Gambit, Wuss Variation`.

This line `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` in the Scandinavian Defense has many different names across chess literature. Selby Anderson released the book [Center Counter Defense: The Portuguese Variation](https://www.amazon.com/Center-Counter-Defense-Portuguese-Variation/dp/1886846103) in the year 1997 and, apparently, named it `Portuguese Variation`. In his book [Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943), [David Smerdon](https://en.wikipedia.org/wiki/David_Smerdon) called this line `Portuguese Complex`, but he noted that it was also called `Portuguese Opening` as well as `Jadoul Variation` [Section 1]. It's called `Portuguese Gambit` in Wikipedia's [list of chess gambits](https://en.wikipedia.org/wiki/List_of_chess_gambits#Scandinavian_Defense) and `Portuguese Variation` as well as `Jadoul Variation` in Wikipedia's article on the [Scandinavian Defense](https://en.wikipedia.org/wiki/Scandinavian_Defense#2...Nf6). (Unfortunately, I was unable to check the sources Wikipedia provides because I couldn't find the referenced books.)

Since Selby Anderson's book predates all other sources, there is an argument to name this line `Portuguese Variation`. However, Black delays taking back the pawn on d5 twice (first time with `2... Nf6` and second time with `3... Bg4`). This gives White the opportunity to secure the extra pawn with e.g. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4 Bg6 6. c4`. Additionally, Selby Anderson may not have been aware of the dubious nature of this variation ([Stockfish gives White +0.8](https://lichess.org/7CAhQOCs)). Furthermore, David Smerdon repeatedly refers to this line as a gambit despite calling it `Portuguese Complex`. Because of this, I argue that this line should be called the `Portuguese Gambit`.

[Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943) is currently the most extensive book on the `Portuguese Gambit`. It categorizes all major responses from White after `1. e4 d5 2. exd5 Nf6 3. d4 Bg4`. Smerdon also offers creative names for all variations covered by his theory. Here are the variations sorted by chapter:
1. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` is called `The Banker`. (White "banks" the extra pawn with the immediate `5. c4`.)
2. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` is called `The Jadoul`. (Named after [Michel Jadoul](https://de.wikipedia.org/wiki/Michel_Jadoul) who is one of the earliest exponents of the Portuguese Gambit [Introduction, Inspirational Game #1].)
3. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` is called `The Melbourne Shuffle`. (Played by many australian IMs from Melbourne [Chapter 3]. It is named after a [rave dance](https://en.wikipedia.org/wiki/Melbourne_shuffle) which originated in Melbourne.)
4. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` is called `The Correspondence Refutation`. (A line against the `Portuguese Gambit` successfully employed the correspondence community [Chapter 4].)
5. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` is called `The Wuss`. (Apparently, `4. Be2` is a wimpy move and only a [wuss](https://www.merriam-webster.com/dictionary/wuss) would play it.)
6. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` is called `The Lusophobe`. (According to Wikipedia, [Lusophobia](https://en.wikipedia.org/wiki/Lusophobia) is irrational hostility, racism or hatred towards Portugal, the Portuguese people or the Portuguese language and culture. David Smerdon is making a joke by referring to the line `4. Bb5+ Nbd7 5. Be2` as "Anti-Portuguese" or "effective against the Portuguese Gambit".)
7. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` is called `The Elbow`. (Given the effectivness of the line `4. Bb5+ Nbd7 5. Be2`, occasionally playing `4... c6` may discourage players from studying it while preparing against you. Playing `4... c6` is a metaphor for hitting your well prepared opponent with your elbow [Chapter 7].)
8. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` is called `The Classical`. (Refers to the fact that the move `4. Nf3` is principled [Chapter 8].)

---
## [yoshimo/Grail](https://github.com/yoshimo/Grail)@[4df80ca4cf...](https://github.com/yoshimo/Grail/commit/4df80ca4cf84636fb32cd7c838cedd681f9985af)
#### Friday 2022-12-09 21:52:14 by Yoshimo

The Waking Shores:
- Picture Perfect (65486) requires Pictures with Purpose (69870)
- Black Wagon Flight (65793) requires Claimant to the Throne (66780)
- The Courage of One's Convictions (65939) requires Talon Strike (65956)
- Obsidian Oathstone (66049) doesn't require The Courage of One's Convictions (65939)
- Forging a New Future (66056) requires The Courage of One's Convictions (65939)

Ohn'aran Plaines:
- Toward the City (65803) requires Making Introductions (65801)
- By Broken Road (65940) requires For Food and Rivalry (65804)
- Covering Their Tails (66024) requires The Khanam Matra (66022)
- The Nokhud Threat (66025) requires Trucebreakers (66023)
- Catching Wind (66236) requires Toting Totems (66225)
- Oh No, Ohn'ahra! (66258) requires Eagle-itarian (66256)
- Stormbreaker (66337) requires Deconstruct Additional Pylons (66335)
- Clans of the Plains (66969) requires Honoring Our Ancestors (66019)
- The Hunting Hound (67921) requires The Trouble with Taivan (67772)
- Try Again, Taivan! (68083) requires Part of a Pack (70989
- The Gentle Giant (68084) requires Try Again, Taivan! (68083)
- Shaping a Shepherd (68085) requires The Gentle Giant (68084)
- Danger in Daruukhan (68087) requires Reign of the Ram (71022)
- Saving Centaur (69094) requires Danger in Daruukhan (68087)
- Homeward Hound (69095) requires Saving Centaur (69094)
- Taivan's Purpose (69096) requires Homeward Hound (69095)
- Part of a Pack (70989) requires The Hunting Hound (67921)
- Reign of the Ram (71022) requires Shaping a Shepherd (68085)

The Azure Span:
- Tome-ward Bound (65848) requires Cut Out the Rot (65844)
- Straight to the Top (65852) requires Driven Mad (65702)
- Reclaiming the Oathstone (65854) requires Platform Adjustments (65751)
- Supplies! (65870) requires Snap the Traps (65866)
- Gnoll Way Out (65871) requires Snap the Traps (65866)
- Ill Gnolls with Ill Intent (65872) requires Snap the Traps (65866)
- Leader of the Shadepaw Pack (65873) requires Snap the Traps (65866)
- Kirin Tor Recovery (65977) requires Lava Burst (65944)
- Free Air (66007) requires Primal Power (65958)
- Can We Keep It? (66223) seems to require Scampering Scamps (66218)
- Spreading Decay (66239) requires Gnoll Way Out (65871)
- Setting the Defense (66489) seems to require WANTED: Frigellus (66488)
- Ways of Seeing (66500) requires Suspiciously Quiet (69904)
- For The Love of Others (66503) seems to require Ways of Seeing (66500)
- Assemble the Defenses (67033) requires The Azure Wizard (70747) for Dracthyr
- Preservation of Knowledge (67035) requires The Azure Wizard (70747) for Dracthyr
- How To Stop An Exploding Toy Boat (67175) requires Arcane Detection (67174)
- Needles to Say (68642) requires Mossing the Mark (68641) , might require Prowling Polar Predators (68639)
- Vitamins and Minerals (68643) requires Mossing the Mark (68641) , might require Prowling Polar Predators (68639)
- Sugar, Spice, and Everything Nice (68644) requires Vitamins and Minerals (68643) , might require Needles to Say (68642)
- Save a Slyvern (69862) requires Sugar, Spice, and Everything Nice (68644)
- Toejam the Terrible (70129) requires Rowie (66558)
- Sad Little Accidents (70168) seems to require The Joy of Painting (70166)
- They Took the Kits (70338) requires Save a Slyvern (69862)
- The Azure Wizard (70747) requires Shades of Blue (70746)
- For Blue Eyes Only (70748) requires Wayward Archivists (71182)
- A Claw in Need (71095) requires Help Is Our Way! (71094)
- Is A Claw Indeed (71096) requires A Claw in Need (71095)
- A Helping Claw (71097) requires Is A Claw Indeed (71096)
- Setting Your Very Own Net (72584) seems to require <NONAME> (70793) and Iskaaran Fishing Net (70871)

Thaldraszus:
- The Once and Future Team (65938) requires Quelling Causalities (66646)
- Return to the Present (66032) requires Resistance Isn't Futile (66030)
- To the... Past? (66033) doesn't require Temporal Two-ning (72519)
- Back to Reality (66037) seems to require Deathwingurlugull! (70371) for the Horde
- Feels Like the First Time (66083) requires Time is Running Out (66081)
- Closing Time (66087) requires Times Like These (66084)
- Southern Exposure (66167) requires Nowhere to Hide (66163)
- Remember the Fallen (66245) requires Vengeance, Served Hot (66169)
- Slightly Used Weapons (66247) requires Vengeance, Served Hot (66169)
- Tying Things Together (66248) requires Vengeance, Served Hot (66169)
- Clear the Sky (66249) requires Slightly Used Weapons (66247)
- Rebels With a Cause (70838) requires Follow the Clues (70837)
- Detonation Locations (70842) requires Follow the Clues (70837)
- Maldra's in Hot Water (70850) requires Ruin the Runestones (70843) , may require Rebels With a Cause (70838) & Detonation Locations (70842)
- Chasing Waterfalls (70873) requires Maldra's in Hot Water (70850)
- To Breach a Fire Wall (70874) requires Chasing Waterfalls (70873)
- Worst of the Worst (70875) requires To Breach a Fire Wall (70874)
- Fracture the Foci (70876) requires To Breach a Fire Wall (70874)
- Ring of Fire (70878) requires To Breach a Fire Wall (70874)
- Report on the Rebels (70879)  requires Ring of Fire (70878) , may require Worst of the Worst (70875) & Fracture the Foci (70876)

Azmerloth:
- Deathwingurlugull! (70371) requires Murloc Motes (66035) , seems to require Mugurlglrlgl! (66704)

Professions:
- The Wonders of the World (67298) requires That's My Specialty (67295)
- The Master of Their Craft (69946) requires That's My Specialty (67295)

---
## [ginalamka/ComplexModel_ABM](https://github.com/ginalamka/ComplexModel_ABM)@[0f0eb16826...](https://github.com/ginalamka/ComplexModel_ABM/commit/0f0eb16826934fce917b5ae536a0d908551eff4a)
#### Friday 2022-12-09 22:43:20 by ginalamka

Update RunModel.R

added migSNPs to pop and source AND the proportion of migrant SNPs represented in the indv in the pop matrix.. edited break/next checks to add Analyze.R so that it doesn't keep skipping it. hopefully this is a solution and won't fuck anything up by putting a function in multiple times!

today is the last day of the Fall 2022 semester! I will be taking my end of semester photo on Monday after my end of semester meeting.

This semester was ROUGH, 100% due to my personal life, but unfortunately this ABM is moving slowly because of it. that is ok though. some balls will always be dropped. I'm still proud of you (aka me <3)

---
## [i3roly/CMI8788](https://github.com/i3roly/CMI8788)@[24faeb6609...](https://github.com/i3roly/CMI8788/commit/24faeb660939bbaad8879aa96ead97b3b465cf8c)
#### Friday 2022-12-09 23:32:48 by gagan sidhu

fix dac_routing_call which is in the audioEngine, and not PCIAudioDevice *CLASS*

once you read the docs (https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingAudioDrivers/ImplementDriver/ImplementDriver.html), you're like

"wow, this paradigm is so cool!"

you then realise

"damn i doubt anyone will use it since it's such a small target audience compared to windows"

and counter with

"wow if someone actually implements a driver in this radical paradigm, it would make alsa look primitive"

but OF COURSE dude dies, company goes on cruise control and then we get tim "i can ruin autopilot" cook deciding it's time to cut spending and just deprecate everything and use shittier paradigms.

cheap doesn't even begin how ol' timmy decided mobile processors are the future--as if the margin on mobile phone sales isn't enough--all because talentless hack "musicians" and hollywood wanna dump on H1Bagholders

fucking idiot.

---

