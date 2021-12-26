## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-25](docs/good-messages/2021/2021-12-25.md)


1,127,225 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,127,225 were push events containing 1,479,246 commit messages that amount to 91,002,330 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 21 messages:


## [fulpstation/fulpstation](https://github.com/fulpstation/fulpstation)@[c797bf79ea...](https://github.com/fulpstation/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Saturday 2021-12-25 00:20:27 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[66a9ca0e33...](https://github.com/i3roly/glibc_ddwrt/commit/66a9ca0e33392c69bda1384a8bfde8dac56e94a6)
#### Saturday 2021-12-25 00:45:55 by gagan sidhu

47915/4.14.259, merry christmas. "first came flame, then came autotune" - randy marsh

- tried to fix the httpd javascript a little more. i think it's better
now.

- i am thinking sftp isn't working with my side because i'm on a mac.
everything seems fine. anyways i set the subsystem to 'sftp-internal' in
the sshd_config. so if any of you linux users experience issues please
open a ticket i'd be happy to try and fix it.

merry fucking christmas, and go fuck yourself

- the washington redskins

* Shelly's room, evening. Randy knocks on her door *

Randy
        Shelly, that's enough time on your phone.

Shelly
        Leave me alone, Dad! Stop nagging me all the time!

Randy
        You know we're all cutting down on phone time.

Shelly
        [sits up]

        Don't limit me! You don't even understand me!

Randy
        [sees a poster of himself as <'famous' "musician">,
        his secret identity]

        Yeah. I don't understand you at all. A lot you know.

        [walks away saddened]

        *   The Marsh garage    *

*  Randy is adding more stacks of cash to those already  *
*    hidden behind the poster. A door opens and Randy    *
*            quickly seals it up.                        *

* He gets to his workbench just as Stan closes the door. *

Stan
        Uh hey Dad. I need to talk to you.

Randy
        Oh really? A-About... about what?

Stan
        Dad, is it possible for someone to be one way on
        the outside but totally different on the inside?

        [Randy sighs deeply and stands up to walk]

        I mean, can someone identify as one sex but be
        something else but still have it be nothing about sex?

Randy
        Yes. Yes, Stan. I am <'famous' "musician">.

Stan
        ...What?

Randy
        It started off so simple. There's a guy at work. Hanson.
        He would use the bathroom and just blow the thing up, you know?
        Not only that, but he was in there all the time! I finally got
        fed up and pretended to be a woman.
        I called myself <'famous' "musician">. Have you ever been in a
        woman's bathroom, Stan? It's all clean and there's enough stalls
        for everyone. It was so freeing. I started singing while I was
        in there, and then I- started writing things down.

Stan
        Well you said you knew a guy at work who was
        <'famous' "musician">'s uncle.

Randy
        Yah, that's my cover.

Stan
        The chick that wrote the theme song to the new
        <shitty recession stimulus-funded book and movie series>, is you?

Randy
        Yeah.

        [turns around and faces Stan]

        The record company messed it all up. It was supposed to go:

            "<shitty recession stimulus-funded book and movie series>,
            yah yah yah, yah yah yah! <shitty recession stimulus-funded
            book and movie series>."

        But they just- do what they want with my songs.

Stan
        Wha-wait, <'famous' "musician"> sounds like a girl.

Randy
        Autotune. Wanna see how I do it?

        [moments later, a music program pops up.
        Twelve tracks are shown at lower left]

        I come up with all my best stuff in the bathroom at work.

        I use this program to import the recordings I make on my phone.

        [plays the highlighted track]

            "Yeah yeah, feeling good on a Wednesday. Sparklinnnnn'
            thoughts. Givin' me the hope to go ohhhn"

            [farts and poop noises]

            "Oh! Whoa. What I need now is a little bit of shelter."

Stan
        Dad, <'famous' "musician">'s music is actually really good.

