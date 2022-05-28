## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-27](docs/good-messages/2022/2022-05-27.md)


1,701,809 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,701,809 were push events containing 2,641,195 commit messages that amount to 173,320,647 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[20e4add487...](https://github.com/san7890/bruhstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Friday 2022-05-27 00:01:07 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[f6cc7f575c...](https://github.com/cockroachdb/cockroach/commit/f6cc7f575cd374982752af6909d3efa96908c3dd)
#### Friday 2022-05-27 00:05:57 by craig[bot]

Merge #81409

81409: bazel: upgrade to rules_nodejs 5.4.2 r=rickystewart,nathanstilwell,laurenbarker a=sjbarag

Please forgive the massive second commit — there's very few valid states in this progression, as building, linting, and testing either work or they don't.  There's not much sense in intentionally leaving commits around that won't build in my opinion, as it makes bisecting extremely frustrating.  If anyone disagrees, let me know and I can keep digging for an intermediate state!

----

Upgrading to Bazel's rules_nodejs 5.x exposed a flaw in our previous Bazel integration: because rules_nodejs explicitly doesn't support yarn's "workspaces" feature [1] (in which common dependencies are hoisted to the lowest common parent directory), any NPM dependencies with different major versions between db-console and cluster-ui would
get flattened to a single version. This left one of those packages using an unsupported (and un-requested) version of a dependency. Removing the yarn workspace layout and using separate Bazel repositories for each JS project ensured each project received the correct dependencies, but revealed incompatibilities with the requested versions. Upgrade rules_nodejs to the latest released version, remove yarn workspaces from the pkg/ui/ tree, and fix all revealed compatibility issues.

Co-authored-by: Sean Barag <barag@cockroachlabs.com>

---
## [Kapu1178/tgstation](https://github.com/Kapu1178/tgstation)@[e37591540b...](https://github.com/Kapu1178/tgstation/commit/e37591540b2620b7ad2a2b61734634d848e8eba2)
#### Friday 2022-05-27 00:29:14 by san7890

[MDB Ignore] OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN (#67324)

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

---
## [swordcube/FNF-Crystal-Engine](https://github.com/swordcube/FNF-Crystal-Engine)@[2235b7957b...](https://github.com/swordcube/FNF-Crystal-Engine/commit/2235b7957bfdee712d36b4c2ff8ef4e5817cfd86)
#### Friday 2022-05-27 01:21:05 by swordcube

rename ModAssets to AssetsManager because fuck you

---
## [LightFire53/Paradise](https://github.com/LightFire53/Paradise)@[ab7a358506...](https://github.com/LightFire53/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Friday 2022-05-27 01:56:50 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [bobbyvivian/beebeean](https://github.com/bobbyvivian/beebeean)@[485f134841...](https://github.com/bobbyvivian/beebeean/commit/485f134841020c1ee9340127acc02210abb76c38)
#### Friday 2022-05-27 02:10:43 by Vivian Teo

FINALLY FIGURED OUT THE HITTING BOUNDARIES ON TOP OMG IM SO GOOD I WANNA CRY LIKE FINALLY I FINALLY DID IT HOLY SHIT now it no longer goes into ceiling

---
## [clayne/git](https://github.com/clayne/git)@[bdaf1dfae7...](https://github.com/clayne/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Friday 2022-05-27 04:48:09 by Tao Klerks

branch: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local topic branch from an existing
remote branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the upstream tracking branch.

When the user pushes with a default "git push", with the intention of
pushing their (new) topic branch to the remote, they get an error, and
(amongst other things) a suggestion to run "git push origin HEAD".

If they follow this suggestion the push succeeds, but on subsequent
default pushes they continue to get an error - so eventually they
figure out to add "-u" to change the tracking branch, or they spelunk
the push.default config doc as proposed and set it to "current", or
some GUI tooling does one or the other of these things for them.

When one of their coworkers later works on the same topic branch,
they don't get any of that "weirdness". They just "git checkout
feature1" and everything works exactly as they expect, with the shared
remote branch set up as remote tracking branch, and push and pull
working out of the box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

An experienced git user might say "well yeah, that's what it means to
have the remote tracking branch set to origin/master!" - but the
original user above didn't *ask* to have the remote master branch
added as remote tracking branch - that just happened automatically
when they branched their feature branch. They didn't necessarily even
notice or understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the topic branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make this "branches have the same name locally as on the remote"
workflow less painful / more obvious by introducing a new
branch.autosetupmerge option called "simple", to match the same-name
"push.default" option that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

Update the error displayed when the 'push.default=simple' configuration
rejects a mismatching-upstream-name default push, to offer this new
branch.autosetupmerge option that will prevent this class of error.

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Also extend the existing branch tests with three new cases testing
this option - the obvious matching-name and non-matching-name cases,
and also a non-matching-ref-type case. The matching-name case needs to
temporarily create an independent repo to fetch from, as the general
strategy of using the local repo as the remote in these tests
precludes locally branching with the same name as in the "remote".

Signed-off-by: Tao Klerks <tao@klerks.biz>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [elexis-eu/lexonomy](https://github.com/elexis-eu/lexonomy)@[7bec680c11...](https://github.com/elexis-eu/lexonomy/commit/7bec680c11ca07746cce40daf280c3257f09116b)
#### Friday 2022-05-27 06:14:33 by KCMertens

Rewrite dictionary indexing, entry read+write

There are a lot of changes in this commit, but most are just noise due to some added type checking.

1. The database
The database has had a refactor.
- Remove the needs_refac, needs_resave and needs_refresh columns, added needs_update as a more generic column
- Add flag column. Defaults to empty string. The flag is still kept in the XML as well (because of interop with old dictionaries and because this way we can ectract existing flags when users upload a new dictionary - assuming they conform to our way of doing things)

2. Entry creation/update
This is completely rewritten.
The core entry point is now ops.createEntry(), this is always used, whenever an entry is created or updated.
With the help of some util functions the entry is completely validated and resaved every time (because the user can do whatever they want to the xml, even completely change it).
This also makes it so that whenever any config has changed we just re-run this function for every entry and everything out of date property fixes itself.

3. Subentries
The subentry system has had some changes:
Previously:
- The subentry would be a complete instance, meaning all the subentry's xml would be contained in every parent entry.
- On load by the client, the subentry was surrounded with <lxnm:subentryParent>, which the client detected.
- On save: the <lxnm:subentryParent> was removed again and the subentry copied and saved in the database. Additionally all other parents of the subentry were updated with the subentry's new xml.
This had some limitations, most importantly all xml extraction functions (for title, sortkey, flag, etc) would also match inside subentries, because they were part of the same xml tree.

The new situation:
- XML of subentries is now removed from the parentEntry, and instead a single reference/link placeholder element is inserted before it is saved to the database.
I've chosen to re-use <lxnm:subentryParent id="..."> for this. The id attributes points to a regular entry in the database that contains the subentry. There is no difference in how a subentry is treated from a normal entry otherwise.
- Subentries can be edited separately, and the parents will never need an update unless the subentry is completely deleted.
- **The client needs an update to retrieve the subentry's xml separately**

Previously a subentry was just a specific element name/tag.
However now it is also possible to specify that the element needs a certain attribute to be considered a subentry.
This was required to support newer formats such as TEI-lex0, where a subentry is just an <entry type="relatedEntry>, which we otherwise can't differentiate from a normal <entry>.
This can be configured in the subbing page. It's possible to require just that a certain attribute exists, or require that the attribute exist and also has a specific value.

4. Flagging:
Flags are now also put in a database columnn. For the rest, there are no changes, flags are still keps in sync with the entry's XML, but this removes the need to parse every entry when loading the entry list.

5. Migration:
There is a migration script website/migrate.py which will migrate every dictionary's database schema.
Dictionaries that use one of the rewritten features (flagging, subentries) will have every entry marked as needs_update, which will run when they are first loaded.
NOTE: This is unfortunate, but the first load of the dictionary will be tremendously slow as all entries might need to be updated before the entrylist can be shown.

6. Other notes:
I've attempted to consolidate most of the entry functions.
ops.searchEntries() can search entries by their headword/searchables. It only uses and returns the IDs and Sortkeys, so results can be further used as needed.
ops.sortEntries() can sort the results of searchEntries based on collator and reverse settings
ops.readEntries() actually reads and processes the entries. It has some flags to retrieve xml, parse xml, extract plaintext title, or run xslt/html conversion (because those are heavy operations and you might not always need their result).
	The returned results are ready to send to the frontend.
	It also retrieves the entry's child- and parentEntry IDs, so returns their subentries, or - when it is a subentry itself - where it is used.

---

XML parsing is a headache - especially when cutting up larger documents, and namespace issues crop up because the declaration is lost.
ops.parse() parses xml in a straightforward manner - it pretty much ignores namespaces, and just treats a namespace as if the element or attribute was literally called "someNamespace:someElement".
This means that to match inside the result, you need to specify the namespace prefix inside the attribute/element name.

---

Importing a dictionary is also mostly rewritten because it could not handle elements being nested inside themselved, as the regex would match up wrong.
Ex:
<entry>
	...
	<entry type="relatedEntry"> <!-- actually a subentry -->
	</entry>
</entry>
would previously match up the opening tag with the subentry closing tag and horribly crash because of unbalanced tags.

---

I've also attempted to include type information as much as possible, and codified most of the configs used in the back-end.
This requires Python 3.8, but I very strongly think the developer quality-of-life we get back is worth it.

---
## [petre-symfony/easy-admin-symfonycasts](https://github.com/petre-symfony/easy-admin-symfonycasts)@[1ef542330b...](https://github.com/petre-symfony/easy-admin-symfonycasts/commit/1ef542330b580fefba492a2baef9b410c174cdfc)
#### Friday 2022-05-27 06:14:59 by petrero

38.3. A Global "Export" Action

  How's that for a great name? The "goodby-csv" library is a well-known CSV package... but it hasn't been updated for a while. So "handcraftedinthealps" forked it and made it work with modern versions of PHP. Super helpful!

  If you downloaded the course code, you should have a tutorial/ directory with a CsvExporter.php file inside. Copy that... and then, in your src/Service/ directory, paste. This will handle the heavy lifting of creating the CSV.

  At the bottom, this returns a StreamedResponse (that's a Symfony response)... that contains the file download with the CSV data inside. I won't go into the specifics of how this works... it's all related to the package we installed.

  To call this method, we need to pass it three things: the QueryBuilder that should be used to query for the results, the FieldCollection (this comes from EasyAdmin and holds the fields to include), and also the filename that we want to use for the download. In QuestionCrudController, create that export() action: public function export().

  Reusing the List Query Builder
  - Ok, step 1 is to create a QueryBuilder. We could simply inject the QuestionRepository, make a QueryBuilder... and pass that to CsvExporter. But we're going to do something a bit more interesting... and powerful.

  When we click the "Export" button, I want to export exactly what we see in this list, including the current order of the items and any search parameter we've used to filter the results. To do that, we need to steal some code from our parent class. Scroll up to the top of the controller... and then hold "cmd" or "ctrl" to open AbstractCrudController. Inside, search for "index". There it is.

  So index() is the action that renders the list page. And we can see some logic about how it makes its query. We want to replicate that. Specifically, we need these three variables: this is where it figures out which fields to show, which filters are being applied, and ultimately, where it creates the QueryBuilder. Copy those... go back to our export() action, and paste. I'll say "Okay" to add a few use statements.

  To get this to work, we need a $context. That's the AdminContext which, as you probably remember, is something we can autowire as a service into our methods. Say AdminContext... but this time, call it $context. Awesome!

  At this point, we have both the QueryBuilder and the FieldCollection that we need to call CsvExporter. So... let's do it! Autowire CsvExporter $csvExporter... then, at the bottom, it's as simple as return $csvExporter->createResponseFromQueryBuilder() passing $queryBuilder, $fields, and then the filename. How about, questions.csv

  Let's try it! Refresh... hit "Export" and... I think it worked! Let me open that up. Beautiful! We have a CSV of all of our data!

  Forwarding Ordering & Filtering Query Params to the Action
  - But... there is one hidden problem. Notice the ordering of these items. In the CSV file... it seems like they're in a random order. But if we look at the list in the browser, these are ordered by ID! Try searching for something. Cool. 7 results. But if we export again... and open it... uh oh! We get the same long list of results! So the Search in the CSV export isn't working either!

  The problem is this: the search term and any ordering that's currently applied is reflected in the URL via query parameters. But when we press the "Export" button, we only get the basic query parameters, like which CRUD controller or action is being called. We do not also get the filter, search, or order query parameters. So then, when we get the $queryBuilder and $filter, the parameters aren't there to tell EasyAdmin what filtering and ordering to do!

---
## [petre-symfony/easy-admin-symfonycasts](https://github.com/petre-symfony/easy-admin-symfonycasts)@[ca0096c721...](https://github.com/petre-symfony/easy-admin-symfonycasts/commit/ca0096c721aefd2934eff2314ff8b4f61f4e2aae)
#### Friday 2022-05-27 06:14:59 by petrero

40.5. Form Panels

  Fixing the Icon on the Tab
  - Oh, and we also lost our icon! We added an fa fa-info icon... but it's not showing! Or is it? If you look closely, there's some extra space. Inspect element on that. There is an icon! But... it looks... weird. It has an extra fa-fa for some reason.

  We can fix this by changing the icon to, simply, info. This is... sort of a bug. Or, it's at least inconsistent. When we use tabs, EasyAdmin adds the fa- for us. So all we need is info. Watch: when I refresh... there! fa-info... and now the icon shows up!

  Form Columns
  - The last thing we can do, instead of having this long list of fields, is to put the fields next to each other. We do this by controlling the columns on this page.

  To show this off, move the name field above slug. Yup, got it. And now let's see if we can put these fields next to each other. We're using bootstrap, which means there are 12 invisible columns on each page. So, on name, say ->setColumns(5)... and on slug, do the same thing: ->setColumns(5).

  We could use 6 to take up all of the space, but I'll stick with 5 and give it some room. Refresh now and... very nice! The fields float next to each other. This is a great way to help this page... make a bit more sense.

  And... that's it, friends! We are done! This was fun! We should do it again sometime. I love EasyAdmin, and we here at SymfonyCasts are super proud of the admin section we built with it... which includes a lot of custom stuff. Let us know what you're building! And as always, we're here for you down in the Comments section with any questions, ideas, or delicious recipes that you might have.

  All right friends, see you next time!

---
## [petre-symfony/easy-admin-symfonycasts](https://github.com/petre-symfony/easy-admin-symfonycasts)@[93c5e04186...](https://github.com/petre-symfony/easy-admin-symfonycasts/commit/93c5e041866cf11149aaaeb09d5836052e516b15)
#### Friday 2022-05-27 06:14:59 by petrero

39.3. Linking to EasyAdmin from Twig

  Adding a Link to the Admin From Twig
  - At this point, we know how to generate a link to any EasyAdminBundle page. If I scroll up a bit... the key is to get the AdminUrlGenerator, and then set whatever you need on it, like the action and CRUD controller.

  Go to the Homepage... and click into a question. To make life easier for admin users, I want to put an "Edit" button that takes us directly to the edit action for this specific question. So... how do we generate URLs to EasyAdmin from Twig?

  Open the template for this page - templates/question/show.html.twig - and find the <h1>. Here it is. For organization, I'll wrap this in a <div> with class="d-flex justify-content-between".

  After the h1, add the link... but only for admin users. So {% if is_granted('ROLE_ADMIN') %}... and {% endif %}. Inside <a href=""> - I'll leave the href empty for a moment - with class="text-white". And inside of that, a <span class="fa fa-edit">.

  Back in our browser, try that. And... hello edit link!

  To generate the URL, we need to tell EasyAdmin which CRUD controller, action, and entity ID to use... all stuff we've done in PHP. In Twig, it's nearly the same thing thanks to a shortcut function called ea_url().

  This gives us the AdminUrlGenerator object. And so, we can just... call the normal methods, like .setController()... passing the long controller class name. We have to use double slashes so that they don't get escaped, since we're inside of a string. Now add .setAction('edit') and .setEntityId(question.id).

  It's a little weird to write this kind of code in Twig, but that's how it's done! Back over here, refresh... and try the button. Got it!

  Ok team, last topic! Let's talk about how we can leverage layout panels and other goodies to organize our form into groups, rows, or even tabs on this form page.

---
## [petre-symfony/easy-admin-symfonycasts](https://github.com/petre-symfony/easy-admin-symfonycasts)@[3ee8e0f6b2...](https://github.com/petre-symfony/easy-admin-symfonycasts/commit/3ee8e0f6b222d842021ad888123054b247a5894c)
#### Friday 2022-05-27 06:14:59 by petrero

38.1. A Global "Export" Action

  There are actually three different types of actions in EasyAdmin. The first consists of the normal actions, like Add, Edit, Delete, and Detail. These operate on a single entity. The second type is batch actions, which operate on a selection of entities. For example, we can click two of these check boxes and use the Delete button up here. That is the batch Delete, and it's the only built-in batch action.

  Side note: to make sure approved questions aren't deleted - which is work we just finished, you should also remove the batch Delete action for the Question crud. Otherwise, people might try to batch Delete questions. That won't work... thanks to some code we wrote, but they'll get a very-unfriendly 500 error.

  Anyways, the third type of action is called a "global action", which operates on all the entities in a section. There are no built-in global actions, but we're going to add one: a button to "export" the entire questions list to a CSV file.

  Creating the Global Action
  - For the most part, creating a global action... isn't much different than creating a normal custom action. It starts the same. Over in the actions config, create a new $exportAction = Action::new() and call it export. Below, we'll ->linkToCrudAction() and also call it export. Then, add some CSS classes... and an icon. Cool. We're ready to add this to the index page: ->add(Crud::PAGE_INDEX, $exportAction) to get that button on the main list page.

  If we stopped now, this would be a normal action. When we refresh... yup! It shows up next to each item in the list. Not what we wanted.

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[5a8037da67...](https://github.com/ammarfaizi2/linux-block/commit/5a8037da67d89bf2d38ea7bd36b2b0792d288598)
#### Friday 2022-05-27 06:31:21 by Jason A. Donenfeld

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
## [NotActuallyTerry/DiscordReddit](https://github.com/NotActuallyTerry/DiscordReddit)@[3ae50c6261...](https://github.com/NotActuallyTerry/DiscordReddit/commit/3ae50c626196d345efcf48fe92fbc327e4cfb6d7)
#### Friday 2022-05-27 07:08:33 by Ike Johnson-Woods

Rewrite from near-scratch
Fuck you it's all one commit

---
## [Etaiva/Etaiva](https://github.com/Etaiva/Etaiva)@[e014876385...](https://github.com/Etaiva/Etaiva/commit/e01487638534add687422d577d7bccaebc8fb414)
#### Friday 2022-05-27 07:43:09 by Etienne Pretorius

Create data bio 2

My name is Etienne. I was referred here by Maggie Wolff (Thanks Maggie). I follow Maggie on a number of social media because her career switch to data science got my attention, and she just makes sense when publishing material. I have advanced MS Excel skills, I am learning SQL and will progress to other languages in time, I have fundamental exposure to statistics skills. I have +20 years corporate management experience in manufacturing operations. In that role I have performed regular business analysis in both business environments and lean manufacturing, with some six sigma exposure. I currently function as a freelancer in technical writing, and storyboarding to instructional designers and sme's; and, I am a director in PBC Group http://www.pbcgroup.co.za based in Johannesburg South Africa. PBC Group (Pty) Ltd offers business services, legal services and learning services. All this said to justify not having a formal qualification in science, data or engineering, albeit my qualifications are all business related (viewed on my LinkedIn https://www.linkedin.com/in/etienne-pretorius/). I want to connect with like minded people such as the people on this network. Looking forward to some 121's online and networking on this platform. Kind regards from Johannesburg, the trading house into South Africa.

---
## [Etaiva/Etaiva](https://github.com/Etaiva/Etaiva)@[93d27f133c...](https://github.com/Etaiva/Etaiva/commit/93d27f133c8040956928bd9d2d661e5f75401159)
#### Friday 2022-05-27 07:44:41 by Etienne Pretorius

Delete data bio 2

My name is Etienne. I was referred here by Maggie Wolff (Thanks Maggie). I follow Maggie on a number of social media because her career switch to data science got my attention, and she just makes sense when publishing material. I have advanced MS Excel skills, I am learning SQL and will progress to other languages in time, I have fundamental exposure to statistics skills. I have +20 years corporate management experience in manufacturing operations. In that role I have performed regular business analysis in both business environments and lean manufacturing, with some six sigma exposure. I currently function as a freelancer in technical writing, and storyboarding to instructional designers and sme's; and, I am a director in PBC Group http://www.pbcgroup.co.za/ based in Johannesburg South Africa. PBC Group (Pty) Ltd offers business services, legal services and learning services. All this said to justify not having a formal qualification in science, data or engineering, albeit my qualifications are all business related (viewed on my LinkedIn https://www.linkedin.com/in/etienne-pretorius/). I want to connect with like minded people such as the people on this network. Looking forward to some 121's online and networking on this platform. Kind regards from Johannesburg, the trading house into South Africa.

---
## [shdeep15/gate](https://github.com/shdeep15/gate)@[e2a108db75...](https://github.com/shdeep15/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Friday 2022-05-27 09:23:11 by Chris Phillips

fix(authn/oauth2): prevent oauth2 redirect loops (#1517)

During setup of spinnaker authentication with oauth2 a common hurdle is a redirect loop.

For example:

https://github.com/spinnaker/spinnaker/issues/5794
https://github.com/spinnaker/spinnaker/issues/1630

Also, many threads in Slack discuss these problems. In fact this appears to be a common
pitfall for the spring-security-oauth2-autoconfigure library in general. A light refresher
on the ouath2 flow in play here seems worthwhile. The user is redirected from `/login` in gate
to the external auth provider (google, github, etc.) and after successfully authenticating
they are redirected back to the gate `/login` endpoint but this time with a code parameter
that is to be used to request an access token.

This request can fail for a variety of reasons, and if it does, the underlying spring library
triggers a redirect to the `/error` endpoint. What causes the redirect loop for gate in particular
(and for other users of the library in a similar fashion) is that the WebSecurityConfigurerAdapter
in play is treating `/error` as an authenticated path and so instead of just returning with a 401,
it re-redirects to `/login` and the redirect loop continues.

My thought is that instead of a redirect loop, simply allowing the 401 to be returned will be a stronger
more helpful signal as to what is going on. Hopefully it will save future first-time installers headaches.

Spinnaker docs have included several troubleshooting hints and tips for how where you terminate SSL
affects configuration etc. Even after following all of these and lots of spelunking through spinnaker
github issues and combing over threads in slack, I found myself still experiencing a redirect loop even
though I had applied all the combined wisdom that was applicable to my setup.

As it turns out, I had a bad copy/paste of my client secret in my configuration. So the request
to turn the code from google into an access token from google was failing with a 401. After much
debugging and deep diving into the spring security code I found that had I turned on DEBUG in gate
for these classes in gate-local.yml:

```
logging:
  level:
    org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler: DEBUG
    org.springframework.security.oauth2.client.filter.OAuth2ClientAuthenticationProcessingFilter: DEBUG
```

Then I would have seen in the logs that a 401 response was returned from google and perhaps it would have
caused me to look closer at my botched client secret configuration. I think perhaps we don't want to require
that all operators of spinnaker become spring-security-oauth2 experts. So I'm proposing adding `/error` to
the list of paths in gate that aren't treated as authenticated. Thus short-circuiting the redirect loop and
bringing to light helpful troubleshooting info that was previously more or less swallowed.

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[1c851af620...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/1c851af6201f3d90f5da685dda1aee7ee92576d2)
#### Friday 2022-05-27 10:01:02 by petrero

5.1. Symfony Flex: Aliases, Packs & Recipes - composer require templates

  Symfony is a set of libraries that gives us tons of tools: tools for logging, making database queries, sending emails, rendering templates and making API calls, just to name a few. If you counted them, I did, Symfony consists of about 100 separate libraries. Wow!

  Right now, I want to start turning our pages into true HTML pages... instead of just returning text. But we are not going to jam a bunch of HTML into our PHP classes. Yuck. Instead, we're going to render a template.

  Symfony's Start Small & Install Features Philosophy

  Well... Symfony does have a tool for that. But our app currently uses very few of the Symfony libraries. The tools we have so far don't amount to much more than a route-controller-response system. If you need to render a template or make a database query, we do not have those tools installed in our app... yet.

  I actually love this about Symfony. Instead of starting us with a gigantic project, with everything we need, plus tons of stuff that we don't need, Symfony starts tiny. Then, if you need something, you install it!

  But before we install a templating library, at your terminal, run:

    git status
  Let's commit everything:

    git add .
  I can safely run git add . - which adds everything in my directory to git - because one of the files that our project originally came with was a .gitignore file, which already ignores stuff like the vendor/ directory, var/ directory, and several other paths. If you're wondering what these weird marker things are, that's related to the recipe system, which we're about to talk about.

  Anyways, run git commit and add a message:

    git commit -m "route -> controller -> response -> profit"
  Perfect! And now, we are clean.

  Installing a Templating Library (Twig)
  - Okay. So how can we install a templating library? And what templating libraries are even available for Symfony? And which is recommended? Well, of course, a great way to answer these questions would be check the Symfony documentation.

  But we can also just... guess! In any PHP project, you can add new third-party libraries to your app by saying "composer require" and then the package name. We don't know the package name we need yet, so I'll just guess:

    composer require templates
  Now, if you've used Composer before, you might be screaming at your screen right about now! Why? Because in Composer, package names are always something/something. It is literally not possible to have a package just named templates.

  But watch: when we run this, it works! And up on top, it says using version 1 for symfony/twig-pack. Twig is the name of the templating engine for Symfony.

  Flex Aliases
  - To understand this, let's take a tiny step backwards. Our project started with a composer.json file containing several Symfony libraries. One of these is called symfony/flex. Flex is a composer plugin. So it adds more features to composer. Actually, it adds three superpowers to composer.

  Tip

    The flex.symfony.com server was shut down in favor of a new system. But you can still see a list of all of the available recipes at https://bit.ly/flex-recipes!

  The first, which we just saw, is called Flex aliases. Head to https://flex.symfony.com to see a giant page full of packages. Search for "templates". Here it is. Under symfony/twig-pack, it says Aliases: template, templates, twig, and twig-pack.

  The idea between behind Flex aliases is dead simple. We type composer require templates. And then, internally, Flex changes that to symfony/twig-pack. Ultimately, that is the package that Composer installs.

  This means that, most of the time, you can just "composer require" whatever you want, like composer require logger, composer require orm, composer require icecream, whatever. It's just a shortcut system. The important point is that, what really got installed was symfony/twig-pack.

  Flex Packs
  - And that means that, in our composer.json file, we should now see symfony/twig-pack under the require key. But if you spin over, it's not there! Gasp! Instead, it added symfony/twig-bundle, twig/extra-bundle, and twig/twig.

  We're witnessing the second superpower of Symfony Flex: unpacking packs. Copy the original package name and... we can actually find that repository on GitHub by going to https://github.com/symfony/twig-pack.

  And... it contains just one file: composer.json. And this requires three other packages: the three we just saw added to our project.

  This is called a Symfony pack. It's... really just a fake package that helps us install other packages. It turns out, if you want a rich template engine to be added to your app, we recommend installing these three packages. But instead of making you add them manually, you can composer require symfony/twig-pack and get them automatically. When you install a "pack", like this, Flex automatically "unpacks" it: it finds the three packages that the pack depends on and adds those into your composer.json file.

  So, packs are a shortcut so that you can run one composer require command and get multiple libraries added to your project.

  Ok, so what is the third and final superpower of Flex? So glad you asked! To find out, at your terminal, run:

    git status

  Flex Recipes
  - Whoa. Normally when you run composer require, the only files it should modify - other than downloading packages into vendor/ - are composer.json and composer.lock. Flex's third superpower is its recipes system.

  Whenever you install a package, that package may have a recipe. If it does, in addition to downloading the package into the vendor/ directory, Flex will also execute its recipe. Recipes can do things like add new files or even modify a few existing files.

  Watch: if we scroll up a little, ah yes: it says "configuring 2 recipes". So apparently there was a recipe for symfony/twig-bundle and also a recipe for twig/extra-bundle. And these recipes apparently updated the config/bundles.php file and added a new directory and file.

  The recipe system is sweet. All we need to do is composer require a new library and its recipe will then add all the configuration files or other setup needed so that we can start using that library immediately! No more following 5 manual "installation" steps in a README. When you add a library, it works out-of-the-box.

  Next: I want to dive a bit deeper into the recipes. Like, where do they live? What's their favorite color? And what did this recipe added specifically to our app and why? I'm also going to let you in on a little secret: every file on our project - all the files in config/, the public/ directory... all of this stuff - was added via a recipe. And I'll prove it.

---
## [petre-symfony/harmonious-development-with-Symfony6](https://github.com/petre-symfony/harmonious-development-with-Symfony6)@[c0f2d7c6e7...](https://github.com/petre-symfony/harmonious-development-with-Symfony6/commit/c0f2d7c6e7ade8e36953aa76ae3e0e5c954461d4)
#### Friday 2022-05-27 10:01:02 by petrero

6.1. Flex Recipes

  We just installed a new package by running composer require templates. Normally when you do that, Composer will update the composer.json and composer.lock files, but nothing else.

  But when we run:

    git status
  There are other changes. This is thanks to Flex's recipe system. Each time we install a new package, Flex checks a central repository to see if that package has a recipe. And if it does, it installs it.

  Where do Recipes Live?
  - Where do these recipes live? In the cloud... or more specifically GitHub. Check it out. Run:

    composer recipes
  This is a command added to composer by Flex. It lists all of the recipes that have been installed. And if you want more info about one, just run:

    composer recipes symfony/twig-bundle
  This is one of the recipes that was just executed. And... cool! It shows us a couple of nice things! The first is a tree of the files it added to our project. The second is a URL to the recipe that was installed. I'll click to open that.

  Yep! Symfony recipes live in a special repository called symfony/recipes. This is a big directory organized by package name. There's a symfony directory that holds recipes for all packages starting with symfony/. The one we were just looking at... is way down here: twig-bundle. And then there are different versions of the recipe based on your version of the package. We're using the latest 5.4 version.

  Every recipe has a manifest.json file, which controls what it does. The recipe system can only do a specific set of operations, including adding new files to your project and modifying a few specific files. For example, this bundles section tells flex to add this line to our config/bundles.php file.

  If we run git status again... yup! That file was modified. If we diff it:

    git diff config/bundles.php
  It added two lines, probably one for each of the two recipes.

  Symfony Bundles?
  - By the way, config/bundles.php is not a file that you need to think about much. A bundle, in Symfony land, is basically a plugin. So if you install a new bundle into your app, that gives you new Symfony features. In order to activate that bundle, its name needs to live in this file.

  So the first thing that the recipe did for twig-bundle, thanks to this line up here, was to activate itself inside bundles.php... so that we didn't need to do it manually. Recipes are like automated installation.

  New, Copied Files
  - The second section in the manifest is called copy-from-recipe. This is simple: it says to copy the config/ and templates/ directories from the recipe into the project. If we look... the recipe contains a config/packages/twig.yaml file... and also a templates/base.html.twig file.

  Back at the terminal, run git status again. We see these two files at the bottom: config/packages/twig.yaml... and inside of templates/, base.html.twig.

  I love this. Think about it: if you install a templating tool into your app, we're going to need some configuration somewhere that tells that templating tool which directory to look inside of to find our templates. Whelp, go check out that config/packages/twig.yaml file. We're going talk about these Yaml files more in the next tutorial. But on a high level, this file controls how Twig - the templating engine for Symfony - behaves. And check out the default_path key set to %kernel.project_dir%/templates. Don't worry about this percent syntax: that's a fancy way to refer to the root of our project.

  The point is, this config says:

    Hey Twig! When you look for templates, look for them in the templates/ directory.

  And then the recipe even created that directory with a layout file inside. We'll use this in a few minutes.

  symfony.lock & Committing Files
  - The last unexplained file that was modified is symfony.lock. This is not important: it just keeps track of which recipes have been installed... and you should commit it.

  In fact, we should commit all of this stuff. The recipe might give us files, but then they are our's to modify. Run:

    git add .
  Then:

    git status
  Cool. Let's commit!

    git commit -m "Adding Twig and its beautiful recipe"

  Updating Recipes
  - Done! By the way, a few months down the road, there might be changes to some of the recipes that you've installed. And if there are, when you run

    composer recipes
  you'll see a little "update available" next to them. Run composer recipes:update to upgrade to the latest version.

  Oh, and before I forget, in addition to symfony/recipes, there is also a symfony/recipes-contrib repository. So recipes can live in either of these two places. The recipes in symfony/recipes are approved by Symfony's core team, so they're a bit more vetted for quality. Other than that, there's no difference.

  Our Project Started as One File
  - Now, the recipe system is so powerful that every single file in our project was added via a recipe! I can prove it. Go to https://github.com/symfony/skeleton.

  When we originally ran that symfony new command to start our project, what that really did was clone this repository... and then ran composer install inside of it, which downloads everything into the vendor/ directory.

  Yup! Our project - the one that we see right here - was originally just a single file: composer.json. But then, when the packages were installed, the recipes for those packages added everything else we see. Run:

    composer recipes
  again. One recipe is for something called symfony/console. Check out its details:

  composer recipes symfony/console
  - And... yes! The recipe for symfony/console added the bin/console file! The recipe for symfony/framework-bundle - one of the other packages that was originally installed - added almost everything else, including the public/index.php file. How cool is that?

  Okay next: we installed Twig! So let's get back to work and use it to render some templates! You're going to love Twig.

---
## [Gaxeer/tgstation](https://github.com/Gaxeer/tgstation)@[3f18dadd1a...](https://github.com/Gaxeer/tgstation/commit/3f18dadd1a5d654aafc2c37539ff917580bfe0b2)
#### Friday 2022-05-27 10:28:40 by san7890

Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

---
## [demogorgon22/notdnethack](https://github.com/demogorgon22/notdnethack)@[6406d2d4bc...](https://github.com/demogorgon22/notdnethack/commit/6406d2d4bc959480d8f62a86a414dc373e730adc)
#### Friday 2022-05-27 12:59:28 by chris

Add spell bonuses from PC species as well as role.

The base bonus is (spell level+1)/2 * 5. This yeilds bonuses in the vanilla range, but that may be too small to really matter :-/

Humans: Abjuration. They make things mundane
Clockwords: Wizard lock (auto cast). Affinity with mechanical things.
Chiros: Magic Mapping. They know caves.
Dwarves: Digging. They dig.
Drow: Sleep. Affinity with sleeping poison.
Elves: Remove curse. Low-key holy.
Gnomes: Invisibility. They can vanish.
Half-dragons: Detect treasure. Dragons can horde.
Incants: no bonus. Already has a bonus to all spells.
Orcs: Cancellation. Good vs. angels and other mighty foes.
Vampires: Drain life. They drain life.
Yukis: Charm monster. Nymphs.

---
## [eirini-forks/eirini-station](https://github.com/eirini-forks/eirini-station)@[9a36225c6e...](https://github.com/eirini-forks/eirini-station/commit/9a36225c6e4f24c196b1053a2d84abd68c88ec68)
#### Friday 2022-05-27 14:05:40 by Giuseppe Capizzi

Don't store the hostname in ~/.ssh/known_hosts

Given we destroy our machines every night, we don't need to remember the
host. This will save us the annoying warnings and the need to delete
entries from ~/.ssh/known_hosts.

---
## [transcom/mymove](https://github.com/transcom/mymove)@[8af1f5a031...](https://github.com/transcom/mymove/commit/8af1f5a03143dce4ab3c6aa01b8772cd2f41adb9)
#### Friday 2022-05-27 14:22:56 by Marty Boren

Very rough skeleton of move code search

after many moons of struggle, I've finally got something that
kinda works.
There's an endpoint for searching for moves.
and an office page with a search box that hits that endpoint
and drops the results in a table.

i was really struggling to get the react part of this to work without
setting off an infinite loop, so now that I've finally gotten there
i want to commit even though this is still full of debug cruft.

lots of exciting things left to do, such as:
- the moves that are returned by the endpoint are missing most of the
  stuff they should have.
- We also can't search for DoD ID
- interface for passing search info between things is inconsistent

---
## [hexylena/emc-movie-club-bot](https://github.com/hexylena/emc-movie-club-bot)@[a188227dc7...](https://github.com/hexylena/emc-movie-club-bot/commit/a188227dc70d43d9ee3aee889dff25e2652da180)
#### Friday 2022-05-27 14:50:15 by Helena Rasche

dear diary today i remembered how awful data ingress is

---
## [iradukud/Codewars](https://github.com/iradukud/Codewars)@[42e437a47c...](https://github.com/iradukud/Codewars/commit/42e437a47c5e98c0579c0e28aec689e506150ad0)
#### Friday 2022-05-27 15:04:07 by David Iradukunda

Blood-Alcohol_Content

Bob drinks too much, and he gets in trouble for it a lot. He drinks so much, in fact, that he has broken the local law enforcement's breathalizer with his alcoholic breath! Bob feels simply aweful, so he wants to make up for it by creating a function that will calculate his blood-alcohol level for them. Unfortunately, Bob has gotten too inebriated to do any programming today, so he needs your help!

He did manage to research the formula for blood-alcohol content before getting too drunk, which he describes below.

BAC calculator Formula:

BAC% = (A × 5.14 / W × r) - .015 × H

A: Total alcohol consumed, in ounces (oz)
W: Body weight, in pounds (lbs)
r: The alcohol distribution ratio, 0.73 for man, and 0.66 for women
H: Time passed since drinking, in hours
Example
generate_link('matt c')
http://www.codewars.com/users/matt%20c
reference
use this as a reference encoding

---
## [chupAkabRRa/terminal](https://github.com/chupAkabRRa/terminal)@[77215d9d77...](https://github.com/chupAkabRRa/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Friday 2022-05-27 15:12:13 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [DSharpPlus/DSharpPlus](https://github.com/DSharpPlus/DSharpPlus)@[8380b5b2de...](https://github.com/DSharpPlus/DSharpPlus/commit/8380b5b2deb9f2243c87e3277a34902ec08bb716)
#### Friday 2022-05-27 15:26:30 by InFTord

[ci-skip] Fix docs typos in DiscordRestClient (#1317)

* Update DiscordRestClient.cs

* insanity

edited all of this with github site editor
madness
editing 2k lines of code is kinda pain with github site editor

* im idiot

* fixing...

* uh oh

* i love fixing docs

* fixing inconsistent ID stuff..

---
## [andreimatei/cockroach](https://github.com/andreimatei/cockroach)@[ef3db17963...](https://github.com/andreimatei/cockroach/commit/ef3db1796395a3c649f72848315bb7590b74e090)
#### Friday 2022-05-27 15:44:13 by Andrei Matei

util/timeutil: don't strip mono time in timeutil.Now

Our timeutil.Now() insists on returning UTC timestamps, for better or
worse. It was doing this by calling time.Now.UTC(). The rub is that the
UTC() call strips the monotonic clock reading from the timestamp.
Despite repeatedly trying ([1]), I've failed to find any reasonable
reason for that behavior. To work around it, this patch does unsafe
trickery to get a UTC timestamp without stripping the monos.

Stripping the monos has the following downsides:
1. We lose the benefits of the monotonic clock reading.
2. On OSX, only the monotonic clock seems to have nanosecond resolution. If
we strip it, we only get microsecond resolution. Besides generally sucking,
microsecond resolution is not enough to guarantee that consecutive
timeutil.Now() calls don't return the same instant. This trips up some of
our tests, which assume that they can measure any duration of time.
3. time.Since(t) does one less system calls when t has a monotonic reading,
making it twice as fast as otherwise:
https://cs.opensource.google/go/go/+/refs/tags/go1.17.2:src/time/time.go;l=878;drc=refs%2Ftags%2Fgo1.17.2

An alternative considered was setting the process' timezone to UTC in an
init(): time.Local = time.UTC. That has downsides: it makes cockroach
more unpleasant to link as a library, and setting the process timezone
makes the timestamps not roundtrip through marshalling/unmarshalling
(see [1]).

[1] https://groups.google.com/g/golang-nuts/c/dyPTdi6oem8

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[cbfe74af84...](https://github.com/mrakgr/The-Spiral-Language/commit/cbfe74af84aa5c96c5c51026803b74e30512e945)
#### Friday 2022-05-27 17:28:43 by Marko Grdinić

"9:40am. I am up. Let me chill just a bit and then I will start.

9:45am. I watched Spider Verse yesterday. It was genuinely entertaining, but it promotes the kind of morality I aim to oppose.

10:05am. Let me start. I should be able to put away 2 whole days into one if I focus.

One thing I am wondering is how would it be possible to do layouting in Zbrush. I do not think that it even has the notion of objects. Subtool unions are not a good way to do it.

10:25am. He has a lot of presets. There are a bunch of them that are anime related.

10:45am. Right now he is showing how to create matcaps. This is useful for comic style stuff.

Focus me. Why is the matcap circular?

Hnnn, I see. It matches the contours of the sphere exactly. The reason why it is circular is because the back facing normals aren't necessary. I see.

10:55am. There is a comic style one already in Blender. Ok, I see.

I thought it would be something more complicated, but this is simple enough.

11:30am. He notees that Zbrush does an excellent job at reducing the amount of polygons, but keeping the shape using Decimation Master.

11:45am. So nanomesh can be used to just distribute instances on faces similarly how geo nodes in Blender do it.

The kind of precise line work the basic matcap is giving me would be hard to get with just drawing. It has potential. I just need to dive deeper into it. How would I do something like this in Eevee...

Well, I probably couldn't, not directly. Hmmm, but maybe, actually yeah, there should be a way to combine it with the normal. Just get the first two coords of a normal, and this would allow me to sample a matcap for a particular color. I'd have to figure out how to mix that with the shadow information. Nevermind that for now.

Still, if it is just black or white, I could do that as a compositing step. No need to mess with shaders.

11:50am. Besides Nanomesh, earlier he showed how to use grooming frushes and fiber meshes.

12:15pm. Finally done watching part 1 of day 2. It was 1:40h long. I'll take a break here myself and then get back to this.

12:20pm. I feel like going back to that render and playing with gradient maps on it. If I set it to constant I'll get instant cell shading. If I could also extract lines and object ids for masks, I could get something good. I do not need to even worry too much about Eevee vs Malt vs Cycles vs Luxcore. The workflow should work for anything.

I thought his comic thing would be something more fancy, but it is just a simple matcap.

I am looking forward to seeing what the filters are about.

1:05pm. Let me do the chores here and I will resume.

1:10pm. Focus me. Chores. I need to get through this course as soon as possible.

1:15pm. Nevermind, I guess I'll save them for later. Let me start.

1:40pm. I do not know how focused I am, but I definitely get the gist of what he is doing. What I am most interested in are the parts after he is done modeling. I want to see what he does in Photoshop and what those NPR filters will be doing. I do have an interest in how he will compose the whole scene in Zbrush. Right now I don't know how it could be used for layouting. It is interesting to see that Zbrush has scattering capabilities.

Now he is going into a work mode.

http://docs.pixologic.com/user-guide/materials-lights-rendering/rendering/npr/npr-filters/

1:50pm. These filters do not look like anything too fancy. They would take having 3d information though. Maybe Blender's compositor can immitate them? Maybe that is what I am really missing - compositing skills.

Also, I know that Zbrush has a render option? Just what is it supposed to be doing?

Hmmm, Luxcore does not have freestyle, but I can just extract those using Eevee or Cycles. I wonder if it would be possible to use the compositor directly. With the Mangaka plugin it could.

1:55pm. i didn't think he would be spending so much time sculpting a rock. Remember how this would be done in Houdini? I spent hours learning about that, but this is also a viable approach.

It would be extremely hard to draw something like this using a pencil. Those fancy brushes really come in handy for this.

2pm. Focus me, stop surfing /a/. Go back to the course.

2:25pm. Hmmm, I guess it could be possible to do layouting in Zbrush if you set aside a tool that would just have union subtools. You can work on the object in other tools and them append them to the scene. That would work. That is sort of what I am doing in Blender.

Still, imagine trying to rotate doors in Zbrush. Could that be done in it. I doubt it.

2:35pm. The video player keeps crashing as I move around the track. I think it might be corruped at the 1:10h mark. Let me jump a head a bit then.

1.5m is fine.

2:40pm. It seems it is possible to stack fibremeshes ontop of each other.

2:50pm. Ah, move topological is like move except it works only on the selected polygroup.

It seems a lot of the stuff in Zbrush has a simple explanation. I keep thinking it would be more complicated than it really is.

That having said, even if Zbrush could be used for layouting, just how could it be used for rendering? I don't see it yet, but no doubt I will by the end of the course.

3pm. Finally done with day two. Let me take a short break and then I'll watch another video.

3:05pm. Let me start the third video. I already have an inkling, but I'll really know what to do

3:25pm. Instead of doing those tomato vines the way he did, he should have used 'cont z' and 'as line'. That would have been simpler.

> There kinds of tubes, they work really well in illustration.

I am starting to see it. What would be overly simple in 3d can look good in 3d.

That spaceship by Asano could be done like this as well.

3:35pm. Let me take a break again. I need to do the chores.

3:50pm. Let me resume. My goal is to get through at least 3 vids per day. I have one more to meet my quota so let me get on with it.

This stuff about decimating the models is useful to me. I should keep that in mind for objects far awar from the camera.

4:05pm. He shows how to cycle through different gizmos at 32:40m of day 3 part 1.

47 out 94 minutes in. Let me just pause to remark, this is such a dream. I am not following along myself in Zbrush and I am bored, but the modeling stuff he is doing in Zbrush here I could do in so many different ways in different programs. And the matcap stuff he showed me is trivial. I could take the one he is using and import it in Blender, no problem.

I am going to try to pack away another video after this one so I can get to the interesting stuff tomorrow. While the Zbrush stuff might be of interest to other people, I am really into seeing how he does things after being done with modeling.

4:55pm. Ugh, let me watch another video. I skipped during the work mode. I just want to get through these boring parts.

This one might be intersting. I wonder how he will pose the chara.

5:20pm. Let me take a break here at 18m. I really can't pay attention anymore. 5h of tutorials is really a lot for one day.

Maybe I'll space it out over the next 5h, but let me take a real break here. It would be fine if I closed.

5:40pm. Let me do a bit more. 10m and then I will close.

Oh, right now he is doing wrinkles using curves. That is something. The secret is to have it be pointy at both ends, but fat in the middle. You can do that kind of thing in Zbrush using a curve profile.

6pm. I am going to do it. I am going to go all the way with this video and finish day 3 today.

It seems he will use Transpose Master to pose the model.

6:10pm. It seems he is just using the gizmo to pose the character. Lame.

6:15pm. 47m in. It seems transpose master comes into play after the posing is done.

Ugh, I am not sure I will manage another hour of this. Let me try for another 10m and then I will close.

I do not get this stuff with the layers, but nevermind it.

6:25pm. This posing he is doing is something I should keep in mind. It is a pain in the ass, I could do it like this in Blender. Blender does have a pose brush thought just for cases like these, but I remember not liking it when I tried it.

6:50pm. http://docs.pixologic.com/user-guide/2d-illustration/2-5d-basics/

I'll take a look at this later. It seems Zbrush really was meant for illustrations. For now let me just finish the video, I am 70% of the way in. I can do this.

6:55pm. No, I think I'll stop here at 1:13, with 31 minutes left to go. He is talking about polypaint brushes, I see some of them are supposedly for hatching, but I can be bothered to even look at the screen. I am just wasting my time.

Let me stop here. It is good that I put in some overtime. I've met my quota for the day, and there is nothing to be ashamed of with stopping.

http://docs.pixologic.com/user-guide/2d-illustration/illustration-techniques/

Interesting illustrations."

---
## [Spyroshark/Pariah-Station](https://github.com/Spyroshark/Pariah-Station)@[c77fb1e795...](https://github.com/Spyroshark/Pariah-Station/commit/c77fb1e7959bec41276673ba903da1625be8b68e)
#### Friday 2022-05-27 18:40:03 by Octus

Parallax but better: Smooth movement cleanup (#66567) (#724)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [OxygenCobalt/Auxio](https://github.com/OxygenCobalt/Auxio)@[c6d7d8fe39...](https://github.com/OxygenCobalt/Auxio/commit/c6d7d8fe39ae0f84051482961c3d2ad5ae64137a)
#### Friday 2022-05-27 20:34:28 by OxygenCobalt

playback: implement "safe" slider wrapper

Implement a safe slider wrapper that does not crash with invalid values
as often.

Slider is a terrible component that is not designed with Auxio's
use-case in the slightest. Instead of gracefully degrading with invalid
values, it just crashes the entire app, which is horrible for UX.

Since SeekBar is a useless buggy version-specific sh******ed mess too,
we have no choice but to wrap Slider in a safe view layout that
hopefully hacks with the input enough to not crash the app when doing
simple seeking actions.

I hate android so much.

Resolves #140.

---
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[db2e4bde78...](https://github.com/payday-restoration/restoration-mod/commit/db2e4bde7896851d7a961169331ce18f0d09d612)
#### Friday 2022-05-27 23:38:28 by Noep

fuck

idiot moron forgets the winchester barrels affect tube length and the copypasta barrel stats won't have that shit on them

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cd294e9040...](https://github.com/tgstation/tgstation/commit/cd294e9040505e73e46384d6166015afa43217f3)
#### Friday 2022-05-27 23:49:10 by vincentiusvin

Scipaper rebalancing: Nitrium and halon shell removal. Nitrous added. Emphasis on BZ. (#66738)

Similar in spirit to #65707, with some more changes.

Restructured the gaseous experiments to:

    Nitrous (practice experiment)
    BZ (mainstay experiment)
    Hyper-Nob (lategame/once-in-a-while experiment)

Added a mining partner.

Moved adv weaponry lock to normal weaponry under reactionless. Toned down t3 reactionless.

BZ locks adv engi. Medbay unbridled by toxin gasses now.

Removed Xenobio's BZ Can.
Why It's Good For The Game

My original intent with papers was expanding the difficulty range of toxins. Both to things harder than tritium (nob, nitrium, etc) and also to things easier than tritium (bz, reactionless, etc).

In that process, I feel that i strayed a bit to the harder side, this PR is an attempt to tone down the overall difficulty of some of the gaseous experiments a notch.

Nitrous now takes place of the old BZ, BZ takes place of old nitrium/halon, and noblium stays because it's difficulty is in a pretty good spot for a relatively unimportant but nice to have tech.

While we're at it, I also added more emphasis to BZ production to toxins instead of tritium. This will hopefully incentivize people to try the department out. There is a risk of this being a bit of a chore, but I believe that the relevant atmos gameplay loop is strong enough to have it be fun. You need to check on the chamber, turn on pipes, adjust the input rate, and many more that makes it significantly more fun to do.

We do this by:

    Locking advanced engineering with BZ (organs and implants lock lifted). Depending on feedback i wont mind changing this around if you want to suggest another node as long as it's of similar or very slightly less importance.

    Getting rid of xeno's BZ can. Some xeno players need it for making slimes sleep, with their roundstart supply removed there should be a significant demand for the BZ production in toxins to go online asap.

If you have been paying attention to our PRs, i have been working to make BZ production as seamless and quick as possible in toxins. My five map prs #66454 #66198 #66064 #66010 #65857 have been building up to this. You can make BZ relatively quickly with the new freezer chamber in place. Probably even faster than ordering it in cargo, which is a fine ballpark to use if you want to make changes to it.

If you want to know how to operate it, here is a wiki guide in place https://tgstation13.org/wiki/User:Vincentius_vin/Sandbox#BZ_Synthesis. We will move it to the main toxins page once the rest of the page is finished, pictures are added, 

Made adv engi tech node require bz shells as an experiment, organs no longer need it.
Adv mining no longer requires adv engi.
Removed nitrium and halon shell, implant experiment lock lifted because of the former.
Relocked sec 1 tech node to need pressure bombs, sec 2 no longer needs tritium bomb.
Made advanced pressure bombs easier to do without funny fusion gases.
Added a new mining partner that accepts smaller (even non-atmos/non-ordnance related) bombs
Added more options to purchase nodes in the paper partners. Your point gain stays the same though.
Removed roundstart BZ can from xenobio.

---

