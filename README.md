## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-03](docs/good-messages/2023/2023-08-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,320,702 were push events containing 3,558,012 commit messages that amount to 279,458,744 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [ameerj/yuzu](https://github.com/ameerj/yuzu)@[8e703e08df...](https://github.com/ameerj/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Thursday 2023-08-03 00:00:37 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [SiegeB0t/TerraGov-Marine-Corps](https://github.com/SiegeB0t/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/SiegeB0t/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Thursday 2023-08-03 00:59:47 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [Monkeytoes999/monkeytoes999.github.io](https://github.com/Monkeytoes999/monkeytoes999.github.io)@[03baf3dfbf...](https://github.com/Monkeytoes999/monkeytoes999.github.io/commit/03baf3dfbf38fd7ba576288eed599038e8e26432)
#### Thursday 2023-08-03 01:21:21 by Bret Jones

Fixed the one thing. Not that one. Or that one. The other one. Yeah. The third one that came to your mind. I fixed that. Honestly embarrassing it took you 3 tries to guess. Learn to read code. Also I misspelled embarrassing. While we are on the subject. Yes. Both times. God I love you. Not god. Well frick.

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[3af26df8ca...](https://github.com/psychonaut-station/PsychonautStation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Thursday 2023-08-03 01:24:37 by GoldenAlpharex

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
## [CliffracerX/Skyraptor-SS13](https://github.com/CliffracerX/Skyraptor-SS13)@[d7c6d18aee...](https://github.com/CliffracerX/Skyraptor-SS13/commit/d7c6d18aeed11dd21d2b418cab1fa360ea754f6d)
#### Thursday 2023-08-03 01:28:02 by Watermelon914

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
## [Higgin/Shiptest](https://github.com/Higgin/Shiptest)@[ee4021c507...](https://github.com/Higgin/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Thursday 2023-08-03 02:06:26 by Imaginos16

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
## [Sagnac/streamsave](https://github.com/Sagnac/streamsave)@[43abedc5a7...](https://github.com/Sagnac/streamsave/commit/43abedc5a702160327b3d47c1922c50d1e80e02f)
#### Thursday 2023-08-03 02:31:06 by Sagnac

Redesign how options are updated

The previous scheme was pretty ugly. This is due for a much more
comprehensive rewrite as there's quite a bit of redundancy with the
script-message functions and maintaining both script-opts and
script-message updates requires more effort. But that will have to come
at a later time.

One alternative approach would be to hook into the current override
functions by using them as fields in the update table and have them
perform double duty, but this may prove more trouble than it's worth.

As a user, the script-message approach to changing options is more
convenient to use during runtime either with keybinds or through the
console. Also, it supports more arguments (e.g. cycle, on_demand) and
provides status messages. That being said, with script-opts you can send
an entire list of options to be updated instead of having to chain
script-message commands. The names being used for this also differ
between the two methods, with the script-message names being shorter and
likely easier to remember, but the inconsistency in naming between the
options and the runtime commands could be an issue.

Of course I could just turn off the script-opt updating mechanism by
not using update_opts, which I probably should do, but I'm going to keep
this around for now while I trim the script down to a lite version at a
separate branch; this will prove useful there as script-opts becomes the
desired minimalistic approach.

Another thing to note with regards to removing on_update handling of the
options is that some options such as the likely widely used
force_extension option would still require support in that regard, as
the runtime command is simply an on-demand single-stream change and a
revert handler, and does not in actuality set the format in a global
manner - if a new stream is loaded then it will take on the
automatically determined format.

---
## [pineapple-man/linux-lab](https://github.com/pineapple-man/linux-lab)@[561d896a14...](https://github.com/pineapple-man/linux-lab/commit/561d896a14684eb648a138fd18f9084c51b2dd14)
#### Thursday 2023-08-03 02:47:08 by Michal Vlasák

tools: labs: qemu: Add run-qemu.sh as alternative

TL;DR: In one window run `make -j$(ncproc) console` and `cd` to some
lab's subdirectory (`skels/...`). In second window `cd` to matching
`skels/...` subdirectory, edit source files and compile with something
like `kmake` (`alias kmake='make -C "$HOME/src/linux/" M="$(pwd)"'`) as
needed. The `skels` directory is shared between the host and the guest,
thus in the first window, so you can just `insmod` and `rmmod` the
compiled modules. You can kill the VM by `CTRL-a x` (if you made some
writes from the VM it might be a good idea to run `sync` first). Samba
and QEMU are required.

Full description:

To be honest I don't like the current QEMU setup. I am sure there are
things it does that I don't understand yet, because I have not yet
finished all the labs, but in any case I think that the setup can be
improved.

Some things in particular I don't like about the current setup:

 - "Huge" opaque `.ext4` images are used, even though the contents of
   the  root file system are not that large.
 - While running QEMU newly built modules can't be copied to the image.
 - Mounting and unmounting the `.ext4` image for copying the modules
   requires `sudo`.
 - The networking setup seems too complex, requires `sudo` and was
   broken (at least for me - IIRC I didn't get IP through DHCP), thus I
   also didn't get `ssh` to work. I also seem to be not the only one
   having issues with this:
   https://github.com/linux-kernel-labs/linux/pull/240#issuecomment-956219190
 - `dnsmasq` and `nttctp` mostly don't start correctly (they are not
   killed correctly by the previous run) - this isn't a problem on my
   end, as demonstrated by the output at
   https://linux-kernel-labs.github.io/refs/heads/master/info/vm.html,
   which shows the same issues.
 - Running `minicom` is required to access the serial port, thus at
   least two terminals are required for working with the VM (not a huge
   problem for me personally, since I use `tmux`, but I know some people
   complain about this). The setup also seems unnecessarily complex.
 - I remember a lot of the `.mon` `.pts` files being left uncleaned in
   some cases.
 - I recall warnigns about some of the entries added to `/etc/inittab`
   being ignored.
 - Even though root login requires no password I have to enter the
   `root` username.

In this commit I introdoce an alternative way of running QEMU through a
new `run-qemu.sh` script. The setup is laregely independent and its user
interface consists of `console` and `gui` targets. I tried to make the
script parameterizable through environment variables (inherited from
Make variables), though it may be argued that the default values should
be encoded in Makefile rather than in the script like they are now. I
have no strong opinions about that, it's' just that the current state
allows running the script in standalone fashion.

What the setup brings:

 - A rootfs is extracted from the official Yocto Project tarball and
   kept in a directory that is shared through  [Samba as network
   share](https://www.kernel.org/doc/html/latest/filesystems/cifs/cifsroot.html).
   The `skels` directory is shared as well. Thus the modules can be
   freely tweaked / compiled / ran from either the host or guest.
 - The QEMU stdio serial console setup is used (`ttyS0` on the kernel
   side). This means that running QEMU results in the serial console
   being mapped directly to standard input and output of the terminal -
   `minicom` is not needed. This is the console mode (`make console`).
 -  The setup allows also allows the virtual machine to be run in
    graphical mode (`make gui`).
 - Root is logged in automatically in `console` mode (though similar
   thing could be done for the `gui` mode).
 - Although Samba (`smbd`) is required, `sudo` or root access is not.
 - Networking through QEMU's default [SLIRP backend](https://wiki.qemu.org/Documentation/Networking#User_Networking_.28SLIRP.29).
   DHCP is handled by the kernel, which overcomes some problems I had
   with the System V init system in the Yocto images.
 - The compilation can largely be done with something like this `kmake`
   alias: `alias kmake='make -C "$HOME/src/linux/" M="$(pwd)"'`
   (customize as needed). Though this is not enough for some labs (I no
   longer remember the details, but I think it was some of the earlier
   labs which had dependencies between modules, I think I used the
   classic `make build` for that.

Known issues:

 - SSH support is currently missing. This both requires more featureful
   Yocto images and is IMO unnecessary, since it wouldn't bring much
   benefit over the console mode. Though it can be easily achieved by
   using QEMU option like `-nic user,hostfwd=tcp::2222-:22`, which would
   allow SSH'ing into the guest by something like `ssh -p 2222
   root@localhost`.
 - I used a slightly less advanced setup while doing the labs, so the
   lab workflow with this particular setup is largely untested. There
   may be problems with file permissions due to the samba share.
 - The guest seems to fail to shutdown correctly in a timely manner. I
   just took the habbit of killing qemu with `CTRL-a` followed by `x`,
   potentially running `sync` first to ensure my work is saved (though
   rarely did I actually modify anything on the guest side).

[The former setup](https://github.com/vlasakm/linux/commit/720bd6444a036c2ae6a3e76b7f6aac72f562053a)
I used contains some details of the SSH setup if anyone is interested in
that. It was the basis for this PR, so some ideas can be seen there
(Samba share for `skels`), but I didn't take particular care with [the
kernel config](https://github.com/vlasakm/linux/commit/0290919905e7f4fe3562a46d3274f8d41ad02c55)
and the automounting didn't really work (the `init` would try to mount
the filesystem before networking was up).

What I evaluated and didn't use in the end:

 - At first I tried to extend my former setup by just automounting the
   Samba share. I didn't manage to do this - the (non)workings of init
   scripts seem to be beyond me. If anyone is interested here are a few
   pointers:
   [[1]](https://unix.stackexchange.com/questions/169697/how-does-netdev-mount-option-in-etc-fstab-work),
   `/etc/inittab`, `/etc/init.d/mountall.sh`, `/etc/init.d/mountnfs.sh`.
 - I tried using `9p` [[2]](https://wiki.qemu.org/Documentation/9p),
   [[3]](https://wiki.qemu.org/Documentation/9psetup)
   [[4]](https://wiki.qemu.org/Documentation/9p_root_fs) which is built
   into QEMU and can be compiled into the kernel. With `mapped-xattr`
   security model it would be too cumbersome to create the rootfs, and
   `passthrough` would require root privileges. It is also very slow.
   There are also some problems with trying to use it as rootfs, maybe
   specific to `linux-kernel-labs` kernel version or config. Ask me if
   interested.
   [[5]](https://lists.gnu.org/archive/html/qemu-devel/2016-09/msg07184.html)
   [[6]](https://lore.kernel.org/linux-fsdevel/20210608153524.GB504497@redhat.com/)
   [[7]](https://lore.kernel.org/all/YL1eM+mzjuggDvqp@codewreck.org/T/)
 - QEMU has an option to setup the Samba share on its own, though I
   found a custom config (based on the QEMU one) to be easier - allows
   customization like multiple shares, unix extensions, different port,
   etc.

Signed-off-by: Michal Vlasák <lahcim8@gmail.com>
Signed-off-by: Daniel Baluta <daniel.baluta@nxp.com>

---
## [DGamerL/Paradise](https://github.com/DGamerL/Paradise)@[2d10818063...](https://github.com/DGamerL/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Thursday 2023-08-03 03:12:38 by ATP-Engineer

Fixes IV bag blood overlays being too damn bright for some mixtures (#21813)

* Removes old .dmi

* Fixes blood overlay coloring being too bright for IV bags

* Fine-tuning

* Makes the blood bag IV color overlays not as bright as they used to be

In hindsight it was probably easy to avoid

* FINAL TUNE UP

FUCK

* Fixes coloring for IV bags so they're not too bright

FINAL COMMIT

---
## [theonetruejesse/mSync](https://github.com/theonetruejesse/mSync)@[fbcdea5b64...](https://github.com/theonetruejesse/mSync/commit/fbcdea5b6470c8202e3be8beab8347b78e6d0596)
#### Thursday 2023-08-03 03:17:18 by Ethan Kim

Create `/create-student`

I'm not gon' fake the story
Most people flip the script
I'm not gon' say I'm sorry
I don't give a fuck 'bout forgiveness
I don't give a fuck 'bout no target

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[f31327a949...](https://github.com/git-for-windows/git/commit/f31327a9498855e2e5fe60836d6057381b5b31e2)
#### Thursday 2023-08-03 03:18:17 by Johannes Schindelin

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
## [elunna/hackem](https://github.com/elunna/hackem)@[3d46a8a33a...](https://github.com/elunna/hackem/commit/3d46a8a33abf1b2710a8d691556b4ffe5be684c9)
#### Thursday 2023-08-03 05:16:31 by Erik Lunna

Gnomes hate eggs (from EvilHack)

By player request, inspired from the 'Oz books' by author L. Frank Baum
- gnomes hate eggs. SporkHack has it so if you throw eggs and a
gnomes sees it, they become scared and flee. Decided to do my own thing
with it for EvilHack, and aosdict happened to have some old code laying
around that was inspired by the same; that's incorporated here. Here's
what happens:

* If you have regular eggs in open inventory and gnomes are nearby and
can see you, there's a chance they'll become agitated and flee
* If you're a gnome and eat a regular egg, you'll take 4d10 worth of
damage, and if you survive, it'll make you sick/vomitting
* If you throw a regular egg at a gnome and it hits, they'll take 4d5
worth of damage, and it will cause them to shout and flee, waking nearby
monsters

There are some potential to-do's here, such as should special
consideration be taken for gnomish priests/shopkeepers if they see you
carrying eggs? Should intelligent monsters want to collect regular eggs
to throw at you if you're a gnome? Should gnomes avoid regular eggs
altogether, and not even step over them? And probably a couple more I'm
not thinking of right now.

Co-authored-by: copperwater <copperwater@users.noreply.github.com>

---
## [merhmood/react](https://github.com/merhmood/react)@[b6978bc38f...](https://github.com/merhmood/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Thursday 2023-08-03 07:09:33 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[934bb31c09...](https://github.com/treckstar/yolo-octo-hipster/commit/934bb31c09ead000f17b6f2321b5b14dc95ad3a4)
#### Thursday 2023-08-03 07:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[7e1d97af9e...](https://github.com/mc-oofert/tgstation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Thursday 2023-08-03 09:56:53 by Justice

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
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[0d769e0ffa...](https://github.com/mc-oofert/tgstation/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Thursday 2023-08-03 09:56:53 by Jacquerel

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
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[f418bb0eff...](https://github.com/MCBCMF/MCBCMassacre/commit/f418bb0eff86ef3b8738132831a4304e328f4278)
#### Thursday 2023-08-03 10:49:53 by Kelvin Williams

Add files via upload

To @github @23andme @apple
Guys circulate far and wide FAST. 

BECAUSE I TAGGED YOUR COMPANIES I HAVE TO WARN YOU ABOUT CONNORS STEAK AND SEAFOOD, or any restaurant that gives you a free gift certificate. 

I don’t think they use the name Connors anymore but these photos show my mom, sister and my nieces (including one in the Katrina’s belly) just before they were MURDERED. I never noticed it on my phone but when I loaded these on a big screen to show people what my real mom and sis looked like (they made a porn to defame them, my mother would never do that—she is the primary reason they went to MCBC). I received them from a CIA impersonator pretending to be my sister. On TV I noticed three individuals. Brian, Annie and Michael behind my sister. I met all three of these individuals, all definitely CIA I know now in drastically differing roles from reality. Brian and Michael were homeless in ATL. Annie (director at one point of the CIA after Bill Burns was taken out after leaving THIS church) I first met in my sister’s kitchen. She told me she was the housekeeper. She was there to clean house to setup a #hotel. See that on Twitter under @asotc23. 

Michael, longtime CIA previously helped end @nasa space travel for just $2b. They spent only $5k on a sharpshooter and .22 rifle according to the Creator. They made a pretty  nice profit from SpaceX. 

So they know how to do the most with no money. Michael and Brian pretended to be homeless in Atl. 

This all started because Giles’s Sciences found out through routine testing of an HIV+ man that he was now negative. So Gilead did what they thought they had to do, kill him and the person who gave him “something “ … I’m rambling. 

Do this very simple thing with any gift certificate you receive. Mom always said “there’s no such thing as a free lunch.” She didn’t know what dinner would cost her—they were never served water! CALL WHOMEVER SENT IT TO YOU AND THANK THEM. IF THEY DONT KNOW WHAT YOURE TALKING ABOUT BURN IT. 

IF IT SOUNDS FISHYBURN IT. IF YOU WOULDNT SEND YOU A GIFT CERTIFICATE IF THE TABLES WERE REVERSED BURN IT. 

They are probably changing the name they operate under. But  Connors opened and I think closed everywhere I had friends go missing. Especially armed people (my sister was a probation officer and mom just a country bumpkin), and folks you can’t just walk in on (because of doormen, etc). 

BURN IT!!! Especially for new restaurants. BURN IT. THEY DONT. CHECK IDS. YOU WALK INTO THIS CIA TRAP AND YOURE GONNA DIE  

OK? Thanks.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c0c378ce5e...](https://github.com/treckstar/yolo-octo-hipster/commit/c0c378ce5e4480d8aac3a51c8a10ed8a0443affc)
#### Thursday 2023-08-03 12:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[e86e939461...](https://github.com/wrye-bash/wrye-bash/commit/e86e9394613357d0b5d94c4f4ebeea21c85516af)
#### Thursday 2023-08-03 12:42:15 by Infernio

Rework temporary file handling

View with whitespace diff off for an easier time (--ignore-all-space).

This turned out to be a lot more work than I thought. Really should have
been a branch, but I misjudged this horribly, then it kept growing...
Also not sure how feasible this would be to have as a branch without
breaking dev.

Wrye Bash's temporary files handling was actually a complete mess. There
were *three* different ways that random pieces of code were using it:
 - bass.getTempDir/newTempDir/rmTempDir
 - Path.temp and Path.untemp
 - Just use Path.baseTempDir/tempDir or even tempfile directly and do
   it completely manually.

These all had problems:
 - The bass APIs were very implicit - you would extract something to the
   'bass temp dir' and then access it via getTempDir in some other
   function, then remove the directory via rmTempDir in another
   function. XXX I'm still not done tracking this implicit mess down
   (see converters.py).
 - Path.temp did not guarantee that the file would be unique. This isn't
   really a problem for Wrye Bash right now, but would become a big
   problem if we ever wanted to allow multiple instances to run at the
   same time (which we do). Path.untemp also did some really weird I/O
   stuff that doesn't seem necessary at all and would just cost us a
   bunch of syscalls.
 - Path.baseTempDir/tempDir and tempfile required you to keep track of
   all the path manipulation and logic manually. After going through all
   this refactoring, trust me when I say that you do *not* want to do
   this manually. These places were few, thankfully, and none seem to
   have messed it up.

The new API (wbtemp.py) exposes two ways to do it:
 - Use TempDir or TempFile in a context manager. This is extremely
   simple and works very well. It guarantees that the file will be
   cleaned up, even if your logic becomes very complex or an exception
   occurs.
 - Use new_temp_dir/new_temp_file to create a temporary dir/file and
   manually clean it up via cleanup_temp_dir/cleanup_temp_file. These
   should be used *very sparingly*, only where absolutely needed.
   Right now we only have a single usage of manual temp files in
   dialogs.UpdateNotification and two usages of manual temp dirs (one in
   InstallerArchive.unpackToTemp and one in env.shellMakeDirs).

It also has other advantages:
 - Complexity is encapsulated to a single file.
 - Works even during (very) early boot (though doesn't seem to be
   needed right now?).
 - Should work perfectly with multiple instances of WB running at the
   same time (which isn't possible yet, but is a goal for the future).

There's one ugly wart. barb wants to extract archives to a temporary
folder, which then needs to survive a restart of WB, whereupon it will
be handled by the boot '--restore' handler. wbtemp, by design, does not
allow this and will clean up all created directories and files on exit.
To handle this, I used manual tempfile fiddling. Perhaps a future
refactoring of barb could fix this, but for now I think it's an
acceptable tradeoff for the massive improvements this commit brings us.

Some random stuff that got stuck in here:

Note that I got rid of the utf-8-sig encodings passed to 7z, the docs
say:

  Notes: The list file in Unicode charset can start with the BOM (byte
  order mark) character (U+FEFF). In that case 7-Zip checks that
  encoding of BOM corresponds to encoding specified with this switch
  (for UTF-16LE and UTF-16BE).

and:

  Default charset is UTF-8.

From https://7-zip.opensource.jp/chm/cmdline/switches/charset.htm
Very happy to see some of these terrible BOMs disappear from the
codebase.

Mopy/bash/basher/gui_fomod.py:
Some minor warning fixups in gui_fomod

Utumno:
Refactor compress7z:

The time is ripe for dropping the rel_dest param - note this drops a
couple of FName imports.

Closes #665

Co-authored-by: lojack5 <1458329+lojack5@users.noreply.github.com>
Co-authored-by: MrD <the.ubik@gmail.com>

---
## [mukeshparjapat143/spotify-clone](https://github.com/mukeshparjapat143/spotify-clone)@[fcca19bf23...](https://github.com/mukeshparjapat143/spotify-clone/commit/fcca19bf236aef58bf526ce8232ce1507147bea7)
#### Thursday 2023-08-03 14:09:29 by mukeshparjapat143

spotify clone

**Building a Spotify Clone with HTML, CSS, and JS**

Creating a Spotify clone using HTML, CSS, and JavaScript can be a fun and educational project that allows you to practice your web development skills. Though it won't have the full functionality and extensive music library of the actual Spotify platform, it can still provide a basic user interface and offer some similar features. Here's a brief overview of how you can get started:

1. **Project Setup:**
   Begin by setting up a new folder for your project. Inside, create three files: `index.html`, `styles.css`, and `script.js`. Link the CSS and JavaScript files to your HTML file using `<link>` and `<script>` tags.

2. **HTML Structure:**
   Construct the basic layout of your Spotify clone using HTML. Create a header, a main content area to display albums and songs, and a footer for playback controls. You can also include some dummy content to style and structure your elements.

3. **CSS Styling:**
   Utilize CSS to design the user interface, making it visually appealing and resembling Spotify's aesthetics. Focus on the layout, colors, fonts, and icons. CSS frameworks like Bootstrap or Materialize can help speed up the process and make the design more consistent.

4. **JavaScript Functionality:**
   Implement JavaScript to add interactivity to your Spotify clone. Create functions to handle user interactions, such as playing/pausing songs, changing tracks, and displaying album details. You can use DOM manipulation methods like `document.getElementById` to access and modify HTML elements.

5. **Audio Playback:**
   To simulate audio playback, create a playlist of songs with URLs to audio files hosted online or locally. Use the HTML5 `<audio>` element or the Web Audio API to control audio playback and enable features like play, pause, volume control, and track progress.

6. **Data Management:**
   Since you won't have access to Spotify's massive database, you can create a local JavaScript array to store the song and album data. This array will represent your music library, and you can use it to display album covers, track names, artists, etc.

7. **Search Functionality:**
   Implement a simple search feature to filter and display relevant songs or albums based on user input. You can use JavaScript's array methods like `filter` or `find` to achieve this functionality.

8. **Responsive Design:**
   Ensure your Spotify clone is responsive and can adapt to different screen sizes and devices. Test it on various devices to ensure it looks good and functions properly on desktops, tablets, and mobile phones.

9. **Testing and Debugging:**
   Thoroughly test your Spotify clone to identify and fix any bugs or issues. Use browser developer tools to debug JavaScript code and ensure smooth functionality.

10. **Deployment:**
   Once your Spotify clone is complete, you can deploy it online using hosting services like GitHub Pages, Netlify, or Vercel. This way, you can share your creation with others and showcase your web development skills.

Remember that building a complete Spotify clone is an ambitious project, and it's essential to manage your expectations. This basic version will provide a good learning experience and a foundation for more complex projects in the future. Happy coding!

---
## [AnywayFarus/Fluffy-STG](https://github.com/AnywayFarus/Fluffy-STG)@[8ddcb6ba45...](https://github.com/AnywayFarus/Fluffy-STG/commit/8ddcb6ba45b3d6e3bb4c6045c04ccdd296422a18)
#### Thursday 2023-08-03 14:48:06 by SkyratBot

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
## [Smalltasty/tgstation](https://github.com/Smalltasty/tgstation)@[03c964ac45...](https://github.com/Smalltasty/tgstation/commit/03c964ac45e727543aac85ad817df89a7555fb31)
#### Thursday 2023-08-03 15:46:06 by LemonInTheDark

Reworks Duffel Bags (Zippers) (#76313)

## About The Pull Request

Reworks duffel bags in line with oranges proposed plan.


![image](https://github.com/tgstation/tgstation/assets/58055496/126743dd-d7b8-47e0-bdd8-a0caec39c515)

Basically, instead of just making you slower all the time, they make you
slower while you have them open, but give you the same speed while
they're closed.
As a trade off, opening and closing them takes time, 2.1 seconds
(matches the sound) and 0.5 respectively.


https://github.com/tgstation/tgstation/assets/58055496/555d2cd0-038e-4b0b-a693-0c66dac16f5b

[Adds support for limiting extra storage, uses it to make syndie stuff
cool](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

[d0b2bbf](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

Syndicate bags currently ignore downsides by just ignoring the slowdown,
but that's kinda boring so let's just buff em instead.

They now support holding a limited amount of bulky items (3), filtered
down to things that would otherwise constitute going loud (or otherwise
be useful to carry around as a loudish traitor)

I may have gone a bit overboard on what I whitelisted here, lemme know
yeah?

I also did some fenangling with backpack uses of create_storage, I don't
like this pattern it was a bad idea I think.

## Why It's Good For The Game

I'm unsure if these delays enough, I think any length of time is decent
since it means you need to stop moving and focus on it for a bit.
My hope is this will make them a proper sidegrade, rather then something
that goes unused/acts as newbie bait

## Changelog
:cl:
balance: Duffelbags will now only make you slow while they are unzipped.
As a tradeoff, you now need to stand still and zip/unzip them to access
their contents/not move real slow.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [zerbina/nimskull](https://github.com/zerbina/nimskull)@[c4250cc115...](https://github.com/zerbina/nimskull/commit/c4250cc11536bf6c8922bbd192d2ec39142d46d9)
#### Thursday 2023-08-03 15:50:33 by Saem Ghani

Parser: drop direction `reports` dependencies

This removes direct dependency on `reports`, but an indirect one still
exists via `msgs`. It's pretty trivial indirection at the moment, but
after dropping direct reports dependencies the API can be changed more
drastically.

A number of changes were required in order to make this possible, here
is an overview:

- smaller parser public API & simpler implementation
- added `parse` compiler command, for devs
- parser error message improvements
- fixes to `astrepr` logic and output
- lots of style clean-ups

Details
=======

Slimmer `parser` Public API
---------------------------

Previously the parser had many public procedures (eg: `isOperator`,
`getTok`, `skipComment`, etc) that would allow fine grained control for
other modules.

There are many issues with this:
- there are no consumers of this API
- lots of public API surface to test
- the API itself was bad, it conflated lexing and parsing

The public API surface for the parser has been reduced significantly,
now consisting of:
- `openParser`
- `parseTopLevelStmt`
- `parseAll`
- `closeParser`
- `parseString`

That's it, which frankly reads far more sensibly.

Simplified `parser` Implementation
----------------------------------

- removed `InternalReport`, `reports_parser`, and `reports_enum` imports
- introduced diagnostics for the parser, akin to the lexer, `ParseDiag`
- `ParseDiag` favours data over strings
- `ParsedNode` now has its own kind enum, mostly a subset of
   `TNodeKind`, but entirely compatible

Consolidated a pattern within the parser, where a node was created with
the current token's information, and then the token was immediately
consumed via `getTok` to advance the `lexer`. This is captured in the
newly introduced `newNodeConsumingTok`.

Long-term, itemizing these traversal/consumption patterns will make the
parser logic not only more regular, but also highlight oddities in the
grammar as the implementation will be convoluted.

Parsing/Diagnostics Performance
-------------------------------

`ParsedNode` uses a lightweight `ParsedToken`

Introduce `ParsedToken`, a smaller data type, storing the least amount
of data required from `lexer.Token` for `ParsedNode`. This not only
saves memory, but the runtime performance impact on my machine is
roughly 33% faster full compiler testament run for all targets

- before change: 3+ minutes
- after change:  2+ minutes

Added specialized diagnostic/report kinds for:
- empty accent quote when ident expected
- msg for asm statements without a string literal
These reduces the amount of string data carried around in the compiler.

Improved Custom Numeric Literal Handling
----------------------------------------

- the `lexer` still does silly things for lexing these
- it just does less work and produces better data
- fewer string operations and hacks are required by the `parser`

Parser Diagnostic/Reporting - Invalid Indentation
-------------------------------------------------

- now has correct source line information
- tracks instantiation and submission location
- has the appropriate severity
- improved phrasing for indent error from possible missed `=` character
- adjusted tests for the above

Parser Diagnostic/Reporting - Malformed Call Syntax
---------------------------------------------------

- `parser` detects malformed calls and sets better line info
- net-net the user will have a better chance to find the issues

Parser Diagnostic/Reporting - Misc
----------------------------------

- token rendering call out keywords via prefix, eg: `keyword template`
- inconsistent spacing style check shows the problematic source

Removed unused report kinds:
- `rparIdentOrKwdExpected`
- `rparRotineExpected`
- `rparPragmaAlreadyPresent`

Parse Compiler Command
----------------------

`parse` command:
- added `parse` command, which outputs the parsed ast for a file
- usage: `nim parse foo.nim`
- super useful for diffing parser output changes
- heavily leverages `astrepr`

`astrepr` module:
- `astrepr.treeRepr` now works for `ParsedNode`, was previously broken
- AST trasversal is now exhaustive and breakages less likely to pass CI

`astrepr` output improvements, mainly for `ParsedNode`:
- `astrepr` now shortens ParsedNodeKind enum
- output now includes line and column information
- comments no longer result in excessive new line output
- fixed many formatting issues for `ParsedNode` output
- improved `astrepr`'s output for custom numeric literals

Canonical Filenames Performance Issue
-------------------------------------

Also discovered a performance issue with canonical filenames option and
the `nimdebugstacktrace` option. Removed some of the pain, but canonical
file paths result in significant performance issues due to filesystem
IO. I've fixed part of it and filed an issue:
https://github.com/nim-works/nimskull/issues/546

Other Improvements
------------------

- introduced `debugutils.setFrame` template for frame msg hints
- above `setFrame` avoids the canonical path performance hit
- removed circular dependency between `ast` and `options` module
- document unused parser reports and other outliers
- move `isImportedException` to `ast/types`, whice drops `front/options`
  cyclic depencdency from `ast/ast_query`
- fixed docs in nimlexbase, also easier to understand
- `ast.toPNode` now handles `nil` input
- `syntaxes.parseFile` returns `ParsedNode`, allows avoiding unnecessary
  conversions in future use cases where only `ParsedNode` is required

Special Mentions
----------------

Thanks, clyybber and zerbina for the reviews!

Misc
----
- remove blank space characters from otherwise empty lines
- remove awful code style of `0 < foo.len`
- fixed a number of typos in comments
- adjusted a few tests to ensure they pass

---
## [IProduceWidgets/space-station-14](https://github.com/IProduceWidgets/space-station-14)@[31607a0be0...](https://github.com/IProduceWidgets/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Thursday 2023-08-03 16:01:31 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [atlanticwave-sdx/datamodel](https://github.com/atlanticwave-sdx/datamodel)@[bf281c288d...](https://github.com/atlanticwave-sdx/datamodel/commit/bf281c288d2dbccb3264bfbf2d4ddc7fbb691f45)
#### Thursday 2023-08-03 16:09:40 by Sajith Sasidharan

Use setuptools as the build backend, rather than flit

I think we can, and should, eventually switch to flit -- because flit
is faster and stricter, and because it catches more mistakes such as
when you build packages on a source tree with uncommitted changes.

But I have painted myself into a corner by the module naming
convention "src/sdx/datamodel" rather than "src/sdxdatamodel".  Flit
expects the the top-level module name to follow project name.
Setuptools is a little more forgiving, so using setuptools as build
backend for now will help us make progress.

Flit's strictness here is better because it also makes sure that
editable installs will continue to work.  With the former module
naming scheme, we have "src/sdx/datamodel" here, and "src/sdx/pce" in
pce, and because of that, we can't have editable installs in pce...

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[fff87e4a50...](https://github.com/sourcegraph/sourcegraph/commit/fff87e4a50ce83d4f0a55b144c144eb592385a56)
#### Thursday 2023-08-03 16:17:17 by Felix Kling

sveltekit: Setup unit tests with vitest (#54953)

This PR adds vitest and faker for unit testing, and to use it properly
already I refactored the promise->store helper to be more flexible.

**Unit testing**
vitest works prefectly together with vite (it's from the same
author/community). It will use the same configuration and so there is
very little additional configuration necessary.
I only had to update vite.config.ts to not overwrite `process` (but
according to https://vitejs.dev/config/shared-options.html#define I
might not be doing it right anyway... will look into this another time).

The API is pretty compatible with jest, so there shouldn't be any
surprises.

Tests can be run with `pnpm vitest`.

**Faker**
I stared to use faker on a differnt branch to generate more (and more
realistic) test data for storybook stories and unit test. Eventually I'd
like to use this to generate mock data for any of our GraphQL APIs. One
great feature is the ability to _seed_ the random number generator so
that you can get random but repeatable values in tests.

**Promise<>store utility**
Working with promises in a reactive way can be tricky. There is a risk
of stale data ovewriting current data when an older promise resolves
after a newer one.
Observables can help here but since we are trying to move away from
them, I introduced a simple store to handle promises. I extended it now
to handle more cases, especially being able to access the previous value
while a new promise is loading. The API might seem clunky (and I'd be
happy to improve it eventually), but this way makes it easier to
remember to call `set` whenever the promise changes.



## Test plan

`pnpm vitest`

Run dev server, open pages affected by promise store changes (repo
pages) and verify that they behave as expected.

---
## [Raxen001/raxen001.github.io](https://github.com/Raxen001/raxen001.github.io)@[33d74f8f96...](https://github.com/Raxen001/raxen001.github.io/commit/33d74f8f96f6dcb89471e05a7aac78bd19bff2bb)
#### Thursday 2023-08-03 17:10:58 by raxen001

i dont know what i did or how i did it somehow everything seems to work for now please for the love all that if fucking holy do not ever try to web design again if you do future raxen and if you come across this commit message please note that at this point you knew you were not fit for webdesing it just takes too much of your sanity stick with devops, kernel, or anything that requires you not write ui

---
## [freedoom/freedoom](https://github.com/freedoom/freedoom)@[a828330d25...](https://github.com/freedoom/freedoom/commit/a828330d25e950933bc97ef5ba5630e2a2dca93a)
#### Thursday 2023-08-03 17:16:57 by mc776

levels: more minor fixes. (#1040)

* levels: fix e1m2 tutti frutti around exit door.

Also took the liberty of fixing a longtime pet peeve I had about the really bright grey-white of the exit room steps clashing with the rest of the room for no apparent reason. (It looks less bad with Korp's new greys but we're not adding those yet...)

* levels: fix floating candle on map22.

It's fine until you actually use the secret, at which point it snaps to the top of the lowering platform.

* levels: more minor fixes.

Mostly for objects "floating" with a tiny bit of their hitbox rounded to be overlapping a higher adjacent floor.

E1M8
Inside the pillars containing the painlords there are two that spawn gore (and a dead player) in lieu of painlords only on easy. These have now been edited so that in each pillar the gore appears whenever the painlord does not. (The player has also been changed to a gore actor.)

Map03
Floaties by the first door switch.

Map23
Central room with the barrels and combat slugs has several gore decorations that do not appear on hard, but do not block movement nor represent any living monsters that might appear there in hard. Flagged to appear in all skill levels (and also not be flagged ambush).

Map25
1-pixel vertical misalignment on line 44.

Map28
Floaty medikit(s?) near (-955,-435), moved away from the double teleport pad.
Fixed the textures on that door now that the SLOPPY textures have been updated
Moved stuff around the starting skull switch so you start with a screen full of skull again.

Map29
Floaty shellbox 444.

* levels: more minor fixes.

Mostly to address #1043.

Map09
- Moved the crates in front of the eastern teleport door to keep the player from potentially falling into the gap between the big crate and the main crate rack and softlocking. The small step-crates are now also properly aligned with the flat they use.

Map14
- The entire lower floor of the big octagon room has been lowered to -56 from -48. This restores access to the alcove in front of the minigun secret, and also better aligns with the textures of several surrounding walls.
- Merged the sectors of the yellow key cage teleporter pad so the lights would sync.

Map15
- A room will lower two teleporters when you step in and two worms will warp in through those teleporters in hard, one in medium, none in easy. It looks bugged where the worms don't appear and absolutely nothing shows up, so pickups are revealed instead when they don't.

Map18
- Added one more step crate to let the player directly access the necromancer soul sphere (and the health bonus tucked away in the corner) without retracing their route back to the upper ledge.

Map25
- Got rid of that starting elevator once and for all. The only purpose in forcing that starting gunshot was to make that first room marginally more awful to pistol-start. Moved the shotgun and shells to the "outside" platforms to make up for it.
- Widened the side windows facing the yellow key so the trilobites have room to move.
- Shrunk down the exit line to make it completely impossible to trigger it while the painlord/necromancer standing there is alive.
- Added more monster blockers to the RL warp-in ambush closet, as the worms would still sometimes warp in both on the same side. I've also made the destination sectors larger as that simplifies the underlying geometry a bit.
- Flagged everything in the deathmatch arena multi-only.
- Thing 445 (last monster before SSG in hard mode) is now a pain lord instead of an octaminator.

* levels: more minor fixes.

Map13
Exit teleport pad lines now block monsters.

Map18
End soulsphere secret is now tagged as secret.

Map19
The straferun armour trench setup could not possibly work without having the worms below block your movement sometimes. The trench is now fenced off and the platform accessible by bridge; the pinkies are now spectres outside of easy and hard gives you two more of them; they can only harm you by teleporting.

* levels: readjust map28 skull.

The vertical offset would no longer be needed after #1047; however the tiling is a bit off if we need to offset this horizontally due to the additional trim, so a new linedef was added.

* levels: map26 minor fixes.

The secret blue lift switch error message would indicate it's a "door" which despite being correct from an engine point of view doesn't reflect its actual function.

The red armour secret is now player-shoot only, and the wall breach effect is instant.

* levels: fix high jump platform texture alignment.

---
## [Tilk1/Shiptest](https://github.com/Tilk1/Shiptest)@[f07cb3bd3b...](https://github.com/Tilk1/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Thursday 2023-08-03 17:25:53 by Bjarl

Overmap 4.7: Gas Giants, More Storms, 8 hours of work (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds some content based on sprites I saw sitting around in the overmap
file, mainly carp storms and dust storms.
Carp storms throw space carp at you. Dust storms throw dust.

Also adds gas giants, a place to harvest gasses if you're low, and don't
want to stop at a planet. They *should* be persistent. Your average gas
giant mix is very cold, very high pressure, and absolutely not something
you want to breathe. Plasma giants are cold and allow harvesting of
plasma.

Electrical storms have been rebalanced to not Explode Your Ship. Minor
and Moderate ones will now only shock and damage objects and mobs, major
ones will still explode you, so remain careful.



![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/84257435-32de-45a5-8a8d-d9aa30021f90)
Example overmap with some carp migrations.


https://github.com/shiptest-ss13/Shiptest/assets/94164348/5c30fa9a-c7e4-453a-99a6-5c3564946b26
flying through a minor electrical storm


https://github.com/shiptest-ss13/Shiptest/assets/94164348/db7fcdf0-3f7a-4830-821e-a4a7106632ba
gas giant


https://github.com/shiptest-ss13/Shiptest/assets/94164348/0a5f0575-b7d9-4e3f-9e13-942a8fdf8617

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/6bb5ddc2-373a-4dd9-9a63-0f6f0bdd26a9)

plasma giant

https://github.com/shiptest-ss13/Shiptest/assets/94164348/9268c293-39f3-4306-889e-f8c19067cec1

A particularly dusty solar system

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/5b27e2a8-1cc1-47bb-95b8-e9d5c3ba8e71)


I might try and fix ion storms but I don't see what might be breaking
them.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More content for the overmap / balancing out some old systems
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Planets now can (and will) play a sound when you land on them
add: Gas / Plasma giants, cold, dockable worlds with absolutely no
livable surfaces. As a matter of fact it's all chasm. All highly
pressurized, gas rich, chasm.
add: Dust storms and carp storms now grace the sector. 
add: physical storms (dust, carp, asteroid), will now only trigger if
you go through them too fast. Take it easy and you might get through
unscathed.
add: planets will now have a name on the overmap
add: overmap hazards now have a description
tweak: Space carp can now survive in hyperspace, their natural habitat
balance: minor and moderate electrical storms will no longer Explode you
balance: asteroid storm lists have been trimmed of Extremely Deadly ones
fix: restores planet naming behavior, I believe this was unintentionally
removed at some point
fix: Ion storms work again. Fuck you whoever touched them last.
soundadd: planet_landing_1 and planet_landing_2, (tech_notification and
sos_morse_code from CM respectively. I don't know how to attribute
properly please tell me how if you have issue with this attribution
because I did not make these sounds they're from Colonial Marines)
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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[27d46f1717...](https://github.com/tgstation/tgstation/commit/27d46f17173034b805d6ef064d4db31c7e34b26d)
#### Thursday 2023-08-03 17:34:49 by OrionTheFox

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
## [goyalkunjann/HackerRank](https://github.com/goyalkunjann/HackerRank)@[4e06aa3fd9...](https://github.com/goyalkunjann/HackerRank/commit/4e06aa3fd9a6927e2f1aa0694336f19b58d86327)
#### Thursday 2023-08-03 18:01:36 by goyalkunjann

Bill Division

Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: . Anna declines to eat item  which costs . If Brian calculates the bill correctly, Anna will pay . If he includes the cost of , he will calculate . In the second case, he should refund  to Anna.

Function Description

Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill
Input Format

The first line contains two space-separated integers  and , the number of items ordered and the -based index of the item that Anna did not eat.
The second line contains  space-separated integers  where .
The third line contains an integer, , the amount of money that Brian charged Anna for her share of the bill.

Constraints

The amount of money due Anna will always be an integer
Output Format

If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., ) that Brian must refund to Anna. This will always be an integer.

Sample Input 0

4 1
3 10 2 9
12
Sample Output 0

5
Explanation 0
Anna didn't eat item , but she shared the rest of the items with Brian. The total cost of the shared items is  and, split in half, the cost per person is . Brian charged her  for her portion of the bill. We print the amount Anna was overcharged, , on a new line.

Sample Input 1

4 1
3 10 2 9
7
Sample Output 1

Bon Appetit
Explanation 1
Anna didn't eat item , but she shared the rest of the items with Brian. The total cost of the shared items is  and, split in half, the cost per person is . Because , we print Bon Appetit on a new line.

---
## [eltociear/gorilla](https://github.com/eltociear/gorilla)@[f3ce849a8c...](https://github.com/eltociear/gorilla/commit/f3ce849a8c46f5683477ff26ec34dc04518c294b)
#### Thursday 2023-08-03 18:09:00 by Shishir Patil

Releasing Torch and TF weights 🚀  (#16)

In this PR we release the weights for Gorilla 0-shot model for Torch Hub
and Tensorflow Hub APIs 🎉

It chooses from 626 (exhaustive) TensorFlow v2 APIs, and 94 (exhaustive)
Torch Hub in a 0-shot fashion (without any retrieval). In the spirit of
being open, we do not filter, nor carry out any post processing either
to the prompt nor response 🎁 We would like to remind the community that
neither of `gorilla-7b-hf-v0`, `gorilla-7b-tf-v0`, nor
`gorilla-7b-th-v0` have any generic chat capability. We do have a model
with all the 1600+ APIs which also has generic chat capability, which we
release slowly to accommodate server demand.

You can play around with Gorilla either through our hosted colab (OpenAI
Chat completion API compliant) or you can download and run it locally.

Thank you for all the comments and suggestions so far! Keep them
coming!!!

🚀 🚀 🚀

---
## [MahleAaronS/ThemaniacPlayground](https://github.com/MahleAaronS/ThemaniacPlayground)@[b73714966e...](https://github.com/MahleAaronS/ThemaniacPlayground/commit/b73714966e3c3a217d91896d219811239440ed92)
#### Thursday 2023-08-03 20:34:28 by Aaron Stokes

Update install_chocolatey.txt

Sure! Here's a famous passage from Shakespeare's play, Hamlet:

"To be or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;"

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a288abcaf2...](https://github.com/tgstation/tgstation/commit/a288abcaf2a6b6c44edade8265a66b9ba3f0e67b)
#### Thursday 2023-08-03 21:30:41 by san7890

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ebbc45b161...](https://github.com/tgstation/tgstation/commit/ebbc45b1616c08d2dc0b6e6ce48258f68eefd46a)
#### Thursday 2023-08-03 21:43:33 by distributivgesetz

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
## [V-Sekai/manuals](https://github.com/V-Sekai/manuals)@[9e5a02f7de...](https://github.com/V-Sekai/manuals/commit/9e5a02f7dee54a67e4c94271b9dc14ad570265f0)
#### Thursday 2023-08-03 21:47:55 by K. S. Ernest (iFire) Lee

Add idle RPG world feature proposal

This commit adds a new file proposing the implementation of an idle RPG world feature in V-Sekai. The proposed solution includes setting elements such as a cozy place, interactive objects like couches and mirrors, and gameplay features like socializing with friends and playing an idle RPG game for rewards. The positive consequences include increased user engagement, prolonged interaction within the V-Sekai world, and enhanced socialization among players. However, there may be negative consequences such as increased development time and unbalanced gameplay if not properly designed. This feature cannot be easily worked around with a few lines of script due to its complexity. Creating this feature aligns with our goal of providing a compelling virtual world experience in V-Sekai.

---
## [JuliaLang/julia](https://github.com/JuliaLang/julia)@[b86b64f84e...](https://github.com/JuliaLang/julia/commit/b86b64f84eaa6fb49e437a859c81783b15b81550)
#### Thursday 2023-08-03 22:08:08 by Keno Fischer

WIP: Add explicitly wrapping versions of integer arithmetic

This adds operators `+%`, `-%`, `*%`, which are equivalent to the
non-`%` versions, but indicate an explicit semantic expectation that
twos completement wrapping behavior is expected and correct. As discussed
at JuliaCon 2014 and every year since, users have often requested
a way to opt into explicit overflow checking of arithmetic, whether
for debugging or because they have regulatory or procedural requirements
that expect to be able to do this. Having explicit operators for
overflowing semantics allows use cases that depend on overflow behavior
for correct functioning to explicitly opt-out of any such checking.

I want to explicitly emphasize that there are no plans to change
the default behavior of arithmetic in Julia, neither by introducing
error checking nor by making it undefined behavior (as in C). The
general consensus here is that while overflow checking can be useful,
and would be a fine default, even if hardware supported it efficiently
(which it doesn't), the performance costs of performing the check
(through inhibition of other optimization) is too high. In our experience
it also tends to be relatively harmless, even if it can be a very
rude awakeing to users coming from Python or other languages with
big-default integers.

The idea here is simply to give users another tool in their arsenal
for checking correctness. Think sanitizers, not language change.
This PR includes a macro `@Base.Experimental.make_all_arithmetic_checked`,
that will define overrides to make arithmetic checked, but does not
include any mechanism (e.g. #50239) to make this fast.

What is included in this PR:
 - Flisp parser changes to parse the new operators
 - Definitions of the new operators
 - Some basic replacements in base to give a flavor for using the
   new operator and make sure it works

Still to be done:
 - [] Parser changes in JuliaSyntax
 - [] Correct parsing for `+%` by itself, which currently parses as `+(%)`

The places to change in base were found by using the above-mentioned
macro and running the test suite. I did not work through the tests
exhaustively. We have many tests that explicitly expect overflow and
many others that we should go through on a case by case basis. The
idea here is merely to give an idea of the kind of changes that
may be required if overflow checking is enabled. I think they can
broadly be classed into:

- Crypto and hashing code that explicitly want modular arithmetic
- Bit twidelling code for arithmetic tricks (though many of these,
  particularly in Ryu, could probably be replaced with better
  abstractions).
- UInt8 range checks written by Stefan
- Misc

---
## [OnionUI/Onion](https://github.com/OnionUI/Onion)@[8383dda087...](https://github.com/OnionUI/Onion/commit/8383dda087ac09f4e6bdbd52a0d034dcc853a013)
#### Thursday 2023-08-03 22:45:02 by XK

FIX: ScummVM scrollbars - revert from 2.8.0git to 2.7.1stable (#1092)

## Overview
Fix missing scrollbars in options containers. 
Adds new bin & new themes.

ScummVM downgraded to 2.7.1 STABLE built from source with same engine
support as before - 2.8.0 master branch has not been updated with the
container scroll-bar fix that 2.7.1 has.

Release announcement: https://www.scummvm.org/news/20230731
Release notes:
https://downloads.scummvm.org/frs/scummvm/2.7.1/ReleaseNotes.html
GH branch: https://github.com/scummvm/scummvm/tree/branch-2-7-1

<img
src="https://github.com/OnionUI/Onion/assets/47260768/10dce908-0e76-4f53-bd53-037db0467af1"
width="400" alt="Run ScummVM_000"><img
src="https://github.com/OnionUI/Onion/assets/47260768/86848e29-a304-4c9e-ae1f-1c4d491d044a"
width="400" alt="Run ScummVM_001">

## To test

Testing downscaler:

- [x] Load a game engine that would natively run at 800x600 (sword25
with Broken Sword 2.5) - If it boots at all with a clear image DS is
working

Testing broken sword 2.5 fix for crash after menu (when intro video
starts):

- [x] As above, this killed the game after the main menu, if you make it
past the main menu you're good.

Testing GUI -> 640 x 480: 

- [x]  GUI can be freely scaled to its smallest size

Testing scrollbars:

- [x] Open global options -> Keymaps & observe a scrollbar is now
present.

## Build details
<details>

```markdown

Backend... miyoo (SDL 1.2.15), 16bit color, high resolution, TinyGL, savegame timestamp, HQ and Edge scalers, aspect ratio correction, Lua, virtual keyboard
WARNING: Disabling engine Hpl1 because the following dependencies are unmet: OpenGL with shaders
WARNING: Disabling engine Tetraedge because the following dependencies are unmet: libtheoradec

Engines (builtin):
    SCUMM [all games]
    Access
    ADL
    AGI
    AGOS [all games]
    Adventure Game Studio
    Sanitarium
    Lord Avalot d'Argent
    Beavis and Butthead in Virtual Stupidity
    Blade Runner
    The Journeyman Project 2: Buried in Time
    CGE
    CGE2
    Chewy: Esc from F5
    Cinematique evo 1
    Magic Composer
    Cinematique evo 2
    Lost Eden
    Cryo Omni3D games [all games]
    Macromedia Director
    Dungeon Master
    Dragon History
    Blazing Dragons
    Drascula: The Vampire Strikes Back
    Dreamweb
    Freescape
    Glk Interactive Fiction games
    UFOs
    Gobli*ns
    The Griffon Legend
    Grim [all games]
    Groovie [all games]
    Hades Challenge
    Hyperspace Delivery Boy!
    Hopkins FBI
    Hugo Trilogy
    Hypnotix Inc.
    In Cold Blood
    Illusions Engine
    Kingdom: The Far Reaches
    Kyra [all games]
    Labyrinth of Time
    The Last Express
    Lilliput
    Lure of the Temptress
    MacVenture
    MADE
    MADS [all games]
    Mohawk [all games]
    Mortevielle
    mTropolis
    Mutation of JB
    Myst 3
    Nancy Drew
    Neverhood
    Nikita Game Interface
    Parallaction
    The Journeyman Project: Pegasus Prime
    Red Comrades
    Pink Panther
    Playground 3d: the testing and playground environment for 3d renderers
    Plumbers Don't Wear Ties
    The Prince and The Coward
    Private Eye
    Flight of the Amazon Queen
    SAGA [all games]
    SAGA2
    SCI [all games]
    The Lost Files of Sherlock Holmes
    Beneath a Steel Sky
    Sludge
    The Longest Journey
    Star Trek 25th Anniversary/Judgment Rites
    Mission Supernova
    Broken Sword
    Broken Sword II
    Broken Sword 2.5
    Teen Agent
    TestBed: the Testing framework
    Tinsel
    Starship Titanic
    3 Skulls of the Toltecs
    Tony Tough and the Night of Roasted Moths
    Toonstruck
    Touche: The Adventures of the Fifth Musketeer
    Trecision Adventure Module
    TsAGE
    Bud Tucker in Double Trouble
    Little Big Adventure
    Ultima
    Voyeur
    WAGE
    Wintermute [all games]
    World of Xeen
    Z-Vision

Engines Skipped:
    Hpl1
    Tetraedge

WARNING: This ScummVM build contains the following UNSTABLE engines:
    Lord Avalot d'Argent
    Lost Eden
    Dungeon Master
    Grim [Escape from Monkey Island]
    In Cold Blood
    Kingdom: The Far Reaches
    The Last Express
    Lilliput
    MacVenture
    MADS [MADS V2]
    Mohawk [Where in Time is Carmen Sandiego?]
    Mutation of JB
    Nancy Drew
    Playground 3d: the testing and playground environment for 3d renderers
    Sludge
    Star Trek 25th Anniversary/Judgment Rites
    TestBed: the Testing framework
    WAGE
    Wintermute [Wintermute3D]

```
</details>

---
## [Macaulay2/Workshop-2023-Minneapolis](https://github.com/Macaulay2/Workshop-2023-Minneapolis)@[77ea22a172...](https://github.com/Macaulay2/Workshop-2023-Minneapolis/commit/77ea22a1721eead4b5fd8472dfed5a563762fbec)
#### Thursday 2023-08-03 23:14:57 by Michael DeBellevue

Attempted speed improvements, needs second opinion.

I tried to speed up the core computations in the following ways:

1. Added a function ACol, which computes the i'th column of the A
   matrix (but as a list, so calling
		for i to n list ACol(n,i)
	returns the transpose of the A matrix)
2. Memoizing ACol (by placing "memoize" in front of its definition)
3. I realized that the "compositions" builtin function seems to return
   compositions in revlex order.  In other words, the following returns
the set of compositions in lex order:
		for comp in compositions(n,k) list (reverse comp)
	this means we can remove the need to sort compositions by
rewriting the entry calculator to run through the composition in reverse
order.

Implementing these changes resulted in significant speed improvements
when I called faceMapik and degenMapik individually, but not when I
called faceMapi and not when I called the simplicialModule constructor
on a real complex.  It is faster when I call simplicialModule with
degeneracy set to true, because degenMapi is still faster.
  Furthermore, faceMapi becomes slower when ACol is memoized.  I'm very
confused as to why this is the case.  Some thoughts:
1. An obvious guess is that I goofed and that the code for faceMapi is
   somehow still running the same code as before.  I couldn't see any
reason why this would be the case, but I would appreciate another set of
eyes to make sure I didn't miss something stupid.
2. compositions(n-1,j) runs faster after compositions(n,k) has been
   called (for any j,k), so there might be some kind of caching speedup that's
happening in faceMapik that's errasing the speed gain.  I'm not
convinced by this, because calling ABuilder(n,k) doesn't seem to speed up ABuilder(n-1,j) for any values of n,j.
But I can't think of anything else.

I put the modified functions in SimplicialMapUtilities_Modified and
SimplicialModule_Modified, with "Modified" appended at the end of all of
them (faceMapi -> faceMapiModified, faceMapik -> faceMapik -> Modified,
etc). so that testing is easier to do.  Let me know if you have any
questions or if you can spot anything.

---
## [MortoSasye/Skyrat-tg](https://github.com/MortoSasye/Skyrat-tg)@[a1609c4536...](https://github.com/MortoSasye/Skyrat-tg/commit/a1609c4536fe05f95560bd1a1be4607b944ee5a5)
#### Thursday 2023-08-03 23:28:06 by SkyratBot

[MIRROR] [NO GBP] Fixes clown car + deer collision  [MDB IGNORE] (#22709)

* [NO GBP] Fixes clown car + deer collision  (#77076)

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

* [NO GBP] Fixes clown car + deer collision

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---

