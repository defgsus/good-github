## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-27](docs/good-messages/2022/2022-01-27.md)


1,701,862 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,701,862 were push events containing 2,717,396 commit messages that amount to 213,656,092 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [MickTheRus/MickTitus](https://github.com/MickTheRus/MickTitus)@[e1db777ffa...](https://github.com/MickTheRus/MickTitus/commit/e1db777ffa6491f194dc7a59d0f3cefa84cd3fe2)
#### Thursday 2022-01-27 00:14:49 by Mick Romanchenko

I do not even know what the fuck is going in this gay ass script but what I do know is that I do not store passwords in a setup.conf file that's for damn sure

---
## [RTEMS/sourceware-mirror-binutils-gdb](https://github.com/RTEMS/sourceware-mirror-binutils-gdb)@[bbea680797...](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/bbea68079781ac4c2fc941867ee9888585cafb77)
#### Thursday 2022-01-27 00:23:14 by Andrew Burgess

gdb/python: improve the auto help text for gdb.Parameter

This commit attempts to improve the help text that is generated for
gdb.Parameter objects when the user fails to provide their own
documentation.

Documentation for a gdb.Parameter is currently pulled from two
sources: the class documentation string, and the set_doc/show_doc
class attributes.  Thus, a fully documented parameter might look like
this:

  class Param_All (gdb.Parameter):
     """This is the class documentation string."""

     show_doc = "Show the state of this parameter"
     set_doc = "Set the state of this parameter"

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_All, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_All ('param-all')

Then in GDB we see this:

  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

Which is fine.  But, if the user skips both of the documentation parts
like this:

  class Param_None (gdb.Parameter):

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_None, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_None ('param-none')

Now in GDB we see this:

  (gdb) help set param-none
  This command is not documented.
  This command is not documented.

That's not great, the duplicated text looks a bit weird.  If we drop
different parts we get different results.  Here's what we get if the
user drops the set_doc and show_doc attributes:

  (gdb) help set param-doc
  This command is not documented.
  This is the class documentation string.

That kind of sucks, we say it's undocumented, then proceed to print
the documentation.  Finally, if we drop the class documentation but
keep the set_doc and show_doc:

  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

That seems OK.

So, I think there's room for improvement.

With this patch, for the four cases above we now see this:

  # All values provided by the user, no change in this case:
  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

  # Nothing provided by the user, the first string is now different:
  (gdb) help set param-none
  Set the current value of 'param-none'.
  This command is not documented.

  # Only the class documentation is provided, the first string is
  # changed as in the previous case:
  (gdb) help set param-doc
  Set the current value of 'param-doc'.
  This is the class documentation string.

  # Only the set_doc and show_doc are provided, this case is unchanged
  # from before the patch:
  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

The one place where this change might be considered a negative is when
dealing with prefix commands.  If we create a prefix command but don't
supply the set_doc / show_doc strings, then this is what we saw before
my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- This command is not documented.
  ... snip ...

And after my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- Set the current value of 'print param-none'.
  ... snip ...

This seems slightly less helpful than before, but I don't think its
terrible.

Additionally, I've changed what we print when the get_show_string
method is not provided in Python.

Back when gdb.Parameter was first added to GDB, we didn't provide a
show function when registering the internal command object within
GDB.  As a result, GDB would make use of its "magic" mangling of the
show_doc string to create a sentence that would display the current
value (see deprecated_show_value_hack in cli/cli-setshow.c).

However, when we added support for the get_show_string method to
gdb.Parameter, there was an attempt to maintain backward compatibility
by displaying the show_doc string with the current value appended, see
get_show_value in py-param.c.  Unfortunately, this isn't anywhere
close to what deprecated_show_value_hack does, and the results are
pretty poor, for example, this is GDB before my patch:

  (gdb) show param-none
  This command is not documented. off

I think we can all agree that this is pretty bad.

After my patch, we how show this:

  (gdb) show param-none
  The current value of 'param-none' is "off".

Which at least is a real sentence, even if it's not very informative.

This patch does change the way that the Python API behaves slightly,
but only in the cases when the user has missed providing GDB with some
information.  In most cases I think the new behaviour is a lot better,
there's the one case (noted above) which is a bit iffy, but I think is
still OK.

I've updated the existing gdb.python/py-parameter.exp test to cover
the modified behaviour.

Finally, I've updated the documentation to (I hope) make it clearer
how the various bits of help text come together.

---
## [RTEMS/sourceware-mirror-binutils-gdb](https://github.com/RTEMS/sourceware-mirror-binutils-gdb)@[299953ca95...](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/299953ca95cc5ac47e52236e2eeb44afc5369134)
#### Thursday 2022-01-27 00:23:14 by Andrew Burgess

gdb/python: handle non utf-8 characters when source highlighting

This commit adds support for source files that contain non utf-8
characters when performing source styling using the Python pygments
package.  This does not change the behaviour of GDB when the GNU
Source Highlight library is used.

For the following problem description, assume that either GDB is built
without GNU Source Highlight support, of that this has been disabled
using 'maintenance set gnu-source-highlight enabled off'.

The initial problem reported was that a source file containing non
utf-8 characters would cause GDB to print a Python exception, and then
display the source without styling, e.g.:

  Python Exception <class 'UnicodeDecodeError'>: 'utf-8' codec can't decode byte 0xc0 in position 142: invalid start byte
  /* Source code here, without styling...  */

Further, as the user steps through different source files, each time
the problematic source file was evicted from the source cache, and
then later reloaded, the exception would be printed again.

Finally, this problem is only present when using Python 3, this issue
is not present for Python 2.

What makes this especially frustrating is that GDB can clearly print
the source file contents, they're right there...  If we disable
styling completely, or make use of the GNU Source Highlight library,
then everything is fine.  So why is there an error when we try to
apply styling using Python?

The problem is the use of PyString_FromString (which is an alias for
PyUnicode_FromString in Python 3), this function converts a C string
into a either a Unicode object (Py3) or a str object (Py2).  For
Python 2 there is no unicode encoding performed during this function
call, but for Python 3 the input is assumed to be a uft-8 encoding
string for the purpose of the conversion.  And here of course, is the
problem, if the source file contains non utf-8 characters, then it
should not be treated as utf-8, but that's what we do, and that's why
we get an error.

My first thought when looking at this was to spot when the
PyString_FromString call failed with a UnicodeDecodeError and silently
ignore the error.  This would mean that GDB would print the source
without styling, but would also avoid the annoying exception message.

However, I also make use of `pygmentize`, a command line wrapper
around the Python pygments module, which I use to apply syntax
highlighting in the output of `less`.  And this command line wrapper
is quite happy to syntax highlight my source file that contains non
utf-8 characters, so it feels like the problem should be solvable.

It turns out that inside the pygments module there is already support
for guessing the encoding of the incoming file content, if the
incoming content is not already a Unicode string.  This is what
happens for Python 2 where the incoming content is of `str` type.

We could try and make GDB smarter when it comes to converting C
strings into Python Unicode objects; this would probably require us to
just try a couple of different encoding schemes rather than just
giving up after utf-8.

However, I figure, why bother?  The pygments module already does this
for us, and the colorize API is not part of the documented external
API of GDB.  So, why not just change the colorize API, instead of the
content being a Unicode string (for Python 3), lets just make the
content be a bytes object.  The pygments module can then take
responsibility for guessing the encoding.

So, currently, the colorize API receives a unicode object, and returns
a unicode object.  I propose that the colorize API receive a bytes
object, and return a bytes object.

---
## [TheOnlySolitaire/fulpstation](https://github.com/TheOnlySolitaire/fulpstation)@[c449fbb56c...](https://github.com/TheOnlySolitaire/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Thursday 2022-01-27 00:30:14 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [EwoutH/setup-nasm](https://github.com/EwoutH/setup-nasm)@[6d7e8520e1...](https://github.com/EwoutH/setup-nasm/commit/6d7e8520e18d809c0f1d40f43a2064f80fffb912)
#### Thursday 2022-01-27 00:58:22 by Alexei Lozovsky

Download nasm source tarballs instead of ZIP archives (#10)

ZIP archives use DOS line endings while tarballs have UNIX line endings.
Autotools, and shell, and other stuff on UNIX systems like Linux and
macOS break down when they encounter DOS line endings. We used to work
around that by converting some files into UNIX line endings (while
keeping everything else using DOS). However, with latest versions of
nasm even more files need to be converted. This is painful to track.

Instead, let's just download tarballs with UNIX line endings in them in
the first place. I don't really remember why ZIPs have been used instead
of tarballs. I guess because we already needed ZIP for prebuilt binaries
(which are *not* available in tarballs), and I did not want to mess with
yet another dependency. Well, it's not the case now.

Add a "tar-fs" module to deal with tarballs. "node-fetch" will gunzip
them during the download but we still need to extract the results into
filesystem. Popping dependencies like candies, yay for Node.js!

Note that tarballs have a bit different structure -- a proper one --
with all files stored inside a directory. Also note that I have zero
clues about writing proper JavaScript code with async/await and I used
evolutionary programming to write this code. It works. I'm fine with it.

Source builds are not supported on Windows, but I guess if they did
work, they would not have trouble dealing with UNIX line endings there.

---
## [karanbirsingh/accessibility-insights-web](https://github.com/karanbirsingh/accessibility-insights-web)@[60a93ded2b...](https://github.com/karanbirsingh/accessibility-insights-web/commit/60a93ded2b227455a1fc794a2fa0ef1735a2c200)
#### Thursday 2022-01-27 01:01:54 by Dan Bjorge

fix(tabstops-report): enable hover/focus highlighting on tab stops requirement rows (#5111)

#### Details

This PR enables the Details View > Fast Pass > Tab Stops' new Requirements table to use Office Fabric's default on-hover/on-focus styling that darkens the row backgrounds, to be consistent with the similar behavior in the similar looking Assisted Instance tables in Assessment.

The implementation for this is a little more complicated than expected. The on-hover/on-focus behavior is actually the default fabric behavior; Assessment doesn't do anything special to enable it. The reason we weren't seeing it in FastPass was that we were previously using a very hacky bit of CSS to override the background of the Fabric `DetailsView` to match the slightly-darker-than-usual-gray background we use in FastPass pages (it's different from Assessment to support Cards-based views that want to use our "normal" white background color for Card backgrounds):

```scss
.requirement-table {
    // ...
    * {
        background-color: $neutral-2;
    }
}
```

This was used because the fabric `DetailsView` contains many implementation-detail subcomponents (for rows, cells, headers, etc) that each individually apply overlapping background-color styles; if you just apply background-color to our containing `requirement-table` class, it doesn't have any effect on its own. However, this also has the effect of overriding all of the `:hover` and `:focus` styling under the table.

I originally tried using various combinations of `:not(:focus):not(:hover)` styles, but it rapidly devolved into a big mess of very hacky CSS. Instead, this PR implements a solution based on Office Fabric Themes, which are Fabric's intended way to solve this problem but not the way we normally use in our codebase (we usually use hacky overrides of CSS styles that are Fabric implementation details instead).

The typical Fabric-recommended solution for this is to use their `<Customizer>` to temporarily override the globally-loaded theme; however, this has the disadvantage that it isn't cognizant of the way we swap between "default" and "high-contrast" theme palettes at runtime in our top-level `<Theme>` component. This PR implements a new `<ThemeFamilyCustomizer>` which wraps the fabric `<Customizer>` in a way which respects our app's high contrast mode setting.

##### Animated screenshots

Before:

![animation showing no background color changes on hover/focus](https://user-images.githubusercontent.com/376284/151073621-adfcdd04-33de-4a77-8eed-ecb79cd42936.gif)

After (default theme):

![animation showing background color changing on hover/focus](https://user-images.githubusercontent.com/376284/151073627-a7fe0460-af59-40de-94bb-7c690f959d2a.gif)

After (app high contrast setting):

![animation showing background color changing on hover/focus](https://user-images.githubusercontent.com/376284/151074562-16c08b67-c134-42d2-92dd-04a66af30373.gif)

After (Windows "Night Sky" HC theme):

![animation showing background color changing on hover/focus](https://user-images.githubusercontent.com/376284/151076651-43484480-bb32-4958-aacf-3bdc9e6b2516.gif)

##### Motivation

* Make table hover/focus behavior consistent between Assessment and FastPass
* Set up infrastructure that can be used in other components to avoid some types of CSS hacks

##### Context

n/a

#### Pull request checklist
<!-- If a checklist item is not applicable to this change, write "n/a" in the checkbox -->
- [x] Addresses an existing issue: Part of #5099
- [x]  Ran `yarn fastpass`
- [x] Added/updated relevant unit test(s) (and ran `yarn test`)
- [x] Verified code coverage for the changes made. Check coverage report at: `<rootDir>/test-results/unit/coverage`
- [x] PR title *AND* final merge commit title both start with a semantic tag (`fix:`, `chore:`, `feat(feature-name):`, `refactor:`). See `CONTRIBUTING.md`.
- [x] (UI changes only) Added screenshots/GIFs to description above
- [x] (UI changes only) Verified usability with NVDA/JAWS

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[6ed2fafd4e...](https://github.com/ArtemisStation/artemis-tg/commit/6ed2fafd4eccdc6f11e53acb9a1017b037d76360)
#### Thursday 2022-01-27 01:04:41 by Iamgoofball

Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

---
## [bruhlookatthisdood/Bungalow-13](https://github.com/bruhlookatthisdood/Bungalow-13)@[43a0c13035...](https://github.com/bruhlookatthisdood/Bungalow-13/commit/43a0c13035a40df85187f585130cb6b69d3144c5)
#### Thursday 2022-01-27 02:16:12 by liljackrabbit25

moves infection icons to blob icons because we werent really using it…

… anyways and they already share a bunch of shit

reworks infection upgrading alltogether to be custom per structure

fixes infection layers to not overlay a bunch of shit it shouldnt

adds ambience to infection on entry

the infection no longer absolutely destroys mechs

adds 3 turret types, resistant, infernal, and homing.

adds framework for shields to be upgradeable through non-radial-menu ways (so it doesnt take 3000 years)

removes levels and max levels for infection structures because it was stupid and boring

infection turret bullets can no longer go past beacon walls

---
## [Leo2323232/MARDEK-Leos-Mod](https://github.com/Leo2323232/MARDEK-Leos-Mod)@[598eef3635...](https://github.com/Leo2323232/MARDEK-Leos-Mod/commit/598eef3635ef2c39c951239a571503ee9f12b164)
#### Thursday 2022-01-27 02:53:57 by Leo2323232

Action skill ap cost reduction

Mardek
wound, puncture, cripple, power attack, smite evil, shock, keen strike, remove evil 10 to 5

Deugan
spiritblade, scorch, magic bolt, earth slash, power attack 10 to 5

Emela
all abilities 10 to 5

Steele
all abilities 5

zach
crescendo, sure slash, coup de grace, swift end, immoral 10 to 5

vehrn
holy slash, magic bolt, judgement, maledict, lay on hands, green lightning 10 to 5, emerald shock 20 to 5

flame, burn, combust, fire lance, 10 to 5, blaze 15 to 5

sharla
lightning bolt, stun bolt, healing wind 10 to 5, thunder bolt 15 to 5

sslenck
fire breath, fire stream, perforate, earth slash 10 to 5

solaar
solar flare, galaxy burst, spirit ember, mischief ray, pleasant sunbeam 10 to 5

elywen
all songs 5 to 3

gloria
wildfire, whirlpool, twister, razor leaf, earth heal, cleanse, 10 to 5 mass cleanse 15 to 5

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[de8695ae49...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/de8695ae4987fb8fd3c08cbb1683ce581c7e572b)
#### Thursday 2022-01-27 03:17:35 by SkyratBot

[MIRROR] makes most statpanel tabs update a tenth or so as often (>= 4 seconds instead of 4 deciseconds) because theyre wastful of cpu [MDB IGNORE] (#10929)

* makes most statpanel tabs update a tenth or so as often (>= 4 seconds instead of 4 deciseconds) because theyre wastful of cpu (#63991)

makes most updating stat panel tabs update once every 4 seconds instead of 4 deciseconds, but switching tabs instantly updates statpanel data for you. also makes examining a turf make flat icons for a maximum of 10 contents instead of 30 because its ridiculous to call getFuckingFlatIcon() wrappers that many times. also makes SSfluids not have SS_TICKER and updates its wait accordingly because theres no reason for it to be a ticker subsystem

the mc tab updates every 2 seconds unless someone has the pref enabled to refresh it quickly because SOME UNILLUMINATED LEMONS absolutely must watch overtime spikes in real time

statpanels can take between 1-3% of masters total processing time at very high pop, which is silly considering theres no need for someone to know any of the data updated accurate to less than half of a second. The only reason it needed to update so fast was because it looked awful when switching tabs, which will only be updated on the next fire. now switching tabs updates data instantly so theres no need to update the rest of the data quickly.

also makes each stat tab update into its own proc so we can tell how much each tab update costs

* makes most statpanel tabs update a tenth or so as often (>= 4 seconds instead of 4 deciseconds) because theyre wastful of cpu

* E

* https://github.com/Skyrat-SS13/Skyrat-tg/pull/11003

Co-authored-by: Kylerace <kylerlumpkin1@gmail.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [cloudflare/terraform-provider-cloudflare](https://github.com/cloudflare/terraform-provider-cloudflare)@[7dc1827e5f...](https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc1827e5f785898adcf04cb796c0710072c64ff)
#### Thursday 2022-01-27 03:37:46 by Jacob Bednarz

resource/cloudflare_ruleset: improve dashboard collisions

One of the earliest niggles with customers coming from the dashboard to
Terraform was the collision caused by a Ruleset phase being created in
the UI but the Terraform provider also needing to create the same
phase. This was problematic for a few reasons:

- The first was that when you deleted Ruleset rules in the UI, it didn't
  remove the phase. This was intentional but hidden behind the UI and
  only accessible via the API.
- Secondly, when customers wanted to use Terraform, there was an
  assumption they would be starting from scratch and many were not.
- Finally, in the event of a collision, we didn't know which Ruleset the
  customer wanted to use so we error'd out with a link to manually
  resolve which isn't a great solution but made the issue more
  prominent.

I had a chance to rethink through this issue and managed to find a way
that we improve all three points above and remove majority of the pain
points. With the proposed changes, the only time a customer needs to
manually resolve the Ruleset rules is if there are existing rules in the
UI which requires them to be deleted or migrated.

Achieving this requires the assumption that if the Ruleset has no rules,
it is ok to modify. Unfortunately, it's not that simple in practice. If
the phase already exists, we cannot just update it as the `name`
attribute is not writable after creation. Along with this, the `ref` and
`version` values will be automatically incremented causing a permadiff
in Terraform as the customer hasn't actually modified these values but
the backing service (and API) has. To work around this, if we find a
phase with no rules, we recreate it with the provided values which is
essentially the same the same thing as the "happy path" for a new
Terraform resource would be anyway.

---
## [mspeytcam/EssayGen](https://github.com/mspeytcam/EssayGen)@[9fb77a3d98...](https://github.com/mspeytcam/EssayGen/commit/9fb77a3d98e81a780e39ad769efb6f2bb3826300)
#### Thursday 2022-01-27 05:32:27 by mspeytcam

research

The effect of inclusive classes on grade 12 students' overall educational performance.


A Thesis
Presented to
The Faculty of the Basic Education 
Department
Isabela national high school 



In Partial Fulfilment
Of the Requirements for the Subject
Research





Submitted by: 
CRUZ, JESTONI 


Members:
ALONSAGAY, ROGIE
PAUDEN, JOHN REY
 

DEDICATION

This academic endeavour is dedicated to our families and friends. Without your unwavering and overwhelming support and encouragement, we would not have been able to accomplish this feat. We are eternally grateful to each and every one of you.
Most importantly, we want to express our gratitude to our Heavenly Father and Creator for providing us with the courage and perseverance to persevere in the face of endless difficulties.
"Through Jesus Christ our Lord, and through Mama Mary, before all ages, now and forevermore, be glory, majesty, power, and authority to the one God our Saviour!"






















ACKNOWLEDGEMENT
The researchers recognize the assistance and support of these illustrious individuals in performing this study. They made this work feasible, and the researchers would like to express their gratitude to the following individuals:

First and foremost, the researchers thank the Father Almighty for His unending and continuing guidance and wisdom, as well as the tenacity, mental strength, and good health they demonstrated in conducting the study despite significant challenges in terms of communication and face-to-face engagements.
Second, the researchers would like to convey their gratitude and appreciation to their families for their support and encouragement, which has aided them in continuing their work. Especially to each of our parents who, despite the cost and hardships, supported us emotionally and financially in completing this education.

Third, we are highly indebted to Ms. Nicole bitgue for sharing his knowledge, assistance, and skills in the study with our Research Project adviser. Throughout the creation of this study, his supervision provided us with support.
Finally, we would like to express our gratitude to our good friends and classmates who have led and freely assisted us in our studies to the best of their abilities. We appreciate their willingness to contribute their ideas and criticisms to the study's development. The group is really grateful for their help and all of the information that has been provided with each and every one of them in order for this study to be completed.
This research would not have been feasible without the assistance of the individuals listed, as well as their invaluable support and direction, therefore the researchers express their heartfelt gratitude to them.









ABSTRACT

At the secondary level, inclusive or mainstream classes are rejected, and there is little research on the possible benefits of combining students with and without impairments or an Individualized Education Plan in the same class. It is critical to gain a deeper understanding of the possible benefits of traditional classrooms on grade 12 students' overall educational performance.
To have a better understanding of the viewpoints of teachers who work in various high school environments the goal of this research was to relate teachers' tales and describe the changes they notice in inclusive classrooms. Four instructors were interviewed for their perspectives on mutual learning between the academic performance of grade 12 pupils as a whole, the challenges of making inclusion work, and the social, emotional, and behavioural development that occurs as a result of inclusion.
In an inclusive, mainstream classroom, this occurs for all senior high school student. 
The purpose of this paper is to promote awareness among educators regarding the potential for progress among all students integrated at the high school level, as well as the need for additional support for instructors in these settings.


















CHAPTER 1
INTRODUCTION
Background of the study 

It's important to remember that a person's entire existence is often determined by the quantity of knowledge that they may accumulate and how that knowledge is applied. This clarifies the reason for the necessity of inclusive classes on grade 12 students' overall educational performance. The most fundamental benefit of school is knowledge. From mathematics to history, literature to political science etc., one learns about a wide range of topics. The worldwide information we learn via module education process, according to my research. It has a significant impact on our future lives and allows us to comprehend events in a much more coherent manner. Educational success, on the other hand, is a metric based on a student's academic accomplishment. Educators and scholars have long been fascinated by the factors that influence the quality of students' academic performance. Many factors influence academic success, including parental education and income, instructors' topic competence, absenteeism, textbook availability and accessibility, libraries, practical laboratories, lunch provision, and many others. Academic success is heavily influenced by one's home environment. Poverty affects children's physical environs, which may provide less excitement and learning tools. Secondary school education is considered to be the backbone and foundation for pursuing higher education at postsecondary institutions. Lower academic performance at Senior High School is a threat to the educational system of any country. As a result, there is a need to evaluate the literature on academic performance and gain insight into the elements that influence students' academic success in Senior High Schools. This could assist highlight some gaps in the literature and other concerns that have been favored by research and publications in one way or another. The purpose of this study is to review the literature on determinants and their effects on senior high school students' academic outcomes.  







Statement of the Problem
         The purpose of this study is to see if there is an effect of inclusive courses on the overall educational achievement of senior high students.

Specifically, it seeks to answer the following questions:
1. What effect does inclusion have on the academic accomplishment of grade 12 students' total educational achievements?
2. What conclusions can be derived with certainty about the application of inclusion strategies in grade 12 students in terms of their impact on overall educational achievement?


Hypothesis
               Null Hypothesis: In terms of overall educational performance, there will be no difference in academic accomplishment between grade 12 students who experience inclusion and children who experience the resource classroom.


Theoretical Framework



























Conceptual Framework
       The conceptual framework below highlights the relationship between the inclusion techniques in grade 12 pupils according to their site as the basis of the dependent variable which is the impact on overall educational attainment. 

  INDEPENDENT VARIABLE                                    	DEPENDENT VARIABLE








Significance of the study
The study is seen to contribute in the practical, methodological, and theoretical significance to the area and to the following:

          Students. This study will help them understand what draws students of all abilities together, and how inclusive education initiatives are fostering understanding, shaping attitudes, and cultivating pleasant learning environments.

          Future researchers.  This study will assist them in gaining a clearer and deeper understanding of the teaching-learning situation in order to develop new knowledge about the teaching-learning situation in order to improve educational practice and learning methods by providing data to assist you in teaching and leading more strategically and effectively. This can also serve as a basis for a study of the impact of inclusive classes on students' overall academic performance in grade 12.

           	Parents. This research will assist them in improving communication with students and teachers. Updates on how the children are doing in school on a regular basis. Input on classroom goals and tactics that is useful. It also provides the opportunity to learn about and embrace individual diversity.

         Teachers. This study will provide them with additional clarifications as well as ideas that they can share with their students in order to improve their understanding of their professional and policy context on an organizational, local, and national level, allowing them to teach and lead more strategically and effectively by connecting with sources of information and professional support networks.








Delimitation of the study
The study mainly focus in determining the presence of the effect of inclusive courses on grade 12 pupils' overall educational achievement.  The objectives of this study is to understand the effect does inclusion have on the academic accomplishment of students' total educational successes that can be deduced with certainty concerning the deployment of inclusion techniques in grade 12 in terms of their impact on overall educational achievement. 


Definition of Terms 
To guarantee uniformity and comprehension of these concepts throughout the study, the following definitions were provided.



















CHAPTER II
REVIEW OF RELATED LITERATURE
This section contains thoughts and ideas that may provide context for the proposed research activity and aid in a better understanding of the study. It also contains research that is directly related to this investigation.

 METHODS
This chapter discusses the research design, locale of the study, selection of sampling site. 

RESEARCH DESIGN
In this study, a research design was adopted. Attempts to determine whether two or more groups have a cause-and-effect relationship. In contrast to correlation research, which looks at relationships, this research involves comparison. For example, a researcher might want to see how inclusive classrooms affect students' overall academic achievement in grade 12. In this situation, the researcher is not modifying any variables; instead, the goal is to get a clearer and deeper knowledge, which can also be used as a foundation for further research into this article. The researcher's purpose is to see how inclusive senior high classes affect overall educational performance in 2022. It usually begins with the result and works backwards to uncover potential causes.


Synthesis
The notion and studies found in the conceptual and theoretical literature led to a clear definition and focus for this study. It has broadened the researchers' understanding of the impact of inclusive classes on students' overall academic achievement in grade 12.
We are able to obtain suggestions on how the influence of inclusive courses on grade 12 students' general educational performance works and how we should get rid of it through the various studies that we have investigated. The researchers may be able to grasp the significance and significance of this investigation.
Furthermore, because we are in the Humms strand, it is beneficial for us to study this type of topic because it will aid us in better understanding the process of inclusive classrooms in senior high school, as well as enhance other students' general educational success.


CHAPTER III
METHODOLOGY







Research Instrument



















PRESENTATION, ANALYSIS
AND INTERPRETATION OF DATA

The summary of findings, conclusions, and suggestions are covered in this chapter.

Summary of Findings









Conclusions




Recommendations
From the findings and conclusions of the study, the following recommendations are suggested:

---
## [jdeslip/arxiv-mobile](https://github.com/jdeslip/arxiv-mobile)@[c0283ba867...](https://github.com/jdeslip/arxiv-mobile/commit/c0283ba8674a587fcfca31a6ba5c1cb29cc56318)
#### Thursday 2022-01-27 05:43:18 by Naitim

Add data loss patch for Search Activity

Hello developers of arxiv mobile

I am using your app privacy friendly notes. I think the app is great but I have one minor patch that could improve the user experience.

Here is a picture to help illustrate what activity that are changed in my patch:

https://ibb.co/mN1YmTG

When the user tries to do a new search. If the screen focus goes to another app or activity or if the user accidentally closes or press back the app, the user might lose any data they had put into this page

This feature will automatically store the data when the user leaves the activity without submitting and restore said data when they restart the activity(this can be seen here where I closed the activity and restarted it https://ibb.co/qdtCnVZ). Therefore, the user does not have to fill in the data again thus improving the user experience.

I have tested out the feature to ensure it works.

If you have any questions or if you would like me to change anything, please do not hesitate to let me know!

Thank you for your time,
Tim

---
## [BSCPGROUPHOLDINGSLLC/153974-2020](https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020)@[4bde38a23f...](https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/commit/4bde38a23f53556d48c25760b81df12b7a93d6b7)
#### Thursday 2022-01-27 06:26:45 by DINCER & CO

ADDRESSED TO THE ATTENTION OF ORTIZ & PENA AT THE NYPD: Wednesday, January 26th, 2022 at 9:49 AM 

THANK YOU

Tuesday, January 25, 2022 at 02:41:58
FROM FEBRUARY AND THROUGHOUT MY LEASE... requested ORTIZ and PENA send this to the Mayor Eric Adams earlier


https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/2022.01.25%20--%20LETTER%20TO%20THE%20MAYOR..pdf

    
BANGING ON THE RADIATOR > VIEW FROM THE CORRIDOR / HALLWAYS...
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/BANGING%20ON%20THE%20RADIATOR.PNG

VIEW FROM OUTSIDE
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/INSIDER%20VIEW%20OF%20MY%20APARTMENT..PNG


NO CONSENT. NO JAIL?
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/NON%20CONSENT%20TO%20FILM%20INSIDE%20OF%20MY%20APARTMENT.PNG


APPARENTLY - THE ZUCKERS ALSO HAD A VIDEO-A-GRAPHER?
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/ROSALIA%20CHANN.PNG


GOOD CAUSE ORDERED BY HAGGLER?
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/%5B00037%5D153974_2020%20--%20HAGGLER%20ORDERS.pdf



RENT REGULATION BANDS.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/%5B00179%5D153974_2020%20-%20rent%20regulation%20bands.pdf


ROSALIA CHANN - ONDEMAND VIDEO
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/rosalia%20chann.pdf


A.  THIS EMAIL CAME FROM A ZUCKER? NEVER....
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/Pages%20from%2020200730_ASSHOLE.pdf


B.  NOTARIZED BY WHO? NEVER....
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/Pages%20from%2020200730_RISOPLI%20NOTARIZED.pdf


CAUGHT "BANGING ON MY RADIATOR" WHICH GIRL
- AND WHY WONT THEY GIVE ME THOSE SHOTS FROM THE FRONT CAMERA AS WELL - SHE KNEW ON THE 27TH OF APRIL, 2020.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/BANGING%20ON%20THE%20RADIATOR.PNG
   

VERY AGGRESIVE PLAY-BY-PLAY ON THE RECORD. WITHOUT CONSENT.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/INSIDER%20VIEW%20OF%20MY%20APARTMENT..PNG


EMAIL FROM ASHLEY, DIRECTED BY SHARI. S. LASKOWITZ...
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/ASHLEY_IPHONE4_%20RE_%20Sullivan%20Properties%20v%20Baris%20Dincer.PDF

EMAIL DATED DECEMBER 20TH, 2021
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/A%20-%20NYCRR%20202%20-%20SSN%20-%20ADMITTED%20AS%20GOOD%20EVIDENCE%20IN%20153974.pdf


NOTICE TO NYPD OF LARCENY - AS EMAILED EARLIER TO RE-STATE 2022.01.24 - TUESDAY MORNING.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/-2022.01.20%20-%20CODE%2010013%20-%20101%20WEST%2055TH%2010019.pdf


ATTORNEYS - PARTIALLY - ON BEHALF OF ZUCKERS.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM,-TAPE---AND-PEEKING-INSIDE/NYS%20BAR%20%20IDENTIFIERS

ENTERED ON BEHALF OF ZUCKERS, BY ITS ATTORNEYS.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/%5B00025%5D153974_2020%20-%20LaToya%20Britton%20%20Legalasst_mskyline.com%20ANNE.BRANDON%20APRIL%2013.pdf


NOTARIZED BY ALEXIS BRANDON ON THE 11TH OF APRIL 2020 - IN THE COUNTY OF ALAMEDA, CALIFORNIA.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/%5B00031%5D153974_2020%20%20%20--%20NOTARIZED%20%20APRIL%2011TH%20IN%20CA%20%5B00025%5D%20153974_2020%20ANNE.BRANDON%20APRIL%2013.pdf


A CASUAL EVENING OF BUSINESS AND CONVERSATION AT THE ZUCKER.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/%5B00022%5D153974_2020%20-%20ANOTHER%20EMAIL%20%20FROM%20ALEXIS%20MOTHER%20APRIL%2011.pdf



REQUEST TO HAGGLER - NOTARIZED BY DINCER, REQUESTING INTERVENTION
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/%5B00079%5D%20153974_2020%20-%20NOTARIZED%20LETTER%20FROM%20DINCER%20TO%20SHLOMO.pdf


MIWA'S DESPERATE HOUSEWIFE REPORTS. DATED APRIL 3RD, 2020.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/%5B00020%5D153974_2020%20%20-%20MIWA.pdf



SATURDAY - Jun 6- 2020 - NO WINDOW REPAIR -- FIRE EGRESS AND SAFETY
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/NONCONSENT-TO-FILM%2C-TAPE---AND-PEEKING-INSIDE/...2020.07.25.%20NOTIFIED%202020.06.05.pdf


REQUESTED TO CEASE AND DESIST FROM THEIR BUSINESS DEALINGS. FOLLOWING MY LETTER TO THEM ON THE 8TH OF AUGUST - RESPONDED IMMEDIATELY ON BEHALF OF DONALD ZUCKER.
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/main/2020.08.10%5BMyscan_2020081014343276%5D.PDF

---
## [PKRoma/git](https://github.com/PKRoma/git)@[07564773c2...](https://github.com/PKRoma/git/commit/07564773c2569d012719ab9e26b9b27251f3d354)
#### Thursday 2022-01-27 07:19:07 by Ævar Arnfjörð Bjarmason

compat: auto-detect if zlib has uncompress2()

We have a copy of uncompress2() implementation in compat/ so that we
can build with an older version of zlib that lack the function, and
the build procedure selects if it is used via the NO_UNCOMPRESS2
$(MAKE) variable.  This is yet another "annoying" knob the porters
need to tweak on platforms that are not common enough to have the
default set in the config.mak.uname file.

Attempt to instead ask the system header <zlib.h> to decide if we
need the compatibility implementation.  This is a deviation from the
way we have been handling the "compatiblity" features so far, and if
it can be done cleanly enough, it could work as a model for features
that need compatibility definition we discover in the future.  With
that goal in mind, avoid expedient but ugly hacks, like shoving the
code that is conditionally compiled into an unrelated .c file, which
may not work in future cases---instead, take an approach that uses a
file that is independently compiled and stands on its own.

Compile and link compat/zlib-uncompress2.c file unconditionally, but
conditionally hide the implementation behind #if/#endif when zlib
version is 1.2.9 or newer, and unconditionally archive the resulting
object file in the libgit.a to be picked up by the linker.

There are a few things to note in the shape of the code base after
this change:

 - We no longer use NO_UNCOMPRESS2 knob; if the system header
   <zlib.h> claims a version that is more cent than the library
   actually is, this would break, but it is easy to add it back when
   we find such a system.

 - The object file compat/zlib-uncompress2.o is always compiled and
   archived in libgit.a, just like a few other compat/ object files
   already are.

 - The inclusion of <zlib.h> is done in <git-compat-util.h>; we used
   to do so from <cache.h> which includes <git-compat-util.h> as the
   first thing it does, so from the *.c codes, there is no practical
   change.

 - Until objects in libgit.a that is already used gains a reference
   to the function, the reftable code will be the only one that
   wants it, so libgit.a on the linker command line needs to appear
   once more at the end to satisify the mutual dependency.

 - Beat found a trick used by OpenSSL to avoid making the
   conditionally-compiled object truly empty (apparently because
   they had to deal with compilers that do not want to see an
   effectively empty input file).  Our compat/zlib-uncompress2.c
   file borrows the same trick for portabilty.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Helped-by: Beat Bolli <dev+git@drbeat.li>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Ahayaa/dragonheart_kernel_oneplus_sm8150](https://github.com/Ahayaa/dragonheart_kernel_oneplus_sm8150)@[fa06799344...](https://github.com/Ahayaa/dragonheart_kernel_oneplus_sm8150/commit/fa06799344ee507b343c8c989e3ee27ecf22ec58)
#### Thursday 2022-01-27 08:40:56 by alk3pInjection

drm: Handle dim for udfps

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
## [ghc/ghc](https://github.com/ghc/ghc)@[c0757c4d19...](https://github.com/ghc/ghc/commit/c0757c4d19af232abe352bf0cfe37fc1adb2e064)
#### Thursday 2022-01-27 10:12:45 by David Feuer

Add test supplied in T20996 which uses data family result kind polymorphism

David (@treeowl) writes:

> Following @kcsongor, I've used ridiculous data family result kind
> polymorphism in `linear-generics`, and am currently working on getting
> it into `staged-gg`. If it should be removed, I'd appreciate a heads up,
> and I imagine Csongor would too.
>
> What do I need by ridiculous polymorphic result kinds? Currently, data
> families are allowed to have result kinds that end in `Type` (or maybe
> `TYPE r`? I'm not sure), but not in concrete data kinds. However, they
> *are* allowed to have polymorphic result kinds. This leads to things I
> think most of us find at least quite *weird*. For example, I can write
>
> ```haskell
> data family Silly :: k
> data SBool :: Bool -> Type where
>   SFalse :: SBool False
>   STrue :: SBool True
>   SSSilly :: SBool Silly
> type KnownBool b where
>   kb :: SBool b
> instance KnownBool False where kb = SFalse
> instance KnownBool True where kb = STrue
> instance KnownBool Silly where kb = Silly
> ```
>
> Basically, every kind now has potentially infinitely many "legit" inhabitants.
>
> As horrible as that is, it's rather useful for GHC's current native
> generics system. It's possible to use these absurdly polymorphic result
> kinds to probe the structure of generic representations in a relatively
> pleasant manner. It's a sort of "formal type application" reminiscent of
> the notion of a formal power series (see the test case below). I suspect
> a system more like `kind-generics` wouldn't need this extra probing
> power, but nothing like that is natively available as yet.
>
> If the ridiculous result kind polymorphism is banished, we'll still be
> able to do what we need as long as we have stuck type families. It's
> just rather less ergonomical: a stuck type family has to be used with a
> concrete marker type argument.

Closes #20996

Co-authored-by: Matthew Pickering <matthewtpickering@gmail.com>

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[ab0f0681ec...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/ab0f0681ecefbbf962c0730959a87b9519ae8fa1)
#### Thursday 2022-01-27 10:45:29 by Peter Zijlstra

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
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [occydaboss/occydaskyblock](https://github.com/occydaboss/occydaskyblock)@[a299a1b9e8...](https://github.com/occydaboss/occydaskyblock/commit/a299a1b9e8a0ed28e77a64766e63150a1bb84c96)
#### Thursday 2022-01-27 13:06:23 by OccyDaBoss

oh shit oh fuck my mongodb url was live on githbub

---
## [Project-1CE/vendor_ice](https://github.com/Project-1CE/vendor_ice)@[2bde28e191...](https://github.com/Project-1CE/vendor_ice/commit/2bde28e19148a95be15acbb8ac8f068bd85e44fa)
#### Thursday 2022-01-27 13:08:17 by alk3pInjection

ice: Sugisawa alpha1 is available now.

CODE FREEZE!

So yes, I've been working on this project for the whole two weeks,
and five days were wasted dealing with keystore2 -- Jesus! Till
today I still have no idea of why this could be easily solved by
enforcing SELinux. This must be the most weird thing I've ever seen.

As can be seen, Project ICE is currently based on the Qualcomm fork
of Android. I can hardly say it is a good decision, but whatever,
feel damn good now. Tagged as alpha1, this stage of development is
mainly focused on the bring-up all around, with some basic features
and fixes merged. And its successor, alpha2, will be much more completed
I think. But hold on, let's celebrate our Lunar New Year first.

So that's all of the RELEASE NOTE for Sugisawa alpha1. This commit
also squashes a change of the target kernel repo for guacamole. Yeah,
I'm tired of syncing multiple remotes ;)

Change-Id: I4053e710319f03bde32a0e1635125e5ac754d921
Signed-off-by: alk3pInjection <webmaster@raspii.tech>

---
## [west3436/vgstation13](https://github.com/west3436/vgstation13)@[b879dddba0...](https://github.com/west3436/vgstation13/commit/b879dddba0f6a2afcf72a77f4696f3e9c031ecb5)
#### Thursday 2022-01-27 15:05:37 by rob

adds sound effects to surgery steps (#31850)

* the everything

* nmb

* ok

* dfdffdfsds

* ssssssssssssssssssssskurfusr

* fuck yoiu damian fuck you!!!!!

* DAMIANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

* D

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[413fd90502...](https://github.com/Ghommie/tgstation/commit/413fd9050271829e2899b88a676995ae2517111c)
#### Thursday 2022-01-27 15:29:30 by GoldenAlpharex

Dullahan Partial Refactor: They Work Again Edition (#63696)

So, a few months ago I was like "hmm there's something weird going on with party pods...", which got me looking into important_recursive_hearers or something like that. I spoke about it in the coding channel and Kyler actually fixed it before I did. But I also caught a similar glitch with Dullahans, so I decided to investigate...

Two months later...

I present to you a partial unfuckening of the Dullahans, in that I made them fully functional once again:

They only hear speech through their head (not sounds, sadly, someone else would have to tell me how to do that because I otherwise really wouldn't know how to do it in a sane way), they speak through their head, runechat-included.
When you spawn a Dullahan, you're set to look through the Dullahan's eyes (so from their head), and that doesn't reset when you log off and back in, or admin-ghost and come back in your body.
When you're looking through your head, your view will no longer be reset to your body upon entering a locker, which is nice to avoid not being blind while looking through your body.
Dullahan heads no longer look completely lifeless and without organs. They have eyes that don't look dead and that even match the player's intended eye color.
Dullahan can now properly examine things from their head, which was intended and 100% not functional.
Dullahan heads now speak with the proper name of their owner, instead of having a random name attached to it at round-start.
Dullahan heads are also now properly named too.
Dullahans can now properly whisper, sing and do all these funny things that they were unable to do before.
Dullahan whispers will now properly respect the range of the whisper.
Dullahans can now succumb in hardcrit by whispering, as intended. This potentially fixes other species that worked similarly not being able to succumb, like abductors, although I didn't test if they normally could, I just know they absolutely will be able to now.
When switching from Dullahans to a different species, your old head will no longer stay behind.
I also added a proc for species to do some code when we get a ckey login in our mob, which could potentially be useful for other stuff in the future, but it was necessary here as the view is reliant on the client, which we want to ensure doesn't get weird view glitches like having their head's vision overlay while actually being centered on their body.

I also made it so say() now takes a range argument, which is 7 by default, just so things that aren't humans can also whisper and do all those kinds of things. Going with that, there's probably a few more things that will be able to be done better thanks to this, although I haven't tested every edge case with this, but I doubt it will make much of a difference in the future.

---
## [thesadru/hikari](https://github.com/thesadru/hikari)@[0028d63489...](https://github.com/thesadru/hikari/commit/0028d634892a68f141dd1c326e7d81e44ddfcca8)
#### Thursday 2022-01-27 15:54:34 by sadru

I DESPISE WORKFLOWS UwU

I FUCKING HATE OVERLOADS
MYPY DOESN'T DETECT THEM WHAT THE HELL????
FUCK FLAKE8, IT CAN SUCK MY DICK. IT TAKES LIKE 10 MINUTES TO RUN ONLY TO TELL ME MY CODE ISN'T SHITTY ENOUGH?!!?!!?

---
## [argrath/NetHack](https://github.com/argrath/NetHack)@[420d121f93...](https://github.com/argrath/NetHack/commit/420d121f939686f2bdc734038119b9cf932e1f3a)
#### Thursday 2022-01-27 16:39:05 by PatR

'urgent' messages

Follow up on some old groundwork.  For tty, if the core has designated
a message as 'urgent', override any message suppression taking place
because of ESC typed at the --More-- prompt.  Right now, "You die"
messages, feedback about having something stolen, feedback for
"amorous demon" interaction (mainly in case of armor removal), and
exploding a bag of holding are treated as urgent.

The "You die" case is already handled by a hack in top-line handling;
I left that in place so the conversion of 3 or 4 pline("You die.*")
to custompline(URGENT_MESSAGE, "You die.*") was redundant.  There
are probably various non-You_die messages which precede done() which
should be marked urgent too.

Other interfaces might want to do something similar.  And we ought to
implement MSGTYPE=force or MSGTYPE=urgent to allow players to indicate
other messages that they want have to override suppression.  But I'm
not intending to work on either of those.  I mainly wanted to force
the magic bag explosion message to be shown since a sequence of "You
put <foo> into <bag>." messages is a likely candidate for --More--ESC.

---
## [CoriolisStorm/bc7enc_rdo](https://github.com/CoriolisStorm/bc7enc_rdo)@[d651cfdd16...](https://github.com/CoriolisStorm/bc7enc_rdo/commit/d651cfdd16c1ef26ca9298ef0e3eb0bc7e29bdf9)
#### Thursday 2022-01-27 17:01:33 by CoriolisStorm

Update bc7e.ispc

OVERVIEW
--------
The biggest image quality improvement is a new way of measuring error that tries to minimize the final frame buffer error after blending by treating color and alpha error together, rather than as independent channels. This really helps eliminate blocking artifacts in some alpha images, with no user-tweaked parameters. (A big downside of user-tweaked parameters is that often different parts of an image need different settings!) The only user setting is how color and alpha are to be used, which is one of four intuitive choices. In addition, the alpha blended and alpha tested error metrics don't even need you to set the alpha weight relative to RGB weights! That's because it optimizes color and alpha together based on the worst case color error after blending with the frame buffer, either in RGB or in YCbCr color space. Since it's minimizing color error after blending, alpha is implicitly handled by the color weights, making it even easier to tune.

I also did some improvements to the color partition selector that reduce overall error.

I improved the perceptual compressor by supporting rotation and by using the YPbPr weights for sRGB (in gamma space) rather than the weights for linear RGB. Using the original linear weights is a simple #if change. The images that we compress are always expected to be in sRGB.

One other improvement is to make bc7e optionally return the error for each block. Apex Legends used this to recompress just the really low quality blocks with the uber quality setting. This gives most of the benefit of uber quality in a fraction of the time.

The per-channel error weights are now floats instead of integers.

I tried to keep the API the same as Rich Geldreich's original BC7E with additions that default to old behavior, so it should be an easy drop-in replacement.


MAJOR DETAILS
-------------
) Added "m_optimize_for" to "ispc::bc7e_compress_block_params". This can be one of the following values:
  BC7E_OPTIMIZE_FOR_INDEPENDENT_CHANNELS -- optimize each color channel independently based on their relative error weights (old behavior)
  BC7E_OPTIMIZE_FOR_COLOR_TIMES_ALPHA -- optimize for color times alpha, where the product replaces or adds to the frame buffer
  BC7E_OPTIMIZE_FOR_ALPHA_BLENDING -- optimize for alpha blending with the frame buffer.
  BC7E_OPTIMIZE_FOR_ALPHA_TEST -- optimize for alpha test.

The default is to keep the old behavior.

) When optimizing for alpha blending, we want to minimize the peak squared error between the original and compressed images after blending with every possible frame buffer. The math is pretty simple. If the color is C, the alpha is A, and the frame buffer is F, the final on-screen error is "(C1 A1 + F (1 - A1)) - (C0 A0 + F (1 - A0))", which easily simplifies to "C1 A1 - C0 A0 - F (A1 - A0)". It turns out this is equivalent to "((C1 + C0)/2 - F) * (A1 - A0) + (A1 + A0)/2 * (C1 - C0)". The error is linear in F, so the maximum must be at F = 0 or F = 255. Whether the absolute value is maximized with F = 0 or F = 255 depends on the signs of A1 - A0 and C1 - C0, as well as the magnitude of C1 + C0. The cheapest way to compute which F to use is to try both and keep the maximum.

The code uses "C1 A1 - C0 A0 - F (A1 - A0)", since it's the cheapest to compute. But, the last equivalent form in the previous paragraph does give a bit more intuition. The importance of changes in alpha is whatever "A1 - A0" gets multiplied by, and similarly for color. So, the importance of color is proportional to the average alpha value, which is not surprising. But, the importance of alpha is generally proportional to "(C1 + C0) / 2 - F". This is more complex to analyze, since F may be 0 or 255. Because of that, alpha is generally more important when the color is near black or white, and less important when the color is near middle gray. But there are still complex interactions between color and alpha, especially since there are three color channels! So, it really is worth it to model the full complexity of how color and alpha interact; it doesn't seem worth it to try to come up with a per-pixel importance for color and alpha, and certainly not a full-image importance.

) Optimizing for color times alpha is most useful for alpha-weighted additive blending, where you do "C * A + F". The error is simply "(C1 A1 - F) - (C0 A0 - F)", which easily simplifies to "C1 A1 - C0 A0". Note that this is identical to the alpha blended form, except that we always use F = 0. So, these two use the exact same code path. One frame buffer value is always 0, and I just set whether the "other" frame buffer value is 0 or 255.

) Optimizing for alpha test is complicated to support a single image with multiple alpha test thresholds, which artists sometimes do to save memory when one alpha tested image is known to be a subset of another. To support this accurately, we should sum the error for each alpha test threshold, which would really complicate the code. Instead, I added "ispc::bc7e_compress_block_params::m_alpha_test_threshold_min" and "m_alpha_test_threshold_max". It remaps alpha so that it is 0 below the min and 255 above the max, and then just uses the alpha blend error metric. This was much easier to implement. If min == max, this is normal alpha testing with a single threshold; this is the most important case. As min and max get further apart, it still tries to minimize error in alpha, but it isn't as accurate as if it knew where the thresholds were.

) To improve quality, I made the BC7E compressor optionally return the error for each block. In my calling code, after all compression is done, I gather all blocks that had error greater than a threshold, and then I recompress just those blocks at "uber" quality. This brings quality up and spends compression time where it matters most. About 1% of blocks try uber quality, and about 50% of those improve. Sometimes the improvement is slight, sometimes it is surpringly better (like 1/20th of the squared error).



PERCEPTUAL ERROR AND PARTITION SELECTION IMPROVEMENTS
-----------------------------------------------------
) The bc7e compressor has a "perceptual" error mode. This tries to minimize error in YCbCr space. There were some minor issues with it:
  - The perceptual space is implemented as YCrCb, but the standard definition is YCbCr -- it swapped Cr and Cb. This makes a little sense, because Cb is strongest in blue... but if you were to do that, the order CrYCb makes the most sense, since Cr is strongest in red and Y is strongest in green. The only public-facing part of this is how you specify the weights for perceptual error. I decided to keep the non-standard order so as to not break the API.
  - The perceptual space internally is sometimes called "YPbPr", and sometimes uses "l" instead of "y" for luminance. "l" is never a good variable name; it looks too much like "1" and "I". It is not great to use that to hold a value called "y", though it does seem that "l" is more natural than "y" for luminance. I think the standard "Y" for luminance comes from the CIE XYZ color space, where Y is luminance, and I think they picked XYZ as color coordinates because 3D coordinates in math are pretty much always XYZ. CIE XYZ was ratified in the early 1900s, long before computers (depending on what you call a "computer"), much less computer graphics.
  - It used the YCbCr transform for linear RGB, not the transform for non-linear sRGB. The inputs to the compressor are sRGB, so this overemphasizes green and deemphasizes blue. I switched it to the transform from sRGB to sYCC, but left the transform for linear RGB as a #if toggle.
  - Modes 4 and 5 support rotation (where alpha swaps with a color channel), but it skipped that in perceptual mode. I think that's because it couldn't do the proper weights once a color channel was swapped with alpha. If you interpret the channels after rotation as if there was no rotation when calculating error, you can get bizarre error values that make the compressor select some really bad blocks. Since I added rotation support to do alpha-aware optimization, it was pretty easy to let perceptual optimization handle rotation too. Rich Geldreich also wrote on his blog that rotation has a relatively small impact on total MSE and hurts RDO, so he may have also thought it wasn't worth the effort to support. He's absolutely right about it being minor in most images, but it can be a noticeable quality improvement for images that are strongly red, green or blue with a simple alpha channel, such as the blue earth image mentioned before.
  - Many BC7 modes use partitions. Instead of just one pair of color endpoints in a 4x4 block, modes 0-3 and 7 have 2 or 3 pairs of endpoints called subsets. Each pixel knows what subset to use based on the partition map, which is chosen from a table of 64 pre-defined partitions (16 partitions for mode 0). To decide what partition works best, the compressor iterates each partition and splits pixels by their subset in that partition, then gets a quick estimate of the error for the colors in each subset. It keeps the N partitions with the lowest error, where N is usually 1, and then does the expensive color fitting to the pixels in each subset. Anyway, there was an issue with the fast estimated colors when using perceptual error. For modes 0-3, it would use the Y Cr Cb weights as if they were R G B weights, respectively. For mode 7, it switched to uniform weights. This could cause it to choose an inferior partition in modes 0-3, but it would then correctly optimize the colors for that subset. I at first fixed this by making modes 0-3 switch to uniform weights as well, but later I made this even better (see next point).

) So, the partition selector needs more discussion. It does quick color estimation of each subset in each partition by finding a color ramp for each subset. In the old code, the color ramp just took the minimum and maximum of RGB (or RGBA) independently, then made one end of the line the mins and the other end the maxs. It then chose which point to use for each color by projecting it as a 0-1 fraction on the line, clamping it, scaling it by the maximum selector value (so * 7 for 3-bit indexes), and rounding. It then got the squared distance of each channel to this chosen point, and weighted those errors by the individual channel weights.

I made three improvements to this.

First, I track the covariance of the red, blue and alpha channels versus green. If the covariance is negative, I swap the start and end of that line for that channel. It is usually the case that all channels are positively correlated, but this is often untrue at edges. For instance, if you have a redish region with an antialiased boundary with a greenish region, then red and green will have negative correllation. In simple English instead of math speak, the code was assuming that when green got bigger, red/blue/alpha also got bigger. The new code handles those channels getting smaller when green gets bigger. This had the biggest impact on choosing better partitions.

Second, I weighted the dot product to account for the relative weights of the different channels. This is easiest to understand if you think of RGB colors as XYZ coordinates in a 3D space. The error metric finds a weighted sum of the squares of the RGB deltas. But, you can first transform the space by scaling each coordinate by the square root of that channel's weight, and then in this modified space the squared error is exactly equal to the squared Cartesian distance. In this "error space", we can project the query point onto the color line and pick the closest point by rounding, and we're guaranteed to get the point that minimizes squared error. This is usually the same point as if we did the projection in standard RGB space, but not always! That's because the non-uniform weights correspond to a non-uniform scale. So, vectors that are perpendicular in one space are not necessarily perpendicular in the other space. The closest point on the line forms a perpendicular vector, so the closest point on the line in one space is probably not the closest point on the line in the other space. We round the closest point, so these two points will usually round the same way to choose the same index on the color line, but not always. When they round differently, it will be near halfway between two points, so their distances are still expected to be similar. So, using the suboptimal projection will usually have no effect on the partition ranking order. But, it does affect the order sometimes, because using the more accurate projection reduces the total error. Using the correct projection is really cheap, too; it's just 3 or 4 additional multiplies outside the inner loop.

Finally, I made perceptual error use weights that are a blend between uniform weights and the YCbCr weights for Y from RGB. I experimentally found that a ratio of 10:1 was the sweet spot (the Y weights are 10x as strong as the uniform weights). This gives better results than just using the Y weights, probably because just using the Y weights ignores all errors in Cb and Cr.

) There is one thing I tried for improving perceptual error that didn't pan out. I tried transforming all pixels to YCbCr space before doing the partition estimates. This made it cheap to estimate error difference directly in YCbCr space, instead of approximately in RGB space. Surprisingly, this actually increased total compression error as measured in YCbCr! My theory is that the line connecting two opposite corners of the color box in RGB is a better estimate of the optimal color line than doing the same thing for the corners of the color box in YCbCr, but I didn't spend any time actually figuring out why this was worse.

) I implemented perceptual error with alpha-aware error. This was mathematically interesting. The error for a pixel should be the worst possible error after alpha blending the pixel with the frame buffer, measured in YCbCr (with weights).

It's best to think of this geometrically, by treating RGB as coordinates in 3D space. The uncompressed color C0 and compressed color C1 are two points. The set of all possible frame buffer colors forms a cube. The error equation "A1 C1 - A0 C0 - (A1 - A0) F" is then a linear combination of two points and a cube, so the resulting shape is still a cube, just translated and scaled. So, in 3D space using RGB coordinates, the set of all possible errors is a solid cube. We then transform this set of errors into 3D space using YCbCr coordinates. This is a linear transform, but it is not orthogonal, so the resulting shape is sheared into a parallelepiped (i.e., a 3D parallelogram).

There's one more transform to consider. To get the error, we take a weighted sum of the squared differences in each YCbCr color channel. If we first multiply each channel of YCbCr by the square root of its respective weight, we would get the error as the sum of the squares of each difference... i.e., the error is just the normal squared Cartesian distance in this new space.

So, the last transformation is non-uniform scale by the square root of the color weights. This remains a parallelepiped. In this final space, squared Cartesian distance is the error. So, the maximal error is just the squared distance to the point on this parallelepiped that is furthest from the origin.

To find the furthest point, we first find the center of the parallelepiped. This is actually pretty easy. The parallelepiped is a weighted sum of 3 non-orthogonal axis vectors. To get those vectors, first take the YCbCr transform matrix and multiply the rows by the square roots of the YCbCr weights. The axis vectors are now the columns of this matrix, so these vectors just depend on the color transform matrix and the error weights and can be precalculated. To construct the parallelepiped in error space, we multiply each axis by R, G, or B, respectively (and scaled by A1 - A0). The "first" corner is the alpha-weighted difference between the transformed points C0 and C1; the rest of the parallelepiped is gotten by adding 0-255 times each axis vector. So, the center is just 127.5 times each axis vector. You can get this by adding the R, G, B axis vectors together and scaling the sum by 127.5. That's convenient, because the sum of those vectors has a lot of cancelation. In fact, it just moves in the Y direction by the square root of the Y weight! This kind of makes intuitive sense for Y Cb Cr, because Cb and Cr are centered around 0.

Once we have the center of the parallelepiped, we know the furthest point is half a parallelepiped away on each axis. We can tell which way to go by taking the dot product of the axis and the center; the sign of that dot product is the sign we should use for adding the other half of the step on that axis. We do this for each channel of Y Cb Cr, and we arrive at the point that has the most error. The squared distance between this point and the origin is the maximum error, which is what we wanted to find all along.



MINOR DETAILS
-------------
) Most of the work was refactoring the BC7E code to make it easier to do a different error metric. The existing error metric was really simple, just basically squaring a vector and dotting it with a constant, so the math was rewritten in literally dozens of places rather than in a function.

) One tricky thing is that 2 of the 8 modes in BC7 have separate "scalar" and "vector" parts. Two bits specify which channel is scalar; 0 = alpha, 1 = red, 2 = green, and 3 = blue. They call this the rotation. If the rotation is not 0, then after decompression, it swaps alpha and the corresponding color channel (so the rotation swaps color channels, it does not rotate them, and the official name is something of a misnomer). It is clearly designed for separate color + alpha, with the observation that sometimes it's better for another channel to be independent. For instance, one test image is basically earth from space with a slow alpha gradient. In this image, most of the variation is in the blue channel, so the vector/scalar split is more often RGA|B than it is RGB|A.

The original bc7e compressor handled this by swapping the color and alpha channels before compressing, as well as their weights. This lets the rest of the compressor code not have to worry about rotation at all. This works great when you treat error as a weighted sum of the individual channel weights. If you are trying to emulate alpha blending, and alpha was swapped with blue, it doesn't work so great. So, I had to handle the alpha channel swapping with another channel.

Part of handling this was to make alpha compress before color (scalar before vector), so that vector compression can use the results of scalar compression. The scalar channel always optimizes independently, then the compressed scalar channel is passed to the vector compressor, so that it can measure the error after taking into account alpha blending or color times alpha. This needs to handle rotation, so there are several cases in the vector compressor!

Compressing alpha independently is the right thing to do for independent channels, but not quite right with alpha-aware error metrics. I still optimize independently as a performance optimization. It's possible that a compression choice that is inferior for the scalar channel independently is actually superior for the scalar and vector channels collectively. The chances of this are quite small, and the improvement when it does happen is expected to be quite small, and getting that improvement is a lot of work (both dev time and CPU time), so I decided it wasn't worth it.

) The BC7E compression code often calculated "floor(x + 0.5)". This should be the same as "round(x)", except when the fraction part of x is exactly 0.5; the "floor" version always rounds this up, but the "round" version rounds to the nearest even value. SSE2 has an efficient "round" instruction, but you don't get an efficient "floor" instruction until SSE4.1. The compiler can't just turn "floor(x + 0.5)" to "round(x)" because of the difference in rounding some half values. So, I changed all cases of "floor(x + 0.5)" to "round(x)" in the BC7E code.

) The BC7E compression code sometimes initialized "infinite" error as 1e+9 or 1e+10, or 1-10 billion. I ran into cases where really bad blocks with high error weights exceeded this limit. I changed this to FLT_MAX.

) The BC7E code was doing too much work to calculate p bits, and split cases and loops that could be merged (see the top of find_optimal_solution in bc7e.ispc, around line 3007). I made this more efficient. I noticed it was also always calculating the alpha channel even when it didn't need to; I tracked this down to "scale_color" in "evaluate_solutions" always transforming all 4 channels, so it needed the alpha channel to be initialized. I made "scale_color" only scale the channels we care about, which does less work for opaque blocks there, and lets us do less work in "find_optimal_solution" too. Not only was initializing alpha doing more math, but needing to initialize alpha was the only reason the various loops over color channels had to be split.

) The partition error estimation functions in BC7E were taking the same parameters as the accurate color compressor, but only using a small subset of the values. I made a new struct to hold just the values it needs, plus any values that only apply to partition error estimation.

) The partition error estimation functions took in a "best so far" value. This was never used. It could be used as an early out in the last part of the function, but that's only saving a fraction of the work, and in ISPC code it only saves that if all lanes in the gang agree to take the early out. But, testing for the early out takes work on every iteration. So, using this as an early out is unlikely to save more time than it costs in ISPC code, so it's not worth passing to the function. I removed it.

) BC7E had some mysterious "disable_faster_part_selection || num_solutions <= 2" bools passed to a function, then a "!disable_faster_part_selection && num_solutions > 2" check several pages of code later. It turns out that, if you have more than 2 partitions, this was asking it to find the best partition without spending extra time to refine the endpoints. Then, if the best partition you found was better than the best solution using another method, it would refine the endpoints of just the winning partition. So, this is a performance optimization. I made a bool "refine_while_choosing" and used this in the two places to better document what it does and how the two uses are connected.

) BC7E had some tables initialized with floats specified with 6 fractional digits. The exact constants need at most 12 mantissa bits, but the 6-digit floats usually needed 23 mantissa bits, because they were usually off by 2 ULPs from the exact constants. I replaced the initializers for this table with a macro that gives the exact values, and is easier to understand. This avoids some potential numerical issues in the least squares solver, where a determinant should have been zero but wasn't. See how "pSelector_weights" is used in "compute_least_squares_endpoints_rgb[a]"; the calculation of the "z" determinant has a high chance of being exact when summing 12-bit floats, and a much lower chance of being exact when summing 23-bit floats. It does an early out check with exactly zero; epsilon issues can make it skip this check, doing extra work and getting nonsense results. This would just waste compression time. It wouldn't crash, and the code only keeps the best results, which would never be this result (except maybe by an incredible freak miracle).

) Made BC7E use float errors instead of integer errors. This is needed to improve compression on low alpha blocks when optimizing for alpha blended error. For example, if alpha is 1 out of 255, then all color errors are basically scaled by 1/255, which can easily round to 0 when cast to an integer. If multiple encodings all round to 0, it can't tell which was actually better.

