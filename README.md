## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-29](docs/good-messages/2022/2022-06-29.md)


1,647,129 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,647,129 were push events containing 2,468,586 commit messages that amount to 181,082,676 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 17 messages:


## [vicirdek/psychonaut](https://github.com/vicirdek/psychonaut)@[707fbfac7e...](https://github.com/vicirdek/psychonaut/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Wednesday 2022-06-29 00:28:15 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [gitstart/metabase](https://github.com/gitstart/metabase)@[9c4e73899e...](https://github.com/gitstart/metabase/commit/9c4e73899e8914fd41e85987d4a652a9b6058d8a)
#### Wednesday 2022-06-29 04:18:38 by dpsutton

Enterprise settings (#23441)

* Allow for disabling settings

Disabled settings will return their default value (else nil if no
default is set). This allows us to have enterprise override settings and
use them from regular OSS code without classloaders, extra vars,
remembering to check if the feature is enabled, etc.

Motivating examples are the appearance settings. We allow
`application-font` setting to change the font of the application. This
is an enterprise feature, but anyone can post to
`api/setting/application-font` and set a new value or startup as
`MB_APPLICATION_FONT=comic-sans java -jar metabase.jar` and have the
functionality.

Same thing for application colors in static viz. The calling code just
calls `(settings/application-colors)` and uses them but doesn't check if
the enterprise settings are enabled. To do this correctly, you have to
remember to implement the following onerous procedure:

A whole namespace for a setting
```clojure
(ns metabase-enterprise.embedding.utils
  (:require [metabase.models.setting :as setting :refer [defsetting]]
            [metabase.public-settings :as public-settings]
            [metabase.public-settings.premium-features :as premium-features]
            [metabase.util.i18n :refer [deferred-tru]]))

(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :getter (fn []
            (when (premium-features/hide-embed-branding?)
              (or (setting/get-value-of-type :string :notification-link-base-url)
                  (public-settings/site-url)))))
```

And then in the calling code you have to do the procedure to
conditionally require it and put it behind a var that can handle it
being nil:

```clojure
;; we want to load this at the top level so the Setting the namespace defines gets loaded
(def ^:private site-url*
  (or (u/ignore-exceptions
        (classloader/require 'metabase-enterprise.embedding.utils)
        (resolve 'metabase-enterprise.embedding.utils/notification-link-base-url))
      (constantly nil)))

;; and then the usage
(defn- site-url
  "Return the Notification Link Base URL if set by enterprise env var, or Site URL."
  []
  (or (site-url*) (public-settings/site-url)))
```

Far nicer to just place the following into the regular public-settings
namespace:

```clojure
(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :enabled?    premium-features/hide-embed-branding?)
```

Then no need for a custom namespace to hold this setting, no need to
have an extra var to point to the setting else a fallback value.

Note that this feature is not required on every enterprise feature we
have. We a namespace `metabase-enterprise.sso.integrations.sso-settings`
that has 24 settings in it, all of which are enterprise features. But
these features are used in our enterprise sso offerings and are directly
referenced from the enterprise features. No need for the extra var to
point to them and the flag checks happen in other parts.

* Mark the UI/UX customization settings as requiring whitelabeling

Mark the following settings as requiring
premium-settings/enable-whitelabeling? (aka token check)

- application-name
- loading-message (override of "doing science")
- show-metabot (override of showing our friendly metabot)
- application-colors
- application-font
- application-logo-url
- application-favicon-url

Updates the helper functions for colors to use the setting rather than
feeling entitled to use a lower level `setting/get-value-of-type`. We
need the higher level api so it takes into account if its enabled or
not.

* Move notification-link-base-url into regular settings with enabled?

* Cleanup ns

---
## [kyanagi/melpa](https://github.com/kyanagi/melpa)@[570bde6b4b...](https://github.com/kyanagi/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Wednesday 2022-06-29 05:07:42 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[84c63a66cb...](https://github.com/newstools/2022-new-york-post/commit/84c63a66cb3451354da7c2784110a21c53596b1d)
#### Wednesday 2022-06-29 05:14:57 by Billy Einkamerer

Created Text For URL [nypost.com/2022/06/28/i-figured-out-my-boyfriend-was-cheating-from-his-breakfast-order/]

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[4471ee4dfa...](https://github.com/GeoB99/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Wednesday 2022-06-29 08:06:59 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[45a1ddfb52...](https://github.com/treckstar/yolo-octo-hipster/commit/45a1ddfb52b53851a29ac4ffed0d623437a1b531)
#### Wednesday 2022-06-29 11:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [uclouvain/osis-portal](https://github.com/uclouvain/osis-portal)@[797852bc38...](https://github.com/uclouvain/osis-portal/commit/797852bc3880c027afb3be7cb9cc445602d072e9)
#### Wednesday 2022-06-29 11:49:26 by mathieuzen

OSIS-6757 in every life we have some trouble, but when you worry you make it double

=> don't worry be happy

---
## [alphagov/govuk-prototype-kit](https://github.com/alphagov/govuk-prototype-kit)@[0d40cc2786...](https://github.com/alphagov/govuk-prototype-kit/commit/0d40cc2786a4778a583fa8d8abf99b700609fa72)
#### Wednesday 2022-06-29 12:11:06 by Laurence de Bruxelles

Change tests to generate a release archive only once

Use a lockfile to make sure that if the test helper `mkReleaseArchive()`
is called more than once, it won't create more than one
`create-release-archive` process. The behaviour we want is that it all
calls will block until the initial process has finished.

The way I figured to do that was that all calls try and acquire a
lockfile (atomically), if that lockfile is already held that means
another call is already creating the release archive. When the lockfile
is released, the process should have successfully created a release
archive, so no extra work is needed.

Unfortunately, in Node.js it seems there is no way to block waiting for
a lockfile to be released, so we have to rewrite the test utils and all
relevant tests to be asynchronous. To be fair they should have been
asynchronous in the first place, but it was still a very painful
process.

Note that I haven't rewritten the scripts in `cypress/scripts` to use
async functions; without the use of top-level await it was a bit more
effort than I was prepared to do, compounded with the fact that
there doesn't seem to be an easy way to await `child_process.spawn()`
(`util.promisify` doesn't work), and async `child_process.exec()` and
`child_process.execFile()` don't do `stdio: 'inherit'`. Maybe the only
way around it is to use the `execa` library (: Anyway I couldn't be
dealing with that, so now we have to deal with duplication in
`__tests__/util`. There are ...ways... to reduce the duplication
(proper-lockfile does this with its `lib/adapter` module) but they are a
bit magic, and plus it means writing our code using callbacks, which is
just... woof. No.

Anyway as you can tell this is has been a great learning opporunity :')
Just use async the first time and save myself the pain later!!

---
## [sunofang/Foundation-19](https://github.com/sunofang/Foundation-19)@[04d704a78a...](https://github.com/sunofang/Foundation-19/commit/04d704a78ac84cbd9fef3ae3c9c68e9232dfccf1)
#### Wednesday 2022-06-29 12:37:37 by Calyxman

Deletes corporations, gets rid of lion-spelling.

Fuck the old one. It was written by a toddler. And none of these old corporations were removed. Fuck you Lion

---
## [chrisholmes/opentelemetry-ruby](https://github.com/chrisholmes/opentelemetry-ruby)@[45429c7d53...](https://github.com/chrisholmes/opentelemetry-ruby/commit/45429c7d537807aad94003f7568650e4a7dc16d2)
#### Wednesday 2022-06-29 14:10:39 by Andrew Hayworth

Split CI builds by gems at top-level (#1249)

* fix: remove unneeded Appraisals for opentelemetry-registry

It's not actually doing anything, so we skip it.

* ci: remove ci-without-services.yml

We're going to bring back these jobs in the next few commits, but we can delete it right now.

* ci: remove toys/ci.rb

We're going to replicate this in Actions natively, so that we can get
more comprehensible build output.

* ci: replace toys.rb functionality with an explosion of actions + yaml

This replaces the "test it all in a loop" approach that `toys/ci.rb` was
taking, by leveraging some more advanced features of GitHub Actions.

To start, we construct a custom Action (not a workflow!) that can run
all the tests we were doing with `toys/ci.rb`. It takes a few different
inputs: gem to test, ruby version to use, whether or not to do rubocop,
etc. Then, it figures out where in the repo that gem lives, sets up ruby
(including appraisals setup, if necessary), and runs rake tests (and
then conditionally runs YARD, rubocop, etc).

Then, over in `ci.yml`, we list out all of the gems we currently have
and chunk them up into different logical groups:

- base (api, sdk, etc)
- exporters
- propagators
- instrumentation that requires sidecar services to test
- instrumentaiton that doesn't require anything special to test

For most groups, we set up a matrix build of operating systems (ubuntu,
macos, and windows) - except for the "instrumentation_with_services"
group, because sidecar services are only supported on linux.

For each matrix group (gem + os), we then have a build that has multiple
steps - and each step calls the custom Action that we defined earlier,
passing appropriate inputs. Each step tests a different ruby version:
3.1, 3.0, 2.7, or jruby - and we conditionally skip the step based on
the operating system (we only run tests against ruby 3.1 for mac /
windows, because the runners are slower and we can't launch as many at
once).

Notably, we have a few matrix exclusions here: things that wont build on
macos or windows, but there aren't many.

Finally, each group also maintains a "skiplist" of sorts for jruby -
it's ugly, but some instrumentation just doesn't work for our Java
friends. So we have a step that tests whether or not we should build the
gem for jruby, and then the jruby step is skipped depending on the
answer. We can't really use a matrix exclusion here because we don't use
the ruby version in the matrix at all - otherwise we'd have a *huge*
explosion of jobs to complete, when in reality we can actually install +
test multiple ruby versions on a single runner, if we're careful.

The net effect of all of this is that we end up having many different
builds running in parallel, and if a given gem fails we can *easily* see
that and get right to the problem. Builds are slightly faster, too.

The major downsides are:
- We need to add new gems to the build list when we create them.
- We can't cache gems for appraisals, which adds a few minutes onto the
  build times (to be fair, we weren't caching anything before)
- It's just kinda unwieldy.
- I didn't improve anything around the actual release process yet.

Future improvements could be:
- Figuring out how to cache things with Appraisals, because I gave up
  after a whole morning of fighting bundler.
- Dynamically generating things again, because it's annoying to add gems
  to the build matrices.

* feat: add scary warning to instrumentation_generator re: CI workflows

* fix: remove testing change

* ci: Add note about instrumentation_with_services

---
## [brando-soen/CodeWars](https://github.com/brando-soen/CodeWars)@[802a4901a0...](https://github.com/brando-soen/CodeWars/commit/802a4901a0bcd91fc0c28e46cafe115f7c2a4301)
#### Wednesday 2022-06-29 14:50:40 by brando-soen

A Strange Trip to the Market

You're on your way to the market when you hear beautiful music coming from a nearby street performer. The notes come together like you wouln't believe as the musician puts together patterns of tunes. As you wonder what kind of algorithm you could use to shift octaves by 8 pitches or something silly like that, it dawns on you that you have been watching the musician for some 10 odd minutes. You ask, "how much do people normally tip for something like this?" The artist looks up. "It's always gonna be about tree fiddy."

It was then that you realize the musician was a 400 foot tall beast from the paleolithic era! The Loch Ness Monster almost tricked you!

There are only 2 guaranteed ways to tell if you are speaking to The Loch Ness Monster: A) it is a 400 foot tall beast from the paleolithic era; B) it will ask you for tree fiddy.

Since Nessie is a master of disguise, the only way accurately tell is to look for the phrase "tree fiddy". Since you are tired of being grifted by this monster, the time has come to code a solution for finding The Loch Ness Monster. Note that the phrase can also be written as "3.50" or "three fifty".

---
## [alimbaga/dwm](https://github.com/alimbaga/dwm)@[67d76bdc68...](https://github.com/alimbaga/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-06-29 15:07:11 by Chris Down

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
## [TailsFanLOL/TailsFanLOL.github.io](https://github.com/TailsFanLOL/TailsFanLOL.github.io)@[0b7cdba398...](https://github.com/TailsFanLOL/TailsFanLOL.github.io/commit/0b7cdba3987e453bfdfe3af89d925288345af8ba)
#### Wednesday 2022-06-29 16:19:48 by WinDos6.22

We're no strangers to love You know the rules and so do I (do I) A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching, but you're too shy to say it (say it) Inside, we both know what's been going on (going on) We know the game and we're gonna play it And if you ask me how I'm feeling Don't tell me you're too blind to see Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching, but you're too shy to say it (to say it) Inside, we both know what's been going on (going on) We know the game and we're gonna play it I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you

```text
█▓▓▓▓▓▓▓▓▓▓███▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╫▓▓▓▓▓▓▓╫▓▓▓█▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓╫╫▓╬╫╫╫╫╫█╫▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███╫███████▓▓▓▓▓╫▓▓╫╫╫╫╫╫▓▓█▓╫╫
█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓█╫██████▓▓▓▓▓▓▓▓▓╫▓▓██████▓
█▓▓▓██▓▓▓█▓█▓▓▓▓▓██╦K╫░██╫╫████▓▓▓▓▓▓▓▓▓▓▓█▓██████
██▓▓▓██▓█▓██████▓█▓╫░╫░██╫╫█████▓▓▓▓▓█▓▓▓▓█▓▓█████
██████████████████░║▄█▓▌╙╫╫██████▓▓▓███▓▓╬█▓▓█████
██████████████▓▀  »╦▀███U░╠█████▓███▓████▓█▓▓█████
█▓██▓▓▓███████  »»»»░██▌»U╫░╙███▓▓▓█▓▓▓▓▓╫█▓██████
█████████████ » ]»»»░███░░░░»▀██▓▓▓▓▓▓▓▓▓▓█▓██████
████████▓▓▓█H,═"▀»»»Ñ████░▓╦╫Ñ██▓▓▓▓▓▓▓▓╫▓▓╫██████
█████▓▓▓▓▓▓▓▓▄╦╦µ«░▓▓▓╬███░█▓▓██▓▓▓█▓▓╫▓▓▓████████
██▓▓▓████▓▓▓█▓░»╨▄▓▓██████╫█████▓▓▓▓▓▓▓▓▓▓▓█▓█████
▓▓▓▓█▓▓▓▓▓██▓▓░╦░░░╠██████╫╢▓█████████████████████
▓▓▓▓▓▓▓▓▓▓▓█▓▌░╫╫╫╫▐██████▓╫██████████████████████
▓▓▓████▓███We are no strangers to love████████████
▓▓▓██████████╫╫╫╫╫Ü██████▓█H██████████████████████
`

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1af2ab4084...](https://github.com/mrakgr/The-Spiral-Language/commit/1af2ab40846082a17b8546fbcc82847a4cf559b3)
#### Wednesday 2022-06-29 16:28:13 by Marko Grdinić

"6:30am. Let me go to bed. I've been stacking wood for the past few hours. I feel like hurling right now. I went to bed at 1am and did not get a wink of sleep, so I said fuck it all and did the chores. I bet tonight I will sleep like a rock. Let me see if I can get some shut eye.

12:20pm. I am up. I see today is going to be messed up. What I want to do right now is check out the Arcana vid by Flycat. I want to see what he does to get the look. After that I am going to adjust the city scene and put it behind me.

...It is just him doing speed modeling. Nevermind.

https://www.youtube.com/watch?v=FXuReln3XD0
Arcane Style Tutorial Part 1: Hair (Blender 3.0 / EEVEE)

https://youtu.be/FXuReln3XD0?t=945

This is interesting.

https://youtu.be/FXuReln3XD0?t=1025

This is a pretty good hair tutorial.

https://youtu.be/FXuReln3XD0?t=1325

This is nice.

https://youtu.be/FXuReln3XD0?t=1446

I had no idea that the translucent shader gets light from behind.

1pm. https://youtu.be/gG7ZoP3fd1w
Arcane Tutorial Part 2 : Deep Dive Into the Arcane Look and Camera Projections (Blender 3.0 / EEVEE)

I'll leave this for later. Let me have breakfast here.

1:35pm. Done with breakfast, let me have this piece of piece and I will resume.

2:05pm. Enough Legendary Mechanic. Let me watch the video. I am interested in it. After that I am going to deal with the city scene, and properly put it behind me.

2:15pm. https://www.reddit.com/r/OpenAI/comments/u2yuf1/how_much_do_you_think_dalle2_will_cost_per_image/

I am wondering about the costs of DALLE 2, and found this thread. It makes more sense to me at this point to buy these services.

2:20pm. I've been thinking about the scenario of actually hiring an artist, and it would be hard with a programmer's salary. If I have an dedicated artist, and I paid them 60k a year, that would eat up half of my own salary. So I really need an AI to do this for me. If I had enough money it would be viable to train my own model.

Then estimating the cost of this, I can't just look at the raw figures. For example, spending 50k to train my own model might seem huge, but it would still be less than hiring a dedicated artist and would have large benefits.

* An AI could give me any kind of image I want in under a minute as opposed to days to weeks for a human.
* Does not need to be paid recurringly.
* Is actually better than the human arists.
* I'd actually be able to use my programming skills to cultivate this path.
* Would be able to enjoy the stability of having an income versus struggling in poverty for years as an artist.

As time goes on the costs will be lower and lower, while the quality would go up.

I am really being heavily pressured by this. I guess reading the cultivation novels like Reverend Insanity and Legendary Mechanic where they fight with the size of their wallet did point out the parallels between that and the real world situation.

I am pretty much failing at everything due to not having enough resources to make a proper initial investment.

If I go the pure artist route, I actually risk missing the Singularity due to lack of support from other people.

If I had no programming skills whatsoever right now, what I would do here to build up my art skills is start taking low paid comissions. I know that my work is not impressive and that I need more experience. Right now, I am at most a junior level artist. I am just about good enough to look for such roles as an artist. This would allow me to further improve my skills and even pick up drawing on the way.

But being an uber programmer that I am, it makes zero sense for me to pick that path. I am very clear that the money I could make from programming and the money that I could make from art are worlds apart.

Sure, sometimes you get people like Rowling who become billionaires through their art, but hoping for that is like trying to win a lottery.

To even achieve moderate success I need both talent and hard work.

To get where I want to be as an artist, I'd need to dedicate myself to it more.

But the circumstances are telling me to instead dedicate myself to it less and take an alternate path.

2:35pm. Let me finish the video and then I am going to deal with the city scene.

...I said it myself in the realy review - if I could get DALLE 2 I'd actually get a job to be able to afford it.

https://youtu.be/gG7ZoP3fd1w?t=528

This looks quite nice.

I can only regret that I do not have the time to dedicate myself to this fully. But I can't give up programming no matter what.

https://youtu.be/gG7ZoP3fd1w?t=598

I see where this is going. This is an interesting technique.

https://youtu.be/gG7ZoP3fd1w?t=1104

What is this screen grabbing stuff.

2:55pm. I am losing focus, let me stop the video here.

Let me take a short break here while it renders.

3:15pm. It is not going well. Plan B. Why don't I just do the touch up in CSP? It would certainly be easier to do the sunbeams that way I want them there.

First of all, I need to get rid of the forest trees in the background. They tower above the city. I should use the copy stamp tool. I saw that in the Ctrl Alt Paint tutorials, but I am not sure what the equivalent of that is in CSP.

https://tips.clip-studio.com/en-us/articles/3844

Ah here it is.

3:40pm. Cleaning up the trees was easy, but my head is aching as I try to do the rest. I do not feel fit for doing any other art today.

3:50pm. Fuck. It is like 100 C in this room, my head hurts from lack of sleep and I am tired.

https://www.youtube.com/results?search_query=clip+studio+glare

Those experiments with different layers have faded from my mind and I've forgotten how to add glare effects. Using a color layer causes the color underneath to change completely. Let me watch some tutorials as usual.

https://youtu.be/PxKz9qz1_-w?t=146

This is not the problem. The problem is getting it to go all the way to white. I would not mind using gradient maps, but the problem with those is the opacity of the layer. If I start drawing on a normal layer, it goes to white immediatelly. It is a huge pain in the ass.

4:20pm. Yeah, I am an idiot. I could have just used the screen mode, but made the color less saturated. My brain is not working properly. Doing this was actually my plan, but my fiddling around with not in sync with my high level thinking.

At any rate, what I have here looks really good. What I have here looks much better than the fog I did in Blender.

Next up is style transfer.

5:05pm. I've gone over it. Let me post it on Twitter.

It seems I got two extra followers compared to last time. Keep it coming.

5:10pm.

///

I said in the previous post that the city looked too much like an UFO. This bothered me enough to go back and fix things. In Blender, I've gotten rid of the fog, exported the image into CSP, and added the glow effects by hand. This feels a lot more like what I was going for.

I've highlighted the two as my main picks. I feel satisfied with this scene, and I won't be getting back to it.

Now I have a problem. I've realized quite quickly that I am not good at drawing anime characters. Doing stylized work requires a higher level of skill than doing it realistically. Though I enjoy looking at anime illustrations, I have a very loose grasp on how to create them. I am not good at drawing at all, so a plan I've come up to get better it to forget anime and focus on realism. Realism is more work, but it is easier to know whether you are doing a good or bad job of it, so it would be easier to develop skills in such a style. In anime, shading and form can be somewhat arbitrary, and these ambiguities would make it a poor learning target.

My initial impulse was to do some anime heads in Blender, but I've changed my mind. I should be both sculpting and drawing realistic figures in order to really assimilate those fundamentals, afterwards I'd have the foundation to simplify that into the anime style. Right now my skills are not good enough for that.

If I am going to sacrifice something at this point, it should be the anime aesthetic. That is what I've decided, a style is something you attain by optimizing your workflow rather than through imitation anyway.

A second problem that I have, is that I am not sure I have the patience for this kind of development anymore. My art skills are at best at the junior level now. Had I been pursuing an art career, what I would to here is try taking on lowly paid commissions so I get some income while I develop my skills.

If I was a regular guy that is what would make sense, but I actually have both strong talent and high skill in programming, as well as 6.5 years of experience doing it. I have a lot of familiarity with ML as well. I am seriously considering just leaving art up to a NN model.

What is really irreplaceable in my art is the writing. If I could afford it, I wouldn't mind paying an artist and a composer to tackle the other parts. Hiring actual humans is expensive though. Even if I had a high salary over 100k a year doing programming, I'd need to pass half of that to an artist.

Spending something like 50k to train a NN model might seem huge, but if I compare it to how I'd need to pay a human artist to give the equivalent level of service it does not seem too much. The longer time goes on, the better the hardware and the algorithms will get, and the lower the figure to train such a model will be.

Right now, I don't know how much it would cost, for all I know it could be a million, so I am just using the example as a thought exercise. I do not really need to train such a model myself, I should be able to pay to use OpenAI's service until that price to possess such models personally comes to an affordable level. ML companies have the worst business model, they have weak moats and fast deprecation in the value of their property, but while that is bad for them, it is good for me.

Selecting from a pool of 100 AI generated images would sure beat spending a week trying to do it myself. Some people would whine about it not being my own work, but I think of it as being a director. It would leave me time to do writing instead.

My thoughts have started going in that direction, so it is likely I'll look for a programming job, hopefully at some ML focused company for real. But I want to do some sculpting first as well as check out music composition before I do that.

Having to endure poverty as long as I have is not fun, but learning all of this was as stressful as it is. I do not regret spending the time to learn 3d skills at all. Being able to do at least this much gives me a sense of fulfilment as a living being. It is not like I didn't get anything out of it either. Right now I am at least capable of doing covers for my own novels.

///

Let me go with this.

https://twitter.com/Ghostlike/status/1542177545537425408?s=20&t=QZ5s4Rm4NBGmODkCTVpbCg

6:15pm. I haven't done any sculpting today, but this is possibly the best way I could have used the day given gow tired I was. I feel like I've actually recovered a bit at this point.

I just need some time to get my feelings in order.

I've decided to get a job so I can afford better NN models for art, but it is true that I do not want to drop everything either to start applying.

I have a very one track mind, so stressing me out to switch things in the middle. I keep thinking whether I should or should not do this. I should think of art as playing a game, that is the healthiest way to approach it.

Working on big scenes is too much work, but working on a single thing at a time is fine for an amateur such as myself.

I need to leave getting a job and everything else out of mind. Just focus on scultping.

Well, sculpting the bones anyway. What I am going to do is start with a skeleton. I want it for a bad end scene.

I should focus to my limit on just doing that. After that I can decide whether I want to sculpt some male and female bodies. I'll do this for as long as I feel like. Then I will take a look at music. Then, I will get a job so I can train the next gen of DALLE.

6:25pm. I want to do this so I should do it.

Forget anime, trying to grind that crap will only lead to a bad result in the end. With sculpting I can put in effort and get something I can be proud off in the end. It is better to have high quality realism than low quality stylization.

I should pursue that which I can be good at."

---
## [QWERTYghri/hoiStyleGame](https://github.com/QWERTYghri/hoiStyleGame)@[99c97642e7...](https://github.com/QWERTYghri/hoiStyleGame/commit/99c97642e7e738dd3a1765ac2370723bf950a09a)
#### Wednesday 2022-06-29 18:40:06 by QWERTYbae

Made changes to the header files again

I fucking hate the config shit

---
## [interactions-py/autosharder](https://github.com/interactions-py/autosharder)@[d0a7232a2d...](https://github.com/interactions-py/autosharder/commit/d0a7232a2dea87ad8df3827b3c5a9b7803047dc8)
#### Wednesday 2022-06-29 19:31:09 by EdVraz

fuck you <@709135116819103865> for making me do this it is hell

---
## [amir73il/linux](https://github.com/amir73il/linux)@[98872a41ca...](https://github.com/amir73il/linux/commit/98872a41caff2e569b1b008bb91e75e6d30f9a36)
#### Wednesday 2022-06-29 21:49:36 by Dave Chinner

xfs: logging the on disk inode LSN can make it go backwards

commit 32baa63d82ee3f5ab3bd51bae6bf7d1c15aed8c7 upstream.

When we log an inode, we format the "log inode" core and set an LSN
in that inode core. We do that via xfs_inode_item_format_core(),
which calls:

	xfs_inode_to_log_dinode(ip, dic, ip->i_itemp->ili_item.li_lsn);

to format the log inode. It writes the LSN from the inode item into
the log inode, and if recovery decides the inode item needs to be
replayed, it recovers the log inode LSN field and writes it into the
on disk inode LSN field.

Now this might seem like a reasonable thing to do, but it is wrong
on multiple levels. Firstly, if the item is not yet in the AIL,
item->li_lsn is zero. i.e. the first time the inode it is logged and
formatted, the LSN we write into the log inode will be zero. If we
only log it once, recovery will run and can write this zero LSN into
the inode.

This means that the next time the inode is logged and log recovery
runs, it will *always* replay changes to the inode regardless of
whether the inode is newer on disk than the version in the log and
that violates the entire purpose of recording the LSN in the inode
at writeback time (i.e. to stop it going backwards in time on disk
during recovery).

Secondly, if we commit the CIL to the journal so the inode item
moves to the AIL, and then relog the inode, the LSN that gets
stamped into the log inode will be the LSN of the inode's current
location in the AIL, not it's age on disk. And it's not the LSN that
will be associated with the current change. That means when log
recovery replays this inode item, the LSN that ends up on disk is
the LSN for the previous changes in the log, not the current
changes being replayed. IOWs, after recovery the LSN on disk is not
in sync with the LSN of the modifications that were replayed into
the inode. This, again, violates the recovery ordering semantics
that on-disk writeback LSNs provide.

Hence the inode LSN in the log dinode is -always- invalid.

Thirdly, recovery actually has the LSN of the log transaction it is
replaying right at hand - it uses it to determine if it should
replay the inode by comparing it to the on-disk inode's LSN. But it
doesn't use that LSN to stamp the LSN into the inode which will be
written back when the transaction is fully replayed. It uses the one
in the log dinode, which we know is always going to be incorrect.

Looking back at the change history, the inode logging was broken by
commit 93f958f9c41f ("xfs: cull unnecessary icdinode fields") way
back in 2016 by a stupid idiot who thought he knew how this code
worked. i.e. me. That commit replaced an in memory di_lsn field that
was updated only at inode writeback time from the inode item.li_lsn
value - and hence always contained the same LSN that appeared in the
on-disk inode - with a read of the inode item LSN at inode format
time. CLearly these are not the same thing.

Before 93f958f9c41f, the log recovery behaviour was irrelevant,
because the LSN in the log inode always matched the on-disk LSN at
the time the inode was logged, hence recovery of the transaction
would never make the on-disk LSN in the inode go backwards or get
out of sync.

A symptom of the problem is this, caught from a failure of
generic/482. Before log recovery, the inode has been allocated but
never used:

xfs_db> inode 393388
xfs_db> p
core.magic = 0x494e
core.mode = 0
....
v3.crc = 0x99126961 (correct)
v3.change_count = 0
v3.lsn = 0
v3.flags2 = 0
v3.cowextsize = 0
v3.crtime.sec = Thu Jan  1 10:00:00 1970
v3.crtime.nsec = 0

After log recovery:

xfs_db> p
core.magic = 0x494e
core.mode = 020444
....
v3.crc = 0x23e68f23 (correct)
v3.change_count = 2
v3.lsn = 0
v3.flags2 = 0
v3.cowextsize = 0
v3.crtime.sec = Thu Jul 22 17:03:03 2021
v3.crtime.nsec = 751000000
...

You can see that the LSN of the on-disk inode is 0, even though it
clearly has been written to disk. I point out this inode, because
the generic/482 failure occurred because several adjacent inodes in
this specific inode cluster were not replayed correctly and still
appeared to be zero on disk when all the other metadata (inobt,
finobt, directories, etc) indicated they should be allocated and
written back.

The fix for this is two-fold. The first is that we need to either
revert the LSN changes in 93f958f9c41f or stop logging the inode LSN
altogether. If we do the former, log recovery does not need to
change but we add 8 bytes of memory per inode to store what is
largely a write-only inode field. If we do the latter, log recovery
needs to stamp the on-disk inode in the same manner that inode
writeback does.

I prefer the latter, because we shouldn't really be trying to log
and replay changes to the on disk LSN as the on-disk value is the
canonical source of the on-disk version of the inode. It also
matches the way we recover buffer items - we create a buf_log_item
that carries the current recovery transaction LSN that gets stamped
into the buffer by the write verifier when it gets written back
when the transaction is fully recovered.

However, this might break log recovery on older kernels even more,
so I'm going to simply ignore the logged value in recovery and stamp
the on-disk inode with the LSN of the transaction being recovered
that will trigger writeback on transaction recovery completion. This
will ensure that the on-disk inode LSN always reflects the LSN of
the last change that was written to disk, regardless of whether it
comes from log recovery or runtime writeback.

Fixes: 93f958f9c41f ("xfs: cull unnecessary icdinode fields")
Signed-off-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Amir Goldstein <amir73il@gmail.com>

---

