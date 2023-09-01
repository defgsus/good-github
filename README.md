## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-31](docs/good-messages/2023/2023-08-31.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,296,202 were push events containing 3,471,666 commit messages that amount to 265,348,963 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [hemidactylus/langchain](https://github.com/hemidactylus/langchain)@[d57d08fd01...](https://github.com/hemidactylus/langchain/commit/d57d08fd01e05889af4e59fa3577c824de6df09d)
#### Thursday 2023-08-31 00:06:23 by nikhilkjha

Initial commit for comprehend moderator (#9665)

This PR implements a custom chain that wraps Amazon Comprehend API
calls. The custom chain is aimed to be used with LLM chains to provide
moderation capability that let’s you detect and redact PII, Toxic and
Intent content in the LLM prompt, or the LLM response. The
implementation accepts a configuration object to control what checks
will be performed on a LLM prompt and can be used in a variety of setups
using the LangChain expression language to not only detect the
configured info in chains, but also other constructs such as a
retriever.
The included sample notebook goes over the different configuration
options and how to use it with other chains.

###  Usage sample
```python
from langchain_experimental.comprehend_moderation import BaseModerationActions, BaseModerationFilters

moderation_config = { 
        "filters":[ 
                BaseModerationFilters.PII, 
                BaseModerationFilters.TOXICITY,
                BaseModerationFilters.INTENT
        ],
        "pii":{ 
                "action": BaseModerationActions.ALLOW, 
                "threshold":0.5, 
                "labels":["SSN"],
                "mask_character": "X"
        },
        "toxicity":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        },
        "intent":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        }
}

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})

print(response['output'])


```
### Output
```
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii validation...
Found PII content..stopping..
The prompt contains PII entities and cannot be processed
```

---------

Co-authored-by: Piyush Jain <piyushjain@duck.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Bagatur <baskaryan@gmail.com>

---
## [LittleHuman1/README.md](https://github.com/LittleHuman1/README.md)@[5062c2aec3...](https://github.com/LittleHuman1/README.md/commit/5062c2aec38677014e1ad894e213085045262ef3)
#### Thursday 2023-08-31 00:08:57 by LittleHuman1

README.md

Semantic Versioning 1.0.0-beta
In the world of software management there exists a dread place called “dependency hell.” The bigger your system grows and the more packages you integrate into your software, the more likely you are to find yourself, one day, in this pit of despair.

In systems with many dependencies, releasing new package versions can quickly become a nightmare. If the dependency specifications are too tight, you are in danger of version lock (the inability to upgrade a package without having to release new versions of every dependent package). If dependencies are specified too loosely, you will inevitably be bitten by version promiscuity (assuming compatibility with more future versions than is reasonable). Dependency hell is where you are when version lock and/or version promiscuity prevent you from easily and safely moving your project forward.

As a solution to this problem, I propose a simple set of rules and requirements that dictate how version numbers are assigned and incremented. For this system to work, you first need to declare a public API. This may consist of documentation or be enforced by the code itself. Regardless, it is important that this API be clear and precise. Once you identify your public API, you communicate changes to it with specific increments to your version number. Consider a version format of X.Y.Z (Major.Minor.Patch). Bug fixes not affecting the API increment the patch version, backwards compatible API additions/changes increment the minor version, and backwards incompatible API changes increment the major version.

I call this system “Semantic Versioning.” Under this scheme, version numbers and the way they change convey meaning about the underlying code and what has been modified from one version to the next.

Semantic Versioning Specification (SemVer)
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

Software using Semantic Versioning MUST declare a public API. This API could be declared in the code itself or exist strictly in documentation. However it is done, it should be precise and comprehensive.

A normal version number MUST take the form X.Y.Z where X, Y, and Z are integers. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically by increments of one. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.

When a major version number is incremented, the minor version and patch version MUST be reset to zero. When a minor version number is incremented, the patch version MUST be reset to zero. For instance: 1.1.3 -> 2.0.0 and 2.1.7 -> 2.2.0.

A pre-release version number MAY be denoted by appending an arbitrary string immediately following the patch version and a decimal point. The string MUST be comprised of only alphanumerics plus dash [0-9A-Za-z-] and MUST begin with an alpha character [A-Za-z]. Pre-release versions satisfy but have a lower precedence than the associated normal version. Precedence SHOULD be determined by lexicographic ASCII sort order. For instance: 1.0.0.alpha1 < 1.0.0.beta1 < 1.0.0.beta2 < 1.0.0.rc1 < 1.0.0.

Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications must be released as a new version.

Major version zero (0.y.z) is for initial development. Anything may change at any time. The public API should not be considered stable.

Version 1.0.0 defines the public API. The way in which the version number is incremented after this release is dependent on this public API and how it changes.

Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible bug fixes are introduced. A bug fix is defined as an internal change that fixes incorrect behavior.

Minor version Y (x.Y.z | x > 0) MUST be incremented if new, backwards compatible functionality is introduced to the public API. It MAY be incremented if substantial new functionality or improvements are introduced within the private code. It MAY include patch level changes.

Major version X (X.y.z | X > 0) MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY include minor and patch level changes.

Tagging Specification (SemVerTag)
This sub-specification SHOULD be used if you use a version control system (Git, Mercurial, SVN, etc) to store your code. Using this system allows automated tools to inspect your package and determine SemVer compliance and released versions.

When tagging releases in a version control system, the tag for a version MUST be “vX.Y.Z” e.g. “v3.1.0”.

The first revision that introduces SemVer compliance SHOULD be tagged “semver”. This allows pre-existing projects to assume compliance at any arbitrary point and for automated tools to discover this fact.

Why Use Semantic Versioning?
This is not a new or revolutionary idea. In fact, you probably do something close to this already. The problem is that “close” isn’t good enough. Without compliance to some sort of formal specification, version numbers are essentially useless for dependency management. By giving a name and clear definition to the above ideas, it becomes easy to communicate your intentions to the users of your software. Once these intentions are clear, flexible (but not too flexible) dependency specifications can finally be made.

A simple example will demonstrate how Semantic Versioning can make dependency hell a thing of the past. Consider a library called “Firetruck.” It requires a Semantically Versioned package named “Ladder.” At the time that Firetruck is created, Ladder is at version 3.1.0. Since Firetruck uses some functionality that was first introduced in 3.1.0, you can safely specify the Ladder dependency as greater than or equal to 3.1.0 but less than 4.0.0. Now, when Ladder version 3.1.1 and 3.2.0 become available, you can release them to your package management system and know that they will be compatible with existing dependent software.

As a responsible developer you will, of course, want to verify that any package upgrades function as advertised. The real world is a messy place; there’s nothing we can do about that but be vigilant. What you can do is let Semantic Versioning provide you with a sane way to release and upgrade packages without having to roll new versions of dependent packages, saving you time and hassle.

If all of this sounds desirable, all you need to do to start using Semantic Versioning is to declare that you are doing so and then follow the rules. Link to this website from your README so others know the rules and can benefit from them.

FAQ
How do I know when to release 1.0.0?
If your software is being used in production, it should probably already be 1.0.0. If you have a stable API on which users have come to depend, you should be 1.0.0. If you’re worrying a lot about backwards compatibility, you should probably already be 1.0.0.

Doesn’t this discourage rapid development and fast iteration?
Major version zero is all about rapid development. If you’re changing the API every day you should either still be in version 0.x.x or on a separate development branch working on the next major version.

If even the tiniest backwards incompatible changes to the public API require a major version bump, won’t I end up at version 42.0.0 very rapidly?
This is a question of responsible development and foresight. Incompatible changes should not be introduced lightly to software that has a lot of dependent code. The cost that must be incurred to upgrade can be significant. Having to bump major versions to release incompatible changes means you’ll think through the impact of your changes, and evaluate the cost/benefit ratio involved.

Documenting the entire public API is too much work!
It is your responsibility as a professional developer to properly document software that is intended for use by others. Managing software complexity is a hugely important part of keeping a project efficient, and that’s hard to do if nobody knows how to use your software, or what methods are safe to call. In the long run, Semantic Versioning, and the insistence on a well defined public API can keep everyone and everything running smoothly.

What do I do if I accidentally release a backwards incompatible change as a minor version?
As soon as you realize that you’ve broken the Semantic Versioning spec, fix the problem and release a new minor version that corrects the problem and restores backwards compatibility. Remember, it is unacceptable to modify versioned releases, even under this circumstance. If it’s appropriate, document the offending version and inform your users of the problem so that they are aware of the offending version.

What should I do if I update my own dependencies without changing the public API?
That would be considered compatible since it does not affect the public API. Software that explicitly depends on the same dependencies as your package should have their own dependency specifications and the author will notice any conflicts. Determining whether the change is a patch level or minor level modification depends on whether you updated your dependencies in order to fix a bug or introduce new functionality. I would usually expect additional code for the latter instance, in which case it’s obviously a minor level increment.

About
The Semantic Versioning specification is authored by Tom Preston-Werner, inventor of Gravatars and cofounder of GitHub.

If you’d like to leave feedback, please open an issue on GitHub.

License
Creative Commons ― CC BY 3.0 http://creativecommons.org/licenses/by/3.0/

---
## [GhostMaster69-dev/kernel_xiaomi_tulip](https://github.com/GhostMaster69-dev/kernel_xiaomi_tulip)@[db86d35b4b...](https://github.com/GhostMaster69-dev/kernel_xiaomi_tulip/commit/db86d35b4be5e47dd8d5147c65aff81ff490a1e7)
#### Thursday 2023-08-31 00:41:12 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>
Signed-off-by: GhostMaster69-dev <rathore6375@gmail.com>

---
## [SethLafuente/tgstation](https://github.com/SethLafuente/tgstation)@[fb4587b336...](https://github.com/SethLafuente/tgstation/commit/fb4587b3368ebb55e0cc10f8c650abcc26afa5d4)
#### Thursday 2023-08-31 00:46:18 by san7890

Cursed Slot Machine Fixes (#77989)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

A lot of these were stuff I did in response to reviews but apparently
didn't test extremely thoroughly. My bad.

* The proc for checking if the machine is in use is split out into its
own thing for clarity, and for potential reuse.
* The signal is no longer fucked up so you can actually get more than
one curse out of the slot machine as intended.
* Admin heals (and admin heals only) can remove the status effect. This
is just in case someone fucks up a variable when running an event and
wants to quickly heal some people while they varedit it to actually be a
proper event.
* Some nice code stuff while I was there, we don't need to be
typecasting to human anymore so it's nice to fix that.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Fixes are good.

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
fix: The Cursed Slot Machine should now actually give you more than one
pull.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[bbdacbd688...](https://github.com/mc776/freedoom/commit/bbdacbd6880a03c7419495733f9830b081e91f56)
#### Thursday 2023-08-31 00:47:36 by mc776

manual/dehacked: edit for clarity.

Some probably overambitious attempts to address #992.

[Note: I do not speak Spanish. Some longer translations are copied almost verbatim from DeepL output. Efforts have been made to parse the basic grammar of the output before committing anything but idiom is by no means guaranteed. If you find *anything* odd (that isn't obviously motivated by alliteration for the IDBEHOLD cheat), or any item/monster names already established that I'm not using here, please go ahead and fix it or tell someone who will! (Or tell me in the replies to this PR if you manage to catch it that soon)]

**General**

Rephrased the "Installing Freedoom" to make it a little easier on the kind of person who would actually need it: vanilla compatibility is also implied. FreeDM is also mentioned.

The armour example has been rewritten so we're only dealing with amounts the player will lose, instead of making the reader do internal arithmetic to track what went where.

The colorblind accessibility section for the keys is now just part of the description of the key pickups, and is also present in the Spanish manual. The keys are presented in the same order as they appear on the status bar and I've added a mnemonic that I found helpful.

Loading quicksaves is clarified: no need to die and menu is still available.

Miscellaneous rewordings to make things more to the point and avoid overexplaining.

Removed some references to "higher-level" and "lower-level" monsters. Someone who actually needs to be told this stuff might think this was an RPG thing.

Converted some CxMy references in the cheat code section.

**Ammo**

It's needlessly confusing to have "ammo" be used for both the pistol/minigun ammo and ammo generally. The gun pedant in me died a little inside, but the pickup messages now say "bullets" in line with both "bullets" and "balas" in the manuals.

(I've floated the idea of replacing the ammo box sprite with something without a label, but that's fairly low priority since everyone can see themselves touching the green square thing and only seeing one number go up.)

Clarified that backpacks don't stack their carrying capacity increase.

**Weapons**

Spanish weapon descriptions now bold the name as they are bolded in English.

Handgun description now uses the pickup sprite.

Pump shotgun's spread is clearly neither tight nor long for anyone who is playing at higher resolutions than vanilla 320x200. And it's not the main workhorse weapon in Phase 2.

Double-barreled shotgun isn't "twice" as powerful as the pump by any measurement. (Even its rate of shell consumption over time is more than double.) The much dimmer and unorthodoxically distributed red flash in #1085 can provide an excuse for the damage disparity for now.

SKAG no longer implies the ball does radius damage.

**Monsters**

The animal names are an evocative metaphor but the poetry is lost in doubling down on them in the descriptions when every single one is clearly taxonomically not that thing. ("Worm" was left untouched however since really that could mean any long wiggly thing.)

Matribite and hatchling image alt text should be capitalized for consistency; "hatchling" de-captalized in matribite description.

Painlord Spanish description seemed to imply it could only survive 5 missile *explosions* not direct hits, whereas the English is a bit clearer by using the same word for both painbros.

Large technospider and tripod explicitly said to be immune to explosions (but not SKAG).

---
## [bdazzle43/git](https://github.com/bdazzle43/git)@[8f23432b38...](https://github.com/bdazzle43/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Thursday 2023-08-31 00:47:49 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [jhnc-oss/poky](https://github.com/jhnc-oss/poky)@[89394ac832...](https://github.com/jhnc-oss/poky/commit/89394ac832e1a3f584271e3c855168c78b75e471)
#### Thursday 2023-08-31 01:02:12 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

(From OE-Core rev: 387b276c2d56d58c2a25d59984fcaaf9c88ac788)

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [timibot/simon_game](https://github.com/timibot/simon_game)@[32780b1535...](https://github.com/timibot/simon_game/commit/32780b15351238e72bdb09613eb0fb5629a7b607)
#### Thursday 2023-08-31 01:10:43 by Timileyin Olufisoye

Add files via upload

Key Features:

Kid-friendly Interface: A vibrant and intuitive interface designed with kids in mind, making it easy for them to play and enjoy.
Colourful Visuals: Bright and attractive colours that capture children's attention and make the game visually appealing.
Engaging Sounds: Fun and exciting sounds accompany each colour in the sequence, enhancing the overall gameplay experience.
Increasing Difficulty: As players progress, the sequences become progressively longer and more complex, providing an appropriate level of challenge.
Feel free to explore the code and assets in this repository to understand how I've implemented the game mechanics, user interface, and audio features. If you have any suggestions, bug reports, or contributions, please don't hesitate to open an issue or submit a pull request. Let's work together to enhance this educational and entertaining game for kids!

Get ready to test your memory, have some fun, and experience the joy of the Simon Kid game. Play, learn, and enjoy!"

Please note that this is just a sample GitHub repository description for the Simon Kid game. You can modify it based on the actual features, design, and goals of your game.

---
## [bakour1/shoppay-ecommerce](https://github.com/bakour1/shoppay-ecommerce)@[f7fa7f1c44...](https://github.com/bakour1/shoppay-ecommerce/commit/f7fa7f1c44074f2c840a3365108d28e9af46b2f5)
#### Thursday 2023-08-31 01:23:01 by bakour1

35. Sign up 4 Send email 1

So after using the activation token, the risk is to actually create the URL so we can go in sequence

and we call this URL.

We're going to have back six because we need to have first of all, it's going to be our, you know,

our website, which is going to be, for example, HTTP localhost, 3000.

So maybe we can go back, write it to the dot in V here and we have this next URL you can use.

That's what I prefer to have something that is called always the base URL because this will change when

you host your application.

The PCR will change for your application and it's not going to be local host 3000.

It could be like WW dot shop, a dot com or something like that.

So I'm just going to take this URL.

Also, we need to restart the server.

Okay.

And then go back to our code.

So this is the first thing.

So we're going to go to process dot E and V, and this is basic.

So that's the first thing.

Then we're going to go forward slash, which is going to be something like activate account or activate

and then forward slash.

We need to have the activation token right here like that.

This way and we can actually just resend the URL so you can see that here.

So if I go back, let me just see if it's runs.

Okay, so the server is running.

We can go back here and then let me try something like that and then send and this waits a little bit.

And I hope there is no problem right here.

Let me just make sure.

So open the console.

Okay.

Just been waiting to connect to the database.

Okay.

And we get this.

So that's the URL we sent to the email.

So the email is going to be like that.

He clicks in that you are.

So that means he's going to go to our websites and then to the activity page and we're going to have

this long activation token that we're just going to extract from that URL and get the user ID and then

make the email verified in the database from here.

If you go back, we're going to make, as I told you, the email verified from NULL to true.

And now if this is true, that means the user is activated.

So it's a pretty simple idea to make.

So the second the second thing is, which would be to have some sort of way to send the emails because

now we have the data ready, but we need the tool to send this and that's when it's going to use the

Gmail API from the Google Cloud console.

And also we're going to use node mail and some stuff.

So I've done this like before in my other course and some people say that after like two days or something,

the method stops working or like you can send email until you refresh and do the method again.

And I've been aware of that and I've looked into it and the problem was simply from the Express server.

So if you follow this with me, you're using next year's, I promise you it will never happen to you.

It doesn't even get revoked or nothing.

Like I created this, this application like five months ago and is still working till now.

So I promise you, if you follow me carefully and everything I do the same is not going to be a problem

at all.

It will always work no matter what.

And that's a pretty, pretty good thing because sending emails is a little bit complicated, you know?

So let's go back.

So the first thing is you've got to go to Google Cloud Console and you open the console.

I open that, so I'm here.

So if you are this is the first time here we show you log login and then you're going to it's going

to have some button to create a new project.

If you if you have another project before you can click right here and then click in your projects,

make sure in the Google Cloud console and right here is called this, for example, Shop or something

like that.

Okay, This is just for testing purposes.

I'm going to click Create and let's wait a little bit as it's still creating.

Okay.

You see right here this some process six times.

So you just got to be patient with it a little bit.

So it's been created.

I'm going to click select projects.

I know minutes.

So what you can do is simply click on the minority on the navigation.

You're going to have this API and services and then you're going to go to the oath consent screen and

you're going to click right here and then you're going to get redirected to this page.

So let me close this.

So right here, make sure you use Excel so it can be available for all users and then click create.

And then right here you need an app name.

So for me, I'm just going to call it both.

And then the support image should be the email that you use.

And I'm just having this for testing purposes.

You can have a logo for your application and then some some information for your application or like

your websites as you want.

So right here, everything as it is for the email address, just have the same one and then save and

continue.

And it's a lot of written right here.

So this is for scoops.

You really don't have to do anything right here.

Just save and continue.

And then for chase users, this is very important.

You need to add the email that you will send from.

So I'm just going to add it and then add like that.

Let me add.

Okay.

So it's been added right here in the table and then save and continue.

Kelly Sweet.

This is the summary.

Everything is right.

Then you can click back to Dashboard.

Dashboard was actually you can just go to credentials from here.

Just go to credentials from here.

Clicking here.

Okay?

Please, let's make this faster.

And right here, we're going to go to create credentials, and we're going to go to the oath.

Client ID.

And let's click on that and then we're going to define the application type, which is going to be a

web application, then the name of it, make sure to use the same name for you.

Have everything organized for us or like so you don't have any mix up.

So for the authorized JavaScript login, we need to add the local host 3000.

But if it's hosted, it should be the URL of your websites.

That's it.

So http make sure everything is right.

That's very important.

And then if you click again, you need to.

Okay, so it's been added automatically and then the otherwise redirects you.

Or else you need something like this, which is this URL that I'm going to leave for you, which is

this one.

So developers dot google dot com for slash playground and you're going to see why because we're going

to use the Gmail API, which is available right here for us from Google developers so that everything

seems fine.

Let me remove this from here and then I'm just going to click create.

And as we click Create, we get our first client's key and the secret key.

So these two are very important.

You can download them as JSON.

I'm just going to copy the first one, then go back to our application, go back to the DOT EMV and.

Okay, So we can have it.

Maybe.

So maybe right here.

And you can call this, for example, mailing service.

And I say we're going to do the same.

So it's going to be mailing service, mailing service, client ID, and we can also have the second

one, which is going to be client secrets.

So for the ID, that's the ID, don't use this because just I'm going to delete that later.

So make sure you use your own and go back again, get the secrets, go back and just paste it.

It sets also right here like that and you need to reset the server to you.

Really?

You don't really need that to do.

You really don't need to do that.

Sorry.

I don't know what's happened to my tank.

So then simply we're going to go back to the oath to playground and this is simply going to go to settings

here on the right and then make sure to click on use your own or credentials like this.

And then here we're going to need the client ID and the client secrets, which is simply what we have.

So the secret is already like copied so we can copy that and paste it.

Also, we need the client ID.

This is very important.

If you don't do this, it's going to keep refreshing the data and the ID and the secret is always going

to be changing.

Not the client's ID, but the client secrets.

Make sure to do that and click close.

Make sure that it's already registered there.

And then here we just simply got to go https four four slash and then mail dot google dot com and then

you're going to click authorize APIs to use the mail Google API.

So click on it and let's switch.

Okay.

So now we need to log in with the same, you know, the one that we had in the test user.

Make sure to log in with that and you click on and then we're going to click, continue to make sure

it's accepted, then continue to give the access.

Okay.

And simply everything is been done and we get the authorization code.

So right here we're just simply going to click exchange authorization for tokens like that.

And we get that.

So and we're going to get this refreshed token.

Sorry.

Let's go back right here to the second sip.

So the refresh token is all we need.

Don't worry.

This is this this message has expired.

Don't worry about it.

It's not going to create any problems, I promise you, because we're going to always going to get the

new token.

So just take this refresh token for now and just go back right here and then let me copy just the text.

That's what I need.

Client refresh.

Token, something like that, and paste that their mail in their mail in service client's refresh token

and go back.

Right.

And this is all actually what we need for now we have the dots are there and now actually we can go

we're going to go back to code and we actually change a few things.

So first thing that we need to do is actually just open the console and click right here and we need

to go here and add and then we're going to use Google APIs because we're going to use the node mailer.

But the node mailer is already been installed before.

If you don't if you don't have it, like if you go back to the package JSON, if you don't have rotate

the node mailer, make sure to install it, which I believe we installed it when we install next.

But if you don't make sure to install it and we tell this installs, let me go back right here and also

you have to refresh.

Okay, maybe, maybe not.

Now let's wait.

Okay.

Let's wait until it's installs.

---
## [Enchoseon/dotfiles](https://github.com/Enchoseon/dotfiles)@[c7174fe96d...](https://github.com/Enchoseon/dotfiles/commit/c7174fe96d2dbd42109c6fd6dadc79e51582fdca)
#### Thursday 2023-08-31 01:38:49 by Enchoseon

fix: Use Georgia font instead of Palatino

Mathpazo is deprecated and missing a ton of glyphs. Font fallback in
LaTeX SUCKS ASS, because it DOESN'T FUCKING EXIST.

So I just use Georgia now.

---
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[138bfd7042...](https://github.com/PlagueVonKarma/kep-hack/commit/138bfd704208776320e4cde5dea8edcefc61d271)
#### Thursday 2023-08-31 01:48:04 by Llinos Evans

Multiple bug fixes

* Moves the Mystery Box activation into Event Constants. This means that now, the Mystery Box activation is handled in the save, preventing some jank from happening when resetting.
* The "don't switch off the box yet" variable is now always unset after entering a map. Meltan itself allows the variable to keep being re-set, which is super handy. Now, whenever you enter and exit maps, it'll work properly.
* Flying, using an Escape Rope, and using Dig, all now unset the Mystery Box. If for some reason everything fucks up, this'll fix it.
* Fixed a text bug with the scientist in Celadon University.
* Fixed a menu alignment issue with the Vermilion Beauty.
* Attempted to fix the Battle Tent exit. Failed. This is a really, really bad bug, hopefully this gets sorted sometime.

---
## [a4lg/binutils-gdb](https://github.com/a4lg/binutils-gdb)@[05e1cac249...](https://github.com/a4lg/binutils-gdb/commit/05e1cac2496f842f70744dc5210fb3072ef32f3a)
#### Thursday 2023-08-31 03:25:33 by Andrew Burgess

gdb: fix vfork regressions when target-non-stop is off

It was pointed out on the mailing list[1] that after this commit:

  commit b1e0126ec56e099d753c20e91a9f8623aabd6b46
  Date:   Wed Jun 21 14:18:54 2023 +0100

      gdb: don't resume vfork parent while child is still running

the test gdb.base/vfork-follow-parent.exp now has some failures when
run with the native-gdbserver or native-extended-gdbserver boards:

  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to end of inferior 2 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: inferior 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: print unblock_parent = 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to break_parent (timeout)

The reason that these failures don't show up when run on the standard
unix board is that the test is only run in the default operating mode,
so for Linux this will be all-stop on top of non-stop.

If we adjust the test script so that it runs in the default mode and
with target-non-stop turned off, then we see the same failures on the
unix board.  This commit includes this change.

The way that the test is written means that it is not (currently)
possible to turn on non-stop mode and have the test still work, so
this commit does not do that.

I have also updated the test script so that the vfork child performs
an exec as well as the current exit.  Exec and exit are the two ways
in which a vfork child can release the vfork parent, so testing both
of these cases is useful I think.

In this test the inferior performs a vfork and the vfork-child
immediately exits.  The vfork-parent will wait for the vfork-child and
then blocks waiting for gdb.  Once gdb has released the vfork-parent,
the vfork-parent also exits.

In the test that fails, GDB sets 'detach-on-fork off' and then runs to
the vfork.  At this point the test tries to just "continue", but this
fails as the vfork-parent is still selected, and the parent can't
continue until the vfork-child completes.  As the vfork-child is
stopped by GDB the parent will never stop once resumed, so GDB refuses
to resume it.

The test script then sets 'schedule-multiple on' and once again
continues.  This time GDB, in theory, resumes both the parent and the
child, the parent will be held blocked by the kernel, but the child
will run until it exits, and which point GDB stops again, this time
with inferior 2, the newly exited vfork-child, selected.

What happens after this in the test script is irrelevant as far as
this failure is concerned.

To understand why the test started failing we should consider the
behaviour of four different cases:

  1. All-stop-on-non-stop before commit b1e0126ec56e,

  2. All-stop-on-non-stop after commit b1e0126ec56e,

  3. All-stop-on-all-stop before commit b1e0126ec56e, and

  4. All-stop-on-all-stop after commit b1e0126ec56e.

Only case #4 is failing after commit b1e0126ec56e, but I think the
other cases are interesting because, (a) they inform how we might fix
the regression, and (b) it turns out the behaviour of #2 changed too
with the commit, but the change was harmless.

For #1 All-stop-on-non-stop before commit b1e0126ec56e, what happens
is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-non-stop, every thread is resumed
    individually, so GDB tries to resume both the vfork-parent and the
    vfork-child, both of which succeed,

  3. The vfork-parent is held stopped by the kernel,

  4. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  5. At this point we might take two paths depending on which event
     GDB handles first, if GDB handles the VFORK_DONE first then:

     (a) As GDB is controlling both parent and child the VFORK_DONE is
         ignored (see handle_vfork_done), the vfork-parent will be
	 resumed,

     (b) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     Alternatively, if GDB selects the EXITED event first then:

     (c) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     (d) At some future time the user resumes the vfork-parent, at
         which point the VFORK_DONE is reported to GDB, however, GDB
	 is ignoring the VFORK_DONE (see handle_vfork_done), so the
	 parent is resumed.

For case #2, all-stop-on-non-stop after commit b1e0126ec56e, the
important difference is in step (2) above, now, instead of resuming
both the vfork-parent and the vfork-child, only the vfork-child is
resumed.  As such, when we get to step (5), only a single event, the
EXITED event is reported.

GDB handles the EXITED just as in (5)(c), then, later, when the user
resumes the vfork-parent, the VFORKED_DONE is immediately delivered
from the kernel, but this is ignored just as in (5)(d), and so,
though the pattern of when the vfork-parent is resumed changes, the
overall pattern of which events are reported and when, doesn't
actually change.  In fact, by not resuming the vfork-parent, the order
of events (in this test) is now deterministic, which (maybe?) is a
good thing.

If we now consider case #3, all-stop-on-all-stop before commit
b1e0126ec56e, then what happens is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-all-stop, the resume is passed down to the
     linux-nat target, the vfork-parent is the event thread, while the
     vfork-child is a sibling of the event thread,

  3. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this causes the vfork-child to be resumed.  Then
     in linux_nat_target::resume, the event thread, the vfork-parent,
     is also resumed.

  4. The vfork-parent is held stopped by the kernel,

  5. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  6. We are now in a situation identical to step (5) as for
     all-stop-on-non-stop above, GDB selects one of the events to
     handle, and whichever we select the user sees the correct
     behaviour.

And so, finally, we can consider #4, all-stop-on-all-stop after commit
b1e0126ec56e, this is the case that started failing.

We start out just like above, in proceed, the resume_ptid is
-1 (resume everything), due to schedule multiple being on.  And just
like above, due to the target being all-stop, we call
proceed_resume_thread_checked just once, for the current thread,
which, remember, is the vfork-parent thread.

The change in commit b1e0126ec56e was to avoid resuming a vfork-parent
thread, read the commit message for the justification for this change.

However, this means that GDB now rejects resuming the vfork-parent in
this case, which means that nothing gets resumed!  Obviously, if
nothing resumes, then nothing will ever stop, and so GDB appears to
hang.

I considered a couple of solutions which, in the end, I didn't go
with, these were:

  1. Move the vfork-parent check out of proceed_resume_thread_checked,
     and place it in proceed, but only on the all-stop-on-non-stop
     path, this should still address the issue seen in b1e0126ec56e,
     but would avoid the issue seen here.  I rejected this just
     because it didn't feel great to split the checks that exist in
     proceed_resume_thread_checked like this,

  2. Extend the condition in proceed_resume_thread_checked by adding a
     target_is_non_stop_p check.  This would have the same effect as
     idea 1, but leaves all the checks in the same place, which I
     think would be better, but this still just didn't feel right to
     me, and so,

What I noticed was that for the all-stop-on-non-stop, after commit
b1e0126ec56e, we only resumed the vfork-child, and this seems fine.
The vfork-parent isn't going to run anyway (the kernel will hold it
back), so if feels like we there's no harm in just waiting for the
child to complete, and then resuming the parent.

So then I started looking at follow_fork, which is called from the top
of proceed.  This function already has the task of switching between
the parent and child based on which the user wishes to follow.  So, I
wondered, could we use this to switch to the vfork-child in the case
that we are attached to both?

Turns out this is pretty simple to do.

Having done that, now the process is for all-stop-on-all-stop after
commit b1e0126ec56e, and with this new fix is:

  1. GDB calls proceed with the vfork-parent selected, but,

  2. In follow_fork, and follow_fork_inferior, GDB switches the
     selected thread to be that of the vfork-child,

  3. Back in proceed user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid still, but now,

  4. When GDB calls proceed_resume_thread_checked, the vfork-child is
     the current selected thread, this is not a vfork-parent, and so
     GDB allows the proceed to continue to the linux-nat target,

  5. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this does not resume the vfork-parent (because
     it is a vfork-parent), and then the vfork-child is resumed as
     this is the event thread,

At this point we are back in the same situation as for
all-stop-on-non-stop after commit b1e0126ec56e, that is, the
vfork-child is resumed, while the vfork-parent is held stopped by
GDB.

Eventually the vfork-child will exit or exec, at which point the
vfork-parent will be resumed.

[1] https://inbox.sourceware.org/gdb-patches/3e1e1db0-13d9-dd32-b4bb-051149ae6e76@simark.ca/

---
## [BeagleGaming1/cmss13](https://github.com/BeagleGaming1/cmss13)@[a95d6a3656...](https://github.com/BeagleGaming1/cmss13/commit/a95d6a3656ff6dd7ff220bb30259080c231d0f03)
#### Thursday 2023-08-31 03:30:49 by QuickLode

PMC Survivors can now use WY channel (#4234)

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

It allows PMC Survivors to utilize the WY channel.
# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->
Allowing PMC Survivors to communicate and thus RP better with WY assets
and within themselves. Team-based survivors should stick together
because lone wolves are not good for RP - I think we have seen a lot of
evidence from Chance's Claim survivors who, upon withdrawing, break
apart and cannot ever regroup due to communication impossibilities. From
an outsider's perspective, the impact of seeing a 'team' of survivors vs
a single survivor is a difference like night and day. With the former
being much more immersive and reflective of the professionalism a team
would have.

Also all that aside it was unintended for PMC Survivors to not have WY
comms - consider this a bugfix haha

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
fix: PMC Survivors now can use WY Comms.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [bhl-foss-mirrors/openembedded-core](https://github.com/bhl-foss-mirrors/openembedded-core)@[387b276c2d...](https://github.com/bhl-foss-mirrors/openembedded-core/commit/387b276c2d56d58c2a25d59984fcaaf9c88ac788)
#### Thursday 2023-08-31 03:38:13 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[f07cb3bd3b...](https://github.com/meemofcourse/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Thursday 2023-08-31 03:49:14 by Bjarl

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
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[8744738e59...](https://github.com/meemofcourse/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Thursday 2023-08-31 03:56:48 by Arturlang

Updates TGUI and adds bin folder for .bat scripts (#2011)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Updates TGUI and build tools and .vscode files to what TG has.
Does not actually update UI's, but does have fixes for a couple
including the join game UI's tabs not working.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not needing to have a local installation of yarn to run dev-mode is
nice.
Updating TGUI is a annoying chore that helps in the future when porting
more interfaces
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
code: Adds a bin folder with dev scripts, updates TGUI, .vscode folder
to what TG has.
fix: Fixes the input in the bottom right being white in darkmode, no
more unreadable text
fix: You can now use the tab buttons in the join ship menu.
qol: The outpost mission menu now looks a whole lot better
fix: The input bar no longer randomly becomes white and unreadable on
darkmode
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [girishsontakke/react](https://github.com/girishsontakke/react)@[ac1a16c67e...](https://github.com/girishsontakke/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Thursday 2023-08-31 05:52:42 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [Eveynowagain32/python3--m-pip-install--r-requirements.txt](https://github.com/Eveynowagain32/python3--m-pip-install--r-requirements.txt)@[d3326fcbd8...](https://github.com/Eveynowagain32/python3--m-pip-install--r-requirements.txt/commit/d3326fcbd8838dae1a5af9eefee163202be4c3a0)
#### Thursday 2023-08-31 07:34:19 by Eveynowagain32

Create SECURITY.md

Get me on email if you can help me out.

Se what’s possible to delete and delete the trash can like shit has done to me. 
See if anyone’s good enough to get past 2step authentication knowing that these are the emails that need to be removed from her access 
Lil_jolley_dawg_fans@yahoo.com
Ashlyndjolley27@live.com
Ashlyndjolley@gmail.com
Ashlyndjolley@icloud.com
Ashlyndmjolley@icloud.com
Has snapschat with phone number 7274579771
Facebook has same phone number with lil_jolley_dawg_fans@yahoo.com as email
Tictoc with the same
Verizon iCloud account and there’s plenary of sex tapes and other videos along with 1000s of pictures.
Is anyone able to get them out to her small town of Cochran GA to make her see how it feels when her personal life and info gets out to the world is like. She’s not a good mother and treats her kid like a dog. Even her father is in the process of taking her kid from her. She needs to get done to her like what she does to most the people around her.
It’s time to expose the real truth about the way she’s treated her own child

---
## [NithaIsTired/Bubbz](https://github.com/NithaIsTired/Bubbz)@[c6e0ba7516...](https://github.com/NithaIsTired/Bubbz/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Thursday 2023-08-31 09:21:01 by SkyratBot

[MIRROR] Drill module automatically disables if it's about to drill into gibtonite [MDB IGNORE] (#22990)

* Drill module automatically disables if it's about to drill into gibtonite (#77385)

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

* Drill module automatically disables if it's about to drill into gibtonite

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [tomaarsen/argilla](https://github.com/tomaarsen/argilla)@[2f2a113352...](https://github.com/tomaarsen/argilla/commit/2f2a11335289d660ce20aea11c9b969b0316fd2b)
#### Thursday 2023-08-31 09:45:12 by peppinob-ol

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
## [w3f/ring-vrf](https://github.com/w3f/ring-vrf)@[48b8507e28...](https://github.com/w3f/ring-vrf/commit/48b8507e2896e399172d7e3fe07fa63d2f9eea57)
#### Thursday 2023-08-31 10:22:05 by ¨Jeff

cargo test in the crate root fails without this

It worked in the individual crates before this, not sure why.
I bet this is due to ark_std::io being either std::io or the fork of it.

Awful lot of stupid shit in Rust is due to std::io not being core::io,
which afaik happens because of the missguided effort to add backtraces
everywhere.

---
## [DETrooper/Begotten-III](https://github.com/DETrooper/Begotten-III)@[7703af75e5...](https://github.com/DETrooper/Begotten-III/commit/7703af75e53a553382c332f820d3c9914a79cd8a)
#### Thursday 2023-08-31 11:51:47 by DETrooper

Faith gain rebalance, bug fixes.

- Faith gain changes:
	- Clan Reaver Gores now receive an amount of XP from selling slaves equivalent to the amount gained from a kill divided by 4.
	- Doubled the XP gain from dealing damage, dealing killing blows, drinking, eating, reading scripture, and copying scripture. This also affect sacrifice XP for the CoS and Gores.
	- Fixed the level modifier for kill XP gain capping at 30 instead of 40.
	- Gatekeepers now get increased residual XP gain at Gorewatch, which stacks on top of their inherent residual XP gain bonus.
	- Greatly increased the XP gain from killing thralls.
	- Increased XP gain from iron ore piles by a factor of 10, and from wood piles by a factor of 5.
	- Increased XP gain from the /electrocute command from 1 to 3.
	- Increased XP gain from successfully performing surgery from 15 to 100.
	- Instead of each player receiving 25 XP, the scrap factory now gives 200 XP per successful run, this is divided amongst the amount of people in the scrap factory, so completing it with less people will give more reward.
	- Medical items now give the correct amount of use XP when used on yourself instead of only when applied to other players, not just 5 XP (for example the survival pack now gives 50).
- Fixed an exploit where you could lower your melee weapon while holding the block key and still be blocking with it while lowered.
- 'Followed' trait changes:
	- Cursed characters will now wake when sleeping with night terrors, allowing them to sleep in short bursts but at a cost of sanity.
	- Lua error fix for maps that aren't rp_begotten3.
	- Slightly reduced the walking speed of the follower.
- Holding the block key while raising a melee weapon will now automatically block when the action bar is completed.
- Stamina plugin lua error fix.

---
## [MrSamu99/Shiptest](https://github.com/MrSamu99/Shiptest)@[7468161f7e...](https://github.com/MrSamu99/Shiptest/commit/7468161f7ec2180c7752cd2cc99b164522a3540a)
#### Thursday 2023-08-31 12:00:54 by FalloutFalcon

Trickwines! Again! (#1914)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Trickwines are a set of new reagents aimed at improving tribal/srm style
ships
The core concept are wines crafted out of mob drops and plants that
provide a buff on drinking and a debuff on throwing with bonus effects
against fauna
To facilitate the transfer of booze to target it also adds breakaway
flasks, 50u glass bottles that shatter violently on contact providing
extra throw force as well as a 25u gulp size which forces the user to
choose between buff or debuff
I plan on adding a fair few more Trickwines and the SRM Barrel Class
Brewer Vessel (SRM could really use one then 1 original ship) in later
prs to build on this concept
This HackMD will provide descriptions for the wines as well as a place
of information for all Trickwine-related content
https://hackmd.io/eUIddN2dS3mpeU1CThFGng

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Adds a fun new option for ships that lack proper chemistry and forces
them to choose which effect they actually want.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: FalloutFalcon
add: Trickwines
add: Breakaway flasks!
add: Basic Trickwine brewing equipment to the SRM glaive
imageadd: Sprites for breakaway flasks along with trick wine icons for
them!
code: Breakaway_flask_icon_state = null used for the same purpose as the
glass and shot glass versions
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

I DIDNT KNOW IF YOU RENAME A BRANCH IT CLOSES PRS RELATED TO IT?? I
THOUGHT IT JUST KNEW!!
3rd times a charm!

---------

Signed-off-by: FalloutFalcon <86381784+FalloutFalcon@users.noreply.github.com>
Signed-off-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [MrSamu99/Shiptest](https://github.com/MrSamu99/Shiptest)@[0e6f7fa646...](https://github.com/MrSamu99/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Thursday 2023-08-31 12:00:54 by Imaginos16

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
## [TwIStOy/neovide](https://github.com/TwIStOy/neovide)@[937decd850...](https://github.com/TwIStOy/neovide/commit/937decd850f2087a20e6488e42ffd1fafbec02e0)
#### Thursday 2023-08-31 12:28:31 by fredizzimo

fix: Improve nvim detection (#1946)

* Improve nvim detection:

Don't rely on the shell specific `exists", instead run `nvim -v`.
Additionally, if there's unexpected output, for example if your shell is
configured wrongly to output something when run in non-interactive mode,
it will tell you so, instead of failing with very strange errors later.

The `neovim-bin` argument has also been changed to always require the
binary to exist, instead if falling back to `nvim` as that's probably
not what the user wants. If `nevoim-bin` contains path separators the
binary will be tried directly, otherwise `which` will be used to find
the correct executable.

The which command has also been changed to always use the which crate
first to avoid shell specific issues (for example nushell).

The output is printed directly to stderr instead of the log, for a more
user friendly experience. Furthermore, the maybe disown call has been
moved so that the user actually has a chance to see the errors in the
console.

* fix(command): correct typos and clarify help message

* fix: preliminarly restore forking behavior

This however also loses possible error messages at startup about the
nvim binary not being found.

* codestyle: calm rustfmt

* fix(command): make error message about missing/errornous nvim visible

---------

Co-authored-by: MultisampledNight <contact@multisamplednight.com>

---
## [zaclegarssure/bevy](https://github.com/zaclegarssure/bevy)@[44f677a38a...](https://github.com/zaclegarssure/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Thursday 2023-08-31 12:48:59 by Sélène Amanita

Improve documentation relating to `Frustum` and `HalfSpace` (#9136)

# Objective

This PR's first aim is to fix a mistake in `HalfSpace`'s documentation.

When defining a `Frustum` myself in bevy_basic_portals, I realised that
the "distance" of the `HalfSpace` is not, as the current doc defines,
the "distance from the origin along the normal", but actually the
opposite of that.

See the example I gave in this PR.

This means one of two things:
1. The documentation about `HalfSpace` is wrong (it is either way
because of the `n.p + d > 0` formula given later anyway, which is how it
behaves, but in that formula `d` is indeed the opposite of the "distance
from the origin along the normal", otherwise it should be `n.p > d`)
2. The distance is supposed to be the "distance from the origin along
the normal" but when used in a Frustum it's used as the opposite, and it
is a mistake
3. Same as 2, but it is somehow intended

Since I think `HalfSpace` is only used for `Frustum`, and it's easier to
fix documentation than code, I assumed for this PR we're in case number
1. If we're in case number 3, the documentation of `Frustum` needs to
change, and in case number 2, the code needs to be fixed.

While I was at it, I also :
- Tried to improve the documentation for `Frustum`, `Aabb`, and
`VisibilitySystems`, among others, since they're all related to
`Frustum`.
- Fixed documentation about frustum culling not applying to 2d objects,
which is not true since https://github.com/bevyengine/bevy/pull/7885

## Remarks and questions

- What about a `HalfSpace` with an infinite distance, is it allowed and
does it represents the whole space? If so it should probably be
mentioned.
- I referenced the `update_frusta` system in
`bevy_render::view::visibility` directly instead of referencing its
system set, should I reference the system set instead? It's a bit
annoying since it's in 3 sets.
- `visibility_propagate` is not public for some reason, I think it
probably should be, but for now I only documented its system set, should
I make it public? I don't think that would count as a breaking change?
- Why is `Aabb` inserted by a system, with `NoFrustumCulling` as an
opt-out, instead of having it inserted by default in `PbrBundle` for
example and then the system calculating it when it's added? Is it
because there is still no way to have an optional component inside a
bundle?

---------

Co-authored-by: SpecificProtagonist <vincentjunge@posteo.net>
Co-authored-by: Alice Cecile <alice.i.cecile@gmail.com>

---
## [Martin-Moreira-de-jesus/orka](https://github.com/Martin-Moreira-de-jesus/orka)@[004088a21d...](https://github.com/Martin-Moreira-de-jesus/orka/commit/004088a21d17b7a042a0413b3d9d966fa1b36fe6)
#### Thursday 2023-08-31 13:08:52 by Martin Moreira de Jesus

feat(node-agent): implement node agent

# Node Agent Integration

## gRPC Worklod Service Server Integration

Add a wrapper for `containerd-client` lib (and `ctr` cli for creation) to create a container and run a workload.

The wrapper uses gRPC to communicate to the containerd socket. It reconnects to the socket before each request. This is done to avoid potential issues with resource management, isolation, and security and simplicity. It is also more fault tolerant.

This will however mean more resource usage, overhead, latency, potential socket exhaustion, etc.. This is a tradeoff we are willing to make for now since theses issues are not likely to be a problem in the near future.

The `ctr` cli was used to create the container because the `containerd-client` we did not manage to create a container with the `containerd-client` lib. It runs the command `ctr run -d <image> <container-id>`.

The `containerd-client` lib was also used to kill the container. We did however have an issue concerning an ambiguous type efinition. Indeed, the Workload Signal enum is ambiguous. It is not clear what signal STOP represents. For now we made the assumption that stop is SIGINT (2). Both Stop (SIGINT) and Kill (SIGKILL) signals are sent to the workload, then the workload is cleaned up.

**Note**: It seems Kuruyia has managed to prepare a rootfs and run a container, you can find it [here](https://github.com/Martin-Moreira-de-jesus/orka/blob/tmp/containerd-create-workload/node-agent/src/workload_manager/container/client.rs).

But to be honest going with `runc` or a container runtime made in rust might be an easier way to achieve our goals.

## gRPC Lifecycle Service Client and Status Update Service Client Integration

When the program starts, it connect to the scheduler and registers itself to it. If it fails, it will retry every 5 seconds. If it fails 3 times (can be modified in args or env see `node-agent/src/args.rs`), it will exit. It also starts the gRPC server.

If any of the two processes fail (gRPC of lifecycle), the server will shutdown and try to leave the cluster if needed.

Note: We would be glad to know how you think we managed the application's lifecycle. It was a first for us and it feels clunky.

## Cargo Workspaces

We added a `Cargo.toml` file at the root of the project to manage the dependencies of the different crates. Building, formatting and linting will now be easier.

However, we had an issue when building the node-agent. When you build the binary from the root of the project, request to the `containerd` socket fails saying it didn't find it. We did not manage to fix this issue. We did however manage to make it work only if build from the node-agent directory. We are not sure why this is happening.

## Misc

Add ide directory to gitignore.

## What's next

Use the network team's CNI implementation.

Signed-off-by: Martin Moreira de Jesus <martin.moreiradj@icloud.com>
Signed-off-by: Noé Tarbouriech <noe.tarbouriech@etu.umontpellier.fr>

fix(node-agent): remove duplicated import

feat(node-agent): add metrics from containers

feat(node-agent): add connection retries and refactor

fix(node-agent): update gitignore

feat(node-agent): implement status code return

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[0dd3e66aef...](https://github.com/MTandi/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Thursday 2023-08-31 13:46:08 by Vekter

Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation (#77860)

## About The Pull Request
Ports BeeStation/BeeStation-Hornet#3590. As it is right now, it's
trivial to set up a contraption using a conveyor belt and a shocked
grille to continuously shock monkey bodies. While this is very funny, it
also serves as a ghetto powersink that's hard to locate, easy to
replicate, and lasts effectively forever, since you can just keep
shocking the same bodies over and over again.

This doesn't completely remove the ability to make these, but it makes
them require at least a little maintenance and provides a way for them
to stop working even if the crew isn't able to locate them.

In an attempt to finally get people using the _actual_ powersink,
they'll show up a bit earlier in progression now. I'm not convinced 20
minutes is enough, but I don't want to put them in early enough that it
fucks with Engineering's ability to set things up at round start. We can
turn this down further if need be.

I'm also up for turning the TC requirement down, but 11 feels about
right for what they're supposed to do, so I'd prefer we try this first
and see how that works.

## Why It's Good For The Game
I'm all for goofy weird shit players have found, but there's an issue
with being able to do what an antag item is supposed to do but just
plain better. This shouldn't make creating these impossible or make them
unusable, but it'll require players to actively monitor them if they
want it to run for an extended period.

Additionally, we don't really see powersinks much anymore, and while
that might be more because powernets are kind of buggy and unreliable, I
think making them easier to get will make them show up a little more.

## Changelog
:cl: Vekter
balance: Grilles will now take 0-1 damage every time they shock
something.
balance: Powersinks are now available earlier in traitor progression.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [bendk/uniffi-rs](https://github.com/bendk/uniffi-rs)@[ae00abada1...](https://github.com/bendk/uniffi-rs/commit/ae00abada1d9a5ab6b9dc6b673722f9de426c5f3)
#### Thursday 2023-08-31 14:58:45 by Ben Dean-Kawamura

Store macro metadata in the cdylib file

The nice thing about this system is that the metadata is always bundled
together with the build output.  This makes it easier to ensure that the
generated scaffolding matches up with the dylib that it's going to be link to.
This avoids the work that `rebuild_metadata()` needed to do.  Metadata
is serialized with bincode to keep the binary size reasonable.

The downside is that we need to parse a dylib, which feels slightly
risky. However, it seems less risky overall to me, since we don't have
to worry about tracking the JSON files -- especially after fixing the
recent the sccache issue.  Also, extracting the symbol data with the
goblin crate is not that bad, see `macro_metadata/extract.rs` for how
it's done.

In order to use the macro metadata, you now need to specify `--cdylib
[path-to-library]` when running `uniffi-bindgen`.  This is annoying, but it
will be simpler once the proc-macros can handle all parts of the interface.
At that point, we can make `uniffi-bindgen` accept either a UDL path or a cdylib
path as it's positional arg.

I didn't add support for external bindings to pass in a cdylib path, since
adding an argument to that function would be a breaking change, then we would
need to do another breaking change to make the param `udl_or_cdylib_file`.  If
external bindings really want to, they can call
`uniffi_bindgen::interface::macro_metadata::add_to_ci` directly.

Added the `uniffi-bindgen dump-json` command that inputs a cdylib path and
prints the matadata as JSON.

I tested that `dump-json` works properly on the following targets:
  - x86_64-unknown-linux-gnu (ELF 64-bit)
  - i686-unknown-linux-gnu (ELF 32-bit)
  - x86_64-apple-darwin (Mach-O 64-bit)
  - x86_64-pc-windows-gnu (DLL 64-bit)
  - i686-pc-windows-gnu (DLL 32-bit)

This seems like good enough coverage to me, although there are a lot of other
systems that would be nice to test on.  The limiting factor was setting up the
cross-compilation toolchains on my machine.  Maybe we should add some more CI
platforms that just run macro-metadata-related tests.

Updated the testing code to pass the cydlib path, rather than the
directory that contains it.

Added an enum that covers all Metadata types.  This is what we serialize
in the cdylib.

---
## [madscientist42/meta-runit](https://github.com/madscientist42/meta-runit)@[8088709ae7...](https://github.com/madscientist42/meta-runit/commit/8088709ae7bf630fa014b56fc2722b4b33d44d04)
#### Thursday 2023-08-31 15:03:13 by Frank Earl

Additional cruft removal and tuning

- Don't want/need bootchart support in here for now.
  (We're going to eventually do boottrace which is
   more accurate and capable for bootcharting with
   trace charting tools.)
- Cleaned up hwclock service.  Don't need to stupidly
  fetch from RTC if the core-services actually DO this.
  Just go to sleep so we have the save ops hooked for
  down/restart and system shutdowns.  Finish is not
  as noisy.  Don't do silly things like announcing
  you're about to do it to the console- just do it
  and state you did it.
- Cleaned up core-services for 00-hwclock.  Use one
  msg line to convey this instead of two, which causes
  messy console output under some conditions.

---
## [404Dev-404/404Dev-404.github.io](https://github.com/404Dev-404/404Dev-404.github.io)@[613b30edd2...](https://github.com/404Dev-404/404Dev-404.github.io/commit/613b30edd2ff3ffe86c3a8566bd1ead68486f905)
#### Thursday 2023-08-31 15:18:00 by 404Dev-404

some long overdue maintenance

i should probably get a life

anyways here's a pretty detailed commit details because i deleted a shit ton of stuff so i removed the blogs folder because yes i changed the contrast and brightness of the favicon so it looks better at small sizes i got rid of Akzidenz Grotesk because to be blunt it is UGLY AS FUCK also i removed kidneystones.html because i have no fucking idea why i added it also i removed the part in the introduction on index.html that tells people what my favourite genre of music is because nobody gives a shit anyways so tbh i have no idea why i have this website when virtually nobody apart from me looks at it

---
## [plaguss/argilla](https://github.com/plaguss/argilla)@[028416a56e...](https://github.com/plaguss/argilla/commit/028416a56e1eb05defe9dffcd03de5d1744bdcf2)
#### Thursday 2023-08-31 16:04:31 by Natalia Elvira

Docs/feedback setfit tutorial (#3530)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

Adds a new tutorial on how to use SetFit to get zero-shot suggestions
for `Label` and `MultiLabel` questions in Feedback datasets.

Closes #3528 

**Type of change**

(Remember to title the PR according to the type of change)

- [x] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes.)

- [x] `sphinx-autobuild` (read [Developer
Documentation](https://docs.argilla.io/en/latest/community/developer_docs.html#building-the-documentation)
for more details)

**Checklist**

- [ ] I added relevant documentation
- [x] I followed the style guidelines of this project
- [x] I did a self-review of my code
- [x] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the `CHANGELOG.md` file (See
https://keepachangelog.com/)

---
## [sysfce2/MAMEUI](https://github.com/sysfce2/MAMEUI)@[dbb0909cba...](https://github.com/sysfce2/MAMEUI/commit/dbb0909cbab3f2094088a42687894e0e6053986b)
#### Thursday 2023-08-31 16:04:54 by wilbertpol

msx1_flop.xml: Added 105 working items, and replaced one item. (#11511)

* Replaced Konami Game Collection 3: Shooting Series (Japan) with a better dump. [file-hunter]

New working software list items (msx1_flop.xml)
-------------------------------
10 Programas Serie Oro (Spain) [file-hunter]
20 Programas Serie Oro (Spain) [file-hunter]
747 400b Flight Simulator (Europe, cracked) [file-hunter]
Alfabet en Deelsom (Netherlands) [file-hunter]
Alien Panic (Spain) [file-hunter]
Andon (Japan, hacked) [file-hunter]
Duad-MSX (Japan) [file-hunter]
Engels + Procenten (Netherlands) [file-hunter]
Fracta (Brazil) [file-hunter]
Graphos III (Brazil) [file-hunter]
Gruta de Maquine (Brazil)
The Iron Gauntz (Japan, prototype) [file-hunter]
Konami Game Collection 1: Action Series (Japan, alt) [file-hunter]
Konami Game Collection 4: Sports Series 2 (Japan, alt) [file-hunter]
Lettergrijper + Geld (Netherlands) [file-hunter]
Manuscript (United Kingdom) [file-hunter]
MSX Compilation 5 (Netherlands) [file-hunter]
MSX PageMaker DeLuxe (Brazil) [file-hunter]
Music Creator (Netherlands) [file-hunter]
Professional Data Retrieve (Brazil) [file-hunter]
Professional Paint (Brazil) [file-hunter]
Professional Publisher (Brazil, cracked) [file-hunter]
Rekenen tot 20 + Optellen en aftrekken tot 100 + Taalbedrijf (Netherlands) [file-hunter]
SF Zone 1999 (Japan) [file-hunter]
Simulador Profesional de Tenis (Spain) [file-hunter]
Super Procole (Japan) [file-hunter]
Super Procole 2 (Japan) [file-hunter]
Super Procole 3 (Japan) [file-hunter]
Supersellers 1 (Netherlands) [file-hunter]
Twin Hammer (Korea) [file-hunter]
The Wood (Spain) [file-hunter]
Woordmaker en Cijferend Vermenigvuldigen (Netherlands) [file-hunter]
Word Plus (Brazil) [file-hunter]
Wordstore+ (Netherlands) [file-hunter]
Zen (United Kingdom) [file-hunter]
3D Maze [Chalky]
666 - Uma Aventura Macabra [file-hunter]
8192 Story Tower [NAGI-P SOFT]
Baruko [file-hunter]
Blinky's Scary School [file-hunter]
Bounce Mania [MSXdev]
Burner Burst [file-hunter]
Buster Mystery [file-hunter]
City (Japan) [file-hunter]
Defence (v1.3) [MSXdev]
Galaxy Zone [aburi6800]
Ghosts'n Goblins (v1.1.0) [file-hunter]
Hibernated 1 - This Place is Death [file-hunter]
Hibernated 1 - Eight Feet Under [file-hunter]
JUMPER [NAGI-P SOFT]
Kame Graphics [file-hunter]
Kill Mice [MSXdev]
Las Aventuras de Rudolphine Rur (Spanish) [Dwalin]
Las Aventuras de Rudolphine Rur (Spanish, xmessage) [Dwalin]
Last War [NAGI-P SOFT]
Last War II [NAGI-P SOFT]
Logic (Russia) [file-hunter]
Mars [NAGI-P SOFT]
Mars II [NAGI-P SOFT]
May The Force Be With You [Cobinee]
Maze Chase [JLTurSan]
Micro Rocketz [MSXdev]
Mood Land [file-hunter]
Muhonmourn 3 (v1.1) [MSXdev]
Muhonmourn 3 (v1.1, with Ninja Tap support) [file-hunter]
Muhonmourn 3 (v1.0) [file-hunter]
Nibbles [file-hunter]
Oceano [file-hunter]
Paint-it (rev2) [file-hunter]
Paint-it (rev1) [file-hunter]
Paint-it [file-hunter]
Palhada City (Brazil) [file-hunter]
Penguin Catcher (v1.1) [MSXdev]
Penguin Catcher (v1.0) [file-hunter]
Pyramid Quest [Crappysoft]
Raftoid [PlattySoft]
Roger Dice (Spain) [oniric-factor]
Search for Mum (Netherlands) [file-hunter]
Sim City [file-hunter]
Storm Rescue [Concurso MSX-BASIC]
Stripgirl [file-hunter]
SubCommander (v1.02) [MSXdev]
SubCommander (older) [file-hunter]
Super Adventure [file-hunter]
The Tower of Gold [MSXdev]
UZIX (v1.0.0) [UZIX]
Wash Man (v2.8) [MSXdev]
Wash Man (v1.9) [file-hunter]
Wash Man (v1.5) [file-hunter]
Wash Man (v1.3) [file-hunter]
Wash Man (v1.2) [file-hunter]
Wash Man (v1.1) [file-hunter]
Wash Man (v1.0) [file-hunter]
Wired Shooting [Cobinee]
MSXMAS Demo [file-hunter]
Xadrama [file-hunter]
Xarchon [file-hunter]
XOR [Chalky]
XOR (older) [file-hunter]
Yellow Submarin [file-hunter]
Yobai [file-hunter]
Zero Gravity [file-hunter]
The zoBITRONics Inc [Hannu Töyrylä]
Zone TNT [MSXdev]
La Abadia del Crimen (Spain, alt) [file-hunter]

---
## [jktjkt/oopt-gnpy](https://github.com/jktjkt/oopt-gnpy)@[8f91279e7c...](https://github.com/jktjkt/oopt-gnpy/commit/8f91279e7cb4dd6e790ced92e13b4b03c9b99754)
#### Thursday 2023-08-31 16:26:27 by Jan Kundrát

YANG: Equipment Library

The first step in adding YANG description for GNPy's input is the
equipment library (`tip-photonic-equipment`). It contains data about all
defined EDFA and Fiber types. This is supposed to be functionally
equivalent to the `eqpt_config.json`, but the actual JSON structure is
different.

The core idea of this model is to describe capabilities of the
simulation engine as it exists, which means that the individual
choice/case statements mirror our different "simulation input
parameters". The user is not expected to do any augmentations of the
YANG model -- just describe the amplifiers, fiber, etc, with data. This
means that the user just *uses* the YANG model, which is unlike another
proposal that was floated around back in 2019 which used YANG-level
augmentations for the equipment library.

The pre-YANG code actually split stuff from `eqpt_config.json` into
additional JSON files for "fancy bits", such as the DGT LUT. That's
something that, IMHO, does not make sense when we're willing to ship
with machine-validation of the complete input set. So instead of
deferring to another JSON file for the NF-/gain-ripple/DGT, let's move
everything in-line into the input data. This has one obvious downside in
making the amplifier data a bit too verbose. There were several options:

- Ignore the human-friendliness and push everything into the amplifier
description. This is nice and self-contained, but the data are going to
be very, very long, and the majority of the WG was worried that it would
make human editing too difficult.

- Move everything to a side-loaded JSON file. This option separates out
some numerical parameters from the equipment library, and therefore
splits the configuration into two places. One of these places would be
exempt from the YANG validation, and loaded via unspecified means.
That's a no-go.

- Put stuff into a YANG model, but use one level of indirection between
the amplifier description and the numerical data.

This took us quite some time to decide, but ultimately on 2020-09-01 we
decided that the numbers that we have been shipping are *probably*
specific to a given EDFA model they were measured on. The actual *slope*
of the DGT looks very similar between, say, the Juniper/Lumentum
measurements and the data from Orange, but the multiplication factor is
different. So the outcome was that we will probably have to ship with
some sane default, *but* any measurements done by the user will apply
only to a specific amplifier model. The YANG model reflects that, and it
uses per-type lists. They are now indexed by frequency as agreed on the
2020-09-01 coders call.

In the real world, some "common fiber types" are well-defined by ITU,
such as the SSMF. Esther tried to model this via a set of identities and
YANG `identityref`s. I think that there's no disadvantage in shipping
these data as a default content of the YANG-formatted datastore,
similarly to how the equipment library used to be structured prior to
this patch. Once again, I'm following the pattern where the user can
change any *data* without augmenting the YANG model. The only reason for
editing/augmenting the (equipment) YANG model should be changes in our
simulation *engine*, such as when adding different input parameters for
NF calculations, or adding Raman amplification, etc.

The amplifier model has been reworked a bit. I've reduced the number of
available "simulation parameters" to a reasonable minimum as suggested
by Jean-Luc (cf. issue #227):

- a polynomial NF model
- a simplified model for operators with NF_min and NF_max
- a dual-stage amplifier comprising two individual sub-amplifiers that
  are each any of the above
- a faux-Raman
- three OpenROADM-specific models

In terms of correspondence to the previous code, the "polynomial NF" is
used for current `advanced_model` (which uses yet another external JSON
file) and the `fixed_gain` model. The simplified, min-max-NF is what
Jean-Luc called "operator model"; the wording is a compromise of various
suggestions done via GitHub. The OpenROADM models are, unfortunately,
magic, especially the preamp+booster simulation. But it reflects how
it's been implemented in GNPy.

The values which are stored in the YANG-formatted JSON files have
different units than what was stored in the legacy JSON files. We are
now using the "customary units", such as ps/km, instead of s/m. This is
largely a matter of taste, but the technical reason behind this is that
YANG only defines a decimal64 data type with a limited precision, and we
were running out of fraction-digits for certain parameters where the SI
representation is "too low" (the pmd-coefficient is one example).

Other "subtle" changes have been done as well, such as clarifying that
the amplifier's band boundaries refer to the edges of the passband and
not the central frequencies, etc.

Change-Id: I449d66e952834011b3ec476023c9cc353dfca5c0

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d93dfbc35c...](https://github.com/tgstation/tgstation/commit/d93dfbc35c4b86435f9b436160e0d6c0670a8e28)
#### Thursday 2023-08-31 16:31:35 by Sealed101

Adds Summon Cheese (#77778)

oh apparently this is my 100th PR on tg, which is weird because github
reports 99 total, and i made at least one to the old voidcrew repo, and
filtering tg prs by my name still shows 99. weird. here's to 100 more i
guess?

<sub>could have been better if it was a get, jhonflupwliiard watch ur
back 🔫 </sub>

## About The Pull Request

Adds a new spell granter book to the Wizard's Den - Summon Cheese, which
grants the spell by the same name, which summons 9 heads of cheese.
That's about it, I think.

## Why It's Good For The Game

Wizards are a hungry bunch, so why can't they just summon food? They can
even share, if they'd like, since the notion of a friendly wizard still
exists

<details>
<summary>... </summary>

alright fine
i'm slightly malding over not getting the 77777 get so no more
roleplaying in the pr body

Wizard Grand Ritual now has a hidden goal of sacrificing 50 cheese
wheels. Sacrificing a cheese wheel is done with invoking the grand rune,
and each invocation/pulse of the rune will whisk away more cheese until
all cheese on the rune is taken by whichever entity lurks in the other
realm. The sacrifice will be hinted at in an _ancient parchment_ which
will be on the bookshelf (when i add it lmao) alongside the spell book.

Meeting this cheese goal will lock the wizard's grand finale rune and
grand finale effect to special ones. The cheese rune is mostly identical
to the normal grand rune, barring the custom sprites/animations.
The cheese finale consists of the wizard getting permanent Levitation
(nogravity + free space movement), a 0.5 modifier(reducing incoming
damage in half) to every damage type, a comically strong mood buff and
**The Wabbajack**(separate sprite pending) - a juiced up chaos staff
which can fire a lot more projectiles than a normal one can (it will get
more, I may even make a few just for it).
Everybody else (including any invader antags) gets hallucinations, 175
brain damage and a comically strong mood debuff, as well as a vendetta
against the wizard. If the victim was already suffering from
hallucinations from a trauma (including the quirk), they are instead
healed.

if you didn't catch the obvious reference, this entire shtick is a
tribute to Sheogorath. the rune makes use of daedric script, and most of
the catchphrases are a direct quotation of the Daedric Prince of
Madness, so if any of those things can get us in trouble somehow, let me
know. i will be sad but i will comply.

This shtick is intended as an easter egg, really, so I wasn't really
planning on expanding the wizard grand finale into heretic paths thing
or whatever.

Oh, and finale grand runes now allow the wizard to select the effect
even if it's time-gated. If it is, you just won't be able to invoke it
until the time comes. The rune will tell you how much time is left until
you can invoke it. And grand finale runes with a finale effect selected
also glow in the color of their effect. I also think I fixed some step
of the grand rune animation not triggering but I'm not sure.

<details><summary>Some rune animations (some are subject to
change)</summary>


![rune_cheese_activate](https://github.com/tgstation/tgstation/assets/75863639/62ae184d-b6fc-4883-a169-4d8ca7636b40)


![rune_cheese_flash_2](https://github.com/tgstation/tgstation/assets/75863639/619545c8-3c55-4264-bfa4-d40067ef7406)


</details> 

## Why It's Great For The Game

it's funny

</details> 

## Changelog


:cl: Sealed101, EBAT_BASUHA for spritework
add: Wizard's Den now has a book of Summon Cheese in the Studies Room
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [conrad-mo/website](https://github.com/conrad-mo/website)@[a1ce85f846...](https://github.com/conrad-mo/website/commit/a1ce85f846742052dcc3230e2c50be69f939ea00)
#### Thursday 2023-08-31 16:38:10 by conrad-mo

holy fuck, i hate react i finally got routing to work oml i hate this so much, im so thankful im only using react for websites and NOTHING else

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[d1afd66508...](https://github.com/Sealed101/tgstation/commit/d1afd66508ed3474ca6179d54294742bef531419)
#### Thursday 2023-08-31 16:49:39 by san7890

The Curse Of The Slot Machine - Now Clone-less (#77841)

## About The Pull Request

Hey there,

I think it's commonly held that clone damage sucks and is overused. One
of the last places where it was in slot machine code as a type of
"immutable" damage that would cause you to die if you didn't leave and
get medical attention. It had a lot of silliness and I'm not sure if a
lot of it was meant to work the way it was, but here we are.

So, what's the changes?

* The Cursed Slot Machine will give you a status effect that will
"curse" you with repeated damage. After five curses, you get gibbed
(similar to the old behavior of the machine). Each curse has it's own
change to the status effect, with a lot of depth included. Let me know
if the fluff messages about the status effect change sucks, I think it's
neat though.
* A person with the curse will smoke. I wanted this to look a bit more
"steamy" or grey, but I think it's a decent way of communicating that
shit is fucked up with that dude.
* You also get a branded wound after your first failure at the slot
machine. Ouchers. Should get it looked at by a doctor.
* We also throw a nice screen alert and all of that jazz.
* I also cleaned up all of the code relating to the slot machine
(including a stupid double and), and did some tinkering with the status
effects framework to get the desired effect I wanted. I hope you enjoy
it as much as I did making it. We use cooldowns and stuff between slot
machine pulls.
* If _anyone_ wins on the slot machine, all curses/brands are lifted.
Lucky jackpot!
* A lot of the stuff in this code has a lot of vars that might not be
modified codewise in case admins still want to jank with this for
events.
## Why It's Good For The Game

Clone damage stinks, and I don't really like it as a way to subvert the
whole "oh you can't use legion cores to get your way". It's a cursed
slot machine, and it should do long term damage so that even if you
expend all of the resources on the station, it might all be for naught.
It's a horrible price to pay in your search for that d20. I think the
negative side effects are pretty OK as far as balance, earlier
iterations of this concept had you die _way_ too fast.

All in all, it's just way more of an interesting interaction than "you
take damage and then go to medbay and then come back in the hopes of
gambling a d20".
## Changelog
:cl:
add: The Lavaland Cursed Slot Machine of Greed suddenly seems a lot more
sinister...
refactor: Instead of taking clone damage from the cursed slot machine,
you now get a status effect with a number of curses associated with it.
There's some interesting florid language associated with the status
effect as a nicety until your eventual gibbing from chasing that prize.
/:cl:

I remain undecided if I should keep the curse limit uncapped (but have
the damages increase rapidly after the 5-curse threshold), so I left it
as the `gib()` from the old code. Let me know your thoughts, but I
really don't like the thought that getting the fabled d20 is easy.

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[67e97b7877...](https://github.com/jlsnow301/tgstation/commit/67e97b787740fd2a5017fd3c66c4f52a0a511a5a)
#### Thursday 2023-08-31 16:53:51 by RikuTheKiller

Light eater is now indestructible (#77903)

## About The Pull Request

This means a nightmare going into an emagged recycler will no longer be
fucked by their lack of a light eater.
Oh yeah, also moved the ACID_PROOF flag to the correct bitflag.
## Why It's Good For The Game

Bugfix good, you're not supposed to be able to delete an external limb
generated by an internal one, such as implants and such. Pretty sure
reimplanting the heart would make the light eater reappear, too, but
that's night impossible to get done as a nightmare.
## Changelog
:cl:
fix: Light eaters can no longer be eaten by their higher-grade brothers,
the trash eaters. (recyclers)
/:cl:

---
## [AleksanderBodurri/angular](https://github.com/AleksanderBodurri/angular)@[acd59ad037...](https://github.com/AleksanderBodurri/angular/commit/acd59ad0371a19838813cfc934a73fa3cc357602)
#### Thursday 2023-08-31 17:03:44 by Ward Bell

docs: Migrate Observables guides & code examples to standalone (#51516)

None of the guide pages mentions ngModules. Only `observables-in-angular` needed conversion to Standalone.

However, some of the guide pages reflect old versions of RxJS, including signatures that are no longer valid. These have been corrected.

More significantly, *the existing guide is pretty bad at explaining RxJS and its usage*. It was written (by me I think) in the very early days of Angular and Angular RxJS instruction. I've taught numerous "RxJS in Angular" classes since and learned from that experience what does and does not work with students.

There was neither the time nor the charter to completely overhaul this guide. But this commit attempts to remove what flops with students and to bring the teaching closer to what seems more effectively. I hope reviewers agree that my revisions are an improvement.

**Revised Overview**

The overview doc, `observables.md`, had a few errors (ex: `next` is NOT REQUIRED) and deprecated patterns (you now must pass the Observer object to `subscribe`).

More importantly, it was wildly overcomplicated and scary, especially when it got into multi-casting.

Moved the multi-casting section to  "RxJS Library" and rewrote it (with working example) for simplicity and context.

I made other changes in an effort to make this an overview that is  more comprehensive and more clear. I paid particular attention to the "Basic usage and terms" section.

Finally, I relocated the "Naming conventions for observables" section here from `rx-library`. This is the section that describes the dollar-sign convention. It made more sense for it to be here.

**Revised "RxJS Library" page and code**

*RxJS no longer supports chaining* and hasn't for a very long time. Removed note in `rx-library.md` that suggested you could use operator chaining.

The RxJS `pipe` discussion in the "Operators" section was just weird. Almost no one calls the `pipe` function. We certainly should *start* there. We should start with how people actually use operators - by adding them to the argument list of the `Observable.pipe()` method.

I kept the original `pipe` function example but subordinated it in a "callout". Most readers will (and should) ignore it.

`Subject` is a *critically important RxJS mechanism for creating custom observables*. It was completely missing from the list of observable creators on this guide page. So I added it to the "Observable creation functions" section of the guide and wrote an accompanying `MessageService` code sample (see the new `rx-library/app/` folder).

The `MessageService` is a pretty common pattern in Angular apps - far more common than creating an observable from a counter or an event, two of the creation patterns currently on this page.

This new section also afforded an opportunity to show how RxJS helps with building loosely coupled applications. We will soon be talking about Signals. Many will wonder whether and when they should still use RxJS.

At least a partial answer is that RxJS is really good at progressively combining and enhancing streams of data as they cross component boundaries. Of course you can pass signals around; but they are not as rich in transformers as RxJS. This is where RxJS shines.

**Revised "Comparing observables"**

The Promises section in `comparing-observables.md` had many errors and misleading remarks.

The comparison of error handling was especially egregious; the code example for that was nonsense.

The "Chain" sub-section was really about transforming values. It also failed to demonstrate chaining promise `.then`s.

Reworked these sub-sections and improved the code samples to match.

PR Close #51516

---
## [Sancaknr/Sancak](https://github.com/Sancaknr/Sancak)@[07dde91a34...](https://github.com/Sancaknr/Sancak/commit/07dde91a34e723bea26bdd139fd667d989a6f9a5)
#### Thursday 2023-08-31 17:33:42 by Sancaknr

"Tweet Counter: Version 0.4 Update!"

🎉 New Update - Transform Your Tweeting Interface! 🎉

📢 Introducing the latest rendition of your beloved Tweet Counter application, now equipped with a revamped interface that takes your tweeting experience to new heights. Prepare to indulge in smoother interactions, refined aesthetics, and unparalleled functionality. Let's delve into the exciting refinements:

🎨 Redesigned User Interface: Get ready to be captivated by the sleek and intuitive new look of the Tweet Counter. With carefully curated fonts, pleasing color schemes, and streamlined elements, your tweeting journey will be both delightful and efficient.

🌐 Enhanced User Interaction: We've meticulously reimagined the way you interact with the application. From tweet entry to account login, every step has been fine-tuned to ensure a seamless and comfortable experience, making your tweeting adventure even more enjoyable.

📜 Comprehensive Tweet History: Your past tweets are now elegantly displayed in a dedicated section. Effortlessly scroll through your tweet history and witness the progression of your thoughts over time. It's a visual journey through your digital expressions.

🚀 Smoother Authentication: Say goodbye to hassle. The authentication process has been optimized for simplicity and speed. Logging in is now a breeze, allowing you to dive into the world of tweeting without delay.

🎙️ Express Yourself with Ease: Crafting tweets has never been this effortless. The tweet entry field is now conveniently accessible, enabling you to share your thoughts, ideas, and experiences with the world in an instant.

Stay tuned as we continue to elevate your tweeting experience with ongoing updates. Happy tweeting and enjoy the new and improved interface! 🚀📱

---
## [t895/yuzu](https://github.com/t895/yuzu)@[8e703e08df...](https://github.com/t895/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Thursday 2023-08-31 17:39:50 by comex

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
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[7d600bf36a...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/7d600bf36a691d4be27e852eed0106a1564d7aee)
#### Thursday 2023-08-31 18:18:49 by TheObserver-sys

More plants, new chems, new carpet generation techniques, plantcell buff, and the drills now have a GPS signal! (#5912)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/4d3a51f1-7d2b-4d56-9971-7f33d76610f1)

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/608ba481-2499-4bf0-a25c-cc503655bf7d)

New! Exciting! Things! YEEHAW!

Okay, hype aside, this adds two plants from Main -- the third, and most
powerful sister of the ambrosia family, and the better grass, carpet!

Ambrosia Gaia: A difficult plant to keep alive, being very vulnerable to
weeds, pests, and any amount of toxins in the tray, as well as voracious
when it comes to nutrients and water. In exchange, the plant produces a
very, very powerful healing agent: Earthsblood.

For the cost of your brain, your ability to gauge how injured you are,
and when it works again, the ability to see clearly, your body will be
repaired in miraculous ways! (4/4 Brute Burn, 4 tox, 10 oxy, 2 clone).
The current damage is set to 1 brain damage, which means you'd need to
use a fair amount to die -- but not treating it will debilitate you.
Overdoses at over 15u.
In the future, it will also be a usable plant chem -- but let's not
worry about that until after I scream at the entirety of botany.

Carpet: Grass mutation, pull it free, get free carpet tile. OR! Mix with
the items in the image to create New! and Exciting! colors. Mix 2 parts
liquefied carpet, with 1 part plasticide, and you too can redecorate
like the best of them*

*some colors still have to be bought from cargo.
*someone help me make it a sprayable so we don't need solidification
please....

This also buffs a certain aspect of xenobotany -- plant cells.
For reasons only known to god.. and I think he left baycode a long time
ago, plant cells could only ever reach a maximum rating of 2000. As a
large cell. So you can't stuff it in a gun. This is dogshit --
especially for the challenge of reaching 200 potency on a plant, a feat
that is nearly impossible. The math has been buffed, so if you even
manage to get to 100, you at least have a Rating 20000 cell, something
you can run a department off of if straits are dire.

The final, and more QoL thing than straight buff or new thing: GPS
Drills
Drills now have a GPS signal. Never lose a pesky drill again!*
*you did remember your GPS device, yeah?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Give a xenobotanist something worth working to in normal gameplay, and
they'll endeavour to do so while waiting for the fun plants to come back
to station. Don't, and watch them just kinda wilt waist deep in glow
berries, gold apples, and ice chilis. Also, it's easier than you think
to lose a giant drill when you've stepped away from the planet for a
long while. only to come back later. Putting GPSes in them just means
you can continue the work again.

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
add: Two new plants, Ambrosia Gaia, and Carpet
add: New chems! Earthsblood, trading the mind for the body, and Carpet
and it's many mixtures, capable of being solidified later!
qol: Mining Drills now have an integral GPS. It took strength of a
million men to not make the tag DRILLD0 as a terrible joke.
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
Co-authored-by: Captain277 <agentraven16@gmail.com>

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[4155eecdac...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/4155eecdacd658fd0509f41e3bf8a7c48b13102c)
#### Thursday 2023-08-31 18:18:49 by silicons

Completely changes how DCS types works (#5911)

DCS now registers based on its registered type, as opposed to at every
subtype.
Dupe mode is no longer considered realistically usable unless
if-and-only-if all var pre-setting behavior is considered - which is not
the case on the majority of citrp-made components outside of
/datum/component/radioactive

## Why?

Components are a generic way to attach datums to things.
The common practices included:
- No getcomponent
- Use signals for all interaction
- Don't subtype, set vars on initialization

This resulted in components, while being quite stable, being also quite
rigid, in my opinion. Given we don't use components for the same things,
and probably never will, I think it's better for us to get the
optimizations from not supporting what's honestly behavior that we
shouldn't rely on in the first place - if something needs to be applied
multiple times (e.g. radiation) it should rely on the old behavior and
this new system still allows it. If it doesn't, the author should either
not be adding the component multiple times, or **making** their
component functional under this system. InheritComponent still has all
the tools necessary to properly do component inheritance, it's just now
we default to all components only being considered the same if it's the
exact subtype - which from what I could see, is also the previous case
(as if you add a subtype, uh, bad shit's going to happen if the base
type is registered but not the subtype anyways!)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[fc836593a5...](https://github.com/tgstation/tgstation/commit/fc836593a51771fc6c06adfa28f81d3cd134a501)
#### Thursday 2023-08-31 18:42:29 by GuillaumePrata

Makes fanny packs be silent, others can't see what you put in or take out. (#78010)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Just like the syndicate toolbox and a handful of other items.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This is a blatantly stealth antag buff.

Pockets are 2 silent storage slots everyone has, so it is not adding
anything that antags didn't have access already.
But going from 2 to 5 small items can help a lot, also belts are a lot
smoother to use with their shortcut keys.

Love stealth antags, hate murderboners, gonna help my stealth boys not
be valid hunted because someone checked their chat logs from 10 minutes
ago and read that X player put Y contraband in their bag.

Or people that have some contraband names highlighted on chat... but no
one does that right.... right?
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

:cl:Guillaume Prata
balance: Fanny packs are now silent, no one will get a chat message
about what you put in or take out.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Aki Ito <11748095+ExcessiveUseOfCobblestone@users.noreply.github.com>

---
## [momentum-mod/website](https://github.com/momentum-mod/website)@[3784467551...](https://github.com/momentum-mod/website/commit/378446755159a8fbc6ecd876250c991776e4eb2f)
#### Thursday 2023-08-31 18:50:08 by tsa96

chore(back-e2e): split maps.e2e-spec.ts

I'M SORRY FOR DUMPING THIS IN THE MIDDLE OF THIS PR BUT THIS FILE IS NUKING MY EDITOR.
So, Jest sucks. You're forced to run tests on a per-file basis, and we have to set up a Nest instance for at once.
If we ran Nest in the global test env, we can't access the instance in code, which we need to override providers in some cases.
So each separate file slows down CI so I try to avoid too many. Since this file is so monstrous and slowing down WebStorm,
I'm just splitting it in two. There's *probably* a better way of doing it, but honestly, Jest makes it difficult.
I'd rather not mess with it RN, so just doing this.

---
## [simplymathematics/wasp_SE_course](https://github.com/simplymathematics/wasp_SE_course)@[1e7bd40b88...](https://github.com/simplymathematics/wasp_SE_course/commit/1e7bd40b88ad5a950fcb50f92f89013507241e74)
#### Thursday 2023-08-31 18:56:50 by simplymathematics

Sorry this is late. I definitely put a lot of thought into following our discussion at the beginning of the summer. I just noted a submission deadline of midnight in my calendar. Please forgive that.

---
## [axodotdev/cargo-dist](https://github.com/axodotdev/cargo-dist)@[f9c62e71e4...](https://github.com/axodotdev/cargo-dist/commit/f9c62e71e4ffd2249f03625dc55f8068e79fc557)
#### Thursday 2023-08-31 19:16:10 by Aria Beingessner

feat(msi): add msi installer

The "msi" installer vendors the binaries into a windows msi.
msi generation is implemented by using cargo-wix as a library,
which in turn handles generating templates and invoking WiX (v3).

The resulting msi's are unsigned -- signing will be handled by a followup,
as changes to OV certs mean that "proper" signing is now very complicated
and messy.

This implementation has some notable details:

WiX requires an xml-based template called main.wxs for each msi it generates.
This template includes things like the application name, version, publisher,
EULA, embedded files, and so on.

cargo-wix's default workflow is for you to run `cargo wix init` once to generate
that file and check it in. At this point the developer is free to hand-edit
the template to suit their needs. We like this idea, `cargo dist generate-ci`
is based on that same premise!

But our experience with generate-ci has also taught us that this approach
is really prone to frustrating desyncs. The main.wxs bakes in several pieces
of information that were sourced from your Cargo.toml. As a result, if you
ever change your Cargo.toml, you now need to remember to apply the same
change to your main.wxs, or rerun `cargo wix init` and potentially clobber
any hand-edits you made.

As such, for the first draft of this feature we've opted for a more aggressive
solution: whenever you run `cargo dist init` we will invoke `cargo wix init`
to force the template to have up to date contents, essentially forbidding
hand-edits.

[Not Yet Implemented] When you run `cargo dist build` or `cargo dist plan`
we will also error out if we detect that `cargo wix init` would modify
main.wxs.

[Not Yet Implemented] A new allow-dirty config is added to cargo-dist to
prevent `init` from regenerating main.wxs or checking that it's up to date,
essentially restoring the original design of cargo-wix. We believe this
should be opt-in because most people ideally shouldn't want to do hand-edits,
and desyncing is a very nasty footgun.

`cargo dist init` will also modify your Cargo.tomls to add
`[package.metadata.wix]` with two generated GUIDs (if those GUIDs aren't
already present).

These GUIDs are used by windows to identify that two different msis actually
intend to refer to the same application and install dir. As such, each release
of your app needs to use the same GUID.

cargo-wix bakes these GUIDs into your main.wxs, and critically it defaults to
generating new random ones every time you run init (because constantly
re-initing wasn't part of the design).

By persisting the GUIDs to your package's Cargo.toml, we unlock the ability
to freely regenerate main.wxs whenever we want.

The logic to select the packages that need msi's in `cargo dist init` is
currently a temporary hack that doesn't properly check all config. We should
add a proper `generate-wix` command that does proper config/package using
the DistGraph.

We invoke cargo-wix to actually build the msi's in a kind of hacky way.
cargo-wix was built to assume it would be in charge of building the binaries
that get embedded in the msi, but cargo-dist wants to be in charge of that.

cargo-wix does have a --no-build option, but it still assumes the binaries
will be in the cargo target dir, and emits a warning that this is happening
(which will confuse our users).

I did some upstream work to add a --profile flag so that it would understand
we built with the 'dist' profile, but after working through the details I've
realized that cargo-dist really just wants to give cargo-wix a temp dir that
the binaries (and any other files to include) have been copied into.

The issue is that multiple Cargo builds in series can clobber eachother's binaries,
so if you want to do multiple builds and potentially combine the results you
really need to be actively copying the binaries out of the target dir between
each build. This notably happens if you build multiple feature variations of
an application (which cargo-dist doesn't yet support but plans to).

cargo-dist is therefore architected to just run all the builds in series and
copy the binaries to different temp dirs for each bundling method, notifying
the bundling method its temp dir is ready only once all dependencies are
fulfilled.

I briefly considered replicating the target dir structure in the temp-dir
so that we could just tell cargo-dist the temp-dir *is* the target dir but
this still wouldn't get rid of the warning so really I should just work with
upstream on a proper API for this.

As a temporary hack we just assume target clobbering isn't a problem and
have cargo-wix read the binaries out of the real target dir, while still
passing --no-build.

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[5abafddaea...](https://github.com/MrMelbert/tgstation/commit/5abafddaea2373b5e367a7ac658d6cab6499b70c)
#### Thursday 2023-08-31 19:26:38 by carlarctg

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
## [Blothorn/RP-1](https://github.com/Blothorn/RP-1)@[8c4ebb0442...](https://github.com/Blothorn/RP-1/commit/8c4ebb0442a632aa66d786e0e87ebfe19af1289f)
#### Thursday 2023-08-31 19:43:50 by Ian Sturdy

X-Planes overhaul

As much as I like planes, I have a few frustrations with the X-Planes contracts/program--some going back to legacy, some new with PLC.
- It's somewhat tedious. Despite not having any unlimited repeatables, a full completion of the program involves about 30 flights--even ignoring the levels of SS High that require High-speed Flight or above. This is quite a lot of flight time, and much of it non-AFK game time for the many people who haven't fully automated these flights. (Also, the high number of cooldown contracts combined with crew training requirements can require a lot of bookkeeping.)
- There isn't a lot of variety. All missions are basically either "hold X speed with a jet" or "reach X altitude with a rocket plane"--the only deviation being the rocketplane development contracts that somewhat constrain the flight path to reach an altitude. It's possible, and in PLC quite attractive, to complete the program with two planes, each optimized for a single mission profile, and one of which repeats the exact same kOS script over a dozen times.
- The funding fits awkwardly within PLC. Now that crewed orbit is split, no program comes close to the time and tech range--the first handful of missions can be easily completed in the first year, while the last requires post-orbital tech. This means that from start to finish the opportunity cost of the program slots increase considerably, and thus its funding is only competitive for a fairly narrow range of start dates and speeds--most of which require painful compromises. (And I think it's actually more expensive to run than an SR program--almost all of the tech required is dead-end tech you could otherwise skip without issue, and hiring a pilot in the first year is a significant expense. Meanwhile, since you need to complete an SR program to advance and both overlap heavily in tech and LC requirements, you save very little from only taking one.

I've attempted to address this from a few directions. I think these are largely separable if you think some but not others are good ideas; I've lumped them in this PR so I don't have to also balance them separately.
- Split the program into an early program (roughly covering the X-1 through X-3 missions) and a late program (X-15). This allows people to start planes late while still seeing X-15 funding while it's still vaguely competitive. (Particularly attractive to double SR/heavy sat playthroughs where you need to wait for either two admin upgrades or finishing both SR programs to take early.) I considered further splitting early into 1-point jet and rocket programs to appease people who are bored of jets, but I think that would make taking at least one of the plane programs at the start to fill out the fifth program slot much too attractive.
- Reduce the number of missions--this cuts the Supersonic and 80km Altitude milestones, reduces the repetitions of most optional missions by 30-50% by increasing the gap between contracts, and bumps up some reputation rewards to partially make up for the reduced count.
- Add some new missions. The Stratospheric Research missions are modeled on the cover story for the U-2, and I think provide an interesting design challenge that doesn't consist of optimizing the wave-drag coefficient. The hypersonic research missions are modeled on the high-speed low-altitude X-15 flights, and probably don't change plane design much but at least provide something different to do.

Aside from contract testing, I've done a partial career taking X-planes at the start. I still think that's suboptimal; hiring an astronaut or two and adding at least one point of research that doesn't benefit sounding rockets can't compete with the synergy between the SR programs. However, the reduction in confidence for the smaller program and better first-year funding feels a lot better than the current slow start. I think the situation will be somewhat better for careers taking it alongside sounding rockets after an admin upgrade. I expect the X-15 program is somewhat undertuned--if you take it in late '52 it's respectable money through 53 and 54, but after FO it blocks the targeted/comms satellite programs that are even more lucrative despite being single-slot programs--but I haven't tested that stage enough to dare push it higher.

---
## [powerhome/playbook](https://github.com/powerhome/playbook)@[205619a0e9...](https://github.com/powerhome/playbook/commit/205619a0e9ce327306acf84735c13ea4ed356c7b)
#### Thursday 2023-08-31 20:17:05 by Gavin Huang

[PLAY-972] dateTime Bug Fixes (#2716)

**What does this PR do?**
- Corrects incorrect weekdays by removing the `getUTC` functions
- In the DB, for example, the date was August 15, 2023 01:30:00. The
`toWeekday` function formatted the date from UTC to Local Time, but
`getUTCDay()` went back to grab the UTC date. This issue was evident
with late-day appointments. Therefore, we should not be using any
`getUTC` functions.
- Corrects two bugs Jason found within`fromNow()`:
  - Remove period from "years ago"
- Fix miscalculation of "milliseconds in a month" - this was causing any
past date with a timestamp of "x months ago" to have a random number
- Updates `toLocaleString()` to use `en-US`
- Hayden R. reported he was receiving `undefined NaN`. Upon
investigation, certain locales (like en-GB [Great Britain]), can't use
functions like `getMonth()` so it was returning `undefined NaN`. We
default to `en-US` because internationalization and formatting does not
matter since Playbook formats dates in a specific way.

**Screenshots**

**Before**

![Before](https://github.com/powerhome/playbook/assets/47684670/07303adf-f2eb-4d7b-a0ba-ad82cf7f945c)

**After**

![After](https://github.com/powerhome/playbook/assets/47684670/8696283f-d4b4-4ab3-9302-c9651af672cd)

**How to test?** Steps to confirm the desired behavior:
1. The weekday problem was experienced in the [Sales
Books](https://nitro.powerhrg.com/sales/reps/11115/sales_books?rep_filter%5Bdate%5D%5Byear%5D=2023&rep_filter%5Bdate%5D%5Bmonth%5D=8).
In Miguel Picart's (or any RC), select their "Books" tab, select "All
Appointments", find any place that has 2+ appointments the same day -
they should be correct.
2. For Hayden's bug, impersonate Hayden and in his user profile ensure
that the address is showing as his European address. Go to a Runway
ticket and check the reviewers, he should not see `undefined NaN`. We
should also ensure that Hayden can see a date after the release.

#### Checklist:
- [X] **LABELS** Add a label: `enhancement`, `bug`, `improvement`, `new
kit`, `deprecated`, or `breaking`. See [Changelog &
Labels](https://github.com/powerhome/playbook/wiki/Changelog-&-Labels)
for details.
- [X] **DEPLOY** I have added the `milano` label to show I'm ready for a
review.
- [ ] **TESTS** I have added test coverage to my code.

---------

Co-authored-by: Nida Ghuman <nidaqg@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[0055338d73...](https://github.com/TaleStation/TaleStation/commit/0055338d73af8b638f4f33b37ed7b06906ca4de5)
#### Thursday 2023-08-31 20:57:32 by TaleStationBot

[MIRROR] [MDB IGNORE] Makes fanny packs be silent, others can't see what you put in or take out. (#7580)

Original PR: https://github.com/tgstation/tgstation/pull/78010
-----

## About The Pull Request
Just like the syndicate toolbox and a handful of other items.
## Why It's Good For The Game
This is a blatantly stealth antag buff.

Pockets are 2 silent storage slots everyone has, so it is not adding
anything that antags didn't have access already.
But going from 2 to 5 small items can help a lot, also belts are a lot
smoother to use with their shortcut keys.

Love stealth antags, hate murderboners, gonna help my stealth boys not
be valid hunted because someone checked their chat logs from 10 minutes
ago and read that X player put Y contraband in their bag.

Or people that have some contraband names highlighted on chat... but no
one does that right.... right?
## Changelog
:cl:Guillaume Prata
balance: Fanny packs are now silent, no one will get a chat message
about what you put in or take out.
/:cl:

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Aki Ito <11748095+ExcessiveUseOfCobblestone@users.noreply.github.com>

---
## [Reco201/Skyrat-tg](https://github.com/Reco201/Skyrat-tg)@[d5655c3c55...](https://github.com/Reco201/Skyrat-tg/commit/d5655c3c55fab0f4450659947fad1a40043893dc)
#### Thursday 2023-08-31 21:09:41 by SkyratBot

[MIRROR] Adds Summon Simians & Buffs/QoLs Mutate [MDB IGNORE] (#22970)

* Adds Summon Simians & Buffs/QoLs Mutate (#77196)

## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races.

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

* Adds Summon Simians & Buffs/QoLs Mutate

* Updates our modular file to take this into account (I hate that this exists)

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [Reco201/Skyrat-tg](https://github.com/Reco201/Skyrat-tg)@[3782e4b710...](https://github.com/Reco201/Skyrat-tg/commit/3782e4b71098d12588696d9263f2ee8748caf9bf)
#### Thursday 2023-08-31 21:09:41 by Bloop

[MISSED MIRROR] Martian Food: A Taste of the Red Planet (#75988) (#23013)

Martian Food: A Taste of the Red Planet (#75988)

## About The Pull Request
Adds a selection of new foods and drinks based around Mars.
More information on Mars can be found here:
https://github.com/tgstation/common_core/blob/master/Interesting%20Planets/Human%20Space/The%20Sol%20System.md
To summarise for the general audience, Mars is a vital colony of the
Terran Federation, having been primarily settled (at least originally)
by Cybersun Industries to harvest its lucrative supplies of plasma, the
second largest in human space behind Lavaland. This has given Mars a
diverse culture evolving from the mostly East Asian colonists, and their
food reflects this.

Thanks to Melbert for their work on the soup portion of this PR.

The food:
Martian cuisine draws upon the culinary traditions of East Asia, and
adds in fusion cuisine from the later colonists. Expect classics such as
ramen, curry, noodles and donburi, as well as new takes on the formula
like the Croque-Martienne, Peanut Butter Ice Cream Mochi, and the
Kitzushi- chilli cheese and rice inside a fried tofu casing. Oh, and
lots of pineapple. The Martians love pineapple:

![image](https://github.com/tgstation/tgstation/assets/58124831/c9ae33a1-e03a-4f94-8ce0-8ad124e88e8d)
Also included are some foods for Ethereals, which may or may not be
hinting at something I've got planned...

The drinks:
Four new base drinks make their way to the game, bringing with them a
host of new cocktails: enjoy new ventures in bartending with Coconut
Rum, Shochu/Soju, Yuyake (our favourite legally-distinct melon liqueur),
and Mars' favourite alcoholic beverage, rice beer. Each is available in
the dispenser, as well as bottles in the booze-o-mat:

![image](https://github.com/tgstation/tgstation/assets/58124831/914a6e2a-7ef5-4791-ae31-d08fa9211083)

The recipes:
To make your (and the wiki editors) lives easier, please find below the
recipes for both foods and drinks:
Food: https://hackmd.io/@EOBGames/BkVFU0w9Y
Drinks: https://hackmd.io/@EOBGames/rJ1OhnsJ2
## Why It's Good For The Game
Another lot of variety for the chef and bartender, as well as continuing
the work started with lizard and moth food in getting Common Core into
the game in a tangible and fun way.
## Changelog
:cl: EOBGames, MrMelbert
add: Mars celebrates the 250th anniversary of the Martian Concession
this year, and this has brought Martian cuisine to new heights of
popularity. Find a new selection of Martian foods and drinks available
in your crafting menu today!
/:cl:

---------

Co-authored-by: EOBGames <58124831+EOBGames@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Sancaknr/Sancak](https://github.com/Sancaknr/Sancak)@[a05269c3e2...](https://github.com/Sancaknr/Sancak/commit/a05269c3e2cb234332c1f02d34cf6f6939961665)
#### Thursday 2023-08-31 21:42:38 by Sancaknr

"Tweet Counter: Version 0.5 Update!"

🎉 New Update - Elevate Your Tweeting Interface! 🎉

📢 Presenting the latest iteration of your cherished Tweet Counter application, now infused with an even more refined and interactive interface. Get ready for a journey filled with smoother interactions, stunning aesthetics, and exceptional functionality. Let's delve into the captivating enhancements:

🖌️ Redesigned User Interface: Immerse yourself in the beauty of the Tweet Counter's new look. With carefully chosen fonts, harmonious color schemes, and seamlessly integrated elements, your tweeting experience will be as visually appealing as it is functional.

🌟 Streamlined Username Validation: We've taken username validation to the next level. Your username now needs to start with a single '@' symbol, followed by at least one alphanumeric character. Receive instant feedback on your username's validity with clear and informative messages.

🔒 Robust Password Requirements: Strengthen your security with a robust password. We've set the bar higher with password requirements, including a minimum length of 8 characters, at least one letter, and one digit. Ensure your account is fortified against unauthorized access.

🗨️ Comprehensive Tweet Insights: Dive into your tweet history like never before. The updated interface displays your past tweets elegantly, allowing you to reflect on your thoughts and memories. Scroll through your digital expressions and relive your tweeting journey.

🚀 Effortless Interaction: From logging in to composing tweets, every aspect of interaction has been meticulously optimized for ease. Experience a fluid and intuitive flow as you navigate through the application's features.

Stay tuned as we continue to enhance your tweeting adventure with ongoing updates. Happy tweeting and enjoy the fresh and upgraded interface! 🚀📱

---

