## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-14](docs/good-messages/2022/2022-06-14.md)


1,756,067 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,756,067 were push events containing 2,762,245 commit messages that amount to 203,725,286 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [cheekybrdy/goonstation](https://github.com/cheekybrdy/goonstation)@[7a51b963ef...](https://github.com/cheekybrdy/goonstation/commit/7a51b963efea995ff059c08ebf5e885dfd3b0f0f)
#### Tuesday 2022-06-14 02:10:41 by cheekybrdy

Medbay Crunching

Ate the central blank space and medbay, started fixing the errors stated by @ZeWaka. I made all suggestions over git and discord into a checklist as follows below.
☑=done
☐=todo
☒=was intentional & needs discussion design wise/in progress
Spread out crew area☐

More Space needs to be used?  ☑

MOVE THE SYNDICATE OUTPOST (/) ☑
use the big medbay lobby properly ☑

split ghosties?☒

Major issues
-I'm not going to complain about the many pipes going through walls since most maps do that in places (except for the disposal pipe in west medbay that one's just nasty), but several areas are set up wrong (particularly around sec but not exclusively). Pipes can cross over one another fine but you can't put multiple in the same direction on the same tile, the system isn't advanced enough to handle that.☐
-Although I appreciate criming toys, the syndie destruction, purge and rewind systems in maint are well into overkill for maint goodies.☐
-The mail network as is won't function as most things end up in the mail room. The pipes need to loop back at some point. (see cog1 for a simple setup, and cog2 for one that has several loops and a central router)☐
-/area/station/chapel is an abstract type for some reason, but you can just make the whole chapel the sanctuary subtype☑
-The listening post is kinda fucked in general: it's not meant to be on station, the wall between the foyer and the cairngorm teleporter is simulated, and I'm pretty sure the buddies in there are just hostile to everybody. Also the strelka isn't appropriate.
-The 3 N2O cans in the patho sector are, but it might be fine if you replace them with a static N2O tank (probably enough to feed all the rooms too). The N2O pressure tank in engineering seems odd too, but I personally approve. :P☒
-Quartermasters don't have engineering access, so they can't open one of the doors to get in their office. When they get there, they're missing a bunch of manufacturers and a way to easily get crates out front.☒
-Your engine is hotwired by default. To map SMESes properly, you need to lead the raw engine output into /obj/machinery/power/terminals that feed into the SMESes. Then you can have a wire from under the SMES to the station grid. If you need an example cog1 is probably easiest, because the raw engine wire is brown and easier to follow because of that. When you fix this, also look at the spare SMES in security.☐
-Speaking of that room with the SMES, dedicated execution chambers really aren't a good vibe.☒
-I'm not sure if the mining teleporter functions on space maps. The mineral magnet is also rectangular and I think it needs to be square to function.☐
-Jazz lounge looking straight onto a major hallway limits its capacity for crime.☐
-The inputs to the huge toxins burn chambers and the mixer need pumps/valves.☐
-All of medbay has just one nanomed to supply them.
-6 tasers and 4 eguns in the armoury is fairly spicy. Might get antags to pay attention to the dang place though. :P (Probably ask others for second opinions on that one, I'm not a sec/combat balance person)☐
-I appreciate this is probably because the map is a draft, but there's so few windows into places.☐
Minor issues/concerns
-Red crosses in medbay are (to my knowledge) discouraged, so the one in medbay's floor should maybe be changed.☑
-If the free-standing bit of medbay is meant to be another pathology lab, it's missing an autoclave☑
-I don't remember patho that well but 8 centrifuges seems way superfluous☐
-Armory auth computer isn't an appropriate match for the☐
-Also I don't think it can do any harm, but why the nuclear centrifuge in there?☐
-I appreciate you've got the cleanerbot in robotics, but usually there's a drain near the operating tables too☑
-The robotics database is unused and I think doesn't do anything☑
-You don't need to add Faith to the chaplain's locker, they spawn with it.☐
-The long couch (whose comical length I love) doesn't have proper ends☑
-Some of the chapel pews are missing the top bit☑
-Library doesn't need the torpedo guide if the map doesn't have torpedos☐
-Space tile under the NAS-T in the listening post foyer, and another under a conveyor in the ghostdrone factory☑
-A few misplaced firedoors around the bridge
-The bridge windows need electrification☑
-I think data terminals need a wire with a node at the center to work, and if I'm correct in that the mainframe isn't☐
-Missing turret control for the computer core☑
-Missing corner in that nasty disposal pipe in west medbay☑
-Missing wire for the APC to that main engineering/atmospherics room☑
-What are those carousel units in engineering going to power?☑
-Missing wall in the telesci pad room☐
-Missing mug rack in the medbay break room (critical, I know), same with sec.☑
-The shower room in the medbay/bar cluster is only accessible via maint?☐
-EVA missing tank dispenser and RCD crate, luminol grenade is kinda weird to see there?☑
-Missing bit of pipe under a chute in botany☑
-Sauna pipe junction is probably non-functional, but there's dedicated junctions instead. (I think you have to search for manifold)☐
-Missing wire corner near in sauna/barber maint☐
-I haven't heard of the prototype Nano-fabricator (the blue tinted one), but it seems like it has no recipes.☐
-Prototype RCD in tool storage is, I think, a deathtrap from an azone.☑
-A few of the main station sections are done in plating instead of floortiles☐
-Medbay hand trader is missing the supply marker☑
-Missing cap's spare☑
-Misplaced bedsheet in bridge wall.☑
-Bar doesn't have a reagent heater, bartender is kinda just missing the stuff normally in their office too.☑
-Robotics is missing the borg parts crate I think☑
-Chemistry is missing a bunch of glasswear and stuff, also there's no source of welding fuel in all of sci.
-Clock 188 in the HoS room?☑

---
## [xdroid-devices/xd_kernel_realme_mt6785](https://github.com/xdroid-devices/xd_kernel_realme_mt6785)@[469a006517...](https://github.com/xdroid-devices/xd_kernel_realme_mt6785/commit/469a006517ad46a1bc141bf9e7356f97edeb8f0b)
#### Tuesday 2022-06-14 02:21:25 by Wang Han

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
Signed-off-by: officialputuid <officialputuid@hack.id>

---
## [soitun/canvas-lms](https://github.com/soitun/canvas-lms)@[a403ea1af0...](https://github.com/soitun/canvas-lms/commit/a403ea1af0c5ccc59b803ba65962471f0c1074d5)
#### Tuesday 2022-06-14 02:26:52 by Evan Battaglia

Fix inconsistent plagiarism report permissions

Previously, due to permissions pecularities, if the plagiarism report
visibility was set to "never", teachers would not be able to view
plagiarism reports after their enrollments were "concluded" (due to them
not having the "manage_grades" permission then). This was inconsistent,
however, since the score would still show on speedgrader (but not the
submission page) but clicking it would error when trying to view the
report. Also, preventing them from seeing reports is especially
nonsensical since the teachers are usually the ones to set up the
assignment plagiarism report visibility which prevented them from
viewing them.

This commit makes the permissions for on the submissions page, and
actually viewing the report, nearly the same as that for using
speedgrader, although is difficult to get perfect. The permissions for
speedgrader are:
  - to use speed grader at all:
    manage_grades OR view_all_grades
  - additionally, the turnitin score is only shown if
    manage_grades OR (@context.concluded? && can_do(@context, @current_user, :read_as_admin))
    (see app/views/gradebooks/speed_grader.html.erb:235)

This commit brings the permissions for showing the score on the
submissions page, or viewing the report, to:
  - manage_grades OR view_all_grades

This means it's still possible for some cases for the score / report to
be visible from the submission page, but not from speed grader -- if:
  - the user can view_all_grades
  - the user cannot manage_grades (in the ticket this was just because
    the course/teacher enrollment was concluded)
  - the course is not concluded OR the user cannot read_as_admin

This seems like it should be very rare and I'm not sure it's worth
trying to tweak the permissions in speedgrader (which honestly I don't
understand well -- there may be some other reason for limiting what is
shown in speedgrader) or making the conditions for viewing the report as
complex as those in speedgrader. And, the risk is only that the score
will not show in speedgrader but will in the submission, not that there
will be any broken link.

fixes INTEROP-7312
flag=none

Test plan:
- setup to repro the original problem. Here is how I did this:
  - set up plagiarism platform in an assignment with report visibility
    "never" (students can never view reports). I used the
    lti_originality_report_example tool.
  - as a student, submit to the assignment
  - create an originality score/report for the submission. I used tok
    (Set up to get a token with the lti_2_token endpoint):
      tok web.canvas-lms2.docker/api/lti/assignments/469/submissions/1428/originality_report \
        originality_report[originality_score]=33 \
        originality_report[workflow_state]=scored \
        originality_report[originality_report_url]=http://example.com/123
  - make the course concluded
      course.update workflow_state: :completed
    that wil make all the enrollments also "completed".
- Make sure the original problem can now be repro'd: In this scenario
  (with the code before this commit), when viewed as a teacher, the
  submission page (e.g. courses/123/assignments/456/submissions/789,
  where 789 is the user id) should not show a plagiarism score;
  speedgrader will show a score, but when clicked, no report will be
  viewable.
  NOTE: it seems like I had to run "AdheresToPolicy::Cache.clear" and/or
  "Rails.cache.clear" for permissions to get updated when switching code
  for some reason.
- with this code checked out, make sure that:
  - the score shows up on speedgrader
  - clicking it works to show the report
  - the score shows up on the submission page and clicking it works to
    show the report
  - as a student, the score should NOT show up on the submission page

Change-Id: I6d527884205bb48de6dda98f9eac96939834f2f5
Reviewed-on: https://gerrit.instructure.com/c/canvas-lms/+/293531
Tested-by: Service Cloud Jenkins <svc.cloudjenkins@instructure.com>
Reviewed-by: Tucker Mcknight <tmcknight@instructure.com>
QA-Review: Xander Moffatt <xmoffatt@instructure.com>
Product-Review: Alexis Nast <alexis.nast@instructure.com>

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Tuesday 2022-06-14 02:43:18 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [Zharay/BitburnerBotnet](https://github.com/Zharay/BitburnerBotnet)@[832ec1d0e4...](https://github.com/Zharay/BitburnerBotnet/commit/832ec1d0e407d111852fe72c52729c34734c78b4)
#### Tuesday 2022-06-14 03:38:49 by Danny

Heavy stock-bot modifications
- stock-bot - Is now short capable (option to enable)
- stock-bot - Completely re-organized and redid its logic and naming conventions. Now it all makes sense.
- stock-bot - Log now posts a history of transactions (up to last 50 by default)
- stock-bot - Still being worked on to figure out how to better handle shorts (forecasts suck)
- stock-bot-v2 - Has an option to disable shorts (for those without access to BN8 or BN8.2)
- stock-bot and stock-bot-v2 - Now reports to the coordinator any stocks we own for market manipulation!
- coordinator - Now maintains a list of all possible stock capable servers (breaking my personal rule against "cheating")
- coordinator - Updated target status ports to include stock information (long/short)
- hack-daemon - Now uses the new stock information from the coordinator in order to hack to $0 (short) or grow to max and not hack at all (long)
- liquidate - Now toggles selling of stocks on/off

---
## [mudasirahanger/opencart](https://github.com/mudasirahanger/opencart)@[89c304ae61...](https://github.com/mudasirahanger/opencart/commit/89c304ae61fb683b2ca8ff7dcf5ceabfc4f5a0eb)
#### Tuesday 2022-06-14 04:05:55 by Anton

OC4 return created module_id

IMHO every single model function, creating a row in DB, must return this row id after executed.

I can check `$module_id = $this->db->getLastId();` in my code on clean opencart installation.
But what if this model function calls any `after` events which also insert rows into DB?

This is not a developer friendly software architecture when you need to create hacks, hooks, workarounds and other voodoo magic to get a single value for page redirect.

BUG:
By the way on creating, for example a banner module, on save you are not redirected to created module page. 
So every click on Save button just creates a duplicate of a module.

---
## [Alex-Lee-Myers/Capture-Portfolio-JS](https://github.com/Alex-Lee-Myers/Capture-Portfolio-JS)@[26b21f7436...](https://github.com/Alex-Lee-Myers/Capture-Portfolio-JS/commit/26b21f74365b90629a753ffb921d212a09889be8)
#### Tuesday 2022-06-14 04:27:21 by Alex-Lee-Myers

was able to get page transitions to work through both exported variables from Animation.jsx as well as integrate React 18 with new Framer, while keeping in mind React-Router-Dom V6 new Routes/Routes/Links/etc. Took some troubleshooting but was able to accomplish it by end of night after playing some DnD with friends till late. May try to get a few more animations done since they're fun, but also maybe I should sleep since I work in 7 hours. I just wish I did this every day at work!

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[95ffcd4e19...](https://github.com/jlsnow301/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Tuesday 2022-06-14 04:40:39 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [maxproske/next.js](https://github.com/maxproske/next.js)@[91146b23a2...](https://github.com/maxproske/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Tuesday 2022-06-14 06:06:16 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [DWaffles/DSharpPlus](https://github.com/DWaffles/DSharpPlus)@[8380b5b2de...](https://github.com/DWaffles/DSharpPlus/commit/8380b5b2deb9f2243c87e3277a34902ec08bb716)
#### Tuesday 2022-06-14 06:57:54 by InFTord

[ci-skip] Fix docs typos in DiscordRestClient (#1317)

* Update DiscordRestClient.cs

* insanity

edited all of this with github site editor
madness
editing 2k lines of code is kinda pain with github site editor

* im idiot

* fixing...

* uh oh

* i love fixing docs

* fixing inconsistent ID stuff..

---
## [JOKR-Services/gqlgen](https://github.com/JOKR-Services/gqlgen)@[43b56cbaf3...](https://github.com/JOKR-Services/gqlgen/commit/43b56cbaf3f1de1d1ad379055ab1de157592cf38)
#### Tuesday 2022-06-14 07:43:46 by Ben Kraft

Forward `go mod tidy` stdout/stderr

This is a command that can fail (in my case I think for stupid reasons
in a hell of my own construction, but nonetheless).  Right now we just
get
```
$ go run github.com/Khan/webapp/dev/cmd/gqlgen
tidy failed: go mod tidy failed: exit status 1
exit status 3
```
which is not the most informative.  Now, instead, we'll forward its
output to our own stdout/stderr rather than devnull.

---
## [V3dantSh4rma/Vibey-discord-bot](https://github.com/V3dantSh4rma/Vibey-discord-bot)@[d49f2d414e...](https://github.com/V3dantSh4rma/Vibey-discord-bot/commit/d49f2d414ef7767c063b8c90249bd687e01fc32a)
#### Tuesday 2022-06-14 08:17:46 by VedantSharma7

- Added a Website to this bot. Which means, when you'll run the "npm start", it will make an attempt to bring the bot online and start the express server.

- Also, Reformatted the code, Came out with a better music queue logic which is not implemented in this code yet. It's becoming a pain in the ass lately. But, here we go. Do expect bugs/errors in this project since it's still in beta.

---
## [magdalenamae/plantr](https://github.com/magdalenamae/plantr)@[246b1fd141...](https://github.com/magdalenamae/plantr/commit/246b1fd1412b1c8f1db5cd5131d44ab215e0160e)
#### Tuesday 2022-06-14 08:46:32 by magdalena

Sorry for the last commit, that was a mistake.
Let me know what you think of the sign up frunction and ill incorperate it into the rest of the code later tonight.

---
## [zhjwpku/postgres](https://github.com/zhjwpku/postgres)@[c40ba5f318...](https://github.com/zhjwpku/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Tuesday 2022-06-14 09:16:59 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [cheekybrdy/goonstation](https://github.com/cheekybrdy/goonstation)@[ddfe4f8c76...](https://github.com/cheekybrdy/goonstation/commit/ddfe4f8c76743ca3cdfbdbf902911a7897d7935c)
#### Tuesday 2022-06-14 09:37:18 by cheekybrdy

Pandemic Ward + More Fixes

Corrected more things and added Pandemic Ward area.
Current Todo:
Spread out crew area☒ (thought split maint equaling main hallways meant that antags would be disadvantaged especially vamps so I tried to make SE and SW wings lower traffic. Was this antag issue a misdiagnosis?
Squishy Silicon rooms☑
More Space needs to be used? ☑

MOVE THE SYNDICATE OUTPOST (/) ☑
use the big medbay lobby properly

split ghosties?☒

Major issues
-I'm not going to complain about the many pipes going through walls since most maps do that in places (except for the disposal pipe in west medbay that one's just nasty), but several areas are set up wrong (particularly around sec but not exclusively). Pipes can cross over one another fine but you can't put multiple in the same direction on the same tile, the system isn't advanced enough to handle that.
-Although I appreciate criming toys, the syndie destruction, purge and rewind systems in maint are well into overkill for maint goodies.☑
-The mail network as is won't function as most things end up in the mail room. The pipes need to loop back at some point. (see cog1 for a simple setup, and cog2 for one that has several loops and a central router)
-/area/station/chapel is an abstract type for some reason, but you can just make the whole chapel the sanctuary subtype☑
-The listening post is kinda fucked in general: it's not meant to be on station, the wall between the foyer and the cairngorm teleporter is simulated, and I'm pretty sure the buddies in there are just hostile to everybody. Also the strelka isn't appropriate.☒
-The 3 N2O cans in the patho sector are, but it might be fine if you replace them with a static N2O tank (probably enough to feed all the rooms too). The N2O pressure tank in engineering seems odd too, but I personally approve. :P☒
-Quartermasters don't have engineering access, so they can't open one of the doors to get in their office. When they get there, they're missing a bunch of manufacturers and a way to easily get crates out front.☒ (the out the front bit, rest makes since
-Your engine is hotwired by default. To map SMESes properly, you need to lead the raw engine output into /obj/machinery/power/terminals that feed into the SMESes. Then you can have a wire from under the SMES to the station grid. If you need an example cog1 is probably easiest, because the raw engine wire is brown and easier to follow because of that. When you fix this, also look at the spare SMES in security.☐
-Speaking of that room with the SMES, dedicated execution chambers really aren't a good vibe.☒
-I'm not sure if the mining teleporter functions on space maps. The mineral magnet is also rectangular and I think it needs to be square to function.☒ (magnet changes done).
-Jazz lounge looking straight onto a major hallway limits its capacity for crime.☐
-The inputs to the huge toxins burn chambers and the mixer need pumps/valves.☑
-All of medbay has just one nanomed to supply them.☑
-6 tasers and 4 eguns in the armoury is fairly spicy. Might get antags to pay attention to the dang place though. :P (Probably ask others for second opinions on that one, I'm not a sec/combat balance person)☐
-I appreciate this is probably because the map is a draft, but there's so few windows into places.☐
Minor issues/concerns
-Red crosses in medbay are (to my knowledge) discouraged, so the one in medbay's floor should maybe be changed.☑
-If the free-standing bit of medbay is meant to be another pathology lab, it's missing an autoclave☑
-I don't remember patho that well but 8 centrifuges seems way superfluous☐
-Armory auth computer isn't an appropriate match for the ☐ (placeholder for what likley will be blue retextured armoury auth)
-Also I don't think it can do any harm, but why the nuclear centrifuge in there?☐
-I appreciate you've got the cleanerbot in robotics, but usually there's a drain near the operating tables too☑
-The robotics database is unused and I think doesn't do anything☑
-You don't need to add Faith to the chaplain's locker, they spawn with it.☒
-The long couch (whose comical length I love) doesn't have proper ends☑
-Some of the chapel pews are missing the top bit☑
-Library doesn't need the torpedo guide if the map doesn't have torpedos☑ (intended as a late manta reference)
-Space tile under the NAS-T in the listening post foyer, and another under a conveyor in the ghostdrone factory☑
-A few misplaced firedoors around the bridge☑
-The bridge windows need electrification☑
-I think data terminals need a wire with a node at the center to work, and if I'm correct in that the mainframe isn't☑
-Missing turret control for the computer core☑
-Missing corner in that nasty disposal pipe in west medbay☑
-Missing wire for the APC to that main engineering/atmospherics room☑
-What are those carousel units in engineering going to power?☑
-Missing wall in the telesci pad room☑
-Missing mug rack in the medbay break room (critical, I know), same with sec.☑
-The shower room in the medbay/bar cluster is only accessible via maint?☒ (less accessibility for crimeing)
-EVA missing tank dispenser and RCD crate, luminol grenade is kinda weird to see there?☑
-Missing bit of pipe under a chute in botany☑
-Sauna pipe junction is probably non-functional, but there's dedicated junctions instead. (I think you have to search for manifold)☑
-Missing wire corner near in sauna/barber maint☑
-I haven't heard of the prototype Nano-fabricator (the blue tinted one), but it seems like it has no recipes.☐
-Prototype RCD in tool storage is, I think, a deathtrap from an azone.☑
-A few of the main station sections are done in plating instead of floortiles☐
-Medbay hand trader is missing the supply marker☑
-Missing cap's spare☑
-Misplaced bedsheet in bridge wall.☑
-Bar doesn't have a reagent heater, bartender is kinda just missing the stuff normally in their office too.☑
-Robotics is missing the borg parts crate I think☑
-Chemistry is missing a bunch of glasswear and stuff, also there's no source of welding fuel in all of sci.☑
-Clock 188 in the HoS room?☒

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7776c3198e...](https://github.com/mrakgr/The-Spiral-Language/commit/7776c3198e2e9de2c77f0d4946941364bfdedaa5)
#### Tuesday 2022-06-14 10:39:02 by Marko Grdinić

"10:35am. I am up. Let me chill a bit. Last night my brain finally started working again.

https://forums.odforce.net/topic/50964-how-are-variations-in-labs-building-generator-utility-supposed-to-be-used/

I asked here, but did not get an answer. Yesterday I checked out the point cloud outputs and it is good. The points have orientation and scale in them. So even if I can't pass in the geo variants directly, I can still use the base as a template for regular scattering. It is no trouble.

10:40am. Yesterday I was just overwhelmed, but today I am ready to build up the pieces one by one. I will manage it somehow.

https://www.lightnovelpub.com/novel/the-legendary-mechanic-novel-10062255/245-chapter-254

Let me sate my addiction for a bit and then I will get started. My first priority will be to finish the city building tutorials and then move on from that.

11:10am. https://www.sidefx.com/tutorials/city-building-with-osm-data/

That was fun. Let me start.

I am going to watch part 2 again and then watch 3 and 4. Then I'll also watch the other vid as well.

Oh, it is possible to disable the top and bottom ledges.

Yeah, it is coming to me now. I seem to be actually capable of paying attention today.

11:20am. I find it strange how the two ledges are split into so many faces, unlike the walls.

> So we will using this cloud point for our instancing. I guess I should be using those if I want to scatter. I could export it to something like Clarisse and make it work there.

11:40am. It is going smoothly into my brain now. Yesterday this video completely perplexed me, but now I can grasp it. It seems Unreal itself has some ability to do instancing. I'll have to tackle one of the engines, Unity or Unreal at some point, but not now. Since I an F# fan, I'll very probably go with Unity.

11:45am. Focus me, stop reading /a/, go to the next video.

Hmmmm, Houdini has a Road Tool SOP.

11:50am. What was polyframe used again? I'll figure it out when I get to it. Once I finish watching the tutorials I will actually try following them.

12:05pm. Done with part 3. It is time for part 4.

12:10pm. It is just a hunch, but I think that Unreal is capable of handling more geometry than Blender.

He will use the peak node to move points along normals. This is a great idea. I was wondering how he would move the trees inside.

12:15pm. Now he is randomly deleting points.

Hmmm, ah right. I usually just randomly distriubte them along the curve or a surface, so I never had a need to do that. The way he is doing it now will ensure that they are evenly sampled. I'll keep the technique in mind.

12:15pm. Hmmm, rather than do it like this, he would have been better off offsetting the curve first, the sampling the points and then deleting them. The reason why is because the trees can get close together at the intersections. I wonder if there is a way of deleting points that are too close to each other?

Another option is to just sample the curve and make sure that the points are relaxed enough.

Actually, that reminds me, wasn't there a relax node in there somewhere?

12:20pm. The next are trash bins. Yeah, I am wondering how he intends to place them close to the buildings. I do have an idea, but it is not good.

12:30pm. https://www.sidefx.com/tutorials/assembling-your-city-part-1/
https://www.sidefx.com/tutorials/complex-roads/

I want to watch these.

12:35pm. Mhhh, since the first vid is 30m, let me stop so I can have breakfast here. I feel like watching these videos. I do not feel a sense of perplexity like before. I should be able to absorb all of this today."

---
## [Qowevisa/dwm](https://github.com/Qowevisa/dwm)@[67d76bdc68...](https://github.com/Qowevisa/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Tuesday 2022-06-14 10:52:45 by Chris Down

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
## [muhdsalm/roburobu](https://github.com/muhdsalm/roburobu)@[f60aea1e05...](https://github.com/muhdsalm/roburobu/commit/f60aea1e05252b03d67bcfa5b7db4a3e9d770cf1)
#### Tuesday 2022-06-14 11:42:28 by ali

Fixed the problems... mostly

The game speeds up, robu robu is textured, heck, even the animations
plays!

The window still closes when you crash because, hey, you need something
to look forward to.

Anything else?

Oh yeah, switched over to sublime text, rust-analyzer works after
following the instructions, just 10 seconds! Beats the two hours i spent
trying to figure it out!

Next time, read the official instructions.

No change on the project structure, just wanted to throw that out.

Also, resized the robu robu image to be more friendly with my game.
Removed the gaps, and made it a lot bigger.

All in 10 minutes' work, i guess.

---
## [Gullwing-door/restoration-mod](https://github.com/Gullwing-door/restoration-mod)@[436132621c...](https://github.com/Gullwing-door/restoration-mod/commit/436132621c713306cba351b474199cc75d3d60ad)
#### Tuesday 2022-06-14 11:59:37 by Noep

.30-06 stopping power

-Reduced the range but increased the minimum damage of the M1 Garand
--Also fuck you, Woody :)

---
## [racs4/Kindelia](https://github.com/racs4/Kindelia)@[381577cfaa...](https://github.com/racs4/Kindelia/commit/381577cfaa9dbcb29d0b3a48918bc8c9ce7f5d82)
#### Tuesday 2022-06-14 12:23:35 by Victor Maia

ECDSA account system. Sorry.

Kindelia now uses the same accounts as Ethereum. Run statements can now be signed:

run {
  code_here
} sign {
  signature_here
}

The payload is the serialization of the block. If there is no signature, or if
ECDSA.verify fails, the statement will run with the subject set to "0". If it
checks, the statement runs as usual, except the subject, instead of "0", will
store the last 120 bits of the corresponding Ethereum address. This allows
functions to address users by u120 (20-letter) names.

At this point, I can already hear Kelvin yelling:

"Why... why would you, betray us all like that? How dare you ruin this
magnificently pure, strong network with such a complex, convoluted, fragile
cryptographic primitive that is about to be broken into pieces, either by the
rise of quantum computers, or even classical solutions? We haven't even had a
chance to talk this over! Can't you think of the future children? Can't you
think of the future cats? Why would you put so much effort into designing a
network capable of lasting centuries... only to ruin it overnight?

For him, for future users, for myself, I can only admit: no network can last a
hundred years if it never launches, to begin with. Truth is, it is 2022, we
won't get any kind of reasonable funding if we don't present a working network
with great apps that people can use to buy things and do stuff, today. Lamport
signatures are so huge they don't fit in an entire block, WOTS is extremelly
inefficient, implementing ECDSA on HVM will take months, which we don't have.
All that to end up with inefficient, error-prone, roll-your-own-crypto account
systems on HVM. And until then, there won't be many exciting apps running on
Kindelia. Perhaps anonymous boards, an /r/place clone, things like that, but not
anything that requires authentication. We can avoid all this pain with one line:

  external crate secp256k1;

Sounds tempting, doesn't it? We aren't in a bargaining position. If it helps,
the network will NOT be destroyed by a sudden rise of Quantum computers, unlike
Bitcoin and Ethereum. After all, we don't *rely* on ECDSA. We just use it on the
short term. We can simply demand users to assign hash signatures for backup,
allowing us to just disable ECDSA and let the network recover after such event.
All in all, if Kindelia's most unjustified, fragile aspect is the use of the
most reviewed signature standard in existence, which is also used by every other
project, I guess we're in good shoes.

---
## [Blocksrey/Blocksrey](https://github.com/Blocksrey/Blocksrey)@[52e52c7282...](https://github.com/Blocksrey/Blocksrey/commit/52e52c7282a9f16c511ad1242a9a40d3c311a0a9)
#### Tuesday 2022-06-14 12:59:18 by Jeff Skinner

So I just made like 100 commits trying to debug a fucking problem and it was github's stupid caching of course. Thanks github, fuck you.

---
## [BrunoComitre/ml-design-patterns](https://github.com/BrunoComitre/ml-design-patterns)@[37110a3269...](https://github.com/BrunoComitre/ml-design-patterns/commit/37110a32691d8c63d3c52b842c36e84a3128a9fe)
#### Tuesday 2022-06-14 13:09:08 by Robert Lacok

Include a link to open the project 

Hey, I'm reading through the book and thoroughly enjoying it, thanks @lakshmanok! 

I have some trouble viewing the notebooks here on GitHub though (it keeps saying "Sorry, something went wrong", likely hitting some size limits).

I work at Deepnote, and we try to build better data science notebooks. The proposed button opens the repo as a project in Deepnote, and you can view and execute all of the files – it might be helpful for other readers too :)

---
## [ProjectIgnis/BabelCDB](https://github.com/ProjectIgnis/BabelCDB)@[37423207dd...](https://github.com/ProjectIgnis/BabelCDB/commit/37423207dd2d2f6048aca60c240ff3b21e7f0d9b)
#### Tuesday 2022-06-14 13:27:09 by Naim

Added new Rush cards

From "Megaroad Pack":
- The Half-Body Crawling Around
- Ghoulish Gal
- The Thing in the Purple Mirror
- The Doll of Dread
- Nightmare Knock
- Frightening Fan Mail
- Zombie Carnival
- Zombie Fireworks
- Surprising Zombie Victory
- Gradually Approaching Footsteps
- The Cursed Cat Counting Dishes
- Terror Phone Number
- Cursed Skeletal Dragon Diarga
- The Strange Specter of Celestial Severance
- Sacrificial Summon
- Progress Potter
- Mother's Storm
- Excitagain
From "Deck Modification Pack - Requiem of Destruction!!":
- Dian Keto the Cure Maiden
- Cremation Dog Nitro
- Dynamo Might
- Chemicalize Salamander
- Rice Terrace Ripple
- Ewekai Aquasheep
- Ewekai Thunderlambda
- Ewekai Airaries
- Ewekai Waveschaf
- Melo Melo Meeeg☆Uuultra Beam
- Splendid Floor Master
- Tutumes Dark Witch
- Ichthyosteguard
- Sunbathing Kappa
- Kappa's Gas
- Miginagi the Talismanic Warrior
- Rainy Megalopolis
- Bubble Kingdom
- Nuvia the Wicked Mischief Maker
- Sannomiya Golden G Robo MK-III
- Alien 33
- The Three Warp-Granny Sisters
- Alien Count of the White Dwarf, St. Germain
- 300 Light-Year Red Cloak
- Third Coming of the Reptilian Count
- Area 33
- The Three Moonlit Mystery Geckos
The "Jump Victory Carnival 2022" promo:
- Luster Dragon

---
## [karmaisblackandbluepilled/Merchant-Station-13](https://github.com/karmaisblackandbluepilled/Merchant-Station-13)@[144b5838c0...](https://github.com/karmaisblackandbluepilled/Merchant-Station-13/commit/144b5838c01985628a46954e276f5f643596634c)
#### Tuesday 2022-06-14 13:48:27 by karmaisblackandbluepilled

Adds surplus crate-only items. (#256)

* Funny stuff right here

* is this piece of shit ACTUALLY complaining about indentation in a fucking comment fuck you

---
## [karmaisblackandbluepilled/Merchant-Station-13](https://github.com/karmaisblackandbluepilled/Merchant-Station-13)@[8c35a11b61...](https://github.com/karmaisblackandbluepilled/Merchant-Station-13/commit/8c35a11b61efc2bb38c7d33bd7cb577b536d49f5)
#### Tuesday 2022-06-14 13:48:27 by EtraIV

Fix point vendors (#259)

* Fix point vendors bluescreening if accessed with an ID with no registered account

* You can't (brokenly) take apart point vendors anymore

* Moves the point vendors to the FUCKIGN VENDING DIRECTORY HOLY SHIT TCEO WHY DID YOU PUT THEM IN ECONOMY YOU IDIOT

---
## [T-J-Teru/binutils-gdb](https://github.com/T-J-Teru/binutils-gdb)@[5ea45af594...](https://github.com/T-J-Teru/binutils-gdb/commit/5ea45af594489928873e20ffd4c1c5d31aa30790)
#### Tuesday 2022-06-14 13:57:27 by Andrew Burgess

gdb: native target invalid architecture detection

If GDB is asked to start a new inferior, or attach to an existing
process, using a binary file for an architecture that does not match
the current native target, then, currently, GDB will assert.  Here's
an example session using current HEAD of master with GDB built for an
x86-64 GNU/Linux native target, the binary being used is a RISC-V ELF:

  $ ./gdb/gdb -q --data-directory ./gdb/data-directory/
  (gdb) file /tmp/hello.rv32imc.x
  Reading symbols from /tmp/hello.rv32imc.x...
  (gdb) start
  Temporary breakpoint 1 at 0x101b2: file hello.rv32.c, line 23.
  Starting program: /tmp/hello.rv32imc.x
  ../../src/gdb/gdbarch.h:166: internal-error: gdbarch_tdep: Assertion `dynamic_cast<TDepType *> (tdep) != nullptr' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.

The same error is encountered if, instead of starting a new inferior,
the user tries to attach to an x86-64 process with a RISC-V binary set
as the current executable.

These errors are not specific to the x86-64/RISC-V pairing I'm using
here, any attempt to use a binary for one architecture with a native
target of a different architecture will result in a similar error.

Clearly, attempting to use this cross-architecture combination is a
user error, but I think GDB should do better than an assert; ideally a
nice error should be printed.

The problem we run into is that, when the user starts a new inferior,
or attaches to an inferior, the inferior stops.  At this point GDB
attempts to handle the stop, and this involves reading registers from
the inferior.

These register reads end up being done through the native target, so
in the example above, we end up in the amd64_supply_fxsave function.
However, these functions need a gdbarch.  The gdbarch is fetched from
the register set, which was constructed using the gdbarch from the
binary currently in use.  And so we end up in amd64_supply_fxsave
using a RISC-V gdbarch.

When we call:

  i386_gdbarch_tdep *tdep = gdbarch_tdep<i386_gdbarch_tdep> (gdbarch);

this will assert as the gdbarch_tdep data within the RISC-V gdbarch is
of the type riscv_gdbarch_tdep not i386_gdbarch_tdep.

The solution I propose in this commit is to add a new target_ops
method supports_architecture_p.  This method will return true if a
target can safely be used with a specific architecture, otherwise, the
method returns false.

I imagine that a result of true from this method doesn't guarantee
that GDB can start an inferior of a given architecture, it just means
that GDB will not crash if such an attempt is made.  A result of false
is a hard stop; attempting to use this target with this architecture
is not supported, and may cause GDB to crash.

This distinction is important I think for things like remote targets,
and possibly simulator targets.  We might imagine that GDB can ask a
remote (or simulator) to start with a particular executable, and the
target might still refuse for some reason.  But my thinking is that
these refusals should be well handled (i.e. GDB should give a user
friendly error), rather than crashing, as is the case with the native
targets.

For example, if I start gdbserver on an x86-64 machine like this:

  gdbserver --multi :54321

Then use GDB to try and load a RISC-V binary, like this:

  $ ./gdb/gdb -q --data-directory ./gdb/data-directory/
  (gdb) file /tmp/hello.rv32imc.x
  Reading symbols from /tmp/hello.rv32imc.x...
  (gdb) target extended-remote :54321
  Remote debugging using :54321
  (gdb) run
  Starting program: /tmp/hello.rv32imc.x
  Running the default executable on the remote target failed; try "set remote exec-file"?
  (gdb)

Though the error is not very helpful in diagnosing the problem, we can
see that GDB has not crashed, but has given the user an error.

And so, the supports_architecture_p method is created to return true
by default, then I override this in inf_child_target, where I compare
the architecture in question with the default_bfd_arch.

Finally, I've added calls to supports_architecture_p for the
run (which covers run, start, starti) and attach commands.

This leaves just one question, what about native targets that support
multiple architectures?

These targets can be split into two groups.  First, we have targets
like x86-64, which also supports i386 binaries.  This case is easy to
handle, as far as BFD is concerned there is only one architecture,
bfd_arch_i386, and we then use machine types to split this
architecture into x86-64 and i386 (and others).  As the new
supports_architecture_p function only checks the bfd architecture,
then there is nothing additional needed for this case.

The second group of multi-architecture targets requires more work.
The only targets that I'm aware of that fall into this group are the
rs6000-aix-nat.c, ppc-*-nat.c targets, and the aarch64-linux-nat.c
target.

The first group (rs600/ppc) support bfd_arch_rs6000 and
bfd_arch_powerpc, while the second (aarch64) supports bfd_arch_arm and
bfd_arch_aarch64.

To deal with these targets I have overridden the
supports_architecture_p function in each of the separate target files,
these overrides check both of the supported architectures.

One final note, in the rs6000/ppc case, the FreeBSD target supports
both architectures, and so we override supports_architecture_p.  In
contrast, the aarch64_fbsd_nat_target target does not (yet) support
bfd_arch_arm, and so there is no supports_architecture_p here.  This
can always be added later if/when support is added.

You will notice a lack of tests for this change.  I'm not sure of a
good way that I can build a binary for a different architecture as
part of a test, but if anyone has any ideas then I'll be happy to add
a test here.  The gdb.base/multi-arch.exp test exists, which for
AArch64 will test compiling and running something as both AArch64 and
ARM, but this doesn't cover the error case, just that the overridden
supports_architecture_p works in that case.

---
## [Rahul1719/ML-project1](https://github.com/Rahul1719/ML-project1)@[948b667f9a...](https://github.com/Rahul1719/ML-project1/commit/948b667f9a920223179fd8114f579bfcf22004bf)
#### Tuesday 2022-06-14 14:02:26 by Rahul Pal

Update README.md

Machine Learning Project1

Topic : Make a ML model to predict whether person has Heart disease or not.
Used: Python, Jupyter notebook 
Step1: Took a data from Kaggle datasets.
Step2: performed EDA
Step3: Build a ML model and predict and checked accuracy.

Observations:
1. Our problem involves a tabular dataset with 18 variables in which we can find categorical and numerical variables and one of them is the target variable. 
2. We are going to Analyze different type of parameters which are given in the dataset and try to find out correlation between them. There are zero null values which will simply our work. 
3. Wow, these data suggest that not consuming alcohol has a correlation with suffering heart disease. But this part also would be advisable to consult with an expert.
4. Given dataset states that males have the maximum numbers of heart disease in comparison to females. 
5. We can easily say that there is a positive correlation between get heart disease and be older. 
6. It also states that white people have more heart disease cases comparison to others. 
7. And if your health status is poor then you might be under threat of heart disease comparison to other health conditions.

About Model:
1.	It is a classification problem so have used two classification models one of them is Logistic Regression and another one is KNN.
2.	After building the model have checked accuracy of the model and compared the accuracy of Logistic regression and KNN.
3.	And we got 91% accuracy of logistic regression and 90% accuracy of KNN.

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[de7e66b921...](https://github.com/canalplus/rx-player/commit/de7e66b921dc8c803cafd38b4d25bd1c9c82d777)
#### Tuesday 2022-06-14 14:59:56 by Paul Berberian

HTMLMediaElement's related error have now the initial message if it exists

I was very shamefully not aware that `MediaError`s as emitted by
HTMLMediaElement could have a `message` property describing the actual
problem.

For my defense, this was not always the case for MediaErrors (I found
some w3c and chrome links to prove it!).
Yet it apparently is since 2017, so my defense is still pretty weak.

Relying on those could definitely have saved us many hours of debugging
over the years, where we were trying to find which segment of which
type provoked a MEDIA_ERR_DECODE and why.

Anyway, I prefer not to think to much about it, here it is, and now it's
available: the corresponding error message will actually be the message
of the corresponding `RxPlayer`'s `MediaError`'s message (yes, both the
native browser error and the RxPlayer supplementary layer have the
exact same name, and no, it cannot be a source of confusion at all, why
would you say that?).

---
## [TDKorn/my-magento](https://github.com/TDKorn/my-magento)@[b268bdfab9...](https://github.com/TDKorn/my-magento/commit/b268bdfab96f2b977cbfffdd7e88340a2add33ab)
#### Tuesday 2022-06-14 15:01:56 by TDKorn

Update README I think this was a mistake

* Oh my god?? That took so long
* What
* What am I gonna do when I update literally anything
* It's kinda 🆒 though 😎

---
## [owenmoogk/wave-function-collapse](https://github.com/owenmoogk/wave-function-collapse)@[c6c36f52f1...](https://github.com/owenmoogk/wave-function-collapse/commit/c6c36f52f106178793c4076a21360c577eb0dc83)
#### Tuesday 2022-06-14 16:45:39 by Owen Moogk

fucking finally

this was weeks in the making, javascript is wonderful but the timing of things can be a royal pain.

very happy i was able to diagnose and troubleshoot this one

basically made another dictionary which contained the changes, and then we were able to propagate and update, while not yet applying the changes. Then, we could propagate after we updated the screen.

yay

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[13a65d3682...](https://github.com/cockroachdb/cockroach/commit/13a65d3682863dc94b5057801edae7ed8f7d7d18)
#### Tuesday 2022-06-14 17:12:45 by Andrei Matei

util/tracing: fix crash in StreamClientInterceptor

Before this patch, our client-side tracing interceptor for streaming rpc
calls was exposed to gRPC bugs being currently fixed in
github.com/grpc/grpc-go/pull/5323. This had to do with calls to
clientStream.Context() panicking with an NPE under certain races with
RPCs failing. We've recently gotten two crashes seemingly because of
this. It's unclear why this hasn't shown up before, as nothing seems new
(either on our side or on the grpc side). In 22.2 we do use more
streaming RPCs than before (for example for span configs), so maybe that
does it.

This patch eliminates the problem by eliminating the
problematic call into ClientStream.Context(). The background is that
our interceptors needs to watch for ctx cancelation and consider the RPC
done at that point. But, there was no reason for that call; we can more
simply use the RPC caller's ctx for the purposes of figuring out if the
caller cancels the RPC. In fact, calling ClientStream.Context() is bad
for other reasons, beyond exposing us to the bug:
1) ClientStream.Context() pins the RPC attempt to a lower-level
connection, and inhibits gRPC's ability to sometimes transparently
retry failed calls. In fact, there's a comment on ClientStream.Context()
that tells you not to call it before using the stream through other
methods like Recv(), which imply that the RPC is already "pinned" and
transparent retries are no longer possible anyway. We were breaking
this.
2) One of the grpc-go maintainers suggested that, due to the bugs
reference above, this call could actually sometimes give us "the
wrong context", although how wrong exactly is not clear to me (i.e.
could we have gotten a ctx that doesn't inherit from the caller's ctx?
Or a ctx that's canceled independently from the caller?)

This patch also removes a paranoid catch-all finalizer in the
interceptor that assured that the RPC client span is always eventually
closed (at a random GC time), regardless of what the caller does - i.e.
even if the caller forgets about interacting with the response stream or
canceling the ctx.  This kind of paranoia is not needed. The code in
question was copied from grpc-opentracing[1], which quoted a
StackOverflow answer[2] about whether or not a client is allowed to
simply walk away from a streaming call. As a result of conversations
triggered by this patch [3], that SO answer was updated to reflect the fact
that it is not, in fact, OK for a client to do so, as it will leak gRPC
resources. The client's contract is specified in [4] (although arguably
that place is not the easiest to find by a casual gRPC user). In any
case, this patch gets rid of the finalizer. This could in theory result
in leaked spans if our own code is buggy in the way that the paranoia
prevented, but all our TestServers check that spans don't leak like that
so we are pretty protected. FWIW, a newer re-implementation of the
OpenTracing interceptor[4] doesn't have the finalizer (although it also
doesn't listen for ctx cancellation, so I think it's buggy), and neither
does the equivalent OpenTelemetry interceptor[6].

Fixes #80689

[1] https://github.com/grpc-ecosystem/grpc-opentracing/blob/8e809c8a86450a29b90dcc9efbf062d0fe6d9746/go/otgrpc/client.go#L174
[2] https://stackoverflow.com/questions/42915337/are-you-required-to-call-recv-until-you-get-io-eof-when-interacting-with-grpc-cl
[3] https://github.com/grpc/grpc-go/issues/5324
[4] https://pkg.go.dev/google.golang.org/grpc#ClientConn.NewStream
[5] https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/tracing/opentracing/client_interceptors.go#L37-L52
[6] https://github.com/open-telemetry/opentelemetry-go-contrib/blame/main/instrumentation/google.golang.org/grpc/otelgrpc/interceptor.go#L193

Release note: A rare crash indicating a nil-pointer deference in
google.golang.org/grpc/internal/transport.(*Stream).Context(...)
was fixed.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[fc361369a6...](https://github.com/mrakgr/The-Spiral-Language/commit/fc361369a67d2058083159346b824ee1a59fa766)
#### Tuesday 2022-06-14 18:01:09 by Marko Grdinić

"2:10pm. https://www.lightnovelpub.com/novel/the-legendary-mechanic-novel-10062255/245-chapter-267

Let me stop this here. It is time to resume.

During the break I've resumed the style transfer. Only 150 images more until I hit the 800 limit. I plan on going over all the 800 different styles after that.

2:45pm. I had to take an extended break.

https://whoisnnamdi.com/never-enough-developers/

This is an interesting article.

///

Two points I want to drive home:

First — software development has a turnover problem.

Growing the supply of software developers is not trivial because the field already sees high levels of developer dropout and turnover, and this would only increase if the field were to grow larger. A larger software development labor pool would presumably drive down wages, encouraging even more developers to shift out of the profession, especially those past their career midpoints. On that flat part of the earnings curve, the incentive to remain a developer is weak at best.

Second — software development also has a selection problem.

The highest ability, fastest learners disproportionately leave the field over time. They have a multitude of other ways to profitably leverage their intellect and skills. Software development carries serious opportunity cost. Again, this is ironic because one would normally expect the best to stay and worst to leave, but that's not what we see in the data. The software development talent pool mix shifts toward lower cognitive ability as any given cohort matures.

Combined, these points suggest software development may be destined for perennial labor shortages unless the pace of change slows sufficiently.

To conclude, I emphasize: highly skilled people prefer highly stable careers in the long-run. This lets their relative ability and human capital advantage compound over time. Rapid deterioration of skills continuously levels the playing field, preventing the best from separating themselves from the pack. In such a situation, it makes more sense to quit the race early than get caught in the pile up.

///

Pro software development is a field for midwits today. But boy do I miss the money.

Enough of this. Let me start. Reading the HN comments is negative value.

2:50pm. I have two goals.

* Study the building tutorial.
* Study the building generator tutorial.

The later I've studied a bit yesterday, but I want to see what volumetric overrides do while I am at it. I need to drill down into the hip file.

Let me begin with the building tutorial.

3pm. Polyframe is similar to orient along curve.

3:10pm. He set up a sop net directly in the loop. Yeah, I should be doing that more often myself. I always create messy loops.

3:25pm. He is turning a normal into a quaternion, then converting that into a matrix, then multiplying the up vector to change its angle. This is something I will remember how to do.

3:40pm. https://www.sidefx.com/tutorials/assembling-your-city-part-1/

I watched the first tutorial in this mostly out of curiosity, but I am not sure I am willing to build my own building generator.

https://www.sidefx.com/tutorials/complex-roads/

Hmmm, I am going to have to study roads.

https://cgpersia.com/2022/06/unreal-engine-marketplace-real-city-sf-downtown-environment-mega-pack-184465.html

I've also started thinking about assets. This pack is over 14gb though. I might want a Rapidgator account.

https://cgpersia.com/?s=kitbash

The kitbashed scenes here look quite impressive.

3:55pm. Ok, let's not pussyfoot around. I am going to go through the Houdini videos. Then I am going to practice putting together some simple cities. After that if I need to I'll be easily able to swap my cheapo assets with what I've downloaded off the net. It is no problem. What I should instead ore the fundamentals. Thanks to style transfer, I'll be able to get a lot further with a low poly style that I would have otherwise. Also, I should put some thought into how I could use photograps in my art. Style transfer also makes such a workflow much more viable. If necessary why not make use of even paid resources in this area?

The NASA photograph of the background made the cover much better that it would have been otherwise. The Earth textures came from it as well. So it is no trouble.

4:05pm. If I want to pirate kitbashed content and even photographs, I should not hesitate to do it. Once I get some earnings from Heaven's Key I can always license them afterwards. If I do not get any earnings nobody is going to waste their time suing me. Piracy is a win/win for everybody.

I need to focus. The goal is to make the scaffolding. Once I am done with that, only texturing and making the models more elaborate will remain, but that is the easy part. It will be no problem for me to work on pieces, either by myself or to get them from some kit.

The procedural approach I am taking is ideal for blocking out the cities. Houdini was made for this kind of thing. It will give me a lot of power.

After I am done with this, I'll also want an atmospheric shot, so I'll have to model the clouds using volumetrics, but that won't be too hard in Houdini.

Let's just do it. As long as I perservere I'll be able to make rapid progress on this, and then these skills will trully be my own. Right now I am very shallowly 3/5, I need to make the material I've learned practical through a few more projects.

After that I'll start thinking about chara modeling, as well as finishing that Zbrush course. After that comes music.

4:15pm. For now let me not worry too much. Today I should just focus on watching these tutorials. Tomorrow I'll really dive into practice, as well as studying building generator hip file.

https://www.sidefx.com/tutorials/assembling-your-city-part-1/

Let me move to part 2 here.

https://dokaitutorials.com/procedural-buildings-1/

There is some demos of these tools in use here.

4:35pm. It it kind of interesting to finally find out how inline can be used. But watching him do VOP instead of Vex programming is ridiculous. Still, I'll finish what I've started. My focus is not high, but it is not low either.

4:35pm. I have idea why he is spending time aligning points on an axis.

4:40pm. The tutorial is putting me to sleep. I've decided to start skipping. Let me watch part 3 for 5m and then I am going to check out the roads one.

4:55pm. Trying to watch this tutorial was a mistake. It is a waste of time.

Let me take a short break.

Damn it, I knew that watching tutorials that are not on point can impact my motivation negatively and derail me for the day, but I perservered thinking it might get good. It is not a complete waste as I learned about inline code in VOPs, but in general it was.

I somewhat regret getting back into Houdini - this is the danger of it. When you are doing basic modeling you have a clear goal, but once you start messing with nodes and programming it becomes easy to lose sight of that. Fundamentally I must not lose sight of the fact that I just want Hudini to modularize the buildings and not much more.

https://www.sidefx.com/tutorials/complex-roads/

Let me watch these, afterwards I will be done with the tutorials.

5:05pm. Enough, enough, enough!

I must be insane to keep watching this. By the looks of this, these tutorials are really intended if you want to build your own road system and building system from scratch which I do not. I have better things to do.

For the roads, I'll just look into the labs road node.

https://youtu.be/HyOW6fmkgrc
Google’s Imagen AI: Outrageously Good! 🤖

Let me watch this a bit to relax. Imagen is another big diffusion model like DALLE 2.

5:25pm. Time sure flies. What is my goal right now?

The buildgen tutorial.

https://www.sidefx.com/tutorials/building-generator/

Did I maybe get a reply by now on the odforce forums? Nope.

https://www.youtube.com/results?search_query=blender+city+generator

Let me watch some of these. The Houdini tutorials are getting me nowhere, but I want to compare these techniques with Blender. The Blender vids are very succinct.

https://youtu.be/ligKs9aXKsA
City Generator -- Free Procedural City Generation

https://youtu.be/ligKs9aXKsA?t=88

Not something I have in Houdini.

https://youtu.be/ligKs9aXKsA?t=663

This is pretty nice.

5:45pm. Ok, let me start studying the hip file from yesterday.

I am going to go over the labs node again.

```
F1_WINDOW_01_*
```

Hmmm, it allows patterns like this. Then...

Edit: It does not work for the wall.

6pm. Ok, I get the hand placement collider.  I mean, hand placed overrite. It put a bounding box around the gometry, puts that into a group and then does a special group to hide that from 3d view. Strikes me as easy enough. What about the volumetric ovverides?

One thing I am also wondering how I could do curved roofs for arbitrary goes.

6:10pm. God I hate Houdini's UI bugs. I remove a connection, but the scene view does not update. This makes testing out the effects of various actions really confusing.

At any rate, I have it.

With hand placed overrides, you pass in the geometry directly. With volumetric overrides you just pass in a string. Both are fairly similar.

Now, let me try out the wall patterns.

6:25pm. No, putting in `*` does not work. To be honest, this is something I hate the most. Given that you can give the modular pieces weights, it should be possible to mix multiple of them together. But I did the obvious thing and it did not work. Let me study the node directly. I will work backwards from the front.

6:30pm. I want to punch Houdini in the face right now. I am studying the labs code and am trying to figure out how it is instancing the modules and yet I am running into that familiar UI bug where it would keep old data around. Piece of crap. What I just want to figure out if it is possible to make use of modular pieces with different weights.

6:40pm. No forget it. The UI bugs make studying this even harder than it needs to be. The node net for the labs node is huge.

https://youtu.be/n3m9E4-NkqE
Houdini Procedural City Generator

Let me watch this. I am considering ditching Houdini. Let me gather the info I need and then I will move forward with my planning.

https://youtu.be/n3m9E4-NkqE?t=102

Yeah, it is nice.

Time for lunch.

6:55pm. Done with lunch. Let me watch the video. I feel like I am going through this the wrong way. Rather than trying to make Houdini work, I should be trying to make city generation work with the best tool that is out there.

As for the Labs Building Generator, it feels like work on it was dropped midway which is why it has so many unexplained features and missing documentation. The irony is, if the tool had less stuff in it, but had the docs available, I would be a lot less anxious about using it.

7:15pm. https://www.turbosquid.com/FullPreview/Index.cfm/ID/1631084

Costs 120$. I haven't watched more than a few minutes before I checked it out.

http://www.cgchan.com/
SceneCity

This one looks really promising, it is an addon for Blender, works with 3.0 and the latest version is right on CGPersia.

> You can also use your own assets.

Yeah, this is a really strong sell compared to doing it in Houdini.

7:20pm. Tsk.

https://www.youtube.com/results?search_query=blender+city+generation

Well, I still want to watch some of the other Youtube vids on this. But yeah, it is 100% the case that Houdini should not have been my first goto for building cities. I should have look specifically for city generators. This mistake probably cost me two days of my time.

Finally, my brain has started working properly again.

Let me start the download for it.

https://cgpersia.com/2021/08/gumroad-scenecity-1-9-1-179252.html

7:25pm. I must make sure not to mess up the download start.

At any rate, this is the true benefit of living in a technologically advanced society. It is being able to reuse programs made by others. Afterwards if I want my own buildings and need more control, I can consider Houdini.

This is the proper way to use 3d.

You start from the high and move to the low.

RapidGator Captcha: skynet watches

Where do they get these things? Well, if you are really watching, I hope you like what you see.

I am not sure what Skynet's political affiliation is, but I think pro-piracy would be a part of it.

7:35pm. Ok...I won't set the style transfer training until this finishes downloading. Otherwise I might get corruption.

7:40pm. I was really wondering how the Ex-Arm author could do those beautiful cities so easily. Imagine trying to do that from imagination, the effort would be immense. But if he just used a city generator, it might not have been that hard. Or even OSM + texturing. Because of the shot was from a bird's eye view there is no change of it being from reference. Satelite? That just beams straight down. High up on another skyscaper? Very unlikely given how high it was. Helicopter? This one would be possible, but it would be way more expensive than the alternative.

7:45pm. I put in the effort in learning all aspects of 3d. Given time there is nothing that I can't do. But I do not have weeks to spend on each scene. In fact, the deadlines will be so tight once I start, that doing things like ripping the scenes straight from photographs, even going as far as pirating them is a viable tactic.

If I am poor nobody is going to sue me, and if I am rich, getting sued won't bankrupt me.

NN style transfer is really my license to steal. It is the world telling me to pillage and plunder far and wide. Want to model props? Then better resign to getting a job for some studio.

7:50pm. Still...I need to make a golden, reflective city. I am not going to find a photo ref for that. So procedural 3d is my best bet.

In the future if I have to do something like a forest or a mountain - let me not mess with heightfield maps in Houdini or anything of that sort. I will google the relevant generator for that instead. I'll learn the lesson from this.

CGPersia exists for a reason, and I should be taking full advantage of it.

7:55pm. As a programmer I can program in assembly and C, but wouldn't for a good reason. Those things are something I need to understand if I want to have a sense for how the machine works, but it is not like I have to spend my time working in them.

The same goes with 3d. To get impressive scenes done quickly I have to reuse assets of others. It is not strictly the raw skill that separates 2/5 from 3/5, but how they approach the problem to begin with.

8pm. Let me close here, I should have some fun."

---
## [jaddison06/dart-cbuild](https://github.com/jaddison06/dart-cbuild)@[45ae513a92...](https://github.com/jaddison06/dart-cbuild/commit/45ae513a92698c8529acf489cc79ce48c6dc18b7)
#### Tuesday 2022-06-14 18:05:59 by James Addison

this bitch actually cannot code to save his life

#59652b6 was dodgy but the "fix" was also shit

---
## [replayio/devtools](https://github.com/replayio/devtools)@[aa62c1e8a1...](https://github.com/replayio/devtools/commit/aa62c1e8a1aac5cef19453014894023735f05df2)
#### Tuesday 2022-06-14 18:35:34 by Josh Morrow

Make Soft Focus the Default #7114

I've been saying for the past week that we basically already shipped
soft focus, but not technically. I'd like to clarify what I meant by
that, because it's confusing. Let's start from the beginning-ish.

I started [a
document](https://www.notion.so/replayio/Loading-Region-Problems-b8dc0d03c49840f8b504e967c7ea5778)
on April 26th describing an underlying cause for an entire family of
problems that I was seeing in the devtools UI. Around that same time, we
were also seeing a *lot* of crazy behavior with regions loading and
unloading (I'm gonna come back to this). The big takeaway from that
document was that we needed methods for focusing at slices more specific
than regions. We did a lot of work to support this.

- We added range parameters to backend endpoints, so that front-end
  requests could send the range they were interested in, rather than
  always addressing the entirety of all loaded regions
- We reworked how we run, monitor, and store the results of analyses
  generally
- We built two completely new backend endpoints for converting from
  times to TimeStampedPoints
- We built a thunk which observed the focus mode, and decided when it
  should attempt to reload some resources (starting with console
  messages, and then analyses) based on the newly chosen window and
  previous fetches

I'd like to pause at that last one. In many ways, that was the ultimate
goal at the time I wrote that document. It solves all "edge-piece" and
"overflow" problems, and while we can go even farther in the direction
of efficiency, I'm quite happy with the soundness of the foundation
we've laid, and soundness was the motivator for this project.

We shipped the first version of everything up above one week ago, and
sent it out with the newsletter. However, remember how I said that back
when I was first scoping this project we were having a lot of trouble
with loading and unloading regions? Well, one of the things that I
realized early on was that if we correctly handled edge-pieces, it no
longer mattered how big the edge pieces were. And if it does not matter
how big the edge pieces are, then there's no reason to forcibly unload
parts of the recording in order to exclude them. Back when unloading and
loading were causing massive headaches both for us and for users, this
seemed like a huge win, so I made it the final goal of Soft Focus - be
able to move your focus window around, without ever having to unload a
region.

My first shot at it was kind of wonky (you'll see just how wonky in a
second), and I didn't love it. And while we were busy getting everything
ready so we *could* turn this flag on, the rest of the team shipped
Turbo Replay, and all of a sudden, it did not matter that much if we
forcibly loaded or unloaded regions. It's still a nice performance win I
think, for users who are moving their focus window around a lot, and
more importantly, we corrected a ton of soundness problems on the way
here.

---

OK, so back to this change.

The final solution is probably best explained by this comment I wrote
earlier today to explain a type (if you've been deep in the weeds on
this stuff already a lot of this will sound familiar):

>  You might be wondering why there are multiple `begin`s and `end`s for
a single FocusRegion. Well, this is an artifact of the difference
between world-time, which is essentially continuous (and thus, linearly
interpolable), and execution time, which is both discrete (in the sense
that even though there may be many points "between" points 100 and 200,
there may not be any points that are valid for operations like Pausing)
and irregularly spaced (the recording might have many valid points
between the times 100-150ms, but no valid points between 150-500ms).
>
> It is very convenient to accept user input in the form of times. The
user can click somewhere on the timeline (which is really just a visual
interpretation of the continuous, evenly-spaced number line underlying
it), and we can try and use that to filter things down to that time.
>
> And that is where the trouble starts.
>
>  In order to accurately filter resources that are in memory, or to
specify a range to a backend endpoint which accepts ranges, we need to
bound our range by *points*, not just *times*. But the user did not give
us a point, they only gave us a time. So what should we do? Well, we try
to convert from our time to a point. However, because points are
discrete and unevenly spaced, this is not an exact translation, it
introduces a small amount of error (usually on the order of <100ms, but
occasionally more). Also, to be as precise in the conversion as possible
we need to hit a backend endpoint (getPointsBoundingTime), which is not
horribly expensive, but is significantly more expensive than a simple
lookup, for instance.
>
>  All of this causes problems, especially when the user is dragging
around a focus window. This is because:
>  1) The little errors start to add up. If you "snap" the continuous
values of
>  the timeline to the discrete values of the pointline, you introduce a
little bit of error. Then, maybe the user drags the line another pixel,
and you introduce another little error, and so on and so forth and, well
screens have many pixels so this can get out of hand quickly.
>  2) A difference of less than 100ms might not be super noticeable on
the timeline, but as the errors get larger (or if the recording is quite
short, for instance) it will start to be clear to the user that we are
not actually putting them at quite the time that they asked for. And,
well, we have very good reasons for doing that, but they are very hard
to explain (for instance, we might have to subject them to reading
something like this comment).
>  3) If we try and do an exact lookup every time the focus window
changes while selecting it, we will end up sending a *ton* of protocol
messages.
>
>  The solution I have come up with so far is that we store *two*
windows. One window is used for display. It is what we show on
timelines, and it is also what we use as the inputs to our time -> point
transformation *after* the user has chosen their focus window.
>
>  The other time is a proper TimeStampedPointRange, which we use to do
things like filter resources by point and interact with backend
endpoints which accept ranges.

With the above solution, we can ship Soft Focus (in the sense that there
does not need to be any forced unloading) without degrading the
experience of picking a focus window or having to expose the messiness
of the above to the user. Next, will be actually utilizing
`Session.getPointsBoundingTime` to be more specific in our mapping, but
even now, we are pretty darn specific most of the time, so I wanted to
get this in rather than waiting for that optimization piece to be done.

As for the changes this actually makes:

- Deletes the `Soft Focus` flag from experimental settings
- Changes `startTimeForFocusRegion` to `displayedStartForFocusRegion`
- Likewise for `endTimeForFocusRegion` to `displayedEndForFocusRegion`
- Displays the `displayed` time values when choosing a window, rather
  than the mapped-points' time values

That's it! Not a ton of changes, but building on a much larger set over
the past 6 weeks 🏗️

---
## [Shahidahmed212/Shahid-Ahmed-](https://github.com/Shahidahmed212/Shahid-Ahmed-)@[fb711fcc67...](https://github.com/Shahidahmed212/Shahid-Ahmed-/commit/fb711fcc67f3b4c296356623f43d166c594ba51b)
#### Tuesday 2022-06-14 19:33:35 by Shahid Ahmed

Shahid Ahmed 

Shahid Ahmed (born 08 January 1996) was born in Moulvibazar,Sylhet,Bangladesh. His Current address is Saudi Arabia, Mecca. Shahid Ahmed is a Bangladeshi musical artist, Singer, Song writer, politician, Author, Entrepreneur and Actor. Shahid Ahmed is a young Musician in the music industry. With the rapid growth and modernization of technology in the twenty-first century, young minds are inspired to create new and inspiring ideas that can make a huge difference in today’s technology. One such example is Shahid Ahmed. Who, through his knowledge and hard work, is gifting new music to the world.

Career:
Musician in Sylhet,Bangladesh did not show any age limit when it comes to dreams and aspirations. At a very young age he set up his own company called the World of Love. Shahid Ahmed is spreading love music around the world through his various solo songs as well as international podcasts Spotify, MusicMatch, Amazon Music, Apple Music. 

Personal Life:
Shahid Ahmed gave one love music gift after another. His notable music was Fake Love, Like Wow, Love Game. He has taken many initiatives in the digital market and is also working in the market plus with the digital market.

Shahid Ahmed’s success at a young age helps us to understand that we must try to succeed. We have much to learn from him. We should all learn from young Shahid Ahmed that everything is possible if people try.

Discography-

Single Track:
01. Love Story
02. Love Letter
03. Love Game
04. Mother Love
05. Love is Game
06. Father Love
07. Music is enjoyed Life.  Etc.

---
## [bob-b-b/tgstation](https://github.com/bob-b-b/tgstation)@[20e4add487...](https://github.com/bob-b-b/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Tuesday 2022-06-14 21:02:16 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [nicolinc/iommufd](https://github.com/nicolinc/iommufd)@[b9364eed92...](https://github.com/nicolinc/iommufd/commit/b9364eed9232f3d2a846f68c2307eb25c93cc2d0)
#### Tuesday 2022-06-14 21:41:12 by Douglas Anderson

drm/msm/dpu: Move min BW request and full BW disable back to mdss

In commit a670ff578f1f ("drm/msm/dpu: always use mdp device to scale
bandwidth") we fully moved interconnect stuff to the DPU driver. This
had no change for sc7180 but _did_ have an impact for other SoCs. It
made them match the sc7180 scheme.

Unfortunately, the sc7180 scheme seems like it was a bit broken.
Specifically the interconnect needs to be on for more than just the
DPU driver's AXI bus. In the very least it also needs to be on for the
DSI driver's AXI bus. This can be seen fairly easily by doing this on
a ChromeOS sc7180-trogdor class device:

  set_power_policy --ac_screen_dim_delay=5 --ac_screen_off_delay=10
  sleep 10
  cd /sys/bus/platform/devices/ae94000.dsi/power
  echo on > control

When you do that, you'll get a warning splat in the logs about
"gcc_disp_hf_axi_clk status stuck at 'off'".

One could argue that perhaps what I have done above is "illegal" and
that it can't happen naturally in the system because in normal system
usage the DPU is pretty much always on when DSI is on. That being
said:
* In official ChromeOS builds (admittedly a 5.4 kernel with backports)
  we have seen that splat at bootup.
* Even though we don't use "autosuspend" for these components, we
  don't use the "put_sync" variants. Thus plausibly the DSI could stay
  "runtime enabled" past when the DPU is enabled. Techncially we
  shouldn't do that if the DPU's suspend ends up yanking our clock.

Let's change things such that the "bare minimum" request for the
interconnect happens in the mdss driver again. That means that all of
the children can assume that the interconnect is on at the minimum
bandwidth. We'll then let the DPU request the higher amount that it
wants.

It should be noted that this isn't as hacky of a solution as it might
initially appear. Specifically:
* Since MDSS and DPU individually get their own references to the
  interconnect then the framework will actually handle aggregating
  them. The two drivers are _not_ clobbering each other.
* When the Qualcomm interconnect driver aggregates it takes the max of
  all the peaks. Thus having MDSS request a peak, as we're doing here,
  won't actually change the total interconnect bandwidth (it won't be
  added to the request for the DPU). This perhaps explains why the
  "average" requested in MDSS was historically 0 since that one
  _would_ be added in.

NOTE also that in the downstream ChromeOS 5.4 and 5.15 kernels, we're
also seeing some RPMH hangs that are addressed by this fix. These
hangs are showing up in the field and on _some_ devices with enough
stress testing of suspend/resume. Specifically right at suspend time
with a stack crawl that looks like this (from chromeos-5.15 tree):
  rpmh_write_batch+0x19c/0x240
  qcom_icc_bcm_voter_commit+0x210/0x420
  qcom_icc_set+0x28/0x38
  apply_constraints+0x70/0xa4
  icc_set_bw+0x150/0x24c
  dpu_runtime_resume+0x50/0x1c4
  pm_generic_runtime_resume+0x30/0x44
  __genpd_runtime_resume+0x68/0x7c
  genpd_runtime_resume+0x12c/0x20c
  __rpm_callback+0x98/0x138
  rpm_callback+0x30/0x88
  rpm_resume+0x370/0x4a0
  __pm_runtime_resume+0x80/0xb0
  dpu_kms_enable_commit+0x24/0x30
  msm_atomic_commit_tail+0x12c/0x630
  commit_tail+0xac/0x150
  drm_atomic_helper_commit+0x114/0x11c
  drm_atomic_commit+0x68/0x78
  drm_atomic_helper_disable_all+0x158/0x1c8
  drm_atomic_helper_suspend+0xc0/0x1c0
  drm_mode_config_helper_suspend+0x2c/0x60
  msm_pm_prepare+0x2c/0x40
  pm_generic_prepare+0x30/0x44
  genpd_prepare+0x80/0xd0
  device_prepare+0x78/0x17c
  dpm_prepare+0xb0/0x384
  dpm_suspend_start+0x34/0xc0

We don't completely understand all the mechanisms in play, but the
hang seemed to come and go with random factors. It's not terribly
surprising that the hang is gone after this patch since the line of
code that was failing is no longer present in the kernel.

Fixes: a670ff578f1f ("drm/msm/dpu: always use mdp device to scale bandwidth")
Fixes: c33b7c0389e1 ("drm/msm/dpu: add support for clk and bw scaling for display")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Abhinav Kumar <quic_abhinavk@quicinc.com>
Tested-by: Jessica Zhang <quic_jesszhan@quicinc.com> # RB3 (sdm845) and
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@linaro.org>
Patchwork: https://patchwork.freedesktop.org/patch/487884/
Link: https://lore.kernel.org/r/20220531160059.v2.1.Ie7f6d4bf8cce28131da31a43354727e417cae98d@changeid
Signed-off-by: Abhinav Kumar <quic_abhinavk@quicinc.com>

---
## [tvrusso/XyceBundle](https://github.com/tvrusso/XyceBundle)@[6d250cd9f7...](https://github.com/tvrusso/XyceBundle/commit/6d250cd9f795484ccbd9af3426c7af454bdd5ce2)
#### Tuesday 2022-06-14 22:33:25 by Tom Russo

Update reconfigure for FreeBSD

Clang loves to complain when you specify an argument that is not used
by the compiler.  For example, if you specify "-Wl,..." (which means
"pass this argument to the linker") on a straight compile line, it'll
complain that it is a compiler not a linker and it is ignoring the
linker arguments.  This is a pointless warning --- we *KNOW* it's for
the linker, it is OK for everything but the linker to ignore it.

The Xyce autoconf process now forces a "-Wl,-rpath..." into the flags
automagically and so now Clang bitches constantly on every file.

This commit adds the magic incantation to tell clang to shut up and
ignore the unused arguments like a good boy.

---
## [Qwertytoforty/Paradise](https://github.com/Qwertytoforty/Paradise)@[ab7a358506...](https://github.com/Qwertytoforty/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Tuesday 2022-06-14 22:36:24 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [phoebethewitch/phoebethewitch.github.io](https://github.com/phoebethewitch/phoebethewitch.github.io)@[9b23d78bc9...](https://github.com/phoebethewitch/phoebethewitch.github.io/commit/9b23d78bc90e5ccd16cd8c8c019fcd58d26e3c2f)
#### Tuesday 2022-06-14 23:34:19 by phoebe

this doesnt fucking work and i dont care about life enough anymore to fucking fix it

i want to die.

---

