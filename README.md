## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-21](docs/good-messages/2022/2022-01-21.md)


1,805,406 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,805,406 were push events containing 2,740,079 commit messages that amount to 206,641,062 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[f1af1046be...](https://github.com/cockroachdb/cockroach/commit/f1af1046bec1215130ed1a872d1fd26f7cb196c2)
#### Friday 2022-01-21 00:16:33 by craig[bot]

Merge #73883 #74823

73883: tracing: pool and reuse spans r=andreimatei a=andreimatei

This patch adds sync.Pool-ing and reuse to tracing spans, so that they
don't need to be dynamically allocated on every span creation. This has
a big effect on the heap footprint.

Conceptually, a span is made available for reuse on Finish(). In
practice, it's more complicated because there can still be references of
the span used concurrently with Finish(), either internally in the
tracing library or externally. The external ones are bugs by definition,
but we want to avoid some particularly nasty consequences of such bugs.

The BenchmarkTracing results below show that this saves around 10KB
worth of heap allocations per simple query, when tracing is enabled
(minimal tracing: TracingModeActiveSpansRegistry). I believe the span
allocations go from being serviced from the shared heap to being
serviced from CPU-local freelists, since they become small enough. In
the single-node case, this is 25% of the query's allocations. As can be
seen in the benchmarks below in the differences between the trace=on and
trace=off rows, the impact of tracing is big on memory footprint; with
this patch, there's not much impact.

```
name                               old alloc/op   new alloc/op   delta
Tracing/1node/scan/trace=off-32      19.7kB ± 1%    19.7kB ± 1%     ~     (p=0.768 n=10+5)
Tracing/1node/scan/trace=on-32       29.2kB ± 0%    22.0kB ± 0%  -24.85%  (p=0.001 n=10+5)
Tracing/1node/insert/trace=off-32    38.5kB ± 1%    38.4kB ± 1%     ~     (p=0.440 n=10+5)
Tracing/1node/insert/trace=on-32     45.5kB ± 1%    38.7kB ± 1%  -15.03%  (p=0.001 n=10+5)
Tracing/3node/scan/trace=off-32      68.1kB ± 3%    67.9kB ± 3%     ~     (p=0.768 n=10+5)
Tracing/3node/scan/trace=on-32       86.8kB ± 2%    75.3kB ± 2%  -13.21%  (p=0.001 n=9+5)
Tracing/3node/insert/trace=off-32    88.1kB ± 5%    90.8kB ± 7%     ~     (p=0.112 n=9+5)
Tracing/3node/insert/trace=on-32     96.1kB ± 3%    89.0kB ± 2%   -7.39%  (p=0.001 n=9+5)
```

Unfortunately, pooling spans only saves on the size of allocations, not
the number of allocations. This is because the Context in which a Span
lives still needs to be allocated dynamically, as it does not have a
clear lifetime and so it cannot be re-used (plus it's immutable, etc).
Before this patch, the code was optimized to allocate a Span and a
Context together, through trickery (we had a dedicated Context type,
which we now get rid of). So, this patch replaces an allocation for
Span+Context with just a Context allocation, which is a win because
Spans are big and Contexts are small.

BenchmarkTracing (which runs SQL queries) only show minor improvements
in the time/op, but the memory improvements are so large that I think
they must translate into sufficient GC pressure wins to be worth doing.
Micro-benchmarks from the tracing package show major time/op wins.

```
name                                           old time/op    new time/op    delta
Tracer_StartSpanCtx/opts=none-32                  537ns ± 1%     275ns ± 2%  -48.73%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real-32                  537ns ± 2%     273ns ± 2%  -49.16%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,logtag-32           565ns ± 1%     278ns ± 1%  -50.81%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,autoparent-32       879ns ±29%     278ns ± 5%  -68.36%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,manualparent-32     906ns ±26%     289ns ± 2%  -68.08%  (p=0.008 n=5+5)
Span_GetRecording/root-only-32                   11.1ns ± 2%    11.6ns ± 4%     ~     (p=0.056 n=5+5)
Span_GetRecording/child-only-32                  11.1ns ± 4%    11.7ns ± 2%   +5.44%  (p=0.016 n=5+5)
Span_GetRecording/root-child-32                  18.9ns ± 3%    19.5ns ± 1%   +3.55%  (p=0.008 n=5+5)
RecordingWithStructuredEvent-32                  1.37µs ± 2%    1.17µs ± 2%  -14.22%  (p=0.008 n=5+5)
SpanCreation/detached-child=false-32             1.84µs ± 2%    0.96µs ± 0%  -47.56%  (p=0.008 n=5+5)
SpanCreation/detached-child=true-32              2.01µs ± 1%    1.14µs ± 1%  -43.32%  (p=0.008 n=5+5)

name                                           old alloc/op   new alloc/op   delta
Tracer_StartSpanCtx/opts=none-32                   768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real-32                   768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,logtag-32            768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,autoparent-32        768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,manualparent-32      768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Span_GetRecording/root-only-32                    0.00B          0.00B          ~     (all equal)
Span_GetRecording/child-only-32                   0.00B          0.00B          ~     (all equal)
Span_GetRecording/root-child-32                   0.00B          0.00B          ~     (all equal)
RecordingWithStructuredEvent-32                  1.54kB ± 0%    0.77kB ± 0%  -49.86%  (p=0.008 n=5+5)
SpanCreation/detached-child=false-32             4.62kB ± 0%    0.29kB ± 0%     ~     (p=0.079 n=4+5)
SpanCreation/detached-child=true-32              5.09kB ± 0%    0.77kB ± 0%  -84.87%  (p=0.008 n=5+5)
```

This patch brings us very close to enabling the
TracingModeActiveSpansRegistry tracing mode by default in production -
which would give us a registry of all in-flight spans/operations in the
system.

 ### Interactions with use-after-Finish detection

Span reuse interacts with the recently-introduced span-use-after-Finish
detection. Spans are made available for reuse on Finish (technically,
when certain references to the span have been drained; see below). When
a span is reused in between Finish() and an erroneous use of the
Finish()ed span, this bug cannot be detected and results in the caller
operating on an unintended span. This can result in the wrong log
message apearing in the wrong span, and such. Care has been taken so
that use-after-Finish bugs do not result in more structural problems,
such as loops in the parent-child relationships.

 ### Technical details

The mechanism used for making spans available for reuse is reference
counting; the release of a span to the pool is deferred to the release
of the last counted reference.
Counted references are held:
- internally: children hold references to the parent and the parent holds
  references to the children.
- externally: the WithParent(sp) option takes a reference on sp.

Apart from WithParent, clients using Spans do not track their references
because it'd be too burdensome to require all the references to have a
clearly defined life cycle, and to be explicitly released when they're
no longer in use. For clients, the contract is that a span can be used
until Finish(). WithParent is special, though; see below.

Different alternatives to reference counting were explored. In
particular, instead of a deferred-release scheme, an alternative was a
fat-pointer scheme where references that can outlive a span are tagged
with the span's "generation". That works for the internal use cases, but
the problem with this scheme is that WithParent(s) ends up allocating -
which I want to avoid. Right now, WithParent(s) returns a pointer as an
interface, which doesn't allocate.  But if the pointer gets fat, it no
longer fits into the class of things that can be put in interfaces
without allocating.

The reference counter is an atomic; it is not protected by the span's
lock because a parent's counter needs to be accessed under both the
parent's lock and the children's locks.

In details, the reference counter serves a couple of purposes:
1) Prevent re-allocation of a Span while child spans are still operating on
it. In particular, this ensures that races between Finish()ing a parent and
a child cannot result in the child operating on a re-allocated parent.
Because of the span's lock ordering convention, a child cannot hold its
lock while operating on the parent. During Finish(), the child drops its
lock and informs the parent that it is Finish()ing. If the parent
Finish()es at the same time, that call could erroneously conclude that the
parent can be made available for re-use, even through the child goroutine
has a pending call into the parent.

2) Prevent re-allocation of child spans while a Finish()ing parent is in
the process of transforming the children into roots and inserting them into
the active spans registry. Operating on the registry is done without
holding any span's lock, so a race with a child's Finish() could result in
the registry operating on a re-allocated span.

3) Prevent re-allocation of a Span in between the time that WithParent(s)
captures a reference to s and the time when the parent option is used to
create the child. Such an inopportune reuse of a span could only happen is
the span is Finish()ed concurrently with the creation of its child, which
is illegal. Still, we optionally tolerate use-after-Finishes, and this use
cannot be tolerated with the reference count protection. Without this
protection, the tree of spans in a trace could degenerate into a graph
through the introduction of loops. A loop could lead to deadlock due to the
fact that we lock multiple spans at once. The lock ordering convention is
that the parent needs to be locked before the child, which ensures
deadlock-freedom in the absence of loops.
For example:
1. parent := tr.StartSpan()
2. parentOpt := WithParent(parent)
3. parent.Finish()
4. child := tr.StartSpan(parentOpt)
If "parent" would be re-allocated as "child", then child would have itself
as a parent. The use of parentOpt in step 4) after parent was finished in
step 3) is a use-after-Finish of parent; it is illegal and, if detection is
enabled, it might be detected as such. However, if span pooling and re-use
is enabled, then the detection is not realiable (it does not catch cases
where a span is re-used before a reference to it taken before the prior
Finish() is used).
A span having itself as a parent is just the trivial case of the problem;
loops of arbitrary length are also possible. For example, for a loop of
length 2:
1. Say we have span A as a parent with span B as a child (A -> B).
2. parentA := WithParent(A)
3. parentB := WithParent(B)
4. A.Finish(); B.Finish();
5. X := tr.StartSpan(parentA); Y := tr.StartSpan(parentB);
If B is re-used as X, and A is re-used as Y, we get the following graph:
```
 B<-┐
 |  |
 └->A
```

We avoid these hazards by having WithParent(s) increment s' reference
count, so spans are not re-used while the creation of a child is pending.
Spans can be Finish()ed while the creation of the child is pending, in
which case the creation of the child will reliably detect the
use-after-Finish (and turn it into a no-op if configured to tolerate
such illegal uses).

Introducing this reference count, and only reusing spans with a
reference count of zero, introduced the risk of leaking references if
one does opt = WithParent(sp) and then discards the resulting opt
without passing it to StartSpan(). This would cause a silent performance
regression (not a memory leak though, as the GC is still there). This
risk seems worth it for avoiding deadlocks in case of other buggy usage.

Release note: None

74823: sql: add create_session_revival_token builtin r=catj-cockroach,knz,otan a=rafiss

refs https://github.com/cockroachdb/cockroach/issues/74643

This builtin function will be used by sqlproxy in order to migrate
sessions from one sql node to another. The token will be used to
authenticate as the current user without using a password.

The builtin is only usable by tenants.

No release note since this is only meant to be used internally.

Release note: None

Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>
Co-authored-by: Rafi Shamim <rafi@cockroachlabs.com>

---
## [mohammad-akhlaghi/maneage-fork](https://github.com/mohammad-akhlaghi/maneage-fork)@[8463df97c6...](https://github.com/mohammad-akhlaghi/maneage-fork/commit/8463df97c6f26ec4d22cd5828bb0574fd5e450d2)
#### Friday 2022-01-21 00:16:46 by Mohammad Akhlaghi

IMPORTANT: Updates to almost all software

This commit primarily affects the configuration step of Maneage'd projects,
and in particular, updated versions of the many of the software (see
P.S.). So it shouldn't affect your high-level analysis other than the
version bumps of the software you use (and the software's possibly
improve/changed behavior).