I could have kept everything as integers and scaled the squared error by 255^2, but instead I chose to use floats for error and let the errors be less than 1. It usually used float errors internally and converted them to integers at the end, so staying in floats is more efficient and doesn't lose any precision.

) Measuring errors as floats lets me turn the error weights into floats as well. This lets callers have easier control over the weights, and avoids a lot of integer-to-float conversions.

) "color_cell_compression()" only tried to do the "uber" stuff if the error metric exceeded num_pixels * 3.5. If you scale the weights by a constant, the error metric is scaled by that same constant, but this threshold is not. The default weights for RGB errors sum to 4, so this is an average squared error of about 0.875, or average error of about 0.9354. But the default weights for perceptual errors summed to 464, so this is an average squared error of about 0.007543, or an average error of about 0.08685 (assuming all channels have equal error). In other words, the default perceptual weights are more than 10x as likely to do the "uber" stuff as the default non-perceptual weights.

I changed the threshold to be numPixels * 0.875f * the sum of the weights. This will keep the default behavior for non-perceptual weights, and will stop making other methods do the extra uber stuff for really low error blocks. This is a performance optimization.

) "evaluate_solution()" did something odd for 4-bit indices, which is only mode 6. It also only did this for non-perceptual error; perceptual error tries all 16 options.

