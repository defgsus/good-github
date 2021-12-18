## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-08-24](docs/good-messages/2021/2021-08-24.md)


2,946,547 events, 1,470,740 push events, 2,334,109 commit messages, 181,077,786 characters


## [jroinc/TerraGov-Marine-Corps](https://github.com/jroinc/TerraGov-Marine-Corps)@[38be00e0a6...](https://github.com/jroinc/TerraGov-Marine-Corps/commit/38be00e0a6f61130b02d6ca447540eb665fa43df)
#### Tuesday 2021-08-24 00:37:00 by jroinc

Adds in a few researchchems

Quietus is a chemical that causes rapid, large amounts of oxyloss upon a patient entering critical condition. It causes trace stamina damage upon initial injection for about 2 minutes, warns the recipient once, then becomes latent. No OD given as generally having more of this is *bad* for you.

Upon the patient becoming unconscious for any reason, the chemical deals 25 oxyloss/tick, which should prevent bodydragging. Note that defibrilation sets the unconscious flag for a few seconds, more-or-less requiring dex+ or hypervene to allow a revive. This may require a rework to function properly, we'll see.

Somolent is a chemical that heals rapidly, as long as the player is unconscious or sleeping. It heals 0.2 points of brute and burn per tick, multiplied by cycle counter, capped at 10 of each via cycle counter. Post-cap it shuts off, as it should already have fully healed the target. No OD as the requirement to sleep is stringent enough. The chemical does not put players to sleep, but can and should be combined with chems that do.

A 2.5u inject heals 3 damage (of both types, for all these listed stats), a 5u inject heals 11 damage, a 7.5u inject heals 24 damage (and is now outhealing other, stacked chems), and a 10u inject 42 damage. A 15u inject heals a total of 93 damage of both types while it processes, and takes 25 ticks to do this. More than that heals progressively faster.

Medical nanites are designed to allow use of blood as a secondary health bar. Upon implantation, they cause a significant amount of damage over approximately five minutes. Once they settle down and are functional, they build up to 30u at 0.5u/tick, using 2 blood/tick to do so.

Upon taking either brute or burn damage while there are more than 5u of medical nanites, they heal 2 points per tick of each, using 1u/tick of nanites, for a total heal ratio of 1 point of damage healed per two units of blood. OD is at 36u, with 1 pt/tick of toxin damage.

Now to add recipies, then figure out how much I screwed this shit up already.

---
## [Techno-code/Techno-code.github.io](https://github.com/Techno-code/Techno-code.github.io)@[c08504eed5...](https://github.com/Techno-code/Techno-code.github.io/commit/c08504eed51691b16be0f77eab500353ae451804)
#### Tuesday 2021-08-24 02:20:49 by Techno-code

how long can this summary go? kagja;gjaljkawdjvnwadafsdjfjjj my butt hurts ooooooooooooooooooooooooooooooooooooooooooooooooooooo  We're no strangers to love You know the rules and so do I A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching but you're too shy to say it Inside we both know what's been going on We know the game and we're gonna play it And if you ask me how I'm feeling Don't tell me you're too blind to see Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye my god

---
## [swbain/relisten-android](https://github.com/swbain/relisten-android)@[f9f111451f...](https://github.com/swbain/relisten-android/commit/f9f111451f0be7bf1b85e337cd99e8ed381d1f66)
#### Tuesday 2021-08-24 04:16:50 by Stephen Bain

multi module di setup!!!! i love it when this shit works!!!!

---
## [jooskim/transport-typescript](https://github.com/jooskim/transport-typescript)@[ec96c97765...](https://github.com/jooskim/transport-typescript/commit/ec96c97765a5707f39b4b15c30858bc1b5cd8320)
#### Tuesday 2021-08-24 04:40:55 by Josh Kim

Buffer sendResponseMessage and its variant methods

Internal testing on VMware Cloud UI revealed that there are certain
conditions that could impact the performance of the Angular change
detection system, or any other frontend frameworks that rely on the
Event Loop of the JS engine.