The following software (and thus their dependencies) couldn't be updated as
described below:
  - Cryptography: isn't building because it depends on a new
    setuptools-rust package that has problems
    (https://savannah.nongnu.org/bugs/index.php?61731), so it has been
    commented in 'versions.conf'.
  - SecretStorage: because it depends on Cryptography.
  - Keyring: because it depends on SecretStorage.
  - Astroquery: because it depends on Keyring.

This is a "squashed" commit after rebasing a development branch of 60
commits corresponding to a roughly two-month time interval. The following
people contributed to this branch.
  - Boudewijn Roukema added all the R software infrastructure and the R
    packages, as well as greatly helping in fixing many bugs during the
    update.
  - Raul Infante-Sainz helped in testing and debugging the build.
  - Pedram Ashofteh Ardakani found and fixed a bug.
  - Zahra Sharbaf helped in testing and found several bugs.

Below a description of the most noteworthy points is given.

  - Software tarballs: all updated software now have a unified format
    tarball (ustar; if not possible, pax) and unified compression (Lzip) in
    Maneage's software repository in Zenodo
    (https://doi.org/10.5281/zenodo.3883409). For more on this See
    https://savannah.nongnu.org/task/?15699 . This won't affect any extra
    software you would like to add; you can use any format recognized by
    GNU Tar, and all common compression algorithms. This new requirement is
    only for software that get merged to the core Maneage branch.

  - Metastore (and thus libbsd and libmd) moved to highlevel: Metastore
    (and the packages it depends on) is a high-level product that is only
    relevant during the project development (like Emacs!): when the user
    wants the file meta data (like dates) to be unchanged after checking
    out branches. So it should be considered a high-level software, not
    basic. Metastore also usually causes many more headaches and error
    messages, so personally, I have stopped using it! Instead I simply
    merge my branches in a separate clone, then pull the merge commit: in
    this way, the files of my project aren't re-written during the checkout
    phase and therefore their dates are untouched (which can conflict with
    Make's dates on configuration files).

  - The un-official cloned version of Flex (2.6.4-91 until this commit) was
    causing problems in the building of Netpbm, so with this commit, it has
    been moved back to version 2.6.4.

  - Netpbm's official page had version 10.73.38 as the latest stable
    tarball that was just released in late 2021. But I couldn't find our
    previously-used version 10.86.99 anywhere (to see when it was released
    and why we used it! Its at last more than one year old!). So the
    official stable version is being used now.

  - Improved instructions in 'README.md' for building software environment
    in a Docker container (while having project source and output data
    products on the local system; including the usage of the host's
    '/dev/shm' to speed up temporary operations).

  - Until now, the convention in Maneage was to put eight SPACE characters
    before the comment lines within recipes. This was done because by
    default GNU Emacs (also many other editors) show a TAB as eight
    characters. However, in other text editors, online browsers, or even
    the Git diff, a TAB can correspond to a different number of
    characters. In such cases, the Maneage recipes wouldn't look too
    interesting (the comments and the recipe commands would show a
    different indentation!).

    With this commit, all the comment lines in the Makefiles within the
    core Maneage branch have a hash ('#') as their first character and a
    TAB as the second. This allows the comment lines in recipes to have the
    same indentation as code; making the code much more easier to read in a
    general scenario including a 'git diff' (editor agnostic!).

P.S. List of updated software with their old and new versions
 - Software with no version update are not mentioned.
 - The old version of newly added software are shown with '--'.

Name (Basic)              Old version    New version
------------              -----------    -----------
Bzip2                     1.0.6          1.0.8
CURL                      7.71.1         7.79.1
Dash                      0.5.10.2       0.5.11.5
File                      5.39           5.41
Flock                     0.2.3          0.4.0
GNU Bash                  5.0.18         5.1.8
GNU Binutils              2.35           2.37
GNU Coreutils             8.32           9.0
GNU GCC                   10.2.0         11.2.0
GNU M4                    1.4.18         1.4.19
GNU Readline              8.0            8.1.1
GNU Tar                   1.32           1.34
GNU Texinfo               6.7            6.8
GNU diffutils             3.7            3.8
GNU findutils             4.7.0          4.8.0
GNU gmp                   6.2.0          6.2.1
GNU grep                  3.4            3.7
GNU gzip                  1.10           1.11
GNU libunistring          0.9.10         1.0
GNU mpc                   1.1.0          1.2.1
GNU mpfr                  4.0.2          4.1.0
GNU nano                  5.2            6.0
GNU ncurses               6.2            6.3
GNU wget                  1.20.3         1.21.2
Git                       2.28.0         2.34.0
Less                      563            590
Libxml2                   2.9.9          2.9.12
Lzip                      1.22-rc2       1.22
OpenSLL                   1.1.1a         3.0.0
Patchelf                  0.10           0.13
Perl                      5.32.0         5.34.0
Podlators                 --             4.14

Name (Highlevel)          Old version    New version
----------------          -----------    -----------
Apachelog4cxx             0.10.0-603     0.12.1
Astrometry.net            0.80           0.85
Boost                     1.73.0         1.77.0
CFITSIO                   3.48           4.0.0
Cmake                     3.18.1         3.21.4
Eigen                     3.3.7          3.4.0
Expat                     2.2.9          2.4.1
FFTW                      3.3.8          3.3.10
Flex                      2.6.4-91       2.6.4
Fontconfig                2.13.1         2.13.94
Freetype                  2.10.2         2.11.0
GNU Astronomy Utilities   0.12           0.16.1-e0f1
GNU Autoconf              2.69.200-babc  2.71
GNU Automake              1.16.2         1.16.5
GNU Bison                 3.7            3.8.2
GNU Emacs                 27.1           27.2
GNU GDB                   9.2            11.1
GNU GSL                   2.6            2.7
GNU Help2man              1.47.11        1.48.5
Ghostscript               9.52           9.55.0
ICU                       --             70.1
ImageMagick               7.0.8-67       7.1.0-13
Libbsd                    0.10.0         0.11.3
Libffi                    3.2.1          3.4.2
Libgit2                   1.0.1          1.3.0
Libidn                    1.36           1.38
Libjpeg                   9b             9d
Libmd                     --             1.0.4
Libtiff                   4.0.10         4.3.0
Libx11                    1.6.9          1.7.2
Libxt                     1.2.0          1.2.1
Netpbm                    10.86.99       10.73.38
OpenBLAS                  0.3.10         0.3.18
OpenMPI                   4.0.4          4.1.1
Pixman                    0.38.0         0.40.0
Python                    3.8.5          3.10.0
R                         4.0.2          4.1.2
SWIG                      3.0.12         4.0.2
Util-linux                2.35           2.37.2
Util-macros               1.19.2         1.19.3
Valgrind                  3.15.0         3.18.1
WCSLIB                    7.3            7.7
Xcb-proto                 1.14           1.14.1
Xorgproto                 2020.1         2021.5

Name (Python)             Old version    New version
-------------             -----------    -----------
Astropy                   4.0            5.0
Beautifulsoup4            4.7.1          4.10.0
Beniget                   --             0.4.1
Cffi                      1.12.2         1.15.0
Cryptography              2.6.1          36.0.1
Cycler                    0.10.0         0.11.0+}
Cython                    0.29.21        0.29.24
Esutil                    0.6.4          0.6.9
Extension-helpers         --             0.1
Galsim                    2.2.1          2.3.3
Gast                      --             0.5.3
Jinja2                    --             3.0.3
MPI4py                    3.0.3          3.1.3
Markupsafe                --             2.0.1
Numpy                     1.19.1         1.21.3
Packaging                 --             21.3
Pillow                    --             8.4.0
Ply                       --             3.11
Pyerfa                    --             2.0.0.1
Pyparsing                 2.3.1          3.0.4
Pythran                   --             0.11.0
Scipy                     1.5.2          1.7.3
Setuptools                41.6.0         58.3.0
Six                       1.12.0         1.16.0
Uncertainties             3.1.2          3.1.6
Wheel                     --             0.37.0

Name (R)                  Old version    New version
--------                  -----------    -----------
Cli                       --             2.5.0
Colorspace                --             2.0-1
Cowplot                   --             1.1.1
Crayon                    --             1.4.1
Digest                    --             0.6.27
Ellipsis                  --             0.3.2
Fansi                     --             0.5.0
Farver                    --             2.1.0
Ggplot2                   --             3.3.4
Glue                      --             1.4.2
GridExtra                 --             2.3
Gtable                    --             0.3.0
Isoband                   --             0.2.4
Labeling                  --             0.4.2
Lifecycle                 --             1.0.0
Magrittr                  --             2.0.1
MASS                      --             7.3-54
Mgcv                      --             1.8-36
Munsell                   --             0.5.0
Pillar                    --             1.6.1
R-Pkgconfig               --             2.0.3
R6                        --             2.5.0
RColorBrewer              --             1.1-2
Rlang                     --             0.4.11
Scales                    --             1.1.1
Tibble                    --             3.1.2
Utf8                      --             1.2.1
Vctrs                     --             0.3.8
ViridisLite               --             0.4.0
Withr                     --             2.4.2

---
## [Bungalow-13/Bungalow-13](https://github.com/Bungalow-13/Bungalow-13)@[5b4a42d3bd...](https://github.com/Bungalow-13/Bungalow-13/commit/5b4a42d3bd9cdac8697d1718c2b55d2cec8686cc)
#### Friday 2022-01-21 00:28:09 by DaddyIssues98

a (#470)

What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.
I am trained in guerilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words.

You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands.

Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue.

Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue.

But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it.

You’re fucking dead, kiddo.

---
## [physicalrobot/brainstorm](https://github.com/physicalrobot/brainstorm)@[bb67f0a829...](https://github.com/physicalrobot/brainstorm/commit/bb67f0a8295d523659b43a1f067c96df74039383)
#### Friday 2022-01-21 00:49:43 by Vikalp Malhotra

holy shit finally, the css for the buttons is where I want it and the music works

---
## [uvhw/bitcoin](https://github.com/uvhw/bitcoin)@[9354f60be6...](https://github.com/uvhw/bitcoin/commit/9354f60be62cf54c67c5cfe768749f520f84aeeb)
#### Friday 2022-01-21 01:15:52 by uvhw

Create main.yml

/*
    rfc1751.js : Converts between 128-bit strings and a human-readable
    sequence of words, as defined in RFC1751: "A Convention for
    Human-Readable 128-bit Keys", by Daniel L. McDonald.
    Ported from rfc1751.py / Python Cryptography Toolkit (public domain).
*/

var rfc1751_wordlist = [ "A", "ABE", "ACE", "ACT", "AD", "ADA", "ADD",
   "AGO", "AID", "AIM", "AIR", "ALL", "ALP", "AM", "AMY", "AN", "ANA",
   "AND", "ANN", "ANT", "ANY", "APE", "APS", "APT", "ARC", "ARE", "ARK",
   "ARM", "ART", "AS", "ASH", "ASK", "AT", "ATE", "AUG", "AUK", "AVE",
   "AWE", "AWK", "AWL", "AWN", "AX", "AYE", "BAD", "BAG", "BAH", "BAM",
   "BAN", "BAR", "BAT", "BAY", "BE", "BED", "BEE", "BEG", "BEN", "BET",
   "BEY", "BIB", "BID", "BIG", "BIN", "BIT", "BOB", "BOG", "BON", "BOO",
   "BOP", "BOW", "BOY", "BUB", "BUD", "BUG", "BUM", "BUN", "BUS", "BUT",
   "BUY", "BY", "BYE", "CAB", "CAL", "CAM", "CAN", "CAP", "CAR", "CAT",
   "CAW", "COD", "COG", "COL", "CON", "COO", "COP", "COT", "COW", "COY",
   "CRY", "CUB", "CUE", "CUP", "CUR", "CUT", "DAB", "DAD", "DAM", "DAN",
   "DAR", "DAY", "DEE", "DEL", "DEN", "DES", "DEW", "DID", "DIE", "DIG",
   "DIN", "DIP", "DO", "DOE", "DOG", "DON", "DOT", "DOW", "DRY", "DUB",
   "DUD", "DUE", "DUG", "DUN", "EAR", "EAT", "ED", "EEL", "EGG", "EGO",
   "ELI", "ELK", "ELM", "ELY", "EM", "END", "EST", "ETC", "EVA", "EVE",
   "EWE", "EYE", "FAD", "FAN", "FAR", "FAT", "FAY", "FED", "FEE", "FEW",
   "FIB", "FIG", "FIN", "FIR", "FIT", "FLO", "FLY", "FOE", "FOG", "FOR",
   "FRY", "FUM", "FUN", "FUR", "GAB", "GAD", "GAG", "GAL", "GAM", "GAP",
   "GAS", "GAY", "GEE", "GEL", "GEM", "GET", "GIG", "GIL", "GIN", "GO",
   "GOT", "GUM", "GUN", "GUS", "GUT", "GUY", "GYM", "GYP", "HA", "HAD",
   "HAL", "HAM", "HAN", "HAP", "HAS", "HAT", "HAW", "HAY", "HE", "HEM",
   "HEN", "HER", "HEW", "HEY", "HI", "HID", "HIM", "HIP", "HIS", "HIT",
   "HO", "HOB", "HOC", "HOE", "HOG", "HOP", "HOT", "HOW", "HUB", "HUE",
   "HUG", "HUH", "HUM", "HUT", "I", "ICY", "IDA", "IF", "IKE", "ILL",
   "INK", "INN", "IO", "ION", "IQ", "IRA", "IRE", "IRK", "IS", "IT",
   "ITS", "IVY", "JAB", "JAG", "JAM", "JAN", "JAR", "JAW", "JAY", "JET",
   "JIG", "JIM", "JO", "JOB", "JOE", "JOG", "JOT", "JOY", "JUG", "JUT",
   "KAY", "KEG", "KEN", "KEY", "KID", "KIM", "KIN", "KIT", "LA", "LAB",
   "LAC", "LAD", "LAG", "LAM", "LAP", "LAW", "LAY", "LEA", "LED", "LEE",
   "LEG", "LEN", "LEO", "LET", "LEW", "LID", "LIE", "LIN", "LIP", "LIT",
   "LO", "LOB", "LOG", "LOP", "LOS", "LOT", "LOU", "LOW", "LOY", "LUG",
   "LYE", "MA", "MAC", "MAD", "MAE", "MAN", "MAO", "MAP", "MAT", "MAW",
   "MAY", "ME", "MEG", "MEL", "MEN", "MET", "MEW", "MID", "MIN", "MIT",
   "MOB", "MOD", "MOE", "MOO", "MOP", "MOS", "MOT", "MOW", "MUD", "MUG",
   "MUM", "MY", "NAB", "NAG", "NAN", "NAP", "NAT", "NAY", "NE", "NED",
   "NEE", "NET", "NEW", "NIB", "NIL", "NIP", "NIT", "NO", "NOB", "NOD",
   "NON", "NOR", "NOT", "NOV", "NOW", "NU", "NUN", "NUT", "O", "OAF",
   "OAK", "OAR", "OAT", "ODD", "ODE", "OF", "OFF", "OFT", "OH", "OIL",
   "OK", "OLD", "ON", "ONE", "OR", "ORB", "ORE", "ORR", "OS", "OTT",
   "OUR", "OUT", "OVA", "OW", "OWE", "OWL", "OWN", "OX", "PA", "PAD",
   "PAL", "PAM", "PAN", "PAP", "PAR", "PAT", "PAW", "PAY", "PEA", "PEG",
   "PEN", "PEP", "PER", "PET", "PEW", "PHI", "PI", "PIE", "PIN", "PIT",
   "PLY", "PO", "POD", "POE", "POP", "POT", "POW", "PRO", "PRY", "PUB",
   "PUG", "PUN", "PUP", "PUT", "QUO", "RAG", "RAM", "RAN", "RAP", "RAT",
   "RAW", "RAY", "REB", "RED", "REP", "RET", "RIB", "RID", "RIG", "RIM",
   "RIO", "RIP", "ROB", "ROD", "ROE", "RON", "ROT", "ROW", "ROY", "RUB",
   "RUE", "RUG", "RUM", "RUN", "RYE", "SAC", "SAD", "SAG", "SAL", "SAM",
   "SAN", "SAP", "SAT", "SAW", "SAY", "SEA", "SEC", "SEE", "SEN", "SET",
   "SEW", "SHE", "SHY", "SIN", "SIP", "SIR", "SIS", "SIT", "SKI", "SKY",
   "SLY", "SO", "SOB", "SOD", "SON", "SOP", "SOW", "SOY", "SPA", "SPY",
   "SUB", "SUD", "SUE", "SUM", "SUN", "SUP", "TAB", "TAD", "TAG", "TAN",
   "TAP", "TAR", "TEA", "TED", "TEE", "TEN", "THE", "THY", "TIC", "TIE",
   "TIM", "TIN", "TIP", "TO", "TOE", "TOG", "TOM", "TON", "TOO", "TOP",
   "TOW", "TOY", "TRY", "TUB", "TUG", "TUM", "TUN", "TWO", "UN", "UP",
   "US", "USE", "VAN", "VAT", "VET", "VIE", "WAD", "WAG", "WAR", "WAS",
   "WAY", "WE", "WEB", "WED", "WEE", "WET", "WHO", "WHY", "WIN", "WIT",
   "WOK", "WON", "WOO", "WOW", "WRY", "WU", "YAM", "YAP", "YAW", "YE",
   "YEA", "YES", "YET", "YOU", "ABED", "ABEL", "ABET", "ABLE", "ABUT",
   "ACHE", "ACID", "ACME", "ACRE", "ACTA", "ACTS", "ADAM", "ADDS",
   "ADEN", "AFAR", "AFRO", "AGEE", "AHEM", "AHOY", "AIDA", "AIDE",
   "AIDS", "AIRY", "AJAR", "AKIN", "ALAN", "ALEC", "ALGA", "ALIA",
   "ALLY", "ALMA", "ALOE", "ALSO", "ALTO", "ALUM", "ALVA", "AMEN",
   "AMES", "AMID", "AMMO", "AMOK", "AMOS", "AMRA", "ANDY", "ANEW",
   "ANNA", "ANNE", "ANTE", "ANTI", "AQUA", "ARAB", "ARCH", "AREA",
   "ARGO", "ARID", "ARMY", "ARTS", "ARTY", "ASIA", "ASKS", "ATOM",
   "AUNT", "AURA", "AUTO", "AVER", "AVID", "AVIS", "AVON", "AVOW",
   "AWAY", "AWRY", "BABE", "BABY", "BACH", "BACK", "BADE", "BAIL",
   "BAIT", "BAKE", "BALD", "BALE", "BALI", "BALK", "BALL", "BALM",
   "BAND", "BANE", "BANG", "BANK", "BARB", "BARD", "BARE", "BARK",
   "BARN", "BARR", "BASE", "BASH", "BASK", "BASS", "BATE", "BATH",
   "BAWD", "BAWL", "BEAD", "BEAK", "BEAM", "BEAN", "BEAR", "BEAT",
   "BEAU", "BECK", "BEEF", "BEEN", "BEER",
   "BEET", "BELA", "BELL", "BELT", "BEND", "BENT", "BERG", "BERN",
   "BERT", "BESS", "BEST", "BETA", "BETH", "BHOY", "BIAS", "BIDE",
   "BIEN", "BILE", "BILK", "BILL", "BIND", "BING", "BIRD", "BITE",
   "BITS", "BLAB", "BLAT", "BLED", "BLEW", "BLOB", "BLOC", "BLOT",
   "BLOW", "BLUE", "BLUM", "BLUR", "BOAR", "BOAT", "BOCA", "BOCK",
   "BODE", "BODY", "BOGY", "BOHR", "BOIL", "BOLD", "BOLO", "BOLT",
   "BOMB", "BONA", "BOND", "BONE", "BONG", "BONN", "BONY", "BOOK",
   "BOOM", "BOON", "BOOT", "BORE", "BORG", "BORN", "BOSE", "BOSS",
   "BOTH", "BOUT", "BOWL", "BOYD", "BRAD", "BRAE", "BRAG", "BRAN",
   "BRAY", "BRED", "BREW", "BRIG", "BRIM", "BROW", "BUCK", "BUDD",
   "BUFF", "BULB", "BULK", "BULL", "BUNK", "BUNT", "BUOY", "BURG",
   "BURL", "BURN", "BURR", "BURT", "BURY", "BUSH", "BUSS", "BUST",
   "BUSY", "BYTE", "CADY", "CAFE", "CAGE", "CAIN", "CAKE", "CALF",
   "CALL", "CALM", "CAME", "CANE", "CANT", "CARD", "CARE", "CARL",
   "CARR", "CART", "CASE", "CASH", "CASK", "CAST", "CAVE", "CEIL",
   "CELL", "CENT", "CERN", "CHAD", "CHAR", "CHAT", "CHAW", "CHEF",
   "CHEN", "CHEW", "CHIC", "CHIN", "CHOU", "CHOW", "CHUB", "CHUG",
   "CHUM", "CITE", "CITY", "CLAD", "CLAM", "CLAN", "CLAW", "CLAY",
   "CLOD", "CLOG", "CLOT", "CLUB", "CLUE", "COAL", "COAT", "COCA",
   "COCK", "COCO", "CODA", "CODE", "CODY", "COED", "COIL", "COIN",
   "COKE", "COLA", "COLD", "COLT", "COMA", "COMB", "COME", "COOK",
   "COOL", "COON", "COOT", "CORD", "CORE", "CORK", "CORN", "COST",
   "COVE", "COWL", "CRAB", "CRAG", "CRAM", "CRAY", "CREW", "CRIB",
   "CROW", "CRUD", "CUBA", "CUBE", "CUFF", "CULL", "CULT", "CUNY",
   "CURB", "CURD", "CURE", "CURL", "CURT", "CUTS", "DADE", "DALE",
   "DAME", "DANA", "DANE", "DANG", "DANK", "DARE", "DARK", "DARN",
   "DART", "DASH", "DATA", "DATE", "DAVE", "DAVY", "DAWN", "DAYS",
   "DEAD", "DEAF", "DEAL", "DEAN", "DEAR", "DEBT", "DECK", "DEED",
   "DEEM", "DEER", "DEFT", "DEFY", "DELL", "DENT", "DENY", "DESK",
   "DIAL", "DICE", "DIED", "DIET", "DIME", "DINE", "DING", "DINT",
   "DIRE", "DIRT", "DISC", "DISH", "DISK", "DIVE", "DOCK", "DOES",
   "DOLE", "DOLL", "DOLT", "DOME", "DONE", "DOOM", "DOOR", "DORA",
   "DOSE", "DOTE", "DOUG", "DOUR", "DOVE", "DOWN", "DRAB", "DRAG",
   "DRAM", "DRAW", "DREW", "DRUB", "DRUG", "DRUM", "DUAL", "DUCK",
   "DUCT", "DUEL", "DUET", "DUKE", "DULL", "DUMB", "DUNE", "DUNK",
   "DUSK", "DUST", "DUTY", "EACH", "EARL", "EARN", "EASE", "EAST",
   "EASY", "EBEN", "ECHO", "EDDY", "EDEN", "EDGE", "EDGY", "EDIT",
   "EDNA", "EGAN", "ELAN", "ELBA", "ELLA", "ELSE", "EMIL", "EMIT",
   "EMMA", "ENDS", "ERIC", "EROS", "EVEN", "EVER", "EVIL", "EYED",
   "FACE", "FACT", "FADE", "FAIL", "FAIN", "FAIR", "FAKE", "FALL",
   "FAME", "FANG", "FARM", "FAST", "FATE", "FAWN", "FEAR", "FEAT",
   "FEED", "FEEL", "FEET", "FELL", "FELT", "FEND", "FERN", "FEST",
   "FEUD", "FIEF", "FIGS", "FILE", "FILL", "FILM", "FIND", "FINE",
   "FINK", "FIRE", "FIRM", "FISH", "FISK", "FIST", "FITS", "FIVE",
   "FLAG", "FLAK", "FLAM", "FLAT", "FLAW", "FLEA", "FLED", "FLEW",
   "FLIT", "FLOC", "FLOG", "FLOW", "FLUB", "FLUE", "FOAL", "FOAM",
   "FOGY", "FOIL", "FOLD", "FOLK", "FOND", "FONT", "FOOD", "FOOL",
   "FOOT", "FORD", "FORE", "FORK", "FORM", "FORT", "FOSS", "FOUL",
   "FOUR", "FOWL", "FRAU", "FRAY", "FRED", "FREE", "FRET", "FREY",
   "FROG", "FROM", "FUEL", "FULL", "FUME", "FUND", "FUNK", "FURY",
   "FUSE", "FUSS", "GAFF", "GAGE", "GAIL", "GAIN", "GAIT", "GALA",
   "GALE", "GALL", "GALT", "GAME", "GANG", "GARB", "GARY", "GASH",
   "GATE", "GAUL", "GAUR", "GAVE", "GAWK", "GEAR", "GELD", "GENE",
   "GENT", "GERM", "GETS", "GIBE", "GIFT", "GILD", "GILL", "GILT",
   "GINA", "GIRD", "GIRL", "GIST", "GIVE", "GLAD", "GLEE", "GLEN",
   "GLIB", "GLOB", "GLOM", "GLOW", "GLUE", "GLUM", "GLUT", "GOAD",
   "GOAL", "GOAT", "GOER", "GOES", "GOLD", "GOLF", "GONE", "GONG",
   "GOOD", "GOOF", "GORE", "GORY", "GOSH", "GOUT", "GOWN", "GRAB",
   "GRAD", "GRAY", "GREG", "GREW", "GREY", "GRID", "GRIM", "GRIN",
   "GRIT", "GROW", "GRUB", "GULF", "GULL", "GUNK", "GURU", "GUSH",
   "GUST", "GWEN", "GWYN", "HAAG", "HAAS", "HACK", "HAIL", "HAIR",
   "HALE", "HALF", "HALL", "HALO", "HALT", "HAND", "HANG", "HANK",
   "HANS", "HARD", "HARK", "HARM", "HART", "HASH", "HAST", "HATE",
   "HATH", "HAUL", "HAVE", "HAWK", "HAYS", "HEAD", "HEAL", "HEAR",
   "HEAT", "HEBE", "HECK", "HEED", "HEEL", "HEFT", "HELD", "HELL",
   "HELM", "HERB", "HERD", "HERE", "HERO", "HERS", "HESS", "HEWN",
   "HICK", "HIDE", "HIGH", "HIKE", "HILL", "HILT", "HIND", "HINT",
   "HIRE", "HISS", "HIVE", "HOBO", "HOCK", "HOFF", "HOLD", "HOLE",
   "HOLM", "HOLT", "HOME", "HONE", "HONK", "HOOD", "HOOF", "HOOK",
   "HOOT", "HORN", "HOSE", "HOST", "HOUR", "HOVE", "HOWE", "HOWL",
   "HOYT", "HUCK", "HUED", "HUFF", "HUGE", "HUGH", "HUGO", "HULK",
   "HULL", "HUNK", "HUNT", "HURD", "HURL", "HURT", "HUSH", "HYDE",
   "HYMN", "IBIS", "ICON", "IDEA", "IDLE", "IFFY", "INCA", "INCH",
   "INTO", "IONS", "IOTA", "IOWA", "IRIS", "IRMA", "IRON", "ISLE",
   "ITCH", "ITEM", "IVAN", "JACK", "JADE", "JAIL", "JAKE", "JANE",
   "JAVA", "JEAN", "JEFF", "JERK", "JESS", "JEST", "JIBE", "JILL",
   "JILT", "JIVE", "JOAN", "JOBS", "JOCK", "JOEL", "JOEY", "JOHN",
   "JOIN", "JOKE", "JOLT", "JOVE", "JUDD", "JUDE", "JUDO", "JUDY",
   "JUJU", "JUKE", "JULY", "JUNE", "JUNK", "JUNO", "JURY", "JUST",
   "JUTE", "KAHN", "KALE", "KANE", "KANT", "KARL", "KATE", "KEEL",
   "KEEN", "KENO", "KENT", "KERN", "KERR", "KEYS", "KICK", "KILL",
   "KIND", "KING", "KIRK", "KISS", "KITE", "KLAN", "KNEE", "KNEW",
   "KNIT", "KNOB", "KNOT", "KNOW", "KOCH", "KONG", "KUDO", "KURD",
   "KURT", "KYLE", "LACE", "LACK", "LACY", "LADY", "LAID", "LAIN",
   "LAIR", "LAKE", "LAMB", "LAME", "LAND", "LANE", "LANG", "LARD",
   "LARK", "LASS", "LAST", "LATE", "LAUD", "LAVA", "LAWN", "LAWS",
   "LAYS", "LEAD", "LEAF", "LEAK", "LEAN", "LEAR", "LEEK", "LEER",
   "LEFT", "LEND", "LENS", "LENT", "LEON", "LESK", "LESS", "LEST",
   "LETS", "LIAR", "LICE", "LICK", "LIED", "LIEN", "LIES", "LIEU",
   "LIFE", "LIFT", "LIKE", "LILA", "LILT", "LILY", "LIMA", "LIMB",
   "LIME", "LIND", "LINE", "LINK", "LINT", "LION", "LISA", "LIST",
   "LIVE", "LOAD", "LOAF", "LOAM", "LOAN", "LOCK", "LOFT", "LOGE",
   "LOIS", "LOLA", "LONE", "LONG", "LOOK", "LOON", "LOOT", "LORD",
   "LORE", "LOSE", "LOSS", "LOST", "LOUD", "LOVE", "LOWE", "LUCK",
   "LUCY", "LUGE", "LUKE", "LULU", "LUND", "LUNG", "LURA", "LURE",
   "LURK", "LUSH", "LUST", "LYLE", "LYNN", "LYON", "LYRA", "MACE",
   "MADE", "MAGI", "MAID", "MAIL", "MAIN", "MAKE", "MALE", "MALI",
   "MALL", "MALT", "MANA", "MANN", "MANY", "MARC", "MARE", "MARK",
   "MARS", "MART", "MARY", "MASH", "MASK", "MASS", "MAST", "MATE",
   "MATH", "MAUL", "MAYO", "MEAD", "MEAL", "MEAN", "MEAT", "MEEK",
   "MEET", "MELD", "MELT", "MEMO", "MEND", "MENU", "MERT", "MESH",
   "MESS", "MICE", "MIKE", "MILD", "MILE", "MILK", "MILL", "MILT",
   "MIMI", "MIND", "MINE", "MINI", "MINK", "MINT", "MIRE", "MISS",
   "MIST", "MITE", "MITT", "MOAN", "MOAT", "MOCK", "MODE", "MOLD",
   "MOLE", "MOLL", "MOLT", "MONA", "MONK", "MONT", "MOOD", "MOON",
   "MOOR", "MOOT", "MORE", "MORN", "MORT", "MOSS", "MOST", "MOTH",
   "MOVE", "MUCH", "MUCK", "MUDD", "MUFF", "MULE", "MULL", "MURK",
   "MUSH", "MUST", "MUTE", "MUTT", "MYRA", "MYTH", "NAGY", "NAIL",
   "NAIR", "NAME", "NARY", "NASH", "NAVE", "NAVY", "NEAL", "NEAR",
   "NEAT", "NECK", "NEED", "NEIL", "NELL", "NEON", "NERO", "NESS",
   "NEST", "NEWS", "NEWT", "NIBS", "NICE", "NICK", "NILE", "NINA",
   "NINE", "NOAH", "NODE", "NOEL", "NOLL", "NONE", "NOOK", "NOON",
   "NORM", "NOSE", "NOTE", "NOUN", "NOVA", "NUDE", "NULL", "NUMB",
   "OATH", "OBEY", "OBOE", "ODIN", "OHIO", "OILY", "OINT", "OKAY",
   "OLAF", "OLDY", "OLGA", "OLIN", "OMAN", "OMEN", "OMIT", "ONCE",
   "ONES", "ONLY", "ONTO", "ONUS", "ORAL", "ORGY", "OSLO", "OTIS",
   "OTTO", "OUCH", "OUST", "OUTS", "OVAL", "OVEN", "OVER", "OWLY",
   "OWNS", "QUAD", "QUIT", "QUOD", "RACE", "RACK", "RACY", "RAFT",
   "RAGE", "RAID", "RAIL", "RAIN", "RAKE", "RANK", "RANT", "RARE",
   "RASH", "RATE", "RAVE", "RAYS", "READ", "REAL", "REAM", "REAR",
   "RECK", "REED", "REEF", "REEK", "REEL", "REID", "REIN", "RENA",
   "REND", "RENT", "REST", "RICE", "RICH", "RICK", "RIDE", "RIFT",
   "RILL", "RIME", "RING", "RINK", "RISE", "RISK", "RITE", "ROAD",
   "ROAM", "ROAR", "ROBE", "ROCK", "RODE", "ROIL", "ROLL", "ROME",
   "ROOD", "ROOF", "ROOK", "ROOM", "ROOT", "ROSA", "ROSE", "ROSS",
   "ROSY", "ROTH", "ROUT", "ROVE", "ROWE", "ROWS", "RUBE", "RUBY",
   "RUDE", "RUDY", "RUIN", "RULE", "RUNG", "RUNS", "RUNT", "RUSE",
   "RUSH", "RUSK", "RUSS", "RUST", "RUTH", "SACK", "SAFE", "SAGE",
   "SAID", "SAIL", "SALE", "SALK", "SALT", "SAME", "SAND", "SANE",
   "SANG", "SANK", "SARA", "SAUL", "SAVE", "SAYS", "SCAN", "SCAR",
   "SCAT", "SCOT", "SEAL", "SEAM", "SEAR", "SEAT", "SEED", "SEEK",
   "SEEM", "SEEN", "SEES", "SELF", "SELL", "SEND", "SENT", "SETS",
   "SEWN", "SHAG", "SHAM", "SHAW", "SHAY", "SHED", "SHIM", "SHIN",
   "SHOD", "SHOE", "SHOT", "SHOW", "SHUN", "SHUT", "SICK", "SIDE",
   "SIFT", "SIGH", "SIGN", "SILK", "SILL", "SILO", "SILT", "SINE",
   "SING", "SINK", "SIRE", "SITE", "SITS", "SITU", "SKAT", "SKEW",
   "SKID", "SKIM", "SKIN", "SKIT", "SLAB", "SLAM", "SLAT", "SLAY",
   "SLED", "SLEW", "SLID", "SLIM", "SLIT", "SLOB", "SLOG", "SLOT",
   "SLOW", "SLUG", "SLUM", "SLUR", "SMOG", "SMUG", "SNAG", "SNOB",
   "SNOW", "SNUB", "SNUG", "SOAK", "SOAR", "SOCK", "SODA", "SOFA",
   "SOFT", "SOIL", "SOLD", "SOME", "SONG", "SOON", "SOOT", "SORE",
   "SORT", "SOUL", "SOUR", "SOWN", "STAB", "STAG", "STAN", "STAR",
   "STAY", "STEM", "STEW", "STIR", "STOW", "STUB", "STUN", "SUCH",
   "SUDS", "SUIT", "SULK", "SUMS", "SUNG", "SUNK", "SURE", "SURF",
   "SWAB", "SWAG", "SWAM", "SWAN", "SWAT", "SWAY", "SWIM", "SWUM",
   "TACK", "TACT", "TAIL", "TAKE", "TALE", "TALK", "TALL", "TANK",
   "TASK", "TATE", "TAUT", "TEAL", "TEAM", "TEAR", "TECH", "TEEM",
   "TEEN", "TEET", "TELL", "TEND", "TENT", "TERM", "TERN", "TESS",
   "TEST", "THAN", "THAT", "THEE", "THEM", "THEN", "THEY", "THIN",
   "THIS", "THUD", "THUG", "TICK", "TIDE", "TIDY", "TIED", "TIER",
   "TILE", "TILL", "TILT", "TIME", "TINA", "TINE", "TINT", "TINY",
   "TIRE", "TOAD", "TOGO", "TOIL", "TOLD", "TOLL", "TONE", "TONG",
   "TONY", "TOOK", "TOOL", "TOOT", "TORE", "TORN", "TOTE", "TOUR",
   "TOUT", "TOWN", "TRAG", "TRAM", "TRAY", "TREE", "TREK", "TRIG",
   "TRIM", "TRIO", "TROD", "TROT", "TROY", "TRUE", "TUBA", "TUBE",
   "TUCK", "TUFT", "TUNA", "TUNE", "TUNG", "TURF", "TURN", "TUSK",
   "TWIG", "TWIN", "TWIT", "ULAN", "UNIT", "URGE", "USED", "USER",
   "USES", "UTAH", "VAIL", "VAIN", "VALE", "VARY", "VASE", "VAST",
   "VEAL", "VEDA", "VEIL", "VEIN", "VEND", "VENT", "VERB", "VERY",
   "VETO", "VICE", "VIEW", "VINE", "VISE", "VOID", "VOLT", "VOTE",
   "WACK", "WADE", "WAGE", "WAIL", "WAIT", "WAKE", "WALE", "WALK",
   "WALL", "WALT", "WAND", "WANE", "WANG", "WANT", "WARD", "WARM",
   "WARN", "WART", "WASH", "WAST", "WATS", "WATT", "WAVE", "WAVY",
   "WAYS", "WEAK", "WEAL", "WEAN", "WEAR", "WEED", "WEEK", "WEIR",
   "WELD", "WELL", "WELT", "WENT", "WERE", "WERT", "WEST", "WHAM",
   "WHAT", "WHEE", "WHEN", "WHET", "WHOA", "WHOM", "WICK", "WIFE",
   "WILD", "WILL", "WIND", "WINE", "WING", "WINK", "WINO", "WIRE",
   "WISE", "WISH", "WITH", "WOLF", "WONT", "WOOD", "WOOL", "WORD",
   "WORE", "WORK", "WORM", "WORN", "WOVE", "WRIT", "WYNN", "YALE",
   "YANG", "YANK", "YARD", "YARN", "YAWL", "YAWN", "YEAH", "YEAR",
   "YELL", "YOGA", "YOKE" ];

var binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', 
              '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'];

function _key2bin(key) {
    res = ''
    for (var i = 0; i < key.length; i++) {
        res += binary[key[i] >> 4] + binary [key[i] & 0x0f];
    }
    return res;
}

function _extract(key, start, length) {
    k = key.substring(start, start+length);
    var acc = 0;
    for (var i = 0; i < k.length; i++) {
        acc = acc * 2 + k.charCodeAt(i) - 48;
    }
    return acc;
}

function key_to_english(key) {

    //pad to 8 bytes
    var padding = [];
    for (var i = 0; i < (8 - (key.length % 8)) % 8; i++) {
        padding.push(0);
    }
    key = padding.concat(key);

    var english = [];
    for (var index = 0; index < key.length; index += 8) {
        var subkey = key.slice(index, index + 8);

        //add parity
        var skbin = _key2bin(subkey);
        var p = 0;
        for (var i = 0; i < 64; i += 2) {
            p = p + _extract(skbin, i, 2);
        }
        subkey.push((p << 6) & 0xff);

        skbin = _key2bin(subkey);
        for (var i = 0; i < 64; i += 11) {
            english.push(rfc1751_wordlist[_extract(skbin, i, 11)]);
        }
    }
    return english.join(' ');
}

function english_to_key(str) {

    var L = str.split(' ');
    var key = [];

    for (var index = 0; index < L.length; index += 6) {
        var sublist = L.slice(index, index + 6);
        var bits = 0;
        var ch = [0,0,0,0,0,0,0,0,0];
        for (var k = 0; k < sublist.length; k++) {
            var word = sublist[k];
            var idx = rfc1751_wordlist.indexOf(word);
            var shift = (8 - (bits + 11) % 8) % 8;
            var y = idx << shift;
            var cl = y >> 16;
            var cc = (y >> 8) & 0xff;
            var cr = y & 0xff;
            var t = Math.floor(bits / 8);
            if (shift > 5) {
                ch[t] = ch[t] | cl;
                ch[t+1] = ch[t+1] | cc;
                ch[t+2] = ch[t+2] | cr;
            } else if (shift > -3) {
                ch[t] = ch[t] | cc;
                ch[t+1] = ch[t+1] | cr;
            } else { 
                ch[t] = ch[t] | cr;
            }
            bits = bits + 11;
        }
        var subkey = ch.slice();

        //check parity
        var skbin = _key2bin(subkey);
        var p = 0;
        for (var i = 0; i < 64; i += 2) {
            p = p + _extract(skbin, i, 2);
        }
        var cs0 = _extract(skbin, 64, 2);
        var cs1 = p & 3;
        if (cs0 != cs1) {
            throw new Error("Parity error at " + word);
        }

        key = key.concat( subkey.slice(0,8) );
    }
    return key;
}

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[89c5bfcf12...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/89c5bfcf1212f4ee460c25413d11a3b1c4c00f64)
#### Friday 2022-01-21 01:34:57 by Christian Morales

I wasn't expecting to make another push today...

I was gonna go back to playing Resident Evil 8 but I figured fuck it I'll see if getting the Zoom glitch fixed with yoyo zooming worked as easy as I thought it would and well uh... butter my bussy and call me Sally it sure fucking did so yeah...

Shit Done Today:
- Zooming (even yoyo zooming) no longer has the issue of Olaf flying past the thing. I made a failsafe to safeguard against it
- What were you expecting more? Fuck you it's Christmas

Glitches Fixed:
- Sometimes Olaf will Zoom past something he wants to zoom to

Noticed Glitches:
- Sometimes a missed parry does enough damage to kill the player regardless of the amount of their health? Gotta look into what's causing that wtf

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[7581f684f8...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/7581f684f8af85f5c65512b93a1863ab31ebb2f2)
#### Friday 2022-01-21 01:34:57 by Christian Morales

Fuckin Health System Shit idk man

Shit Done Today:
- Fixed some animation glitches in the playerHealth script
- Added in code that let's you disable all player input when the bool "inputDisabled" in "playerController" is set to true.
- Added some shit in playerHealth that makes it so that when you get hit it takes away player control for a bit and makes anything on the "parryable" layer no longer
collide with you. Just in case we have non parryable attacks I made a layer for them and have the code set up for those to also not collide with the player. Do we want
players to be able to attack while in this state?

Glitches Fixed:
- The "Hurt" animation wasn't playing originally. I had it set to a bool to determine if it should play and that was a fucking mistake. It'd flip the bool on the same
fucking frame so no shit it never played, what a shit show. I switched it to a Trigger now and it activates just fine.
- Once I fixed the "Hurt" animation I realized it wouldn't play while you were in ball man or running so I added some more transitions in the animator AND some code to
tell the game "hey moron, he just got hurt in ball man mode knock him out of it".
- Fixed the "First hit doesn't take damage" glitch and it was due to my own spaghet code. It's honestly kind of funny I didn't notice this shit sooner but a bit of
distance from the code helps you see it with much more fresh eyes. Just wish it wasn't fucking months of distance but whatever. I only had it set the Health value to
the UI every time you got hurt. Meaning it wasn't that health wasn't subtracting correctly, it just wasn't SHOWING the correct number of HP until you took a fucking
hit. Shit's fixed now though.
- Fucking with the health script to get the hurt animation to play basically accidentally fixed the "Player dying in ball man form makes death state unobtainable"
glitch. Eat your heart out Bob Ross because shit like that is what we call a fucking happy accident.
- The following glitch "Button Axis Dashing: if you press the dash button and no direction it will wait until the next direction you press then immediately dash" was
fixed at some point in some way and I have NO FUCKING clue how. I tried to replicate it and couldn't do it but it was still on the list of glitches so... Problem
solved?

Noticed Glitches:
- Whooooo lord yo-yo zooming is scuffed, it has a ton of issues that might be easier to discuss in a meeting.
- Grappling when next to an object you collide with will cause all kinds of bullshit

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[671cfe24be...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/671cfe24bec0746211f74b7ca6d0d0f6ff6fbd23)
#### Friday 2022-01-21 01:34:57 by Christian Morales

Christian feels like a moron for not understanding basic math

Discuss in the next meeting:
- Is Dashing the way we want it?
- Is damage knockback the way we want it?

Glitches:

- Need to make the player invulnerable while parrying or they'll sometimes hit bullets after a parry
- Sometimes player will keep zooming past enemies in a yo-yo zoom
- Parrying an enemy who shoots projectiles leads to a few problems. Preferably I would like it if one parry captured an attack and a bullet I want it to maybe
destroy the bullet object? We should also have stunned enemies unable to spawn more bullets. Or even maybe stop enemies from spawning bullets during a danger
zone attack? This might mean we will want to make bullet spawning part of Universal Enemy Behavior? Food for thought... This also makes me wonder what we should
do if you're sandwiched between two danger zone attacks? What takes priority? What happens if you're halfway through a yo-yo zoom and you parry a Danger Zone attack?
Will it cause nested Yo-Yo loops? Ehhhhh fuck it whatever I'm tired I got work in the mornin I'm gettin too old for this shit I'm a week away from retirement I can't
relate to these kids no more with their tiktaks and their fuckin whatever you have it fuckin I don't know, fugehtabouteeet.
- Whooooo lord yo-yo zooming is scuffed, it has a ton of issues that might be easier to discuss in a meeting.
- Grappling when next to an object you collide with will cause all kinds of bullshit
- Player is able to parry after getting hit. Maybe disable parry button after taking damage?

Shit Done Today:
- Become invincible after successful parry
- Tried to fix the glitch of zooming past stuff by calculating the amount of distance you zoom but it wasn't working out

Glitches Fixed:

Noticed Glitches:

I'll come back to this grapple zoom shit later I got eggnog to drink and a broken car to despair over.

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[cb3c968673...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/cb3c9686733c59a31ea2a2844a66466539190f03)
#### Friday 2022-01-21 01:34:57 by Christian Morales

More Parrying shit BAYBEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

Shit Done Today:
- Bullets reflect when parried and when reflected only hurt enemies not player
- Enemy stun function created but since enemy movement is not implemented it kind of doesn't do shit. But it's there and boy do it look purty
- Cuphead-esque bounce after parry
- Yo-Yo Parry Slightly implemented but obviously needs some fucking polish man.

Glitches Fixed:
- Bullets no longer collide with grapple rope
- Danger Zone attacks weren't despawning correctly and their despawn coroutine was being called like 400 times in a row. It works now and now only calls the coroutine once

Noticed Glitches:
- Button Axis Dashing: if you press the dash button and no direction it will wait until the next direction you press then immediately dash.
- First hit doesn't take damage
- Need to make the player invulnerable while parrying or they'll sometimes hit bullets after a parry
- Player dying in ball man form makes death state unobtainable
- Sometimes player will keep zooming past enemies in a yo-yo zoom
- Parrying an enemy who shoots projectiles leads to a few problems. Preferably I would like it if one parry captured an attack and a bullet I want it to maybe destroy the bullet object? We should also have stunned enemies unable to spawn more bullets. Or even maybe stop enemies from spawning bullets during a danger zone attack? This might mean we will want to make bullet spawning part of Universal Enemy Behavior? Food for thought... This also makes me wonder what we should do if you're sandwiched between two danger zone attacks? What takes priority? What happens if you're halfway through a yo-yo zoom and you parry a Danger Zone attack? Will it cause nested Yo-Yo loops? Ehhhhh fuck it whatever I'm tired I got work in the mornin I'm gettin too old for this shit I'm a week away from retirement I can't relate to these kids no more with their tiktaks and their fuckin whatever you have it fuckin I don't know, fugehtabouteeet. Sorry, most of this post seemed too professional so I had to make sure I fucked it up at the end somehow.

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[9754e445d8...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/9754e445d8ebae937a5447e5e568529460fd7cd5)
#### Friday 2022-01-21 01:34:57 by Christian Morales

Changes Made During the Meeting

Good lord I am a fucking moron for not documenting shit better I'm sorry frends I am a hack fraud. We fixed some shit with these changes but I don't recall everything we fixed. For sure we fixed the glitch of the crazy goddamn bullshit that would happen when you tried to wrap around a circular object.

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[59f2f32b17...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/59f2f32b17d3e72f6543248f5a3408ca8692f5ca)
#### Friday 2022-01-21 01:34:57 by Christian Morales

Got that Zoom Overshoot glitch fixed BITCH

Don't feel like filling out that little thing I've been doing normally but I did in fact fix the glitch where players would overshoot a zoom. SORT OF. The problem is that it doesn't work with yoyo zooming but come onnnnnn that shit oughtta be easy riiiight? In theory all I have to do is when a yoyo zoom happens tell the script "we have a bit more distance to travel before you shut us down" and then the script will totally give us that distance to travel and it'll all work out. Or maybe it won't and we'll have to win a skii competition to win the skii resort back to get that greedy fucking cunt of a script to give us our motherfucking goddamn distance back before we fucking take it back you motherfuckers just try and pry it from my goddamn cold dead hands you motherfucker just fucking try it I fucking dare you you piece of shit I fucking DARE you!

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[4dc0e66f48...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/4dc0e66f48e5df698c44c86e5e11f94d953a91b7)
#### Friday 2022-01-21 01:34:57 by Christian Morales

Fuckin... Uhhh Parrying Bullets and shit dude?

So uh like fuckin uhm uh yeah like parrying bullets like fuckin totally makes them at least reverse direction and shit yeah uh still haven't got the bullets stun enemies yet though yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeup.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[eb384bd2d7...](https://github.com/Paxilmaniac/Skyrat-tg/commit/eb384bd2d72a5b23dd9785cc06815049d507d3d5)
#### Friday 2022-01-21 01:59:19 by Useroth

Telemetry 'n shit (#10810)

* Refactors dbcore and limits the maximum amount of concurrent async queries to a variable amount (#59676)

Refactors dbcore to work off a subsystem if executed async and limits the maximum amount of concurrent async queries to 25.

This has been tested locally on a mysql docker image and there were no crashes (as long as you didn't run it with debug extools) + data was getting recorded fine.
Why It's Good For The Game

May or may not resolve terry crashes, however, each query creates a new thread which takes up 2mb, preventing the game from using that 2mb. This can lead to ooms if they stack up, e.g. due to poor connectivity. This solves that issue.

maintainer note: this did not actually resolve the crashes, but has value anyway. Crashes were sidestepped fixed by finding out Large Address Awareness works

cl
refactor: Refactors dbcore.dm to possibly resolve the crashes that happen on Terry.
/cl

* Fixes an oversight in database code and cleans up telemetry (#64177)

As it is right now, we never actually clear the temporary list processing_queries
So if the subsystem is for some reason unable to complete a run, we will just whip right back around to it again
If it's been long enough, this could even cause horrific log spam. There was just now a manuel round with roughly 30k undeleted query errors. not good.

But what was actually not deleting you may ask?
Well

When you create a db request, a 5 minute timer starts. after those 5 minutes are up, the request is qdeleted by the db subsystem
This is to prevent the creation of unused requests, and to handle requests that are never cleaned up

Telemetry code was creating all of its db requests inside a for loop that could check tick, and then later
attempting to call them in series

Since requests by default sleep, this almost always lead to undeleted queries, which harddel'd given long enough periods

I've fixed this by moving the data gathering away from the query creation
Why is it good for the game

I was working on atmos code, happy, safe in my delusion, when suddenly I got a ping from tattle freaking out over 200 undeleted queries a second
This resolves that issue, so I can once again live in peace
Changelog

cl
admin: Telemetry code will spam you with undeleted query logs much less often now!
server: Improved how the db subsystem handles undeleted queries, should never have an incident like that again
/cl

* Fixes an error in telemetry queries (#64205)

* Hardsynced time_track.dm with upstream

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [RedMisao/Cataclysm-DDA-Touhou-Mod](https://github.com/RedMisao/Cataclysm-DDA-Touhou-Mod)@[f2395e263f...](https://github.com/RedMisao/Cataclysm-DDA-Touhou-Mod/commit/f2395e263f6df1116ebb009c2ef3dccf71a27a1d)
#### Friday 2022-01-21 02:38:12 by RedMisao

0.9.1.2b mostly a backup

- Added dodo, moa, eurypterids with their related files
- (Forgot to mention for the previous upload, added youkai: Beast of Gévaudan and nightcrawler)
- Added basic recipes with generic arthropod flesh (from eurypterids)
- Changed chicken_meat and related stuff to bird_meat
- Added magical material for ethereal items. This is so Remi's blood spells don't create infinite blood, and for flavor
- Added fire ball spell for Mokou (untested)
- Kaenbyou vengeful spirit release should technically work now (untested)

---
## [apache/couchdb](https://github.com/apache/couchdb)@[f0994aa42f...](https://github.com/apache/couchdb/commit/f0994aa42ff797cab6061599924d6f28751659e7)
#### Friday 2022-01-21 02:46:53 by Adam Kocoloski

Refactor Jenkins to dynamically generate stages

This is one of those situations where you go in to make a small change,
see an opportunity for some refactoring, and get sucked into a rabbit
hole that leaves you wondering if you have any idea how computers
actually work. My initial goal was simply to update the Erlang version
used in our binary packages to a modern supported release. Along the
way I decided I wanted to figure out how to eliminate all the copypasta
we generate for making any change to this file, and after a few days of
hacking here we are. This rewrite has the following features:

* Updates to use Debian 11 (current stable) as the base image for
  building releases and packaging repos.

* Defaults to Erlang 24.2 as the embedded Erlang version in packages.

* Dynamically generates the parallel build stages used to test and
  package CouchDB on various OSes. This is accomplished through a bit
  of scripted pipeline code that relies on two new methods defined at
  the beginning of the Jenkinsfile, one for "native" builds on macOS
  and FreeBSD and one for container-based builds. See comments in the
  Jenkinsfile for additional details.

* Expands commands like `make check` into a series of steps to improve
  visibility. The Jenkins UI will now show the time spent in each step
  of the build process, and if a step (e.g. `make eunit`) fails it will
  only expand the logs for that step by default instead of showing the
  logs for the entire build stage. The downside is that if we do make
  changes to the series of targets underneath `check` we need to
  remember to update the Jenkinsfile as well.

* Starts per-stage timer _after_ agent is acquired. Previously builds could
  fail with a 15m timeout when all they did was sit in the build queue.

This is a cherry-pick of 9b6454b from main, modified to drop the
MINIMUM_ERLANG_VERSION to 20 and adding ARM and POWER back into the
matrix. Still need to build newer container images for those
architectures, though, so for now they're still Buster / Erlang 20.

---
## [Not-A-Thinker/OUR-GamesV2](https://github.com/Not-A-Thinker/OUR-GamesV2)@[fb6f1b10e3...](https://github.com/Not-A-Thinker/OUR-GamesV2/commit/fb6f1b10e3b1406fcc8fb023f7fc67b9d6a9deb9)
#### Friday 2022-01-21 02:51:17 by Kleon

Tornado big one tracking skill tweak

i hate my life.

---
## [polygoblyn/MonkeStation](https://github.com/polygoblyn/MonkeStation)@[040b7ff839...](https://github.com/polygoblyn/MonkeStation/commit/040b7ff839d51d4db2ce1747f92312e0925bccd2)
#### Friday 2022-01-21 03:15:11 by Zonespace

Adds Flavor Text (#48)

* lgtm

* aaaAAAA

* might be better idk

* flavor-examine

* info

* haaa fuck you github

---
## [HappenLee/incubator-doris](https://github.com/HappenLee/incubator-doris)@[ef2ea1806e...](https://github.com/HappenLee/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Friday 2022-01-21 06:00:37 by HB

[docs] Improve the chapter on debugging FE in doc.  (#7309)

At present, there are defects in the chapter on debugging FE in doc. My colleagues and I stepped on the pit when 
building the debugging environment, so I want to improve this chapter in combination with my own stepping on the pit 
experience.

The following is my explanation of the changes: 

1. mkdir -p ./thirdparty/installed/bin
explain: When I downloaded versions 0.14 and 0.15, there were no files under thirdparty, so I didn't know whether to 
create it myself or what to do. Finally, I decided to create it myself. I think it's necessary to add instructions here.

2. Add installation thrift@0.13.0 Failed handling method. 
explain: My colleagues and I failed to find the installation package when executing the installation command, and finally 
found a solution on GitHub. Therefore, I added the handling method of the problem to avoid other Mac users from 
getting stuck in this place.

3. Fixed an error in the generated code description.
explain: Before I finished building the code, I debugged FE, and I failed all the time. Idea hints that no files can be found. 
Later, after consulting with morningman in wechat group, it was understood that `mvn install -DskipTests` does not 
need to execute `mvn generate-sources` after execution. This is inconsistent with the description in the document and 
needs to be corrected.

---
## [NBtheMC/The-Adventurers-Guild](https://github.com/NBtheMC/The-Adventurers-Guild)@[7ba7db6ed9...](https://github.com/NBtheMC/The-Adventurers-Guild/commit/7ba7db6ed9393cb1e84a8e38d8d865b5c60ff2fa)
#### Friday 2022-01-21 06:21:54 by Eric Long

Storylet System works. Fuck yeah.

fuck yeah. Shit's mostly done.

---
## [UMM-CSci-3601/3601-iteration-template](https://github.com/UMM-CSci-3601/3601-iteration-template)@[8716543574...](https://github.com/UMM-CSci-3601/3601-iteration-template/commit/8716543574b925fc6ff2b3112e101fddabecdf8c)
#### Friday 2022-01-21 06:28:00 by Nic McPhee

Disable several Checkstyle checks

This disables several Checkstyle checks that are included in the Sun configuration. I like the spirit of these, but our experience is that these tend to confuse people more than help them. Also, the structure of the Java code in the project has become quite simple because the server library (e.g., Javalin) encapsulates the bulk of the design complexity, leaving us to just write code at the "leaves" of the design.

The disabled checks are:

   *  DesignForExtension: This only really makes sense if we're building a reasonably
         sophisticate OO library, and that kind of design really doesn't
         come up in this class, because the server library (e.g., Javalin)
         encapsulates all that design work, leaving us to just act around
         the "leaves" of the design.
   *  HideUtilityClassConstructor: If everything is static 
         in a class, then it shouldn't have
         an accessible constructor. This is both subtle and
         confusing, and not likely to come up much in the class,
         so we'll just leave it out.
   * FinalParameters: I really likes the *intent* of this rule,
         but it's really trying to use CheckStyle to fix
         a mistake in the design of Java. This just confuses
         students, and requires a ton of extra typing
         that probably doesn't buy folks much.

---
## [ImACoderImACoderImACoder/onyx](https://github.com/ImACoderImACoderImACoder/onyx)@[1bddc9a284...](https://github.com/ImACoderImACoderImACoder/onyx/commit/1bddc9a2843e96582d0d0eda694cd57b05f70cd3)
#### Friday 2022-01-21 07:45:18 by A Coder

What an exciting update! Android is now supported! Themes are supported and we are shipping with 4, yes I said 4, 4! themes!  4.  Introduced styled components. they're all over the place right now. I have some ideas on how the code can be better but I was really excited to get this update out and it will take me some time to think about what is optimal.  I've also removed the fan/heat debounces.  I put in some checks to prevent excessive spam, but I think this is more of a coding/user burden than it is a feature.  So I've decided to remove it.  The only thing that still debounces is the plus/minus temperature button. This update also has a great number of stability and performance improvements (for real).  I do feel obligated to thank android for that.  I think the phone I bought is so slow it guarenteed a loss in some kind of race condition.  This condition happens almost never on pc and iphone.  After many hours of debugging I figured out that I needed to await on my notification subscriptions.  This update made me realize I should take some time to reflect on my desigin.  There were mistkaes I made in the beginning that I kind of forgot about since they appeared to work.   Now that I have more experience with BLE programming I should really go back to the initial core features and see if there are any changes I'd like to make.  I did notice the writeValue api I'm using is deprecated so I'll be updating those calls soon.  Hopefully that doesn't break anything on those 3rd party mobile browsers.  If you're still reading... good for you.

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Friday 2022-01-21 08:39:40 by Albert Liu

Add PresetService (User Presets Step 3) (#1164)

Final feature demo:

![Kapture 2022-01-13 at 23 36 00](https://user-images.githubusercontent.com/12578068/149469927-b62bfa43-4701-4498-a489-565aea36da2c.gif)

---------------------------

This PR is extracted from #1041 as step 2 of the User Preset feature.

rebase of picked commits pertaining to PresetServiceService onto Albert-UserDictionaryService

PresetService provides the ability to save and "apply" collections of settings (represented by objects) that a user might find convenient to save and apply as a group. These groups are called Presets.

PresetService uses DictionaryService to store presets (it creates kind of a *view* in the database sense, of the user dictionary, that only includes Presets)

Changes from last review (for Yicong)
 - Code comments
 - fixed subscription memory leak by using takeUntil(observable), where said observable completes on NgOndestroy
 - DictionaryService now attempts to init whenever client logs in (sorry, you'll have to re-review my changes to DictionaryService)
 - PresetService now has public ready promise/value member 
   - This indicates that its init isn't complete until DictionaryService's init is complete (which is async, and cant be awaited in the constructor)
 - DeletePreset now built into PresetService (don't know why I ever didn't have that)
 - Revert Changes to Styles.scss to fix Karma test runner interface (I originally changed them as a workaround for an ng-zorro component that's no longer used)

 Note: for this step, I had less time and more complex code to test. I'm not sure I caught all the bugs, but it passes unit tests.
The quality of the code in this pr is lesser, in my opinion, so You'll have to be a little more careful on my behalf.



Co-authored-by: Zuozhi Wang <zuozhiw@gmail.com>
Co-authored-by: Yicong Huang <17627829+Yicong-Huang@users.noreply.github.com>

---
## [Ken-Blooket-hacks/Blooket-hack-working2022-](https://github.com/Ken-Blooket-hacks/Blooket-hack-working2022-)@[ad95b17776...](https://github.com/Ken-Blooket-hacks/Blooket-hack-working2022-/commit/ad95b1777601878ac6d15e58c989caf565c27846)
#### Friday 2022-01-21 08:57:50 by KenProBlooket

Add 500 tokens(free)

By Glixzzy, visit https://github.com/glixzzy/blooket-hack also.
Don't hack or you'll be banned by the god of blooket: Ben steward
Btw... visit SchoolCheats.net/blooket for all hacks at once, thank you!

---
## [plumvillage/newsletter](https://github.com/plumvillage/newsletter)@[89cec07761...](https://github.com/plumvillage/newsletter/commit/89cec077610ffdd3fb3e42ed4d2d238b04c85517)
#### Friday 2022-01-21 09:48:15 by giacanaloha

Update brother-chan-troi-duc-niem--i-have-a-dream.md

edited this section per Br Duc N's request
I have a dream that one day many different spiritual and faith traditions, humanitarian groups and NGOs will come together to co-create and follow a code of Global Ethics similar to the Five Mindfulness Trainings. I am convinced that this can serve as a connecting element between different groups and engaged people, and as a foundation, and inspiration for a new movement.

---
## [mawrick26/SM8250](https://github.com/mawrick26/SM8250)@[844428d326...](https://github.com/mawrick26/SM8250/commit/844428d3263e3ef2cab040a40855e7d8a633c841)
#### Friday 2022-01-21 13:55:59 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [snickl/lpppd](https://github.com/snickl/lpppd)@[81ad945630...](https://github.com/snickl/lpppd/commit/81ad945630120cc1c27c8bb00503be42b76ff202)
#### Friday 2022-01-21 16:12:23 by Jaco Kroon

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
## [mate-amargo/dwm](https://github.com/mate-amargo/dwm)@[67d76bdc68...](https://github.com/mate-amargo/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2022-01-21 16:27:43 by Chris Down

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
## [oracle/linux-uek](https://github.com/oracle/linux-uek)@[99782a23ed...](https://github.com/oracle/linux-uek/commit/99782a23ed03d618209b3f20a05507d44ee6be62)
#### Friday 2022-01-21 17:01:26 by Darrick J. Wong

xfs: change the order in which child and parent defer ops are finished

The defer ops code has been finishing items in the wrong order -- if a
top level defer op creates items A and B, and finishing item A creates
more defer ops A1 and A2, we'll put the new items on the end of the
chain and process them in the order A B A1 A2.  This is kind of weird,
since it's convenient for programmers to be able to think of A and B as
an ordered sequence where all the sub-tasks for A must finish before we
move on to B, e.g. A A1 A2 D.

Right now, our log intent items are not so complex that this matters,
but this will become important for the atomic extent swapping patchset.
In order to maintain correct reference counting of extents, we have to
unmap and remap extents in that order, and we want to complete that work
before moving on to the next range that the user wants to swap.  This
patch fixes defer ops to satsify that requirement.

The primary symptom of the incorrect order was noticed in an early
performance analysis of the atomic extent swap code.  An astonishingly
large number of deferred work items accumulated when userspace requested
an atomic update of two very fragmented files.  The cause of this was
traced to the same ordering bug in the inner loop of
xfs_defer_finish_noroll.

If the ->finish_item method of a deferred operation queues new deferred
operations, those new deferred ops are appended to the tail of the
pending work list.  To illustrate, say that a caller creates a
transaction t0 with four deferred operations D0-D3.  The first thing
defer ops does is roll the transaction to t1, leaving us with:

t1: D0(t0), D1(t0), D2(t0), D3(t0)

Let's say that finishing each of D0-D3 will create two new deferred ops.
After finish D0 and roll, we'll have the following chain:

t2: D1(t0), D2(t0), D3(t0), d4(t1), d5(t1)

d4 and d5 were logged to t1.  Notice that while we're about to start
work on D1, we haven't actually completed all the work implied by D0
being finished.  So far we've been careful (or lucky) to structure the
dfops callers such that D1 doesn't depend on d4 or d5 being finished,
but this is a potential logic bomb.

There's a second problem lurking.  Let's see what happens as we finish
D1-D3:

t3: D2(t0), D3(t0), d4(t1), d5(t1), d6(t2), d7(t2)
t4: D3(t0), d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3)
t5: d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)

Let's say that d4-d11 are simple work items that don't queue any other
operations, which means that we can complete each d4 and roll to t6:

t6: d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
t7: d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
...
t11: d10(t4), d11(t4)
t12: d11(t4)
<done>

When we try to roll to transaction #12, we're holding defer op d11,
which we logged way back in t4.  This means that the tail of the log is
pinned at t4.  If the log is very small or there are a lot of other
threads updating metadata, this means that we might have wrapped the log
and cannot get roll to t11 because there isn't enough space left before
we'd run into t4.

Let's shift back to the original failure.  I mentioned before that I
discovered this flaw while developing the atomic file update code.  In
that scenario, we have a defer op (D0) that finds a range of file blocks
to remap, creates a handful of new defer ops to do that, and then asks
to be continued with however much work remains.

So, D0 is the original swapext deferred op.  The first thing defer ops
does is rolls to t1:

t1: D0(t0)

We try to finish D0, logging d1 and d2 in the process, but can't get all
the work done.  We log a done item and a new intent item for the work
that D0 still has to do, and roll to t2:

t2: D0'(t1), d1(t1), d2(t1)

We roll and try to finish D0', but still can't get all the work done, so
we log a done item and a new intent item for it, requeue D0 a second
time, and roll to t3:

t3: D0''(t2), d1(t1), d2(t1), d3(t2), d4(t2)

If it takes 48 more rolls to complete D0, then we'll finally dispense
with D0 in t50:

t50: D<fifty primes>(t49), d1(t1), ..., d102(t50)

We then try to roll again to get a chain like this:

t51: d1(t1), d2(t1), ..., d101(t50), d102(t50)
...
t152: d102(t50)
<done>

Notice that in rolling to transaction #51, we're holding on to a log
intent item for d1 that was logged in transaction #1.  This means that
the tail of the log is pinned at t1.  If the log is very small or there
are a lot of other threads updating metadata, this means that we might
have wrapped the log and cannot roll to t51 because there isn't enough
space left before we'd run into t1.  This is of course problem #2 again.

But notice the third problem with this scenario: we have 102 defer ops
tied to this transaction!  Each of these items are backed by pinned
kernel memory, which means that we risk OOM if the chains get too long.

Yikes.  Problem #1 is a subtle logic bomb that could hit someone in the
future; problem #2 applies (rarely) to the current upstream, and problem

This is not how incremental deferred operations were supposed to work.
The dfops design of logging in the same transaction an intent-done item
and a new intent item for the work remaining was to make it so that we
only have to juggle enough deferred work items to finish that one small
piece of work.  Deferred log item recovery will find that first
unfinished work item and restart it, no matter how many other intent
items might follow it in the log.  Therefore, it's ok to put the new
intents at the start of the dfops chain.

For the first example, the chains look like this:

t2: d4(t1), d5(t1), D1(t0), D2(t0), D3(t0)
t3: d5(t1), D1(t0), D2(t0), D3(t0)
...
t9: d9(t7), D3(t0)
t10: D3(t0)
t11: d10(t10), d11(t10)
t12: d11(t10)

For the second example, the chains look like this:

t1: D0(t0)
t2: d1(t1), d2(t1), D0'(t1)
t3: d2(t1), D0'(t1)
t4: D0'(t1)
t5: d1(t4), d2(t4), D0''(t4)
...
t148: D0<50 primes>(t147)
t149: d101(t148), d102(t148)
t150: d102(t148)
<done>

This actually sucks more for pinning the log tail (we try to roll to t10
while holding an intent item that was logged in t1) but we've solved
problem #1.  We've also reduced the maximum chain length from:

    sum(all the new items) + nr_original_items

to:

    max(new items that each original item creates) + nr_original_items

This solves problem #3 by sharply reducing the number of defer ops that
can be attached to a transaction at any given time.  The change makes
the problem of log tail pinning worse, but is improvement we need to
solve problem #2.  Actually solving #2, however, is left to the next
patch.

Note that a subsequent analysis of some hard-to-trigger reflink and COW
livelocks on extremely fragmented filesystems (or systems running a lot
of IO threads) showed the same symptoms -- uncomfortably large numbers
of incore deferred work items and occasional stalls in the transaction
grant code while waiting for log reservations.  I think this patch and
the next one will also solve these problems.

As originally written, the code used list_splice_tail_init instead of
list_splice_init, so change that, and leave a short comment explaining
our actions.

Signed-off-by: Darrick J. Wong <darrick.wong@oracle.com>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Brian Foster <bfoster@redhat.com>

(cherry picked from commit 27dada070d59c28a441f1907d2cec891b17dcb26)
Orabug: 33548995
Signed-off-by: Chandan Babu R <chandan.babu@oracle.com>
Reviewed-by: Allison Henderson <allison.henderson@oracle.com>
Signed-off-by: Brian Maly <brian.maly@oracle.com>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[f2ebb21bd1...](https://github.com/microsoft/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Friday 2022-01-21 17:41:17 by Mike Griese

Add snap-layouts support to the Terminal (#11680)

Adds snap layout support to the Terminal's maximize button. This PR is
full of BODGY, so brace yourselves.

Big thanks to Chris Swan in #11134 for building the prototype.
I don't believe this solves #8795, because XAML islands can't get
nchittest messages

- The window procedure for the drag bar forwards clicks on its client
  area to its parent as non-client clicks.
- BODGY: It also _manually_ handles the caption buttons. They exist in
  the titlebar, and work reasonably well with just XAML, if the drag bar
  isn't covering them.
- However, to get snap layout support, we need to actually return
  `HTMAXBUTTON` where the maximize button is. If the drag bar doesn't
  cover the caption buttons, then the core input site (which takes up
  the entirety of the XAML island) will steal the `WM_NCHITTEST` before
  we get a chance to handle it.
- So, the drag bar covers the caption buttons, and manually handles
  hovering and pressing them when needed. This gives the impression that
  they're getting input as they normally would, even if they're not
  _really_ getting input via XAML.
- We also need to manually display the button tooltips now, because XAML
  doesn't know when they've been hovered for long enough. Hence, the
  `_displayToolTip` `ThrottledFuncTrailing`

## Validation
Minimized, maximized, restored down, hovered the buttons slowly, moved
the mouse over them quickly, they feel the same as before. But now with
snap layouts appearing.

## TODO!
* [x] I'm working on getting the ToolTips on the caption buttons back. Alas, I needed a demo of this _today_, so I'll fix that tomorrow morning.
* [x] mild concern: I should probably test Win 10 to make sure there wasn't weird changes to the message loop in win11 that means this is broken on win10.
* [x] I think I used the wrong issue number for tons of my comments throughout this PR. Double check that. Should be #9443, not #9447. 

Closes #9443
I thought this took care of #8587 ~as a bonus, because I was here, and the fix is _now_ trivial~, but looking at the latest commit that regressed.

Co-authored-by: Chris Swan <chswan@microsoft.com>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[442432ea15...](https://github.com/microsoft/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Friday 2022-01-21 17:41:17 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [KrishnakantShedge/kernel_realme_RMX1851](https://github.com/KrishnakantShedge/kernel_realme_RMX1851)@[d1d6188bc8...](https://github.com/KrishnakantShedge/kernel_realme_RMX1851/commit/d1d6188bc8a27821b7843a2de012c8e3aade04b8)
#### Friday 2022-01-21 19:27:39 by Francis Yan

BACKPORT: tcp: instrument tcp sender limits chronographs

This patch implements the skeleton of the TCP chronograph
instrumentation on sender side limits:

	1) idle (unspec)
	2) busy sending data other than 3-4 below
	3) rwnd-limited
	4) sndbuf-limited

The limits are enumerated 'tcp_chrono'. Since a connection in
theory can idle forever, we do not track the actual length of this
uninteresting idle period. For the rest we track how long the sender
spends in each limit. At any point during the life time of a
connection, the sender must be in one of the four states.

If there are multiple conditions worthy of tracking in a chronograph
then the highest priority enum takes precedence over
the other conditions. So that if something "more interesting"
starts happening, stop the previous chrono and start a new one.

The time unit is jiffy(u32) in order to save space in tcp_sock.
This implies application must sample the stats no longer than every
49 days of 1ms jiffy.

saalim :- Drop rate_app_limited from tcp header (already present)
original :- https://github.com/danascape/kernel-msm-4.14/commit/05b055e89121394058c75dc354e9a46e1e765579#diff-4ddfd98f3453244962e17ac121bea6162887af47d0531ba6e2cf49a941edf2c9

Signed-off-by: Francis Yan <francisyyan@gmail.com>
Signed-off-by: Yuchung Cheng <ycheng@google.com>
Signed-off-by: Soheil Hassas Yeganeh <soheil@google.com>
Acked-by: Neal Cardwell <ncardwell@google.com>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: danascape <saalimquadri1@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dakkshesh <dakkshesh5@gmail.com>

---
## [Bobthe28th/tgstation](https://github.com/Bobthe28th/tgstation)@[7bead07444...](https://github.com/Bobthe28th/tgstation/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Friday 2022-01-21 19:43:32 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [mamedev/mame](https://github.com/mamedev/mame)@[a49e215466...](https://github.com/mamedev/mame/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Friday 2022-01-21 20:39:29 by Firehawke

Apple II updates for January 2022 (#9189)

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Earth Science: Interplanetary Travel (cleanly cracked) [4am, Firehawke]
Isaac Newton and F.I.G. Newton (cleanly cracked) [4am, Firehawke]
Return to Reading: The Call of the Wild (cleanly cracked) [4am, Firehawke]
The German Hangman (cleanly cracked) [4am, Firehawke]
Legionnaire (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Bridge Tutor with Precision and Scientific Bidding (cleanly cracked) [4am, san inc, Firehawke]
The French Hangman (cleanly cracked) [4am, Firehawke]
The Russian Hangman (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Mickey's Space Adventure [4am, Firehawke]
The Environment Life Dynamic [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Stellar Power [4am, Firehawke]

New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Ken Uston's Professional Blackjack (Version 1.12) (cleanly cracked) [4am, Firehawke]
Dinosaur's Lunch (cleanly cracked) [4am, Firehawke]
Race Car Keys (cleanly cracked) [4am, Firehawke]
Functional Harmony: Basic Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Diatonic Seventh Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Borrowed and Altered Chords (cleanly cracked) [4am, Firehawke]
Building Reading Skills: The Letter-Sound Farm (cleanly cracked) [4am, Firehawke]
Follow Me (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

The German Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Russian Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Spanish Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Exploring Library Land (cleanly cracked) [4am, Firehawke]
Library Treasure Hunt (cleanly cracked) [4am, Firehawke]
Expedition U.S.A.! (cleanly cracked) [4am, Firehawke]
Codes and Cyphers (cleanly cracked) [4am, san inc, Firehawke]
Ripley's Believe It Or Not: Beginning Library Research Skills (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Glutton [4am, Firehawke]

---
## [bgoonz/Javascript](https://github.com/bgoonz/Javascript)@[b3b4ad43a3...](https://github.com/bgoonz/Javascript/commit/b3b4ad43a3c4f84647869daffac8773320b9cc7f)
#### Friday 2022-01-21 22:01:41 by Legendary Noob

chore: Added Sum of Digits Implementation (#684)

* Added the main logic, need to work on Tests

* Added tests for SOD

* Fix typo and add Wikipedia link in comments

* Fix mistake in SumOfDigitsUsingStrings

I intended to initially write a different implementation but I wrote something else :man_facepalming:

* Converted Spacing from Tabs to Spaces

* Oops, forgot about the test file

* Fixed semicolon problems...

* Oops, I missed a few semicolons

* Linting is hell TwT

Co-authored-by: SpiderMath <{ID}+{username}@users.noreply.github.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[a2fa7799f3...](https://github.com/jlsnow301/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Friday 2022-01-21 22:29:10 by Jeremiah

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
## [guest3444307/OneshotGB](https://github.com/guest3444307/OneshotGB)@[bf56e0a341...](https://github.com/guest3444307/OneshotGB/commit/bf56e0a3415e437bb4ea282d177d080f3af24d1c)
#### Friday 2022-01-21 22:49:13 by guest3444307

1/21/22 minor update

god damn it, i really should ask the discord for help, i tried just replacing the sprite that got replaced and it just bloody messed with a different sprite, the only solution i see is to replace every sprite every time, it seems to be tied to replacing the player sprite (why!!! also noticed a difference in speed between color when trying to see if that would fix anything suggesting poor performance (should've seen that coming with how poorly optimized this is!)

---
## [12589-PioneerRobotics/Freight-Frenzy](https://github.com/12589-PioneerRobotics/Freight-Frenzy)@[7fdada18f6...](https://github.com/12589-PioneerRobotics/Freight-Frenzy/commit/7fdada18f62991e55c945b2b37140cb37f473d80)
#### Friday 2022-01-21 23:07:28 by Backup Programming laptop

ausPicious tumor [cancerous};

foreach joke in jokes (
Tumor.Joke = funny;
Armaan.SenseOfHumor = Tumorous (Haha Funny because humorous)
}

---

