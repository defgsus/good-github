## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-07](docs/good-messages/2022/2022-09-07.md)


2,154,644 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,154,644 were push events containing 3,280,436 commit messages that amount to 230,685,871 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [chanzuckerberg/redcord](https://github.com/chanzuckerberg/redcord)@[c26372291d...](https://github.com/chanzuckerberg/redcord/commit/c26372291df9414046f6bf3160a11e5487479662)
#### Wednesday 2022-09-07 00:03:27 by Matt Wang

fix Ruby 3 keyword arg errors (#110)

Overall, this PR resolves issues that *break tests* on Ruby 3. It's a different question on whether or not these actually bring us to Ruby 3 usability.

To test this, I think we should probably link in `redcord` to `traject` locally, and run some tests. I'm not sure if this is sufficient (or how confident we are in the test coverage in general).

Even though these two changes are one-liners, I do want to enumerate my reasoning - and apprehension - for both.

### `.send` and `define_method`

This one was trickier to hunt down, since I was confused where this call was coming from; the deprecation warning indicates that it's from sorbet, but it's actually a call validation layer in-between `redis.send`.

The core issue is explained in the "Handling argument delegation" of [the official post](https://www.ruby-lang.org/en/news/2019/12/12/separation-of-positional-and-keyword-arguments-in-ruby-3-0/); the tl;dr is

```ruby
# Ruby 2.6, works
# Ruby 2.7, deprecation warning
# Ruby 3, ArgumentError
def foo(*args, &block)
  target(*args, &block)
end

# Ruby 2.5, 2.6: seems to have a problem
# Ruby 2, may require `Module#ruby2_keywords`
# Ruby 3, works
def foo(*args, **kwargs, &block)
  target(*args, **kwargs, &block)
end
```

In `connection_pool`, we iterate through instance method; one of them is `create_hash_returning_id`:

```ruby
redis.send(:create_hash_returning_id, *args, &blk) 
# ~ redis.create_hash_returning_id(*args, &blk)
```

`create_hash_returning_id` takes a mix of both positional and keyword args. Thus, the new behaviour (which separates them) won't work, we'll instead need to do

```ruby
redis.send(:create_hash_returning_id, *args, **kwargs, &blk)
# ~ redis.create_hash_returning_id(*args, **kwargs, &blk)
```

So, this PR does that. 

It's a bit unclear to me on whether or not I should also update `method_missing` and `define_method`, though my intuitive understanding of this is that we should. Would love a double-check here.

(under the hood - this should resolve other sorbet call-validator errors we get, like the ones we saw in Along)

### `zscan_each`

This is a more straightforward example. I'm more curious about the behaviour we want, and in particular, why the `key` parameter was `nil` before (was it?)! And, should we be setting the `key` value to `key` instead?

Anyways, explicitly setting the positional argument as `nil` forces the keyword argument to be interpreted as a keyword. I think this is one of the edge case-like issues they discuss in the "Why we're deprecating the automatic conversion" section [of the release blog post](https://www.ruby-lang.org/en/news/2019/12/12/separation-of-positional-and-keyword-arguments-in-ruby-3-0/).

---
## [AcPvP/PkKillTracker](https://github.com/AcPvP/PkKillTracker)@[2a123bb106...](https://github.com/AcPvP/PkKillTracker/commit/2a123bb106c3033a2fec6515fe8902ffa01dc988)
#### Wednesday 2022-09-07 00:08:54 by AcPvP

Fuck Microsoft and their stupid fucking bullshit always changing how things work and making the most convoluted bullshit documentation

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[3b2cf65d59...](https://github.com/Shadow-Quill/tgstation/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Wednesday 2022-09-07 00:37:13 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [julianamilson/42-libft](https://github.com/julianamilson/42-libft)@[5f54d948e7...](https://github.com/julianamilson/42-libft/commit/5f54d948e7ae9cf6428a2b117a3b1a749e6a7be6)
#### Wednesday 2022-09-07 01:01:02 by Juliana Milson

Update README.md

Special thanks to Felipe Aguilar. May you rest in peace, my friend. You'll always be remembered.

---
## [bosmak/otservbr-global](https://github.com/bosmak/otservbr-global)@[fbd70d116c...](https://github.com/bosmak/otservbr-global/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Wednesday 2022-09-07 01:04:12 by rigis1

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
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[a4bfe65cb1...](https://github.com/Paxilmaniac/Skyrat-tg/commit/a4bfe65cb1caece1e3e6a4635fa17d39f1aa3478)
#### Wednesday 2022-09-07 02:05:22 by SkyratBot

[MIRROR] Dimensional Anomaly [MDB IGNORE] (#15974)

* Dimensional Anomaly (#69512)

About The Pull Request

Everyone has been asking: "When will there be an anomaly like the bioscrambler, but for the space station? Please, we need more things which replace objects with different objects from the same typepath."
Well I made it and it looked like ass because non-tiling floor and walls look terrible, so then I made this instead.
Dimensional.mp4

The "dimensional anomaly" shifts matter into a parallel dimension where objects are made out of something else.
Like the Bioscrambler anomaly, it does not expire on its own and only leaves when someone signals it or uses an anomaly remover.
When it spawns it picks a "theme" and converts terrain around it until it covers a 7x7 square, then it teleports somewhere else and picks a new theme.

A lot of these themes are relatively benign like "meat", "fancy carpet", or "gold". Some of them are kind of annoying like "icebox" because it creates floor which slows you down, or "clown" because bananium is intentionally annoying. Some of them are actively dangerous, mostly "uranium" and "plasma".
The main problem this will usually cause for crewmembers is decreasing area security. When it replaces doors it replaces them with ones which don't have any access control, and it will also replace RWalls with normal and much more vulnerable walls which will make breaking and entering significantly easier until someone has taken the time to fix the damage. But also sometimes it will irradiate them, you never know.

The fact that sometimes the changes are benign (or provide uncommon materials) and might be happening in places you don't care about access to might encourage people to push their luck and leave it alone until it starts turning the captain's office into a bamboo room or repainting medbay a fetching shade of flammable purple, which I would consider a success.
Armour.mp4

If you successfully harvest the anomaly core you can place it into the reactive armour to get Reactive Barricade Armour, which shifts your dimension when you take damage and attempts to place some randomised (not terribly durable) objects between you and hopefully your attacker (it really just picks up to four random unoccupied tiles next to you). If you're EMPed then the changes it make to the environment will often be as unpleasant for you as they are for a pursuer, and significantly more likely to harm both of you rather than just provide obstacles.

Other changes:
I split anomalies out into their own dmi file, seems to be all the rage lately.
I moved the anomaly placing code into a datum instead of the event because I wanted to reuse it but if you have a better idea about where I could have put it let me know.
This also fixes a bug where the material spreader component wasn't working when I applied plasma materials to something, the extra whitespace was parsing as another argument for some reason and meant it would runtime.
Supermatter delamination was still pointing to Delimber anomalies instead of Bioscrambler.

* Dimensional Anomaly

* Fixes the upstream merge skew

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [justdie386/Milky-terry](https://github.com/justdie386/Milky-terry)@[3931e0bbda...](https://github.com/justdie386/Milky-terry/commit/3931e0bbdacde425a78f718fa2513a5db35556c6)
#### Wednesday 2022-09-07 02:24:29 by justdie386

Fuck yeah

Im done with that shit, but like use it if you want, join the discordia server if ya got questions on how to adapt it to your server, and have a g'day :D

---
## [ThakaRashard/BUBBLEGUMPOP_HUMA](https://github.com/ThakaRashard/BUBBLEGUMPOP_HUMA)@[23bb669b90...](https://github.com/ThakaRashard/BUBBLEGUMPOP_HUMA/commit/23bb669b9056335bc6898008d7f9661a45536ce4)
#### Wednesday 2022-09-07 02:27:15 by ThakaRashard

[A girl is involuntarily engaged to a boy who turns female when hit with cold water and male when hit with hot.](https://www.imdb.com/title/tt0096686/)

---
## [suassuna/dwm](https://github.com/suassuna/dwm)@[67d76bdc68...](https://github.com/suassuna/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-09-07 02:56:42 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [stinodego/black](https://github.com/stinodego/black)@[0019261abc...](https://github.com/stinodego/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Wednesday 2022-09-07 05:06:03 by Richard Si

Update stable branch after publishing to PyPI (#3223)

We've decided to a) convert stable back into a branch and b) to update
it immediately as part of the release process. We may as well automate
it. And about going back to a branch ...

Git tags are not the right tool, at all[^1]. They come with the
expectation that they will never change. Things will not work as
expected if they do change, doubly so if they change regularly. Once
you pull stable from the remote and it's copied in your local
repository, no matter how many times you run git pull you'll never see
it get updated automatically. Your only recourse is to delete the tag
via `git tag -d stable` before pulling.

This gets annoying really quickly since stable is supposed to be the
solution for folks "who want to move along as Black developers deem
the newest version reliable."[^2] See this comment for how this impacts
users using our Vim plugin[^3]. It also affects us developers[^4]. If
you have stable locally, once we cut a new release and update the stable
tag, a simple `git pull` / `git fetch` will not pull down the updated
stable tag. Unless you remember to delete stable before pulling, stable
will become stale and useless.

You can argue this is a good thing ("people should explicitly opt into
updating stable"), but IMO it does not match user expectations nor
developer expectations[^5]. Especially since not all our integrations
that use stable are bound by this security measure, for example our
GitHub Action (since it does a clean fetch of the repository every time
it's used). I believe consistency would be good here.

Finally, ever since we switched to a tag, we've been facing issues with
ReadTheDocs not picking up updates to stable unless we force a rebuild.
The initial rebuild on the stable update just pulls the commit the tag
previously pointed to. I'm not sure if switching back to a branch will
fix this, but I'd wager it will.

[^1]: https://git-scm.com/docs/git-tag#_on_re_tagging

[^2]: https://black.readthedocs.io/en/stable/contributing/release_process.html#moving-the-stable-tag

[^3]: https://github.com/psf/black/issues/2503#issuecomment-1196357379

[^4]: In fairness, most folks working on Black probably don't use the
      `stable` ref anyway, especially us maintainers who'd know what is
      the latest version by heart, but it'd still be nice to make it
      usable for local dev though.

[^5]: Also what benefit does a `stable` ref have over explicit version
      tags like `22.6.0`? If you're going to opt into some odd pin
      mechanism, might as well use explicit version tags for clarity
      and consistency.

---
## [fredericdalleau/linuxkit](https://github.com/fredericdalleau/linuxkit)@[860934d5d9...](https://github.com/fredericdalleau/linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Wednesday 2022-09-07 06:51:45 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [Dylan-DPC/rust](https://github.com/Dylan-DPC/rust)@[eb3b53f316...](https://github.com/Dylan-DPC/rust/commit/eb3b53f316ca5927c417c52c205021ba6b56bea1)
#### Wednesday 2022-09-07 07:39:35 by Dylan DPC

Rollup merge of #101455 - thomcc:why-is-this-here, r=jyn514

Avoid UB in the Windows filesystem code in... bootstrap?

This basically a subset of the changes from https://github.com/rust-lang/rust/pull/101171. I didn't think to look in src/bootstrap for more windows filesystem API usage, which was apparently a mistake on my part. It's kinda goofy that stuff like this is in here, but what are you gonna do, computers are awful.

I also added `winbase` to the `winapi` dep -- I tested this in a tmp crate but needed to add this to your Cargo.toml -- you `use winapi::stuff::winbase` in this function, but are relying on something else turning on that feature.

---
## [alexraputa/laminas-modulemanager](https://github.com/alexraputa/laminas-modulemanager)@[6c82a43952...](https://github.com/alexraputa/laminas-modulemanager/commit/6c82a43952fb8f4a3b949a7d572784c01c709ece)
#### Wednesday 2022-09-07 09:34:41 by Michał Bundyra

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
## [radetsky/themis](https://github.com/radetsky/themis)@[9a6b4ed019...](https://github.com/radetsky/themis/commit/9a6b4ed019464e5f2e6258482bcb7bcf42a9fa09)
#### Wednesday 2022-09-07 09:53:53 by Alexei Lozovsky

Update GoThemis and WasmThemis examples to 0.14.0 (#893)

* go: Update examples to GoThemis 0.14.0

* go: Update tools to GoThemis 0.14.0

* wasm: Update examples to WasmThemis 0.14.0

* wasm: Upgrade "webpack-dev-server" 3 => 4

dev-only dependency of the example. Bumping the version to get rid
of "npm audit" warnings. Of course there are breaking changes...

* wasm: Throw away more polyfills

Newer versions of webpack-dev-server start showing all the warnings from
webpack right in your face. Let's fix them then...

WasmThemis includes code paths for Node.js support. They are not used
since browsers are not Node.js, but try explaining that to webpack.
So we do that but telling it to shut up and ignore all those built-in
Node.js modules.

* wasm: Suppress more warnings about "ws" dependency

WebSockets? Why?..

Anyway. I've found this workaround that gets webpack to shut up.

* wasm: Disable subresource integrity in dev builds

webpack-subresource-integrity used by the SRIPlugin *really* does not
like being used from a development web server. It prints warnings and
webpack-dev-server throws a giant full-screen overlay right in your
face when doing "npm run start". Okay, FINE, I'll disable you...

* wasm: Check package-lock.json into the repo

WasmThemis and JsThemis already do this, let the example have it
in the repo too. GitHub will scan it for vulnerabilities for us.

* go: Update pkg.go.dev badge

Uh... I don't remember why this is done manually. I guess because
the proper badges [1] don't show neither package name, nor version?

[1]: https://pkg.go.dev/badge/?path=https%3A%2F%2Fpkg.go.dev%2Fgithub.com%2Fcossacklabs%2Fthemis%2Fgothemis

---
## [ProjectIgnis/CardScripts](https://github.com/ProjectIgnis/CardScripts)@[cc8f36cb12...](https://github.com/ProjectIgnis/CardScripts/commit/cc8f36cb12c9f1ca1b064c5294a1e09651992bca)
#### Wednesday 2022-09-07 10:45:58 by pyrQ

Various script fixes/updates

Official:
- Armed Dragon Blitz: General script polish.
- Blackwing - Chinook the Snowstrike: The Quick version of its effect should be usable in the Damage Step.
- Blackwing - Twin Shadow: Added a hint timing for the opponent's End Phase.
- Chorus in the Sky: Small typo in the code regarding target redirection effects.
- Cipher Spectrum: Shouldn't activate if the Xyz Monster was sent to the GY by an effect but wasn't destroyed.
- Earth Golem @Ignister: Small typo in the code regarding target redirection effects.
- Ebon High Magician: Match the strings used in its script with the ones in its database entry.
- Evil★Twin Ki-sikil: Should check that you control an appropriate monster only when the effect would be activated.
- Evil★Twin Lil-la: Should check that you control an appropriate monster only when the effect would be activated.
- Fire Formation - Yoko: Shouldn't be considered an effect that destroys if the player doesn't target anything when activating it + general script polish.
- Flower Bloom of the Vernusylph: The last effect now uses the correct string.
- Gishki Chain: Adding a card to the hand and re-arranging the order of the rest shouldn't happen at the same time.
- Jurrac Meteor: If the effect doesn't successfully destroy anything then the player shouldn't be able to Special Summon a Tuner.
- Legendary Six Samurai - Enishi: Should also check the condition on resolution + general script polish.
- Live☆Twin Lil-la: Should check that you control no other monsters only when the effect would be activated.
- Live☆Twin Ki-sikil: Should check that you control no other monsters only when the effect would be activated.
- Lovely Labrynth of the Silver Castle: Should only protect Normal Trap Card activations, not Normal Traps' effects' activations.
- Shock Troops of the Ice Barrier: Shouldn't destroy the target if it's not a WATER monster anymore when this card's effect resolves.
- Star-Crossed Meeting: Should be able to negate its GY effect with something like "Solemn Warning".
- Virtual World Hime - Nyannyan: The Special Summoning restriction should be applied even if it's not Special Summoned successfully + general script polish.
- Wrath of Neos: Shuffling and destroying should be simultaneous + general script polish.

Unofficial/Rush:
- Monster Reborn (Rush): Should use the value indicating that it's a summon with "Monster Reborn".
- Speed Spell - Monster Reborn: Should use the value indicating that it's a summon with "Monster Reborn".

---
## [erfanoabdi/android_kernel_gigaset_mt6768](https://github.com/erfanoabdi/android_kernel_gigaset_mt6768)@[ea51dd856a...](https://github.com/erfanoabdi/android_kernel_gigaset_mt6768/commit/ea51dd856a87985ba4a17f3283af364c7e2e4bd6)
#### Wednesday 2022-09-07 11:05:15 by Peter Zijlstra

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

---
## [mkowalski/assisted-installer-agent](https://github.com/mkowalski/assisted-installer-agent)@[15557354b2...](https://github.com/mkowalski/assisted-installer-agent/commit/15557354b2e2d92afa46d36004153315c30c1d16)
#### Wednesday 2022-09-07 13:03:45 by Omer Tuchfeld

MGMT-10973: Copy coredns & keepalived static pod manifests in day-2 connectivity-check ignition (#388)

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

However, that ignition file is incomplete as currently we only include
necessary information in it (because that file is very big). The parts
of that file that we care in this case are currently missing, so we have
to modify the agent to include those files.

This commit does that. A follow-up commit will be done on the service to
actually check for the presence of these files in this ignition to make
the decision of whether the cluster is managed or not, and in turn turn
on the necessary validations if not.

# Ignition Files

The ignition files we currently include are:

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
## [jonreeve/NotifyXso](https://github.com/jonreeve/NotifyXso)@[9632fb57bd...](https://github.com/jonreeve/NotifyXso/commit/9632fb57bd9069e039c65502748f2902ddfeb64a)
#### Wednesday 2022-09-07 13:54:19 by Jon Reeve

Use ViewState instead of ConfigurationVO

Now that the view layer has no implicit state, need to explicitly retain
the state somewhere. Where we could previously use a slightly more
detail-agnostic ViewState and keep rendering detail in the view layer, doing
so now would require re-introducing local state in the Composables and
comparing input to it, knowing which to keep. Yuk. So instead the ViewState
has to become very tightly bound to the UI impl. details, to actually keep
their state, such as text entry for a decimal number. That kinda sucks.
I'm probably just looking at it wrong, fighting it and doing it the wrong
way, based on previous experience. I'm sure different seams exist here
instead like with React. Maybe should emit the Compose UI straight out of
the VM or something. Don't know yet.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[4c8cfb57aa...](https://github.com/pytorch/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Wednesday 2022-09-07 14:23:41 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [v4lkyr/whyred](https://github.com/v4lkyr/whyred)@[913fff3d01...](https://github.com/v4lkyr/whyred/commit/913fff3d0136076a7893e2bad15fc2ea21bb86b9)
#### Wednesday 2022-09-07 14:45:58 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>
Signed-off-by: v4lkyr <valkyr23@gmail.com>

---
## [newstools/2022-the-times](https://github.com/newstools/2022-the-times)@[175d14b83b...](https://github.com/newstools/2022-the-times/commit/175d14b83b352587bb90d892e906e00122d36c16)
#### Wednesday 2022-09-07 14:54:11 by Billy Einkamerer

Created Text For URL [www.timeslive.co.za/news/south-africa/2022-09-07-man-who-killed-girlfriend-and-stabbed-her-suspected-lover-gets-life-sentence/]

---
## [kovdb75/postgres](https://github.com/kovdb75/postgres)@[7fed801135...](https://github.com/kovdb75/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Wednesday 2022-09-07 16:02:39 by Tom Lane

Clean up inconsistent use of fflush().

More than twenty years ago (79fcde48b), we hacked the postmaster
to avoid a core-dump on systems that didn't support fflush(NULL).
We've mostly, though not completely, hewed to that rule ever since.
But such systems are surely gone in the wild, so in the spirit of
cleaning out no-longer-needed portability hacks let's get rid of
multiple per-file fflush() calls in favor of using fflush(NULL).

Also, we were fairly inconsistent about whether to fflush() before
popen() and system() calls.  While we've received no bug reports
about that, it seems likely that at least some of these call sites
are at risk of odd behavior, such as error messages appearing in
an unexpected order.  Rather than expend a lot of brain cells
figuring out which places are at hazard, let's just establish a
uniform coding rule that we should fflush(NULL) before these calls.
A no-op fflush() is surely of trivial cost compared to launching
a sub-process via a shell; while if it's not a no-op then we likely
need it.

Discussion: https://postgr.es/m/2923412.1661722825@sss.pgh.pa.us

---
## [Sudip-Shrestha-2051219/allOfAutomation](https://github.com/Sudip-Shrestha-2051219/allOfAutomation)@[cb8ec06e92...](https://github.com/Sudip-Shrestha-2051219/allOfAutomation/commit/cb8ec06e929f43ba6f6a153ac3aafbed97111ed4)
#### Wednesday 2022-09-07 16:24:37 by Sudip-Shrestha-2051219

strip() using regex.

I have made the strip function using regex module. This is one of the very few programs where I've sweated my balls off. Days and days of anger, frustration, fear, wastefulness and all emotions mixed with this small piece of code. Finally I completed the code today and I just can't describe the joy that I feel right now. Details of regex(regular expression) are to follow soon.

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[d454952b07...](https://github.com/newstools/2022-express/commit/d454952b076307fd3bf8e619a6db4d64039dc4cd)
#### Wednesday 2022-09-07 17:07:00 by Billy Einkamerer

Created Text For URL [www.express.co.uk/entertainment/music/1666031/Freddie-Mercury-does-girlfriend-Mary-own-Queen-star-house-boyfriend-Jim-Hutton]

---
## [daviditen/chapel](https://github.com/daviditen/chapel)@[1b5d5a5140...](https://github.com/daviditen/chapel/commit/1b5d5a5140309b41f569904e73fb9974afcae5b5)
#### Wednesday 2022-09-07 17:30:49 by Brad Chamberlain

Merge pull request #20616 from bradcray/range-docs-tidying

Tidy up range docs

[reviewed by @bmcdonald3 — thanks!]

While reviewing my the range docs after my changes to its behavior
last night, I found some pre-existing bugs that needed fixing,
that the operators were now being generated by chpldoc, and some
other opportunities for cleanup.  Summarizing, they were:

* the expected output from the alignedLow/High docs wasn't printing
  (and hadn't been in previous releases either)

* the signatures on the param/type queries in the spec used illegal
  syntax (though now they fall prey to the poor spacing when
  rendered by Sphinx on Chrome.

* I squashed the chpldocumentation of the operators because they're
  already described in the text of the spec, which does a better job
  of it.  That said, going forward, I think we'd like to find a way to
  integrate operator signatures into these sections of the spec so
  that people can see what the overloads are.  Not today's task though.

* I tried to clarify some wordings and descriptions.

* removed the "more descriptive" clause that I'd applied to the
  alignedLow/High queries yesterday because it sounded like more of
  a value judgement or preference than I'd intended.

* I more uniformly set ``true`` and ``false`` off using code
  formatting.

* I more uniformly started entries with "Returns" rather than "Return"

* I more uniformly ended descriptions with periods

---
## [Crosse/dotfiles](https://github.com/Crosse/dotfiles)@[b5e0a008cc...](https://github.com/Crosse/dotfiles/commit/b5e0a008cc14b8464d867a63ff4a887e24945b61)
#### Wednesday 2022-09-07 19:28:36 by Seth Wright

GET RID OF gpg-agent, FINALLY

...I mean, I hope so. I'm going to experiment with a two-tier x.509 CA using
Yubikeys which, on the surface, is pretty stupid considering I'M JUST ONE
PERSON, but that's never stopped me before. This is what we're going to:

- Yubikey for root CA
- Yubikey for intermediate CA
- Two Yubikeys with unique x.509 certs for the same
  principal (seth@crosse.org): one key (prism) for work, one (geode) for
  personal
- Use ssh-agent's built-in ability to handle PKCS#11 providers to talk to
  the keys
- Distribute the intermediate CA as an SSH "certificate authority" in
- ~/.ssh/authorized_keys using Salt so that we can log in to our own stuff
  with any key signed by the CA
- Use ssh keys for git signing (done in a previous commit)

Doing all of the above I think (I _think) removes the need to deal with GPG
at all. I can use ssh-agent to store keys instead of gpg-agent, and with Git
using SSH keys instead of GPG keys for signing, I don't need GPG at
all. (Right? Right?)

This will necessitate a change to standard operating procedure, such that I
need to remember to run `ssh-agent -D ; ssh-agent -e $LIBYKCS11 ; ssh-agent
-s $LIBYKCS11` to load the key(s) into the agent. I didn't have to do
anything previously to get keys into gpg-agent because it "just
worked"...with opensc and whatever else it needed that I've forgotten about.

---
## [ijadams/poor-boys-bar](https://github.com/ijadams/poor-boys-bar)@[7b7f11a9e3...](https://github.com/ijadams/poor-boys-bar/commit/7b7f11a9e3deb7ee15e5dcc00c342fa313ca77f7)
#### Wednesday 2022-09-07 19:56:14 by ijadams503@gmail.com

Update from Forestry.io
ijadams503@gmail.com deleted content/blog-posts/eyehategod-goatwhore-sick-thoughts-shitload.md

---
## [scrtlabs/SecretNetwork](https://github.com/scrtlabs/SecretNetwork)@[a8ffddebfe...](https://github.com/scrtlabs/SecretNetwork/commit/a8ffddebfe95cb7bad51eb0ecdcdcd7108319d1c)
#### Wednesday 2022-09-07 20:01:58 by Cashmaney

Setting up gitpod username with proper permissions on github

Also, fuck you wavy lines logo

---
## [eliorerz/assisted-service](https://github.com/eliorerz/assisted-service)@[564650feca...](https://github.com/eliorerz/assisted-service/commit/564650feca372064314282d98d6fd9c6ee69bd2c)
#### Wednesday 2022-09-07 20:20:29 by Omer Tuchfeld

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
## [romikumar7/free-programming-books](https://github.com/romikumar7/free-programming-books)@[97016edd67...](https://github.com/romikumar7/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Wednesday 2022-09-07 20:29:35 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [USNA-CyberScience/CAE-CD-Application-](https://github.com/USNA-CyberScience/CAE-CD-Application-)@[234c0931f0...](https://github.com/USNA-CyberScience/CAE-CD-Application-/commit/234c0931f07d46f0b1f422becae0ebc27f88e40f)
#### Wednesday 2022-09-07 21:16:36 by Jack Murray

USNA Cyber Security Team Exercises: August 2018 - November 2019

NCX Winners: 2018

CDX Winners: 2017, 2015, 2010, 2005

The Cyber Security Team is the Naval Academy's competitive hacking and cyber-security team for Midshipmen interested in learning about computer network operations. Founded in the early 2000's to compete in the NSA's Cyber Defense Exercise, the team has expanded to compete in Jeopardy style Capture the Flags (CTFs), Attack/Defense Exercises, policy competitions, and other various events.

The team meets every day during the sports period in classes split by experience level. This allows the team to teach new members basic hacking skills, while pushing the more experienced members of the team to continue to advance their skills. Classes range from network attack and defense, binary exploitation, and web exploitation to forensics and incident response, cryptography, and hacker culture. The team's hands-on approach is a great supplement for any student studying a technically focused cyber-related major across the Academy. It also exposes our students to skills and operational knowledge that is not taught anywhere else on the Yard.

Over the past year, the United States Naval Academy (USNA) has participated in numerous cyber competitions. Below is a list of cyber competitions participated in and achievements received.

2019

January 2019- Shmoocon Hacker Conference in Washington D.C.

February 2019- The Cyber-Insecurity: How to Improve America’s Digital Defenses

March 2019- RSA, 2 midshipmen presented research to peers and experts; received feedback from the Cyber industry's most respected experts.

March 2019- SANS Institute: 2 students took a course on Windows Forensic Analysis; 1 student took a course on Advanced Network Forensics; 5 students took the flagship course on Hacker Tools, Techniques and exploits; and 2 more students took courses in Management and Policy

March 2019- Atlantic Council’s Cyber Policy Competition

April 2019- NSA Cyber Defense Exercise, Interservice Academy Competition at USAFA; 2nd place (1st place in cyber policy)

May 2019- Europe; Language Proficiency, Regional Expertise, Cultural Awareness. Students attended the 11th annual NATO International Conference, focused on current and critical issues in cyber by bringing together the key decision-makers and cyber experts representing government, military, academia and the private sector. In addition midshipmen, attended the CONFidence Conference in Poland, where they explored hands on coding and hacking techniques.

June 2019- UK Language Proficiency, Regional Expertise, Cultural Awareness. Nine midshipmen immersed themselves in centuries of history and culture while also meeting a number of distinguished professionals who informed them about UK and European views of cybersecurity policy.

July 2019- Asia Language Proficiency, Regional Expertise, Cultural Awareness. Eight midshipmen visited Japan, South Korea and Australia and participated in activities and meetings that focused on that country’s efforts in the cyber domain, its relationship with the US, and its cultural identity and history.

July 2019- Israel Language Proficiency, Regional Expertise, Cultural Awareness. Midshipmen attended a week long seminar class in Cyber Operations at Tel Aviv University and then the "Cyber Week 2019" Conference in Tel Aviv, Israel during the second week of the LREC. Continuing the cyber education and exposure with Israeli cyber counterparts from military and academia.

August 2019- DEFCON: attended this world-renowned conference where we learned about social engineering, policy and planning for cyber operations, reverse engineering concepts, and other insightful information security topics

September 2019- Hack the Machine: identified vulnerabilities in shipboard systems to include navigation, propulsion, control area networks, local area networks, and 3-D printers. Midshipman Heckel was recognized as identifying previously unknown vulnerabilities in 3-D printers which caused structural integrity issues.

October 2019 - picoCTF - Introductory skillbuilder public cyber security competition (online).

October 2019- AvengerCon

Two 1/C MIDN initiated and led a half-day policy simulation exercise that included 14 USNA MIDN, 8 students from American University, 3 students from James Madison University, and 2 students from UMBC. We were able to recruit several individuals from industry, government, and academia to serve as mentors to the various groups represented in the policy simulation (e.g. NSA, USCYBERCOM, Department of Justice, Department of State, State of New York, etc.)

Additionally, around 20 MIDN attended various presentations and workshops covering a number of technical topics during the two-day conference

October 2019- FireEye Defense Summit learning what security practitioners need to know to mitigate, detect and respond to cyber attacks.

November 2019- CYCON U.S. Conference

November 2019- Cyber Security Awareness Week Policy Competition, second and third place nationwide (among undergraduate, graduate, and law school competitors)

December 2019 - Codebreaker competition by NSA, scored evolution for NCX

December 2019 - ITsec, remotely competed to test out the new PCTE

2018

November 2018 - Cyber Security Awareness Week Policy Competition, second place nationwide

November 2018: SWAT-C-Electronic Warfare competition against Army at Quantico, VA

November 2018- Cyber Security Awareness Week Policy Competition- 2nd place-Midshipmen were encouraged to think critically about major policy issues affecting society and the impact on the cyber industry by presenting their ideas to leaders within the field.

December 2018- All-Army CyberStakes

---
## [derfelot/android_kernel_sony_msm8998](https://github.com/derfelot/android_kernel_sony_msm8998)@[76323f96b0...](https://github.com/derfelot/android_kernel_sony_msm8998/commit/76323f96b03c58c2e5d6b951c9f4b97cc034bf8b)
#### Wednesday 2022-09-07 22:14:51 by Christian Brauner

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
Signed-off-by: electimon <electimon@gmail.com>

---
## [projects-nexus/nexus_kernel_xiaomi_sm8250](https://github.com/projects-nexus/nexus_kernel_xiaomi_sm8250)@[dd063b4757...](https://github.com/projects-nexus/nexus_kernel_xiaomi_sm8250/commit/dd063b47575584a59e00bfb9f6cb38d4d3e65236)
#### Wednesday 2022-09-07 23:09:41 by George Spelvin

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