Currently every message being sent via the `sendResponseMessage()`,
 `sendResponseMessageWithId()` or
`sendResponseMessageWithIdAndVersion()` method is scheduled as a macro
task, which means send message logic shares CPU resources with other
macro tasks like DOM painting or other event handling. This way of
sharing the CPU single thread with other tasks usually is benign enough
not to cause much trouble if any.

However, if 1) the send message method is called in rapid succesion,
and 2) each macro task triggers a compute-intensive task such as a
complete re-render of the view like Angular with default change
detection strategy does, the UI will experience a significant
performance hit that looks like a tight loop that could be observed
in the Chrome Inspect Panel.

A sensible solution to the problem is to buffer the payload by a
certain interval and scheduling the macro tasks by chunks not by
every single entry. By doing this it will limit the impact to the
CPU because now the change detection will happen only as frequently
as the buffer is flushed.

See the attached benchmarks for comparisons in CPU utilization.

Signed-off-by: Josh Kim <kjosh@vmware.com>

---
## [theY4Kman/experimentation](https://github.com/theY4Kman/experimentation)@[67ae7a8927...](https://github.com/theY4Kman/experimentation/commit/67ae7a892746a54d573d7336a22590e27be3e3d3)
#### Tuesday 2021-08-24 08:21:50 by Zach "theY4Kman" Kanzler

fix(mandelbrot): resolve broken zoom-to-mouse; use mouse wheel now

The zoom issue was due to the zoom matrix being in unit scale, instead of in mandelbrot scale. Now, instead of using values between 0.0 and 1.0 for the zoom matrix's x and y, we first translate those values into their corresponding mandelbrot coords. I might be able to get away with avoiding the intermediate normalization, but for now, this settles my biz.

Also, I started experimenting with the colours. At the moment, she calculates the reverse number of iterations in a logarithmic scale (to the base of max # iterations), multiplies that by the highest 24-bit value (rounded to the nearest multiple of 25), and picks apart each 8 bit section into an RGB color. It's sorta psychedelic, and I don't hate it — but I would really like to display something with more depth. Also, I would love to do some kind of anti-aliasing.

---
## [christiankuhl/titanium](https://github.com/christiankuhl/titanium)@[cdde5d3f36...](https://github.com/christiankuhl/titanium/commit/cdde5d3f36f11ed5bb6b37a325df41fff981af5b)
#### Tuesday 2021-08-24 08:41:10 by Christian Kuhl

Fix stupid multithreading bug

If I trestrict QEMU to one core with '-smp 1', there will be no simulated
hardware interrupts, if the only thread it has is currently in a busy loop.
:facepalm:
Thank God I'm the only one on this project...

---
## [ethaninja/gamejam2021](https://github.com/ethaninja/gamejam2021)@[15ab993da6...](https://github.com/ethaninja/gamejam2021/commit/15ab993da6ec68e34e7609d428b6eb1fe10a7d63)
#### Tuesday 2021-08-24 09:09:42 by Me Me Me

Added Enemy Follow Script

It's a bit janky currently but the enemy will now follow the player around.
BE ADVISED: As I configured a lot of this in my scene and didn't make it some damn prefabs it won't work until you link up shit properly. So I will do so now and it shouldn't be a problem.

Also, we need to move the movement/input/etc off the player_model and onto the base of the player :)  The model should only be the model and the parent Player object should drive everything

---
## [PrakharGupta36/Breathe](https://github.com/PrakharGupta36/Breathe)@[898c34c4da...](https://github.com/PrakharGupta36/Breathe/commit/898c34c4dab6b3869828ec8e9ec32d02c1c17fe9)
#### Tuesday 2021-08-24 10:38:53 by prakhar_36

Fuck You I am fucking tired and I am gonna come back tommorow and fix that bug

---
## [h2sm/Photobooth](https://github.com/h2sm/Photobooth)@[2cad3fb6aa...](https://github.com/h2sm/Photobooth/commit/2cad3fb6aaf1d65d33f4adab3073301744414156)
#### Tuesday 2021-08-24 12:55:35 by Egor Fedorenko