It rounded to the nearest index assuming linear interpolation, then tried that index and the previous index. If you were to take an index and the previous index, I'd expect to start with "ceil" instead of "round", so that you're trying the integers on either side of the fraction. For example, if you decide you want index 3.4, this would round to 3, so it would try indices 2 and 3. I think it makes more sense to try indices 3 and 4, so I switched it from "round" to "ceil".

Now, the indices aren't actually evenly spaced. This code assumes the fraction "f" used for index "i" is simply "f = i / 15", so you can go backwards using "i = f * 15". In fact, the fraction for an index is defined to be in fixed point with 6 bits of precision, so the actual math is "f = ((i * 64 + 7) / 15) * 0.015625", where this is a mix of standard C++ integer and float math. In all float math it would be "f = round( i * 64 / 15 ) / 64".

The actual palette lookup is a bit more complex than even this. It first decodes the two end points to 8-bit integers. Then, it interpolates those integers using the 6-bit interpolation factor, and rounds the final result to an 8-bit integer. So, the palette entries may not actually approximate a line very well at all, especially when the end points are near each other but not equal. The code ignores the effects of this second rounding when choosing the indices to try. With non-uniform error weights, I could see situations where the best index is not actually where we predict. I think this is why most modes try all indices, not just the most likely 1 or 2.

