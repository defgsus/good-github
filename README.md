## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-08](docs/good-messages/2023/2023-08-08.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,318,559 were push events containing 3,453,377 commit messages that amount to 272,273,566 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 69 messages:


## [git-for-windows/git](https://github.com/git-for-windows/git)@[edacbb7a55...](https://github.com/git-for-windows/git/commit/edacbb7a5558a566451a2ff3a9c2488e254c6d4d)
#### Tuesday 2023-08-08 00:18:31 by Johannes Schindelin

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
## [ZainCheung/next.js](https://github.com/ZainCheung/next.js)@[e06880ea4c...](https://github.com/ZainCheung/next.js/commit/e06880ea4c061fc5c298b262d01f347edd8dce74)
#### Tuesday 2023-08-08 00:22:06 by Josh Story

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
## [ktxyz/stuff](https://github.com/ktxyz/stuff)@[7be505d325...](https://github.com/ktxyz/stuff/commit/7be505d325a7feb1b4ae8f2ca42906da1bbdcf38)
#### Tuesday 2023-08-08 00:29:45 by Kamil Tokarski

MagicCompare from codewars - kinda cool kinda annoying

---
## [meedan/check-api](https://github.com/meedan/check-api)@[dc890de6e2...](https://github.com/meedan/check-api/commit/dc890de6e23208a4db9e99f8e28e665b8ffc8a7e)
#### Tuesday 2023-08-08 00:31:37 by Christa Hartsock

Update GraphQL to use class-based SDK 🫠

This commit upgrades us to GraphQL 1.11.10, from 1.9.21, and begins using the new class-based SDK from the previous .define syntax.Though this change isn't supposed to be required until GraphQL 2.0, I found in practice that we couldn't upgrade to the minimum version needed for Ruby 3.0 (1.11.7) without doing it. 

**What I did**

With the new GraphQL DSL, we are able to use Ruby class composition, which includes inheritance from base classes and including modules to get specific functionality.

I tried to create some useful abstract base classes that borrowed heavily from our previous GraphQL CRUD generator. We had a lot of carveouts in the generator for specific classes (specifically in .define_parent_returns or the generator functions for what wanted to be classes), and I tried to eliminate these and move them to explicit declarations in classes now that we have the ability to do that (yay library enabling composition!)

As much as possible, I tried to move us toward declaring things explicitly to reduce my and hopefully future us's confusion rather than using metaprogramming or extracting abstract functions. Going forward, I think we should only extract methods or classes where there is shared functionality for a type or mutation, and rely on explicit declaration or modules for attributes that differ based on the underlying class we're modifying.

There is some kind of tricky metaprogramming and code in the mutation base classes, because of problems I ran into with inheritance and other things. I also hope that now that the pattern is set up we won't have to touch them too much, and can instead rely on configuring their child classes.

**Some gotchas I ran into / things of note**

Our API uses a mix of camel-case and snake-case. The new GraphQL library wants to convert everything to camelcase, which will break our API. I've tried where possible to default attributes to snakecase (changing this in the base Type), but it's not possible for everything - specifically when we set fields and arguments on mutation classes. To override the default behavior of camelcaseing, we have to manually set camelize: false on any field or argument that has an underscore in mutation classes.

* GraphQL Ruby now has a new base mutation class that we could opt into if we want, but it changes the way the API would look - of note is removing the input: key from request bodies, not allowing direct setting of inputs and fields on the input type in the mutation class (I think), and not automatically injecting the global ID in the response. To maintain our old behavior, we have to descend from GraphQL::Schema::RelayClassicMutation rather than GraphQL::Schema::Mutation, which I've done in Mutations::BaseMutation (and all descendent classes we expect to use for our mutations: Mutations::CreateMutation, Mutations::UpdateMutation, Mutations::DestroyMutation, Mutations::BulkUpdateMutation, Mutations::BulkDestroyMutation)
* GraphQL schema now gets generated at runtime. When our tests run they only start the application a maximum of once per file. This means that the previous approach we used to create and delete annotation types, which the GraphQL schema relies on to be generated correctly, and reloading the schema as necessary does not work - as a result we're now calling  TestDynamicAnnotationTables.load! before GraphQL controller tests, which loads the existing annotation tables generated in development into test fresh each time.
* Our QueryType returns an always null ID field. This is because the frontend was requesting it even though we don't use it. I don't know why, but this fixed it. So, I added it and moved on.

Resources:

Here's the migration guide I leaned on heavily: https://imaharu.github.io/graphql-ruby-doc-ja/schema/class_based_api.html#compatibility--migration-overview. It's still missing a lot, but may help if you want to understand changes in the API.

Also, the new API is described in the GraphQL ruby docs: https://graphql-ruby.org/guides

**Some additional things that appear in this commit, that may be of note in future**

* Manually specify resolve functions for missing methods

We sometimes automatically generate getters for attributes stored
as a hash (eg get_slack_webhook, get_languages) but since we rely
on method_missing to do so, GraphQL doesn't detect those methods as
being valid because it checks for their validity using
Model.respond_to(:method_name), which returns false even though
Model.method_name returns a legitimate value. To get around this,
we can manually create resolve methods with the attribute name
that just call into the model.

* Allow batch nesting

This is now allowed in GraphQL batch, and the error we were previously
catching no longer exists.

https://github.com/Shopify/graphql-batch/issues/70

* Properly implement nodes and interfaces, and support OpenStructs

OpenStructs break the class hierarchy, so we need more explicit
handling to support our current use case. Our id_from_object now
calls down into the OpenStruct :type method, like we were doing before

* Fix edge setting in most mutation classes

I think there was a naming conflict (name -> obj_name) causing things
to go totally wonky.

* Fix tests that depend on a specific schema

Certain tests require annotation types to be in the database before loading
the schema. We can't reload the schema easily in test environment. Given that this
data is actually static in practice (and hardcoded into the GraphQL schema we
generate), we might want to consider preloading it into the database rather than
creating it in individual tests. For now, we just create the dynamic annotations in
the test setup for the controller test file the test is run within.

Try to avoid altering the other tests for now, even though we'll need
to eventually. Begins loading in DynamicAnnotation stuff from a dump
of our local (and QA) database after a fresh build so that we can have
a consistent GraphQL schema. The new GraphQL interpreter only creates the
schema at runtime, which means we build it once per test run. As a result,
we need to have all of our DynamicAnnotation annotation types and fields
in place before we start the app to run tests.

This sidesteps fixing the dynamic annotation stuff for the rest of the
app, since that's a big one.

* Change flaking tests to use createDynamic instead of db-gen mutation

Also adds :action to Dynamic mutations to support using createDynamic
for createDynamicReportDesign, which requires the action attribute
in certain circumstances. Kind of a hack for tests to pass, since we're
having problems loading the schema from database consistently