Boris Yeltsin said that his biggest mistake was mixing port wine with vodka. My biggest mistake is creating this fucking bullshit. Now i have to end it lol. btw i made deleting files from an admin panel, it looks so sick!! Sheesh.

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[4e7d593cd7...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/4e7d593cd733684017cf8b82a163c67133b294aa)
#### Tuesday 2021-08-24 13:12:56 by AmyBSOD

New monsters

"Omg some of them have 'girl' in their name that's soooooo offensive." Also "where the hell does she find the time to add so much content" well, soon she won't, because her vacation ends today and then the rate of commits will plummet. But no one cares anyway, no one (except a few people who just goof around) is touching this game anymore and therefore no one will ever see any of the level 6+ monsters because the few people who play on esm just for fun will always die before their chars are strong enough to see the higher-level monsters. Yay.

---
## [Mohsenselseleh/CevicalCancer](https://github.com/Mohsenselseleh/CevicalCancer)@[30653d8cbc...](https://github.com/Mohsenselseleh/CevicalCancer/commit/30653d8cbcf3439a41254b313e862c7de6799ab8)
#### Tuesday 2021-08-24 15:17:41 by Mohsen Selseleh

Add files via upload

Cervical-Cancer-Prediction
In this data set, We have to predict the patients who are most likely to suffer from cervical cancer using Machine Learning algorithms for Classifications, Visualizations and Analysis.

Description
Cervical Cancer Risk Factors for Biopsy: This Dataset is Obtained from UCI Repository and kindly acknowledged!

This file contains a List of Risk Factors for Cervical Cancer leading to a Biopsy Examination!

About 11,000 new cases of invasive cervical cancer are diagnosed each year in the U.S. However, the number of new cervical cancer cases has been declining steadily over the past decades. Although it is the most preventable type of cancer, each year cervical cancer kills about 4,000 women in the U.S. and about 300,000 women worldwide. In the United States, cervical cancer mortality rates plunged by 74% from 1955 - 1992 thanks to increased screening and early detection with the Pap test. AGE Fifty percent of cervical cancer diagnoses occur in women ages 35 - 54, and about 20% occur in women over 65 years of age. The median age of diagnosis is 48 years. About 15% of women develop cervical cancer between the ages of 20 - 30. Cervical cancer is extremely rare in women younger than age 20. However, many young women become infected with multiple types of human papilloma virus, which then can increase their risk of getting cervical cancer in the future. Young women with early abnormal changes who do not have regular examinations are at high risk for localized cancer by the time they are age 40, and for invasive cancer by age 50. SOCIOECONOMIC AND ETHNIC FACTORS Although the rate of cervical cancer has declined among both Caucasian and African-American women over the past decades, it remains much more prevalent in African-Americans -- whose death rates are twice as high as Caucasian women. Hispanic American women have more than twice the risk of invasive cervical cancer as Caucasian women, also due to a lower rate of screening. These differences, however, are almost certainly due to social and economic differences. Numerous studies report that high poverty levels are linked with low screening rates. In addition, lack of health insurance, limited transportation, and language difficulties hinder a poor woman’s access to screening services. HIGH SEXUAL ACTIVITY Human papilloma virus (HPV) is the main risk factor for cervical cancer. In adults, the most important risk factor for HPV is sexual activity with an infected person. Women most at risk for cervical cancer are those with a history of multiple sexual partners, sexual intercourse at age 17 years or younger, or both. A woman who has never been sexually active has a very low risk for developing cervical cancer. Sexual activity with multiple partners increases the likelihood of many other sexually transmitted infections (chlamydia, gonorrhea, syphilis).Studies have found an association between chlamydia and cervical cancer risk, including the possibility that chlamydia may prolong HPV infection. FAMILY HISTORY Women have a higher risk of cervical cancer if they have a first-degree relative (mother, sister) who has had cervical cancer. USE OF ORAL CONTRACEPTIVES Studies have reported a strong association between cervical cancer and long-term use of oral contraception (OC). Women who take birth control pills for more than 5 - 10 years appear to have a much higher risk HPV infection (up to four times higher) than those who do not use OCs. (Women taking OCs for fewer than 5 years do not have a significantly higher risk.) The reasons for this risk from OC use are not entirely clear. Women who use OCs may be less likely to use a diaphragm, condoms, or other methods that offer some protection against sexual transmitted diseases, including HPV. Some research also suggests that the hormones in OCs might help the virus enter the genetic material of cervical cells. HAVING MANY CHILDREN Studies indicate that having many children increases the risk for developing cervical cancer, particularly in women infected with HPV. SMOKING Smoking is associated with a higher risk for precancerous changes (dysplasia) in the cervix and for progression to invasive cervical cancer, especially for women infected with HPV. IMMUNOSUPPRESSION Women with weak immune systems, (such as those with HIV / AIDS), are more susceptible to acquiring HPV. Immunocompromised patients are also at higher risk for having cervical precancer develop rapidly into invasive cancer. DIETHYLSTILBESTROL (DES) From 1938 - 1971, diethylstilbestrol (DES), an estrogen-related drug, was widely prescribed to pregnant women to help prevent miscarriages. The daughters of these women face a higher risk for cervical cancer. DES is no longer prsecribed.

