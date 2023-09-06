## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-05](docs/good-messages/2023/2023-09-05.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,337,681 were push events containing 3,528,993 commit messages that amount to 281,063,329 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [OctusGit/Paradise](https://github.com/OctusGit/Paradise)@[a3dc32cf34...](https://github.com/OctusGit/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Tuesday 2023-09-05 00:39:23 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[06e7270008...](https://github.com/Ghommie/tgstation/commit/06e7270008d4b49a7e73fd088135822a9ec76891)
#### Tuesday 2023-09-05 01:09:30 by GuillaumePrata

Funny clown internals (#77963)

# About The Pull Request
This PR changes the internals that spawn inside the clown's survival box
for a new one with a rainbow sprite, higher O2 volume (same as the engi
ones) and a secondary gas on top of O2 to make things more interesting
for the clowns.
The gas options are:
BZ, which just adds hallucinations for the clown, without the brain
damage effect as it is in low percentages.
N2O will make the clown giggle and laugh, without the sleep.
Helium will give the clown a "funny voice".

These tanks are also added to the mail list of clown fans and the clown
costume crate at cargo.

And codersprites, I can polish them later if people think it is pixel
soup, I'm not happy with them that much, but making this looks good
might be above my paygrade...
<details><summary>Pics here</summary>
<p>


![clown_internals](https://github.com/tgstation/tgstation/assets/55374212/f5eda877-a01a-4dfa-b481-7d406c4fb768)

![in game clown
internals](https://github.com/tgstation/tgstation/assets/55374212/342285ae-919b-49ab-a97e-cdf25a975f83)


</p>
</details>

## Why It's Good For The Game
The main goal I have with this is to add more uses for Atmos Content to
other players in a flavorful way.
Atmos is not something the crew interacts in a positive way often and I
want to change that.

These tanks are something quite minor but flavorful IMO, also will make
people know Helium fucking exists...

The tanks *shouldn't* change much of the clown's round in a negative
way, and the default O2 internals are in every hallway's locker so even
if they don't want to deal with the hallucinations it is not a big deal
to dodge them.
## Changelog
:cl: Guillaume Prata
add: New funny internals for the clowns to spawn with. They come with O2
and a secondary gas between 3 options: BZ, Helium and N2O. Talk with a
"different tone" with Helium, giggle and laugh "uncontrollably" while
under the minor effects of N2O or have "fun" hallucinations while under
the minor effects of BZ.
balance: To not cut on how long the clown's O2 internals last due to the
mixed gases, the funny internals have 50% more gas volume, same as
engineers' internals.
/:cl:

---------

Co-authored-by: CRITAWAKETS <sebastienracicot@hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [1080pCat/Paradise](https://github.com/1080pCat/Paradise)@[acb7352265...](https://github.com/1080pCat/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Tuesday 2023-09-05 01:30:16 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [water-sucks/nixed](https://github.com/water-sucks/nixed)@[4cd942d582...](https://github.com/water-sucks/nixed/commit/4cd942d5823fffee528ee512bc7a4c9c3b8e141a)
#### Tuesday 2023-09-05 02:08:08 by Varun Narravula

fix: persist volume on NixOS systems

Oh my fucking God, it was WirePlumber. And the fact that I didn't
persist all the right directories. Welp, I love life. At least this
works now.

---
## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[cf0be10b07...](https://github.com/francinum/Therac-Gameserver/commit/cf0be10b075f2c64220e81d653075b7bcd8fe060)
#### Tuesday 2023-09-05 02:15:03 by Kapu1178

Drunk slurring scales based on how drunk you are (#75459) (#460)

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...

![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11

![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[9ea70e75de...](https://github.com/mc776/freedoom/commit/9ea70e75de134e0922ed4120e05721f73dd2b097)
#### Tuesday 2023-09-05 03:16:34 by mc776

levels: various QOL fixes.

Generally there should be nothing *necessary to finish a level* that requires any of:
- straferunning;
- extremely sensitive timing that could softlock you if you're on keyboard, lagging in multiplayer or have motor issues;
- checking only for a sound cue that something has happened;
- remembering how to distinguish two visually nearly identical areas; or
- backtracking to a previous area on the map that you had previously been given no reason to revisit.

I haven't caught all of them by any stretch of the imagination but it's a start.

Also some regular minor fixes.

E1M9
- Fixed some textures around the big blue-trimmed lift and removed an extraneous use line that triggered a faraway lift for no reason.
- The red key bridge lowerable section is now textured differently from the rest of the bridge.

E3M5
- Teleporter platform to get back up to the catwalk from the northeastern blood maze is now clearly marked as having a switch, as it is a mandatory progression rather than a secret.

E4M8
- Got rid of some fake contrasts on the noodles at the start.
- Added a radsuit for the northwest switch. While it is possible to avoid damage even without straferun, unless you've got a tic counter display and can time it to the damage interval this is basically RNG.
- The water flat on top of the lowering wall in the east was very, very noticeable. The switch is now stepped on instead of hit. (Not too sure if the secret isn't *too* obscure now...)
- Removed asymmetrical doortrak on the slime bridge on the southeastern piston switch.
- The linedefs of said slime bridge pit are flipped so a deathmatch opponent trying to grab the berserk in there is not magically immune to rocket blasts. (see #996)
- Realigned the four pistons by the gate to the starship. They also reveal moving parts when activated - not nearly as good as the crushers on the original DI, but better than nothing.
- Made the southern walls use PLAT1 to make it more obvious that those walls will lower later (with the added bonus that they match the four pistons).
- The southern light bronze area now has a strip to guide the player towards the switch in case they lose track of their direction while fighting monsters and forget to explore inside that area, as well as to better distinguish it from the southeast.
- The gate threshold to the southern light bronze area now matches that of the pre-opened southeast.
- There is now actually a threshold where you can tell where the starport ends and the ship begins.
- The two light bronze areas are a bit too similar-looking. Added a few health boosts so the player can spot/be attacked by them and know this is an unexplored area.

Map11
- The lift going down into the yellow key room requires a switch that is out of sight from the lift itself, which is not clearly marked as a lift to begin with. The only real way to realize what's going on if you don't already know about the lift is to locate the sound and immediately turn to investigate before the lift comes back up. I thought this was annoying when I first did my big overhaul of this map, but ultimately left the basic mechanism alone out of an abundance of caution; however, with the recent discussion of accessibility in the proposed changes to the documentation I'm revisiting this. That upper switch now lowers a wall to reveal the lift which is triggered by a walk line.
- The lower far switch on that same lift was actually literally *impossible* to make on keyboard and no straferun (and no vanilla wallbounce exploit), even if I change it to a regular lift instead of fast. This is completely unacceptable for something necessary to progression (rather than an obscure secret). The lower switches are now permanent repeatable floor-lowerers, while the line crossing from the lift into the lower chamber is a permanent repeatable floor-raiser, with the line crossing into the lift from above being a simple lift line.
- Retextured the stairs out of the water in the eastern branch so it's not an unreadable mess of criss-crossing grey lines.
- Realigned the new skull switch texture in the skull room.

Map19
- One of the stealth worms was stuck in a burning barrel.
- Removed monster block flag on line 2083.
- Unmerged and remerged a few identical sectors to better match the intended sound travel.
- Flagged line 281 as a monster blocker. This allows the player to always be able to make the jump onto that bottom stair without being blocked by the octaminator.
- That octaminator is now a pain bringer in easy mode. The far end of that platform path is well outside the maximum vertical autoaim range in vanilla, which means that to actually hit the octaminator without up/down aiming you'd have to be on one of the later platforms - i.e., confined to a relatively narrow area with no cover *against an opponent that has seeker missiles*. The best way to solve this is to charge towards the octaminator as fast and as soon as possible with the SSG, minigun, or ripsaw+prayer to RNGsus that you'll get a good painlock. This is not the kind of tactic the sort of person who *needs* to play on easy will think to do, or could do while also being ready to sidestep if the octaminator fires at the wrong time.
- 347 and 249 are now also monster blockers, and the worms in that slime pit have been moved to the platform just behind the combat slug since they're awakened early on and that's where you'll first encounter them anyway.
- Replaced the teleport pad in the vertical platforming sequence with a lift, to minimize disorientation and going the wrong way. (In retrospect I probably could have just made the teleport destination face the pit you came in from, but the lift worked aesthetically better anyway.)
- A good chunk of that entire platforming area has been moved 8 units to the west so that things would align with the flat grid.
- Lines 307 and 309 are now also monster blockers. The worm that would be trapped between them is now moved further down the route and marked ambush.

Map20
- Removed the useless, misleading skull switch texture on the bars at the start.
- The door leading into the blue key arena needs no blue key; the door leading out needs a blue key. Both are marked with blue-light trim. Removed the blue lights on the first one.
- The lowering wall leading to the teleporter now uses a pipe texture.
- The door leading out of the giant quadruped arena now has a bright flickering light.
- Yellow key is another case of effectively-randomly-mandatory damage. Added a path.
- Same with the lava tunnel on the red key route.

Map25
- The silver lift near the river and shack is now activated by SW1GSTON switch right on the wall at eye level, rather than counterintuitively and invisibly recessed into additional sectors.
- The painlord ambush lift is now accessible after the encounter. A small health refill has been added there for easy and medium.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[4792a8e19d...](https://github.com/lessthnthree/tgstation/commit/4792a8e19dc6885a2f6e8d25f1086505624e7a6c)
#### Tuesday 2023-09-05 03:17:40 by carlarctg

Nerfs Confusion symptom for diseases (#77991)

## About The Pull Request

Removed the threshold for confusion symptom that adds illiteracy to the
disease.

Clamps confusion symptom's confusion to a maximum of 30 seconds.

Confusion as a debuff no longer guarantees random movement if you're
resting.

## Why It's Good For The Game

> Removed the threshold for confusion symptom that adds illiteracy to
the disease.

This virus makes you unable to actually treat yourself when cured, which
is frankly bonkers. Viruses are too virulent and it's rare that a doctor
actually gets to a biosuit in time to inoculate themselves, and if they
forget internals they're screwed anyways. People should be able to fix
their own got damn disease, this is asinine.

> Clamps confusion symptom's confusion to a maximum of 30 seconds.

The lack of clamping literally makes this symptom send your confusion
level to the fucking atmosphere, you can easily get upwards of 5 minutes
of confusion left because it doesn't clamp, adds 16 seconds per
activation, which is made even worse by the fact that confusion gets
stronger the more duration confusion has on you.

> Confusion as a debuff no longer guarantees random movement if you're
resting.

This remedies the last bit by not making it a literal guarantee that you
can't move in any direction after...... *3* triggers of confusion. It
should be obvious to anyone how absurd this is.

Honestly, it's plain as day that the only reason any of this ended up
like it is because of poor coding and oversights. This is just bringing
things down to their designed level.

## Changelog

:cl:
del: Removed the threshold for confusion symptom that adds illiteracy to
the disease.
balance: Clamps confusion symptom's confusion to a maximum of 30
seconds.
qol: Confusion as a debuff no longer guarantees random movement if
you're resting.
/:cl:

---
## [Merek2/coyote-bayou](https://github.com/Merek2/coyote-bayou)@[38f0f053be...](https://github.com/Merek2/coyote-bayou/commit/38f0f053be0bdbafea827fdb8b9b7dd6535e3323)
#### Tuesday 2023-09-05 03:33:58 by Tk420634

Merge pull request #2951 from ARF-SS13/Fixes-wooden-shelves-at-their-core

Fuck you

---
## [EuansPrivateORG/DemonGame](https://github.com/EuansPrivateORG/DemonGame)@[6250525b73...](https://github.com/EuansPrivateORG/DemonGame/commit/6250525b73897a7067fb97a22ba30659b27c5c05)
#### Tuesday 2023-09-05 05:32:23 by AIE\s200552

REALTIME CSG I LOVWE YOU HOLY SHIT I GOD DAM HATE WHEN THIS ASTUPID BUGH KEEEORPS SDHIASHOWEING UPS

---
## [Vasudev-22/magento2](https://github.com/Vasudev-22/magento2)@[b6fbaeb89a...](https://github.com/Vasudev-22/magento2/commit/b6fbaeb89a5f14b195b6bb84546db895afcf7a1e)
#### Tuesday 2023-09-05 05:57:12 by Igor Wulff

Improve performance of DataObject magic calls and addData()

The magic calls from the DataObject are being called over a 100k when there is no block_cache available and depending on the page often thousands of times when all block_cache is available.

The small change for addData() is just included because its a tiny optimization and prevents a bug from happening. When a $value is an array the original call to setData would override the internal $_data array, this is not expected behavior and just setting it directly to $_data is faster anyway.

The other change is in the __call magic method and the _underscore function and the change is quite radical.
Since this method can be called so often, we want to prevent further function calls if possible. Functional calls are normally not that expensive, but will become more expensive if you use this extensively (thousands of even hundred of thousands extra calls):

These are my own benchmarks based on a local environment with opcache and with PROD mode. 

HOMEPAGE transaction
All cache enabled except for FPC (__call is called 975 times): 4.318307ms -> 1.469747ms
All cache enabled except for FPC + Block_html  (__call is called 100379 times): 385.36412ms -> 88.412914ms

PLP transaction:
All cache enabled except for FPC  (__call is called 4628 times): 19.625463ms -> 5.754514ms
All cache enabled except for FPC + Block_html (__call is called 112591 times): 404.84066ms -> 99.390374ms

Now this PR also skips some checks. It assumes if a $method call start with 'g' it will be for 'get' for example, this is done in my PR to get the most optimal performance result but might not be preferred. I also removed an index check with $args[1] for the setter since it isn't used anywhere, but might also be something we would want to change.

---
## [DETrooper/Begotten-III](https://github.com/DETrooper/Begotten-III)@[a65c4b10e8...](https://github.com/DETrooper/Begotten-III/commit/a65c4b10e82e0c79548033da3ac50389b389061e)
#### Tuesday 2023-09-05 06:29:50 by DETrooper

Possession Changes, Roaches, Fixes

- Added a small amount of XP gain for mutiliating animals/corpses. Harvesting corpses will also now degrade dagger durability.
- Added the fucking roaches...
- Added XP values for killing Gore Forest animals. Summoned spirit bears will have a slightly higher XP value than normal cave bears due to their buffed HP.
- Expensive properties in the Tower of Light now have more storage space in their stashes. Lower end properties have the old default 40, medium tier properties have 60, and high tier properties (hotel rooms) have 100. High-end property prices have been raised moderately.
- Fix for accidental double-clicking in the weapon select menu.
- Fixed being able to change to senses while mid-swing to activate it erroneously.
- Fixed NPCs attacking dead bodies.
- Fixed some stamina bugs.
- Fixed sound effects for some thralls being broken.
- Insane players that cannot hear IC chat can no longer hear radios, nor any faith-based communications (i.e. darkwhisper, ravenspeak, relay). Also fixed them being able to hear the message for someone yelling too far away.
- Minor optimizations.
- NPCs summoned by rituals no longer give any XP to players of the same faith as the summoner when killed.
- Possession changes:
	- Added a new radial menu (tab key) for possessors to quickly run relevant commands.
	- Demon heal now resets poise/stability/stamina.
	- Increased the trait points given for taking 'Possessed' from 4 to 6.
	- /PlyMakeFreakout now checks for the 'Possessed' trait and the new 50% corruption requirement, but this can also be ignored by supplying an argument in the command to do so.
	- Taking the 'Possessed' trait will now result in your character passively accruing corruption, but you can now not be possessed until your corruption level reaches 50%. This can be ignored by the admins if needed, though.
	- While actively possessed, characters will not lose sanity or other character needs, and will also take less stability and poise damage in addition to less health damage.
	- Various other improvements to reduce possession jankiness.
- Raised the maximum number of NPCs that dynamically spawn from 4 to 8.
- The 'Marked' trait now gives an extra trait point.
- The rare 'explosion' suicide method actually explodes you now.
- The weapon selection UI now hides while swinging a melee weapon.
- Updated the thralls to use full models instead of kitbashed parts (thanks filterfeeder!), which should hopefully result in much improved performance.
- XP is now distributed for NPC kills by character key instead of by player index.

---
## [TimUkrainian/zechub](https://github.com/TimUkrainian/zechub)@[5a6601eb41...](https://github.com/TimUkrainian/zechub/commit/5a6601eb41f22a7d984aa1fcb4ddb4c41d704765)
#### Tuesday 2023-09-05 06:42:55 by Hardaeborla

Non Custodial Exchanges.md



In the ever-evolving world of cryptocurrency trading, the rise of non-custodial exchanges which is also known as Decentralized Exchanges or DEXs is redefining how users engage with digital assets. These platforms offer a revolutionary approach to trading by eliminating the need for intermediaries or third party and putting control firmly in the hands of users.

It is also undoubtedly that as Zcash is concerned, privacy matters as it remains an innovative project that pushes the boundaries of privacy within the cryptocurrency space, offering users the option to transact in a more confidential and secure manner.

In this piece, we'll delve into the present non-custodial exchanges that enable you to effortlessly obtain and trade Zcash independently, without the need for intermediaries in the transaction process. Before we dive into these accessible non-custodial exchanges for acquiring Zcash, let's take a quick look at Non-Custodial Exchanges (DEXs) vs Centralized Exchanges to gain a better understanding.

### **Understanding Non Custodial Exchanges In Brief** 
Non-custodial exchanges, also known as Decentralized Exchanges (DEXs) are platforms that facilitate cryptocurrency trading without requiring users to deposit their funds into the exchange itself. Instead, users retain control of their private keys and trade directly from their wallets without the need for third parties. This decentralized approach enhances security and privacy, as users are not reliant on the exchange to hold their assets which also reduces the risk of hacks or mismanagement. Transactions on non-custodial exchanges often leverage smart contracts to ensure trustless and transparent trading. 

A key advantage of non-custodial cryptocurrency exchanges lies in the increased control they provide to users over their assets. As these exchanges don't retain the assets, users enjoy complete ownership and authority over their digital currencies. This aspect can be especially attractive to individuals worried about asset security.

### **Understanding Custodial Exchanges** 
Custodial Exchanges are also known as centralized Exchanges. They are cryptocurrency trading platforms where users deposit their funds into accounts managed by the exchange itself. In this model, users entrust the exchange with the custody of their assets, meaning the exchange holds and controls the private keys necessary to access and manage the cryptocurrencies. This setup can provide convenience, especially for newcomers to the cryptocurrency space, but it also means users are reliant on the exchange's security measures. While custodial exchanges often offer user-friendly interfaces and customer support, they may present higher security risks due to the centralization of funds and the potential for hacks or mismanagement.


An advantage of custodial exchanges is their provision of a straightforward and user-friendly interface, simplifying the initiation of crypto trading for newcomers. Additionally, these exchanges offer an array of functionalities, including charting tools, real-time market information, and the capability to establish stop-loss orders, catering to the needs of more seasoned traders

### **Non Custodial Exchanges Vs Custodial Exchanges** 

**#1 Security**
Non-custodial exchanges eliminate the need for users to trust a central entity with their funds or assets. This enable users to maintain and have control of their private keys, reducing the risk of hacks, insider attacks and platform vulnerabilities that custodial exchanges may experience. 


**#2 Privacy**: Non-custodial exchanges often provide greater privacy by allowing users to trade directly from their wallets without the need for any intermediary. Transactions can be executed with greater anonymity, as sensitive information is not stored unlike Centralized Exchanges 


**#3 Decentralization**: Non-custodial exchanges align more closely with the decentralized ethos of cryptocurrencies. Users have greater autonomy and control over their trading activities, in line with the broader principles of blockchain technology.

When it comes to Custodial Exchanges, the level of Decentralization is often quite minimal in most centralized exchanges which give rise to the exchange team or officials managing user data or information on the exchange. 


**#4 Adaptability to Changing Regulations**: Non-custodial exchanges are often more adaptable to changing regulatory environments. Since they do not hold user funds, they might have fewer compliance challenges compared to custodial exchanges.




**#5 Innovation and Experimentation**: Non-custodial exchanges frequently drive innovation in the crypto space. They encourage the development of decentralized technologies, such as automated market makers (AMMs) and decentralized finance (DeFi) applications.



**#6 Global Accessibility**: Non-custodial exchanges often provide access to cryptocurrencies for users around the world, including regions where regulatory hurdles might limit the availability of custodial exchange services.

**#7 No KYC Requirements**: 
Many non-custodial exchanges do not require users to undergo extensive know-your-customer (KYC) procedures, offering a level of privacy and inclusivity that is absent in some custodial platforms.



While non-custodial exchanges offer compelling advantages, it's important to acknowledge that they might come with drawbacks, such as potential liquidity issues and a steeper learning curve for less experienced users. As with any financial decision, traders should carefully assess their priorities, risk tolerance, and familiarity with the technology before choosing between non-custodial and custodial exchange options.

Now, let's explore a few of the accessible non-custodial exchanges that facilitate Zcash trading. Utilizing these platforms will provide you with a convenient means to acquire more Zcash coins.

### **Non Custodial Exchanges To Trade or Acquire Zcash**

**#1 Simple Swap** 
SimpleSwap presents an exchange platform providing swift and straightforward swaps for users globally. The process is uncomplicated as it enable users to exchange cryptocurrencies, earn SWAP tokens, acquire a subscription and acquire BTC. No registration is necessary for conducting exchanges through the SimpleSwap Mobile App or web service.

SimpleSwap supports Transparent Address on both Zcash Blockchain and Binance Smartchain (Bep20). It enables you swap your Zcash tokens into other supported coins like USDT very easily. Follow the below steps as tested by [Zula](https://free2z.cash/Zula/zpage/como-hacer-intercambio-de-zecs) 

* Visit [SimpleSwap](https://simpleswap.io/) either Web or mobile app. 


* Select the Supported Crypto Pairs, in this case I'm selecting ZEC and USDT 

* Enter amount of ZEC you intend to swap on the DEX and paste the address. 










 

SimpleSwap DEX Link :https://simpleswap.io

Mobile App (Android):https://simpleswap-subdomain.onelink.me/XxkL/4d83a727


Mobile App (iPhone):https://simpleswap-subdomain.onelink.me/XxkL/85fe1e52

**#2 Fixed Float** 
Fixed Float is another non Custodial Exchange that has been in existence since 2018 and it equips you with the means to fully leverage your digital assets via a user-friendly and accessible exchange platform. 

[Fixed Float](https://fixedfloat.com/) also supports swapping and trading of Zcash on it's DEX as it enables you to swap ZEC easily into other supported cryptos available on the DEX.

[Fixed Float](https://fixedfloat.com/) can easily be used to swap ZEC as explained by [Zula](https://free2z.cash/Zula/zpage/como-hacer-intercambio-de-zecs) in the below description;

FixedFloat DEX Link: https://fixedfloat.com


**#3 SideShift** 
Experience the No Registration Crypto Exchange. Seamlessly switch between BTC, ETH, BCH, XAI, and over 100 other cryptocurrencies all without needing an account using SideShift.

SideShift is another non-custodial exchange that facilitates trading of Zcash. It supports both shielded and transparent Zcash wallet addresses on its decentralized exchange (DEX), offering user-friendly accessibility for Zcash trading.

Check out the guide on how to swap your ZEC on SideShift in the below description;


 
**#4 Changelly**
[Changelly](https://changelly.com/) stands out as a user-friendly non-custodial exchange that enables hassle-free trading or swapping of Zcash for various other supported assets. 

During the swapping process, this non-custodial exchange facilitates transactions with Zcash Transparent wallets. Discover the instructions below for guidance on how to proceed:


You can learn more about how it works [here](https://changelly.com/blog/how-to-exchange-crypto-on-changelly/) 

Changelly DEX Link: https://changelly.com/


**#5 Trocador** 
[Trocador](https://trocador.app/en/) serves as a privacy-centric exchange aggregator. The team hold the conviction that cryptocurrency possesses the potential to counteract government overreach, censorship, and tyranny, fostering decentralization and liberty for a world that thrives in prosperity and freedom.

This Non Custodial Exchange also support the trading of Zcash by depositing and withdrawing through the Zcash mainnet address. 

Trocador DEX Link: https://trocador.app/en/


**#6 Swapzone** 
Swapzone is Swapzone is a cryptocurrency exchange aggregator that enables user to browse through services, compare exchange rates, analyze and swap cryptocurrency in just one interface. All swaps are custody-free, with no registration needed.

[Swapzone](https://swapzone.io/) also supports the trading and swapping of Zcash including deposits and withdrawals of Zcash addresses such as Transparent, Bep20, Hecochain and BEP2. 


Swapzone Link:https://swapzone.io/

**#7 Flyp**
Flyp stands as the swiftest, most secure and exceedingly confidential means of swapping over 30 cryptocurrencies directly into your wallet. There's no need for registration, email, or an account. A single click effortlessly facilitates instantaneous exchanges. Your privacy and private keys are under your constant command. The process is as straightforward as executing a transaction from your own wallet. 

The good news is that Flyp.me also supports Zcash transactions on it's DEX, users have option to input either their Transparent Address (recommended) or shielded or unified address. 


Flyp.me DEX Link: https://flyp.me/



**#8 Pancakeswap** 
[Pancakeswap](https://pancakeswap.finance/swap) stands as the top decentralized exchange on the BNB Smart Chain, boasting the market's highest trading volumes.

The non Custodial Exchange supports swapping of Zcash (Bep20) into other crypto assets on the BNB Chain Cake, BNB, USDT and others. 


DEX Link:https://pancakeswap.finance/swap

**#9 Decred** 
Decred DEX enables you to engage in peer-to-peer cryptocurrency trading without any trading fees or KYC requirements. DCRDEX represents a decentralized exchange crafted by the Decred Project.

[Decred DEX](https://dex.decred.org/) also supports the Swapping and trading of Zcash on it's DEX and users are able to deposit and withdraw Zcash tokens either transparently or privately. 

DEX Link : https://dex.decred.org/

**#10 GODEX** 
[GODEX](https://godex.io/) stands out as a high-speed exchange platform, with order executions typically taking between 5 to 30 minutes. The execution time is contingent upon confirmation speed within the decentralized network, with larger amounts, such as those exceeding 1 BTC, often requiring more time. The DEX dependability rests on contemporary security protocols and robust physical server protection.

The DEX offers support for both Transparent (t-address) and Shielded (z-address) transactions from the Zcash Network. GODEX further facilitates the effortless swapping and trading of tokens.

DEX Link: https://godex.io/
Android App:  https://play.google.com/store/apps/details?id=com.godex.app.GodexApp




**#11 ChangeNow** 
ChangeNOW operates as a non-custodial platform designed to facilitate swift and straightforward cryptocurrency exchanges. The DEX focus is on providing the utmost security, ease of use, and convenience. The DEX neither retain your funds nor mandate any form of account setup. With nearly 700 coins accessible for exchange, ChangeNOW imposes no restrictions; you can perform exchanges to your heart's content without an account, all while ensuring a speedy process. 

ChangeNOW also supports Zcash deposit and withdrawals using address from Zcash mainnet and Bep20 (Binance Smartchain) Network. 

**#12 StealthEx** 
StealthEX offers non-custodial cryptocurrency exchanges where there's no need to set up an account or reveal personal information. Additionally, funds are not stored on StealthEX; exchanges occur directly between wallets.

[StealthEX](https://stealthex.io/) also supports the withdrawal and deposits of Zcash mainnet addresses including swapping and trading of Zcash. 

DEX Link: https://stealthex.io

Mobile App : https://play.google.com/store/apps/details?id=com.stealthex

**#13 SwapSpace** 
SwapSpace serves as a real-time aggregator for cryptocurrency exchanges. The platform empowers you to select from various swap offers provided by major crypto exchanges, all conveniently assembled in a single location. [SwapSpace](https://swapspace.co/) is committed to streamlining the exchange experience, granting access to over 2650 cryptocurrencies for swift, registration-free swaps, all at the most competitive rates available in the market. 

Through the [SwapSpace DEX](https://swapspace.co), individuals have the capability to engage in trading and withdrawals involving Zcash using various options including Zcash mainnet address, Zcash (Bep20), Zcash (Bep20), and Zcash on the Heco Chain.

DEX Link : https://swapspace.co


**#14 ChangeHero** 
ChangeHero combines a UX flow of decentralized exchange with liquidity from multiple popular CEXs after successful DEX integration as announced by the team [here](https://changehero.io/blog/dex-integration-in-changehero/) 

Change Hero also supports trading and swapping of Zcash into other available tokens on the DEX. The DEX also supports Zcash mainnet (t-address) address on it's platform. 

DEX Link: https://changehero.io/


**#15 EasyBit** 
EasyBit is also a non Custodial Exchange that enables users to swap and trade digital assets easily on it's DEX.  It operates without a central authority or intermediary, allowing users to trade directly from their wallets and retaining control over their private keys.

Users can also trade Zcash with EasyBit as the DEX also supports Zcash mainnet network, Zcash (Bep20) and Zcash (BEP2) 

DEX Link: https://easybit.com/en/

### **Conclusion** 

Non-custodial exchanges, or DEXs, are decentralized platforms enabling direct cryptocurrency trading from users' wallets. Users retain control of their private keys, enhancing security and privacy. These exchanges offer features like shielded transactions for confidentiality and operate on trustless principles through smart contracts. They play a key role in the DeFi ecosystem, though they might face challenges like liquidity concerns. Non-custodial exchanges offer a decentralized, secure, and private way to trade cryptocurrencies globally.




Non-custodial exchanges offer an alternative trading experience that aligns with the principles of cryptocurrencies. While they bring advantages in terms of security, privacy, and control, users should assess their risk tolerance and familiarity with the technology before engaging in trading on these platforms.

---
## [TimUkrainian/zechub](https://github.com/TimUkrainian/zechub)@[9e448711f9...](https://github.com/TimUkrainian/zechub/commit/9e448711f9676343eb138487a4be9d80d30de65a)
#### Tuesday 2023-09-05 06:42:55 by Hardaeborla

zecweekly57.md

#Iwe Iroyin Osẹ-ọsẹ Zec #57

Àwọn ifunni Zcash Kékeré Ṣí fún Àwọn olubẹwẹ, Àwọn imudojuiwọn Agbègbè àti Rántí Wípé “Aṣiri jẹ Deede”

 Atunto nipasẹ "Tony Akins"[(@Tonyakins01)](https://twitter.com/TonyAkins01) 
ati Itumọ si ede Yoruba nipasẹ "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

### EKaabo si ZecWeekly

Ọsẹ moriwu mìíràn fún Zcash bí àgbègbè ṣé gbá atilẹyin ńlá àti àwọn ìgbì ìdàgbàsókè túntún, ZecHub pínpín nkan Ìwé ìròhìn kàn, àwọn imudojuiwọn Ìdàgbàsókè Arborist àti àgbègbè ṣe ìdáhùn sí ikọlu lórí òmìnira ọrọ tí àwọn olupilẹṣẹ.
---

## Nkan Ẹkọ ti Ọsẹ yii
Pipinpin awọn iyatọ laarin awọn adagun-omi Idabobo Imọ Zero ati ailorukọ-orisun ti o da lori ni afikun aipẹ si wiki ZecHub. Iṣafihan si Awọn adagun-omi Dabobo, Awọn ẹri Imọye Zero, Awọn Ibuwọlu Iwọn & Awọn iṣowo Asiri. Awọn afiwera lẹhinna fa ni fifun ni ero ti o daju lẹhin idi ti Zcash n pese awọn iṣeduro aṣiri lori-pq aifẹ.
[Ka ni ibi yìí](https://wiki.zechub.xyz/zk-shielded-pools-vs-decoy-based-privacy) 




## Awọn imudojuiwọn Zcash

####  Awọn imudojuiwọn ECC ati ZF
[Awọn ohun elo🗎 Ṣii fun Yika Keji ti Awọn ifunni Kekere ZF](https://forum.zcashcommunity.com/t/all-ecc-teams-focused-on-wallet-performance/42860/107) 

[Awọn ẹgbẹ ECC dojukọ iṣẹ ṣiṣe apamọwọ](https://forum.zcashcommunity.com/t/opening-applications-for-the-second-round-of-zf-minor-grants/45463) 

[Ẹgbẹ ZFAV ṣe atẹjade awọn itọsọna 📚 fun awọn olupilẹṣẹ àkóónú](https://wiki.zechub.xyz/zfav/guides) 

####  Awọn imudojuiwọn Awọn ifunni Agbegbe Zcash

[Imudojuiwọn Lórí Ilolupo Aboo](https://forum.zcashcommunity.com/t/zcash-ecosystem-security-lead/42090/91) 

[Igbero fun 🇧🇷  Aṣiri Alliance tí Ilu Brazil](https://forum.zcashcommunity.com/t/brazilian-privacy-alliance/45486) 

[Àgbègbè Igbowosile ZFAV ní Ipele](https://twitter.com/ZFAVClub/status/1693689895254949983) 

#### Awujo Ise Agbese 
[Awọn agbasọ nipa Asiri🗣️ - Topcrypto](https://free2z.cash/TopCrypto/zpage/dont-overshare-privacy-is-power-zcash) 

[Zcash Espanol ṣe iṣẹlẹ iṣẹlẹ atunṣe Zcon4](https://twitter.com/zcashesp/status/1694857330284712324) 

[Ìpè  🌳 Arborist Lakotan](https://twitter.com/zksquirrel/status/1694876187586170957) 

[Ọ̀rọ̀ @Zulakyz NFT lórí tí ZecHub Extras](https://zcashesp.com/zechub-nft-acceso-extra-a-beneficios-e-informacion-zcash/) 

[Itan kékeré láti ọ̀dọ̀ Cypherpunk Zero - Zerodartz🔥](https://free2z.com/zerodartz/zpage/cypherpunk-hacks-in-zed-city-short-story-3-out-of-12-chapters) 

[Awọn itumọ nilo fun Nighthawk apamọwọ](https://crowdin.com/project/Nighthawk-wallet) 


#### Iroyin ati Media 

[Ilosiwaju tí de ba Ethereum Staking💹  - Decrypt](https://decrypt.co/153813/ethereum-staking-is-booming-but-value-of-defi-assets-keeps-falling) 

[Kini idi ti asiri di ọrọ buburu? - Coindesk](https://www.coindesk.com/consensus-magazine/2023/08/25/when-did-privacy-become-a-bad-word) 

[Account tí OnlyFans tí Gba Friend.tech - Decrypt](https://decrypt.co/153723/onlyfans-accounts-take-over-friend-tech-crypt-app-adds-photo-feature) 

[Òṣìṣẹ́ banki aringbungbun sọrọ nipa Euro oni nọmba aladani ni ìlú 🇪🇸 Spanish - Cointelegraph](https://cointelegraph.com/news/spanish-central-bank-official-talks-about-private-payment-services-era-digital-euro) 

[Awọn anfani Lido n pọ si ti Ethereum - Trustnodes](https://www.trustnodes.com/2023/08/27/lido-closes-in-on-33-of-the-ethereum-network) 

[Awọn iran ti ọjọ iwaju lórí Decentralization - Cypherpunk](https://www.cypherpunktimes.com/visions-of-a-decentralised-future/) 

[Akojọpọ ọsẹ - Lori Brink](https://onthebrink-podcast.com/roundup-08-25-23/) 



## Awon oro die Nipa ZCash Lori Twitter
[👉 Iyatọ laarin Monero àti Zcash](https://twitter.com/MKjrstad/status/1695814999405379672) 

[Ikede nla nbọ laipẹ? - TrendsXBT](https://twitter.com/TrendsXBT/status/1694891818226213127) 

[Awọn iṣagbega nla ti a ṣe si Nighthawk](https://twitter.com/aiyadt/status/1694973730856866228) 

[Strawpoll ti o ni ipo 📊 ti Zcash Awọn ìṣáájú](https://twitter.com/nate_zec/status/1694405933638861048) 

[ZeroDAO ṣe igbega Zcash DeFi](https://twitter.com/zerodaoHQ/status/1694762728345456889) 

[Àṣírí sì jẹ déédéé](https://twitter.com/ZecHub/status/1694417573541007445) 

[O ṣeun lati ọdọ ZcashEsp!](https://twitter.com/zcashesp/status/1694861382154338648) 

[Fidio FROST ❄️  Ririnkiri lori Youtube](https://twitter.com/ZcashFoundation/status/1694410320859545939) 

[Awọn ifẹ ojo ibi Ailorukọ nipasẹ Zcash Memo](https://twitter.com/AyanlajaAdebola/status/1695721838943289694) 

[Bawo ni o ṣe n ṣe pẹlu ZEC?](https://twitter.com/ZcashForum/status/1693520113797116406) 

[Ṣe awọn spammers n ṣe rere fun nẹtiwọọki naa?](https://twitter.com/ZcashForum/status/1693430229044445287) 

[Awọn iwe afọwọkọ oluranlọwọ Zcasd lati Dismad :)] (https://twitter.com/ZcashForum/status/1693385561116164360) 

[A wa fun ominira - @zcash](https://twitter.com/zcash/status/1669397156212375583) 

[Iwe Iwe irohin ZecHub nipa Awọn adagun Àṣírí](https://twitter.com/ZecHub/status/1695082959911403585) 


[Joel Valenzuela pẹlu iwoye diẹ sii 📽️ lori Tornado Cash](https://twitter.com/TheDesertLynx/status/1694816146355036620) 




## Zeme ti Ose Yii 

[https://twitter.com/ZFAVClub/status/1694817298677113308](https://twitter.com/ZFAVClub/status/1694817298677113308) 


## Awọn iṣẹ ni ilolupo
[ZecWeekly #58  iwe iroyin Agbegbe](https://app.dework.xyz/zechub-2424/board?taskId=102e34d1-8f77-45d1-bd4f-d3d8f2a040ce) 

[Ṣiṣe Zcash Full Node lori Akash Network](https://app.dework.xyz/zechub-2424/board?taskId=543cab70-627d-4222-a712-9fb8768abe9c)

---
## [twilightwanderer/FluffySTG](https://github.com/twilightwanderer/FluffySTG)@[8ddcb6ba45...](https://github.com/twilightwanderer/FluffySTG/commit/8ddcb6ba45b3d6e3bb4c6045c04ccdd296422a18)
#### Tuesday 2023-09-05 06:45:49 by SkyratBot

Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

## About The Pull Request

This PR adds a new wizard ritual (the kind that require 100 threat on
dynamic)

This ritual allows the wizard to select one spellbook entry (item or
spell), to which everyone on the station will be given or taught said
spell or item. If the spell requires a robe, the spell becomes robeless,
and if the item requires wizard to use, it makes it usable. Mostly.

- Want an epic sword fight? Give everyone a high-frequency blade

- One mindswap not enough shenanigans for you? Give out mindswap

- Fourth of July? Fireball would be pretty hilarious...

The wizard ritual costs 3 points plus the cost of whatever entry you are
giving out. So giving everyone fireball is 5 points.

It can only be cast once by a wizard, because I didn't want to go
through the effort to allow multiple in existence

## Why It's Good For The Game

Someone gave me the idea and I thought it sounded pretty funny as an
alternative to Summon Magic

Maybe I make this a Grand Finale ritual instead / in tandem? That's also
an idea.

## Changelog

:cl: Melbert
add: Wizards have a new Right and Wrong: Mass Teaching, allowing them to
grant everyone on the station one spell or relic of their choice!
/:cl:

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Mitali-Warang/SQL](https://github.com/Mitali-Warang/SQL)@[9491fe54e4...](https://github.com/Mitali-Warang/SQL/commit/9491fe54e4cc9d23f7fba92c85cd91a660cfac1e)
#### Tuesday 2023-09-05 07:00:51 by Mitali-Warang

Add files via upload

I'm thrilled to share my latest SQL project with you all!
I recently dove into the world of Olympic data, utilizing a dataset downloaded from Kaggle, and wrote a series of queries to uncover some fascinating insights. This project was a true journey of exploration, utilizing a plethora of SQL functions to extract valuable insights.

Here's a sneak peek at the questions I tackled:
1. How Many Olympics Games Have Been Held?
Leveraging SELECT, COUNT, and AS to determine the total number of Olympic Games held.
2. List Down All Olympics Games Held So Far?
Using SELECT and ORDER BY to compile a comprehensive list of Olympic Games.
3. How Many Athletes Won Gold Medals?
Employing SELECT, COUNT, and WHERE conditions to identify Gold Medal winners.
4. Which Teams Participated in the 1992 Summer Games?
Harnessing SELECT and WHERE conditions to extract the participating teams.
5. Top 3 Cities in Terms of Total Number of Medals?
Combining SELECT, GROUP BY, COUNT, LIMIT and ORDER BY to unveil the top medal-winning cities.
6. Average Age of Female & Male Athletes Who Won Medals?
Calculating the average age using SELECT, GROUP BY, and AVG.
7. Top 5 Sports in Which Female Athletes Have Won the Most Medals?
Utilizing SELECT, GROUP BY, COUNT, ORDER BY, and LIMIT to identify the top sports for female athletes.
8. Mention the Total Number of Nations Who Participated in Each Olympic Game?
Employing SELECT, WITH,COUNT, GROUP BY, and JOIN to reveal the participating nations for each Olympic Game.
9. Show How Many Males and Females Participated from All Countries?
Utilizing SELECT, COUNT, GROUP BY, JOIN to distinguish between male and female participants.


This project was not only a fantastic learning experience but also a deep dive into the rich history of the Olympics. This project has been a captivating blend of data analysis and SQL.

---
## [balena-os/poky](https://github.com/balena-os/poky)@[89394ac832...](https://github.com/balena-os/poky/commit/89394ac832e1a3f584271e3c855168c78b75e471)
#### Tuesday 2023-09-05 07:10:40 by Richard Purdie

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[30976c33ee...](https://github.com/treckstar/yolo-octo-hipster/commit/30976c33ee319952e4ce163eb039bbb4d2e51561)
#### Tuesday 2023-09-05 07:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [crisbeto/angular](https://github.com/crisbeto/angular)@[acd59ad037...](https://github.com/crisbeto/angular/commit/acd59ad0371a19838813cfc934a73fa3cc357602)
#### Tuesday 2023-09-05 07:54:30 by Ward Bell

docs: Migrate Observables guides & code examples to standalone (#51516)

None of the guide pages mentions ngModules. Only `observables-in-angular` needed conversion to Standalone.

However, some of the guide pages reflect old versions of RxJS, including signatures that are no longer valid. These have been corrected.

More significantly, *the existing guide is pretty bad at explaining RxJS and its usage*. It was written (by me I think) in the very early days of Angular and Angular RxJS instruction. I've taught numerous "RxJS in Angular" classes since and learned from that experience what does and does not work with students.

There was neither the time nor the charter to completely overhaul this guide. But this commit attempts to remove what flops with students and to bring the teaching closer to what seems more effectively. I hope reviewers agree that my revisions are an improvement.

**Revised Overview**

The overview doc, `observables.md`, had a few errors (ex: `next` is NOT REQUIRED) and deprecated patterns (you now must pass the Observer object to `subscribe`).

More importantly, it was wildly overcomplicated and scary, especially when it got into multi-casting.

Moved the multi-casting section to  "RxJS Library" and rewrote it (with working example) for simplicity and context.

I made other changes in an effort to make this an overview that is  more comprehensive and more clear. I paid particular attention to the "Basic usage and terms" section.

Finally, I relocated the "Naming conventions for observables" section here from `rx-library`. This is the section that describes the dollar-sign convention. It made more sense for it to be here.

**Revised "RxJS Library" page and code**

*RxJS no longer supports chaining* and hasn't for a very long time. Removed note in `rx-library.md` that suggested you could use operator chaining.

The RxJS `pipe` discussion in the "Operators" section was just weird. Almost no one calls the `pipe` function. We certainly should *start* there. We should start with how people actually use operators - by adding them to the argument list of the `Observable.pipe()` method.

I kept the original `pipe` function example but subordinated it in a "callout". Most readers will (and should) ignore it.

`Subject` is a *critically important RxJS mechanism for creating custom observables*. It was completely missing from the list of observable creators on this guide page. So I added it to the "Observable creation functions" section of the guide and wrote an accompanying `MessageService` code sample (see the new `rx-library/app/` folder).

The `MessageService` is a pretty common pattern in Angular apps - far more common than creating an observable from a counter or an event, two of the creation patterns currently on this page.

This new section also afforded an opportunity to show how RxJS helps with building loosely coupled applications. We will soon be talking about Signals. Many will wonder whether and when they should still use RxJS.

At least a partial answer is that RxJS is really good at progressively combining and enhancing streams of data as they cross component boundaries. Of course you can pass signals around; but they are not as rich in transformers as RxJS. This is where RxJS shines.

**Revised "Comparing observables"**

The Promises section in `comparing-observables.md` had many errors and misleading remarks.

The comparison of error handling was especially egregious; the code example for that was nonsense.

The "Chain" sub-section was really about transforming values. It also failed to demonstrate chaining promise `.then`s.

Reworked these sub-sections and improved the code samples to match.

PR Close #51516

---
## [ohiscot/The-Great-Planet-Project](https://github.com/ohiscot/The-Great-Planet-Project)@[c95911c4a6...](https://github.com/ohiscot/The-Great-Planet-Project/commit/c95911c4a65c32a8577a5568d4cc701767345c6b)
#### Tuesday 2023-09-05 08:04:07 by ScottMitchell[Private] 1993-1994 BOBCATS :469A|Artificial Intelligence Applications

Add files via upload

HEx#F4A14A - Delphia(R) Investments has -25USDT PULL~!ing from 45,000USDT - illegally.
This was the I,M,F,-Kenyan-Branch-ostensibly-to-maneuver/cause/to-cause/OR-to-"Otherwise"-DECREE-"Settlement-and-Resignation" a CONTRACT-BUYBACK-Attached/Affixed/In-RI-VERIFICATION-Aspiration(R)Mutual_Fund-WOULD-DO-AS-HE-STATES-OR-AND-XOR-BUT-Butter-But-GONNA'FEEL-M-I-Do-Re-Mi-MyBROTHERS-In-Turkey-A-Place-Jupyter.9WHOA)-My-Five-O!-butter-gonna-be-funniest-sucker-hmmpf-to-your-Gal-Pal-Woof-Alot-AKA-Barack-Butter-Sauce-piece-Of-THe-Touopee-Approachin'-yo!~

By the Guiudelines"(r) Butter-45,000USD$ Losses- to-Marina-del-Rey? Pitchess-Barack-Butter-AKA-0BHOII-Oh-I-Told-You-IF-THE-THEN-POLITICAL-Tuopee-Be-ASCERTAINING-My-emotion_y'sall-gonna-see-m-i-shaking-Heavily-OhPlease-Please-MissBeGotten-Dems-In-A-FREEFALLIN'-cask-oh-05'O.-Yo..:.

---
## [camunda/zeebe](https://github.com/camunda/zeebe)@[d659ab4f30...](https://github.com/camunda/zeebe/commit/d659ab4f306f39893e6feaaf6f2edc06fe5dde17)
#### Tuesday 2023-09-05 08:58:41 by Nico Korthout

ci(.dependabot): stretch the open pr limits

Some dependencies are not being updated, because we have too many
pull requests by Dependabot open. We'll need to make sure to close/merge
pull requests earlier, but we should also avoid that we miss out on
dependency upgrades.

This stretches the limits as follows:
- maven: 5 -> 25
- go: 5 -> 10
- gha: 5 -> 10

These are still just magic numbers, chosen at my personal whim. However,
I feel that they better reflect our project. What numbers are optimal is
hard to say. My thoughts are as follows:
- we have many maven dependencies, we should allow many open maven pull
  requests
- we have fewer go and gha dependencies, we don't need as many open pull
  requests for these dependencies

There is no way to disable the limit AFAIK.
Any limit is a magically chosen number.
These numbers feel good to me.

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[bae1aef3b4...](https://github.com/Jackraxxus/tgstation/commit/bae1aef3b457cb4fbad551a8560319ed993ba397)
#### Tuesday 2023-09-05 09:36:23 by san7890

Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

## About The Pull Request

I literally can't focus on anything nowadays, so I just did this to
break a never-ending chain of distress. Anyways, regal rats! These
fellas are mostly player controlled, but did have _some_ AI capabilities
(mainly tied to their actions), so that was incorporated too. Everything
should work as-expected (as well as look a shitload cleaner).

Instead of doing weird and awful conditional signals being sent out, I
made the `COMSIG_REGAL_RAT_INTERACT` (not the actual name) have a return
value so we can always rely on that working whenever we have that signal
registered on something we attack. I also cleaned up pretty much every
proc related to regal rats, gave them AIs to reflect their kingly nature
(and action capabilities (as well as move the action to
`mob_cooldown`)).

Since I thought they needed it, Regal Rats now get a special moniker!
This is stuff like "the Big Cheese" and what-not, like actual regents in
history. That's nice.
## Why It's Good For The Game

Two more off the list. Much better code to read. Way smarter rats with
spawning their army as part of a retaliatory assault (war). More sovl
with better regal rat names. The list goes on.
## Changelog
:cl:
refactor: Regal Rats have been refactored into basic mobs. They should
be a bit smarter and retain their docility (until attacked, in which
case you should prepare to get rekt by summoned rats), and properly flee
when they can instead of just sit there as you beat them to death. The
framework for them interacting with stuff (i.e. opening doors while
slobbering on food) is a bit more unified too, now. They also have
cooler names too!
/:cl:

FYI: Beyond a few code touchups, I haven't touched the actions at all. I
do not believe myself to be enthusiastic about fixing anything involving
the actions code as of this moment so that this PR is more overbloated
unless it's unbelievably stupid or easy to fix.

---
## [RengaN02/PsychonautStation](https://github.com/RengaN02/PsychonautStation)@[820c22a5f5...](https://github.com/RengaN02/PsychonautStation/commit/820c22a5f5381364c595d21b6c047e269f7f0497)
#### Tuesday 2023-09-05 09:46:01 by DaydreamIQ

Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

---
## [RengaN02/PsychonautStation](https://github.com/RengaN02/PsychonautStation)@[63f7eb1a6a...](https://github.com/RengaN02/PsychonautStation/commit/63f7eb1a6a01c0c48dcc075f57b58a662d27fc17)
#### Tuesday 2023-09-05 09:46:01 by san7890

Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#77632)

Closes #77631

## About The Pull Request

Hey there,

Ticked File Enforcement simply wasn't catching files that were missed.
That's a bit stupid, so I decided to look into what the issue might be,
and whoopsie daisies I did double periods back in #76592
(020ac2405308eab83f314282499dfe777aba5874).

![image](https://github.com/tgstation/tgstation/assets/34697715/6023afe8-313d-4550-9a60-58a8bc211b4f)

I also added some debug info and some more checks to prevent such a
break from happening again on runtime of this script. I thought it was a
weird string concatenation issue (and not the simple break I thought it
was), so I rewrote how it adds `glob`s. I think it's cleaner so I'll
keep it anyhow

This PR also corrects the oversight of the missing unit test (introduced
in #77218 (69827604c46952dd4393db8617cd494ade17bea2)) by reticking it in
the `_unit_tests.dm` file, and also makes it compile because it didn't
do that.

I also then had to do some more work to get the unit test to work.
* Genericizes the Create-and-Destroy "ignore" list to be a static list
on `/datum/unit_test` to allow it to be shared between these types of
tests that we need to test.
* Adds that list to C&D and the broken unit test regarding fantasy
bonuses
* Fixes some actually broken that the unit test was made to catch (beam
rifles, butterdogs and other slippery items, random ingredient boxes).
* Adds cases for things that the unit test and overall framework really
shouldn't be altering anyways (mythril), and was likely causing
inappropriate stack traces on master

## Why It's Good For The Game

Unit Tests WORK. Tools WORK.


![image](https://github.com/tgstation/tgstation/assets/34697715/9a59c0db-7a33-4546-918b-c73372a5b867)


## Changelog

:cl:
fix: Beam rifles will no longer inappropriately retain any bonuses they
may gain from wizardry.
fix: Inappropriate stack traces over bonuses being applied to components
that gain bonuses innately (like Mythril stacks) should cease.
/:cl:

---
## [cooljeanius/git](https://github.com/cooljeanius/git)@[8f23432b38...](https://github.com/cooljeanius/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Tuesday 2023-09-05 10:06:40 by Johannes Schindelin

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
## [warptools/rustwarp](https://github.com/warptools/rustwarp)@[9cdb05e6f9...](https://github.com/warptools/rustwarp/commit/9cdb05e6f9d3609271b53680361271e637165508)
#### Tuesday 2023-09-05 10:34:09 by Eric Myhre

wishful thinking on rustfmt configuration...

... but most of the options I want aren't present, or are in nightly

 The max_width is especially insanely global.  What I really want
is "leave my fucking line breaks alone, thank you", but that...
 doesn't seem to exist.  *sigh*

---
## [warptools/rustwarp](https://github.com/warptools/rustwarp)@[49117b0804...](https://github.com/warptools/rustwarp/commit/49117b0804dfcf8adc4d1f57b2209318c5c07cfe)
#### Tuesday 2023-09-05 12:02:46 by Eric Myhre

okay, rustfmt, this is a CRIMINALLY idiotic diff, and I'm really honestly angry.

- it makes the longest lines LONGER

- it's reflowing entire function call positions across lines -- that
  is NOT an acceptable behavior from a formatter.  That's *way* too
  much failure to preserve original user intent.

- and it just so happens to be hiding error handling and major
  flowcontrol by shoving it to the end of a long line.
  This is where I cross the line into calling it outright criminal:
  hidding my `map_err(...)?` from me is absolute
  Fuck OFF fuck OFF fuck ENTIRELY off. Fuck no.

And yet I have not found the knob to disable this; and I've tried --
see earlier commits today.

So I give up for now.

But I'm making this commit to document my extreme discontent.

...

I'm almost willing to change completely over to huge match statements
using explicit return on error arm and implicit return out of the match
on the okay arm.  That's a large amount of boilerplate, but at least
it leaves it very clear that there's an exit branching happening.
Which is otherwise, apparently, impossible to do within rustfmt's
absolutely bonkersly strong opinions.

---
## [retrohun/mame](https://github.com/retrohun/mame)@[e97630981c...](https://github.com/retrohun/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Tuesday 2023-09-05 12:08:37 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [madisongh/openembedded-core](https://github.com/madisongh/openembedded-core)@[387b276c2d...](https://github.com/madisongh/openembedded-core/commit/387b276c2d56d58c2a25d59984fcaaf9c88ac788)
#### Tuesday 2023-09-05 12:59:02 by Richard Purdie

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
## [Advithi-23/E-Commerce-website](https://github.com/Advithi-23/E-Commerce-website)@[55540afe5d...](https://github.com/Advithi-23/E-Commerce-website/commit/55540afe5dd4d542b648053f62093211f63381a6)
#### Tuesday 2023-09-05 14:07:02 by Advithi-23

Update README.md

# Ganesh Designmatics - Dynamic Website

Welcome! This repository contains the source code for our dynamic website, which was developed to showcase the graphic design company's portfolio and enhance client interaction. This README file will provide you with an overview of the website, its features, and how to set it up locally.

## Table of Contents
- [About Ganesh Designmatics](#about-ganesh-designmatics)
- [Features](#features)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## About Ganesh Designmatics

Ganesh Designmatics is a graphic design company that specializes in creating stunning visual solutions for businesses and individuals. We are committed to delivering top-notch designs that resonate with our clients' brand identities and goals. To showcase our work, we have developed a dynamic website that features a modern, user-friendly interface and utilizes the latest web technologies.

## Features

Our dynamic website offers a range of features to provide an engaging and informative experience for our visitors:

1. **Modern User Interface**: The website boasts a sleek and contemporary design, ensuring a visually appealing experience for users.

2. **Responsive Design**: We have implemented a responsive design to ensure that the website looks and works seamlessly across various devices and screen sizes.

3. **Dynamic Image Galleries**: Our portfolio section includes dynamic image galleries that allow us to showcase our design projects effectively. Users can browse through our work with ease.

4. **Improved Client Interaction**: We have integrated contact forms and interactive elements to encourage client inquiries and feedback. This facilitates better communication with potential clients.



## Getting Started

To run this website locally, follow these steps:

1. **Clone the Repository**: 
   ```
https://github.com/Advithi-23/E-Commerce-website.git
   ```

2. **Navigate to the Project Folder**:
   ```
   cd E-Commerce-website
   ```

3. **Open the Website**:
   - Open the `index.html` file in your preferred web browser to view the website locally.

4. **Explore the Code**: Feel free to explore the HTML, CSS to understand how the website was built.

## Contributing

We welcome contributions from the GitHub community to improve and enhance Ganesh Designmatics. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Create a pull request to merge your changes into the main repository.

Please ensure that your contributions align with our goals and maintain the website's user-friendly and modern design.

## License

This project is licensed under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the code as long as you provide appropriate attribution and include the same license in your distribution.

Thank you for visiting! We hope you enjoy exploring our website, and we look forward to your contributions and feedback.

---
## [sholderbach/nushell](https://github.com/sholderbach/nushell)@[ad49c17eba...](https://github.com/sholderbach/nushell/commit/ad49c17ebacd04585fb4355e079ec87d7fc63d8d)
#### Tuesday 2023-09-05 14:17:41 by Kiryl Mialeshka

fix(nu-parser): do not update plugin.nu file on nu startup (#10007)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description

I've been investigating the [issue
mentioned](https://github.com/nushell/nushell/pull/9976#issuecomment-1673290467)
in my prev pr and I've found that plugin.nu file that is used to cache
plugins signatures gets overwritten on every nushell startup and that
may actually mess up with the file content if 2 or more instances of
nushell will run simultaneously.

To reproduce:
1. register at least 2 plugins in your local nushell
2. remember how many entries you have in plugin.nu with `open
$nu.plugin-path | find nu_plugin`
3. run 
    - either `cargo test` inside nushell repo
- or run smth like this `1..100 | par-each {|it| $"(random integer
1..100)ms" | into duration | sleep $in; nu -c "$nu.plugin-path"}` to
simulate parallel access. This approach is not so reliable to reproduce
as running test but still a good point that it may effect users actually
4. validate that your `plugin.nu` file was stripped

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# Solution

In this pr I've refactored the code of handling the `register` command
to minimize code duplications and make sure that overwrite of
`plugin.nu` file is happen only when user calls the command and not on
nu startup

Another option would be to use temp `plugin.nu` when running tests, but
as the issue actually can affect users I've decided to prevent
unnecessary writing at all. Although having isolated `plugin.nu` still
worth of doing

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->
It changes the behaviour actually as the call `register <plugin>
<signature>` now doesn't updates `plugin.nu` and just reads signatures
to the memory. But as I understand that kind of call with explicit
signature is meant to use only by nushell itself in the `plugin.nu` file
only. I've asked about it in
[discord](https://discordapp.com/channels/601130461678272522/615962413203718156/1140013448915325018)

<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect -A clippy::result_large_err` to check that
you're using the standard code style
- `cargo test --workspace` to check that all tests pass
- `cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

Actually, I think the way plugins are stored might be reworked to
prevent or mitigate possible issues further:
- problem with writing to file may still arise if we try to register in
parallel as several instances will write to the same file so the lock
for the file might be required
- using additional parameters to command like `register` to implement
some internal logic could be misleading to the users
- `register` call actually affects global state of nushell that sounds a
little bit inconsistent with immutability and isolation of other parts
of the nu. See issues
[1](https://github.com/nushell/nushell/issues/8581),
[2](https://github.com/nushell/nushell/issues/8960)

---
## [kirillzyusko/react-native-keyboard-controller](https://github.com/kirillzyusko/react-native-keyboard-controller)@[01dbb7f225...](https://github.com/kirillzyusko/react-native-keyboard-controller/commit/01dbb7f225c34a2822004477d4973230230bf20a)
#### Tuesday 2023-09-05 15:36:22 by Kirill Zyusko

fix: react-native-navigation integration (#149)

## 📜 Description

Fixed an integration with `react-native-navigation` without hacks.

## 💡 Motivation and Context

To overcome the initial problem I've decided to re-create callback
between `onAttachedToWindow`/`onDetachFromWindow` lifecycles. It
improves the situation, but at some point of time you still may
inconsistent values returned by hook and actual keyboard position.

For me it seems like if the `WindowInsetsAnimationCompat.Callback` is
attached to any parent view of the current screen (i. e. `decorView`,
`rootView`, etc.), then it can be broken after some navigation cycles.

This solution was inspired by
https://github.com/Omelyan/RNNKeyboardController-Test/commit/d5ee7eaf90e0ef90fcf9ed6d71dd1f44803e5e62.
If we send events through overlay, then it's never broken. I had a look
on a view hierarchy and realised, that overlays are not attached to
parent views or to navigation tree:

<img width="672" alt="image"
src="https://github.com/kirillzyusko/react-native-keyboard-controller/assets/22820318/629002ec-7b41-479e-83b0-6122e75c5827">

I got an inspiration from this idea and decided to replicate this
mechanism in native code. I've decided to attach a view as a child to
`@id/action_bar_root` and setup callback on this view. In this case this
view will not be a parent of navigation tree and will not be inside of
navigation tree:

<img width="675" alt="image"
src="https://github.com/kirillzyusko/react-native-keyboard-controller/assets/22820318/18fc5714-6260-4b8f-b66a-7cee7ff3bc29">

However such approach didn't work out - it seems like if current view
has `onAttachedToWindow`/`onDetachedFromWindow` calls, then Keyboard
insets detection in the end will be broken on API < 30.

I've tried to remove this `eventView` in `onDetachedFromWindow` and
re-create it again in `onAttachedToWindow` - and such combination worked
out.

Fixes
https://github.com/kirillzyusko/react-native-keyboard-controller/issues/130

## 📢 Changelog

### Android
- setup callbacks in `onAttachedToWindow`;
- add `eventView` as a child of `@id/action_bar_root` view (in
`onAttachedToWindow`);
- attach a callback to `eventView` rather than
`EdgeToEdgeReactViewGroup` (but still send events through
`EdgeToEdgeReactViewGroup` id)
- added `removeSelf` to `ViewGroup` extensions;
- remove `eventView` in `onDetachedFromWindow`;
- change `inputMode` only if new mode is not equal to current one;

### Docs
- update `README.md`;

## 🤔 How Has This Been Tested?

Tested on Pixel 6 Pro (API 28), emulator.

## 📸 Screenshots (if appropriate):


https://github.com/kirillzyusko/react-native-keyboard-controller/assets/22820318/923fe0b6-cdb3-4bca-92e2-44a2c7fe678d

## 📝 Checklist

- [x] CI successfully passed

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[0055338d73...](https://github.com/TaleStation/TaleStation/commit/0055338d73af8b638f4f33b37ed7b06906ca4de5)
#### Tuesday 2023-09-05 16:32:24 by TaleStationBot

[MIRROR] [MDB IGNORE] Makes fanny packs be silent, others can't see what you put in or take out. (#7580)

Original PR: https://github.com/tgstation/tgstation/pull/78010
-----

## About The Pull Request
Just like the syndicate toolbox and a handful of other items.
## Why It's Good For The Game
This is a blatantly stealth antag buff.

Pockets are 2 silent storage slots everyone has, so it is not adding
anything that antags didn't have access already.
But going from 2 to 5 small items can help a lot, also belts are a lot
smoother to use with their shortcut keys.

Love stealth antags, hate murderboners, gonna help my stealth boys not
be valid hunted because someone checked their chat logs from 10 minutes
ago and read that X player put Y contraband in their bag.

Or people that have some contraband names highlighted on chat... but no
one does that right.... right?
## Changelog
:cl:Guillaume Prata
balance: Fanny packs are now silent, no one will get a chat message
about what you put in or take out.
/:cl:

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Aki Ito <11748095+ExcessiveUseOfCobblestone@users.noreply.github.com>

---
## [isc-projects/bind9](https://github.com/isc-projects/bind9)@[84d71c8e2c...](https://github.com/isc-projects/bind9/commit/84d71c8e2c3d3e4c2aa93b32da19fa550dd58821)
#### Tuesday 2023-09-05 16:47:22 by Artem Boldariev

TLS DNS: take into account partial writes by SSL_write_ex()

This commit changes TLS DNS so that partial writes by the
SSL_write_ex() function are taken into account properly. Now, before
doing encryption, we are flushing the buffers for outgoing encrypted
data.

The problem is fairly complicated and originates from the fact that it
is somewhat hard to understand by reading the documentation if and
when partial writes are supported/enabled or not, and one can get a
false impression that they are not supported or enabled by
default (https://www.openssl.org/docs/man3.1/man3/SSL_write_ex.html). I
have added a lengthy comment about that into the code because it will
be more useful there. The documentation on this topic is vague and
hard to follow.

The main point is that when SSL_write_ex() fails with
SSL_ERROR_WANT_WRITE, the OpenSSL code tells us that we need to flush
the outgoing buffers and then call SSL_write_ex() again with exactly
the same arguments in order to continue as partial write could have
happened on the previous call to SSL_write_ex() (that is not hard to
verify by calling BIO_pending(sock->tls.app_rbio) before and after the
call to SSL_write_ex() and comparing the returned values). This aspect
was not taken into account in the code.

Now, one can wonder how that could have led to the behaviour that we
saw in the #4255 bug report. In particular, how could we lose one
message and duplicate one twice? That is where things get interesting.

One needs to keep two things in mind (that is important):

Firstly, the possibility that two (or more) subsequent SSL_write_ex()
calls will be done with exactly the same arguments is very high (the
code does not guarantee that in any way, but in practice, that happens
a lot).

Secondly, the dnsperf (the software that helped us to trigger the bug)
bombed the test server with messages that contained exactly the same
data. The only difference in the responses is message IDs, which can
be found closer to the start of a message.

So, that is what was going on in the older version of the code:

1. During one of the isc_nm_send() calls, the SSL_write_ex() call
fails with SSL_ERROR_WANT_WRITE. Partial writing has happened, though,
and we wrote a part of the message with the message
ID (e.g. 2014). Nevertheless, we have rescheduled the complete send
operation asynchronously by a call to tlsdns_send_enqueue().

2. While the asynchronous request has not been completed, we try to
send the message (e.g. with ID 2015). The next isc_nm_send() or
re-queued send happens with a call to SSL_write_ex() with EXACTLY the
same arguments as in the case of the previous call. That is, we are
acting as if we want to complete the previously failed SSL_write_ex()
attempt (according to the OpenSSL documentation:
https://www.openssl.org/docs/man3.1/man3/SSL_write_ex.html, the
"Warnings" section). This way, we already have a start of the message
containing the previous ID (2014 in our case) but complete the write
request with the rest of the data given in the current write
attempt. However, as responses differ only in message ID, we end up
sending a valid (properly structured) DNS message but with the ID of
the previous one. This way, we send a message with ID from the
previous isc_nm_send() attempt. The message with the ID from the send
request from this attempt will never be sent, as the code thinks that
it is sending it now (that is how we send the message with ID 2014
instead of 2015, as in our example, thus making the message with ID
2015 never to be sent).

3. At some point later, the asynchronous send request (the rescheduled
on the first step) completes without an error, sending a second
message with the same ID (2014).

It took exhausting SSL write buffers (so that a data encryption
attempt cannot be completed in one operation) via long DoT streams in
order to exhibit the behaviour described above. The exhaustion
happened because we have not been trying to flush the buffers often
enough (especially in the case of multiple subsequent writes).

In my opinion, the origin of the problem can be described as follows:

It happened due to making wrong guesses caused by poorly written
documentation.

---
## [greearb/linux-6.5-be200](https://github.com/greearb/linux-6.5-be200)@[8b9c1cc041...](https://github.com/greearb/linux-6.5-be200/commit/8b9c1cc0418a43196477083e7082568e7a4c9418)
#### Tuesday 2023-09-05 17:07:36 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [cnleth/tgstation](https://github.com/cnleth/tgstation)@[a5aef3b823...](https://github.com/cnleth/tgstation/commit/a5aef3b823dd3b8b5bfe40d68bbc0f89b403f79a)
#### Tuesday 2023-09-05 17:35:09 by MrMelbert

Replaces Ascended Blade Heretic stun imminuty with a stun absorption effect (it's not as cool as it sounds)  (#78060)

## About The Pull Request

Instead of being completely immune to stuns after ascension, blade
heretics now have a stun absorption. This is the effect that His Grace
and the Bastard Sword use.

It functions similarly, in that it stops you from being hardstunned, but
the difference it is they are only immune to a limited amount of stuns
for a limited amount of time before it recharges.

Currently that number is 45 seconds of stuns, with a 2 minute recharge,
meaning if you take more than 45 seconds of stun effects you will stop
being immune.

Bear in mind this still provides full immunity to being stamcrit*, as
stam doesn't contribute towards "seconds stunned" number.

*Unless you used all 45 seconds of stun immunity then you will no longer
be immune until you recharge.

Also to compensate, I gave them a slightly modifier protecting against
knockdowns.

## Why It's Good For The Game

I forgot Stun Absorptions were a thing entirely when making this even
though I refactored the darn things.

Anyways, the reason why I'm doing this is that Stun Absorptions are just
a slightly more fair, less overt way of providing stun immunity, and I
think it fits the theme more.

You're supposed to be a master duelist, but being able to take on a
dozen people at once is not entirely intended (even though this is the
ascension, I know). Stun Absorptions lend better to that, since you run
out of stun juice eventually before you have to pull back.

Though ultimately this doesn't change very much, as we use very few
hardstuns now-a-days:

- A flashbang will contribute about 10 seconds of stun time
- A flash is similar to a flashbang
- Bodythrows and tackles are less than 5 seconds
- Beepsky, 10 seconds
- Stamcrit, 0 seconds, but you are still slowed by stamina damage
- A banana peel, default is roughly 6 seconds. <-- (This is why I gave
them a knockdown modifier)

However it does mean you can't really tank an AI stun turret all day.
That's Rust's thing. Go play Rust Heretic.

## Changelog

:cl: Melbert
balance: Ascended Blade Heretics no longer have blanket stun immunity,
they now have 45 seconds of stun absorption that recharges after 2
minutes - think His Grace. This doesn't affect stamcrit (still immune to
that) (assuming you haven't consumed all of your immunity charge) but
does affect hard CC such as slips, flashbangs, or beepsky.
balance: Ascended Blade Heretics now have a 0.75 modifier to incoming
knockdowns.
/:cl:

---
## [SHIBAMMOHANTY/CODSOFT](https://github.com/SHIBAMMOHANTY/CODSOFT)@[81bfd30918...](https://github.com/SHIBAMMOHANTY/CODSOFT/commit/81bfd309183f3c6761327a2f0e03fe22270eed69)
#### Tuesday 2023-09-05 17:44:34 by Shibam Mohanty

Update README.md

Repository Name: Codsoft

Description:
Welcome to the Codsoft repository! This is a dedicated space where I showcase my coding projects, experiments, and the code that powers them. As a passionate web developer, I've poured my creativity and technical expertise into these projects, and I'm excited to share them with you.

What You'll Find Here:

Web Development Projects: Explore a collection of web applications, websites, and interactive demos, each designed to showcase my skills in HTML, CSS, JavaScript, and more.

Code Samples: Dive into the codebase of various projects to gain insights into my coding style and problem-solving techniques. Feel free to use these code snippets as learning resources or inspiration for your own projects.

Open-Source Contributions: I believe in the power of open source. You'll find contributions to various open-source projects, demonstrating my commitment to collaborating with the developer community.

Experimental Work: Sometimes, I like to experiment with new technologies and techniques. Discover my experiments, prototypes, and creative coding projects here.

Why Explore This Repository:

Learn from Real-World Projects: Explore practical examples of web development in action, from responsive design to interactive features.

Code Quality: I take pride in writing clean, well-documented code. Use this repository to see how I structure my projects and maintain code quality.

Collaboration Opportunities: If you find something interesting or want to collaborate on a project, feel free to reach out! I'm always open to connecting with fellow developers.

Get in Touch:

Have questions, feedback, or project ideas? Don't hesitate to contact me. Let's collaborate and create something amazing together!


LINKDIN-https://www.linkedin.com/in/shibammohanty/

---
## [henrif75/comprehensive-rust](https://github.com/henrif75/comprehensive-rust)@[c6af2a0d37...](https://github.com/henrif75/comprehensive-rust/commit/c6af2a0d3732ce8860c65ba7d1ebb23e58947619)
#### Tuesday 2023-09-05 17:50:53 by Martin Geisler

Mention how long each course day is (#1155)

Most classes run with 2.5 hours for the morning session and 2.5 hours
for the afternoon session.

I have tried running the course as 2 × 2.5 hours and 2 × 3 hours. My
experience was that people ended up getting really worn out after
spending 6 hours in total on Rust (7 hours including a lunch break).
However, the experience varies from group to group, so this is just a
recommendation.

---
## [pulumi/pulumi](https://github.com/pulumi/pulumi)@[3d9ddb2981...](https://github.com/pulumi/pulumi/commit/3d9ddb2981016dbdfa7ff4293b2eb814e9d11ce1)
#### Tuesday 2023-09-05 18:42:25 by Fraser Waters

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
## [axodotdev/cargo-dist](https://github.com/axodotdev/cargo-dist)@[83a61cbdee...](https://github.com/axodotdev/cargo-dist/commit/83a61cbdee2aa5abb22d750b05e9a324da642154)
#### Tuesday 2023-09-05 18:43:33 by Aria Beingessner

feat(msi): add msi installer

The "msi" installer vendors the binaries into a windows msi.
msi generation is implemented by using cargo-wix as a library,
which in turn handles generating templates and invoking WiX (v3).

The resulting msi's are unsigned -- signing will be handled by a followup,
as changes to OV certs mean that "proper" signing is now very complicated
and messy.

This implementation has some notable details:

main.wxs generation
--------------------

WiX requires an xml-based template called main.wxs for each msi it generates.
This template includes things like the application name, version, publisher,
EULA, embedded files, and so on.

cargo-wix's default workflow is for you to run `cargo wix init` once to generate
that file and check it in. At this point the developer is free to hand-edit
the template to suit their needs. We like this idea, `cargo dist generate-ci`
is based on that same premise!

But our experience with generate-ci has also taught us that this approach
is really prone to frustrating desyncs. The main.wxs bakes in several pieces
of information that were sourced from your Cargo.toml. As a result, if you
ever change your Cargo.toml, you now need to remember to apply the same
change to your main.wxs, or rerun `cargo wix init` and potentially clobber
any hand-edits you made.

As such, for the first draft of this feature we've opted for a more aggressive
solution: whenever you run `cargo dist init` we will invoke `cargo wix init`
to force the template to have up to date contents, essentially forbidding
hand-edits.

When you run `cargo dist build` or `cargo dist plan`
we will also error out if we detect that `cargo wix init` would modify
main.wxs.

A new `allow-dirty = ["msi"]` can be added to your cargo-dist config to
prevent `init` from regenerating main.wxs or checking that it's up to date,
essentially restoring the original design of cargo-wix. We believe this
should be opt-in because most people ideally shouldn't want to do hand-edits,
and desyncing is a very nasty footgun.

GUID persistence
----------------

`cargo dist init` will also modify your Cargo.tomls to add
`[package.metadata.wix]` with two generated GUIDs (if those GUIDs aren't
already present).

These GUIDs are used by windows to identify that two different msis actually
intend to refer to the same application and install dir. As such, each release
of your app needs to use the same GUID.

cargo-wix bakes these GUIDs into your main.wxs, and critically it defaults to
generating new random ones every time you run init (because constantly
re-initing wasn't part of the design).

By persisting the GUIDs to your package's Cargo.toml, we unlock the ability
to freely regenerate main.wxs whenever we want.

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[b22529fc74...](https://github.com/shiptest-ss13/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Tuesday 2023-09-05 18:46:50 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[d5655c3c55...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/d5655c3c55fab0f4450659947fad1a40043893dc)
#### Tuesday 2023-09-05 19:16:23 by SkyratBot

[MIRROR] Adds Summon Simians & Buffs/QoLs Mutate [MDB IGNORE] (#22970)

* Adds Summon Simians & Buffs/QoLs Mutate (#77196)

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

Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

* Adds Summon Simians & Buffs/QoLs Mutate

* Updates our modular file to take this into account (I hate that this exists)

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[3782e4b710...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/3782e4b71098d12588696d9263f2ee8748caf9bf)
#### Tuesday 2023-09-05 19:16:23 by Bloop

[MISSED MIRROR] Martian Food: A Taste of the Red Planet (#75988) (#23013)

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

Co-authored-by: EOBGames <58124831+EOBGames@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Arceveti/HackerSM64](https://github.com/Arceveti/HackerSM64)@[ef38abb1c0...](https://github.com/Arceveti/HackerSM64/commit/ef38abb1c0c2b39536e2a1a04003bc10556f5cb1)
#### Tuesday 2023-09-05 19:58:02 by Fazana

Frustratio funny fix 2 (#593)

* Update game_init.c

* fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo

---
## [fabiangreffrath/freedoom](https://github.com/fabiangreffrath/freedoom)@[3efe8a0e41...](https://github.com/fabiangreffrath/freedoom/commit/3efe8a0e4114414d764d4a1f03400a9a0f2094dd)
#### Tuesday 2023-09-05 20:17:53 by mc776

levels: fix various bugs. (#871)

* levels: fix various bugs.

Thanks to Goji!, Inuk and rednakhla on Discord for pointing these out.


E1M3: Northern lift simplified to address texture alignment problems.

E1M5: Door near (-205,1336) (leading out into open ceiling area with the big strip of lights down the middle) door tracks needed to be lower unpegged.

E1M9: Lift near (-2328,120) was split into 2 sectors, causing HOMs when they went out of sync. There's nothing that relies on this split (contrast the neat lighting stuff from Map22) so the lift is just merged into one sector.

E2M2: Shellbox near (-486,192) is right on the line between two stairs, causing it to rest on the bottom step which causes ports like GZDoom to have the sprite clip *very* visibly into the upper stair. Moved it slightly so it rests on the upper of those two stairs.

E2M3: Door leading to red key and "door" leading to soulsphere: former should be lower unpegged but latter should not, but were reversed. Two exit-door-textured doorframes also given more conventional DOORTRAK and lower unpegged treatment. The teleporter representing the hatch going down into the nukage is now fully repeatable.


Map07: Infinite height in vanilla would cause the spectres in the red key courtyard to trap the player on the entrance ledge from below in a way that could not be seen or diegetically explained. Those three spectres now warp in only after you cross the ledge. (Setting them to "ambush" would do nothing since you're in LOS with them from the top of the ledge.)

Map11: Lights above red keycard weren't aligned; moved that entire sector and added a few lines to round the corner. Removed a strobe effect on the exit teleporter to compensate for a GZDoom issue where the light would go to absolute zero during the blink.

Map12: Room to the south with the 2 stimpacks, ammo boxes, 2 chaingunners and berserk would sometimes cause some of the items to be "levitated" to the highest sectors they touch. Moved them away from said higher sectors - it looks a bit sloppier but this is a backroom not a storefront lol.

Map13: The easternmost archvile platform had the archvile stuck in the seam, preventing it from lowering in vanilla. (Worked fine in GZDoom) Moved it a little further in.

Map19: The combat slugs teleport in from a W1 teleporter which could sometimes be spent while one of the pinkies is blocking the destination, permanently preventing that slug from teleporting in. These are now WRs like the other teleporting enemies.

Map22: More W1 monster teleports that should be WR. Also filled in some missing textures in the multi-sector lift connecting the cavern to the hall in the southwest, which parts are clearly not meant to be seen moving separately but can - it still looks fucked up if you manage to desync them, but it's a diegetic fucked up now.

Map24: Another W1 spawn. This one is impossible to screw up in vanilla, but there are some mods that could end up spawning something there that could block the archviles from teleporting.

Map25: More W1 problems. The spawn source room now also has a small barrier to make sure each pinkie only goes to its own teleporter unless the initial teleport fails.

Map27: Lizardbaby dropping too far meant that the bracket was falling along with it in a visibly unnatural way.

Map29: Broke up all the long linedefs on the perimeter of the map to get around the invisible hitscan barrier bug: https://doomwiki.org/wiki/Hitscan_attacks_hit_invisible_barriers_in_large_open_areas
(Ideally this entire perimeter should be redone to break up the box in favour of more natural-looking formations, but that's a bit outside the scope of a fix like this.)


Also got rid of the Plutonia-style start/end teleports on the fixed Phase 2 maps, to address #867.

* maps: more fixes.

More floaty items and other things.

E1M9
- floater mid south stim by staircase
E1M7
- floater northwest clips near the tunnels
- floaters near switch by railings, now all on the railings
- duckproofed sector 439 barrier
E2M9
- floater thing #125 medikit on top of lift, now in middle of platform
- shotgun guy (thing #309) and the spectre behind it stuck in geometry.
- lines 430 and 761 both open the same door and are in the same room right next to each other. Since 761 is actually textured and positioned as a switch, the tag and special on 430 is removed.

* levels: flag e2m7 DM stuff as multi-only.

Marked the following based on eyeballing out what items are right next to DM spawns with no obvious alternate route to them: 487, 488; 203, 397; 499, 500, 501, 502; 482, 485; 491, 492, 493; 494; 496; 28, 486; 182; 54

* levels: more misc. fixes.

E1M6 W1 lines 2318 and 2321.

E3M5 Removed all monster block lines in that gross blood room and raised the blood floor to only 4 below the normal floors, but flagged more monsters in there as ambush to make up for it. Also fixed a lot of texture alignment issues in the top skin panels and lowered the ceiling, along with adding a new sector to address texture tiling issues in the northern teleporter room.

E4M1 fixed a mysterious HOM that was going on near the northern shadow line in the northern outdoor area. Merged a lot of sectors that were identical in their properties.

E4M7 entrance to sector 985 seems to be intended that the player run off the ledge into that room, then the pinkie near the ledge ambushes the player from behind. Instead, what sometimes happens is that the pinkie is alerted somehow, then obstructs the player (vanilla infinite height) from being able to get down there. That means of getting down into that room is now walled off, and instead you step onto that lift to bring it down from above. Neat side effect: any monsters still in the ring when you enter that room will follow you down there.

E4M5 linedefs 1724 and 1725 were facing the wrong way and couldn't be hit with projectiles.

Map25 Float thing 217. Moved that entire row further south to address floating item issues.

Map28 Float thing 464.

* levels: use inner room texture in E4M7 lift.

* levels: align side textures on that lift.

Didn't realize the little squares were sticking into the floor at the *bottom* of the lift as well.

---
## [mach-kernel/n-tac-toe](https://github.com/mach-kernel/n-tac-toe)@[e36fa26680...](https://github.com/mach-kernel/n-tac-toe/commit/e36fa266802be348ea197227b4fa194991126adf)
#### Tuesday 2023-09-05 20:32:29 by David Stancu

holy shit re-frame is amazing, ::play and ::cpu-play

---
## [remove32/fulpstation](https://github.com/remove32/fulpstation)@[c449fbb56c...](https://github.com/remove32/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Tuesday 2023-09-05 20:48:17 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [Das15/tgstation](https://github.com/Das15/tgstation)@[d93dfbc35c...](https://github.com/Das15/tgstation/commit/d93dfbc35c4b86435f9b436160e0d6c0670a8e28)
#### Tuesday 2023-09-05 21:44:21 by Sealed101

Adds Summon Cheese (#77778)

oh apparently this is my 100th PR on tg, which is weird because github
reports 99 total, and i made at least one to the old voidcrew repo, and
filtering tg prs by my name still shows 99. weird. here's to 100 more i
guess?

<sub>could have been better if it was a get, jhonflupwliiard watch ur
back 🔫 </sub>

## About The Pull Request

Adds a new spell granter book to the Wizard's Den - Summon Cheese, which
grants the spell by the same name, which summons 9 heads of cheese.
That's about it, I think.

## Why It's Good For The Game

Wizards are a hungry bunch, so why can't they just summon food? They can
even share, if they'd like, since the notion of a friendly wizard still
exists

<details>
<summary>... </summary>

alright fine
i'm slightly malding over not getting the 77777 get so no more
roleplaying in the pr body

Wizard Grand Ritual now has a hidden goal of sacrificing 50 cheese
wheels. Sacrificing a cheese wheel is done with invoking the grand rune,
and each invocation/pulse of the rune will whisk away more cheese until
all cheese on the rune is taken by whichever entity lurks in the other
realm. The sacrifice will be hinted at in an _ancient parchment_ which
will be on the bookshelf (when i add it lmao) alongside the spell book.

Meeting this cheese goal will lock the wizard's grand finale rune and
grand finale effect to special ones. The cheese rune is mostly identical
to the normal grand rune, barring the custom sprites/animations.
The cheese finale consists of the wizard getting permanent Levitation
(nogravity + free space movement), a 0.5 modifier(reducing incoming
damage in half) to every damage type, a comically strong mood buff and
**The Wabbajack**(separate sprite pending) - a juiced up chaos staff
which can fire a lot more projectiles than a normal one can (it will get
more, I may even make a few just for it).
Everybody else (including any invader antags) gets hallucinations, 175
brain damage and a comically strong mood debuff, as well as a vendetta
against the wizard. If the victim was already suffering from
hallucinations from a trauma (including the quirk), they are instead
healed.

if you didn't catch the obvious reference, this entire shtick is a
tribute to Sheogorath. the rune makes use of daedric script, and most of
the catchphrases are a direct quotation of the Daedric Prince of
Madness, so if any of those things can get us in trouble somehow, let me
know. i will be sad but i will comply.

This shtick is intended as an easter egg, really, so I wasn't really
planning on expanding the wizard grand finale into heretic paths thing
or whatever.

Oh, and finale grand runes now allow the wizard to select the effect
even if it's time-gated. If it is, you just won't be able to invoke it
until the time comes. The rune will tell you how much time is left until
you can invoke it. And grand finale runes with a finale effect selected
also glow in the color of their effect. I also think I fixed some step
of the grand rune animation not triggering but I'm not sure.

<details><summary>Some rune animations (some are subject to
change)</summary>


![rune_cheese_activate](https://github.com/tgstation/tgstation/assets/75863639/62ae184d-b6fc-4883-a169-4d8ca7636b40)


![rune_cheese_flash_2](https://github.com/tgstation/tgstation/assets/75863639/619545c8-3c55-4264-bfa4-d40067ef7406)


</details> 

## Why It's Great For The Game

it's funny

</details> 

## Changelog


:cl: Sealed101, EBAT_BASUHA for spritework
add: Wizard's Den now has a book of Summon Cheese in the Studies Room
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Das15/tgstation](https://github.com/Das15/tgstation)@[fb4587b336...](https://github.com/Das15/tgstation/commit/fb4587b3368ebb55e0cc10f8c650abcc26afa5d4)
#### Tuesday 2023-09-05 21:44:21 by san7890

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[51c82f3222...](https://github.com/tgstation/tgstation/commit/51c82f32223179f7263dd8d4de11eb62f23ef8fd)
#### Tuesday 2023-09-05 22:46:54 by RICK IM RI

Adds Blood-drunk and demonic frost miner boss music. (#78123)

Acts as a continuation of PR #77149 for boss music functionality and
implements a BDM and demonic frost miner boss music theme.

More music is good, but I do have some gripes with my own PR. This
particular track relies on instrumentation that when compressed just
doesn't sound as good, and the in-game version is noticeably less
enjoyable that the high quality version. I wish I could help the track
out more, but as is it's already at 811 kb which is barely in line with
file requirements, so i just can't justify bloating the audio file sizes
to make it sound better. You notice this kind of problem a lot with the
higher runtime music and background tracks. It just feels a bit more
clunky than hierophant, but what are you gonna do right?

---
## [ElijahB09/ASCII-Pokemon-Game](https://github.com/ElijahB09/ASCII-Pokemon-Game)@[3371c782c6...](https://github.com/ElijahB09/ASCII-Pokemon-Game/commit/3371c782c655460dab5076b6f9c241f98a3f6647)
#### Tuesday 2023-09-05 23:15:34 by Elijah Brady

Honestly im going a little insane with what im doing right now. Essentially trying to build my own dijkstras cause I got annoyed looking at tutorials online

---
## [bartcubbins/kernel](https://github.com/bartcubbins/kernel)@[373ef51f3e...](https://github.com/bartcubbins/kernel/commit/373ef51f3e8ac62ee12aeb53f0ca81ec50160b0b)
#### Tuesday 2023-09-05 23:22:37 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

commit c570449094844527577c5c914140222cb1893e3f upstream.

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[bfca7608f6...](https://github.com/mc776/freedoom/commit/bfca7608f642220f69a03da4d535b3a484dff27c)
#### Tuesday 2023-09-05 23:28:38 by mc776

dehacked: adjust obituaries.

First, let's just make all the DM ones consistent in naming the victim first, so it's easier to quickly skim in the middle of a match.

I've also fixed the comment now that these are compatible with not just ZDoom.

There's a couple things that are inherited from ZDoom that don't even make sense, or are clearly derived from the Doom monsters - I don't think anything in FD calls the painlords "bruisers".

The "smitten" never sat well with me because the primary usage I see is like "she's so smitten with him, just look at all the little hearts she drew on his yearbook photo" and not like smite as in lightning.

Monsters with (ostensibly) player-equivalent weapons are given equivalent obituaries. (I love how deadpan the zombieman "killed" is and I think it works for PvP too.)

Slashed didn't even make sense for the id imp.

Both worms deserve to eat.

I'm sorry but we *have* to make that trilo-bite pun.

I've taken the liberty to move "perforate" to the shotgun to reflect how it tends to make a very visibly straight line of hits compared to the other bullet weapons. (Technically pistol and minigun do this too but it's harder to see as they're not all at the same time and the puff moves upwards.)

Yeah, I changed the railgun. Was anyone ever actually comfortable with that innuendo?

P.E.W. was a forced meme anyway. :(

---

