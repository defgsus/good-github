## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-16](docs/good-messages/2022/2022-10-16.md)


1,971,180 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,971,180 were push events containing 2,673,423 commit messages that amount to 163,856,264 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [Wiredista/jam2022](https://github.com/Wiredista/jam2022)@[369777621b...](https://github.com/Wiredista/jam2022/commit/369777621bd7a7bfdca581273d6fbc897b6a8455)
#### Sunday 2022-10-16 00:08:10 by Álvaro Antônio

I hate my life. If you're seeing this commit please be aware that god ends here.

---
## [Mu-L/NetHack](https://github.com/Mu-L/NetHack)@[4c98ba493b...](https://github.com/Mu-L/NetHack/commit/4c98ba493bb7eaa7c556c4b720a7b6df7ea74d0e)
#### Sunday 2022-10-16 00:12:03 by Michael Meyer

Remove explicit 'none' opt from autounlock handler

The autounlock handler included an explicit 'none' option, a choice that
gave it a different UX from similar existing compound option handlers
(e.g. paranoid_confirm or pickup_types), which set 'none' simply by
deselecting all options.  It didn't make the menu any easier to use (at
least in my experience), since in order to go from some combination of
options to 'none', you'd have to deselect everything anyway (which on
its own was enough to set 'none', so there was no reason to explicitly
select it after doing so).

