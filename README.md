## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-23](docs/good-messages/2022/2022-10-23.md)


1,809,013 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,809,013 were push events containing 2,523,626 commit messages that amount to 148,586,834 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [hanami/controller](https://github.com/hanami/controller)@[9c123ecdd5...](https://github.com/hanami/controller/commit/9c123ecdd5152c942fa3fb6b7b5359a569943531)
#### Sunday 2022-10-23 00:03:38 by Tim Riley

Reenable MIME specs and check both `Accept` and `Content-Type` headers checks via `accept` (#396)

## Background

The way our `accept` macro has worked has taken over time has taken a few different shapes.

- In 1.3.x it worked on the `Accept` header only ([see here for code](https://github.com/hanami/controller/blob/2496ac797237d7320b96048a3c9e3fbebb00532c/lib/hanami/action/mime.rb#L168-L172)) and returned a 406 response for non-matching types.
- However, 1.3.x _also_ had a `content_type` macro that operated on the `Content-Type` header ([see code](https://github.com/hanami/controller/blob/2496ac797237d7320b96048a3c9e3fbebb00532c/lib/hanami/action/mime.rb#L198-L204)) and returned a 415 response for non-matching types.
- In the very earliest phase of 2.0 development, when @jodosha was completely overhauling the shape of hanami-controller, we removed the `content_type` macro and left the `accept` macro only (in [this commit](https://github.com/hanami/controller/commit/85e927a694998e5ebfcbad216d7bdec4109b6806), which is rather large). The `accept` macro and its behaviour were left largely unchanged at this point.
- Then not too long after, we changed the `accept` macro to no longer operate on the `Accept` header and instead look at `Content-Type` only, and return a 415 response for all non-matching types (see [this PR](https://github.com/hanami/controller/pull/265), addressing [this issue](https://github.com/hanami/controller/issues/257))

## Shortcomings 

I ran into some trouble with this early 2.0-phase implementation, because it meant that if you put `accept :json` into a base action class (e.g. for every action class within an API service to inherit from), then it would reject _any_ request without a `Content-Type: application/json` header.

Requiring a `Content-Type` header like this would make sense for POST, PUT, PATCH requests, that is, any kind of request that contains a request body and needs to describe its content type.

However, `GET` and other requests without bodies are likely _not_ to have `Content-Type` headers. These requests would more likely have an `Accept` header only.

## Changes

I believe that when an action contains `accept :json`, then it should be able to successfully handle a request with only an `Accept: application/json` header, and no `Content-Type`. It should also handle weighted `Accept` headers too, like `text/html, application/xhtml+xml, application/xml;q=0.9`.

This PR changes the way we enforce the accepted formats configured with `accept`. It:

- Checks the `Accept` header first. If it is present, it will check if any any of the header's MIME types are acceptable per the configured `accepted_formats`. If none are acceptable, then the request will be a 406 error.
- If the `Accept` is not present, it then checks `Content-Type`. If this header is present, but checks to see if the Content-Type MIME type is accepted able per the configured `accepted_formats`. If it is not acceptable, then the request will be a 415 error.
  - If the `Content-Type` header is not present, then it will substitute this with the MIME type for the `default_request_format`, if configured.
- Lastly, if there is no `Accept`, no `Content-Type`, no `default_request_format`, then the request is accepted regardless, with the idea here being that the client has no care or opinion about the format they want, and our Action class can return whatever content it likes in its response.

I believe this strikes a balance that should satisfy the spread of real-world requests. It captures the spirit of _both_ the original `accept` and `content_type` macros while ensuring we still keep the slimmer API surface area of the `accept` macro only.

Certainly if this were implemented earlier, I could have avoided hacking in a workaround inside the app in which I discovered this issue.

---
## [OpenNMS/opennms](https://github.com/OpenNMS/opennms)@[0f0debc173...](https://github.com/OpenNMS/opennms/commit/0f0debc173b80950d2664c484f2f44c773ec25ec)
#### Sunday 2022-10-23 01:08:46 by DJ Gregor

Make the progress bar play well with systemd.

Unfortunately, we won't see the updates directly out of
'sudo systemctl restart opennms'. To see status during OpenNMS
restarts use 'journalctl -f -u opennms' to monitor separately and/or
something like 'watch -n 1 systemctl status opennms' (I personally
like seeing the systemd view with the latter).

We do a few things in the systemd case:
1. If the 'opennms' script isn't running in terminal with a tty, the
   terminal.columns property isn't passed and Invoker.java treats the
   terminal as non-interactive. We use this to tweak our output in a
   few ways to work well with systemd:
   - Use '\n' instead of '\r' for progress updates, to avoid
     'systemd status' from just reporting very unhelpful
     '[2.9K blob data]' messages.
   - Use ProgressBarStyle.ASCII only in non-interactive mode, and use
     the default style in interactive mode.
   - Disable continuous update in non-interactive mode because it makes
     the status output needlessly verbose. systemd alreday monitors
     whether the process is still alive, so the only value continous
     updates provide is to see the estimated remaining time update,
     which feels a lot less useful given the amount of 'systemd status'
     noise it generates.
2. Some moderate tweaks to 'opennms' when the progress bar is enabled
   and we are running in systemd:
   - Redirect opennms output to output.log just like we do normally
     when running outside of systemd.
   - Run tail(1) with "--pid $pid" to that tail(1) will die when the
     OpenNMS process exits. Without this systemd will still think the
     service is active. Also add a check in systemd mode to make sure
     that tail(1) supports "--pid", and if not, disable the progress
     bar. See the notes at the end of the commit for what happens if
     we don't do this. BTW, we should probably eventually switch to
     use Type=notify in systemd instead of Type=forking that we have
     now. See
   - When stopping, don't run another tail(1) process because the one
     from the start will still be running in the CGroup.
3. Pass "-s" to the stop command in the systemd opennms.service unit
   file to support the last item above to avoid an extra tail(1).
4. Tweak our invocations of tail(1) to use "-F -n 0" so we work with
   more tail(1) variants (in particular, the one in Ubuntu).
5. Increase our progressbar.log rotation size from 10 kB to 100 kB
   because tail(1) on Ubuntu spits out a log message or two when the
   file is rotated and these messages can't be disabled. :(

Also, quiet down tput(1) when there is no tty present.

=== Okay, so about this systemd forking business and tail --pid ===

Currently in systemd mode and with these changes, we have an
interesting and slightly problematic process structure:

     CGroup: /system.slice/opennms.service
             ├─29777 bash /usr/share/opennms/bin/opennms -s start
             ├─29778 tail -F -n 0 --pid 29777 /var/log/opennms/progressbar.log
             └─29779 /usr/lib/jvm/java-11-openjdk-amd64/bin/java ... -jar /usr/share/opennms/lib/opennms_bootstrap.jar start

(Note: the only difference without this change would be the lack of the
tail process).

Note that we have the bash process for 'opennms -s start' that sticks
around after OpenNMS has been started. The 'opennms' script runs
'runCmd "${CMD[@]}" &' and 'runCmd' is a shell function not an external
command (although inside 'runCmd' it does call an external command).
Since that shell function is what is backgrounded, a copy of the shell
sticks around to run the command (in the foreground in that shell
function to make things even more confusing, so I think this happens in
all cases of running OpenNMS using this script).

You'll also notice that it is the PID for that bash process which is
passed to 'tail --pid' (29777 in the above sample) *not* the OpenNMS
process itself (29779 in this case). Luckily, when OpenNMS exits, the
shell should exit, as well.

If we don't use "tail --pid" and OpenNMS exits abruptly (without
'opennms stop' being called **by systemd**), we end up with just the
tail(1) process running in the CGroup:

     CGroup: /system.slice/opennms.service
             └─163703 tail -F -n 0 /var/log/opennms/progressbar.log

And systemd thinks things are still happy, which is **bad**:

     Active: active (running) since Sat 2022-10-22 02:37:54 UTC; 5min ago

So, that's why the startup script is picky about 'tail --pid' being
there in systemd mode with the progress bar, and if it isn't, the
progress bar feature is disabled.

As an FYI, here are two other things I noticed:

Oct 23 00:46:18 dgregor-vm-perf systemd[1]: opennms.service: Can't open PID file /run/opennms/opennms.pid (yet?) after start: Operation not permitted
Oct 23 00:46:19 dgregor-vm-perf systemd[1]: opennms.service: Supervising process 37802 which is not our child. We'll most likely not notice when it exits.

I think the latter message about supervising is related to using the
forking configuration. Both of these seem to happen with or without
the changes in this commit.

---
## [OpenNMS/opennms](https://github.com/OpenNMS/opennms)@[910297e9df...](https://github.com/OpenNMS/opennms/commit/910297e9df40efae7964c4900b8c4e3317c27fe9)
#### Sunday 2022-10-23 01:25:03 by DJ Gregor

Make the progress bar play well with systemd.

Unfortunately, we won't see the updates directly out of
'sudo systemctl restart opennms'. To see status during OpenNMS
restarts use 'journalctl -f -u opennms' to monitor separately and/or
something like 'watch -n 1 systemctl status opennms' (I personally
like seeing the systemd view with the latter).

We do a few things in the systemd case:
1. If the 'opennms' script isn't running in terminal with a tty, the
   terminal.columns property isn't passed and Invoker.java treats the
   terminal as non-interactive. We use this to tweak our output in a
   few ways to work well with systemd:
   - Use '\n' instead of '\r' for progress updates, to avoid
     'systemd status' from just reporting very unhelpful
     '[2.9K blob data]' messages.
   - Use ProgressBarStyle.ASCII only in non-interactive mode, and use
     the default style in interactive mode.
   - Disable continuous update in non-interactive mode because it makes
     the status output needlessly verbose. systemd alreday monitors
     whether the process is still alive, so the only value continous
     updates provide is to see the estimated remaining time update,
     which feels a lot less useful given the amount of 'systemd status'
     noise it generates.
2. Some moderate tweaks to 'opennms' when the progress bar is enabled
   and we are running in systemd:
   - Redirect opennms output to output.log just like we do normally
     when running outside of systemd.
   - Run tail(1) with "--pid $pid" to that tail(1) will die when the
     OpenNMS process exits. Without this systemd will still think the
     service is active. Also add a check in systemd mode to make sure
     that tail(1) supports "--pid", and if not, disable the progress
     bar. See the notes at the end of the commit for what happens if
     we don't do this.
   - When stopping, don't run another tail(1) process because the one
     from the start will still be running in the CGroup.
3. Pass "-s" to the stop command in the systemd opennms.service unit
   file to support the last item above to avoid an extra tail(1).
4. Tweak our invocations of tail(1) to use "-F -n 0" so we work with
   more tail(1) variants (in particular, the one in Ubuntu).
5. Increase our progressbar.log rotation size from 10 kB to 100 kB
   because tail(1) on Ubuntu spits out a log message or two when the
   file is rotated and these messages can't be disabled. :(

Also, quiet down tput(1) when there is no tty present.

=== Okay, so about this systemd forking business and tail --pid ===

Currently in systemd mode and with these changes, we have an
interesting and slightly problematic process structure:

     CGroup: /system.slice/opennms.service
             ├─29777 bash /usr/share/opennms/bin/opennms -s start
             ├─29778 tail -F -n 0 --pid 29777 /var/log/opennms/progressbar.log
             └─29779 /usr/lib/jvm/java-11-openjdk-amd64/bin/java ... -jar /usr/share/opennms/lib/opennms_bootstrap.jar start

(Note: the only difference without this change would be the lack of the
tail process).

Note that we have the bash process for 'opennms -s start' that sticks
around after OpenNMS has been started. The 'opennms' script runs
'runCmd "${CMD[@]}" &' and 'runCmd' is a shell function not an external
command (although inside 'runCmd' it does call an external command).
Since that shell function is what is backgrounded, a copy of the shell
sticks around to run the command (in the foreground in that shell
function to make things even more confusing, so I think this happens in
all cases of running OpenNMS using this script).

You'll also notice that it is the PID for that bash process which is
passed to 'tail --pid' (29777 in the above sample) *not* the OpenNMS
process itself (29779 in this case). Luckily, when OpenNMS exits, the
shell should exit, as well.

If we don't use "tail --pid" and OpenNMS exits abruptly (without
'opennms stop' being called **by systemd**), we end up with just the
tail(1) process running in the CGroup:

     CGroup: /system.slice/opennms.service
             └─163703 tail -F -n 0 /var/log/opennms/progressbar.log

And systemd thinks things are still happy, which is **bad**:

     Active: active (running) since Sat 2022-10-22 02:37:54 UTC; 5min ago

So, that's why the startup script is picky about 'tail --pid' being
there in systemd mode with the progress bar, and if it isn't, the
progress bar feature is disabled.

We should probably eventually switch to use Type=notify in systemd
instead of Type=forking that we have now. Ideally, we'd just exec
the OpenNMS Java process on startup and have it notify systemd when
it is up and running. See:
https://www.freedesktop.org/software/systemd/man/systemd.service.html#Type=

Here are some references for doing the notification directly in Java:
- https://github.com/faljse/SDNotify
- https://gist.github.com/juur/048cc3d0554953b717e9c6867970f30e
- Once we require Java 16, it has Unix domain socket channels:
  https://inside.java/2021/02/03/jep380-unix-domain-sockets-channels/
- Netty has it now: https://netty.io/4.0/api/io/netty/channel/unix/DomainSocketChannel.html

As an FYI, here are two other things I noticed:

Oct 23 00:46:18 dgregor-vm-perf systemd[1]: opennms.service: Can't open PID file /run/opennms/opennms.pid (yet?) after start: Operation not permitted
Oct 23 00:46:19 dgregor-vm-perf systemd[1]: opennms.service: Supervising process 37802 which is not our child. We'll most likely not notice when it exits.

I think the latter message about supervising is related to using the
forking configuration. Both of these seem to happen with or without
the changes in this commit.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[223e8bfd96...](https://github.com/lessthnthree/tgstation/commit/223e8bfd96a7762f0d23dd9b789fa90be1a572ec)
#### Sunday 2022-10-23 01:34:17 by Time-Green

Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

---
## [oxen-io/lokinet](https://github.com/oxen-io/lokinet)@[e981c9f899...](https://github.com/oxen-io/lokinet/commit/e981c9f89983a12cc75d691fc439366703d5bfff)
#### Sunday 2022-10-23 01:38:32 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [npjohnson/android_kernel_google_wahoo](https://github.com/npjohnson/android_kernel_google_wahoo)@[eb169c7fd4...](https://github.com/npjohnson/android_kernel_google_wahoo/commit/eb169c7fd4de408076e88ccd3532d68fd3846cac)
#### Sunday 2022-10-23 01:53:49 by Christian Brauner

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

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[75dfa159f0...](https://github.com/TaleStation/TaleStation/commit/75dfa159f0ba53b65bd4f256547842ec424173bb)
#### Sunday 2022-10-23 02:13:42 by TaleStationBot

[MIRROR] [MDB IGNORE] Micros the lighting subsystem (Saves a second of init) (#2605)

* Micros the lighting subsystem (Saves a second of init) (#69838)


About The Pull Request

Micros lighting objects, and their creation

We save a good bit of time by not walking space turfs adjacent to new objects.
We also save some time with micros in the actual underlay update logic.

I swear dude we spend like 0.8 seconds of init applying the underlay. I want threaded maptick already

Micros lighting sources, and corner creation

A: Corners were being passed just A turf, and then expected to generatecorners based on that. This is pointless.
It is better to instead pass in the coords of the bottom left turf, and then build in a circle. This saves like 0.3 seconds

B: We use so many damn datum vars in corner application that we just do not need to.
This resolves that, since it pissed me off. It's pointless. Lets cache em instead

There's some misc datum var caching going on here too. Lemme see...
Oh and a bit of shortcutting for a for loop, since it was a tad expensive on its own.

Also I removed the turfs list, because it does fucking nothing. Why is this still here.

All my little optimizations save about 1 second of init I think
Not great, but not bad, and plus actual lighting work is faster now too
Why It's Good For The Game

Speed

* Micros the lighting subsystem (Saves a second of init)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[f2d6f4a07d...](https://github.com/TaleStation/TaleStation/commit/f2d6f4a07d5fb8e7f1db90701bf64b890048e5d6)
#### Sunday 2022-10-23 02:13:42 by TaleStationBot

[MIRROR] [MDB IGNORE] Airlock open delay audit (#2609)

* Airlock open delay audit (#69905)


About The Pull Request

A: Mineral doors no longer take 6 SECONDS to open if you bump anything beforehand. Holy shit why would you do this.
B: Airlocks no longer require you to have not bumped anything in a second, lowered to 0.3 seconds. This is safe because I've moved shock immunity to its own logic. This should make opening doors feel less horrible
Why It's Good For The Game

Feels better.
Changelog

cl
balance: Airlocks will open on bump in series much faster now. As a tradeoff, you're immune to shocks from them for a second after you last got shocked by one.
fix: Mineral doors will no longer take 6 WHOLE SECONDS to open if you've bumped something else recently
/cl

* Airlock open delay audit

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [SecurityLab-CodeAnalysis/tgstation_tgstation](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation)@[3582aa77bb...](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation/commit/3582aa77bb68d43c1ebbff9e06226bf3089cb07a)
#### Sunday 2022-10-23 03:52:39 by LemonInTheDark

Slightly optimizes reagent splashing (#70709)

* Slightly optimizes reagent splashing

Ok so like, before, splashing a reagent performed a rudimentary
floodfill based off atmos connectivity.

This was really slow, because it did it using orange(), and repeated
orange()s to cut out JUST the rim, because we
needed to ensure things were ordered.

I've changed this to use floodfill. I've also moved some code that was
in a second loop into the first one, and replaced a repeated in check
with a single use of &

This is still not optimal for large ranges, because we filter by connectivity first
and THEN view, but it's faster for smaller ones.

BTW I'm also capping the max spread range at 40x40 tiles. If you want
more then 1600 you can rot in hell.

This takes the (uncapped range) cost of deconstructing a highcap tank
from 40 seconds to 0.16.

I hate this codebase

* god damn it

Co-authored-by: san7890 <the@san7890.com>

* whoops that's redundant

Co-authored-by: san7890 <the@san7890.com>

---
## [ddnet/ddnet-maps](https://github.com/ddnet/ddnet-maps)@[da9fdc59a6...](https://github.com/ddnet/ddnet-maps/commit/da9fdc59a6ddf925063eb92ded4cf9b78f7c3771)
#### Sunday 2022-10-23 04:30:42 by DDNet Maps

R Back to the Roots 1, R Back to the Roots 2, R Bumba, R Core, R Drain-Age, R EasyCore, R Everest, R Fairy Land, R GlassBox 10, R GlassBox 9, R Grey 1, R Grey 2, R Grey 3, R Grey 4, R HappyValenTees, R Hop, R JetPack, R Pathway 2, R Pathway 3, R Pathway 4, R Pathway, R Peaks, R R.I.P, R Red & Orange, R Retro 0, R Retro 1, R Strike, R Sunsetcave, R Want_a_Cookie, R Zip, R vitaminC, R .Background', R 0 KBeeeR S - 1, R 0 KBeeeR S - 2, R 007 - 1, R 007 - 2, R 2Long, R 3way, R 42, R 4luvz, R 84, R ATLAS, R Angry 2, R Angry, R Around the Globe, R Autumn, R Away, R Axom, R BSWL, R Bercy, R Bixnet, R Black Jungle, R Black, R Blue & Yellow, R Blue Adventures 1, R Blue Sky, R BlueRift, R BoX, R Brick World 2, R Brick World, R CCrush, R Castle of Glass, R Caveman, R Chaos Factory 2, R Chaos Factory, R Cigarette, R Cloudy, R Colors V2, R Creepeez, R CreeperFace, R DARKness 1, R DARKness 2, R DaFuQ, R DaMap 2, R DaMap, R Dark Rainbow, R DeadEnd, R Deeve1, R Derpy 1, R Desert Pain, R Desolation, R Diamond, R Divinum V2, R Drag-House, R Drag-House2, R Dream 1 V2, R Dream 2, R Drunk, R Equestria Girls, R Evo 1, R Experiment, R FWYS 1, R FWYS 2, R FWYS 3, R FWYS 4, R FWYS 5, R Fall In Love, R Feeling, R Finito, R Fly-4-2, R Forest, R Frats 1, R Frats 2, R Frats 3, R Frats 4, R Frats 5, R FreeZe, R Frostbite, R Full Moon, R GTF 1, R Genesis-2, R Genesis, R Get The Gifts, R Google, R Green, R GreenDream, R Halloween, R HappyEaster, R Hell 1 V2, R HellGate 1.5, R HellGate 1, R HellGate 2.5, R HellGate 2, R HellGate 3, R HellGate 4, R HellGate 5, R Heroic, R HeyYa, R Hook Fever, R Hope 2, R Hope, R Ice, R Icy Morning, R Icy Mountain, R Impulse_01, R Impulse_02, R Impulse_03, R JLI 1, R Jungle, R JustMap, R KitKat 1, R KitKat 2, R LATOM, R Lime, R Lost Story, R Love 0.6, R MCPV, R Maroon, R Maximum, R Michler 2, R Michler, R Moon of the Jungle, R Myth, R Next 2, R Next, R Pale 2, R Pale, R Pandaland, R Pandora, R Purple Panic 2, R Purple Panic, R R2D2, R RageOne, R Rainboom, R Reach Pluto, R Regret, R Revolution, R RockBlock 1, R Rovo, R S-Race 1, R S-Race 2, R Shaxx, R SilentNight, R Sky line, R Slim, R Snowy Sakura I, R Snowzz, R Spectrus I, R SpongeBob 1, R SpongeBob 2, R Stamina, R Standby, R Steff I beginning, R Steff III peace, R StormzZ, R The Captive Mind, R TheVoiD, R Totoro, R Toxic, R Tribute 1, R Tribute 2, R TsinmaS, R Tylost 2, R Tylost, R Underworld, R VeryLow1, R VeryLow2, R Violet, R Winter Dream, R WinterMine, R X-Cross, R Xeno Race #1, R Yin&Yang, R black-mountains 2, R black-mountains, R brainbase, R double up, R illusion, R lemonland, R lovely me, R lovely me2, R mario(=D), R o_O, R pepsi, R run_the_cube, R secreT, R skynet1, R skynet10, R skynet2, R skynet3, R skynet4, R skynet5, R skynet6, R skynet7, R skynet8, R skynet9, R slow, R smile, R valentees, R #MegaRosenkohl, R -Ikarus-, R 21, R Adrenaline 3, R Alpaga, R Ambrosia, R Arcade 2, R Arcade, R AreaOfEffect, R At Night, R Beachmap, R Besbex, R Best Of, R Black & Red, R Black_City, R Blizzard!, R Blue Hell, R BrokenBlack-1, R Brownie, R Chaos 1, R Chaos 2, R Chaos 3, R Chaos 4, R Cloud Nine, R Cocaine, R Confusion, R CrazyHOOD, R Creative, R Curse, R DawnOfDust, R Day, R DayWalker, R Dead Island, R Deadline 1, R Deadline 2, R DeathClaw, R Dels 2, R Dels 3, R Dels, R Deria, R Difficult 1.1, R Difficult 1.2, R Difficult 1.3, R Difficult 2.1, R Difficult 2.2, R Difficult 2.3, R Divided, R DoT, R Dragonscale, R Dreadful, R Easy Way, R Eclipse, R Elo-Hell, R Energie, R Equalize!, R Executive, R Explosive, R Fantabob, R Fly to the Moon, R Forever, R Four Gates, R Gold Rush, R Hard Way 1.0, R HardcoreZ, R HearTbeaT, R HearTcross, R Hell Fly, R Imagination3, R Insane 2, R Insane 3, R Insane, R Inspire, R IronFlight, R Jajka, R Lost Castle, R LowPossibility3.1, R Madness 5, R MicCore, R Multivitamin, R Nasa, R Natura, R Night Jungle, R NightRunner, R Nightmare, R Notice 1, R Ntumba, R Outlet, R Paik, R Paranoia, R Picklock, R Poke, R Rampage, R Reality, R Red Hell, R Repeat, R Rockita, R Scabrous 2, R SkyIsland, R Skyfly, R Skyisland2, R Skyisland3, R Space, R Summer Hell, R The Tower, R TheWalkingDead, R Therapy, R Think! 2, R Veni Vidi Vici, R Volcano, R Woader, R World of Magic, R Zephronikon, R blue-mountains, R skynet compilation, R supernice, R whatever, R ~AuTuMn~, R NUT Hardcore UNITED, R NUT_hardcore_bestof, R NUT_hardcore_race1, R NUT_hardcore_race2, R NUT_hardcore_race3, R NUT_hardcore_race4, R NUT_hardcore_race5, R NUT_hardcore_race6, R NUT_race1, R NUT_race2, R NUT_race3, R NUT_race4, R NUT_race5, R NUT_race6, R NUT_race7, R NUT_race8, R NUT_race9, R NUT_short_race1, R NUT_short_race2, R NUT_short_race3, R NUT_short_race4, R NUT_short_race5, R NUT_short_race6, R NUT_short_race7, A 4k

---
## [mmmm40/the-love](https://github.com/mmmm40/the-love)@[a92979dfbc...](https://github.com/mmmm40/the-love/commit/a92979dfbcb828d1e35489d35680a8b4c27e2815)
#### Sunday 2022-10-23 04:32:49 by mmmm40

Create README.md

# the-love
love in life 
There was a woman of very beautiful beauty, rich and rich, and she had everything. She went to the market every day. One day, he went to the market to buy. There was a handsome man, but he was poor. He went to buy, but he had little money. The market was selling used clothes and expensive clothes, so he bought clothes. The second-hand and she is his lung and his question was what made you buy this when you are handsome, he replied that I buy used because I do not have money I fell in love with him and took him every day with her

---
## [jiangbo0216/react](https://github.com/jiangbo0216/react)@[b6978bc38f...](https://github.com/jiangbo0216/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Sunday 2022-10-23 04:42:24 by Andrew Clark

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
## [newstools/2022-national-daily-nigeria](https://github.com/newstools/2022-national-daily-nigeria)@[b3eecf52d0...](https://github.com/newstools/2022-national-daily-nigeria/commit/b3eecf52d07a9b424bd5c8b801e62a101cad685f)
#### Sunday 2022-10-23 07:21:08 by Billy Einkamerer

Created Text For URL [nationaldailyng.com/17-yr-old-girl-commit-suicide-after-her-mom-reportedly-stopped-her-from-seeing-her-boyfriend/]

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[5637445413...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/563744541377564a28e31646410bef7e34507944)
#### Sunday 2022-10-23 09:20:58 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [wendyjasmine/Assignment-3](https://github.com/wendyjasmine/Assignment-3)@[921544244f...](https://github.com/wendyjasmine/Assignment-3/commit/921544244f42d5d7e4b8ff851f06fc8df4aa7812)
#### Sunday 2022-10-23 09:24:52 by wendyjasmine

Create README.md

#Wendy Woodward u3248688
This was my first time putting together an actual website and I relied heavily on the lectures, tutorials and quick google searches to do it, considering that I would say that this project was done pretty well. 

##Formatting
 I had a lot of problems with learning about divs and classes and when to put a div in, I would say I put in an unnecessary amount of div tags which made the overall work a bit clunky. I also did not utilise the class aspect very well, I should have given one class for all the headings and another for all the other chunks of text to make it easier. I also could have condensed a lot of the css by being more efficient with my planning as that made it hard to debug. I also did not know what to name everything so the naming of my elements and divs are very inconsistent.

##Presentation
I think overall all the colours and images are very fitting, the sound effects add an extra touch, as does the burnt bark in the background. These simple touches elevate the theme a little, along with the consistent colour scheme that contrasts nicely together. I constructed a few of the elements myself using photoshop and illustrator to add an extra bit of artistic flare which I think suited nicely. 

##Content
I managed to put a fair bit of information into the website which informs the reader well. It is not very extensive however becasue I wanted the website to be more simple, there is onyl a few facts for each panel and 3 panels in total. However I think by adding a link at the end that justifies it. 

##Interactivity & Javascript
I tried to make each panel interactive, the first being an animated button, 2 scrollable divs and 1 navigated by 4 buttons. I could have been more adventurous with my javascript use as I only used simple functions but I like how the sound decreases based on the window position, I thought that was a nice touch. My only worry is that the viewer might not know when to scroll or click a button which is why I added scrollbars and hover functions but I could have been clearer with the intention by saying "scroll" or "press this" after a few seconds.

Overall I think I did a decent job of this assignment, there is much room for improvement of course, particularly in the formatting and experimentation but I am satisfied with the outcome.

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[b4b6636b49...](https://github.com/PKRoma/Terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Sunday 2022-10-23 09:37:23 by Mårten Rånge

Relax shader strictness in RELEASE mode (#13998)

Disables strictness and warnings as errors for custom pixel shaders in
RELEASE. Windows terminal is not telling the user why the shader won't
compile which makes it very frustrating for the shader hacker.

After trying the recent preview none of my shaders loaded anymore in
Windows Terminal Preview which made me very sad. I had no idea what was
wrong with them. After cloning the git repo, building it, fighting an
issue that prevent DEBUG SDK from being used I finally was able to
identify some issues that were blocking my shaders.

> error X3556: integer modulus may be much slower, try using uints if possible.
> error X4000: use of potentially uninitialized variable (rayCylinder)

While the first one is a good warning I don't think it is an error and
the tools I use didn't flag it so was hard to know.

The second one I was staring at the code and was unable to identify what
exactly was causing the issues, I fumbled with the code a few times and
just felt the fun drain away.

IMHO: I want it to be fun to develop shaders for windows terminal.
Fighting invisible errors are not fun. I am not after building
production shaders for Windows Terminal, I want some cool effects. So
while I am as a .NET developer always runs with Warning as errors I
don't think it's the right option here. Especially since Windows
Terminal doesn't tell what is the problem.

However, I understand if the shaders you ship with Windows Terminal
should be free of errors and silly mistakes, so I kept the stricter
setting in DEBUG mode.

## Validation Steps Performed

Loaded Windows Terminal in RELEASE and DEBUG mode and validated that
RELEASE mode had reduced strictness but DEBUG retained the previous more
restrictive mode.

---
## [ccanandmallik/ruminations](https://github.com/ccanandmallik/ruminations)@[d18c8a5d06...](https://github.com/ccanandmallik/ruminations/commit/d18c8a5d06e979a1d3a27aab01ce7f783fadef31)
#### Sunday 2022-10-23 13:28:05 by Anand Mallik

and then, the poignant and provingly prolific stoner took a piss, paused his music, and from the voice of god -- though to be honest, it sounded like a snake but it was booming and from the heavens or whatever but I was very dehydrated at the time -- then I heard, from the voice of God -- 'Yeah OK, I'll allow it.'

---
## [PixelTheKermit/Combat-RIM-14](https://github.com/PixelTheKermit/Combat-RIM-14)@[ef884e34ed...](https://github.com/PixelTheKermit/Combat-RIM-14/commit/ef884e34ed7851d7780a9ea04963d445e4f06d99)
#### Sunday 2022-10-23 13:48:05 by PixelTheKermit

My name is not important. What is important is what I'm going to do

... I just fuckin' hate this world. And the human worms feasting on its corpus. My whole life is just cold, bitter hatred. And I always wanted to die violently. This is the time of vengeance and no life is worth saving. And I will put in the grave as many as I can. It's time for me to kill. And it's time for me to die. My genocide crusade begins here.

---
## [LovliestPlant/Skyrat-tg](https://github.com/LovliestPlant/Skyrat-tg)@[e8be775da4...](https://github.com/LovliestPlant/Skyrat-tg/commit/e8be775da4892a20186105a69bdc8b0832fba1cb)
#### Sunday 2022-10-23 15:23:16 by Paxilmaniac

Adds a collection of some kinda random greyscaled, recolorable clothes options (#16961)

* that's a few dmis

* a few sprite changes

* i hate making greyscale configs

* oh the misery

* 2:29 AM

* a few small things

* adds the stuff around more

* amazing work boss, this is why you're the best

---
## [FlacoFF/test_tgstation](https://github.com/FlacoFF/test_tgstation)@[422accbe4e...](https://github.com/FlacoFF/test_tgstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Sunday 2022-10-23 15:40:42 by John Willard

[MDB IGNORE] Shuttle engines part 2: Engines are now machines (#69793)

* Makes engines machines instead of structures

* Updates the maps

* Fixes boards and anchoring

* Removes 2 unused engine types

Router was actually used a total of once, so I just replaced it with propulsion.
I think cutting down on these useless engine types that make no difference in-game would be a nice first step to adding more functionalities to them.

* Don't use power (since shuttles dont have)

Shuttles don't have APCs, instead they just have infinite power, so I'm removing their power usage for now. I'm hoping this can be removed when unique mechanics are added to engines, because I would like them to make use of power like other machines.

* re-organizes vars

* deletes deleted dm file

* Slightly improves cargo selling code

* Renames the updatepaths

* Removes in_wall engines

I hate this stupid engine it sucks it's useless it's used solely for the tram it provides nothing of benefit to the server
replaces them with regular engines

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3bf95c086a...](https://github.com/treckstar/yolo-octo-hipster/commit/3bf95c086af12491bb90dc259c52ddd69183791a)
#### Sunday 2022-10-23 16:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [15peaces/15-3athena](https://github.com/15peaces/15-3athena)@[d6850638e9...](https://github.com/15peaces/15-3athena/commit/d6850638e90fb594d5b94547acf777e9ba9da1ae)
#### Sunday 2022-10-23 18:12:11 by 15peaces

== Skills & more ==
=General:
*Merged missing changes from 3ceam rev. 860

*Added official 2013 halloween event.

*Script command sscanf will now return -1 when a string is empty.

*Corrected a typo in a message related to push carts.

*Fixed a issue with the "allskills" command where it may not appear to give you all the skills accessable by your job. This is needed due to the normalize job skilltree recode.

*pc_normalize_job_max_skillpoint
-Added support for ths function.
-This works with the normalizing of jobs to set how many skill points should be invested into certain skills in a skill tree depending on the job since the max job level is different between jobs.

*pc_calc_skilltree_normalize_job
-Recoded the function to properly work for 3rd jobs.
-Note: This was so broken. I had to reverted it back to the original eAthena code and then update it to the way it should be. Wasn't easy.

*pc_search_job_skilltree
-Added support for this function.
-This replaces "pc_isSkillFromJob" and is a recode of it.

*pc_skillup
-Recoded the checks and message handling for telling the player how many skill points need to be placed into lower tier skills. This is also part of the reason "pc_calc_skilltree_normalize_job" was recoded. Having to update the skill range
-check every time new 3rd job skills come out is annoying. Better to let the normalize_job and search_job_skilltree functions work together for this.

*pc_jobchange
-Removed JOBL_THIRD from the upper setting switch.
-Third jobs are not a alternate version of 2nd jobs. Its a higher tier, making it its own job.

*Updated "pc_msg" and "msg_skill" MSG names with official ones.

*cooldown_rate; min_skill_cooldown_limit; no_skill_cooldown
-Added these config settings to the skill.conf file.

*Fixed a issue where some status's that deal damage and shows it will not show the damage done on the enemy if its a killing blow.

*Autocasted skills will no longer trigger a cooldown on renewal era skills.

*skill_cooldownfix
-Added support for this function.
-This function is kinda like skill_delayfix, but for cooldowns.
-At the moment its functional enough to allow cooldown time adjustments through status's but will be updated later to work with equip bonuses.

=Skills:
*WS_WEAPONREFINE
-Updated refine chance bonus gained from JobLV's to official.
-JobLV will not affect the success chance when below 50.
-When above 50, it will add a 0.5% chance bonus for each level above 50.
-This brings the added success chance to 10% at JobLV 70.
-Mechanics now get the full 10% added chance bonus no matter the JobLV.

*LG_BANDING
-Fixed a issue where using the skill under certain conditions would crash the server.

*WM_METALICSOUND
-Fixed a issue where it didn't deal bonus damage on sleeping targets.
-Now displays SP damage as blue numbers.

*GN_ILLUSIONDOPING
-Fixed a issue where casting the skill didn't require alcohol.

*SJ_STAREMPEROR
*SJ_NOVAEXPLOSING
*SJ_BOOKOFDIMENSION
*SJ_BOOKOFCREATINGSTAR
*SJ_GRAVITYCONTROL
-Added support for these skills.

*SJ_FALLINGSTAR_ATK
-The AoE size for the stellar mark check is now 5x5.
-Note: Sucks that its this small but its confirmed official.

*SJ_PROMINENCEKICK
-Now deals 2 hits.
-The first hit is the main damage. The second hit is the 100% fire damage.

*SJ_SUNSTANCE
*SJ_LUNARSTANCE
*SJ_STARSTANCE
*SJ_UNIVERSESTANCE
-Switching or disabling stances now removes status's given from skills exclusive to the previously active stance.

*SP_SOULDIVISION
-Adjusted map check code.

*SP_SOULEXPLOSION
-Now only usable in PVP type maps.

---
## [uup-dump-dev/website](https://github.com/uup-dump-dev/website)@[77ea6e8003...](https://github.com/uup-dump-dev/website/commit/77ea6e8003fe7447492c08d44e872b2a73fe3a17)
#### Sunday 2022-10-23 18:18:43 by eraseyourknees

Fix XSS in the error messages
The so-called """security researcher""" pretending he sent me a report
can go fuck himself. I never received your report. Not that I would pay
for this "work", or as I've recently taken to calling it, log shitting.

---
## [Jaybirdnerd/Citadel-Station-13-RP](https://github.com/Jaybirdnerd/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/Jaybirdnerd/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Sunday 2022-10-23 18:19:48 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [boxxxxxy/sandbox](https://github.com/boxxxxxy/sandbox)@[8f13363682...](https://github.com/boxxxxxy/sandbox/commit/8f133636822742248600915aa8b023a5300477dc)
#### Sunday 2022-10-23 19:00:32 by jrhy

sql fun
    fix unary- with precedence climbing
    want to see in side the index dammit
    wip: order by
    drop table
    recognize column constraints to reject keys/uniqueness for now
    s3db working but dirty
    funkyshooshoo
    break out memory/s3db db drivers
    null values going through driver
    left join works
    hmmmm, permutation broken
    simplify right-to-left fromItem permutation
    start join conditions
    joins working, alias untangled
    join working except need to fix schemas through subqueries
    holy shit join is kinda working
    adjust join parsing to be loud about subquery unimpl
    parse join on/using/unconditional
    breakout fromitem
    push joins, tableOrSubquery
    verking, gotta fix aliases
    rename FromItem->Source and Table->FromItem
    why TestJoin there is no JOIN
    verking
    fixedit
    insert
    verking
    sql: create table
    sql: start go sql driver
    sql: add funcs.go
    derive operator matching and precedence from single table
    string concatenation

---
## [marcxjo/stulto](https://github.com/marcxjo/stulto)@[9319f2b6bc...](https://github.com/marcxjo/stulto/commit/9319f2b6bc296df899fc20c133f6ebfccb9e4dcb)
#### Sunday 2022-10-23 19:12:40 by Mark Givens

config-cleanup - StultoGlobalConfig: remove unused settings

`nodecorations` isn't useful for my use case and almost certainly won't
be for anyone else's. I don't like being brusque about my reasoning, but
this is one of those cases where there's an argument that, if you don't
want window decorations, that's the window manager's responsibility to
accommodate. (I'm willing to be persuaded otherwise, given that GTK
_does_ expose the ability to override this handling for its own
windows, after all.)

`command_argv` arguably almost _should_ love in the global config. I'm
not really sure what I want to do here yet, to be honest. We probably
eventually _do_ want to support opening new tabs in a window and passing
in a command, so there's arguably a use case for this field even within
individual terminal configs (though it almost certainly doesn't need to
live directly within the profile config type, since we should be able to
free it immediately after loading the terminal widget).

---
## [haint126/obsidian](https://github.com/haint126/obsidian)@[3fec95b0de...](https://github.com/haint126/obsidian/commit/3fec95b0de8f55591d74e18543d49a07e982b3b9)
#### Sunday 2022-10-23 19:22:27 by haint126

Vault backup: 2022-10-24 00:36:31 : home

Affected files:
03_Life_experience/Growing up/50+ short, timeless hacks for your life/50+ short, timeless hacks for your life.md

---
## [flip1995/rust-clippy](https://github.com/flip1995/rust-clippy)@[9e8f53d09a...](https://github.com/flip1995/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Sunday 2022-10-23 20:08:19 by bors

Auto merge of #101986 - WaffleLapkin:move_lint_note_to_the_bottom, r=estebank

Move lint level source explanation to the bottom

So, uhhhhh

r? `@estebank`

## User-facing change

"note: `#[warn(...)]` on by default" and such are moved to the bottom of the diagnostic:
```diff
-   = note: `#[warn(unsupported_calling_conventions)]` on by default
   = warning: this was previously accepted by the compiler but is being phased out; it will become a hard error in a future release!
   = note: for more information, see issue #87678 <https://github.com/rust-lang/rust/issues/87678>
+   = note: `#[warn(unsupported_calling_conventions)]` on by default
```

Why warning is enabled is the least important thing, so it shouldn't be the first note the user reads, IMO.

## Developer-facing change

`struct_span_lint` and similar methods have a different signature.

Before: `..., impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>)`
After: `..., impl Into<DiagnosticMessage>, impl for<'a, 'b> FnOnce(&'b mut DiagnosticBuilder<'a, ()>) -> &'b mut DiagnosticBuilder<'a, ()>`

The reason for this is that `struct_span_lint` needs to edit the diagnostic _after_ `decorate` closure is called. This also makes lint code a little bit nicer in my opinion.

Another option is to use `impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>) -> DiagnosticBuilder<'a, ()>` altough I don't _really_ see reasons to do `let lint = lint.build(message)` everywhere.

## Subtle problem

By moving the message outside of the closure (that may not be called if the lint is disabled) `format!(...)` is executed earlier, possibly formatting `Ty` which may call a query that trims paths that crashes the compiler if there were no warnings...

I don't think it's that big of a deal, considering that we move from `format!(...)` to `fluent` (which is lazy by-default) anyway, however this required adding a workaround which is unfortunate.

## P.S.

I'm sorry, I do not how to make this PR smaller/easier to review. Changes to the lint API affect SO MUCH 😢

---
## [JuliaMath/QuadGK.jl](https://github.com/JuliaMath/QuadGK.jl)@[a55d889b97...](https://github.com/JuliaMath/QuadGK.jl/commit/a55d889b9799e052f2bbc89dac862d3d64bcd086)
#### Sunday 2022-10-23 20:35:41 by Christopher Rackauckas

Duals in the boundary values: avoid infinite recursion (#61)

* Duals in the boundary values: avoid infinite recursion

The previous behavior led to https://discourse.julialang.org/t/error-with-forwarddiff-in-turing/88633/16 . Dual numbers would just hit an infinite recursion because `float(::Dual)::Dual !<: AbstractFloat`. This should handle more cases where float(T) !<: AbstractFloat too, like TrackedReal.

Though I know that this probably isn't the best way to handle it. In a higher level interface like Integrals.jl, I think it would be better to detect such differentiation by boundary terms and specialize it. It's actually kind of funny and would be a good homework problem. If you put a dual number into the boundary with dual part one, i.e. , so then you integrate (f + df/dt eps) dt and by linearity of the integral it's just fundamental theorem of calculus approximated by GK! However, the argument above assumes that the dual part generated in the rules is exactly 1 (or rather, matches the partials of the boundary term so that it weighs it correctly). The algorithm doesn't exactly work like that, but it ends up being mathematically the same. What happens naturally in the code is that the rule values are multiplied by segment sizes as weights`f(a + (1-x[2i-1])*s)` and it is there that the `x` is "imparted with" the correct dualness to then give the integral of the derivative. 

Of course, algorithmically it should probably just see this is the case, integrate f, and then slap f into the dual part. I'm not sure if QuadGK.jl should be mucking with dual numbers and autodiff overloads though, so I'll just do that at a higher level. But it's something to think about here.

The reason to not do a complete overload is because for differentiating with respect to other quantities like parameters, you can fuse the primal and derivative calls rather than having them as two separate integrals, so it's definitely faster to differentiate the algorithm here. Except for handling the boundary.

I don't know, it's pretty cool haha. Such a beautifully convoluted way to approximate f(x).

* handle complex bigfloat

---
## [demonolock/postgres](https://github.com/demonolock/postgres)@[8272749e8c...](https://github.com/demonolock/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Sunday 2022-10-23 21:09:53 by Tom Lane

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
## [thebombzen/mpv](https://github.com/thebombzen/mpv)@[6f7506b660...](https://github.com/thebombzen/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Sunday 2022-10-23 23:24:38 by Philip Langdale

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