---
## [aliz0908/Fylo-Dark-Theme-Landing-Page](https://github.com/aliz0908/Fylo-Dark-Theme-Landing-Page)@[f867a3e139...](https://github.com/aliz0908/Fylo-Dark-Theme-Landing-Page/commit/f867a3e139039acda06eade4e3030e50732dc521)
#### Tuesday 2021-08-24 16:01:59 by aliz0908

Update README.md

# Frontend Mentor - Fylo dark theme landing page

![Design preview for the Fylo dark theme landing page challenge](./design/desktop-preview.jpg)

## Welcome! 👋

Thanks for checking out this front-end coding challenge.

[Frontend Mentor](https://www.frontendmentor.io) challenges help you improve your coding skills by building realistic projects.

**To do this challenge you need a basic understanding of HTML and CSS.**

## The challenge

Your challenge is to build out this landing page and get it looking as close to the design as possible.

You can use any tools you like to help you complete the challenge. So if you've got something you'd like to practice, feel free to give it a go.

Your users should be able to: 

- View the optimal layout for the site depending on their device's screen size
- See hover states for all interactive elements on the page

Want some support on the challenge? [Join our Slack community](https://www.frontendmentor.io/slack) and ask questions in the **#help** channel.

## Where to find everything

Your task is to build out the project to the designs inside the `/design` folder. You will find both a mobile and a desktop version of the design. 

The designs are in JPG static format. Using JPGs will mean that you'll need to use your best judgment for styles such as `font-size`, `padding` and `margin`. 

If you would like the design files (we provide Sketch & Figma versions) to inspect the design in more detail, you can [subscribe as a PRO member](https://www.frontendmentor.io/pro).

You will find all the required assets in the `/images` folder. The assets are already optimized.

There is also a `style-guide.md` file containing the information you'll need, such as color palette and fonts.

## Building your project

Feel free to use any workflow that you feel comfortable with. Below is a suggested process, but do not feel like you need to follow these steps:

1. Initialize your project as a public repository on [GitHub](https://github.com/). Creating a repo will make it easier to share your code with the community if you need help. If you're not sure how to do this, [have a read-through of this Try Git resource](https://try.github.io/).
2. Configure your repository to publish your code to a web address. This will also be useful if you need some help during a challenge as you can share the URL for your project with your repo URL. There are a number of ways to do this, and we provide some recommendations below.
3. Look through the designs to start planning out how you'll tackle the project. This step is crucial to help you think ahead for CSS classes to create reusable styles.
4. Before adding any styles, structure your content with HTML. Writing your HTML first can help focus your attention on creating well-structured content.
5. Write out the base styles for your project, including general content styles, such as `font-family` and `font-size`.
6. Start adding styles to the top of the page and work down. Only move on to the next section once you're happy you've completed the area you're working on.

## Deploying your project

As mentioned above, there are many ways to host your project for free. Our recommend hosts are:

- [GitHub Pages](https://pages.github.com/)
- [Vercel](https://vercel.com/)
- [Netlify](https://www.netlify.com/)

You can host your site using one of these solutions or any of our other trusted providers. [Read more about our recommended and trusted hosts](https://medium.com/frontend-mentor/frontend-mentor-trusted-hosting-providers-bf000dfebe).

## Create a custom `README.md`

We strongly recommend overwriting this `README.md` with a custom one. We've provided a template inside the [`README-template.md`](./README-template.md) file in this starter code.

The template provides a guide for what to add. A custom `README` will help you explain your project and reflect on your learnings. Please feel free to edit our template as much as you like.

Once you've added your information to the template, delete this file and rename the `README-template.md` file to `README.md`. That will make it show up as your repository's README file.

## Submitting your solution

Submit your solution on the platform for the rest of the community to see. Follow our ["Complete guide to submitting solutions"](https://medium.com/frontend-mentor/a-complete-guide-to-submitting-solutions-on-frontend-mentor-ac6384162248) for tips on how to do this.

Remember, if you're looking for feedback on your solution, be sure to ask questions when submitting it. The more specific and detailed you are with your questions, the higher the chance you'll get valuable feedback from the community.

## Sharing your solution

There are multiple places you can share your solution:

1. Share your solution page in the **#finished-projects** channel of the [Slack community](https://www.frontendmentor.io/slack). 
2. Tweet [@frontendmentor](https://twitter.com/frontendmentor) and mention **@frontendmentor**, including the repo and live URLs in the tweet. We'd love to take a look at what you've built and help share it around.
3. Share your solution on other social channels like LinkedIn.
4. Blog about your experience building your project. Writing about your workflow, technical choices, and talking through your code is a brilliant way to reinforce what you've learned. Great platforms to write on are [dev.to](https://dev.to/), [Hashnode](https://hashnode.com/), and [CodeNewbie](https://community.codenewbie.org/).

We provide templates to help you share your solution once you've submitted it on the platform. Please do edit them and include specific questions when you're looking for feedback. 

The more specific you are with your questions the more likely it is that another member of the community will give you feedback.

## Got feedback for us?

We love receiving feedback! We're always looking to improve our challenges and our platform. So if you have anything you'd like to mention, please email hi[at]frontendmentor[dot]io.

This challenge is completely free. Please share it with anyone who will find it useful for practice.

**Have fun building!** 🚀

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[11a7b83d4d...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/11a7b83d4dd8e34a75c199d2eb131f866fee835e)
#### Tuesday 2021-08-24 18:20:50 by AmyBSOD

More new monsters

Yeah I know, they're sooooo offensive and I'm such a bad, stupid, evil or whatever person. Blah to that I say, like I would care at this point. SLEX ain't gonna make a comeback on that server, that's for sure. Anyway, this is the last commit before my vacation ends, so from this point on I'll probably not be able to pump out nearly as many commits for a while.

---
## [Gmk07/apps](https://github.com/Gmk07/apps)@[54b3e13138...](https://github.com/Gmk07/apps/commit/54b3e1313845b1547c7eaa7fd30de01ac3f78c56)
#### Tuesday 2021-08-24 18:51:02 by Gmk07

Update sausage.json

{
"bodies": [
{
"step": "The Baby In Yellow 2 Tips (Unofficial) : It's Guide and Free The Baby In Yellow 2 Tips (Unofficial) 202for Free Games has a horror school in which there are many rooms. Each room of this scary granny creepy fun game has an unsolved mystery that you have to solve for your revenge.Every room of this scary nun horror school game will reveal Scary Teacher Halloween Secrets that help you to complete the given tasks. Be careful and avoid to catch by your creepy horror school teacher in this horror survival game."
},
{
"step": "Story is about a The Baby In Yellow 2 Tips (Unofficial) for Free and her worst high school experience with naughty children. Say Goodbye to creepy teacher and go with your activities. Scary teacher 3D game is waiting for you, your survival in this spooky game depends on the teacher around you. Don’t get frightened from the scary creepy teacher during act."
},
{
"step": "Move to The Baby In Yellow 2 Tips (Unofficial)creepy house and pick the items from there. Extreme missions in The Baby In Yellow 2 Tips (Unofficial) to detract her and caught her households for the fun and for the thrills…"
},
{
"step": "Features :\n- Open World style haunted school\n- Different rooms with different unsolved stories\n- Horror themes and Easy controls\n- Scary ghost game missions\n- High-quality 3d Graphics and Realistic Sounds\n- Interesting Scared activities and addictive stories\nDISCLAMER!\n- We are not affiliated with Scary Teacher 3D game or Z & K Games company\n- The app maybe will not work on all devices"
}
],
"admob_banner": "",
"admob_inter": "",
"facebook_banner": "",
"facebook_inter": "",
"sorryMessage": "We Are Sorry, The Application Not Available for this time, we are update our system, you can check the app after 24h, you can install the version pro.",
"popAppLink": "h",
"popAppName": "Les De",
"popAppImage": "rw",
"popAppPackage": "",
"URL_APP": "s1=",
"popAppIsActive": false,
"APP_KEY": ""
"BANNER_PLACEMENT": "DefaultBanner",
"INTERSTITIAL_PLACEMENT": "DefaultInterstitial",
"whichAds": 0
}

---
## [MariaMod/Young-Maria](https://github.com/MariaMod/Young-Maria)@[6b51514094...](https://github.com/MariaMod/Young-Maria/commit/6b515140942f2feee1f59b02617a470fa2802dd3)
#### Tuesday 2021-08-24 20:05:27 by MilkyNail (MariaMod)

Add files via upload

- School WCs no longer teleport you to the Night Club (I wish we had such bugs in real life)
- Now you can make abort in Family Bitch mode. It will cost the same $700
- Changed the pregnancy chance checking system. This will allow to increase/decrease the chance easier in the future (I have one idea..)
- I removed one anti-grind system implemented by someone without my knowledge
- Fixed the error that caused that pop-up window in the "Mother after dad's laps" scene
- Made a few cosmetic changes
- Fixed an error with infinitely masturbating brother
- Added a small secret you need to find (it's not that hard and pretty useless)
- Hid some code players don't need to see (my bad)
- Removed a few webcam options from the list of what you can do on cam
- Now training will take only 30 points of Energy, and showering at the gym doesn't require shampoo. I also started to work on an NSFW scene there, but it's not finished yet
- Added another 6 gifs to webcam actions

---
## [kittstone/AxionPlus](https://github.com/kittstone/AxionPlus)@[2dcbbd4bc9...](https://github.com/kittstone/AxionPlus/commit/2dcbbd4bc9a77dd3125d400a23bb0664c4cea82c)
#### Tuesday 2021-08-24 20:22:28 by kittstone

FUCK FUCXK FUCK FUCK SHIT SHIT SHIT SHIT FUCK ASS DAMN IT :grief:

---
## [SAMTOMINDUSTRYS/stex2s-python](https://github.com/SAMTOMINDUSTRYS/stex2s-python)@[b6cdd131e3...](https://github.com/SAMTOMINDUSTRYS/stex2s-python/commit/b6cdd131e3bf70be8e7e8d0d9bf14c8d9ea02780)
#### Tuesday 2021-08-24 20:35:25 by Sam Nicholls

holy shit i just wanted to read from the fucking terminal

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[808abcf76f...](https://github.com/Buildstarted/linksfordevs/commit/808abcf76f9c2c53d4ef021f8bf8cc33cbe16c97)
#### Tuesday 2021-08-24 22:09:37 by Ben Dornis

Updating: 8/24/2021 10:00:00 PM

 1. Added: I used to love Bootstrap. God, now I just hate it
    (https://ruky.me/2021/08/24/i-used-to-love-bootstrap-god-now-i-just-hate-it/)
 2. Added: The most underused browser feature
    (https://frankgroeneveld.nl/2021/08/24/most-underused-browser-feature/)
 3. Added: The Rise Of User-Hostile Software
    (https://den.dev/blog/user-hostile-software/)
 4. Added: Tools for thinking
    (https://www.juliendesrosiers.com/2021/08/21/tools-for-thinking.php)
 5. Added: Record and publish your meeting
    (https://beny23.github.io/posts/screen_record_meetings/)
 6. Added: Samsung Supports Retailers Affected By Looting  With Innovative Television Block Function
    (https://news.samsung.com/za/samsung-supports-retailers-affected-by-looting-with-innovative-television-block-function)
 7. Added: My Journey as a Self-Taught Programmer
    (https://blog.octachart.com/my-journey-as-a-self-taught-programmer)
 8. Added: Launching a mobile app, frustration, and creativity - making my own luck
    (https://troyshu.com/2021/08/24/launching-a-mobile-app-frustration-and-creativity/)

Generation took: 00:09:27.0133980
 Maintenance update - cleaning up homepage and feed

---
## [facebookincubator/OnlineSchemaChange](https://github.com/facebookincubator/OnlineSchemaChange)@[917e8ae8ea...](https://github.com/facebookincubator/OnlineSchemaChange/commit/917e8ae8ea11d9e7fd5d201da9974e883fac0d42)
#### Tuesday 2021-08-24 22:31:18 by Srinivasan Mohan

Part1: Parse `partitions` config

Summary:
* Basic partitions parsing support
* String to `pyparsing.ParseResults` alone for now (`model` TODO which should wrap around all the complexity)
* What is supported:
  * hash/key/range/list type partitions (+linear or columns type modifiers)
  * partitions definitions
* What is not supported
  * subpartitions
  * any partition definition property other than `ENGINE` / `COMMENT`
* Parsing the `expr` for a `HASH` type partition is weird and ugly. If theres a cleaner way, I would love to do it right!

While this adds to `sqlparse.create` - the partitions parser is still quite separate and does not get called by the "main" table parsing logic. I will do that once we have a proper `models.PartitionConfig` setup. Grammar as defined in https://dev.mysql.com/doc/refman/8.0/en/create-table.html

Reviewed By: cenalulu

Differential Revision: D30443348

fbshipit-source-id: 04339284d9c69f0f0a4a8c8bc61a6c9ad5057e0f

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6e3b74da04...](https://github.com/tgstation/tgstation/commit/6e3b74da049698fb186be306eb2d317c7e697107)
#### Tuesday 2021-08-24 22:38:29 by Colovorat

Fixes cable merging, changes merging code just a little bit (#60997)

Makes stack code support merging two different stacks with the same mats, but different mats_per_unit numbers by implementing averages.

It's in an attempt to support the stupid efficiency shit that protolathes do. It's not great, but it ought to work alright for now. Kinda a bandaid
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [asigalov61/Optimus-VIRTUOSO](https://github.com/asigalov61/Optimus-VIRTUOSO)@[35fd37b5b9...](https://github.com/asigalov61/Optimus-VIRTUOSO/commit/35fd37b5b92b69987f26593e95c819c8eb5dfca8)
#### Tuesday 2021-08-24 23:57:15 by Alex

Another beautiful RGA output sample

This was was generated from 0 (random seeding). You can see the pure original improvisation by the model in the very beginning. And then it of course resolves into what it remembers once the spooky (latent) memory saturates. WOW!! Absolutely amazing if you ask me!!!

As always performance is incredible and it only takes ~10 minutes to generate 15 minutes (faster-than-real-time for music, lol)

Enjoy! :)

---

