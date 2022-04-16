## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-15](docs/good-messages/2022/2022-04-15.md)


1,716,549 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,716,549 were push events containing 2,677,993 commit messages that amount to 187,939,256 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [RealWinterFrost/Skyrat-tg](https://github.com/RealWinterFrost/Skyrat-tg)@[20d3361f6b...](https://github.com/RealWinterFrost/Skyrat-tg/commit/20d3361f6b9e81e83b1fe2b69a57713f5a81cc2e)
#### Friday 2022-04-15 00:51:36 by SkyratBot

[MIRROR] makes podpeople spec_life call parent [MDB IGNORE] (#12106)

* makes podpeople call parent (#65362)

About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

* makes podpeople spec_life call parent

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[b1a793f840...](https://github.com/Zytolg/tgstation/commit/b1a793f840d90131f88eabc0450e2b2b2157123e)
#### Friday 2022-04-15 01:18:21 by Tim

Refactor and improve antimagic to be more robust (#64124)

This refactors the antimagic component to use and have bitflags, documentation, defines, code comments, named arguments, and renames variable names for clarity. 

- /obj/effect/proc_holder/spell/aoe_turf/conjure/creature/cult is not used anywhere and has been removed
- /obj/effect/proc_holder/spell/targeted/turf_teleport/blink/cult is not used anywhere and has been removed

- New sound effects are played when magic is blocked. Depending on the type of magic being used it will be either:

- Equipping antimagic now properly updates the magic buttons
- Any magic being blocked or restricting casting now displays a message
- MAGIC_RESISTANCE_MIND now properly blocks telepathy effects
- Removes blood splatter when fireball is blocked
- Magic projectiles for staff of locker no longer spawn lockers when blocked by antimagic
- Fire breath is no longer blocked by antimagic
- Spellcards are now blocked by antimagic

Any antimagic on a mob blocks that magic type from being casted. (certain spells such as mime abilities completely ignore antimagic)

- Foilhats prevent someone from casting mind magic (telepathy, mindswap, etc.)
- Bibles, ritual Totems, nullrods, holymelons, and TRAIT_HOLY prevent someone from casting unholy magic (cult spells, etc.)
- Nullrods, ritual totem, and holymelons prevent someone from casting wizard magic (fireball, magic missile, etc.)
- Immorality talismans, berserker suits, and TRAIT_ANTIMAGIC prevents all types of magic (except stuff like mime abilities)
- Touch of Madness and Mindswap is now blocked with MAGIC_RESISTANCE and MAGIC_RESISTANCE_MIND
- Voice of god is now blocked with MAGIC_RESISTANCE_HOLY and MAGIC_RESISTANCE_MIND

---
## [carenas/git](https://github.com/carenas/git)@[5cb28270a1...](https://github.com/carenas/git/commit/5cb28270a1ff94a0a23e67b479bbbec3bc993518)
#### Friday 2022-04-15 02:04:37 by Ævar Arnfjörð Bjarmason

pack-objects: lazily set up "struct rev_info", don't leak

In the preceding [1] (pack-objects: move revs out of
get_object_list(), 2022-03-22) the "repo_init_revisions()" was moved
to cmd_pack_objects() so that it unconditionally took place for all
invocations of "git pack-objects".

We'd thus start leaking memory, which is easily reproduced in
e.g. git.git by feeding e83c5163316 (Initial revision of "git", the
information manager from hell, 2005-04-07) to "git pack-objects";

    $ echo e83c5163316f89bfbde7d9ab23ca2e25604af290 | ./git pack-objects initial
    [...]
	==19130==ERROR: LeakSanitizer: detected memory leaks

	Direct leak of 7120 byte(s) in 1 object(s) allocated from:
	    #0 0x455308 in __interceptor_malloc (/home/avar/g/git/git+0x455308)
	    #1 0x75b399 in do_xmalloc /home/avar/g/git/wrapper.c:41:8
	    #2 0x75b356 in xmalloc /home/avar/g/git/wrapper.c:62:9
	    #3 0x5d7609 in prep_parse_options /home/avar/g/git/diff.c:5647:2
	    #4 0x5d415a in repo_diff_setup /home/avar/g/git/diff.c:4621:2
	    #5 0x6dffbb in repo_init_revisions /home/avar/g/git/revision.c:1853:2
	    #6 0x4f599d in cmd_pack_objects /home/avar/g/git/builtin/pack-objects.c:3980:2
	    #7 0x4592ca in run_builtin /home/avar/g/git/git.c:465:11
	    #8 0x457d81 in handle_builtin /home/avar/g/git/git.c:718:3
	    #9 0x458ca5 in run_argv /home/avar/g/git/git.c:785:4
	    #10 0x457b40 in cmd_main /home/avar/g/git/git.c:916:19
	    #11 0x562259 in main /home/avar/g/git/common-main.c:56:11
	    #12 0x7fce792ac7ec in __libc_start_main csu/../csu/libc-start.c:332:16
	    #13 0x4300f9 in _start (/home/avar/g/git/git+0x4300f9)

	SUMMARY: LeakSanitizer: 7120 byte(s) leaked in 1 allocation(s).
	Aborted

Narrowly fixing that commit would have been easy, just add call
repo_init_revisions() right before get_object_list(), which is
effectively what was done before that commit.

But an unstated constraint when setting it up early is that it was
needed for the subsequent [2] (pack-objects: parse --filter directly
into revs.filter, 2022-03-22), i.e. we might have a --filter
command-line option, and need to either have the "struct rev_info"
setup when we encounter that option, or later.

Let's just change the control flow so that we'll instead set up the
"struct rev_info" only when we need it. Doing so leads to a bit more
verbosity, but it's a lot clearer what we're doing and why.

An earlier version of this commit[3] went behind
opt_parse_list_objects_filter()'s back by faking up a "struct option"
before calling it. Let's avoid that and instead create a blessed API
for this pattern.

We could furthermore combine the two get_object_list() invocations
here by having repo_init_revisions() invoked on &pfd.revs, but I think
clearly separating the two makes the flow clearer. Likewise
redundantly but explicitly (i.e. redundant v.s. a "{ 0 }") "0" to
"have_revs" early in cmd_pack_objects().

While we're at it add parentheses around the arguments to the OPT_*
macros in in list-objects-filter-options.h, as we need to change those
lines anyway. It doesn't matter in this case, but is good general
practice.

1. https://lore.kernel.org/git/619b757d98465dbc4995bdc11a5282fbfcbd3daa.1647970119.git.gitgitgadget@gmail.com
2. https://lore.kernel.org/git/97de926904988b89b5663bd4c59c011a1723a8f5.1647970119.git.gitgitgadget@gmail.com
3. https://lore.kernel.org/git/patch-1.1-193534b0f07-20220325T121715Z-avarab@gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [PrFly69/Gondola](https://github.com/PrFly69/Gondola)@[46b9d01e18...](https://github.com/PrFly69/Gondola/commit/46b9d01e18d70f7b4be9ae65ed0f827651cf5ee3)
#### Friday 2022-04-15 02:45:11 by PrFly69

i love randomly fixing and doing a lot of shit in one day its really funny i think GOD i cant wait to finally go to therapy one day cause lordy lord up above knows i need it

---
## [exordium-vic3/exordium-vic3.github.io](https://github.com/exordium-vic3/exordium-vic3.github.io)@[621e4cb2a6...](https://github.com/exordium-vic3/exordium-vic3.github.io/commit/621e4cb2a63ae9093538b1e04bfa4a7fe4a2a847)
#### Friday 2022-04-15 03:16:46 by exordium-vic3

fucking hate crackers i swear to god BITCHHHHHHHHH CRACKKKKKKA

---
## [VladinXXV/tgstation](https://github.com/VladinXXV/tgstation)@[123f57cc70...](https://github.com/VladinXXV/tgstation/commit/123f57cc70697c7964bbf10f9927e5225a4451ff)
#### Friday 2022-04-15 03:17:56 by VladinXXV

processor now inherits chems

holy shit guys i did it it works how did i do this i dont understand code at all oh my god this was so painful to do ahahahahahahahahahahahaha FUCK CARROT FRIES THIS IS ALL THEIR FAULT.

---
## [antonyggvzvmnxxcx/git](https://github.com/antonyggvzvmnxxcx/git)@[96bfb2d8ce...](https://github.com/antonyggvzvmnxxcx/git/commit/96bfb2d8ce221d31b3da08a49a455e316dbef7fb)
#### Friday 2022-04-15 03:50:34 by Jeff King

run-command: unify signal and regular logic for wait_or_whine()

Since 507d7804c0 (pager: don't use unsafe functions in signal handlers,
2015-09-04), we have a separate code path in wait_or_whine() for the
case that we're in a signal handler. But that code path misses some of
the cases handled by the main logic.

This was improved in be8fc53e36 (pager: properly log pager exit code
when signalled, 2021-02-02), but that covered only case: actually
returning the correct error code. But there are some other cases:

  - if waitpid() returns failure, we wouldn't notice and would look at
    uninitialized garbage in the status variable; it's not clear if it's
    possible to trigger this or not

  - if the process exited by signal, then we would still report "-1"
    rather than the correct signal code

This latter case even had a test added in be8fc53e36, but it doesn't
work reliably. It sets the pager command to:

  >pager-used; test-tool sigchain

The latter command will die by signal, but because there are multiple
commands, there will be a shell in between. And it's the shell whose
waitpid() call will see the signal death, and it will then exit with
code 143, which is what Git will see.

To make matters even more confusing, some shells (such as bash) will
realize that there's nothing for the shell to do after test-tool
finishes, and will turn it into an exec. So the test was only checking
what it thought when /bin/sh points to a shell like bash (we're relying
on the shell used internally by Git to spawn sub-commands here, so even
running the test under bash would not be enough).

This patch adjusts the tests to explicitly call "exec" in the pager
command, which produces a consistent outcome regardless of shell. Note
that without the code change in this patch it _should_ fail reliably,
but doesn't. That test, like its siblings, tries to trigger SIGPIPE in
the git-log process writing to the pager, but only do so racily. That
will be fixed in a follow-on patch.

For the code change here, we have two options:

  - we can teach the in_signal code to handle WIFSIGNALED()

  - we can stop returning early when in_signal is set, and instead
    annotate individual calls that we need to skip in this case

The former is a simpler patch, but means we're essentially duplicating
all of the logic. So instead I went with the latter. The result is a
bigger patch, and we do run the risk of new code being added but
forgetting to handle in_signal. But in the long run it seems more
maintainable.

I've skipped any non-trivial calls for the in_signal case, like calling
error(). We'll also skip the call to clear_child_for_cleanup(), as we
were before. This is arguably the wrong thing to do, since we wouldn't
want to try to clean it up again. But:

  - we can't call it as-is, because it calls free(), which we must avoid
    in a signal handler (we'd have to pass in_signal so it can skip the
    free() call)

  - we'll only go through the list of children to clean once, since our
    cleanup_children_on_signal() handler pops itself after running (and
    then re-raises, so eventually we'd just exit). So this cleanup only
    matters if a process is on the cleanup list _and_ it has a separate
    handler to clean itself up. Which is questionable in the first place
    (and AFAIK we do not do).

  - double-cleanup isn't actually that bad anyway. waitpid() will just
    return an error, which we won't even report because of in_signal.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [theselfish/Skyrat-tg](https://github.com/theselfish/Skyrat-tg)@[d96e7b7e27...](https://github.com/theselfish/Skyrat-tg/commit/d96e7b7e278dd0226a4de8d9463edda37af709f9)
#### Friday 2022-04-15 03:58:52 by SkyratBot

[MIRROR] Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things. [MDB IGNORE] (#11821)

* Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

* Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things.

Co-authored-by: Wallem <66052067+Wallemations@users.noreply.github.com>

---
## [PixelExperience-Devices/kernel_oneplus_sm8150](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150)@[c43d7ae3c6...](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150/commit/c43d7ae3c6b686876b152043fe007cbd103de74c)
#### Friday 2022-04-15 04:12:19 by alk3pInjection

drm: Handle dim for udfps

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
## [exordium-vic3/exordium-vic3.github.io](https://github.com/exordium-vic3/exordium-vic3.github.io)@[1694a29f37...](https://github.com/exordium-vic3/exordium-vic3.github.io/commit/1694a29f375ac706fb521b4119847f1ed3aa9675)
#### Friday 2022-04-15 04:41:49 by exordium-vic3

amerikkka fuck you god damnit i fucking hate all of you cracker ass

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[351afe260b...](https://github.com/ZephyrTFA/tgstation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Friday 2022-04-15 05:42:49 by san7890

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
## [JamesonSherman/FoundryCustom](https://github.com/JamesonSherman/FoundryCustom)@[1ec8084196...](https://github.com/JamesonSherman/FoundryCustom/commit/1ec808419614f13ee25bdab62980fc6eadb93482)
#### Friday 2022-04-15 06:12:59 by J.S

god why do i hate myself. fix the PHB items entries to have content.

---
## [rvsoni/LicenseFinder](https://github.com/rvsoni/LicenseFinder)@[c64fdda4bf...](https://github.com/rvsoni/LicenseFinder/commit/c64fdda4bf206f3b13986ac786a0bcd70cdea3a0)
#### Friday 2022-04-15 06:33:40 by Sven Dunemann

License: Change pretty name of WTFPL

should be short version WTFPL
instead of long version (Do What the Fuck You Want To Public License)

---
## [iyefrat/evil-tex](https://github.com/iyefrat/evil-tex)@[cf58bc5aea...](https://github.com/iyefrat/evil-tex/commit/cf58bc5aeab46fb1d08d22c799e2d0f714923bdb)
#### Friday 2022-04-15 08:49:02 by Dan Kessler

fix regex used in evil-tex-toggle-delim

Previously, it would match anything that had a slash followed optionally by a
balancing keyword followed optionally by l, which would mess up how it matched
things like \{ or \|

Currently, the regex it uses to decide if the delimiters are already
balanced (based just on the initial one) is:

"\\\\\\(?:left\\|big\\|bigg\\|Big\\|Bigg\\)?l?"

(note: all regexes here are taken from elisp so have extra backslashes for
string escapes)

The trouble is that this matches *anything* that has a slash, since everything
that follows is optional. For example, if you have math like $ \{ x \} $ and you
run evil-tex-toggle-delim, then this *will* match (just the literal backslash),
causing it to think that it is already size balanced, and then "toggling" will
just strip the backslash rather than prepending \left and \right.

This could be fixed by changing it to

"\\\\\\(?:\\(left\\|big\\|bigg\\|Big\\|Bigg\\)\\|l\\)"

This extra level of grouping means that it only matches if there is a literal
backslash followed by *either* one of the balancing keywords OR l. This way it
has to match something in the second part, and this will not match \{

However, I think that trailing (optional) l is perhaps a mistake. I assume it is
there to catch things like \langle, but this will then toggle \langle to
angle (which without the slash is not a macro). Moreover, \langle and
\rangle (or similarly \lvert and \rvert, etc) are paired delimiters but they do
not automatically resize (at least not for me), I instead need to do
\left\langle if I want that behavior. For that reason, I think the trailing l
should be cut, and the final regex is just

"\\\\\\(?:left\\|big\\|bigg\\|Big\\|Bigg\\)"

---
## [pipe-cd/pipecd](https://github.com/pipe-cd/pipecd)@[2480da0f07...](https://github.com/pipe-cd/pipecd/commit/2480da0f07a053c05d0491a6cf1ae2b367dc8605)
#### Friday 2022-04-15 10:14:44 by knanao

Fix the wrong way to cancel the context (#3540)

**What this PR does / why we need it**:
I'm sorry for my making a stupid but serious mistake with my carelessness.

**Which issue(s) this PR fixes**:

Fixes #

**Does this PR introduce a user-facing change?**:
<!--
If no, just write "NONE" in the release-note block below.
-->
```release-note
NONE
```

This PR was merged by Kapetanios.

---
## [Lustmored/EasyAdminBundle](https://github.com/Lustmored/EasyAdminBundle)@[f3a4b13382...](https://github.com/Lustmored/EasyAdminBundle/commit/f3a4b13382f6d96f85b0b1d8dfe329f40a39d32c)
#### Friday 2022-04-15 10:56:42 by Javier Eguiluz

minor #5139 Disable UX-Turbo (Lustmored)

This PR was merged into the 4.x branch.

Discussion
----------

Disable UX-Turbo

In all my projects with EasyAdmin I am sharing Stimulus controllers between EasyAdmin and frontend (I need them sometimes and it's just simpler). Since enabling Turbo on some projects I need to overwrite EasyAdmin layout just to disable it.

Currently EA is very unfriendly towards Turbo - there are JavaScripts in body, DOMContentLoaded listeners and so on. Refactoring everything to be turbo-compatible would be titanic effort with little benefit (it's not really needed in CRUD dashboards in my opinion), while adding this single attribute will make life easier for probably more consumers than just myself :)

Commits
-------

735b2397 Disable UX-Turbo

---
## [exordium-vic3/exordium-vic3.github.io](https://github.com/exordium-vic3/exordium-vic3.github.io)@[ce2b34f5da...](https://github.com/exordium-vic3/exordium-vic3.github.io/commit/ce2b34f5daced649fa11efa8ebfd5ad2015eaf17)
#### Friday 2022-04-15 11:09:46 by exordium-vic3

fuck you cracker i will fucking kill you piece of shit

---
## [DusanLesan/dwm](https://github.com/DusanLesan/dwm)@[67d76bdc68...](https://github.com/DusanLesan/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2022-04-15 11:12:55 by Chris Down

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
## [dimitris-athanasiou/elasticsearch](https://github.com/dimitris-athanasiou/elasticsearch)@[37ea6a8255...](https://github.com/dimitris-athanasiou/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Friday 2022-04-15 11:31:25 by Nik Everett

TSDB: Support GET and DELETE and doc versioning (#82633)

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "BsYQJjqS3TnsUlF3aDKnB34BAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/BsYQJjqS3TnsUlF3aDKnB34BAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing calculated from routing_path fields
* 8 bytes of hash from the dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the routing from the first four bytes. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. In our tsdb rally track this costs 8.75 bytes per
document. It's substantial, but not overwhelming.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. ~~We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.~~ Included in this PR based on review comments.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in Lucene stored fields for tsdb indices. Now
   that we're building it from the dimensions and the `@timestamp` we
   really don't *need* to store it. We could recalculate it when fetching
   documents. In the tsdb rall ytrick this'd save us 6 bytes per document
   at the cost of marginally slower fetches. Which is *fine*.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.
6. ~~If you specify an `_id` on the request right now we just overwrite
   it. We should send you an error.~~ Included in this PR after review comments.
7. We have to entirely disable the append-only optimization that allows
   Elasticsearch to skip looking up the ids in lucene. This *halves*
   indexing speed. It's substantial. We have to claw that optimization
   back *somehow*. Something like sliding bloom filters or relying on
   the increasing timestamps.
8. We parse the source from json when building the routing hash when
   parsing fields. We should just build it from to parsed field values.
   It looks like that'd improve indexing speed by about 20%.
9. Right now we write the `@timestamp` little endian. This is likely bad
   the prefix encoded inverted index. It'll prefer big endian. Might shrink it.
10. Improve error message on version conflict to include tsid and timestamp.
11. Improve error message when modifying dimensions or timestamp in update_by_query
12. Make it possible to modify dimension or timestamp in reindex.
13. Test TSDB's `_id` in `RecoverySourceHandlerTests.java` and `EngineTests.java`.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. I'm not excited by it. But it works and it's what
we're going with.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---
## [TheHorizonFivemLive/qb-core](https://github.com/TheHorizonFivemLive/qb-core)@[9d83a952c2...](https://github.com/TheHorizonFivemLive/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Friday 2022-04-15 13:08:20 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [Devcon902/qb-vehiclekeys](https://github.com/Devcon902/qb-vehiclekeys)@[757fdd0859...](https://github.com/Devcon902/qb-vehiclekeys/commit/757fdd0859013e45f9d432fa894f0ecb03d8bbf5)
#### Friday 2022-04-15 13:10:55 by ItsANoBrainer

Proper Refactor

Refactored the entire resource because the key system was not working.

No longer does a server callback 10 or so times a second, on top of other bad practices.

Tested pretty much everything with my devs, but there might be some weird issues we havnt found. Please lookover as I've been going crazy with the small tedious issues I've come across doing this.

Throwing this up to get feedback, and for people to use who want it.

Features:

- Keys are saved server side, and sent to each client when they are added or removed, as well as on character selection. This allows characters to leave and come back in the same server uptime session and still have the same keys
- Keys are only pulled from the server once on character load
- Giving keys has 3 types, /givekeys with an id will attempt to give keys you have to an id, not including an id will try to give it to the closest person, and if you're in a vehicle it will give to everyone
- Can only give keys to vehicles you have keys to
- Server event to force acquire keys to a plate for a person (for lockpicking/stealing/spawning, etc.)
- Can Carjack an NPC with a gun, has different percentages to work based on weapon (config)
- Take keys from dead npc drivers
- Can lockpick a car to unlock the doors
- Can hotwire a car if you're in the driver seat of the vehicle you dont have keys to to get keys
- Keeps the engine of a vehicle off if you dont have keys to it (allows other resources to attempt to toggle car engine without needing to interface if you have keys or not)
- Vehicle blacklist system for vehicles you dont want to be lockable (always unlocked)
- Police Alerts from lockpicking/hotwiring/carjacking
- Export to check if you have keys to a vehicle
- Locking/unlocking with hotkey
- Locking/unlocking and giving keys uses a custom GetVehicleInDirection you are facing for realism/accuracy
- Fully compatible with old resource. Has an event handler for 'vehiclekeys:client:SetOwner' in which it gives keys for that plate
- Some other shit I probably forgot

TODO:
- Add LOCALE support
- Stop peds from wanting to get back into the vehicle they just got carjacked out of as they're fleeing

---
## [Cenrus/Skyrat-tg](https://github.com/Cenrus/Skyrat-tg)@[8607ba8b7d...](https://github.com/Cenrus/Skyrat-tg/commit/8607ba8b7d98c52e81f23816a9224adf70559c25)
#### Friday 2022-04-15 14:08:08 by SkyratBot

[MIRROR] Adds a very rare sussy firelock [MDB IGNORE] (#12401)

* Adds a very rare sussy firelock (#65677)

On a VERY low chance (1/25000) a normal full tile firelock can instead be generated with a more suspicious appearance based on this recent quality shitpost.

Sussy firelocks are completely identical when open (save the desc) and thus are apt not to be noticed except during exciting times. It's a fully cosmetic joke that got me to log into github, and that's an accomplishment in itself. Probability rate fully negotiable, I've added a one in a million chance before after all.

* Adds a very rare sussy firelock

* ruins all the fun

people can get banned for doing the funny sus amogus so encouraging it in code, whilst it's beautiful and funny, eh someone is going to throw a fit.

Co-authored-by: Incoming5643 <incomingnumbers@gmail.com>
Co-authored-by: KathrinBailey <53862927+KathrinBailey@users.noreply.github.com>

---
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[e88efdab31...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/e88efdab3148409c9de084d0e84a3f799863dfde)
#### Friday 2022-04-15 14:12:45 by Peter Zijlstra

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
## [newstools/2022-the-guardian-nigeria](https://github.com/newstools/2022-the-guardian-nigeria)@[dc1471adbd...](https://github.com/newstools/2022-the-guardian-nigeria/commit/dc1471adbd406f391c2d91a5f564fd80291c9e02)
#### Friday 2022-04-15 14:16:53 by Billy Einkamerer

Created Text For URL [guardian.ng/politics/abiodun-urges-apc-members-to-eschew-do-or-die-politics-imbibe-spirit-of-love-forgiveness/]

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[cd2bd18cf8...](https://github.com/ss220-space/Skyrat-tg/commit/cd2bd18cf8193c7cfc2f0014ef449baa8792aad4)
#### Friday 2022-04-15 15:29:01 by SkyratBot

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
## [RocketChat/RC4Community](https://github.com/RocketChat/RC4Community)@[ddc933b9cc...](https://github.com/RocketChat/RC4Community/commit/ddc933b9cc0e4d53f4041682d01789ee8477ee0a)
#### Friday 2022-04-15 15:59:11 by Sidharth Mohanty

Official Project License Christening Commit (#147)

@sidmohanty11  was nominated by @Dnouv  and seconded unanimously by all in attendance for creating this milestone commit:

@sidmohanty11 @samad-yar-khan @demonicirfan @Sing-Li @RonLek @Dnouv 

On this "Good Friday 2022"  team members meeting,  @Sing-Li was moved to tears by the open source team spirit and camaraderie displayed (seldom seen in "day job" meetings nowadays)  Thanks for sharing  ! :pray: all !

License choice was voted on by team members (between Apache 2, MIT and GPL):

@sidmohanty11 @samad-yar-khan  @demonicirfan @Sing-Li  @RonLek  @Dnouv @debdutdeb @dudanogueira @abhinavkrin @engelgabriel 

All team members - please post a daytime bitmap of an environment near you  (on this comment)  to "remember this time".    Thanks.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[af92d4a5d6...](https://github.com/crawl/crawl/commit/af92d4a5d6ba2f841e8bfdf8639f77a784fcaeae)
#### Friday 2022-04-15 16:03:56 by Nicholas Feinberg

Make Hell Knights evil again (catern)

Lost this when they lost Pain.

Slightly hacky.

---
## [Defirence/Defirence](https://github.com/Defirence/Defirence)@[30d0be8dac...](https://github.com/Defirence/Defirence/commit/30d0be8dacb3ce3ffd4dab7a0cf963530d582462)
#### Friday 2022-04-15 16:11:45 by Defirence

cunt shit bitch fucking work now

Signed-off-by: Defirence <33593621+Defirence@users.noreply.github.com>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[1b7d7d9327...](https://github.com/pytorch/pytorch/commit/1b7d7d93276eb37c009905ef87ea9c2a7c95481e)
#### Friday 2022-04-15 16:17:57 by Brian Hirsh

Reland: "free up dispatch key space (in C++)" (#74963)

Summary:
Pull Request resolved: https://github.com/pytorch/pytorch/pull/74963

This is a re-land of D35192346 (https://github.com/pytorch/pytorch/commit/9872a06d77582e91e834103db75f774ca75f7fff) and D35192317 (https://github.com/pytorch/pytorch/commit/a9216cde6cc57f94586ea71a75a35aaabee720ff), which together are a diff that changes the internal representation of `DispatchKeySet` in pytorch core to free up the number of dispatch keys that we have available. See a more detailed description of the design in the original PR: https://github.com/pytorch/pytorch/pull/69633.

The original PR broke Milan workflows, which use a pytorch mobile build, and manifested as a memory corruption bug inside of `liboacrmerged.so`.

**Background: Existing Mobile Optimization**
Pytorch mobile builds have an existing optimization (here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/c10/core/DispatchKey.h#L382 and here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/OperatorEntry.h#L214), which works as follows:

Every operator in pytorch has a "dispatch table" of function pointers, corresponding to all of the (up to 64) different kernels that we might dispatch to when we run an operator in pytorch (autograd, cpu, cuda, complex number support, etc).

In mobile builds, the size of that table is shrunk from 64 to 8 to save a bunch of space, because mobile doesn't end up using the functionality associated with most dispatch keys.

The dispatcher also has a notion of "fallback kernels", which are kernels that you can register to a particular dispatch key, but should be able to work for "any operator". The array of fallback kernels is defined here: https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/Dispatcher.h#L294.

The mobile-optimization currently does **not** extend to this array (it wouldn't be that useful anyway because there is only one array of fallback kernels globally - vs. there is a separate dispatch table of function pointers per operator). So the per-operator tables on mobile are size 8, while the fallback table is size 64.

**The Bug**
This PR actually makes it difficult to enable that optimization separately for the per-operator arrays vs. the fallback array, and incidentally shrunk the size of the fallback array from 64 to 8 for mobile (that happened on this line: https://github.com/pytorch/pytorch/pull/69633/files#diff-f735cd7aa68f15b624100cbc4bb3b5ea76ffc7c9d3bec3b0ccabaa09609e5319R294).

That isn't a problem by itself (since mobile doesn't actually use any of the fallbacks that can no longer be stored). However, pytorch core will still register all of those fallback kernels on startup in mobile builds, even if they aren't used. When we tried to register one of those fallbacks on startup, it would try to dump the kernel somewhere in memory past the bounds of the (now smaller) array inside of the `Dispatcher` object, `backendFallbackKernels_`.

**Why didn't this problem show up in OSS CI? Why didn't it break other internal mobile workflows aside from Milan?**

Ideally, this failure would show up as part of the OSS signal on GitHub, since we already have mobile OSS builds. Given that it was another memory corruption issue that only affected Milan (subset of mobile), I'm not sure what's specific about Milan's builds that caused it only to manifest there. dreiss I wonder if there's another flavor of mobile builds we could run in OSS CI that could potentially help catch this?

**The debugging experience was pretty difficult**

Debugging the Milan-specific failure was made difficult by the following:

(1) lack of CI
- the original Milan failure didn't surface on my original diff, because the Milan job(s) that failed weren't triggered to run on pytorch changes. There's probably a balance to strike here, since those jobs will only be useful if they aren't flaky, and if they can produce reliable failure logs for debugging.

(2) It's difficult to get a repro.
- my work laptop doesn't have the right specs to run the Milan development workflow (not enough disk space)
- There is an existing OnDemand workflow for Milan, but it appears to be relatively new, and after a bunch of help from MarcioPorto, we ran into issues forwarding the log output from Milan tests on the emulator back to the terminal (see the original discussion here: https://fb.workplace.com/groups/OnDemandFRL/permalink/1424937774645433/)

(3) Lack of stack-traces.
- Most Milan failures didn't include actionable stack traces. phding generously helped me debug by running my suggested patches locally, and reporting back if there were any failures. The failing test didn't include a stack trace though (just the line where the crash appeared), so I ended up making some educated guesses about what the issue was based on the area of the crash.
ghstack-source-id: 152688542

Test Plan: Confirmed with phding that the broken Milan workflow from the previous version of this diff is now passing.

Reviewed By: phding, albanD

Differential Revision: D35222806

fbshipit-source-id: 0ad115a0f768bc8ea5d4c203b2990254c7092d30
(cherry picked from commit 002b91966f11fd55ab3fa3801b636fa39a6dd12c)

---
## [fAntMP/ChurchBellsTower](https://github.com/fAntMP/ChurchBellsTower)@[05962b50ce...](https://github.com/fAntMP/ChurchBellsTower/commit/05962b50ce3d1a21b6499a65963be697f05c3a64)
#### Friday 2022-04-15 17:48:42 by fAntMP

Religious celebrations names/descriptions edit

Changed a few of the religious celebrations descriptions/names.

Standardized the naming:

- Removed (for the most part) the word "The" before the feast.

- Used "Lord Jesus Christ" in naming a feast of the Lord.

- Used "Blessed Virgin Mary" in naming the Marian feasts.

- Changed the name of "Falling asleep" of the BVM to the "Dormition" of the BVM (I think that's how it is normally known as AFAIK- blame wiki)
*it might be even better to use the Dormition of the Theotokos (Mother of God) since that's probably the most common name used by the orthodox to name the BVM.

- I changed Christmas 2nd day to St Stephen's Day as it is celebrated in the church. However, I do not know what to do with the Orthodox feasts, since I have little knowledge of the Orthodox calendar. Also, since they follow the Julian calendar liturgically, Christmas day is different for them since (I think!) they use the Gregorian calendar on their computers and in everyday life.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2e1fc53391...](https://github.com/mrakgr/The-Spiral-Language/commit/2e1fc533913f42e6b3c8420ed45901d2d8ba4151)
#### Friday 2022-04-15 19:33:34 by Marko Grdinić

"9:40am. Things are going well. Any mail? Nope. I'll just notify the PMer that I emailed him yesterday.

9:50am. I slept well tonight. Let me chill just a bit and then I will get started on the desk piece. I am looking forward to getting it done properly.

10:10am. Let me get started on the desk piece. My comprehension of beveling really went up yesterday.

11am. This is ridiculous. I am getting my ass kicked by these bevels once again. None of the options fix the weird twisting issues.

11:10am. Gahhhhh! I can't figuring out how to do the bevel for that indented part. It is ridiculous.

https://youtu.be/kOteyoLZ2nk
MESHmachine 0.6 - Unf*ck

Let me watch this.

https://youtu.be/kOteyoLZ2nk?t=77

Ah, I see.

https://youtu.be/kOteyoLZ2nk?t=156

Blender has a redo?

11:25pm.

https://youtu.be/iZi5H73_Z6I
MESHmachine 0.8 - Wedge

I have no idea where I am going wrong. Maybe I don't understand bevels after all.

1:40pm. Let me have breakfast. I am still messing with it.

1:55pm.

///

nyaa.si for anime
rargb or 1337x for movies

///

There is some discussion on pirate sites. I never heard of rargb or 1337x.

2:35pm. Done with breakfast. Don't have chores today. Let me chill a bit and then I will resume.

3:15pm. Let me finish the Dungeon Meshi chapter and I will resume. It is a slow day today. I am just moving things around trying to comprehend how those bevels work.

3:25pm. Let me start.

3:45pm. https://blender.stackexchange.com/questions/32675/how-to-subdivide-part-of-mesh-but-not-apply-the-modifier

Let me try that alternative technique. Splitting apart the mesh at the point you down't want it to subdivided is not a bad idea.

But actually, no. This would result in inadequate geometry.

4:45pm. Let me take a break. Absolutely is nothing is going the way I imagine it.

All I wam trying to do is bevel a random hole. It literally has 5 faces.

How did I almost the entire day on this? And days on this previously?

5:20pm. I finally figured out how to do the corners properly. Let me try it again.

5:45pm. I did it! I finally understand how to do that piece perfectly. Let me just try some other things. There is something I need to make sure of.

6:40pm. Right now I am taking a break trying to digest all my insights. Let me finish reading Tower of God and then I will talk about it. As it turns out, I never used MESHmachine for the trouble parts because it was not capable of doing it. Instead I used the % bevel with supporting edges. That turned out to be so powerful. And now that I am actually thinking in this direction, I realize that I could use the technique to make any kind of edge.

7:05pm.  Ok, let me rant a bit. I won't do any art today apart integrating the new piece. The indent is a bit too large so I have to rescale it.

I've actually spent all this time working on the side that won't even be visible in the scene simply because I wanted to know the right way to do it. And now I know.

I was so stupid not because I took the time to learn, but because the techniques I used today are really so obvious yet my head was empty.

Remember how I did it with subdiv by using controlling loop cuts. You can use the exact same technique with bevel with % mode. This would allow you to get any kind of edge variation. Whereas the regular modes are very limited. You can only get a fixed offsets of various kinds.

For whatever reason, I was under the impression that % mode is difficult to use compared to the other modes and never thought more deeply about it. Instead I just bashed my head against the wall.

Had I known what I knew today, I probably would not have bothered buying MESHmachine. What was really digging at me from the inside was the lack of flexibility, and it turns out, the regular bevel tool is the flexible one!

It can quite a lot that MeshMachine's Fuse can't.

Still, this problem here was pretty exceptional. I won't have to dig out the other props and furniture pieces in the room.

But, I can't really call myself a 3d artist if I can't deal with making an indent into a cube and then beveling it so the corners are rounded. You can't make progress by avoiding difficult things. I just had to get a grasp on this very basic thing.

I knew that it should have been possible without resorting to subdiv and now I know how.

7:25pm. Now, even though I put in so much time into texturing it last time, I really will have to retexture it from scratch. The reason - I accidentally got rid of the file with the old object, both the .obj and the .blend version. So I have no choice.

Hmmm, let me try something. How would bevels behave with subdiv style loop cuts? The same as with regular ones assuming the loop slide is turned on. And it really should be with % mode. There is no problem.

8:20pm. I am playing around beveling the cube with supporting loop cuts. Let me watch that radial fillet vid again.

8:25pm. https://youtu.be/7xojWBmfx84?t=149
How to Create Variable Radius Bevel in Blender

Here is him using the bevel modifier while using loop edges to control the sliding. Sigh. This is the peril of going past 6pm.

I am pretty engrossed in studying art though. It is not as mentally strenuous as programming and I am having fun making steady progress in my understanding.

https://youtu.be/7xojWBmfx84?t=332

I am watching this again. The way he did this was in the most inefficient way possible. What he should have done is used the knif tool to carve out the support edges and then just beveled them.

8:40pm. I tried this just now and as expected it works great.

Bevel + knife tool is really a combo to keep in mind.

https://youtu.be/7xojWBmfx84?t=417

Using space to make the edges even is something worth keeping in mind.

8:55pm. Forget it. Let me just put the piece into place and I will close.

9:15pm. It seems the area coverage is actually worse than when it was done automatically. I get only 1.67 while the auto one got 1.82. 83% vs 91%.

9:20pm. Sigh, what a masterpiece. Today I've finally grasped the fundamentals of beveling. Over six months into the journey, but better late than never.

Tomorrow I'll retexture it and move on to the rig and the monitor. The rig will be a bit challeging if I decided to go the boolean approach. If I decide to do the holes in Substance Painter using normals, things will be a lot easier. I'll have to try the both approaches since it is my first time."

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[bfd0d71d22...](https://github.com/newstools/2022-express/commit/bfd0d71d22778cd69671a3a525663cf6c2a69f52)
#### Friday 2022-04-15 20:02:23 by Billy Einkamerer

Created Text For URL [www.express.co.uk/news/science/1596606/end-of-the-world-nasa-scientist-left-tears-dire-warning-climate-crisis-impending-disaster]

---
## [pitaden/MonkeStation](https://github.com/pitaden/MonkeStation)@[040b7ff839...](https://github.com/pitaden/MonkeStation/commit/040b7ff839d51d4db2ce1747f92312e0925bccd2)
#### Friday 2022-04-15 20:28:42 by Zonespace

Adds Flavor Text (#48)

* lgtm

* aaaAAAA

* might be better idk

* flavor-examine

* info

* haaa fuck you github

---
## [filecoin-project/evergreen-dealer](https://github.com/filecoin-project/evergreen-dealer)@[1fb8a2f005...](https://github.com/filecoin-project/evergreen-dealer/commit/1fb8a2f005cafc2abc3fec74d5e4a80e652686b0)
#### Friday 2022-04-15 20:39:07 by Peter Rabbitson

Do not normalize CidV0 to CidV1 - it breaks fil-markets :cryingbear:

A piece of code from a different project ( .storage ) got copied over together
with the deal-on-chain tracking gadget. While in other projects this is an
innocuous and even welcome addition, it is a catastrophic bug any time evergreen
interacts with a deal originally made using CidV0.

The core reason for this lies deeply in the car file format: it is not sensitive
to multibase variations, but it *is* sensitive to cid version. The sequence of
failure events would be:

- Participant retrieves a deal made with a CidV0 root, exports as car
- This car is currently likely to end up as the exact bytes that were in the
  sealed sector, thus will continue satisfying the PieceCid (*)
- The new deal proposal made by Evergreen upgrades the `Label` to Cidv1. At
  this point nothing odd is going on yet - the Label should ideally be correct
  but it is not a must / there is no cheap mechanism to verify this anyway.
- The new deal is satisfied and sealed. Now the dagstore has an entry for a
  CidV1 even though the underlying car ( and thus PieceCid ) refer to CidV0.
- *Another* participant tries to retrieve the deal evergreen made: this is
  where things go sideways. Either the dagstore does byte-level CID equivalence
  and outright says "I do not have this", or (worse) the dag is streamed out
  over graphsync and a new car is assembled with a different Header and first
  block. This in turn means that the subsequent user will not be able to
  arrive at the same PieceCid and will not be able to satisfy their own deal.

Since we currently "quantize" every individual car file, regardless of transfer
method (see * below) the only expedient way to fix this is to remove the
normalization when a CidV0 is encountered, declare all "incorrect" deals
invalid, and get the individual SPs to re-seal the same cars with the "proper"
proposal label in a few days.

The original code and its inclusion in this project were both a singlehanded
product of one Mr Ribasushi. Shame be on his name.

(*) This entire change is a temporary hack to unblock Evergreen, it is by no
means a robust nor desired solution. The Label field has been advisory from
the launch of the network, and there are already plenty of proposals on chain
with malformed/incorrect/missing Label's. Moreover - the assumption that a car
file can be "quantized" and recreated is extremely fragile, and is quickly
becoming outright wrong. The savvier a client the less likely they are to
produce a "depth-first" car, and less likely to use a quantizing transport
like graphsync (e.g. .storage is switching all their filecoin dealmaking to
non-indeterminstic cars by the end of 2022)

In order for programs like Evergreen and later on various DAO/FVM-based renewal
mechanism to work, there must be a way to bulk retrieve a payload by its PieeCid
alone. This will be written up as a feature request for Boost in the next few
weeks.

---
## [JuliaPackaging/Yggdrasil](https://github.com/JuliaPackaging/Yggdrasil)@[1f850e1d63...](https://github.com/JuliaPackaging/Yggdrasil/commit/1f850e1d637634be4df8145ea4775ebfdf20732d)
#### Friday 2022-04-15 21:03:29 by Elliot Saba

[GCCBootstrap_jll] Build using `crosstool-ng`

In the beginning, I wanted to compile a nice little standalone `GCC_jll`
that could be hooked together with a `Glibc_jll` and a `Binutils_jll`,
and a `LinuxKernelHeaders_jll`, etc...  That work is sitting in [0] but
bootstrapping is such a giant pain in the neck that I wanted to give up
the complexity of bootstrapping to instead focus on simply building each
product in isolation.  This _vastly_ reduces the amount of work
necessary to get things working, but it introduces a new dependency: we
need a base C compiler and libc that are already compiled for the target
platform.  To be precise, we need a `build -> host` compiler in order to
build a `host -> target` compiler.  We already have one of those for all
of our current platforms, so I could generate `GCC_jll` packages, but
then when we want to add a new platform, we'd be in trouble.  For this
reason, I realized we'll never truly escape the bootstrapping problem.

I thought about reverting back to the bootstrapping configuration we've
had until now, but rebelled at the thought.  Then I discovered
crosstool-ng, and realized that I could separate concerns here: I can
use ct-ng to build a working cross-toolchain for each target, then use
that compiler to do a much simpler build for all of the other
components.  Therefore, I extract the work of getting a bootstrap build
onto crosstool-ng, and then use that to do whatever other builds I want
in the presence of a fully-functional cross-compiler.

This also breaks the need for the initial bootstrap to be quite as
restricted as the target toolchain.  The GCC that we build technically
doesn't need to run everywhere, it just needs to generate code that runs
everywhere.  We can build GCC against glibc 2.19, and then at build time
have it link the code it generates against glibc 2.12.2, and that will
work just fine for BB.  The compiler may be using a newer glibc to run,
but when it builds, it uses whatever glibc is placed within the target
sysroot.  This also means we don't need to do things like build GFortran
as part of our bootstrap; we can build it later, in the simpler build
script.

In principle, we don't actually need a GCCBootstrap for all platforms.
We only need a functional cross-compiler.  Theoretically, we could use
Clang to do the bootstrapping.  But I'm not going to fully embrace that
because I know that compiling Glibc with Clang is a pain, so for
`*-linux-gnu` at the very least, we're not going to attempt that.  On
macOS and FreeBSD however, there is a possibility that we can use Clang
as our "bootstrap compiler" in order to generate the actual GCC_jlls.

[0] https://github.com/JuliaPackaging/Yggdrasil/tree/sf/gcc

---
## [Discord-Snake-Pit/Dis-Snek](https://github.com/Discord-Snake-Pit/Dis-Snek)@[86d1f3b77f...](https://github.com/Discord-Snake-Pit/Dis-Snek/commit/86d1f3b77f4cdba92bba3a5b675b6af29314eb21)
#### Friday 2022-04-15 23:04:38 by LordOfPolls

feat: integrate ugly-ass localisation into app_cmds

Discord i hate how you did localisation - its midnight, im tired, this works, i want to scream. ive had "enaff"

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8f1522343c...](https://github.com/treckstar/yolo-octo-hipster/commit/8f1522343cd402aa06be982076f8ed91d62e0d27)
#### Friday 2022-04-15 23:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[cc9932de58...](https://github.com/newstools/2022-new-york-post/commit/cc9932de582b309fcc9027c1fb6ccb3ae92eab48)
#### Friday 2022-04-15 23:36:04 by Billy Einkamerer

Created Text For URL [nypost.com/2022/04/15/josh-allen-girlfriend-brittany-williams-enjoy-dinner-date/]

---

