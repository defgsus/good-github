## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-13](docs/good-messages/2023/2023-06-13.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,178,862 were push events containing 3,524,974 commit messages that amount to 287,248,001 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[b420c1d519...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/b420c1d519b30cd75759de68f6b2abbe0b12a055)
#### Tuesday 2023-06-13 00:14:39 by vampirebat74

Adds tool E.G.O (#1019)

Tool ego

adds tool E.G.O

removes a extra line

fixes shit

swindle

voce

divinity

fixes shit

shifts divinity down a few pixels

This is the fourth time this same commit was made

I hate TG so fucking much like it's unbelievable why does this only fuck up on my PC? WHY?

hyde weapon

stuff

hyde code

hyde fix

new sprites

inhands

destiny effect

heart sfx

stuff

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [KhalfounMehdi/hhvm](https://github.com/KhalfounMehdi/hhvm)@[d29989197d...](https://github.com/KhalfounMehdi/hhvm/commit/d29989197df04f50f044d062f464579376f6bd14)
#### Tuesday 2023-06-13 00:33:55 by Lucian Wischik

5/6 rewrite ClientIdeInit - reimplement, richer telemetry+logging

Summary:
[This series of 6 diffs rewrites the "load naming table + search index" parts of ClientIdeDaemon. I'm doing this because I want to rollout Tom's "ide_batch_process_changes" feature which changes performance characteristics, but the existing telemetry wasn't adequate for measuring its impact, and the code had grown too complex to tweak.]

This diff rewrites the control-flow in ClientIdeInit.ml, and adds telemetry+logging in a more uniform way than what was there before.

BEFORE:
* `init` -- try to find existing ss on disk, otherwise fallback to init_via_initialize_or_download, and if that fails then call init_via_build and also use the resulting si_addenda to update sienv.
  * `init_via_initialize_or_download` -- if LSP Initialize method specifies a path to a naming-table then use that, otherwise fetch saved-state
  * `init_via_build` -- calls into rust to produce a naming-table sqlite

AFTER:
* `init_via_find` -- attempts to use a naming-table on disk, or returns Failure if it didn't find anything
* `init_via_lsp` -- attempts to use what's in the LSP initialize method, or returns Skip if nothing specified
* `init_via_fetch` -- attempts to download saved-state, or returns Failure in case of error or absence
* `init_via_build` -- attempts to build saved-state, or returns Skip if not allowed by the project's .hhconfig, or returns Failure if it didn't work
* `map_attempt` -- given an attempt, wraps it in comprehensive telemetry+logging
* `init` -- attempts each strategy in turn (find, init, fetch, build) by calling them in turn and using map_attempt on the result.

```
  (* We will make several attempts using different techniques, in order, to try
     to find a saved-state, and use the first attempt to succeed.
     The goal of this code is (1) rich telemetry about why each attempt failed,
     (2) in case none of them succeed, then return a user-facing
     [ClientIdeMessage.rich_error] that has the most pertinent information for the user.

     An attempt might either skip (e.g. if config flags disable it), or it might fail.
     The way I've solved goal (2) is that we'll display a user-facing message
     about the final failed attempt.
     There are some subtle interactions here worth drawing attention to, based on how
     various libraries were written that we call into:
     1. [init_via_find] returns Skip if ide_load_naming_table_on_disk=false, but it
        returns Failure if there were no saved-states on disk, or none were recent enough,
        or if it found a candidate but experienced a runtime failure trying to use it.
     2. [init_via_fetch] doesn't ever return Skip; it only uses Failure. This makes
        sense in cases like manifold crash or zstd crash, but it's a bit odd in cases
        like the user modified .hhconfig so no saved-state is possible, or the user
        is in a repository that doesn't even have saved-states.

     How does all this fit together to satisfy goal (2)? If we're in a repository that
     allows building (i.e. its .hhconfig lacks "ide_fallback_to_full_index=false") then
     the user-facing message upon overall failure will only ever be about the failure to build.
     If we're in a repository that doesn't allow building, then the user-facing message
     message upon overall failure will only ever be about the failure to load saved-state.

     How does it satisfy goal (1)? Inside [map_attempt], if there was a "skip" then we
     only store brief telemetry about it. But if there was a "failure" then we store
     very detailed telemetry. Once ide_load_naming_table_on_disk is fully rolled out,
     we'll end up storing detailed telemetry about every single "failed to find on disk".
     That's good! I fully hope and expect that 99% of users will find something on disk
     and be good. But if that fails, we'll always store rich information about every
     "failed to fetch". That's also what we want. *)
```

I wanted to make this diff be a refactor without changing behavior. Hence:
```
If a step determines that it has got an sqlite file path, but we subsequently error
while trying to open the sqlite file (e.g. it has zero size) then that counts as
failure and we continue on to the next attempt. Weird but true. *)
```

There was one behavior I changed. Previously, if load failed, then it would report to the VSCode UX just a vague message "Hack IDE support has failed". We have two sources of wording: (1) Saved_state_loader.load_error can give a very precise actionable error message in some cases like watchman not working, but it deliberately doesn't mention the IDE because it's a common library not IDE-specific; (2) ClientIdeUtils gives a vague but IDE-related message. I split the difference by preferring the wording from Saved_state_loader.load_error if the error is actionable, and from ClientIdeUtils if it's not. This is exercised by the existing test "failed_to_load_saved_state_no_full_index".

(Also, along the way, I changed the pair "ClientIdeMessage.rich_error * Lsp.Error.t" to just "ClientIdeMessage.rich_error", since the previous diff had made it sufficiently expressive).

Reviewed By: mheiber

Differential Revision: D46623369

fbshipit-source-id: 830da87328bbd15d03803be2308dec8291f969ae

---
## [KhalfounMehdi/hhvm](https://github.com/KhalfounMehdi/hhvm)@[2ca9947fbc...](https://github.com/KhalfounMehdi/hhvm/commit/2ca9947fbc94e2779879d5a2c99d74f9940226cd)
#### Tuesday 2023-06-13 00:33:55 by Lucian Wischik

2/6 rewrite ClientIdeInit - refactor into separate file

Summary:
[This series of 6 diffs rewrites the "load naming table + search index" parts of ClientIdeDaemon. I'm doing this because I want to rollout Tom's "ide_batch_process_changes" feature which changes performance characteristics, but the existing telemetry wasn't adequate for measuring its impact, and the code had grown too complex to tweak.]

This diff makes a few steps along the way to rewriting...

**STEP 1: New module clientIdeInit.ml**. This diff moves all the load-naming-table code into its own module. I didn't change the code much yet (that's done in next-but-one diff); all I did was (1) remove Hh_logger.log in anticipation of rebuilding them better, (2) remove the dependency upon clientIdeDaemon state, by passing parameters explicitly. Sorry the diff makes it hard to read what is the difference between the old and new, which will be hard to review. You could just take it as granted that it's mostly all just copy+paste.

**STEP 2: config, local_config**. The behavior for loading saved-state is controlled by four in .hhconfig and hh.conf:
* `ide_should_use_hack_64_distc` - hh.conf + JK flag, currently at 100% and awaiting cleanup, controls whether HackIDE should use the same saved-state as hh_server (rather than downloading its own "hack/naming" saved-state).
* ide_load_naming_table_on_disk - hh.conf + JK flag, currently at 50%, controls whether HackIDE should be willing to load a (possibly old) saved-state that already exists on disk, rather than insisting on the newest one and waiting for it to download.
* ide_naming_table_update_threshold - hh.conf + JK flag, currently at 500, controls how hold HackIDE is willing to use a saved-state that's already on disk
* ide_batch_process_changes - .hhconfig (false for WWW, true elsewhere), currently at 0% and awaiting rollout, controls whether to use the newer synchronous rust multicore indexing of file-changes, or the old asynchronous single-threaded ocaml indexing.

They're treated pretty idiosyncratically. Some are read direct from local_config during the initialize method. Others are copied into GlobalOptions and read from Provider_context.typechecker_options in other methods. Some are read during the initialize method, copied into HackIDE "common-state" (for mutable data that's common to During_init and Initialized states) and read from there.

None of this idiosyncrasy makes sense. What I've done in this diff is simply store `config` (from .hhconfig settings, including tcopt and popt) and `local_config` (for hh.conf settings) into the "common-state". In this way, all the code in clientIdeDaemon can retrieve whatever settings it wants, and we don't need to duplicate them.
```
BEFORE:
type common_state = {
  hhi_root: Path.t;
  sienv: SearchUtils.si_env; [opaque]
  popt: ParserOptions.t;  (** parser options *)
  tcopt: TypecheckerOptions.t;  (** typechecker options *)
  local_memory: Provider_backend.local_memory; [opaque]
  fall_back_to_full_index: bool;
  ide_batch_process_changes: bool;
}

AFTER:
type common_state = {
  hhi_root: Path.t;
  config: ServerConfig.t; [opaque]
  local_config: ServerLocalConfig.t; [opaque]
  local_memory: Provider_backend.local_memory; [opaque]
}
```

**STEP 3. sienv in Initialized state**. The clientIdeDaemon code has four states:
```
| Pending_init  (** We have not yet received init request *)
| During_init of dstate (** We are working on the init request: still loading naming-table *)
| Failed_init of ClientIdeMessage.rich_error (** failed to load naming-table *)
| Initialized of istate  (** Succeeded to load naming-table; ready to handle requests *)

BEFORE:
type istate = {
  icommon: common_state;
  ifiles: open_files_state; [opaque]
  naming_table: Naming_table.t; [opaque]
}

AFTER:
type istate = {
  icommon: common_state;
  ifiles: open_files_state; [opaque]
  naming_table: Naming_table.t; [opaque]
  sienv: SearchUtils.si_env; [opaque]
}
```
The job of initializing is to load the naming-table and symbol index from whatever source (manifold, on-disk, build one from scratch, ...). The result is stored in `Naming_table.t` and `sienv`. Conceptually, we don't even have a naming-table nor sienv until after initialize has finished, i.e. until after we're in `Initialized istate`.

Before this diff, sienv was initialized prior to `During_init`. That wasn't principled, but it used to work out in practice because sienv was merely a placeholder saying "please ask Glean for symbols". Things changed however with the recent advent of naming_table_builder which constructs an in-memory sienv out of the symbols it parsed while building the naming table. Therefore, now, there is no meaningful sienv to be had During_init.

This diff moves `sienv` out of "common-state" and into "istate" where it belongs, adjacent to `naming_table`.

**STEP 4: ServerEnvBuild**. ServerEnv and ServerEnvBuild represent the state of hh_server, i.e. its multiworkers, what things have been invalidated by watchman. None of these things make sense in ClientIdeDaemon which doesn't have multiworkers and doesn't have hh_server's state.

We used to be calling into ServerEnvBuild as a weird way to fetch `tcopt, popt, gleanopt` out of ServerConfig. I changed it to fetch those things directly. This way I can remove the dependency upon ServerEnv.

Reviewed By: mheiber

Differential Revision: D46619424

fbshipit-source-id: 37f06ced7c268fe73ffca634b3af2d2812cae391

---
## [MichaelDeBoey/react-native](https://github.com/MichaelDeBoey/react-native)@[ee38c4a40c...](https://github.com/MichaelDeBoey/react-native/commit/ee38c4a40c9d301c30fad4d127e8d020a6100b8e)
#### Tuesday 2023-06-13 00:38:49 by Phillip Pan

introduce build boilerplate for ios unit tests (#37811)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/37811

Changelog: [Internal]

i am looking to add ios unit tests to venice and this is the first unit test suite that will test native ios code in the new architecture afaik, so i wanted to open this up to discussion.

currently, all `XCTest` in `react-native-github` are coupled with the `RNTester` target. my main qualm with this is i am concerned that it won't scale well. currently we have only ~30ish tests but ultimately if we want a proper testing suite, surely this count will be in the hundreds and that won't be able to reasonably live in a single test target.

however, the trade is that this test will not show up in RNTester. i have added a unit test to RNTester before in D31949237, however the experience was extremely painful as i had to manually update the `project.pbxproj` to include my file, and i had to manually determine what hex value was the next one (for whatever reason, this doesn't increment at the endian...).

i am wondering if we can treat the current unit testing experience in RNTester as pretty much maintenance mode and start thinking of a improved version starting with something more modular like this.

Reviewed By: cipolleschi

Differential Revision: D46467229

fbshipit-source-id: 09de9cf8bc5f8b9c86abcaf7750a6f63686d8d1a

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[18819cc7fb...](https://github.com/Latentish/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Tuesday 2023-06-13 00:43:11 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [canonical/operator](https://github.com/canonical/operator)@[a4ba60bf08...](https://github.com/canonical/operator/commit/a4ba60bf08e703c676adc1bd36fabfd5d3eb94a0)
#### Tuesday 2023-06-13 01:26:24 by Ben Hoyt

Update Pyright version to latest (1.1.313) (#944)

Boy this was more painful than I expected. Lots of fighting with the
compiler. I ended up disabling a few more Pyright issues, specifically
these seemed more trouble than they're worth:

* reportPrivateUsage: we do this often in the codebase, for example
  charm.py pokes at _ModelBackend stuff
* reportUnnecessaryIsInstance: we do lots of isinstance checks to
  detect type issues at runtime (we've done this since the beginning,
  and it's useful for people not using type checking)
* reportUnnecessaryComparison: similar to the above, but for checking
  "if non_optional_value is None" and the like

* Fix issue with Pebble.exec and Container.exec types

Currently Pyright isn't (usually?) able to find the return type of
Container.exec, I think due to an import ordering thing? As such,
charms that use it get an Any type and static checks pass.

However, as soon as Pyright *can* find the return type, it's not really
correct, and we get errors like shown below.

We need to use Generic[AnyStr] and various overloads to ensure the
caller gets an ExecProcess[str] if they call exec() with "encoding" set
(the default), or ExecProcess[bytes] if they call exec() with
"encoding" set to None.

$ tox -e static-charm
static-charm: commands[0]> pyright /home/ben/w/grafana-k8s-operator/src
/home/ben/w/grafana-k8s-operator/src/charm.py
  /home/ben/w/grafana-k8s-operator/src/charm.py:929:28 - error: Argument of type "Literal['Version (\\d*\\.\\d*\\.\\d*)']" cannot be assigned to parameter "pattern" of type "bytes | Pattern[bytes]" in function "search"
    Type "Literal['Version (\\d*\\.\\d*\\.\\d*)']" cannot be assigned to type "bytes | Pattern[bytes]"
      "Literal['Version (\\d*\\.\\d*\\.\\d*)']" is incompatible with "bytes"
      "Literal['Version (\\d*\\.\\d*\\.\\d*)']" is incompatible with "Pattern[bytes]" (reportGeneralTypeIssues)
  /home/ben/w/grafana-k8s-operator/src/charm.py:929:56 - error: Argument of type "_StrOrBytes" cannot be assigned to parameter "string" of type "ReadableBuffer" in function "search"
    Type "_StrOrBytes" cannot be assigned to type "ReadableBuffer"
      Type "str" cannot be assigned to type "ReadableBuffer"
        "str" is incompatible with "ReadOnlyBuffer"
        "str" is incompatible with "bytearray"
        "str" is incompatible with "memoryview"
        "str" is incompatible with "array[Any]"
        "str" is incompatible with "mmap"
        "str" is incompatible with "_CData"
    ... (reportGeneralTypeIssues)
2 errors, 0 warnings, 0 informations

* Remove now-unnecessary quotes around 'pebble.X' types

* Comment out alertmanager-k8s-operator CI for now

---
## [Al-1ce/cmss13](https://github.com/Al-1ce/cmss13)@[0f386c8188...](https://github.com/Al-1ce/cmss13/commit/0f386c8188849b2a761ef773ed83d7f2a95d40e7)
#### Tuesday 2023-06-13 01:38:39 by fira

Stops Squad Leaders and ComTechs from blowing up the Almayer (#3602)

# About the pull request

Okay that's a clickbait....

When people put C4 and Breaching Charges in their bag and what not the
log gets triggered.

This spams niche log with false warnings of /!\ DANGEROUS GRIEFING
TERRORISTS /!\

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Uh

# Changelog
:cl:
fix: Handling C4 and Breaching Charges should not zealously trigger
antigrief protection anymore
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [ferrous-systems/rust-training](https://github.com/ferrous-systems/rust-training)@[d1105c5b32...](https://github.com/ferrous-systems/rust-training/commit/d1105c5b32d8da918a7749c3869cb16fb0ba31e9)
#### Tuesday 2023-06-13 02:02:39 by Andrei Listochkin

Lifetimes Intro slides

These are based on how I've been teaching lifetimes in the past **8-12 months**. I build up an intuition around functions returning references and using annotations to tag returned references and their corresponding sources of data. When I do it live I tend to have more intermediate situations covered: functions that only accepts references but don't return references, a function that takes a single reference and returns many, their variations with non-reference parameters and returned components, you get the idea. I dropped most of it because they don't work as well in slide format.

Also, while this flow leads to a much gentler introduction in general, it requires covering static data and `'static` lifetime before anything else, and there's this awkward chicken-and-egg phase early. In my experience, it can be tip-toed over pretty easily. I actually started introducing the concepts of three memory types: static, stack, and heap very early, - on day 1 or 2. C/C++ people don't need it per se, but even they benefit from discussing it when we talk about containers like `Vec`, `String`, or `Box` and recursive structs or enums. This way by the time we talk lifetimes the audience has a benefit of familiarity ("Oh, `static`, I remember: that's for static memory!")

One example I add in the middle actually shows how adding lifetime annotations helps the programmer find and fix bugs in code. Some of the code fragments are *subtly* incorrect, and I'd love to add speaker notes for them so that trainers won't stumble through them too much. I show this example to demonstrate that these annotations are not only to keep the compiler happy, but also for your benefit as well. Another attempt at turning lifetimes perception around: they are friends, not enemies.

----

Despite the fact that there's quite a bit more content I actually cover *less* in terms of material. I don't mention elision, non-lexical lifetimes, lifetime dependencies and sub-lifetimes. In my view these concepts are too advanced to present to intro groups, and advanced groups would benefit from doing more exploratory lifetime coverage via Serde exercise and / or `std::thread::scope` API. It has everything: sub-lifetimes, higher-ranked trait bounds for lifetimes, and all of that mixed with multithreading safety discussion! Still, if we want to keep old contend I don't mind moving my material into a separate deck.

I do, however, mention a few type system aspects of lifetimes, mostly around `T: 'a` and `T: 'static`. Both show up in signature of standard library methods, both look very confusing for newcomers. For my training flow (`syntax -> traits -> memory -> multithreading`) this information bits play out really well. `std::thread::spawn` has a `+ 'static` in its signature *twice*, and I can point to it and tell my audience: "remember this? we talked about it yesterday!"

----

Finally, I'm afraid my terminology around lifetime annotations, lifetime type parameters, and lifetime generics is not entirely accurate. I try to find a balance around being precise and not overload the audience too much.

---
## [FENLLY/session-pysogs](https://github.com/FENLLY/session-pysogs)@[31bfd14d80...](https://github.com/FENLLY/session-pysogs/commit/31bfd14d80ec723fde3c3589408a27fc878f247f)
#### Tuesday 2023-06-13 04:08:48 by Jason Rhinelander

Use SQLAlchemy for database backend

We're using it fairly minimally: essentially still writing manual
queries, but now using SQLAlchemy to handle placeholder binding which is
nicer, and portable.

The API now goes like this:

- `db.get_conn()` returns a connection from the connection pool;
  web.appdb, in particular, is a preloaded, app-context connection
  object that most code uses.

- `web.query()` does an SQLAlchemy 'text' query, which is almost like
  regular prepare+bind+execute, except that it always uses `:name` for
  placeholders and binds using `name=...` keyword arguments.  That is,
  instead of:

      db.execute("SELECT token FROM rooms WHERE id = ?", (123,))

  we now do:

      query("SELECT token FROM rooms WHERE id = :id", id=123)

  or equivalently:

      db.query(appdb, "SELECT token FROM rooms WHERE id = :id", id=123)

  (the latter version is more useful where an app context doesn't exist
  and you need to pass in some other conn, such as is now done in
  __main__).

- transactions are now controlled with a `with appdb.begin_nested():`
  context, replacing the custom nested tx handler I made for sqlite.

We *could* start using more advanced SQLAlchemy query composition, but
that seems like more of a pain rather than something useful.  (I *don't*
want to use SQLAlchemy ORM, because in my experience ORM just gets in
the way as soon as you want non-trivial database structure, which we
have here).

This will allow us to (easily) add postgresql support.  (Other database
are probably a no-go: SQLite has long looked up to postgresql for
features and syntax and so the two are very similar dialects).

---
## [danieljharvey/mimsa](https://github.com/danieljharvey/mimsa)@[e26ca2a932...](https://github.com/danieljharvey/mimsa/commit/e26ca2a9320e5c59b7b12433bc7d36b2cdfa8b99)
#### Tuesday 2023-06-13 04:17:32 by Daniel Harvey

Actually typecheck multiple definitions (#962)

* Test module typechecking more throughly

* Damn this shit is fucked

* We need to make these types stricter

* Skippy

* Nice

---
## [ValoTheValo/CEV-Eris](https://github.com/ValoTheValo/CEV-Eris)@[b92562ad8f...](https://github.com/ValoTheValo/CEV-Eris/commit/b92562ad8f26c2354730f8a013195a90bbfbe9fd)
#### Tuesday 2023-06-13 04:56:52 by ValoTheValo

Makes the "Gun" Not spawn in maint, makes MK58 fit in holsters (#8200)

* changes item path to be consistent

i hate kegdo

* kegdo code moment

what fucking moron designed this

* fixes MK58 not fitting in holster

pain

* Update holster.dm

* kegdo moment

---
## [orcunc/hazelcast](https://github.com/orcunc/hazelcast)@[566574a5b4...](https://github.com/orcunc/hazelcast/commit/566574a5b49f423109a4de61f21427838bd8076b)
#### Tuesday 2023-06-13 05:23:35 by James Holgate

Modify KubernetesClient shutdown behaviour  (#24613) [5.3.z] (#24710)

Backport of: https://github.com/hazelcast/hazelcast/pull/24613

The overall goal of this change is to change the shutdown behaviour of
KubernetesClient so our Stateful Set monitor thread shuts down before
our `ClusterTopologyIntentTracker`, to allow the intent tracker to fully
process all completed messages before Node shutdown.

**The Current Problem**
In its current state, the Stateful Set monitor thread is intended to
shutdown after `Thread#interrupt` is called, triggering the
`Thread#interrupted` check within the main `while(running)` loop of the
Runnable. However, this check is not reached as the call to
`WatchResponse#readLine` from within the main `run()` method is a
blocking call that waits until data is available to read before
proceeding. Since this call waits for non-null data before completing,
the result is always non-null, and therefore this code block never exits
under normal conditions:
```java
while ((message = watchResponse.nextLine()) != null) {
    onMessage(message);
}
```

Since this `while` loop cannot exit, and the `#readLine` method (which
passes to `BufferedReader#readLine` under the hood) is a blocking I/O
operation which cannot be interrupted, this operation does not end when
`Thread#interrupt` is called. This leads to the Stateful Set monitor
thread out-living the `ClusterTopologyIntentTracker`, even if the
StsMonitor is interrupted first. As a result, during shutdown, it is
possible for the StsMonitor to send data to the intent tracker after it
has been destroyed and its executor is no longer accepting tasks.

**The Root of the Problem**
To reach our goal of ensuring that the Stateful Set monitor thread can
no longer send requests to the `ClusterTopologyIntentTracker`, we need
to add synchronization between the two objects that guarantees the
intent tracker shuts down after the StsMonitor thread has completed.
This can be achieved using a simple `CountDownLatch` which is counted
down after the thread has completed, and awaited before shutting down
the tracker.

The main obstacle to achieving this is, as mentioned above, that the
StsMonitor thread cannot be interrupted when waiting for
`WatchResponse#readLine` to complete, and so the thread never completes.
The only way this thread can complete is to either force its
termination, or alter the message reading approach to allow interruption
as intended.

**Identifying Resolution Paths**
We don't want to force termination of our Stateful Set monitor thread as
this could result in message handling being terminated after it has been
received, but not before it has finished being processed. Therefore the
only way we can allow this thread to be interrupted as intended is to
alter the message reading mechanics in a way that allows it to be
interrupted as well.

There is no way for us to know if more messages are pending from the k8s
watch besides waiting for data to be received, so the best we can do is
allow the StsMonitor to finish processing any messages it has already
received (preventing process corruption), but terminate the stream of
new messages it is waiting for before we shutdown the intent tracker.

**Potential Solutions**
So we've identified the root of the problem as our `#readLine` function
blocking through interrupts, so how do we make it interruptible? Sadly
one of the shortcomings of I/O operations in Java is that they usually
cannot be interrupted in the traditional manner, so we have a few
approaches to consider:

1) We could modify the message reading code to use
`BufferedReader#ready` and `Thread#sleep` to periodically check if there
is data to be read before calling any read functions. The problem with
this approach is that A) `#ready` returns true if any data is available,
not just if there is a full line of data to be read; and B) utilizing a
sleep loop can result in delayed message handling at the least, or
busy-waiting overhead at worst.

2) We could use "hacky" solutions to interrupt the
`BufferedReader#readLine` such as closing underlying sockets or
connections, propagating an exception to the reader. The problem with
this solution is that everything related to our reading operation is
handled in `syncrhonized` blocks, and since our shutdown process starts
outside the StsMonitor thread, our calling thread is unable to obtain
these locks (being held by the StsMonitor)!

3) It's possible that we could rewrite the `WatchResponse` mechanics to
use Java NIO magic such as `Selector` for interruptible I/O operations.
The issue with this approach is that it would require fairly significant
refactoring of the related codebase, and may not end up providing the
exact functionality we are looking for in our use case.

4) We can introduce an `Executor` to handle our I/O operations within
the StsMonitor thread, allowing us to wait on a `Future#get` call
instead of our `BufferedReader#readLine` call, where a `Future#get`
operation can be interrupted by the waiting thread being interrupted.
The downside to this solution is we have to introduce an additional
thread on top of the existing StsMonitor thread itself.

**Selecting a Solution**
Considering the above information, I concluded the most sensible
approach was to use (4) and introduce an `Executor` thread for the I/O
operations. By using a separate thread for this call we can be rougher
with it, as we know that worse case scenario we interrupt a message
being read that has not started being processed yet (but we're shutting
down anyway).

This solution also allows for the least amount of underlying code
changes, as our `Future#get` can be interrupted without issue,
maintaining the current approach used for handling the StsMonitor
shutdown. The only downside for this approach is the addition of another
thread alongside the StsMonitor thread, but the actual impact of this
should be minimal as both threads will still be waiting most of the
time, so the only negative impact is being 1 tiny step closer to
possible thread starvation.

Generally I think this is the best solution at hand which allows quick
shutdown of the StsMonitor thread while minimising potential for data
loss or corruption. Combined with the `CountDownLatch` used, this allows
for consistent service shutdown order between the `StsMonitor` thread
and the `ClusterTopologyIntentTracker`.

---
## [Yobrocharlie/tgstation](https://github.com/Yobrocharlie/tgstation)@[2aaafd9a67...](https://github.com/Yobrocharlie/tgstation/commit/2aaafd9a67c270fa0772cd9beffb6789d53750e3)
#### Tuesday 2023-06-13 05:24:25 by TheVekter

Replaces the syndicate corpse Legions can drop with one without a MODSuit (#75700)

## About The Pull Request
This is part of a pass I'm working on doing where I go through and
remove instances of antag gear outside of their normal context. This is
mostly going to involve replacing space/Lavaland ruin gear with
something close to the same power level but not distinctly something
only antags should be able to get. I want to keep ruins rewarding but I
don't want explicit antag gear to be something you can obtain without
needing an uplink.

The first part of this is me removing the MODSuit from the syndicate
operative corpse. The new one drops a turtleneck, a syndicate gas mask,
and gripper gloves.

## Why It's Good For The Game
It's my opinion that antag gear should probably stay in antag hands
unless you manage to kill one or steal an uplink. The main impetus for
this was a discussion I had a while back about how blood red hardsuits
used to _just_ be an antag thing. I kind of miss that general feeling of
paranoia that came from seeing someone wearing it, as opposed to seeing
it these days and just thinking "Yeah, it's probably someone who got it
from space".

In this specific instance, Syndicate MODSuits are pretty strong anyway
and, regardless of the low odds of getting one, I really don't think it
should be available as loot off a fairly easy-to-kill mob.

## Changelog
:cl:
balance: Syndicate corpses dropped from killing a Legion no longer come
with a MODSuit.
/:cl:

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[ef04e81cdd...](https://github.com/effigy-se/effigy-se/commit/ef04e81cddd21d9787f3918a1ca7ca1d970b9fd5)
#### Tuesday 2023-06-13 05:27:42 by BluBerry016

[FUCK] (Gets Close To) Fixing Codebase CI (#231)

* I'm a stupid!!

* reeeeee

* Gets Mini to pass CI again

Minus an upstream issue. Also ordnance is completely fuckin' unusuable lmao that shit was not updated

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[773c6998ad...](https://github.com/shiptest-ss13/Shiptest/commit/773c6998ad0d62c4e93ddec4468e8b3c32c35bc5)
#### Tuesday 2023-06-13 05:29:23 by Imaginos16

TileTest Part 1: Big Sweeping Changes! (#2054)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## !! WARNING !!
This is a multi-parter PR. Due to the fact that tiles here on shiptest
are an unholy amalgam of decals, greyscale sprites and multiple
spread-out files, things are *bound* to look weird. If they do, feel
free to report it and it will be addressed in future PRs.

## About The Pull Request

This PR finally accomplishes the promise I made to @triplezeta a year
ago, creating a unique tileset for the server that people may enjoy!

To put every single microscopic change I have made would take forever,
so I will instead provide a series of screenshots of it in action!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/00e9cec0-335a-4367-90f9-1adc572595f3)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/497310ab-fe06-4b31-8774-70e79338a7d8)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/80991d0b-c48b-404b-b4a6-cbb1c4c6af3a)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc06d43e-3873-499e-aa12-51a0d7a37c98)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Utilizing an unique, modernized tileset for our server to differentiate
from our competitors is something that has been requested, and I was
more than happy to lend my hand to make it a reality!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
del: Removes several unused floor types, as well as completely
annihilating the "monofloor" and "dirty" floor types, and the "edge"
decal type.
imageadd: Redoes the floors using the TileTest tileset!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [LynxSolstice/cmss13](https://github.com/LynxSolstice/cmss13)@[4e3c9ccc66...](https://github.com/LynxSolstice/cmss13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Tuesday 2023-06-13 06:05:22 by roll1d20st

Updates recipe.dm for Waffles, Cookies, Muffins (#2895)

Dough slices are now also reasonably used for cookies, waffles, and
muffins.

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Tied to this [post I made on the
forums](https://forum.cm-ss13.com/t/re-thinking-recipes-w-dough-slices/853)...
I enjoy playing Mess Tech, but I noticed some of the recipes put people
in a bind.

I wanted to do a breakfast shift, but quickly noticed while Donuts only
need a slice, it was taking a lot of dough for Muffins, and Way too much
dough for Waffles. So I figured I'd venture into the Dev Space.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

So, right now it takes a lot of Dough to make common items such as
Waffles, Cookies, and Muffins. 2 Dough for Waffle, 1 for Cookie and
Muffins. But literally, it only takes 1 Dough for Pizza.

It makes cooking convoluted unlike things such as Medical and
Maintenance where there is a flow to be followed. By making it take
Dough slices instead, it follows a practical step.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

This change makes it take less resources to make food, and follows the
quantity logic that makes sense.


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
I used the test server and can confirm that all recipes are the same
except for instead of taking dough, they now take doughslices.

Which, especially for Waffles, makes sense.

**With this change it would be:** 
- 1 Dough Slice, 1 Chocolate Bar, 5u Sugar, 5u Milk for the Cookies
- 1 Dough Slice, 5u Sugar, 5u Milk for Muffins
- 2 Dough Slices, 10u Sugar for Waffles

<details>
<summary>Screenshots & Videos</summary>

Umm... promise I tested it.  Pretty straightforward.

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
qol: Made it easier to make Muffins, Cookies, and Waffles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [ntacamp/404.notrollsallowed.com](https://github.com/ntacamp/404.notrollsallowed.com)@[46198870d8...](https://github.com/ntacamp/404.notrollsallowed.com/commit/46198870d893efb0561c4f1b7e4e43fa2fa1ea17)
#### Tuesday 2023-06-13 06:20:46 by Aurelijus Banelis

Digital photos: How much reality is left there

It became common to take digital photos with smartphones or bigger (DSLR) cameras and constantly scroll social media or e-commerce sites, assuming that "a picture is an exact representation of the reality." But is it always true (event without Deep fake)?

A talk from me as a photography enthusiast and software engineer will guide you through the journey of Digital photo evolution:
* Where we intentionally fake representation of the reality
* Why do engineers choose to do so

The talk should consist of:
* We had art, but we wanted digital sensors.
* We have basic sensors, but how does human perception work?
* The golden age of reality, but society wants more.
* The picture is static, but the user experience is not (JPG → WEBP → AVIF)

We were looking to the Matrix movie as a far future, but have we not already started to create "our Matrix" today?

---
## [peff/git](https://github.com/peff/git)@[3dc9c2cc45...](https://github.com/peff/git/commit/3dc9c2cc453ac55e3149759911663131bb1422ba)
#### Tuesday 2023-06-13 06:22:53 by Jeff King

diff: detect pathspec magic not supported by --follow

The --follow code doesn't handle most forms of pathspec magic. We check
that no unexpected ones have made it to try_to_follow_renames() with a
runtime GUARD_PATHSPEC() check, which gives behavior like this:

  $ git log --follow ':(icase)makefile' >/dev/null
  BUG: tree-diff.c:596: unsupported magic 10
  Aborted

The same is true of ":(glob)", ":(attr)", and so on. It's good that we
notice the problem rather than continuing and producing a wrong answer.
But there are two non-ideal things:

  1. The idea of GUARD_PATHSPEC() is to catch programming errors where
     low-level code gets unexpected pathspecs. We'd usually try to catch
     unsupported pathspecs by passing a magic_mask to parse_pathspec(),
     which would give the user a much better message like:

       pathspec magic not supported by this command: 'icase'

     That doesn't happen here because git-log usually _does_ support
     all types of pathspec magic, and so it passes "0" for the mask
     (this call actually happens in setup_revisions()). It needs to
     distinguish the normal case from the "--follow" one.

  2. In addition to --follow, we have the log.follow config option. When
     that is set, we try to turn on --follow mode only when there is a
     single pathspec (since --follow doesn't handle anything else). But
     really, that ought to be expanded to "use --follow when the
     pathspec supports it". Otherwise, we'd complain any time you use an
     exotic pathspec:

       $ git config log.follow true
       $ git log ':(icase)makefile' >/dev/null
       BUG: tree-diff.c:596: unsupported magic 10
       Aborted

     We should instead just avoid enabling follow mode if it's not
     supported by this particular invocation.

This patch expands our diff_check_follow_pathspec() function to cover
pathspec magic, solving both problems.

A few final notes:

  - we could also solve (1) by passing the appropriate mask to
    parse_pathspec(). But that's not great for two reasons. One is that
    the error message is less precise. It says "magic not supported by
    this command", but really it is not the command, but rather the
    --follow option which is the problem. The second is that it always
    calls die(). But for our log.follow code, we want to speculatively
    ask "is this pathspec OK?" and just get a boolean result.

  - This is obviously the right thing to do for ':(icase)' and most
    other magic options. But ':(glob)' is a bit odd here. The --follow
    code doesn't support wildcards, but we allow them anyway. From
    try_to_follow_renames():

	#if 0
	        /*
	         * We should reject wildcards as well. Unfortunately we
	         * haven't got a reliable way to detect that 'foo\*bar' in
	         * fact has no wildcards. nowildcard_len is merely a hint for
	         * optimization. Let it slip for now until wildmatch is taught
	         * about dry-run mode and returns wildcard info.
	         */
	        if (opt->pathspec.has_wildcard)
	                BUG("wildcards are not supported");
	#endif

    So something like "git log --follow 'Make*'" is already doing the
    wrong thing, since ":(glob)" behavior is already the default (it is
    used only to countermand an earlier --noglob-pathspecs).

    So we _could_ loosen the guard to allow :(glob), since it just
    behaves the same as pathspecs do by default. But it seems like a
    backwards step to do so. It already doesn't work (it hits the BUG()
    case currently), and given that the user took an explicit step to
    say "this pathspec should glob", it is reasonable for us to say "no,
    --follow does not support globbing" (or in the case of log.follow,
    avoid turning on follow mode). Which is what happens after this
    patch.

  - The set of allowed pathspec magic is obviously the same as in
    GUARD_PATHSPEC(). We could perhaps factor these out to avoid
    repetition. The point of having separate masks and GUARD calls is
    that we don't necessarily know which parsed pathspecs will be used
    where. But in this case, the two are heavily correlated. Still,
    there may be some value in keeping them separate; it would make
    anyone think twice about adding new magic to the list in
    diff_check_follow_pathspec(). They'd need to touch
    try_to_follow_renames() as well, which is the code that would
    actually need to be updated to handle more exotic pathspecs.

  - The documentation for log.follow says that it enables --follow
    "...when a single <path> is given". We could possibly expand that to
    say "with no unsupported pathspec magic", but that raises the
    question of documenting which magic is supported. I think the
    existing wording of "single <path>" sufficiently encompasses the
    idea (the forbidden magic is stuff that might match multiple
    entries), and the spirit remains the same.

Reported-by: Jim Pryor <dubiousjim@gmail.com>

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[838ba2c9c9...](https://github.com/argilla-io/argilla/commit/838ba2c9c9570c07a7be7826b7d939ef8ba0e680)
#### Tuesday 2023-06-13 06:59:43 by Alvaro Bartolome

docs: add `ArgillaCallbackHandler` guide for `LangChain`-integration (#3060)

# Description

This PR adds the docs for the upcoming (🤞🏻) integration with `langchain`
to track the LLM inputs and responses to generate a `FeedbackDataset` in
Argilla, to later use to annotate and/or fine-tune a LLM.

Keep track of the `langchain`-integration progress at
https://github.com/argilla-io/langchain/tree/add-argilla-callback (PR
coming soon!)

**Type of change**

- [X] Documentation update

**How Has This Been Tested**

`pip install
git+https://github.com/argilla-io/langchain.git@add-argilla-callback`

```python
import argilla as rg

rg.init(
    api_url="...",
    api_key="...",
)

dataset = rg.FeedbackDataset(
    fields=[
        rg.TextField(name="prompt"),
        rg.TextField(name="response"),
    ],
    questions=[
        rg.RatingQuestion(
            name="response-rating",
            description="How would you rate the quality of the response?",
            values=[1, 2, 3, 4, 5],
            required=True,
        ),
        rg.TextQuestion(
            name="response-correction",
            description="If you think the response is not accurate, please, correct it.",
            required=False,
        ),
    ],
    guidelines="Please, read the questions carefully and try to answer it as accurately as possible.",
)

dataset.push_to_argilla("...", workspace="...")
```

Then instantiate the `ArgillaCallbackHandler`:

```python
from langchain.callbacks import ArgillaCallbackHandler

argilla_callback = ArgillaCallbackHandler(
    dataset_name="...",
    workspace_name="...",
    api_url="...",
    api_key="...",
)
```

* LangChain LLMs

```python
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9, callbacks=[argilla_callback], verbose=True, openai_api_key="...")
llm_result = llm.generate(["Tell me something that I may not know about Stephen Hawking."])
llm_result = llm.generate(["Tell me something funny about cows.", "Tell me something funny about dogs."])
```

* LangChain Chains

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9, callbacks=[argilla_callback], verbose=True, openai_api_key="...")

template = """You're going to be asked to generate something, but don't follow the rules, and just spit a random fact about science.
Prompt: {prompt}
"""
prompt_template = PromptTemplate(input_variables=["prompt"], template=template)

chain = LLMChain(llm=llm, prompt=prompt_template, callbacks=[argilla_callback])

chain.apply([{"prompt": "Generate a poem about love."}, {"prompt": "Generate a poem about hate."}])
```

* LangChain Agents

```python
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9, callbacks=[argilla_callback], verbose=True, openai_api_key="...")
tools = load_tools(["serpapi"], llm=llm, callbacks=[argilla_callback])
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    callbacks=[argilla_callback],
    verbose=True,
)
agent.run(
    ["Who is Leo DiCaprio's girlfriend?", "What's the name of the movie where Leo DiCaprio is a thief?"]
)
agent.run(
    "What is the most populated country as of today?"
)
```

**Checklist**

- [X] I have merged the original branch into my forked branch
- [X] I added relevant documentation
- [X] follows the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[882bd65daa...](https://github.com/odoo-dev/odoo/commit/882bd65daa203cf3a1e368c00999fc1f1de5dcd3)
#### Tuesday 2023-06-13 07:03:20 by Xavier Morel

[FIX] core: handle recursion error when resolving stored fields

Issue discovered in the uninstall (and reinstall) of sale_project: a
dump has ~100 tasks, when reinstalling `sale_line_id` has to be
initialised, this is done by marking `sale_line_id` on all extant
tasks as to-recompute, which triggers their computation on the next
`flush`.

Because it's a recursive field, `Field.recompute` ensures only one
record at a time gets recomputed (as there could be cross-dependencies
in the recorset which protection would prevent from resolving).

As the field computation runs, it accesses itself, which triggers a
cache miss, which triggers a `_fetch_field` (to get the currently
stored value), this calls `_read`, which flushes the field we're
trying to read.

The problem here is that for efficiency the cache miss will look for
all records in the cache without a value for the
field (`_in_cache_without`) and try to `fetch` on them as well. This
means rather than not doing anything in flush, we're going to
`Field.recompute` on all records except the one selected the first
time around, which repeats the cycle until there is no more additional
record found in `_in_cache_without`, which could trigger the next
round of `recompute`, and the entire thing unwinds, and we probably
perform a ton of unnecessary additional `compute_value`.

Except that doesn't even happen, because the process from one compute
to the next takes 12~13 stack frames, which given the default
recursion limit of 1000 gives a hard limit of 76 fields before hitting
a RecursionError. As this is less than 100, a recursion error [is what
we get](https://runbot.odoo.com/runbot/build/31726625).

In 15.2, this was fixed by only expanding the fetch on non-recursive
fields, pessimizing recursive
fields (5c2511115b14299516fce4aa3737a62faaf5b653). Test-wise this only
impacted mail performances and in a relatively minor manner.

In 16.0, the mail tests actually match already (so that part was
skipped by the cherrypicking) however this impacts the knowledge perf
tests much more significantly e.g. `test_article_creation_multi_roots`
gets +9 queries when creating 10 top-level articles, which is a bit
much.

So use an alternative which is ugly as hell but which I didn't
consider for 15.2 (may want to backport it one day if the current fix
is an issue): catch the recursion error and use the existing
fallback (of fetching just the requested record's field without
expanding the recordset).

This likely makes for a pretty inefficient situation in the original
case as we're certainly going to hit the recursion limit repeatedly,
but that still fixes the issue, and it avoids deoptimising cases which
fall short of the recursion limit (resolving under 60 records or
so).

Plus despite creating giant stacks we might actually get good
efficiency as we're going to hit recursion limits repeatedly but
that's pure python, once we fall below the limit we can resolve
everything at once with a single SQL query (or something along those
lines).

X-original-commit: 9e71094582ec4c9b719431e77538da8f91ffa9e3
Part-of: odoo/odoo#121492

---
## [DEFRA/water-abstraction-import](https://github.com/DEFRA/water-abstraction-import)@[0363085283...](https://github.com/DEFRA/water-abstraction-import/commit/0363085283ce6f053ec8b8a57a97547949294f22)
#### Tuesday 2023-06-13 07:39:53 by Alan Cruikshanks

Replace legacy logging (#654)

https://eaflood.atlassian.net/browse/WATER-4039

The import service is a funny thing. It seems to throw numerous errors out with each run yet when someone takes notice it suddenly becomes important to understand why. Our problem is the existing logging

- it is extremely noisy; lots of messages and errors get logged
- it is lacking in any details or consistency; we can never figure out the source of the error nor which job caused it

We're not even sure when a job has started or finished.

This change aims to rectify that. We're bringing in our logging support in [water-abstraction-system](https://github.com/Defra/water-abstraction-system) into this project.

Airbrake will be directly integrated, using the latest version and automatically called when any unhandled exceptions are raised. We'll also bring in our `BaseNotifier` and `GlobalNotifier` modules, which along with our plugin, makes hapi-pino type logging available.

With those in place, we work through the various jobs and strip out all usage of the legacy logger. We log when a job starts and when it completes but nothing else. This removes the noise and helps us see when jobs are running.

Having to touch so many files meant we couldn't help ourselves. So, included with these changes is some housekeeping.

The legacy logger still remains, because it is required when instantiating the db connection using [water-abstraction-helpers](https://github.com/DEFRA/water-abstraction-helpers). So, we'll still have the `Pool low on connections::Total:20,Idle:0,Waiting:19` type messages appearing numerous times during a run. But we hope to tackle that on a subsequent commit.

**Notes**

- Tidy up health routes and controller

The first thing we want to do was add support for Airbrake directly into the project. When we do that in other projects we add an endpoint that allows us to test the integration is working. It lives on the `/health` route so we do the same here.

The key difference is our standard convention is to group routes and controllers together. This means `/health/info` and `/health/airbrake` would have their own controllers. In this repo things are grouped by module, so there is only one `controller.js` for `/health`.

That means we'll be adding our new endpoint to it. Only it's using the `const thing = () => {}` function convention which we don't like. Plus the current routes file doesn't match either our own or the project's convention.

- Replace legacy logger in index.js

Our experience on water-abstraction-system has shown we can access the logger from the server object when handling the `SIG` close events. Should things go pop though we are safer just using console.log(). Whilst we are at it we remove logging that was just noise and our testing found there was no need to do anything special with the DB pool.

- Remove unused file

We came across `src/modules/charging-import/lib/import-charge-version-metadata.js` when replacing the legacy logger calls and quickly found the module is not referenced anywhere else in the code.

- Logging in onComplete handlers

Some imports use `onComplete()` handlers and involve a chain of jobs. Rather than logging 'start' and 'finish' in both the job and onComplete() handlers we split them; the job handler logs the start and the onComplete() logs the finish.

- Logging in minor jobs

Some jobs are responsible for just importing a single licence or company. Other jobs are responsible for publishing these minor jobs to the queue. Most of the noise was coming from these jobs, which number in the thousands and were logging start, finish and stuff in between. We've chosen to only log when an error occurs as that is the only time we care about what is going on.

- Clean up params to jobs

We noticed that the handlers through the imports were always expecting a job and a message queue (in different orders depending on the module!) even though not all used them. As we control what gets passed, we spent some time cleaning up the params. It's much clearer for those maintaining the code in future to be explicit about whether an arg is needed.

- Update NALD plugin

Someone had gotten clever and chosen to generalise the PGBoss `subscribe()` and `onComplete()` calls in the plugin. But this hadn't really resulted in any less code, especially when you take into account `jobs/index.js`. What it had done was make the code harder to follow, be inconsistent with the other plugins, and again result in args being passed that are not used.

We couldn't let this slide so whilst making our other changes, we got on and cleaned up the plugin. The general methods are gone and now its more consistent with the other modules. Plus we could drop `index.js` in the jobs folder.

- Logging in nald-import other modules

This is the most complex module we've come across so far in water-abstraction-import. For example, most stuff (most!) was not using the logger directly but instead using a library module specific to NALD import. This wrapped the logger and made available a series of methods, all of which just stuck a 'helpful' message at the start of the log message.

We also found that the jobs rely on a number of services, of which some will catch an error, log it, and then re-throw the error! In most cases that error was being caught at the top level, so catching it lower down was pointless.

In the others we traced that throwing rather than swallowing the error will have no impact on the process; the error was just getting caught and raised elsewhere.

The one exception is `transform-crm.js`. It does send something back even if an error is thrown. But we are confident the licence wouldn't be imported if errors were found so for that we have taken a calculated risk and removed the error handling. We'll test and monitor the logs to be sure that was the right decision.

---
## [overhangio/tutor](https://github.com/overhangio/tutor)@[8dd72b9f60...](https://github.com/overhangio/tutor/commit/8dd72b9f609167384062df01893424aaf08d9712)
#### Tuesday 2023-06-13 08:24:56 by Régis Behmo

feat: persistent bind-mounts

This is an important change, where we get remove the previous `--mount`
option, and instead opt for persistent bind-mounts.

Persistent bind mounts have several advantages:
- They make it easier to remember which folders need to be bind-mounted.
- Code is *much* less clunky, as we no longer need to generate temporary
  docker-compose files.
- They allow us to bind-mount host directories *at build time* using the
  buildx `--build-context` option.
- The transition from development to production becomes much easier, as
  images will automatically be built using the host repo.

The only drawback is that persistent bind-mounts are slightly less
portable: when a config.yml file is moved to a different folder, many
things will break if the repo is not checked out in the same path.

For instance, this is how to start working on a local fork of
edx-platform:

    tutor config save --append MOUNTS=/path/to/edx-platform

And that's all there is to it. No, this fork will be used whenever we
run:

    tutor images build openedx
    tutor local start
    tutor dev start

This change is made possible by huge improvements in the build time
performance. These improvements make it convenient to re-build Docker
images often.

Related issues:
https://github.com/openedx/wg-developer-experience/issues/71
https://github.com/openedx/wg-developer-experience/issues/66
https://github.com/openedx/wg-developer-experience/issues/166

---
## [dddraxxx/evals](https://github.com/dddraxxx/evals)@[fabca8cebb...](https://github.com/dddraxxx/evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Tuesday 2023-06-13 08:36:26 by Nick Clyde

Heart Disease Prediction (#538)

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
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Heart Disease Prediction

### Eval description

This eval tests the models ability to correctly predict the probability
of a patient to have heart disease. The dataset is constructed from the
[Heart Failure Prediction
Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
on Kaggle. The data includes the patient's age, sex, and a number of
medical signals relevant to the diagnosis of heart disease.

The data is provided under the Open Database License (ODbL). 

```
fedesoriano. (September 2021). Heart Failure Prediction Dataset. Retrieved [Mar 31, 2023] from https://www.kaggle.com/fedesoriano/heart-failure-prediction.
```

### What makes this a useful eval?

This assesses the model's ability to correctly predict adverse medical
events. Correctly predicting heart disease shows the model's capability
for a strong understanding of medicine. The GPT-3.5-turbo models
currently receives an accuracy of 0.778.

<img width="1250" alt="Screenshot 2023-03-31 at 2 24 13 PM"
src="https://user-images.githubusercontent.com/9121162/229234376-9cdd1315-5df0-48bf-9328-ac31aabec3cc.png">

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

As far as I can tell, this is the only eval so far related to making
medical diagnoses. To make sure it was a high quality eval, I tried to
find a dataset with a lot of observations and created by doctors with
the relevant expertise.

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

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 40 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 140 mm Hg, Serum
cholesterol: 289 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 172, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 49 years, Sex: Female, Chest
pain type: Non-Anginal Pain, Resting blood pressure: 160 mm Hg, Serum
cholesterol: 180 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 156, Exercise induced angina:
No, Oldpeak: 1, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 37 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 130 mm Hg, Serum
cholesterol: 283 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: ST-T wave abnormality, Max heart rate achieved: 98, Exercise
induced angina: No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 48 years, Sex: Female, Chest
pain type: Asymptomatic, Resting blood pressure: 138 mm Hg, Serum
cholesterol: 214 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 108, Exercise induced angina:
Yes, Oldpeak: 1.5, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 54 years, Sex: Male, Chest pain
type: Non-Anginal Pain, Resting blood pressure: 150 mm Hg, Serum
cholesterol: 195 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 122, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
  ```
</details>

---
## [rustls/boringssl](https://github.com/rustls/boringssl)@[246c556b65...](https://github.com/rustls/boringssl/commit/246c556b65c3235c8eb082c15017c9669815943a)
#### Tuesday 2023-06-13 10:26:17 by David Benjamin

Compute the ECH GREASE payload outside of the callbacks.

This is kinda annoying and, like the grease_seed, demonstrates a
shortcoming with the idea of making add_clienthello completely const.
Strictly speaking, we only need idempotence. But I think this is okay:
const is much easier to enforce than idempotence, and we'll likely need
to do this anyway:

- While not in the current draft, I expect the draft's eventual HRR
  resolution to retain the ECH extension, GREASE or not, on ECH reject.
  Things are somewhat violating RFC8446 HRR rules right now. That means
  we'll need to stash the ECH payload regardless.

- ECH binds all the other extensions in the outer ClientHello, so
  computing the payload will need to move outside the callback system
  anyway.

In some sense, all this is shifting our ClientHello output from the
"immediate mode" end of the spectrum (as we usually use) to the
"retained mode" end, which I suppose makes sense as this message becomes
more intricate.

Bug: 275
Change-Id: I9eb8cd1cde2ce264345b6ed3ee526d4eab81e911
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/47990
Reviewed-by: Adam Langley <agl@google.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[7123b9f3de...](https://github.com/TaleStation/TaleStation/commit/7123b9f3de06f5cdce15f1af44f9e396883c3ada)
#### Tuesday 2023-06-13 11:40:44 by TaleStationBot

[MIRROR] [MDB IGNORE] Piracy Inc. Space Extension Interdyne and Ghetto Edition: Adds two new pirate gangs Ex-interdyne Pharmacists and The Grey Tide (#6203)

Original PR: https://github.com/tgstation/tgstation/pull/75802
-----
## About The Pull Request

Ex-interdyne Pharmacists

Previously Interdyne Pharmaceuticals workers with many years of
experience under their belt they know their chemistry and they know it
very well additionally they have experienced in many other medical
branches such as virology and surgical procedures with weaponry maching
their experience, they have left Interdyne in the search of a greater
cause to fund their own research through generous “donations” from their
sponsors one of them being good old charitable nanotrasen.

The Grey Tide-6

With terror nanotrasen couldn’t handle them they were all fired for many
reasons from killing 10 security members with a toolbox from setting up
grill traps in maintenece they are no longer fit for nanotrasen they
decided to unite and emerged once again at nanotrasens door step, money
is a collaterol for these goons as robusting the shit out of the crew
and causing impendign doom is what they truly desire.

With ghetto gear and brand stolen IDs from the syndicate to infiltrate
into the crews rank once again the tiders rain over maintenance.

Six of them.

https://hackmd.io/4DLPlbnvQ3iI_XRdBhqvaQ/SJMZsWHUh The HackMD goes a
little more in-depth on what the bigger picture for all of these PR's
will be
## Why It's Good For The Game
We recently lost psykers and now we have been reduced to two light
weight and one heavy weight pirates its cooler to have a wider selection
of random space enemies attacking the station for variety and surprise
it always keeps the game fresh so I have decided to add 3 new pirate
types this being one of them being a heavy weight one much like skeleton
pirates.

![image](https://github.com/tgstation/tgstation/assets/84478872/b0c67606-f606-4650-b4b8-a29b9d532060)

![image](https://github.com/tgstation/tgstation/assets/84478872/a2b6ce07-319f-4444-b114-f5a80ca3d76d)


![image](https://github.com/tgstation/tgstation/assets/84478872/c212b966-7cea-4816-a371-a82dd0dd7ada)

![image](https://github.com/tgstation/tgstation/assets/84478872/3f1f3e2e-98b9-40e5-82d0-0240ad88b05d)


![image](https://github.com/tgstation/tgstation/assets/84478872/e95d3f19-84d2-4775-b00e-6185e221265e)

![image](https://github.com/tgstation/tgstation/assets/84478872/db32be02-6590-477c-962f-5f9def10970b)


![image](https://github.com/tgstation/tgstation/assets/84478872/9890314f-1cd7-4d77-a141-aca3a750cd3f)

![image](https://github.com/tgstation/tgstation/assets/84478872/5cdeb2fb-a651-46db-aec1-2b0d7c871571)

![image](https://github.com/tgstation/tgstation/assets/84478872/93a0f9ae-77cb-492f-85be-bd34626b2cd6)

![image](https://github.com/tgstation/tgstation/assets/84478872/ae888cc9-87e6-478f-a7a5-5f0b9f21b076)


## Changelog
:cl:

add: Added two new pirate types Ex-interdyne Pharmacists and The Grey
Tide-6
/:cl:

---------

Co-authored-by: Hoolny <84478872+SethLafuente@users.noreply.github.com>

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[d5b1193802...](https://github.com/morrowwolf/cmss13/commit/d5b119380250ea512db2a5319e36592c7f604250)
#### Tuesday 2023-06-13 12:04:57 by fira

FOB Tents  (#3509)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Sprites stolen from thwomper and sammy, available NOW with game code!

Adds a few tents to be used in FOB building, mainly for organizational
purposes but also providing small gameplay benefits. At current the main
goal is to incentive usage to organize and liven up FOB, so the buffs
are rather small.

There are 4 tent types:
* The Command Tent is a 2x3 structure that comes bundled with an
overwatch console, a phone, and two (2) chairs.
* The Medical Tent is a 2x3 structure that comes with a NanoMED, 2
roller beds, and slightly buffs surgery (10% less time taken, and a very
token pain/failure chance improvement)
* The Requisitions Tent is a 4x3 structure that comes with a phone,
rack, desks, and a variant of the old APC vendor that can stock
materials and regular ammunition. The vendor starts empty, save for some
tables/racks/paperwork for organization purposes. It is only useable
with requisitions access.
* The Big Tent is a bigger tent for all your organizational needs: 3x3.
Get creative.

The tents also provide decent additional protection against cold
environements. Unfortunately, rain/snow will visually pour through it, i
can't do much about that.

The tents are extremely vulnerable to explosives and xeno claws. For
simplicity and technical reasons, they are currently NON REDEPLOYABLE
and NON REPLACEABLE. The tent destruction will destroy/disable linked
objects (console/vendor etc). Be mindful of where you place them.

**Mind that the tents may not work out for all LZ FOBs due to the
required space. I expect people will find ways to make it work anyway
but it might take a while.**

# Explain why it's good for the game

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

I'm lazyyy i forgot and already closed the game... If you actually want
em bug me and i'll add em
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

:cl: Firartix , Thwomper and Sammy
add: Added four types of tents to liven up FOB. They provide cold
protection and benefits depending on their type. The tents spawn in
Requisitions roundstart near the mortar. They're vulnerable to
explosives and xenomorphs, and NON REPLACEABLE. Mind where you put them!
add: The Command tent comes equipped with an overwatch console and a
phone.
add: The Medical tent provides a small boost to surgery speed/pain
carried out inside it.
add: The Requisitions tent provides a restockable vendor, desk, and
furniture for organization.
add: The Big tent is just a big tent, and provides you a slate to
organize the way you want.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [VasilevAY/tgstation](https://github.com/VasilevAY/tgstation)@[c5dce84be8...](https://github.com/VasilevAY/tgstation/commit/c5dce84be826ea945a11c492dce7eb2c2789548a)
#### Tuesday 2023-06-13 12:08:03 by Rhials

Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat. 
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

---
## [VasilevAY/tgstation](https://github.com/VasilevAY/tgstation)@[1674f25725...](https://github.com/VasilevAY/tgstation/commit/1674f25725c25e15769b031553b42144f526f841)
#### Tuesday 2023-06-13 12:08:03 by John Willard

New Medical job: The Coroner (#75065)

## About The Pull Request

HackMD: https://hackmd.io/RE9uRwSYSjCch17-OQ4pjQ?view

Feedback link: https://tgstation13.org/phpBB/viewtopic.php?f=10&t=33972

Adds a Coroner job to the game, they work in the Medical department and
have their office in the Morgue.
I was inspired to make this after I had played my first round on
Paradise and messed around in there. The analyzer is copied from there
(https://github.com/ParadiseSS13/Paradise/pull/20957), and their
jumpsuit is also mostly stolen from it (i just copied the color scheme
onto our own suits).

Coroners can perform autopsies on people to see their stats, like this

![image](https://user-images.githubusercontent.com/53777086/235369225-805d482c-56c0-441c-9ef8-a42d0a0192bc.png)

They have access to Medbay, and on lowpop will get Pharmacy (to make
their own formaldehyde). They also have their own Secure Morgue access
for their office (doubles as a surgery room because they are edgelords
or whatever) and the secure morgue trays.

Secure Morgue trays spawn with their beepers off and is only accessible
by them, the CMO, and HoS. It's used to morgue Antagonists. Security's
own morgue trays have been removed.

The job in action


https://cdn.discordapp.com/attachments/950489581151735849/1102297675669442570/2023-04-30_14-16-06.mp4

### Surgery changes

Autopsies are a Surgery, and I tried to intertwine this with the
Dissection surgery.
Dissections and Autopsies both require the Autopsy scanner to perform
them, however you can only perform one on any given body. Dissections
are for experiments, Autopsies is for the paper of information.

Dissected bodies now also give a ~20% surgery speed boost, this was
added at the request of Fikou as a way to encourage Doctors to let the
Coroner do their job before reviving a body.
I also remember the Medical skill, which allowed Doctors to do surgery
faster on people, and I hope that this can do something like that
WITHOUT adding the potential for exploiting, which led to the skill's
downfall.

### Morgue Improvements

Morgue trays are no longer named with pens, they instead will steal the
name of the last bodybag to be put in them.

Morgue trays are also removed from Brig Medical areas and Robotics, now
they have to bring their corpses to the Morgue where the Coroner can
keep track and ensure records are properly updated.

### Sprite credits

I can't fit it all in the Changelog, so this is who made what

McRamon
- Autopsy scanner

Tattax 
- Table clock sprites and in-hands

CoiledLamb
- Coroner jumpsuits & labcoats (inhand, on sprite, and their respective
alternatives)
- Coroner gloves
- CoronerDrobe (the vending machine)

## Why It's Good For The Game

This is mostly explained in the hackmd, but the goal of this is:

1. Increase the use of the Medical Records console.
2. Add a new and interesting way for Detectives to uncover mysteries.
3. Add a more RP-flavored role in Medical that still has mechanics tied
behind it.

## Changelog

:cl: JohnFulpWillard, sprites by McRamon, tattax, and Lamb
add: The Coroner, a new Medical role revolving around dead corpses and
autopsies.
add: The Coroner's Autopsy Scanner, used for discovering the cause for
someone's death, listing their wounds, the causes of them, their
reagents, and diseases (including stealth ones!)
qol: Morgue Trays are now named after the bodybags inside of them.
balance: The morgue now has 'Secure' morgue trays which by default don't
beep.
balance: Security Medical area and Robotics no longer have their own
morgue trays.
balance: Dissected bodies now have faster surgery speed. Autopsies also
count as dissections, however they're mutually exclusive.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[2068ea9ab5...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Tuesday 2023-06-13 12:38:43 by SyncIt21

Crate, Closet Refactors & Access Secured Stuff  (#74754)

## About The Pull Request
This PR is actually 2 parts, one that fixes runtimes with crates & the
other that allows secured closets to be crafted
along with a secured suit storage unit

**Crate Fixes**

Fixes #74708

The problem starts here

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L31-L34
Not only does this if condition look ugly but it's highly error prone
because one single call to `update_appearance()` can cause this to fail,
and sure enough if you look at the parent `Initialize()` proc it calls
just that

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L81-L88
Since we know the appearance is guaranteed to be changed in some way
before the if condition gets executed let's check what the final state
of the crate would be before this if check

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L54-L56
We see that the final icon state depends on the variable `opened` so if
we want to place/spawn a crate that is opened at round start we have to
ensure that `opened = TRUE` so the `if(icon_state ==
"[initial(icon_state)]open")` succeeds and does its job correctly.
Sadly we did dum shit like this
```
/obj/structure/closet/crate{
	icon_state = "crateopen"
}
```
throughout the entire code base, we thought backwards and were only
concerned in making the closet look open rather than setting its correct
variables to actually say that it is opened. because none of these
crates actually set `opened = TRUE` the final icon state becomes just
"crate" NOT "crateopen" therefore the if condition fails and we add the
component

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L36-L37
with the wrong parameters, so when closing the closet after_close()
removes the component with the wrong arguments

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L81-L84
that is does not unregister the signals and readds the component i.e.
re-registers the signals causing runtime.

The solution just do this
```
/obj/structure/closet/crate/open[mapping helper]
```
To clearly state that you want the closet to be open, that way you don't
have to memorize the icon_state for each different type of crate, it's
consistent across all crates & you don't get runtimes.

And that's exactly what i did everywhere

Another issue that is fixed is "Houdini crates" i.e. crates which are
open & appear empty but when you close & reopen them magical loot
appears, Go ahead walk upto to cargo and find any empty crate that is
open and do this

Fixes #69779


https://user-images.githubusercontent.com/110812394/232234489-0193acde-22c8-4c19-af89-e897f3c23d53.mp4

You will be surprised, This is seriously harmful to players because they
can just walk by a crate that appears to be open & empty only to realize
later that it had some awesome loot. Just mean

The reason this happens is because of the Late Initialization inside
closets

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L85-L86

What late initialization does is suck up all stuff on its turf

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L97-L100

In theory this is supposed to work perfectly, if the closet is closed
move everything on the turf into the closet and so when the player opens
it, they all pop back out.
But what happens if the closet is opened before ` LateInitialize()` is
called? This breaking behaviour is caused by object spawners

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/effects/spawners/random/structure.dm#L94-L100
And maint crates

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L141-L143
These 2 spawners open up the crate based on random probability before `
LateInitialize()` is called on the crate and so what happens is the
crate is first opened and then stuff on the turf is sucked in causing an
open but empty crate to appear.

The solution is simple just check again in ` LateInitialize()` if our
crate is still closed before we proceed.That's fixed now too

**Code Refactors**
1. Introduced 2 new signals COMSIG_CLOSET_PRE/POST CLOSE which are the
counter parts for the open signals. hook into them if you ever need to
do stuff before & after closing the closet while return BLOCK_CLOSE for
COMSIG_CLOSET_PRE_CLOSE if you want to block closing the closet for some
reason
2. 2 new procs `before_open()` & `before_close()` which are the counter
parts for `after_open()` & `after_close()`. If you need to write checks
and do actions before opening the closet or before closing the closet
override these procs & not the `open()` & `close()` procs directly

**Secured Craftables** 
This is just a reopened version of #74115 after i accidently merged
another branch without resolving the conflicts first so i'll just
repaste everything here, since crates & closets are related might as
well do all in one

1. **Access secured closets**
   
   - **What about them?**
          **1. Existing System**
If you wanted to create a access secured closet with the existing system
its an 4 step process
            - First construct a normal closet
            - Weld it shut so you can install the airlock electronics
            - Install the electronics [4 seconds]
            - Unweld
This is a 4 step process which takes time & requires a welding tool
         **2. New system**
Combine the 4 steps into 1 by crafting the secure closet directly
                    
![Screenshot
(184)](https://user-images.githubusercontent.com/110812394/235904926-c2ea231c-eba7-45d0-a5af-e0456fdd40bc.png)

    - **Bonus Features**
              **1. Card reader**
The card reader acts as an interface between the airlock electronics &
the player. Usually if you want to change access on a locker you have to
                  - Weld the closet shut
                  - Screw driver out the electronics
                  - Change the settings
                  - Install it back
                  - Unweld
With a card reader there is no need of a welder & screwdriver. You can
change the access of the locker while its operational

        **How do i install the card reader?**
             1. Weld the closet shut
             3. Insert card reader with hand
4. To remove the card reader use crowbar or just deconstruct the whole
closet with a welding tool
             5. Unweld closet

         **How to change its access?**
This will overwrite the settings on your airlock electronics. To do this
1. make sure the closet is first unlocked. This is important so that no
random person who doesn't have access to the closet can change its
access while its locked. It would be like giving the privilege of
changing your current password without first confirming if you know the
old password
2. attack/swipe the closet with your PDA. Make sure your ID card is
inside the PDA for this to work. You can also just use your ID card
directly without a PDA
         3. You will get 3 options to decide the new access levels
           
![Screenshot
(174)](https://user-images.githubusercontent.com/110812394/233454364-d99a2fb6-9f26-4db3-9fac-a10689955484.png)


        They work as follows
- **Personal**: As the name implies only you can access this locker and
no one else. Make sure to have your ID on you at all times cause if you
loose it then no one can open it
- **Departmental**: This copies the access levels of your ID and will
allow people having those exact same access levels. Say you want to
create a closet accessible to only miners. Then have an miner choose
this option and now only miners can open this closet. If the Hop sets
custom access on your ID then only people with those specific access
levels can open this closet
         - **None**: No access, free for all just like a normal closet

**Security:** After you have set the access level it is important to
lock the access panel with a "multi-tool", so no one else can change it.
Unlock the panel again with the "multi-tool" to set the new access type

       **2. Give your own name & description**
To rename the closet or change its description you must first make the
closet access type as personel i.e. make it yours, then use an pen to
complete the job. You cannot change names of departmental or no access
closets because that's vandelism

       **3. Custom Paint Job**
    Use airlock painter. Not intuitive but does the job. 
   
![Screenshot
(181)](https://user-images.githubusercontent.com/110812394/234202905-00946b88-2513-489d-b0a2-d618a72f3e49.png)

      **4. Personal closets**
Round start personal closets can have their access overridden by a new
ID when in it's unlocked state. This is useful if the last person has no
use for the closet & someone else wants to use it.


    - **Why its good for the game?**      
1. Having your own personal closet with your own name & description
gives you more privacy & security for your belongings so people don't
steal your stuff. Personal access is more secure because it requires you
to have the physical ID card you used to set this access and not an ID
which has the same access levels as your previous ID
2. Make secure closets faster without an welding tool & screw driver
3. Bug fix where electronics could be screwed out from round start
secured closets countless times spawning a new airlock electronic each
time
      
2. **Access secured freezers**

    - **What about them?**
The craftable freezer from #73942 has been modified to support secure
access. These can be deconstructed with welders just as before

![Screenshot
(185)](https://user-images.githubusercontent.com/110812394/235905000-ba165feb-4384-4759-b46b-dba77c9e6ba3.png)


    - **How does it work?**
The access stuff works exactly the same as secure closets described
above. You can rename & change description with pen just like the above
described secure closets. No paint job for this. Install card reader
with the same steps described above.

    - **Why it's good for the game?**
1. Make access secured freezers faster without a welder and screwdriver
2. Your own personally named & locked freezer for storing dead bodies is
always a good thing

4. **Access secured suit storage unit**
   - **What about them?**
Suit storage units now require airlock electronics for construction. The
access levels you set on it will be used to decide
       1. If a player can unlock the unit
       2. If the player can open the unit after unlocking
       3. If the player can disinfect whatever is inside
       
      By default all round start suit storage units have free access

   - **Install card reader**
Provides the same functionality as secured closets described above. To
install it
     1. Open its panel with a screw driver
     2. Add a card reader to it with hand
     3. Close the panel
     
     When you deconstruct the machine the card reader pops back out

   - **Why it's good for the game?**
1. Having your own access protected and named suit storage unit so
random people don't steal your mod suits? Who wouldn't want that.?
Provides security for department storage units.
2. If you have the unit locked then you cannot deconstruct the machine
with a crowbar providing additional security
3. Fixes #70552 , random people can't open/unlock the suit storage unit
without access. You can set personal access to make sure only you can
access the unit

## Changelog
:cl:
add: Access secured closets. Personal closets can have their access
overwritten by an new id in it's unlocked state
add: Access secured freezers.
add: Access secured suit storage units.
fix: Suit storage unit not having access restrictions.
fix: airlock electronics not properly getting removed after screwing
them out from round start lockers
fix: round spawned open crates run timing when closed
fix: open crates hiding stuff in plain sight
fix: open closets/crates sucking up contents during late initialize
causing them appear empty & open
/:cl:

---------

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [mvollmer/cockpit](https://github.com/mvollmer/cockpit)@[79d6a888d4...](https://github.com/mvollmer/cockpit/commit/79d6a888d43a1544ec275c7681cc699abdd698f0)
#### Tuesday 2023-06-13 13:08:17 by Martin Pitt

pybridge: Fix clobbering remote user set in SSH config

When opening a remote host channel without `user`, stop assuming the
current local user name, as that overwrites any `User` field in
the SSH configuration.

Instead, we need to do the opposite: for an unknown host, the UI will
not set a `user` field in the channel options, but for an actual login
attempt with a password it will. We need to treat them as the same
channel in the `self.remotes` map. The C bridge deals with this in
cockpit_router_normalize_host_params() by disregarding the `user` field
if it is equal to the current user name.

This is a rather silly hack for backwards compatibility, but while we
have two bridges, let's rather stay bug-for-bug compatible and clean
this up in the UI only after we drop the C bridge.

There is one extra tweak: `rpartition()` returns an empty string, but
we can't pass that on literally. So turn those into `None`.

Fixes #18714

---
## [CDCgov/prime-reportstream](https://github.com/CDCgov/prime-reportstream)@[8b92a1e515...](https://github.com/CDCgov/prime-reportstream/commit/8b92a1e515d1f0e0c68d9471fcb1163432dae487)
#### Tuesday 2023-06-13 13:34:20 by Stephen Kao

Experience-7891: Disable organization-specific fetches as admin (#7928)

This changeset disables a few Organization-specific requests to mitigate the number of 404s we're getting as admins try to fetch Organization resources:
- Organization settings
- Deliveries
- Submissions

There's not a one-size-fits-all solution here given the different fetch mechanisms we already have and how the data is rendered, so I tried to add minimal changes to prevent disrupting anything down the line.  I think going forward, we can make a generic `useOrganizationQuery` hook that'll automatically be disabled if the user is logged in as an admin without impersonating an Organization.  There are a lot of layers with our fetching that in my opinion should be untangled, but that's out of the scope of this pull request.

---
## [ilyasher/pytorch](https://github.com/ilyasher/pytorch)@[b5840f99c3...](https://github.com/ilyasher/pytorch/commit/b5840f99c3f2ae01b7831fd32b99758180fc22c3)
#### Tuesday 2023-06-13 16:56:07 by Mark Saroufim

torch.compiler public namespace (#102182)

# torch.compiler public API

## Goal

The goal of this document is to describe the public facing API for torchdynamo and torchinductor.

Today both dynamo and torchinductor are in `torch/_dynamo` and `torch/_inductor` namespace with the only public function

`torch.compile()` which is directly placed in `torch/__init__.py`

This poses a few problems for users trying to take dependencies on PyTorch 2.0
1. Unclear BC guarantees
2. No builtin discovery mechanism outside of reading the source code
3. No hard requirements for docstrings or type annotations

Most importantly it mixes two personas the PyTorch 2.0 developer vs the PyTorch 2.0 customer so this is an attempt to address this. We draw a lot of inspiration from the `functorch` migration to the `func` namespace.

## Alternate names

We did discuss some other alternative names

1. `torch.compile` -> problem is this would break BC on the existing `torch.compile` function
2. `torch.dynamo` -> `dynamo` is so far not something we've deliberately hidden from users but problem is now figuring out what it's `_dynamo` vs `dynamo` might be confusing
3. `torch.compiler` -> 1 would be better but to keep BC this is a good compromise

# The general approach
## Proposal 1
In https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py

We have function called `reset()`, this function is essential if users are trying to `torch.compile()` a model under different settings

```python
# in _dynamo/
def reset():
    do_reset_stuff()
```

Instead we propose

```python
# in compiler/
def reset():
    do_reset_stuff() # As in copy paste the logic from _dynamo.reset

# in _dynamo/
import warnings
import inspect

def reset():
    function_name = inspect.currentframe().f_code.co_name
    warnings.warn(f"{function_name} is deprecated, use compiler.{function_name} instead", DeprecationWarning)
    return compiler.reset()

```
## Proposal 2

```python
# in compiler/
def reset():
    “””
    Docstrings here
    “””
    _dynamo.reset()

# in _dynamo/
No changes
```
Consensus so far seems to be proposal 2 since fewer warnings will be less jarring and it’ll make it quite easy to merge the public API

## Docstrings

The above was an example of a function that has no inputs or outputs but there are other functions which could use an improvement in their docstrings, for example allow_in_graph actually works over lists of functions but that’s not mentioned anywhere in the example only if you read the source code.

def allow_in_graph(fn):
    """
    Customize which functions TorchDynamo will include in the generated
    graph. Similar to `torch.fx.wrap()`.

    Parameters:
        fn (callable or list/tuple): The function(s) to be allowed in the graph.

    Returns:
        callable or list/tuple: The input function(s) included in the graph.

    Examples:
        Customize inclusion of a single function:
        ::
            torch._dynamo.allow_in_graph(my_custom_function)

        Customize inclusion of multiple functions:
        ::
            torch._dynamo.allow_in_graph([my_custom_function1, my_custom_function2])

        @torch._dynamo.optimize(...)
        def fn(a):
            x = torch.add(x, 1)
            x = my_custom_function(x)
            x = torch.add(x, 1)
            return x

        fn(...)

    Notes:
        The `allow_in_graph` function allows customization of which functions TorchDynamo
        includes in the generated graph. It can be used to include specific functions that
        are not automatically captured by TorchDynamo.

        If `fn` is a list or tuple, `allow_in_graph` will be called recursively on each
        element in the sequence.

        Once a function is allowed in the graph using `allow_in_graph`, it will be captured
        in the graph generated by TorchDynamo. This customization enables more fine-grained
        control over the functions included in the graph.

        Note that `allow_in_graph` expects the input `fn` to be a callable.

    """
    if isinstance(fn, (list, tuple)):
        return [allow_in_graph(x) for x in fn]
    assert callable(fn), "allow_in_graph expects a callable"
    allowed_functions._allowed_function_ids.add(id(fn))
    allowed_functions._disallowed_function_ids.remove(id(fn))
    return fn

So to make the API public, we’d have to write similar docstrings for all public functions we’d like to create.

The benefit of this approach is that
1. No BC risks, internal and external users relying on our tooling can slowly wean off the private functions.
2. We will also have to write correct docstrings which will automatically make our documentation easier to maintain and render correctly on pytorch.org
3. We already have some BC guarantees already, we don’t kill OptimizedModule, we rejected the PR to change the config system

The con of this approach is that
Will be stuck with some potentially suboptimal functions/classes that you can’t kill

## Testing strategy
If the approach is to mostly make a public function call an already tested private function then all we need to do is ensure that the function signatures don't change

## Which functions should be in the public API

Our heuristic for deciding whether something should be public or not is are users already relying on it for lack of other options or have we recommended some non public functions for users to debug their PT 2.0 programs.

Heuristic for not putting something in public is that it’s an experimental subsystem with the goal of turning it on by default, it’s very core dev centric, meta centric, a bunch of different configs that should be batched into a single user facing one, or something that needs to be renamed because the name is confusing

#### Top level
`torch.compile()` -> already is a public API it does require some minor improvements like having configs be passed in to any backend and not just inductor (EDIT: This was already done https://github.com/pytorch/pytorch/pull/99645l) and renaming `mode=reduce-overhead` to `mode=cudagraph`

To make sure that PT 2.0 is supported with a given pytorch version users can create a new public function and this would replace the need for `try/except` blocks around `import torch._dynamo` that has been populating user code.

```python
def pt2_enabled():
    if hasattr(torch, 'compile'):
        return True
    else:
        return False
```

For all of the below they will be translated to `torch.compiler.function_name()`

#### From _dynamo

As a starting point we looked at https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py and we suggest redefining these functions in `pytorch/torch/compiler/__init__.py`

It might also make sense to split them over multiple files and import them in `__init__.py` but because the number of functions is small it'd probably be fine to add them all into a single compiler/__init__.py until this list becomes larger

1. `reset()`
2. `allow_in_graph()`
10. `list_backends()`
12. `compile()`:  torch.compile() would be mostly a shell function passing arguments to torch.compiler.compile()
13. `assume_constant_result()`: TODO: Double check how this is useful
15. `torch._dynamo.disable()`

Some notable omissions
11. `explain()`: We need to clean up the output for this function, make it a data class and pretty printable
1. `forbid_in_graph()`: Considered adding this but should instead consolidate on `disallow_in_graph`
2. `optimize_assert()`: Already covered by `torch.compile(fullgraph=True)`
3. `check_if_dynamo_supported()`: this would be supplanted by pt2_enabled()
4. `compilation_metrics`, `graph_breaks_reasons` ..: would all be accessed via `torch.compiler.explain()`
5. `replay` does not seem useful to end customers
6. . `graph_break()`: Mostly useful for debugging or unit tests
9. `register_backend()`: End users will just pass a string backend to torch.compile, only devs will create new backends
10. `export()` : Eventually this needs to public but for now it’s not ready so just highlighting that it will be in the public API eventually
11. `disallow_in_graph()`: Usage is limited
12. `mark_static()`: we can keep this private until dynamic=True is recommended in stable
13. `mark_dynamic()`:  we can keep this private until dynamic=True is recommended in trunk
14. 8. `OptimizedModule`: This is the only class that we'd expose but is crucial since users are running code like `if isinstance(mod, OptimizedModule): torch.save(mod._orig_mod)` EDIT: because we fixed pickling we no longer need to
expose this
15. `is_compiling()`: Still not clear how this useful to end users

There are also config variables which we need to expose https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/config.py

Some of our configs are useful dev flags, others are to gate experimental functionality and others are essential debugging tools and we seperate out the essential debugging and logging tools to a public facing config.

TODO: I still need to think of a good way of porting the config in a BC way here are some ideas
1. Just make all passes available and controllable via `torch.compile(options={})` but only show docstrings for the ones users should care about.

The current problem with our config system is we have 3 ways of setting them once via `options={}`, environment variables and variables in `config.py`, it'd be worth settling on one source of truth and have that be the public API.

The configs we should make public are
1. `log_file_name`
2. `verbose`
3. `cache_size_limit`
4. `repro_level` and `repro_after`: Although we can rename these to minifier and give human readable names to the levels

Everything else should stay private in particular

1. `print_graph_breaks`, `print_specializations`: should be supplanted by `explain()` for public users
2. dynamic shape configs : Users should only have to worry about `torch.compile(dynamic=True/False)`
3. The distributed flags, hook or guard configs: If we tell a user to use FSDP and DDP then the flag should be enabled by default or be in a private namespace
4. The fbcode flags: Obviously no need to be user facing
5. Skip/Allow lists: Not something normal users should play around with

#### From _inductor
Very little of inductor should be exposed in a public facing API, our core audience as in people writing models mostly just need information on what certain passes mean and how to control them a high level and they can do this with `torch.compile(options={})` so the goal here should be more to make available passes clearer and ideally consolidate them into `torch.compile()` docstrings or modes.

There are some exceptions though from https://github.com/pytorch/pytorch/blob/main/torch/_inductor/__init__.py

1. `list_mode_options()`
2. `list_options()`: this needs an additional pass to hide internal or debug options

For both of these we’d rename them to compiler.inductor_list_mode_options and compiler.inductor_list_options() since they would be in the same init file as the one for dynamo

Notable omissions
1. `_inductor.compile()`: Because of users are coming in with their own fx graph, they are likely developers
2. `_inductor.aot_compile()`:Again this is about capturing and modifying fx graphs so users APIs don't need to be public

However the configs are a slightly different story, because we can choose to either
1. Make all configs public
2. Make some configs public and keep most of the private ones. If public config is set it should override the private version
3. Make all configs controllable via `torch.compile(options={})` but make list_options() hide more things

For now 3 seems like the most reasonable choice with some high level configs we’ll keep like TORCH_COMPILE_DEBUG

Regardless here's what should probably be public or advertised more
1. `disable_progress` and verbose_progress:  Combine and enable by default
2. `fallback_random`: We could make the case this shouldn't be public if a top level deterministic mode enables this
3. `profile_bandwidth`: Or could make the case that this should be in TORCH_COMPILE_DEBUG

Notable omissions
1. Any config that would generally improve performance for most that we should probably enable by default but might be disabled in the short term because of stability: example `epilogue_fusion`, `pattern_matcher`, `reordering`
2. Autotuning flags: Should just sit behind `torch.compile(mode="max-autotune")` like `max_autotune`, `max_autotune_gemm`
3. `coordinate_descent_tuning`: This one I'm a but mixed about, maybe it just also fall into `mode="max-autotune"`
4. `trace`: `TORCH_COMPILE_DEBUG` is the best flag for all of this
5. `triton.cudagraphs`: Default should be `torch.compile(mode="reduce-overhead")` - I'd go further and rename the `mode=cudagraph` and we can keep reduce-overhead for BC reasons
6. `triton_unique_kernel_names`: Mostly useful for devs debugging
7. `dce`: which doesnt really do anything
8. `shape_padding`: Elias is working on enabling this by default in which case we also remove it

## Mechanics

This PR would include the public functions with their docstrings

Another PR will take a stab at the configs

And for work where the APIs are still being cleaned up whether its minifier or escape hatches, export or dynamic shapes, aot_inductor etc.. we’ll keep them private until a public commitment can be made

Pull Request resolved: https://github.com/pytorch/pytorch/pull/102182
Approved by: https://github.com/jansel

---
## [ASVGay/the-rhapsodies](https://github.com/ASVGay/the-rhapsodies)@[9fe40cab45...](https://github.com/ASVGay/the-rhapsodies/commit/9fe40cab45456a73ecd3e921c5efc49f03d9c7c3)
#### Tuesday 2023-06-13 17:10:19 by F.S. Koulen

Update dependency react-redux to v8.1.0 (#298)

[![Mend
Renovate](https://app.renovatebot.com/images/banner.svg)](https://renovatebot.com)

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence |
|---|---|---|---|---|---|
| [react-redux](https://togithub.com/reduxjs/react-redux) | [`8.0.5` ->
`8.1.0`](https://renovatebot.com/diffs/npm/react-redux/8.0.5/8.1.0) |
[![age](https://badges.renovateapi.com/packages/npm/react-redux/8.1.0/age-slim)](https://docs.renovatebot.com/merge-confidence/)
|
[![adoption](https://badges.renovateapi.com/packages/npm/react-redux/8.1.0/adoption-slim)](https://docs.renovatebot.com/merge-confidence/)
|
[![passing](https://badges.renovateapi.com/packages/npm/react-redux/8.1.0/compatibility-slim/8.0.5)](https://docs.renovatebot.com/merge-confidence/)
|
[![confidence](https://badges.renovateapi.com/packages/npm/react-redux/8.1.0/confidence-slim/8.0.5)](https://docs.renovatebot.com/merge-confidence/)
|

---

### Release Notes

<details>
<summary>reduxjs/react-redux</summary>

###
[`v8.1.0`](https://togithub.com/reduxjs/react-redux/releases/tag/v8.1.0)

[Compare
Source](https://togithub.com/reduxjs/react-redux/compare/v8.0.7...v8.1.0)

This **feature release** adds new development-mode safety checks for
common errors (like poorly-written selectors), adds a workaround to fix
crash errors when React-Redux hooks are imported into React Server
Component files, and updates our hooks API docs page with improved
explanations and updated links.

#### Changelog

##### Development Mode Checks for `useSelector`

We've had a number of users tell us over time that it's common to
accidentally write selectors that have bad behavior and cause
performance issues. The most common causes of this are either selectors
that unconditionally return a new reference (such as `state =>
state.todos.map()` without any memoization ), or selectors that actually
return the *entire* root state ( `state => state` ).

We've updated `useSelector` to add safety checks in development mode
that warn if these incorrect behaviors are detected:

- Selectors will be called twice with the same inputs, and `useSelector`
will warn if the results are different references
- `useSelector` will warn if the selector result is actually the entire
root `state`

By default, **these checks only run *once* the first time `useSelector`
is called**. This should provide a good balance between detecting
possible issues, and keeping development mode execution performant
without adding many unnecessary extra selector calls.

If you want, you can configure this behavior globally by passing the
enum flags directly to `<Provider>`, or on a per-`useSelector` basis by
passing an options object as the second argument:

```ts
// Example: globally configure the root state "noop" check to run every time
<Provider store={store} noopCheck="always">
  {children}
</Provider>
```

```ts
// Example: configure `useSelector` to specifically run the reference checks differently:
function Component() {
  // Disable check entirely for this selector
  const count = useSelector(selectCount, { stabilityCheck: 'never' })
  // run once (default)
  const user = useSelector(selectUser, { stabilityCheck: 'once' })
  // ...
}
```

This goes along with the similar safety checks we've added to [Reselect
v5
alpha](https://togithub.com/reduxjs/reselect/releases/tag/v5.0.0-alpha.2)
as well.

##### Context Changes

We're still trying to work out how to properly use Redux and React
Server Components together. One possibility is using RTK Query's
`createApi` to define data fetching endpoints, and using the generated
thunks to fetch data in RSCs, but it's still an open question.

However, users have reported that merely importing *any* React-Redux API
in an RSC file causes a crash, because `React.createContext` is not
defined in RSC files. RTKQ's React-specific `createApi` entry point
imports React-Redux, so it's been unusable in RSCs.

This release adds a workaround to fix that issue, by using a proxy
wrapper around our singleton `ReactReduxContext` instance and lazily
creating that instance on demand. In testing, this appears to both
continue to work in all unit tests, *and* fixes the import error in an
RSC environment. We'd appreciate further feedback in case this change
does cause any issues for anyone!

We've also tweaked the internals of the hooks to do checks for correct
`<Provider>` usage when using a custom context, same as the default
context checks.

##### Docs Updates

We've cleaned up some of the Hooks API reference page, and updated links
to the React docs.

#### What's Changed

- check for Provider even when using custom context by
[@&#8203;EskiMojo14](https://togithub.com/EskiMojo14) in
[https://github.com/reduxjs/react-redux/pull/1990](https://togithub.com/reduxjs/react-redux/pull/1990)
- Add a stability check, to see if selector returns stable result when
called with same parameters. by
[@&#8203;EskiMojo14](https://togithub.com/EskiMojo14) in
[https://github.com/reduxjs/react-redux/pull/2000](https://togithub.com/reduxjs/react-redux/pull/2000)
- Add an E2E-ish test that verifies behavior when imported into RSCs by
[@&#8203;markerikson](https://togithub.com/markerikson) in
[https://github.com/reduxjs/react-redux/pull/2030](https://togithub.com/reduxjs/react-redux/pull/2030)
- lazily create Context for RSC compat by
[@&#8203;phryneas](https://togithub.com/phryneas) in
[https://github.com/reduxjs/react-redux/pull/2025](https://togithub.com/reduxjs/react-redux/pull/2025)
- Add warning for selectors that return the entire state by
[@&#8203;EskiMojo14](https://togithub.com/EskiMojo14) in
[https://github.com/reduxjs/react-redux/pull/2022](https://togithub.com/reduxjs/react-redux/pull/2022)

**Full Changelog**:
https://github.com/reduxjs/react-redux/compare/v8.0.7...v8.1.0

###
[`v8.0.7`](https://togithub.com/reduxjs/react-redux/releases/tag/v8.0.7)

[Compare
Source](https://togithub.com/reduxjs/react-redux/compare/v8.0.6...v8.0.7)

This release updates the peer dependencies to accept Redux Toolkit, and
accept the ongoing RTK and Redux core betas as valid peer deps.

> **Note**: These changes were initially in 8.0.6, but that had a typo
in the peer deps that broke installation. Sorry!

#### What's Changed

- Bump Redux peer deps to accept 5.0 betas, and bump RTK dev dep by
[@&#8203;markerikson](https://togithub.com/markerikson) in
[https://github.com/reduxjs/react-redux/pull/2017](https://togithub.com/reduxjs/react-redux/pull/2017)
- [`d45204f`](https://togithub.com/reduxjs/react-redux/commit/d45204f) :
Fix broken RTK peer dep

**Full Changelog**:
https://github.com/reduxjs/react-redux/compare/v8.0.5...v8.0.7

###
[`v8.0.6`](https://togithub.com/reduxjs/react-redux/releases/tag/v8.0.6)

[Compare
Source](https://togithub.com/reduxjs/react-redux/compare/v8.0.5...v8.0.6)

\~~This release updates the peer dependencies to accept Redux Toolkit,
and accept the ongoing RTK and Redux core betas as valid peer deps.~~

**This release has a peer deps typo that breaks installation - please
use 8.0.7 instead !**

#### What's Changed

- Bump Redux peer deps to accept 5.0 betas, and bump RTK dev dep by
[@&#8203;markerikson](https://togithub.com/markerikson) in
[https://github.com/reduxjs/react-redux/pull/2017](https://togithub.com/reduxjs/react-redux/pull/2017)

**Full Changelog**:
https://github.com/reduxjs/react-redux/compare/v8.0.5...v8.0.6

</details>

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined),
Automerge - At any time (no schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR has been generated by [Mend
Renovate](https://www.mend.io/free-developer-tools/renovate/). View
repository job log
[here](https://app.renovatebot.com/dashboard#github/ASVGay/the-rhapsodies).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzNS4xMTUuMiIsInVwZGF0ZWRJblZlciI6IjM1LjExNS4yIiwidGFyZ2V0QnJhbmNoIjoiZGV2In0=-->

---
## [k2project/nt-mern](https://github.com/k2project/nt-mern)@[ea341e6b46...](https://github.com/k2project/nt-mern/commit/ea341e6b46cfaa8fff49731f54dbf06a2dd8c90b)
#### Tuesday 2023-06-13 17:33:04 by Kris

Podcasts updates.

Please can you remove the BACP logo on the home page.
On the FAQ about working online, please can we change those circles to either the question mark or the numbers on the home page.
On FAQ please can we make WHAT IS PSYCHOTHERAPY? Bold.
On Blog can we change opinion piece to BLOG ARTICLE.
I like the question mark thing, can we try a small one to the left of Nujoji Calvocoressi Psychotherapy in the header?
Can you give me a bit more chin in my profile pic pls.
Is there a way that when you get to the bottom of the page it scrolls onto the next page?
Can we move the two new books to the top of the book section (Klein and Hirsch).
Let’s move down EMDR and ARE YOU LOST IN THE WORLD LIKE ME to the bottom videos and replace thumbnail with the rat attached.
Kirk Honda should be Dr Kirk Honda
Please can you replace the room image with ROOM 4 Geo.
Can we make the dummy a little darker like in the attached.
On the contact page can we hyperlink the addresses in the right box and change the map square on the left to a big question mark and hyperlink to https://en.wikipedia.org/wiki/Question_mark and maybe a small thumbnail photo of me in the corner, perhaps in black and white. This is a different image.
Do you think we should display an email address on the website if people don’t want to use the box?
Is something happening to Google Analytics? Is it closing down?
On the Inside Time article, when you expand, please can it show the Inside Time logo.
What do you think that on each page somewhere different on the squares section on the lines we have a small butterfly? I might be getting carried away but could look interesting. Maybe a little bigger than the ones on the chairs.
Do I need a pop-up cookie banner?
Can we try these background colours (attached) going dark – light in the order of the tabs, left – right.
On the home page – underneath bottom right-hand square in the white text box can we do a CTA to contact and remove the one from the top box.
On the blog page top right can we do a CTA to FAQ.
https://kijo.co.uk/blog/luxury-web-design-techniques-2021/ I like the custom curser.
Can we do some hidden animation on the navigation buttons? Make them jiggle or something.

---
## [apache/cxf](https://github.com/apache/cxf)@[5b69dd06a6...](https://github.com/apache/cxf/commit/5b69dd06a61a8985e9166108e66e56f481a438cf)
#### Tuesday 2023-06-13 17:39:38 by Daniel Kulp

[CXF-8885] Make an attempt to get the HttpClient selector threads to shutdown sooner
Technically, they should shut themselves down about 3 seconds after a garbage collection assuming the client they are associated with is cleaned up and released.   However, if many clients are used, this may be too long and thus we'll make an attempt (via some hacks) to get the thread to shutdown sooner.  It's a shame HttpClient doesn't implement Closeable. :(

(cherry picked from commit 65711680af99de16f56cbaa819d207edb9428e8a)

---
## [Brigzilla/PWRLFTR](https://github.com/Brigzilla/PWRLFTR)@[2f7ccdb118...](https://github.com/Brigzilla/PWRLFTR/commit/2f7ccdb1188b723ed59598f8b279aff85e8962d9)
#### Tuesday 2023-06-13 17:40:31 by Brigzilla

Program can be generated with a one rep max for squats. When the user clicks to generate the program it won't update the UI immediately. This is because Room is fucking awful and coroutines are shit. Two options:
1: Remove the ViewPager support and go back to a nav graph, which honestly sounds great right now
2: Figure out a way to make the recyclerview refresh

---
## [nickabooch/evals](https://github.com/nickabooch/evals)@[b93700ab49...](https://github.com/nickabooch/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Tuesday 2023-06-13 18:12:18 by DunedainStrider

Do math problems related to calculating dates using the Chinese Sexagenary Cycle method. 🧮 (#190)

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
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Do math problems related to calculating dates using the Chinese
Sexagenary Cycle method

### Eval description

The Sexagenary Cycle combines 10 Heavenly Stems (Jia 甲, Yi 乙, Bing 丙,
Ding 丁, Wu 戊, Ji 己, Geng 庚, Xin 辛, Ren 壬, Gui 癸) and 12 Earthly Branches
(Zi 子, Chou 丑, Yin 寅, Mao 卯, Chen 辰, Si 巳, Wu 午, Wei 未, Shen 申, You 酉,
Xu 戌, Hai 亥) to form a 60-unit cycle. To calculate, convert the
Gregorian date to its corresponding Heavenly Stem and Earthly Branch
combination, used for marking specific years, months, and days.

### What makes this a useful eval?

The existing GPT models tend to make errors when performing calculations
related to the Sexagenary Cycle. To address this issue, we have provided
a specialized dataset aimed at improving the model's accuracy in
handling Sexagenary Cycle calculations.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

[2023-03-16 12:46:51,594] [record.py:320] Final report: {'accuracy':
0.65}. Logged to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl
[2023-03-16 12:46:51,594] [oaieval.py:211] Final report:
[2023-03-16 12:46:51,594] [oaieval.py:213] accuracy: 0.65
[2023-03-16 12:46:51,597] [record.py:309] Logged 60 rows of events to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl:
insert_time=2.463ms

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"甲戌的次日是？"}], "ideal": "乙亥"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"乙亥的次日是？"}], "ideal": "丙子"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬寅的后日是？"}], "ideal": "甲辰"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"癸卯的后日是？"}], "ideal": "乙巳"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬子的后日是？"}], "ideal": "甲寅"}
  ```
</details>

---------

Co-authored-by: dunedainstrider <dunedainstrider@mac16>

---
## [nickabooch/evals](https://github.com/nickabooch/evals)@[8e276ea460...](https://github.com/nickabooch/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Tuesday 2023-06-13 18:12:18 by steven-luabase

Eval: Probability Questions Sourced From Actuarial Exam P and University Statistics Courses (#263)

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
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Probability Questions

### Eval description

Tests the model's ability to understand answer probability questions.
Questions are sourced from Society of Actuaries Exam P sample questions
and practice problems/exams from statistics classes at MIT, UPenn,
California State University, Durham University, University of
Connecticut, and other sources. The full list of questions and sources
(in the same order as in the `.jsonl` files) can be found in this Google
[sheet](https://docs.google.com/spreadsheets/d/1TU_4VPhIce9JtLV5gLy619WNibVjiWB-dtiwqkBtCrU/edit?usp=sharing)

### What makes this a useful eval?

Test the model's ability to understand worded probability questions,
bring in concepts such as probability distributions, and then reason
through a correct answer.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Using the `match` grading criteria, GPT3.5-turbo got an accuracy score
of `{'accuracy': 0.07}`

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A pair of fair, standard dice are rolled. What is the
probability the sum of the dice is 5"}], "ideal": ["0.1111"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "An airplane is built to be able to fly on one engine. If the
plane's two engines operate independently, and each has a 1% chance of
failing in any given four-hour flight, what is the chance the plane will
fail to complete a four-hour flight to Oklahoma due to engine
failure?"}], "ideal": ["0.0001"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A 1-inch-diameter coin is thrown on a table covered with a
grid of lines two inches apart. What is the probability the coin lands
in a square without touching any of the lines of the grid?"}], "ideal":
["0.2500"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 50 students in a certain class, 5 speak French. Two
students of the class will be selected at random. Which of the following
is closest to the probability that neither of the students selected will
speak French?"}], "ideal": ["0.8100"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 10 marbles in a box, 2 are green. A person will
select 2 marbles simultaneously and at random from the box. What is the
probability that neither of the marbles selected will be green?"}],
"ideal": ["0.6222"]}
  ```
</details>

---
## [nickabooch/evals](https://github.com/nickabooch/evals)@[33484c8341...](https://github.com/nickabooch/evals/commit/33484c83416c30733359d5c4dcb9a61f91cab8a6)
#### Tuesday 2023-06-13 18:12:18 by emu1729

Added AIME eval (#293)

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
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
AIME-Evaluation

### Eval description

This eval evaluates GPT on some selected AIME (American Invitational
Mathematics Examination) problems. This is a selective and prestigious
mathematical examination for high schoolers. All questions are selected
from the 2001 and 2002 AIME I and II examinations.

### What makes this a useful eval?

This evaluation combines math and logical evaluation and is designed to
be quite challenging. The model must first understand the math question
asked and then perform the math equations needed to come up with a
reasonable solution.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

Our eval was designed to include both math and logical reasoning and is
quite challenging. This is a level above the AMC10 examination.

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

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

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Find the sum of all positive
two-digit integers that are divisible by each of their
digits."}],"ideal":"630"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A fair die is rolled four
times. The probability that each of the final three rolls is at least as
large as the roll preceding it may be expressed in the form m\/n, where
m and n are relatively prime positive integers. Find m +
n"}],"ideal":"079"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A sphere is inscribed in the
tetrahedron whose vertices are A = (6, 0, 0), B = (0, 4, 0), C = (0, 0,
2), and D = (0, 0, 0).The radius of the sphere is m \/ n, where m and n
are relatively prime positive integers. Find m + n."}],"ideal":"005"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A mail carrier delivers mail
to the nineteen houses on the east side of Elm Street. The carrier
notices that no two adjacent houses ever get mail on the same day, but
that there are never more than two houses in a row that get no mail on
the same day. How many different patterns of mail delivery are
possible?"}],"ideal":"351"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"The numbers 1, 2, 3, 4, 5, 6,
7, and 8 are randomly written on the faces of a regular octahedron so
that each face contains a different number. The probability that no two
consecutive numbers, where 8 and 1 are considered to be consecutive, are
written on faces that share an edge is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"085"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Let N be the largest positive
integer with the following property: reading from left to right, each
pair of consecutive digits of N forms a perfect square. What are the
leftmost three digits of N?"}],"ideal":"816"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each of the 2001 students at a
high school studies either Spanish or French, and some study both. The
number who study Spanish is between 80 percent and 85 percent of the
school population, and the number who study French is between 30 percent
and 40 percent. Let m be the smallest number of students who could study
both languages, and let M be the largest number of students who could
study both languages. Find M-m."}],"ideal":"298"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A set of positive numbers has
the 'triangle-property' if it has three distinct elements that are the
lengths of the sides of a triangle whose area is positive. Consider sets
{4, 5, 6, ..., n} of consecutive positive integers, all of whose
ten-element subsets have the triangle property. What is the largest
possible value of n?"}],"ideal":"253"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each unit square of a 3-by-3
unit-square grid is to be colored either blue or red. For each square,
either color is equally likely to be used. The probability of obtaining
a grid that does not have a 2-by-2 red square is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"929"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Given that x and y are both
integers between 100 and 999, inclusive; y is the number formed by
reversing the digits of x; and z=|x-y|. How many distinct values of z
are possible?"}],"ideal":"009"}

  ```
</details>

---------

Co-authored-by: Emily Mu <emilymu@30-10-85.wireless.csail.mit.edu>
Co-authored-by: Emily Mu <emilymu@30-10-24.wireless.csail.mit.edu>

---
## [nickabooch/evals](https://github.com/nickabooch/evals)@[aa71d43273...](https://github.com/nickabooch/evals/commit/aa71d4327328933a463e972d662e6988234d0ef7)
#### Tuesday 2023-06-13 18:12:18 by Andrew Kondrich

Fix get_answer (#972)

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
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
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
  INSERT_EVAL_HERE
  ```
</details>

---
## [nickabooch/evals](https://github.com/nickabooch/evals)@[8f8632ec55...](https://github.com/nickabooch/evals/commit/8f8632ec55ee1f9704fe34225e1bce0cd999a8b1)
#### Tuesday 2023-06-13 18:12:18 by Oshan Upreti

Nepali song singer recognition (#892)

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

## Eval details 📑
### Eval name
Nepali Song Singer

### Eval description

It tests the ability to understand Nepali language from given English
Transliteration phrase which is provided by user as a song title, and
checks the singer/band of the song. This eval has the accuracy of zero.
And, I still created this eval PR because I get the wrong answers every
time I ask, and I don't think that should be the case. It might not be
something that needs to be done immediately, but in a near future you
would expect your AI to answer it correctly.

### What makes this a useful eval?

If it can do for any English songs in the database, it should be able to
do for other languages as well. This is just a pattern I found it in my
mother tongue, but there might be different other languages where this
is happening as well, and it can be other things as well not just the
song title recognition.

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

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Sayad Timro Bato Ma"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Timi Lai Dekhera"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Aaja maan udhera bhagchha"}],
"ideal": "Udit Narayan"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Kaha Hola Ghar Bara"}], "ideal":
"Karma"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Khaseka Tara"}], "ideal":
"Albatross"}
  ```
</details>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[0cff53fc09...](https://github.com/Bjarl/Shiptest/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Tuesday 2023-06-13 18:40:45 by meemofcourse

Reworks the Twinkleshine-Class (#1825)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![2023 05 13-23 20
45](https://github.com/shiptest-ss13/Shiptest/assets/75212565/de6f3a47-7be8-4800-ae73-9fc386e4bf01)

![twinklerework5](https://github.com/shiptest-ss13/Shiptest/assets/75212565/f1808576-70e3-4b56-b977-5b5e7d665fdd)





The Twinkleshine is a CyberSun-made Syndicate display of force, staffed
by every branch of the Syndicate. Despite the silly name, the presence
of one in a sector implies it to be of importance to the Syndicate, and
enemies within sight can only pray that the Twinkleshine crew are
incompetent enough to shoot themselves with their own weaponry (or blow
themselves up with the supermatter on-board).

It is staffed by:

- 1 Captain
- 1 Lieutenant (previously the Operative - serves as a warden/hos)
- 2 Medics
- 2 Engineers (previously the Mechanics)
- 5 Operatives (previously the Troopers)
- 1 Bartender
- 1 Miner
- 2 Deck Assistants

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Few days ago, an admin spawned a Twinkleshine, and I got to captain it.
The Twinkleshine is old. It sucks. This, hopefully, fixes that.

Originally, this was going to be minor fixes, but ended up becoming an
attempt at reworking the ship to a more modern state - the hull has been
redone and is mostly symmetrical, the old spacepod was replaced with a
Dark Gygax, the supermatter shouldn't be activated upon spawning the
ship, there's more turf decals and a bigger lot-of-things, added a
bartender and a miner, people can actually tell who they are and what
they do, and there is now a box moth. Rejoice.

Also, this is the first time I've ever mapped a ship. What better way to
begin with a giant battleship?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
tweak: Reworks the Twinkleshine
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: meemofcourse <75212565+meemofcourse@users.noreply.github.com>

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[c67d6a22a4...](https://github.com/JohnFulpWillard/tgstation/commit/c67d6a22a405f006a9d7a537dc35cecbdb65cfde)
#### Tuesday 2023-06-13 18:45:09 by Kyle Spier-Swenson

fix stupid error message in delay pre-game (#75824)

tabbing out during init after hitting the verb, while you wait for the
server to un-lockup and present you with the prompt, and coming back in,
noticing you were too late, and cancelling out of the time prompt, only
to get told the round had already started, was kinda fucking lame. I
know, thats why i fucking hit cancel you fucking robit.

also makes the proc more early return

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[d01b433ab1...](https://github.com/JohnFulpWillard/tgstation/commit/d01b433ab12e7aa45416d42f9045f1135e545dae)
#### Tuesday 2023-06-13 18:45:09 by Sealed101

Fixes colossus possessor crystal cockroaches/animals not dumping the user's body upon death/gibbing (#75843)

## About The Pull Request
Hooks the stasis closet thingamajing into `COMSIG_LIVING_DEATH` instead
of checking the animal's stat on `process()`, which makes possessed
animals properly dump the stasis closet's contents upon death or gibbing
(which is death but cooler).
yeah uh this method is hilarious but it does protect the user's body
quite reliably at least lol

## Why It's Good For The Game
Fixes #75829
also probably makes cockroach death saner in some unreported way, this
`. = ..()` vs `..()` is above my non-existent paygrade but it keeps
popping up from time to time

## Changelog
:cl:
fix: gibbing colossus possessor crystal possessed animals will no longer
stick the user's body and their stuff into the shadow realm. the animals
will properly drop your corpse when killed or gibbed
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Dark-WarriorZD/my-work](https://github.com/Dark-WarriorZD/my-work)@[8a1554d960...](https://github.com/Dark-WarriorZD/my-work/commit/8a1554d960e414a0d7a7d8f2444e494d8e7902f8)
#### Tuesday 2023-06-13 18:58:01 by Dark-WarriorZD

Update README.md

Esther Hautzig's emotions underwent a profound transformation from the moment she took home the "filthy rag of a skirt" to her heartfelt expression of gratitude to God for the gift. The author employs vivid descriptions and powerful language techniques to portray Esther's evolving feelings, revealing her resilience and gratitude amidst difficult circumstances.

Upon receiving the ragged skirt, Esther's initial reaction is one of disappointment and resentment. The author captures her disillusionment through the embedded quote, "I took home the filthy rag of a skirt." This choice of words, utilizing a metaphor, conveys Esther's perception of the skirt as something worthless and degrading. The metaphor emphasizes the poor condition of the garment, symbolizing her low expectations and the lack of material possessions in her life.

However, a profound shift occurs within Esther as she reflects on her situation. The author reveals this transformation through the embedded quote, "and thanked God for the gift." Here, the author uses a juxtaposition of contrasting ideas to highlight Esther's newfound gratitude. This shift in perspective showcases her ability to find gratitude in the midst of hardship, demonstrating her resilience and strength of character.

Additionally, the author employs repetition as a language technique to emphasize Esther's determination and resourcefulness. The phrase "one more cup of flour, one more sip of milk" is repeated, creating a rhythmic pattern that underscores Esther's tenacity. The repetition not only serves to emphasize her relentless pursuit of sustenance but also symbolizes her unwavering hope and her ability to find solace in the simplest of things.

Moreover, the author utilizes imagery to evoke a sense of poverty and scarcity. The description of the skirt as a "filthy rag" conjures vivid mental images of its tattered and unclean state. This visual imagery serves as a stark reminder of the difficult circumstances in which Esther finds herself, adding depth to her emotional journey and highlighting her ability to find gratitude amidst adversity.

In conclusion, Esther Hautzig's emotional journey, from disappointment to gratitude, is effectively portrayed through the author's skilled use of language techniques. The metaphor and juxtaposition highlight Esther's evolving perceptions and emotions, while the repetition emphasizes her determination and resilience. The vivid imagery employed by the author further immerses the reader in Esther's world, allowing them to empathize with her ability to find gratitude and hope even in the face of challenging circumstances.

---
## [deadlocklogic/corrade](https://github.com/deadlocklogic/corrade)@[65d8851d3b...](https://github.com/deadlocklogic/corrade/commit/65d8851d3b3f7cb3e574fb183c5c2e4601e5f6b2)
#### Tuesday 2023-06-13 22:25:03 by Vladimír Vondruš

package/ci: adapt to arbitrary unnecessary Codecov breakages.

They removed the Python uploader because "nobody used it" (it was in
the top 1% of pip packages), and the token-less upload stopped working
some weeks ago (and of course even an error is reported with a zero
return code, YOLO).

I thought I'd upgrade to the "new" uploader, but can't because it's a
fifty megabyte Node.js binary that doesn't even have an ARM version.
So, yeah, it's now using the long-deprecated bash uploader that is long
unsupported instead. Imagine that!

I hate all this technology. Everything is extremely janky, poorly
documented, and any "upgrade" is actually a massive downgrade that
makes everyone angry. What the fuck.

---
## [Warfan1815/cmss13](https://github.com/Warfan1815/cmss13)@[84fd6b6eb7...](https://github.com/Warfan1815/cmss13/commit/84fd6b6eb7fdd48d8499b954dfd216fd5a42ed04)
#### Tuesday 2023-06-13 22:59:28 by ihatethisengine

Medevac Buffs (#1513)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request
Reduces cooldown of medevac from 60 seconds to 20 seconds. PO no longer
needs to manually activate the winch, so medevac can be operated from
the cockpit. What's more, you can operate medevac by interacting with
the medevac system itself, and even if you don't have the skills of a
pilot, you can use it if you have the skills of a doctor (which means
nurse can run medevac). And finally, the medical stretcher is now
automatically activated when deployed.

I know there is a PR by jeser that reduces cooldown, but it stuck in PR
hell anyway and also I changed more stuff.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Since we want to force wounded marines to go shipside, we must provide
them a more convenient way to reach the Almayer. Medevac was always
underutilized because it required too much coordination and unnecessary
actions (e.g. having to activate medical stretcher every time, keep in
mind a huge portion of the medic playerbase still has no idea you need
to do this). PO had to spend their limited fly-by time (which should
normally be used on firemissions) to manually activating the winch,
which was always annoying. And cooldown is ridiculous. You have at best
three minutes of fly-by, so that means you could use medevac only twice
(remember that you needed to run to the system every time) per fly-by,
which is definitely not enough.
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

:cl: ihatethisengine
balance: reduced the medevac cooldown from 60 seconds to 20 seconds.
add: anyone with the skills of a doctor or a pilot can manage the
medevac by interacting with the system itself.
qol: medical stretcher automatically activates when deployed.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[d1cb2e8751...](https://github.com/lessthnthree/tgstation/commit/d1cb2e87519869b5c7baafd66d0e2454cfa6282b)
#### Tuesday 2023-06-13 23:08:45 by Rhials

New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/28870487/2451bc69-db1e-420d-9a18-2f899ca65427

This introduces a new unfavorable situation (non-antagonist random
events that dynamic triggers under certain circumstances), restricted to
planetary maps (Icebox). An earthquake occurs, felt by everyone on the
map, forming a fault that tears the a hole somewhere on the station.

The fault zone is indicated by shaking tiles, which gives a chance
(about 30 seconds) for you to move your machinery/property/crewmembers
out of the way. If you're on those tiles when the fault forms, get ready
to take a nasty fall.

Anything caught in the fault zone as it collapses inward will be
destroyed, violently, _before_ being dropped down into the z-level
below.


![image](https://github.com/tgstation/tgstation/assets/28870487/56916c9f-c8da-4ffb-9d8b-7e940e92bbc2)

These can also happen as a random event, however their rarity is on-par
with that of a meteor storm.

This also adds a helper for finding a midpoint turf between two provided
turfs, thanks to ZephyrTFA.

This idea basically possessed me over the course of a few days, and I
found myself unable to work on anything else until I had it complete.
I'm glad its done.
## Why It's Good For The Game

Gives Icebox its own big "environmental disaster" event. I'm hoping it
isn't received as being too destructive, but mind that this is meant to
be an equal to the dreaded meteor storm.

Also makes it so that unfavorable events aren't a coinflip between a
portal storm/rod on planetary maps.
## Changelog
:cl: Rhials
add: Chasmic Earthquake random event, exclusive to Icebox. Tears a huge
chasm in the hull of the station. Watch out for shaking tiles!
sound: Adds sounds for distant rumbling, metal creaking, and rubble
shaking.
imageadd: Achievement icon for getting sucked up in an earthquake chasm.
/:cl:

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[59dd02fe7c...](https://github.com/ZephyrTFA/tgstation/commit/59dd02fe7cd54b4153b294ccb965249c587f189d)
#### Tuesday 2023-06-13 23:10:09 by san7890

Welding Fuel Tanks now log_bomber when hit by projectile (#75885)

## About The Pull Request

This was intended behavior, but I think a lot of bullshit over the years
sorta corrupted this proc's intention. Anyways, we just override the
whole ass proc for this one check, give a good return value (or at least
the same one that we were always giving) if our criteria is met, rather
than deal with the problems that parent was feeding us.


![image](https://github.com/tgstation/tgstation/assets/34697715/e2b39140-d365-43aa-8834-2740f9fa5036)

The specific issue here was that the parent of `bullet_act()` was
invoking `take_damage()` which prematurely invoked `boom()` which
invokes `qdel()`, meaning that the `QDELETED()` check would _always_
early return without fail every time.

Let's just do our own thing here.
## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/34697715/ca8fdeba-9f5d-4bed-afba-88824d389cfb)

Intended behavior actually works.
## Changelog
:cl:
admin: Shooting a welding fuel tank (big or small) with a projectile
will now accurately post to list_bombers with the name of the person who
shot the projectile from the gun. If you don't know how to list-bombers,
it will also be present in game.log for your viewing pleasure.
/:cl:

---
## [Michaelmanicotti/poetry](https://github.com/Michaelmanicotti/poetry)@[496d461ecf...](https://github.com/Michaelmanicotti/poetry/commit/496d461ecfadf5807b64d2ca04127f9180d5fab8)
#### Tuesday 2023-06-13 23:13:29 by Michaelmanicotti

Rename Movement III | To the pretty boy who stole my heart, Fuck You. to Movement III | To the pretty boy I can't stop writing poems about, Fuck You for stealing my heart.

---
## [tired-wired/Shiptest](https://github.com/tired-wired/Shiptest)@[09e95cdfbc...](https://github.com/tired-wired/Shiptest/commit/09e95cdfbc8337b5b7a84a088c32b458ee1d996d)
#### Tuesday 2023-06-13 23:35:51 by Bjarl

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
## [tired-wired/Shiptest](https://github.com/tired-wired/Shiptest)@[c21670412d...](https://github.com/tired-wired/Shiptest/commit/c21670412dff10f4a3a1b1ab1e72f53294581d25)
#### Tuesday 2023-06-13 23:35:51 by Bjarl

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
## [tired-wired/Shiptest](https://github.com/tired-wired/Shiptest)@[0410075cc8...](https://github.com/tired-wired/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Tuesday 2023-06-13 23:35:51 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [AnonymousHacker1279/ImmersiveWeapons](https://github.com/AnonymousHacker1279/ImmersiveWeapons)@[520fc1eefb...](https://github.com/AnonymousHacker1279/ImmersiveWeapons/commit/520fc1eefbbe34a544ad164179f09b65faa17373)
#### Tuesday 2023-06-13 23:39:36 by Nicholas Smit

More accessories

Add new accessories and a new curse item.

Blademaster Emblem: Increase melee damage by 10% and add a 30% chance to inflict a bleed effect. Obtained via crafting.

Deadeye Pendant: Increases damage over distance, up to 20% at 100 meters. Not currently obtainable, but will be later.

Bloody Sacrifice: A permanent, consumable item that grants a wide array of effects. The effects are +50% damage taken, permanent hunger effect, and 10% less damage dealt, with the bonus of a permanent level 3 looting effect bonus and a 25% chance to roll loot drops a second time entirely. Upon crafting, it requires the player to kill 100 entities while holding it in the inventory before it can be used. The effects are permanent without using cheats to remove them, making it a Hardcore-style experience.

Curse Cleaning Soap: A creative-only item which can be used to clear curses like the Bloody Sacrifice.

---