CV2-3094

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[dc0e5caca7...](https://github.com/MrMelbert/tgstation/commit/dc0e5caca763769242fe9254d95049ac0468bf64)
#### Tuesday 2023-08-08 01:05:06 by Sheits

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
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[3dc75f84f2...](https://github.com/MrMelbert/tgstation/commit/3dc75f84f2eebc388c7f698284d77df4d8cf8fdf)
#### Tuesday 2023-08-08 01:05:06 by YakumoChen

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
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[b6b00df15c...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/b6b00df15ca8fe5458b81e655496f872718d7449)
#### Tuesday 2023-08-08 01:16:44 by carlarctg

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
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[e80cf8f358...](https://github.com/Wallemations/heavenstation/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Tuesday 2023-08-08 01:21:47 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [senicluxus/A3_Theseus](https://github.com/senicluxus/A3_Theseus)@[7853ecddcf...](https://github.com/senicluxus/A3_Theseus/commit/7853ecddcf92abd65bc6ad97bddc27b343239b1f)
#### Tuesday 2023-08-08 01:25:19 by Senicluxus

INTERPOL - TF1814 Activation

I swear in the name of truth and justice, before the Supreme Being, to guard, by sacrificing my own life, and suffering the hardest toils, the mystery, which shall be explained to me and that I shall respond with the truth whatever I am asked.

---
## [TheObserver-sys/Citadel-Station-13-RP](https://github.com/TheObserver-sys/Citadel-Station-13-RP)@[1468797059...](https://github.com/TheObserver-sys/Citadel-Station-13-RP/commit/146879705978b0416739823fa54467e865c3ffb2)
#### Tuesday 2023-08-08 01:34:02 by TheObserver-sys

Take 2: Some fixes and QoL (#5601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Would you believe me if I hadn't updated my git in about 400 years, and
had to blow the old version of my repo up?
Yes? No? It doesn't matter.

Anyways! Meat and potatoes of this:
Allows players to make gene and plant discs freely in the protolathe.
Since we do not have a dedicated genetics, this will help the pains of
actually doing genetics by giving us storage solutions for genes.

Fixes a problem with brass also creating slag when compressing, by
setting the copper alloy flag to 1.

And finally: Allows you to upgrade the braces! If your brace has T3 or
better, a single brace can hold an entire drill. All credit goes to
Hatterhat for this one, as I pretty much wholesale ripped it from his
buff of the big drill™ on Virgo.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not making slag is ALWAYS good. It saves on material, too.
Having more discs for a cheap cost is also good, it means you can reduce
headaches while scoping out for genes, because there are many, and the
ability to track them are currently few.
And honestly, the less lugging a person has to do with the mining drill,
the more likely people might stop blowing up an already unstable planet
with miniature hydrogen bombs.
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

:cl: The0bserver
add: Discs are able to be produced in the protolathe now. Go nuts, or
don't. I'm not your guardian.
balance: Mining Drills can finally be operated with just one brace with
the requisite parts. Thank you, Hatterhat!
fix: Copper no longer smelts slag when set to "Alloying."
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: TheObserver-sys <Gizmomaster777@gmail.com>

---
## [ogbigboss/a-new-false-hope](https://github.com/ogbigboss/a-new-false-hope)@[57d9f43341...](https://github.com/ogbigboss/a-new-false-hope/commit/57d9f43341f8a24d594169395bdc64e9f228feb5)
#### Tuesday 2023-08-08 01:58:24 by ogbigboss

by the way, YES, I thought about a hyphenated last name being mine. And yes, Mallik was second in my fantasy. Shit, I'd drop the name but it's funnier to keep at this point. Anyway a boy remains dreaming etc etc

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[1895bd5c51...](https://github.com/sojourn-13/sojourn-station/commit/1895bd5c511012ac1978d52aea8f6810a90fcf08)
#### Tuesday 2023-08-08 02:17:31 by CDB

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
## [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)@[2733a5574f...](https://github.com/microsoft/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Tuesday 2023-08-08 03:15:20 by Mark Karle

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
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[40df076b36...](https://github.com/ss220club/Skyrat-tg/commit/40df076b365a221ef25c8ff5049633354fbafd37)
#### Tuesday 2023-08-08 03:18:34 by SkyratBot

[MIRROR] Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks [MDB IGNORE] (#22919)

* Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks (#77393)

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

* Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks

---------

Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[f3fc60ed65...](https://github.com/cmss13-devs/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Tuesday 2023-08-08 03:19:44 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---
## [DHDAXCW/kernel](https://github.com/DHDAXCW/kernel)@[d0f788b8fa...](https://github.com/DHDAXCW/kernel/commit/d0f788b8fab24197232a6753c3f556ee0cc9d039)
#### Tuesday 2023-08-08 03:56:27 by Greg Kroah-Hartman

ANDROID: struct io_uring ABI preservation hack for 5.10.162 changes

In the 5.10.162 release, the io_uring code was synced with the version
that is in the 5.15.y kernel tree in order to resolve a huge number of
potential, and known, problems with the codebase.  This makes for a more
secure and easier-to-update-and-maintain 5.10.y kernel tree, so this is
a great thing, however this caused some issues when it comes to the
Android KABI preservation and checking tools.

A number of the io_uring structures get used in other core kernel
structures, only as "opaque" pointers, so there is not any real ABI
breakage.  But, due to the visibility of the structures going away, the
CRC values of many scheduler variables and functions were changed.

In order to preserve the CRC values, to prevent all device kernels to be
forced to rebuild for no reason whatsoever from a functional point of
view, we need to keep around the "old" io_uring structures for the CRC
calculation only.  This is done by the following definitions of struct
io_identity and struct io_uring_task which will only be visible when the
CRC calculation build happens, not in any functional kernel build.

Yes, this all is a horrible hack, and these really are not the true
structures that any code uses, but so life is in the world of stable
apis.

Bug: 161946584
Bug: 268174392
Fixes: 788d0824269b ("io_uring: import 5.15-stable io_uring")
Signed-off-by: Greg Kroah-Hartman <gregkh@google.com>
Change-Id: I2294f220ae78fe9aa32ee25b81829ae765e9deb2

---
## [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud)@[1636f51119...](https://github.com/ubicloud/ubicloud/commit/1636f511193699655c863c40204d585d454debe3)
#### Tuesday 2023-08-08 03:56:37 by Daniel Farina

Switch product names to standard-(cores*2) notation

Why cores * 2? Because SMT features, as seen on Intel and AMD products
for some year now make this equal to the number of "CPUs" or "vCPUs"
when exposed to the guest operating system.

The theory is that an integer in the product code will be compared to
vCPU references similar products on various data tables and so forth
on The Internet, or more to the point, shouldn't be a smaller integer
than those references for the same hardware.  Note, I do not subscribe
to theory's assigned magnitude of this, and have my objections to what
it does to the cogency of product comparison as written below, but
nonetheless, I've written this operating under this theory.

The ugliness arrives when we consider SMT-off configurations or
relatively recent addition of ARM processors that do not implement
SMT.  If the product scale factor was taken to describe vCPUs, we'd
end up the situation that GCP and Azure are in: t2d.standard-1 and
t2a.standard-1 are one vCPU in SMT-off configuration, and thus a
single core, and most directly comperable to n2d.standard-2.  The
customer is left the job of being SMT-aware and scaling the model
names.

Azure did something rather strange to deal with this, where a
"Standard_E2" is 2 vCPUs on one core via SMT and 16 gigabytes of
memory, but "Standard_E2p" on ARM is 2 cores and 16 gigabytes of
memory, a more compute-rich ratio by quite a bit.

One solution, absent indexing the product by cores directly, which
produces an integer that could be misconstrued and deemed too small,
is to double the core number in all circumstances.  The idea of a
popular architecture with three or more threads per core seems
unlikely at this point, and in any case it'd be an emergent
architecture where we could be forgiven for an awkward numbering
system.  And it solves the problem for allowing someone to scan
laterally from "standard-2" and a hypothetical "standard-2-arm".  Even
if standard-2-arm has a single core.

Of course, there's nothing stopping us from deciding to really make
the product scale factor relate to vCPUs, that is, to have integers of
larger magnitudes for architectures with SMT, and maybe if people do
prove to be uniformly alert about SMT and find `standard-2-arm`
misleading, we can elect to do things that way.

If it were up to me, I'd index the model numbers on cores, and in
addition to cleaning all that up, would also attain the aesthetically
pleasing "standard-1".

---
## [10to22/CC](https://github.com/10to22/CC)@[e08c0f5abd...](https://github.com/10to22/CC/commit/e08c0f5abd5c5ae16d82131cf32e753a4e15b89c)
#### Tuesday 2023-08-08 04:01:53 by 10to22

Update and rename fuck you textbox.html to Index.html

---
## [newstools/2023-daily-post-nigeria](https://github.com/newstools/2023-daily-post-nigeria)@[0cd36c7a97...](https://github.com/newstools/2023-daily-post-nigeria/commit/0cd36c7a9711812f68382aa9a9ea8e2dbf204fe3)
#### Tuesday 2023-08-08 05:45:07 by Billy Einkamerer

Created Text For URL [dailypost.ng/2023/08/07/i-once-borrowed-money-to-impress-my-girlfriend-singer-boy-spyce/]

---
## [jalenng/Draw](https://github.com/jalenng/Draw)@[f286df5ff3...](https://github.com/jalenng/Draw/commit/f286df5ff3f2ffd3501f5e716df7acf7c0de8665)
#### Tuesday 2023-08-08 07:21:08 by spicywheatbread

Add files for SFX (#39)

* Basic SFX Added

Added placeholder sound effects to things like jumping and dying.

(cherry picked from commit e721f5ff4a91ac3e89c323e4e900a352f9b02ebf)

* More SFX

Added new page flip sound, added sounds to return buttons in menus, more work to be done on this but just uploading so I can work on this from my laptop at school

(cherry picked from commit 17ef3bacf1a95b3778570ce80ec9582177c4649c)

* SFX files and settings menu

Added some sound files for sfx and light changes for the settings menu to continue to work on later.

(cherry picked from commit 571e9bcd4503ab057ca9b09099a4f41f4f9d562f)

* Sorry this is a bunch of random changes lmao. Added ambiences to NathanP2, the Prefab to play Ambience. Also, added new respawnManager to respawn necesasry objects like OrangeObjects and ScribbleWall. Moved some scripts into folders. Random level fixes for Mike, Claire, etc from playtesting.

(cherry picked from commit b1b9afbf29567d345e08e4a96ca4f4da3b63e885)

* sfx added + slider func

Added some more sound effects, sliders in settings menu now play a sound to reflect their real volumes, added looping sound to drawing canvases.

(cherry picked from commit 8007a22b04b5dde97c5cbfba0ebc9ccc8ab904c2)

* I'm not gonna lie. I don't remember what I changed
about the levels, but I'm PRETTY sure it's something.
Mostly, Stickman now stops walking animation when walking into a wall
and stops playing footstepSFX as well. PageflipSFX when finishing level.
Quick logic fix for levelendtrigger b/c it would call loadnextscene
multiple times. Made audiosystem global so it's easier to code.

(cherry picked from commit 65a49121750f5d3fb48a452b08b4d0063a770bdd)

* Forgot to commit the change for the animation
controller update.

(cherry picked from commit b6cd4de1442639ee872adb574f27acf95450c4dd)

* Delete it.

I hate it. new page flip wav meta

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[08f720517b...](https://github.com/vdaular-dev/linksfordevs/commit/08f720517b645afcc5cc8bbd422084474926b9c6)
#### Tuesday 2023-08-08 08:23:11 by Ben Dornis

Updating: 8/7/2023 10:00:00 PM

 1. Added: Notes on exit interviews
    (https://rednafi.com/zephyr/notes_on_exit_interviews/)
 2. Added: Removing Randomness with LLDB
    (https://bryce.co/lldb-remove-randomness/)
 3. Added: My (Painful) Experience With Ubiquiti As A DevOps Engineer | tyzbit.blog
    (https://tyzbit.blog/my-painful-experience-with-ubiquiti-as-a-devops-engineer)
 4. Added: How does a CTO know when they need a coach?
    (https://blog.mocoso.co.uk/2023/06/26/how-does-a-cto-know-when-they-need-a-coach/)
 5. Added: Writing a recursive descent parser in Bash · m10k
    (https://m10k.eu/2023/07/29/pkgex-parser.html)
 6. Added: Being a Disciplined Person In an Undisciplined World
    (https://durmonski.com/self-improvement/disciplined-person/)
 7. Added: Tradeoffs in Testing
    (https://dillonshook.com/tradeoffs-in-testing/)
 8. Added: The Central Binomial Coefficient and Laplace's Method
    (https://cgad.ski/blog/the-central-binomial-coefficient-and-laplaces-method.html)
 9. Added: The universe is (probably) not a simulation
    (https://blog.georgovassilis.com/2023/08/07/the-universe-is-probably-not-a-simulation/)
10. Added: "Make something idiot-proof, the world will show you a better idiot"
    (https://www.izoukhai.com/blog/make-something-idiot-proof-the-world-will-show-you-a-better-idiot)
11. Added: Humble Tech Book Bundle: Math for Programmers 2023 by Manning
    (https://www.humblebundle.com/books/math-for-programmers-2023-manning-books)
12. Added: Hacking is child's play - SQL injection with Havij by 3 year old
    (https://youtube.com/watch?v=Fp47G4MQFvA)
13. Added: 06 We Speak: IBM MQ
    (https://youtu.be/fv-ag8h5lYA)
14. Added: MassTransit Bus Stop - Request Response via Messaging (RPC)
    (https://youtube.com/watch?v=TWWVHWlBGIs)
15. Added: Disinterest.
    (https://www.baldurbjarnason.com/2023/disinterest/)
16. Added: Bike: Row Types
    (https://www.hogbaysoftware.com/posts/bike-row-types/)
17. Added: Growth Experiment: How Much Traffic Unsplash Drives to Your Website - Fresh van Root
    (https://freshvanroot.com/blog/how-much-traffic-unsplash-drives-website/)
18. Added: Layoffs and its impact
    (https://aravind.dev/layoff/)
19. Added: The Concretude of the Cloud
    (https://notes.ghed.in/cloud-computing-water-consumption-90e7e46f5d54)

Generation took: 00:10:08.3053764

---
## [rsalmaso/mame](https://github.com/rsalmaso/mame)@[e97630981c...](https://github.com/rsalmaso/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Tuesday 2023-08-08 08:45:12 by A-Noid33

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
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[2f2a113352...](https://github.com/argilla-io/argilla/commit/2f2a11335289d660ce20aea11c9b969b0316fd2b)
#### Tuesday 2023-08-08 08:45:58 by peppinob-ol

[DOCS] Code Refactoring and content update of quickstart_workflow.ipynb (#3472)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

I found the quickstart workflow not as quick as it could be:

- Cells cannot be run straightaway in google colab and need extra work
(eg. libraries not imported).
- Some important concepts (eg. records and datasets) are not clearly
stated in text and code snippets
- Text refers to the same steps more than once (no clear chain of
thought)
- Cells override the same variable (eg. record), so the feeling is more
of a cheatsheet than of a tutorial notebook
- Content is not updated (eg. ArgillaTrainer is not ever mentioned in
the Train section)

I worked on a new version of the notebook with enhanced code and text
cells.Ii added also code snippets for training examples which were only
described textually.

One last suggestion: It's advisable that external files (data) are
downloaded programmatically by running a cell (eg. using `requests
`library). `Snapchat_app_store_reviews.csv` and `kaffee_reviews.csv` are
taken from kaggle which requires sign-in, so it's not possible to
download them directly. Possible solutions:

- place a copy of the Kaggle datasets in Arggilla's GitHub repository
(if permitted by Kaggle's terms of use)
- select other datasets from another source.

Closes #3431

**Type of change**

(Please delete options that are not relevant. Remember to title the PR
according to the type of change)

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Refactor (change restructuring the codebase without changing
functionality)
- [ ] Improvement (change adding some improvement to an existing
functionality)
- [X] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes. And
ideally, reference `tests`)

- [ ] Test A: code run with latest google-colab (v.1.0.0)

**Checklist**

- [X] I added relevant documentation
- [X] follows the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [X] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---------

Co-authored-by: devorma <94636163+devorma@users.noreply.github.com>
Co-authored-by: davidberenstein1957 <david.m.berenstein@gmail.com>

---
## [Boopideedoo/tgstation](https://github.com/Boopideedoo/tgstation)@[f2ec16c1e6...](https://github.com/Boopideedoo/tgstation/commit/f2ec16c1e6485bdf2035837fb3d42de24900e8b4)
#### Tuesday 2023-08-08 08:50:14 by Vekter

Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

---
## [GagosideForMayor/webhook-testing](https://github.com/GagosideForMayor/webhook-testing)@[d7c2e56e45...](https://github.com/GagosideForMayor/webhook-testing/commit/d7c2e56e458be672410f2bd49563cacafe89cc3b)
#### Tuesday 2023-08-08 09:00:51 by GagosideForMayor

Simplified confirmation.html because im too lazy to troubleshoot and the complicated code is fucking annoying

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[55379fad3b...](https://github.com/Offroaders123/NBTify/commit/55379fad3b3ddb73a5dfc694c940fd4df2aea03d)
#### Tuesday 2023-08-08 09:02:59 by Offroaders123

Improved Tipes + To Organize

Was surprised that 'tipes' isn't a real word, thought it would be taken for something already. Any time I think of a weird name of a mispelling on purpose for the memes, I always Google it to make sure it's not something I don't mean it to be lol. Did that ever happen to your when you were little? You use a word because you thought it had a funny reaction from people, or that it just sounded cool, but then it's bad and you're not supposed to use it? That happened a few times for me before, and I've been on edge from doing it again accidentally 😂

Listening to Psychedelic Porn Crumpets, such a great album! (High Visceral {Part 1})

---
## [OasisDEX/oasis-borrow](https://github.com/OasisDEX/oasis-borrow)@[74ba200fb3...](https://github.com/OasisDEX/oasis-borrow/commit/74ba200fb34574189018be38df82e6159271b0e3)
#### Tuesday 2023-08-08 09:25:03 by Jakub Swierczek

[Network Switcher] Goerli Support (#2677)

* Add support for specifying test networks in wallet connection

This commit adds functionality for including test networks when establishing the wallet connection. An optional parameter 'includeTestNet' has been introduced to multiple components and helper functions concerning wallet connections and network configurations.

The new parameter's state is also included in useEffect dependencies lists, ensuring the correct behavior concerning the component's lifecycle when changing the network status. This extension aids in testing and development activities by enabling the interaction with test networks directly from the user interface.

Furthermore, the reducer logic for handling network change events has been extended. Network changes are now handled more gently: instead of a brute force approach, a method was introduced to decide whether sending a network chain change event is necessary or not.

Console.log() statements were introduced for debugging purposes to help & monitor the correctness of the established context.

Finally, extra precautions were included to handle unwanted state changes or transitions between mainnet and the Goerli test network by implementing a safety reload mechanism. This ensures the application's stability & predictability in terms of state transition between differing network environments.

* Improve error logging in jsonRpcBatchProvider

This commit enhances the logging of the batch request errors by including the connection URL. The change will print out not only the request that caused the error and the error itself, but also the URL of the connection it was made to. This extra information should help with debugging, especially when troubleshooting problems in environments with multiple instances of the application.

* Remove custom network parameter

This commit removes custom network parameter from the application in files along with their respective tests. The network parameter was removed as we now retrieve this information directly from Web3 rather than depending on application's state/configuration. This improvement makes the way we handle networks in the application more understandable and less error-prone.

* Add testNet connection capability

The connecting functionality has been updated to provide optional support for testNet. The Context and functions 'connect' and 'shouldSendChangeNetworkOnConnected' have been modified to accept another parameter 'couldBeConnectedToTestNet'. This change allows users to connect to testNet networks by passing 'includeTestNet={true}' in 'WithWalletConnection'. This added flexibility aids in development and testing scenarios without affecting the production-ready, main network functionality.

* Remove unused 'connect' function to switch networks

* Refactored web3-on-board-connector-provider for clarity

In this commit, I have removed some unnecessary code to make the web3OnBoard more readable and maintainable. The 'getNetworksFromPageNetwork' function was moved to a separate file for better organization. The condition to change network was also simplified; it now only checks if the desiredNetworkHexId is different from state.walletNetworkHexId. Some unused functions and excess code were removed from the file to declutter the environment. As a result, the code inside 'connect' method is now cleaner and easier to understand.

* Added function to toggle between Mainnet and Testnet

A new function "toggleBetweenMainnetAndTestnet" has been added to switch connectivity between Mainnet and Testnet. Changes have been made to web3-on-board-connector-provider.tsx, connected-wallet-state-reducer.ts, useConnection.tsx, NavigationNetworkSwitcher.tsx and wallet-state-event.ts files.

This update allows users to easily swap between the two networks, hence improving the user interaction with our blockchain functionalities. Previously, swapping networks required a manual change of network configurations. This all-in-one toggle simplifies this process increasing efficiency and usability.

* Refactor codes related to network handling for better flexibility

This commit comprises a series of changes to improve the handling of different networks across the platform. Previously, many parts of the code were hardcoded with specific network ids. They were replaced by a more dynamic approach, providing greater flexibility in setting and changing the network.

The major alteration is in `use-network-connector.tsx` - a new hook `useLegacyDefaultChain` is implemented for remembering the last utilized chain to ensure consistency across different sessions. Also, the `defaultChainId` attribute is now set to `defaultChain` to fetch the stored value from the localStorage.

Simultaneously, removals of redundant or unused code are performed across several files, and a few files for better organizing codes are added. For instance, `use-safafty-reload.tsx` is created to store the page reload logic.

The structure for function getNetworkRpcEndpoint is also simplified to only accept the network ID argument as there was no need anymore for the argument `isTestnet`. This commit is aimed at simplifying the codebase and reducing the redundancy for easier traceability of codes. In addition, it should make the app more resistant to bugs related to network id changes.

* Update wallet state to improve network flexibility

The wallet-state-guards.ts file has been updated to better handle changes in network id's. Instead of checking for a 'desiredNetworkHexId' in 'state.pageNetworkHexIds', the change ensures that the current wallet's network id is not included. This enhances the application's flexibility when handling various network changes and ensures consistency across different network ids, thereby reducing potential bugs.

* Fix typo in 'useSafetyReload' function and file name

The 'useSafaftyReload' function and its corresponding file are renamed to 'useSafetyReload' to correct the spelling mistake. This change ensures that the function name reflects its purpose more clearly, improving code readability and maintainability.

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[f26fec823d...](https://github.com/ARF-SS13/coyote-bayou/commit/f26fec823d7d769507a58776ceb2ecf9622f3de4)
#### Tuesday 2023-08-08 09:27:54 by Tk420634

Unleashing the void

If I want to play as the literal Void from Hallow Knight I fucking will, fuck you Poojawa.

---
## [Tsurupeta/Foundation-19](https://github.com/Tsurupeta/Foundation-19)@[8de9ad250a...](https://github.com/Tsurupeta/Foundation-19/commit/8de9ad250ad057d1b24aa81f449ff32c26816cd7)
#### Tuesday 2023-08-08 10:15:02 by cheesePizza2

Fixes contraband detectors (whooooooooooops) (#1228)

* whooooooooooooooooops

* fixes for my fixes

* fuck you

* qdel(announce)

* QDEL_NULL

---------

Co-authored-by: TheDarkElites <73414180+TheDarkElites@users.noreply.github.com>

---
## [kemdict/kemdict](https://github.com/kemdict/kemdict)@[6ed2c3b8df...](https://github.com/kemdict/kemdict/commit/6ed2c3b8df783d8413a90f0d72885f19f2359919)
#### Tuesday 2023-08-08 10:26:30 by Kisaragi Hiu

Remove locally installed eslint

This is -72 packages.

The JS world apparently wants every single project to pin every
development tool they use and install them locally. If pnpm isn't
used, and every project follows this "best practice", every project
will have its own instance of every editing tool that it needs.

This is ridiculous.

An editing tool doesn't need to be versioned as precisely as a library
dependency. Pinning them makes it more convenient for a new
developer to the repository to set up their development environment,
but getting every project to install the same tools over and over
again isn't the best way, or even a good way. It's standardized and
arguably works, but it is still ridiculous.

Install scripts and helper scripts might not work as well, but we've
settled on a dirty workaround without even remembering how ridiculous
it is.

If using a linter is depending on a linter, literally every project
that follows the best practice will have to depend on a linter, and
this is what JS best practice demands for every project right now. It
works fine, across platforms and across familiarities with the
ecosystem, but it's still a dirty mess.

An ecosystem-wide linter should hopefully eventually settle down such
that it has a core that is safe to install globally and assume to be
unchanging.

I would also like to remove locally installed prettier, but

- The current version of astro (2.10.3) depends on
  @astrojs/language-server ^1.0.0 (???)
- @astrojs/language-server 1.0.8 depends on prettier 2.8.8
- so `npx prettier` is always 2.8.8

It's a mess, and I honestly am not sure what it should've been like.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[95ec0e6545...](https://github.com/tgstation/tgstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Tuesday 2023-08-08 10:39:22 by necromanceranne

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6c34d93be7...](https://github.com/tgstation/tgstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Tuesday 2023-08-08 10:40:25 by necromanceranne

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
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[d875610098...](https://github.com/CoiledLamb/lorbstation/commit/d875610098a1259a5112d4a0e5afc0b7bd32ff6d)
#### Tuesday 2023-08-08 11:26:52 by Rhials

[NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**


https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

---
## [ibrahim1031/QuotesWebsite](https://github.com/ibrahim1031/QuotesWebsite)@[32709dfc32...](https://github.com/ibrahim1031/QuotesWebsite/commit/32709dfc32b1b0cd7285a3463f75821e8c0fee85)
#### Tuesday 2023-08-08 12:28:05 by ibrahim1031

Update README.md

Welcome to our Quotes GitHub repository, where inspiration, wisdom, and wit converge in a collection of thought-provoking and uplifting quotes! Our repository is a treasure trove of carefully curated quotes from various sources, spanning literature, philosophy, pop culture, and beyond. Whether you're seeking a spark of motivation, a touch of humor, or a moment of reflection, our Quotes repository has something for everyone.

Key Features:
1. **Diverse Range of Quotes:** Our repository boasts a diverse array of quotes that cover a wide spectrum of topics, emotions, and perspectives. From ancient philosophers to contemporary thinkers, from movie dialogues to famous book excerpts, we've gathered quotes that resonate across cultures and generations.

2. **Easy Browsing:** With our user-friendly interface, exploring quotes is a breeze. You can easily search for quotes by keyword, author, category, or even by the mood they evoke. Whether you're looking for a quote to kick-start your day or to complement a heartfelt message, our repository has you covered.

3. **Contributions Welcome:** We believe in the power of community collaboration. Feel free to contribute your favorite quotes or submit corrections to existing ones. Our repository thrives on the collective wisdom and creativity of contributors like you.

4. **API Access:** Developers, rejoice! We offer API access to our quotes repository, allowing you to integrate these pearls of wisdom into your applications, websites, or projects seamlessly. Enhance your content with quotes that add depth and engagement.

5. **Random Quote Generator:** Need a dose of inspiration at random? Our repository features a random quote generator that serves up gems from our collection with just a click. You never know which quote might touch your heart or spark your imagination.

6. **Categorized Collections:** To streamline your search, we've organized our quotes into intuitive categories such as Love, Success, Wisdom, Humor, and more. Explore these categories to find the perfect quote for any occasion or mood.

7. **Open Source:** We believe in open collaboration and knowledge-sharing. Our Quotes repository is open source, inviting developers and enthusiasts to contribute, enhance, and improve the platform for everyone's benefit.

Whether you're a quote aficionado, a content creator seeking that perfect touch of eloquence, or simply someone who appreciates the beauty of language, our Quotes GitHub repository is your go-to destination for all things quotable. Join us in celebrating the power of words, one quote at a time. Explore, contribute, and be inspired!

---
## [munborn007/improved-funicular](https://github.com/munborn007/improved-funicular)@[f0d102961e...](https://github.com/munborn007/improved-funicular/commit/f0d102961e8c70670dd2dff9ef31bbfac32058b0)
#### Tuesday 2023-08-08 13:00:23 by Munborn

MONSTER BOUNDER SAMURAI

Honored guests and art enthusiasts, welcome to my NFT collection, where the brushstrokes of a digital samurai come to life. I am not bound by steel, but by lines of code, and my canvas is the boundless realm of the blockchain.

🌌 Like a swift katana, my art transcends time and space, encapsulating the spirit of ancient warriors and modern dreams alike. Each stroke is a dance of precision, a harmonious fusion of tradition and innovation.

🎨 As you traverse the ethereal landscapes of my collection, you'll witness the essence of bushido, the unwavering courage, and the devotion to mastery. My NFTs are not mere images; they carry the soul of the samurai, guiding you on a journey through the ever-changing tides of life.

🏯 Embrace the delicate beauty of a cherry blossom in bloom, and feel the raw power of a thundering storm on the horizon. From serene meditation to fierce battles, my art encapsulates the duality of existence.

💫 As you claim a piece from this collection, you become part of the lineage of warriors, guardians of a timeless legacy. Let these NFTs resonate with your soul, for they are not just tokens but reflections of the warrior within you.

🌟 So, dear visitors, immerse yourselves in the enigmatic world of my NFT collection, and let the spirit of the samurai ignite the flames of inspiration within your heart.

🗻 Embark on this odyssey, and together, we shall embrace the ephemeral beauty and eternal strength that defines the way of the digital samurai. Arigato, and may the path of honor guide your journey.

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[86b58866bc...](https://github.com/Stalkeros2/Skyrat-tg/commit/86b58866bc0e3e8a1ee2e511328b6a76687b6e77)
#### Tuesday 2023-08-08 13:30:27 by SkyratBot

[MIRROR] Science Resprite! (With Sovl!) [MDB IGNORE] (#22861)

* Science Resprite! (With Sovl!) (#77314)

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

* Science Resprite! (With Sovl!)

* Update vending.dm

---------

Co-authored-by: OrionTheFox <76465278+OrionTheFox@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [ZoeB/mame](https://github.com/ZoeB/mame)@[c4a19a68a6...](https://github.com/ZoeB/mame/commit/c4a19a68a67cd32ffaaa37edfd6f1c2ba347905f)
#### Tuesday 2023-08-08 13:32:37 by Ivan Vangelista

New systems marked not working
------------------------------
Desert Gold (20202311, ASP) [anonymous, Heihachi_73]
Diamond Eyes (10129211, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (10177911, ASP) [anonymous, Heihachi_73]
Silk Road (10176811, ASP) [anonymous, Heihachi_73]
Snap Shot (20115211, ASP) [anonymous, Heihachi_73]
The Golden Gong (20196011, ASP) [anonymous, Heihachi_73]
Wild Cougar - Power Pay (30214211, ASP) [anonymous, Heihachi_73]
Wings over Olympus (10176511, ASP) [anonymous, Heihachi_73]

New clones marked not working
-----------------------------
5 Dragons (10176611, ASP) [anonymous, Heihachi_73]
5 Dragons (10178611, New Zealand) [anonymous, Heihachi_73]
5 Koi - Power Pay (1J016211, ASP) [anonymous, Heihachi_73]
50 Lions (0152077, US) [anonymous, Heihachi_73]
100 Lions (30223811, ASP) [anonymous, Heihachi_73]
Arabian Nights (10122611, ASP) [anonymous, Heihachi_73]
Big Ben (10169611, ASP) [anonymous, Heihachi_73]
Buccaneer (10181911, ASP) [anonymous, Heihachi_73]
Buffalo (20232611, ASP) [anonymous, Heihachi_73]
Brazil (10218511, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (20265311, New Zealand) [anonymous, Heihachi_73]
Dream Catcher (10172921, ASP) [anonymous, Heihachi_73]
Fire Dancer (10191311, ASP) [anonymous, Heihachi_73]
Fortune King (10230911, ASP) [anonymous, Heihachi_73]
Geisha (10122011, ASP) [anonymous, Heihachi_73]
Geisha (10112411, ASP) [anonymous, Heihachi_73]
Go For Green (10122111, ASP) [anonymous, Heihachi_73]
Golden Pyramids (10196511, ASP) [anonymous, Heihachi_73]
Heart of Gold (10184211, ASP) [anonymous, Heihachi_73]
Helen of Troy (10129121, ASP) [anonymous, Heihachi_73]
Helen of Troy (10116411, ASP) [anonymous, Heihachi_73]
Hollywood Dreams (10122811, ASP) [anonymous, Heihachi_73]
Helen of Troy (10122711, ASP) [anonymous, Heihachi_73]
House of Hearts (10208411, ASP) [anonymous, Heihachi_73]
Indian Dreaming (10192211, ASP) [anonymous, Heihachi_73]
King of the Nile (10127511, ASP) [anonymous, Heihachi_73]
Let's Go Fish'n (10223911, ASP) [anonymous, Heihachi_73]
Money Tree (10122211, ASP) [anonymous, Heihachi_73]
Paris Lights (10139011, ASP) [anonymous, Heihachi_73]
Peacock Magic (10134311, ASP) [anonymous, Heihachi_73]
Pelican Pete (10196211, ASP) [anonymous, Heihachi_73]
Pirates (10122311, ASP) [anonymous, Heihachi_73]
Pompeii (10122411, ASP) [anonymous, Heihachi_73]
Queen of Sheba (30146921, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10204311, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10192311, ASP) [anonymous, Heihachi_73]
Queen of the Nile Special Edition (10127411, ASP) [anonymous, Heihachi_73]
Ruby Magic (10148811, ASP) [anonymous, Heihachi_73]
Scatter Magic II (10122511, ASP) [anonymous, Heihachi_73]
Spring Festival (20267211, New Zealand) [anonymous, Heihachi_73]
Tigress (20243811, ASP) [anonymous, Heihachi_73]
Tiki Torch (10124011, New Zealand) [anonymous, Heihachi_73]
Torch of the Gods (20210211, ASP) [anonymous, Heihachi_73]
Turtle Treasure (10239811, ASP) [anonymous, Heihachi_73]
Where's The Gold (10177111, ASP) [anonymous, Heihachi_73]
Wild Cats (20258111, ASP) [anonymous, Heihachi_73]
Wild Goose (10155911, ASP) [anonymous, Heihachi_73]
Wild Panda (20225011, ASP) [anonymous, Heihachi_73]
Zorro (20167511, ASP) [anonymous, Heihachi_73]

-aristocrat/aristmk6.cpp updates:
* dumped 3 more System EPROM Sets [anonymous, Heihachi_73]
* renamed "Malaysian" games to ASP as the games don't have any specific region, only the BIOS does [Heihachi_73]

---
## [NetBSD/pkgsrc-wip](https://github.com/NetBSD/pkgsrc-wip)@[b256b79a7e...](https://github.com/NetBSD/pkgsrc-wip/commit/b256b79a7ede136d0ea6fbd3301295c005a1e37b)
#### Tuesday 2023-08-08 13:36:06 by Leonardo Taccari

regal: Update to 0.6.0

Changes:
0.6.0
-----
This release brings a new command for quickly generating new (custom or
built-in) rules, a new linter rule, and some improvements around
tooling.

0.5.0
-----
This release brings improvements and new features to improve the
experience of authoring custom rules, as well as new, granular
capabilities for ignoring files. Most of these improvements are
directly based on feedback — and in some cases contributions — from
Regal users, which is particularly exciting!

0.4.0
-----
This release brings three new rules related to comments and metadata annotations:

- invalid-metadata-attribute
- detached-metadata
- no-whitespace-comment

Additionally, new end-to-end tests exposed a few mistakes in a previous
refactoring, which have been fixed. This mistake meant that v0.3.0
failed to correctly run the `line-length` and `function-arg-return`
rules... so if you started from that release you're really getting
*five* new rules with v0.4.0... good thing we're keeping a fast paced
release cadence! Thanks to @kristiansvalland for reporting on this
regression.

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[8520a1f48a...](https://github.com/Hatterhat/Skyrat-tg/commit/8520a1f48a92c3733635daa8a74c209dd8aed04c)
#### Tuesday 2023-08-08 13:54:09 by SkyratBot

[MIRROR] When Space Dragons devour people they get .extinguish()ed [MDB IGNORE] (#22820)

* When Space Dragons devour people they get .extinguish()ed (#77248)

## About The Pull Request

When Space Dragons devour people they get extinguished, removing flames.
## Why It's Good For The Game

> When Space Dragons devour people they get extinguished, removing
flames.

I find it quite annoying that even after you die to a space dragon, the
jackass melts not just your jumpsuit, your suit, your hat, your mask, he
also melts your entire skin off, leaving your body husked with 400
million burn damage when and if the dragon finally dies. I don't think
there's any real reason for this to be necessary, it doesn't help the
dragon in any way - It's just kind of a middle finger to the dead guy,
or more accurately, an oversight.

Worse, because the flame sprite is stupidly noisy, when a dragon DOES
die the corpses are all thrown around randomly and they all look the
exact same, which makes it easier to ignore them.

If there's a concern about tracking sensors, I can make it disable them,
but honestly if you can do that with demons I don't see why this would
be a problem. Not even accounting for the fact that many jumpsuits
ingame are fireproof.
## Changelog
:cl:
qol: When Space Dragons devour people they get extinguished, removing
flames.
/:cl:

* When Space Dragons devour people they get .extinguish()ed

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [re0312/rust](https://github.com/re0312/rust)@[4fc6b33474...](https://github.com/re0312/rust/commit/4fc6b33474680ba57e10d56371c2c3df91788e26)
#### Tuesday 2023-08-08 13:55:28 by bors

Auto merge of #114011 - RalfJung:place-projection, r=oli-obk

interpret: Unify projections for MPlaceTy, PlaceTy, OpTy

For ~forever, we didn't really have proper shared code for handling projections into those three types. This is mostly because `PlaceTy` projections require `&mut self`: they might have to `force_allocate` to be able to represent a project part-way into a local.

This PR finally fixes that, by enhancing `Place::Local` with an `offset` so that such an optimized place can point into a part of a place without having requiring an in-memory representation. If we later write to that place, we will still do `force_allocate` -- for now we don't have an optimized path in `write_immediate` that would avoid allocation for partial overwrites of immediately stored locals. But in `write_immediate` we have `&mut self` so at least this no longer pollutes all our type signatures.

(Ironically, I seem to distantly remember that many years ago, `Place::Local` *did* have an `offset`, and I removed it to simplify things. I guess I didn't realize why it was so useful... I am also not sure if this was actually used to achieve place projection on `&self` back then.)

The `offset` had type `Option<Size>`, where `None` represent "no projection was applied". This is needed because locals *can* be unsized (when they are arguments) but `Place::Local` cannot store metadata: if the offset is `None`, this refers to the entire local, so we can use the metadata of the local itself (which must be indirect); if a projection gets applied, since the local is indirect, it will turn into a `Place::Ptr`. (Note that even for indirect locals we can have `Place::Local`: when the local appears in MIR, we always start with `Place::Local`, and only check `frame.locals` later. We could eagerly normalize to `Place::Ptr` but I don't think that would actually simplify things much.)

Having done all that, we can finally properly abstract projections: we have a new `Projectable` trait that has the basic methods required for projecting, and then all projection methods are implemented for anything that implements that trait. We can even implement it for `ImmTy`! (Not that we need that, but it seems neat.) The visitor can be greatly simplified; it doesn't need its own trait any more but it can use the `Projectable` trait. We also don't need the separate `Mut` visitor any more; that was required only to reflect that projections on `PlaceTy` needed `&mut self`.

It is possible that there are some more `&mut self` that can now become `&self`... I guess we'll notice that over time.

r? `@oli-obk`

---
## [zydras/Skyrat-tg](https://github.com/zydras/Skyrat-tg)@[1fe7b10e33...](https://github.com/zydras/Skyrat-tg/commit/1fe7b10e339ea0d6a3d49f864e1badc5c831e791)
#### Tuesday 2023-08-08 13:57:39 by SkyratBot

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
## [caryr35/docs](https://github.com/caryr35/docs)@[e4574dfbbe...](https://github.com/caryr35/docs/commit/e4574dfbbeff9f6ff7ed0d4e6e427085809d9abb)
#### Tuesday 2023-08-08 14:24:50 by Ben Jarmak

Release Selector 23.06 Updates (#394)

This PR updates the release selector for 23.06:
- Python `3.8` has been replaced with `3.9`
- CUDA 12 has been added for pip!
   - In Conda/Docker it shows as a disabled button
- I've added a new CUDA options row for pip - doing this let us get rid
of the note and make it clear the CUDA version supported directly
through the selector
- Moves `Method` above `Python` since it's more thematically appropriate
IMO
- ~I could see doing this for CUDA also, but didn't want to change
_tooooo_ much all at once~
- Made the change - I did this because `Method` changes the results of
`CUDA`, feels wrong for something downstream to be above physically
- Adds cuSpatial for pip (Paul's working hard here 🙏 )
- Removes all `CLX` options as it has been removed/archived from RAPIDS

Some thoughts/comments:
- I don't clear the conda/pip cuda versions when they aren't being used
- I figured it's a better experience for it to be saved if the user goes
back and forth (and seemed like wasted cycles)
- I think we might be opening ourselves to questions about CUDA version
compatibility, not 100% on the best path forward, but I can imagine a
thought process like:
   1. I have a CUDA 12 machine
   2. I want RAPIDS
3. Huh...only pip supports CUDA 12. I guess that means I can't use
cuXFilter since it doesn't have a pip release
- Not sure if it makes sense to have a note that says Conda/Docker CUDA
11 installations work great on CUDA 12 machines

Contributes to #386

---
## [Letinemeso/LEti_Engine](https://github.com/Letinemeso/LEti_Engine)@[34d5f71e5e...](https://github.com/Letinemeso/LEti_Engine/commit/34d5f71e5e6eab2ee0f9becb19cbd3c8151e43b6)
#### Tuesday 2023-08-08 15:15:05 by Letinemeso

holy fuck, this small cosinus miscalculation took the whole evening to find in the most unpredictable place

---
## [tcbrindle/flux](https://github.com/tcbrindle/flux)@[44a30780b4...](https://github.com/tcbrindle/flux/commit/44a30780b4f0ad1072dce997b055c6f5d066ff8a)
#### Tuesday 2023-08-08 15:40:27 by Tristan Brindle

Add cmp::min cmp::max

Because they're ordinary function templates, `std::min` and `std::max` can't be passed as arguments to functions without wrapping them in lambdas (or doing a horrible function pointer cast). This makes me sad.

`std::ranges::min` and `std::ranges::max` are function objects and so can be passed as function arguments -- except for MSVC, which annoyingly goes out of its way to prevent you doing this very useful thing. This also makes me sad.

To improve matters, we'll add `flux::cmp::min` and `flux::cmp::max` which take two arguments and an optional comparator and return the lesser and greater respectively.

As an added bonus, `max()` now correctly returns the second argument if both are equal, and our versions of these functions should be less likely than the standard versions to cause dangling when used with rvalues.

---
## [rahul93030/BTSArmymr.r.status](https://github.com/rahul93030/BTSArmymr.r.status)@[6fb9eb99c6...](https://github.com/rahul93030/BTSArmymr.r.status/commit/6fb9eb99c6bf3a25d428f7c47a43902451d3e213)
#### Tuesday 2023-08-08 16:11:00 by rahul93030

Mr.r.status

The BTS ARMY is a dedicated fanbase of the South Korean boy band BTS. BTS, short for Bangtan Sonyeondan or "Bulletproof Boy Scouts," is a popular K-pop group formed by Big Hit Entertainment. The ARMY consists of millions of fans worldwide who support and celebrate BTS through social media, fan art, fan fiction, and more. The group's members are RM (formerly Rap Monster), Jin, Suga, J-Hope, Jimin, V, and Jungkook. BTS has achieved immense global success, breaking numerous records and winning awards. Their music blends various genres, including pop, hip-hop, and R&B, and often addresses social issues and personal experiences. Their fandom is known for their passionate support and involvement in charitable activities. Keep in mind that information may have evolved since my last update in September 2021.

---
## [NullDagaf/NovusSS13](https://github.com/NullDagaf/NovusSS13)@[5b923710f0...](https://github.com/NullDagaf/NovusSS13/commit/5b923710f078cad3a3d97024b7cc6bcdc437ec3a)
#### Tuesday 2023-08-08 18:10:37 by ChungusGamer666

Merge pull request #7 from ChungusGamer666/blackbetty

Genitals 3 - Fuck you Null

---
## [darkyy92/inclementpatch](https://github.com/darkyy92/inclementpatch)@[d4354bedc2...](https://github.com/darkyy92/inclementpatch/commit/d4354bedc22aeee34cea3b38d16ef8640145e831)
#### Tuesday 2023-08-08 19:12:59 by mutantmassadri

Makes a bunch of moves relevant to Doubles more common across the roster for better options in a Double Only run

Life Dew- Politoed, Golduck, Starmie, Vaporeon, Lapras, Azumarill, Suicune, Milotic, Alomomola, Primarina, Dhelmise
Jungle Healing- Meganium, Bellossom, Sunflora, Celebi, Lilligant, Tangrowth, Gogoat, Rillaboom
Instruct- Jynx, Porygon, Mewtwo, Xatu, Ludicolo, Gardevoir, Kecleon, Vespiquen, Watchog, Simisage, Simisear, Simipour, Sigilyph, Meloetta, Pangoro, Sirfetchd
Mat Block- Heracross, Hariyama, Medicham, Infernape, Emboar, Samurott, Pangoro, Hitmontop
Strength Sap- Ariados, Crustle
Spotlight- Pachirisu, Pikachu, Ambipom, Meloetta, Wigglytuff, Ledian, Watchog
Follow Me- Audino, Clefable, Togedemaru, Primarina, Obstagoon, Miltank, Grumpig, Perrserker
Rage Powder- Oranguru, Toxapex, Bellossom, Venusaur, Appletun
Psycho Shift- Simisage, Liepard, Obstagoon
Healing Wish- Delcatty, Simipour, Delibird, Meowstick, Cosmoem
Lunar Dance- Jumpluff, Meloetta, Minior, Meganium, Hoopa, Liepard
After You- Meloetta, Meowstick, Liepard, Pachirisu, Bisharp, Lurantis, Meowth (both), Dusknoir, Gardevoir, Gallade, Jynx,  Volbeat, Mienshao, Cryogonal, Ribombee, Alakazam, Inteleon, Froslass, Watchog
Quash- Rattata (both), Nidoran (both), Meowth (not galarian), Muk (both), Kingler, Vespiquen, Pangoro, Incineroar, Bisharp, Liepard, Accelgor, Crobat, Weavile, Greninja, Hawlucha, Salazzle, Seviper, Hitmonlee, Ambipom, Illumise
Sky Drop- Charizard, Articuno, Zapdos, Moltres, Aerodactyl, Dragonite, Skarmory, Lugia, Ho-Oh, Pelipper, Rayquaza, Braviary, Tornadus, Thundurus, Hawlucha, Yveltal, Tapu Koko, Lunala, Naganadel
		  Scyther, Vikavolt, Noivern, Empoleon, Delibird, Flygon, Drifblim, Emolga, Yanmega, Talonflame, Altaria, Archeops, Corviknight, Mandibuzz
Ion Deluge- Luxray, Wishcash, Klinklang, Pikachu, Zapdos, Heliolisk, Togedemaru, Dragapult, Whimsicott, Grumpig

---
## [GrahamBurgers/grahamsperks](https://github.com/GrahamBurgers/grahamsperks)@[ed82752538...](https://github.com/GrahamBurgers/grahamsperks/commit/ed8275253897d8ebf62406399abc9320c46d01a8)
#### Tuesday 2023-08-08 19:31:31 by Graham

Chinese translation merging!

let me know if any bugs arise from this... but this should make development a lot easier. having to make every change twice on different versions was a pain in the ass, and I kinda feel like an idiot for not doing this sooner

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[280388435b...](https://github.com/TaleStation/TaleStation/commit/280388435b173226e37973b55e1413997cc35093)
#### Tuesday 2023-08-08 19:47:26 by TaleStationBot

[MIRROR] [MDB IGNORE] Science Resprite! (With Sovl!) (#7124)

Original PR: https://github.com/tgstation/tgstation/pull/77314
-----

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
## Changelog
:cl:
image: resprited the entirety of RnD! Genetics, Robotics, the RD, and
the Science Team themselves will enjoy the fresh new looks but same
great taste! No, wait, great STYLE! Don't eat these, they're covered in
chemicals.
/:cl:

---------

Co-authored-by: OrionTheFox <76465278+OrionTheFox@users.noreply.github.com>

---
## [hedgehog1029/Yogstation](https://github.com/hedgehog1029/Yogstation)@[d1c7dfdc1a...](https://github.com/hedgehog1029/Yogstation/commit/d1c7dfdc1ae55bfd9fa7f603f415b762ba6a472a)
#### Tuesday 2023-08-08 19:56:52 by SapphicOverload

IPC tweaks (#19467)

* funny tv head robot go brrrrr

* Update IPC.dm

* not that fast

* fuck it we ball

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[051cdc3256...](https://github.com/MCBCMF/MCBCMassacre/commit/051cdc3256bac89a26dd137aeeddf74da7ef3a5d)
#### Tuesday 2023-08-08 20:06:57 by Kelvin Williams

Tonight (EDT) the bell will ring!

# The Ringing of the Bell

The Creator is going to “ring the bell” very soon. The exact time is not going to be announced, but the order and intensity of the bell ringing (earthquakes) is as follows:

## Orr Chapel Quake
This earthquake’s epicentre will be located  in Sandy Hook, TN (an unincorporated city near Mount Pleasant) in Maury county. 

This will be a large earthquake for the CIA’s destruction of Orr chapel and the murder of it’s members. 

This quake also recognises Micah’s slain family and his family’s graveyard that was destroyed, both by or at the direction of the CIA. 

## Mount Calvary Baptist Church Quake
This earthquake’s epicentre will be located at Mount Calvary Baptist Church in Lexington, KY (4742 Todds Road). 

This will be the largest quake for the massacre that occurred there. 

## The Micah Quake 
This earthquake’s epicentre will be in Jessamine county, KY. It will signal when Micah (born: Kelvin Eugene Williams on March 23, 1977) has started his mission for the Creator. This will be Micah’s 23rd mission on Earth. 

This minor quake will also be to recognise the lives lost in Jessamine county, mostly Micah’s friends, throughout the larger tragedy. 

## The TomTom Quake
This earthquake’s epicentre will be in Kanawha county (Hughes Creek), WV. It will signal when TomTom (to practically everyone TomTom, to others Thomas, born: September 23, 1978) has started his mission for the Creator. This also is TomTom’s 23rd mission on Earth. 

This minor quake will also recognise the lives lost in Kanawha county, mostly TomTom’s friends and family, throughout the larger tragedy. 

# Aftermath
The Creator hopes this will be all He has to do to stop the ongoing massacre and end the greater tragedy. 

The tragedy is all a [“Sign of the Times.”](https://youtube.com/watch?v=8EdxM72EZ94&feature=sharea).

And so begins the [“Purple Rain”](https://youtube.com/watch?v=S6Y1gohk5-A&feature=sharea). That means [“It’s raining men.”](https://youtube.com/watch?v=l5aZJBLAu1E&feature=sharea). He has never had to rain down men , although the 23rd mission for both of His servants, they’ve never been identified before. This is just the beginning of the “Great Storm” but it’s the [“Nature of our Kind.”](https://youtube.com/watch?v=lzoABrBtH9A&feature=sharea). 

He does this because life is supposed to be fun. After all, [“Girls just want to have fun.”](https://youtube.com/watch?v=PIb6AZdTr-A&feature=sharea) We WILL get back to fun in this neighbourhood called Earth. 

Guys, don’t get hung up on the use of  "woman" or “girl" (it does not always mean female).

---
## [PelicanPlatform/pelican](https://github.com/PelicanPlatform/pelican)@[bc56423c42...](https://github.com/PelicanPlatform/pelican/commit/bc56423c4210dfa1e9a480bf5e449edd1acbc000)
#### Tuesday 2023-08-08 20:07:43 by Justin Hiemstra

Local lint & Director CLI hookup + bug fixes

PR #7 introduced a framework for including the Director in the Pelican CLI,
toward making all Pelican services available under a single binary. This commit
extends that PR to hook the Director package up to the CLI, the Pelican's
configuration mechanisms, and to actually sort out a few bugs related to the
untested director code.

It should be noted that there are currently a few hacks in the code that need
clearing up before any merge, but as of now the commit makes the following
possible:
`pelican director serve --cache-port 8000`
This will serve the Director's cache-redirection service on port 8000 using a gin
engine. When we've figured out how to handle Origin redirects and implemented an
origin-redirect service, we'll be able to do:
`pelican director serve --cache-port 8000 --origin-port 8001`
to split apart the two endpoints.

As for the local lint... I'm still trying to figure out how to shut that feature
off in my editor. Sorry for the noise!

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[8ddcb6ba45...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/8ddcb6ba45b3d6e3bb4c6045c04ccdd296422a18)
#### Tuesday 2023-08-08 20:09:43 by SkyratBot

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
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[4d754d86cd...](https://github.com/Zeodexic/tsorcRevamp/commit/4d754d86cd59250806fd9f83c2b6b48ae1658fd1)
#### Tuesday 2023-08-08 20:15:42 by timhjersted

Enemy Balance Pass 1 + Other Enemy Changes

-Health values for SHM enemy spawns have been equalized to roughly all be in the same range (1k-3k mostly, in increments of 500), that way, if these values are still too high they can be reduced by increments of 500
-Some health values for preHM & HM enemies were rounded up or down slightly to be less random
-Soul drop values have been equalized roughly using a basic equation: life / 2 for preHM and HM, and life / 2.5 for SHM - these equations ended up being very close to existing values for most enemies: some enemies thus got an increase, some got a reduction, but the standardization should allow us to monitor the soul economy more easily (vanilla enemies weren't touched however, but should probably be handled differently due to their simplicity, like life / 3 or 4 etc)
-Several enemies soul drops were adjusted differently or untouched based on their rarity, simplicity, or worm-multi-hit nature (worms were life / 2 / 2)
-Many enemies got spawn rate buffs or nerfs based on feedback and a look through their current locations
-Several enemies spawn in new locations
-Basilisk enemies no longer can teleport by default and spawns were reduced slightly
-All Hollow and Lothric enemies finally got damage scaling for HM and SHM, and a visual ring was added for lothric enemies to reveal their proximity debuffs
-The Birds now are a bit more thematically distinct:  On enrage, The Hunter goes invisible, The Rage gains a bit of life, and The Sorrow gains high defense (ice protection)
-Red Knight gained SHM stats
-Fighter AI enemies TP less often when hit
-Added Black Knight event to SHM dungeon
-The old Jungle Wyvern sprite folder was renamed OceanWyvern as a reminder to potentially add a mini-boss event in the Western Ocean

---
## [sorbet/sorbet](https://github.com/sorbet/sorbet)@[6a1084aa55...](https://github.com/sorbet/sorbet/commit/6a1084aa558fbf334ccb605e40f347c6fa7f5069)
#### Tuesday 2023-08-08 20:29:39 by Jake Zimmerman

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
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[3e9d54628d...](https://github.com/realforest2001/forest-cm13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Tuesday 2023-08-08 20:30:37 by Ben

Can no longer bypass Lesser Drone Limit (#4034)

# About the pull request

Users can no longer keep menu open and bypass lesser drone slots

# Explain why it's good for the game

Honestly kinda wish I didn't make this one, infinite lesser drones
sounds really funny.

# Changelog
:cl:
fix: You can no longer circumvent the lesser drone limit by keeping the
prompt open.
/:cl:

---
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[9c79c3af49...](https://github.com/Katskan/cmss13/commit/9c79c3af49ba90e18f85c1624ba4e80d608debf2)
#### Tuesday 2023-08-08 21:10:36 by spartanbobby

Sweeping LV522 Changes + FORECON GL replaced by FORECON Sniper (Without the sniper) (#3917)

# About the pull request

This PR makes alot of small changes to LV522 along with alot of big ones
mainly

Blocks off the area north of fitness to prevent a "just go north" meta
Adds a new more central way to the reactor that branches off to 4 flanks
should give LZ2 more use since it's a bit more central than LZ1
Adds a new route into the reactor from the SE
Blocks off the small alleyway north of the engineering funnel people
into the dorm building
tightens up some parts of the reactor loosens some other parts
removes some detailing in the main hive areas to help builders
Adds new secrets to be found on the map
adds an overextension flank for those very brave marines to use
Changes to LZ2 making it more compressed
Addition of the FORECON Sniper (replacing the FORECON GL)
the FORECON sniper is a unique take on FORECON he spawns away from his
fellow survivors next to the corpse of his battle buddy the advantage
given to the sniper however is his thermal tarp a subtype of the ghillie
suit with a placeholder sprite at the moment that will allow the sniper
to hide and stealthily move throughout the colony to hopefully regroup
with his squad
the M42A rifle has been removed from the map
Adds a small piece of text explaining that FORECON should probably move
west to the crashed dropship to the FORECON intro
swaps the black weedable turf with a browner one for people who have bad
eyes and were mistaking it for weeds
swaps the assignments for defines bc nanu told me someone would ask me
to do it at somepoint
gives FORECON radioheadsets with the SOC and common channel because the
desc literally says FORECON use it and it doesn't make sense for them to
be radio-less

# Explain why it's good for the game

Map stuff:
LV522 currently just has a "go north" problem this PR aims to fix that
by opening more routes for the marines to go, centralize the main route
in an attempt to see more use in the rest of the colony and give LZ2
more use I'd really like to see this test-merged for a few days so see
what needs addressing in this new area

the wall north of engineering looks kinda funky but having it there
funnels people into the building and into the eastern section of the
colony rather than a straight line to the reactor

The FORECON Sniper:
Currently, FORECON GL is kinda unfitting and also kinda sucks the
sniper, on the other hand, would be a perfect fit for FORECON now I'm
not going to pretend the sniper isn't kinda OP right now so the FORECON
sniper won't actually get his M42A just the ghillie suit that gives him
still some uniqueness as a survivor as well as an incentive to survive
beyond the life of the regular sniper (to steal his gun)

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: SpartanBobby
add: Added a new survivor to LV522 the FORECON sniper he spawns alone
his only company being the corpse of his dead battle buddy, good luck
maptweak: Sweeping changes to LV522 including the reactor, north of
engineering, LZ1, the entire central area of the map, and north of
fitness in an attempt to see more of the colony used and to incentivize
flanking
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[ce09b07afd...](https://github.com/Katskan/cmss13/commit/ce09b07afd0f8d433ffee1a43bc4dfeb978f45f1)
#### Tuesday 2023-08-08 21:10:36 by ihatethisengine

Xeno Alliance Announcements + Greeno Civil War (#3990)

# About the pull request

Xenos now get messages when their queen set/break alliance to another
faction and when other queen set/break alliance with their hive.

Corrupted Xenos with implanted IFF tag now has a choice to defect from
the hive and become Renegade (hive allied to USCM) when Queen decides to
break alliance with USCM. Xenos that stay loyal to Queen rip the IFF
tags out. You have only 10 seconds to make a decision, so think quick.
By default xenos stay loyal to Queen.

Renegade Hive is allied to all human factions, but it mostly affects
structures and weeds. Renegade ability to attack someone fully depends
on its IFF tag settings.

Please check my messages because I'm not very good at writing.

# Explain why it's good for the game

More announcements are good because it's less confusing. You know when
someone set ally to you and you know when someone is betraying you. It
makes sense because allied xenos share announcements anyway. And sudden
betrayals are always a bit cheesy.

I think the Renegade addition makes research a little more fun and
rewarding. Now, if you implant corrupted xeno with an IFF tag, the xeno
player can choose to remain loyal to you if/when the Queen decides to
betray. Plus corrupted xenos with the IFF tag are no longer forced to
betray, so it's also good. Not sure if that makes sense lore-wise, but
since corrupted are artificially created and their DNA is decrypted, it
makes at least some sense. Plus we kinda have tamed xenos which work
really similarly.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
add: Added announcements for xenos about forming and breaking alliances.
add: Xenos with IFF tag now have a choice to stay loyal to USCM when
Queen decides to betray.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: Drathek <76988376+Drulikar@users.noreply.github.com>
Co-authored-by: harryob <me@harryob.live>

---
## [CUST-0M/fallout-exiles](https://github.com/CUST-0M/fallout-exiles)@[9c5b35479e...](https://github.com/CUST-0M/fallout-exiles/commit/9c5b35479eb64ede92d4f6d37b30f03e194d6a06)
#### Tuesday 2023-08-08 21:28:47 by ConstantineII

Fuck you Desert Rose

and your shitty copy paste sprites from citadel.

---
## [smclacke/minishell](https://github.com/smclacke/minishell)@[1445eafbfb...](https://github.com/smclacke/minishell/commit/1445eafbfb944d13d2cb97c4d2e17cbb34200fd2)
#### Tuesday 2023-08-08 21:42:56 by Sarah Mclacken

holy shit quotations are bullshit, notes in sarah.md

---
## [LanceSmites328/LC13Master](https://github.com/LanceSmites328/LC13Master)@[171b1478f9...](https://github.com/LanceSmites328/LC13Master/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Tuesday 2023-08-08 21:46:19 by vampirebat74

Limbus Company E.G.O dump (#1062)

* Adds roseate desire

roseate sfx

datums

weapons

add aedd

sprite adjustments

unfucks suits

new sfx

name fix

aaaa

adds capote

adds sloshing

farmwatch

farmwatch suit

stuff

farmwatch stuff

capote inhands

red sheet finished

sloshing gift

linters

Stuff

stuff

fixes shit

stuff

weapon code cleanup

spicebush finished

removes the heal

code fix

stuff

removes reference

farmwatch hat

new vfx

requested changes

* block duration

---------

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[cfd40aeef5...](https://github.com/Comxy/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Tuesday 2023-08-08 22:38:54 by necromanceranne

Imports and Contraband 2: Landfill Gacha Addiction (I put trash randomizers into cargo crates and called it content) (#76771)

## About The Pull Request

This is a followup on my previous PR involving cargo imports. I've made
a number of changes and new additions to cargo's imports and contraband.
But I've also changed how Smuggler's Satchels generate loot as well.

### New:
**Abandoned Crates:** You can now order in abandoned crates at a steep
price. Obviously these are just your standard fare abandoned crates, so
they've got a pretty long list of potential contents. Some great, some
utterly not worth the price you paid for the crate. Since they're quite
pricey, you can't order very many quickly. But this does allow cargo
techs the opportunity to spend the round solving puzzles to get
interesting loot.

**Dumpster of Maint Garbage:** This dumpster (similarly named to another
dumpster you can order) is filled with maint trash and potential maint
random spawns. This list is extensive enough that anything spawned in
this crate is likely to be mostly garbage. But, it is more affordable
than abandoned crates. I'd consider this the literally trashier version
of the abandoned crate.

**Shamber's Juice Eldritch Energy! Crate:** A crate with one can of the
extremely rare, short run edition of Shambler's Juice, Eldritch Energy!
This contains 5 units of eldritch essence. Heals heretics, hurts
everyone else! This is a VERY potent poison, but it also happens to be a
handy way for a Cargonian heretic to get a potent healing item without
having to waste knowledge points.

**Animal Hide Crate:** It's a cargo crate full of animal hides! This can
include fairly rare hides and some icebox creature hides as well, like
polar bear hides and wolf sinew. It's not too expensive, and mostly
spits out leather.

**Dreadnog Carton Crate:** A carton full of the worst eggnog imaginable.
This is just something to troll people with. Drink it and you'll get a
massive mood penalty. Dreadnog! May or may not contain space cola!

### Updated:

**Contraband Crate and Smuggler's Satchels:** This has had it's price
increased considerably. But, for good reason. It now contains some more
controlled random items, but also some more valuable contraband as well
as a very rare spawn. The upper end on his contraband can be extremely
valuable, but the majority of the items gained from contraband crates
will probably be either what you can get now (quite weak), or something
a bit more middle of the road (some more unique narcotics).

As a consequence, I've also passed this change onto smuggler's satchels,
as they used the crate to generate its contents. (it literally spawned
and then deleted a contraband crate to generate the contents hoo haa).

I've also increased the number of items in the smuggler's satchel. Since
the randomly spawned smuggler's satchels are quite a bit rarer now there
is only ever two spawned in the map, and spending actual TC on these is
somewhat counterproductive, I don't imagine this will be more beneficial
for scavenger hunters hoping for some interesting goodies.

**Russian Crate (the normal one):** The mosins now spawn in ancient gun
cases. These determine what kind of mosin you can get. 79% of the time,
you get the crap mosin. 20% of the time, you get a good mosin. And 1% of
the time, you get rations. This more tightly controls how many good
mosins are entering into the round and how much of a value purchase the
Russian crate actually is for getting ballistics. Since the process is
even more unlikely than before, it isn't necessarily as guaranteed that
you will get a good mosin. Hell, you might not even get a gun if you're
that unlucky.

**Shocktrooper Crate:** It now has an armor vest and helmet. So, not
only do you get some grenades, you get some protection as well. Since
this is the 'loud' crate, I felt it appropriate to make it slightly more
useful for enabling that.

**Special Ops Crate:** It now contains five mirage grenades and a
chameleon belt, and has had the survival knife improved to a
switchblade. This is probably the weakest of the two crates STILL, but
hopefully these make them a little more interesting and novel by giving
them pretty fun grenade to toy with.

## Why It's Good For The Game

My initial PR hoped to add in a few more interesting purchases for
cargo. I think currently cargo has a slight issue of not having enough
valuable or interesting uses for their money. I think it still has that
problem, but by including more unique crates that allow cargo to provide
some oddities into the round, that might slowly work itself out.

This PR hopes to provide another way to waste their money if they have
an excess amount. Landfill Trash Gambling. Spending it away on complete
junk, which I think is absolutely hilarious when it doesn't work out, as
it is soulful in its design. Definitely not inspired by my recent thrift
shop excursions this month buying and scrounging for furniture and
interesting clothing.

[Relevant](https://www.youtube.com/watch?v=QK8mJJJvaes)

Also, I wanted to buff some of the crates I introduced a bit last time,
and nerf the mosin production somewhat via a more controllable method
that I can actually adjust as necessary down the line.

## Changelog
:cl:
fix: Stops manifest generation runtiming when a cargo crate is empty.
add: Abandoned crates are now available via cargo imports.
add: Dumpsters full of maintenance trash are now available via cargo
imports.
add: An ultra-rare can of Shambler's Juice is now available via cargo
imports.
add: Animal hides and leathers can be (unreliably) ordered via cargo
imports.
add: The Dreadnog has entered this realm. To consume, purchase it via
cargo imports.
balance: Contraband Crates (and as a consequence, smuggler's satchels)
now generate more varied goods. Mostly the same, but sometimes you get
something quite different or even valuable.
balance: Mosins generated via the Russian supply crate are a bit more
random, weighing more heavily towards bad mosins than good mosins.
balance: Buffed both the shocktrooper and special op crate. Shocktrooper
now has an armored helmet and vest, and special op now has 5 mirage
grenades and a chameleon belt. The survival knife in the special op
crate is now a switchblade.
/:cl:

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[52c8da7ea4...](https://github.com/Comxy/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Tuesday 2023-08-08 22:38:54 by Jacquerel

PAI Holochassis are now leashed to an area around their card (#76763)

## About The Pull Request

This change restricts PAI holograms to an area around their assigned PAI
card. If you leave this area, you are teleported back to the card's
location (but not automatically put back into the card).

https://www.youtube.com/watch?v=L2ThEVa4nx8

This setting can be configured from the PAI menu, it's set pretty short
in the video because otherwise it wouldn't teleport when I threw the
card and I like doing that.

![image](https://github.com/tgstation/tgstation/assets/7483112/faf0fa0b-e9d6-4990-8d8c-f30def2892f1)

To accomodate this I set up a component to deal with a reasonably common
problem I have had, "what if I want to track the movement of something
in a box in a bag in someone's inventory". Please tell me if the
solution I came up with is stupid and we already have a better one that
I forgot about.

Also now you can put pAIs inside bots again, by popular request.

## Why It's Good For The Game

Personal AIs are intended to be personal assistants to their owner.
rather than fully independent entities which can pick up their own card
and leave as soon as they spawn.
As "aimless wanderer" players can now possess station bots, pAIs can be
limited to an area around the bearer of their card.

Because the holoform now doesn't contain the card, this also means that
a PAI cannot run off and then be impossible to retrieve. You are always
in control of where it can go.

Also it's funny to throw the card and watch the chicken get teleported
to it.

## Changelog

:cl:
add: Personal AI holograms are now limited to an area around their PAI
card. The size of this are can be configured via the PAI card.
add: pAI cards can now be placed inside bots in order to grant them
control of the bot.
/:cl:

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[3af26df8ca...](https://github.com/Comxy/tgstation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Tuesday 2023-08-08 22:39:15 by GoldenAlpharex

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
## [Rafael1108/datasheet](https://github.com/Rafael1108/datasheet)@[5843c6a707...](https://github.com/Rafael1108/datasheet/commit/5843c6a707c4d7e7c1b4364ce070300e8b80aaed)
#### Tuesday 2023-08-08 23:01:46 by Edwin Rafael Larrea Buste

Social Network Ads

Context
There's a story behind every dataset and here's your opportunity to share yours.

Content
What's inside is more than just rows and columns. Make it easy for others to get started by describing how you acquired the data and what time period it represents, too.

Acknowledgements
We wouldn't be here without the help of others. If you owe any attributions or thanks, include them here along with any citations of past research.

Inspiration
Your data will be in front of the world's largest data science community. What questions do you want to see answered?

Kaggle link
https://www.kaggle.com/datasets/rakeshrau/social-network-ads

---
## [vimpostor/vim-lumen](https://github.com/vimpostor/vim-lumen)@[c74fb000f8...](https://github.com/vimpostor/vim-lumen/commit/c74fb000f85092d2d641dbb0d1b3a87e38def819)
#### Tuesday 2023-08-08 23:05:42 by Magnus Groß

Implement Windows support

Originally my plan was to wait until some random user contributes
support for Windows, because I don't really care about that platform.
But let's face it: The odds of finding a skilled developer that is still
on Windows are already pretty low, but the odds of finding a Windows
developer that is good in FOSS and that uses vim on Windows of all
platforms are pretty much non-existent.

Together with the outlook on the hacky task of calling a bunch of Win32
API through Powershell - a single dumpster fire of a shell - it became
clear that there was no other way than to take matters in my own hands
and implement this myself.

And oh boy, was I not prepared for this epitome of cursedness.
Even the MacOS support that literally has to compile Swift programs on
the fly looks benign in comparison to this feast of Win32 API.

And what is up with Windows' fetish for handles everywhere? Oh, you want
to get a handle on a registry key? You better pass another useless root
handle for HKEY_CURRENT_USER so that we can return you yet another
handle for the key that you are really interested in.

OK before this ends in a page-long rant about what the hell is all
wrong with development on Windows, I'd rather quickly explain this
patch:

There luckily is a registry key that returns the user's dark mode
preference:

HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize\AppsUseLightTheme

Querying this key is easy with "reg query". Subscribing to changes
without polling is a bit more involved though. There doesn't really
exist a pure Powershell way to do this, so we abuse Powershell's ability
to call into Win32 API via signatures as strings (lol) to accomplish
this with interrupts (i.e. we get notified as soon something changes,
instead of having to poll).
For that we use another event struct and WaitForSingleObject that blocks
our thread until the next event is ready.

The windows platform itself can be detected by checking for the win32
feature, which is also set on 64bit Windows.
We must also expand <script> instead of <sfile> (which is used in the
MacOS platform), because it is expanded inside the function call instead
of free without function in the script file.

Another thing to watch out for is the whole CRLF bullshit, e.g. most vim
methods that convert from lines to arrays really only trim the line
feed, not the carriage return.
There also is some weird execution policy bullshit that prevents us from
running the script directly, but we can easily circumvent it just by
passing a parameter, wtf.
There is just so much bullshit when developing on Windows that gets into
your way in little but very annoying ways. Of course I also got a
forced update from this meme operating system as soon as I shut down...

Alright, this is enough Windows for me, can't wait to start you up again
in another 2 years.

Fixes #3

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[66d67d3ae8...](https://github.com/treckstar/yolo-octo-hipster/commit/66d67d3ae8db17aaf66a70459522bf0c6c067142)
#### Tuesday 2023-08-08 23:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [sjp38/linux](https://github.com/sjp38/linux)@[af50d6151c...](https://github.com/sjp38/linux/commit/af50d6151cba1d797b2fde232b161608a5e264ce)
#### Tuesday 2023-08-08 23:38:37 by David Hildenbrand

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
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[7d1086d320...](https://github.com/vampirebat74/lobotomy-corp13/commit/7d1086d320eb137661780e0acecec03a7d016aa3)
#### Tuesday 2023-08-08 23:56:51 by Mr.Heavenly

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

---

