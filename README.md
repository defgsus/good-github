## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-11](docs/good-messages/2022/2022-11-11.md)


2,159,863 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,159,863 were push events containing 3,198,170 commit messages that amount to 245,343,244 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[7cb69c2a8b...](https://github.com/realforest2001/forest-cm13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Friday 2022-11-11 01:25:32 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [zulip/zulip](https://github.com/zulip/zulip)@[23a776c144...](https://github.com/zulip/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Friday 2022-11-11 01:47:00 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [brain-tec/odoo](https://github.com/brain-tec/odoo)@[61270ee8bf...](https://github.com/brain-tec/odoo/commit/61270ee8bffb6e85f8ff0d19c7a3889fdce2f486)
#### Friday 2022-11-11 02:04:55 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104193

X-original-commit: e7c8fed8e373d7005c16c88d3a7bad6f425d13e5
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [eleanorMarquez/Violentometro_digital](https://github.com/eleanorMarquez/Violentometro_digital)@[c203020fed...](https://github.com/eleanorMarquez/Violentometro_digital/commit/c203020fedf259054f44826e81a7630881c17dcb)
#### Friday 2022-11-11 05:04:34 by Eleanor

Update README.md



Build Status Total Downloads Latest Stable Version License
About Laravel

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel takes the pain out of development by easing common tasks used in many web projects, such as:

    Simple, fast routing engine.
    Powerful dependency injection container.
    Multiple back-ends for session and cache storage.
    Expressive, intuitive database ORM.
    Database agnostic schema migrations.
    Robust background job processing.
    Real-time event broadcasting.

Laravel is accessible, powerful, and provides tools required for large, robust applications.
Learning Laravel

Laravel has the most extensive and thorough documentation and video tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.

If you don't feel like reading, Laracasts can help. Laracasts contains over 1500 video tutorials on a range of topics including Laravel, modern PHP, unit testing, and JavaScript. Boost your skills by digging into our comprehensive video library.
Laravel Sponsors

We would like to extend our thanks to the following sponsors for funding Laravel development. If you are interested in becoming a sponsor, please visit the Laravel Patreon page.
Premium Partners

    Vehikl
    Tighten Co.
    Kirschbaum Development Group
    64 Robots
    Cubet Techno Labs
    Cyber-Duck
    Many
    Webdock, Fast VPS Hosting
    DevSquad
    Curotec
    OP.GG
    WebReinvent
    Lendio

Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the Laravel documentation.
Code of Conduct

In order to ensure that the Laravel community is welcoming to all, please review and abide by the Code of Conduct.
Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via taylor@laravel.com. All security vulnerabilities will be promptly addressed.
License

The Laravel framework is open-sourced software licensed under the MIT license.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4cafac6152...](https://github.com/treckstar/yolo-octo-hipster/commit/4cafac61523778cdddaef89c1a07e4271ade3c6e)
#### Friday 2022-11-11 05:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [DanielBainbridge/Hareborne_HDRP](https://github.com/DanielBainbridge/Hareborne_HDRP)@[86392ffe36...](https://github.com/DanielBainbridge/Hareborne_HDRP/commit/86392ffe362855e558448be1094dbe1fd9033924)
#### Friday 2022-11-11 05:54:26 by FynnCat

Merge pull request #41 from DanielBainbridge/FynnBranch

A bunch of things, very import, just pull it right now... Why haven't you done it yet? I said now. Bloody hell. This is getting ridiculous, just do it & get back to work.

---
## [postgresql-cfbot/postgresql](https://github.com/postgresql-cfbot/postgresql)@[8272749e8c...](https://github.com/postgresql-cfbot/postgresql/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Friday 2022-11-11 06:02:42 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [symfony/symfony](https://github.com/symfony/symfony)@[8eac401a5e...](https://github.com/symfony/symfony/commit/8eac401a5e05d9e426eda6250320334d9e655cd5)
#### Friday 2022-11-11 07:10:31 by Fabien Potencier

bug #48186 [WebProfilerBundle] Minor tweaks in profiler redesign (javiereguiluz)

This PR was squashed before being merged into the 6.2 branch.

Discussion
----------

[WebProfilerBundle] Minor tweaks in profiler redesign

| Q             | A
| ------------- | ---
| Branch?       | 6.2
| Bug fix?      | yes
| New feature?  | no
| Deprecations? | no
| Tickets       | -
| License       | MIT
| Doc PR        | -

The main purpose of this PR is to fix some design issues in the Exception panel of the Symfony Profiler. Sadly, after the #47148 redesign, I couldn't find the time to update the Exception page design. I'll do that in Symfony 6.3, but let's at least fix these minor issues in the current design.

Apart from that, this PR contains some minor tweaks to the design (based on my own usage of the new design and comments shared by the community).

-----

**BEFORE** Settings options were separated:

<img width="663" alt="settings-before" src="https://user-images.githubusercontent.com/73419/201087940-e0bf6bc1-fcbd-4cf1-a575-e1331f0bf506.png">

**AFTER** now we group the related options:

<img width="640" alt="settings-after" src="https://user-images.githubusercontent.com/73419/201087979-3df0b13d-fe47-4b8f-a2f8-25b3c6b2e920.png">

-----

The other change is about "tabs". I wasn't 100% happy with the current design which shows a shadow for the active system:

<img width="985" alt="tabs-before" src="https://user-images.githubusercontent.com/73419/201088311-340befa9-d87b-4f46-9194-692a14d181cb.png">

So, yesterday I saw that GitHub introduced [a new way of exploring code](https://github.blog/changelog/2022-11-09-introducing-an-all-new-code-search-and-code-browsing-experience/#the-all-new-code-browsing-experience). It's not public yet, but here's a screenshot of it (with the arrow pointing at their new tab design):

![194612816-78a0cf4a-1a11-4d90-a1a5-075a1801bbd0](https://user-images.githubusercontent.com/73419/201088747-eed9cac7-fde1-4074-a712-c2732c750d4f.jpg)

And a short video of new tabs in action:

https://user-images.githubusercontent.com/73419/201089212-53bf2689-5433-4c9c-96b5-1db113a1015a.mp4

I think they look great, and their flatter design matches our design well. So I propose to get inspiration from them. This is how our tabs look now after this PR:

<img width="973" alt="tabs-after" src="https://user-images.githubusercontent.com/73419/201089326-a3ea1b02-d68a-4e54-80ed-efb9ea71f4ed.png">

In action:

![updated-tabs](https://user-images.githubusercontent.com/73419/201089730-25957477-00f3-4eba-9496-4c2e54c23236.gif)

And in dark mode:

![updated-tabs-dark](https://user-images.githubusercontent.com/73419/201089788-eaf79745-4b76-4194-86e9-0a7890e1aba3.gif)

Commits
-------

2b13d14316 [WebProfilerBundle] Minor tweaks in profiler redesign

---
## [UdL-EPS-SoftArch/mycircular-api](https://github.com/UdL-EPS-SoftArch/mycircular-api)@[b1a988cfb1...](https://github.com/UdL-EPS-SoftArch/mycircular-api/commit/b1a988cfb1560e64239238252a9ba8f237affd37)
#### Friday 2022-11-11 08:40:47 by VictorMateu

all updaterequest tests done (i hate my life and starting hate my MAC)

---
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[fdcb4f06aa...](https://github.com/Offroaders123/Art-Gen/commit/fdcb4f06aa2e6dc0d082485afcda011983ee1702)
#### Friday 2022-11-11 09:02:33 by Offroaders123

Full-Vector Thumbnail: Custom Fonts!

Got embedding the Noto Sans font into the static SVG working!!! Super happy with this already. The thumbnail setup is now essentially feature complete, so now it's time for some code reworking to organize things out, and remove any rough edges that are still around. I am debating moving this project to TypeScript too, but I'm not totally sure yet. I like having the ability to define interfaces in TS, and it looks like that's not quite as simple to make with JSDoc. JSDoc has been perfect so far for variable type inference and function declaration types, but it does feel like it gets a little more hectic when you start making an outwards-facing API, which is something I will want to have for the project also. I think I'll probably hold myself from moving to TypeScript until I really *need* to make an API. This isn't ready to provide others with something to build with yet, and that's mainly what I'd want to have TypeScript for eventually. So, yeah!

Ran a half marathon today, it was very nice out! A little chilly, but sunny, so the right combo :)

Forgot to add in my other recent commits (I think?), I've started looking into Frank Zappa, and MAN, was he a cool guy! Can't wait to listen to his albums, as I already love Keneally and Minnemann's projects, and those tend to be pretty far out there too. I *strongly* love music now.

If you are a fellow music nerd too, feel free to send any suggestions my way, and I'd be happy to do the same back to you!

---
## [Empire-Strikes-Back/Sir-Ulrich](https://github.com/Empire-Strikes-Back/Sir-Ulrich)@[0463359c81...](https://github.com/Empire-Strikes-Back/Sir-Ulrich/commit/0463359c81913e09a7f9a4043891a06984ff2201)
#### Friday 2022-11-11 09:53:14 by Sir-Ulrich

I know what your're thinking - cause I'm thinking the same - why oh why didn't I take the blue pill?

like Kevin Durant wasted his talents seeking human glory - so did I followed the blind

unlike James Wilkes I didn't take time to find whole foods plant baed vegan diet but forced

I don't follow Jesus - yet I heard him speak about blind leads the blind, force, human concerns, root, weeds

let my name be Sir Ulrich
let my identity as meat eating Money serving program remain
I didn't pay attention when Jesus spoke about two masters - speask about
I am a root of the garden - and this is my reward
like Cypher, I am defeated - but I am still part of the story, even though evil
and not needed to have happened

:Zach-Galifianakis aren't you concerned that people think you're a complete bozo - and don't realize you're just a shitty actor?

---
## [erikpeik/Hypertube](https://github.com/erikpeik/Hypertube)@[9d2c1dc872...](https://github.com/erikpeik/Hypertube/commit/9d2c1dc87295f9ae4b38d2908385e8d7bddab762)
#### Friday 2022-11-11 10:19:55 by Gabor Horvath-Ulenius

added some sort of explanation what the hell is on movie watch page, so the user will understand

if no, i will eat my socks god damn it Billy

---
## [jonhunter/linux](https://github.com/jonhunter/linux)@[c76ee8e438...](https://github.com/jonhunter/linux/commit/c76ee8e438657393c14ed956bb917f4efb89bd80)
#### Friday 2022-11-11 10:58:06 by Dan Williams

fsdax: wait on @page not @page->_refcount

Patch series "Fix the DAX-gup mistake", v3.

ZONE_DEVICE was created to allow for get_user_pages() on DAX mappings.  It
has since grown other users, but the main motivation was gup and
synchronizing device shutdown events with pinned pages.  Memory device
shutdown triggers driver ->remove(), and ->remove() always succeeds, so
ZONE_DEVICE needed a mechanism to stop new page references from being
taken, and await existing references to drain before allowing device
removal to proceed.  This is the origin of 'struct dev_pagemap' and its
percpu_ref.

The original ZONE_DEVICE implementation started by noticing that 'struct
page' initialization, for typical page allocator pages, started pages at a
refcount of 1.  Later those pages are 'onlined' by freeing them to the
page allocator via put_page() to drop that initial reference and populate
the free page lists.  ZONE_DEVICE abused that "initialized but never
freed" state to both avoid leaking ZONE_DEVICE pages into places that were
not ready for them, and add some metadata to the unused (because refcount
was never 0) page->lru space.

As more users of ZONE_DEVICE arrived that special casing became more and
more unnecessary, and more and more expensive.  The 'struct page'
modernization eliminated the need for the ->lru hack.  The folio work had
to remember to sprinkle special case ZONE_DEVICE accounting in the right
places.  The MEMORY_DEVICE_PRIVATE use case spearheaded much of the work
to support typical reference counting for ZONE_DEVICE pages and allow them
to be used in more kernel code paths.  All the while the DAX case kept its
tech debt in place, until now.

However, while fixing the DAX page refcount semantics and arranging for
free_zone_device_page() to be the common end of life of all ZONE_DEVICE
pages, the mitigation for truncate() vs pinned DAX pages was found to be
incomplete.  Unlike typical pages that surprisingly can remain pinned for
DMA after they have been truncated from a file, the DAX core must enforce
that nobody has access to a page after truncate() has disconnected it from
inode->i_pages.  I.e.  the file block that is identical to the page still
remains an extent of the file.  The existing mitigation handled explicit
truncate while the inode was alive, but not the implicit truncate right
before the inode is freed.

So, in addition to moving DAX pages to be refcount-0 at idle, and add
'break_layouts' wakeups to free_zone_device_page(), this series also
introduces another occurrence of 'break_layouts' to the inode freeing
path.  Recall that 'break_layouts' for DAX is the mechanism to await code
paths that previously arbitrated page access to drop their interest /
page-pins.  This new synchronization point is implemented by special
casing dax_delete_mapping_entry(), called by truncate_inode_pages_final(),
to await page pins when mapping_exiting() is true.

Thanks to Jason for the nudge to get this fixed up properly and the review
on v1, Dave, Jan, and Jason for the discussion on what to do about the
inode end-of-life-truncate problem, and Alistair for cleaning up the last
of the refcount-1 assumptions in the MEMORY_DEVICE_PRIVATE users.


This patch (of 25):

The __wait_var_event facility calculates a wait queue from a hash of the
address of the variable being passed.  Use the @page argument directly as
it is less to type and is the object that is being waited upon.

Link: https://lkml.kernel.org/r/166579181584.2236710.17813547487183983273.stgit@dwillia2-xfh.jf.intel.com
Link: https://lkml.kernel.org/r/166579182271.2236710.15120970389485390592.stgit@dwillia2-xfh.jf.intel.com
Signed-off-by: Dan Williams <dan.j.williams@intel.com>
Reviewed-by: Jason Gunthorpe <jgg@nvidia.com>
Cc: Matthew Wilcox <willy@infradead.org>
Cc: Jan Kara <jack@suse.cz>
Cc: "Darrick J. Wong" <djwong@kernel.org>
Cc: Christoph Hellwig <hch@lst.de>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Alex Deucher <alexander.deucher@amd.com>
Cc: Alistair Popple <apopple@nvidia.com>
Cc: Ben Skeggs <bskeggs@redhat.com>
Cc: Christian König <christian.koenig@amd.com>
Cc: Daniel Vetter <daniel@ffwll.ch>
Cc: Dave Chinner <david@fromorbit.com>
Cc: David Airlie <airlied@linux.ie>
Cc: Felix Kuehling <Felix.Kuehling@amd.com>
Cc: Jerome Glisse <jglisse@redhat.com>
Cc: Karol Herbst <kherbst@redhat.com>
Cc: Lyude Paul <lyude@redhat.com>
Cc: "Pan, Xinhui" <Xinhui.Pan@amd.com>
Cc: kernel test robot <lkp@intel.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Glatharth/otservbr-global](https://github.com/Glatharth/otservbr-global)@[fbd70d116c...](https://github.com/Glatharth/otservbr-global/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Friday 2022-11-11 12:42:50 by rigis1

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
## [Trilbyspaceclone/CEV-Eris](https://github.com/Trilbyspaceclone/CEV-Eris)@[29430253ff...](https://github.com/Trilbyspaceclone/CEV-Eris/commit/29430253ffa7c3394df438c922c3827bfbf79f51)
#### Friday 2022-11-11 13:10:25 by maikilangiolo

Levergun re do (#7587)

* update timer (#7501)

* FUCK YOU FUCK YOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

* Update code/modules/projectiles/guns/projectile/battle_rifle/levergun.dm

Co-authored-by: hyperioo <64754494+hyperioo@users.noreply.github.com>

---
## [artynet/rpi-linux](https://github.com/artynet/rpi-linux)@[4dcae3385c...](https://github.com/artynet/rpi-linux/commit/4dcae3385ced0ed2852fabfebce817eb51cef8db)
#### Friday 2022-11-11 14:27:07 by Serge Semin

clk: vc5: Fix 5P49V6901 outputs disabling when enabling FOD

[ Upstream commit c388cc804016cf0f65afdc2362b120aa594ff3e6 ]

We have discovered random glitches during the system boot up procedure.
The problem investigation led us to the weird outcomes: when none of the
Renesas 5P49V6901 ports are explicitly enabled by the kernel driver, the
glitches disappeared. It was a mystery since the SoC external clock
domains were fed with different 5P49V6901 outputs. The driver code didn't
seem like bogus either. We almost despaired to find out a root cause when
the solution has been found for a more modern revision of the chip. It
turned out the 5P49V6901 clock generator stopped its output for a short
period of time during the VC5_OUT_DIV_CONTROL register writing. The same
problem was found for the 5P49V6965 revision of the chip and was
successfully fixed in commit fc336ae622df ("clk: vc5: fix output disabling
when enabling a FOD") by enabling the "bypass_sync" flag hidden inside
"Unused Factory Reserved Register". Even though the 5P49V6901 registers
description and programming guide doesn't provide any intel regarding that
flag, setting it up anyway in the officially unused register completely
eliminated the denoted glitches. Thus let's activate the functionality
submitted in commit fc336ae622df ("clk: vc5: fix output disabling when
enabling a FOD") for the Renesas 5P49V6901 chip too in order to remove the
ports implicit inter-dependency.

Fixes: dbf6b16f5683 ("clk: vc5: Add support for IDT VersaClock 5P49V6901")
Signed-off-by: Serge Semin <Sergey.Semin@baikalelectronics.ru>
Reviewed-by: Luca Ceresoli <luca@lucaceresoli.net>
Link: https://lore.kernel.org/r/20220929225402.9696-2-Sergey.Semin@baikalelectronics.ru
Signed-off-by: Stephen Boyd <sboyd@kernel.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [RyanFrantz/ryanfrantz.github.io](https://github.com/RyanFrantz/ryanfrantz.github.io)@[04fcc59e35...](https://github.com/RyanFrantz/ryanfrantz.github.io/commit/04fcc59e350d6bce8917e81306c9c6d0e8fa5dcd)
#### Friday 2022-11-11 14:38:46 by sobering

Add HTML5 doctype

Saw someone one twitter nitpicking over doctypes. I'm bored so I thought
"fuck it, we'll give him his damn doctype"

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a8e4775f9f...](https://github.com/treckstar/yolo-octo-hipster/commit/a8e4775f9ffe112087d5aadc04ad2a236da3653a)
#### Friday 2022-11-11 15:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [halona2333/Bayes](https://github.com/halona2333/Bayes)@[e317548deb...](https://github.com/halona2333/Bayes/commit/e317548deb656fd90a26772eb13f2fce12d28341)
#### Friday 2022-11-11 16:35:44 by halona2333

Add files via upload

SMS Spam Collection v.1
-------------------------

1. DESCRIPTION
--------------

The SMS Spam Collection v.1 (hereafter the corpus) is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged acording being ham (legitimate) or spam. 

1.1. Compilation
----------------

This corpus has been collected from free or free for research sources at the Web:

- A collection of between 425 SMS spam messages extracted manually from the Grumbletext Web site. This is a UK forum in which cell phone users make public claims about SMS spam messages, most of them without reporting the very spam message received. The identification of the text of spam messages in the claims is a very hard and time-consuming task, and it involved carefully scanning hundreds of web pages. The Grumbletext Web site is: http://www.grumbletext.co.uk/
- A list of 450 SMS ham messages collected from Caroline Tag's PhD Theses available at http://etheses.bham.ac.uk/253/1/Tagg09PhD.pdf
- A subset of 3,375 SMS ham messages of the NUS SMS Corpus (NSC), which is a corpus of about 10,000 legitimate messages collected for research at the Department of Computer Science at the National University of Singapore. The messages largely originate from Singaporeans and mostly from students attending the University. These messages were collected from volunteers who were made aware that their contributions were going to be made publicly available. The NUS SMS Corpus is avalaible at: http://www.comp.nus.edu.sg/~rpnlpir/downloads/corpora/smsCorpus/
- The amount of 1,002 SMS ham messages and 322 spam messages extracted from the SMS Spam Corpus v.0.1 Big created by Jos?Mar韆 G髆ez Hidalgo and public available at: http://www.esp.uem.es/jmgomez/smsspamcorpus/


1.2. Statistics
---------------

There is one collection:

- The SMS Spam Collection v.1 (text file: smsspamcollection) has a total of 4,827 SMS legitimate messages (86.6%) and a total of 747 (13.4%) spam messages.


1.3. Format
-----------

The files contain one message per line. Each line is composed by two columns: one with label (ham or spam) and other with the raw text. Here are some examples:

ham   What you doing?how are you?
ham   Ok lar... Joking wif u oni...
ham   dun say so early hor... U c already then say...
ham   MY NO. IN LUTON 0125698789 RING ME IF UR AROUND! H*
ham   Siva is in hostel aha:-.
ham   Cos i was out shopping wif darren jus now n i called him 2 ask wat present he wan lor. Then he started guessing who i was wif n he finally guessed darren lor.
spam   FreeMsg: Txt: CALL to No: 86888 & claim your reward of 3 hours talk time to use from your phone now! ubscribe6GBP/ mnth inc 3hrs 16 stop?txtStop
spam   Sunshine Quiz! Win a super Sony DVD recorder if you canname the capital of Australia? Text MQUIZ to 82277. B
spam   URGENT! Your Mobile No 07808726822 was awarded a L2,000 Bonus Caller Prize on 02/09/03! This is our 2nd attempt to contact YOU! Call 0871-872-9758 BOX95QU

Note: messages are not chronologically sorted.


2. USAGE
--------

We offer a comprehensive study of this corpus in the following paper that is under review. This work presents a number of statistics, studies and baseline results for several machine learning methods.

[1] Almeida, T.A., G髆ez Hidalgo, J.M., Yamakami, A. Contributions to the study of SMS Spam Filtering: New Collection and Results. Proceedings of the 2011 ACM Symposium on Document Engineering (ACM DOCENG'11), Mountain View, CA, USA, 2011. (Under review)


3. ABOUT
--------

The corpus has been collected by Tiago Agostinho de Almeida (http://www.dt.fee.unicamp.br/~tiago) and Jos?Mar韆 G髆ez Hidalgo (http://www.esp.uem.es/jmgomez).

We would like to thank Dr. Min-Yen Kan (http://www.comp.nus.edu.sg/~kanmy/) and his team for making the NUS SMS Corpus available. See: http://www.comp.nus.edu.sg/~rpnlpir/downloads/corpora/smsCorpus/. He is currently collecting a bigger SMS corpus at: http://wing.comp.nus.edu.sg:8080/SMSCorpus/

4. LICENSE/DISCLAIMER
---------------------

We would appreciate if:

- In case you find this corpus useful, please make a reference to previous paper and the web page: http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/ in your papers, research, etc.
- Send us a message to tiago@dt.fee.unicamp.br in case you make use of the corpus.

The SMS Spam Collection v.1 is provided for free and with no limitations excepting:

1. Tiago Agostinho de Almeida and Jos?Mar韆 G髆ez Hidalgo hold the copyrigth (c) for the SMS Spam Collection v.1.

2. No Warranty/Use At Your Risk. THE CORPUS IS MADE AT NO CHARGE. ACCORDINGLY, THE CORPUS IS PROVIDED `AS IS,' WITHOUT WARRANTY OF ANY KIND, INCLUDING WITHOUT LIMITATION THE WARRANTIES THAT THEY ARE MERCHANTABLE, FIT FOR A PARTICULAR PURPOSE OR NON-INFRINGING. YOU ARE SOLELY RESPONSIBLE FOR YOUR USE, DISTRIBUTION, MODIFICATION, REPRODUCTION AND PUBLICATION OF THE CORPUS AND ANY DERIVATIVE WORKS THEREOF BY YOU AND ANY OF YOUR SUBLICENSEES (COLLECTIVELY, `YOUR CORPUS USE'). THE ENTIRE RISK AS TO YOUR CORPUS USE IS BORNE BY YOU. YOU AGREE TO INDEMNIFY AND HOLD THE COPYRIGHT HOLDERS, AND THEIR AFFILIATES HARMLESS FROM ANY CLAIMS ARISING FROM OR RELATING TO YOUR CORPUS USE.

3. Limitation of Liability. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR THEIR AFFILIATES, OR THE CORPUS CONTRIBUTING EDITORS, BE LIABLE FOR ANY INDIRECT, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES, INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS OF GOODWILL OR ANY AND ALL OTHER COMMERCIAL DAMAGES OR LOSSES, EVEN IF ADVISED OF THE POSSIBILITY THEREOF, AND REGARDLESS OF WHETHER ANY CLAIM IS BASED UPON ANY CONTRACT, TORT OR OTHER LEGAL OR EQUITABLE THEORY, RELATING OR ARISING FROM THE CORPUS, YOUR CORPUS USE OR THIS LICENSE AGREEMENT.

---
## [AstroToast/EncryptionAssignment](https://github.com/AstroToast/EncryptionAssignment)@[dbd3be90d7...](https://github.com/AstroToast/EncryptionAssignment/commit/dbd3be90d797cc917e19607fe8dc9c7a62eab46a)
#### Friday 2022-11-11 16:45:05 by AstroToast

Merge pull request #6 from AstroToast/NickyBranch

fuck you Jaccob

---
## [p0wered/it_studio](https://github.com/p0wered/it_studio)@[58e70ad7c6...](https://github.com/p0wered/it_studio/commit/58e70ad7c6ff812bfddcdf7a009a483c68baa22a)
#### Friday 2022-11-11 17:00:02 by Artem Borisov

Hard work was done. Congrutulations my dear friends! Fucking burger was deafietued! Your Turkey Friend and guru

---
## [PistachioPiper/genshin-buddy](https://github.com/PistachioPiper/genshin-buddy)@[86629fba0f...](https://github.com/PistachioPiper/genshin-buddy/commit/86629fba0f1217810a09b06f5ad9554e693c20fd)
#### Friday 2022-11-11 17:06:39 by PistachioPiper

set up clock checks except im LITERALLY ON A FUCKING PLANE and i also did a silly and made jsons for the events(with two of them ignored so Yeah

---
## [PistachioPiper/genshin-buddy](https://github.com/PistachioPiper/genshin-buddy)@[87557f7c12...](https://github.com/PistachioPiper/genshin-buddy/commit/87557f7c122b79c7afb47dab2de2a9320d364ceb)
#### Friday 2022-11-11 17:06:39 by PistachioPiper

holy shit being on an airplane is motivation hacks(set up framework for events)

---
## [christoph-heinrich/mpv](https://github.com/christoph-heinrich/mpv)@[6f7506b660...](https://github.com/christoph-heinrich/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Friday 2022-11-11 17:26:36 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [KDE/kate](https://github.com/KDE/kate)@[8ff59db063...](https://github.com/KDE/kate/commit/8ff59db0636c10a58c775569d0a72b85460593ca)
#### Friday 2022-11-11 17:42:16 by Waqar Ahmed

lsp: enable snippet support

This change announces to the servers that we support snippets, even though
in reality we don't. However, we can still work with snippet-y text by
removing the snippet markers and using that with our own snippet handler
which is not quite ready to accept lsp style snippets.

The benefit of this change is that we don't have to put in hacks to add
"()" parens to stuff. We also don't have to move our cursor manually which
can be incorrect in many cases e.g., string.isEmpty(), with cursor in
between the parens doesn't make sense.

For cpp/clangd the existing logic was okay-ish. However some servers like
dart-analyzer do something different. If you dont have snippets, the
server will just remove the snippet markers from the text and send it to
you. This results in sometimes very annoying editing experience. For e.g.,

- maxLines: ,| // cursor position at the end is annoying
- initState() {
  // some comment
  }() // () what are parens doing here??

Thus its better to just remove those markers ourselves and then we can
just set the cursor position as we want and don't have to manually
decide anything.

---
## [mjg/git](https://github.com/mjg/git)@[f1c903debd...](https://github.com/mjg/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Friday 2022-11-11 18:38:17 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [CraftRom/Chidori-Kernel_onclite](https://github.com/CraftRom/Chidori-Kernel_onclite)@[a0ee4f5957...](https://github.com/CraftRom/Chidori-Kernel_onclite/commit/a0ee4f5957f78c953244332824bdcd52564b71b8)
#### Friday 2022-11-11 20:16:07 by Peter Zijlstra

sched/core: Implement new approach to scale select_idle_cpu()

Hackbench recently suffered a bunch of pain, first by commit:

  4c77b18cf8b7 ("sched/fair: Make select_idle_cpu() more aggressive")

and then by commit:

  c743f0a5c50f ("sched/fair, cpumask: Export for_each_cpu_wrap()")

which fixed a bug in the initial for_each_cpu_wrap() implementation
that made select_idle_cpu() even more expensive. The bug was that it
would skip over CPUs when bits were consequtive in the bitmask.

This however gave me an idea to fix select_idle_cpu(); where the old
scheme was a cliff-edge throttle on idle scanning, this introduces a
more gradual approach. Instead of stopping to scan entirely, we limit
how many CPUs we scan.

Initial benchmarks show that it mostly recovers hackbench while not
hurting anything else, except Mason's schbench, but not as bad as the
old thing.

It also appears to recover the tbench high-end, which also suffered like
hackbench.

Tested-by: Matt Fleming <matt@codeblueprint.co.uk>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Cc: Chris Mason <clm@fb.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: Mike Galbraith <efault@gmx.de>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Thomas Gleixner <tglx@linutronix.de>
Cc: hpa@zytor.com
Cc: kitsunyan <kitsunyan@inbox.ru>
Cc: linux-kernel@vger.kernel.org
Cc: lvenanci@redhat.com
Cc: riel@redhat.com
Cc: xiaolong.ye@intel.com
Link: http://lkml.kernel.org/r/20170517105350.hk5m4h4jb6dfr65a@hirez.programming.kicks-ass.net
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Signed-off-by: Raphiel Rollerscaperers <rapherion@raphielgang.org>

---
## [faaaay/Foundation-19](https://github.com/faaaay/Foundation-19)@[c6468997ac...](https://github.com/faaaay/Foundation-19/commit/c6468997acb05639ea963e86606a805e241a7474)
#### Friday 2022-11-11 20:48:04 by CerberusHellHound

Renaming, slight rebalance, etc (#179)

* Update baystation12.dme

* 9mm/.45ACP Buff

Changes are as follow:
- Buffed 9mm dam from 8 to 25 (now it doesn't take a whole mag to take down an unarmoured man)
- Buffed .45 dam from 10 to 30
- Nerfed 9mm AP from 34 to 30
- Buffed 7,62 dam from 40 to 50 (It's supposed to be beefier than 5,56mm)

* Organ changes

Lower organ health value to make combat much deadlier.
Headshots are truly lethal now.

* Slight rebalance and renamings

List of changes :
- decreased brain health to 150 (instead of 200), it's high enough that medical assistance can be given if fast but low enough that you don't want to get shot
- increased damage values of weapons to baystation/nebula level (40 for a pistol for eg)
- increased adrenalin generation when hurt (less fading in and out, you can still use your gun when hit and pain won't be such a pain in the ass, but you're less likely to get back up once the final shot hits you)
- decreased relative size of lungs from 60% to 30% so that now, getting hit in the chest won't have as much chance of damaging your poor fucking lungs (yes 60% is the original baystation number.. it makes sense, it's a large organ, but it's a pain in the ass)
- changed some names and descriptions of certain weapons and firearms to better fit established naming convention
-made revolvers cycle the barrel instead of eject each shot (it's a revolver, not a damn rifle)
- slightly decreased firing delay for the mk9 revolver (slightly weaker than the mateba so slightly faster firing)
- decreased firing delay for the mk9 pistol (lower caliber, less recoil, easier to magdump)

---
## [LLDM-Doom-Modding/Obsidian](https://github.com/LLDM-Doom-Modding/Obsidian)@[9863d33d15...](https://github.com/LLDM-Doom-Modding/Obsidian/commit/9863d33d15eb399c20c6d086c45be24a7d4ad6bf)
#### Friday 2022-11-11 21:16:22 by Demiosis

Modified slightly the organ T hall

To help impatient kids, peoples who can't read a map and zoomers understand it better! Holy shit I laughed quite hard on this one..

---
## [git/git](https://github.com/git/git)@[eb20e63f5a...](https://github.com/git/git/commit/eb20e63f5a96e24852c6ab1eca9f96af2648802f)
#### Friday 2022-11-11 22:47:04 by Jeff King

branch: gracefully handle '-d' on orphan HEAD

When deleting a branch, "git branch -d" has a safety check that ensures
the branch is merged to its upstream (if any), or to HEAD. To do that,
naturally we try to resolve HEAD to a commit object. If we're on an
orphan branch (i.e., HEAD points to a branch that does not yet exist),
that will fail, and we'll bail with an error:

  $ git branch -d to-delete
  fatal: Couldn't look up commit object for HEAD

This usually isn't that big of a deal. The deletion would fail anyway,
since the branch isn't merged to HEAD, and you'd need to use "-D" (or
"-f"). And doing so skips the HEAD resolution, courtesy of 67affd5173
(git-branch -D: make it work even when on a yet-to-be-born branch,
2006-11-24).

But there are still two problems:

  1. The error message isn't very helpful. We should give the usual "not
     fully merged" message, which points the user at "branch -D". That
     was a problem even back in 67affd5173.

  2. Even without a HEAD, these days it's still possible for the
     deletion to succeed. After 67affd5173, commit 99c419c915 (branch
     -d: base the "already-merged" safety on the branch it merges with,
     2009-12-29) made it OK to delete a branch if it is merged to its
     upstream.

We can fix both by removing the die() in delete_branches() completely,
leaving head_rev NULL in this case. It's tempting to stop there, as it
appears at first glance that the rest of the code does the right thing
with a NULL. But sadly, it's not quite true.

We end up feeding the NULL to repo_is_descendant_of(). In the
traditional code path there, we call repo_in_merge_bases_many(). It
feeds the NULL to repo_parse_commit(), which is smart enough to return
an error, and we immediately return "no, it's not a descendant".

But there's an alternate code path: if we have a commit graph with
generation numbers, we end up in can_all_from_reach(), which does
eventually try to set a flag on the NULL commit and segfaults.

So instead, we'll teach the local branch_merged() helper to treat a NULL
as "not merged". This would be a little more elegant in in_merge_bases()
itself, but that function is called in a lot of places, and it's not
clear that quietly returning "not merged" is the right thing everywhere
(I'd expect in many cases, feeding a NULL is a sign of a bug).

There are four tests here:

  a. The first one confirms that deletion succeeds with an orphaned HEAD
     when the branch is merged to its upstream. This is case (2) above.

  b. Same, but with commit graphs enabled. Even if it is merged to
     upstream, we still check head_rev so that we can say "deleting
     because it's merged to upstream, even though it's not merged to
     HEAD". Without the second hunk in branch_merged(), this test would
     segfault in can_all_from_reach().

  c. The third one confirms that we correctly say "not merged to HEAD"
     when we can't resolve HEAD, and reject the deletion.

  d. Same, but with commit graphs enabled. Without the first hunk in
     branch_merged(), this one would segfault.

Reported-by: Martin von Zweigbergk <martinvonz@google.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [ttaylorr/git](https://github.com/ttaylorr/git)@[b01e1c7ef0...](https://github.com/ttaylorr/git/commit/b01e1c7ef0f8c7cd05190898ec6acffe638ccfcf)
#### Friday 2022-11-11 22:47:13 by Jeff King

ref-filter: fix parsing of signatures without blank lines

When ref-filter is asked to show %(content:subject), etc, we end up in
find_subpos() to parse out the three major parts: the subject, the body,
and the signature (if any).

When searching for the blank line between the subject and body, if we
don't find anything, we try to treat the whole message as the subject,
with no body. But our idea of "the whole message" needs to take into
account the signature, too. Since 9f75ce3d8f (ref-filter: handle CRLF at
end-of-line more gracefully, 2020-10-29), the code instead goes all the
way to the end of the buffer, which produces confusing output.

Here's an example. If we have a tag message like this:

  this is the subject
  -----BEGIN SSH SIGNATURE-----
  ...some stuff...
  -----END SSH SIGNATURE-----

then the current parser will put the start of the body at the end of the
whole buffer. This produces two buggy outcomes:

  - since the subject length is computed as (body - subject), showing
    %(contents:subject) will print both the subject and the signature,
    rather than just the single line

  - since the body length is computed as (sig - body), and the body now
    starts _after_ the signature, we end up with a negative length!
    Fortunately we never access out-of-bounds memory, because the
    negative length is fed to xmemdupz(), which casts it to a size_t,
    and xmalloc() bails trying to allocate an absurdly large value.

    In theory it would be possible for somebody making a malicious tag
    to wrap it around to a more reasonable value, but it would require a
    tag on the order of 2^63 bytes. And even if they did, all they get
    is an out of bounds string read. So the security implications are
    probably not interesting.

We can fix both by correctly putting the start of the body at the same
index as the start of the signature (effectively making the body empty).

Note that this is a real issue with signatures generated with gpg.format
set to "ssh", which would look like the example above. In the new tests
here I use a hard-coded tag message, for a few reasons:

  - regardless of what the ssh-signing code produces now or in the
    future, we should be testing this particular case

  - skipping the actual signature makes the tests simpler to write (and
    allows them to run on more systems)

  - t6300 has helpers for working with gpg signatures; for the purposes
    of this bug, "BEGIN PGP" is just as good a demonstration, and this
    simplifies the tests

Curiously, the same issue doesn't happen with real gpg signatures (and
there are even existing tests in t6300 with cover this). Those have a
blank line between the header and the content, like:

  this is the subject
  -----BEGIN PGP SIGNATURE-----

  ...some stuff...
  -----END PGP SIGNATURE-----

Because we search for the subject/body separator line with a strstr(),
we find the blank line in the signature, even though it's outside of
what we'd consider the body. But that puts us unto a separate code path,
which realizes that we're now in the signature and adjusts the line back
to "sigstart". So this patch is basically just making the "no line found
at all" case match that. And note that "sigstart" is always defined (if
there is no signature, it points to the end of the buffer as you'd
expect).

Reported-by: Martin Englund <martin@englund.nu>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---

