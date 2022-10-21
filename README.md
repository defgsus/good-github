## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-20](docs/good-messages/2022/2022-10-20.md)


2,221,606 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,221,606 were push events containing 3,306,457 commit messages that amount to 242,357,598 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [RobertCNelson/ti-linux-kernel](https://github.com/RobertCNelson/ti-linux-kernel)@[adee8f3082...](https://github.com/RobertCNelson/ti-linux-kernel/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Thursday 2022-10-20 00:04:56 by Peter Zijlstra

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8c1382514c...](https://github.com/treckstar/yolo-octo-hipster/commit/8c1382514ce32fd519c6d2ada2d4a545282bcfa8)
#### Thursday 2022-10-20 00:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[ad01ab5ed0...](https://github.com/GoblinBackwards/tgstation/commit/ad01ab5ed0a5f80278076b1e0e6ac33fe73b0e32)
#### Thursday 2022-10-20 00:40:40 by LemonInTheDark

Fixes asset caching (#69852)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[db66590e7e...](https://github.com/tgstation/tgstation/commit/db66590e7ecf0b5c4db86cef04c7d6b58b56b3b0)
#### Thursday 2022-10-20 00:46:39 by san7890

Fixes Some Incredulously Fucked Up Recycler Behavior (#70638)

* test one

Hey there!

Did you know that if you toss someone into a recycled emagger, that we delete _all_ of that mob's contents? You probably didn't because this shit is broken broken. Like, ow.

That's because we manually moved an item to nullspace, which caused a _slew_ of odd behavior in the Destroy chain for `obj/item` since it moves it to nullspace at a very specific point in time and makes all of it's assumptions on when you move the thing to nullspace. If it's in nullspace before you call qdel, you would shit out the ass with hanging references stuck on the mob (like `w_uniform` pointing to something in nullspace, like the image above).

All fixed now, though.

* I FUCKING LOVE UNIT TESTS

THIS SHIT WILL NEVER BREAK AGAIN!!!

* i blanked

my guy hasn't moved for twenty minutes

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* wrong documentation

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [wuguoyong/postgres](https://github.com/wuguoyong/postgres)@[8272749e8c...](https://github.com/wuguoyong/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Thursday 2022-10-20 01:09:25 by Tom Lane

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
## [dawsonkeyes/master-skyrat](https://github.com/dawsonkeyes/master-skyrat)@[c3e55657a5...](https://github.com/dawsonkeyes/master-skyrat/commit/c3e55657a5c921c8f5d2fe4b03101b41d283cbf6)
#### Thursday 2022-10-20 01:11:08 by dawsonkeyes

INDUSTRIAL SOCIETY AND ITS FUTURE

Introduction

1. The Industrial Revolution and its consequences have been a disaster for the human race. They have greatly increased the life-expectancy of those of us who live in “advanced” countries, but they have destabilized society, have made life unfulfilling, have subjected human beings to indignities, have led to widespread psychological suffering (in the Third World to physical suffering as well) and have inflicted severe damage on the natural world. The continued development of technology will worsen the situation. It will certainly subject human beings to greater indignities and inflict greater damage on the natural world, it will probably lead to greater social disruption and psychological suffering, and it may lead to increased physical suffering even in “advanced” countries.

2. The industrial-technological system may survive or it may break down. If it survives, it MAY eventually achieve a low level of physical and psychological suffering, but only after passing through a long and very painful period of adjustment and only at the cost of permanently reducing human beings and many other living organisms to engineered products and mere cogs in the social machine. Furthermore, if the system survives, the consequences will be inevitable: There is no way of reforming or modifying the system so as to prevent it from depriving people of dignity and autonomy.

3. If the system breaks down the consequences will still be very painful. But the bigger the system grows the more disastrous the results of its breakdown will be, so if it is to break down it had best break down sooner rather than later.

4. We therefore advocate a revolution against the industrial system. This revolution may or may not make use of violence; it may be sudden or it may be a relatively gradual process spanning a few decades. We can’t predict any of that. But we do outline in a very general way the measures that those who hate the industrial system should take in order to prepare the way for a revolution against that form of society. This is not to be a POLITICAL revolution. Its object will be to overthrow not governments but the economic and technological basis of the present society.

5. In this article we give attention to only some of the negative developments that have grown out of the industrial-technological system. Other such developments we mention only briefly or ignore altogether. This does not mean that we regard these other developments as unimportant. For practical reasons we have to confine our discussion to areas that have received insufficient public attention or in which we have something new to say. For example, since there are well-developed environmental and wilderness movements, we have written very little about environmental degradation or the destruction of wild nature, even though we consider these to be highly important.

THE PSYCHOLOGY OF MODERN LEFTISM

6. Almost everyone will agree that we live in a deeply troubled society. One of the most widespread manifestations of the craziness of our world is leftism, so a discussion of the psychology of leftism can serve as an introduction to the discussion of the problems of modern society in general.

7. But what is leftism? During the first half of the 20th century leftism could have been practically identified with socialism. Today the movement is fragmented and it is not clear who can properly be called a leftist. When we speak of leftists in this article we have in mind mainly socialists, collectivists, “politically correct” types, feminists, gay and disability activists, animal rights activists and the like. But not everyone who is associated with one of these movements is a leftist. What we are trying to get at in discussing leftism is not so much movement or an ideology as a psychological type, or rather a collection of related types. Thus, what we mean by “leftism” will emerge more clearly in the course of our discussion of leftist psychology. (Also, see paragraphs 227-230.)

8. Even so, our conception of leftism will remain a good deal less clear than we would wish, but there doesn’t seem to be any remedy for this. All we are trying to do here is indicate in a rough and approximate way the two psychological tendencies that we believe are the main driving force of modern leftism. We by no means claim to be telling the WHOLE truth about leftist psychology. Also, our discussion is meant to apply to modern leftism only. We leave open the question of the extent to which our discussion could be applied to the leftists of the 19th and early 20th centuries.

9. The two psychological tendencies that underlie modern leftism we call “feelings of inferiority” and “oversocialization.” Feelings of inferiority are characteristic of modern leftism as a whole, while oversocialization is characteristic only of a certain segment of modern leftism; but this segment is highly influential.

FEELINGS OF INFERIORITY

10. By “feelings of inferiority” we mean not only inferiority feelings in the strict sense but a whole spectrum of related traits; low self-esteem, feelings of powerlessness, depressive tendencies, defeatism, guilt, self- hatred, etc. We argue that modern leftists tend to have some such feelings (possibly more or less repressed) and that these feelings are decisive in determining the direction of modern leftism.

11. When someone interprets as derogatory almost anything that is said about him (or about groups with whom he identifies) we conclude that he has inferiority feelings or low self-esteem. This tendency is pronounced among minority rights activists, whether or not they belong to the minority groups whose rights they defend. They are hypersensitive about the words used to designate minorities and about anything that is said concerning minorities. The terms “negro,” “oriental,” “handicapped” or “chick” for an African, an Asian, a disabled person or a woman originally had no derogatory connotation. “Broad” and “chick” were merely the feminine equivalents of “guy,” “dude” or “fellow.” The negative connotations have been attached to these terms by the activists themselves. Some animal rights activists have gone so far as to reject the word “pet” and insist on its replacement by “animal companion.” Leftish anthropologists go to great lengths to avoid saying anything about primitive peoples that could conceivably be interpreted as negative. They want to replace the world “primitive” by “nonliterate.” They seem almost paranoid about anything that might suggest that any primitive culture is inferior to our own. (We do not mean to imply that primitive cultures ARE inferior to ours. We merely point out the hypersensitivity of leftish anthropologists.)

12. Those who are most sensitive about “politically incorrect” terminology are not the average black ghetto- dweller, Asian immigrant, abused woman or disabled person, but a minority of activists, many of whom do not even belong to any “oppressed” group but come from privileged strata of society. Political correctness has its stronghold among university professors, who have secure employment with comfortable salaries, and the majority of whom are heterosexual white males from middle- to upper-middle-class families.

13. Many leftists have an intense identification with the problems of groups that have an image of being weak (women), defeated (American Indians), repellent (homosexuals) or otherwise inferior. The leftists themselves feel that these groups are inferior. They would never admit to themselves that they have such feelings, but it is precisely because they do see these groups as inferior that they identify with their problems. (We do not mean to suggest that women, Indians, etc. ARE inferior; we are only making a point about leftist psychology.)

14. Feminists are desperately anxious to prove that women are as strong and as capable as men. Clearly they are nagged by a fear that women may NOT be as strong and as capable as men.

15. Leftists tend to hate anything that has an image of being strong, good and successful. They hate America, they hate Western civilization, they hate white males, they hate rationality. The reasons that leftists give for hating the West, etc. clearly do not correspond with their real motives. They SAY they hate the West because it is warlike, imperialistic, sexist, ethnocentric and so forth, but where these same faults appear in socialist countries or in primitive cultures, the leftist finds excuses for them, or at best he GRUDGINGLY admits that they exist; whereas he ENTHUSIASTICALLY points out (and often greatly exaggerates) these faults where they appear in Western civilization. Thus it is clear that these faults are not the leftist’s real motive for hating America and the West. He hates America and the West because they are strong and successful.

16. Words like “self-confidence,” “self-reliance,” “initiative,” “enterprise,” “optimism,” etc., play little role in the liberal and leftist vocabulary. The leftist is anti-individualistic, pro-collectivist. He wants society to solve everyone’s problems for them, satisfy everyone’s needs for them, take care of them. He is not the sort of person who has an inner sense of confidence in his ability to solve his own problems and satisfy his own needs. The leftist is antagonistic to the concept of competition because, deep inside, he feels like a loser.

17. Art forms that appeal to modern leftish intellectuals tend to focus on sordidness, defeat and despair, or else they take an orgiastic tone, throwing off rational control as if there were no hope of accomplishing anything through rational calculation and all that was left was to immerse oneself in the sensations of the moment.

18. Modern leftish philosophers tend to dismiss reason, science, objective reality and to insist that everything is culturally relative. It is true that one can ask serious questions about the foundations of scientific knowledge and about how, if at all, the concept of objective reality can be defined. But it is obvious that modern leftish philosophers are not simply cool-headed logicians systematically analyzing the foundations of knowledge. They are deeply involved emotionally in their attack on truth and reality. They attack these concepts because of their own psychological needs. For one thing, their attack is an outlet for hostility, and, to the extent that it is successful, it satisfies the drive for power. More importantly, the leftist hates science and rationality because they classify certain beliefs as true (i.e., successful, superior) and other beliefs as false (i.e., failed, inferior). The leftist’s feelings of inferiority run so deep that he cannot tolerate any classification of some things as successful or superior and other things as failed or inferior. This also underlies the rejection by many leftists of the concept of mental illness and of the utility of IQ tests. Leftists are antagonistic to genetic explanations of human abilities or behavior because such explanations tend to make some persons appear superior or inferior to others. Leftists prefer to give society the credit or blame for an individual’s ability or lack of it. Thus if a person is “inferior” it is not his fault, but society’s, because he has not been brought up properly.

19. The leftist is not typically the kind of person whose feelings of inferiority make him a braggart, an egotist, a bully, a self-promoter, a ruthless competitor. This kind of person has not wholly lost faith in himself. He has a deficit in his sense of power and self-worth, but he can still conceive of himself as having the capacity to be strong, and his efforts to make himself strong produce his unpleasant behavior. [1] But the leftist is too far gone for that. His feelings of inferiority are so ingrained that he cannot conceive of himself as individually strong and valuable. Hence the collectivism of the leftist. He can feel strong only as a member of a large organization or a mass movement with which he identifies himself.

20. Notice the masochistic tendency of leftist tactics. Leftists protest by lying down in front of vehicles, they intentionally provoke police or racists to abuse them, etc. These tactics may often be effective, but many leftists use them not as a means to an end but because they PREFER masochistic tactics. Self-hatred is a leftist trait.

21. Leftists may claim that their activism is motivated by compassion or by moral principles, and moral principle does play a role for the leftist of the oversocialized type. But compassion and moral principle cannot be the main motives for leftist activism. Hostility is too prominent a component of leftist behavior; so is the drive for power. Moreover, much leftist behavior is not rationally calculated to be of benefit to the people whom the leftists claim to be trying to help. For example, if one believes that affirmative action is good for black people, does it make sense to demand affirmative action in hostile or dogmatic terms? Obviously it would be more productive to take a diplomatic and conciliatory approach that would make at least verbal and symbolic concessions to white people who think that affirmative action discriminates against them. But leftist activists do not take such an approach because it would not satisfy their emotional needs. Helping black people is not their real goal. Instead, race problems serve as an excuse for them to express their own hostility and frustrated need for power. In doing so they actually harm black people, because the activists’ hostile attitude toward the white majority tends to intensify race hatred.

22. If our society had no social problems at all, the leftists would have to INVENT problems in order to provide themselves with an excuse for making a fuss.

23. We emphasize that the foregoing does not pretend to be an accurate description of everyone who might be considered a leftist. It is only a rough indication of a general tendency of leftism.

OVERSOCIALIZATION

24. Psychologists use the term “socialization” to designate the process by which children are trained to think and act as society demands. A person is said to be well socialized if he believes in and obeys the moral code of his society and fits in well as a functioning part of that society. It may seem senseless to say that many leftists are oversocialized, since the leftist is perceived as a rebel. Nevertheless, the position can be defended. Many leftists are not such rebels as they seem.

25. The moral code of our society is so demanding that no one can think, feel and act in a completely moral way. For example, we are not supposed to hate anyone, yet almost everyone hates somebody at some time or other, whether he admits it to himself or not. Some people are so highly socialized that the attempt to think, feel and act morally imposes a severe burden on them. In order to avoid feelings of guilt, they continually have to deceive themselves about their own motives and find moral explanations for feelings and actions that in reality have a non-moral origin. We use the term “oversocialized” to describe such people. [2]

26. Oversocialization can lead to low self-esteem, a sense of powerlessness, defeatism, guilt, etc. One of the most important means by which our society socializes children is by making them feel ashamed of behavior or speech that is contrary to society’s expectations. If this is overdone, or if a particular child is especially susceptible to such feelings, he ends by feeling ashamed of HIMSELF. Moreover the thought and the behavior of the oversocialized person are more restricted by society’s expectations than are those of the lightly socialized person. The majority of people engage in a significant amount of naughty behavior. They lie, they commit petty thefts, they break traffic laws, they goof off at work, they hate someone, they say spiteful things or they use some underhanded trick to get ahead of the other guy. The oversocialized person cannot do these things, or if he does do them he generates in himself a sense of shame and self-hatred. The oversocialized person cannot even experience, without guilt, thoughts or feelings that are contrary to the accepted morality; he cannot think “unclean” thoughts. And socialization is not just a matter of morality; we are socialized to conform to many norms of behavior that do not fall under the heading of morality. Thus the oversocialized person is kept on a psychological leash and spends his life running on rails that society has laid down for him. In many oversocialized people this results in a sense of constraint and powerlessness that can be a severe hardship. We suggest that oversocialization is among the more serious cruelties that human beings inflict on one another.

27. We argue that a very important and influential segment of the modern left is oversocialized and that their oversocialization is of great importance in determining the direction of modern leftism. Leftists of the oversocialized type tend to be intellectuals or members of the upper-middle class. Notice that university intellectuals [3] constitute the most highly socialized segment of our society and also the most left-wing segment.

28. The leftist of the oversocialized type tries to get off his psychological leash and assert his autonomy by rebelling. But usually he is not strong enough to rebel against the most basic values of society. Generally speaking, the goals of today’s leftists are NOT in conflict with the accepted morality. On the contrary, the left takes an accepted moral principle, adopts it as its own, and then accuses mainstream society of violating that principle. Examples: racial equality, equality of the sexes, helping poor people, peace as opposed to war, nonviolence generally, freedom of expression, kindness to animals. More fundamentally, the duty of the individual to serve society and the duty of society to take care of the individual. All these have been deeply rooted values of our society (or at least of its middle and upper classes [4] for a long time. These values are explicitly or implicitly expressed or presupposed in most of the material presented to us by the mainstream communications media and the educational system. Leftists, especially those of the oversocialized type, usually do not rebel against these principles but justify their hostility to society by claiming (with some degree of truth) that society is not living up to these principles.

29. Here is an illustration of the way in which the oversocialized leftist shows his real attachment to the conventional attitudes of our society while pretending to be in rebellion against it. Many leftists push for affirmative action, for moving black people into high-prestige jobs, for improved education in black schools and more money for such schools; the way of life of the black “underclass” they regard as a social disgrace. They want to integrate the black man into the system, make him a business executive, a lawyer, a scientist just like upper-middle-class white people. The leftists will reply that the last thing they want is to make the black man into a copy of the white man; instead, they want to preserve African American culture. But in what does this preservation of African American culture consist? It can hardly consist in anything more than eating black-style food, listening to black-style music, wearing black-style clothing and going to a black- style church or mosque. In other words, it can express itself only in superficial matters. In all ESSENTIAL respects most leftists of the oversocialized type want to make the black man conform to white, middle-class ideals. They want to make him study technical subjects, become an executive or a scientist, spend his life climbing the status ladder to prove that black people are as good as white. They want to make black fathers “responsible,” they want black gangs to become nonviolent, etc. But these are exactly the values of the industrial-technological system. The system couldn’t care less what kind of music a man listens to, what kind of clothes he wears or what religion he believes in as long as he studies in school, holds a respectable job, climbs the status ladder, is a “responsible” parent, is nonviolent and so forth. In effect, however much he may deny it, the oversocialized leftist wants to integrate the black man into the system and make him adopt its values.

30. We certainly do not claim that leftists, even of the oversocialized type, NEVER rebel against the fundamental values of our society. Clearly they sometimes do. Some oversocialized leftists have gone so far as to rebel against one of modern society’s most important principles by engaging in physical violence. By their own account, violence is for them a form of “liberation.” In other words, by committing violence they break through the psychological restraints that have been trained into them. Because they are oversocialized these restraints have been more confining for them than for others; hence their need to break free of them. But they usually justify their rebellion in terms of mainstream values. If they engage in violence they claim to be fighting against racism or the like.

31. We realize that many objections could be raised to the foregoing thumbnail sketch of leftist psychology. The real situation is complex, and anything like a complete description of it would take several volumes even if the necessary data were available. We claim only to have indicated very roughly the two most important tendencies in the psychology of modern leftism.

32. The problems of the leftist are indicative of the problems of our society as a whole. Low self-esteem, depressive tendencies and defeatism are not restricted to the left. Though they are especially noticeable in the left, they are widespread in our society. And today’s society tries to socialize us to a greater extent than any previous society. We are even told by experts how to eat, how to exercise, how to make love, how to raise our kids and so forth.

THE POWER PROCESS

33. Human beings have a need (probably based in biology) for something that we will call the “power process.” This is closely related to the need for power (which is widely recognized) but is not quite the same thing. The power process has four elements. The three most clear-cut of these we call goal, effort and attainment of goal. (Everyone needs to have goals whose attainment requires effort, and needs to succeed in attaining at least some of his goals.) The fourth element is more difficult to define and may not be necessary for everyone. We call it autonomy and will discuss it later (paragraphs 42-44).

34. Consider the hypothetical case of a man who can have anything he wants just by wishing for it. Such a man has power, but he will develop serious psychological problems. At first he will have a lot of fun, but by and by he will become acutely bored and demoralized. Eventually he may become clinically depressed. History shows that leisured aristocracies tend to become decadent. This is not true of fighting aristocracies that have to struggle to maintain their power. But leisured, secure aristocracies that have no need to exert themselves usually become bored, hedonistic and demoralized, even though they have power. This shows that power is not enough. One must have goals toward which to exercise one’s power.

35. Everyone has goals; if nothing else, to obtain the physical necessities of life: food, water and whatever clothing and shelter are made necessary by the climate. But the leisured aristocrat obtains these things without effort. Hence his boredom and demoralization.

36. Nonattainment of important goals results in death if the goals are physical necessities, and in frustration if nonattainment of the goals is compatible with survival. Consistent failure to attain goals throughout life results in defeatism, low self-esteem or depression.

37, Thus, in order to avoid serious psychological problems, a human being needs goals whose attainment requires effort, and he must have a reasonable rate of success in attaining his goals.

SURROGATE ACTIVITIES

38. But not every leisured aristocrat becomes bored and demoralized. For example, the emperor Hirohito, instead of sinking into decadent hedonism, devoted himself to marine biology, a field in which he became distinguished. When people do not have to exert themselves to satisfy their physical needs they often set up artificial goals for themselves. In many cases they then pursue these goals with the same energy and emotional involvement that they otherwise would have put into the search for physical necessities. Thus the aristocrats of the Roman Empire had their literary pretensions; many European aristocrats a few centuries ago invested tremendous time and energy in hunting, though they certainly didn’t need the meat; other aristocracies have competed for status through elaborate displays of wealth; and a few aristocrats, like Hirohito, have turned to science.

39. We use the term “surrogate activity” to designate an activity that is directed toward an artificial goal that people set up for themselves merely in order to have some goal to work toward, or let us say, merely for the sake of the “fulfillment” that they get from pursuing the goal. Here is a rule of thumb for the identification of surrogate activities. Given a person who devotes much time and energy to the pursuit of goal X, ask yourself this: If he had to devote most of his time and energy to satisfying his biological needs, and if that effort required him to use his physical and mental faculties in a varied and interesting way, would he feel seriously deprived because he did not attain goal X? If the answer is no, then the person’s pursuit of goal X is a surrogate activity. Hirohito’s studies in marine biology clearly constituted a surrogate activity, since it is pretty certain that if Hirohito had had to spend his time working at interesting non-scientific tasks in order to obtain the necessities of life, he would not have felt deprived because he didn’t know all about the anatomy and life-cycles of marine animals. On the other hand the pursuit of sex and love (for example) is not a surrogate activity, because most people, even if their existence were otherwise satisfactory, would feel deprived if they passed their lives without ever having a relationship with a member of the opposite sex. (But pursuit of an excessive amount of sex, more than one really needs, can be a surrogate activity.)

40. In modern industrial society only minimal effort is necessary to satisfy one’s physical needs. It is enough to go through a training program to acquire some petty technical skill, then come to work on time and exert the very modest effort needed to hold a job. The only requirements are a moderate amount of intelligence and, most of all, simple OBEDIENCE. If one has those, society takes care of one from cradle to grave. (Yes, there is an underclass that cannot take the physical necessities for granted, but we are speaking here of mainstream society.) Thus it is not surprising that modern society is full of surrogate activities. These include scientific work, athletic achievement, humanitarian work, artistic and literary creation, climbing the corporate ladder, acquisition of money and material goods far beyond the point at which they cease to give any additional physical satisfaction, and social activism when it addresses issues that are not important for the activist personally, as in the case of white activists who work for the rights of nonwhite minorities. These are not always PURE surrogate activities, since for many people they may be motivated in part by needs other than the need to have some goal to pursue. Scientific work may be motivated in part by a drive for prestige, artistic creation by a need to express feelings, militant social activism by hostility. But for most people who pursue them, these activities are in large part surrogate activities. For example, the majority of scientists will probably agree that the “fulfillment” they get from their work is more important than the money and prestige they earn.

41. For many if not most people, surrogate activities are less satisfying than the pursuit of real goals (that is, goals that people would want to attain even if their need for the power process were already fulfilled). One indication of this is the fact that, in many or most cases, people who are deeply involved in surrogate activities are never satisfied, never at rest. Thus the money-maker constantly strives for more and more wealth. The scientist no sooner solves one problem than he moves on to the next. The long-distance runner drives himself to run always farther and faster. Many people who pursue surrogate activities will say that they get far more fulfillment from these activities than they do from the “mundane” business of satisfying their biological needs, but that is because in our society the effort needed to satisfy the biological needs has been reduced to triviality. More importantly, in our society people do not satisfy their biological needs AUTONOMOUSLY but by functioning as parts of an immense social machine. In contrast, people generally have a great deal of autonomy in pursuing their surrogate activities.

AUTONOMY

42. Autonomy as a part of the power process may not be necessary for every individual. But most people need a greater or lesser degree of autonomy in working toward their goals. Their efforts must be undertaken on their own initiative and must be under their own direction and control. Yet most people do not have to exert this initiative, direction and control as single individuals. It is usually enough to act as a member of a SMALL group. Thus if half a dozen people discuss a goal among themselves and make a successful joint effort to attain that goal, their need for the power process will be served. But if they work under rigid orders handed down from above that leave them no room for autonomous decision and initiative, then their need for the power process will not be served. The same is true when decisions are made on a collective basis if the group making the collective decision is so large that the role of each individual is insignificant. [5]

43. It is true that some individuals seem to have little need for autonomy. Either their drive for power is weak or they satisfy it by identifying themselves with some powerful organization to which they belong. And then there are unthinking, animal types who seem to be satisfied with a purely physical sense of power (the good combat soldier, who gets his sense of power by developing fighting skills that he is quite content to use in blind obedience to his superiors).

44. But for most people it is through the power process—having a goal, making an AUTONOMOUS effort and attaining the goal—that self-esteem, self-confidence and a sense of power are acquired. When one does not have adequate opportunity to go through the power process the consequences are (depending on the individual and on the way the power process is disrupted) boredom, demoralization, low self-esteem, inferiority feelings, defeatism, depression, anxiety, guilt, frustration, hostility, spouse or child abuse, insatiable hedonism, abnormal sexual behavior, sleep disorders, eating disorders, etc. [6]

SOURCES OF SOCIAL PROBLEMS

45. Any of the foregoing symptoms can occur in any society, but in modern industrial society they are present on a massive scale. We aren’t the first to mention that the world today seems to be going crazy. This sort of thing is not normal for human societies. There is good reason to believe that primitive man suffered from less stress and frustration and was better satisfied with his way of life than modern man is. It is true that not all was sweetness and light in primitive societies. Abuse of women was common among the Australian aborigines, transexuality was fairly common among some of the American Indian tribes. But it does appear that GENERALLY SPEAKING the kinds of problems that we have listed in the preceding paragraph were far less common among primitive peoples than they are in modern society.

46. We attribute the social and psychological problems of modern society to the fact that that society requires people to live under conditions radically different from those under which the human race evolved and to behave in ways that conflict with the patterns of behavior that the human race developed while living under the earlier conditions. It is clear from what we have already written that we consider lack of opportunity to properly experience the power process as the most important of the abnormal conditions to which modern society subjects people. But it is not the only one. Before dealing with disruption of the power process as a source of social problems we will discuss some of the other sources.

47. Among the abnormal conditions present in modern industrial society are excessive density of population, isolation of man from nature, excessive rapidity of social change and the breakdown of natural small-scale communities such as the extended family, the village or the tribe.

48. It is well known that crowding increases stress and aggression. The degree of crowding that exists today and the isolation of man from nature are consequences of technological progress. All pre-industrial societies were predominantly rural. The Industrial Revolution vastly increased the size of cities and the proportion of the population that lives in them, and modern agricultural technology has made it possible for the Earth to support a far denser population than it ever did before. (Also, technology exacerbates the effects of crowding because it puts increased disruptive powers in people’s hands. For example, a variety of noise- making devices: power mowers, radios, motorcycles, etc. If the use of these devices is unrestricted, people who want peace and quiet are frustrated by the noise. If their use is restricted, people who use the devices are frustrated by the regulations. But if these machines had never been invented there would have been no conflict and no frustration generated by them.)

49. For primitive societies the natural world (which usually changes only slowly) provided a stable framework and therefore a sense of security. In the modern world it is human society that dominates nature rather than the other way around, and modern society changes very rapidly owing to technological change. Thus there is no stable framework.

50. The conservatives are fools: They whine about the decay of traditional values, yet they enthusiastically support technological progress and economic growth. Apparently it never occurs to them that you can’t make rapid, drastic changes in the technology and the economy of a society without causing rapid changes in all other aspects of the society as well, and that such rapid changes inevitably break down traditional values.

51. The breakdown of traditional values to some extent implies the breakdown of the bonds that hold together traditional small-scale social groups. The disintegration of small-scale social groups is also promoted by the fact that modern conditions often require or tempt individuals to move to new locations, separating themselves from their communities. Beyond that, a technological society HAS TO weaken family ties and local communities if it is to function efficiently. In modern society an individual’s loyalty must be first to the system and only secondarily to a small-scale community, because if the internal loyalties of small-scale communities were stronger than loyalty to the system, such communities would pursue their own advantage at the expense of the system.

52. Suppose that a public official or a corporation executive appoints his cousin, his friend or his co- religionist to a position rather than appointing the person best qualified for the job. He has permitted personal loyalty to supersede his loyalty to the system, and that is “nepotism” or “discrimination,” both of which are terrible sins in modern society. Would-be industrial societies that have done a poor job of subordinating personal or local loyalties to loyalty to the system are usually very inefficient. (Look at Latin America.) Thus an advanced industrial society can tolerate only those small-scale communities that are emasculated, tamed and made into tools of the system. [7]

53. Crowding, rapid change and the breakdown of communities have been widely recognized as sources of social problems. But we do not believe they are enough to account for the extent of the problems that are seen today.

54. A few pre-industrial cities were very large and crowded, yet their inhabitants do not seem to have suffered from psychological problems to the same extent as modern man. In America today there still are uncrowded rural areas, and we find there the same problems as in urban areas, though the problems tend to be less acute in the rural areas. Thus crowding does not seem to be the decisive factor.

55. On the growing edge of the American frontier during the 19th century, the mobility of the population probably broke down extended families and small-scale social groups to at least the same extent as these are broken down today. In fact, many nuclear families lived by choice in such isolation, having no neighbors within several miles, that they belonged to no community at all, yet they do not seem to have developed problems as a result.

56. Furthermore, change in American frontier society was very rapid and deep. A man might be born and raised in a log cabin, outside the reach of law and order and fed largely on wild meat; and by the time he arrived at old age he might be working at a regular job and living in an ordered community with effective law enforcement. This was a deeper change than that which typically occurs in the life of a modern individual, yet it does not seem to have led to psychological problems. In fact, 19th century American society had an optimistic and self-confident tone, quite unlike that of today’s society. [8]

57. The difference, we argue, is that modern man has the sense (largely justified) that change is IMPOSED on him, whereas the 19th century frontiersman had the sense (also largely justified) that he created change himself, by his own choice. Thus a pioneer settled on a piece of land of his own choosing and made it into a farm through his own effort. In those days an entire county might have only a couple of hundred inhabitants and was a far more isolated and autonomous entity than a modern county is. Hence the pioneer farmer participated as a member of a relatively small group in the creation of a new, ordered community. One may well question whether the creation of this community was an improvement, but at any rate it satisfied the pioneer’s need for the power process.

58. It would be possible to give other examples of societies in which there has been rapid change and/or lack of close community ties without the kind of massive behavioral aberration that is seen in today’s industrial society. We contend that the most important cause of social and psychological problems in modern society is the fact that people have insufficient opportunity to go through the power process in a normal way. We don’t mean to say that modern society is the only one in which the power process has been disrupted. Probably most if not all civilized societies have interfered with the power process to a greater or lesser extent. But in modern industrial society the problem has become particularly acute. Leftism, at least in its recent (mid- to late-20th century) form, is in part a symptom of deprivation with respect to the power process.

DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY

59. We divide human drives into three groups: (1) those drives that can be satisfied with minimal effort; (2) those that can be satisfied but only at the cost of serious effort; (3) those that cannot be adequately satisfied no matter how much effort one makes. The power process is the process of satisfying the drives of the second group. The more drives there are in the third group, the more there is frustration, anger, eventually defeatism, depression, etc.

60. In modern industrial society natural human drives tend to be pushed into the first and third groups, and the second group tends to consist increasingly of artificially created drives.

61. In primitive societies, physical necessities generally fall into group 2: They can be obtained, but only at the cost of serious effort. But modern society tends to guaranty the physical necessities to everyone [9] in exchange for only minimal effort, hence physical needs are pushed into group 1. (There may be disagreement about whether the effort needed to hold a job is “minimal”; but usually, in lower- to middle- level jobs, whatever effort is required is merely that of OBEDIENCE. You sit or stand where you are told to sit or stand and do what you are told to do in the way you are told to do it. Seldom do you have to exert yourself seriously, and in any case you have hardly any autonomy in work, so that the need for the power process is not well served.)

62. Social needs, such as sex, love and status, often remain in group 2 in modern society, depending on the situation of the individual. [10] But, except for people who have a particularly strong drive for status, the effort required to fulfill the social drives is insufficient to satisfy adequately the need for the power process.

63. So certain artificial needs have been created that fall into group 2, hence serve the need for the power process. Advertising and marketing techniques have been developed that make many people feel they need things that their grandparents never desired or even dreamed of. It requires serious effort to earn enough money to satisfy these artificial needs, hence they fall into group 2. (But see paragraphs 80-82.) Modern man must satisfy his need for the power process largely through pursuit of the artificial needs created by the advertising and marketing industry [11], and through surrogate activities.

64. It seems that for many people, maybe the majority, these artificial forms of the power process are insufficient. A theme that appears repeatedly in the writings of the social critics of the second half of the 20th century is the sense of purposelessness that afflicts many people in modern society. (This purposelessness is often called by other names such as “anomic” or “middle-class vacuity.”) We suggest that the so-called “identity crisis” is actually a search for a sense of purpose, often for commitment to a suitable surrogate activity. It may be that existentialism is in large part a response to the purposelessness of modern life. [12] Very widespread in modern society is the search for “fulfillment.” But we think that for the majority of people an activity whose main goal is fulfillment (that is, a surrogate activity) does not bring completely satisfactory fulfillment. In other words, it does not fully satisfy the need for the power process. (See paragraph 41.) That need can be fully satisfied only through activities that have some external goal, such as physical necessities, sex, love, status, revenge, etc.

65. Moreover, where goals are pursued through earning money, climbing the status ladder or functioning as part of the system in some other way, most people are not in a position to pursue their goals AUTONOMOUSLY. Most workers are someone else’s employee and, as we pointed out in paragraph 61, must spend their days doing what they are told to do in the way they are told to do it. Even people who are in business for themselves have only limited autonomy. It is a chronic complaint of small-business persons and entrepreneurs that their hands are tied by excessive government regulation. Some of these regulations are doubtless unnecessary, but for the most part government regulations are essential and inevitable parts of our extremely complex society. A large portion of small business today operates on the franchise system. It was reported in the Wall Street Journal a few years ago that many of the franchise-granting companies require applicants for franchises to take a personality test that is designed to EXCLUDE those who have creativity and initiative, because such persons are not sufficiently docile to go along obediently with the franchise system. This excludes from small business many of the people who most need autonomy.

66. Today people live more by virtue of what the system does FOR them or TO them than by virtue of what they do for themselves. And what they do for themselves is done more and more along channels laid down by the system. Opportunities tend to be those that the system provides, the opportunities must be exploited in accord with rules and regulations [13], and techniques prescribed by experts must be followed if there is to be a chance of success.

67. Thus the power process is disrupted in our society through a deficiency of real goals and a deficiency of autonomy in the pursuit of goals. But it is also disrupted because of those human drives that fall into group 3: the drives that one cannot adequately satisfy no matter how much effort one makes. One of these drives is the need for security. Our lives depend on decisions made by other people; we have no control over these decisions and usually we do not even know the people who make them. (“We live in a world in which relatively few people—maybe 500 or 1,000—make the important decisions”—Philip B. Heymann of Harvard Law School, quoted by Anthony Lewis, New York Times, April 21, 1995.) Our lives depend on whether safety standards at a nuclear power plant are properly maintained; on how much pesticide is allowed to get into our food or how much pollution into our air; on how skillful (or incompetent) our doctor is; whether we lose or get a job may depend on decisions made by government economists or corporation executives; and so forth. Most individuals are not in a position to secure themselves against these threats to more [than] a very limited extent. The individual’s search for security is therefore frustrated, which leads to a sense of powerlessness.

68. It may be objected that primitive man is physically less secure than modern man, as is shown by his shorter life expectancy; hence modern man suffers from less, not more than the amount of insecurity that is normal for human beings. But psychological security does not closely correspond with physical security. What makes us FEEL secure is not so much objective security as a sense of confidence in our ability to take care of ourselves. Primitive man, threatened by a fierce animal or by hunger, can fight in self-defense or travel in search of food. He has no certainty of success in these efforts, but he is by no means helpless against the things that threaten him. The modern individual on the other hand is threatened by many things against which he is helpless: nuclear accidents, carcinogens in food, environmental pollution, war, increasing taxes, invasion of his privacy by large organizations, nationwide social or economic phenomena that may disrupt his way of life.

69. It is true that primitive man is powerless against some of the things that threaten him; disease for example. But he can accept the risk of disease stoically. It is part of the nature of things, it is no one’s fault, unless it is the fault of some imaginary, impersonal demon. But threats to the modern individual tend to be MAN-MADE. They are not the results of chance but are IMPOSED on him by other persons whose decisions he, as an individual, is unable to influence. Consequently he feels frustrated, humiliated and angry.

70. Thus primitive man for the most part has his security in his own hands (either as an individual or as a member of a SMALL group) whereas the security of modern man is in the hands of persons or organizations that are too remote or too large for him to be able personally to influence them. So modern man’s drive for security tends to fall into groups 1 and 3; in some areas (food, shelter etc.) his security is assured at the cost of only trivial effort, whereas in other areas he CANNOT attain security. (The foregoing greatly simplifies the real situation, but it does indicate in a rough, general way how the condition of modern man differs from that of primitive man.)

71. People have many transitory drives or impulses that are necessarily frustrated in modern life, hence fall into group 3. One may become angry, but modern society cannot permit fighting. In many situations it does not even permit verbal aggression. When going somewhere one may be in a hurry, or one may be in a mood to travel slowly, but one generally has no choice but to move with the flow of traffic and obey the traffic signals. One may want to do one’s work in a different way, but usually one can work only according to the rules laid down by one’s employer. In many other ways as well, modern man is strapped down by a network of rules and regulations (explicit or implicit) that frustrate many of his impulses and thus interfere with the power process. Most of these regulations cannot be dispensed with, because they are necessary for the functioning of industrial society.

72. Modern society is in certain respects extremely permissive. In matters that are irrelevant to the functioning of the system we can generally do what we please. We can believe in any religion we like (as long as it does not encourage behavior that is dangerous to the system). We can go to bed with anyone we like (as long as we practice “safe sex”). We can do anything we like as long as it is UNIMPORTANT. But in all IMPORTANT matters the system tends increasingly to regulate our behavior.

73. Behavior is regulated not only through explicit rules and not only by the government. Control is often exercised through indirect coercion or through psychological pressure or manipulation, and by organizations other than the government, or by the system as a whole. Most large organizations use some form of propaganda [14] to manipulate public attitudes or behavior. Propaganda is not limited to “commercials” and advertisements, and sometimes it is not even consciously intended as propaganda by the people who make it. For instance, the content of entertainment programming is a powerful form of propaganda. An example of indirect coercion: There is no law that says we have to go to work every day and follow our employer’s orders. Legally there is nothing to prevent us from going to live in the wild like primitive people or from going into business for ourselves. But in practice there is very little wild country left, and there is room in the economy for only a limited number of small business owners. Hence most of us can survive only as someone else’s employee.

74. We suggest that modern man’s obsession with longevity, and with maintaining physical vigor and sexual attractiveness to an advanced age, is a symptom of unfulfillment resulting from deprivation with respect to the power process. The “mid-life crisis” also is such a symptom. So is the lack of interest in having children that is fairly common in modern society but almost unheard-of in primitive societies.

75. In primitive societies life is a succession of stages. The needs and purposes of one stage having been fulfilled, there is no particular reluctance about passing on to the next stage. A young man goes through the power process by becoming a hunter, hunting not for sport or for fulfillment but to get meat that is necessary for food. (In young women the process is more complex, with greater emphasis on social power; we won’t discuss that here.) This phase having been successfully passed through, the young man has no reluctance about settling down to the responsibilities of raising a family. (In contrast, some modern people indefinitely postpone having children because they are too busy seeking some kind of “fulfillment.” We suggest that the fulfillment they need is adequate experience of the power process—with real goals instead of the artificial goals of surrogate activities.) Again, having successfully raised his children, going through the power process by providing them with the physical necessities, the primitive man feels that his work is done and he is prepared to accept old age (if he survives that long) and death. Many modern people, on the other hand, are disturbed by the prospect of physical deterioration and death, as is shown by the amount of effort they expend trying to maintain their physical condition, appearance and health. We argue that this is due to unfulfillment resulting from the fact that they have never put their physical powers to any practical use, have never gone through the power process using their bodies in a serious way. It is not the primitive man, who has used his body daily for practical purposes, who fears the deterioration of age, but the modern man, who has never had a practical use for his body beyond walking from his car to his house. It is the man whose need for the power process has been satisfied during his life who is best prepared to accept the end of that life.

76. In response to the arguments of this section someone will say, “Society must find a way to give people the opportunity to go through the power process.” For such people the value of the opportunity is destroyed by the very fact that society gives it to them. What they need is to find or make their own opportunities. As long as the system GIVES them their opportunities it still has them on a leash. To attain autonomy they must get off that leash.

HOW SOME PEOPLE ADJUST

77. Not everyone in industrial-technological society suffers from psychological problems. Some people even profess to be quite satisfied with society as it is. We now discuss some of the reasons why people differ so greatly in their response to modern society.

78. First, there doubtless are differences in the strength of the drive for power. Individuals with a weak drive for power may have relatively little need to go through the power process, or at least relatively little need for autonomy in the power process. These are docile types who would have been happy as plantation darkies in the Old South. (We don’t mean to sneer at the “plantation darkies” of the Old South. To their credit, most of the slaves were NOT content with their servitude. We do sneer at people who ARE content with servitude.)

79. Some people may have some exceptional drive, in pursuing which they satisfy their need for the power process. For example, those who have an unusually strong drive for social status may spend their whole lives climbing the status ladder without ever getting bored with that game.

80. People vary in their susceptibility to advertising and marketing techniques. Some are so susceptible that, even if they make a great deal of money, they cannot satisfy their constant craving for the the shiny new toys that the marketing industry dangles before their eyes. So they always feel hard-pressed financially even if their income is large, and their cravings are frustrated.

81. Some people have low susceptibility to advertising and marketing techniques. These are the people who aren’t interested in money. Material acquisition does not serve their need for the power process.

82. People who have medium susceptibility to advertising and marketing techniques are able to earn enough money to satisfy their craving for goods and services, but only at the cost of serious effort (putting in overtime, taking a second job, earning promotions, etc.). Thus material acquisition serves their need for the power process. But it does not necessarily follow that their need is fully satisfied. They may have insufficient autonomy in the power process (their work may consist of following orders) and some of their drives may be frustrated (e.g., security, aggression). (We are guilty of oversimplification in paragraphs 80- 82 because we have assumed that the desire for material acquisition is entirely a creation of the advertising and marketing industry. Of course it’s not that simple. [11]

83. Some people partly satisfy their need for power by identifying themselves with a powerful organization or mass movement. An individual lacking goals or power joins a movement or an organization, adopts its goals as his own, then works toward those goals. When some of the goals are attained, the individual, even though his personal efforts have played only an insignificant part in the attainment of the goals, feels (through his identification with the movement or organization) as if he had gone through the power process. This phenomenon was exploited by the fascists, nazis and communists. Our society uses it too, though less crudely. Example: Manuel Noriega was an irritant to the U.S. (goal: punish Noriega). The U.S. invaded Panama (effort) and punished Noriega (attainment of goal). Thus the U.S. went through the power process and many Americans, because of their identification with the U.S., experienced the power process vicariously. Hence the widespread public approval of the Panama invasion; it gave people a sense of power. [15] We see the same phenomenon in armies, corporations, political parties, humanitarian organizations, religious or ideological movements. In particular, leftist movements tend to attract people who are seeking to satisfy their need for power. But for most people identification with a large organization or a mass movement does not fully satisfy the need for power.

84. Another way in which people satisfy their need for the power process is through surrogate activities. As we explained in paragraphs 38-40, a surrogate activity is an activity that is directed toward an artificial goal that the individual pursues for the sake of the “fulfillment” that he gets from pursuing the goal, not because he needs to attain the goal itself. For instance, there is no practical motive for building enormous muscles, hitting a little ball into a hole or acquiring a complete series of postage stamps. Yet many people in our society devote themselves with passion to bodybuilding, golf or stamp-collecting. Some people are more “other-directed” than others, and therefore will more readily attach importance to a surrogate activity simply because the people around them treat it as important or because society tells them it is important. That is why some people get very serious about essentially trivial activities such as sports, or bridge, or chess, or arcane scholarly pursuits, whereas others who are more clear-sighted never see these things as anything but the surrogate activities that they are, and consequently never attach enough importance to them to satisfy their need for the power process in that way. It only remains to point out that in many cases a person’s way of earning a living is also a surrogate activity. Not a PURE surrogate activity, since part of the motive for the activity is to gain the physical necessities and (for some people) social status and the luxuries that advertising makes them want. But many people put into their work far more effort than is necessary to earn whatever money and status they require, and this extra effort constitutes a surrogate activity. This extra effort, together with the emotional investment that accompanies it, is one of the most potent forces acting toward the continual development and perfecting of the system, with negative consequences for individual freedom (see paragraph 131). Especially, for the most creative scientists and engineers, work tends to be largely a surrogate activity. This point is so important that it deserves a separate discussion, which we shall give in a moment (paragraphs 87-92).

85. In this section we have explained how many people in modern society do satisfy their need for the power process to a greater or lesser extent. But we think that for the majority of people the need for the power process is not fully satisfied. In the first place, those who have an insatiable drive for status, or who get firmly “hooked” on a surrogate activity, or who identify strongly enough with a movement or organization to satisfy their need for power in that way, are exceptional personalities. Others are not fully satisfied with surrogate activities or by identification with an organization (see paragraphs 41, 64). In the second place, too much control is imposed by the system through explicit regulation or through socialization, which results in a deficiency of autonomy, and in frustration due to the impossibility of attaining certain goals and the necessity of restraining too many impulses.

86. But even if most people in industrial-technological society were well satisfied, we (FC) would still be opposed to that form of society, because (among other reasons) we consider it demeaning to fulfill one’s need for the power process through surrogate activities or through identification with an organization, rather than through pursuit of real goals.

THE MOTIVES OF SCIENTISTS

87. Science and technology provide the most important examples of surrogate activities. Some scientists claim that they are motivated by “curiosity” or by a desire to “benefit humanity.” But it is easy to see that neither of these can be the principal motive of most scientists. As for “curiosity,” that notion is simply absurd. Most scientists work on highly specialized problems that are not the object of any normal curiosity. For example, is an astronomer, a mathematician or an entomologist curious about the properties of isopropyltrimethylmethane? Of course not. Only a chemist is curious about such a thing, and he is curious about it only because chemistry is his surrogate activity. Is the chemist curious about the appropriate classification of a new species of beetle? No. That question is of interest only to the entomologist, and he is interested in it only because entomology is his surrogate activity. If the chemist and the entomologist had to exert themselves seriously to obtain the physical necessities, and if that effort exercised their abilities in an interesting way but in some nonscientific pursuit, then they wouldn’t give a damn about isopropyltrimethylmethane or the classification of beetles. Suppose that lack of funds for postgraduate education had led the chemist to become an insurance broker instead of a chemist. In that case he would have been very interested in insurance matters but would have cared nothing about isopropyltrimethylmethane. In any case it is not normal to put into the satisfaction of mere curiosity the amount of time and effort that scientists put into their work. The “curiosity” explanation for the scientists’ motive just doesn’t stand up.

88. The “benefit of humanity” explanation doesn’t work any better. Some scientific work has no conceivable relation to the welfare of the human race—most of archaeology or comparative linguistics for example. Some other areas of science present obviously dangerous possibilities. Yet scientists in these areas are just as enthusiastic about their work as those who develop vaccines or study air pollution. Consider the case of Dr. Edward Teller, who had an obvious emotional involvement in promoting nuclear power plants. Did this involvement stem from a desire to benefit humanity? If so, then why didn’t Dr. Teller get emotional about other “humanitarian” causes? If he was such a humanitarian then why did he help to develop the H- bomb? As with many other scientific achievements, it is very much open to question whether nuclear power plants actually do benefit humanity. Does the cheap electricity outweigh the accumulating waste and the risk of accidents? Dr. Teller saw only one side of the question. Clearly his emotional involvement with nuclear power arose not from a desire to “benefit humanity” but from a personal fulfillment he got from his work and from seeing it put to practical use.

89. The same is true of scientists generally. With possible rare exceptions, their motive is neither curiosity nor a desire to benefit humanity but the need to go through the power process: to have a goal (a scientific problem to solve), to make an effort (research) and to attain the goal (solution of the problem.) Science is a surrogate activity because scientists work mainly for the fulfillment they get out of the work itself.

90. Of course, it’s not that simple. Other motives do play a role for many scientists. Money and status for example. Some scientists may be persons of the type who have an insatiable drive for status (see paragraph 79) and this may provide much of the motivation for their work. No doubt the majority of scientists, like the majority of the general population, are more or less susceptible to advertising and marketing techniques and need money to satisfy their craving for goods and services. Thus science is not a PURE surrogate activity. But it is in large part a surrogate activity.

91. Also…

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[d45e244401...](https://github.com/timothymtorres/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Thursday 2022-10-20 01:26:41 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[223e8bfd96...](https://github.com/ArtemisStation/artemis-tg/commit/223e8bfd96a7762f0d23dd9b789fa90be1a572ec)
#### Thursday 2022-10-20 02:24:11 by Time-Green

Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

---
## [sd-webui/stable-diffusion-webui](https://github.com/sd-webui/stable-diffusion-webui)@[468d468fbb...](https://github.com/sd-webui/stable-diffusion-webui/commit/468d468fbb4c48f213db38ebbc1be9809cbfc6be)
#### Thursday 2022-10-20 02:57:58 by Ruslan Sheptolut

Don't ask about restoring stash if nothing was stashed (#1533)

# Description

Minor quality of life update.

Recently launching the webui.bat became a bit more annoying, as it
always asks about restoring changes, even if I have none, and then it
needs another interaction for no reason (pause>nul).

This change makes sure the interaction is only needed when there were
changes stashed, and removes the second pause.

Yesterday I double clicked the shortcut to start the Stable Horde worker
overnight, and even noticed the "Y/N" prompt, but went to bed not
realizing it also does the (pause>nul) after that... No reason to be
this intrusive.

Closes: #1532

# Checklist:

- [X] I have changed the base branch to `dev`
- [X] I have performed a self-review of my own code
- [X] I have commented my code in hard-to-understand areas
- [X] I have made corresponding changes to the documentation

---
## [repjackson/dreddit](https://github.com/repjackson/dreddit)@[e549c54cb5...](https://github.com/repjackson/dreddit/commit/e549c54cb583b7978125519bb3bd8df80164d62e)
#### Thursday 2022-10-20 03:42:55 by john smith

fix last emotion icons and make them smaller, this is actually fun holy shit

---
## [Ariq139/GFD-Studio-Preset-Collection](https://github.com/Ariq139/GFD-Studio-Preset-Collection)@[4d090bbac2...](https://github.com/Ariq139/GFD-Studio-Preset-Collection/commit/4d090bbac2fc81d12a5f990da70974358c43cf7c)
#### Thursday 2022-10-20 04:35:53 by Cherry Cream Soda

Suda51CharacterMaterial.yml

This shit looks awful bruhhh goddamn
The flags are kind of trashy buttt the end result is good. Mostly relies on a heavily edited Type0 so yoink that if u want

---
## [Pointerbender/rust](https://github.com/Pointerbender/rust)@[9e8f53d09a...](https://github.com/Pointerbender/rust/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Thursday 2022-10-20 05:38:18 by bors

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
## [monster860/Yogstation-TG](https://github.com/monster860/Yogstation-TG)@[9118cab4fd...](https://github.com/monster860/Yogstation-TG/commit/9118cab4fda02a964b40895aa7aedf3dd55580ef)
#### Thursday 2022-10-20 05:59:33 by Redmoogle

ports fake viruses from tgstation (#15412)

* fakevirus

* fuck you too byond

* Update code/datums/status_effects/debuffs.dm

Co-authored-by: tattax <71668564+tattax@users.noreply.github.com>

Co-authored-by: tattax <71668564+tattax@users.noreply.github.com>

---
## [newstools/2022-iol](https://github.com/newstools/2022-iol)@[7a15192461...](https://github.com/newstools/2022-iol/commit/7a15192461ed25a1c3dc07cf77adf80dc591f428)
#### Thursday 2022-10-20 06:16:05 by Billy Einkamerer

Created Text For URL [www.iol.co.za/news/news/world/watch-british-coroner-rules-that-social-media-were-to-blame-after-14-year-old-girl-committed-suicide-3e0b5bd6-01ad-497c-bc55-0194e31f7207]

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[fc7c186957...](https://github.com/Sealed101/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Thursday 2022-10-20 07:01:28 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [19hhowton/Practice_Questions](https://github.com/19hhowton/Practice_Questions)@[d21c8f15d1...](https://github.com/19hhowton/Practice_Questions/commit/d21c8f15d1bec7aea47c7beadff8659b128eb49d)
#### Thursday 2022-10-20 07:08:42 by 19hhowton

Update Strings

Optional Adds

🌶️ Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'


🌶️ Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'


🌶️ Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'



🌶️ You need to create an if statement to send accurate alerts to passengers.
`boarding_call="Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."`
    1. Oh no! Replace Good Evening with Good Morning in the below boarding call string. You would use two string functions.
    2.  Check if the string has “AL”. If so, then print "Welcome to Air Lines." in the consol. You would use one string functions.
    3.  Check if the string says AM or PM. If AM print “Passengers are requested to have their breakfast.”


🌶️ Write a Python function to create the HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

---
## [boost-entropy-typescript/apollo-server](https://github.com/boost-entropy-typescript/apollo-server)@[7c763c0f19...](https://github.com/boost-entropy-typescript/apollo-server/commit/7c763c0f19d9164e094773d41664659001d835e7)
#### Thursday 2022-10-20 09:07:38 by Trevor Scheer

Remove `postinstall` script (#7037)

Having a `postinstall` script provides a (sometimes) minor convenience
for developers cloning the repo and updating dependencies in that
`compile` is run whenever an `install` occurs. This also has indirectly
led us to an implicit dependency in the publish and testing workflows
that an install implies that a build is performed.

The _inconvenience_ posed by this is mentioned here:

https://github.com/apollographql/typescript-repo-template/pull/92#issuecomment-1277787991

...in summary, if the repo is not in a compilable state but you want to
`install` due to a dependency update, the command will exit non-zero and
fail due to the `postinstall` script failure. The "solution" to this is
to run `npm install --ignore-scripts` which is cumbersome.

`pretest` now runs the standard `compile` script. Running `tsc` against the
whole project (including test files) is unnecessary.

This repo expects that all publishes occur via `changeset`. The
changeset action docs recommend the publish command to include the build
command: https://github.com/changesets/action#inputs. I think this could
be similarly accomplished via lifecycle scripts (`prepack`,
`prepublishOnly`) but they would need to be duplicated within each
individual package and they would need to trigger a build at the
parent's level due to interdependencies. As such, I chose the option which
allowed me to keep all of that logic in top-level scripts.

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [rajkumarnewgit/ECOM_PROJECT](https://github.com/rajkumarnewgit/ECOM_PROJECT)@[0d2d321733...](https://github.com/rajkumarnewgit/ECOM_PROJECT/commit/0d2d321733c454c2e12d59380d72d16892023ada)
#### Thursday 2022-10-20 11:41:10 by Harish Raj

Create README.md

This is my 'eCommerce Website With Visitor Tracking System' project.
CHAPTER 1 INTRODUCTION:- The broad definition of e-commerce transactions refers to the selling and buying of products and services over computer-mediated networks while the end process of payment and delivery is managed offline. Electronic Commerce (e-commerce) is defined as the conduct of commerce in goods and services, with the assistance of telecommunications and telecommunications-based tools such as the Internet. E-commerce is often used in a much broader sense, to mean essentially the same as “electronic business” (EB). E-commerce encompasses many areas, which include electronic catalogues that refer to means whereby sellers can communicate their offerings to potential buyers.

1.1 BACKGROUND: - E-Commerce is fast gaining ground as an accepted and used business paradigm. More and more business houses are implementing web sites providing functionality for performing commercial transaction over the web. It is reasonable to say that the process of shopping on the web is becoming commonplace. The eCommerce websites to track users in order to maximize their turnover. Simply put, the more insight a commercial website has into its customer’s actions and interest, the better it can present its product to the specific user, the more it will sell. The central concept of the application is to allow the customer to shop virtually using the Internet and allow customers to buy the items and products of their desire from the store. and allow customers to buy the items and articles of their desire from the store. An online store is a virtual store on the Internet where customers can browse the category and select products of interest. The selected items may be collected in a shopping cart. At checkout time, the items in the shopping cart will be presented as an order. At that time, more information will be needed to complete the transaction. Usually, the customer will be asked to fill or select a billing address, a shipping address, and payment information such as Card or Cash on Delivery. An email notification is sent to the customer as soon as the order is placed.

1.2 OB0JECTIVE: - The Online Shopping is the process whereby consumers directly buy goods and services without any intermediary service over the internet. The goal of this website is to develop a web-based interface for eCommerce website, the website would be easy to use and hence the shopping experience pleasant for the users. The main goal of this website is: • To develop an easy to use web-based interface where customers can search for products, view a complete description of the product and order the product. • Reach out to a larger audience - internet access is becoming so mainstream now that your product/service can reach almost everyone on the planet with an internet-enabled device. • Your virtual shop remains open and operational 24x7 even if you/your staff are not working- this might not be wholly true if your product is a service-which requires immediate human-intervention. • In most cases; you need not maintain the whole stock of products - again this varies for different business models and will work greatly if you have a good supplier who does not defaults on supplies and a good shipping partner/team who work in sync for delivery. • You build your brand more quickly - as more people will know and talk and post and blog about you on social networks. • Once your brand is built you can diversify easily and also pull out of a certain segment if that does not work out for you with minimal losses - typical example will be Flipkart's music(tunes) store which closed off even being a great initiative. • For most part, setting up a website and maintaining it is lots cheaper given the plethora of hosting services available.

1.3 PURPOSE, SCOPE, APPLICABILITY: - 1.3.1 PURPOSE: - With advancements in technology and with the popularity of the internet, more and more people are turning to the web for a variety of purposes. The internet is no longer limited to searching information or connecting with people but is a platform where you can also buy and sell products. An ecommerce website is a website which allows your business to sell products and services to their online audience. These days, an increasing number of consumers prefer making most of their purchases online and in such a scenario, having an ecommerce website for your business is the need of the hour. The following is a list of the top 5 reasons to have an ecommerce platform: - Wider customer reach-when you sell a product or service through a national or global platform of an ecommerce website, then you tend to reach out to a much wider audience as compared to traditional commerce methods. This gives you a broader audience and hence possibility of better overall sales. Ability to be open 24/7-with an ecommerce website, you will give your audiences to purchase from you not just during regular store hours but throughout the day. Whether it is Sunday or a national holiday, your store is always open. This too helps you to make more sales, hence boosting sales. Better conversion rates-no matter how popular your brand is, if conversion rate is low, then profits will be low. Having an ecommerce platform helps you to increase your conversion rate since people get a chance to immediately buy from you rather than wait to visit the store. Easier to set up-an ecommerce platform is definitely much easier to set up and run than an actual physical store. There are many good website development and management platforms which can easily do this task for you at reasonable rates. It is not just easier but also a lot cheaper. Reduced risk, increased profitability-to manage and run an online store, you need a smaller workforce, thus increasing margin between profits and spending. Also, there is also the advantage of reduced risk which adds to the list of the benefits of having an ecommerce store. Having an ecommerce website gives you a certain competitive edge over those who may still not have gone online. Customers these days are looking for the easiest and cheapest way to make their purchasing and thus search online for their desired products and services. In such a case, the presence of an online store not only helps you to retain existing customers but also attract new ones. 1.3.2 SCOPE: - Nowadays, India is in a completely growing stage of development and we need to update our business to the growing needs of the new generation. There is a huge scope of eCommerce. The current generation completely belongs to e-services. Today, every business and service are going the ‘internet’ way. Everyone prefers e-services and e-governance which are the most preferred ways to connect to the people around the world. According to a report released by an American Information Technology Research & Advisory Corporation known as Garner, “e-commerce in India will probably exceed $6 Billion in profits by 2015, estimating a 70% growth from a year-ago”. Nearly 8 million people did their shopping from one of top 4 online shopping websites in 2012, and the number has grown to 35 million this year. By 2016, this online consumer base will rise to nearly 3 times to 100- million, and over 50 percent of the new buyers could be from Tier-I and Tier-II towns. This makes India one of the wildest-growing e-commerce markets in the Asia Pacific region.

1.3.3 APPLICABILITY: - E-Commerce Website with Visitor Tracking System is applicable in such areas where the people want following tasks to do: • Customers will be able to login/register into the website. • Customers will also be able to easily search for products by using different keywords like name, category wise etc and will be able to refine their results by using filters such as price, product type etc. on the website. • If the user is comfortable with some product then he/ she can purchase the product. • Customers will be able to make payments for their orders by using integrated payment gateway given by the Admin. • Once the payment is done then the user will get the product at the user location. • Customers will be able to receive an email for confirmation after an order placed on the website. • Admin will be able to manage the customers, products, orders etc on the website from the backend. • Provide the basic pages (i.e., about us, Contact Us, FAQ, help) for company information.

CHAPTER 2 SURVEY OF TECHNOLOGY In this project the following technologies are used: -

Python: - Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically typed and garbagecollected. It supports multiple programming paradigms, including procedural, objectoriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library. Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released 2000, introduced features like list comprehensions and a garbage collection system capable of collecting reference cycles. Python 3.0, released 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3. Due to concern about the amount of code written for Python 2, support for Python 2.7 (the last release in the 2.x series) was extended to 2020. Language developer Guido van Rossum shouldered sole responsibility for the project until July 2018 but now shares his leadership as a member of a five-person steering council.

Django Framework: - Django is a Python-based free and open-source web framework, which follows the model-template-view (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established as a non-profit. Django’s primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings files and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models. Some well-known sites that use Django include the Public Broadcasting Service, Instagram, Mozilla, The Washington Times, Bitbucket, and NeXT door. It was used on Pinterest, but later the site moved to a framework built over Flask.

MySQL Database: - MySQL is an open-source relational database management system (RDBMS). Its name is a combination of "My", the name of co-founder Michael Widenius's daughter, and "SQL", the abbreviation for Structured Query Language. The MySQL development project has made its source code available under the terms of the GNU General Public License, as well as under a variety of proprietary agreements. MySQL was owned and sponsored by a single for-profit firm, the Swedish company MySQL AB, now owned by Oracle Corporation. For proprietary use, several paid editions are available, and offer additional functionality. In 2010, when Oracle acquired Sun, Widenius forked the open-source MySQL project to create MariaDB. MySQL is a central component of the LAMP open-source web application software stack (and other "AMP" stacks). LAMP is an acronym for "Linux, Apache, MySQL, Perl/PHP/Python". Applications that use the MySQL database include: TYPO3, MODx, Joomla, WordPress, Simple Machines Forum, phpBB, MyBB, and Drupal. MySQL is also used in many high-profile, large-scale websites, including Google (though not for searches), Facebook, Twitter, Flickr, and YouTube.

HTML: - Hypertext Mark-up Language (HTML) is the standard mark-up language for creating web pages and web applications. With Cascading Style Sheets (CSS) and JavaScript it forms a triad of cornerstone technologies for the World Wide Web. Web browsers receive HTML documents from a webserver or from local storage and render them into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document. HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects, such as interactive forms, may be embedded into the rendered page. It provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as and introduce content into the page directly. Others such as surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page. HTML can embed programs written in a scripting language such as JavaScript which affect the behaviour and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), maintainer of both the HTML and the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.

CSS: - CSS is designed to enable the separation of presentation and content, including layout, colours, and fonts. This separation can improve content accessibility, provide more flexibility and control in the specification of presentation characteristics, enable multiple web pages to share formatting by specifying the relevant CSS in a separate ‘.css’ file, and reduce complexity and repetition in the structural content. Separation of formatting and content also makes it feasible to present the same mark-up page in different styles for different rendering methods, such as on-screen, in print, by voice (via speech-based browser or screen reader), and on Braille-based tactile devices. CSS also has rules for alternate formatting if the content is accessed on a mobile device. The name cascading comes from the specified priority scheme to determine which style rule applies if more than one rule matches a particular element. This cascading priority scheme is predictable.

Bootstrap: - Bootstrap is a free and open-source front-end web framework for designing websites and web applications. It contains HTML- and CSS-based design templates for typography, forms, buttons, navigation and other interface components, as well as optional JavaScript extensions. Unlike many web frameworks, it concerns itself with front-end development only. Bootstrap is the second most-starred project on GitHub, with more than 107,000 stars and 48,000 forks. Bootstrap, originally named Twitter Blueprint, was developed by Mark Otto and Jacob Thornton at Twitter as a framework to encourage consistency across internal tools. Before Bootstrap, various libraries were used for interface development, which led to inconsistencies and a high maintenance burden. According to twitter developer Mark Otto: “A super small group of developers and I got together to design and build a new internal tool and saw an opportunity to do something more. Through that process, we saw ourselves build something much more substantial than another internal tool. Months later, we ended up with an early version of Bootstrap as a way to document and share common design patterns and assets within the company.” After a few months of development by a small group, many developers at Twitter began to contribute to the project as a part of Hack Week, a hackathon-style week for the Twitter development team. It was renamed from Twitter Blueprint to Bootstrap, and released as an open source project on August 19, 2011. It has continued to be maintained by Mark Otto, Jacob Thornton, and a small group of core developers, as well as a large community of contributors.

CHAPTER 3 REQUIREMENT AND ANALYSIS 3.1 PROBLEM DEFINATION: -

This project aims to develop an online shopping for customers with the goal so that it is very easy to shop your loved things from an extensive number of online shopping sites available on the web. With the help of this you can carry out an online shopping from your home. Here is no compelling reason to go to the crowed stores or shopping centres during festival seasons. You simply require a PC or a laptop or a mobile phone and one important payment sending option to shop online. To get to this online shopping system all the customers will need to have an email and password to login and proceed your shopping. The login credentials for an online shopping system are under high security and nobody will have the capacity to crack it easily. Upon successful login the customers can purchase a wide range of things such as mobiles, books, apparel, jewellery, infant care, gifts, tools, etc. can be dispatched using online shopping system. Not just these, you can also purchase from outside nations by few clicks on your mouse. And of course, you will get your requested ordered items at your door step. It is simple. You will pick your favourite items from variety of online shopping sites looking at cost and quality. No need to go physical shops with this you will have more time to spend with your family. It Just need a computer and a payment making options like net banking, credit card, debit card or PayPal. Almost a wide range of things can be brought through online shopping system. You can purchase goods from foreign places from your bedroom and you will get your goods at your home. It is extremely secure. Customer service is accessible.

3.2 REQUIREMENT SPECIFICATION: -

FUNCTIONAL REQUIREMENTS: - Registration: - A new user will have to register in the system by providing essential details in order to view the products in the system. The admin must accept a new user by unblocking him. Login: - A user must login with his user name and password to the system after registration. Add Products The shopping cart project contains different kind of products. The products can be classified into different categories by name. Admin can add new products into the existing system with all its details including an image. View Products: - User can view the list of products based on their names after successful login. A detailed description of a particular product with product name, products details, product image, price can be viewed by users. Delete Products: - Administrator can delete the products based on the stock of that particular product. Search products: - Admin will have a list view of all the existing products. He can also search for a particular product by name. View Order: - Administrator can view the Orders which is generated by the users. He can verify the details of the purchase. Delete Order: - Admin can delete order from the orders list when the product is taken for delivery. Add to cart: - The user can add the desired product into his cart by clicking add to cart option on the product. He can view his cart by clicking on the cart button. All products added by cart can be viewed.

NON-FUNCTIONAL REQUIREMENTS: - i. EFFICIENCY REQUIREMENT: - When an online shopping cart android application implemented customer can purchase product in an efficient manner. ii. RELIABILITY REQUIREMENT: - The system should provide a reliable environment to both customers and owner. All orders should be reaching at the admin without any errors. iii. USABILITY REQUIREMENT: - The android application is designed for user friendly environment and ease of use. iv. IMPLEMENTATION REQUIREMENT: - Implementation of the system using CSS and html in front end with just as back end and it will be used for database connectivity. And the database part is developed by MySQL. Responsive web designing is used for making the website compatible for any type of screen. v. DELIVERY REQUIREMENT: - The whole system is expected to be delivered in four months of time with a weekly evaluation by the project guide.

3.3 PLANNING AND SCHEDULING: -

GANTT CHART: - PERT CHART: -

3.4 SOFTWARE AND HARDWARE REQUIREMENTS: - Hardware Requirements: - ➢ Operating System: - Windows 7 and above ➢ Processor: - Intel i3 or above ➢ Installed Memory (RAM): - Minimum 1 GB ➢ System Type: - 32-bit or 64-bit Operating System Software Requirements: - ➢ Front End: - HTML, CSS, JS, Bootstrap ➢ Back End: - Python Django Framework, MySQL

3.5 PRELIMINARY PRODUCT DESCRIPTION: - This project is a web-based shopping system for an existing shop. The project objective is to deliver the E-Commerce Website with Visitor Tracking System based on Python Django Framework. E-Commerce Website with Visitor Tracking system is the process whereby consumers directly buy goods or products from a seller in real-time, over the Internet. It is a form of electronic commerce. This project is an attempt to provide the advantages of online shopping system to customers of a real shop. It helps buying the products in the shop anywhere through internet. Thus, the customer will get the service of E-Commerce Website and home delivery for that product.

3.6CONCEPTUAL MODEL: -

3.6.1 Event Table: - 3.6.2 Use Case Diagram: - 3.6.3 Sequence Diagram: - 3.6.4 Class Diagram: - 3.6.5 State Chart Diagram: -

CHAPTER 4 SYSTEM DESIGN

4.1 BASIC MODULES: -

Customer Module: - The main purpose of this module is providing all the functionality related to customers. It tracks all the information and details of the customer. We have developed all type of CRUD (Create, Read, Update and Delete) operations of the customers. This is a role-based module where admin can perform each and every operation on data but the customer will be able to view only his/her data, so access level restrictions has also been implemented on the project. Features of Customer Module: - • Admin can add new customers records • Admin can see the list of customers details • Only admin can edit and update the record of the customers • Admin will be able to delete the records of the customers • Customer will be able to see his details • Customer will be able to update his details

Category Module: - The main purpose for developing this module is to manage the category of the product data wise. So, all product category will be managed by admin and customer will be able to see product category. Admin can see the list of all the product category and filter it according to the customers. Features of Category Module: • Admin can manage the category • Admin can edit/delete the category • Admin can see the list of all category • Customer can see category

Product Module: - The main purpose for developing this module is to manage the product. So, all category of product will be managed by admin and customer will be able to see the product. Features of product Module: - • Admin can manage the product • Admin can edit/delete the product • Admin can see the list of all product • Customer can see product

Order Module: - The main purpose for developing this module is to manage the customer orders for the product. So, all orders will be managed by admin and customer will be able to see his order and their payment receipt. Features of Order Module: • Admin can manage the order • Admin can edit/delete the order • Admin can see the list of all order • Customer can see his order Functionality

Admin user: These are the functionality performed by the admin users: - • Login for Admin • Change Password for Admin • Logout Functionality • Dashboard for Admin User • Manage Category • Adding New Category • Edit the Exiting Category • View details of the Category • Listing of all Category • Manage Customer • Adding New Customer • Edit the Exiting Customer • View details of the Customer • Listing of all Customer • Manage Product • Adding New Product • Edit the Exiting Product • View details of the Product • Listing of all Product • Advertising Popular Products • Checking User Activity • Manage Order • Adding New Order • Edit the Exiting Order • View details of the Order • Listing of all Order • Reports of the Project E-Commerce Website with Visitor Tracking System • Report of all Orders 6. Functionality performed by Customer user: - Customer Registration: - • Any customer can register on website using the registration module. • Customer Login: This is the login form, from where customer can login into the system • Customer Payment: Customer can manage all the product payment from this form. • Item Cart: This is item cart form in this project. • Customer Order Receipt: This customer gets order receipt form details. • Customer My Order: This customer gets my order form details. • Change Password: This is the change password module from where customer change his account password.

4.2 DATA DESIGN: - 4.2.1 Schema Design with Data Integrity and Constraints: - 4.2.2 Database Relationship Design: -

4.3 USER INTERFACE DESIGN: -

4.4 SECURITY ISSUES: - ➢ E-commerce Security Risks Currently Faced by Online Retailers Security risks associated with e-commerce can be as a result of human error, an accident or unauthorized access to systems. Online retailers are most likely to face credit card fraud or data errors. Their online stores are also likely to face phishing attacks, distributed denial of service (DDoS) attacks and man-in-the-middle attacks as explained below. Credit Card Fraud: - Credit card fraud is the most common security threat that online retailers face. It occurs when a hacker gains unauthorized access to customers’ personal and payment information. To access this data, the hacker may penetrate the database of an e-commerce site using malicious software programs. At times, a hacker’s intention when stealing customers’ data is to sell it on black markets. Phishing Scams: - E-commerce sites are also prone to phishing scams sent by known or unknown people in form of emails. These scams focus on targeting important user data like credit card numbers and login credentials. An attacker may use a scheme known as social engineering to lure online shoppers to give out their personal information. When sent in an email to an online shopper, a phishing scam may contain a link to a malicious site that resembles an e-commerce site.

➢ Best Practices to Curb the Security Issues in E-commerce Fraud costs online retailers billions of dollars yearly. To solve the security issues in ecommerce, merchants and payment companies should collaboratively come up with effective solutions. Though these security issues are becoming intense with time, there are solutions that online retailers can implement without affecting the user experience of their sites. In other words, they can adopt the following solutions without impacting the customer experience. Require stronger passwords: - The reason why hackers easily gain access to users’ login credentials is that most ecommerce sites fail to ask users to provide stronger passwords. Hackers can utilize algorithms to figure out the passwords easily. A strong password contains a mix of alphabetical letters and numbers. Use SSL Certificates: - It is mandatory for e-commerce websites to have SSL certificates for facilitating secure user connections. These certificates are also useful in authenticating the identity of an online retail business and securing users’ checkout data. They also keep customers of online retail stores protected from financial fraud or information loss.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[032980362e...](https://github.com/git-for-windows/git/commit/032980362e4550007d0a262d8afc807fccb9c88e)
#### Thursday 2022-10-20 12:33:45 by Jeff King

Makefile: force -O0 when compiling with SANITIZE=leak

Compiling with -O2 can interact badly with LSan's leak-checker, causing
false positives. Imagine a simplified example like:

  char *str = allocate_some_string();
  if (some_func(str) < 0)
          die("bad str");
  free(str);

The compiler may eliminate "str" as a stack variable, and just leave it
in a register. The register is preserved through most of the function,
including across the call to some_func(), since we'd eventually need to
free it. But because die() is marked with NORETURN, the compiler knows
that it doesn't need to save registers, and just clobbers it.

When die() eventually exits, the leak-checker runs. It looks in
registers and on the stack for any reference to the memory allocated by
str (which would indicate that it's not leaked), but can't find one.  So
it reports it as a leak.

Neither system is wrong, really. The C standard (mostly section 5.1.2.3)
defines an abstract machine, and compilers are allowed to modify the
program as long as the observable behavior of that abstract machine is
unchanged. Looking at random memory values on the stack is undefined
behavior, and not something that the optimizer needs to support. But
there really isn't any other way for a leak checker to work; it
inherently has to do undefined things like scouring memory for pointers.
So the two things are inherently at odds with each other. We can't fix
it by changing the code, because from the perspective of the program
running in an abstract machine, there is no leak.

This has caused real false positives in the past, like:

  - https://lore.kernel.org/git/patch-v3-5.6-9a44204c4c9-20211022T175227Z-avarab@gmail.com/

  - https://lore.kernel.org/git/Yy4eo6500C0ijhk+@coredump.intra.peff.net/

  - https://lore.kernel.org/git/Y07yeEQu+C7AH7oN@nand.local/

This patch makes those go away by forcing -O0 when compiling with LSan.
There are a few ways we could do this:

  - we could just teach the linux-leaks CI job to set -O0. That's the
    smallest change, and means we wouldn't get spurious CI failures. But
    it doesn't help people looking for leaks manually or in a specific
    test (and because the problem depends on the vagaries of the
    optimizer, investigating these can waste a lot of time in
    head-scratching as the problem comes and goes)

  - we default to -O2 in CFLAGS; we could pull this out to a separate
    variable ("-O$(O)" or something) and modify "O" when LSan is in use.
    This is the most flexible, in that you could still build with "make
    O=2 SANITIZE=leak" if you really wanted to (say, for experimenting).
    But it would also fail to kick in if the user defines their own
    CFLAGS variable, which again leads to head-scratching.

  - we can just stick -O0 into BASIC_CFLAGS when enabling LSan. Since
    this comes after the user-provided CFLAGS, it will override any
    previous -O setting found there. This is more foolproof, albeit less
    flexible. If you want to experiment with an optimized leak-checking
    build, you'll have to put "-O2 -fsanitize=leak" into CFLAGS
    manually, rather than using our SANITIZE=leak Makefile magic.

Since the final one is the least likely to break in normal use, this
patch uses that approach.

The resulting build is a little slower, of course, but since LSan is
already about 2x slower than a regular build, another 10% slowdown isn't
that big a deal.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [AkashiLover/Skyrat-tg](https://github.com/AkashiLover/Skyrat-tg)@[e66aaaa0c2...](https://github.com/AkashiLover/Skyrat-tg/commit/e66aaaa0c257fb021a3aa5d6e3f8910fa599edad)
#### Thursday 2022-10-20 13:06:01 by SkyratBot

[MIRROR] Add speech modifier to zombie tongue [MDB IGNORE] (#16417)

* Add speech modifier to zombie tongue (#69899)

About The Pull Request

A zombie rotten tongue has a complex language modifier.
The language modifier works by:

    All occurrences of characters "eiou" (case-insensitive) are replaced with "r".
    All characters other than "zhrgbmna .!?-" (case-insensitive) are stripped.
    Multiple spaces are replaced with a single.
    Lower-case "r" at the end of words replaced with "rh".
    An "a" or "A" by itself will be replaced with "hra".
    The first character is capitalised.

Some interesting dialogue examples:

    Bab, am gaa habbah abah zah namrh ah Bh!rh!b?
    Bob, are you happy about the death of Philip?

    Zah bang bang man ganna harm mah zambah?
    Will the Zombie Hunter attack me?

    Mah zambah nah harm brazzarz.
    I do not hurt brothers.

    Mah zambah ganna gangbang harmanz zammarrar.
    I will kill humans tomorrow.

    Mah zambah am nah habbah, an mah zambah gab, -Graaaagh!-
    I am not happy, and I say "Graaaagh!"

The language idea was taken from a zombie game back in 2005 called Urban Dead. It's no longer developed and I made all the code myself while following the given language rule structures.

Zombie Speech Translator
Zombie Language Examples
Zombie Dictionary
Why It's Good For The Game
Abracadabra - The Steve Miller Band

    Ah raab zha brahnz ahn zarh hagh, (I love the brains in your head)
    Ah ganna barg abgrah gangbang, (I'm gonna eat them when you're dead)
    Az rahnah zarh ranz ahn hahg ahahz, (Now as you run and hide away)
    Zarh harh mah zambah az hah zahz: (You hear my zombie as he says:)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)

Changelog

cl
add: Rotten zombie tongue has a new speech modifier that converts spoken language into zombie sentences. If the person speaking is a high-functioning zombie this is bypassed.
/cl

* Add speech modifier to zombie tongue

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [sbueringer/cluster-api-provider-aws](https://github.com/sbueringer/cluster-api-provider-aws)@[867afc7ac7...](https://github.com/sbueringer/cluster-api-provider-aws/commit/867afc7ac718621a11e00fc2b05589ac2548d4d5)
#### Thursday 2022-10-20 14:10:57 by Claudia Beresford

Fail apidiff make target when git fails

This is a fairly simple fix to ensure that when `git diff` fails on the
`make apidiff` target, the exit code is actually picked up by make.
Previously the exit code from `diff` was "swallowed" by the `if`.

eg:
```
$ cat Makefile
thing:
        if (exit 1); then \
		echo foo; \
        fi
        echo "still here"

$ make thing
still here
$ echo $?
0
```

What we want:
- exit 1 when `git diff` fails
- exit 0 when `grep` fails
- call `go-apidiff` when `git diff` and `grep` succeeds
- exit 1 when `go-apidiff` fails

This is honestly a complete pain to do in a Makefile.

I tried capturing output, moving everything to a script, calling from
one thing to another. But really this is just tricky to do the way we
want in Make.

So, if we can live with a little repetition, we can do the following:
- Check the `git diff` can run, exit 1 if not
- Run the `git diff` again, this time piping the successful command to
  `grep`
- If `grep` fails, then no worries, the target will roll on and exit 0
  like it always has.
- If `grep` succeeds then the `go-apidiff` tool is called and the target
  runs as intended.

------

In the case of `$(APIDIFF_OLD_COMMIT)`, there is some annoying `make`
magic going on here. Which I can't simply make fail since it will cause any
job which uses something in this Makefile to fail out of proximity.
The `shell` is expanded when the file is loaded meaning even targets
which do not care about the value will end up erroring (but not exiting)
when it fails. These are not errors which impact the target's run, but
they look annoying in CI.

Since this var is only used by `apidiff`, we can move it into that
target so it is only evaluated when specifically called.

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[ea72946bb8...](https://github.com/dsmith328/LC13Master/commit/ea72946bb8a6a62ef557b0226e6240339510f41c)
#### Thursday 2022-10-20 14:40:10 by Lance

Initial Commit

Fairy Festival and Wellcheers

Second Commit

Fairy Festival Final, Bald, and Summon_Backup Fix

Third Commit

Training Rabbit, Spider Bud, Old Lady, Beauty and the Beast, Dingle Dangle

Partial Commit

Crumbling Armor

4th Commit

Crumbling Armor, Bloodbath, and We Can Change Anything

4.1 Commit

Moved to a better place.

Second Commit

White Lake

Temp WL/SG Commit

Second Commit

Silent Girl finish and Red Queen

Small SG Fix

Fixed Proc Call

Removed Commented Code

Removed Redundant Code

Second Commit

Punishing Bird attack chance increase. Tutorial Abnos can't be targetted hit by Pink Midnight. Party Everlasting doesn't move until it's summoned backup. Staining Rose unique buff. Temporary non-breaching.

---
## [hashicorp/terraform-plugin-framework](https://github.com/hashicorp/terraform-plugin-framework)@[b868035519...](https://github.com/hashicorp/terraform-plugin-framework/commit/b8680355191b65ec6ce86c339e57adca46cd624e)
#### Thursday 2022-10-20 14:46:43 by Brian Flad

types: Deprecate Null, Unknown, and Value fields

Reference: https://github.com/hashicorp/terraform-plugin-framework/issues/447

When the framework type system was originally being developed, the value types were introduced with exported fields which also served as the internal details of whether a value was null, unknown, or a known value of a friendlier Go type. It was known that there was the potential for issues, but the simplified developer experience seemed to outweigh the potential for developer issues. Fast forward a few months, this decision appears to have two consequences that the framework maintainers hear about across various forums.

One issue is that the value types directly expose their internal implementation details and support the three states of a Terraform type value: being null, unknown, or a known value. Only one state should ever be set, but provider developers can make a value that is any combination of those states. This makes the framework behavior potentially indeterminate from the provider developer perspective whether, for example, a null AND unknown value becomes null OR unknown as it works its way through the framework.

```go
type ThingResourceModel struct{
  Computed types.String `tfsdk:"computed"`
}

func (r ThingResource) Create(ctx context.Context, req resource.CreateResource, resp *resource.CreateResponse) {
  var data ThingResourceModel

  resp.Diagnostics.Append(req.Plan.Get(ctx, &data)...)

  tflog.Trace(ctx, "Data Values", map[string]any{
    // Unknown value: types.String{Null: false, Unknown: true, Value: ""}
    "computed": plan.Computed,
  })

  // Maybe some external API responses here, but showing hardcoded updates for
  // brevity. This will make the value invalid by enabling Null without
  // disabling Unknown.
  data.Computed.Null = true

  tflog.Trace(ctx, "Data Values", map[string]any{
    // Invalid value: types.String{Null: true, Unknown: true, Value: ""}
    "computed": data.Computed,
  })

  // The invalid value will be either null or unknown, depending on the
  // type implementation. If unknown, Terraform will error, since unknown
  // values are never allowed in state.
  resp.Diagnostics.Append(resp.State.Set(ctx, &data)...)
}
```

Another issue is that the default (zero-value) state for an "unset" value type turns into a known value, which is confusing since these values explicitly support being null. This causes Terraform errors which would surface to practitioners (especially when untested) that provider developers then have to troubleshoot the error message containing Terraform's type system details, potentially discover the reason why it is happening by looking at the framework type source code, then figure out a workable solution. It's not intuitive.

```go
type ThingResourceModel struct{
  // let's assume this is left unconfigured (null in config and plan)
  Optional types.String `tfsdk:"optional"`
}

func (r ThingResource) Create(ctx context.Context, req resource.CreateResource, resp *resource.CreateResponse) {
  // Providers can opt to use a single variable that is updated based on an
  // external response, however that logic can be more difficult sometimes,
  // so it can be easier to split them. Showing the split way to exemplify
  // the "unset" problem.
  var plan, state ThingResourceModel

  resp.Diagnostics.Append(req.Plan.Get(ctx, &plan)...)

  tflog.Trace(ctx, "Plan Values", map[string]any{
    // Null value: types.String{Null: true, Unknown: false, Value: ""}
    "optional": plan.Optional,
  })

  // Maybe some external API responses here, but intentionally not
  // doing any state.Optional setting, which might happen if the
  // external response for that data was null for example.

  tflog.Trace(ctx, "State Values", map[string]any{
    // Zero-value: types.String{Null: false, Unknown: false, Value: ""}
    "optional": state.Optional,
  })

  // The state zero-value will later cause Terraform to error, such as:
  // Error: Provider produced inconsistent result after apply
  // ... expected cty.NullVal(cty.String), got cty.StringVal("")
  // Since the plan value said it would be null.
  resp.Diagnostics.Append(resp.State.Set(ctx, &state)...)
}
```

This deprecation of the fields in preference of functions and methods aims to unexport the internal details and treat the value types as immutable once they are created. When provider developers switch over to the new model, any errant changes to the deprecated exported fields will have no effect. A future version will remove the exported fields entirely and switch the zero-value implementation of these values to being null, instead of a known zero-value of the underlying type.

---
## [reach-sh/reach-lang](https://github.com/reach-sh/reach-lang)@[369d4e327b...](https://github.com/reach-sh/reach-lang/commit/369d4e327bd8239529425b44102f6070d5808589)
#### Thursday 2022-10-20 15:01:23 by William G Hatch

change isDataVariant test to use different length keys

Proving to myself and everybody that I was wrong and temporarily crazy when I wrote that I made a mistake in my implementation of this feature the first time.  I don't remember what I did that made me think there was a bug here.  But now I can rest assured in the knowledge of my own infallibility when writing code, and can view with skepticism any claims from myself or others that there is ever any problem with my code at any time for any reason.

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[c1bd175125...](https://github.com/newstools/2022-express/commit/c1bd175125d4b9d933dbd8b12bd974f0de605584)
#### Thursday 2022-10-20 15:36:10 by Billy Einkamerer

Created Text For URL [www.express.co.uk/entertainment/music/1685501/elvis-presley-girlfriend-wanda-jackson-tribute-album-i-remember-elvis]

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[b4b6636b49...](https://github.com/microsoft/terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Thursday 2022-10-20 16:15:20 by Mårten Rånge

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
## [nextstrain/cli](https://github.com/nextstrain/cli)@[c9ced1a13f...](https://github.com/nextstrain/cli/commit/c9ced1a13f21de86af2ef6a0d1508ad6f31d1b63)
#### Thursday 2022-10-20 17:50:44 by Thomas Sibley

runner.conda: Pin the version of Micromamba used

For the same reason we pin deps with nextstrain-base, this ensures that
`nextstrain setup conda` can't break between one day and the next
because of a new Micromamba release.  This happened during my
development of the Conda runtime with the release of Micromamba 0.26.0¹,
and so has been on my mind to address.

The version used is overridable by an environment variable for debugging
and troubleshooting purposes, but it also serves as an escape hatch for
users stuck on older Nextstrain CLI versions who might need a newer
Micromamba for whatever reason.

We should generally try to keep the pinned version current as long as
new releases work ok.  It's too bad Dependabot doesn't support the Conda
ecosystem.²  If we're bad at remembering to update this over time, we
can setup a GitHub Action workflow to check for new releases and remind
us.

¹ https://github.com/mamba-org/mamba/issues/1979
² https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates#supported-repositories-and-ecosystems

---
## [cgwalters/coreos-assembler](https://github.com/cgwalters/coreos-assembler)@[4e6df71a7f...](https://github.com/cgwalters/coreos-assembler/commit/4e6df71a7fbd520f7fcf0f8a7d2eead2e889ed83)
#### Thursday 2022-10-20 18:31:12 by Colin Walters

Add new `build-cimage` command

This is a big step towards https://github.com/coreos/coreos-assembler/issues/2685

I know there's a lot going on with the pipeline, and I don't
want to conflict with all that work - but at the same time,
in my opinion we are just too dependent on complex Jenkins flows
and our bespoke "meta.json in S3".

The core of CoreOS *is a container image* now.  This new command
adds an opinionated flow where one can do:

```
$ cosa init
$ cosa build-cimage quay.io/cgwalters/ostest
```

And *that's it* - we do proper change detection, reading and
writing from the remote container image.  We don't do silly things
like storing an `.ociarchive` in S3 when we have native registries
available.

Later, we can build on this and rework our disk images to
derive from that container image, as #2685 calls for.

Also in the near term future, I think we can rework `cmd-build`
such that it reuses this flow, but outputs to an `.ociarchive` instead.
However, this code is going to need a bit more work to run in
supermin.

---
## [MemeHoovy/chromatic-scales-and-soundfont](https://github.com/MemeHoovy/chromatic-scales-and-soundfont)@[2432b4a325...](https://github.com/MemeHoovy/chromatic-scales-and-soundfont/commit/2432b4a325d1539574df3995123753eb228020e3)
#### Thursday 2022-10-20 19:18:39 by ToastedNoodles

Merge pull request #2 from MemeHoovy/MemeHoovy-patch-1

The do whatever the fuck you want license

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[06090b9269...](https://github.com/cockroachdb/cockroach/commit/06090b92696bfc4c84f457ac204c4bf17f780170)
#### Thursday 2022-10-20 19:40:25 by craig[bot]

Merge #86603 #87166 #87535 #87870 #88078 #88111

86603: changefeedccl: redact user from confluent schema registry r=jayshrivastava a=jayshrivastava

This change redacts the confluent schema registry key
from the jobs table.

Fixes: https://github.com/cockroachdb/cockroach/issues/85902

Release justification: This change is important because
it prevents a user's secret key from being store in the DB.
The footprint of this change is small as it only touches
a specific changefeed option - confluent schema registry.

Release note (enterprise change): Previously, SHOW CHANGEFEED
JOBS would reveal confluent schema registry user information,
including a user's secret key. This change makes this info
redacted, meaning it will not be stored in CockroachDB
internal tables at all.

87166: kvserver: shorten `raft.process.handleready.latency` help text r=tbg a=erikgrinaker

We should get confirmation in #87112 that this size is below the limit before merging this.

---

AWS managed Prometheus rejects `raft.process.handleready.latency`
because the help text is too long. The text is currently 1123 bytes, so
the limit is suspected to be 1024 bytes. This patch reduces the size of
this help text to 938 bytes.

Resolves #87112.

Release justification: bug fixes and low-risk updates to new functionality

Release note (ops change): Reduced the length of the
`raft.process.handleready.latency` metric help text to avoid it being
rejected by certain Prometheus services.

87535: sql: support `#typeHints` greater than `#placeholders` for prepare stmt r=rafiss a=ZhouXing19

Previous, we only support pgwire prepare stmt with the number of typehints equal or smaller than the number of the placeholders in the query. E.g. the following usage are not supported:

```
Parse {"Name": "s2", "Query": "select $1", "ParameterOIDs":[1043, 1043, 1043]}
```
Where there is 1 placeholder in the query, but 3 type hints.

This commit is to allow mismatching #typeHints and #placeholders. The former can be larger than the latter now.

This feature is needed for [CRDB's support for Hasura GraphQL Engine](https://github.com/hasura/graphql-engine/issues/8839#issuecomment-1236691642).

Release justification: Low risk, high benefit changes to existing functionality

Release note: For pgwire-level prepare statements, add support for the case where the number of the type hints is greater than the number of placeholders in the given query.

87870: kvnemesis: reset op.Result r=erikgrinaker a=tbg

We found out (in #87814) after a wild goose chase that op.Result was not
reset, so unless operations were cognizant of this fact and
always fully repopulated the Result field, weird failures
could result from txn retries.

Reset the field.

Release note: None


88078: ui: update filter labels r=maryliag a=maryliag

Update filter label from "App" to "Application Name" and "Username" to "User Name" on SQL Activity and Insights pages.

Fixes #87960

<img width="467" alt="Screen Shot 2022-09-16 at 6 40 51 PM" src="https://user-images.githubusercontent.com/1017486/190827281-36a9c6df-3e16-4689-bcae-6649b1c2ff86.png">


Release note (ui change): Update filter labels from "App" to "Application Name" and from "Username" to "User Name" on SQL Activity and Insights pages.

88111: sql: fix `pg_get_viewdef` for materialized views r=rafiss a=knz

Fixes #88109.

Release note (bug fix): The function `pg_catalog.pg_get_viewdef` now works properly for materialized views.

Co-authored-by: Jayant Shrivastava <jayants@cockroachlabs.com>
Co-authored-by: Erik Grinaker <grinaker@cockroachlabs.com>
Co-authored-by: Jane Xing <zhouxing@uchicago.edu>
Co-authored-by: Tobias Grieger <tobias.b.grieger@gmail.com>
Co-authored-by: Marylia Gutierrez <marylia@cockroachlabs.com>
Co-authored-by: Raphael 'kena' Poss <knz@thaumogen.net>

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[8a87301c84...](https://github.com/yogstation13/Yogstation/commit/8a87301c84287ec6f2e1549ba3bb67e071065a63)
#### Thursday 2022-10-20 20:26:47 by Vaelophis Nyx

[ASTEROID] Atmos Approved: Atmospherics Changes + More (#16111)

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

* guh

* fuck you mapbot

* need that to breathe!

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

---
## [GillianZech/unc-gamejam-f2022](https://github.com/GillianZech/unc-gamejam-f2022)@[eb8c7f9c0b...](https://github.com/GillianZech/unc-gamejam-f2022/commit/eb8c7f9c0b2ea261487a73063267f2502f492bfd)
#### Thursday 2022-10-20 20:39:00 by Lmonte695

finally did the fucking movement its finished god damn

---
## [kaiocesarb15/Introduction-to-Programming-for-Computer-Engineering](https://github.com/kaiocesarb15/Introduction-to-Programming-for-Computer-Engineering)@[b29112ba81...](https://github.com/kaiocesarb15/Introduction-to-Programming-for-Computer-Engineering/commit/b29112ba81764ce66d88a9a065c148327a20ec30)
#### Thursday 2022-10-20 22:59:00 by Kaio César Barreto

Upload ex011-pIdeal.c

By receiving as input the sex and height of a person, build a program to calculate your ideal weight using the following Instructions:
Ideal weight for men: (72.7*h) - 58, ideal weight for women: (62.1*h) - 44.7 (where h represents the height value in meters).
Recommended steps:
    a. Define the variables. Sex can be stored in a char or in a int, if you prefer.
    b. Read the sex (remember the prompt), if it is char type, the formatter is %c.
        i. It is important that this reading is done first.
    c. Read the height.
    d. Implement the offset with if-else by placing an assignment with different expression in the true and false part, according to
       the condition used and with the corresponding sex.
        i. For simplification, suppose the user will always inform only two options for sex, female or male.
       ii. Alternatively, you can also add two if independent, without the respective else, one for each sex.
    e. Display the calculated optimal weight.

---
## [gitster/git](https://github.com/gitster/git)@[a88ba63cb3...](https://github.com/gitster/git/commit/a88ba63cb31970a5f5df973849d84ff62d0fcb36)
#### Thursday 2022-10-20 23:04:45 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[9b4501d4fe...](https://github.com/Buildstarted/linksfordevs/commit/9b4501d4fe913ac1533a0d3508af3f059113999b)
#### Thursday 2022-10-20 23:07:10 by Ben Dornis

Updating: 10/20/2022 11:00:00 PM

 1. Added: The Raspberry Pi 400 in My Bedroom
    (https://joeldare.com/private-analtyics-and-my-raspberry-pi-400.html)
 2. Added: Applying for a faculty job in CS
    (https://abhvio.us/posts/faculty-job-in-cs/)
 3. Added: How to Make Your Marketing Team More Agile
    (https://brianchristner.io/how-to-make-your-marketing-t-eam-more-agile/)
 4. Added: What if the team hates my functional code?
    (https://jrsinclair.com/articles/2022/what-if-the-team-hates-my-functional-code/)
 5. Added: Syncing Notion databases into Tinybird using notion-objects
    (https://thrau.at/blog/syncing-notion-database-into-tinybird-with-notion-objects-20221017.html)
 6. Added: Support reminder for older versions of Visual Studio
    (https://devblogs.microsoft.com/visualstudio/support-reminder-for-older-versions-of-visual-studio/)
 7. Added: Sharp Tools
    (https://alexcwatt.com/sharp-tools/)
 8. Added: ViewComponent in the Wild I: building modern Rails frontends—Martian Chronicles, Evil Martians’ team blog
    (https://evilmartians.com/chronicles/viewcomponent-in-the-wild-building-modern-rails-frontends)
 9. Added: Launching Useful Sensors!
    (https://petewarden.com/2022/10/20/launching-useful-sensors/)
10. Added: Computability Theory (i): the Halting Problem.
    (https://www.amolas.dev/blog/halting-problem/)
11. Added: Computability Theory (ii): uncomputable numbers.
    (https://www.amolas.dev/blog/uncomputable-numbers/)
12. Added: 10 Choses que Tous les Développeurs de Logiciels Juniors Devraient Savoir pour Réussir - Doumer's Blog
    (https://doumer.me/10-choses-que-tous-les-developpeurs-de-logiciels-juniors-devraient-savoir-pour-reussir/)
13. Added: Friends From First Principles — Simon Berens
    (https://simonberens.me/blog/friends-from-first-principles)
14. Added: 10 Things Every Junior Software Developer Should Know To Be Successful - Doumer's Blog
    (https://doumer.me/10-things-every-junior-software-developers-should-know/)

Generation took: 00:06:59.3240687
 Maintenance update - cleaning up homepage and feed

---
## [Mishuba/Tech](https://github.com/Mishuba/Tech)@[7a60f159be...](https://github.com/Mishuba/Tech/commit/7a60f159be717ebfaf4aa96ff0acefcd5fb4c848)
#### Thursday 2022-10-20 23:17:26 by Mishuba

doing the damn thing tomorrow so hackers you should prepare tonight because I'm back

---

