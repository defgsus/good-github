## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-17](docs/good-messages/2021/2021-12-17.md)


3,190,428 events, 1,749,540 push events, 2,715,996 commit messages, 198,550,432 characters


## [ksh93/ksh](https://github.com/ksh93/ksh)@[c5018f7c95...](https://github.com/ksh93/ksh/commit/c5018f7c9523a1e9d2039ae83caf52a8011dec82)
#### Friday 2021-12-17 00:19:26 by Martijn Dekker

Re-fix defining types conditionally or in subshells (re: 5cc9fcc1)

New version. I'm pretty sure the problems that forced me to revert
it earlier are fixed.

This commit mitigates the effects of the hack explained in the
referenced commit so that dummy built-in command nodes added by the
parser for declaration/assignment purposes do not leak out into the
execution level, except in a relatively harmless corner case.

Something like

    if false; then
        typeset -T Foo_t=(integer -i bar)
    fi

will no longer leave a broken dummy Foo_t declaration command. The
same applies to declaration commands created with enum.

The corner case remaining is:

    $ ksh -c 'false && enum E_t=(a b c); E_t -a x=(b b a c)'
    ksh: E_t: not found

Since the 'enum' command is not executed, this should have thrown
a syntax error on the 'E_t -a' declaration:
ksh: syntax error at line 1: `(' unexpected

This is because the -c script is parsed entirely before being
executed, so E_t is recognised as a declaration built-in at parse
time. However, the 'not found' error shows that it was successfully
eliminated at execution time, so the inconsistent state will no
longer persist.

This fix now allows another fix to be effective as well: since
built-ins do not know about virtual subshells, fork a virtual
subshell into a real subshell before adding any built-ins.

src/cmd/ksh93/sh/parse.c:

- Add a pair of functions, dcl_hactivate() and dcl_dehacktivate(),
  that (de)activate an internal declaration built-ins tree into
  which check_typedef() can pre-add dummy type declaration command
  nodes. A viewpath from the main built-ins tree to this internal
  tree is added, unifying the two for search purposes and causing
  new nodes to be added to the internal tree. When parsing is done,
  we close that viewpath. This hides those pre-added nodes at
  execution time. Since the parser is sometimes called recursively
  (e.g. for command substitutions), keep track of this and only
  activate and deactivate at the first level.
     (Fixed compared to previous version of this commit: calling
  dcl_dehacktivate() when the recursion level is already zero is
  now a harmless no-op. Since this only occurs in error handling
  conditions, who cares.)

- We also need to catch errors. This is done by setting libast's
  error_info.exit variable to a dcl_exit() function that tidies up
  and then passes control to the original (usually sh_exit()).
     (Fixed compared to previous version of this commit: dcl_exit()
  immediately deactivates the hack, no matter the recursion level,
  and restores the regular sh_exit(). This is the right thing to
  do when we're in the process of erroring out.)

- sh_cmd(): This is the most central function in the parser. You'd
  think it was sh_parse(), but $(modern)-form command substitutions
  use sh_dolparen() instead. Both call sh_cmd(). So let's simply
  add a dcl_hacktivate() call at the beginning and a
  dcl_deactivate() call at the end.

- assign(): This function calls path_search(), which among many
  other things executes an FPATH search, which may execute
  arbitrary code at parse time (!!!). So, regardless of recursion
  level, forcibly dehacktivate() to avoid those ugly parser side
  effects returning in that context.

src/cmd/ksh93/bltins/enum.c: b_enum():

- Fork a virtual subshell before adding a built-in.

src/cmd/ksh93/sh/xec.c: sh_exec():

- Fork a virtual subshell when detecting typeset's -T option.

Improves fix to https://github.com/ksh93/ksh/issues/256

---
## [pauamma/git_ports_journal](https://github.com/pauamma/git_ports_journal)@[361d1a8453...](https://github.com/pauamma/git_ports_journal/commit/361d1a84533acbedaf0631cc1c15b07088120cf2)
#### Friday 2021-12-17 00:26:55 by Pau Amma

First (and likely only) round of line edits.

- "From an implementation perspective" Clarity: if you mean "implementation" as in "how git and workflow fit together, I'd use "project-wide workflow" instead. If you mean "how git works", it's design and use, not implementation. I'm assuming the latter.
- "The history of a Git repository can be considered as a directed acyclic graph with nodes of the graph repository snapshots." Concision, completeness: "can be considered as" -> "is", "nodes of the graphs repository snapshots" -> "nodes of the graphs being repository snapshots" (and I'd add something about what edges are, maybe "and edges being commits").
- "Creating a new branch means starting a new line of development" Clarity: define "line of development", or maybe better, list (here or later) what a port maintainer is likely to use a new branch for (if that port maintainer is me, that's almost always "upgrade to new upstream version", but may not be that for a port committer or even maintainers who are not me). Going for "; for ports, it will usually propose a new port or upgrade an existing one you maintain".
- "From a user perspective, support for lightweight local branches and the simplicity of switching between and merging the work of different branches is..." Sentence flow, concision: rewriting as "...Git's support of lightweight local branches, easy switching between branches, and merging different branches are..." "...Git’s defining feature" Terminology quibble: I'd write "strong points" instead, because you wrote earlier "the defining property that makes Git different" and while they each can be "a defining (mumble)", they can't be both be "the defining (mumble)" IMO. (Which also means that if you want to keep "defining" here, you need to change "the" to "a" both here and in that earlier use.)
- "we value a simple linear history" Precision and accuracy: changed  to "the ports committers require".
- "so viewing the history of the FreeBSD ports main branch under Git looks similar to how the history looked under Subversion" Concision: "so the history of the FreeBSD ports main branch under Git looks similar to how it looked under Subversion"
- "This requires certain constraints when developers" Precision: again, I'd say "port committers".
- "a different workflow that results in parallel paths along in the main branch" Accuracy, grammar: I'd reword it as "a different overall process that relies on parallel paths along with the main branch" (which is sorta-kinda what FreeBSD does for ports too - see quarterly port branches).
- "at the time of writing" Future-proofing: I used "starting in October 2021" with a few other tweaks to that sentence.
- "This can only happen when the output of git log --oneline main..freebsd/main descends from the local main branch." Clarity, text flow: I'd swap this and the next sentence and use "To check whether this is the case in your local main branch, run git log --oneline main..freebsd/main and check for any local changes.
- "This can only happen when the output of git log --oneline main..freebsd/main descends from the local main branch." Clarity, text flow: I swapped this and the next sentence, tweaked that, and used "To check whether this is the case, run git log --oneline main..freebsd/main and check for any local changes." This is clearer wording for what I think you mean, but I'm only about 60-70% confident I interpreted that correctly, so proceed with caution.
- "As a convenience, there is a ~pull~ command that will do both the ~fetch~ and ~merge~." Concision, precision: "...the ~pull~ command will ~fetch~ then ~merge~."
- "Now that we are able to keep our repository copy up-to-date with git.freebsd.org/ports.git, let's start to think" Concision: "Now that we can", "let's think".
- "Start by creating a new feature branch to work on the new nyxt port." Completeness: I added a link to https://docs.freebsd.org/en/books/porters-handbook/new-port/, but check my markup in case I misunderstood the link markup syntax you used elsewhere.
- "If you ever want to check which branch you have checked out, you can run" Concision, tone: "To check which branch you have checked out, ..."
- "At the time of writing there is only one hook in that location, prepare-commit-msg, which..." Future-proofing, nomenclature: I made that "That directory contains the prepare-commit-msg hook, which..."
- "There should be a short subject line" Consistency with git-commit(1): Added "no more than 50 characters" and mentioned the blank line git expects before the commit message body.
- "To recap" EFL friendliness: "To recapitulate" or "So far" (went with the latter).
- "Once you have poudriere set up, we can test our port." Pronouns consistency: use only one of "you" and "we". (I went with "you"/"your" for all 3.)
- "for run-time testing terminal application" Grammar, EFL friendliness: "for testing terminal applications".
- "From PKG.CONF(5)," Consistency with actual manual page; used lowercase.
- "you snapshotted your work at the end of the day with a commit containing a message with..." Taste, concision: "you committed a day's work with a log message containing...".
- "pkg install arcanist-php74" or the one for your PHP version, eg arcanist-php80.
- "poudriere testport 12/13 amd64/arm64" Consistency with FreeBSD nomenclature: "aarch64", not "arm64".
- "www/nyxt: New port for the Nyxt browser" Consistency: per https://docs.freebsd.org/en/books/porters-handbook/quick-porting/#porting-submitting, make it "[NEW PORT] www/nyxt: New port for the Nyxt browser".
- "In the description you can add the information the rest of the commit log and any other information helpful for others reading the bug, like a link to the phabricator review." Concision, missing word: s/the information the rest of the commit log/the rest of the commit log message/ Accuracy: Phabricator review link would go in "See also" (and it needs an uppercase initial).
- "When there simple updates to your port that only contain ..." Grammar, taste: "When your port update is simple and only contains ..."
- "It is sufficient to ..." Taste, concision: "... is enough."
- "Many FreeBSD developers and contributors who dedicated significant time to becoming productive using Subversion," Punctuation: remove this comma or add one after "contributors". (Went for the latter.)

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[803292b879...](https://github.com/willior/Action_RPG_1/commit/803292b879992079aaea982b04d711d48ce4e60c)
#### Friday 2021-12-17 00:32:17 by willior

re-doing buttons...

hover & focus have been divorced in 3.4 so my button visuals have to be completely redone.
since the theme override system has been overhauled, i am just going to do things with themes, from scratch, which will take time but will save headaches in the future, i guess. who the fuck knows. i'm always planning to avoid headaches and end up causing more in doing so. there seems to be no correct way to go about doing this in a manner that doesn't waste colossal amounts of time. it seems the only way to learn how to go about doing this is to fuck up, repeatedly, over and over again. if you keep doing this, every day, there is a microscopic chance that you'll arrive at where you desire. but more often than not, you will end up wasting hours and days of your time,  you will have learned nothing, and there is no possibility to get back that lost time.
looking at the changed files, i've noticed a lot of changes to margin values that i did not make. just another wonderful thing about working with control nodes: changing one thing changes all the others, there is no way of stopping this, and no way of re-doing it. deal with it, you fucking bitch. the worst part is i have no idea what has actually changed because of this and will have no way of knowing until i finish re-doing the buttons, at which point i will realize it's all fucked up and will likely have to start over, again. i will have no way to prevent this from happening. i will simply have to waste my time, knowing that i am wasting my time, and then arriving at a point having learned nothing, after time has been wasted.

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[d7b1d064cd...](https://github.com/i3roly/glibc_ddwrt/commit/d7b1d064cd2f7c1a83d4e953f792314300f494f7)
#### Friday 2021-12-17 00:32:35 by gagan sidhu

47859,(mb?) fix sftp server."autotune is the new magic" - randy marsh

- include the updated openvpn

- i noticed that the dd-wrt logo would go missing in firefox but not
safari. i suspected this had something to do with the javascript files
so i fixed it, or at least the logo appears for me now. maybe it already
appeared for others.

- i have tried to fix sftp-server. i observed that the client coudln't
sftp into the router. i am hoping the addition of the /etc/sshd_config
file will fix this problem, but i have not tested this.

in spite of not testing the proposed sftp-server fix, i have actually
tested this build (it doesn't have /etc/sshd_config is all).

don't like it? G F Y - the washington MF redskins

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
## [MartyX5555/ACE-Dev](https://github.com/MartyX5555/ACE-Dev)@[6784d8c86b...](https://github.com/MartyX5555/ACE-Dev/commit/6784d8c86b9e6a756e992701c05285723ded8e8e)
#### Friday 2021-12-17 01:10:07 by Mr Marty

New fixes and additions, missile rebalance (wip)

-Added sound new concept. This will be used for a future sound update (written in cl_extension.lua since i need to see how stuff will go)
-Improved how HE checks occlussion when applying damage. (beta)
-antimissile little rework (beta): They CAN shot down missiles and reseek again.
-glatgm can be intercepted by radars. Note that it will not return velocity due to requirement to learn how original missiles get its velocity. Weird.
-Missiles/Bombs old fix was polished. Missile detonation is like it was on ACF2 now
-Rack model preview when selecting it
-Fixed ammo crates not displaying guidance data properly (seekcone and viewcone )
-Fixed most of reported bugs from last update. POSSIBLE fix for gearbox displaying a for loop error
-Possible fix for ACE update attempting to fetch a http request before server even start
--Missile rebalance. Its not completed, but most of them were adjusted according to what ive seen ingame and related reports, but:
-AAM: no missile can insta-turn anymore. Done every missile has similar guidance cones, difference is their agility, which makes aim9 more agile than aim120, etc
-ATGM: javelin cannot insta turn inmediately once fired. Increased flight time
-Bombs: Dont fucking use them, although they will not destroy your pc, finding their irl counterparts is a pain in the ass and not easy to balance for me atm.
-SAM: Increased Strela acceleration but reduced agility due to strela insta turning and losing tracking. Attempt to reduce fim92 payload.... bad

If you find a bug apart of what i told you here, let me know.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[d51d6c0de3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/d51d6c0de326a78b97d9750807a05ea33d61c031)
#### Friday 2021-12-17 01:36:35 by SkyratBot

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
## [Mezque/Santa-s-Naughty-List](https://github.com/Mezque/Santa-s-Naughty-List)@[520f8f8f07...](https://github.com/Mezque/Santa-s-Naughty-List/commit/520f8f8f07fe24ca4cb2cb2c6d0d307f6db00dc3)
#### Friday 2021-12-17 03:45:01 by Micah

the file?

But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure? On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains.

---
## [realness-online/web](https://github.com/realness-online/web)@[d28ea55f0d...](https://github.com/realness-online/web/commit/d28ea55f0d8fc0190c45f73719f0e51814abb54e)
#### Friday 2021-12-17 04:20:44 by Scott Fryxelo

Remove US only placeholder stuff

I was worried about those lame cookie message that people have to show. 

fuck that shit. I'm not tracking you. I don't need to EU forcing me to 
tell you that I'm not tracking. 

I should only have to pop that bullshit when I'm doing bullshit

---
## [snitchbcc/articles](https://github.com/snitchbcc/articles)@[ee82cd9bb7...](https://github.com/snitchbcc/articles/commit/ee82cd9bb714160e9f558e1910614f22605f64bf)
#### Friday 2021-12-17 05:00:11 by snitchbot

Upload article 'Everyone's A Critic: HOLY MOTHERFUCKING SHIT! SPIDERVERSE TWO! HELL YEAH!'

---
## [jiffydominguez/CS-330](https://github.com/jiffydominguez/CS-330)@[d0f441feea...](https://github.com/jiffydominguez/CS-330/commit/d0f441feea45c1f51b416001108f3e4ce7c8837f)
#### Friday 2021-12-17 05:19:03 by jiffydominguez

Update README.md

How do I approach designing software?
Some of the skills I learned in this project was to ensure that everything was commented. I had to keep changing one line of code and it would either make or break my image, program, or even the texture. Staying organized made a huge difference in this.
Doing this kept me productive on my project. The biggest part was where I labeled which side and section each vertex was on. This kept it easy to move an entire object, a single vertex, and even the texture.
I will use this to keep all my future programs organized. Thanks to the way I made my program, it is very modular and doing it this way will allow me to be able to reuse some parts or even just change small sections of my code to come out with completely different images. 
How do I approach developing programs?
The biggest development strategy I used for this project was a simple one. I ended up going out and buying graph paper. This allowed me to have a physical copy of what my program would look like. On top of that. Because it was a graph paper, it made it super easy to find out where my points should go on my program. 
The iteration became a huge time consuming this. Especially when trying to make a simple object like a cube. You needed two lines of code per side. However, by staying organized it just became a copy and paste thing where you could just edit two points. This part of the iteration made it run fast after I figured it out. 
Each milestone was just the same program with another thing added to it. This made the final project not seem like such a big deal. Since it was all small sections, it made it much easier with way less anxiety when working on this project. 
How can computer science help me in reaching my goals?
This class gave me a much more in dept understanding about the time and effort some videogames go through. I have taken several years of Autodesk and Blender classes, and this seems like an extremely easier way to make some of the objects. However, OpenGL has some advantages over things like Autodesk so it’s important to keep that in mind.
I will take the information I have learned in this class and continue to work on it. I do love playing video games and if I can slowly work on a personal project that would be a great plus. However, I want to go into cyber security, and I do not think this will help me with my career path at all. I will keep playing around with it as a hobby though.

---
## [leapofazzam123/awesome-osdev](https://github.com/leapofazzam123/awesome-osdev)@[4c3b2b6ad8...](https://github.com/leapofazzam123/awesome-osdev/commit/4c3b2b6ad8d71e5126facbab2e6132df43788223)
#### Friday 2021-12-17 06:53:21 by Leap of Azzam

fuck you github for adding an unnecessary padding on the bottom of columns that i cant remove

Signed-off-by: Leap of Azzam <leapofazzam@gmail.com>

---
## [oumajgad/BlackICE](https://github.com/oumajgad/BlackICE)@[4335aa65e7...](https://github.com/oumajgad/BlackICE/commit/4335aa65e76a0532cdc657c28668c9197a08683b)
#### Friday 2021-12-17 10:23:16 by oumajgad

increased max covert ops points
lowered scout covert op cost
added War Exhaustion effects (WIP) It take roughly 55 months to reach max without going with heavy war related laws and losing too many battles (also WIP)
increased surface warships practical gain
added OMG event that removes resources buildings from captured provinces because fuck you

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e61f542678...](https://github.com/mrakgr/The-Spiral-Language/commit/e61f5426787151326466aea318743ab17b0cc139)
#### Friday 2021-12-17 12:32:02 by Marko Grdinić

"10:20am. I am up. I wonder if I'll get replies to the TensTorrent query. At any rate, posting it there is the best idea ever as I'll be able to decisively get rid of them not knowing about the language scenario. If they don't want it then so be it. I'll be able to move forward knowing that this is the case, and not have to be concerned about not doing enough to get it noticed.

No, nothing yet. The sub is very inactive, so I'll have to wait for a while until somebody from the company sees it. I'll post it on Groq and Graphcore's pages as well. It should happen eventually. At some point the CEO or somebody higher up will log into their social media page and see my post.

10:30am. Let me chill for a bit and thne I will start. The extreme tension I've been feeling for the past few days has abbated. This is the correct strategy for seeking sponsors. Doing just this while I do my own things on the side is enough.

I was wrong to ever try applying at places. Applying to jobs should be done for the sake of actually getting a job.

11:10am. Let me start. Where was I yesterday?

https://youtu.be/al3vR6ySXfo?t=39
Nodes 4 Noobs | Lvl 6 | Displacement | Beginners Guide to Nodes

This looks really great.

11:25am. https://youtu.be/al3vR6ySXfo?t=356

Let me actually try this.

11:30am. Hmmm, how do I turn on displacement? I fact, I should not forget to do a subsurface mod first. ...But that is complicated.

11:35am. I figured out how to get it to work, but it seems it only works in Cycles. Still it looks quite nice there. I wonder why suddenly it is wanting to get 1024 samples whereas previously 32 was max. I don't think I changed any parameter by accident. Edit: I forgot that I upgrade to Blender 3 which has rendering performance improvements. This is probably related to that.

https://youtu.be/al3vR6ySXfo?t=405

Hmmm, there is a modifier for this.

12:15pm. https://youtu.be/oYtfY1ESMwU
Nodes 4 Noobs | Lvl 8 | Pointiness & Blend Modes | Beginners Guide to Nodes

I think this should be the last one. Let me check.

https://www.youtube.com/playlist?list=PLn3ukorJv4vtnU_TaZob7QD6Q8d9C9Ki7

Ah, there is also the mossy rocks exercise in the playlist.

I'll take a look at it after I am done with this one.

12:35pm. https://youtu.be/oYtfY1ESMwU?t=233

I have no idea what this is supposed to be doing. This is one of those cases where I really need the guy to explain it to me. Plenty of such cases in Blender. Blender is so complex that even the stuff that is easy is hidden away amongst piles of other options. A lot of stuff needs to go into my procedural memory to make all of this work.

12:40pm. Ohhh, ok I see it. For making this work it is best to edit the pos of the slider nodes manually. When I set it to .495/.505 I really see the crevices getting darker. Quite an interesting effect. I'll have to remember this trick for the future.

https://youtu.be/oYtfY1ESMwU?t=361

Oh, this is an interesting way of doing it. Yes, this is one way to get precision.

1:30pm. Let me have breakfast here. I got into it. Today's session was ideal. I learned a bunch.

My heart is finally at peace now. It is all because I could imagine a future where these chips get sold and have customers congregating on Reddit. That is the place I could advertize. If my current efforts fail, I could implement that backend, push tutorials and such. No prob.

Right now, these chips are still in early stages, so it does not matter that I start work immediately. But it does matter that I start advertizing Spiral immediately.

I'll finish this tutorial and then post on the Groq and Graphcore pages. Maybe I should look into SambaNova as well."

---
## [Rajdeepkaur96/Deep](https://github.com/Rajdeepkaur96/Deep)@[c9490adc89...](https://github.com/Rajdeepkaur96/Deep/commit/c9490adc89d8a9776406bc6afa60714504fd24da)
#### Friday 2021-12-17 13:47:17 by Rajdeepkaur96

Create TECHNOLOGY

TECHNOLOGY CHANGING THE FACE OF EDUCATION?
HomeTechnology changing the face of education?

 
Spread the love
By Rajdeep kaur

Technology changing the face of education: Technology cannot be terminated without the utilization of procedures, tools, machines, materials, and sources of power to make human life more comfortable throughout. it has aided in changing the face of education and developing the education system and productivity as well.


technology advancement
It encourages one’s abilities and permits one to use the immense material forces of creation.  Technological advancement is the driving force of commercial growth.  Consequently, the availability of technology defines the efficiency of stock and the acceleration of economic growth.

Technology is essential in our life
It has the main purpose of solving the query of humankind and making work more peaceful. We have been massively dependent on technology that we cannot do anything without it. Technology is used everywhere when we utilize mobile phones, drive a car, watch tv, electrical engines and use the computer, etc . with the maintenance of technology, we can bright not only the present but also the future.

Technology development in several areas
In the earlier years, the masses have made excellent advancements in technology. Present-day India has had a robust focus on technology and science that designates it as a core component for economic growth and cultural development. Development is progressing in the various fields i.e. product and service of information of technology, the building of electronics and transportation, etc.

Technology boosts in artificial intelligence, robotic process automation, edge computing, virtual reality, cybersecurity, blockchain, quantum computing, internet of things, 5g.

The technology department gives goods and services that are used in consumer and merchandising functions. Consumer commodities are mobiles, wearable technology, computers and home appliances. Business uses technology to handle their databases, preserve financial data, performances of business, and overall outcomes.

Technology transforming the appearance of teaching

technology transforming the appearance of teaching
Technology has converted an enormous part of society and day-to-day life. it is utilized to assist both teaching and learning technology in the classroom.  technology is a predominant mechanism that supports and moulds education. it has the capability to enhance connections between teachers and students.

It can put all the data into one position, promote learning motivation, it also intensifies learning efficiency because of visualization of the thought.  technology presents a satisfactory environment in which students discover and solve their own troubles. Students are also capable to cooperate with their own classroom through technology purposes.

we have multiple platforms on which we can communicate with friends, and teachers. those platforms are Google meet, Skype, Slack, zoom, and Bigbluebutton, etc. Zoom is one of the most prevalent conferencing platforms.

Technology has a positive and a negative influence.
No doubt, technology has enhanced a significant factor of daily life. but it has a positive impact and a negative consequence.

POSITIVE EFFECT
1 we can reach distant places within hours.

2 save time and money

3 enhancement of learning skills

4 development of social interaction

5 Problem-solving abilities

6 with the help of mobile technology,  we can easily reach our friends and relatives who are living far from us

7 enhancement of student engagement

8 through the internet, we are able to learn new things and online lectures

NEGATIVE EFFECT
1 Due to the evolution of technology workers face difficulties means it generates unemployment.

2 It is also created depressing social issues, health problems.

3 reduce slumber due to mobile devices.

4 less physical motions

5 feeling lonely

6 neck pain and bad posture.

7 kids play those games which are dangerous in their life.

8 somebody utilizes technology in the wrong way which destroys their life. an eg. terrorist, thieves.

CONCLUSION
We can observe nowadays, without technology we are worthless because everyone wants to use technology to facilitate work. with technology, teachers have discovered new techniques to interact with their pupils. so we can say technology changing the face of education. it improves interaction, learning system, resourcing sharing by innovative audio-video characteristics. it helps administration, businesses, and people increase their efficiency and effectiveness.

---
## [Jprimero15/lolz_kernel_redmi8](https://github.com/Jprimero15/lolz_kernel_redmi8)@[e789b90366...](https://github.com/Jprimero15/lolz_kernel_redmi8/commit/e789b90366db4914ea1ed8688cf6f8d35fab50b1)
#### Friday 2021-12-17 14:49:55 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: sweetyicecare <gabrielseedev@outlook.com>
Signed-off-by: Jprimero15 <jprimero155@gmail.com>

Conflicts:
	mm/swapfile.c

---
## [turex/siberia_hi6250_kernel](https://github.com/turex/siberia_hi6250_kernel)@[068580bddb...](https://github.com/turex/siberia_hi6250_kernel/commit/068580bddb5b40c1ff46b6c8674617d487f17a69)
#### Friday 2021-12-17 15:35:00 by Christian Brauner

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
        kernel/signal.c - struct kernel_siginfo does not exist in 4.9
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.9 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. exclude kill() changes to avoid struct kernel_siginfo usage
 4. exclude copy_siginfo_from_user_any() to avoid struct kernel_siginfo usage
 5. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 6. replaced COND_SYSCALL with cond_syscall
 7. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 8. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I00f1c618b2e9dbafae4d4113ad4d8a1a44b6957c
Signed-off-by: Suren Baghdasaryan <surenb@google.com>

---
## [nvllsvm/dotfiles](https://github.com/nvllsvm/dotfiles)@[567f8daea2...](https://github.com/nvllsvm/dotfiles/commit/567f8daea2cac98d909fa479857edbd2b6252b50)
#### Friday 2021-12-17 18:07:42 by Andrew Rabert

Because Firefox 95 is completely fucked when opening Links from Slack
Get your head out of your fucking ass, Mozilla. Fix your shit instead of
focusing on features like "Pocket" or whatever-the-fuck-else anus-projectile vomit some "PMP, MBA" came up with.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[c513ab93c1...](https://github.com/mrakgr/The-Spiral-Language/commit/c513ab93c19cdf1ace82411e67592a23d5e0ca43)
#### Friday 2021-12-17 18:45:20 by Marko Grdinić

"3:45pm. Let me just finish reading the thread and I will resume. I am thinking about how the third run should go.

My heart is a lot more at ease now. I feel that by figuring out the social media idea, I've done my duty with regard to Spiral. Whether people accept or refuse it from here on out is not my responsibility. My responsibility is only that I get to the point where they can make that choice. I'll get the chips sooner or later.

So what I've been thinking is how I would do ML research on those AI chips. I am thinking how the yearly review will go. Just what kind of direction will I take it in?

I've realized one single fact. If I had an oracle and could ask it what are the optimal learning algorithms for the poker family of games within reasonable hardware constraints are, the answer I would get would be extremely enlightening. It would definitley not be backprop, but something that resolves all the problems with it, and uses the existing primitives in extremely clever ways.

No doubt such algorithms would work on things beyond poker.

It should be possible to use them to improve the process of learning the learning algos as well. That is how the Singularity should happen. Human genius will not reach the conclussion, but human perseverance instead.

This path would resolve the issue that has been plaguing me - if I cannot move to the next level now, just why do I think I'll be able to make algorithmic improvements on my own mind in the post-Singularity era.

Obviously, because I'll be playing a different game then. But since that era is near, why not play it now?

4:05pm. Let me resume, I could have started an hour earlier, but instead I've let myself become distracted. Still, this is how I am going to overcome my depression. Build a new vision of the future and commit to it. The way to win is to come up with an appropriate plan and commit to it. For the past months, all I've been doing is coming up with things that might benefit me, but would require me doing things that I do not want to do.

There is no way that the paths taken by NPCs will lead me out of this simulation. Life will always test whether you can stay true to your desire.

I should have known that I would need massive parallelism to really win, and simply did my cultivation with that in mind. That way I would not have gotten knocked out when current day RL methods turned out to be useless.

At some point I will get back to programming, but why not give it a year for my wounds to heal like in 2019? I'll have fun learning new things and then get back for the final push.

https://youtu.be/9f-B8xk0peA?list=PLn3ukorJv4vtnU_TaZob7QD6Q8d9C9Ki7
Mossy Rocks - Beginner Node Exercises in Blender

Let me take a look at this.

Hmmmm, this is pretty good. How did he create the muddy ground? There is even water.

I do not know how to do that at my present level and this is something I'd like to learn.

4:35pm. https://youtu.be/9f-B8xk0peA?list=PLn3ukorJv4vtnU_TaZob7QD6Q8d9C9Ki7&t=248

Should I give these texture a try? Let me get them.

Moss texture https://www.textures.com/download/PBR0481/138373
Rock texture https://www.textures.com/download/3DScans0151/132400

Ah, right. So far he did not cover ambient occlussion. I still have no idea what the point of that is.

4:40pm. https://www.textures.com/

This site seems pretty nice. Let me get the relevant stuff that I need.

///

Hi @mrakgr,
these are some interesting commits. Like the idea and also your honesty.

I'm currently crawling through all public commit messages using gharchive.org and select messages that contain a couple of words that are not directly related to programming. Currently my script finds about 5 to 20 messages per day (among millions) and your's are always in there ;)

I'm writing because i will actually commit those interesting messages per day to another repo, collecting them in markdown files. It will probably not get popular and i don't intention it to be but since you would be one of the prominent contributors i rather ask for your approval. Maybe your messages are not really intended to be found by people, who knows? I'm fine with excluding your repo/user if you say so.

Anyways, thanks a lot for sharing your thoughts!

///

Found this in my inbox.

https://github.com/mrakgr/The-Spiral-Language/commit/e61f5426787151326466aea318743ab17b0cc139

It is this commit. Well, my commits are hardly hidden. I have no reason to refuse this, but let me leave the reply for after the day is done. Right now I want to focus on the task at hand and do not want to get distracted.

4:45pm. As I was saying the site is nice. Let me get the height image as well, as I like the displacement effect.

Downloading this is really easy. I was worried since it does not come as a pack, but it seems the intention behind that is credit allocation. I have about 7 free credits left. I wonder if those get refilled.

https://www.textures.com/pricing

Wow, the prices are quite expensive. This could stack up.

4:55pm. I've been admiring the highlights at the bottom. Nevermind this for now. Let me bring in the textures.

5:05pm. Agghhhh, how do I turn on displacement?

5:10pm. Agggghhhhhh...

The displacement is in the material settings. But I forgot that I can't use this on a flat plane! Let me subdivide it.

Yeah, now it works. Sheesh.

Good. Hopefully, I'll remember how to do it right in the future. Now what do I do with this?

5:30pm. Damn it, is it possible to swap links without having to do it manually. Right now the nodes are getting hairy and it is a drag to do it visually instead of programatically.

https://docs.blender.org/manual/en/latest/addons/node/node_wrangler.html#swap-links

Maybe this? Yeah, Alt + S was it. Great.

Let me get back to the video. It does not look that great, certainly nowhere near as the impressive scene at the start.

5:45pm. I did not realize it at first, but it is not a good idea to mix displacement maps.

I wish these rocks had more detail to them.

5:45pm. Uhhh, I did not think they would literally have 5-10 vertices each.

Once you apply all the modifiers it starts looking better.

5:50pm. No, the displacement on the rock itself does not look that great. I figured out how to increase the detail, but that is not enough. Nevermind, I spent too much time on this. Let me get back to the video.

5:55pm. Let me go have lunch.

6:25pm. Let me resume. Where was I?

https://youtu.be/9f-B8xk0peA?list=PLn3ukorJv4vtnU_TaZob7QD6Q8d9C9Ki7&t=410

It has 3 minutes left. Ok, let me watch it. At this point I'd prefer to stop for the day.

Ah, yeah, let me put in the HDRI.

6:40pm. It does not seem he will be covering the muddy ground.

6:45pm. https://www.detailingwiki.org/correction/what-is-a-clear-coat/

Am Googling this. So I get what a clearcoat is now. Ok, good.

I had no idea that paint was originally used to prevent the metal underneath from oxydizing.

6:50pm. I am just chilling here.

Hmmmm...I think that's it for the day. I should reply to that guy from earlier.

I should make the posts on the Groq and Graphcore subs, but I do not feel like it right now. I'll leave that for tomorrow when I am fresh.

What should I do tomorrow? That texturing tutorial for the knife caught my interest. So did that brick wall tutorial while I was searching for shading tuts.

At this time, I do not think I am done with the shading tutorials just yet. I feel like I have the basics down thanks to Grant, but I need to learn more before I get back int othe action. That big tutorial which goes over all the shader nodes I'll want to watch before going back to do my own thing.

6:55pm. Sigh, I need to get into the habit of going to bed earlier. Because of gaming I feel like I never have enough hours in the day to think. I alway end up going to bed past 1am. I want to stop earlier, but I get the urge to play more until I am at my limits. Well, I'll get tired of it at some point. I should feel blessed that I have games like Lobotomy Corp to play now. I'll try to halt at 12am today, but I won't hold myself to it.

The urge to go to bed on time should come to me naturally once I bolster my will.

I need to make it a two pronged plan. I'll think about where on social media do these companies hang out and try to grab their attention there.

It really is so simple, it is like the fog has lifted from my mind. Of course that if one of these chips takes off, it is going to have people talking how to program them on the Internet somewhere. So I do not have to worry too much and just wait for that moment.

Of course, it would be even better to get access to them now, but that is not an absolute requirement. If absolutely everything fails - Spiral, Heaven's Key, art cultivation, then I'll just have to get a job, but it would take both extreme unluck and incompetence for that to happen. So I won't need to think about it.

My house is not going to burn down for some stupid reason, and neither is my father going to die in an accident. I am not going to develop a medical condition that requires expensive medical treatment.

And not everybody is going to be a dumb script kiddie like the ML sub pros.

I should just do as I desire and let the dice fall where they may.

7:10pm. Now let me reply to that guy.

7:35pm. Now let me look up genetic programming for a bit.

https://www.youtube.com/results?search_query=genetic+programming

There is a bunch of stuff here. I am not going to watch anything right now. I really should just get the book by Koza when I am ready.

Let me chill. I am done for the day."

---
## [defgsus/good-github](https://github.com/defgsus/good-github)@[4bf13694d6...](https://github.com/defgsus/good-github/commit/4bf13694d6649c6f3fbecb1b48297ee68ae7d785)
#### Friday 2021-12-17 22:40:32 by bergi

Okay. *Servi* is working on years 2020 and 2021 and in the spirit
of this project i'll put all the thoughts into a commit message
instead of the repo files. The README should really just show the newest
commit messages and not the project description.

The repo description says *collector*, not archive, because really
github itself is the archive and alive species, gharchive.org is
the means to access much of the data without request throttling
and this repo is just one little boil down.

Yes, it serves as another exponential growth factor for github.org.
Commit messages with character, fantasy or strong words will eventually
be stored twice by github.

In the first draft, i tried bag-of-word statistics, text entropy and some
classifiers from [huggingface](https://huggingface.co), nothing of it
worked well. Finally i went back to the old count of a handful of carefully
chosen words. Of course it's not perfect, either. It catches a few
interesting messages but certainly just yet a fraction. E.g. this message
would not get included by the words used so far. Not that this is
a particularly interesting text, but this repository would certainly
interest me ;)

Originally i was breaking my brain how to do something like **github untrending**
using just the archived github api events. That would point you to
cool trendy projects that do not have stars yet, e.g. which aren't yet trendy.
I think that's quite difficult, having nothing but commit frequency, authorship
and message content.

Finally. Why republish those messages? Partly, because it's possible, i admit.
And it's just nice to not have to parse those events locally. Everyone around
the laptop, including me, is annoyed by the fan.

Next steps: bread the
[word list](https://github.com/defgsus/good-github/blob/master/src/words.py)
and recompile a couple of github years. Then maybe start *auto-tagging*
or something to better navigate this repo..

---