Anyway, we can encapsulate the rounding in a random error "e", such that "f = i / 15 + e". It is obvious that "|e| <= 1/128"; rounding introduces up to +/-0.5 error, and we divide that by 64. Going backwards, "i = (f - e) * 15 = 15 f - 15 e".

So, we can use "i0 = round( 15 * f - 15/128 )" and "i1 = round( 15 * f + 15/128 )" to get upper and lower bounds, respectively, for the nearest index. The old code could miss the nearest index by only looking at indices that were too low.

To fix this, I just changed "round" to "ceil". There is never a case where "ceil( 15 * f ) < round( 15 * f + 15/128 )", since "ceil(x) ~= round(x + 0.5)" (they can only differ when the fraction of x is 0.5). Similarly, there is never a case where "ceil( 15 * f ) - 1 > round( 15 * f - 15/128 )". So, this will now try the two indices on either side of the index predicted by assuming linear interpolation, which will always try the nearest index, and will almost always try the second nearest index.

It may not actually try the second closest index. For example, if "f * 15 = 2.001", it will try indices 2 and 3. It could be the case that the fraction for index 1 is closer than the fraction for index 3 to the ideal fraction. But when this happens, the nearest fraction is always much closer to the ideal fraction than the second nearest fraction, so it should never matter. It only really becomes important to try both fractions when you're close to the transition between indices, which will be when "f * 15" has a fraction somewhat near 0.5. Using "ceil" will always try the two closest options in this case, where "round" would only try the two closest options about half the time.

) BC7 mode 6 uses 7777.1 end points, meaning that you get 7 unique bits for each of RGBA and 1 shared LSB bit (the parity or p bit). So, all channels are even or odd. It also has 4-bit indices. So, this is a pretty good format for many blocks, even fully opaque blocks.