Make the autounlock handler work like other compound option handlers,
such that deselecting all options is the way to set 'none', and there is
no explicit 'none' option included in the list.

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[216bbb170d...](https://github.com/newstools/2022-express/commit/216bbb170dd6750cfe57248ff6b554a1a1fea4b5)
#### Sunday 2022-10-16 00:37:52 by Billy Einkamerer

Created Text For URL [www.express.co.uk/news/science/1683130/macron-shamed-totalenergies-putin-war-planes-ukraine-bombing-oil-anti-terrorism]

---
## [MartyX5555/ACE-Dev](https://github.com/MartyX5555/ACE-Dev)@[93be1b21bb...](https://github.com/MartyX5555/ACE-Dev/commit/93be1b21bbdbf656b4de5abb25a3fbd6fb01ec69)
#### Sunday 2022-10-16 02:42:33 by Mr Marty

optional nadmod, missile adjustments & more

- added acf3's traceline workaround. useless tracehull calls should be removed as time passes.
- Fixed closest distance output. Now it will give a distance properly.
- Fixed some bugs with some missile crazy trayectory. Remember: dont shoot at 90°, you will not want friendly causalities...
- Added Plunging fuze. Aka tow2b top attack capacity
- Done fuze core less shitty. Ability to override the detonation perform.
- Nadmod becomes optional. Without it, damage can be done. Damage permissions becomes no available.
- Added primitive class ent into contraption look for filter.
- Updated armor analyzer. ERA armor calculation considers angle now.
- Minor changes to AT-3 and AT-2 missiles

---
## [OpheliaXI/AirSkyBoat](https://github.com/OpheliaXI/AirSkyBoat)@[40e1c4a7d7...](https://github.com/OpheliaXI/AirSkyBoat/commit/40e1c4a7d7f07de631b3a074c0976270428ba690)
#### Sunday 2022-10-16 02:42:40 by dallano

Better the Demon You Know Quest Implementation

Implements the quest: "Better the Demon You Know"
NM Behaviors:
- Andrealphus uses blood weapon every 3 minutes
- Andrealphus escapes the target with hate out of the zone at 75% and 25% HP

---
## [iLVL-Key/FFXI](https://github.com/iLVL-Key/FFXI)@[786520887f...](https://github.com/iLVL-Key/FFXI/commit/786520887f411fb8d14682ca980cfe82e23aa509)
#### Sunday 2022-10-16 04:17:40 by iLVL-Key

10.15.22 (VCC: Invincible)

-Overhauled how enmity spells are handled. No more macro with a custom command in it. If you are /BLU, just use a macro for Sheep Song and it will cast Sheep Song, Geist Wall, Stinking Gas, or Soporific, in that order, as recasts timers allow. Additionally, now you can use a macro for Flash and it will also use Jettatura or Blank Gaze if you are /BLU, or Provoke if you are /WAR, depending on recast timers and distance to target.
-Added an Oh Shit gear set and accompanying option to use it. HP threshold required to activate is adjustable in the Advanced Options.
-Added AutoSentinel option. Automatically attempts to activate Sentinel when your HP gets critically low. HP threshold required to activate is adjustable in the Advanced Options.
-Added Low HP Notification.
-Added AutoHWater option. Automatically attempts to use Holy Waters when you get Doomed until it wears off. Currently will keep trying even if you run out of Holy Waters.
-Added DoomAlert option. Will alert your party when you are doomed. You can also customize the text that displays in party chat.
-Added CharmNaked option. Removes all gear, or all gear except weapons, when you are charmed.
-Added Crusade, Phalanx, Cocoon, Defender, Reprisal, Palisade, and Enlight to the list of things that will trigger AutoMajesty after use.
-Added Sneak and Invisible status notification.
-Added missing listings in the /fileinfo printout for a few Notifications.
-Added Silver Knife to list of Adoulin/Town areas.
-Adjusted the code that tries to wake you when you are asleep to not trigger if you are charmed.
-Adjusted resting to equip Refresh + Rest gear sets regardless of Mode.
-Moved AutoMajWindow, ModeCtrlPlus, and RRReminderTimer from Options to Advanced Options.
-Removed Gearswaps built-in showswaps function from the files debug mode.
-Fixed looking in the hands slot for the leg pieces to augment Invincible. (Thanks to Mailani for the catch)
-Updated Version Compatibility Codename to Invincible.
-Code cleanup.

---
## [iLVL-Key/FFXI](https://github.com/iLVL-Key/FFXI)@[1ab9f4cc18...](https://github.com/iLVL-Key/FFXI/commit/1ab9f4cc18ca46c384fa3043eac0506279a33a3c)
#### Sunday 2022-10-16 04:52:44 by iLVL-Key

10.15.22 (VCC: Tachi: Goten)

-Renamed Mode to Stance.
-Added new Hasso Modes. Seigan still uses one set while Hasso is split into 3. These modes can be used (and named) however you'd like. You can switch between the 3 modes on the fly with a macro, alias, or keyboard shortcut.
-Added Capped TP Weapon Skill set.
-Added Hybrid Weaponskill set.
-Added an Oh Shit gear set and accompanying option to use it. HP threshold required to activate is adjustable in the Advanced Options.
-Added Low HP Notification.
-Added AutoHWater option. Automatically attempts to use Holy Waters when you get Doomed until it wears off. Currently will keep trying even if you run out of Holy Waters.
-Added DoomAlert option. Will alert your party when you are doomed. You can also customize the text that displays in party chat.
-Added Sneak and Invisible status notification.
-Added missing listings in the /fileinfo printout for a few Notifications.
-Added Silver Knife to list of Adoulin/Town areas.
-Adjusted CharmNaked option to have three options: all gear, all gear except weapons, or off.
-Adjusted the code that tries to wake you when you are asleep to not trigger if you are charmed.
-Moved RRReminderTimer from Options to Advanced Options.
-Removed Gearswaps built-in showswaps function from the files debug mode.
-Updated Version Compatibility Codename to Tachi: Goten.
-Code cleanup.

---
## [dyphire/mpv](https://github.com/dyphire/mpv)@[6f7506b660...](https://github.com/dyphire/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Sunday 2022-10-16 05:14:57 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[db83f6498d...](https://github.com/lessthnthree/tgstation/commit/db83f6498da37ecd25588ea3f7024409d2f3f117)
#### Sunday 2022-10-16 05:57:47 by vincentiusvin

Simplifies SM damage calculation, tweaks the numbers. (#70347)


About The Pull Request

We apply the damage hardcap individually now, split off the old flat 1.8 into individual caps for heat, moles, and power.

Set it to 1.5 for heat, 1 for mole and 1 for power. This means for most delams it'll be a tad slower! But its possible to make SM delam nearly twice as fast if you combine all 3. (3.5). Be pretty hard tho.

Set the heat healing to -1 so you can counteract one factor at most (except heat since you'll never get both heat healing and heat damage at the same time anyway).

I'm not hell bent on any of the numbers, just picked round even ones and ones that i think will make sense. If you want them changed lmk.

Got rid of the cascade mole and power multipliers since there's probably like three people that are aware that it even exists. Ideally we just add another entry to the CIMS but its already pretty crowded. Figured nobody is gonna miss it anyway? Sorry ghil.

Got rid of the moles multiplier thing since its nicer to keep the temp damage fully based on temp damage instead of adding another multiplier. I just applied the .25 to the damage flatly, meaning it slows down delams again!

And some space exposure stuff: #70347 (comment)
Why It's Good For The Game

Hardcap: Discrete, less randomly interconnected factors are easier to present and remember. The calculation procs are also made to be additive so we had to hack a bit and do some rescaling to accomodate the old behavior in my original PR #69240. Can remove the hack if this pr goes through.

Cascade and mole multiplier: The rest are just getting rid of underutilized factors so we have a cleaner behavior to maintain, present, and understand. (In a perfect world modifiers that aren't visible to the players shouldn't have been merged in the first place smh smh)
Changelog

🆑
fix: Fixed sm space exposure damage going through walls
del: got rid of the molar multiplier for sm heating damage. It will now only impact molar damage and temp limit. We apply the lowest value directly so this slows down sm delams a tiny bit.
del: got rid of cascades making sm delam at 450 moles and 1250 mev. It delams normally now.
balance: Applied the sm damage hardcap of 1.8 individually to heat (1.5), moles (1), power (1). Meaning most sm delams are slower now, but the really bad ones can be faster.
balance: Halved sm temp healing across the board. Temp limits are still the same though so you shouldn't notice it that much.
balance: Halved SM power damage across the board.
balance: Changed sm space exposure damage to just check for the current tile and adjacent atmos connected tiles.
/🆑

---
## [vlggms/lobotomy-corp13](https://github.com/vlggms/lobotomy-corp13)@[0220bde488...](https://github.com/vlggms/lobotomy-corp13/commit/0220bde48808454df3754d7c71953f66553dcd47)
#### Sunday 2022-10-16 08:42:32 by PotatoTomahto

pathfinding

revert

oops

oops 2

god fragment

fixes

fixes oopsie

forgot scorched girl

real scorched fix:

typo

better patrolling

final

forgot about dreaming

dreaming current name

fragment oopsies

violet oopsie

really the final one

final final one

---
## [MeteorTheLizard/MMM_M9k_Remastered](https://github.com/MeteorTheLizard/MMM_M9k_Remastered)@[81df2e686e...](https://github.com/MeteorTheLizard/MMM_M9k_Remastered/commit/81df2e686e68f33e73e4982b5abd203796a72fe3)
#### Sunday 2022-10-16 08:56:24 by Meteor

Version 2.0

The Gameplay is unaffected. All the controls are the same as before and everything should feel just like it always has with the exception of being less jank and less prone to glitching out.
Base SWEP files now feature Dev Notes so that developers will have an easier time making weapons using the bases.
The Gameplay should feel better overall for people with a high ping as lag compensation was added wherever it was needed.

LEFT HAND SUPPORT! wow. I know. "m9k_lefthanded 1" in console to enable left-hand mode. Clientside only. Do note that Weapons that make use of viewmodel projection cannot be flipped and therefor will still be right-handed.

General:
- Major performance improvements in pretty much every file.
- Script files have been made more readable in general.
- Code has been separated between CLIENT and SERVER for a slight performance increase and improved readability.
- Various improvements to sound scripts, should take up less memory and reduce load times.
- Improved idle animations. They're now Lua-level, meaning jank/broken idle animations are automatically replaced.
- Every bullet fired now has a tracer.
- You can no longer use IronSights on some shotguns as it was just weird and its pointless anyway.
- Improved the Shotgun-base reload animations for thirdperson view.
- Slightly adjusted the position of the machete viewmodel.
- Categories have been renamed from "M9K (Weapon Type)" to "M9kR: (Weapon Type)"
- Admin Weapons have been removed. As fun as they were, they were causing far too many issues to be worth it. There MIGHT be an expansion in the future featuring these Weapons and new ones.
- Slightly adjusted the Ironsight position and angles of the m249lmg.
- The Honeybadger and KAC_PDW now also have a scope in thirdperson view and when dropped.
- The Remington 1858 no longer fires multiple shots like a shotgun in the remastered balance and can no longer make use of ironsights. They were unusable and hilariously bad.
- Changed the holdtype of the tec9 to "SMG" to more accurately represent the viewmodel.
- Disabled ironsights for the Magpul PDR. I wanted to add a scope to it but the viewmodel doesn't allow it and aiming down the rail was dumb.
- The Harpoon now does more damage on melee attacks.
- Increased the RPM of the m9k_m202 and the Reloading is now a bit faster.
- Reduced the spread penalty from moving from *6 to *2. Bullets going sideways are a thing of the past now.
- The Flaregun and Peashooters have been moved to the "M9kR: Other" Category.
- Frag Grenade has been renamed to M61 Grenade.
- Added IED ammo crate and 40mm Grenades ammo crate
- Sticky Grenades stick to all entities now.
- The Knife, Machete, and Harpoon stick to surfaces way easier as the logic for that has been overhauled.
- Ammo Entities have gotten a [B] tag which stands for "BASE" in their name at the start now.
- RPG crate has been renamed to Propelled Rockets crate.
- Countless of other improvements for all entities.

New Weapons:
- Orbital Strike Cannon. Yes, it is back and better than ever! With c_hands! wow!
- IED Detonator. They make use of c_hands through model projection and they do not crash your game when you spam a ton of them! wow! Also matching world models! wow!
- Davy Crockett. A lot of people requested for this weapon to return. I didn't want to bring it back as this single Weapon has 8 lua files associated with it and it is a crazy amount of work to do. I did it anyway. You're welcome.
> The Davy Crockett no longer changes the models of players and NPCs to charpels. Changing models causes more issues than you think.

Base Improvements:
- Recoil of Weapons has been improved drastically for People that have a high ping.
- Weapons can now be reloaded even when full. Unused ammo is refunded. (Exception: Most Shotguns) - This means that you can also UNLOAD Weapons, wow!
- Added a new var that allows weapons to fire underwater if set to true.
- Added a new var that allows you to modify the volume of a firing sound.
- Sounds are more immersive in general as the loudness of the sounds actually make sense now. Though they're not as loud as they would be IRL since that would be annoying.
- For more fluid gameplay you're now allowed to reload while deploying the weapon.
- Scope logic is now handled serverside for bobs_scoped_base.lua based weapons which fixed countless of issues related to it.
- Throwing melee Weapons now always gets rid of the Weapon. No more knife/harpoon spamming! At least not that efficiently.
- You can now only throw melee Weapons by pressing the Reload key. Consistency!
- Lag compensation everywhere!

New Features:
- Dynamic Reload Sounds! All Weapons have received Dynamic Reload sound compatibility.
> This means that reload sounds are now played for other players as well, while the thirdperson animation may not match the sounds, at least you can now tell if someone is reloading and what the reload progress is.
> This also means that sounds are now properly synced with the firstperson animation which was not the case with some weapons before.
> Bolt-Action weapons are also affected. The sounds of the bolt being pulled back and released are now played for other players as well.
> Dynamic sounds have been synced using host_timescale 0.1 - It took a really really long time..

- Balance Switch. You can choose between the Legacy balancing and the Remastered balancing. m9k_balancemode 0/1. By default this mod now uses the Legacy balancing as it should have from the very beginning.
> This can be changed whenever and all active weapons get updated on the fly. Yes, it really happened!
> 0 = Legacy balancing | 1 = Remastered balancing.
> Do note that when using the Legacy balance.. You're still subject to the Remastered Recoil system that imitates CS:S Recoil behavior.

- Base Hooks. The majority of Weapon functions now have a "Hooked" call whenever they are executed.
> This allows Developers to expand on the Weapon functions instead of having to copy & paste the code from the base and then modifying it.
> CLIENT & SERVER
> Initialize > IntializeHooked
> ResetInternalVars > ResetInternalVarsHooked
> Deploy > DeployHooked
> Equip > EquipHooked
> Reload > ReloadHooked - Note: Can be blocked by returning true in ReloadHooked (Serverside only)
> Think > ThinkHooked
> SERVER
> OnDrop > OnDropHooked
> PrimaryAttack > PrimaryAttackHooked
.. And many more!

ConVars:
- Better help text for all ConVars.
- ConVars were moved to their respective bases.
- New Serverside print that tells you about all available ConVars and what they do.

Bug fixes:
- Fixed a bug with the bases that would cause the reload and ironsights to break after reloading a file.
- Fixed a bug with the ironsights sometimes getting stuck in the aiming position when reloading.
- Fixed a bug with m9k_spawn_with_ammo that was allowing players to duplicate ammo.
- Fixed a bug with m9k_spawn_with_reserve that was allowing players to duplicate ammo.
- Fixed scopes sometimes not working as intended. (Going out of sync, getting stuck, and more.)
- Fixed an error with meteors_grenade_base_model.lua attempting to get the information of non-existent bones on some world/view models. This used to happen with badly rigged models. Thanks to wrefgtzweve on GitHub for reporting this error.
- Fixed a bug with the m9k_minigun where the left pinkie finger becomes unwilling to grip the handle after reloading. You can't make this shit up man.
- Fixed the muzzleflash of the mp9 coming out of the shell ejection mechanism while aiming down the sights. This weapon does not have a muzzleflash parent bone and therefor should never have a muzzleflash.
- Implemented code that replaces missing textures with the appropriate materials automagically. The original creators of M9k really messed up here.
- Fixed sound loops caused by the Flaregun.

Known bugs:
- When switching m9k_zoomtoggle on and off while using a scope it can sometimes start at ZoomStage 2 instead of 1 as values cannot reset when m9k_zoomtoggle is set to 0. This is not really a problem as it fixes itself when using the scope again.
- In most environments the automatic dropping of armed grenades on player death will not work.

>> Singleplayer only:
- Shell ejection remains broken while aiming down the sights.
- The flaregun reload animations glitch out.
- Viewmodel projection is sometimes incorrectly oriented.
- The Reload animation is missing for the Matador.

COMPATIBILITY NOTE:
- If you had made custom weapons that use an M9kR base, they will most likely be broken now.
	> This had to be done as the general state of M9kR before this update was just bad.
	> Sacrifices have to be made sometimes if the result is something outstanding.

- NPCs remain unsupported. This MIGHT change in the future.
- Still no c_hands. I want them too but I'm not gonna rework hundreds of models. They're used wherever possible through viewmodel projection.

PLANNED FEATURES:
- Attaching Silencers to Weapons that used to be able to be silenced ( ACR, g36, hk416, Vikhr, KAC_PDW, and probably more that I'm forgetting about! )
- Selecting Firemodes	(MAYBE)
- Bullet Ricochet		(MAYBE) - It will always be jank so most likely not!

---
## [cys9211/otservbr-global](https://github.com/cys9211/otservbr-global)@[fbd70d116c...](https://github.com/cys9211/otservbr-global/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Sunday 2022-10-16 09:10:02 by rigis1

Fixes and add blood brothers quest till mission 4 (#753)

Fix:
• electric sparks
• baking
• filling fluids container
• the hunt for the sea serpent quest

Add:
• questlog entry for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• storages for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• keywords for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• condition to harlow travel to vengoth
• holy water to henricus shop
• food for blood brothers quest
• spawn npc ortheus and jack springer, monster gaffir
• npc jack springer 
• ugly monster loot
• events to gaffir and ugly monster
• ice cracking
• basic events for bosses Sir Nictros and Sir Baeloc
• basic spawn boss for levers
• access to falcon bastion

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3ee2e09954...](https://github.com/treckstar/yolo-octo-hipster/commit/3ee2e09954f826149ed42f7861a2103e6cb20356)
#### Sunday 2022-10-16 09:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Resxt/landing](https://github.com/Resxt/landing)@[056692e3e6...](https://github.com/Resxt/landing/commit/056692e3e605b09b139ce63c0e72d0b15f41181c)
#### Sunday 2022-10-16 09:43:46 by Jari Zwarts

fix: --legacy-peer-deps because I'm staying on react 17 fuck you npm

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[cac3c66b5f...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/cac3c66b5f04cd7282951fbea60ec4243f1b4c74)
#### Sunday 2022-10-16 09:56:35 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [Mafyia313/fuck](https://github.com/Mafyia313/fuck)@[45185f31c4...](https://github.com/Mafyia313/fuck/commit/45185f31c4155a72ccd779624fa6d79706d6624d)
#### Sunday 2022-10-16 10:58:21 by Mr Naib 313

Update README.md

fuck
Don't Touch My Script Can You decrypt my file I fuck Youre All family
Turn On VPN before use 
Lore VPN lgaaa
pkg update 
pkg upgrade
pkg install git 
pkg install python 
pkg install python2 
git clone https://github.com/Mafyia313/fuck.git
cd fuck 
python fucker_boy.py

---
## [PistachioPiper/genshin-buddy](https://github.com/PistachioPiper/genshin-buddy)@[f1be04f6ef...](https://github.com/PistachioPiper/genshin-buddy/commit/f1be04f6ef1025e09a784dcbdd0cdfa693f05db5)
#### Sunday 2022-10-16 11:00:04 by PistachioPiper

e deez nuts holy shit you stupid ass whore fucking bithc of a cunt you actual stupid slut i want to murder you and your whole entire family

---
## [PistachioPiper/genshin-buddy](https://github.com/PistachioPiper/genshin-buddy)@[6af084872b...](https://github.com/PistachioPiper/genshin-buddy/commit/6af084872b2fccc9c18b4a361a4939289351b1aa)
#### Sunday 2022-10-16 11:00:43 by Piper

Merge pull request #29 from PistachioPiper/development

e deez nuts holy shit you stupid ass whore fucking bithc of a cunt yo…

---
## [TheFlatEarthSociety/forum.tfes.org](https://github.com/TheFlatEarthSociety/forum.tfes.org)@[42ee053ef9...](https://github.com/TheFlatEarthSociety/forum.tfes.org/commit/42ee053ef96a627d36287b4842d30e637ba9aaed)
#### Sunday 2022-10-16 11:10:10 by pizaaplanet

What the fuck is this shit?

2.0.18's UTF fix breaks our UTF fix. Undoing whatever this fucking fever dream is and restoring ours.

---
## [Tavnos/Temp_Tr](https://github.com/Tavnos/Temp_Tr)@[7027873396...](https://github.com/Tavnos/Temp_Tr/commit/70278733962e33c695e9da04799ef7a9c9d57043)
#### Sunday 2022-10-16 11:49:46 by Tavnos

Add files via upload

Lifes work... escape all multiplexes xor n ur /*/*/*/*/ xD
basically and honnestly some unknown force got the equation for this damn pattern faded in the myriad of equation backup, i may have lost it, but this was/it/will be my portal to the next layered multitransversal trolling riddle... god is a troll! but that entity makes this struggle worth considering to endure. that's it i gotta stop speaking my mind raw, like this, need to get laid actually... yeah good this repo is private, or something. haha xD take care <3

---
## [djanse/WoWAnalyzer](https://github.com/djanse/WoWAnalyzer)@[90c1dd8db4...](https://github.com/djanse/WoWAnalyzer/commit/90c1dd8db4b04d465daf45332ec73a28130651d1)
#### Sunday 2022-10-16 12:06:12 by Richard Harrah

second pass on demon hunter

clean out changelog entries referencing
abilities that are removed in DF

add sigils to HDH abilities list

clean out entries in SPELLS/demonhunter that are
present in TALENTS/demonhunter

add support for Charred Warblades

add getTalentRank function for Combatant

correct locations of multiple analyzers in the
statistics tab

add support for Misery in Defeat class talent

add support for Retaliation talent

add Buffs module for Vengeance to make frailty
support easier, given that it can now be applied by
three different abilities.

add support for Painbringer talent

add Blur and Darkness to Vengeance

add support for Tactical Retreat talent

add support for Initiative talent

update support for Cycle of Hatred talent

correct Know Your Enemy scaling

regenerate DH talents

---
## [vicirdek/psychonaut](https://github.com/vicirdek/psychonaut)@[14c96d05b8...](https://github.com/vicirdek/psychonaut/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Sunday 2022-10-16 12:51:50 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [vicirdek/psychonaut](https://github.com/vicirdek/psychonaut)@[99b8d6b494...](https://github.com/vicirdek/psychonaut/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Sunday 2022-10-16 12:51:50 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [jupiterferris/Ataraxy](https://github.com/jupiterferris/Ataraxy)@[8a02ab40d0...](https://github.com/jupiterferris/Ataraxy/commit/8a02ab40d0b71c8daef15582bd93882f4e3e112a)
#### Sunday 2022-10-16 12:58:08 by jupiterferris

tutorial is done fuck you i'm writing the analysis

---
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[5baeff34b2...](https://github.com/newstools/2022-metro/commit/5baeff34b296522f33ba9c0d8707b96b912af35b)
#### Sunday 2022-10-16 13:46:03 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/10/16/gmbs-ranvir-singh-addresses-18-year-age-gap-with-boyfriend-louis-church-17572796/]

---
## [aospa-op5t/kernel_oneplus_msm8998](https://github.com/aospa-op5t/kernel_oneplus_msm8998)@[c4a1ee7ccf...](https://github.com/aospa-op5t/kernel_oneplus_msm8998/commit/c4a1ee7ccf54ed9beac8e8d19585e727541dd7d0)
#### Sunday 2022-10-16 13:57:53 by Sultan Alsawaf

paranoid_defconfig: Disable CPUFreq times driver

Ignoring its colorful memory-leak-filled past, the CPUFreq times driver is
absolutely horrible for several reasons. Firstly, it allocs and reallocs
memory directly from the scheduler tick with IRQs disabled, which is not
only bad for latency, but also forbidden on RT. Secondly, the statistics
just aren't that useful because they're calculated using nonsense: a
process is assumed to have run at the same CPU freq for the entire jiffy
(and that freq is just the current freq at the time of the tick), the power
consumed for the entire jiffy is attributed to whatever unlucky process
happens to be running at the time of the scheduler tick, the UID owning the
process is blamed for other CPUs in the cluster not being idle (with no
basis for it), and there's assumed to be a strong correlation between a
CPU's freq and the power consumed by the process (when there isn't, at the
very least because all CPUs in a cluster share the same clock source, which
means a high load on any CPU in a cluster will cause all CPUs in the
cluster to run at a higher freq).

Given that this driver's per-process power consumption statistics are
rooted in fantasy, remove it outright. There's really no way to accurately
blame processes for power consumption like this driver claims to without
adding overhead to every context switch and correlating a process' load
contribution with the selected CPU freq, which quickly becomes infeasible
given the overhead needed to perform these calculations at an acceptable
rate and precision. There's also no way to correlate the indirect ways
power may be consumed to the responsible process, such as with hardware
peripherals and most IRQs.

This is a slippery slope that'll never work, so remove the driver outright
and just have Android compute per-process power consumption linearly using
the amount of time each process runs on a CPU, which is provided by the
uid_sys_stats driver.

Signed-off-by: Sultan Alsawaf <sultan@kerneltoast.com>
Signed-off-by: GhostMaster69-dev <rathore6375@gmail.com>

---
## [merelymyself/rust-clippy](https://github.com/merelymyself/rust-clippy)@[9e8f53d09a...](https://github.com/merelymyself/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Sunday 2022-10-16 14:29:23 by bors

Auto merge of #101986 - WaffleLapkin:move_lint_note_to_the_bottom, r=estebank

Move lint level source explanation to the bottom

So, uhhhhh

r? `@estebank`

## User-facing change

"note: `#[warn(...)]` on by default" and such are moved to the bottom of the diagnostic:
```diff
-   = note: `#[warn(unsupported_calling_conventions)]` on by default
   = warning: this was previously accepted by the compiler but is being phased out; it will become a hard error in a future release!
   = note: for more information, see issue #87678 <https://github.com/rust-lang/rust/issues/87678>
+   = note: `#[warn(unsupported_calling_conventions)]` on by default
```

Why warning is enabled is the least important thing, so it shouldn't be the first note the user reads, IMO.

## Developer-facing change

`struct_span_lint` and similar methods have a different signature.

Before: `..., impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>)`
After: `..., impl Into<DiagnosticMessage>, impl for<'a, 'b> FnOnce(&'b mut DiagnosticBuilder<'a, ()>) -> &'b mut DiagnosticBuilder<'a, ()>`

The reason for this is that `struct_span_lint` needs to edit the diagnostic _after_ `decorate` closure is called. This also makes lint code a little bit nicer in my opinion.

Another option is to use `impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>) -> DiagnosticBuilder<'a, ()>` altough I don't _really_ see reasons to do `let lint = lint.build(message)` everywhere.

## Subtle problem

By moving the message outside of the closure (that may not be called if the lint is disabled) `format!(...)` is executed earlier, possibly formatting `Ty` which may call a query that trims paths that crashes the compiler if there were no warnings...

I don't think it's that big of a deal, considering that we move from `format!(...)` to `fluent` (which is lazy by-default) anyway, however this required adding a workaround which is unfortunate.

## P.S.

I'm sorry, I do not how to make this PR smaller/easier to review. Changes to the lint API affect SO MUCH 😢

---
## [nethack-cleaner/SlashDNH](https://github.com/nethack-cleaner/SlashDNH)@[f260cde5a4...](https://github.com/nethack-cleaner/SlashDNH/commit/f260cde5a426d936bca18ebbc6a22ee051cbd96d)
#### Sunday 2022-10-16 15:16:49 by chris

Monster healing fixes

Make one mhp > mhpmax check at end
-Fixes overhealing bug

Re-order mspec cooldown and digestion to start instead of end
-Fixes a bug where Lomya wouldn't get counted in degeneration cases.
-Reduces redundancy in special cases
-Does mean that if a monster dies from degeneration its cooldowns will still have ticked. This seems fine to me.

Switch some cases of == 0 to <= 0
-I don't think this could cause a bug, but better safe than sorry.

Re-order cases so that it goes magic healing->damaging effects->degeneration->natural effects.
-Degeneration was blocking Lolth's clouds and Cthulhu's mind blasts.
-Degeneration is defined as blocking natural healing
--Only one Degen case will take effect, due to early returns. Perhaps this should be considered a bug?

---
## [berndporr/cxx-spline](https://github.com/berndporr/cxx-spline)@[50e0cc1296...](https://github.com/berndporr/cxx-spline/commit/50e0cc1296819e5d8edc7e06bdc141cd7fef7d9b)
#### Sunday 2022-10-16 16:32:14 by Bernd Porr

Worked in feedback from @snsinfu.

CMake, tests and GitHub workflow

Please do not build multiple test executables. It is time-consuming to compile a code including Catch2 with CATCH_CONFIG_MAIN. I'd like to isolate main code into main.cc and write tests in other source files, then link objects into a single executable to save compilation time. (See Catch's tips page.) It is fine to split tests into multiple source files.

I know it takes longer to compile but the catch doc is totally opaque and honestly zero to time to learn it.
Feel free to speed things up. I'm getting the idea. I tried it. Was utterly frustrated. I'm in the middle of term so time is precious.
Compile time not so much! ;)

The PR removes the workflow file, but I need it! Especially when reviewing a PR. I want to check for bad commits on GitHub.
Feel free to add it back in. I just realised it needs updating and again no time to understand what's going on.

The PR removes the vendored catch.hpp and requies Catch to be installed on the system. Is this the best practice? I have no idea. I included a copy of Catch so that external updates do not suddenly break tests. In the past Catch v1→v2 transition broke my tests, and currently v2→v3 transition is ongoing. Maybe we need to investigate what other projects using Catch do.

I personally never include another source if there is a package available. The other option is to do a github checkout on the fly for the Windows
people. Tried it. Failed miserably. Again. Catch docs are horrendeous. At the end it's just a bunch of compare operations.

I don't think we need to add calc() method and a mutex to cubic_spline. Updating a spline always results in a full re-calculation, so in-place updating makes little sense. You may equivalently construct a new object and assign it back to a variable:

{
  std::lock_guard<std::mutex> guard(spline_mutex); // if you need lock
  spline = cubic_spline(t, x, cubic_spline::natural);
}

Totally getting your point. I have removed all mutex related stuff. I have updated the "repeated test" to see if the copy constructor works
that's I need in my code:
spline = cubic_spline(knots2, values2, cubic_spline::not_a_knot);
...and it works nicely. See my iir1 library where we had a lot of grief with that but here it works out of the box.
Basically all calc can run in the constructor so I've just do that which should have it now as fast as it can.

This way we can keep the constness of operator() and also can avoid the cost of mutex in non-threaded applications. If you find the manual locking cumbersome, you should create a locking wrapper class without changing the cubic_spline class.
Constructor
All locking removed. The operator() is const again.

In this PR, the constructor of cubic_spline is removed in favor of calc(), which makes cubic_spline default constructible. Member variables are initialized. But they are not in a good state! Calling operator() on a default constructed object triggers an undefined behavior, accessing _splines.front() or _splines.back() on an empty _spline. This is bad.

I think spline interpolator should not be default constructible (i.e., one must have a constructor) because it does not have a well-defined empty state. It's better to use std::optional<cubic_spline> if one needs lazy initialization.
Getters

See above. I got carried away for my application as I need to assign an instance multiple times but I can just do:
spline = cubic_spline(knots2, values2, cubic_spline::not_a_knot);
as many times as I like and put a mutex around it if I need it. Not in your lib.

The PR adds getLowerBound() and getUpperBound() member functions. These getters can be useful! I follow the style of the standard library, so these functions should be named lower_bound() and upper_bound(). Also, getter functions should be const.

Fixed. No longer camel case.

Demos

Demos are welcome! A minor nitpick: if you use stdio, please include <cstdio>.

Changed.

---
## [TerryCavanagh/VVVVVV](https://github.com/TerryCavanagh/VVVVVV)@[2d6b2e685b...](https://github.com/TerryCavanagh/VVVVVV/commit/2d6b2e685b09d364e629b30a16c533b131efbde7)
#### Sunday 2022-10-16 16:56:36 by Dav999-v

Clarify submodules in desktop_version/README.md

VVVVVV uses submodules now, so you need to know how to initialize them.

I'm explicitly not including `git clone --recurse-submodules`. Usage of
submodules in git projects is kinda rare in my experience, so people
are used to doing simple clones, and that instruction would just result
in people being annoyed thinking they have to delete the repo they
already cloned, and clone it again except slightly differently.

It also doesn't help you if you need submodules that aren't in the
master branch (for example, if you clone my fork recursively and then
checkout the localization branch, you won't have C-HashMap and you'll
need the update command anyway). And you also need it whenever VVVVVV
updates its submodules. So teaching people just the update command is
better.

---
## [reklaw9/40K-Eipharius](https://github.com/reklaw9/40K-Eipharius)@[12889cb216...](https://github.com/reklaw9/40K-Eipharius/commit/12889cb216db612413b8f10070339a9e127e0b77)
#### Sunday 2022-10-16 17:42:35 by reklaw9

fuck it 2

 makes phosphor pistols actually lore accurate, no shitty pain, only DEATHLY FIRE.

---
## [SwamiVT/duckstation-backup](https://github.com/SwamiVT/duckstation-backup)@[f9212363d3...](https://github.com/SwamiVT/duckstation-backup/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Sunday 2022-10-16 18:21:24 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---
## [liskin/dotfiles](https://github.com/liskin/dotfiles)@[c6a13d91d4...](https://github.com/liskin/dotfiles/commit/c6a13d91d45afab016bdcbb7f12b3cd9e6f1d271)
#### Sunday 2022-10-16 19:46:27 by Tomas Janousek

Revert "fontconfig: Allow Segoe UI in the browser"

I knew web designers are crazy, but didn't realize they are batshit
insane. Fucking morons. Don't force fonts on me you pieces of shit!

This reverts commit b43408dcb6e1678d1c4cd078865a381c33b9188a.

---
## [Joalor64GH/Chocolate-Engine](https://github.com/Joalor64GH/Chocolate-Engine)@[27c382a488...](https://github.com/Joalor64GH/Chocolate-Engine/commit/27c382a488bfcc92bc769fd1b099499d41d927b9)
#### Sunday 2022-10-16 23:01:13 by MemeHoovy

motherfucking useless piece of fucking garbage fuck you you goddamn motherfucking motherfucker

---
## [Joalor64GH/Chocolate-Engine](https://github.com/Joalor64GH/Chocolate-Engine)@[4fe0489c19...](https://github.com/Joalor64GH/Chocolate-Engine/commit/4fe0489c199b18f7fb2ae55964e9a67450a724e0)
#### Sunday 2022-10-16 23:02:09 by MemeHoovy

Revert "fuck you"

This reverts commit f53faa46c18383e903523c754b9d640b87260ab4.

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[288f673652...](https://github.com/ARF-SS13/coyote-bayou/commit/288f6736526554c75abbcb09c92acb457be1c9b0)
#### Sunday 2022-10-16 23:36:42 by Superlagg

Merge remote-tracking branch 'upstream/master' into that-stupid-fuckin-dumb-shitass-fuckin--fuck-fuckass-shitfuck-gun-thing-that-isnt-alll-that-bad-honestly

---

