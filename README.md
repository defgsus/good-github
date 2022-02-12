## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-11](docs/good-messages/2022/2022-02-11.md)


1,677,560 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,677,560 were push events containing 2,633,609 commit messages that amount to 202,565,624 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [Clancey/Maui](https://github.com/Clancey/Maui)@[ac6befcbee...](https://github.com/Clancey/Maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Friday 2022-02-11 00:11:51 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[5e29827ceb...](https://github.com/MemedHams/Shiptest/commit/5e29827cebbb7cd08d4bf5b210675526f324bf6d)
#### Friday 2022-02-11 00:37:51 by Zephyr

Spacemandmm fixes (#799)

* do it

Signed-off-by: Matthew <matthew@tfaluc.com>

* little more detail here

Signed-off-by: Matthew <matthew@tfaluc.com>

* put it in the wrong dmi

Signed-off-by: Matthew <matthew@tfaluc.com>

* Update code/game/objects/items/tools/chisel.dm

Copy paste gp BRRR

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

* resolve some issues that spacemandmm is complaining about because got fucking damn is it annoying when I am trying to code something and I get nonstop errors about stupid issues. also did you know that people though rand was exclusive on the high end? its actually not, both params are inclusive, which is stupid since this is different to almost every other god damn language

Signed-off-by: Matthew <matthew@tfaluc.com>

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[079f8ac515...](https://github.com/OrionTheFox/tgstation/commit/079f8ac51554bb338ac5826c9d06c8d4bc10be80)
#### Friday 2022-02-11 01:03:24 by LemonInTheDark

Adds moveloop bucketing, uses queues for the singulo rather then sleeps (#64418)

Adds a basic bucketing system to move loops.

This should hopefully save a lot of cpu time, and allow for more load while gaining better smoothness.

The idea is very similar to SStimer, but my implementation is much more simple, since I have to worry less about long delays and redundant buckets.
Insertion needs to be cheaper too, since I'm making a system that by design holds a lot of looping things

It comes with some minor tradeoffs, we can't have constant rechecking of loops if a move "fails", not that we really want that anyway
We also lose direct control over the timer var, but I think that's better, don't want people manipulating that directly
Not that it even really worked very well back when we did have it
Removes the sleep from singularity code

Rather then using sleep to store the state of our iteration, we instead queue the iteration in a list.
We then use a custom singulo processing subsystem to call our "digest" proc several times per full eat, with the hope of staying on top of
our queue
This rarely happens because the queue is too large, god why is a sm powered singulo 24x24 tiles.

I've also A: cached our dist checks, and B: Added dist checks to prevent attempting to pull things out of range
This might look a bit worse, but it saves a lot of work

Oh right and I made the singulo unable to eat while it still has tiles to digest. The hope is to prevent
overwork and list explosion.

Hopefully this will prevent singulo server stoppage, though I've seen some other worrying things in testing.

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[da30e9df00...](https://github.com/Stalkeros2/Skyrat-tg/commit/da30e9df0084a82e0f32df493d11ccaae7ad2aca)
#### Friday 2022-02-11 01:06:14 by SkyratBot

[MIRROR] Should fix shuttles leaving without sections [MDB IGNORE] (#11407)

* Should fix shuttles leaving without sections(#64764)

Should(tm)

This was a suggestion by @ Mothblocks and it seemed easy to implement

Fixes #64546 (Icebox evac will sometimes leave without sections)
Fixes #64653 (You might have fixed the kilo whiteship by making it move, but you didn't fix all of it)

Uh people won't just randomly get yeeted into space with half of a shuttle.
Kinda funny for people watching but not if you die of pressure loss or get stuck on the station
Runtime man bad

(Sleeping in here in general is like admitting that we're ok with missing a few atoms, which is what this runtime is. S just missing is better then overtime. Supposedly --Lemon)

* Should fix shuttles leaving without sections

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [Xen0byte/Stockfish](https://github.com/Xen0byte/Stockfish)@[cb9c2594fc...](https://github.com/Xen0byte/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Friday 2022-02-11 01:07:20 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [MrJamesGaming/FtcRobotController](https://github.com/MrJamesGaming/FtcRobotController)@[95e8c5b36a...](https://github.com/MrJamesGaming/FtcRobotController/commit/95e8c5b36a2593ae9a3b1eea00c1c0b4c5b246dc)
#### Friday 2022-02-11 01:13:27 by ProDCG

JAVA was developed by James Gosling at Sun Microsystems Inc in the year 1991, later acquired by Oracle Corporation. It is a simple programming language. Java makes writing, compiling, and debugging programming easy. It helps to create reusable code and modular programs.  Java is a class-based, object-oriented programming language and is designed to have as few implementation dependencies as possible. A general-purpose programming language made for developers to write once run anywhere that is compiled Java code can run on all platforms that support Java. Java applications are compiled to byte code that can run on any Java Virtual Machine. The syntax of Java is similar to c/c++.  History Java’s history is very interesting. It is a programming language created in 1991. James Gosling, Mike Sheridan, and Patrick Naughton, a team of Sun engineers known as the Green team initiated the Java language in 1991. Sun Microsystems released its first public implementation in 1996 as Java 1.0. It provides no-cost -run-times on popular platforms. Java1.0 compiler was re-written in Java by Arthur Van Hoff to strictly comply with its specifications. With the arrival of Java 2, new versions had multiple configurations built for different types of platforms.  In 1997, Sun Microsystems approached the ISO standards body and later formalized Java, but it soon withdrew from the process. At one time, Sun made most of its Java implementations available without charge, despite their proprietary software status. Sun generated revenue from Java through the selling of licenses for specialized products such as the Java Enterprise System.  On November 13, 2006, Sun released much of its Java virtual machine as free, open-source software. On May 8, 2007, Sun finished the process, making all of its JVM’s core code available under open-source distribution terms.  The principles for creating java were simple, robust, secured, high performance, portable, multi-threaded, interpreted, dynamic, etc. James Gosling in 1995 developed Java, who is known as the Father of Java. Currently, Java is used in mobile devices, internet programming, games, e-business, etc.  Java programming language is named JAVA. Why? After the name OAK, the team decided to give a new name to it and the suggested words were Silk, Jolt, revolutionary, DNA, dynamic, etc. These all names were easy to spell and fun to say, but they all wanted the name to reflect the essence of technology. In accordance with James Gosling, Java the among the top names along with Silk, and since java was a unique name so most of them preferred it.  Java is the name of an island in Indonesia where the first coffee(named java coffee) was produced. And this name was chosen by James Gosling while having coffee near his office. Note that Java is just a name, not an acronym.  Java Terminology Before learning Java, one must be familiar with these common terms of Java.  1.  Java Virtual Machine(JVM):  This is generally referred to as JVM. There are three execution phases of a program. They are written, compile and run the program.  Writing a program is done by a java programmer like you and me. The compilation is done by the JAVAC compiler which is a primary Java compiler included in the Java development kit (JDK). It takes Java program as input and generates bytecode as output. In the Running phase of a program, JVM executes the bytecode generated by the compiler. Now, we understood that the function of Java Virtual Machine is to execute the bytecode produced by the compiler. Every Operating System has a different JVM but the output they produce after the execution of bytecode is the same across all the operating systems. This is why Java is known as a platform-independent language.  2. Bytecode in the Development process:  As discussed, the Javac compiler of JDK compiles the java source code into bytecode so that it can be executed by JVM. It is saved as .class file by the compiler. To view the bytecode, a disassembler like javap can be used.  3. Java Development Kit(JDK): While we were using the term JDK, when we learn about bytecode and JVM . So, as the name suggests, it is a complete Java development kit that includes everything including compiler, Java Runtime Environment (JRE), java debuggers, java docs, etc. For the program to execute in java, we need to install JDK on our computer in order to create, compile and run the java program.  4. Java Runtime Environment (JRE): JDK includes JRE. JRE installation on our computers allows the java program to run, however, we cannot compile it. JRE includes a browser, JVM, applet supports, and plugins. For running the java program, a computer needs JRE.  5. Garbage Collector: In Java, programmers can’t delete the objects. To delete or recollect that memory JVM has a program called Garbage Collector. Garbage Collectors can recollect the of objects that are not referenced. So Java makes the life of a programmer easy by handling memory management. However, programmers should be careful about their code whether they are using objects that have been used for a long time. Because Garbage cannot recover the memory of objects being referenced.  6. ClassPath: The classpath is the file path where the java runtime and Java compiler look for .class files to load. By default, JDK provides many libraries. If you want to include external libraries they should be added to the classpath.  Primary/Main Features of Java 1. Platform Independent:  Compiler converts source code to bytecode and then the JVM executes the bytecode generated by the compiler. This bytecode can run on any platform be it Windows, Linux, macOS which means if we compile a program on Windows, then we can run it on Linux and vice versa. Each operating system has a different JVM, but the output produced by all the OS is the same after the execution of bytecode. That is why we call java a platform-independent language.  2. Object-Oriented Programming Language:  Organizing the program in the terms of collection of objects is a way of object-oriented programming, each of which represents an instance of the class.  The four main concepts of Object-Oriented programming are:  Abstraction Encapsulation Inheritance Polymorphism 3. Simple:  Java is one of the simple languages as it does not have complex features like pointers, operator overloading, multiple inheritances, Explicit memory allocation.   4. Robust:  Java language is robust that means reliable. It is developed in such a way that it puts a lot of effort into checking errors as early as possible, that is why the java compiler is able to detect even those errors that are not easy to detect by another programming language. The main features of java that make it robust are garbage collection, Exception Handling, and memory allocation.  5. Secure:  In java, we don’t have pointers, and so we cannot access out-of-bound arrays i.e it shows ArrayIndexOutOfBound Exception if we try to do so. That’s why several security flaws like stack corruption or buffer overflow is impossible to exploit in Java.        6. Distributed:  We can create distributed applications using the java programming language. Remote Method Invocation and Enterprise Java Beans are used for creating distributed applications in java. The java programs can be easily distributed on one or more systems that are connected to each other through an internet connection.  7. Multithreading:  Java supports multithreading. It is a Java feature that allows concurrent execution of two or more parts of a program for maximum utilization of CPU.  8. Portable:  As we know, java code written on one machine can be run on another machine. The platform-independent feature of java in which its platform-independent bytecode can be taken to any platform for execution makes java portable.  9. High Performance: Java architecture is defined in such a way that it reduces overhead during the runtime and at some time java uses Just In Time (JIT) compiler where the compiler compiles code on-demand basics where it only compiles those methods that are called making applications to execute faster.  10. Dynamic flexibility: Java being completely object-oriented gives us the flexibility to add classes,  new methods to existing classes and even creating new classes through sub-classes. Java even supports functions written in other languages such as C, C++ which are referred to as native methods.  11. Sandbox Execution: Java programs run in a separate space that allows user to execute their applications without affecting the underlying system with help of a bytecode verifier. Bytecode verifier also provides additional security as it’s role is to check the code for any violation access.  12. Write Once Run Anywhere: As discussed above java application generates ‘.class’ file which corresponds to our applications(program) but contains code in binary format. It provides ease t architecture-neutral ease as bytecode is not dependent on any machine architecture. It is the primary reason java is used in the enterprising IT industry globally worldwide.  13. Power of compilation and interpretation: Most languages are designed with purpose either they are compiled language or they are interpreted language. But java integrates arising enormous power as Java compiler compiles the source code to bytecode and JVM  executes this bytecode to machine OS-dependent executable code.  Example   // Demo Java program   // Importing classes from packages import java.io.*;   // Main class public class GFG {       // Main driver method     public static void main(String[] args)     {           // Print statement         System.out.println("Welcone to GeeksforGeeks");     } } Output Welcone to GeeksforGeeks Explanation:  1.  Comments: Comments are used for explaining code and are used in a similar manner in Java or C or C++. Compilers ignore the comment entries and do not execute them. Comments can be of a single line or multiple lines.  Single line Comments: Syntax:  // Single line comment Multi-line comments: Syntax:  /* Multi line comments*/ 2.  import java.io.*: This means all the classes of io package can be imported. Java io package provides a set of input and output streams for reading and writing data to files or other input or output sources.  3.  class: The class contains the data and methods to be used in the program. Methods define the behavior of the class. Class GFG has only one method Main in JAVA.  4.  static void Main(): static keyword tells us that this method is accessible without instantiating the class.   5.  void: keywords tell that this method will not return anything. The main() method is the entry point of our application.  6.  System.in: This is the standard input stream that is used to read characters from the keyboard or any other standard input device.  7.  System.out: This is the standard output stream that is used to produce the result of a program on an output device like the computer screen.  8.  println(): This method in Java is also used to display text on the console. It prints the text on the console and the cursor moves to the start of the next line at the console. The next printing takes place from the next line.

---
## [josephcrosmanplays532/Vyond-Legacy-Offline](https://github.com/josephcrosmanplays532/Vyond-Legacy-Offline)@[1155f27fce...](https://github.com/josephcrosmanplays532/Vyond-Legacy-Offline/commit/1155f27fce92bee67b895306d5ac4d4904ccde6a)
#### Friday 2022-02-11 02:44:41 by Joseph The Animator

Stupid Fucking Complaints Keep On Fucking Coming!

Gosh! can these complaints stop already! whiteboard animation desguised as comedy world not loading is normal. to fix that would be the starters trick or others!

---
## [copperwater/xNetHack](https://github.com/copperwater/xNetHack)@[50cfe48089...](https://github.com/copperwater/xNetHack/commit/50cfe48089d68c729f08a647c6f02a3f3da9242d)
#### Friday 2022-02-11 03:53:40 by copperwater

Optimization: only compute current holidays when needed

I want to expand use of holidays, but have been stopped by not wanting
to call it too much. Not that I seriously think it will harm
performance, but because it'd feel icky calling it once per turn or
whatever. Calling it every time a slime mold gets created already feels
like too much.

So this implements a system by which holidays only get recomputed when
there's been a day change to necessitate it. This is a little weird
since the game tracks days which begin at midnight and days which begin
at 6 PM, but overall it seems to work. If there hasn't been a change, it
just returns the holidays it computed last time.

---
## [s00se/termux-packages](https://github.com/s00se/termux-packages)@[7b355a29d0...](https://github.com/s00se/termux-packages/commit/7b355a29d05fa8570c2d9e25b55d135db96d6725)
#### Friday 2022-02-11 04:06:14 by Henrik Grimler

texlive{,-full}: remove package

It is one (soon two) years behind, and is a big hack: some of the debs
are larger than our upload system can handle, and the file lists are
generated from the tlpdb in a not so nice way that breaks horribly on
every texlive release.  Disk space is somewhat of a concern again on
the host that fosshost gives us at no (!) cost, and removing
texlive-full gives us ~1 GB of space.

The reasonable thing to do would be to set up a separate
"termux-texlive" repo, and create a package for every texlive package
rather than for every collection as done here.  Debian, ubuntu and
friends properly creates subpackages.  I am not really motivated to do
this though, so if someone else has use of a properly packaged texlive
and wants to look into it, then that would be great.

Users that want to use texlive should install texlive-installer
instead, it anyways allows for more convenient installation (you can
freely choose which scheme and which packages to install).

---
## [zulip/zulip-mobile](https://github.com/zulip/zulip-mobile)@[e117df5f73...](https://github.com/zulip/zulip-mobile/commit/e117df5f7375eecf6d50156038e6f699e3a6c04c)
#### Friday 2022-02-11 04:20:30 by Greg Price

Fix major startup lag, by using Animated.loop instead of giant duration

This was always a silly-looking hack: what we really want is for
this animation to loop indefinitely, and we do that by saying it
runs for 1000 seconds.

It turns out that doing that makes it extremely slow to start up!
Specifically, in my desktop Android emulator (which is typically
1x-2x the speed of my physical Pixel 4), it takes about 500ms.

Worse: it blocks the entire JS thread while it does that.  So
the app's whole UI is stalled.

Because we use this at startup (in LoadingIndicator), it's been
adding that 500ms of lag (likely more like 1000ms on many devices)
to our startup time since forever.  Moreover, we use
LoadingIndicator in the "Connecting..." banner... which there's
*four* of, one on each of the app's main-screen tabs.  So when we
start loading -- which is promptly after each startup, if you're
already logged in -- the UI hangs for another 2000ms, or more
depending on device.

There are a number of things we could do here.  It seems like a
performance bug in RN's `Animated`.  Also we could shorten the
1000 seconds to like 100 seconds, or 50 seconds -- better that
you occasionally see a stopped spinner, if you've already waited
a long time, than that you find the app completely stuck for a
full second or more every time you start it.

But in fact a very simple solution is available: if you take a look
at the upstream docs for Animated:
  https://reactnative.dev/docs/animated
there is built-in support for just explicitly having a loop.
There's no need for this hack at all.  Even in RN v0.47.2, the
version we were using when this hack was introduced in 2017 in
6594f8ebc, there was an `Animated.loop` and there was no need
for this hack.

So use that.

---
## [PixelPlusUI-Devices/alioth_kernel_xiaomi_sm8250](https://github.com/PixelPlusUI-Devices/alioth_kernel_xiaomi_sm8250)@[e597a250e1...](https://github.com/PixelPlusUI-Devices/alioth_kernel_xiaomi_sm8250/commit/e597a250e15b557aaaf29ca2733ae9934bab91de)
#### Friday 2022-02-11 04:37:05 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [jaltod/kernel_xiaomi_vayu](https://github.com/jaltod/kernel_xiaomi_vayu)@[009bb8613c...](https://github.com/jaltod/kernel_xiaomi_vayu/commit/009bb8613c8f467f6bc9089ab8aeacf6fce68e1b)
#### Friday 2022-02-11 06:31:38 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Carlos Jimenez (JavaShin-X) <javashin1986@gmail.com>
Signed-off-by: jaltod <jaguarexodus@gmail.com>
Signed-off-by: Jagaddhita Jalu <jaguarexodus@gmail.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[906fb0682b...](https://github.com/necromanceranne/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Friday 2022-02-11 06:47:32 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [sbaglivi/pollution](https://github.com/sbaglivi/pollution)@[74075e9854...](https://github.com/sbaglivi/pollution/commit/74075e9854a83462d6e997c3d6894183f02a9a9c)
#### Friday 2022-02-11 11:10:11 by Simone

deep in shit after my root password for sql is not working and resetting it is proving one hell of a bitch

---
## [kirin970-dev/android_kernel_huawei_kirin970](https://github.com/kirin970-dev/android_kernel_huawei_kirin970)@[ba6a506144...](https://github.com/kirin970-dev/android_kernel_huawei_kirin970/commit/ba6a506144ea666c6f4bc9f9d38bbc79557a1205)
#### Friday 2022-02-11 12:56:30 by A2L5E0X1

[DNM] kirin970: fuck you huawei

Change-Id: Ibc25ed2306e2ad7f717abe0adb124bb194226357

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[8f32cbe38d...](https://github.com/timothymtorres/tgstation/commit/8f32cbe38d956e06c919be36386da76befb0555b)
#### Friday 2022-02-11 13:19:06 by LemonInTheDark

Reworks janitor cyborg cleaning, focus on the slipping (#64131)

Alt of #64105 and #64126 (I'm sorry Novva, I should have said something earlier)
I main janitor. As a janitor main, my greatest joy in life is slipping people who ignore my signs

I've seen some people complain about janitor borgs, so I decided to look into em

Unfortunately, not only is the janitor borg just a straight upgrade to janitors, it has absolutely no reason to use most of its kit
We give it standard cleaning supplies, and hell even bespoke tools to deal with leaving slippery tiles everywhere, but we also just let them clean anything they can walk over

This seems a bit too much to me, even for borgs. Also it's like, really boring

So what if we made their movement based cleaning cost something? How about we make it suck water from their bucket. Use the same pattern as mop code, make it twice as expensive though. Give it a slowdown, some sound cues, and an action button to trigger it all

---
## [determined-ai/determined](https://github.com/determined-ai/determined)@[08888717a6...](https://github.com/determined-ai/determined/commit/08888717a6db21304115cd119ebb5d926d51c88e)
#### Friday 2022-02-11 13:39:00 by Bradley Laney

feat: unify task logs [DET-6062, DET-6063, DET-6064, DET-6065, DET-6066] (#3070)

This change adds persistent logs for all task types (well, all except poor old checkpoint GC). This means that logs are written to the logging back-end as configured in the master (PostgreSQL through master or Elastic) by Fluentbit and accessible through APIs in the master that translate reads to the back-end's language. To allow for this change, many other changes were required. A (probably) non-exhaustive list follows:
* Trial logs used to go to a `trial_logs` table or index. I tried to not tear the codebase asunder forever with trials and the others using different tables/queries/structs/etc everywhere. Existing tasks were marked has having `log_version == 0` and the old `trial_logs` table now serves logs those tasks (only trials). From now on, all tasks are written with `log_version == 1` and queries for their logs are routed to the `task_logs` table. The old trial logs table (now the `log_version == 0` table) is mothballed - it (mostly) shouldn't be touched again and the old logs should load from there fine forever while new features can be built on the new table. There were alternatives besides leaving trials and task logs separate forever that I shied away from; e.g., I considered a migration to update the trial logs table to schema of the task logs table, but since we access task logs by task_id, this would require rewriting the index on trial_id or adding one on task_id which is too expensive for a migration. This solution balances complexity, maintainability and migration cost.
* Because task logs went through the master, we were free to built features like readiness checks on top of them. Now that they don't, before logs leave the container a small helper script skims them, checks for the readiness logs and posts readiness to a new API. I considered alternatives here, too, like reading the logs back in on the master side, but that incurs a lot more overhead I felt this was more flexible anyway.
* The old events endpoint used to return logs, now it doesn't. This was because it (the eventManager that backed the endpoint) used to _store_ the logs, and now it doesn’t. In my opinion, the work to read the log stream and the old event stream and merge them is low value and annoying. Users should just prefer the new `/api/v1/tasks/:id/logs` endpoint for logs and rely on events to get the few task events that were relied on. Events will likely be supplanted by a task state watcher of some time so webui/cli can just watch for the readiness bit to flip.

---
## [LensPlaysGames/LensorOS](https://github.com/LensPlaysGames/LensorOS)@[58eba1f4fb...](https://github.com/LensPlaysGames/LensorOS/commit/58eba1f4fb27c760bab8c1741c25e8234fc95a82)
#### Friday 2022-02-11 13:52:28 by LensPlaysGames

[UART]: Overhault, refactor

So it turns out I'm an idiot and did a whole bunch of things wrong. Now boot time of the OS is literally near zero seconds (as opposed to a few, before this commit). It appears some missing parentheses and comparisons causes nonsensical spins to happen, meaning we were waiting for `maxSpins` to get to zero every single time. Luckily, I decided to rework the entire UART driver, and I ended up catching this bug. I am insanely blessed by the boot times now and I feel bad for spending two weeks with boot times over a second for no reason. Oh well, ig :^|

Improvements:
- Remove software-buffering before flush to hardware (UART chips have FIFO buffers that handle this situation with the hardware itself).
- Parse what type of physical chip the driver is interacting with
- Correctly wait for hardware to be ready (rather than just always waiting because conditions were backwards :^)

---
## [freedesktop/NetworkManager](https://github.com/freedesktop/NetworkManager)@[c944c9e9c4...](https://github.com/freedesktop/NetworkManager/commit/c944c9e9c46069e7053002588328ff9b068b9ddb)
#### Friday 2022-02-11 14:36:28 by Thomas Haller

platform: support IPv6 mulitpath routes and fix cache inconsistency

Add support for IPv6 multipath routes, by treating them as single-hop
routes. Otherwise, we can easily end up with an inconsistent platform
cache.

Background:
-----------

Route are hard. We have NMPlatform which is a cache of netlink objects.
That means, we have a hash table and we cache objects based on some
identity (nmp_object_id_equal()). So those objects must have some immutable,
indistinguishable properties that determine whether an object is the
same a different one.

For routes and routing rules, this identifying property is basically a subset
of the attributes (but not all!). That makes it very hard, because tomorrow
kernel could add an attribute that becomes part of the identity, and NetworkManager
wouldn't recognize it, resulting in cache inconsistency by wrongly
thinking two different routes are one and the same. Anyway.

The other point is that we rely on netlink events to maintain the cache.
So when we receive a RTM_NEWROUTE we add the object to the cache, and
delete it during RTM_DELROUTE. When you do `ip route replace`, kernel
might replace a (different!) route, but only send one RTM_NEWROUTE message.
We handle that by somehow finding the route that was replaced/deleted. It's
ugly. Did I say, that routes are hard?

Also, for IPv4 routes, multipath attributes are just a part of the
routes identity. That is, you add two different routes that only differ
by their multipath list, and then kernel does as you would expect.
NetworkManager does not support IPv4 multihop routes and just ignores
them. As the multipath attribute is part of the identity of an IPv4
route, we can get away with pretending that multipath IPv4 routes don't
exist.

Not so for IPv6. When you add (`ip route append`) an IPv6 route that is
identical to an exist route -- except their multipath attribute -- then it
behaves as if the existing route was modified and the result is the
merged route with more next-hops. Note that in this case kernel will
only send a RTM_NEWROUTE message with the full multipath list. If we
would treat the multipath list as part of the route's identity, this
would be as if kernel deleted one routes and created a different one (the
merged one), but only sending one notification. It would be nightmare to
find out which route was thereby replaced.
Likewise, when you delete a route, then kernel will "subtract" the
next-hop and sent a RTM_DELROUTE notification only about the next-hop that
was deleted. To handle that, you would have to find the full multihop
route, and replace it with the subtracted result.

NetworkManager so far ignored IPv6 routes with more than one next-hop, this
means you can start with one single-hop route (that NetworkManger sees
and has in the platform cache). Then you create a similar route (only
differing by the next-hop). Kernel will merge the routes, but not notify
NetworkManager that the single-hop route is not longer a single-hop
route. This can easily cause a cache inconsistency and subtle bugs. For
IPv6 we MUST handle multihop routes.

Kernels behavior makes little sense, if you expect that routes have an
immutable identity and want to get notifications about addition/removal.
We can however make sense by it by pretending that all IPv6 routes are
single-hop! With only the twist that a single RTM_NEWROUTE notification
might notify about multiple routes at the same time. This is what the
patch does.

The Patch
---------

Now one RTM_NEWROUTE message can contain multiple IPv6 routes
(NMPObject). That would mean that nmp_object_new_from_nl() needs to
return a list of objects. But it's not implemented that way. Instead,
we still call nmp_object_new_from_nl(), and the parsing code can
indicate that there is something more, indicating the caller to call
nmp_object_new_from_nl() again in a loop to fetch more objects.

In practice, I think all RTM_DELROUTE messages for IPv6 routes are
single-hop. Still, we implement it to handle also multi-hop messages the
same way.

Note that we just parse the netlink message again from scratch. The alternative
would be to parse the first object once, and then clone the object and
only update the next-hop. That would be more efficient, but probably
harder to understand/implement.

https://bugzilla.redhat.com/show_bug.cgi?id=1837254#c20

---
## [Aerden/tgstation](https://github.com/Aerden/tgstation)@[b48cda6afa...](https://github.com/Aerden/tgstation/commit/b48cda6afa047be95390dc1360e8d899ec6394b0)
#### Friday 2022-02-11 15:11:04 by LemonInTheDark

Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

* Please stop typecasting target, noooooooooooooooooo

* Fixes harddels in pinned module code

The logic for pinned modules was intentionally hanging references to the
mob that pinned the action button. I have depression.

The pinned_to list also was never fully cleared, but that would have
just exasperated the issue. I've converted its use of mobs to refs, and
its use of the module var into something better managed

(Friendly reminder that actions will persist in your nightmares forever
unless they are manually qdel'd, this code wasn't doing that.

Also cleaned up how the pinned_to list is managed, hopefully it's a bit
more action centered now

---
## [Aetherum17/WWU](https://github.com/Aetherum17/WWU)@[1621ac3bc7...](https://github.com/Aetherum17/WWU/commit/1621ac3bc785632bb892e4e0d8e2aa92f1f02270)
#### Friday 2022-02-11 15:25:33 by Vawser

World Trees

# World Trees
- Changed the World tree destruction to use a similar system to the Old God awakening system: the aggressor starts the process, and after 10 years the tree is destroyed. Other nations then have a chance to douse the tree and stop the destruction process.
- Added Demonic Vanguard nation: they spawn in around Nordrassil and represent as Archimonde and his legion forces. They appear after year 650 or later.
- "Plant Seeds of Teldrassil" decision now only appears after Nordrassil has been destroyed.
- "Form Darnassus" decision now only appears after Seeds of Teldrassil have been planted.
- Fixed Night Elf immortality so it is invalidated when Nordrassil is burnt.

---
## [SimonCalleLaverde/portfolio-v3-2022-next-js](https://github.com/SimonCalleLaverde/portfolio-v3-2022-next-js)@[06736449a5...](https://github.com/SimonCalleLaverde/portfolio-v3-2022-next-js/commit/06736449a5466a0fc5be1fde7331adf894a6aeea)
#### Friday 2022-02-11 17:25:37 by Simon Calle Laverde

Created base "npx create-next-app portfolio-v3-2022-next-js" app.

- Inspiring myself, starting simple 'wireframe/design'. Mood board.
- Adding 'Inspiration Sites' file.

-- Where I am (La Vega, Cundinamarca, Colombia) there was no light yesterday all day, until night. I drained my Mac's battery in the morning. Literally with candles during the night, and playing offline games (SuperHot VR) in my "Oculus Quest 2". :)

---
## [lidatong/agnostic-orderbook](https://github.com/lidatong/agnostic-orderbook)@[d8a2228f81...](https://github.com/lidatong/agnostic-orderbook/commit/d8a2228f81fad9b3fd91fcf6d5626cd589c5e068)
#### Friday 2022-02-11 18:03:36 by Charles Li

feat: optimize critbit using serum

test: add aob integration test against solana test validator

chore: remove logging

chore: fix unused import

feat: almost compiling...

feat: holy shit it compiles

fix: size panic, warnings, get unit tests passing

chore: bump to 2021 ed, solana 1.9.4

feat: add solana-profiler for profiling compute units

chore: CLion is stupid at linting

chore: explicit BorshDeserialize because CLion is stupid, fix warnings

chore: gitignore cargo lock

perf: unsafely transmute Vec<u8> into Slab DST [u8] a la Serum

Revert "perf: unsafely transmute Vec<u8> into Slab DST [u8] a la Serum"

This reverts commit 403d9e72b76781a99140609d9d6b00422f06d576.

chore: remove todo about DST

chore: debug solana unit test issue

---
## [bparees/api](https://github.com/bparees/api)@[5b82635ef1...](https://github.com/bparees/api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Friday 2022-02-11 18:52:26 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [chadvandy/community_bugfix_mod](https://github.com/chadvandy/community_bugfix_mod)@[b732cfeeee...](https://github.com/chadvandy/community_bugfix_mod/commit/b732cfeeeeebcae4f543de6466ee9a4f1a7bee2f)
#### Friday 2022-02-11 19:05:16 by sm0kin

Fix for Morathi Invisible Sword Bug

>messing around today trying to figure out why morathi's sword doesnt show in the campaign, found a fix funny enough, tested it working on the battle where I noticed it in my current campaign, and i loaded a new campaign to check out if it made her combat wonky on foot, no issues there, but importantly it does work while shes mounted and in the campaign overworld now, so no more swinging at empty air with her oddly clenched fist for me anymore, welcome to take a look and do with it as you see fit, just a simple variantmeshdefintion tweak (my theory is someone forgot to put it in, as this has been infrequently reported by players if you look it up since launch)

by Mr.Soul

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4dfeba3b67...](https://github.com/mrakgr/The-Spiral-Language/commit/4dfeba3b6731f3e663bb932e8cc3ae39f214b8b1)
#### Friday 2022-02-11 19:33:57 by Marko Grdinić

"10:55am. I am up. Let me chill just for a bit more and then I will start.

11:05am. The latest Konchuki chapter was wild. Let me start.

11:25am. No, what I had thought of yesterday would be too much of a pain in the ass to do. Forget it.

Right now, I do not have a good way of getting a tuple of outputs from a for loop. Let me ask about that.

11:45am. I asked, but I had a different idea from yesterday. What I am doing now is packing the body inside Flower Body. It is a HDA helper. Yesterday and during the night I've been thinking about producing multiple outputs, but that is wrong. What I need to do instead is do more packing and delineate them with groups. That will allow me to produce multiple outputs succinctly.

I need to make more liberal use of packing. When I merge packed objects, the underlying refs do not need to have the same fields. Meaning I do not need to have the bulbs have the `curveu` attribute in order to match the stalk.

12:55pm. Ok, I have it. I think I am finally satisfied with the level of control. I did a great deal of refactoring. I wasn't wrong about producing groups after all. But what I should not have neglected is packing. It is useful for more than just saving memory. It is an indispesable organizational tool. I also need to keep in mind that I need to mark object with groups so I can split them after merging.

This is the way to go.

1pm. Right now the whole scene has as much detail as the original, but it bakes in a snap.

1:10pm. Time for that break. I've started slacking anyway. I am perfectly satisfied with this.

2:25pm. Done with breakfast and chores. Let me finish the ep of Kenja no Deshi and I will resume. I think it is finally time I put down that bench and did the props.

2:45pm. Let me resume. Let me make a reply in the Houdini thread. Then I'll get started on the props. I've been working on these vines for way too long.

3:10pm. Did the update in the thread. I feel like a little break. Let me make up my mind to do the props.

3:40pm. Let me finally start the afternoon session for real. I want to make just one final adjustment to the flowers.

4:20pm. Ok, I've figured out how to orient the leaves along the stalk curve as opposed to in the upwards direction. The normal way is good for branches as they fall in the direction of gravity, but for the small leaves I really wanted them to go in the direction of the mesh curve.

It turns out the scatter and align can take in the target forward as an attribute. What I need to do is simply pass the `up` attribute there. I had to change how the flower HDA works to get it out, but now it works just fine. Great!

4:25pm. By giving an output node to an object, you can make sure it always displays the end result.

It is really good I figured this out. That is another bit of knowledge added to my mental library. It is important that I know how to pipeline the curve data up to the mesh.

Now...

4:35pm. I need to get started on the props. I literally have everything I'd ever need with the plants. This was the third refactor in the last half week, and I even put in a bit extra just now.

I've got it down.

The trouble is that I am backing in my own glory instead of moving on to the next step.

Let me just put down that bench.

4:40pm. Done. That is a good bit of icebreaking. Now let me do the sunbed. Let me open Blender so I can get a sense for its dimensions.

4:50pm. This is killing me. Drawing curves is beyond painful.

What I need to do here is rewatch those hipflask tutorials on construction planes. I should have done this earlier while doing the entry posts. Instead of modeling those using extrusions, I should have just done a curve and then swept it, but I had so much difficulty putting it where I'd want to.

https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273889/posts/4428289

Let me start from here.

5pm. > To enter the construction plane manipulation mode, you just tab the slash key.

Ahhhhhh...

5:05pm. Hrmmm, how do I manipulate breakpoints directly. It is no good if I have to fiddle with regular points.

https://youtu.be/SNDJzhOZZeg?list=PL4XNGOsVprEoijbvM0eLlwihBx0M2p1Lp
The Weekly Houdini Tutorial: The Anatomy of Nurbs Curves

Let me watch this again.

https://youtu.be/SNDJzhOZZeg?list=PL4XNGOsVprEoijbvM0eLlwihBx0M2p1Lp&t=38

I see a method there in the pane. That is what I should manipulate.

5:15pm. Hmmm, I could just draw a Bezier curve instead.

5:25pm. Ran into some ridiculous recursion related bug.

Sigh this will take a while. It turns out I have no idea how to draw curve. I know how to do it in Adobe Illustrator and Clip Studion. Even in Blender I should be able to manage it. But here things are so confusing.

5:40pm. I finally put the 4 sunbed points in the right place. It turns out that order 3 Bezier curves are hard to deal with. Let me watch the tutorials all the way through.

5:55pm. https://youtu.be/iv51A4syohU?list=PL4XNGOsVprEoijbvM0eLlwihBx0M2p1Lp&t=31

I really need to figure out how to draw using breakpoints.

6pm. I did not manage to figure out how to draw breakpoints, but the path tool is amazing. It allows me to draw nurbs curves, but also to control and rotate CVs.

6:35pm. As amazing as it is, putting an object network in geometry causes the outside geometry to disappear. As a rasult I lose track of relative sizes. Sigh. The reason why I need to do that is because the path tool just tosses CVs as objects on the top level.

I think I'll just stick with Bezier curves.

7:30pm. Let me go have lunch.

Actually, it will be in a bit.

8pm. Done with lunch. Let me close here.

Right now I am trying to make that sunbed. You wouldn't think this would be challenging for me, but you run into things.

First of all, I need to investigate what Bezier surfaces are.

I do not know how to make effective use of them. I fiddled around for a bit, and then I just resampled after that.

The second, I need more basic modeling skill in Blender. With the lantern plant, I studied a lot how to scatter and instantiate, but I still have great weakness in basic modeling. I still do not know what 99.9% of the nodes in Houdini do. A sunbed is possibly the easiest thing imaginable to model, but already I am running into limitations of my skill. In Blender it would be much easier. I can think of ways of doing it there. But here it is hard.

8:15pm. Also, I find myself being annoyed at not being able to go in isolation mode in Houdini. In Blender I just have to press slash to isolate an object, there should be something similar in Houdini, and I should really find out what it is.

The challenge of doing modeling is knowing which technique to use in what situation.

8:20pm. I've been in the zone the whole day today, but I think I should close here. Tomorrow I'll launch an in depth investigation of things I've overlooked.

I need more basic modeling skills to do these props effectively in Houdini.

8:25pm. I want to do them in it too, even though at this point I have the option of importing Blender stuff. But still, picking the best tool for the job requires me to actually understand the tools. Unless I put in the effort to get to know what is unfamiliar, that will never happen.

Forget the time taken. At some point I'll have the skills to move smoothly in Houdini. Until then I should keep practicing.

Eventually my 3d art skill will reach a sufficient level to work on my own things unimpeded.

8:30pm. Right now I might have completely failed my ML quest, but put it another way, all I need to break through to the next level is get an AI chip and implement a genetic programming system. The Singularity is quite near, yet so far away for me. Just when will I get rewarded for my efforts? I guess this journey is its own reward."

---
## [deathandmayhem/jolly-roger](https://github.com/deathandmayhem/jolly-roger)@[fd24a66ce8...](https://github.com/deathandmayhem/jolly-roger/commit/fd24a66ce8a537466b91181beb32b2d1255d861f)
#### Friday 2022-02-11 19:41:11 by Evan Broder

Improve fixture hunt data

This replaces the old fixture data from the 2015 hunt with a new set of
fixtures from the 2018 hunt. This improves on the old fixtures in a few
notable ways:

- The hunt is no longer complete. Our old fixture data had the hunt
  after all puzzles had been solved. The new fixture data is about
  halfway through the hunt (the team in our fixtures has fully solved
  the Emotions round, unlocked Hacking Island and Games Island but not
  completely solved either). We also now include guesses. The old
  fixtures didn't create guess objects, meaning that the guess queue
  didn't work as expected.
- The hunt has interesting structural components. The 2015 hunt was a
  great hunt, but mostly flat structurally. Thus it provides a
  suboptimal example of Jolly Roger's more sophisticated organization
  schemes. 2018 had much more going on structurally (including
  overlapping metas and multi-level round structure)

In order to make the experience more pleasant, if you are an admin and
there are no hunts, we add a button to the hunt list page to create the
fixtures (instead of needing to invoke the Meteor API method manually
from the JS console).

---
## [FiendsOfTheElements/FF1Randomizer](https://github.com/FiendsOfTheElements/FF1Randomizer)@[34eea2f3d1...](https://github.com/FiendsOfTheElements/FF1Randomizer/commit/34eea2f3d105d9b5067aa55400b894c58c00e924)
#### Friday 2022-02-11 20:11:52 by mhn65536

Mhn65536/oops2 (#802)

* Tournament Item magic Pool
Lower Thief Agility Settings
Buff Tier1 Damage Spells

* fix

* oops

* i hate my life

Co-authored-by: x.y <x.y@z>

---
## [gnestor1815/TheSqueezeFG](https://github.com/gnestor1815/TheSqueezeFG)@[7245b5805d...](https://github.com/gnestor1815/TheSqueezeFG/commit/7245b5805d5c8a6b705d48c513b89381006e5c90)
#### Friday 2022-02-11 20:22:06 by gnestor1815

README.md

This is a game based on a video series that my friends made in their first year of college. I got bored found a fandom my friend made for them, read it, and made a video game based on that. Here are links to those. To properly play this game remember to keep every file together in the same folder you download it. Sadly there will be a method telling you that something went wrong. That's the background music I couldn't upload to github.
Youtube Vid: https://youtu.be/JRh9_gPsRUM
Fandom: https://the-squeeze-epic-series.fandom.com

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[eeb81a265b...](https://github.com/Perkedel/Kaded-fnf-mods/commit/eeb81a265b7b23e04d17de0326871c947b0243dc)
#### Friday 2022-02-11 20:36:59 by Joel Robert Justiawan

[skip ci] 🍐 Bar Psi Pascal

TODO: create confession statement of peer pressure. talk about how did Animusic failed because of enforcing yourself for perfectionism, mismanagement by not hiring more and because the only talented left it destroyed everything, use videos from llike The Science Elf & Computer Clan. what did you learn from it. and add other failed projects and get what lesson can be taken. talk about your own LFM mod, Heartbreaking song took longer time than expected, mark this mistake that I shouldn't have chosen song with unstable tempo like this. make this grounds why are you pressured. So then you will prematurely release this update leaving the incomplete state (but pls still continue after you merged master of Kade Engine for one last time, pay respecc).

links you will need to consider:
- TwitLonger https://www.twitlonger.com/show/n_1srv3c2 Post this to twitter. SIKE!! ya you wish, I would use such a centralized website that if gone, destroyed, sued, what tragedies then its content too gone for good. LOL NOPE! you just got bamboozled haha! sorry, jk. TwitLonger good, based.
- Odysee https://odysee.com/@JOELwindows7:a/LFM-Confession-PeerPressure:5 the original file. sorry, I have to bamboozle you. don't use TwitLonger yeah. use Odysee instead! Okay clarfication, Odysee is based on LBRY, which itself is a protocol where it's legionized, decentralized. every user of LBRY backs the content up and reseed them. the power of Blockchain. so decentralized, makes it hard to destroy, because everyday, the LBRY user increases.

unlist latest week Overbuse Kevin Macleod temporarily

change texted week loading count measurement based on Week Name array instead of previously of Week loads (contains what song in each line). Week Name text file itself is from upstream Kade.

add text on Boot splash screen stating that this LFM is a mod of FNF. maybe I should also state that we forked directly from Kade Engine github repo???

install hitsound so it's like osu! UNTESTED! also each note can select which audio file to play per hit. yey customizable hitsound!!!

IDEA: okay uh, perhaps I should've gone with osu!'s treatment too, where hitsounds are grouped. each section selects what group. and each note plays one of the audio file in that group selected during this section. be it snare, kick drum, tick, or other. customize group! add new group of sound for more custom sound! and also still back again, directly choose sound file. OH OH OH!!! soundfonteh too!! doggydentures. alright, that's complicated. we need ways to load SF2 into that. Haxe SF2 pls!!!! also WHERE IS JUCE INTEGRATION?!?!??! WE NEED VST SUPPORT!!!!
edit what audio file of hitsound plays in charting state UNTESTED. Select a note (or adding a note selects that newly created note), and go to Notes tab. there is new input text field `Hitsound Audio filepath` there, all default note uses `SNAP` like this charting state hitsound is. now you can pick filename whatever audio file exist in a... shared??? or maybe preload? idk.. yeah I should take a look more again.

TODO: now I also should have checkbox whether or not to use note's hitsound, during charting state. you know hitsound in charting state has bug! play again, and DUAR!!! all hitsound plays till the one that is not touched yet. okay, check this to use note's hitbox sound. uncheck to use internal charting state's sound instead.

okay Kontraktua Majoris is a shrine for the Protoglin Amexamlef. NO, no religiousy. no. this is to honor 3 significant mods that requires greatest and luxurious attention and care.

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[6d52cc6fe3...](https://github.com/Koi-3088/ForkBot.NET/commit/6d52cc6fe395e1ed84194e2fa338784afd853ea8)
#### Friday 2022-02-11 20:52:15 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [AICP/kernel_oneplus_sm8250](https://github.com/AICP/kernel_oneplus_sm8250)@[c851c59490...](https://github.com/AICP/kernel_oneplus_sm8250/commit/c851c59490ce5b1efeca8c9775b2588246ff1d3c)
#### Friday 2022-02-11 21:39:59 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[7780b7bfd8...](https://github.com/cockroachdb/cockroach/commit/7780b7bfd8a73b1ec0567563465e4cb097a0cdd0)
#### Friday 2022-02-11 23:57:42 by craig[bot]

Merge #75568 #76327 #76355 #76386 #76388 #76392

75568: util/tracing: prevent spans reuse during registry iteration r=andreimatei a=andreimatei

ActiveSpansRegistry.VisitSpans() was referencing spans without
accounting for the references by incrementing the span's reference
count. This resulted in races between that use and the spans getting
Finish()ed and re-allocated.

Fixes #75380

Release note: None

76327: pkg/storage: support suffix replacement on MVCC interval collector r=sumeerbhola a=nicktrav

The `SuffixReplaceableBlockCollector` interface was added to to Pebble
in cockroachdb/pebble#1377, which allows a block property collector to
indicate that it supports being updated during suffix replacement.

The existing `pebbleDataBlockMVCCTimeIntervalCollector` block property
collector does not currently support suffix replacement. However, given
a new suffix, the interval for a block can be trivially calculated.

Implement the `SuffixReplaceableBlockCollector` interface.

Release note: None

76355: bazel: various improvements to generation r=irfansharif a=ajwerner

This adds targets for `:stringer`, `:gomock`, `:execgen`, `:optgen`, `:misc`, and `:docs` to `//pkg/gen` and then some aliases `:code` and `:gen`. This PR then leverages these targets to do all code generation. 


76386: multitenant: add more log messages around RU limiting r=RaduBerinde a=RaduBerinde

#### tenantcostserver: add some verbose logs

This commit adds some verbose logs describing the token bucket
requests that are happening.

Release note: None

#### tenantcostserver: add logs when reconfiguring RUs for a tenant

This commit adds a log message when a tenant token bucket is
reconfigured.

Release note: None

#### tenantcostclient: add trace event for delayed requests

This change adds a trace event for any request that has to wait for
more than 1 second in the RU limiting subsystem.

Release note: None

76388: execinfra,streamingccl: fix a span use-after-finish in eventStream r=andreimatei a=andreimatei

The eventStream was capturing the ctx passed to its Start() method and
using it until Close(). At least in the case when the eventStream was
used by the DistSQL projectSet processors, eventStream.Close() was being
called after the respective ctx stopped being valid (because the
respective tracing span had been Finish()ed).

This patch fixes this in two separate ways:
- the eventStream creates a new span for its work, as the Start() interface
  does not guarantee that the ctx will have a longer lifetime (and
  neither should it make any such guarantees, in my opinion).
- the projectSet processor will now keep its span open for long enough
  to encompass the full lifetime of the underlying generators (of which
  the eventStream is one). Its span was already living almost long
  enough; it was just a matter of ordering. To get the ordering right,
  I've had to add some indirection through the ProcessorBase.

Fixes #75335

Release note: None

76392: rowexec: lower the minimum limit in join reader from 8MiB to 100KiB r=yuzefovich a=yuzefovich

If `distsql_workmem` limit is set to a value lower than 8MiB we bump it
up to 8MiB (this was introduced in 306f8edada31e3386e0414eb8a69436b67fd11d8).
The reasoning is that the joinReader doesn't know how to spill most of
its in-memory state to disk (except for the buffered rows stored in the
disk-backed row container). The value was chosen based on 4MiB batch
size hint for the index join strategy. This commit lowers the value to
100KiB while making a corresponding adjustment to the batch size hint.
Namely, whenever the Streamer API is used, then a quarter of workmem
limit is used as the hint; if the Streamer API is not used, then a half
of workmem limit is used.

This should not really matter in the production setting since workmem
should not go lower than 8MiB, but it helps us to work with smaller
blobs in some tests.

Release note: None

Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>
Co-authored-by: Nick Travers <travers@cockroachlabs.com>
Co-authored-by: Andrew Werner <awerner32@gmail.com>
Co-authored-by: Radu Berinde <radu@cockroachlabs.com>
Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>

---

