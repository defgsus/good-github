## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-20](docs/good-messages/2022/2022-02-20.md)


1,541,745 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,541,745 were push events containing 2,259,377 commit messages that amount to 131,982,214 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2209c36036...](https://github.com/tgstation/tgstation/commit/2209c36036c5c0c303443fd4a6304da9384e5107)
#### Sunday 2022-02-20 00:02:18 by san7890

Fixes Weird Area Definition on DeltaStation (#64986)

So, there I was. Pondering the blobbosity of Auxiliary Base Construction. Deciphering and unclothing the issue in my mind in order to better comphrehend it. I was there for a few moments, until this ugly beast of a fucking area definition caught my eye:

Hideous. Repugnant. I was relishing the thought of dissecting Auxiliary Base Construction into fifteen million more areas (it _will_ lessen obtusities) when that scraggletooth of an utterly mortifying error forced me into a visceral rage: the likes of which have never been experienced on this planet Earth.

---
## [DerErizzle/The-Jackbox-Party-Pack-8-German](https://github.com/DerErizzle/The-Jackbox-Party-Pack-8-German)@[49bdfb6bd9...](https://github.com/DerErizzle/The-Jackbox-Party-Pack-8-German/commit/49bdfb6bd96cea0a8e76c1fab0cc47eec69aa87a)
#### Sunday 2022-02-20 00:06:29 by Maxi

8 Fragen

Bezüglich der VfB-Frage: Leider ist der Begriff VfB allein nicht sehr aussagekräftig, da es VfB's wie Sand am Meer gibt. Verstehe aber die Frustration. Ja, ich wollte die Fragen mal im Spiel sehen. Faszinierendes Gefühl XD.
1. Welches sind echte Krawattenknoten? (ID 83447).
2. Welche dieser Athleten haben fünf oder mehr olympische Goldmedaillen gewonnen? Ich habe ein paar deutsche Namen hinzugefügt, auch wenn die vermutlich auch keine Sau kennt (ID 83080).
3. Welches sind echte Arten von Quallen? Bah, ekelhafte Viecher (ID 82907).
4. Welche dieser Personen, Gruppen oder Gegenstände wurden Stand 2021 vom US-amerikanischen Time Magazine zur "Person of the Year" ausgezeichnet? Sie ist jetzt nicht mehr familienfreundlich, da ich entdeckt habe, dass Hitler und Stalin auf dieser Liste sind XD (ID 82899).
5. Welche dieser Speisen wurden in der ersten Klasse der Titanic serviert, nur Stunden bevor sie am 14. April 1912 sank? Ich hatte echt Probleme, diese Speisen zu übersetzen (ID 82891).
6. Welche dieser Tiere sind Beuteltiere? Endlich mal niedliche Tiere (ID 82742).
7. Wobei handelt es sich um Positionen im Fußball? (ID 82716).
8. Welches sind Teile eines Kreises? Schon wieder so ein übelster Dad-Joke. Kreisverwaltung lol (ID 82689).

---
## [dominicm00/dotfiles](https://github.com/dominicm00/dotfiles)@[85b64eefe4...](https://github.com/dominicm00/dotfiles/commit/85b64eefe452860ecb707d8f74b300803bfb6abd)
#### Sunday 2022-02-20 00:40:36 by Dominic Martinez

attempt at nvidia proprietary drivers

Currently fails because Guix provides no way to completely replace a
package unless you add a replacement field to the original package
definition, meaning we can't graft the nvidia drivers onto all the
system packages

At this point I'm done. This is absurd. It's fun having a reproducible
home environment but the system configuration is insane and has taken
up far too much of my time. Guix actively limits facilities that are
percieved as being used for proprietary software. I simply cannot
handle a system that literally jumps to 80% CPU usage when dragging a
terminal around because of software rendering.

Maybe I'll go back to Nix. Maybe I'll use Guix on Fedora so I can
still use Guix home. I don't even know if I should keep my Emacs
config; I mean it's basically just watered down Doom Emacs.

I've put so many uncountable hours into this frankly it's
unhealthy. No one should spend this much time configuring their
system. I'm gonna go try and get a life.

---
## [autonomical1/ObsidianBackup](https://github.com/autonomical1/ObsidianBackup)@[b01609249c...](https://github.com/autonomical1/ObsidianBackup/commit/b01609249cd79d3548a9a2b30daacfc7573317c0)
#### Sunday 2022-02-20 00:41:09 by Neel Mittal

fuck you i fucking hate you u degenerate imbecile

FUCKfUCKFUCKFUCKFUCKFYCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKCuFKcFICKFUCKUFCFUckFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUCKFUKFUFUCKFUCKFUCKFUCKFU

---
## [lockboxauth/oauth2](https://github.com/lockboxauth/oauth2)@[fbe6d29906...](https://github.com/lockboxauth/oauth2/commit/fbe6d2990611d160f9984f87f391129fd0a85972)
#### Sunday 2022-02-20 00:42:03 by Paddy Carver

Finish testing grant creation from email, fix bugs.

Add test cases checking that scopes are handled correctly when creating
grants using emails, and fix the bug exposed by them, namely that we
weren't validating that users had access to the scopes they were
requesting; we only checked clients. This involved updating the scopes
module, but also involved refactoring our granters and grantCreators to
be able to surface the profile ID a grant is for, which was annoying.

In theory, in the future, it may be desirable to filter scopes based on
the account ID (e.g., you can request admin scopes using your work
email, but they won't be handed out if you request them with your
personal email, or you can request admin scopes using your email but if
you're logging in with WebAuthn, you don't get admin scopes, or
whatever) but the big issue here is that refresh tokens aren't currently
tracking the account that created them, only the grant. So to get to the
account that started the chain, you need to unwrap the token into the
grant that created it, which has that information. Unfortunately, when
creating the Grant that gets exchanged for the refresh token, we're not
populating the account ID on the grant because we don't have easy access
to it. That's probably not good, and we should address that.

🎵 Now Playing: Impossible Year
🎵 Artist: Panic! at the Disco
🎵 Album: Death of a Bachelor

---
## [bluedogz162/lambdas-weapon-pack](https://github.com/bluedogz162/lambdas-weapon-pack)@[1eca065e81...](https://github.com/bluedogz162/lambdas-weapon-pack/commit/1eca065e813fb15b64fd53b7a5a4b534bf75e28e)
#### Sunday 2022-02-20 00:45:11 by MarcusKubis9

Added some Engineer hats

Added some Engineer hats because fuck you.wav

---
## [seanm/GDCM](https://github.com/seanm/GDCM)@[ff550ec21a...](https://github.com/seanm/GDCM/commit/ff550ec21a0a57f307c0743b240e335504a21eb4)
#### Sunday 2022-02-20 00:54:45 by Blair Conrad

Comment out MITRA MARKUP 1.0 references

There is no real sense in keeping those fake private attributes around.
Original discussion copy/pasted here:

I did see those in privatedicts.xml and did a quick scan in my source to
see if I had information at hand to augment. I didn't.
Since you asked, I looked a little more deeply this morning and learned
a bit more, but it's not great news.

I found some DICOM conformance statements that match the data currently
in privatedicts.xml, with no additional information.

I also found one other internal document that suggested a different use
(well, maybe consistent up to xx11 but not for xx12, xx13, and xx14;
then again maybe x12 and onward were errors in the first conformance
statements I mentioned). The document describes a long-defunct product.
But here's what I get from it.

Each element from xx00 to xxFF describes a piece of markup. The values
consist of different components. In each case, the first component is an
indicator of the type of markup (e.g. caliper, freeform caption, angle,
…) and there are 15 subsequent components which will vary depending on
the type of markup. As far as I can tell, each component is a string,
although some will be essentially an enumeration, some are integer
strings, some are double strings, and so on.

We could in theory replace xx12, xx13, and xx14's value multiplicity
with 1-n, and extend up to xxFF, but I'm not incredibly comfortable with
it, and I'm not sure there's great value, unless you're aware of people
having problems with these tags. I'm leery of changing the dictionary to
be both new and erroneous. 😁

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[3a9eacf198...](https://github.com/Buildstarted/linksfordevs/commit/3a9eacf1985a54ad4d2a7f74e2364b5cf2417d9c)
#### Sunday 2022-02-20 01:06:34 by Ben Dornis

Updating: 2/20/2022 1:00:00 AM

 1. Added: Toy Traceroute With Ping - Susam's Maze
    (https://susam.net/maze/toy-traceroute-with-ping.html)
 2. Added: How I got Crostini to work in Chrome OS Flex
    (https://jlelse.blog/dev/crostini-fix)
 3. Added: Some (crazy?) thoughts on the future
    (https://billwadge.com/2022/02/19/some-thoughts-on-the-future-2/)
 4. Added: Web Guitar
    (https://wybiral.github.io/guitar/)
 5. Added: Software development is like tetris
    (https://www.adibsaad.com/2022/02/19/software-development-tetris)
 6. Added: .NET Frontend Day 2022: Xamarin & MAUI Recap
    (https://blog.taranissoftware.com/net-frontend-day-2022-xamarin-and-maui-recap)
 7. Added: Off-The-Record Messaging part 1: the problem with PGP | Robert Heaton
    (https://robertheaton.com/otr1)
 8. Added: User-Centered Design is Killing Innovation
    (https://philbeaudoin.com/2022/02/10/user-centered-design-is-killing-innovation/)
 9. Added: Dirty Nix flake quality-of-life hacks
    (https://siraben.dev/2022/02/13/nix-flake-hacks.html)
10. Added: Is Datalog a good language for authorization?
    (https://neilmadden.blog/2022/02/19/is-datalog-a-good-language-for-authorization/#more-3717?utm_source=hnblogs.substack.com)
11. Added: Simplify Rails Views Using ViewComponents with Tailwind CSS and RSpec
    (https://stefcoetzee.com/2022/02/18/rails-viewcomponent-rspec-tailwind)

Generation took: 00:06:23.9321997
 Maintenance update - cleaning up homepage and feed

---
## [nicwaller/spellie](https://github.com/nicwaller/spellie)@[ff6838b794...](https://github.com/nicwaller/spellie/commit/ff6838b794dc8693091ada961db142fcb1fa4cc4)
#### Sunday 2022-02-20 02:11:08 by Nic Waller

final removals

CLITS
COCKET
COCKS
COCKSY
COCKUP
CUNTS
FUCKUP
SHITES
SHITTY

---
## [newstools/2022-sahara-reporters](https://github.com/newstools/2022-sahara-reporters)@[0dc43911db...](https://github.com/newstools/2022-sahara-reporters/commit/0dc43911db2c64b1f8c3a0a0e7b2e62435b226af)
#### Sunday 2022-02-20 02:51:35 by Billy Einkamerer

Created Text For URL [saharareporters.com/2022/02/19/any-member-my-church-who-goes-big-brother-will-die-controversial-preacher-mummy-go-says]

---
## [nstrike2/alchemy-docs](https://github.com/nstrike2/alchemy-docs)@[081957d0c3...](https://github.com/nstrike2/alchemy-docs/commit/081957d0c337ccb49577091ea447faa7d1c190be)
#### Sunday 2022-02-20 03:51:56 by Neetish Sharma

Changing NFT tutorial to be compatible with new Solidity 0.8.0 compiler version

So here's the issue — with the new solidity compiler version 0.8.0 and all the minor changes after that (e.g. https://blog.soliditylang.org/2022/02/16/solidity-0.8.12-release-announcement/), OpenZeppelin's npm package from the Alchemy tutorial (`@openzeppelin/contracts@3.1.0-solc-0.7`) was out of date. So, what do we want to do?

We want to download the new npm package using `npm install @openzeppelin/contracts` instead. This will update all of our pragma headers from `pragma solidity ^0.7.0;` (out of date) to `pragma solidity ^0.8.0;`, where the compiler versions are up-to-date!!

All is good, right? No! Take a look at the code below:

```java
//Contract based on https://docs.openzeppelin.com/contracts/3.x/erc721
// SPDX-License-Identifier: MIT
pragma solidity ^0.7.3;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract MyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() public ERC721("MyNFT", "NFT") {}

    function mintNFT(address recipient, string memory tokenURI)
        public onlyOwner
        returns (uint256)
    {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}
```

Notice how the `_setTokenURI` function is called to set the URI in the new NFT, which updates the mapping _tokenURIs allowing to retrieve its content through function tokenURI(uint256 tokenId). However, OpenZeppelin decided to deprecate this function in their new 0.8.0-updated library (wtf?) in the name of flexibility for developers to define their own functions. This meant that developers had to implement the `mapping (uint256 => string) private _tokenURIs;` _tokenURIs mapping themselves :man_facepalming: 

However, OpenZeppelin finally came to their senses and updated their library to include the _setTokenURI function, except instead of being in the `"@openzeppelin/contracts/token/ERC721/ERC721.sol"` filepath, it's now sitting in an extension in an extension resource designated by `"@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol"`. What this means is that is we should now change our `import ` to `import `. Then, you also want to change your `contract MyNFT is ERC721, Ownable` to `contract MyNFT is ERC721URIStorage, Ownable` to specify the new object you're inheriting from.

In addition, you want to switch your solidity version under `module.exports` in `hardhat.config.js` from `solidity: "0.7.3",` to `solidity: "0.8.1",`. The reason it's 0.8.1 and not 0.8.0 is because the file "@openzeppelin/contracts/utils/Address.sol" uses `pragma solidity ^0.8.1`; instead of `pragma solidity ^0.8.0;`. I have no clue why, when everything else in their library uses 0.8.0 — must be a bug or inconsistency. (I ran into this compiler error myself — it will first download the 0.8.1 compiler, then compile your code successfully).

Side note, you can remove the `public` keyword from `constructor() public ERC721("peppermintTestNFT", "PMINT") {}`. Constructors are run only once — when the contract is initially deployed. They can't be called at a later time, so aren't "visible" in the sense that variables or functions are. Thus, you don't need to specify the function as public since it can't be called again.

All in all, your new smart contract code should look like this:

```java
//Contract based on https://docs.openzeppelin.com/contracts/3.x/erc721
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract MyNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() public ERC721("MyNFT", "NFT") {}

    function mintNFT(address recipient, string memory tokenURI)
        public onlyOwner
        returns (uint256)
    {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}
```

Your new `hardhat.config.js` should look like this:

```javascript
/**
* @type import('hardhat/config').HardhatUserConfig
*/
require('dotenv').config();
require("@nomiclabs/hardhat-ethers");
const { API_URL, PRIVATE_KEY } = process.env;
module.exports = {
   solidity: "0.8.1",
   defaultNetwork: "ropsten",
   networks: {
      hardhat: {},
      ropsten: {
         url: API_URL,
         accounts: [`0x${PRIVATE_KEY}`]
      }
   },
}
```

---
## [DirtyApexAlpha/cli-1](https://github.com/DirtyApexAlpha/cli-1)@[e6a99d2798...](https://github.com/DirtyApexAlpha/cli-1/commit/e6a99d27987e76795e24889753d7552b6bd9a611)
#### Sunday 2022-02-20 04:51:18 by thinkbubble.cloud@thinkbubble.com

create stackhawk-analysis.yml

directly leadership under towing bottomless consumption...eat your heart out since you all have so much in you and not enough of  your words can express truly where you all think speaking gonna answer your hard undertones of empowerment with children bullet proof vestments  without in. I got my prayers answered  with God said into me Your going to succeed at what you seek and he answers to my deceased angel Ty Kaleb Arteaga  claimed it "I just want my dad to be the best because he is" . love being a dad fathers is teaching repeat crazy so I always am better than you so have to ask to be blessed... closed mouth won't get fed a, en I always speak my mind with the mightest of the word  GOD save us ALL. I never knew Jesus trust just seems one way with a symbolic snake talking and a Virgin Mary God only said light  the rest is timeline transversal of a universal counter clock wise flowing unlike the others around it.

---
## [luciensadi/AwakeMUD](https://github.com/luciensadi/AwakeMUD)@[901318adbb...](https://github.com/luciensadi/AwakeMUD/commit/901318adbb9452a5ce464c720b4bf6239d5fa405)
#### Sunday 2022-02-20 05:04:37 by Lucien

PRONE-PAIN AND PRONE-PAIN-RELATED ACCESSORIES
- Added knockdown in combat, which forces you prone.
- Gel ammo probe string now tells you about knockdown.
- Made it so that prone mobs don't push buttons etc.
- Prone NPCs are now shown manning their weapons in room descs.
- You can now fire too-heavy weapons from prone; when you wield them, you'll be told to prone to use it.
- Added will check to rising from prone while wounded.
- Going prone now only costs half an init pass.
- Going prone with a tripod still costs a full init pass, and tells you you're deploying it.
- NPCs now stand up from prone if they don't gain benefits from it.
- Added a warning for being prone while using melee weapons / bare hands.
- Added warning for prone people with dodge dice.

OTHERS
- Probing heavy weapons now warns you about low str/bod and tells you they can damage you when fired.
- Fixed a bunch of messages to characters that didn't have trailing newlines.
- Reloading now costs two simple actions (aka one init pass).
- Added MOB_EMPLACED flag for turrets etc to prevent them trying to close the distance. These also have much higher ammo stores and no recoil penalties, simulating emplaced turrets etc.
- Fixed issues with ranged_response that were triggering mobs who couldn't actually hit you.
- Fixed issue where NPCs would rarely charge into rooms when being shot.
- Fixed bug where guards attacking vehicles printed odd messages.
- Fixed issue with wrong die output in unable-to-dodge rolls message.
- Fixed prone NPC logic.
- Added probe strings to weapon accessories.
- Invis NPCs you can see now show (invisible) in their room desc.

---
## [Tiktodz/android_kernel_asus_sdm660](https://github.com/Tiktodz/android_kernel_asus_sdm660)@[9cb695e0a1...](https://github.com/Tiktodz/android_kernel_asus_sdm660/commit/9cb695e0a1e130ad2f6d6b42169a0fe48a7dbc93)
#### Sunday 2022-02-20 05:13:27 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tiktodz <kuplemarkeple@gmail.com>

---
## [henshaw/bestmotherfucking.website](https://github.com/henshaw/bestmotherfucking.website)@[fe6c0dd67e...](https://github.com/henshaw/bestmotherfucking.website/commit/fe6c0dd67eab0aa550e0f2de0938e41b1ba5870f)
#### Sunday 2022-02-20 05:22:40 by Jon Henshaw

Updated index.html with lots of sweet goodness

Removed the title attributes from links because they are useless. Useless for SEO or any other purpose. And they aren't any good for accessibility either: https://www.a11yproject.com/posts/title-attributes/

Modified the dfn attribute, which should really be wrapped around the word. The way the sentence is structured, parsers and decent algos will be able to comprehend word and its definition as it's written.

Replaced all of the' with' because gross.

Removed header element. If you're not using the head or body element, then why the fuck use the header element. Totally useless.

Removed aside element, because it's really part of the article. It's not a true aside and is therefore not being used semantically as intended. If you wanted to use an aside element, it would be used to reference something else that's vaguely related to the article. But this is completely relevant to the article.

Almost every paragraph didn't have a closing p element. What kind of sick bastard leaves their paragraph wide open for anyone to tickle?! Fixed!

Added a bunch of abbr elements to the acronyms and abbreviations. Unlike title attributes on links, these are actually useful. They're helpful to readers who aren't familiar with an acronym or abbreviation and they disambiguate the meaning for search engines (that's a good thing). 

Added canonical link. Kind of helpful considering this is a public repos and anyone could post it anywhere. You want that hint to be there for search bots to consider this domain the end all, be all domain.

Added a better meta for UTF-8 content type

All this talk on the page about HTTPS and SEO but no meta description. For shame!

Added Open Graph data because you want to be social, don't you? DON'T YOU!? I made an Open Graph image for it. Feel free to change it to whatever you want, but it needs to exist and should be no smaller than 1200x630 px. It's on IPFS, just for the heck of it. Let's live in the future, but feel free to add it to the repose if you want.

Added Schema structured data in JSON format. That's the format Google prefers and you should disambiguate ALL THE THINGS and talk them bots in their own language.

Added periods to the headings that didn't have them. Consistency would make mother proud.

Added system fonts so the main system font for the OS would be used. If that's not elegant as fuck, I don't know what is. It's instantaneous and nothing is loaded because it already IS loaded. It's also consistent with the paragraph about using fonts on the page.

---
## [newstools/2022-information-nigeria](https://github.com/newstools/2022-information-nigeria)@[50afa9c49b...](https://github.com/newstools/2022-information-nigeria/commit/50afa9c49b287071bdf730116860fcfb841b9b36)
#### Sunday 2022-02-20 05:36:47 by Billy Einkamerer

Created Text For URL [www.informationng.com/2022/02/any-member-of-my-church-who-goes-for-big-brother-will-die-mummy-g-o.html]

---
## [projects-nexus/android_kernel_lavender-4.19](https://github.com/projects-nexus/android_kernel_lavender-4.19)@[2c54ecfdd4...](https://github.com/projects-nexus/android_kernel_lavender-4.19/commit/2c54ecfdd459f9d902be27362fd8a5df6cc65c30)
#### Sunday 2022-02-20 06:57:43 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: ImPrashantt <prashant33968@gmail.com>

---
## [2bnum1/guava](https://github.com/2bnum1/guava)@[e015172847...](https://github.com/2bnum1/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Sunday 2022-02-20 07:15:16 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [everettadw/MyMoney](https://github.com/everettadw/MyMoney)@[1b08101210...](https://github.com/everettadw/MyMoney/commit/1b08101210fb729e7cd08cb4799a84b7fa180a5f)
#### Sunday 2022-02-20 07:59:37 by Everett Daniels-Wright

Made significant changes to how form validation works, animated the error text, and tried for hours to combat Chrome's idiotic overwriting of autfilled input styles. *FACEPALM*

---
## [crdroidandroid/android_kernel_oneplus_sm8350](https://github.com/crdroidandroid/android_kernel_oneplus_sm8350)@[5b41637143...](https://github.com/crdroidandroid/android_kernel_oneplus_sm8350/commit/5b41637143d35bfff08fe97877a26e291f7a2cc6)
#### Sunday 2022-02-20 08:44:05 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [osamuaoki/qmk_firmware](https://github.com/osamuaoki/qmk_firmware)@[2d07f0bc4b...](https://github.com/osamuaoki/qmk_firmware/commit/2d07f0bc4b541fc04dbce1d6111036612ba9e686)
#### Sunday 2022-02-20 10:22:12 by Osamu Aoki

Format update and note

Note: Although these 2 lines should move to // Magic section, doinso may
cause trouble.  (My development time vague memory:  Back slash and back
space became swapped.  Since others had MAGIC_TOGGLE_CONTROL_CAPSLOCK
here, I assume this is the least invasive (but ugly patch.)

Signed-off-by: Osamu Aoki <osamu@debian.org>

---
## [YumeMichi/kernel_oneplus_sm8250](https://github.com/YumeMichi/kernel_oneplus_sm8250)@[0ef283cd45...](https://github.com/YumeMichi/kernel_oneplus_sm8250/commit/0ef283cd45fe73b9f9e5b7a01bb819c60a8f29c7)
#### Sunday 2022-02-20 10:30:35 by alk3pInjection

techpack: display: Handle dim for udfps

Apparently, los fod impl is better than udfps cuz it
has onShow/HideFodView hook, which allows us to toggle
dimlayer seamlessly.

Since udfps only partially supports the former one,
we'd better kill dim in kernel. This is kinda a hack
but it works well, bringing perfect fod experience
back to us.

Also implement a panel status check to ensure that
the dim layer dies when display is off.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I14d028a821e4a776bc62feb5836b3fe012bc808e

---
## [obsproject/cef](https://github.com/obsproject/cef)@[36fdac16a7...](https://github.com/obsproject/cef/commit/36fdac16a71140735ebc1b8c3dd6518c0215adce)
#### Sunday 2022-02-20 11:57:05 by Jim

Legendary 4638 shared texture perf improvement

This fixes remaining performance and frame pacing issues when using CEF
95 with texture sharing on Windows. I hacked Chromium internally to
treat shared textures similarly to how the 3770 method worked.

Let me document my little adventure.

First, we were getting system freezes, and from analysis of the
bluescreen dumps, they were always during synchronization, so I had a
hunch: "are keyed mutexes doing this?" The system freeze issue left me
hopeless. I already had a disdain for the stupid keyed mutexes, and due
to my immense hatred of them, I was angry and I just wanted to try
removing them, because 1.) What if they were the cause? (They were), and
2.) I hated them anyway. It was an irrational vendetta, and I was on a
war path to remove them just in the *slightest* chance that those god
forsaken keyed mutexes were the cause.

So I got angry and decided to remove them from almost everything in
Chromium just to see if it would fix the system freeze issue. I removed
their usage from almost everything in Chromium related to GLImageDXGI.

Let me go on a rant about keyed mutexes. I hate keyed mutexes. I *want*
synchronization between devices, but what I *don't* want is to be forced
to swap stupid "keys" between the two devices; especially if you're in a
situation where you cannot pass the next key value to the next device so
the next device knows what key to use, because then, the original device
can no longer lock the object anymore, and the object is completely
forfeit. Then you get suck in a situation where you're forced to wait
infinitely if you have no way of telling the other device to use the
correct key. I wish I could suggest a better design, but all I know is
that I hate it, it's an insufferable design as it is right now, and I
don't think there's a single human being on the planet who will ever
convince me otherwise. Absolutely insufferable design. I've always hated
them and always will.

Anyway, sorry about that. Like I was saying, I removed keyed mutex usage
from texture sharing inside chromium. But the problem is that with the
4638 version of shared textures, it was about 5 textures which were used
round-robin. Because we were forced to remove keyed mutexes (which were
crashing the entire system), we could no longer synchronize between
client and Chromium, thus frame pacing issues were introduced. Even
flushing wasn't helping. They weren't noticeable, and we were *almost*
just going to use it as it, but I decided I wasn't finished with my war
path.

I had fixed the system freeze issue by removing keyed mutexes, but now
there was this frame pacing issue. So, I was upset, and I tried many
different techniques to try to synchronize. Flushing, more textures,
less textures, trying to adjust timing; I thought it was hopeless, until
I started looking at the 3770 version and started looking around
4638 code for ways I could do the same thing. I had already removed
keyed mutex objects from GLImageDXGI objects, but then I realized: what
if I just add the same staging/CopyResource method 3770 did, and then
just use one shared texture? 3770 worked amazingly well, so why not try
it? Through much toil and experimentation, I got it working.

However, there was still one annoying caveat. Because of the fact that
Chromium now only deals with NT-style HANDLE objects for shared
textures, it would duplicate handles every time it was passed. There was
no way of detecting whether we were already using the same shared
texture (and CompareObjectHandles in KernelBase didn't work), so we had
to recreate the stupid texture object every time. So I introduced a new
OnAcceleratedPaint2 function specifically to specify whether the texture
has been changed -- that way we don't need to have to continually keep
recreating the god-forsaken texture object.

All these things combined has won us a huge victory, not only did we
solve the system freeze issue, but we also reduced the amount of
resources being used from the original version by removing the round
robin, eliminated frame pacing issues, and improved the perf back to
3770 levels. In fact, I'm pretty sure that perf levels are even better
than they were even with the keyed mutex version (if they weren't
causing stupid system freezes), because the keyed mutex version forced
INFINITE lock durations due to the inability to relay keys.

After 27.2 had this issue, I had to delay the release, and I spent a
week toiling over this. To get the system freeze issue fixed, and then
to get perf levels back to 3770 levels. And I did it by sifting through
millions of lines of Chromium code.

Needless to say I feel really damn good right now. This was a legendary
fix. I'm sorry, I need a little bit of ego just for once. I feel like
I've earned it.

---
## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[c7251155e1...](https://github.com/kleinesfilmroellchen/serenity/commit/c7251155e1d60dd02664248e68d3df83671e2778)
#### Sunday 2022-02-20 13:10:35 by kleines Filmröllchen

LibAudio+Userland: Use new audio queue in client-server communication

Previously, we were sending Buffers to the server whenever we had new
audio data for it. This meant that for every audio enqueue action, we
needed to create a new shared memory anonymous buffer, send that
buffer's file descriptor over IPC (+recfd on the other side) and then
map the buffer into the audio server's memory to be able to play it.
This was fine for sending large chunks of audio data, like when playing
existing audio files. However, in the future we want to move to
real-time audio in some applictions like Piano. This means that the size
of buffers that are sent need to be very small, as just the size of a
buffer itself is part of the audio latency. If we were to try real-time
audio with the existing system, we would run into problems really
quickly. Dealing with a continuous stream of new anonymous files like
the current audio system is rather expensive, as we need Kernel help in
multiple places. Additionally, every enqueue incurs an IPC call, which
are not optimized for >1000 calls/second (which would be needed for
real-time audio with buffer sizes of ~40 samples). So a fundamental
change in how we handle audio sending in userspace is necessary.

This commit moves the audio sending system onto a shared single producer
circular queue (SSPCQ) (introduced with one of the previous commits).
This queue is intended to live in shared memory and be accessed by
multiple processes at the same time. It was specifically written to
support the audio sending case, so e.g. it only supports a single
producer (the audio client). Now, audio sending follows these general
steps:
- The audio client connects to the audio server.
- The audio client creates a SSPCQ in shared memory.
- The audio client sends the SSPCQ's file descriptor to the audio server
  with the set_buffer() IPC call.
- The audio server receives the SSPCQ and maps it.
- The audio client signals start of playback with start_playback().
- At the same time:
  - The audio client writes its audio data into the shared-memory queue.
  - The audio server reads audio data from the shared-memory queue(s).
  Both sides have additional before-queue/after-queue buffers, depending
  on the exact application.
- Pausing playback is just an IPC call, nothing happens to the buffer
  except that the server stops reading from it until playback is
  resumed.
- Muting has nothing to do with whether audio data is read or not.
- When the connection closes, the queues are unmapped on both sides.

This should already improve audio playback performance in a bunch of
places.

Implementation & commit notes:
- Audio loaders don't create LegacyBuffers anymore. LegacyBuffer is kept
  for WavLoader, see previous commit message.
- Most intra-process audio data passing is done with FixedArray<Sample>
  or Vector<Sample>.
- Improvements to most audio-enqueuing applications. (If necessary I can
  try to extract some of the aplay improvements.)
- New APIs on LibAudio/ClientConnection which allows non-realtime
  applications to enqueue audio in big chunks like before.
- Removal of status APIs from the audio server connection for information
  that can be directly obtained from the shared queue.
- Split the pause playback API into two APIs with more intuitive names.

Known issues/exposed bugs:
- Two processes running audio enqueues at the same time will pin the CPU
  at 100% due to both of them yield()ing all the time. See #12679.
- AudioServer hangs in driver after changing sample rate. (Probably
  already an issue before these changes.)
- SoundPlayer's BarsVisualization doesn't draw anything until you switch
  to another visualization and back again.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [SakuraOran/Shiptest](https://github.com/SakuraOran/Shiptest)@[031c0866ed...](https://github.com/SakuraOran/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Sunday 2022-02-20 13:13:53 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Fireblend/squirdle](https://github.com/Fireblend/squirdle)@[72ccf18743...](https://github.com/Fireblend/squirdle/commit/72ccf18743a9ad4c2257fb3153207044ad47237f)
#### Sunday 2022-02-20 13:50:53 by Tyeforce

Update pokedex.csv

Added (missing forms with different generation/type/height/weight data than base forms):
- Giratina Origin Forme
- Thundurus Therian Forme
Note: Mega Evolutions, Primal Reversions, Gigantamax/Eternamax forms, Alolan/Galarian/Hisuian forms, Arceus/Silvally's type forms, and Pumpkaboo/Gourgeist's sizes are still excluded at this time.

Removed (for redundancy; same generation/type/height/weight data as base forms):
- Ash-Greninja
- Meowstic Female
Note: Lycanroc Dusk Form is also redundant with Lycanroc Midday Form, but unsure if it should be kept or not due to Midnight Form's inclusion

Changed (corrected Pokémon names):
- "Ho-oh" to "Ho-Oh"
- "Thundurus" to "Thundurus Incarnate Forme"
- "Meowstic Male" to "Meowstic"
- "Hoopa Hoopa Confined" and "Hoopa Hoopa Unbound" to "Hoopa Confined" and "Hoopa Unbound"

---
## [very-scary-scenario/relocaliser](https://github.com/very-scary-scenario/relocaliser)@[fc5bdde366...](https://github.com/very-scary-scenario/relocaliser/commit/fc5bdde3664fe51c8c79e83e6748f85c7ebf4496)
#### Sunday 2022-02-20 15:43:08 by colons

Use Firefox for image rendering, and try to fix the height check.

Ubuntu made me do this. Fuck you, Canonical.

---
## [gh4ever/dictionary-react-app](https://github.com/gh4ever/dictionary-react-app)@[ba9ad2c654...](https://github.com/gh4ever/dictionary-react-app/commit/ba9ad2c654e1c3e868b999d659fd1e62aca3b1e2)
#### Sunday 2022-02-20 16:13:37 by gh4ever

my stupid ass api key from effing annoying pexels

563492ad6f91700001000001ac6bd4a96db444b2b8110ee3e62d4edd

---
## [mgartner/cockroach](https://github.com/mgartner/cockroach)@[255c1fb027...](https://github.com/mgartner/cockroach/commit/255c1fb02708f99fef62b0af719af5e0984d9de3)
#### Sunday 2022-02-20 17:09:59 by craig[bot]

Merge #71542 #73319 #74077 #76401 #76748

71542: backupccl: Support RESTORE SYSTEM USERS from a backup r=gh-casper a=gh-casper

Support a new variant of RESTORE that recreates system users that don't exist in current cluster from a backup that contains system.users and also grant roles for these users. Example invocation: RESTORE SYSTEM USERS FROM 'nodelocal://foo/1';

Similar with full cluster restore, we firstly restore a temp system database which contains system.users and system.role_members into the restoring cluster and insert users and roles into the current system table from the temp system table.

Fixes: #45358

Release note (sql change): A special flavor of RESTORE, RESTORE SYSTEM USERS FROM ..., is added to support restoring system users from a backup. When executed, the statement recreates those users which are in a backup of system.users but do not currently exist (ignoring those who do) and re-grant roles for users if the backup contains system.role_members.

73319: jobs: Execute scheduled jobs on a single node in the cluster. r=miretskiy a=miretskiy

Execute scheduled jobs daemon on a single node -- namely, the lease
holder for meta1 range lease holder.

Prior to this change, scheduling daemon was running on each node,
polling scheduled jobs table periodically with a `FOR UPDATE` clause.
Unfortunately, job planning phase (namely, the backup planning phase) could
take significant amount of time.  In such situation, the entirety
of the scheduled jobs table would be locked, resulting in inability
to introspect the state of schedules (or jobs) via `SHOW SCHEDULES` or similar
statements.

Furthermore, dropping `FOR UPDATE` clause by itself is not ideal because
that would lead to expensive backup planning being executed on almost every
node, with all but 1 node making progress.

The single node mode is disabled by default, but can be enabled
via a `jobs.scheduler.single_node_scheduler.enabled` setting.

Release Notes: scheduled jobs scheduler now runs on a single node by default
in order to reduce contention on scheduled jobs table.

74077: kvserver: lease transfer in JOINT configuration r=shralex a=shralex

Previously:
1. Removing a leaseholder was not allowed.
2. A VOTER_INCOMING node wasn't able to accept the lease.

Because of (1), users needed to transfer the lease before removing
the leaseholder. Because of (2), when relocating a range from the
leaseholder A to a new node B, there was no possibility to transfer
the lease to B before it was fully added as VOTER. Adding it as a
voter, however, could degrade fault tolerance. For example, if A
and B are in region R1, C in region R2 and D in R3, and we had
(A, C, D), and now adding B to the cluster to replace A results in
the intermediate configuration (A, B, C, D) the failure of R1 would
make the cluster unavailable since no quorum can be established.
Since B can't be added before A is removed, the system would
transfer the lease out to C, remove A and add B, and then transfer
the lease again to B. This resulted a temporary migration of leases
out of their preferred region, imbalance of lease count and degraded
performance.

The PR fixes this, by (1) allowing removing the leaseholder, and
transferring the lease right before we exit the JOINT config. And (2),
allowing a VOTER_INCOMING to accept the lease.

Release note (performance improvement): Fixes a limitation which meant 
that, upon adding a new node to the cluster, lease counts among existing
nodes could diverge until the new node was fully upreplicated.

Here are a few experiments that demonstrate the benefit of the feature.
1. 
> roachprod create local -n 4 // if not already created and staged
> roachprod put local cockroach
> roachprod start local:1-3 --racks=3 // add 3 servers in 3 different racks
> cockroach workload init kv --splits=10000
> roachprod start local:4 --racks=3 // add a 4th server in one of the racks

Without the change (master):
<img width="978" alt="Screen Shot 2022-02-09 at 8 35 35 AM" src="https://user-images.githubusercontent.com/6037719/153458966-609dbb7e-ca3d-4db6-9cfb-adc228f2bdf2.png">

With the change:
<img width="986" alt="Screen Shot 2022-02-08 at 8 46 41 PM" src="https://user-images.githubusercontent.com/6037719/153459366-2d4e2def-37cf-405b-b601-8be57419ae02.png">

We can see that without the patch the number of leases on server 0 (black line) goes all the way to 0 before it goes back up and that the number of leases in other racks goes up, both undesirable. With the patch both things are no longer happening.

2. Same as 1, but with a leaseholder preference of rack 0:

ALTER RANGE default CONFIGURE ZONE USING lease_preferences='[[+rack=0]]';

Without the change (master):
<img width="966" alt="Screen Shot 2022-02-09 at 10 45 27 PM" src="https://user-images.githubusercontent.com/6037719/153460753-bce048f0-f6da-4e21-afdc-317620c035b2.png">

With the change:
<img width="983" alt="leaseholder preferences - with change" src="https://user-images.githubusercontent.com/6037719/153460780-55795866-cf47-404d-b77a-45d9e011f972.png">

We can see that without the change the number of leaseholders in racks 1 and 2 together (not in preferred region) grows from 300 to 1000, then goes back to 40. With the fix it doesn’t grow at all.






76401: pgwire: add server.max_connections public cluster setting r=rafiss a=ecwall

This setting specifies a maximum number of connections that a server can have open at any given time.
<0 - Connections are unlimited (existing behavior)
=0 - Connections are disabled
>0 - Connections are limited
If a new non-superuser connection would exceed this limit, the same error message is
returned as postgres: "sorry, too many connections" with the 53300 error code
that corresponds to "too many connections".

Release note (ops change): An off-by-default server.max_connections cluster
setting has been added to limit the maximum number of connections to a server.

76748: sql: add missing specs to plan diagrams r=rharding6373 a=rharding6373

This change allows missing specs (e.g., RestoreDataSpec and
SplitAndScatterSpec) to be shown in plan diagrams. Before this change a
plan involving these types would result in an error generating the
diagrams. Also added a test to make sure future specs implement the
`diagramCellType` interface, which is required to generate diagrams.

Release note: None


Co-authored-by: Casper <casper@cockroachlabs.com>
Co-authored-by: Yevgeniy Miretskiy <yevgeniy@cockroachlabs.com>
Co-authored-by: shralex <shralex@gmail.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: rharding6373 <rharding6373@users.noreply.github.com>

---
## [tdauth/wowr](https://github.com/tdauth/wowr)@[d55f394053...](https://github.com/tdauth/wowr/commit/d55f3940534e1fe784b4b858fab128acf7bbba5b)
#### Sunday 2022-02-20 18:49:57 by barade

1.9.9

- Save XP of hero 2 in savecodes.
- Replace bugged Frost Armor ability of Crown of the Lich King by Item Attack Frost Bonus.
- Fix soundset of bonus hero Medivh.
- Give bonus hero Malfurion Invisibility and Summon Mount abilities.
- Remove ability Spell Immunity from bonus hero Wizard. Otherwise, it would take too many slots.
- Add missing learn tooltips to ability Summon Sea Elemental of bonus hero Admiral Proudmoore.
- Try to revive Illidan immediately before changing his ownership to avoid a bug while he is being revived.
- Make items in backpack always droppable to fix the drop bug with Illidan's Ring of the Dark Legion.
- Increase the produced food of Hideouts and all upgraded versions from 25 to 55.
- Add ability Invisibility to bonus hero Anasterian Sunstrider.
- Fix ability Storm Bolt in the description of bonus hero Rexxar.
- Turtle Shell and Frostmourne use fixed defense and attack type values now to avoid bugs.
- Remove Neutral Citizen Female from Goblin Laboratories to get the Reveal slot back.
- Add new boss Murloc Sorcerer on a new island with creeps.
- Add Gnomish Submarines.
- Replace Taunt of hero Mountain Giant with Hurl Boulder.
- Add note how to repick your second hero when picking him/her.
- Add new boss The Eye of Sargeras on a new island with creeps.
- Add Boss Fight Island.
- Fix mount in description of Brewmaster, Tinker and Alchemist.
- Change recommended start location of Pit Lord to Outland.
- Crystal Ball is sold by Power Generator.
- Add new fixed computer player The Alliance.

---
## [elodotwe/2022practice](https://github.com/elodotwe/2022practice)@[cb1ee3e7dd...](https://github.com/elodotwe/2022practice/commit/cb1ee3e7ddc39907316156db74ff24948533f009)
#### Sunday 2022-02-20 18:54:21 by Jacob Rau

"Long shot" autonomous

Was tinkering to see if I could pick up all 3 of our balls from our side
of the field and deliver them all before auton is over. If we drive like
hell, and the pickup and shooter both work 100% and fast, then yes.

I kinda think not, but hey, it's a nice dream right?

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6b180a3303...](https://github.com/mrakgr/The-Spiral-Language/commit/6b180a330367a5517ae6a90a2850539173d32b2f)
#### Sunday 2022-02-20 19:34:15 by Marko Grdinić

"11:05am. Let me chill a bit and then I will get started. Such a heavy night. My stress levels are too high because I am pushing myself too hard. I really need to stop at the alloted time.

11:25am. Let me play with UV Flatten a bit more. Then...

11:40am. Ok, enough. It is as I thought. If you want to maximize coverage while minimizing distortion, what you should do is cut all the faces individually. The regular unwrap is just horrible at things like spheres.

Let me have a break here. Once I start painting things are going to take a while.

12:10pm. Done with breakfast. Let me do the chores here.

Clearing the wall will take me more than usual.

I really do not feel like doing anything today, I haven't slept properly tonight. Today I should just go to bed no later than 11am. Forget going past that.

1:20pm. Done with the chores. They took less than I thought they would.

1:25pm. I need to get started. Now where do I begin? First of all, let me check out the big block that makes the island platform.

1:45pm. The UVs in Houdini are driving me insane.

That big block is easy enough to unwrap when it is a square. But after I do the boolean with the pool, the UVs get wrecked. So I have to do the UVs after the booleans. But after the booleans, even if I put the seams, it inwraps them in uncomfortable places. The ground ends up being rotated.

So put the pins in the corner and adjust it manually. What is the problem?

The problem is that due to all the overlapping textures in the UV view, I literally can't see where the top part is. Fuck!

This is different from in Blender. When I open the UV mode in Blender, whether I select in the edit mode ends up being highlighted and isolated in the UV window. Here I get shit. I hate Houdini's shitty UI design.

What do I do about this? This would not have been a problem had I been using flat colors only, but I really should use the floor tiles. I can hardly call myself an expert if I can't do at least this much.

1:55pm. > Adjusts texture coordinates in the UV viewport by painting.

Hmmm, Houdini does have an UV brush?

2pm. I go into UV Edit so I can scale the UVs because they are too big for the tile. I enter the group select. I press N to select all the groups. I press enter to confirm. None of the groups get selected. I play around and note that individual groups work.

2:10pm. i managed to get it to work. But I'd be fucked if the geometry had more islands and was more complex.

https://vimeo.com/257186263
UV Flatten | Cut, Sew, Align & Straighten

2:15pm. Focus me stop looking at /a/ on the side.

...Ahhh, I forgot about the UV transform. I should have used that to scale instead of Edit. Let me fix that mistake.

2:20pm. Had to get a refil. Let me go back to the video.

> Visibility SOP will allow me to isolate the geomtry that I want to cut the seams.

I didn't expect this to take another SOP. It was the right decision to watch this.

2:30pm. I never noticed the repack button. That could be useful.

Also this ability to align might be really useful when I work on the flower stalk. Houdini goes between the two extremes of annoyance and admiration for me. This is definitely one of the times I admire it.

2:35pm. Wait, you can press Q and select? That is another thing I did not know about.

2:40pm. Let me think. What do I do now. I've put in the textures for the floor.

I need to keep going forward. Do I have the displacement?

2:45pm. Occlusion literally does nothing noticeable.

Displacement is giving me some trouble. it does not work properly in

Oh, I was wrong. What I thought was wobbliness was in fact displacement. It is just that it is shitty in the viewport renderer.

....Ahhhhhh, I completely forgot about this, but I was supposed to watch the Solaris vids. Right.

Well, first let me try making a Mantra render of the scene. This is without the vines. After that I'll decide where I want to go. If the renders end up taking some ridiculous amount of time once I put in all the geometry, I might ditch Houdini in favor of Blender. But if it works...

Well, let me give it a try.

Even after 1.5m of rendering it looks like shit. Mantra is basically unusable.

I can't wait 10m every time to get something decent. And this is without the flowers which will increase the complexity massively. Let me try Karma.

Why can't I select the camera I previously put in?

Houdini is just super annoying at times and this is one of those times.

There is no way around it. Here I either get rendering to run in reasonable time or I go back to Blender. Let me watch the Solaris vids.

https://www.sidefx.com/learn/solaris-karma/

I am thinking what to start here. CGForge was quite decent last time so let me try it.

The turials are somewhat old, but let me roll with it.

https://youtu.be/y2ywi_c-ftg?t=45
> So if you want to use Karma, this is not where you go for that.

He is talking about the out context. Have I been using it wrong. in the previous versions, it wasn't even here.

3:10pm. https://youtu.be/y2ywi_c-ftg?t=93
>Lops utilizes USD to build out your entire scene.

I doubt he means actual dollars. I keep hearing about USD, what is it?

https://youtu.be/y2ywi_c-ftg?t=297

Hmmmm...Let me give this a try.

Houdini crashed as soon as I tried opening a LOP network.

3:20pm. Now I am letting Karma grind away, but it is quite slow as well. Rather than use SOP Import, I did a scene import and put in everything in obj.

3:30pm. 7:20m for this? The resulting image is quite noisy as well. Ew.

At this point I should start thinking how to go back to Blender or how to get an outside render.

3:35pm. Let me take a break here.

3:40pm. Let watch the rest of these videos. I need to figure out what Solaris is at least.

3:45pm. I have no focus. Right now I am waiting for the bathroom to clear. Let me waste time some more then.

You know what, forget the main scene. The thing I want to animate first is look up from the bottom of the pool. The scene I am building for this first image is not even going to be present.

That is what I should focus on. I need to shade the vines and the bulbs, and the leaves. This will be easy. I will also set up the water. I'll replace the Luna box with some prop as well.

Then I'll render it in Karma. I need to see how long that will take.

3:50pm. No forget shading the flowers. Let me check out how long that will take period.

4:10pm. Let me resume. Forget worrying about Houdini's renderers being slow. Let me just see how long it takes Karma to do the wines.

4:15pm. I am running into responsiveness bugs. I switch from XPU to regular and the viewport does not update. Houdini is full of such annoyances.

It has a weak reactive foundation. The under the hood work is not solid.

4:20pm. The XPU option confuses me. I gives me a sort of decent result in 5s and then stops. It is hard to believe that this is real.

At any rate, what I've been fearing is not reality. I thought that once I turned on the vines and increased the scene poly count massively that the renderer will start to drag even more, but it still finishes in 7m either way.

This just about makes things doable.

Let me watch a tutorial on Karma XPU. Can I let it run for longer. Alternatively, can I pirate an 3rd party rendered. I'll look up CG Peers. It is invite only.

https://berkerdag.medium.com/experiment-testing-houdini-karma-xpu-in-a-big-scene-57da531f7972
> Then came materials, where I decided to use the new Material X shaders. They were easy to use and a bit faster with Karma compared to Principled Shader.

Some of the tuts I am eyeing mention these shaders as well.

> After these tweaks render times on average was 6.5 minutes per frame. Of course the beginning of the shot rendered faster since there was not much foam and the HDRI -which is very fast to render- was more visible. Whereas the end parts of the render was much slower, the reason being a big wave, more foam and refractions and less negative space.

> If you are wondering, I tried to render with Karma CPU too and it gave me 13 hours and 45 minutes ETA for one frame and I didn’t wait for it to finish as you might have guessed.

So it is not an accident that XPU finished in 3s.

Still, there is no way that this is enough for the scene. It would not be enough for Cycles. Or maybe it would.

///

* Karma XPU is again pretty fast and for an Alpha version of a renderer it doesn’t crash often.
* One of the most important thing is, the render starting instantly, so when you hit render you start to see the first pixels immediately (most GPU renderers are not like that) and it makes material and render tests a lot easier. The annoying thing is each time I open the Karma Viewport it converted everything into USD which when added up takes a lot of time. But if you use the Solaris Context you won’t have that issue, therefore using Solaris for big scenes is essential.
* There are no random weird errors or crashes like in Karma Beta in Houdini 18.5.
* Material X is very easy to use compared to principled shader, it resembles the other materials you find in various render engines like Arnold, Redshift, Octane, Vray, therefore migrating to MatX is not painful.
* Particles felt a bit unpredictable, both renderwise and had issues with motion blur but I am sure it will be fixed soon.
* I also feel motion blur makes the render run more slower compared to other GPU renderers although I didn’t do a side by side test with the same scene on another GPU renderer with motion blur.

///

So it is good aparently. Maybe I won't need to look for outside renderers.

> For the render settings first I used the new trick that I hear often which is to get a sharp 1920x1080 render, you render in a 4K resolution with low samples then denoise with Intel or NVIDIA Optix Denoiser inside Houdini and then scale down to 1920x1080. I tested this and it really didn’t lose any quality and had a much sharper look. The great thing about this method is, for example rendering 3840x2160 resolution with 16 samples takes the same time as 1920x1080 with 64 samples.

This trick is worth keeping in mind.

https://youtu.be/tI4zqTezniI
Test Driving Houdini 19: Karma XPU, MaterialX And A Hidden Gem

Let me watch this. After that I am going to watch the rest of the lighting tuts.

4:40pm. Yeah, it boggles my mind that it can go from 7m to 3s. Something has to be wrong for that to happen. The GPU is good, but not that good.

https://youtu.be/tI4zqTezniI?t=308

Maybe it would ...

No wait, instead of convert line, it might have been worth using edge group to curve?

Oh, this is a great node. Instead of ripping the nodes into separate primitives, it leaves them whole. The reason why that is important is because convert line messes up the edge flow.

It does use Convert Line internally.

https://youtu.be/tI4zqTezniI?t=451

Ah, I forgot about having multiple tabs.

I am really learning a lot from this.

Maybe there is hope for Houdini. I had issues, but there are solutions. At first I complained a visibility, but there is the Visibility SOP for that. Now I am trying to deal with shaders, and it seems that Houdini 19 will be able to take care of it.

https://youtu.be/tI4zqTezniI?t=457

He mentions that MaterialX is the new standard that not only Houdini, but Unreal as well is going to support.

https://youtu.be/tI4zqTezniI?t=604

Wow, it really is fast. Still, why is it not using a noise threeshold instead of the pixel samples?

https://youtu.be/tI4zqTezniI?t=806

This is a such an useful tutorial. It tells me how to ramp up the quality, how to turn on caustics and now it is showing me how to import things into the stage context.

https://youtu.be/tI4zqTezniI?t=956

Did he sweep the wire? I need to go back and check.

https://youtu.be/tI4zqTezniI?t=1015

Nope. Strange that it show up in render regardless.

5:05pm. Great tut. It is worth taking Karma XPU seriously. It is way faster than I would have expected. I'll have to figure out how to use the MaterialX shaders, and how to load textures using a separate node, but nevermind that.

If it were a few years earlier and I was on Houdini 18, I'd have to drop it at this point, but now I can still keep going. I can make this work. There is no need to drop Houdini and its benefits.

5:15pm. Focus me. Enough of that breather. Let me watch the rest of the shading tuts.

I am going to have to figure out how to pain my own roughness map so that only the entry of the pool looks wet. Right now the tiles are too glossy and reflective.

https://youtu.be/wLJmr5d78I0?t=27

Now that I have more hope, I can focus on the properly. These light mixers could be quite useful.

https://youtu.be/wLJmr5d78I0?t=151
> I love how intuitive that is.

Yeah, it is nice.

https://youtu.be/wLJmr5d78I0?t=232
> It is a lot more straightforward on this node than it is on the Mantra node.

https://youtu.be/wLJmr5d78I0?t=387
He mentions the variance threeshold works by looking at the contrast between neighboring pixels. Pixel samples determines the maximum. I should crank that up to get better quality.

5:30pm. Actually, I had no idea that with Ctrl + Shift + Esc I could open the Task Manager directly. I usually go through Ctrl + Alt + Delete.

5:35pm. Focus me, leave the Baki thread for later.

https://youtu.be/_X9sl5d_ObE?t=215
> Many of you have never worked at a large studio, and so many of you don't really know about the specific challenges that are obvious to people who work at a studio every day.

https://youtu.be/BFIbTjtgyv8?t=61

So stage is a LOP net as I expected.

https://youtu.be/BFIbTjtgyv8?t=749

He is really putting me to sleep here. Just move on dude, I get object hierarchies.

https://youtu.be/EKPZE1RFwzM?t=161

I am confused. Why does this result in two barrels for him? Does the edit work differently in a LOP network?

https://youtu.be/AbZ3XyM9UDw
Learning Solaris - Part IV - CG Forge

Thus far, this series has been incredibly boring.

I am going to forget everything he is talking about soon enough.

6:20pm. Let me stop here so I can have lunch. Then I'll finish the last two vids in this series and call it a day.

7:15pm. Let me watch the last two vids...No, I am too tired. Let me close. Trying to push myself here will just spike my stress levels.

https://youtu.be/Y8JVxnJSDic
Should you render in Houdini?

Let me listen to these two guys talk instead. I am done for today.

*

7:40pm. https://youtu.be/Y8JVxnJSDic?t=1489
> I enjoy exporting the stuff to Blender and doing the lookdev there.

He talks about how Solaris added more complexity rather than reduced it. And before that he mentioned how much he likes working with geometry in Houdini. Holy shit, he is like me.

I really wonder if I could schlep things back to Blender and finish the shading and the rest there?

They mention that animating the camera inside Houdini is a pain in the ass.

https://youtu.be/Y8JVxnJSDic?t=1590
> It is weird that SideFX clearly misses the point on lookdev on the way Solaris has been built.

https://youtu.be/Y8JVxnJSDic?t=1658
> In Blender you have these shortcuts where you press G and move your object around. And in Houdini you have these handles and they are just off...

https://youtu.be/Y8JVxnJSDic?t=1750
> In Houdini it is a pain in the ass to make even a diffuse map show up correctly.

https://blender.stackexchange.com/questions/81851/does-transparency-work-in-eevee

///

Use these settings:

Render → Screen Space Reflections - On
Render → Screen Space Reflections → Refraction - On
Material → Surface → Principled BSDF → Transmission - 1.000
Material → Surface → Principled BSDF → Roughness - Adjust to your needs
Material → Settings → Blend Mode - Opaque
Material → Settings → Screen Space Refraction - ON
Material → Settings → Refraction Depth - Adjust to your needs, I generally suggest 0.8 but depends on the thickness of the object.

///

It seems it might be possible to get transmission to work with Eevee. I should have checked a lot earlier instead of assuming it is impossible.

8:20pm. Let me try setting it up and I will take a bath.

8:25pm. It really works!

8:35pm. It seems I forgot to push the last commit. Let me do it now."

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[620fc5cb02...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/620fc5cb022b2a9c441515d952a0db1303d38435)
#### Sunday 2022-02-20 19:50:15 by AmCath

guides.24.t:0 "Union of Britain Guides" guides.24.d:0 "To Get Hobart-Elect Mosley in the Trade Union Congress chain. After electing Mosley, you'll get an event about anti-mosley activity in the army, choose to ignore it. During the Revolution event, choice to declare martial law. In the following event, have Hobart's men win the day. In the following event, you can choice to either restore the UK or have Hobart stay in power. (note: The AI will never restore the UK and will always have Hobart hold on)\n\nHow do I get the various Counterrevolutionary paths? For Atlee: During the Return of the True Exiles event chain, work with the Liberals, and Atlee will come to power\nFor Legionary Britain: Work with nationalist groups than cave to the Legionaries and they'll come to power.(An event to switch between Leese or Joyce will fire after completing the Expose World Jewry focus) \nFor Archibald Ramsay and the Right Club: Work with nationalist groups, don't cave to the Legionaries and accept their aid. (if you have Ramsay become Lord High Chancellor, you'll get an event sometime after were he can die and be replaced by Hilaire Belloc)\nFor Hobart: Work with Nationalist groups, don't cave to the legionaries and don't accept the aid of the Right Club.(depending on if you elect a King or have Hobart become the new Cromwell, new faction joining will be open)" guides.24.a:0 "Cool" guides.24.b:0 "Go Back"

---
## [crawl/crawl](https://github.com/crawl/crawl)@[a852ce8369...](https://github.com/crawl/crawl/commit/a852ce8369264a3a4759b99df0bbba7645a78c97)
#### Sunday 2022-02-20 20:10:35 by Nicholas Feinberg

Play with ranged weapon stats more

Following some thinking about ranged weapons, here's a new set of
ammoless stats. Philosophy:

- Slings are high-skill 1-handers. Hunting slings are vaguely like
  war axes, and fustibaluses are no longer ultra-rare but are now
  more like broad axes.
- Bows are high-skill 2-handers.
- Crossbows are lower-skill - it takes fairly little to get the hand
  crossbow or the arbalest to mindelay. The triple crossbow is still
  high-skill, but it's quite rare, so doesn't define the 'feel' of
  the class, much as you can't rely on finding a triple sword as a
  lbl user or an exec axe as an axe user. (Unless a gifting god gets
  involved.)

If we're going to keep all these item classes, it would be great to
have some more obvious and pronounced gimmicks. I suspect we'll end
up merging or removing some of these at some point, but that's a
larger project than I'm ready for right now.

TODO: make fustibali spawn at a higher rate - right now they're about
1/5th as common as I'd like.

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[bdc055b803...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/bdc055b803fc9d049a6ac95d093cf826ca3a1921)
#### Sunday 2022-02-20 20:39:51 by AmyBSOD

New feminism traps

OMG amy they are SOOOOOOO offensive I don't even! like why do you even have that shit in your game that's turbo gross and misogynistic and transphobic and oh my god why does your game even exist of course it rightfully got removed from that big public server because seriously what the FUCK!!!!!!!!!!11111

Anyway, they're unfinished but it's taking time to code all that stuff.

---
## [mawrick26/SM8250](https://github.com/mawrick26/SM8250)@[e63d06fbeb...](https://github.com/mawrick26/SM8250/commit/e63d06fbeb0f86024896e31da815665ce56e48cd)
#### Sunday 2022-02-20 21:50:26 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [dav1312/Stockfish](https://github.com/dav1312/Stockfish)@[cb9c2594fc...](https://github.com/dav1312/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Sunday 2022-02-20 22:22:22 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [BoomerangAide/CustomJSforFx](https://github.com/BoomerangAide/CustomJSforFx)@[64066ac621...](https://github.com/BoomerangAide/CustomJSforFx/commit/64066ac621e141ac88ba5db884dc79db5b87dbb2)
#### Sunday 2022-02-20 22:25:51 by UndeadStar

Create download_button_open_list_directly.js

My other exclusive change with "other_customizations".
Left click on download button open a downloads window, Right click open the downloads in a new tab (as well as opening the context menu), and middle click attempt a retry on all downloads that may be in error, useful for buggy sites, ended up on middle click because having the context menu open every time I tried to use that was annoying.
While downloading, it is possible to track how many downloads are ongoing, successful, stopped or cancelled with the tooltip text.
It should restore the default localized tooltip text when there are no downloads.
Download window has a "Clear successful downloads" (instead of the genocidal "remove all completed downloads" usually available that remove the errors and make you lose all your progress) and a Retry All (I don't remember if it's still bugged and will only retry one of the failed on every click, or if it do retry every failed dl right now).
Also has stuff related to "attention" attribute due to CSS personal mods.
Known bug: the window increase its height infinitely instead of allowing to scroll, workaround to leave it working enough was implemented that move the buttons at the top beyond a certain height, the fix should be somewhat generic and compatible with all resolutions, though more or less accurate.

---
## [matchu/engineering-for-good](https://github.com/matchu/engineering-for-good)@[d1b66c1cf1...](https://github.com/matchu/engineering-for-good/commit/d1b66c1cf12b4a3490fdc973804be6a2ba165f38)
#### Sunday 2022-02-20 22:57:35 by Matt Dunn-Rankin

Remove Khan Academy re workplace & values concerns

A lot of good work has happened at Khan Academy over the years, but Sal himself is unfortunately not an especially values-oriented leader, in my opinion.

We had to organize a strike in order to force him to allow any anti-racism education or action during the Black Lives Matter uprisings in 2019. We also demanded that he *not* invite a known racist politician onto his podcast during that time, to which he responded with a contemptuous email reminding us to keep an open mind and not silence people we happen to disagree with politically.

Staff and executives have been fleeing since, which means Sal is even more empowered to take unilateral action, like his recent NFT gambling game partnership that he advertised on the official school YouTube channels for children, and in a special CNBC interview. When former employees started raising concerns in the company's Slack channel for us, Sal personally banned all the people who did (except the white men), and eventually shut down the channel altogether.

I've also personally witnessed *many* instances of discrimination in the engineering department, and concerns are consistently met with career-ending retaliation. And it doesn't help that Sal in particular loves to surround himself with young starry-eyed industry newcomers, who are primed to believe whatever he and the company say. Practically all of my personal friends during my 5 years left the org confused and broken, taking years to recover 😖

Former employees have been talking about it more recently, here's a link summary thread from Caroline Charrow: https://twitter.com/CarolineCharrow/status/1492695969917407232

Good things have happened at Khan Academy, but I worry that's increasingly in the past; and I would strongly warn marginalized people not to trust management whatsoever. If it were me, I wouldn't include the company on a list of recommendations. Thank you for considering!

---
## [crawl/crawl](https://github.com/crawl/crawl)@[b0a319194c...](https://github.com/crawl/crawl/commit/b0a319194c5fb1ade151c20a8f7ed1952bf500cf)
#### Sunday 2022-02-20 23:01:02 by Nicholas Feinberg

Improve characters' starting kits (Hellmonk)

One of the most interesting and exciting decisions in Dungeon Crawl
is when and where to use your consumable items. In the very early
game, characters may not yet have any consumables, which diminishes
the tactical aspect of the game.

So, let's try to give most characters some options which, if used
wisely, can help them with a tough situation.

- All 'mages' ('pure casters') start with a potion of magic.
- Fighters get an additional potion of might.
- Gladiators get a few throwing weapons, roughly half of what the AM
  throwing start got.
- Monks get a potion of ambrosia. (See, it's divine.)
- Hunters get a throwing net. (Not sure about this one.)
- Brigands get an additional poisoned & curare dart.
- Artificers trade their xom piece for three charges of iceblast.
- Wanderers get an additional random potion or scroll.
- Delvers get nothing, for now, since I'm already pretty happy with
  how they play. They're a challenge anyway, really. :)
- Berserkers and Cinder Acolytes likewise get nothing. They already
  have perfectly good early game buttons.
- Abyssal Knights start at 60 piety (just over 2*) instead of 38 (just
  over 1*). This should allow them to use Bend Space if needed.
  (I think they're still quite weak.)
- Chaos Knights get Artificer's xom chesspiece.
- Transmuters get a potion of lignification, which should work well
  with their unarmed combat focus. It's also very thematic.
- Warpers get another scroll of blinking and a few more boomerangs of
  dispersal. This is one of the strongest boosts, but warpers were
  not particularly strong to start with.
- Arcane Markspersons get a few boomerangs of dispersal too. I'm sort
  of hoping to rework this background more broadly at some point.
- Enchanters get another potion of invisibility.

This should also be a nice compensation for various recent changes that
increased early game difficulty.

---