However, the BC7E compressor for fully opaque blocks was choosing if the p bit should be 0 or 1. If it chose 0, alpha for the opaque block would change from 255 to 254. When testing the error, it only looked at RGB and not alpha, because it knew alpha was always 255, so the error metric didn't actually register any error for the alpha changing.

My fix is to make the p bits always 1 for mode 6 for fully opaque blocks. This forces alpha to stay 255. It may cause the other colors to compress slightly worse, but keeping alpha 255 is more important for us. This fixes a thin gray line over some dark art. The thin gray line was actually the bright background seeping through the alpha 254 transparency. You can disable this by setting "force_pbits_to_1" to false in "find_optimal_solution".

---
## [YosiSF/EinsteinDB](https://github.com/YosiSF/EinsteinDB)@[8dacf47b5a...](https://github.com/YosiSF/EinsteinDB/commit/8dacf47b5a4a704e430746942aad0031a82712bf)
#### Thursday 2022-01-27 17:03:59 by Karl Whitford

probably make all hashmaps implement consuuuu

// clone https://www.github.com/Mozilla/Mentat
//inside the program navigate to the folder 'db'
//open src/db.rs

/*
Datomic used to expose :db.fn/retractEntity and
:db.fn/retractAttribute, but there latest Cloud offering has only
:db/retractEntity. Since that's what I am interested in using, that's
all I've implemented.

This transformation doesn't follow the existing pattern of inserting
into the temp.*_searches table. It instead populates
temp.search_results directly from datoms, and in so doing it makes
some assumptions about how the searches tables will be accessed.

It might be even more efficient to have an entirely new temporary
table just for these retractions. One advantage with the current
scheme is that indexing restrictions placed on the search results
table will apply to the datoms retracted by :db/retractEntity as well.

There are a few remaining items TODO.

TODO: ensure that we mark the schema as potentially modified when we
:db/retractEntity. It's not clear to me how to do this efficiently.

TODO: ensure that transaction watchers get the correct transacted
datom stream. I didn't try to address this yet because it appears to
me that the existing watcher implementation isn't quite correct: it
tells watchers about datoms that are potentially to be transacted but
not about datoms that actually are transacted. This, of course,
matters when watching :db/retractEntity entities being transacted.
*/

