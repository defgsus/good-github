## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-14](docs/good-messages/2022/2022-07-14.md)


1,773,346 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,773,346 were push events containing 2,591,838 commit messages that amount to 186,647,748 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [cdcline/demo-website](https://github.com/cdcline/demo-website)@[d7bf630155...](https://github.com/cdcline/demo-website/commit/d7bf6301557eeed6838e9b3bfee14c1ed25a7ed7)
#### Thursday 2022-07-14 00:02:58 by Chris Cline

Design Beta: Animate Welcome Header Circles

Currently all the headers are static and we'd like them to be animated.

The Welcome Header has some circles that we'd like to kinda move around in
the background.

This adds a couple circles and animates them to randomly move to a new X, Y
position over a random time.

It also hacks in some header logic to display the new code.

The JS also got a bit wonky with multiple files requiring the same
external file so the loading order of them got modified a bit.

Part of #108

---
## [lgritz/oiio](https://github.com/lgritz/oiio)@[32ff1bd867...](https://github.com/lgritz/oiio/commit/32ff1bd867686b257d76f74c24868ec17ced6e8d)
#### Thursday 2022-07-14 00:57:58 by Larry Gritz

parallel.h refactoring and add support for TBB

Hide nearly all of the implementation of the parallel_for family of
methods rather than expose them as inline. This gives us more freedom
to change the implementation in the future without breaking ABI.

Deprecate the parallel methods that take task functions whose first
parameter is the thread ID. The only reason they existed is because
our cobbled together thread_pool used that in its inner workings.  But
there are good reasons why we should not expose that:

  * We never used it anyway.

  * It was not very useful, since sometimes it was a real thread ID, but
    other times it was -1 in cases where the calling thread executed the
    task directly.

  * It is inconsistent with other thread pool implementations that we may
    wish to try in the future.

So better just to not expose those thread IDs at all. Mark those
versions of the parallel loops as deprecated and schedule them for
removal in OIIO 3.0.

If TBB is detected at build time, support will be built in that allows
either the old OIIO built-in pool, or TBB, depending on the setting of
a new global OIIO attribute, "use_tbb" (default 0), if set to nonzero
will use the TBB thread pool.

In my experiments, the TBB thread pool seems slightly better -- I
think because there is less overhead, and maybe the clever
work-stealing it does elps to load balance. It's not used by default,
set the attribute if you want to use it (assuming the build
included. After we've had a chance to test more thoroughly, we may
change to use TBB by default. I'm interested to hear people's thoughts
on the matter.

One case where you almost certainly will want to use the TBB thread
pool is if you're using libOpenImageIO from within an application that
uses TBB for its own threding -- that way you're using one pool for
everything, rather than have two separate thread pools that don't know
about each other (and probably twice as many threads as you have
cores)..

---
## [RadsammyT/coding-playground](https://github.com/RadsammyT/coding-playground)@[95b348d8d7...](https://github.com/RadsammyT/coding-playground/commit/95b348d8d77693182cd43f47f5f0f74443d3f378)
#### Thursday 2022-07-14 01:12:37 by RadsammyT

oh god oh fuck oh shit im starting to become a crab

---
## [emiliodaf/emiliodaf](https://github.com/emiliodaf/emiliodaf)@[86c51435e0...](https://github.com/emiliodaf/emiliodaf/commit/86c51435e062077e7ab03759b360736e8b2abae1)
#### Thursday 2022-07-14 01:51:34 by Emílio Fonseca

Update README.md

Hi there🖐️
I am a Front End Software Engenieer. I consider myself an enthusiast of Technology who is working on a daily basis in order to grow my hard skills and knowledge to be an updated Front End developer on the market. I have just 8 months experience as a Front End developer but with a huge desire to make things happen. It's been a challenging experience but when we realize it and see our personal growth not only as an human being and but also as Software Engenieer we figure out for ourselves that all the long hours invested worth the effort. For many times It's been challenging but at the same time a really gratifing experience. If you have a purpose in life Keep moving on and Never give up! It doesn't matter how long it will take! Just Make it happen!

---
## [emiliodaf/emiliodaf](https://github.com/emiliodaf/emiliodaf)@[b4d11f77ec...](https://github.com/emiliodaf/emiliodaf/commit/b4d11f77ecb1e193bc29d7927836e546ce25c2f2)
#### Thursday 2022-07-14 01:53:32 by Emílio Fonseca

Update README.md

 I am a Front End Software Engenieer. I consider myself an enthusiast of Technology who is working on a daily basis in order to grow my hard skills and knowledge to be an updated Front End developer on the market.
   I have just 8 months experience as a Front End developer but with a huge desire to make things happen. It's been  a challenging experience but when we realize it and see our personal growth not only as an human being but also as Software Engenieer we figure out for ourselves that all the long hours invested worth the effort.  For many times It's been challenging but at the same time a really gratifing experience. If you have a purpose in life Keep moving on and  Never give up! It doesn't matter how long it will take!
Just Make it happen!

---
## [acramernc/babot](https://github.com/acramernc/babot)@[9026036e28...](https://github.com/acramernc/babot/commit/9026036e28192bd0653f0bb0eced4773dc841744)
#### Thursday 2022-07-14 02:34:01 by KittenMoon

well well well, you have caught me here again and it is a day of typing to do again. it is 4 am so this start section will not be as long as the previous one but i feel i may be able to get this git commit message to be longer than the last one, if you are reading this then i am proud of you. So tomorrow in the am or sometime tomorrow i will do an in depth explination of either SAO or AoT, the one that will ge tthe explination is deterministic on wheather or not i finish AoT final season part 2 sub seciton a class I episode 13. Yes i did over exagerate the naming of the season but that is only because it is the "final season" which has been split into three parts, one in 2021, anotehr in 2022 and the last int 2023. so that is that but when i finish it then i will continue onto the next show which is something that i cant remember at the moment but if i look it up then i would be able to figure it out. SO when i watch my epsiodes, i do not skip through it like some "unnamed" person who i will not call out at all, defininately not some eye boy with a sack at all. ANyway i do have to infrom you that i iwll be in boone this weekend so there is a highter chance i will see hey buddy but that is like me saying there the chance goes from .1% to 1%, basically nothing but not 0 so whose to say, dont you hate it when your headphones just die when the good song is playing, silly headphoenes please dont do that. Well back to what i was saying with how i will be watching some shows this summer and after AoT it will be the fate movies which knowing me will likely get post poned as i will be in boone and when there i will want to watch something shortish on the laptop. I will use the boone pokemon weekend as an excuse to just watch things on my laptop as i will be in boone w/o the desktop :(. ඞ surprise mogus. be warned they can occur anytime. ok as i was saying there will be a time an place for the summer shows and as it is june first i normally wouldve watched my one movie today but i forgot and plus i will save it for a day i am not busy withh stufff which today was. alas i will have to make sure that i can do as well as summer shows 2020 in terms of amount watched which was 16 to 17 depending on how you count it with seasons of shows and movies and finishing one right as classes started (the weekend after). but that was still in technical summer. if i can do the 14 on my list i should be on par as some of the 14 are actually multiple seasons grouped together which would make the number go up higher and there is a set of 3 movies and in the 2020 group there were 2 movies counted in that. Another thing is that the start of SS 2020 was around now (june 1) and i started around now technically but there was some earlier just like there was some earlier in 2020 (soul eater, which isaac still hasnt finished). the time may be almost 5 am (4:54 to be exact) so i should be calling it for this part of the commit for today, but this commit will not be done until i finish 3 of my shows on the list (excluding fate movies), or in a week, whichever comes sooner as it could take a bit to watch all the shows as i get distracted or it could be soon as isaac is done watching SAO which means i will not have anything to distract me, unless i watch SAO, which if i finish all 14 shows i will reward myself with a season1 rewatch, but then again it isnt as fun to rewatch when dong it alone as i cant make comentary about what i enjoy and what is going on, oh well maybe the boi will be watching his drink of bleach show, which other than the pendulum arc wasnt the best as it was well c tier at most. The orb folding playlist is currently playing at this hour as we are expirencing real classic 2021 vibe time vibes witht he late times and golden age music vibe time vibes witht the bot -playing some classic orb folding songs. there are over 400 songs in the playlist and that do be pretty knifty. so the database update worked better than i thought it would as it went off (other than hank typos) without a problem. The database update allows for so many more things as we could easily do many things with it like the whomst command which i fixed here to require a user as opposed to it being an optional argument. which that was done on the second call of deploy commands which i thought didnt work but turns out that it just needs time to deploy the command update which it told me when i tried to run the command which led me to fixing move to as well with this commit. Well i shall be sleeping soon here for real this time but to you reading this it will seem like no time passed but for me it will be as if i had a sleep, maybe i will update you with soime stuff that occurs between now and well a few words from now. idk well see you on the flip side as hank sometimes says. So it has been a day now and i it is now the AM hourse of june 2. this means it is time to continue the commit message, and well now shows got watched due to me being distracted but i think i will be watching some soon. cookie dough is good and that is what i am eating right now as it is late and i dont want to wake anyone by doing stuff in the kitchen to cook the dough, alas it still tastes good. so i took a short break there, which you probably wouldnt have known if it werent for me telling, but it was because of COC as i was doing stuff on there. i used the Adam troops to steamroll something i really shouldnt have at my level. they had over 100k of each resouce which caused me to get full and now can research level 2 boney bois. So back to what the day was, as it started off with me planning on doing some AoT watching but i watched youtube because i found something on there to watch and then it was 6pm and dinner time and i got distracted and then now it is now. I will likely watch some AoT after i finish with the tasks for the day and hopefuly maybe finish the season, idk it has 8 eps left and calculating how long that is would be about 2-3 hours dependant on if i take a break or not to get foods. tomorrow will be the day i do the genshin story quests so i will not be able to watch AoT during the day hours as that is dedicated to genshin quests as there will be some LORE in there and it will be a good watch. I do still want to do a Man rants about AoT or SAO for far to long part to this but that may have to be over the weekend or after as weekend as i said before is a semi-busy time with being in boone. Typing this commit message is bringing back flashbacks to a hey buddys class and back to when i was in classes last semester and well that is when i did the last one so it would make sense that it would be what i am remembering.  hopefully i can use my detective skills to determine the accurate date of shanes birthday, if i find it before i send this commit then i will add it but it may be a year long endeavor to get the date. I have my suspicions that it may be on July 21 but that is just a hunch and i will have to do some day checking when the time gets closer, for now his birthday is on june 9 because that is 69 haha funny number. i may hide the fact that i will put it on 69 until it is june 8th and then on the 9th call a baba command in general to confuse everyone and then cause them to have to ask for the real shane bday and call his hand, this has given me a date that this commit will have to be after now as i have wrtitten all my plans here and if anyone were to parse this it may be shane so i cant go putting this on the github yet until probably after june 9th. good thing is baba has no urgent changes and we probably wont be focusing any updates to baba until well likely sometime later this month or when i do request it. i hope that by the time that this commit message is done it will be longer than the last and more content as in other than the SAO/AoT rant, just random thoughts spewing from my brain. hank has stated that he needs to find a new jet flying truck in stormworks which is one of the games that baba could be playing if i added it in this which i havent yet but i could if i remember tomorrow as i cant be bothered to do it now. Unlike the last one i am trying my best to limit spelling errors just for my sanity but any punctuation other than commas and periods are basically being forgotten. and capitalization of things that are not the first letter of a sentence is basically a no go too. hopefully we can convince hank to add dadbot back to the server but that is not going to happen sadly :(. THe way that i will likely explain the SAO storyline will probably be more clear than if you were to watch it as isaac was watching it which was more of a skip every scene of the show as if it were a stone skipping on a pond. but that is for another day. Today bob has 6 o's in his name and he has yet to say anything about it but it has been 1 per day and hoepfully he is just not going to notice until it hits the character limit. it is a many day strat but one day he will have all the os in the world, well now that means i cant post this commit until he notices for that would play my hand, well he doesnt do anything with the github so it "should" be fine to do it before but i will probably not take the chance yet, as he does know about me doing the commit messages as i have told him both times. so back on topic here with whatever i was talking about before, well today will mark nothing as it is only june 2 and as of baba there is no holidays on june second. i will lilkely find some more holidays to add to baba and also will instead of posting error.png as the image for when the holiday has no main image, i will just do the same text overlay thing as i did with the wednesdays until, hold on let me check something real quick. ok i am back and it is fixed for this commit as well, this is how things go around here orignially the last one was 3 file changes and it ended up being a massive update with many changes and this one will lilely be the same. i will also be doing some callback stuff for baba wednesday potentially here as i had a issue with image delay again but it might just be a one time thing so i may just push the wait timer a few 10ths of a second to a whole second longer and none will be the wiser, well anyway that is all for this days stuff as i am going to watch AOT now with some snacks, see you on the flip side, again.  SO the thing is there was no watching of AoT last night, who knows when i will get around to it but i was able to get to the interlude story quest and it was a great quest where we got basically a bunch of Xiao and yaksha lore and it gave character to all the yakshas that were the hero of the liyue region. Twas good and i hope that maybe someday down the line (copium) we get to play some of the yakshas as playable characters somehow idk how they would do it but it would be nice, yelan story quest will likely have to wait for a monday playthrough as i wont want to play it while in boone, but i may do it later tonight im sure you will know sooner than later as i will say if i did it when i do it or sometime around the time i played it. Well it has been a while hasnt it, so i went to boone and am back watched AOT already and started dressup darling. so the cliffhanger for AoT was good and i am excited for part 3 after we leaned about the rumbling and the titans are heading for the mainland which caused much strife to all of the main characters. but that is enough of AoT until the next time when i will do the long explanation. currently i am on dressup darling which has been a swell time as the show is reminding me of horimiya which was a very good show that i watched back earlier this year. But enough about anime lets explain why it has basically been over a week since the last time i was doing this writing of the git commit, well there is some leek wars stuff going on which the main three working on leeks are me jeremy and ryan as week have leeks that will kill the enemies. so far the leeking has been going swell and swimingly. the leek wars also have created 5 haikus that were in the database which means we have a massive amount of haikus  now and almost have reached the covited 500 haikus number which hopefully wont be horse related like the 400th one was (hank). leek wars has been taking a lot of my time as i am making bikus the leek be able kill all the enemies in the leek gardens. Today is pizza day so it is going to be time to eat the beepza. well i have been heavily distracted while watching the great and powerful Aleeksander do his fights vs the domingo ai leek.  but anyway i think that tomorrow and this weekend will be a bit of work as i will be busy in the evenings which will result in tired time so idk if i will work on leeks until monday but who is to say really as i will possibly work beforehand on leeks or i will just watch shows like i always do, similar to today. the good thing is that deino community day was confirmed as i accurately predicted back during go fest last weekend. the good thing is it is an 11-2 cd which means i can do the whole event at the park in cary without having distractions and after while at the place in the evning i can potentially do some catching if poeople do the dieno evolved form raids there. hopefully i get a hundo but i dont have high hopes. we are back because headphones are deadphones and now i can full focus writing the git commit message. well i have now wrote the code that allows for the haiku to do a custom one and it is working well, aslo added a code part that will sanitize the inputs for adams hopes and dreams to be improved much more and he will really like the command name and not go insane because of it. ඞ surprise mogus. hey i guess i can do the wordle again in here like i did last time, it is not because i want to pad out the characters with easy amounts of text no, it is because i can do it. :) Wordle 356 4/6  ⬛🟩⬛🟨⬛ 🟨🟩⬛⬛🟨 ⬛🟩🟨⬛🟨 🟩🟩🟩🟩🟩 there you have it, the wordle for  the day splendid isnt it. the word was annoying as it took way to long of random guesses to get but i got it in the end. ok enough words, time to go back to talking about leeks and then we will do a SAO rand as decided by baba with his coin flip, next time i do a long one of these when headphones are deadphones, probably on moday, we will get the AoT rand i promised as well, that will surely pad out the run time on this if it were a video but it isnt so whatever it will take YOU long to read my dude. So we start off on November 6 2022 which is this year but when the show initially released it was 10 years out so funny how time works, but back to the show. So SAO takes place in a VRMMORPG and well it uses a brain connecting thing which allows the users to view into the game, so at first the MC goes into the game and all is well, he meets some friends like Klein, and then his friend wanted to log out but couldnt. this led to them going to the main plaza where the game master kaiba was and he told them that if they die in the game they die in rreal life and to win was the only way out. this reulted in mass panic and at the end of episode 1 one month passed and 2000 people had died so far, So as the time went on they were stuck on floor one for a while but the people wanted to get out so some decided to form a party to slay the first boss and after losing a few people to it they succeeded and we meed the main female lead asuna.  kirito told her to join a guild as she is strong and should not be a solo player alone.  Later on kirito meets a group of people who he considers guilding with but when an accident and trap kill them all he thinks it is all his fault and decides to go it solo for more time as he doesnt want to put anyone else in danger. by now there had been at least 35 floors defeated and it was about 1 year into the story as it was around chrmbo 2023.  Now around the early 2024 times we get to where kirito meets the beast tamer character silica and basically this was one of the episodes where we meet a new character who will be in his group later on when they escape. Now it is march 6 2024 and they have gotten up to floor 56 defeated and there is a main ground called the knights of the blood who asuna has joined and is one of the top ranking members of. Kirito and asuna talk a bit after meeting again, rocky start, but then they get to a town where they witness a murder. normally as this is a game where this can happen that would be bad but not odd, but this was in a town which as a safe zone so it was way out of the ordianry. they then do investiagitng and by the end the end up witnessing another murder  Kirito and Asuna contemplate the events that had just occured and whilst doing so make some food, asuna makes a sandwitch for kitito and after some witty banter about food he accidently drops it and it shatters similar to how the other two died. this made kirito realize that the shattering of the people who were murdered wasnt them but their items and they teleported away at the moment which made it look like it was a murder, they then go to the grave site of the fallen comrad of the people who were thought to be dead and realized they were paid off to do this and wee meet the dark guild laughing coffin who are people who go around killing people in the game for fun.  SOme of the people seen here are more relivent in later storylines in future seasons so remember the guild, there were 3 memebers at the site, johnny black, PoH and XaXa, these three will be important later, so anyway they go back to town talk about stuff and then carry on with their adventures, Next episdes is another one where they MC meets another side character who will be part of his team outside of the world, basically same as the other story but she is a weaponsmith. So they then go and have to fight another boss same deal asuna wants kirito to join her guild, there is a wager that happens sometime but this part was a bit fuzzy for me. then they go to around do some more boss clearing and then by the end kirito asks for asuna to go with him on leave but they have to do a battle with the guild leader in order for it to be approved, otherwise kirito has to join the guild if he loses. so kirito duels with heathcliff the guild leader and whilst battling heath ends upo moving his shield at an unmatchable and impossible. kirito ends up losing and then gets forced to join the guild. They go to get him some clothes and when stopping to rest they are met with a member of blood oath who is confiming himself to be a member of laughing coffin and almost kills asuna but kirito is able to step in and ends up  killing him.  they then decided to have time alone together and get a house on the 22 floor which comes back into play later when they come back to this place. The two of them end up getting married and then actually take a temp leave from the guild.  they then encounter an ai of the game who they make their daughter. they get yui and have a bunch of fun in their house. things occur that are not super important to the story but it is fine, we learn that yui was made by the cardinal system of the game and it initially prevented her from interacting with people but she somehow was able but now the cardinal systam was trying to remove her, but kirito was able to save her data and keep it with him so they could recreate her when they leave the game eventually.  So time has passed and they are back to fighting bosses over time and they have reached the 75th floor boss and there is a big battle against it. The next episode is the final of this arc as the final battle was going on after the battle for floor 75. so kirito was sus of heath because oh how he had such high health and was surprisingly not exhausted. so kirito attacked him and what occured was a purple immortal object was there similar to back with yui which raised many questions amongst the players in the game. Thus it was revealed that heath was the game master kayaba who then confirmed it. some dialoge continues and we learn about what is going on kirito and asuna attempt to attack him resulting in them dying but main character syndrom kicks in and he is able to kill kayaba and they then realize they cleared the game, kayaba gives a monologue and they then are able to wake up from the game for the first time in 2+ years.  and that was SAO Aincrad Arc which was only the first of 5-7 arcs dependant on how you would classify it.  so time for at least the rest of this season.  starting after they get out of the game we meet kiritos sister and we learn about what happened over the past years whilst he was in the game and what was going on outside of the game. at the end we learn about asuna as they were at the bar of the main bar keep in the game, Agil. this surprises kirito. So kirito learns about the game ALfheim online which is where he will be going to next. kirito promises to get asuna back so he ends up going into the  game to try and save her. once he gets in he revives Yui and realizes he has some buffs from sao somehow. then near the end we meet some new characters leefa and her friend who are runing from salamanders, another group in this game.. so they do basic introduction stuff and not much goes on but we meet the main big bad oberon and we learn how they would be able to get up there,.  so they now are going to go on an adventure and decide to take shits when disconnecting so they dont get killed whilst in the neutral zone. but unbenonst to both of them is that each other is the others sibling. basically kirito is trying to get a bunch of allies to help him get to the top of the world tree. and they  do the stuff in this epsidoes and yada yada not much happens sister likes brother generi anime stuff .basically there was a faction war, he solved it and now he has friend to help him with thre world tree.  so basically he knows about asuna being at the top of the tree he tried to go up there, there is an invisible barrier and there is mutiple failed attemps which are not promising for his success.  his sister confesses but knows about asuna and is sad but so be it, next up is the final push and everyone helps with this and they get into the top of the world tree after yui opens it. kirito reunites with asuna and then oberon shows and causes a proble. kitito gains god mode and then is able to use kayabas powers to defeat oberon and cause him massive amounts of pain.  this results in kirito recieving the seed and he is able to create games similar to SAO with it that are based off it with the same underlying cardinal system,  basically now they are in the real world and we learn about what kitito does with the seed which is he makes it open source so anyone can create games based off it. this also means they add a version of  SAO to ALO which this time they decided that they would successfully beat it, and thusly that was all of season 1 of SAO.   so i did say i would do the AoT on monday but i think i may end up doing s2 of SAO and maybe Aliceization too as that is as long as s1+2 combined. there is also a movie but that will be short and easy to explain as all i need to do is explain the plot. the good thing is that s2 onward will be easier as i watched some of s2 recently and all of s3-a not underworld so that will be needing some info and research but it was a watch of 2021 but early. but that may be all i type tonight but that wouldnt be fun as albedos theme is going on and it is pretty great way of carefuly drowning out the fnv stuff, i will leave it as acronym but it was a true 76, 104 nauvis orbit moment and i just dont need to worry about it as i will likely be sleeping soon aka watching more dressup darling in bed. i am attempting to become woketh around 2-3 so i can eat lunch here then and not have to worry about dinner until a perhaps hopefully a sheetz run, i can potentially get ryan in as he wanted one and it would probably snowball into multiple people being there. so yeah today has been a day of leeks, anime and pizza, with a touch of nauvis orbit., well i hope your day was great i will see you on the flip side aka in a few seconds as it will be quick for you. Ok, it is now a new day here after i have watched a few more episodes of dressup darling, it has been really good so far. so we now are vibing with the music bot and it is giving some quality songs after i do my tactial song search for the spaghetti rat song and i make a list of many songs to push to the start of the list, twas very good. so mogus has done a crossover with fortnite so i will have now a delema if i want to obtain that or not but alas monday is the day of all the things i will be working on leekscript possibly if i find time but also anime would be fun to watch. in a bit (after all the chosen songs are completed), i will start to continue some more to the dressup darling episodes as i want to finish that by the end of the week. Sumemr shows 2022 is not going as fast as i want but it should pick up soon, hahaha sure. well i hope that i can get up to par with the amount of shows in 2020, but that would be a long shot. so i will probably do a fate movie three, where i watch one per night or i binge all 3 easily. so after watching dressup i can go to vivy or i can go to fate movies which i will decide in the moment. i also want to make a timeline feature for ol scheduly, with something similar to a calendar for checking future stuff, because why not, but that is not anytime soon. ok it is now time for me to explain why there is a frog that needs to be in our house at the moment. 🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸 ahh there was some nice frogs for you to enjoy. so it is time for me to rant about my shows list which i hope i can get done before going back to class, as i have 2 months to watch a bunch of shows but the thing is i only finished 3 shows since i got back which there was time i was busy and yeah, but that doesnt matter much. well if i dont keep getting distracted i would be able to watch all the shows i want so maybe when the vibe crew goes to non-woke times i will likely go and watch some episodes. the vibe playlist has some great songs on it from love live that is flintstones and other things involving hhgregg which are all quality songs that i will try and place at the start of the song everytime i see them when doing queue scouring. at the current moment isaac is starting fallout 4 which is the same day as when he finished fallout new vegas. thusly we will probably have some form of 76 104 nauvis orbit but that will probably not happen as it is only the start and isnt about NV. take a ride on the bungle bus you will enjoy it. bikus the leek is doing well and i hope that when i implement the quality leek stuff that i want to on monday then i will have to do that then. i also could use the wed/thurs pair time to do the leek stuff or watch a bunch of episodes. i do plan on having some form of watch time when the time comes, i will need to make sure not to get distracted when the time come but that will probably happen and what can i say but i told you so me. something about hank meeting a ghoul is what is going on in fallout right now as the person who was at the gate became a ghoul in 200 years.  after this song that plays finishes then i will have to go downstair and get some sort of dinenr as i am hungry and only ate the tacos around 4 when i was not at home. timelines of frogs invlove the frogs in the time of the frogs being timed to find where they are kept hostage for the time being. hopefully when i finish this git commit message we will be over 50k characters as right now we are only at 27k so if i am playing my cards right this will be the middle of the whole document. crab rave time!!! the haiku database is going well, as we are going to hit haiku 500 real soon, at the time of this recording we are at haiku 496 so we only need 4 more haikus to get the perfect 500 in the database. it would be extra great to have 500 be a good haiku and not some sort of horse repeating haiku as 400 was. it took us 3.5 months to make a total of 100 haikus which is a good HPS haikus per second rate, even though they are not made each second it is faster than other sets of 100 like 0 to 100 or 100 to 200, etc. but that is not to be worried about as i am estimating by the time that this update goes out to baba we will be well above 500 if we keep talking in the leek channel like we do as it causes many haikus when we do that. ooo grand escape, good song is now playing and it is a blast to listen too. i should tune my car reckonign playlist to be set to play grand escape tomorrow whilst i drive to the place i must go to at 3:30pm. ok i want to go get dinner still but i havent as i am currently listening to the quality songs that the music bot is playing which i do enjoy at the highest degree. we soon will get horse race, genshin themes and random chiptunes and it will not even be 2 yet, i hope that by 3am i will start up some episodes of dressup darling. that would be swimingly great and exceptionally splendid, indubitably quality watching of shows to watch. BEANS! So it has been a few days again, and in that time i finished dressup darling. it was a very good show to watch and i hope there is a second season because i want to see more of the content that is in this show. also tomorrow is supposed to be 109 feels like which will be pain and we have nauvis orbiting going on with NV so aaaaa but whatever. now onto something that may be pushed soon in this update, it will be the voice activity update. so in this we will have baba have the ability to track users voice activity and when they are in voice, there will be some things to make sure that the data isnt lost when baba crashes but this may require testing on production. this couldnt easily be done without the db update and i am glad it will be made as i hope it works out well. i think i can code it well, it shouldnt be too hard, the difficult part will be crash data prevention. so we may need to do a bunch of testing but whatever. that may get worked on around wed/thurs if i have watched enough episodes of vivy to be satisfied in doing a bit of programming for baba. and yes vivy is the next show i am watching as it seems like it will be a fun watch to see. idk what the major premise of it is but it was reccomended during one of the videos i watch with seasonal animes, it is many months old but i am sure it will be a fun and entertaining show to watch. speaking of watching stuff, tangentally i was able to get all but 2 of my friend-10 max ascention characters in genshin to have their lore explained and read/listened too. I have mona and ALBEDO left to do that with and i may do that later tonight after getting snacks or it will be tomorrow/wed as tomorrow will be the most painful day  of the year. i hope the thing i need to do gets cancelled tomorrow as heat is not enjoyable and it will feel OVER 100 in temp and i would not like to be outside at all when it is 80+ none the less but 100 is going to far. so i had a thought about rendering the bungle bus in the hey buddy renderer but i dont want to think about the logistics that would be needed to do that. so i will probably not do that at all as why would i cause myself pain when i could cause myself fun with coding baba :). also the weather update for baba will have to occur too, if i have time on wed/thurs and get the voice activity update working early then i will possibly work with baba to get some weather predicting and allowing baba to give you weather for any location as long as you provide it, also it will be restricted to USA. baba hurricane tracker will be easy as it will just use the one from NOAA but i hope that it is just a single link i can copy and send in chat and it will work correctly, i hope it doesnt involve web scraping but i may have to figure it out and im sure it wont be super horrendous, only a little bit but that will be as expected of anything with baba the multi-funtional random discord bot. oh and back to the voice activity thing, baba will also detect if a user is in voice on their birthday, i may do a crude date detection thing if user is already in channel, similar to how baba makes holiday channels, and if a user joins on birthday then baba will join and say happy birthday too. the only thing is should i check if user has already had baba say happy birthday or should it happen everytime, also i may put it on a one minute delay to allow the user to settle in, and void if user leaves within the minute (hank jumping in with mic problems). this is turning out to be more complex than i thought but it should work out. also i hope shane makes some good charts from the data i collect, but it will take some time to get working. also for getting baba to speak we could try playing audio clips generated by 15.ai of thing that i pre-provide the bot, including saying like happy birthday, etc. and a list of audio clips of each of the people in the servers' names. now we need shane to provide his birthday and this might just be the incentive. we could also have the voices be different and random, such as horse, tf2 characters, narrator, etc. it will be an excessive amount of audio files but why bother, it will be cool. to splice them we could either use a package for node or we could do the crude way of just playing them in order after each one stops, which may be more complex dependant on how discord's API works with detecting when an audio file finishes. oh no does this mean we will be needed to add ffmpeg to baba because i dont want to deal with that after jukebot and all his fun things, but it will not be as bad as i have it installed on here already, i think, either here or the laptop and if i have to do laptop gaming to get baba to work so be it. well that last part of the text was all actually relevant to baba so there is some use to reading all of this commit message, also i wonder if this is longer than the last one as the last one was some unknown length. also i think it is snack time perhaps, but that involves moving downstairs and oh boi do i not want to do that. especially if i have to deal with massive heat tomorrow and be outside for many hours on end without any breaks to go inside, i guess bathroom breaks may occur more often as i will have to use the 'bathroom' as i am drinking more water to keep away the heat from murking me on the morrow. ඞ surprise mogus. ok ok ok, time to get back to doing something that is important, reading genshin lore, i learned so much about the characters as i am learning about their lore and such. once i finish the genshin lore stuff, i will have to swap over to doing teapot suff as i have wanted to basically since before 2.6 and 2.6 was the 9 week update with no teapot editing ability so that is a hefty amount of time, this will also allow me to get the ruples for all the inazuma characters which i have been neglecting getting but i will eventually. so i will check off two things at once, which once that is done i will only have the recokoning left on my any day events part of the schedule other than the shows i am watching which currently i am between shows so nothing has been added as i dont normally add things until the day of. but if i am able to check 4 things off of this list by the end of the week it will be super great and i wont have them lingering over me like they have been for months now. i could work on the teapot stuff today but i may just call it an early night and use tomorrow to finish a bunch of things too whilst waiting to see if there is any cancelations due to heat (oh how i hope). i think the reason i am drained right now is just hunger and if i get english flavored muffins i will be able to regen my energy and stay awake to post 4am doing genshin or even starting the show i plan to watch, vivy. i ate snack, twas good, now i have energy again and will probably just move to bed and finish off the day there. so its been a bit, today now has become june 20th and we have finished vivy, very good show and i enjoyed it swimmingly. it has spoked the want for me to do another version of the recokoning. as right now i am listening to the final song of vivy. so i have also yet to do the genshin stuff i said i would do the following day but i think i will get to it tomorrow possibly or even tonight as it will be a long night of being awake and watching some dragon maid. i have started a bit of watching dragon maid and it is going to be one of those good entertaining shows which i find fun but not movingly great like vivy and horimiya. the shows that are single season which are 12-13 episodes are the ones to watch out for good stuff. so a brief summary of vivy is that at the start an ai from 2061 gets a helper ai from 100 years in the future sent back in time to help prevent a war between AIs and humans. this happens on a specific day that is significent and it will be explained later by me why. so the first episode goes into the two of them meeting and saving a person who wants to give AI's more rights as he is being targeted by an enemy faction known as TOAK. whilst battling them vivy saves a man who turns out to be important figure in toak in the future. after saving them vivy sees a future news paper where her friend dies and she tries to save the friend but the support AI stops vivy as they are not here to change the timeline. we now skip into the future where we vivy reconviens with matsumoto (support ai) after he shutdown for the years between in order to not cause any anomolies. this mission involves them saving a space station in which it kills many humans and is caused by one of the ai's that were controlling it. so they go onto the space station, and the head ai on the ship was not what matsumoto thought she was. this made vivy want to find out more and not just shut down the head AI. we then learn that TOAK has infultrated the space station and it is headed by the person who vivy saved back at the falling building. the members of toak brought an ai that is the sister of the head of the space station. they tried to impersonate her and cause the ship to fall down with them on it to send a message. vivy ended up saving the head of the station and they fought toak and the only casualties were the two ais, the head ai and the one toak brought. so then there was another time skip to many years later when there was another event they needed to fix due to the singularity project which they were working on. this one was stopping the ai only island from existing as it was a step up in ai rights. so they try and go to the island and meet up with another who wants to destroy the island too, which results in them making it to the island. they meet some friendly bots at the island but sadly they had to put the shutdown virus into it which resulted in the islands defense systems kicking in. at the same time toak trys to invade and vivy saves the same dude again and he sort of helps them take back the island. the island is actually the dude who they met initially's ai girlfriend who was going to become his wife but due to the sunrise incident (space station), things played out differently. this resulted in a chase sequence where they were able to shut down the island but the dude couldnt live without his ai wife. this caused vivy to have a catastrophic error which resulted in her being reset. many many years later a vivy (with no memories so we will refer to her as diva), sees a person who she thinks she knows so follows him but this results in her meeting with matsumoto again and he ended up trying to pretend they dont know each other but they chase each other around and mutually agree to work together to stop the next catastrophy. this one is the first documented ai killing themselves. so they spend this episode seperate but together working on the mission which resulted in matsumoto learning who was behind the catastrophy which was a support bot controling the girl ai who died. on the other end diva meets with the head of toak who now is in an ai body as he would be too old now. they do battle with each other and he just wants to know why she saved him as his former teacher was an ai who sacrifised himself to save others and he couldnt understand why. he was successful in getting a virus into diva which reset her alter ego back to vivy again. this occurs duing her final concert on the main stage. we then jump to a point in the future where she is now in a museum as she now has retired from singing and is a display that people can talk and view. this is where she meets osamu who she talks with over and over throughout the next many years. she also starts trying to write her own song as she wants to know what the heart means to people and her. we then learn that osamu is the person who created matsumoto the ai. then we cut to the day of the war and it still happens which results in them trying to find osamu to learn what they could do. they then go to toak which is where they meet the grand daughter of the toak leader she saved many times. whilst there they meet the sister ai who was brought on the sunrise and they learn of how she still serves her master. they then learn about what is going on in the world and how the ai are following orders from the archive and how any ai that hasnt connected to it is still safe. vivy connects with the archive to learn more and learns that the archive has known about what they have been doing for the past 100 years and still decide that this was the right path, but one part of the archive believes that vivys song she wrote on her own was enough to show that ais and humans could live together. and that ai tells vivy if she sings the song then they could stop the ai from destroying humanity. thus they go and try and take over the archives tower but while doing so almost everyone dies due to the ais getting the upperhand and they archive sends down all 1000+ sattelites to earth basically wiping most of humanity out. but osamu survives and this allows for him to send vivy's conciousness back to when they first met to go to toak immediately. in doing so it would cause him to die as he was saved by her but he was willing to risk his life to save humanity. vivy goes back in time which allows her to go to toak immediately and tell them about the plan of action to stop the sattelites from falling and the rogue ais. so they split up and vivy goes to the stage, while everyone else goes to the archive to stop it. vivy is able to sing her song and they are able to stop the sattelites in time except one which would destroy vivy but matsumoto is able to stop it in time which results in all rogue ais stopping function. in the epilogue matsumoto is all fine again and vivy is revived with no memories but she has her purpose to sing still. so that was the brief recap of vivy -fluorite eyes song-. basically if the show is something i really enjoy then expect a recap here, as long as the baba update hasnt gone out yet which it still hasnt as i am waiting a bit for people to forget about the voice activity update. speaking of that well it was implemented basically the day after i said i would and i did get it working 100% efficiently but then i brought it up and now it is opt in so ugh, but whatever it works and there is a new opt in command and opt out command. also it will technially opt you out immediatly but you will get a message until you run one of the commands and i cant be bothered to get that working anytime soon so that may just be how it is. but the good thing is that it works very well and i am glad that it does. i think that this update may be done soon but idk as i dont feel like dealing with the hastle this week maybe it will be sometime next week or after hank and adam go on summer camp which will be the most reasonable as in case baba breaks catestrophically then we dont need to cause hank pain whilst he is not home. still got the final song of vivy playing i think that this will be one of the first GG bois songs in a long whiles as i havent added to this since idk when but it has def been a while. oh and another thing that has happened since the last stuff that has happened here was that we had not one but two winning clan wars in COC which was good, i was mr 98% the first time but redeemed myself for the second war. we are about to have our third war tomorrow which will be knifty but after that i think we will take a break (as adam wants to). i have gotten 4 builders now which is gaming but alas. also the vibe playlist (scriblos to feed bikus too) has gotten the vivy song too which i may have had a part in making happen :). ░██████╗██╗░░░██╗░██████╗ ██╔════╝██║░░░██║██╔════╝ ╚█████╗░██║░░░██║╚█████╗░ ░╚═══██╗██║░░░██║░╚═══██╗ ██████╔╝╚██████╔╝██████╔╝ ╚═════╝░░╚═════╝░╚═════╝░ omega sus, this is rare but could happen anytime. oh in this week too we had a drum event in genshin which was really fun and we got some itto lore which is always appreated. back to vivy, so the matsumoto ai cube/bear was voiced by itto's va which is really cool as i like his va and he makes things funny and entertaining when talking. so i am hungry again and want to get waffle house but everyone is playing a game which means no waffle for me likely tonight :(. mayhaps around 2 am but that will be cutting it late in the night as i will be starved by then and have withered away probably. heyo again, it is I, and i have finished dragon maid season 1 but that is not why i am here, the real reason i have arrived is for the fact of that baba has buttons now. so haiku purity score will show only 5 items per page and if it gets more than that then buttons appear which allow for going between each page successfully. this was new thing i learned which means buttons could be used for other baba stuff as i have figured out how to parse the fact that only the user who sent the message can click the button. this could work for some other functions but idk what it could be used for yet if i add more then it will be included here. well today is sheetz night and pizza day too which is a double win. extra gaming will be done today which means fun. so i want to start some more dragon maid but i paused watching it due to so many YT stuffs but i finished that and now i could easily watch it later in the evning which may happen but i cant stay up that late as pokemon CD is tomorrow which means an early bed not to mention the double game tommorow which will mean a LONG day but hey baba wont be updated for a couple weeks as we are wating until post summer camp so that there will be no need to debug whilst hank is away. bikus is cool. so the next two days will be a hastle to deal with but once they are done i will have 2 days of good, and that will be alternating on and off for the next few bit of time until we hit the day SAO movie home relase which will be a good pattern. but the good thing that is better than last week at this time is that my friday was fully open which means that i was able to watch all my YT stuffs which will free up saturday and sunday evenings for dragon maid as if i play cards correctly i could do a 4 episodes per day system in which the next three days i do 4 per day, maybe more on sunday evening as that will lead to monday which is free and the night before i will be overly drained probably but who knows. hey at least the baba update is working well and it is done efficently so it will only get the data on call 1 to baba so it will just used the cached data when paging around. this will result in mismatched data if something is added while command is active but that will happen very rarely as i manually add the data and i would be the only one who is using the command when that could possibly happen as i am the one who commands. we are nearing the covited 50k characters i wanted for the commit update which means i will be able to do the baba update any time after that. that was the real reason i was saying baba should be updated post hank summer camp as i wasnt sure i would get to the character count when i wanted to. also it would mean i would have to omit the SAO s2+ introspectives and the AoT one as well which i will likely get to once i finish 2 more shows fully and probably before fate movies (i will get to them eventually). i have done well for this week as i finished 2 shows this week (technically, as vivy was started last week but it was only thursday last week which means i got through 2 shows in a 7 day period of the 16th - 23rd/24th. so after dragon maid is done, which i will likely next be here after that as i wont care too much to do any typing here over the weekend until potentially monday and i HOPE that i will be done with dragon maid by then but that is unlikely to happen fully. but we will see, and that is probably all for me here on the 24th of june, see when i see. heyo it is me mr boi boi back here on saturday after the long day of stuff, wasnt expecting to do any baba stuff but i got next birthday for wednesday command working so we now can get the next persons who has a birthday, their birthday to show. also baba has more buttons for the button update which was the solution to multiple events on same day when calling next event when it came to displaying them both like the legacy command system did. the old way was to pass both images at once but that wouldnt work with interactions as easily so now we just have a pagins system which allows for switching between frogs similar to how the haiku purity list works. there is no page numbers but oh well doesnt matter. also the code i wrote for haiku embeds works for this as i just pass the message i send in an array and it will generate it with the pages and it just works well. there may be some more buttons in the button update but at the moment i am unable to think of good ideas for them, maybe voting or something but idk how to get that to work. i will have to look throught the list of commands. 50k characters were just hit now so we can update baba anytime but that will be still done post july 4th and the summer camp week. that week will be likely high levels of show watching as most people will be away leaving me the ability to be at the computer or bed and watch many shows and maybe even the fate movies, ha funny joke. ok that was all, time to go watch my shows again but first get through YT stuff as i was busy all day and am now just getting time to do that. hey buddy, it is i here after the weekend of stuff popping in again on the 27th in the am to say no progress on dragon maid season 2 except for 2 episodes but i just ate a snack so i will probably stay up watching some episodes potentially soon. ok that is all for now. it is wednesday my dudes, no it is really June 28 and i finished the episodes of dragon maid now and the tuesday before the big rains start occuring amongst the north carolina areas. so dragon maid is done now and baba button update has been added a bit more too as well, we have now the paging system for wednesdays and all the other frog related commands that deal with holidays. oh and idk if this was mentioned all the way 50k characters ago but baba has now more friday varients for when the command is called on a non-friday day. they are funny also we brought back the how was your X doing funny command. so next up on the chopping block will be the show called sabikui bisco which is a show that i know not much about but it seems to be a good thing to watch and it might be fun. ok we have done 2 episodes of the show and now it is the 30th in the am and i will have to drive out to raleigh for picking up people. oh boy will it be a time to drive at this hour but alas it must be done. we shall take the fun road and it will make it the most easy to do. but then later we will be able to watch some more episodes of my show and also probably eat some form of dinner, i thought i would have to leave earlier than i did so i didnt eat yet as i was going to after but since it has been so long i guess i must eat snacks beforehand. ooph. oh how mind bending 5d chess with multiverse time travel is, thusly we must go and play that tomorrow potentially but unlikely as those who may play it wont be playing it when i get home around 10/11 tomorrow, alas it will be for the days i dont go outside. but at least there is a pattern to the outsides where it is 2 days out, 2 days in up until the 8th which is the day SAO movie is released which will be cool and i will likely watch it that evening. this meaning i should have no shows on the plate when that day occurs, so i must plan accordingly. i would be watching some of my episodes right now but i must leave at anytime and i dont want to leave mid episode and i know 100% sure that when i start an episode i will be summoned to leave on my adventure. finales for some of my other shows were this week so that frees up 45 mins for both wed and thurs for the next few months which is good and lets me watch more shows/YT videos. the kitten is making noise again and he needs to get some pets but he will be a special snowflake as he was playing with the cat door. still havent left yet and it is 1am :). i couldve watched many episodes and had dinner by now but i have yet to, alas we must keep wating. i will be taking the outer circle road for sure now as it is the most straight drive there without any odd paths. the issue here is that it will be one hour of time before i get back home and preferably want to get home before 3 so i can possibly eat something. alas i must continue to wait. ඞ, surprise mogus. i guess i could get cookout whilst out there as it is along the way and it would solve my hunger issues. that would be gaming to the extreme levels and it would allow me to not be hungry anymore. so about the AoT and SAO rants, they will return but i will likely do them during the week of summer camp so that i could wait until the absolute last moment possible. but that doesnt matter much as i will still do them for sure if not in this commit then the next one that will be published to baba in september. this is what i call a pro gamer commit message. long and im sure no one will read it but as the days go on it gets longer and longer until it becomes so long that it causes adam to go insane. the only person who i think will even skim any of this is SHANE, i put his name in caps there so that he will se it more likly and read the stuff before this, i see you reading this and you should know that there is some quality content in here you just have to read it ALL. ok enough about future people, back to now where i still havent left and basically i will just keep typing random stuff here until i am going to leave. see i need to limit my time to before 2 so that i am guarenteed to get some cook out as it closes at 3am, which is good for me at least, but why do i need to wait so long before leaving? idk man, i just want to go now so that i can eat dinner or something. hey we hit 55k characters now which is pretty cool but can we hit 100k? probably not without the AoT or SAO rants, might even need both. but who knows, as AoT is 4 seasons of stuff so that would be a lot to type and SAO has 3ish seasons but the 3rd is the same length as s1 and s2 combined so technically same amount of episodes as if it were 4 seasons. so both have the same season counts which means probably 40k+ characters in there total or each idk how to count that well. you can give spahgetti to a rat, incase you didnt know that. here frog 55555, that is the character count at the end of the last 5 in the 55555. you see i am running out of quality content to provide you and have resulted to listing the character count now multiple times within a 1000 characters, the old me wouldnt have done that, youve changed me, youve changed. Frog, ah a classic. so the baba progress bar is working well and we have gotten to 49% through the year which is very good but i hope to post the progress for 50% before daniel is able to post the twitter message in general. he has posted it at 40% and 45% so according to the pattern he should post at 50% as well which will happen any day now as we are .37% through 49% so soon we shall arive on the prophecised moment. why so late? idk because i said i would do the thing i would do at this hour but i thought it would be sometime around midnight or maybe even 11pm but not post 1:30, i think i will leave and head out at 1:50 even if not summoned and get food before hand. see i was going to have chicken for dinner once i got home but i cant make it before as it is a 30 min timer and once i get home would not be fun to do at this hour. plus i cant make it whilst waiting as if i get summoned i cant just pause the cooking easily. so i have decided to get cookout as i said before. daniel would be jealous of me as he lives for cookout so much and wants one closer to his house, which is why he likes the one in boone which is fairly close to where he lives there and he goes there frequently. it is me again, been a week or so, we are now on the eve of july 4th and it was an extra spicy hot outside day today where it was so hot i felt like death. but that isnt why i am here right now, no, i am here to talk about how we have had a takeover of the server by jeremy as hank and adam are gone and the server is now a concertina server, very excellent. ok now no knew baba stuff was added recently but i did finish about half of the next show i am watchign which is very good and i should be able to finish the rest within the next few days, famous last words. ok but anyway there may be frogs in the house somewhere as frogs are always in the house!! so the genshin livestream has occured and oh boi is it a hype to want the next update to come soon as we get kazoohoo as one of the 5 stars which means i will be getting him, there is also a new 4 star on that banner that i will get along with him as a bonus and if i dont then i will be sure to wish until i get him, and if i get a klee so be it i can get another character i dont have. lets just hope i dont get a dupe standard banner 5 star again, but knowing my past luck i will be likely to get one (that is if i get another 5 star). see i will want to save up my genshin ruples for the update after this, the one in august, as that is speculated to be 3.0 which means new characters in the masses as that will be a major update that has been a year and coming. also the thing is at the later half of that update, really close to the end that is, there will be the aniverary stuff as that falls in september which means more stuff there as well and hopefully more quality genshin character themes. but back to the next update, 2.8, so if i am to get kazoohoo before i get any copies of heizou then i will do a bit of wishing on klees banner so if i do happen to get another 5 star whilst trying for heizou it will be a new character so i can only be missing 3 characters, yae miko, yelan, and kuki shinobu (who may be obtained). see shinobu is a 4 star and will be in the pool of possible characters in the banner so if i am "unlucky" i will get her and then i will only not have 2 or 3 characters (klee dependant). see klee is the character that has been out the longest who i have yet to get which may change as i do want to have every character at some point and i say that i will try to get characters on their re-runs if possible (no other good characters on the current banner or no upcoming quality characters). but klee is the exception as she doesnt seem to have much use to me, but maybe i will get a copy of klee. so now 3.0 should be releasing on aug 23, which annoyingly is the day after classes start back up so it will be a pain as i do not want to deal with both classes and 3.0 at the same time but that is how it will have to be i guess, but hopefully since it is the start of the week, i will not have much going on in terms of HW so i will have plenty of time to do the probable archon quests that get released, and the probable story quests that do as well. because i know for sure that 3.1 will be when the release the archon as that is how they tend to do it as 1.1 was zhongli, 2.1 was baal, and 3.1 should be kusalani (i think). venti is the exception as he was in 1.0 but the whole prologue was released when the game released so it doesnt matter that much with him. but the good thing about 3.0 is there should be new content and exploration to do, not that we havent had new exploration at all as we have gotten chasm and enkanomiya recently which were a good change of pace. i also have to continue my 100% clearing run which will require a day or two of full genshin focus, as i got enkanomiya/chasm basically complete except for a few things, but now i have to do all of mondstadt, liyue and inazuma, and i want to preferably be done with this before 3.0 which means i have until classes begin again, which if i carve out a week to do this, i should reliably get it done, even if it is an hour a night leading up to that week, it should be done in less time that i think. but then again there is a lot of map to clear and i have gotten only a smallish chunk of mondstadt done. especially the puzzles that i have to do, those will be the hardest to make sure i have completed, but i think with some determination i should be able to get this done. ok now we move on to the 3.0 stuff. so in 3.0 i assume we will get 3 sections of sumeru as we got 3 islands of inazuma when it released and hopefully the subsequent updates after will release some more sections until we reach the usual 6 parts per region. also i wonder what the conflict/enemy fatui will be in sumeru because all i know about it is that there is a semi-new archon who was only put into power in the last 500 years after the previous one died in the archon war. but stepping back to 2.8 we have a semi-rerun of the golden apple archapelego event in which we can go to the islands again which i am looking forward too. another thing that we will be getting in the next update is a diluc skin which is the first 5 star rated skin as the previous skins for 5 stars were only rated 4 stars. this being that it comes with new voice lines and new idle animations so it will hopefully be not much more higher in the genshin ruple price but we will see when the update gets released in about a week. the good thing is that on the day of the update and the day after the update there is nothing going on for me in the outside realm so i will be able to stay up extra in order to do more genshin stuffs which will be pretty cool and it will be likely after this baba update comes out as well as hank/adam will be back around that weekend before the update. july 7th and we have now achieved another small addition to the baba haiku stuff in which we will now have the ability to view purity score list of dates, which previously impossible to do because it would be too long is now going to work as the list is now paged. this means we have it sorted by number of haikus, then purity if haiku count is the same, and if purity is same then it is sorted based on date in where the newest dates fall first in the list. oh so idk where i was in shows last time but i have gotten through all of sabuki bisco and also finished all of the finest assassin which well that was both done in the same day which was a good day for watching shows, i think the next show i will watch may be a fun one but idk what to pick exactly, im sure it will be picked before i return here and maybe done before then but i do have to be on the outside tomorrow as i did today let today was shorter than normal as it was a slow day. but on genshin note i have done all of the hangout events and now i am ready for the new update to release in under a week, also tomorrow is SAO movie release but lets hope it is up somewhere with easy access as soon as possible because i have been looking forward to this for over 9 months now and probably even more since it was announced back sometime last year. i havent gotten much new SAO since pre-bleach era, but i did get a good dose of it when isaac 'watched' it, more like skimmed through it. convient timing that my music is playing the SAO section right now but that is not now when whomst ever is reading this if they are reading this is reading this at the time they are reading this by reading it. bikus. ok time to figure out the next show to watch but that may be difficult as i want to pick a short and quick one so i can watch SAO, love is war and spy x family later next week or this week. but i do have good choices lined up which is pretty cool but that just means indecistion which is great. baba update is coming soon which means that this message will be coming to a close and mayhaps it will be this weekend or sometime next week, all depends on hanks mood, schedule and when i am able to be here to help debug the update. thusly it will be a waiting game and i wonder how many patch updates will be need to be in place after this one as it will have the voice detection update which hopefully goes off without any issues. i will have a bunch of changes that i will need to test on production when it goes live but that is for future me to deal with and he will have to take all the pain. oh and maybe there will be a SAO/AoT explain here soon if i get the want to do it today or tomorrow when just sitting in voice. oh speaking of voice the boi has joined voice which means perhaps i will join too, well i did and now i am watching a v…

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[70f669363d...](https://github.com/k21971/EvilHack/commit/70f669363d6cad4712da587a346b7443e8552ba7)
#### Thursday 2022-07-14 03:09:47 by k21971

Fix: foo, poisoned by a cursed amulet of life saving.

Wearing a cursed amulet of life saving will not work, and the player
will die via whatever caused them to die in the first place. The
inclusion of KILLED_BY here was not entirely correct. Yes, the cursed
amulet of life saving didn't help you, but that's not why you died.

This commit incorporates NetHack 3.7 commit 47cef18, which provides a
proper 'while' statement if an amulet of life saving doesn't work. Then
we call savelife() in the routine that causes a cursed amulet to fail.
End product is proper death reason output.

---
## [JamesAgerton/Ranger](https://github.com/JamesAgerton/Ranger)@[37b47f61bd...](https://github.com/JamesAgerton/Ranger/commit/37b47f61bd25a2d463296b09be5ce93b9e42b49d)
#### Thursday 2022-07-14 03:55:42 by James Agerton

LET THE ENGINEERING BEGIN

So current plan is to set up override input in the main menu, and pass down commands to "active pages" using interfaces. Fuck you common ui, I'll make my own!

---
## [Layla-Veridian/XRF-Third-Contact-production](https://github.com/Layla-Veridian/XRF-Third-Contact-production)@[05ff5cdfce...](https://github.com/Layla-Veridian/XRF-Third-Contact-production/commit/05ff5cdfce37fc95d79f9f92a260eabf1fb467ee)
#### Thursday 2022-07-14 04:07:22 by Aphast

Sneed - Feed and Seed. CHUCK - F**K AND SUCK WE GET IT HAHAHA HA SO FUNNY BECAUSE F**K AND SUCK F**K WHOOOOOA BRO LIKE HAVING INTERCOURSE AND FELLATIO HOLY WOW HOW DID THE SIMPSONS GET AWAY WITH THIS ONE? GOLLY GEE WILLIKERS WHAT THE F**K IT'S ABSOLUTELY HILARIOUS AHAHAHAHAHA BECAUSE SNEED SELLS FEED AND SEED WHICH IS TOTALLY NORMAL BUT CHUCK, CHUCKY, CHUCK SELLS F**K AND SUCK CHUCK SELLS F**K AND SUCK! F**K AND SUCK! (#3)

---
## [mehkanik/C39](https://github.com/mehkanik/C39)@[af9acf357d...](https://github.com/mehkanik/C39/commit/af9acf357da0b1271e29396e8de4d392605e0642)
#### Thursday 2022-07-14 04:11:58 by Mehkanik

fucking fan fell over and scared the living shit out of me while thinking about what this commit would be

---
## [delphix/linux-kernel-generic](https://github.com/delphix/linux-kernel-generic)@[9997f61537...](https://github.com/delphix/linux-kernel-generic/commit/9997f615374a116e05bbad5b2fef49a28e6afdf0)
#### Thursday 2022-07-14 04:26:20 by Linus Torvalds

gpiolib: acpi: use correct format characters

BugLink: https://bugs.launchpad.net/bugs/1973085

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

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
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kamal Mostafa <kamal@canonical.com>
Signed-off-by: Kleber Sacilotto de Souza <kleber.souza@canonical.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[eef96411a3...](https://github.com/treckstar/yolo-octo-hipster/commit/eef96411a33c7fd383ec847a14ed515929f0daf7)
#### Thursday 2022-07-14 05:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [vbegin/terminal](https://github.com/vbegin/terminal)@[9ccd6ecd74...](https://github.com/vbegin/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Thursday 2022-07-14 05:25:35 by Mike Griese

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

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [Zman2024/WaifuOS](https://github.com/Zman2024/WaifuOS)@[e79e1ed4d5...](https://github.com/Zman2024/WaifuOS/commit/e79e1ed4d591d6cc3ce06be9b570c534a2232a08)
#### Thursday 2022-07-14 06:02:21 by Zman2024

working scheduler?
he broken or maybe not

also added some cxa stuff pls ingore

Oops i didnt commit, oh well!

So yeah the scheduler kinda works. I should really look into how to do it properly a bit more but for now it does switch context and thats kinda the point

In other news, i made fixes for real hardware.
Added/Changed CPU.h/cpp/asm for discovering / enabling hardware features

Did some optimizations for memcpy (but i still dont really know what the FASTEST way to copy large amounts of data is)

Yield is now a seperate interrupt

I did other things too but i forgor 💀

I need to add thread safety this is bad

---
## [dfinity/motoko](https://github.com/dfinity/motoko)@[e883348f8a...](https://github.com/dfinity/motoko/commit/e883348f8a35c0925d7363cc6b9488fdac261a29)
#### Thursday 2022-07-14 06:17:10 by Gabor Greif

feat: introduce array-slice processing for compacting GC (#3231)

This PR introduces a modified marking (and visiting) technique for array fields, where `Array`s are GC-ed by considering their suffixes as slices, pushing these on the mark stack as bulk collections, and treating the fields in the prefix as individual objects being pushed onto the mark stack.

Following key changes are made:
- when visiting an `Array` in the dynamic heap we consult a new callback that can opt-out of the individual processing of some suffix of the array (by returning an index smaller than the array length)
- fields before this index will be processed as before by the first callback
- for the suffix the new callback is in charge to perform the bulk action
- in case of array marking, the new callback checks if the current slice is longer than some cutoff, and if so, it will push the array and the start of the suffix to the mark stack. (We abuse the tag entries as the start index for the suffix slice, so the cutoff must be numerically bigger than the biggest heap tag; this invariant is enforced)
- when pulling entries `(obj, tag)` from the mark stack a `tag >= TAG_ARRAY_SLICE_LOW_LIMIT` indicates that we have to deal with a suffix slice of an `Array`. The visitor will then again check the slice's length and do the subdivision again, as necessary.

This way of treating suffix-slices as pseudo-heapobjects originates from the suggestion of @ulan in a SGM (2022-05-30). It sidesteps the issue with layering violations, and restricts the handling of pseudo-tags to a very restricted portion of the collector source code, viz. the pushing of the range, and the visitor's case analysis on the tag, which now needs to  know about the suffix slices. Fortunately the visitor already accepts the heap tag as an argument (and doesn't extract it from the object; which would be unreliable due to threading), so the appearance of pseudo-tags is not a big deal.

The cutoff is currently chosen as 127, so for any `Array` at most 128 new entries are being placed on the mark stack.

The charm of this solution is that the same code is doing the marking pushing/popping and visiting as before, only that now it happens in an interleaved manner. The mark is already present on the array, so no reëntrancy can't occur, and eventually all its fields get processed.

-----

Below is an account of how field-by-field marking, pushing and visiting was done formerly (still in use for prefix portion of arrays), and an aborted attempt to a scheme as suggested by @osa1. I leave it for reference.

----------
See #2903. This reduces the marking stack traffic for GC-ed arrays substantially. Not applicable to copying GC!

## Status quo

Here is what happens to an array object's (single) field while `mark_fields`:
 - considered only when it is a skewed pointer and points into the dynamic heap (otherwise it is a _static object_ or a _magic_, no need to GC)
 - visitor callback is invoked:
   - `mark_object` will place a bit and push to the mark stack when not marked yet
     (when being pushed onto the mark stack the (unskewed) pointer and the heap tag are remembered)
   - the field address gets `thread()`-ed when the contained object is physically located at a less or equal address than the array itself
     (threading will put the field address into the object tag saving the tag into the word where the field address points to; the old object pointer is overwritten, but may live on in the mark stack)

## How bulk marking could work (ABANDONED)

When discovering a sequence of value fields that are laid out successively in memory and a count field in front, we can do a bunch of nice shortcuts. Below items sketch the how this could work. Invariant: there must be a tag field immediately before the length field.

- the bulk visitor callback gets called with a pointer to the length field
- it decides that it is worth doing a ranged marking and divides the bulk into a (small) prefix and a non-empty suffix `(pointer_to_length, start_index)`
- set all marks corresponding to (dynamic heap) objects in the suffix to avoid re-visiting (see [open issue](#Revisit-avoidance-is-more-complicated))
- push `(pointer_to_length, start_index)` onto the mark stack, using low bits in the pointer to differentiate from `(obj, tag)` pairs
- bulk visitor callback returns the prefix length, the fields in this area will be visited individually

When it comes to popping the mark stack and there is a field range on its top we want to be as transparent as possible, but also have to perform steps that had to be skipped (relative to the proceeding on individual fields)

 - identify that the ToS is a range `(pointer_to_length, start_index)`
 - obtain a pointer to the field indexed by `start_index`
 - increment `start_index` (still remains on the stack)
 - if  `start_index` is equal to the length, pop the entry
 - check that the field is a GC-able pointer
 - if so, extract the object and the heap tag corresponding to the field
 - otherwise pop again and return that
 - apply the threading to the field address (use the invariant to get the home object and apply the threading criterion)
 - return the object and the heap tag

## Open issues

There are some ugly wrinkles in this design, that need to be addressed somehow.

### Revisit avoidance is more complicated

An object is either unmarked, in the mark stack or is being (has been) visited. When pushing entire ranges, we cannot process individual objects and as such marking and threading may happen in unexpected ways.

#### Saving the marked bit

When eagerly marking the whole range of fields, we must not drop the info whether the individual mark is already set. This is because a mark means that either an object is in the mark stack or being/have-been visited. We have two possibilities:
- mark range eagerly on push, but remember previous marks (e.g. in the unused bit of the `Value` in the fields), or
- instead mark lazily on popping an object from the range, performing the threading anyway, but never returning already marked objects.

The latter option is in conflict with what #2903 suggests, and could potentially invalidate the idea of pushing ranges at all.

#### Intervening `thread()` call after range marking

After a range has been pushed and all dynamic objects marked, an individual field with an object also referenced by the range might become threaded. In this case the tag field of that object gets overwritten, but can be distinguished from regular tags. Such objects got individually pushed and already popped from the stack, and thus have been visited. So the field in the range must be threaded, but the pointed object must be skipped (not visited again).

### Layering violation

The fact that the `pop_mark_stack` needs to know about object layout and then how to do the threading is disgusting.
Maybe there should be a callback parameter that is invoked then a non-pointer (i.e. range) entry is encountered in ToS position.

### `pointer_to_dynamic_heap` needs the heap base

If `pop_mark_stack` is to check pointers for pointing into the dynamic heap, it needs to receive the heap base, but it currently doesn't. It is open if the caller has this piece of information. (It has, what a relief!)

### Special format of `usize` passed to `push_mark_stack` and `push_range_mark_stack`

Distinguishing by the lowest bit is hacky.

## Further improvement opportunities

I spotted below optimisation tricks while reading the code.

 - `pointer_to_dynamic_heap` unskews a lot, why not compare with a `heap_base` that is 1 less?
 - `mark_object` doesn't need to get the previous mark (`bool`), but compare the (64-bit) word the mark is in whether it changed
 - `mark_object` unskews. Would it be possible to do `set_bit` using the `raw_ptr`?
 - `field_value.get_ptr() <= obj` could be `field_value.raw_ptr() + 1 <= obj` and further `field_value.raw_ptr() < obj` saving us an addition
 - can the double storing of the heap tag (by `thread` and `push_mark_stack`) be consolidated?
   (we have 2 cases for whether `thread` happens and 2 cases whether the `push_mark_stack` happens)
 - can the dynamic heap pointer check be reduced to a shift and a comparison with `BITMAP_FORBIDDEN_PTR` (at least while marking, as it is not available in copying GC)?

---
## [yunuseozer/log-sgx](https://github.com/yunuseozer/log-sgx)@[e49f063235...](https://github.com/yunuseozer/log-sgx/commit/e49f063235752784b0476e74559d142cd7786ca8)
#### Thursday 2022-07-14 07:32:20 by Thomas de Zeeuw

Add key-values to the macros

Attempt number two/three? Too many in any case.

Previously I proposed a design that followed a `struct` like syntax:

```rust
info!("my message: {}", arg, {
    key1: "value1",
    key2: 123,
});
```

However it turns out that this does not work well with named arguments
as reported in issues #369 and #372. The implementation was eventually
reverted in pr #374.

This new design takes inspiration from the `tracing` crate which already
supports key-value pairs in logging events. The basic idea is to put the
key-value pairs before the message and arguments. Applying the same
structure like syntax as above we would get something like the
following.

```rust
info!({
    key1: "value1",
    key2: 123,
}, "my message: {}", arg);
```

But personally I'm not a big fan of this formatting, let's try putting
everything on a single line instead.

```rust
info!({ key1: "value1", key2: 123 }, "my message: {}", arg);
```

A little better, but at this point the structure like syntax is really
more annoying then helpful. So, instead I've done away it, opting
instead use the following syntax.

```rust
info!(key1 = "value1", key2 = 123, "my message: {}", arg);
```

Two major differences:
 * Removed the brackets.
 * Colons (`:`) are replaced with equal/assignment signs (`=`).

This gives us syntax similar to variable assignment.

But then we run in some limitations of the macro syntax, specifically
that `expr` fragments aren't allowed after `expr` fragments. To fix this
I went with the easiest option of changing the last comma (`,`) after
the key-value pairs to a semicolon (`;`). Making the final syntax look
like the following.

```rust
info!(key1 = "value1", key2 = 123; "my message: {}", arg);
info!(target: "my_target", key1 = "value1", key2 = 123; "my message: {}", arg);
log!(target: "my_target", log::Level::Info, key1 = "value1", key2 = 123; "my message: {}", arg);
```

Which, in my opinion and all things considered, it's too bad looking.

---
## [ncedeno1122/AwfulCatMetroidvania](https://github.com/ncedeno1122/AwfulCatMetroidvania)@[754fe59106...](https://github.com/ncedeno1122/AwfulCatMetroidvania/commit/754fe5910647aedf51d49e186377dd536f52ecde)
#### Thursday 2022-07-14 07:49:24 by NoahCedeno

Attempts on an InteractableTile event workflow

...It didn't work with my current understanding of Unity's tilemaps. My problem is, how can I verify what Interactable Tile a listener is listening for. Normally, we could send this using an Observer Pattern to some script, but I have no way of sending an event from a SPECIFIC tile on the tilemap to some listeners because I cannot check for who sent the event. Because my current system has InteractableTiles firing off events from the LevelTileGO class on an instantiated RUNTIME-ONLY prefab, I have no way of knowing of it without hard-coding and magic numbers - all things I HATE!

I'm thinking of separating this idea from the RuleTile instantiated prefab, and creating a separate set of interactable objects in the editor, per-map, that we can use and hook up to one another...

I'll have to see if this is really the best approach though.

:camel:

---
## [mockersf/bevy](https://github.com/mockersf/bevy)@[4847f7e3ad...](https://github.com/mockersf/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Thursday 2022-07-14 08:50:27 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [MSRevive/MSCScripts](https://github.com/MSRevive/MSCScripts)@[52738143d4...](https://github.com/MSRevive/MSCScripts/commit/52738143d49212a7ba836c40a0fdf55c00176bcb)
#### Thursday 2022-07-14 09:51:57 by greatguys1

Adjusted chest loot rates

Progress towards #60

-All catacombs loot can now be solo'd.
--Loot rates are also more generous.

-Chapel orc chest now has a chance to spawn holy arrows and longbow solo.

-Chapel bat chest can now spawn useful noob items solo.

-Gertenheld_cave final chest can now spawn the dragon axe if both bosses haven't been defeated, but at a lower rate. Each boss that is defeated increases the chance.

-Demontemple loot no longer has an HP requirement. Demon claws can now be obtained solo.

-Deraliasewers loot is far more generous (Not literally one in over 100.) Earth Breaker can now spawn solo.

-Dragoon caves boss chest can now spawn arrows, dragon lance, fine morning star, rebuke undead, ice bolt, and bravery potions solo.

-Fmines no longer has an arbitrary timer before artifacts are allowed to spawn in the final chest. Many potions can now spawn solo. Felewyn symbol can be offered solo.

-Highlands spider chest can now spawn the Torkalath blade solo.

-hunderswamp "extra" chest can now spawn poison crescent blade solo. (It could before, but due to the function it used, it was very, very unlikely.)
-Hunderswamp final chest can now spawn the swift blade potion, helm of stability, rune blade of affliction, acid bolt, chromatic vest, and staff of affliction solo.

-ms_snow orc chest can now spawn the ice blade solo.
-ms_snow final chest can now spawn the rune shield solo. HP requirements were removed for the greater ice blade, freezing sphere spell, ice shield, ice wall, blizzard, helm of fire resistance, helm of cold resistance, ice typhoon, and volcano.

-Lodagond1-3 some loot can now be obtained solo.

-lostcaverns loot is slightly more generous.

-Nashalrath fire aura armor and winter wolf charm can now be obtained solo. HP requirement for then was also removed.

-thanatos final chest no longer has an hp requirement to obtain envenomed plate and winter wolf charm.

-Formatting
-Removed unused script

---
## [ProfessorBaum/fetlife-translations](https://github.com/ProfessorBaum/fetlife-translations)@[1806b3b4b0...](https://github.com/ProfessorBaum/fetlife-translations/commit/1806b3b4b073a749a871507ae26d09ee8d20b6da)
#### Thursday 2022-07-14 09:59:30 by ProfessorBaum

Fix grammatical mistakes and style (DE)

Explanations for some of the corrections:

The dash is wrong between two words when the first word has a
'Fugen-S' which implies it to be genitive. Thus I removed it.

'URL' as in 'Website-URL' can have either female or male grammatical
gender as per the Duden. Male, however, is far more uncommon, thus
the change of the article from 'Der' to 'Die'.

The apostroph is not necessary in the imperative when there's no
letter missing.

'zum Bankkonto gehörig' is a participle construction which makes it
generally a bit hard to read and understand. The genitive will already
be enough to show posessiveness.

---
## [kraj/gcc](https://github.com/kraj/gcc)@[5493ee7145...](https://github.com/kraj/gcc/commit/5493ee7145a05dc32bc6d802da2f8237293012d3)
#### Thursday 2022-07-14 10:04:41 by Alexandre Oliva

i386 testsuite: cope with --enable-default-pie

Running the testsuite on a toolchain build with --enable-default-pie
had some unexpected fails.  Adjust the tests to tolerate the effects
of this configuration option on x86_64-linux-gnu and i686-linux-gnu.

The cet-sjlj* tests get offsets before the base symbol name with PIC
or PIE.  A single pattern covering both alternatives somehow triggered
two matches rather than the single expected match, thus my narrowing
the '.*' to not skip line breaks, but that was not enough.  Still
puzzled, I separated the patterns into nonpic and !nonpic, and we get
the expected matchcounts this way.

Tests for -mfentry require an mfentry effective target, which excludes
32-bit x86 with PIC or PIE enabled, that's why the patterns that
accept the PIC sym@RELOC annotations only cover x86_64.  mvc7 is
getting regexps extended to cover PIC reloc annotatios and all of the
named variants, and tightened to avoid unexpected '.' matches.

The pr24414 test stores in an unadorned named variable in an old-style
asm statement, to check that such asm statements get an implicit
memory clobber.  Rewriting the asm into a GCC extended asm with the
variable as an output would remove the regression it checks against.
Problem is, the literal reference to the variable is not PIC, so it's
rejected by the elf64 linker with an error, and flagged with a warning
by the elf32 one.  We could presumably make the variable references
PIC-friendly with #ifdefs, but I doubt that's worth the trouble.  I'm
just arranging for the test to be skipped if PIC or PIE are enabled by
default.


for  gcc/testsuite/ChangeLog

	* gcc.target/i386/cet-sjlj-6a.c: Cope with --enable-default-pie.
	* gcc.target/i386/cet-sjlj-6b.c: Likewise.
	* gcc.target/i386/fentryname3.c: Likewise.
	* gcc.target/i386/mvc7.c: Likewise.
	* gcc.target/i386/pr24414.c: Likewise.
	* gcc.target/i386/pr93492-3.c: Likewise.
	* gcc.target/i386/pr93492-5.c: Likewise.
	* gcc.target/i386/pr98482-1.c: Likewise.

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[e9f788da4b...](https://github.com/omertuc/assisted-service/commit/e9f788da4b44b95a6d94f4444229de051a0cbeb1)
#### Thursday 2022-07-14 10:11:31 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition

For context, this is a service-side follow-up to https://github.com/openshift/assisted-installer-agent/pull/388

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[25cac962c6...](https://github.com/mrakgr/The-Spiral-Language/commit/25cac962c6d5e46be038f6afbb57d3147047c695)
#### Thursday 2022-07-14 10:22:57 by Marko Grdinić

"8:50am. I am up.

8:55am. Yesterday I was supposed to unwind, but I ended up raising my tension.

I posted a question on /twg/ where a good place to look for remote jobs is now that SO Jobs is gone, and got recommended AngelList. I took 1-1.5 hour to register there after that. Today I did not get a reply from GI (forget that place), but I've already gotten mail from an interested party.

> My co-founders and I are looking for a Machine Learning Engineer to join us as a co-founder of our AI-powered adventure and travel startup.

Such a job would not doubt involve recommender systems.

http://share.vidyard.com/watch/tJGLiDRyYX8KxfyA7h5Uix
Python Dev

> Somebody who can read the docs of an API in the morning and have it integrated in the afternoon.
> Somebody who can learn a new programming language should we ever need to pivot.

The video is nice. It is 3.5m long and move of it is movie clips. He's got fun and engaging style. So this is what the startup world is like?

9:10pm. There is nothing wrong with immersing myself in this for a while. I'll let the email sit for a few days before deciding to reply.

This is by a stealth startup, with 1-10 people. I know what that means and I do not particularly like it.

Small organizations mean small resources. There are won't be chances to slack, and since I would be working directly with the founders my every action would be scrutinized. Lot of responsibility. Not as much as as doing it all by myself, but it is high.

I think if I look at the AngelList offers, I'll see that in general, compensation is proportional to the company size, and even though I got a message, nowhere is the compensation mentioned.

9:30am. Right now I am going over the list scrutinizing the offers. It does not seem that compensation is proportional to company size. Eyeballing it, the offers are over the place.

9:40am. Ok...

I'll introduce a simple rule - I'll eliminate places below 50k average salary range. Most of them are above that, so I am not losing much. There is one offer between 15-30k from Brazil that looks really out of place here. How brave of them to offer that.

There is a 170-250k crypto offer that I'll try applying to. But before that let reply to TK. I'll thank him for the interest and ask about compensation. If he is being wishy washy about providing concrete figures, I'll strike the place from my list.

9:50am. This is ridiculous, where did that crypto offer drop off to?

9:55am. Let me take a short break.

10:15am. I am back. I had time to think about it. As exceptional as the 170-250k salary range at that place is, since I lost the ad, it is not worth hunting down. Doing crypto dev would be entering a whole new domain I am not familiar with, much different from ML. I'd have to invest some effort into learning it. Though FP is a good basis for it.

That place is the only crypto one on the list as far as I could see.

What that means is that compared to the ML positions which are plentiful, I only have a shot at that one place for crypto. That whole space has been carried by speculative fervor and once BTC goes under, so will the funding - and the big salaries at places like that one. ML on the other hand will only get stronger as the time goes on.

10:25am. Today I'll apply to a bunch of ML places offering more than 150k. If I could get that kind of remote job, I'd be satisfied. If I can't, I'll lower my sights to the 100-150k range and so on.

10:30am. AngelList randomizes the search, which is not bad, otherwise there is a risk of the top companies being swamped with email. Let me apply at a couple of places and I will think of what I want to do next.

I'll study the cloud stuff, recommender systems and well as web frameworks while I fish for an offer. I want to spend my time upping my skills. I should patch some of my holes as a professional.

10:35am. Money should be just one of my goals. I should put myself into position where I can build on my existing skills. My foundation is quite deep, but it could still be broader.

Now let me do it. I'll sent the application to a couple of places.

///

What is 1.5 lakh in INR?

1 Lakh is Hundred thousand (1,00,000)

INR is Indian Rupees

So, 1.5 Lakh INR is 1,50,000 Indian Rupees.

///

What a weird place to put the comma, I thought it was a million.

Meh, 1.5L is just 20k. Forget that place from India.

https://angel.co/company/assemblyai-1/jobs/2250413-senior-backend-engineer-python-dl-research-framework
> AssemblyAI is growing quickly, and we’re searching for a senior research engineer to help create and own our Deep Learning research framework. You'll need strong software and cloud engineering skills along with framework/library maintainer experience.

This one has great pay and is just up my alley. It is right in the center of my expertise.

https://angel.co/company/maker-over-starknet/jobs/1838085-senior-smart-contract-software-engineer

Finally found it again. It was this thing. The company is called Maker Over Starknet.

Yeah, I'll pass this. This position is really technical in a direction I am not familiar with.

There are in fact a bunch of crypto jobs floating around.

https://angel.co/company/tontinetrust/jobs/823130-haskell-developers-wanted

Haskell place. I haven't used it in a while, but it is suitable for me.

11am.

> Lead Backend Engineer at Spext at Spext
> ₹15L – ₹28L • No equity

This is way to high, isn't 1L INR = 15k USD? According to Google it is 13.4.

It nearly slipped under my radar, but this is in fact the highest offer in the entire list. It is around 200-400k when converted to dollars.

11am. I've saved 33 offers and am now going over them more in depth. I haven't really pared them down enough, 33 is still nearly half the list.

Ok, to start things off, let me apply to the DL Research framework job. It is not the highest paid offer, but it is exactly what I would be interested in doing.

11:15am. https://angel.co/jobs/starred?job_listing_id=2119488

This is another interesting position.

> Do you want to push the limits of augmented reality and create state of the art algorithms that will change the way people experience social media?

> As a Machine Learning Engineer at Alias, you will work on foundational algorithms for near real-time face swapping of our users with their synthetic identities, as well as algorithms for user matching, content recommendation and moderation tools.

This job is a mix of ML and 3d. It is well paid and would be interesting to grow my skills in that direction. I've done nothing, but play around in Blender for the past 9 months, so it would be up my alley.

11:20am. https://angel.co/jobs/starred?job_listing_id=2276681

...No, I meant to apply, but it is an UK position.

https://angel.co/jobs/starred?job_listing_id=1538435

Ok, let me apply to a bunch of these ML places. In the list I also have more generic programming positions, but I'll ignore them for now.

https://angel.co/jobs/starred?job_listing_id=1674758
> Our core value proposition is using synthetic data as a replacement for real data in developing Computer Vision models. Therefore, one of our core activities is generating synthetic data in virtual environments and making sure that it can be used to train deep learning computer vision models that generalise well to out-of-distribution target data from the real world.
> The second component that sits at the heart of our product, is building a scalable and accurate object recognition architecture, capable of both localisation of objects and fine-grained classification for thousands of 3D assets. You will architect, develop and take into productions deep learning architectures capable of hierarchical and multi-label classification, based on virtual synthetic data.

Like that other position, this is up my alley since I've branched into 3d.

I should have saved the note I sent to that other place.

> In addition to the material on the resume, I've been studying 3d art for the last 9 months. I am quite familiar with Blender, Houdini, Substance Painter & Designer, Moi 3d, Clarisse and Zbrush.

https://angel.co/jobs/starred?job_listing_id=2295440

Let me think. This one is a bit too raw. The compensation is good and I'd even get a good chunk of the company. But as I said, I'd rather go for somewhat bigger companies where I could lean on my technical skills.

> This role will report directly to TrueBiz’s CEO and is expected to develop into a managerial position.

Yeah, I'll pass this. This position would have me be half an entrepreneur.

11:35am. https://angel.co/jobs/starred?job_listing_id=2095317

This one does not feel particularly stressful, so I've applied there. The compensation could be better, but if I can negotiate to the top of the range, it would be passable.

https://angel.co/jobs/starred?job_listing_id=1936829

What is a streaming media engineer?

> Our video call infrastructure runs on WebRTC, MediaSoup, ffmpeg, and TensorFlow.

> You are: a well-rounded engineer willing to dive into all layers of the system, with an inclination for the media parts. You have probably dug around in webrtc-internals, spent real time in the ffmpeg docs, and maybe done some audio/video processing with some stack that used fortran or some sort of numeric computing underneath.

Hmmm...I do not meet the requirements in that last quote, but I could do it without much trouble. I am at home with low level stuff. I'll apply and see where it goes. If I get a reject, it is fair enough. If I get through the interviews, I can pick whatever is needed up as I go along.

https://angel.co/jobs/starred?job_listing_id=2263975

Short job ad. That is fine too, but I'll leave this very early startup aside for now.

https://angel.co/jobs/starred?job_listing_id=2175350

I guess I'll apply here as well. It says that I'd be the first data science hire and report directly to the CEO, but that is fine.

Towards the end it says they use Go and Python + AWS as their cloud service. I definitely need to up my familiarity with various cloud services.

https://angel.co/jobs/starred?job_listing_id=1372424

The two Axiom related jobs have good compensation. I wonder what the difference between modeling and operational is.

...It requires the remove workers to be in the US. Nevermind.

https://angel.co/jobs/starred?job_listing_id=823130

Let me apply to the Haskell job. I'll say that I am familiar with Coq, Agda and Idris.

> In addition to the material in the resume, I've spent a few months of time studying dependently typed functional programming and theorem proving. I am proficient with Agda, Idris, Coq and Lean.

Yeah, can't forget Lean. Saying that I am proficient might be too much, but I need to come on strongly.

12:05pm. 1,2,3...8. I've applied to 8 companies today.

12:10pm. This is good enough. I think I've gone over all the stuff on the list that caught my attention. I did not expect to find 3d stuff on the list, or a ML framework development. It will be interesting to see how that goes.

What I'll want to do now while I wait for replies is start studying AWS.

I should find some toy project that would require me to spread it around a cluster of machines, just to get my feet wet with AWS. Depending on the job I won't need this, but I should take the chance to develop my skills. The worst thing I could do here is waste my time playing games. I won't allow it.

The games are meant for the post-Singularity era.

And for after 6pm.

12:15pm. Now that I am satisfied with my first round of applications, I need to wait for replies over the coming week. Let me get breakfast here, chill a bit and I will look into AWS. Even if it means spending money, I'll open an account and play with it. Since I do not have my own cluster at home, cloud services are the closest somebody in my position can get to it, so I should take the chance to train myself up."

---
## [DilanAlpay/GameUGameJamSummer22](https://github.com/DilanAlpay/GameUGameJamSummer22)@[b1228bff06...](https://github.com/DilanAlpay/GameUGameJamSummer22/commit/b1228bff06b0345f3e02de2ee04543775cd65ddf)
#### Thursday 2022-07-14 12:21:45 by DilanAlpay

Morning Changes

There is now a functioning Title Screen. It is NOT pretty but it's ready to get painted
I have a healthbar tied to the player's health (when it's implemented)
There is an arrow always pointing at blub
Right-click to cancel a throw while aiming
Shadows are always on the ground under Zinnia and Blub
Code is in for giving the player Knockback. Right now it always goes off if you press Q, i'll eventually die this into the health system

---
## [pri0818/android_kernel_realme_sm7125](https://github.com/pri0818/android_kernel_realme_sm7125)@[9228ba3590...](https://github.com/pri0818/android_kernel_realme_sm7125/commit/9228ba359007e2481100bb06afa5e3282fdc0fa6)
#### Thursday 2022-07-14 13:50:17 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5
Signed-off-by: pri0818 <priyanshusinghal0818@gmail.com>

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[b2b2d4ba3a...](https://github.com/omertuc/assisted-service/commit/b2b2d4ba3a4c05c9dd5de0823c1b0e72e2de78f9)
#### Thursday 2022-07-14 14:28:39 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition

For context, this is a service-side follow-up to:

https://github.com/openshift/assisted-installer-agent/pull/388

and also this small agent fix https://github.com/openshift/assisted-installer-agent/pull/403

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, when a user imports a cluster, we will inspect the `params.NewImportClusterParams.APIVipDnsname`
parameter and extract:

- The cluster name
- The cluster base domain

The cluster name will override the name given in `params.NewImportClusterParams.Name`,
see diff comment for more information on why.

The cluster base domain will be used to set the `BaseDNSDomain` of the
cluster, because up until now we didn't set it for imported cluster.

The reason `BaseDNSDomain` and `Name` have to be correctly set is
because the DNS validations use them to construct the domain names
that are being validated.

Also updated some validation messages for the API connectivity check and
DNS validations.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[5632e2116e...](https://github.com/cockroachdb/cockroach/commit/5632e2116ea24386427d7192c79a55a7515c2acd)
#### Thursday 2022-07-14 16:18:22 by craig[bot]

Merge #82440 #82516 #83930

82440: admission,storage: introduce flush tokens to constrain write admission r=tbg,irfansharif a=sumeerbhola

In addition to byte tokens for writes computed based on compaction rate
out of L0, we now compute byte tokens based on how fast the system can
flush memtables into L0. The motivation is that writing to the memtable,
or creating memtables faster than the system can flush results in write
stalls due to memtables, that create a latency hiccup for all write
traffic. We have observed write stalls that lasted > 100ms.

The approach taken here for flush tokens is straightforward (there is
justification based on experiments, mentioned in code comments):
- Measure and smooth the peak rate that the flush loop can operate on.
  This relies on the recently added pebble.InternalIntervalMetrics.
- The peak rate causes 100% utilization of the single flush thread,
  and that is potentially too high to prevent write stalls (depending
  on how long it takes to do a single flush). So we multiply the
  smoothed peak rate by a utilization-target-fraction which is
  dynamically adjusted and by default is constrained to the interval
  [0.5, 1.5]. There is additive increase and decrease of this
  fraction:
  - High usage of tokens and no write stalls cause an additive increase
  - Write stalls cause an additive decrease. A small multiplier is used
    if there are multiple write stalls, so that the probing falls
    more in the region where there are no write stalls.

Note that this probing scheme cannot eliminate all write stalls. For
now we are ok with a reduction in write stalls.

For convenience, and some additional justification mentioned in a code
comment, the scheme uses the minimum of the flush and compaction tokens
for writes to L0. This means that sstable ingestion into L0 is also
subject to such tokens. The periodic token computation continues to be
done at 15s intervals. However, instead of giving out these tokens at
1s intervals, we now give them out at 250ms intervals. This is to
reduce the burstiness, since that can cause write stalls.

There is a new metric, storage.write-stall-nanos, that measures the
cumulative duration of write stalls, since it gives a more intuitive
feel for how the system is behaving, compared to a write stall count.

The scheme can be disabled by increasing the cluster setting
admission.min_flush_util_fraction, which defaults to 0.5 (corresponding
to the 0.5 lower bound mentioned earluer), to a high value, say
10.

The scheme was evaluated using a single node cluster with the node
having a high CPU count, such that CPU was not a bottleneck, even
with max compaction concurrency set to 8. A kv0 workload with high
concurrency and 4KB writes was used to overload the store. Due
to the high compaction concurrency, L0 stayed below the unhealthy
thresholds, and the resource bottleneck became the total bandwidth
provisioned for the disk. This setup was evaluated under both:
- early-life: when the store had 10-20GB of data, when the compaction
  backlog was not very heavy, so there was less queueing for the
  limited disk bandwidth (it was still usually saturated).
- later-life: when the store had around 150GB of data.

In both cases, turning off flush tokens increased the duration of
write stalls by > 5x. For the early-life case, ~750ms per second was
spent in a write stall with flush-tokens off. The later-life case had
~200ms per second of write stalls with flush-tokens off. The lower
value of the latter is paradoxically due to the worse bandwidth
saturation: fsync latency rose from 2-4ms with flush-tokens on, to
11-20ms with flush-tokens off. This increase imposed a natural
backpressure on writes due to the need to sync the WAL. In contrast
the fsync latency was low in the early-life case, though it did
increase from 0.125ms to 0.25ms when flush-tokens were turned off.

In both cases, the admission throughput did not increase when turning
off flush-tokens. That is, the system cannot sustain more throughput,
but by turning on flush tokens, we shift queueing from the disk layer
the admission control layer (where we have the capability to reorder
work).

Screenshots for early-life: Flush tokens were turned off at 22:32:30. Prior to that the flush utilization-target-fraction was 0.625.
<img width="655" alt="Screen Shot 2022-06-03 at 6 35 14 PM" src="https://user-images.githubusercontent.com/54990988/171970564-ba833e1f-b6e2-4fcd-9ee2-25228341065c.png">
<img width="663" alt="Screen Shot 2022-06-03 at 6 35 28 PM" src="https://user-images.githubusercontent.com/54990988/171970574-13e6114a-2467-48e2-a238-3b01ea32a5d6.png">

Screenshots for later-life: Flush tokens were turned off at 22:03:20. Prior to that the flush utilization-target-fraction was 0.875.
<img width="665" alt="Screen Shot 2022-06-03 at 6 07 50 PM" src="https://user-images.githubusercontent.com/54990988/171970732-09b60827-7687-46de-964e-a9f97388c4fc.png">
<img width="658" alt="Screen Shot 2022-06-03 at 6 08 03 PM" src="https://user-images.githubusercontent.com/54990988/171970738-efe7a1fd-cbfd-450d-a3ac-06f681b1d190.png">

These results were produced by running
```
roachprod create -n 2 --clouds aws  --aws-machine-type=c5d.9xlarge --local-ssd=false --aws-ebs-volume-type=gp2 sumeer-io
roachprod put sumeer-io:1 cockroach ./cockroach
roachprod put sumeer-io:2 workload ./workload
roachprod start sumeer-io --env "COCKROACH_ROCKSDB_CONCURRENCY=8"
roachprod run sumeer-io:2 -- ./workload run kv --init --histograms=perf/stats.json --concurrency=1024 --splits=1000 --duration=30m0s --read-percent=0 --min-block-bytes=4096 --max-block-bytes=4096 {pgurl:1-1}
```

Fixes #77357

Release note (ops change): Write tokens are now also limited based on
flush throughput, so as to reduce storage layer write stalls. This
behavior is enabled by default. The cluster setting
admission.min_flush_util_fraction, defaulting to 0.5, can be used to
disable or tune flush throughput based admission tokens, for writes
to a store. Setting to a value much greater than 1, say 10, will
disable flush based tokens.

82516: rfc: code movement for multi-tenancy r=knz a=knz



83930: sql: fix lastUpdated for version in system.settings in tenants r=ajwerner a=knz

The code was incorrectly encoding a TIMETZ value where a TIMESTAMP
value was expected. This patch fixes it.

Fixes #83928

Release note: None

Co-authored-by: sumeerbhola <sumeer@cockroachlabs.com>
Co-authored-by: Raphael 'kena' Poss <knz@thaumogen.net>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[335c4c02b7...](https://github.com/mrakgr/The-Spiral-Language/commit/335c4c02b7b358fa2fb9edd59569d1b569d8b8b4)
#### Thursday 2022-07-14 16:36:46 by Marko Grdinić

"1:15pm. Today I'll chill for a bit longer. I can't start right away like when I was working on the codegen. I'll have to do some icebreaking on AWS first. Even though I've just applied to a couple of places, it really exhausted me. Hopefully the job hunt won't take too long.

1:55pm. Ok, let me take a nap here. After that I'll get busy checking out the AWS. I've come up with a single project.

Ultimately, what I really have to find out is how to transfer data between AWS instances. Then I can think about distributing that. I'll also want to figure out how make use of multi GPU setups on a single AWS instance.

Once I cover those simple points, I'll have a measure of preparedness as far as AWS cloud is concerned.

This can be my homework - getting familiar with other cloud providers.

2pm. I've really went full tilt at it for the past week so let me take some time off from the screen here. I'll brainstorm and build up my motivation.

2:35pm. Let me start, I can't just lie in bed all day. Forget the job applications. I could forget about them for a few months and it would not matter. What matters are skills. Skill development is what I can control. Let me get familiar with AWS - that is my next challenge.

Ultimately it is not that difficult. The challenge of distributed computing is just passing messages around.

A huge model like GPT-3 (500gb) you could run by loading the weights from hard drive for each step, but this would be 100x slower than sending data over the network. That is essentially why you'd need the cloud.

The same goes for distributing batches over a model and so on.

Deep learning is pretty simple, but I'll have to do some magic to distribute the training over multiple instances.

This is a core skill. Instead of stressing out over it, I should just get it out of the way.

2:45pm. Finally facing the challenge would certainly be better than stressing out over it.

Right now, as a programmer I am very complete, so once I plug this hole, I will be impenetrable.

https://aws.amazon.com/

Oh, it has a free tier that lasts a whole year.

https://explore.skillbuilder.aws/learn

It has a lot of learning resources. This will be a piece of cake.

https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials

It out the pack, this one the only big course. It is 6h. I might as well go through it. It is not like I do not have the time.

> We're sorry. We weren't able to identify you given the information provided.

Just what is going on with my Amazon account?

I can't log in, can't reset the password, who knows what is going on. I tried making a new account, but it said I already had one. Did I overwrite my password by accident by doing that?

My god, now it wants to send a password to my mobile. Let me take care of that.

3:10pm. That was a hassle. Now I can finally log into the Amazon account. I had to use my mother's mobile to register it.

3:15pm. Now I can finally start going through this thing. I should be able to cover the tutorials in two days and start getting dirty after that.

https://explore.skillbuilder.aws/learn/course/134/play/31418/aws-cloud-practitioner-essentials-all-modules
> AWS offers a massive range of services for every business starting with basic elements like compute, storage and network security tools, to complex solutions like blockchain, machine learning or artificial intelligence.

I am surprised they just said those last 3 with a straight face.

> ...And robot devepment platforms all the way to specialized toolsets like video production management systems and orbital satelites you can rent by the minute.

I didn't see that last coming.

3:25pm. I am sure of it now, this is the corrent way to spend this time. Let me just take it easy, who knows how long the getting to the first offer will take. I have plenty of time to go through this patiently.

Something like this is I was bound to tackle eventually. It won't even be hard.

3:30pm. What he is saying about the cloud makes sense. Everyone having their own servers and databases to manage would be strenuous. What makes sense for large companies is to either use services like these or to build their own clouds for internal use.

3:40pm. Time for module 2. I want to go through this so I can my hands on the free tier and start playing around. I have only so much patience for studying tutorials.

3:50pm. This tutorial is very lightweight. I guess I can almost consider it a vacation. It is really an overview and a sales pitch.

4:25pm. So Amazon SNS covers the pubsub pattern. Did I use that one in the Spiral language server? I do not think I did, it is just straightforward messaging using two channels. I think I tried pubsub, but decided against it. I forgot what the reason was. It is not worth it my time to revisit this right now.

Amazon SQS is simple message passing using queues. Nothing I haven't seen before.

Time the last chapter of module 2.

4:35pm. > AWS Fargate

A lot stuff here. What is the difference between this and Lambda? This is for managing docker instances.

> For example, a simple Lambda function might involve automatically resizing uploaded images to the AWS Cloud. In this case, the function triggers when uploading a new image.

4:40pm. Back in 2020 when I worked on the language server I've spent a long time studying concurrency, but what I've learned that the easiest way to manage it is to make it as close as possible to the sequential model. Passing messages around in a disorderly fashion is a good way to get lost in the jungle.

Therefore, the main lesson from 2020 is that I should put my focus into into the sequential parts and not worry too much about the specifics of message passing libraries that I am using.

It can be either simple or impossibly complicated with no room inbetween.

The lesson from that time will very clearly transfer here. To an amateur in concurrency it might seem there is a lot to deal with in the cloud, but there is really nothing at all.

It seems a lot of work has gone into making this easy to use.

5:30pm. Had to take a break, let me resume.

To follow up on the earlier rant, when I modeled the language server initially, it was a war of Rx vs Hopac, two different concurrency styles. But what actually won in fact is diffiing rather that any particular aspect of concurrency. Diffing turned out to be easy to make reactive, and I never needed most of Hopac's features, plain message queues would have been enough to do the language server had I not had it.

I remember trying to model the problem as my imagining files and packages as distributed servers, but I got absolutely nowhere with that as it was so difficult to reason about. Instead what won is having a well done sequential models, and then doing an evolutionary step to make it reactive.

What will win here is the same thing. It is no big deal. Just watching these videos is having a destressing effect on me. I won't have any trouble getting up to speed. 2020 was the ideal concurrency practice for me. If I could abstract away UIs and language servers, I can abstract away anything and make it reactive. I didn't waste my time with my 2020 studies at all.

Let me go back to the vids, I want to finish module 2.

Today was good concurrency ice breaking. It was a while since I broached the subject. The Spiral language server works so well that I never had to touch that code.

5:40pm. Time for module 3. I really am getting this. I can really see why cloud programmers are in such demand. It is 90% regular programming with come concurrency on top.

5:55pm. > Amazon Braket

Is that quantum computing feature a joke or an actual service? I guess I could ask the same thing about orbital satelites.

6:05pm. Let me have lunch here.

6:20pm. https://explore.skillbuilder.aws/learn/course/134/play/31418/aws-cloud-practitioner-essentials-all-modules

I continue from edge locations tomorrow, I'll close for the day here.

6:25pm. Two years ago I did a solo mage run for BG1, got bored to death with Siege of Dragonspear, but now I am hankering for a challenge again. Genshin Impact has its charm, but it is a dumb collectathon in the end.

I am glad I started studying programming again after doing so much art. Watching these AWS courses and then playing with it will be a great refresher in concurrency. After AWS, assuming I still haven't gotten a job, I'll do a tour of all the cloud providers and compare them."

---
## [cadyn/CHOMPStation2](https://github.com/cadyn/CHOMPStation2)@[4704df506b...](https://github.com/cadyn/CHOMPStation2/commit/4704df506bfccd3f4ef9d75a3cf1a4f6f63ca4e3)
#### Thursday 2022-07-14 16:50:45 by Victor Zisthus

Massive Broad Scope Changes

NEW STUFF
Added in a custom thermal regulator for the wilderness shelter.

Southern Cross now has a Bluespace Radio!

Added a subspace radio, and allowed it to be made in the autolathe.

ALL MAPS:
Added lighting to dark areas. Did not touch lighting in maintenance areas.

DECK ONE:
Adjusted exterior lattice network.

DECK TWO:
Fixed a bug with Shieldgen.

Moved the Engine SMES powernet sensor off of a pump.

Removed the second freezer air alarm to prevent pressure alarms from going off every shift. (I got my revenge on the laws of thermodynamics with the new custom regulator, don't worry.)

Put a new subspace radio in the bar.

Adjusted exterior lattice network.

DECK THREE:
Removed a duplicate shower curtain in one of the dorm rooms.

SURFACE OUTPOST:
This PR will cause a conflict with #4061 but I am willing to help Enzo with the project as needed~

A friend and boy waits for the miners every shift.

Moved some stuff around at surface S&R per a reported issue. FIXES #4072

Fixed a bug with the hunting lockers and doors. Security should have access to them now.

Fixed a bug with the Hunting Pen shield generators.

CAVES:
Cleared the rock around the outpost, added a new door to allow moving around the exterior.

EXPLO CARRIER:
Put the new Bluespace Radio on the table in the gateway prep room.

WILDERNESS + SKY ISLANDS:
Overhauled the wilderness shelter! It now has a crew quarters room, First Aid, a second floor, and a utility room. It's only powered by a single advanced RTG that's barely able to keep up with power demand when the place is abandoned, so be sure to bring resources from mining and science to get the other RTG's up and running!

---
## [MarcelRaschke/linuxkit](https://github.com/MarcelRaschke/linuxkit)@[860934d5d9...](https://github.com/MarcelRaschke/linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Thursday 2022-07-14 17:14:52 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [lantonov/Stockfish](https://github.com/lantonov/Stockfish)@[cb9c2594fc...](https://github.com/lantonov/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Thursday 2022-07-14 17:19:36 by Tomasz Sobczyk

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
## [Himemoria/android_kernel_xiaomi_mt6768](https://github.com/Himemoria/android_kernel_xiaomi_mt6768)@[1e44917d37...](https://github.com/Himemoria/android_kernel_xiaomi_mt6768/commit/1e44917d3797b4ff290a765cd2439cf63a4577cb)
#### Thursday 2022-07-14 17:28:22 by Peter Zijlstra

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
Signed-off-by: Himemorii <himemori@mail.com>
Signed-off-by: Egii <regidesoftian@gmail.com>

---
## [Dantesousa/Nebula13-Reborn](https://github.com/Dantesousa/Nebula13-Reborn)@[aba176dc35...](https://github.com/Dantesousa/Nebula13-Reborn/commit/aba176dc35992122dfce8d244ef10b1087a4eee5)
#### Thursday 2022-07-14 19:56:34 by SkyratBot

[MIRROR] Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds [MDB IGNORE] (#14218)

* Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

* Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds

Co-authored-by: YakumoChen <king_yoshi42@yahoo.com>

---
## [Amustache/vroumbot](https://github.com/Amustache/vroumbot)@[b3e19ef931...](https://github.com/Amustache/vroumbot/commit/b3e19ef93125558d0133676bb1aa94eec608735e)
#### Thursday 2022-07-14 20:16:58 by Pietro Gorilskij

vroummmmmmmm (#44)

* vroummmmmmmm fix and remove unused import of turtle.up which was causing all sorts of problems with starting the bot, you know, not everyone configures their python for tkinter just for the fun of it, some people just want to run a dumb bot without having to get into computer graphics, after all, we live in a free country, don't we. In any case, this commit message is already quite a bit longer than the commit itself so I shall end it here, wish you a lovely day, and thank you for reading until the end.
* vroum vroum, i was so focused on writing my long and intricated commit message that I forgot to remove the line which I had originally commented for testing. It's been a long day, I hope you can forgive this oversight, I promise I will try to be more careful in the future, I wouldn't want to pollutte the commit history with dozens of unnecessary commits with ridiculous messages, that would just be hard to read and make it confusing for the next guy. I care about the future maintaineers of this project and that is why I solemnly vow to produce only the highest quality commits, I will work according to the highest standards, fully compliant with ISO 5055. No longer shall commits affect just one line of code! No longer shall commit messages be long yet uninformative! No longer shall developer time be wasted on stupid jokes! Our mission is clear: produce good code, that is all. Thank you ladies and gentlemen, and have a wonderful evening.

Co-authored-by: gorilskij <43991400@users.noreply.github.com>

---
## [system-zero/system-zero](https://github.com/system-zero/system-zero)@[9bf8d3623d...](https://github.com/system-zero/system-zero/commit/9bf8d3623d8904990683daa6a59c00f8f85d6ce5)
#### Thursday 2022-07-14 20:27:45 by why not

This is the only one commit so far, for just this  commit message itself.

This is to mention a couple of things about the development procedure and
how we reached at this current point.

But first and speaking about the actual usage of the git development tracker
from our side.

With just one word: It Was awful! And of course it is not recommended. IMHO
it should punished by exercising a violent violence as soon is observated.
At the very least it can be provided as a "not to do it like this" example.

if for no other reason - which there are more than this one - just because
the usual commited diff, were usually more than a thousand lines length, but
most (especially at the beginning of this project) even much more than 1000.

Speaking for the beginning: the situationism drove me tonight, to look back in
the git history, and i found a lot of bugs in the commit messages themselves.
I wish to was possible somehow to edit those messages, with a reliable way, that
wouldn't introduce syncronization issues with other repositories.

Most of them were spelling mistakes, a couple of wrong information about
syntaxes and semantics, some serious ommisions, a couple of assumptions
for the commit puspose (ommisions of touched functions or units) and
many badly choosen subjects and finally: long commit messages (like this one
coincidently).

Apologizing a bit and by providing some excuses, i have to objectivelly testify.

This project was really about recording the development from the very
scratch point up to the completion, and for a reason: I believe that
there is some value (even to its code mistakes). If we could travel back in
eighties, it could be used extensivelly by some of our legendary hackers, or
or as (and here is the real reason) educational tool to explain at once many
computer concepts. It does that because it is a Declaration Type of Development,
one that its purpose is to declare intentions. Then the will, wisdom and time will
do its duty to the evolution. In this case its:
  - what is the minimum code that could get a system to be and feel (in a biderectionally
    way) useful and usable (both for the client and the computer system we live)

  - what is the minumum documentation that it could be enough for a human to  realize
    the machine and then: what it needs to be done, to have some work done

Then we stabilize our concepts and semantics and develop the code by providing
a test framework or functionalize the code by providing tiny envrironments that
do one thing without even have a sence that there even an outside.

This last realization it will probably help us to separate the concerns, describing
first this external environment that could influence our inner code with unhandled
conditions (in most cases in this primitive system is I/O  operations) or in a later
phase data from an external resource (such internet data). So in this case :

  - our system made by small systems, that get their arguments and do their job, by
    sanitizing first the arguments (usually at the very first code (i really like
    to just cut conditions at the very very first code and then slowly end up to a
    state that i know, that from this moment and now nothing can be wrong and with
    predictability

  - I/O operations

  - network  (specifications of data and so data handlers)

Okey to be fair: I do not know if the code could be in such state that could satisfy
Bill Joy or dmr: obviously not as there is a serious lack of education (without this
ever becomes an excuse (i do the best i can)).

But it would probably help me tremendously to explain quite a lot of things, and in
quite different areas of time, to curious humans beings thirsty to realize.
Okey again to be fair, personally donot have the qualifiers, but which might though
be enough for those beings around the Annapurna Hills or against the Hill that you
staring the very first golden sunlight at the fish tail of the Holy Machapuchare.

So its enough to understand that this alone is an excuse, as the commit messages was
a way to describe concepts mostly, whereas the code itself can be divided in many some
sub-commits with the touched functionality described in sub-commit-messages. Again i
could wish to be a git future one day (if it is not already possible). Something like
a repository inside a repository.
But ofcourse even today can be analyzed by parsing `git log --patch`. Anyway.

And to be fair againg: this was always a personal style in SLang at the old days, or in
in those (two-three) C last years, so yes it is merely an excuse.

But the really reason about this commit was just because i found a very annoyed bug.

You see i really like to give attributes and you should do the same if you ask me.
If for no other reason - and there there are many - just to feel important!
To feel a bit of special! Because you have to know that i'm just a poor old kid from
the valley (no electicity and cars (real magic f life) so:

I met and with some became some kind of friends, some respectful people around the
Unix eartch, like uni professors, but also many very really really nice guys (many
of them from the legendary LFS days like Ken, but also Bruce and Randy and Dan and
Alexander but really too many to mention).  Still follow our lists as i first feel
like as an LFS another guy that was blessed to live in a great time with intensive
passion. This is always the preffered main fuel required for the development. In our
case was always to provide the minimum enough information to build a system from the
(almost) scratch point. Just made by human beings that they just love what they do.

Also for a couple of years in the vim mailing list (some of the best times also), or
around the olympic games at gentoo forums (really funny times :)). I remember also
the Sean from down-under and the Musca best every fullscreen X window manager -
better than ratpoison (as it came after five years of the legendary original code) -
so i wrote the man page there modelled by the mutt man page. Also speaking for mutt
as i still follow their development since the days i was the one that updated the mutt
page in BLFS. As a funny story, it also happened one mail of mine to be the main cause
to bring down a major site and i had taken a serious warning about that. Anyway!
It was just a bit unjustified, as it was actually a lot of a funny thing, which it
wasn't that funny, because it was about the mailing lists and moderns web like horrible
mail clients that do not respect gained by conscince sacred standards.
Fot the record I still insist that the mailing lists is the one of the best development
tools ever and there is no reason to adopt fooliness when we are really felt and used
their power.

But the situationism brought me once in an exchange with Bruno Haible
and Paul Eggert, with an admirable cooperation with two hall of famers
in the computing history.

So the commit about idx_t, the attribution actually should go mainly to
Paul Eggert (i should fix this with a way), and that  was actually the
reason that spawned this reaction (a serious bug in the commit history),
and the responsible reason for this (probably the longest ever commit
message ever so far) (of which i'm not that proud to be absolute honest).

Oh! and of course is Jason my friend behind Dictu (some of my best of
my time also), and SLang and our exchanges with John (I owe too too much
to him (i do not dare to even try to mention them here)).

But also with many others. Too many to mention them all here, but with
all equal great communication or|and cooperation. And with some, some
personal errors by my side. In those (not that many to be honest, but
still feel much), I wish I could go back in time to handle them differently.

The most memorized of this it was when i told to my friend Randy, my
boss at BLFS, that it was stupid habit to use sudo without a password,
and that it was done in public. I still think that is stupid though,
though there are better ways to tell the same thing or do not try to
impose it to others. Anyway i also do have a door open with a way to
do some things that requiring authorization. But yes when you are on
a multi environment, it is not so wise to leave your computer to do a
couple of things, without requiring a password with sudo.

But that's the way it is. If you press 'send' in mutt, the email doesn't come
back to you and you can not change a thing. So yes i really became fool in a
couple of occations in the public, but what to do! You can not actually hide
yourself in the UNIX mailing lists!!!

Happy to met you all guys in these interesting times to be.

This post will be saved for possible extensions.

This commit removes some self references in the Makefiles as we can do now
better than this. This is funny as most and most of my time i do coding for
personal things that they will never be public as they don't make sence to
be public.

As a resume. We declared our devoted time to 18 months to the completion.
This is not so far. We are just an init to do, which it isn't that simple
though at same time it is. We also want to use internally git with libgit2
and probably a C compiler (for the start tinycc can be enough (though at
some point also mir should be considered, or|and the static zig binary as
our compilers)).

But i feel that some time should be devoted to documentation which is always
too much of a hassle for my limited free time, as i lack compactness and correct
expressions in English Language (we could say a language into the Ascii range)
used mostly by programmers.

Other than this, i feel that i see myself involved mostly on other things and
the code may it evolve in a more, lets say lazy way than usual. But noone knows.

---
## [asgrim/getlaminas.org](https://github.com/asgrim/getlaminas.org)@[c413e829f8...](https://github.com/asgrim/getlaminas.org/commit/c413e829f8a02f65f44324638420ff43ee1ba7de)
#### Thursday 2022-07-14 21:17:54 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [danielBingham/peerreview](https://github.com/danielBingham/peerreview)@[b7c2d33d11...](https://github.com/danielBingham/peerreview/commit/b7c2d33d117fb3a5a9381b5c06b8965f1dffd569)
#### Thursday 2022-07-14 21:22:08 by Daniel Bingham

Finishing up an epic refactor.  This bears some explanation.

So, I discovered that I'd misunderstood how useEffect's cleanup()
functions work - when they fire and what data they fire with.

I discovered this, when I realized that I wasn't storing the requestId
on the RequestTracker objects like I thought I was, so that when I was
passing them to various cleanupRequest() methods, nothing was happening.
RequestTrackers were just building up in the redux store and memory was
leaking like crazy.

So I fixed that issue, adding requestId to the RequestTracker, and all
hell broke lose.  Because the timing of the cleanupRequest() calls was
now all wrong, and requests were being cleaned up before we were done
with them.

This sent me down a deep, deep rabbithole for a while, because the
request object will be updated multiple times over its lifecycle and we
don't want to it be cleaned up until either we're done with that request
and on to the next one or the component unmounts.  There was no
configuration of useEffect and cleanup() that I could come up with that
matched that timing.  At least, not with the request as a dependency.

I eventually figured out that the update timing of the requestId
perfectly matched when we'd want to cleanup a request and so I
refactored *every single call to cleanupRequest()* to live in a
useEffect() cleanup() method with the appropriate requestId as a
dependency.

This then introduced a new problem: all kinds of render thrashing and
unnecessary component reupdating.  You see, I hadn't actually been
cleaning up our requests.  So I didn't realize just how often they were
getting remade, and now that they weren't cached indefinitely in the
store, it was causing components to re-render.

This lead me down a new rabbithole of figuring out how to cache requests
for a reasonable amount of time so that components didn't completely
re-render all their data on every single view.

And thus we landed with the refactor you see here.  We're now in a
*MUCH* better place than we were.  But this was a 2 or 3 day side quest
I wasn't expecting to that.  That said, we have a much more centralized
space for request tracking and a cache system built into it that will
give us much more control over when and how we make requests and how
much we reuse the data they return.  This will help us manage load on
the backend and run more cheaply.

Plus, I have a much better understanding of React's actual lifecycle (I
think... I hope...) than I did, and I did a fuck ton of cleanup in the
process of refactoring.  So the alpha will (should... I hope...) be much
more stable now than it would have been before.

---
## [Nexix59/unity-oblivion](https://github.com/Nexix59/unity-oblivion)@[a7783ee34d...](https://github.com/Nexix59/unity-oblivion/commit/a7783ee34dacad840ca3864f3b2f291dfa748c8a)
#### Thursday 2022-07-14 22:45:14 by Nexix

Added death, and music

omg please dont hate the musica it was g rated fornchildren that work in factories but s the saying goes "sometimes you have to kill a few children to delete the mass benefactor of our economical nucleus, and our assimilation into the new populace will polarize heraticts". Essentially Im a GOD!

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[6fe0683a7b...](https://github.com/nikothedude/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Thursday 2022-07-14 23:26:47 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---