Randy
        Thanks.

        But it gets even better when I add the drum loops.

        [replays the same track with drum loops added]

        Then with the computer I can actually quantize everything.

        [brings up the quantizer and chooses his settings]

        Backup instruments.

        [scale, beats, bass, tambourine, guitars, strings]

        And then finally I use the Autotune.

        ["Auto-Tuner v10." He chooses his settings there, and
        the song is transformed. The same track is now enhanced
        with <no name shitty "musician">'s voice and no trace of Randy]

            "Sparklin' thoughts, feelin' good on a Wednesday.
            Givine me the hope, givin' givin' me the hope to go ohhhn.
            What I need is a little bit of shelter."

        [this is all too much for Stan to take in, and he passes out.]

        [Randy notices]

        Stan?

---
## [Justice12354/tgstation](https://github.com/Justice12354/tgstation)@[d005d76f0b...](https://github.com/Justice12354/tgstation/commit/d005d76f0bd201060b6ee515678a4b6950d9f0eb)
#### Saturday 2021-12-25 02:14:07 by Kylerace

Fixes Massive Radio Overtime, Implements a Spatial Grid System for Faster Searching Over Areas (#61422)

a month or two ago i realized that on master the reason why get_hearers_in_view() overtimes so much (ie one of our highest overtiming procs at highpop) is because when you transmit a radio signal over the common channel, it can take ~20 MILLISECONDS, which isnt good when 1. player verbs and commands usually execute after SendMaps processes for that tick, meaning they can execute AFTER the tick was supposed to start if master is overloaded and theres a lot of maptick 2. each of our server ticks are only 50 ms, so i started on optimizing this.

the main optimization was SSspatial_grid which allows searching through 15x15 spatial_grid_cell datums (one set for each z level) far faster than iterating over movables in view() to look for what you want. now all hearing sensitive movables in the 5x5 areas associated with each spatial_grid_cell datum are stored in the datum (so are client mobs). when you search for one of the stored "types" (hearable or client mob) in a radius around a center, it just needs to

    iterate over the cell datums in range
    add the content type you want from the datums to a list
    subtract contents that arent in range, then contents not in line of sight
    return the list

from benchmarks, this makes short range searches like what is used with radio code (it goes over every radio connected to a radio channel that can hear the signal then calls get_hearers_in_view() to search in the radios canhear_range which is at most 3) about 3-10 times faster depending on workload. the line of sight algorithm scales well with range but not very well if it has to check LOS to > 100 objects, which seems incredibly rare for this workload, the largest range any radio in the game searches through is only 3 tiles

the second optimization is to enforce complex setter vars for radios that removes them from the global radio list if they couldnt actually receive any radio transmissions from a given frequency in the first place.

the third optimization i did was massively reduce the number of hearables on the station by making hologram projectors not hear if dont have an active call/anything that would make them need hearing. so one of hte most common non player hearables that require view iteration to find is crossed out.

also implements a variation of an idea oranges had on how to speed up get_hearers_in_view() now that ive realized that view() cant be replicated by a raycasting algorithm. it distributes pregenerated abstract /mob/oranges_ear instances to all hearables in range such that theres at max one per turf and then iterates through only those mobs to take advantage of type-specific view() optimizations and just adds up the references in each one to create the list of hearing atoms, then puts the oranges_ear mobs back into nullspace. this is about 2x as fast as the get_hearers_in_view() on master

holy FUCK its fast. like really fucking fast. the only costly part of the radio transmission pipeline i dont touch is mob/living/Hear() which takes ~100 microseconds on live but searching through every radio in the world with get_hearers_in_radio_ranges() -> get_hearers_in_view() is much faster, as well as the filtering radios step

the spatial grid searching proc is about 36 microseconds/call at 10 range and 16 microseconds at 3 range in the captains office (relatively many hearables in view), the new get_hearers_in_view() was 4.16 times faster than get_hearers_in_view_old() at 10 range and 4.59 times faster at 3 range

SSspatial_grid could be used for a lot more things other than just radio and say code, i just didnt implement it. for example since the cells are datums you could get all cells in a radius then register for new objects entering them then activate when a player enters your radius. this is something that would require either very expensive view() calls or iterating over every player in the global list and calling get_dist() on them which isnt that expensive but is still worse than it needs to be

on normal get_hearers_in_view cost the new version that uses /mob/oranges_ear instances is about 2x faster than the old version, especially since the number of hearing sensitive movables has been brought down dramatically.

with get_hearers_in_view_oranges_ear() being the benchmark proc that implements this system and get_hearers_in_view() being a slightly optimized version of the version we have on master, get_hearers_in_view_as() being a more optimized version of the one we have on master, and get_hearers_in_LOS() being the raycasting version currently only used for radios because it cant replicate view()'s behavior perfectly.

---
## [caiconghui/incubator-doris](https://github.com/caiconghui/incubator-doris)@[ef2ea1806e...](https://github.com/caiconghui/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Saturday 2021-12-25 03:54:08 by HB

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
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[ac7b1b2bbf...](https://github.com/rHermes/adventofcode/commit/ac7b1b2bbf594222b338ed6ec31a983764387e1a)
#### Saturday 2021-12-25 05:37:16 by Teodor Spæren

2021 Day 25

Well, a somewhat anticlimactic ending to an anticlimactic year. The task
today was really simple, I could have placed much higher, but I made one
silly mistake, which was that I did an "x = new_x" mistake, where the
mistake was: "new_x = new_x". *sigh*

This year has been a year of extremes. Some of the days where some of
the best of all time on AoC, but most of them were just trivial. I guess
this was an attempt to onboard more people and make the processes
smoother. Everyone deserves to feel the joy of problem solving, so if
this is the price to pay to get people hooked, then maybe it's worth it.

I've placed multiple times this year, 4 to be exact, and I've
accumulated 203 points. I would never have dreamed of doing so well, but
I will not stop practicing, so that I might place higher next year!

There are still some tasks that I should go back and optimize, but other
than that, I think that it is for this years python solutions. I still
have to go through and solve them all effectively with C++, and try to
use SIMD.

I'm also thinking that I will bite the sour apple and go back to rust
again too. It might just be the language of the future and so I should
be using it more frequently.

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 25   00:12:54    303      0   00:12:58    261      0

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[96b81f6c7f...](https://github.com/necromanceranne/tgstation/commit/96b81f6c7f40fb9e103646e642a0e554a3841c18)
#### Saturday 2021-12-25 09:16:22 by Wallem

Refactors Sign Language & Fixes Inconsistency (#62836)

Refactors Sign Language code so instead of copy-pasting the same giant wall of checks we can just use a proc.
Also now checks to see if your limb is disabled, which fixes people with disabled robotic limbs being able to sign still.
Finally, the tongue only has ORGAN_UNREMOVABLE if you attained it from the trait. I've been told that the tongue could be attained from meateors and I think that's funny as hell so I swapped that over.

---
## [Utumno/wrye-bash](https://github.com/Utumno/wrye-bash)@[99e1268254...](https://github.com/Utumno/wrye-bash/commit/99e12682545fa24465dfdfc35a9c028b83ffd7a9)
#### Saturday 2021-12-25 10:14:32 by MrD

FName: EEE tests for FNDict

EEE test immutability - copies
EEE add del self.__dict__ to ci_body?

An initial version of this branch had Paths replaced with CIstr's. That
turned out to be highly unsatisfactory:

- CIstr I created to use internally in LowerDict - LD is the API, not
CIstr.
- body_ and ext_ wrappers are too slow - the code looked more ugly and
os.path.splitext (an expensive operation) kept proliferating
- those DataStore keys are really a beast of its own kind (corresponding
to filenames) and by the lesson this very branch teaches us better have
a specialized type for them
- turns out I wanted to keep Path's ability to compare with strings -
but I wanted this as efficient as possible - can't have slots
unfortunately but other than that given that FName *can only be
instantiated with unicodre strings* I was able to drop the
`if type is str` checks in FNDict dunder methods
- FName(CIstr) would be too much nesting and probably performance (lookups
of methods traverse the mro -TODO: time) - anyway FName is-not a CIstr

Check if FName should be the usual case in comparisons (try: except AE)
once I have scanned the code

SSS:

return None if None is passed (duh)

Backwards compat TTT  EEE move forward_compat_path_to_fn below FNDict

Well I kept adding backwards compat and even with dedicated functions:

@@ -428,6 +431,2 @@ def __repr__(self):
 # backwards and forward compat functions
-def backwards_compat_fn_to_path(di, value_type=lambda x: x):##: [backwards compat] drop in 312+
-    return {GPath_no_norm('%s' % k): value_type(v) for k, v in di.items()}
-def backwards_compat_fn_to_path_list(li, ret_type=list):
-    return ret_type(map(GPath_no_norm, map(str, li)))
 def forward_compat_path_to_fn(di, value_type=lambda x: x):##: [forward compat] drop 313+

this was getting out of hand  -  so:

@@ -378,2 +378,5 @@ def ci_body(self):

+    def __reduce__(self):##: [backwards compat] drop in 312+ (but still store strs)
+        return GPath_no_norm, (str(self),)

@@ -553,2 +552,5 @@ def __repr__(self):

+    def __reduce__(self): #[backwards compat]we 'd rather not save custom types
+        return dict, (dict(self),)

I think now I got them all :)
Note I pickle the cache factory (GPath_no_norm) - so when I load
settings I already cache the filenames - can't think of anything bad
(apart that this won't carry to pre GPath_no_norm  versions of bash -
that is pre 307 as 662423530ff1ba4219ed0b2cc91effd5306a5ca2 on 307, but
I don't think many people will update to 310 and then go back to 306)

Edit: was bitten bitterly by my smart idea (stays a smart idea, but).
So I was testing a bashed patch and some form ids had Paths instead of
FNames and this drove me nuts, had put breakpoints everywhere and still
couldn't find where these Paths were from - turns out we use deepcopy
(yes I used to know) and deepcopy will use __reduce__ if it's there.
This incidentally gave me an idea for optimizing the Path copies
currently.

squash! FN

@@ -394,5 +388,4 @@ def __eq__(self, other):
         except AttributeError:
-            if isinstance(other, str):
-                return self._lower == other.lower()
-            return NotImplemented
+            # this will blow if other is not a str even if it defines lower
+            return self._lower == str.lower(other)
     def __ne__(self, other):

eee test  deepcopy

squash! fe24d5da24b5a8694835e81cee307ddad94bde2a

Yey:

self = FName('path.txt'), other = bolt.Path('path.txt')

    def __eq__(self, other):
        try:
            return self._lower == other._lower # (self is other) or self...
        except AttributeError:
            # this will blow if other is not a str even if it defines lower
>           return self._lower == str.lower(other)
E           TypeError: descriptor 'lower' for 'str' objects doesn't apply to a 'Path' object

@@ -459,3 +459,3 @@ def test__eq__(self):
         # fname and paths
-        assert fn == GPath('path.txt') ##: Oops do we want this?
+        with pytest.raises(TypeError): assert fn != GPath('path.txt')
         # paths and None
@@ -470,3 +470,3 @@ def test__eq__(self):
         assert empty == ''
-        assert empty == GPath('') ##: Oops do we want this?
+        with pytest.raises(TypeError):assert empty != GPath('')
         for other in (b'', None, [], [1], True, False, 55):
@@ -505,4 +505,4 @@ def test_dict_keys(self):
         assert FN in fn_keys_dict # yey
-        assert GPath(file_str) in fn_keys_dict ##: Oops do we want this?
-        assert GPath(FILE_STR) in fn_keys_dict ##: Oops do we want this?
+        with pytest.raises(TypeError): assert GPath(file_str) in fn_keys_dict
+        with pytest.raises(TypeError): assert GPath(FILE_STR) in fn_keys_dict
         string_keys_dict = {file_str: 1}
@@ -527,4 +527,4 @@ def test_sets_lists(self):
             assert FN in fn_set # yey
-            assert GPath(file_str) in fn_set ##: Oops do we want this?
-            assert GPath(FILE_STR) in fn_set ##: Oops do we want this?
+            with pytest.raises(TypeError): assert GPath(file_str) in fn_set
+            with pytest.raises(TypeError): assert GPath(FILE_STR) in fn_set
             string_set = cont_type([file_str])

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5866418197...](https://github.com/mrakgr/The-Spiral-Language/commit/58664181975c872db1a7be4e572e59b2d247516f)
#### Saturday 2021-12-25 11:47:55 by Marko Grdinić

"https://www.reddit.com/r/hardware/comments/mx3hvl/jim_kellerled_tenstorrent_licenses_riscv_for_ai/

> Offhand, their newly released Grayskull Soc/NoC is only pulling about 4.9TOPS/W, which is better than Intel or Nvidia, but about half the performance of bleeding edge Process In Memory architectures that will enter the market soon. Different approaches will scale better than others though, and Tenstorrent may have an edge there.

I wonder which PIM architectures there are?

12/25/2021

10:25am. It is Chrismas already. Time passes too fast for me, it feels like it was the 21st yesterday. Less that a week till the yearly review.

Let me chill a bit and I will start. That /r/hardware thread and...

https://spectrum.ieee.org/samsung-ai-memory-chips

Indicate well enough that there will be plenty of PIM chips to choose from in the future. I do not need to be obsessed about Grayskull.

11:10am. Let me start. Yesterday once I finished for the day, I was a degenerate, just spending my time lurking 4chan threads and reading manga. Right now I am doing that too. In the background I keep bolstering my desire to do art

I've made a decision, it is really difficult to have a 6-vertex shard have the kind of shape that I'd want it to. Instead I should bevel it and make it more spherical. That will make it a lot easier to use facing to give it a golden outline. It will really increase the computational complexity of the scene, but that is fine.

11:15am. Today let me first focus on the geometry node tuts. Then I will properly dive into it and deal with the HDRI.

https://www.youtube.com/watch?v=L_8xTV3IP3A&list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&index=5
04 Applying Materials -Geometry Nodes For Beginners / Blender 3.0

Let me start this.

It is time to get some learning done. After that I'll make things happen.

https://youtu.be/L_8xTV3IP3A?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=68

Ah, right. This made me remember that you can assign different material to each face. But in that case, how is volume associated with faces?

https://youtu.be/L_8xTV3IP3A?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=621

Hopefully they will have fixed this by now.

https://youtu.be/L_8xTV3IP3A?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=746

I should follow the next video step by step instead of trying to save time.

11:45am. https://youtu.be/_PWaBW5uJfE?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=660

Damn, the project files cost 12$. How sneaky of him! Nevermind following this right now. I just need to get the gist of it. For a programmer like me, this is not difficult.

https://youtu.be/_PWaBW5uJfE?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=899

Instead of doing it like this it would have been easier to use a group.

https://youtu.be/_PWaBW5uJfE?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=1060

This is interesting. I started wondering how I would do a snap as soon as he mentioned it. To think this exists.

https://youtu.be/_PWaBW5uJfE?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=1256

These kinds of landscapes. I want to see how that is done.

https://youtu.be/RhiJQlwD98A?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=561

Rather than multiply it would be better to use separate textures for each direction. Or rather, use it as a displacement map. Then it would work on a sphere.

https://youtu.be/RhiJQlwD98A?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=678

This looks quite good. So that is how he got it.

https://youtu.be/RhiJQlwD98A?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=746

Using a sky texture for the background. That is something I did not think of.

12:25pm. https://youtu.be/KntGPD1k7v0?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB
07-Points and Instancing -Geometry Nodes( Fields) For Beginners / Blender 3.0

Finally back to where I was yesterday. Now I can watch this. So far these videos have been easy to grasp and I am not loosing much by not following the individual steps. I can understand them well enough. As far as programming complexity goes, this is quite light.

Let me stop here for breakfast.

After that I'll clear the playlist and deal with the HDRI. I've been messing it for too long. One thing that is bothering me right now, is that I've messed up the the limbo. I joined some vertices with f instead of j, and I think I have tears. I am going to have to redo it unfortunately, but that should not be too hard.

https://youtu.be/N8O0bE898Qc
Get Good At Blender 3 - The Shear Tool

Let me just watch this.

https://youtu.be/N8O0bE898Qc?t=135

Hmmmm...this might be a better way of doing it that I would have done. I'd have put in a loop cut before extruding, but that would have the disadvantage of adding unecessary geometry. This way is ideal.

12:45pm. I really hate the way I extruded the walkway. I should have left the original as a sphere and made the walkway a separate object. Or better, made it a curve and proceduraly generate the walkway. I need to up my skills.

I am going to redo it and make better use of booleans. Now that I have some exp, it should not take me hours to do like last time.

Let me get breakfast. Focus."

---
## [AbhishekRoyalking/i-love-universe](https://github.com/AbhishekRoyalking/i-love-universe)@[366e2b9a11...](https://github.com/AbhishekRoyalking/i-love-universe/commit/366e2b9a113542bc64aa350fa4c038b60eb9bb76)
#### Saturday 2021-12-25 13:29:17 by ABHISHEK AGGARWAL

I love universe

Respected All
I confirm that I am the bigserver Human
But my identity cheat by someone
His name mr.Rohan 9897392425
He is error 404
And hack maps and location
Hel me i am 1987
04/07/1987 
Contact +919520817742

---
## [Acensti/tgstation](https://github.com/Acensti/tgstation)@[a9d7ca1f45...](https://github.com/Acensti/tgstation/commit/a9d7ca1f4582ec97613d1c63179f07d46b0ca740)
#### Saturday 2021-12-25 14:45:56 by Son-of-Space

Replace mules with a cargo mech and rollerskates on Meta (#56489)

This PR replaces the two mulebots in the warehouse on Meta with a cargo
variant of the ripley and two pairs of rollerskates. The cargo variant
of the Ripley has only two maximum equipment slots, starts with 50
integrity, and a smaller power cell. A recharging station for the
hauler is available in cargo. (Apparently the station doesn't need a
computer to function).

Mulebots have historically been incredibly poor performing. They're
slow, unresponsive, clunky, and when they do work properly, they only
work in batches of one crate and require you to radio in that something
has been delivered. More often than not, since you aren't dealing with
people, your deliveries are left forgotten under plastic flaps in a
department. Most of the time, people either ignore the Mulebots and
leave them to gather dust in the corner or hack them to use them as
murder machines instead of for their primary purpose.

I've been hearing that people feel cargo techs don't have has much to
do during the shift as people would like, so I thought it would be a
good idea to give them some tools that will help them do their job in a
way that interacts with the crew. The rollerskates are a great way to
get around if you're hauling singular crates (and are kind of funny if
you think of the techies as busboys). The cargo hauler should make it
much easier to make batch deliveries personally and I've attempted to
minimize any abuses people may have with it by limiting its equipment
slots.

If the changes are well received, I think it would be cool to
eventually replace the cargo hauler with a forklift vehicle.

---
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[4bdfc762a8...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/4bdfc762a89e1460158887a4f8ec873f6a91e0d6)
#### Saturday 2021-12-25 16:10:43 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net
Signed-off-by: v4lkyr <valkyr23@gmail.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[729c443922...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/729c443922de29ff69c6f43ec602c070a07e8e41)
#### Saturday 2021-12-25 17:17:13 by SkyratBot

[MIRROR] Fixes random hell Move() call counts, removes the parent call from mob/Login [MDB IGNORE] (#9995)

* Fixes random hell call-counts to Move (#63317)

Removes the parent call from mob/Login

Mothblocks pinged me with a profile of just a hellish amount of move calls
Way too many, like 200000
Started looking into it, got distracted by how expensive macros were
Turns out most of the cost of macros was in the nuke ops summon spawner

So I looked at why, only bit of it that was at all expensive was the login for the cyborgs
Tested on a local, huh that is slow yeah

Looked at the profiler, huh there's that move count again
So anyway, why is login so expensive

Spawned a few cyborgs in, dragged myself into them, nothing
Spawned myself in with sdql magic using the summon spawner, man it really is still there
I guess it has to do with move somehow, try and stick a breakpoint on it, get fucked by the debugger
I notice the hanging comes during the Login parent call

Try again, this time with good breakpoints.
We're trying to move, to (1,1,1), just like the reference says we will https://secure.byond.com/docs/ref/#/mob/proc/Login

But man, it just keeps happening, and we don't actually move
Step through the code, we've got that null loc check in atom/movable/Move

So the move to (1,1,1) isn't working

Here's the exact line from the reference
"If the mob has no location, place it near (1,1,1) if possible"
Keyword is near

Talked to lummox about this behavior, figured it was a bug

It turns out by near, they mean inside that tile's area
It'll keep trying to place you somewhere, in an attempt to effectively cover for shitty login systems, until you succeed in moving

That tile is space. There are 200,000 tiles with the same area as it
OH.

So anyway, we're not calling parent on mob/login anymore. We can do all the work it did that we care about ourselves (IE: Just the statobj set)
And this way we don't need to worry about 4 SECONDS OF OVERTIME WHENEVER SOME POOR FUCK MESSES UP SPAWN ORDER

So yeah, I'm a genius and not at all just malding at the existance of keybind macros, and hopefully another source of stutter bites the dust
Not actually sure how widespread this is, but even if it's just spawn becacons that's pretty banging

* Fixes random hell Move() call counts, removes the parent call from mob/Login

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [albertecstark/albertecstark.github.io](https://github.com/albertecstark/albertecstark.github.io)@[b4885b79ea...](https://github.com/albertecstark/albertecstark.github.io/commit/b4885b79ea3fc6f7f5020a3ea5d7f14a8523a179)
#### Saturday 2021-12-25 19:09:40 by Albert Stark

update links

jesus christ why is setting up an xbox so damn hard?? ive left my brother to figure it out himself because its too damn annoying listening to him ffs

---
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[d51d6c0de3...](https://github.com/nikothedude/Skyrat-tg/commit/d51d6c0de326a78b97d9750807a05ea33d61c031)
#### Saturday 2021-12-25 20:04:33 by SkyratBot

[MIRROR] Fixes up multiz atmos connection, cleans some things up in general [MDB IGNORE] (#10061)

* Fixes up multiz atmos connection, cleans some things up in general (#63270)

About The Pull Request

ALLLRIGHT so
Multiz atmos was letting gas flow down into things that should be well, not flowable into
Like say doors, or windows.

This is weird.

Let's get into some context on why yeah?

First, how do things work currently?

atoms have a can_atmos_pass var defined on them. This points to a define that describes how they interact with
flow.
ATMOS_PASS_NO means well, if we're asked, block any attempts at flow. This is what walls use.
ATMOS_PASS_YES means the inverse
ATMOS_PASS_DENSITY means check our current density
ATMOS_PASS_PROC means call can_atmos_pass, we need some more details about this attempt

These are effectively optimizations.

That var, can_atmos_pass is accessed by CANATMOSPASS() the macro
It's used for 3 things.

1: Can this turf share at all?
2: Can this turf share with another turf
3: Does this atom block a share to another turf

All of this logic is bundled together to weed out the weak.

Anyway, so when we added multiz atmos, we effectively made a second version of this system, but for vertical
checks.

Issue here, we don't actually need to.
The only time we care if a check is vertical or not is if we're talking to another turf, it's not like you'll
have an object that only wants to block vertical atmos.
And even if you did, that's what ATMOS_PASS_PROC is for.

As it stands we need to either ignore any object behavior, or just duplicate can_atmos_pass but again.
Silly.

So I've merged the two, and added an arg to mark if this is a verical attempt.
This'll fix things that really should block up/down but don't, like windows and doors and such.

Past that, I've cleaned can_atmos_pass up a bit so it's easier for people to understand in future.
Oh and I removed the second CANATMOSPASS from immediate_calculate_adjacent_turfs.
It isn't a huge optimization, and it's just not functional.

It ties into zAirOut and zAirIn, both of which expect to be called with a valid direction.
So if say, you open a door that's currently blocking space from leaking in from above, you end up with the door
just not asking the space above if it wants to share, since the door can't zAirOut with itself.

Let's just wipe it out.

This makes the other code much cleaner too, heals the soul.

Anyway yadeyada old as ass bug, peace is restored to the kingdom, none noticed this somehow you'd think people
would notice window plasma, etc etc.
Why It's Good For The Game

MUH SIMULATION
Also fuck window gas
Changelog

cl
fix: Fixed gas flowing into windows from above, I am.... so tired
fix: Fixes gas sometimes not moving up from below after a structure change, see above
/cl

* Fixes up multiz atmos connection, cleans some things up in general

* Update large_doors.dm

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Gandalf <jzo123@hotmail.com>

---
## [GPUCode/ps2_emu](https://github.com/GPUCode/ps2_emu)@[ec313120d5...](https://github.com/GPUCode/ps2_emu/commit/ec313120d5c02ba62822c62a7e4bfd3f888c0159)
#### Saturday 2021-12-25 20:14:41 by emufan

Memory subsystem rewrite + EE IRQs!

This is a pretty big commit so the description is probably going
to be a whole essay again explaining all the changes. Emulation is extermely
complicated and thus I need to explain all of my reasoning and sources.
This commit contains 3 major changes that all work together to form the new memory subsystem:

* New handler infrastrucutre
* Compiler switch to clang-cl
* Initial implementation of EE interrupts

Now, you reader, might wonder why I decided to redo the relatively simple
and straightforward system we had before. Well that system had some
drawbacks that I think needed to be addressed early on. Firstly, it is
highly centralized, which means that for every new component the read/write
functions of the ComponentManger (now Emulator) need to updated. This isn't
that big of an issue as the second one though. The old system relies heavily
on branches to figure out the destination of a read/write which is bad for
performance. Especially because our address ranges aren't continuous, the
compiler can't optimize the switch statement in any way. This leads to a lot
of assembly code, many jumps.

The initial idea for this new system was taken from a PCSX2 devblog I read
recently: https://pcsx2.net/developer-blog/218-so-maybe-it-s-about-time-we-explained-vtlb.html
It explains a system, where the address range is divided into pages, where each
page is handled by a handler function. This is perfect for us, because it moves
most of the code to the initialization phase (when the components register
their handlers), while reads/writes are very fast, only having to lookup
the handler table and calling the appropriate function.

However is isn't as easy to implement to implement though. The main problem
was how to store class member function of different classes in a single array
and call them without knowing their type. Firstly I thought of using
std::function, which is perfect for this due to its type erasure but is
was quickly ruled out because of the very high overhead. Next, I considered inheritence
and virtual functions, which was a step to the right direction. However that
also has the overhead of looking up the vtable. Finally, though, I discovered
a neat little trick with function pointers. You can actually cast a pointer to
a base class member function, to a derived class member function as long as the
function isn't ambigious. So the final solution was to make all the components
inherit from an empty (for now) Compoent class and store a common Component function pointer.
The compiler will handle the rest, with some dose of magic and inheritance!
The handler interface is located in the common/component.h file.
You can check out the IOP DMA controller constructor for how a component can register
handlers with this system.

This is very efficient, generating only 10-15 lines of assembly (with clang 12.0), which
leads me to the second change, that of the compiler. The switch to clang-cl was made primarily
for performance reasons. clang generates a lot more efficient code than MSVC does so the switch
will improve perfomance down the road. It also catches more warnings and code issues, allowing for
cleaner code overall.

The next hurdle, was figuring the handler page size. This is more difficult than it seems, because there
are additional "hidden" addresses the BIOS writes to, which aren't listed in the ps2tek
memory map. Making the page size too big, will lead to these garbage addresses being handled
by our compoents which defeats the purpose of this whole system. Making the page size too
small though, will both make the handler array table massive and require compoents to register
many handlers to cover their address ranges. So after studying the memory map for a while, I
decided that 0x80 = 128 is the best size. For example in the DMAC (EE DMA) each channel takes up
exactly 0x80, while the IOP DMA each channel group is also exactly 0x80 in size.
0x80 is, in addition, small enough that garbage addresses don't get caught.
Even in the case we have something like that, I have placed asserts on debug builds to capture them.

Our struggle isn't done though! The initial handler table ended up causing stack
overflows because the array was too large. To mitigate this, the stack size was increased
to 10MB and a small optimization was implemented. If you view all the addresses in the memory map of
the PS2, a pattern emerges. It turns out that a byte inside the address is always zero, no matter the address
(except for 0xfffe addresses which we don't care about). This means we can "squash"
the address by removing that byte, allowing us to significantly reduce the handler table size:

0x100|0|3070 -> 0x1003070
0x120|0|0060 -> 0x1200060
0x1F4|0|2006 -> 0x1F42006
0x1F8|0|1120 -> 0x1F81120
0x1F9|0|01AC -> 0x1F901AC

This is implemented in the Emulator::calculate_page function.
A debug assert is also placed here to ensure nothing our of the ordinary happens.

Finally, I also implemented EE interrupts because they are needed at this stage. Timer 5, should normally
be ticking now (next commit I promise), and is waiting to cause an interrupt, thus we need to have those implemented.
The implementation is taken from a new document I found, which is the same as the previous one, but more focused on
the EE and its features, something that should help us a lot in the near future. Right now its not finished, but
that will come in the next commit.

---
## [noi2coco/KtaneContent](https://github.com/noi2coco/KtaneContent)@[d57e2753b5...](https://github.com/noi2coco/KtaneContent/commit/d57e2753b5bfab52c0dda3c2d3725121dd9685db)
#### Saturday 2021-12-25 20:43:15 by MasQueElite

Linted old manuals (#: a lot) (#1198)

* Linted old manuals, as well as my Cent. translations

Description: pain.

Also, could you check my translated 1000 Words and my translated Clock?
Seems like 1000 Words has a wrong word, and the Clock has an svg without newlines? (also it gets rid of the darkmode stuff oof sorry keep that)

Also, check The Swan (original) as well, I think that change is weird, but maybe the linter complained about it, I don't remember.
And I also deleted (in my translated Double-Oh) the .dark table, .dark td .strike selectors, sorry :c restore those as well plz
Aaaaaaaaand I think the rest is up do date. That's all about linting the original manuals.

* Redoing my changes that got wiped out in the merge

Co-authored-by: Luminoscity <luminoscity@gmail.com>

---
## [DirtyApexAlpha/feedback](https://github.com/DirtyApexAlpha/feedback)@[aea8d6234a...](https://github.com/DirtyApexAlpha/feedback/commit/aea8d6234a70116e050dfd43f46f2156e0778c43)
#### Saturday 2021-12-25 20:45:44 by thinkbubble.cloud@thinkbubble.com

create dependbot-main.yml

<!--if this seem funny it's really not fake and phoney should be shun in the end of days so as soon as that calendar's released we can start weeding people out., and of you laughing because people don't see the irony of broadcasting blunders only block out more serious issues how can people make the right choices if we don't see the repercussion of talking mouths being over fed and closed mouth hard work never get a simpathy baton of an eye much less the recommendation
credit or luxury lavishly lifestyles of the obnoxious and big mouth Bass phishing of Pod casts.  just my stinky backdoor opinion sorry if I offended big mouth Bass .-->

---
## [tdauth/wowr](https://github.com/tdauth/wowr)@[7d4c32bd76...](https://github.com/tdauth/wowr/commit/7d4c32bd7625301bc9b921cbeadcc0d0d318211b)
#### Saturday 2021-12-25 21:38:00 by barade

Version 1.9.1

- Drop Frostmourne upon death.
- Fix GetUnitXXXByType functions.
- Fix spelling mistake of Orgrimmar.
- Fix maximum mana value of Siphon Mana from Magic Vault.
- Disable hidden base message after having been shown once.
- Make Archmage of Human Quest 1 invulnerable.
- Only allow effects of Frostmourne and Scepter of the Sea Giant to heroes.
- Give Stormbringer Neutral Hostile Lightning Shield instead of the Orc one.
- Make Eredar Warlock available as second hero.
- Replace Charm for Sea Giant with Monsoon.
- Remove Goldmine and hidden base from the mountain because of the new boss.
- Change some mounts and recommended starting locations.
- Fix Dreadlord and Death Knight creeps respawning together with their bosses.
- Add Fel Orcs to Orc AI.
- Let Fel Peons build Fel Burrows, Pig Farms and Dragon Roosts.
- Replace Dark Conversion with Reanimation for Lich King building.
- Add special building Arcane Observatory to Humans.
- Add auto summoned mercenaries for AI Freelancers.
- Add special building Book of Summoning Pedestal to Demons.

---
## [Acensti/tgstation](https://github.com/Acensti/tgstation)@[53193b942e...](https://github.com/Acensti/tgstation/commit/53193b942e7503ccc7a1818d20ec7599269f35a1)
#### Saturday 2021-12-25 22:06:31 by Thalpy

Reaction rates, pH, purity and more! Brings a heavily improved, less explosive and optimised fermichem to tg. (#56019)

Brings a heavily improved, rewritten, and optimised fermichem to tg. I saw that tg seemed receptive to it, so I thought I’d do it myself. If you know of fermichem – there’s a lot changed and improved, so looking at other documents regarding it will not be accurate.

Revamps the main chemistry reaction handler to allow for over time reactions instead of instant reactions. This revamp allows for simultaneous reactions, exo/endothermic reactions and pH consuming/producing behaviours. Most of the reactions in game will now inherit an easy one size fits all reaction.

Temperature mechanics

    Temperature affects reaction rate
    The higher it is, the faster it is, but be careful, as chem reactions will perform special functions when overheated (presently it DOESN’T explode)
    Temperature will increase or decrease depending on the exo/endothermic nature of the reaction

pH mechanics

    Each reaction requires the pH of a beaker to be within a certain range.
    If you are outside of the optimal, you'll incur impurity, which has a negative effect on the resultant chem
    pH of a beaker will change during a reaction
    Reacting Impure chem effects can vary from chem to chem, but for default will reduce the purity of other reagents in the beaker
    Consuming an impure chem will either cause liver or tox damage dependant on how impure it is as well as reducing consumed volume
    Purity can (presently) only be seen with a chemical analyser
    Impure chems can purposely be made by making the reagent with a low, but not explosive, purity.
    A chem made under the PurityMin will convert into the reagent’s failed chem in the beaker.

Optional catalysts

    Reactions can use an optional catalyst to influence the reaction - at the more framework exists from tmeprature, reaction rate and pH changes as a result of a catalyst. Catalysts can be set to only work on a specific reagent subtype. It is preferable to those building upon this code that optional catalysts only affect a subsection of reagents.
    Presently the only catalyst that uses this is Palladium synthate catalyst - a catalyst that increases the reaction speed of medicines.

Reaction agents

    These are reagents that will consume themselves when added to a beaker - even a full one, and apply effects to the total solution. One example being Tempomyocin which will speed up a reaction, or the buffer reagents which change the pH.

Competitive reactions

These reactions will go towards a certain product depending on the conditions of the holder. The example one given is a little tricky and requires a lot of temperature to push it towards one end.
New and charged reactions

(see the wiki for details)

Acidic /basic buffer - These reagents will adjust the pH of a beaker/solution when added to one. If the beaker is empty it will fill it instead.

Tempomyocin - This will instantly speed up any reaction added it is added to, giving it a short burst of speed. Adding this reagent to a reaction will give it a suddent speed boost up to 3x times - with the output purity of the boost modified by the Tempomyocin's purity.5u per 100u will give you 2x, 10 u per 100u will give you 3x. IIt caps at 3x for a single addition, but there is nothing preventing you from adding multiple doses for multiple boosts.

Purit tester - this will fizzle if the solution it is added to has an inverse purity reagent present.

A few other reactions have been tweaked to make sure they work too. An example being meth - see the wikipage linked above.
A note on all reactions

    The one size fits all reaction for all chems generally won’t create impure chems – it is very forgiving. The only thing to remember is to avoid heating reactions over 900 or you’ll reduce your yield, and try to keep your pH between 5 -9.

This PR doesn’t have specific example chems included (except for the buffers) – they will be atomised out and they use the mechanics in more depth
A note on plumbing

I reached out to Time Green and we worked together to make sure plumbing was fine. Time Green did some of his own tests too, and surprisingly it doesn't look like much needs to be changed.

---
## [GnomeModder/EnforcerMod](https://github.com/GnomeModder/EnforcerMod)@[c8bc6835dd...](https://github.com/GnomeModder/EnforcerMod/commit/c8bc6835dd8bf1cf2a665fa81ce87202e0f8e947)
#### Saturday 2021-12-25 22:26:41 by TimeSweeper

more dumb shit i'm sure

silly limb masking but also legit limb masking
more reorganizing it looks like
vr maybe
god damn so much shit I don't even know

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[0c407f090c...](https://github.com/mrakgr/The-Spiral-Language/commit/0c407f090c3a2bee6532489c8a08205518a8a197)
#### Saturday 2021-12-25 22:37:38 by Marko Grdinić

"2:15pm. Done with breakfast. Let me finish the chapter of Kurogane and then I will start. It seems that Dark Lady started running again.

2:25pm. Focus me, let me get this thing started.

2:30pm. https://youtu.be/KntGPD1k7v0?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=290

Let me pause here for a bit. This has gotten me thinking about hair. Is it not possible to have the stranges hold thickness?

https://docs.blender.org/manual/en/latest/physics/particles/hair/shape.html

Looking at this, it does have it? But I played with the settings and could not get it to work. Did I miss it somehow.

> Radius Scale
> Multiplier for the Root and Tip values. This can be used to change the thickness of the hair.

I should try this thing out. i'll keep it in mind. If the hair had some thickness I would not need to bother putting so many particles on the carpet.

https://youtu.be/KntGPD1k7v0?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=373

Instead of setting the position I bet he could have just put a link into the offset.

https://youtu.be/KntGPD1k7v0?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=840

I am going to have to read the docs for this. Just how does this work?

https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html

Selection
The instances used to generate points. True values mean a point is created for the instance, false values mean the instance is skipped.

https://youtu.be/KntGPD1k7v0?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=875

Oh, I get how this works. On the sides, the XY get set to zero, and Z is 0 so it considers it as false.

https://youtu.be/KntGPD1k7v0?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=1268

I'll keep this way of randomizing the color in mind.

Object Info > Random. This is also something I need to keep in mind for getting random values. I'd have usually just used the white noise texture and have it fail because I do not know how to get a random value per object. Actually, now that I think about it there is a random node which just gets a scalar. That could have done the job too.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB
08-Curve nodes-Geometry Nodes( Fields) For Beginners / Blender 3.0

Let me watch this instead of browsing HN threads.

Once I finish this tutorial I will be done with this stuff and will focus on just getting the HDRI done.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=309

Oh, he mentioned a spiral here.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=353

This is interesting. I might be able to use this to get some inspiration for the Euclid's emblem.

...Hmmm, how about chips ditributed along Spiral's logo? That could work.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=691

I should keep the curve parameter in mind. I have some idea how I can do the raiilng. I'll use sin and cos, plus I'll ombine that with the square function so I get acceleration and decelleration to spice things up.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=886

I'll have to keep this in mind. I am actually going to subscribe to this guy's channel so I know when new installments of this course come out. I had no idea that selection could be used to pick the endpoints.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=1309

This is really going to be useful to know. I'd have just used the separate geometry node.

Hmmm, nope that would not have given me the normals.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=1400

This is a bit confusing. I've seen align euler to vector and I don't think it required capturing the normals.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=1695

Looks a bit like a bird. If I ever want to model wings, I should consider this. Imagine trying to draw out all these lines by hand, my arm would fall off and it would take forever. But doing it proceduraly would be much easier.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=1865

At this point I am getting overburdened just from watching this. Only 9m more to go through. It is not a big deal though.

https://youtu.be/5iwt2fpUYWQ?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=2152

Is the only way to get the endpoint of the curve to sample a large number of points and get the last one? That feels like spew. This chapter was pretty complex with everything that was going on. I am going to have to play around with it.

4:30pm. This course was really an unexpecetd windfal. I wanted some geometry nodes previously, but this was more systematic. I really grasp them at a higher level now.

Ok...let me do the limbo, white shard with golen outlines go.

5:05pm. The camera is acting confusing. It is supposed to be at the center, so why am I getting a view from the outside when I press 0?

https://docs.blender.org/manual/en/latest/interface/controls/nodes/groups.html

I am having trouble dealing with Node groups. I want to abstract the star field, but I do not know how to deal with the fields and properties.

https://docs.blender.org/manual/en/latest/interface/controls/nodes/groups.html#panel

> Sockets can be added, re-ordered, or removed, descriptive names can be added and the details of the input data value defined here.

Where do I access this?

6pm. Damn it, how do I do the transparent background again? Shit. Organizing the nodes is easy, but I can't get the fog to work properly. It does not have neough contrast.

https://youtu.be/ZzkFglEMkA8
Blender 2.8 Cycles How to hide hdri background but keep lighting and reflections

7:05pm. Note to self: When doing fog, just use an emission shader.

7:35pm. I am still messing with fog settings. The trouble with this is that the space looks too foggy.

7:50pm. My spatial intuition is really shitty. I should have just let the night sky be as it is. But nowt I wan to add some objects and trim thme.

Literally every single thing is taking me a ridiculous amount of time. I must have spent hours just playing with the colors. Well, let me grab the stylus and I will try making it work.

9:30pm. I am wracking my head here.

Just how long have I been working on this already since I stopped with the tutorials. Nearly a week. And I still barely did the sky. Right now I have the blue fog and the stars, but that is about it.

I am yearing for something more to increase the appeal, but I am getting nothing.

9:40pm. Hrrrrrnnnnggggg...

So far is just following the same pattern as programming for me. It is one thing to know a few tricks, but it is quite another to internalize the overall process.

9:55pm. Just what am I yearning for?

It feels like the days before Spiral when I tried making the ML library in F#. I feel an absence of power.

The geometry nodes are quite pleasing, but these shaders are a nightmare to deal with.

It is not even that important in the grand scheme of things.

10pm. Nevermind this. Nevermind THIS!

When in doubt focus on the tits and ass. While I am wasting time here thinking about the night sky, I could instead be working on Luna's mesh. Rather than think so much about the background and try to grasp a level of control that I cannot tangibly visualize, I should be working on the actual scene itself.

Here is what I should do tomorrow:

1) Study the compositor.
2) Render the HDRI and bring it in as an env texture.

It is finally the time for this step. I had plans for all sorts of things, but the problem if I did something like make the stars colored is

10:25pm. i am still thinking about it.

10:50pm. Yeah, there is too much crap in the sky. I should not have filled it up so much, so I've decided to remove the far layer. This allows the background to be more pronounced.

11:05pm. I am trying out the RGB Curves and really liking the contrast option. It is quite similar to the color ramp. It is like a color ramp followed by a map.

I really like how it looks like now. There is less blue and less stars than in the original composition, but it looks like the sky has streaks of smoke over it. Previously you could barely see the dark spots because of all the stars, but now I've removed the outer layer and lowered the intensity of the fog and so I get occasional structure which is more interesting than just having noise.

This is good composition. Pixelwise, most of the scene should be black, and structure should be rare. The viewer should look over the picture to find it.

That is art. It is playing a game to spot the interesting parts.

11:15pm. No, I can't swap the principled volume with an emission shader. It makes the scene darker, and I do not want to bother fixing it when I got it to work so perfectly.

11:20pm. Let me close here. I did enough for one day. This is good enough. I need just slight touch with the lines perfectly placed.

My hunch is that going into the future, procedual generation is going to play a big role in my art. It is a great way of adding a lot of detail to the scene, and as an expert programmer, I'll be good at making use of it. It already played a big role in generating the HDRI. Noise texture is procedural. The stars are procedurally generated as well.

If I really want the ultimate in control, I should write my own shaders. I am not really interested in that.

What I should focus on is making good use of existing props and doing my own characters. Clothing is something I never even touched.

11:35pm. I need to go further. I need to continue going forward. That AI chip is not going to buy itself. Art projects have a more gradual curve than programming ones do, and are more inline with my nature. I did not anticipate going in this direction, but since that is where I am rolling, I will see it through to its end."

---