use std::collections::HashSet;
use std::collections::HashMap;
use eavt;
use event;
use mentat_db as db;
// use mentat_store as store;
// use mentat_query as qm;

/* define the interface that datoms need to implement */
trait EntityFn { fn entity(&self) -> eavt::Entity ; }  //: EntityFn { }
impl EntityFn for eavt::Datom { fn entity(&self) -> eavt::Entity { self.entity() }}  //: DataPoint {} }

/* Given two input streams of datoms (the old and the new), figure out the set difference */
fn diff<'a, T>(datoms_new: T, datoms_old: HashSet<eavt::Datom>) -> Vec<eavt::Datom> where T : Iterator<Item=&'a eavt::Datom> + ExactSizeIterator {

    let mut ret : Vec<eavt::Datom> = vec![];

    // keep a set of the indices of elements we've seen so far. This is imprecise but should be good enough.  Really, I'd just like to not have a hset in Rust. It's silly!
    let mut seen : HashSet<usize> = HashSet::with_capacity(datoms_old.len());

    /* loop over each value in the new dataset. Compare it against each element in the old list, saving nonduplicates into a vector we build up before returning it. */
    for d in datoms_new {

        /* skip over any seen values */
        if seen.contains(&(d.position())) { continue }

        /* if we haven't seen it yet, check against all previous values */
        for old in &datoms_old {

            /* if this new value matches an old value we've already seen, no need to include it again */
            if d == *old { break }

            /* otherwise, continue searching */

        } // next old value in list of old values considered so far

        /* since we made it through all the matches without finding a match, add this value to our output array and mark it as such with an index */
        ret.push(*d);  // TODO actually clone datom rather than move vals around? don't really want `clone` types everywhere...? Or maybe I want abstractions around cloning... Ultimately I want something that isn't generic over types... Like an assignment operator instead? Or maybe `consume` -- take ownership of everything? That sounds nice... But there are SO MANY rocks that are caught in cloning paths that call mea culpa here... Plus the 'make everything generic constraine types' thing seems like its short-term thinking at best -- when specific problems arise, carve out what you need and leave the rest wherver you find them (I suppose!)... No dicts and hashes are currently a major pain point!! Grrrr!! ... TODO probably make all hashmaps implement consuuuu

---
## [JRDead/KirieStation](https://github.com/JRDead/KirieStation)@[0b5947a20f...](https://github.com/JRDead/KirieStation/commit/0b5947a20f2f218ad0e3f972add1e6ea5a90a9b5)
#### Thursday 2022-01-27 17:24:24 by Kirie Saito

6 MONTHS. SIX FUCKING MONTHS OF THIS CRAP I FINALLY FIXED IT (#376)

FUCK YOU

---
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[5faedc3759...](https://github.com/LumberKing/Tianxia/commit/5faedc3759e51764c7bb312dcce155a1cdf346e1)
#### Thursday 2022-01-27 18:24:50 by Silversweeper

Balance/optimization/polishing (part 8 of ???) + Fujiwara improvements (4 of ???):

Casus Belli:
- Cleaned up old, irrelevant CBs related to Decadence for Chinese dynasties. That hasn't been relevant since JD...
- Cleaned up old, unused Chinese county conquest CB. Another CB that's not ben relevant for a good while...
- Wars to overthrow the Permanent Regent can now end in a white peace, restoring the regent but not punishing the liege aside from a prestige loss.
- Wars to overthrow the Permanent Regent waged against the Regency Loyalists no longer end the Permanent Regency on a white peace.
- If the prospective Shogun loses the war to become the Shogun and has selected someone as their would-be Tenno this would-be Tenno will now be regarded as a traitor by the Tenno.
- Added Permanent Regent-related factions for the Ryukyuan knockoff.
- Added new CB for valid Imperial Family members to press de facto claims on the Chrysanthemum Throne.
- Added new CB to press the de facto claims of valid Imperial Family members on the Chrysanthemum Throne.

Council voting:
- AI Permanent Regents will no longer be Loyalists unless they are friends or lovers of their liege.

Governments:
- Imperial (roman_imperial_government) is no longer an option for anyone that'd be eligible for any of the assorted eastern governments. This prevents certain weird scenarios that'd potentially cause a government switch, e.g. a character eligible for Japanese Bureaucracy being Imperial one moment and losing it the next because a vassal happened to inherit the Chrysanthemum Throne.

Landed titles:
- Reordered the de jure vassals of e_japan a bit so that d_rokuhara hopefully takes precedence over other Fujiwara-held duchies as far as title naming goes.
- k_chrysanthemum_throne is now even more difficult to recreate, because you shouldn't ever need to.

Laws:
- The Tenno now always has access to Absolute Cognatic Succession, as should the Ryukyuan knockoff if they didn't pick Agnatic/Enatic Clans.
- The Tenno no longer has access to Enatic Succession under any conditions.
- Neither the Tenno nor the Ryukyuan knockoff have access to Agnatic-Cognatic or Enatic-Cognatic Succession any longer.
- Added (still WIP) Ryukyuan knockoff of the Tenno's succession law.
- Unreformed and Reformed Ryukyuans can now use Agnatic unless blocked for specific reasons (e.g. Equality or Enatic Clans).
- Chinese/Eastern/Japanese/Divine Imperial, Confucian/Japanese Bureaucracy, Japanese Feudal, and Japanese Monastic Feudal rulers should no longer default to Agnatic-Cognatic, and will therefore default to Agnatic outside of Japanese/Divine Imperial (defaults to Absolute Cognatic unless barred due to Doctrines). Certain historical realms are still scripted to start with Agnatic-Cognatic, e.g. Silla.
- Various flavours of bureaucratic realms now default to the council having all powers except the last one (forced Elective).
- Restructured the Regency Power laws as a single group, and made some other changes to them.
- The Tenno and the Ryukyuan knockoff are now locked into their respective succession laws as far as secondary titles go as well, which generally will mean they have the same heir in AI hands.

Minor titles:
- The Tenno now gets the extra advisor for emperors even if he doesn't hold an emperor-tier title.
- The Ryukyuan knockoff now gets both advisors even as a duke or king.

Objectives:
- Removed the plots (Tenno and Shogun) to become a Permanent Regent; use the faction instead!
- None of the Japanese factions (for becoming the permanent regent (either kind), being a regency loyalist (either kind), becoming the shogun, or ousting the shogun) are now blocked for council members.
- The faction to become the permanent regent now requires the prospective faction leader to be a king, be a duke with 1000 prestige and a regency bloodline, or be a duke with 5000 prestige (comparable to the Shogunate faction's conditions) unless the liege already has a non-permanent regent. The faction leader gets to stay in charge if the regency ends.
- Made the AI less willing to start a faction to give the Shogun a Permanent Regent unless they have an active Regency bloodline, and also made it less willing to back such a faction unless the faction leader has such a bloodline, seeing as the Ashikaga Shoguns shouldn't have to be overly concerned about this threat. This does not apply if the Shogun already has a regent.
- Updated relevant faction logic to let unreformed/sensibly reformed Ryukyuans join the fun that is the Japanese government faction mess. A Tenno knockoff cannot join the fun, but he can (TODO) be the target of some of the fun.
- Vassals that'd hypothetically be eligible for Chinese Imperial will now not start factions to put women on the throne of a Chinese Imperial empire if the title is Agnatic unless they happen to be female, and will also be unwilling to back female claimants. You're supposed to faction for their male children; silly AI!
- It is no longer possible to start or join claimant factions against the Tenno if you are someone that cares about the Tenno, or to start them on behalf of someone that cares about the Tenno... unless it's for some kingdom (other than k_chrysanthemum_throne) he holds and he also holds an emperor-tier title. In that case, still no claiming it for members of the Tenno's dynasty. If you are someone that cares about the Tenno, you'll have to use the Shogunate faction if you want to take his empire title (or you can become the Permanent Regent, if you prefer a less direct approach) and you're not from his dynasty. If you're from his dynasty, well, see below.
- Started work on adding the Ryukyuan knockoff's Permanent Regent/Regency Loyalist factions.
- Made the AI very unwilling to support claimants that'd switch the realm from assorted eastern governments to other kinds of feudalism if they can have one of those assorted governments, particularly within subgroups (e.g. a character with Japanese Bureaucracy will be more concerned about a Japanese Feudal liege being replaced by someone that'd have regular Feudal than they'd be about a Chinese Imperial liege being replaced by a regular Feudal liege), as well as the opposite way around.
- Chinese and Japanese viceroys no longer consider "I am a viceroy!" a reason to be more eager to seek independence if their liege has a government they approve of (Chinese Imperial in the former case, Japanese/Divine Imperial in the latter).
- The AI should now be considerably less likely to seek independence if their liege has a Permanent Regent if it cares about such things and is a de jure vassal.
- AI Japanese Bureaucracy/Feudal/Monastic Feudal de jure vassals should not seek independence from a Shogun if they instead could restore the Tenno's rule.
- AI Japanese Bureaucracy/Feudal/Monastic Feudal de jure vassals should not seek independence from the Tenno if they could become the Shogun.
- AI Confucian Bureaucracy viceroys are now less likely to seek independence under a Chinese Imperial liege unless the Mandate rating of the liege drops below Average unless they also have non-viceroy titles of the same tier.
- The AI Tenno shouldn't ever seek independence if under a Japanese Bureaucracy/Feudal/Monastic Feudal liege; overthrowing the Shogunate is obviously better.
- If the Mandate rating of a liege drops below Average Confucian Bureaucracy vassals will become more eager to seek independence.
- Added new faction to press de facto claims of valid Imperial Family members on the Chrysanthemum Throne.
- The Tenno is no longer blocked from the End Shogunate faction by having a regent, but an actual regency is still a blocker.
- The AI is now more likely to join the Regency Loyalists if the Permanent Regent has managed to shift the Regency Power laws far in his favour.

scripted_triggers/_effects/_score_values:
- AI-controlled characters with a bureaucratic (Chinese Imperial/Eastern Imperial/Confucian Bureaucracy/Japanese Imperial/Japanese Bureaucracy/Divine Imperial) government will now not take to the field personally unless they a) are commanders, b) are marshals, c) have a martial education, or d) are members of either the WotRS or the Hwarang.
- Shinto is now considered a spiritual "culture" rather than a warrior "culture". It's a bit more historical.
- Tolerant reformations now make you a spiritual "culture" rather than a diplomatic "culture", thus bringing you closer to the Eastern religions.
- Added/reworked/removed a bunch of things related to Japanese government stuff, e.g. the abdication/usurpation logic when the Tenno is abdicating/being usurped.

Societies:
- Much to the displeasure of the Sohei, monks (and nuns) are no longer permitted to become Warriors of the Rising Sun, seeing as it has some potential issues.

succession_voting:
- Overhauled the voting logic for the Tenno's succession law substantially.
- Did most of the preliminary setup for the Ryukyuan derivative of the above.
- Shinto electors will now be more likely to vote for Amaterasu Descendants in assorted elections, should that end up being relevant.

Traits:
- Added a Daijo Tenno trait.
- Added (still not fully implemented) Ryukyuan equivalents to under_regency and japanese_regent.

Decisions:
- Cleaned up some commented out script.
- Added a decision for the Tenno to found Heian-kyo if you start in 769. It's kind of an important city, so you should...
- Removed the now irrelevant decision to meddle/cancel meddling in the Tenno's succession.
- Cut the "Hey, can I be your Permanent Regent?" decisions and the "Hey, could you end this whole Permanent Regency thing, please?" decisions. Use the ultimatums, and fight for it if necessary.
- If you or your liege have a bureaucratic government the "Request land for Son/Daughter" decision now requires a valid adult son/daughter.
- Fixed several issues with the regency powers, added a few more, and did some general polishing.
- Added a targeted decision for the Tenno to give the Taira surname to Imperial Family members, working effectively the same way as the decision to give someone the Minamoto surname. This decision is impossible to use after the Genpei War, seeing as the Tairas lost. The AI will not use it, due to the risk of it stupiding the Imperial Family into extinction.
- Added a player-only (the AI does it using an on_yearly_pulse event) decision to restore an agnate to the Imperial Family.
- If the Tenno uses the special decision to recreate Japan while holding the de jure liege title of a Japanese kingdom (including Ezo and Ryukyu) the title in question will instantly de jure drifct into Japan.
- If the Tenno uses the special decision to recreate Japan while holding a Japanese kingdom (including Ezo and Ryukyu) the title in question will instantly de jure drifct into Japan

Events:
- Permanent Regents are now checked roughly every month, instead of every instance of anyone getting a regent checking if there should be a different regent.
- If the Tenno dies without a dynastic heir (and it hasn't happened before), k_chrysanthemum_throne and any held empires and kingdoms are immediately destroyed and Shinto MA is hurt massively.
- Cleaned up old events related to Japanese government stuff that no longer are relevant.
- Restructured still relevant Japanese government events.
- Reworked Japanese government trait inheritance so that all unlanded children (of an appropriate gender) of a title holder that are eligible inherits the trait.
- Characters being landed (in any fashion) by someone with Japanese Feudal/Monastif Feudal that'd be eligible for that government now get the option to swap to the that government.
- Characters usurping a new higher tier title from someone with Japanese Feudal/Monastif Feudal that'd be eligible for that government now get the option to swap to the that government.
- Characters inheriting a new higher tier title from someone with Japanese Feudal/Monastif Feudal that'd be eligible for that government now get the option to swap to the that government.
- If the Shogun, Shogun's PR, Tenno's PR, or Ryukyuan knockoff's PR receives a request for land for a son/daughter they can now take a title off of other relevant parties (with special protection for c_yamashiro if it's held by the Tenno).
- Significantly improved the regnal name selection for the Tenno.

Graphics:
- The Disinherited trait now has an icon. I suppose that's why vanilla had it hidden...

History:
- More Fujiwaras and related title history.
- Corrected some imperial reigns, and added Daijo Tenno traits where relevant.
- e_japan and k_chrysanthemum_throne are now scripted to start with Absolute Cognatic succession whenever the Tenno is in charge. Women are still unlikely to be elected.
- Posthumously recognized emperors of Japan now have their posthumous names.
- Set up starting laws for a few more titles.
- Most bureaucratic realms now start with the council having all powers (except the one that'd force Feudal Elective, which of course is disallowed).
- Various Confucian Bureaucracy realms that are NOT among the Ten Kingdoms are now scripted to start with Only External Vassal Wars.
- Various Chinese Imperial realms that are NOT among the Five Dynasties and Ten Kingdoms are now generally scripted to start with Disallowed Vassal Wars. Tang is an exception to this, starting with Only External Vassal Wars since the An-Shi Rebellion didn't leave them in a good spot.

Localization:
- Ashikaga Takauji will no longer claim to be ruling the "Ashikaga Empire". He knows better than that!

---
## [SK0lll/NEPS](https://github.com/SK0lll/NEPS)@[8a69c714ea...](https://github.com/SK0lll/NEPS/commit/8a69c714ea0126844bdd16756e154d58347ece4d)
#### Thursday 2022-01-27 18:27:36 by MrJohnnyAppleseed

Fix crashing bug

We all know that when all Terrorists die and manage to plant the bomb, they all begin to spectate the bomb. When that would happen, it would cause the cheat to read the eyeangles of the bomb, which would just result in an error and a instant crash. This should add a check to prevent this bug from occurring again.

---
## [ChristopherFrydryck/Riive](https://github.com/ChristopherFrydryck/Riive)@[7c72f04577...](https://github.com/ChristopherFrydryck/Riive/commit/7c72f045773df37bfc402699fd7944c7c7fd2ba7)
#### Thursday 2022-01-27 20:22:21 by Christopher Frydryck

Holy fuck I hate location based bullshit. I think android is working now?

---
## [betrusted-io/xous-core](https://github.com/betrusted-io/xous-core)@[ea31f54a79...](https://github.com/betrusted-io/xous-core/commit/ea31f54a796680df704067d4da7cb38015cc2d7d)
#### Thursday 2022-01-27 20:27:21 by bunnie

console escape codes working better

just couldn't let it go. figured out the issue is a race condition
in how the Litex UARTs are constructed...I don't know how Litex
normally handles this kind of situation but they have this funky
construction where reading the fifo doesn't advance it, you have
to...clear the pending bit. I think it was meant to be a "clever"
thing that saves an instruction or something like that since you
always have to clear the pending bit.

Anyways, the previous incarnation of this loop checked to see
if the pending bit was set again and if it was it'd run back
and fetch another character. This turns out to be a bad idea
because the pending bit goes through a multireg and other stuff
before it's readable which means it has a lot of delay on it.
This leads to a race condition.

This version actually checks if the fifo is empty and if it isn't,
it reads the character *and* pumps the pending bit (because
the FIFO doesn't auto-advance when you read it, you have to clear
the pending bit).

This works a lot better, but it's not at all well documented how
this works and it's very hard to tell from reading the source code
because it's written using really fancy migen abstractions that
are also poorly documented and have a lot of cursed constructions.

Anyways. At least the console doesn't die now when you type
a control character, *but* you do have the problem that the
escape codes get mis-interpreted sometimes. If it really really
becomes important later on to fix that it would involve tracing
out the sequence of keys that arrive at InjectKey and figuring
out if things are coming out of order or what is triggering the
bad escape codes.

---
## [Fabsoll/AtYourMercy](https://github.com/Fabsoll/AtYourMercy)@[372ec99405...](https://github.com/Fabsoll/AtYourMercy/commit/372ec994058f8c6a0734caae96d8c140cfedb55b)
#### Thursday 2022-01-27 20:41:37 by nosebleed42069

MY FUCKING GOD THE FINAL FUCKING FIX FOR THE STUPID LITTLE IDIOT TRAITS

---
## [zombocom/dead_end](https://github.com/zombocom/dead_end)@[084688196b...](https://github.com/zombocom/dead_end/commit/084688196bc070bfa85ac6591d31bd5cfc584bbc)
#### Thursday 2022-01-27 22:17:18 by schneems

WIP handling invalid nodes

Really loving these properties

I don't want an invalid node to "capture" a valid one. We can prevent this by ensuring that the blocks are always built from the inside out. 

For example if we're going up and see `)` It's a sign that above us is building a valid block. If we grab it now, it means the the above code couldn't just be 

```
(
 # inner
)
```

It would have to be 

```
(
  # inner
)
# plus extra stuff here
```

Which we don't want. If all the code is completely valid then we'll eventually build correct blocks. Otherwise (I'm hoping) that we'll preserve relatively logical blocks that isolate their own syntax errors.

One unknown is how a :both leaning line would do here. I think if we are expanding up a line leaning "both" would need to expand down so we should capture it. Same follows for expanding down. So I think the current logic will hold, but perhaps there will be edge cases to find.

Either way, this is quite an exciting development. I am hopeful that this is the right path.

I want to keep working on the tree logic, adding some more tests. Then I want to take a stab at building an algorithm that searches the tree. We can't purely rely on leaning when doing a search, as the syntax error could be due to missing `|` or an extra comma etc. However it might inform us as to which nodes to look at first as long as we fall back to checking all nodes (if those prove to not hold the full set of syntax errors.

Also worth noting that I think we'll have to completely re-visit the "capture context" logic. As it was mostly based on the blocks that the prior search produced. This new search will make different shaped blocks. We should optimize for speed and quality. The "bad" blocks returned should contain the error, and we should do it fast. Later on we might want to split the blocks up, say by chunking into logical blocks at the same indentation based off of newline/whitespace as the old algorithm did. 

This new algorithm throws away empty/double-newline lines currently. That allows us to completely get rid of any "is this line empty" checks which littered the prior algorithm. It's better to normalize and build a general algorithm that works and doesn't have to handle edge cases. Then later go back and clean up the results instead of making the search/tree-building overly complicated just to simplify showing results.



TODO: 

- Set a max bound iterations for building tree? Could be nice
- Build a reporter for building the tree
- Build a reporter for searching the tree

---
## [Calinou/godot-docs](https://github.com/Calinou/godot-docs)@[b872229427...](https://github.com/Calinou/godot-docs/commit/b872229427dddb9b749f46af597e85e25cf2955a)
#### Thursday 2022-01-27 23:24:11 by Rémi Verschelde

Remove controversial satirical piece 🔥

This piece was written back in 2014 before open sourcing Godot, and while its
intent is to be sarcastic, it leaves ample room for misinterpretation.

The intended meaning of this piece was, and always has been, the following:

Exploitative game mechanics suck. Games are a beautiful and artful medium
which can provide players with a wide range of experiences: entertainment,
enlightenment, joy, sadness... Games can be just for fun or they can bear
a message. They can connect people with each other or open the player's mind.

Make games worth your players' time and their money, and do your best to do so
while running a successful and respectful business. Hugs <3

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[cd97725d8b...](https://github.com/mrakgr/The-Spiral-Language/commit/cd97725d8bff7cc27db02899dc579f58003df8fd)
#### Thursday 2022-01-27 23:41:26 by Marko Grdinić

"9:50am. I feel absolutely fucked up. Whatever this cold is, it seem to be going after my brain. Right now I keep having pangs of pain near the base of my right ear. I am lightheaded as well and feel light chills. No way can I study in this condition.

11:30an. I guess I'll spend today gaming. If not on days like this, then when else? Right now, I am playing Lona RPG. It caught my eye and I do not feel like playing Dohna Dohna or LoboCorp.

Let me have breakfast here.

11:50pm. It feels the cold is going away, but I still have those annoying pangs of pain in my right ear base. Aghhhhh!

It really is agonizing. Hopefully it passes by tomorrow. If it does I should be able to resume studying tomorrow.

12:20pm. Brrrr, I am getting the chills. Let me eat and I am heading to bed. This would be a lot more bearable if it weren't for the ear pangs."

---
## [Peksterix/NYPxTrident](https://github.com/Peksterix/NYPxTrident)@[552fc2e4bb...](https://github.com/Peksterix/NYPxTrident/commit/552fc2e4bbe37738fc87af86dc1db2c9f8afa2ee)
#### Thursday 2022-01-27 23:43:38 by Peksterix

24 hours no sleep, brain empty and i want to die. I dont remember what i did in this commit

---

