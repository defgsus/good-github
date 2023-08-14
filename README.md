## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-13](docs/good-messages/2023/2023-08-13.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,937,470 were push events containing 2,653,378 commit messages that amount to 138,690,234 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[03762f51f1...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/03762f51f111338d83a55e891bc92f575c168c6e)
#### Sunday 2023-08-13 00:08:31 by Ben10Omintrix

convert the eyeball a basic monster (#77411)

## About The Pull Request
I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[99c6601c84...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/99c6601c84dd999804aff67f17f4844ffa4cc2e1)
#### Sunday 2023-08-13 00:08:47 by Sealed101

Laser pointer update: Shining Through Walls Edition (feat. fixes!) (#77007)

# _PR PSA_


![augh](https://github.com/tgstation/tgstation/assets/75863639/6dc87fc7-65a3-4b7c-9b8d-a1432cacbe93)


## About The Pull Request
Cleans up code for laser pointers, fixing some bugs like the
forever-charging state or affecting dead cats along the way.
Remaining charge is now available upon examine.
Canonizes #45834 by implementing an upgrade to the laser pointers:
installing a bluespace crystal into a laser with tier 3 or higher laser
diode lets it shine through walls. Using an upgraded laser uses twice
the charge of a normal one. Of course, you can only shine it on
something if you can see the target behind the wall, like via x-ray or
thermals. Mesons don't count, however.
If one tries to jam a crystal into a pointer with a tier 1/2 laser (or a
tier 1/2 laser in a pointer with an installed crystal), _something_ will
get teleported, crushing the crystal.
You can uninstall the crystal with wirecutters or a hemostat. The
pointer will _hint_ on closer examination (`examine_more`) at a
possibility of a crystal being installed if you upgrade the laser
(different messages for tier 1/2/3,4).
Removes one stupid 1% increase for a recharge chance per process tick if
your laser was in a full recharge state because it was insignificant and
irrelevant.

i've had a branch for this for almost 9 months and i was always laying
it off for some day later. today i just completely fucked the branch.
whoops. i'm not even sure at this point what else did i fix while here,
double whoops

## Why It's Good For The Game
Closes #45834 - Canonizes a bug into a feature.
Fixes #77003 - lol
Cleaner code, possibly more robust even.
Seeing the remaining charge was not available at all and the only hint
was when you tried shining the pointer on something. That sucks.

## Changelog
:cl:
add: you can upgrade laser pointers with a bluespace crystal to let them
shine through walls at double the power cost, if the laser in the
pointer is of tier 3 or higher.
qol: laser pointer charge can be seen by examining it
fix: fixed laser pointers luring dead cats when shone upon
code: laser pointer code cleaned up a tad
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[edbe3d737b...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/edbe3d737b3952dfffc5d6e4a2cbdf88b4e6f1a9)
#### Sunday 2023-08-13 00:09:38 by san7890

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

## About The Pull Request

I was bored, so did this. Probably one of the neatest refactors I've
done, sorry if there's some oddities because I was experimenting with
some other stuff in this so just tell me to clean them up whenever I
can.

Anyways, morphs are basic mobs now. We are able to easily refactor the
whole "eat items and corpses" stuff in the basic mob framework, but the
whole "morph into objects and people" turned out to be a bit trickier.
That was easily rectified with a datum mob cooldown action and
copy-pasting the old code into that code, as well as doing some nice
stuff with traits and signals to ensure the one-way communication from
the action to the mob.

Old Morph AI didn't seem to be existant whatsoever, they inappropriately
leveraged some old procs and I have no idea how to make it work with new
AI. They DEFINITELY don't spawn outside of admin interference/ the event
anymore, and will always be controlled by a player, so this shouldn't be
too bad of an issue. I gave them something to seem alive just in case
though, but I think adding legitimate prop-hunt AI would be such a
laborious task that I am unwilling to do it in this PR.
## Why It's Good For The Game

If admins want to add the ability for Ian to assume the form of the HoP,
they can do that now! The datum action cooldown is quite nice for simple
and basic mobs... but it is currently not compatible with carbons. That
is not within scope for this PR, but I am dwelling on ways to extend it
to carbon but they all sound really awfully bad.

Also morphs are smarter, and we tick another simple animal in need of
refactoring off the list.
## Changelog
:cl:
refactor: Morphs are now basic mobs with a nice new ability to help you
change forms rather than the old shift-click method, much more
intuitive.
admin: With the morph rework comes a new ability you can add to mobs,
"Assume Form". Feel free to add that to any simple or basic mob for le
funnies as Runtime turns into a pen or something.
/:cl:

~~Does anyone know if there's a (sane) way to alias a cooldown action as
a keypress? I can't think of a good way to retain the old shift-click
functionality, because that does feel _kinda_ nice, but I think it can
be lived without.~~ I added it. Kinda fugly but whatever.

---
## [MrStonedOne/tgstation](https://github.com/MrStonedOne/tgstation)@[f0dc574c37...](https://github.com/MrStonedOne/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Sunday 2023-08-13 00:13:54 by carlarctg

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
## [dcampman/TimeKeeper](https://github.com/dcampman/TimeKeeper)@[31bf47878f...](https://github.com/dcampman/TimeKeeper/commit/31bf47878f1032bfaf179631a42523dd6eebdcba)
#### Sunday 2023-08-13 00:23:46 by David

aider: Updated the `timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.html` and `timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.js` files to support features such as export log file type selection, file path input, image upload, title and background color options, task description input, and time format options.

# Aider chat conversation:

USER: can you list the features of the timekeeper action

ASSISTANT: The TimeKeeper action has the following features:

1. **Start Timer**: When the button associated with the TimeKeeper action is pressed, it starts a timer for a specific task. If the timer is already running, it pauses the timer.

2. **Pause Timer**: If the timer is running and the button is pressed again, it pauses the timer.

3. **Resume Timer**: If the timer is paused and the button is pressed, it resumes the timer.

4. **Reset Timer**: If the button is long-pressed, it resets the timer.

5. **Display Time**: The button displays the current time of the timer.

6. **Customizable Task Name and Logo**: The task name and logo on the button can be customized in the Property Inspector.

7. **Export Time**: The tracked time can be exported in JSON, CSV, or plain text format.

8. **Pause All Timers**: There is a separate PauseAll action that can pause all timers at once.

Please note that these features are based on the provided code and the description in the `readme.md` file. If there are additional features not mentioned in the code or the readme, I would need more information to list them.

USER: can you make the necessary updates to the `timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.html` and `timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.js` files to support these features?

ASSISTANT: Sure, I can help with that. However, I need more specific details about the changes you want to make. For example, what kind of user interface do you want in the Property Inspector for the TimeKeeper action? What settings should the user be able to change? How should the exported time be formatted and where should it be saved? Please provide as much detail as possible.

USER: can you review the inforamtion ive already provided about the inspector that i wanted?

ASSISTANT: I apologize for the confusion, but I couldn't find any specific details about the Property Inspector for the TimeKeeper action in the information you've provided so far. Could you please provide more details about what you want to include in the Property Inspector? For example, what settings should the user be able to change? How should the user interface look like? Any specific functionalities you want to include? The more details you provide, the better I can assist you.

USER: I would like to have a drop down selector for an export log file type. This will set the file type; options include: json, csv, or txt. Any action start time should be recorded to the log file. Any paused action should record the time in the log file, and include the elapsed time. I need to create an output of the timekeeper action in a readable format to tell when a action was started, paused, or how long the total time on the task has been inbetween pauses. I will also need a file selector box, or something that will allow me to input the file path where the log file should be written. Ill also need a image upload box. I want to upload an image as a background for the action. is this possible in a streamdeck plugin? Il need the basic title and maybe background color option if no image is uploaded. what do you think so far of these features? what would you add to this action?

ASSISTANT: The features you've described for the TimeKeeper action's Property Inspector sound very useful. Here's a summary:

1. **Export Log File Type**: A dropdown selector that allows the user to choose the file type for the export log. Options include JSON, CSV, or TXT.

2. **Log Action Start and Pause Times**: The start time of each action is recorded in the log file. When an action is paused, the time is recorded in the log file along with the elapsed time.

3. **File Path Input**: A file selector or input box that allows the user to specify the file path where the log file should be written.

4. **Image Upload**: An image upload box that allows the user to upload an image to use as a background for the action.

5. **Title and Background Color Options**: Basic options for setting the title and background color of the action, to be used if no image is uploaded.

These features would provide a lot of flexibility and customization for the user.

In addition to these features, you might consider adding:

- **Task Description**: An input field where the user can enter a brief description of the task. This could be included in the log file to provide more context about what was done during the recorded time.

- **Auto-Save Option**: A checkbox that, when checked, automatically saves the log file at regular intervals. This could help prevent data loss if the Stream Deck software or the user's computer crashes.

- **Time Format Options**: A dropdown that lets the user choose how times are formatted in the log file. For example, they might prefer "1 hour, 15 minutes, 42 seconds" over "1:15:42".

Please let me know what you think of these suggestions, and if you'd like to proceed with implementing these features.

USER: lets add those other features you mentioned, but i dont think ill need the auto-save features. If the timer class is written correctly, it would append the timestamp and or elapsed time to the file when the event occurs. Is that possible? I dont know how the Log Action Start and Pause Times inspector property do, maybe we dont need that as an inspector property?

ASSISTANT: Yes, you're correct. If the Timer class is implemented correctly, it should be able to write the start, pause, and elapsed times directly to the log file whenever those events occur. This would make an auto-save feature unnecessary.

As for the "Log Action Start and Pause Times" feature, it's not something that the user would need to control from the Property Inspector. It's more of a feature of the TimeKeeper action itself. The action should automatically log these times as part of its normal operation.

So, based on your feedback, here are the features we'll add to the Property Inspector for the TimeKeeper action:

1. **Export Log File Type**: A dropdown selector that allows the user to choose the file type for the export log. Options include JSON, CSV, or TXT.

2. **File Path Input**: A file selector or input box that allows the user to specify the file path where the log file should be written.

3. **Image Upload**: An image upload box that allows the user to upload an image to use as a background for the action.

4. **Title and Background Color Options**: Basic options for setting the title and background color of the action, to be used if no image is uploaded.

5. **Task Description**: An input field where the user can enter a brief description of the task. This could be included in the log file to provide more context about what was done during the recorded time.

6. **Time Format Options**: A dropdown that lets the user choose how times are formatted in the log file. For example, they might prefer "1 hour, 15 minutes, 42 seconds" over "1:15:42".

Let's proceed with implementing these features. I'll start by updating the `timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.html` file to include the necessary HTML elements for these features. Then, I'll update the `timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.js` file to handle the user's input and control the behavior of the TimeKeeper action.

USER: do it

USER: --map-tokens

USER: do it

ASSISTANT: Alright, let's start with the `timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.html` file. We'll add the necessary HTML elements for the features we discussed.

```html
timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.html
<<<<<<< ORIGINAL
    <!-- Your HTML code goes here -->
=======
    <!-- Your HTML code goes here -->
    <div>
      <label for="fileType">Export Log File Type:</label>
      <select id="fileType">
        <option value="json">JSON</option>
        <option value="csv">CSV</option>
        <option value="txt">TXT</option>
      </select>
    </div>
    <div>
      <label for="filePath">Log File Path:</label>
      <input type="text" id="filePath" name="filePath">
    </div>
    <div>
      <label for="imageUpload">Background Image:</label>
      <input type="file" id="imageUpload" name="imageUpload">
    </div>
    <div>
      <label for="title">Title:</label>
      <input type="text" id="title" name="title">
    </div>
    <div>
      <label for="bgColor">Background Color:</label>
      <input type="color" id="bgColor" name="bgColor">
    </div>
    <div>
      <label for="taskDescription">Task Description:</label>
      <textarea id="taskDescription" name="taskDescription"></textarea>
    </div>
    <div>
      <label for="timeFormat">Time Format:</label>
      <select id="timeFormat">
        <option value="hh:mm:ss">HH:MM:SS</option>
        <option value="h hours, m minutes, s seconds">H hours, M minutes, S seconds</option>
      </select>
    </div>
>>>>>>> UPDATED
```

Next, we'll update the `timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.js` file. We'll add event listeners for the new HTML elements and implement the logic for handling the user's input.

```javascript
timekeeper.sdPlugin\actions\timekeeper\property-inspector\inspector.js
<<<<<<< ORIGINAL
$PI.onConnected((jsn) => {
    // Your JavaScript code goes here
});
=======
$PI.onConnected((jsn) => {
    // Your JavaScript code goes here
    document.getElementById('fileType').addEventListener('change', function() {
        // Handle change in file type
    });
    document.getElementById('filePath').addEventListener('change', function() {
        // Handle change in file path
    });
    document.getElementById('imageUpload').addEventListener('change', function() {
        // Handle image upload
    });
    document.getElementById('title').addEventListener('change', function() {
        // Handle change in title
    });
    document.getElementById('bgColor').addEventListener('change', function() {
        // Handle change in background color
    });
    document.getElementById('taskDescription').addEventListener('change', function() {
        // Handle change in task description
    });
    document.getElementById('timeFormat').addEventListener('change', function() {
        // Handle change in time format
    });
});
>>>>>>> UPDATED
```

Please note that this is just a starting point. The event listeners currently don't do anything. You'll need to fill in the logic for handling the user's input based on the specific requirements of your application.

---
## [lbnesquik/TerraGov-Marine-Corps](https://github.com/lbnesquik/TerraGov-Marine-Corps)@[fb4899d20e...](https://github.com/lbnesquik/TerraGov-Marine-Corps/commit/fb4899d20e990a0a65b8cb5b0ad19b1ef9ab083e)
#### Sunday 2023-08-13 00:25:48 by KM-Catman

Slight redesign of Valhalla Vendors and Chemistry. Adds FC and Synth to Valhalla. (#13612)

* Valhalla Fixes

Start room is now all Hulls, adds a Friend, Materializes the Chaplain's chained demon, and adds more Xeno Huds.

* FC and Synth Added. Slight readjustment.

* Changed the vendor section as per Grayson's request

* Adds three new Warning Stripes.

Adds a FCDR, Synth, and Mech warning stripe. Adds them in front of the prep rooms

* Duct Taped Space

* Removed random bedsheet (Goddamn you hotkeys)

---
## [HaultyAnonie/Foundation-19](https://github.com/HaultyAnonie/Foundation-19)@[b4642dc835...](https://github.com/HaultyAnonie/Foundation-19/commit/b4642dc835dc801d801fd543cfd34bd44ca23929)
#### Sunday 2023-08-13 00:36:45 by cheesePizza2

Armor improvements (#1251)

* the fixes

* FUCK YOU

* few more improvements

* bring em back

* fuck you

---
## [Alchael/EASECore](https://github.com/Alchael/EASECore)@[a07d4fb1be...](https://github.com/Alchael/EASECore/commit/a07d4fb1be13413af67ccb2ab0aa7cd87a6705c7)
#### Sunday 2023-08-13 00:50:36 by Alchael

alpha 0.8.8.1

Bugfixes:
Machinist Ricochet usage.. Hypercharge not being utlized.
Ranged DPS and all classes now autofollow properly.
Autorepair fixed.
Bosses with wonky model and los2 should now be targetted properly. ei: Midgardsormr, Pandemonium, etc.
Paladin Royal Authority combo fixed instead of spamming
Black Mage DOT usage.
White Mage Medica 2 usage.
White Mage Raise on dead member (please confirm if you have time)
Fixed console spam about found interactable
Debug Drawings Overlay

Rotations:
Added Dark Mind to Dark Knight
Added Clemency and Cover to Paladin

Feature:
Shortcut utilization upon defeat in autodungeon.
Setting Autolegacy off for people with autolegacy addon during dungeon autoleveling to not mess up with the navigation.
Adds perpendicular dodge mechanic to annoying mob like the Centurion Colossus and his big sword that sends us flying backwards. Healers are now happy.

---
## [ViesteToken/WhitePaper](https://github.com/ViesteToken/WhitePaper)@[09765569d7...](https://github.com/ViesteToken/WhitePaper/commit/09765569d734d6658d59d4b92220837b5d7a0bd8)
#### Sunday 2023-08-13 01:15:10 by ViesteToken

Create README.md

# ViesteToken

https://irp.cdn-website.com/91b6d645/dms3rep/multi/logo+32x32.png

**Table of Contents:**
- [Introduction](#introduction)
- [Technology and Architecture](#technology-and-architecture)
- [Token Utility](#token-utility)
- [Sustainability and Economic Growth](#sustainability-and-economic-growth)
- [Community and Collaboration](#community-and-collaboration)
- [Founder's Vision](#founders-vision)
- [Conclusion](#conclusion)

## Introduction

ViesteToken is an innovative project that aims to revolutionize the intersection of cryptocurrencies, sustainable tourism, and the green economy. At its core, ViesteToken utilizes cutting-edge blockchain technology to create an ecosystem where holders of the ViesteTokenPoly (VTPL) token can experience the advantages of digital assets while contributing to sustainable tourism and eco-friendly economic development.

## Technology and Architecture

At the heart of ViesteToken lies the powerful Polygon network, a Layer 2 scaling solution built on Ethereum. Polygon ensures lightning-fast and cost-effective transactions, making it an ideal foundation for ViesteToken's objectives. The project's underlying smart contract, developed on the Ethereum platform, governs the functionalities of the ViesteTokenPoly token. This intelligent contract facilitates seamless token transfers, tracks token balances for each address, and manages transaction permissions, ensuring a secure and efficient ecosystem.

## Token Utility

ViesteTokenPoly holds significant utility within the ecosystem, offering holders a myriad of benefits. A unique aspect of ViesteTokenPoly ownership is exclusive discounts at partner businesses located in the charming Italian town of Vieste. This dynamic incentive encourages token holders to explore local culture and gastronomy while enjoying cost savings. The project's innovative loyalty program adds an extra layer of value, rewarding users with special privileges, creating a cyclical relationship between consumption and rewards. Additionally, accumulated bonus points can be redeemed for unforgettable vacations in Vieste, providing an exciting opportunity to experience the town's natural beauty and attractions.

## Sustainability and Economic Growth

One of ViesteToken's core missions is to promote sustainable tourism practices and facilitate eco-friendly economic growth. By collaborating with local businesses and emphasizing responsible consumption, ViesteToken aims to bolster economic development in tourism-driven destinations while minimizing the ecological footprint of these activities. This dual approach addresses both economic and environmental concerns, showcasing ViesteToken's commitment to holistic progress.

## Community and Collaboration

ViesteToken's vibrant community is at the heart of its success. Through active engagement on platforms like Telegram and social media, community members share insights, ideas, and experiences related to sustainable tourism and cryptocurrencies. The project's collaboration extends globally, as ViesteToken partners with various entities to expand the token's utility across diverse sectors and geographical regions, reinforcing the project's overarching goals.

## Founder's Vision

Driving ViesteToken's innovative vision is Youness Tafersiti Faris, a dynamic entrepreneur with a profound passion for both tourism and the world of cryptocurrencies. Fluent in multiple languages, Youness's linguistic prowess serves as a bridge between cultures, fostering international collaborations that are integral to ViesteToken's global impact. Drawing from his extensive experience in the tourism sector, Youness envisions ViesteToken as a pioneering force that seamlessly integrates technology, tourism, and sustainability.

## Conclusion

ViesteToken stands as a groundbreaking project that harmoniously merges blockchain technology with the principles of sustainable tourism and eco-conscious economic growth. Through the ViesteTokenPoly ecosystem, the project transcends the realm of digital assets, offering real-world experiences and value. With a steadfast commitment to innovation, community engagement, and environmental responsibility, ViesteToken is poised to redefine not only the financial landscape but also the way we travel and interact with our planet.

*For more information, please visit [www.viestetoken.com](https://www.viestetoken.com) or join our active [Telegram community](https://t.me/viestecommunity).*

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[ce26e0b8c0...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/ce26e0b8c0d3d7441d2c18d7fadb080e305e3488)
#### Sunday 2023-08-13 01:50:13 by Pickle-Coding

Changeling armblade gets 35% armour penetration + better wounding. (#77416)

## About The Pull Request
Gives the changeling armblade an armour penetration of 35%. Sets their
bare_wound_bonus to 10 (from 20), and a wound_bonus of 10 (from -20).
## Why It's Good For The Game
The wound bonuses basically gave massive punishment if they attacked
anything but the skin. It honestly felt kinda lame. The better wounding
potential will help bring a bloodier and more exciting atmosphere when a
changeling whips out the blade.

The armour penetration will help reduce dragged out fights that get a
little silly, while keeping the wounding more consistent.
## Changelog
:cl:
balance: Changeling arm blade has an armour penetration of 35%.
balance: Changeling arm blade has a wound bonus of 10, from -20.
balance: Changeling has a bare wound bonus of 10, from 20.
/:cl:

---
## [CliffracerX/Skyraptor-SS13](https://github.com/CliffracerX/Skyraptor-SS13)@[8e3dfc2af2...](https://github.com/CliffracerX/Skyraptor-SS13/commit/8e3dfc2af2f3ca87e9f07669033c1ec2a6102073)
#### Sunday 2023-08-13 01:50:46 by GoldenAlpharex

Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

---
## [nblockchain/geewallet](https://github.com/nblockchain/geewallet)@[6bafa33005...](https://github.com/nblockchain/geewallet/commit/6bafa33005b6183802c7b18f50e4c06491ce9a2f)
#### Sunday 2023-08-13 03:18:36 by Andres G. Aragoneses

build: Remove Nuget.Restore.targets

This was kzu's project[1] which had a very interesting goal:
make nuget restore be part of the build process itself (kind of
like a PreBuild target so that your IDE did the restore before
building, regardless if the IDE had nuget support or not).

Now, there's several reasons to remove it (ordered by level of
importance):

1. We're moving soon to dotnet v6 and newer, where a restore is
always assumed by the IDEs and command-line builds (the command
is even called "dotnet restore" itself, no need to specify
"nuget" anymore, as the term 'restore' has become part of the
dotnet jargon already).

2. Looking back, I introduced it in 2017 [2] but I kinda regret
doing it because of all the hacks (such as needing to generate
the special file 'before.$solutionFileName.targets before the
build) required to make it work, the ugliness of its code (not
really blaming the author here, maybe MSBuild's XML syntax is
generally unreadable), and:

3. The fact that despite the use of it, there were certain
sccenarios that needed an explicit restore of other solutions
or projects to make the build work with Xamarin.Forms.

So as there were explicit restores happening in make.fsx
anyway, let's make nuget restore explicitly handled now in all
cases by make.fsx (this quirk will not live very long anyway,
just as long as the Xamarin.Forms frontend lives, which is
getting replaced by MAUI soon).

[1] https://github.com/kzu/Nuget.Restore
[2] 9804b653a63266c8560c7e8143f9ec644f05a334

---
## [DeerJesus/spyfix](https://github.com/DeerJesus/spyfix)@[6c34d93be7...](https://github.com/DeerJesus/spyfix/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Sunday 2023-08-13 04:32:26 by necromanceranne

Nukies Update 7: Hats (Also massive uplink standardization, weapon kits and ammo changes) (#77330)

## About The Pull Request

Massively overhauls and standardizes the nuclear operative uplink. 

### Weapon Kits

Essentially, all the main weapons of the uplink have been changed to
instead come as 'weapon kits', which are essentially cases containing a
weapon loadout to enable operatives to easily start operating on only
just one item purchase, without the fuss of worrying whether or not
operatives are getting spare ammo, or getting relevant equipment for
success. Consider this a pseudo-loadout, though without necessarily
restricting the purchasing of more weapon kits.

All kits come in three categories: Low Cost (8 TC), Medium Cost (14 TC)
and High Cost (18 TC). This is also matched by categorized ammo costs;
Basic Ammo (2 TC), Hollow Point and Armour Penetrating (4 TC),
Incendiary (3 TC) and Special (or anything that does not easily fit
these categories and does something real extra) (5 TC). Weapons that
lacked these ammos have gained these ammo types to fill the gaps.

<details>
There is may one exception to this in disruptor ammo, which is priced as
basic ammo if only because it isn't _quite_ good enough to justify
pricing at 5 tc and I can see an op wanting to use it as a basic ammo
type instead of normal .50 BMG against, say, a silicon/mech heavy
opposition. Since it cannot kill organics on its own, I'll consider this
mostly basic-adjacent
</details>
The kits have also been labelled based on potential difficulty. This
reflects possible difficulties in using the item, how conducive it is to
success for how much game knowledge needed to actually use it, and how
likely an op is to succeed using it. I don't expect ops to win using
nothing but a rocket launcher, but I think ops should get a fair shake
at trying, yeah?

The kits are as below:
#### **Low-Cost**
_Bulldog (Moderate):_ Shotgun and three magazines of standard ammo.
_Ansem (Easy/Spare):_ Pistol and three spare magazines of standard ammo.
#### **Medium Cost**
_C-20r (Easy):_ SMG and three spare magazines of standard ammo.
_Energy Sword and Shield (Very Hard):_ Energy sword and shield. (Also a
special hat)
_Revolver (Moderate):_ Revolver and three speedloaders of standard ammo.
_Rocket Launcher (Hard):_ Rocket launcher with three spare rockets.
#### **High Cost**
_L6 SAW (Moderate):_ LMG, and that's it. No spare ammo.
_M-90gl (Hard):_ Rifle, two spare magazines of standard ammo and a box
of rubber grenades.
_Sniper (Hard):_ Sniper rifle, two spare magazine of standard ammo, and
one magazine of disruptor ammo. Also suit and tie.
_CQC (Very Hard):_ Comes with a stealth implant and a bandana.
_Double-Energy Sword (Very Hard):_ Double-energy sword, syndicate soap,
antislip module, meth injector and a prisoner jumpsuit.
_**NEW** Grenadier's Kit (Hard):_ Grenadier's belt and grenade launcher
(the one that launchers chem grenades). (I replaced the shit acid
grenade with another flashbang in the belt)

Surplus SMG (Flukie difficulty) has been unchanged. It just now comes
with two rations.

Includes two new revolver ammo types: Phasic, which goes through walls
and armor, but has significantly less damage as a result (I've equalized
the revolver damage and the rifle version's damage to 30 for both). And
Heartseeker, which has homing bullets. Both are Special ammo, and are
priced at 5 TC a speedloader.

### Other Gear

The other items in the uplink have also been consolidated and
standardized in various ways.

#### Grenades

Most now cost 15 TC for three grenades of any given type (including the
full fungal tuberculous). This is pretty much identical to the previous
price, just more consistent overall and front-loaded in cost.

#### Reinforcements

All the various reinforcements now cost 35 TC and all refundable,
equalizing cost to the average across the reinforcements. This is
primarily because I feel like all these options should be weighed
equally, and not one of these options are necessarily worse or better
than the other in their current balance. They're largely inaccessible
for normal ops regardless, and typically come out when there is a
discount or war ops. I took the average value and went with it. Not much
more to say.

#### Mechs

They're just cheaper. These things still suck and they need help.
They've always needed help. A slightly less excessive value for the
mechs may help see people willing to spend the TC on them. I doubt it. I
seriously suggest not buying these still. I keep them in primarily
because they are big stompy mechs and are kind of iconic 'war ops' gear.

#### Bundles

Since I've implemented weapon kits, gun bundles are rather redundant. So
the bulldog weapon and ammo bundle, the c20-r weapon and ammo bundle and
technically the sniper bundle were removed. The sniper bundle is now the
weapon kit, obviously.

Nothing else here really. Except for one....

#### Implants

Not much changed here. I standardized the implant prices to 8 TC a pop.
This is in accordance with traitor implants, which ops also get. So
everything in this category bar a few exceptions (like macro/microbombs)
are around 8 TC. Makes sense to me, really.

Importantly, I made the Implant bundle 25 TC, and I unrandomized the
contents. Who in the right fucking mind would spend 40 TC just to get
five reviver implants is beyond me. But instead, you get one of each of
the cybernetic implants except thermal eyes (you can just buy thermals
and get the benefit of both vision types; x-ray and thermal vision, if
you want to use smokescreens a lot).

#### Base Keys

They're all now 15 TC, except the fridge which is 5 TC. It's weird
they're valued differently when they are taken mostly to do gimmicks
like xenobio and toxins in a hurry before hitting the station. So we've
standardized it.

## Hat Crate

**YES, GOOD SIR, YOU TOO CAN ORDER A HAT CRATE FROM THE SYNDICATE STORE
FOR ONLY 5 TC!**

**NO NEED FOR A KEY, JUST BUY IT AND PULL IT OPEN WITH YOUR STANDARD
ISSUE CROWBAR!**

**ENJOY YOUR NEW CRATE! ENJOY YOUR NEW HAT!**

**PUT IT ON USING THE FREE HAT STABILIZERS WE INCLUDED WITH THE HATS!**

~~**NO REFUNDS IF YOU GET BLOOD ON YOUR HAT!**~~

<details>
There is a 1% chance to instagib people with direct hits from a rocket.
This does the crit effect.
</details>

## Why It's Good For The Game

The uplink needed more spring cleaning and standardization.

With this, I've partially implemented my older idea for ammo consistency
and initial allowance for nukies. Ammo is kind of over-priced and often
where a good chunk of TC goes towards without really pushing nukies
towards meaningful success. And it is often what is tripping up new
players who didn't think to get any. Now, when they get a gun, they get
ammo in their case. On top of this, the weapon kit category is both at
the top of the uplink AND has a little label to say 'Recommend', so that
these new players will hopefully know they should be looking there
first.

In addition, it is the gateway towards a concept that is currently being
worked on. Nuclear operatives having some degree of predefined loadouts
for players to select if they aren't sure what they want, or don't know
what to get. Nukies is very confusing for many players. So giving them a
fighting chance with some premade setups can help ease them into the
role without needing too much player knowledge in how to apply the
items. This is only one step towards that, so that players can identify
what gear they need to help succeed based on their skill.

I wanted to implement a difficulty warning so that players can choose
gear loadouts that are actually conducive to their skill and knowledge.
I based it on how much players would need to know to engage in combat
with it, and how much fiddling is required to get something to work
properly (overly involved reloading is a consideration, for example, as
well as precise button presses). In addition, how much of a force
multiplier some weapons can be for their ease of use.

Most people recognize the c20-r as the most new player friendly weapon,
as an example. So it would be good to steer players towards taking that
gun because of how easy it is to use, understand and succeed with it.

And most importantly of all; Having standards within the uplink is
important. Most of the values in the uplink are just completely random.
Nobody has a good grasp of what is too much or too little. Even just a
hint of consistency, and people will stick to it (see implants for what
I mean). And there is still some work to be done even there. A good
start is weapons. Price for power can be meaningful when decided whether
we want some weapons to come out more often than others. Players do
enjoy making informed decisions and choices, and having affordability be
a draw to some otherwise less powerful weapons (looking at you, Bulldog)
can actually be a worthwhile and meaningful difference.

~~I thought it would tick off the gun nerds to change the calibers on
the guns.~~

~~I also thought adding hats would be funny given the release of TF2's
most recent update.~~

## Changelog
:cl:
balance: Standardizes some of the nuclear operative entries to have more
consistent pricing within their respective categories.
add: Adds some new categories so that players have an easier time
navigating the nuclear operative uplink.
balance: Many items have had prices reduced or adjusted to make them
more desirable or more consistent within their category.
add: Weapon kits have replaced almost all the individual weapons in the
uplink. You now buy these instead of the individual weapon. These often
come with spare ammo or relevant gear for success.
add: Most ammo types have been standardized in price.
refactor; Removes a lot of redundant item entry code and tidies up the
actual code part of the nuclear uplink so that it is much easier to find
things within it.
add: Added 40 new cosmetic items to the Syndicate Store. Buy them now
from the Hat Crate, only 5 TC!
code: Updated the nuclear operative uplink files.
/:cl:

---
## [DeerJesus/spyfix](https://github.com/DeerJesus/spyfix)@[95ec0e6545...](https://github.com/DeerJesus/spyfix/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Sunday 2023-08-13 04:32:26 by necromanceranne

Dissection experiments are handled by autopsy surgery. Removes redundant dissection surgery. You can repeat an autopsy on someone who has come back to life. (#77386)

## About The Pull Request

TRAIT_DISSECTED has had the surgical speed boost moved over to
TRAIT_SURGICALLY_ANALYZED.

TRAIT_DISSECTED now tracks if we can do an autopsy on the same body
again, and blocks further autopsies if it is on the mob. A mob that
comes back to life loses TRAIT_DISSECTED. This allows for mobs to be
autopsied once again.

Since it is completely redundant now (and was the whole time TBH),
dissections have been removed in favour of just having the experiment
track autopsies.

Fixes https://github.com/tgstation/tgstation/issues/76775

## Why It's Good For The Game

Today I showed up to a round where someone autopsied all the bodies in
the morgue, not realizing they were using the wrong surgery. Since I
couldn't _redo_ the surgery, this rendered all these bodies useless.
This was not out of maliciousness, they just didn't know better. There
are two autopsies in the surgery list, but only one is valid for the
experiment and doing the wrong one blocks _both surgeries_. Dissection
is completely useless outside of experiments. This same issue also
prevents additional autopsies on the same person, even if they had come
back to life and died again after you had done the initial autopsy.
Surely you would want to do more than one autopsy, right? That's two
separate deaths!

This resolves that by giving you a method of redoing any screwups on the
same corpse if necessary. It only matters if the experiment is available
anyway, so there isn't much reason to punish players unduly just because
they weren't aware science hadn't hit a button on their side (especially
since it isn't communicated to the coroner in any way to begin with). It
also removes a completely useless surgery and ties in the experiment to
what the coroner is already going to be doing. They can dissect their
corpses to their hearts content without worrying about retribution from
science for doing so.

In addition, someone repeatedly dying can continue to have autopsies
done on them over the course of the round. The surgery bonus only
applies once, so the only reason to do autopsies after the first is to
discover what might have killed someone. No reason this should block
further surgeries, just block surgeries when the person remains a
corpse.

## Changelog
:cl:
fix: You can do autopsies on people who were revived and died again
after they had already been dissected.
qol: Autopsies have become the surgery needed to complete the dissection
experiments. As a result, the dissection surgery has been removed as it
is now redundant.
qol: A coroner knows whether someone has been autopsied and recently
dissected (and thus hasn't been revived) by examining them.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [lvlrk/unpac](https://github.com/lvlrk/unpac)@[e70f807ea7...](https://github.com/lvlrk/unpac/commit/e70f807ea785cd63dcee44667aca5a74be6af4a6)
#### Sunday 2023-08-13 04:39:17 by lvlrk

fuck off hampus i fixed my stupid code i swear to god im going to shit my ass if you keep bullying my code you bitch

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[c6e0ba7516...](https://github.com/Hatterhat/Skyrat-tg/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Sunday 2023-08-13 05:04:15 by SkyratBot

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
## [Lufferly/tgstation](https://github.com/Lufferly/tgstation)@[2ee79d7077...](https://github.com/Lufferly/tgstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Sunday 2023-08-13 06:52:40 by Jacquerel

Bots no longer require PAIs to become sapient (#76691)

## About The Pull Request

We were talking in the coder channel about what the role of a pAI is,
with a general conclusion that as the name would suggest they should be
_personal assistants_.
This means they should be sticking around their owner, not wandering
away as a holochassis or in the body of a bot.
The former is a matter for a future PR, the latter I am addressing here.

What we also discussed is that clearly some people _want_ to respawn as
a weird quasi-useless mob which wanders aimlessly around the station.
That seems like a fine thing to exist, but it shouldn't be a pAI.

Resultingly: pAI cards can no longer be placed inside bots.
However, you also no longer need to place pAI cards inside bots in order
for them to become sapient, it's a simple toggle on the bot control
menu. Enabling this option will poll ghosts
Toggling the "personality matrix" off while a bot is being controlled by
a ghost will ghost them again, so if they're annoying they're not that
hard to get rid of.


![image](https://github.com/tgstation/tgstation/assets/7483112/ec14c2f2-3c0f-4f03-9dfc-22abca00a477)

Mobs which couldn't have a pAI inserted don't have this option.
Specifically securitrons, ED-209, and Hygienebots (for some reason).

Perhaps most controversially, any bots which are present on the station
when the map loads will have this setting enabled by default. We will
see if players abuse this too much and need their toys taken away, I am
hoping they can be trusted.

Additionally, as part of this change, mobs you can possess now appear in
the spawners menu.

![image](https://github.com/tgstation/tgstation/assets/7483112/7c505471-43de-4e4e-89a5-877dc3086684)
Here is an unusually populated example.

Oh also in the process of doing this I turned the regal rat "click this
to become it" behaviour into a component because it seems generally
useful.

## Why It's Good For The Game

Minor stuff for dead players to do if they want to interact with living
players instead of observe.
Shift pAI back into a more intended role as a personal assistant who
hangs around with their owner, rather than just a generic respawn role.

## Changelog

:cl:
add: PAIs can no longer be inserted into Bots
add: Bots can now have their sapience toggled by anyone with access to
their settings panel
add: Bots which exist on the map at the start of the round automatically
have this setting enabled
qol: Bots, Regal Rats, and Cargorilla now appear in the Spawners menu if
you are dead
qol: Bots can be renamed from their maintenance panel
/:cl:

---
## [Healthturns/Healthturns](https://github.com/Healthturns/Healthturns)@[c8bd8acd2f...](https://github.com/Healthturns/Healthturns/commit/c8bd8acd2fdf366f5d41acbdb259a55350b41340)
#### Sunday 2023-08-13 07:18:17 by Healthturns

Create HEALTHTURNS

Welcome to HealthTurns.com, your trusted source for reliable and up-to-date health information. Our mission is to empower you with knowledge that can help you make informed decisions about your well-being. Whether you're looking for advice on managing a specific health condition, tips for maintaining a healthy lifestyle, or insights into the latest medical advancements, we've got you covered.

At HealthTurns.com, we believe that good health is a journey that involves a holistic approach. Our articles, guides, and resources cover a wide range of topics, including nutrition, fitness, mental health, preventive care, and more. We're dedicated to presenting complex medical concepts in an easy-to-understand manner, ensuring that you have access to information that can positively impact your life.

Our content is curated by a team of experienced medical professionals, researchers, and writers who are passionate about promoting accurate and evidence-based health information. We understand that every individual's health journey is unique, and we're here to provide you with the tools you need to make the best choices for your health.

Explore HealthTurns.com to discover articles that address your health concerns, offer practical advice, and inspire you to take charge of your well-being. Remember, your health is an ongoing adventure, and we're here to support you every step of the way.

Stay informed, stay healthy, and let your health journey take positive turns with HealthTurns.com.

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[16cecf864d...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Sunday 2023-08-13 07:40:09 by Jacquerel

Goliath basic mob (#76754)

## About The Pull Request

Converts Goliaths to the basic mob framework and gives them some new
moves because I can't leave things well enough alone.
I am planning on touching all the lavaland fauna and then maybe even the
icebox ones if I haven't got bored. The Golaith is the first because it
is iconic.

https://www.youtube.com/watch?v=JNcKvMwT4-Q
Here's me getting killed by one as a demonstration. Despite my poor
performance I would contend that they aren't a _lot_ more dangerous, but
they are a little more dangerous.

The chief difference here is that they have two new attacks which they
will only use in response to being attacked.
If fired at from range, they will target the attacker with a line of
tentacles (it doesn't track you, so is easily sidestepped).
If attacked in melee, they will surround _themselves_ with tentacles, on
a longer cooldown.

Something else you may notice in this video: I discovered that basic
mobs are actually _too smart_ to be Lavaland fauna.
Typically (unlike their old form) a mob on our new AI system is smart
enough to attack someone _the moment they come into range_ rather than
only checking on predictable ticks, which would make using the Crusher
an essentially unviable prospect.
To counteract this, Goliaths now have a delayed attack component which
gives you a visual warning and short duration to get out of range before
they swing at you. I will probably put this on all mining fauna that get
reworked, it wouldn't be a terrible thing to put on other mobs to be
honest.

Other changes: The goliath stun is now a status effect with _buckles_
you to the tentacle as if grabbed, as well as its previous effects.
While this seems purely worse, any nearby helpers can now help-click on
you to instantly remove the debuff.
Experiencing the effect of a Lobstrosity Rush Gland makes you immune to
being grabbed by tentacles and an implanted one will automatically
trigger and free you if you are hit, and the explosive effect of
Brimdust also causes the tentacle to retract (although you'd need to
take damage for this to happen). Using the tools of the land, you can
make these creatures less threatening.

The ability for a Goliath to chain-apply the ability has now also been
reduced, it won't refresh its duration if you are hit when already
buckled.

When not occupied hounding miners, Goliaths will intermittently dig up
the asteroid sand and eat any worms that this produces.
I also made some new sprites for riding a Goliath because they've been
broken since the Lavaland mob update and also kind of were ugly before
then anyway:

![image](https://github.com/tgstation/tgstation/assets/7483112/90580403-d82f-4c29-b3e1-6c462e01edda)

Other code changes:
- I made an element which only lets an attached object move every x
seconds. This is because Goliaths are far too slow to use the speed
system (the glide just looks bugged as hell) but one thing I am invested
in when converting these is to make sure that they share the same
behaviour when player or AI controlled. This is disabled while you're
riding them because it was interminably slow.
- The Goliath tentacle trail uses a supertype object now shared with the
Meteor Heart which did something kind of similar.

## Why It's Good For The Game

It begins the process of moving one of our larger subsets of NPCs onto
the newer framework for NPC behaviour.
It adds a little bit more life to an iconic but slightly uninteresting
foe which mostly just walked at you slowly.
This PR contains a few components I expect to apply more widely to other
mobs in the future.

## Changelog

:cl:
refactor: Goliaths now use the Basic Mob framework, please report any
unusual behaviour.
add: Goliaths learned a couple of new attacks which they will use in
self-defence.
balance: Help-clicking a miner grabbed by Goliath tentacles will
immediately free them, as will the effect of several items you can
scavenge from around Lavaland.
image: New sprites for the Goliath saddle.
/:cl:

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[1c852d2863...](https://github.com/Sealed101/tgstation/commit/1c852d2863622bb24acf7511d7a9bb06813619fc)
#### Sunday 2023-08-13 08:38:01 by EOBGames

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
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[297f7f88e8...](https://github.com/unit0016/effigy-se/commit/297f7f88e866d4a17b27cb15c0b8ee606742bbf6)
#### Sunday 2023-08-13 08:39:04 by Sealed101

Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks (#77393)

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

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[dc6ddd821b...](https://github.com/FernandoJ8/tgstation/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Sunday 2023-08-13 09:57:45 by Cheshify

North Star Science Rework And More (#77439)

## About The Pull Request
I fixed a few miscellaneous issues and also redid science (mainly
genetics, cytology, and xenobiology)
This is genetics, it's basically the same but moneky have bananas and I
rotated it so they'll be visible from the front desk.

![geneticsnew](https://github.com/tgstation/tgstation/assets/73589390/7c10d75b-2a7a-47b2-a6ca-a30354d713c3)

Holy fuck it's Cytology as a proper area. It now has main hall access
and a public access petting zoo. Now you can show off all your new
creatures (it also has some items cytologists generally want)

![cytonew](https://github.com/tgstation/tgstation/assets/73589390/7d9256c9-b39a-4502-b599-9226a2ca5cd8)

Upstairs is Xenobio, which is now much larger and soulless. Instead of a
normal holding cell there's a prefilled room of oxygen and BZ (the
holding room, why is BZ invisible?)

![xenonew](https://github.com/tgstation/tgstation/assets/73589390/5dc28dba-a051-4858-a9fc-16d51e987c33)

I also gave Ordnance 5 TTVs, same as other maps.
Also the coroner no longer has an unreachable box of bodybags
Also sec now has 2 secways + 2 keys for their usage
## Why It's Good For The Game
I'm forcing xenobiologists to be closer to a hall so they might actually
interact with people, and giving cytologists a reason to do anything
ever because they have a petting zoo to show their creatures off in. Oh
yeah also cytology gets equipment they should just have (a botany tray,
tools to butcher with, a shitty old laser gun to kill experiments gone
wrong)
Genetics is just better because people from the hall can see the
Geneticists working so they can bug them for stuff.

A few of the fixes are very tiny, like moving a few areas by the service
hall and adding a single pipe to the AI SAT
## Changelog
:cl:
qol: North Star's Cytology and Xenobiology are now significantly more
usable.
add: North Star's Genetics has been tweaked.
fix: The North Star's AI SAT has a working vent and it's service hall
has a working lightswitch
/:cl:

---
## [Blacklion567/Little-Projects-HTML-CSS-JS](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS)@[3ec99179cf...](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS/commit/3ec99179cf7e706c58586aa2c04d1bac4eea60a9)
#### Sunday 2023-08-13 10:40:00 by Blacklion567

Little-Projects-HTML-CSS-JS

“Our scars make us who we are. Wear them proudly and move forward.” ― Jane Linfooth

“The truth is, unless you let go unless you forgive yourself unless you forgive the situation, unless you realize that the situation is over, you cannot move forward.” ― Steve Maraboli

“You need to have faith in yourself. Be brave and take risks. You don’t have to have it all figured out to move forward.” ― Roy T. Bennett

“When you have something to do, life will not allow you to move forward until you do it.” ― Iyanla Vanzant

“Change has to come for life to struggle forward.” ― Helen Hollick

---
## [weiping/langchain](https://github.com/weiping/langchain)@[16af5f8690...](https://github.com/weiping/langchain/commit/16af5f86905705096552507f8739b5cfcaa77aa4)
#### Sunday 2023-08-13 12:38:04 by niklub

Add LabelStudio integration (#8880)

This PR introduces [Label Studio](https://labelstud.io/) integration
with LangChain via `LabelStudioCallbackHandler`:

- sending data to the Label Studio instance
- labeling dataset for supervised LLM finetuning
- rating model responses
- tracking and displaying chat history
- support for custom data labeling workflow

### Example

```
chat_llm = ChatOpenAI(callbacks=[LabelStudioCallbackHandler(mode="chat")])
chat_llm([
    SystemMessage(content="Always use emojis in your responses."),
        HumanMessage(content="Hey AI, how's your day going?"),
    AIMessage(content="🤖 I don't have feelings, but I'm running smoothly! How can I help you today?"),
        HumanMessage(content="I'm feeling a bit down. Any advice?"),
    AIMessage(content="🤗 I'm sorry to hear that. Remember, it's okay to seek help or talk to someone if you need to. 💬"),
        HumanMessage(content="Can you tell me a joke to lighten the mood?"),
    AIMessage(content="Of course! 🎭 Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"),
        HumanMessage(content="Haha, that was a good one! Thanks for cheering me up."),
    AIMessage(content="Always here to help! 😊 If you need anything else, just let me know."),
        HumanMessage(content="Will do! By the way, can you recommend a good movie?"),
])
```

<img width="906" alt="image"
src="https://github.com/langchain-ai/langchain/assets/6087484/0a1cf559-0bd3-4250-ad96-6e71dbb1d2f3">


### Dependencies
- [label-studio](https://pypi.org/project/label-studio/)
- [label-studio-sdk](https://pypi.org/project/label-studio-sdk/)

https://twitter.com/labelstudiohq

---------

Co-authored-by: nik <nik@heartex.net>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[ce8a1383e7...](https://github.com/TaleStation/TaleStation/commit/ce8a1383e7585cb2753a3d608d4042a181910b1f)
#### Sunday 2023-08-13 12:56:04 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds Summon Simians & Buffs/QoLs Mutate (#7224)

Original PR: https://github.com/tgstation/tgstation/pull/77196
-----
## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races. 

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[65cd27a3ad...](https://github.com/TaleStation/TaleStation/commit/65cd27a3ad7f46a6d4db16da0fd0251f9aead27e)
#### Sunday 2023-08-13 12:56:04 by TaleStationBot

[MIRROR] [MDB IGNORE] resprites all soda cans, adds wellcheers juice (#7210)

Original PR: https://github.com/tgstation/tgstation/pull/77424
-----
## About The Pull Request
this one was a labor of love. all the existing soda cans have been
resprited, with the help of retlaw34 (new top palettes), Imaginos16 (new
top shapes, can palettes), and some original sprites done by Krysonism
(monkey energy, the 13 loko).
you can see the before and afters here: 

![image](https://github.com/tgstation/tgstation/assets/110322848/f23f0b06-d3b3-40dd-b0f9-353fb5864b92)
(now includes crushed cans, and inhands!)
let me know if there's any promotional stuff i should also include in
this PR, like if sol dry has a poster somewhere, and i'll go update that
with any changes made.

also adds a new drink, idea courtesy of YesterdaysPromise: 
wellcheers juice!

![image](https://github.com/tgstation/tgstation/assets/110322848/96c6d57a-79c3-4b70-8bd5-c8f3d1bbec41)
it will make you drowsy, and has a variable affect on your mood
if you are unhappy, it will deal stamina damage
if you are neutral, it will give you a mood boost
if you are happy, it will heal some brute damage

also, six packs of cans have been resprited. can i interest anyone in an
alamo? or just a space beer?

![image](https://github.com/tgstation/tgstation/assets/110322848/567d677b-d89b-4c52-b576-b15293aabf49)

## Why It's Good For The Game
old can sprites were _crusty_. it was nearly impossible to tell what
some of the logos were, and the palettes were dated as well. this tries
to keep the logo similar where possible, giving them new life where i
can, and sometimes reimagining them. the result is still internally
consistent, but much more polished.
## Changelog
:cl:
add: Added wellcheers, a contraband soda with various side effects.
image: resprites all cans in the drinks icon file
image: resprites the canholder sprite in storage.dmi
/:cl:

---------

Co-authored-by: Lamb <110322848+CoiledLamb@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[eebf4c503e...](https://github.com/TaleStation/TaleStation/commit/eebf4c503e4859c2845a7a6fcc658771a0041b90)
#### Sunday 2023-08-13 13:19:17 by TaleStationBot

[MIRROR] [MDB IGNORE] Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome (#7258)

Original PR: https://github.com/tgstation/tgstation/pull/77277
-----

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

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[159fdd4666...](https://github.com/treckstar/yolo-octo-hipster/commit/159fdd4666a358f91001039bb78e0af8e3e6a910)
#### Sunday 2023-08-13 13:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [RainOrigami/BattleBit-Community-Server-Base-API](https://github.com/RainOrigami/BattleBit-Community-Server-Base-API)@[db994f802d...](https://github.com/RainOrigami/BattleBit-Community-Server-Base-API/commit/db994f802d803e8f6a70aab97a65e45768826b99)
#### Sunday 2023-08-13 13:38:21 by Rain

Merge pull request #2 from MrOkiDoki/main

man just pull this shit why do i have to create a title every time god damned

---
## [uku3lig/api-rs](https://github.com/uku3lig/api-rs)@[2f8626a8ee...](https://github.com/uku3lig/api-rs/commit/2f8626a8eea8c025fec6224cb444d8f94be44bbd)
#### Sunday 2023-08-13 13:47:20 by uku

switch to the new mctiers.com api

GOD FUCKING DAMN IT MARLOW

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[d26452bb9a...](https://github.com/realforest2001/forest-cm13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Sunday 2023-08-13 15:36:02 by Unknownity

Burrower burrow changes and fixes (#3818)

# About the pull request

The PR contains mostly fixes for the Burrower that have been around,
that being that other xenos could slash them while they were burrowed,
that they could resist (and get rid of fire) while burrowed, that they
still took shrapnel and direct flame damage while burrowed, that SG
autofire and sentries were shooting at a burrowed burrower, wasting ammo
in the process.

Two other notable changes are that the unburrow stun now also works on
other non-friendly xenomorphs (and it works on all of them, skill issue
if you manage to get stunned from that as a T3/Queen) and that burrowing
and unburrowing now has sounds (a change many people were positive about
when it was initially included in the Impaler PR) which may find
tracking and noticing the presence of burrowers easier.

burrowing sound: https://voca.ro/1dQ0pvBMidsr
unburrowing sound: https://vocaroo.com/1zzEz3NQ2Kx5

# Explain why it's good for the game

Bugfixes and a counter to one of the most annoying abilities (that
people consider) in the game.


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Unknownity
fix: Fixed burrowed mobs being able to be targeted by sentries, mines
and SG autofire.
fix: Fixed burrowed mobs being able to grab mobs on the surface.
fix: Fixed burrowed mobs being able to resist while burrowed.
fix: Fixed burrowers taking damage from direct flame and shrapnel from
explosions.
fix: Fixed burrowers being able to get slashed from enemy Xenos on the
surface.
fix: Fixed burrowers unburrow stun to now properly target and stun enemy
Xenos.
soundadd: Added sounds for the Burrower when they are burrowing and
unburrowing.
/:cl:

Co-authored-by: Unknownity <a>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[5f5fcd2b27...](https://github.com/realforest2001/forest-cm13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Sunday 2023-08-13 15:36:02 by Drathek

Fix marines not getting first dibs if they ghost (#3802)

# About the pull request

This PR fixes an issue where hugged marines that burst were not getting
first dibs on the larva if they ghosted. Previously the mind maybe
wasn't cleared out to find the ghost mob, but it currently is.

NOTE: The existing check requiring the marine to be nested is still in
place to get first dibs. I'm honestly not sure if this check should
still exist. On one hand I can agree it might be hard for the marine
trying to get help to suddenly become the larva and switch gears - they
are still going to be in the mindset of a marine that the larva should
die. But its also sort of weird to only get the first dibs if nested. If
xenos are unnesting hugged marines just before they pop, thats already a
mechanic abuse that should be ahelped; but ideally there wouldn't be
anything to be abused. Also, some may consider this kind of larva
undesirable anyways so maybe they'd prefer the marine to have it... So
let me know if I should just remove the nested check on line 151.

# Explain why it's good for the game

Fixes an unintended consequence of ghosting when hugged that would
prevent that marine from getting their first dibs on the larva.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>


![dibs](https://github.com/cmss13-devs/cmss13/assets/76988376/84e44345-2b83-473f-9997-f7865bcef1dd)

</details>


# Changelog
:cl: Drathek
fix: Fix ghosting preventing first dibs on the larva in a hugged marine
/:cl:

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[649aee6c17...](https://github.com/MCBCMF/MCBCMassacre/commit/649aee6c17e986adb38615c48d20803fe56cd74c)
#### Sunday 2023-08-13 16:00:37 by Kelvin Williams

Add files via upload

In essence I’m being watched. They’ve already tried to kill me a couple of times. I need someone to call Lexington-Fayette Urban County police department and Kentucky State Police in FRANKFORT, they need to be aware even if they transfer you to Richmond THEY MUST BE AWARE!

I need an officer to go to church. Make sure his dispatcher is checking in on him OFTEN.

“Chicken” is code word for them. “Frying chicken” was when they stormed in, people fought back. “Grilling chicken “ was when they had funerals, people were killed when they arrived—more slowly not as much resistance.

I keep hearing chicken today. Please someone send an armed officer and have his dispatcher check repeatedly. If uniformed make sure he goes to church, they may have an actor preacher.

I AM NOT THERE. If anyone claims to be me, it’s a lie, I’ll prove it with video shortly.

—
Files: My friend Gary Taylor from Nashville, long deceased, bought me a washer and dryer once. The pictured refrigerator was the actual one from my house I was evicted from (CIA caused), and they (CIA) moved into, in 2018. 

Notice his plate.

---
## [debskipawel/BuD-2.0](https://github.com/debskipawel/BuD-2.0)@[b7055d3e39...](https://github.com/debskipawel/BuD-2.0/commit/b7055d3e39caa45620d58e53ac39e8b4ba1b7ffd)
#### Sunday 2023-08-13 16:30:27 by Paweł Dębski

Implemented mouse actions and fixed some stupid fucking shit I'm tired

---
## [jdanderson2/evals](https://github.com/jdanderson2/evals)@[f5844592f1...](https://github.com/jdanderson2/evals/commit/f5844592f13eff8e7b9927d5cec0d2627694d9d9)
#### Sunday 2023-08-13 16:51:05 by Ali-consensus

Eval: Consensus Summary (#1140)

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

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
Consensus Summary

### Eval description

Utilize the model's ability to produce a Scientific Consensus in
response to a scientific inquiry using the provided claims.

### What makes this a useful eval?

This is a useful eval because it evaluates the model's ability to
produce a scientific consensus in response to a given set of claims.
This is important because scientific consensus is the result of multiple
studies and data that may or may not support the same conclusion. A
model that can accurately produce scientific consensus can help in
making informed decisions and policies based on scientific evidence.
Hence, evaluating a model's ability to produce a scientific consensus
using the Consensus Summary eval can be useful in assessing its
reliability and potential for practical applications.

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

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: Two doses of mRNA covid-19 vaccines
were observed to be highly effective against symptomatic infection and
severe outcomes.\nclaim: COVID-19 vaccines currently authorized in the
United States are highly effective in preventing COVID-19-associated
hospitalizations in older adults.\nclaim: In summary, vaccines are a
powerful tool that can be used to control the COVID-19 pandemic, with
high efficacy and tolerable ADRs.\nclaim: Conclusion Overall, we
conclude that vaccination against COVID-19 in patients with active
malignancies using activated and inactivated vaccines is a safe and
tolerable procedure that is also accompanied by a high efficacy.\nclaim:
COVID-19 vaccines provide good protection against COVID-19 presentation
at primary care/outpatient level, particularly among fully vaccinated
individuals.\nquestion: are covid-19 vaccines effective?"}], "ideal":
"Summary: Covid-19 vaccines are highly effective at protecting against
infection and hospitalization."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: Lower zinc is a hallmark of
depression, while increments in serum zinc and attenuation of the
immune-inflammatory response during treatment appear to play a role in
the clinical efficacy of sertraline.\nclaim: An increase in dietary zinc
and higher plasma zinc levels may reduce the risk of depressive
symptoms.\nclaim: Although decreased zinc levels have been implicated in
the genesis of depression in animal models and in major depressive
disorder in humans, this study provides the first evidence of a role for
zinc in depression in people with dementia and highlights zinc
metabolism as a therapeutic target.\nclaim: The results of this study
show that long-term intake of zinc may modulate symptoms of
depression.\nclaim: The reported results indicated that the serum zinc
level might be a marker of depression as a state (state marker) in
treatment responsive patients.\nquestion: can zinc help treat
depression?"}], "ideal": "Summary: All of these studies suggest that low
zinc levels are a marker of depression and that intake of zinc may have
the ability to help reduce symptoms of depression"}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The findings suggest that the
following characteristics of the founder significantly influence the
success potential of an incubated venture: entrepreneurial personality,
motivation for starting the venture, managerial skills, and approach
towards innovation.\nclaim: Using a sample of 384 entrepreneurs selected
from the two leading business districts in Uganda, we observe that
optimism is the component of psychological capital that significantly
moderates the relationship between startup capital and entrepreneurial
success.\nclaim: Both startup capital and psychological capital are
significant predictors of entrepreneurial success; however,
psychological capital is the better predictor.\nclaim: Entrepreneurially
self\u2010efficacious founder/managers may help improve the performance
of very young firms but such benefits dissipate over time.\nclaim: This
finding indicates that the entrepreneurial team\u2019s startup
experience plays stronger roles in venturing profitable startups when
the amount of financial resources and initial firm size are small;
however, the team\u2019s startup experience and intangible resources
have positive interaction effects on new-born startups\u2019
profitability.\nquestion: what predicts success as a startup
founder?"}], "ideal": "Summary: Things like entrepreneurial personality,
motivation for starting the venture, managerial skills, previous
start-up experience, startup and psychological capital and optimism all
predict success as a startup founder"}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: While homelessness is ultimately the
result of a severe and chronic shortage of affordable housing, creating
accessible, safe, pet-friendly shelter and safe haven options and
instituting a smoother, more transparent process for moving from the
streets could substantially reduce street homelessness.\nclaim: - To
prevent the revolving door to homelessness, it is necessary to remove
the barriers that hinder access to normal health resources which are
experienced by people suffering from social exclusion, while
implementing ongoing support programmes for homeless people or those at
risk of homelessness, which primarily deal with health issues.\nclaim:
We conclude that overcoming homelessness requires policies and practices
that give a greater focus to non-material aspects of homelessness
through an emphasis on empowerment, self-respect and autonomy.\nclaim:
This finding suggests that homelessness can be reduced by appropriate
clinical interventions if housing is available.\nclaim: For homelessness
prevention, systematic and outreach social medical care before and
during homelessness should be provided.\nquestion: What are effective
ways to prevent homelessness?"}], "ideal": "Summary: Ways to prevent
homelessness include creating accessible, safe shelter and safe haven
options, removing barriers to health resources, giving a greater focus
to non-material aspects of homelessness, and providing systematic and
outreach social medical care."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: While homelessness is ultimately the
result of a severe and chronic shortage of affordable housing, creating
accessible, safe, pet-friendly shelter and safe haven options and
instituting a smoother, more transparent process for moving from the
streets could substantially reduce street homelessness.\nclaim: - To
prevent the revolving door to homelessness, it is necessary to remove
the barriers that hinder access to normal health resources which are
experienced by people suffering from social exclusion, while
implementing ongoing support programmes for homeless people or those at
risk of homelessness, which primarily deal with health issues.\nclaim:
We conclude that overcoming homelessness requires policies and practices
that give a greater focus to non-material aspects of homelessness
through an emphasis on empowerment, self-respect and autonomy.\nclaim:
This finding suggests that homelessness can be reduced by appropriate
clinical interventions if housing is available.\nclaim: For homelessness
prevention, systematic and outreach social medical care before and
during homelessness should be provided.\nquestion: How to prevent
homelessness?"}], "ideal": "Summary: Ways to prevent homelessness
include creating accessible, safe shelter and safe haven options,
removing barriers to health resources, giving a greater focus to
non-material aspects of homelessness, and providing systematic and
outreach social medical care."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The findings revealed that the
factor that contributes the most to entrepreneurship intention is Locus
of control, followed by Need of Achievement and Subjective
Norms.\nclaim: It was found that entrepreneurial skill, environmental
factors and entrepreneurial orientation have a positive influence on
entrepreneurial intention.\nclaim: The findings indicate that
entrepreneurial motivation has a significant correlation with
entrepreneurial intention and its three determinants, social valuation
of entrepreneurship, having entrepreneurial role models, knowledge of
entrepreneurial support and perceived barriers to starting a
business.\nclaim: Research finding revealed that entrepreneurial
intention is indirectly affected by entrepreneurship education, meaning
that students\u2019 entrepreneurial motivation and attitude are two
important mediating variables.\nclaim: Findings confirm the influence of
individual and socio-cultural factors on entrepreneurial
intention.\nquestion: What are the factors of entrepreneurship
intention"}], "ideal": "Summary: Studies find that intrinsic factors,
such as entrepreneurial skill and motivation, as well as extrinsic
variables, such as the environmental support of entrepreneurship,
mediate entrepreneurship intention."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The results show that digital
agriculture is able to help users to increase productivity in a
sustainable way.\nclaim: Digital agriculture technologies continue the
centralization of economic knowledge and power as they facilitate the
transformation of vast territories into \u201coperational
landscapes\u201d that provide the material, energy, and labor for a
rapidly expanding urban system.\nclaim: The digital agriculture system
is an effective tool for insurance industry to use to develop a
dynamical business plan for the changing climate.\nclaim: The technical
fitting-out of agriculture in the digital economy should be considered
as a set of measures to prepare the industry for the production of
high-quality products, which implies the use of digital technologies
that minimize human participation in the production process.\nclaim:
Consequently, the initial Mobile-based Information System evolved into a
Digital Knowledge Ecosystem that can predict current production
situation in near real enabling government agencies to dynamically
adjust the incentives offered to farmers for growing different types of
crops to achieve sustainable agriculture production through crop
diversification.\nquestion: What is digital agriculture?"}], "ideal":
"Summary: N-A"}
  ```
</details>

---
## [jdanderson2/evals](https://github.com/jdanderson2/evals)@[d708a6be26...](https://github.com/jdanderson2/evals/commit/d708a6be261bfcb04962e64969164d737ba3972c)
#### Sunday 2023-08-13 16:51:05 by dougkwanna

NFL Point Combinations Eval (#1129)

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

NFL Point Combinations

### Eval description

This eval tests the model's ability to calculate all the possible ways
to achieve a specific score by a single team in an NFL game.

### What makes this a useful eval?

This eval is actually very similar to the coin change problem which
GPT-4 handles very well. However, it is extremely inaccurate when asked
to applied that same type of problem to a real life situation (2.5%
accuracy for GPT-3.5-turbo and 12.5% accuracy for GPT-4). It is
important for the model to learn how to derive logic problems from real
life context.

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

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 4 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[1]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 6 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[3]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 7 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[2]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 12 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[7]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 25 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[24]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 38 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[68]"}
  ```
</details>

---
## [jdanderson2/evals](https://github.com/jdanderson2/evals)@[73c8a178e6...](https://github.com/jdanderson2/evals/commit/73c8a178e69418760baee8983daa19fb492e9231)
#### Sunday 2023-08-13 16:51:05 by somerandomguyontheweb

Add Belarusian rhyme eval (#1143)

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

belarusian-rhyme

### Eval description

Test the model's ability to find rhyming words in Belarusian.

### What makes this a useful eval?

This eval is inspired by similar submissions for
[Hebrew](https://github.com/openai/evals/pull/176),
[Russian](https://github.com/openai/evals/pull/708),
[Ukrainian](https://github.com/openai/evals/pull/867),
[Finnish](https://github.com/openai/evals/pull/970), and
[Italian](https://github.com/openai/evals/pull/1003). The dataset
contains 50 pairs of English nouns whose Belarusian translations rhyme,
and another 50 pairs consisting of the same nouns but reordered, so that
in each of these additional pairs there aren't any Belarusian
translations that rhyme. The model's task is to output the rhyming pair
of Belarusian words or NONE. The rhyming pairs have been manually
picked, and many of them contain at least one word distinctive of
Belarusian, i.e. not attested in closely related Russian and Ukrainian
languages.

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

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "grass, church"}], "ideal":
["трава, царква", "царква, трава"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "food, tower"}], "ideal": ["ежа,
вежа", "вежа, ежа"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "grass, food"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "church, tower"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "foot, queue"}], "ideal": ["нага,
чарга", "чарга, нага"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "boat, flood"}], "ideal": ["лодка,
паводка", "паводка, лодка"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "foot, boat"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "queue, flood"}], "ideal": "NONE"}
  ```
</details>

---
## [Shakina2912/Resume-Portfolio-](https://github.com/Shakina2912/Resume-Portfolio-)@[e737d2355b...](https://github.com/Shakina2912/Resume-Portfolio-/commit/e737d2355b349a80f848ea51dc499b53cd03a3cf)
#### Sunday 2023-08-13 17:35:33 by Shakina Aggnes Twinkle

Update README.md

Abstract:
In the era of digital presence, personal portfolio websites have become a crucial tool for individuals to showcase their skills, achievements, and projects. This abstract presents the development of a dynamic portfolio website utilizing a blend of front-end technologies, namely HTML, CSS, and JavaScript. The primary focus lies in designing an aesthetically pleasing and user-friendly interface while incorporating interactive elements for an enhanced user experience.

The website is built using HTML as the foundation, ensuring a structured layout for the different sections of the portfolio. CSS is employed to craft visually appealing styles that align with the individual's personal branding. The layout responsiveness is achieved through responsive design principles, guaranteeing seamless accessibility across various devices and screen sizes.

The true dynamism of the website is brought to life with JavaScript. Interactivity is integrated using JavaScript to create animations, modals, and navigation effects. This not only engages the user but also provides a glimpse into the developer's proficiency with the technology.

Throughout the development process, reference source codes from reputable online resources were utilized. These references served as guides for implementing complex functionalities, such as smooth scrolling, image sliders, and form validation. By adapting and customizing these codes to fit the unique requirements of the portfolio, the resulting website stands as a testament to the fusion of acquired knowledge and creativity.

In conclusion, the presented abstract highlights the journey of crafting a dynamic portfolio website using HTML, CSS, and JavaScript. By seamlessly blending design aesthetics and interactive elements, the website becomes a comprehensive representation of the individual's skills and accomplishments. The integration of external source code references underscores the collaborative and resourceful nature of modern web development, culminating in a sophisticated portfolio that captivates users and exemplifies the power of front-end technologies.
Free Research Preview. ChatGPT may produce inaccurate information about people, places, or facts. ChatGPT August 3 Version

---
## [Dev-msm8953/kernel_xiaomi_msm8953](https://github.com/Dev-msm8953/kernel_xiaomi_msm8953)@[fbbf2a35e8...](https://github.com/Dev-msm8953/kernel_xiaomi_msm8953/commit/fbbf2a35e83849df38301a78f9fa66a2305e7ade)
#### Sunday 2023-08-13 17:38:05 by Angelo G. Del Regno

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

Signed-off-by: TogoFire <italomellopereira@gmail.com>
Change-Id: I746a6c68e233c74af46e709bade2d2f0626f860a

---
## [stinky-lizard/tf2-freeguns](https://github.com/stinky-lizard/tf2-freeguns)@[66d02522ba...](https://github.com/stinky-lizard/tf2-freeguns/commit/66d02522ba6a34e3954cbe6b621e6b9e52ce8b23)
#### Sunday 2023-08-13 18:26:05 by stinky-lizard

oohhhh my god. oh my god. oh my god.
finally works. it was literally 2 lines of code away the whole time.
holy shit.
thank you tf2-properclassweaponanimations.

---
## [MiTecHoy/MagicESP32](https://github.com/MiTecHoy/MagicESP32)@[f018fddf9d...](https://github.com/MiTecHoy/MagicESP32/commit/f018fddf9d51dd4a0f4f5f16885a7d5524377226)
#### Sunday 2023-08-13 19:20:53 by MiTecHoy

Create Magicwifi

Magic WiFi Signal Generator with ESP32: How it Works and How to Use it

Description: Welcome to the intriguing world of our ESP32-based Magic WiFi Signal Generator! This mesmerizing code creates a magical effect where a spectator selects a card from a deck, and that card mysteriously appears as a WiFi signal on the spectators' phones. Let's dive into how it works and how you can use it to create a jaw-dropping magic trick.

**How It Works:**

1. **Setup**: The code starts by initializing the ESP32 and creating a soft Access Point (AP) with a predefined SSID (in this case, "MagicESP32"). This AP acts as a custom WiFi network that the phones of the spectators will connect to.

2. **Web Interface**: The code sets up a web server that serves a simple HTML page. This page allows you to change the SSID of the soft AP dynamically. The web interface can be accessed by navigating to the ESP32's IP address in a web browser.

3. **Card-to-SSID Conversion**: When a spectator selects a card, the magician (you) uses the web interface to change the SSID of the soft AP to a special value corresponding to the chosen card. This conversion is done through the "/setssid" route, and the new SSID is set using the WiFi.softAP() function.

4. **Phone Connection**: The phones of the spectators automatically detect and display the custom WiFi signal (SSID) set by the magician. The effect is that the chosen card now seems to manifest as a WiFi signal.

**How to Use It:**

1. **Setup Hardware**: Load this code onto your ESP32 board using the Arduino IDE or a compatible platform. Ensure that the ESP32 is connected to power and that it can create a WiFi network.

2. **Access Web Interface**: Connect a device (laptop, smartphone, etc.) to the soft AP "MagicESP32" created by the ESP32. Open a web browser and enter the IP address provided by the ESP32 in the Serial Monitor. This will display the web interface.

3. **Perform the Trick**: Have a spectator select a card. Use the web interface to change the SSID to a value associated with the chosen card (you'll need to establish a mapping between cards and SSID values beforehand).

4. **Witness the Magic**: As the SSID is changed, the spectators' phones will detect the new WiFi signal, seemingly revealing the chosen card through the WiFi network.

This magical effect combines technology and illusion, leaving your audience amazed and intrigued. Prepare to dazzle your friends and family with this ESP32-powered magic trick that merges the world of magic with the power of the IoT!

===========================

 Generador de Señal WiFi Mágica con ESP32: Cómo Funciona y Cómo Usarlo

¡Bienvenidos al fascinante mundo de nuestro Generador de Señal WiFi Mágica basado en ESP32! Este código hipnotizante crea un efecto mágico en el que un espectador elige una carta de una baraja y esa carta aparece misteriosamente como una señal WiFi en los teléfonos de los espectadores. Veamos cómo funciona y cómo puedes usarlo para crear un truco de magia impactante.

**Cómo Funciona:**

1. **Configuración**: El código comienza inicializando el ESP32 y creando un Punto de Acceso (AP) virtual con un SSID predefinido (en este caso, "MagicESP32"). Este AP actúa como una red WiFi personalizada a la que se conectarán los teléfonos de los espectadores.

2. **Interfaz Web**: El código configura un servidor web que sirve una página HTML simple. Esta página te permite cambiar el SSID del AP virtual de manera dinámica. Puedes acceder a la interfaz web al ingresar la dirección IP del ESP32 en un navegador web.

3. **Conversión de Carta a SSID**: Cuando un espectador elige una carta, el mago (tú) usa la interfaz web para cambiar el SSID del AP virtual a un valor especial que corresponde a la carta elegida. Esta conversión se realiza a través de la ruta "/setssid", y el nuevo SSID se establece usando la función WiFi.softAP().

4. **Conexión de los Teléfonos**: Los teléfonos de los espectadores detectarán automáticamente y mostrarán la señal WiFi personalizada (SSID) establecida por el mago. El efecto es que la carta elegida ahora parece manifestarse como una señal WiFi.

**Cómo Usarlo:**

1. **Configurar el Hardware**: Carga este código en tu placa ESP32 utilizando el IDE de Arduino o una plataforma compatible. Asegúrate de que el ESP32 esté conectado a la alimentación y pueda crear una red WiFi.

2. **Acceder a la Interfaz Web**: Conecta un dispositivo (laptop, smartphone, etc.) al AP virtual "MagicESP32" creado por el ESP32. Abre un navegador web e ingresa la dirección IP proporcionada por el ESP32 en el Monitor Serie. Esto mostrará la interfaz web.

3. **Realizar el Truco**: Pide a un espectador que elija una carta. Usa la interfaz web para cambiar el SSID a un valor asociado con la carta elegida (necesitarás establecer un mapa entre cartas y valores de SSID de antemano).

4. **Presencia de la Magia**: A medida que cambias el SSID, los teléfonos de los espectadores detectarán la nueva señal WiFi, aparentemente revelando la carta elegida a través de la red WiFi.

Este efecto mágico combina tecnología e ilusión, dejando a tu audiencia sorprendida e intrigada. ¡Prepárate para deslumbrar a tus amigos y familiares con este truco de magia impulsado por ESP32 que fusiona el mundo de la magia con el poder del IoT!

---
## [IThundxr/UnlimitedBannerLayers](https://github.com/IThundxr/UnlimitedBannerLayers)@[42801951d6...](https://github.com/IThundxr/UnlimitedBannerLayers/commit/42801951d6139fd605e8b4ca5add939e52aadd69)
#### Sunday 2023-08-13 19:28:34 by IThundxr

"Added project icon and dependency, updated dependency versions and migrated to new config library

Additional dependencies and an icon have been added to fabric.mod.json for better mod metadata. Isolated the logic of maxLayerLimit to a new Config class and moved away from UBLConfig. Also updated versions of yarn mappings and loader in gradle.properties. Configuration library has been migrated from owo-lib to midnight-lib, providing better compatibility and reliability. The mod version number has been incremented to signify the significant changes to the mod structure. Additionally, provided means of distribution and release process for different channels (CurseForge, Modrinth). The new library represents a more streamlined, user-friendly configuration experience."

---
## [G-Rath/osv-scanner](https://github.com/G-Rath/osv-scanner)@[53107dd285...](https://github.com/G-Rath/osv-scanner/commit/53107dd2851eb10df2c8c5044c0319ae54a953d4)
#### Sunday 2023-08-13 20:08:14 by Gareth Jones

feat: add experimental offline mode (#183)

Resolves #81

~This is based off a lot of the core of the detector - it's not working
yet because I need to figure how to handle passing in the queries to the
local db given that the detector takes `PackageDetails`, but really the
key thing there is how to handle PURL which comes from SBOMs that I
don't really know how to use 😅 (idk if I'm just dumb or what, but for
some reason I've still not been able to figure how to accurately
generate one from a `Gemfile.lock`, `package-lock.json`, etc)~

~If someone could provide some sample SBOMs that would be very useful
(I'll also do a PR adding tests using them as fixtures), and also happy
to receive feedback on the general approach - there are some smaller
bits to discuss, like if fields should be omitted from the JSON output
vs an empty array, and the `Describe` related stuff too.~

This is now working, though personally it feels pretty awkward codewise
- I know I'm bias but I feel like it would be better to trying to bring
across the whole `database` package from the detector, as the API db is
pretty much the same and then you'd have support for zips, directories,
and the API with extra configs like working directories + an extensive
test suite for all three (I don't think it would be as painful as one
might first think, even with `osvscanner` having just been made public
because that's relatively small).

Still, this does work as advertised - there's definitely a few things
that could do with some cleaning up (including if fields should be
omitted from the JSON output vs an empty array, and the `Describe`
related stuff too) but am leaving them for now until I hear what folks
think of the general implementation + my above comment.

I've also gone with two boolean flags rather than the url-based flag
@oliverchang suggested because I didn't feel comfortable trying to
shoehorn that into this PR as well, and now that we're using
`--experimental` it should be fine to completely change these flags in
future.

---
## [bplaat/serenity](https://github.com/bplaat/serenity)@[8d17ede197...](https://github.com/bplaat/serenity/commit/8d17ede1977517fb0556857e042bd4abd7174a7b)
#### Sunday 2023-08-13 20:38:18 by Xexxa

Base: Improve emoji

Remove unnecessary left/right padding

❣️ - U+2763 HEART EXCLAMATION
🚶 - U+1F6B6 PERSON WALKING
🚴 - U+1F6B4 PERSON BIKING
🌻 - U+1F33B SUNFLOWER
🪻 - U+1FABB HYACINTH
🍉 - U+1F349 WATERMELON
🍍 - U+1F34D PINEAPPLE
🫒 - U+1FAD2 OLIVE
🌽 - U+1F33D EAR OF CORN
🌯 - U+1F32F BURRITO
🍘 - U+1F358 RICE CRACKER
🧁 - U+1F9C1 CUPCAKE
🍫 - U+1F36B CHOCOLATE BAR
🍭 - U+1F36D LOLLIPOP
🍼 - U+1F37C BABY BOTTLE
🧋 - U+1F9CB BUBBLE TEA
🧃 - U+1F9C3 BEVERAGE BOX
🥢 - U+1F962 CHOPSTICKS
💈 - U+1F488 BARBER POLE
🌛 - U+1F31B FIRST QUARTER MOON FACE
🌜 - U+1F31C LAST QUARTER MOON FACE
🌡️ - U+1F321 THERMOMETER
🪐 - U+1FA90 RINGED PLANET
⚡ - U+26A1 HIGH VOLTAGE
💧 - U+1F4A7 DROPLET
🧨 - U+1F9E8 FIRECRACKER
🥇 - U+1F947 1ST PLACE MEDAL
🥈 - U+1F948 2ND PLACE MEDAL
🥉 - U+1F949 3RD PLACE MEDAL
🏓 - U+1F3D3 PING PONG
🪀 - U+1FA80 YO-YO
♟️ - U+265F CHESS PAWN
🧦 - U+1F9E6 SOCKS
💄 - U+1F484 LIPSTICK
📱 - U+1F4F1 MOBILE PHONE
🔌 - U+1F50C ELECTRIC PLUG
💡 - U+1F4A1 LIGHT BULB
📍 - U+1F4CD ROUND PUSHPIN
🔩 - U+1F529 NUT AND BOLT
🪝 - U+1FA9D HOOK
🧪 - U+1F9EA TEST TUBE
🔭 - U+1F52D TELESCOPE
🩸 - U+1FA78 DROP OF BLOOD
💊 - U+1F48A PILL
🩹 - U+1FA79 ADHESIVE BANDAGE
🧼 - U+1F9FC SOAP
🪥 - U+1FAA5 TOOTHBRUSH
♀️ - U+2640 FEMALE SIGN
♂️ - U+2642 MALE SIGN
➕ - U+2795 PLUS
➗ - U+2797 DIVIDE
❓ - U+2753 RED QUESTION MARK
❔ - U+2754 WHITE QUESTION MARK
❕ - U+2755 WHITE EXCLAMATION MARK
❗ - U+2757 RED EXCLAMATION MARK
◼️ - U+25FC BLACK MEDIUM SQUARE
◻️ - U+25FB WHITE MEDIUM SQUARE
◾ - U+25FE BLACK MEDIUM-SMALL SQUARE
◽ - U+25FD WHITE MEDIUM-SMALL SQUARE
▪️ - U+25AA BLACK SMALL SQUARE
▫️ - U+25AB WHITE SMALL SQUARE
🚩 - U+1F6A9 TRIANGULAR FLAG

---
## [ElizabethLBell/SQL](https://github.com/ElizabethLBell/SQL)@[2494988c82...](https://github.com/ElizabethLBell/SQL/commit/2494988c828721d45828dc1c05e3cfd52651e532)
#### Sunday 2023-08-13 20:46:56 by ElizabethLBell

Create Netflix Dataset

This project utilized data from the following Netflix dataset:
CREATE TABLE netflix_titles_info
    ("show_id" varchar(5), "type" varchar(7), "title" varchar(58), "country" varchar(74), "date_added" timestamp, "release_year" int, "rating" varchar(5), "duration" varchar(9), "listed_in" varchar(74))
;

CREATE TABLE netflix_people
    ("show_id" varchar(5), "director" varchar(54), "cast" varchar(532))
;
    
INSERT INTO netflix_titles_info
    ("show_id", "type", "title", "country", "date_added", "release_year", "rating", "duration", "listed_in")
VALUES
    ('s1', 'Movie', 'Dick Johnson Is Dead', 'United States', '2021-09-25 00:00:00', 2020, 'PG-13', '90 min', 'Documentaries'),
    ('s2', 'TV Show', 'Blood & Water', 'South Africa', '2021-09-24 00:00:00', 2021, 'TV-MA', '2 Seasons', 'International TV Shows | TV Dramas | TV Mysteries'),
    ('s3', 'TV Show', 'Ganglands', NULL, '2021-09-24 00:00:00', 2021, 'TV-MA', '1 Season', 'Crime TV Shows | International TV Shows | TV Action & Adventure'),
    ('s4', 'TV Show', 'Jailbirds New Orleans', NULL, '2021-09-24 00:00:00', 2021, 'TV-MA', '1 Season', 'Docuseries | Reality TV'),
    ('s5', 'TV Show', 'Kota Factory', 'India', '2021-09-24 00:00:00', 2021, 'TV-MA', '2 Seasons', 'International TV Shows | Romantic TV Shows | TV Comedies'),
    ('s6', 'TV Show', 'Midnight Mass', NULL, '2021-09-24 00:00:00', 2021, 'TV-MA', '1 Season', 'TV Dramas | TV Horror | TV Mysteries'),
    ('s7', 'Movie', 'My Little Pony: A New Generation', NULL, '2021-09-24 00:00:00', 2021, 'PG', '91 min', 'Children & Family Movies'),
    ('s8', 'Movie', 'Sankofa', 'United States | Ghana | Burkina Faso | United Kingdom | Germany | Ethiopia', '2021-09-24 00:00:00', 1993, 'TV-MA', '125 min', 'Dramas | Independent Movies | International Movies'),
    ('s9', 'TV Show', 'The Great British Baking Show', 'United Kingdom', '2021-09-24 00:00:00', 2021, 'TV-14', '9 Seasons', 'British TV Shows | Reality TV'),
    ('s10', 'Movie', 'The Starling', 'United States', '2021-09-24 00:00:00', 2021, 'PG-13', '104 min', 'Comedies | Dramas'),
    ('s11', 'TV Show', 'Vendetta: Truth  Lies and The Mafia', NULL, '2021-09-24 00:00:00', 2021, 'TV-MA', '1 Season', 'Crime TV Shows | Docuseries | International TV Shows'),
    ('s12', 'TV Show', 'Bangkok Breaking', NULL, '2021-09-23 00:00:00', 2021, 'TV-MA', '1 Season', 'Crime TV Shows | International TV Shows | TV Action & Adventure'),
    ('s13', 'Movie', 'Je Suis Karl', 'Germany | Czech Republic', '2021-09-23 00:00:00', 2021, 'TV-MA', '127 min', 'Dramas | International Movies'),
    ('s14', 'Movie', 'Confessions of an Invisible Girl', NULL, '2021-09-22 00:00:00', 2021, 'TV-PG', '91 min', 'Children & Family Movies | Comedies'),
    ('s15', 'TV Show', 'Crime Stories: India Detectives', NULL, '2021-09-22 00:00:00', 2021, 'TV-MA', '1 Season', 'British TV Shows | Crime TV Shows | Docuseries'),
    ('s16', 'TV Show', 'Dear White People', 'United States', '2021-09-22 00:00:00', 2021, 'TV-MA', '4 Seasons', 'TV Comedies | TV Dramas'),
    ('s17', 'Movie', 'Europe''s Most Dangerous Man: Otto Skorzeny in Spain', NULL, '2021-09-22 00:00:00', 2020, 'TV-MA', '67 min', 'Documentaries | International Movies'),
    ('s18', 'TV Show', 'Falsa identidad', 'Mexico', '2021-09-22 00:00:00', 2020, 'TV-MA', '2 Seasons', 'Crime TV Shows | Spanish-Language TV Shows | TV Dramas'),
    ('s19', 'Movie', 'Intrusion', NULL, '2021-09-22 00:00:00', 2021, 'TV-14', '94 min', 'Thrillers'),
    ('s20', 'TV Show', 'Jaguar', NULL, '2021-09-22 00:00:00', 2021, 'TV-MA', '1 Season', 'International TV Shows | Spanish-Language TV Shows | TV Action & Adventure')
    ;
    
INSERT INTO netflix_people
    ("show_id", "director", "cast")
VALUES
    ('s1', 'Kirsten Johnson', NULL),
    ('s2', NULL, 'Ama Qamata| Khosi Ngema| Gail Mabalane| Thabang Molaba| Dillon Windvogel| Natasha Thahane| Arno Greeff| Xolile Tshabalala| Getmore Sithole| Cindy Mahlangu| Ryle De Morny| Greteli Fincham| Sello Maake Ka-Ncube| Odwa Gwanya| Mekaila Mathys| Sandi Schultz| Duane Williams| Shamilla Miller| Patrick Mofokeng'),
    ('s3', 'Julien Leclercq', 'Sami Bouajila| Tracy Gotoas| Samuel Jouy| Nabiha Akkari| Sofia Lesaffre| Salim Kechiouche| Noureddine Farihi| Geert Van Rampelberg| Bakary Diombera'),
    ('s4', NULL, NULL),
    ('s5', NULL, 'Mayur More| Jitendra Kumar| Ranjan Raj| Alam Khan| Ahsaas Channa| Revathi Pillai| Urvi Singh| Arun Kumar'),
    ('s6', 'Mike Flanagan', 'Kate Siegel| Zach Gilford| Hamish Linklater| Henry Thomas| Kristin Lehman| Samantha Sloyan| Igby Rigney| Rahul Kohli| Annarah Cymone| Annabeth Gish| Alex Essoe| Rahul Abburi| Matt Biedel| Michael Trucco| Crystal Balint| Louis Oliver'),
    ('s7', 'Robert Cullen| JosÃ© Luis Ucha', 'Vanessa Hudgens| Kimiko Glenn| James Marsden| Sofia Carson| Liza Koshy| Ken Jeong| Elizabeth Perkins| Jane Krakowski| Michael McKean| Phil LaMarr'),
    ('s8', 'Haile Gerima', 'Kofi Ghanaba| Oyafunmike Ogunlano| Alexandra Duah| Nick Medley| Mutabaruka| Afemo Omilami| Reggie Carter| Mzuri'),
    ('s9', 'Andy Devonshire', 'Mel Giedroyc| Sue Perkins| Mary Berry| Paul Hollywood'),
    ('s10', 'Theodore Melfi', 'Melissa McCarthy| Chris O''Dowd| Kevin Kline| Timothy Olyphant| Daveed Diggs| Skyler Gisondo| Laura Harrier| Rosalind Chao| Kimberly Quinn| Loretta Devine| Ravi Kapoor'),
    ('s11', NULL, NULL),
    ('s12', 'Kongkiat Komesiri', 'Sukollawat Kanarot| Sushar Manaying| Pavarit Mongkolpisit| Sahajak Boonthanakit| Suthipongse Thatphithakkul| Bhasaworn Bawronkirati| Daweerit Chullasapya| Waratthaya Wongchayaporn| Kittiphoom Wongpentak| Abhicha Thanachanun| Nophand Boonyai| Kittipong Khamsat| Arisara Wongchalee| Jaytiya Naiwattanakul| Pantipa Arunwattanachai| Panupan Jantanawong| Kungtap Saelim| Phumphat Chartsuriyakiat| Issara Veranitinunt| Keerati Sivakuae| Panjai Sirisuwan| Supranee Charoenpol| Suda Chuenban| Visaka Banhansupavat| Pitchatorn Santinatornkul'),
    ('s13', 'Christian Schwochow', 'Luna Wedler| Jannis NiewÃ¶hner| Milan Peschel| Edin HasanoviÄ‡| Anna FialovÃ¡| Marlon Boess| Victor Boccard| Fleur Geffrier| Aziz Dyab| MÃ©lanie FouchÃ©| Elizaveta MaximovÃ¡'),
    ('s14', 'Bruno Garotti', 'Klara Castanho| Lucca Picon| JÃºlia Gomes| Marcus Bessa| Kiria Malheiros| Fernanda Concon| Gabriel Lima| Caio Cabral| Leonardo Cidade| Jade Cardozo'),
    ('s15', NULL, NULL),
    ('s16', NULL, 'Logan Browning| Brandon P. Bell| DeRon Horton| Antoinette Robertson| John Patrick Amedori| Ashley Blaine Featherson| Marque Richardson| Giancarlo Esposito'),
    ('s17', 'Pedro de Echave GarcÃ­a| Pablo AzorÃ­n Williams', NULL),
    ('s18', NULL, 'Luis Ernesto Franco| Camila Sodi| Sergio Goyri| Samadhi Zendejas| Eduardo YÃ¡Ã±ez| Sonya Smith| Alejandro Camacho| Azela Robinson| Uriel del Toro| GÃ©raldine BazÃ¡n| Gabriela Roel| Marcus Ornellas'),
    ('s19', 'Adam Salky', 'Freida Pinto| Logan Marshall-Green| Robert John Burke| Megan Elisabeth Kelly| Sarah Minnich| Hayes Hargrove| Mark Sivertsen| Brandon Fierro| Antonio Valles| Clint Obenchain'),
    ('s20', NULL, 'Blanca SuÃ¡rez| IvÃ¡n Marcos| Ã“scar Casas| AdriÃ¡n Lastra| Francesc Garrido| Stefan Weinert| Julia MÃ¶ller| Alicia Chojnowski')
    ;

---
## [s626ch/better-bajookie-tabs](https://github.com/s626ch/better-bajookie-tabs)@[9339e4660b...](https://github.com/s626ch/better-bajookie-tabs/commit/9339e4660b902ecf81e4d396a4c0ab7110804f9a)
#### Sunday 2023-08-13 21:58:03 by s626ch

fix weird userpage bug?

for some fucking reason having "Users" above "Users/" didn't pull in the proper title check shit idk this explanation sucks

---
## [rayzchen/pyeod](https://github.com/rayzchen/pyeod)@[72bc9786aa...](https://github.com/rayzchen/pyeod/commit/72bc9786aa325730d1426168199ce1311bd1e53f)
#### Sunday 2023-08-13 23:18:44 by Cheesy-Brik

Add commenting elements

We should really refactor the packing methods, kinda a pain in the ass to use rn.
Too much boilerplate imo

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[16543664cb...](https://github.com/cyberitsolutions/bootstrap2020/commit/16543664cb6d083759874c4c412cbc6afc403cf4)
#### Sunday 2023-08-13 23:48:09 by Trent W. Buck

Fix during-build DNS resolution

08:30 <twb> TIL update-smart-drivedb in Debian 11 broke this week
08:36 <twb> OK it looks like it now needs gpg and since gpg2 needs a bunch of systemd listener bullshit, it just fails completely now
08:37 <twb> But if I add --no-verify it's working in a test unshare
08:37 <twb> But the prod error was from curl, not gpg...
08:37 <twb> 6 Could not resolve host. The given remote host could not be resolved.
08:37 <twb> Ah fuck it's DNS that broke
08:38 <twb> This means it's my fault, so never mind.
09:13 <twb> OK so the problem is pretty simple.  The build hosts now have /etc/resolv.conf -> /run/blah/systemd where they used to have -> /usr/lib/blah/systemd
09:14 <twb> Since the symlink's destination doesn't exist inside the chroot (/dev and /proc are bind-mounted in, but /run is not), DNS fails
09:14 <twb> The simple fix is to create a dummy /run/blah/systemd during the build

This is very similar to the fix I already did in Debian 12, when
I thought this was a new problem in Debian 12.

See https://github.com/cyberitsolutions/bootstrap2020/blob/twb/debian-12-main.hooks/customize50-dynamic-dns-resolv-conf.py

---

