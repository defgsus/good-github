## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-28](docs/good-messages/2022/2022-01-28.md)


1,687,865 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,687,865 were push events containing 2,697,536 commit messages that amount to 196,115,418 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [KDr2/ghc](https://github.com/KDr2/ghc)@[31088dd32a...](https://github.com/KDr2/ghc/commit/31088dd32a4dbbed649dff0700610eb7ed7a9fca)
#### Friday 2022-01-28 00:03:16 by David Feuer

Add test supplied in T20996 which uses data family result kind polymorphism

David (@treeowl) writes:

> Following @kcsongor, I've used ridiculous data family result kind
> polymorphism in `linear-generics`, and am currently working on getting
> it into `staged-gg`. If it should be removed, I'd appreciate a heads up,
> and I imagine Csongor would too.
>
> What do I need by ridiculous polymorphic result kinds? Currently, data
> families are allowed to have result kinds that end in `Type` (or maybe
> `TYPE r`? I'm not sure), but not in concrete data kinds. However, they
> *are* allowed to have polymorphic result kinds. This leads to things I
> think most of us find at least quite *weird*. For example, I can write
>
> ```haskell
> data family Silly :: k
> data SBool :: Bool -> Type where
>   SFalse :: SBool False
>   STrue :: SBool True
>   SSSilly :: SBool Silly
> type KnownBool b where
>   kb :: SBool b
> instance KnownBool False where kb = SFalse
> instance KnownBool True where kb = STrue
> instance KnownBool Silly where kb = Silly
> ```
>
> Basically, every kind now has potentially infinitely many "legit" inhabitants.
>
> As horrible as that is, it's rather useful for GHC's current native
> generics system. It's possible to use these absurdly polymorphic result
> kinds to probe the structure of generic representations in a relatively
> pleasant manner. It's a sort of "formal type application" reminiscent of
> the notion of a formal power series (see the test case below). I suspect
> a system more like `kind-generics` wouldn't need this extra probing
> power, but nothing like that is natively available as yet.
>
> If the ridiculous result kind polymorphism is banished, we'll still be
> able to do what we need as long as we have stuck type families. It's
> just rather less ergonomical: a stuck type family has to be used with a
> concrete marker type argument.

Closes #20996

Co-authored-by: Matthew Pickering <matthewtpickering@gmail.com>

---
## [tromey/gdb](https://github.com/tromey/gdb)@[299953ca95...](https://github.com/tromey/gdb/commit/299953ca95cc5ac47e52236e2eeb44afc5369134)
#### Friday 2022-01-28 00:31:32 by Andrew Burgess

gdb/python: handle non utf-8 characters when source highlighting

This commit adds support for source files that contain non utf-8
characters when performing source styling using the Python pygments
package.  This does not change the behaviour of GDB when the GNU
Source Highlight library is used.

For the following problem description, assume that either GDB is built
without GNU Source Highlight support, of that this has been disabled
using 'maintenance set gnu-source-highlight enabled off'.

The initial problem reported was that a source file containing non
utf-8 characters would cause GDB to print a Python exception, and then
display the source without styling, e.g.:

  Python Exception <class 'UnicodeDecodeError'>: 'utf-8' codec can't decode byte 0xc0 in position 142: invalid start byte
  /* Source code here, without styling...  */

Further, as the user steps through different source files, each time
the problematic source file was evicted from the source cache, and
then later reloaded, the exception would be printed again.

Finally, this problem is only present when using Python 3, this issue
is not present for Python 2.

What makes this especially frustrating is that GDB can clearly print
the source file contents, they're right there...  If we disable
styling completely, or make use of the GNU Source Highlight library,
then everything is fine.  So why is there an error when we try to
apply styling using Python?

The problem is the use of PyString_FromString (which is an alias for
PyUnicode_FromString in Python 3), this function converts a C string
into a either a Unicode object (Py3) or a str object (Py2).  For
Python 2 there is no unicode encoding performed during this function
call, but for Python 3 the input is assumed to be a uft-8 encoding
string for the purpose of the conversion.  And here of course, is the
problem, if the source file contains non utf-8 characters, then it
should not be treated as utf-8, but that's what we do, and that's why
we get an error.

My first thought when looking at this was to spot when the
PyString_FromString call failed with a UnicodeDecodeError and silently
ignore the error.  This would mean that GDB would print the source
without styling, but would also avoid the annoying exception message.

However, I also make use of `pygmentize`, a command line wrapper
around the Python pygments module, which I use to apply syntax
highlighting in the output of `less`.  And this command line wrapper
is quite happy to syntax highlight my source file that contains non
utf-8 characters, so it feels like the problem should be solvable.

It turns out that inside the pygments module there is already support
for guessing the encoding of the incoming file content, if the
incoming content is not already a Unicode string.  This is what
happens for Python 2 where the incoming content is of `str` type.

We could try and make GDB smarter when it comes to converting C
strings into Python Unicode objects; this would probably require us to
just try a couple of different encoding schemes rather than just
giving up after utf-8.

However, I figure, why bother?  The pygments module already does this
for us, and the colorize API is not part of the documented external
API of GDB.  So, why not just change the colorize API, instead of the
content being a Unicode string (for Python 3), lets just make the
content be a bytes object.  The pygments module can then take
responsibility for guessing the encoding.

So, currently, the colorize API receives a unicode object, and returns
a unicode object.  I propose that the colorize API receive a bytes
object, and return a bytes object.

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[1f70226654...](https://github.com/Sonic121x/Skyrat-tg/commit/1f70226654438f75811a2d59ad9c52bf88c048fc)
#### Friday 2022-01-28 00:54:47 by SkyratBot

[MIRROR] Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit [MDB IGNORE] (#11027)

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit

Co-authored-by: Iamgoofball <iamgoofball@gmail.com>

---
## [jjpark-kb/tgstation](https://github.com/jjpark-kb/tgstation)@[a2fa7799f3...](https://github.com/jjpark-kb/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Friday 2022-01-28 01:06:15 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [Ichthyostega/yoshimi](https://github.com/Ichthyostega/yoshimi)@[881b250912...](https://github.com/Ichthyostega/yoshimi/commit/881b25091274d21e186f411909adea24b0b81ae3)
#### Friday 2022-01-28 01:12:45 by Ichthyostega

[padthread] Run "synchronous Apply" from the Cmd-Dispatch (background) thread

It used to be that way before all the reworking of PADSynth wavetable building.
Seemingly also better, since we don't block the Synth-Thread then, only the
Command dispatch and indirectly also the CLI.

However, the non-blocking wavetable builds are still triggered directly from
the Synth-Thread (commandSendReal -> commandPad() ), since there is no reason
to go through the background Cmd thread (sortResultsThread). For that reason,
we now distinguish in InterChange::commandPad() if the requested "Apply" is
really blocking, and forward to indirectTransfers only in that case.

Remark: cleaning up an "evil hack"
The ENUM PART::control::padsynthParameters "magically happened" to have
the same integer value 104 as PADSYNTH::control::applyChanges

It cost me literally hours to find out thus how the dispatch of "Apply"
to the background thread works.

---
## [PetMudstone/Shiptest](https://github.com/PetMudstone/Shiptest)@[2c3e36df75...](https://github.com/PetMudstone/Shiptest/commit/2c3e36df75d18f0970a199d0780f04215033232c)
#### Friday 2022-01-28 03:57:35 by Omppusolttu

Scrapper-b Update (#417)

* Discovery Update

* Fuck you. *unfucks your scrapper-b

* Add files via upload

---
## [PetMudstone/Shiptest](https://github.com/PetMudstone/Shiptest)@[bccb2d32d3...](https://github.com/PetMudstone/Shiptest/commit/bccb2d32d3f82bfa5ea3e24543f08590c45b618e)
#### Friday 2022-01-28 03:57:35 by Omppusolttu

Scrapper Update (#416)

* scrapper update

* fix

* Fuck you. *unfucks your scrapper-A*

* Add files via upload

---
## [dfrank2781/week-03-salter.md](https://github.com/dfrank2781/week-03-salter.md)@[412cfca901...](https://github.com/dfrank2781/week-03-salter.md/commit/412cfca9016d1a7aab5a8e9eec3a93b0179a3f93)
#### Friday 2022-01-28 05:48:51 by dfrank2781

# writing reflection <--! great read -->

In my opinion, there could be a few different forms of contemporary tools that could be used to create art that is a Gesamtkunstwerk, or a full work of art made of multiple components. When one looks at artwork, some elements may pop out more than others. Some may be less visible, or less eye catching than others, but each serves its own purpose. One thing I feel could be used is dramatic lighting. Dramatic light can be shown on the side of a person's face, their body, or even their entire face. This can help the audience feel the element of surprise or suspense leading up to what the actor is supposed to portray in a play. I also believe that as aforementioned in the Entangled reading by Chris Salter, sound affects are very key in conveying different things as well, Depending on how loud or soft the music is, one can also feel certain emotions of intensity, or serenity in a given setting, or point in a play.


      Another thing that I believe can really sell a Gesamtkunstwerk is a collection of varying facial expressions. As we've often heard, one's body language, or facial expressions can say a lot about a person, or how they're feeling toward the speaker/audience. Some prime examples from Net Art Anthology are Arcangel Surfware, The World in 24 Hours, and Floodnet. Varying facial expressions in one scene can show the multiple emotions faced by the different characters in the room at any given time. It makes for a much more entertaining performance, and overall visual appeal within stage acting. Lastly, the atmosphere, or overall visual scene can play a big role in how a Gesamtkunstwerkis decided upon. Often times, when we think of a beautiful scenery, we consider it a complete work of art when we can see it very well from an intriguing angle.  For example, in Net Art Anthology, The Thing, Untitled, and Starrynight do a great job conveying this example. When one is able to see a wide spectrum, or field of view, it cause cause a dramatic feeling, and visual affect. As similarly mentioned in the article, when the stage came in one show formed a pyramid like shape, and everything came together as one, it made for a great spectacle for the eye to see, and a much more enjoyable atmosphere and performance.

---
## [dsonbill/Reactor](https://github.com/dsonbill/Reactor)@[6080fc3854...](https://github.com/dsonbill/Reactor/commit/6080fc3854e1c2cf03b03439bd8fe3c0c57f4441)
#### Friday 2022-01-28 05:51:39 by William C. Donaldson

Invert Me Again Foir Five Hours, Bitch! JK I love and hate you, go die in a fire you stupid fucking whore. call for good time.

---
## [Link-Jon/CC-OSish](https://github.com/Link-Jon/CC-OSish)@[a52e15b626...](https://github.com/Link-Jon/CC-OSish/commit/a52e15b626591a7df0a78bb87877e32a8ae51b29)
#### Friday 2022-01-28 07:25:19 by Link-Jon

Rename (math->logic) and switch()

Adding switch function... however im not entirely sure how to impliment it yet. likely it will come down to running binary functions, which would be a pain but... oh well. Ah, for loops... thanks writing! That helps on the retesting the thing... but i will need to check something else.

switch(num1,num2,arry,act,equal)
num1 should be an array of nums, and num2 should be a number
arry should be an array of functions (num = [foo1,foo2]--NOTE, not the return of a function, like 'foo()', but 'foo' only! Moreso a refrence of a function)


Keep in mind that the switch() function isnt really done and.. all i did so far is error handling. I dont think i will be able to finish it properly untill i can get back into minecraft, to test it.
Oh well... im tired. Really tired. good night...
err
correction. did it. Needs a little bit more work, but its functioning

---
## [betrusted-io/xous-core](https://github.com/betrusted-io/xous-core)@[25bccd9446...](https://github.com/betrusted-io/xous-core/commit/25bccd9446ec7aaecb998393c3e50c9c7eaf3dde)
#### Friday 2022-01-28 07:32:07 by bunnie

THE BALDEST YAK: keyboard injection now working

I wrote in a commit yesterday how there was no ROI on doing this
yet somehow I kept on doing it. I blame poor impulse control.

Turns out there was a series of race conditions and bugs that
caused this thing to "mostly work" on the first go at it but
really hard to debug and get very right.

1. Litex UART has a weird undocumented API. You advance the Rx
FIFO by writing `1` to the PENDING bit, and no other way. However,
you determine if there are any more characters to receive by
reading the EMPTY bit and seeing if it is 1. The previous method
wrote `1` to the PENDING bit and then used the PENDING bit to
see if a character was available, under the theory that the
PENDING bit would be set again if there was still a character.
This is somewhat true, except that the PENDING bit is set only
some amount of time later which is about comparable to a few
CPU instructions, so if you had a fast loop path the PENDING
bit would show as cleared and you'd exit, which would cause
no further interrupts to fire because the interrupt was
effecitvely not acknowledged.

This isn't written up anywhere but I figured this out by
just reading the source code for Litex UART and BIOS:
https://github.com/enjoy-digital/litex/blob/e8be3915041707860e70b15d062661fc1f67a09f/litex/soc/cores/uart.py#L264-L279
https://github.com/enjoy-digital/litex/blob/ccd3ab17be1f8770c59ec1c62e0285d3bac3cc26/litex/soc/software/libbase/uart.c#L38-L44

2. I had the Key Injector IP block in the `sys` domain, which
would have its clock cut when the CPU went to sleep, which would
cause input characters to disappear when the CPU went into power
saving. moving this to "always on" domain fixes that.

3. I had the UART PHY in the always on block (so you could
send or receive exactly one character), but not the
separate UART block (which contained the FIFOs).
The UART block would also go into power
savings, and this would cause FIFO entries to go missing.

4. Escape sequences get sent as a burst of characters. The Key Injector
originally did not have a FIFO of its own, so it would only
remember the *last* key of the sequence that was written, causing
some keys to be dropped occassionally. Adding a 16-deep FIFO
to the injector fixes this.

5. The code I had to read out the injector's results was designed with
the "strobe" bit (to indicate that the FIFO had characters) in the
same regsiter as the character itself. Thus the loop that 1. checked
if the fifo was empty then 2. read and forwarded the character
would actually perform two reads from the FIFO. However, this "mostly worked"
I think because the FIFO retains the last value that was written
even when it was empty, so if only one character was read at a time
everything was fine. It only didn't work when you stuffed two characters
in there, as you'd drop the first one. Reading the FIFO once and
then interpreting the code with a bitmask fixes this.

6. The escape sequences, in their full glory with no dropped characters,
required a refactored parsing routine, which I have now added.

7. backspace->delete mappings, the bane of computer engineers since 1960.

OK. very bald yak. Here I lay down the shears next to several
mooshi pillows stuffed with the finest Yak hair.

---
## [betrusted-io/xous-core](https://github.com/betrusted-io/xous-core)@[ea31f54a79...](https://github.com/betrusted-io/xous-core/commit/ea31f54a796680df704067d4da7cb38015cc2d7d)
#### Friday 2022-01-28 07:47:23 by bunnie

console escape codes working better

just couldn't let it go. figured out the issue is a race condition
in how the Litex UARTs are constructed...I don't know how Litex
normally handles this kind of situation but they have this funky
construction where reading the fifo doesn't advance it, you have
to...clear the pending bit. I think it was meant to be a "clever"
thing that saves an instruction or something like that since you
always have to clear the pending bit.

Anyways, the previous incarnation of this loop checked to see
if the pending bit was set again and if it was it'd run back
and fetch another character. This turns out to be a bad idea
because the pending bit goes through a multireg and other stuff
before it's readable which means it has a lot of delay on it.
This leads to a race condition.

This version actually checks if the fifo is empty and if it isn't,
it reads the character *and* pumps the pending bit (because
the FIFO doesn't auto-advance when you read it, you have to clear
the pending bit).

This works a lot better, but it's not at all well documented how
this works and it's very hard to tell from reading the source code
because it's written using really fancy migen abstractions that
are also poorly documented and have a lot of cursed constructions.

Anyways. At least the console doesn't die now when you type
a control character, *but* you do have the problem that the
escape codes get mis-interpreted sometimes. If it really really
becomes important later on to fix that it would involve tracing
out the sequence of keys that arrive at InjectKey and figuring
out if things are coming out of order or what is triggering the
bad escape codes.

---
## [valoeghese/Dash](https://github.com/valoeghese/Dash)@[39f7847ea9...](https://github.com/valoeghese/Dash/commit/39f7847ea948b74d9dab6b36057d1ee54c258007)
#### Friday 2022-01-28 09:38:06 by Valoeghese

I wake up, man that night flew by I say what's up to the beautiful-ness that's outside
And it may be only blocks but you gotta' look past that
To me it's all big jungles and grasslands
I need some tools
Now what should I pick-axe and a sword
Yah that should do that trick
And back never bored, creeper time-bomb ticks
I'm so fast and I get outta' there quick
And it's that double tap sprint, gotta' love it
I'm runnin' fast, tryin' make somethin' of it
And I'm always running out of food to eat
I guess ten loaves of bread just wasn't enough for me
Hash tag #firstworldminecraftproblems
Wait, 32 ingots just to build an iron golem
Woowee better get minin'
Them I'm like OMG what's that shinin'

---
## [fanglingsu/dwm](https://github.com/fanglingsu/dwm)@[67d76bdc68...](https://github.com/fanglingsu/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2022-01-28 10:21:31 by Chris Down

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
## [NoComment1105/ConsistencyPlus](https://github.com/NoComment1105/ConsistencyPlus)@[15b8b1dea8...](https://github.com/NoComment1105/ConsistencyPlus/commit/15b8b1dea8d0f7364468326f9821d80ab9b77418)
#### Friday 2022-01-28 10:25:17 by Siuol

This is not the number one champion sound.

In this commit I did the following:

Fixed the Cobbled Blackstone issue #92

Finally a reference people will understand. (Please don't victory royale this please don't please I beg of you absolutely do not make this the fortnite parody please don't please I just wanna do this in peace please this is just the haha funny blackstone fix please isn't that funny enough for you haha blackstone fix haha funny funny joke Siuol I think Siuol is quite funny without the victory royale please don't victory royale this.)

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

---
## [avar/git](https://github.com/avar/git)@[24c3207e94...](https://github.com/avar/git/commit/24c3207e949573f8a8b25d4cf46baf87c0063d0f)
#### Friday 2022-01-28 11:14:10 by Ævar Arnfjörð Bjarmason

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
## [avar/git](https://github.com/avar/git)@[f7a4610f54...](https://github.com/avar/git/commit/f7a4610f54c8982f233dd3cd81f7d155f15dc515)
#### Friday 2022-01-28 11:14:10 by Ævar Arnfjörð Bjarmason

usage API: add "core.usageAddSource" config to add <file>:<line>

Optionally extend the support that BUG() has had for emitting line
numbers to the {usage,fatal,error,warning}{,_errno}() functions.

Before we'd unconditionally get error messages like:

    $ git -c core.x=y config --get --bool core.x
    fatal: bad boolean config value 'y' for 'core.x'

Which can be changed with core.usageAddSource=true to include the file
and line numbers:

    $ git -c core.usageAddSource=true -c core.x=y config --get --bool core.x
    fatal: config.c:1241: bad boolean config value 'y' for 'core.x'

As the added documentation notes this is primarily intended to be
useful to developers of git itself, but is being exposed as a user
setting to e.g. help file better bug reports.

This also adds a "GIT_TEST_USAGE_ADD_SOURCE" setting intended to run
the test suite in this mode.

Currently it has a lot of failures. Most of those are rather trivial,
and can be "fixed" by pointing GIT_TEST_CMP to a "diff -u" that does a
s/^(usage|fatal|error|warning): [^:]+:[0-9]+/$1/g on its input files,
and likewise for a "grep" wrapper that does the same.

Even if we can't run the tests in this mode yet I'd like to have this
for ad-hoc debugging, and to make it easier to work towards running
the tests in this mode. If we can turn this on permanently it'll be
much easier to read test output, as we won't need to worry about the
indirection of looking up where an error might have been emitted,
which can be especially painful when the message being emitted isn't
unique within git.git.

This new code needs to be guarded by the "dying" variable for the
reasons explained in 2d3c02f5db6 (die(): stop hiding errors due to
overzealous recursion guard, 2017-06-21), and for those same reasons
it's racy under multi-threading.

Here the worst case is that incrementing the variable will run away
from us, and we won't get our desired <file>:<line> number. That's OK
in this case, those cases should be isolated to the config code (if we
can't parse the config), memory allocation etc, but we'll get it right
in the common cases.

Using GIT_TEST_USAGE_ADD_SOURCE should be immune from any racyness, as
it only needs a getenv() and git_parse_maybe_bool(), which won't die.

Add a repo_cfg_bool_env() wrapper to repo-settings.c for
GIT_TEST_USAGE_ADD_SOURCE, in 3050b6dfc75 (repo-settings.c: simplify
the setup, 2021-09-21) I indicated that the GIT_TEST_MULTI_PACK_INDEX
env variable/config pair in that file has odd semantics, but users of
repo_cfg_bool_env() have straightforward and expected semantics. If
the environment variable is set (true or false) we'll use it,
otherwise we'll use the config, and finally fall back on the
default (of "false", in this case).

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[e1313b9636...](https://github.com/avar/git/commit/e1313b9636f40ef7c9e663f49f4c86254d1f513f)
#### Friday 2022-01-28 11:14:10 by Ævar Arnfjörð Bjarmason

usage API: make the "{usage,fatal,error,warning,BUG}: " translatable

In preceding commits the vreportf() function was made static, so we
know it's only being called with a limited set of fixed prefixes. Pass
an enum indicating the kind of usage message we're emitting instead,
which means that we can fold the BUG_vfl_common() functionality
directly into it.

Since we've now got one place were we're emitting these usage messages
we can make them translatable.

We need to be careful with this function to not malloc() anything, as
a failure in say a use of strbuf_vaddf() would call xmalloc(), which
would in turn call die(), but here we're using static strings, either
from libintl or not.

I was on the fence about making the "BUG: " message translatable, but
let's do it for consistency. Someone who doesn't speak a word of
English may not know what "BUG" means, but if it's translated they
might have an easier time knowing that they have to report a bug
upstream. Since we'll always emit the line number it's unlikely that
we're going to be confused by such a report.

As we've moved the BUG_vfl_common() code into vsnprintf() we can do
away with one of the two checks for buffer sizes added in
116d1fa6c69 (vreportf(): avoid relying on stdio buffering, 2019-10-30)
and ac4896f007a (fmt_with_err: add a comment that truncation is OK,
2018-05-18).

I.e. we're being overly paranoid if we define the fixed-size "prefix"
and "msg" buffers, are OK with the former being truncated, and then
effectively check if our 256-byte buffer is larger than our 4096-byte
buffer. I wondered about adding a:

    assert(sizeof(prefix) < sizeof(msg)); /* overly paranoid much? */

But I think that would be overdoing it. Anyone modifying this function
will keep these two buffer sizes in mind, so let's just remove one of
the checks instead.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [adrianstanescu/lol-stats](https://github.com/adrianstanescu/lol-stats)@[493db08316...](https://github.com/adrianstanescu/lol-stats/commit/493db08316edf8744030ca5bf9eb79005302fdc8)
#### Friday 2022-01-28 11:26:06 by Adrian Stanescu

Add more awards (#7)

Trailblazer, Combat Medic, Dominator,
Protector, Finisher, Pain Bringer,
Siege Master, Creep Lover,
Crowd Controller, Rich Bitch, Al-Qaeda,
Pressing Intensifies

Co-authored-by: Adrian Stanescu <adrianstanescu@thinkmedia.ro>

---
## [AvanaPY/DV1655_Lab1](https://github.com/AvanaPY/DV1655_Lab1)@[c11196047c...](https://github.com/AvanaPY/DV1655_Lab1/commit/c11196047c6eba142e01693e2895c52b5375318c)
#### Friday 2022-01-28 11:33:59 by Emil Karlström

killed all shift/reduce errors, oh my god fuck you

---
## [BaconLords/Random-Shit](https://github.com/BaconLords/Random-Shit)@[2d3f645095...](https://github.com/BaconLords/Random-Shit/commit/2d3f645095c5a4dea580b9d84860d0c635e4950d)
#### Friday 2022-01-28 11:55:37 by Bacon Lord

Create FLAMINGO ON YOUTUBE FAV FAN YEAH BACONLORD IS SUPER PRO ISH AND EVERYONE ELSE SUCKS BIG MAN NIGGER BALLES LIKE LITTLE KIDS IN BED TOUCHING THERE DICK AND SUCKING ON COCK AND PUTTING IT IN YOUR MOUTH HOLE SO BIG AND JUICIY.lua

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[10ba80973b...](https://github.com/vincentiusvin/tgstation/commit/10ba80973bfc977b17aa116f3b630862e9e70a7c)
#### Friday 2022-01-28 13:28:10 by Kylerace

makes most statpanel tabs update a tenth or so as often (>= 4 seconds instead of 4 deciseconds) because theyre wastful of cpu (#63991)

makes most updating stat panel tabs update once every 4 seconds instead of 4 deciseconds, but switching tabs instantly updates statpanel data for you. also makes examining a turf make flat icons for a maximum of 10 contents instead of 30 because its ridiculous to call getFuckingFlatIcon() wrappers that many times. also makes SSfluids not have SS_TICKER and updates its wait accordingly because theres no reason for it to be a ticker subsystem

the mc tab updates every 2 seconds unless someone has the pref enabled to refresh it quickly because SOME UNILLUMINATED LEMONS absolutely must watch overtime spikes in real time

statpanels can take between 1-3% of masters total processing time at very high pop, which is silly considering theres no need for someone to know any of the data updated accurate to less than half of a second. The only reason it needed to update so fast was because it looked awful when switching tabs, which will only be updated on the next fire. now switching tabs updates data instantly so theres no need to update the rest of the data quickly.

also makes each stat tab update into its own proc so we can tell how much each tab update costs

---
## [HugoOdaX/fulpstation](https://github.com/HugoOdaX/fulpstation)@[c449fbb56c...](https://github.com/HugoOdaX/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Friday 2022-01-28 13:47:47 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [Polynomial-C/ppp](https://github.com/Polynomial-C/ppp)@[81ad945630...](https://github.com/Polynomial-C/ppp/commit/81ad945630120cc1c27c8bb00503be42b76ff202)
#### Friday 2022-01-28 13:52:00 by Jaco Kroon

Expand byte count statistics to 64 bits (#298)

* Add Gigawords to radius packets where applicable.

IMPORTANT NOTE:  The ioctl() only supports 32-bit counters.  In order t
obtain 64-bit counters, these are now pulled in from sysfs (it's assumed
to be mounted on /sys which I'm assuming is standard).

It is unknown whether sysfs will be available everywhere, as such, keep
the ioctl() method in place, but attempt to detect wrap-overs.

If the sysfs mechanism fails, fail back to the ioctl().

Given maximum data rates, the intervals between calling this needs to be
such that no more than 4GB (2^32) bytes are sent or received in any
given interval.  Mostly important for radius plugin where data
accounting may be in effect.

Towards this, a timer interval on 25 seconds is set to force a ioctl()
poll irrespective of the rate of stats update calls.  This may be
important for especially radius that needs to provide interim-update
intervals, if the interim updates is too long and the counters could
wrap-over twice in a single interval.  At 25 seconds we should detect
all wraps up to an effective data rate of 1.37Gbps, which for my
purposes is adequate.

Possible downsides, 4 files are opened, read and closed every time
statistics is requested.  This results in 12 system calls every single
time statistics is required, compared to 1 for the ioctl.  Efficiency is
unknown, but as a rule of thumb fewer system calls are better, this is
however not a critical path in my opinion, so should not be a problem.
If required I can run a few benchmarks using gettimeofday() to measure
actual impact.

Signed-off-by: Jaco Kroon <jaco@uls.co.za>

* Use netlink if possible to obtain 64-bit stats.

This uses two system calls per round.

This should be preferred where available.  It seems the RTM_GETSTATS was
only added from 2016 some point (4.7.0 as per pali), which is in my
opinion old, but given experience with certain embedded systems does
need to be supported.

Signed-off-by: Jaco Kroon <jaco@uls.co.za>

Co-authored-by: Jaco Kroon <jaco@iewc.co.za>

---
## [kraj/gcc](https://github.com/kraj/gcc)@[aeac414923...](https://github.com/kraj/gcc/commit/aeac414923aa1e87986c7fc6f9b921d89a9b86cf)
#### Friday 2022-01-28 14:04:25 by Thomas Schwinge

Revert "Fix PR 67102: Add libstdc++ dependancy to libffi" [PR67102]

This reverts commit db1a65d9364fe72c2fff65fb2dec051728b6f3fa.

On 2021-09-17T01:01:39-0700, Andrew Pinski via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
> On Fri, Sep 17, 2021 at 12:46 AM Thomas Schwinge <thomas@codesourcery.com> wrote:
>> On 2021-09-15T13:56:37-0700, apinski--- via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
>> > The error message is obvious -funconfigured-libstdc++-v3 is used
>> > on the g++ command line.  So we just add the dependancy.
>>
>> > --- a/Makefile.def
>> > +++ b/Makefile.def
>> > @@ -592,6 +592,7 @@ dependencies = { module=configure-target-fastjar; on=configure-target-zlib; };
>> >  dependencies = { module=all-target-fastjar; on=all-target-zlib; };
>> >  dependencies = { module=configure-target-libgo; on=configure-target-libffi; };
>> >  dependencies = { module=configure-target-libgo; on=all-target-libstdc++-v3; };
>> > +dependencies = { module=configure-target-libffi; on=all-target-libstdc++-v3; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libbacktrace; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libffi; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libatomic; };
>>
>> I'm confused, because given that this 'Makefile.def' change only has the
>> following effect:
>>
>> > --- a/Makefile.in
>> > +++ b/Makefile.in
>> > @@ -61261,6 +61261,7 @@ all-bison: maybe-all-intl
>> >  all-flex: maybe-all-intl
>> >  all-m4: maybe-all-intl
>> >  configure-target-libgo: maybe-all-target-libstdc++-v3
>> > +configure-target-libffi: maybe-all-target-libstdc++-v3
>> >  configure-target-liboffloadmic: maybe-configure-target-libgomp
>> >  all-target-liboffloadmic: maybe-all-target-libgomp
>> >  configure-target-newlib: maybe-all-binutils
>>
>> ... isn't that actually a no-op, because we already had such a dependency
>> listed?  Now twice:
>>
>>     $ grep -n -F 'configure-target-libffi: maybe-all-target-libstdc++-v3' -- Makefile.in
>>     61264:configure-target-libffi: maybe-all-target-libstdc++-v3
>>     61372:configure-target-libffi: maybe-all-target-libstdc++-v3
>>
>> Compared to the existing one, the one you've added is additionally
>> restricted by '@unless gcc-bootstrap'.
>>
>> I noticed this as I remembered that on our og[...] development branches
>> we have a patch in the opposite direction: get rid of this dependency via
>> removing 'lang_env_dependencies = { module=libffi; cxx=true; };' from
>> 'Makefile.def'.  See
>> <http://mid.mail-archive.com/alpine.DEB.2.21.9999.1812201344250.99920@build7-trusty-cs.sje.mentorg.com>
>> "Disable libstdc++ dependency for libffi".  (Maciej CCed in case you have
>> any further thoughts on that.)
>
> Oh, I see what happened now, the old bug was actually fixed by r6-5415
> which added cxx=true.
> So yes my patch is actually not needed and can be reverted.
> I tried to look to see if there was a dependency was there but for
> some reason I did not see it.

---
## [thoughtbot/hotwire-example-template](https://github.com/thoughtbot/hotwire-example-template)@[ecb43c4d52...](https://github.com/thoughtbot/hotwire-example-template/commit/ecb43c4d52284aee687ec514e27043fd4f147d8b)
#### Friday 2022-01-28 14:32:55 by Sean Doyle

Hiding the results when inactive

Now that we're overlaying our results on top of the rest of the page,
we'll only want to do so when the end-user is actively searching. We'll
also want to avoid needless requests to the server with empty query
text.

Lucky for us, browsers provide a built-in mechanism to prevent bad
`<form>` submissions and to surface a field's correctness: [Constraint
Validations][]!

In our case, there are two ways that a search can be invalid:

1. The query `<input>` element is completely blank.
2. The query `<input>` element has a value, but that value is comprised
   of entirely empty text characters.

To consider those states invalid, render the `<input>` with [required][]
and [pattern][] attributes:

```diff
--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
       <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results">
         <label for="search_query">Query</label>
-        <input id="search_query" name="query" type="search">
+        <input id="search_query" name="query" type="search" pattern=".*\w+.*" required>
```

By default, browsers will communicate a field's invalidity by
rendering a field-local tooltip message. While it's important to
minimize the number of invalid HTTP requests sent to our server, a
type-ahead search box works best when users can incrementally make
changes to the query string. In our case, a validation message could
disruptive or distract a user mid-search.

To have more control over the validation experience, we'll need to write
some JavaScript. Let's create
`app/javascript/controllers/form_controller.js` to serve as a [Stimulus
Controller][]:

```javascript
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
}
```

Next, we'll need to listen for browsers' built-in [invalid][] events to
fire. When they do, we'll route them to the `form` controller as a
[Stimulus Action][] named `hideValidationMessage`:

```diff
--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
     <header>
-      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results">
+      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results"
+        data-controller="form" data-action="invalid->form#hideValidationMessage:capture">
         <label for="search_query">Query</label>
```

One quirk of [invalid][] events is that they _do not_ [bubble up][]
through the [DOM][]. To account for that, our `form` controller will
need to act on them during the capture phase. Stimulus supports the
[`:capture` suffix][capture] as a directive to hint to our action
routing that the controller's action should be invoked during the
capture phase of the underlying event listener.

Once we're able to act upon the [invalid][] event, we'll want the
`form#hideValidationMessage` action to [prevent the default behavior][]
to stop the browser from rendering the validation message.

```diff
--- a/app/javascript/controllers/form_controller.js
+++ b/app/javascript/controllers/form_controller.js
 import { Controller } from "@hotwired/stimulus"

 export default class extends Controller {
+  hideValidationMessage(event) {
+    event.stopPropagation()
+    event.preventDefault()
+  }
 }
```

When an ancestor `<form>` element contains fields that are invalid, it
will match the [:invalid][] pseudo-selector. By rendering the search
results `<turbo-frame>` element as a [direct sibling][] to the `<form>`
element, we can incorporate the `:invalid` state into the sibling
element's style, and hide it.

```diff
--- a/app/assets/stylesheets/application.css
+++ b/app/assets/stylesheets/application.css
*= require_tree .
*= require_self
*/
+
+.empty\:hidden:empty                                { display: none; }
+.peer:invalid ~ .peer-invalid\:hidden               { display: none; }

--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
    <header>
-      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results"
+      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results" class="peer"
        data-controller="form" data-action="invalid->form#hideValidationMessage:capture">
        <label for="search_query">Query</label>

--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
-      <turbo-frame id="search_results" target="_top"></turbo-frame>
+      <turbo-frame id="search_results" target="_top" class="empty:hidden peer-invalid:hidden"></turbo-frame>
    </header>
```

[Constraint Validations]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Constraint_validation
[required]: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/required
[pattern]: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/pattern
[invalid]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/invalid_event
[capture]: https://stimulus.hotwire.dev/reference/actions#options
[Stimulus Controller]: https://stimulus.hotwire.dev/handbook/hello-stimulus#controllers-bring-html-to-life
[Stimulus Action]: https://stimulus.hotwire.dev/handbook/building-something-real#connecting-the-action
[bubble up]: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#Bubbling_and_capturing_explained
[DOM]: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
[prevent the default behavior]: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#preventing_default_behavior
[:invalid]: https://developer.mozilla.org/en-US/docs/Web/CSS/:invalid
[Tailwind CSS]: https://tailwindcss.com/
[variant]: https://tailwindcss.com/docs/hover-focus-and-other-states
[direct sibling]: https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator

---
## [CorruptedPlazma/CorruptedPlazma.github.io](https://github.com/CorruptedPlazma/CorruptedPlazma.github.io)@[ef4b55d6d2...](https://github.com/CorruptedPlazma/CorruptedPlazma.github.io/commit/ef4b55d6d2d72ef78a3bf521e6cb146363790988)
#### Friday 2022-01-28 14:38:28 by CorruptedPlazma

yes I am making commits for the smallest of changes fuck you

---
## [StiffRobot/Foundation-19-Temp](https://github.com/StiffRobot/Foundation-19-Temp)@[966374d4c0...](https://github.com/StiffRobot/Foundation-19-Temp/commit/966374d4c09daec8636b27ad408e4c81d5bdad5d)
#### Friday 2022-01-28 15:00:03 by Calyxman

Update SCP-173.dm with Neck_Snap2 and flavor text

Changes 
'A statue, constructed from concrete and rebar with traces of Krylon brand spray paint'
to
'A statue, constructed from concrete and rebar with spray paint coating the top portion. You can see faint blood stains coating it.'

Changes
'(SCP-173) snaps (Victim)'s neck!'
to
'(SCP-173) appears at (Victim)'s location, their neck violently twisting with a loud crack by an unseen force!'

Changes 
'Shit on Floor'
to
'Defecate'

---
## [Lythine/MonkeStation](https://github.com/Lythine/MonkeStation)@[040b7ff839...](https://github.com/Lythine/MonkeStation/commit/040b7ff839d51d4db2ce1747f92312e0925bccd2)
#### Friday 2022-01-28 15:07:52 by Zonespace

Adds Flavor Text (#48)

* lgtm

* aaaAAAA

* might be better idk

* flavor-examine

* info

* haaa fuck you github

---
## [rexscaria/terraform-provider-cloudflare](https://github.com/rexscaria/terraform-provider-cloudflare)@[7dc1827e5f...](https://github.com/rexscaria/terraform-provider-cloudflare/commit/7dc1827e5f785898adcf04cb796c0710072c64ff)
#### Friday 2022-01-28 16:38:39 by Jacob Bednarz

resource/cloudflare_ruleset: improve dashboard collisions

One of the earliest niggles with customers coming from the dashboard to
Terraform was the collision caused by a Ruleset phase being created in
the UI but the Terraform provider also needing to create the same
phase. This was problematic for a few reasons:

- The first was that when you deleted Ruleset rules in the UI, it didn't
  remove the phase. This was intentional but hidden behind the UI and
  only accessible via the API.
- Secondly, when customers wanted to use Terraform, there was an
  assumption they would be starting from scratch and many were not.
- Finally, in the event of a collision, we didn't know which Ruleset the
  customer wanted to use so we error'd out with a link to manually
  resolve which isn't a great solution but made the issue more
  prominent.

I had a chance to rethink through this issue and managed to find a way
that we improve all three points above and remove majority of the pain
points. With the proposed changes, the only time a customer needs to
manually resolve the Ruleset rules is if there are existing rules in the
UI which requires them to be deleted or migrated.

Achieving this requires the assumption that if the Ruleset has no rules,
it is ok to modify. Unfortunately, it's not that simple in practice. If
the phase already exists, we cannot just update it as the `name`
attribute is not writable after creation. Along with this, the `ref` and
`version` values will be automatically incremented causing a permadiff
in Terraform as the customer hasn't actually modified these values but
the backing service (and API) has. To work around this, if we find a
phase with no rules, we recreate it with the provided values which is
essentially the same the same thing as the "happy path" for a new
Terraform resource would be anyway.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[9e681642b6...](https://github.com/crawl/crawl/commit/9e681642b6851451cbfcbc7a92e7de4b97106055)
#### Friday 2022-01-28 17:28:51 by Nicholas Feinberg

Tweak Mlioglotl

Make him demonic holiness to better match player expectations (re
vulnerability to holy word), and make his Lugonu abilities priestly
rather than magical.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[848502a6c2...](https://github.com/mrakgr/The-Spiral-Language/commit/848502a6c2211ea373db6451f74f09f0befd1d14)
#### Friday 2022-01-28 18:29:19 by Marko Grdinić

"10:50am. Apart from the pain at the bases of my ear, I feel rather good today relatively speaking. I still have a light fever, but it is nothing bad. The pain that comes in every few seconds though is like being stabbed with a needle. It is nasty. I reasoned out during the night that I must have pulled some kind of muscle, since I never seen a cold do something like this, but I found out this morning that my dad has had the same symptom so that can't be right. It is due to the flu then. I guess I'll have to endure it for a few more days.

Since I am decent today, I'll try to get some studying done.

Ok, let me read the Railgun and Onii-chan chapters and then I'll resume the plant tutorial.

11:35am. Let me start studying. Right now I am just wasting my time reading the Kengan thread. I actually stopped following the manga a while ago once I realized every fight was an circus act.

Now where was that plant vid?

https://youtu.be/GxKfKvYu7VU
Plant Growing animation | Houdini Full Tutorial

11:40am. Focus me, stop reading /3/. Actually, let me have breakfast here.

11:55am. I did some icebreaking, by factoring out some key params. I suppose this will serve to get me back into the groove. Let me eat and then I'll do it more seriously. Yesterday's gaming session was great, but I can't afford to live my life like that. In order to be able to just play games at my leasure, I'd need to attain transcendence first. Time for a human is limited and I need to spend it cultivating my skills.

1:45pm. Let me chill just for a bit and then I will start.

1:55pm. Let me start. It is time to get serious. My condition is starting to improve.

https://youtu.be/GxKfKvYu7VU?t=254

Let me start from here. I need to get the edge group.

2:05pm. https://youtu.be/GxKfKvYu7VU?t=276

Rather than promoting the group to a point group, he could have started with the just a point group.

2:15pm. Let me take a short break here so I can take my temp again.

I did a rapid test 20m ago, and now that I am seeing the results it came out positive. To think I'd actually manage to catch Covid in my NEET fortress. This is surprising because my father tested himself twice, and my brother and they came out negative.

https://www.healthline.com/health/how-accurate-are-rapid-covid-tests#how-accurate-is-it
> Although these tests provide quick results, they aren’t as accurate as laboratory tests because they require more of the virus in your sample to report a positive result. Rapid tests come with a high risk of giving a false negative result.

If I have it, then definitely the whole family has it. I am a bit concerned for my brother since he has 39.5C temperature and is saying that everything hurts for him, but for me, it hasn't been much worse than a regular cold. Covid is overhyped.

2:35pm. I am playing around with some of the nodes. He is using a bounding box near the bottom to avoid the saw effect there, but even without it, the scaling towards the x axis is imperceptible on the horizontal sides.

2:45pm. https://youtu.be/GxKfKvYu7VU?t=320

Here he is using smooth. I've played around with this, and it seems that this does absolutely nothing. Here he is using the default settings, but even if you crank the strength up to maximum, it has zero effect. I wonder why he made this kind of mistake?

...Agh, let me take a short break here.

3:05pm. Let me resume.

https://youtu.be/GxKfKvYu7VU?t=338

I do not like how he keeps overwritting the groups, but I suppose it might be passable. He'd have been better off using a bounding box instead of a selection here though.

3:50pm. Ah, I am such a fool. I forgot something obvious. If I want to make sure the leaf starts at 0, I should just use the match size node. The same goes for the stalk. Just what am I going trying to make use of the transform node and eyeballing it for this same purpose. The biggest problem with that is that changing the number of segments and the subdiv quantity can affect the geometry and change its lowest and highest points.

4:25pm. https://youtu.be/GxKfKvYu7VU?t=440

I've been messing with the mask way too long. Just how did he visualized it in red like that?

https://youtu.be/GxKfKvYu7VU?t=501

Instead of adding noise like this, couldn't he have used something like a mountain node?

4:40pm. No I can't figure out how this would work. Mountain node is just the attribute noise node.

Even if I set the element size to mask, I do not get the correct results for some reason.

5:15pm. Had to leave for lunch. I had an idea. Let me try multiplying the element size by mask.

Nope, I have no idea what these local variables in the attribute node are doing.

https://youtu.be/GxKfKvYu7VU?t=569

Can I do this in vex, using the attribute wrangler? Trying to use geo nodes for everything is painful.

https://mrkunz.com/blog/03-04-2017_Using-noise-in-VEX.html

So it is possible to import the vop library. I was wondering about that. Ok...

How did he animate the noise?

https://youtu.be/GxKfKvYu7VU?t=526

Why did he do this promotion, what is it for? Nothing changes for me when I do it as expected.

5:50pm. https://youtu.be/GxKfKvYu7VU?t=576

Ah, this is what promotion does.

I'll have to leave this for later. I have no idea what that string is supposed to be. But I get the gist of it. If it was me, I'd try to make use the 4th input to the position node, but this way is guaranteed to be consistent.

6pm. https://youtu.be/GxKfKvYu7VU?t=732

If it were me, I'd select every 1 in 10 points on the edge and using soft editing, scale them outwards. That would be an easier way of getting the v shape...though, in the image it is probably v because of the depth. Hmm....

https://youtu.be/GxKfKvYu7VU?t=812

Let me do this in VEX. Yeah, it did take me 4h just to get through 13m of this video, but so be it. I'll go through it completely at some point. Let me continue going forward.

```vex
@P.z = abs(@P.x);
```

Is this right?

```vex
@P.z = abs(@P.x * chf("factor"));
```

How do I create a channel? I thought that it would just appear for editing as soon as I did it.

6:15pm. i do not get it. Let me do a search through the journal. When did I study vex nodes last?

https://www.youtube.com/playlist?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT
VEX Isn't Scary: Beginner Series

It was this. I ended up skipping it due to it being a very basic PL tutorial. Maybe it has something about channels in it. Let me review it.

https://youtu.be/9xhmDWAyPRA?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT&t=281
> You have to go on the right and click on create param on each unique call of `ch`.

Who is going to remember this. I doubt I was even playing along back then. In a way I am only properly studying that material now.

6:25pm. Let me study the VOP node program once again. I do not like this right now. I think instead of doing it like I have it, might have been better to just rotate it.

https://youtu.be/GxKfKvYu7VU?t=802

Hmmm, but I am in fact following this accurately, so I guess it is fine then.

https://youtu.be/GxKfKvYu7VU?t=910

I do not get why the points are increasing for him.

Maybe he meant to say they are decreasing because of the fuse.

No wait, he is doing beveling, extruding as well. That would increase them. BUt why did he try to take the trails then, if that works on a per point basis?

https://youtu.be/GxKfKvYu7VU?t=1002

I do not like this. Doing extrude here would also do the same for that stalk. He should have done this work before merging them.

6:50pm. https://youtu.be/GxKfKvYu7VU?t=1617

Enough, let me stop here. In order to understand this, I'd need to understand basic rigging.

At the back of my mind, I am trying to figure out how I would do it. Watching this reminds me of my Logo days. If I was doing it in Logo, I'd just draw a spiral and bend it afterwards. The way to draw a Spiral using the logo turtle would be to keep the rotation magnitude in a variable and increment it by a specified amount on every step. If that amount is 0, that would just result in a circle. Above 0 would result in a Spiral.

Of course, it is possible to do spirals analitically, like the time I did the Spiral logo in Processing.

Once you have the spiral making code, which would not be hard, the way to get the unrolling on top of that would be to use the power function on the input coordinates.

I used power for similar kinds of uses before. By varying it, you could get a very loose or a tight spiral. If it is 1, then it would just end up being the same as the regular thing. Values higher than 1 would loosen it up.

So I do have an option for how to do it myself, but I should try to understand the all stuff in the plant tutorial at some point soon. I should overcome this challenge and move on to the next thing.

7pm. Let me think. What is my plan here?

Should I study rigging for a bit, just so I know enough to understand the plant tutorial?

An alternative is to drop this for now, and study Simon's stuff which is more relevant to my interests. I hate giving up on things, so I am tempted to just study rigging, but I really don't need that right now. Just like with texture mapping, how about I leave this for later? I am fine focusing only on SOPs for now.

Yeah, forget the plant. The reason why this is so complex is because he needs to animate it. I on the other hand am just interested in static scenes.

I should try recreating that bridge tomorrow. After that, what I want to know is more basic node functionality. I got the sweep down, but there are a bunch of other ones.

I should get familiar with the basics before trying to use Houdini for my own ends.

7:10pm. Could bend itself work for making a spiral? It did occur to me just now that it is a nonlinear thing, but it does have to capture the underlying mesh, so having it curve on itself would not work as one would hope.

Still, on the subject of spirals, I'd be shocked if Houdini did not have a way of making them directly. There should be a node somewhere in there for that. And I'd expect it would also have a deform along a curve in there as well. That should be an alternative to the rigging method.

7:25pm. Let me close here, since I've already started browsing on the side. Today was not bad considering what I am going through. I think that by tomorrow, most of the illness should be purged from my system. That will allow me to get back into the swing of things.

I need to remember what my goal is. I need to master the essentials of Houdini so that I can start work on the pool scene. I already know enough in fact, but before I commit, I want to explore what Houdini can do for a while longer."

---
## [beakeyz/dadjoke-gen](https://github.com/beakeyz/dadjoke-gen)@[8f330096be...](https://github.com/beakeyz/dadjoke-gen/commit/8f330096be9e5a6a6a76d4df26e7340147110108)
#### Friday 2022-01-28 18:43:57 by beakeyz

sick epic amazing such retard shitface goblin comment

---
## [SnowJay2005/SnowJay2005.github.io](https://github.com/SnowJay2005/SnowJay2005.github.io)@[73955b4992...](https://github.com/SnowJay2005/SnowJay2005.github.io/commit/73955b49927b16f1f9a71f97b3975c74bf112cba)
#### Friday 2022-01-28 19:18:46 by SnowJay2005

yeah ok i added everything again

this time its uncompressed, ooooh, i love 16.7 megabytes of flappy fucking bird

---
## [krux02/nimskull](https://github.com/krux02/nimskull)@[f35b5bf2d4...](https://github.com/krux02/nimskull/commit/f35b5bf2d447c10b6a104ef0649115a266e8dea6)
#### Friday 2022-01-28 19:47:14 by haxscramper

Make compiler report structured

Full rework of the compiler message handling pipeline. Remove old-style message generation that was
based purely on strings that were formatted in-place, and instead implement structured logging where
main compiler code only instantiates objects with required information.

Explanation of changes for this commit will be split into several sections, matching number of edit
iterations I had to make in order for this to work properly.

* File reorganization

In addition to the architectural changes this PR requires some type definition movements.

- PNode, PSym and PType definitions (and all associated types and enums) were moved to the
  ast_types.nim file which is then reexported in the ast.nim
- Enum defininitions for the nilability checking were moved to nilcheck_enums.nim and then
  reexported
- Enum definitions for the VM were moved to to vm_enums.nim

* New files

- Main definition of the report types is provided in the reports.nim file, together with minor
  helper procedures and definition of the ReportList type. This file is imported by options, msgs
  and other parts of the compiler.
- Implementation of the default error reporting is provided in the cli_reporter.nim - all
  disguisting hardcoded string hacks were moved to this single file. Now you can really witness the
  "error messages are good enough for me" thinking that prevailed in the compiler UX since it's
  inception.

* Changed files

Most of the changes follow very simple pattern - old-style hardcoded hacks are replaced with
structural report that is constructed in-place and then converted to string /when necessary/. I'm
pretty sure this change already puts me close to getting CS PHD - it was *unimaginably hard* to
figure out that hardcoding text formatting in place is not the best architecture. Damn, I can
probably apply to the nobel prize right now after I figure that out.

** Changes in message reporting pipeline

Old error messages where reportined via random combinations of the following:

- Direct calls to `msgs.liMessage` proc - it was mostly used in the helper templates like
  `lintReport`
- `message`
- `rawMessage`
- `fatal`
- `globalError` - template for reporting global errors. Misused to the point where name completely
  lost it's meaning and documentation does not make any sense whatsoever. [fn:global-err]
- `localError` - template for reporting necessary error location, wrapper around `liMessage`
- `warningDeprecated` - used two times in the whole compiler in order to print out error message
  about deprecated command switches.

Full pipeline of the error processing was:

- Message was generated in-place, without any colored formatting (was added in `liMessage`)
  - There were several ways message could be generated - all of them were used interchangeably,
    without any clear system.
    1. Some file had a collection of constant strings, such as `errCannotInferStaticParam = "cannot
       infer the value of the static param '$1'"` that were used in the `localReport` message
       formatting immediately. Some constants were used pretty often, some were used only once.
    2. Warning and hint messages were categorized to some extent, so and the enum was used to
       provide message formatting via `array[TMsgKind, string]` where `string` was a `std/strutils`
       formatting string.
    3. In a lot of cases error message was generated using hardcoded (and repeatedly copy-pasted)
       string
- It was passed down to the `liMessage` (removed now) procedure, that dispatched based on the global
  configuration state (whether `ignoreMsgBecauseOfIdeTools` holds for example)
- Then message, together with necessary bits of formatting (such as `Hint` prefix with coloring) was
  passed down to the `styledMsgWriteln(args: varargs[typed])` template, whcih did the final dispatch
  into
- One of the two different /macros/ for writing text out - `callStyledWriteLineStderr` and
  `callIgnoringStyle`.
  - Dispatch could happen into stdout/stderr or message writer hook if it was non-nil
- When message was written out it went into `writeLnHook` callback (misused for
  `{.explain.}` [fn:writeln-explain]) (hacked for `compiles()` [fn:writeln-compiles]) and was
  written out to the stdout/stderr.

It is now replaced with:

- `Report` object is instantiated at some point of a compilation process (it might be an immediate
  report via `localError` or delayed via `nkError` and written out later)
- `structuredReportHook` converts it to string internally. All decitions for formatting, coloring
  etc. happen inside of the structured report hook. Where to write message, which format and so on.
- `writeLnHook` /can/ be used by the `structuredReportHook` if needed - right now it is turned into
  simple convenience callback. In future this could even be replaced with simple helper proc, for
  now I left it as it is now because I'm not 100% sure that I can safely remove this.

** Changes in the warning and hint filtering

Report filtering is done in the particular *implementation* of the error hook -
`options.isEnabled()` provides a default predicate to check whether specific report can be written
out, but it must still be called manually. This allows to still see all the reports if needed. For
example, `cli_reporter.reportHook()` uses additional checks to force write some reports (such as
debug trace in `compiles()` context).

Most of the hint and warning were already categorized, altough some reports had to be split into
several (such as `--hint=Performance` that actually controlled reports for `CopiesToSink` and
`CannotMakeSink`, `--hint=Name` that controlled three reports).

None of the errors were categorized (reports from the `nkError` progress was incorporated, but in
I'm mostly describing changes wrt. to old reporting system) and all were generated in-place

** Minor related changes

- List of allowed reports is now stored in the `noteSets: array[ConfNoteSet, ReportKinds]` field of
  the `ConfigRef`, instead of *seven* separate feilds. Access is now done via getter/setter procs,
  which allows to track changes in the current configuration state.
- Renamed list of local options to `localOptions` - added accessors to track changes in the state.
- Move all default report filter configuration to `lineinfos.computeNotesVerbosity()` - previously
  it was scattered in two different places: `NotesVerbosity` for `--verbosity:N` was calculated in
  `lineinfos`, foreignPackageNotesDefault was constructed in `options`
- Changed formatting of the `internalAssert` and `internalError` messages
- Removed lots of string formatting procs from the various `sem*` modules - ideally they should
  *all* be moved to the `cli_reporter` and related.

-------

Additional notes

[fn:global-err] As I said earlier, `globalError` was misused - it is still not possible to fully get
rid of this sickening hack, since it is used for /control flow/ (you read this correct - it is an
error reporting template, and it is used for control flow. Wonderful design right?).

So, in short - `globalError` can raise `ERecoverableError` that can be caught in some other layer
(for example `sem.tryConstExpr` abuses that in order to bail out (pretty sure it was done as an
'optimization' of some sort, just like 'compiles') when expression fails to evaluate at
compile-time [fn:except])

[fn:except] https://github.com/nim-works/nimskull/pull/94#issuecomment-1006927599

[fn:writeln-explain] Of course you can't have a proper error reporting in the nim compiler, so this
hook was also misused to the point of complete nonsense. Most notable clusterfuck where you could
spot this little shit is implementation of `{.explain.}` pragma for concepts. It was implemented via
really 'smart' (aka welcome to hell) solution in

https://github.com/nim-works/nimskull/commit/74a80988d9289e8147a791c4b0939d4287baaff3 (sigmatch
~704) and then further "improved" in
https://github.com/nim-lang/Nim/commit/fe48dd1cbec500298f7edeb75f1d6fef8490346c by slicing out parts
of the error message with `let msg = s.replace("Error:", errorPrefix)`

For now I had to reuse similar hack - I *do* override error reporting hook in order to collect all
the missing report information. In the future it would be unnecessary - when concept is matched it's
body will be evaluated to `nkError` with reports that are written out later.

[fn:writeln-compiles] when `compiles()` check is executed, all error output is temporarily disabled
(both stderr and stdout) via setting allowed output flags to `{}` (by default it is set to

---
## [mernst/jspecify](https://github.com/mernst/jspecify)@[4ac4961c5d...](https://github.com/mernst/jspecify/commit/4ac4961c5d11beef765742ee3e2d57a8ec575d16)
#### Friday 2022-01-28 20:30:37 by Chris Povirk

Remove TODO about substitution into type-variable bounds.

It's still conceivable that we need such a thing. But if we do, it's
likely more correctly addressed at a deeper level. Notably, I see that
[JLS
4.10.2](https://docs.oracle.com/javase/specs/jls/se11/html/jls-4.html#jls-4.10.2)
has no mention of substitution in its discussion of type-parameter
bounds.

Additionally, with our hacky test checker, I am finding that *undoing*
the Checker Framework's subsitution into type-variable bounds *improves*
results. *That said*, I remember some other change that improved results
(but maybe only on *net*?) not long ago that I decided to back out
because it seemed to be getting the right answers for the wrong reasons.
So I'm not sure that undoing substitution is *actually* right, though
it's possible.

Honestly, I can't quite get my head around "substitution into
type-variable bounds" at all today. Arguably I should leave the TODO for
a day when I'm feeling more up to it. But I'm going to remove it in the
hope that:

- The bounds at the declaration site always provide enough information,
  since they must always be as strict as any bounds at a use site.
- If there is "extra" information available from viewing the type
  variable "as a member of" a type, then we get that from the type
  argument supplied to that type (a type argument that may itself by a
  type variable) or perhaps wildcard capture?

---
## [qemu-bsd-user/qemu-bsd-user](https://github.com/qemu-bsd-user/qemu-bsd-user)@[ede52811db...](https://github.com/qemu-bsd-user/qemu-bsd-user/commit/ede52811db688608c18796f1be2d8a0299771b14)
#### Friday 2022-01-28 21:53:19 by Warner Losh

bsd-user: Super Ugly hack and wire guest base address as 32GB on LP64

When the host bits are 64 bit, just hard wire the guest base address at
32GB which should be well above the qemu bsd-user binary. This is super
ugly, to be true. More nuanced code is needed to avoid
collisions. linux-user has a way to guess where is safe that asks the
kenrel for the current vm map.  FreeBSD has similar things available via
sysctl which we should bolt into the Linux code. Until then, allow most
things to build with this kludge. Since the VM is sparse, this won't
cause undue grief to those that have tiny resource limits (the amount of
grief is the same, no matter where we map this stuff in at).

Signed-off-by: Warner Losh <imp@bsdimp.com>

---
## [Semetrix/Semetrix](https://github.com/Semetrix/Semetrix)@[0e6b6e2c34...](https://github.com/Semetrix/Semetrix/commit/0e6b6e2c348a06b6ab674709479be299a6038e48)
#### Friday 2022-01-28 22:23:10 by Semetrix

made things good

Then final Saturday morning I woke up, completely psyched. Ready to start. So praying to RNGesus that wherever the March got me my knees would give up and I'd get the place to pee, I got the ride down to city. Not the long road, mind you, but the ride nonetheless. And the time I worked onto Biscayne street, I knew I was leading into something undeniable, something revealing. I would sense it. It was in the air suddenly charged with energy, at the noise of voices gathering strength and at all those sides filled with joy and great cheer converging onto Bayfront stadium.  All quality feelings was shot between April and July 2008 at America and New York . Originally scheduled for the July 24, 2009 announcement, the movie finally had a special release in December 3, 2010.  (Horn , Aug 24, 2010)   (Ioncinema. Oct 2010.)  As the creator, I created sites and apps for people, so I kept things focused on the person. Then I used those techniques to define who the observer could take and what parts they could refer to in this movie. I wrote very little descriptions and narrations of real-life events that I needed to make, and so I got very broad with these characters. Instead of writing this story, I made the drawing. This means, I could know who connected with what and everything within the story. Throughout my career, when I was in the position where I had to make headlines, I concentrated largely on these verbs. Verbs amaze readers. Verbs hold readers. Great verbs at headlines pushed the readers into the story. But I was never as proficient in writing headlines as some of the copy editors in newspapers where I get gone. In newspapers, location is the most important thing, and place is valued at column inches. The reporter often knows how some column inches the editor is ready to devote to the story. With nearly every story, you get more knowledge than would fit in this place. The place forces you to make the work close. Take questions if you are the least time missing. My system was the 12-week system and it was really easy for somebody to get lost. I made sure that I got in with doubts for my teacher. I still asked questions to affirm my understanding of matters! Great teachers are there to help you develop within the bootcamp, use them as a resource.

---
## [nikp123/xava](https://github.com/nikp123/xava)@[4f4a49f155...](https://github.com/nikp123/xava/commit/4f4a49f155bbf134a5d4adede30d704aa9f42b4b)
#### Friday 2022-01-28 22:37:37 by Nikola Pavlica

[bugfix] wayland: display update timing

GOD FUCKIGN DAMN THIS WAS HARD TO FIND. Wayland is the most
developer-unfriendly API imaginable.

---
## [JK0JK/Minigame-Investigator](https://github.com/JK0JK/Minigame-Investigator)@[860fcd1ffd...](https://github.com/JK0JK/Minigame-Investigator/commit/860fcd1ffdf96f329d101b84f65311b82e8eb35c)
#### Friday 2022-01-28 23:23:54 by root

The Identity Update

Finished the Hurricane welcome sign
Unfortunately, GBA wants to be problematic and won't read anything past C0 on graphics/birch_speech/welcum.png, and instead will fill tiles it won't read with stripes. YOU'RE SUPPOSED TO READ THE OTHER 24 TILES!!
Fixed problems with the palette loading and not loading properly

Once the problem with C0 onward is fixed, we are ready to work on:
*deeper customizing the intro cutscene
*adding character designs for the player (male and female)
*customizing the naming screen
*adding animated sprites for the introduction
*adding frames for opening the diary
*making our own title screen
*making our own title screen music
*making the player's room's tiles
*making the player's room's layout
*debugging
*pushing this bloody thing

---
## [Xavierlm11/Assignment1](https://github.com/Xavierlm11/Assignment1)@[79e22baf8d...](https://github.com/Xavierlm11/Assignment1/commit/79e22baf8deb36a65eb48361aa499cf3c3005399)
#### Friday 2022-01-28 23:38:13 by Marina Albalà

menu pause

Last Christmas, I gave you my heart
But the very next day, you gave it away (you gave it away)
This year, to save me from tears
I'll give it to someone special (special)
Once bitten and twice shy
I keep my distance, but you still catch my eye
Tell me, baby, do you recognize me?
Well, it's been a year, it doesn't surprise me
"Merry Christmas, " I wrapped it up and sent it
With a note saying, "I love you, " I meant it
Now I know what a fool I've been
But if you kissed me now, I know you'd fool me again

---

