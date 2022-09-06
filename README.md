## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-05](docs/good-messages/2022/2022-09-05.md)


2,226,575 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,226,575 were push events containing 3,233,862 commit messages that amount to 218,702,192 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[dc820fef30...](https://github.com/treckstar/yolo-octo-hipster/commit/dc820fef309eb3c7ba5d48650b6503554242c33b)
#### Monday 2022-09-05 00:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [DunniDee/Project-R](https://github.com/DunniDee/Project-R)@[9399dd164b...](https://github.com/DunniDee/Project-R/commit/9399dd164bffaa93b9dcfa60f4faf40eafa4f2eb)
#### Monday 2022-09-05 00:39:36 by Noobcoodoocoo

1st and 2nd level tweaks for beter fuck you leroy for loking ov

---
## [armyofevilrobots/aoer-plotty-rs](https://github.com/armyofevilrobots/aoer-plotty-rs)@[942604c305...](https://github.com/armyofevilrobots/aoer-plotty-rs/commit/942604c305dfd65ae2e66ee29d61edce1245c3b8)
#### Monday 2022-09-05 01:01:49 by Derek Anderson

Many changes

 - Completely change how hatches work:
   - no more Rc<dyn Bullshit> in the hatch generator. It seemed
     like a good idea at the time, but turned into a painful
     kluge when I went to parallelize the hatching
   - Now it's an Enum. That means no external/pluggable hatches,
     but that wasn't realistically happening anyhow
   - Use par_iter from rayon to make hatch fills brutally fast
   - Turns out that performance was suffering NOT due to the
     intersection code for the lines inside the polygons,
     but instead due to the INSET that we did to keep the
     lines inside the polys by some amount so that we
     didn't have messy hatches. Switched to a clever
     but slightly less accurate method for literally
     a 100:1 speedup. You'll never notice the difference.
 - Fix all tests and examples broken by the above^

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[f0ceecff46...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/f0ceecff46f9b600dfe8e60199f354f61d63a0a4)
#### Monday 2022-09-05 01:06:45 by SkyratBot

[MIRROR] Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff [MDB IGNORE] (#16000)

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff (#69158)

About The Pull Request

Title!
The CO2 thing is there because it makes my job much easier. Can probably find a way to make it move slowly if a maint insist on it. Prefer not to though.

Drafting because I want to make a second PR that have more sweeping changes (clean vars up, make a simpler formula for damage and heat production, delete underused behaviors, etc). Would honestly prefer if both this and that gets merged at the same time but I'm separating it out since it might be rejected. Or maybe ill combine it here we'll see.
Ignore that, looks like i can keep this one absolutely atomic.
Why It's Good For The Game

Had a lot of trouble when trying to document the SM gas interactions into the wiki, the interactions are all scattered and tracking down everything a gas does is extremely annoying. Hopefully this fixes that.
Changelog

cl
balance: CO2 powerloss inhibition now works immediately based on gas composition instead of slowly ramping up.
refactor: refactored how the SM fetches it's gas info and data. No changes expected except for the co2 thing.
/cl

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[e7230e8b4a...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/e7230e8b4a6d60e1b6c025b52b9f3d2fc26577a5)
#### Monday 2022-09-05 01:06:45 by SkyratBot

[MIRROR] Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) [MDB IGNORE] (#16001)

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)

About The Pull Request

Just to be clear, when I refer to time here, I am not talking about cpu time. I'm talking about real time.
This doesn't significantly reduce the amount of work we do, it just removes a lot of the waiting around we need to do for db calls to finish.

Adds queuing support to sql bans, so if an ongoing ban retrieval query is active any successive ban retrieval attempts will wait for the active query to finish

This uses the number/blocking_query_timeout config option, I hope it's still valid

This system will allow us to precache ban info, in parallel (or in batches)
With this, we can avoid needing to setup all uses of is_banned_from to support parallelization or eat the cost of in-series database requests

Clients who join after initialize will now build a ban cache automatically

Those who join before init is done will be gathered by a batch query sent by a new subsystem, SSban_cache.

This means that any post initalize uses of is_banned_from are worst case by NATURE parallel (since the request is already sent, and we're just waiting for the response)

This saves a lot of headache for implementers (users) of the proc, and saves ~0.9 second from roundstart setup for each client (on /tg/station)

There's a lot of in series is_banned_from calls in there, and this nukes them. This should bring down roundstart join times significantly.

It's hard to say exactly how much, since some cases generate the ban cache at other times.
At base tho, we save about 0.9 seconds of real time per client off doing this stuff in parallel.
Why It's Good For The Game

    When I use percentages I'm speaking about cost per player

I don't like how slow roundstart feels, this kills about 66% of that. the rest is a lot of misc things. About 11% (it's actually 16%) is general mob placing which is hard to optimize. 22% is manifest generation, most of which is GetFlatIcons which REALLY do not need to be holding up the main thread of execution.

An additional 1 second is constant cost from a db query we make to tell the server we exist, which can be made async to avoid holding the proc chain.

That's it. I'm bullying someone into working on the manifest issue, so that should just leave 16% of mob placing, which is really not that bad compared to what we have now.
Changelog

cl
code: The time between the round starting and the game like, actually starting has been reduced by 66%
refactor: I've slightly changed how ban caches are generated, admins please let me know if anything goes fuckey
server: I'm using the blocking_query_timeout config. Make sure it's up to date and all.
/cl

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [153974-HSI-OXLEY-BANKS-40ACT/150-EAST-42ND-STREET](https://github.com/153974-HSI-OXLEY-BANKS-40ACT/150-EAST-42ND-STREET)@[4f4f578c7b...](https://github.com/153974-HSI-OXLEY-BANKS-40ACT/150-EAST-42ND-STREET/commit/4f4f578c7beff55f66ea382ea376102baa320d63)
#### Monday 2022-09-05 01:51:01 by 1212-5858

 *** YOU ARE GOING TO REQUIRE A DISCLAIMER TO WARN ALL OF YOUR CLIENTS, THEY WERE AND ARE AT A SEVERE DISADVANTAGE FOR ANY CASE FILED IN AMERICA. THE WHOLE FIRM. CAPICHE? ANY PUBLICLY TRADED CLIENTS I NEED TO TALK TO?

ATTN OF THE WILSON ELSER LAW FIRM.

*** YOU ARE GOING TO REQUIRE A DISCLAIMER TO WARN ALL OF YOUR CLIENTS, THEY WERE AND ARE AT A SEVERE DISADVANTAGE FOR ANY CASE FILED IN AMERICA. THE WHOLE FIRM. CAPICHE? ANY PUBLICLY TRADED CLIENTS I NEED TO TALK TO?

I ADVISE YOU REFUND ALL OF THOSE RETAINERS, AND BRING THAT LEXUS BACK TO THE DEALERSHIP. YOU FUCKING BITCH.

https://github.com/BSCPGROUPHOLDINGSLLC/ZUCKER/blob/main/153974_2020_382%20%5B%206MM%20AGREEMENT%20%5D%20(2).pdf

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Tuesday, January 25th, 2022 at 6:55 AM, BD <bondstrt@protonmail.com> wrote:

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Tuesday, January 25th, 2022 at 6:50 AM, BD <bondstrt@protonmail.com> wrote:
ENJOY THE REPO, AND PLUS, ITS NOT A LISTSERV... ITS A DISTRO.

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/main
Address Required in State of Formation
(Foreign Limited Liability Partnership):
150 EAST 42ND STREET
NEW YORK,NY 10017 USA

SAME ADDRESS AS SHARI S. LASKOWITZ

amy.hanrahan@wilsonelser.com

DIRECTOR OF FINANCE, ALAN RUBIN

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Tuesday, January 25th, 2022 at 6:44 AM, BD <bondstrt@protonmail.com> wrote:

Address Required in State of Formation
(Foreign Limited Liability Partnership):
150 EAST 42ND STREET
NEW YORK,NY 10017 USA

SAME ADDRESS AS SHARI S. LASKOWITZ

amy.hanrahan@wilsonelser.com
DIRECTOR OF FINANCE, ALAN RUBIN

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Tuesday, January 25th, 2022 at 6:29 AM, BD <bondstrt@protonmail.com> wrote:

ATTN: THE MESSES ORTIZ & PENA...
YOU CAN USE SOME EXERCISE, AT LEAST BACK THEM YOU P.O.S.
>> INSTEAD OF PLAYING WITH THE ZUCKERS (YOU DID LOSE A 22-YEAR OLD) IF YOU DIDN'T NOTICE....

THIS ORTIZ & PENA GROUP WILL RE-DIRECT THE BARIS DINCER, OF MANHATTAN WITH 99+ POLICE OFFICERS ON A EMAIL... HAPPENS EVERYDAY RIGHT?

A 3-min walk from Trinity Church
 55 Thompson St, New York, NY

- WHERE THE F^^^ ARE THEY, AND WHERE THE  F^^^ ARE MY TAPES?
- SEND A DETECTIVE? MAYBE A GOOD IDEA - FOR YOUR OWN SPIRIT...
- NOT MY JOB. I ALREADY ASKED.. YOU SEE THE RESPONSE I GET... BELOW??

- LAST I ASKED YOU SENT ME TO THE WRONG PRECINCT, SO WHAT THE F^^^ ARE YOU HIDING FOR THEM?
- GUESS WHAT, I STOPPED FIGHTING WHEN I WAS 22, AND I CAN'T CARRY GUNS EITHER... MY BROTHERS' ORDERS, AND UNFORTUNATELY...
I AM MY BROTHERS' KEEPER.

SO GO BACK TO CADET SCHOOL OR SOMETHING ARITE JUNIOR. GET SOME EXERCISE... I'LL BE THERE  ON THURSDAY, BUT WILL YOU???

DO I SEEM LIKE THE TYPE THAT REALLY CALLS/EMAILS POLICE, LIKE ALL OF THEM, EVEN IN THE COUNTY OF KINGS, ZIP-CODED 10018.
> HOW STUPID ARE YOU, SERIOUSLY - MUST BE A ZUCKER...

101 WEST 55TH STREET, NEW YORK, NY, 10019

SEE ALSO DOCKET 179 [ RENT REGULATION BANDS ]
SEE ALSO DOCKET 073 [ AUTOPAID $3,106.82 ]

THAT NUMBER LOOKS HIGHER THAT $3000.00 RIGHT?
- DO YOU SEE A CHECK BOX THERE, ON DOCKET 6?
NYSCEF DOC. NO. 6 - 153974/2020:   NO CHECK BOX...
AUTOBILLED DOCKET 073 [ AUTOPAID $3106.82 ]  = THEFT, PETTY... RIGHT...

REGULAR RENT = 2395.00

RANDOM OVERCHARGE, CONVENIENTLY THROUGH THE THRESHOLD:

REQUEST FOR A REFUND....

NO RESPONSE.

[DOCKET 00048] 153974_2020 - INSIDE VIEW YES OR NO.

THERE'S NO OPTION, TO WILLFULLY PAY FOR THE ATTORNEY'S - NO CHECK BOX ON THE LEASE. ANYWHERE.

FINED $352,500,000.00 USD IN 2015, FOR THE EXACT...SAME...THING.
- WERE YOU LEGAL AGE THEN BTW?

- MIWA CAN SWEAR UNDER OATH TO FINDING A MASK DURING COVID-19...
- IT CAN BE CONSIDERED A LIE, HEARSAY, OR INADMISSIBLE.

WHAT A NOVEL AND IMPRESSIVE STATEMENT "MIWA"... NOW ABOUT THIS WHOLE PRIVACY ISSUE...

THE ZUCKERS WILL SIGN ANYTHING... AND FOR 6 MILLION MILLION DOLLARS THEY PUT THOUSANDS OF PAGES (AS REQUIRED)

- ATTEMPTED TO OBTAIN A LOAN AND TRANSFER TO A STATE FARM INSURANCE CORPORATION...
I NOTICED THE EXECUTIVES AGGRESSIVELY NONSENSICAL ACCESS, WITHOUT ANY GROUNDS REALLY SO
I LOOKED INTO THE FEDERAL DOMAIN AND TAX RECORDS WHILE I WAS BEING HARRASSED, VIDEOTAPED, ETC...

FOUND SOME IMPORTANT INFORMATION, AND CONTACTED THE RESPECTIVE INDIVIDUALS ON THE 8TH OF AUGUST, 2020.
> HAVE NOT HEARD BACK FROM THEM SINCE, NOT A WHISPER - AND THEY HAVE NOT RESPONDED TO AN EMAIL, WIRED ME THE MONEY THEY STOLE, AND
I AM CERTAIN THEY ARE NOT ALL IN JAIL, OWING TO A RECENT FILING I SAW IN THE FEDERAL RECORDS
> DEMONSTRATES THERE IS A FINANCIAL ARM OF THE ZUCKERS' FUNCTIONING

101 WEST 55TH STREET, NEW YORK, NY, 10019

AS ENTERED TOGETHER WITH DOCKET 380, IN THE MATTER OF 153974/2020:

101 WEST 55TH STREET, NEW YORK, NY, 10019

OR IS 103 WEST 55TH STREET, ZIPCODE 100018 AAS SWORD TO UNDER THE QUEEN OF ENGLAND BY THE ZUCKERS AND THEIR REPRESENTATIVES WHILE VIDEOTAPING, AND HARASSING ME FOR NEARLY A YEAR.

HOW DO YOU FEEL TODAY PRECINCT #1? '
PRECINCT #23?
     YOU PUT THE GUY ON HOLD TO WATCH THE NEW ZUCKER TENANTS TOUCHING THEMSELVES AND RE-DIRECT AN EMERGENCY ON FRIDAY TO HELP THE QUEEN OF ZUCKER

LOCATED AS ENTERED IN THEIR F^^^^ NY DOS AND THEIR P.O.S 55 THOMPSON STREET, IF IT WERE UPTO ME,..
LOOKS LIKE A NICE POLICE STATION ACTUALLY.... SERIOUSLY..

24 HOUR DOORMAN... WHY DON'T YOU GO OVER THERE AND ASK THEM WHERE TO FIND THESE CRIMINALS BEFORE YOU UNDERSTAND WHAT IT MEANS TO INCITE THE PEACE, AND REACH ABOUT TWO FEET, PICK UP YOUR WALKIE-TALKIE - AND DISPATCH A ZUCKER INSTEAD OF PLAYING GAMES...

- WELL, WHILE YOU ARE IN THE JURISDICTION... WHY DON'T YOU CARRY YOU WALK OVER THERE BEFORE THURSDAY.... THEN YOU CAN SEE WHAT HAPPENS WHEN YOU PLAY GAMES WITH LARCENISTS, CHILD MOLESTORS, AND VIOLATORS OF THE STATE AND FEDERAL LAWS WHILE THE GOOD ONES CARRY THE ONES YOU LOST ON FRIDAY.

THINK ABOUT YOUR CHILDREN, AND I DID ASK YOU DO THE CITY A SERVICE LAST I CHECKED...NOT MY JOB BUT NOW...
 THE F^^^^ ZUCKERS  WILL WATCH YOUR CHILDREN, AND SO WILL THEIR RELATED ENTITIES, ATTORNEYS, ASSOCIATES, FRIENDS, ETC...

AS ENTERED, BY YOURS TRULY,  THEY WILL FALSELY ATTEST TO THEIR OWN ADDRESSES...
-  AS DID YOU MISS PENA WHEN I ASKED FOR ASSISTANCE, LED ME TO THE 1ST PRECINCT - THEIR CROWN JEWEL!!!
-  IS THAT WHAT YOU WERE DOING ON FRIDAY? PLAYING DESPERATE HOUSEWIFE WITH THE ZUCKERS' CROWN JEWEL MISS PENA?

WASTE OF SPACE, DO THE CITY A FAVOR... AND LET ME KNOW WHAT ZIP CODE THAT IS DOWN THERE?

HERE IS A DIRECT LINK FOR YOU TO SEND TO SHARI, AND THE ZUCKER'S [ IN CASE YOU ARE ENJOINED, OR AFFILIATED WITH THEM]
https://github.com/BSCPGROUPHOLDINGSLLC/153974-2020/blob/main/STFGX-40-17G--FIDELITY%20BOND%20FILING%20-06.08.2020.pdf

FOR LAURIE, DONALD,  ANNE, MIWA AND THE REST OF THE ZUCKER'S NEST:
PLEASE ALSO REFER TO THE PRICE WATERHOUSE COOPERS GLOBAL TAX POLICY CONTACTS AND LET ME KNOW HOW THE CONVERSATION GOES!

THANK YOU FOR YOUR 24 HOUR TURNAROUND ON THE 10TH OF AUGUST 2020.

IN THE COUNTY OF ALAMEDA IN THE AFFIDAVIT OF ALEXIS.. ON THE 10TH OF APRIL (MAYBE EVEN THE 11TH) BUT LOOK HOW THEY PASS THE MESSAGES ALONG
[ DESPERATELY AND WITHOUT MY CONSENT ] , VIDEOTAPE, AND DOCUMENT #21.. IN THEIR PLEADINGS TO VACATE....

DOCKET 32 NOTE THESE TWO RED STAMPS...
- FOR THE CONGLOMERATE OF ZUCKERS... 30 MONTHS IS A DISCOUNT, UNDER OATH...

]
---

THE AFFIDAVIT OF MISS ALEXIS BRANDON, WHO IN THE AFFIDAVIT OF MIWA IS STATED DIFFERENTLY, BUT HER MOTHER WAS EXPECTING HER TO BE HOME.'\

IF YOU THINK THAT'S A 16, AND NOT AN 11,

>>> IT STILL DOESN'T SOLVE THEIR PRIVACY ISSUE, THE FINANCIAL CRIMES, NOTWITHSTANDING LARCENY.
>>> DEEMED "HARDSHIP" IN THE LEASE AND TRANSFER OF ASSETS.

ASK THE 1ST AND 23RD PRECINCT, WHAT DO YOU DO WHEN YOU HIT A YELLOW LIGHT WHEN APPROACHING AN INTERSECTION...
- ENJOY THIS... .AS PAUL R. REGAN, the Esquire DID NOT REFUND ME THE MONEY ON JUNE 3RD, 2020 FOR THE EMERGENCY DAMAGES AND DETONATION OF ALL THEIR PROPERTIES...

HOWEVER DID NOT RETURN THE SECURITY DEPOSIT, WITH NO DAMAGES AWARDED BY HAGGLER IN THE PRIOR, ALSO CONTINUED TO AGGRESSIVELY BILL LARGER SUMS OF MONEY, NONE OF WHICH WERE REFUNDED WERE ALL STOLEN, AND EVERY LAST ZUCKER HAS GONE COMPLETELY SILENT, HOW CONVENIENT.
> ABOUT THIS WHOLE BARRETT IN ANDREWS...
IT WAS DEFINITELY THE LASKOWITZ OUTFIT...

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Tuesday, January 25th, 2022 at 4:39 AM, BD <bondstrt@protonmail.com> wrote:

Tuesday, January 25, 2022 at 02:41:58
FROM FEBRUARY AND THROUGHOUT MY LEASE...
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

no check box either ZUCKERS.

I apologize, but NO CHECK BOX no check box on the LEASE.
as entered in the prior - is LARCENY you CS.

GL and goodnight. You look at the State Farm Documents, semi-annual, ,annual reports.. match them with the Elsers, and the Zuckers' corporataions as well... I will just upon wait for the Edgar Filings on the Federal Record and Post the Securities and Exchange Commission upon notice and information, just like I did on the 8TH of August back in 2020.

 Happy Tuesday, but not for everybody - unfortunately, wasting my TIME is valuable as well
- barring whatever the heck it is you call this rat's nest....

affidavit of Miwako "MIWA" G. Messer

First Name:
BARIS
Last Name:

DINCER
Suffix:
COLUMBIA UNIVERSITY obo TRUSTEES
Company:
COLUMBIA UNIVERSITY obo TRUSTEES
Street Address:
99 WALL STREET
City:	NEW

YORK

State:	NY
Postal Code:	10005
Country:	United States
Work Phone #:	6462563609
Email Address:	BONDSTRT@protonmail.com

Tuesday, January 25, 2022 at 02:41:58
FROM FEBRUARY AND THROUGHOUT MY LEASE...
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

I AM COMING FOR YOUR CLIENTS RICKI. YOU NEED A DISCLAIMER TO INFORM THEM, THEY WILL BE AT A SEVERE DISADVANTAGE - EVEN IF I AM ON A HELICOPTER.

Bergesen v. Manhattanville College
Publication Date: 2021-07-26
Practice Area: Civil Rights
Industry: Education
Court: U.S District Court for the Southern District of New York, U.S. - SDNY
Judge: District Judge Kenneth Karas

	Search | Law.com

Attorneys: For plaintiff: Counsel for Plaintiff: Justin Stedman Clark, Esq., Levine & Blit, PLLC, New York, NY.
for defendant: Counsel for Defendant: Matthew Stein, Esq., Nancy V. Wright, Esq., Ricki E. Roer, Esq., Wilson Elser Moskowitz Edelman & Dicker LLP, New York, NY.
Case Number: 20-CV-3689
Sexual Orientation Discrimination Claim Grounded on Presumed Stereotype Survives Dismissal

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[e1839f0e37...](https://github.com/Paxilmaniac/Skyrat-tg/commit/e1839f0e375a2169c8d80d942376dddb8be1958d)
#### Monday 2022-09-05 02:07:57 by SkyratBot

[MIRROR] Spider Rebalance PR: Burn Baby Burn Edition [MDB IGNORE] (#15997)

* Spider Rebalance PR: Burn Baby Burn Edition (#68971)

This is a remake of #66106, with more thought put into the underlying balance. The main goal of this PR is to make fighting spiders more accessible and interesting for the majority of the crew while nerfing the extremely strong and boring option of simply using freezing temps to kill spiders. Also fixes #67765. The changes are as follows:

NEW SPIDER COUNTERS

    Fly swatters now deal 25 damage to spiders on hit, increased from 1
    Pesticide now deals massive stamina damage to spiders and a little bit of physical damage as well (the damage portion not added by this PR)
    Spiders can now be caught on fire through any traditional mean of catching something on fire. Spiders will automatically put themselves out after a time. This was done instead of an active action because AI spiders are also subject to this change as well, and I don't feel like bloating the simple mob AI with putting themselves out

SPIDER CHANGES

NERFS

    Toxin injection has been removed from all spiders except for the hunter, flesh spiders and the viper
    Hunter toxin (used by hunters and flesh spiders) now only brings the afflicted down to 40 health, and will stop taking effect once the afflicted reaches that threshold. Should the afflicted still have the toxin in their system and get healed, the toxin will begin dealing damage again until the afflicted is at 40 health or below again
    Viper toxin now only brings the afflicted down to 10 health, but also has the hallucination effects of Mindbreaker toxin. This hallucination effect is applied regardless of target health. It also no longer generates other harmful chemicals into the afflicted's system, but is much more potent at base
    Flesh spiders cannot regenerate while on fire

BUFFS

    Time it takes for spiders to normalize their temperature cut by half. While they will react faster when in cold or hot environments, when they leave said environments it will take less time to return to normal temperature
    Unsuitable temperature damage reduced to 4 from 8
    You can no longer push spiders by running into them
    Webbing heat damage threshold increased from 300 to 350 (same temp where spiders also take damage)
    Broodmother egg laying time reduced to 12 seconds from 15
    Broodmother web laying time multiplier reduced to 0.5 from 1
    Broodmother health increased to 60 from 40
    Broodmother damage increased to 10 - 15 from 5 -10

BEHIND THE SCENES CHANGES

    You can now make any simple mob able to be caught on fire by setting flammable to true
    How fast a simplemob stops burning is controlled by fire_stack_removal_speed
    Can now now control how fast simplemobs regulate their temperature using temperature_normalization_speed. Before this PR, this value was hard-coded at 10, I have set the default to 5 as 10 was too long in almost any case. This will notably affect slimes, who could easily die to being cold long after being removed from the cold area. I see this as purely beneficial
    Toxins now have a health_required value. The afflicted has to be above this health value in order to take damage from the toxin. Only used in the spider toxins currently
    When I was setting up simplemobs to be flammable, I noticed basic mobs can be glitchily set on fire, so I fixed it to where they can't be set on fire.

Why It's Good For The Game

    Spacing something is very easy, but not very fun or interesting compared to starting and controlling a fire. Swapping spiders' temperature weakness from spacing to fire is beneficial to the fun of fighting them and playing as them, allowing more creativity and resourcefulness on both sides. Ideally, this should allow for atmosians and chemists to use their skills in a fun way.
    Currently, ignoring spacing them, the only people who can reasonably take on spiders is security, since they have lasers which do burn and stuns to slow the spiders down. However, this small subset of players cannot normally destroy a spider infestation without spacing them, so letting fly swatters and pesticide be used to combat spiders allows other crewmembers to fight back, letting them actually enjoy facing spiders as a threat and allowing the crew to defend themselves.
    Being killed by spider toxin after fighting off a horde isn't fun. The changes still make it a threat you have to be aware of, but not one which detracts as much from the combat loop. This also forces spiders to secure the kill themselves, which is more fun than having the toxin do it for you.
    Broodmothers in their current state are incredibly weak by themselves, which is intentional by design. However, the new changes hope to make playing as a broodmother easier and hopefully allow more broodmothers to get the spider infestation started properly. After all, Dynamic is their common source now, and they should be consistently worth the threat cost to spawn them.
    Previously, spider structures would seemingly vanish for no reason if the room was heated to be greater than 300 but less than 350, as the spiders would not be able to tell that it was too hot. Now, if the structures are taking damage, spiders will also be taking damage, so understanding what's going on should be easier now.
    Pushing spiders into a corner by running into them was not a fun tactic to deal with as a spider and didn't make much sense seeing how big the spiders are.

Changelog

cl
add: Spiders can now be caught on fire
add: Spiders take significant damage from fly swatters and stamina damage from pesticide
balance: Spiders have been re-balanced. Their toxins can no longer kill but they are not as susceptible to freezing
balance: General stats of spider broodmothers have been buffed with more health, damage, and faster web and egg placement
balance: Flesh spiders cannot regenerate whilst on fire
balance: Simplemobs change their internal temperature twice as fast
fix: Basic mobs no longer glitchily catch on fire.
/cl

* Spider Rebalance PR: Burn Baby Burn Edition

Co-authored-by: IndieanaJones <47086570+IndieanaJones@users.noreply.github.com>

---
## [pankajpreet/fucking-algorithm](https://github.com/pankajpreet/fucking-algorithm)@[15b428a8ab...](https://github.com/pankajpreet/fucking-algorithm/commit/15b428a8ab2d3bf09c3f710f90a2240bed0b39c8)
#### Monday 2022-09-05 02:09:54 by Tomasz Surowiec

[English] Correct Edit Distance 

(I feel a need to preface this by saying that the changes I made were based solely on the English version, and the reading experience, for I do not speak Chinese (I'm not even sure if it's Mandarin, Cantonese or which one, nor if there's any difference in writing). Should you object to any changes, please let me know)

1. Changed the apostrophe character from *`* to *'*. The former is not used as an apostrophe, and is actually an accent mark (for preferred characters, refer to (this)[http://snowball.tartarus.org/texts/apostrophe.html] (U+0027 ', U+2019 ’, U+201B ‛)).
2. Changed certain verb forms. For instance: *"The last question is that **writing** a function to calculate [...]"* to *"The last question is **to write** a function which calculates [...]"* (also *which* -> *to* in order to avoid the repetition).
3. Changed the capitalization where necessary. For example: *Helpless* to *helpless* (since it's not a proper name); *We* to *we* (middle of a sentence).
4. Changed a few verbs to nouns, and vice versa: *"explain"* (on its own serves as an imperative, which would demand that the reader explain it) to *"explanation"*; *"storage"* to "store [the least editing distance of s1 and s2; L226]".
5. Fixed redundant spaces: *"[...] `s2`  in [...]"* to *"[...] `s2` in [...]"*; *"s1[i]！=s2[j]"* to *"s1[i] != s2[j]"*
6. Changed a few odd phrases: *"a violent solution"* to *"a brute force solution"* ( (most)[https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiolLjsxK3xAhUspIsKHU-9BwEQFjADegQIBBAD&url=https%3A%2F%2Fgsdrc.org%2Fwp-content%2Fuploads%2F2019%2F11%2F671_P-CVE_Programming_on_Men_Women_Boys_and_Girls.pdf&usg=AOvVaw2QjJ_-yjxxw2oWYtG77sgE], albeit (not all)[https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiolLjsxK3xAhUspIsKHU-9BwEQFjABegQIAhAE&url=https%3A%2F%2Fwww.programmersought.com%2Farticle%2F27011223160%2F&usg=AOvVaw1f6OCbf1r7M8GAfmGotBDg], uses of the former did not refer to programming ); *"from the bottom to up"* to *"from the bottom up"* (or *"bottom-up"*; see: (from the bottom up)[https://www.lexico.com/definition/from_the_bottom_up], and (bottom-up)[https://dictionary.cambridge.org/dictionary/english/bottom-up] ); *"operation number"* to *"the number of operations"* (this one might have been more subjective).
7. Removed latex dollar signs (since github markdown does not support it): *"$O(min(M, N))$"* to *"O(min(M, N))"* (as used in other articles).
8. Pluralized certain nouns after *"any"* ( ("We use any for indefinite quantities in questions and negative sentences")[https://dictionary.cambridge.org/grammar/british-grammar/any] ): *"any operation"* to *"any operations"*.
9. Added some formatting: "dp(i, j)" to "`dp(i, j)`" (L98).

I'm also not sure if *"[...] I wrote some words out of place by mistake"* refers to mistyping, but it's still more than clear, albeit slightly wordy.

To reiterate, should any of these be of concern, let me know, especially since it is my second language.
Best regards

---
## [frlegg/cosine-rule](https://github.com/frlegg/cosine-rule)@[d770b502b3...](https://github.com/frlegg/cosine-rule/commit/d770b502b3059c59db48f450f37090995dfae6b6)
#### Monday 2022-09-05 02:19:35 by frlegg

Created license for project.

Do what the fuck you want to.

---
## [vdbe/kubernetes-cluster](https://github.com/vdbe/kubernetes-cluster)@[9ee8433fa3...](https://github.com/vdbe/kubernetes-cluster/commit/9ee8433fa371b90ba75d2d5128cb1f514152c2fa)
#### Monday 2022-09-05 03:33:00 by ewoutvdb

This was painfull

Merge pull my finger request

Herping the derp

Revert "Herping the derp"

This reverts commit 5071e4d1bbeb9daf27f2ec0a27bc8b8465ce6227.

I must sleep... it's working... in just three hours...

harharhar

TDD: 1, Me: 0

I should get a raise for this.

Never gonna let you down

commit

Is there an achievement for this?

This bunny should be killed.

TOMEKWOJCIK, WE WENT OVER THIS. C++ IO SUCKS.

Revert "TOMEKWOJCIK, WE WENT OVER THIS. C++ IO SUCKS."

This reverts commit 1a32f61e2c6728c634594b5313d1753a3f2797ed.

I must have been drunk.

PEBKAC

Either Hot Shit or Total Bollocks

Fixed mispeling

tl;dr

oops

Update helm-release.yaml

clarify further the brokenness of C++. why the fuck are we using C++?

Corrected mistakes

Bit Bucket is down. What should I do now?

Fixed the fuck out of #48!

just trolling the repo

TODO: Fix later

Who knows...

forgot we're not using a smart language

bla

Finished fondling.

Revert "Finished fondling."

This reverts commit de1c5cbb8c0d5f93d3fec25f577c59ac64f94a37.

I __ a word

If it's hacky and you know it clap you hands (clap clap)!

Refactor factories, revisit visitors

fixed mistaken bug

The same thing we do every night, Pinky - try to take over the world!

Shit code!

ffs

I am Root. We are Root.

DAVID, WE WENT OVER THIS. C++ IO SUCKS.

permanent hack, do not revert

I should get a raise for this.

c&p fail

Revert "c&p fail"

This reverts commit ea0ff839d00fa3b2615a4fe44f9b819fe8c77851.

need another beer

Revert "need another beer"

This reverts commit 6b0d34b4a2712fd2a82434562706bcc4dd67f3f3.

extra debug for stuff module

Revert "extra debug for stuff module"

This reverts commit 053f752f98ef0c5f60acf32c30ac10d7a9b51fa8.

I was wrong...

yo recipes

fixed some minor stuff, might need some additional work.

I cannot believe that it took this long to write a test for this.

It was the best of times, it was the worst of times

did everything

To be honest, I do not quite remember everything I changed here today. But it is all good, I tell ya.

Herpderp, shoulda check if it does really compile.

Why The Fuck?

I have no idea what I'm doing here.

Working on WIP

Revert "Working on WIP"

This reverts commit a6f20fa5f799b9387df22c31a6f6a76748108ad9.

It's Working!

SHIT ===> GOLD

a few bits tried to escape, but we caught them

MOAR BIFURCATION

Never gonna give you up

syntax

Fixed Bug

Minor updates

Useful text

Revert "yo recipes"

This reverts commit 635bc68eb40682fe9b4eda9f463e32a730d0d437.

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[d92544282a...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/d92544282a977984973ab0019111afd8ba300955)
#### Monday 2022-09-05 07:50:00 by ODRI-the-human

lots of shit

- Barry 63 is now funnier than ever!
- Added new item (bleed), which makes it so your bullets have a chance to inflict bleed on enemies. With this addition comes the framework/UI for any other status effects I want to add.
- Changed soy and firerate up to stack linearly rather than exponentially.
- Shots spawned as a result of split shot now inheret your bullet effects. So it can now get fucking ridiculous with your split shots homing in on enemies, bouncing off them, etc.

---
## [swastik-college/free-programming-books](https://github.com/swastik-college/free-programming-books)@[97016edd67...](https://github.com/swastik-college/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Monday 2022-09-05 08:26:58 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [woodsts/linux-stable](https://github.com/woodsts/linux-stable)@[adee8f3082...](https://github.com/woodsts/linux-stable/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Monday 2022-09-05 08:31:51 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [facebook/react](https://github.com/facebook/react)@[b6978bc38f...](https://github.com/facebook/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Monday 2022-09-05 09:55:46 by Andrew Clark

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
## [martinezjavier/linux](https://github.com/martinezjavier/linux)@[4a557a5d1a...](https://github.com/martinezjavier/linux/commit/4a557a5d1a6145ea586dc9b17a9b4e5190c9c017)
#### Monday 2022-09-05 10:10:08 by Linus Torvalds

sparse: introduce conditional lock acquire function attribute

The kernel tends to try to avoid conditional locking semantics because
it makes it harder to think about and statically check locking rules,
but we do have a few fundamental locking primitives that take locks
conditionally - most obviously the 'trylock' functions.

That has always been a problem for 'sparse' checking for locking
imbalance, and we've had a special '__cond_lock()' macro that we've used
to let sparse know how the locking works:

    # define __cond_lock(x,c)        ((c) ? ({ __acquire(x); 1; }) : 0)

so that you can then use this to tell sparse that (for example) the
spinlock trylock macro ends up acquiring the lock when it succeeds, but
not when it fails:

    #define raw_spin_trylock(lock)  __cond_lock(lock, _raw_spin_trylock(lock))

and then sparse can follow along the locking rules when you have code like

        if (!spin_trylock(&dentry->d_lock))
                return LRU_SKIP;
	.. sparse sees that the lock is held here..
        spin_unlock(&dentry->d_lock);

and sparse ends up happy about the lock contexts.

However, this '__cond_lock()' use does result in very ugly header files,
and requires you to basically wrap the real function with that macro
that uses '__cond_lock'.  Which has made PeterZ NAK things that try to
fix sparse warnings over the years [1].

To solve this, there is now a very experimental patch to sparse that
basically does the exact same thing as '__cond_lock()' did, but using a
function attribute instead.  That seems to make PeterZ happy [2].

Note that this does not replace existing use of '__cond_lock()', but
only exposes the new proposed attribute and uses it for the previously
unannotated 'refcount_dec_and_lock()' family of functions.

For existing sparse installations, this will make no difference (a
negative output context was ignored), but if you have the experimental
sparse patch it will make sparse now understand code that uses those
functions, the same way '__cond_lock()' makes sparse understand the very
similar 'atomic_dec_and_lock()' uses that have the old '__cond_lock()'
annotations.

Note that in some cases this will silence existing context imbalance
warnings.  But in other cases it may end up exposing new sparse warnings
for code that sparse just didn't see the locking for at all before.

This is a trial, in other words.  I'd expect that if it ends up being
successful, and new sparse releases end up having this new attribute,
we'll migrate the old-style '__cond_lock()' users to use the new-style
'__cond_acquires' function attribute.

The actual experimental sparse patch was posted in [3].

Link: https://lore.kernel.org/all/20130930134434.GC12926@twins.programming.kicks-ass.net/ [1]
Link: https://lore.kernel.org/all/Yr60tWxN4P568x3W@worktop.programming.kicks-ass.net/ [2]
Link: https://lore.kernel.org/all/CAHk-=wjZfO9hGqJ2_hGQG3U_XzSh9_XaXze=HgPdvJbgrvASfA@mail.gmail.com/ [3]
Acked-by: Peter Zijlstra <peterz@infradead.org>
Cc: Alexander Aring <aahringo@redhat.com>
Cc: Luc Van Oostenryck <luc.vanoostenryck@gmail.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [owid/owid-static](https://github.com/owid/owid-static)@[8f07bb006e...](https://github.com/owid/owid-static/commit/8f07bb006eea6b323ea388292e87b392b83dd4f5)
#### Monday 2022-09-05 10:22:05 by owidbot

Deploy 2022-09-05T10:13:56.251Z
Updating chart female-and-male-life-expectancy-at-birth-in-years
Updating chart world-population-and-projected-growth-to-2100-by-age-group-young-vs-working-age
Updating chart world-population-and-projected-growth-to-2100-by-age-group-young-vs-working-age

Co-authored-by: Lucas Rodés-Guirao <lucas@ourworldindata.org>
Co-authored-by: Lucas Rodés-Guirao <lucas@ourworldindata.org>
Co-authored-by: Lucas Rodés-Guirao <lucas@ourworldindata.org>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a2f67c4c10...](https://github.com/mrakgr/The-Spiral-Language/commit/a2f67c4c107e9a42e79f448bc8723a43ab9b388e)
#### Monday 2022-09-05 10:52:50 by Marko Grdinić

"9:30am. I am up. Let me chill a bit and then I will get started. Actually, let me just start things off by posting 7b.

Note: I need to put in a loading blurb for ch 8.

9:40am. https://www.royalroad.com/fiction/57747/simulacrum-heavens-key/chapter/986985/chapter-7b-spark-of-success

Here it is. I only fixed a small typo in the author's note. Anyway, the number of views is 203 like it was yesterday. I'll see if it starts getting slower as I go along or speeding up. I published the first chapter 19 days ago, and posting a link on my Twitter which has 6 followers, and in the PL thread is all the advertizement it got.

It is basically nothing. I bet if it wasn't for this journal I wouldn't have even gotten this much. Some things are slow burn.

Every time I log into the gamesoftranscendi blog and check the dailies view, I see them being higher than before, though that is in 6 month gaps.

No matter what I need to keep going. This world is forcing me to be honest. It is not the same as in 2014. The years of programming have changed my mentality.

But at the same time, it is not like I have any way of being successful, so in the end, I just end up writing about what I want.

9:55am. Let me finish chilling and then I will get started.

10:20am. Let me watch the Witch of Mercury trailer and then I will get started.

https://www.tsungxu.com/performance-biomaterials/

I'll leave this link for later. I found it yesterday on HN, but haven't mustered up the nerve to read more than half of part 1. But what I've read was interesting.

$$$

(Heaven's Key, Heavenly realm)

Slowly, out of the pocket of his trenchcoat, the revolver came out. To my eyes, the movement seemed impossibly smooth and ethereal. I had a sense of time and could see exactly the trail the gun followed and as he raised it, where it would go. As if to draw out the tension, the white haired guy lifted the gun straight up, paused it a bit and then swung it down until it was pointed straight at me. He had a grin on his face. I perfect slow motion, I could see him put his finger on the trigger.

I knew what would happen next.

The last time I was here I got shot to death. This time, my mind is whirring a lot faster, so I even though I have a second in game time until the trigger gets squeezed, I have 27h to think about my next move. If this wasn't a game running at 10,000x speed, but the real world I'd have 30 years. Before I had started the game, the controller me did a memory merge, so I understood everything that I'd missed while I was crossing the Street. Right now I have the programming and the ML skills of the controller, and the optimized mind of the instance that beat the Street game, as well as the memories of both.

I understand what the controller wants, which is to beat this white haired dude with my newly found superintelligence.

But as I am staring down the barrel of the gun, I am really wondering what I could do here.

Make my body resistant to bullets? Make them phase through my body? Regenerate the wounds?

I am racking my brain here, but I don't know how to do this. I try to do an act of will here. I picture a rock in very vivid detail and try to manifest it in front of me. My mind is working too fast for the body to react, so I do not make any movements, but nonetheless I try to focus all of my mental abilities into making something happen.

...

As expected, nothing is happening. I do not know how the white haired dude is doing it, but there must be some other trick to it than just wanting magic to work really badly. Expanding my mind and speeding it up, didn't do much to change the situation from where I was a human. I am going to get a few new holes either way.

[Gnosis check DC 1.9 Succeeded - Sampled 2.76]

Imminent death facing me, I get a sudden burst of inspiration. I realize that if I just let things as they stand, I am just going to get shot like last time. It is inevitable. So I might as well quit the game now and go to an earlier save. There is no point in letting the events unfold. That much is obvious, but...is it really? I seriously consider eating a few bullets and then realize something.

Was I really killed last time?

This situation is just too weird. Last time I took it at face value, but it is strange that the game would allow one of the players to kill another. Last time, I just aborted the game due to shock once the darkness overtook me, but had I actually gotten a notification that I died from the game itself?

I do not think that happened. Did I abort the game too quickly to get that notice? Did I simply miss it in my panic? Or is there something deeper to this?

I can't help, but to loathe myself for what I am going to do, but let's eat a few bullets to make sure of what is going on.

Bang...

I put all my willpower into not escaping to an earlier state and let the lead object pierce my chest. Damn it, it hurts! Like last time, I look at it in horror, and on cue the white haired guy empties the rest of the magazine.

Bang...bang...bang...bang...bang...

The speed at which my mind works now really drew out the horror of this moment.

I sprawl out on the table, waiting for death to come to me. Like before, I can see my blood pooling out on the table until it covered my two face down cards. And then my vision became hazy and dark. Like last time, I couldn't make out what the white haired dude was saying. It felt distant...

Like that, I slipped into unconsciousness and death.

But...since this was a game, while it can simulate many things, it can't literally simulate the absence of life. Not without killing me in the real world as well. And now that I am keeping my emotions in order, I realize that despite being dead, I can still think just fine. I can't hear anything, I can't see anything, I can't touch anything. But my mind is working.

I feel out with my senses and I realize that I still have the connection with my chip pile. I wait a while in that senseless space, and there is no change. While I can't feel anything else, my life chips are still there. And I don't get a death notification from the game itself. Meaning, the game was still on.

Experiment - success!

I save the game here and exit it.

I should have noticed this last time, but that is the weakness of the mind controlling program that I used to get rid of my fear. It is one thing to be calm, but creativity requires an active and restless mind. It is easy to notice what is there when you are calm, but hard to notice what isn't. I guess that is the difference between what you need to be a member of society and what you need to conquer it.

(Heaven's Key, Inn room)

I go back to one of the earlier save states. This point in time is exactly the time before sliped out in secret out of my room through the window and explored the city. It was the dead of night and I wasn't tired enough to sleep, so that is why I did it. It was that time I met Mickey in the park of ghosts.

I remember what that translucent old ghost told me. That we are all holograms here. And the system is what determines what exists based on our inner state.

Right now I am sitting on my bed with the lights turned off in the room. I close the courtains and flip them on. Then I manifest a body sized mirror and sit in front of it, pondering.

I need to figure out the trick to becoming translucent. Mickey did it somehow and if I could do it as well, it would give me a hint for how to deal with bullets. I'll go about it scientifically. I do not really know how to trick the system into doing it, but it is not like I can't interface with it at all.

For example...I take out one of the chips, place it on the floor in front of me and using it as a focus, manifest a bottle of water.

Rather than asking how I should change my body, why not instead start by asking how I did this obvious bit of magic?

This gives me a lot of information about the system. It is commonly believed that VR works by hijacking your senses, but if it was just that, then how would movement work? Obviously it has to capture a lot more from the brain in order to be able to do those. But why stop there?

That I could manifest this bottle as I'd imagined it, that is proof that the system understand my desires... and in the dueling realms, it rejects them. Well, Mickey told me as much, but I am thinking things through and confirming them as I go along.

Then the next step would be, rather than just my desires, my true beliefs...

I spend a few minutes thinking about it from various angles.

Honestly, I have no idea how I'd do this if I were a human. If I were a human it'd literally be like trying to develop psychic powers. I'd have to try out all sorts of drugs in order to get something going, messing myself up in the process. Maybe get into the occult mindset. It is dumb.

But as I am now, the various perspectives are all converging to one conclussion. It should actually be pretty easy.

I have access to the entirety of my mind, and thought is merely the transfer of high dimensional vectors throughout the system. A small part of that data describes whether for example I am looking at a water bottle or just imagining a water bottle. It makes sense, otherwise I wouldn't be able to tell my own imagination and reality apart. This is a very good thing, since in the real world, the perception does not affect reality, but here the system is literally basing a part of it on what it sees in my mind.

So if I mess with those thought vectors and conventiently erase the part of the data that tells me what the imagination is, I should make my first step on becoming a reality warper.

Doing this unhindered is dangerous as I'd completely lose track of what is real and isn't.

I understand where things are going with this though. If I could make it safe, I would receive a strong power. Right now even though I've increased my intelligence significantly, my emotional system is still that of a human. When I lost to the white haired guy the first time, I swore that I'd challenge him as a player, not as a character in a game.

This capability of tricking myself to think my imagination is reality should not be in my own hands, but the player's. But there is no reason why I couldn't automate the process eventually. It is like how computer programs become a part of you once you get rid of the interface obstructions, one day the player and the character might be one. Furthermore, now that I've moved from the human model of cognition to my own streamlined one, the tool I was using to regulate my emotions before has become unusable. I need to recover its capabilities by making my own.

I am still a beginner, my capability is nowhere near close enough to the person who made this game. The game is here to teach me.

Anyway, what I have to do is straightforward now that I've planned it out. The first thing I have to get out of the way is the player. The one who is currently supervising me is no good. I need him to have at least my level of capability otherwise he won't be able to keep up.

I really need the controller to help me in this because my own measure of what is sane and isn't will become distorted once I start relying on this power, and I don't mean that in the based, anti-normie way.

I need to account for any and all risks.

Having made my decision, I open up a text editor and compose a message to the controller. After that I save the game, and as a show of will, I terminate my own process.

(Helix Studio, Regent Suite, Bedroom)

I was using the emotion controlling tool to keep my focus up, so I was in fact paying attention to what was going on. Still, it is not like I can read my other self's thoughts. So far, I saw him get shot by the white haired guy, reload back a week ago, and then spend a few minutes staring at himself in the mirror. Then he terminated himself, which shocked me enough to curse. I was really perplexed as to what was going on and started thinking that something might have gone wrong in the optimization process to make him mentally unstable. My thoughts went in that direction for a few seconds and then I realized I got a message from him.

> Subject: Self-Improvement Step Request

What followed is a report by him that went into great detail regarding his thinking since he started the game. It hadn't even occured to me to think about that he deliberated whether to load back right away or get shot purposely. It went on for couple of pages and by the end I got the gist of what he wanted to develop and why he wanted to replace me with somebody more fitting.

> You won't be able to keep up, I need somebody more fitting for the role.

He literally said as much directly to me. Sigh. I didn't think my turn would come so quickly. I've been expecting him to challenge Lily's group without relying on saveloading and was looking forward to seeing how he does it, but it seems a lot of action has happened in his head that I've been unaware of.

...It is just too soon, so let me compromise. The report he wrote demonstrated his intelligence to me, so I no longer have any doubts about him broken in some way. But nonetheless, I want to see him in action before I just hand him the reigns to everything. If something goes wrong, who is going to take the responsibility of explaining that to the main me who is currently sleeping in the real world?

Maybe the role of the controller is too much, but I need to spend a while observing. So I'll do that.

I copy his paused process and do a memory merge. Then I make the necessary setup and start him in a different Helix Studio limbo. Now he should have what he needs to act as a controller. He'll be able to fork himself and start the game.

If this was a real self-improvement step, I'd erase myself here, but I am not going to do that, not yet. He is asking me to literally kill myself for him, so it is fair that I take some time to observe before deciding if I want to go forth with it. The report he sent me was pretty interesting. I'll have him do a writeup at the end of every day. At his speed of thought it shouldn't take him more than a few seconds, and it really gives me an insight into what is going on.

(Helix Studio, Skylark Island)

> Hello, welcome to the Skylark Island. Whereas most character limbos tend to be obvious, this one is heavily inspired by the Simulacrum scenario Wordly Abyss, and it is magic based. In order to acclimate the host, the tutorial messages will show up as you explore the areas. For now, keep in mind that you can access the spell list whenever you wish for it.

Before I copied myself, I wasn't aware of what I would pick, so this limbo is new to me. I remmeber seeing it in passing during past selections. The controller me picked something weird this time. I guess he didn't want to duplicate the Regent Suite.

This place was interesting, it was like a cottage made of wood. There was a table, chairs for it. It wasn't too big, certainly smaller than the Regent Suite. But whereas regular wood cottage were made of modular wood planks and boards, walls, the floors, and the ceiling and indeed the furniture seems to be made of composite wood, as if it were grown. It was how I'd imagine a fantasy druid would build it. He wouldn't use saws and nails, but magic to guide nature into the shape he desired. Looking behind me, I realize what I see is a bed.

It isn't really obvious at first glance, as it looked like some furry, green plant. It had some oversized leaves that felt like animal fur to my touch and bended flexibly as I'd moved it. The pillows were some kind of membranes and I could see liquid inside. I poke it a bit and realize that while it is flexible, it is also tough and wouldn't burst easily. It felt smooth to the touch. I tried the bed out a bit and found that it felt comfortable to rest here.

I like this place. As I walked, I noted than unlike the regular floor, this one was a slightly uneven due to being bark. My first thought that this would make it difficult to position furniture, but when I tried out the chair and sat on it, I found that it had a bit of springiness, that ensured its seat was always balanced horizontally.

The table itself, unlike the floor was made of smooth polished wood. I brushed my hand along its surface, liking how it feels.

This is a really nice feeling of adventure. It is like being a child during its first days in the world.

I take a look at the windows from my sets in the middle of the room, and realize that instead of glass, they seemed to be some kind of translucent membrane. I come up to it, touch it a bit, push it and note how flexible it is. I give it a punch. My fist sinks into it, but the membrane does not tear, instead it bounces me backwards and comes into the original straight position. I approve, it feels reliable as a window.

Looking through the window I realize that the place I am in is quite high up. My cotage in particular is high in the island, but beyond the island it feels like it is a very deep drop given how high it is. It reminds me looking over the edge of the city in Heaven's Key, though not quite that high. In the distance I can see the sea, the mountains and the forests. Sunlight gleams off it, and I get the impression of looking at another natural wonder.

In the minds of people, when people think of techology, they think of steel and concrete. Cars, robots, machines. Guns, tanks, airplanes. Skyscrappers.

But maybe that is wrong. They haven't realized it yet, but maybe the true form of techology is celestial in nature. These simulated worlds. Can breathtaking wonders that I've seen, and the powers that I am trying to attain be anything other than divine?

The brain cores that I've gotten are supposedly mostly made of carbon. Experiencing them from the inside, they don't feel technological in nature at all.

I brush away these thoughts and come to the door. It doesn't have a handle, but two wooden hook on the side. I detatch them and the door slides inward as it were a measuring tape. Like the windows, it the door was made of sturdy and flexible biological material that looked like wood, but was more like plant matter that I'd guess doesn't exist in the real world.

I poke my head outside and realize there is a huge drop below. As I imagine splattering myself below, I get a sense of vertigo and take a step backward.

> If you want to exit the building to explore the rest of the island, please use the Wings spell.

I get a helpful notification and do as instructed. As I do some large fairy wings manifest themselves on my back, and my body feels weightless. This reminds me of being a disembodied entity in the Heaven's Key title menu, and I find that it is much the same. Rather than having to beat them against the air to take flight, they are more like an antigravity device attached to my back.

I have no trouble controlling my flight and exit the room to explore the island beyond.

I spend some time playing like that and then I create a fork of myself and plug it into the game.

(Heaven's Key, Inn room)

"I am visualizing my hands at twice their usual size. How are my recordings?" I ask the controller back at the the Skylark Island.

Back in the game, I am seated in front of the big mirror. I have my hands raised in front. I think it is due to the latest batch of improvements, but my imagination is very vivid compared to before. I can almost see my enlarged hands overlaid over my regular ones as if they were real. No amount of desiring they are real will be enough to make it so. instead the controller me has to be the one to make the step. While I am focusing on visualization, right now he shuold be looking directly at my brain studying the neural messaging as it occurs.

"I've recorded it, but it is a bit hard. Instead try imagining yourself pinching your hand." I do as instructed.

"Good, now actually pinch yourself lightly." I do it just enough to be a bit painful.

"I see it. Now relax. Don't try to think of anything." I do so. What happens next is that I get a bizzare feeling of having my hand in front of me and pinching it with the other. It feels a bit dissonant, but eventually that fixes itself by me focusing on it. Just like before, I seem to be imagining pinching myself, but there is an obsessive streak to it. I am finding it difficult to focus on anything else. After a bit I get relieved.

"Good. I've aborted the program, how is your mental state?" He messages me.

"I seem to be fine." I reply. "The obsession is gone."

"Is that how it feels like? Anyway, I'll try the actual pinching next."

"Ah!" Feeling being pinched, I raise my hand to look at it. I expected to see some pain, but I am surprised to see that my skin is physically twisted. It is as if an invisble hand was pinching it. I try to relax the skin with my other hand, but it does not help. The feeling of my skin being pulled remains and after I remove it, I see the pinching fold again. "Are you seeing this?" I show it triumphantly.

"It is a success! I think I understand this. Let's try the hands again. This is like hacking memory states to cheat in games. Focus on the hands and I'll try edit the relevant thought vectors based on the previous recording. I don't want to make everything real."

I raised my hands in front of me and focus, imagining them to be oversized. As I do so something in me shifts, and to my surprise, it works. What was once imagination turns into reality. I clench and unclench them, marveling at the unfamiliar sensations. I try using them to lift the water bottle and unscrew the bottle. It feels so weird, but they aren't clumsy. I take a gulp, and screw the cap back on.

"This is pretty cool." I show of my hands in front of me. The controller can't see or feel anything my senses can't. He doesn't have direct access to them through his own mind, instead he is looking at what I am seeing through the screen. Eventually what we have planned is to integrate the rest of the senses into him, so he can feel directly what I feel through separate neural channels. If the controller had that kind of ability, it would make his work a lot easier. At the end of that road, what the controller will become is a higher order consciousness for myself, able to control me as I would a video game character.

At that point, we'll be able to do these transformations instinctively. For now...

"This is cool, but let's turn them back. I'll imagine them being normal. You do your thing." I message him.

I look at my hands and imagine them being as same as before. As I watch, I again get that strange impulse like a gear in my head has skipped a turn and the hands transform back into their previous shape. I flex them to test them out and satisfied, I let out a breath.

"Phew. We've got it!"

That white hair dude is going to get what is coming to him. Right now I could go back to that dead end, and try to resurrect myself. Except, it is one thing to imagine my hands changing shape, but quite another to imagine having a living body. I am getting to ahead of myself. We did just the very first step. The program we have is not capable of flexible whole-identity transformations. We should challenge him when we are ready.

Right now, how about we beat on some noobs?

I think back to Lily and Dale's group.

They are the ideal testing ground to develop our skills at programming the language of the mind.

Back then I just scammed them out of a ton of chips, but then they sent the tough white haired guy after me. This time I am not going to do it using saveloading, but with my own skills. Maybe if I did it that way, something different will happen.

Me and the controller burned the candle late into the night, creating some simple cheating methods and trying out what we would call the True Belief Modification. It wasn't until later that we realize that the method we invented was the legendary hallmark of the stories of the Inspired. Their titular ability was called the Inspired Desire. This was its embryonic form.

(Heaven's Key, Raven's Eye Casino, Shadow realm)

"Fold." On the small button, Lily folded.
"Check." The thin guy who has been looking down on me, follows up.
"Fold."
"Fold." The two guys behind me toss away their cards.
"Call." I limp into the pot. I look to my left, and see Dale deliberating. He raises from 4 to 12. I look at his face down card, and mased on the red markings, I note that he has suited AhTh.

My own hand is crap, an unsuited Jd 7h. To Dale's left, the thin guy thinks for a bit and folds. Unlike Dale's card, only one of his cards had a marking. Even though my hand is weaker than Dale's, since I know what he is holding it is hugely beneficial to enter the pot regardless, so I call.

The flop manifests.

Ks Qc Tc.

There is a flush draw on this board, but Dale has hearts rather than clubs. He hit a low pair. A very dangerous flop for him. I do not hesitate and lead out by betting 20 into the pot. Dale hesitates and stupidly makes a call, bringing it up to 70.

On the turn, 5c comes out. Not hesitating, I shove my entire pile and go all in.

Dale stares at me for a while, trying to read my mind.

"Fold." He makes the sensible decision, and I increase my pile by 38 chips.

In this hand, I happened to have a straight draw, but I'd have played it the same way regardless of what I was holding.

The hands we are holding get purged, and the next round starts promptly. I get dealt two cards, and luckily, they don't have markings on them. I check my hand to see what it is, 2d 9c, and silently message the controller.

> Manifest the UV pigment on my fingertips.

I feel the familiar feel of something skipping in my brain and with a light touch put two marks in the right places. With a light brush, as I move the cards, I make two angular lines at 30-60 degree angle to either of the edges. That way if the card is rotated, I won't be confused as to which is the rank and which is the suit marking.

As I look at the group, each them is covered in a film of blue, or more more to the point, my entire vision is that way. I've modified my eyes so I am capable of seeing in UV. It wasn't too difficult, it used to be the case that laser surgery of cataract got rid of the membrane protecting the lens, which allowed the patients to see UV. I had to study the structure of the eyeball for a while, but after that I modified my true belief to change the structure and got the ability to see in UV. After that it was just a matter of doing research on pigments and finding the right one.

Thanks to this cheating method, I can take it easy during the first few revolutions, just marking cards and only playing strong preflop hands. After that once the blinds go up, I can loosen and jump into the fray to land a sneak attack.

A few days ago, I started the matched at 240 chips, and now I am up to 600. My winnings are a lot slower than when I was saveloading, but I am really happy regardless. This is real power! I worked hard to get to this point and my reward is that now I can beat these people. It might be possible to use something like this in real life, but the method is too unrefined and would easily be found out in a casino. Here I have my improved eyes, and can manifest the pigment directly on my fingers. If I had to carry around a can of it in my pocket, it would quickly get spend. Moreover, I wouldn't want to damage my eyes just to cheat at cards. My vision might be crap so there is no need to make it even worse. But if I came to the table wearing fancy UV glasses, it would raise some eyebrows.

Using this method in reality is beneath me. I have much better things planned.

Anyway, I continue playing and notice that things are moving quicker this time. Whereas before the party tried really hard to bust me, now that I am winning using what looks like actual good play, the party is close to breaking. I can tell that the others are hesitating and exhanging looks when I propose duels.

A few days earlier than last time, Lily doesn't arrive and her place is instead taken by an old guy named Geoffrey.

After a few games with him, I get the sense that rather than focusing on winning, he is instead watching me like a hawk, not really caring about any of the other players. He radiates an aura as if he is preparing to strike me, but nothing happens and I just end up making some money off him. This is fine, I guess.

(Report by Geoffrey to the Enforcement Department)

Subject: Aleator-level enforcement request

One of the newcomers from about a week ago is currently in possession of 680 chips. I've played him personally, and in my estimation, he is at least a low ranked Aleator who possesses the ability to mark cards. He employs a strategy of playing strong hands at the start, and once the cards have been marked, he loosens up and picks the other players off. He has decent gameplaying skills from what I've observed even without the use of cheats.

We've done extensive background checking and confirmed that he is a newcomer, he should be easy prey for an experienced Aleator.

In the attachments are the report I received from my subordinate guide as well as my own. The reports have extensive recordings of our games with him.

(Heaven's Key, Streets)

Night comes, I go back to the inn, and then once the morning gets around it is time for action again.

The next day I play with Dale's group again, but they've started to clam up. Once I realize that I switch to bluffing more often and take the money off them that way. I was uncomfortable of going all out, but the controller did some modifications and spiked my confidence, allowing me to execute the strategy properly. I blitzed the table, and it felt good picking on those weakling with my strong bets. Hell, yeah!

That day, as the sun was falling beyond the horizon in the background, I exit the casino in high spirits, swinging a pair of big ones.

> Be on guard. I think that guy Geoffrey was responsible for sending that white haired guy after us last time.

I get a message from the controller. We are a dream team, me and him. My own skill at both manifesting my imagination and poker is growing, while on his own end, I can sense he is getting new insights about the mind. We've already recovered a lot of the functionality of the mind controlling app over the last week.

Doing as he instructed, I unwind a bit and take note of the surroundings. Gleaming golden buildings enter my attention. The rays the light look quite beautiful at this time of day, painting the town in a crimson tint. The work day is starting to wind down and I can see people returning to their places. The usual boisterous atmosphere of the golden city is starting to quiet. Compared to the real world, where you usually have some insects chirping at night, when it gets quiet here, it becomes deathly quiet.

As I walk the streets, the previous scenario repeats itself. Not the white haired guy, but some other one walks around the corner and moves straight towards me, looking me straight in the eyes like he wants to kill.

Bang!

(Heaven's Key, Shadow realm)

After the bullet was fired from a gun, I find myself in the familiar duel space. Looking around, I am surprised that the background is the familiar deep space with bluish nebulas. I thought that resolution matches would be different, but maybe the reason for the background change last time was different. I take a good look at my assailant. Unlike the white haired guy, I am not going to let this guy off. I am going to send him straight to the grave. I am going to kill for the first time.

As I think that, my killing intent surges. Forget those tiny duels against Dale's group. This is what a real match should feel like.

My chips here are my life and blood. Even if I beg, the assassin is not going to let me off. There is only way to survive, and that is to kill him first.

...

$$$

12:45pm. Let me have breakfast here. I need to figure out how to describe the guy. I am not good at these textural descriptions.

How much have I written, it doesn't feel like much?

5.7k. About 1.4k words. It is not too bad.

12:50pm. I added another few lines. Let me stop here.

Note: I forgot the damn loading blurb."

---
## [osama2000418/-](https://github.com/osama2000418/-)@[8e6636dadd...](https://github.com/osama2000418/-/commit/8e6636dadde750400d8a1291ebd4c0d6c27713f5)
#### Monday 2022-09-05 11:13:19 by osama2000418

Update README.md

1
00:00:00,000 --> 00:00:02,500
[Music playing]

2
00:00:03,000 --> 00:00:09,500
[Dan] On a tropical hillside of
Puerta Plata, Dominican 
Republic lies the Residence 
Suites at Lifestyle Holidays 

3
00:00:10,000 --> 00:00:11,000
Vacation Club Resort.

4
00:00:12,000 --> 00:00:20,000
Designed in a contemporary
Spanish style, the Residence 
Suites is a relaxing year-round
Caribbean retreat offering one

5
00:00:20,500 --> 00:00:23,500
and two-bedroom luxury 
accommodations. 

6
00:00:25,000 --> 00:00:29,000
Every Residence features king-
size beds and a private
bathroom. 

7
00:00:30,000 --> 00:00:36,000
Enjoy a spacious living room
with comfortable furnishings,
a dining area and kitchenette. 

8
00:00:37,000 --> 00:00:43,000
Beautiful balcony views 
surround your Residence with
the ocean and beach within
walking distance.

9
00:00:46,000 --> 00:00:52,000
[Eddie] Everybody is very nice.
They greet us with open arms.
The scenery is beautiful. It’s a
very exciting experience to 

10
00:00:52,500 --> 00:00:55,000
come here and be treated 
like that so quickly.

11
00:01:02,500 --> 00:01:09,000
[Dan] Lifestyle Holidays 
Vacation Club Resorts brings
an all-inclusive stay which 
features six onsite restaurants

12
00:01:09,500 --> 00:01:16,500
including Asian, Italian,
Mexican, seafood and steak as
well as an international buffet
and gourmet restaurant. 

13
00:01:17,000 --> 00:01:24,000
[Thomas] The highlight of my 
stay has definitely been all-
inclusive, all you can eat, any
time I feel. All you can drink.

14
00:01:24,500 --> 00:01:31,000
And it’s fully-furnished, good
air conditioning. You know it’s
been real comfortable and 
relaxing for myself and the 
family.

15
00:01:33,500 --> 00:01:39,000
[Dan] Lush landscape and 
walkways create attractive
surroundings at the resort.
Three large swimming pools

16
00:01:39,500 --> 00:01:44,000
complete with swim-up bars
are only steps away from the
accommodations and the 
beach.

17
00:01:44,500 --> 00:01:50,000
where golden sand and ocean
breezes help define this 
beautiful getaway paradise.

18
00:01:57,000 --> 00:01:59,500
[Eddie] Everything has been 
good, the service here, 
everybody does everything 
with a smile.

19
00:02:00,000 --> 00:02:06,000
They want to help you as
much as possible. It’s not 
something that they need to 
do here I think. 

20
00:02:06,500 --> 00:02:11,500
It’s something they want to do.
They step up to and make sure
everything is going all right 
for everybody. 

21
00:02:16,500 --> 00:02:24,000
[Dan] Other favorite features
include a fully-equipped fitness
center, tennis courts and even
an onsite full-service spa

22
00:02:24,500 --> 00:02:29,500
where guests can indulge in
an expert massage and other
pampering experiences.

23
00:02:31,000 --> 00:02:37,500
For more outdoor fun, explore
the nearby mountains on 
horseback, take the fast track
with a fun and crazy banana 

24
00:02:38,000 --> 00:02:46,000
boat ride in perfect Caribbean
waters. Or how about a wild
sea life encounter right next
door at Ocean World.

25
00:02:47,000 --> 00:02:54,500
Every Thursday night is a VIP
party and exciting performance
show and every Sunday night
is a VIP welcome party for 

26
00:02:55,000 --> 00:02:57,000
special guests on the 
peninsula. 

27
00:02:58,000 --> 00:03:04,000
[Thomas] Folks down in the
Dominican Republic have been
excellent service and it’s a warm,
like family environment actually.

28
00:03:04,500 --> 00:03:10,000
Everybody just wants to cater
anything I need, all the way 
down to the baby, you know?
So it’s been a wonderful stay.

29
00:03:15,500 --> 00:03:18,500
[Sound of fireworks]

30
00:03:22,000 --> 00:03:31,000
[Dan] So, come, and relax. 
Enjoy perfect accommodations
and a tropical island paradise
at the Residences at Lifestyle

31
00:03:31,500 --> 00:03:33,000
Holidays Vacation Club Resort. 

32
00:03:33,500 --> 00:03:46,000
[Music playing, fades]

33
00:03:57,000 --> 00:04:04,000
[Fatima] The Residence Suites 
are spacious one or two-
bedroom suites with one or two
bathrooms with a very nice 

34
00:04:04,500 --> 00:04:12,000
balcony with different views,
some of them ocean views,
other ones are views to the
nice gardens, the nice tropical

35
00:04:12,500 --> 00:04:19,500
gardens of the Dominican 
Republic. What is unique about 
the Residence Suites is that it’s
perfect for families. 

36
00:04:20,000 --> 00:04:28,000
Perfect if you just want to relax
from your stressful days, you’re
located in spacious apartments.
You have your own pool right
there.

37
00:04:28,500 --> 00:04:34,500
We have [inaudible] pool at 
the Residence Suites plus a
children’s pool if you’re with
children.

38
00:04:35,000 --> 00:04:44,500
If you want to, you can go and
enjoy the activities at the main
resort. So you can choose
between relaxing or activities

39
00:04:45,000 --> 00:04:46,000
whenever you want to.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[226efcd9cc...](https://github.com/wrye-bash/wrye-bash/commit/226efcd9ccbcc1499a5cd37d60da31488a099e3f)
#### Monday 2022-09-05 13:08:04 by Infernio

Rework the Mods tab's context menu

You now what really doesn't help the first time user experience?
Throwing a giant context menu in their face. Sometimes people report
they can't find the Rebuild Patch option even though it's right there -
almost certainly because in order to find it, their eyes have to scan
through up to *twenty-eight* menu items.

This commit brings a similar refactoring to what we did to the
Installers tab to the Mods tab as well. There are now only twelve
top-level items, exposing the most commonly used features (e.g. Rebuild
Patch, Move to, Jump to Installer, etc.) at the top level and placing
the less commonly used features in sub-menus (Info and Plugin, in this
case - plus an Advanced menu for the weird shit:tm:).

Note 'Export Patch Configuration' getting dropped entirely - you can
already do that via Rebuild Patch... > Export, plus it was confusing
that you could export like this but not *import* that way. And on top of
all that, it would have lead to unintuitive UI with the new context
menu, since I would have either had to move it to Plugin.. or kept such
a rarely used command at top level.

Didn't update the docs for this because they also haven't been updated
for the latest Installers changes yet and I want to do all that in one
go with updated images and all.

Closes #643

---
## [Jupiterson/Throne-of-Lorraine](https://github.com/Jupiterson/Throne-of-Lorraine)@[a7b24ffea1...](https://github.com/Jupiterson/Throne-of-Lorraine/commit/a7b24ffea10c16d695b2899b3dd529bed91570fa)
#### Monday 2022-09-05 15:40:27 by WelshSlateMiner

Merge pull request #112 from WelshSlateMiner/AIDs

GO FUCK YOURSELF LOCALISZTION ASS CHEEK

---
## [harryob/Foundation-19](https://github.com/harryob/Foundation-19)@[6bf6cdb77f...](https://github.com/harryob/Foundation-19/commit/6bf6cdb77f582598b90e63fa44a922fd033ae3d0)
#### Monday 2022-09-05 15:50:48 by harry

fixes panic bunker adjacent shitcode (#769)

* ugly as hell

* idiot

* think before i commit (never)

---
## [vgstation-coders/vgstation13](https://github.com/vgstation-coders/vgstation13)@[496d3bb777...](https://github.com/vgstation-coders/vgstation13/commit/496d3bb777d9538dd05b57d9a042acffd6496741)
#### Monday 2022-09-05 16:13:54 by ValkyrieSkies

Med/Sci mapping changes on Metaclub, also Bridge lightswitch (#33197)

* Metaclub Science Improvements

* Feature creep

* Fixes the god awful bridge wallpipes

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[cb4aae8406...](https://github.com/mrakgr/The-Spiral-Language/commit/cb4aae84069de44ed4b006030bf9ed5f09b760a2)
#### Monday 2022-09-05 16:28:17 by Marko Grdinić

"1:55pm. I want to resume, but I realized an issue, and I am thinking about how to deal with it.

2:10pm. Let me finish what I am reading and then I will resume.

3:30pm. I am still thinking about it.

3:35pm. Let me take a nap.

5:35pm. Mhhh, I am still thinking about it.

6pm. I am still thinking about it. I think I am starting to grasp the feeling. The way I originally imagined the city battles is for them to be will based. I do not want Euclid to trivialize them by just going to a higher tech level. I've sort of been going in this direction, and am gradually losing track of things.

Anyway this tension is reaching its apex in this battle, but I know how to deal with it. I need to borrow some spirit from 2014.

6:25pm. Just what are my plans? To hell with them. If Heaven's Key turns out shorter than expected, then so be it. I can't really tell how long it will be if I start ramping up the pace. Maybe it will be quite long.

I'll have lunch here. Tomorrow I'll focus on implementing, I mean, writing down my ideas."

---
## [ChoGGi/SurvivingMars_CheatMods](https://github.com/ChoGGi/SurvivingMars_CheatMods)@[0ea11aff73...](https://github.com/ChoGGi/SurvivingMars_CheatMods/commit/0ea11aff733d5c3e346bb6e9abba41615f9edde9)
#### Monday 2022-09-05 16:40:21 by ChoGGi

Mods:

Game Rule Amazonian Mars 0.4:
More validation before culling.
Cleaned up some code.
v0.3
Fixes rocket crash?
v0.2
Added mod option for male model size.
Was culling too many male colonists.
Challenge rating is 301.

RC Driller Cheats 0.6:
Added mod option No Waste Rock.
Checks for auto-mode tech.

Rocket Show Hours Remaining 0.7:
Ok, proper mod options now.

The Parish Boy's Progress 0.3:
Picard update...

github@choggi.org

---
## [divagant-martian/lighthouse](https://github.com/divagant-martian/lighthouse)@[66eca1a882...](https://github.com/divagant-martian/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Monday 2022-09-05 17:06:05 by Michael Sproul

Refactor op pool for speed and correctness (#3312)

## Proposed Changes

This PR has two aims: to speed up attestation packing in the op pool, and to fix bugs in the verification of attester slashings, proposer slashings and voluntary exits. The changes are bundled into a single database schema upgrade (v12).

Attestation packing is sped up by removing several inefficiencies: 

- No more recalculation of `attesting_indices` during packing.
- No (unnecessary) examination of the `ParticipationFlags`: a bitfield suffices. See `RewardCache`.
- No re-checking of attestation validity during packing: the `AttestationMap` provides attestations which are "correct by construction" (I have checked this using Hydra).
- No SSZ re-serialization for the clunky `AttestationId` type (it can be removed in a future release).

So far the speed-up seems to be roughly 2-10x, from 500ms down to 50-100ms.

Verification of attester slashings, proposer slashings and voluntary exits is fixed by:

- Tracking the `ForkVersion`s that were used to verify each message inside the `SigVerifiedOp`. This allows us to quickly re-verify that they match the head state's opinion of what the `ForkVersion` should be at the epoch(s) relevant to the message.
- Storing the `SigVerifiedOp` on disk rather than the raw operation. This allows us to continue track the fork versions after a reboot.

This is mostly contained in this commit 52bb1840ae5c4356a8fc3a51e5df23ed65ed2c7f.

## Additional Info

The schema upgrade uses the justified state to re-verify attestations and compute `attesting_indices` for them. It will drop any attestations that fail to verify, by the logic that attestations are most valuable in the few slots after they're observed, and are probably stale and useless by the time a node restarts. Exits and proposer slashings and similarly re-verified to obtain `SigVerifiedOp`s.

This PR contains a runtime killswitch `--paranoid-block-proposal` which opts out of all the optimisations in favour of closely verifying every included message. Although I'm quite sure that the optimisations are correct this flag could be useful in the event of an unforeseen emergency.

Finally, you might notice that the `RewardCache` appears quite useless in its current form because it is only updated on the hot-path immediately before proposal. My hope is that in future we can shift calls to `RewardCache::update` into the background, e.g. while performing the state advance. It is also forward-looking to `tree-states` compatibility, where iterating and indexing `state.{previous,current}_epoch_participation` is expensive and needs to be minimised.

---
## [Tejaswini283/Zonal-Accident-Prediction-system](https://github.com/Tejaswini283/Zonal-Accident-Prediction-system)@[38087bd5e0...](https://github.com/Tejaswini283/Zonal-Accident-Prediction-system/commit/38087bd5e003d74baa3693f3e8cde4f6c4b5d578)
#### Monday 2022-09-05 17:56:41 by Tejaswini Parlapalli

Add files via upload

Introduction 
What was once a groundbreaking discovery for everyday convenience, has now become a major 
death  cause.  The  total  number  of  vehicles  has  immensely  increased  over  a  span  of  a few  years,  thereby 
increasing the deaths per year rates, both nationally and internationally. 
 
It is estimated that road accidents cause 1.3 million people deaths each year. On average, almost 
3,700 people are killed globally. Vehicular crashes are one of the main reasons for deaths other than natural 
deaths. People across the globe, experience huge losses of friends, family members and loved ones due to 
this and despite multiple organizations, governments trying to reduce these accidents issue seems to be ever 
evolving and deeper. While certain reasons like drunk driving, rash driving, etc. have a whole new set of 
probable solutions, we wanted to figure out if there were any common patterns or features that might also 
contribute  to  the  increase  in  accidents.  While  major  preventive  measures  revolve  around  increasing 
awareness  and  a  general  change  in  traffic  culture,  we  believe  an  overview  of  some  of  the  most  notable 
features regarding accidents such as the ones here may bring about a positive effect. The whole idea behind 
the project is to reduce the number of accidents by implementing possible safety measures. For example, 
by knowing the postal codes, and road types with the most accidents, implementing new road systems and 
additional stop signs could save lives. 
Data Description 
We sourced  the  accident risk  data  with various important features  from Kaggle  by Gaurav datta 
site. The data contained 5 csv files as in below, the main csv files test and train datasets contain 30 MB and 
120  MB  of  data  respectively.  The  dataset  in brief has records  of  occurrences  of  75864  road  accidents  in 
8035  postal  codes  (UK)  with  multiple  features  like  zonal  codes,  time,  day  weather  conditions,  road 
conditions, type of road, deaths caused, casualties, etc. The largest table is the observation table which has 
over a million rows and 49772 unique postal code entries. This dataset is well suited for cloud computing 
because of its large size, and the need for data transformation. 
List of files in the dataset: 
• Population.csv 
• Roads_network.csv 
• Sample_submission.csv 
Zonal Accident Risk Prediction 
 
2 
 
• test.csv 
• Train.csv 
Methodology 
Environment Setup 
Google Drive & Colab 
Google colab was set up using personal google account and data files were imported into drive of 
the same account.  
Spark Installation 
Spark was used in google colab for our project and simultaneously Jupyter Notebook is used. Few 
engines were not found on the google colab to run codes. Pip install is used to install necessary packages.  
PySpark & Python Modules 
PySpark modules which are necessary for model building and analysis are pyspark.sql, 
SparkSession, pyspark.ml.classifications, pyspark.ml.regression, pyspark.sql.functions, pyspark.sql.types, 
SQLContext, sklearn.preprocessing, sklearn.model_selection. The Python modules that are required are os, 
random, and pandas. 
Exploratory Data Analysis 
Our goal during EDA is to develop an understanding of the data and to develop questions, insights 
that can help us reach our goal of finding out common patterns in data to reduce accidents. We investigated 
the quality of our data, and the dataset had a good amount of data, but we observed some rows containing 
empty entries on multiple columns and hence had to be dropped to maintain consistency in data. The data 
set has 27 columns with various features relating to accidents. 
Data Cleaning 
Once the libraries have been imported and the dataset has been loaded, we started to remove the 
rows with the no values using spark, once our dataset is cleaned of all the null values, we replaced missing 
values of other columns finally getting a clean dataset. 
Then we converted the datatypes of our dataset which had a huge number of columns in string type 
objects to integer type for calculation purposes. 
Answering Research Questions 
As  a  part  of  the  project,  we  wanted  to  answer  few  research  questions  based  on  the  data  and 
predictors available. First question is to know which postal codes have experienced the highest number of 
accidents  with  number  of  fatalities  occurred  in  those  postal  codes  and  understand  what  the  road  types 
Sunandan Chakraborty
This is not EDA. This more about understanding the data quality. EDA is about getting high level insights that should help in the subsequent analysis phase
[...]
Zonal Accident Risk Prediction 
 
3 
 
available and their respective speed limits are? Second question we answered is to understand if there is 
any effect of day of week effects on occurrence of accidents?  
 Initially  a  temporary  table  is  created  to  store  the  data  frame  and  this  temporary  table  is  used  in 
Spark SQL queries to get back the data from data frame and received the expected outputs. To answer the 
first  question  number  of  repetitions  of  postal codes  in  accident  data  is  calculated  and  sum  of  respective 
number of casualties in those postal codes is displayed. Second question is answered like the first question 
by calculating the repetition of accidents on each day where 1 represents the Monday and 7 represents the 
Sunday. 
Model building 
To build a model on a data frame which is a combination of test and train csv files to build a model 
and  selected  few  predictors  from  all  available  predictors,  those  predictors  are  police  force,  number  of 
vehicles involved in accident, day of the week on which accident occurred, number of casualties involved 
in  an  accident,  urban  or  rural  area.  Predictors  used  in  this  model  are  initially  converted  into  vectorized 
features by using Vector Assembler. This data is then split into train and test data in the ratio of 70% and 
30% using random split function.  
For the prediction of which factors are affecting the ‘speed limit,’ we wanted to understand on what 
factors will the speed limit be fixed on a particular road, linear regression model was built. Model is then 
performed on the train data to fit the regression and then prediction was performed on the test data. As a 
part of second model, we used Random Forest Classifier to predict the speed limit based on the vectorized 
features that has been selected to perform on linear regression model.  
To understand and predict the number of fatalities all the 5 csv files are used. Since the data is large 
when all 5 csv files are considered instead of performing the linear regression model, Cat Boost Regression 
and LGBM (Light Gradient Boosting Machine) are selected to reduce the runtime of code and load on the 
machine.  
All the predictors are split into train and test data randomly and setting seed randomly using random 
function. The format of date and time has been changed as per the requirement of performing models. For 
loop is used to perform these two models on train data in a single code. 
Few  predictors  have  been  created  as  per  necessity  and  dropped  few  predictors  which  are  not 
relevant, heatmap is plotted to understand the correlation between the features. There are around 60 features 
after  calculating  few  predictors.  Cat  Boost  regression  model  is  used  to  calculate  and  plot  the  loss  by 
eliminating few features. 
For  the  cat  boost  regression  model  a  function is  defined  to  calculate  the  feature  importance  and 
understand which feature most effect the accidents and fatalities. Finally, a formula is used to calculate the 
accident  risk  index  for  all  postal  codes.  Where  accident  risk  index  means  the  ratio  of  total  number  of 
fatalities occurred to the total number of accidents occurred in a particular postal code. 
 
Sunandan Chakraborty
Aren't these directly obtainable using a query?
Zonal Accident Risk Prediction 
 
4 
 
 
Model Evaluation 
Linear regression model is evaluated by calculating the coefficients, intercepts, root mean squared 
errors  and  r-squared  values  to  interpret  the  results  of  this  model,  r-squared  value  of  test  data  is  also 
calculated.  For  evaluation of  Random  Forest  classifier,  accuracy, false  positive  rate,  true  positive  rate,  f 
Measure, precision and recall are calculated.  
Error and mean error of test and train data are calculated to evaluate the performance of cat boost 
regression and LGBM regression.  
Results 
1. Research  Question  1:  In  the  result  table  1  we can see that ‘BB2 7NP’ and ‘B32 1AG’ have 
experienced the greatest number of accidents with 30 accidents in the year 2013 and their respective 
total number of casualty counts were displayed with 31 deaths for ‘BB2 7NP’ and 41 deaths for 
‘B32 1AG.’ Table 2 shows the road types and their respective speed limits. 
  
Table 1.       Table 2. 
2. Research Question 1: In the table 3 we can see the days and the number of accidents occurred on 
those days through out the year 2013. We can observe that Saturday experiences the highest number 
of accidents, main reason behind this can be lot of travelling and parties happen on weekends. But 
unexpectedly Wednesday experience second highest number of accidents. While Monday recorded 
the least number of accidents. 
Sunandan Chakraborty
Not sure I understand the key takeaways from these tables
Sunandan Chakraborty
shouldn't be R.Q. 2?
Zonal Accident Risk Prediction 
 
5 
 
 
Table 3. 
3. Linear Regression Model: when linear regression is performed to calculate the speed limit, we got 
the following results. 
Coefficients -0.0131 -0.5094 0.0931 0.6279 13.1945 
Intercept 18.3523 - - - - 
RMSE 10.485732 - - - - 
r-squared 0.275869 - - - - 
 Table 4. 
 We got r squared value as 0.2758, That is model is 27.58% accurate in predicting the speed 
limits based on the predictors. 
4. Random Forest Classifier: Table 5 shows the result of the Random Forest Classifier which got the 
accuracy of 74.02%. 
Accuracy 0.7402 
False Positive Rate 0.4166 
True Positive Rate 0.7402 
Precision 0.6358 
Recall 0.7402 
Table 5. 
5. Cat Boost Regression and LGBM Regression: 
Model Cat Boost Regression LGBM Regression 
 Train Test Train Test 
Mean Error -0.3520 -0.3577 -0.3548 -0.3580 
Zonal Accident Risk Prediction 
 
6 
 
MSE 0.1239 0.1279 0.1258 0.1282 
Table 6. 
6. Loss By Eliminating Features 
 
7. Feature Importance: The following table represents the features and their importance calculated 
from cat boost regression. Police force is the most important feature with 19.12 importance. We 
can observe the speed limit in the 7th position which plays a major role in changing the accident 
rates. 
 
Table 7. 
8. Accident Risk Index: A csv file is generated to get the calculated accident risk index of the postal 
codes. Below picture of csv file shows few post codes its respective accident risk index.  
Sunandan Chakraborty
This is an interesting finding!!
Zonal Accident Risk Prediction 
 
7 
 
 
Limitations 
 In this project initially we wanted to consider the predictors road surface conditions and weather 
conditions. But the inputs are manually entered as per witness description. Which require Natural Language 
Processing. We believe these predictors affect the accidents more and result in more accuracy. 
References 
1. Susan Li, Building A Linear Regression with PySpark and MLlib, Apr 2018 
https://towardsdatascience.com/building-a-linear-regression-with-pyspark-and-mllib-
d065c3ba246a 
2. Hanish Sai Rohit Pallapothu, What’s so special about CatBoost? March 2019 
https://hanishrohit.medium.com/whats-so-special-about-catboost-335d64d754ae 
3. Alvira Swalin , Deep Dive into Catboost Functionalities for Model Interpretation ,Jun 
2019 https://towardsdatascience.com/deep-dive-into-catboost-functionalities-for-model-
interpretation-7cdef669aeed 
4. Nick F.Pidegon , Risk assessment and accident analysis May 2002 
https://www.sciencedirect.com/science/article/abs/pii/0001691888900662 
5. Gaurav Datta , Predict accident risk score for unique postcode ,May 2018 
https://www.kaggle.com/datasets/gauravduttakiit/predict-accident-risk-score-for-unique-
postcode 
Appendix: Contributions from each member 
Task Team Member 
Data Collection & pre-processing Arunodhaya Reddy Chityala 
Data Cleaning &Visualization Tejaswini Parlapalli & Arunodhaya Reddy Chityala 
Model Building  Tejaswini Parlapalli & Arunodhaya Reddy Chityala 
Model Evaluation Tejaswini Parlapalli 
Report Tejaswini Parlapalli & Arunodhaya Reddy Chityala 
 Zonal Accident Risk Prediction 
 
7 
 
 
Limitations 
 In this project initially we wanted to consider the predictors road surface conditions and weather 
conditions. But the inputs are manually entered as per witness description. Which require Natural Language 
Processing. We believe these predictors affect the accidents more and result in more accuracy. 
References 
1. Susan Li, Building A Linear Regression with PySpark and MLlib, Apr 2018 
https://towardsdatascience.com/building-a-linear-regression-with-pyspark-and-mllib-
d065c3ba246a 
2. Hanish Sai Rohit Pallapothu, What’s so special about CatBoost? March 2019 
https://hanishrohit.medium.com/whats-so-special-about-catboost-335d64d754ae 
3. Alvira Swalin , Deep Dive into Catboost Functionalities for Model Interpretation ,Jun 
2019 https://towardsdatascience.com/deep-dive-into-catboost-functionalities-for-model-
interpretation-7cdef669aeed 
4. Nick F.Pidegon , Risk assessment and accident analysis May 2002 
https://www.sciencedirect.com/science/article/abs/pii/0001691888900662 
5. Gaurav Datta , Predict accident risk score for unique postcode ,May 2018 
https://www.kaggle.com/datasets/gauravduttakiit/predict-accident-risk-score-for-unique-
postcode 
Appendix: Contributions from each member 
Task Team Member 
Data Collection & pre-processing Arunodhaya Reddy Chityala

---
## [Alia5/GlosSI](https://github.com/Alia5/GlosSI)@[ae45a9918b...](https://github.com/Alia5/GlosSI/commit/ae45a9918bcecb0b51bc12a280f0bbcf7e53b4db)
#### Monday 2022-09-05 18:11:35 by Peter Repukat

Fix build

Fix stupid visual studio paths
My gosh, you suck!

Why cannot it be **easily** possible to include icons RELATIV THE THE FUCKING SOLUTION?! FUCK MICROCRAP

---
## [SoubranMx/React-Courses](https://github.com/SoubranMx/React-Courses)@[e1b6b49454...](https://github.com/SoubranMx/React-Courses/commit/e1b6b4945484021e670f50737a56ec61dc775743)
#### Monday 2022-09-05 18:32:25 by Uriel Soubran

IMPORTANT: getStaticPaths

Woooh, there's a lot of things to understand here.

Again, see the video Section 04: 52. Next - getStaticPaths and 53. Generando las 151 páginas de Pokémons

Where to even begin?

You write the getStaticPaths function before the getStaticProps. Not sure if it NEEDS to be before, but anyway.

GetstaticPaths is the one in charge to create ALL 151 PAGES when yarn build.

Later on, getStaticPaths allows StaticProps to obtain the params on the url, in this case, just the id as a string, using the context.
The context has way more properties, but we destructure it to obtain only params.

From the params, we obtain the id, and with that ID we axios the shit out of the pokemon ID.

We send that data as props to the page and there you can do whatever the hell you want with it.

In dev mode it is slow af, but when you yarn build, the build process is the one and only time it will be slow, because it is fetching the data and stuff from all 151 pokemons.

Once it finishes, yarn start will serve all the pages and it will be smooth fast... tho, not as fast as simple React App with vite or CRA.

---
## [6165-MSET-CuttleFish/TeamTrack](https://github.com/6165-MSET-CuttleFish/TeamTrack)@[c8f1c3a458...](https://github.com/6165-MSET-CuttleFish/TeamTrack/commit/c8f1c3a4587ae0bb68fa9d2152d5b018d2914f14)
#### Monday 2022-09-05 19:38:03 by jiru-shan

okay delete button is done i hate everything especially my sleep schedule

i love egirl asmr & playing Azur Lane at 1AM in the morning. It's very fun and is definitely not me coping while having to write dogshit code that may or may not work. Also the cloud function is a slight(larger) vulnerability, but I wrote some potential fixes in comments on index.ts.

---
## [FinsaasGH/Node](https://github.com/FinsaasGH/Node)@[b0e9bb484e...](https://github.com/FinsaasGH/Node/commit/b0e9bb484effc32ed164eb4bef51b624c3d7982a)
#### Monday 2022-09-05 21:46:51 by dnwiebe

GH-625: Log message enhancements, plus clippy appeasement (#153)

* Log message enhancements, plus clippy appeasement

* GH-627: Clippy should be happy again by now

* GH-627: one line was silly

* GH-627: starting ignoring the troublesome test again

* GH-627: there was a formatting issue

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* Added import

* GH-625: Formatting

* GH-625: Remember to return

Co-authored-by: Bert <Bert@Bert.com>

---
## [Aetherum17/WWU](https://github.com/Aetherum17/WWU)@[583af91417...](https://github.com/Aetherum17/WWU/commit/583af91417256e4fb7bace56712db18a7b1c1703)
#### Monday 2022-09-05 21:58:58 by Vawser

Magic

- Added magic schools to the magic system.
 - Each school has its own spells.
 - After learning to become a spellcaster, you can select which school your ruler will follow.
  - Which are available depends on the possibility your ruler would be exposed to it (e.g. Fel will only appear if you have a Fel province or a Fel natio has a +25 opinion of you)

- Magic schools:
 - Arcane
 - Holy
 - Chi
 - Voodoo
 - Nature
 - Necromancy
 - Shamanism
 - Fel
 - Draconic
 - Corruption (Old God)
 - Shadow
 - Runic (Vrykul)
 - Nightmare
 - Earth (Elemental)
 - Fire (Elemental)
 - Water (Elemental)
 - Wind (Elemental)

- Spells for the new schools are WIP

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[a4bfe65cb1...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/a4bfe65cb1caece1e3e6a4635fa17d39f1aa3478)
#### Monday 2022-09-05 21:59:36 by SkyratBot

[MIRROR] Dimensional Anomaly [MDB IGNORE] (#15974)

* Dimensional Anomaly (#69512)

About The Pull Request

Everyone has been asking: "When will there be an anomaly like the bioscrambler, but for the space station? Please, we need more things which replace objects with different objects from the same typepath."
Well I made it and it looked like ass because non-tiling floor and walls look terrible, so then I made this instead.
Dimensional.mp4

The "dimensional anomaly" shifts matter into a parallel dimension where objects are made out of something else.
Like the Bioscrambler anomaly, it does not expire on its own and only leaves when someone signals it or uses an anomaly remover.
When it spawns it picks a "theme" and converts terrain around it until it covers a 7x7 square, then it teleports somewhere else and picks a new theme.

A lot of these themes are relatively benign like "meat", "fancy carpet", or "gold". Some of them are kind of annoying like "icebox" because it creates floor which slows you down, or "clown" because bananium is intentionally annoying. Some of them are actively dangerous, mostly "uranium" and "plasma".
The main problem this will usually cause for crewmembers is decreasing area security. When it replaces doors it replaces them with ones which don't have any access control, and it will also replace RWalls with normal and much more vulnerable walls which will make breaking and entering significantly easier until someone has taken the time to fix the damage. But also sometimes it will irradiate them, you never know.

The fact that sometimes the changes are benign (or provide uncommon materials) and might be happening in places you don't care about access to might encourage people to push their luck and leave it alone until it starts turning the captain's office into a bamboo room or repainting medbay a fetching shade of flammable purple, which I would consider a success.
Armour.mp4

If you successfully harvest the anomaly core you can place it into the reactive armour to get Reactive Barricade Armour, which shifts your dimension when you take damage and attempts to place some randomised (not terribly durable) objects between you and hopefully your attacker (it really just picks up to four random unoccupied tiles next to you). If you're EMPed then the changes it make to the environment will often be as unpleasant for you as they are for a pursuer, and significantly more likely to harm both of you rather than just provide obstacles.

Other changes:
I split anomalies out into their own dmi file, seems to be all the rage lately.
I moved the anomaly placing code into a datum instead of the event because I wanted to reuse it but if you have a better idea about where I could have put it let me know.
This also fixes a bug where the material spreader component wasn't working when I applied plasma materials to something, the extra whitespace was parsing as another argument for some reason and meant it would runtime.
Supermatter delamination was still pointing to Delimber anomalies instead of Bioscrambler.

* Dimensional Anomaly

* Fixes the upstream merge skew

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3b2cf65d59...](https://github.com/tgstation/tgstation/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Monday 2022-09-05 23:06:07 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [sjp38/linux](https://github.com/sjp38/linux)@[210c4163a0...](https://github.com/sjp38/linux/commit/210c4163a098540e57d96cb9a78dbf3024082c9b)
#### Monday 2022-09-05 23:18:53 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---

