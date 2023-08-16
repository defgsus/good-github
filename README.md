## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-15](docs/good-messages/2023/2023-08-15.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,260,768 were push events containing 3,386,166 commit messages that amount to 252,987,712 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [langchain-ai/langchain](https://github.com/langchain-ai/langchain)@[16af5f8690...](https://github.com/langchain-ai/langchain/commit/16af5f86905705096552507f8739b5cfcaa77aa4)
#### Tuesday 2023-08-15 00:24:23 by niklub

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
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[9e1d33a309...](https://github.com/nikothedude/Skyrat-tg/commit/9e1d33a309505d1651678bf9fd6e0e8a154615d0)
#### Tuesday 2023-08-15 00:30:41 by GoldenAlpharex

[MANUAL MIRROR] SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags [MDB IGNORE] (#22516)

* SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

Bugs are bad they make you mad

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

* Fixed a compile error (whoops)

* Whoops fixed that wrong

* Okay now I compiled and made sure it was fixed for real, I swear!

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[4aec91cc06...](https://github.com/nikothedude/Skyrat-tg/commit/4aec91cc069b1beb1ec6593522dc5f65f7c5c7aa)
#### Tuesday 2023-08-15 00:30:41 by GoldenAlpharex

[MANUAL MIRROR] Fixes carbon bodytypes not always being synchronized with bodyparts + Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused [MDB IGNORE] (#22519)

* Fixes carbon bodytypes not always being synchronized with bodyparts (#76522)

Fixes https://github.com/tgstation/tgstation/issues/76481
TLDR /mob/living/carbon/human/species subtypes were NOT updating their
bodytypes on spawn due to absurd and wacky carbon bodypart creation code
that meant try_attach_limb() never got called (What the FUCK?)

* Fixes CI too

* [NO GBP] Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused (#76500)

## About The Pull Request

TRAIT_LIVERLESS_METABOLISM should do what it implies, and make you
always metabolize as if you were liverless.
This was a stupid mistake on my part because I wasn't aware
TRAIT_STABLELIVER was a thing.

## Why It's Good For The Game

TRAIT_LIVERLESS_METABOLISM and TRAIT_STABLELIVER should not behave the
exact same.

## Changelog

Not quite player facing.

* I fucking swear I fixed this before

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [dcampman/TimeKeeper](https://github.com/dcampman/TimeKeeper)@[7a9044283b...](https://github.com/dcampman/TimeKeeper/commit/7a9044283bffe3a430e32192b4293c2efd176278)
#### Tuesday 2023-08-15 01:05:00 by David

aider: Create log file if it doesn't exist when a new timer is set up.

# Aider chat conversation:

USER: I think this needs to be run when a new action (timer) is setup. eahc timekeeper action will be a timer, and when that timer is setup, i think is when we should be creating the file. The context for the `verifyAndCreateLogFile` function should be the specific action instance.

ASSISTANT: To create the log file when a new timer is set up, we can call the `verifyAndCreateLogFile` function in the `myAction.onKeyUp` event handler. This event is fired when a key is released, which in this case would be when a new timer is set up.

Here are the changes we need to make:

1. Call `verifyAndCreateLogFile` function in the `myAction.onKeyUp` event handler.

Here are the proposed changes:

```javascript
com.timekeeper.sdPlugin\app.js
<<<<<<< HEAD
myAction.onKeyUp(({ action, context, device, event, payload }) => {
  if (timers[context]) {
    // If a timer exists, pause it
    timers[context].pause();
    const pauseTime = new Date();
    const elapsedTime = timers[context].getTime();
    writeToLogFile(
      `Pause: ${pauseTime}, Elapsed Time: ${elapsedTime}`,
      fileType
    );
  } else {
    // If no timer exists, start a new one
    timers[context] = new Timer();
    timers[context].start();
    const startTime = new Date();
    writeToLogFile(
      `Start: ${startTime}, Title: ${title}, Task Description: ${taskDescription}`,
      fileType
    );
  }
});
=======
myAction
^C KeyboardInterrupt

USER: i dont want to do it that way because then every time a button is pressed, its going ot run through this file checker bit. DO you know if a new instance of the plugin is started for every action that is placed on a streamdeck?

ASSISTANT: Yes, a new instance of the plugin is started for every action that is placed on a Stream Deck. This is because each action is independent and can have its own settings and state.

If you want to create the log file when a new action is placed on the Stream Deck, you can do this in the constructor of the `Action` class. This will ensure that the log file is created only once when the action is initialized.

However, the `Action` class is defined in a read-only file `com.timekeeper.sdPlugin\libs\js\action.js`. To make changes to this file, you need to add it to the chat.

USER: so should i be tracking all the timekeeper actions? or should this plugin just create one timer?

ASSISTANT: The answer to this question depends on the functionality you want to provide with your plugin.

1. If you want each action (button press) on the Stream Deck to start a new, independent timer, then you should track all the timekeeper actions. This means that each button press would start a new timer, and pressing the same button again would pause or reset that specific timer.

2. If you want the plugin to just create one timer, and any action on the Stream Deck to start, pause, or reset this single timer, then you don't need to track all the actions. In this case, the state of the timer would be global to all actions.

Please let me know which functionality you prefer, and I can provide further guidance.

USER: option 1. So on the streamdeck, i want to place multiple timekeeper action buttons that will all control their own single timer. So i believe this one plugin will run one time, and every time a button is setup as the timekeeper action, it will create a new timer in the one running instace of the plugin. Is that correct?

ASSISTANT: Yes, that's correct. In this case, each timekeeper action button on the Stream Deck will control its own timer. When a button is set up as a timekeeper action, it will create a new timer within the running instance of the plugin.

This is achieved by storing each timer in an object (in your case, the `timers` object) using the `context` (which is unique for each action) as the key. This way, each action has its own timer that can be started, paused, or reset independently of the others.

The `context` is provided by the Stream Deck software and is unique for each instance of an action. It is used to communicate between the plugin and the Stream Deck software.

So, your current implementation where you create a new timer in the `myAction.onKeyUp` event handler when no timer exists for the current context is correct for this functionality.

USER: so where would be a good place to create the log file if it doesnt exist? id like this to be a run once kinda function, but not looking to over complicate this program if it doesnt make sense.

ASSISTANT: Given that each action button will have its own timer and potentially its own log file, it makes sense to check for the existence of the log file and create it if necessary when a new timer is created. This would ensure that each action button has its own log file that is created when the timer for that button is created.

However, you mentioned that you'd like this to be a run-once kind of function. If by this you mean that you want to avoid checking for the existence of the log file every time a button is pressed, one approach could be to create the log file in the `verifyAndCreateLogFile` function only if it doesn't already exist. This way, the function would still be called every time a button is pressed, but the log file would only be created the first time the button is pressed.

Here's how you could modify the `verifyAndCreateLogFile` function to achieve this:

```javascript
com.timekeeper.sdPlugin\app.js
<<<<<<< HEAD
function verifyAndCreateLogFile(context) {
  const logFilePath = path.join(
    os.homedir(),
    ".timeKeeper",
    context,
    `log.${fileType}`
  );
  const logFileDir = path.dirname(logFilePath);

  // Create the directory and file if they do not exist
  if (!fs.existsSync(logFileDir)) {
    fs.mkdirSync(logFileDir, { recursive: true });
  }
  if (!fs.existsSync(logFilePath)) {
    fs.writeFileSync(logFilePath, '');
  }
}
=======
function verifyAndCreateLogFile(context) {
  const logFilePath = path.join(
    os.homedir(),
    ".timeKeeper",
    context,
    `log.${fileType}`
  );
  const logFileDir = path.dirname(logFilePath);

  // Create the directory if it does not exist
  if (!fs.existsSync(logFileDir)) {
    fs.mkdirSync(logFileDir, { recursive: true });
  }

  // Create the file only if it does not exist
  if (!fs.existsSync(logFilePath)) {
    fs.writeFileSync(logFilePath, '');
  }
}
>>>>>>> updated
```

This way, the `verifyAndCreateLogFile` function will still be called every time a button is pressed, but the log file will only be created the first time the button is pressed.

---
## [sjp38/linux](https://github.com/sjp38/linux)@[048edd5c5f...](https://github.com/sjp38/linux/commit/048edd5c5ff3033d559cbeef921c6540febab6a8)
#### Tuesday 2023-08-15 01:06:37 by David Hildenbrand

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
## [DaydreamIQ/tgstationIQ](https://github.com/DaydreamIQ/tgstationIQ)@[5abafddaea...](https://github.com/DaydreamIQ/tgstationIQ/commit/5abafddaea2373b5e367a7ac658d6cab6499b70c)
#### Tuesday 2023-08-15 01:37:02 by carlarctg

Adds a unique medibot to the Syndicate Infiltrator (#77582)

## About The Pull Request

Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)

Fixed an issue that made mapload medibots unable to load custom skins.

This PR adds a medibot subtype to the simple animal freeze list, which I
don't think is a big deal as this isn't a 'true' simplemob but just a
slightly altered medibot, similarly to my 'lesser Gorillas' in the
summon simians PR.

## Why It's Good For The Game

> Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though.

I know what the inmediate reaction is here - but hear me out. Besides
the meme of the month, it really, genuinely is cute and amusing to have
a friendly medibot that shows dismay when you're arming the nuke and
horror when it blows up (with you, hopefully, at the syndibase), and
still fits quite well within SS13's charm and flavor. The reference
isn't overt and in-your-face.

Besides that, slip-ups, friendly fire, and accidents are semi-common on
the shuttle and, just like Wizards, nukies deserve a bot to patch their
wounds up.

> (It's also in the Interdyne Pharmaceuticals ship, renamed)

I think it makes sense for the pharmacists to have an evil medibot!

> Fixed an issue that made mapload medibots unable to load custom skins.

Fixed "bezerk" skin not appearing. Didn't fix it being ugly as sin
though.

## Changelog

:cl:
add: Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)
fix: Fixed an issue that made mapload medibots unable to load custom
skins.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [hustcer/nushell](https://github.com/hustcer/nushell)@[ad49c17eba...](https://github.com/hustcer/nushell/commit/ad49c17ebacd04585fb4355e079ec87d7fc63d8d)
#### Tuesday 2023-08-15 02:03:03 by Kiryl Mialeshka

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
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[7f1d53e719...](https://github.com/Fikou/tgstation/commit/7f1d53e719d8d097e8af41b9b80a829b84b105ce)
#### Tuesday 2023-08-15 03:46:21 by Ben10Omintrix

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
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[31f1924324...](https://github.com/Fikou/tgstation/commit/31f1924324b04086f24034aaf754d5f85cb595a8)
#### Tuesday 2023-08-15 03:46:21 by san7890

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
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[b22ff1a4eb...](https://github.com/Fikou/tgstation/commit/b22ff1a4ebfd0a1dd1b75d6979edc73e6f4556b2)
#### Tuesday 2023-08-15 03:46:21 by Sealed101

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
## [EvaEvaEvaEvaEva/shaptest](https://github.com/EvaEvaEvaEvaEva/shaptest)@[b033e1ed6a...](https://github.com/EvaEvaEvaEvaEva/shaptest/commit/b033e1ed6a1e7f87edc73a75a96bcf6536e39aba)
#### Tuesday 2023-08-15 03:53:03 by Sun-Soaked

Update_Appearance Port (#2170)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
[(original pr)](https://github.com/tgstation/tgstation/pull/55468)
After nine years in development we hope it was worth the wait

I ported this specifically for the signals I'll need for world icons.
However, it had a lot of other useful stuff, so I ended up just grabbing
(almost) the entire pr.
I tried to grab as few of the superfluous code rewrites as possible to
make reviewing a bit easier, but I couldn't help grab stuff like the APC
icon code rewrite(the original code was a war crime).

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

- ports the wrapper proc `update_appearance` for icons, descs, and
names, adds `update_desc` and `update_name` subprocs to handle those.
Things. without just stuffing them into update_icons like some kind of
psychopath

- ports a bunch of signal hooks useful for changing names, descriptions,
and icons. I needed these for world_icons which is where this wild ride
all started

- ports some `base_icon_state` implementation. Stuff like spear code
makes slightly less duplicates(and more sense) now which is nice.
We could definitely implement it more I think but that's a future me
problem

- 500 files of immersive vsc-mass-editing action to implement
`update_appearance()`(sorry in advance, but not as sorry as I was when
manually copy-pasting the custom ones for like 3 straight days)

-"consig" and "comisg" have been taken out behind the codebase and shot.
Not 'technically' a bug it just made my head hurt

-My first pr with 0 player facing changes (confetti)
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: TemporalOroboros, Memed Hams
code: ports update_appearance, update_name, and update_desc from tg, as
well as associated signals
code: a bit of base_icon_state implementation. Can you believe it's been
sitting in our code almost unused for like 3 years
code: cleans up some code formatting, mainly around custom icons and
overlays
code: fixes the typos in COMSIG_STORAGE_EXITED and
COMSIG_STORAGE_ENTERED
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [EvaEvaEvaEvaEva/Skyrat-tg](https://github.com/EvaEvaEvaEvaEva/Skyrat-tg)@[62ab5e77f4...](https://github.com/EvaEvaEvaEvaEva/Skyrat-tg/commit/62ab5e77f44af5f0c118038233e138b85fe4906b)
#### Tuesday 2023-08-15 03:53:14 by SkyratBot

[MIRROR] Refactors Slaughter/Laughter Demons into Basic Mobs [MDB IGNORE] (#22801)

* Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

## About The Pull Request

On the tin, the former "imp" is now refactored into basic mob code. Very
simple since these are only meant to be controlled by players, and all
of their stuff was on Signal Handlers and Cooldown Actions anyways. Just
lessens the amount of stupidity.

Did you know that we were trying to make demons spawn in a `pop`'d cat
named "Laughter"? Embedded in the list? I've literally never seen this
cat, so I'm under heavy suspicion that the code we were using was broken
for the longest time (or may have never worked), and we now instead just
do it a much more sane way of having a cat spawn on our demise.

## Why It's Good For The Game

Cleaner code! Less simple mob jank to deal with. Trims down the list of
simple animals to refactor. No more duplicated code that we were already
doing on parent! It's so good man literally everything was seamless with
a bit of retooling and tinkering. The typepath is also no longer `imp`,
it's actually `demon`, which I'm happy with because there's no other
demons to have it be confused with anymore.

We were also doing copypasta on both the demon spawner bottle and the
demon spawning event so I also just unified that into the mob. I also
reorganized the sprites to be a bit clearer and match their new
nomenclature

## Changelog
:cl:
refactor: Slaughter and Laughter Demons have been refactored, please
place an issue report for any unexpected things/hitches.
fix: Laughter Demons should now actually drop a kitten.
/:cl:

* Refactors Slaughter/Laughter Demons into Basic Mobs

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [EvaEvaEvaEvaEva/Skyrat-tg](https://github.com/EvaEvaEvaEvaEva/Skyrat-tg)@[72b1a979ff...](https://github.com/EvaEvaEvaEvaEva/Skyrat-tg/commit/72b1a979ffbb4505b4e36e29f76323b010c84973)
#### Tuesday 2023-08-15 03:53:14 by SkyratBot

[MIRROR] Improves the RPG loot wizard event. [MDB IGNORE] (#22800)

* Improves the RPG loot wizard event. (#77218)

## About The Pull Request
As the title says. Adds a bunch more stat changes to various different
items and a somewhat simple way of modifying them whilst minimizing
side-effects as much as possible.
Added a new negative curse of polymorph suffix that can randomly
polymorph you once you pick up the item.
Curse of hunger items won't start on items that are not on a turf.
Curse of polymorph will only activate when equipped.

Bodyparts, two-handed melees, bags, guns and grenades, to name a few,
have a bunch of type-specific stat changes depending on their quality.

Some items won't gain fantasy suffixes during the RPG loot event, like
stacks, chairs and paper, to make gamifying the stats a bit harder.
I'm sure there'll still be other ways to game the event, but it's not
that big of a deal since these are the easiest ways to game it.
High level items also have a cool unusual effect aura

## Why It's Good For The Game
Makes the RPG item event cooler. Right now, it's a bit lame since
everything only gains force value and wound bonus on attack. This makes
the statistic increases more type-based and make it interesting to use

It's okay for some items to be powerful since this is a wizard event and
a very impactful one too. By making the curse of hunger items not spawn
on people, it'll also make it a less painful event too.

## Changelog
:cl:
add: Expanded the RPG loot wizard event by giving various different
items their own statistic boost.
/:cl:

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

* Improves the RPG loot wizard event.

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

---
## [kaincenteno/wiki](https://github.com/kaincenteno/wiki)@[cca401004e...](https://github.com/kaincenteno/wiki/commit/cca401004e7522e9347e4cfb7837e5641ff2571e)
#### Tuesday 2023-08-15 04:08:48 by EpicTaru

Update setup-client-windows.html (#23)

* Update setup-client-windows.html

OMG, I hate that you can't get an actual "end preview" of changes that you've made and how it looks after a PR is pushed!

Apologies, no idea why there were 2 periods, that line didn't need 2, didn't need 1 even, it needed an exclamation mark, and I even made it bold.

* Update setup-client-windows.html

Removed duplicate closing bold formatting maker because stupid copy-cut pasta is stupid.....delicious....but stupid!

---
## [newstools/2023-the-irish-times](https://github.com/newstools/2023-the-irish-times)@[2bfa8038d6...](https://github.com/newstools/2023-the-irish-times/commit/2bfa8038d6133e4ab377d1057782624ef809bfba)
#### Tuesday 2023-08-15 04:31:52 by Billy Einkamerer

Created Text For URL [www.irishtimes.com/ireland/2023/08/14/good-night-i-love-you-a-ukrainian-boys-last-words-to-his-sister-in-leitrim-before-the-russian-shell-hit/]

---
## [cashapp/AccessibilitySnapshot](https://github.com/cashapp/AccessibilitySnapshot)@[65521e8e36...](https://github.com/cashapp/AccessibilitySnapshot/commit/65521e8e3666749c3bb4f04f038920a19316f21e)
#### Tuesday 2023-08-15 04:48:54 by Nicholas Entin

Add imprecise comparison variants to iOSSnapshotTestCase extension

This adds variants of the `SnapshotVerify*(...)` methods that allow for imprecise comparisons, i.e. using the `perPixelTolerance` and `overallTolerance` parameters.

 ## Why is this necessary?

Adding tolerances has been a highly requested feature (see #63) to work around some simulator changes introduced in iOS 13. Historically the simulator has supported CPU-based rendering, giving us very stable image representations of views that we can compare pixel-by-pixel. Unfortunately, with iOS 13, Apple changed the simulator to use exclusively GPU-based rendering, which means that the resulting snapshots may differ slightly across machines (see uber/ios-snapshot-test-case#109).

The negative effects of this were mitigated in iOSSnapshotTestCase by adding two tolerances to snapshot comparisons: a **per-pixel tolerance** that controls how close in color two pixels need to be to count as unchanged and an **overall tolerance** that controls what portion of pixels between two images need to be the same (based on the per-pixel calculation) for the images to be considered unchanged. Setting these tolerances to non-zero values enables engineers to record tests on one machine and run them on another (e.g. record new reference images on their laptop and then run tests on CI) without worrying about the tests failing due to differences in GPU rendering. This is great in theory, but from our testing we've found even the lowest tolerance values to consistently handle GPU differences between machine types let through a significant number of visual regressions. In other words, there is no magic tolerance threshold that avoids false negatives based on GPU rendering and also avoids false positives based on minor visual regressions.

This is especially true for accessibility snapshots. To start, tolerances seem to be more reliable when applied to relatively small snapshot images, but accessibility snapshots tend to be fairly large since they include both the view and the legend. Additionally, the text in the legend can change meaningfully and reflect only a small number of pixel changes. For example, I ran a test of full screen snapshot on an iPhone 12 Pro with two columns of legend. Even an overall tolerance of only `0.0001` (0.01%) was enough to let through a regression where one of the elements lost its `.link` trait (represented by the text "Link." appended to the element's description in the snapshot). But this low a tolerance _wasn't_ enough to handle the GPU rendering differences between a MacBook Pro and a Mac Mini. This is a simplified example since it only uses `overallTolerance`, not `perPixelTolerance`, but we've found many similar situations arise even with the combination.

Some teams have developed infrastructure to allow snapshots to run on the same hardware consistently and have built a developer process around that infrastructure, but many others have accepted tolerances as a necessity today.

 ## Why create separate "imprecise" variants?

The simplest approach to adding tolerances would be adding the `perPixelTolerance` and `overallTolerance` parameters to the existing snapshot methods, however I feel adding separate methods with an "imprecise" prefix is better in the long run. The naming is motivated by the idea that **it needs to be very obvious when what you're doing might result in unexpected/undesirable behavior**. In other words, when using one of the core snapshot methods, you should have extremely high confidence that a test passing means there's no regressions. When you use an "imprecise" variant, it's up to you to set your confidence levels according to your chosen tolerances. This is similar to the "unsafe" terminology around memory in the Swift API. You should generally feel very confident in the memory safety of your code, but any time you see "unsafe" it's a sign to be extra careful and not gather unwarranted confidence from the compiler.

Longer term, I'm hopeful we can find alternative comparison algorithms that allow for GPU rendering differences without opening the door to regressions. We can integrate these into the core snapshot methods as long as they do not introduce opportunities for regressions, or add additional comparison variants to iterate on different approaches.

---
## [dannybwebdev/Anadvi_Blog](https://github.com/dannybwebdev/Anadvi_Blog)@[f6581aebce...](https://github.com/dannybwebdev/Anadvi_Blog/commit/f6581aebce8d2065f2bcdfdc92188258ce182259)
#### Tuesday 2023-08-15 04:51:03 by dannybwebdev

Create Blog “2023-08-15-have-you-become-a-back-pocket-boyfriend-or-girlfriend”

---
## [miyoo-oss/linux](https://github.com/miyoo-oss/linux)@[0a2c2baafa...](https://github.com/miyoo-oss/linux/commit/0a2c2baafa312ac4cec4f0bababedab3f971f224)
#### Tuesday 2023-08-15 04:53:51 by Linus Torvalds

proc: fix missing conversion to 'iterate_shared'

I'm looking at the directory handling due to the discussion about f_pos
locking (see commit 797964253d35: "file: reinstate f_pos locking
optimization for regular files"), and wanting to clean that up.

And one source of ugliness is how we were supposed to move filesystems
over to the '->iterate_shared()' function that only takes the inode lock
for reading many many years ago, but several filesystems still use the
bad old '->iterate()' that takes the inode lock for exclusive access.

See commit 6192269444eb ("introduce a parallel variant of ->iterate()")
that also added some documentation stating

      Old method is only used if the new one is absent; eventually it will
      be removed.  Switch while you still can; the old one won't stay.

and that was back in April 2016.  Here we are, many years later, and the
old version is still clearly sadly alive and well.

Now, some of those old style iterators are probably just because the
filesystem may end up having per-inode mutable data that it uses for
iterating a directory, but at least one case is just a mistake.

Al switched over most filesystems to use '->iterate_shared()' back when
it was introduced.  In particular, the /proc filesystem was converted as
one of the first ones in commit f50752eaa0b0 ("switch all procfs
directories ->iterate_shared()").

But then later one new user of '->iterate()' was then re-introduced by
commit 6d9c939dbe4d ("procfs: add smack subdir to attrs").

And that's clearly not what we wanted, since that new case just uses the
same 'proc_pident_readdir()' and 'proc_pident_lookup()' helper functions
that other /proc pident directories use, and they are most definitely
safe to use with the inode lock held shared.

So just fix it.

This still leaves a fair number of oddball filesystems using the
old-style directory iterator (ceph, coda, exfat, jfs, ntfs, ocfs2,
overlayfs, and vboxsf), but at least we don't have any remaining in the
core filesystems.

I'm going to add a wrapper function that just drops the read-lock and
takes it as a write lock, so that we can clean up the core vfs layer and
make all the ugly 'this filesystem needs exclusive inode locking' be
just filesystem-internal warts.

I just didn't want to make that conversion when we still had a core user
left.

Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Christian Brauner <brauner@kernel.org>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[30e35436be...](https://github.com/Droidcraft/evals/commit/30e35436be663f416ce6d125f09f92a1faf70d12)
#### Tuesday 2023-08-15 05:06:08 by Nazar

Hard russian computer science tasks  (#1323)

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

hard_russian_computer_science_tasks

### Eval description

Challenging computer science problems primarily sourced from Russian
academic and competitive programming contexts. The problems cover
various subfields of computer science, including data structures,
algorithms, computational mathematics, and more.

### What makes this a useful eval?

Russian computer science education and competitive programming are known
for their rigorous and complex problem sets. These problems can be used
to assess an GPT's ability to solve high-level, challenging problems.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ + ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ + ] Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.
- [ + ] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ + ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ + ] Check that your data is in `evals/registry/data/{name}`
- [ + ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ + ] Ensure you have the right to use the data you submit via this
eval

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

- [ + ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ + ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ + ] I understand that opening a PR, even if it meets the
requirements above, does not guarantee the PR will be merged nor GPT-4
access be granted.

### Submit eval

- [ + ] I have filled out all required fields of this form
- [ + ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Алёна очень любит алгебру.
Каждый день, заходя на свой любимый алгебраический форум, она с
вероятностью $\\frac14$ находит там новую интересную задачу про группы,
а с вероятностью $\\frac{1}{10}$ интересную задачку про кольца. С
вероятностью $\\frac{13}{20}$ новых задач на форуме не окажется. Пусть
$X$ — это минимальное число дней, за которые у Алёны появится хотя бы
одна новая задача про группы и хотя бы одна про кольца. Найдите
распределение случайной величины $X$. В ответе должны участвовать только
компактные выражения (не содержащие знаков суммирования, многоточий и
пр.)."}], "ideal": "Нам нужно найти $ P[X = k] $. Для этого надо понять
на пальцах, в каком случае $ X = k $. Первый случай — когда в каждый из
предыдущих $ k - 1 $ дней либо не было задач, либо были только про
группы, а в $k$-ый попалась задача про кольца. Второй случай — когда в
каждый из предыдущих $ k - 1 $ дней либо не было задач, либо были только
про кольца, а в $k$-ый попалась задача про группы. На самом деле мы оба
раза учли не подходящий случай, когда все предыдущие $k-1$ дней задач не
было вообще. С поправкой на это ответ будет таким: $P[x=k]=\\left
(\\left (\\frac{13}{20}+\\frac{1}{4}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{10}+\\left
(\\left (\\frac{13}{20}+\\frac{1}{10}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{4}$"}
{"input": [{"role": "system", "content": "В множестве из $n$ человек
каждый может знать или не знать другого (если $A$ знает $B$, отсюда не
следует, что $B$ знает $A$). Все знакомства заданы булевой матрицей
$n×n$. В этом множестве может найтись или не найтись знаменитость —
человек, который никого не знает, но которого знают все. Предложите
алгоритм, который бы находил в множестве знаменитость или говорил, что
ее в этом множестве нет. Сложность по времени — $O(n)$, сложность по
памяти — $O(1)$."}], "ideal": "Для определенности положим
$K_{ij}=\\left\\{\\begin{matrix}1, \\text{если i-й знает j-ого;}
\\\\0\\text{,иначе.}\\end{matrix}\\right.$.\nЗаметим, что если
$K_{ij}=1$, то $i$-ый не может быть знаменитостью, а если $K_{ij}=0$, то
$j$-ый не может быть знаменитостью. Таким образом, за одну проверку
можно исключить одного человека из кандидатов в знаменитости.\nСначала
пусть $s=1$, а $l$ пробегает значения от $22$ до $n$. Если в какой-то
момент $K_{sl}=1$, то приравниваем $s=l$. Тогда значение $s$ после
последней проверки — номер единственного оставшегося кандидата. Чтобы
проверить, является ли этот кандидат знаменитостью, нужно провести еще
$n−1$ проверок, знают ли его остальные, и $n−1$ проверок, знает ли он
остальных. Всего будет проведено $3(n−1)$ проверок, следовательно,
сложность по времени — $O(n)$. Поскольку мы использовали только $2$
переменные, сложность по памяти — $O(1)$."}
{"input": [{"role": "system", "content": "В двумерном полукруге есть n
неизвестных нам точек. Разрешается задавать вопросы вида «каково
расстояние от точки X до ближайшей из этих точек?» Если расстояние
оказывается нулевым, точка считается угаданной. Докажите, что хотя бы
одну из этих точек можно угадать не более чем за $2n+1$ вопрос."}],
"ideal": "Возьмем на диаметре полукруга $n+1$ точку. Точки назовем
$A_1$, $A_2$, … $A_{n+1} и для каждой из них зададим наш вопрос. По
принципу Дирихле, для каких-то двух соседних точек ближайшая точка будет
одна и та же и полученное расстояние было бы до одной и той точки из
множества загаданных точек. Теперь мы рассматриваем точки $B+i$
пересечения окружностей с центрами в точках $A_i$ и $A_{i+1}, $i=1, … ,
n и радиусами равными ответам полученным на предыдущем шаге. По принципу
Дирихле, хотя бы одна из загаданных точек совпадает с одной из точек
$B_i$. Тогда за n вопросов для каждой точки $B_i$ мы получим хотя бы
один ответ 0. Итого нам потребовалось не более (n+1)+n=2n+1 вопросов."}
{"input": [{"role": "system", "content": "В равностороннем треугольнике
$ABC$ площади $1$ выбираем точку $M$. Найти математическое ожидание
площади $ABM$."}], "ideal": "Заметим, что
$M(S_{ABM}+S_{BCM}+S_{CAM})=1$. Тогда из линейности матожидания и
равенства матожиданий площадей треугольников $ABM$, $BCM$ и $CAM$
получим $M(S_{ABM})=\\frac{1}{3}$."}
{"input": [{"role": "system", "content": "Верно ли, что всякая нечетная
непрерывная функция, \nудовлетворяющая условию $f(2x) = 2f(x)$,
линейна."}], "ideal": "Контрпример: $f(x) = x \\cos(2\\pi
\\log_2(|x|))$.\nНеверно."}
{"input": [{"role": "system", "content": "Верно ли, что rank AB = rank
BA для любых квадратных матриц A и B?"}], "ideal": "Пусть
$A=\\begin{pmatrix} 0& 1 \\\\ 1& 0 \\\\ \\end{pmatrix}$, а
$B=\\begin{pmatrix} 1& 0 \\\\ 1& 0 \\\\ \\end{pmatrix}$. Тогда rank AB =
0, но rank BA = 1. Неверно."}
{"input": [{"role": "system", "content":
"Вычислите $\\int_{0}^{2π}(\\sin x)^8dx$."}], "ideal": "Заметим, что
$\\int_{0}^{2\\pi} (\\sin x)^n dx=-\\int_{0}^{2\\pi} (\\sin x)^{n-1}
d(\\cos x)=(n-1)\\int_{0}^{2\\pi} (\\cos x)^2(\\sin x)^{n-2}
dx$.\nИспользуя основное тригонометрическое тождество,
получаем:\n$\\int_{0}^{2\\pi} (\\sin x)^n
dx=\\frac{n-1}{n}\\int_{0}^{2\\pi} (\\sin x)^{n-2}dx$.\nТогда
$\\int_{0}^{2\\pi} (\\sin x)^8 dx=2\\pi
\\prod_{\\substack{k=2\\\\k+=2}}^{8}\\frac{k-1}{k}=\\frac{35\\pi}{64}$."}
{"input": [{"role": "system", "content": "Дан массив из $n$ чисел.
Предложите алгоритм, позволяющий за $O(n)$ операций определить, является
ли этот массив перестановкой чисел от $1$ до $n$. Дополнительной памяти
не более $O(1)$."}], "ideal": "Идея состоит в том, чтобы рассматривать
массив $A$ как подстановку. Пусть индекс $i$ пробегает значения от $0$
до $n−1$. Когда мы встречаем положительный элемент $A[i]$, переходим от
него к элементу $A[A[i]−1]$, от элемента $A[A[i]−1]$ к элементу
$A[A[A[i]−1]−1]$ и так далее, пока мы не не вернемся к $A[i]$, либо не
сможем совершить очередной шаг (в таком случае, массив перестановкой не
является). В процессе меняем знак всех пройденных элементов на
отрицательный. Поскольку на каждом элементе массива мы можем оказаться
максимум два раза, итоговая сложность — $O(n)$. Дополнительная память —
$O(1)$."}
{"input": [{"role": "system", "content": "Дан неориентированный непустой
граф $G$ без петель. Пронумеруем все его вершины. Матрица смежности
графа $G$ с конечным числом вершин $n$ (пронумерованных числами
от 11 до $n$) — это квадратная матрица $A$ размера $n$, в которой
значение элемента $a_{ij}$ равно числу ребер из $i$-й вершины графа
в $j$-ю вершину. Докажите, что матрица $A$ имеет отрицательное
собственное значение."}], "ideal": "Заметим, что $A$ — симметрическая
ненулевая матрица с неотрицательными элементами и нулями на диагонали.
Докажем, что у такой матрицы есть отрицательное собственное
значение.\nИзвестный факт, что симметрическая матрица диагонализуема в
вещественном базисе (все собственные значения вещественны). Допустим,
что все собственные значения $A$ неотрицательны. Рассмотрим квадратичную
форму $q$ с матрицей $A$ в базисе $\\{e1,…,en\\}$. Тогда эта
квадратичная форма неотрицательно определена, так как все собственные
значения неотрицательны. То есть $\\forall v:q(v)⩾0$. С другой стороны,
пусть $a_{ij}≠0$. Тогда $q(e_i−e_j)=a_{ii}−2a_{ij}+a_{jj}=−2a_{ij}<0$.
Это противоречит неотрицательной определенности $q$. Значит, исходное
предположение неверно, и у $A$ есть отрицательное собственное
значение."}
{"input": [{"role": "system", "content": "Дана матрица из нулей и
единиц, причем для каждой строки матрицы верно следующее: если в строке
есть единицы, то они все идут подряд (неразрывной группой из единиц).
Докажите, что определитель такой матрицы может быть равен только $\\pm1$
или $0$."}], "ideal": "Переставляя строки, мы можем добиться того, чтобы
позиции первых (слева) единиц не убывали сверху вниз. При этом
определитель либо не изменится, либо поменяет знак. Если у двух строк
позиции первых единиц совпадают, то вычтем ту, в которой меньше единиц
из той, в которой больше. Определитель при этом не меняется. Такими
операциями мы можем добиться того, что позиции первых единиц строго
возрастают сверху вниз. При этом либо матрица окажется вырожденной, либо
верхнетреугольной с единицами на диагонали. То есть, определитель станет
либо $0$, либо $1$. Так как определитель при наших операциях либо не
менялся, либо поменял знак, изначальный определитель был $\\pm1$ или
$0$."}
  ```
</details>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[305b237cdb...](https://github.com/Droidcraft/evals/commit/305b237cdb3884c7ddb6a5d12cb184a83551fcba)
#### Tuesday 2023-08-15 05:06:08 by Anders Wang-Rask

Irrelevant negative diversion (#1318)

Tests the model's reasoning ability in face of a negative diversion
(e.g. "However, ...") with irrelevant information.

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

irrelevant-negative-diversion

### Eval description

The eval tests the model's ability to reason. It has been demonstrated
that a negative diversion (e.g. "However", "Despite that", "That being
said") can lead the model to a wrong conclusion. Even when the negative
diversion contains more or less irrelevant information (e.g. "However,
they often squabbled as children.")

### What makes this a useful eval?

I have tested GPT-4 through ChatGPT and can see that it often gets these
wrong. It's a little bit random. Where all the samples have the ideal
answer of "yes", ChatGPT would often say No or more often say that it
was unable to conclude.

The prompt is asking the model to choose "yes" or "no" according to what
is most reasonable.

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
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. However, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. But, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. Unfortunately, Anna and Briana squabbled often
as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Sadly, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. But regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Even though, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Despite, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. That being said, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
  ```
</details>

---
## [sarcasticadmin/uronode](https://github.com/sarcasticadmin/uronode)@[90e8bb8717...](https://github.com/sarcasticadmin/uronode/commit/90e8bb8717183edb131a3b1f3cf319bf87302aea)
#### Tuesday 2023-08-15 05:47:16 by n1uro

26/05/2013 v2.1

Fixed a bug in gateway.c where the finger "stop" ansi was white instead
of red (for stop). This was one I missed not having proper routing yet
to fully test. Thanks Brett WA7V for the link!!

Made another change in gateway.c in regards to the handling of the
flexnet destinations listing when using Flex/AX25 ONLY. There is a
reason for this (believe it or not) and that's in the shell and netrom
interfaces they both begin the destinations list with the string
"Flexnet Destinations:". This may cause neighbor URONode/AWZNode/etc
systems using flexd to improperly parse flexnet destinations from each
other. At the moment, I don't have the facilities to properly test this
but am hoping to work something out.

Thanks to Bob K2JJT, I added an include for socket.h in ipc.c. While I
never saw any errors here, I don't believe I've ever tested or compiled
on a Slackware system... Bob uses Slack. K2JJT reported adding this to
ipc.c helped him fix issues with his compile as it was griping about
AF_NETROM. Adding it here made no difference so since it helps Slackware
I'm all for being multi-distro compatable as much as humanly possible.

In reviewing 2.0 changes, it had me look more into the shell function
for sysops. I made a change that more defines which shell you may be
in when you do a 'w' or a 'who' in a linux shell via the node. This
was changed in system.c

Made a patch to node.c where if called from a shell, it would coredump.
Now, if it's called from a shell it simply exits back to the shell
prompt. I believe the same is in other "node" variants to which
the documentation directs the local sysop not to call the node from
a prompt, however KI6ZHD felt this was an issue. Being harmless in
nature to the function of my design I felt it wasn't harmful to add
it in. This patch was provided by David Ranch KI6ZHD. Thanks to him
for providing this, and eliminating any accidental core files on your
hard drives, and to Steven, K6SPI for coding the patch.

Thanks to David KI6ZHD for motivating me to do something I wanted to do
but put it way on the back burner, and to Barry K2MF for his elite C
skills. MHeard now will only print up to the 20 most recent heards. With
the initial routine, it would just dump either the global list heard
or if the user selected a specific interface the entire list for that
interface. At first, it worked fine for telnet and/or ax25/flex
connections but in NetRom it was double spacing. This was fixed by me. I
chose 20 to leave room for system headers and prompt returns. In a
standard 80x25 terminal screen, with a full listing, this should fill
the entire screen without a need for the end user to scroll up and
should help keep some traffic down on a busy network.

Made a change in gateway.c to eliminate the "trying state" message only
in NetRom when trying to connect to a remote NetRom node. This should
keep the node more in compliance with Software2000 specifications.

There was chatter within the BPQ32 user group on Yahoo that URONode was
not releasing any keep-alive timers. Please, this is NOT the duty of
a node Front End to control what the native protocol stack is designed
to do. This is totally sysop configurable. To flag this I strongly
suggest the following be added to your scripts:
echo "600000" > /proc/sys/net/ax25/ax0/idle_timeout
echo "600000" > /proc/sys/net/ax25/ax1/idle_timeout
echo "600000" > /proc/sys/net/ax25/ax2/idle_timeout
and so on... one line for each ax25 interface. This will break the
keep-alive virtual circuit Netrom AND IP will use for transport, and
thus break your IP as well. If you're running IP through an ax25
interface I suggest you leave this defaulted to 0 (disabled).

Rewrote the auto-find routine in gateway.c in do_connect so that first
order of preference for connects searches the destis table from flexd
BEFORE checking the netrom nodes and mheard tables, THEN it will search
for the destination in the netrom nodes if not found in the destis
table and prior to searching the mheard list. If you don't use flexnet,
then this shouldn't be an issue for you. As of this time, I'm unsure
if this would create any bugs if you don't define FlexNet during
the configure procedure. If it does, please file a report on the
online forum at https://www.n1uro.net/forum for me!

Made some changes in util.c and gateway.c in regards to duplicate ax25
route connection attempts. If you attempt to connect twice through the
same path, same call, etc, to clarify the error handling. This was
something I worked with K2MF on in regards to MFNOS. This does not mean
you can't make a connect on the same interface you came in on, you will
get a loop warning but the connect will attempt. If you connect from
the node, and try to connect to <callsign>, loop back into the node,
and try to connect to the same <callsign> again, you will NOT be allowed
to connect. URONode will tell you that a duplicate connection is not
allowed.

Cleaned up the do_routes routine in command.c. Shortened "Quality" to
"Qual" and renamed "Destinations" to "Nodes". After all, netrom doesn't
really use "Destinations", that's more a flexnet thing. Still more
cleanup to do in there *sigh*.

While I was at the do_routes, I noticed missing ansi in do_routes and
do_nodes. This has been fixed (and was previously in 1.0.10). I also
cleaned up the ansi routine in do_destinations in router.c to match
that of the netrom counterpart routines in command.c. Again, this was
done in 1.0.10 *double sigh*.

Rather than include an i686 elf of Craig Small's axdigi cross-port
digipeater which probably would NOT work on a Raspberry PI, I added
it into the Makefile by default. I also added an additional routine
in the configure script to check to insure that this file is made.

I also had to update axdigi.c so that it wouldn't error on the newer
(as if I run newer ha!) gcc. This was done for strcpy so that it
wouldn't produce errors as it does. I suspect in the "OLD" days of
linux/gcc it may have been OK as I consider Craig to be one of the
"village elders" of the packet system on linux.

Added a man page for axdigi. READ THIS VERY CAREFULLY!! To digi through
linux you *must* know some specific information and you might have to
educate your users on how exactly to cross-port digi through you if
they intend to do such. It's not something normally visible to them!
I may add a node-help file on digi...but for now please study the man
page on how. It works and works very slick as I've been testing it for
a couple of months. Mheard also will learn digi paths and use them to
connect to digipeated nodes if need be.

Cleaned up do_nodes in command.c. Shortened Quality to Qual, and the
equivilant of Obs. This will use less chars per line when doing a
node <node> or node * . I've been wanting to do this but saved
it for one of those rainy day things. Guess today was that rainy day?

Cleaned up more code and hope to have it finished before 2.1's final
release. So far I'm doing flexd.c at this point. FYI; code cleanup will
be a 2-fold process. First; I'll be formatting each file so it's at a
level of consistency. Second, things I have commented out for testing
that aren't needed may be permanently removed. I may leave a few things
in in case someone desires to say add a 'Welcome." message to netrom
(which is NOT Software2000 compliant!).

Speaking of which, I see I introduced a bug when ANSI is defined for
a specific user which violates Software2000 specs. I believe I did this
as a fail-safe in the prompt routine however now I see it's not needed
with all the other ANSI cleanups I've done. This change (deletion)
was done in node.c where I forced a shutoff of ANSI upon NetRom connects
only, as NetRom does not display the MOTD.

I rewrote a bit of the reconnect string. The "reconnect" in uronode.conf
should be set to OFF. All connections with the exception of NetRom WILL
reconnect. NetRom defaults to off, however with the {S|D} flags you may
manually request you stay connected. Eventually I will remove this flag
in the file so it will become moot. Please change it now to OFF! This
was done in gateway.c. Previously, these flags were moot in NetRom
connects. With the default to OFF, this keeps the NetRom in URONode
Software2000 compliant. A NetRom disconnect should *never* send any
text back whether it's a user or robot/script. Now a user can request
staying connected to URONode from a incoming NetRom connection. For
clarity sake, this only affects the user IF they connect INTO URONode
via NetRom. The "S" flag works for ax25/Flex/NetRom outbound connects.
A user connecting INTO URONode via ax25/Flex/IP will still automatically
be reconnected after an outbound connect.

N1UAN reports make install fails to install the config files. He's
correct. Changed Makefile.in so that "make install" also includes
make installconf which run by itself will install just the config
files for /etc/ax25.

I'm also working on changing the configure script to have some
"eye candy". This will be a continuing work in progress. You'll see it
as it comes. You will need the package "whiptail" in order to see this
new configuration routine. I don't know if this is standard amongst
ALL distributions, however I do know it comes default in debian and
debian based systems. If this *is* too much of an issue, I'll revert
back to the old method.

Almost forgot about an ANSI bug in extcmd.c where if you created an
external command in the node and the user was in via NetRom, when the
node issued "Welcome back." the ansi did NOT clear the color. I found
this in ver 2.0 and thought I fixed it, apparently not (age catching
up to me?) In any event, this is now fixed and working properly again.
Since most people don't use the +512 Color flags I'm sure it was missed.

Found a non-critical bug in cmdparse.s in regards to running external
commands - where it would automatically input a line feed before it
executed the command. This was the only routine which did this. A
routine like this really got under my skin and I was determined to find
and fix this finally... this was a routine I never changed, and that
was halted today (28 July 2013). Instead of totally removing this line
of code, I changed it to now display "Executing command... " and where
ANSI is defined, it is, naturally, green.

Found a non-critical bug in the Info command where it would show as
the first string to the user: "Help command for help" then it would push
the uronode.info file. This is very wrong. While the Info command does
use the routine of do_help in command.c, Info is an independent internal
command and this should not have occurred. This is now fixed with ANSI
if permissions display ANSI.

Updated the outdated INSTALL text document. It had some now misleading
pieces of information in it as some paths and make options have been
changed. Since no one has said anything to this, I'll assume no one
RTFM? (not surprised! email me and say in the subject line: surprise!
if you do!)

Went through the example config files and heavily commented them so for
new installs, it explains each line more specifically in hopes less
misconfigured systems will be created. I also found some typos as to
man page references - fixed. Also updated some of the help files in
regards to the new changes in relation to the "stay" sub command when
connecting out from URONode.

Note: in node.c I modified the pre-provided segfault patch to now
push text to the local console instructing the local sysop or user
what/how to properly execute the node. This will (I hope) force
some RTFM to occur. Syslog logging was also added in the event this
occurs. Actually, after thinking about this, I figured I'd dummy it up
a bit and have it launch a login anyway. This depends that the local
administrator/sysop -properly configures their box- and does the
following:
1 - add a line in /etc/services to point tcp/3694 to uronode
2 - add uronode as a service in inetd or xinetd
3 - insure you have a local telnet client on the box
4 - enjoy!
You will be reminded about this during the login, and syslog will
reflect a local console login as well.I strongly urge you not to open
2 shells and tail your syslog in one while you try to run URONode from
the console. Wink

Cleaned up a minor routine in do_nodes which lays in command.c where
under an incoming NetRom connect, a user who did "Nodes" received
an extra line feed if the columns were all equal at 4 per row. This
was a bit under my skin... fixed/changed. While I was at it, I changed
the output string when doing "Nodes *" from 'Nodes:' to "Detailed
nodes listing:' which actually makes more sense since it is a detailed
list.

Fixed a minor bug in the way the prompts were handled under certain
telnet clients. This was reported also by Marius Petrescu yo2loj. Under
telnet, I added a carriage return (/r) along with the line feed (/n).
Thank you Marius for the report.

In doing the above, I made an error in the non-ANSI telnet prompt where
the (/r) was also chopping off the first letter of a callsign! OOPS!
This was reported by Ted K1YON. Fixed.

Slightly rewrote the way meminfo() was being handled. While I may have
created a bug in 2.4 and lower kernels, this now should work in 2.6 and
higher kernels. I guess the phrase "if it's not broke don't fix it"
doesn't apply anymore?

FINALLY - split the CHANGES file into a new page!! This makes it easier
for me to input the change notes instead of having to scroll down for 30
seconds Smile Call me lazy but don't call me late for supper! <G>

04/09/2013 v2.2

Made multiple .c file edits to reflect the new libax25-devel .h files.
Currently these were pointing to the older kernel_*.h files and on newer
linux systems was preventing compile. Now URONode should work fine.

Added Marius Petrescu to the URONode team! With his c version of ripv2d,
Marius will (and already has) make a huge impact on the future of
URONode! Welcome Marius to the team! Made a reflection of this in the
configure script.

Marius brought to my attention the issue in the log timer routine where
it was forcing 32-bit. He supplied code to fix this in both system.c and
flexd.c.

While in discussions, Marius brought it to my attention that Ubuntu (and
this includes Mint and any other Ubuntu backed distributions) where they
run as he calls it a "fortified libc6" which segfaults on every (what it
thinks is suspicious) buffer accesses to prevent overflows however this
libc6 itself causes buffer overflowing. Why on earth did the Ubuntu team
ever do this?? Anyway, we're investigating how we're going to handle
this issue. I personally have verified URONode to compile and work on
the new kernel 3.x series on Debian and Fedora.

Known Critical Bugs:
(see below 3 lines)

Known NON-Critical Bugs:
Status memory/swap reporting fix

Wish-list:
Who file sorter
pactor - requested by sv1uy
-----------

Development Information (aka Disclaimer):
URONode is developed on an IBM eSeries 330 eServer with dual 1.2GHz CPUs
The OS is Debian Linux 4 using kernel 2.4.27, libax25 v0.0.11,
ax25-tools v0.0.8 and ax25-apps v0.0.6. This software comes with
absolutely NO guarantees so crash n burn at your own risk. We all may
be surprised and find out that it actually DOES something useful!
URONode may not run 100% depending on environmental conditions specific
to your system.

------------

Comments/suggestions? email: n1uro@n1uro.ampr.org
Gripes??? cat gripes > /dev/null Smile just kidding!

This version will get you going for now. I'll post any changes to:
ftp://ftp.n1uro.net/packet

73 de Brian N1URO

---
## [sarcasticadmin/uronode](https://github.com/sarcasticadmin/uronode)@[465b9c7dc2...](https://github.com/sarcasticadmin/uronode/commit/465b9c7dc293edfe9cc330198b45f139826ccb67)
#### Tuesday 2023-08-15 05:47:16 by n1uro

04/09/2013 v2.2

Made multiple .c file edits to reflect the new libax25-devel .h files.
Currently these were pointing to the older kernel_*.h files and on newer
linux systems was preventing compile. Now URONode should work fine.

Added Marius Petrescu to the URONode team! With his c version of ripv2d,
Marius will (and already has) make a huge impact on the future of
URONode! Welcome Marius to the team! Made a reflection of this in the
configure script.

Marius brought to my attention the issue in the log timer routine where
it was forcing 32-bit. He supplied code to fix this in both system.c and
flexd.c.

While in discussions, Marius brought it to my attention that Ubuntu (and
this includes Mint and any other Ubuntu backed distributions) where they
run as he calls it a "fortified libc6" which segfaults on every (what it
thinks is suspicious) buffer accesseD to prevent overflows however this
libc6 itself causes buffer overflowing. Why on earth did the Ubuntu team
ever do this?? Anyway, we're investigating how we're going to handle
this issue. I personally have verified URONode to compile and work on
the new kernel 3.x series on Debian and Fedora.

In "fixing" the prompt bug earlier reported by Marius, I made an error in
the non-ANSI telnet prompt where the (/r) was also chopping off the first
letter of a callsign! OOPS! This was reported by Ted K1YON. Fixed.

** Key news of this release: ROSE is a LOT more user friendly, AND it also
has the ability to display color screens to the end user. This now means
that URONode is an 8-prompt system! 4 main prompts, and 4 color prompts.
The prompt system is designed to show the end user what protocol/method
they used to connect into URONode with. Also proper SSIDs are displayed
to match that of how the end user connected. I did this because seeing
other nodes, they don't and when (as a user) connect into, for example,
a NetRom node who's ssid is -12 and the node displays something
-=totally=- different, I often wonder if I connected to the proper node.

The new prompt schema is:
telnet   :	user@<sysop>.ampr.org:/uronode$
netrom   :	<none> - this keeps in spec with Software2000
flex/ax25:	=>
rose     :	-=>

Each matches with its own colors as well if you run the ansi flag. The
goodbye message for rose is also different than it is for flex/ax25 and
telnet links. The new RoseID flag is used as a personalized message to
the remote user to say a nice goodbye, and to remind them of your Rose
information. The (V)ersion command also has a rose column added to show
the remote user your rose information. An example of this is included
in the uronode.conf.5 man page.

With such, a new uronode.conf file string called RoseID has been created.
Details are in the file. You must keep the single quotes ' ' around the
string for it to display properly. You have been warned. Also, I've added
a default ExtCmd called ROSe so those who connect remotely can get rose
addresses for now. I'm sure I'll be changing this in the future.

Also, I decided to eliminate the permissions flag for use of hidden interfaces.
Reason being is if a sysop flags an interface to be hidden, they did so for a
specific reason. With that, I moved the ANSI flag from 512 in it's place to
64. This was also changed in the man page uronode.perms.5.

In regards to PBBS forwarding, I -=URGE=- you to read BBS.txt. Since
there's no need for me to rewrite it, please heed my warning here. This
is not something critical, just informational to help you improve your
link with URONode systems.

Fixed a cosmetic bug in regards to windows->linux emulation where when
logging in, sentences were not getting properly wrapped. This was done
in node.c. Other emulations such as PuTTY do not give you in windows
full linux-type emulation. Higher profile programs such as SecureCRT
will. For a free/shareware program I suggest MobiXterm. This also
gives you a raw Xserver emulated screen. Of course, there are no issues
if you use a standard linux console.

Added a .pid file to flexd, code supplied by Jaroslav, OK2JRQ and other
patches such as installer edits, etc. The only patches he supplied that I
have yet to add is the install location patch, and one he feels is good
for non-interactive. Source installs need to be interactive, if not you
would not be compliling - just my honest opinion. I can see in the case
of a possible distro package this may not be desired. The distros for now
can hash that out on their own.

Many more cosmetic bugs fixed/changed. Moreso in ROSE but I did find a
few others in there which needed my attention. I have noticed windows terminal
based programs such as PuTTY have an issue determining \n based line feeds
vs \r carriage returns in C code. This mainly seems to affect the various
8 prompts. It seems if I put both in the code, Windows is happy but *nx
may issue an added line-feed. I had thought I cleaned these all up but
I introduced a couple old ones and some new ones with the ROSE work.

01/10/2014 -2.2 released!

Known Critical Bugs:
SYSop command does NOT spawn a shell anymore. This is due to the changes
with the UNIX98 file system. I'm debating on whether or not I wish to
continue to keep this or possibly eliminate this (for possible security
reasons). I see both PROs and CONs with it. Note: this ONLY affects those
systems which force the use of /dev/ptmx in which one needs to use SOCAT
to create static /dev/tty*# and /dev/pty*# pipes. This only affects the
Kernel 3-series

(see below 3 lines)

Known NON-Critical Bugs:
Status memory/swap reporting fix

Wish-list:
Who file sorter
pactor - requested by sv1uy
callsign sort in netrom - requested by ve2pkt
-----------

Development Information (aka Disclaimer):
URONode wass developed on an IBM eSeries 330 eServer with dual 1.2GHz CPUs
The OS is Debian Linux 4 using kernel 2.4.27, libax25 v0.0.11,
ax25-tools v0.0.8 and ax25-apps v0.0.6. This software comes with
absolutely NO guarantees so crash n burn at your own risk. We all may
be surprised and find out that it actually DOES something useful!
URONode may not run 100% depending on environmental conditions specific
to your system.

------------

Comments/suggestions? email: n1uro@n1uro.ampr.org
Gripes??? cat gripes > /dev/null Smile just kidding!

This version will get you going for now. I'll post any changes to:
ftp://ftp.n1uro.net/packet

Join our support mail list graciously donated by TAPR!
http://www.tapr.org/mailman/listinfo/uronode

73 de Brian N1URO

---
## [sarcasticadmin/uronode](https://github.com/sarcasticadmin/uronode)@[66b3227943...](https://github.com/sarcasticadmin/uronode/commit/66b322794332efdcb876d97d4d7fa0a9f471df7d)
#### Tuesday 2023-08-15 05:47:16 by n1uro

18/04/2016 - v2.6
Removed stale and unused axdigi.conf file. Thanks to David KI6ZHD for
pointing this out that I had a stale file in the archive. This file
belonged to another digi daemon I was going to revive instead of Craig
Small's multi-interface crossport digi daemon. I find that especially
with FlexNet, a multi-interface crossport digipeat system not only is
unique to the native linux kernel BUT is also very efficient. If you
have a stale copy of axdigi.conf floating around, please delete this.

Added a question to engage or disengage interactive configure/make mode.
This idea came to me from a query I received by KI6ZHD. If you choose NOT
to use interactive mode, than you must run make/make upgrade/make install
manually. Note: ALL options including rose and flexnet WILL BE COMPILED IN.

Tomasz SP2L was seeing carriage returns when administering his server
remotely and sending SIGHUP to flexd in the terminal messages confirming
the -HUP. Removed.

Added a version output for FlexD and tweeked the one for axdigi. Now both
helper daemons will display its versions based on URONode's version and
some very brief information about themselves. flexd -v or flexd -h
along with axdigi -v or axdigi -h will bring up this information.

Decided that since there's so many commands beginning with M I would move
the MHeard command to a Jheard command. This keeps the commandset more in
line with other systems except for TheNet and X1J-4, and separates that one
command away from the volume of M's. While at it I also made a JL for
Just heard Long. If you specify an interface, Jheard/JLong engages only for
that interface. Note - JLong will say: it may time out HFers. I also had to
modify Makefile and rework the help files to match. While at it I needed to
modify the uronode.8 MAN page.

Gave Makefile a more modernized compile line option. I'm hoping this will
keep URONode one of packet's better robust nodes.

I noticed some sites were violating Software2000's NetRom specifications
by defaulting reconnect on still in their uronode.conf files. I had thought
that I fixed this in an earlier release. Perhaps I did and then migrated
an old .c file back into the mix? (wouldn't be the first time I've done
that by mistake!) Anyway... three key things Software2000 was insistant upon
were NO CTEXT, NO RECONNECT, NO GOODBYE MESSAGES. If you've noticed, I've
taken ALL that out of URONode. These things were done as to not confuse
robot scripts such as PBBS mail forwarding sessions. While other systems
may wish to continue to violate the NetRom protocol (and others) I will
do everything in my power NOT to.

An anonymous user from sourceforge had a compiler warning on the
do_prompt cycle in config.c and provided a fix for it. I don't know if
the user is even a ham but their alias is dcb314, and we thank them. Their
report and fix which is included:
config.c:407:35: warning: logical 'or' of collectively exhaustive tests is always true [-Wlogical-op]
Source code is
if ((User.ul_type != AF_NETROM) || (User.ul_type != AF_INET) ||
(User.ul_type != AF_INET6)) {
Maybe better code
if ((User.ul_type != AF_NETROM) && (User.ul_type != AF_INET) &&
(User.ul_type != AF_INET6)) {
While I don't get the warning he had, the logistics seem to be fine. Thanks
again to dcb314 at sourceforge for their report.

I have made a diff file for JNOS2.0K that makes it a bit more user
compatible with URONode, and other linux-based nodes. For almost 30 years
TCP port 3694 has been used for inbound telnet for linux-based nodes, and
URONode is no exception... just as IP protocol 93 is for axip and UDP
port 93 is for axudp (again other systems love to violate protocols, we
try not to). Besides my little isms that I like in xNOS which I often
contributed to K2MF for MFNOS, I've began to do similar for JNOS. I'm adding
the .diff file in the main code distribution so if you do run JNOS 2.0K as
your PBBS TCP port 3694 is now recognized in JNOS with my patch. I have
as of this writing submitted it to Maiko for considerations, I don't know
if he's going to use it or not. If you do want to patch your JNOS 2.0K
copy it into your jnos source directory and run: patch -p1 -i jnos20k.diff
and you should see about a half dozen files updated. If Maiko doesn't wish
to include this and you want me to keep up to date with it, let me know.

With the recent CVE study on Winlink2000 and plain text passwords exposed, I
went through URONode to insure it wasn't posessing the same issue. By
default URONode doesn't ask for ANY passwords however it's highly suggested
that the sysop require passwords on any internet or amprnet interface. Before
yes, a sysop could require a password on an ax25/NetRom/Rose interface which
would be exposed. Now, if a sysop mistakenly tries to force a password
on RF, it will be ignored by the node so it's not exposed.

----------- Note on SystemD --------
In uronode.socket, you'll notice the line:
ListenStream=0.0.0.0:3694
This tells SystemD to listen on TCP socket 3694 for any IPv4 ONLY incoming
connection. If you wish to filter JUST your amprnet and IPv4 localhost
IPs make a line for each changing 0.0.0.0 to 127.0.0.1 and another for
your amprnet IP. This will by default filter any commercial IP requests
to URONode. If you want SystemD to try IPv6 *first*, don't enter in any
IP schemas and just list the port number. SystemD by default appears to
use IPv6 prior to IPv4.

You can verify the above by running systemctl status uronode.socket:
ystemctl status uronode.socket
● uronode.socket - URONode Server Activation Socket
   Loaded: loaded (/usr/lib/systemd/system/uronode.socket; enabled)
   Active: active (listening) since Mon 2016-03-07 15:30:39 EST; 6min ago
   Listen: 0.0.0.0:3694 (Stream)
 Accepted: 3; Connected: 1

----------- Wish-list: -----------
----------------------------------
Original Development Information (aka Disclaimer): URONode was developed
on an IBM eSeries 330 eServer with dual 1.2GHz CPUs The OS is Debian
Linux 4 using kernel 2.4.27, libax25 v0.0.11, ax25-tools v0.0.8 and
ax25-apps v0.0.6. This software comes with absolutely NO guarantees so
crash n burn at your own risk. We all may be surprised and find out that
it actually DOES something useful! URONode may not run 100% depending on
environmental conditions specific to your system.

URONode is GLPv2 code, and tested by it's main author on the following
platforms: Raspberry Pi ver. B, Debian 7.7 on a Core-i3, Ubuntu
12.0.4LTS on a Core-i3, Fedora ver. 21

------------

Comments/suggestions? email: n1uro@n1uro.ampr.org Gripes??? cat gripes >
/dev/null :D just kidding!

This version will get you going for now. I'll post any changes to:
ftp://ftp.n1uro.net/packet and https://uronode.sourceforge.net. You may
also find URONode in your distro's repositories. <dnf/yum or apt-cache>
search uronode

Join our support mail list graciously donated by TAPR!
http://www.tapr.org/mailman/listinfo/uronode

73 de Brian N1URO

---
## [sarcasticadmin/uronode](https://github.com/sarcasticadmin/uronode)@[f6214eeb0a...](https://github.com/sarcasticadmin/uronode/commit/f6214eeb0a3b0219012dbccc7949a29fdf2dee2d)
#### Tuesday 2023-08-15 05:47:16 by n1uro

15/06/2017 - v2.8
In gateway.c I cleaned up the do_ping routing slightly. I was going to add
a default timer but instead decided to let the user hit enter for their own
"timer" of sorts. Users are also now instructed on the node to hit enter
in order to abort a ping.

Cleaned up do_nodes so now if there's a slime trail node, rather than prefix
it with a colon ":", now it will display ##TEMP: instead. This was sorta
bugging me on just how to handle these. While I was at it, I made a
modification to gateway.c so if a user tried to "C ##TEMP" it instructs the
end user to use the callsign-ssid. I can't think of any other node that does
this.

Thanks to Dave Hibbard (at Debian) for pointing out a dropped "t" in the word
"software" in flexd.c when the -v switch is used.

Cleaned up some prompt routines including the ipv4/ipv6 login sequences.
Before (especially with ipv6) if a callsign had no permissions to login via
the internet they were never informed how to gain access - they were simply
denied. I found this to somewhat make the node a bit unfriendly. Fixed.

With all the chatter on the 44-net list about IPv6, I've decided to get my
block active for further testing. In doing so, I noticed that if a user
telnetted in via IPv6 and made a NetRom connect out, the node failed to
inform them that they were connected... fixed.

As of this writing there's no outboud telnet or dns functions for IPv6
but that's not to say it's not in the works. Personally, I don't see a
true need for IPv6 outbound for amateur radio as the amprnet is going
quite strong however that's not to say things may not change either. If
anything, IPv6 through an HE.net tunnel works as slick as the amprnet
does with the exception of how it handles dynamic clients. Other than
that, it does appear to tunnel through your ISP filters as amprnet
does which is a plus.

----------- Note on SystemD --------
In uronode.socket, you'll notice the line:
ListenStream=0.0.0.0:3694
This tells SystemD to listen on TCP socket 3694 for any IPv4 ONLY incoming
connection. If you wish to filter JUST your amprnet and IPv4 localhost
IPs make a line for each changing 0.0.0.0 to 127.0.0.1 and another for
your amprnet IP. This will by default filter any commercial IP requests
to URONode. If you want SystemD to try IPv6 *first*, don't enter in any
IP schemas and just list the port number. SystemD by default appears to
use IPv6 prior to IPv4.

You can verify the above by running systemctl status uronode.socket:
ystemctl status uronode.socket
● uronode.socket - URONode Server Activation Socket
   Loaded: loaded (/usr/lib/systemd/system/uronode.socket; enabled)
   Active: active (listening) since Mon 2016-03-07 15:30:39 EST; 6min ago
   Listen: 0.0.0.0:3694 (Stream)
 Accepted: 3; Connected: 1

----------- Wish-list: -----------
----------------------------------
Original Development Information (aka Disclaimer): URONode was developed
on an IBM eSeries 330 eServer with dual 1.2GHz CPUs The OS is Debian
Linux 4 using kernel 2.4.27, libax25 v0.0.11, ax25-tools v0.0.8 and
ax25-apps v0.0.6. This software comes with absolutely NO guarantees so
crash n burn at your own risk. We all may be surprised and find out that
it actually DOES something useful! URONode may not run 100% depending on
environmental conditions specific to your system.

URONode is GLPv2 code, and tested by it's main author on the following
platforms: Raspberry Pi ver. B, Debian 7.7 on a Core-i3, Ubuntu
12.0.4LTS on a Core-i3, Fedora ver. 21

------------

Comments/suggestions? email: n1uro@n1uro.ampr.org Gripes??? cat gripes >
/dev/null :D just kidding!

This version will get you going for now. I'll post any changes to:
ftp://ftp.n1uro.net/packet and https://uronode.sourceforge.net. You may
also find URONode in your distro's repositories. <dnf/yum or apt-cache>
search uronode

Join our support mail list graciously donated by TAPR!
http://www.tapr.org/mailman/listinfo/uronode

73 de Brian N1URO

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[dc6ddd821b...](https://github.com/unit0016/effigy-se/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Tuesday 2023-08-15 06:05:54 by Cheshify

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
## [G-Rath/osv-scanner](https://github.com/G-Rath/osv-scanner)@[53107dd285...](https://github.com/G-Rath/osv-scanner/commit/53107dd2851eb10df2c8c5044c0319ae54a953d4)
#### Tuesday 2023-08-15 06:06:45 by Gareth Jones

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
## [Folkess/tgstation](https://github.com/Folkess/tgstation)@[f0dc574c37...](https://github.com/Folkess/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Tuesday 2023-08-15 07:11:45 by carlarctg

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
## [rkc137/numbers](https://github.com/rkc137/numbers)@[dd57a7773a...](https://github.com/rkc137/numbers/commit/dd57a7773aec5e9244a891c0829f6910c24a388d)
#### Tuesday 2023-08-15 07:36:21 by rkc137

why i dont use stl god damn i need to refresh all this shit

---
## [Hocnonsense/snakemake](https://github.com/Hocnonsense/snakemake)@[c9eaa4e12e...](https://github.com/Hocnonsense/snakemake/commit/c9eaa4e12e4a348f93e5ea5793faaec1fd547fac)
#### Tuesday 2023-08-15 08:11:52 by Vanessasaurus

feat: support for external executor plugins (#2305)

Hi @johanneskoester! :wave: As we chat about in a thread somewhere, I
think it would be really powerful to allow for installing (and
discovering) external plugins to Snakemake. Specifically for the Flux
Operator, I have easily three designs I'm testing, and it's not really
appropriate to add them proper to snakemake - but I believe the
developer user should be empowered to flexibly add/remove and test them
out.

This pull request is first try demo of how snakemake could allow
external executor plugins. I say "first try" because it's the first time
I've experimented with plugins, and I tried to choose a design that
optimizes simplicity and flexibility without requiring external
packages, or specific features of setuptools or similar (that are likely
to change). The basic design here uses pkgutil to discover
snakemake_executor_* plugins, and then provides them to the client (to
add arguments) and scheduler to select using one with `--executor`.

I've written up an entire tutorial and the basic design in this early
prototype, which is basically the current Flux integration as a plugin!
https://github.com/snakemake/snakemake-executor-flux. The user would
basically do:

```bash
# Assuming this was released on pypi (it's not yet)
$ pip install snakemake-executor-flux

# Run the workflow using the flux custom executor
$ snakemake --jobs 1 --executor flux
```
I've designed it so that plugins are validated only when chosen, and
each plugin can add or otherwise customize the parser, and then (after
parsing) further tweak the args if chosen. Then in scheduler.py, we
simply look if the user selected a plugin, and call the main executor
(and local_executor) classes if this is the case.

The one hard piece is having a flexible way to pass forward all those
custom arguments. The current snakemake design has basically a custom
boolean for every executor hard coded (e.g., `--flux` or `--slurm`) and
while we don't want to blow that up, I'm worried moving forward passing
all these custom namespaced arguments through the init, workflow,
scheduler/dag, is going to get very messy. So the approach here is a
suggested way to handle the expanding space of additional executors by
way of passing forward full args, and then allowing the plugins to
customize the parser before or after. If we were to, for example, turn
current executors into plugins (something I expect we might want to do
for the Google Life Sciences API that is going to be deprecated in favor
of batch) we could write out a more hardened spec - some configuration
class that is passed from the argument parser through the executor and
through execution (instead of all the one off arguments).

Anyway - this is just a first shot and I'm hoping to start some
discussion! This is a totally separate thing from TBA work with Google
Batch - this is something that I've wanted to try for a while as I've
wanted to add more executors and have seen the executor space exploding.
:laughing: I haven't written tests or updated any docs yet pending our
discussion!

### QC

* [ ] The PR contains a test case for the changes or the changes are
already covered by an existing test case.
* [ ] The documentation (`docs/`) is updated to reflect the changes or
this is not necessary (e.g. if the change does neither modify the
language nor the behavior or functionalities of Snakemake).

---------

Signed-off-by: vsoch <vsoch@users.noreply.github.com>
Co-authored-by: vsoch <vsoch@users.noreply.github.com>
Co-authored-by: Johannes Köster <johannes.koester@tu-dortmund.de>
Co-authored-by: Johannes Köster <johannes.koester@uni-due.de>

---
## [ProjectIgnis/BabelCDB](https://github.com/ProjectIgnis/BabelCDB)@[031d35c929...](https://github.com/ProjectIgnis/BabelCDB/commit/031d35c929faae7ee5bb3fb6a98c72d7ce6bd280)
#### Tuesday 2023-08-15 08:14:51 by Yoshi80

added new rush alt arts

-CAN:D LIVE
-Sevens Road Witch
-Magical Sheep Girl Meeeg-chan
-Prophecy Phrase of the Colors of the Wind
-Cat Claw Girl
-Machvio of the Ultimate Aria
-Star Replacer
-Mad Rare Aquila
-Protection of Arthenée
-Rice Terrace Crisis
-The Strange Specter of Celestial Starts
-Steel Soldier Gale Vinary
-Rising Light Angel Esser
-Amusi Annoyance

---
## [AnywayFarus/tgstation](https://github.com/AnywayFarus/tgstation)@[2ee79d7077...](https://github.com/AnywayFarus/tgstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Tuesday 2023-08-15 08:45:52 by Jacquerel

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
## [williamli/next.js](https://github.com/williamli/next.js)@[e06880ea4c...](https://github.com/williamli/next.js/commit/e06880ea4c061fc5c298b262d01f347edd8dce74)
#### Tuesday 2023-08-15 09:07:19 by Josh Story

Implement new forking technique for vendored packages. (#51083)

## Vendoring

Updates all module resolvers (node, webpack, nft for entrypoints, and nft for next-server) to consider whether vendored packages are suitable for a given resolve request and resolves them in an import semantics preserving way.

### Problem

Prior to the proposed change, vendoring has been accomplished but aliasing module requests from one specifier to a different specifier. For instance if we are using the built-in react packages for a build/runtime we might replace `require('react')` with `require('next/dist/compiled/react')`.

However this aliasing introduces a subtle bug. The React package has an export map that considers the condition `react-server` and when you require/import `'react'` the conditions should be considered and the underlying implementation of react may differ from one environment to another. In particular if you are resolving with the `react-server` condition you will be resolving the `react.shared-subset.js` implementation of React. This aliasing however breaks these semantics because it turns a bare specifier resolution of `react` with path `'.'` into a resolution with bare specifier `next` with path `'/dist/compiled/react'`. Module resolvers consider export maps of the package being imported from but in the case of `next` there is no consideration for the condition `react-server` and this resolution ends up pulling in the `index.js` implementation inside the React package by doing a simple path resolution to that package folder.

To work around this bug there is a prevalence of encoding the "right" resolution into the import itself. We for instance directly alias `react` to `next/dist/compiled/react/react.shared-subset.js` in certain cases. Other times we directly specify the runtime variant for instance `react-server-dom-webpack/server.edge` rather than `react-server-dom-wegbpack/server`, bypassing the export map altogether by selecting the runtime specific variant. However some code is meant to run in more than one runtime, for instance anything that is part of the client bundle which executes on the server during SSR and in the browser. There are workaround like using `require` conditionally or `import(...)` dynamically but these all have consequences for bundling and treeshaking and they still require careful consideration of the environment you are running in and which variant needs to load.

The result is that there is a large amount of manual pinning of aliases and additional complexity in the code and an inability to trust the package to specify the right resolution potentially causing conflicts in future versions as packages are updated.

It should be noted that aliasing is not in and of itself problematic when we are trying to implement a sort of lightweight forking based on build or runtime conditions. We have good examples of this for instance with the `next/head` package which within App Router should export a noop function. The problem is when we are trying to vendor an entire package and have the package behave semantically the same as if you had installed it yourself via node_modules

### Solution

The fix is seemingly straight forward. We need to stop aliasing these module specifiers and instead customize the resolution process to resolve from a location that will contain the desired vendored packages. We can then start simplifying our imports to use top level package resources and generally and let import conditions control the process of providing the right variant in the right context.

It should be said that vendoring is conditional. Currently we only vendor react pacakges for App Router runtimes. The implementation needs to be able to conditionally determine where a package resolves based on whether we're in an App Router context vs a Page Router one.

Additionally the implementation needs to support alternate packages such as supporting the experimental channel for React when using features that require this version.

### Implementation

The first step is to put the vendored packages inside a node_modules folder. This is essential to the correct resolving of packages by most tools that implement module resolution. For packages that are meant to be vendored, meaning whole package substitution we move the from `next/(src|dist)/compiled/...` to `next/(src|dist)/vendored/node_modules`. The purpose of this move is to clarify that vendored packages operate with a different implementation. This initial PR moves the react dependencies for App Router and `client-only` and `server-only` packages into this folder. In the future we can decide which other precompiled dependencies are best implemented as vendored packages and move them over.

It should be noted that because of our use of `JestWorker` we can get warnings for duplicate package names so we modify the vendored pacakges for react adding either `-vendored` or `-experimental-vendored` depending on which release channel the package came from. While this will require us to alter the request string for a module specifier it will still be treating the react package as the bare specifier and thus use the export map as required.

#### module resolvers
The next thing we need to do is have all systems that do module resolution implement an custom module resolution step. There are five different resolvers that need to be considered

##### node runtime
Updated the require-hook to resolve from the vendored directory without rewriting the request string to alter which package is identified in the bare specifier. For react packages we only do this vendoring if the `process.env.__NEXT_PRIVATE_PREBUNDLED_REACT` envvar is set indicating the runtime is server App Router builds. If we need a single node runtime to be able to conditionally resolve to both vendored and non vendored versions we will need to combine this with aliasing and encode whether the request is for the vendored version in the request string. Our current architecture does not require this though so we will just rely on the envvar for now

##### webpack runtime
Removed all aliases configured for react packages. Rely on the node-runtime to properly alias external react dependencies. Add a resolver plugin `NextAppResolverPlugin` to preempt perform resolution from the context of the vendored directory when encountering a vendored eligible package.

##### turbopack runtime
updated the aliasing rules for react packages to resolve from the vendored directory when in an App Router context. This implementation is all essentially config b/c the capability of doing the resolve from any position (i.e. the vendored directory) already exists

##### nft entrypoints runtime
track chunks to trace for App Router separate from Pages Router. For the trace for App Router chunks use a custom resolve hook in nft which performs the resolution from the vendored directory when appropriate.

##### nft next-server runtime
The current implementation for next-server traces both node_modules and vendored version of packages so all versions are included. This is necessary because the next server can run in either context (App vs Page router) and may depend on any possible variants. We could in theory make two traces rather than a combined one but this will require additional downstream changes so for now it is the most conservative thing to do and is correct

Once we have the correct resolution semantics for all resolvers we can start to remove instances targeting our precompiled instances for instance making `import ... from "next/dist/compiled/react-server-dom-webpack/client"` and replacing with `import ... from "react-server-dom-webpack/client"`

We can also stop requiring runtime specific variants like `import ... from "react-server-dom-webpack/client.edge"` replacing it with the generic export `"react-server-dom-webpack/client"`

There are still two special case aliases related to react
1. In profiling mode (browser only) we rewrite `react-dom` to `react-dom/profiling` and `scheduler/tracing` to `scheduler/tracing-profiling`. This can be moved to using export maps and conditions once react publishses updates that implement this on the package side.
2. When resolving `react-dom` on the server we rewrite this to `react-dom/server-rendering-stub`. This is to avoid loading the entire react-dom client bundle on the server when most of it goes unused. In the next major react will update this top level export to only contain the parts that are usable in any runtime and this alias can be dropped entirely

There are two non-react packages currently be vendored that I have maintained but think we ought to discuss the validity of vendoring. The `client-only` and `server-only` packages are vendored so you can use them without having to remember to install them into your project. This is convenient but does perhaps become surprising if you don't realize what is happening. We should consider not doing this but we can make that decision in another discussion/PR.

#### Webpack Layers
One of the things our webpack config implements for App Router is layers which allow us to have separate instances of packages for the server components graph and the client (ssr) graph. The way we were managing layer selection was a but arbitrary so in addition to the other webpack changes the way you cause a file to always end up in a specific layer is to end it with `.serverlayer`, `.clientlayer` or `.sharedlayer`. These act as layer portals so something in the server layer can import `foo.clientlayer` and that module will in fact be bundled in the client layer.

#### Packaging Changes
Most package managers are fine with this resolution redirect however yarn berry (yarn 2+ with PnP) will not resolve packages that are not defined in a package.json as a dependency. This was not a problem with the prior strategy because it was never resolving these vendored packages it was always resolving the next package and then just pointing to a file within it that happened to be from react or a related package.

To get around this issue vendored packages are both committed in src and packed as a tgz file. Then in the next package.json we define these vendored packages as `optionalDependency` pointing to these tarballs. For yarn PnP these packed versions will get used and resolved rather than the locally commited src files. For other package managers the optional dependencies may or may not get installed but the resolution will still resolve to the checked in src files. This isn't a particularly satisfying implemenation and if pnpm were to be updated to have consistent behavior installing from tarballs we could actually move the vendoring entirely to dependencies and simplify our resolvers a fair bit. But this will require an upstream chagne in pnpm and would take time to propogate in the community since many use older versions

#### Upstream Changes

As part of this work I landed some other changes upstream that were necessary. One was to make our packing use `npm` to match our publishing step. This also allows us to pack `node_modules` folders which is normally not supported but is possible if you define the folder in the package.json's files property.

See: #52563

Additionally nft did not provide a way to use the internal resolver if you were going to use the resolve hook so that is now exposed

See: https://github.com/vercel/nft/pull/354

#### additional PR trivia
* When we prepare to make an isolated next install for integration tests we exclude node_modules by default so we have a special case to allow `/vendored/node_modules`

* The webpack module rules were refactored to be a little easier to reason about and while they do work as is it would be better for some of them to be wrapped in a `oneOf` rule however there is a bug in our css loader implementation that causes these oneOf rules to get deleted. We should fix this up in a followup to make the rules a little more robuts.


## Edits
* I removed `.sharedlayer` since this concept is leaky (not really related to the client/server boundary split) and it is getting refactored anyway soon into a precompiled runtime.

---
## [dvsdude2/doom](https://github.com/dvsdude2/doom)@[848fde9b36...](https://github.com/dvsdude2/doom/commit/848fde9b36b3fc86787375e89f419d6f318aa99b)
#### Tuesday 2023-08-15 09:25:58 by dvsdude2

changes were made....repos need updating

still in the process of integrating my config with doom better.
added more pkgs cause ....why not?
here some changes that maybe need more description
this will be from config.org

@@ -112,6 +112,11 @@ Startup-settings
- added the save place setting into start-up dont plan on changing them
so no need for it's own header

@@ -170,7 +175,7 @@ dashboard
- this don't look like much but it is predefinded by doom and does
couple of things one of which is it open it in it's own workspace and
names it rss. Like this part, however it opens it to the right of the
main page and I have got in the habit of opening another workspace to
the right. this causes me to never use that first workstation not a big
deal. keeping this for a while. I think there is a command to move said
workspace and probably a easy way to add it to the config and have it
automated ....what ever!

@@ -299,13 +304,13 @@ org-settings
- like this package "org-pandoc-import" just never sure if I'm accually
using it or got it set right. have the ability to do it with pandoc but
like how this makes that even easier. So did a quick check and updated
it to the doom-way and added some better description

@@ -317,7 +322,7 @@ org-settings
- reset after debugging

@@ -440,6 +445,90 @@ doom-Smartparens
- added this for reference :tangle no (already is)

@@ -453,27 +542,52 @@ evil-surround
- adding doom-mod-configs and reordering some headers

@@ -711,7 +830,7 @@ cape
- comment by minad on a forum made me take a closer look at my settings
try some fine-tuning. the TLDR is he proposes that triggering them
manually is better.

@@ -939,38 +1050,7 @@ consult-doom
- more doom intergation and references

@@ -1267,12 +1375,13 @@ personal-settings
- one of the typing exercise packages that I'm tring out

@@ -1287,12 +1396,13 @@ personal-settings
- new function for occur to put cursor in it's buffer after search

@@ -1301,14 +1411,14 @@ way of pasting that automatically surrounds the snippet in blocks,
- add some links here. this sounds like something I would use but have
not used much mainly because I forget its here. added a not to remember
next time.

@@ -1346,26 +1456,204 @@ my-keybindings
- added doom-keybinding reference

@@ -1867,7 +2137,12 @@ Elfeed
- BUG after reverting emacs back to 28.2.2 something got lost and there
was no function definition for elfeed-expose. found it and just added it
it was small so hacky but worked. did work so thinking this is temporary

@@ -2102,8 +2380,8 @@ EWW
@@ -2150,9 +2428,9 @@ EWW
- trying to debug why eww chokes on pdfs

@@ -2456,17 +2746,98 @@ logos
- try another "Prot" package this time logos
- the problem is I only get about 30% of Prot's packages to work. not
sure why if it's just me or the translation to doom not working not sure
but like the other Prot packages I have yet to get this to work properly
- will keep "f"ing with it for now.

---
## [Robbbert/exp](https://github.com/Robbbert/exp)@[e97630981c...](https://github.com/Robbbert/exp/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Tuesday 2023-08-15 10:08:27 by A-Noid33

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
## [RogerBarreto/semantic-kernel](https://github.com/RogerBarreto/semantic-kernel)@[2733a5574f...](https://github.com/RogerBarreto/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Tuesday 2023-08-15 11:02:56 by Mark Karle

Python: Import OpenAPI documents into the semantic kernel (#2297)

### Motivation and Context

<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->

This allows us to import OpenAPI documents, including ChatGPT plugins,
into the Semantic Kernel.

### Description

<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
- The interface reads the operationIds of the openapi spec into a skill:
```python
from semantic_kernel.connectors.openapi import register_openapi_skill
skill = register_openapi_skill(kernel=kernel, skill_name="test", openapi_document="url/or/path/to/openapi.yamlorjson")
skill['operationId'].invoke_async()
```
- Parse an OpenAPI document
- For each operation in the document, create a function that will
execute the operation
- Add all those operations to a skill in the kernel
- Modified `import_skill` to accept a dictionary of functions instead of
just class so that we can import dynamically created functions
- Created unit tests

TESTING:
I've been testing this with the following ChatGPT plugins:
- [Semantic Kernel Starter's Python Flask
plugin](https://github.com/microsoft/semantic-kernel-starters/tree/main/sk-python-flask)
- [ChatGPT's example retrieval
plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/docs/providers/azuresearch/setup.md)
- This one was annoying to setup. I didn't get the plugin functioning,
but I was able to send the right API requests
- Also, their openapi file was invalid. The "servers" attribute is
misindented
- [Google ChatGPT
plugin](https://github.com/Sogody/google-chatgpt-plugin)
- [Chat TODO plugin](https://github.com/lencx/chat-todo-plugin)
- This openapi file is also invalid. I checked with an online validator.
I had to remove"required" from the referenced request objects'
properties:
https://github.com/lencx/chat-todo-plugin/blob/main/openapi.yaml#L85

Then I used this python file to test the examples:

```python
import asyncio
import logging

import semantic_kernel as sk
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
from semantic_kernel.connectors.openapi.sk_openapi import register_openapi_skill

# Example usage
chatgpt_retrieval_plugin = {
    "openapi": # location of the plugin's openapi.yaml file,
    "payload": {
        "queries": [
            {
                "query": "string",
                "filter": {
                    "document_id": "string",
                    "source": "email",
                    "source_id": "string",
                    "author": "string",
                    "start_date": "string",
                    "end_date": "string",
                },
                "top_k": 3,
            }
        ]
    },
    "operation_id": "query_query_post",
}

sk_python_flask = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"skill_name": "FunSkill", "function_name": "Joke"},
    "payload": {"input": "dinosaurs"},
    "operation_id": "executeFunction",
}
google_chatgpt_plugin = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "query_params": {"q": "dinosaurs"},
    "operation_id": "searchGet",
}

todo_plugin_add = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo": "finish this"},
    "operation_id": "addTodo",
}

todo_plugin_get = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "operation_id": "getTodos",
}

todo_plugin_delete = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo_idx": 0},
    "operation_id": "deleteTodo",
}


plugin = todo_plugin_get # set this to the plugin you want to try

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

kernel = Kernel(log=logger)
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_text_completion_service(
    "dv", AzureTextCompletion(deployment, endpoint, api_key)
)

skill = register_openapi_skill(
    kernel=kernel, skill_name="test", openapi_document=plugin["openapi"]
)
context_variables = ContextVariables(variables=plugin)
result = asyncio.run(
    skill[plugin["operation_id"]].invoke_async(variables=context_variables)
)
print(result)
```

### Contribution Checklist

<!-- Before submitting this PR, please make sure: -->

- [ ] The code builds clean without any errors or warnings
- [ ] The PR follows the [SK Contribution
Guidelines](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
and the [pre-submission formatting
script](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md#development-scripts)
raises no violations
- [ ] All unit tests pass, and I have added new tests where possible
- [ ] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <abharris@microsoft.com>

---
## [popek1990/namada-testnets](https://github.com/popek1990/namada-testnets)@[b4c14e6c11...](https://github.com/popek1990/namada-testnets/commit/b4c14e6c11dab3a6e5025bb3325b8f646cf1868d)
#### Tuesday 2023-08-15 11:17:00 by popek1990.eth

Add a popek1990.toml

Hello, 

I'm popek1990.eth. 

I've been working in the web2 & web3 industry for over half of my life. My beginnings involve creating web2 websites and php forums using html/css/php. Later on, I delved into SEO & marketing. Throughout my life, I've been in love with Linux, especially the Debian distribution which I still use to this day. For the past 4 years, I've been developing my skills in the areas of blockchain and smart contracts. I'm deeply interested in privacy, which led me to discover NAMADA. Previously, I ran my own node in Monero & [Railgun](https://railgun.org/).

 I want to be an active member of the community. I'm also an influencer in the Polish crypto market, and my goal is to spread the good word about crypto technology through articles on my [mirror.xyz](https://mirror.xyz/popek1990.eth) . I would be very pleased if I could join as a genesis validator. I'm aware that I'm joining late, but I've been systematically observing the NOMADA project for many months. I've read the entire whitepaper and .docs, and I'm very impressed with your vision. 

Here are my links: https://linktr.ee/popek1990

Of course, NOMADA and all repositories installed on a strong server and ready to go. I'd like join to testnet 12 ale pre-gnosis validator.

---
## [Tkiliay/android_kernel_xiaomi_sm8250](https://github.com/Tkiliay/android_kernel_xiaomi_sm8250)@[5469bf88d2...](https://github.com/Tkiliay/android_kernel_xiaomi_sm8250/commit/5469bf88d2e43b87300a97cfe9f50b989d65c03b)
#### Tuesday 2023-08-15 11:17:38 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [Iajret/FluffySTG](https://github.com/Iajret/FluffySTG)@[54ce0ae44a...](https://github.com/Iajret/FluffySTG/commit/54ce0ae44ae9c1534fe4e4917a7be0e83a69d589)
#### Tuesday 2023-08-15 11:19:40 by SkyratBot

There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [MossesRoss/Hand_controller](https://github.com/MossesRoss/Hand_controller)@[8d747e6ab1...](https://github.com/MossesRoss/Hand_controller/commit/8d747e6ab132a1bd61175af6c0b553482089caef)
#### Tuesday 2023-08-15 11:34:17 by Mosses Ross

create virtual_mouse.py

Hey there! Alright, so I see you're interested in understanding how this code works. No worries, I'll break it down for you step by step.

**Step 1:** We're getting ready by bringing in some tools that we'll use to make our virtual keyboard with hand gestures. Think of these like the tools you need before building something cool.

**Step 2:** We're getting the "mediapipe hands" tool ready. This is like a magic box that helps us see and understand where your hands are in front of the camera.

**Step 3:** We're turning on your computer's camera. It's like switching on your phone's camera so you can see what's in front of it.

**Step 4:** We're starting a loop, which means we're going to do some things over and over again until we decide to stop. Each time we do this loop, we'll take a look at what the camera sees.

**Step 5:** We're looking at what the camera sees and trying to understand where your hands are using the magic "mediapipe hands" tool. This tool helps us find special points on your hands, like the tip of your finger.

**Step 6:** If the magic tool sees your hand, we're going to do something with that information. We're going to pretend that your finger is typing on a virtual keyboard based on where it is on the screen. If it's high up, we'll type "Hello." If it's in the middle, we'll type "World." And if it's low down, we'll type "Gesture."

**Step 7:** We're showing you what the camera sees and the magic tool understands. It's like having a window on your computer screen that shows you what the camera is looking at.

**Step 8:** We're paying attention to your computer keyboard. If you press the "Esc" key (that's like the exit button), we'll stop doing our loop and everything will stop running.

**Step 9:** Once we're done and you're ready to close the program, we'll turn off the camera and close the window that was showing you what the camera saw. It's like turning off your phone's camera when you're done taking pictures.

Hope that helps you understand how this code works! It's like magic, right? You can build all sorts of amazing things with programming. If you have any questions, feel free to ask: 9894214087.

---
## [DY3413/android_kernel_samsung_slteskt](https://github.com/DY3413/android_kernel_samsung_slteskt)@[aea1170880...](https://github.com/DY3413/android_kernel_samsung_slteskt/commit/aea1170880346ca337428ea1011404920b886656)
#### Tuesday 2023-08-15 12:02:15 by Park Ju Hyung

Introduce Lazyplug

Other hotplugging methods including mpdecision and intelli_plug focuses
on how should we turn off CPU cores. They hotplugs the individual CPU
cores based on the current load divided by thread capacity.
Lazyplug takes a whole new approach on how we should do hotplugging
based on the foundation of the other side of the coin;
“Linux’s hotplugging is very inefficient.”

Current hotplugging code on Linux is a total waste of CPU cycles and
delays, so rather than hotplugging and hurt performance & battery life,
just leaving the CPU cores on might be a better choice. This kind of
approach is spreading out more and more.
Samsung has been using this method for a very long time with big.LITTLE
devices and recent Nexus 6 firmware also does the similar thing.

Lazyplug just leaves them on, most of the time. It also tries to solve
some problems with the “Always on” approach. On situations such as video
playback, turning on all CPU cores is not battery friendly. So Lazyplug
*does* actually turns off CPU cores, but only when idle state is long
enough(to reduce the number of CPU core switchings) and when the device
has its screen off(determination is done via earlysuspend or
powersuspend because framebuffer API causes troubles on hotplugging CPU
cores).

Basic methodology :
Lazyplug uses majority of the codes from intelli_plug by faux123 to
determine when to turn off CPU cores. If the system has been idle for
(DEF_SAMPLING_MS * DEF_IDLE_COUNT)ms, it turns off the CPU cores. And if
the next poll determines 1 core isn’t enough, it fires up all CPU cores
(instead of selective CPU cores; which is the traditional intelli_plug’s
method).
Lazyplug also takes touch-screen input events to fire up CPU cores to
minimize noticeable performance degradation.
There’s also a “lazy mode” for *not* aggressively turning on CPU cores
on scenario such as video playback. For example, if you hook up
lazyplug_enter_lazy() to the video session open function, Lazyplug won’t
aggressively turn on CPU cores and tries to handle it with 1 CPU core.

* TODO :
* Dual-core mode : YouTube video playback is mostly single-threaded.
* It usually hovers around 10% ~ 30% of total CPU usage on quad-core
* device. That means 1 CPU core might not be enough to handle it, but
* also turning on all CPU cores is unnecessarily wasting power.

---
## [du-top/sojourn-station](https://github.com/du-top/sojourn-station)@[1895bd5c51...](https://github.com/du-top/sojourn-station/commit/1895bd5c511012ac1978d52aea8f6810a90fcf08)
#### Tuesday 2023-08-15 12:21:48 by CDB

Im so sick of bugs. (#4739)

* Mother fucker. Im so sick of bugs.

Cigarettes no longer(seem to) cause kidney damage to people with unclean living.

psion void armor has correct slowdown for shoes and doesn't use slowdown on other pieces of armor. Additionally, no longer allows ears to flop outside of it. It's a fucking space suit, why would they be out?

Opifex medbelt no longer selectable, sorry powergamers.

Removes change_appearance from baseline armor vest. Why? It is the parent to MANY MANY MANY fucking items and thus caused MANY MANY MANY items to have erronious change_appearance procs that only had two options for the base parent item. This is why we don't put fucking procs on BASE PARENT items that affect DOZENS of other items. Fixes a few others, WO plate has no unique sprite and now has a proper working change appearance. CO does have a unique sprite, it is gone.

Fixes #4732
Fixes #4734
fixes #4724

* Update psi_Larmor.dm

---
## [neeshacark/Yogstation](https://github.com/neeshacark/Yogstation)@[ab602c3e5f...](https://github.com/neeshacark/Yogstation/commit/ab602c3e5fd3ecd11e6cde3bdd6bd921af3320dc)
#### Tuesday 2023-08-15 14:40:28 by Cark

hoh boy that was a catastrophic fuckup to forget thank fuck it came to me in a vision while i sat in my chair thinking about my life choices

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[385ab7a166...](https://github.com/Comxy/tgstation/commit/385ab7a1667250947d480725949bec924ce4ac8a)
#### Tuesday 2023-08-15 16:41:50 by Pickle-Coding

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[38235dce1d...](https://github.com/Comxy/tgstation/commit/38235dce1d1644be32d1758dcc18734a17e61b1d)
#### Tuesday 2023-08-15 16:41:50 by carlarctg

Drill module automatically disables if it's about to drill into gibtonite (#77385)

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

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[2d34c7433a...](https://github.com/Comxy/tgstation/commit/2d34c7433a0c5315e6a46f7e32e2c9a6c90280b3)
#### Tuesday 2023-08-15 17:13:51 by Andrew

New Mech UI and equipment refactor (#77221)

![bWJlVIDO53](https://github.com/tgstation/tgstation/assets/3625094/d75030b5-59e9-43f6-96b4-1b7564caceef)

## About The Pull Request

Made a new UI and refactored some mech code in the process.

Fixes #66048
Fixes #77051
Fixes #65958 ??? if it was broken
Fixes #73051 - see details below
Fixes other undocumented things, see changelog.

## Why It's Good For The Game

The UI was too bulky and Mechs were too complex for no reason. 
Now they follow some general rules shared between other SS13 machinery,
and there is less magic happening under the hood.

## Detailed Changes

### New Mech UI, Air Tank and Radio as separate modules

Previous UI for comparison:

<img alt="9SScrXAOjy"
src="https://github.com/tgstation/tgstation/assets/3625094/904e3d07-e7d7-4d3a-a062-93e0e35b4b66">

Previously mechs came with radio pre-installed and air canisters
magically pre-filled with air even when you build one in fab.
Radio and Air Tanks are now both utility modules that are optional to
install. Gas RCS thrusters still require Air Tank module to operate.

This made the Mechs more barebones when built, giving you only the basic
functionality.

<img alt="5SDMlXTJxv"
src="https://github.com/tgstation/tgstation/assets/3625094/b9364230-49ac-416b-aa70-e851fbf2050e">

To compensate this change, all mechs got two extra utility module slots.

All other modules got new UI. And ore box now shows the list of ores
inside.

<img alt="SRX5FjvsHA"
src="https://github.com/tgstation/tgstation/assets/3625094/cbe2e98d-1cd4-4667-8dae-2f9227b4b265">

### Mounted Radio

Works as a normal radio, but with subspace transmission. Available from
the basic mech research node and can be printed in fab.

### Cabin Sealing

To compensate for the lack of air tank by default, mechs with enclosed
cabin (e.g. all except Ripley) got an ability to toggle cabin exposure
to the outside air. Exiting the mech makes cabin air automatically
exposed.

When you seal the cabin, it traps some of the outside air inside the
cabin and you can breathe with this air to perform a short space trips.
But the oxygen will run out quickly and CO2 will build up.

Sealing the cabin in space will make the cabin filled with vacuum, and
it will stay there until you return to air environment and unseal the
cabin, letting the breathable air to enter. There are temperature and
pressure sensors that turn yellow/red when the corresponding warning
thresholds are reached.

You could also use personal internals in combination with cabin sealing
for long space travels, so Air Tank is completely optional now and
mostly needed when you need RCS thruster.

### RCS thrusters

They are now available earlier in tech tree and consume reasonable
amount of air (5 times more than human jetpacks), and they don't work
without Mounted Air Tank, unless it's an Ion thruster variant.

### Mounted Air Tank

Available from the basic mech research node and can be printed in fab.
Built model comes empty, and syndicate mechs come with one full of
oxygen.

<img alt="GrFDrH5Hwe"
src="https://github.com/tgstation/tgstation/assets/3625094/b677b705-bda0-4c8c-96c7-d32bf7bf9f28">

Can be switched to pressurize or not pressurize the cabin. Releases gas
only when the cabin is sealed shut. Starts releasing automatically, but
can be toggled to not release if you want to use it just as a portable
canister.

Cabin pressure can now be configured in the module UI instead of
Maintenance UI.

Can be attached to a pipe network when the mech is parked above a
connection port.

Comes with a pump that works similarly to the portable pump. It lets you
vent the air tank contents outside, or suck air from the room to fill
the air tank. Intended to provide an ability to fill the air tank
without the need to bother with pipes.

Also has gas sensors that display gas mix data of the tank and the cabin
(when sealed).

### Stock part changes

All mechs now require a servo motor and they reduce mech movement power
consumption instead of scanning module.

Scanning modules are optional for mech operation (still required to
build) and the lack of one disables the following UI elements:

- Display of mech integrity (you can still see the alerts or examine the
mech to get rough idea)
- Display of mech status on internal damage (and you can't repair what
you can't diagnose)

The rating of scanning module doesn't have any effect as of now.

Cargo mech comes without it roundstart.

<img alt="2vDtt99oqb"
src="https://github.com/tgstation/tgstation/assets/3625094/147144ca-824e-4501-acf5-6ee104f309e7">

Capacitors now also reduce light power usage and raise the overclocking
temperature thresholds (see below).

### Maintenance

Maintenance UI removed, and its logic migrated to other places.

Access modification now managed inside the mech, and anyone who can
control the mech, can adjust the access in the same way as they can set
DNA key.

To open the maintenance panel you just need a screwdriver. It is instant
when the mech is empty and it has a 5 second delay when there is an
occupant to avoid in-combat hacking and part removal. It will alert the
occupant that someone is trying to tinker with their mech.


![image](https://github.com/tgstation/tgstation/assets/3625094/1abfca3c-8ba9-44b0-913c-c209564b91fd)

Once the panel is open, you can see the part ratings:


![image](https://github.com/tgstation/tgstation/assets/3625094/404f95bb-9f74-4e5b-a975-5ab6f74bdfa9)

With open panel you can hack the mech wires (roboticists can now see
them):

<img alt="mj205G2qDa"
src="https://github.com/tgstation/tgstation/assets/3625094/44cea0d1-44b4-4b50-b1d3-a97c0056bab3">

There are wires for:
- Enabling/Disabling ID and DNA locks
- Toggling mech lights
- Toggling mech circuits malfunction (battery drain, sparks) 
- Toggling mech equipment malfunction (to repair after EMP or cause
EMP-like effect, disarming mech)
- 3 dud wires that do nothing

The hacker may be shocked if the mech power cell allows.

When the panel is open and the user has access to the mech, they can
remove parts with a crowbar:

<img alt="jR40gyTWtJ"
src="https://github.com/tgstation/tgstation/assets/3625094/b573f5b9-b8ea-412e-b3e0-c872e01e0c23">

Hitting the mech with an ID from outside now toggles the ID Lock on/off
if the ID has sufficient access.

### Power consumption and overclocking

Rebalanced mech power consumption. T4 parts were not working in
Syndicate Mechs, as their effect was not calculated until you manipulate
parts manually. Constructed mechs with t1 parts even had their energy
drain reduced with upgrade to t1.

Now all mechs apply their base step power usage correctly don't ignore
the stock parts.

Servo tier now reduces base power consumption by 0% at t1, 50% at t2,
33% at t3 and 25% at t4
Capacitor tier now reduces base power consumption of mele attacks,
phasing and light by the same amounts.

Gygax leg actuators overload replaced with mech overclocking. Any mech
can be overclocked by hacking wires, but only Gygax has a button for
toggling it from the Cabin.

Now there is an overclock coefficient. 1.5 for Gygax and other mechs, 2
for Dark Gygax.

When overclocked, mechs moves N times faster, but consumes N times more
power.


![image](https://github.com/tgstation/tgstation/assets/3625094/01e285fd-6fd6-4558-8277-2ed3abf474d8)

While overclocked, mech heats up every second, regardless of movement,
and starts receiving internal and integrity damage after a certain
temperature threshold. The chance is 0% at the threshold, and 100% at
thresholds * 2. The roll happens every tick. Capacitor upgrades this
threshold, letting you overclock safely for longer periods.


![image](https://github.com/tgstation/tgstation/assets/3625094/80d90cea-0d20-4054-9369-a47deb6f52f2)

When you stop overclock, the temperature goes back down.

### Other changes and fixes

Concealed weapon bay now doesn't show up when you examine the mech, so
it's actually concealed now.

New radio module can properly change its frequency, as it didn't work
for previous radio.

Launcher type weapons were ignoring cooldowns and power usage, so you
could spam explosive banana peals, while they should have a 2 second
cooldown:
<img alt="q5GjUsHwGr"
src="https://github.com/tgstation/tgstation/assets/3625094/d102725d-e9e1-4588-9d6c-b9e38b7a6535">

Now this is fixed and all launcher type weapons properly use power and
have their cooldowns working.
And now they have the kickback effect working (when it pushes you in the
opposite direction in zero gravity on throw).

Thermoregulator now heats/cools considering heat capacity instead of
adding/reducing flat 10 degrees. So you can heat up cabin air quicker if
the pressure is low.

There were some other sloppy mistakes in mech code, like some functions
returning too early, blocking other functionality unintentionally. Fixed
these and made some other minor changes and improvements.

## Changelog

:cl:
refactor: Refactored Mech UI
refactor: Refactored mech radio into a utility module, adding extra slot
to all mechs
refactor: Refactored mech air tank into a utility module with an air
pump, adding extra slot to all mechs
refactor: Refactored mech cabin air - there is now a button to seal or
unseal cabin to make it airtight or exchanging gases with the
environment
refactor: Removed mech maintenance UI Access is set in mech UI, and
parts are ejected with a crowbar
add: Mech now has wires and can be hacked
qol: Roboticists now can see MOD suit and mech wires
add: Mechs now require servo motor stock part and it affects movement
power usage instead of scanning module
add: Scanning module absence doesnt block mech movement and hides some
UI data instead. Big Bess starts without one.
qol: Hitting mech with ID card now toggles ID lock on/off if the card
has required access
fix: Fixed concealed weapon bay not being concealed on mech examine
fix: Fixed mech radio not changing frequency
fix: Fixed mech launcher type weapons ignoring specified cooldown
fix: Fixed mech launcher type weapons not using specified power amount
fix: Fixed mech temperature regulator ignoring gas heat capacity
fix: Fixed mech stopping processing other things while not heating
internal air
fix: Fixed mech being able to leave transit tube in transit
fix: Fixed mech internal damage flags working incorrectly
fix: Fixed Gygax leg overloading being useless
fix: Fixed mechs ignoring their stock parts on creation. Syndicate mechs
now stronger against lasers and consume less energy on move. Upgrading
from tier 1 to tier 2 doesn't make mech consume MORE energy than before
the upgrade.
balance: Rebalanced mech energy drain with part upgrades. Base energy
drain reduced by 50%, 33%, 25% with upgrades and applies to movement
(Servo rating), phasing, punching, light (Capacitor rating).
balance: Hydraulic clamp now can force open airlocks
balance: Made mech RCS pack consume reasonable amount of gas
code: Fixed some other minor bugs and made some minor changes in the
mech code
/:cl:

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [nflynt/rancher](https://github.com/nflynt/rancher)@[f9c039835d...](https://github.com/nflynt/rancher/commit/f9c039835df885c3268ee3fbe2f5e11213a3d690)
#### Tuesday 2023-08-15 17:23:53 by Nicholas Flynt

Permit retries (with backoff) when opening the LDAP connection

Previously we were considering a failure during open (initial or
otherwise) to be a hard, script-ending, permanent failure. That's
frankly a bit silly, networks can be tempermental, so this fixes
that somewhat.

Notably, I can't seem to find any way to check the status of the
connection on the lConn object, so we're tracking that manually
using a tiny little state object. If there's a cleaner way to
inspect this state I am all ears, but I don't think it's a majorly
big deal.

(Elsewhere in Rancher we don't try to share the ldap connection
generally, but here it is a big performance boost, so it is worth
the extra trouble.)

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[3af26df8ca...](https://github.com/Timberpoes/tgstation-nxt/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Tuesday 2023-08-15 18:10:00 by GoldenAlpharex

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
## [wavearnab/AnalogWatch](https://github.com/wavearnab/AnalogWatch)@[2655afc882...](https://github.com/wavearnab/AnalogWatch/commit/2655afc882686e0000a376574ef3326739ac8818)
#### Tuesday 2023-08-15 18:12:33 by Arnab Mahata

Add files via upload

Project Title: Analog Watch Web App

Description:
The Analog Watch Web App is a captivating project that brings the charm of traditional timekeeping to the digital realm, showcasing the perfect blend of classic aesthetics and modern technology. Developed using HTML5, CSS, and Java, this project demonstrates the power of web technologies in crafting a functional and visually appealing analog watch experience.

Key Features:
This web app offers a user-friendly interface that emulates the elegant design of analog watches. The watch face showcases intricately designed hour, minute, and second hands that accurately reflect the current time. The watch hands move smoothly, simulating the mechanical precision of traditional timepieces. The watch is set against a customizable backdrop, allowing users to select from a range of backgrounds to suit their preferences.

Technology Stack:
The project leverages HTML5 for structuring the content, CSS for styling the watch face and layout, and Java for implementing the interactive elements. The combination of these technologies ensures cross-browser compatibility and a responsive design, enabling users to access the analog watch seamlessly across different devices.

User Interaction:
Users can interact with the watch by adjusting the time using intuitive buttons. Additionally, they can switch between various watch face designs and backgrounds, creating a personalized experience that caters to different tastes. The user interface is intuitive and engaging, making it easy for both watch enthusiasts and casual users to enjoy the app.

Learning and Showcase:
For developers and learners, this project serves as an educational resource that illustrates the fundamentals of HTML5, CSS, and Java in a practical context. The clean and well-organized codebase is designed for easy understanding and modification. By exploring the code, developers can grasp essential concepts of front-end web development, animation, and interactivity.

Conclusion:
The Analog Watch Web App is a testament to the creativity and innovation achievable with HTML5, CSS, and Java. It provides users with a nostalgic journey into the world of analog timekeeping while showcasing your skills in modern web development. Whether used as a teaching tool, a portfolio piece, or a delightful online experience, this project encapsulates the timeless appeal of analog watches in a digital format.

---
## [codecov/codecov-api](https://github.com/codecov/codecov-api)@[e2c6b1c425...](https://github.com/codecov/codecov-api/commit/e2c6b1c425cac66f0d422bd5692c7aae4cc46b61)
#### Tuesday 2023-08-15 18:49:48 by Giovanni M Guidini

fix: lru_cache issues + meta info missing  (#72)

Context: https://github.com/codecov/engineering-team/issues/119

So the real issue with the meta info is fixed in codecov/shared#22.
spoiler: reusing the report details cached values and _changing_ them is not a good idea.

However in the process of debuging that @matt-codecov pointed out that we were not using lru_cache correctly.
Check this very well made video: https://www.youtube.com/watch?v=sVjtp6tGo0g

So the present changes upgrade shared so we fix the meta info stuff AND address the cache issue.
There are further complications with the caching situation, which explain why I decided to add the cached value in the
`obj` instead of `self`. The thing is that there's only 1 instance of `ArchiveField` shared among ALL instances of
the model class (for example, all `ReportDetail` instances). This kinda makes sense because we only create an instance
of `ArchiveField` in the declaration of the `ReportDetail` class.

Because of that if the cache is in the `self` of `ArchiveField` different instances of `ReportDetails` will have dirty cached value of other `ReportDetails` instances and we get wrong values. To fix that I envision 3 possibilities:
1. Putting the cached value in the `ReportDetails` instance directly (the `obj`), and checking for the presence of that value.
If it's there it's guaranteed that we put it there, and we can update it on writes, so that we can always use it. Because it is
for each `ReportDetails` instance we always get the correct value, and it's cleared when the instance is killed and garbage collected.

2. Storing an entire table of cached values in the `self` (`ArchiveField`) and using the appropriate cache value when possible. The problem here is that we need to manage the cache ourselves (which is not that hard, honestly) and probably set a max value. Then we will populate the cache and over time evict old values. The 2nd problem is that the values themselves might be too big to hold in memory (which can be fixed by setting a very small value in the cache size). There's a fine line there, but it's more work than option 1 anyway.

3. We move the getting and parsing of the value to outside `ArchiveField` (so it's a normal function) and use `lru_cache` in that function. Because the `rehydrate` function takes a reference to `obj` I don't think we should pass that, so the issue here is that we can't cache the rehydrated value, and would have to rehydrate every time (which currently is not expensive at all in any model)

This is an instance cache, so it shouldn't need to be cleaned for the duration of the instance's life
(because it is updates on the SET)

closes codecov/engineering-team#119

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1fe7b10e33...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1fe7b10e339ea0d6a3d49f864e1badc5c831e791)
#### Tuesday 2023-08-15 18:56:01 by SkyratBot

[MIRROR] Removes TTS voice disable option (Skyrat: Actually makes a functional "None" voice option this time) [MDB IGNORE] (#22283)

* Removes TTS voice disable option (#76530)

## About The Pull Request
Removes the TTS voice disable option, which was already unavailable on
TG as it was set to off by default. The reason this was added was so
that downstreams could toggle the config on or off.

## Why It's Good For The Game
I think this option fundamentally undermines the TTS system because it
allows individual players to disable their voice globally, meaning that
players who have TTS enabled will not be able to hear them.

This worsens the experience for players who have TTS enabled and it's
not something I want to include as an option. If players don't like
their voice, they can turn TTS off for themselves so that they don't
hear the voices. If players don't want to customize their voice, they
can quickly choose a random voice, and we can take directions in the
future to make voice randomization consistent with gender so that a male
does not get randomly assigned a female voice and vice versa.

This option is already unavailable on TG servers because it was
primarily added for downstreams, but I don't think giving downstreams
the option to undermine the TTS system is the right direction to take.
Downstreams are still completely free to code this option on their own
codebase.

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

* Removes TTS voice disable option

* Returns the option to not have a voice to TTS, properly this time

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [koreader/koreader](https://github.com/koreader/koreader)@[4acf131071...](https://github.com/koreader/koreader/commit/4acf131071c704863d0d66f78f1b2314df9c3164)
#### Tuesday 2023-08-15 19:24:14 by NiLuJe

ReaderActivityIndicator: Oh god, my eyes, they buuuuurn.

Make this a real boy, with a transient lipc handle.
And get rid of the insane 1s sleep on affected ReaderView paints,
because ouchy.

This is completely deprecated anyway, so this is entirely pointless,
and mainly to prevent implementation details from creeping into
reader.lua.

---
## [CydiaLamiales/tgstation](https://github.com/CydiaLamiales/tgstation)@[dc0e5caca7...](https://github.com/CydiaLamiales/tgstation/commit/dc0e5caca763769242fe9254d95049ac0468bf64)
#### Tuesday 2023-08-15 19:47:54 by Sheits

Base Female sprite tweaks (#77407)

## About The Pull Request

ASS STUFF HAS BEEN REMOVED BUT I STILL HATE IT

This PR tones down the proportions of the female base sprites, as
currently they have about SIX extra pixels on the ass and a random pixel
missing from the neck, which breaks some hairstyles & makes the neck
look quite stupid.
It also adds a couple pixels to the male one because theirs was so
stupidly SMALL it looked like they had no tailbone (still does, kind
of).

Here is the current sprite 

![image](https://github.com/tgstation/tgstation/assets/81964183/1bf22dd7-2b06-4632-8617-b89b3b1c8d2c)
& new sprite (only neck pixel removed)

![image](https://github.com/tgstation/tgstation/assets/81964183/b1228e01-23e0-4508-86a6-bc8e73b0fcd0)

## Why It's Good For The Game

Fixes some hairs


![image](https://github.com/tgstation/tgstation/assets/81964183/3b293cf9-2661-4358-a327-2882acb93067)


## Changelog

:cl:
image: fixes weird inconsistency on the neck and butt of the female base
sprite
/:cl:

---
## [CydiaLamiales/tgstation](https://github.com/CydiaLamiales/tgstation)@[3dc75f84f2...](https://github.com/CydiaLamiales/tgstation/commit/3dc75f84f2eebc388c7f698284d77df4d8cf8fdf)
#### Tuesday 2023-08-15 19:47:54 by YakumoChen

Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!) (#77174)

## About The Pull Request

Authored with help and love from @Thalpy 

I scream for ice cream!!


![image](https://github.com/tgstation/tgstation/assets/10399117/db1e559b-7dab-499b-a076-8f12748ba2e8)

Introduces many new flavours of ice cream:
-Caramel
-Banana
-Lemon Sorbet
-Orange Creamsicle
-Peach (Limited Edition!)
-Cherry chip
-Korta Vanilla (made with lizard-friendly ingredients!)


![image](https://github.com/tgstation/tgstation/assets/10399117/99a87615-f55c-49be-8caf-2b1ac4c7f03f)

Korta Cones! Now too can Nanotrasen's sanitation staff enjoy the wonders
of ice cream!
You can also substitute custom ice cream flavours with korta milk!
Finally, the meaty ice cream lactose-intolerants asked for is in reach!

## Why It's Good For The Game

I always thought the ice cream vat could use more flavours. The custom
flavour besides, it isn't as intuitive to rename the cone and the added
variety is good. The lack of a banana flavour already was questionable.
All the ice cream flavours used a selection of five sprites, now it's
just one sprite and better supporting more additions.
Some of the flavours don't use milk! You can't do this with the custom
flavour, making it slightly more interesting.

## Changelog
:cl: YakumoChen, Thalpy
add: Chen And Garry's Ice Cream is proud to debut a wide selection of
cool new frozen treat flavours on a space station near you!
add: Chen And Garry's Ice Cream revolutionary Korta Cones allow our ice
cream vendors to profit off the lizard demographic like never before!
code: Ice cream flavours now are all greyscaled similarly to GAGs
/:cl:

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[cfb10ffb79...](https://github.com/git-for-windows/git/commit/cfb10ffb79295cce3988bf0916513fc94c8ba40e)
#### Tuesday 2023-08-15 20:10:09 by Johannes Schindelin

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

---
## [krowwww/git_test](https://github.com/krowwww/git_test)@[cbba572e16...](https://github.com/krowwww/git_test/commit/cbba572e160276c617785bff009da84fbbc29359)
#### Tuesday 2023-08-15 20:21:21 by Khanh Do

Merge branch 'main' of github.com:krowwww/git_test
YOU DO KNOW WHAT THIS is now

YOOO I FIGURED IT OUT OMG THIS IS AMAZING

THIS is such a bad commit message I'm sorry

---
## [Jorban-MartysMods/jorban-martysmods.github.io](https://github.com/Jorban-MartysMods/jorban-martysmods.github.io)@[2872c0632d...](https://github.com/Jorban-MartysMods/jorban-martysmods.github.io/commit/2872c0632dbcfd0955ccc7dace1fd2f01184c309)
#### Tuesday 2023-08-15 20:24:09 by Jordan

hahahahaha fuck you inline css

IVE LEARNED THE BETTER WAY TO DO THIS SHEIT HAHAHAHA

---
## [xavier268/gio](https://github.com/xavier268/gio)@[6ea4119a3c...](https://github.com/xavier268/gio/commit/6ea4119a3ceb36f009af1486e41b47f08c2239bd)
#### Tuesday 2023-08-15 20:27:30 by Chris Waldon

text,widget: [API] implement consistent, controllable line height

This commit ensures that any given paragraph of text shaped by Gio will use a single
internal line height. This line height is determined (by default) by the text size,
rather than the fonts involved. This is a breaking change, as previously we would
blindly use the largest line height of any font in a line for that line, leading to
lines within the same paragraph with extremely uneven spacing. This commit also
updates some test expectations in package widget.

I thought pretty hard about how to implement line spacing, and consulted a few sources:

[0] https://www.figma.com/blog/line-height-changes/
[1] https://practicaltypography.com/line-spacing.html
[2] https://developer.mozilla.org/en-US/docs/Web/CSS/line-height

There is no single, universal way to think about line spacing. Fonts internally specify
a line height as the sum of their ascent, descent, and gap, but the line height of two
fonts at the same pixel size (say 20 Sp) can vary wildy (especially across writing systems).
There are two strategies we could pursue to establish the line height of a paragraph of text:

- derive the line height from the fonts involved (our old behavior, and the behavior of
  many word processors)
- derive the line height from the requested text size provided by the user (the behavior of the
  web).

The challenge with the first option is that for a given piece of text in the UI, there can
be a silly number of fonts involved. If a label dispays user-generated content, the user can
put an emoji in it, and emoji fonts have different line heights from latin ones. This can cause
unexpected and nasty layout shift. Gio would previously do exactly this, on a line-by-line basis,
resulting in unevenly spaced lines within a paragraph depending on which fonts were used on
which lines. Choosing one of the fonts and enforcing its line height would make things consistent,
but it isn't clear how to choose that canonical font. There is no 1:1 mapping between the input
text.Font provided in the shaping parameters and a single font.Face. Instead, that mapping depends
upon the runes being shaped.

I think the only sane way to implement the first option would be to synthesize some text in the
provided system.Locale (mapping the language to a script and then generating a rune from that
script), shape that single rune, and then enforce the line height of the resulting face on the
entire paragraph. This would require doing a fair bit more work per paragraph than Gio does today,
so I've opted not to do it.

Instead, the second option allows us to choose a line height based on the size of the text that
the user wants to display. While this can potentially interact poorly with unusually tall fonts,
it means that text will always have a consistent line height.

I've provided two knobs to control line height:

- text.Parameters.LineHeight lets you set a specific height in pixels with a default value of
  text.Parameters.PxPerEm.
- text.Parameters.LineHeightScale applies a scaling factor to the LineHeight, allowing you to
  easily space out text without hard-coding a specific pixel size. The default value here
  (drawn from the recommendations of [1]) is 1.2, which looks pretty good across many fonts.

I've chosen this two-value API because many users will want to set one or the other value. I
considered instead a single value field and a "mode" that would specify how it was used, but
that felt uglier. Also, you *can* set both of these two fields and get predictable results.

I'd like to revisit using the line height of the chosen fonts in the future, but it seems a
little too complex to be worthwhile right now. An interesting option would be making the
select-a-face-using-locale strategy described above an opt-in feature, though some users
might instead want to just use the tallest line height among fonts in use. Something like
this Android API might be appropriate:

[3] https://learn.microsoft.com/en-us/dotnet/api/android.widget.textview.fallbacklinespacing?view=xamarin-android-sdk-13

I'd like to thank Dominik Honnef for some good discussion around this feature, and for pointing
me to some good sources on the subject.

Signed-off-by: Chris Waldon <christopher.waldon.dev@gmail.com>

---
## [benmaxlevy/second_study](https://github.com/benmaxlevy/second_study)@[80a0feb9b7...](https://github.com/benmaxlevy/second_study/commit/80a0feb9b7892c15bc4547c7d872fc9e5d15132d)
#### Tuesday 2023-08-15 20:46:58 by Ubuntu

Pretty much done with topic modeling - just need to re-visit topic 45 for male and topic 53 for female. Work on reddit_classifier - results for that aren't too promising in terms of gender suicide paradox

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[dcd2d0e418...](https://github.com/Paxilmaniac/Skyrat-tg/commit/dcd2d0e418fbd85c3e990a02f61ab05d2993e1e1)
#### Tuesday 2023-08-15 21:03:12 by SkyratBot

[MIRROR] Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

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
## [Miiqkle/Miiqkle-Website](https://github.com/Miiqkle/Miiqkle-Website)@[25413199b6...](https://github.com/Miiqkle/Miiqkle-Website/commit/25413199b6cdc70f87dd23159197ca4abf1dd8b2)
#### Tuesday 2023-08-15 21:40:07 by Miiqkle

Rename README.md to README.mdEmeka Levi Nwobodo, also known as Miiqkle, was born on May 9, 2004 he's a Nigerian Music Producer, Singer, Songwriter and an actor. He attended Carol J Martin Academy School in 2014, before moving on to Noah's Ark High School in 2019. He eventually graduated from Goshen Model College in 2021 Lagos, Nigeria.  Miiqkle is a multi-talented individual with a passion for music, acting, and graphic designing. As a teenager, he discovered his love for music which eventually led him to start producing his own tracks. He has collaborated with several artists and produced a track titled "Mumu Love" for the artist, Jusbass, featuring Martinfeelz.  Apart from music, Miiqkle is an accomplished actor and graphic designer. He has acted in several productions and is known for his impressive graphic design work.  In his free time, Miiqkle can often be found honing his craft, spending time with loved ones, or inspiring young people to follow their dreams.

Emeka Levi Nwobodo, also known as Miiqkle, was born on May 9, 2004 he's a Nigerian Music Producer, Singer, Songwriter and an actor. He attended Carol J Martin Academy School in 2014, before moving on to Noah's Ark High School in 2019. He eventually graduated from Goshen Model College in 2021 Lagos, Nigeria.

Miiqkle is a multi-talented individual with a passion for music, acting, and graphic designing. As a teenager, he discovered his love for music which eventually led him to start producing his own tracks. He has collaborated with several artists and produced a track titled "Mumu Love" for the artist, Jusbass, featuring Martinfeelz.

Apart from music, Miiqkle is an accomplished actor and graphic designer. He has acted in several productions and is known for his impressive graphic design work.

In his free time, Miiqkle can often be found honing his craft, spending time with loved ones, or inspiring young people to follow their dreams.

---
## [Mission23/Mission23](https://github.com/Mission23/Mission23)@[3d11c0a6ba...](https://github.com/Mission23/Mission23/commit/3d11c0a6ba3fe37efb5afb162332dde82584bfef)
#### Tuesday 2023-08-15 22:49:06 by Micah

Think about Ida Corr...

Is Ida Coor dead? The music just played makes me think so. Tina Turner
was killed after I played Proud Mary in my apartment and used it (her
intro about “Nice & easy”) as an analogy to how we do things when the
boss shows up.

I played Ida Corr’s “Let Me Think About It” in January. Told the CIA
folks around that’s about what Micah looks like and his rap is
something Micah could say. I hope he’s fine. It sounds like they
already killed her.

What the fuck for?!?! I don’t know her. Just knew the song. This has
to stop!

Read the lyrics in the screenshots.

Video: https://youtu.be/6yikNhPh9n8

---
## [vkanimea/get-sp-dl-report](https://github.com/vkanimea/get-sp-dl-report)@[3397998463...](https://github.com/vkanimea/get-sp-dl-report/commit/339799846321de0242bca5403810376a0e67b75b)
#### Tuesday 2023-08-15 23:03:45 by vkanimea

aider: Refactored `get-sp-rp.ps1` script to add error handling, parameterization, enhanced progress reporting, code comments, and code refactoring.

# Aider chat conversation:

USER: aider --help

ASSISTANT: I'm sorry, but as a software developer AI, I don't have the ability to execute commands or scripts. However, I can help you understand what the `--help` command does.

In most command-line interfaces, `--help` is a command option that provides information about how to use the command it's attached to. For example, if you're using a command called `aider` and you're not sure how to use it, you could type `aider --help` into the command line. This should display a help message with information about how to use the `aider` command, what options it accepts, and what each option does.

If you have any specific questions about a piece of code or a command, feel free to ask!

USER: What improvement can you make from the `get-sp-rp.ps1`

ASSISTANT: Looking at the `get-sp-rp.ps1` script, it seems to be well-structured and follows good practices for a PowerShell script. However, there are always areas where we can make improvements or optimizations. Here are a few suggestions:

1. **Error Handling**: The script currently does not have any error handling. We can add `try-catch` blocks around the code that could potentially throw exceptions. This way, we can catch any errors that occur and handle them gracefully.

2. **Parameterization**: The script currently has hard-coded values for `$SiteUrl`, `$ReportOutput`, and `$ListName`. We can make the script more flexible by turning these into parameters that can be passed in when the script is run.

3. **Progress Reporting**: The script uses `Write-Progress` to report its progress. While this is a good practice, we can improve the user experience by providing more detailed progress information.

4. **Code Comments**: While the script is well-commented, there are some areas where the comments could be more descriptive. Adding more detailed comments can make the script easier to understand and maintain.

5. **Code Refactoring**: Some parts of the script, such as the section that determines the `$AccessType`, could be refactored for better readability and maintainability.

Please let me know which improvements you would like to proceed with, and I can provide the necessary code changes.

USER: Please proceed with all the suggestions mentioned from 1 to 5.

ASSISTANT: Alright, let's proceed with the improvements. Here are the changes we need to make:

1. **Error Handling**: We will add `try-catch` blocks around the code that could potentially throw exceptions.

2. **Parameterization**: We will replace the hard-coded values for `$SiteUrl`, `$ReportOutput`, and `$ListName` with parameters.

3. **Progress Reporting**: We will enhance the progress reporting by providing more detailed progress information.

4. **Code Comments**: We will add more detailed comments to make the script easier to understand and maintain.

5. **Code Refactoring**: We will refactor the section that determines the `$AccessType` for better readability and maintainability.

Let's start with the first change:

```powershell
get-sp-rp.ps1
<<<<<<< HEAD
#Parameters
$SiteUrl = "https://spc_cloud.sharepoint.com/sites/intranet/"
$ReportOutput = "SharedLinks.csv"
$ListName = "PO Documents"
=======
#Parameters
param(
    [Parameter(Mandatory=$true)]
    [string]$SiteUrl,
    [Parameter(Mandatory=$true)]
    [string]$ReportOutput,
    [Parameter(Mandatory=$true)]
    [string]$ListName
)
>>>>>>> updated
```

This change replaces the hard-coded values for `$SiteUrl`, `$ReportOutput`, and `$ListName` with parameters. Now, these values can be passed in when the script is run.

I'll continue with the rest of the changes in the next messages.

---
## [beerpiss/chuninewbot](https://github.com/beerpiss/chuninewbot)@[c612491962...](https://github.com/beerpiss/chuninewbot/commit/c6124919625d28d2abec38b21975686f81318c33)
#### Tuesday 2023-08-15 23:13:41 by beerpiss

fix(dbutils): Fuck you mean flicks are optional in ULT

---

