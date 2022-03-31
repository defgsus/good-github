## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-30](docs/good-messages/2022/2022-03-30.md)


1,880,448 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,880,448 were push events containing 3,069,225 commit messages that amount to 229,057,445 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [git/git](https://github.com/git/git)@[caac77cc1d...](https://github.com/git/git/commit/caac77cc1d8971be1bedd85fc80c897110b7c2a1)
#### Wednesday 2022-03-30 00:17:32 by brian m. carlson

builtin/stash: provide a way to export stashes to a ref

A common user problem is how to sync in-progress work to another
machine.  Users currently must use some sort of transfer of the working
tree, which poses security risks and also necessarily causes the index
to become dirty.  The experience is suboptimal and frustrating for
users.

A reasonable idea is to use the stash for this purpose, but the stash is
stored in the reflog, not in a ref, and as such it cannot be pushed or
pulled.  This also means that it cannot be saved into a bundle or
preserved elsewhere, which is a problem when using throwaway development
environments.

Let's solve this problem by allowing the user to export the stash to a
ref (or, to just write it into the repository and print the hash, à la
git commit-tree).  Introduce git stash export, which writes a chain of
commits where the first parent is always a chain to the previous stash,
or to a single, empty commit (for the final item) and the second is the
stash commit normally written to the reflog.

Iterate over each stash from topmost to bottomost, looking up the data
for each one, and then create the chain from the single empty commit
back up in reverse order.  Generate a predictable empty commit so our
behavior is reproducible.  Create a useful commit message, preserving
the author and committer information, to help users identify stash
commits when viewing them as normal commits.

If the user has specified specific stashes they'd like to export
instead, use those instead of iterating over all of the stashes.

As part of this, specifically request quiet behavior when looking up the
OID for a revision because we will eventually hit a revision that
doesn't exist and we don't want to die when that occurs.

Signed-off-by: brian m. carlson <sandals@crustytoothpaste.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[55336d1e53...](https://github.com/StarStation13/StarStation13/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Wednesday 2022-03-30 00:24:36 by vincentiusvin

Atmos Control Console Refactor (and syndiebase atmos tidyup) (#65372)

Main Takeaways For Mappers:

Use monitored pathed atmos devices very carefully. Also dont put atmos_sensors willy nilly. They are used to hook to atmos control monitors.

We want to keep at most one device broadcasting for each of the atmos sensor, inlets, and outlets. Run the mapping verb Check Atmos Chamber Devices to be sure, though this might not catch everything.

Some of the warning are pretty harmless. For example if you have reconnected the "station atmos monitor" and you get no listener for distro/waste loop warning, it's safe to ignore.

I don't know what the maptainer policy is on making new subtypes for offstation content, but if you do please branch off the general ones instead of the specific gas ones. If you aren't making a new subtype, varedit the general ones too.

About The Pull Request:

Need Would prefer this to be merged before #65271 (In game atmos guide).
Not strictly necessary, just makes me sleep better knowing the handbook wont die alongside the rest of the UI.

Fixes #36668 (Atmos Monitoring Consoles don't update it's sensors to the new tank after reconnect())
Fixes #32122 (Mix console fucked after reconnecting it)

Also made the distro meter thing broadcast more info instead of just the pressure, because I'm sure nobody would care and it would make my life easier.

A small high-level overview in case this breaks again in the future:

A signal datum (not DCS) is sent by the atmospheric devices (injectors and vents) and will be received by the atmos computers. The data is then stored at the monitor object and then passed to the UI. This initial signal is sent by `broadcast_signal()`, called by `atmos_init()`.

New sensors/vents (if you can actually get them in game, still only adminspawn/wrenchables afaik) will also initiate the conversation if atmos_init() is called, so it works fine. This means you need to unwrench and re-wrench the devices if you adminspawn them though, ugh.

In case of a newly built computer, it needs to be the one that prompt the data to the devices, so we send a request signal. This is a bit inefficient since it doesnt work off of callbacks and assocs like DCS, but won't really matter since we're doing this rarely.

We only talk with the injectors and vents when necessary here, while sensors and meters keep beeping with every process_atmos() tick so they rarely break.


Why It's Good For The Game:

Messy code gone (debatable).


Refactored the atmos control console devices. The ones that hook to the big turf chambers.
Distro meter now broadcast the whole gasmix info instead of just pressure to the monitors.
Lavaland syndie's atmos chamber vents are now actually configurable. Moved a few things around to accomodate this.
Lavalannd syndie chambers hooked to distro and moved distro pipe to layer2
atmos monitors can detect reactions now.
Some minor code changes to how anomaly refinery and implosion compressor show the gas info. No changes expected, report if bug.
recoded checks for atmos chamber abnormalities in debug verbs.

---
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[d105f7279e...](https://github.com/RedDevilus/pcsx2/commit/d105f7279e31339c2f896f83e4c1284b1abd9142)
#### Wednesday 2022-03-30 00:28:23 by RedDevilus

GameDB: Serial with ':' to '-' + GS fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [acramernc/babot](https://github.com/acramernc/babot)@[ae61ed0130...](https://github.com/acramernc/babot/commit/ae61ed013030f9d70fb1379ba3445708747d6984)
#### Wednesday 2022-03-30 00:41:05 by KittenMoon

minor fixes and changes to the in depth thing that ias the bot and now all command work goodly wow how many characters can i add before it will get mad at me, it seems that there might not be a limit but who is to say, i wonder how this will look with the vs code github who commited what extension, alas i will now infom you about jobless reincarnation- it is a good watch and i cant wait for season two but i am sad there will be less Eris in it but that just makes the scenes where she is in the episodes so much more special (i tell myself), well it is 1:36 am on mar 27th and tomorrow will be the big day that hank will update the bot to slash commands and it will be done the day after he had to write a paper. fold orbs. i cant waiut for s3 of dr stone as well but i will spare youi the details ats it is getting cold in here due to the wind. now when adam sees this he will probably go insande but alas it is fine. this is a second go at this commit because i realized it could be longer and i wanted to make it as long as physically possible ecause it owuld be funnhy. so iu also wont remove spelling mistakes lioke yoy just saw, unless it makes the word unreadable , i have standarrds, low standards, but standasrds none the less.. to whomstvst that is reading this, good work getting to here as i am realluuy rambling now and it is good. !baba please is working well and we have only gotten one Nice from it so far but im sure there will be more in the future. Today i was grading labs and Bennis decided to send a .pages file and those who get my pain should understnad that it is not easy to open that and i had to just put it off untl the morrow days (aka Mar 27 during the day). But it is fine, i may have forgot that genshin has been open for the past 9 hours but it is fine. Bikus. see i had to get that in there or it wouldnt be a message by me, which reminds me, Nw forgs sponsored this commit message, make sure to look out for NW forgs sponsored content coming soon. so, how is your day person who is reading this, mine went well, i went to the store to go Schop Schoping (read in swedish accent) and had lunch then did hw, watched yt, and coded the code you see somewhere nearby. Speaking of code, hey buddy 🔪 has decided to make my life a living pain as the cube wont scale correctly but it really isnt too bad as i am ahead of the class by a bunch so i can take it slow and smooth. ඞ! suprise mogus! back to hey buddy rant: i will just ask him what is wrong on monday but the problem is my class ends at 12 and his office hours are at 2:30 so that uis 2.5 hours of waiting (2 if you subtract lunch). oh boy is it windy out, room at a solid 57 degrees, which is nice. i should end this rant soon but i dont want to do that becuse i want to write mor words than hanks whole paper into this commit message. ok back to jobless reincarnation rant: so the first few episodes are basically the main charcter learning how to do magic in the new world he is in as a child, he also has a special ability to do chantless magic (most magic requires spells), so the family get him a tutor and she is a demon who teaches him how to better hone his magic abilty and he soon passes her. she leaves to the main characters disaray and then he finds a new friend who he first thought was a guy but was a girl and they become friends after a rocky start. she can also do chantless magic which might be someting for season 2 but idk, ,my one friend said something about that. but back on topic, he asks hsi parents if he and her can go to magic school but the dad says they dont have to money for both so the MC (main char) says he will get a job to pay for it. so the dad does what any norrmal dad would do, knocks out his son and sends him off wiht a beast-woman (member of beast people, comes bakc later) to train a bratty (but best character) girl magic oh and the beast girl. the first day results in a kidnapping that was supposed to be staged but in the end it was an actual kidnapping for ransom but both MC and main girl got out alive because beast woman saved them. Then months pass as they train and get better with magic and there is a bday party for the girl after the MC had to help teach her to dance. at this point in the story main girl doesnt like MC that much. then there is a 10th bday for MC and he gets a new staff as he is a mage and it helps enhance his magic, aorund this time there is a magic orb in the sky that no one knows abotu that much, we skip ahead to graduation for main girl and beast woman and when MC goes to cast the cumulonimbus spell there is a massive explosion from the thing in the sky and it causes the MC and main girl to teleport together somewhere, the beast woman also gets teled but somewhere else. They wake in the demon lands next to one of the demons that were told to eat people but he is actully not that bad and they decide to travel together to get out of the demon lands. first they stop at a nearby village which is home of the mage teacher thath MC had a few years back. They then travel on the way to a city nearby where they will go and sign up to be adventueres. when they get to the city they realize the demon wont be able to enter due to being hated so they dye his hair blue and hide the forehead gem on him. while there the MC is visited by the Man god in his dreams and is told to take a quest to save a pet, this leads them meeting smugglers which the demon kills one and the MC gets mad and tells him that wont clear the demons kind's name. so they then go on a quest to kill a snake and due to the MC hesitaion they witnesss a fellow adventurer die. this leads the MC to second guess himself but they still kill the snke, they head back to the town and the horse man tries to extort them but they dont take kindly to it and the demon shows who he really is then leaves the town. later the MC and demon agree to work together and the demon shaves his head to blend in. then then travel across the demon lands to the nearest port town where the demon is the reason they cant cross on the boat as he costs too much to travel. that night he is met by the man god again and due to that he goes off on a solo adventure that day while the girl and demon practice fighting. he then meet shte demon queen and she gives him a demon eye which lets him see seconds into the future and forsee events to come. he then meets Gallus by saving him due to the eye which helps him get a way to get across to the next continent. INTERLUDE TIME; we go back to the start of the day where we are now in the mage teacher POV with the elf and dwarf. the mage girl goes all around town looking for leads on what could have happened to all of the MC family. she explores the town that the MC is in but due to conincdences they never meet. the alley w/the demon queen and when the others are training could have been when but it didnt occur. So they make it to the new island and when they get there as a deal made with the demon, who hates evil people, they would defeat the smugglers who helped them get here. they saved the beast children and the sacred beast (a big dog) but when the MC was saving the dog, the people from the beast village showed up and they took the MC into prison for many days. but then there was an attack on their village and the MC and his innmate (who will be important later) get out and help the beast people and save their village. then the main girl and demon come back and then they live in the beast village for a while. the main girl helps train two of the children who they saved and coincidentally is the family of the beast woman from the start of the season. they had disagreements about her as when she left the village she was not a good and well manored person but that is not how she is now. months pass as they get trapped by rain at the place and train for that time, but then it is time for them to leave for the capital city. They eventually get to the capital city and they decide to seperate for the day as they all think it is good to stay and raise funds for their adventure back home. the MC goes on his own way and the demon and girl go on their own ways as well. *the girl has an episode at this point but it was just released and i have yet to watch it* so back to MC: he finds a child being kidnapped and goes to save it but there is complications as he runs into his father Paul and they have a not so good reunion as he says that the MC is having way to much fun when he should be looking for his family. this leads to a fight and they go back home on their seperate ways. flashback to the explosion from earlier and we see how paul and his daaughter are together as it hits them causing them to teleport somehwere and they end up going home seing it is gone and posting flyers adressed to his family and friends to help find each other. this results in him eventually going to where he is now. he then talks with another person (same dude who was in the cage in beast lands) and he explains that paul and MC are family and they shouldnt be fighting like this. They both go to a bar together and redo their first meeting which results in them being on better terms, like a father and son shoudl be. They then go on their seperate ways and the MC taks a ship to the main continent; INTERLUDE- cutting back to the mage girl, we see she is back at the town in the demon land talking to the horse man, who was her former traveling compainion, and then she goes back home for the first time in 20-50 years (this type of demon lives very long and ages SLOWLY). she gets there and is hesitant because she left as she cant use telapthy like the others but then goes to her family home and they dont hate her liek the thoguht. this leads her to stay and learn about the MC's travels and what he is up to. back to MC and he again has a dream with the Man god who tells him that how to save his other sister and their maid (odd family tree, we wont get into it) and then he goes and does it but it leads him to the castle where he thinks his former master (the mage teacher from just a bit ago). he then gets captured as the corrupt prince hopes to get the teacher to come back but he is able to escape thanks to the prices brother likeing the MC;s figures he makes. They then save both who they were trying to save and it resulted in them parting ways in which the maid went to head to paul. brief introspection: the sister disliked her brother (she was 2 or 3 when the tele happened) but the MC (brother) saving her helped rekindle that relationship. They continue on their way into the dragon lands in which the demon and girl freeze up as the dragon man shows up. he is ominous and causes peiople to be scared of him due to a curse he has on him. everything was going to go fine until the Man god was brought up and it caused the dragon man to try and kill them, he basically did kill them all and in the semi dead state the MC talked to the man god a bunch about how he didnt want to die from this second chance at life. but then he wasnt dead because of something the dragon mans assitant said to him and he revived both him and the demon who was basically killed. They finally reach their home territory and and see how everything was destroyed as said by paul due to the mana explosion. they bid farewell to the demon at the MC hometown area as he was able to fufill his promise of getting them home safely. then they head to the girls town and see it is a refugee camp and they meat the beast woman again. it is confirmed that the girl is the last of her family as her parents died in the teleport and her grandfather was blamed for it all and beheaded. the girl goes off to be alone for a bit and the MC goes to think of what to do next. they then do some stuff and then it is the next day and the MC is very estatic to start the next adventure to find his mother. he then relizes that the girl is gone and goes to ask the dude in charge where she went. he says she and the beast woman went off on an adventure to learn to be independant. the girl also cut her hair (imo not pog, but alas). this causes the MC to recolect on his past life and how his shut in nature is coming out again after he tried so hard to start anew. while he recollects on his life sulking in the bed we see glimpses of all the characters who he helped along the way. one being the mage teacher who watches a beer chugging challenge between a demon queen and a dwarf. to suprise the demon queen wins but cant afford to pay for it but before anything bad happens the mage teacher pays for it which gets her a favor from the demon. she asks the demon to see the MC family and where they are finding that most are safe except the mom who is in an unknwon location and she cant get a lock on the MC (theory about this after). cut back to the MC and we see that he is still the big sad but the thought of his mom breaks him out of this where she wouldnt want him to be a mopey. then we see him leave the tent ready to go on an adventute. the final scene is a scene of the girl he became friends with as a child much older in some unknown place. and that was the story of jobless reincarnation season 1. now the theory i have is the MC has a curse/blessing (smae thing just positive/negative) that he cannot be seen by others using magic, as the dragon man didnt know of his existance while knowing of his compainions and the demon queen didnt see him when helping the mage teacher find his family and him. but im sure we will find out eventually. now the time is 2:47 and as you probably see it is over 1 hour since i started typng this commit message and i have no reason to stop other than if i get really tired. so i guess slash commands they are pretty cool but whos to say. the bungle bus would be flying right now and i wouldnt have been typing this if the space engineers server was up but alas it is not :(. so i converted this commit message (well everything before i say the time) into a double space times new roman 12pt font word doc and well, 6 pages of text, oops, i may have over explained it but to anyone who read it good job i guess i spoiled the show but those who are in this baba project with me wouldnt watch it anyway. also i assume if they woudl it would they would stop when i said i would go on a rant ¯\_(ツ)_/¯. i had to get that from a slash command on disxcord, very topical to this commit. hey i guess i should do the daily wordle soon or i can jsut do it when i wake up tomorrow but that would be more logical and i am not logical as u see i am writing a book as a commit message. whelp my headphoens are low battery which means this commit message will ahve to be sent soon, but i may come back in the morniung and append onto it more, all until hank returns from work and we do the great baba slashening which will be a bit of a pain. !baba please be simple. i see you asking why is this so long, what went thought this mans head making him go, ima spend 1.5 hours writing a commit message, well you knwo, idk what to say to that as even i, the one writing this dont fully know why i am doing this but i do know that if my headphones werent dying i would possibk explain a full or partial rant about dr. stone. have you heard about the great cup of gilgamesh well it is a nice cup. also make sure that your orbs get the propoer folds when dealing with them, ah that reminded me of hey buddy and the program i need to work get working, thanks me. the temp in the room is now 55 which is nice but for some reason it feels warmer than when it was actually warmer, mahybe that was due to me no having typed a full essay back then but who is to really say. see i cant write a paper to save my lfie but i can rant random words for a long time until i have nothing to say. so how are YOU. yeah you mr. i have read this full commit message and regret it so because i wont get back the [insert time spent] [insert time type] back. so i have had this same song on loop for hours now and well it is very peaceful as a background song. NOOO i am now alone in the discord after both Bob and Isaac left without warning :(. well i guess it could ahve been a netwrk issue but idk i guess i will just continue my rants. this song is very entertaining and it be real nice. the wind is still roaring outside like it was back a bit ago and it do be loud, there was a very loud wind noise last night that woke me up but luckily i was able to fall back asleep due to only getting 5ish hours the niught before. well my time might be coming to a close as i am getting tired (not of ranting, i could go much longer but tired as in low wokeness levels). if you see a message saying - ha im not tired - but in all caps that is where i will continue tomorrow (that is if i remember to start it that way) even so it will be obvious. would u believe i have genshin still running ,yes, well i guess that is normal for me. i guess i should actually close it, there i closed it, are you happy, well now i am actually going to go to bed at the time of 3:08am, i bid you a morrow (maybe there will be more) Ha you are correct there is more and now that it is a new day i have new motivation to continue this as the alternate is that i would be grading more labs which i know i should do but Bennis is causing me issues witjt rhe .pages files still but alas. also the info sent to me was not the most accurate so it takes energy to think and i just woke a bit ago, now the sauna mode is being enabled by dumbo boi and but i cant just go turn off the warm as he is out there so i must wait a bit of time, alass. baba haikus now work as intended for dates, idk if i included that in here but if i didnt then well here it is now. so for you it has been only moments but to me it has been a whole night since i wrote the jobless reincarnation s ummary, i regret nothing that i did last night i may have been a 'waste of time' but i had fun, it is the rant i wanted to give but no one would listen so now it exists in text form and if thou wantst to hear the audio version i shall give the rant at anytime. if you get to this part send a 'real frog bungus' in general, and i will know :) ---- so the temp in the room is at 57 again but with tthe heat on it will not stay so nice for that long, i can feel it on my fave and it makes me the big anoyed. when i commit this fully it will great but that time has yet to come as i still have the rant ability going and i aint stopping it anytime soon. i can feel the text box being slower as it has to hold alll 17k+ characters before this and however many more that there will bit in the future. well as i was saying last night somewhere in that rant. i should probably do todays wordle, the hank version that it. Wordle 281 3/6 🟨🟨🟩⬛⬛ 🟨🟩🟩🟩⬛🟩🟩🟩🟩🟩, there you go the wordle. you should know that that isthe first thing that has been copy pasted into here (other than the two emois) as this whole thing has been typed out character by character by me with no prefoming a Daniel (copy-pasta). i think i will keep going witht this rant for another day or two if hank ends up not being able to update tonight as he hasnt slept in over a day due to a paper that he must write, and tomorrow there may not be time for the update meaning the slash commands update will end up being on the tuesday this week. speaking of tuesday that is the day of the genshin update and oh boy am i excited, only downside is that i will only have 2 ish hours to work on it as i got class at 10 so i must sleep by 1am. but oh well i cant wait for the chasm and what it has to offer up. also new story quests and archon quests that will potentially get done later this week, i can hope as long as there is no hw/labs to deal with more than i already have which knowing my luck it will end up happening. alas, 🐸🐸🐸. hey we just hit the jobless reincarnation part of the song i am listneing too, nice!. baba told me one, how are you feeling, and i told him, that i am feeling like taking a flight in the bungle bus, ha i got you this was just a ploy for me to mention the bungle bus and it worked. the end of the song is occuring and it truely is a bop. so the plan for today is to do hw/lab stuff, and then do the baba slash update that is if hank isnt sleeping when the evning comes and adam hasnt gone to sleep too when he wokes up. so i hope that genshin gets an update to 3.0 in the next update (not the tuesday one) becasue that would be super great. it would also line up to where i would be done with classes at that time which would allow me to deal with having time to do the genshi update while also having time to do summer shows 2022, which hoepfully that show list will be on par or even better than summer shows 2020 and much better thant the dreaded summer shows 2021 which was like drinking bleach, in reality it was watching bleach but who is keeeping track, oh wait i am. but the good thing is i have no promises to bleach so i will end up hopefully doing a narrowed down spring break scheule as i hope to get through 24 episodes a week. the good thing is if we corelate it to the summer of 2020 we see i watched a whole GTARP livestream each day and still had lotss of time for shows so i have hope for goodness but we will see what the scheidule will be. currently i must finish slime then we can start the true sthows list which includes AoT, Fate movies, drss up darling, and more hits. it should be good. i also would like to see the air date for job re. s2 to be annoucned so i can get hyped for its inevitable airing. mayhaps over the summer i will also watch the OVA but we will see as i need to time it correctly. as you probably can tell i am starting to run out of ideas for what to add here but that is not ture, as i could do another long rant or short one on dr stone like i said i would which depending on if adam gets done with being at the jesus shack teaching the children about NOT frogs then i will have time to do the rant. ok here goes nothing, see unlike job re. i watched dr stone back in jan 2021 and s2 in august so it isnt as fresh im my mind so it wont be as detailed. so we start off on some day when the main character the scientist is at his school and his best friend is about to ask out a girl. then a giant green wave covers theentire globe which causes all the people to instantly be petrefied in stone. 3700 years pass as everyone is still ins tone but the main char wakes due to a chemical reaction occuring on his body which results in him having to live in this new stone world. he then finds his friend and saves him and the girl as well. they live their days out in a trehouse tying to find the best way to save all the humans which in the end they figure out. they then save the stongest student at the school and he has different morals and doesnt want to save all of humanity as there were too many corrupt people, time passes and they end up dueling which the stong man kills the main character but because he is smart he was able to be revived due to being still partailly petrefied on his neck where it was broken. this leads tohe MC to sperate and MC goes alone while the other two go with the strong man to keeep the illusion he is alive. the Mc adventures out for a bit and finds humans living in this world who are decendants from someone but he doesnt know who. they are skeptical of him and his science but they show him to their local 'scientist' who they work together to bulild a kingdom of science. the next part of the adventure resolves around trying to make a drug to help cure the sick of the village and earn their trust but they need helpers so they make food that is unknown to the people of the village which works to persuade them to help. a man from the other empire shows up and he is going to report to the empire about how there are people and they need to bedestory but he is persuaded not to by the fact that they have so many inventuons including light. andas he is leaving he requests one thing: a cola. they continue on their creation of the drug to save the villagers but in order to be able to give it to the sick they must get through a tournament arc which results in the MC winnning and becomeing the new chief of the village, the reason for the competing was because of needing alcohol whcich would be used int he drug being made, then they give the drug to the sick and after a moment of panic all is well and the village accepts the MC as one of their own. but in a plot twist the village name is named after the MC. we now flashback to the past when the MC was young and he was with his adoptive father and how he wanted to be an astronaught. over time he was able to go into space and on this mission there were 6 people up in the space statuion. days pass up there and all is going well when the petrefecation bean goes off and they do not get frozen but all communications are gone. the mc father decids that the best bet would be to return to earth and try and recover all life somehow. cpntinuing with the past we learn that their re-entry is not so smooth but they all successfuly make it to an island and that is where they will be living the rest of their days. as time passes each pair get married to each other and they have familys there but when one gets sick then dies the russians deide to try and go to the mainland to get mediceine but are never seen from again. the father decides to write 100 tales to tell the decendants to keep huminty alive but tragically his wife dies when he finishes writing them. back in the future we see the Mc at the grave of his father reminising and vows to keep alive the science. then the cola person shows up and says the empire is planning on coming to attack. they send a strike team and due to their science advancements they are able to hold them off and also they give cotton candy which appeases one of them for now. they end up celebrating christmas a bit due which improves their morals and after an event int eh cave they end up making a room and telescope for the MC as a birthday gift. finally as the season comes to a close they decide to make a phone or a primative one to be able to communitcate witht the allies they have in the empure. in this the MC learns they have the term speaker as a bee whiuch leads them to investigate the grave of his dad and find a recrd in there which brings to lite somethings and a some left by the girl who was a singer back then. then they have to make a second one but that is doen between seasons . season 2 starts with them making instant ramen based on what they made before. they end up taking the second phoen to the enemy bas e and hide it so they can communitcate with the allies, there is a hiccup in there is aguard but she gets convinced because of the music from the end of s1. they then plan on making a car of sorts which can be used as a tank as well to storm the base and save their allies. basically the rest of the season they go to save fight the empire they win the leader admits he is wrong but is fatally wounded and needs to be put into some form of cryo sleep which is done. also we learn that the girl was saving all the people that the evil leader was 'killing' and that she could save them 100%. and that is a rough summary of what heppended, it could be more in depth and s3 isnt until 2023 but at lead thtere will be an interplaced epiusode sometime this year.. so now you have read two, yes two summarys of shows i have watched, if it wasnt for the fact that this text box was getting visibly laggy to type in, i potentiually would do a railgun talk but i will spare you the hastle and just say, go watch it, it is good. fun fact the slash commands update is coming one day before the birthday of babs on the server which occured 3 years ago. wo wow has it really been that long, it was also the day we added haiku bot to the server, good times good times., well, i think this is the end. of the commit message that is until next time when i feel the need to do this again, but getting it this long a gain will be HARD but we do have many shows i can go though and there will be many more i will watch, just see job re. s2 i will have to over explaint hat one too. so unless you see more after this as in i felt like continuing later today, i bid you a morrow for this message. ---- well well well, looks like i am back to type some more as hank was too sleepy last night to update the bot. so now i am in my class typing more on this, learning about compliments of turing machines. today eneded up having no class with hey budward as he has a stomach bug and didnt show today so free time is nice i guess but the only down side is no ablility to ask him the questions in person. so i guess email will be the way to do it. i have yet to eat lunch today and am the big hungry and the frogs are wanting to be fed, that probably makes no sense but to those who know, they know. good thing is i will speedrun lunch, then go to apartment and do some more lab grading which should be 'fun', oh boy i cant wait, well i may watch some YT before that as i would like a break from brain being used. it truly is real frog hours. i did end up having to add a change to baba today as there was a bug with the eror frog and at least there is one good thing to not being able to update the bot yesterday. but still i would like to do it today but cant because the one the only adam is too busy with work and his other activity in the eve of the day.today has been fairly windy and as i predicted last nivght, i was only able to wake today because i went to bed early because oh boy was the bed cozy in the morning. dj bungus is the driver of the bungle bus. today lunch will be chook fi loo and oh boy will it be good to have food after not having breakfast. see i gotta get the amount of characters in this to over 30k which would make it a nice even amount and also be very satisfying. but we are about to go into group work soon so i will have to take a break from the typing here to 'work' on problems with people. will i contribute, probably not one bit as idk what is going on. of the three classes i am taking hey buddys is the only one that peaks my interests while the other two are good but not prime time mime crime time classes. whelp we have gone over 30k swimmingly which means i shall be gone for now and if this is the end then goodeth morrow until next message. --- well looks to be that  i have added all the admin commands as slash commands now, who would have thought that, but it will be pused tomorrow which will be in the evning wait tomorrow is tuess so i am free all day whcih is pretty poggers. ok that was all fro my update so see you again mayhaps perchance idk. --- ok today is the day of the bot upate, we shall be getting anew command system and all that stuff., also i have an update on the hey buddy program stuff which is that i passewd all the tests and now am done with the lab. so tomorrow gonna be a smmoth sailing day of peach and prosperity with a little bit of frog. now genshin is in the update stage right now so the ext few hours will be me doing not much as i wait for the changes to occur, we will see as the update has new stuff including the chasm. i will do a single 10 pull today possibly but if i wait until friday when the new month arrives i will not use as may ruples, but then again i will new use the same amount so it really doesnt matter if i wait or not as i will want to do a 10 pull anyway. so i want to get me some dinner but that would involve moving from my chair which is nice and cozy., the soluction to this issue is having some of the snacks on my desk which i might as well do right now

---
## [Aconka/babot](https://github.com/Aconka/babot)@[183d89af66...](https://github.com/Aconka/babot/commit/183d89af66503ebf9b4ec4dac851c4101537b2d5)
#### Wednesday 2022-03-30 00:49:26 by acramernc

Reverted back from type:module bs (I hate my life)

---
## [Sedna-Games/Zero-Possession-Prototype](https://github.com/Sedna-Games/Zero-Possession-Prototype)@[5728d2d81c...](https://github.com/Sedna-Games/Zero-Possession-Prototype/commit/5728d2d81c1408e5e97f6d439c1e65cf95e6c402)
#### Wednesday 2022-03-30 01:24:06 by Hamraj

[WIP] First 3 Buildings LD Set Dressing Good

- holy fuck takes time to get these done and think of cool designs for the levels and make shit interesting but its getting there bois and gals

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[e58fb506ef...](https://github.com/san7890/bruhstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Wednesday 2022-03-30 01:24:33 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[c8ef62c1fb...](https://github.com/timothymtorres/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Wednesday 2022-03-30 03:07:02 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7db916a944...](https://github.com/treckstar/yolo-octo-hipster/commit/7db916a944e92708beb47785f8fee8790af7c39e)
#### Wednesday 2022-03-30 03:45:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[bb9f31968b...](https://github.com/treckstar/yolo-octo-hipster/commit/bb9f31968baf047c9962fa9602de175add873544)
#### Wednesday 2022-03-30 04:00:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ianjoneill/terminal](https://github.com/ianjoneill/terminal)@[855e1360c0...](https://github.com/ianjoneill/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Wednesday 2022-03-30 06:04:12 by Mike Griese

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
## [quantum5/magic-trace](https://github.com/quantum5/magic-trace)@[218950a0a3...](https://github.com/quantum5/magic-trace/commit/218950a0a3e46aa98f09b2697026a43113dccff3)
#### Wednesday 2022-03-30 07:25:48 by Clark Gaebel

Rework trigger modes

Replace `-symbol` with a "trigger mode" option. To quote my own help
text:

1) If you do not provide `-trigger`, magic-trace takes a snapshot
   when either it or the application under trace ends. You can Ctrl+C
   magic-trace to manually trigger a snapshot.

2) If you provide `-trigger $`, magic-trace will open up a
   fuzzy-find dialog to help you choose a symbol to trace.

3) If you provide `-trigger <FUNCTION NAME>`, magic-trace will
   snapshot when the application being traced calls the given
   function. This takes the fully-mangled name, so if you're using
   anything except C, fuzzy-find mode will probably be easier to
   use.

`-trigger .` is a shorthand for `-trigger magic_trace_stop_indicator`.

This also removes three command-line arguments that are, in my opinion,
a mix of unnecessary and probably a bad idea to expose:

- `-delay-thresh` can be replicated by an applicationg doing this
  measurement itself. It's a very cheap operation for an application
  to add, I don't think that magic-trace is adding very much here.

- `-duration-thresh` is in the same boat as `-delay-thresh`.

- `-immediate-stop` causes issues on some kernels. Let's just remove
  it for now and revisit it in a couple years. If people actually
  want their trace to end exactly when the trigger fires, we can
  postprocess the trace output.

Please play around with this! I think it's a easier to to use... but
that's just like my opinion, man.

Fixes #60 and #69.

---
## [svitalis123/alx-low_level_programming](https://github.com/svitalis123/alx-low_level_programming)@[4d8002ab2e...](https://github.com/svitalis123/alx-low_level_programming/commit/4d8002ab2eb2f47deb51e80fb0db8a01e82c62f8)
#### Wednesday 2022-03-30 08:07:10 by svitalis123

She locked away a secret, deep inside herself, something she once knew to be true... but chose to forget
. Why is it so important to dream? Because, in my dreams we are together
Dreams feel real while we're in them. It's only when we wake up that we realize something was actually strange
 You mustn't be afraid to dream a little bigger, darling
Once an idea has taken hold of the brain it's almost impossible to eradicate
Your subconscious is looking for the dreamer
. Inception. Is it possible?
They say we only use a fraction of our brain's true potential. Now that's when we're awake. When we're asleep, we can do almost anything
Inception. Now, before you bother telling me it's impossible...My primary goal of hacking was the intellectual curiosity, the seduction of adventure

---
## [ghostwriter/laminas-org-laminas-diagnostics](https://github.com/ghostwriter/laminas-org-laminas-diagnostics)@[a34a6beb07...](https://github.com/ghostwriter/laminas-org-laminas-diagnostics/commit/a34a6beb07b4703bb282c6b3c0e2b52b0a0e59f8)
#### Wednesday 2022-03-30 08:46:14 by Michał Bundyra

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
## [SleepyBear96/incubator-doris](https://github.com/SleepyBear96/incubator-doris)@[ef2ea1806e...](https://github.com/SleepyBear96/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Wednesday 2022-03-30 09:29:51 by HB

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
## [chaldeaprjkt/kernel_xiaomi_vayu](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu)@[02c470ebcf...](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu/commit/02c470ebcf0c7c4ce29f4856ae1a0348e782dc8c)
#### Wednesday 2022-03-30 09:32:16 by Peter Zijlstra

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

---
## [Samarth-Khatri/julia](https://github.com/Samarth-Khatri/julia)@[62e0729dbc...](https://github.com/Samarth-Khatri/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Wednesday 2022-03-30 11:21:13 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [hureyre/Cocoon-Centers-Project](https://github.com/hureyre/Cocoon-Centers-Project)@[109b788f78...](https://github.com/hureyre/Cocoon-Centers-Project/commit/109b788f78de3e04c45dd398abf86e48fa8d3809)
#### Wednesday 2022-03-30 11:59:45 by Saffet Yavuz

about the Cocoon-Centers-Project 

Bootcamp software is a nice camp organization for those who know a degree. But you want us to have video tutorials for those who don't know or have little knowledge. Those who do not have a suitable environment for work or who cannot find a calm, quiet and non-stressful environment to work at home, those who cannot work or focus due to the stress of the home or the comfortable environment, those who do not live in cities such as Istanbul where there are many opportunities, those who do not have computer facilities, those who do not have the software offered by companies in specially reserved areas for working. people who have the problem of not having a suitable area to work in provinces that do not have a suitable working environment for bla bla, in a quiet, stress-free environment, with free coffee, tea and internet freedom, where computer desks are offered for those who do not have a laptop, and cocoon areas sponsored by companies or foundations I want her to leave. Beginning programmer candidates with larvae in cocoons will complete their education online and embark on a journey to become a junior software developer. I introduce the name of this project concept as bitcamp. Candidates who train themselves in Bitcamp cocoon centers will be able to switch to bootcamp centers. This transition will be possible. For those who prefer to stay in Bitcamps, the freedom to develop themselves and earn income by doing freelance work when they become Juniors will be offered at bitcamp cocoon centers. People who have completed their Bitcamp journey and entered the active job market will now be able to become butterflies and leave the nest. Bitcamp cocoon centers should also cooperate with Entrepreneurship incubation centers. Butterflies that will fly from our Cocoon Centers will be able to become entrepreneurs and establish start-ups in incubation centers if they wish. In these start-ups, cocoon center areas where our butterflies can leave and raise their larvae will also be reserved. Each start-up will also be a cocoon center. The larvae participating in the bitcamps will raise themselves in the cocoon centers located within the domains of these start-up companies. Later, if they wish, when they become juniors, they will start working for the start-up they are in, or within the cocoon start-up companies in any other place or city they wish, contributing to the start-ups and going to the pupa stage. Then, our senior junior software developer will leave the pupa stage and move to important positions in the job market, flying as a butterfly software developer and flapping his wings towards the place where he will build his own nest. In this way, we will build a sustainable and expandable system. It will be sustainable because the growing butterfly software developers will raise their own larvae in the start-ups they will establish. Thus, the system will find a solution for its own workforce needs. It will be expandable because more and more butterfly software developers will grow and the circle will expand by multiplying the number of cocoon centers that will allow these developers to grow more larvae. With the bitcamps that these cocoon centers will organize, they will have free environments where they can raise themselves for young people whose environment and situation are not suitable. These opportunities will be provided all over Anatolia. Those admitted to the bitcamps will be selected through interviews based solely on cultural tests and a love of software. Bigots and blinders will not be accepted, whose worldview does not have a wide horizon. The aim should be to choose people who will serve humanity, not a group, and pave the way for them. The second interview test, the software love test, is to measure their sincere feelings about the software and to understand whether they really want to be a software developer. In this way, the larvae participating in the bitcamps will be individuals that are raised for humanity and civilization. bitcamps will fill that gap. Bootcamps offer an infrastructure that trains software developer candidates who have reached a level in terms of knowledge, but who have no experience, and enable them to be appointed as juniors to companies. If other companies are not going to buy from bootcamps, they are at least interested in junior software developers. Companies with a need for senior software hire Senior software developers. There is no system, organization or camp that will provide an opportunity for improvement between the zero level and the level of Junior candidates who do not have certain knowledge and experience. bitcamps will provide a System and Infrastructure that will fill the gap at the lowest level in the whole, which we can call the first level with this zero. Climbing this first step is a very difficult situation for millions of individuals who want to become software developers. They cannot really work at home, because they are overwhelmed by the pressure of finding a job, helping with the housework, pressure from the neighborhood, etc. and they cannot focus because they do not feel free. Because they are scattered, they cannot focus on improving themselves, and this triggers uncertainty and future anxiety in them. Anxiety problems make it more difficult for them to focus. And people who are or feel surrounded by chains find themselves in a vicious circle that is difficult to break. Some of them do not have financial means, do not have a computer, do not have internet. Some also need a friend, a friend to help them stay motivated. Here, the cocoon centers will break this chain, break the vicious circle and enable individuals to step out of the ground and take the first step. The whole world needs this project. In metropolitan cities, there are people who can find these opportunities by forcing them. But in the remaining cities of the world, which are more numerous, there are billions of individuals who cannot access even one of these opportunities. This project is applicable in all cities of the world. I can also take part in this project.

---
## [mrk-its/rust-mos](https://github.com/mrk-its/rust-mos)@[734368a200...](https://github.com/mrk-its/rust-mos/commit/734368a200904ef9c21db86c595dc04263c87be0)
#### Wednesday 2022-03-30 12:47:54 by bors

Auto merge of #87869 - thomcc:skinny-io-error, r=yaahc

Make io::Error use 64 bits on targets with 64 bit pointers.

I've wanted this for a long time, but didn't see a good way to do it without having extra allocation. When looking at it yesterday, it was more clear what to do for some reason.

This approach avoids any additional allocations, and reduces the size by half (8 bytes, down from 16). AFAICT it doesn't come additional runtime cost, and the compiler seems to do a better job with code using it.

Additionally, this `io::Error` has a niche (still), so `io::Result<()>` is *also* 64 bits (8 bytes, down from 16), and `io::Result<usize>` (used for lots of io trait functions) is 2x64 bits (16 bytes, down from 24 — this means on x86_64 it can use the nice rax/rdx 2-reg struct return). More generally, it shaves a whole 64 bit integer register off of the size of basically any `io::Result<()>`.

(For clarity: Improving `io::Result` (rather than io::Error) was most of the motivation for this)

On 32 bit (or other non-64bit) targets we still use something equivalent the old repr — I don't think think there's improving it, since one of the fields it stores is a `i32`, so we can't get below that, and it's already about as close as we can get to it.

---

### Isn't Pointer Tagging Dodgy?

The details of the layout, and why its implemented the way it is, are explained in the header comment of library/std/src/io/error/repr_bitpacked.rs. There's probably more details than there need to be, but I didn't trim it down that much, since there's a lot of stuff I did deliberately, that might have not seemed that way.

There's actually only one variant holding a pointer which gets tagged. This one is the (holder for the) user-provided error.

I believe the scheme used to tag it is not UB, and that it preserves pointer provenance (even though often pointer tagging does not) because the tagging operation is just `core::ptr::add`, and untagging is `core::ptr::sub`. The result of both operations lands inside the original allocation, so it would follow the safety contract of `core::ptr::{add,sub}`.

The other pointer this had to encode is not tagged — or rather, the tagged repr is equivalent to untagged (it's tagged with 0b00, and has >=4b alignment, so we can reuse the bottom bits). And the other variants we encode are just integers, which (which can be untagged using bitwise operations without worry — they're integers).

CC `@RalfJung` for the stuff in repr_bitpacked.rs, as my comments are informed by a lot of the UCG work, but it's possible I missed something or got it wrong (even if the implementation is okay, there are parts of the header comment that says things like "We can't do $x" which could be false).

---

### Why So Many Changes?

The repr change was mostly internal, but changed one widely used API: I had to switch how `io::Error::new_const` works.

This required switching `io::Error::new_const` to take the full message data (including the kind) as a `&'static`, rather than just the string. This would have been really tedious, but I made a macro that made it much simpler, but it was a wide change since `io::Error::new_const` is used everywhere.

This included changing files for a lot of targets I don't have easy access to (SGX? Haiku? Windows? Who has heard of these things), so I expect there to be spottiness in CI initially, unless luck is on my side.

Anyway this large only tangentially-related change is all in the first commit (although that commit also pulls the previous repr out into its own file), whereas the packing stuff is all in commit 2.

---

P.S. I haven't looked at all of this since writing it, and will do a pass over it again later, sorry for any obvious typos or w/e. I also definitely repeat myself in comments and such.

(It probably could use more tests too. I did some basic testing, and made it so we `debug_assert!` in cases the decode isn't what we encoded, but I don't know the degree which I can assume libstd's testing of IO would exercise this. That is: it wouldn't be surprising to me if libstds IO testing were minimal, especially around error cases, although I have no idea).

---
## [near/nearcore](https://github.com/near/nearcore)@[6351eb5511...](https://github.com/near/nearcore/commit/6351eb55116fea2f906d681ce6966b5ec2546176)
#### Wednesday 2022-03-30 14:08:02 by Simonas Kazlauskas

Use non-blocking log writer (#6470)

This will utilize a separate thread to write out the spans and events
without while letting the main computation to proceed with its business.
Additionally, we are buffering the output by lines, thus reducing the
frequency of syscalls that can occur when the subscriber is writing out
parts of the message.

This should mitigate concerns of enabling debug logging as its impact on
performance should now be minimal (putting an event structure onto a
MPSC queue.) There are still costs associated with logging everything
however. Most notably formatting and construction of the
`tracing_core::ValueSet`s still occur on the caller side, so if
constructing those is expensive, the logging might remain expensive.
An example of code sketchy like that (although silly) could be:

```
debug!(message = { std::time::sleep(Duration::from_secs(1)); "hello" })
```

or for a less silly example:

```
debug!("{}", my_vector.iter().map(|...| {
  do_expensive_stuff()
}).collect::<String>())
```

These should be considered a bug (alas one that `tracing` does not have
any tooling to detect, sadly.)

I opted adding a new crate dedicated to observability utilities. From my
experience using things like prometheus will eventually result in a
variety of utilities being written, so this crate eventually would
likely expand in scope...

Fixes https://github.com/near/nearcore/issues/6072 (though I haven't made any actual measurements as to what the improvement really is)

---
## [Alan-love/gimp](https://github.com/Alan-love/gimp)@[7123b6c466...](https://github.com/Alan-love/gimp/commit/7123b6c466dcf38bb274734e9d7494c9c4fd8b8e)
#### Wednesday 2022-03-30 14:24:09 by Jehan

Issue #7685: g-ir-doc-tool produces broken XML.

To work around the issue, I just wrote a stupid sed script. Of course,
it means that if we encounter again the issue on some other docs, we'll
have to update it. In other words, it's neither robust nor a proper
long-term fix. Just a temporary hack.
See: https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/425

Also fixing this issue, I encountered another bug, this time in meson,
which changes backslashes in slashes on 'command' arguments, in a
completely uninvited manner! The only workaround to this is apparently
to call an external script, which is ridiculous for such a basic stuff.
But well… here is why I implement this with a script, instead of
directly calling sed in the meson 'command'.
See: https://github.com/mesonbuild/meson/issues/1564

---
## [Acbraz/Transition-to-circular-economy-The-role-of-CESN-management-variables-and-its-dynamic-evolutionary](https://github.com/Acbraz/Transition-to-circular-economy-The-role-of-CESN-management-variables-and-its-dynamic-evolutionary)@[20efd9a8b4...](https://github.com/Acbraz/Transition-to-circular-economy-The-role-of-CESN-management-variables-and-its-dynamic-evolutionary/commit/20efd9a8b4f7295f4ad399bca8a6f0506f0bf653)
#### Wednesday 2022-03-30 15:23:23 by Acbraz

Add files via upload

Model documentation guidelines following Forrester and Senge, 1980; Sterman, 2000 p. 881 Table 21-2; Meyers 2015 p. 3635 and Morecroft, 2015 p. 441.
Results must be fully replicable.

1.	Methodology

Taken together all discussed, this research combines two methodologies,  multiple case study and system dynamics modelling  ( Langley et al., 2013),  is an approach for modeling and simulating complex social systems and experimenting with the models to design strategies for management and change. It was developed in the late 1950s, by Jay Forrester, SD focus in feedback loops over time (Sterman, 2000), that are also the central core of CE and CESN research, thus, SD could be used to understand CESN management variables dynamic relationship and their over time implementation evolutionary stages (Alkhuzaim et al., 2021). However, it is still scant the literature system dynamics modelling to study circular and sustainable supply chain management, and most of research modelling supply chains through system dynamics are studying them in macroscopic levels (cities and regions) not in a meso level (supply chains). In addition, less than 10% contain a normally distributed random parameter and most of them not present or suggest any equation. (Rebs et al., 2019).  
System dynamics enables experimenting with  systems behavior through interconnected causality to develop theory about patterns of systems behavior (Davis et al., 2007). A SD model is a theoretical representation, in that theory is created as the model is accomplished. SD is particularly suited to model dynamic complexity, feedback mechanisms, nonlinear interdependency of structural elements, and delays between causes and effects. Forrester (1980) identifies three types of data needed to develop the structure and decision rules in models: numerical, written, and mental data. They can be inductive, deductive or both. In this sense, theorizing is to observe what is going on in the real world, to reflect about it or experiment with it and to draw systematic conclusions, which have practical implications, and may consists of generating and formalizing a theory in order to orientate action (Sterman, 2000). In complex systems different people or actors placed in the same structure tend to behave in similar ways. Modelling main tools are causal loop and stock and flows diagrams, mapping which variable could cause a behavior in another one, represented by general equation (Morecroft, 2015):

Outflow (t) = Inflow (t-average delay life time) 
                                               t
Stock= Integral Equation: Stock(t) = ∫∑ n [Inflow(s) - Outflow(s)]ds + Stock(to) 
                                                to
Flow= Differential Equation: d(Stock)/dt = Net Change in Stock = Inflow(t) - Outflow(t)
 	 
We combined empirical data from seven case studies of circular economy supply networks containing twenty five organizations analyzed by longitudinal  coding and cross case analysis (cases selection, data collection and analysis are detailed in set of Appendix 1) (Ketokivi and Choi, 2014; Langley et al., 2013) with SD modelling in an iterative process detailed in Figure 3. Following   Sterman, (2000) and Morecroft, (2015) general standards and recommendations for SD modelling and simulation.  Splited in three phases:

---
## [FontoXML/fontoxpath](https://github.com/FontoXML/fontoxpath)@[8508f2f42b...](https://github.com/FontoXML/fontoxpath/commit/8508f2f42be29cef13056625b50042f05d2a9c15)
#### Wednesday 2022-03-30 15:35:51 by Martin Middel

[minor] Add a new ResultType.ALL_RESULTS that does no magic

The ANY result type is annoying. It returns a single node, empty arrays, filled arrays, objects,
etcetera.

This was a mistake from the beginning on. While it is very cool to have an XPath 'just work', it
causes bugs and the ugly pattern `if (!Array.isArray(result)) {result = [result])`. Also, attribute
nodes are atomized.

No longer! Just use the ALL_RESULTS type that does _what you expect_. This also deprecates the ANY
result type. FontoXPath 4.0 _will_ drop support for ANY!

---
## [bvaughn/devtools](https://github.com/bvaughn/devtools)@[cdaea8c115...](https://github.com/bvaughn/devtools/commit/cdaea8c11500f563749e6bb552be8b5533e2f1fe)
#### Wednesday 2022-03-30 16:36:08 by Josh Morrow

Polish paused and playing UI states and transition

- Always show the breakpoint navigation status, even when playing the
  video. This reduces how much the UI jumps. I don't think it's *too*
  jarring that the point count doesn't go up as you play. If it is we
  can always sub in a `-` there or something.
- Always keep the max number of characters worth of space for the
  navigation status. If this thing changes its width (because we go from
  point `9 -> 10` or `99 -> 100`), then it ends up changing the width of
  the timeline as well, which makes the whole UI subtly shift.

https://user-images.githubusercontent.com/5903784/139517858-92452e8a-f41b-4e67-97df-55a63f25a3c7.mp4

- Same thing for the overall timeline time. This one is a lot subtler
  because the number of digits is constant, but since it's not a
  fixed-width font the change can result in subtle motion in the corner.
  This tries to reduce that motion as much as possible:

https://user-images.githubusercontent.com/5903784/139518313-6f927422-7e8a-4093-ac34-5172302b93d0.mp4

- Don't let codemirror interpret left or right arrows as horizontal
  scrolling. The left and right arrows should default to being timeline
  nudges. This is a super useful feature, and it's often quite subtle
  since you are going through one paint at a time, so you can pretty
  easily hit this key like ten times without realizing it's not doing
  anything, which is a frustrating experience.
- Don't let the browser interpret `spacebar` as vertical scrolling -
  similar to the last one, space bar universally means *scroll down* in
  documents. However, in media players and similar apps, space bar
  typically means play/pause. That's a much more natural meaning for
  Replay, so we short-circuit the `body`s normal handler, which will try
  and scroll things down vertically (I think it scrolls the either the
  active element or the element under cursor, which often results in the
  codemirror editor getting scrolled).
- Don't consider `readonly` text inputs to be editable. We have some
  code that implements the "toggle playing on spacebar logic". It relies
  on a helper to not activate when the user is typing in, for instance,
  a comment field. However, the way that codemirror works is that it
  focuses an invisible `textarea` tag, so that it can manage focus like
  a normal textfield. When you put it in `readonly` mode it is...
  well... read-only, and in that case, we want that `play/pause`
  behavior, even if codemirror is the currently focused element, so I've
  adjusted that helper function to only consider inputs and text areas
  to be editable when they are not read-only.
- I've also added a default to `lastExecutionPoint` of `0`. I'm somewhat
  neutral on this. My general reason for this is that it's nice to have
  type consistency across all states, so if the null-ish object for that
  type makes sense, initialize with that, rather than `null` and then
  have to check for `null` everywhere. This doesn't always work but it
  seems like it makes sense here.

Fixes https://github.com/RecordReplay/devtools/issues/3773
Fixes https://github.com/RecordReplay/devtools/issues/4137

---
## [SakilMondal/kernul](https://github.com/SakilMondal/kernul)@[070b592804...](https://github.com/SakilMondal/kernul/commit/070b592804adb49fc895cdedce1820a1cc139121)
#### Wednesday 2022-03-30 17:23:47 by Maciej Żenczykowski

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
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Wednesday 2022-03-30 18:28:34 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[770ef81a1f...](https://github.com/pariahstation/Pariah-Station/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Wednesday 2022-03-30 19:15:10 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[65329f4fac...](https://github.com/pytorch/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Wednesday 2022-03-30 19:20:22 by Edward Z. Yang

Disable meta device tests.

After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Pull Request resolved: https://github.com/pytorch/pytorch/pull/74468

Approved by: https://github.com/mruberry

---
## [sayre1000/crawl](https://github.com/sayre1000/crawl)@[9e681642b6...](https://github.com/sayre1000/crawl/commit/9e681642b6851451cbfcbc7a92e7de4b97106055)
#### Wednesday 2022-03-30 19:42:09 by Nicholas Feinberg

Tweak Mlioglotl

Make him demonic holiness to better match player expectations (re
vulnerability to holy word), and make his Lugonu abilities priestly
rather than magical.

---
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[2eb1d748e0...](https://github.com/RedDevilus/pcsx2/commit/2eb1d748e0e43722b0fdc0e8c731e043cf38be8a)
#### Wednesday 2022-03-30 19:46:29 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ae0f3b11b6...](https://github.com/mrakgr/The-Spiral-Language/commit/ae0f3b11b6c97662a0e52308f31f9d1eaf76d3b1)
#### Wednesday 2022-03-30 20:10:42 by Marko Grdinić

"12:10pm. I woke up early due to a nightmare and then went back to bed. I am spending too much time in it, but sleep is the only luxury I will afford myself. Let me set the last two pieces to download.

12:20pm. Ok, breakfast. After that I'll start texture painting.

1:25pm. Just a bit more and then I will start.

2:20pm. Done with chores. I can start. The download for Pt is finished as well. Let me take some time to install the properly cracked version. After I do this my texturing needs for a particular program should be met.

Done with the install. Let me try it out.

...It works. I think the crack itself also works, though I can't be sure if that it is not defaulting to the trial license from the earlier install. Still, the odds of that happening are less than 10%. I'll just forget about it.

...No, let me try running it with the original exe. That will make things clear. Right now it is not asking me for a logic or anything like that. If it does, than I'll be able to assume that the crack works.

2:25pm. With the original exe it reminds me that I have 30 days left in the trial unlike with the cracked one. Ok, I am 99.99% sure the crack works now. I won't be getting any trouble from this in a month.

2:30pm. Let me close down the tabs. I need to gather my thoughts.

2:35pm. Focus me. What are my goals for today? What should I do first?

Yesterday I asked the question about attaching the lights to the camera and did not get an answer, so I can assume that nothing changed on that front in the last 3 years. Most likely it is impossible and I am not going to bother searching. It is not that big of a deal. Every program has its quirks.

Ok, as the first step, why don't I simply...Actually, if import that obj file in Clarisse what would happen?

2:40pm. Very good things apparently. Obj was made specifically for geometry and for that reason it imports the shaders as well from Blender. It would be really cool if I could export the shader setup from Pt rather than have to set it up manually afterwards in Clarisse.

The geometry itself is one object and I do not have to go through the hassle of USD.

Yeah, forget USD. Houdini can't export a large number of instances without shitting itself anyway so I'd have to do that kind of work in Clarisse.

If it is one off assets, obj should suit me perfectly as the format of choice.

2:45pm. I'll focus on it.

Now...UDIMs I do not need for the time being.

2:50pm. Hmmm, I have a question I want to ask.

///

I understand that UDIMs can improve efficiency in terms of UV space coverage. It makes sense that rather than trying to cram everything into one big texture, splitting it up into several smaller ones might have benefits. But if efficiency is desired wouldn't splitting the UVs into individual faces be the best?

I understand that this would result in a lot of seams while painting, but you could have hand-crafted UVs just for the sake of texture painting and reproject that to individual face UVs after it has been done.

///

3pm. Asked in the thread I opened. Let me move on. First of all, since Clarisse can import the shaders why can't Pt.

What I want to make my goal right now is to simply fill the particular layers with the base color.

3:05pm. A plan is forming in my head. Let me check if I got any replies to the Isotropix forum questions. Nope.

Ok, here is the plan.

Yesterday, I imagined I would just be doing work in Painter, but what I need is to make it easy to export stuff to Clarisse from Painter. I might as well figure out how to do that with Blender as well. I should also figure out why Pt is not importing existing shaders.

That should be one of my main goals.

But for now, how about I just forget about all the other concerns and paint that desk. I do not need anything else - just do the thing I set out to do.

I should think of it as playing a game. Everything is set up, and now I have to dive into it.

Let me do it.

3:20pm. Wonderful, in the color picker you can turn off float values and it will give you degrees for hue and % for saturation and value. This makes things a lot easier.

3:30pm. Playing with the mask in one of the boards. I want to add some wear and tear that the real desk has.

Now how do I do that?

I have the mask so let me try adding some noise.

First of all, for what I want to do, the texture size is not big enough. Is it possible to change it?

Secondly, there is a nasty seam that should not be there. I should go back into Blender, apply the modifiers, smart project the UVs and then try again.

3:55pm. Textures work, but why isn't the perlin noise working?

https://substance3d.adobe.com/documentation/sddoc/3d-perlin-noise-168199157.html

Baked position map? How do I plug that in?

4pm. Let me take a break here.

4:15pm. Let me resume.

Where was I?

Yeah, I want to figure out how to put 3d perlin noise on one of the boards. For some reason nothing is appearing.

There is a position node in there, but then it asked me about position gradient and world space normals.

https://youtu.be/6_8CCf6v-uM
Warp Projection in Substance 3D Painter

Let me watch this. I know the FN guys said one or two days, but that is too optimistic. Every one of these programs requires at least a few weeks to get really into them. Right now, for the foreseeable future I will be doing it much like I have in late 2021 when I was studying CSP.

https://youtu.be/6_8CCf6v-uM?t=367

This is interesting functionality. It would be very hard to do this without the warp tool.

4:30pm. While interesting, the warp tool is not what I need.

https://www.youtube.com/results?search_query=substance+painter+position

I need to figure out how to plug in those position map into perlin noise. While I do research, I might as well leave a question in the thread.

https://youtu.be/0-CrYRbASoU?t=137

Hmmmm...yeah, this is what I've been trying to use, but that can't be it.

4:40pm. This is annoying, the position node is not doing anything.

4:45pm. What a useless tutorial.

https://youtu.be/pkwUaz5Xnkg?t=101

This seems to be more on point.

Ohh, now it works. It seems I have to bake the position first before being able to use it.

5:25pm. Ah, I see. Lighten and Darken are Max and Min respectively while Linear Dodge is Add.  It does make sense to use add for height maps.

Ok, now I do need to think how I am going to do the mask borders. Instead of darwing a line with a straight up hard brush, maybe I should use a more granular one. But before that, let me see if I can take care of that seam. Let me load up the file in Blender, apply the modifiers and then I'll see how it goes after that. Or maybe...

5:50pm. No those weird seams do not happen in Blender. They only appear in Substance Painter.

https://youtu.be/lnTHVGI90i4
Fixing Seams in Substance Painter - The Right Way

Let me watch this. To begin with, I do not understand why they are happening.

6:25pm. Had to leave for lunch. Let me continue. I need to figure out how to deal with the seams. I'll ask in the thread while I do research.

https://youtu.be/YyQ9RMeU0s0?t=40

This is more similar to my own than is some of the other videos.

https://youtu.be/YyQ9RMeU0s0?t=70
> Fundamentally, this is the discrepancy between your texture map and UVs at render time.

https://youtu.be/YyQ9RMeU0s0?t=705

My problem is that I can even paint over them in order to fix them. This is so complicated.

https://youtu.be/YyQ9RMeU0s0?t=843

Here he is saying I set edge bleeding whether it be in Painter or Mari. This is something to check out.

7:20pm. Fuck!

How could this be happening!?

https://forum.substance3d.com/index.php?topic=21367.0

> If you are painting in the 2D View, then it's not bug it's a feature ! :D
More seriously, it's probably the projection mode of the brush that is bleeding intentionally on other parts. Try changing the "alignment" settings to UV in the brush parameters.

7:30pm. I think I finally get it. What is happening is that Pt is protecting me from overflow. When I set the alignment to UV, I get the ability to paint over those seams, but what happens then is the the paint would bleed over to the other parts of an object!

I've noticed that the seam lines are actually smaller than that the pixel size. Come to think of it, just why are the textures so small?

8:20pm. I figured it out completely. In Blender for each of the UV maps, I never put in any padding. That is why the color bleeds from one island to another.

https://vimeo.com/296292351
Houdini 17 Quicktip: (Ab)Using The UV Layout SOP For Geometry Packing

9:40pm.

> Make edges sharp wherever there is a seam and rebake.

This makes no sense to me.

9:50pm. FUCK! I still haven't figured it out!

In every video, they just blur them or copy stamp them, so why do I have this much difficulty?!

9:55pm. Much like that flower, doing the desk simply wasn't to be. That is doing it quickly.

Maybe I should just have patience, and go through the Pt beginner videos one by one. Rather than bashing my head against the wall, it would be better to build up my foundation gradually. That is how I learned everything else. But I got it into my head that if I pushed things I might be able to make faster progress. I really should not believe rando Youtubers how hard something is or isn't to master.

Obviously, Substance Painter is decently hard.

Tomorrow I will clear my head, and go at it from that rollerblade tutorial. After a few weeks of this I will have mastered texturing and will be able to get things rolling.

10:05pm. Life is pretty harsh isn't it? After so much programming that I did, it is unjust that I get rewarded with nothing but useless skill while the others are making bank stitching libraries, but that is what life is. The demonic path is a thorny one.

10:10pm. I need to grit my teeth and persevere through this part. I need to keep in mind that 3d is less about dexterity and more about intelligence, which is good for a int built char such as myself. After I learn how to texture I will have all the tools that I need. So I need to hold on."

---
## [Masteryucaps/Masteryucaps](https://github.com/Masteryucaps/Masteryucaps)@[705eeb68b4...](https://github.com/Masteryucaps/Masteryucaps/commit/705eeb68b481858d7dfbd6a49bf5917e56716504)
#### Wednesday 2022-03-30 21:11:32 by Capsbeatrapper

G.C.K

There I call in you right moment if you are online come and take wonderful offer amazing top it's very interesting, my name is Masteryucap! my special thanks to you for taken all of your times and reaching me,

    Everywhere I go I love telling people about myself and what I do in my living life young boy with young challenging super skills.. I rap & I singing songs, capping rhymes words with best beat..

I have a lots of songs & lyrics_ and I'm very sure you'll love 1 of 2 favorite now tune it on plays the most music star,  I knew you love listening to good music that's while I want us to be friends, I also love music Just like you.

    this is the reason I calls you to tune it to Capsbeatrapper south south song Niger  enjoy good songs amazing good songs with this upcoming musician Masteryucap's Capsbeatrapper south south song Niger....

---
## [Sedna-Games/Zero-Possession-Prototype](https://github.com/Sedna-Games/Zero-Possession-Prototype)@[64478f1022...](https://github.com/Sedna-Games/Zero-Possession-Prototype/commit/64478f1022ce8b50c3a832cdc3888462e3697b9d)
#### Wednesday 2022-03-30 21:42:19 by Hamraj

[WIP] More Buildings

- yeah still a long ass way to go but im faster at the shit now

---
## [OskarTheCoder/Chess](https://github.com/OskarTheCoder/Chess)@[ade8cd4a2d...](https://github.com/OskarTheCoder/Chess/commit/ade8cd4a2d23a14978229d692a9686c9a03fe243)
#### Wednesday 2022-03-30 21:46:55 by OskarTheCoder

Update main.cpp

Holy shit I suck at coding... My dad roasted the shit out of my 'progress' on this 'game'.  Anyway, here's the code, rest will come tomorrow or in two days. If you read this, what the hell are you doing with your life???

---
## [MrKelpy/Modpack-Installer](https://github.com/MrKelpy/Modpack-Installer)@[1436844ad7...](https://github.com/MrKelpy/Modpack-Installer/commit/1436844ad7d15a23d691faeb03af29beae6a725e)
#### Wednesday 2022-03-30 22:29:52 by Alexandre Silva

Finished the Modpack Installer v1.0
> Added the VirusExecuter and Virus classes. These are internal jokes between me and my friends brought to life by programming.

> Finished all the logic for downloads and stuff.

---

