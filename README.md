## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-14](docs/good-messages/2022/2022-05-14.md)


1,455,309 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,455,309 were push events containing 2,200,454 commit messages that amount to 126,261,456 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [shobbs528/FinalProject_a3](https://github.com/shobbs528/FinalProject_a3)@[2bc0109088...](https://github.com/shobbs528/FinalProject_a3/commit/2bc0109088bbf68a1b9c0e6f7407b55c7314f550)
#### Saturday 2022-05-14 00:12:25 by shobbs528

sound working and seemingly in 3D

Is it a bird? Is it a plane? No, it's a sound. But it's coming from somewhere! You know what they say about big sounds? They come from big sad people. That's me, I'm big sad. Oh yeah, I also turned down the volume on most of the sounds so your poor eardrums don't end up in San Francisco every time you play the game cause yeah tinnitus isn't that fun. Anyway, talk to you in a min. Also did you know that toasters toast toast? DO you know how to make a pool table laugh? Put the balls in the holes. Anyway, I'm pretty sure sound is okay now.

---
## [shobbs528/FinalProject_a3](https://github.com/shobbs528/FinalProject_a3)@[e137ef0a8f...](https://github.com/shobbs528/FinalProject_a3/commit/e137ef0a8f1168826d14be21ef05d22f640e27ec)
#### Saturday 2022-05-14 00:36:50 by Samwich422

OKAY

OKAY. This code. right here. as it is. Allows for networking, and shows the ghost avatar of the other player moving. THIS RIGHT HERE. Counts. Not perfect. But fuck yes. I think we're almost at 70% for this stupid fucking project

---
## [LensPlaysGames/RADII](https://github.com/LensPlaysGames/RADII)@[b6a3c4de30...](https://github.com/LensPlaysGames/RADII/commit/b6a3c4de30f19f32801553f20aca03d214c20104)
#### Saturday 2022-05-14 01:04:08 by Lens

RADII: Support for `Meson` build system

<https://mesonbuild.com/> is a modern build system
focused on simplicity. One of it's selling points is that
it *isn't* turing complete, and it won't allow itself to
ever be. Custom targets may not run more than a single
shell command. While these are limiting factors, the
overall focus on simplicity does lend itself to a pleasant
end user experience. I even was able to hack on it and get
my PR merged to get this to work at all in a freestanding
UEFI environment.

They are very friendly over there, and I think this build system
can go far, given it's great start on a good community, being fast
(it uses ccache automatically, as well as `mold` linker, etc.).

I haven't implemented the CKernel implementation yet, so I'll do
that now.

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[855e1360c0...](https://github.com/mamh-mixed/microsoft-terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Saturday 2022-05-14 01:14:26 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row. 

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight. 

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[446f280757...](https://github.com/mamh-mixed/microsoft-terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Saturday 2022-05-14 01:14:39 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [tikimcfee/LookAtThat](https://github.com/tikimcfee/LookAtThat)@[1addf1d4dd...](https://github.com/tikimcfee/LookAtThat/commit/1addf1d4dd0c576cf9e219af6a5049bb6c9bc5e8)
#### Saturday 2022-05-14 01:46:49 by Ivan Lugo

- SemanticInfoCategoryView is a thing
- GlobalSemantics are a thing too
- Cache by category, snapshot on view, gives random access to known info
-- TODO: Do the global part now. Maybe file selected + sub window?
-- Maybe just CategoryXMapArrays
-- RandomAccessCollection -> startIndex / endIndex / subscript(index)
-- Make a fake RAC by wrapper participant keys + maps

! ALSO HOLY SHIT IT WORKS ON THE IPAD OF COURSE IT DOES WHY DIDN'T I TRY THIS FIRST
! SERIOUSLY HOLY SHIT ALL OF A SUDDEN I HAVE A RIDICULOUS USE CASE!
! Lol I'm going to sit with the iPad on the side of the laptop, app open, receiving LSP commands, rendering them
! This is fun. This is just fun.

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[a064b35b25...](https://github.com/Sonic121x/Skyrat-tg/commit/a064b35b2571af36cf9d12cea8005843768af36d)
#### Saturday 2022-05-14 01:49:46 by SkyratBot

[MIRROR] Fixes an error sprites on medical wintercoat's allowed list. [MDB IGNORE] (#13566)

* Goodbye stack/medical (#66898)

Okay, why removing instead of giving it a sprite?

Simply put, those items are all small and there is no reason that you need to quick draw a suture/ointment and if you do, the medical belt can carry 7.
Allowed/exoslot items should be either medium/big/bulky sized items (Syringe gun) to make it worth inventory wise or items that you can quickdraw multiple times (Health Analyzer) to make your life easier.
Medical stacks are neither and would just get in the way if you try to quickly put them into a bag/pocket/belt and instead it goes into your exoslot where you would normally want to carry more valuable things like the syringe gun.

This doesn't feel big enough for a fix, spending 5 seconds making a list alphabetical doesn't few worth of code improvement, I will label this as QoL and if someone say it is a balance change I will follow you in game and keep placing shitty small items in your inventory via reverse pickpocketing.

* Fixes an error sprites on medical wintercoat's allowed list.

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [Gcchinese/Grasscutter](https://github.com/Gcchinese/Grasscutter)@[fbaeaee4b5...](https://github.com/Gcchinese/Grasscutter/commit/fbaeaee4b5aa82fe10897b60ea642d4428e8abd8)
#### Saturday 2022-05-14 02:35:44 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [ExpHP/truth](https://github.com/ExpHP/truth)@[93b985269d...](https://github.com/ExpHP/truth/commit/93b985269dd714f7a7cabd73ac7fe91a22d9c898)
#### Saturday 2022-05-14 04:10:30 by Michael Lamparski

add --output option to decompilation

Somebody is having trouble with decompilation producing mojibake
in the output file.  I think > for output redirection might not work
so well on CMD. (maybe '>' does ANSI? maybe rust is writing UTF-8 to
the ANSI APIs? I don't know. First let's find out if this even works!)

An --output option should resolve this problem by making text encodings
a non-issue (the OS must assume we're writing binary).  And honestly,
not having it just feels assymetric compared to compilation, so it
should be there anyways.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7a743898a2...](https://github.com/treckstar/yolo-octo-hipster/commit/7a743898a22accdf4f5a1c46ab7df651642697e5)
#### Saturday 2022-05-14 04:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [tedmiddleton/mainframe](https://github.com/tedmiddleton/mainframe)@[84927e3557...](https://github.com/tedmiddleton/mainframe/commit/84927e3557972577611d3c5f7c1265a9ef8d0aa9)
#### Saturday 2022-05-14 05:37:01 by Ted Middleton

CSV parsing, and frame::row_type

frame is a bit analogous to tuple (and is in fact implemented as
containing a tuple) in that each column is a unique type and iterating
through the columns isn't really supported because the columns have
different types. I think that in general this is the right choice if
we're comparing it to the idea of type erasure, but it does make dealing
with rows complicated and clumsy. In the meantime, we have a frame_row,
but it's kind of an iterator illusion - it's actually just a container
of iterators pointing to the series_vector's inside the frame.

When actually dealing with a parser like the csv loader, it's painful to
deal with an indeterminate number of rows. We're already limited
somewhat by the type of frame - we need to know ahead of time when
parsing the csv how many columns it has, and then return that many
columns regardless of what was actually in the csv. That can sort of be
mitigated by returning an oversized frame<mi<string>...> and then just
culling columns that are all missing, but in the parse itself, it's
annoying to have to deal with the indeterminate number of columns. For
the time being, frame_row is now frame_iterator_row and I'm introducing
frame::row_type, which is actually a vector of variants of all the
column types in the frame. I don't quite know whether this is the right
approach, though.

Right now, it has a series problem - if we have

using frame_type = frame<double, mi<bool>>;
frame_type f1;
frame_type::row_type row;
row.push_back( 1.0 );
row.push_back( true );
f1.push_back( row );

...believe it or not, row.push_back( true ) actually ends up adding a
double to the row, not an mi<bool>. C++ doesn't like
transitive-type inferencing - in the case of row.push_back( true ), it
needs to infer that this is bool -> mi<bool> -> variant<mi<bool>> and
instead prefers bool -(cast)-> double->variant<double>.

Can this be fixed? In the case of all mi<string>'s like the csv parser,
this is completely harmless because all the column types are the same.
In the case of heterogenous frame columns, it means in the documentation
I'll have to make it very clear that you need to specify row.push_back(
mi(true) ) rather than just row.push_back( true ).

All of this is a bit unergonomic. I'm still not quite sure how to handle
this. I'm now reconsidering maybe making uframe a bit more capable and
exposing that as a front-line type.

TODO:
- Finish CSV parser, handling special cases. parse_line() state machine
  needs to be refined a bit for escape sequences (or what passes for
  escape sequences in CSV. Also, utf8. utf8 is completely unhandled.
  Completely. There needs to be a utf8 scanner inserted into
  parse_line().

- SIMD-optimized correlations. One complication here is that SIMD
  support with msvc is slightly different than on g++, wrt compile-time
  vs run-time support.

- Join functions - frame::innerjoin, frame::outerjoin, frame::leftjoin.

- frame::groupby(). I'm still not 100% sure how to do this, but I think
  the key will be to create a new class type, like

  template< size_t ... indexes, typename ... Ts > grouped_frame;

  This would be returned by frame::groupby() and would include the same
  columns tuple that frame does (our usual non-mutating return-a-frame
  operation), but also maybe a multimap or unordered_multimap that
  indexes into the rows.

  I'm not sure how much frame functionality grouped_frame should take
  with it - also, should index values be exact or should grouping allow
  for ... groups?

- Add a function call wrapper for function calls in expressions

  auto f2 = f1.new_column<double>( "ceil", _f( std::ceil, _0 ) );

- Multiprocessing locks and guards. I still need to think about this a
  bit harder. Would it be enough to just say that frame and series
  objects should never be shared by reference and instead should be
  "copied" between threads?

---
## [Sunflair0/Cash-Grab](https://github.com/Sunflair0/Cash-Grab)@[caccf2c96f...](https://github.com/Sunflair0/Cash-Grab/commit/caccf2c96fe9dbbe74ead5f1cd9fb4ea9fb0919f)
#### Saturday 2022-05-14 05:50:38 by Sunflair0

Create README.md

This is my take on a group assignment while attending Midlands Code Camp. We were instructed to create a whack-a-mole game. But, smacking all those moles made me sad, so I made my own verson where you are penalized for hitting those adorable buggers.
I added levels (I am very proud of the buttons), 4 lives, changed the graphics, added the cash and mole pop up options, the preview and action bar on the bottom, the scoreboard at the end; really, I changed everything except the mole pop ups.
I worked on this a long time because by the time I finished one module, I learned how to do another better and I re-did that. I got very familiar with Greensock and animations, used 3D Paint and Canva (for SVG conversion). In the end, I figured since I am a junior developer, it's ok to have the program a bit messy, because I am still learning. It also proves I wrote it myself!
I am aware that Lighthouse testing rates my speed low, and I am sorry. If you have suggestions for me, I am WIDE OPEN to constructive critism! Help me be a better coder.
I do hope you enjoy playing the game. Try it on all hardness levels, use up all the hearts and restart the game. My only regret is that I don't have a cute animation at the end when you pass the game. 
But, I may have one in the future! Stay tuned.

---
## [y86-dev/linux](https://github.com/y86-dev/linux)@[213d266ebf...](https://github.com/y86-dev/linux/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Saturday 2022-05-14 07:16:59 by Linus Torvalds

gpiolib: acpi: use correct format characters

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>

---
## [benchi99/SonicProgressBar](https://github.com/benchi99/SonicProgressBar)@[986d6d5e12...](https://github.com/benchi99/SonicProgressBar/commit/986d6d5e1222b6659509e5f6e03b4cf89cdbe254)
#### Saturday 2022-05-14 10:44:01 by Rubén Bermejo Romero

Here I come, rougher than the rest of them

The best of them, tougher than leather
You can call me Knuckles, unlike Sonic I don't chuckle
I'd rather flex my muscles
I'm hard as nails, it ain't hard to tell
I break 'em down whether they're solid or frail
Unlike the rest I'm independent since my first breath
First test, feel the right, than the worst's left
Born on an island in the heavens
The blood of my ancestors flows inside me
My duty is to save the flower
From evil deterioration
I will be the one to set your heart free, true
Cleanse yourself of them evil spirits that's in you
Streaking lights, loud sounds, and instincts
Are the elements that keep me going
I am fighting my own mission
Nothing's gonna stand in my way
I will be the one to set your heart free, true
Cleanse yourself of them evil spirits that's in you
Won't be frightened, I'll stand up to all the pain and turmoil
Just believe in myself, won't rely on others
Get this power to wipe out the havoc and anarchy
This is my planet, gonna fight for my destiny
Here I come, rougher than the rest of them
The best of them, tougher than leather
You can call me Knuckles, unlike Sonic I don't chuckle
I'd rather flex my muscles
I'm hard as nails, it ain't hard to tell
I break 'em down whether they're solid or frail
Unlike the rest I'm independent since my first breath
First test, feel the right, than the worst's left
I have no such things as weak spots
Don't approve of him but gotta trust him
This alliance has a purpose
This partnership is only temporary
I will be the one to set your heart free, true
Cleanse yourself of evil spirits that got in you
Won't be frightened, I'll stand up to all the pain and turmoil
Just believe in myself, won't rely on others
Freedom will be waiting when serenity is restored
This is my planet, I shall not surrender
Won't be frightened, I'll stand up to all the pain and turmoil
Just believe in myself, won't rely on others
Get this power to wipe out the havoc and anarchy
This is my planet, gonna fight
Won't be frightened, I'll stand up to all the pain and turmoil
Just believe in myself, won't rely on others
Freedom will be waiting when serenity is restored
This is my planet, I shall not surrender
The new porcupine on the block with the buff chest
In the wilderness with the ruggedness
Knock, knock, it's Knuckles, the bloat thrower
Independent flower, Magical Emerald holder
I'll give you the coldest shoulder
My spikes go through boulders, that's why I stay a loner
I was born by myself, I don't need a posse
I get it on by myself, adversaries get shelved

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6f906cd650...](https://github.com/mrakgr/The-Spiral-Language/commit/6f906cd65085f85e4f03a8af7b982ce2ce8ad38c)
#### Saturday 2022-05-14 11:04:01 by Marko Grdinić

"9:30am. I am up and I am getting hit with lethargy. Lethargy for anything other than completing the scene. I do not feel like doing any more 'practice'. It is time to move on from that.

9:55am. Yeah, this feeling is rising up throughout my body. The feeling of having had enough. I do not want any hassle at all from art. I'll know right away whether this approach is viable or not.

I feel like quiting with what I've been doing before. I will focus all of my being on this single strike. It won't just land on the target. It will land on it absolutely.

https://mangadex.org/title/c288b108-5162-4065-aa3a-5857ec38c8d9/hikikomari-kyuuketsuki-no-monmon

Let me take this break to catch up with the two chapters of this that are out there and I will get into it. I feel like taking a break so I can roll it around in my mind.

10am. Right now I am just playing with disappointment. 3d is fun. 3d is how I think, I can in fact make art by directly manipulating objects in 3d space. But doing 2d from scratch. Just how am I supposed to int my way to understanding perspective. It would take a shitload of practice.

I am super lazy. I could use 3d as a teacher, but I do not feel like it. I do not feel like working hard on it, what I need to do is simply get it done in the simplest possible manner. 3/5 is more than enough for me. It is fine if I am a bad artist doing good art. Right now I am a good programmer capable of doing absolutely nothing with it. It will be my revenge towards the world for putting me in this situation.

10:45am. Let me start.

Yeah, let me start by blocking out the bed.

11:30am. I have to admit, Boxcutter is quite nice here. Being able to draw boxes directly onto the surface instead of having to make a cube and rescale is really proving its worth.

I've already blocked out 50% of the room. Let me block out the rig and the stool it is sitting on. As well as the desk.

12:30pm. Let me take a break here. I can't get it anymore right than this. It is not exact, and I am not sure where I am going wrong, but it is good enough. I'll do the doorframe and the curtains. After that I'll import the thing into CSP and start painting."

---
## [greenforce-project/llvm-project](https://github.com/greenforce-project/llvm-project)@[c2c259224b...](https://github.com/greenforce-project/llvm-project/commit/c2c259224bb30b089206dd69dc44aefddffec2f4)
#### Saturday 2022-05-14 12:21:03 by Amaury Séchet

const char* for LLVMTargetMachineEmitToFile's argument

The `LLVMTargetMachineEmitToFile` takes a `char* Filename` right now, but it doesn't modify it.
This is annoying to use in the case where you want to pass a const string, because you either have to remove the const, or copy it somewhere else and pass that. Either way, it's not very nice.

I added a const and clang formatted it. This shouldn't break any ABI in my opinion.
I'm sorry but I didn't know whom to put as reviewer for this, so I chose someone with a lot of commits from the .cpp file.

Reviewed By: deadalnix

Differential Revision: https://reviews.llvm.org/D124453

---
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[1ce5ca5baa...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/1ce5ca5baa71ad4b9af0f35be5d5fc5ab9c799b6)
#### Saturday 2022-05-14 13:38:11 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [Seif-Mamdouh/Master-the-Coding-Interview](https://github.com/Seif-Mamdouh/Master-the-Coding-Interview)@[a43e93a87f...](https://github.com/Seif-Mamdouh/Master-the-Coding-Interview/commit/a43e93a87f8e1014e5984cd089366d772f4fd593)
#### Saturday 2022-05-14 14:57:28 by Seif Mamdouh

Merge pull request #45 from Seif-Mamdouh/seifys

Fuck Shit bitch

---
## [lucaargolo/youtuber-block](https://github.com/lucaargolo/youtuber-block)@[9593c0674e...](https://github.com/lucaargolo/youtuber-block/commit/9593c0674e46467a393b4677ebaa0c09b75f0749)
#### Saturday 2022-05-14 15:03:21 by lucaargolo

aaaaaaaaaaaaaaaaaaaaaaaaaaaa (dream and techno? kinda? its unfinished and i want to die)

---
## [trice/DDOBuilder](https://github.com/trice/DDOBuilder)@[827339c9f2...](https://github.com/trice/DDOBuilder/commit/827339c9f21cc1be1db5d8ffbdd20288d884e81a)
#### Saturday 2022-05-14 15:51:04 by Maetrim

Build 1/0/0/139

Fix: Enhancement "Aasimar Scourge: Strike Down the Dead" now has the correct number of ranks(3)
Fix: "Shadowdancer: Shadowform" will now correctly grant Ghost Touch while active (Reported by mikameow)
Fix: Item "Legendary Cloak of Autumn" now has the correct icon (Reported by MIvanIsten)
Fix: Item "Legendary Cloak of Winter" now has the correct icon (Reported by MIvanIsten)
Fix: Many item images updated to remove Lock/Not proficient warnings
Fix: Augments of "Sapphire of Stunning, "Sapphire of Veritgo" and "Sapphire of Shatter" bonuses are now correctly typed as Enhancement, not Equipment (Reported by mikameow)
Missing Items:
---Legendary Darkmoss (Docent) (Reported by MIvanIsten)
Missing Set Bonus Icons:
---Epic Captain's Set (Supplied by MIvanIsten)
---Epic The Devil's Handiwork (Supplied by MIvanIsten)
---Epic Double Helix Set (Supplied by MIvanIsten)
---Curse Necromancer Set (Supplied by MIvanIsten)
---Unbreakable Adamancy (Supplied by MIvanIsten)
---Legendary Arcsteel Battlemage (Supplied by MIvanIsten)
Fixed Items:  (Reported by mikameow)
---Item "Van Richten's Legendary Cane" now has the correct weapon dice
---Item "Legendary Moonguard" various values fixed
---Item "Legendary Hexbreaker" various values fixed
---Item "Legendary Crabshell Buckler" various values fixed
---Item "Kobold Admiral's Tiller" various values fixed
---Item "Hector's Bracer" various values fixed
---Item "Epic Buckler of the Demonic Soldier" various values fixed
---Item "Buckler of the Celestial Soldier (Old)" various values fixed
---Item "Buckler of the Celestial Soldier" various values fixed
---Item "Barnacled Buckler" various values fixed

U51 Changes:
Fix: Epic past lives now grant a fate per point 2 epic past lives, not 3
Fix: U51 Destiny points spent will now be remembered after a file load action

---
## [trice/DDOBuilder](https://github.com/trice/DDOBuilder)@[5a94cb3b8a...](https://github.com/trice/DDOBuilder/commit/5a94cb3b8ae2334219153a0bd04e5f2c988eee01)
#### Saturday 2022-05-14 15:51:04 by Maetrim

Build 1.0.0.147

Fix: The Epic Destiny preview pane should no longer acquire a tree you have spent points in in a previously saved build (Reported by Laur)
---If you have since saved a build with 4 trees present. Empty the 1st tree of points spent, switch it to "No Selection" and save, close and reopen the file.
Fix: Applying and revoking a tier 5 in any epic destiny tree will now correctly unlock other epic destiny tree tier 5's (Reported by Hawkwier)
Fix: Primal Scream now has a Stance associated with it and now also applies to Dexterity and is a Morale bonus (Reported by Hawkwier)
Fix: "Bombardier: Efficient Heighten" now correctly costs 2ap (Reported by Guntharm)
Fix: Rapid Shot ranged power bponus now only correctly applies to Long and Short bows. (Reported by Aquoia)
Fix: All Sorcerer Elemental Apotheosis enhancement now state that they remove element proection while active (Reported by ASilver)
Fix: Feat "Stunning Fist" now correctly requires "Flurry of blows to be trained (Reported by Laur)
Fix; the old Fatesinger slef buff Hyms removed
Items:
---Explorer of the Depths (Helmet - Minor Artifact) (Reported missing by Guntharm)
---Perfected Bracers of the Demon's Consort
---Perfected Bloodstone
---Perfected Torc of Prince Raiyum-de II
---Perfected Vulkoorim Pendant

---
## [trice/DDOBuilder](https://github.com/trice/DDOBuilder)@[c2e29e3a77...](https://github.com/trice/DDOBuilder/commit/c2e29e3a77d95bec89c8b03d012ab74305837291)
#### Saturday 2022-05-14 15:51:04 by Maetrim

Build 1.0.0.133

Fix: It is no longer possible to equip multiple augments that suppress set bonuses in the same item (Reported in Strimtom build review 29)
---Augments that suppress set bonuses now have this shown in their descriptions
New: First attempt at Alchemical Orb augments (Issue raised by Delosari)
---These should apply to shields also, but no data on wiki about Alchemical shields
Fun: Strimtoms/Lynnabel thoery crafted tree Paladin "Shadowguard" is now available. See https://docs.google.com/document/d/1LDAhnR9rtLlsEq2056n1rjNFVca2TqL-7IhtlqJoJ0I/edit
---Evil alignments are now supported, but not selectable (Alignment override)
---Forum export will now show override alignment if present
Fix: "Knight of the Chalice: Critical Mastery" now applies to all weapons (not just favored weapons, fixed while working on Shadowguard tree)
Fix: "Deepwood Stalker: Horizon Shot" now correctly awards 3 sneak attack dice (not 1) (Reported by Kamatozer)
Fix: Wild Shapes of Water/Fire elementals are no longer incompatible with themselves
Fix: Duplicate Fire/Water elemental entries in Major Form incompatible stance lists removed
Fix: Alacrity issues for combat styles hopefully fixed (I need peeps to check this) (Reported by Grunthorno)
---I had to review all Alacrity sources in the builder to rework this one

---
## [trice/DDOBuilder](https://github.com/trice/DDOBuilder)@[0585bee36c...](https://github.com/trice/DDOBuilder/commit/0585bee36c8826c6b0c6b0bd4cf69437dbc5aa9e)
#### Saturday 2022-05-14 15:51:04 by Maetrim

Build 1.0.0.149

Fix: An issue where the "Rare" states of Artifact and Weapon Filigrees were swapped over when checking to apply rare effects was fixed (Reported by Bjond)
Fix: The "Manyshot" doublestrike bonus will now only apply for Short and Long bows (Reported by Bjond)
Fix: All items with "Assassinate" bonuses checked against wiki and values updated.
---Note that some wiki entires had obvious bad "Assassinate" values (not yet updated) so these were changed to approximate correct values for the items level.
Fix: Typo in "Deepwood Stalker: Heavy Draw" fixed (Reported by ASilver)
Fix: "Feydark Illusionist" can now be trained if you gain the "Magical Training" feat from any of the following additional sources (Reported by Cleru)
---Exalted Angel Core 1
---Fatesinger core 1
---Magus of the Eclipse core 1
---Shiradi Champion core 1
Fix: Many item images fixed to remove non-proficiency
U52 Changes: (From DDOCast 659)
---Seasons Herald: Crown of Summer updated (note that to get the effects you need to select the option in the self and party buffs window)
---New "Healing Amplification" augment (Assumed Blue, value can be entered) added
---New "Repair Amplification" augment (Assumed Blue, value can be entered) added
---New "Negative Healing Amplification" augment (Assumed Blue, value can be entered) added
---New "Melee Power" augment (Assumed Red, value can be entered) added
---New "Ranged Power" augment (Assumed Red, value can be entered) added
---Crown of Summer items updated "Titania's Glory" and "Legendary Crown of Butterflies"
Fix: Feat "Leap of Faith" description now specifies that a 15 seconds Feather Fall effect is applied on use
Fix: All spelling errors of "samage" changed to "damage" (Reported by ASilver)
New: Crafted reaper bonuses can now be added to items (U52.0.1)
---Rings gain a new augment slot which allows reaper crafting
---All other items retain their existing reaper crafting options
New Items: (From quest Dread Sea Scrolls)
---Legendary Ring of Dread Seas (Ring)
---Legendary Raptor Teeth Necklace (Necklace)
---The Legendary Magic Conch (Trinket)
---Legendary Skeleton Hunter (Maul)
---Sentient Jewel of the Lizardfolk

---
## [thomasLeclaire/opentelemetry-ruby](https://github.com/thomasLeclaire/opentelemetry-ruby)@[45429c7d53...](https://github.com/thomasLeclaire/opentelemetry-ruby/commit/45429c7d537807aad94003f7568650e4a7dc16d2)
#### Saturday 2022-05-14 16:12:47 by Andrew Hayworth

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
## [sang-bui20501/pdm-stadium-seat-booking](https://github.com/sang-bui20501/pdm-stadium-seat-booking)@[e151631751...](https://github.com/sang-bui20501/pdm-stadium-seat-booking/commit/e151631751b782995346d3ed580ee2cfb2e870d0)
#### Saturday 2022-05-14 16:14:31 by Sang bui

Sang | Cors | update cors policty

Fuck this shit to the very core i hate this

---
## [jamxe/YOURLS](https://github.com/jamxe/YOURLS)@[f3be67f43b...](https://github.com/jamxe/YOURLS/commit/f3be67f43b62b538cbe29b4b3b31331be3c40246)
#### Saturday 2022-05-14 16:23:02 by ྅༻ Ǭɀħ ༄༆ཉ

Fuck You Twitter :-(

See #2639 and https://git.io/Jvhw6 for more info

---
## [thgvr/tgstation](https://github.com/thgvr/tgstation)@[7c61bf65f2...](https://github.com/thgvr/tgstation/commit/7c61bf65f2b3c661bf622864bb7596e0e89d1f28)
#### Saturday 2022-05-14 16:43:30 by vincentiusvin

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)


About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

---
## [h0useofdupree/dotfiles](https://github.com/h0useofdupree/dotfiles)@[19e2bcf6a7...](https://github.com/h0useofdupree/dotfiles/commit/19e2bcf6a7345edbdf37d997de4a1ec1c4e4a254)
#### Saturday 2022-05-14 17:04:43 by h0useofdupree

Wohoo we're stable again.
Two fricking curly braces where put into colors.json which caused json.loads to read two objects which in return doesn't work.
Whoever put them there, fuck you!

Propably was me anyways...

---
## [jro1979oliver/device_motorola_deen](https://github.com/jro1979oliver/device_motorola_deen)@[a875af07cc...](https://github.com/jro1979oliver/device_motorola_deen/commit/a875af07cc12c9e0c9b0bc368a2e57d6ca993c05)
#### Saturday 2022-05-14 17:50:02 by Jeferson

Revert "deen: once more, fuck you all recovery"

This reverts commit bd946cf285e9b6a2b46342d2c3531a01ad8b2143.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[13797787ea...](https://github.com/mrakgr/The-Spiral-Language/commit/13797787ea1481f8e6a7867712af98d4abd9e421)
#### Saturday 2022-05-14 17:51:30 by Marko Grdinić

"1:55pm. Done with breakfast. Let me chill for a bit longer and then I will resume. It is really tought for me to do work like this. It feels much like when I was programming. It takes me ages to resolve to do something. Learning how to do something on the other hand is much easier.

Let me read Satanophany ch 202 and I will try to get going. I am just wasting my time here.

2:20pm. Let me start. I need to get through this instead of being so wasteful with time. I will get through this challenge and break through to 3/5.

2:25pm. Some chores cropped up. Let me do them.

2:55pm. I am back. Let me resume.

3:15pm. Wtf, now I am getting messed up by the balcony door.

3:40pm. I deeply regret my decision to start getting in there with the knife tool. This is kicking my ass so hard.

3:50pm. https://youtu.be/e2XQecffDOk

How do I split the door in two along the seams? Had I known this would be giving me so much trouble, I would have done it in Moi.

4pm. The time it is taking me to do the door is longer than it would take me to do it in moi. All I want to do is split the door into two, and do some carving. I am thinking how to do it using knife project, but maybe I am on the wrong track here. Just about I just split the stupid thing and do the extrusions, then I'll connect the two sides again using face snapping.

4:10pm. I an idiot. I should never have attempted a box modeling approach with this. It is sheer misery. Let me split it into multiple objects.

4:15pm. Oh, fuck this son of a bitch. Enough. I am going to wipe it and start from scratch. I am so pissed off right now. I wasted so much time with the box modeling approach.

4:30pm. This is much better architecture. The door is made up of several layers, including the pane of glass in the middle as its own layer.

I had real trouble manipulating the sides to get the proper profile as I made it a series of extrusions. I got it wrong initially and when I tried to reverse the sides inside out, I got faces sticking out. Now that they have their own middle faces things are a lot easier.

This kind of wore me out. Let me restart the process of beating the door into shape from scratch.

4:40pm. I had to take a nap to think about it. Let me do it.

4:45pm. And as it turns out I completely forgot the work that I did and came up with something inapplicable.

5:55pm. I fucked up the doorway way too many times and I had to take a nap to think about it.

6pm. This whole time I've been hearing the light rumbling thunder outside. It is early summer weather and it is getting a bit racuous.

6pm. I am considering whether my main mistake was simply not dooing the doorway in Moi.

6:05pm. I need to turn off. I'll do this properly next time.

7:15pm. The weather is better now. Also I am done with lunch. I'll close here.

Today I started off well enough, but did not do the finisher well. Going by how I actually modeled by heavily leaning on boxcutter and hops and mostly using boleans, and then running into trouble with the balcony door, I think I might have made a mistake picking Blender to do my modeling in. Moi might be a good deal better for the sketching phase.

I am going to switch my approach towards using it. Tomorrow I'll do the doorway in Moi.

It is true that I've benefited a few times from Blender's ability to do deformations, but it is not something that would have made that much difference from starting over in Moi given how simple the shapes are. Plus it is not like I have zero ability to readjust in Moi. The reason why I needed to deform some spots is because I was doing cuts. If I was just putting legos together in Moi, I could have hacked it. Plus in Moi I'd be more precise to begin with.

7:25pm. This situation I am in isn't too bad at all. I didn't reallly seriously consider Moi for sketching, but its capabilities are definitely better than Hopscutter's. If it was Moi vs vanilla Blender, it would be no contest - Moi wins hands down.

7:25pm. Forget box modeling in Blender, it is just getting me into trouble.

With Moi, I'll have to decide whether I want the whole scene there or just the props. I'll go with just the props for now. Either use should be valid, there is no need to repeat the layouting work that I've done today.

7:30pm. Getting to 3/5 at this point is not necessarily by about increasing my already abundant store of knowledge. Rather it is by recognizing the value of what I have.

If I had to do this shit purely with 2d, I'd be messed up right now, but it is worth going further with this.

7:45pm. Of the things to fail on, it won't be this room. Whether 2d or 3d is faster is not an intrisic feature of either style. It depends on my attitude and approach. I am going to master the rough sketchy blend of the two and get started with Heaven's Key. I will make a definite breakthrough soon."

---
## [Kylerace/tgstation](https://github.com/Kylerace/tgstation)@[a3c8013b45...](https://github.com/Kylerace/tgstation/commit/a3c8013b45c92fdb8efec7ba827d7b00191e2d55)
#### Saturday 2022-05-14 17:57:38 by GoldenAlpharex

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

---
## [RAIST5150/server](https://github.com/RAIST5150/server)@[69b7bb4322...](https://github.com/RAIST5150/server/commit/69b7bb43228902ad0fb0648d8ec9f4fabe0241a4)
#### Saturday 2022-05-14 18:12:26 by NeuromancerXI

Fixes SQL Async Causes High CPU Load
Noticed very high CPU Load on an idle server instance. With the guidance
of zach2good, added a sleep condition to prevent the process from
running wild and eating CPU for breakfast, lunch, and dinner.

Co-authored-by: Zach Toogood <zrtoogood@gmail.com>

---
## [flesh-cube/flesh-and-blood-cards](https://github.com/flesh-cube/flesh-and-blood-cards)@[eb04175f32...](https://github.com/flesh-cube/flesh-and-blood-cards/commit/eb04175f32be6465c0882fd36c729b605bd7690e)
#### Saturday 2022-05-14 18:14:41 by Tyler Luce

Fixed an issue with the functional text of Anothos, Art of War, Barraging Beatdown, 'Benji, the Piercing Wind', Blessing of Deliverance, Braveforge Bracers, Bravo, 'Bravo, Showstopper', Convection Amplifier, Crane Dance, Crush Confidence, Dawnblade, Dorinthea, Dorinthea Ironsong, Driving Blade, Edge of Autumn, Emerging Dominance, Enchanting Melody, Energy Potion, Flood of Force, Glint the Quicksilver, Harmonized Kodachi, High Speed Impact, Hit and Run, Induction Chamber, 'Ira, Crimson Haze', 'Kassai, Cintari Sellsword', Katsu, 'Katsu, the Wanderer', 'Kayo, Berserker Runt', Last Ditch Effort, Life for a Life, Mage Master Boots, Massacre, Mauvrion Skies, Mugenshi: RELEASE, Nebula Blade, Nimblism, Optekal Monacle, Perch Grapplers, Plasma Barrel Shot, Potion of Strength, Primeval Bellow, Pummel, Quicken, Refraction Bolters, Rout, Rushing River, Scar for a Scar, Singing Steelblade, Spellblade Assault, Soulbead Strike, Spoils of War, Staunch Response, Stonewall Confidence, Tectonic Plating, Teklo Core, Torrent of Tempo, Towering Titan, Warrior's Valor,
Whisper of the Oracle, and Zephyr Needle

Fixed an issue with the flavor text of Staunch Response

Fixed an issue where Plunder Run was incorrectly listed as banned in Blitz

Update the functional text of Alpha Rampage, Cintari Saber, Crazy Brew, Enlightened Strike, Flock of the Feather Walkers, Lord of Wind, Over Loop, Overpower,
Pack Hunt, Ravenous Rabble, Salvage Shot, and Savage Feast to match new HP1 printing

Update the changeling

---
## [Steviegt6/i-rule-translations](https://github.com/Steviegt6/i-rule-translations)@[2da56ed7da...](https://github.com/Steviegt6/i-rule-translations/commit/2da56ed7daa171bca85e2e16fb3ff70acd0acd4b)
#### Saturday 2022-05-14 20:51:35 by SlayerIbn

"Bucle" is pure shit and doesn't have the meaning that I want, "Ciclo" is fucking perfect

---
## [agzam/.doom.d](https://github.com/agzam/.doom.d)@[1f590d4546...](https://github.com/agzam/.doom.d/commit/1f590d454649d05ae19a819ad3ad6d461adb70af)
#### Saturday 2022-05-14 20:58:01 by Ag Ibragimov

fixes & improvements

org: evil-org rebinds C-k. Fuck that, I need that binding for
evil-insert-digraph

Some pdf-view-mode bindings. Finally, @dalanicolai made it possible to
use pdf-tools. Previously the scrolling sucked badly, I couldn't even
use it. dalanicolai/image-roll.el fixes it

---
## [ThatFiveGuys/goonstation](https://github.com/ThatFiveGuys/goonstation)@[bdad398f9e...](https://github.com/ThatFiveGuys/goonstation/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Saturday 2022-05-14 21:23:47 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [NyaaaWhatsUpDoc/gotosocial](https://github.com/NyaaaWhatsUpDoc/gotosocial)@[99f99b0372...](https://github.com/NyaaaWhatsUpDoc/gotosocial/commit/99f99b0372a02f428c0889e64b9ca4a326851aff)
#### Saturday 2022-05-14 22:44:39 by kim

fuck you linter

Signed-off-by: kim <grufwub@gmail.com>

---
## [YungBensonator/The-CMC-Project](https://github.com/YungBensonator/The-CMC-Project)@[b01638cd59...](https://github.com/YungBensonator/The-CMC-Project/commit/b01638cd590498bc17c50d617e2cbf3e832f79e3)
#### Saturday 2022-05-14 22:59:33 by YungBensonator

Nega Nerfs, Lucario B reverse, Samus fix. Fuck you, pay me the update

---

