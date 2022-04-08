## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-07](docs/good-messages/2022/2022-04-07.md)


1,827,948 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,827,948 were push events containing 2,967,540 commit messages that amount to 203,179,774 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[c8ef62c1fb...](https://github.com/ZephyrTFA/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Thursday 2022-04-07 00:03:06 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

---
## [jadarling/Reed-College-CSCI](https://github.com/jadarling/Reed-College-CSCI)@[0865bf2593...](https://github.com/jadarling/Reed-College-CSCI/commit/0865bf2593d27a9ae8d7afe1cf40582aa0010908)
#### Thursday 2022-04-07 00:30:33 by Jackson Darling

Started MP3

Holy shit dude i am actually done
This is It my love for CS has been killed by the field itself thats so cool.

---
## [KeatonRozema2004/Bot-Track-GUI](https://github.com/KeatonRozema2004/Bot-Track-GUI)@[886940cffc...](https://github.com/KeatonRozema2004/Bot-Track-GUI/commit/886940cffc52c48bd6ae97d6902c925017f7830a)
#### Thursday 2022-04-07 00:32:25 by ryan-veersma

04-06-22 Ryan Veersma

OH GOD IT WORKS SOME WHAT
lol sorry had to make a joke :smile:

---
## [perfectly-preserved-pie/rejectedplates](https://github.com/perfectly-preserved-pie/rejectedplates)@[f8e3bd0101...](https://github.com/perfectly-preserved-pie/rejectedplates/commit/f8e3bd0101477fbca89282c824c8dcb9d899f447)
#### Thursday 2022-04-07 00:41:40 by Sahib Bhai

Don't use Twitter's timeline API to get the last known tweet... do it manually... fuck you twitter API limits

---
## [Tokorizo/Skyrat-tg](https://github.com/Tokorizo/Skyrat-tg)@[b995fbe31b...](https://github.com/Tokorizo/Skyrat-tg/commit/b995fbe31b87402d3da2f8e98cec1f5659e52a47)
#### Thursday 2022-04-07 00:42:06 by Zonespace

Contractor Expansion 2 (#12311)

* weh!

* fuck you linter

* very important

* Update modular_skyrat/modules/contractor/code/datums/midround/event.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* Update modular_skyrat/modules/contractor/code/datums/midround/outfit.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* requested changes

* also this

* requested + cleanup

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [Dieterdemuynck/OGP-Practica-2022](https://github.com/Dieterdemuynck/OGP-Practica-2022)@[99d97d1d54...](https://github.com/Dieterdemuynck/OGP-Practica-2022/commit/99d97d1d54f0e1143959b087539c04f5864afc19)
#### Thursday 2022-04-07 00:42:17 by Dieter Demuynck

Basis for Link and Directory + Expansion of Item for Directory

This is bad dumb code that is stupid and terrible just like my ability to concentrate on this horrendous, horrible, awful programming language.
I truly have become a Java hater. May it burn in hell. I'm tired. I want a hug :c

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[cd2bd18cf8...](https://github.com/Zonespace27/Skyrat-tg/commit/cd2bd18cf8193c7cfc2f0014ef449baa8792aad4)
#### Thursday 2022-04-07 00:54:02 by SkyratBot

[MIRROR] Creates Linters for (bad) Commented Out Lines in Maps [MDB IGNORE] (#12543)

* Creates Linters for (bad) Commented Out Lines in Maps (#65888)

* Creates CI Linters for Commented Out Lines in Maps

Creates Linters for (bad) Commented Out Lines in Maps

Hey there,

This PR is made because what happened in #65837 was fucking horrible awful shit that I'm still dealing with a few days after I fixed it. This _should hopefully_ add a new linter for commented out lines of code in a .DMM file, and HOPEFULLY doesn't flag the commented line that prevents unwanted TGM > DMM conversion.

As a proof to see if it works, I'll be adding a comment to Line 2 of IcemoonUnderground_Above.dmm. Hopefully, on the first CI check, it'll fail. I'll remove that line so it doesn't make its way into production (it will suck).

* Creates Linters for (bad) Commented Out Lines in Maps

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[54403a1ca0...](https://github.com/TheBoondock/tgstation/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Thursday 2022-04-07 01:15:24 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [newstools/2022-naija-news-agency](https://github.com/newstools/2022-naija-news-agency)@[d56ca64b69...](https://github.com/newstools/2022-naija-news-agency/commit/d56ca64b694cb2cd9adce7bb623cf4ba311a66ac)
#### Thursday 2022-04-07 01:16:50 by Billy Einkamerer

Created Text For URL [www.naijanewsagency.com/little-girl-tearfully-accuses-her-family-of-not-being-holy-because-they-dont-go-to-church/]

---
## [ozzono/scripts](https://github.com/ozzono/scripts)@[e75f6d6234...](https://github.com/ozzono/scripts/commit/e75f6d6234b330270b0222fa64fdd02d5d96e77e)
#### Thursday 2022-04-07 01:17:25 by Hugo Virgilio

Fortune Commit: 	Young men and young women may work systematically six days in the
week and rise fresh in the morning, but let them attend modern dances for
only a few hours each evening and see what happens.  The Waltz, Polka,
Gallop and other dances of the same kind will be disastrous in their effects
to both sexes.  Health and vigor will vanish like the dew before the sun.
	It is not the extraordinary exercise which harms the dancer, but
rather the coming into close contact with the opposite sex.  It is the
fury of lust craving incessantly for more pleasure that undermines the
soul, the body, the sinews and nerves.  Experience and statistics show
beyond doubt that passionate excessive dancing girls can hardly reach
twenty-five years of age and men thirty-one.  Even if they reached that
age they will in most instances be broken in health physically and morally.
This is the claim of prominent physicians in this country.
		-- Quote from a 1910 periodical

---
## [pdx-tools/pdx-tools](https://github.com/pdx-tools/pdx-tools)@[e1056e4630...](https://github.com/pdx-tools/pdx-tools/commit/e1056e4630945a0ab164bde55050753d823d624a)
#### Thursday 2022-04-07 01:24:16 by Nick Babcock

Allow recording map timelapse into a video

This feature allows users to capture a timelapse into a video recording
to download and share. This implemented at a high level by using a
[canvas's `captureStream`][2] and piping that to a [`MediaRecorder`][3].

Users may choose what resolution to render the map as well as the how
fast the timelapse progresses.

Conceptually simple, but several problems arose.

Capturing the map's canvas omits UI elements like the current date in a
timelapse, something that seems critical when evaluating a timelapse. To
embed a date in the recording, we'd need to either send text into the
map or we could copy the map's canvas into a separate canvas that uses
the 2d api, which has better support for text and we could record that
one instead. While copying around map canvas data seems inefficient, it
was deemed better than needing to figure how to embed rapidly updating
text into WebGL. To support the copy use case the webgl map exposes a
callback (`onCommit`) right after it has rendered so the recording
canvas can copy it hot off the press.

Since users will want the option to record the entire map, the recording
logic communicates to the canvas that it'll be assuming control of the
size of the canvas. Seeing the canvas expand beyond one's viewport may
be unsightly, but it was the most intuitive way to get the resolution
necessary for the recording. The good news is that we restore the map
state when the recording is done so the user's focus point and scale
will not have changed.

The hardest part about the implemenation is all the coordination between
updating the map, progressing the timelapse, and making sure that
recording captures both the start and tail end of the timelapse.

For instance, there are some variations in browser implementations of a
canvas's capture stream and the media recorder. The biggest one is that
chrome would cut several seconds out of a recording especially when
there was a lack of data (like when using a freeze frame at the end).
The solution is extremely hacky: when the recording stops, repeatedly
write a transparent rectangle until we the media recorder emit non-empty
data.

That same technique (writing transparent data) is used to synchronize
the start of the recording with the start of the timelapse.

Another variation is that Chrome's canvas stream needed to be updated
every 250ms or it wouldn't register any changes. This is why the minimum
intervals per second is 4.

The output of a recording is a webm file. While this format is the [
recommended approach for video playback][4], webm upload is not often
supported sites like reddit. The solution is that after the recording is
finished, transcode it into an mp4 file using [`ffmpeg.wasm`][5]. This
is a pretty extreme approach as ffmpeg is a large download (several
times larger than all the pdx.tools wasm bundles put together), and may
take several minutes to complete while using 100% CPU usage. But the end
result is worth it if users can take the download and immediately upload
it elsewhere with minimal hassle.

However I still view the mp4 export as a bit experimental as every few
recordings ffmpeg takes 10x as long to process the input and the output
is horribly choppy. I'm not sure what causes this, but I'm assuming
other users will experience this issue, so my recommendation to those
who constantly experience it is to accept the webm output and convert it
to mp4 through a 3rd party tool.

Needed to add two new headers: `Cross-Origin-Embedder-Policy:
require-corp` and `Cross-Origin-Opener-Policy: same-origin` in order to
get [ffmpeg.wasm to work][0] as it relies on `SharedArrayBuffer` and its
[security requirements][1]

The timelapse and recording work through `requestAnimationFrame` which
is paused when running in a background tab ([source][6]), so in order to
avoid corrupting the canvas capture, a warning is presented to the user
when they switch back to our tab (as one can't eagerly detect tab
switching in the browser beforehand), informing them of this
restriction. At least the MP4 transcoding can happen in the background.

[0]: https://github.com/ffmpegwasm/ffmpeg.wasm#installation
[1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer#security_requirements
[2]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream
[3]: https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder
[4]: https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Video_codecs#recommendations_for_everyday_videos
[5]: https://github.com/ffmpegwasm/ffmpeg.wasm
[6]: https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame

---
## [magatsuchi/tgstation](https://github.com/magatsuchi/tgstation)@[e58fb506ef...](https://github.com/magatsuchi/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Thursday 2022-04-07 02:03:33 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [garyleecummins/surge](https://github.com/garyleecummins/surge)@[e6f4ffaef9...](https://github.com/garyleecummins/surge/commit/e6f4ffaef9d6f3222749fcf0d86a37063130a36e)
#### Thursday 2022-04-07 02:39:30 by Paul

Doubleclick Renamed Modulators without annoying bug (#6024)

Doubleclick renames a modulator. Cool

But this kinda sucks if you click into a modulator and then click to arm
quickly and misfire a double click

So if you have *just* selected a modulator the double click doesn't work.

Only after that

Closes #5774

---
## [tellowkrinkle/pcsx2](https://github.com/tellowkrinkle/pcsx2)@[89f10e1605...](https://github.com/tellowkrinkle/pcsx2/commit/89f10e160572063b4871bfb8d0c6ffff54f9543a)
#### Thursday 2022-04-07 03:23:43 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [blessedcoolant/lama-cleaner](https://github.com/blessedcoolant/lama-cleaner)@[eea85b834e...](https://github.com/blessedcoolant/lama-cleaner/commit/eea85b834eee527f3a05fca9410e671c935603b2)
#### Thursday 2022-04-07 03:49:20 by blessedcoolant

Complete GUI Refactor

This patch brings in a massive number of changes to the frontend of the application. Please feel free to discuss the proposed changes with me at any time.

Implemented Recoil as a state management system.
Why Recoil? It is a robust library built by developers at Facebook for state management. It has an  extremely simple API for implementation that is in sync with React syntax compared to any other state management system out there and works amazingly well. While the official release status is beta as it becomes fully featured, the library is already used in various systems at Facebook and is very stable for the use cases of this application.

Why global state management? One of the major issues I saw with the current file structure is that there is minimal code splitting and it makes further development of the frontend a cumbersome task. I have broken down the frontend into various easy to access components isolating the GUI from the logic. To avoid prop drilling, we need global state management to handle the necessary tasks. This will also facilitate the addition of any new features greatly.

Code Splitting. Majority of the components that can be isolated in the application have now been done so.
All New Custom CSS & Removal of Tailwind
While Tailwind is a great way to deploy beautiful interfaces quickly, anyone trying to stylize the application further needs to be familiar with Tailwind which makes it harder for more people to work on it. Not to mention, I am not a particular fan of flooding JSX elements with inline CSS classes. That makes reading the code extremely hard and bloats up component code drastically.

As a replacement to Tailwind, I implemented a custom styling system using SCSS as a developer dependency.

In the new system, all the general and shared styles are in the styles folder and all the component styles are in the same folder as the component for easy access.The _index.scss file now acts as a central import for every other stylesheet that needs to be loaded.

What Changed?
The entire application looks and feels like the current implementation with minimal changes.
The green (#bdff01) highlight used in the application has now been changed to a bright yellow (rgb(255, 190, 0)) because I felt it better suited the new Dark Mode (see below).
The swipe bar for comparing before and after images has now been removed and instead the comparison is a smooth fade effect. I felt this was better to analyze image changes rather than a swiper. // Can add the swipe back if needed.

Dark Mode
A brand new Dark Mode has been added for the application. Users can enable and disable by tapping the button in the header or by using the Shift + D hotkey.

Other Misc New Features
When the editor image is now zoomed out to its default size, the image now also gets centered back.

TODO
The currently used react-zoom-pinch-pan module is not mobile friendly. It does not allow brush strokes. Need to figure out a way to fix this.
Further optimization of the frontend code with better code splitting and performance.
When using the LaMa model, the first stroke has a delayed response from the backend but the ones that follow are almost immediate. I believe this is happening because of the initialization of the model on the first stroke. I wonder if either of us can look at it and see if this can somehow be preloaded so the user experience is smooth from the first stroke.
Enable threading for the desktop application mode so flaskwebgui does not block the main applications Python console.

---
## [Inrlbots/inrl](https://github.com/Inrlbots/inrl)@[fdce3ea001...](https://github.com/Inrlbots/inrl/commit/fdce3ea0017a41eb71a8c52b85feb48d1a1959d8)
#### Thursday 2022-04-07 03:56:07 by Inrlbots

Delete EN.json

{
    "__ASENAJSON__": true,
    "LANGUAGE": "English",
    "LANGCODE": "en",
    "AUTHOR": "AsenaDev",
    "STRINGS": {
        "_asena": {
            "EXAMPLE": "Eg:- ",
            "NOT_FOUND": "*I couldnt find a command like this*",
            "PLKADMIN": ".report you are not admin \n\n 🇩​🇴​🇳​🇹​ 🇹​🇷​🇾​ 🇦​🇬​🇦​🇮​🇳​, 🇮​🇫​ 🇾​🇴​🇺​ 🇹​🇷​🇾​ 🇾​🇴​🇺​ 🇼​🇮​🇱​🇱​ 🇧​🇪​ 🇷​🇪​🇲​🇴​🇻​🇪​🇩​ 🇧​🇾​ 🇦​🇩​🇲​🇮​🇳​🇸​",
            "WARN": "Warn"
            
        },
        "_plugin": {
            "INSTALL_DESC": "Install external plugins.",
            "NEED_URL": "Please enter a URL! Example:",
            "UNOFF": "⚠️ *Attention!* \n*The plugin you have installed is not official!*",
            "INVALID_URL": "```Please enter a valid url!```",
            "INVALID_PLUGIN": "*❌ Your plugin is invalid!*\n*Error:*",
            "INSTALLED": "*✅ Plugin has been successfully installed!*",
            "PLUGIN_DESC": "Shows the plugins you have installed.",
            "INSTALLED_FROM_REMOTE": "*Plugins you install externally:*\n",
            "NO_PLUGIN": "*You have not installed any external plugins!*",
            "REMOVE_DESC": "Removes the plugin.",
            "NEED_PLUGIN": "```Please enter a Plugin! Example: .plugin __test```",
            "NOT_FOUND_PLUGIN": "```Maybe you have installed such a plugin, or maybe not. But it sure isn't right now.```",
            "DELETED": "*✅ Module successfully deleted!*",
            "WARN": "Get plugins only from t.me/remasterplugin channel."
        },
        "admin": {
            "BAN_DESC": "Ban someone in the group. Reply to message or tag a person to use command.",
            "IM_NOT_ADMIN": "*I am not admin in this group!*",
            "BANNED": "kicked out of the group!",
            "GIVE_ME_USER": "*Give me a user!*",
            "ADD_DESC": "Adds someone to the group.",
            "ADDED": "added to the group!",
            "ALREADY_PROMOTED": "```How can I make someone admin who is already admin?```",
            "PLKADMIN": ".report you are not admin \n\n 🇩​🇴​🇳​🇹​ 🇹​🇷​🇾​ 🇦​🇬​🇦​🇮​🇳​, 🇮​🇫​ 🇾​🇴​🇺​ 🇹​🇷​🇾​ 🇾​🇴​🇺​ 🇼​🇮​🇱​🇱​ 🇧​🇪​ 🇷​🇪​🇲​🇴​🇻​🇪​🇩​ 🇧​🇾​ 🇦​🇩​🇲​🇮​🇳​🇸​",
            "PROMOTED": "```, admin role was given!```",
            "PROMOTE_DESC": "Makes any person an admin.",
            "DEMOTE_DESC": "Takes the authority of any admin.",
            "ALREADY_NOT_ADMIN": "```How can I make someone admin who is already admin?```",
            "DEMOTED": "```, has been demoted!```",
            "MUTE_DESC": "Mute the group chat. Only the admins can send a message.\n⌨️ Example: .mute & .mute 5m etc",
            "MUTED": "```Group chat muted!```",
            "UNMUTE_DESC": "Unmute the group chat. Anyone can send a message.",
            "UNMUTED": "```The group chat has unmuted!```",
            "INVITE_DESC": "Provides the group's invitation link.",
            "INVITE": "```Invitation link: ```"
        },
        "locate": {
            "L_DESC": "It send your location.",
            "L_WARN": "Please open your location before using command!"
        },
        "news": {
            "NEWS_DESC": "It send News."
        },
        "afk": {
            "AFK_DESC": "It makes you AFK - Away From Keyboard.",
            "IM_AFK": "*I'm AFK now!*",
            "IM_AFK_NOMD": "I'm AFK now!",
            "REASON": "Reason",
            "LAST_SEEN": "Last Seen",
            "IM_NOT_AFK": "```I am not AFK anymore!```",
            "AFK_TEXT": "```Bip bop! This is a bot. My owner is not here at the moment.```",
            "AFK_TEXT_NOMD": "Bip bop! This is a bot.",
            "HOUR": "hour",
            "MINUTE": "minute",
            "SECOND": "second",
            "AGO": " ago```"
        },
        "evaluators": {
            "TERM_DESC": "Allows to run the command on the server's shell.",
            "GIVE_ME_CODE": "*Give me a code!*"
        },
        "nekobin": {
            "NEKO_DESC": "Replied messages will be added to nekobin.com.",
            "NEED_REPLY": "```Please reply to a message!```",
            "MUST_TEXT": "```Please reply to any message```"
        },
        "heroku": {
            "RESTART_DESC": "Restart Rudhra",
            "RESTART_MSG": "```Restarting...```",
            "SHUTDOWN_DESC": "Shutdown Bot",
            "SHUTDOWN_MSG": "```Appo Seri Tata📴```",
            "DYNO_DESC": "Check heroku dyno usage",
            "DYNO_TOTAL": "```Total Quota```",
            "DYNO_USED": "```Quota used```",
            "PERCENTAGE": "```Percentage```",
            "DYNO_LEFT": "```Remaining```",
            "GR_DEL": "*Greetings Message Set!*\n*Type* ```.goodbye delete & .welcome delete``` *to remove!*",
            "SETVAR_DESC": "Set heroku config var",
            "SET_SUCCESS": "Successfully set ```{} ➜ {}```",
            "KEY_VAL_MISSING": "```Either Key or Value is missing```",
            "INVALID": "```Invalid key:value format```",
            "GETVAR_DESC": "Get heroku config var",
            "DELVAR_DESC": "Delete heroku config var",
            "DEL_SUCCESS": "```{} successfully deleted```",
            "NOT_FOUND": "```no results found for this key```",
            "SUCC": "*Successfully Setted Up ✅* \n*Please wait a little while.*",
            "SUCC_AF": "*To restore, use* ```default```",
            "DEGİS_NONE": "```Please Enter Any Module Name!``` \n\n*.degis afk*\n*.degis alive* << **Variables** >> \n_{pp}: You only need to use it once. Adds your profile photo to the message._ \n_{info}: Shows your status._ \n_{version}: Shows the version of the bot._ \n_{plugin}: Shows the plugin channel._\n*.degis ban*\n*.degis add*\n*.degis mute*\n*.degis unmute*\n*.degis promote*\n*.degis demote*\n*.degis welcome* \n*.degis goodbye* \n*.degis kickme*\n*.degis block*\n*.degis unblock*",
            "WR": "*Please use the modules that exists!*",
            "DEGİS_DESC": "Changes the text of modules like alive, afk etc.."       
        },
        "filters": {
            "FILTER_DESC": "It adds a filter. If someone writes your filter, it send the answer. If you just write .filter, it show's your filter list.",
            "NO_FILTER": "*❌ There are no filters in this chat!*",
            "FILTERS": "*🔎 There is your filters in this chat:*",
            "NEED_REPLY": "*❌ Please type in reply!*\n*Example:*",
            "FILTERED": "*✅ Successfully set* ```{}``` *to filter!*",
            "STOP_DESC": "Stops the filter you added previously.",
            "NEED_FILTER": "*❌ Please type a filter!*\n*Example:*",
            "ALREADY_NO_FILTER": "*❌ There is already no filter like this!*",
            "DELETED": "*✅ The filter was successfully deleted!*"
        },
        "greetings": {
            "WELCOME_DESC": "It sets the welcome message. If you leave it blank it shows the welcome message.",
            "NOT_SET_WELCOME": "*You don't set the welcome message yet.!*\n**To set:** ```.welcome hi && hi#how are you? \n to add member mention use {mention} \n to add  group description in welcome message use {gpdesc} \n to add group name use {gphead} \n to add group maker name use {gpmaker} \n to add bot name use {owner} \n to add exact indian time use {time} ```",
            "WELCOME_ALREADY_SETTED": "*✅ Welcome message already set!*\n*Message:* ```",
            "NEED_WELCOME_TEXT": "*You must write a message to set up the welcome message.*\n*Example:* ```.welcome hi && hi#how are you?```",
            "WELCOME_DELETED": "*✅ Welcome message has been deleted successfully!*",
            "WELCOME_SETTED": "*✅ Welcome message has been set successfully!*",
            "PLKADMIN": ".report you are not admin \n\n 🇩​🇴​🇳​🇹​ 🇹​🇷​🇾​ 🇦​🇬​🇦​🇮​🇳​, 🇮​🇫​ 🇾​🇴​🇺​ 🇹​🇷​🇾​ 🇾​🇴​🇺​ 🇼​🇮​🇱​🇱​ 🇧​🇪​ 🇷​🇪​🇲​🇴​🇻​🇪​🇩​ 🇧​🇾​ 🇦​🇩​🇲​🇮​🇳​🇸​",
            "GOODBYE_DESC": "Sets the goodbye message. If you leave blank, it show's the goodbye message.",
            "NOT_SET_GOODBYE": "*You didn't set a goodbye message!*\n*To set:* ```.goodbye bye && bye#see ya \n to add member mention use {mention} \n to add  group description in welcome message use {gpdesc} \n to add group name use {gphead} \n to add group maker name use {gpmaker} \n to add bot name use {owner} \n to add exact indian time use {time} ```",
            "GOODBYE_ALREADY_SETTED": "*✅ Goodbye message has been set!*\n*Message:* ```",
            "NEED_GOODBYE_TEXT": "*You must write a message to set up the goodbye message.*\n*Example:* ```.goodbye bye && bye#see ya```", 
            "GOODBYE_DELETED": "*✅ Goodbye message has been deleted successfully!*",
            "GOODBYE_SETTED": "*✅ Goodbye message has been setted successfully!*"
        },
        "lydia": {
            "ADDLYDIA_DESC": "Activates Lydia (AI) for the user.",
            "NEED_REPLY": "```Please respond to a user's message!```",
            "COFFEEHOUSE": "```You haven't defined the Coffehouse API Key! ```",
            "ENABLED_LYDIA": "```Lydia has been activated for this user!```",
            "RMLYDIA_DESC": "Makes Lydia disabled for the user.",
            "ALREADY_EMPTY": "```Your user list is already empty!```",
            "NOT_ADDED": "```You haven't added this user already!```",
            "DISABLED": "```Lydia has been disabled for this user!```"
        },
        "memes": {
            "MEMES_DESC": "Photo memes you replied to.",
            "NEED_REPLY": "*Reply to a photo!*",
            "DOWNLOADING": "```Downloading media & making meme...```"
        },
        "ocr": {
            "OCR_DESC": "Reads the text on the photo you have replied.",
            "NEED_REPLY": "*Reply to a photo!*",
            "DOWNLOADING": "```Media is downloading & reading...```",
            "ERROR": "```I couldn't read this :/```\n*Error:*```{}```",
            "RESULT": "*Language:* ```{}```\n*Here is what I read:* ```{}```"
        },
        "profile": {
            "KICKME_DESC": "It kicks you from the group you are using it in.",
            "KICKME": "```Bye bye! Rudhra ini varathilla 🥲```",
            "PP_DESC": "Makes the profile photo what photo you reply.",
            "NEED_PHOTO": "*Give me a photo!*",
            "PPING": "```Setting profile photo...```",
            "BLOCK_DESC": "Block user.",
            "UNBLOCK_DESC": "Unblock user.",
            "BLOCKED": "blocked",
            "UNBLOCKED": "unblocked",
            "BLOCKED_UPPER": "Blocked!",
            "UNBLOCKED_UPPER": "Unblocked.",
            "NEED_USER": "Give me a user!",
            "JID_DESC": "Giving user's JID.",
            "JID": "```JID address of``` @{} ```: {}```",
            "JID_CHAT": "```Chat's JID address: {}```"
        },
        "removebg": {
            "REMOVEBG_DESC": "Removes the background of the photos.",
            "NEED_PHOTO": "*Give me a photo!*",
            "NO_API_KEY": "*You don't have an API key!*\nYou can get it here: remove.bg.",
            "RBGING": "```Removing background...```"
        },
        "scrapers": {
            "TRANSLATE_DESC": "It translates with Google Translate. You must reply any message.",
            "TRANSLATE_USAGE": ".trt tr it (From Turkish to Italian)",
            "NEED_REPLY": "```Please reply to any message!```",
            "LANG": "Language",
            "SING_DESC": "It sings song that you have written",
            "CURRENCY_DESC": "It coverts currency",
            "FROM": "Translated Language",
            "RESULT": "Translate",
            "DEVICE": "It shows the details of requested devices",
            "TRANSLATE_ERROR": "❌ An error occured while translating!*",
            "CURRENCY_ERROR": "```Syntax error! Example: .currency 1 TRY USD```",
            "INVALID_CURRENCY": "```Foreign currency transaction failed. You wrote wrong currency!```",
            "UNKNOWN_ERROR": "```An error occurred. Foreign currency transaction failed!```",
            "TTS_DESC": "It converts text to sound.",
            "TTS_ERROR": "```Error, Speech example of your sentence couldn't be made!```",
            "SONG_DESC": "Uploads the song you wrote.",
            "ISONG_DESC": "Uploads the song you wrote for ios users.",
            "NEED_TEXT_SONG": "*Please write a song!*\n*Example:* ```.song eminem - rap god```",
            "NO_RESULT": "*I couldn't find anything :(*",
            "DOWNLOADING_SONG": "✮⃝🎸INRL BOTÐØ₩₦ŁØÐł₦G ¥ØUƦ $Ø₦G✮⃝🎧",
            "NAMEY": "NAME",
            "URL": "LINK",
            "THUMB": "THUMB",
            "RATING": "RATING",
            "UPLOADING_SONG": "✮⃝🎸INRL BOT UPŁØλÐł₦G ¥ØUƦ $Ø₦G✮⃝🎧",
            "VIDEO_DESC": "Downloads video from YouTube.",
            "NEED_VIDEO": "*Please write a video link!*\n*Example:* ```.video https://youtube.com/watch?v=HD1-MX9q6fY```",
            "DOWNLOADING_VIDEO": "*✮⃝🎞️inrl bot downloadιng yoυr vιdeo✮⃝🎥*",
            "UPLOADING_VIDEO": "*✮⃝🎞️inrl bot υploadιng yoυr vιdeo✮⃝🎥*",
            "LOADING": "*✮⃝🎞️inrl bot downloadιng yoυr vιdeo✮⃝🎥*",
            "YT_DESC": "It searchs on YouTube.",
            "NEED_WORDS": "```Please write a few words!```",
            "GETTING_VIDEOS": "```I'm bringing videos...```",
            "NOT_FOUND": "*I couldn't find anything :(*",
            "SEARCHING": "*inrl bot 🔎 ѕearcнιng...*",
            "WIKI_DESC": "Searches query on Wikipedia.",
            "IMG_DESC": "Searches for related pics on Google.",
            "IMG": "Uploading photo ```{}``` number ```{} ```..."
        },
        "sticker": {
            "STICKER_DESC": "It converts your replied photo or video to sticker.",
            "NEED_REPLY": "*Reply to a photo or video!*",
            "DOWNLOADING": "```Wait cheyy ippo taram😉```"
        },
        "system_stats": {
            "ALIVE_DESC": "Does bot work?",
            "SYSD_DESC": "Shows the system properties."
        },
        "tagall": {
            "TAGALL_DESC": "Tags everyone in the group.",
            "ADMİN": "*I am not admin in this group!*",
            "SCAN": "Checks whether the entered number is registered on WhatApp.",
            "NO": "*Please Enter Any Phone Number!*\n*Example:* ```.scan 90xxxx```",
            "SUC": "*Numbered Person Uses WhatsApp! ✅*",
            "UNSUC": "*Numbered Person Does Not Use WhatsApp! ❌*",
            "PLKADMIN": ".report you are not admin \n\n 🇩​🇴​🇳​🇹​ 🇹​🇷​🇾​ 🇦​🇬​🇦​🇮​🇳​, 🇮​🇫​ 🇾​🇴​🇺​ 🇹​🇷​🇾​ 🇾​🇴​🇺​ 🇼​🇮​🇱​🇱​ 🇧​🇪​ 🇷​🇪​🇲​🇴​🇻​🇪​🇩​ 🇧​🇾​ 🇦​🇩​🇲​🇮​🇳​🇸​",
            "TAGADMİN": "Tags group admins.",
            "REPORT": "Sends reports to group admins.",
            "USER": "=== ```Report``` ===\n\n*User:* ",
            "REASON": "\n*Reason:* ",
            "REPLY": "*Please Respond to User's Message to Report!*"
        },
        "updater": {
            "UPDATER_DESC": "Checks the update.",
            "UPDATE": "*inrl bot ł$ ₡ØMPŁE₸EŁ¥ UP-₸Ø-Ðλ₸E!*",
            "NEW_UPDATE": "*₦E₩ UPÐλ₸E λVλłŁλBŁE ₣ØƦ inrl bot!*\n\n*To update Bot give this command: .update now*\n\n*Supporting Group Join First: https://chat.whatsapp.com/HVpTaTICeUi2G7hPlUlGUP*\n\n*https://youtube.com/c/PrinceRudh*\n\nChanges:\n```",
            "UPDATE_NOW_DESC": "It makes updates.",
            "UPDATING": "```inrl bot UPÐλ₸E ₡ҤE¥¥λ₸₸E...⏳```",
            "INVALID_HEROKU": "*❌ Your Heroku app name or api key wrong!*",
            "UPDATED": "*inrl bot UPÐλ₸E ƙλZҤł₦JU ✅*",
            "UPDATED_LOCAL": "*✅inrl bot UPÐλ₸EÐ!*",
            "AFTER_UPDATE": "*inrl bot ƦE$₸λƦ₸ł₦G*",
            "IN_AF": "*Please check* ```HEROKU_APP_NAME``` *and* ```app name``` *They must be same.*\n*If these two values ​​are the same, please restore* ```HEROKU_API_KEY```\n\n_To access these settings, use Heroku >> App >> Settings >> Reavel Config Vars_\n_To renew your API key, follow these steps, Heroku >> Account >> API Key then replace old api key in config vars._"
        },
        "whois": {
            "PL_DESC": "Displays metadata data of group or person.",
            "SUB": "*Group Name:* ",
            "DES": "*Group Description:* ",
            "OWN": "*Founder:* ",
            "COD": "*Unique Group Code:* ",
            "JİD": "*Person JID:* ",
            "ST": "*Person Status:* "
        },
        "log": {
            "LOG": "Saves the message you reply to your private number.",
            "REPLY": "*Please Reply To Any Message!*",
            "ANIM": "Does not support animated stickers!",
            "HEAD": "```===== [LOGGED MESSAGE] =====```\n\n",
            "USER": " From User Number \n",
            "FROM": " From the group with ID, ",
            "MSG": "Message: \n\n",
            "SUC": "*Message Successfully Saved to LOG!*"
        },
        "weather": {
            "WEATHER_DESC": "Shows the weather.",
            "NEED_LOCATION": "* Please write a location!*\n*Example:* ```.weather Bakü```",
            "LOCATION": "Location",
            "HMOD": "Finds mod apps from happymod",
            "QUOTE_DESC": "It shares famous quotes",
            "CM_DESC": "It sends complimentry sentenses",
            "EVINS_DESC": "It sends insulted words",
            "JOKE_DESC": "It sends random jokes",
            "APK_MOD": "It sends some special mod apks",
            "CARBON_DESC": "It sends carbon picture",
            "TEMP": "Temperature",
            "BOT_DESC": "Chat with Rudhra.\n Use .molu <message>",
            "BOT": ":",
            "DEVICE": "It shows the details of device",
            "DESC": "Description",
            "HUMI": "Humidity",
            "WIND": "Wind Speed",
            "CLOUD": "Cloud",
            "NOT_FOUND": "```I couldn't find a city with this name. 😖```"
        },
        "web": {
            "SPEEDTEST_DESC": "Measures Download and Upload speed.",
            "SPEEDTESTING": "```Running speed test...```",
            "SPEEDTEST_RESULT": "*Speed ​​test completed!*",
            "UPLOAD": "Upload",
            "DOWNLOAD": "Download",
            "CALC": "Performs simple math operations.",
            "SUC": "*Calculation Done ✅*\n*Result:* ",
            "UNSUC": "*Calculation Failed ❌*\n*Error:* \n",
            "VALİD": "*Please Use As Applicable!* \n*.calc 1 + 2*\n*.calc 3 x 5*\n*.calc 10 / 5*\n*.calc 5 - 2*",
            "PING_DESC": "Measures your ping.",
            "URL": "Shorten the long link."
        },
        "conventer": {
            "MP4TOAUDİO_DESC": "Rudhra Converts video to sound.",
            "MP4TOAUDİO_NEEDREPLY": "*You Must Reply to a Video!*",
            "MP4TOAUDİO": "```Rυԃԋɾα Cσɳʋҽɾƚιɳɠ Vιԃҽσ ƚσ Aυԃισ..```",
            "ANİM_STİCK": "Converts animated stickers to video.",
            "ANİMATE": "```Converting Animated Sticker To Video..```",
            "STİCKER_DESC": "Converts the sticker to a photo.",
            "STİCKER_NEEDREPLY": "*You Must Reply to a sticker!*",
            "STİCKER": "```ʀᴜᴅʜʀᴀ ᴄᴏɴᴠᴇʀᴛɪɴɢ ᴛʜᴇ sᴛɪᴄᴋᴇʀ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ..```",
            "XMEDİA_DESC": "It is a plugin with more than 25 media tools.",
            "T_FALSE": "```❌ Incorrect Blend Effect Entered!```\n```🔎 Existing Commands:```\n\n*$dodge* - Applies a pink color filter to the video.\n*$multiply* - Applies a green color filter to the video.\n*$grainmerge* - Increases the contrast of the video.\n*$and* - Applies black lightning effect according to the speed of the video.\n*$or* - Applies a white lightning effect according to the speed of the video.\n*$burn* - Applies green contrast to video.\n*$difference* - Shows the differences by applying green relief to the video.\n*$grainextract* - Shows the differences by applying gray relief to the video.\n*$divide* - Demonstrates the differences by applying a pink relief to the video.\n*$xor* - Applies both green relief and lightning effect to video.\n*$hardmix* - Mixes the colors of the video into a yellow and red tone.\n*$negation* - Turns the dynamics of the video to pink.",
            "T_NOT": "```💭 You Need To Enter Any Blend Effects!\n```🔎 Existing Commands:```\n\n*$dodge* - Applies a pink color filter to the video.\n*$multiply* - Applies a green color filter to the video.\n*$grainmerge* - Increases the contrast of the video.\n*$and* - Applies black lightning effect according to the speed of the video.\n*$or* - Applies a white lightning effect according to the speed of the video.\n*$burn* - Applies green contrast to video.\n*$difference* - Shows the differences by applying green relief to the video.\n*$grainextract* - Shows the differences by applying gray relief to the video.\n*$divide* - Demonstrates the differences by applying a pink relief to the video.\n*$xor* - Applies both green relief and lightning effect to video.\n*$hardmix* - Mixes the colors of the video into a yellow and red tone.\n*$negation* - Turns the dynamics of the video to pink.",
            "T_DESC": "Applies the selected TBlend effect to videos." 
        },
        "multiuse": {
            "NEED_WORD": "*Please enter username of any instagram account.*"
        },
        "mute": {
            "BİRMUTE": "*The group was silenced for 1 minute!*",
            "İKİMUTE": "*The group was silenced for 2 minute!*",
            "ÜÇMUTE": "*The group was silenced for 3 minute!*",
            "DÖRTMUTE": "*The group was silenced for 4 minute!*",
            "BEŞMUTE": "*The group was silenced for 5 minute!*",
            "ALTIMUTE": "*The group was silenced for 6 minute!*",
            "YEDİMUTE": "*The group was silenced for 7 minute!*",
            "SEKİZMUTE": "*The group was silenced for 8 minute!*",
            "DOKUZMUTE": "*The group was silenced for 9 minute!*",
            "ONMUTE": "*The group was silenced for 10 minute!*",
            "ONBİRMUTE": "*The group was silenced for 11 minute!*",
            "ONİKİMUTE": "*The group was silenced for 12 minute!*",
            "ONÜÇMUTE": "*The group was silenced for 13 minute!*",
            "ONDÖRTMUTE": "*The group was silenced for 14 minute!*",
            "ONBEŞMUTE": "*The group was silenced for 15 minute!*",
            "ONALTIMUTE": "*The group was silenced for 16 minute!*",
            "ONYEDİMUTE": "*The group was silenced for 17 minute!*",
            "ONSEKİZMUTE": "*The group was silenced for 18 minute!*",
            "ONDOKUZMUTE": "*The group was silenced for 19 minute!*",
            "YİRMİMUTE": "*The group was silenced for 20 minute!*",
            "YİRMİBİRMUTE": "*The group was silenced for 21 minute!*",
            "YİRMİİKİMUTE": "*The group was silenced for 22 minute!*",
            "YİRMİÜÇMUTE": "*The group was silenced for 23 minute!*",
            "YİRMİDÖRTMUTE": "*The group was silenced for 24 minute!*",
            "YİRMİBEŞMUTE": "*The group was silenced for 25 minute!*",
            "YİRMİALTIMUTE": "*The group was silenced for 26 minute!*",
            "YİRMİYEDİMUTE": "*The group was silenced for 27 minute!*",
            "YİRMİSEKİZMUTE": "*The group was silenced for 28 minute!*",
            "YİRMİDOKUZMUTE": "*The group was silenced for 29 minute!*",
            "OTUZMUTE": "*The group was silenced for 30 minute!*",
            "OTUZBİRMUTE": "*The group was silenced for 31 minute!*",
            "OTUZİKİMUTE": "*The group was silenced for 32 minute!*",
            "OTUZÜÇMUTE": "*The group was silenced for 33 minute!*",
            "OTUZDÖRTMUTE": "*The group was silenced for 34 minute!*",
            "OTUZBEŞMUTE": "*The group was silenced for 35 minute!*",
            "OTUZALTIMUTE": "*The group was silenced for 36 minute!*",
            "OTUZYEDİMUTE": "*The group was silenced for 37 minute!*",
            "OTUZSEKİZMUTE": "*The group was silenced for 38 minute!*",
            "OTUZDOKUZMUTE": "*The group was silenced for 39 minute!*",
            "KIRKMUTE": "*The group was silenced for 40 minute!*",
            "KIRKBİRMUTE": "*The group was silenced for 41 minute!*",
            "KIRKİKİMUTE": "*The group was silenced for 42 minute!*",
            "KIRKÜÇMUTE": "*The group was silenced for 43 minute!*",
            "KIRKDÖRTMUTE": "*The group was silenced for 44 minute!*",
            "KIRKBEŞMUTE": "*The group was silenced for 45 minute!*",
            "KIRKALTIMUTE": "*The group was silenced for 46 minute!*",
            "KIRKYEDİMUTE": "*The group was silenced for 47 minute!*",
            "KIRKSEKİZMUTE": "*The group was silenced for 48 minute!*",
            "KIRKDOKUZMUTE": "*The group was silenced for 49 minute!*",
            "ELLİMUTE": "*The group was silenced for 50 minute!*",
            "ELLİBİRMUTE": "*The group was silenced for 51 minute!*",
            "ELLİİKİMUTE": "*The group was silenced for 52 minute!*",
            "ELLİÜÇMUTE": "*The group was silenced for 53 minute!*",
            "ELLİDÖRTMUTE": "*The group was silenced for 54 minute!*",
            "ELLİBEŞMUTE": "*The group was silenced for 55 minute!*",
            "ELLİALTIMUTE": "*The group was silenced for 56 minute!*",
            "ELLİYEDİMUTE": "*The group was silenced for 57 minute!*",
            "ELLİSEKİZMUTE": "*The group was silenced for 58 minute!*",
            "ELLİDOKUZMUTE": "*The group was silenced for 59 minute!*",
            "SAATBİRMUTE": "*The group was silenced for 1 hour!*",
            "SAATİKİMUTE": "*The group was silenced for 2 hour!*",
            "SAATÜÇMUTE": "*The group was silenced for 3 hour!*",
            "SAATDÖRTMUTE": "*The group was silenced for 4 hour!*",
            "SAATBEŞMUTE": "*The group was silenced for 5 hour!*",
            "SAATALTIMUTE": "*The group was silenced for 6 hour!*",
            "SAATYEDİMUTE": "*The group was silenced for 7 hour!*",
            "SAATSEKİZMUTE": "*The group was silenced for 8 hour!*",
            "SAATDOKUZMUTE": "*The group was silenced for 9 hour!*",
            "SAATONMUTE": "*The group was silenced for 10 hour!*",
            "SAATONBİRMUTE": "*The group was silenced for 11 hour!*",
            "SAATONİKİMUTE": "*The group was silenced for 12 hour!*",
            "GÜNBİRMUTE": "*The group was silenced for 1 day!*",
            "GÜNİKİMUTE": "*The group was silenced for 2 day!*",
            "GÜNÜÇMUTE": "*The group was silenced for 3 day!*",
            "TÜR": "*Unknown Command!*\n_Minute: 1-59m_\n_Hour: 1-12h_\n_Day: 1d-3d_",
            "MUTE_DESC": "Turns off group chat. Only admins can send messages!",
            "MUTE_OPEN": "```The group chat has unmuted!```"
        },
        "unvoice": {
            "UV_DESC": "Rudhra Converts audio to sound recording.",
            "UV_REPLY": "*You Must Reply to the Audio File!*",
            "UV_PROC": "```Rudhra Converting to Sound Recording..```"
        },
        "ffmpeg": {
            "FF_DESC": "Applies the desired ffmpeg filter to the video.\n⌨️ Example: .ffmpeg fade=in:0:30",
            "FF_PROC": "Applying Effect.."
        },
        "spammer": {
            "SPAM_DESC": "It spam until you stop it.\n⌨️ Example: .spam test",
            "NEED_WORD": "*Need Some Words!*",
            "STOP_SPAMDESC": "Stops spam command.",
            "STOP_SPAM": "✅ *Spam successfully stopped! Please wait a moment.*",
            "ST_DESC": "Convert the replied photo or video to sticker and send it as spam.",
            "ST_ST": "```Please Don't Reply to Stciker!```\n```Only Reply to Video or Photo!```",
            "ST_NEED": "```You Must Reply To Any Video Or Photo!```",
            "AU_DESC": "Sends the replied audio as spam.",
            "AU_REP": "```Please Only Reply To Audio File!```",
            "FOTO_DESC": "Sends the replied photo as spam.",
            "FOTO_FOT": "```Please Reply To Any Picture!```",
            "VİD_DESC": "Sends the replied video as spam.",
            "VİD_NEED": "```Please Reply to Any Video!```"
        },
        "carbon": {
            "CARBON_DESC": "Uses carbon.sh for Text-to-Image",
            "CARBON_NEEDWORD": "*Not enough arguments to translate Text-to-Image!*\nExample: ```.carbon test```\nExample: ```.carbon making#test```",
            "CARBON_WARN": "Please only type in en and tr character!"
        },
        "scam": {
            "SCAM_DESC": "Creates 5 minutes of fake actions.",
            "SCAM_NOTFOUND": "*You Must Enter Fake Action!*\nExisting Types: ```typing & recording & online & stop```",
            "SCAM_NULL": "```Wrong Action Entered! Please use existing types.```"
        },
        "deepai": {
            "DEEPAI_DESC": "Runs the most powerful artificial intelligence tools using artificial neural networks.",
            "TEXT": "*You must enter text! Although I am a powerful artificial intelligence, I cannot read your thoughts!*",
            "URL": "*You must enter the image URL!*\n*Example:* https://i.hizliresim.com/nrg50b.jpg"
        },
        "ttp": {
            "TTP_DESC": "Converts text to plain painting.",
            "ATTP_DESC": "Adds rainbow effect to the text as a sticker.",
            "NEED_WORD": "*You must enter words!*",
            "ANIME_DESC": "It writes the text inside the banner the anime girl is holding",
            "TRUMP_DESC": "Converts the text to Trump's tweet.",
            "CHANGE_DESC": "Turns the text into the change my mind poster.",
            "GLOW_DESC": "Converts text into neon painting."
        },
        "wallpaper": {
            "WP": "It sends high resolution wallpapers."
        },
        "webss": {
            "SS_DESC": "Takes a screenshot from the page in the given link.",
            "LİNK": "You must enter link!"
        },
        "voicy": {
            "NEED_REPLY": "```Please reply to any message!```",
            "ONLY_AUDIO":"```Only audio file is accepted.```",
            "USAGE": "It converts audio to text.",
            "TEXT": "*Hey! I listened secretly to this voice and heard those!:* \n\n"
        },
        "notes": {
            "NOTES_USAGE": "Shows all your existing notes.",
            "NO_SAVED": "You don't have any saved notes.",
            "SAVED": "Here is your saved messages: ",
            "SAVE_USAGE": "Reply a message and type .save or just use .save <Your note> without replying",
            "REPLY": "Please provide a note or reply to a message.",
            "SUCCESSFULLY_ADDED": "Successfully added new note, check your notes with .notes.",
            "UNSUCCESSFUL": "Could not add note, please try again later or contact WhatsAsena developers.",
            "DELETE_USAGE": "Deletes *all* your saved notes.",
            "SUCCESSFULLY_DELETED": "Successfully deleted all your notes."
        },
        "instagram": {
            "NEED_WORD": "*Please enter username of any instagram account.*",
            "USAGE": ".insta <userName>",
            "DESC": "Fetches user informations from instagram",
            "LOADING": "*Searching*",
            "USERNAME": "Username",
            "FULL_NAME": "Fullname",
            "PRIVATE": "Private",
            "VERIFIED": "Verified",
            "ACCOUNT": "Account privacy",
            "PUBLIC": "Public",
            "HIDDEN": "Hidden",
            "NOT_FOUND":"User not found: "
        },
        "github": {
            "GİTHUB_DESC": "Collects github information from the given username.\n⌨️ Example: .github PrinceRudh",
            "REPLY": "```You Need To Type Any Username!```",
            "NOT": "```User not found!```",
            "FOLLOWERS": "Followers:",
            "NAME": "Name:",
            "USERNAME": "Username:",
            "REPO": "Public Repos:",
            "BİO": "Biography:",
            "FOLLOWİNG": "Following:",
            "COMPANY": "Company:",
            "BLOG": "Blog:",
            "MAİL": "Mail Address:",
            "LOCATİON": "Location:",
            "GİST": "Public Gists:",
            "JOİN": "Joining Date:",
            "HİRE_FALSE": "Cannot Hirable 🚫",
            "HİRE_TRUE": "Hirable ☑️",
            "HİRE": "Can s/he Hirable?:",
            "URL": "Profile URL:",
            "UPDATE": "Last Update:"
        },
        "tiktok": {
            "TİKTOK": "Downloads videos from Tiktok.",
            "NEED": "```You Must Enter Any Tiktok Link!``` \n*Example:* ```.tiktok https://vm.tiktok.com/ZSJY27ExT/```",
            "DOWN": "```Downloading Media..```",
            "CAPTİON": "Title:",
            "USERNAME": "Username:",
            "NAME": "Name:",
            "LİKE": "Likes:",
            "LİNK": "User Link:",
            "COMM": "Comments:",
            "VİEW": "Views:",
            "SHARE": "Shares:",
            "MUSİC": "Music:",
            "M_AUT": "Music Author:"
        },
        "lyrics": {
            "LY_DESC": "Finds the lyrics of the song.",
            "NEED": "```You Must Write Any Song!```",
            "SLY": "Lyrics:",
            "AUT": "Song Owner:",
            "BUL": "Founded Song:",
            "ARAT": "Searched Song:"
        },
        "gitlink": {
            "GL": "To get github links."
        },
        "covid": {
            "COV_DESC": "Shows the daily and overall covid table of more than 15 countries.",
            "NOT": "```Sorry I Could Not Find A Country Like This! Please Enter Applicable Country Codes!```\n\n```Country Codes:``` *.covid tr || az || usa || in || cn || nl || pk || ru || de || uk || gr || fr || jp || kz || id*"
        }
    }
}

---
## [wezm/mistakes.computer](https://github.com/wezm/mistakes.computer)@[3e9687b03b...](https://github.com/wezm/mistakes.computer/commit/3e9687b03b687f39118a3a09e3c8ab3e5fb33bbb)
#### Thursday 2022-04-07 07:51:43 by Jack Kelly

Using `::` instead of `:` in type signatures

Haskell, unlike most other ML-style languages, uses `::` for type
signatures and `:` for list cons. This allowed the following sort of
layout:

```hs
function
  :: Foo -- ^ docstring for Foo argument
  -> Bar
  -> Baz
```

But the advent of `-XLinearTypes` in GHC 9.x means that arrows can be
more than two characters long. Also, formatters like `ormolu` generate
the following style, which is more greppable and increasingly popular:

```hs
function ::
  -- | Docstring for Foo argument
  Foo ->
  Bar ->
  Baz
```

So: it's a wart that's different from the rest of the language family,
the alignment style it enables is falling out of favour, and if you
use linear types the alignment dream is dead anyway. Sadly, I think we
have to call it a mistake.

---
## [davideschiavone/ibex](https://github.com/davideschiavone/ibex)@[c15f3b8888...](https://github.com/davideschiavone/ibex/commit/c15f3b88883781808eaa96bda205a9bdaff5eb98)
#### Thursday 2022-04-07 08:25:45 by Rupert Swarbrick

[icache] Define some fake DPI functions to simplify linking

This is triggered by the fact that if the ICache parameter is false
then we don't instantiate the ibex_icache module. For verilator
simulations, the module is then discarded entirely, which means that
its two DPI functions are not defined. That's unfortunate because
we're also compiling the code in scrambled_ecc32_mem_area.cc, which
expects the functions to be defined.

The obvious solution (don't include scrambled_ecc32_mem_area.cc if you
don't have an icache) isn't easy to do, because FuseSoc doesn't
currently allow us to use parameters to configure its dependency
tree (see fusesoc issue 438 for a discussion).

The super-clever solution that I came up with before(!) was to declare
these symbols as weak in the C++ code. That way, we can do a runtime
check to make sure that no-one is silly enough to call them without an
icache, but everything will still build properly either way.

Unfortunately, that doesn't work well with xcelium simulations.
Xcelium turns out to compile all the C++ code into one .so library and
generate functions for exported DPI functions in another. These two
solibs then get loaded at runtime with dlopen(). But this doesn't work
with weak symbols: in fact, it seems you end up with the C++ version
every time. Boo!

So let's be stupider about it and define (bogus) versions of the DPI
functions in this case. Fortunately, both of them are designed to
return zero on failure so we can just return zero and needn't worry
too much.

The idea is that when this lands, we can revert the OpenTitan change
that switched the C++ code to using weak symbols and Xcelium
simulations will start working.

---
## [YUMGUY/SharedGameJam22New](https://github.com/YUMGUY/SharedGameJam22New)@[d1563c8a07...](https://github.com/YUMGUY/SharedGameJam22New/commit/d1563c8a07955b63ef8bf680401d47f08e4f2abc)
#### Thursday 2022-04-07 09:56:21 by RileySharar

implemented temp bar

Was buisier than expected tonight ill work on scaling the temp bar tomorrow along with getting the hp bar and and starting on more shit sorry for the wait

---
## [alphagov/govuk-infrastructure](https://github.com/alphagov/govuk-infrastructure)@[ed382d7f66...](https://github.com/alphagov/govuk-infrastructure/commit/ed382d7f664a7d4bb2bfdc5110c6d1e20795f852)
#### Thursday 2022-04-07 10:04:26 by Chris Banks

Update EKS module to v18 and fix up security group rules.

See https://github.com/terraform-aws-modules/terraform-aws-eks/releases
for changes.

In v18 of `terraform-aws-modules/eks`, the control plane nodes and
worker nodes belong to different AWS security groups by default, per
Amazon's recommendation. It's possible to revert to the previous
behaviour by setting a flag, but sticking with the recommendation means
we'll be able to control access to the control plane independently of
access to services running on the nodes.  It's slightly more complex in
theory, but I don't think introduces any extra operational/maintenance
complexity in practice (and will significantly simplify maintenance if
we should ever need to tighten the security group rules).

The `eks` module now outputs the cluster OIDC provider URL so we no
longer have to construct it ourselves.

Learning from our experience so far, we also allow minor (but not major,
i.e. breaking) version upgrades of the `eks` module to happen
automatically from now on, so that we won't keep getting bitten by bugs
which have already been fixed upstream when we make changes to live
clusters. It's very rare for one of these modules to introduce a serious
bug in a minor update - and we should be checking the diffs when
applying anyway - so on balance this is preferable to over-pinning and
the inevitable version rot that ensues. TF Cloud will further improve
the situation, hopefully in the near future.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[058b44b81e...](https://github.com/mrakgr/The-Spiral-Language/commit/058b44b81e850375e2f1580f73d942058b904be9)
#### Thursday 2022-04-07 10:58:39 by Marko Grdinić

"8:15am. I woke up an hour or two ago due to bad sleep, and had time to lounge.

A man can be on two teams for a time, but inevitably he will be on one. I can only strike out at the world through my own self development.

Let me just chill a bit and then I will get started on the course. Thanks to today at least, I will get my schedule readjustment. Waking up at 8am feels like I've got so many more hours in the day.

> Dendrofags... It's out baby!

No yet on VN Meido.

9am. Let me start. I've gotten over my grogginess a little.

Ah, yes. I remember what I wanted to do. I've been developing ways of thinking about blending modes. Let me just check out overlay again. I need to make sure of something.

10:15am. I got it. Right now I have a complete understanding of all the major blending modes.

I understand overlay. I understand hard light. I understand all the ones in the Designer, if not CSP.

It was really easy, all I had to do was just stack two fill layers, put a box mask on the top and compare the pixel brightness values via color sampling. That immediately reveals the mystery of the various modes. I can confirm that linear light is addsub.

https://substance3d.adobe.com/tutorials/courses/Mastering-Blending-Modes/youtube-fvmBCavPDLY

Let me watch the overlay video again.

There is no way around figuring this out. Understanding what blending modes do is just so crucial to being a digital artist. You can't call yourself an expert if you don't know what the main ones do.

10:35am. While watching the Designer course yesterday at the back of my mind was finding effective ways to think about the blending modes.

I realize for example that multiply is just subtract with the background passed in as the opacity mask. Screen would be the opposite, it is add with the inverse background passed in as a mask.

Overlay? Addsub with the background passed through a pyramid curve. All such masks can be linearized.

The more complex blending modes are just linear ones with implicit masks. That is a good way of thinking about them while working with height maps. Rather than trying to figure things out at random, I can thinking aobut what kinds of areas I want to affect? Top? Multiply. Middle? Overlay. Bottom? Screen.

10:45am. Now...shall I get started with the course? Yesterday I did the pebbles. How about I do the twig?

I'll have to watch it a gain, I forgot how to make a separate graph.

Usually, when I am under pressure like today, I do good work, so let's not make it an exception.

12:10pm. https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-_U2iLgqdZC4

Finally the last chapter of part 2.

12:45pm. Let me put down the twigs and I'll take a break here.

12:55pm. That was easy. The next up are roughness and coloring.

If I take stock of what I've been taught so far, none of it is difficult. It is just making deformed shapes, and layering them. I can do this. Let me have breakfast here."

---
## [spicetify/spicetify-cli](https://github.com/spicetify/spicetify-cli)@[0a89573c1c...](https://github.com/spicetify/spicetify-cli/commit/0a89573c1ce2f4ed3f4cdaac7651bc34dffb3a0a)
#### Thursday 2022-04-07 12:13:35 by Łukasz Ordon

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
## [thiagocardozo/terminal](https://github.com/thiagocardozo/terminal)@[446f280757...](https://github.com/thiagocardozo/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Thursday 2022-04-07 12:51:52 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [avar/git](https://github.com/avar/git)@[e571a7547e...](https://github.com/avar/git/commit/e571a7547e48433802eeb750f6dae00a2c147940)
#### Thursday 2022-04-07 13:19:02 by Ævar Arnfjörð Bjarmason

usage API: use C99 macros for {usage,usagef,die,error,warning,die}*()

Change the "usage" family of functions to be defined in terms of C99
variadic macros, as we've optionally done with the BUG() macro and
BUG_fl() function since d8193743e08 (usage.c: add BUG() function,
2017-05-12), and unconditionally since 765dc168882 (git-compat-util:
always enable variadic macros, 2021-01-28).

This would have been possible before having a hard dependency on C99,
but as the dual implementations of C99 and pre-C99 macros and
functions adjusted in preceding commits show, doing so would have been
rather painful.

By having these be macros we'll now log meaningful "file" and "line"
entries in trace2 events. Before this we'd log "usage.c" in all of
them, and the line would be the relevant locations in that file.

To do this we need to not only introduce X_fl() functions for
{die,error,warning,die}{,_errno}(), but also change all the callers of
the set_*() and get_() functions in usage.h to take "file" and "line"
arguments.

Neither the built-in {die,error,warning,die}{,_errno}() nor anyone
else does anything useful with these "file" and "line" arguments for
now, but it means we can define all our macros and functions
consistently.

It also opens the door for a follow-up change where these functions
could optionally emit the file name and line number, e.g. for
DEVELOPER=1 builds, or depending on configuration.

It might be a good change to remove the "fmt" key from the "error"
events as a follow-up change. As these few examples from running the
test suite show it's sometimes redundant (same as the "msg"), rather
useless (just a "%s"), or something we could now mostly aggregate by
file/line instead of the normalized printf format:

      1 file":"builtin/gc.c","line":1391,"msg":"'bogus' is not a valid task","fmt":"'%s' is not a valid task"}
      1 file":"builtin/for-each-ref.c","line":89,"msg":"format: %(then) atom used more than once","fmt":"%s"}
      1 file":"builtin/fast-import.c","line":411,"msg":"Garbage after mark: N :202 :302x","fmt":"Garbage after mark: %s"}

"Mostly" here assumes that it would be OK if the aggregation changed
between git versions, which may be what all users of trace2 want. The
change that introduced the "fmt" code was ee4512ed481 (trace2: create
new combined trace facility, 2019-02-22), and the documentation change
was e544221d97a (trace2: Documentation/technical/api-trace2.txt,
2019-02-22).

Both are rather vague on what problem "fmt" solved exactly, aside from
the obvious one of it being impossible to do meaningful aggregations
due to the "file" and "line" being the same everywhere, which isn't
the case now.

In any case, let's leave "fmt" be for now, the above summary was given
in case it's interesting to remove it in the future, e.g. to save
space in trace2 payloads.

The change here in git_die_config() is the bare minimum needed to get
it working, but better would be a change[1] to correctly report the
caller file and line numbers. Let's leave that for later, it can be
done later.

1. https://lore.kernel.org/git/patch-4.4-e0e6427cbd3-20211206T165221Z-avarab@gmail.com/#t

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [marcelo-gonzalez/nearcore](https://github.com/marcelo-gonzalez/nearcore)@[6351eb5511...](https://github.com/marcelo-gonzalez/nearcore/commit/6351eb55116fea2f906d681ce6966b5ec2546176)
#### Thursday 2022-04-07 15:39:52 by Simonas Kazlauskas

Use non-blocking log writer (#6470)

This will utilize a separate thread to write out the spans and events
without while letting the main computation to proceed with its business.
Additionally, we are buffering the output by lines, thus reducing the
frequency of syscalls that can occur when the subscriber is writing out
parts of the message.

This should mitigate concerns of enabling debug logging as its impact on
performance should now be minimal (putting an event structure onto a
MPSC queue.) There are still costs associated with logging everything
however. Most notably formatting and construction of the
`tracing_core::ValueSet`s still occur on the caller side, so if
constructing those is expensive, the logging might remain expensive.
An example of code sketchy like that (although silly) could be:

```
debug!(message = { std::time::sleep(Duration::from_secs(1)); "hello" })
```

or for a less silly example:

```
debug!("{}", my_vector.iter().map(|...| {
  do_expensive_stuff()
}).collect::<String>())
```

These should be considered a bug (alas one that `tracing` does not have
any tooling to detect, sadly.)

I opted adding a new crate dedicated to observability utilities. From my
experience using things like prometheus will eventually result in a
variety of utilities being written, so this crate eventually would
likely expand in scope...

Fixes https://github.com/near/nearcore/issues/6072 (though I haven't made any actual measurements as to what the improvement really is)

---
## [ceseo/binutils-gdb](https://github.com/ceseo/binutils-gdb)@[86d77f6a5b...](https://github.com/ceseo/binutils-gdb/commit/86d77f6a5be904f13c633f10bdf77ff3dd69db94)
#### Thursday 2022-04-07 16:00:33 by Andrew Burgess

gdb: don't try to use readline before it's initialized

While working on a different patch, I triggered an assertion from the
initialize_current_architecture code, specifically from one of
the *_gdbarch_init functions in a *-tdep.c file.  This exposes a
couple of issues with GDB.

This is easy enough to reproduce by adding 'gdb_assert (false)' into a
suitable function.  For example, I added a line into i386_gdbarch_init
and can see the following issue.

I start GDB and immediately hit the assert, the output is as you'd
expect, except for the very last line:

  $ ./gdb/gdb --data-directory ./gdb/data-directory/
  ../../src.dev-1/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.
  ----- Backtrace -----
  ... snip ...
  ---------------------
  ../../src.dev-1/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.
  Quit this debugging session? (y or n) ../../src.dev-1/gdb/ser-event.c:212:16: runtime error: member access within null pointer of type 'struct serial'

Something goes wrong when we try to query the user.  Note, I
configured GDB with --enable-ubsan, I suspect that without this the
above "error" would actually just be a crash.

The backtrace from ser-event.c:212 looks like this:

  (gdb) bt 10
  #0  serial_event_clear (event=0x675c020) at ../../src/gdb/ser-event.c:212
  #1  0x0000000000769456 in invoke_async_signal_handlers () at ../../src/gdb/async-event.c:211
  #2  0x000000000295049b in gdb_do_one_event () at ../../src/gdbsupport/event-loop.cc:194
  #3  0x0000000001f015f8 in gdb_readline_wrapper (
      prompt=0x67135c0 "../../src/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.\nA problem internal to GDB has been detected,\nfurther debugging may prove unreliable.\nQuit this debugg"...)
      at ../../src/gdb/top.c:1141
  #4  0x0000000002118b64 in defaulted_query(const char *, char, typedef __va_list_tag __va_list_tag *) (
      ctlstr=0x2e4eb68 "%s\nQuit this debugging session? ", defchar=0 '\000', args=0x7fffffffa6e0)
      at ../../src/gdb/utils.c:934
  #5  0x0000000002118f72 in query (ctlstr=0x2e4eb68 "%s\nQuit this debugging session? ")
      at ../../src/gdb/utils.c:1026
  #6  0x00000000021170f6 in internal_vproblem(internal_problem *, const char *, int, const char *, typedef __va_list_tag __va_list_tag *) (problem=0x6107bc0 <internal_error_problem>, file=0x2b976c8 "../../src/gdb/i386-tdep.c",
      line=8455, fmt=0x2b96d7f "%s: Assertion `%s' failed.", ap=0x7fffffffa8e8) at ../../src/gdb/utils.c:417
  #7  0x00000000021175a0 in internal_verror (file=0x2b976c8 "../../src/gdb/i386-tdep.c", line=8455,
      fmt=0x2b96d7f "%s: Assertion `%s' failed.", ap=0x7fffffffa8e8) at ../../src/gdb/utils.c:485
  #8  0x00000000029503b3 in internal_error (file=0x2b976c8 "../../src/gdb/i386-tdep.c", line=8455,
      fmt=0x2b96d7f "%s: Assertion `%s' failed.") at ../../src/gdbsupport/errors.cc:55
  #9  0x000000000122d5b6 in i386_gdbarch_init (info=..., arches=0x0) at ../../src/gdb/i386-tdep.c:8455
  (More stack frames follow...)

It turns out that the problem is that the async event handler
mechanism has been invoked, but this has not yet been initialized.

If we look at gdb_init (in gdb/top.c) we can indeed see the call to
gdb_init_signals is after the call to initialize_current_architecture.

If I reorder the calls, moving gdb_init_signals earlier, then the
initial error is resolved, however, things are still broken.  I now
see the same "Quit this debugging session? (y or n)" prompt, but when
I provide an answer and press return GDB immediately crashes.

So what's going on now?  The next problem is that the call_readline
field within the current_ui structure is not initialized, and this
callback is invoked to process the reply I entered.

The problem is that call_readline is setup as a result of calling
set_top_level_interpreter, which is called from captured_main_1.
Unfortunately, set_top_level_interpreter is called after gdb_init is
called.

I wondered how to solve this problem for a while, however, I don't
know if there's an easy "just reorder some lines" solution here.
Looking through captured_main_1 there seems to be a bunch of
dependencies between printing various things, parsing config files,
and setting up the interpreter.  I'm sure there is a solution hiding
in there somewhere.... I'm just not sure I want to spend any longer
looking for it.

So.

I propose a simpler solution, more of a hack/work-around.  In utils.c
we already have a function filtered_printing_initialized, this is
checked in a few places within internal_vproblem.  In some of these
cases the call gates whether or not GDB will query the user.

My proposal is to add a new readline_initialized function, which
checks if the current_ui has had readline initialized yet.  If this is
not the case then we should not attempt to query the user.

After this change GDB prints the error message, the backtrace, and
then aborts (including dumping core).  This actually seems pretty sane
as, if GDB has not yet made it through the initialization then it
doesn't make much sense to allow the user to say "no, I don't want to
quit the debug session" (I think).

---
## [ParadiseSS13/Paradise](https://github.com/ParadiseSS13/Paradise)@[6082c95eb3...](https://github.com/ParadiseSS13/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Thursday 2022-04-07 16:13:08 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [shanuflash/freeram](https://github.com/shanuflash/freeram)@[b74d5cf8c3...](https://github.com/shanuflash/freeram/commit/b74d5cf8c34a8df5421a43912904bc953b4f4cff)
#### Thursday 2022-04-07 16:13:18 by Shanu Flash #noυ

run command

"The method exec(String, String[]) from the type Runtime is deprecated since version 18" fuck you java

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[351afe260b...](https://github.com/tgstation/tgstation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Thursday 2022-04-07 16:42:47 by san7890

Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!) (#65899)

* Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!)

Hey there,

I implore you look at this photograph right here:

Ugly stupid base broken dumb /obj instead of the actual sprite fucking garbage idiotic purple-white square damn it i hate it so much fuck fuck fuck fuck let's fix it before the fire under my seat gets worse argh

Anyways, I checked with Kapu and did a bit of testing, and I managed to figure out a way to get the best of both the mapping world and the in-game world. Don't believe me? Check these out:

* addressses review

things still work

* kills female moth chests

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[38a13983cd...](https://github.com/mrakgr/The-Spiral-Language/commit/38a13983cd14aa41773a40676b8a74fe591eb558)
#### Thursday 2022-04-07 17:22:08 by Marko Grdinić

"2:25pm. Done with breakfast. I thought I had the last two chapters, but in fact it turns out that 190-192 of UQ Holder are not out on Nyaa. I am not sure why that is. I'll look around later.

Right now, let me focus on finishing the course.

https://youtu.be/ZW6b4FQ4kYk?t=203

It makes zero visual difference between copy, min and multiply here.

2:50pm. Interesting discovery from yesterday - if you click on the histogram icon in 2d view while using the histogram range, you can see the effect of moving the levels around exactly.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-5jcBPwUFnmU

Now finally come colors.

I wonder how this will work.

https://youtu.be/5jcBPwUFnmU?t=277

This is disappointing. I thought he would take into account the individual scattered objects.

https://youtu.be/5jcBPwUFnmU?t=324

First time hearing about highpass. What is it for?

https://www.gamedeveloper.com/art/the-power-of-the-high-pass-filter

3:20pm. Let me get back on track. I am getting distracted with that highpass filter thing.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-9gl3v5lelpY

I dislike the previous part so I am not going to do it, at least not as shown.

https://youtu.be/9gl3v5lelpY?t=67

I like this a lot more.

3:45pm. I am really yawning here. The lack of sleep is hitting me.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-yLQBRDGAnJ4

Let me at least just watch all of these. I am not too interested in following along at this point. I can just move to the next course for tips or go work on the desk.

I think there will be new things to learn in the wood plank course, but I know enough to do it by myself at this point.

Let me finish this one first and then I will think about it.

https://youtu.be/yLQBRDGAnJ4?t=463

There textures are far overengineered. There is zero chance anybody is going to notice these details other than the artist himself.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-o-N4iMwU9Yc

Just 2 more and I am done with part 3.

4:15pm. Having height be apart from color, roughness and the rest really makes it quite annoying to deal with. If I had to do a texture with such a large amount of detail, I'd honestly be tempted to do it in Houdini instead.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-0P337YhtX3Y

I am struggling to stay awake at 03-06, but let me watch this as well. I know that learning won't be as effective unless I practice as I go along, but at this point I just want to finish this course and move to the next thing.

https://youtu.be/0P337YhtX3Y?t=83
> 32 bit/channel is "assumed" to be in RAW (linear) space by most rendering software.

4:45pm. https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-QxC4HJhZ4B8

Here comes the last section. Let me watch this. I am at the end of my will here, but I can manage at least 3 more.

4:50pm. Ah, let me pause, I had enough. Let me take a break.

5:10pm. I am in a daze, and it seems time just went by in a flash. While I was thinking I realized something. I should have realized this yesterday and even earlier while I was playing making knots and trying out various blending mode, but given that I have Gradient Dynamic in Painter, there is literally nothing stopping me from painting the pattern myself.

Yeah, I know I said that I could do it in either Painter or Clip Studio Paint, but not in the way I am imainging right now.

Right now to get what I want, all I'd need to do is paint a few lines using a soft brush and bingo instant parallel lines. For knots, I just have to press on a particular point and it will give me what I want.

I am not sure how many of the nodes Painter has compared to Designer, but it has a ton of them. It wouldn't surprise me if it had things like Shape Splatter too.

Let me check.

Ohhh, if I click on Start Painting on the welcome screen it gives me that character model to start things off! That is convenient.

No, I am looking for it, and it seems it does not have mesh tilers or splatterers.

It does not really matter, since the brush takes their role. And the brush has plenty of randomization built into it already.

It has Blur Slope as expected.

A lot of this stuff I simply wouldn't think of studying in the Painter context, but the concepts translate seamlessly into Painter.

Doing the knots and the regular lines, one by one by hand would be incredibly difficult. But by simply putting things into gradient dynamic and painting that as well as taking advantage of blending modes, I could get a lot of power, on par with Designer, but with a lot more ease.

Whereas previously I'd need to paint this intricate pattern very carefully and tediously line by line, now I have the ability to do it in a couple of sweeping gestures.

5:40pm. Somebody posted vol 17 Dendro on Meido. Nice.

I am done with the break. I checked if Painter has Height Blend and it does. Nice.

Hmmm, one thing that has been bugging me - is it possible to rerandomize the brush strokes?

https://www.youtube.com/watch?v=0Vxne6fAOew
Using Dynamic Strokes

I did a search and this came up.

5:40pm. I've decided. I am going to continue my Designer studies for a bit longer since it is so beneficial for my Painter skills.

This gives me more motivation to finish the course.

Yeah, it is important. It is important to establish for what reason you are studying something. As I went deeper into the course my desire to study Designer dwindled, but now that I've reviewed I know how to do it efficiently in Painter, and my desire to make further gains is reignited. Working hard is not just a matter of willpower. The willpower will come once the incentives are established.

https://youtu.be/QxC4HJhZ4B8?t=590

Material Color Blend is basically just a fill layer.

6pm. Only two chapters left. They are just on publishing textures and .sbsar files. Let me watch them and then I am done with the course.

I'll probably close for the day. Usually I'd go on for longer, but I got up really early today so I am pooped.

https://youtu.be/oZt0eLeNx6c?t=496

He says that Ds has automatically been exporting the outputs as he is working on them. Interesting. I'd bet that Painter has this same capability then.

https://youtu.be/yQQx3NQNltk?t=173

It seems it has an option to automatically expose the random seed. I expected this should be possible somewhere. It would be too tedious to manually expose random seeds for the individual graph nodes.

6:30pm. Great. Let me check out the Dynamic Strokes video. I'll leave the wood plank 1.5 hour long video for later. I really don't have the energy to tackle it now.

https://youtu.be/0Vxne6fAOew?t=63

Isn't it great that I've just learned what a sbsar file is so I can follow this without problem.

So I am guessing it generates a different texture for each stamp by modifying the random seed? Yeah, that would be powerful.

https://youtu.be/0Vxne6fAOew?t=119

Ah, no, it is more than that. Simply changing the texture on each stamp would not allow to get a smooth gradient like this.

https://youtu.be/0Vxne6fAOew?t=162

So it can use one of stamp start, random seed and time.

https://youtu.be/0Vxne6fAOew?t=281

Sp might be better for 2d than CSP.

https://youtu.be/0Vxne6fAOew?t=491

It has random per stroke and random per stamp.

6:40pm. Come to think of slope blur would be very good for creating desert dunes. Those jagged ones I mean. I could work on height maps directly in Painter that way.

https://youtu.be/0Vxne6fAOew?t=634

Cracks, dynamic rocks, footprints. All this is good stuff.

https://youtu.be/0Vxne6fAOew?t=786

It seems that Painter has functionality for creating dynamic strokes directly in it.

7pm. That was satisfying. I seem to be getting better at Painter without actually using it.

Familiarizing yourself with the tools you are going to be using is really a major part of actually being good at using them.

I really do have enough to start work on the desk now, but I will give the rest of the courses a try tomorrow. After I feel satisfied, I will dive into Painter again and get the desk done. I have so many new possibilities compared to even a few days ago."

---
## [Tsumirez/react-cryptocurrency-app](https://github.com/Tsumirez/react-cryptocurrency-app)@[7affc4ce05...](https://github.com/Tsumirez/react-cryptocurrency-app/commit/7affc4ce055ef6f6945d1d8cfa77d02a36bee922)
#### Thursday 2022-04-07 17:33:12 by Tsumirez

Installed packages for the project.

One pain point is chart.js and react-chartjs-2 having a dependancy issue. It seems react v18 is the cause, not all npm packages are ready for this badboy yet. You can tell it to shut the fuck up and install anyway with --force flag!

npm install react-chartjs-2 chart.js --force.

As for other packages:

antd - UI component library. Chinese made...yeah.

npm install @ant-design/icons - kinda self explanatory.

chart.js, react-chartjs-2 - libraries for javascript powered chart components.

@reduxjs/toolkit - something new on redux block. We'll learn it in this project

axios - well no brainer here. For handling data fetching and making server calls.

html-react-parser - converts html elements into react elements (remember that synthetic react stuff)

milify - long ass numbers made into human readable strings.

moment - library for doing all sorta down and dirty with dates.

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[a7dad265de...](https://github.com/sunamo/sunamo/commit/a7dad265de6fe7a628668a8d23a296d6a3666f4a)
#### Thursday 2022-04-07 18:01:59 by Radek Jancik

I share the belief of many of my contemporaries that the spiritual crisis pervading all spheres of Western industrial society can be remedied only by a change in our world view. We shall have to shift from the materialistic, dualistic belief that people and their environment are separate, toward a new consciousness of an all reality, which embraces the experiencing ego, a reality in which people feel their oneness with animate nature and all of creation. - Hofmann, Dr. Albert

---
## [yonipy/voltage](https://github.com/yonipy/voltage)@[33c9a7d6bb...](https://github.com/yonipy/voltage/commit/33c9a7d6bb0b4a4f3dd29755dec15f449e145140)
#### Thursday 2022-04-07 19:34:05 by EnokiUN

Let me tell you a fun story, no?

So I decided that I'll -for once- test what I added before i push it,
crazy I know

Thing is, I made a file called `commands.py` to test commands the was
confused why `from voltage.ext import commands` didn't have the shit it
was supposed to have.

There goes my evening, oh well.

---
## [ghostwriter/mezzio-org-mezzio-authentication-basic](https://github.com/ghostwriter/mezzio-org-mezzio-authentication-basic)@[aa90688807...](https://github.com/ghostwriter/mezzio-org-mezzio-authentication-basic/commit/aa90688807c6b201caeafe2f51a1bf8b6ac40b99)
#### Thursday 2022-04-07 20:10:33 by Michał Bundyra

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[00e0af307e...](https://github.com/treckstar/yolo-octo-hipster/commit/00e0af307eae463d205193b827bb5a2ac58acf09)
#### Thursday 2022-04-07 20:45:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [ascent08/MCubed](https://github.com/ascent08/MCubed)@[17dca8ed74...](https://github.com/ascent08/MCubed/commit/17dca8ed7477077a79dd4744a394027a73f3a30b)
#### Thursday 2022-04-07 21:41:47 by ascent_

some updates

Removed Horse Stats Vanilla, updated a bunch of other mods

unfortunately we're still missing a bunch of mods for 1.18.2. here are my thoughts on each mod that has yet to be updated.

also i'm not listing the versions of the mods that were updated. figure it out for yourself fucko. ANYWAYS:

BetterEnd: i have been considering removing it because i don't want to go too overboard with adding new materials and this mod actually does add new materials that end up being stronger than netherite. i want the pack to keep a sort-of vanilla feel and adding new materials pushes it further away from that. however the mod does add some cool shit biome-wise.

Botania: to be completely honest I've never actually played around with the mod while testing the pack out. however it is one of those older mods that's decently well-known and the fact that i can have one of those older mods in the pack is really cool.

Gate of Babylon: I REALLY want to keep this mod because so far it's been the only mod i could find that adds new types of weapons. unfortunately it hasn't been updated since february (before 1.18.2 came out) which is painful.

Rat's Mischief: honestly we could do without it, i'd just like to have it in because ha ha funny rat

Spectrum: i really want to keep this mod in because it adds so much to the game yet keeps the game feel a lot like vanilla, as you progressively unlock the ability to see certain blocks. the only issue i really have with it is the geodes spawning above ground, which i can easily fix through the configs.

Stoneholm: underground villages. a relatively minor addition, but one that is really nice to have nonetheless.

YUNG's Better Strongholds: I'd rather have this in the pack for fairly obvious reasons. It genuinely makes strongholds better and more interesting than the current vanilla design which has been around for over a decade now.

anyways yeah

---
## [Opentrons/ot3-firmware](https://github.com/Opentrons/ot3-firmware)@[a35a8bbb4e...](https://github.com/Opentrons/ot3-firmware/commit/a35a8bbb4edc79618a15ba66ffdef673022ac4ce)
#### Thursday 2022-04-07 22:03:39 by Seth Foster

im so sorry

This commit contains two major pieces of work.

First, I was finally unable to resist the siren song of getting the i2c
stuff into its own subproject. I can only blame the crew, who did not
lash me to the mast tightly enough.

That comes with new github actions workflows, dependencies in the
pipette on the new subdirectory, and a whole bunch of renames in a whole
bunch of places.

Second, we finally found the problem that we were debugging: if you
memcpy std::functions, that obviously doesn't trigger their copy ctor,
so the memcpyd-from function gets destroyed when it leaves the scope
where it was memcpyd, and there goes its closure object. This is going
to be a consistent problem with anything with a non-trivial dtor that
goes through a message buffer.

The solution is to instead pass around queue handles that we can write
responses to. This is in itself kind of a pain since we can't use std
functions! We kind of have to bodge in manual c-style closures with
reinterpret cast, but we can at least protect the building of those
closures with some nice template concepts.

At this point, there also really didn't seem like a point keeping the
various different kinds of i2c messages so now there's just transact and
transactionresponse.

The i2c subdirectory compiles and passes the tests for i2c_task and
i2c_writer; it probably doesn't compile or pass the test for poller, but
a) it's kind of cool that the includes are clean enough that you can
just not run the poller tests and it's fine, and b) yeah no kidding. It
also For Sure will not be able to compile the pipettes until the sensor
and eeprom classes are adapted.

---

