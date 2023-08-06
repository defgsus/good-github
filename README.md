## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-05](docs/good-messages/2023/2023-08-05.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,878,895 were push events containing 2,547,025 commit messages that amount to 142,536,601 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [greenhas/spg_website](https://github.com/greenhas/spg_website)@[242ad993a5...](https://github.com/greenhas/spg_website/commit/242ad993a5b5c58927e4e5347b0371c3199a5654)
#### Saturday 2023-08-05 00:12:26 by Spencer Greenhalgh

post We decided to stuff this weekend full (early anniversary dinner and movie, then visit to friends across the state, then family visit to water park) so naturally kiddo tested positive for COVID-19 tonight.

---
## [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)@[2733a5574f...](https://github.com/microsoft/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Saturday 2023-08-05 00:13:37 by Mark Karle

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
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[ef04f254d4...](https://github.com/newstools/2023-new-york-post/commit/ef04f254d49f7ba23f48351583c7a8bf50369299)
#### Saturday 2023-08-05 00:13:53 by Billy Einkamerer

Created Text For URL [nypost.com/2023/08/04/ariana-grandes-new-boyfriend-looks-like-her-brother-fans-say/]

---
## [ijjk/next.js](https://github.com/ijjk/next.js)@[e06880ea4c...](https://github.com/ijjk/next.js/commit/e06880ea4c061fc5c298b262d01f347edd8dce74)
#### Saturday 2023-08-05 00:39:01 by Josh Story

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
## [wuseman/TG799VAC-XTREME-17.2-MINT](https://github.com/wuseman/TG799VAC-XTREME-17.2-MINT)@[b9a03a45c5...](https://github.com/wuseman/TG799VAC-XTREME-17.2-MINT/commit/b9a03a45c5bfb5710f09d8639173195a0df431c8)
#### Saturday 2023-08-05 01:26:43 by wuseman

Updated the previously fixed part in the disclosure as an "end of this repo."

Thanks for your support everyone! Today is a new day filled with endless possibilities and opportunities. As I continue my journey in the world of development, I'm looking forward to meeting you all again in future projects and repositories. Your enthusiasm and collaboration have been invaluable, and I'm excited to see where our paths will cross next.

Always remember to embrace challenges with curiosity, stay passionate about learning, and enjoy the process of creating something meaningful. Let's keep pushing the boundaries of what we can achieve together and remember, never give up!

Regards, wuseman

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[ebbc45b161...](https://github.com/Derpguy3/tgstation/commit/ebbc45b1616c08d2dc0b6e6ce48258f68eefd46a)
#### Saturday 2023-08-05 02:04:31 by distributivgesetz

Improved PDA Direct Messenger (#75820)

## About The Pull Request

Fixes #76708, Closes #76729 (sorry Zephyr)

This PR expands the Direct Messenger UI, adding a chat screen for each
available messenger that you can find, and moving message sending over
to TGUI.

This chat screen includes a message log that displays messages sent by
you as well as messages received from the recipient. This gets rid of
the previous chat log, which just had all messages thrown together that
you received or have sent, in one big list.

Furthermore, all messaging is now done inside the UI. This kills all
TGUI popups you would ever need to send messages forever (except for
quick replies). Use the input bar on the bottom, press Enter or the Send
button, and it sends your message. Spam mode is now done in the UI too,
via a text field you can find in the contacts list.

Additionally, because I have a habit of blowing things massively out of
scope, I've also completely refactored how messages and chat logs are
stored in the PDA messenger. I plan on using this in a PR that merges
the chat client with the messenger, sometime in the future. Sorry this
took so long.

Stuff left to do before I open this PR for review:
- [x] Add "recent messages"
- [x] Add "unread messages"
- [x] Add message drafts
- [x] Make photo sending not shit
- [x] Implement the edge cases for automated and rigged messages
- [x] Make sure shit isn't fucked
- [x] Profit

<details>
  <summary>Screenshots</summary>
  

![dreamseeker_HIrEfrap5X](https://github.com/tgstation/tgstation/assets/47710522/97c713b7-dda3-44d3-a8f5-d0ec11c92668)

![qIOWhVld4l](https://github.com/tgstation/tgstation/assets/47710522/3ab4e2c1-a38f-4b20-8e9f-509ea14c0434)

![dreamseeker_LIqwi05i4O](https://github.com/tgstation/tgstation/assets/47710522/c051c791-b595-4166-a4d3-82cb7568411f)

![BIYxNVjGL7](https://github.com/tgstation/tgstation/assets/47710522/b9c97eab-52b5-449f-b00f-a0d8aa5f865c)

![dreamseeker_IWdoSsUinC](https://github.com/tgstation/tgstation/assets/47710522/2a4cd76a-2bdc-4283-b642-09e92476fef5)

![L9DxzFHDEF](https://github.com/tgstation/tgstation/assets/47710522/6a5b0e29-d535-4c7e-a88e-e9b71198719b)

![rAuDgqBLNE](https://github.com/tgstation/tgstation/assets/47710522/128a0291-91da-4f9e-9bc5-a65cf411ea6d)

![dreamseeker_voui6S8MUf](https://github.com/tgstation/tgstation/assets/47710522/6e3ba044-b8df-492d-b58d-6c73ab07233d)

![image](https://github.com/tgstation/tgstation/assets/47710522/522c1d85-b9cf-4e0e-9588-9d3993eea03f)

</details>

## Why It's Good For The Game

The UI has largely stayed the same since modular tablets were added a
year ago. Even better, direct messaging has been the same since PDAs
were first added *more than a decade ago*. Imagine that.

Now we finally actually (!) make use of those brand new features that we
got from the TGUI switch in this regard.
## Changelog
:cl: distributivgesetz
add: Updated Direct Messenger to v6.5.3. Now including brand new
individual chat rooms, proper image attachments and a revolutionary
message input field!
add: Added a "Reset Imprint" option to the PDA painter.
refactor: Refactored PDA imprinting code just a bit.
fix: PDAs should now properly respond to rigged messages.
/:cl:

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[a288abcaf2...](https://github.com/Derpguy3/tgstation/commit/a288abcaf2a6b6c44edade8265a66b9ba3f0e67b)
#### Saturday 2023-08-05 02:04:31 by san7890

Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#77309)

## About The Pull Request

Servers are crashing on every round restart and I have absolutely no
idea where to start, but I noticed this so I figure I'll throw up a PR
to fix it.

This is the runtime (only found in dd.log, sorry non-admin/maintainer
gamers
https://[tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log](https://tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log)
)

```txt
[00:07:07] Runtime in code/modules/logging/log_holder.dm,166: Attempted to call shutdown_logging twice!
  proc name: shutdown logging (/datum/log_holder/proc/shutdown_logging)
  src: /datum/log_holder (/datum/log_holder)
  call stack:
  /datum/log_holder (/datum/log_holder): shutdown logging()
  shutdown logging()
  world: Reboot(0, 0)
  Ticker (/datum/controller/subsystem/ticker): Reboot("Round ended.", "proper completion", 600)
```

This is the full log:


![image](https://github.com/tgstation/tgstation/assets/34697715/af938235-3076-41d5-98b2-02907dedb6d5)

This is the code:


![image](https://github.com/tgstation/tgstation/assets/34697715/371b11cb-3bc9-4a99-a17c-73968ded308d)

For some reason, even though we invoke `TGSEndProcess`, we still
continue on in this `if()` chain. I don't know why we keep executing DM
code after TGS is supposed to be shut down (which may be why no one has
ever included a `return` here, but let's be safe instead of sorry.

If you really want to investigate why TGS is running DM code after we
end the process, I am amenable to including a stack trace or crash of
this phenomenon instead.
## Why It's Good For The Game

Since we aren't invoking `LOG_CLOSE_ALL` to rust-g twice (which seems to
be really unwanted per the code I read), hopefully thing no crash?
Rust-g had two breaking changes (one with logs, and one with SQL), so
I'm presuming that this might be related to the log one (which is why we
didn't see this sorta thing happen pre-#77307)... Worst case scenario
less runtimes in the funny runtime log.

I hope this wasn't loadbearing either... Likely requires testmerging
since TGS and I don't get along on my machine.
## Changelog
:cl:
server: Added a preventative measure to prevent calling both
TGSHardRestart and TGSReboot, as well as potentially invoking sensitive
procs that are only meant to be called once.
/:cl:

TL;DR- I do not definitively know why servers are crashing but I noticed
this runtime so I'll put out this open flame while I have the time to do
so.

---
## [PhantornRU/Skyrat-SS220](https://github.com/PhantornRU/Skyrat-SS220)@[2f2ec4b9d6...](https://github.com/PhantornRU/Skyrat-SS220/commit/2f2ec4b9d64c448e5b544ecbcdca42a7dae0f094)
#### Saturday 2023-08-05 02:05:02 by SkyratBot

[MIRROR] There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

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
## [CliffracerX/Skyraptor-SS13](https://github.com/CliffracerX/Skyraptor-SS13)@[8e3dfc2af2...](https://github.com/CliffracerX/Skyraptor-SS13/commit/8e3dfc2af2f3ca87e9f07669033c1ec2a6102073)
#### Saturday 2023-08-05 03:23:59 by GoldenAlpharex

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
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[2d0b4f053f...](https://github.com/necromanceranne/tgstation/commit/2d0b4f053f1db70d9f3ab6548f58b7928f159eaf)
#### Saturday 2023-08-05 03:28:28 by san7890

Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

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

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[69827604c4...](https://github.com/necromanceranne/tgstation/commit/69827604c46952dd4393db8617cd494ade17bea2)
#### Saturday 2023-08-05 03:28:28 by Watermelon914

Improves the RPG loot wizard event. (#77218)

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

Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [kokizzu/sorbet](https://github.com/kokizzu/sorbet)@[6a1084aa55...](https://github.com/kokizzu/sorbet/commit/6a1084aa558fbf334ccb605e40f347c6fa7f5069)
#### Saturday 2023-08-05 04:30:52 by Jake Zimmerman

Factor some common code (#7202)

* Factor some common code

I was seeing some crashes that arise because we were desugaring `begin;
end` to `EmptyTree`.

That's super annoying when it happens, because EmptyTree is the only
node in Sorbet's AST that doesn't have a loc (it doesn't have a loc so
that we can manage to allocate only one of them and share it across all
trees).

Which honestly, is kind of dumb these days anyways? Because the
EmptyTree will get inlined into the pointer, so it's not like we're
actually allocating memory for the EmptyTree. We're just clinging to our
old habits.

Anyways, `Kwbegin` is `begin; end` while `Begin` is `( )` (because of
course `x = ()` is valid Ruby). Their implementations in desugar were
identical, except that `()` desugared to `Nil` instead of `EmptyTree`,
and thus got a loc. That's the behavior I want, so I factored out a
helper and used it in both places.

(Maybe in a future change change I'll make it so that EmptyTree is no
longer shared globally, but that's a problem for some other day.)

* Update exp files

* Remove this error

Sorbet infers the type as `NilClass` now.

---
## [sonicdcer/sotn-decomp](https://github.com/sonicdcer/sotn-decomp)@[b488191654...](https://github.com/sonicdcer/sotn-decomp/commit/b488191654aef67226d141568be5104b78ea4ea7)
#### Saturday 2023-08-05 04:57:28 by bismurphy

Decompile DRA func_800FE044 (#407)

This function is responsible for upgrading the player's stats. This is
called upon collection of a Life Max Up, Heart Max Up, or when killing
an enemy to get experience. This function gives experience to the player
and their active familiar.

HUGE thanks to @mkst for the maspsx update that allowed this one to
match!

The arguments to this function are a little unusual. arg0 is mostly used
as the amount to increase the heartMax, hpmax, or exp, but in the case
where we're getting a relic, is used as the relic ID. Similarly, arg1 is
mostly used to identify which of these traits is being increased, but in
the case where we're getting exp, is used to define the enemy's level to
determine how much exp to award. It seems odd that increasing each of
these stats is baked into this one function, instead of all being their
own functions.

This is one of the first functions I looked at when I joined the decomp
several months ago and it's very cool to have it finally working, now
using the extra knowledge I've picked up over that time.

---------

Co-authored-by: bismurphy <bismurphy@users.noreply.github.com>
Co-authored-by: Mark Street <streetster@gmail.com>

---
## [EvaEvaEvaEvaEva/shaptest](https://github.com/EvaEvaEvaEvaEva/shaptest)@[ee4021c507...](https://github.com/EvaEvaEvaEvaEva/shaptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Saturday 2023-08-05 05:04:46 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[f5784dabc7...](https://github.com/ihatethisengine/cmss13/commit/f5784dabc77752802da20f2d14787667161d61ac)
#### Saturday 2023-08-05 06:04:14 by ihatethisengine

More portable cades tweaks and buffs (#3967)

# About the pull request

Despite making a lot of tweaks and changes to portable cades I barely
touched them in the game until recently. Now I have more experience and
can tweak it again.

1) You can now stack damaged cades and stack stores health of each cade.
You can repair stacked cades but it will take longer time.

2) Miniengi pamphlet allows faster repairs but only when cade is folded.

3) You can quickly collapse portable cades with crowbar if you have at
least miniengi skills.

4) You no longer need to have folded portable cade in hand in order to
repair it, but if you do, you can move while repairing.

# Explain why it's good for the game

1) It's extremely annoying to repair each individual cade in order to
stack them just because it got hit by a stray bullet once. Now you can
just ignore damage and keep going.

2) Yeah it took 10 second for PFC to repair each single cade. Really
long. Now it's 5 seconds, but only when folded and if you have miniengi
skills. Makes miniengi pamphlet a bit more relevant.

3) It was intended, but turned out it was a bit inconvenient. It was
faster to collapse by hand because you didn't need to deal with tools.
Now it requires just a crowbar and slightly faster. Also requires
miniengi skill to use crowbar.

4) First was just a bit annoying, second allows more mobility which is
the point of portable barricades.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: you can stack scratched portable cades if their HP at least
75%. Doing so will reduce the health of all barricades in the stack to
the level of the most damaged.
balance: you can repair stacked portable cades but it will take longer
time depending on how many cades in stack.
balance: miniengi skill makes repairs of folded portable cades faster
(10 seconds to 5 seconds, same as engineer).
balance: with engineering skill at least of miniengi you can collapse
deployed portable barricade with a crowbar (wrench is no longer
required, slightly faster (2 sec to 1.5 sec)).
balance: you no longer need to have folded portable cade in hand in
order to repair it.
balance: if you have folded portable cade in hand, you can move while
repairing it.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [lilypond/lilypond](https://github.com/lilypond/lilypond)@[36161db800...](https://github.com/lilypond/lilypond/commit/36161db80089ee75b27f8def40a1af0c5ef0af23)
#### Saturday 2023-08-05 07:35:19 by Jonas Hahnfeld

Remove validation link from website

Having these links and icons was a fashion some years ago, but that
seems to have mostly faded. And the placement on our website looks
quite ugly (in my opinion). Moreover, HTML 4.01 Transitional is not
the latest and greatest anymore, long live HTML 5!

Funnily enough, the added div actually introduces an error since commit
1edb8b3c85 removed the opening paragraph in the hosting_thanks that is
still closed after the validator link. As far as I can tell, it is the
only validation error...

---
## [2002jai/GPT-Model](https://github.com/2002jai/GPT-Model)@[21f46fa5dc...](https://github.com/2002jai/GPT-Model/commit/21f46fa5dcdbb0f818dd28b0aee5d35ea2e89b7b)
#### Saturday 2023-08-05 08:49:42 by jai chauhan

GPT Model

Welcome to the "GPT-3 Model Exploration" GitHub repository! This comprehensive repository is dedicated to helping you delve into the world of GPT-3, a revolutionary language model developed by OpenAI. GPT-3, short for Generative Pre-trained Transformer 3, has garnered widespread attention for its extraordinary capabilities in natural language processing.

In this repository, we provide in-depth documentation, code examples, and interactive Jupyter notebooks to guide you through understanding and leveraging GPT-3's full potential. Learn how to interact with GPT-3 using the OpenAI API, enabling you to perform text generation, question-answering, translation, and more.

Our step-by-step tutorials will also walk you through the process of fine-tuning GPT-3 for custom tasks, making it a powerful tool for a wide range of natural language understanding applications. Whether you're a beginner or an experienced practitioner, this repository aims to facilitate your journey into the realm of GPT-3.

However, it's essential to remember that this repository is intended for educational and research purposes only. For commercial usage or any deployment in production environments, please adhere to OpenAI's guidelines and usage policies.

Feel free to contribute, enhance, and explore GPT-3's capabilities with the community's support. Together, let's unlock the potential of GPT-3 and revolutionize the way we interact with natural language. Happy exploring!

---
## [flarialmc/launcher](https://github.com/flarialmc/launcher)@[f549ef04f2...](https://github.com/flarialmc/launcher/commit/f549ef04f26c737c78d934c7c818dcc88eb19297)
#### Saturday 2023-08-05 09:22:27 by that one lad

Bari will you suck my dick after this

I hate melvin he works for ashanki now anyways,
- version manager officially fixed, your welcome.
-  A lot of input lag and fps optimizers (dont blame me if it doesnt work)
- developer mode fixy
- oh ye vsync disabler (launcher automatically disables vsync)

---
## [saujix/My.Web_Scraping.Projects](https://github.com/saujix/My.Web_Scraping.Projects)@[1632151517...](https://github.com/saujix/My.Web_Scraping.Projects/commit/16321515176e820ece94709ff55445b7647cdd6f)
#### Saturday 2023-08-05 10:26:40 by the_black_digger

Add files via upload

this scraper logs into your account
then downloads the target's picture
make sure that the target profile is public
......either way this is kinda useless.........
i hate my life for making this, now i cant even access insta :(

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f0dc574c37...](https://github.com/tgstation/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Saturday 2023-08-05 12:04:15 by carlarctg

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
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[27d46f1717...](https://github.com/Sealed101/tgstation/commit/27d46f17173034b805d6ef064d4db31c7e34b26d)
#### Saturday 2023-08-05 13:18:28 by OrionTheFox

Science Resprite! (With Sovl!) (#77314)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
What a crusty department. These outfits are...
Something.

![image](https://github.com/tgstation/tgstation/assets/76465278/63fe13cf-bcbf-42c2-a22c-c868ae49a72c)

How old are these now? I'm pretty sure they're unchanged since when I
started playing years ago on other servers.... besides the RD Turtleneck
and Roboticist suit of course. But they still did have some touch-ups to
be made...

Regardless, I think this department deserves a little love!
I've tried to stay true as I could to their current designs; this isn't
a re-**_design_**, just a re-sprite. I used the base jumpsuit design
from Medbay for most of these since it's the most modern suit that fit
with the colored-spots style.

![image](https://github.com/tgstation/tgstation/assets/76465278/ef7ff5b0-f0e3-481a-9ed4-ba830e3ee0c3)

All of them have been touched up, and the RD's "alt" is now a subtype of
the buttondown so it can easily inherit any sprite updates in the
future.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
These deserved some touch-ups and modernization, and while I'm not keen
on entirely reworking them I figured I could at the least give them the
update the Science Team deserves.

(The buttondown has an outdated obj sprite in this image! It's since
been made smaller and more folded)
Also labcoats for comparison

![dreamseeker_Ds8gZLKoGE](https://github.com/tgstation/tgstation/assets/76465278/4da60512-b813-4260-b3fe-5c71b60cec81)

![dreamseeker_C9DpFWWOS7](https://github.com/tgstation/tgstation/assets/76465278/1de55f4c-2eaa-480b-811f-aaa5832eeceb)

![dreamseeker_02d3d7b6aj](https://github.com/tgstation/tgstation/assets/76465278/b1f40d03-c9b8-4f6b-bc54-516b11a7bfb3)

![dreamseeker_DwJGDwbUf1](https://github.com/tgstation/tgstation/assets/76465278/20f97a5e-42ab-4fe0-8eae-4ac6ed24ead4)


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
image: resprited the entirety of RnD! Genetics, Robotics, the RD, and
the Science Team themselves will enjoy the fresh new looks but same
great taste! No, wait, great STYLE! Don't eat these, they're covered in
chemicals.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Realife-Brahmin/MultiPeriod-DistOPF](https://github.com/Realife-Brahmin/MultiPeriod-DistOPF)@[531bc5e4aa...](https://github.com/Realife-Brahmin/MultiPeriod-DistOPF/commit/531bc5e4aaba0d623c9e206f2468e2a52babf4ab)
#### Saturday 2023-08-05 13:37:46 by Aryan Ritwajeet Jha

Will deal with this plotting shit tomorrow.

Is ~black magic~ metaprogramming evil? Tune in tomorrow to find out.

---
## [donvito007/Xiaomi_sm8250_N0Kernel](https://github.com/donvito007/Xiaomi_sm8250_N0Kernel)@[c1c783981e...](https://github.com/donvito007/Xiaomi_sm8250_N0Kernel/commit/c1c783981e86e1367332f6e546a6177cb057413b)
#### Saturday 2023-08-05 14:02:21 by Peter Zijlstra

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
## [SZL0056/Spacetime-pixel-dungeon](https://github.com/SZL0056/Spacetime-pixel-dungeon)@[8eac732143...](https://github.com/SZL0056/Spacetime-pixel-dungeon/commit/8eac732143112dba4b42346b50376abd759e4e0b)
#### Saturday 2023-08-05 14:06:07 by CODE0056

Update to 1.0.1demo,include a little improvement.

1.修复了许多Bug
2.完善了一些道具:
例如撬棍的撬锁功能
3.加入了一些以后会用到的东西:
(1)老版本女猎手的回旋镖
(2)圣骑士幽灵
(3)异端巨魔骑士(未完善)
4.加入了法师的惩戒牧师转职(未完善)
5..加入了盗贼的忍者转职(未完善)
6.投掷武器类的合成配方:
两个相同的投掷武器和一些液金，合成一个升级过的投掷武器
7.加入了克苏鲁偶像雕像:
带着它在地牢里探险会发生一些你意想不到的事情
8.加入了开锁器:
可以打开水晶门或是水晶箱子
9.加入怪物，仇恨元素:
与烈焰元素一样，属于元素类。在死亡后爆炸，有概率掉落复仇卷轴

目前依然是测试版本，所以还没有调整开局的道具，实际改动以中文说明为准。

1. Fixed many bugs

2. Improved some items:

For example, the lock picking function of the crowbar

3. Add some things you'll need later:

(1) The old Huntress's boomerang

(2) Paladin Ghost

(3) Heresy Troll Knight (incomplete)

4. Added the Master's Disciplinary pastor transfer (incomplete)

5.. Ninja transfer with Rogue (incomplete)

6. Synthetic formula for throwing weapons:

Two identical throwing weapons and some liquid gold combine to create an upgraded throwing weapon

7. Added a Cthulhu idol statue:

Exploring the dungeons with it will do some unexpected things

8. Added lock picker:

You can open crystal doors or crystal chests

9. Add monsters and hate elements:

Like the flame element, it belongs to the element class. When it explodes after death, it has a chance to drop the Revenge scroll

At present, it is still the test version, so the props of the opening have not been adjusted. The actual changes are subject to the Chinese instructions.

---
## [TacRP-EX-Creators-Club/tacrp-ak](https://github.com/TacRP-EX-Creators-Club/tacrp-ak)@[169ace0089...](https://github.com/TacRP-EX-Creators-Club/tacrp-ak/commit/169ace00891df19aaec3364cbe83b1175155cff7)
#### Saturday 2023-08-05 15:58:56 by Jayrazer

sorry i fucking suck and keep forgetting everything

---
## [fmhy/FMHYedit](https://github.com/fmhy/FMHYedit)@[cc29e0dee0...](https://github.com/fmhy/FMHYedit/commit/cc29e0dee03dd27ca52c5ece1c229f1276ab843e)
#### Saturday 2023-08-05 16:31:35 by Q

Update STORAGE.md

* ⭐ **[r0.ru](https://r0.ru/)** 
* ⭐ **[Mail.ru](https://mail.ru/)**
- Russian search engines, should be re-tested and moved to non eng Russian section

* ⭐ **[Baidu](https://www.baidu.com/)** - [PHP Version](https://github.com/yuantuo666/baiduwp-php) - Chinese search engine, should be re-tested and moved to non eng Chinese section 

https://www.harmari.com/harmari-search/ - "HARMARI SEARCH IS *NOT FREE AND RESTRICTED TO LAW ENFORCEMENT AND GOVERNMENT AGENCIES*", signup required and requires pretty much all personal information possible

[llarryyllarryy's Search Engine](https://llarryyllarryy.github.io/Max-Impact-Search/) - Just uses default Ecosia search results

[dogpile](https://www.dogpile.com/) - probably country specific since it doesn't allow access to a bunch of locations, needs to be checked which country it allows access to and added to that countries section in non eng

[Goodshop](https://www.goodshop.com/) - isn't a search engine

[Instya](https://www.instya.com/) - PaidMediaHeckYeah search engine :), is useless for the wiki and also in the general sense since search doesn't work

[Impersonal.me](https://ambition.dk/impersonal/) - Danish site, doesn't appear to be a search engine, should be tested and if it's worth anything added to the impoverished danish section of non eng

[oscobo](https://www.oscobo.com/) - has the front page which makes me regret turning off dark reader and only uses the default google search results

[Petal Search](https://petalsearch.com/) - dead

[seekport](https://www.seekport.com/) - search, and language change is broken

[search.tl](http://www.search.tl/) - redirects to http://www.amidalla.de/ which, besides UI war crimes, also has broken search because the server is under "high load". Sure.

[Surf Canyon](http://www.surfcanyon.com/) - instead of showing search results, it shows double search bar. yeh idk anymore

[Entfer](https://entfer.com/) - this was probably added ages ago and is still in non functional preview mode.

[Fagan Finder](https://www.faganfinder.com/) - duplicate, already listed once under starred search engines

 [Goofram](http://www.goofram.com/) - on one side you have the lawful good, generic google search results, and on the other you have AI search results that are the equivalent of asking a person high on LSD, meth, weed, and ecstasy to brainstorm something. It identifies "ass" as species on default :')

 [MyAllSearch](http://www.myallsearch.com/) - broken search, having a clean UI for a search engine is a struggle, etc etc you know the drill

 [iZito](https://www.izito.com/), [ZapMeta](https://www.zapmeta.com/) - the result of "sure bro you can copy my homework just change up a few things". I don't know who copied who here, but neither of them provide anything useful or unique, so I say remove em both

 [WorldWideScience](https://worldwidescience.org/) - dead

---
## [pritamdas98/p3343](https://github.com/pritamdas98/p3343)@[97821350e8...](https://github.com/pritamdas98/p3343/commit/97821350e8f6fbfa5e3eb335dab2a57dd82e641d)
#### Saturday 2023-08-05 16:37:31 by pritam das

Update README.md

I am a passionate and dedicated software engineer with a strong foundation in computer science and technology. With a Diploma in Computer Science & Technology from Camellia Institute of Polytechnic and currently pursuing a B.Tech in Computer Science & Engineering from Guru Nanak Institute of Technology, I am equipped with both theoretical knowledge and practical skills.

Throughout my educational journey, I have gained expertise in various programming languages such as C, Java, HTML,CSS ,JAVA-SCRIPT, Python. I am also well-versed in libraries/frameworks like JavaScript and have hands-on experience with tools/platforms like VS Code, PyCharm, Dev C++, Anaconda Additionally, I have a solid understanding of databases including DBMS, SQL, Query, and MySQL.

During my internship and job preparation at Internshala, I honed my technical skills and gained valuable industry exposure. I believe in continuous learning and strive for a little progress every day, knowing that it adds up to significant results over time.

One of my notable projects is the "Image Quality Analysis," where I delved into the differences between images required for computer vision and human perception. I developed a vision system for quality control purposes, emphasizing defect detection rather than aesthetics. This project showcased my ability to work with system components like lighting, lens, camera, and software to achieve specific objectives.

Another significant project I worked on is an "Online Social Networking Site Using Java." Leveraging technologies such as Servlet, JSP, and MySQL, I created a web application that allows users to interact and socialize virtually. Similar to popular social media platforms, users can make friends, post videos, share images, and engage in various activities.

To supplement my practical skills, I have acquired certifications in Python programming from Techno Exponent, SQL basics from HackerRank, Cyber Security from Coursera, web development training from Internshala, and completed "The Fundamentals of Digital Marketing" course through Google Digital Unlocked.

In recognition of my academic and professional achievements, I have received honors and awards, including distinction honors and honorable mentions. These accolades reflect my commitment to excellence and continuous growth in the field of software engineering.

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[8de9ad250a...](https://github.com/cheesePizza2/Foundation-19/commit/8de9ad250ad057d1b24aa81f449ff32c26816cd7)
#### Saturday 2023-08-05 16:38:17 by cheesePizza2

Fixes contraband detectors (whooooooooooops) (#1228)

* whooooooooooooooooops

* fixes for my fixes

* fuck you

* qdel(announce)

* QDEL_NULL

---------

Co-authored-by: TheDarkElites <73414180+TheDarkElites@users.noreply.github.com>

---
## [wesoda25/tgstation](https://github.com/wesoda25/tgstation)@[d85e44c69c...](https://github.com/wesoda25/tgstation/commit/d85e44c69cc06dbeeb3a0de7f76273de45ee3893)
#### Saturday 2023-08-05 16:55:48 by ChungusGamer666

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

## About The Pull Request

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

## Why It's Good For The Game

Bugs are bad they make you mad

## Changelog

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[beb98e0665...](https://github.com/treckstar/yolo-octo-hipster/commit/beb98e0665f8053e889fafd2339ecce2db300007)
#### Saturday 2023-08-05 18:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [mpjovanovich/illustmath_snippets](https://github.com/mpjovanovich/illustmath_snippets)@[15e7ff5813...](https://github.com/mpjovanovich/illustmath_snippets/commit/15e7ff5813aa860820f7f73a7f0e37ec48d9101c)
#### Saturday 2023-08-05 19:10:18 by Mike Jovanovich

jupyter sucks. seriously. it's so bad. I hate my life right now

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[cc57581b73...](https://github.com/nikothedude/tgstation/commit/cc57581b73e2979d775dfd9408978e4987b6635b)
#### Saturday 2023-08-05 19:11:31 by Sealed101

Dog wit the butter (feat. a bunch of dog-related code improvements) (#77039)

## About The Pull Request
Adds a `dog_fashion` for the stick of butter.(screenshot is outdated as
Lisa won't have butter no more)
![butter
dawgs](https://github.com/tgstation/tgstation/assets/75863639/a22e702c-98a8-4283-abd9-28d4a9fb3bd0)

Also cleans up dog.dm because it was SHIT and FUCK and MY FUCKING GOD
TWO INITIALIZE()s TWO TIMES IN A SINGLE FILE WHAT IN THE GODDAMN

Most noticeably, Lisa properly won't wear any hats, and puppies properly
can't wear head/back items (by just removing those item slots from the
strip/equip menu. if some admeme wants to fumble around they may still
equip shit there. but otherwise for a normal player those slots are
inaccessible).
Basic mobs now also send signals when they run
`appear_dead`/`appear_alive` procs, which corgis hook into to update
their dead fashion overlays.
The side-effect of getting that to work is that dogs (and any basic mob
that uses `play_dead` ai behavior) are so good at feigning death, that
they fool medical HUDs and other related things. They're just that good.
There's a bunch of other things involved and I was mostly just being
angry at the state of the file so I'll check back when I gather all
things changed.


![strippy](https://github.com/tgstation/tgstation/assets/75863639/ec4d17a2-d4df-401c-bd1f-7c4ee1b95671)


## Why It's Good For The Game


https://github.com/tgstation/tgstation/assets/75863639/b34589cb-94d6-4b80-bf0f-1814c08da100



## Changelog
:cl:
add: dog with a butter on 'em
add: dead dog with da butter on 'em (dogs feigning death are so good at
it, they appear dead to medical HUDs and other things)
add: Nars-Ian now can revive from the dead if he consumes a pet
fix: fixes dog fashion items with no speech modifiers set making dressed
up corgis unable to perform their speech or emote behaviors
fix: fixes old Ian losing his mobility ride when shaved with a razor
fix: fixes pets not dropping their collar when gibbed
fix: butter don't go on Lisa and corgi puppies (Lisa won't wear hats and
corgi puppies can't wear hats and back slot items)
/:cl:

---
## [Polybui92/Polybui92](https://github.com/Polybui92/Polybui92)@[5fb717e577...](https://github.com/Polybui92/Polybui92/commit/5fb717e57701db13c037d39dd7bb3243dc449697)
#### Saturday 2023-08-05 20:15:19 by Polybui92

Update README.md

I am writing to express my strong interest in the Inventory Control Data Analyst position at [Company Name], as advertised. With over two years of extensive experience in inventory control data analysis, a profound understanding of information systems, and a wide array of technical skills, I am confident I can contribute significantly to your team and its objectives.

During my tenure at CSAT Solution, I have successfully managed and evaluated the inventory control process, promptly identifying and resolving potential issues. I have conducted daily cycle counts, audited material movement processes, and provided trend analysis and insight to drive process improvements. My familiarity with Microsoft Team, SharePoint, SAP, GP, DELL REAL TIME, JAGUAR, and ERP systems has enabled me to streamline operations and ensure accurate inventory management.

I have a proven track record of troubleshooting and diagnosing data quality issues, offering valuable insights, and implementing practical solutions. My proficiency in SQL, Data Analysis, HTML,  Power BI Tableau, and Python has enabled me to perform in-depth analyses, contributing to strategic decision-making. Additionally, my ability to manage competing priorities and lead a team in a fast-paced environment was showcased when I showed my team to achieve the highest inventory check score by the RSM team in 2022.

One of my notable achievements was completing two significant improvements in the inventory control process for 2 building through the difference tracking data in daily reports based on the weekly report of 48 weeks and  2 years from 2020  to 2021 and 2021 to 2022.

Success in using in-depth data analysis tools has helped the inventory control team to provide data insight to reduce the risk of discrepancies between actual inventory when compared With SAP systems of Apple and Dell customers.

Demonstrating my commitment to delivering exceptional results. My educational background includes a Data Analytics AAS Degree from Lone Star College and studies in Business Administration at the Industrial University of Ho Chi Minh City.

I am excited to apply my skills and experience to [Company Name] and contribute to its continued success. I am confident that my exceptional inventory control data analysis knowledge, technical proficiency, and leadership capabilities make me a strong fit for this role.


Thank you for considering my application. I look forward to discussing how my background aligns with your needs in greater detail.

Sincerely,

Poly Bui

---
## [GPeckman/tgstation](https://github.com/GPeckman/tgstation)@[7e1d97af9e...](https://github.com/GPeckman/tgstation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Saturday 2023-08-05 21:28:27 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [GPeckman/tgstation](https://github.com/GPeckman/tgstation)@[0d769e0ffa...](https://github.com/GPeckman/tgstation/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Saturday 2023-08-05 21:28:27 by Jacquerel

Removes two redundant components (#76866)

## About The Pull Request

We're starting to get to have enough components that people don't
realise that what they want already exists but doesn't have the name
they expect 🙃

I recently added `track_hierarchical_movement` which is similar enough
to `connect_containers` that it shouldn't independently exist, even if I
like sending a new signal more than the ugly setup pattern for
`connect_loc`.

`trait_loc` is actually older than `give_turf_traits` but
`give_turf_traits` covers more edge cases than `turf_loc` so seems like
the better one to maintain.
HOWEVER `give_turf_traits` held a list of references to atoms in it,
which isn't great in an element. I couldn't think of a way to completely
eliminate the list, but it isn't a list of references any more so it
shouldn't cause any hard deletions.

## Why It's Good For The Game

Having two components which do the same thing but marginally differently
is confusing and going to cause us trouble down the line.

## Changelog

Not player facing

---
## [seeess/Defcon-Tor-31-Badge](https://github.com/seeess/Defcon-Tor-31-Badge)@[9be900c5db...](https://github.com/seeess/Defcon-Tor-31-Badge/commit/9be900c5dbaec74af55feaeeaed8215e9bf748c5)
#### Saturday 2023-08-05 21:53:55 by seeess

Do What The Fuck You Want To License

Do What The Fuck You Want To License

---
## [lbnesquik/TerraGov-Marine-Corps](https://github.com/lbnesquik/TerraGov-Marine-Corps)@[fb4899d20e...](https://github.com/lbnesquik/TerraGov-Marine-Corps/commit/fb4899d20e990a0a65b8cb5b0ad19b1ef9ab083e)
#### Saturday 2023-08-05 22:19:17 by KM-Catman

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
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[5c4b13863f...](https://github.com/Zonespace27/cmss13/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Saturday 2023-08-05 22:40:43 by ihatethisengine

Larva surge is limited by marines/xenos ratio (#3592)

# About the pull request

Xenos after hijack now get larva based on marines/xenos ratio. Instead
of infinite larva, larva surge will try to increase the initial amount
of xenos on hijack to 50% of marines forces over time (with a minimum of
5 larvas, if xenos already have good numbers).

# Explain why it's good for the game

Initially, if I remember correctly, larva surge was brought into the
game to discourage marines from early meta-evacuations, which is fair.
But consequently, it really hurt the hijack sequence. Even if marines
evac fair and square, larva surge still comes in action and makes
situation for marines even worse, utterly discouraging everything but
either boomrushing the Alamo or holding lifeboats to evac.

This resulted in hijacks being very repetitive and boring. More than
that, larva surge is extremely busted on lowpop due to the fact you can
get around 20 xenos from nothing, making lowpop hijack even less
interesting. So with this change marines will still get punished for
evaccing with good numbers, but won't be penalized as much for honest
evacuations.

So hopefully, we will see more variety of hijacks and more interesting
stories!

P.S. if you have a better formula, let me know.


# Testing Photographs and Procedure
<details>
My friend @Diegoflores31 tested this for me, thanks!
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: larva surge is limited by marines/xenos ratio
fix: xenos no longer get free larva from abandoned facehuggers during
hijack
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: fira <loyauflorian@gmail.com>

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[255ef2c778...](https://github.com/ARF-SS13/coyote-bayou/commit/255ef2c77853b41581d072fe7aafad3e700b30a6)
#### Saturday 2023-08-05 22:54:02 by Tk420634

Merge pull request #2737 from Superlagg/you-know-what-fuck-you-(bitflags-your-item-slots)

fixes ID timer and mistyped box slot

---
## [mietek/mame](https://github.com/mietek/mame)@[6db28f4041...](https://github.com/mietek/mame/commit/6db28f40416aa72a75128537e29b20985c26c75d)
#### Saturday 2023-08-05 23:45:58 by A-Noid33

New working software list items (mac - macii) 123 dumps (#11432)

* Initial softlist for mac moof 400/800 floppy disks

* Added mac moof software list support

New working software list items (123 working dumps)
-------------------------------
mac_flop_orig:

Lode Runner (version 1.0) [4AM, Anoid]
Balance of Power (version 1.03) [4AM, Anoid]
Shanghai (version 1.0) [4AM, Anoid]
Skyfox [4AM, Anoid]
Temple of Apshai Trilogy [4AM, Anoid]
The Surgeon (version 1.5) [4AM, Anoid]
Uninvited [4AM, Anoid]
King's Quest (version 1.10) [4AM, Anoid]
Smash Hit Racquetball (version 1.01) [4AM, Anoid]
The Ancient Art of War [4AM, Anoid]
Hacker II [4AM, Anoid]
Rambo: First Blood Part II [4AM, Anoid]
One on One [4AM, Anoid]
Indiana Jones and the Revenge of the Ancients [4AM, Anoid]
Winter Games (version 1985-10-24) [4AM, Anoid]
Winter Games (version 1985-10-31) [4AM, Anoid]
Star Trek: The Kobayashi Alternative (version 1.0) [4AM, Anoid]
Mac Attack [4AM, Anoid]
GATO (version 1.3) [4AM, Anoid]
Dark Castle (version 1.0) [4AM, Anoid]
Oids (version 1.4) [4AM, Anoid]
MacWars [4AM, Anoid]
Shadowgate [4AM, Anoid]
Seven Cities of Gold [4AM, Anoid]
Enchanted Scepters [4AM, Anoid]
Beyond Dark Castle [4AM, Anoid]
Arkanoid (version 1.00) [4AM, Anoid]
The Chessmaster 2000 (version 1.02) [4AM, Anoid]
Maze Survival [4AM, Anoid]
Frogger (version 1.0) [4AM, Anoid]
SimCity (version 1.2, black & white) [4AM, Anoid]
Falcon (version 1.0) [4AM, Anoid]
Cutthroats (release 23 / 840809-C) [4AM, Anoid]
The Witness (release 22 / 840924-C) [4AM, Anoid]
Seastalker (release 15 / 840522-C) [4AM, Anoid]
Zork III (release 17 / 840727-C) [4AM, Anoid]
A Mind Forever Voyaging (release 77 / 850814-E) [4AM, Anoid]
Hollywood Hijinx (release 37 / 861215-I) [4AM, Anoid]
Nord and Bert Couldn't Make Head or Tail of It (release 19 / 870722-I) [4AM, Anoid]
Border Zone (release 9 / 881008-3B) [4AM, Anoid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914) [4AM, Anoid]
Zork I: The Great Underground Empire (release 76 / 840509) [4AM, Anoid]
Deadline (release 27 / 831005-C) [4AM, Anoid]
Infidel (release 22 / 840522-C) [4AM, Anoid]
Suspect (release 14 / 841005-C) [4AM, Anoid]
Planetfall (release 29 / 840118-B) [4AM, Anoid]
Ballyhoo (release 97 / 851218-G) [4AM, Anoid]
Enchanter (release 24 / 851118-G) [4AM, Anoid]
Spellbreaker (release 63 / 850916-F) [4AM, Anoid]
Trinity (release 11 / 860509-3H) [4AM, Anoid]
Stationfall (release 107 / 870430-G) [4AM, Anoid]
The Lurking Horror (release 203 / 870506-G) [4AM, Anoid]
Alter Ego (male version 1.0) [4AM, Anoid]
Alter Ego (version 1.1 female) [4AM, Anoid]
The Print Shop (version 1.2) [4AM, Anoid]
Flight Simulator (version 1.02) [4AM, Anoid]
Run for the Money [4AM, Anoid]
Master Tracks Pro (version 4.0) [4AM, Anoid]
Where in Time is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Deluxe Music Construction Set (version 1.0) [4AM, Anoid]
Apache Strike (version 1.2) [4AM, Anoid]
Wizardry VI: Bane of the Cosmic Forge [4AM, Anoid]
Harrier Strike Mission [4AM, Anoid]
Airborne! [4AM, Anoid]
Mac Vegas (version 1.1) [4AM, Anoid]
Dragonworld [4AM, Anoid]
MacDraft (version 1.2) [4AM, Anoid]
The Mind Prober (version 1.0) [4AM, Anoid]
The Toy Shop (version 1.1) [4AM, Anoid]
Strategic Conquest (version 1.2) [4AM, Anoid]
The Home Accountant (version 1.01) [4AM, Anoid]
Sub Battle Simulator [4AM, Anoid]
Vegas Video Poker [4AM, Anoid]
The Pawn (version 2.3) [4AM, Anoid]
Downhill Racer [4AM, Anoid]
Dollars and Sense (version 1.3) [4AM, Anoid]
Alternate Reality: The City (version 3.0) [4AM, Anoid]
Borrowed Time [4AM, Anoid]
The Quest [4AM, Anoid]
The Crimson Crown [4AM, Anoid]
Mindshadow [4AM, Anoid]
Pensate (version 1.1) [4AM, Anoid]
Sierra Championship Boxing [4AM, Anoid]
Championship Star League Baseball [4AM, Anoid]
Forbidden Castle [4AM, Anoid]
Defender of the Crown [4AM, Anoid]
The King of Chicago [4AM, Anoid]
Macintosh Pascal (version 1.0) [4AM, Anoid]
Fusillade [4AM, Anoid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) [4AM, Anoid]
Speed Reader II (version 1.1) [4AM, Anoid]
][ in a Mac (version 2.03) [4AM, Anoid]
Q-Sheet (version 1.0) [4AM, Anoid]
Fontographer (version 2.4.1) [4AM, Anoid]
Mouse Stampede (version 1.00) [4AM, Anoid]
The Mist [4AM, Anoid]
Tass Times in Tonetown [4AM, Anoid]
Pinball Construction Set [4AM, Anoid]
Transylvania [4AM, Anoid]
Déjà Vu: A Nightmare Comes True!! [4AM, Anoid]
Déjà Vu II: Lost in Las Vegas!! [4AM, Anoid]
Rogue (version 1.0) [4AM, Anoid]
Bridge (version 6.0) [4AM, Anoid]
Harrier Strike Mission II (version 1.2) [4AM, Anoid]
Patton vs. Rommel (version 1.05) [4AM, Anoid]
Moebius: The Orb of Celestial Harmony (version 1.03) [4AM, Anoid]
Tesserae (version 1.06) [4AM, Anoid]
Where in Europe is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Shufflepuck Cafe (version 1.0) [4AM, Anoid]
Geometry (version 1.1) [4AM, Anoid]
Physics (version 1.2) [4AM, Anoid]
SimCity (version 1.1) [4AM, Anoid]
Murder by the Dozen [4AM, Anoid]
The Duel: Test Drive II [4AM, Anoid]
Master Tracks Pro (version 1.10) [4AM, Anoid]
Master Tracks Pro (version 2.00h) [4AM, Anoid]
Master Tracks Pro (version 3.4a) [4AM, Anoid]
Squire (version 1.1) [4AM, Anoid]
Millionaire (version 1.0) [4AM, Anoid]
Microsoft File (version 1.04) [4AM, Anoid]
Microsoft Excel (version 1.00) [4AM, Anoid]
The Fool's Errand (version 2.0) [4AM, Anoid]
MacGammon! (version 1.0) [4AM, Anoid]

---------

Co-authored-by: Bob Schultz <bobschultz03@gamil.com>

---

